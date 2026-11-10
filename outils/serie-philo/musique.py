"""Musique de fond et bruitages des épisodes, synthétisés ici (aucune œuvre tierce, aucun droit à régler).

Une boucle douce en la mineur (la – fa – do – sol), 84 battements par minute : nappe, arpège de type
piano, basse et léger frémissement rythmique, passés dans une réverbération. La musique s'efface sous
la voix (environ −20 dB) et remonte pendant les silences, les cartons de chapitre et le générique.
Tout est déterministe : le même épisode redonne exactement le même fichier.
"""
import numpy as np

SR = 24000
BPM = 84.0
BEAT = 60.0 / BPM

# accords sur deux mesures chacun : (basse, notes de l'accord) en numéros MIDI
ACCORDS = [(45, [57, 60, 64, 69]),   # la mineur
           (41, [57, 60, 65, 69]),   # fa majeur
           (48, [55, 60, 64, 67]),   # do majeur
           (43, [55, 59, 62, 67])]   # sol majeur
MOTIF = [0, 2, 1, 3, 2, 1, 3, 2]     # ordre de l'arpège (croches)

# humeurs : une couleur musicale par chapitre (même instrumentation, donc même identité sonore)
HUMEURS = {
    "lumiere": dict(bpm=84, accords=ACCORDS, arpege=1.0, nappe=0.20),
    "mystere": dict(bpm=70, accords=[(38, [50, 53, 57, 62]), (46, [50, 53, 58, 62]),      # ré m, si bémol
                                     (43, [50, 55, 58, 62]), (45, [49, 52, 57, 61])],     # sol m, la
                    arpege=0.55, nappe=0.26),
    "tension": dict(bpm=92, accords=[(40, [52, 55, 59, 64]), (36, [52, 55, 60, 64]),      # mi m, do
                                     (45, [52, 57, 60, 64]), (47, [51, 54, 59, 63])],     # la m, si
                    arpege=1.0, nappe=0.18),
    "calme": dict(bpm=76, accords=[(41, [53, 57, 60, 65]), (48, [52, 55, 60, 64]),        # fa, do
                                   (38, [53, 57, 62, 65]), (46, [53, 58, 62, 65])],       # ré m, si bémol
                  arpege=0.7, nappe=0.22),
}


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def _note_piano(f, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    env = np.exp(-t * 3.2) * np.minimum(1, t / 0.004)
    s = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) * np.exp(-t * 4)
         + 0.12 * np.sin(6 * np.pi * f * t) * np.exp(-t * 6))
    return amp * env * s


def _nappe(freqs, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    att = np.minimum(1, t / 1.6)
    rel = np.minimum(1, (dur - t) / 1.4).clip(0, 1)
    s = np.zeros(n)
    for i, f in enumerate(freqs):
        for d in (-0.6, 0.6):
            s += np.sin(2 * np.pi * (f + d) * t + i)
        s += 0.25 * np.sin(2 * np.pi * 2 * f * t + i * 0.7)
    trem = 1 + 0.08 * np.sin(2 * np.pi * 0.23 * t)
    return amp * att * rel * trem * s / (2.25 * len(freqs))


def _ajoute(dst, src, i):
    if i >= len(dst):
        return
    j = min(len(dst), i + len(src))
    dst[i:j] += src[:j - i]


def _reverb(x, duree=2.2, mix=0.32):
    rng = np.random.default_rng(7)
    n = int(duree * SR)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / SR * 3.2)
    ir /= np.sqrt((ir ** 2).sum())
    m = len(x) + n - 1
    taille = 1 << (m - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, taille) * np.fft.rfft(ir, taille), taille)[:len(x)]
    return (1 - mix) * x + mix * y * 0.9


# reel irlandais original (composé ici, aucune œuvre tierce) pour la danse de Dancing at Lughnasa : violon, basse,
# accords sur les contretemps et tambour sur chaque temps ; « very fast, very heavy beat, a raucous sound » (p. 22)
REEL_A = [[74, 78, 81, 78, 74, 78, 81, 83], [86, 83, 81, 78, 79, 78, 76, 74], [79, 83, 86, 83, 79, 83, 86, 83],
          [81, 85, 88, 85, 81, 79, 78, 76], [74, 78, 81, 78, 74, 78, 81, 83], [86, 85, 83, 81, 79, 78, 76, 78],
          [79, 81, 83, 79, 81, 76, 73, 76], [74, 73, 74, 76, 78, 76, 74, 69]]
REEL_B = [[86, 81, 78, 81, 86, 81, 78, 81], [83, 79, 74, 79, 83, 79, 74, 79], [86, 81, 78, 81, 86, 88, 86, 85],
          [83, 81, 79, 78, 76, 73, 69, 73], [86, 81, 78, 81, 86, 81, 78, 81], [83, 79, 74, 79, 83, 85, 86, 88],
          [86, 83, 81, 79, 78, 76, 73, 76], [74, 73, 74, 76, 74, 69, 74, 0]]
REEL_ACC = {"D": (38, [62, 66, 69]), "G": (43, [62, 67, 71]), "A": (45, [61, 64, 69])}
REEL_GRILLE = ["D", "D", "G", "A", "D", "D", "G", "D"] * 2 + ["D", "G", "D", "A", "D", "G", "A", "D"] * 2


def _violon(f, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t)
    ph = 2 * np.pi * f * np.cumsum(vib) / SR
    s = sum(np.sin(k * ph) / k for k in range(1, 7))
    env = np.minimum(1, t / 0.012) * np.exp(-t * 2.5) * np.minimum(1, (dur - t) / 0.02).clip(0, 1)
    return amp * env * s


def reel(duree):
    croche = 60.0 / 113 / 2
    n = int(duree * SR) + SR
    out = np.zeros(n)
    melodie = REEL_A + REEL_A + REEL_B + REEL_B
    t, k = 0.0, 0
    while t < duree:
        mesure = melodie[k % len(melodie)]
        acc = REEL_ACC[REEL_GRILLE[k % len(REEL_GRILLE)]]
        for c, m in enumerate(mesure):
            if m:
                _ajoute(out, _violon(hz(m), croche * 1.05, 0.11 if c % 2 == 0 else 0.085), int((t + c * croche) * SR))
        for b in range(4):
            i = int((t + b * 2 * croche) * SR)
            L = int(0.18 * SR); tt = np.arange(L) / SR
            _ajoute(out, (0.32 if b % 2 == 0 else 0.22) * np.sin(2 * np.pi * (75 - 30 * tt) * tt) * np.exp(-tt * 22), i)
            if b % 2 == 0:
                _ajoute(out, _note_piano(hz(acc[0]), 0.5, 0.22), i)
            else:
                for m in acc[1]:
                    _ajoute(out, _note_piano(hz(m), 0.25, 0.06), i)
        t += 8 * croche
        k += 1
    out = np.tanh(2.2 * out) / np.tanh(2.2)          # le son « raucous » d'un vieux poste
    return out[:int(duree * SR)]


# ---------------------------------------------------------------------------------------------
# Musique des vidéos d'histoire (DNL, 11/2026, choisie par Cengiz : « combine les trois, elles vont bien ensemble ») :
# trois couleurs en ré mineur, composées ici, qui se relaient selon l'humeur de la scène.
#   salon    : piano feutré, contrebasse pincée, balais, craquement de 78 tours (l'entre-deux-guerres)
#   archives : violoncelle et alto tenus, notes de piano, tic-tac d'horloge (le ton du documentaire)
#   marche   : caisse claire étouffée, cuivres doux, timbales (la guerre, la terreur)
from scipy.signal import lfilter as _lfilter


def _lp(x, a):
    return _lfilter([a], [1, a - 1], x)


def _piano_feutre(f, dur, amp):
    n = int(dur * SR); t = np.arange(n) / SR
    env = np.exp(-t * 2.2) * np.minimum(1, t / 0.008)
    s = np.sin(2 * np.pi * f * t) + .22 * np.sin(4 * np.pi * f * t) * np.exp(-t * 5) + .06 * np.sin(6 * np.pi * f * t) * np.exp(-t * 8)
    return amp * env * s


def _pizz(f, dur, amp):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + .5 * np.sin(4 * np.pi * f * t) * np.exp(-t * 9) + .2 * np.sin(6 * np.pi * f * t) * np.exp(-t * 14)
    return amp * s * np.exp(-t * 6) * np.minimum(1, t / 0.003)


def _balai(dur, amp, rng):
    n = int(dur * SR); t = np.arange(n) / SR
    return amp * np.diff(rng.standard_normal(n), prepend=0) * np.sin(np.pi * np.minimum(1, t / dur)) ** 2


def _archet(f, dur, amp, vib=5.0):
    n = int(dur * SR); t = np.arange(n) / SR
    v = 1 + 0.003 * np.sin(2 * np.pi * vib * t) * np.minimum(1, t / .8)
    ph = 2 * np.pi * f * np.cumsum(v) / SR
    s = sum(np.sin(k * ph) / k ** 1.3 for k in range(1, 9))
    return amp * np.minimum(1, t / .7) * np.clip((dur - t) / .9, 0, 1) * s


def _cuivre(freqs, dur, amp):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for f in freqs:
        s += sum(np.sin(k * 2 * np.pi * f * t) / k for k in range(1, 7))
    return amp * np.minimum(1, t / .35) * np.clip((dur - t) / .6, 0, 1) * _lp(s, .08) / len(freqs)


def _tictac(amp, aigu=True):
    n = int(.03 * SR); t = np.arange(n) / SR
    return amp * np.sin(2 * np.pi * (2400 if aigu else 1800) * t) * np.exp(-t * 260)


def _caisse(amp, rng, dur=.16):
    n = int(dur * SR); t = np.arange(n) / SR
    return amp * (_lp(rng.standard_normal(n), .35) * np.exp(-t * 26) + .4 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30))


def _timbale(f, amp):
    n = int(1.2 * SR); t = np.arange(n) / SR
    return amp * np.sin(2 * np.pi * f * t * (1 - .03 * t)) * np.exp(-t * 3.5) * np.minimum(1, t / .004)


def _craquements(dur, rng):
    n = int(dur * SR); x = np.zeros(n)
    idx = rng.integers(0, n, int(dur * 9))
    x[idx] = rng.standard_normal(len(idx)) * .5
    return _lp(x, .5) + .004 * _lp(rng.standard_normal(n), .05)


_SALON = [(38, [53, 57, 60, 64]), (43, [53, 58, 62, 65]), (45, [52, 55, 61, 64]), (38, [50, 53, 57, 60])]   # ré m9, sol m6, la 7, ré m7
_ARCH = [(38, [50, 53, 57]), (34, [50, 53, 58]), (31, [50, 55, 58]), (33, [49, 52, 57])]                    # ré m, si bémol, sol m, la
_MARCHE = [(38, [62, 65, 69]), (34, [62, 65, 70]), (36, [60, 64, 67]), (33, [61, 64, 69])]                  # ré m, si bémol, do, la


def salon(duree):
    rng = np.random.default_rng(5); B = 60 / 72
    out = np.zeros(int(duree * SR) + SR); t, k = 0.0, 0
    while t < duree:
        b, acc = _SALON[k % 4]
        for j, m in enumerate(acc):
            _ajoute(out, _piano_feutre(hz(m), 3.0, .07), int((t + j * .06) * SR))
        for j, m in enumerate([acc[3] + 12, acc[2] + 12, acc[1] + 12, acc[2] + 12]):
            if (k + j) % 3:
                _ajoute(out, _piano_feutre(hz(m), 1.4, .045), int((t + (1 + j * .75) * B) * SR))
        for j in range(4):
            _ajoute(out, _pizz(hz([b, b + 7, b + 12, b + 7][j]), .9, .2), int((t + j * B) * SR))
            if j % 2:
                _ajoute(out, _balai(.22, .012, rng), int((t + j * B) * SR))
        t += 4 * B; k += 1
    out = _reverb(out, 1.8, .28)[:int(duree * SR)]
    return out + _craquements(duree, rng)[:len(out)] * .25


def archives(duree):
    B = 60 / 64
    out = np.zeros(int(duree * SR) + SR); t, k = 0.0, 0
    while t < duree:
        b, acc = _ARCH[k % 4]; d = 8 * B
        _ajoute(out, _archet(hz(b + 12), d + .6, .11), int(t * SR))
        _ajoute(out, _archet(hz(acc[1]), d + .6, .045, 4.6), int(t * SR))
        for j, m in enumerate([acc[0] + 12, acc[2] + 12, acc[1] + 12]):
            _ajoute(out, _piano_feutre(hz(m), 3.5, .05), int((t + (1 + j * 2.5) * B) * SR))
        for j in range(8):
            _ajoute(out, _tictac(.03, j % 2 == 0), int((t + j * B) * SR))
        t += d; k += 1
    return _reverb(out, 2.6, .36)[:int(duree * SR)]


def marche(duree):
    rng = np.random.default_rng(13); B = 60 / 84
    out = np.zeros(int(duree * SR) + SR); t, k = 0.0, 0
    motif = [1, 0, .5, .5, 1, 0, .5, 1]
    while t < duree:
        b, acc = _MARCHE[k % 4]; d = 4 * B
        _ajoute(out, _cuivre([hz(m - 12) for m in acc], d + .3, .18), int(t * SR))
        _ajoute(out, _timbale(hz(b + 12), .22), int(t * SR))
        _ajoute(out, _timbale(hz(b + 7), .12), int((t + 2 * B) * SR))
        for j, a in enumerate(motif):
            if a:
                _ajoute(out, _caisse(.05 * a, rng), int((t + j * B / 2) * SR))
        _ajoute(out, _archet(hz(b + 24), d + .4, .04), int(t * SR))
        t += d; k += 1
    return _reverb(out, 2.0, .3)[:int(duree * SR)]


# humeurs des scripts → musique d'histoire (generer.py et remixer.py l'appliquent aux vidéos DNL) :
# « lumière » → salon ; « calme » et « mystère » → archives ; « tension » → marche sur un fond de guerre ou dans le
# chapitre sur la Seconde Guerre mondiale (h3), salon sinon (la crise, la montée des régimes, l'entre-deux-guerres)
def humeur_dnl(humeur, fond, code):
    if humeur == "lumiere":
        return "salon"
    if humeur in ("calme", "mystere"):
        return "archives"
    if humeur == "tension":
        return "marche" if fond == "guerre" or code.startswith("h3") else "salon"
    return humeur


def boucle(duree, humeur="lumiere"):
    """Musique brute (sans dosage) de la durée demandée, dans l'humeur choisie."""
    if humeur == "reel":
        return reel(duree)
    if humeur in ("salon", "archives", "marche"):
        return {"salon": salon, "archives": archives, "marche": marche}[humeur](duree)
    H = HUMEURS[humeur]
    BEAT = 60.0 / H["bpm"]
    ACCORDS = H["accords"]
    n = int(duree * SR) + SR
    out = np.zeros(n)
    rng = np.random.default_rng(3)
    mesure = 4 * BEAT
    t, k = 0.0, 0
    while t < duree:
        basse, notes = ACCORDS[k % 4]
        d = 2 * mesure
        i = int(t * SR)
        _ajoute(out, _nappe([hz(m) for m in notes[:3]], d + 1.2, H["nappe"]), i)
        for b in (0, 2, 4, 6):  # basse sur les temps forts
            nb = _note_piano(hz(basse), 1.6, 0.20)
            _ajoute(out, nb * np.exp(-np.arange(len(nb)) / SR * 0.8), int((t + b * BEAT) * SR))
        for c in range(16):     # arpège en croches, une octave au-dessus
            m = notes[MOTIF[c % 8]] + 12
            amp = (0.075 if c % 2 == 0 else 0.055) * H["arpege"]
            if H["arpege"] < 0.8 and c % 2 == 1:
                continue        # humeurs calmes : arpège en noires
            _ajoute(out, _note_piano(hz(m), 0.9, amp), int((t + c * BEAT / 2) * SR))
        for c in range(16):     # frémissement : souffle très court à contretemps
            if c % 2 == 1:
                L = int(0.05 * SR)
                bruit = rng.standard_normal(L)
                bruit = np.diff(bruit, prepend=0) * np.exp(-np.arange(L) / SR * 90)
                _ajoute(out, 0.012 * bruit, int((t + c * BEAT / 2) * SR))
        t += d
        k += 1
    out = _reverb(out)
    return out[:int(duree * SR)]


def souffle(duree=1.4):
    """Bruitage de transition : souffle qui monte puis retombe."""
    n = int(duree * SR)
    rng = np.random.default_rng(11)
    x = rng.standard_normal(n)
    t = np.arange(n) / n
    # passe-bas d'ordre 1 dont la coupure balaie
    coup = 0.02 + 0.25 * np.sin(np.pi * t) ** 2
    y = np.zeros(n)
    acc = 0.0
    for i in range(n):
        acc += coup[i] * (x[i] - acc)
        y[i] = acc
    env = np.sin(np.pi * t) ** 1.5
    return 0.5 * y * env / (np.abs(y).max() + 1e-9)


def cloche(freq=880.0, duree=2.4):
    n = int(duree * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * freq * 2.76 * t) * np.exp(-t * 2)
         + 0.25 * np.sin(2 * np.pi * freq * 5.4 * t) * np.exp(-t * 4))
    return 0.22 * s * np.exp(-t * 1.8) * np.minimum(1, t / 0.003)


def enveloppe(duree, paroles, haut=1.0, bas=0.11, attaque=0.25, relache=0.9):
    """Gain de la musique : bas pendant la parole (intervalles [t0, t1]), haut sinon, transitions douces."""
    n = int(duree * SR)
    cible = np.full(n, haut)
    for a, b in paroles:
        i, j = int(max(0, a - 0.15) * SR), int(min(duree, b + 0.25) * SR)
        cible[i:j] = bas
    # lissage asymétrique (descente rapide, remontée lente), sous-échantillonné pour aller vite
    pas = 240
    c = cible[::pas]
    g = np.empty_like(c)
    v = c[0]
    ka, kr = pas / (attaque * SR), pas / (relache * SR)
    for i, x in enumerate(c):
        v += (x - v) * (ka if x < v else kr)
        g[i] = v
    return np.repeat(g, pas)[:n]
