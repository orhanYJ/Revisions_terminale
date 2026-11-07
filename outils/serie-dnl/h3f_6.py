"""Histoire · H3 « La Seconde Guerre mondiale » — édition française, épisode 6 : « La Seconde Guerre mondiale à l'examen ».

Adaptation (et non simple traduction) de h3_6.py, d'après outils/serie-dnl/EDITION_FR.md : l'épisode présente les deux
exercices de l'histoire-géographie de Terminale, la réponse à une question problématisée (analyse du sujet, introduction
avec problématique et plan, paragraphes argument + exemple précis, conclusion) et l'analyse de document(s) (consigne,
présentation, contexte, explication, intérêt et limites, bilan critique), sur les mêmes sujets et documents du chapitre que
l'épisode anglais (ordre de sévérité de Reichenau, 10 octobre 1941 ; discours de Staline, 6 novembre 1941), avec les mêmes
pauses « À toi ». La scène de l'oral (propre à l'édition anglaise) est retirée ; une introduction modèle est ajoutée.
Les sujets, consignes et copies modèles sont écrits pour la vidéo et dits comme tels. Aucun barème.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-6"
NOTION = "La Seconde Guerre mondiale"
NUM = 6
TITRE = "La Seconde Guerre mondiale à l'examen"
SUIVANT = "Épisode 7 · Récap"
PRONONCIATION = {"Reichenau": "Raï-che-naou", "Untermenschen": "Ountère-mènchen", "Reichsmarks": "Raïchs-marks",
                 "Panzerdivision": "Panntsère-division", "Einsatzgruppen": "Aïne-zats-groupen"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="aube", humeur="lumiere", carton=False, beats=[
        "{q1}Tu connais le chapitre. Mais sais-tu t'en servir ? Le jour de l'épreuve, personne ne te demandera de raconter la guerre. "
        "Il faudra expliquer, argumenter, analyser des documents.",
        "{-q1}{plan}Cet épisode est donc un atelier. {plan.1}D'abord, les deux exercices de l'histoire-géographie. "
        "{plan.2}Puis la réponse à une question problématisée : les paragraphes, l'introduction et la conclusion, avec des modèles. "
        "{plan.3}Puis l'analyse de documents, sur deux documents du cours. {plan.4}Et enfin, les pièges de ce chapitre : "
        "les erreurs qui coûtent des points.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "q1": dict(type="question", t="Tu connais le chapitre. Sais-tu t'en servir ?"),
        "plan": dict(type="liste", titre="Cet épisode, un atelier", items=[
            "Les deux exercices", "La question problématisée : paragraphes, introduction, conclusion",
            "L'analyse de document(s) : présenter, expliquer, critiquer", "Les pièges du chapitre"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 6", t="La Seconde Guerre mondiale à l'examen",
                      sous="question problématisée · analyse de document(s) · les pièges du chapitre"),
    }),

    # ================================================================ I. les deux exercices
    dict(id="format", chap="Les deux exercices", fond="nuit", humeur="calme",
         retenir="Deux exercices : la réponse à une question problématisée et l'analyse de document(s). Souvent dans un même devoir : l'un en histoire, l'autre en géographie.",
         beats=[
        "{fmt}En histoire-géographie, en Terminale, tu rencontres deux grands exercices. {fmt.1}La réponse à une question problématisée : "
        "un texte organisé, qui répond à une question précise. {fmt.2}L'analyse de document(s) : présenter un ou deux documents, "
        "les expliquer, les critiquer. {fmt.3}Dans un même devoir, ils sont souvent associés : l'un porte sur l'histoire, l'autre sur la géographie. "
        "Si le devoir dure deux heures, compte environ une heure pour chacun.",
        "{-fmt}{ess}D'abord, la question problématisée. {ess.1}Au brouillon, analyse le sujet : définis chaque mot, repère les bornes, "
        "dans le temps et dans l'espace, et demande-toi quel problème pose la question. {ess.2}Ensuite, l'introduction : tu présentes le sujet, "
        "tu poses la problématique, et tu annonces ton plan. {ess.3}Puis le développement, en parties : chaque paragraphe porte un argument "
        "et un exemple précis. Et la conclusion répond clairement à la question.",
        "{-ess}{dbq}Ensuite, l'analyse de document(s). Tout part de la consigne : elle te dit quoi chercher. "
        "{dbq.1}Tu présentes chaque document, et tu le situes dans son contexte. {dbq.2}Puis tu l'expliques avec tes connaissances, "
        "et tu montres son intérêt et ses limites.",
        "{-dbq}Voyons tout cela sur des sujets du chapitre.",
    ], vis={
        "fmt": dict(type="liste", titre="Histoire-géographie · deux exercices", items=[
            "La réponse à une question problématisée", "L'analyse de document(s)",
            "Souvent dans un même devoir : l'un en histoire, l'autre en géographie"], x=170, y=140, w=940),
        "ess": dict(type="liste", titre="La question problématisée", cles=["problématique", "plan", "exemple"], items=[
            "Analyser le sujet : les mots, les bornes, le problème posé", "Introduction : le sujet, la problématique, le plan",
            "Paragraphes : un argument + un exemple précis ; conclusion : la réponse"], x=170, y=140, w=940),
        "dbq": dict(type="liste", titre="L'analyse de document(s)", items=[
            "Présenter et situer : nature, auteur, date, destinataire, contexte",
            "Expliquer et critiquer : connaissances, intérêt, limites"], x=170, y=160, w=940),
    }),

    # ================================================================ II. les paragraphes
    dict(id="explain", chap="Question problématisée · les paragraphes", fond="nuit", humeur="tension",
         retenir="Pourquoi la France est-elle vaincue si vite en 1940 ? Une stratégie défensive dépassée · la surprise des Ardennes · la guerre éclair. Un argument = un paragraphe : argument, exemple précis, explication, lien.",
         beats=[
        "{ex1}Voici un sujet, écrit pour cette vidéo. {!Pourquoi}Pourquoi la France est-elle vaincue si rapidement en 1940 ?",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{rais}Trois arguments, tirés de l'épisode deux. {rais.1}Un : une stratégie défensive dépassée. La France a la ligne Maginot, "
        "et elle attend derrière pendant la drôle de guerre. {rais.2}Deux : la surprise des Ardennes. La principale attaque allemande passe par la forêt, "
        "là où personne ne l'attend, entre le treize et le vingt mai 1940. "
        "{rais.3}Trois : la guerre éclair. Chars et avions agissent ensemble, comme la septième Panzerdivision de Rommel, qui fonce jusqu'à la Somme.",
        "{-rais}{peel}Chaque argument devient un paragraphe, construit en quatre temps. {peel.1}L'argument : l'idée, en une phrase. "
        "{peel.2}L'exemple précis : une date, un chiffre, un nom. {peel.3}L'explication : pourquoi cela a causé la défaite. "
        "{peel.4}Et le lien avec la question.",
        "{-peel}{mod1}Écoute un paragraphe modèle, pour le premier argument.",
        "La France est d'abord vaincue parce que sa stratégie militaire est dépassée. Marqués par la guerre de 1914 à 1918, ses chefs ont construit "
        "la ligne Maginot le long de la frontière allemande, et ils attendent derrière elle : de septembre 1939 à mai 1940, pendant la drôle de guerre, "
        "on ne se bat presque pas à l'Ouest. Mais la ligne ne couvre pas la frontière belge, et une armée tournée vers la défense ne sait pas réagir "
        "à une guerre de mouvement. Cette stratégie d'un autre temps laisse la France incapable d'arrêter une offensive rapide : "
        "voilà ce qui explique son effondrement en six semaines.",
        "{-mod1}Argument, exemple, explication, lien. Fais de même pour les Ardennes et pour la guerre éclair, et ton développement est prêt.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Pourquoi la France est-elle vaincue si rapidement en 1940 ?",
                    src="Sujet écrit pour cette vidéo", enonce=["Réponse à une question problématisée · un paragraphe par argument"]),
        "pa1": dict(type="pause", t="Trouve trois arguments, chacun avec un exemple précis.",
                    sous="Mets la vidéo en pause, écris tes trois arguments, puis relance."),
        "rais": dict(type="liste", titre="Trois arguments", items=[
            "Une stratégie défensive dépassée → ligne Maginot, drôle de guerre", "La surprise des Ardennes → 13-20 mai 1940",
            "La guerre éclair → chars + avions, 7e Panzerdivision de Rommel"], x=170, y=140, w=940),
        "peel": dict(type="liste", titre="Un argument = un paragraphe", cles=["argument", "exemple", "explication", "lien"], items=[
            "Argument : l'idée en une phrase", "Exemple précis : une date, un chiffre, un nom",
            "Explication : pourquoi cela a causé la défaite", "Lien : retour à la question"], x=170, y=140, w=940),
        "mod1": dict(type="note", terme="Paragraphe modèle · argument 1", cles=["parce que", "Maginot", "explique"],
                     t="La France est d'abord vaincue parce que sa stratégie est dépassée : la ligne Maginot, la drôle de guerre (sept. 1939 – mai 1940), "
                       "une frontière belge non couverte… Cela explique un effondrement en six semaines.",
                     etape="Argument · exemple · explication · lien", x=150, y=170, w=980),
    }),

    # ================================================================ III. introduction et conclusion
    dict(id="assess", chap="Question problématisée · introduction et conclusion", fond="nuit", humeur="tension",
         retenir="Dans quelle mesure le nouvel ordre européen est-il avant tout un ordre racial ? Pour : génocide, Lebensraum, « Untermenschen ». Contre : exploitation économique, anticommunisme, guerre totale. Réponse : la race est le principe qui organise tout.",
         beats=[
        "{ex2}Maintenant, un sujet plus large, lui aussi écrit pour cette vidéo. "
        "{!Dans quelle mesure}Dans quelle mesure le nouvel ordre européen est-il avant tout un ordre racial ?",
        "{-ex2}{gd}Au brouillon, cherche les deux côtés. {gd.1}Pour : l'ordre racial. Six millions de Juifs assassinés ; les Slaves traités "
        "en Untermenschen, en sous-hommes ; et les mots de Hitler, le onze décembre 1941, tels que le cours les cite : l'élimination absolue des Juifs. "
        "{gd.2}Contre : l'ordre est aussi économique et militaire. La France paie vingt millions de Reichsmarks par jour ; l'Est doit nourrir l'Allemagne "
        "avec le blé d'Ukraine et le pétrole du Caucase ; et la guerre à l'Est est aussi une croisade contre le communisme.",
        "{-gd}{jug}Vient alors l'essentiel : prendre position, et construire le plan. Ne reste pas au milieu du gué. {jug.1}Pèse les facteurs : "
        "lequel explique les autres ? {jug.2}Une réponse possible : la race est le principe qui organise tout. Elle décide qui est exploité, "
        "comme la France, traitée en apparence comme un partenaire, et qui doit être asservi ou exterminé, à l'Est. "
        "{jug.3}D'où un plan en deux parties : d'abord un ordre économique et militaire ; ensuite, un ordre organisé par une hiérarchie raciale.",
        "{-jug}{intro}L'introduction pose tout cela en quelques phrases. Écoute un modèle. "
        "Au début des années 1940, l'Allemagne nazie domine presque toute l'Europe. Ses partisans présentent cette domination comme un nouvel ordre européen, "
        "censé sauver la civilisation européenne. Mais cet ordre sert-il d'abord à exploiter l'Europe pour gagner la guerre, "
        "ou repose-t-il avant tout sur une hiérarchie des races ? Nous verrons d'abord qu'il est un ordre économique et militaire, "
        "puis qu'il est organisé par une hiérarchie raciale, jusqu'au génocide.",
        "{-intro}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod2}Une conclusion modèle. Dans une large mesure, le nouvel ordre européen est un ordre racial. Ses buts économiques et militaires "
        "sont bien réels, des frais d'occupation payés par la France au blé d'Ukraine, mais ils sont organisés par une hiérarchie raciale : "
        "des partenaires à l'Ouest, des esclaves à l'Est, et pour les Juifs, l'assassinat. "
        "C'est pourquoi le génocide n'est pas un effet secondaire de la guerre, mais l'un de ses buts proclamés.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Dans quelle mesure le nouvel ordre européen est-il avant tout un ordre racial ?",
                    src="Sujet écrit pour cette vidéo", enonce=["Réponse à une question problématisée · introduction, plan, conclusion"]),
        "gd": dict(type="cols", g="Pour", gq="génocide : 6 millions · les Slaves en « Untermenschen » · Hitler, 11 déc. 1941",
                   d="Contre", dq="20 millions de RM par jour payés par la France · blé d'Ukraine, pétrole du Caucase · anticommunisme", vs="ou"),
        "jug": dict(type="liste", titre="Prendre position, construire le plan", items=[
            "Peser : quel facteur explique les autres ?", "La race, principe qui organise tout : partenaires à l'Ouest, esclaves à l'Est",
            "Le plan : I. un ordre économique et militaire ; II. une hiérarchie raciale"], x=170, y=140, w=940),
        "intro": dict(type="note", terme="Introduction modèle", cles=["nouvel ordre européen", "exploiter", "hiérarchie"],
                      t="Au début des années 1940, l'Allemagne nazie domine presque toute l'Europe : un « nouvel ordre européen ». "
                        "Sert-il d'abord à exploiter l'Europe, ou repose-t-il sur une hiérarchie des races ? "
                        "I. Un ordre économique et militaire. II. Un ordre organisé par la race.",
                      etape="Le sujet · la problématique · le plan", x=150, y=170, w=980),
        "pa2": dict(type="pause", t="Écris ta conclusion : dans quelle mesure ? Choisis, et justifie en trois phrases.",
                    sous="Mets la vidéo en pause, écris-la, puis relance pour voir un modèle."),
        "mod2": dict(type="note", terme="Conclusion modèle", cles=["large", "hiérarchie", "assassinat"],
                     t="Dans une large mesure : les buts économiques et militaires sont réels, mais organisés par une hiérarchie raciale — "
                       "partenaires à l'Ouest, esclaves à l'Est, assassinat pour les Juifs.",
                     etape="La réponse · les facteurs pesés · la preuve la plus forte", x=150, y=170, w=980),
    }),

    # ================================================================ IV. l'analyse de documents
    dict(id="dbq_a", chap="Analyse de document(s) · la démarche", fond="guerre", humeur="tension",
         retenir="Lire la consigne · présenter (nature, auteur, date, destinataire) · situer dans le contexte · expliquer avec ses connaissances · intérêt et limites, jusqu'à un bilan critique.",
         beats=[
        "{doc}Passons à l'analyse de documents, sur deux documents du cours. {doc.1}Document A : l'ordre de sévérité du feld-maréchal von Reichenau, "
        "le dix octobre 1941. Il appelle les soldats allemands à détruire le système judéo-bolchevique, et à châtier ce qu'il appelle "
        "la sous-humanité juive. {doc.2}Document B : le discours de Staline à Moscou, le six novembre 1941.",
        "{-doc}",
        ("C", "Eh bien, si les Allemands veulent une guerre d'extermination, ils l'auront.", "c_stal"),
        "{-c_stal}{ex3}La consigne : présentez les documents A et B, puis montrez leur {!intérêt et limites}intérêt et leurs limites "
        "pour comprendre la guerre d'anéantissement sur le front de l'Est.",
        "{-ex3}{str}Voici la démarche à suivre, à chaque fois. {str.1}D'abord, la consigne : lis-la deux fois, elle te dit quoi chercher. "
        "{str.2}Puis la présentation : pour chaque document, sa nature, son auteur, sa date, son destinataire. "
        "{str.3}Ensuite, le contexte : dans quelle situation le document a-t-il été écrit ? "
        "{str.4}Puis l'explication : ce que dit le document, éclairé par tes connaissances. "
        "{str.5}Et enfin, l'intérêt et les limites, avec plusieurs arguments, jusqu'à un bilan critique.",
        "{-str}{pa3}",
        ("P", 2.0),
        "{-pa3}{rep}Un modèle. {rep.1}Le document A est un ordre donné par un feld-maréchal allemand à ses troupes, en octobre 1941 ; "
        "le document B est un discours prononcé par Staline à Moscou, un mois plus tard. {rep.2}Tous deux datent de l'automne 1941, "
        "au plus fort de l'avance allemande : les Allemands marchent encore sur la capitale soviétique.",
        "{rep.3}Leur intérêt. Ils montrent les deux faces d'une même logique : l'ordre allemand déshumanise l'ennemi, avec des mots comme sous-humanité, "
        "et Staline répond à l'anéantissement par l'anéantissement, sans pitié pour l'occupant. Ce sont des textes officiels, écrits par des chefs : "
        "ils montrent des intentions, pas des rumeurs.",
        "{rep.4}Leurs limites. Ce sont des textes de propagande : des mots, pas des faits ; ils ne montrent pas ce qui se passe sur le terrain, "
        "les fusillades, les prisonniers affamés. Chacun ne montre que les intentions d'un camp. Et ils ne disent rien des civils, "
        "premières victimes de cette guerre. Le bilan critique : confrontés, ces documents expliquent pourtant pourquoi plus aucune règle "
        "ne tient sur le front de l'Est.",
    ], vis={
        "doc": dict(type="liste", titre="Deux documents du cours", items=[
            "A · Ordre de sévérité de Reichenau, 10 oct. 1941 : « la sous-humanité juive »", "B · Discours de Staline, Moscou, 6 nov. 1941"],
            x=170, y=150, w=940),
        "c_stal": dict(type="cit", a="Joseph Staline", o="discours, Moscou, 6 novembre 1941", x=200, y=190, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="Présentez les documents A et B, puis montrez leur intérêt et leurs limites pour comprendre "
                    "la guerre d'anéantissement sur le front de l'Est.",
                    src="Consigne écrite pour cette vidéo, sur deux documents du cours", enonce=["Analyse de documents · présenter, expliquer, critiquer"]),
        "str": dict(type="liste", titre="Analyse de document(s) : la démarche", cles=["consigne", "présentation", "contexte", "intérêt", "limites"], items=[
            "La consigne : la lire deux fois", "La présentation : nature, auteur, date, destinataire",
            "Le contexte : la situation du moment", "L'explication : le document éclairé par tes connaissances",
            "L'intérêt et les limites, puis un bilan critique"], x=150, y=120, w=980),
        "pa3": dict(type="pause", t="Rédige la présentation : nature, auteur, date et destinataire de chaque document, puis le contexte.",
                    sous="Mets la vidéo en pause, écris-la, puis relance pour voir un modèle."),
        "rep": dict(type="liste", titre="Un modèle de réponse", items=[
            "Présentation : A, ordre d'un feld-maréchal, oct. 1941 · B, Staline, Moscou, nov. 1941",
            "Contexte : automne 1941, l'avance allemande vers Moscou",
            "Intérêt : les deux faces d'une même logique · des textes officiels",
            "Limites : propagande · un seul camp chacun · rien sur les civils"], x=150, y=130, w=980),
    }),

    # ================================================================ V. aller au-delà des documents
    dict(id="dbq_b", chap="Analyse de document(s) · au-delà des documents", fond="nuit", humeur="tension",
         retenir="Montrer que la guerre à l'Est est une guerre d'anéantissement : documents + connaissances (ordre des commissaires, prisonniers soviétiques : 3,3 millions de morts sur 5,7, terre brûlée, Einsatzgruppen, Stalingrad).",
         beats=[
        "{ex4}L'explication va plus loin que les documents. Une consigne fréquente : montrez, à l'aide des documents et de "
        "{!vos connaissances}vos connaissances, que la guerre à l'Est est une guerre d'anéantissement.",
        "{-ex4}{g1}Utilise les documents, puis ce que tu sais des épisodes quatre et cinq. {g1.1}L'ordre des commissaires, en juin 1941 : "
        "les commissaires politiques sont fusillés dès leur capture. Environ deux millions huit cent mille prisonniers de guerre soviétiques meurent "
        "entre juin 1941 et février 1942, surtout de faim ; en tout, environ trois millions trois cent mille des cinq millions sept cent mille "
        "meurent en captivité allemande, près de six sur dix. {g1.2}La terre brûlée, du côté soviétique. "
        "{g1.3}Les Einsatzgruppen, qui fusillent les Juifs derrière le front. {g1.4}Et Stalingrad, où l'on se bat rue par rue.",
        "{-g1}{nua}Et pour nuancer : la guerre à l'Est reste une guerre entre armées, avec un front, des offensives et un tournant. "
        "Mais sur ce front, la guerre des armées et la guerre contre les civils sont une seule et même guerre. "
        "C'est pourquoi trois cinquièmes de tous les morts de la Seconde Guerre mondiale y sont tombés.",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="Montrez, à l'aide des documents et de vos connaissances, que la guerre à l'Est est une guerre d'anéantissement.",
                    src="Consigne écrite pour cette vidéo", enonce=["Analyse de documents · l'explication : documents + connaissances"]),
        "g1": dict(type="globe", code="H3", sc=[28, 26, 27, 38]),
        "nua": dict(type="note", terme="La nuance", cles=["armées", "civils", "même guerre"],
                    t="Encore une guerre entre armées, avec un front et un tournant ; mais la guerre des armées et la guerre contre les civils "
                      "sont une seule et même guerre.",
                    etape="3/5 de tous les morts de la Seconde Guerre mondiale sont tombés sur le front de l'Est", x=150, y=200, w=980),
    }),

    # ================================================================ VI. les pièges
    dict(id="pieges", chap="Les pièges du chapitre", fond="guerre", humeur="mystere",
         retenir="Été 1942 : la police française (pas la Milice) · ≈ 43 000 civils tués dans tout le Royaume-Uni · Stalingrad : l'offensive de 1942 · purges 1937-1938 · Roumanie avec l'Axe jusqu'en août 1944.",
         beats=[
        "{pi}Pour finir, cinq pièges. Chacun vient d'un document ou d'un chiffre du chapitre, et chacun peut te coûter des points. "
        "{pi.1}Un : les arrestations de Juifs en France à l'été 1942, la rafle du Vél d'Hiv, sont menées par la police française. "
        "Pas par la Milice, qui n'est créée qu'en janvier 1943.",
        "{pi.2}Deux : un document du cours donne quarante-trois mille civils tués à Londres pendant le Blitz. Ce chiffre est d'ordinaire celui "
        "de tout le Royaume-Uni, dont environ la moitié à Londres. Écris : environ quarante-trois mille civils tués au Royaume-Uni.",
        "{pi.3}Trois : en 1941, la poussée sud de Barbarossa vise l'Ukraine, Kiev et Rostov. Stalingrad et le Caucase sont les objectifs "
        "de la seconde offensive, à l'été 1942.",
        "{pi.4}Quatre : les purges qui décapitent l'Armée rouge ont lieu surtout en 1937 et 1938 ; Toukhatchevski est fusillé en juin 1937.",
        "{pi.5}Et cinq : le tableau des divisions range la Roumanie parmi les Alliés, alors qu'elle combat avec l'Axe jusqu'en août 1944. "
        "Une limite idéale dans une analyse de document.",
        "{-pi}{fin}Prochain épisode, le dernier : le récapitulatif de tout le chapitre, d'un seul tenant.",
        ("P", 2.0),
    ], vis={
        "pi": dict(type="liste", titre="Cinq pièges", items=[
            "Été 1942 : la police française, pas la Milice (créée en janv. 1943)", "Blitz : ≈ 43 000 civils tués dans tout le Royaume-Uni",
            "Stalingrad : l'objectif de 1942, pas de 1941", "Les purges : surtout 1937-1938", "La Roumanie : avec l'Axe jusqu'en août 1944"],
            x=150, y=120, w=980),
        "fin": dict(type="mot", t="Prochain : le récap", g="Épisode 7 · tout le chapitre", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Quels sont les deux grands exercices de l'histoire-géographie en Terminale ?",
         r=["La réponse à une question problématisée et l'analyse de document(s)", "Deux dissertations",
            "Un QCM et un oral", "Un commentaire de texte littéraire et un résumé"], ok=0, voir="fmt",
         ex="Dans un même devoir, l'un porte souvent sur l'histoire, l'autre sur la géographie."),
    dict(q="Que doit contenir l'introduction d'une réponse à une question problématisée ?",
         r=["La présentation du sujet, la problématique et l'annonce du plan", "La réponse détaillée, avec tous les exemples",
            "Une liste de dates", "Une citation et rien d'autre"], ok=0, voir="intro",
         ex="Le sujet, la problématique, le plan : la réponse elle-même vient dans le développement et la conclusion."),
    dict(q="Que comprend la présentation d'un document ?", r=["Sa nature, son auteur, sa date, son destinataire", "Un résumé ligne à ligne",
         "Ton avis personnel", "Une citation de tout le texte"], ok=0, voir="str",
         ex="Puis le contexte, l'explication, et enfin l'intérêt et les limites."),
    dict(q="Laquelle est une vraie LIMITE de l'ordre de sévérité de Reichenau pour cette consigne ?",
         r=["Il montre des intentions, pas ce qui se passe sur le terrain", "Il date de 1941", "C'est un document officiel",
            "Il parle des Juifs"], ok=0, voir="rep",
         ex="La propagande montre des mots, pas des faits ; et un seul camp."),
    dict(q="Qui mène les rafles de Juifs en France en juillet 1942 ?", r=["La police française", "La Milice", "La Gestapo seule",
         "Les Einsatzgruppen"], ok=0, voir="pi", ex="La Milice n'est créée qu'en janvier 1943."),
    dict(q="Dans la conclusion d'une question problématisée, qu'est-ce qui compte le plus ?",
         r=["Une réponse nette à la question, après avoir pesé les facteurs", "Une chronologie complète",
            "Le plus de citations possible", "Éviter toute prise de position"], ok=0, voir="jug",
         ex="Ne reste pas au milieu du gué : pèse les facteurs, et réponds."),
]

CREDITS = [
    "Contenu : la méthode des exercices d'histoire-géographie de Terminale (réponse à une question problématisée, analyse de document(s)) ; "
    "documents du cours d'histoire de Terminale, chapitre « La Seconde Guerre mondiale » (ordre de sévérité de Reichenau, discours de Staline "
    "du 6 novembre 1941) ; les points à vérifier du chapitre.",
    "Sujets, consignes et copies modèles écrits pour cette vidéo.",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
