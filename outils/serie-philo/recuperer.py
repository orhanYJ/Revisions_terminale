"""Reconstitue le cache de voix d'un épisode déjà publié, à partir de sa piste de voix publiée (voix/<code>-v-*.mp3).

Utile quand le cache .cache/ a été perdu (conteneur neuf) : au lieu de réenregistrer tout l'épisode (des heures avec Qwen),
on découpe la piste publiée passage par passage (bornes tirées des sous-titres), on retrouve l'instant des mots par la
reconnaissance vocale, et on range chaque passage sous sa clé de cache. Seuls les passages dont le texte n'a pas changé
depuis la publication sont récupérés ; les autres seront enregistrés par generer.py. Ensuite, SERIE_REVOIX=1 refait les
passages monocordes.

Usage : python3 recuperer.py <module>     (ex. h3_1 ; le script publié est relu dans git, au commit des données publiées)
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
RACINE = os.path.dirname(os.path.dirname(ICI))
import generer as G


def _norm(s):
    return re.sub(r"[^0-9a-zàâäçéèêëîïôöûùüœæ]", "", s.lower())


def passages(ep):
    """[(clé, texte lu, voix)] dans l'ordre de l'épisode, comme generer.py."""
    G.PRONONCIATION.clear(); G.PRONONCIATION.update({"Leute": "Loïte", "liberi": "libéri"})
    G.PRONONCIATION.update(getattr(ep, "PRONONCIATION", {}))
    G.VOIX.clear(); G.VOIX.update(G.VOIX_LANGUE[getattr(ep, "LANGUE", "fr")])
    res = []
    for sc in ep.SCENES:
        for b in G._beats(sc):
            if "pause" in b:
                continue
            lu, _ = G._nettoie(b["t"])
            orig = lu
            lu = G.prononce(lu)
            if not lu.strip():
                continue
            pros = dict(G.PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([G.MOTEUR, G.VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            res.append((cle, lu, b["v"], orig))
    return res


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(module):
    nouveau = importlib.import_module(module)
    site, code = getattr(nouveau, "SITE", "philo"), nouveau.CODE
    data = os.path.join(RACINE, site, "serie", f"{code}.data.js")
    rel = os.path.relpath(data, RACINE)
    commit = subprocess.run(["git", "-C", RACINE, "log", "-1", "--format=%H", "--", rel], capture_output=True, text=True).stdout.strip()
    src = os.path.relpath(nouveau.__file__, RACINE)
    ancien_txt = subprocess.run(["git", "-C", RACINE, "show", f"{commit}:{src}"], capture_output=True, text=True, check=True).stdout
    d = tempfile.mkdtemp()
    open(os.path.join(d, "ancien.py"), "w", encoding="utf-8").write(ancien_txt)
    sys.path.insert(0, os.path.dirname(nouveau.__file__))
    ancien = charger(os.path.join(d, "ancien.py"), module + "_publie")
    vieux, neufs = passages(ancien), passages(nouveau)
    cles_neuves = {c[0] for c in neufs}
    s = open(data, encoding="utf-8").read()
    ep = json.loads(s[s.index("{"):s.rindex("}") + 1])
    sous = ep["sous"]
    piste = os.path.join(RACINE, site, "serie", ep["audio"]["voix"])
    # regroupe les sous-titres par passage (texte normalisé)
    import difflib
    k, bornes = 0, []
    for cle, lu, v, orig in vieux:
        cible = _norm(orig)
        meilleur = (0, 0)
        for n in range(1, 40):
            if k + n > len(sous):
                break
            acc = "".join(_norm(x[2]) for x in sous[k:k + n])
            r = difflib.SequenceMatcher(None, cible, acc, autojunk=False).ratio()
            if r > meilleur[0]:
                meilleur = (r, n)
        r, n = meilleur
        if r >= 0.9:
            bornes.append((cle, lu, v, sous[k][0], sous[k + n - 1][1], True))
            k += n
        else:
            bornes.append((cle, lu, v, None, None, False))
    print("appariés :", sum(1 for b in bornes if b[5]), "/", len(bornes), flush=True)
    if os.environ.get("ESSAI"):
        for b in bornes:
            if not b[5]: print("   ✗", b[3], b[4], b[1][:70])
        return
    a_prendre = [b for b in bornes if b[0] in cles_neuves and not os.path.exists(os.path.join(G.CACHE, b[0] + ".mp3"))]
    print(f"{code} : {len(vieux)} passages publiés, {sum(1 for b in bornes if b[0] in cles_neuves)} inchangés, "
          f"{len(a_prendre)} à récupérer, {len(neufs) - len(cles_neuves & {b[0] for b in bornes})} nouveaux ou modifiés", flush=True)
    if not a_prendre:
        return
    from faster_whisper import WhisperModel
    import voix_qwen
    wh = WhisperModel("small", device="cpu", compute_type="int8")
    os.makedirs(G.CACHE, exist_ok=True)
    langue = getattr(nouveau, "LANGUE", "fr")
    pris = 0
    for i, (cle, lu, v, t0, t1, ok) in enumerate(bornes):
        if cle not in cles_neuves or os.path.exists(os.path.join(G.CACHE, cle + ".mp3")):
            continue
        if not ok:
            print(f"  sous-titres non appariés, laissé à generer.py : {lu[:60]}", flush=True)
            continue
        # bornes : du début du premier sous-titre (un peu avant) à la fin du dernier, sans mordre sur les voisins
        av = bornes[i - 1][4] if i > 0 and bornes[i - 1][4] else 0
        ap = bornes[i + 1][3] if i + 1 < len(bornes) and bornes[i + 1][3] else t1 + 0.5
        a, b = max(t0 - 0.25, (av + t0) / 2), min(t1 + 0.15, (t1 + ap) / 2 if ap > t1 else t1 + 0.15)
        chemin = os.path.join(G.CACHE, cle + ".mp3")
        wav = chemin[:-4] + ".rec.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", piste, "-ac", "1", "-ar", "16000", wav], check=True)
        import soundfile as sf
        y, sr = sf.read(wav, dtype="float32")
        segs, _ = wh.transcribe(y, language=langue, word_timestamps=True)
        mots = [(x.start, x.end - x.start, x.word.strip()) for sg in segs for x in (sg.words or [])]
        sc = voix_qwen._score(lu, " ".join(m[2] for m in mots))
        if sc < 0.85:
            print(f"  reconnaissance {sc:.2f}, laissé à generer.py : {lu[:60]}", flush=True)
            os.remove(wav)
            continue
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-ac", "1", "-b:a", "96k", chemin + ".part.mp3"], check=True)
        os.remove(wav)
        with open(chemin + ".json", "w", encoding="utf-8") as f:
            json.dump(voix_qwen._caler(lu, mots, len(y) / sr), f, ensure_ascii=False)
        os.replace(chemin + ".part.mp3", chemin)
        pris += 1
        print(f"  {pris} récupéré ({sc:.2f}) : {lu[:60]}", flush=True)
    print(f"{code} : {pris} passages récupérés", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
