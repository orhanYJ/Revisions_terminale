#!/usr/bin/env python3
"""Audit de la voix d'un épisode, passage par passage, dans le cache (10/11/2026, Cengiz : « souvent elle vrille,
elle prononce mal, elle fait des trucs haut et robotique »).

Pour chaque passage du script : reconnaissance vocale (justesse, nombres remis en lettres), hauteur par fenêtres de
0,25 s (voix partie dans l'aigu, vrille, glissements : prosodie.anomalies), intonation (prosodie.plat).
Usage : python3 audit_voix.py <module> [--supprimer]
--supprimer efface du cache les passages fautifs : generer.py les réenregistrera (jusqu'à six prises, la meilleure gardée).
"""
import json, os, re, subprocess, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import generer as G, prosodie, voix_qwen, recuperer

SEUIL_SCORE = 0.86
SEUIL_MOT = 0.6          # confiance de la reconnaissance sous laquelle un mot est jugé mal articulé
SEUIL_AIGU, DUREE_AIGU = 1.35, 0.5   # montée au-delà de 135 % du registre pendant au moins 0,5 s


def main(module, supprimer=False):
    import importlib, librosa
    from faster_whisper import WhisperModel
    ep = importlib.import_module(module)
    langue = getattr(ep, "LANGUE", "fr")
    wh = WhisperModel("small", device="cpu", compute_type="int8")
    regs = {}
    fautifs, vus = [], 0
    for cle, lu, v, orig in recuperer.passages(ep):
        chemin = os.path.join(G.CACHE, cle + ".mp3")
        if not os.path.exists(chemin):
            continue
        vus += 1
        voix = G.VOIX[v]
        if voix not in regs:
            regs[voix] = voix_qwen.registre(voix) if voix in voix_qwen.REF else None
        y, _ = librosa.load(chemin, sr=16000, mono=True)
        segs, _ = wh.transcribe(y, language=langue, word_timestamps=True)
        segs = list(segs)
        mots = [w for s_ in segs for w in (s_.words or [])]
        sc = voix_qwen._score(lu, " ".join(s.text for s in segs))
        lp = min([s.avg_logprob for s in segs], default=0)
        an = prosodie.anomalies(y, 16000, regs[voix], seuil=SEUIL_AIGU, duree=DUREE_AIGU)
        pm = prosodie.mesure(y, 16000)
        motifs = list(an)
        # mot par mot : syllabes déformées (reconnaissance très incertaine) ou mot étiré
        # calé le 10/11/2026 sur deux défauts signalés par Cengiz (ch5 2:28 « foyer objet », 11:43 « Comment mesurer… ») :
        # une syllabe mal articulée donne une confiance de 0,5 à 0,6 ; une montée aiguë dure environ 0,5 s à 145 %
        incertains = [w.word.strip() for w in mots if w.probability < SEUIL_MOT and len(re.sub(r"[^\w]", "", w.word)) > 2
                      and not re.search(r"\d", w.word)]
        if len(incertains) >= 1:
            motifs.append("mots déformés (%s)" % ", ".join(incertains[:4]))
        etires = [w.word.strip() for w in mots if (w.end - w.start) > 1.3 and len(w.word.strip()) < 12]
        if etires:
            motifs.append("mot étiré (%s)" % ", ".join(etires[:3]))
        if sc < SEUIL_SCORE:
            motifs.append("mal dit (reconnaissance %.2f)" % sc)
        if lp < -0.9:
            motifs.append("élocution confuse (logprob %.2f)" % lp)
        if prosodie.plat(pm):
            motifs.append("monocorde (relief %.1f, élan %.1f)" % (pm["relief"], pm["elan"]))
        if motifs:
            fautifs.append((cle, lu, motifs))
            print("✗ %s · %s · %s" % (cle, " ; ".join(motifs), lu[:70]), flush=True)
            if supprimer:
                for ext in ("", ".json", ".vu", ".wav"):
                    if os.path.exists(chemin + ext if ext != ".wav" else chemin[:-4] + ".wav"):
                        os.remove(chemin + ext if ext != ".wav" else chemin[:-4] + ".wav")
        else:
            open(chemin + ".vu", "w").close()
    print("%s : %d passages contrôlés, %d fautifs%s" % (ep.CODE, vus, len(fautifs), " (effacés du cache)" if supprimer else ""), flush=True)


if __name__ == "__main__":
    main(sys.argv[1], "--supprimer" in sys.argv)
