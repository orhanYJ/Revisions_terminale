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
    # voix anglaises (04/11/2026), créées par description (Qwen3-TTS VoiceDesign) pour Dancing at Lughnasa
    "narrateur_en": (os.path.join(ICI, "voix_ref", "narrateur_en.wav"),
                     "Picture a kitchen in Donegal, in the summer of nineteen thirty-six. Five sisters, a wireless that "
                     "crackles, and a memory that refuses to stay still. Let's look closely at how it all begins."),
    "cit_en_m": (os.path.join(ICI, "voix_ref", "cit_en_m.wav"),
                 "When I cast my mind back to that summer, different kinds of memories offer themselves to me."),
    "cit_en_f": (os.path.join(ICI, "voix_ref", "cit_en_f.wav"),
                 "Do you want the whole countryside to be laughing at us? Women of our years, mature women, dancing?"),
}
LANGUES = {"fr": "French", "en": "English"}
_modele, _prompts, _whisper = None, {}, None


def _charger():
    global _modele, _whisper
    if _modele is None:
        import torch
        from qwen_tts import Qwen3TTSModel
        from faster_whisper import WhisperModel
        torch.set_num_threads(os.cpu_count() or 4)
        # Hugging Face répond parfois 429 (trop de requêtes) au chargement : on patiente et on réessaie
        # (le mode hors ligne ne marche pas : qwen_tts interroge l'API même quand le modèle est en cache)
        import time
        for essai in range(8):
            try:
                _modele = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base", device_map="cpu", dtype=torch.float32)
                break
            except Exception as err:
                if essai == 7 or "429" not in str(err):
                    raise
                print(f"Hugging Face 429, nouvel essai dans {60 * (essai + 1)} s", flush=True)
                time.sleep(60 * (essai + 1))
        local = os.path.isdir(os.path.expanduser("~/.cache/huggingface/hub/models--Systran--faster-whisper-small"))
        _whisper = WhisperModel("small", device="cpu", compute_type="int8", local_files_only=local)
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


def dire(texte, voix, chemin, tempo=1.0, langue="fr"):
    """Enregistre un passage ; renvoie le score de reconnaissance obtenu."""
    import torch
    import soundfile as sf
    m = _charger()
    p = _prompt(voix)
    # Chaque prise est jugée sur deux plans : la justesse (reconnaissance vocale) et l'intonation (prosodie.py :
    # une prise monocorde est refaite, demande de Cengiz du 06/11/2026 : « une voix naturelle, des intonations,
    # moins de robotisme »). On garde la prise juste la plus vivante ; au plus quatre prises.
    import prosodie
    # Défauts de voix (10/11/2026, Cengiz : « souvent elle vrille, elle prononce mal, elle fait des trucs haut et
    # robotique ») : une prise trop haute, qui décroche, qui bafouille après le dernier mot ou au débit anormal passe
    # après toutes les prises propres, et on tente jusqu'à six prises tant qu'aucune n'est propre. Un passage écarté
    # par controle_voix.py --rejeter repart avec d'autres graines (nombre de rejets déjà faits).
    ref = prosodie.ref_hz(REF[voix][0])
    rejets = os.path.join(os.path.dirname(chemin), "rejets")
    decal = len([x for x in os.listdir(rejets) if x.startswith(os.path.basename(chemin)) and x.endswith(".mp3")]) if os.path.isdir(rejets) else 0
    meilleur = None
    for essai in range(6):
        if essai >= 4 and meilleur is not None and meilleur[0][0]:
            break
        torch.manual_seed(1234 + 17 * (essai + 6 * decal) + len(texte))
        w, sr = m.generate_voice_clone(text=texte, language=LANGUES[langue], voice_clone_prompt=p)
        a = w[0].astype(np.float32)
        y = np.interp(np.arange(0, len(a), sr / 16000), np.arange(len(a)), a).astype(np.float32)
        segs, _ = _whisper.transcribe(y, language=langue, word_timestamps=True)
        mots = [(x.start, x.end - x.start, x.word.strip()) for s in segs for x in (s.words or [])]
        sc = _score(texte, " ".join(x[2] for x in mots))
        try:
            pm = prosodie.mesure(y, 16000)
        except Exception:
            pm = {"relief": 3.0, "elan": 2.0}
        vie = pm["relief"] + pm["elan"]
        try:
            df = prosodie.suspect(prosodie.defauts(y, 16000, ref, mots, len(texte)))
        except Exception:
            df = []
        # rang : d'abord une prise sans défaut, puis la justesse (au-dessus de 0,88 toutes les prises se valent), puis l'intonation
        rang = (not df, min(sc, 0.88), vie)
        if meilleur is None or rang > meilleur[0]:
            meilleur = (rang, sc, a, sr, mots, pm, df)
        if not df and sc >= 0.9 and not prosodie.plat(pm):
            break
        if essai >= 1 and not meilleur[6] and meilleur[1] >= 0.9 and not prosodie.plat(meilleur[5]):
            break
    _, sc, a, sr, mots, pm, df = meilleur
    if df:
        print(f"    défaut de voix gardé faute de mieux ({' ; '.join(df)}) : {texte[:60]}", flush=True)
    if prosodie.plat(pm):
        print(f"    intonation plate (relief {pm['relief']}, élan {pm['elan']}) : {texte[:60]}", flush=True)
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
    open(chemin + ".vu", "w").close()   # intonation déjà jugée à l'enregistrement
    return sc
