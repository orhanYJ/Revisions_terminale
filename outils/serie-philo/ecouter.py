"""Réécoute des passages enregistrés par transcription (faster-whisper), pour vérifier les passages « À VÉRIFIER ».

Usage (depuis la racine du dépôt) :
    python3 outils/serie-philo/ecouter.py pc_ch4 "Faisons un premier" "Question deux"
Chaque argument après le module est le début d'un passage lu ; le script affiche le texte et ce qui a été entendu.
Le score de generer.py baisse dès qu'un passage contient des nombres (la transcription les écrit en chiffres, le texte
en lettres) : un passage signalé est le plus souvent bien dit. Un nombre réellement mal dit se corrige en reformulant
légèrement la phrase dans le script (nouvelle prise, le cache garde les autres passages).
"""
import hashlib, json, os, subprocess, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(1, os.path.join(os.path.dirname(ICI), "serie-pc"))
sys.path.insert(2, os.path.join(os.path.dirname(ICI), "serie-svt"))
os.environ.setdefault("SERIE_MOTEUR", "qwen")
import generer as G  # noqa: E402


def ecouter(module, cibles):
    import importlib
    from faster_whisper import WhisperModel
    ep = importlib.import_module(module)
    G.PRONONCIATION.update(getattr(ep, "PRONONCIATION", {}))
    w = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=1)
    for sc in ep.SCENES:
        for b in G._beats(sc):
            if "pause" in b:
                continue
            lu, _ = G._nettoie(b["t"])
            lu = G.prononce(lu)
            if cibles and not any(lu.startswith(c) for c in cibles):
                continue
            pros = dict(G.PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([G.MOTEUR, G.VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            f = os.path.join(G.CACHE, cle + ".mp3")
            if not os.path.exists(f):
                print("ABSENT :", lu[:70])
                continue
            # décodage par ffmpeg (la version d'av installée ne convient pas toujours à faster-whisper)
            raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                                 capture_output=True).stdout
            segs, _ = w.transcribe(np.frombuffer(raw, dtype=np.float32), language="fr")
            print("TEXTE   :", lu)
            print("ENTENDU :", " ".join(s.text.strip() for s in segs))
            print()


if __name__ == "__main__":
    ecouter(sys.argv[1], sys.argv[2:])
