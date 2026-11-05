"""Repère les visuels de texte qui restent affichés en même temps (oubli d'un repère {-id}).

Usage : python3 outils/serie-philo/chevauchements.py liberte-2   (lit philo/serie/<code>.data.js)
"""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PRINCIPAUX = {"portrait", "def", "note", "cols", "cartes", "liste", "cit", "mot", "question", "dialogue", "carte", "nuage", "titre", "illu", "frise",
              "anim", "formule", "graphe", "exo", "pause", "globe", "mental"}


def donnees(code):
    """Données d'un épisode philo (philo/serie) ou d'une vidéo de cours PC (pc/serie)."""
    for site in ("philo", "pc", "acl-lughnasa", "dnl", "svt"):
        f = os.path.join(RACINE, site, "serie", code + ".data.js")
        if os.path.exists(f):
            js = open(f, encoding="utf-8").read()
            return json.loads(js[js.index("{"):js.rindex("}") + 1])
    raise SystemExit(f"données introuvables : {code}.data.js")


def boite(v):
    if v["type"] == "portrait":
        return (0, 600)         # grand portrait fondu à gauche
    if v["type"] == "mental":
        return (0, 1280)        # carte mentale plein cadre
    if v["type"] == "globe":
        x = v.get("x", 0)
        return (x, x + v.get("w", 1280))
    if v["type"] == "anim":
        x = v.get("x", 50)
        return (x, x + round(v.get("h", 600) * 400 / 430))
    if v["type"] == "exo" and v.get("mode") == "coin":
        return (34, 504)
    if v["type"] == "pause":
        x = v.get("x", 200)
        return (x, x + v.get("w", 880))
    if v["type"] == "graphe":
        x = v.get("x", 640)
        return (x, x + v.get("w", 600))
    if v["type"] == "formule":
        x = v.get("x", 150)
        return (x, x + v.get("w", 980))
    if "x" in v and "w" in v:
        return (v["x"], v["x"] + v["w"])
    return (100, 1180)          # centré : occupe la largeur


def chevauchements(code, marge=0.8):
    d = donnees(code)
    vis = [v for v in d["vis"] if v["type"] in PRINCIPAUX]
    res = []
    for i, a in enumerate(vis):
        for b in vis[i + 1:]:
            deb, fin = max(a["t0"], b["t0"]), min(a["t1"], b["t1"])
            if fin - deb < marge:
                continue
            ba, bb = boite(a), boite(b)
            if min(ba[1], bb[1]) - max(ba[0], bb[0]) < (150 if "portrait" in (a["type"], b["type"]) else 40):
                continue        # côte à côte
            res.append((round(deb, 1), round(fin - deb, 1), a["id"], a["type"], b["id"], b["type"]))
    # encadrés « Notions abordées » et étiquettes « Notion · … » : même place, en haut à droite
    no = [v for v in d["vis"] if v["type"] == "notion"]
    for i, a in enumerate(no):
        for b in no[i + 1:]:
            deb, fin = max(a["t0"], b["t0"]), min(a["t1"], b["t1"])
            if fin - deb > 0.3:
                res.append((round(deb, 1), round(fin - deb, 1), a["id"], "notion", b["id"], "notion"))
    return res


def trous(code, seuil=3.0):
    """Intervalles de plus de `seuil` secondes où l'écran n'a ni texte, ni image, ni illustration."""
    d = donnees(code)
    iv = sorted((v["t0"], v["t1"], v["id"]) for v in d["vis"] if v["type"] not in ("tag",))
    res, cur = [], 0.0
    for a, b, _ in iv:
        if a - cur > seuil:
            res.append((round(cur, 1), round(a - cur, 1)))
        cur = max(cur, b)
    if d["dur"] - cur > seuil:
        res.append((round(cur, 1), round(d["dur"] - cur, 1)))
    return res


if __name__ == "__main__":
    for code in sys.argv[1:]:
        r = chevauchements(code)
        print(f"{code} : {len(r)} chevauchement(s)")
        for x in r:
            print("  t=%-6s %4.1fs  %s (%s)  ×  %s (%s)" % x)
        for t, d in trous(code):
            print(f"  écran vide à t={t} pendant {d} s")
