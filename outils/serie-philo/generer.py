"""Génère un épisode de série philo : voix, musique, calage des visuels, données du lecteur.

Usage (depuis la racine du dépôt) :
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 outils/serie-philo/generer.py liberte_1
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 outils/serie-philo/generer.py pc_ch4     (vidéo de cours PC)

Le même générateur sert aux vidéos de cours de physique-chimie : leurs scripts sont dans outils/serie-pc/ et portent
SITE = "pc" ; tout est alors écrit dans pc/serie/ (moteur pc/serie/moteur.js, avec ses types propres aux sciences).

Lit outils/serie-philo/<module>.py (texte lu + visuels), enregistre chaque passage, récupère l'instant de chaque mot,
et écrit :
  philo/serie/<code>.data.js            données du lecteur (scènes, visuels calés, sous-titres, quiz)
  philo/serie/voix/<code>-v-<h>.mp3     voix seule
  philo/serie/voix/<code>-m-<h>.mp3     voix + musique + bruitages
Les passages déjà enregistrés sont gardés dans outils/serie-philo/.cache (non versionné).

Voix : MOTEUR = "qwen" (défaut depuis le 30/10/2026) clone localement les voix de voix_ref/ (voir voix_qwen.py,
environ 2 h de calcul par épisode) ; MOTEUR = "edge" reprend les voix Microsoft de l'épisode 1 initial (edge-tts).

Vidéos de cours SVT (05/11/2026, une vidéo par chapitre, scripts dans outils/serie-svt/, SITE = "svt") : sortie dans
svt/serie/ ; moteur svt/serie/moteur.js (copie du moteur PC aux couleurs de la SVT, type mental = carte mentale du
thème 1.A, svt/carte-mentale.js) ; illustrations propres à un chapitre dans svt/serie/illu-<code>.js, chargé s'il existe.

Séries d'histoire DNL (04/11/2026, scripts dans outils/serie-dnl/, SITE = "dnl", LANGUE = "en") : sortie dans dnl/serie/,
type globe (carte animée du chapitre, dnl/cartes/<code>.html, pilotée par le temps de la vidéo).

Vidéos en anglais (04/11/2026, résumé-analyse de Dancing at Lughnasa, scripts dans outils/serie-acl/) : le module porte
LANGUE = "en" et SITE = "acl-lughnasa" ; voix anglaises de voix_ref/ (narrateur_en, cit_en_m, cit_en_f). Une citation
peut être lue par la voix féminine : ("C", texte, id, {"voix": "F"}).
"""
import asyncio, hashlib, importlib, json, os, re, subprocess, sys, wave

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "serie-pc"))
sys.path.insert(2, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "serie-acl"))
sys.path.insert(3, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "serie-dnl"))
sys.path.insert(4, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "serie-svt"))
# autres dossiers de scripts (serie-maths, serie-ses, serie-hggsp…) : trouvés d'office
import glob as _glob  # noqa: E402
sys.path += [d for d in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "serie-*")))
             if os.path.isdir(d) and d not in sys.path]
import musique  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "philo", "serie")
CACHE = os.path.join(ICI, ".cache")
SR = musique.SR

MOTEUR = os.environ.get("SERIE_MOTEUR", "qwen")   # SERIE_MOTEUR=edge : brouillon rapide (voix en ligne) ; =muet : brouillon sans voix ni réseau
VOIX_LANGUE = {
    "fr": ({"H": "narrateur", "C": "citations", "F": "citations"} if MOTEUR == "qwen"
           else {"H": "fr-FR-RemyMultilingualNeural", "C": "fr-FR-VivienneMultilingualNeural", "F": "fr-FR-VivienneMultilingualNeural"}),
    "en": ({"H": "narrateur_en", "C": "cit_en_m", "F": "cit_en_f"} if MOTEUR == "qwen"
           else {"H": "en-GB-RyanNeural", "C": "en-IE-ConnorNeural", "F": "en-IE-EmilyNeural"}),
}
VOIX = dict(VOIX_LANGUE["fr"])
PROSODIE = {"H": {"rate": "+0%", "pitch": "+0Hz"}, "C": {"rate": "-6%", "pitch": "+0Hz"}, "F": {"rate": "-6%", "pitch": "+0Hz"}}
ECART = {"H": 0.38, "C": 0.95, "F": 0.95}       # silence après un passage


def _ecart_vivant(v, lu, k):
    """RYTHME = "vivant" dans un script (SVT, demande de Cengiz du 10/11/2026 : « un rythme vivant ») : le silence après
    un passage du narrateur dépend de la façon dont la phrase finit, au lieu d'un écart fixe ; légère variation
    déterministe (k = rang du passage) pour éviter un tempo de métronome."""
    if v != "H":
        return ECART[v]
    fin = lu.rstrip()[-1:] if lu.strip() else "."
    base = {"?": 0.72, "!": 0.55, ":": 0.26, ",": 0.18, "…": 0.6, ";": 0.3}.get(fin, 0.42)
    if len(lu) < 40 and fin in ".!":     # phrase courte qui claque : on la laisse respirer
        base += 0.12
    return round(base * (0.88 + 0.24 * ((k * 0.6180339) % 1)), 3)
AVANT_CIT = 0.45                      # silence avant une citation
CARTON = 2.9                          # durée d'un carton de chapitre
DEBUT = 1.6                           # musique seule avant la première phrase
ROMAINS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV"]
V_MOTEUR = 12                          # à incrémenter quand moteur.js ou moteur.css change (et le cache de philo/sw.js)
V_MOTEUR_SITE = {"philo": V_MOTEUR, "pc": 2, "acl-lughnasa": 2, "dnl": 3, "svt": 5,
                 "maths": 1, "ses": 1, "hggsp": 1}   # pc/serie/moteur.* (et le cache de pc/sw.js) ; acl-lughnasa/serie/moteur.*
TEINTE = {"philo": "#0b111e", "pc": "#120c07", "acl-lughnasa": "#0e1729", "dnl": "#0e1729", "svt": "#0b120e",
          "maths": "#1b2422", "ses": "#0d1f24", "hggsp": "#141414"}
PAGE = """<!DOCTYPE html>
<html lang="{langue}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="{teinte}">
<title>{titre}</title>
<link rel="stylesheet" href="fonts.css?v={vm}">
<link rel="stylesheet" href="moteur.css?v={vm}">
</head>
<body>
<div id="serie"></div>
<script src="{code}.data.js?v={v}"></script>
{extra}<script src="moteur.js?v={vm}"></script>
{apres}
<script>SERIE.lancer(window.EPISODE);</script>
</body>
</html>
"""
MARQUE = re.compile(r"\{([-!#]?)([^{}]+)\}")
GENERIQUE = 5.6                       # générique commun à la série, avant la première phrase
DUREE_NOTION = 4.5                    # étiquette « Notion · … » quand le texte touche une autre notion ({#le bonheur})
DUREE_NOTIONS = 6.5                   # encadré « Notions abordées » au début d'une partie (champ notions de la scène)
FLASH = 3.8                           # « À retenir » de fin de chapitre (silence de voix, la musique monte)
HUMEUR_DEFAUT = "lumiere"
# prononciation : graphie donnée à la voix pour les mots non français (le texte affiché et les sous-titres gardent
# l'orthographe normale) ; à compléter quand un nom est mal dit (vérifier par la transcription de l'épisode)
PRONONCIATION = {"Leute": "Loïte", "liberi": "libéri"}


def prononce(lu):
    for mot, dit in PRONONCIATION.items():
        lu = re.sub(r"(?<![\w-])" + re.escape(mot) + r"(?![\w-])", dit, lu)
    return lu


def _nettoie(texte):
    """Retire les repères ; renvoie le texte lu et la position (dans ce texte) de chaque repère."""
    out, reperes, pos = [], [], 0
    for m in MARQUE.finditer(texte):
        out.append(texte[pos:m.start()])
        reperes.append((len("".join(out)), m.group(1), m.group(2)))
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
    # décodage en cache, refait si le MP3 a été réenregistré depuis (SERIE_REVOIX, prise refaite)
    if not os.path.exists(wav) or os.path.getmtime(wav) < os.path.getmtime(mp3):
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
    # mots dits selon PRONONCIATION (« Man-choo-kwo ») : on les ramène au mot écrit (« Manchukuo »), sinon
    # le sous-titre perd ou tronque le mot ; les morceaux suivants d'une graphie en plusieurs mots allongent le premier
    inverse = {}
    for mot, dit in PRONONCIATION.items():
        for k, tk in enumerate(re.findall(r"[\wÀ-ÿœæ'’-]+", dit)):
            inverse.setdefault(tk.lower(), (mot, k == 0))
    res, p = [], 0
    for off, dur, w in mots:
        i = lu.find(w, p)
        if i < 0:
            i = lu.lower().find(w.lower(), p)
        if i < 0 and w.lower() in inverse:
            mot, premier = inverse[w.lower()]
            if not premier:
                if res:
                    a = res[-1]
                    res[-1] = (a[0], a[1], round(off + dur - a[1], 3), a[3])
                continue
            i = lu.find(mot, p)
            if i >= 0:
                w = mot
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
            pros = dict(b[3]) if len(b) > 3 else {}
            yield {"v": pros.pop("voix", "C"), "cit": True, "t": b[1], "vis": b[2], "pros": pros}
        else:
            yield {"v": "H", "t": b[0], "pros": b[1]}


def generer(nom_module):
    ep = importlib.import_module(nom_module)
    site = getattr(ep, "SITE", "philo")
    SORTIE = os.path.join(RACINE, site, "serie")
    PRONONCIATION.update(getattr(ep, "PRONONCIATION", {}))   # graphies propres à l'épisode
    langue = getattr(ep, "LANGUE", "fr")
    VOIX.clear(); VOIX.update(VOIX_LANGUE[langue])
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
            lu = prononce(lu)
            b["lu"] = lu
            if not lu.strip():
                continue
            pros = dict(PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([MOTEUR, VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            chemin = os.path.join(CACHE, cle + ".mp3")
            b["fichier"] = chemin
            passages.append(b)
            if not os.path.exists(chemin):
                a_faire.append((lu, VOIX[b["v"]], pros["rate"], pros["pitch"], chemin))
            elif MOTEUR == "qwen" and os.environ.get("SERIE_REVOIX") and not os.path.exists(chemin + ".vu"):
                # SERIE_REVOIX=1 : un passage déjà enregistré mais monocorde est refait (prosodie.py) ; « .vu » = déjà contrôlé
                import prosodie
                try:
                    import librosa
                    y, _sr = librosa.load(chemin, sr=16000, mono=True)
                    pm = prosodie.mesure(y, 16000)
                except Exception:
                    pm = None
                if pm and prosodie.plat(pm):
                    print(f"  monocorde, à refaire (relief {pm['relief']}, élan {pm['elan']}) : {lu[:60]}", flush=True)
                    a_faire.append((lu, VOIX[b["v"]], pros["rate"], pros["pitch"], chemin))
                else:
                    open(chemin + ".vu", "w").close()
    if a_faire and MOTEUR == "qwen":
        import voix_qwen
        print(f"enregistrement de {len(a_faire)} passages (clonage local)…", flush=True)
        for i, (lu, voix, rate, pitch, chemin) in enumerate(a_faire, 1):
            tempo = 1 + float(rate.rstrip("%")) / 100      # le débit seul est repris ; la hauteur suit la voix
            sc = voix_qwen.dire(lu, voix, chemin, tempo=tempo, langue=langue)
            print(f"  {i}/{len(a_faire)} {voix} score {sc:.2f}" + ("  À VÉRIFIER" if sc < 0.85 else "") + f"  {lu[:60]}", flush=True)
        a_faire = []
    if a_faire and MOTEUR == "muet":
        # brouillon sans voix ni réseau : silence d'une durée calée sur le débit moyen du narrateur, mots répartis régulièrement
        for lu, voix, rate, pitch, chemin in a_faire:
            mots = re.findall(r"[\w'’-]+", lu)
            dur = max(0.6, len(mots) / (2.6 if langue == "en" else 2.9))
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{dur:.2f}",
                            "-af", "volume=0", "-b:a", "48k", chemin], check=True)
            pas = dur / max(1, len(mots))
            with open(chemin + ".json", "w", encoding="utf-8") as f:
                json.dump([[round(i * pas, 3), round(pas * .9, 3), m] for i, m in enumerate(mots)], f, ensure_ascii=False)
        a_faire = []
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
    t = GENERIQUE + 0.6
    plein = []                # intervalles où une image occupe tout l'écran (la musique remonte un peu)
    humeurs = []              # (début, humeur) par scène
    voix = []                 # (instant, signal)
    paroles = []              # intervalles parlés (pour la musique)
    bruitages = []            # (instant, nom)
    scenes, vis, sous = [], [], []
    cues = {}                 # id -> instant ; "id.k" -> instant ; "-id" -> instant
    cit_mots = {}
    n_chap = 0
    n_pass = 0
    vivant = getattr(ep, "RYTHME", "") == "vivant"   # silences variables après les passages (voir _ecart_vivant)
    n_frappe = 0
    n_notion = 0
    vis.append({"id": "_generique", "type": "generique", "scene": ep.SCENES[0]["id"], "serie": ep.NOTION,
                "num": ep.NUM, "t0": 0.0, "t1": GENERIQUE})
    bruitages.append((0.15, "souffle"))
    bruitages.append((1.6, "cloche"))
    for sc in ep.SCENES:
        t0 = t
        humeurs.append((t0 if humeurs else 0.0, sc.get("humeur", HUMEUR_DEFAUT)))
        mots_sc = []          # (instant, mot) dits par le narrateur dans la scène
        carton = sc.get("carton", True)
        if carton:
            vis.append({"id": "_chap_" + sc["id"], "type": "chapitre", "scene": sc["id"],
                        "num": ROMAINS[n_chap], "t": sc["chap"], "t0": round(t, 3), "t1": round(t + CARTON - 0.2, 3)})
            bruitages.append((t, "souffle"))
            n_chap += 1
            t += CARTON
        if sc.get("notions"):  # au début de la partie : les notions du programme abordées (la notion de la série en tête)
            vis.append({"id": "_notions_" + sc["id"], "type": "notion", "scene": sc["id"], "titre": "Notions abordées",
                        "items": [ep.NOTION] + [x for x in sc["notions"] if x.lower() != ep.NOTION.lower()],
                        "t0": round(t + 0.4, 3), "t1": round(t + 0.4 + DUREE_NOTIONS, 3)})
        for b in sc["_b"]:
            if "pause" in b:
                t += b["pause"]
                continue
            lu, reperes = _nettoie(b["t"])
            if not lu.strip():
                for _, kind, ident in reperes:
                    if kind == "#":
                        n_notion += 1
                        vis.append({"id": f"_notion{n_notion}", "type": "notion", "scene": sc["id"], "items": [ident],
                                    "t0": round(t, 3), "t1": round(t + DUREE_NOTION, 3)})
                    elif kind == "-":
                        cues.setdefault("-" + ident, t)     # la première fermeture compte
                    else:
                        cues[ident] = t
                continue
            if b.get("cit"):
                t += AVANT_CIT
            x = _pcm(b["fichier"])
            x, tete = _rogne(x)
            with open(b["fichier"] + ".json", encoding="utf-8") as f:
                mots = json.load(f)
            al = _aligne(lu, mots)
            dur = len(x) / SR
            for pos, kind, ident in reperes:
                w = next((a for a in al if a[0] >= pos), None)
                inst = max(t, t + (w[1] - tete if w else dur))
                if kind == "#":       # autre notion du programme touchée ici : une étiquette glisse en haut à droite
                    n_notion += 1
                    vis.append({"id": f"_notion{n_notion}", "type": "notion", "scene": sc["id"], "items": [ident],
                                "t0": round(inst, 3), "t1": round(inst + DUREE_NOTION, 3)})
                    continue
                if kind == "!":       # mot clé qui frappe : grand, une seconde et demie
                    n_frappe += 1
                    vis.append({"id": f"_frappe{n_frappe}", "type": "frappe", "scene": sc["id"], "t": ident,
                                "t0": round(inst, 3), "t1": round(inst + 1.5, 3)})
                    continue
                if kind == "-":
                    cues.setdefault("-" + ident, inst)      # la première fermeture compte
                else:
                    cues[ident] = inst
            if b["v"] == "H":
                mots_sc += [(t + a[1] - tete, a[3]) for a in al]
            if b.get("cit"):
                cues[b["vis"]] = t - 0.25
                cit_mots[b["vis"]] = {"c0": round(t, 3), "c1": round(t + dur, 3),
                                      "m": [[round(t + a[1] - tete, 3), a[3]] for a in al]}
                if "." not in b["vis"]:      # pas de cloche pour une réplique jouée sur le plateau (visuel jeu)
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
            n_pass += 1
            t += dur + (_ecart_vivant(b["v"], lu, n_pass) if vivant else ECART[b["v"]])
        t_parole = t                  # fin de la voix : « À retenir » s'affiche seul
        if sc.get("retenir"):
            vis.append({"id": "_flash_" + sc["id"], "type": "flash", "scene": sc["id"], "t": sc["retenir"],
                        "t0": round(t, 3), "t1": round(t + FLASH - 0.3, 3)})
            bruitages.append((t, "cloche"))
            t += FLASH
        scenes.append({"id": sc["id"], "chap": sc["chap"], "fond": sc.get("fond", "nuit"),
                       "t0": round(t0, 3), "t1": round(t, 3)})
        # visuels de la scène
        for ident, spec in sc["vis"].items():
            if ident not in cues:
                raise SystemExit(f"visuel {ident} (scène {sc['id']}) jamais appelé dans le texte")
            v = dict(spec)
            v["id"], v["scene"] = ident, sc["id"]
            v["t0"] = round(cues[ident], 3)
            v["t1"] = round(cues.get("-" + ident, t if v["type"] == "tableau" else t_parole), 3)
            etapes = {k.split(".", 1)[1]: round(x, 3) for k, x in cues.items()
                      if k.startswith(ident + ".") and not k.startswith("-")}
            if etapes:
                v["et"] = etapes
            if ident in cit_mots:
                v.update(cit_mots[ident])
                v["t"] = next(b["t"] for b in sc["_b"] if b.get("vis") == ident)
            if v.get("cles"):         # mots du visuel qui s'allument quand la voix les prononce
                def _n(x):
                    return re.sub(r"[^a-zàâçéèêëîïôûùüœ]", "", x.lower())
                kt = {}
                for c in v["cles"]:
                    w = next((ti for ti, mo in mots_sc if ti >= v["t0"] - 0.3 and _n(mo).startswith(_n(c)[:max(4, len(_n(c)) - 2)])), None)
                    kt[c] = round(w if w is not None else v["t0"] + 1.0, 3)
                v["kt"] = kt
            if v["type"] == "tableau" and not v.get("fond"):
                plein.append((v["t0"], v["t1"]))
            vis.append(v)
        # écrans vides (DNL, 06/11/2026) : un visuel fermé par un repère reste affiché jusqu'au visuel suivant
        # quand, sinon, l'écran resterait vide plus de 2 s pendant que la voix continue
        if getattr(ep, "COMBLER", site == "dnl"):
            contenu = [v for v in vis if v["scene"] == sc["id"] and v["type"] not in ("chapitre", "notion", "flash", "generique", "frappe", "tag")]
            contenu.sort(key=lambda v: v["t0"])
            for k, v in enumerate(contenu):
                if "-" + v["id"] not in cues:
                    continue
                suite = [w["t0"] for w in contenu[k + 1:] if w["t0"] > v["t1"]]
                autres = [w["t1"] for w in contenu if w is not v and w["t0"] <= v["t1"] < w["t1"]]
                if autres:          # un autre visuel couvre déjà la suite
                    continue
                cible = min(suite) if suite else t_parole
                if 2.0 < cible - v["t1"] < 40:
                    v["t1"] = round(cible, 3)
    duree = t + 0.5
    vis.sort(key=lambda v: (v["t0"], v["type"] != "tableau"))
    bruitages.append((next(v["t0"] for v in vis if v["type"] == "titre"), "cloche"))

    # 3. pistes audio
    n = int(duree * SR) + SR
    pv = np.zeros(n)
    for inst, x in voix:
        i = int(inst * SR)
        pv[i:i + len(x)] += x
    crete = np.abs(pv).max()
    pv *= 0.89 / crete
    # musique : une humeur par chapitre, fondu enchaîné de 2,5 s entre deux humeurs
    pistes = {}
    for _, hu in humeurs:
        if hu not in pistes:
            x = musique.boucle(duree + 1, hu)[:n]
            pistes[hu] = np.pad(x, (0, max(0, n - len(x))))[:n] / (np.abs(x).max() + 1e-9) * 0.42
    tt = np.arange(n) / SR
    mus = np.zeros(n)
    poids_total = np.zeros(n)
    for k, (deb, hu) in enumerate(humeurs):
        fin = humeurs[k + 1][0] if k + 1 < len(humeurs) else n / SR + 5
        w = np.clip((tt - deb + 1.25) / 2.5, 0, 1) * np.clip((fin - tt + 1.25) / 2.5, 0, 1) if k else np.clip((fin - tt + 1.25) / 2.5, 0, 1)
        mus += pistes[hu] * w
        poids_total += w
    mus /= np.maximum(poids_total, 1e-6)
    g = musique.enveloppe(n / SR, paroles, haut=1.0, bas=0.12)
    g = np.pad(g, (0, max(0, n - len(g))), constant_values=g[-1])[:n]
    for a, b in plein:       # images plein écran : la musique remonte un peu sous la voix
        i, j = int(a * SR), int(b * SR)
        g[i:j] = np.maximum(g[i:j], 0.2)
    # danse sur la radio (humeur « reel ») : la musique reste présente sous la voix ; coupure nette au repère « coupe » de la scène
    for k, (deb, hu) in enumerate(humeurs):
        fin = humeurs[k + 1][0] if k + 1 < len(humeurs) else n / SR
        if hu == "reel":
            i, j = int(deb * SR), int(fin * SR)
            g[i:j] = np.maximum(g[i:j], 0.38)
    for sc, s_ in zip(ep.SCENES, scenes):
        if sc.get("coupe") and sc["coupe"] in cues:
            i, j = int(cues[sc["coupe"]] * SR), int(s_["t1"] * SR)
            mus[i:j] = 0
    # fondu d'entrée et de sortie de la musique
    g *= np.clip(tt / 0.4, 0, 1) * np.clip((duree + 0.5 - tt) / 3.0, 0, 1)
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
        wav = os.path.join(CACHE, f"tmp-{ep.CODE}.wav")   # un fichier par épisode : deux générations simultanées ne se gênent pas
        with wave.open(wav, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes((np.clip(sig, -1, 1) * 32767).astype(np.int16).tobytes())
        # volume harmonisé à la norme des vidéos en ligne (-16 LUFS, crêtes à -1,5 dB)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR),
                        "-codec:a", "libmp3lame", "-b:a", debit, os.path.join(SORTIE, "voix", nomf)], check=True)
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
    titre = (f"Chapitre {ep.NUM} — {ep.TITRE} · SVT Terminale" if site == "svt"
             else f"Chapitre {ep.NUM} — {ep.TITRE} · " + {"maths": "Maths", "ses": "SES", "hggsp": "HGGSP"}[site] + " Terminale" if site in ("maths", "ses", "hggsp")
             else f"Chapitre {ep.NUM} — {ep.TITRE} · le cours en vidéo" if site == "pc"
             else f"{ep.NOTION} · Episode {ep.NUM} — {ep.TITRE}" if site == "dnl"
             else f"{ep.NOTION} · Part {ep.NUM} — {ep.TITRE}" if langue == "en" else f"{ep.NOTION} · Épisode {ep.NUM} — {ep.TITRE}")
    extra, apres = "", ""
    if site == "svt":   # carte mentale du thème (type mental) et illustrations propres au chapitre (illu-<code>.js)
        with open(os.path.join(RACINE, "svt", "carte-mentale.js"), "rb") as f:
            extra += f'<script src="../carte-mentale.js?v={hashlib.sha1(f.read()).hexdigest()[:8]}"></script>\n'
    if site in ("svt", "maths", "ses", "hggsp"):   # illustrations (et scènes de carte, HGGSP) propres à la vidéo, si le fichier existe
        illu = os.path.join(SORTIE, "illu-" + ep.CODE + ".js")
        if os.path.exists(illu):
            with open(illu, "rb") as f:
                apres += f'<script src="illu-{ep.CODE}.js?v={hashlib.sha1(f.read()).hexdigest()[:8]}"></script>\n'   # après le moteur : SERIE_OUTILS existe
    page = PAGE.format(titre=titre, code=ep.CODE, v=v, vm=V_MOTEUR_SITE[site], teinte=TEINTE[site], langue=langue, extra=extra, apres=apres)
    with open(os.path.join(SORTIE, ep.CODE + ".html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{ep.CODE} : {duree / 60:.1f} min, {len(vis)} visuels, {len(sous)} sous-titres, audio {noms}")


if __name__ == "__main__":
    for m in sys.argv[1:]:
        generer(m)
