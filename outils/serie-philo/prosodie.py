"""Mesure de l'intonation d'un passage de voix (contrôle du « robotisme », demande du responsable du projet du 06/11/2026).

Trois indicateurs, calculés sur l'audio :
- relief : écart-type de la hauteur (F0) en demi-tons sur les trames voisées — une voix plate, monocorde, est sous ~2 ;
- élan : écart-type, en demi-tons, des hauteurs moyennes par fenêtre de 1,5 s — la mélodie de phrase (montées, retombées) ;
- débit : syllabes approchées par seconde de parole (pics d'énergie), pour repérer un débit mécanique trop régulier ou trop rapide.
Usage en module : mesure(audio, sr) -> dict ; en ligne de commande : python3 prosodie.py <code ou fichiers…>
liste les passages les plus plats d'un épisode (d'après les MP3 du cache de la voix).
"""
import json, os, sys

import numpy as np

SEUIL_RELIEF = 2.3   # demi-tons : en dessous, le passage sonne plat (calibré sur les épisodes H3, 06/11/2026 : médiane 2,6 ; voix de référence 2,9)
SEUIL_ELAN = 1.2     # demi-tons (médiane 1,5 ; référence 2,5)


def mesure(a, sr):
    import librosa
    if sr != 16000:
        a = librosa.resample(np.asarray(a, dtype=np.float32), orig_sr=sr, target_sr=16000)
        sr = 16000
    f0, voix, _ = librosa.pyin(a, fmin=55, fmax=300, sr=sr, frame_length=1024, hop_length=256)
    f = f0[voix & np.isfinite(f0)] if f0 is not None else np.array([])
    if len(f) < 20:
        return {"relief": 0.0, "elan": 0.0, "debit": 0.0, "voise": 0.0}
    st = 12 * np.log2(f / np.median(f))
    relief = float(np.std(st))
    # mélodie de phrase : moyenne par fenêtres de 1,5 s
    t = np.arange(len(f0)) * 256 / sr
    blocs = []
    for d in np.arange(0, t[-1], 1.5):
        m = (t >= d) & (t < d + 1.5) & voix & np.isfinite(f0)
        if m.sum() > 5:
            blocs.append(12 * np.log2(np.median(f0[m]) / np.median(f)))
    elan = float(np.std(blocs)) if len(blocs) > 2 else relief
    env = librosa.feature.rms(y=a, frame_length=512, hop_length=160)[0]
    pics = librosa.util.peak_pick(env, pre_max=6, post_max=6, pre_avg=10, post_avg=10, delta=float(np.max(env)) * 0.04, wait=8)
    parole = float((env > np.max(env) * 0.05).sum() * 160 / sr) or 1.0
    return {"relief": round(relief, 2), "elan": round(elan, 2), "debit": round(len(pics) / parole, 2), "voise": round(float(voix.mean()), 2)}


def plat(m):
    return m["relief"] < SEUIL_RELIEF or m["elan"] < SEUIL_ELAN


if __name__ == "__main__":
    import librosa
    fichiers = [x for x in sys.argv[1:] if os.path.exists(x)]
    res = []
    for p in fichiers:
        a, sr = librosa.load(p, sr=16000, mono=True)
        m = mesure(a, sr)
        res.append((p, m))
        print(("PLAT " if plat(m) else "     ") + os.path.basename(p), json.dumps(m), flush=True)
    if res:
        r = np.array([m["relief"] for _, m in res]); e = np.array([m["elan"] for _, m in res])
        print(f"{len(res)} passages : relief médian {np.median(r):.2f} (p10 {np.percentile(r, 10):.2f}), élan médian {np.median(e):.2f} (p10 {np.percentile(e, 10):.2f}), plats {sum(plat(m) for _, m in res)}")
