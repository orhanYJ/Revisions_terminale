"""HGGSP, thème 1, axe 2 : « Enjeux diplomatiques et coopérations » — le chapitre en vidéo.

Même chaîne que la vidéo pilote de l'introduction du thème 1 (hggsp_t1_intro.py) : outils/serie-philo/generer.py, voix
clonée, calage des visuels sur les mots ; moteur hggsp/serie/moteur.js (la table des cartes de l'état-major).
Contenu : le chapitre « t1-a2 » du site (outils/specialites/hggsp/src/data-t1.js), rien au-delà ; animations du site
iss, mer, scs et t1bbnj ; les données de l'épreuve viennent de la page « L'épreuve » du site (data-commun.js) et de la
vidéo d'introduction ; le sujet de dissertation et son corrigé sont ceux du chapitre (champ bac).
Ce qui dépasse le programme est dit « hors programme ».

Avant la voix (à refaire seulement si une animation du site ou une carte de la vidéo change) :
    node outils/serie-hggsp/scenes_t1_a2.js        → hggsp/serie/illu-hggsp-t1-a2.js
Contrôles : python3 outils/serie-philo/verifier.py hggsp_t1_a2 ;
brouillon sans voix : SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py hggsp_t1_a2 ;
puis chevauchements.py hggsp-t1-a2 et fermer.py hggsp_t1_a2.
"""

SITE = "hggsp"
CODE = "hggsp-t1-a2"
NOTION = "De nouveaux espaces de conquête"
NUM = 3
TITRE = "Enjeux diplomatiques et coopérations"
SUIVANT = "Thème 1 · Objet de travail conclusif · La Chine : à la conquête de l'espace, des mers et des océans"
RYTHME = "vivant"
PRONONCIATION = {"milles marins": "mil marins", "milles": "mil marins", "ISS": "I S S", "NASA": "Nasa", "Roscosmos": "Roscosmosse",
                 "Freedom": "Fridomme", "Reagan": "Rèïgane", "Zarya": "Zaria", "Zvezda": "Zvezda", "Columbus": "Colombusse",
                 "Kibo": "Kibo", "Crew": "Crou", "Dragon": "Dragonne", "SpaceX": "Spèïce X", "Tiangong": "Tiane-gongue",
                 "Wolf": "Woulf", "Artemis": "Artémisse", "ILRS": "I L R S", "Pesquet": "Pesquet", "Proxima": "Proxima",
                 "Truman": "Trouman", "CLPC": "C L P C", "OMI": "O M I", "OMC": "O M C", "AIFM": "A I F M",
                 "Atalanta": "Atalannta", "Clarion-Clipperton": "Clarionne-Clipeurtonne", "Ifremer": "Ifrémère",
                 "Trump": "Treumpe", "The Metals Company": "Ze Métalse Compagnie", "NOAA": "N O A A",
                 "Galápagos": "Galapagosse", "BBNJ": "B B N J", "Kunming": "Kounminngue", "Kingston": "Kinngstonne",
                 "Montego": "Montégo", "Bay": "Bèï", "ZEE": "Z E E", "URSS": "U R S S", "ONU": "O N U",
                 "Baïkonour": "Baïkonour", "Hambourg": "Hambour", "Costa Rica": "Costa Rica"}

# ---------------------------------------------------------------- étapes de cartes propres à la vidéo
ESP_A = [
    dict(date="1984", titre="Le projet américain « Freedom »", montre=["us", "ust", "freedom"], accent=["us"]),
    dict(date="1993", titre="La Russie rejoint le projet", montre=["ru", "rut", "mir"], accent=["ru"]),
    dict(date="29 janv. 1998", titre="Un accord à quinze pays", montre=["jp", "jpt", "ca", "cat", "esa", "a15"], cache=["freedom", "mir"], accent=["jp", "ca"]),
]
PARTENAIRES = ["us", "ru", "jp", "ca", "ust", "rut", "jpt", "cat", "esa"]
ESP_B = [
    dict(date="2011", titre="L'amendement Wolf : la Chine exclue", montre=["cn", "cnt", "tg"], accent=["cn"]),
    dict(date="Juillet 2022", titre="Un échange de sièges, malgré la guerre", montre=["sieges", "siegest"], accent=["us", "ru"]),
]
ESP_C = [
    dict(date="13 oct. 2020", titre="Les accords Artemis", montre=["art", "artt"], cache=["us", "ru", "jp", "ca", "jpt", "cat", "esa", "cnt", "tg"], accent=["art"]),
    dict(date="Mars 2021", titre="La station lunaire sino-russe (ILRS)", montre=["ilrs", "ilrst"], cache=["cn"], accent=["ilrs"]),
    dict(date="2022-2026", titre="Plus de 70 signataires pour Artemis", montre=["artfr", "artfrt", "art70"], accent=["artfr"]),
]
MERS_A = [
    dict(date="1958-1976", titre="Les « guerres de la morue »", montre=["uk", "isl", "morue"], accent=["isl", "uk"]),
    dict(date="1976", titre="L'Islande obtient ses 200 milles", montre=["islt"], accent=["isl"]),
    dict(date="10 déc. 1982", titre="La convention de Montego Bay", montre=["jam"], accent=["jam"]),
    dict(date="16 nov. 1994", titre="L'entrée en vigueur", montre=["vig"], accent=["jam"]),
]
MERS_B = [
    dict(date="Hambourg", titre="Le Tribunal international du droit de la mer", montre=["hamb"], accent=["hamb"]),
    dict(date="La Haye", titre="Ou un tribunal arbitral", montre=["haye"], accent=["haye"]),
]
MERS_C = [
    dict(date="Déc. 2008", titre="L'opération Atalanta, au large de la Somalie", montre=["som", "atal", "atalt"], accent=["atal"]),
]
SCS = [
    dict(date="Revendication", titre="La « ligne en neuf traits »", montre=["ligne", "lignet", "cn", "vn", "ph"], accent=["ligne"]),
    dict(date="12 juil. 2016", titre="La sentence arbitrale : pas de base légale", montre=["pca"], accent=["ligne"]),
]
FRANCE = [
    dict(date="Hexagone", titre="Une petite part du domaine", montre=["zmet", "zmett"], accent=["zmet"]),
    dict(date="Outre-mer", titre="Plus de 90 % du domaine", montre=["zom", "pft", "nct", "taaft", "ept"], accent=["zom"]),
]
FONDS = [
    dict(date="« La Zone »", titre="Clarion-Clipperton, entre Hawaï et le Mexique", montre=["ccz", "cczt", "haw", "mex"], accent=["ccz"]),
    dict(date="2001", titre="Un contrat d'exploration français", montre=["ifr"]),
    dict(date="Kingston", titre="L'Autorité internationale des fonds marins", montre=["kgn"], accent=["kgn"]),
]
FONDS_US = [
    dict(date="24 avril 2025", titre="Un décret américain", montre=["us25"], accent=["ccz"]),
]
HAUTE = [
    dict(date="Haute mer", titre="Près des deux tiers des océans", montre=["hm"]),
    dict(date="2020", titre="Des calmars au large des Galápagos", montre=["gal", "galt", "calm"], accent=["gal"]),
]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="orbite", humeur="mystere", carton=False, beats=[
        "{o1}Juillet 2022. Depuis quelques mois, la Russie fait la guerre à l'Ukraine. Les sanctions pleuvent. "
        "Entre Washington et Moscou, presque tout est coupé.",
        ("P", 0.5),
        "{-o1}{o2}Et pourtant, ce même mois, la NASA et l'agence spatiale russe Roscosmos signent un accord. "
        "Des cosmonautes russes voleront dans des capsules américaines. Et des astronautes américains, dans des fusées russes.",
        "{-o2}{q1}Comment deux rivaux peuvent-ils encore coopérer… au-dessus de nos têtes ?",
        ("P", 0.6),
        "{-q1}{oe}{oe.g}L'espace {oe.d}et les océans sont des terrains de rivalité. Mais ce sont aussi des terrains de coopération. "
        "Parce que certains problèmes sont trop grands, ou trop chers, pour un seul État.",
        "{-oe}{plan}Voici le dossier. {plan.1}D'abord, la Station spatiale internationale : un modèle de coopération… et ses limites. "
        "{plan.2}Ensuite, le partage des mers, de Montego Bay aux zones économiques exclusives. "
        "{plan.3}Puis les grands fonds et la haute mer, jusqu'au traité BBNJ. "
        "{plan.4}Et pour finir, le bac, avec un sujet de dissertation corrigé.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "o1": dict(type="mot", t="Juillet 2022", g="la guerre en Ukraine : presque tout est coupé entre Washington et Moscou", taille=130, y=220),
        "o2": dict(type="cols", g="Des cosmonautes russes", gq="dans des capsules américaines", d="Des astronautes américains",
                   dq="dans des fusées russes", vs="⇄"),
        "q1": dict(type="question", t="Comment deux rivaux peuvent-ils encore coopérer ?"),
        "oe": dict(type="cols", g="L'espace", gq="rivalités… et coopération", d="Les océans", dq="rivalités… et coopération", vs="+"),
        "plan": dict(type="liste", titre="Le dossier", items=[
            "La Station spatiale internationale : un modèle et ses limites", "Partager les mers : de Montego Bay aux ZEE",
            "Exploiter et préserver : des grands fonds au traité BBNJ", "Au bac : une dissertation corrigée"],
            marques=["I", "II", "III", "IV"], x=170, y=140, w=940),
        "titre": dict(type="titre", sur="HGGSP · Thème 1 · Axe 2", t="Enjeux diplomatiques et coopérations",
                      sous="De nouveaux espaces de conquête"),
    }),

    # ================================================================ I. une station née de la fin de la guerre froide
    dict(id="naissance", chap="Une station née de la fin de la guerre froide", fond="orbite", humeur="mystere",
         retenir="ISS : projet américain Freedom (1984), la Russie le rejoint en 1993 ; accord du 29 janvier 1998 entre 15 pays ; premier module Zarya (20 nov. 1998) ; occupée en permanence depuis le 2 nov. 2000.",
         beats=[
        "{esa}Remontons le temps. {esa.1}En 1984, en pleine guerre froide, le président américain Ronald Reagan annonce un projet de station spatiale. "
        "Son nom : Freedom. La liberté. Tout un programme.",
        "{esa.2}Puis l'URSS disparaît. Et en 1993, la Russie rejoint le projet. Elle apporte une expérience précieuse : "
        "celle de sa station Mir, en orbite de 1986 à 2001.",
        "{esa.3}Le 29 janvier 1998, un accord intergouvernemental réunit quinze pays : les États-Unis, la Russie, le Japon, le Canada, "
        "et onze États de l'Agence spatiale européenne.",
        "{-esa}{iss1}Et la station s'assemble, morceau par morceau. {iss1.1}Le premier module est russe : Zarya, lancé le 20 novembre 1998, "
        "depuis Baïkonour. Il est vite relié à un module américain, Unity.",
        "{iss1.2}Le 2 novembre 2000, le premier équipage s'installe : un Américain et deux Russes. "
        "Et depuis ce jour, la station n'a jamais été vide. Pas une seule journée.",
        "{-iss1}{f1}Retiens bien l'idée : l'ISS est un enfant de la {!fin de la guerre froide}fin de la guerre froide.",
    ], vis={
        "esa": dict(type="scene", anim="espace", etapes=ESP_A, fs=20,
                    cam={"0": [0, 0, 1000, 437], "1": [90, 30, 330, 144], "2": [470, 0, 380, 166], "3": [0, 0, 1000, 437]}),
        "iss1": dict(type="scene", anim="iss", pas=[1, 2], fs=20),
        "f1": dict(type="note", titre="À retenir", t="L'ISS naît de la fin de la guerre froide : la Russie rejoint le projet américain en 1993.", y=230),
    }),

    # ================================================================ II. un laboratoire hors norme
    dict(id="labo", chap="Un laboratoire hors norme", fond="orbite", humeur="lumiere",
         retenir="L'ISS : environ 420 t, environ 400 km d'altitude, un tour de la Terre en 90 min ; plus de 100 milliards de dollars ; environ 280 personnes de plus de 20 pays (2024).",
         beats=[
        "{tab_iss}Regarde-la. C'est la plus grande coopération scientifique de l'histoire.",
        "{-tab_iss}{ch}Quelques chiffres. {ch.1}Elle pèse environ quatre cent vingt tonnes. "
        "{ch.2}Elle vole à environ quatre cents kilomètres d'altitude. "
        "{ch.3}Et elle fait le tour de la Terre en quatre-vingt-dix minutes environ. Seize levers de soleil par jour !",
        "{-ch}{ch2}{ch2.1}Et c'est l'objet le plus coûteux jamais construit : plus de cent milliards de dollars.",
        "{-ch2}{rech}Mais à quoi sert-elle ? {rech.1}À étudier les effets de l'apesanteur sur le corps humain. "
        "Des mois en orbite, qu'est-ce que ça fait aux muscles, aux os, au cœur ? "
        "Il faut le savoir avant de partir loin. C'est indispensable si l'on veut un jour aller sur Mars. "
        "{rech.2}On y fait aussi de la physique des fluides, de la biologie. {rech.3}Et on y observe la Terre.",
        "{-rech}{pes}Un exemple que tu peux citer. {pes.1}Le Français Thomas Pesquet y a fait deux séjours. "
        "La mission Proxima, en 2016 et 2017. {pes.2}Puis la mission Alpha, en 2021, dont il est le commandant. "
        "Il y mène de nombreuses expériences scientifiques.",
        "{-pes}{ch3}{ch3.1}Et il n'est pas seul. En 2024, environ deux cent quatre-vingts personnes, venues de plus de vingt pays, étaient montées à bord.",
    ], vis={
        "tab_iss": dict(type="tableau", img="t1a2-iss", de=[1.0, .5, .5], a=[1.16, .5, .45],
                        legende="La Station spatiale internationale photographiée depuis la navette Atlantis, mai 2010, NASA (domaine public, Wikimedia Commons)"),
        "ch": dict(type="chiffres", items=[
            dict(v=420, avant="≈ ", apres=" t", t="la masse de la station"),
            dict(v=400, avant="≈ ", apres=" km", t="d'altitude"),
            dict(v=90, avant="≈ ", apres=" min", t="pour un tour de la Terre")], x=50, w=1180, y=200),
        "ch2": dict(type="chiffres", items=[dict(v=100, avant="plus de ", apres=" Md$", t="l'objet le plus coûteux jamais construit")], y=190),
        "rech": dict(type="liste", titre="Un laboratoire en orbite", items=[
            "Les effets de l'apesanteur sur le corps humain (avant d'aller sur Mars)",
            "La physique des fluides, la biologie", "L'observation de la Terre"], x=170, y=170, w=940),
        "pes": dict(type="chrono", titre="Un Français à bord", items=[
            dict(d="2016-2017", t="Thomas Pesquet : la mission Proxima", c="espace"),
            dict(d="2021", t="La mission Alpha : il commande la station", c="espace")], x=290, w=700, y=150, h=420),
        "ch3": dict(type="chiffres", items=[dict(v=280, avant="≈ ", t="personnes, de plus de 20 pays, montées à bord", src="en 2024")], y=190),
    }),

    # ================================================================ III. une coopération par interdépendance
    dict(id="interdep", chap="Une coopération par interdépendance", fond="orbite", humeur="calme",
         retenir="Deux segments indispensables l'un à l'autre : propulsion russe, électricité américaine. Columbus (2008), Kibo, bras canadien. De 2011 à 2020, la NASA dépend des Soyouz russes.",
         beats=[
        "{m1}Maintenant, la question clé. Pourquoi cette coopération tient-elle ? Réponse : parce que personne ne peut partir sans les autres.",
        "{-m1}{iss2}{iss2.1}La station est faite de deux segments : un américain, un russe. Et ils ne peuvent pas fonctionner l'un sans l'autre. "
        "Les Russes assurent notamment le maintien en orbite. Les Américains, l'essentiel de l'électricité.",
        "{iss2.2}Les autres partenaires ont aussi leur pièce. L'Europe fournit le laboratoire Columbus, en 2008. "
        "Le Japon, le module Kibo. Et le Canada, le bras robotique.",
        "{iss2.3}Et l'interdépendance va plus loin. En juillet 2011, la navette spatiale américaine fait son dernier vol. "
        "Alors, pendant près de dix ans, les astronautes de la NASA ne peuvent rejoindre la station qu'à bord des Soyouz russes. "
        "Jusqu'au premier vol habité de Crew Dragon, la capsule de SpaceX, en mai 2020.",
        "{-iss2}{def1}Voilà le mot à placer dans ta copie : une coopération par {!interdépendance}interdépendance.",
    ], vis={
        "m1": dict(type="mot", t="Personne ne part sans les autres.", taille=78, y=280),
        "iss2": dict(type="scene", anim="iss", pas=[3, 4, 5], fs=20),
        "def1": dict(type="def", terme="Coopération par interdépendance", t="Chaque partenaire tient une pièce indispensable : propulsion russe, électricité américaine, modules européen et japonais, bras canadien.", y=200),
    }),

    # ================================================================ IV. résister aux crises, mais exclure
    dict(id="limites", chap="Une coopération qui résiste… et qui exclut", fond="crise", humeur="tension",
         retenir="L'ISS survit aux crises (Crimée 2014, Ukraine 2022) : échange de sièges NASA-Roscosmos (juillet 2022). Mais elle exclut la Chine (amendement Wolf, 2011), qui construit Tiangong.",
         beats=[
        "{cr}Cette coopération résiste aux crises. {cr.1}En 2014, la Russie annexe la Crimée. {cr.2}En 2022, elle envahit l'Ukraine. "
        "Moscou menace de quitter la station… mais la station continue de voler.",
        "{-cr}{esb}Mais attention, elle a aussi ses limites. Et la première, c'est qui elle laisse dehors. "
        "{esb.1}En 2011, une loi américaine, l'amendement Wolf, interdit à la NASA de coopérer avec Pékin. "
        "La Chine est donc exclue de l'ISS. Sa réponse ? Elle construit sa propre station : Tiangong, assemblée en 2021 et 2022.",
        "{esb.2}Et pendant la guerre en Ukraine ? Revenons à notre accord de juillet 2022. Quelques mois après l'invasion, "
        "la NASA et Roscosmos s'échangent des sièges : des cosmonautes sur Crew Dragon, des astronautes américains sur Soyouz.",
        "{-esb}{f2}La coopération spatiale reste l'un des {!derniers canaux ouverts}derniers canaux ouverts entre Washington et Moscou.",
        "{-f2}{nu}Alors, comment lire ça ? {nu.g}Oui, l'espace force à coopérer. {nu.d}Mais cette coopération dessine aussi un camp. "
        "Et elle sert le prestige, et la diplomatie, des États-Unis.",
    ], vis={
        "cr": dict(type="chrono", titre="Des crises traversées", items=[
            dict(d="2014", t="La Russie annexe la Crimée", c="conflit"),
            dict(d="2022", t="L'invasion de l'Ukraine : Moscou menace de partir", c="conflit")], x=290, w=700, y=150, h=420),
        "esb": dict(type="scene", anim="espace", etapes=ESP_B, depart=PARTENAIRES, fs=20,
                    cam={"0": [0, 0, 1000, 437], "1": [560, 40, 330, 144], "2": [100, 0, 700, 306]}),
        "f2": dict(type="note", titre="À retenir", t="La coopération spatiale reste l'un des derniers canaux ouverts entre Washington et Moscou.", y=230),
        "nu": dict(type="cols", g="Une coopération réelle", gq="elle résiste à la guerre", d="Une coopération sélective",
                   dq="elle exclut la Chine et sert le prestige américain", vs="mais"),
    }),

    # ================================================================ V. après l'ISS
    dict(id="apres", chap="Après l'ISS : des blocs rivaux", fond="orbite", humeur="tension",
         retenir="ISS désorbitée vers 2030 (véhicule commandé à SpaceX, juin 2024). Sur la Lune, deux coalitions : accords Artemis (13 oct. 2020, plus de 70 signataires en 2026, France en juin 2022) contre ILRS sino-russe (mars 2021).",
         beats=[
        "{iss3}Et la suite ? {iss3.1}L'ISS doit être exploitée jusqu'en 2030. Puis elle sera désorbitée, et détruite en rentrant dans l'atmosphère, "
        "au-dessus du Pacifique. Le véhicule qui la poussera a été commandé à SpaceX, par un contrat de juin 2024.",
        "{-iss3}{ap}{ap.1}Après elle, chacun prend sa route. Les États-Unis misent sur des stations commerciales. "
        "{ap.2}La Chine a déjà la sienne. {ap.3}Et la Russie annonce un projet national.",
        "{-ap}{esc}Et sur la Lune ? Deux coalitions se forment. "
        "{esc.1}Le 13 octobre 2020, les États-Unis proposent les accords Artemis, pour encadrer l'exploration lunaire. "
        "{esc.2}En mars 2021, la Chine et la Russie répondent par leur propre projet : une station internationale de recherche lunaire, l'ILRS.",
        "{esc.3}La France signe les accords Artemis en juin 2022. Et en 2026, ils comptent plus de soixante-dix signataires.",
        "{-esc}{f3}La coopération de l'ISS laisse place à des {!blocs rivaux}blocs rivaux.",
    ], vis={
        "iss3": dict(type="scene", anim="iss", pas=[6], fs=20),
        "ap": dict(type="cartes", items=[
            dict(ic="drapeau", t="États-Unis", q="des stations commerciales"),
            dict(ic="satellite", t="Chine", q="sa station, Tiangong"),
            dict(ic="fusee", t="Russie", q="un projet national annoncé")]),
        "esc": dict(type="scene", anim="espace", etapes=ESP_C, depart=PARTENAIRES + ["cn"], fs=20),
        "f3": dict(type="note", titre="À retenir", t="Après l'ISS, des blocs rivaux : les accords Artemis contre le projet sino-russe ILRS.", y=230),
    }),

    # ================================================================ VI. pourquoi coopérer ?
    dict(id="pourquoi", chap="Pourquoi des rivaux coopèrent", fond="crise", humeur="calme", beats=[
        "{q2}Prenons du recul. Pourquoi des États rivaux acceptent-ils de coopérer ?",
        "{-q2}{rai}Il y a quatre raisons. {rai.1}Le coût, d'abord : plus de cent milliards de dollars, aucun pays ne veut payer seul. "
        "{rai.2}L'intérêt scientifique : on apprend plus à plusieurs. "
        "{rai.3}Le prestige : participer, c'est en être. Et diriger, c'est mieux encore. "
        "{rai.4}Et enfin les intérêts communs : un problème qui touche tout le monde, que personne ne peut régler seul.",
        "{-rai}{ex4}Et tu peux illustrer chaque raison. {ex4.1}Le coût ? La station elle-même, la plus chère jamais construite. {ex4.2}La science ? Les expériences de Thomas Pesquet. {ex4.3}Le prestige ? Les accords Artemis, menés par les États-Unis. {ex4.4}Les intérêts communs ? On va les retrouver en mer : la piraterie, la pêche, la biodiversité.",
        "{-ex4}{pg1}Et voilà le premier piège. Ne présente jamais l'ISS comme une coopération sans arrière-pensée. "
        "Elle sert aussi le prestige et la diplomatie américaine… et elle exclut la Chine.",
    ], vis={
        "q2": dict(type="question", t="Pourquoi des États rivaux coopèrent-ils ?"),
        "rai": dict(type="liste", titre="Quatre raisons de coopérer", items=[
            "Le coût : trop cher pour un seul État", "L'intérêt scientifique", "Le prestige",
            "Des intérêts communs, qu'aucun État ne peut défendre seul"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "ex4": dict(type="liste", titre="Un exemple pour chaque raison", items=[
            "Le coût : l'ISS, plus de 100 milliards de dollars", "La science : les expériences de Thomas Pesquet",
            "Le prestige : les accords Artemis, menés par les États-Unis", "Les intérêts communs : piraterie, pêche, biodiversité"],
            marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "pg1": dict(type="note", titre="Piège", t="L'ISS n'est pas une coopération sans arrière-pensée : prestige et diplomatie américaine, Chine exclue.", y=220),
    }),

    # ================================================================ VII. Montego Bay
    dict(id="montego", chap="Montego Bay : la fin de la course aux mers", fond="ocean", humeur="calme",
         retenir="Course aux mers après 1945 (Truman 1945 ; 200 milles revendiqués en 1952) ; guerres de la morue (1958-1976). Montego Bay : signée le 10 déc. 1982, en vigueur le 16 nov. 1994, plus de 160 États ; les États-Unis l'appliquent sans l'avoir ratifiée.",
         beats=[
        "{m2}Changeons d'élément. Direction la mer. Là aussi, il a fallu apprendre à partager.",
        "{-m2}{mer1}Tout part d'une course. {mer1.1}En 1945, la proclamation Truman : les États-Unis revendiquent les ressources de leur plateau continental. "
        "{mer1.2}En 1952, le Chili, le Pérou et l'Équateur réclament deux cents milles marins, pour protéger leur pêche. Et d'autres États suivent.",
        "{-mer1}{msa}Et quand chacun tire la mer à soi, ça finit mal. {msa.1}Regarde l'Atlantique Nord : entre 1958 et 1976, "
        "ce sont les « guerres de la morue ». Des garde-côtes islandais coupent les filets des chalutiers britanniques. "
        "{msa.2}L'Islande finit par obtenir ses deux cents milles, en 1976.",
        "{msa.3}Il fallait des règles. Une grande conférence des Nations unies s'ouvre en 1973. Elle aboutit à la convention de Montego Bay, "
        "signée le 10 décembre 1982. {msa.4}Elle entre en vigueur le 16 novembre 1994.",
        "{-msa}{rat}Aujourd'hui, plus de cent soixante États l'ont ratifiée. {rat.1}Mais retiens une exception de taille : les États-Unis "
        "l'appliquent… sans l'avoir ratifiée.",
    ], vis={
        "m2": dict(type="mot", t="Partager la mer", g="après 1945, chacun la tire à soi", taille=110, y=250),
        "mer1": dict(type="scene", anim="mer", pas=[2, 3], fs=20),
        "msa": dict(type="scene", anim="mers", etapes=MERS_A, fs=20,
                    cam={"0": [0, 0, 1000, 437], "1": [330, 0, 300, 131], "3": [130, 110, 300, 131]}),
        "rat": dict(type="chiffres", items=[dict(v=160, avant="plus de ", t="États ont ratifié la convention", src="mais pas les États-Unis")], y=190),
    }),

    # ================================================================ VIII. la ZEE
    dict(id="zee", chap="La ZEE : un partage qui profite aux côtiers", fond="ocean", humeur="lumiere",
         retenir="ZEE : 200 milles, monopole des ressources pour l'État côtier ; environ un tiers des océans. La France : environ 10 millions de km² de ZEE, 2e domaine du monde après les États-Unis, plus de 90 % outre-mer.",
         beats=[
        "{mer2}Le cœur de la convention, c'est la ZEE, la zone économique exclusive. {mer2.1}Jusqu'à deux cents milles des côtes, "
        "l'État côtier a le monopole de l'exploitation des ressources.",
        "{-mer2}{zch}Et c'est énorme. {zch.1}Les ZEE couvrent environ un tiers de la surface des océans. "
        "{zch.2}Et elles concentrent l'essentiel des ressources de la pêche, et des gisements d'hydrocarbures en mer.",
        "{-zch}{q3}Alors, qui gagne à ce partage ? Les États côtiers, bien sûr. Mais surtout… ceux qui ont des îles.",
        "{-q3}{fr}Prends la France. {fr.1}Son territoire européen ne lui donne qu'une petite part de son domaine maritime. "
        "{fr.2}Mais grâce à ses îles, partout sur le globe, plus de quatre-vingt-dix pour cent de ses ZEE sont outre-mer. "
        "La Polynésie française, la Nouvelle-Calédonie, les Terres australes, les îles Éparses…",
        "{-fr}{frc}{frc.1}Résultat : environ dix millions de kilomètres carrés. Le deuxième domaine maritime du monde, juste derrière les États-Unis.",
        "{-frc}{f4}Les anciennes {!puissances coloniales}puissances coloniales y gagnent beaucoup, grâce à leurs îles.",
    ], vis={
        "mer2": dict(type="scene", anim="mer", pas=[4], fs=20),
        "zch": dict(type="chiffres", items=[
            dict(v="1/3", avant="≈ ", t="de la surface des océans est en ZEE", taille=96),
            dict(v="L'essentiel", t="de la pêche et des hydrocarbures en mer", taille=72)], x=90, w=1100, y=200),
        "q3": dict(type="question", t="Qui gagne au partage des mers ?"),
        "fr": dict(type="scene", anim="france", etapes=FRANCE, fs=19,
                   cam={"0": [0, 0, 1000, 437], "1": [370, 20, 260, 114], "2": [0, 0, 1000, 437]}),
        "frc": dict(type="chiffres", items=[dict(v=10, avant="≈ ", apres=" millions de km²", t="de ZEE : le 2e domaine maritime du monde", src="plus de 90 % outre-mer", taille=96)], y=190),
        "f4": dict(type="note", titre="À retenir", t="La ZEE profite aux États côtiers, et surtout aux anciennes puissances coloniales, grâce à leurs îles.", y=220),
    }),

    # ================================================================ IX. nouvelles rivalités
    dict(id="rivalites", chap="De nouvelles rivalités", fond="crise", humeur="tension",
         retenir="Le partage crée des conflits : ZEE qui se chevauchent, îlots, plateau continental jusqu'à 350 milles (CLPC). Juges : Tribunal du droit de la mer (Hambourg), tribunaux arbitraux. 12 juillet 2016 : les « droits historiques » chinois sans base légale ; Pékin rejette.",
         beats=[
        "{q4}Alors, Montego Bay a-t-elle réglé tous les conflits ? Pas du tout. Elle en a même fait naître de nouveaux.",
        "{-q4}{nr}{nr.1}D'abord là où les ZEE se chevauchent : il faut tracer une ligne. "
        "{nr.2}Ensuite autour des îlots : un rocher bien placé peut valoir deux cents milles de mer. "
        "{nr.3}Et sous la mer : un État peut demander d'étendre son plateau continental jusqu'à trois cent cinquante milles. "
        "Il dépose un dossier devant une commission spécialisée, la CLPC.",
        "{-nr}{msb}Et quand on ne s'entend pas ? On peut aller devant un juge. "
        "{msb.1}Le Tribunal international du droit de la mer, installé à Hambourg. {msb.2}Ou bien un tribunal arbitral.",
        "{-msb}{scs}Le cas le plus célèbre, c'est la mer de Chine méridionale. "
        "{scs.1}La Chine y revendique l'essentiel de la mer, à l'intérieur d'une ligne en neuf traits. Au nom de « droits historiques ».",
        "{scs.2}Les Philippines saisissent un tribunal arbitral, à La Haye. Le 12 juillet 2016, la sentence tombe : ces « droits historiques » "
        "n'ont pas de base légale.",
        "{-scs}{nul}Et la réponse de Pékin ? La Chine, pourtant partie à la convention, déclare la sentence {!« nulle et non avenue »}« nulle et non avenue ».",
        "{-nul}{pg2}Deuxième piège : ne crois pas que Montego Bay a supprimé les conflits. Elle en a déplacé certains : "
        "les délimitations, les îlots, le plateau continental.",
    ], vis={
        "q4": dict(type="question", t="Montego Bay a-t-elle réglé tous les conflits ?"),
        "nr": dict(type="liste", titre="Les nouvelles rivalités", items=[
            "Des ZEE qui se chevauchent : il faut délimiter", "Des îlots qui valent 200 milles de mer",
            "Le plateau continental jusqu'à 350 milles, sur dossier (CLPC)"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "msb": dict(type="scene", anim="mers", etapes=MERS_B, fs=20,
                    cam={"0": [0, 0, 1000, 437], "1": [380, 10, 260, 114]}),
        "scs": dict(type="scene", anim="scs", etapes=SCS, fs=19),
        "nul": dict(type="mot", t="« Nulle et non avenue »", g="la réponse de Pékin à la sentence de 2016", taille=84, y=250),
        "pg2": dict(type="note", titre="Piège", t="Montego Bay n'a pas supprimé les conflits : elle en a déplacé certains (délimitations, îlots, plateau continental).", y=210),
    }),

    # ================================================================ X. coopérer contre les menaces communes
    dict(id="menaces", chap="Coopérer contre les menaces communes", fond="ocean", humeur="calme",
         retenir="Piraterie, trafics, pêche illégale, pollution : aucun État ne peut lutter seul. L'OMI fixe les règles des navires ; l'opération européenne Atalanta (décembre 2008) a fait reculer la piraterie au large de la Somalie.",
         beats=[
        "{mc}Mais la mer oblige aussi à coopérer. Pourquoi ? Parce que certaines menaces ignorent les frontières. "
        "{mc.1}La piraterie. {mc.2}Les trafics. {mc.3}La pêche illégale. {mc.4}La pollution. Aucun État ne peut les combattre seul.",
        "{-mc}{omi}Alors on s'organise. Il y a une institution : l'Organisation maritime internationale, l'OMI. "
        "Elle fixe les règles de sécurité des navires, et de lutte contre la pollution.",
        "{-omi}{msc}Et il y a des opérations multinationales. {msc.1}La plus célèbre : l'opération européenne Atalanta, lancée en décembre 2008, "
        "au large de la Somalie. C'est la première opération navale de l'Union européenne. Et elle a fait reculer la piraterie dans l'océan Indien.",
    ], vis={
        "mc": dict(type="liste", titre="Des menaces sans frontières", items=["La piraterie", "Les trafics", "La pêche illégale", "La pollution"],
                   marques=["!", "!", "!", "!"], x=230, y=150, w=820),
        "omi": dict(type="def", terme="OMI", t="L'Organisation maritime internationale fixe les règles de sécurité des navires et de lutte contre leur pollution.", y=220),
        "msc": dict(type="scene", anim="mers", etapes=MERS_C, fs=20, cam={"0": [0, 0, 1000, 437], "1": [450, 110, 320, 140]}),
    }),

    # ================================================================ XI. les grands fonds
    dict(id="fonds", chap="Les grands fonds, patrimoine commun", fond="ocean", humeur="mystere",
         retenir="« La Zone » : fonds au-delà des juridictions nationales, patrimoine commun de l'humanité ; nodules polymétalliques (manganèse, nickel, cobalt, cuivre). L'AIFM (Kingston) accorde des contrats d'exploration ; le code minier n'est pas adopté. Clarion-Clipperton ; contrat français (Ifremer, 2001).",
         beats=[
        "{m3}Descendons maintenant. Tout au fond. Au-delà des eaux des États.",
        "{-m3}{nod}Ces fonds-là, on les appelle « la Zone ». Et ils cachent des trésors. {nod.1}Des nodules polymétalliques : "
        "des boules de minerai, posées sur le fond, riches en manganèse, en nickel, en cobalt, en cuivre. "
        "{nod.2}Mais aussi des encroûtements, sur les reliefs sous-marins. {nod.3}Et des sulfures.",
        "{-nod}{pcm}À qui sont-ils ? À personne en particulier. La convention de 1982 en fait un {!patrimoine commun}patrimoine commun de l'humanité.",
        "{-pcm}{fda}Regarde la carte. {fda.1}Dans le Pacifique, entre Hawaï et le Mexique, la zone de Clarion-Clipperton concentre "
        "les contrats d'exploration de nodules. {fda.2}La France y détient un contrat, obtenu par l'Ifremer en 2001.",
        "{fda.3}Qui accorde ces contrats ? L'Autorité internationale des fonds marins, l'AIFM, installée à Kingston, en Jamaïque. "
        "Elle doit aussi partager les bénéfices.",
        "{-fda}{cm}Mais voilà le hic. Pour passer de l'exploration à l'exploitation, il faut un « code minier ». Et ce code n'est {!toujours pas adopté}toujours pas adopté.",
    ], vis={
        "m3": dict(type="mot", t="Tout au fond", g="au-delà des eaux des États", taille=110, y=250),
        "nod": dict(type="cartes", items=[
            dict(ic="globe", t="Les nodules", q="manganèse, nickel, cobalt, cuivre"),
            dict(ic="vague", t="Les encroûtements", q="sur les reliefs sous-marins"),
            dict(ic="radar", t="Les sulfures", q="d'autres gisements des grands fonds")]),
        "pcm": dict(type="def", terme="Patrimoine commun de l'humanité", t="Statut des fonds marins internationaux (« la Zone ») : leurs ressources sont gérées au profit de tous par l'AIFM.", y=210),
        "fda": dict(type="scene", anim="fonds", etapes=FONDS, fs=20,
                    cam={"0": [0, 0, 1000, 437], "1": [10, 100, 330, 144], "3": [10, 90, 400, 175]}),
        "cm": dict(type="note", titre="Le blocage", t="Le « code minier » qui autoriserait l'exploitation n'est toujours pas adopté.", y=230),
    }),

    # ================================================================ XII. exploiter ou protéger
    dict(id="debat", chap="Exploiter ou protéger ?", fond="crise", humeur="tension",
         retenir="Pour : les métaux de la transition énergétique. Contre : des écosystèmes mal connus, qui mettraient des siècles à se reconstituer ; une trentaine d'États, dont la France, demandent un moratoire. 24 avril 2025 : décret américain pour accélérer les permis ; l'AIFM dénonce une atteinte au droit international.",
         beats=[
        "{dbt}Alors, faut-il exploiter ces fonds ? C'est un vrai débat géopolitique. "
        "{dbt.g}Pour : la transition énergétique a besoin de métaux. Pour les batteries, pour les réseaux électriques. "
        "{dbt.d}Contre : on connaît très mal ces écosystèmes. Et ils mettraient des siècles à se reconstituer.",
        "{-dbt}{mor}Une trentaine d'États, dont la France, demandent un {!moratoire}moratoire : une pause, avant toute exploitation.",
        "{-mor}{fdb}Et les États-Unis ? Ils n'ont pas ratifié la convention. Ils veulent délivrer eux-mêmes des permis. "
        "{fdb.1}Le 24 avril 2025, un décret du président Trump ordonne d'accélérer la délivrance de permis miniers en eaux profondes. "
        "Y compris en haute mer. Il s'appuie sur une loi américaine de 1980.",
        "{-fdb}{tmc}{tmc.1}Dans la foulée, l'entreprise The Metals Company dépose une demande auprès de l'agence américaine NOAA. "
        "{tmc.2}Et l'AIFM dénonce une atteinte au droit international.",
        "{-tmc}{f5}Tu vois le problème ? Une grande puissance peut décider d'agir {!seule}seule, en dehors des règles communes.",
    ], vis={
        "dbt": dict(type="cols", g="Exploiter", gq="les métaux de la transition énergétique", d="Protéger",
                    dq="des écosystèmes mal connus, des siècles pour se reconstituer", vs="?"),
        "mor": dict(type="chiffres", items=[dict(v=30, avant="≈ ", t="États demandent un moratoire", src="dont la France")], y=190),
        "fdb": dict(type="scene", anim="fonds", etapes=FONDS_US, depart=["ccz", "cczt", "haw", "mex", "ifr", "kgn"], fs=20,
                    cam={"0": [0, 50, 420, 184], "1": [0, 50, 420, 184]}),
        "tmc": dict(type="liste", titre="Les États-Unis agissent seuls", items=[
            "The Metals Company dépose une demande auprès de l'agence américaine NOAA",
            "L'AIFM dénonce une atteinte au droit international"], x=170, y=190, w=940),
        "f5": dict(type="note", titre="À retenir", t="Une grande puissance peut agir seule, en dehors des règles communes : la limite du droit.", y=230),
    }),

    # ================================================================ XIII. la haute mer
    dict(id="hautemer", chap="La haute mer, longtemps sans protection", fond="ocean", humeur="mystere",
         retenir="La haute mer : près des deux tiers des océans, mais de l'ordre de 1 % protégé. Ressources génétiques marines convoitées (médicaments, cosmétiques). 2020 : des centaines de navires, en majorité chinois, pêchent le calmar au large des Galápagos, sans rien d'illégal.",
         beats=[
        "{hma}Remontons un peu. Au-delà des ZEE, il y a la haute mer. {hma.1}Elle couvre près des deux tiers des océans.",
        "{-hma}{pct}Et pourtant, seule une infime partie était protégée. {pct.1}De l'ordre de un pour cent.",
        "{-pct}{q5}Pourquoi si peu ? À cause de son principe même : la liberté de la haute mer. "
        "Aucun État ne pouvait y créer une aire marine protégée valable pour tous.",
        "{-q5}{gen}Or les enjeux grandissent. {gen.1}Les ressources génétiques marines intéressent l'industrie : les médicaments, les cosmétiques. "
        "{gen.2}Et la biodiversité recule.",
        "{-gen}{hmb}Un exemple frappant. {hmb.1}Regarde le Pacifique, au large de l'Amérique du Sud : au-delà des ZEE, c'est la haute mer. "
        "{hmb.2}En 2020, des centaines de navires de pêche, en majorité chinois, pêchent intensivement le calmar au large des îles Galápagos. "
        "Juste à la limite de la ZEE de l'Équateur.",
        "Et le pire ? C'était en haute mer. Donc ce n'était {!pas illégal}pas illégal.",
    ], vis={
        "hma": dict(type="chiffres", items=[dict(v="2/3", avant="près des ", t="des océans sont en haute mer", taille=110)], y=190),
        "pct": dict(type="chiffres", items=[dict(v=1, avant="≈ ", apres=" %", t="de la haute mer était protégé", jauge=.01)], y=190),
        "q5": dict(type="question", t="Pourquoi la haute mer était-elle si peu protégée ?"),
        "gen": dict(type="liste", titre="Des enjeux qui grandissent", items=[
            "Les ressources génétiques marines : médicaments, cosmétiques", "Une biodiversité qui recule"], x=200, y=190, w=880),
        "hmb": dict(type="scene", anim="fonds", etapes=HAUTE, depart=["mex"], fs=20,
                    cam={"0": [0, 100, 420, 184], "1": [0, 100, 420, 184], "2": [140, 190, 230, 100]}),
    }),

    # ================================================================ XIV. le traité BBNJ
    dict(id="bbnj", chap="Le traité BBNJ", fond="ocean", humeur="lumiere",
         retenir="BBNJ : adopté à l'ONU le 19 juin 2023, ouvert à la signature le 20 sept. 2023 ; 60e ratification le 19 sept. 2025 ; en vigueur le 17 janv. 2026 (120 jours plus tard). Aires marines protégées en haute mer, partage des ressources génétiques, études d'impact, transferts de technologies.",
         beats=[
        "{m4}C'est pour combler ce vide qu'est né le traité BBNJ. Quatre lettres pour un nom à rallonge : "
        "l'accord sur la biodiversité marine des zones situées au-delà de la juridiction nationale.",
        "{-m4}{bb}Suis bien son parcours, c'est une vraie leçon de droit international. "
        "{bb.1}Il faut près de vingt ans de discussions. "
        "{bb.2}Le texte est adopté à l'ONU le 19 juin 2023. "
        "{bb.3}Il est ouvert à la signature le 20 septembre 2023. Mais attention : signer n'est pas ratifier. Seule la ratification engage l'État.",
        "{bb.4}Alors les ratifications s'accumulent, une à une. Il en faut soixante. "
        "{bb.5}La soixantième arrive le 19 septembre 2025. Et le traité prévoit un délai de cent vingt jours. "
        "{bb.6}Le 17 janvier 2026, il entre en vigueur.",
        "{-bb}{prv}Que prévoit-il ? {prv.1}Des aires marines protégées en haute mer. "
        "{prv.2}Un partage des avantages tirés des ressources génétiques marines. "
        "{prv.3}Des études d'impact environnemental. "
        "{prv.4}Et des transferts de technologies vers les pays du Sud.",
        "{-prv}{nice}Ce traité s'inscrit dans un mouvement plus large. {nice.1}En décembre 2022, la COP quinze biodiversité fixe un objectif : "
        "protéger trente pour cent des terres et des mers d'ici 2030. Le traité BBNJ doit aider à l'atteindre. "
        "{nice.2}Puis un coup d'accélérateur vient de France. Du 9 au 13 juin 2025, Nice accueille la conférence des Nations unies sur l'océan, "
        "coorganisée par la France et le Costa Rica. Elle accélère les ratifications.",
        "{-nice}{pg3}Attention à deux pièges. Ne confonds pas BBNJ, la biodiversité de la haute mer en 2023, et Montego Bay, le partage des espaces en 1982. "
        "Et n'écris pas que le traité est « en négociation » : il est en vigueur depuis le 17 janvier 2026.",
    ], vis={
        "m4": dict(type="def", terme="BBNJ", t="Accord sur la biodiversité marine des zones situées au-delà de la juridiction nationale.", y=220),
        "bb": dict(type="scene", anim="t1bbnj", fs=20),
        "prv": dict(type="liste", titre="Ce que prévoit le traité BBNJ", items=[
            "Des aires marines protégées en haute mer", "Un partage des avantages tirés des ressources génétiques marines",
            "Des études d'impact environnemental", "Des transferts de technologies vers les pays du Sud"], marques=["1", "2", "3", "4"], x=150, y=140, w=980),
        "nice": dict(type="chrono", titre="Accélérer", items=[
            dict(d="Déc. 2022", t="COP15 biodiversité : protéger 30 % des terres et des mers d'ici 2030", c="droit"),
            dict(d="9-13 juin 2025", t="Conférence de l'ONU sur l'océan à Nice (France, Costa Rica)", c="mer")], x=230, w=820, y=150, h=420),
        "pg3": dict(type="note", titre="Pièges", t="BBNJ (haute mer, 2023) ≠ Montego Bay (partage, 1982). Et BBNJ n'est plus « en négociation » : en vigueur depuis le 17 janvier 2026.", y=200),
    }),

    # ================================================================ XV. les limites
    dict(id="gouvernance", chap="Les limites de la gouvernance des océans", fond="crise", humeur="calme",
         retenir="Un traité n'engage que ceux qui le ratifient ; contrôles difficiles en haute mer ; pavillons de complaisance. Mais des progrès : accord de l'OMC sur les subventions à la pêche, adopté le 17 juin 2022, en vigueur le 15 septembre 2025.",
         beats=[
        "{lim}Alors, la haute mer est sauvée ? Pas si vite. {lim.1}Un traité n'engage que ceux qui le ratifient. Et les grandes puissances maritimes "
        "ne le font pas toujours. {lim.2}En haute mer, les contrôles sont difficiles. "
        "{lim.3}Et les pavillons de complaisance diluent les responsabilités.",
        "{-lim}{omc}Mais il y a des progrès, par le commerce et la pêche. {omc.1}Le 17 juin 2022, l'Organisation mondiale du commerce adopte un accord. "
        "Il interdit certaines subventions à la pêche illégale, et à la pêche de stocks surexploités. "
        "{omc.2}Il entre en vigueur le 15 septembre 2025. C'est un rare accord mondial contraignant sur la pêche.",
        "{-omc}{bil}Bilan de ce dossier. {bil.1}Coopérer, c'est possible : l'ISS, Montego Bay, BBNJ le prouvent. "
        "{bil.2}Mais la coopération bute sur les rivalités. {bil.3}Et elle avance quand l'intérêt commun est évident.",
    ], vis={
        "lim": dict(type="liste", titre="Les limites", items=[
            "Un traité n'engage que ceux qui le ratifient", "Des contrôles difficiles en haute mer",
            "Des pavillons de complaisance qui diluent les responsabilités"], marques=["✗", "✗", "✗"], x=170, y=170, w=940),
        "omc": dict(type="chrono", titre="Un accord sur la pêche", items=[
            dict(d="17 juin 2022", t="L'OMC adopte l'accord sur les subventions à la pêche", c="droit"),
            dict(d="15 sept. 2025", t="Il entre en vigueur : un rare accord mondial contraignant", c="mer")], x=230, w=820, y=150, h=420),
        "bil": dict(type="cartes", items=[
            dict(ic="balance", t="Coopérer, c'est possible", q="ISS, Montego Bay, BBNJ"),
            dict(ic="drapeau", t="Mais des rivalités", q="Chine exclue, sentence rejetée, décret américain"),
            dict(ic="globe", t="Quand l'intérêt est commun", q="la coopération progresse")]),
    }),

    # ================================================================ XVI. au bac : la dissertation
    dict(id="dissert", chap="Au bac : la dissertation", fond="archive", humeur="calme", beats=[
        "{bac}Passons au bac. {bac.1}À l'écrit, ce thème n'est pas au programme de la session 2027 : il revient en 2028. "
        "{bac.2}Et le sujet de 2028 peut porter sur lui. {bac.3}En attendant, il reste un excellent terrain pour le Grand oral, chaque année.",
        "{-bac}{sujet}Voici un sujet de dissertation, inventé pour l'entraînement : "
        "« Coopérer dans les océans et dans l'espace : un idéal impossible ? »",
        "{sujet.1}Analyse les termes. « Coopérer » : agir ensemble, entre États rivaux, et avec d'autres acteurs. "
        "« Un idéal impossible », avec un point d'interrogation : le sujet t'invite à discuter. Ni oui, ni non, d'emblée. "
        "{sujet.2}Puis trouve une problématique. {sujet.3}Et construis un plan en trois parties, avec des exemples datés.",
        "{-sujet}{pz}À toi ! Mets la vidéo sur pause. Prends cinq minutes, une feuille, et cherche une problématique et un plan.{pz.stop}",
        ("P", 2.0),
        "{-pz}{pb}Voici une proposition. La problématique : pourquoi des États rivaux coopèrent-ils dans les océans et l'espace, "
        "et jusqu'où cette coopération peut-elle aller ?",
        "{-pb}{pl}Et le plan, en trois parties. "
        "{pl.1}Un : des coopérations réelles, fondées sur des intérêts communs. L'ISS, avec l'accord de 1998 et une station occupée depuis 2000. "
        "Montego Bay, en 1982. L'opération Atalanta, en 2008. Et le traité BBNJ, en vigueur en 2026.",
        "{pl.2}Deux : des coopérations limitées par les rivalités de puissance. La Chine exclue de l'ISS en 2011. "
        "Les blocs lunaires : Artemis contre l'ILRS. La sentence de 2016, rejetée par Pékin. Et le décret américain sur les grands fonds, en 2025.",
        "{pl.3}Trois : une coopération qui progresse quand l'intérêt commun est évident. L'échange de sièges, malgré la guerre, en 2022. "
        "L'accord de l'OMC sur la pêche, en vigueur en 2025. Et le traité BBNJ, entré en vigueur dès 2026.",
        "{-pl}{rep}Ta réponse finale ? Ce n'est pas un idéal impossible. C'est un idéal {!limité}limité : "
        "la coopération avance quand elle sert les intérêts des puissances.",
        "{-rep}{me}Un dernier conseil de méthode. Chaque paragraphe tient en quatre temps : une idée, une explication, "
        "un exemple précis, daté, et une phrase de liaison.",
    ], vis={
        "bac": dict(type="liste", titre="Le thème 1 au bac", items=[
            "2027 : pas à l'écrit", "2028 : à l'écrit", "Grand oral : un excellent terrain, chaque année"],
            marques=["✗", "✓", "✓"], x=170, y=190, w=940),
        "sujet": dict(type="exo", niveau="dissert", titre="Coopérer dans les océans et dans l'espace : un idéal impossible ?",
                      src="Sujet de dissertation inventé pour l'entraînement (thème 1, axe 2)",
                      questions=["Analyse les termes du sujet", "Trouve une problématique", "Construis un plan en trois parties"]),
        "pz": dict(type="pause", t="Une problématique et un plan en trois parties pour ce sujet.",
                   sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "pb": dict(type="def", terme="Problématique", t="Pourquoi des États rivaux coopèrent-ils dans les océans et l'espace, et jusqu'où cette coopération peut-elle aller ?", y=190),
        "pl": dict(type="liste", titre="Un plan possible", items=[
            "Des coopérations réelles, fondées sur des intérêts communs — ISS (1998, occupée depuis 2000), Montego Bay (1982), Atalanta (2008), BBNJ (2026)",
            "Des coopérations limitées par les rivalités — Chine exclue (2011), Artemis contre ILRS, sentence de 2016 rejetée, décret américain (2025)",
            "Une coopération qui progresse quand l'intérêt commun est évident — échange de sièges (2022), accord de l'OMC sur la pêche (2025), BBNJ"],
            marques=["I", "II", "III"], x=130, y=110, w=1020),
        "rep": dict(type="mot", t="Un idéal limité", g="la coopération avance quand elle sert les intérêts des puissances", taille=110, y=250),
        "me": dict(type="note", titre="Méthode", t="Un paragraphe = une idée, une explication, un exemple précis et daté, une phrase de liaison.", y=230),
    }),

    # ================================================================ XVII. au Grand oral
    dict(id="oral", chap="Au Grand oral : argumenter", fond="archive", humeur="calme", beats=[
        "{go}Deuxième entraînement, pour l'oral cette fois. Voici la question : "
        "« Le droit international peut-il réguler les rivalités dans les océans et dans l'espace ? »",
        "{go.1}C'est la question qui guide tout le thème. {go.2}Ta mission : trouver deux arguments pour, et deux arguments contre. "
        "Chacun avec un exemple daté de ce chapitre.",
        "{-go}{pz3}À toi ! Mets sur pause, et cherche tes quatre arguments.{pz3.stop}",
        ("P", 2.0),
        "{-pz3}{arg}Correction. {arg.g}Pour, d'abord. Le droit existe, et il fonctionne souvent : Montego Bay a mis fin à beaucoup de conflits de pêche. "
        "Et il progresse : le traité BBNJ est en vigueur en 2026, l'accord de l'OMC sur la pêche en 2025. "
        "Même les rivaux coopèrent quand l'intérêt commun est évident : pense à l'échange de sièges de 2022.",
        "{arg.d}Contre, maintenant. Les grandes puissances l'ignorent quand il les gêne : la Chine rejette la sentence de 2016, "
        "et les États-Unis n'ont pas ratifié Montego Bay. Il reste des vides, comme l'exploitation minière des grands fonds. "
        "Et surtout, le droit international n'a pas de police : personne ne peut forcer un État à respecter une décision.",
        "{-arg}{bilo}Ta conclusion, en une phrase : le droit international encadre et apaise… mais il ne s'impose aux puissances "
        "que si elles y trouvent leur {!intérêt}intérêt.",
    ], vis={
        "go": dict(type="exo", niveau="Grand oral · s'entraîner", titre="Le droit international peut-il réguler les rivalités dans les océans et l'espace ?",
                   src="Question d'entraînement pour le Grand oral (thème 1)",
                   questions=["C'est la question directrice du thème", "Deux arguments pour, deux contre, chacun avec un exemple daté"]),
        "pz3": dict(type="pause", t="Deux arguments pour, deux arguments contre, avec un exemple daté chacun.",
                    sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "arg": dict(type="cols", g="Oui", gq="Montego Bay ; BBNJ (2026) ; accord de l'OMC (2025) ; échange de sièges (2022)", d="Non",
                    dq="sentence de 2016 rejetée ; Montego Bay non ratifiée par les États-Unis ; grands fonds ; pas de police", vs="?"),
        "bilo": dict(type="note", titre="Conclusion", t="Le droit international encadre et apaise, mais ne s'impose aux puissances que si elles y trouvent intérêt.", y=220),
    }),

    # ================================================================ XVIII. les pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="crise", humeur="calme", beats=[
        "{pgs}Avant le récap, les cinq pièges qui coûtent des points. "
        "{pgs.1}Un : présenter l'ISS comme une coopération sans arrière-pensée. "
        "{pgs.2}Deux : croire que Montego Bay a supprimé les conflits. "
        "{pgs.3}Trois : confondre BBNJ et Montego Bay. "
        "{pgs.4}Quatre : écrire que le traité BBNJ est encore « en négociation ». "
        "{pgs.5}Et cinq : oublier que les États-Unis n'ont pas ratifié la convention de 1982.",
    ], vis={
        "pgs": dict(type="liste", titre="Les cinq pièges", items=[
            "L'ISS, une coopération sans arrière-pensée ? Non : prestige américain, Chine exclue",
            "Montego Bay n'a pas supprimé les conflits : elle en a déplacé",
            "BBNJ (haute mer, 2023) ≠ Montego Bay (partage, 1982)",
            "BBNJ n'est plus « en négociation » : en vigueur depuis le 17 janvier 2026",
            "Les États-Unis n'ont pas ratifié la convention de 1982"], marques=["✗", "✗", "✗", "✗", "✗"], x=130, y=110, w=1020),
    }),

    # ================================================================ XIX. récap
    dict(id="recap", chap="Récap pour le bac", fond="crise", humeur="lumiere", beats=[
        "{dat}Il est temps de tout ranger. Les dates, d'abord. {dat.1}1982, Montego Bay. {dat.2}1994, son entrée en vigueur. "
        "{dat.3}1998, l'accord sur l'ISS. {dat.4}2000, la station occupée pour de bon. {dat.5}2008, Atalanta. "
        "{dat.6}2011, la Chine exclue. {dat.7}2016, la sentence sur la mer de Chine méridionale. "
        "{dat.8}2022, l'échange de sièges. {dat.9}2025, le décret américain sur les grands fonds. "
        "{dat.10}Et 2026, le traité BBNJ en vigueur.",
        ("P", 1.8),
        "{-dat}{cmr}Et la carte du chapitre. {cmr.1}La Station spatiale internationale. {cmr.2}Le partage des mers. "
        "{cmr.3}Les grands fonds. {cmr.4}Et la haute mer.",
        ("P", 1.2),
        "{-cmr}{qd}Garde en tête la question du thème : le droit international peut-il réguler les rivalités de puissance, "
        "dans les océans et dans l'espace ? Ce chapitre te donne la réponse : il encadre, il apaise… quand les puissances y trouvent leur intérêt.",
        "{-qd}{fin}Les fiches, les QCM, la frise et les animations du chapitre t'attendent sur le site Ligne rouge : "
        "le lien est dans la description. Prochain dossier : la Chine, à la conquête de l'espace, des mers et des océans. À très vite.",
        ("P", 2.5),
    ], vis={
        "dat": dict(type="chrono", titre="Les dates du chapitre", items=[
            dict(d="1982", t="Montego Bay", c="droit"), dict(d="1994", t="Montego Bay en vigueur", c="droit"),
            dict(d="1998", t="Accord sur l'ISS", c="espace"), dict(d="2000", t="L'ISS occupée en permanence", c="espace"),
            dict(d="2008", t="Opération Atalanta", c="mer"), dict(d="2011", t="La Chine exclue de l'ISS", c="conflit"),
            dict(d="2016", t="Sentence sur la mer de Chine", c="conflit"), dict(d="2022", t="Échange de sièges", c="espace"),
            dict(d="2025", t="Décret américain sur les grands fonds", c="conflit"), dict(d="2026", t="Traité BBNJ en vigueur", c="mer")],
            x=60, w=1160, y=120, h=470),
        "cmr": dict(type="carte", centre="Coopérer en mer et dans l'espace", branches=[
            dict(t="L'ISS", items=["15 pays (1998)", "interdépendance", "Chine exclue (2011)"]),
            dict(t="Partager les mers", items=["Montego Bay (1982)", "ZEE : 200 milles", "sentence de 2016"]),
            dict(t="Les grands fonds", items=["patrimoine commun", "AIFM, Kingston", "décret américain (2025)"]),
            dict(t="La haute mer", items=["2/3 des océans", "BBNJ en vigueur (2026)", "accord de l'OMC (2025)"])]),
        "qd": dict(type="question", t="Le droit international peut-il réguler les rivalités de puissance dans les océans et l'espace ?"),
        "fin": dict(type="mot", t="Ligne rouge", g="Fiches, QCM, frise et animations : le lien est dans la description.", taille=110, y=250),
    }),
]

QUIZ = [
    dict(q="Depuis quand l'ISS est-elle occupée en permanence ?", r=["1986", "20 novembre 1998", "2 novembre 2000", "2011"], ok=2,
         ex="Le 20 novembre 1998, c'est le lancement du premier module, Zarya ; l'occupation permanente commence le 2 novembre 2000.", voir="iss1"),
    dict(q="Quel pays est exclu de l'ISS par une loi américaine de 2011 ?", r=["La Russie", "Le Japon", "La Chine", "L'Inde"], ok=2,
         ex="L'amendement Wolf interdit à la NASA de coopérer avec la Chine, qui construit donc Tiangong.", voir="esb"),
    dict(q="Comment les astronautes américains rejoignaient-ils l'ISS entre 2011 et 2020 ?", r=["Par la navette", "Par les Soyouz russes",
                                                                                                "Par des fusées chinoises", "Par Ariane 5"], ok=1,
         ex="Après l'arrêt de la navette (juillet 2011), seuls les Soyouz russes y menaient, jusqu'à Crew Dragon (mai 2020).", voir="iss2"),
    dict(q="Les accords Artemis (2020) sont…", r=["un traité de l'ONU", "des accords proposés par les États-Unis pour encadrer l'exploration lunaire",
                                                 "un accord sino-russe", "un accord sur la pêche"], ok=1,
         ex="Proposés par les États-Unis le 13 octobre 2020, plus de 70 signataires en 2026 ; la Chine et la Russie portent un projet rival (ILRS).", voir="esc"),
    dict(q="En quelle année la convention de Montego Bay entre-t-elle en vigueur ?", r=["1958", "1982", "1994", "2023"], ok=2,
         ex="Signée le 10 décembre 1982, elle entre en vigueur le 16 novembre 1994.", voir="msa"),
    dict(q="Quel pays possède le deuxième domaine maritime (ZEE) du monde ?", r=["La Chine", "La France", "Le Royaume-Uni", "La Russie"], ok=1,
         ex="La France, avec environ 10 millions de km² de ZEE, dont plus de 90 % outre-mer, derrière les États-Unis.", voir="fr"),
    dict(q="Que décide la sentence arbitrale du 12 juillet 2016 ?", r=["Elle donne raison à la Chine",
                                                                     "Elle juge sans base légale les « droits historiques » chinois en mer de Chine méridionale",
                                                                     "Elle partage l'Arctique", "Elle crée la ZEE"], ok=1,
         ex="Pékin, pourtant partie à la convention, la déclare « nulle et non avenue ».", voir="scs"),
    dict(q="Quelle opération européenne lutte contre la piraterie au large de la Somalie depuis 2008 ?", r=["Barkhane", "Atalanta", "Aspides", "Chammal"], ok=1,
         ex="Atalanta (décembre 2008), première opération navale de l'Union européenne.", voir="msc"),
    dict(q="Où se trouve la zone de Clarion-Clipperton ?", r=["Dans l'Arctique", "Dans le Pacifique, entre Hawaï et le Mexique", "En mer de Chine", "Dans l'océan Indien"], ok=1,
         ex="C'est la principale zone d'exploration des nodules polymétalliques ; la France y a un contrat (Ifremer, 2001).", voir="fda"),
    dict(q="Qu'a ordonné le décret américain du 24 avril 2025 ?", r=["Un moratoire sur l'exploitation minière",
                                                                    "D'accélérer les permis miniers en eaux profondes, y compris en haute mer",
                                                                    "La ratification de Montego Bay", "La fin de l'ISS"], ok=1,
         ex="Les États-Unis contournent l'AIFM en s'appuyant sur une loi américaine de 1980.", voir="fdb"),
    dict(q="Quand le traité BBNJ entre-t-il en vigueur ?", r=["Le 19 juin 2023", "Le 20 septembre 2023", "Le 19 septembre 2025", "Le 17 janvier 2026"], ok=3,
         ex="Adopté en 2023, il entre en vigueur 120 jours après sa 60e ratification (19 septembre 2025), soit le 17 janvier 2026.", voir="bb"),
    dict(q="Que permet notamment le traité BBNJ ?", r=["Exploiter les nodules en haute mer", "Créer des aires marines protégées en haute mer",
                                                       "Étendre les ZEE à 300 milles", "Interdire la pêche partout"], ok=1,
         ex="Aires marines protégées, partage des ressources génétiques, études d'impact, transferts de technologies.", voir="prv"),
]

CREDITS = [
    "Cartes : fond Natural Earth (domaine public), projections d3-geo (licence ISC) ; ZEE françaises approchées par des cercles de 200 milles, "
    "zone de Clarion-Clipperton et ligne en neuf traits : tracés schématiques.",
    "Schémas animés : la Station spatiale internationale, la course aux mers, le traité BBNJ (site Ligne rouge).",
    "Photographie : la Station spatiale internationale vue depuis la navette Atlantis, mai 2010, NASA (domaine public), via Wikimedia Commons.",
    "Sujet de dissertation inventé pour l'entraînement.",
]
