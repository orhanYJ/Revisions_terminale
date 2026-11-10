"""Contrôle des défauts de voix d'un épisode, passage par passage (demande de Cengiz du 10/11/2026 : « vérifie bien sur
les voix qu'il n'y a pas de bugs de voix, souvent elle vrille, elle prononce mal, elle fait des trucs haut et robotique »).

Usage (depuis la racine du dépôt, après ou pendant l'enregistrement de la voix) :
    PYTHONPATH=outils/serie-maths python3 outils/serie-philo/controle_voix.py maths_ch1 [--rejeter] [--tout] ["début de passage" …]

Pour chaque passage déjà enregistré (cache de generer.py) :
- prononciation : transcription faster-whisper comparée au texte lu (score lettre à lettre, mots manquants ou ajoutés) ;
- voix trop haute ou montées aiguës : hauteur comparée à la voix de référence (prosodie.defauts) ;
- voix qui vrille : sauts brusques de hauteur à l'intérieur d'une émission ;
- bafouillage : son après le dernier mot reconnu ou avant le premier ; débit anormal ;
- voix robotique : intonation plate (prosodie.mesure : relief, élan).
Affiche les passages suspects, du plus grave au moins grave. Avec --rejeter, les passages suspects sont mis de côté
(.cache/rejets/) : le prochain `generer.py` les réenregistre, avec d'autres graines (voix_qwen lit le nombre de rejets)
et le même contrôle sur chaque prise. Avec des débuts de passage après le module, seuls ces passages sont mis de côté
(après relecture de la liste : noms propres, homophones comme « indice » entendu « un dix » ou « sept » entendu « cette »
sont de fausses alertes). --tout affiche aussi les passages propres. Ne rien mettre de côté pendant qu'un generer.py
tourne sur le même épisode (il lirait un fichier absent à l'assemblage) : attendre la fin, rejeter, relancer generer.py.
Une seconde écoute (faster-whisper medium, téléchargé au premier usage) confirme chaque défaut de prononciation ;
les nombres sont comparés en lettres si num2words est installé (pip install num2words).
"""
import difflib, hashlib, json, os, re, shutil, subprocess, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
for d in ("serie-pc", "serie-svt", "serie-maths", "serie-ses", "serie-hggsp", "serie-dnl", "serie-acl"):
    sys.path.insert(1, os.path.join(os.path.dirname(ICI), d))
os.environ.setdefault("SERIE_MOTEUR", "qwen")
import generer as G  # noqa: E402
import prosodie  # noqa: E402
import voix_qwen as VQ  # noqa: E402

SEUIL_SCORE = 0.86   # sous ce score lettre à lettre, on regarde les mots (les nombres écrits en chiffres font baisser le score)


NOMBRES = set("""zéro un une deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize
vingt trente quarante cinquante soixante cent cents mille million millions milliard milliards et virgule premier
première deuxième troisième quatrième cinquième sixième septième huitième neuvième dixième onzième douzième
treizième quatorzième quinzième seizième dixseptième dixhuitième dixneuvième vingtième siècle""".split())


def _nombres_en_lettres(texte):
    """La transcription écrit souvent les nombres en chiffres (et les siècles en chiffres romains) : on retire les
    nombres des deux côtés pour comparer les mots ; « l 'hérédité » (découpe de la transcription) redevient « l'hérédité »."""
    texte = re.sub(r"\s+(['’-])", r"\1", texte)
    texte = re.sub(r"\b[XVI]+(e|ème)\b", " ", texte)
    texte = re.sub(r"\d+([,.]\d+)?(e|er|ème)?", " ", texte)
    garde = []
    for w in texte.split():
        parties = [VQ._norm(x) for x in re.split(r"[-\s]", w)]
        if parties and all(x in NOMBRES or not x for x in parties):
            continue
        garde.append(w)
    return " ".join(garde)


def _romain(r):
    v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}
    t = 0
    for i, c in enumerate(r):
        t += -v[c] if i + 1 < len(r) and v[c] < v[r[i + 1]] else v[c]
    return t


def _en_lettres(texte):
    """Écrit en lettres les nombres d'une transcription (num2words, s'il est installé) ; None sinon."""
    try:
        from num2words import num2words
    except ImportError:
        return None
    def dec(m):
        ent, frac = m.group(1), m.group(3)
        out = num2words(int(ent), lang="fr")
        if frac:
            out += " virgule " + " ".join(num2words(int(c), lang="fr") for c in frac) if frac.startswith("0") else " virgule " + num2words(int(frac), lang="fr")
        return " " + out + " "
    texte = re.sub(r"\b([XVILCM]+)(e|ème)\b", lambda m: " " + num2words(_romain(m.group(1)), lang="fr", to="ordinal") + " ", texte)
    texte = re.sub(r"(\d+)(er|re)\b", lambda m: " premier " if m.group(1) == "1" else " " + num2words(int(m.group(1)), lang="fr", to="ordinal") + " ", texte)
    texte = re.sub(r"(\d+)(e|ème)\b", lambda m: " " + num2words(int(m.group(1)), lang="fr", to="ordinal") + " ", texte)
    texte = re.sub(r"(\d+)\s(\d{3})\b", r"\1\2", texte)   # 1 681 -> 1681
    return re.sub(r"(\d+)([,.](\d+))?", dec, texte)


def _flux_nombres(texte):
    """Suite des mots-nombres ; « un », « une », « et » ne comptent que dans un nombre composé (« quarante et un »,
    « quatre-vingt-un »), pas comme article ou conjonction."""
    mots = [re.sub(r"s$", "", VQ._norm(x)) if VQ._norm(x) in ("vingts", "cents") else VQ._norm(x)
            for x in re.split(r"[\s'’,.;:!?-]+", texte)]
    out, prec = [], False
    for x in mots:
        if x in NOMBRES and x not in ("et", "un", "une", "siecle", "siècle"):
            out.append(x); prec = True
        elif x in ("et", "un", "une") and prec:
            out.append("un" if x == "une" else x); prec = x == "et"
        else:
            prec = False
    while out and out[-1] == "et":
        out.pop()
    return [x for i, x in enumerate(out) if not (x == "et" and (i + 1 == len(out) or out[i + 1] != "un"))]


def ecarts_nombres(lu, entendu):
    """Nombres dits autrement que le texte (ex. « mille six cent quatre-vingt-un » entendu « 1680 »)."""
    e = _en_lettres(entendu)
    if e is None:
        return []
    # le texte peut lui aussi porter des nombres en chiffres (dates) : la voix les lit en lettres
    a, b = _flux_nombres(_en_lettres(lu)), _flux_nombres(e)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != "equal":
            out.append(f"{' '.join(a[i1:i2]) or '—'} → {' '.join(b[j1:j2]) or '—'}")
    return out


def ecarts_mots(lu, entendu):
    """Mots du texte absents de la transcription et mots entendus en trop (hors nombres)."""
    # l'apostrophe sépare les mots (« n'égale » transcrit pour « n égale »)
    a = [VQ._norm(w) for w in re.findall(r"[\wÀ-ÿœæ-]+", _nombres_en_lettres(lu))]
    b = [VQ._norm(w) for w in re.findall(r"[\wÀ-ÿœæ-]+", _nombres_en_lettres(entendu))]
    # homophones fréquents de la transcription (« retient » pour « retiens », « égal » pour « égale ») : on ignore
    # l'écart s'il ne porte que sur la dernière lettre muette
    # et le « h » muet (« l'hérédité » transcrit « l'érédité »)
    a = [re.sub(r"[stex]$", "", re.sub(r"^([ldnmstcj]|qu)?h", r"\1", x)) for x in a]
    b = [re.sub(r"[stex]$", "", re.sub(r"^([ldnmstcj]|qu)?h", r"\1", x)) for x in b]
    a = [x for x in a if x]; b = [x for x in b if x]
    manque, trop = [], []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ("delete", "replace"):
            manque += a[i1:i2]
        if op in ("insert", "replace"):
            trop += b[j1:j2]
    return manque, trop


def passages(module):
    import importlib
    ep = importlib.import_module(module)
    G.PRONONCIATION.update(getattr(ep, "PRONONCIATION", {}))
    langue = getattr(ep, "LANGUE", "fr")
    G.VOIX.clear(); G.VOIX.update(G.VOIX_LANGUE[langue])
    for sc in ep.SCENES:
        for b in G._beats(sc):
            if "pause" in b:
                continue
            ecrit, _ = G._nettoie(b["t"])
            lu = G.prononce(ecrit)
            if not lu.strip():
                continue
            pros = dict(G.PROSODIE[b["v"]], **b["pros"])
            cle = hashlib.sha1(json.dumps([G.MOTEUR, G.VOIX[b["v"]], pros, lu], ensure_ascii=False).encode()).hexdigest()[:14]
            yield lu, ecrit, G.VOIX[b["v"]], os.path.join(G.CACHE, cle + ".mp3"), langue


def comparer(lu, ecrit, entendu):
    """Score, écarts de mots et de nombres : contre la graphie donnée à la voix (PRONONCIATION) et contre le texte
    écrit, la transcription suivant l'une ou l'autre selon les mots (noms propres)."""
    best = None
    for ref in {lu, ecrit}:
        sc = VQ._score(ref, entendu)
        m, t = ecarts_mots(ref, entendu)
        nb = ecarts_nombres(ref, entendu)
        k = (len([w for w in m + t if len(w) > 3]) + len(nb), -sc)
        if best is None or k < best[0]:
            best = (k, sc, m, t, nb)
    return best[1:]


def gravite(d, sc, manque, trop, pm, nombres=()):
    """Raisons d'écarter un passage, avec un poids (plus grand = plus grave)."""
    raisons = [(3, r) for r in prosodie.suspect(d)]
    if nombres:
        raisons.append((4, "nombre mal dit : " + " ; ".join(nombres[:4])))
    graves = [w for w in manque + trop if len(w) > 3]
    if (sc < SEUIL_SCORE and len(graves) >= 2) or len(graves) >= 4:
        raisons.append((4, f"prononciation (score {sc:.2f}) : manque {' '.join(manque[:8]) or '—'} ; en trop {' '.join(trop[:8]) or '—'}"))
    if prosodie.plat(pm):
        raisons.append((1, f"intonation plate (relief {pm['relief']}, élan {pm['elan']})"))
    return raisons


_w2 = []


def _second():
    if not _w2:
        try:
            from faster_whisper import WhisperModel
            _w2.append(WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=2))
        except Exception as err:
            print("(pas de seconde écoute :", err, ")", flush=True)
            _w2.append(None)
    return _w2[0]


def controler(module, rejeter=False, tout=False, choix=()):
    from faster_whisper import WhisperModel
    w = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
    res, absents = [], 0
    for lu, ecrit, voix, f, langue in passages(module):
        if not os.path.exists(f):
            absents += 1
            continue
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                             capture_output=True).stdout
        y = np.frombuffer(raw, dtype=np.float32)
        segs, _ = w.transcribe(y, language=langue, word_timestamps=True)
        mots = [(x.start, x.end - x.start, x.word.strip()) for s in segs for x in (s.words or [])]
        entendu = " ".join(m[2] for m in mots)
        sc, manque, trop, nombres = comparer(lu, ecrit, entendu)
        d = prosodie.defauts(y, 16000, prosodie.ref_hz(VQ.REF[voix][0]), mots, len(lu))
        pm = prosodie.mesure(y, 16000)
        raisons = gravite(d, sc, manque, trop, pm, nombres)
        if any(p == 4 for p, _ in raisons):
            # seconde écoute par un modèle plus grand : la petite transcription se trompe souvent sur les nombres,
            # les noms propres et les homophones ; on ne garde le défaut de prononciation que s'il se confirme
            w2 = _second()
            if w2 is not None:
                segs2, _ = w2.transcribe(y, language=langue, beam_size=5)
                entendu2 = " ".join(s.text.strip() for s in segs2)
                sc2, m2, t2, n2 = comparer(lu, ecrit, entendu2)
                r2 = gravite(d, sc2, m2, t2, pm, n2)
                if not any(p == 4 for p, _ in r2):
                    raisons = [x for x in raisons if x[0] != 4]
                else:
                    raisons = [x for x in raisons if x[0] != 4] + [x for x in r2 if x[0] == 4]
                    entendu = entendu2
        res.append((sum(p for p, _ in raisons), lu, f, raisons, d, pm, sc, entendu))
        if tout or raisons:
            print(("SUSPECT " if raisons else "ok      ") + lu[:70], flush=True)
            for _, r in raisons:
                print("        -", r, flush=True)
            if raisons:
                print("        entendu :", entendu[:160], flush=True)
    res.sort(key=lambda x: -x[0])
    sus = [x for x in res if x[3]]
    print(f"\n{len(res)} passages contrôlés, {len(sus)} suspects, {absents} pas encore enregistrés.")
    if res:
        for k in ("hauteur", "aigu", "sauts", "queue", "debit"):
            v = [x[4].get(k) for x in res if x[4].get(k) is not None]
            if v:
                print(f"  {k} : médiane {np.median(v):.2f}, p90 {np.percentile(v, 90):.2f}, max {np.max(v):.2f}")
    if choix:
        # rejet ciblé : seulement les passages dont le texte commence par l'un des débuts donnés (après relecture de la
        # liste : les noms propres et quelques homophones, « indice » entendu « un dix », sont de fausses alertes)
        sus = [x for x in res if any(x[1].startswith(c) for c in choix)]
        rejeter = True
    if rejeter and sus:
        dos = os.path.join(G.CACHE, "rejets")
        os.makedirs(dos, exist_ok=True)
        for _, lu, f, raisons, *_ in sus:
            base = os.path.basename(f)
            n = len([x for x in os.listdir(dos) if x.startswith(base)])
            for src, ext in ((f, ""), (f + ".json", ".json"), (f + ".vu", ".vu"), (f[:-4] + ".wav", ".wav")):
                if os.path.exists(src):
                    shutil.move(src, os.path.join(dos, f"{base}.{n}{ext}"))
        print(f"{len(sus)} passages mis de côté : relancer generer.py pour les réenregistrer.")
    return sus


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    controler(args[0], rejeter="--rejeter" in sys.argv, tout="--tout" in sys.argv, choix=args[1:])
