"""Repère les visuels de texte qui restent affichés en même temps (oubli d'un repère {-id}).

Usage : python3 outils/serie-philo/chevauchements.py liberte-2   (lit philo/serie/<code>.data.js)
"""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PRINCIPAUX = {"portrait", "def", "note", "cols", "cartes", "liste", "cit", "mot", "question", "dialogue", "carte", "nuage", "titre", "illu", "frise"}


def boite(v):
    if v["type"] == "portrait":
        return (0, 600)         # grand portrait fondu à gauche
    if "x" in v and "w" in v:
        return (v["x"], v["x"] + v["w"])
    return (100, 1180)          # centré : occupe la largeur


def chevauchements(code, marge=0.8):
    js = open(os.path.join(RACINE, "philo", "serie", code + ".data.js"), encoding="utf-8").read()
    d = json.loads(js[js.index("{"):js.rindex("}") + 1])
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
    return res


def trous(code, seuil=3.0):
    """Intervalles de plus de `seuil` secondes où l'écran n'a ni texte, ni image, ni illustration."""
    js = open(os.path.join(RACINE, "philo", "serie", code + ".data.js"), encoding="utf-8").read()
    d = json.loads(js[js.index("{"):js.rindex("}") + 1])
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
