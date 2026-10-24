"""Clé de tri chronologique des scènes : (année, mois, jour) du début de la période (date anglaise).
Pour une période sur plusieurs années, seule la première compte. Un champ « tri » : [a, m, j] la remplace."""
import re

MOIS = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9,
        "october": 10, "november": 11, "december": 12, "jan.": 1, "feb.": 2, "mar.": 3, "apr.": 4, "aug.": 8, "sept.": 9,
        "oct.": 10, "nov.": 11, "dec.": 12}
SAISONS = {"winter": 12, "spring": 4, "summer": 7, "autumn": 10, "late": 11, "early": 1}


def cle(s):
    if s.get("tri"):
        return tuple(s["tri"])
    d = s["date"]["en"].replace("—", "–").replace(" - ", "–")
    tete = re.split(r"–", d)[0].strip().lower()
    tout = d.lower()
    an = re.search(r"\d{4}", tete) or re.search(r"\d{4}", tout)
    an = int(an.group(0))
    mois = 0
    for k, v in MOIS.items():
        if re.search(r"\b" + re.escape(k), tete):
            mois = v
    if not mois and re.fullmatch(r"\d{1,2}", tete):          # « 13–20 May 1940 »
        for k, v in MOIS.items():
            if re.search(r"\b" + re.escape(k), tout):
                mois = v
                break
    for k, v in SAISONS.items():
        if k in tete:
            mois = v
    jour = re.match(r"(\d{1,2})(?!\d)", tete)
    return (an, mois, int(jour.group(1)) if jour else 0)


def trier(scenes):
    return sorted(scenes, key=cle)
