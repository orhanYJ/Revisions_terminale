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


# --- Défauts de voix (demande de Cengiz du 10/11/2026 : « souvent elle vrille, elle prononce mal, elle fait des trucs
# haut et robotique ») : mesures complémentaires, comparées à la voix de référence du passage.
_REF_HZ = {}


def ref_hz(chemin_wav):
    """Hauteur médiane (Hz) de la voix de référence (voix_ref/*.wav)."""
    if chemin_wav not in _REF_HZ:
        import librosa
        a, sr = librosa.load(chemin_wav, sr=16000, mono=True)
        f0, v, _ = librosa.pyin(a, fmin=50, fmax=500, sr=sr, frame_length=1024, hop_length=256)
        _REF_HZ[chemin_wav] = float(np.median(f0[v & np.isfinite(f0)]))
    return _REF_HZ[chemin_wav]


def defauts(a, sr, ref, mots=None, nb_car=None):
    """Mesures de défaut d'un passage (a : audio mono, ref : hauteur médiane de la voix de référence en Hz,
    mots : [(début, durée, mot)] reconnus, nb_car : longueur du texte lu). Renvoie un dict de mesures."""
    import librosa
    if sr != 16000:
        a = librosa.resample(np.asarray(a, dtype=np.float32), orig_sr=sr, target_sr=16000)
        sr = 16000
    a = np.asarray(a, dtype=np.float32)
    f0, v, _ = librosa.pyin(a, fmin=50, fmax=500, sr=sr, frame_length=1024, hop_length=256)
    ok = v & np.isfinite(f0)
    r = {"duree": round(len(a) / sr, 2)}
    if ok.sum() < 20:
        r.update(hauteur=0.0, aigu=0.0, sauts=0.0, voise=0.0)
    else:
        st = 12 * np.log2(f0[ok] / ref)
        r["hauteur"] = round(float(np.median(st)), 2)              # demi-tons au-dessus de la référence
        r["aigu"] = round(float((st > 9).mean()), 3)               # part de la voix à plus de 9 demi-tons au-dessus
        # sauts brusques de hauteur à l'intérieur d'une même émission (trames voisées consécutives) ; les erreurs
        # d'octave de pyin donnent ±12 : on ne compte que les sauts de 4 à 10 demi-tons
        s = 12 * np.log2(f0[1:] / f0[:-1])
        cons = ok[1:] & ok[:-1]
        d = np.abs(s[cons])
        r["sauts"] = round(float(((d > 4) & (d < 10)).sum()) / max(1.0, cons.sum() * 256 / sr), 2)  # par seconde voisée
        r["voise"] = round(float(ok.mean()), 2)
        # hauteur qui « décroche » de la ligne mélodique : écart à la médiane glissante (0,25 s) dans chaque émission
        hors, n = 0, 0
        stf = np.where(ok, 12 * np.log2(np.where(ok, f0, ref) / ref), np.nan)
        i = 0
        while i < len(stf):
            if np.isnan(stf[i]):
                i += 1
                continue
            j = i
            while j < len(stf) and not np.isnan(stf[j]):
                j += 1
            run = stf[i:j]
            if len(run) >= 8:
                from scipy.ndimage import median_filter
                m = median_filter(run, size=15, mode="nearest")
                e = np.abs(run - m)
                hors += int(((e > 3) & (e < 10)).sum()); n += len(run)
            i = j
        r["decroche"] = round(hors / max(1, n), 3)
    if mots:
        fin = max(o + du for o, du, _ in mots)
        deb = min(o for o, _, _ in mots)
        # parole active (énergie) après le dernier mot reconnu : bafouillage ou bruit en fin de passage
        env = librosa.feature.rms(y=a, frame_length=512, hop_length=160)[0]
        act = env > max(1e-4, float(np.max(env)) * 0.08)
        t = np.arange(len(env)) * 160 / sr
        r["queue"] = round(float(act[t > fin + 0.25].sum() * 160 / sr), 2)
        r["tete"] = round(float(act[t < deb - 0.25].sum() * 160 / sr), 2)
        if nb_car:
            r["debit"] = round(nb_car / max(0.5, fin - deb), 1)    # caractères lus par seconde de parole
    return r


SEUILS = {"hauteur": 4.0, "aigu": 0.08, "sauts": 2.5, "decroche": 0.05, "queue": 0.6, "tete": 0.6, "debit": (9.0, 21.0)}


def suspect(d):
    """Liste des défauts franchis (vide si le passage est propre)."""
    out = []
    if d.get("hauteur", 0) > SEUILS["hauteur"]:
        out.append(f"voix haute (+{d['hauteur']} demi-tons)")
    if d.get("aigu", 0) > SEUILS["aigu"]:
        out.append(f"montées aiguës ({round(100 * d['aigu'])} %)")
    if d.get("sauts", 0) > SEUILS["sauts"]:
        out.append(f"hauteur qui vrille ({d['sauts']} sauts/s)")
    if d.get("decroche", 0) > SEUILS["decroche"]:
        out.append(f"hauteur qui décroche ({round(100 * d['decroche'])} % de la voix)")
    if d.get("queue", 0) > SEUILS["queue"]:
        out.append(f"son après le dernier mot ({d['queue']} s)")
    if d.get("tete", 0) > SEUILS["tete"]:
        out.append(f"son avant le premier mot ({d['tete']} s)")
    if "debit" in d and not (SEUILS["debit"][0] <= d["debit"] <= SEUILS["debit"][1]):
        out.append(f"débit anormal ({d['debit']} car/s)")
    return out
