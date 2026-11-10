#!/usr/bin/env python3
"""Refait la piste « voix + musique » d'un épisode déjà publié, sans réenregistrer la voix ni toucher au minutage.

Usage (depuis la racine du dépôt) :
    python3 outils/serie-philo/remixer.py pc_ch1 [pc_ch2 ...]

Lit <site>/serie/<code>.data.js et la piste « voix seule » (audio.voix), refait la musique avec musique.py
(physique-chimie : musique « labo », une variante par humeur de scène, humeurs lues dans le script), la dose sous la
voix (parole repérée par les sous-titres), ajoute les bruitages (souffle aux cartons, cloche au générique et au titre),
écrit un nouveau MP3 (nom à empreinte), met à jour audio.mix dans le .data.js et le ?v= de la page.
Le .data.js reste identique par ailleurs : une vidéo MP4 déjà rendue garde son image, seule la piste son change.
"""
import hashlib, importlib, json, os, re, subprocess, sys, wave
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))
sys.path.insert(0, ICI)
for d in os.listdir(os.path.join(RACINE, "outils")):
    if d.startswith("serie-"):
        sys.path.insert(0, os.path.join(RACINE, "outils", d))
import musique

SR = musique.SR


def lire_mp3(chemin):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", chemin, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float64) / 32768.0


def remixer(nom_module):
    ep = importlib.import_module(nom_module)
    site = getattr(ep, "SITE", "philo")
    sortie = os.path.join(RACINE, site, "serie")
    fjs = os.path.join(sortie, ep.CODE + ".data.js")
    js = open(fjs, encoding="utf-8").read()
    data = json.loads(js[js.index("=") + 1:].strip().rstrip(";"))
    duree = data["dur"]
    pv = lire_mp3(os.path.join(sortie, data["audio"]["voix"]))
    n = int(duree * SR) + SR
    pv = np.pad(pv, (0, max(0, n - len(pv))))[:n]
    pv *= 0.89 / max(1e-9, np.abs(pv).max())
    # humeurs par scène (dans l'ordre des scènes du script)
    hum = {s["id"]: s.get("humeur", "lumiere") for s in ep.SCENES}
    humeurs = [(0.0 if i == 0 else s["t0"], hum.get(s["id"], "lumiere")) for i, s in enumerate(data["scenes"])]
    style = (lambda h: "pc-" + h) if site == "pc" else (lambda h: h)
    pistes = {}
    for _, hu in humeurs:
        if hu not in pistes:
            x = musique.boucle(duree + 1, style(hu))[:n]
            pistes[hu] = np.pad(x, (0, max(0, n - len(x))))[:n] / (np.abs(x).max() + 1e-9) * (0.5 if site == "pc" else 0.42)
    tt = np.arange(n) / SR
    mus, poids = np.zeros(n), np.zeros(n)
    for k, (deb, hu) in enumerate(humeurs):
        fin = humeurs[k + 1][0] if k + 1 < len(humeurs) else n / SR + 5
        w = np.clip((fin - tt + 1.25) / 2.5, 0, 1) * (np.clip((tt - deb + 1.25) / 2.5, 0, 1) if k else 1)
        mus += pistes[hu] * w
        poids += w
    mus /= np.maximum(poids, 1e-6)
    paroles = [(a, b) for a, b, _ in data["sous"]]
    g = musique.enveloppe(n / SR, paroles, haut=1.0, bas=0.12)
    g = np.pad(g, (0, max(0, n - len(g))), constant_values=g[-1])[:n]
    for v in data["vis"]:
        if v["type"] in ("titre", "chapitre", "generique"):
            i, j = int(v["t0"] * SR), int(v["t1"] * SR)
            g[i:j] = np.maximum(g[i:j], 0.2)
    g *= np.clip(tt / 0.4, 0, 1) * np.clip((duree + 0.5 - tt) / 3.0, 0, 1)
    bruit = [(0.15, "souffle"), (1.6, "cloche")] + [(v["t0"], "souffle") for v in data["vis"] if v["type"] == "chapitre"] \
        + [(v["t0"], "cloche") for v in data["vis"] if v["type"] == "titre"][:1]
    fx = np.zeros(n)
    for inst, nom in bruit:
        s = musique.souffle() if nom == "souffle" else musique.cloche()
        i = max(0, int(inst * SR)); j = min(n, i + len(s))
        fx[i:j] += s[:j - i] * (0.55 if nom == "souffle" else 0.35)
    pm = pv + mus * g + fx
    pm *= 0.95 / max(1e-9, np.abs(pm).max())
    pm = np.tanh(1.4 * pm) / np.tanh(1.4)
    pm = pm[:int(duree * SR)]
    h = hashlib.sha1(pm.tobytes()[::97]).hexdigest()[:8]
    ancien = os.path.join(sortie, data["audio"]["mix"])
    nomf = "voix/%s-m-%s.mp3" % (ep.CODE, h)
    wav = os.path.join(ICI, ".cache", "tmp-remix-%s.wav" % ep.CODE)
    os.makedirs(os.path.dirname(wav), exist_ok=True)
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(pm, -1, 1) * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR),
                    "-codec:a", "libmp3lame", "-b:a", "64k", os.path.join(sortie, nomf)], check=True)
    os.remove(wav)
    if os.path.abspath(ancien) != os.path.abspath(os.path.join(sortie, nomf)) and os.path.exists(ancien):
        os.remove(ancien)
    assert js.count('"mix":"%s"' % data["audio"]["mix"]) == 1
    js = js.replace('"mix":"%s"' % data["audio"]["mix"], '"mix":"%s"' % nomf)
    open(fjs, "w", encoding="utf-8").write(js)
    v = hashlib.sha1(js.encode("utf-8")).hexdigest()[:8]
    fh = os.path.join(sortie, ep.CODE + ".html")
    page = open(fh, encoding="utf-8").read()
    page2 = re.sub(re.escape(ep.CODE) + r"\.data\.js\?v=[0-9a-f]+", ep.CODE + ".data.js?v=" + v, page)
    open(fh, "w", encoding="utf-8").write(page2)
    print("%s : nouvelle piste %s (%.1f min, humeurs %s)" % (ep.CODE, nomf, duree / 60, ", ".join(sorted(pistes))))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for m in sys.argv[1:]:
        remixer(m)
