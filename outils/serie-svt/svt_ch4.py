"""SVT, thème 1.A, chapitre 4 : « Mécanismes de diversité non génétique du vivant » — le cours en vidéo.

Même chaîne que les vidéos de physique-chimie (outils/serie-pc/pc_ch5.py) : outils/serie-philo/generer.py svt_ch4,
verifier.py, chevauchements.py svt-ch4, fermer.py. Moteur svt/serie/moteur.js (type mental : la carte mentale du
thème 1.A, svt/carte-mentale.js) ; illustrations propres au chapitre dans svt/serie/illu-svt-ch4.js (c4_*).
Contenu : la page t4 du site (svt/index.html), rien au-delà. Tous les exemples du cours y sont : ver de Roscoff,
microbiote intestinal, gammare parasité, phrygane, jardinier satiné, araignée, port de Marseille, mésanges bleues,
nids et termitières, chimpanzés et noix (avec l'exercice du graphique), chant des oiseaux, baleines à bosse, et les
macaques du bilan (exemple de Koshima, déjà signalé sur le site comme extérieur au diaporama). Ce qui vient d'ailleurs
est dit à voix haute (« précision qui ne vient pas de ton cours ») ; ce qui dépasse le programme est dit « hors programme ».
Le graphique du chimpanzé est redessiné d'après la description du site (valeurs approchées) ; la question 3 de
l'exercice est incomplète sur la diapositive : la réponse est une proposition (aucune correction reçue).
"""

SITE = "svt"
CODE = "svt-ch4"
NOTION = "Mécanismes de diversité non génétique du vivant"
NUM = 4
TITRE = "Mécanismes de diversité non génétique du vivant"
SUIVANT = "Partie B · À la recherche du passé géologique de notre planète"
PRONONCIATION = {"Roscoff": "Roscoffe", "Coula": "Coula", "Parinari": "Parinari", "Pigliucci": "Pilioutchi",
                 "Müller": "Muleur", "Dawkins": "Dôkinss", "Koshima": "Koshima", "Tonga": "Tonnga", "terpènes": "terpènnes",
                 "limonène": "limonènne", "pinène": "pinènne"}

# exercice du chimpanzé : courbes redessinées d'après la description du cours (taux de succès en fonction de l'âge en mois)
PARINARI = [[0, 0], [9, 0], [11, .02], [14, .1], [18, .3], [22, .46], [26, .55], [30, .6], [40, .61], [50, .6], [60, .61], [70, .6]]
COULA = [[0, 0], [44, 0], [47, .03], [50, .15], [53, .33], [56, .47], [60, .55], [65, .56], [70, .55]]
AXES_CHIMP = dict(x=[0, 72], y=[0, 1], gx=[12, 24, 36, 48, 60, 72], gy=[.2, .4, .6, .8, 1], lx="âge (mois)", ly="taux de succès")

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="foret", humeur="mystere", carton=False, beats=[
        "{cm0}Voici la carte mentale de la partie A du thème un : génétique et évolution. "
        "Quatre chapitres. Les trois premiers expliquent la diversité du vivant par les gènes : "
        "les brassages de la reproduction sexuée, les transferts de gènes, la dérive et la sélection dans les populations.",
        "{cm0.1}Le chapitre quatre, lui, s'intéresse à tout le reste. Ta prof l'appelle, sur sa carte : autres mécanismes évolutifs. "
        "Sur le site, son titre complet est : mécanismes de diversité non génétique du vivant. "
        "Trois branches : les associations entre êtres vivants, le phénotype étendu, et les comportements.",
        "{-cm0}{q0}Alors, posons la question du chapitre.",
        ("Le phénotype d'un être vivant ne dépend-il que de ses gènes ?", {"rate": "-6%"}),
        "{-q0}{plan}Voici le chemin. {plan.1}D'abord le but du chapitre, et l'idée d'hérédité non génétique. "
        "{plan.2}Puis les associations entre êtres vivants : le mutualisme, avec le ver de Roscoff et ton microbiote, et le parasitisme, avec le gammare. "
        "{plan.3}Ensuite le phénotype étendu : ce qu'un animal construit hors de son corps, de la larve de phrygane au port de Marseille. "
        "{plan.4}Puis les comportements appris : les chimpanzés qui cassent des noix, le chant des oiseaux, celui des baleines à bosse. "
        "{plan.5}Et pour finir, l'exercice du graphique corrigé, une rédaction type bac, et tout ce qu'il faut savoir pour l'examen.",
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
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. le but du chapitre
    dict(id="but", chap="Le but du chapitre", fond="foret", humeur="lumiere",
         retenir="Le phénotype se diversifie aussi sans que le génome change. Hérédité non génétique : transmission, de génération en génération, d'informations non codées dans l'ADN.",
         beats=[
        "{rap}Un rappel de Première, d'abord. {rap.1}Le phénotype, ce sont les caractères d'un individu : sa forme, sa couleur, son métabolisme, son comportement. "
        "{rap.2}Il dépend de son génotype, c'est-à-dire de ses allèles. Mais pas seulement : il dépend aussi de l'environnement.",
        "Depuis le début de l'année, on a surtout expliqué la diversité des phénotypes par des mécanismes génétiques. "
        "{-rap}{gen}{gen.1}Au chapitre un, les brassages de la reproduction sexuée, pendant la formation des gamètes et la fécondation. "
        "{gen.2}Au chapitre deux, les transferts de gènes entre êtres vivants. "
        "{gen.3}Au chapitre trois, la dérive et la sélection, qui font varier les fréquences des allèles dans les populations.",
        "{-gen}{trois}Mais en dehors de ces processus génétiques, d'autres mécanismes diversifient aussi le phénotype des individus. "
        "Le génome, lui, ne change pas. {trois.1}Le phénotype peut changer par des associations entre êtres vivants. "
        "{trois.2}Par ce que l'animal construit hors de son corps. {trois.3}Et par des comportements appris. "
        "Ce sont exactement les trois branches de la carte de ta prof.",
        "{-trois}{but_c}Ton cours donne le but du chapitre dès sa première diapositive. "
        "{but_c.1}Il s'agit de reconsidérer la place centrale des gènes dans l'explication de la construction, de la diversification et de l'évolution du vivant.",
        "{-but_c}{def_hng}Et elle introduit une idée nouvelle : l'hérédité non génétique. "
        "{def_hng.1}C'est la transmission, de génération en génération, d'informations qui ne sont pas codées dans l'ADN. "
        "Retiens cette définition mot pour mot : c'est le fil rouge de tout le chapitre.",
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
        "but_c": dict(type="note", titre="Le but du chapitre (diapositive 1)", cles=["place", "centrale", "gènes"],
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
        "{cm1}Première branche de la carte : {cm1.1}les associations entre êtres vivants. "
        "Elle a deux sous-branches : le mutualisme, et le parasitisme.",
        "{-cm1}{tab_ros}Premier exemple du cours : le ver de Roscoff. C'est un minuscule ver plat marin, de un à cinq millimètres. "
        "Il est vert pomme à vert foncé. "
        "Et ce vert ne vient pas de lui : il vient de milliers de micro-algues vertes, logées sous son épiderme.",
        "{-tab_ros}{ros}Regarde son histoire. {ros.1}Jeune, le ver est translucide, et il a un tube digestif. "
        "Il ingère des micro-algues, une seule fois dans sa vie.",
        "{ros.2}Les algues s'installent sous son épiderme et se multiplient. Pendant ce temps, le tube digestif du ver régresse. "
        "{ros.3}Chez l'adulte, il a complètement disparu. Le ver ne mange plus : il est devenu autotrophe. "
        "Ce sont les algues qui réalisent la photosynthèse, à la lumière du soleil, et qui partagent avec lui les nutriments produits.",
        "{ros.4}Ta prof précise que ces détails sont à lire, mais pas à noter. Ce qu'il faut noter, c'est ce que gagne chaque partenaire.",
        "{-ros}{gain_ros}{gain_ros.g}Les micro-algues gagnent un habitat, et une stabilité de leur environnement. "
        "{gain_ros.d}Le ver, lui, gagne la capacité photosynthétique des algues : il devient totalement autonome pour fabriquer sa matière carbonée, "
        "sans avoir besoin de consommer de matière organique venue de l'extérieur.",
        "{-gain_ros}{def_mut}Voici la phrase à retenir mot pour mot. "
        "{def_mut.1}On assiste à une association dont les deux partenaires tirent des bénéfices réciproques : on l'appelle une association mutualiste. "
        "{def_mut.2}Les deux partenaires sont devenus interdépendants : on appelle cela une symbiose.",
        "Et observe bien le point clé : le ver est devenu vert, autotrophe, sans tube digestif. Son phénotype a complètement changé. "
        "Pourtant, son génome n'a pas bougé. C'est l'association qui a tout fait.",
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
    dict(id="microbiote", chap="Le mutualisme : ton microbiote", fond="cellule", humeur="calme",
         retenir="Microbiote intestinal : les bactéries gagnent un habitat et une protection ; l'être humain digère des aliments sinon indigestes et voit son système immunitaire stimulé.",
         beats=[
        "{tab_bac}Deuxième exemple de mutualisme, et il te concerne directement : ton microbiote intestinal. "
        "Ton intestin abrite un très grand nombre de bactéries. Ensemble, elles forment le microbiote.",
        "{-tab_bac}{gain_bac}{gain_bac.g}Que gagnent les bactéries ? Un habitat, et une protection. "
        "{gain_bac.d}Et toi ? D'abord, la possibilité de digérer des aliments qui seraient sinon indigestes. "
        "Ensuite, une protection : le microbiote stimule ton système immunitaire.",
        "{-gain_bac}{obes}Le cours ajoute une remarque : le microbiote est aussi relié à l'obésité. "
        "Autrement dit, la composition de ces bactéries influence un caractère de ton phénotype, sans que tes gènes y soient pour rien.",
        "{-obes}{prem}Et fais le lien avec la Première. {prem.1}Tu y as vu une autre association à bénéfices réciproques : la mycorhize, "
        "où le champignon aide la plante à absorber les sels minéraux, et où la plante lui fournit des sucres. "
        "{prem.2}Le bilan du chapitre cite aussi les nodosités des racines. C'est la même logique : deux espèces différentes, deux bénéficiaires.",
        "{-prem}",
    ], vis={
        "tab_bac": dict(type="mot", t="Le microbiote", g="un très grand nombre de bactéries, dans ton intestin"),
        "gain_bac": dict(type="cols", g="Les bactéries", gq="un habitat ; une protection",
                         d="L'être humain", dq="digérer des aliments sinon indigestes ; un système immunitaire stimulé", vs="↔"),
        "obes": dict(type="note", titre="Remarque du cours", cles=["obésité", "phénotype"],
                     t="Le microbiote est aussi relié à l'obésité : des bactéries influencent un caractère du phénotype.", x=170, y=220, w=940),
        "prem": dict(type="liste", titre="Rappel de Première · même logique", items=[
            "La mycorhize : le champignon aide la plante à absorber les sels minéraux, la plante lui fournit des sucres",
            "Les nodosités des racines, citées dans le bilan du chapitre"], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ IV. le parasitisme : le gammare
    dict(id="parasitisme", chap="Le parasitisme : le gammare", fond="cellule", humeur="tension",
         retenir="Parasitisme : un seul partenaire, le parasite, tire bénéfice de l'association ; pour l'hôte, elle est néfaste. Le parasite du gammare change son comportement.",
         beats=[
        "{def_par}Deuxième sous-branche : le parasitisme. Voici la définition à noter. "
        "{def_par.1}Dans une association parasitaire, un seul des deux partenaires tire bénéfice de l'association ; pour l'autre, elle est néfaste.",
        "{-def_par}{tab_gam}L'exemple du cours, présenté comme à lire : les gammares. Ce sont de petits crustacés d'eau douce. "
        "Et ce sont des proies pour les oiseaux.",
        "{-tab_gam}{comp}Certains gammares sont infestés par des parasites, qui s'enkystent dans leur corps. "
        "{comp.1}Et là, les crustacés changent de comportement. Un gammare sain reste au fond, à l'abri. Le gammare parasité, lui, est attiré par la lumière. "
        "{comp.2}Il remonte à la surface, et il tournoie frénétiquement. "
        "{comp.3}Résultat : il devient une proie facile pour les oiseaux.",
        "Le parasite a modifié le comportement de son hôte. Et ce n'est pas un hasard : c'est ce qui lui permet de continuer son cycle.",
        "{-comp}{cyc}Voici ce cycle. Le parasite passe d'un hôte à l'autre. "
        "{cyc.1}Il se multiplie d'abord de façon asexuée chez un premier hôte intermédiaire. "
        "{cyc.2}Il vit ensuite sous forme de larves chez le gammare, le second hôte intermédiaire. "
        "{cyc.3}Et il atteint l'état adulte dans l'intestin de l'oiseau, l'hôte définitif, où il se reproduit sexuellement.",
        "{cyc.4}Pour boucler le cycle, ses œufs doivent retourner dans l'eau : cette précision ne vient pas de ton cours, "
        "qui ne nomme d'ailleurs ni le parasite, ni le premier hôte. Retiens le principe, pas les noms.",
        "{-cyc}{bil_par}Faisons le bilan des gains. {bil_par.1}Le parasite exploite les ressources de son partenaire, à son détriment. "
        "{bil_par.2}L'hôte lui offre un habitat, de la nourriture, {bil_par.3}et même un moyen efficace de dispersion : "
        "le gammare transporte le parasite jusqu'à l'oiseau.",
        "Le cours renvoie aussi à une vidéo qui présente l'exemple, de trois minutes vingt à six minutes trente.",
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
        "{sym}Voici le bilan de cette première branche, à noter. {sym.3}La symbiose désigne une association biologique étroite, intime et durable, "
        "entre deux ou plusieurs organismes d'espèces différentes. On en distingue deux formes. "
        "{sym.1}Le mutualisme : une interaction où les deux partenaires tirent un avantage réciproque, comme les bactéries du microbiote et l'être humain. "
        "{sym.2}Le parasitisme : une relation où l'un des partenaires, le parasite, profite au détriment de l'autre, l'hôte.",
        "{sym.4}Attention, piège. Ton cours emploie le mot symbiose dans deux sens. Au chapitre deux, avec les endosymbioses, et sur la diapositive du ver de Roscoff, "
        "la symbiose est une association à bénéfices réciproques où les partenaires sont devenus interdépendants. "
        "Dans le bilan de ce chapitre, c'est toute association étroite et durable, parasitisme compris.",
        "{-sym}{piege_sym}Les deux usages existent chez les scientifiques. Alors en devoir, dis dans quel sens tu l'emploies. "
        "Ou, plus simple : parle de mutualisme et de parasitisme. Là, aucune ambiguïté.",
        "{-piege_sym}{effets}Et maintenant, l'idée qui relie tout. {effets.1}Les associations symbiotiques de toutes sortes, nodosités, microbiote, parasitisme, "
        "contribuent à diversifier les métabolismes de certains êtres vivants, {effets.2}leurs comportements, {effets.3}et donc leur survie.",
        "{-effets}{conc_sym}Dans toutes ces situations, les caractéristiques de l'hôte sont modifiées sans que son génome ait changé. "
        "{conc_sym.1}La symbiose contribue donc bien à diversifier le phénotype des individus.",
        "Un approfondissement, maintenant, que ta prof présente pour ta culture générale, mais à ne pas retenir : il est hors programme. "
        "{-conc_sym}{hp1}{hp1.1}Les chercheurs distinguent plusieurs hérédités non génétiques. L'hérédité d'associations symbiotiques, quand les symbiotes sont transmis à la descendance. "
        "{hp1.2}L'hérédité épigénétique, quand une variation de l'expression des gènes, liée à l'environnement, est transmise. "
        "{hp1.3}L'hérédité écologique, quand les descendants héritent de l'habitat de leurs parents. "
        "{hp1.4}L'hérédité par effets parentaux, quand l'action des parents influe sur le phénotype des descendants. "
        "{hp1.5}Et l'hérédité culturelle, par la transmission sociale de comportements appris.",
        "{-hp1}{hp2}En deux mille dix, deux chercheurs, Pigliucci et Müller, ont proposé d'étendre la théorie de l'évolution, "
        "pour reconnaître dans ces processus un rôle moteur de l'évolution. Ce point de vue est loin d'être partagé par toute la communauté scientifique : "
        "il fait l'objet de vifs débats. Encore une fois : hors programme.",
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
        "{cm2}Deuxième branche de la carte : {cm2.1}le phénotype étendu. "
        "L'idée est simple : le phénotype d'un animal ne s'arrête pas aux limites de son corps. Le cours le montre par quatre exemples, en vidéo et en images.",
        "{-cm2}{tab_phr}Premier exemple : le fourreau de la larve de phrygane. La phrygane est un insecte, et sa larve vit dans l'eau.",
        "{-tab_phr}{phr}{phr.1}La larve se construit un fourreau de soie, à partir des sécrétions de ses glandes. "
        "{phr.2}Puis elle le recouvre d'éléments récoltés au fond de l'eau : des graviers, des débris. Ce fourreau la protège. "
        "{phr.3}Quand il devient trop petit, elle l'abandonne, et elle en construit un autre.",
        "Note au passage une coquille du diaporama : une diapositive écrit larve de pyrane. Il faut lire larve de phrygane, comme l'écrit la diapositive treize.",
        "{-phr}{tab_jar}Deuxième exemple : le nid du jardinier satiné, un oiseau d'Australie. "
        "Le mâle construit et décore une sorte de tonnelle, pour attirer les femelles. Sur la photo, il l'a entourée d'objets bleus. "
        "Ces précisions ne viennent pas de ton cours, qui montre l'oiseau en vidéo : retiens surtout qu'il s'agit d'une construction.",
        "{-tab_jar}{tab_ara}Troisième exemple : la toile et le cocon de l'araignée. Ils sont fabriqués par l'animal, avec sa soie, mais ils sont à l'extérieur de son corps.",
        "{-tab_ara}{tab_mar}Et quatrième exemple, le plus surprenant : le port de Marseille, construit par l'espèce humaine. "
        "Oui : nos constructions font aussi partie de notre phénotype étendu.",
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
        "{eten}Rassemblons ces exemples. Au centre, le corps de l'animal : sa forme, sa couleur, ses organes. C'est le phénotype au sens habituel. "
        "Mais autour, il y a tout ce qu'il construit. {eten.1}Le fourreau de la phrygane. {eten.2}La tonnelle du jardinier. "
        "{eten.3}La toile et le cocon de l'araignée. {eten.4}Le port des humains.",
        "{-eten}{def_pe}D'où la définition, à noter. {def_pe.1}Le phénotype étendu désigne tous les caractères d'un organisme qui se situent hors de son corps. "
        "Il s'agit principalement de son comportement, et de l'environnement qu'il construit : nid, terrier, relations sociales.",
        "{-def_pe}{rec}Le cours en tire trois idées. {rec.1}De nombreux animaux recrutent dans leur milieu des éléments non vivants, et modulent ainsi leur phénotype : "
        "nids d'oiseaux, toiles d'araignées, ruches. Et dans l'espèce humaine, les exemples sont innombrables. "
        "{rec.2}La prise de contrôle d'autres organismes élargit aussi le phénotype de certaines espèces. Tu connais déjà un exemple : "
        "le parasite qui modifie le comportement du gammare. Le comportement du gammare fait partie du phénotype étendu du parasite. "
        "{rec.3}Enfin, cet élargissement peut servir l'habitat, la survie, ou l'attrait du partenaire sexuel.",
        "{-rec}Le cours conclut : c'est un {!moteur évolutif}moteur évolutif non génétique.",
        "{hp_dk}Une précision hors programme : l'expression phénotype étendu vient du biologiste britannique Richard Dawkins, "
        "qui en a fait le titre d'un livre en mille neuf cent quatre-vingt-deux. Elle ne vient pas du diaporama.",
        "{-hp_dk}",
    ], vis={
        "eten": dict(type="illu", nom="c4_etendu", x=90, y=100, w=1100, h=540),
        "def_pe": dict(type="def", terme="Phénotype étendu", cles=["hors", "comportement", "construit"],
                       t="Tous les caractères d'un organisme qui se situent hors de son corps : principalement son comportement et l'environnement qu'il construit (nid, terrier, relations sociales…).",
                       x=150, y=190, w=980),
        "rec": dict(type="liste", titre="Trois idées du cours", items=[
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
        "{tab_mes}Un exemple à lire, pour voir jusqu'où va le phénotype étendu : les mésanges bleues, adeptes de l'aromathérapie.",
        "{-tab_mes}{mes}{mes.1}Chez les mésanges bleues, la femelle ajoute dans le nid des fragments frais de plantes aromatiques, glissés entre les matériaux. "
        "{mes.2}Et elle le fait chaque jour, depuis la fin de la construction du nid jusqu'à l'envol des jeunes.",
        "Cinq espèces se retrouvent dans plus d'un quart des nids suivis. {-mes}{plantes}{plantes.1}L'achillée de Ligurie. {plantes.2}La lavande papillon. "
        "{plantes.3}L'immortelle d'Italie. {plantes.4}La menthe à feuilles rondes. {plantes.5}Et la pulicaire odorante.",
        "{-plantes}{tab_lav}{terp}Pourquoi ces plantes ? {terp.1}Elles sont riches en terpènes, des molécules qui agissent comme insecticides, bactéricides et fongicides. "
        "{terp.2}La lavande, par exemple, dégage du bêta-pinène, un puissant répulsif des insectes. "
        "{terp.3}Et au Portugal, les mésanges ajoutent des aiguilles de pin parasol, riches en limonène, un composé connu pour réduire les puces et les poux.",
        "Le nid protège ainsi les oisillons des parasites. Le comportement de la mère, et le nid qu'elle construit, "
        "font partie de son phénotype étendu, et ils augmentent la survie de sa descendance.",
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
        "{cm3}Troisième et dernière branche : {cm3.1}les comportements. La diversification des individus peut reposer sur des caractères comportementaux, "
        "et pas seulement sur leur forme. On retrouve d'ailleurs le phénotype étendu. Cette branche a deux parties.",
        "{-cm3}{tab_ter}Première partie : des comportements qui dépendent des ressources du milieu. "
        "Le comportement des individus dépend des ressources dont ils disposent dans leur environnement. {res}Le cours cite quatre cas. "
        "{res.1}La construction des nids d'oiseaux. {res.2}Les termitières. {res.3}Les fourreaux des phryganes, faits avec les graviers et les débris disponibles. "
        "{res.4}Et le comportement reproducteur de certains oiseaux, comme le jardinier satiné.",
        "Le même animal, dans un milieu différent, construira donc autrement. Son génome est le même, son phénotype diffère.",
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
        "{idee_c}Deuxième partie : des comportements non héréditaires, transmis au sein d'une espèce. Voici l'idée, à noter. "
        "{idee_c.1}Certains comportements phénotypiques sont transmis, par voie non héréditaire, entre individus d'une même espèce. "
        "Cela conforte l'idée que le phénotype ne repose pas que sur des bases génétiques.",
        "{-idee_c}{tab_chi}Premier exemple : le chimpanzé, et la casse des noix.",
        "{-tab_chi}{noix}{noix.1}Le chimpanzé place une noix sur un support qui sert d'enclume, en bois ou en pierre. "
        "{noix.2}Puis il la frappe à l'aide d'un percuteur. Il recommence, encore et encore. {noix.3}Jusqu'à ce que la coque cède.",
        "{-noix}{cult}Et ce savoir-faire est ancien. {cult.1}Des percuteurs ont été retrouvés enfouis dans le sol. "
        "{cult.2}Le savoir-faire se transmet depuis plus de deux cents générations. "
        "{cult.3}Les chercheurs parlent d'une véritable culture, vieille de plus de quatre mille trois cents ans.",
        "Mais comment un jeune chimpanzé apprend-il ? C'est tout l'objet de l'exercice du cours. À toi de jouer.",
        "{-cult}",
    ], vis={
        "idee_c": dict(type="def", terme="L'idée à noter", cles=["non", "héréditaire", "génétiques"],
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
        "{ex1}Voici l'exercice du cours : l'acquisition de comportements chez le jeune chimpanzé. "
        "Le document est un graphique : le taux de succès du jeune chimpanzé en fonction de son âge, en mois, pour deux tâches.",
        "Une tâche facile : manger les fruits tendres de Parinari. Et une tâche compliquée : casser, avec un outil, les noix de Coula, très nourrissantes, mais très dures.",
        "{-ex1}{gr1}{gr1.1}Voici la première courbe : les fruits de Parinari. {gr1.2}Et la seconde : les noix de Coula. "
        "Ce graphique est redessiné d'après la description du cours : les valeurs sont approchées.",
        "{-gr1}{ex1b}Trois questions. Un : décrire le graphique. Deux : comparer les deux comportements. "
        "Trois : des jeunes chimpanzés élevés sans congénères ont un taux de succès de zéro virgule deux seulement. Qu'en conclure ?",
        "{-ex1b}{pa1}Prends une feuille. Mets la vidéo sur pause, et rédige tes trois réponses.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}{gr2}Correction. Question un : décrire. On décrit chaque courbe, avec des valeurs, et dans l'ordre. "
        "{gr2.1}Pour les fruits de Parinari, le taux de succès augmente dès l'âge de dix à quinze mois, {gr2.2}et il atteint un plateau d'environ zéro virgule six, vers trente mois.",
        "{gr2.3}Pour les noix de Coula, le taux de succès reste nul jusque vers quarante-cinq à cinquante mois. "
        "{gr2.4}Puis il augmente brusquement, jusqu'à un plateau d'environ zéro virgule cinquante-cinq, vers soixante mois.",
        "{ex1c.q2}{gr2.5}Question deux : comparer. Les deux comportements finissent par être maîtrisés à un niveau proche. "
        "Mais la casse des noix, plus complexe, et qui demande un outil, s'acquiert beaucoup plus tard : environ trois ans plus tard. "
        "Il faut donc un long apprentissage.",
        "{-gr2}{ex1c.q3}{rep3}{rep3.1}Question trois. Sans congénères à observer, le jeune chimpanzé n'atteint pas le niveau de ceux qui ont grandi dans le groupe. "
        "{rep3.2}Le comportement n'est donc pas inné : il s'acquiert par observation et imitation des adultes. "
        "{rep3.3}C'est une transmission culturelle, non génétique.",
        "Une précision honnête : sur la diapositive, l'énoncé de cette question est incomplet, et ta prof n'a pas encore donné de correction. "
        "Cette réponse est donc une proposition, mais c'est bien ce qu'on attend.",
        "{-rep3}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="L'acquisition de comportements chez le jeune chimpanzé", src="Exercice du cours",
                    enonce=["Le graphique donne le taux de succès du jeune chimpanzé en fonction de son âge (en mois), pour deux tâches.",
                            "Tâche facile : manger les fruits tendres de Parinari excelsa. Tâche compliquée : casser avec un outil les noix très nourrissantes, mais très dures, de Coula edulis."]),
        "gr1": dict(type="graphe", titre="Taux de succès selon l'âge", x=300, y=100, w=680, h=520, ax=AXES_CHIMP, el=[
            dict(type="courbe", pts=PARINARI, c="vert", lbl="fruits de Parinari", lp=[20, .72]),
            dict(type="courbe", pts=COULA, c="ca", lbl="noix de Coula", lp=[58, .7])]),
        "ex1b": dict(type="exo", niveau="simple", titre="Les questions", src="Exercice du cours",
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
        "{cul}Un texte à lire, sur la culture animale. {cul.1}Longtemps, la culture a été considérée comme propre à l'humanité. "
        "{cul.2}Depuis les années mille neuf cent quatre-vingt-dix, les spécialistes du comportement animal ont montré qu'une culture animale existe aussi. "
        "{cul.3}Apprentissage par imitation du langage, de techniques comme l'utilisation d'outils, élaboration de codes sociaux, "
        "{cul.4}et transmission entre congénères, avec des variantes selon les régions.",
        "{-cul}{def_cul}{def_cul.1}La culture concerne l'ensemble des animaux qui ont une organisation sociale. C'est l'ensemble des savoirs et des pratiques "
        "qui se partagent et se transmettent socialement au sein d'un groupe. Et cette transmission n'est pas un héritage génétique.",
        "{-def_cul}{tab_ois}Deuxième exemple du cours : le chant des oiseaux.",
        "Le cours le résume en une phrase : un oisillon isolé de tous ses congénères ne peut pas apprendre, et présente un chant très éloigné de celui de son espèce. "
        "{-tab_ois}{chant}Ce schéma te le montre, avec des sonogrammes simplifiés : le temps de gauche à droite, la hauteur du son de bas en haut. "
        "{chant.1}En haut, le chant d'un adulte de l'espèce. {chant.2}Au milieu, un jeune élevé avec ses congénères : après entraînement, il reproduit ce chant. "
        "{chant.3}En bas, un jeune élevé seul : son chant ne ressemble plus à celui de son espèce.",
        "{-chant}{bil_ch}Le bilan, à noter. {bil_ch.1}Ce comportement montre une démarche d'apprentissage. "
        "L'oisillon finit par maîtriser le chant de son espèce, par entraînement et par apprentissage. "
        "{bil_ch.2}Il s'agit d'une transmission non génétique d'un comportement, c'est-à-dire qu'il n'est pas inné.",
        "Profites-en pour fixer deux mots. {-bil_ch}{inne}{inne.g}Un comportement inné se met en place sans apprentissage. "
        "{inne.d}Un comportement acquis s'apprend, par observation et entraînement. Et le test, c'est l'isolement : un individu isolé n'acquiert pas un comportement qui s'apprend.",
        "{-inne}",
    ], vis={
        "cul": dict(type="liste", titre="À lire · la culture animale", items=[
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
        "Troisième exemple : {tab_bal}le chant des baleines à bosse du Pacifique. Chez cette espèce, seuls les mâles chantent, "
        "notamment pour séduire les femelles, lors des migrations de la saison des amours.",
        "{-tab_bal}{str}Un chant est très organisé. {str.1}Des unités sonores s'organisent en phrases, répétées. {str.2}Les phrases forment un thème. "
        "{str.3}Un chant compte de quatre à sept thèmes différents, repris dans un ordre précis, {str.4}pendant huit à trente minutes.",
        "{-str}{varie}Et ce chant n'est pas fixe. {varie.1}Il diffère selon la population, et selon le moment de l'année. {varie.2}Et des variations s'y accumulent.",
        "{-varie}{bal}Le manuel suit, de mille neuf cent quatre-vingt-dix-huit à deux mille huit, le type de chant de six populations, de l'Australie à la Polynésie française. "
        "{bal.1}Un nouveau chant apparaît d'abord chez les baleines d'Australie. "
        "{bal.2}Puis on le retrouve, un ou deux ans plus tard, chez les populations situées plus à l'est : la Nouvelle-Calédonie, les Tonga, les Samoa américaines, les îles Cook, la Polynésie.",
        "Un changement génétique ne pourrait jamais se propager aussi vite, d'une population à l'autre, en un an ou deux. "
        "Le chant se transmet donc d'une population à l'autre par apprentissage, et non par les gènes.",
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
        "{bil}Voici le bilan du chapitre, à noter. {bil.1}Certains comportements se transmettent de manière non génétique entre congénères, "
        "par observation et apprentissage : le chant et l'alimentation des oiseaux, l'alimentation des macaques.",
        "{bil.2}Lorsqu'on isole des individus de leurs proches, on constate que le langage adulte ne se met pas en place, ou qu'il est incomplet : il n'est donc pas inné. "
        "Petite coquille du diaporama, au passage : il écrit isoler des individus de leur roche. Il faut lire : de leurs proches.",
        "{bil.3}Cela contribue à la diversification des individus, car les sources des apprentissages varient, notamment dans les sociétés humaines, "
        "où les échanges entre populations se sont accentués. "
        "{bil.4}Et selon leurs conséquences, ces comportements ont pu se maintenir ou non dans les populations : "
        "ils ont ainsi contribué à l'évolution technique et culturelle des espèces.",
        "{-bil}{frappe_m}La conclusion du chapitre : la transmission culturelle et comportementale est donc, elle aussi, un moteur évolutif.",
        "{-frappe_m}{tab_mac}Et ces macaques du bilan ? Le diaporama les cite sans document. Alors voici l'exemple classique, "
        "qui vient des manuels et de la littérature scientifique, pas de ton diaporama : {mac}{mac.1}les macaques japonais de l'île de Koshima. "
        "{mac.2}Dans les années mille neuf cent cinquante, une jeune femelle s'est mise à laver dans l'eau les patates douces que lui donnaient les chercheurs. "
        "{mac.3}Le comportement s'est ensuite répandu dans le groupe, d'abord chez les jeunes, puis de génération en génération.",
        "C'est exactement le même mécanisme que pour les chimpanzés et les oiseaux : un comportement nouveau, appris, transmis, sans aucun gène nouveau.",
        "{-mac}{-tab_mac}",
    ], vis={
        "bil": dict(type="liste", titre="Bilan du chapitre · à noter", petit=True, items=[
            "Des comportements se transmettent entre congénères, par observation et apprentissage (oiseaux, macaques)",
            "Isolé de ses proches, l'individu n'acquiert pas le langage adulte : il n'est pas inné",
            "Les sources d'apprentissage varient : diversification des individus",
            "Maintenus ou non selon leurs conséquences : évolution technique et culturelle"], marques=["1", "2", "3", "4"], x=150, y=120, w=980),
        "frappe_m": dict(type="mot", t="Un moteur évolutif", g="la transmission culturelle et comportementale"),
        "tab_mac": dict(type="tableau", img="ch4-macaque", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Un macaque japonais · Justin, iNaturalist, CC BY"),
        "mac": dict(type="liste", titre="Exemple extérieur au diaporama · les macaques de Koshima", items=[
            "Des macaques japonais, sur l'île de Koshima",
            "Années 1950 : une jeune femelle lave les patates douces dans l'eau",
            "Le comportement se répand : d'abord les jeunes, puis de génération en génération"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ XV. exercice 2 : la rédaction type bac
    dict(id="exo2", chap="Exercice · une rédaction type bac", fond="nuit", humeur="tension", beats=[
        "{ex2}Dernier exercice, au format du bac : une question de synthèse, qu'on appelle aussi restitution des connaissances. C'est l'exercice de rédaction du site. "
        "Montrer, à l'aide d'exemples précis, que le phénotype des êtres vivants peut se diversifier sans modification de leur génome. "
        "Avec une introduction, un développement structuré, et une conclusion. Comptez trente minutes.",
        "{-ex2}{pa2}C'est le moment de vérité. Mets sur pause, fais d'abord un plan au brouillon, puis rédige.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. Voici une proposition, construite à partir du diaporama. "
        "{intro}{intro.1}L'introduction pose le décor : la diversité des phénotypes s'explique en grande partie par des mécanismes génétiques, "
        "brassages de la reproduction sexuée, mutations, transferts de gènes. {intro.2}Pourtant, d'autres mécanismes diversifient le phénotype sans toucher à l'ADN. "
        "{intro.3}Lesquels ? C'est la problématique.",
        "{-intro}{ex2c.q2}{dev}Le développement suit les trois branches du cours. {dev.1}Première partie : les associations entre êtres vivants. "
        "Le ver de Roscoff et ses algues, le microbiote et l'être humain, pour le mutualisme ; le gammare parasité, pour le parasitisme. "
        "Et l'idée clé : le métabolisme ou le comportement de l'hôte changent, mais pas son génome.",
        "{dev.2}Une phrase de transition : le phénotype ne s'arrête pas non plus aux limites du corps. "
        "{dev.3}Deuxième partie : le phénotype étendu. Sa définition, puis les exemples : la phrygane, l'araignée, les mésanges et leurs plantes aromatiques, le port de Marseille. "
        "{dev.4}Troisième partie : les comportements appris. Le jeune chimpanzé qui ne maîtrise la casse des noix que vers quarante-cinq à soixante mois, "
        "l'oisillon isolé qui chante autrement, et le nouveau chant des baleines qui passe d'une population à l'autre en un ou deux ans.",
        "{-dev}{ex2c.q3}{concl}{concl.1}Et la conclusion répond à la question : associations, phénotype étendu et apprentissage diversifient les phénotypes "
        "sans modifier les génomes. {concl.2}Puis elle ouvre : selon leurs conséquences, ces caractères se maintiennent ou non dans les populations. "
        "La transmission culturelle et comportementale est donc, elle aussi, un moteur évolutif.",
        "{-concl}{grille}Vérifie ta copie avec la grille du site, en douze points. {grille.1}La problématique. {grille.2}Les trois exemples de mutualisme et de parasitisme, "
        "et l'idée clé. {grille.3}Une transition. {grille.4}La définition du phénotype étendu, et ses exemples. "
        "{grille.5}Le chimpanzé, l'oisillon isolé, les baleines. {grille.6}Et la conclusion sur le moteur évolutif. "
        "Chaque exemple doit être précis : un nom, un chiffre, un mécanisme. C'est ça qui fait la note.",
        "{-grille}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", titre="Une diversité qui ne vient pas des gènes", src="Exercice de rédaction du site (30 min)",
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
        "grille": dict(type="liste", titre="La grille du site · à cocher", petit=True, items=[
            "Problématique : une diversité sans modification du génome",
            "Roscoff, microbiote, gammare, et l'idée clé",
            "Une phrase de transition",
            "Définition et exemples du phénotype étendu",
            "Chimpanzé, chant des oiseaux, baleines à bosse",
            "Conclusion : un moteur évolutif"], marques=["✓"] * 6, x=540, y=90, w=700),
    }),

    # ================================================================ XVI. pour le bac
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, l'idée : le phénotype se diversifie sans que le génome change. "
        "{carte.1}Le mutualisme : des bénéfices réciproques, avec le ver de Roscoff et le microbiote. "
        "{carte.2}Le parasitisme : un seul bénéficiaire, avec le gammare. "
        "{carte.3}Le phénotype étendu : ce qui est hors du corps, de la phrygane au port de Marseille, sans oublier les mésanges. "
        "{carte.4}Et les comportements appris : chimpanzés, oiseaux, baleines, macaques.",
        "{-carte}{pieges}Quatre pièges à éviter. {pieges.1}Ne jamais écrire que le génome de l'hôte change : c'est tout le contraire du chapitre. "
        "{pieges.2}Préciser le sens du mot symbiose, ou parler de mutualisme et de parasitisme. "
        "{pieges.3}Ne pas confondre inné et acquis : l'expérience d'isolement fait la différence. "
        "{pieges.4}Et toujours un exemple précis derrière chaque idée.",
        "{-pieges}Voici ce que tu dois savoir faire, {bac}à cocher. {bac.1}Définir l'hérédité non génétique. {bac.2}Définir le mutualisme et le parasitisme, avec un exemple chacun. "
        "{bac.3}Définir la symbiose, en précisant le sens. {bac.4}Définir le phénotype étendu, avec des exemples. "
        "{bac.5}Décrire et exploiter un graphique d'apprentissage, comme celui du chimpanzé. "
        "{bac.6}Expliquer pourquoi un comportement n'est pas inné. {bac.7}Et rédiger une synthèse sur la diversité non génétique.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre. Le site t'attend avec le vocabulaire, le quiz et la rédaction corrigée.",
        "{-bac}{cm4}Et voici la carte complète de la partie A du thème un. {cm4.1}Ce chapitre quatre la referme : "
        "après les mécanismes génétiques, il montre que le vivant se diversifie et évolue aussi sans ses gènes. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
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
    "est redessiné d'après la description du cours (valeurs approchées), les sonogrammes et la carte des baleines sont schématiques.",
]
