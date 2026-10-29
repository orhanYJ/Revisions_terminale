"""Génère un épisode de série philo : voix, musique, calage des visuels, données du lecteur.

Usage (depuis la racine du dépôt) :
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 outils/serie-philo/generer.py liberte_1

Lit outils/serie-philo/<module>.py (texte lu + visuels), enregistre chaque passage avec les voix neuronales
Microsoft (paquet edge-tts, voir outils/cartes-animees/voix.py), récupère l'instant de chaque mot, et écrit :
  philo/serie/<code>.data.js            données du lecteur (scènes, visuels calés, sous-titres, quiz)
  philo/serie/voix/<code>-v-<h>.mp3     voix seule
  philo/serie/voix/<code>-m-<h>.mp3     voix + musique + bruitages
Les passages déjà enregistrés sont gardés dans outils/serie-philo/.cache (non versionné).
"""
import asyncio, hashlib, importlib, json, os, re, subprocess, sys, wave

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import musique  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "philo", "serie")
CACHE = os.path.join(ICI, ".cache")
SR = musique.SR

VOIX = {"H": "fr-FR-RemyMultilingualNeural", "C": "fr-FR-VivienneMultilingualNeural"}
PROSODIE = {"H": {"rate": "+0%", "pitch": "+0Hz"}, "C": {"rate": "-6%", "pitch": "+0Hz"}}
ECART = {"H": 0.38, "C": 0.95}       # silence après un passage
AVANT_CIT = 0.45                      # silence avant une citation
CARTON = 2.9                          # durée d'un carton de chapitre
DEBUT = 1.6                           # musique seule avant la première phrase
ROMAINS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
V_MOTEUR = 1                          # à incrémenter quand moteur.js ou moteur.css change (et le cache de philo/sw.js)
PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0b111e">
<title>{titre}</title>
<link rel="stylesheet" href="fonts.css?v={vm}">
<link rel="stylesheet" href="moteur.css?v={vm}">
</head>
<body>
<div id="serie"></div>
<script src="{code}.data.js?v={v}"></script>
<script src="moteur.js?v={vm}"></script>
<script>SERIE.lancer(window.EPISODE);</script>
</body>
</html>
"""
MARQUE = re.compile(r"\{(-?)([\w.]+)\}")


def _nettoie(texte):
    """Retire les repères ; renvoie le texte lu et la position (dans ce texte) de chaque repère."""
    out, reperes, pos = [], [], 0
    for m in MARQUE.finditer(texte):
        out.append(texte[pos:m.start()])
        reperes.append((len("".join(out)), m.group(1) == "-", m.group(2)))
        pos = m.end()
    out.append(texte[pos:])
    lu = re.sub(r"\s+", " ", "".join(out))
    return lu, reperes


async def _synth(texte, voix, rate, pitch, chemin):
    import edge_tts
    mots = []
    for essai in range(5):
        try:
            c = edge_tts.Communicate(texte, voix, rate=rate, pitch=pitch,
                                     proxy=os.environ.get("HTTPS_PROXY"), boundary="WordBoundary")
            mots = []
            with open(chemin + ".part", "wb") as f:
                async for ch in c.stream():
                    if ch["type"] == "audio":
                        f.write(ch["data"])
                    elif ch["type"] == "WordBoundary":
                        mots.append((ch["offset"] / 1e7, ch["duration"] / 1e7, ch["text"]))
            os.replace(chemin + ".part", chemin)
            with open(chemin + ".json", "w", encoding="utf-8") as f:
                json.dump(mots, f, ensure_ascii=False)
            return
        except Exception:
            if essai == 4:
                raise
            await asyncio.sleep(2 * (essai + 1))


def _pcm(mp3):
    wav = mp3[:-4] + ".wav"
    if not os.path.exists(wav):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", str(SR), wav], check=True)
    with wave.open(wav) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768.0


def _rogne(x):
    """Retire le silence de tête et de queue (seuil bas) ; renvoie le signal et le décalage de tête en s."""
    seuil = 0.004
    idx = np.where(np.abs(x) > seuil)[0]
    if len(idx) == 0:
        return x, 0.0
    a = max(0, idx[0] - int(0.03 * SR))
    b = min(len(x), idx[-1] + int(0.08 * SR))
    return x[a:b], a / SR


def _aligne(lu, mots):
    """Position de chaque mot (offset, durée, texte) dans le texte lu."""
    res, p = [], 0
    for off, dur, w in mots:
        i = lu.find(w, p)
        if i < 0:
            i = lu.lower().find(w.lower(), p)
        if i < 0:
            continue
        res.append((i, off, dur, w))
        p = i + len(w)
    return res


def _beats(scene):
    for b in scene["beats"]:
        if isinstance(b, str):
            yield {"v": "H", "t": b, "pros": {}}
        elif b[0] == "P":
            yield {"pause": b[1]}
        elif b[0] == "C":
            yield {"v": "C", "t": b[1], "vis": b[2], "pros": b[3] if len(b) > 3 else {}}
        else:
            yield {"v": "H", "t": b[0], "pros": b[1]}


def generer(nom_module):
    ep = importlib.import_module(nom_module)
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(os.path.join(SORTIE, "voix"), exist_ok=True)

    # 1. enregistrer tous les passages manquants
    a_faire, passages = [], []
    for sc in ep.SCENES:
        sc["_b"] = list(_beats(sc))
        for b in sc["_b"]:
            if "pause" in b:
                continue
            lu, _ = _nettoie(b["t"])
            b["lu"] = lu
            if not lu.strip():
                continue
            pros = dict(PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            chemin = os.path.join(CACHE, cle + ".mp3")
            b["fichier"] = chemin
            passages.append(b)
            if not os.path.exists(chemin):
                a_faire.append((lu, VOIX[b["v"]], pros["rate"], pros["pitch"], chemin))
    if a_faire:
        print(f"enregistrement de {len(a_faire)} passages…")

        async def tout():
            sem = asyncio.Semaphore(4)

            async def un(args):
                async with sem:
                    await _synth(*args)
            await asyncio.gather(*[un(a) for a in a_faire])
        asyncio.run(tout())

    # 2. frise temporelle
    t = DEBUT
    voix = []                 # (instant, signal)
    paroles = []              # intervalles parlés (pour la musique)
    bruitages = []            # (instant, nom)
    scenes, vis, sous = [], [], []
    cues = {}                 # id -> instant ; "id.k" -> instant ; "-id" -> instant
    cit_mots = {}
    n_chap = 0
    for sc in ep.SCENES:
        t0 = t
        carton = sc.get("carton", True)
        if carton:
            vis.append({"id": "_chap_" + sc["id"], "type": "chapitre", "scene": sc["id"],
                        "num": ROMAINS[n_chap], "t": sc["chap"], "t0": round(t, 3), "t1": round(t + CARTON - 0.2, 3)})
            bruitages.append((t, "souffle"))
            n_chap += 1
            t += CARTON
        for b in sc["_b"]:
            if "pause" in b:
                t += b["pause"]
                continue
            lu, reperes = _nettoie(b["t"])
            if not lu.strip():
                for _, cache, ident in reperes:
                    cues[("-" if cache else "") + ident] = t
                continue
            if b["v"] == "C":
                t += AVANT_CIT
            x = _pcm(b["fichier"])
            x, tete = _rogne(x)
            with open(b["fichier"] + ".json", encoding="utf-8") as f:
                mots = json.load(f)
            al = _aligne(lu, mots)
            dur = len(x) / SR
            for pos, cache, ident in reperes:
                w = next((a for a in al if a[0] >= pos), None)
                inst = t + (w[1] - tete if w else dur)
                cues[("-" if cache else "") + ident] = max(t, inst)
            if b["v"] == "C":
                cues[b["vis"]] = t - 0.25
                cit_mots[b["vis"]] = {"t0": round(t, 3), "t1": round(t + dur, 3),
                                      "m": [[round(t + a[1] - tete, 3), a[3]] for a in al]}
                bruitages.append((t - 0.3, "cloche"))
            voix.append((t, x))
            paroles.append((t, t + dur))
            # sous-titres : morceaux de phrase de 90 caractères au plus
            morceau, debut = [], None
            for i, (pos, off, d, w) in enumerate(al):
                if debut is None:
                    debut = t + off - tete
                morceau.append(w)
                fin_phrase = re.search(r"[.?!…:;]$", lu[pos:pos + len(w) + 1].strip()) is not None
                txt = " ".join(morceau)
                if fin_phrase or len(txt) > 78 or i == len(al) - 1:
                    a_suivre = al[i + 1] if i + 1 < len(al) else None
                    fin = t + (a_suivre[1] - tete if a_suivre else dur)
                    s = lu[al[i - len(morceau) + 1][0]:pos + len(w)]
                    # récupère la ponctuation qui suit le dernier mot
                    reste = re.match(r"[^\w«]*", lu[pos + len(w):]).group(0).rstrip()
                    sous.append([round(debut, 3), round(min(fin, t + off - tete + d + 0.6), 3), (s + reste).strip()])
                    morceau, debut = [], None
            t += dur + ECART[b["v"]]
        scenes.append({"id": sc["id"], "chap": sc["chap"], "fond": sc.get("fond", "nuit"),
                       "t0": round(t0, 3), "t1": round(t, 3)})
        # visuels de la scène
        for ident, spec in sc["vis"].items():
            if ident not in cues:
                raise SystemExit(f"visuel {ident} (scène {sc['id']}) jamais appelé dans le texte")
            v = dict(spec)
            v["id"], v["scene"] = ident, sc["id"]
            v["t0"] = round(cues[ident], 3)
            v["t1"] = round(cues.get("-" + ident, t), 3)
            etapes = {k.split(".", 1)[1]: round(x, 3) for k, x in cues.items()
                      if k.startswith(ident + ".") and not k.startswith("-")}
            if etapes:
                v["et"] = etapes
            if ident in cit_mots:
                v.update(cit_mots[ident])
                v["t"] = next(b["t"] for b in sc["_b"] if b.get("vis") == ident)
            vis.append(v)
    duree = t + 0.5
    bruitages.append((next(v["t0"] for v in vis if v["type"] == "titre"), "cloche"))

    # 3. pistes audio
    n = int(duree * SR) + SR
    pv = np.zeros(n)
    for inst, x in voix:
        i = int(inst * SR)
        pv[i:i + len(x)] += x
    crete = np.abs(pv).max()
    pv *= 0.89 / crete
    mus = musique.boucle(duree + 1)[:n]
    mus = mus / (np.abs(mus).max() + 1e-9) * 0.42
    g = musique.enveloppe(n / SR, paroles, haut=1.0, bas=0.12)
    g = np.pad(g, (0, max(0, n - len(g))), constant_values=g[-1])[:n]
    # fondu d'entrée et de sortie de la musique
    tt = np.arange(n) / SR
    g *= np.clip(tt / 1.2, 0, 1) * np.clip((duree + 0.5 - tt) / 3.0, 0, 1)
    fx = np.zeros(n)
    for inst, nom in bruitages:
        s = musique.souffle() if nom == "souffle" else musique.cloche()
        i = max(0, int(inst * SR))
        j = min(n, i + len(s))
        fx[i:j] += s[:j - i] * (0.55 if nom == "souffle" else 0.35)
    pm = pv + mus * g + fx
    pm *= 0.95 / max(1e-9, np.abs(pm).max())
    # saturation douce : environ 3 dB de volume en plus, utile sur un haut-parleur de téléphone
    pv = np.tanh(1.6 * pv) / np.tanh(1.6)
    pm = np.tanh(1.6 * pm) / np.tanh(1.6)
    pv = pv[:int(duree * SR)]
    pm = pm[:int(duree * SR)]

    h = hashlib.sha1(pm.tobytes()[::97]).hexdigest()[:8]
    for f in os.listdir(os.path.join(SORTIE, "voix")):
        if f.startswith(ep.CODE + "-"):
            os.remove(os.path.join(SORTIE, "voix", f))
    noms = {}
    for cle, sig, debit in (("voix", pv, "48k"), ("mix", pm, "64k")):
        nomf = f"{ep.CODE}-{cle[0]}-{h}.mp3"
        wav = os.path.join(CACHE, "tmp.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes((np.clip(sig, -1, 1) * 32767).astype(np.int16).tobytes())
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-codec:a", "libmp3lame", "-b:a", debit,
                        os.path.join(SORTIE, "voix", nomf)], check=True)
        noms[cle] = "voix/" + nomf

    data = {"code": ep.CODE, "notion": ep.NOTION, "num": ep.NUM, "titre": ep.TITRE, "suivant": ep.SUIVANT,
            "dur": round(duree, 3), "audio": noms, "scenes": scenes, "vis": vis, "sous": sous,
            "quiz": [dict(q, voir=cues.get(q["voir"])) if q.get("voir") else q for q in ep.QUIZ],
            "credits": getattr(ep, "CREDITS", [])}
    js = ("// Généré par outils/serie-philo/generer.py depuis " + nom_module + ".py : ne pas modifier à la main.\n"
          "window.EPISODE = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
    with open(os.path.join(SORTIE, ep.CODE + ".data.js"), "w", encoding="utf-8") as f:
        f.write(js)
    v = hashlib.sha1(js.encode("utf-8")).hexdigest()[:8]
    page = PAGE.format(titre=f"{ep.NOTION} · Épisode {ep.NUM} — {ep.TITRE}", code=ep.CODE, v=v, vm=V_MOTEUR)
    with open(os.path.join(SORTIE, ep.CODE + ".html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{ep.CODE} : {duree / 60:.1f} min, {len(vis)} visuels, {len(sous)} sous-titres, audio {noms}")


if __name__ == "__main__":
    for m in sys.argv[1:]:
        generer(m)
