"""Musiques « épiques » des shorts : partitions originales écrites en MIDI, jouées par FluidSynth
avec la banque General MIDI FluidR3 (licence MIT : vraies cordes, chœurs, timbales, cuivres, harpe, sons 8 bits).

Chaque morceau est écrit en couches (stems) de plus en plus fortes ; `composer()` de musique_short.py
les mélange selon le niveau de tension du short (chapitres, chocs, relâche), comme pour les autres styles.

Installation dans un conteneur neuf :
  apt-get update && apt-get install -y fluidsynth fluid-soundfont-gm && pip install mido
Essai : python3 orchestre.py <style> [durée]  -> sortie/essai-<style>.wav
"""
import os, subprocess, sys, tempfile
import numpy as np
import mido
import soundfile as sf

SR = 48000
SF2 = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
ICI = os.path.dirname(os.path.abspath(__file__))

# instruments General MIDI (numéro de programme)
CORDES, CORDES_LENTES, TREMOLO, PIZZ, VIOLONCELLE, CONTREBASSE = 48, 49, 44, 45, 42, 43
CHOEUR, VOIX_OOH, HARPE, GUITARE, PIANO, CELESTA = 52, 53, 46, 24, 0, 8
CUIVRES, COR, TROMBONE, TUBA, TROMPETTE, HIT = 61, 60, 57, 58, 56, 55
TIMBALES, TAIKO, CARRE, SCIE, BASSE_SYNTH, NAPPE = 47, 116, 80, 81, 38, 89
BATTERIE = "batterie"  # canal 10
GC, CAISSE, CHARLEY, CRASH, TOM_G, TOM_M, TOM_A, BLOC, CHARLEY_O, RIDE, CLAP = 36, 38, 42, 49, 41, 45, 48, 76, 46, 51, 39

NOTES = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
         "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}


def n(nom):
    """'E4' -> 64 (do central C4 = 60)."""
    o = int(nom[-1]); return 12 * (o + 1) + NOTES[nom[:-1]]


def accord(nom, octave=3):
    """'Em' / 'C' / 'A' -> (fondamentale, tierce, quinte) en MIDI à l'octave donnée."""
    mineur = nom.endswith("m"); r = n(nom.rstrip("m") + str(octave))
    return [r, r + (3 if mineur else 4), r + 7]


class Partition:
    """Notes rangées par couche : couche -> instrument -> [(début en temps, durée en temps, note, vélocité)]."""
    def __init__(self, bpm):
        self.bpm, self.couches, self.synth = bpm, {}, []

    def note(self, couche, instr, debut, duree, note, vel=90):
        self.couches.setdefault(couche, {}).setdefault(instr, []).append((debut, duree, note, vel))

    def notes(self, couche, instr, debut, suite, vel=90):
        """suite = [(note ou nom ou None, durée)] jouées à la file."""
        t = debut
        for x, d in suite:
            if x is not None: self.note(couche, instr, t, d * .98, n(x) if isinstance(x, str) else x, vel)
            t += d
        return t

    def son(self, couche, debut, x, g=1.0):
        """Son synthétisé (signal mono numpy) posé au temps `debut` (en temps) dans la couche."""
        self.synth.append((couche, debut, x * g))

    def frappe(self, couche, son, debut, vel=100):
        self.note(couche, BATTERIE, debut, .25, son, vel)

    def midi(self, couche, chemin):
        mf = mido.MidiFile(ticks_per_beat=480); tps = 480
        canaux = {}
        for instr, ev in self.couches[couche].items():
            if instr == BATTERIE: ch = 9
            else:
                ch = len([c for c in canaux.values() if c != 9]); ch = ch + 1 if ch >= 9 else ch
            canaux[instr] = ch
            pi = mido.MidiTrack(); mf.tracks.append(pi)
            pi.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm), time=0))
            if ch != 9: pi.append(mido.Message("program_change", channel=ch, program=instr, time=0))
            pi.append(mido.Message("control_change", channel=ch, control=91, value=70, time=0))  # réverbération
            msgs = []
            for d, du, note, v in ev:
                msgs.append((int(d * tps), 1, mido.Message("note_on", channel=ch, note=int(note), velocity=int(v))))
                msgs.append((int((d + du) * tps), 0, mido.Message("note_off", channel=ch, note=int(note), velocity=0)))
            msgs.sort(key=lambda m: (m[0], m[1])); t0 = 0
            for t, _, m in msgs: m.time = t - t0; t0 = t; pi.append(m)
        mf.save(chemin)

    def rendre(self, dur):
        """-> {couche: signal stéréo (n, 2) de dur secondes}."""
        sortie = {}
        with tempfile.TemporaryDirectory() as dos:
            for c in self.couches:
                mid, wav = os.path.join(dos, f"{c}.mid"), os.path.join(dos, f"{c}.wav")
                self.midi(c, mid)
                subprocess.run(["fluidsynth", "-ni", "-g", "0.6", "-r", str(SR), "-F", wav, SF2, mid],
                               check=True, capture_output=True)
                x, sr = sf.read(wav, dtype="float32")
                if x.ndim == 1: x = np.stack([x, x], 1)
                m = int(dur * SR); x = x[:m] if len(x) >= m else np.pad(x, ((0, m - len(x)), (0, 0)))
                sortie[c] = x
        m = int(dur * SR)
        for c, debut, x in self.synth:
            if c not in sortie: sortie[c] = np.zeros((m, 2), np.float32)
            i = int(debut * 60 / self.bpm * SR)
            if i >= m: continue
            k = min(len(x), m - i); sortie[c][i:i + k] += x[:k, None] if x.ndim == 1 else x[:k]
        return sortie


# ---------------------------------------------------------------- morceaux (partitions originales)
# Chaque fonction écrit `mesures` mesures à 4 temps, en boucle sur sa grille d'accords, en trois couches :
# 1 = fond (toujours là), 2 = montée, 3 = plein. Le mélange choisit les couches selon le niveau du short.

def epopee(mesures):
    """Épopée héroïque façon final de jeu vidéo : ostinato de cordes, timbales, chœur, cuivres et lead 8 bits.
    Mi mineur, 150 bpm."""
    P = Partition(150)
    grille = ["Em", "C", "G", "D"]
    melo = [  # mélodie originale, une mesure par accord
        [("E5", 1.5), ("B4", .5), ("E5", 1), ("F#5", 1)],
        [("G5", 2), ("F#5", 1), ("E5", 1)],
        [("D5", 1.5), ("B4", .5), ("D5", 1), ("G5", 1)],
        [("F#5", 2), ("A5", 1), ("F#5", 1)],
        [("G5", 1.5), ("F#5", .5), ("E5", 1), ("B5", 1)],
        [("C6", 2), ("B5", 1), ("G5", 1)],
        [("B5", 1.5), ("A5", .5), ("G5", 1), ("D6", 1)],
        [("C#6", 1), ("D6", 2), (None, 1)],
    ]
    for m in range(mesures):
        a = grille[m % 4]; r, ti, q = accord(a, 3); t = m * 4
        for k in range(8):  # ostinato de croches : fondamentale, quinte, octave, quinte
            P.note(1, CORDES, t + k * .5, .45, [r, q, r + 12, q][k % 4], 78 + 10 * (k % 2 == 0))
        P.note(1, VIOLONCELLE, t, 4, r - 12, 85)
        P.note(2, CHOEUR, t, 4, ti + 12, 70); P.note(2, CHOEUR, t, 4, q + 12, 70); P.note(2, CHOEUR, t, 4, r + 12, 70)
        P.note(2, TIMBALES, t, 1, r - 12, 110); P.note(2, TIMBALES, t + 2, 1, r - 12, 95)
        P.notes(2, COR, t, [(ti + 12, 2), (q + 12, 2)], 80)
        if m % 4 == 3:  # roulement de timbales vers la mesure suivante
            for k in range(8): P.note(2, TIMBALES, t + 2 + k * .25, .25, r - 12, 60 + 6 * k)
        P.notes(3, CUIVRES, t, melo[m % 8], 105)
        P.notes(3, CARRE, t, [(None if x is None else n(x) + 12, d) for x, d in melo[m % 8]], 55)
        P.note(3, CONTREBASSE, t, 4, r - 24, 100)
        for b in range(4):
            P.frappe(3, GC, t + b, 110 if b % 2 == 0 else 90)
            if b % 2: P.frappe(3, CAISSE, t + b, 105)
        if m % 4 == 0: P.frappe(3, CRASH, t, 110); P.frappe(2, CRASH, t, 80)
    return P


def heritage(mesures):
    """Mélancolie héroïque (esprit « famille d'assassins ») : harpe en triolets, voix, violoncelles, puis tambours.
    Ré mineur, 72 bpm, balancement ternaire."""
    P = Partition(72)
    grille = ["Dm", "Bb", "F", "C", "Dm", "Bb", "Gm", "A"]
    melo = [
        [("A4", 2), ("D5", 1), ("C5", 1)], [("D5", 2), ("F5", 1), ("E5", 1)],
        [("C5", 3), ("A4", 1)], [("G4", 2), ("E4", 2)],
        [("A4", 2), ("D5", 1), ("E5", 1)], [("F5", 2), ("E5", 1), ("D5", 1)],
        [("D5", 2), ("Bb4", 2)], [("C#5", 4)],
    ]
    for m in range(mesures):
        a = grille[m % 8]; r, ti, q = accord(a, 3); t = m * 4
        motif = [r, q, r + 12, ti + 12, r + 12, q]
        for k in range(12):  # triolets de croches
            P.note(1, HARPE, t + k / 3, .6, motif[k % 6], 80 if k % 3 == 0 else 62)
        P.note(1, VIOLONCELLE, t, 4, r - 12, 75)
        P.notes(2, VOIX_OOH, t, melo[m % 8], 88)
        P.note(2, CORDES_LENTES, t, 4, ti + 12, 55); P.note(2, CORDES_LENTES, t, 4, q + 12, 55)
        P.note(3, CHOEUR, t, 4, r + 12, 80); P.note(3, CHOEUR, t, 4, q + 12, 80)
        P.notes(3, CORDES, t, [(x if x is None else n(x) + 12, d) for x, d in melo[m % 8]], 82)
        P.note(3, CONTREBASSE, t, 4, r - 24, 95)
        for b in range(4):  # tambours : grosse frappe au temps 1 et 3, triolets de toms au 4
            if b in (0, 2): P.note(3, TIMBALES, t + b, 1, r - 12, 112)
            P.frappe(3, TOM_G, t + b, 100 if b in (0, 2) else 70)
        for k in range(3): P.frappe(3, TOM_M, t + 3 + k / 3, 70 + 12 * k)
        if m % 4 == 0: P.frappe(3, CRASH, t, 95)
    return P


def boss(mesures):
    """Combat de boss en 8 bits : riff carré en doubles croches, basse en scie, batterie. Ré mineur, 168 bpm."""
    P = Partition(168)
    grille = ["Dm", "Bb", "C", "A"]
    riff = [  # riff original, 16 doubles croches par mesure (None = silence)
        ["D5", None, "D5", "C5", None, "A4", "D5", None, "F5", None, "E5", "D5", "C5", None, "A4", "C5"],
        ["Bb4", None, "Bb4", "A4", None, "F4", "Bb4", None, "D5", None, "C5", "Bb4", "A4", None, "F4", "A4"],
        ["C5", None, "C5", "Bb4", None, "G4", "C5", None, "E5", None, "F5", "G5", "E5", None, "C5", "E5"],
        ["A4", "C#5", "E5", "A5", None, "G5", "F5", "E5", "C#5", "E5", "A5", "C#6", "E6", None, "C#6", "A5"],
    ]
    for m in range(mesures):
        a = grille[m % 4]; r, ti, q = accord(a, 2); t = m * 4
        for k in range(8): P.note(1, BASSE_SYNTH, t + k * .5, .4, r if k % 2 == 0 else r + 12, 100)
        for b in range(4): P.frappe(1, GC, t + b, 105)
        for k in range(8): P.frappe(1, CHARLEY, t + k * .5, 70)
        for k, x in enumerate(riff[m % 4]):
            if x: P.note(2, CARRE, t + k * .25, .22, n(x), 92)
        P.frappe(2, CAISSE, t + 1, 110); P.frappe(2, CAISSE, t + 3, 110)
        for k in range(16): P.note(3, SCIE, t + k * .25, .2, [r + 24, ti + 24, q + 24, ti + 24][k % 4], 55)
        P.note(3, CORDES, t, 4, r + 12, 70); P.note(3, CORDES, t, 4, q + 12, 70)
        if m % 2 == 1:
            for k in range(4): P.frappe(3, [TOM_A, TOM_M, TOM_G, TOM_G][k], t + 3 + k * .25, 110)
        if m % 4 == 0: P.frappe(3, CRASH, t, 115)
    return P


def bande_annonce(mesures):
    """Bande-annonce sombre : cordes martelées, tic-tac, « braams » de cuivres graves, chœur et frappes.
    Ré mineur, 120 bpm."""
    P = Partition(120)
    grille = ["Dm", "Dm", "Bb", "A"]
    for m in range(mesures):
        a = grille[m % 4]; r, ti, q = accord(a, 2); t = m * 4
        for k in range(16): P.note(1, CORDES, t + k * .25, .2, r + (12 if k % 4 == 3 else 0), 95 if k % 4 == 0 else 70)
        for k in range(8): P.frappe(1, BLOC, t + k * .5, 65)
        if m % 2 == 0:  # braam : trombones et tuba sur deux mesures
            for x in (r - 12, r, q): P.note(2, TROMBONE, t, 7.5, x, 110)
            P.note(2, TUBA, t, 7.5, r - 12, 115)
        P.note(2, CHOEUR, t, 4, r + 12, 75); P.note(2, CHOEUR, t, 4, ti + 12, 75)
        P.note(2, TIMBALES, t, 1, r, 115)
        for b in range(4): P.frappe(3, TOM_G, t + b, 115); P.frappe(3, GC, t + b, 100)
        for k in range(4): P.frappe(3, TOM_A, t + 3 + k * .25, 90 + 8 * k)
        for k in range(8): P.note(3, CORDES, t + k * .5, .45, [r + 24, q + 24, ti + 24, q + 24][k % 4], 95)
        P.notes(3, COR, t, [(r + 12, 2), (ti + 12, 1), (q + 12, 1)], 105)
        if m % 4 == 0: P.note(3, HIT, t, 1, r + 12, 120); P.frappe(3, CRASH, t, 120)
    return P



# ---------------------------------------------------------------- sons synthétisés (numpy)
from musique_short import scie, lp, hp, bp, clap, charley, R as _R


def fq(note):
    return 440 * 2 ** ((note - 69) / 12)


def kick_dur(d=.34):
    """Kick saturé de hardtekk : attaque sèche, chute de hauteur, queue grave distordue."""
    k = int(d * SR); t = np.arange(k) / SR
    fr = 46 + 190 * np.exp(-t * 28)
    corps = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .2)
    x = np.tanh(corps * 6) * .8 + bp(_R.standard_normal(k), 2000, 8000) * np.exp(-t / .004) * .5
    return lp(x, 7000) * np.minimum(1, (d - t) / .01)


def supersaw(f, d, coupure=6000, att=.005, rel=.08):
    """Sept scies désaccordées (lead de hardtekk / trance), enveloppe courte."""
    k = int(d * SR)
    x = sum(scie(f * 2 ** (dc / 1200), k) for dc in (-24, -14, -6, 0, 6, 14, 24)) / 7
    e = np.minimum(1, np.arange(k) / (att * SR + 1)) * np.minimum(1, (k - np.arange(k)) / (rel * SR + 1))
    return lp(x, coupure) * e


def basse_roulante(f, d):
    k = int(d * SR); t = np.arange(k) / SR
    return np.tanh(lp(scie(f, k), 900) * 2.5) * np.exp(-t / (d * .7)) * .6


def pulsation(f, d, coupure=2500):
    """Note de synthé courte et filtrée (arpège pulsé façon bande originale électro-orchestrale)."""
    k = int(d * SR); t = np.arange(k) / SR
    return lp(scie(f, k) + .5 * scie(f * 2.003, k), coupure) * np.exp(-t / (d * .45)) * np.minimum(1, t / .002)


def riser(d):
    k = int(d * SR); r = np.linspace(0, 1, k) ** 2.5
    return hp(_R.standard_normal(k), 1500) * r * .4


# ---------------------------------------------------------------- morceaux inspirés des références de Cengiz
# (énergie, tempo, construction ; mélodies et harmonies originales)

def hardtekk(mesures):
    """Hardtekk épique, 160 bpm, sol dièse mineur : kick saturé sur chaque temps, basse roulante, lead supersaw,
    chœur et cordes. Couche 1 : thème au piano et nappe ; 2 : kick, basse, accords ; 3 : lead, clap, charleys."""
    P = Partition(160)
    grille = ["G#m", "E", "B", "F#"]
    melo = [
        [("D#5", 1), ("G#5", 1), ("F#5", .5), ("D#5", .5), ("B4", 1)],
        [("E5", 1.5), ("D#5", .5), ("B4", 1), ("G#4", 1)],
        [("F#5", 1), ("D#5", .5), ("F#5", .5), ("B5", 1), ("A#5", 1)],
        [("A#5", 2), ("G#5", 1), ("F#5", 1)],
    ]
    for m in range(mesures):
        a = grille[m % 4]; r, ti, q = accord(a, 3); t = m * 4
        P.notes(1, PIANO, t, melo[m % 4], 85)
        for x in (r, ti, q): P.note(1, CORDES_LENTES, t, 4, x + 12, 60)
        for x in (r, ti, q): P.son(1, t, supersaw(fq(x + 12), 4 * 60 / 160, 1400, .25, .2), .16)
        tt = t
        for x, d in melo[m % 4]:  # le thème, filtré, comme sous l'eau avant le drop
            if x: P.son(1, tt, supersaw(fq(n(x)), d * 60 / 160 * .9, 1800), .22)
            tt += d
        for b in range(4):
            P.son(2, t + b, kick_dur(), .9)
            for k in (1, 2, 3): P.son(2, t + b + k * .25, basse_roulante(fq(r - 12), .09), .7)
        for b in (0, 1.5, 3):  # accords supersaw syncopés
            for x in (r, ti, q): P.son(2, t + b, supersaw(fq(x + 12), .3, 4000), .12)
        for x in (r, q): P.note(2, CHOEUR, t, 4, x + 12, 85)
        tt = t
        for x, d in melo[m % 4]:
            if x: P.son(3, tt, supersaw(fq(n(x)), d * 60 / 160 * .95, 7000), .35); P.son(3, tt, supersaw(fq(n(x) - 12), d * 60 / 160 * .95, 5000), .2)
            tt += d
        for b in (1, 3): P.son(3, t + b, clap(), .5)
        for k in range(8): P.son(3, t + k * .5 + .5 * (k % 1), charley(.05, k % 2 == 1), .18)
        P.notes(3, CORDES, t, [(None if x is None else n(x) + 12, d) for x, d in melo[m % 4]], 90)
        if m % 4 == 0: P.frappe(3, CRASH, t, 120); P.frappe(2, CRASH, t, 90)
        if m % 4 == 3: P.son(2, t, riser(4 * 60 / 160), 1)
    return P


def finale(mesures):
    """Final lumineux qui grandit (esprit « final de jeu vidéo ») : le même thème joué d'abord seul par la boîte
    à musique, puis par les cordes et le chœur, puis par tout l'orchestre avec batterie. La bémol majeur, 100 bpm."""
    P = Partition(100)
    grille = ["Ab", "Fm", "Db", "Eb", "Ab", "Fm", "Db", "Eb"]
    theme = [
        [("C5", 1), ("Eb5", 1), ("Ab5", 1.5), ("G5", .5)],
        [("F5", 1), ("Eb5", 1), ("C5", 2)],
        [("Db5", 1), ("F5", 1), ("Bb5", 1.5), ("Ab5", .5)],
        [("G5", 2), ("Bb5", 1), ("Eb5", 1)],
        [("C6", 1.5), ("Bb5", .5), ("Ab5", 1), ("Eb5", 1)],
        [("F5", 1), ("Ab5", 1), ("C6", 2)],
        [("Db6", 1.5), ("C6", .5), ("Bb5", 1), ("Ab5", 1)],
        [("Bb5", 3), ("Eb5", 1)],
    ]
    for m in range(mesures):
        a = grille[m % 8]; r, ti, q = accord(a, 3); t = m * 4; th = theme[m % 8]
        P.notes(1, CELESTA, t, th, 95)
        for k in range(4): P.note(1, PIANO, t + k, .9, [r, q, r + 12, ti + 12][k], 55)
        P.notes(2, CORDES, t, th, 88)
        for x in (r, ti, q): P.note(2, CORDES_LENTES, t, 4, x, 65)
        P.note(2, VIOLONCELLE, t, 4, r - 12, 85)
        for x in (r + 12, q + 12): P.note(2, CHOEUR, t, 4, x, 72)
        for k in range(8): P.note(2, PIANO, t + k * .5, .45, [r, q, r + 12, q, ti + 12, q, r + 12, q][k], 70)
        P.notes(3, CUIVRES, t, th, 110)
        P.notes(3, CARRE, t, [(n(x) + 12, d) for x, d in th], 60)
        P.note(3, CONTREBASSE, t, 4, r - 24, 105)
        P.note(3, TIMBALES, t, 1, r - 12, 115); P.note(3, TIMBALES, t + 2, 1, q - 24, 100)
        for b in range(4):
            P.frappe(3, GC, t + b, 115 if b % 2 == 0 else 95)
            if b % 2: P.frappe(3, CAISSE, t + b, 112)
            P.frappe(3, RIDE, t + b + .5, 70)
        if m % 4 == 0: P.frappe(3, CRASH, t, 120); P.note(3, HIT, t, 1, r + 12, 110)
    return P


def terre(mesures):
    """Électro-orchestral d'aventure (esprit bande originale d'Assassin's Creed) : arpège de synthé pulsé en
    doubles croches, guitare en ostinato, voix lointaine, cordes graves, tambours qui montent. Ré mineur, 112 bpm."""
    P = Partition(112)
    grille = ["Dm", "Dm", "Bb", "C", "Dm", "Dm", "Gm", "A"]
    voix = [
        [("A4", 3), ("G4", .5), ("F4", .5)], [("E4", 2), ("D4", 2)],
        [("F4", 2), ("Bb4", 2)], [("A4", 2), ("G4", 2)],
        [("A4", 2), ("D5", 1), ("C5", 1)], [("A4", 4)],
        [("Bb4", 2), ("A4", 1), ("G4", 1)], [("A4", 2), ("C#5", 2)],
    ]
    for m in range(mesures):
        a = grille[m % 8]; r, ti, q = accord(a, 3); t = m * 4
        arp = [r, q, r + 12, q, ti + 12, q, r + 12, q + 12]
        for k in range(16): P.son(1, t + k * .25, pulsation(fq(arp[k % 8]), .2, 1800 + 300 * (k % 4 == 0)), .14)
        P.note(1, VIOLONCELLE, t, 4, r - 12, 80)
        for k in range(8): P.note(2, GUITARE, t + k * .5, .45, [r, ti, q, r + 12][k % 4], 85)
        P.notes(2, VOIX_OOH, t, voix[m % 8], 90)
        for x in (r, ti, q): P.note(2, CORDES_LENTES, t, 4, x + 12, 62)
        for b in (0, 1.5, 2.5): P.note(2, TIMBALES, t + b, .5, r - 12, 95)
        P.notes(3, CORDES, t, [(n(x) + 12, d) for x, d in voix[m % 8]], 95)
        P.note(3, CHOEUR, t, 4, r + 12, 85); P.note(3, CHOEUR, t, 4, q + 12, 85)
        P.note(3, CONTREBASSE, t, 4, r - 24, 100)
        for b in range(4): P.frappe(3, TOM_G, t + b, 115); P.frappe(3, GC, t + b, 95 if b % 2 else 112)
        for k in range(4): P.frappe(3, TOM_M, t + 3 + k * .25, 80 + 10 * k)
        for k in range(16): P.son(3, t + k * .25, pulsation(fq(arp[k % 8] + 24), .12, 4000), .07)
        if m % 4 == 0: P.frappe(3, CRASH, t, 115)
    return P


MORCEAUX = {"epopee": epopee, "heritage": heritage, "boss": boss, "bande_annonce": bande_annonce,
            "hardtekk": hardtekk, "finale": finale, "terre": terre}
NIVEAU_COUCHES = {1: (1,), 2: (1, 2), 3: (1, 2, 3)}
GAINS = {1: 1.0, 2: .9, 3: .85}


def stems(style, dur):
    """-> (couches rendues {1, 2, 3: (n, 2)}, durée d'une mesure en s)."""
    f = MORCEAUX[style]
    bpm = f(1).bpm; mesure = 4 * 60 / bpm
    P = f(int(dur / mesure) + 2)
    return P.rendre(dur), mesure


def essai(style, dur=20.0):
    """Extrait qui monte : un tiers par niveau, puis coupe nette sur un accent final."""
    c, mesure = stems(style, dur)
    m = int(dur * SR); y = np.zeros((m, 2), np.float32)
    bornes = [0, round(dur / 3 / mesure) * mesure, round(2 * dur / 3 / mesure) * mesure, dur]
    for niv in (1, 2, 3):
        a, b = int(bornes[niv - 1] * SR), int(bornes[niv] * SR)
        for k in NIVEAU_COUCHES[niv]: y[a:b] += c[k][a:b] * GAINS[k]
    f = int(.02 * SR); y[-f:] *= np.linspace(1, 0, f)[:, None]
    return densifier(y)


def densifier(y, cible=-13.0):
    """Mur de son : niveau RMS visé (dBFS) puis saturation douce qui écrase les crêtes, comme les références."""
    rms = np.sqrt((y ** 2).mean()) + 1e-9
    y = y * 10 ** (cible / 20) / rms
    return (np.tanh(y * 1.3) / np.tanh(1.3) * .95).astype(np.float32)


if __name__ == "__main__":
    style = sys.argv[1]; dur = float(sys.argv[2]) if len(sys.argv) > 2 else 20.0
    y = essai(style, dur); chemin = os.path.join(ICI, "sortie", f"essai-{style}.wav")
    sf.write(chemin, y, SR); print("écrit", chemin)
