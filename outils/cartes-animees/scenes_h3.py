"""Scènes de la carte animée H3 « World War Two » (cours de M. Ros, introduction à II.2, jusqu'au 2 février 1943).
Content gate : seulement ce qui a été vu en classe ; ce qui vient d'ailleurs porte la balise [hors].
Caméra : [longitude, latitude, zoom] (zoom 1 = globe entier dans la hauteur de la carte).
st : couleurs cumulatives par pièce, [remplissage, couleur des hachures] (None = rien).
"""

TITRE = {"fr": "La Seconde Guerre mondiale, 1931-1943 : la carte animée", "en": "World War Two, 1931–1943: the animated map"}
PARTIES = {
    "Intro": {"fr": "Une guerre-monde", "en": "A world war"},
    "I.1": {"fr": "L'invasion de l'Europe de l'Ouest : le cas français", "en": "Nazi invasion of Western Europe: the French case"},
    "I.2": {"fr": "La résistance britannique soutenue par les États-Unis", "en": "The British resistance supported by the US"},
    "II.1": {"fr": "Les projets allemands pour l'Europe de l'Est", "en": "German plans for Eastern Europe"},
    "II.2": {"fr": "Barbarossa : une guerre d'anéantissement", "en": "Barbarossa: a war of annihilation"},
    "Bilan": {"fr": "Le Nouvel Ordre européen en 1942", "en": "The New European Order in 1942"},
}

# palette (celle des fiches PDF)
G33, G38, IT, USSR, USSR2 = "#5E1C19", "#B8564C", "#8E6F37", "#6F7E99", "#AEB8CB"
DEMO, NEUTRE, UK, ALLIE = "#C3D3E2", "#E3DED2", "#5F86AD", "#E2C88E"
JAP, USA, VICHY = "#9A6A3A", "#4F7CA6", "#F6E7E3"
ROUGE, BLEU, VERT, NOIR = "#8E2F2A", "#2F4F7F", "#3E6259", "#2B0E0C"
OCC = G38

SU = [USSR2, USSR]          # pris par l'URSS (hachures)
OVERLAY = ["fr_occ", "fr_nord", "fr_annex", "fr_libre", "fr_ital", "sov41", "rhenanie", "dustbowl", "ukraine32"]

CLES = {
    "reich": {"c": [G33, None], "fr": "Reich", "en": "The Reich"},
    "occ": {"c": [G38, None], "fr": "Occupé par l'Allemagne", "en": "Occupied by Germany"},
    "ital": {"c": [IT, None], "fr": "Italie", "en": "Italy"},
    "allie": {"c": [ALLIE, None], "fr": "Alliés de l'Allemagne", "en": "Germany's allies"},
    "urss": {"c": [USSR, None], "fr": "URSS", "en": "USSR"},
    "su": {"c": SU, "fr": "Pris par l'URSS en 1939-40", "en": "Taken by the USSR, 1939–40"},
    "allies39": {"c": [DEMO, None], "fr": "France et Pologne, alliées du R.-U.", "en": "France and Poland, Britain's allies"},
    "uk": {"c": [UK, None], "fr": "Royaume-Uni", "en": "United Kingdom"},
    "usa": {"c": [USA, None], "fr": "États-Unis", "en": "United States"},
    "neutre": {"c": [NEUTRE, None], "fr": "Neutres", "en": "Neutral"},
    "japon": {"c": [JAP, None], "fr": "Japon", "en": "Japan"},
    "mandch": {"c": ["#E9D9C4", JAP], "fr": "Mandchourie, sous contrôle japonais", "en": "Manchuria, under Japanese control"},
    "vichy": {"c": [VICHY, G38], "fr": "« Zone libre » (Vichy)", "en": "“Free zone” (Vichy)"},
    "nord": {"c": [G38, G33], "fr": "Nord rattaché à Bruxelles", "en": "Nord, attached to Brussels"},
    "front": {"c": ["line", NOIR], "fr": "Ligne de front", "en": "Front line"},
}

LABELS = {
    # pays et régions
    "l_all": {"p": [9.5, 52.0], "fr": "Allemagne", "en": "Germany", "c": "w"},
    "l_ita": {"p": [12.8, 42.6], "fr": "Italie", "en": "Italy", "c": "w"},
    "l_urss": {"p": [46.0, 59.5], "fr": "URSS", "en": "USSR", "c": "w", "s": 14},
    "l_urss_m": {"p": [90.0, 62.0], "fr": "URSS", "en": "USSR", "c": "w", "s": 14},
    "l_fra": {"p": [2.4, 46.9], "fr": "France", "en": "France"},
    "l_ru": {"p": [-2.0, 53.3], "fr": "Royaume-\nUni", "en": "United\nKingdom", "c": "w"},
    "l_pol": {"p": [20.8, 50.5], "fr": "Pologne", "en": "Poland"},
    "l_jap": {"p": [134.0, 35.2], "fr": "Japon", "en": "Japan", "c": "w"},
    "l_chine": {"p": [108.0, 31.0], "fr": "Chine", "en": "China"},
    "l_mand": {"p": [124.5, 46.5], "fr": "Mandchourie", "en": "Manchuria"},
    "l_usa": {"p": [-99.0, 39.5], "fr": "États-Unis", "en": "United States", "c": "w", "s": 14},
    "l_nor": {"p": [9.0, 61.5], "fr": "Norvège", "en": "Norway"},
    "l_dan": {"p": [9.2, 56.1], "fr": "Danemark", "en": "Denmark"},
    "l_sue": {"p": [15.5, 62.5], "fr": "Suède", "en": "Sweden"},
    "l_fin": {"p": [26.5, 63.0], "fr": "Finlande", "en": "Finland"},
    "l_bel": {"p": [4.6, 50.6], "fr": "Belgique", "en": "Belgium"},
    "l_pb": {"p": [5.6, 52.3], "fr": "Pays-Bas", "en": "Netherlands"},
    "l_baltes": {"p": [24.5, 57.0], "fr": "Pays baltes", "en": "Baltic states"},
    "l_bess": {"p": [28.6, 47.1], "fr": "Bessarabie", "en": "Bessarabia"},
    "l_carelie": {"p": [30.0, 61.6], "fr": "Carélie", "en": "Karelia"},
    "l_hon": {"p": [19.3, 47.1], "fr": "Hongrie", "en": "Hungary"},
    "l_rou": {"p": [24.8, 45.8], "fr": "Roumanie", "en": "Romania"},
    "l_bul": {"p": [25.3, 42.7], "fr": "Bulgarie", "en": "Bulgaria"},
    "l_you": {"p": [19.5, 44.2], "fr": "Yougoslavie", "en": "Yugoslavia"},
    "l_gre": {"p": [22.0, 39.5], "fr": "Grèce", "en": "Greece"},
    "l_slo": {"p": [19.6, 48.75], "fr": "Slovaquie", "en": "Slovakia"},
    "l_esp": {"p": [-3.8, 40.0], "fr": "Espagne", "en": "Spain"},
    "l_ukr": {"p": [32.0, 49.0], "fr": "Ukraine : blé", "en": "Ukraine: wheat", "t": "evt", "dx": 0, "dy": -12},
    "l_cauc": {"p": [45.5, 42.6], "fr": "Caucase : pétrole", "en": "Caucasus: oil", "t": "evt", "dx": 0, "dy": -12},
    "l_ardennes": {"p": [5.5, 50.05], "fr": "Ardennes", "en": "Ardennes", "t": "mer"},
    "l_somme": {"p": [2.75, 49.78], "fr": "Somme", "en": "Somme", "t": "mer"},
    "l_maginot": {"p": [7.2, 48.6], "fr": "Ligne Maginot", "en": "Maginot Line", "t": "evt", "dx": 8},
    "l_occ": {"p": [0.6, 48.2], "fr": "Zone occupée", "en": "Occupied zone"},
    "l_libre": {"p": [2.0, 45.0], "fr": "« Zone libre »", "en": "“Free zone”"},
    "l_annex": {"p": [6.9, 48.75], "fr": "Annexée", "en": "Annexed", "t": "evt", "dx": 8},
    "l_afn": {"p": [2.0, 31.5], "fr": "Afrique du Nord française", "en": "French North Africa"},
    "l_pac": {"p": [-170.0, 30.0], "fr": "Océan Pacifique", "en": "Pacific Ocean", "t": "mer"},
    "l_atl": {"p": [-38.0, 40.0], "fr": "Océan Atlantique", "en": "Atlantic Ocean", "t": "mer"},
    "l_manche": {"p": [-1.2, 50.15], "fr": "Manche", "en": "Channel", "t": "mer"},
    "l_volga": {"p": [46.4, 49.6], "fr": "Volga", "en": "Volga", "t": "mer"},
    "l_noire": {"p": [34.0, 43.3], "fr": "Mer Noire", "en": "Black Sea", "t": "mer"},
    "l_balt": {"p": [19.0, 56.6], "fr": "Baltique", "en": "Baltic", "t": "mer"},
    "l_fer": {"p": [18.5, 66.8], "fr": "Fer suédois", "en": "Swedish iron ore", "t": "evt", "dx": 0, "dy": -12},
    # villes et lieux d'événements
    "berlin": {"p": [13.40, 52.52], "fr": "Berlin", "en": "Berlin", "t": "ville"},
    "moscou": {"p": [37.62, 55.75], "fr": "Moscou", "en": "Moscow", "t": "ville", "dy": -4},
    "varsovie": {"p": [21.01, 52.23], "fr": "Varsovie", "en": "Warsaw", "t": "ville"},
    "paris": {"p": [2.35, 48.86], "fr": "Paris", "en": "Paris", "t": "ville"},
    "londres": {"p": [-0.13, 51.51], "fr": "Londres", "en": "London", "t": "ville", "dx": -7},
    "vichy": {"p": [3.43, 46.13], "fr": "Vichy", "en": "Vichy", "t": "ville"},
    "rethondes": {"p": [2.90, 49.43], "fr": "Rethondes", "en": "Rethondes", "t": "evt"},
    "dunkerque": {"p": [2.38, 51.03], "fr": "Dunkerque", "en": "Dunkirk", "t": "evt"},
    "douvres": {"p": [1.31, 51.13], "fr": "Douvres", "en": "Dover", "t": "ville", "dx": -7},
    "sedan": {"p": [4.94, 49.70], "fr": "Sedan", "en": "Sedan", "t": "evt"},
    "abbeville": {"p": [1.83, 50.10], "fr": "Abbeville", "en": "Abbeville", "t": "ville", "dx": -7},
    "rome": {"p": [12.50, 41.90], "fr": "Rome", "en": "Rome", "t": "ville"},
    "oslo": {"p": [10.75, 59.91], "fr": "Oslo", "en": "Oslo", "t": "ville"},
    "narvik": {"p": [17.43, 68.44], "fr": "Narvik", "en": "Narvik", "t": "evt"},
    "leningrad": {"p": [30.32, 59.93], "fr": "Leningrad", "en": "Leningrad", "t": "ville"},
    "stalingrad": {"p": [44.50, 48.71], "fr": "Stalingrad", "en": "Stalingrad", "t": "evt"},
    "kiev": {"p": [30.52, 50.45], "fr": "Kiev", "en": "Kiev", "t": "ville"},
    "rostov": {"p": [39.70, 47.23], "fr": "Rostov", "en": "Rostov", "t": "ville"},
    "minsk": {"p": [27.56, 53.90], "fr": "Minsk", "en": "Minsk", "t": "ville", "dx": -7},
    "smolensk": {"p": [32.05, 54.78], "fr": "Smolensk", "en": "Smolensk", "t": "ville", "dy": 9},
    "helsinki": {"p": [24.94, 60.17], "fr": "Helsinki", "en": "Helsinki", "t": "ville", "dx": -7},
    "shanghai": {"p": [121.47, 31.23], "fr": "Shanghai", "en": "Shanghai", "t": "evt"},
    "nankin": {"p": [118.80, 32.06], "fr": "Nankin", "en": "Nanking", "t": "ville", "dx": -7},
    "pekin": {"p": [116.40, 39.90], "fr": "Pékin", "en": "Beijing", "t": "ville", "dx": -7},
    "moukden": {"p": [123.43, 41.80], "fr": "Moukden", "en": "Mukden", "t": "evt"},
    "tokyo": {"p": [139.70, 35.70], "fr": "Tokyo", "en": "Tokyo", "t": "ville"},
    "geneve": {"p": [6.14, 46.20], "fr": "Genève (SDN)", "en": "Geneva (League)", "t": "ville"},
    "pearl": {"p": [-157.97, 21.36], "fr": "Pearl Harbor", "en": "Pearl Harbor", "t": "evt"},
    "washington": {"p": [-77.04, 38.90], "fr": "Washington", "en": "Washington", "t": "ville"},
    "casablanca": {"p": [-7.60, 33.57], "fr": "Casablanca", "en": "Casablanca", "t": "evt"},
    "oran": {"p": [-0.63, 35.70], "fr": "Oran", "en": "Oran", "t": "evt", "dx": -7},
    "alger": {"p": [3.06, 36.75], "fr": "Alger", "en": "Algiers", "t": "evt"},
}

F0 = [(21.1, 55.75), (21.6, 55.2), (22.6, 55.0), (22.9, 54.4), (23.5, 53.95), (23.9, 53.2), (23.6, 52.6), (23.65, 52.1), (24.1, 51.6), (24.05, 50.9),
      (23.6, 50.4), (23.0, 49.9), (22.65, 49.5), (22.5, 49.1), (23.3, 48.3), (24.6, 47.95), (26.2, 48.0), (26.6, 48.25), (27.5, 48.1), (28.2, 47.1),
      (28.25, 46.4), (28.2, 45.5), (28.9, 45.3), (29.7, 45.2)]
F41 = [(29.6, 59.9), (30.8, 59.7), (31.1, 59.95), (33.5, 59.65), (32.3, 58.8), (31.3, 58.5), (31.9, 57.9), (33.1, 57.2), (35.9, 56.85), (37.1, 56.4),
       (37.45, 56.05), (36.9, 55.6), (36.7, 55.38), (37.1, 54.9), (37.4, 54.3), (38.0, 54.1), (38.4, 53.4), (38.5, 52.6), (37.3, 51.7), (37.6, 50.6),
       (37.7, 49.5), (38.2, 48.3), (38.9, 47.25)]
F42 = [(29.6, 59.9), (30.8, 59.7), (31.1, 59.95), (32.2, 59.2), (31.5, 58.6), (32.0, 58.0), (33.4, 57.9), (32.6, 57.3), (34.0, 56.6), (35.0, 56.2),
       (35.3, 55.6), (35.0, 55.0), (34.5, 54.4), (35.6, 53.6), (36.6, 53.0), (37.5, 52.3), (38.5, 51.9), (39.2, 51.66), (40.0, 50.6), (41.3, 50.0),
       (42.5, 49.6), (43.4, 49.3), (44.0, 48.9), (44.5, 48.75), (44.3, 47.8), (44.6, 46.5), (45.0, 45.3), (44.6, 43.8), (43.7, 43.5), (42.0, 43.3),
       (40.5, 43.9), (39.3, 44.2), (38.9, 44.35)]
FRONTS = {"F0": {"pts": F0, "occ": 0}, "F41": {"pts": F41, "occ": 1}, "F42": {"pts": F42, "occ": 1}}

MAGINOT = [(8.2, 49.0), (7.6, 49.15), (6.9, 49.25), (6.4, 49.45), (5.9, 49.5), (5.5, 49.55), (5.0, 49.62)]


def ordre(P):
    """Ordre de dessin : le monde, puis les pièces européennes, puis les zones françaises."""
    monde = ["terre"] + sorted(k for k in P if k.startswith("w:"))
    fr = ["fr_occ", "fr_nord", "fr_annex", "fr_libre", "fr_ital"]
    europe = [k for k in P if not k.startswith("w:") and k not in fr and k not in ("sov41", "vilnius", "terre", "rhenanie", "dustbowl", "ukraine32")]
    return monde + europe + ["rhenanie", "dustbowl", "ukraine32"] + fr + ["sov41"]


def L(fr, en):
    return {"fr": fr, "en": en}


def F(a, b, col=ROUGE, k=0.15, w=3.2, **kw):
    d = {"id": kw.pop("id", f"{a[0]:.1f},{a[1]:.1f}>{b[0]:.1f},{b[1]:.1f}"), "a": a, "b": b, "k": k, "col": col, "w": w}
    d.update(kw)
    return d


EUROPE_1939 = {
    **{k: [NEUTRE, None] for k in ("portugal", "spain", "switzerland", "sweden", "irlande", "turquie", "iceland", "finlande", "carelie", "hungary",
                                    "roumanie", "bessarabie", "bulgaria", "yugoslavia", "greece", "baltes", "belgium", "netherlands", "luxembourg",
                                    "denmark", "norway", "danzig")},
    **{k: [G33, None] for k in ("germany", "saar", "austria", "sudetes", "boheme")},
    "slovaquie": [ALLIE, None], "italie": [IT, None], "albanie": [IT, None], "urss": [USSR, None],
    "ru": [UK, None], "france": [DEMO, None], "pologne_all": [DEMO, None], "pologne_urss": [DEMO, None],
}


def scenes():
    S = []

    def add(part, d, cam, date, titre, texte, **kw):
        s = {"part": part, "d": d, "cam": cam, "date": date, "titre": titre, "texte": texte}
        s.update(kw)
        S.append(s)

    # ---------------- Introduction
    add("Intro", 13, [55, 28, 1.0], L("1931-1947", "1931–1947"),
        L("Une guerre-monde", "A world war"),
        L("Pour des historiens comme Robert Frank, la guerre commence avant 1939 : sa chronologie s'étire de 1931 à 1947. C'est une guerre idéologique : il ne s'agit pas seulement de vaincre l'ennemi, mais de détruire sa civilisation. Environ 60 millions de morts.",
          "For historians such as Robert Frank, the war began before 1939: its chronology stretches from 1931 to 1947. It was an ideological war: the aim was not only to defeat the enemy but to destroy its civilisation. About 60 million dead."),
        st={"germany": [G33, None], "saar": [G33, None], "austria": [G33, None], "italie": [IT, None], "w:Empire of Japan": [JAP, None],
            "w:Manchuria": ["#E9D9C4", JAP], "urss": [USSR, None], "ru": [UK, None], "france": [DEMO, None]},
        labels=["l_all", "l_ita", "l_jap", "l_urss_m"], cles=["reich", "ital", "japon", "mandch", "urss"])
    add("Intro", 12, [124, 40, 2.6], L("Septembre 1931", "September 1931"),
        L("Le Japon s'empare de la Mandchourie", "Japan seizes Manchuria"),
        L("Après l'incident de Moukden, l'armée japonaise conquiert la Mandchourie, riche en charbon et en fer, et en fait un État fantoche. La SDN condamne, le Japon la quitte : la sécurité collective se fissure (chapitres 1 et 2).",
          "After the Mukden incident, the Japanese army conquered Manchuria, rich in coal and iron, and turned it into a puppet state. The League condemned it and Japan left the League: collective security began to crack (chapters 1 and 2)."),
        labels=["l_jap", "l_mand", "l_chine", "tokyo"], pins=["moukden"], cles=["japon", "mandch"],
        arrows=[F((129.5, 36.5), (123.6, 41.6), JAP, 0.2, id="jap31")])
    add("Intro", 14, [116, 34, 2.7], L("1937", "1937"),
        L("Le Japon attaque la Chine du Sud : le tournant", "Japan attacks southern China: the turning point"),
        L("En 1937, le Japon attaque la Chine du Sud. La Chine appelle aussitôt la SDN à l'aide, mais la SDN se montre incapable de régler les tensions, qui gagnent bientôt l'échelle mondiale. Pour Robert Frank et Alya Aglan, c'est le début de « la guerre-monde 1937-1947 ».",
          "In 1937 Japan attacked southern China. China immediately appealed to the League of Nations, but the League proved incapable of regulating the tensions, which soon spread to a global scale. For Robert Frank and Alya Aglan, this is the start of “the world war 1937–1947”."),
        labels=["l_jap", "l_chine", "pekin", "nankin"], pins=["shanghai"], cles=["japon", "mandch"],
        arrows=[F((121.5, 41.0), (116.6, 39.3), JAP, 0.15, id="jap37a"), F((116.0, 39.0), (114.6, 33.5), JAP, -0.1, id="jap37b"),
                F((126.5, 30.0), (121.8, 31.2), JAP, 0.2, id="jap37c"), F((121.2, 31.2), (118.9, 32.0), JAP, 0.1, id="jap37d")])

    # ---------------- I.1 : l'Europe 1939-1941, le cas français
    add("I.1", 13, [20, 51, 2.5], L("Août 1939", "August 1939"),
        L("Le pacte germano-soviétique", "The Nazi-Soviet pact"),
        L("L'Allemagne a déjà absorbé l'Autriche, les Sudètes puis la Bohême-Moravie (chapitre 2). Par le pacte d'août 1939, Hitler s'assure la neutralité de l'URSS ; en secret, les deux puissances prévoient de se partager la Pologne. L'Allemagne se sent prête à conquérir son Lebensraum.",
          "Germany had already absorbed Austria, the Sudetenland and then Bohemia-Moravia (chapter 2). By the pact of August 1939 Hitler secured the neutrality of the USSR; in secret, the two powers planned to carve up Poland. Germany felt ready to conquer its Lebensraum."),
        st=dict(EUROPE_1939), labels=["l_all", "l_urss", "l_pol", "l_fra", "l_ru", "l_ita", "moscou"],
        cles=["reich", "allie", "ital", "urss", "allies39", "uk", "neutre"])
    add("I.1", 13, [19.5, 52, 4.6], L("1er septembre 1939", "1 September 1939"),
        L("L'Allemagne envahit la Pologne", "Germany invades Poland"),
        L("Hitler envahit la Pologne par l'ouest, par la Prusse-Orientale et par la Slovaquie. Le Royaume-Uni et la France, alliés de la Pologne, déclarent la guerre à l'Allemagne le 3 septembre. L'Allemagne et l'URSS sont les deux puissances qui attaquent les premières.",
          "Hitler invaded Poland from the west, from East Prussia and from Slovakia. Britain and France, Poland's allies, declared war on Germany on 3 September. Germany and the USSR were the two powers that attacked first."),
        labels=["l_pol", "berlin", "varsovie"], pins=["varsovie"], cles=["reich", "allie", "allies39", "urss"],
        arrows=[F((14.4, 52.4), (20.4, 52.2), ROUGE, -0.12, id="pl1"), F((20.6, 54.1), (21.1, 52.5), ROUGE, 0.1, id="pl2"),
                F((15.0, 51.0), (19.6, 51.4), ROUGE, -0.1, id="pl3"), F((19.6, 49.3), (21.7, 50.8), ROUGE, 0.12, id="pl4")])
    add("I.1", 13, [22, 52.2, 4.2], L("17 septembre 1939", "17 September 1939"),
        L("L'URSS envahit l'est de la Pologne : le partage", "The USSR invades eastern Poland: the partition"),
        L("Le 17 septembre, l'Armée rouge entre dans l'est de la Pologne. En un mois, la Pologne est vaincue et partagée entre l'Allemagne nazie et l'Union soviétique, de part et d'autre d'une ligne de démarcation qui passe entre Varsovie et Białystok.",
          "On 17 September the Red Army entered eastern Poland. Within a month Poland was defeated and partitioned between Nazi Germany and the Soviet Union, on either side of a demarcation line running between Warsaw and Białystok."),
        st={"pologne_all": [G38, None], "danzig": [G33, None], "pologne_urss": SU},
        labels=["l_pol", "varsovie", "moscou"], cles=["reich", "occ", "su", "urss"],
        arrows=[F((28.6, 53.6), (24.4, 52.9), USSR, 0.12, id="su1"), F((28.4, 50.6), (24.4, 50.0), USSR, -0.12, id="su2")])
    add("I.1", 14, [6.0, 49.4, 7.5], L("Sept. 1939 - mai 1940", "Sept. 1939 – May 1940"),
        L("La drôle de guerre", "The phoney war"),
        L("À l'ouest, presque aucun combat. La France a sans doute la plus grande armée du monde (105 divisions), mais elle est dirigée par les vainqueurs de 1918 et choisit la défense : éviter une nouvelle guerre de tranchées et attendre l'attaque derrière la ligne Maginot, qui ne couvre pas la frontière belge.",
          "In the west, almost no fighting. France probably had the largest army in the world (105 divisions), but it was led by the victors of 1918 and chose defence: avoid a new trench war and wait for the attack behind the Maginot Line, which did not cover the Belgian border."),
        labels=["l_fra", "l_all", "l_bel", "l_maginot", "paris"], cles=["reich", "allies39", "neutre"],
        arrows=[{"id": "maginot", "ligne": MAGINOT, "col": BLEU, "w": 4, "nohead": True, "dash": True, "dur": 2.2}])
    add("I.1", 12, [27, 61.5, 4.2], L("Hiver 1939-1940", "Winter 1939–1940"),
        L("L'URSS prend sa part à l'est", "The USSR takes its share in the east"),
        L("Pendant la drôle de guerre, l'URSS attaque la Finlande [hors] et lui prend la Carélie en mars 1940 : la carte du cours la range dans les « terres saisies par la Russie, 1939-40 ».",
          "During the phoney war the USSR attacked Finland [hors] and took Karelia from it in March 1940: the course map counts it among the “land seized by Russia, 1939–40”."),
        st={"carelie": SU}, labels=["l_fin", "l_carelie", "helsinki", "leningrad"], cles=["su", "urss", "neutre"],
        arrows=[F((32.0, 62.4), (29.6, 61.3), USSR, 0.15, id="fin1"), F((31.5, 60.5), (29.0, 60.7), USSR, -0.15, id="fin2")])
    add("I.1", 14, [13, 61, 3.0], L("Avril 1940", "April 1940"),
        L("Le Danemark et la Norvège envahis", "Denmark and Norway invaded"),
        L("L'Allemagne occupe le Danemark et envahit la Norvège : la carte du cours montre la route du fer suédois, exporté vers l'Allemagne par Narvik. Le Royaume-Uni n'empêche pas l'occupation de la Norvège : Chamberlain perd le soutien des Communes.",
          "Germany occupied Denmark and invaded Norway: the course map shows the route of Swedish iron ore, shipped to Germany through Narvik. Britain failed to prevent the occupation of Norway: Chamberlain lost the support of the House of Commons."),
        st={"denmark": [G38, None], "norway": [G38, None]}, labels=["l_nor", "l_dan", "l_sue", "l_fer", "oslo"], pins=["narvik"], cles=["reich", "occ", "neutre"],
        arrows=[F((9.9, 54.4), (10.3, 56.6), ROUGE, 0.15, id="dk"), F((10.6, 54.7), (10.6, 59.6), ROUGE, -0.25, id="no1"),
                F((8.5, 57.6), (16.9, 68.2), ROUGE, 0.25, id="no2"),
                {"id": "fer", "ligne": [(20.2, 67.85), (18.9, 68.2), (17.43, 68.44), (14.5, 68.2), (12.0, 66.0), (8.0, 63.0), (5.2, 60.0), (5.0, 57.5), (8.0, 54.8)],
                 "col": "#5A4630", "w": 2.4, "dash": True, "dur": 2.6}])
    add("I.1", 14, [4.0, 50.6, 6.5], L("10 mai 1940", "10 May 1940"),
        L("L'attaque à l'ouest ; Churchill Premier ministre", "The attack in the west; Churchill prime minister"),
        L("Le Blitzkrieg, la « guerre éclair » des chars et des avions, frappe les Pays-Bas, la Belgique et le Luxembourg. Comme en 1914, Français et Britanniques s'attendent à une attaque par le centre de la Belgique et y envoient leurs meilleures troupes. Le même jour, Churchill devient Premier ministre.",
          "The Blitzkrieg, the “lightning war” of tanks and aircraft, struck the Netherlands, Belgium and Luxembourg. As in 1914, the French and British expected an attack through central Belgium and rushed their best forces there. The same day, Churchill became prime minister."),
        labels=["l_pb", "l_bel", "l_fra", "londres", "paris"], pins=["londres"], cles=["reich", "allies39", "uk"],
        arrows=[F((7.4, 51.7), (5.0, 52.1), ROUGE, 0.15, id="nl"), F((6.6, 50.9), (4.7, 50.95), ROUGE, -0.15, id="be"),
                F((3.0, 50.45), (4.5, 50.8), BLEU, 0.1, w=2.6, dash=True, id="dyle"), F((2.0, 50.6), (3.6, 51.0), BLEU, 0.1, w=2.6, dash=True, id="dyle2")])
    add("I.1", 15, [3.4, 49.9, 8.5], L("13-20 mai 1940", "13–20 May 1940"),
        L("La percée des Ardennes", "The breakthrough in the Ardennes"),
        L("L'attaque principale passe là où personne ne l'attend : par la forêt des Ardennes. Les chars allemands percent les lignes françaises à Sedan, puis foncent jusqu'à la Manche ; la 7e Panzer de Rommel traverse la campagne française vers la Somme. Les meilleures troupes alliées sont prises au piège en Belgique.",
          "The main attack came where nobody expected it: through the Ardennes forest. German tanks broke through the French lines at Sedan, then raced to the Channel; Rommel's 7th Panzer Division crossed the French countryside towards the Somme. The best Allied troops were trapped in Belgium."),
        st={"belgium": [G38, None], "netherlands": [G38, None], "luxembourg": [G38, None]},
        labels=["l_ardennes", "l_somme", "abbeville", "l_manche"], pins=["sedan"], cles=["reich", "occ", "allies39"],
        arrows=[F((6.9, 50.15), (4.95, 49.75), ROUGE, 0.12, w=3.6, id="ard1"), F((4.9, 49.8), (1.9, 50.12), ROUGE, -0.18, w=3.6, id="ard2", dur=2.4)])
    add("I.1", 14, [1.9, 51.0, 13], L("26 mai - 4 juin 1940", "26 May – 4 June 1940"),
        L("Dunkerque : l'opération Dynamo", "Dunkirk: Operation Dynamo"),
        L("Pris au piège contre la côte, les Britanniques évacuent leur armée par la mer : 338 000 soldats alliés rejoignent l'Angleterre. Les Français le vivent comme une trahison, mais la Royal Navy et la RAF restent intactes. Le 4 juin, Churchill promet : « nous ne nous rendrons jamais ».",
          "Trapped against the coast, the British evacuated their army by sea: 338,000 Allied soldiers reached England. The French saw it as a betrayal, but the Royal Navy and the RAF were left intact. On 4 June Churchill promised: “we shall never surrender”."),
        labels=["douvres", "l_manche"], pins=["dunkerque"], cles=["occ", "allies39", "uk"],
        arrows=[F((2.3, 51.08), (1.42, 51.12), UK, 0.35, w=2.6, id="dyn1", dt=0.25), F((2.45, 51.1), (1.38, 51.2), UK, -0.25, w=2.6, id="dyn2", dt=0.25),
                F((2.2, 51.06), (1.4, 51.05), UK, 0.1, w=2.6, id="dyn3", dt=0.25)])
    add("I.1", 14, [2.4, 48.3, 7.5], L("14 juin 1940", "14 June 1940"),
        L("Paris tombe ; l'exode", "Paris falls; the exodus"),
        L("Depuis la Somme, l'offensive allemande fonce vers Paris ; le gouvernement fuit la capitale. Paris tombe le 14 juin, six semaines après le début de la campagne. Quelque 8 millions de civils paniqués prennent les routes du sud : c'est l'exode. Bilan : environ 100 000 soldats français tués et 1 850 000 prisonniers.",
          "From the Somme, the German offensive drove towards Paris; the government fled the capital. Paris fell on 14 June, six weeks after the campaign began. Some 8 million panic-stricken civilians took to the roads south: the exodus. The toll: about 100,000 French soldiers killed and 1,850,000 taken prisoner."),
        labels=["l_somme", "l_fra"], pins=["paris"], cles=["reich", "occ", "allies39"],
        arrows=[F((2.2, 49.95), (2.35, 49.0), ROUGE, 0.1, w=3.6, id="par1"), F((2.0, 48.6), (0.6, 46.9), ROUGE, -0.1, id="par2"),
                F((3.0, 48.6), (4.6, 46.9), ROUGE, 0.12, id="par3"),
                F((2.4, 48.7), (1.6, 45.8), "#7D7465", 0.05, w=2.2, dash=True, id="exode1"), F((2.6, 48.7), (3.4, 45.6), "#7D7465", -0.05, w=2.2, dash=True, id="exode2")])
    add("I.1", 13, [-0.5, 50.0, 6.0], L("18 juin 1940", "18 June 1940"),
        L("L'appel du général de Gaulle", "General de Gaulle's appeal"),
        L("Le maréchal Pétain, chef du gouvernement, demande l'armistice. De Gaulle refuse, s'enfuit à Londres le 17 juin et rencontre Churchill. Le 18 juin, depuis Londres, il lance son appel : « la flamme de la résistance française ne doit pas s'éteindre et ne s'éteindra pas ».",
          "Marshal Pétain, now head of the government, asked for an armistice. De Gaulle refused, fled to London on 17 June and met Churchill. On 18 June, from London, he broadcast his appeal: “the flame of French resistance must not and shall not die”."),
        labels=["l_fra", "l_ru", "paris"], pins=["londres"], cles=["uk", "occ", "allies39"],
        arrows=[F((-1.6, 47.2), (-0.4, 51.3), UK, -0.2, w=2.6, dash=True, id="dg")])
    add("I.1", 15, [2.5, 46.6, 9.5], L("22 juin 1940", "22 June 1940"),
        L("L'armistice de Rethondes : la France découpée", "The armistice of Rethondes: France cut up"),
        L("L'armistice est signé à Rethondes. L'Allemagne occupe les trois cinquièmes du pays : les régions les plus riches et les côtes. La ligne de démarcation la sépare de la « zone libre », gouvernée depuis Vichy. Le Nord est rattaché au commandement allemand de Bruxelles, l'Alsace-Moselle annexée : retour aux frontières de 1871.",
          "The armistice was signed at Rethondes. Germany occupied three-fifths of the country: the richest regions and the coasts. The demarcation line separated it from the “free zone”, governed from Vichy. The Nord was attached to the German command in Brussels, and Alsace-Moselle was annexed: back to the borders of 1871."),
        st={"france": [VICHY, None], "fr_occ": [G38, None], "fr_nord": [G38, G33], "fr_annex": [G33, None], "fr_libre": [VICHY, G38]},
        labels=["l_occ", "l_libre", "l_annex", "paris", "vichy"], pins=["rethondes"], cles=["reich", "occ", "nord", "vichy"])
    add("I.1", 15, [2.8, 46.4, 10.5], L("Juillet 1940 - 1941", "July 1940 – 1941"),
        L("Vichy : un État autoritaire qui choisit la collaboration", "Vichy: an authoritarian state that chooses collaboration"),
        L("Dans la zone libre, le maréchal Pétain installe à Vichy un régime autoritaire, qui recherche la collaboration et persécute les Juifs avant même que l'Allemagne ne le demande : en octobre 1940, un décret définit qui est juif ; en mars 1941, Vichy crée un Commissariat aux questions juives.",
          "In the free zone, Marshal Pétain set up an authoritarian regime at Vichy, which sought collaboration and persecuted Jews even before Germany demanded it: in October 1940 a decree defined who was a Jew; in March 1941 Vichy created an Office for Jewish Affairs."),
        labels=["l_libre", "l_occ", "paris"], pins=["vichy"], cles=["occ", "vichy"])
    add("I.1", 13, [25, 55, 3.6], L("Été 1940", "Summer 1940"),
        L("L'URSS annexe les pays baltes et la Bessarabie", "The USSR annexes the Baltic states and Bessarabia"),
        L("Pendant que l'Allemagne écrase l'ouest, l'URSS prend sa part de l'Europe de l'Est : elle annexe l'Estonie, la Lettonie et la Lituanie, et prend la Bucovine du Nord et la Bessarabie à la Roumanie. En 1941, l'Axe domine l'Europe continentale.",
          "While Germany crushed the west, the USSR took its share of Eastern Europe: it annexed Estonia, Latvia and Lithuania, and took Northern Bukovina and Bessarabia from Romania. By 1941 the Axis dominated continental Europe."),
        st={"baltes": SU, "bessarabie": SU}, labels=["l_baltes", "l_bess", "l_rou", "l_urss", "moscou"], cles=["su", "urss", "occ", "reich"],
        arrows=[F((31.0, 57.6), (25.6, 57.0), USSR, 0.12, id="balt"), F((31.5, 48.2), (28.4, 47.4), USSR, -0.12, id="bess")])

    # ---------------- I.2 : le Royaume-Uni seul, soutenu par les États-Unis
    add("I.2", 14, [-1.0, 52.0, 4.6], L("Juin - août 1940", "June – August 1940"),
        L("Le Royaume-Uni seul : deux stratégies allemandes", "Britain alone: two German strategies"),
        L("La France vaincue, le Royaume-Uni est le seul ennemi qui reste à l'ouest. Dans son mémorandum de juin 1940, Alfred Jodl envisage soit une attaque directe (offensive aérienne et navale, bombardements de terreur sur les villes, débarquement), soit une guerre à la périphérie : la Méditerranée et les routes commerciales.",
          "With France defeated, Britain was the only enemy left in the west. In his memorandum of June 1940, Alfred Jodl considered either a direct attack (air and sea offensive, terror bombing of cities, a landing) or a war on the periphery: the Mediterranean and the trade routes."),
        labels=["l_ru", "l_fra", "l_manche", "londres"], cles=["uk", "occ", "reich", "vichy"])
    add("I.2", 15, [-0.6, 51.5, 9.0], L("7 septembre 1940", "7 September 1940"),
        L("Le Blitz sur Londres", "The Blitz on London"),
        L("La Luftwaffe commence ses raids du soir sur l'East End de Londres. Pour envahir, il faut d'abord abattre la RAF : bombardiers sur les docks, les usines et surtout les villes, pour briser l'industrie et le moral. Le cours compte 43 000 civils tués à Londres (chiffre d'ordinaire donné pour tout le Royaume-Uni).",
          "The Luftwaffe began its evening raids on London's East End. An invasion first required defeating the RAF: bombers struck docks, factories and above all cities, to break industry and morale. The course gives 43,000 civilian dead in London (usually the figure for the whole UK)."),
        labels=["l_manche"], pins=["londres"], cles=["uk", "occ"],
        arrows=[F((2.4, 49.6), (-0.05, 51.45), ROUGE, 0.12, w=2.4, dash=True, id="bl1", dt=0.3), F((4.4, 50.9), (0.05, 51.55), ROUGE, -0.12, w=2.4, dash=True, id="bl2", dt=0.3),
                F((1.0, 49.2), (-0.3, 51.4), ROUGE, 0.2, w=2.4, dash=True, id="bl3", dt=0.3)])
    add("I.2", 15, [-42, 44, 1.3], L("Décembre 1940 - mars 1941", "December 1940 – March 1941"),
        L("Le Royaume-Uni tient, l'Amérique l'approvisionne", "Britain holds, America supplies it"),
        L("La Luftwaffe n'obtient pas la maîtrise du ciel : en décembre 1940, l'invasion est reportée sine die, Hitler se tournant vers l'URSS. Les États-Unis, neutres, deviennent « l'arsenal de la démocratie » : le cash and carry, puis la loi prêt-bail de mars 1941 [hors], arment le Royaume-Uni.",
          "The Luftwaffe never won control of the air: in December 1940 the invasion was postponed indefinitely, as Hitler turned to the USSR. The neutral United States became the “Arsenal of Democracy”: cash and carry, then the Lend-Lease Act of March 1941 [hors], armed Britain."),
        labels=["l_usa", "l_atl", "washington", "londres"], cles=["usa", "uk", "occ"],
        st={"w:United States": ["#A9BED3", None]},
        arrows=[F((-73.5, 40.5), (-5.5, 51.0), BLEU, -0.12, w=2.8, dash=True, id="conv1", dur=2.8), F((-66.0, 44.5), (-6.0, 54.6), BLEU, -0.1, w=2.8, dash=True, id="conv2", dur=2.8)])

    # ---------------- II.1 : les projets allemands pour l'Est
    add("II.1", 14, [21, 45, 3.4], L("Avril - mai 1941", "April – May 1941"),
        L("Les Balkans conquis, les alliés de l'Allemagne", "The Balkans conquered, Germany's allies"),
        L("La Yougoslavie et la Grèce sont envahies [hors]. La Hongrie, la Roumanie et la Slovaquie, alliées de l'Allemagne sur la carte du cours, et la Bulgarie [hors] couvrent le flanc sud : à la veille de l'invasion de l'URSS, l'Allemagne domine le continent.",
          "Yugoslavia and Greece were invaded [hors]. Hungary, Romania and Slovakia, Germany's allies on the course map, and Bulgaria [hors] covered the southern flank: on the eve of the invasion of the USSR, Germany dominated the continent."),
        st={"yugoslavia": [G38, None], "greece": [G38, None], "hungary": [ALLIE, None], "roumanie": [ALLIE, None], "bulgaria": [ALLIE, None]},
        labels=["l_hon", "l_rou", "l_bul", "l_you", "l_gre", "l_slo"], cles=["reich", "occ", "allie", "ital", "urss"],
        arrows=[F((15.0, 46.6), (19.8, 44.4), ROUGE, -0.2, id="you"), F((22.6, 42.3), (22.8, 39.2), ROUGE, -0.2, id="gre")])
    add("II.1", 16, [31, 51, 2.6], L("1941", "1941"),
        L("Pourquoi envahir l'URSS ? Trois raisons", "Why invade the USSR? Three reasons"),
        L("Économique : le Grossraum, un Reich plus vaste et autosuffisant, la colonisation et l'asservissement des Slaves, le blé d'Ukraine et le pétrole du Caucase. Idéologique : la croisade contre le « judéo-bolchevisme ». Raciale : l'« Übermensch » aryen contre l'« Untermensch » slave ; les Juifs doivent être éliminés.",
          "Economic: the Grossraum, a larger self-sufficient Reich, German settlement and the enslavement of the Slavs, Ukrainian wheat and Caucasus oil. Ideological: the crusade against “Jewish Bolshevism”. Racial: the Aryan “Übermensch” against the Slavic “Untermensch”; the Jews were to be eliminated."),
        labels=["l_ukr", "l_cauc", "l_urss", "l_all", "moscou", "berlin"], cles=["reich", "occ", "allie", "urss", "su"])

    # ---------------- II.2 : Barbarossa
    add("II.2", 15, [29, 53, 3.0], L("22 juin 1941", "22 June 1941"),
        L("L'opération Barbarossa", "Operation Barbarossa"),
        L("Hitler rompt le pacte et lance l'invasion de l'URSS, que la Wehrmacht voit comme une croisade contre le communisme. Trois poussées sur un front de la Baltique à la mer Noire : au nord vers Leningrad, au centre par Minsk et Smolensk vers Moscou, au sud par l'Ukraine vers Kiev et Rostov. La Finlande, la Roumanie et la Hongrie combattent aux côtés de l'Allemagne.",
          "Hitler broke the pact and launched the invasion of the USSR, which the Wehrmacht saw as a crusade against communism. Three thrusts on a front from the Baltic to the Black Sea: north towards Leningrad, centre through Minsk and Smolensk towards Moscow, south through Ukraine towards Kiev and Rostov. Finland, Romania and Hungary fought alongside Germany."),
        st={"finlande": [ALLIE, None]}, front="F0",
        labels=["leningrad", "moscou", "kiev", "minsk", "smolensk", "rostov"], cles=["occ", "allie", "urss", "front"],
        arrows=[F((21.8, 55.2), (29.4, 59.2), ROUGE, -0.12, w=3.6, id="bN", dur=2.4), F((23.8, 52.6), (36.4, 55.5), ROUGE, -0.06, w=3.6, id="bC", dur=2.6),
                F((24.2, 50.7), (39.0, 47.6), ROUGE, 0.08, w=3.6, id="bS", dur=2.8)])
    add("II.2", 17, [33, 54.5, 3.3], L("Juin - décembre 1941", "June – December 1941"),
        L("L'avance allemande ; la terre brûlée", "The German advance; scorched earth"),
        L("L'Armée rouge, désorganisée et « décapitée » par les grandes purges, recule. Mais les paysans fuient en brûlant leurs récoltes, en emmenant leur bétail et en détruisant leurs villages : c'est la terre brûlée. Les troupes allemandes s'enfoncent profondément en URSS : 200 jours de guerre, 5 millions de morts, mille par heure en moyenne.",
          "The Red Army, disorganised and “beheaded” by the Great Purges, retreated. But peasants fled burning their crops, driving off their cattle and destroying their villages: scorched earth. German troops advanced deep into the USSR: 200 days of war, 5 million dead, a thousand an hour on average."),
        front="F41", fdur=9, fdelay=0.2, labels=["leningrad", "moscou", "kiev", "rostov", "minsk", "smolensk"], cles=["occ", "allie", "urss", "front"],
        arrows=[F((21.8, 55.2), (29.4, 59.2), ROUGE, -0.12, w=3.6, id="bN"), F((23.8, 52.6), (36.4, 55.5), ROUGE, -0.06, w=3.6, id="bC"),
                F((24.2, 50.7), (39.0, 47.6), ROUGE, 0.08, w=3.6, id="bS")])
    add("II.2", 15, [31, 51.5, 3.8], L("Automne 1941", "Autumn 1941"),
        L("Une guerre d'anéantissement", "A war of annihilation"),
        L("Sur le front de l'Est, les règles de la guerre disparaissent : meurtres de civils et de prisonniers deviennent la norme. L'ordre de Jodl de mai 1941 prescrit d'exécuter les commissaires politiques ; l'« ordre de sévérité » de Reichenau (10 octobre 1941) vise « l'espèce sous-humaine de la juiverie ». Environ 2,8 millions de prisonniers soviétiques meurent, surtout de faim.",
          "On the Eastern Front the rules of war disappeared: the murder of civilians and prisoners became the norm. Jodl's order of May 1941 prescribed shooting political commissars; Reichenau's “Severity Order” (10 October 1941) targeted “the subhuman species of Jewry”. About 2.8 million Soviet prisoners died, mainly of starvation."),
        front="F41", labels=["kiev", "minsk", "moscou", "leningrad"], cles=["occ", "urss", "front"])
    add("II.2", 14, [37.0, 55.6, 8.0], L("7 novembre 1941", "7 November 1941"),
        L("Staline : « Pas de pitié pour les occupants ! »", "Stalin: “No mercy to the occupiers!”"),
        L("À Moscou, alors que les Allemands avancent encore vers la capitale, Staline reprend le mot des nazis : « Si les Allemands veulent une guerre d'anéantissement, ils l'auront. » Tous les peuples soviétiques doivent détruire les envahisseurs « jusqu'au dernier ».",
          "In Moscow, while the Germans were still advancing on the capital, Stalin took up the Nazis' own word: “If the Germans want a war of annihilation, they will get it.” All the Soviet peoples were to destroy the invaders “to the last man”."),
        front="F41", labels=["smolensk"], pins=["moscou"], cles=["occ", "urss", "front"])
    add("II.2", 14, [34, 57.5, 4.4], L("Décembre 1941", "December 1941"),
        L("Arrêtés devant Leningrad et Moscou", "Stopped before Leningrad and Moscow"),
        L("La résistance croissante de l'Armée rouge empêche les Allemands de prendre Leningrad, assiégée, et Moscou. Le Blitzkrieg qui avait vaincu la France en six semaines échoue dans l'immensité russe. La guerre à l'Est sera longue.",
          "Stiffening Red Army resistance prevented the Germans from taking Leningrad, now besieged, and Moscow. The Blitzkrieg that had defeated France in six weeks failed in the immensity of Russia. The war in the East would be long."),
        front="F41", pins=["leningrad", "moscou"], labels=["l_fin"], cles=["occ", "allie", "urss", "front"])
    add("I.2", 15, [-172, 33, 1.12], L("7 décembre 1941", "7 December 1941"),
        L("Pearl Harbor", "Pearl Harbor"),
        L("Le même mois, le Japon, membre de l'Axe, bombarde la base américaine de Pearl Harbor, à Hawaï. Les États-Unis déclarent aussitôt la guerre au Japon.",
          "The same month, Japan, one of the Axis powers, bombed the American base of Pearl Harbor in Hawaii. The United States immediately declared war on Japan."),
        front="F41", st={"w:United States": [USA, None]}, labels=["l_jap", "l_usa", "l_pac", "tokyo"], pins=["pearl"], cles=["japon", "usa"],
        arrows=[F((146.5, 43.0), (201.6, 21.8), JAP, -0.18, w=3.4, id="pearl", dur=3.0)], lent=1.15)
    add("I.2", 15, [-30, 42, 1.12], L("11 décembre 1941", "11 December 1941"),
        L("La guerre devient mondiale", "The war goes global"),
        L("L'Allemagne et l'Italie déclarent la guerre aux États-Unis. Le même jour, Hitler définit devant le Reichstag le « nouvel ordre » : l'élimination des Juifs et la suprématie du peuple allemand. La guerre se mène désormais sur tous les océans et tous les continents : le Royaume-Uni n'est plus seul.",
          "Germany and Italy declared war on the United States. The same day, Hitler defined the “new order” before the Reichstag: the elimination of the Jews and the supremacy of the German people. From then on the war was fought on every ocean and continent: Britain was no longer alone."),
        front="F41", labels=["l_usa", "l_urss_m", "l_atl", "washington", "berlin"], cles=["usa", "uk", "urss", "reich", "occ", "allie"],
        arrows=[F((13.0, 52.3), (-76.0, 39.5), ROUGE, 0.12, w=2.4, dash=True, id="decl", dur=2.6)])

    # ---------------- retour en France : l'exploitation, la persécution (I.1)
    add("I.1", 15, [5.5, 49.0, 5.6], L("1942-1943", "1942–1943"),
        L("La France exploitée : argent, biens, travailleurs", "France exploited: money, goods, workers"),
        L("L'occupation est d'abord une exploitation : 20 millions de Reichsmarks par jour de frais d'occupation, réquisitions de charbon, de nourriture et de carburant, d'où rationnement et marché noir. À partir de 1942, le STO créé par Vichy envoie des travailleurs français en Allemagne.",
          "The occupation was above all exploitation: 20 million Reichsmarks a day in occupation fees, requisitions of coal, food and fuel, hence rationing and the black market. From 1942 the STO, created by Vichy, sent French workers to Germany."),
        front="F41", labels=["l_occ", "l_libre", "l_all", "paris", "berlin"], cles=["reich", "occ", "vichy"],
        arrows=[F((2.6, 48.8), (12.6, 52.3), ROUGE, -0.1, w=2.6, dash=True, id="sto1", dur=2.4), F((3.4, 46.3), (11.5, 50.9), ROUGE, 0.08, w=2.6, dash=True, id="sto2", dur=2.4)])
    add("I.1", 15, [2.35, 48.86, 12], L("Juin - juillet 1942", "June – July 1942"),
        L("L'étoile jaune et les rafles", "The yellow star and the round-ups"),
        L("En zone occupée, les Juifs sont dépouillés par l'« aryanisation », doivent porter l'étoile jaune à partir de juin 1942, puis sont arrêtés pour être déportés vers l'est, surtout par la police française (rafle du Vel' d'Hiv, juillet 1942). Environ 80 000 Juifs sont déportés de France ; 3 % survivent.",
          "In the occupied zone, Jews were dispossessed by “Aryanisation”, had to wear the yellow star from June 1942, then were arrested for deportation to the east, mainly by the French police (the Vel' d'Hiv round-up, July 1942). About 80,000 Jews were deported from France; 3% survived."),
        front="F41", pins=["paris"], cles=["occ", "vichy"],
        arrows=[F((2.45, 48.9), (5.6, 49.3), NOIR, -0.08, w=2.4, dash=True, id="dep", dur=2.2)])

    # ---------------- II.2 : 1942, vers Stalingrad
    add("II.2", 17, [40, 49.5, 3.6], L("Été 1942", "Summer 1942"),
        L("La seconde offensive : vers Stalingrad et le Caucase", "The second offensive: towards Stalingrad and the Caucasus"),
        L("Arrêtés devant Moscou, les Allemands, euphoriques, frappent au sud vers la Volga et le pétrole du Caucase. Le 28 juillet 1942, l'ordre n° 227 de Staline exige : « Pas un pas en arrière ! » Fin 1942, l'avance allemande atteint son maximum.",
          "Stopped before Moscow, the euphoric Germans struck south towards the Volga and the oil of the Caucasus. On 28 July 1942 Stalin's Order No. 227 demanded: “Not one step back!” By late 1942 the German advance reached its furthest point."),
        front="F42", fdur=8, fdelay=0.6, labels=["l_cauc", "l_volga", "rostov", "moscou"], pins=["stalingrad"], cles=["occ", "allie", "urss", "front"],
        arrows=[F((37.4, 49.6), (43.9, 48.85), ROUGE, -0.15, w=3.6, id="s42a", dur=2.6), F((39.6, 47.0), (43.6, 44.2), ROUGE, 0.15, w=3.6, id="s42b", dur=2.6)])
    add("II.2", 15, [44.4, 48.7, 10], L("Août - novembre 1942", "August – November 1942"),
        L("Stalingrad : défendre à tout prix", "Stalingrad: defend at all costs"),
        L("Les Russes défendent Stalingrad à tout prix : un bastion de la stratégie de Staline, un grand centre industriel et de transport sur la Volga qui garantit l'accès au pétrole du Caucase, et un symbole, la ville qui porte le nom de Staline. On se bat rue par rue, usine par usine (l'usine « Barricades »).",
          "The Russians defended Stalingrad at all costs: a stronghold of Stalin's strategy, a major industrial and transport hub on the Volga ensuring access to Caucasus oil, and a symbol, the city bearing Stalin's name. The fighting went street by street, factory by factory (the “Barricade” factory)."),
        front="F42", labels=["l_volga"], pins=["stalingrad"], cles=["occ", "urss", "front"])
    add("I.1", 15, [1.5, 41.0, 3.6], L("8 - 11 novembre 1942", "8–11 November 1942"),
        L("Le débarquement en Afrique du Nord ; la zone libre envahie", "The landing in North Africa; the free zone invaded"),
        L("Les Alliés débarquent en Afrique du Nord française : c'est l'opération Torch. En réponse, le 11 novembre 1942, l'Allemagne envahit la « zone libre », et l'Italie occupe une large partie du Sud-Est. Toute la France est désormais occupée.",
          "The Allies landed in French North Africa: Operation Torch. In response, on 11 November 1942, Germany invaded the “free zone”, and Italy occupied a large part of the south-east. All of France was now occupied."),
        front="F42", st={"france": [G38, None], "fr_libre": [G38, None], "fr_ital": [IT, None]},
        labels=["l_afn", "l_fra", "l_esp", "vichy"], pins=["casablanca", "oran", "alger"], cles=["occ", "ital", "usa", "uk"],
        arrows=[F((-14.0, 36.5), (-7.9, 33.8), USA, 0.15, w=3, id="tor1"), F((-5.0, 36.6), (-0.9, 35.85), UK, 0.2, w=3, id="tor2"),
                F((-0.5, 37.8), (2.9, 36.95), UK, -0.15, w=3, id="tor3"),
                F((2.5, 47.0), (2.9, 44.6), ROUGE, -0.1, w=3, id="zl1", dt=0.3), F((5.0, 46.9), (5.2, 44.8), ROUGE, 0.1, w=3, id="zl2", dt=0.3)], lent=1.1)
    add("II.2", 16, [43.6, 48.9, 6.5], L("Novembre 1942", "November 1942"),
        L("Le rapport de forces a basculé : l'encerclement", "The balance of forces has turned: the encirclement"),
        L("En novembre 1942, l'Armée rouge aligne à Stalingrad plus d'hommes (1 143 500 contre 1 011 500), plus de canons et plus de chars que les Allemands, qui ne gardent qu'une légère avance en avions. Malgré ses pertes, l'URSS mobilise plus vite. Ce même mois, l'armée allemande est encerclée.",
          "In November 1942 the Red Army lined up at Stalingrad more men (1,143,500 against 1,011,500), more guns and more tanks than the Germans, who kept only a slight edge in planes. Despite its losses, the USSR was mobilising faster. That same month, the German army was encircled."),
        front="F42", labels=["l_volga"], pins=["stalingrad"], cles=["occ", "urss", "front"],
        arrows=[F((42.0, 50.4), (43.3, 48.9), BLEU, 0.2, w=3.6, id="enc1"), F((45.4, 47.4), (43.7, 48.6), BLEU, -0.2, w=3.6, id="enc2")])
    add("II.2", 16, [44.5, 48.7, 9.5], L("2 février 1943", "2 February 1943"),
        L("Paulus capitule : le tournant de la guerre", "Paulus capitulates: the turning point of the war"),
        L("Le 2 février 1943, Paulus capitule : 95 000 soldats allemands sont faits prisonniers. L'URSS a perdu 1,13 million de soldats et de civils à Stalingrad, l'Allemagne et ses alliés 760 000. C'est une défaite retentissante pour la Wehrmacht, et une bataille qui correspond à la définition de la guerre totale.",
          "On 2 February 1943 Paulus capitulated: 95,000 German soldiers were taken prisoner. The USSR lost 1.13 million soldiers and civilians at Stalingrad, Germany and its allies 760,000. It was a resounding defeat for the Wehrmacht, and a battle that fits the definition of total war."),
        front="F42", pins=["stalingrad"], labels=["l_volga"], cles=["occ", "urss", "front"])

    # ---------------- bilan
    add("Bilan", 18, [17, 50, 2.2], L("Fin 1942", "Late 1942"),
        L("Le Nouvel Ordre européen", "The New European Order"),
        L("L'Europe nazie au plus loin : une entité raciale, le Lebensraum à l'Est, la croisade anticommuniste, le Grossraum économique, des hommes, des biens et de l'argent pour la guerre totale. Trois cinquièmes des morts de la guerre tombent sur le front de l'Est. La suite du chapitre (partie III, la politique raciale et le génocide) n'a pas encore été vue en classe.",
          "Nazi Europe at its furthest: a racial entity, Lebensraum in the East, the anti-communist crusade, the economic Grossraum, people, goods and money for total war. Three-fifths of the war's dead fell on the Eastern Front. The rest of the chapter (Part III, racial policy and genocide) has not yet been studied in class."),
        front="F42", labels=["l_all", "l_urss", "l_ru", "l_ita", "l_fra", "l_esp", "l_sue", "l_fin"], cles=["reich", "occ", "allie", "ital", "urss", "uk", "neutre", "front"])
    return S
