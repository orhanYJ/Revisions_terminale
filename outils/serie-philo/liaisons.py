"""Contrôle des liaisons d'une prise de voix, par reconnaissance des phonèmes (11/11/2026, pilote : « elle ne fait pas la
liaison des fois, par exemple de mieux en mieux » ; en maths, « il y a des liaisons entre les noms des symboles et le
nom des lettres et même les chiffres »).

La reconnaissance vocale (faster-whisper) écrit « de mieux en mieux » que la liaison soit faite ou non : elle ne peut pas
juger. On reconnaît donc les phonèmes (modèle wav2vec2 « xlsr-53-espeak-cv-ft », Apache 2.0, téléchargé au premier
usage, environ 1,2 Go) et on regarde, à la frontière de deux mots (instants donnés par la transcription, voir
voix_qwen._caler), si une consonne de liaison est entendue au début du second mot :
- liaison obligatoire manquante (« les océans », « deux espaces », « de mieux en mieux », « on a », « un océan ») ;
- liaison interdite faite devant une lettre ou un nombre d'une formule (« tout-t-ène », « deux-z-ène », « plus-z-un »),
  règle active seulement quand le script le demande (LIAISONS = "maths").
Le résultat sert à écarter les prises fautives (voix_qwen.dire) et à relire un épisode (controle_voix.py).
"""
import json, os, re

import numpy as np

MODELE = "facebook/wav2vec2-xlsr-53-espeak-cv-ft"
_m = []
VOY = set("aeiouyéèêëàâîïôöûüœæ")
# mots qui se lient en [z] devant une voyelle (déterminants, nombres, pronoms, quelques adverbes)
EN_Z = {"les", "des", "ces", "mes", "tes", "ses", "nos", "vos", "aux", "deux", "trois", "six", "dix", "nous", "vous",
        "ils", "elles", "quelques", "plusieurs", "leurs", "certains", "certaines", "toutes", "tous", "très", "chez",
        "grands", "grandes", "petits", "petites", "nouveaux", "anciens", "anciennes", "premiers", "premières",
        "derniers", "dernières", "autres", "mêmes", "beaux", "vieux", "mieux", "moins"}
EN_N = {"on", "en", "mon", "ton", "son", "aucun"}
EN_T = {"tout", "petit", "grand", "quand", "dont", "c'est", "est", "sont", "ont", "font", "vont", "étaient", "était"}
# h muet courants (la liaison se fait) ; tout autre mot en h est laissé de côté (h aspiré possible)
H_MUET = {"homme", "hommes", "histoire", "histoires", "heure", "heures", "habitant", "habitants", "hypothèse",
          "hypothèses", "hémisphère", "hémisphères", "hérédité", "huile", "hiver", "hivers", "horizon", "hôpital",
          "hôpitaux", "humain", "humains", "humanité", "hydrocarbures", "hydrocarbure", "habitude", "habitudes"}
# mots après lesquels la liaison n'est pas obligatoire (on ne la réclame pas) même devant voyelle
PAS_APRES = {"et"}
# en maths : lettres et nombres d'une formule, devant lesquels on ne lie jamais
MATHS = {"n", "k", "p", "f", "x", "b", "v", "m", "q", "r", "a", "u", "un", "une", "huit", "onze", "ène", "ka", "pé",
         "effe", "ixe", "bé", "vé", "ème", "ku", "erre", "plusse"}
LIANTS_MATHS = {"plus", "moins", "deux", "trois", "six", "dix", "fois", "tout", "vingt", "cent", "les", "des", "sous",
                "dans", "est", "sont", "sans", "quand", "pas", "mais", "aux", "plusse"}


def _charger():
    if not _m:
        import torch
        from transformers import Wav2Vec2ForCTC, Wav2Vec2FeatureExtractor
        from huggingface_hub import snapshot_download
        d = snapshot_download(MODELE)
        voc = json.load(open(os.path.join(d, "vocab.json")))
        _m.append((Wav2Vec2FeatureExtractor.from_pretrained(d), Wav2Vec2ForCTC.from_pretrained(d).eval(),
                   {v: k for k, v in voc.items()}))
    return _m[0]


def phonemes(a, sr):
    """[(phonème, instant en s)] reconnus dans l'audio (une trame CTC = 20 ms)."""
    import torch, librosa
    fe, mod, inv = _charger()
    a = np.asarray(a, dtype=np.float32)
    if sr != 16000:
        a = librosa.resample(a, orig_sr=sr, target_sr=16000)
    x = fe(a, sampling_rate=16000, return_tensors="pt").input_values
    with torch.no_grad():
        ids = torch.argmax(mod(x).logits, -1)[0].tolist()
    pas = len(a) / 16000 / max(1, len(ids))
    out, prec = [], None
    for i, k in enumerate(ids):
        if k != prec and inv[k] not in ("<pad>", "<s>", "</s>", "<unk>"):
            out.append((inv[k], i * pas))
        prec = k
    return out


def _cle(w):
    return w.lower().replace("’", "'")


def _commence_voyelle(w):
    w = _cle(w)
    if w[:1] in VOY:
        return True
    return w in H_MUET


def contextes(mots, maths=False):
    """Paires de mots à contrôler : [(i, attendu, mot1, mot2)] ; attendu = 'z', 'n', 't' (liaison obligatoire) ou
    '-' (liaison interdite)."""
    out = []
    for i in range(len(mots) - 1):
        a, b = _cle(mots[i]), _cle(mots[i + 1])
        if maths and a in LIANTS_MATHS and b in MATHS:
            out.append((i, "-", mots[i], mots[i + 1]))
            continue
        if not _commence_voyelle(b) or a in PAS_APRES or (maths and b in MATHS):
            continue
        if a in EN_Z and not (a in ("mieux", "moins") and b != "en"):
            out.append((i, "z", mots[i], mots[i + 1]))
        elif a in EN_N:
            out.append((i, "n", mots[i], mots[i + 1]))
    return out


VOYP = set("aeiouyɛɑɔøœəɪʊɐɛ̃ɑ̃ɔ̃œ̃") | {"ɛ̃", "ɑ̃", "ɔ̃", "œ̃"}
# première voyelle attendue d'une lettre ou d'un nombre dit dans une formule
PREM = {"n": "ɛ", "f": "ɛ", "x": "i", "m": "ɛ", "r": "ɛ", "s": "ɛ", "l": "ɛ", "a": "a", "u": "y", "ène": "ɛ", "effe": "ɛ",
        "ixe": "i", "ème": "ɛ", "erre": "ɛ", "un": "ɛ̃ɑ̃œ̃a", "une": "y", "huit": "ɥyi", "onze": "ɔ̃ɔo"}


def fautes(texte, temps, a, sr, maths=False, ph=None):
    """Liaisons fautives d'une prise. texte : texte lu ; temps : [[début, durée, mot]] calés sur les mots du texte
    (voix_qwen._caler) ; a, sr : audio. Renvoie [(mot1, mot2, 'manquante' | 'en trop', phonèmes entendus)].
    Les instants de la transcription et ceux des phonèmes ne coïncident pas exactement (≈ 0,1 s) : on regarde une
    fenêtre autour du début du second mot."""
    mots = [m[2] for m in temps]
    ctx = contextes(mots, maths)
    if not ctx:
        return []
    ph = ph if ph is not None else phonemes(a, sr)
    res = []
    for i, att, m1, m2 in ctx:
        t2 = temps[i + 1][0]
        fen = [p for p, t in ph if t2 - .15 <= t <= t2 + .3]
        if att == "-":
            v = PREM.get(_cle(m2))
            if not v:
                continue
            # [z] ou [t] suivi de la première voyelle de la lettre / du nombre : liaison faite, fautive
            if any(fen[j] in ("z", "t") and fen[j + 1][:1] in v for j in range(len(fen) - 1)):
                res.append((m1, m2, "en trop", " ".join(fen)))
        else:
            c = att
            if not any(fen[j] == c and fen[j + 1] in VOYP for j in range(len(fen) - 1)):
                res.append((m1, m2, "manquante", " ".join(fen)))
    return res
