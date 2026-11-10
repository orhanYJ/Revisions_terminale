"""SVT, thème 1.A, chapitre 4 : « Mécanismes de diversité non génétique du vivant » — la vidéo du chapitre.

Même chaîne que les vidéos de physique-chimie (outils/serie-pc/pc_ch5.py) : outils/serie-philo/generer.py svt_ch4,
verifier.py, chevauchements.py svt-ch4, fermer.py. Moteur svt/serie/moteur.js (type mental : la carte mentale du
thème 1.A, svt/carte-mentale.js) ; illustrations propres au chapitre dans svt/serie/illu-svt-ch4.js (c4_*).
Contenu : la page t4 de svt/index.html, rien au-delà. Tous ses exemples y sont : ver de Roscoff,
microbiote intestinal, gammare parasité, phrygane, jardinier satiné, araignée, port de Marseille, mésanges bleues,
nids et termitières, chimpanzés et noix (avec l'exercice du graphique), chant des oiseaux, baleines à bosse, et les
macaques de Koshima. Vidéo destinée à YouTube (10/11/2026) : que du contenu, aucune mention personnelle ni scolaire ;
seul « hors programme » est signalé. Graphique du chimpanzé schématique
(valeurs approchées) ; la réponse à la question 3 de l'exercice est une proposition.
"""

SITE = "svt"
CODE = "svt-ch4"
NOTION = "Mécanismes de diversité non génétique du vivant"
NUM = 4
TITRE = "Mécanismes de diversité non génétique du vivant"
RYTHME = "vivant"
SUIVANT = "Partie B · À la recherche du passé géologique de notre planète"
PRONONCIATION = {"Roscoff": "Roscoffe", "Coula": "Coula", "Parinari": "Parinari", "Pigliucci": "Pilioutchi",
                 "Müller": "Muleur", "Dawkins": "Dôkinss", "Koshima": "Koshima", "Tonga": "Tonnga", "terpènes": "terpènnes",
                 "limonène": "limonènne", "pinène": "pinènne"}

# exercice du chimpanzé : courbes schématiques, valeurs approchées (taux de succès en fonction de l'âge en mois)
PARINARI = [[0, 0], [9, 0], [11, .02], [14, .1], [18, .3], [22, .46], [26, .55], [30, .6], [40, .61], [50, .6], [60, .61], [70, .6]]
COULA = [[0, 0], [44, 0], [47, .03], [50, .15], [53, .33], [56, .47], [60, .55], [65, .56], [70, .55]]
AXES_CHIMP = dict(x=[0, 72], y=[0, 1], gx=[12, 24, 36, 48, 60, 72], gy=[.2, .4, .6, .8, 1], lx="âge (mois)", ly="taux de succès")

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="foret", humeur="mystere", carton=False, beats=[
        "{cm0}Voici la carte mentale du thème un, partie A : génétique et évolution. Quatre chapitres.",
        "Les trois premiers expliquent la diversité du vivant par les gènes. "
        "Les brassages de la reproduction sexuée. Les transferts de gènes. La dérive et la sélection.",
        "{cm0.1}Le chapitre quatre, lui, s'occupe de tout le reste : les autres mécanismes évolutifs. "
        "Son titre complet : mécanismes de diversité non génétique du vivant.",
        "Trois branches. Les associations entre êtres vivants. Le phénotype étendu. Et les comportements.",
        "{-cm0}{q0}Alors, une question pour commencer.",
        ("Le phénotype d'un être vivant ne dépend-il que de ses gènes ?", {"rate": "-6%"}),
        ("P", 0.8),
        "{-q0}{plan}Voici le chemin. {plan.1}D'abord, une idée neuve : l'hérédité non génétique.",
        ("{plan.2}Puis les associations : le ver de Roscoff, le microbiote humain, le gammare parasité. "
         "{plan.3}Ensuite, tout ce qu'un animal construit hors de son corps, de la larve de phrygane au port de Marseille. "
         "{plan.4}Puis les comportements appris : chimpanzés, oiseaux chanteurs, baleines à bosse.", {"rate": "+4%"}),
        "{plan.5}Et pour finir : un graphique à exploiter, une rédaction type bac, et l'essentiel pour l'examen.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "cm0": dict(type="mental", vers=["t1a", "c4"], pousse=True),
        "q0": dict(type="question", t="Le phénotype ne dépend-il que des gènes ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Le but du chapitre : l'hérédité non génétique",
            "Les associations : mutualisme et parasitisme",
            "Le phénotype étendu : ce qui est construit hors du corps",
            "Les comportements appris : chimpanzés, oiseaux, baleines",
            "L'exercice du graphique, une rédaction type bac, le bilan"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="SVT · Thème 1.A · Chapitre 4", t="Mécanismes de diversité non génétique du vivant",
                      sous="Tout le chapitre, de zéro au bac"),
    }),

    # ================================================================ I. le but du chapitre
    dict(id="but", chap="Le but du chapitre", fond="foret", humeur="lumiere",
         retenir="Le phénotype se diversifie aussi sans que le génome change. Hérédité non génétique : transmission, de génération en génération, d'informations non codées dans l'ADN.",
         beats=[
        "{rap}Petit rappel de Première. {rap.1}Le phénotype, ce sont les caractères d'un individu. Sa forme, sa couleur, son métabolisme, son comportement.",
        "{rap.2}Il dépend du génotype, c'est-à-dire des allèles. Mais pas seulement. L'environnement compte aussi.",
        "Jusqu'ici, on a surtout expliqué la diversité par les gènes. "
        "{-rap}{gen}{gen.1}Au chapitre un, les brassages de la reproduction sexuée : la formation des gamètes, puis la fécondation.",
        "{gen.2}Au chapitre deux, les transferts de gènes entre êtres vivants. "
        "{gen.3}Au chapitre trois, la dérive et la sélection, qui font varier les fréquences des allèles.",
        ("P", 0.7),
        "{-gen}{trois}Mais il existe d'autres façons de changer un phénotype. Et là, le génome ne bouge pas.",
        "{trois.1}Une association avec un autre être vivant. {trois.2}Ce que l'animal construit hors de son corps. {trois.3}Des comportements appris. "
        "Ce sont exactement les trois branches de la carte.",
        "{-trois}{but_c}Le but du chapitre est donc clair. "
        "{but_c.1}Reconsidérer la place centrale des gènes, pour expliquer comment le vivant se construit, se diversifie, et évolue.",
        "{-but_c}{def_hng}Et pour ça, il faut une idée nouvelle : l'hérédité non génétique.",
        ("{def_hng.1}C'est la transmission, de génération en génération, d'informations qui ne sont pas codées dans l'ADN.", {"rate": "-4%"}),
        "Retiens-la mot pour mot. C'est le fil rouge de tout le chapitre.",
        "{-def_hng}",
    ], vis={
        "rap": dict(type="liste", titre="Rappel de Première", items=[
            "Le phénotype : l'ensemble des caractères d'un individu",
            "Il dépend du génotype… et de l'environnement"], marques=["1", "2"], x=150, y=200, w=980),
        "gen": dict(type="liste", titre="Ce qu'on a vu : la diversité par les gènes", items=[
            "Chapitre 1 · les brassages de la reproduction sexuée",
            "Chapitre 2 · les transferts de gènes",
            "Chapitre 3 · la dérive et la sélection dans les populations"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "trois": dict(type="illu", nom="c4_trois", x=90, y=110, w=1100, h=520),
        "but_c": dict(type="note", titre="Le but du chapitre", cles=["place", "centrale", "gènes"],
                      t="Reconsidérer la place centrale des gènes dans l'explication de la construction, de la diversification et de l'évolution du vivant.",
                      x=170, y=200, w=940),
        "def_hng": dict(type="def", terme="Hérédité non génétique", cles=["transmission", "ADN"],
                        t="Transmission, de génération en génération, d'informations qui ne sont pas codées dans l'ADN.",
                        etape="Le fil rouge du chapitre.", x=170, y=190, w=940),
    }),

    # ================================================================ II. associations : le ver de Roscoff
    dict(id="roscoff", chap="Le mutualisme : le ver de Roscoff", fond="cellule", humeur="lumiere",
         retenir="Ver de Roscoff : les algues gagnent un habitat stable, le ver leur capacité photosynthétique. Association mutualiste ; partenaires interdépendants : symbiose.",
         beats=[
        "{cm1}Première branche : {cm1.1}les associations entre êtres vivants. Deux sous-branches : le mutualisme, et le parasitisme.",
        "{-cm1}{tab_ros}Premier exemple : le ver de Roscoff. Un minuscule ver plat marin, de un à cinq millimètres. Vert pomme, ou vert foncé.",
        "Et ce vert ne vient pas de lui. Il vient de milliers de micro-algues, logées sous sa peau.",
        "{-tab_ros}{ros}Regarde bien son histoire. {ros.1}Jeune, le ver est translucide. Il a un tube digestif. "
        "Et une seule fois dans sa vie, il avale des micro-algues.",
        "{ros.2}Les algues s'installent sous son épiderme. Elles se multiplient. Pendant ce temps, le tube digestif du ver régresse.",
        "{ros.3}Chez l'adulte, il a complètement disparu. Le ver ne mange plus ! Il est devenu autotrophe. "
        "Les algues font la photosynthèse, au soleil, et partagent avec lui ce qu'elles produisent.",
        "{ros.4}Alors, qui gagne quoi ?",
        "{-ros}{gain_ros}{gain_ros.g}Les micro-algues gagnent un habitat, et un environnement stable. "
        "{gain_ros.d}Le ver, lui, gagne leur photosynthèse. Il fabrique seul sa matière carbonée, sans rien manger venu de l'extérieur.",
        ("P", 0.6),
        "{-gain_ros}{def_mut}Voici la phrase à retenir.",
        ("{def_mut.1}Quand les deux partenaires tirent des bénéfices réciproques, on parle d'association mutualiste. "
         "{def_mut.2}Et quand ils sont devenus interdépendants, on parle de symbiose.", {"rate": "-4%"}),
        "Et voilà le point clé. Le ver est devenu vert, autotrophe, sans tube digestif. Son phénotype a tout changé. "
        "Son génome, lui, n'a pas bougé. C'est l'association qui a tout fait.",
        "{-def_mut}",
    ], vis={
        "cm1": dict(type="mental", vers=["c4", "c4a"]),
        "tab_ros": dict(type="tableau", img="ch4-roscoff", de=[1.0, .5, .5], a=[1.25, .55, .5],
                        legende="Vers de Roscoff (Symsagittifera roscoffensis) · Lou Wagstaffe, iNaturalist, CC BY"),
        "ros": dict(type="illu", nom="c4_roscoff", x=90, y=110, w=1100, h=540),
        "gain_ros": dict(type="cols", g="Les micro-algues", gq="un habitat ; un environnement stable",
                         d="Le ver de Roscoff", dq="leur capacité photosynthétique : il fabrique seul sa matière carbonée", vs="↔"),
        "def_mut": dict(type="def", terme="Association mutualiste", cles=["bénéfices", "réciproques", "interdépendants", "symbiose"],
                        t="Une association dont les deux partenaires tirent des bénéfices réciproques.",
                        etape="Les deux partenaires sont devenus interdépendants : on appelle cela une symbiose.", x=170, y=190, w=940),
    }),

    # ================================================================ III. le microbiote
    dict(id="microbiote", chap="Le mutualisme : le microbiote humain", fond="cellule", humeur="calme",
         retenir="Microbiote intestinal : les bactéries gagnent un habitat et une protection ; l'être humain digère des aliments sinon indigestes et voit son système immunitaire stimulé.",
         beats=[
        "{tab_bac}Deuxième exemple de mutualisme. Et celui-là nous concerne tous : le microbiote intestinal. "
        "Notre intestin abrite un nombre immense de bactéries. Ensemble, elles forment le microbiote.",
        "{-tab_bac}{gain_bac}{gain_bac.g}Que gagnent les bactéries ? Un habitat, et une protection.",
        "{gain_bac.d}Et l'être humain ? D'abord, il digère des aliments qui seraient sinon indigestes. "
        "Ensuite, son système immunitaire est stimulé.",
        "{-gain_bac}{obes}Autre point étonnant : le microbiote est relié à l'obésité. "
        "Des bactéries influencent donc un caractère du phénotype. Sans que les gènes y soient pour rien.",
        ("P", 0.7),
        "{-obes}{prem}Ça te rappelle quelque chose ? {prem.1}En Première, tu as vu la mycorhize. "
        "Le champignon aide la plante à absorber les sels minéraux. La plante, elle, lui fournit des sucres.",
        "{prem.2}Même chose avec les nodosités des racines. Deux espèces différentes, deux gagnants.",
        "{-prem}",
    ], vis={
        "tab_bac": dict(type="mot", t="Le microbiote", g="un très grand nombre de bactéries, dans l'intestin humain"),
        "gain_bac": dict(type="cols", g="Les bactéries", gq="un habitat ; une protection",
                         d="L'être humain", dq="digérer des aliments sinon indigestes ; un système immunitaire stimulé", vs="↔"),
        "obes": dict(type="note", titre="Remarque", cles=["obésité", "phénotype"],
                     t="Le microbiote est aussi relié à l'obésité : des bactéries influencent un caractère du phénotype.", x=170, y=220, w=940),
        "prem": dict(type="liste", titre="Rappel de Première · même logique", items=[
            "La mycorhize : le champignon aide la plante à absorber les sels minéraux, la plante lui fournit des sucres",
            "Les nodosités des racines, citées dans le bilan du chapitre"], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ IV. le parasitisme : le gammare
    dict(id="parasitisme", chap="Le parasitisme : le gammare", fond="cellule", humeur="tension",
         retenir="Parasitisme : un seul partenaire, le parasite, tire bénéfice de l'association ; pour l'hôte, elle est néfaste. Le parasite du gammare change son comportement.",
         beats=[
        "{def_par}Deuxième sous-branche : le parasitisme. Et cette fois, le partage n'est plus équitable. "
        "{def_par.1}Dans une association parasitaire, un seul des deux partenaires en tire bénéfice. Pour l'autre, elle est néfaste.",
        "{-def_par}{tab_gam}Exemple : le gammare. Un petit crustacé d'eau douce. Une proie pour les oiseaux.",
        "{-tab_gam}{comp}Certains gammares sont infestés par des parasites, qui s'enkystent dans leur corps. "
        "{comp.1}Et c'est là que tout bascule.",
        "Un gammare sain reste au fond, à l'abri. Le gammare parasité, lui, est attiré par la lumière. "
        "{comp.2}Il remonte à la surface. Il tournoie, frénétiquement. {comp.3}Résultat ? Une proie facile.",
        "Le parasite a changé le comportement de son hôte. Et ce n'est pas un hasard : c'est ce qui lui permet de continuer son cycle.",
        "{-comp}{cyc}Suivons ce cycle. Le parasite passe d'un hôte à l'autre. "
        "{cyc.1}Il se multiplie d'abord, de façon asexuée, chez un premier hôte intermédiaire.",
        "{cyc.2}Puis il vit sous forme de larves chez le gammare, le second hôte intermédiaire. "
        "{cyc.3}Enfin, il devient adulte dans l'intestin de l'oiseau, l'hôte définitif. Là, il se reproduit sexuellement.",
        "{cyc.4}Et ses œufs retournent dans l'eau. La boucle est bouclée. Retiens le principe, plus que les noms.",
        "{-cyc}{bil_par}Le bilan, maintenant. {bil_par.1}Le parasite exploite les ressources de son hôte, à son détriment. "
        "{bil_par.2}L'hôte lui offre un habitat, de la nourriture. {bil_par.3}Et même un taxi : le gammare emmène le parasite jusqu'à l'oiseau.",
        "{-bil_par}",
    ], vis={
        "def_par": dict(type="def", terme="Association parasitaire · parasitisme", cles=["seul", "néfaste"],
                        t="Un seul des deux partenaires tire bénéfice de l'association ; pour l'autre, elle est néfaste.", x=170, y=210, w=940),
        "tab_gam": dict(type="tableau", img="ch4-gammare", de=[1.0, .5, .5], a=[1.25, .5, .48],
                        legende="Un gammare (Gammarus pulex) · Alexis Tinker-Tsavalas, iNaturalist, CC BY"),
        "comp": dict(type="illu", nom="c4_comport", x=60, y=90, w=1160, h=580),
        "cyc": dict(type="illu", nom="c4_cycle", x=90, y=100, w=1100, h=560),
        "bil_par": dict(type="liste", titre="Ce que le gammare offre à son parasite", items=[
            "Le parasite exploite les ressources de son hôte, à son détriment",
            "Un habitat et de la nourriture",
            "Un moyen efficace de dispersion : le voyage jusqu'à l'oiseau"], marques=["−", "1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ V. bilan des associations
    dict(id="symbiose", chap="Le bilan : symbiose et phénotype", fond="foret", humeur="calme",
         retenir="Symbiose : association étroite, intime et durable entre organismes d'espèces différentes (mutualisme ou parasitisme). Elle modifie le phénotype de l'hôte sans changer son génome.",
         beats=[
        "{sym}Faisons le point sur cette première branche. "
        "{sym.3}La symbiose, c'est une association étroite, intime et durable, entre des organismes d'espèces différentes. Elle a deux formes.",
        "{sym.1}Le mutualisme : les deux partenaires y gagnent, comme les bactéries du microbiote et l'être humain. "
        "{sym.2}Le parasitisme : l'un profite, au détriment de l'autre, l'hôte.",
        ("P", 0.6),
        "{sym.4}Attention, piège ! Le mot symbiose a deux sens. "
        "Au chapitre deux, avec les endosymbioses, et pour le ver de Roscoff, il désigne une association à bénéfices réciproques, avec des partenaires interdépendants.",
        "Dans le bilan de ce chapitre, il désigne toute association étroite et durable. Parasitisme compris.",
        "{-sym}{piege_sym}Les deux usages existent chez les scientifiques. Alors, à l'écrit, dis dans quel sens tu l'emploies. "
        "Ou plus simple : parle de mutualisme et de parasitisme. Aucune ambiguïté.",
        "{-piege_sym}{effets}Et maintenant, l'idée qui relie tout. "
        "{effets.1}Nodosités, microbiote, parasitisme : toutes ces associations diversifient les métabolismes, {effets.2}les comportements, {effets.3}et donc la survie.",
        "{-effets}{conc_sym}Dans chaque cas, l'hôte change. Mais son génome, non. "
        "{conc_sym.1}La symbiose diversifie donc bien le phénotype des individus.",
        ("P", 0.8),
        "Pour aller plus loin, un détour hors programme. "
        "{-conc_sym}{hp1}{hp1.1}Les chercheurs distinguent plusieurs hérédités non génétiques. L'hérédité d'associations symbiotiques : les symbiotes passent à la descendance.",
        ("{hp1.2}L'hérédité épigénétique : une variation de l'expression des gènes, liée à l'environnement, est transmise. "
         "{hp1.3}L'hérédité écologique : on hérite de l'habitat de ses parents. "
         "{hp1.4}Les effets parentaux : l'action des parents influe sur le phénotype des petits. "
         "{hp1.5}Et l'hérédité culturelle : des comportements appris, transmis socialement.", {"rate": "+4%"}),
        "{-hp1}{hp2}En deux mille dix, deux chercheurs, Pigliucci et Müller, ont proposé d'étendre la théorie de l'évolution à ces processus. "
        "Une idée loin de faire l'unanimité : elle fait l'objet de vifs débats. Encore une fois, hors programme.",
        "{-hp2}",
    ], vis={
        "sym": dict(type="illu", nom="c4_symbiose", x=90, y=100, w=1100, h=540),
        "piege_sym": dict(type="note", titre="Deux sens du mot « symbiose »", cles=["sens", "mutualisme", "parasitisme"],
                          t="En devoir, précise le sens que tu emploies, ou parle de mutualisme et de parasitisme : aucune ambiguïté.",
                          x=170, y=220, w=940),
        "effets": dict(type="liste", titre="Ce que les associations diversifient", items=[
            "les métabolismes (ver de Roscoff autotrophe)", "les comportements (gammare parasité)", "et donc la survie"],
                       marques=["1", "2", "3"], x=150, y=190, w=980),
        "conc_sym": dict(type="def", terme="À retenir", cles=["phénotype", "génome"],
                         t="La symbiose contribue à diversifier le phénotype des individus, sans modification de leur génome.", x=170, y=220, w=940),
        "hp1": dict(type="liste", titre="Hors programme · les formes d'hérédité non génétique", petit=True, items=[
            "Hérédité d'associations symbiotiques : symbiotes transmis à la descendance",
            "Hérédité épigénétique : variation de l'expression des gènes transmise",
            "Hérédité écologique : on hérite de l'habitat de ses parents",
            "Hérédité par effets parentaux : l'action des parents sur le phénotype des descendants",
            "Hérédité culturelle : comportements appris transmis socialement"], marques=["1", "2", "3", "4", "5"], x=150, y=120, w=980),
        "hp2": dict(type="note", titre="Hors programme · un débat", plus=True, cles=["débats"],
                    t="Pigliucci et Müller (2010) proposent d'étendre la théorie de l'évolution à ces processus non génétiques. Point de vue loin d'être partagé : vifs débats.",
                    x=170, y=210, w=940),
    }),

    # ================================================================ VI. le phénotype étendu : quatre exemples
    dict(id="exemples_pe", chap="Le phénotype étendu : quatre exemples", fond="foret", humeur="lumiere", beats=[
        "{cm2}Deuxième branche : {cm2.1}le phénotype étendu. "
        "Une idée simple, mais vertigineuse : le phénotype d'un animal ne s'arrête pas aux limites de son corps. Quatre exemples.",
        "{-cm2}{tab_phr}Premier exemple : la larve de phrygane. La phrygane est un insecte. Sa larve vit dans l'eau.",
        "{-tab_phr}{phr}{phr.1}La larve se fabrique un fourreau de soie, avec les sécrétions de ses glandes. "
        "{phr.2}Puis elle le couvre de ce qu'elle trouve au fond de l'eau : des graviers, des débris. Le voilà blindé.",
        "{phr.3}Et quand il devient trop petit ? Elle l'abandonne. Et elle en construit un autre.",
        "{-phr}{tab_jar}Deuxième exemple : le jardinier satiné, un oiseau d'Australie. "
        "Le mâle construit une sorte de tonnelle, et il la décore, pour séduire les femelles. Sur la photo, il l'a entourée d'objets bleus.",
        "Une construction, donc. Hors du corps de l'animal.",
        "{-tab_jar}{tab_ara}Troisième exemple : l'araignée. Sa toile, son cocon. Fabriqués avec sa soie, mais à l'extérieur de son corps.",
        "{-tab_ara}{tab_mar}Et le quatrième, le plus surprenant : le port de Marseille. Construit par l'espèce humaine. "
        "Eh oui : nos constructions font partie de notre phénotype étendu.",
        "{-tab_mar}",
    ], vis={
        "cm2": dict(type="mental", vers=["c4", "c4b"]),
        "tab_phr": dict(type="tableau", img="ch4-phrygane", de=[1.0, .5, .5], a=[1.25, .5, .5],
                        legende="Larve de phrygane dans son fourreau de grains de sable · Jonas V., iNaturalist, CC BY"),
        "phr": dict(type="illu", nom="c4_phrygane", x=60, y=100, w=1160, h=540),
        "tab_jar": dict(type="tableau", img="ch4-jardinier", de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="La tonnelle d'un jardinier satiné mâle, Australie · Sockrosma, iNaturalist, CC BY"),
        "tab_ara": dict(type="tableau", img="ch4-araignee", de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Une épeire diadème sur sa toile · Ben G., iNaturalist, CC BY"),
        "tab_mar": dict(type="mot", t="Le port de Marseille", g="construit par l'espèce humaine : notre phénotype étendu"),
    }),

    # ================================================================ VII. la définition du phénotype étendu
    dict(id="def_pe", chap="Le phénotype étendu : la définition", fond="foret", humeur="calme",
         retenir="Phénotype étendu : tous les caractères d'un organisme situés hors de son corps, surtout son comportement et l'environnement qu'il construit. Un moteur évolutif non génétique.",
         beats=[
        "{eten}Rassemblons tout ça. Au centre, le corps de l'animal : sa forme, sa couleur, ses organes. Le phénotype au sens habituel. "
        "Et autour, tout ce qu'il construit. {eten.1}Le fourreau de la phrygane. {eten.2}La tonnelle du jardinier. "
        "{eten.3}La toile et le cocon de l'araignée. {eten.4}Le port des humains.",
        "{-eten}{def_pe}D'où la définition.",
        ("{def_pe.1}Le phénotype étendu, ce sont tous les caractères d'un organisme situés hors de son corps. "
         "Surtout son comportement, et l'environnement qu'il construit : nid, terrier, relations sociales.", {"rate": "-4%"}),
        ("P", 0.6),
        "{-def_pe}{rec}Trois idées en découlent. {rec.1}Beaucoup d'animaux recrutent des éléments non vivants dans leur milieu, et modulent ainsi leur phénotype. "
        "Nids d'oiseaux, toiles d'araignées, ruches. Et chez l'être humain, les exemples sont innombrables.",
        "{rec.2}Deuxième idée : prendre le contrôle d'un autre organisme élargit aussi le phénotype. Tu connais déjà un exemple. "
        "Le parasite du gammare ! Le comportement du gammare fait partie du phénotype étendu du parasite.",
        "{rec.3}Troisième idée : cet élargissement sert l'habitat, la survie, ou la séduction du partenaire.",
        "{-rec}Conclusion : c'est un {!moteur évolutif}moteur évolutif non génétique.",
        "{hp_dk}Une précision hors programme. L'expression phénotype étendu vient du biologiste britannique Richard Dawkins. "
        "C'est le titre d'un de ses livres, paru en mille neuf cent quatre-vingt-deux.",
        "{-hp_dk}",
    ], vis={
        "eten": dict(type="illu", nom="c4_etendu", x=90, y=100, w=1100, h=540),
        "def_pe": dict(type="def", terme="Phénotype étendu", cles=["hors", "comportement", "construit"],
                       t="Tous les caractères d'un organisme qui se situent hors de son corps : principalement son comportement et l'environnement qu'il construit (nid, terrier, relations sociales…).",
                       x=150, y=190, w=980),
        "rec": dict(type="liste", titre="Trois idées", items=[
            "Recruter des éléments non vivants du milieu : nids, toiles, ruches… et les constructions humaines",
            "Prendre le contrôle d'autres organismes : le parasite et le comportement du gammare",
            "Au service de l'habitat, de la survie, de l'attrait du partenaire sexuel"], marques=["1", "2", "3"], x=150, y=160, w=980),
        "hp_dk": dict(type="note", titre="Hors programme", plus=True, cles=["Dawkins"],
                      t="L'expression « phénotype étendu » vient du biologiste Richard Dawkins, titre de son livre de 1982.", x=170, y=230, w=940),
    }),

    # ================================================================ VIII. les mésanges
    dict(id="mesanges", chap="Des mésanges adeptes de l'aromathérapie", fond="foret", humeur="lumiere",
         retenir="La mésange bleue garnit son nid de plantes aromatiques riches en terpènes (insecticides, bactéricides, fongicides) : le nid protège les oisillons des parasites.",
         beats=[
        "{tab_mes}Jusqu'où peut aller le phénotype étendu ? Réponse avec les mésanges bleues. Des adeptes de l'aromathérapie !",
        "{-tab_mes}{mes}{mes.1}Chez la mésange bleue, la femelle glisse dans le nid des fragments frais de plantes aromatiques. "
        "{mes.2}Et elle le fait chaque jour, de la fin de la construction du nid jusqu'à l'envol des jeunes.",
        "Cinq plantes reviennent dans plus d'un quart des nids suivis. "
        "{-mes}{plantes}{plantes.1}L'achillée de Ligurie. {plantes.2}La lavande papillon. "
        "{plantes.3}L'immortelle d'Italie. {plantes.4}La menthe à feuilles rondes. {plantes.5}Et la pulicaire odorante.",
        "{-plantes}{tab_lav}{terp}Pourquoi celles-là ? {terp.1}Parce qu'elles sont riches en terpènes. Des molécules insecticides, bactéricides et fongicides.",
        "{terp.2}La lavande, par exemple, dégage du bêta-pinène, un puissant répulsif des insectes. "
        "{terp.3}Et au Portugal, les mésanges ajoutent des aiguilles de pin parasol, riches en limonène. De quoi réduire les puces et les poux.",
        "Le nid protège donc les oisillons des parasites. Le comportement de la mère, et le nid qu'elle construit, font partie de son phénotype étendu. "
        "Et ils augmentent la survie de ses petits.",
        "{-terp}{-tab_lav}",
    ], vis={
        "tab_mes": dict(type="tableau", img="ch4-mesange", de=[1.0, .5, .5], a=[1.2, .5, .45], legende="Une mésange bleue · Vladimir Kharuk, iNaturalist, CC BY"),
        "mes": dict(type="liste", titre="Ce que fait la femelle", items=[
            "Elle ajoute des fragments frais de plantes aromatiques entre les matériaux du nid",
            "Chaque jour, de la fin de la construction du nid jusqu'à l'envol des jeunes"], marques=["1", "2"], x=150, y=200, w=980),
        "plantes": dict(type="liste", titre="Dans plus d'un quart des nids suivis", items=[
            "L'achillée de Ligurie", "La lavande papillon", "L'immortelle d'Italie", "La menthe à feuilles rondes", "La pulicaire odorante"],
                        marques=["1", "2", "3", "4", "5"], x=150, y=140, w=980),
        "tab_lav": dict(type="tableau", img="ch4-lavande", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="La lavande papillon (Lavandula stoechas) · Marios Thoma, iNaturalist, CC BY"),
        "terp": dict(type="liste", titre="Des plantes riches en terpènes", items=[
            "Insecticides, bactéricides et fongicides",
            "La lavande : bêta-pinène, puissant répulsif des insectes",
            "Au Portugal : aiguilles de pin parasol, riches en limonène, contre puces et poux"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ================================================================ IX. comportements et ressources du milieu
    dict(id="ressources", chap="Des comportements qui dépendent du milieu", fond="foret", humeur="calme",
         retenir="Le comportement des individus dépend des ressources de leur environnement : nids, termitières, fourreaux de phryganes, parade du jardinier satiné.",
         beats=[
        "{cm3}Troisième et dernière branche : {cm3.1}les comportements. "
        "Les individus ne diffèrent pas seulement par leur forme. Ils diffèrent aussi par ce qu'ils font. Deux parties.",
        "{-cm3}{tab_ter}Première partie : des comportements qui dépendent du milieu. "
        "Un animal fait avec ce que son environnement lui offre. {res}Quatre cas.",
        ("{res.1}La construction des nids d'oiseaux. {res.2}Les termitières. {res.3}Les fourreaux des phryganes, faits avec les graviers et les débris disponibles. "
         "{res.4}Et le comportement reproducteur de certains oiseaux, comme le jardinier satiné.", {"rate": "+4%"}),
        "Le même animal, dans un autre milieu, construira autrement. Même génome. Phénotype différent.",
        "{-res}{-tab_ter}",
    ], vis={
        "cm3": dict(type="mental", vers=["c4", "c4c"]),
        "tab_ter": dict(type="tableau", img="ch4-termitiere", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Des termitières en Australie · Sockrosma, iNaturalist, CC BY"),
        "res": dict(type="liste", titre="Selon les ressources du milieu", items=[
            "Les nids d'oiseaux", "Les termitières", "Les fourreaux des phryganes", "La parade du jardinier satiné"],
                    marques=["1", "2", "3", "4"], x=150, y=170, w=980),
    }),

    # ================================================================ X. le chimpanzé et la casse des noix
    dict(id="chimpanze", chap="Des comportements transmis : les chimpanzés", fond="foret", humeur="lumiere",
         retenir="Certains comportements se transmettent entre individus d'une même espèce par voie non héréditaire : la casse des noix chez le chimpanzé, une culture de plus de 4 300 ans.",
         beats=[
        "{idee_c}Deuxième partie : des comportements transmis au sein d'une espèce. Mais pas par les gènes.",
        ("{idee_c.1}Certains comportements se transmettent, par voie non héréditaire, entre individus d'une même espèce. "
         "Preuve de plus : le phénotype ne repose pas que sur des bases génétiques.", {"rate": "-4%"}),
        "{-idee_c}{tab_chi}Premier exemple : le chimpanzé, casseur de noix.",
        "{-tab_chi}{noix}{noix.1}Il pose une noix sur une enclume, en bois ou en pierre. "
        "{noix.2}Il la frappe avec un percuteur. Encore. Et encore. {noix.3}Jusqu'à ce que la coque cède.",
        "{-noix}{cult}Et ce savoir-faire ne date pas d'hier. {cult.1}On a retrouvé des percuteurs enfouis dans le sol. "
        "{cult.2}Il se transmet depuis plus de deux cents générations. "
        "{cult.3}Les chercheurs parlent d'une véritable culture, vieille de plus de quatre mille trois cents ans.",
        "Mais alors, comment un jeune chimpanzé apprend-il ? C'est tout l'enjeu de l'exercice qui suit. À toi de jouer.",
        "{-cult}",
    ], vis={
        "idee_c": dict(type="def", terme="L'idée clé", cles=["non", "héréditaire", "génétiques"],
                       t="Certains comportements « phénotypiques » sont transmis, par voie non héréditaire, entre individus d'une même espèce.",
                       etape="Le phénotype ne repose pas que sur des bases génétiques.", x=170, y=190, w=940),
        "tab_chi": dict(type="tableau", img="ch4-chimpanze", de=[1.0, .5, .5], a=[1.2, .5, .45], legende="Une femelle chimpanzé et ses petits · Stan Rullman, iNaturalist, CC BY"),
        "noix": dict(type="illu", nom="c4_noix", x=60, y=100, w=1160, h=540),
        "cult": dict(type="liste", titre="Une culture vieille de plus de 4 300 ans", items=[
            "Des percuteurs retrouvés enfouis dans le sol",
            "Un savoir-faire transmis depuis plus de 200 générations",
            "Une véritable culture : plus de 4 300 ans"], marques=["1", "2", "3"], x=150, y=190, w=980),
    }),

    # ================================================================ XI. exercice 1 : le graphique du jeune chimpanzé
    dict(id="exo1", chap="Exercice · le jeune chimpanzé", fond="nuit", humeur="tension", beats=[
        "{ex1}Exercice : l'acquisition de comportements chez le jeune chimpanzé. "
        "Le document : un graphique. Le taux de succès du jeune, en fonction de son âge en mois, pour deux tâches.",
        "Une tâche facile : manger les fruits tendres de Parinari. Et une tâche difficile : casser, avec un outil, les noix de Coula. Très nourrissantes. Mais très dures.",
        "{-ex1}{gr1}{gr1.1}Première courbe : les fruits de Parinari. {gr1.2}Seconde courbe : les noix de Coula. "
        "Graphique schématique : les valeurs sont approchées.",
        "{-gr1}{ex1b}Trois questions. Un : décrire le graphique. Deux : comparer les deux comportements. "
        "Trois : des jeunes élevés sans congénères n'atteignent qu'un taux de succès de zéro virgule deux. Qu'en conclure ?",
        "{-ex1b}{pa1}Prends une feuille. Mets sur pause, et rédige tes trois réponses.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}{gr2}Voyons les réponses. Question un : décrire. Chaque courbe, avec des valeurs, dans l'ordre. "
        "{gr2.1}Pour les fruits de Parinari, le succès grimpe dès dix à quinze mois. {gr2.2}Il plafonne vers zéro virgule six, autour de trente mois.",
        "{gr2.3}Pour les noix de Coula, c'est zéro. Jusque vers quarante-cinq, cinquante mois. "
        "{gr2.4}Puis la courbe décolle brusquement, jusqu'à un plateau d'environ zéro virgule cinquante-cinq, vers soixante mois.",
        "{ex1c.q2}{gr2.5}Question deux : comparer. Au final, les deux niveaux sont proches. "
        "Mais la casse des noix, plus complexe, avec un outil, arrive bien plus tard. Environ trois ans plus tard ! Il faut un long apprentissage.",
        "{-gr2}{ex1c.q3}{rep3}{rep3.1}Question trois. Sans congénères à observer, le jeune n'atteint pas le niveau de ceux qui ont grandi dans le groupe. "
        "{rep3.2}Le comportement n'est donc pas inné. Il s'acquiert en observant et en imitant les adultes.",
        "{rep3.3}C'est une transmission culturelle. Pas génétique.",
        "{-rep3}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="L'acquisition de comportements chez le jeune chimpanzé", src="Exploitation d'un graphique",
                    enonce=["Le graphique donne le taux de succès du jeune chimpanzé en fonction de son âge (en mois), pour deux tâches.",
                            "Tâche facile : manger les fruits tendres de Parinari excelsa. Tâche compliquée : casser avec un outil les noix très nourrissantes, mais très dures, de Coula edulis."]),
        "gr1": dict(type="graphe", titre="Taux de succès selon l'âge", x=300, y=100, w=680, h=520, ax=AXES_CHIMP, el=[
            dict(type="courbe", pts=PARINARI, c="vert", lbl="fruits de Parinari", lp=[20, .72]),
            dict(type="courbe", pts=COULA, c="ca", lbl="noix de Coula", lp=[58, .7])]),
        "ex1b": dict(type="exo", niveau="simple", titre="Les questions", src="Exploitation d'un graphique",
                     questions=["Décrire le graphique.", "Comparer les deux comportements.",
                                "Des jeunes élevés sans congénères ont un taux de succès de 0,2. Qu'en conclure ?"]),
        "pa1": dict(type="pause", t="Décrire chaque courbe avec des valeurs, comparer, puis conclure sur les jeunes élevés seuls."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="Le jeune chimpanzé",
                     donnees=["Parinari : tâche facile", "Coula : tâche avec outil"],
                     questions=["Décrire", "Comparer", "Jeunes isolés : conclure"]),
        "gr2": dict(type="graphe", titre="Taux de succès selon l'âge", x=540, y=100, w=700, h=520, ax=AXES_CHIMP, tax=0, el=[
            dict(type="courbe", pts=PARINARI, c="vert", lbl="Parinari", lp=[22, .74], dur=.6),
            dict(type="point", x=30, y=.6, c="vert", proj=True, lbl="≈ 0,6 vers 30 mois", lp=[30, .82]),
            dict(type="courbe", pts=COULA, c="ca", lbl="Coula", lp=[52, .74], dur=.6),
            dict(type="point", x=60, y=.55, c="ca", proj=True, lbl="≈ 0,55 vers 60 mois", lp=[58, .4]),
            dict(type="texte", x=30, y=.25, t="≈ 3 ans d'écart", c="or")]),
        "rep3": dict(type="liste", titre="3 · Les jeunes élevés sans congénères", items=[
            "Ils n'atteignent pas le niveau des jeunes élevés dans le groupe",
            "Le comportement n'est pas inné : il s'acquiert par observation et imitation",
            "Une transmission culturelle, non génétique"], marques=["1", "2", "3"], x=540, y=170, w=700),
    }),

    # ================================================================ XII. la culture animale, le chant des oiseaux
    dict(id="oiseaux", chap="La culture animale et le chant des oiseaux", fond="aube", humeur="lumiere",
         retenir="Un oisillon isolé de ses congénères ne peut pas apprendre le chant de son espèce : ce chant n'est pas inné, il est acquis par entraînement et apprentissage.",
         beats=[
        "{cul}La culture, est-ce propre à l'être humain ? {cul.1}On l'a longtemps cru. "
        "{cul.2}Mais depuis les années mille neuf cent quatre-vingt-dix, les spécialistes du comportement animal ont montré qu'une culture animale existe.",
        ("{cul.3}Imitation du langage, usage d'outils, codes sociaux. "
         "{cul.4}Et transmission entre congénères, avec des variantes selon les régions.", {"rate": "+4%"}),
        "{-cul}{def_cul}{def_cul.1}La culture concerne tous les animaux qui ont une organisation sociale. "
        "C'est l'ensemble des savoirs et des pratiques qui se partagent et se transmettent dans un groupe. Et cette transmission n'a rien de génétique.",
        "{-def_cul}{tab_ois}Deuxième exemple : le chant des oiseaux.",
        "Un oisillon isolé de tous ses congénères ne peut pas apprendre. Son chant sera très éloigné de celui de son espèce. "
        "{-tab_ois}{chant}Regarde ce schéma. Des sonogrammes simplifiés : le temps de gauche à droite, la hauteur du son de bas en haut.",
        "{chant.1}En haut, le chant d'un adulte. {chant.2}Au milieu, un jeune élevé avec ses congénères : après entraînement, il reproduit ce chant. "
        "{chant.3}En bas, un jeune élevé seul. Son chant ne ressemble plus du tout à celui de son espèce.",
        "{-chant}{bil_ch}Le bilan. {bil_ch.1}Ce chant s'apprend. L'oisillon le maîtrise par entraînement. "
        "{bil_ch.2}C'est une transmission non génétique d'un comportement. Autrement dit : il n'est pas inné.",
        "Deux mots à bien fixer. {-bil_ch}{inne}{inne.g}Un comportement inné se met en place sans apprentissage. "
        "{inne.d}Un comportement acquis s'apprend, par observation et entraînement.",
        "Et le test, c'est l'isolement. Un individu isolé n'acquiert pas un comportement qui s'apprend.",
        "{-inne}",
    ], vis={
        "cul": dict(type="liste", titre="La culture animale", items=[
            "Longtemps, la culture a été considérée comme propre à l'humanité",
            "Depuis les années 1990 : une culture animale existe aussi",
            "Imitation du langage, utilisation d'outils, codes sociaux",
            "Transmission entre congénères, avec des variantes selon les régions"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "def_cul": dict(type="def", terme="La culture", cles=["savoirs", "pratiques", "génétique"],
                        t="L'ensemble des savoirs et des pratiques qui se partagent et se transmettent socialement au sein d'un groupe ; cette transmission n'est pas un héritage génétique.",
                        x=150, y=200, w=980),
        "tab_ois": dict(type="tableau", img="ch4-oiseau", de=[1.0, .5, .5], a=[1.25, .5, .45], legende="Un pinson des arbres, oiseau chanteur · Donald Davesne, iNaturalist, CC BY"),
        "chant": dict(type="illu", nom="c4_chant", x=40, y=110, w=1200, h=520),
        "bil_ch": dict(type="def", terme="Bilan · le chant des oiseaux", cles=["apprentissage", "inné"],
                       t="Le chant montre une démarche d'apprentissage : l'oisillon le maîtrise par entraînement.",
                       etape="Transmission non génétique d'un comportement : il n'est pas inné.", x=170, y=190, w=940),
        "inne": dict(type="cols", g="Comportement inné", gq="se met en place sans apprentissage",
                     d="Comportement acquis", dq="s'apprend, par observation et entraînement", vs="≠",
                     repere="le test : isoler l'individu"),
    }),

    # ================================================================ XIII. les baleines à bosse
    dict(id="baleines", chap="Le chant des baleines à bosse", fond="nuit", humeur="mystere",
         retenir="Chez les baleines à bosse, un nouveau chant apparaît en Australie et gagne, en un ou deux ans, les populations plus à l'est : il se transmet par apprentissage, pas par les gènes.",
         beats=[
        "Troisième exemple, et le plus spectaculaire : {tab_bal}le chant des baleines à bosse du Pacifique. "
        "Chez cette espèce, seuls les mâles chantent. Surtout pour séduire les femelles, pendant les migrations de la saison des amours.",
        "{-tab_bal}{str}Ce chant est très organisé. {str.1}Des unités sonores forment des phrases, répétées. {str.2}Les phrases forment un thème. "
        "{str.3}Un chant compte de quatre à sept thèmes, dans un ordre précis, {str.4}pendant huit à trente minutes.",
        "{-str}{varie}Et ce chant bouge. {varie.1}Il diffère selon la population, et selon le moment de l'année. {varie.2}Des variations s'y accumulent.",
        "{-varie}{bal}De mille neuf cent quatre-vingt-dix-huit à deux mille huit, des chercheurs ont suivi le chant de six populations, de l'Australie à la Polynésie française. "
        "{bal.1}Un nouveau chant apparaît d'abord en Australie.",
        "{bal.2}Et un ou deux ans plus tard, on l'entend plus à l'est : en Nouvelle-Calédonie, aux Tonga, aux Samoa américaines, aux îles Cook, en Polynésie.",
        ("P", 0.6),
        "Aucun changement génétique ne pourrait voyager aussi vite. Le chant passe d'une population à l'autre par apprentissage. Pas par les gènes.",
        "{-bal}",
    ], vis={
        "tab_bal": dict(type="tableau", img="ch4-baleine", de=[1.0, .5, .5], a=[1.2, .5, .45], legende="Une baleine à bosse · Lawrence Hylton, iNaturalist, CC BY"),
        "str": dict(type="liste", titre="Comment est fait un chant", items=[
            "Des unités sonores organisées en phrases répétées", "Des phrases qui forment un thème",
            "De 4 à 7 thèmes, repris dans un ordre précis", "Pendant 8 à 30 minutes"], marques=["1", "2", "3", "4"], x=150, y=160, w=980),
        "varie": dict(type="liste", titre="Un chant qui change", items=[
            "Il diffère selon la population et le moment de l'année", "Des variations s'y accumulent"],
                      marques=["1", "2"], x=150, y=210, w=980),
        "bal": dict(type="illu", nom="c4_baleines", x=60, y=90, w=1160, h=580),
    }),

    # ================================================================ XIV. le bilan du chapitre
    dict(id="bilan", chap="Le bilan du chapitre", fond="aube", humeur="lumiere",
         retenir="La transmission culturelle et comportementale est aussi un moteur évolutif.",
         beats=[
        "{bil}Le bilan du chapitre. {bil.1}Certains comportements se transmettent entre congénères, sans les gènes : par observation et apprentissage. "
        "Le chant et l'alimentation des oiseaux. L'alimentation des macaques.",
        "{bil.2}Isolé de ses proches, un individu n'acquiert pas le langage adulte, ou alors incomplet. Il n'est donc pas inné.",
        "{bil.3}Comme les sources d'apprentissage varient, les individus se diversifient. Surtout dans les sociétés humaines, où les échanges se sont multipliés. "
        "{bil.4}Et selon leurs conséquences, ces comportements se maintiennent, ou non. Ils ont façonné l'évolution technique et culturelle des espèces.",
        ("P", 0.6),
        "{-bil}{frappe_m}La conclusion : la transmission culturelle et comportementale est, elle aussi, un moteur évolutif.",
        "{-frappe_m}{tab_mac}Et ces macaques ? Voici l'exemple classique, bien connu des primatologues : {mac}{mac.1}les macaques japonais de l'île de Koshima.",
        "{mac.2}Dans les années mille neuf cent cinquante, une jeune femelle se met à laver dans l'eau les patates douces données par les chercheurs. "
        "{mac.3}L'habitude se répand dans le groupe. D'abord chez les jeunes. Puis de génération en génération.",
        "Même mécanisme que pour les chimpanzés et les oiseaux. Un comportement nouveau, appris, transmis. Sans aucun gène nouveau.",
        "{-mac}{-tab_mac}",
    ], vis={
        "bil": dict(type="liste", titre="Bilan du chapitre", petit=True, items=[
            "Des comportements se transmettent entre congénères, par observation et apprentissage (oiseaux, macaques)",
            "Isolé de ses proches, l'individu n'acquiert pas le langage adulte : il n'est pas inné",
            "Les sources d'apprentissage varient : diversification des individus",
            "Maintenus ou non selon leurs conséquences : évolution technique et culturelle"], marques=["1", "2", "3", "4"], x=150, y=120, w=980),
        "frappe_m": dict(type="mot", t="Un moteur évolutif", g="la transmission culturelle et comportementale"),
        "tab_mac": dict(type="tableau", img="ch4-macaque", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Un macaque japonais · Justin, iNaturalist, CC BY"),
        "mac": dict(type="liste", titre="Exemple · les macaques de Koshima", items=[
            "Des macaques japonais, sur l'île de Koshima",
            "Années 1950 : une jeune femelle lave les patates douces dans l'eau",
            "Le comportement se répand : d'abord les jeunes, puis de génération en génération"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ XV. exercice 2 : la rédaction type bac
    dict(id="exo2", chap="Exercice · une rédaction type bac", fond="nuit", humeur="tension", beats=[
        "{ex2}Dernier exercice, au format du bac : une question de synthèse. "
        "Montrer, à l'aide d'exemples précis, que le phénotype des êtres vivants peut se diversifier sans modification de leur génome.",
        "Une introduction, un développement structuré, une conclusion. Trente minutes.",
        "{-ex2}{pa2}C'est le moment de vérité. Mets sur pause. Un plan au brouillon d'abord, puis la rédaction.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Voici une proposition de réponse. "
        "{intro}{intro.1}L'introduction pose le décor. La diversité des phénotypes s'explique surtout par des mécanismes génétiques : "
        "brassages de la reproduction sexuée, mutations, transferts de gènes.",
        "{intro.2}Pourtant, d'autres mécanismes diversifient le phénotype sans toucher à l'ADN. {intro.3}Lesquels ? Voilà la problématique.",
        "{-intro}{ex2c.q2}{dev}Le développement suit les trois branches du chapitre. {dev.1}Première partie : les associations. "
        "Le ver de Roscoff et ses algues, le microbiote et l'être humain, pour le mutualisme. Le gammare parasité, pour le parasitisme. "
        "Et l'idée clé : l'hôte change de métabolisme ou de comportement, mais pas de génome.",
        "{dev.2}Une transition : le phénotype ne s'arrête pas non plus aux limites du corps. "
        "{dev.3}Deuxième partie : le phénotype étendu. Sa définition, puis la phrygane, l'araignée, les mésanges et leurs plantes, le port de Marseille.",
        "{dev.4}Troisième partie : les comportements appris. Le jeune chimpanzé, qui ne casse les noix que vers quarante-cinq à soixante mois. "
        "L'oisillon isolé, qui chante autrement. Et le chant des baleines, qui passe d'une population à l'autre en un ou deux ans.",
        "{-dev}{ex2c.q3}{concl}{concl.1}La conclusion répond à la question : associations, phénotype étendu et apprentissage diversifient les phénotypes, "
        "sans modifier les génomes. {concl.2}Puis elle ouvre. Selon leurs conséquences, ces caractères se maintiennent ou non. "
        "La transmission culturelle est, elle aussi, un moteur évolutif.",
        ("P", 0.6),
        "{-concl}{grille}Vérifie ta rédaction avec cette grille.",
        ("{grille.1}La problématique. {grille.2}Les exemples de mutualisme et de parasitisme, avec l'idée clé. {grille.3}Une transition. "
         "{grille.4}La définition du phénotype étendu, et ses exemples. {grille.5}Le chimpanzé, l'oisillon isolé, les baleines. "
         "{grille.6}Et la conclusion sur le moteur évolutif.", {"rate": "+4%"}),
        "Chaque exemple doit être précis : un nom, un chiffre, un mécanisme. C'est ça qui fait la note.",
        "{-grille}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", titre="Une diversité qui ne vient pas des gènes", src="Restitution des connaissances (30 min)",
                    enonce=["Montrer, à l'aide d'exemples précis, que le phénotype des êtres vivants peut se diversifier sans modification de leur génome.",
                            "Réponds par une introduction, un développement structuré et une conclusion."]),
        "pa2": dict(type="pause", t="Un plan au brouillon (trois parties), des exemples précis, puis la rédaction."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", titre="Diversité sans modification du génome",
                     questions=["Introduction", "Développement", "Conclusion"]),
        "intro": dict(type="liste", titre="Introduction", petit=True, items=[
            "Le constat : la diversité vient surtout de mécanismes génétiques",
            "Pourtant, d'autres mécanismes diversifient le phénotype sans toucher à l'ADN",
            "Problématique : lesquels ?"], marques=["1", "2", "?"], x=540, y=150, w=700),
        "dev": dict(type="liste", titre="Développement", petit=True, items=[
            "I · Associations : ver de Roscoff, microbiote ; gammare parasité",
            "Transition : le phénotype ne s'arrête pas aux limites du corps",
            "II · Phénotype étendu : définition ; phrygane, araignée, mésanges, port",
            "III · Comportements appris : chimpanzé, oisillon isolé, baleines"], marques=["I", "→", "II", "III"], x=540, y=110, w=700),
        "concl": dict(type="liste", titre="Conclusion", petit=True, items=[
            "Réponse : le phénotype se diversifie sans modifier le génome",
            "Ouverture : la transmission culturelle est un moteur évolutif"], marques=["1", "2"], x=540, y=180, w=700),
        "grille": dict(type="liste", titre="La grille · à cocher", petit=True, items=[
            "Problématique : une diversité sans modification du génome",
            "Roscoff, microbiote, gammare, et l'idée clé",
            "Une phrase de transition",
            "Définition et exemples du phénotype étendu",
            "Chimpanzé, chant des oiseaux, baleines à bosse",
            "Conclusion : un moteur évolutif"], marques=["✓"] * 6, x=540, y=90, w=700),
    }),

    # ================================================================ XVI. pour le bac
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons. Au centre, une idée : le phénotype se diversifie sans que le génome change. "
        "{carte.1}Le mutualisme : des bénéfices réciproques. Le ver de Roscoff, le microbiote. "
        "{carte.2}Le parasitisme : un seul gagnant. Le gammare.",
        "{carte.3}Le phénotype étendu : tout ce qui est hors du corps. De la phrygane au port de Marseille, sans oublier les mésanges. "
        "{carte.4}Et les comportements appris : chimpanzés, oiseaux, baleines, macaques.",
        "{-carte}{pieges}Quatre pièges à éviter. {pieges.1}Écrire que le génome de l'hôte change. C'est tout le contraire du chapitre ! "
        "{pieges.2}Employer symbiose sans préciser le sens. Ou alors, parle de mutualisme et de parasitisme.",
        "{pieges.3}Confondre inné et acquis. C'est l'isolement qui tranche. "
        "{pieges.4}Et une idée sans exemple précis. Jamais.",
        "{-pieges}{bac}Voici ce que tu dois savoir faire. À cocher.",
        ("{bac.1}Définir l'hérédité non génétique. {bac.2}Définir le mutualisme et le parasitisme, avec un exemple chacun. "
         "{bac.3}Définir la symbiose, en précisant le sens. {bac.4}Définir le phénotype étendu, avec des exemples.", {"rate": "+4%"}),
        "{bac.5}Exploiter un graphique d'apprentissage, comme celui du chimpanzé. "
        "{bac.6}Expliquer pourquoi un comportement n'est pas inné. {bac.7}Et rédiger une synthèse sur la diversité non génétique.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre.",
        "{-bac}{cm4}Et voici la carte complète de la partie A. {cm4.1}Le chapitre quatre la referme. "
        "Après les gènes, il montre que le vivant se diversifie, et évolue, aussi sans eux. "
        "Et maintenant ? Les questions du quiz, juste sous la vidéo.",
        ("P", 2.5),
    ], vis={
        "carte": dict(type="carte", centre="LE PHÉNOTYPE SANS LE GÉNOME", branches=[
            dict(t="Le mutualisme", items=["bénéfices réciproques", "ver de Roscoff et algues", "microbiote et être humain"]),
            dict(t="Le parasitisme", items=["un seul bénéficiaire", "le gammare parasité", "comportement modifié"]),
            dict(t="Le phénotype étendu", items=["hors du corps", "phrygane, araignée, nid", "mésanges, port de Marseille"]),
            dict(t="Les comportements appris", items=["chimpanzés et noix", "chant des oiseaux", "baleines à bosse"])]),
        "pieges": dict(type="liste", titre="Quatre pièges", items=[
            "Écrire que le génome de l'hôte change", "Employer « symbiose » sans préciser le sens",
            "Confondre inné et acquis (l'isolement tranche)", "Une idée sans exemple précis"], marques=["✗", "✗", "✗", "✗"], x=150, y=160, w=980),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", petit=True, items=[
            "Définir l'hérédité non génétique", "Mutualisme et parasitisme, un exemple chacun", "La symbiose, en précisant le sens",
            "Le phénotype étendu et ses exemples", "Exploiter un graphique d'apprentissage", "Montrer qu'un comportement n'est pas inné",
            "Rédiger une synthèse sur la diversité non génétique"], marques=["✓"] * 7, x=170, y=120, w=940),
        "cm4": dict(type="mental", vers=["c4", "t1a"]),
    }),
]

QUIZ = [
    dict(q="Qu'appelle-t-on hérédité non génétique ?",
         r=["La transmission des mutations de l'ADN", "La transmission, de génération en génération, d'informations non codées dans l'ADN",
            "L'absence de transmission entre générations"], ok=1,
         ex="C'est le fil rouge du chapitre : symbiotes, habitat, comportements appris peuvent se transmettre sans l'ADN.", voir="def_hng"),
    dict(q="Que gagne le ver de Roscoff de son association avec des micro-algues ?",
         r=["Un habitat et une protection", "Leur capacité photosynthétique : il fabrique seul sa matière carbonée", "De nouveaux gènes"], ok=1,
         ex="Les algues gagnent un habitat stable ; le ver devient autotrophe et son tube digestif disparaît chez l'adulte.", voir="gain_ros"),
    dict(q="Dans une association parasitaire…",
         r=["les deux partenaires tirent bénéfice de l'association", "un seul partenaire en tire bénéfice, au détriment de l'autre",
            "aucun partenaire n'en tire bénéfice"], ok=1,
         ex="Le parasite du gammare profite de son hôte (habitat, nourriture, dispersion) ; pour le gammare, c'est néfaste.", voir="def_par"),
    dict(q="Pourquoi le gammare parasité devient-il une proie facile pour les oiseaux ?",
         r=["Le parasite le rend attiré par la lumière : il remonte et tournoie en surface", "Il perd sa carapace", "Il ne peut plus nager"], ok=0,
         ex="Le parasite modifie le comportement de son hôte : c'est ce qui lui permet d'atteindre l'oiseau, son hôte définitif.", voir="comp"),
    dict(q="Dans le bilan du chapitre 4, la symbiose désigne…",
         r=["uniquement une association à bénéfices réciproques", "toute association étroite, intime et durable entre espèces différentes",
            "une association entre individus de la même espèce"], ok=1,
         ex="Le bilan l'élargit au parasitisme ; au chapitre 2, le mot désigne une association à bénéfices réciproques. Précise le sens en devoir.", voir="piege_sym"),
    dict(q="Le phénotype étendu, c'est…",
         r=["l'ensemble des caractères d'un organisme situés hors de son corps", "le phénotype d'un individu adulte",
            "les caractères dus à plusieurs gènes"], ok=0,
         ex="Surtout le comportement et l'environnement construit : fourreau de phrygane, toile d'araignée, nid, port de Marseille.", voir="def_pe"),
    dict(q="Pourquoi les mésanges bleues ajoutent-elles des plantes aromatiques dans leur nid ?",
         r=["Pour le rendre plus confortable", "Leurs terpènes éloignent insectes, bactéries et champignons : le nid protège les oisillons des parasites",
            "Pour nourrir les oisillons"], ok=1,
         ex="Lavande (bêta-pinène), pin parasol (limonène) : insecticides, bactéricides, fongicides.", voir="terp"),
    dict(q="Le jeune chimpanzé maîtrise la casse des noix de Coula…",
         r=["dès 10 à 15 mois, comme les fruits de Parinari", "vers 45 à 60 mois, environ trois ans plus tard que les fruits tendres", "jamais"], ok=1,
         ex="La tâche demande un outil : il faut un long apprentissage, par observation et imitation des adultes.", voir="gr2"),
    dict(q="Un oisillon élevé seul présente un chant très éloigné de celui de son espèce. On en conclut que ce chant…",
         r=["est inné", "n'est pas inné : il s'acquiert par apprentissage", "dépend d'une mutation"], ok=1,
         ex="L'isolement est le test : un comportement appris ne s'acquiert pas sans congénères.", voir="bil_ch"),
    dict(q="Un nouveau chant de baleine à bosse apparaît en Australie, puis gagne en un ou deux ans les populations plus à l'est. Cela montre que…",
         r=["le chant se transmet par apprentissage, pas par les gènes", "une mutation s'est propagée très vite", "les baleines d'Australie migrent toutes en Polynésie"], ok=0,
         ex="Une transmission aussi rapide d'une population à l'autre est culturelle : la transmission culturelle est un moteur évolutif.", voir="bal"),
]

CREDITS = [
    "Photos : iNaturalist, licence CC BY : Lou Wagstaffe (vers de Roscoff), Alexis Tinker-Tsavalas (gammare), Jonas V. (phrygane), "
    "Sockrosma (tonnelle du jardinier satiné, termitières), Ben G. (épeire), Vladimir Kharuk (mésange bleue), Marios Thoma (lavande papillon), "
    "Stan Rullman (chimpanzés), Donald Davesne (pinson des arbres), Lawrence Hylton (baleine à bosse), Justin (macaque japonais).",
    "Carte mentale du thème. Illustrations, schémas et graphique : faits pour la vidéo ; le graphique du chimpanzé "
    "est schématique (valeurs approchées), les sonogrammes et la carte des baleines sont schématiques.",
]
