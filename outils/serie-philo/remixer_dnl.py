"""Refait la piste « voix + musique » d'un épisode déjà publié, sans réenregistrer la voix.

Usage : python3 outils/serie-philo/remixer_dnl.py <code> [<code> …]      (ex. h2-2 h2f-2)
(par code d'épisode ; remixer.py, écrit en parallèle pour la physique-chimie, prend des noms de modules)

Part de la piste voix seule publiée (<site>/serie/voix/<code>-v-*.mp3) et de <code>.data.js : intervalles parlés
(sous-titres), cartons, titres, citations, « À retenir » et images plein écran. Les humeurs viennent du script de
l'épisode ; pour les vidéos d'histoire, elles passent par musique.humeur_dnl. Même dosage que generer.py :
musique à −20 dB sous la voix, qui remonte dans les silences, bruitages, saturation douce, −16 LUFS.
Écrit la nouvelle piste <code>-m-<empreinte>.mp3, supprime l'ancienne, met à jour <code>.data.js et l'empreinte
de la page <code>.html. Créé le 10/11/2026 pour donner aux vidéos d'histoire leur musique propre.
"""
import hashlib, importlib, json, os, re, subprocess, sys, wave
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
for d in ("serie-pc", "serie-acl", "serie-dnl", "serie-svt"):
    sys.path.append(os.path.join(RACINE, "outils", d))
import musique  # noqa: E402

SR = musique.SR


def site_de(code):
    for s in ("dnl", "philo", "pc", "svt", "acl-lughnasa"):
        if os.path.exists(os.path.join(RACINE, s, "serie", code + ".data.js")):
            return s
    sys.exit("épisode introuvable : " + code)


def remixer(code):
    site = site_de(code)
    dos = os.path.join(RACINE, site, "serie")
    src = open(os.path.join(dos, code + ".data.js"), encoding="utf-8").read()
    m = re.search(r"window\.EPISODE = (\{.*\});\s*$", src, re.S)
    ep = json.loads(m.group(1))
    mod = importlib.import_module(code.replace("-", "_"))
    hum_script = {s["id"]: (s.get("humeur", "lumiere"), s.get("fond", "nuit")) for s in mod.SCENES}
    duree = ep["dur"]
    n = int(duree * SR) + SR

    # voix seule publiée
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(dos, ep["audio"]["voix"]), "-f", "f32le", "-ac", "1",
                          "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    v = np.frombuffer(pcm, np.float32).astype(float)
    pv = np.zeros(n); pv[:min(n, len(v))] = v[:n]
    pv *= 0.89 / max(1e-9, np.abs(pv).max())

    # humeurs par scène
    humeurs = []
    for s in ep["scenes"]:
        hu, fond = hum_script.get(s["id"], ("lumiere", "nuit"))
        if site == "dnl":
            hu = musique.humeur_dnl(hu, fond, code)
        humeurs.append((s["t0"] if humeurs else 0.0, hu))
    paroles = [(a, b) for a, b, _ in ep["sous"]]
    plein, bruit = [], [(0.15, "souffle"), (1.6, "cloche")]
    for x in ep["vis"]:
        if x["type"] == "chapitre":
            bruit.append((x["t0"], "souffle"))
        elif x["type"] in ("titre", "flash"):
            bruit.append((x["t0"], "cloche"))
        elif x["type"] == "cit" and x.get("c0") is not None and "." not in x["id"]:
            bruit.append((x["c0"] - 0.3, "cloche"))
        elif x["type"] == "tableau" and not x.get("fond"):
            plein.append((x["t0"], x["t1"]))

    pistes = {}
    for _, hu in humeurs:
        if hu not in pistes:
            x = musique.boucle(duree + 1, hu)[:n]
            pistes[hu] = np.pad(x, (0, max(0, n - len(x))))[:n] / (np.abs(x).max() + 1e-9) * 0.42
    tt = np.arange(n) / SR
    mus, poids = np.zeros(n), np.zeros(n)
    for k, (deb, hu) in enumerate(humeurs):
        fin = humeurs[k + 1][0] if k + 1 < len(humeurs) else n / SR + 5
        w = np.clip((tt - deb + 1.25) / 2.5, 0, 1) * np.clip((fin - tt + 1.25) / 2.5, 0, 1) if k else np.clip((fin - tt + 1.25) / 2.5, 0, 1)
        mus += pistes[hu] * w
        poids += w
    mus /= np.maximum(poids, 1e-6)
    g = musique.enveloppe(n / SR, paroles, haut=1.0, bas=0.12)
    g = np.pad(g, (0, max(0, n - len(g))), constant_values=g[-1])[:n]
    for a, b in plein:
        i, j = int(a * SR), int(b * SR)
        g[i:j] = np.maximum(g[i:j], 0.2)
    g *= np.clip(tt / 0.4, 0, 1) * np.clip((duree + 0.5 - tt) / 3.0, 0, 1)
    fx = np.zeros(n)
    for inst, nom in bruit:
        s = musique.souffle() if nom == "souffle" else musique.cloche()
        i = max(0, int(inst * SR)); j = min(n, i + len(s))
        fx[i:j] += s[:j - i] * (0.55 if nom == "souffle" else 0.35)
    pm = pv + mus * g + fx
    pm *= 0.95 / max(1e-9, np.abs(pm).max())
    pm = (np.tanh(1.6 * pm) / np.tanh(1.6))[:int(duree * SR)]

    h = hashlib.sha1(pm.tobytes()[::97]).hexdigest()[:8]
    nom = f"{code}-m-{h}.mp3"
    wav = os.path.join("/tmp", f"remix-{code}.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(pm, -1, 1) * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR),
                    "-codec:a", "libmp3lame", "-b:a", "64k", os.path.join(dos, "voix", nom)], check=True)
    os.remove(wav)
    ancien = ep["audio"]["mix"]
    if ancien != "voix/" + nom and os.path.exists(os.path.join(dos, ancien)):
        os.remove(os.path.join(dos, ancien))
    src = src.replace('"mix":"' + ancien + '"', '"mix":"voix/' + nom + '"')
    assert ('"mix":"voix/' + nom + '"') in src
    open(os.path.join(dos, code + ".data.js"), "w", encoding="utf-8").write(src)
    vjs = hashlib.sha1(src.encode("utf-8")).hexdigest()[:8]
    page = os.path.join(dos, code + ".html")
    html = re.sub(re.escape(code) + r"\.data\.js\?v=[0-9a-f]+", f"{code}.data.js?v={vjs}", open(page, encoding="utf-8").read())
    open(page, "w", encoding="utf-8").write(html)
    print(code, "→", nom, "humeurs :", ", ".join(sorted({hu for _, hu in humeurs})))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for c in sys.argv[1:]:
        remixer(c)
