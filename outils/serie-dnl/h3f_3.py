"""Histoire · « La Seconde Guerre mondiale » — édition française de la série vidéo, épisode 3 : « Le Royaume-Uni seul »
(partie I.2 du cours, « La résistance britannique soutenue par les États-Unis »).

Traduction et adaptation de h3_3.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
plus de mention de la DNL ni de l'anglais d'examen ; Worksheet 2 → « le dossier documentaire » ; le DBQ devient une
analyse de document (présenter, situer, expliquer, intérêt et limites). Mêmes scènes, mêmes visuels, mêmes repères.
Chaîne : outils/serie-philo/generer.py h3f_3 ; sortie dans dnl/serie/ (code h3f-3) ; la carte animée passe d'elle-même
en français (sc = numéros de scènes de la carte, voir h3_3.py).
Citations : Churchill (4 juin 1940) en traduction française courante ; de Gaulle (18 juin 1940), texte original.
Hors cours, dit comme tel : la loi prêt-bail (mars 1941), l'opération Otarie (Seelöwe), la bataille d'Angleterre.
La consigne d'analyse et son modèle sont écrits pour la vidéo et dits comme tels.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-3"
NOTION = "La Seconde Guerre mondiale"
NUM = 3
TITRE = "Le Royaume-Uni seul"
SUIVANT = "Épisode 4 · Barbarossa : une guerre d'anéantissement"
PRONONCIATION = {"Jodl": "Yodeul", "Luftwaffe": "Louft-vaffe", "Wehrmacht": "Vèr-markt", "Churchill": "Tcheur-tchil",
                 "Chamberlain": "Tchèm-beur-line", "Neville": "Nèvil", "Hyde Park": "Haïde-Parc", "East End": "Ist-Ènde",
                 "Roosevelt": "Rouz-vèlt", "Pearl Harbor": "Peurl-Arbeur", "Erie Daily Times": "Iri-Dé-li-Taïmz",
                 "cash and carry": "kache-ènde-kari", "Royal Navy": "Royal-Névi", "Royal Air Force": "Royal-Èr-Force"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False,
         retenir="La question de cet épisode : comment le Royaume-Uni a-t-il pu tenir seul face à l'Allemagne nazie, de juin 1940 à décembre 1941 ?",
         beats=[
        "{g0}{q1}Juin 1940. En six semaines, la France est tombée. La Norvège, le Danemark, les Pays-Bas et la Belgique sont occupés. "
        "À l'ouest, un seul ennemi de Hitler est encore debout : le Royaume-Uni.",
        "{-q1}{q2}Tout le monde s'attend à ce qu'il négocie, ou qu'il soit envahi. Il ne fait ni l'un ni l'autre. "
        "Comment une île a-t-elle pu tenir seule face à la machine de guerre nazie, pendant un an et demi ?",
        "{-q2}{-g0}{plan}Voici le plan de cet épisode. {plan.1}D'abord, le récit sur la carte, de Dunkerque à Pearl Harbor. "
        "{plan.2}Puis le cours, idée par idée : les deux stratégies de Jodl, le Blitz, et pourquoi le Royaume-Uni a tenu. "
        "{plan.3}Puis deux hommes qui refusent la défaite, Churchill et de Gaulle, et le dossier documentaire qui les compare. "
        "{plan.4}Puis l'Amérique, l'arsenal de la démocratie, et décembre 1941, quand la guerre devient mondiale. "
        "{plan.5}Et pour finir, un atelier d'épreuve : l'analyse du discours de Churchill.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[17]),
        "q1": dict(type="question", t="Juin 1940 : le Royaume-Uni est seul.", bande=True),
        "q2": dict(type="question", t="Comment une île a-t-elle pu tenir ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 3 · Le Royaume-Uni seul", items=[
            "Sur la carte : de Dunkerque à Pearl Harbor", "Les deux stratégies de Jodl, le Blitz, pourquoi le Royaume-Uni a tenu",
            "Churchill, de Gaulle et le dossier documentaire", "L'arsenal de la démocratie, décembre 1941",
            "À l'épreuve : une analyse de document"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 3", t="Le Royaume-Uni seul",
                      sous="1940 – 1941 · la résistance britannique, soutenue par les États-Unis"),
    }),

    # ================================================================ I. sur la carte : l'été 1940
    dict(id="ete40", chap="L'été 1940, sur la carte", fond="nuit", humeur="tension",
         retenir="Avril 1940 la Norvège · 10 mai Churchill Premier ministre · 26 mai – 4 juin Dunkerque : 338 000 évacués · 18 juin l'appel du général de Gaulle · 22 juin l'armistice : le Royaume-Uni est seul.",
         beats=[
        "{g1}{g1.1}Avril 1940. À l'ouest, c'est encore la drôle de guerre, mais l'Allemagne occupe le Danemark et envahit la Norvège. "
        "Le Royaume-Uni ne parvient pas à l'empêcher. À Londres, le Premier ministre Neville Chamberlain perd le soutien de la Chambre des communes.",
        "{g1.2}Le dix mai 1940, l'offensive allemande à l'ouest commence, à travers les Pays-Bas, la Belgique et le Luxembourg. "
        "Le même jour, Chamberlain démissionne, et Winston Churchill devient Premier ministre.",
        "{g1.3}Fin mai, l'armée britannique est acculée à la mer, à Dunkerque. C'est l'opération Dynamo : "
        "du vingt-six mai au quatre juin, trois cent trente-huit mille soldats alliés sont évacués par la mer vers l'Angleterre. "
        "L'armée est sauvée, et la Royal Navy comme la RAF sont intactes. Le quatre juin, Churchill le dit aux Communes : nous ne nous rendrons jamais.",
        "{-g1}{g2}{g2.1}Le dix-huit juin. Le maréchal Pétain, devenu chef du gouvernement, a demandé l'armistice. "
        "Depuis Londres, un général presque inconnu, Charles de Gaulle, parle à la radio de la BBC : la flamme de la résistance française ne doit pas s'éteindre.",
        "{g2.2}Le vingt-deux juin, l'armistice est signé à Rethondes. La France est découpée, les trois cinquièmes de son territoire sont occupés. C'était l'épisode deux.",
        "{g2.3}Et maintenant, regarde la carte. De la Norvège aux Pyrénées, les côtes qui font face au Royaume-Uni sont aux mains des Allemands. "
        "La Wehrmacht est juste de l'autre côté de la Manche. {!Le Royaume-Uni est seul}Le Royaume-Uni est seul.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[10, 11, 13]),
        "g2": dict(type="globe", code="H3", sc=[15, 16, 17]),
    }),

    # ================================================================ II. sur la carte : du Blitz à Pearl Harbor
    dict(id="blitz41", chap="Du Blitz à Pearl Harbor", fond="nuit", humeur="tension",
         retenir="7 sept. 1940 le Blitz · déc. 1940 l'invasion reportée sans date · les États-Unis, arsenal de la démocratie · 22 juin 1941 Barbarossa · 7 déc. 1941 Pearl Harbor · 11 déc. l'Allemagne et l'Italie en guerre contre les États-Unis.",
         beats=[
        "{g3}{g3.1}Le sept septembre 1940, la Luftwaffe, l'aviation allemande, commence ses raids du soir sur Londres. "
        "C'est le Blitz. Les docks, les usines et des rues entières de l'East End brûlent.",
        "{g3.2}Mais l'aviation allemande ne gagne jamais la maîtrise du ciel. En décembre 1940, l'invasion du Royaume-Uni est reportée sans date : "
        "Hitler s'est tourné vers l'Est. Et de l'autre côté de l'Atlantique, les États-Unis, encore neutres, deviennent le fournisseur du Royaume-Uni : "
        "l'arsenal de la démocratie.",
        "{-g3}{g4}{g4.1}Le vingt-deux juin 1941, l'Allemagne envahit l'Union soviétique. C'est l'opération Barbarossa. "
        "Le Royaume-Uni n'est plus le seul pays à combattre l'Allemagne.",
        "{g4.2}Le sept décembre 1941, le Japon bombarde la base américaine de Pearl Harbor, à Hawaï. "
        "{g4.3}Quatre jours plus tard, l'Allemagne et l'Italie déclarent la guerre aux États-Unis. La guerre est désormais mondiale, et le Royaume-Uni n'est plus seul.",
        "{-g4}{fr1}Dix-huit mois en huit dates. Note-les. {fr1.1}Le dix mai 1940, Churchill devient Premier ministre. "
        "{fr1.2}Fin mai, Dunkerque. {fr1.3}Le dix-huit juin, l'appel du général de Gaulle. {fr1.4}Le vingt-deux juin, l'armistice. "
        "{fr1.5}Le sept septembre, le Blitz. {fr1.6}Décembre 1940, l'invasion reportée. "
        "{fr1.7}Le vingt-deux juin 1941, Barbarossa. {fr1.8}Et le sept décembre 1941, Pearl Harbor.",
        ("P", 2.5),
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[20, 21]),
        "g4": dict(type="globe", code="H3", sc=[25, 31, 33]),
        "fr1": dict(type="frise", items=[
            dict(nom="Churchill", d=1940, q="10 mai : Premier ministre"), dict(nom="Dunkerque", d=1940, q="26 mai – 4 juin"),
            dict(nom="De Gaulle", d=1940, q="18 juin : l'appel"), dict(nom="Armistice", d=1940, q="22 juin"),
            dict(nom="Le Blitz", d=1940, q="7 sept. : Londres"), dict(nom="Invasion", d=1940, q="déc. : reportée"),
            dict(nom="Barbarossa", d=1941, q="22 juin"), dict(nom="Pearl Harbor", d=1941, q="7 déc."),
        ]),
    }),

    # ================================================================ III. idée 1 : les deux stratégies de Jodl
    dict(id="jodl", chap="Le choix de Jodl : deux stratégies", fond="guerre", humeur="tension",
         retenir="Jodl, juin 1940 : une attaque directe (offensive aérienne et navale + bombardement de l'industrie, bombardements de terreur sur les villes, un débarquement) ou une guerre périphérique (la Méditerranée, les routes commerciales).",
         beats=[
        "{q3}Passons au cours, idée par idée. La France est vaincue. Comment vaincre le Royaume-Uni ?",
        "{-q3}{jo}En juin 1940, Alfred Jodl, chef de l'état-major des opérations des forces armées allemandes, expose le choix dans un mémorandum. "
        "Deux stratégies. Soit, selon ses mots, une attaque directe contre la métropole anglaise. "
        "{jo.1}Soit une extension de la guerre aux zones périphériques : la Méditerranée et les routes commerciales, pour étrangler le Royaume-Uni de l'extérieur.",
        "{-jo}{dir}L'attaque directe pouvait elle-même prendre trois formes. {dir.1}Un : une offensive aérienne et navale contre la marine marchande britannique, "
        "combinée à des attaques aériennes sur les centres industriels. {dir.2}Deux : des attaques aériennes de terreur contre les centres de population, c'est-à-dire les villes. "
        "{dir.3}Et trois, en dernier : un débarquement, pour occuper l'Angleterre. Remarque l'ordre. Le débarquement vient en dernier : {!d'abord, le ciel}d'abord, le ciel.",
        "{-dir}{g5}{g5.1}Et regarde ce qui s'est passé. La deuxième forme, la terreur venue du ciel, est exactement celle que les Allemands ont mise en pratique. "
        "{g5.2}Une photographie du cours montre un bombardier de la Luftwaffe au-dessus de l'East End de Londres, au début des raids du soir "
        "du sept septembre 1940. C'est le Blitz.",
    ], vis={
        "q3": dict(type="question", t="La France est vaincue. Comment vaincre le Royaume-Uni ?"),
        "jo": dict(type="cols", g="Directe", gq="« une attaque directe contre la métropole anglaise »", d="Périphérique",
                   dq="« une extension de la guerre aux zones périphériques » : Méditerranée, routes commerciales", vs="ou",
                   repere="Mémorandum d'Alfred Jodl, juin 1940"),
        "dir": dict(type="liste", titre="Une attaque directe : trois formes", cles=["marine", "terreur", "débarquement"], items=[
            "Offensive aérienne et navale contre la marine marchande britannique + attaques aériennes sur l'industrie",
            "Attaques aériennes de terreur contre les centres de population", "En dernier, un débarquement pour occuper l'Angleterre"], x=170, y=140, w=940),
        "g5": dict(type="globe", code="H3", sc=[17, 20]),
    }),

    # ================================================================ IV. idée 2 : le Blitz
    dict(id="blitz", chap="Le Blitz", fond="guerre", humeur="tension",
         retenir="Le Blitz (1940-1941) : vaincre d'abord la RAF, puis briser l'industrie (docks, usines) et la volonté de la population (villes). Environ 43 000 civils tués au Royaume-Uni.",
         beats=[
        "{ph}{def3}Une notion clé de cette leçon : le {!Blitz}Blitz. La campagne de bombardements allemands contre le Royaume-Uni, en 1940 et 1941. "
        "{def3.1}Son but : faire plier le Royaume-Uni sous les bombes.",
        "{-def3}{lo}Suis la logique allemande. {lo.1}Une invasion suppose de vaincre d'abord l'aviation britannique, la Royal Air Force, la RAF. "
        "{lo.2}La guerre aérienne passe donc en premier. {lo.3}Les bombardiers frappent les docks et les usines, pour briser l'industrie britannique. "
        "{lo.4}Et surtout les villes, pour briser la volonté de la population.",
        "{-lo}{civ}Les civils sont donc en première ligne, comme ils l'avaient été en Espagne, pendant la guerre civile, et en Pologne, en 1939. "
        "{civ.1}Regarde ces enfants de l'est de Londres, assis devant ce qui était leur maison. Dans cette guerre, le foyer est un champ de bataille.",
        "{-civ}{hp}Une autre photographie du cours : des canons antiaériens installés à Hyde Park, au cœur de la capitale. "
        "La ligne de front passe au milieu de Londres.",
        "{-hp}{chif}Et le bilan. Le cours donne quarante-trois mille civils tués à Londres. "
        "{chif.1}Attention : ce chiffre est d'ordinaire celui de tout le Royaume-Uni pendant le Blitz, et environ la moitié des victimes sont mortes à Londres. "
        "Dans ta copie, écris : environ quarante-trois mille civils tués au Royaume-Uni.",
        "{-chif}{-ph}",
    ], vis={
        "ph": dict(type="tableau", img="h3-blitz", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .62],
                   legende="Enfants d'une banlieue est de Londres, sans abri après un raid nocturne, septembre 1940 · New Times Paris Bureau Collection (USIA), US National Archives 306-NT-3163V, domaine public"),
        "def3": dict(type="def", cles=["bombardements", "1940", "1941"], terme="Notion clé · le Blitz",
                     t="La campagne de bombardements allemands contre le Royaume-Uni, en 1940 et 1941.",
                     etape="But : faire plier le Royaume-Uni sous les bombes", x=170, y=200, w=940),
        "lo": dict(type="liste", titre="La logique allemande", cles=["RAF", "aérienne", "industrie", "volonté"], items=[
            "Une invasion suppose de vaincre la RAF", "La guerre aérienne passe donc en premier",
            "Docks et usines → briser l'industrie britannique", "Surtout les villes → briser la volonté de la population"],
                   x=170, y=140, w=940),
        "civ": dict(type="note", terme="Les civils en première ligne", cles=["Espagne", "Pologne"],
                    t="Comme en Espagne et en Pologne, les bombardiers visent la population elle-même.",
                    etape="Est de Londres, 1940 : le foyer est un champ de bataille", x=170, y=340, w=940),
        "hp": dict(type="note", terme="Une photographie du cours", cles=["Hyde", "Park"],
                   t="Des canons antiaériens installés à Hyde Park, au cœur de la capitale.",
                   etape="La ligne de front passe par Londres", x=170, y=200, w=940),
        "chif": dict(type="note", terme="Attention · un chiffre à vérifier", cles=["civils", "Londres"],
                     t="Le cours : 43 000 civils tués à Londres pendant le Blitz.",
                     etape="D'ordinaire, le chiffre de tout le Royaume-Uni, dont environ la moitié à Londres. Écris : « au Royaume-Uni ».", x=170, y=200, w=940),
    }),

    # ================================================================ V. idée 3 : pourquoi le Royaume-Uni tient
    dict(id="tenir", chap="Pourquoi le Royaume-Uni a tenu", fond="nuit", humeur="lumiere",
         retenir="Pas de maîtrise du ciel au-dessus du sud-est de l'Angleterre, pas de débarquement. Déc. 1940 : premier ordre d'invasion de l'URSS, invasion du Royaume-Uni reportée sans date. Le Royaume-Uni a arrêté la machine nazie en tenant.",
         beats=[
        "{g6}{ch1}La troisième idée répond à notre question. {ch1.1}Une invasion dépendait de la supériorité aérienne, la maîtrise du ciel, "
        "au-dessus du sud-est de l'Angleterre, là où devait avoir lieu le débarquement. {ch1.2}L'aviation allemande n'a pas réussi à l'obtenir en 1940. "
        "{ch1.3}Hitler a donc reporté l'invasion, d'abord au printemps 1941. "
        "{ch1.4}Puis, en décembre 1940, le premier ordre opérationnel pour l'invasion de l'Union soviétique a été donné, "
        "et l'invasion du Royaume-Uni a été reportée sans date. L'Allemagne avait tourné ses forces vers l'Est.",
        "{-ch1}{-g6}{hold}Le Royaume-Uni a donc été le premier pays à arrêter la machine de guerre nazie. Pas en la battant. {!En tenant}En tenant. "
        "C'est une phrase forte pour une copie : le Royaume-Uni n'a pas gagné en 1940, mais il n'a pas perdu, et cela a suffi à changer le cours de la guerre.",
        "{-hold}{hors}Deux noms que tu trouveras dans les livres, même s'ils ne sont pas dans le cours. {hors.1}Le plan d'invasion s'appelait l'opération Otarie, "
        "et la bataille aérienne de l'été 1940 est connue sous le nom de bataille d'Angleterre. "
        "Tu peux les employer, mais les mots du cours suffisent : la supériorité aérienne, la Luftwaffe, la RAF.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[21]),
        "ch1": dict(type="liste", titre="Pourquoi il n'y a pas eu d'invasion", bande=True, petit=True, x=60, y=130, w=620,
                    cles=["supériorité", "réussi", "printemps", "date"], items=[
                        "Un débarquement exige la supériorité aérienne sur le sud-est de l'Angleterre", "1940 : la Luftwaffe n'a pas réussi à l'obtenir",
                        "Invasion reportée au printemps 1941", "Déc. 1940 : premier ordre d'invasion de l'URSS ; invasion reportée sans date"]),
        "hold": dict(type="mot", t="Pas en la battant : en tenant", g="Le Royaume-Uni n'a pas gagné en 1940, mais il n'a pas perdu — assez pour changer la guerre", y=250, taille=72),
        "hors": dict(type="note", terme="Hors du cours", cles=["Otarie", "bataille", "Angleterre"],
                     t="Le plan d'invasion : l'opération Otarie. La bataille aérienne de l'été 1940 : la bataille d'Angleterre.",
                     etape="Des noms utiles, mais les mots du cours suffisent : supériorité aérienne, Luftwaffe, RAF.", x=170, y=200, w=940),
    }),

    # ================================================================ VI. idée 4 : deux hommes refusent la défaite
    dict(id="hommes", chap="Deux hommes refusent la défaite", fond="nuit", humeur="tension",
         retenir="Churchill : un conservateur hostile à l'apaisement, Premier ministre le 10 mai 1940. De Gaulle : général tout juste promu, membre du gouvernement Reynaud, refuse l'armistice de Pétain, quitte la France pour Londres le 17 juin.",
         beats=[
        "{pwc}{wc}Quatrième idée : en juin 1940, deux hommes refusent la défaite. D'abord Churchill. "
        "{wc.1}C'est déjà une grande figure du parti conservateur, et il s'était opposé à l'apaisement, la politique qui consistait à céder à Hitler. "
        "{wc.2}En avril 1940, pendant la drôle de guerre, le Royaume-Uni ne parvient pas à empêcher l'occupation allemande de la Norvège. "
        "{wc.3}Chamberlain perd le soutien de la Chambre des communes et, quand les troupes allemandes envahissent la Belgique, il démissionne. "
        "{wc.4}Le dix mai 1940, le jour même où commence l'offensive allemande à l'ouest, Churchill devient Premier ministre.",
        "{-wc}{-pwc}{dg}Maintenant, de Gaulle. {dg.1}Il vient d'être promu général, et nommé dans le gouvernement de Paul Reynaud. "
        "{dg.2}Mais Reynaud démissionne, et le maréchal Pétain, héros de la Première Guerre mondiale, devient chef du gouvernement en promettant de signer un armistice. "
        "{dg.3}De Gaulle refuse. Le dix-sept juin, il quitte la France pour échapper à l'arrestation, "
        "{dg.4}et à Londres, il rencontre Churchill. Le lendemain, il parle à la BBC.",
        "{-dg}{cmp1}Deux hommes, deux positions très différentes en juin 1940. {cmp1.1}L'un gouverne un pays qui se bat encore. "
        "L'autre est un rebelle, presque seul, dont le propre gouvernement a renoncé. Garde ce contraste en tête : c'est la clé du dossier documentaire.",
    ], vis={
        "pwc": dict(type="tableau", img="h3-churchill", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .28],
                    legende="Winston Churchill, Ottawa, décembre 1941, par Yousuf Karsh (Bibliothèque et Archives Canada, Wikimedia Commons, CC BY 2.0)"),
        "wc": dict(type="liste", titre="Winston Churchill", cles=["apaisement", "Norvège", "communes", "Premier"], items=[
            "Un grand conservateur, hostile à l'apaisement", "Avril 1940 : le Royaume-Uni ne peut empêcher l'occupation de la Norvège",
            "Chamberlain perd les Communes ; la Belgique envahie : il démissionne", "10 mai 1940 : Premier ministre, le jour de l'attaque à l'ouest"],
                   x=150, y=130, w=980),
        "dg": dict(type="liste", titre="Charles de Gaulle", cles=["général", "Pétain", "refuse", "Churchill"], items=[
            "Général tout juste promu, dans le gouvernement de Paul Reynaud", "Reynaud démissionne ; Pétain, héros de 14-18, promet un armistice",
            "Il refuse, et quitte la France le 17 juin pour échapper à l'arrestation", "À Londres, il rencontre Churchill"], x=150, y=130, w=980),
        "cmp1": dict(type="cols", g="Churchill", gq="Chef du gouvernement d'un pays qui se bat encore", d="De Gaulle",
                     dq="Un général rebelle, presque seul : son gouvernement a renoncé", vs="≠"),
    }),

    # ================================================================ VII. le dossier documentaire : les deux documents
    dict(id="docs", chap="Le dossier documentaire : deux discours", fond="guerre", humeur="tension",
         retenir="Doc. B, Churchill, 4 juin 1940, Communes : « nous ne nous rendrons jamais ». Doc. A, de Gaulle, 18 juin 1940, BBC : « la flamme de la résistance française ne doit pas s'éteindre et ne s'éteindra pas ».",
         beats=[
        "{ws}Le dossier documentaire met leurs deux discours côte à côte. La consigne : comparer leurs attitudes face à l'Axe. "
        "{ws.1}Comparer, c'est relever les ressemblances et les différences, en parlant des deux hommes tout du long, côte à côte.",
        "{-ws}{docb}D'abord le document B, parce qu'il vient en premier dans le temps. {docb.1}Le quatre juin 1940, devant la Chambre des communes, "
        "à la fin de l'évacuation de Dunkerque. {docb.2}Churchill est confiant : le Royaume-Uni défendra son île, s'il le faut pendant des années, s'il le faut seul. "
        "{docb.3}L'Empire britannique et la République française défendront leur sol jusqu'à la mort. "
        "{docb.4}Et si l'île tombait, l'Empire et la flotte poursuivraient la lutte. Viennent alors les lignes les plus célèbres.",
        "{-docb}",
        ("C", "nous nous battrons sur les plages … nous ne nous rendrons jamais", "c_wc"),
        "{-c_wc}{doca}Le document A. {doca.1}Le dix-huit juin 1940, à la radio de la BBC, depuis Londres : le lendemain du jour où Pétain a demandé l'armistice. "
        "{doca.2}Pour de Gaulle, la défaite vient des chars, des avions et de la tactique des Allemands, bien plus que de leur nombre. "
        "{doca.3}La France n'est pas seule : elle a son empire, l'Empire britannique qui tient la mer, et l'industrie des États-Unis. "
        "C'est une guerre mondiale. {doca.4}Il appelle donc les officiers, les soldats, les ingénieurs et les ouvriers français qui se trouvent en territoire britannique "
        "à se mettre en rapport avec lui. Et il conclut :",
        "{-doca}",
        ("C", "Quoi qu'il arrive, la flamme de la résistance française ne doit pas s'éteindre et ne s'éteindra pas.", "c_dg"),
        "{-c_dg}",
    ], vis={
        "ws": dict(type="def", cles=["comparez", "ressemblances", "différences"], terme="Le dossier documentaire · la consigne",
                   t="De Gaulle et Churchill : comparez leurs attitudes face à l'Axe, ressemblances et différences.",
                   etape="Les deux hommes tout du long, côte à côte", x=170, y=200, w=940),
        "docb": dict(type="liste", titre="Document B · Churchill, « nous ne nous rendrons jamais »", items=[
            "4 juin 1940 · Chambre des communes · fin de l'évacuation de Dunkerque", "« s'il le faut pendant des années, s'il le faut seuls »",
            "L'Empire britannique et la République française défendront leur sol jusqu'à la mort",
            "Si l'île tombait, l'Empire et la flotte poursuivraient la lutte"], x=150, y=130, w=980),
        "c_wc": dict(type="cit", a="Winston Churchill", o="Chambre des communes, 4 juin 1940 (traduction française)", x=200, y=200, w=880),
        "doca": dict(type="liste", titre="Document A · De Gaulle, l'appel du 18 juin 1940", items=[
            "Radio de la BBC, Londres · le lendemain de la demande d'armistice de Pétain", "La défaite vient des chars, des avions, de la tactique des Allemands",
            "« la France n'est pas seule » : l'empire, la flotte britannique, l'industrie américaine",
            "Un appel aux officiers, soldats, ingénieurs et ouvriers en territoire britannique"], x=150, y=130, w=980),
        "c_dg": dict(type="cit", a="Charles de Gaulle", o="Appel du 18 juin 1940, BBC", x=200, y=200, w=880),
    }),

    # ================================================================ VIII. idée 5 : comparer
    dict(id="comparer", chap="Comparer les deux discours", fond="nuit", humeur="lumiere",
         retenir="Ressemblances : la bataille de France ne décide pas de la guerre ; tous deux comptent sur les empires, la flotte britannique et l'industrie américaine. Différences : qui, quand, à qui, pour quoi.",
         beats=[
        "{com}Cinquième idée : les deux discours partagent une même analyse. {!une guerre mondiale}La bataille de France ne décide pas de la guerre. "
        "{com.1}Tous deux comptent sur des empires restés intacts. {com.2}Tous deux comptent sur la flotte britannique, qui tient la mer. "
        "{com.3}Et tous deux comptent sur les ressources industrielles des États-Unis. Écoute-les. De Gaulle d'abord.",
        "{-com}",
        ("C", "Elle peut, comme l'Angleterre, utiliser sans limites l'immense industrie des États-Unis. … Cette guerre est une guerre mondiale.", "c_dg2"),
        "{-c_dg2}Et Churchill.",
        ("C", "notre Empire au-delà des mers … poursuivrait la lutte jusqu'à ce que, à l'heure choisie par Dieu, le Nouveau Monde, "
              "avec toute sa force et toute sa puissance, s'avance pour secourir et libérer l'Ancien.", "c_wc2"),
        "{-c_wc2}{dif}Les différences sont tout aussi nettes. Utilise les quatre questions du dossier. "
        "{dif.1}Qui ? Churchill est Premier ministre, une grande figure de son parti ; de Gaulle, un général tout juste promu, presque inconnu, en exil. "
        "{dif.2}Quand ? Churchill parle le quatre juin, avant l'armistice ; de Gaulle le dix-huit, après que son propre gouvernement l'a demandé. "
        "{dif.3}À qui ? Churchill s'adresse au Parlement, et à travers lui à une nation unie ; de Gaulle, à des individus qu'il doit rallier. "
        "{dif.4}Pour quoi ? Churchill prépare son pays à se battre seul ; de Gaulle refuse l'armistice voulu par son propre gouvernement.",
        "{-dif}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}On peut le construire ainsi. {rep1.1}Premier paragraphe, les ressemblances : tous deux refusent la défaite, et tous deux voient une guerre mondiale, "
        "gagnée grâce aux empires, à la flotte et aux États-Unis. {rep1.2}Deuxième paragraphe, les différences : l'auteur, la date, le destinataire, le but. "
        "{rep1.3}Et dans chaque paragraphe, cite les deux hommes, côte à côte. "
        "{rep1.4}Une dernière phrase pour conclure : deux discours, un même pari, celui que le Royaume-Uni tiendrait jusqu'à l'entrée en guerre de l'Amérique. "
        "Décembre 1941 leur a donné raison.",
    ], vis={
        "com": dict(type="liste", titre="Ce que les deux discours partagent", cles=["empires", "flotte", "États-Unis"], items=[
            "Des empires restés intacts", "La flotte britannique, qui tient la mer", "Les ressources industrielles des États-Unis"],
                    x=170, y=150, w=940),
        "c_dg2": dict(type="cit", a="Charles de Gaulle", o="Appel du 18 juin 1940", x=200, y=170, w=880),
        "c_wc2": dict(type="cit", a="Winston Churchill", o="Chambre des communes, 4 juin 1940 (traduction française)", x=200, y=150, w=880),
        "dif": dict(type="liste", titre="Les différences (dossier documentaire)", cles=["Qui", "Quand"], items=[
            "Qui ? Un Premier ministre ≠ un général presque inconnu, en exil",
            "Quand ? Le 4 juin, avant l'armistice ≠ le 18 juin, après la demande",
            "À qui ? Le Parlement et une nation unie ≠ des individus à rallier",
            "Pour quoi ? Se battre seul ≠ refuser l'armistice de son gouvernement"], x=120, y=130, w=1040),
        "pa1": dict(type="pause", t="Prépare un plan en deux paragraphes pour comparer les deux discours.",
                    sous="Mets la vidéo en pause, écris ton plan, puis relance pour comparer."),
        "rep1": dict(type="liste", titre="Un plan modèle", items=[
            "Ressemblances : refus de la défaite, guerre mondiale, empires, flotte, États-Unis", "Différences : auteur, date, destinataire, but",
            "Citer les deux hommes dans chaque paragraphe", "Conclure : un même pari, gagné en décembre 1941"], x=170, y=140, w=940),
    }),

    # ================================================================ IX. idée 6 : l'arsenal de la démocratie
    dict(id="arsenal", chap="L'arsenal de la démocratie", fond="nuit", humeur="lumiere",
         retenir="Lois de neutralité (1935-1937) → cash and carry étendu aux armes (nov. 1939) → l'arsenal de la démocratie → prêt-bail (mars 1941, hors du cours). Les usines américaines ont travaillé pour le Royaume-Uni bien avant que les soldats américains ne combattent.",
         beats=[
        "{g7}{g7.1}Sixième idée. Le titre de la leçon le dit : la résistance britannique, soutenue par les États-Unis. Mais en 1940, les États-Unis sont neutres, de par la loi. "
        "Souviens-toi du chapitre un : les lois de neutralité. En 1935, un embargo sur les armes pour les pays en guerre. En 1936, l'interdiction de leur prêter de l'argent. "
        "En 1937, l'embargo sur les armes devient permanent, les Américains n'ont plus le droit de voyager sur les navires des pays en guerre, "
        "et les autres marchandises ne leur sont vendues qu'au comptant, emportées sur leurs propres navires : c'est le cash and carry.",
        "{g7.2}Puis, en novembre 1939, une fois la guerre commencée, Roosevelt obtient une nouvelle loi de neutralité : l'embargo sur les armes est levé, "
        "et le cash and carry s'applique désormais aux armes. "
        "Les démocraties peuvent acheter des armes américaines, si elles paient comptant et les emportent sur leurs propres navires. "
        "La formule favorise celui qui contrôle la mer : le Royaume-Uni et la France, puis, après juin 1940, le Royaume-Uni seul.",
        "{-g7}{ars}Roosevelt présente alors son pays comme {!l'arsenal de la démocratie}l'arsenal de la démocratie. "
        "Le Royaume-Uni a pu tenir parce que les usines américaines travaillaient pour lui bien avant que les soldats américains ne combattent.",
        "{ars.1}Un exemple hors du cours, mais très utile : la loi prêt-bail, de mars 1941. "
        "Les États-Unis peuvent désormais prêter ou louer du matériel de guerre au Royaume-Uni, sans paiement immédiat. C'est la fin du cash and carry.",
        "{-ars}{et3}Pas à pas, l'Amérique se rapproche donc du Royaume-Uni. {et3.1}De 1935 à 1937 : la neutralité, par la loi. "
        "{et3.2}Novembre 1939 : le cash and carry, pour les armes aussi. "
        "{et3.3}Puis l'arsenal de la démocratie. {et3.4}Mars 1941 : le prêt-bail, hors du cours. "
        "{et3.5}Et décembre 1941 : les États-Unis entrent en guerre.",
    ], vis={
        "g7": dict(type="globe", code="H1", sc=[26, 32]),
        "ars": dict(type="def", cles=["usines", "soldats"], terme="L'arsenal de la démocratie",
                    t="Le Royaume-Uni a pu tenir parce que les usines américaines travaillaient pour lui bien avant que les soldats américains ne combattent.",
                    etape="Hors du cours : la loi prêt-bail, mars 1941 — sans paiement immédiat", x=170, y=200, w=940),
        "et3": dict(type="liste", titre="Pas à pas vers le Royaume-Uni", items=[
            "1935-1937 : les lois de neutralité", "Nov. 1939 : le cash and carry pour les armes", "L'« arsenal de la démocratie »",
            "Mars 1941 : le prêt-bail (hors du cours)", "Déc. 1941 : les États-Unis en guerre"], x=170, y=120, w=940),
    }),

    # ================================================================ X. idée 7 : décembre 1941
    dict(id="mondiale", chap="Décembre 1941 : la guerre devient mondiale", fond="nuit", humeur="tension",
         retenir="Juin 1941 Barbarossa, arrêtée devant Moscou en décembre · 7 déc. 1941 Pearl Harbor · 11 déc. l'Allemagne et l'Italie déclarent la guerre aux États-Unis : la guerre est mondiale, le Royaume-Uni n'est plus seul.",
         beats=[
        "{g8}{g8.1}Septième et dernière idée. Après avoir conquis la France, l'armée allemande s'est tournée vers l'est, contre l'Union soviétique, en juin 1941, "
        "{g8.2}jusqu'à être brutalement arrêtée devant Moscou, en décembre 1941. Ce sera l'épisode quatre.",
        "{g8.3}Le même mois, le sept décembre 1941, le Japon, l'une des puissances de l'Axe, bombarde la base américaine de Pearl Harbor, à Hawaï. "
        "Les États-Unis déclarent aussitôt la guerre au Japon.",
        "{g8.4}Et le onze décembre, l'Allemagne et l'Italie déclarent la guerre aux États-Unis. "
        "Désormais, on se bat sur tous les océans et sur tous les continents.",
        "{-g8}{une}Un document du cours montre la une d'un journal américain, l'Erie Daily Times, le onze décembre 1941. Deux titres. "
        "{une.1}Les États-Unis déclarent la guerre à l'Allemagne et à l'Italie. {une.2}Et en dessous : l'Amérique se range aux côtés de la Grande-Bretagne "
        "et des Soviétiques contre l'Axe, dans la lutte mondiale.",
        "{-une}{bil2}Retiens ces mots : aux côtés de la Grande-Bretagne. Dix-huit mois après Dunkerque, {!plus seul}le Royaume-Uni n'est plus seul. "
        "{bil2.1}Le pari de Churchill et du général de Gaulle est gagné : le Nouveau Monde s'est avancé.",
    ], vis={
        "g8": dict(type="globe", code="H3", sc=[26, 30, 31, 33]),
        "une": dict(type="liste", titre="The Erie Daily Times, 11 décembre 1941 (traduction)", items=[
            "« Les États-Unis déclarent la guerre à l'Allemagne et à l'Italie »",
            "« L'Amérique se range aux côtés de la Grande-Bretagne et des Soviétiques contre l'Axe dans la lutte mondiale »"], x=150, y=200, w=980),
        "bil2": dict(type="note", terme="Le Royaume-Uni n'est plus seul", cles=["pari", "Nouveau", "Monde"],
                     t="Décembre 1941 : la guerre devient mondiale ; le pari de Churchill et de De Gaulle est gagné, le Nouveau Monde s'avance.",
                     etape="« le Nouveau Monde … s'avance pour secourir et libérer l'Ancien »", x=170, y=200, w=940),
    }),

    # ================================================================ XI. à l'épreuve : une analyse de document
    dict(id="dbq", chap="À l'épreuve : une analyse de document", fond="aube", humeur="calme",
         retenir="Analyse de document : présenter (nature, auteur, date, destinataire) · situer · expliquer · intérêt (le chef du gouvernement, la date, la stratégie) et limites (un discours pour le moral, juin 1940, des États-Unis encore neutres, un seul point de vue).",
         beats=[
        "{dq}Une consigne d'analyse, écrite pour cette vidéo. Montre en quoi le discours de Churchill du quatre juin 1940 "
        "permet de comprendre pourquoi le Royaume-Uni continue la guerre en 1940, et quelles en sont les limites.",
        "{-dq}{st}Rappelle-toi la démarche de l'analyse. {st.1}Présenter le document : sa nature, son auteur, sa date, son destinataire. "
        "{st.2}Le situer dans son contexte. {st.3}L'expliquer, idée par idée, en citant le texte. "
        "{st.4}Et en montrer l'intérêt et les limites : c'est le bilan critique.",
        "{-st}{pa2}",
        ("P", 2.0),
        "{-pa2}{m1}Voici un modèle. {m1.1}La présentation : ce document est un discours de Winston Churchill, Premier ministre, "
        "prononcé devant la Chambre des communes le quatre juin 1940, à la fin de l'évacuation de Dunkerque. "
        "{m1.2}Le bilan, que tu annonces dès l'introduction : ce discours éclaire bien pourquoi le Royaume-Uni continue la guerre, "
        "mais il ne suffit pas, à lui seul, à expliquer comment le pays a tenu.",
        "{-m1}{fo}L'intérêt. {fo.1}Le discours vient du chef du gouvernement lui-même : il montre la volonté officielle de continuer le combat, "
        "s'il le faut pendant des années, s'il le faut seul. {fo.2}Sa date compte : il est prononcé avant l'armistice, pendant l'effondrement de la France ; "
        "le choix de se battre est donc fait tout de suite. {fo.3}Et il révèle la stratégie : l'Empire, la flotte, "
        "et l'espoir que le Nouveau Monde vienne au secours de l'Ancien. L'appel du général de Gaulle fait la même analyse, ce qui la confirme.",
        "{-fo}{li}Les limites. {li.1}C'est un discours public, destiné à soutenir le moral : il montre une détermination, pas la situation militaire réelle. "
        "{li.2}Il date de juin : il ne peut pas montrer ce qui a vraiment sauvé le Royaume-Uni ensuite, l'échec de la Luftwaffe à gagner la maîtrise du ciel. "
        "{li.3}Il espère l'aide américaine, mais en 1940, les États-Unis sont encore neutres, et ne vendent des armes que par le cash and carry. "
        "{li.4}Enfin, il ne donne qu'un point de vue, celui du gouvernement britannique : confronte-le à un autre document, comme la photographie du Blitz.",
    ], vis={
        "dq": dict(type="question", t="Montrez en quoi le discours de Churchill du 4 juin 1940 explique que le Royaume-Uni continue la guerre, et quelles en sont les limites."),
        "st": dict(type="liste", titre="L'analyse de document · la démarche", items=[
            "Présenter : nature, auteur, date, destinataire",
            "Situer le document dans son contexte", "Expliquer, idée par idée, en citant le texte",
            "Intérêt et limites : le bilan critique"], x=150, y=140, w=980),
        "pa2": dict(type="pause", t="Analyse le discours de Churchill du 4 juin 1940 : présentation, contexte, intérêt et limites.",
                    sous="Mets la vidéo en pause, suis la démarche, puis relance pour voir un modèle."),
        "m1": dict(type="liste", titre="Un modèle (écrit pour la vidéo)", items=[
            "Discours de Churchill, Premier ministre, Chambre des communes, 4 juin 1940, fin de Dunkerque",
            "« Il éclaire bien pourquoi le Royaume-Uni continue la guerre… mais pas, à lui seul, comment le pays a tenu. »"], x=150, y=170, w=980),
        "fo": dict(type="liste", titre="Intérêt", marques=["+", "+", "+"], items=[
            "Le chef du gouvernement : la volonté officielle, « s'il le faut seuls »",
            "4 juin, avant l'armistice : le choix de se battre est fait tout de suite",
            "La stratégie : l'Empire, la flotte, le Nouveau Monde (confirmée par de Gaulle)"], x=150, y=150, w=980),
        "li": dict(type="liste", titre="Limites", marques=["−", "−", "−", "−"], items=[
            "Un discours public pour le moral, pas la situation militaire",
            "Juin 1940 : ne peut montrer l'échec de la Luftwaffe dans le ciel",
            "Espère l'aide américaine, mais les États-Unis sont encore neutres (cash and carry)",
            "Un seul point de vue : le confronter à un autre document"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Récapitulons. {carte.1}En juin 1940, Jodl hésite entre une attaque directe et une guerre périphérique ; "
        "le Blitz bombarde les villes britanniques, et environ quarante-trois mille civils sont tués. "
        "{carte.2}Le Royaume-Uni tient parce que la Luftwaffe ne gagne jamais la maîtrise du ciel : en décembre 1940, l'invasion est reportée sans date. "
        "{carte.3}Deux hommes refusent la défaite, Churchill le quatre juin et de Gaulle le dix-huit, et tous deux parient sur une guerre mondiale. "
        "{carte.4}Et l'Amérique arme le Royaume-Uni, du cash and carry à l'arsenal de la démocratie, jusqu'en décembre 1941, quand la guerre devient mondiale.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : Barbarossa. Le vingt-deux juin 1941, l'Allemagne envahit l'Union soviétique, "
        "et une guerre d'anéantissement commence à l'Est.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LE ROYAUME-UNI SEUL", branches=[
            dict(t="L'attaque allemande", items=["Jodl : directe ou périphérique", "7 sept. 1940 : le Blitz", "≈ 43 000 civils (R.-U.)"]),
            dict(t="Pourquoi il a tenu", items=["pas de maîtrise du ciel", "déc. 1940 : invasion reportée", "Hitler se tourne vers l'Est"]),
            dict(t="Deux hommes", items=["Churchill, 4 juin 1940", "de Gaulle, 18 juin 1940", "le pari d'une guerre mondiale"]),
            dict(t="L'Amérique", items=["1939 : cash and carry (armes)", "l'arsenal de la démocratie", "déc. 1941 : guerre mondiale"])]),
        "fin": dict(type="mot", t="À suivre : Barbarossa", g="Épisode 4 · une guerre d'anéantissement", y=270, taille=76),
    }),
]

QUIZ = [
    dict(q="Dans son mémorandum de juin 1940, quel choix Jodl expose-t-il face au Royaume-Uni ?",
         r=["Une attaque directe contre l'Angleterre, ou une guerre à la périphérie", "Une alliance avec le Royaume-Uni, ou une guerre contre l'URSS",
            "D'abord un débarquement, puis des attaques aériennes", "Un blocus naval des États-Unis"], ok=0, voir="jo",
         ex="Directe : offensive aérienne et navale, bombardements de terreur, débarquement. Périphérique : la Méditerranée et les routes commerciales."),
    dict(q="Pourquoi les Allemands font-ils de la guerre aérienne la première étape ?",
         r=["Toute invasion supposait de vaincre la RAF", "Leur armée de terre était trop faible pour combattre",
            "La Royal Navy avait été détruite à Dunkerque", "Les États-Unis avaient interdit un débarquement"], ok=0, voir="lo",
         ex="Sans maîtrise du ciel au-dessus du sud-est de l'Angleterre, pas de débarquement : les bombardiers frappent d'abord."),
    dict(q="Le cours donne 43 000 civils tués pendant le Blitz. Que faut-il écrire dans une copie ?",
         r=["Environ 43 000 civils tués au Royaume-Uni", "43 000 civils tués à Londres seulement",
            "43 000 pilotes de la RAF tués", "43 000 aviateurs allemands abattus"], ok=0, voir="chif",
         ex="Le chiffre est d'ordinaire celui de tout le Royaume-Uni, dont environ la moitié des victimes à Londres."),
    dict(q="Pourquoi l'invasion du Royaume-Uni est-elle reportée sans date en décembre 1940 ?",
         r=["La Luftwaffe a échoué et l'Allemagne tourne ses forces contre l'URSS", "Le Royaume-Uni a signé un armistice",
            "Les États-Unis ont déclaré la guerre à l'Allemagne", "L'Italie refuse d'y participer"], ok=0, voir="ch1",
         ex="Décembre 1940 : le premier ordre opérationnel pour l'invasion de l'URSS."),
    dict(q="Quand Churchill devient-il Premier ministre ?",
         r=["Le 10 mai 1940", "Le 4 juin 1940", "Le 18 juin 1940", "Le 3 septembre 1939"], ok=0, voir="wc",
         ex="Le jour où commence l'offensive allemande à l'ouest ; Chamberlain avait perdu le soutien des Communes."),
    dict(q="Laquelle est une DIFFÉRENCE entre les discours de Churchill et de De Gaulle ?",
         r=["Churchill parle avant l'armistice, de Gaulle après que son gouvernement l'a demandé",
            "Seul Churchill compte sur les États-Unis", "Seul de Gaulle croit à une guerre mondiale",
            "Tous deux parlent devant la Chambre des communes"], ok=0, voir="dif",
         ex="Tous deux comptent sur les empires, la flotte et l'industrie américaine ; leur position, la date, le destinataire et le but diffèrent."),
    dict(q="Que permet la loi de neutralité de novembre 1939, le « cash and carry » pour les armes ?",
         r=["Les démocraties peuvent acheter des armes américaines si elles paient comptant et les emportent sur leurs navires",
            "Les États-Unis peuvent prêter des armes sans paiement", "Des soldats américains peuvent combattre en Europe",
            "L'Allemagne peut acheter du pétrole américain"], ok=0, voir="g7",
         ex="Prêter sans paiement immédiat, c'est le prêt-bail, en mars 1941 (hors du cours)."),
    dict(q="Que se passe-t-il le 11 décembre 1941 ?",
         r=["L'Allemagne et l'Italie déclarent la guerre aux États-Unis", "Le Japon bombarde Pearl Harbor",
            "L'Allemagne envahit l'URSS", "Le Blitz commence"], ok=0, voir="une",
         ex="Pearl Harbor, c'est le 7 décembre ; l'Erie Daily Times titre : l'Amérique se range aux côtés de la Grande-Bretagne et des Soviétiques contre l'Axe."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre « La Seconde Guerre mondiale » (partie I.2, « La résistance britannique soutenue "
    "par les États-Unis »), et le dossier documentaire qui compare les discours de Churchill et de De Gaulle, tels qu'ils sont présentés sur le site "
    "(les réponses du dossier sont proposées par le site, ce n'est pas un corrigé officiel) ; rappels du chapitre 1 ; cartes animées des chapitres 1 et 3 (site). "
    "Hors du cours : la loi prêt-bail, l'opération Otarie, la bataille d'Angleterre. La consigne d'analyse et le modèle ont été écrits pour cette vidéo.",
    "Citations : Winston Churchill, discours du 4 juin 1940 à la Chambre des communes, en traduction française ; Charles de Gaulle, "
    "appel du 18 juin 1940, texte original ; titres de l'Erie Daily Times du 11 décembre 1941, traduits.",
    "Photographie : enfants d'une banlieue est de Londres, sans abri après un raid nocturne, septembre 1940 (New Times Paris Bureau Collection, USIA ; "
    "US National Archives, 306-NT-3163V ; domaine public selon sa source ; fichier Wikimedia Commons « WWII London Blitz East London.jpg », "
    "indiqué sous CC BY-SA 2.0 via pingnews.com sur Flickr).",
    "Photographie : Winston Churchill, Ottawa, décembre 1941, par Yousuf Karsh (Bibliothèque et Archives Canada, Wikimedia Commons, CC BY 2.0).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
