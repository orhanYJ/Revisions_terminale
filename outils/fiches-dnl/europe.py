"""Cartes d'évolution de l'Europe pour les fiches DNL : une série de petites cartes datées
et une grande carte où chaque territoire est coloré selon l'année du changement.

Frontières assemblées à partir de trois sources (téléchargées par cartes.py) :
- historical-basemaps, world_1930 : la carte de départ ;
- CShapes 2.0 (ETH Zurich, ICR) : changements datés de jure (Sudètes 1938, Carélie mars 1940,
  Bessarabie et Bucovine du Nord juin 1940, Vilnius octobre 1939) ;
- Natural Earth : Sarre (Saarland actuel), Bohême-Moravie (Tchéquie actuelle, Sudètes ôtées),
  partage de la Pologne (frontière orientale actuelle, plus la Podlachie côté soviétique).
Les deux derniers tracés sont des approximations, signalées dans la légende.
"""
import json, os, datetime as dt
from shapely.geometry import shape, Polygon, LineString, Point
from shapely.ops import unary_union, split
from cartes import Carte, esc, SEA, LAND, EDGE, SLATE, FONT

SOURCES_EU = {
    "cshapes.geojson": "https://icr.ethz.ch/data/cshapes/CShapes-2.0.geojson",
    "ne_50m_admin_0_countries.geojson": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson",
    "ne_10m_admin_1_states_provinces.geojson": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson",
}

# palette : l'Allemagne et ses prises en rouge sombre → clair selon l'année ; l'Italie en brun doré
G33, G35, G38, G39, G40 = "#5E1C19", "#8E2F2A", "#B8564C", "#D88A80", "#EDBDB5"
IT, IT2 = "#8E6F37", "#CDAE6F"
USSR, USSR2 = "#6F7E99", "#AEB8CB"
DEMO, AUTO, NEUTRE, UK = "#C3D3E2", "#EFE3C4", "#E3DED2", "#5F86AD"
ALLIE = "#E2C88E"


def charger_eu(dossier):
    import urllib.request
    out = {}
    for nom, url in SOURCES_EU.items():
        p = os.path.join(dossier, nom)
        if not os.path.exists(p):
            urllib.request.urlretrieve(url, p)
        out[nom] = json.load(open(p, encoding="utf-8"))
    return out


def regions(D, E, tol=0.02):
    """Toutes les zones nécessaires, en coordonnées géographiques, simplifiées à tol degrés."""
    simp = lambda g: g.buffer(0).simplify(tol, preserve_topology=True) if tol and not os.environ.get("SANS_SIMPLIF") else g.buffer(0)
    W = {}
    for ft in D["world_1930.geojson"]["features"]:
        n = str(ft["properties"]["NAME"])
        W.setdefault(n, []).append(shape(ft["geometry"]).buffer(0))
    W = {k: unary_union(v) for k, v in W.items()}
    jour = lambda s: dt.datetime.strptime(s.split()[0], "%d.%m.%Y").date() + dt.timedelta(days=1)
    CS = {}
    for ft in E["cshapes.geojson"]["features"]:
        p = ft["properties"]
        CS[(p["cntry_name"], jour(p["gwsdate"]).isoformat())] = shape(ft["geometry"]).buffer(0)
    ne0 = {ft["properties"]["ADMIN"]: shape(ft["geometry"]).buffer(0) for ft in E["ne_50m_admin_0_countries.geojson"]["features"]}
    ne1 = {}
    for ft in E["ne_10m_admin_1_states_provinces.geojson"]["features"]:
        p = ft["properties"]
        if p.get("admin") in ("Germany", "Poland"):
            ne1[p["name"]] = shape(ft["geometry"]).buffer(0)
    R = {}
    R["saar"] = ne1["Saarland"]
    R["germany"] = unary_union([W["Germany"], W["East Prussia"]]).difference(R["saar"])
    R["austria"] = W["Austria"]
    ger_av, ger_ap = CS[("Germany (Prussia)", "1920-02-10")], CS[("Germany (Prussia)", "1938-09-30")]
    R["sudetes"] = ger_ap.difference(ger_av).buffer(-0.005).buffer(0.005).intersection(W["Czechoslovakia"].buffer(0.02))
    R["boheme"] = ne0["Czechia"].intersection(W["Czechoslovakia"]).difference(R["sudetes"])
    R["slovaquie"] = W["Czechoslovakia"].difference(R["sudetes"]).difference(R["boheme"])
    R["danzig"] = W["Danzig"]
    pol_ouest = ne0["Poland"].difference(ne1["Podlachian"])
    R["pologne_all"] = W["Poland"].intersection(pol_ouest.buffer(0.01))
    lit_av, lit_ap = CS[("Lithuania", "1922-04-18")], CS[("Lithuania", "1939-10-01")]
    R["vilnius"] = lit_ap.difference(lit_av).intersection(W["Poland"].buffer(0.02))
    R["pologne_urss"] = W["Poland"].difference(R["pologne_all"]).difference(R["vilnius"])
    R["baltes"] = unary_union([W["Estonia"], W["Latvia"], W["Lithuania"], R["vilnius"]])
    R["bessarabie"] = CS[("Rumania", "1920-10-28")].difference(CS[("Rumania", "1940-06-28")])
    R["carelie"] = CS[("Finland", "1917-12-06")].difference(CS[("Finland", "1940-03-12")])
    R["finlande"] = W["Finland"].difference(R["carelie"])
    R["roumanie"] = W["Romania"].difference(R["bessarabie"])
    R["urss"] = unary_union([W["White Russia"], W["Armenia"], W["Georgia"], W["Azerbaijan"]])
    R["italie"] = unary_union([W["Italy"], W["Dodecanese Islands"]])
    R["albanie"] = W["Albania"]
    R["irlande"] = ne0["Ireland"]
    R["ru"] = W["United Kingdom of Great Britain and Ireland"].difference(R["irlande"].buffer(0.02))
    R["france"] = W["France"].difference(R["saar"])
    R["turquie"] = unary_union([W["Republic of Turkey"], W["Turkey"]])
    for n in ("Spain", "Portugal", "Switzerland", "Sweden", "Norway", "Denmark", "Netherlands", "Belgium", "Luxembourg",
              "Hungary", "Yugoslavia", "Bulgaria", "Greece", "Iceland"):
        R[n.lower()] = W[n]
    R["fond"] = unary_union([g for k, g in W.items() if k not in ("None",)])
    return {k: simp(v) for k, v in R.items()}


def zones_france(D):
    """Zone occupée, zone libre et Alsace-Moselle (1940), à partir des départements et de la ligne de démarcation."""
    deps = {ft["properties"]["code"]: shape(ft["geometry"]).buffer(0) for ft in D["dep.geojson"]["features"]}
    france = unary_union(list(deps.values())).buffer(0.002).buffer(-0.002)
    ligne = D["ligne.geojson"]["features"][0]["geometry"]["coordinates"]
    a, b = ligne[0], ligne[-1]
    est, ouest = (a, b) if a[0] > b[0] else (b, a)
    pts = [tuple(p[:2]) for p in (ligne if ligne[0] == est else ligne[::-1])]
    coupe = LineString([(est[0] + 0.6, est[1] + 0.05)] + pts + [(ouest[0] - 0.05, ouest[1] - 0.6)])
    morceaux = list(split(france, coupe).geoms)
    occ = unary_union([g for g in morceaux if g.distance(Point(2.35, 48.86)) < 0.01 or g.centroid.y > 46.9 or (g.centroid.x < -0.3 and g.area < 1)])
    libre = france.difference(occ)
    annex = unary_union([deps[k] for k in ("57", "67", "68")])
    return {"occupee": occ.difference(annex), "libre": libre, "annexee": annex}


def _base(c, R, couleurs, defaut=LAND, sw=0.6):
    c.zone(R["fond"], defaut, EDGE, sw)
    for k, f in couleurs.items():
        if f:
            c.zone(R[k] if isinstance(k, str) else k, f, "#FFFFFF" if f in (G33, G35, G38, IT, USSR, UK) else EDGE, sw)


def _motifs(suffixe):
    """Hachures propres à une carte (identifiants uniques quand plusieurs cartes sont dans la même page)."""
    m = lambda i, fond, trait, ang: f'<pattern id="{i}-{suffixe}" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate({ang})"><rect width="7" height="7" fill="{fond}"/><line x1="0" y1="0" x2="0" y2="7" stroke="{trait}" stroke-width="2.6"/></pattern>'
    return m("rh", "#F2E3E0", G35, 45) + m("es", AUTO, "#B8924F", -45) + m("su", USSR2, USSR, 45) + m("vi", "#F6E7E3", G38, -45)


def _h(c, nom, suffixe):
    return f"url(#{nom}-{suffixe})"


def _rhenanie(R):
    return Polygon([(6.0, 49.1), (8.2, 49.0), (8.3, 49.6), (7.6, 50.3), (6.9, 51.2), (6.3, 51.9), (5.9, 51.0), (6.2, 50.3), (6.4, 49.5)]).intersection(R["germany"])


EXT_H2 = (-10.5, 40, 35, 60.5)
EXT_H3 = (-10.5, 50, 35, 65.5)

# lignes de front sur le front de l'Est (tracés simplifiés, du nord au sud) : 5 décembre 1941 et 18 novembre 1942
F41 = [(29.6, 59.9), (30.8, 59.7), (31.1, 59.95), (33.5, 59.65), (32.3, 58.8), (31.3, 58.5), (31.9, 57.9), (33.1, 57.2), (35.9, 56.85), (37.1, 56.4),
       (37.45, 56.05), (36.9, 55.6), (36.7, 55.38), (37.1, 54.9), (37.4, 54.3), (38.0, 54.1), (38.4, 53.4), (38.5, 52.6), (37.3, 51.7), (37.6, 50.6),
       (37.7, 49.5), (38.2, 48.3), (38.9, 47.25)]
F42 = [(29.6, 59.9), (30.8, 59.7), (31.1, 59.95), (32.2, 59.2), (31.5, 58.6), (32.0, 58.0), (33.4, 57.9), (32.6, 57.3), (34.0, 56.6), (35.0, 56.2),
       (35.3, 55.6), (35.0, 55.0), (34.5, 54.4), (35.6, 53.6), (36.6, 53.0), (37.5, 52.3), (38.5, 51.9), (39.2, 51.66), (40.0, 50.6), (41.3, 50.0),
       (42.5, 49.6), (43.4, 49.3), (44.0, 48.9), (44.5, 48.75), (44.3, 47.8), (44.6, 46.5), (45.0, 45.3), (44.6, 43.8), (43.7, 43.5), (42.0, 43.3),
       (40.5, 43.9), (39.3, 44.2), (38.9, 44.35)]


def occupation_est(R):
    """Territoire soviétique (frontières de juin 1941) à l'ouest du front de novembre 1942."""
    ouest = Polygon(F42 + [(38.9, 43.0), (20.0, 43.0), (20.0, 61.5), (29.6, 61.5)])
    sov = unary_union([R["urss"], R["pologne_urss"], R["baltes"], R["bessarabie"], R["carelie"]])
    return sov.intersection(ouest).buffer(0)


def h2_etat(R, etape, suffixe):
    """Couleurs de l'Europe à une étape du H2 (1933, 1936, 1938, 1939)."""
    col = {}
    for k in ("ru", "irlande", "france", "belgium", "netherlands", "luxembourg", "switzerland", "denmark", "norway", "sweden", "finlande", "carelie", "iceland"):
        col[k] = DEMO
    for k in ("portugal", "spain", "hungary", "roumanie", "bessarabie", "yugoslavia", "bulgaria", "greece", "albanie", "baltes", "turquie", "austria", "pologne_all", "pologne_urss", "danzig"):
        col[k] = AUTO
    col["boheme"] = col["slovaquie"] = col["sudetes"] = DEMO
    col["urss"] = USSR
    col["italie"] = IT
    col["germany"] = G33
    col["saar"] = NEUTRE if etape == 1933 else G35
    if etape >= 1936:
        col["spain"] = _h(None, "es", suffixe)
    if etape >= 1938:
        col["austria"] = G38
        col["sudetes"] = G38
    if etape >= 1939:
        col["boheme"] = G39
        col["danzig"] = col["pologne_all"] = G39
        col["pologne_urss"] = _h(None, "su", suffixe)
        col["albanie"] = IT2
        col["spain"] = AUTO
        col["slovaquie"] = ALLIE
    return col


def h2_serie(D, E, lang):
    R = regions(D, E, 0.06)
    out = []
    lab = {"en": {"G": "Germany", "I": "Italy", "U": "USSR"}, "fr": {"G": "Allemagne", "I": "Italie", "U": "URSS"}}[lang]
    for etape in (1933, 1936, 1938, 1939):
        suf = f"h2s{etape}"
        c = Carte(*EXT_H2, 420)
        _base(c, R, h2_etat(R, etape, suf))
        if etape >= 1936:
            c.zone(_rhenanie(R), _h(None, "rh", suf), "#fff", 0.5)
        c.texte(10.5, 51.6, lab["G"], 15, 700, "#fff", halo=False)
        c.texte(13.2, 42.6, lab["I"], 14, 700, "#fff", halo=False)
        c.texte(33, 55, lab["U"], 15, 700, "#fff", halo=False)
        out.append(c.svg(_motifs(suf)))
    return out


def h2_grande(D, E, lang):
    R = regions(D, E, 0.02)
    suf = "h2g"
    c = Carte(*EXT_H2, 1000)
    col = h2_etat(R, 1939, suf)
    col["spain"] = _h(None, "es", suf)
    _base(c, R, col, sw=0.8)
    c.zone(_rhenanie(R), _h(None, "rh", suf), "#fff", 0.6)
    F = lang == "fr"
    for a, b, k in [((10.5, 50.3), (7.0, 50.4), 0.2), ((12.6, 48.6), (15.6, 48.0), -0.25), ((12.2, 51.2), (14.4, 50.7), -0.3),
                    ((13.0, 51.8), (16.2, 49.7), -0.3), ((14.0, 52.8), (19.5, 52.4), -0.15), ((15.0, 53.6), (18.6, 54.3), -0.2)]:
        c.fleche(a, b, "#F7F3EA", 4.8, k)
        c.fleche(a, b, SLATE, 2.6, k)
    c.fleche((37.5, 55.5), (25.5, 52.2), USSR, 3, 0.2)
    c.fleche((15.5, 40.5), (19.5, 35.4), IT, 3, -0.15)
    c.fleche((14.2, 41.6), (19.6, 41.3), IT, 2.6, -0.2)
    c.fleche((10.5, 47.2), (0.5, 41.8), G38, 2, 0.12, dash=True)
    c.fleche((12.0, 42.5), (-0.6, 39.6), IT, 2, 0.1, dash=True)
    c.texte(20.0, 35.9, "→ " + ("Éthiopie, oct. 1935" if F else "Ethiopia, Oct. 1935"), 12, 700, IT, "start", italique=True)
    labs = [("ALLEMAGNE" if F else "GERMANY", 9.6, 52.4, "#fff"), ("ITALIE" if F else "ITALY", 13.0, 42.7, "#fff"), ("URSS" if F else "USSR", 33, 55.6, "#fff"),
            ("FRANCE", 2.2, 46.9, SLATE), ("ROYAUME-\nUNI" if F else "UNITED\nKINGDOM", -2.4, 53.2, SLATE), ("ESPAGNE" if F else "SPAIN", -4.2, 39.6, SLATE),
            ("AUTRICHE" if F else "AUSTRIA", 14.6, 47.45, "#fff"), ("POLOGNE" if F else "POLAND", 19.6, 51.4, SLATE)]
    for t, x, y, co in labs:
        c.texte(x, y, t, 12, 700, co, halo=co == SLATE)
    pts = [(7.0, 49.35, -36, 14), (6.9, 50.5, -34, -10), (16.37, 48.21, 30, 22), (13.6, 50.55, -20, -34), (15.2, 49.7, 30, 22),
           (18.65, 54.35, 18, -26), (20.5, 52.5, 10, -30), (25.5, 52.0, 26, 22), (37.6, 55.75, 0, -24), (20.0, 41.2, 34, 18), (-3.7, 40.4, 26, -24), (11.58, 48.14, -30, 24)]
    for n, (x, y, dx, dy) in enumerate(pts, 1):
        c.repere(x, y, n, dx, dy)
    return c.svg(_motifs(suf))


def h3_etat(R, Z, etape, suffixe):
    """Couleurs de l'Europe à une étape du H3 : 1939 (octobre), 1940 (juillet), 1941 (mai), 1942 (novembre, avancée maximale à l'Est)."""
    col = {}
    for k in ("portugal", "spain", "switzerland", "sweden", "irlande", "turquie", "iceland", "finlande"):
        col[k] = NEUTRE
    for k in ("hungary", "roumanie", "bulgaria", "yugoslavia", "greece", "bessarabie"):
        col[k] = NEUTRE
    for k in ("france", "belgium", "netherlands", "luxembourg", "denmark", "norway"):
        col[k] = DEMO
    col["ru"] = UK
    col["urss"] = USSR
    col["baltes"] = NEUTRE
    col["carelie"] = NEUTRE
    for k in ("germany", "saar", "austria", "sudetes", "boheme", "danzig"):
        col[k] = G33
    col["pologne_all"] = G38
    col["pologne_urss"] = _h(None, "su", suffixe)
    col["slovaquie"] = ALLIE
    col["italie"] = IT
    col["albanie"] = IT
    if etape >= 1940:
        for k in ("belgium", "netherlands", "luxembourg", "denmark", "norway"):
            col[k] = G38
        col["france"] = None
        col[Z["occupee"]] = G38
        col[Z["annexee"]] = G33
        col[Z["libre"]] = _h(None, "vi", suffixe)
        col["baltes"] = col["bessarabie"] = col["carelie"] = _h(None, "su", suffixe)
    if etape >= 1941:
        col["yugoslavia"] = col["greece"] = G38
        col["hungary"] = col["roumanie"] = col["bulgaria"] = ALLIE
    if etape >= 1942:
        col["finlande"] = ALLIE
        col[occupation_est(R)] = G38
    return col


def h3_serie(D, E, lang):
    R = regions(D, E, 0.06)
    Z = {k: v.simplify(0.04) for k, v in zones_france(D).items()}
    out = []
    lab = {"en": ("Germany", "USSR", "UK"), "fr": ("Allemagne", "URSS", "R.-U.")}[lang]
    for etape in (1939, 1940, 1941, 1942):
        suf = f"h3s{etape}"
        c = Carte(*EXT_H3, 420)
        _base(c, R, h3_etat(R, Z, etape, suf))
        if etape >= 1942:
            c.trait(F42, "#2B0E0C", 2.2)
        c.texte(10.6, 51.6, lab[0], 15, 700, "#fff", halo=False)
        c.texte(43.5, 57, lab[1], 15, 700, "#fff", halo=False)
        c.texte(-1.6, 53.0, lab[2], 13, 700, "#fff", halo=False)
        out.append(c.svg(_motifs(suf)))
    return out


def h3_grande(D, E, lang):
    R = regions(D, E, 0.02)
    Z = zones_france(D)
    suf = "h3g"
    c = Carte(*EXT_H3, 1000)
    _base(c, R, h3_etat(R, Z, 1942, suf), sw=0.8)
    F = lang == "fr"
    c.trait(F41, "#F7F3EA", 5)
    c.trait(F41, "#2B0E0C", 2.4, 'stroke-dasharray="8 5"')
    c.trait(F42, "#F7F3EA", 5.5)
    c.trait(F42, "#2B0E0C", 3)
    for a, b, k in [((22.0, 54.6), (29.4, 59.0), -0.15), ((23.5, 52.6), (35.6, 55.4), -0.08), ((24.0, 50.6), (37.0, 48.6), 0.1), ((37.5, 49.5), (43.6, 48.9), -0.15), ((39.5, 47.0), (43.5, 44.4), 0.15)]:
        c.fleche(a, b, "#F7F3EA", 5.4, k)
        c.fleche(a, b, "#2B0E0C", 3, k)
    for a, b, k in [((13.5, 52.6), (20.5, 52.0), -0.15), ((10.0, 54.3), (10.5, 56.8), 0.2), ((10.4, 54.6), (9.5, 60.8), -0.25),
                    ((7.3, 51.6), (5.4, 52.2), 0.2), ((6.6, 50.6), (4.6, 50.7), -0.2), ((6.3, 49.8), (2.4, 48.5), 0.15), ((14.5, 46.6), (19.8, 44.4), -0.2), ((22.4, 42.2), (22.6, 39.3), -0.2)]:
        c.fleche(a, b, "#F7F3EA", 4.8, k)
        c.fleche(a, b, SLATE, 2.6, k)
    labs = [("ALLEMAGNE" if F else "GERMANY", 10.4, 51.9, "#fff"), ("ITALIE" if F else "ITALY", 13.0, 42.7, "#fff"), ("URSS" if F else "USSR", 44.5, 58.0, "#fff"),
            ("ROYAUME-\nUNI" if F else "UNITED\nKINGDOM", -2.4, 53.2, "#fff"), ("ESPAGNE" if F else "SPAIN", -4.2, 39.6, SLATE), ("SUÈDE" if F else "SWEDEN", 15.3, 62.5, SLATE),
            ("VICHY", 2.2, 45.1, SLATE), ("TURQUIE" if F else "TURKEY", 33.5, 39.4, SLATE), ("FINLANDE" if F else "FINLAND", 26.5, 63.2, SLATE)]
    for t, x, y, co in labs:
        c.texte(x, y, t, 12, 700, co, halo=co == SLATE)
    pts = [(20.5, 52.0, 0, -30), (10.0, 56.2, -30, -14), (9.5, 60.8, -32, 0), (5.6, 52.2, -30, -16), (2.4, 48.6, -34, 6), (-0.8, 52.0, -30, 22),
           (25.3, 56.3, 28, -8), (28.6, 47.2, 30, 14), (19.8, 44.3, 26, 22), (22.5, 39.3, 28, 12), (25.0, 45.6, 20, -26), (2.4, 45.6, -30, 24),
           (30.3, 59.93, 24, -20), (37.6, 55.75, 26, -14), (44.5, 48.7, 24, -18), (30.5, 52.0, 0, 0)]
    for n, (x, y, dx, dy) in enumerate(pts, 1):
        c.repere(x, y, n, dx, dy)
    return c.svg(_motifs(suf))


def h1_serie(D, lang):
    """Le monde de la crise en quatre temps : 1929, 1931, 1933, 1935-37 (frontières de 1930)."""
    from cartes import pays, WINE, WINE_L, GOLD_L, GEO_L, BLUE
    W = pays(D["world_1930.geojson"], 0.35)
    out = []
    for etape in (1929, 1931, 1933, 1937):
        suf = f"h1s{etape}"
        c = Carte(-130, 150, -46, 72, 420, corr=False)
        for g in W.values():
            c.zone(g, LAND, EDGE, 0.4)
        col = {"United States": WINE, "White Russia": GEO_L}
        if etape >= 1931:
            col.update({"Germany": WINE_L, "Austria": WINE_L, "United Kingdom of Great Britain and Ireland": WINE_L, "Brazil": GOLD_L, "Chile": GOLD_L, "Empire of Japan": BLUE})
        if etape >= 1933:
            col.update({"France": WINE_L, "Germany": BLUE, "Italy": BLUE})
        for n, f in col.items():
            c.zone(W[n], f, EDGE, 0.4)
        if etape >= 1931:
            c.zone(W["Manchuria"], f"url(#rh-{suf})", EDGE, 0.4)
        if etape >= 1937:
            c.zone(W["Ethiopia"], f"url(#rh-{suf})", EDGE, 0.4)
            c.fleche((133, 34), (115, 31), WINE, 2.2, 0.25)
        if etape == 1929:
            c.fleche((-74, 40.7), (13.4, 52.5), WINE, 1.8, -0.12, dash=True)
        out.append(c.svg(_motifs(suf)))
    return out
