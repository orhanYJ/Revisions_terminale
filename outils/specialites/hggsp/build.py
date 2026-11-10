"""Construit hggsp/index.html à partir des sources de outils/specialites/hggsp/src/.

Usage : python3 outils/specialites/hggsp/build.py [--sans-cartes]
  1. régénère src/cartes.json avec cartes.js (fond Natural Earth 1:50m, téléchargé une fois dans ~/.cache/hggsp/) ;
     --sans-cartes réutilise le src/cartes.json existant ;
  2. assemble shell.html + style.css + cartes + données (data-commun.js puis les autres data-*.js, par ordre
     alphabétique) + app.js, et écrit hggsp/index.html.
"""
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "src")
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson"


def lire(nom):
    with open(os.path.join(SRC, nom), encoding="utf-8") as f:
        return f.read()


def cartes():
    cache = os.path.expanduser("~/.cache/hggsp")
    os.makedirs(cache, exist_ok=True)
    geo = os.path.join(cache, "ne50.geojson")
    if not os.path.exists(geo):
        print("téléchargement de Natural Earth…")
        urllib.request.urlretrieve(NE, geo)
    subprocess.run(["node", os.path.join(ICI, "cartes.js"), geo, os.path.join(SRC, "cartes.json")], check=True)


CHEMIN = re.compile(r"(?:[MLZ](?:-?\d+(?:\.\d)?,-?\d+(?:\.\d)?)?)+")


def _n(v):
    t = ("%.1f" % v).rstrip("0").rstrip(".")
    return "0" if t in ("-0", "") else t


def relatif(d):
    """Chemin M/L/Z absolu (entiers ou une décimale) → même tracé en coordonnées relatives, lignes implicites.
    Sans perte : chaque point est retrouvé exactement ; seuls les points répétés à l'identique dans un segment sont
    retirés. Renvoie None si le chemin contient autre chose (courbes, arcs…), qui est alors laissé tel quel."""
    d2 = d.replace(" ", "")
    if not d2 or not CHEMIN.fullmatch(d2):
        return None
    out, cx, cy, sx, sy, prec = [], 0.0, 0.0, 0.0, 0.0, None
    for cmd, arg in re.findall(r"([MLZ])([^MLZ]*)", d2):
        if cmd == "Z":
            out.append("z"); cx, cy, prec = sx, sy, "z"
            continue
        x, y = (float(v) for v in arg.split(","))
        if cmd == "L" and prec == "l" and x == cx and y == cy:
            continue
        a, b = _n(round(x - cx, 1)), _n(round(y - cy, 1))
        paire = a + ("" if b.startswith("-") else ",") + b
        if cmd == "M":
            out.append("m" + paire); sx, sy, prec = x, y, "m"
        else:
            out.append(("" if paire.startswith("-") else " ") + paire if prec in ("m", "l") else "l" + paire); prec = "l"
        cx, cy = x, y
    return "".join(out)


def compacter(c):
    """Allège la constante CARTES sans rien changer au dessin : chemins en relatif, fonds régionaux identiques stockés
    une seule fois dans CARTES.fonds (référencés par « @n », résolus par fondSVG dans app.js)."""
    def attr(s):
        return re.sub(r"""(?<![\w-])d=(["'])([^"']*)\1""", lambda m: "d=" + m.group(1) + (relatif(m.group(2)) or m.group(2)) + m.group(1), s)

    def parcourir(o, cle=None):
        if isinstance(o, dict):
            return {k: parcourir(v, k) for k, v in o.items()}
        if isinstance(o, list):
            return [parcourir(v) for v in o]
        if isinstance(o, str):
            return (relatif(o) or o) if cle in ("terre", "grat") else attr(o)
        return o
    c = parcourir(c)
    fonds, index = [], {}
    for grp in ("cartes", "anims"):
        for v in c.get(grp, {}).values():
            f = v.get("fond")
            if isinstance(f, str) and f != "monde" and len(f) > 200:
                if f not in index:
                    index[f] = len(fonds); fonds.append(f)
                v["fond"] = "@" + str(index[f])
    c["fonds"] = fonds
    return c


def main():
    if "--sans-cartes" not in sys.argv or not os.path.exists(os.path.join(SRC, "cartes.json")):
        cartes()
    fichiers = ["data-commun.js"] + sorted(os.path.basename(f) for f in glob.glob(os.path.join(SRC, "data-*.js")) if not f.endswith("data-commun.js"))
    for f in fichiers + ["app.js"]:
        r = subprocess.run(["node", "--check", os.path.join(SRC, f)], capture_output=True, text=True)
        if r.returncode:
            sys.exit("Erreur de syntaxe dans " + f + "\n" + r.stderr)
    html = lire("shell.html")
    with open(os.path.join(SRC, "cartes.json"), encoding="utf-8") as f:
        c = compacter(json.load(f))
    morceaux = [
        ("/*STYLE*/", lire("style.css")),
        ("/*CARTES*/", "var CARTES = " + json.dumps(c, ensure_ascii=False, separators=(",", ":")) + ";"),
        ("/*DATA*/", "\n".join(lire(f) for f in fichiers)),
        ("/*APP*/", lire("app.js")),
    ]
    for cle, val in morceaux:
        assert html.count(cle) == 1, cle
        html = html.replace(cle, val)
    sortie = os.path.join(RACINE, "hggsp", "index.html")
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(html)
    print("hggsp/index.html :", len(html.encode()) // 1024, "Ko ;", len(fichiers), "fichiers de données :", ", ".join(fichiers))


if __name__ == "__main__":
    main()
