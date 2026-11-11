"""Mesure de l'intonation d'un passage de voix (contrôle du « robotisme », demande de Cengiz du 06/11/2026).

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


# ---------------------------------------------------------------------------------------------------------------
# Dérapages de la voix clonée (10/11/2026, Cengiz : « souvent elle vrille, elle prononce mal, elle fait des trucs haut
# et robotique ») : le modèle part parfois dans l'aigu, ou glisse brutalement. On mesure la hauteur par fenêtres de
# 0,25 s et on compare au registre du narrateur (médiane de toute la vidéo, ou du passage à défaut).
def profil(a, sr):
    """Hauteurs médianes (Hz) par fenêtre de 0,25 s, et médiane du passage."""
    import librosa
    if sr != 16000:
        a = librosa.resample(np.asarray(a, dtype=np.float32), orig_sr=sr, target_sr=16000)
        sr = 16000
    f0, voix, _ = librosa.pyin(a, fmin=55, fmax=420, sr=sr, frame_length=1024, hop_length=256)
    ok = voix & np.isfinite(f0)
    t = np.arange(len(f0)) * 256 / sr
    fen = []
    for d in np.arange(0, t[-1] if len(t) else 0, 0.25):
        m = (t >= d) & (t < d + 0.25) & ok
        fen.append(float(np.median(f0[m])) if m.sum() >= 4 else np.nan)
    med = float(np.median(f0[ok])) if ok.sum() > 10 else float("nan")
    return np.array(fen), med


def anomalies(a, sr, registre=None, seuil=1.65, duree=0.5):
    """Liste des dérapages d'un passage : « aigu » (tout le passage trop haut), « vrille » (une montée brusque dans
    l'aigu sur au moins 0,5 s), « saut » (glissements de plus d'une octave entre fenêtres voisines)."""
    fen, med = profil(a, sr)
    ref = registre or med
    res = []
    if not np.isfinite(med) or not ref:
        return res
    if med > ref * 1.22:
        res.append("aigu (%.0f Hz pour %.0f)" % (med, ref))
    haut = np.nan_to_num(fen, nan=0) > max(ref * seuil, 140)
    run = best = 0
    for h in haut:
        run = run + 1 if h else 0
        best = max(best, run)
    if best >= max(2, int(round(duree / 0.25))):
        res.append("vrille (%.2f s dans l'aigu)" % (best * 0.25))
    v = fen[np.isfinite(fen)]
    if len(v) > 3:
        sauts = np.abs(np.diff(12 * np.log2(v)))
        if (sauts > 12).sum() >= 2:
            res.append("saut (%d glissements > 1 octave)" % int((sauts > 12).sum()))
    return res


def mots_aigus(a, sr, mots, registre, seuil=1.3):
    """Mots qui sautent dans l'aigu (11/11/2026, défaut signalé par Cengiz au ch. 5 : « passe », « foyer » à 150 %
    au milieu d'une phrase, « Comment » à 145 %) : hauteur médiane du mot au-delà de 130 % du registre du narrateur.
    mots : [(début, fin, mot)] en secondes. Renvoie [(mot, pourcentage)]."""
    import librosa
    if sr != 16000:
        a = librosa.resample(np.asarray(a, dtype=np.float32), orig_sr=sr, target_sr=16000)
        sr = 16000
    f0, voix, _ = librosa.pyin(a, fmin=55, fmax=420, sr=sr, frame_length=1024, hop_length=160)
    t = np.arange(len(f0)) * 160 / sr
    ok = voix & np.isfinite(f0)
    res = []
    for d, f, w in mots:
        m = (t >= d) & (t < f) & ok
        if f - d >= 0.12 and m.sum() >= 4:
            r = float(np.median(f0[m])) / registre
            if r > seuil:
                res.append((w, round(100 * r)))
    return res
