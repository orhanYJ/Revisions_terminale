"""Voix de la série par clonage local (Qwen3-TTS, modèle Base, licence Apache 2.0, gratuit et sans limite).

Chaque voix part d'un court enregistrement de référence (voix_ref/*.wav, voix de synthèse créées pour la série,
choisies par Cengiz le 30/10/2026) : le timbre reste exactement le même d'un passage et d'un épisode à l'autre.
Le modèle ne donne pas l'instant des mots : la reconnaissance vocale (faster-whisper) les retrouve, puis on les
recale sur le texte lu. Un passage mal dit (transcription trop éloignée du texte) est refait avec une autre graine.

Écrit, pour chaque passage, <chemin>.mp3 et <chemin>.json : [[début, durée, mot du texte], …], le même format que
les voix edge-tts, pour que generer.py n'ait rien d'autre à changer.
Lent sur processeur (environ 10 s de calcul par seconde de voix) : prévoir 2 h pour un épisode de 12 min.
"""
import difflib, json, os, re, subprocess

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
REF = {
    "narrateur": (os.path.join(ICI, "voix_ref", "narrateur.wav"),
                  "Imagine une pierre qu'on lance en l'air. Si elle pouvait penser, elle croirait voler parce qu'elle "
                  "l'a décidé ! Et nous… sommes-nous vraiment différents de cette pierre ?"),
    "citations": (os.path.join(ICI, "voix_ref", "citations.wav"),
                  "Imagine une pierre qu'on lance en l'air. Si elle pouvait penser, elle croirait voler parce qu'elle "
                  "l'a décidé ! Et nous… sommes-nous vraiment différents de cette pierre ?"),
}
_modele, _prompts, _whisper = None, {}, None


def _charger():
    global _modele, _whisper
    if _modele is None:
        import torch
        from qwen_tts import Qwen3TTSModel
        from faster_whisper import WhisperModel
        torch.set_num_threads(os.cpu_count() or 4)
        _modele = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base", device_map="cpu", dtype=torch.float32)
        _whisper = WhisperModel("small", device="cpu", compute_type="int8")
    return _modele


def _prompt(voix):
    if voix not in _prompts:
        wav, txt = REF[voix]
        _prompts[voix] = _charger().create_voice_clone_prompt(ref_audio=wav, ref_text=txt)
    return _prompts[voix]


def _norm(m):
    return re.sub(r"[^0-9a-zàâäçéèêëîïôöûùüœæ]", "", m.lower())


def _mots_du_texte(lu):
    return [(mm.start(), mm.group(0)) for mm in re.finditer(r"[\wÀ-ÿœæ'’-]+", lu)]


def _caler(lu, mots_w, duree):
    """Associe à chaque mot du texte un instant, d'après les mots reconnus (appariement, puis interpolation)."""
    mt = _mots_du_texte(lu)
    a = [_norm(w) for _, w in mt]
    b = [_norm(w[2]) for w in mots_w]
    t = [None] * len(mt)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            t[blk.a + k] = (mots_w[blk.b + k][0], mots_w[blk.b + k][1])
    # interpolation des mots non reconnus entre leurs voisins
    connus = [i for i, x in enumerate(t) if x]
    for i in range(len(t)):
        if t[i]:
            continue
        av = max([j for j in connus if j < i], default=None)
        ap = min([j for j in connus if j > i], default=None)
        d0 = t[av][0] + t[av][1] if av is not None else 0.0
        d1 = t[ap][0] if ap is not None else duree
        n = (ap if ap is not None else len(t)) - (av if av is not None else -1)
        k = i - (av if av is not None else -1)
        t[i] = (d0 + (d1 - d0) * (k - 1) / n, (d1 - d0) / n)
    return [[round(x[0], 3), round(max(0.05, x[1]), 3), w] for x, (_, w) in zip(t, mt)]


def _score(lu, texte_reconnu):
    """Ressemblance lettre à lettre (la découpe en mots de la reconnaissance diffère parfois : « l' » + « intelligence »)."""
    return difflib.SequenceMatcher(None, _norm(lu), _norm(texte_reconnu), autojunk=False).ratio()


def dire(texte, voix, chemin, tempo=1.0):
    """Enregistre un passage ; renvoie le score de reconnaissance obtenu."""
    import torch
    import soundfile as sf
    m = _charger()
    p = _prompt(voix)
    meilleur = None
    for essai in range(3):
        torch.manual_seed(1234 + 17 * essai + len(texte))
        w, sr = m.generate_voice_clone(text=texte, language="French", voice_clone_prompt=p)
        a = w[0].astype(np.float32)
        y = np.interp(np.arange(0, len(a), sr / 16000), np.arange(len(a)), a).astype(np.float32)
        segs, _ = _whisper.transcribe(y, language="fr", word_timestamps=True)
        mots = [(x.start, x.end - x.start, x.word.strip()) for s in segs for x in (s.words or [])]
        sc = _score(texte, " ".join(x[2] for x in mots))
        if meilleur is None or sc > meilleur[0]:
            meilleur = (sc, a, sr, mots)
        if sc >= 0.9:
            break
    sc, a, sr, mots = meilleur
    tmp = chemin + ".wav.part"
    sf.write(tmp, a, sr, format="WAV")
    filtre = ["-af", f"atempo={tempo}"] if abs(tempo - 1) > 1e-3 else []
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp] + filtre + ["-ac", "1", "-b:a", "96k", chemin + ".part.mp3"], check=True)
    os.remove(tmp)
    # la reconnaissance place souvent le premier mot à 0 s : on le ramène au vrai début de la parole
    idx = np.where(np.abs(a) > 0.004)[0]
    debut = idx[0] / sr if len(idx) else 0.0
    mots = [(max(o, debut) / tempo, d / tempo, w) for o, d, w in mots]
    with open(chemin + ".json", "w", encoding="utf-8") as f:
        json.dump(_caler(texte, mots, len(a) / sr / tempo), f, ensure_ascii=False)
    os.replace(chemin + ".part.mp3", chemin)
    return sc
