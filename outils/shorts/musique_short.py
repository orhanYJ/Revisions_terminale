"""Musiques originales des shorts (synthèse, déterministe) : une par modèle, calée sur la structure du short.

L'intensité suit les chapitres du plan (accroche, expérience, résultat, Spinoza, verdict) : couches qui
s'ajoutent ou se retirent d'un coup au début du chapitre ; avant chaque plan « choc », la musique se coupe
0,4 s puis revient sur un impact. Registre médium (piano, cordes, arpèges) pour rester audible sur un
haut-parleur de téléphone, qui ne rend presque rien sous 100 Hz.
"""
import numpy as np
from scipy import signal

SR = 48000
R = np.random.default_rng(3)
NIVEAUX = {0: 1, 1: 2, 2: 3, 3: 1, 4: 3}


def hz(nom):
    notes = {"C": 0, "C#": 1, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}
    n, o = nom[:-1], int(nom[-1])
    return 440 * 2 ** ((notes[n] + 12 * (o + 1) - 69) / 12)


def lp(x, f, o=2):
    b, a = signal.butter(o, min(f, SR / 2 - 100) / (SR / 2), "low"); return signal.lfilter(b, a, x)


def hp(x, f, o=2):
    b, a = signal.butter(o, f / (SR / 2), "high"); return signal.lfilter(b, a, x)


def bp(x, f1, f2):
    b, a = signal.butter(2, [f1 / (SR / 2), f2 / (SR / 2)], "band"); return signal.lfilter(b, a, x)


def ar(n, a, r):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)


def adsr(n, a, rel):
    e = np.ones(n); na, nr = int(a * SR), int(rel * SR)
    e[:na] = np.linspace(0, 1, na) if na else 1
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e


def scie(f, n, detune=0.0):
    t = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * f * (1 + detune) * k * t) / k for k in range(1, int(min(16, 9000 / f)) + 1))


# ---------------------------------------------------------------- instruments
def piano(f, d):
    n = int(d * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (1.2 + k * .9)) for k, a in [(1, 1), (2, .5), (3, .25), (4, .12), (5, .06)])
    return x * np.minimum(1, t / .003)


def pluck(f, d, brillance=3000):
    n = int(d * SR); return lp(scie(f, n), brillance) * ar(n, .002, .18)


def cloche(f, d):
    n = int(d * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + .4 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 6) + .2 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 9)) * ar(n, .001, .5)


def nappe(fs, d, coupure=1800):
    n = int(d * SR)
    x = sum(scie(f, n, dt) for f in fs for dt in (-.004, .004))
    return lp(x, coupure) * adsr(n, .25, .3) / len(fs)


def ostinato(f, d):
    n = int(d * SR); return lp(scie(f, n), 1400) * ar(n, .003, .07)


def basse(f, d, coupure=400):
    n = int(d * SR); t = np.arange(n) / SR
    return (lp(scie(f, n), coupure) * .6 + np.sin(2 * np.pi * f * t)) * adsr(n, .005, .05)


def b808(f, d):
    n = int(d * SR); t = np.arange(n) / SR
    fr = f * (1 + 1.5 * np.exp(-t * 30))
    x = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .7)
    return np.tanh(x * 2.2) * .8 + .3 * np.sin(4 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .3)


def taiko(d=.6, f0=95):
    n = int(d * SR); t = np.arange(n) / SR
    fr = f0 * (1 + .8 * np.exp(-t * 25))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .22) + bp(R.standard_normal(n), 200, 1500) * np.exp(-t / .03) * .5


def kick(d=.4):
    n = int(d * SR); t = np.arange(n) / SR
    fr = 50 + 110 * np.exp(-t * 35)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .16) + bp(R.standard_normal(n), 1500, 6000) * np.exp(-t / .004) * .4


def clap(d=.25):
    n = int(d * SR); t = np.arange(n) / SR; x = bp(R.standard_normal(n), 900, 5000)
    e = sum(np.exp(-np.maximum(0, t - o) / .01) * (t >= o) for o in (0, .011, .022)) * .5 + np.exp(-t / .08) * .6
    return x * e


def charley(d=.06, ouvert=False):
    n = int(d * SR); return hp(R.standard_normal(n), 7000) * ar(n, .0005, .12 if ouvert else .012)


def impact(d=1.6):
    n = int(d * SR); t = np.arange(n) / SR
    fr = 35 + 90 * np.exp(-t * 12)
    boum = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .5)
    crash = hp(R.standard_normal(n), 3000) * np.exp(-t / .6) * .35
    return boum * 1.2 + crash


def montee(d):
    n = int(d * SR); r = np.linspace(0, 1, n) ** 3
    return hp(R.standard_normal(n), 2000) * r * .35


def poser(y, x, t, g=1.0):
    o = int(round(t * SR))
    if o >= len(y) or o + len(x) <= 0: return
    if o < 0: x = x[-o:]; o = 0
    m = min(len(x), len(y) - o); y[o:o + m] += x[:m] * g


# ---------------------------------------------------------------- styles
STYLES = {
    # A : cinématique, ré mineur, piano + cordes + taïkos
    "cine": dict(bpm=96, accords=[["D3", "F3", "A3"], ["Bb2", "D3", "F3"], ["F3", "A3", "C4"], ["C3", "E3", "G3"]],
                 basses=["D2", "Bb1", "F2", "C2"]),
    # B : électronique, la mineur, arpèges filtrés + kick régulier
    "synth": dict(bpm=112, accords=[["A3", "C4", "E4"], ["F3", "A3", "C4"], ["C4", "E4", "G4"], ["G3", "B3", "D4"]],
                  basses=["A1", "F1", "C2", "G1"]),
    # C : trap, do mineur, cloches + 808 + charleston en rafales
    "trap": dict(bpm=140, accords=[["C4", "Eb4", "G4"], ["Ab3", "C4", "Eb4"], ["Eb4", "G4", "Bb4"], ["Bb3", "D4", "F4"]],
                 basses=["C2", "Ab1", "Eb2", "Bb1"]),
}
ANCIENS = {"drone": "cine", "pulse": "synth", "beat": "trap"}


def composer(style, dur, sections, chocs):
    style = ANCIENS.get(style, style)
    S = STYLES[style]; n = int(dur * SR); y = np.zeros(n)
    b = 60 / S["bpm"]; s16 = b / 4; mes = 4 * b
    sections = sorted(sections) or [[0, 0]]

    def niveau(t):
        nv = NIVEAUX.get(sections[0][1], 1)
        for t0, ch in sections:
            if t >= t0 - 1e-3: nv = NIVEAUX.get(ch, 2)
        return nv

    pas = int(dur / s16) + 1
    for i in range(pas):
        t = i * s16; nv = niveau(t)
        k = int(t / mes) % 4; ac, bs = S["accords"][k], S["basses"][k]
        pos = i % 16
        def f(note, oct=0): return hz(note) * 2 ** oct
        if style == "cine":
            if pos == 0:
                poser(y, nappe([f(x) for x in ac] + [f(ac[0], 1)], mes + .1), t, .55 if nv >= 2 else .4)
                poser(y, taiko(.8, 80), t, .55 if nv == 1 else .8)
            if pos % 2 == 0:   # piano en croches : arpège montant puis descendant
                motif = [0, 1, 2, 3, 2, 1, 2, 3]; j = motif[(pos // 2) % 8]
                note = f(ac[j % 3], 1 + (1 if j == 3 else 0))
                poser(y, piano(note, .9), t, .32 if nv >= 2 else .38)
            if nv >= 2:
                poser(y, ostinato(f(bs, 1), s16 * .9), t, .22)
                if pos % 2 == 1: poser(y, charley(), t, .1)
            if nv >= 3:
                if pos in (0, 6, 8, 14): poser(y, taiko(.6, 70), t, .85)
                if pos in (4, 12): poser(y, clap(), t, .35)
                if pos in (0, 8): poser(y, basse(f(bs), b * 2 * .95), t, .4)
                if pos in (0, 3, 6, 10, 12): poser(y, piano(f(ac[(pos // 3) % 3], 2), .6), t, .16)
        elif style == "synth":
            arp = [0, 1, 2, 1, 2, 0, 1, 2]
            if pos == 0: poser(y, nappe([f(x) for x in ac], mes + .1, 1400), t, .4)
            cut = 1500 + 2500 * (.5 + .5 * np.sin(2 * np.pi * t / (4 * mes)))
            poser(y, pluck(f(ac[arp[pos % 8]], 1 if pos % 8 >= 4 else 0), s16 * 1.6, cut), t, .32)
            if nv >= 2:
                if pos % 4 == 0: poser(y, kick(), t, .6)
                if pos % 4 == 2: poser(y, charley(.12, True), t, .14)
            if nv >= 3:
                if pos % 4 == 2: poser(y, basse(f(bs, 1), s16 * 1.8, 700), t, .35)
                if pos in (4, 12): poser(y, clap(), t, .4)
                if pos % 2 == 1: poser(y, charley(), t, .09)
                if pos in (0, 3, 6, 10): poser(y, pluck(f(ac[pos % 3], 2), .3, 5000), t, .14)
        else:  # trap (demi-tempo)
            if pos == 0: poser(y, nappe([f(x) for x in ac], mes + .1, 1600), t, .35)
            if pos % 2 == 0:
                mel = [2, 1, 0, 1, 2, 2, 1, 0]
                poser(y, cloche(f(ac[mel[(pos // 2) % 8]], 1), .5), t, .2)
            if nv >= 2:
                rafale = (k % 2 == 1 and pos >= 12)
                if rafale: [poser(y, charley(.03), t + q * s16 / 2, .1) for q in range(2)]
                elif pos % 2 == 0: poser(y, charley(), t, .13)
                if pos == 0: poser(y, b808(f(bs), mes * .9), t, .5)
            if nv >= 3:
                if pos in (0, 7, 10): poser(y, kick(), t, .75)
                if pos == 8: poser(y, clap(), t, .5)
                if pos in (7, 10): poser(y, b808(f(bs), b * 1.4), t, .4)
    # chocs : coupure 0,4 s, montée de souffle, impact
    gain = np.ones(n)
    for tc in chocs:
        a, z = int((tc - .4) * SR), int(tc * SR)
        if a <= 0: continue
        gain[a:z] = 0
        fa = int(.02 * SR); gain[a - fa:a] = np.minimum(gain[a - fa:a], np.linspace(1, 0, fa))
        poser(y, montee(.4), tc - .4, 1)
    y = y * gain
    for tc in chocs:
        poser(y, impact(), tc, .9)
    # fin : la musique s'éteint sur la dernière demi-seconde
    m = int(.5 * SR); y[-m:] *= np.linspace(1, 0, m)
    return y
