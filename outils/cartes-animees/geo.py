"""Géométries des cartes animées DNL : pièces du monde et de l'Europe, en deux niveaux de détail.

Les fonds viennent des mêmes sources que les fiches PDF (outils/fiches-dnl, voir cartes.py et europe.py) :
frontières de 1930 (aourednik/historical-basemaps), CShapes 2.0, Natural Earth, départements français
(gregoiredavid/france-geojson) et ligne de démarcation (Département de l'Ain, data.gouv.fr).

Chaque pièce est codée pour d3-geo : coordonnées en centièmes de degré, anneaux extérieurs dans le
sens des aiguilles d'une montre (convention sphérique de d3), deux niveaux de détail :
« g » (grossier, vue lointaine) et « f » (fin, vue rapprochée).
"""
import os, sys
from shapely.geometry import Polygon, MultiPolygon, shape
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "fiches-dnl"))
from cartes import charger, pays  # noqa: E402
from europe import charger_eu, regions, zones_france  # noqa: E402

# pays de 1930 remplacés en Europe par les pièces fines d'europe.regions
REMPLACES = {"Germany", "East Prussia", "Austria", "Czechoslovakia", "Danzig", "Poland", "Estonia", "Latvia", "Lithuania",
             "Romania", "Finland", "Italy", "Dodecanese Islands", "Albania", "United Kingdom of Great Britain and Ireland",
             "France", "Republic of Turkey", "Turkey", "Spain", "Portugal", "Switzerland", "Sweden", "Norway", "Denmark",
             "Netherlands", "Belgium", "Luxembourg", "Hungary", "Yugoslavia", "Bulgaria", "Greece", "Iceland",
             "White Russia", "Armenia", "Georgia", "Azerbaijan"}


def polys(g):
    if g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    return [p for p in getattr(g, "geoms", []) if isinstance(p, Polygon) and not p.is_empty]


def code(g, tol, aire_min):
    """MultiPolygon d3 (anneaux extérieurs horaires) en entiers (centièmes de degré)."""
    if tol:
        g = g.simplify(tol, preserve_topology=True)
    out = []
    for p in polys(g.buffer(0)):
        if p.area < aire_min:
            continue
        p = orient(p, sign=-1.0)
        anneaux = []
        for r in [p.exterior] + list(p.interiors):
            pts, prec = [], None
            for x, y in r.coords:
                q = (round(x * 100), round(y * 100))
                if q != prec:
                    pts.append(list(q))
                prec = q
            if len(pts) >= 4:
                anneaux.append(pts)
        if anneaux:
            out.append(anneaux)
    return out


def ligne(pts, n=90):
    """Rééchantillonne une ligne (lon, lat) en n points régulièrement espacés (pour faire glisser un front)."""
    import math
    d = [0.0]
    for (a, b), (c, e) in zip(pts, pts[1:]):
        d.append(d[-1] + math.hypot((c - a) * math.cos(math.radians((b + e) / 2)), e - b))
    L, out, j = d[-1], [], 0
    for i in range(n):
        s = L * i / (n - 1)
        while j < len(d) - 2 and d[j + 1] < s:
            j += 1
        t = 0 if d[j + 1] == d[j] else (s - d[j]) / (d[j + 1] - d[j])
        out.append([round((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * t) * 100), round((pts[j][1] + (pts[j + 1][1] - pts[j][1]) * t) * 100)])
    return out


def courbe(a, b, k=0.2, n=28):
    """Flèche courbe de a vers b (Bézier quadratique en lon/lat), k = bombement relatif."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    cx, cy = mx - dy * k, my + dx * k
    out = []
    for i in range(n):
        t = i / (n - 1)
        x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * cx + t * t * b[0]
        y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * cy + t * t * b[1]
        out.append([round(x * 100), round(y * 100)])
    return out


def charger_tout(dossier):
    D = charger(dossier)
    E = charger_eu(dossier)
    return D, E


def pieces_monde(D, E, extra_fr=None):
    """Pièces communes : pays de 1930 hors Europe, pièces européennes datées, zones de la France.
    Renvoie un dict id → (géométrie grossière, géométrie fine)."""
    W = pays(D["world_1930.geojson"], 0)
    Rg = regions(D, E, 0.12)
    Rf = regions(D, E, 0.02)
    P = {}
    # fond de terre continu (Natural Earth) : bouche les lacunes du fond de 1930 (Transjordanie, etc.)
    terre = unary_union([shape(ft["geometry"]).buffer(0) for ft in E["ne_50m_admin_0_countries.geojson"]["features"]
                         if ft["properties"].get("ADMIN") != "Antarctica"])
    for n, g in W.items():
        if n in REMPLACES or n == "None":
            continue
        P["w:" + n] = (g, g)
    from shapely.geometry import box
    europe = box(-32, 27, 70, 72)  # ôte les possessions lointaines (Groenland du Danemark, etc.)
    for k in Rf:
        if k == "fond":
            continue
        g, f = Rg[k], Rf[k]
        if k not in ("urss",):
            g, f = g.intersection(europe), f.intersection(europe)
        if k == "denmark":  # sans l'Islande ni les Féroé, rattachées à la couronne danoise dans le fond de 1930
            g, f = g.intersection(box(7, 54, 16, 58)), f.intersection(box(7, 54, 16, 58))
        P[k] = (g, f)
    # zones de la France (1940-1942)
    Z = zones_france(D)
    deps = {ft["properties"]["code"]: shape(ft["geometry"]).buffer(0) for ft in D["dep.geojson"]["features"]}
    nord = unary_union([deps["59"], deps["62"]])
    ital = unary_union([deps[c] for c in ("73", "74", "38", "26", "05", "04", "06", "83", "2A", "2B")])
    P["fr_occ"] = (Z["occupee"].difference(nord), Z["occupee"].difference(nord))
    P["fr_nord"] = (nord, nord)
    P["fr_annex"] = (Z["annexee"], Z["annexee"])
    P["fr_libre"] = (Z["libre"], Z["libre"])
    P["fr_ital"] = (ital.intersection(Z["libre"].buffer(0.01)), ital.intersection(Z["libre"].buffer(0.01)))
    # territoire soviétique de juin 1941 (zone de découpe de l'occupation à l'Est)
    sov = unary_union([Rf["urss"], Rf["pologne_urss"], Rf["baltes"], Rf["bessarabie"], Rf["carelie"]])
    P["sov41"] = (sov, sov)
    # zones propres aux chapitres H1 et H2
    from europe import _rhenanie
    rh = _rhenanie(Rf)
    P["rhenanie"] = (rh, rh)
    etats = {ft["properties"]["name"]: shape(ft["geometry"]).buffer(0) for ft in E["ne_10m_admin_1_states_provinces.geojson"]["features"]
             if ft["properties"].get("admin") == "United States of America"}
    dust = unary_union([etats[n] for n in ("Oklahoma", "Kansas", "Colorado", "New Mexico", "Texas")]).intersection(box(-104.0, 34.3, -98.0, 39.6))
    P["dustbowl"] = (dust, dust)
    ne0 = {ft["properties"]["ADMIN"]: shape(ft["geometry"]).buffer(0) for ft in E["ne_50m_admin_0_countries.geojson"]["features"]}
    ukr = ne0["Ukraine"].intersection(Rf["urss"].buffer(0.02)).difference(box(32.3, 44.2, 36.8, 46.0))
    P["ukraine32"] = (ukr, ukr)
    if extra_fr:
        P.update(extra_fr)
    # fond de terre : tout ce que les pièces ne couvrent pas (Groenland, Arabie du Nord, îles arctiques…),
    # calculé après coup pour qu'aucune découpe ne laisse de trou
    couvert = unary_union([f for k, (g, f) in P.items() if k != "sov41"]).buffer(0.15)
    lacunes = unary_union([p for p in polys(terre.difference(couvert)) if p.area > 0.1]).buffer(0.2).simplify(0.05)
    P["terre"] = (lacunes, lacunes)
    return P


from shapely.geometry import box as _box
ZOOMS = _box(-12, 33, 50, 62)


def encoder(P, ordre):
    """Encode les pièces dans l'ordre de dessin, en trois niveaux de détail (tolérances en degrés) :
    g (globe entier) 0,2 ; m (un continent) 0,06 ; f (un pays, une région) 0,02, ou 0,004 pour la France."""
    out = []
    for pid in ordre:
        g, f = P[pid]
        fin_tol = 0.004 if pid.startswith("fr_") else 0.02
        d = {"id": pid, "g": code(g, 0.2, 0.03), "m": code(f, 0.06, 0.004)}
        # le niveau fin ne sert qu'aux gros plans, tous en Europe : ailleurs, le moteur se contente de « m »
        if f.intersects(ZOOMS):
            d["f"] = code(f, fin_tol, 0.0004)
        out.append(d)
    return out
