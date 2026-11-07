"""Bande son d'un short : voix + musique originale + bruitages, tout synthétisé ici (aucun son emprunté).

Usage : python3 outils/shorts/mix.py libet a   (lit sortie/libet-a.sons.json écrit par rendu.js)
Écrit sortie/<code>-<m>.mix.wav, normalisé à −14 LUFS (niveau des plateformes de vidéos courtes).
"""
import json, os, subprocess, sys

import numpy as np
from scipy import signal

SR = 48000
ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "sortie")
R = np.random.default_rng(7)


def env(n, a=.005, r=.3):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)


def bruit(d):
    return R.standard_normal(int(d * SR)).astype(np.float32)


def bp(x, f1, f2, o=2):
    b, a = signal.butter(o, [f1 / (SR / 2), min(f2, SR / 2 - 100) / (SR / 2)], "band")
    return signal.lfilter(b, a, x)


def lp(x, f, o=2):
    b, a = signal.butter(o, f / (SR / 2), "low")
    return signal.lfilter(b, a, x)


def hp(x, f, o=2):
    b, a = signal.butter(o, f / (SR / 2), "high")
    return signal.lfilter(b, a, x)


def sinus_glisse(f0, f1, d, courbe=3):
    t = np.arange(int(d * SR)) / SR
    f = f1 + (f0 - f1) * np.exp(-t * courbe / d)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def balaye(d, f0, f1, q=.5):
    """bruit filtré dont la fréquence glisse de f0 à f1 (souffle, whoosh)."""
    n = int(d * SR); x = bruit(d); y = np.zeros(n); k = 2048
    for i in range(0, n, k):
        f = f0 * (f1 / f0) ** (i / n)
        y[i:i + k] = bp(x[i:i + k + 512], f * (1 - q), f * (1 + q))[:len(y[i:i + k])]
    return y * np.sin(np.linspace(0, np.pi, n)) ** 2


# ---------------------------------------------------------------- bruitages
def sfx(nom):
    if nom == "boum":
        s = sinus_glisse(70, 34, 1.4, 4) * env(int(1.4 * SR), .002, .55)
        return s + lp(bruit(1.4), 300) * env(int(1.4 * SR), .001, .12) * .5
    if nom == "drop":
        s = sinus_glisse(140, 38, 1.2, 6) * env(int(1.2 * SR), .001, .5)
        return s * 1.1 + lp(bruit(1.2), 900) * env(int(1.2 * SR), .001, .08) * .5
    if nom == "papier":
        return balaye(.28, 900, 3500, .6) * .6 + hp(bruit(.28), 4000) * env(int(.28 * SR), .002, .05) * .3
    if nom == "clic":
        n = int(.08 * SR); return sinus_glisse(900, 500, .08, 6) * env(n, .0005, .015) * .8
    if nom == "frotte":
        return lp(balaye(.18, 600, 1400, .5), 2500) * .7
    if nom == "whoosh":
        return balaye(.32, 400, 2600, .5) * .8
    if nom == "souffle":
        return balaye(.8, 300, 1800, .4)
    if nom == "montee":
        d = .45; n = int(d * SR); r = np.linspace(0, 1, n) ** 2.5
        return (balaye(d, 300, 5000, .3) * 1.4 + sinus_glisse(200, 900, d, -2)[:n] * .15) * r
    if nom == "aspire":
        d = .5; n = int(d * SR); r = np.linspace(0, 1, n) ** 3
        return hp(bruit(d), 800) * r * .6 + np.sin(2 * np.pi * 55 * np.arange(n) / SR) * r * .5
    if nom == "tampon":
        n = int(.5 * SR)
        return np.sin(2 * np.pi * 90 * np.arange(n) / SR) * env(n, .001, .09) + bp(bruit(.5), 800, 3000) * env(n, .0005, .02) * 1.2
    if nom == "tic":
        n = int(.05 * SR); return np.sin(2 * np.pi * 1700 * np.arange(n) / SR) * env(n, .0005, .008) + hp(bruit(.05), 3000) * env(n, .0003, .004) * .5
    if nom == "blip":
        n = int(.07 * SR); return np.sin(2 * np.pi * 1850 * np.arange(n) / SR) * env(n, .001, .03) * .7
    if nom == "pop":
        return sinus_glisse(700, 180, .06, 5) * env(int(.06 * SR), .0005, .02)
    if nom == "bip":
        n = int(.14 * SR); return np.sin(2 * np.pi * 1000 * np.arange(n) / SR) * np.minimum(1, (n - np.arange(n)) / 400) * .5
    if nom == "lame":
        n = int(.35 * SR)
        return balaye(.35, 2500, 9000, .3) + np.sin(2 * np.pi * 3150 * np.arange(n) / SR) * env(n, .01, .12) * .25
    if nom == "coeur":
        n = int(.6 * SR); t = np.arange(n) / SR
        k = lambda d: np.sin(2 * np.pi * 52 * t) * np.exp(-np.maximum(0, t - d) / .07) * (t >= d)
        return (k(0) + .7 * k(.22)) * 1.3
    if nom == "rembobine":
        d = .7; n = int(d * SR); t = np.arange(n) / SR
        f = 900 * np.exp(-t * 3) + 120 + 300 * np.sin(2 * np.pi * 14 * t)
        return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .25 * np.linspace(1, 0, n) + bp(bruit(d), 500, 4000) * .3 * np.linspace(1, 0, n)
    if nom == "disque":
        d = .45; n = int(d * SR); t = np.arange(n) / SR
        m = np.sin(2 * np.pi * 7 * t) * 2500 + 3000
        y = np.zeros(n); x = bruit(d)
        for i in range(0, n, 1024):
            f = m[i]; y[i:i + 1024] = bp(x[i:i + 1024 + 256], f * .7, f * 1.3)[:len(y[i:i + 1024])]
        return y * 1.5 * np.linspace(1, .2, n)
    if nom == "stylo":
        d = .6; n = int(d * SR); t = np.arange(n) / SR
        return bp(bruit(d), 2000, 7000) * (.5 + .5 * np.sin(2 * np.pi * 11 * t)) ** 2 * .5
    if nom == "statique":
        d = .7; n = int(d * SR); x = bruit(d) * (R.random(n) > .7)
        return hp(x, 1500) * .45 * np.linspace(1, .3, n)
    if nom == "glitch":
        d = .3; n = int(d * SR); t = np.arange(n) / SR
        g = np.sign(np.sin(2 * np.pi * 220 * t)) * ((t * 40).astype(int) % 2) * .3
        return g + bp(bruit(d), 1000, 6000) * ((t * 60).astype(int) % 3 == 0) * .4
    if nom == "gong":
        n = int(2.6 * SR); t = np.arange(n) / SR
        return sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t / dd) for f, a, dd in [(98, .6, 1.4), (196.7, .3, 1), (263, .2, .7), (411, .1, .4)])
    if nom == "chapitre":
        n = int(.45 * SR); y = np.zeros(n)
        for i, f in enumerate([659, 880, 1319]):
            o = int(i * .07 * SR); m = n - o; y[o:] += np.sin(2 * np.pi * f * np.arange(m) / SR) * env(m, .002, .12) * .35
        return y
    if nom == "valide":
        n = int(.6 * SR); y = np.zeros(n)
        for i, f in enumerate([1047, 1568]):
            o = int(i * .09 * SR); m = n - o; y[o:] += np.sin(2 * np.pi * f * np.arange(m) / SR) * env(m, .002, .2) * .4
        return y
    if nom == "coupe":
        n = int(.25 * SR)
        return sinus_glisse(160, 45, .25, 7) * env(n, .001, .09) + hp(bruit(.25), 2500) * env(n, .0005, .025) * .7
    if nom == "frappe":
        n = int(.2 * SR)
        return sinus_glisse(120, 50, .2, 6) * env(n, .001, .06) * .9 + bp(bruit(.2), 1200, 5000) * env(n, .001, .03) * .5
    raise ValueError(nom)


# ---------------------------------------------------------------- musiques (originales, déterministes)
def kick(d=.4):
    n = int(d * SR); return sinus_glisse(150, 45, d, 8) * env(n, .001, .12)


def note(f, d, forme="saw"):
    n = int(d * SR); t = np.arange(n) / SR
    if forme == "saw":
        x = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 9))
    else:
        x = np.sin(2 * np.pi * f * t)
    return x


def poser(y, x, t, g=1.0):
    o = int(t * SR)
    if o >= len(y) or o + len(x) <= 0:
        return
    if o < 0:
        x = x[-o:]; o = 0
    m = min(len(x), len(y) - o); y[o:o + m] += x[:m] * g


def musique(nom, dur, bpm):
    n = int(dur * SR); y = np.zeros(n)
    if nom == "drone":
        t = np.arange(n) / SR
        # nappe grave ré mineur, filtre qui s'ouvre lentement, pulsation sourde toutes les 1,25 s
        pad = sum(np.sin(2 * np.pi * f * t + ph) for f, ph in [(36.7, 0), (55.0, 1), (73.4, 2), (87.3, .5), (110, 1.7)])
        pad += .3 * sum(np.sin(2 * np.pi * f * 1.003 * t) for f in (146.8, 174.6, 220))
        pad *= .16 * (.6 + .4 * np.sin(2 * np.pi * t / 9) ** 2)
        y += lp(pad, 900)
        for k in np.arange(.2, dur, 1.25):
            poser(y, kick(.6) * .5, k)
        return y
    b = 60 / bpm
    if nom == "pulse":
        prog = [(55.0, [220, 261.6, 329.6]), (43.65, [174.6, 220, 261.6]), (65.4, [261.6, 329.6, 392]), (49.0, [196, 246.9, 293.7])]
        for i, k in enumerate(np.arange(0, dur, b / 4)):
            mes = int(k / (4 * b)) % 4; basse, acc = prog[mes]
            d = b / 4 * .9
            x = lp(note(acc[i % 3] * (2 if i % 8 >= 4 else 1), d), 2400) * env(int(d * SR), .003, .08) * .12
            poser(y, x, k)
            if i % 4 == 0:
                poser(y, kick() * .45, k)
                poser(y, lp(note(basse, b * .9), 300) * env(int(b * .9 * SR), .005, .25) * .3, k)
            if i % 4 == 2:
                poser(y, hp(bruit(.05), 7000) * env(int(.05 * SR), .001, .015) * .25, k)
        return y
    if nom == "beat":
        basses = [55.0, 55.0, 43.65, 49.0]
        for i, k in enumerate(np.arange(0, dur, b / 2)):
            mes = int(k / (4 * b)) % 4
            if i % 8 in (0, 3, 5):
                poser(y, kick(.5) * .7, k)
            if i % 4 == 2:
                poser(y, (bp(bruit(.18), 900, 5000) * env(int(.18 * SR), .001, .05) + sinus_glisse(240, 180, .18, 5) * env(int(.18 * SR), .001, .05) * .4) * .55, k)
            poser(y, hp(bruit(.04), 8000) * env(int(.04 * SR), .0005, .01) * (.35 if i % 2 else .2), k)
            if i % 8 == 0:
                d = 4 * b * .95
                poser(y, lp(note(basses[mes], d, "sin") + .3 * note(basses[mes] * 2, d, "sin"), 200) * env(int(d * SR), .01, 1.2) * .5, k)
        return y
    raise ValueError(nom)


def main(code, m):
    voix, _ = None, None
    import soundfile as sf
    voix, sr = sf.read(os.path.join(SORTIE, f"{code}.voix.wav"), dtype="float32")
    assert sr == SR
    info = json.load(open(os.path.join(SORTIE, f"{code}-{m}.sons.json"), encoding="utf-8"))
    n = len(voix)
    import musique_short
    if "sections" in info:
        mus = musique_short.composer(os.environ.get("SHORT_STYLE") or info["musique"], n / SR, info["sections"], info["chocs"], info.get("relache"))[:n]
    else:
        mus = musique(info["musique"], n / SR, info.get("bpm") or 0)[:n]
    # sidechain léger : la musique se tasse sous la voix sans disparaître
    e = np.abs(voix); e = lp(e, 8, 1); e = e / (np.percentile(e, 98) + 1e-9)
    duck = 1 - .3 * np.clip(e, 0, 1)
    mus = mus * duck
    v0 = voix / (np.max(np.abs(voix)) + 1e-9) * .8
    # niveau : la musique à SHORT_MUSIQUE dB sous la voix pendant la parole (−9 par défaut), plus forte dans les silences
    parle = lp(np.abs(v0), 5, 1) > .02
    rv, rm = np.sqrt(np.mean(v0[parle] ** 2)), np.sqrt(np.mean(mus[parle] ** 2)) + 1e-9
    mus = mus * rv / rm * 10 ** (float(os.environ.get("SHORT_MUSIQUE", "-9")) / 20)
    fx = np.zeros(n); cache = {}
    for t, nom, gain in info["sons"]:
        if nom not in cache:
            x = np.asarray(sfx(nom), dtype=np.float64); cache[nom] = x / (np.max(np.abs(x)) + 1e-9)
        poser(fx, cache[nom], t, gain * .5)
    v = voix / (np.max(np.abs(voix)) + 1e-9) * .8
    mix = v + mus + fx
    mix = np.tanh(mix * 1.1) / np.tanh(1.1)          # saturation douce
    tmp = os.path.join(SORTIE, f"{code}-{m}.brut.wav")
    sf.write(tmp, mix.astype(np.float32), SR)
    sortie = os.path.join(SORTIE, f"{code}-{m}.mix.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.2:LRA=9", "-ar", str(SR), sortie], check=True)
    os.remove(tmp)
    print("écrit", sortie)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
