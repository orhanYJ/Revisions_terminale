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


def boucle(duree, humeur="lumiere"):
    """Musique brute (sans dosage) de la durée demandée, dans l'humeur choisie."""
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
