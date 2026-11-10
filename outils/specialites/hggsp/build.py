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


def main():
    if "--sans-cartes" not in sys.argv or not os.path.exists(os.path.join(SRC, "cartes.json")):
        cartes()
    fichiers = ["data-commun.js"] + sorted(os.path.basename(f) for f in glob.glob(os.path.join(SRC, "data-*.js")) if not f.endswith("data-commun.js"))
    for f in fichiers:
        r = subprocess.run(["node", "--check", os.path.join(SRC, f)], capture_output=True, text=True)
        if r.returncode:
            sys.exit("Erreur de syntaxe dans " + f + "\n" + r.stderr)
    html = lire("shell.html")
    with open(os.path.join(SRC, "cartes.json"), encoding="utf-8") as f:
        c = json.load(f)
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
