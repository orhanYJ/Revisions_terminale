"""Génère les cartes animées DNL : dnl/cartes/<CODE>.data.js et dnl/cartes/<CODE>.html.

Usage : python3 outils/cartes-animees/generer.py DOSSIER_DONNEES [H1 H2 H3] [--voix]
  --voix : enregistre les voix manquantes (voir voix.py) ; sans cette option, les fichiers existants sont réutilisés.
  DOSSIER_DONNEES : les fonds de carte (voir outils/fiches-dnl/cartes.py), téléchargés s'ils manquent.
Chaque chapitre a son fichier de scènes (scenes_h3.py, ...) : caméra, couleurs, flèches, étiquettes,
légendes bilingues. Le moteur commun est dnl/cartes/moteur.js (+ moteur.css, d3-geo.min.js).
Après un changement de moteur.js, moteur.css ou des données, incrémenter V ci-dessous et le cache de dnl/sw.js.
"""
import importlib, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import evenements  # noqa: E402
import geo  # noqa: E402
import tri  # noqa: E402
import voix  # noqa: E402

RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
SORTIE = os.path.join(RACINE, "dnl", "cartes")
V = 6

PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre_fr}</title>
<link rel="stylesheet" href="moteur.css?v={v}">
</head>
<body>
<div class="page">
  <div class="kick">DNL History-Geography · M. Ros · {code}</div>
  <h1>{titre_fr}</h1>
  <div id="carte"></div>
  <p class="src">{sources}</p>
</div>
<script>
  if (new URLSearchParams(location.search).get("embed") === "1") {{
    document.body.classList.add("embed-page");
    var pg = document.querySelector(".page"); pg.style.padding = "0"; pg.style.maxWidth = "none";
    pg.querySelector("h1").remove(); pg.querySelector(".kick").remove(); pg.querySelector(".src").remove();
  }}
</script>
<script src="d3-geo.min.js?v={v}"></script>
<script src="{code}.data.js?v={v}"></script>
<script src="moteur.js?v={v}"></script>
</body>
</html>
"""

SOURCES = ("Fonds de carte : frontières de 1930 (aourednik/historical-basemaps), CShapes 2.0 (ETH Zurich), Natural Earth, "
           "départements (gregoiredavid/france-geojson), ligne de démarcation (Département de l'Ain, data.gouv.fr). "
           "Lignes de front et flèches simplifiées. Rendu : d3-geo (licence ISC).")


def generer(code, dossier, produire_voix=False):
    sc = importlib.import_module("scenes_" + code.lower())
    D, E = geo.charger_tout(dossier)
    P = geo.pieces_monde(D, E)
    ordre = sc.ordre(P)
    pieces = geo.encoder(P, ordre)
    scenes = tri.trier(sc.scenes())
    evenements.attacher(code, scenes)  # phrase courte lue par la voix (sans les explications)
    if hasattr(sc, "etat"):
        # carte calculée par date : état politique à la date de la scène (etat), plus les mises en valeur
        # propres à la scène (st) ; on n'écrit que ce qui change d'une scène à l'autre (None = couleur par défaut)
        prec = {}
        for s in scenes:
            k = tri.cle(s)
            plein = dict(sc.etat(k))
            plein.update(s.get("st", {}))
            plein = {p: v for p, v in plein.items() if v}
            diff = {p: v for p, v in plein.items() if prec.get(p) != v}
            diff.update({p: None for p in prec if p not in plein})
            s["st"] = diff
            prec = plein
    for s in scenes:
        s.pop("tri", None)
    utilises = set()
    for s in scenes:
        utilises.update(s.get("st", {}).keys())
        for a in s.get("arrows", []):
            a["pts"] = geo.courbe(a.pop("a"), a.pop("b"), a.pop("k", 0.15)) if "a" in a else [[round(x * 100), round(y * 100)] for x, y in a.pop("ligne")]
    inconnus = utilises - set(ordre)
    assert not inconnus, inconnus
    for s in scenes:
        for k in ("labels", "pins"):
            for i in s.get(k, []):
                assert i in sc.LABELS, (s["date"]["fr"], i)
        assert s["date"]["fr"] and s["date"]["en"] and s["titre"]["fr"] and s["titre"]["en"] and s["texte"]["fr"] and s["texte"]["en"], s["date"]
    nv, nok = voix.preparer(code, scenes, SORTIE, produire_voix)
    data = {
        "code": code, "titre": sc.TITRE, "parties": sc.PARTIES, "overlay": sc.OVERLAY, "occ": sc.OCC,
        "pieces": pieces, "labels": sc.LABELS, "cles": sc.CLES,
        "fronts": {k: {"pts": geo.ligne(v["pts"]), "occ": v["occ"]} for k, v in sc.FRONTS.items()},
        "scenes": scenes,
    }
    js = "/* Carte animée " + code + " — générée par outils/cartes-animees/generer.py : ne pas modifier à la main. */\nwindow.CARTE = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
    open(os.path.join(SORTIE, code + ".data.js"), "w", encoding="utf-8").write(js)
    open(os.path.join(SORTIE, code + ".html"), "w", encoding="utf-8").write(
        PAGE.format(titre_fr=sc.TITRE["fr"], code=code, v=V, sources=SOURCES))
    tot = sum(s["d"] for s in scenes)
    print(f"{code} : {len(scenes)} scènes, {int(tot // 60)} min {int(tot % 60)} s, {len(js) // 1024} Ko, voix {nok}/{2 * len(scenes)} ({nv} enregistrées)")


if __name__ == "__main__":
    dossier = sys.argv[1]
    os.makedirs(SORTIE, exist_ok=True)
    args = sys.argv[2:]
    produire = "--voix" in args
    for code in ([a for a in args if not a.startswith("--")] or ["H3"]):
        generer(code, dossier, produire)
