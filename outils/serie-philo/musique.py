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


def boucle(duree, humeur="lumiere", site=None, graine="", style=None):
    """Musique brute (sans dosage) de la durée demandée, dans l'humeur choisie.

    Pour un site à identité sonore (IDENTITES : maths, ses, hggsp), musique composée d'un seul tenant (voir piste)."""
    if site in IDENTITES:
        return piste(duree, [(0.0, humeur)], site, graine, style)
    if humeur == "reel":
        return reel(duree)
    if humeur in ("salon", "archives", "marche"):
        return {"salon": salon, "archives": archives, "marche": marche}[humeur](duree)
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


# =====================================================================================================================
# Identités sonores des spécialités publiques : maths, SES, HGGSP (10/11/2026)
# =====================================================================================================================
# Demande de Cengiz : « change la musique de fond, ça devient vraiment répétitif ; une musique pour chaque spé ».
# Trois propositions par site, au choix du pilote (STYLES : maths1-3, ses1-3, hggsp1-3 ; celle qui sert est STYLE[site],
# en fin de fichier ; piste(…, style=…) en force une autre). Propositions 1 (les deux autres sont décrites plus bas) :
#   maths  : piano feutré, marimba / pizzicato discrets, motifs minimalistes additifs, modes lumineux (ré dorien,
#            sol mixolydien, fa lydien), 72-80 battements par minute ;
#   ses    : groove lo-fi doux (grosse caisse feutrée, caisse claire aux balais, charleston), piano électrique FM
#            façon Rhodes, basse ronde qui bouge, accords de septième et de neuvième, 86-94 battements ;
#   hggsp  : cordes graves tenues (scies filtrées, vibrato lent), ostinato de cordes basses, timbales et grands
#            tambours lointains, appels de cuivres au début de chaque partie, éolien et phrygien, 66-76 battements.
# Contre la répétition : la vidéo n'est plus une boucle. Chaque partie (scène du script) est composée à part, avec
# sa graine (code de la vidéo + numéro de scène) : tonalité et grilles d'accords tirées dans la banque de l'humeur,
# forme en phrases de 8 ou 16 mesures (intro, A, B, pont, respirations dépouillées), instruments qui entrent et
# sortent d'une phrase à l'autre, motifs et rythmes qui varient. Déterministe : même code, même musique.
# Les autres sites (philo, pc, svt, dnl, acl-lughnasa) gardent exactement la boucle ci-dessus.
import hashlib  # noqa: E402

IDENTITES = ("maths", "ses", "hggsp")
RMS_CIBLE = 0.075     # niveau de l'ancienne boucle ramenée à une crête de 0,42 par generer.py (mesuré le 10/11/2026)
CRETE = 0.42          # crête maximale : la musique ne doit jamais dépasser la voix dans le mixage de generer.py

MODES = {"ionien": [0, 2, 4, 5, 7, 9, 11], "dorien": [0, 2, 3, 5, 7, 9, 10], "phrygien": [0, 1, 3, 5, 7, 8, 10],
         "lydien": [0, 2, 4, 6, 7, 9, 11], "mixolydien": [0, 2, 4, 5, 7, 9, 10], "eolien": [0, 2, 3, 5, 7, 8, 10]}
QUAL = {"M": [0, 4, 7], "m": [0, 3, 7], "5": [0, 7, 12], "sus2": [0, 2, 7], "sus4": [0, 5, 7], "add9": [0, 4, 7, 14],
        "madd9": [0, 3, 7, 14], "maj7": [0, 4, 7, 11], "maj9": [0, 4, 7, 11, 14], "m7": [0, 3, 7, 10],
        "m9": [0, 3, 7, 10, 14], "m11": [0, 3, 7, 10, 14, 17], "7": [0, 4, 7, 10], "9": [0, 4, 7, 10, 14],
        "13": [0, 4, 10, 14, 21], "9sus4": [0, 5, 7, 10, 14], "7sus4": [0, 5, 7, 10], "m7b5": [0, 3, 6, 10]}

# Banques harmoniques : par site et par humeur, des tonalités (mode, basse de la tonique en MIDI, grilles).
# Une grille = une suite d'accords « fondamentale:qualité[/basse] » (demi-tons au-dessus de la tonique), tous
# diatoniques au mode, pour que motifs et mélodies tirés dans la gamme restent consonants.
BANQUES = {
    "maths1": {
        "lumiere": dict(bpm=78, tons=[
            ("dorien", 38, [["0:m9", "5:add9", "0:m7", "10:maj7"], ["0:m7", "7:m7", "10:maj7", "5:sus2"],
                            ["3:maj7", "5:add9", "0:m9", "0:m9"], ["0:sus2", "10:add9", "5:add9", "0:m7"]]),
            ("mixolydien", 43, [["0:add9", "10:add9/0", "5:add9/0", "0:sus2"], ["0:M", "7:m7", "10:maj7", "5:add9"],
                                ["5:maj7", "10:add9", "0:add9", "0:sus4"], ["9:m7", "5:maj7", "10:add9", "0:add9"]])]),
        "mystere": dict(bpm=72, tons=[
            ("dorien", 38, [["0:m9", "0:m9", "10:maj7", "10:maj7"], ["0:sus2", "3:maj7", "0:m7", "7:m7"],
                            ["0:m11", "5:sus2", "3:maj7", "0:sus2"]]),
            ("eolien", 45, [["0:madd9", "8:maj7", "0:madd9", "3:add9"], ["0:m7", "5:m7", "8:maj9", "7:m7"],
                            ["8:maj7", "10:sus2", "0:m9", "0:m9"]])]),
        "tension": dict(bpm=80, tons=[
            ("eolien", 45, [["0:m", "8:maj7", "10:sus2", "7:m7"], ["0:m7", "0:m7", "5:m7", "8:add9"],
                            ["0:m", "10:M", "8:maj7", "10:sus4"], ["5:m7", "7:m7", "8:maj7", "10:M"]]),
            ("phrygien", 40, [["0:m", "1:maj7", "0:m", "10:sus2"], ["0:m7", "1:M", "3:M", "0:m"],
                              ["8:maj7", "1:maj7", "0:sus4", "0:m"]])]),
        "calme": dict(bpm=72, tons=[
            ("lydien", 41, [["0:maj7", "2:add9/0", "0:maj7", "7:sus2"], ["0:maj9", "9:m7", "4:m7", "2:add9"],
                            ["7:sus2", "2:M", "0:maj7", "0:maj9"]]),
            ("ionien", 36, [["0:add9", "9:m7", "5:maj7", "7:sus4"], ["5:maj9", "0:add9", "2:m7", "7:sus2"],
                            ["9:m7", "4:m7", "5:maj7", "0:add9"]])]),
    },
    "ses1": {
        "lumiere": dict(bpm=90, tons=[
            ("ionien", 36, [["5:maj7", "4:m7", "2:m9", "0:maj9"], ["0:maj9", "9:m9", "2:m9", "7:9sus4"],
                            ["5:maj9", "7:13", "4:m7", "9:m9"], ["2:m9", "7:13", "0:maj9", "0:maj9"]]),
            ("ionien", 41, [["5:maj7", "4:m7", "2:m9", "0:maj9"], ["2:m9", "7:9sus4", "0:maj9", "9:m7"],
                            ["0:maj9", "4:m7", "5:maj9", "7:13"]])]),
        "mystere": dict(bpm=86, tons=[
            ("dorien", 45, [["0:m9", "5:9", "0:m9", "5:9"], ["0:m9", "5:9", "3:maj7", "2:m7"],
                            ["0:m11", "10:maj9", "5:13", "0:m9"]]),
            ("dorien", 38, [["0:m9", "5:13", "3:maj7", "0:m11"], ["0:m11", "0:m11", "10:maj9", "5:9"]])]),
        "tension": dict(bpm=94, tons=[
            ("eolien", 40, [["0:m9", "8:maj7", "3:maj7", "10:9sus4"], ["0:m7", "5:m9", "8:maj9", "10:9sus4"],
                            ["0:m9", "0:m9", "8:maj9", "7:m7"]]),
            ("eolien", 45, [["0:m9", "5:m9", "8:maj7", "7:m7"], ["0:m7", "10:9sus4", "8:maj7", "7:m7"]])]),
        "calme": dict(bpm=86, tons=[
            ("ionien", 41, [["0:maj9", "2:m7", "4:m7", "5:maj7"], ["5:maj9", "4:m7", "2:m9", "7:9sus4"],
                            ["0:maj9", "9:m9", "5:maj9", "7:9sus4"]]),
            ("ionien", 43, [["0:maj9", "4:m7", "5:maj9", "2:m9"], ["9:m9", "2:m9", "0:maj9", "5:maj7"]])]),
    },
    "hggsp1": {
        "lumiere": dict(bpm=72, tons=[
            ("eolien", 45, [["0:m", "8:M", "3:M", "10:M"], ["0:m", "10:M", "8:M", "10:sus4"],
                            ["5:m", "8:M", "10:sus4", "0:m"], ["8:M", "3:M", "10:M", "0:sus2"]]),
            ("eolien", 38, [["0:m", "8:M", "3:M", "10:M"], ["0:m", "5:m", "8:M", "10:M"],
                            ["3:M", "10:M", "0:m", "0:sus4"]])]),
        "mystere": dict(bpm=66, tons=[
            ("phrygien", 40, [["0:m", "1:M", "0:m", "1:M"], ["0:m", "10:m", "1:M", "0:sus4"],
                              ["0:5", "1:maj7", "8:M", "0:m"]]),
            ("eolien", 45, [["0:m", "0:m", "8:M", "8:M"], ["0:sus2", "5:m", "0:m", "7:m"]])]),
        "tension": dict(bpm=76, tons=[
            ("eolien", 38, [["0:m", "10:M", "8:M", "7:m"], ["0:m", "0:m", "8:M", "10:M"],
                            ["0:m", "5:m", "8:M", "7:m"]]),
            ("phrygien", 40, [["0:m", "1:M", "3:M", "1:M"], ["0:m", "1:M", "0:m", "10:m"],
                              ["0:5", "1:M", "8:M", "0:m"]])]),
        "calme": dict(bpm=66, tons=[
            ("eolien", 43, [["0:m", "5:m", "8:M", "3:M"], ["0:sus2", "8:maj7", "3:M", "10:M"],
                            ["8:M", "3:M", "5:m", "0:m"]]),
            ("eolien", 41, [["0:m", "8:M", "5:m", "0:m"], ["3:M", "10:M", "8:maj7", "0:sus2"]])]),
    },
}


def _rng(*parts):
    return np.random.default_rng(int(hashlib.sha1("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()[:15], 16))


def _accord(code, centre):
    """« 5:add9/0 » → dict : basse (MIDI), fondamentale, intervalles ; la basse reste dans la quinte de la tonique."""
    tete, _, b = code.partition("/")
    r, q = tete.split(":")
    r = int(r)
    b = int(b) if b else r
    basse = centre + (b if b <= 6 else b - 12)
    return {"basse": basse, "r": centre + r, "iv": QUAL[q]}


def _voix(acc, centre_haut):
    """Notes de l'accord repliées autour de centre_haut : les accords successifs bougent peu (voix conjointes)."""
    return sorted({p + 12 * round((centre_haut - p) / 12) for p in (acc["r"] + iv for iv in acc["iv"])})


def _gamme(mode, centre, bas, haut):
    return [p for p in range(bas, haut + 1) if (p - centre) % 12 in MODES[mode]]


def _bords(x, fin=0.012):
    """Aucun clic : chaque note commence et finit à zéro."""
    k = min(len(x) // 2, int(fin * SR))
    if k > 1:
        x[-k:] *= np.linspace(1, 0, k)
        x[0] = 0.0
    return x


_FILTRES = {}


def _filtre_id(x, kind, fc, ordre=2):
    from scipy import signal
    cle = (kind, tuple(np.atleast_1d(fc)), ordre)
    if cle not in _FILTRES:
        _FILTRES[cle] = signal.butter(ordre, fc, btype=kind, fs=SR, output="sos")
    return signal.sosfilt(_FILTRES[cle], x)


def _creux(x, f0=2600.0, gain_db=-3.0, q=0.7):
    """Égaliseur en cloche (RBJ) : léger creux là où la voix porte, pour qu'elle reste intelligible."""
    from scipy import signal
    A = 10 ** (gain_db / 40)
    w = 2 * np.pi * f0 / SR
    al = np.sin(w) / (2 * q)
    b = np.array([1 + al * A, -2 * np.cos(w), 1 - al * A])
    a = np.array([1 + al / A, -2 * np.cos(w), 1 - al / A])
    return signal.lfilter(b / a[0], a / a[0], x)


def _ir(duree, sombre, graine, predelai=0.0):
    rng = np.random.default_rng(graine)
    n = int((duree + predelai) * SR)
    t = np.arange(n) / SR
    ir = rng.standard_normal(n) * np.exp(-6.9 * np.maximum(0, t - predelai) / duree)
    ir[t < predelai] = 0
    ir = _filtre_id(ir, "lowpass", sombre)
    ir /= np.sqrt((ir ** 2).sum())
    return ir


def _salle(x, duree, mix, sombre, graine, predelai=0.0, sec=True):
    from scipy import signal
    y = signal.oaconvolve(x, _ir(duree, sombre, graine, predelai))[:len(x)]
    return ((1 - mix) * x if sec else 0) + mix * y


# ---------------------------------------------------------------------------------------------------- instruments
def _piano_feutre_id(f, dur, amp, clair=0.5):
    """Piano feutré : marteau doux, peu d'harmoniques aigus, double décroissance (attaque puis résonance)."""
    n = int((dur + 1.6) * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 8):
        fk = k * f * np.sqrt(1 + 0.00025 * k * k)
        if fk > 7000:
            break
        dk = (0.55 + 0.9 * (k - 1)) * (f / 262) ** 0.35
        s += clair ** (k - 1) / k * (0.55 * np.exp(-t * dk * 3.5) + 0.45 * np.exp(-t * dk * 0.7)) * np.sin(2 * np.pi * fk * t + 0.3 * k)
    s *= (1 - np.exp(-t / 0.006)) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.25))
    return _bords(amp * s)


def _marimba(f, amp):
    n = int(1.4 * SR)
    t = np.arange(n) / SR
    d = 3.0 * (f / 440) ** 0.5 + 1.0
    s = np.sin(2 * np.pi * f * t) * np.exp(-d * t)
    if 3.93 * f < 10000:
        s += 0.22 * np.sin(2 * np.pi * 3.93 * f * t) * np.exp(-3.5 * d * t)
    if 9.2 * f < 10000:
        s += 0.05 * np.sin(2 * np.pi * 9.2 * f * t) * np.exp(-7 * d * t)
    return _bords(amp * s * (1 - np.exp(-t / 0.0015)))


def _pizz_id(f, amp):
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 7):
        if k * f < 8000:
            s += k ** -1.2 * np.exp(-t * (4 + 3 * k)) * np.sin(2 * np.pi * k * f * t + k)
    return _bords(amp * s * (1 - np.exp(-t / 0.002)))


def _rhodes_id(f, dur, amp, vel=0.7):
    """Piano électrique en synthèse FM (rapport 1:1, indice qui retombe) avec la petite cloche de l'attaque."""
    n = int((dur + 0.9) * SR)
    t = np.arange(n) / SR
    idx = (0.6 + 1.6 * vel) * np.exp(-t * 4.0) + 0.18
    s = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    if 14 * f < 9000:
        s += 0.10 * vel * np.exp(-t * 30) * np.sin(2 * np.pi * 14 * f * t)
    env = (0.65 * np.exp(-t * 1.4) + 0.35 * np.exp(-t * 0.35)) * (1 - np.exp(-t / 0.003))
    env *= np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.12)) * (1 + 0.10 * np.sin(2 * np.pi * 4.2 * t))
    return _bords(amp * env * s)


def _basse_ronde_id(f, dur, amp):
    n = int((dur + 0.2) * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.5 * np.sin(4 * np.pi * f * t) * np.exp(-t * 2)
         + 0.18 * np.sin(6 * np.pi * f * t) * np.exp(-t * 5))
    s *= (1 - np.exp(-t / 0.008)) * np.exp(-t * 0.9) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.06))
    return _bords(amp * s)


def _grosse_caisse_id(amp):
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(62 + 45 * np.exp(-t / 0.03)) / SR
    return _bords(amp * np.sin(ph) * np.exp(-t * 11) * (1 - np.exp(-t / 0.002)))


def _balai_id(amp, rng, long=False):
    """Caisse claire aux balais : souffle filtré qui glisse, petit choc de peau."""
    n = int((0.38 if long else 0.22) * SR)
    t = np.arange(n) / SR
    b = _filtre_id(rng.standard_normal(n), "bandpass", [900, 5500])
    s = b * (1 - np.exp(-t / 0.012)) * np.exp(-t * (7 if long else 14)) + 0.5 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 28)
    return _bords(amp * s)


def _charley_id(amp, rng, ouvert=False):
    n = int((0.25 if ouvert else 0.08) * SR)
    t = np.arange(n) / SR
    s = _filtre_id(rng.standard_normal(n), "highpass", 7000) * np.exp(-t * (12 if ouvert else 55))
    return _bords(amp * s * (1 - np.exp(-t / 0.001)))


def _scie(f, n, cents, rng, vib=0.0035, vib_f=5.0, retard=0.4):
    """Dent de scie à bande limitée (PolyBLEP), vibrato qui s'installe après l'attaque."""
    t = np.arange(n) / SR
    fr = f * 2 ** (cents / 1200) * (1 + vib * np.sin(2 * np.pi * vib_f * t + rng.uniform(0, 6.28)) * np.clip((t - retard) / 0.6, 0, 1))
    dt = fr / SR
    ph = (rng.uniform() + np.cumsum(dt)) % 1.0
    y = 2 * ph - 1
    m = ph < dt
    x = ph[m] / dt[m]
    y[m] -= x + x - x * x - 1
    m = ph > 1 - dt
    x = (ph[m] - 1) / dt[m]
    y[m] -= x * x + x + x + 1
    return y


def _cordes(f, dur, amp, coupure, rng, attaque=0.7, voix=3):
    """Pupitre de cordes tenues : trois scies désaccordées, vibrato lent, filtre passe-bas, attaque lente."""
    n = int((dur + 1.3) * SR)
    t = np.arange(n) / SR
    s = sum(_scie(f, n, c, rng, vib_f=4.6 + 0.35 * i) for i, c in enumerate((-8, 1, 7)[:voix])) / voix
    s = _filtre_id(s, "lowpass", coupure)
    s *= (1 - np.exp(-t / (attaque / 3))) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.45))
    return _bords(amp * s)


def _spiccato(f, amp, rng, coupure=950):
    n = int(0.24 * SR)
    t = np.arange(n) / SR
    s = (_scie(f, n, -4, rng, vib=0) + _scie(f, n, 5, rng, vib=0)) / 2
    return _bords(amp * _filtre_id(s, "lowpass", coupure) * (1 - np.exp(-t / 0.006)) * np.exp(-t * 15))


def _cor(f, dur, amp, rng):
    """Cuivre de synthèse : légère montée de hauteur à l'attaque, son qui s'ouvre puis se pose."""
    n = int((dur + 0.5) * SR)
    t = np.arange(n) / SR
    fr = f * (1 - 0.012 * np.exp(-t / 0.05))
    s = 0.5 * (_scie(fr, n, -3, rng, vib=0.002, retard=0.5) + _scie(fr, n, 3, rng, vib=0.002, retard=0.5))
    sombre, clair = _filtre_id(s, "lowpass", 450), _filtre_id(s, "lowpass", 2000)
    b = np.clip((1 - np.exp(-t / 0.12)) * (0.75 + 0.25 * np.exp(-t * 1.2)), 0, 1)
    y = sombre * (1 - b) + clair * b
    y *= (1 - np.exp(-t / 0.035)) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.18))
    return _bords(amp * y)


def _timbale_id(f, amp, rng):
    n = int(2.6 * SR)
    t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(f * (1 + 0.02 * np.exp(-t / 0.04))) / SR
    s = (np.sin(ph) * np.exp(-t * 1.6) + 0.5 * np.sin(1.5 * ph) * np.exp(-t * 2.4)
         + 0.35 * np.sin(1.99 * ph) * np.exp(-t * 3.0) + 0.15 * np.sin(2.44 * ph) * np.exp(-t * 4.0))
    s += 0.4 * _filtre_id(rng.standard_normal(n), "lowpass", 600) * np.exp(-t * 60)
    return _bords(amp * s * (1 - np.exp(-t / 0.002)))


def _grand_tambour(amp, rng):
    n = int(1.6 * SR)
    t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(52 + 22 * np.exp(-t / 0.06)) / SR
    s = np.sin(ph) * np.exp(-t * 4) + 0.6 * _filtre_id(rng.standard_normal(n), "lowpass", 260) * np.exp(-t * 8)
    return _bords(amp * s * (1 - np.exp(-t / 0.004)))


# ------------------------------------------------------------------------------------------------ forme d'une partie
def _forme(nmes, rng):
    """Plan d'une partie : [(type, mesures)] ; types intro, A, B, pont, respiration (passage dépouillé)."""
    plan, total, prec, sans_resp = [("intro", 4)], 4, "intro", 0
    suite = {"intro": ["A"], "A": ["A", "B", "B", "pont"], "B": ["A", "pont", "B"], "pont": ["B", "A"],
             "respiration": ["A", "B"]}
    while total < nmes:
        if sans_resp >= 4 or (sans_resp >= 2 and rng.random() < 0.3):
            typ = "respiration"
        else:
            typ = str(rng.choice(suite[prec]))
            if typ == prec == "B":
                typ = "A"
        long_ = 16 if typ in ("A", "B") and rng.random() < 0.35 else 8
        plan.append((typ, long_))
        total += long_
        sans_resp = 0 if typ == "respiration" else sans_resp + 1
        prec = typ
    return plan


def _place(buf, x, t):
    _ajoute(buf, x, int(max(0.0, t) * SR))


# ------------------------------------------------------------------------------------------------------------ maths
def _couches_maths(typ, rng, hu):
    if typ == "intro":
        return {"accords"} if rng.random() < 0.5 else {"nappe", "motif"}
    if typ == "respiration":
        return [{"accords"}, {"nappe", "motif"}, {"accords", "nappe"}][rng.integers(3)]
    if typ == "pont":
        return [{"nappe", "pouls", "basse"}, {"nappe", "motif", "basse"}, {"accords", "pouls"}][rng.integers(3)]
    c = {"accords", "basse", "motif"}
    if typ == "B" or rng.random() < 0.3:
        c.add("pouls")
    if rng.random() < (0.5 if hu in ("mystere", "calme") else 0.3):
        c.add("nappe")
    if typ == "B" and rng.random() < 0.25:
        c.discard("accords")
    return c


def _mesure_maths(bus, cx, t, j, L, typ, acc, couches, rng):
    beat, mes, hu = cx["beat"], 4 * cx["beat"], cx["hu"]
    clair = {"lumiere": 0.55, "mystere": 0.38, "tension": 0.5, "calme": 0.45}[hu]
    vel = lambda: 1 + rng.normal(0, 0.08)               # noqa: E731
    jeu = lambda: rng.normal(0, 0.006)                  # noqa: E731  (léger décalage humain)
    nouvel_acc = j % cx["hr"] == 0
    v = _voix(acc, 57 if hu == "mystere" else 60)
    if "accords" in couches and nouvel_acc:
        rythme = cx["rythme_acc"]
        for deb, d in rythme:
            for k, p in enumerate(v):
                _place(bus["sec"], _piano_feutre_id(hz(p), d * beat * (cx["hr"] if len(rythme) == 1 else 1), 0.034 * vel() * (0.8 if deb else 1), clair),
                       t + deb * beat + 0.012 * k + jeu())
    if "basse" in couches and nouvel_acc:
        _place(bus["sec"], _piano_feutre_id(hz(acc["basse"]), cx["hr"] * mes * 0.9, 0.065 * vel(), clair * 0.8), t + jeu())
        if cx["hr"] == 2 and rng.random() < 0.35:
            _place(bus["sec"], _piano_feutre_id(hz(acc["basse"] + 7), mes, 0.05 * vel(), clair * 0.8), t + mes + 2 * beat + jeu())
    if "nappe" in couches and nouvel_acc:
        _place(bus["sec"], _nappe([hz(p) for p in v[:3]], cx["hr"] * mes + 1.0, 0.075 if hu in ("mystere", "calme") else 0.06), t)
    if "motif" in couches:
        # motif minimaliste additif : les croches du motif s'ajoutent l'une après l'autre (ou se retirent)
        if typ == "respiration":
            nb = 2 + j % 2
        elif cx["sens"] > 0:
            nb = min(8, 2 + j)
        else:
            nb = max(3, 8 - j)
        actifs = set(cx["ordre"][:nb].tolist())
        tons = sorted({p + 12 * o for p in v for o in (1, 2) if 66 <= p + 12 * o <= 86})
        inst = cx["inst_motif"]
        for c in range(8):
            if c in actifs:
                p = tons[cx["motif"][c] % len(tons)]
                a = (0.040 if c % 2 == 0 else 0.030) * vel()
                x = _piano_feutre_id(hz(p), beat * 0.7, a, clair) if inst == "piano" else _marimba(hz(p), a * 1.1)
                _place(bus["sec"], x, t + c * beat / 2 + jeu())
    if "pouls" in couches:
        bas = sorted({p for p in (acc["basse"] + 12, acc["basse"] + 19, acc["basse"] + 24)})
        for c in cx["pouls"]:
            p = bas[(c * 2 + j) % len(bas)]
            a = 0.030 * vel() * (1.15 if c == 0 else 1)
            x = _marimba(hz(p), a) if cx["inst_pouls"] == "marimba" else _pizz_id(hz(p), a * 1.2)
            _place(bus["sec"], x, t + c * beat / 2 + jeu())


def _phrase_maths(cx, typ, rng):
    cx["hr"] = 2 if cx["hu"] in ("mystere", "calme") or rng.random() < 0.4 else 1
    cx["rythme_acc"] = [[(0, 4)], [(0, 4)], [(0, 2), (2, 2)], [(0, 3), (3, 1)]][rng.integers(4)]
    if cx["hr"] == 2:
        cx["rythme_acc"] = [(0, 4)]
    if "motif" not in cx or rng.random() < 0.5:
        cx["motif"] = rng.integers(0, 6, 8)
        cx["ordre"] = np.concatenate([[0], 1 + rng.permutation(7)])
    else:  # variation : rotation ou une note changée
        if rng.random() < 0.5:
            cx["motif"] = np.roll(cx["motif"], int(rng.integers(1, 4)))
        else:
            cx["motif"] = cx["motif"].copy()
            cx["motif"][rng.integers(8)] = rng.integers(0, 6)
    cx["sens"] = -1 if typ in ("pont",) or (typ == "A" and rng.random() < 0.3) else 1
    cx["inst_motif"] = "marimba" if rng.random() < (0.45 if cx["hu"] in ("lumiere", "tension") else 0.2) else "piano"
    cx["inst_pouls"] = "pizz" if cx["hu"] in ("mystere", "tension") and rng.random() < 0.7 else "marimba"
    cx["pouls"] = [[0, 3, 6], [0, 3, 6, 7], [0, 2, 3, 5, 6], [0, 1, 3, 4, 6]][rng.integers(4 if cx["hu"] == "tension" else 2)]


def _mix_maths(bus, hu, graine):
    return _salle(bus["sec"], 1.8, 0.30, 4500, graine)


# -------------------------------------------------------------------------------------------------------------- ses
PAT_RHODES = [[(0, 6)], [(0, 3), (3, 5)], [(0, 2), (3, 2), (6, 2)], [(1, 3), (4, 4)], [(0, 1.5), (2, 2), (5, 3)], [(0, 8)]]
PAT_BASSE = [[(0, "R", 3), (3, "5", 2), (6, "8", 1), (7, "a", 1)], [(0, "R", 5), (5, "R", 1), (6, "5", 2)],
             [(0, "R", 2), (3, "R", 1), (4, "5", 3), (7, "a", 1)], [(0, "R", 7)], [(0, "R", 3), (3, "8", 1), (4, "5", 2), (6, "R", 2)]]
PAT_GC = [[0, 5], [0, 3, 5], [0, 5, 7], [0, 2, 5], [0, 3]]


def _croche(c, beat, swing=0.58):
    return beat * (c // 2) + (beat * swing if c % 2 else 0.0) + beat * (c - int(c)) / 2


def _couches_ses(typ, rng, hu):
    if typ == "intro":
        return [{"rhodes"}, {"rhodes", "basse"}, {"rhodes", "charley"}][rng.integers(3)]
    if typ == "respiration":
        return [{"rhodes"}, {"rhodes", "nappe"}, {"rhodes", "basse", "charley"}][rng.integers(3)]
    if typ == "pont":
        return [{"rhodes", "basse", "charley", "nappe"}, {"rhodes", "basse", "melodie"}][rng.integers(2)]
    c = {"rhodes", "basse", "batterie", "charley"}
    if typ == "B" and rng.random() < 0.75:
        c.add("melodie")
    elif typ == "A" and rng.random() < 0.2:
        c.add("melodie")
    if rng.random() < (0.4 if hu in ("mystere", "calme") else 0.15):
        c.add("nappe")
    return c


def _mesure_ses(bus, cx, t, j, L, typ, acc, couches, rng):
    beat, hu = cx["beat"], cx["hu"]
    vel = lambda: 1 + rng.normal(0, 0.1)                # noqa: E731
    jeu = lambda: rng.normal(0, 0.007)                  # noqa: E731
    fin_phrase = j == L - 1
    v = _voix(acc, 62)
    if "rhodes" in couches:
        pat = cx["pat_rhodes"] if j % 4 != 3 else PAT_RHODES[rng.integers(len(PAT_RHODES))]
        for deb, d in pat:
            for k, p in enumerate(v):
                _place(bus["sec"], _rhodes_id(hz(p), d * beat / 2, 0.030 * vel(), 0.55 if hu == "calme" else 0.7),
                       t + _croche(deb, beat) + 0.008 * k + jeu())
    if "basse" in couches:
        pat = cx["pat_basse"] if j % 2 == 0 else PAT_BASSE[rng.integers(len(PAT_BASSE))]
        r = acc["basse"]
        suiv = cx["suivant"]["basse"]
        for deb, deg, d in pat:
            p = {"R": r, "5": r + 7, "8": r + 12, "a": suiv + (1 if rng.random() < 0.5 else -1)}[deg]
            if p > 55:
                p -= 12
            _place(bus["sec"], _basse_ronde_id(hz(p), d * beat / 2 * 0.92, 0.085 * vel()), t + _croche(deb, beat) + jeu())
    if "nappe" in couches and j % 2 == 0:
        _place(bus["sec"], _nappe([hz(p) for p in v[:3]], 8 * beat + 1, 0.07), t)
    if "batterie" in couches:
        gc = cx["pat_gc"] if j % 2 == 0 else PAT_GC[cx["gc2"]]
        for c in gc:
            _place(bus["sec"], _grosse_caisse_id(0.12 * vel()), t + _croche(c, beat) + jeu())
        for c in (2, 6):
            _place(bus["sec"], _balai_id(0.055 * vel(), rng, long=rng.random() < 0.3), t + _croche(c, beat) + jeu())
        if rng.random() < 0.3 or fin_phrase:
            for c in ((5, 7) if fin_phrase else (7,)):
                _place(bus["sec"], _balai_id(0.022 * vel(), rng), t + _croche(c, beat) + jeu())
    if "charley" in couches:
        for c in range(8):
            if rng.random() < 0.1:
                continue
            ouvert = fin_phrase and c == 7
            _place(bus["sec"], _charley_id((0.020 if c % 2 == 0 else 0.012) * vel(), rng, ouvert), t + _croche(c, beat) + jeu())
    if "melodie" in couches and j % 2 == 0 and (j % 4 == 0 or rng.random() < 0.6):
        # phrase de deux mesures dans la pentatonique, qui finit sur une note de l'accord
        pos = cx["rythmes_mel"][rng.integers(len(cx["rythmes_mel"]))]
        i = cx["mel_i"]
        for k, c in enumerate(pos):
            i = int(np.clip(i + rng.choice([-2, -1, -1, 1, 1, 2]), 0, len(cx["penta"]) - 1))
            p = cx["penta"][i]
            if k == len(pos) - 1:
                p = min((q for q in range(p - 6, p + 7) if (q - acc["r"]) % 12 in [iv % 12 for iv in acc["iv"]]), key=lambda q: abs(q - p))
            d = (pos[k + 1] - c) if k + 1 < len(pos) else 3
            _place(bus["sec"], _rhodes_id(hz(p), min(d, 3) * beat / 2, 0.036 * vel(), 0.9), t + _croche(c % 8, beat) + (4 * beat if c >= 8 else 0) + jeu())
        cx["mel_i"] = i


def _phrase_ses(cx, typ, rng):
    cx["hr"] = 1 if rng.random() < 0.7 else 2
    cx["pat_rhodes"] = PAT_RHODES[rng.integers(len(PAT_RHODES))]
    cx["pat_basse"] = PAT_BASSE[rng.integers(len(PAT_BASSE))]
    cx["pat_gc"] = PAT_GC[rng.integers(len(PAT_GC))]
    cx["gc2"] = int(rng.integers(len(PAT_GC)))
    cx["rythmes_mel"] = [[0, 2, 3, 5], [1, 3, 4, 7, 10], [0, 3, 6, 9, 10], [2, 3, 5, 8], [0, 1, 3, 11, 12]]
    if "penta" not in cx:
        mineur = cx["mode"] in ("dorien", "eolien", "phrygien")
        pc = [0, 3, 5, 7, 10] if mineur else [0, 2, 4, 7, 9]
        cx["penta"] = [p for p in range(67, 87) if (p - cx["centre"]) % 12 in pc]
        cx["mel_i"] = len(cx["penta"]) // 2


def _mix_ses(bus, hu, graine):
    x = _salle(bus["sec"], 0.9, 0.18, 5000, graine)
    x = _filtre_id(_filtre_id(x, "lowpass", 6500), "highpass", 50)                      # le grain doux du lo-fi
    return np.tanh(2.0 * x) / 2.0


# ------------------------------------------------------------------------------------------------------------ hggsp
APPELS = [[(0, 0, 1.5), (4, 1.5, 0.5), (4, 2, 1), (3, 3, 1), (4, 4, 4)],
          [(0, 0, 1), (0, 1, 0.5), (4, 1.5, 2.5), (2, 4, 2), (1, 6, 2)],
          [(4, 0, 2), (3, 2, 1), (2, 3, 1), (0, 4, 4)],
          [(0, 0, 0.75), (0, 0.75, 0.25), (4, 1, 3), (5, 4, 1), (4, 5, 3)]]
PAT_OSTINATO = [[0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 1, 0, 0, 2, 1], [0, 1, 0, 1, 0, 2, 0, 1], [0, 0, 2, 0, 0, 1, 0, 0]]


def _couches_hggsp(typ, rng, hu):
    if typ == "intro":
        return {"cordes", "basses"}
    if typ == "respiration":
        return [{"cordes"}, {"cordes", "violons"}, {"basses", "cordes"}][rng.integers(3)]
    if typ == "pont":
        return [{"cordes", "tambours"}, {"basses", "ostinato"}, {"cordes", "violons", "tambours"}][rng.integers(3)]
    c = {"cordes", "basses"}
    p_ost = {"tension": 0.85, "lumiere": 0.5, "mystere": 0.4, "calme": 0.15}[hu]
    if rng.random() < p_ost:
        c.add("ostinato")
    if typ == "B" and rng.random() < (0.3 if hu == "calme" else 0.7):
        c.add("tambours")
    if rng.random() < (0.7 if typ == "B" else 0.4):
        c.add("violons")
    return c


def _mesure_hggsp(bus, cx, t, j, L, typ, acc, couches, rng):
    beat, mes, hu = cx["beat"], 4 * cx["beat"], cx["hu"]
    vel = lambda: 1 + rng.normal(0, 0.07)               # noqa: E731
    coupure = {"lumiere": 1600, "mystere": 1000, "tension": 1400, "calme": 1100}[hu]
    nouvel_acc = j % cx["hr"] == 0
    tenue = cx["hr"] * mes
    v = _voix(acc, 57)
    if "cordes" in couches and nouvel_acc:
        for p in v[:4]:
            _place(bus["sec"], _cordes(hz(p), tenue + 0.25, 0.034 * vel(), coupure, rng), t)
    if "basses" in couches and nouvel_acc:
        r = acc["basse"]
        _place(bus["sec"], _cordes(hz(r), tenue + 0.25, 0.050 * vel(), 900, rng, attaque=0.5), t)
        _place(bus["sec"], _cordes(hz(r + 12), tenue + 0.25, 0.028 * vel(), 1100, rng, attaque=0.6, voix=2), t)
    if "ostinato" in couches:
        r = acc["basse"] + 12
        notes = [r, r + 7, r + 12] if cx["mode"] != "phrygien" else [r, r + 1, r + 7]
        for c, d in enumerate(cx["pat_ost"]):
            a = 0.042 * vel() * (1.3 if c % 4 == 0 else 1)
            _place(bus["sec"], _spiccato(hz(notes[d]), a, rng), t + c * beat / 2 + rng.normal(0, 0.004))
    if "tambours" in couches:
        if nouvel_acc:
            _place(bus["sec"], _timbale_id(hz(cx["centre"] + (0 if j % 4 == 0 else 7) - (12 if cx["centre"] > 43 else 0)), 0.11 * vel(), rng), t)
        if hu in ("tension", "lumiere") and j % 2 == 1:
            _place(bus["loin"], _grand_tambour(0.30 * vel(), rng), t + 2 * beat)
        if j == L - 1:   # roulement qui monte vers la phrase suivante
            pas = beat / 4
            for k in range(12):
                _place(bus["sec"], _timbale_id(hz(cx["centre"] + 7 - (12 if cx["centre"] > 43 else 0)), 0.012 + 0.006 * k, rng), t + mes - 12 * pas + k * pas)
    if "violons" in couches:
        # ligne lente : une blanche ou une ronde, par degrés conjoints, note de l'accord sur le temps fort
        ga = cx["gamme_haut"]
        acc_pc = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
        cible = min((q for q in ga if q % 12 in acc_pc), key=lambda q: abs(q - cx["vl"]))
        cx["vl"] = cible
        if rng.random() < 0.5:
            _place(bus["sec"], _cordes(hz(cible), mes - 0.1, 0.026 * vel(), 2200, rng, attaque=0.45, voix=2), t)
        else:
            _place(bus["sec"], _cordes(hz(cible), 2 * beat, 0.026 * vel(), 2200, rng, attaque=0.4, voix=2), t)
            i = ga.index(cible) + int(rng.choice([-1, 1]))
            q = ga[int(np.clip(i, 0, len(ga) - 1))]
            _place(bus["sec"], _cordes(hz(q), 2 * beat - 0.1, 0.022 * vel(), 2200, rng, attaque=0.35, voix=2), t + 2 * beat)
            cx["vl"] = q
    if cx.get("appel") is not None and j == 0:
        _appel(bus, cx, t, rng, cx.pop("appel"))


def _appel(bus, cx, t, rng, force):
    """Appel de cuivres au début d'une partie : deux cors à l'octave (ou un seul, doux, dans les humeurs calmes)."""
    beat = cx["beat"]
    gamme = MODES[cx["mode"]]
    base = cx["centre"] + 24
    for deg, deb, d in APPELS[cx["n_appel"]]:
        p = base + gamme[deg % 7] + 12 * (deg // 7)
        _place(bus["sec"], _cor(hz(p), d * beat * 0.95, 0.055 * force, rng), t + deb * beat)
        if force > 0.7:
            _place(bus["sec"], _cor(hz(p - 12), d * beat * 0.95, 0.040 * force, rng), t + deb * beat + 0.01)


def _phrase_hggsp(cx, typ, rng):
    cx["hr"] = 1 if cx["hu"] == "tension" and rng.random() < 0.4 else 2
    cx["pat_ost"] = PAT_OSTINATO[rng.integers(len(PAT_OSTINATO))]
    if "gamme_haut" not in cx:
        cx["gamme_haut"] = _gamme(cx["mode"], cx["centre"], 67, 84)
        cx["vl"] = 74
    if typ == "B" and rng.random() < 0.3 and cx["hu"] != "calme":
        cx["appel"] = 0.6
        cx["n_appel"] = int(rng.integers(len(APPELS)))


def _mix_hggsp(bus, hu, graine):
    x = _salle(bus["sec"], 3.2, 0.36, 3500, graine)
    loin = _filtre_id(bus["loin"], "lowpass", 1500)
    return x + _salle(loin, 4.0, 1.0, 1800, graine + 1, predelai=0.06, sec=False)


def _init_hggsp(cx, rng):
    cx["appel"] = 1.0 if cx["hu"] in ("lumiere", "tension") else 0.55
    cx["n_appel"] = int(rng.integers(len(APPELS)))


STYLES = {
    "maths1": dict(couches=_couches_maths, mesure=_mesure_maths, phrase=_phrase_maths, mix=_mix_maths),
    "ses1": dict(couches=_couches_ses, mesure=_mesure_ses, phrase=_phrase_ses, mix=_mix_ses),
    "hggsp1": dict(couches=_couches_hggsp, mesure=_mesure_hggsp, phrase=_phrase_hggsp, mix=_mix_hggsp, init=_init_hggsp),
}


TEXTURES = ("depouillee", "normale", "pleine")


def _parle(cx, a, b):
    """Vrai si la voix parle entre a et b (secondes, depuis le début de la partie)."""
    return any(p0 < b and p1 > a for p0, p1 in cx.get("paroles", ()))


def _pat(cx, nom, liste, rng):
    """Motif tiré dans le vocabulaire de la partie : deux motifs propres à chaque partie, parfois un autre."""
    if nom not in cx:
        cx[nom] = [int(i) for i in rng.choice(len(liste), size=min(2, len(liste)), replace=False)]
    if rng.random() < 0.15:
        return liste[int(rng.integers(len(liste)))]
    return liste[cx[nom][int(rng.integers(len(cx[nom])))]]


def _texture(couches, S, texture, rng):
    """Partie dépouillée : une couche de moins ; partie pleine : une couche en plus (jamais le cœur du style)."""
    c = set(couches)
    if texture == "depouillee" and len(c) > 2:
        retirables = sorted(x for x in c if x not in S.get("coeur", ()))
        if retirables:
            c.discard(retirables[int(rng.integers(len(retirables)))])
    elif texture == "pleine":
        ajouts = sorted(x for x in S.get("options", ()) if x not in c)
        if ajouts and rng.random() < 0.7:
            c.add(ajouts[int(rng.integers(len(ajouts)))])
    return c


def _autre(options, avant, rng):
    """Un choix différent de celui de la partie précédente (quand c'est possible)."""
    o = [x for x in options if x != avant] or list(options)
    return o[int(rng.integers(len(o)))]


def _partie(style, humeur, duree, rng, prec=None, paroles=()):
    """Une partie (scène) composée d'un bout à l'autre.

    Renvoie (signal ou (fond, gêne), contexte, choix) ; le signal porte sa queue de réverbération (+4 s). D'une partie à
    l'autre changent : tonalité (ton de la banque et transposition), tempo, texture (dépouillée, normale, pleine),
    instrument mélodique principal (lead), vocabulaire de motifs ; prec = les choix de la partie précédente, évités.
    """
    S = STYLES[style]
    prec = prec or {}
    if humeur in S.get("special", {}):
        return S["special"][humeur](duree, rng, prec, paroles)
    B = BANQUES[S.get("banque", style)]
    hu = humeur if humeur in B else "lumiere"
    H = B[hu]
    i_ton = int(rng.integers(len(H["tons"])))
    if len(H["tons"]) > 1 and prec.get("ton") == (hu, i_ton):
        i_ton = (i_ton + 1 + int(rng.integers(len(H["tons"]) - 1))) % len(H["tons"])
    mode, centre, grilles = H["tons"][i_ton]
    tp = _autre(S.get("transpos", (0,)), prec.get("transpo"), rng)
    centre += tp
    while centre > 46:
        centre -= 12
    while centre < 35:
        centre += 12
    bpm = H["bpm"] + rng.uniform(-1, 1) * S.get("dbpm", 1.5)
    beat = 60.0 / bpm
    texture = _autre(S.get("textures", TEXTURES), prec.get("texture"), rng)
    lead = _autre(S.get("leads", (None,)), prec.get("lead"), rng)
    choix = {"ton": (hu, i_ton), "transpo": tp, "texture": texture, "lead": lead}
    temps = S.get("temps", 4)
    mes = temps * beat
    nmes = int(np.ceil(duree / mes)) + 1
    ordre = rng.permutation(len(grilles))
    g_a, g_b, g_p = (grilles[ordre[i % len(ordre)]] for i in range(3))
    if len(grilles) < 3:   # grille du pont : celle de A commencée ailleurs
        g_p = g_a[2:] + g_a[:2]
    n = int((duree + 4.0) * SR)
    bus = {"sec": np.zeros(n), "loin": np.zeros(n), "echo": np.zeros(n), "pad": np.zeros(n), "gene": np.zeros(n),
           "pompe": [], "beat": beat}
    cx = {"beat": beat, "temps": temps, "hu": hu, "mode": mode, "centre": centre, "suivant": None, "lead": lead,
          "texture": texture, "paroles": list(paroles), "duree": duree}
    if "init" in S:
        S["init"](cx, rng)
    m0 = 0
    for typ, L in _forme(nmes, rng):
        grille = {"intro": g_a, "A": g_a, "B": g_b, "pont": g_p, "respiration": g_b if rng.random() < 0.5 else g_a}[typ]
        # le pont module parfois (quarte, ton, tierce) : une couleur nouvelle au milieu d'une partie longue
        mod = int(rng.choice([5, -2, 3, 2])) if typ == "pont" and rng.random() < S.get("modulation", 0.5) else 0
        cx["centre"] = centre + mod
        accs = [_accord(c, centre + mod) for c in grille]
        couches = _texture(S["couches"](typ, rng, hu), S, texture, rng)
        S["phrase"](cx, typ, rng)
        for j in range(L):
            t = (m0 + j) * mes
            if t >= duree - 0.3:
                break
            if L == 16 and j == 8:          # les phrases de 16 mesures changent d'instrumentation à mi-chemin
                couches = _texture(S["couches"](typ, rng, hu), S, texture, rng)
            k = (j // cx["hr"]) % len(accs)
            cx["suivant"] = accs[(k + 1) % len(accs)]
            S["mesure"](bus, cx, t, j, L, typ, accs[k], couches, rng)
        m0 += L
        if m0 * mes >= duree:
            break
    cx["centre"] = centre
    return S["mix"](bus, hu, int(rng.integers(1 << 30))), cx, choix


def _limite(x, plafond):
    """Limiteur doux (anticipation de 5 ms, relâchement de 250 ms) : aucune crête au-dessus du plafond."""
    pas = 120
    nb = -(-len(x) // pas)
    p = np.abs(np.pad(x, (0, nb * pas - len(x)))).reshape(nb, pas).max(axis=1)
    g = np.minimum(1.0, plafond / np.maximum(p, 1e-9))
    g = np.minimum(g, np.concatenate([g[1:], [1.0]]))
    k = pas / (0.25 * SR)
    v, lisse = 1.0, np.empty(nb)
    for i in range(nb):
        v = g[i] if g[i] < v else v + (g[i] - v) * k
        lisse[i] = v
    gain = np.interp(np.arange(len(x)), np.arange(nb) * pas + pas / 2, lisse)
    return np.clip(x * gain, -plafond, plafond)


def _compresse(x, ratio=2.5, seuil_db=5.0):
    """Compresseur doux sur l'enveloppe (blocs de 5 ms, attaque 10 ms, relâchement 300 ms) : au-delà de seuil_db
    au-dessus du niveau médian, les coups (timbales, caisses, attaques de piano) sont ramenés vers le corps du son ;
    le niveau moyen peut alors rejoindre celui de l'ancienne boucle sans que le limiteur ait à travailler."""
    pas = 120
    nb = len(x) // pas
    if nb < 10:
        return x
    env = np.sqrt((x[:nb * pas].reshape(nb, pas) ** 2).mean(axis=1)) + 1e-9
    ka, kr = pas / (0.010 * SR), pas / (0.300 * SR)
    lisse = np.empty(nb)
    v = env[0]
    for i, e in enumerate(env):
        v += (e - v) * (ka if e > v else kr)
        lisse[i] = v
    seuil = np.median(lisse[lisse > 1e-6]) * 10 ** (seuil_db / 20) if (lisse > 1e-6).any() else 1.0
    g = np.where(lisse > seuil, (lisse / seuil) ** (1 / ratio - 1), 1.0)
    return x * np.interp(np.arange(len(x)), np.arange(nb) * pas + pas / 2, g)


def _rms_median(x):
    fen = int(3 * SR)
    nb = len(x) // fen
    if nb < 1:
        return float(np.sqrt((x ** 2).mean())) if len(x) else 0.0
    r = np.sqrt((x[:nb * fen].reshape(nb, fen) ** 2).mean(axis=1))
    return float(np.median(r[r > 1e-5])) if (r > 1e-5).any() else 0.0


# transitions entre parties : délai (s) entre le début de la scène et l'entrée de la nouvelle partie, pendant le carton
DELAIS = {"fondu": 0.0, "coupure": 0.55, "roulement": 1.3, "montee": 1.6}


def piste(duree, humeurs, site, graine="", style=None, paroles=None):
    """Musique de toute une vidéo, composée partie par partie (une partie = une scène du script).

    humeurs : [(début en s, humeur)] ; graine : le code de la vidéo ; paroles : [(t0, t1)] où la voix parle (sert à
    retenir sous la voix les éléments qui la gênent, comme la caisse claire de hggsp2, et à placer les roulements dans
    les silences). Chaque partie a sa graine (code + numéro de scène) et ses choix (voir _partie). Au changement de
    partie : petite transition propre au style (coupure, roulement, montée) dans le silence du carton, ou fondu.
    Chaque partie est ramenée au niveau de son humeur, l'ensemble à celui de l'ancienne boucle ; crête ≤ CRETE.
    style : une entrée de STYLES (par défaut STYLE[site]).
    """
    style = style or STYLE.get(site, "philo1")
    S = STYLES[style]
    n = int(round(duree * SR))
    out = np.zeros(n + 6 * SR)
    gene = np.zeros(n + 6 * SR)
    hs = sorted(humeurs) or [(0.0, "lumiere")]
    paroles = sorted(paroles or [])
    sortes = ["fondu"] + [str(_autre(S.get("transitions", ("fondu",)), None, _rng(graine, site, k, "transition")))
                          for k in range(1, len(hs))]
    prec = {}
    for k, (deb, hu) in enumerate(hs):
        fin = hs[k + 1][0] if k + 1 < len(hs) else duree
        if fin <= deb:
            continue
        sorte = sortes[k]
        depart = deb + DELAIS[sorte]
        if fin - depart < 2.0:
            sorte, depart = "fondu", deb
        rel = [(a - depart, b - depart) for a, b in paroles if b > depart and a < fin]
        rng = _rng(graine, site, k, hu)
        x, cx, prec = _partie(style, hu, fin - depart, rng, prec, rel)
        fond, gn = x if isinstance(x, tuple) else (x, None)
        L = fin - depart
        corps = fond[:int(L * SR)] + (gn[:int(L * SR)] if gn is not None else 0)
        g = S.get("niveaux", {}).get(hu, RMS_CIBLE) / max(_rms_median(corps), 1e-6)
        suivante = sortes[k + 1] if k + 1 < len(sortes) else "fondu"
        tt = np.arange(len(fond)) / SR
        if suivante == "coupure":   # coupure nette (0,3 s, sans clic) au début de la scène suivante
            w = np.clip((L + 0.05 - tt) / 0.3, 0, 1) ** 2
        else:                       # la résonance s'éteint sous la partie suivante
            w = np.clip((L + 2.5 - tt) / 2.5, 0, 1) ** 2
        _ajoute(out, fond * w * g, int(depart * SR))
        if gn is not None:
            _ajoute(gene, gn * w * g, int(depart * SR))
        if sorte != "fondu" and "transition" in S:
            tr = S["transition"](sorte, cx, _rng(graine, site, k, "son"), DELAIS[sorte])
            _ajoute(out, tr * g, int(deb * SR))
    out, gene = out[:n], gene[:n]
    if gene.any():
        # sous la voix, ce qui la gêne (caisse claire militaire) est fortement retenu et assombri ; intact dans les silences
        libre = enveloppe(n / SR, paroles, haut=1.0, bas=0.0, attaque=0.2, relache=0.8)
        libre = np.pad(libre, (0, max(0, n - len(libre))), constant_values=1.0)[:n]
        out += gene * libre + _filtre_id(gene, "lowpass", 700) * 0.3 * (1 - libre)
    if S.get("traitement", True):
        out = _filtre_id(out, "highpass", 45)       # pas de grondement sous la voix
        out = _creux(out, 2600, S.get("creux", -3.0), 0.7)       # place pour la voix entre 1 et 4 kHz
        out = _compresse(out)
    ref = _rms_median(out) or 1.0
    # niveau de l'ancienne boucle, sans que le limiteur ait à écraser plus que de rares crêtes (1 dB au plus)
    out *= min(RMS_CIBLE / ref, 1.2 * RMS_CIBLE / max(np.sqrt((out ** 2).mean()), 1e-9),
               CRETE * 1.12 / max(np.percentile(np.abs(out), 99.95), 1e-9))
    out = _limite(out, CRETE)
    k = min(len(out), int(0.05 * SR))
    out[:k] *= np.linspace(0, 1, k)
    out[-k:] *= np.linspace(1, 0, k)
    return out


# =====================================================================================================================
# Deuxième et troisième propositions par matière (10/11/2026 : le pilote choisira à l'écoute)
#   maths2 : harpe en arpèges, pizzicati, cordes aiguës aériennes, célesta ; mesure à 3 temps, 72-92 ; lydien, ionien
#   maths3 : synthé « pluck » en doubles croches avec écho et filtre qui s'ouvre, nappe, basse douce, pulsation
#            légère ; 92-106 ; éolien, dorien, phrygien
#   ses2   : funk feutré : basse synthétique syncopée, guitare étouffée en doubles croches, caisse sèche, charleston,
#            piano électrique en appoint ; 94-104 ; dorien, mixolydien, accords de neuvième
#   ses3   : électro douce : grosse caisse sur chaque temps, charleston ouvert à contretemps, nappes qui « respirent »
#            (sidechain), accords pincés en écho, clochettes FM ; 104-118 ; ionien, lydien
#   hggsp2 : caisses claires militaires lointaines (roulements), toms, ostinato de cordes en doubles croches sur pédale
#            de tonique, cuivres graves ; 72-84 ; phrygien, éolien
#   hggsp3 : piano grave en octaves, mélodie rare (parfois une note répétée), nappes sombres, violoncelle, souffle
#            documentaire ; 54-64 ; éolien, dorien, phrygien
# =====================================================================================================================
def _harpe(f, amp):
    """Corde pincée de harpe : harmoniques qui s'éteignent d'autant plus vite qu'elles sont aiguës, longue tenue."""
    n = int(2.8 * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 10):
        if k * f > 9000:
            break
        s += abs(np.sin(k * np.pi * 0.28)) / k * np.exp(-t * (0.9 + 0.9 * k) * (f / 330) ** 0.3) * np.sin(2 * np.pi * k * f * t + k)
    return _bords(amp * s * (1 - np.exp(-t / 0.0012)))


def _celesta(f, amp):
    n = int(1.8 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) * np.exp(-t * 2.2)
    if 4 * f < 10000:
        s += 0.25 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t * 9)
    return _bords(amp * s * (1 - np.exp(-t / 0.001)))


def _pluck(f, dur, amp, clair, rng):
    """Synthé « pluck » doux : scie filtrée dont la brillance retombe vite."""
    n = int((dur + 0.5) * SR)
    t = np.arange(n) / SR
    s = _scie(f, n, 0, rng, vib=0)
    a, b = _filtre_id(s, "lowpass", 380), _filtre_id(s, "lowpass", clair)
    y = a + (b - a) * np.exp(-t * 14)
    y *= (1 - np.exp(-t / 0.002)) * np.exp(-t * 3) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.08))
    return _bords(amp * y)


def _cloche_fm(f, amp):
    n = int(2.4 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t + 1.8 * np.exp(-t * 3) * np.sin(2 * np.pi * 3.5 * f * t))
    return _bords(amp * s * np.exp(-t * 1.7) * (1 - np.exp(-t / 0.002)))


def _sub(f, dur, amp):
    n = int((dur + 0.2) * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t)
    s *= (1 - np.exp(-t / 0.01)) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.07))
    return _bords(amp * s)


def _guitare_etouffee(f, amp, long=0.12):
    """Corde de guitare étouffée par la paume (« chicka » funk) : attaque nette, extinction rapide."""
    n = int((long + 0.08) * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 9):
        if k * f > 8000:
            break
        s += abs(np.sin(k * np.pi * 0.18)) / k * np.exp(-t * (18 + 6 * k)) * np.sin(2 * np.pi * k * f * t + 0.7 * k)
    return _bords(amp * s * (1 - np.exp(-t / 0.0015)))


def _basse_funk(f, dur, amp, rng):
    n = int((dur + 0.12) * SR)
    t = np.arange(n) / SR
    s = 0.7 * np.sin(2 * np.pi * f * t) + 0.5 * _filtre_id(_scie(f, n, 0, rng, vib=0), "lowpass", 900) * np.exp(-t * 6)
    s *= (1 - np.exp(-t / 0.003)) * np.exp(-t * 2.5) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.03))
    return _bords(amp * s)


def _caisse_id(amp, rng, corps=200, timbre=(1500, 8000), decl=18, timbre_decl=None):
    """Caisse claire (sèche en funk, militaire avec son timbre qui grésille plus longtemps)."""
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    s = _filtre_id(rng.standard_normal(n), "bandpass", list(timbre)) * np.exp(-t * (timbre_decl or decl))
    s += 0.6 * np.sin(2 * np.pi * corps * t) * np.exp(-t * 30)
    return _bords(amp * s * (1 - np.exp(-t / 0.0008)))


def _tom(f, amp):
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(f * (1 + 0.35 * np.exp(-t / 0.05))) / SR
    return _bords(amp * np.sin(ph) * np.exp(-t * 5) * (1 - np.exp(-t / 0.002)))


def _vent(dur, amp, rng):
    """Texture documentaire : souffle grave filtré qui gonfle puis retombe."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = _filtre_id(rng.standard_normal(n), "bandpass", [180, 900])
    return _bords(amp * s * np.sin(np.pi * t / dur) ** 2)


def _echo(x, delai, retour, mix, n=4):
    y = np.zeros_like(x)
    d = int(delai * SR)
    for k in range(1, n + 1):
        if k * d < len(x):
            y[k * d:] += x[:len(x) - k * d] * retour ** (k - 1)
    return x + mix * _filtre_id(y, "lowpass", 3500)


def _vel(rng, sd=0.08):
    return 1 + rng.normal(0, sd)


# ------------------------------------------------------------------ maths 2 : cordes pincées et harpe, mesure à 3 temps
BANQUES["maths2"] = {
    "lumiere": dict(bpm=84, tons=[
        ("lydien", 41, [["0:maj9", "2:add9/0", "9:m7", "7:sus2"], ["0:add9", "4:m7", "2:add9", "0:maj7"],
                        ["7:sus2", "2:M", "4:m7", "0:maj9"]]),
        ("ionien", 43, [["0:add9", "7:sus2", "9:m7", "5:maj9"], ["5:maj7", "0:add9", "2:m7", "7:sus4"],
                        ["9:m7", "5:maj9", "0:add9", "7:sus2"]])]),
    "mystere": dict(bpm=76, tons=[
        ("dorien", 38, [["0:m9", "5:add9", "0:m9", "3:maj7"], ["0:m11", "10:maj7", "5:sus2", "0:m9"],
                        ["3:maj7", "10:add9", "0:m9", "0:m9"]]),
        ("eolien", 45, [["0:madd9", "8:maj7", "5:m7", "10:sus2"], ["8:maj9", "3:add9", "10:sus2", "0:madd9"]])]),
    "tension": dict(bpm=92, tons=[
        ("eolien", 40, [["0:m", "8:maj7", "3:M", "10:sus4"], ["0:madd9", "5:m7", "8:maj9", "7:m7"],
                        ["0:m", "10:M", "8:maj7", "8:maj7"]]),
        ("dorien", 45, [["0:m7", "5:add9", "0:m7", "10:maj7"], ["7:m7", "5:add9", "3:maj7", "0:m9"]])]),
    "calme": dict(bpm=72, tons=[
        ("lydien", 36, [["0:maj9", "2:add9/0", "0:maj7", "7:sus2"], ["9:m7", "4:m7", "2:add9", "0:maj9"]]),
        ("ionien", 41, [["0:add9", "5:maj7", "9:m7", "7:sus4"], ["5:maj9", "4:m7", "2:m7", "0:add9"]])]),
}
ARP_HARPE = [[0, 2, 4, 5, 4, 2], [0, 2, 3, 4, 5, 6], [1, 3, 5, 6, 5, 3], [0, None, 3, 4, None, 6], [0, 4, 2, 5, 3, 6],
             [6, 5, 4, 3, 2, 1]]


def _couches_maths2(typ, rng, hu):
    if typ == "intro":
        return [{"harpe"}, {"harpe", "aigu"}][rng.integers(2)]
    if typ == "respiration":
        return [{"harpe"}, {"aigu", "celesta"}, {"harpe", "aigu"}][rng.integers(3)]
    if typ == "pont":
        return [{"pizz", "aigu", "celesta"}, {"harpe", "pizz"}][rng.integers(2)]
    c = {"harpe", "pizz"}
    if rng.random() < 0.55:
        c.add("aigu")
    if typ == "B" and rng.random() < 0.7:
        c.add("melodie")
    if rng.random() < 0.35:
        c.add("celesta")
    return c


def _phrase_maths2(cx, typ, rng):
    cx["hr"] = 2 if cx["hu"] in ("mystere", "calme") or rng.random() < 0.6 else 1
    cx["arp"] = ARP_HARPE[rng.integers(len(ARP_HARPE))]
    cx.setdefault("mel", 72)


def _mesure_maths2(bus, cx, t, j, L, typ, acc, couches, rng):
    beat, T = cx["beat"], cx["temps"]
    mes = T * beat
    jeu = lambda: rng.normal(0, 0.006)                  # noqa: E731
    v = _voix(acc, 62)
    tons = sorted({p + 12 * o for p in v for o in (-1, 0, 1) if 55 <= p + 12 * o <= 84})
    if "harpe" in couches:
        arp = cx["arp"] if j % 4 != 3 else ARP_HARPE[rng.integers(len(ARP_HARPE))]
        for c, i in enumerate(arp):
            if i is not None:
                _place(bus["sec"], _harpe(hz(tons[min(i, len(tons) - 1)]), 0.05 * _vel(rng) * (1.15 if c == 0 else 1)), t + c * beat / 2 + jeu())
    if "pizz" in couches and (j % cx["hr"] == 0 or rng.random() < 0.5):
        _place(bus["sec"], _pizz_id(hz(acc["basse"] + 12), 0.10 * _vel(rng)), t + jeu())
        if rng.random() < 0.4:
            _place(bus["sec"], _pizz_id(hz(acc["basse"] + 19), 0.06 * _vel(rng)), t + 2 * beat + jeu())
    if "aigu" in couches and j % cx["hr"] == 0:
        for p in _voix(acc, 74)[:3]:
            _place(bus["sec"], _cordes(hz(p), cx["hr"] * mes + 0.3, 0.012 * _vel(rng), 2400, rng, attaque=1.6, voix=2), t)
    if "celesta" in couches:
        hauts = [q + 12 for q in tons if 72 <= q + 12 <= 91]
        for c in sorted(rng.choice(2 * T, size=int(rng.integers(1, 3)), replace=False)):
            _place(bus["sec"], _celesta(hz(int(rng.choice(hauts))), 0.022 * _vel(rng)), t + c * beat / 2 + jeu())
    if "melodie" in couches:
        ga = _gamme(cx["mode"], cx["centre"], 67, 86)
        acc_pc = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
        p = min((q for q in ga if q % 12 in acc_pc), key=lambda q: abs(q - cx["mel"]))
        _place(bus["sec"], _harpe(hz(p), 0.07 * _vel(rng)), t + jeu())
        if rng.random() < 0.6:
            i = int(np.clip(ga.index(p) + rng.choice([-2, -1, 1, 2]), 0, len(ga) - 1))
            _place(bus["sec"], _harpe(hz(ga[i]), 0.055 * _vel(rng)), t + 2 * beat + jeu())
            p = ga[i]
        cx["mel"] = p


def _mix_maths2(bus, hu, graine):
    return _salle(bus["sec"], 2.4, 0.34, 5000, graine)


# ---------------------------------------------- maths 3 : synthé doux, arpèges électroniques en doubles croches (« focus »)
BANQUES["maths3"] = {
    "lumiere": dict(bpm=100, tons=[
        ("eolien", 45, [["0:m9", "8:maj7", "3:add9", "10:sus2"], ["8:maj9", "10:sus2", "0:m7", "0:m7"],
                        ["5:m9", "3:maj7", "10:add9", "0:m9"]]),
        ("dorien", 38, [["0:m9", "5:add9", "10:maj7", "3:maj7"], ["0:m11", "7:m7", "3:maj9", "5:sus2"]])]),
    "mystere": dict(bpm=94, tons=[
        ("phrygien", 40, [["0:m7", "1:maj7", "0:m7", "10:m7"], ["0:sus2", "8:maj7", "1:maj7", "0:m"]]),
        ("eolien", 43, [["0:m9", "0:m9", "8:maj9", "8:maj9"], ["3:maj7", "10:sus2", "8:maj7", "0:m9"]])]),
    "tension": dict(bpm=106, tons=[
        ("eolien", 40, [["0:m", "8:M", "10:M", "7:m"], ["0:m7", "3:M", "10:sus4", "8:maj7"]]),
        ("dorien", 45, [["0:m7", "5:M", "0:m7", "7:m7"], ["3:maj7", "5:sus2", "0:m9", "10:M"]])]),
    "calme": dict(bpm=92, tons=[
        ("ionien", 36, [["0:maj9", "9:m9", "5:maj9", "7:sus2"], ["5:maj7", "7:sus2", "4:m7", "9:m7"]]),
        ("lydien", 41, [["0:maj9", "2:add9/0", "7:sus2", "4:m7"]])]),
}
ARP_SYNTH = [[0, 1, 2, 3, 4, 3, 2, 1], [0, 2, 1, 3, 2, 4, 3, 5], [0, 4, 1, 3, 2, 4, 1, 3], [0, 1, 2, 3, 0, 1, 2, 4],
             [4, 3, 2, 1, 0, 1, 2, 3], [0, 2, 4, 2, 1, 3, 5, 3]]


def _couches_maths3(typ, rng, hu):
    if typ == "intro":
        return [{"nappe"}, {"arp", "nappe"}][rng.integers(2)]
    if typ == "respiration":
        return [{"nappe"}, {"nappe", "cloche"}, {"arp"}][rng.integers(3)]
    if typ == "pont":
        return [{"nappe", "sub", "pouls"}, {"arp", "sub"}][rng.integers(2)]
    c = {"arp", "nappe", "sub"}
    if typ == "B" or rng.random() < 0.4:
        c.add("pouls")
    if rng.random() < 0.35:
        c.add("cloche")
    if typ == "B" and rng.random() < 0.3:
        c.discard("nappe")
    return c


# ------------------------------------------------------------------- SES 2 : funk feutré (basse, guitare étouffée)
BANQUES["ses2"] = {
    "lumiere": dict(bpm=100, tons=[
        ("dorien", 40, [["0:m7", "5:9", "0:m7", "5:9"], ["0:m9", "3:maj7", "5:9", "7:m7"]]),
        ("mixolydien", 43, [["0:9", "5:add9", "0:9", "10:maj7"], ["0:9", "0:9", "5:9sus4", "7:m7"]])]),
    "mystere": dict(bpm=96, tons=[
        ("dorien", 45, [["0:m9", "0:m9", "5:9", "5:9"], ["0:m7", "3:maj7", "2:m7", "5:9"]]),
        ("phrygien", 40, [["0:m7", "1:maj7", "0:m7", "10:m7"]])]),
    "tension": dict(bpm=104, tons=[
        ("dorien", 38, [["0:m7", "0:m7", "5:7", "3:maj7"], ["0:m9", "10:9sus4", "5:7", "0:m7"]]),
        ("eolien", 40, [["0:m7", "8:maj7", "10:7sus4", "0:m7"]])]),
    "calme": dict(bpm=94, tons=[
        ("mixolydien", 41, [["0:9", "10:maj7", "5:add9", "0:9sus4"], ["7:m7", "5:add9", "0:9", "0:9"]]),
        ("ionien", 43, [["0:maj9", "2:m7", "4:m7", "5:maj7"]])]),
}
BASSE16 = [[(0, "R", 2), (3, "R", 1), (6, "8", 1), (7, "R", 1), (10, "5", 2), (12, "7", 1), (14, "8", 1)],
           [(0, "R", 3), (4, "R", 1), (6, "5", 1), (8, "8", 2), (11, "R", 1), (14, "a", 2)],
           [(0, "R", 1), (2, "R", 1), (3, "8", 1), (6, "R", 2), (9, "5", 1), (10, "7", 2), (13, "8", 1), (15, "a", 1)],
           [(0, "R", 4), (6, "5", 1), (7, "8", 1), (10, "R", 2), (14, "7", 2)]]
GUIT16 = [[2, 6, 10, 14], [2, 3, 6, 10, 11, 14], [0, 2, 6, 7, 10, 14, 15], [2, 5, 6, 10, 13, 14], [1, 2, 6, 9, 10, 14]]


def _couches_ses2(typ, rng, hu):
    if typ == "intro":
        return [{"guitare"}, {"guitare", "basse"}, {"charley", "basse"}][rng.integers(3)]
    if typ == "respiration":
        return [{"clavier"}, {"clavier", "basse"}, {"guitare", "charley"}][rng.integers(3)]
    if typ == "pont":
        return [{"basse", "batterie", "charley"}, {"clavier", "guitare", "basse"}][rng.integers(2)]
    c = {"batterie", "charley", "basse", "guitare"}
    if rng.random() < 0.35:
        c.add("clavier")
    if typ == "A" and rng.random() < 0.25:
        c.discard("guitare")
    return c


def _seize(c, beat, swing=0.53):
    return beat * (c // 4) + (beat / 2) * ((c % 4) // 2) + (beat / 2 * swing if c % 2 else 0.0)


def _mix_ses2(bus, hu, graine):
    x = _salle(bus["sec"], 0.7, 0.15, 5500, graine)
    x = _filtre_id(_filtre_id(x, "lowpass", 7000), "highpass", 50)
    return np.tanh(1.8 * x) / 1.8


# --------------------------------------------------------------- SES 3 : électro douce de magazine (pads qui respirent)
BANQUES["ses3"] = {
    "lumiere": dict(bpm=112, tons=[
        ("ionien", 41, [["0:maj9", "9:m7", "5:maj9", "7:add9"], ["5:maj7", "7:sus2", "9:m7", "4:m7"]]),
        ("lydien", 36, [["0:maj7", "2:add9/0", "9:m7", "7:sus2"], ["4:m7", "2:add9", "0:maj9", "7:sus4"]])]),
    "mystere": dict(bpm=106, tons=[
        ("dorien", 38, [["0:m9", "5:add9", "0:m9", "10:maj7"], ["3:maj7", "5:sus2", "0:m11", "7:m7"]]),
        ("eolien", 45, [["0:m9", "8:maj9", "3:add9", "10:sus2"]])]),
    "tension": dict(bpm=118, tons=[
        ("eolien", 40, [["0:m7", "8:maj7", "3:add9", "10:sus2"], ["5:m7", "0:m7", "8:maj9", "10:M"]]),
        ("dorien", 45, [["0:m7", "5:add9", "3:maj7", "7:m7"]])]),
    "calme": dict(bpm=104, tons=[
        ("ionien", 43, [["0:maj9", "4:m7", "5:maj9", "2:m9"], ["9:m7", "5:maj7", "0:add9", "7:sus4"]]),
        ("mixolydien", 41, [["0:add9", "10:add9", "5:maj9", "0:sus2"]])]),
}
STABS = [[3, 6], [2, 5, 7], [1, 3, 6], [3, 7], [0, 3, 5]]


def _couches_ses3(typ, rng, hu):
    if typ == "intro":
        return [{"nappe"}, {"nappe", "stabs"}][rng.integers(2)]
    if typ == "respiration":
        return [{"nappe"}, {"nappe", "cloche"}, {"stabs", "sub"}][rng.integers(3)]
    if typ == "pont":
        return [{"nappe", "charley", "sub"}, {"stabs", "cloche", "nappe"}][rng.integers(2)]
    c = {"kick", "charley", "nappe", "sub"}
    if rng.random() < 0.7:
        c.add("stabs")
    if typ == "B" and rng.random() < 0.6:
        c.add("cloche")
    if hu == "calme" and rng.random() < 0.5:
        c.discard("kick")
    return c


def _phrase_ses3(cx, typ, rng):
    cx["hr"] = 2 if rng.random() < 0.65 else 1
    cx["stabs"] = STABS[rng.integers(len(STABS))]
    cx.setdefault("mel", 76)


def _mesure_ses3(bus, cx, t, j, L, typ, acc, couches, rng):
    beat = cx["beat"]
    mes = 4 * beat
    v = _voix(acc, 62)
    if "kick" in couches:
        for b in range(4):
            _place(bus["sec"], _grosse_caisse_id(0.10 * _vel(rng, 0.05)), t + b * beat)
            bus["pompe"].append(t + b * beat)
    if "charley" in couches:
        for b in range(4):
            _place(bus["sec"], _charley_id(0.012 * _vel(rng), rng, ouvert=True), t + b * beat + beat / 2)
    if "nappe" in couches and j % cx["hr"] == 0:
        for p in v[:4]:
            _place(bus["pad"], _cordes(hz(p), cx["hr"] * mes + 0.3, 0.020 * _vel(rng), 1500, rng, attaque=1.2, voix=3), t)
    if "sub" in couches:
        for b in range(4):
            _place(bus["sec"], _sub(hz(acc["basse"] + 12 if acc["basse"] < 40 else acc["basse"]), beat * 0.4, 0.07 * _vel(rng)), t + b * beat + beat / 2)
    if "stabs" in couches:
        for c in cx["stabs"]:
            for k, p in enumerate(_voix(acc, 67)):
                _place(bus["echo"], _pluck(hz(p), beat * 0.3, 0.016 * _vel(rng), 2400, rng), t + c * beat / 2 + 0.003 * k)
    if "cloche" in couches and j % 2 == 0:
        ga = _gamme(cx["mode"], cx["centre"], 72, 88)
        acc_pc = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
        for c in sorted(rng.choice(8, size=int(rng.integers(2, 4)), replace=False)):
            i = int(np.clip(ga.index(min(ga, key=lambda q: abs(q - cx["mel"]))) + rng.choice([-2, -1, 1, 2]), 0, len(ga) - 1))
            p = ga[i]
            if c == 0:
                p = min((q for q in ga if q % 12 in acc_pc), key=lambda q: abs(q - p))
            _place(bus["echo"], _cloche_fm(hz(p), 0.028 * _vel(rng)), t + c * beat / 2)
            cx["mel"] = p


def _mix_ses3(bus, hu, graine):
    pad = bus["pad"]
    if bus["pompe"]:   # les nappes respirent au rythme de la grosse caisse (effet « sidechain »)
        tt = np.arange(len(pad)) / SR
        g = np.ones(len(pad))
        for tk in bus["pompe"]:
            i = int(tk * SR)
            L = min(len(pad) - i, int(0.45 * SR))
            if L > 0:
                g[i:i + L] = np.minimum(g[i:i + L], 1 - 0.55 * np.exp(-tt[:L] / 0.12) * np.minimum(1, tt[:L] / 0.004 + 0.6))
        pad = pad * g
    x = bus["sec"] + pad + _echo(bus["echo"], 0.75 * bus["beat"], 0.35, 0.4)
    x = _salle(x, 1.4, 0.22, 5500, graine)
    return _filtre_id(x, "highpass", 50)


# ------------------------------------------------- HGGSP 2 : tambours militaires lointains, ostinato en doubles croches
BANQUES["hggsp2"] = {
    "lumiere": dict(bpm=80, tons=[
        ("eolien", 45, [["0:m", "0:m", "8:M/0", "10:M/0"], ["0:m", "5:m", "8:M", "7:m"]]),
        ("eolien", 40, [["0:m", "8:M/0", "3:M/0", "10:M"], ["0:5", "8:M", "10:M", "0:m"]])]),
    "mystere": dict(bpm=74, tons=[
        ("phrygien", 40, [["0:m", "1:M/0", "0:m", "10:m/0"], ["0:5", "1:maj7/0", "0:sus4", "0:m"]]),
        ("phrygien", 45, [["0:m", "1:M/0", "3:M/0", "1:M/0"]])]),
    "tension": dict(bpm=84, tons=[
        ("phrygien", 38, [["0:m", "1:M/0", "0:m", "1:M/0"], ["0:m", "10:m/0", "8:M/0", "1:M/0"]]),
        ("eolien", 40, [["0:m", "0:m", "8:M", "7:m"], ["0:5", "10:M/0", "8:M/0", "7:m/0"]])]),
    "calme": dict(bpm=72, tons=[
        ("eolien", 43, [["0:m", "8:M/0", "5:m/0", "0:m"], ["3:M", "10:M", "0:m", "0:m"]]),
        ("dorien", 38, [["0:m", "5:M/0", "0:m", "3:M/0"]])]),
}
MILITAIRE = [[(0, 1.0), (3, 0.5), (4, 0.7), (6, 0.5), (8, 1.0), (11, 0.5), (12, 0.7), (14, 0.5), (15, 0.5)],
             [(0, 1.0), (2, 0.5), (3, 0.5), (4, 0.8), (8, 1.0), (10, 0.5), (11, 0.5), (12, 0.8)],
             [(0, 1.0), (4, 0.6), (6, 0.5), (7, 0.5), (8, 1.0), (12, 0.6), (14, 0.5), (15, 0.6)]]
OST16 = [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1],
         [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 2, 1]]


def _couches_hggsp2(typ, rng, hu):
    if typ == "intro":
        return [{"pedale", "caisse"}, {"pedale", "ostinato"}][rng.integers(2)]
    if typ == "respiration":
        return [{"pedale"}, {"pedale", "caisse"}][rng.integers(2)]
    if typ == "pont":
        return [{"ostinato", "toms"}, {"pedale", "caisse", "toms"}][rng.integers(2)]
    c = {"pedale", "ostinato", "caisse"}
    if typ == "B" or rng.random() < 0.4:
        c.add("toms")
    if rng.random() < (0.7 if typ == "B" else 0.35):
        c.add("cuivres")
    if hu == "calme" and rng.random() < 0.5:
        c.discard("ostinato")
    return c


# ----------------------------------------------- HGGSP 3 : piano grave et nappes documentaires (sobre, lent)
BANQUES["hggsp3"] = {
    "lumiere": dict(bpm=60, tons=[
        ("eolien", 45, [["0:madd9", "8:maj7", "3:add9", "10:sus2"], ["5:m7", "8:maj7", "10:sus4", "0:m"]]),
        ("dorien", 38, [["0:m9", "5:add9", "3:maj7", "0:m"]])]),
    "mystere": dict(bpm=56, tons=[
        ("phrygien", 40, [["0:m", "1:maj7", "0:m", "8:maj7"], ["0:sus4", "10:m", "1:M", "0:m"]]),
        ("eolien", 43, [["0:m", "8:maj7", "0:m", "3:M"]])]),
    "tension": dict(bpm=64, tons=[
        ("eolien", 38, [["0:m", "10:M", "8:M", "7:m"], ["0:m", "5:m", "8:maj7", "7:m"]]),
        ("phrygien", 45, [["0:m", "1:M", "0:m", "10:m"]])]),
    "calme": dict(bpm=54, tons=[
        ("eolien", 41, [["0:madd9", "8:maj7", "5:m7", "3:add9"], ["10:sus2", "8:maj7", "0:m", "0:m"]]),
        ("dorien", 43, [["0:m9", "5:add9", "0:m9", "10:maj7"]])]),
}


def _couches_hggsp3(typ, rng, hu):
    if typ == "intro":
        return [{"piano_grave", "nappe"}, {"nappe"}][rng.integers(2)]
    if typ == "respiration":
        return [{"nappe"}, {"nappe", "vent"}, {"piano_grave"}][rng.integers(3)]
    if typ == "pont":
        return [{"nappe", "violoncelle", "vent"}, {"piano_grave", "melodie"}][rng.integers(2)]
    c = {"piano_grave", "nappe"}
    if rng.random() < (0.75 if typ == "B" else 0.45):
        c.add("melodie")
    if rng.random() < 0.35:
        c.add("violoncelle")
    if rng.random() < 0.25:
        c.add("vent")
    return c


def _phrase_hggsp3(cx, typ, rng):
    cx["hr"] = 2 if rng.random() < 0.75 else 1
    cx.setdefault("mel", 64)
    cx["note_rep"] = rng.random() < 0.4        # motif de note répétée (le temps qui passe)


def _init_hggsp3(cx, rng):
    cx["boom"] = True


def _mesure_hggsp3(bus, cx, t, j, L, typ, acc, couches, rng):
    beat = cx["beat"]
    mes = 4 * beat
    if cx.pop("boom", False):     # un seul coup sourd et lointain au début de la partie
        _place(bus["loin"], _timbale_id(hz(cx["centre"] + (12 if cx["centre"] < 41 else 0)), 0.06, rng), t)
    if "piano_grave" in couches and j % cx["hr"] == 0:
        b = acc["basse"] + (12 if acc["basse"] < 41 else 0)      # grave, mais pas de grondement sous la voix
        _place(bus["sec"], _piano_feutre_id(hz(b), cx["hr"] * mes * 0.95, 0.06 * _vel(rng), 0.4), t)
        _place(bus["sec"], _piano_feutre_id(hz(b + 12), cx["hr"] * mes * 0.95, 0.045 * _vel(rng), 0.35), t + 0.015)
        for k, p in enumerate(_voix(acc, 55)[:3]):
            _place(bus["sec"], _piano_feutre_id(hz(p), cx["hr"] * mes * 0.9, 0.022 * _vel(rng), 0.4), t + 2 * beat * (cx["hr"] == 2) + 0.02 * k)
    if "nappe" in couches and j % cx["hr"] == 0:
        for p in _voix(acc, 57)[:3]:
            _place(bus["sec"], _cordes(hz(p), cx["hr"] * mes + 0.5, 0.016 * _vel(rng), 750, rng, attaque=2.4, voix=2), t)
    if "melodie" in couches:
        ga = _gamme(cx["mode"], cx["centre"], 57, 74)
        acc_pc = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
        p = min((q for q in ga if q % 12 in acc_pc), key=lambda q: abs(q - cx["mel"]))
        if cx["note_rep"]:
            for c in (0, 1.5, 3):
                _place(bus["sec"], _piano_feutre_id(hz(p + 12), beat, 0.030 * _vel(rng), 0.45), t + c * beat)
        else:
            _place(bus["sec"], _piano_feutre_id(hz(p + 12), 2 * beat, 0.034 * _vel(rng), 0.45), t + rng.normal(0, 0.01))
            if rng.random() < 0.6:
                i = int(np.clip(ga.index(p) + rng.choice([-2, -1, 1]), 0, len(ga) - 1))
                _place(bus["sec"], _piano_feutre_id(hz(ga[i] + 12), 2 * beat, 0.028 * _vel(rng), 0.45), t + 2 * beat + rng.normal(0, 0.01))
                p = ga[i]
        cx["mel"] = p
    if "violoncelle" in couches and j % 2 == 0:
        _place(bus["sec"], _cordes(hz(acc["basse"] + 12), 2 * mes - 0.2, 0.028 * _vel(rng), 1100, rng, attaque=0.9, voix=2), t)
    if "vent" in couches and j % 4 == 0:
        _place(bus["sec"], _vent(4 * mes, 0.035, rng), t)


def _mix_hggsp3(bus, hu, graine):
    x = _salle(bus["sec"], 2.8, 0.32, 3200, graine)
    return x + _salle(_filtre_id(bus["loin"], "lowpass", 900), 4.0, 1.0, 1500, graine + 1, predelai=0.08, sec=False)


# ---------------------------------------------- propositions retenues (maths3, ses2, hggsp2) : variantes par partie
def _montee(dur, amp, rng):
    """Montée : souffle dont la couleur glisse du grave vers l'aigu, en crescendo."""
    n = max(2, int(dur * SR))
    t = np.arange(n) / n
    bruit = rng.standard_normal(n)
    s = np.zeros(n)
    for i, b in enumerate(((300, 700), (700, 1500), (1500, 3000), (3000, 6000))):
        s += _filtre_id(bruit, "bandpass", list(b)) * np.clip(1 - np.abs(3 * t - i), 0, 1)
    return _bords(amp * s * t ** 2)


def _sig_transition(delai, extra=2.5):
    return np.zeros(int((delai + extra) * SR))


def _orgue(f, dur, amp):
    """Orgue à tirettes (sinus 16', 8', 5 1/3', 4') : petites attaques sèches pour le funk."""
    n = int((dur + 0.05) * SR)
    t = np.arange(n) / SR
    s = sum(a * np.sin(2 * np.pi * k * f * t) for k, a in ((1, 0.6), (2, 0.8), (3, 0.3), (4, 0.25)) if k * f < 9000)
    s *= (1 - np.exp(-t / 0.004)) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.02))
    return _bords(amp * s)


# --- maths 3
def _phrase_maths3(cx, typ, rng):
    cx["hr"] = 2 if rng.random() < 0.6 else 1
    cx["arp"] = _pat(cx, "v_arp", ARP_SYNTH, rng)
    cx["ouvre"] = rng.random() < 0.6           # le filtre de l'arpège s'ouvre au fil de la phrase (sinon se referme)
    cx["octave"] = 12 if rng.random() < 0.25 else 0


def _note_maths3(lead, f, dur, a, clair, rng):
    if lead == "verre":
        return _celesta(f, a * 0.6)
    if lead == "fm":   # cloche FM douce (rapport 2, indice faible) : ronde, sans partiels criards dans la bande de la voix
        n = int(1.2 * SR)
        t = np.arange(n) / SR
        x = np.sin(2 * np.pi * f * t + (0.9 * np.exp(-t * 5) + 0.15) * np.sin(4 * np.pi * f * t))
        return _bords(a * 0.9 * x * np.exp(-t * 2.5) * (1 - np.exp(-t / 0.002)))
    if lead == "doux":
        return _pluck(f, dur, a * 1.15, 900, rng)
    return _pluck(f, dur, a, clair, rng)


def _mesure_maths3(bus, cx, t, j, L, typ, acc, couches, rng):
    beat = cx["beat"]
    mes = 4 * beat
    v = _voix(acc, 64)
    tons = sorted({p + 12 * o for p in v for o in (0, 1) if 60 <= p + 12 * o <= 84})
    lead = cx["lead"]
    if "arp" in couches:
        x = j / max(1, L - 1)
        clair = 700 + 1400 * (x if cx["ouvre"] else 1 - x)
        croches = lead in ("verre", "fm") or typ == "respiration"   # timbres qui sonnent : arpège en croches
        for c in range(16):
            if croches and c % 2:
                continue
            i = cx["arp"][c % 8]
            a = 0.034 * _vel(rng, 0.06) * (1.2 if c % 4 == 0 else 1)
            p = tons[i % len(tons)] + (cx["octave"] if tons[i % len(tons)] + cx["octave"] <= 88 else 0)
            if croches and p > 74:      # célesta et cloche : une octave plus bas, hors de la bande de la voix
                p -= 12 * (1 + (p > 86))
            _place(bus["echo"], _note_maths3(lead, hz(p), beat / 4 * 0.9, a, clair, rng), t + c * beat / 4)
    if "nappe" in couches and j % cx["hr"] == 0:
        for p in v[:4]:
            _place(bus["sec"], _cordes(hz(p), cx["hr"] * mes + 0.4, 0.014 * _vel(rng), 900, rng, attaque=2.0, voix=2), t)
    if "sub" in couches:
        for b in ((0, 2) if cx["hu"] != "calme" else (0,)):
            _place(bus["sec"], _sub(hz(acc["basse"] + (12 if acc["basse"] < 41 else 0)), 1.8 * beat, 0.08 * _vel(rng)), t + b * beat)
    if "pouls" in couches:
        for b in cx["v_kick"]:
            _place(bus["sec"], _grosse_caisse_id(0.07 * _vel(rng)), t + b * beat)
        for c in range(16):
            if c % 2 or rng.random() < 0.5:
                _place(bus["sec"], _charley_id(0.007 * (1.4 if c % 4 == 2 else 1), rng), t + c * beat / 4)
    if "cloche" in couches and rng.random() < 0.6:
        hauts = [q + 12 for q in tons if q + 12 <= 84] or tons
        _place(bus["sec"], _cloche_fm(hz(int(rng.choice(hauts))), 0.016 * _vel(rng)), t + int(rng.integers(4)) * beat)


def _init_maths3(cx, rng):
    cx["v_kick"] = [(0, 2), (0, 2.5), (0, 1.5, 2), (0,)][int(rng.integers(4))]


def _mix_maths3(bus, hu, graine):
    return _salle(bus["sec"] + _echo(bus["echo"], 0.75 * bus["beat"], 0.4, 0.45), 1.6, 0.25, 4500, graine)


def _transition_maths3(sorte, cx, rng, delai):
    s = _sig_transition(delai)
    beat, c = cx["beat"], cx["centre"]
    if sorte == "roulement":
        nb = int(delai / (beat / 4))
        for k in range(nb):
            _place(s, _charley_id(0.004 + 0.014 * k / max(1, nb), rng), delai - (nb - k) * beat / 4)
    elif sorte == "montee":
        _place(s, _montee(delai, 0.035, rng), 0)
    _place(s, _grosse_caisse_id(0.08), delai)
    _place(s, _sub(hz(c + (12 if c < 41 else 0)), 1.5 * beat, 0.07), delai)
    _place(s, _cloche_fm(hz(c + 24 + (12 if c < 41 else 0)), 0.016), delai)
    return _salle(s, 1.6, 0.25, 4500, 5)


# --- SES 2
def _phrase_ses2(cx, typ, rng):
    cx["hr"] = 2 if rng.random() < 0.6 else 1
    cx["basse16"] = _pat(cx, "v_basse", BASSE16, rng)
    cx["guit16"] = _pat(cx, "v_guit", GUIT16, rng)
    cx["gc"] = _pat(cx, "v_gc", GC16, rng)


GC16 = [[0, 7, 10], [0, 3, 10], [0, 6, 8, 11], [0, 10, 13], [0, 8], [0, 3, 6, 10]]


def _mesure_ses2(bus, cx, t, j, L, typ, acc, couches, rng):
    beat = cx["beat"]
    fin_phrase = j == L - 1
    jeu = lambda: rng.normal(0, 0.005)                  # noqa: E731
    if "batterie" in couches:
        gc = cx["gc"] if j % 4 != 3 else GC16[int(rng.integers(len(GC16)))]
        for c in gc:
            _place(bus["sec"], _grosse_caisse_id(0.11 * _vel(rng)), t + _seize(c, beat) + jeu())
        for c in (4, 12):
            _place(bus["sec"], _caisse_id(0.06 * _vel(rng), rng), t + _seize(c, beat) + jeu())
        for c in ((7, 9, 15) if fin_phrase else (7, 15)):
            if rng.random() < 0.5 or fin_phrase:
                _place(bus["sec"], _caisse_id(0.014 * _vel(rng), rng), t + _seize(c, beat) + jeu())
    if "charley" in couches:
        for c in range(16):
            if cx["hats8"] and c % 2:
                continue
            a = (0.016 if c % 4 == 0 else 0.011 if c % 2 == 0 else 0.007) * _vel(rng)
            _place(bus["sec"], _charley_id(a, rng, ouvert=fin_phrase and c == 14), t + _seize(c, beat) + jeu())
    if "basse" in couches:
        r, suiv = acc["basse"], cx["suivant"]["basse"]
        for c, deg, d in cx["basse16"]:
            p = {"R": r, "5": r + 7, "8": r + 12, "7": r + 10, "a": suiv - 1}[deg]
            if p > 57:
                p -= 12
            if p < 37:
                p += 12
            _place(bus["sec"], _basse_funk(hz(p), d * beat / 4 * 0.85, 0.10 * _vel(rng), rng), t + _seize(c, beat) + jeu())
    if "guitare" in couches:   # la partie rythmique, jouée par l'instrument principal de la partie
        lead = cx["lead"]
        v = _voix(acc, 67 if lead == "guitare" else 64)[-3:]
        for c in range(16):
            fort = c in cx["guit16"]
            if not fort and (lead != "guitare" or rng.random() < 0.55):
                continue
            for k, p in enumerate(v):
                if lead == "clav":
                    x = _rhodes_id(hz(p), beat / 4, 0.026 * _vel(rng), 0.95)
                elif lead == "orgue":
                    x = _orgue(hz(p), beat / 4 * 0.8, 0.016 * _vel(rng))
                else:
                    x = _guitare_etouffee(hz(p), (0.028 if fort else 0.010) * _vel(rng))
                _place(bus["sec"], x, t + _seize(c, beat) + 0.004 * k + jeu())
    if "clavier" in couches and j % cx["hr"] == 0:
        for k, p in enumerate(_voix(acc, 60)):
            _place(bus["sec"], _rhodes_id(hz(p), cx["hr"] * 4 * beat * 0.9, 0.020 * _vel(rng), 0.4), t + 0.01 * k)


def _init_ses2(cx, rng):
    cx["hats8"] = rng.random() < 0.35          # charleston en croches dans certaines parties, doubles croches ailleurs


def _transition_ses2(sorte, cx, rng, delai):
    s = _sig_transition(delai)
    beat, c = cx["beat"], cx["centre"]
    if sorte == "roulement":
        nb = int(delai / (beat / 4))
        for k in range(nb):
            _place(s, _caisse_id(0.008 + 0.03 * k / max(1, nb), rng), delai - (nb - k) * beat / 4)
    elif sorte == "montee":
        _place(s, _montee(delai, 0.03, rng), 0)
    _place(s, _grosse_caisse_id(0.12), delai)
    _place(s, _charley_id(0.02, rng, ouvert=True), delai)
    _place(s, _basse_funk(hz(c if c >= 40 else c + 12), beat, 0.10, rng), delai)
    return _salle(s, 0.7, 0.15, 5500, 5)


# --- HGGSP 2
def _phrase_hggsp2(cx, typ, rng):
    cx["hr"] = 2 if rng.random() < 0.75 else 1
    cx["mil"] = _pat(cx, "v_mil", MILITAIRE, rng)
    cx["ost"] = _pat(cx, "v_ost", OST16, rng)
    # d'une phrase à l'autre : pédale fixe ou basse qui suit les accords, ostinato sur la tonique ou sur l'accord,
    # à l'octave ou plus haut, en doubles croches ou en croches
    cx["mobile"] = typ in ("B", "pont") and rng.random() < 0.6 or rng.random() < 0.2
    cx["ost_acc"] = rng.random() < 0.45
    cx["ost_oct"] = 12 if rng.random() < 0.7 else 24
    cx["ost_croches"] = rng.random() < 0.3


def _init_hggsp2(cx, rng):
    cx["ost_inst"] = "cuivres" if rng.random() < 0.3 else "cordes"
    cx["mel"] = cx["centre"] + 31


def _mesure_hggsp2(bus, cx, t, j, L, typ, acc, couches, rng):
    beat = cx["beat"]
    mes = 4 * beat
    fin_phrase = j == L - 1
    tonique = cx["centre"]
    grave = tonique + (12 if tonique < 38 else 0)          # pédale jamais sous 70 Hz
    if "pedale" in couches and j % cx["hr"] == 0:
        b = acc["basse"] + (12 if acc["basse"] < 38 else 0) if cx["mobile"] else grave
        _place(bus["sec"], _cordes(hz(b), cx["hr"] * mes + 0.3, 0.050 * _vel(rng), 800, rng, attaque=0.8), t)
        for p in _voix(acc, 55)[:3]:
            _place(bus["sec"], _cordes(hz(p), cx["hr"] * mes + 0.3, 0.024 * _vel(rng), 1200, rng, attaque=1.0), t)
    if "ostinato" in couches:
        if cx["ost_acc"]:
            v = _voix(acc, tonique + cx["ost_oct"] + 4)
            notes = [v[0], v[1 % len(v)], v[2 % len(v)]]
        else:
            o = tonique + cx["ost_oct"]
            notes = [o, o + (1 if cx["mode"] == "phrygien" else 3), o + 7]
        for c, d in enumerate(cx["ost"]):
            a = 0.034 * _vel(rng) * (1.3 if c % 4 == 0 else 1) * (0.8 if cx["ost_oct"] == 24 else 1)
            if cx["ost_inst"] == "cuivres" or cx["ost_croches"]:
                if c % 2:
                    continue
                x = _cor(hz(notes[d]), beat / 3, a * 0.9, rng)
            else:
                x = _spiccato(hz(notes[d]), a, rng, 1100)
            _place(bus["sec"], x, t + c * beat / 4)
    if "caisse" in couches:   # caisse claire militaire : piste à part, retenue sous la voix par piste()
        for c, a in cx["mil"]:
            _place(bus["gene"], _caisse_id(0.11 * a * _vel(rng), rng, corps=180, timbre=(1200, 5000), decl=14, timbre_decl=9), t + c * beat / 4)
        if fin_phrase and not _parle(cx, t + 2 * beat - 0.2, t + mes + 0.3):   # roulement seulement dans un silence
            for k in range(16):
                _place(bus["gene"], _caisse_id((0.02 + 0.0055 * k) * _vel(rng), rng, corps=180, timbre=(1200, 5000), decl=14, timbre_decl=9),
                       t + 2 * beat + k * beat / 8)
    if "toms" in couches:
        for b in ((0, 2) if cx["hu"] != "calme" else (0,)):
            _place(bus["loin"], _tom(hz(tonique - 7 if tonique >= 45 else grave), 0.30 * _vel(rng)), t + b * beat)
    if "cuivres" in couches:   # la voix principale de la partie : cuivres tenus, violons, ou un cor seul
        lead = cx["lead"]
        if lead == "violons" and j % 2 == 0:
            ga = _gamme(cx["mode"], tonique, 67, 81)
            pcs = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
            p = min((q for q in ga if q % 12 in pcs), key=lambda q: abs(q - cx["mel"]))
            _place(bus["sec"], _cordes(hz(p), 2 * mes - 0.2, 0.022 * _vel(rng), 2400, rng, attaque=0.8), t)
            cx["mel"] = p
        elif lead == "cor_seul" and j % 2 == 0:
            ga = _gamme(cx["mode"], tonique, tonique + 19, tonique + 31)
            pcs = [(acc["r"] + iv) % 12 for iv in acc["iv"]]
            p = min((q for q in ga if q % 12 in pcs), key=lambda q: abs(q - cx["mel"]))
            _place(bus["sec"], _cor(hz(p), 2 * beat * 0.95, 0.045 * _vel(rng), rng), t)
            q = ga[int(np.clip(ga.index(p) + rng.choice([-1, 1, 2]), 0, len(ga) - 1))]
            _place(bus["sec"], _cor(hz(q), (mes + 2 * beat) * 0.95, 0.040 * _vel(rng), rng), t + 2 * beat)
            cx["mel"] = q
        elif lead == "cuivres" and j % 4 == 0:
            for p in (tonique + 12, tonique + 19):
                _place(bus["sec"], _cor(hz(p), 2 * mes * 0.9, 0.035 * _vel(rng), rng), t)


def _mix_hggsp2(bus, hu, graine):
    x = _salle(bus["sec"], 2.6, 0.30, 3000, graine)
    loin = _filtre_id(bus["loin"], "lowpass", 2400)       # lointains : peu d'aigus, beaucoup de salle
    x = x + 0.25 * loin + _salle(loin, 3.5, 1.0, 2000, graine + 1, predelai=0.05, sec=False)
    g = _filtre_id(bus["gene"], "lowpass", 2400)
    return x, 0.25 * g + _salle(g, 3.5, 1.0, 2000, graine + 2, predelai=0.05, sec=False)


def _transition_hggsp2(sorte, cx, rng, delai):
    s = _sig_transition(delai, 3.0)
    beat, c = cx["beat"], cx["centre"]
    if sorte == "roulement":
        nb = int(delai / (beat / 8))
        for k in range(nb):
            _place(s, _caisse_id(0.015 + 0.06 * k / max(1, nb), rng, corps=180, timbre=(1200, 5000), decl=14, timbre_decl=9),
                   delai - (nb - k) * beat / 8)
    elif sorte == "montee":
        _place(s, _cordes(hz(c + 19), delai, 0.04, 1600, rng, attaque=delai * 2.5), 0)
    _place(s, _timbale_id(hz(c + (12 if c < 41 else 0)), 0.12, rng), delai)
    _place(s, _tom(hz(c - 7 if c >= 45 else c + (12 if c < 38 else 0)), 0.2), delai)
    return _salle(_filtre_id(s, "lowpass", 3000), 2.8, 0.4, 2400, 5)


STYLES.update({
    "maths2": dict(couches=_couches_maths2, mesure=_mesure_maths2, phrase=_phrase_maths2, mix=_mix_maths2, temps=3),
    "maths3": dict(couches=_couches_maths3, mesure=_mesure_maths3, phrase=_phrase_maths3, mix=_mix_maths3,
                   init=_init_maths3, transition=_transition_maths3, transitions=("coupure", "roulement", "montee"),
                   leads=("pluck", "verre", "fm", "doux"), transpos=(0, 2, -2, 3, -3, 5), dbpm=4, creux=-6.0,
                   coeur=("nappe",), options=("pouls", "cloche", "sub")),
    "ses2": dict(couches=_couches_ses2, mesure=_mesure_ses2, phrase=_phrase_ses2, mix=_mix_ses2,
                 init=_init_ses2, transition=_transition_ses2, transitions=("coupure", "roulement", "montee"),
                 leads=("guitare", "clav", "orgue"), transpos=(0, 2, -2, 3, 5, -5), dbpm=4,
                 coeur=("basse",), options=("clavier", "charley", "batterie")),
    "ses3": dict(couches=_couches_ses3, mesure=_mesure_ses3, phrase=_phrase_ses3, mix=_mix_ses3),
    "hggsp2": dict(couches=_couches_hggsp2, mesure=_mesure_hggsp2, phrase=_phrase_hggsp2, mix=_mix_hggsp2,
                   init=_init_hggsp2, transition=_transition_hggsp2, transitions=("coupure", "roulement", "montee"),
                   leads=("cuivres", "violons", "cor_seul"), transpos=(0, 2, -2, 3, -3), dbpm=4,
                   coeur=("pedale",), options=("toms", "cuivres", "ostinato")),
    "hggsp3": dict(couches=_couches_hggsp3, mesure=_mesure_hggsp3, phrase=_phrase_hggsp3, mix=_mix_hggsp3, init=_init_hggsp3),
})
# =====================================================================================================================
# Philo, PC, SVT, DNL, ACL Lughnasa : la musique d'origine (nappe, arpège de piano, basse, frémissement, réverbération ;
# mêmes humeurs, même reel), mais en variantes d'une partie à l'autre au lieu d'une boucle (10/11/2026, demande du
# pilote : « évite vraiment ce sentiment de répétition »). Changent : grille (variantes diatoniques de la grille
# d'origine), tonalité (transposition), tempo (± 3), motif d'arpège, densité, entrées et sorties des instruments.
# Les vidéos déjà publiées gardent leur musique tant qu'on ne les régénère pas.
# =====================================================================================================================
NIVEAUX_CLASSIQUE = {"lumiere": 0.0739, "mystere": 0.0740, "tension": 0.0816, "calme": 0.0726, "reel": 0.1009}
BANQUES["classique"] = {   # la première grille de chaque humeur est celle de la boucle d'origine
    "lumiere": dict(bpm=84, arpege=1.0, nappe=0.20, registre=55, tons=[("eolien", 45, [
        ["0:m", "8:M", "3:M", "10:M"], ["0:m", "5:m", "8:M", "10:M"], ["8:M", "3:M", "10:M", "0:m"],
        ["3:M", "10:M", "0:m", "8:M"], ["0:m", "10:M", "8:M", "10:M"]])]),
    "mystere": dict(bpm=70, arpege=0.55, nappe=0.26, registre=50, tons=[("eolien", 38, [
        ["0:m", "8:M", "5:m", "7:M"], ["0:m", "5:m", "8:M", "7:M"], ["0:m", "3:M", "8:M", "7:M"],
        ["0:m", "8:M", "3:M", "7:sus4"]])]),
    "tension": dict(bpm=92, arpege=1.0, nappe=0.18, registre=51, tons=[("eolien", 40, [
        ["0:m", "8:M", "5:m", "7:M"], ["0:m", "5:m", "7:M", "0:m"], ["0:m", "10:M", "8:M", "7:M"],
        ["0:m", "3:M", "5:m", "7:M"]])]),
    "calme": dict(bpm=76, arpege=0.7, nappe=0.22, registre=52, tons=[("ionien", 41, [
        ["0:M", "7:M", "9:m", "5:M"], ["0:M", "9:m", "5:M", "7:M"], ["5:M", "0:M", "7:M", "9:m"],
        ["0:M", "2:m", "5:M", "7:sus4"]])]),
}
MOTIFS_CL = [MOTIF, [0, 1, 2, 3, 2, 1, 2, 3], [0, 2, 3, 2, 1, 2, 3, 1], [3, 2, 1, 0, 1, 2, 3, 2], [0, 3, 1, 2, 0, 3, 2, 1],
             [0, 1, 3, 2, 0, 1, 3, 1]]


def _quatre(acc, registre):
    """Les quatre notes de l'accord, comme dans la boucle d'origine (fondamentale, tierce, quinte, octave…)."""
    tons = sorted({(acc["r"] + iv) % 12 + 12 * o for iv in acc["iv"] for o in range(3, 8)})
    i = next(k for k, p in enumerate(tons) if p >= registre)
    return tons[i:i + 4]


def _couches_cl(typ, rng, hu):
    if typ == "intro":
        return [{"nappe"}, {"nappe", "arpege"}][rng.integers(2)]
    if typ == "respiration":
        return [{"nappe"}, {"nappe", "basse"}, {"arpege"}][rng.integers(3)]
    if typ == "pont":
        return [{"nappe", "arpege"}, {"basse", "arpege", "fremissement"}][rng.integers(2)]
    c = {"nappe", "basse", "arpege", "fremissement"}
    if typ == "A" and rng.random() < 0.3:
        c.discard("fremissement")
    return c


def _init_cl(cx, rng):
    H = BANQUES["classique"][cx["hu"]]
    cx["H"] = H
    r = H["registre"] + (cx["centre"] - H["tons"][0][1])
    cx["registre"] = r - 12 if r > 58 else r + 12 if r < 47 else r


def _phrase_cl(cx, typ, rng):
    cx["hr"] = 1 if cx["hu"] == "tension" and rng.random() < 0.3 else 2
    cx["motif"] = _pat(cx, "v_motif", MOTIFS_CL, rng)
    cx["noires"] = cx["H"]["arpege"] < 0.8 if rng.random() < 0.75 else not (cx["H"]["arpege"] < 0.8)
    cx["oct"] = 24 if typ == "B" and rng.random() < 0.3 else 12
    cx["bt"] = [(0, 2), (0, 2), (0,), (0, 2, 3)][int(rng.integers(4))]


def _mesure_cl(bus, cx, t, j, L, typ, acc, couches, rng):
    beat, H = cx["beat"], cx["H"]
    mes = 4 * beat
    notes = _quatre(acc, cx["registre"])
    if "nappe" in couches and j % cx["hr"] == 0:
        _place(bus["sec"], _nappe([hz(m) for m in notes[:3]], cx["hr"] * mes + 1.2, H["nappe"]), t)
    if "basse" in couches:
        for b in cx["bt"]:
            nb = _note_piano(hz(acc["basse"] + (12 if acc["basse"] < 38 else 0)), 1.6, 0.20)
            _place(bus["sec"], nb * np.exp(-np.arange(len(nb)) / SR * 0.8), t + b * beat)
    if "arpege" in couches:
        for c in range(8):
            if cx["noires"] and c % 2:
                continue
            m = notes[cx["motif"][c] % len(notes)] + (cx["oct"] if notes[cx["motif"][c] % len(notes)] + cx["oct"] <= 88 else 12)
            amp = (0.075 if c % 2 == 0 else 0.055) * H["arpege"]
            _place(bus["sec"], _note_piano(hz(m), 0.9, amp), t + c * beat / 2)
    if "fremissement" in couches:
        for c in range(1, 8, 2):
            n = int(0.05 * SR)
            bruit = np.diff(rng.standard_normal(n), prepend=0) * np.exp(-np.arange(n) / SR * 90)
            _place(bus["sec"], 0.012 * bruit, t + c * beat / 2)


def _mix_cl(bus, hu, graine):
    return _reverb(bus["sec"])


def _reel_variante(duree, rng, prec, paroles):
    """Le reel de Lughnasa, joué autrement à chaque fois : tonalité, tempo, ordre des reprises, violon seul au début,
    second violon à l'octave, tambour plus ou moins chargé. Toujours un reel."""
    tp = _autre((0, -5, -7), prec.get("transpo"), rng)
    croche = 60.0 / (113 + rng.uniform(-3, 3)) / 2
    ordres = [REEL_A + REEL_A + REEL_B + REEL_B, REEL_A + REEL_B + REEL_A + REEL_B, REEL_B + REEL_B + REEL_A + REEL_A]
    melodie = ordres[int(rng.integers(len(ordres)))]
    entree = int(rng.choice([0, 4, 8]))            # mesures de violon seul
    double = rng.random() < 0.5                    # second violon à l'octave inférieure sur les reprises
    n = int((duree + 4.0) * SR)
    out = np.zeros(n)
    t, k = 0.0, 0
    while t < duree - 0.2:
        mesure = melodie[k % len(melodie)]
        acc = REEL_ACC[REEL_GRILLE[k % len(REEL_GRILLE)]]
        reprise = (k // 8) % 2 == 1
        for c, m in enumerate(mesure):
            if m:
                _ajoute(out, _violon(hz(m + tp), croche * 1.05, 0.11 if c % 2 == 0 else 0.085), int((t + c * croche) * SR))
                if double and reprise:
                    _ajoute(out, _violon(hz(m + tp - 12), croche * 1.05, 0.05), int((t + c * croche + 0.004) * SR))
        if k >= entree:
            lourd = (k // 8) % 2 == 0 or rng.random() < 0.5
            for b in range(4):
                i = int((t + b * 2 * croche) * SR)
                if lourd or b % 2 == 0:
                    L = int(0.18 * SR); tt = np.arange(L) / SR
                    _ajoute(out, (0.32 if b % 2 == 0 else 0.22) * np.sin(2 * np.pi * (75 - 30 * tt) * tt) * np.exp(-tt * 22), i)
                if b % 2 == 0:
                    _ajoute(out, _note_piano(hz(acc[0] + tp), 0.5, 0.22), i)
                else:
                    for m in acc[1]:
                        _ajoute(out, _note_piano(hz(m + tp), 0.25, 0.06), i)
        t += 8 * croche
        k += 1
    out = np.tanh(2.2 * out) / np.tanh(2.2)          # le son « raucous » d'un vieux poste
    cx = {"centre": 38 + tp, "beat": 2 * croche}
    return out, cx, {"transpo": tp, "ton": ("reel", 0), "texture": None, "lead": None}


_CLASSIQUE = dict(couches=_couches_cl, mesure=_mesure_cl, phrase=_phrase_cl, mix=_mix_cl, init=_init_cl, banque="classique",
                  transitions=("fondu",), transpos=(0, 2, -2, 3, -3), dbpm=3, modulation=0.4, traitement=False,
                  niveaux=NIVEAUX_CLASSIQUE, coeur=("nappe",), options=("fremissement", "basse", "arpege"))
STYLES.update({nom: dict(_CLASSIQUE) for nom in ("philo1", "pc1", "svt1", "dnl1")})
STYLES["lughnasa1"] = dict(_CLASSIQUE, special={"reel": _reel_variante})


# style de chaque site (choix du pilote du 10/11/2026 pour maths, ses, hggsp) ; piste(…, style="ses1") en force un autre
STYLE = {"maths": "maths3", "ses": "ses2", "hggsp": "hggsp2",
         "philo": "philo1", "pc": "pc1", "svt": "svt1", "dnl": "dnl1", "acl-lughnasa": "lughnasa1"}

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


def _marimba_labo(f, dur, amp):
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


def _caisse_labo(amp):
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
            _ajoute(out, _marimba_labo(hz(m), 0.8, amp), int((t + c * beat / 2) * SR))
        # pulsation feutrée
        if H["pulse"] > 0:
            for b in range(8):
                if b % 2 == 0:
                    _ajoute(out, _caisse_labo(0.085 * H["pulse"]), int((t + b * beat) * SR))
                _ajoute(out, _charleston(rng, 0.026 * H["pulse"]), int((t + (b + 0.5) * beat) * SR))
        # bulles : quelques-unes par mesure, placées au hasard (graine fixe)
        for _ in range(int(round(3 * H["bulles"]))):
            _ajoute(out, _bulle(rng, 0.05 * H["bulles"]), int((t + rng.random() * d) * SR))
        t += d
        k += 1
    out = _reverb(out, duree=1.8, mix=0.26)
    return out[:int(duree * SR)]

# ===================================================================================================
# MUSIQUE LO-FI (vidéos SVT, 10/11/2026). Demande de Cengiz : « changer la musique de fond, c'est tout le temps la
# même chose, la même que Philo » ; parmi trois propositions (documentaire, lo-fi, pizzicato), il a choisi la lo-fi.
# Cinq thèmes originaux qui alternent d'une partie à l'autre : piano électrique (synthèse FM), piano feutré, guitare
# pincée, kalimba ou vibraphone en solo, accords de septième, basse ronde, batterie feutrée et « swinguée », son
# étouffé façon cassette, craquements de vinyle et une ambiance légère (pluie, oiseaux, grillons…). Chaque thème est
# une boucle de 32 mesures (intro sans batterie, couplet, mélodie, pause, reprise), raccord sans couture. Déterministe.
# ===================================================================================================
LOFI = {
    # bpm, swing, grille de 4 accords (basse, notes), instrument des accords, instrument de la mélodie, gamme de la
    # mélodie, motif de grosse caisse (en temps), ambiance
    "etude": dict(bpm=76, swing=.58, acc=[(41, [57, 60, 64, 69]), (40, [55, 59, 62, 67]), (38, [57, 60, 64, 65]), (36, [55, 59, 62, 64])],
                  clavier="rhodes", solo="rhodes", gamme=[64, 67, 69, 71, 72, 74, 76], kick=[0, 2.5], amb=None),
    "pluie": dict(bpm=70, swing=.6, acc=[(45, [55, 60, 64, 71]), (41, [57, 60, 64, 67]), (48, [55, 59, 64, 67]), (43, [55, 59, 62, 64])],
                  clavier="feutre", solo="feutre", gamme=[69, 71, 72, 74, 76, 79, 81], kick=[0, 1.75, 2.5], amb="pluie"),
    "jardin": dict(bpm=82, swing=.57, acc=[(38, [53, 57, 60, 64]), (43, [53, 59, 64, 65]), (36, [55, 59, 62, 64]), (45, [55, 60, 64, 67])],
                   clavier="rhodes", solo="guitare", gamme=[62, 64, 65, 67, 69, 72, 74], kick=[0, 2, 2.75], amb="oiseaux"),
    "nuit": dict(bpm=72, swing=.6, acc=[(39, [55, 58, 62, 67]), (38, [53, 57, 60, 65]), (36, [55, 58, 62, 63]), (34, [53, 57, 62, 65])],
                 clavier="feutre", solo="kalimba", gamme=[67, 70, 72, 74, 75, 77, 79], kick=[0, 2.5, 3.25], amb="grillons"),
    "vague": dict(bpm=78, swing=.57, acc=[(43, [59, 62, 66, 69]), (42, [57, 61, 64, 69]), (40, [55, 59, 62, 66]), (38, [57, 61, 64, 66])],
                  clavier="rhodes", solo="vibra", gamme=[66, 67, 69, 71, 74, 76, 78], kick=[0, 1.5, 2.5], amb="eau"),
}
ORDRE_LOFI = ["etude", "jardin", "pluie", "vague", "nuit"]


def _rhodes(f, dur, amp):          # piano électrique : synthèse FM, trémolo
    t = np.arange(int(dur * SR)) / SR
    idx = 1.6 * np.exp(-t * 5) + 0.25
    s = (np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
         + 0.15 * np.sin(2 * np.pi * 14 * f * t) * np.exp(-t * 30))
    env = np.minimum(1, t / 0.004) * np.exp(-t * 1.3) * np.clip((dur - t) / 0.08, 0, 1)
    return amp * s * env * (1 + 0.12 * np.sin(2 * np.pi * 4.5 * t))


def _feutre(f, dur, amp):          # piano feutré : peu d'harmoniques, attaque douce
    t = np.arange(int(dur * SR)) / SR
    s = sum(np.sin(2 * np.pi * f * k * np.sqrt(1 + 0.0004 * k * k) * t + k) * np.exp(-t * (1.2 + 1.4 * k)) / k ** 1.6
            for k in range(1, 6))
    env = np.minimum(1, t / 0.012) * (0.7 * np.exp(-t * 0.9) + 0.3 * np.exp(-t * 4)) * np.clip((dur - t) / 0.1, 0, 1)
    return amp * 1.3 * s * env


def _guitare(f, dur, amp):         # guitare pincée
    t = np.arange(int(dur * SR)) / SR
    s = sum(np.sin(2 * np.pi * k * f * t) * np.exp(-t * (2.2 + 1.5 * k)) / k for k in range(1, 8))
    return amp * 1.2 * s * np.minimum(1, t / 0.003) * np.clip((dur - t) / 0.06, 0, 1)


def _kalimba(f, dur, amp):
    t = np.arange(int(dur * SR)) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.32 * np.sin(2 * np.pi * 5.4 * f * t) * np.exp(-t * 9)
         + 0.08 * np.sin(2 * np.pi * 2.01 * f * t) * np.exp(-t * 4))
    return amp * s * np.exp(-t * 3.2) * np.minimum(1, t / 0.0015)


def _vibra(f, dur, amp):           # vibraphone : son pur, trémolo du moteur
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f * t) + 0.2 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t * 6)
    return amp * s * np.exp(-t * 1.6) * np.minimum(1, t / 0.002) * (1 + 0.3 * np.sin(2 * np.pi * 5.5 * t))


def _basse_ronde(f, dur, amp):
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)
    return amp * s * np.exp(-t * 1.6) * np.minimum(1, t / 0.01) * np.clip((dur - t) / 0.05, 0, 1)


def _filtre(x, fc, type_="low"):
    from scipy.signal import butter, lfilter
    b, a = butter(2, fc / (SR / 2), type_)
    return lfilter(b, a, x)


def _grosse_caisse(amp):
    t = np.arange(int(0.35 * SR)) / SR
    f = 48 + 70 * np.exp(-t * 28)
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def _caisse_claire(amp, rng):
    t = np.arange(int(0.25 * SR)) / SR
    br = _filtre(rng.standard_normal(len(t)), 4200) * np.exp(-t * 18)
    return amp * (0.7 * br + 0.4 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 25))


def _charley(amp, rng):
    t = np.arange(int(0.05 * SR)) / SR
    return amp * _filtre(rng.standard_normal(len(t)), 7000, "high") * np.exp(-t * 70)


def _ambiance(n, genre, rng):
    t = np.arange(n) / SR
    out = np.zeros(n)
    if genre in ("pluie", "eau"):
        b = _filtre(rng.standard_normal(n), 2200 if genre == "pluie" else 700)
        if genre == "pluie":
            b = _filtre(b, 400, "high")
        lfo = 0.75 + 0.25 * np.sin(2 * np.pi * t / (13 if genre == "pluie" else 5.3))
        out += b / (np.abs(b).max() + 1e-9) * lfo * (0.05 if genre == "pluie" else 0.06)
    if genre == "oiseaux":
        k = 0.0
        while k < n / SR:
            k += 5 + rng.random() * 8
            for j in range(1 + int(rng.random() * 3)):      # deux ou trois notes de chant
                L = int(SR * (0.07 + rng.random() * 0.06)); tt = np.arange(L) / SR
                f0 = 2600 + rng.random() * 1800
                ch = np.sin(2 * np.pi * (f0 * tt + (700 + rng.random() * 900) * tt ** 2 / (2 * tt[-1] + 1e-9)))
                _ajoute(out, 0.025 * ch * np.sin(np.pi * tt / tt[-1]) ** 2, int((k + j * 0.11) * SR))
    if genre == "grillons":
        pulse = (np.sin(2 * np.pi * 28 * t) > 0.3) * (np.sin(2 * np.pi * 0.45 * t) > -0.2)
        out += 0.009 * np.sin(2 * np.pi * 4300 * t) * pulse
    return out


def lofi(theme, mesures=32):
    """Boucle de `mesures` mesures du thème lo-fi, raccord sans couture. Plan sur 32 mesures : intro sans batterie (0-3),
    couplet (4-7), mélodie (8-15), pause sans grosse caisse ni basse (16-19), reprise (20-23), mélodie variée (24-31)."""
    H = LOFI[theme]
    b = 60.0 / H["bpm"]
    n = int(round(mesures * 4 * b * SR))
    out = np.zeros(n + 3 * SR)
    rng = np.random.default_rng(sum(map(ord, theme)) + 31)
    clavier = {"rhodes": _rhodes, "feutre": _feutre}[H["clavier"]]
    solo = {"rhodes": _rhodes, "feutre": _feutre, "guitare": _guitare, "kalimba": _kalimba, "vibra": _vibra}[H["solo"]]
    rythmes = [[(0, 1.5), (1.5, 1), (2.5, 1.5)], [(0.5, 1.5), (2, 2)], [(0, 1), (1, 0.5), (1.5, 1), (3, 1)],
               [(1, 1), (2.5, 1.5)], [(0, 2), (2.5, 0.5), (3, 1)]]
    for m in range(mesures):
        basse, notes = H["acc"][m % 4]
        t0 = m * 4 * b
        intro, pause = m < 4, 16 <= m < 20
        # accords : posés sur le 1 et sur le « et » du 3, égrenés de quelques millisecondes
        for d, L in ((0, 2.3), (2.5, 1.4)):
            for k, x in enumerate(notes):
                _ajoute(out, clavier(hz(x), L * b, 0.07 * (0.9 + 0.2 * rng.random())), int((t0 + d * b + 0.025 * k) * SR))
        if not (intro or pause):
            _ajoute(out, _basse_ronde(hz(basse), 1.8 * b, 0.22), int(t0 * SR))
            _ajoute(out, _basse_ronde(hz(basse + (7 if m % 2 else 12)), 1.0 * b, 0.15), int((t0 + 2.5 * b) * SR))
        # batterie
        if not intro:
            for be in range(4):
                for c, a in ((0, 0.05), (H["swing"], 0.03)):
                    _ajoute(out, _charley(a * (0.8 + 0.4 * rng.random()), rng), int((t0 + (be + c) * b) * SR))
            if not pause:
                for p in H["kick"]:
                    _ajoute(out, _grosse_caisse(0.32 if p == 0 else 0.24), int((t0 + p * b) * SR))
                for be in (1, 3):
                    _ajoute(out, _caisse_claire(0.17, rng), int((t0 + be * b + 0.015) * SR))
        # mélodie : notes de la gamme proches de l'accord, rythmes tirés au sort mais fixés par le thème
        if 8 <= m < 16 or 24 <= m < 32:
            ry = rythmes[int(rng.integers(len(rythmes)))]
            for d, L in ry:
                x = H["gamme"][int(rng.integers(len(H["gamme"])))] + 12
                _ajoute(out, solo(hz(x), L * b + 0.4, 0.055), int((t0 + d * b) * SR))
    out = out[:n] + np.concatenate([out[n:], np.zeros(n - len(out[n:]))])[:n]   # la queue revient au début : boucle continue
    # son « cassette » (étouffé) et réverbération circulaire courte
    out = _filtre(np.concatenate([out[-SR:], out]), 3600)[SR:]
    rr = np.random.default_rng(7); L = int(1.4 * SR)
    ir = rr.standard_normal(L) * np.exp(-np.arange(L) / SR * 4); ir /= np.sqrt((ir ** 2).sum())
    irp = np.zeros(n); irp[:L] = ir
    out = 0.82 * out + 0.18 * np.fft.irfft(np.fft.rfft(out) * np.fft.rfft(irp), n)
    # craquements de vinyle et souffle
    vin = np.zeros(n + SR)
    for i in rng.integers(0, n, int(n / SR * 8)):
        L = int(0.08 * SR); tt = np.arange(L) / SR
        _ajoute(vin, 0.035 * rng.random() * _filtre(rng.standard_normal(L), 1800, "high") * np.exp(-tt * 60), int(i))
    vin = vin[:n] + 0.004 * _filtre(rng.standard_normal(n), 2500)
    out = out + vin
    if H["amb"]:
        out += _ambiance(n, H["amb"], np.random.default_rng(29))
    return out.astype(np.float32)


def theme_lofi(k, humeur=None):
    """Thème de la k-ième partie de la vidéo : les cinq thèmes tournent, jamais deux fois de suite le même."""
    return ORDRE_LOFI[k % len(ORDRE_LOFI)]
