"""Voix enregistrées des cartes animées : un MP3 par scène et par langue, dans dnl/cartes/voix/<CODE>/.

Voix neuronales Microsoft (fr-FR-RemyMultilingualNeural, en-GB-RyanNeural), produites par le paquet edge-tts
(service de lecture à voix haute du navigateur Edge : gratuit, non officiel ; s'il cesse de fonctionner,
les fichiers déjà produits restent et le moteur se rabat sur la voix du téléphone pour les autres).
Le nom de fichier contient une empreinte du texte lu : seule une légende modifiée est réenregistrée.
Usage : generer.py ... --voix (dans ce conteneur : SSL_CERT_FILE=/root/.ccr/ca-bundle.crt ; le proxy est lu dans HTTPS_PROXY).
"""
import asyncio, hashlib, os, re

VOIX = {"fr": "fr-FR-RemyMultilingualNeural", "en": "en-GB-RyanNeural"}
DEBIT = "+0%"

MOIS_FR = {"janv.": "janvier", "févr.": "février", "avr.": "avril", "juill.": "juillet", "sept.": "septembre",
           "oct.": "octobre", "nov.": "novembre", "déc.": "décembre"}
MOIS_EN = {"Jan.": "January", "Feb.": "February", "Apr.": "April", "Aug.": "August", "Sept.": "September",
           "Oct.": "October", "Nov.": "November", "Dec.": "December"}


def a_lire(s, lang):
    """Texte prononcé pour une scène : date, titre et l'événement en une phrase (evenements.py), sans les
    explications de la légende ; abréviations développées."""
    date, titre = s["date"][lang], s["titre"][lang]
    texte = (s["evt"][lang] if s.get("evt") else s["texte"][lang]).replace("[hors]", "")
    t = f"{date}. {titre}. {texte}"
    t = re.sub(r"\s+", " ", t).replace(" .", ".").replace(" ,", ",")
    if lang == "fr":
        for k, v in MOIS_FR.items():
            t = re.sub(re.escape(k), v, t, flags=re.I)
        t = re.sub(r"(\d)\s*[-–]\s*(\d)", r"\1 à \2", t)
        t = re.sub(r"([a-zéû0-9])\s+-\s+(\d|[a-zé])", r"\1 à \2", t)
        t = t.replace("n° ", "numéro ").replace("R.-U.", "Royaume-Uni")
    else:
        for k, v in MOIS_EN.items():
            t = t.replace(k, v)
        t = re.sub(r"(\d)\s*[–-]\s*(\d)", r"\1 to \2", t)
        t = re.sub(r"\s+–\s+", " to ", t)
        t = t.replace("No. ", "Number ")
    return t.strip()


def nom(texte, lang):
    h = hashlib.sha1((VOIX[lang] + DEBIT + texte).encode("utf-8")).hexdigest()[:10]
    return f"{lang}-{h}.mp3"


async def _dire(texte, voix, chemin, sem):
    import edge_tts
    async with sem:
        for essai in range(4):
            try:
                c = edge_tts.Communicate(texte, voix, rate=DEBIT, proxy=os.environ.get("HTTPS_PROXY"))
                await c.save(chemin + ".part")
                os.replace(chemin + ".part", chemin)
                return
            except Exception as e:  # réseau capricieux : on réessaie
                if essai == 3:
                    raise
                await asyncio.sleep(2 * (essai + 1))


def preparer(code, scenes, sortie, produire=False):
    """Associe à chaque scène ses fichiers de voix ; produit les manquants si produire=True,
    et supprime alors les fichiers devenus inutiles."""
    dossier = os.path.join(sortie, "voix", code)
    os.makedirs(dossier, exist_ok=True)
    taches, gardes = [], set()
    for s in scenes:
        for lang in ("fr", "en"):
            t = a_lire(s, lang)
            n = nom(t, lang)
            gardes.add(n)
            chemin = os.path.join(dossier, n)
            if not os.path.exists(chemin) and produire:
                taches.append((t, VOIX[lang], chemin))
            if os.path.exists(chemin) or produire:
                s.setdefault("voix", {})[lang] = f"voix/{code}/{n}"
    if taches:
        async def tout():
            sem = asyncio.Semaphore(4)
            await asyncio.gather(*[_dire(t, v, c, sem) for t, v, c in taches])
        asyncio.run(tout())
    if produire:
        for f in os.listdir(dossier):
            if f not in gardes:
                os.remove(os.path.join(dossier, f))
    n_ok = sum(1 for s in scenes for l in ("fr", "en") if s.get("voix", {}).get(l))
    return len(taches), n_ok
