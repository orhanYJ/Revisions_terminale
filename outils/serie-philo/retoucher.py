#!/usr/bin/env python3
"""Retouche de la voix « vivante » (VOIX_VIVANTE = True), phrase par phrase (11/11/2026).

La voix vivante dit chaque passage phrase par phrase (voix_qwen._dire_phrases). Quelques phrases restent fautives :
un mot isolé qui saute dans l'aigu (« Tous », « Toute », un nombre), défaut signalé par Cengiz (« un mot isolé dans
l'aigu »). Ce script les retrouve dans le cache de l'épisode, refait seulement ces phrases (plus de prises, d'autres
graines : voix_qwen.prise_phrase) et les recolle à leur place, silences compris ; le reste du passage ne bouge pas.
Une phrase n'est remplacée que si la nouvelle prise est moins aiguë que l'ancienne.

Usage : python3 retoucher.py <module> [--seuil 1.38] [--series 3] [--graine 1000] [--essai]
  --graine : à changer pour un second passage (sinon les mêmes prises reviennent) ;
  --seuil : hauteur d'un mot (rapportée au registre du narrateur) à partir de laquelle la phrase est refaite ;
  --essai : liste les phrases fautives sans rien refaire.
Puis relancer generer.py <module> (tout est en cache : il ne fait que remonter la piste).
Ne pas lancer pendant un autre generer.py (mémoire).
"""
import hashlib, json, os, subprocess, sys, tempfile

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import generer as G, prosodie, voix_qwen

SR = 24000


def _passages(ep):
    """[(clé, texte lu, voix, tempo)] comme generer.py (clé de la voix vivante)."""
    G.PRONONCIATION.update(getattr(ep, "PRONONCIATION", {}))
    G.VOIX.clear(); G.VOIX.update(G.VOIX_LANGUE[getattr(ep, "LANGUE", "fr")])
    res = []
    for sc in ep.SCENES:
        for b in G._beats(sc):
            if "pause" in b:
                continue
            lu = G.prononce(G._nettoie(b["t"])[0])
            if not lu.strip():
                continue
            pros = dict(G.PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([G.MOTEUR + "-phrases", G.VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            res.append((cle, lu, G.VOIX[b["v"]], 1 + float(pros["rate"].rstrip("%")) / 100))
    return res


def _charger(chemin):
    import librosa
    a, _ = librosa.load(chemin, sr=SR, mono=True)
    return a.astype(np.float32)


def _tempo(a, sr, tempo):
    if abs(tempo - 1) < 1e-3:
        return a
    import soundfile as sf
    with tempfile.TemporaryDirectory() as d:
        sf.write(os.path.join(d, "a.wav"), a, sr)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(d, "a.wav"), "-af", f"atempo={tempo}",
                        os.path.join(d, "b.wav")], check=True)
        b, _ = sf.read(os.path.join(d, "b.wav"), dtype="float32")
    return b


def _gravite(y16, mots, reg):
    """Hauteur du mot le plus aigu de la phrase, rapportée au registre (2 pour une vrille), et la liste des mots aigus."""
    ag = prosodie.mots_aigus(y16, 16000, mots, reg, seuil=1.0)
    g = max([r / 100 for _, r in ag], default=0.0)
    if prosodie.anomalies(y16, 16000, reg, seuil=1.35, duree=0.5):
        g = max(g, 2.0)
    return g, ag


def main(module, seuil=1.38, series=3, essai=False, graine=1000):
    import importlib, librosa
    ep = importlib.import_module(module)
    langue = getattr(ep, "LANGUE", "fr")
    if not getattr(ep, "VOIX_VIVANTE", False):
        sys.exit("retoucher.py ne sert qu'aux épisodes en voix vivante (VOIX_VIVANTE = True)")
    total = refaites = 0
    for cle, lu, voix, tempo in _passages(ep):
        chemin = os.path.join(G.CACHE, cle + ".mp3")
        if voix not in voix_qwen.REF or not os.path.exists(chemin) or not os.path.exists(chemin + ".json"):
            continue
        reg = voix_qwen.registre(voix)
        mots = json.load(open(chemin + ".json", encoding="utf-8"))
        phrases = voix_qwen._decouper(lu)
        tailles = [len(voix_qwen._mots_du_texte(ph)) for ph in phrases]
        if sum(tailles) != len(mots):
            print(f"  (découpe incertaine, passage ignoré) {lu[:60]}", flush=True)
            continue
        a = _charger(chemin)
        y16 = librosa.resample(a, orig_sr=SR, target_sr=16000)
        # bornes de chaque phrase : du premier au dernier mot ; coupes au milieu des silences entre phrases
        bornes, j = [], 0
        for n in tailles:
            bornes.append((mots[j][0], mots[j + n - 1][0] + mots[j + n - 1][1], j, j + n))
            j += n
        coupes = [0.0] + [(bornes[k][1] + bornes[k + 1][0]) / 2 for k in range(len(bornes) - 1)] + [len(a) / SR]
        nouveaux = {}
        for k, (ph, (t0, t1, j0, j1)) in enumerate(zip(phrases, bornes)):
            total += 1
            g, ag = _gravite(y16[int(coupes[k] * 16000):int(coupes[k + 1] * 16000)],
                             [(m[0] - coupes[k], m[0] + m[1] - coupes[k], m[2]) for m in mots[j0:j1]], reg)
            if g < seuil:
                continue
            print(f"✗ {g:.2f} {', '.join('%s %d %%' % x for x in ag if x[1] >= 100 * seuil) or 'vrille'} · {ph[:70]}", flush=True)
            if essai:
                continue
            b, sr, _, sc, an, gn = voix_qwen.prise_phrase(ph, voix, langue, i=k, series=series, graine=graine)
            if sr != SR:
                b = librosa.resample(b, orig_sr=sr, target_sr=SR)
            b = _tempo(b, SR, tempo)
            if gn < g and sc >= 0.8:
                nouveaux[k] = (t0 - coupes[k], b, coupes[k + 1] - t1)
                refaites += 1
                print(f"    → refaite ({gn:.2f}{', ' + ', '.join(an) if an else ''})", flush=True)
            else:
                print(f"    → gardée (nouvelle prise {gn:.2f}, score {sc:.2f})", flush=True)
        if not nouveaux:
            continue
        morceaux = []
        for k in range(len(phrases)):
            if k in nouveaux:
                avant, b, apres = nouveaux[k]
                morceaux += [np.zeros(int(max(0.0, avant - 0.04) * SR), np.float32), b,
                             np.zeros(int(max(0.0, apres - 0.06) * SR), np.float32)]
            else:
                morceaux.append(a[int(coupes[k] * SR):int(coupes[k + 1] * SR)])
        a2 = np.concatenate(morceaux)
        voix_qwen._charger()
        y2 = librosa.resample(a2, orig_sr=SR, target_sr=16000)
        segs, _ = voix_qwen._whisper.transcribe(y2, language=langue, word_timestamps=True)
        mw = [(x.start, x.end - x.start, x.word.strip()) for s in segs for x in (s.words or [])]
        sc = voix_qwen._score(lu, " ".join(w for _, _, w in mw))
        voix_qwen._ecrire(lu, chemin, 1.0, a2, SR, mw, sc)
        print(f"  passage réécrit (score {sc:.2f}) : {lu[:60]}", flush=True)
    print(f"{ep.CODE} : {total} phrases contrôlées, {refaites} refaites", flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    def opt(nom, defaut):
        return type(defaut)(args[args.index(nom) + 1]) if nom in args else defaut
    main(args[0], seuil=opt("--seuil", 1.38), series=opt("--series", 3), essai="--essai" in args,
         graine=opt("--graine", 1000))
