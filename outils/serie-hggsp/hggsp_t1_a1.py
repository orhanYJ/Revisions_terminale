"""HGGSP, thème 1, axe 1 : « Conquêtes, affirmations de puissance et rivalités » — le chapitre en vidéo.

Même chaîne et même identité que la vidéo pilote (hggsp_t1_intro.py) : la table des cartes de l'état-major, moteur
hggsp/serie/moteur.js. Contenu : le chapitre « t1-a1 » du site (outils/specialites/hggsp/src/data-t1.js) et ses
animations (« espace » : la course à l'espace sur la carte ; « t1asat » : les tirs antisatellites), rien au-delà ;
le sujet de dissertation est celui du chapitre ; le sujet de juin 2025 et son plan viennent du dossier du thème 1
(data-dossiers.js) ; les données de l'épreuve, de la page « L'épreuve » (data-commun.js).

Scènes de carte (avant la voix, à refaire si une animation du site ou la carte « marine » change) :
    node outils/serie-hggsp/scenes.js hggsp-t1-a1        → hggsp/serie/illu-hggsp-t1-a1.js
(la carte « marine », propre à la vidéo, est dans outils/serie-hggsp/cartes-hggsp-t1-a1.js).
Contrôles : python3 outils/serie-philo/verifier.py hggsp_t1_a1 ;
brouillon sans voix : SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py hggsp_t1_a1 ;
puis chevauchements.py hggsp-t1-a1 et fermer.py hggsp_t1_a1.
"""

SITE = "hggsp"
CODE = "hggsp-t1-a1"
NOTION = "De nouveaux espaces de conquête"
NUM = 2
TITRE = "Conquêtes, affirmations de puissance et rivalités"
SUIVANT = "Thème 1 · Axe 2 · Enjeux diplomatiques et coopérations"
RYTHME = "vivant"
PRONONCIATION = {"milles marins": "mil marins", "milles": "mil marins",
                 "Wernher von Braun": "Vèrnère fonne Braoune", "R-7": "R sept", "Baïkonour": "Baï-konour",
                 "Laïka": "La-ïka", "Vostok": "Vostoque", "Terechkova": "Térechkova", "Leonov": "Léonov",
                 "Alexeï": "Alexéï", "Khrouchtchev": "Krouchtchève", "Explorer": "Èxploreur",
                 "Canaveral": "Canavéral", "Armstrong": "Armstrongue", "Buzz": "Beuze", "Aldrin": "Aldrine",
                 "Reagan": "Rigann", "Soyouz": "Soyouze",
                 "CNES": "Cnèsse", "Hammaguir": "Hamaguir", "Galileo": "Galiléo", "GPS": "G P S",
                 "Tiangong": "Tiane-gongue", "Chang'e": "Tchang-eu", "ISRO": "Issro", "Mangalyaan": "Mangalyane",
                 "Chandrayaan": "Tchandrayane", "Gaganyaan": "Gaganyane", "Hope": "Hôp", "Neil": "Nil", "V2": "V deux",
                 "SpaceX": "Spèïce X", "Starlink": "Star-linque", "Elon Musk": "Ilonne Meusk",
                 "Blue Origin": "Blou Orijinne", "New Glenn": "Niou Glène", "Jeff Bezos": "Djèf Bézosse",
                 "Rocket Lab": "Roquette Labe", "Starbase": "Star-bèïse", "Mahia": "Maïa", "Wenchang": "Ouène-tchangue",
                 "Artemis": "Artémisse", "Jeremy Hansen": "Djérémi Hanssène", "Fengyun": "Feng-yune",
                 "Shakti": "Chakti", "Kosmos": "Kosmosse", "Kessler": "Kesslère", "Space Force": "Spèïce Forsse",
                 "Louch-Olymp": "Louch Olimpe", "Athena-Fidus": "Athéna Fidusse", "Alfred Mahan": "Alfrède Mahane",
                 "Mahan": "Mahane", "SNLE": "S N L E", "SNA": "S N A", "Brest": "Bresste", "Triomphant": "Triomphan",
                 "Daech": "Daèche", "Fujian": "Fou-djiane", "Sanya": "Sania",
                 "Hainan": "Haï-nane", "Bab el-Mandeb": "Babe el Mandèbe", "Ormuz": "Ormouze", "Malacca": "Malaka",
                 "Houthis": "Houtis", "houthis": "houtis", "Galaxy Leader": "Galaxi Lideur",
                 "Prosperity Guardian": "Prospériti Gardiane", "Aspides": "Aspidèsse", "Bahreïn": "Ba-rèïne",
                 "Norfolk": "Norfolque", "San Diego": "Sanne Diégo", "Yokosuka": "Yokoska", "URSS": "U R S S",
                 "NASA": "Nassa", "ASAT": "A-sat"}

# ---------------------------------------------------------------- étapes des cartes propres à la vidéo
ESPACE_V = [128, 29, 840, 374]  # cadrage d'ensemble de la carte « espace » du site
MARINE_V = [0, 0, 1000, 437]    # cadrage d'ensemble de la carte « marine »
ESP_NEW = [
    dict(date="2015-2024", titre="Starbase, la base de SpaceX", montre=["starb"], accent=["starb"]),
    dict(date="2018", titre="Mahia : Rocket Lab en Nouvelle-Zélande", montre=["mahia"], accent=["mahia"]),
    dict(date="2016", titre="Wenchang, la base côtière chinoise", montre=["wench"], accent=["wench"]),
]
MAR_US = [
    dict(date="Depuis 1945", titre="La première puissance navale", montre=["us", "us2"], accent=["us", "us2"]),
    dict(date="Méditerranée", titre="La 6e flotte, à Naples", montre=["f6"], accent=["f6"]),
    dict(date="Golfe", titre="La 5e flotte, à Bahreïn", montre=["f5"], accent=["f5"]),
    dict(date="Pacifique", titre="La 7e flotte, au Japon", montre=["f7"], accent=["f7"]),
]
MAR_SNLE = [
    dict(date="Les SNLE", titre="Cinq puissances nucléaires reconnues, et l'Inde",
         montre=["sn1", "sn2", "sn3", "sn4", "sn5", "sn6", "sn7", "sn8"], accent=["sn1", "sn2", "sn3", "sn4", "sn5", "sn6", "sn7", "sn8"]),
    dict(date="France", titre="L'Île Longue : 4 SNLE, missile M51", montre=["ilt"], cache=["sn2"], accent=["sn1"]),
]
MAR_PROJ = [
    dict(date="Depuis 2001", titre="Le Charles-de-Gaulle, port d'attache Toulon", montre=["toulon"], accent=["toulon"]),
    dict(date="2015", titre="Opération Chammal : frapper Daech", montre=["chammal", "chamt"], accent=["chammal"]),
    dict(date="Nov. 2024 - avr. 2025", titre="Mission Clemenceau 25", montre=["clem", "clemt"], cache=["chamt"], accent=["clem"]),
    dict(date="5 nov. 2025", titre="Le Fujian, 3e porte-avions chinois, à Sanya", montre=["sanya"], accent=["sanya"]),
]
MAR_BASES = [
    dict(date="Détroit", titre="Ormuz", montre=["ch1"], accent=["ch1"]),
    dict(date="Détroit", titre="Bab el-Mandeb", montre=["ch2"], accent=["ch2"]),
    dict(date="Détroit", titre="Malacca", montre=["ch3"], accent=["ch3"]),
    dict(date="1er août 2017", titre="Djibouti : des bases étrangères côte à côte", montre=["djib", "djibt"], accent=["djib"]),
]
MAR_ROUGE = [
    dict(date="Nov. 2023", titre="Les Houthis attaquent en mer Rouge", montre=["houthis", "houthist"], accent=["houthis"]),
    dict(date="19 nov. 2023", titre="La saisie du Galaxy Leader", montre=["galaxy"], accent=["galaxy"]),
    dict(date="Déc. 2023", titre="Opération Prosperity Guardian (États-Unis)", montre=["pg", "pgt"], accent=["pg"]),
    dict(date="Févr. 2024", titre="Opération Aspides (Union européenne)", montre=["aspides", "aspt"], accent=["aspides"]),
]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="orbite", humeur="mystere", carton=False, beats=[
        "{tab_sp}Le quatre octobre mille neuf cent cinquante-sept, un petit signal fait le tour de la Terre. Bip… bip… bip. "
        "Toutes les quatre-vingt-seize minutes.",
        "C'est Spoutnik un. Une sphère de métal d'un peu plus de quatre-vingt-trois kilos, lancée par l'Union soviétique.",
        ("P", 0.6),
        "{-tab_sp}{q1}Une boule qui fait bip. Et pourtant, aux États-Unis, c'est la panique. Pourquoi ?",
        "{-q1}{f0}Parce que la fusée qui l'a lancée est un {!missile}missile. Et si l'URSS peut placer un satellite en orbite, "
        "elle peut aussi frapper l'Amérique avec une bombe nucléaire.",
        ("P", 0.5),
        "{-f0}{plan}Voilà tout l'esprit de ce chapitre : conquérir un espace, c'est affirmer sa puissance. "
        "{plan.1}On verra d'abord la course à l'espace, en pleine guerre froide. "
        "{plan.2}Puis l'arrivée de nouveaux acteurs : la Chine, l'Inde, et les entreprises. "
        "{plan.3}Ensuite, une question inquiétante : l'espace devient-il un champ de bataille ? "
        "{plan.4}Puis la mer, où la puissance s'affirme par les sous-marins et les porte-avions. "
        "{plan.5}Et pour finir, le bac : un sujet de dissertation, corrigé.",
        "{-plan}{bac0}Un mot sur l'examen. Ce thème n'est pas à l'écrit en deux mille vingt-sept. Il y revient en deux mille vingt-huit. "
        "Et c'est un excellent terrain pour le Grand oral. Alors on y va.",
        "{-bac0}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_sp": dict(type="tableau", img="t1-spoutnik", de=[1.0, .5, .5], a=[1.16, .6, .45],
                       legende="Réplique de Spoutnik 1, NSSDC / NASA (domaine public, Wikimedia Commons)"),
        "q1": dict(type="question", t="Une boule de métal qui fait « bip » : pourquoi l'Amérique a-t-elle peur ?"),
        "f0": dict(type="note", titre="4 octobre 1957", t="Le lanceur de Spoutnik est un missile : il pourrait porter une bombe nucléaire jusqu'en Amérique.", y=230),
        "plan": dict(type="liste", titre="Le dossier", items=[
            "La course à l'espace, un enjeu de la guerre froide", "De nouveaux acteurs : un espace multipolaire et privatisé",
            "L'espace, nouveau champ de bataille ?", "Affirmer sa puissance à partir des mers",
            "Au bac : une dissertation corrigée"], marques=["I", "II", "III", "IV", "✎"], x=150, y=120, w=980),
        "bac0": dict(type="note", titre="Au bac", t="Thème 1 : pas à l'écrit en 2027, à l'écrit en 2028. Et toujours au Grand oral.", y=230),
        "titre": dict(type="titre", sur="HGGSP · Thème 1 · Axe 1", t="Conquêtes, affirmations de puissance et rivalités",
                      sous="De nouveaux espaces de conquête"),
    }),

    # ================================================================ I.1 des fusées nées des missiles
    dict(id="missiles", chap="Des fusées nées des missiles", fond="orbite", humeur="mystere",
         retenir="Les fusées naissent des missiles : V2 allemands récupérés après 1945, puis R-7 soviétique (août 1957), qui lance Spoutnik 1 le 4 octobre 1957. Aux États-Unis : le « choc Spoutnik ».",
         beats=[
        "{m45}Remontons en mille neuf cent quarante-cinq. L'Allemagne nazie est vaincue. Elle laisse derrière elle des fusées V2, et les ingénieurs qui les ont conçues. "
        "Les deux Grands se jettent dessus. "
        "{-m45}{v2}{v2.g}L'ingénieur Wernher von Braun part travailler pour les États-Unis. "
        "{v2.d}L'URSS, elle aussi, récupère des ingénieurs et des V2.",
        "{-v2}{r7}Douze ans plus tard. {r7.1}En août mille neuf cent cinquante-sept, l'URSS réussit le premier tir de missile intercontinental : le R-7. "
        "{r7.2}Et le quatre octobre, c'est la même fusée qui place Spoutnik en orbite. Quatre-vingt-trois virgule six kilos, "
        "un tour de la Terre en quatre-vingt-seize minutes.",
        "{-r7}{esp1}Sur la carte, regarde d'où elle part. {esp1.1}De Baïkonour, la base de lancement soviétique. "
        "C'est aussi de là que décollera Gagarine.",
        "{-esp1}{choc}Aux États-Unis, c'est le {!choc Spoutnik}choc Spoutnik. Le raisonnement est implacable : "
        "un lanceur capable de mettre un satellite en orbite peut aussi envoyer une bombe nucléaire sur l'Amérique.",
        "{-choc}{f1}Alors retiens bien ceci. La course à l'espace, c'est d'abord une course aux missiles. "
        "Les lanceurs sont les cousins des missiles intercontinentaux.",
    ], vis={
        "m45": dict(type="mot", t="1945", g="Les deux Grands récupèrent les V2 allemands et leurs ingénieurs", taille=150, y=210),
        "v2": dict(type="cols", g="États-Unis", gq="l'ingénieur du V2, Wernher von Braun", d="URSS",
                   dq="des ingénieurs et des V2 allemands", vs="1945"),
        "r7": dict(type="chrono", titre="1957 : du missile au satellite", items=[
            dict(d="Août 1957", t="Le R-7, premier missile intercontinental", c="conflit"),
            dict(d="4 oct. 1957", t="Spoutnik 1 : 83,6 kg, un tour en 96 minutes", c="espace")], x=290, w=700, y=150, h=420),
        "esp1": dict(type="scene", anim="espace", pas=[0], fs=20,
                     cam={"0": ESPACE_V, "1": [470, 20, 330, 162]}),
        "choc": dict(type="def", terme="Le « choc Spoutnik »", t="Si l'URSS peut placer un satellite en orbite, elle peut frapper l'Amérique avec une bombe nucléaire.", y=220),
        "f1": dict(type="note", titre="À retenir", t="La course à l'espace est d'abord militaire : les lanceurs sont des cousins des missiles intercontinentaux.", y=230),
    }),

    # ================================================================ I.2 les victoires soviétiques
    dict(id="premieres", chap="Les victoires soviétiques", fond="orbite", humeur="lumiere",
         retenir="L'URSS gagne presque toutes les « premières » : Laïka (1957), Luna 2 et Luna 3 (1959), Gagarine (12 avril 1961, 108 min), Terechkova (16 juin 1963), Leonov (18 mars 1965).",
         beats=[
        "{pr}Et l'URSS ne s'arrête pas là. Elle enchaîne les premières. "
        "{pr.1}Le trois novembre mille neuf cent cinquante-sept, la chienne Laïka devient le premier être vivant en orbite. "
        "{pr.2}En mille neuf cent cinquante-neuf, la sonde Luna deux est la première à atteindre la Lune. "
        "{pr.3}La même année, Luna trois rapporte les premières images de sa face cachée.",
        "{pr.4}Et le douze avril mille neuf cent soixante et un… Youri Gagarine. "
        "À bord de Vostok un, il fait le tour de la Terre en cent huit minutes. C'est le premier homme dans l'espace. "
        "Il devient un héros mondial. Et un formidable outil de propagande pour le régime de Khrouchtchev.",
        "{pr.5}Le seize juin mille neuf cent soixante-trois, Valentina Terechkova est la première femme dans l'espace. "
        "{pr.6}Et le dix-huit mars mille neuf cent soixante-cinq, Alexeï Leonov sort de son vaisseau : première sortie dans l'espace.",
        ("P", 0.6),
        "{-pr}{but}Pourquoi toutes ces premières ? Pour démontrer la {!supériorité du socialisme}supériorité du socialisme. "
        "Chaque record est une victoire de propagande, montrée au monde entier.",
        "{-but}{pg1}Et voici un piège classique : oublier que l'URSS a gagné presque toutes les premières avant mille neuf cent soixante-neuf. "
        "Dans les années soixante, c'est Moscou qui mène.",
    ], vis={
        "pr": dict(type="chrono", titre="Les « premières » soviétiques", items=[
            dict(d="3 nov. 1957", t="Laïka, premier être vivant en orbite", c="conflit"),
            dict(d="1959", t="Luna 2 atteint la Lune", c="conflit"),
            dict(d="1959", t="Luna 3 : la face cachée", c="conflit"),
            dict(d="12 avril 1961", t="Gagarine, premier homme dans l'espace (108 min)", c="conflit"),
            dict(d="16 juin 1963", t="Terechkova, première femme", c="conflit"),
            dict(d="18 mars 1965", t="Leonov, première sortie dans l'espace", c="conflit")], x=60, w=1160, y=120, h=470),
        "but": dict(type="note", titre="Pourquoi ?", t="Chaque « première » doit prouver la supériorité du socialisme : l'espace est une vitrine de propagande.", y=230),
        "pg1": dict(type="note", titre="Piège", t="Avant 1969, l'URSS a gagné presque toutes les « premières ».", y=240),
    }),

    # ================================================================ I.3 la riposte américaine
    dict(id="apollo", chap="La riposte américaine : Apollo", fond="orbite", humeur="tension",
         retenir="NASA : loi de juillet 1958, active le 1er octobre 1958. 25 mai 1961 : Kennedy fixe l'objectif de la Lune. Apollo 11 : 20 juillet 1969 (21 en heure européenne) ; 6 missions, 12 astronautes américains (1969-1972).",
         beats=[
        "{esp2}Et les Américains ? Ils ripostent. {esp2.1}Le trente et un janvier mille neuf cent cinquante-huit, ils placent leur premier satellite en orbite, "
        "Explorer un, depuis Cap Canaveral.",
        "{-esp2}{us}Surtout, ils s'organisent. {us.1}En juillet mille neuf cent cinquante-huit, une loi crée la NASA. Elle est active dès le premier octobre. "
        "{us.2}Le vingt-cinq mai mille neuf cent soixante et un, six semaines après Gagarine, le président Kennedy parle devant le Congrès. "
        "Son objectif : poser un homme sur la Lune avant la fin de la décennie.",
        "Le programme Apollo mobilise des centaines de milliers de personnes. Et au milieu des années soixante, une part considérable du budget fédéral.",
        "{us.3}Et le vingt juillet mille neuf cent soixante-neuf, c'est la mission Apollo onze. "
        "{-us}{tab_ald}Neil Armstrong et Buzz Aldrin marchent sur la Lune. "
        "En Europe, il est déjà le vingt et un juillet.",
        ("P", 1.0),
        "{-tab_ald}{lun}{lun.1}Entre mille neuf cent soixante-neuf et mille neuf cent soixante-douze, six missions se posent sur la Lune. "
        "{lun.2}Douze astronautes y marchent. Tous américains.",
        "{-lun}{f2}Les États-Unis ont perdu les premières manches. Mais ils gagnent la course {!symbolique}symbolique. Celle que le monde entier retient.",
    ], vis={
        "esp2": dict(type="scene", anim="espace", pas=[1], fs=20, cam={"0": ESPACE_V, "1": [150, 60, 300, 147]}),
        "us": dict(type="chrono", titre="La riposte américaine", items=[
            dict(d="Juillet 1958", t="Une loi crée la NASA (active le 1er octobre)", c="mer"),
            dict(d="25 mai 1961", t="Kennedy devant le Congrès : la Lune avant la fin de la décennie", c="mer"),
            dict(d="20 juil. 1969", t="Apollo 11", c="mer")], x=170, w=940, y=140, h=430),
        "tab_ald": dict(type="tableau", img="t1-aldrin", de=[1.0, .5, .3], a=[1.2, .5, .38],
                        legende="Buzz Aldrin sur la Lune, mission Apollo 11, juillet 1969, photographie de Neil Armstrong, NASA (domaine public)"),
        "lun": dict(type="chiffres", items=[dict(v=6, t="missions posées sur la Lune (1969-1972)"),
                                            dict(v=12, t="astronautes sur la Lune, tous américains")], y=190),
        "f2": dict(type="note", titre="Bilan", t="L'URSS mène les premières ; les États-Unis gagnent la course symbolique à la Lune.", y=230),
    }),

    # ================================================================ I.4 un espace militarisé
    dict(id="militaire", chap="Un espace militarisé, mais pas armé de bombes", fond="crise", humeur="tension",
         retenir="Satellites espions (Corona, 1960), d'écoute et d'alerte : ils stabilisent la dissuasion. Le traité de 1967 n'interdit que les armes nucléaires et de destruction massive. Apollo-Soyouz (17 juillet 1975), puis la « guerre des étoiles » (1983).",
         beats=[
        "{yeux}Pendant ce temps, le ciel se remplit d'yeux et d'oreilles. "
        "{yeux.1}Des satellites espions : le programme américain Corona rapporte ses premières images en août mille neuf cent soixante. "
        "{yeux.2}Des satellites d'écoute. "
        "{yeux.3}Et des satellites d'alerte avancée, qui repèrent le départ des missiles.",
        "{-yeux}{para}Et voilà le paradoxe. Ces satellites militaires rendent la dissuasion plus stable. "
        "Pourquoi ? Parce que chacun peut vérifier les arsenaux de l'adversaire. Moins de doutes, moins de mauvaises surprises.",
        "{-para}{p67}Attention à un piège. Le traité de l'espace, en mille neuf cent soixante-sept, n'interdit pas toutes les armes. "
        "Il interdit les armes nucléaires en orbite, et les armes de destruction massive. Mais pas les armes classiques.",
        "{-p67}{as}Mais la rivalité n'empêche pas les gestes de paix. Le dix-sept juillet mille neuf cent soixante-quinze, "
        "un vaisseau Apollo et un vaisseau Soyouz s'amarrent en orbite. Les deux équipages se serrent la main. "
        "C'est le symbole de la détente. Et l'annonce d'une coopération à venir : la Station spatiale internationale.",
        "{-as}{ids}La détente ne dure pas. En mille neuf cent quatre-vingt-trois, le président Reagan lance l'Initiative de défense stratégique. "
        "On la surnomme la « guerre des étoiles ». La course repart.",
    ], vis={
        "yeux": dict(type="cartes", items=[
            dict(ic="satellite", t="Satellites espions", q="programme Corona : premières images en août 1960"),
            dict(ic="radar", t="Satellites d'écoute", q="capter les communications de l'adversaire"),
            dict(ic="globe", t="Alerte avancée", q="repérer le départ des missiles")]),
        "para": dict(type="note", titre="Le paradoxe", t="Les satellites militaires stabilisent la dissuasion : chacun peut vérifier les arsenaux de l'autre.", y=230),
        "p67": dict(type="note", titre="Piège", t="Le traité de 1967 n'interdit pas toute arme : seulement les armes nucléaires et de destruction massive.", y=230),
        "as": dict(type="mot", t="17 juillet 1975", g="Apollo-Soyouz : une poignée de main en orbite, symbole de la détente", taille=120, y=220),
        "ids": dict(type="mot", t="1983", g="Reagan : l'Initiative de défense stratégique, la « guerre des étoiles »", taille=150, y=210),
    }),

    # ================================================================ I.5 la France et l'Europe
    dict(id="france", chap="La France et l'Europe : l'indépendance", fond="archive", humeur="lumiere",
         retenir="France : CNES (19 décembre 1961) ; Astérix (26 novembre 1965, fusée Diamant, Hammaguir) : 3e puissance spatiale. Europe : ESA (1975), Ariane 1 (24 décembre 1979, Kourou), Galileo (décembre 2016), Ariane 6 (9 juillet 2024).",
         beats=[
        "{q2}Et la France, dans tout ça ? Pour le général de Gaulle, l'accès autonome à l'espace est une question de {!souveraineté}souveraineté. "
        "Ne dépendre de personne.",
        "{-q2}{espf}{espf.1}Le dix-neuf décembre mille neuf cent soixante et un, il crée le CNES, le Centre national d'études spatiales. "
        "Et le vingt-six novembre mille neuf cent soixante-cinq, la fusée Diamant décolle d'Hammaguir, dans le Sahara algérien. "
        "Elle place en orbite le premier satellite français. Son nom ? Astérix !",
        "La France devient la troisième puissance spatiale à placer un satellite en orbite avec son propre lanceur.",
        "{espf.2}L'Europe suit. En mille neuf cent soixante-quinze, elle crée son Agence spatiale européenne. "
        "Et le vingt-quatre décembre mille neuf cent soixante-dix-neuf, la première fusée Ariane décolle de Kourou, en Guyane.",
        "{-espf}{eu}Récapitulons. {eu.1}Le CNES, en soixante et un. {eu.2}Astérix, en soixante-cinq. "
        "{eu.3}L'Agence spatiale européenne, en soixante-quinze. {eu.4}Ariane, en soixante-dix-neuf. "
        "{eu.5}Puis, en décembre deux mille seize, Galileo, le système européen de navigation, offre ses premiers services. "
        "Son but ? Ne pas dépendre du GPS américain. "
        "{eu.6}Et le neuf juillet deux mille vingt-quatre, Ariane six fait son premier vol.",
        "{-eu}{f3}Tu vois le fil rouge ? Pour la France et l'Europe, l'espace est un instrument d'{!indépendance}indépendance.",
    ], vis={
        "q2": dict(type="mot", t="La France ?", g="« L'accès autonome à l'espace est une question de souveraineté »", taille=110, y=230),
        "espf": dict(type="scene", anim="espace", pas=[2, 5], fs=20,
                     cam={"0": ESPACE_V, "1": [340, 55, 260, 127], "2": [260, 120, 260, 127]}),
        "eu": dict(type="chrono", titre="La France et l'Europe dans l'espace", items=[
            dict(d="19 déc. 1961", t="Création du CNES", c="droit"),
            dict(d="26 nov. 1965", t="Astérix : la France, 3e puissance spatiale", c="droit"),
            dict(d="1975", t="L'Agence spatiale européenne (ESA)", c="droit"),
            dict(d="24 déc. 1979", t="Ariane 1 décolle de Kourou", c="droit"),
            dict(d="Déc. 2016", t="Galileo : premiers services", c="droit"),
            dict(d="9 juil. 2024", t="Premier vol d'Ariane 6", c="droit")], x=60, w=1160, y=120, h=470),
        "f3": dict(type="note", titre="À retenir", t="Pour la France et l'Europe, l'espace est un instrument d'indépendance : ses propres lanceurs, sa propre navigation.", y=230),
    }),

    # ================================================================ II.1 un club élargi
    dict(id="club", chap="Un club élargi", fond="orbite", humeur="calme",
         retenir="Une dizaine d'États lancent leurs satellites : URSS (1957), États-Unis (1958), France (1965), Japon et Chine (1970), Royaume-Uni (1971), Inde (1980), Israël (1988), Iran (2009), Corée du Nord (2012), Corée du Sud (2013, puis 2022).",
         beats=[
        "{m2}Deuxième volet. Peu à peu, l'espace cesse d'être un duel. Et depuis les années deux mille, il devient {!multipolaire}multipolaire. Et privatisé.",
        "{-m2}{espc}Regarde le club s'agrandir, dès les années soixante-dix. {espc.1}En mille neuf cent soixante-dix, le Japon et la Chine lancent leur premier satellite. "
        "Puis le Royaume-Uni, en mille neuf cent soixante et onze, depuis l'Australie. "
        "{espc.2}L'Inde suit en mille neuf cent quatre-vingts. Israël, en mille neuf cent quatre-vingt-huit.",
        "{espc.3}Et plus près de nous : l'Iran, en deux mille neuf. La Corée du Nord, en deux mille douze. "
        "Ce n'est pas un hasard : ce sont les mêmes technologies que celles des missiles balistiques.",
        "La Corée du Sud y parvient en deux mille treize, avec un premier étage russe. Puis en deux mille vingt-deux, avec un lanceur entièrement national.",
        "{-espc}{dz}{dz.1}Au total, une dizaine d'États savent mettre un satellite en orbite avec leur propre lanceur. "
        "Les autres achètent des satellites, et des lancements.",
        "{-dz}{hope}Et même un pays sans tradition spatiale peut s'affirmer. Le neuf février deux mille vingt et un, "
        "la sonde Hope, des Émirats arabes unis, atteint l'orbite de Mars. Comment ? En achetant des compétences, et des partenariats.",
    ], vis={
        "m2": dict(type="cols", g="Hier", gq="un duel : États-Unis contre URSS", d="Aujourd'hui", dq="un espace multipolaire et privatisé", vs="→"),
        "espc": dict(type="scene", anim="espace", pas=[4, 6, 7], fs=20,
                     cam={"0": ESPACE_V, "1": [360, 70, 620, 304], "2": [480, 60, 300, 147], "3": [460, 40, 440, 216]}),
        "dz": dict(type="chiffres", items=[dict(v="≈ 10", t="États lancent leurs satellites avec leur propre lanceur")], y=190),
        "hope": dict(type="note", titre="9 février 2021", t="La sonde Hope des Émirats arabes unis atteint l'orbite de Mars : s'affirmer en achetant compétences et partenariats.", y=230),
    }),

    # ================================================================ II.2 la Chine et l'Inde
    dict(id="chineinde", chap="La Chine et l'Inde", fond="orbite", humeur="lumiere",
         retenir="Chine : 1er satellite (1970), 1er taïkonaute (2003), station Tiangong (2021-2022), Chang'e 6 (25 juin 2024, face cachée). Inde : ISRO (1969), Mangalyaan (2014), Chandrayaan-3 (23 août 2023, près du pôle Sud lunaire).",
         beats=[
        "{cn}La Chine d'abord. {cn.1}Son premier satellite, en mille neuf cent soixante-dix. "
        "{cn.2}Son premier taïkonaute, c'est-à-dire un astronaute chinois, en deux mille trois. "
        "{cn.3}Sa propre station, Tiangong, construite en deux mille vingt et un et deux mille vingt-deux. "
        "{cn.4}Et des premières mondiales sur la Lune. Le vingt-cinq juin deux mille vingt-quatre, la sonde Chang'e six rapporte sur Terre "
        "les tout premiers échantillons de la face cachée. Près de deux kilos.",
        "{-cn}{cn2}Aujourd'hui, la Chine est la deuxième puissance spatiale. La seule capable de rivaliser avec les États-Unis dans tous les domaines du spatial. "
        "Tu la retrouveras dans l'objet de travail conclusif.",
        "{-cn2}{mi}Et l'Inde ? Elle a choisi une voie originale : une puissance spatiale « frugale ». "
        "{-mi}{ind}{ind.1}Son agence, l'ISRO, naît en mille neuf cent soixante-neuf. D'abord, l'espace sert le développement : télécommunications, météo, cartographie. "
        "{ind.2}Puis elle explore, avec de petits budgets. En deux mille quatorze, sa sonde Mangalyaan atteint l'orbite de Mars dès la première tentative.",
        "{ind.3}Et le vingt-trois août deux mille vingt-trois, l'atterrisseur de Chandrayaan trois se pose près du pôle Sud de la Lune. "
        "L'Inde devient le quatrième pays à réussir un atterrissage lunaire. Et le premier dans cette région. "
        "{ind.4}Prochaine étape : les vols habités, avec le programme Gaganyaan.",
    ], vis={
        "cn": dict(type="chrono", titre="La Chine, deuxième puissance spatiale", items=[
            dict(d="1970", t="Premier satellite chinois", c="conflit"),
            dict(d="2003", t="Premier taïkonaute", c="conflit"),
            dict(d="2021-2022", t="La station Tiangong", c="conflit"),
            dict(d="25 juin 2024", t="Chang'e 6 : premiers échantillons de la face cachée (près de 2 kg)", c="conflit")], x=120, w=1040, y=130, h=450),
        "cn2": dict(type="def", terme="La Chine", t="Deuxième puissance spatiale, la seule à rivaliser avec les États-Unis sur tous les segments du spatial.", y=220),
        "mi": dict(type="mot", t="L'Inde", g="une puissance spatiale « frugale »", taille=130, y=230),
        "ind": dict(type="liste", titre="L'Inde, une puissance spatiale « frugale »", items=[
            "1969 : l'ISRO, l'espace au service du développement",
            "2014 : Mangalyaan en orbite de Mars, dès la première tentative",
            "23 août 2023 : Chandrayaan-3 se pose près du pôle Sud de la Lune",
            "Demain : les vols habités (programme Gaganyaan)"], x=150, y=130, w=980),
    }),

    # ================================================================ II.3 les entreprises
    dict(id="newspace", chap="SpaceX et le New Space", fond="orbite", humeur="tension",
         retenir="SpaceX (fondée en 2002) : réutilisation des lanceurs, plus de la moitié des lancements orbitaux mondiaux en 2024, Starlink (plus de 10 000 satellites en 2026). Blue Origin : New Glenn (16 janvier 2025). Starlink en Ukraine depuis février 2022.",
         beats=[
        "{sx}Et puis, il y a les entreprises. {sx.1}SpaceX est fondée en deux mille deux par Elon Musk. "
        "Son idée : réutiliser les lanceurs. Résultat : les coûts chutent.",
        "{sx.2}En deux mille vingt-quatre, SpaceX réalise plus de la moitié des lancements orbitaux du monde. Elle transporte les astronautes de la NASA. "
        "{sx.3}Et elle déploie sa constellation Starlink : plus de dix mille satellites en deux mille vingt-six.",
        "{-sx}{espn}Sur la carte apparaissent de nouvelles bases. {espn.1}Starbase, pour SpaceX. {espn.2}Mahia, en Nouvelle-Zélande, pour l'entreprise Rocket Lab. "
        "{espn.3}Et du côté chinois, Wenchang, une base de lancement au bord de la mer.",
        "{-espn}{bo}Les concurrents arrivent. Blue Origin, l'entreprise de Jeff Bezos, lance sa fusée lourde New Glenn pour la première fois "
        "le seize janvier deux mille vingt-cinq.",
        "{-bo}{ukr}Mais voici l'exemple qui change tout. Depuis la fin de février deux mille vingt-deux, l'armée et les autorités ukrainiennes "
        "communiquent grâce à des milliers de terminaux Starlink, malgré l'invasion russe.",
        "Réfléchis une seconde. Un État en guerre dépend d'une {!entreprise privée}entreprise privée étrangère. "
        "Et le dirigeant de cette entreprise peut décider seul de l'accès au service.",
        "{-ukr}{pg2}Un conseil pour ta copie : ne parle jamais des « entreprises privées » sans exemple. Cite SpaceX, Starlink, Blue Origin. Et date.",
    ], vis={
        "sx": dict(type="chiffres", items=[
            dict(v="2002", t="SpaceX est fondée : des lanceurs réutilisables", taille=84),
            dict(v=50, avant="+ de ", apres=" %", t="des lancements orbitaux mondiaux (2024)", taille=84),
            dict(v=10000, avant="+ de ", t="satellites Starlink en orbite (2026)", taille=84)], x=50, w=1180, y=200),
        "espn": dict(type="scene", anim="espace", etapes=ESP_NEW, fs=20,
                     cam={"0": ESPACE_V, "1": [140, 70, 300, 147], "2": [680, 250, 300, 147], "3": [640, 100, 300, 147]}),
        "bo": dict(type="note", titre="16 janvier 2025", t="Blue Origin (Jeff Bezos) lance pour la première fois sa fusée lourde New Glenn.", y=230),
        "ukr": dict(type="def", terme="Starlink en Ukraine", t="Depuis février 2022, un État en guerre dépend d'une entreprise privée étrangère, dont le dirigeant peut décider seul de l'accès au service.", y=200),
        "pg2": dict(type="note", titre="Piège", t="« Les entreprises privées » sans exemple ne vaut rien : cite SpaceX, Starlink, Blue Origin, et date.", y=230),
    }),

    # ================================================================ II.4 Artemis
    dict(id="artemis", chap="Le retour vers la Lune", fond="orbite", humeur="lumiere",
         retenir="Artemis : retour vers le pôle Sud de la Lune (glace d'eau), avec des partenaires et des entreprises (atterrisseur SpaceX, 2021). Artemis II : 1er-10 avril 2026, record de distance le 6 avril (≈ 406 000 km), sans se poser. La Chine vise un atterrissage habité avant 2030.",
         beats=[
        "{art}Et la Lune ? Elle redevient un objectif. {art.1}Le programme américain Artemis veut y ramener des astronautes. Près du pôle Sud. "
        "{art.2}Pourquoi là ? Parce qu'on y trouve de la glace d'eau. "
        "{art.3}Et Artemis s'appuie sur des partenaires internationaux, et sur des entreprises : en deux mille vingt et un, SpaceX est choisie pour construire l'atterrisseur.",
        "{-art}{espa}{espa.1}Le premier avril deux mille vingt-six, Artemis deux décolle de Floride. À bord, quatre astronautes : "
        "trois Américains, et un Canadien, Jeremy Hansen.",
        "{-espa}{a2}{a2.1}Le six avril, l'équipage bat un record : la plus grande distance jamais parcourue par des humains depuis la Terre. "
        "Environ quatre cent six mille kilomètres. "
        "{a2.2}Et le dix avril, il amerrit dans le Pacifique. Sans s'être posé sur la Lune : c'était un vol autour d'elle.",
        "{-a2}{crs}{crs.g}En face, {crs.d}la Chine vise un atterrissage habité avant deux mille trente. Une nouvelle course est engagée.",
    ], vis={
        "art": dict(type="cartes", items=[
            dict(ic="fusee", t="Artemis", q="ramener des astronautes près du pôle Sud de la Lune"),
            dict(ic="vague", t="La glace d'eau", q="une ressource présente au pôle Sud"),
            dict(ic="satellite", t="Des partenaires", q="États alliés et entreprises : SpaceX choisie en 2021 pour l'atterrisseur")]),
        "espa": dict(type="scene", anim="espace", pas=[9], fs=20, cam={"0": ESPACE_V, "1": [180, 20, 330, 162]}),
        "a2": dict(type="chiffres", titre="Artemis II, avril 2026", items=[
            dict(v=406000, avant="≈ ", apres=" km", t="record de distance pour des humains (6 avril)", taille=84),
            dict(v="10 avril", t="amerrissage dans le Pacifique, sans s'être posé", taille=72)], y=180),
        "crs": dict(type="cols", g="États-Unis", gq="Artemis : retour au pôle Sud de la Lune", d="Chine",
                    dq="un atterrissage habité visé avant 2030", vs="2030"),
    }),

    # ================================================================ III.1 des armées dépendantes
    dict(id="dependance", chap="Des armées dépendantes de l'espace", fond="crise", humeur="tension", beats=[
        "{q3}Troisième volet. Et si l'espace devenait un champ de bataille ?",
        "Commence par un constat. Les armées modernes ne peuvent plus combattre sans satellites. "
        "{-q3}{dep}{dep.1}Pour le renseignement. {dep.2}Pour les communications. {dep.3}Pour la navigation, et le guidage des munitions. "
        "{dep.4}Et pour l'alerte antimissile.",
        "Alors celui qui aveugle les satellites de l'adversaire prend l'avantage.",
        "{-dep}{golfe}D'ailleurs, la guerre du Golfe, en mille neuf cent quatre-vingt-onze, est souvent appelée la « première guerre spatiale ». "
        "La coalition guide ses troupes dans le désert grâce au GPS américain, pourtant encore incomplet. "
        "Et elle repère les tirs de missiles irakiens grâce à ses satellites d'alerte.",
    ], vis={
        "q3": dict(type="question", t="L'espace, nouveau champ de bataille ?"),
        "dep": dict(type="liste", titre="Ce que les armées attendent des satellites", items=[
            "Le renseignement", "Les communications", "La navigation et le guidage des munitions", "L'alerte antimissile"],
            x=230, y=160, w=820),
        "golfe": dict(type="mot", t="1991", g="La guerre du Golfe, « première guerre spatiale » : GPS et satellites d'alerte", taille=150, y=210),
    }),

    # ================================================================ III.2 les tirs antisatellites
    dict(id="asat", chap="Tirs antisatellites et forces spatiales", fond="crise", humeur="tension",
         retenir="Tirs antisatellites destructeurs : Chine (11 janvier 2007, plus de 3 000 débris), États-Unis (février 2008), Inde (27 mars 2019), Russie (15 novembre 2021). Forces spatiales : Commandement de l'espace (3 septembre 2019), Space Force (20 décembre 2019).",
         beats=[
        "{at}{at.1}Pire : plusieurs puissances ont prouvé qu'elles pouvaient détruire un satellite depuis le sol. C'est une arme antisatellite, une ASAT.",
        "{at.2}Le onze janvier deux mille sept, la Chine pulvérise l'un de ses vieux satellites météo, Fengyun un C. "
        "Résultat : plus de trois mille débris suivis. "
        "{at.3}En février deux mille huit, les États-Unis abattent à leur tour un de leurs satellites. "
        "{at.4}Le vingt-sept mars deux mille dix-neuf, c'est l'Inde, avec la mission Shakti.",
        "{at.5}Et le quinze novembre deux mille vingt et un, la Russie détruit Kosmos quatorze cent huit. "
        "Le nuage de débris oblige l'équipage de la Station spatiale internationale à se mettre à l'abri.",
        "{at.6}Tu vois le problème ? Ces tirs démontrent une capacité. Mais leurs débris menacent tout le monde, y compris le tireur. "
        "Jusqu'au risque d'une réaction en chaîne de collisions : le syndrome de Kessler.",
        "{at.7}Alors les États s'organisent. L'espace est désormais reconnu comme un « milieu » de conflit, comme la terre, la mer, l'air et le cyberespace. "
        "En France, le Commandement de l'espace est créé le trois septembre deux mille dix-neuf. "
        "Aux États-Unis, la Space Force naît le vingt décembre deux mille dix-neuf. "
        "Et en septembre deux mille vingt, l'armée de l'Air française devient l'armée de l'Air et de l'Espace.",
        "{-at}{lou}Un dernier exemple, digne d'un roman d'espionnage. En septembre deux mille dix-huit, la ministre des Armées révèle qu'en deux mille dix-sept, "
        "un satellite russe, Louch-Olymp, s'est approché de très près d'un satellite militaire franco-italien, Athena-Fidus. "
        "Elle parle d'un « acte d'espionnage ».",
        "{-lou}{gdc}D'où les nouvelles stratégies de défense spatiale. {gdc.1}Surveiller l'espace. {gdc.2}Des satellites capables de manœuvrer. "
        "{gdc.3}Et même des « gardes du corps » en orbite.",
    ], vis={
        "at": dict(type="scene", anim="t1asat", fs=20, cam={"0": [20, 30, 600, 294]}),
        "lou": dict(type="def", terme="2017 : Louch-Olymp", t="Un satellite russe s'approche de très près du satellite militaire franco-italien Athena-Fidus : « un acte d'espionnage » (révélé en septembre 2018).", y=200),
        "gdc": dict(type="liste", titre="Défendre l'espace", items=[
            "Surveiller l'espace", "Des satellites manœuvrants", "Des « gardes du corps » en orbite"], x=230, y=170, w=820),
    }),

    # ================================================================ IV.1 la puissance navale
    dict(id="mahan", chap="La mer, clé de la puissance", fond="ocean", humeur="calme",
         retenir="Mahan (1890) : la maîtrise des mers fait les grandes puissances. Une marine de haute mer protège le commerce, dissuade, intervient partout. États-Unis : 11 porte-avions nucléaires (2025), 6e flotte (Naples), 5e (Bahreïn), 7e (Japon).",
         beats=[
        "{m4}Quatrième volet : la mer. Et pour la comprendre, un retour en arrière, en mille huit cent quatre-vingt-dix.",
        "{-m4}{mah}Cette année-là, l'officier américain Alfred Mahan publie un livre qui va marquer tous les stratèges : "
        "l'influence de la puissance maritime sur l'histoire. Sa thèse ? La maîtrise des mers fait les grandes puissances.",
        "{-mah}{hm}Pour cela, il faut une marine de haute mer. On dit aussi « océanique », ou « de premier rang ». À quoi sert-elle ? "
        "{hm.1}À protéger son commerce. {hm.2}À dissuader. {hm.3}Et à intervenir partout.",
        "{-hm}{mar}Prends les États-Unis, première puissance navale depuis mille neuf cent quarante-cinq. "
        "{mar.1}Ils ont de grandes bases sur leurs deux façades : Norfolk, sur l'Atlantique, et San Diego, sur le Pacifique. "
        "Et des flottes numérotées sur tous les océans. {mar.2}La sixième flotte, à Naples, en Méditerranée. "
        "{mar.3}La cinquième, à Bahreïn, dans le golfe. {mar.4}Et la septième, au Japon.",
        "{-mar}{pa}{pa.1}En deux mille vingt-cinq, ils alignent onze porte-avions à propulsion nucléaire. Onze !",
    ], vis={
        "m4": dict(type="mot", t="La mer", g="« Affirmer sa puissance à partir des mers et des océans »", taille=130, y=230),
        "mah": dict(type="def", terme="Alfred Mahan, 1890", t="The Influence of Sea Power upon History : la maîtrise des mers fait les grandes puissances.", y=220),
        "hm": dict(type="liste", titre="Une marine de haute mer, pour…", items=[
            "Protéger son commerce", "Dissuader", "Intervenir partout"], x=280, y=180, w=720),
        "mar": dict(type="scene", anim="marine", etapes=MAR_US, fs=20,
                    cam={"0": MARINE_V, "1": [100, 60, 280, 137], "2": [400, 40, 260, 127], "3": [480, 80, 260, 127], "4": [700, 40, 260, 127]}),
        "pa": dict(type="chiffres", items=[dict(v=11, t="porte-avions à propulsion nucléaire américains (2025)")], y=190),
    }),

    # ================================================================ IV.2 la dissuasion océanique
    dict(id="snle", chap="La dissuasion océanique : les SNLE", fond="ocean", humeur="mystere",
         retenir="SNLE : presque indétectable, il garantit la seconde frappe et rend la dissuasion crédible. France : 4 SNLE (classe Le Triomphant) à l'Île Longue, missile M51, permanence à la mer depuis janvier 1972.",
         beats=[
        "{q4}Maintenant, imagine une arme que personne ne peut trouver.",
        "{-q4}{dsn}C'est le SNLE : le sous-marin nucléaire lanceur d'engins. Il porte les missiles nucléaires. Et caché dans les profondeurs, il est presque indétectable.",
        "{-dsn}{sf}Et c'est là toute l'astuce. {sf.1}Imagine qu'un État soit frappé par surprise. Son territoire est détruit. "
        "{sf.2}Mais son SNLE, lui, est intact, quelque part sous l'océan. {sf.3}Il peut riposter. "
        "C'est la {!seconde frappe}seconde frappe. Et c'est ce qui rend la dissuasion crédible : personne n'a intérêt à attaquer le premier.",
        "{-sf}{msn}{msn.1}Qui possède des SNLE ? Les cinq puissances nucléaires reconnues par le traité de non-prolifération : "
        "les États-Unis, la Russie, la Chine, le Royaume-Uni, et la France. Plus l'Inde.",
        "{msn.2}Et la France ? Elle entretient quatre SNLE, de la classe Le Triomphant. Ils sont basés à l'Île Longue, dans la rade de Brest, "
        "et armés du missile M cinquante et un.",
        "{-msn}{perm}Depuis la première patrouille du Redoutable, en janvier mille neuf cent soixante-douze, au moins un SNLE français est toujours en mer. "
        "Jour et nuit. Depuis plus de cinquante ans. C'est la « permanence à la mer ».",
        "{-perm}{snav}Et attention au piège. Ne confonds pas SNLE et SNA. "
        "{snav.g}Le SNLE porte les missiles de la dissuasion : c'est la seconde frappe. "
        "{snav.d}Le SNA, le sous-marin nucléaire d'attaque, chasse les navires… et protège les SNLE.",
    ], vis={
        "q4": dict(type="question", t="Une arme que personne ne peut trouver ?"),
        "dsn": dict(type="def", terme="SNLE", t="Sous-marin nucléaire lanceur d'engins : il porte les missiles de la dissuasion et reste presque indétectable.", y=220),
        "sf": dict(type="liste", titre="La seconde frappe", items=[
            "Un État est frappé par surprise : son territoire est détruit",
            "Son SNLE, caché sous l'océan, est intact",
            "Il riposte : la dissuasion est crédible"], marques=["1", "2", "3"], x=150, y=160, w=980),
        "msn": dict(type="scene", anim="marine", etapes=MAR_SNLE, fs=20,
                    cam={"0": MARINE_V, "1": [120, 0, 780, 382], "2": [420, 30, 140, 69]}),
        "perm": dict(type="mot", t="Janvier 1972", g="Le Redoutable part en patrouille : la « permanence à la mer » commence", taille=120, y=220),
        "snav": dict(type="cols", g="SNLE", gq="porte les missiles de la dissuasion : la seconde frappe", d="SNA",
                     dq="sous-marin d'attaque : chasse les navires, protège les SNLE", vs="≠"),
    }),

    # ================================================================ IV.3 la projection de puissance
    dict(id="projection", chap="La projection de puissance", fond="ocean", humeur="tension",
         retenir="Projection : agir loin de son territoire. Le porte-avions, base aérienne mobile, au cœur d'un groupe aéronaval. Charles-de-Gaulle (depuis 2001) : Chammal (2015), Clemenceau 25 (nov. 2024 - avr. 2025). Fujian, 3e porte-avions chinois (5 novembre 2025, Sanya).",
         beats=[
        "{dpj}Deuxième outil de la puissance en mer : la {!projection}projection. C'est la capacité d'agir militairement loin de son territoire.",
        "{-dpj}{pav}Et l'outil roi, c'est le porte-avions. {pav.1}Une base aérienne mobile. Elle permet de frapper loin… sans demander l'autorisation d'un pays voisin. "
        "{pav.2}Autour de lui, des frégates et un sous-marin : c'est le groupe aéronaval. "
        "{pav.3}Et il sert aussi la diplomatie. Montrer le pavillon. Rassurer un allié. Dissuader un adversaire.",
        "{-pav}{cdg}Prends le porte-avions français Charles-de-Gaulle, en service depuis deux mille un. {cdg.1}Son port d'attache : Toulon. "
        "{cdg.2}En deux mille quinze, il frappe Daech en Irak et en Syrie : c'est l'opération Chammal. "
        "{cdg.3}Et de novembre deux mille vingt-quatre à avril deux mille vingt-cinq, il mène la mission Clemenceau vingt-cinq, "
        "dans l'océan Indien et le Pacifique.",
        "{cdg.4}Et la Chine ? Le cinq novembre deux mille vingt-cinq, elle met en service son troisième porte-avions, le Fujian, "
        "à Sanya, sur l'île de Hainan.",
        "{-cdg}{pa3}Fais le compte. {pa3.1}Onze porte-avions américains. {pa3.2}Trois chinois. {pa3.3}Un français. "
        "Les États-Unis dominent toujours. Mais la Chine avance vite.",
    ], vis={
        "dpj": dict(type="def", terme="Projection de puissance", t="Capacité d'agir militairement loin de son territoire : porte-avions, bases, flottes.", y=220),
        "pav": dict(type="cartes", items=[
            dict(ic="fusee", t="Frapper loin", q="une base aérienne mobile, sans autorisation d'un voisin"),
            dict(ic="radar", t="Le groupe aéronaval", q="le porte-avions entouré de frégates et d'un sous-marin"),
            dict(ic="drapeau", t="La diplomatie", q="montrer le pavillon, rassurer un allié, dissuader")]),
        "cdg": dict(type="scene", anim="marine", etapes=MAR_PROJ, fs=20,
                    cam={"0": MARINE_V, "1": [420, 40, 200, 98], "2": [440, 40, 200, 98], "3": [430, 40, 480, 235], "4": [660, 110, 220, 108]}),
        "pa3": dict(type="chiffres", titre="Les porte-avions", items=[
            dict(v=11, t="États-Unis (2025)"), dict(v=3, t="Chine, avec le Fujian (2025)"), dict(v=1, t="France : le Charles-de-Gaulle")], y=180),
    }),

    # ================================================================ IV.4 bases, détroits, nouvelles rivalités
    dict(id="bases", chap="Bases, détroits et nouvelles rivalités", fond="crise", humeur="tension",
         retenir="Bases près des détroits (Ormuz, Bab el-Mandeb, Malacca) ; Djibouti : bases française, américaine, japonaise et chinoise (1er août 2017). Chine : plus de 370 navires (Pentagone, 2024). Mer Rouge : Houthis (Galaxy Leader, 19 novembre 2023), Prosperity Guardian (décembre 2023), Aspides (février 2024).",
         beats=[
        "{bd0}Mais un porte-avions ne vit pas seul. Pour projeter sa puissance, il faut des escales, pour se ravitailler et réparer. "
        "Les puissances maritimes entretiennent donc un réseau de bases. Souvent près des détroits stratégiques. "
        "{-bd0}{bd}{bd.1}Ormuz. {bd.2}Bab el-Mandeb. {bd.3}Malacca.",
        "{bd.4}Et l'exemple le plus parlant, c'est Djibouti, au débouché de la mer Rouge. "
        "On y trouve la principale base française à l'étranger, une base américaine, une base japonaise… "
        "Et depuis le premier août deux mille dix-sept, la première base militaire chinoise à l'étranger.",
        "{-bd}{chn}{chn.1}Car la puissance navale se rééquilibre vers l'Asie. La Chine possède la plus grande marine du monde en nombre de bâtiments : "
        "plus de trois cent soixante-dix navires et sous-marins, selon le Pentagone, en deux mille vingt-quatre.",
        "{-chn}{asie}L'Inde, le Japon, la Corée du Sud, la Turquie modernisent aussi leurs flottes. Et les incidents en mer se multiplient.",
        "{-asie}{rg}Exemple brûlant : la mer Rouge. {rg.1}Depuis novembre deux mille vingt-trois, les rebelles houthis du Yémen attaquent des navires marchands. "
        "{rg.2}Le dix-neuf novembre, ils s'emparent d'un transporteur de voitures, le Galaxy Leader. "
        "{rg.3}En décembre deux mille vingt-trois, les États-Unis lancent l'opération Prosperity Guardian. "
        "{rg.4}Et en février deux mille vingt-quatre, l'Union européenne lance l'opération Aspides.",
        "{-rg}{lec}La leçon ? Une simple {!milice}milice peut perturber l'une des routes maritimes les plus fréquentées du monde.",
    ], vis={
        "bd0": dict(type="note", titre="Des points d'appui", t="Projeter sa puissance suppose des escales pour se ravitailler et réparer : un réseau de bases, souvent près des détroits.", y=230),
        "bd": dict(type="scene", anim="marine", etapes=MAR_BASES, fs=20,
                   cam={"0": MARINE_V, "1": [520, 90, 220, 108], "2": [520, 130, 220, 108], "3": [640, 160, 220, 108], "4": [500, 140, 180, 88]}),
        "chn": dict(type="chiffres", items=[dict(v=370, avant="+ de ", t="navires et sous-marins chinois : la plus grande marine en nombre", src="Pentagone, 2024")], y=190),
        "asie": dict(type="note", titre="Vers l'Asie", t="Inde, Japon, Corée du Sud, Turquie modernisent leurs flottes ; les incidents en mer se multiplient.", y=230),
        "rg": dict(type="scene", anim="marine", etapes=MAR_ROUGE, fs=20,
                   cam={"0": MARINE_V, "1": [520, 120, 160, 78], "2": [520, 120, 160, 78], "3": [500, 115, 200, 98], "4": [490, 100, 220, 108]}),
        "lec": dict(type="note", titre="La leçon", t="Une milice peut perturber l'une des routes maritimes les plus fréquentées du monde.", y=230),
    }),

    # ================================================================ pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="crise", humeur="calme", beats=[
        "{pg}Avant le bac, les cinq pièges qui coûtent des points. "
        "{pg.1}Un : réduire la course à l'espace à une compétition scientifique. C'est d'abord un enjeu militaire et idéologique. "
        "{pg.2}Deux : oublier que l'URSS a gagné presque toutes les premières avant mille neuf cent soixante-neuf. "
        "{pg.3}Trois : confondre SNLE et SNA. "
        "{pg.4}Quatre : croire que le traité de mille neuf cent soixante-sept interdit toute arme dans l'espace. "
        "{pg.5}Et cinq : parler d'entreprises privées sans exemple daté.",
    ], vis={
        "pg": dict(type="liste", titre="Les cinq pièges", items=[
            "Réduire la course à l'espace à la science : elle est militaire et idéologique",
            "Oublier les « premières » soviétiques avant 1969",
            "Confondre SNLE (seconde frappe) et SNA (attaque)",
            "Croire que le traité de 1967 interdit toute arme",
            "Citer « les entreprises privées » sans exemple daté"], marques=["✗", "✗", "✗", "✗", "✗"], x=150, y=110, w=980),
    }),

    # ================================================================ la dissertation
    dict(id="dissert", chap="Au bac : la dissertation", fond="archive", humeur="calme", beats=[
        "{ep}Passons à l'épreuve. Quatre heures, deux exercices. {ep.g}Une dissertation, au choix entre deux sujets. "
        "{ep.d}Et une étude critique d'un ou deux documents, sur un autre thème.",
        "{-ep}{sujet}Entraînons-nous sur un sujet de dissertation, inventé pour l'occasion. "
        "« La conquête spatiale, une affaire d'États ? »",
        "{sujet.1}Première étape : analyser les termes. « Une affaire d'États » : les États sont-ils les seuls acteurs ? Les principaux ? "
        "Et le point d'interrogation t'invite à discuter. "
        "{sujet.2}Deuxième étape : une problématique, une vraie tension. "
        "{sujet.3}Troisième étape : un plan, avec des exemples datés.",
        "{-sujet}{pz}À toi ! Mets la vidéo sur pause. Prends cinq minutes, une feuille, et cherche une problématique et un plan.{pz.stop}",
        ("P", 2.0),
        "{-pz}{pb}Voici une proposition. La problématique : la conquête de l'espace, née de la rivalité entre États pendant la guerre froide, "
        "échappe-t-elle aujourd'hui aux États, avec l'arrivée des entreprises privées ?",
        "{-pb}{pl}Et le plan, en trois parties. "
        "{pl.1}Un : une conquête née de la rivalité entre États, de mille neuf cent cinquante-sept à mille neuf cent quatre-vingt-onze. "
        "Les missiles et les lanceurs, avec le R-7 et Spoutnik. Le prestige, avec Gagarine et Apollo onze. "
        "Et l'indépendance stratégique : Astérix en mille neuf cent soixante-cinq, Ariane en mille neuf cent soixante-dix-neuf.",
        "{pl.2}Deux : des acteurs plus nombreux, États émergents et entreprises. La Chine et Chang'e six, l'Inde et Chandrayaan trois. "
        "SpaceX, Starlink et ses plus de dix mille satellites, Blue Origin.",
        "{pl.3}Trois : mais les États restent maîtres du jeu. Ils financent, avec les contrats de la NASA. Ils régulent : le traité de mille neuf cent soixante-sept, "
        "la loi américaine de deux mille quinze sur les ressources spatiales. Ils militarisent : les tirs antisatellites, la Space Force. "
        "Et l'entreprise privée peut devenir un instrument de puissance : pense à Starlink en Ukraine.",
        "{-pl}{me}Le correcteur valorise la précision. Une date, un nom, un chiffre, dans chaque paragraphe. "
        "Et une phrase de liaison pour passer d'une idée à l'autre.",
        "{-me}{b25}Dernière chose. En juin deux mille vingt-cinq, un sujet proche est tombé au bac : "
        "« La puissance des États dans les espaces maritimes et extra-atmosphériques ». "
        "{b25.1}Et une première partie possible, c'est exactement ce chapitre. {b25.2}La course à l'espace, vitrine de la puissance. "
        "{b25.3}La mer, socle de la dissuasion et de la projection. {b25.4}Et l'espace, nouveau champ de bataille.",
    ], vis={
        "ep": dict(type="cols", g="Dissertation", gq="au choix entre deux sujets", d="Étude critique",
                   dq="d'un ou deux documents, sur un autre thème", vs="4 h"),
        "sujet": dict(type="exo", niveau="dissert", titre="La conquête spatiale, une affaire d'États ?",
                      src="Sujet inventé pour l'entraînement (thème 1, axe 1)",
                      questions=["Analyse les termes du sujet", "Trouve une problématique", "Construis un plan avec des exemples datés"]),
        "pz": dict(type="pause", t="Une problématique et un plan en trois parties pour ce sujet.",
                   sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "pb": dict(type="def", terme="Problématique", t="La conquête de l'espace, née de la rivalité entre États pendant la guerre froide, échappe-t-elle aujourd'hui aux États avec l'arrivée des entreprises privées ?", y=170),
        "pl": dict(type="liste", titre="Un plan possible", items=[
            "Une conquête née de la rivalité entre États (1957-1991) — R-7 et Spoutnik, Gagarine, Apollo 11, Astérix (1965), Ariane (1979)",
            "Des acteurs plus nombreux : États émergents et entreprises — Chang'e 6 (2024), Chandrayaan-3 (2023), SpaceX, Starlink, Blue Origin",
            "Mais les États restent maîtres du jeu — contrats de la NASA, traité de 1967, loi américaine de 2015, tirs ASAT, Space Force (2019), Starlink en Ukraine"],
            marques=["I", "II", "III"], x=130, y=120, w=1020),
        "me": dict(type="note", titre="Méthode", t="Dans chaque paragraphe : une date, un nom, un chiffre. Et une phrase de liaison.", y=230),
        "b25": dict(type="liste", titre="Bac, juin 2025 : « La puissance des États dans les espaces maritimes et extra-atmosphériques »", items=[
            "Une première partie possible : des espaces au service de la puissance militaire et du prestige",
            "A. La course à l'espace, vitrine de la puissance pendant la guerre froide",
            "B. La mer, socle de la dissuasion et de la projection",
            "C. L'espace, nouveau champ de bataille"], marques=["I", "A", "B", "C"], x=130, y=120, w=1020),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap pour le bac", fond="crise", humeur="lumiere", beats=[
        "{dat}Il est temps de tout ranger. Les dates, d'abord. {dat.1}Mille neuf cent cinquante-sept, Spoutnik. "
        "{dat.2}Mille neuf cent soixante et un, Gagarine. {dat.3}Mille neuf cent soixante-cinq, Astérix. "
        "{dat.4}Mille neuf cent soixante-neuf, Apollo onze. {dat.5}Mille neuf cent soixante-douze, la permanence à la mer. "
        "{dat.6}Mille neuf cent soixante-quinze, Apollo-Soyouz. {dat.7}Deux mille sept, le tir antisatellite chinois. "
        "{dat.8}Deux mille dix-sept, la base chinoise de Djibouti. {dat.9}Deux mille dix-neuf, les forces spatiales. "
        "{dat.10}Et deux mille vingt-six, Artemis deux.",
        ("P", 1.8),
        "{-dat}{cm}Et la carte du chapitre. {cm.1}La course à l'espace, enjeu de la guerre froide. {cm.2}De nouveaux acteurs. "
        "{cm.3}L'espace, champ de bataille. {cm.4}Et la mer, socle de la puissance.",
        ("P", 1.2),
        "{-cm}{qd2}Et garde en tête la question du thème : le droit international peut-il réguler ces rivalités de puissance ? "
        "C'est tout l'objet de l'axe deux.",
        "{-qd2}{fin}Les fiches, les QCM, la frise et les animations du chapitre t'attendent sur le site Ligne rouge : "
        "le lien est dans la description. Prochain dossier : la diplomatie et les coopérations. À très vite.",
        ("P", 2.5),
    ], vis={
        "dat": dict(type="chrono", titre="Les dates du chapitre", items=[
            dict(d="1957", t="Spoutnik 1", c="espace"), dict(d="1961", t="Gagarine", c="espace"),
            dict(d="1965", t="Astérix", c="droit"), dict(d="1969", t="Apollo 11", c="espace"),
            dict(d="1972", t="Permanence à la mer", c="mer"), dict(d="1975", t="Apollo-Soyouz", c="espace"),
            dict(d="2007", t="Tir antisatellite chinois", c="conflit"), dict(d="2017", t="Base chinoise à Djibouti", c="mer"),
            dict(d="2019", t="Space Force, Commandement de l'espace", c="conflit"), dict(d="2026", t="Artemis II", c="prive")],
            x=60, w=1160, y=120, h=470),
        "cm": dict(type="carte", centre="Conquêtes et puissance", branches=[
            dict(t="Course à l'espace", items=["Spoutnik (1957)", "Gagarine (1961)", "Apollo 11 (1969)"]),
            dict(t="Nouveaux acteurs", items=["Chine, Inde", "SpaceX, Starlink", "Artemis II (2026)"]),
            dict(t="Champ de bataille ?", items=["tirs ASAT (2007-2021)", "Space Force (2019)", "Golfe (1991)"]),
            dict(t="La mer", items=["SNLE : seconde frappe", "porte-avions", "Djibouti, mer Rouge"])]),
        "qd2": dict(type="question", t="Le droit international peut-il réguler les rivalités de puissance dans ces espaces ?"),
        "fin": dict(type="mot", t="Ligne rouge", g="Fiches, QCM, frise et animations : le lien est dans la description.", taille=110, y=250),
    }),
]

QUIZ = [
    dict(q="Pourquoi Spoutnik provoque-t-il un « choc » aux États-Unis ?", r=["Il a détruit un satellite américain",
                                                                           "Il prouve que l'URSS peut atteindre l'Amérique avec un missile",
                                                                           "Il émet de la propagande en anglais", "Il a été lancé depuis Cuba"], ok=1,
         ex="Le lanceur de Spoutnik est un missile intercontinental (R-7) : l'enjeu est d'abord militaire.", voir="choc"),
    dict(q="Qui est la première femme dans l'espace ?", r=["Sally Ride", "Valentina Terechkova", "Claudie Haigneré", "Christina Koch"], ok=1,
         ex="Valentina Terechkova, le 16 juin 1963 : une autre « première » soviétique.", voir="pr"),
    dict(q="Combien d'astronautes ont marché sur la Lune entre 1969 et 1972 ?", r=["2", "6", "12", "24"], ok=2,
         ex="Six missions Apollo se sont posées, avec deux marcheurs chacune : douze Américains.", voir="lun"),
    dict(q="Avec quel satellite la France devient-elle la troisième puissance spatiale ?", r=["Spot", "Astérix", "Hélios", "Galileo"], ok=1,
         ex="Astérix, lancé par la fusée Diamant le 26 novembre 1965 depuis Hammaguir (Algérie).", voir="espf"),
    dict(q="Quel pays réussit le premier atterrissage près du pôle Sud lunaire, le 23 août 2023 ?", r=["La Chine", "Le Japon", "L'Inde", "Les États-Unis"], ok=2,
         ex="L'Inde avec Chandrayaan-3, exemple d'une puissance spatiale émergente.", voir="ind"),
    dict(q="Pourquoi l'exemple de Starlink en Ukraine est-il important ?", r=["Il montre qu'un État en guerre peut dépendre d'une entreprise privée étrangère",
                                                                            "Il prouve que l'espace est démilitarisé", "Il a été financé par l'ONU", "Il remplace les SNLE"], ok=0,
         ex="Une entreprise devient un acteur géopolitique : son dirigeant peut décider seul de l'accès au service.", voir="ukr"),
    dict(q="Lequel de ces pays n'a PAS réalisé de tir antisatellite destructeur ?", r=["La Chine", "La Russie", "L'Inde", "La France"], ok=3,
         ex="Chine (2007), États-Unis (2008), Inde (2019), Russie (2021). La France n'en a pas réalisé.", voir="at"),
    dict(q="Qu'est-ce qui rend la dissuasion par SNLE crédible ?", r=["Leur vitesse", "Leur capacité de seconde frappe, car ils sont presque indétectables",
                                                                    "Leur nombre de torpilles", "Leur présence dans les ports"], ok=1,
         ex="Caché en mer, le SNLE survivrait à une attaque surprise et permettrait de riposter.", voir="sf"),
    dict(q="Où sont basés les SNLE français ?", r=["À Toulon", "À Cherbourg", "À l'Île Longue (rade de Brest)", "À Djibouti"], ok=2,
         ex="L'Île Longue ; Toulon est le port d'attache du porte-avions Charles-de-Gaulle.", voir="msn"),
    dict(q="Quelle base étrangère s'installe à Djibouti le 1er août 2017 ?", r=["La première base militaire chinoise à l'étranger", "Une base russe",
                                                                             "La première base française", "Une base de l'ONU"], ok=0,
         ex="Djibouti contrôle l'accès à la mer Rouge : la France, les États-Unis, le Japon et la Chine y ont des bases.", voir="bd"),
    dict(q="Quel auteur a théorisé le lien entre maîtrise des mers et puissance (1890) ?", r=["Clausewitz", "Mahan", "Grotius", "Kessler"], ok=1,
         ex="Alfred Mahan, The Influence of Sea Power upon History (1890).", voir="mah"),
]

CREDITS = [
    "Cartes : fond Natural Earth (domaine public), projection d3-geo (licence ISC) ; positions et trajets approximatifs.",
    "Chiffres : NASA, Pentagone (2024) ; sujet de dissertation inventé pour l'entraînement ; sujet de juin 2025 du baccalauréat.",
    "Photographies : réplique de Spoutnik 1, NSSDC / NASA (domaine public) ; Buzz Aldrin sur la Lune, Apollo 11, NASA (domaine public) ; "
    "via Wikimedia Commons.",
]
