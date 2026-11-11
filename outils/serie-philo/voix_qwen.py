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
# mots que la reconnaissance juge souvent incertains dans un texte de sciences, alors que la voix est juste
JARGON = {"prime", "primes", "égal", "égale", "égalent", "sur", "moins", "plus", "fois", "barre", "alpha", "gamma", "delta", "lambda", "sigma", "puissance"}
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


_registres = {}


def registre(voix):
    """Hauteur médiane (Hz) de la voix de référence : sert à repérer une prise partie dans l'aigu."""
    if voix not in _registres:
        import librosa, prosodie
        y, sr = librosa.load(REF[voix][0], sr=16000, mono=True)
        _registres[voix] = prosodie.profil(y, sr)[1]
    return _registres[voix]


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


def _en_lettres(texte):
    """Les nombres écrits en chiffres par la reconnaissance (« 633 », « 6,63 ») passent en lettres, comme le texte lu :
    sans cela, un passage chiffré paraît mal dit alors que la voix est juste."""
    try:
        from num2words import num2words
    except ImportError:
        return texte
    def un(m):
        x = m.group(0).replace("\u202f", "").replace(" ", "")
        try:
            if "," in x or "." in x:
                e, d = re.split(r"[,.]", x, 1)
                return num2words(int(e), lang="fr") + " virgule " + " ".join([num2words(int(d), lang="fr")] if not d.startswith("0") else [num2words(int(c), lang="fr") for c in d])
            return num2words(int(x), lang="fr")
        except Exception:
            return m.group(0)
    return re.sub(r"\d[\d\u202f ]*(?:[,.]\d+)?", un, texte)


def _score(lu, texte_reconnu):
    """Ressemblance lettre à lettre (la découpe en mots de la reconnaissance diffère parfois : « l' » + « intelligence »)."""
    return difflib.SequenceMatcher(None, _norm(lu), _norm(_en_lettres(texte_reconnu)), autojunk=False).ratio()


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
    reg = registre(voix)
    meilleur = None
    for essai in range(4):
        torch.manual_seed(1234 + 17 * essai + len(texte))
        w, sr = m.generate_voice_clone(text=texte, language=LANGUES[langue], voice_clone_prompt=p)
        a = w[0].astype(np.float32)
        y = np.interp(np.arange(0, len(a), sr / 16000), np.arange(len(a)), a).astype(np.float32)
        segs, _ = _whisper.transcribe(y, language=langue, word_timestamps=True)
        mots_w = [x for s in segs for x in (s.words or [])]
        mots = [(x.start, x.end - x.start, x.word.strip()) for x in mots_w]
        sc = _score(texte, " ".join(x[2] for x in mots))
        # mots mal articulés (confiance de la reconnaissance sous 0,6, hors nombres) : voir audit_voix.py
        flous = [x.word.strip() for x in mots_w if x.probability < 0.6 and len(re.sub(r"[^\w]", "", x.word)) > 2
                 and not re.search(r"\d", x.word) and _norm(x.word) not in JARGON]
        if len(flous) < 2:
            flous = []          # un seul mot incertain : souvent la reconnaissance, pas la voix
        try:
            pm = prosodie.mesure(y, 16000)
        except Exception:
            pm = {"relief": 3.0, "elan": 2.0}
        vie = pm["relief"] + pm["elan"]
        try:
            an = prosodie.anomalies(y, 16000, reg, seuil=1.35, duree=0.5)     # voix partie dans l'aigu, vrille, glissements (10/11/2026)
        except Exception:
            an = []
        if flous:
            an = an + ["mots flous (%s)" % ", ".join(flous[:3])]
        try:
            aigus = prosodie.mots_aigus(y, 16000, [(x.start, x.end, x.word.strip()) for x in mots_w], reg)
        except Exception:
            aigus = []
        if aigus:
            an = an + ["mot qui saute dans l'aigu (%s)" % ", ".join("%s %d %%" % m for m in aigus[:3])]
        # rang : d'abord une prise sans dérapage, puis la justesse (au-dessus de 0,88 toutes les prises se valent),
        # puis l'intonation
        rang = (0 if an else 1, min(sc, 0.88), vie)
        if meilleur is None or rang > meilleur[0]:
            meilleur = (rang, sc, a, sr, mots, pm, an)
        if not an and sc >= 0.9 and not prosodie.plat(pm):
            break
        if essai >= 3 and not meilleur[6] and meilleur[1] >= 0.88:
            break
    _, sc, a, sr, mots, pm, an = meilleur
    if an:
        print(f"    dérapage restant ({', '.join(an)}) : {texte[:60]}", flush=True)
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
