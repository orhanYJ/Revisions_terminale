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


def boucle(duree, humeur="lumiere"):
    """Musique brute (sans dosage) de la durée demandée, dans l'humeur choisie."""
    if humeur == "reel":
        return reel(duree)
    if humeur.startswith("pc-"):       # vidéos de physique-chimie : musique « labo »
        return labo(duree, humeur[3:])
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


# ---------------------------------------------------------------------------------------------------------------
# Musique « labo » des vidéos de physique-chimie (11/2026, demande de Cengiz : « change de musique de fond, c'est tout
# le temps la même chose ») : une identité sonore propre à la matière, composée ici. Marimba en modulation de fréquence,
# basse synthétique, nappe large, pulsation douce (grosse caisse feutrée, charleston léger) et petites bulles qui
# montent, comme dans une solution. Quatre variantes (les humeurs des scripts), même instrumentation.
LABO = {
    # bpm, accords (basse, notes) sur deux mesures, densité du marimba, pulsation, bulles
    "lumiere": dict(bpm=100, accords=[(41, [53, 57, 60, 64, 67]), (38, [50, 53, 57, 60, 64]),       # Fa maj7(9), Ré m9
                                      (46, [50, 53, 57, 60, 62]), (48, [52, 55, 60, 62, 67])],      # Si♭ maj7, Do add9
                    motif=[0, 3, 2, 4, 1, 3, 2, 4], marimba=1.0, pulse=1.0, bulles=0.6),
    "mystere": dict(bpm=88, accords=[(38, [50, 53, 57, 62, 64]), (46, [50, 53, 57, 58, 65]),       # Ré m(9), Si♭ maj7
                                     (43, [50, 53, 55, 58, 62]), (45, [49, 52, 55, 57, 62])],      # Sol m7, La7sus
                    motif=[0, 2, 4, 2, 3, 1, 4, 2], marimba=0.6, pulse=0.5, bulles=1.0),
    "tension": dict(bpm=108, accords=[(40, [52, 55, 59, 62, 66]), (36, [52, 55, 59, 60, 64]),      # Mi m9, Do maj7
                                      (45, [52, 55, 57, 60, 64]), (47, [51, 54, 57, 59, 64])],     # La m7, Si7sus
                    motif=[0, 4, 2, 4, 1, 4, 3, 4], marimba=1.0, pulse=1.25, bulles=0.4),
    "calme": dict(bpm=84, accords=[(36, [52, 55, 59, 60, 64]), (45, [52, 55, 57, 60, 64]),         # Do maj7, La m7
                                   (41, [52, 57, 60, 64, 65]), (43, [50, 55, 59, 62, 64])],        # Fa maj7, Sol6
                  motif=[0, 2, 3, 4, 3, 2, 1, 2], marimba=0.7, pulse=0.45, bulles=0.8),
}


def _marimba(f, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    ind = 2.2 * np.exp(-t * 18)                           # modulation qui s'éteint vite : attaque boisée
    s = np.sin(2 * np.pi * f * t + ind * np.sin(2 * np.pi * 4 * f * t)) + 0.18 * np.sin(2 * np.pi * 10 * f * t) * np.exp(-t * 30)
    env = np.exp(-t * 5.5) * np.minimum(1, t / 0.002)
    return amp * env * s


def _basse_synth(f, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.tanh(2.2 * (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)))
    env = np.minimum(1, t / 0.008) * np.exp(-t * 2.6)
    return amp * env * s


def _nappe_large(freqs, dur, amp):
    n = int(dur * SR)
    t = np.arange(n) / SR
    att = np.minimum(1, t / 2.2)
    rel = np.minimum(1, (dur - t) / 1.6).clip(0, 1)
    s = np.zeros(n)
    for i, f in enumerate(freqs):
        for d, p in ((-1.1, 0.0), (0.0, 1.3), (1.1, 2.1)):
            s += np.sin(2 * np.pi * (f + d) * t + p + i)
        s += 0.12 * np.sin(2 * np.pi * 3 * f * t + i) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.11 * t + i))
    return amp * att * rel * s / (3.2 * len(freqs))


def _caisse(amp):
    n = int(0.32 * SR)
    t = np.arange(n) / SR
    f = 46 + 70 * np.exp(-t * 28)
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 11)


def _charleston(rng, amp):
    L = int(0.045 * SR)
    b = rng.standard_normal(L)
    b = np.diff(np.diff(b, prepend=0), prepend=0)         # bruit éclairci (aigus)
    return amp * b * np.exp(-np.arange(L) / SR * 85)


def _bulle(rng, amp):
    d = 0.05 + 0.05 * rng.random()
    n = int(d * SR)
    t = np.arange(n) / SR
    f0 = 500 + 500 * rng.random()
    f = f0 * (1 + 1.6 * t / d)                            # la bulle monte
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / d) ** 2


def labo(duree, humeur="lumiere"):
    """Musique « labo » brute (sans dosage) de la durée demandée, dans l'humeur choisie."""
    H = LABO.get(humeur, LABO["lumiere"])
    beat = 60.0 / H["bpm"]
    n = int(duree * SR) + SR
    out = np.zeros(n)
    rng = np.random.default_rng(17)
    mesure = 4 * beat
    t, k = 0.0, 0
    while t < duree:
        basse, notes = H["accords"][k % 4]
        d = 2 * mesure
        i0 = int(t * SR)
        _ajoute(out, _nappe_large([hz(m) for m in notes[:4]], d + 1.4, 0.16), i0)
        # basse : sur le temps, puis une croche avant le temps suivant (petit balancement)
        for b in (0, 1.5, 4, 5.5):
            _ajoute(out, _basse_synth(hz(basse), 0.9, 0.075), int((t + b * beat) * SR))
        # marimba : motif en croches, une note sur deux sautée dans les humeurs calmes ; variation toutes les 4 mesures
        var = 1 if (k // 2) % 2 else 0
        for c in range(16):
            if H["marimba"] < 0.8 and c % 2 == 1:
                continue
            idx = H["motif"][(c + 3 * var) % 8] % len(notes)
            m = notes[idx] + 12
            amp = (0.11 if c % 4 == 0 else 0.08) * H["marimba"]
            _ajoute(out, _marimba(hz(m), 0.8, amp), int((t + c * beat / 2) * SR))
        # pulsation feutrée
        if H["pulse"] > 0:
            for b in range(8):
                if b % 2 == 0:
                    _ajoute(out, _caisse(0.085 * H["pulse"]), int((t + b * beat) * SR))
                _ajoute(out, _charleston(rng, 0.026 * H["pulse"]), int((t + (b + 0.5) * beat) * SR))
        # bulles : quelques-unes par mesure, placées au hasard (graine fixe)
        for _ in range(int(round(3 * H["bulles"]))):
            _ajoute(out, _bulle(rng, 0.05 * H["bulles"]), int((t + rng.random() * d) * SR))
        t += d
        k += 1
    out = _reverb(out, duree=1.8, mix=0.26)
    return out[:int(duree * SR)]
