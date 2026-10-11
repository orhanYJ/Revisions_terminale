"""Cartes récapitulatives des fiches DNL (H1, H2, H3), en SVG, en anglais et en français.

Usage : python3 cartes.py DOSSIER_DONNEES
  DOSSIER_DONNEES reçoit les fonds de carte téléchargés (non versionnés) :
  - frontières de 1930 : aourednik/historical-basemaps (world_1930.geojson), licence GPL-3.0 ;
  - départements français : gregoiredavid/france-geojson (version simplifiée) ;
  - ligne de démarcation : Département de l'Ain, data.gouv.fr « Ligne de démarcation », Licence Ouverte 2.0 ;
  - pour les cartes d'Europe datées (europe.py) : CShapes 2.0 (ICR, ETH Zurich) et Natural Earth.
Les SVG produits vont dans cartes/ à côté de ce script ; generer.js les insère dans les fiches.
Dépendance : shapely (pip install shapely).
Contrôle de la simplification : SANS_SIMPLIF=1 produit les cartes sans simplification, pour une
comparaison pixel à pixel avec les cartes simplifiées (écart toléré : 3 %).
"""
import json, math, os, sys, urllib.request
from shapely.geometry import shape, box, LineString, Point, MultiPolygon, Polygon
from shapely.ops import unary_union, split

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "cartes")
SOURCES = {
    "world_1930.geojson": "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/world_1930.geojson",
    "dep.geojson": "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson",
    "ligne.geojson": "https://departement-ain.opendata.arcgis.com/api/download/v1/items/73760b9eff0849f6afedc3d8b68b98ce/geojson?layers=5",
}

SEA, LAND, EDGE = "#DCE7EC", "#EFE8D8", "#B9AB89"
WINE, WINE_L, GOLD, GOLD_L, SLATE, GEO, GEO_L, BLUE = "#8E2F2A", "#E8C9C4", "#B8924F", "#EBDDB5", "#17233F", "#2C5F5B", "#CFDDD8", "#A9BED3"
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"


def charger(dossier):
    os.makedirs(dossier, exist_ok=True)
    out = {}
    for nom, url in SOURCES.items():
        p = os.path.join(dossier, nom)
        if not os.path.exists(p):
            urllib.request.urlretrieve(url, p)
        out[nom] = json.load(open(p, encoding="utf-8"))
    return out


class Carte:
    """Projection équirectangulaire recadrée, avec correction cos(latitude moyenne)."""

    def __init__(self, lon0, lon1, lat0, lat1, largeur=1000, corr=True):
        self.lon0, self.lon1, self.lat0, self.lat1 = lon0, lon1, lat0, lat1
        self.k = math.cos(math.radians((lat0 + lat1) / 2)) if corr else 1.0
        self.s = largeur / ((lon1 - lon0) * self.k)
        self.w, self.h = largeur, round((lat1 - lat0) * self.s)
        self.cadre = box(lon0, lat0, lon1, lat1)
        self.parts = []

    def xy(self, lon, lat):
        return ((lon - self.lon0) * self.k * self.s, (self.lat1 - lat) * self.s)

    def chemin(self, geom):
        d = []
        polys = [geom] if isinstance(geom, Polygon) else list(getattr(geom, "geoms", []))
        for p in polys:
            if not isinstance(p, Polygon) or p.is_empty:
                continue
            for ring in [p.exterior] + list(p.interiors):
                pts = [self.xy(x, y) for x, y in ring.coords]
                d.append("M" + "L".join("%.1f,%.1f" % q for q in pts) + "Z")
        return "".join(d)

    def ligne(self, coords):
        return "M" + "L".join("%.1f,%.1f" % self.xy(x, y) for x, y in coords)

    def zone(self, geom, fill, stroke=EDGE, sw=0.7, extra=""):
        g = geom.intersection(self.cadre)
        if not g.is_empty:
            self.parts.append('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" %s/>' % (self.chemin(g), fill, stroke, sw, extra))

    def trait(self, coords, stroke, sw=2, extra=""):
        self.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" %s/>' % (self.ligne(coords), stroke, sw, extra))

    def fleche(self, a, b, stroke=WINE, sw=2.6, courbe=0.18, dash=False):
        (x0, y0), (x1, y1) = self.xy(*a), self.xy(*b)
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        cx, cy = mx - (y1 - y0) * courbe, my + (x1 - x0) * courbe
        self.parts.append('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" %s marker-end="url(#pointe-%s)"/>'
                          % (x0, y0, cx, cy, x1, y1, stroke, sw, 'stroke-dasharray="7 5"' if dash else "", stroke.strip("#")))

    def texte(self, lon, lat, t, taille=13, poids=600, coul=SLATE, ancre="middle", italique=False, halo=True, dx=0, dy=0):
        x, y = self.xy(lon, lat)
        st = ' font-style="italic"' if italique else ""
        h = ' paint-order="stroke" stroke="#F7F3EA" stroke-width="3.2" stroke-linejoin="round"' if halo else ""
        lignes = t.split("\n")
        tsp = "".join('<tspan x="%.1f" dy="%s">%s</tspan>' % (x + dx, "0" if i == 0 else "1.15em", esc(l)) for i, l in enumerate(lignes))
        self.parts.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s"%s%s>%s</text>'
                          % (x + dx, y + dy, FONT, taille, poids, coul, ancre, st, h, tsp))

    def point(self, lon, lat, r=3.2, coul=SLATE):
        x, y = self.xy(lon, lat)
        self.parts.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s" stroke="#fff" stroke-width="1"/>' % (x, y, r, coul))

    def repere(self, lon, lat, n, dx=0, dy=0):
        """Pastille numérotée renvoyant à la légende ; dx/dy décalent la pastille avec un trait de rappel."""
        x, y = self.xy(lon, lat)
        X, Y = x + dx, y + dy
        if dx or dy:
            self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2"/>' % (x, y, X, Y, SLATE))
            self.point(lon, lat, 2.6)
        self.parts.append('<circle cx="%.1f" cy="%.1f" r="11.5" fill="%s" stroke="#fff" stroke-width="1.6"/><text x="%.1f" y="%.1f" font-family="%s" font-size="12.5" font-weight="700" fill="#fff" text-anchor="middle">%s</text>'
                          % (X, Y, SLATE, X, Y + 4.4, FONT, n))

    def svg(self, motifs=""):
        defs = "".join('<marker id="pointe-%s" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="%s"/></marker>' % (c.strip("#"), c) for c in (WINE, SLATE, GEO, GOLD))
        defs += ('<pattern id="hachures" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="%s"/><line x1="0" y1="0" x2="0" y2="7" stroke="%s" stroke-width="3"/></pattern>' % (WINE_L, WINE))
        defs += ('<pattern id="hachures-or" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="7" height="7" fill="%s"/><line x1="0" y1="0" x2="0" y2="7" stroke="%s" stroke-width="2.4"/></pattern>' % (GOLD_L, GOLD))
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%" role="img"><defs>%s%s</defs><rect width="%d" height="%d" fill="%s"/>%s<rect width="%d" height="%d" fill="none" stroke="%s" stroke-width="1.5"/></svg>'
                % (self.w, self.h, defs, motifs, self.w, self.h, SEA, "".join(self.parts), self.w, self.h, EDGE))


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def pays(data, tol):
    out = {}
    for ft in data["features"]:
        n = str(ft["properties"]["NAME"])
        g = shape(ft["geometry"]).buffer(0)
        if tol and not os.environ.get("SANS_SIMPLIF"):
            g = g.simplify(tol, preserve_topology=True)
        out[n] = unary_union([out[n], g]) if n in out else g
    return out


L = lambda en, fr: {"en": en, "fr": fr}


# ---------------------------------------------------------------- H1 : la crise devient mondiale
def carte_h1(D, lang):
    W = pays(D["world_1930.geojson"], 0.12)
    c = Carte(-130, 150, -46, 72, 1000, corr=False)
    for n, g in W.items():
        c.zone(g, LAND)
    fill = {"United States": WINE, "Germany": WINE_L, "Austria": WINE_L, "United Kingdom of Great Britain and Ireland": WINE_L, "France": WINE_L,
            "Brazil": GOLD_L, "Chile": GOLD_L, "White Russia": GEO_L, "Empire of Japan": BLUE, "Italy": BLUE}
    for n, f in fill.items():
        c.zone(W[n], f)
    c.zone(W["Manchuria"], "url(#hachures)")
    c.zone(W["Ethiopia"], "url(#hachures)")
    # flux et agressions
    c.fleche((-74, 40.7), (13.4, 52.5), WINE, 2.4, -0.12, dash=True)
    c.texte(-30, 58, L("American loans recalled, 1929–31", "Rappel des prêts américains, 1929-31")[lang], 12, 600, WINE, italique=True)
    c.fleche((131, 36), (124, 43.5), WINE, 3, 0.25)
    c.fleche((12.5, 42), (38, 10), WINE, 3, -0.2)
    lab = {"en": [("USA", -100, 39), ("BRAZIL", -52, -11), ("CHILE", -76.5, -30), ("USSR", 85, 62), ("JAPAN", 141, 39.5), ("MANCHURIA", 126, 49.5), ("ETHIOPIA", 40.5, 2.0), ("CANADA", -103, 58)],
           "fr": [("ÉTATS-UNIS", -100, 39), ("BRÉSIL", -52, -11), ("CHILI", -76.5, -30), ("URSS", 85, 62), ("JAPON", 141, 39.5), ("MANDCHOURIE", 126, 49.5), ("ÉTHIOPIE", 40.5, 2.0), ("CANADA", -103, 58)]}[lang]
    for t, x, y in lab:
        c.texte(x, y, t, 11.5, 700, SLATE)
    # repères numérotés (légende dans la fiche)
    for n, (x, y, dx, dy) in enumerate([(-74, 40.7, 16, 22), (-75.7, 45.4, -22, -24), (16.4, 48.2, 30, 34), (-0.1, 51.5, -34, -10), (13.4, 52.5, 6, -38),
                                        (2.35, 48.86, -36, 26), (-47, -15, 0, 0), (-70, -27, 26, 0), (37.6, 55.75, 0, 0), (123.4, 41.8, -30, 22), (38.7, 9.0, 36, 6)], 1):
        c.repere(x, y, n, dx, dy)
    return c.svg()


# ---------------------------------------------------------------- H2 : l'Europe des régimes et la route de la guerre
def carte_h2(D, lang):
    W = pays(D["world_1930.geojson"], 0.03)
    c = Carte(-10.5, 40, 35.5, 60.5, 1000)
    for n, g in W.items():
        c.zone(g, LAND)
    fasc = ["Germany", "East Prussia", "Italy"]
    demo = ["United Kingdom of Great Britain and Ireland", "France", "Belgium", "Netherlands", "Luxembourg", "Switzerland", "Czechoslovakia", "Denmark", "Norway", "Sweden", "Finland", "Iceland"]
    auto = ["Portugal", "Poland", "Austria", "Hungary", "Romania", "Yugoslavia", "Bulgaria", "Greece", "Albania", "Estonia", "Latvia", "Lithuania", "Turkey", "Republic of Turkey"]
    for n in demo:
        c.zone(W[n], BLUE)
    for n in auto:
        if n in W:
            c.zone(W[n], GOLD_L)
    c.zone(W["Spain"], "url(#hachures-or)")
    c.zone(W["White Russia"], "#D9A79C")
    for n in fasc:
        c.zone(W[n], WINE, "#fff", 0.8)
    # Rhénanie démilitarisée (zone schématique à l'ouest du Rhin)
    rh = Polygon([(6.0, 49.1), (8.2, 49.0), (8.3, 49.6), (7.6, 50.3), (6.9, 51.2), (6.3, 51.9), (5.9, 51.0), (6.2, 50.3), (6.4, 49.5)]).intersection(W["Germany"])
    c.zone(rh, "url(#hachures)", "#fff", 0.6)
    # flèches d'expansion
    for a, b, k in [((10.5, 50.3), (7.0, 50.4), 0.2), ((12.6, 48.6), (15.6, 48.0), -0.25), ((12.2, 51.2), (14.6, 50.7), -0.3), ((13.0, 51.6), (15.6, 49.9), -0.3), ((14.0, 52.6), (19.5, 52.3), -0.15)]:
        c.fleche(a, b, "#F7F3EA", 4.6, k)
        c.fleche(a, b, SLATE, 2.6, k)
    c.fleche((15.5, 40.5), (19.0, 35.6), WINE, 3, -0.15)
    c.texte(19.6, 36.3, L("to Ethiopia, Oct. 1935", "vers l'Éthiopie, oct. 1935")[lang], 12, 600, WINE, "start", italique=True)
    c.fleche((10.5, 47.2), (0.5, 41.8), WINE, 2, 0.12, dash=True)
    c.fleche((12.0, 42.5), (-0.6, 39.6), WINE, 2, 0.1, dash=True)
    lab = {"en": [("GERMANY", 9.7, 51.9), ("ITALY", 12.6, 43.0), ("FRANCE", 2.2, 46.9), ("UNITED\nKINGDOM", -2.3, 53.1), ("SPAIN", -4.2, 39.4), ("USSR", 33, 54.5), ("POLAND", 20.5, 51.2), ("CZECHOSLOVAKIA", 18.6, 49.0)],
           "fr": [("ALLEMAGNE", 9.7, 51.9), ("ITALIE", 12.6, 43.0), ("FRANCE", 2.2, 46.9), ("ROYAUME-\nUNI", -2.3, 53.1), ("ESPAGNE", -4.2, 39.4), ("URSS", 33, 54.5), ("POLOGNE", 20.5, 51.2), ("TCHÉCOSLOVAQUIE", 18.6, 49.0)]}[lang]
    for t, x, y in lab:
        c.texte(x, y, t, 12, 700, SLATE)
    pts = [(6.9, 50.4, -34, -6), (8.55, 45.9, -30, 10), (16.37, 48.21, 26, 18), (11.58, 48.14, -10, 30), (13.6, 50.55, -18, -32), (14.42, 50.08, 34, -10),
           (19.5, 52.3, 0, -28), (37.6, 55.75, 0, -22), (-3.7, 40.4, 26, -24), (2.35, 48.86, 0, 0), (-0.1, 51.5, 22, 18)]
    for n, (x, y, dx, dy) in enumerate(pts, 1):
        c.repere(x, y, n, dx, dy)
    return c.svg()


# ---------------------------------------------------------------- H3 : la France découpée (1940-1942)
def carte_h3(D, lang):
    W = pays(D["world_1930.geojson"], 0.01)
    deps = {ft["properties"]["code"]: shape(ft["geometry"]).buffer(0) for ft in D["dep.geojson"]["features"]}
    france = unary_union(list(deps.values())).buffer(0.002).buffer(-0.002)
    ligne = D["ligne.geojson"]["features"][0]["geometry"]["coordinates"]
    # prolonger les deux bouts hors du territoire pour couper le polygone
    a, b = ligne[0], ligne[-1]
    est, ouest = (a, b) if a[0] > b[0] else (b, a)
    coupe = LineString([(est[0] + 0.6, est[1] + 0.05)] + [tuple(p[:2]) for p in (ligne if ligne[0] == est else ligne[::-1])] + [(ouest[0] - 0.05, ouest[1] - 0.6)])
    morceaux = sorted(split(france, coupe).geoms, key=lambda g: -g.area)
    paris = Point(2.35, 48.86)
    occ = unary_union([g for g in morceaux if g.distance(paris) < 0.01 or g.centroid.y > 46.9 or (g.centroid.x < -0.3 and g.area < 1)])
    libre = unary_union([g for g in morceaux if not g.equals(occ) and not occ.contains(g.representative_point())])
    annex = unary_union([deps[k] for k in ("57", "67", "68")])
    nord = unary_union([deps[k] for k in ("59", "62")])
    c = Carte(-5.3, 9.6, 41.3, 51.35, 1000)
    for n, g in W.items():
        c.zone(g, LAND)
    c.zone(libre, GEO_L, EDGE, 0.8)
    c.zone(occ.difference(annex).difference(nord), WINE_L, EDGE, 0.8)
    c.zone(nord, GOLD_L, EDGE, 0.8)
    c.zone(annex, WINE, "#fff", 0.8)
    for g in deps.values():
        c.zone(g, "none", "#FFFFFF", 0.35, 'stroke-opacity="0.55"')
    c.zone(france, "none", "#8C7E5E", 1.1)
    # ligne Maginot : frontière franco-allemande et franco-luxembourgeoise
    fr = france.buffer(0.01)
    mag = fr.boundary.intersection(unary_union([W["Germany"], W["Luxembourg"]]).buffer(0.06))
    for seg in getattr(mag, "geoms", [mag]):
        if seg.length > 0.05:
            c.trait(list(seg.coords), SLATE, 4.2, 'stroke-dasharray="2 4"')
    c.trait([tuple(p[:2]) for p in ligne], "#F7F3EA", 5.5)
    c.trait([tuple(p[:2]) for p in ligne], SLATE, 2.6, 'stroke-dasharray="9 5"')
    # percée des Ardennes et avance alliée en Belgique
    c.fleche((5.9, 50.15), (4.95, 49.65), WINE, 3.4, 0.0)
    c.fleche((4.95, 49.62), (1.75, 50.1), WINE, 3.4, -0.18)
    c.fleche((3.1, 50.6), (4.35, 50.85), GEO, 2.4, -0.25, dash=True)
    c.texte(-0.6, 50.45, L("Panzer breakthrough\n13–20 May 1940", "Percée des blindés\n13-20 mai 1940")[lang], 12, 700, WINE, italique=True)
    lab = {"en": [("OCCUPIED ZONE", -0.2, 48.1), ("“FREE ZONE”", 1.6, 44.9), ("SPAIN", -3.6, 42.0), ("SWITZERLAND", 8.0, 46.75), ("ITALY", 8.6, 45.2), ("GERMANY", 8.9, 49.7), ("BELGIUM", 4.4, 51.1), ("UNITED KINGDOM", -2.8, 51.05)],
           "fr": [("ZONE OCCUPÉE", -0.2, 48.1), ("« ZONE LIBRE »", 1.6, 44.9), ("ESPAGNE", -3.6, 42.0), ("SUISSE", 8.0, 46.75), ("ITALIE", 8.6, 45.2), ("ALLEMAGNE", 8.9, 49.7), ("BELGIQUE", 4.4, 51.1), ("ROYAUME-UNI", -2.8, 51.05)]}[lang]
    for t, x, y in lab:
        c.texte(x, y, t, 13 if "ZONE" in t else 11.5, 700, SLATE)
    pts = [(2.38, 51.03, -30, -8), (4.95, 49.70, 26, 16), (2.35, 48.86, -32, 16), (2.90, 49.42, 30, 20), (3.43, 46.13, 28, 4), (7.45, 43.80, 26, 18), (7.5, 48.4, 30, 0), (2.8, 50.45, -32, 12)]
    for n, (x, y, dx, dy) in enumerate(pts, 1):
        c.repere(x, y, n, dx, dy)
    return c.svg()


if __name__ == "__main__":
    D = charger(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, ".donnees"))
    os.makedirs(SORTIE, exist_ok=True)
    import europe
    E = europe.charger_eu(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, ".donnees"))
    ecrire = lambda nom, s: (open(os.path.join(SORTIE, nom), "w", encoding="utf-8").write(s), print(nom, len(s) // 1024, "Ko"))
    for lang in ("en", "fr"):
        # grandes cartes : H1 le monde, H2 et H3 l'Europe ; H3 garde aussi le zoom sur la France
        ecrire("H1-%s.svg" % lang, carte_h1(D, lang))
        ecrire("H2-%s.svg" % lang, europe.h2_grande(D, E, lang))
        ecrire("H3-%s.svg" % lang, europe.h3_grande(D, E, lang))
        ecrire("H3-france-%s.svg" % lang, carte_h3(D, lang))
        # séries de petites cartes datées (sans texte propre à la langue, sauf quelques noms)
        for code, serie in (("H1", europe.h1_serie(D, lang)), ("H2", europe.h2_serie(D, E, lang)), ("H3", europe.h3_serie(D, E, lang))):
            for i, s in enumerate(serie, 1):
                ecrire("%s-serie%d-%s.svg" % (code, i, lang), s)
