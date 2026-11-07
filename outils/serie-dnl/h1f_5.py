"""Histoire · chapitre 1 « Le krach de 1929 et ses conséquences » — édition française, épisode 5 :
« La crise à l'épreuve : question problématisée et analyse de document ».

Édition française adaptée de h1_5.py (voir outils/serie-dnl/EDITION_FR.md, section « Épisode d'épreuve ») : l'épisode
ne présente plus l'essay, le DBQ ni l'oral de la DNL, mais les deux exercices de l'histoire-géographie de Terminale,
la réponse à une question problématisée et l'analyse de document(s). Mêmes sujets et mêmes documents que l'épisode
anglais (causes du krach, Smoot-Hawley, les deux problématiques, le dossier documentaire : graphique du chômage allemand
et mémoires de Melita Maschmann ; Migrant Mother ; « The Doormat » de David Low, décrit et non montré), mêmes scènes,
mêmes identifiants, mêmes pauses « À toi ». Aucun barème, coefficient ni durée d'épreuve n'est donné.
Carte animée H1 : mêmes numéros de scènes que h1_5.py (la carte passe d'elle-même en français).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-5"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 5
TITRE = "La crise à l'épreuve : question problématisée et analyse de document"
SUIVANT = "Épisode 6 · Récap"
PRONONCIATION = {"Maschmann": "Mach-mane", "Creditanstalt": "Crédit-anne-chtalt", "Smoot-Hawley": "Smoute-Hô-lé",
                 "Smoot": "Smoute", "Hawley": "Hô-lé", "Dawes": "Dôze", "Hoover": "Houveur", "Dow Jones": "Dô Djônz",
                 "Wall Street": "Wol Strite", "Import Duties Act": "Im-porte Diou-tiz Akt", "USS": "U S S", "Panay": "Pa-naï",
                 "Chamberlain": "Tchèm-beur-line", "Migrant Mother": "Maï-grante Mo-zeur", "Owens": "Ô-ouènz",
                 "Thompson": "Tom-sonne", "Lange": "Lang", "Resettlement Administration": "Ri-sétteul-mente Administré-cheune",
                 "Low": "Lô", "John Simon": "Djone Saï-meune", "Weimar": "Vaï-mar"}

# Dossier documentaire, document 2 : chômage des travailleurs assurés en Allemagne (H1Germany)
CHOMAGE = [[1928, 8.6], [1929, 13.3], [1930, 22.7], [1931, 34.3], [1932, 43.8], [1933, 36.2]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{g0}{q1}Tu connais maintenant l'histoire : le krach, la Dépression, le nationalisme économique, et des démocraties qui n'ont pas voulu agir. "
        "{-q1}{q2}Mais le jour de l'épreuve, personne ne te demandera de la raconter. Il faudra expliquer, discuter, et analyser des documents.",
        "{-q2}{-g0}{plan}Cet épisode est donc un atelier. {plan.1}D'abord, les deux exercices. {plan.2}Puis la question problématisée : "
        "un sujet qui demande d'expliquer, et deux qui demandent de discuter, avec des modèles. {plan.3}Puis les deux grandes problématiques du chapitre. "
        "{plan.4}Puis l'analyse de documents, sur des documents du cours. {plan.5}Et pour finir, les deux notions clés.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="question", t="Tu connais l'histoire.", bande=True),
        "q2": dict(type="question", t="Sauras-tu t'en servir le jour de l'épreuve ?", bande=True),
        "plan": dict(type="liste", titre="Cet épisode, un atelier", items=[
            "Les deux exercices", "La question problématisée : expliquer, puis discuter", "Les deux problématiques du chapitre",
            "L'analyse de documents", "Les deux notions clés"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · Chapitre 1 · Épisode 5", t="La crise à l'épreuve",
                      sous="question problématisée · analyse de documents · notions clés"),
    }),

    # ================================================================ I. les deux exercices
    dict(id="format", chap="Les deux exercices", fond="nuit", humeur="calme",
         retenir="Deux exercices. La réponse à une question problématisée : introduction avec problématique et plan, paragraphes argument + exemple précis, conclusion qui répond. L'analyse de document(s) : consigne, présentation, contexte, explication, intérêt et limites.",
         beats=[
        "{ecr}En histoire, deux exercices t'attendent. {ecr.1}Le premier : la réponse à une question problématisée. On te pose une question, et tu y réponds par un texte construit. "
        "{ecr.2}Une introduction, un développement en parties, une conclusion. "
        "{ecr.3}Chaque argument s'appuie sur un exemple précis : une date, un chiffre, un nom. {ecr.4}Et la conclusion répond nettement à la question.",
        "{-ecr}{ora}Le second : l'analyse d'un document, ou de deux. {ora.1}D'abord, lire la consigne : elle dit ce qu'on attend de toi. "
        "{ora.2}Ensuite, présenter le document et le situer dans son contexte. {ora.3}Puis l'expliquer, avec tes connaissances. "
        "{ora.4}Enfin, en montrer l'intérêt et les limites.",
        "{-ora}{ch1}Pour ce chapitre, retiens deux grandes problématiques et deux notions clés. Elles arrivent à la fin de cet épisode, "
        "mais garde-les en tête dès maintenant : ce sont aussi d'excellents sujets de question problématisée.",
    ], vis={
        "ecr": dict(type="liste", titre="La réponse à une question problématisée", items=[
            "Une question, une réponse construite", "Introduction · développement · conclusion", "Chaque argument + un exemple précis",
            "Une conclusion qui répond"], x=170, y=130, w=940),
        "ora": dict(type="liste", titre="L'analyse de document(s)", items=[
            "Lire la consigne", "Présenter le document, le situer dans son contexte", "L'expliquer avec tes connaissances",
            "Intérêt et limites : le regard critique"], x=170, y=130, w=940),
        "ch1": dict(type="cols", g="2 problématiques", gq="les démocraties responsables ? · le nationalisme économique, facteur décisif ?",
                    d="2 notions clés", dq="la dépression économique mondiale (années 1930) · l'apaisement", vs="+"),
    }),

    # ================================================================ II. la méthode de la question problématisée
    dict(id="methode", chap="La question problématisée : la méthode", fond="aube", humeur="calme",
         retenir="Expliquer = plusieurs causes, « parce que ». Discuter (« dans quelle mesure », « quel rôle ») = pour, contre, hiérarchie, bilan. Introduction : accroche, définitions, contexte, problématique, plan. Un paragraphe = idée, exemple précis, explication, lien. La conclusion répond.",
         beats=[
        "{ess}Une question problématisée prend en général l'une de deux formes. {ess.1}Certaines demandent d'expliquer : pourquoi, comment. "
        "Tu donnes plusieurs causes bien argumentées, et tu dois te surprendre à écrire « parce que ». "
        "{ess.2}D'autres demandent de discuter : dans quelle mesure, quel rôle. Il faut alors des arguments pour et contre, une hiérarchie des facteurs, et un bilan.",
        "{-ess}{intro}L'introduction suit cinq temps. {intro.1}Une accroche : un fait, une date, un chiffre qui saisit le lecteur. "
        "{intro.2}La définition des termes du sujet. {intro.3}Le contexte : où, quand, qui. "
        "{intro.4}La problématique : la question transformée en problème. {intro.5}Et l'annonce du plan.",
        "{-intro}{peel}Ensuite, chaque paragraphe suit les mêmes quatre temps. {peel.1}Une idée : un argument, en une phrase. "
        "{peel.2}Un exemple précis tiré du cours : une date, un chiffre, un nom. {peel.3}Une explication : pourquoi l'exemple prouve l'idée. "
        "{peel.4}Et un lien avec la question.",
        "{-peel}{ccl}Enfin, la conclusion ne répète pas : elle répond. Dans quelle mesure ? Quel facteur compte le plus, et pourquoi ? "
        "{!Prends position}Prends position.",
    ], vis={
        "ess": dict(type="liste", titre="Deux formes de sujet", cles=["parce que", "bilan"], items=[
            "Expliquer : plusieurs causes… « parce que »", "Discuter : pour, contre, une hiérarchie, un bilan"],
            x=170, y=170, w=940),
        "intro": dict(type="liste", titre="L'introduction, en cinq temps", items=[
            "Accroche : un fait, une date, un chiffre", "Définition des termes du sujet", "Contexte : où, quand, qui",
            "La problématique", "L'annonce du plan"], x=170, y=110, w=940),
        "peel": dict(type="liste", titre="Un argument = un paragraphe", cles=["idée", "exemple", "explication", "lien"], items=[
            "Une idée : un argument, une phrase", "Un exemple précis : une date, un chiffre, un nom", "Une explication : pourquoi l'exemple prouve l'idée",
            "Un lien : retour à la question"], x=170, y=130, w=940),
        "ccl": dict(type="note", terme="La conclusion", cles=["répond", "compte"],
                    t="Elle ne répète pas : elle répond. Dans quelle mesure ? Quel facteur compte le plus, et pourquoi ?",
                    etape="Une réponse claire à la question", x=150, y=200, w=980),
    }),

    # ================================================================ III. expliquer
    dict(id="explain", chap="Question problématisée · expliquer", fond="nuit", humeur="tension",
         retenir="Pourquoi le krach de 1929 devient-il une crise mondiale ? Le rappel des prêts américains (circuit Dawes, Creditanstalt mai 1931) · l'étalon-or (le Royaume-Uni en sort, sept. 1931) · le protectionnisme (Smoot-Hawley 1930 → commerce mondial −66 % en 1934).",
         beats=[
        "{ex1}Voici un sujet qui demande d'expliquer, écrit pour cette vidéo. {!Pourquoi}Pourquoi le krach de Wall Street de 1929 devient-il une crise mondiale ?",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{g1}Trois canaux, un exemple chacun. {g1.1}Un : le rappel des prêts américains. Avec le plan Dawes de 1924, l'Amérique prête huit cents millions de marks à l'Allemagne. "
        "Dès lors, les finances de l'Europe reposent sur le crédit américain. Et après octobre 1929, l'argent est rappelé. "
        "La plus grande banque d'Autriche, la Creditanstalt, fait faillite en mai 1931 ; les banques allemandes suivent en juillet.",
        "{g1.2}Deux : l'étalon-or, la courroie de transmission. Pour défendre le dollar, la Réserve fédérale relève ses taux d'intérêt, "
        "et l'or quitte tous les autres pays, qui doivent relever leurs taux à leur tour : le pire remède possible. "
        "Le Royaume-Uni sort de l'étalon-or en septembre 1931.",
        "{g1.3}Trois : le protectionnisme. Le dix-sept juin 1930, Hoover signe le tarif Smoot-Hawley. "
        "Le Canada a déjà riposté, dès mai, et le commerce mondial chute d'environ deux tiers, en valeur, entre 1929 et 1934.",
        "{-g1}{mod1}Un paragraphe modèle, pour le premier canal.",
        "Le krach devient une crise mondiale d'abord parce que l'Europe dépend du crédit américain. Depuis le plan Dawes de 1924, les prêts américains "
        "permettent à l'Allemagne de payer les réparations, et aux Alliés de rembourser leurs dettes de guerre aux États-Unis. Quand les banques américaines rappellent "
        "leurs prêts après octobre 1929, le circuit se rompt : la Creditanstalt fait faillite en mai 1931, et les banques allemandes suivent en juillet. "
        "Un krach américain gagne donc l'Europe par l'argent que l'Amérique lui avait prêté.",
        "Une idée, un exemple, une explication, un lien. Fais de même pour l'étalon-or et pour le protectionnisme, et ta réponse est construite.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Pourquoi le krach de Wall Street de 1929 devient-il une crise mondiale ?",
                    src="Sujet écrit pour cette vidéo", enonce=["Question problématisée · expliquer"]),
        "pa1": dict(type="pause", t="Trouve trois raisons, chacune avec un exemple précis du cours.",
                    sous="Mets la vidéo en pause, écris tes trois raisons, puis reprends."),
        "g1": dict(type="globe", code="H1", sc=[9, 19, 15]),
        "mod1": dict(type="note", terme="Paragraphe modèle · canal 1", cles=["parce que", "Dawes", "Creditanstalt"],
                     t="Le krach devient une crise mondiale d'abord parce que l'Europe dépend du crédit américain : plan Dawes (1924), prêts rappelés "
                       "après oct. 1929, faillite de la Creditanstalt (mai 1931)…",
                     etape="Idée · exemple · explication · lien", x=150, y=170, w=980),
    }),

    # ================================================================ IV. discuter : les causes du krach
    dict(id="assess1", chap="Question problématisée · discuter les causes", fond="nuit", humeur="tension",
         retenir="Le rôle de chaque facteur : la spéculation est le déclencheur (bourse ×3, achats à crédit jusqu'à 90 %) · les faiblesses structurelles expliquent la profondeur (surproduction, inégalités, prix agricoles) · la panique et la politique suivie amplifient.",
         beats=[
        "{ex2}Maintenant, un sujet tiré directement du cours. {!Quel rôle}Quel rôle chaque facteur a-t-il joué dans le déclenchement du krach de 1929 ? Lequel fut le plus important ?",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mi}Une introduction modèle, en cinq temps. {mi.1}L'accroche : en cinq ans, entre 1924 et 1929, la bourse américaine triple ; "
        "en juillet 1932, le Dow Jones a perdu quatre-vingt-neuf pour cent de sa valeur. {mi.2}La définition : le krach, c'est l'effondrement des cours des actions américaines "
        "fin octobre 1929, pas la Dépression qui suit. {mi.3}Le contexte : les années folles, trois présidents républicains, la consommation de masse à crédit. "
        "{mi.4}La problématique : les facteurs se renforcent les uns les autres ; alors, de quel facteur les autres dépendaient-ils ? "
        "{mi.5}Le plan : une hiérarchie, pas une liste.",
        "{-mi}{hi}Voici cette hiérarchie. {hi.1}D'abord, la spéculation, le meilleur candidat au rôle de déclencheur. Les courtiers prêtaient jusqu'à quatre-vingt-dix pour cent du prix d'une action : "
        "une baisse de dix pour cent suffisait à ruiner l'acheteur. Mais la spéculation explique la soudaineté de la chute, pas sa profondeur. "
        "{hi.2}Ensuite, les faiblesses structurelles expliquent pourquoi la chute devient une catastrophe : la surproduction, une majorité d'Américains trop pauvres pour acheter ce que produisent les usines, "
        "et des prix agricoles en baisse depuis 1920. {hi.3}Enfin, la panique et la politique républicaine ont amplifié la crise, sans en être l'origine. "
        "Et faute de garantie des dépôts, cinq mille banques avaient fait faillite en 1932.",
        "{-hi}{cc2}Et la conclusion tranche. La spéculation a déclenché le krach ; la surproduction et les inégalités ont fait qu'il ne se corrigerait pas de lui-même. "
        "Classer les facteurs compte plus que les énumérer : c'est exactement ce que demande un sujet qui invite à discuter.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Quel rôle chaque facteur a-t-il joué dans le déclenchement du krach de 1929 ? Lequel fut le plus important ?",
                    src="Sujet du cours (chapitre 1)", enonce=["Question problématisée · discuter"]),
        "pa2": dict(type="pause", t="Écris ton introduction : accroche, définition, contexte, problématique, plan.",
                    sous="Mets la vidéo en pause, écris cinq phrases, puis reprends pour voir un modèle."),
        "mi": dict(type="liste", titre="Une introduction modèle", petit=True, items=[
            "Accroche : la bourse ×3 en cinq ans ; le Dow Jones −89 % en juillet 1932", "Définition : le krach = fin octobre 1929, pas la Dépression",
            "Contexte : les années folles, la politique républicaine, le crédit", "Problématique : de quel facteur les autres dépendaient-ils ?",
            "Plan : une hiérarchie, pas une liste"], x=150, y=110, w=980),
        "hi": dict(type="liste", titre="La hiérarchie", marques=["1", "2", "3"], items=[
            "Le déclencheur : la spéculation (achats à crédit jusqu'à 90 %)", "La profondeur : surproduction, inégalités, prix agricoles depuis 1920",
            "Les amplificateurs : panique, politique suivie, pas de garantie des dépôts (5 000 banques)"], x=150, y=150, w=980),
        "cc2": dict(type="note", terme="Conclusion modèle", cles=["déclenché", "Classer"],
                    t="La spéculation a déclenché le krach ; la surproduction et les inégalités ont fait qu'il ne se corrigerait pas de lui-même.",
                    etape="Classer les facteurs compte plus que les énumérer", x=150, y=190, w=980),
    }),

    # ================================================================ V. discuter : Smoot-Hawley
    dict(id="assess2", chap="Question problématisée · juger une politique", fond="nuit", humeur="tension",
         retenir="Le tarif de 1930 : un échec au regard de ses propres buts · il déclenche une guerre commerciale (Canada, Import Duties Act 1932, quotas français 1931 ; commerce mondial −66 %) · sans causer la Dépression. Surtout, il détruit le libre-échange de 1919.",
         beats=[
        "{ex3}Un second sujet du cours, sur une seule politique. Le tarif douanier de 1930 a-t-il été efficace "
        "face aux défis posés par la Grande Dépression ?",
        "{-ex3}{eff}Le piège, c'est le mot efficace. Juge la loi au regard de ses propres buts : protéger les agriculteurs et l'industrie des États-Unis. "
        "Pas au regard de ce que l'on sait aujourd'hui.",
        "{-eff}{g2}Ensuite, trois temps. {g2.1}Elle échoue même au regard de ses propres buts. Des droits de douane sur plus de vingt mille produits, et pourtant les prix agricoles continuent de baisser "
        "et le chômage d'augmenter ; Smoot et Hawley perdent tous deux leur siège en 1932. Et l'échec était annoncé : mille vingt-huit économistes "
        "avaient demandé un veto. {g2.2}Deuxième temps : elle déclenche une guerre commerciale. Le Canada riposte avant même la signature, en mai 1930 ; le Royaume-Uni vote l'Import Duties Act en 1932, "
        "la France instaure des quotas en 1931, chacun ménageant son empire. Le monde se divise en blocs fermés.",
        "{-g2}{nu2}Troisième temps, la nuance. Elle n'a pas causé la Dépression : le ralentissement commence avec le krach et les faillites bancaires, et le tarif l'aggrave. "
        "Roosevelt change de politique en 1934, mais trop tard. D'où le bilan : inefficace au regard de ses buts, néfaste par ses conséquences, "
        "et politiquement décisive, parce qu'elle détruit le pilier libre-échangiste de l'ordre libéral de 1919.",
    ], vis={
        "ex3": dict(type="exo", niveau="essay", titre="Le tarif douanier de 1930 a-t-il été efficace face aux défis posés par la Grande Dépression ?",
                    src="Sujet du cours (chapitre 1)", enonce=["Question problématisée · discuter"]),
        "eff": dict(type="def", cles=["buts", "agriculteurs"], terme="Le mot clé · efficace",
                    t="Au regard de ses propres buts : protéger les agriculteurs et l'industrie des États-Unis.",
                    etape="Pas au regard de ce que l'on sait aujourd'hui", x=170, y=200, w=940),
        "g2": dict(type="globe", code="H1", sc=[15, 16]),
        "nu2": dict(type="cols", g="Inefficace · néfaste", gq="prix agricoles toujours en baisse · 1 028 économistes · guerre commerciale · commerce mondial −66 %",
                    d="Mais pas la cause", dq="le krach et les banques d'abord · abandonné en 1934, trop tard", vs="vs"),
    }),

    # ================================================================ VI. problématique 1
    dict(id="ki1", chap="Problématique 1 · Les démocraties responsables ?", fond="guerre", humeur="tension",
         retenir="Problématique 1 : les démocraties ont bâti un ordre sans le garantir (Sénat américain, SDN sans armée), l'ont affaibli (Smoot-Hawley, prêts, or), ne l'ont pas défendu (Mandchourie, Éthiopie, Munich) ; mais les agresseurs ont voulu la guerre. Possible, pas inévitable.",
         beats=[
        "{ki}Voici la première grande problématique du chapitre, un excellent sujet de question problématisée. "
        "Dans quelle mesure les grandes démocraties portent-elles elles-mêmes une part de responsabilité dans les origines de la Seconde Guerre mondiale ?",
        "{-ki}{mots}Lis bien les mots. {mots.1}Une part : la question invite déjà à une réponse nuancée. "
        "{mots.2}Les grandes démocraties : le Royaume-Uni, la France et les États-Unis, garants de l'ordre libéral de 1919.",
        "{-mots}{g3}Puis argumente en quatre temps. {g3.1}Un : elles ont bâti un ordre qu'elles n'ont pas voulu garantir. Le Sénat américain refuse de ratifier le traité de Versailles : "
        "les États-Unis n'entrent jamais dans la Société des Nations que leur propre président avait conçue ; et la SDN n'a pas d'armée. "
        "Quand le Japon s'empare de la Mandchourie, en septembre 1931, la SDN le condamne. Le Japon quitte tout simplement la SDN, en mars 1933. "
        "{g3.2}Deux : elles l'ont affaibli économiquement après 1929. Smoot-Hawley, le rappel des prêts, la défense de l'or. "
        "{g3.3}Trois : elles ont refusé de le défendre. L'Amérique vote les lois de neutralité, de 1935 à 1937, et ne fait rien, même quand l'USS Panay est bombardé. "
        "{g3.4}Le Royaume-Uni refuse un embargo pétrolier contre l'Italie en 1935. {g3.5}La France et le Royaume-Uni laissent faire en Rhénanie, en mars 1936, "
        "{g3.6}et signent les accords de Munich en septembre 1938.",
        "{-g3}{mais}Quatre : l'argument inverse. L'initiative revient aux régimes militaristes, à Berlin, à Rome et à Tokyo. "
        "La Dépression a offert un public aux nazis ; elle n'a obligé personne à envahir son voisin.",
        "{-mais}{pa3}",
        ("P", 2.0),
        "{-pa3}{cc3}Un bilan modèle. Oui, en partie. Les démocraties partagent la responsabilité par omission, par l'isolationnisme, le protectionnisme et l'apaisement : "
        "elles ont bâti un ordre, l'ont affaibli, et n'ont pas voulu le défendre. Mais la guerre a été voulue par les agresseurs. "
        "{!possible, pas inévitable}Les démocraties ont rendu la guerre possible, pas inévitable. Le mot du cours est le bon : des démocraties réticentes.",
    ], vis={
        "ki": dict(type="exo", niveau="essay", titre="Dans quelle mesure les grandes démocraties portent-elles une part de responsabilité dans les origines de la Seconde Guerre mondiale ?",
                   src="Problématique 1 du chapitre", enonce=["Dans quelle mesure… ? Une réponse nuancée"]),
        "mots": dict(type="liste", titre="Lire le sujet", cles=["nuancée", "1919"], items=[
            "« Une part » : une réponse nuancée est attendue", "« Les grandes démocraties » : Royaume-Uni, France, États-Unis, garants de l'ordre de 1919"],
            x=170, y=170, w=940),
        "g3": dict(type="globe", code="H1", sc=[18, 15, 26, 27, 29, 30]),
        "mais": dict(type="note", terme="L'argument inverse", cles=["initiative", "militaristes"],
                     t="L'initiative revient aux régimes militaristes, à Berlin, à Rome et à Tokyo.",
                     etape="La Dépression a offert un public ; elle n'a obligé personne à envahir", x=150, y=200, w=980),
        "pa3": dict(type="pause", t="Ton bilan : dans quelle mesure ? Trois phrases.",
                    sous="Mets la vidéo en pause, écris ta conclusion, puis reprends pour voir un modèle."),
        "cc3": dict(type="note", terme="Bilan modèle", cles=["partie", "omission", "réticentes"],
                    t="Oui, en partie : les démocraties partagent la responsabilité par omission (isolationnisme, protectionnisme, apaisement), mais la guerre a été voulue par les agresseurs.",
                    etape="Elles l'ont rendue possible, pas inévitable", x=150, y=180, w=980),
    }),

    # ================================================================ VII. problématique 2
    dict(id="ki2", chap="Problématique 2 · Le nationalisme économique", fond="guerre", humeur="mystere",
         retenir="Problématique 2 : le nationalisme économique a rongé l'ordre de 1919 (tarifs, quotas, blocs, autarcie) · mais il est un symptôme de la Dépression, pratiqué aussi par Londres et Paris · l'idéologie compte autant. Un facteur aggravant, pas décisif.",
         beats=[
        "{ki2}La seconde problématique. Dans quelle mesure le nationalisme économique est-il le facteur décisif de la marche à la guerre en 1939 ?",
        "{-ki2}{def2}Commence par une définition. Le nationalisme économique : placer l'intérêt économique national au-dessus de la coopération internationale, "
        "par les droits de douane, les quotas et la manipulation des monnaies. Puis mets à l'épreuve le mot décisif : était-ce le facteur dont dépendaient tous les autres, ou un maillon d'une chaîne ?",
        "{-def2}{pl2}Trois parties. {pl2.1}Pour : il a rongé l'ordre international. Smoot-Hawley, les quotas français et l'Import Duties Act "
        "réduisent le commerce mondial des deux tiers. Ils divisent le monde en blocs impériaux. Et pour un État sans empire, l'autarcie et la conquête finissent par paraître rationnelles : "
        "c'est exactement ce que prétend la politique économique nazie. {pl2.2}Contre : c'est un symptôme autant qu'une cause. Le protectionnisme répond à la Dépression, "
        "qui répond au krach. Et le Royaume-Uni et la France l'ont pratiqué aussi, sans entrer en guerre avant l'invasion de la Pologne. "
        "{pl2.3}Et l'idéologie dispute la même place : le militarisme en Allemagne, en Italie et au Japon, le pillage nazi et la spoliation des citoyens juifs, "
        "des crimes qu'aucune barrière douanière n'explique.",
        "{-pl2}{cc4}Le bilan : un facteur aggravant sérieux, mais pas le facteur décisif. Il explique pourquoi le monde n'a pas su coopérer, "
        "pas pourquoi trois régimes ont choisi la guerre. L'économie a créé l'occasion ; l'idéologie a fourni l'intention. Et cela mène tout droit au chapitre deux.",
    ], vis={
        "ki2": dict(type="exo", niveau="essay", titre="Dans quelle mesure le nationalisme économique est-il le facteur décisif de la marche à la guerre en 1939 ?",
                    src="Problématique 2 du chapitre", enonce=["Mettre à l'épreuve le mot « décisif »"]),
        "def2": dict(type="def", cles=["national", "coopération"], terme="Notion · le nationalisme économique",
                     t="Placer l'intérêt économique national au-dessus de la coopération internationale : droits de douane, quotas, manipulation des monnaies.",
                     etape="« Décisif » : le facteur dont dépendaient les autres ?", x=170, y=200, w=940),
        "pl2": dict(type="liste", titre="Trois parties", marques=["+", "−", "?"], items=[
            "Pour : il ronge l'ordre de 1919 · commerce −66 % · blocs · autarcie", "Contre : un symptôme de la Dépression · le Royaume-Uni et la France aussi",
            "L'idéologie dispute la place : militarisme, pillage nazi"], x=150, y=150, w=980),
        "cc4": dict(type="note", terme="Bilan modèle", cles=["aggravant", "occasion", "intention"],
                    t="Un facteur aggravant sérieux, pas le facteur décisif : il explique pourquoi le monde n'a pas su coopérer, pas pourquoi trois régimes ont choisi la guerre.",
                    etape="L'économie : l'occasion · l'idéologie : l'intention", x=150, y=180, w=980),
    }),

    # ================================================================ VIII. analyse de documents — le dossier documentaire
    dict(id="dbq_a", chap="Analyse de documents · présenter, expliquer, critiquer", fond="aube", humeur="calme",
         retenir="Analyse de document(s) : lire la consigne · présenter chaque document (nature, auteur, date, destinataire) · le situer dans son contexte et l'expliquer avec ses connaissances · en montrer l'intérêt et les limites (provenance, intention, ce qui manque).",
         beats=[
        "{str}Passons à l'analyse de documents. La démarche est toujours la même. "
        "{str.1}D'abord, lire la consigne, mot à mot : elle te dit ce qu'on attend de toi. "
        "{str.2}Ensuite, présenter chaque document : sa nature, son auteur, sa date, et à qui il s'adresse. "
        "{str.3}Puis le situer dans son contexte et l'expliquer, avec tes connaissances. "
        "{str.4}Enfin, le regard critique : son intérêt, et ses limites. D'où vient-il ? Dans quel but ? Et que ne dit-il pas ?",
        "{-str}{gr}Deux documents du dossier documentaire. Le document 2 : {gr.1}un graphique du chômage en Allemagne. {gr.2}Huit virgule six pour cent en 1928, "
        "{gr.3}quarante-trois virgule huit pour cent en 1932, {gr.4}puis trente-six virgule deux en 1933. Attention : il ne compte que les travailleurs assurés.",
        "{doc}Le document 5 : les mémoires de Melita Maschmann, ancienne membre de la Jeunesse hitlérienne, publiés en 1963.{-gr}",
        ("C", "Les nazis promettaient d'en finir avec le chômage et la misère, et je les ai crus.", "c_mas"),
        "{-c_mas}{-doc}{ex4}{!La consigne}La consigne : montrez comment la crise a aidé les nazis, puis portez un regard critique sur les documents 2 et 5.",
        "{-ex4}{pa4}",
        ("P", 2.0),
        "{-pa4}{rep}Un modèle. {rep.1}La présentation. Le document 2 est un graphique du chômage des travailleurs assurés en Allemagne, de 1928 à 1933. "
        "Le document 5 est un extrait des mémoires de Melita Maschmann, ancienne membre de la Jeunesse hitlérienne, publiés en 1963.",
        "{rep.2}Le contexte : la crise frappe de plein fouet une Allemagne dont l'industrie dépend du crédit américain.",
        "{rep.3}L'explication, et l'intérêt. D'abord, le document 2 mesure l'ampleur de la crise : le chômage est multiplié par cinq en quatre ans, "
        "et culmine en 1932, l'année qui précède l'arrivée de Hitler à la chancellerie. Ensuite, le document 5 montre le mécanisme de l'intérieur : "
        "une jeune Allemande explique pourquoi la promesse nazie a fonctionné sur elle. Enfin, ensemble, ils relient un chiffre à un sentiment, la crise au vote.",
        "{rep.4}Les limites. D'abord, le graphique ne compte que les travailleurs assurés, pas toute la population active : il donne un taux, pas le nombre de chômeurs. "
        "Ensuite, les mémoires sont écrits trente ans plus tard, avec le recul, par une femme qui peut vouloir expliquer, ou excuser, son choix. "
        "Enfin, ce qui manque : aucun des deux documents ne montre que les nazis n'ont jamais eu la majorité, ni que les conservateurs ont fait entrer Hitler au pouvoir, en janvier 1933. "
        "Bilan critique : deux documents très utiles, à condition de les compléter.",
    ], vis={
        "str": dict(type="liste", titre="L'analyse de documents : la démarche", cles=["consigne", "présenter", "expliquer", "limites"], items=[
            "Lire la consigne : ce qu'on attend de toi", "Présenter chaque document : nature, auteur, date, destinataire",
            "Le situer dans son contexte, l'expliquer avec tes connaissances", "Intérêt et limites : provenance, intention, ce qui manque"], x=150, y=120, w=980),
        "gr": dict(type="graphe", titre="Document 2 · chômage en Allemagne, travailleurs assurés (%)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.5, 1933.5], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="année", ly="%"),
                   el=[dict(type="courbe", pts=CHOMAGE, c="ca", dur=2.2),
                       dict(type="points", pts=[[1928, 8.6]], c="sa", lbl="1928 : 8,6 %", lp=[1928.2, 15]),
                       dict(type="points", pts=[[1932, 43.8]], c="ca", lbl="1932 : 43,8 %", lp=[1930.4, 47]),
                       dict(type="points", pts=[[1933, 36.2]], c="sa", lbl="1933 : 36,2 %", lp=[1932.2, 30])]),
        "doc": dict(type="tag", t="Document 5 · Melita Maschmann, mémoires, 1963", x=200, y=650),
        "c_mas": dict(type="cit", a="Melita Maschmann", o="mémoires, 1963 (dossier documentaire, document 5)", x=200, y=210, w=880),
        "ex4": dict(type="exo", niveau="dbq", titre="Montrez comment la crise a aidé les nazis, puis portez un regard critique sur les documents 2 et 5.",
                    src="Dossier documentaire · document 2 (graphique) et document 5 (mémoires)",
                    donnees=["Document 2 : chômage en Allemagne, travailleurs assurés, 1928-1933", "Document 5 : Melita Maschmann, mémoires, 1963"],
                    questions=["Présenter les documents", "Les situer dans leur contexte", "Expliquer : ce qu'ils montrent",
                               "Intérêt et limites"]),
        "pa4": dict(type="pause", t="Analyse de documents : montre comment la crise a aidé les nazis, puis critique les documents 2 et 5.",
                    sous="Présentation, contexte, explication, intérêt et limites. Mets la vidéo en pause, écris, puis reprends pour voir un modèle."),
        "rep": dict(type="liste", titre="Un modèle", petit=True, items=[
            "Présentation : graphique, travailleurs assurés, 1928-1933 · mémoires de Maschmann, 1963",
            "Contexte : une Allemagne dont l'industrie dépend du crédit américain",
            "Explication et intérêt : l'ampleur (×5, pic en 1932) · le mécanisme vu de l'intérieur · un chiffre + un sentiment",
            "Limites : assurés seulement · le recul · ni majorité, ni janvier 1933"], x=150, y=120, w=980),
    }),

    # ================================================================ IX. confronter aux connaissances
    dict(id="dbq_b", chap="Analyse de documents · confronter aux connaissances", fond="nuit", humeur="tension",
         retenir="Les documents + tes connaissances : la crise a créé le public (43,8 % en 1932, « Du travail, la liberté, du pain ! ») ; un calcul politique a ouvert la porte (jamais la majorité, les conservateurs nomment Hitler, janv. 1933).",
         beats=[
        "{ex5}Une consigne peut aller plus loin. À l'aide des documents et de vos connaissances, dans quelle mesure la crise explique-t-elle l'arrivée de Hitler au pouvoir ?",
        "{-ex5}{g4}Pars des documents, puis ajoute le cours. {g4.1}L'industrie allemande dépendait du crédit américain : quand les prêts sont rappelés, "
        "la production industrielle chute de quarante pour cent. Les marches de la faim et les soupes populaires deviennent des scènes ordinaires. "
        "Les nazis s'adressent directement aux chômeurs : Du travail ! La liberté ! Du pain ! Voilà la première moitié : {!la crise a créé le public}la crise a créé le public.",
        "{-g4}{b2}Et la seconde moitié, qu'aucun de ces documents ne montre. {b2.1}Les nazis n'ont jamais dépassé cinquante pour cent des voix. "
        "{b2.2}Ce qui les a portés au pouvoir, c'est la peur du communisme, dans les classes moyennes et chez les partis du centre. "
        "{b2.3}En janvier 1933, les conservateurs nomment Hitler chancelier, en pensant pouvoir se servir de lui. "
        "D'où le bilan : la crise explique le public ; {!un calcul politique a ouvert la porte}un calcul politique a ouvert la porte.",
    ], vis={
        "ex5": dict(type="exo", niveau="dbq", titre="À l'aide des documents et de vos connaissances, dans quelle mesure la crise explique-t-elle l'arrivée de Hitler au pouvoir ?",
                    src="Analyse de documents · aller plus loin", enonce=["Les documents, puis tes connaissances"]),
        "g4": dict(type="globe", code="H1", sc=[13]),
        "b2": dict(type="liste", titre="Ce que les documents ne montrent pas", items=[
            "Jamais plus de 50 % des voix", "La peur du communisme : classes moyennes et partis du centre",
            "Janvier 1933 : les conservateurs nomment Hitler"], x=150, y=150, w=980),
    }),

    # ================================================================ X. trois réflexes face aux documents
    dict(id="sources", chap="Trois sortes de documents", fond="aube", humeur="calme",
         retenir="Réflexes critiques : un dessin de presse (Low, 1933) = une opinion, des perceptions, pas des faits · une photo de commande (Lange, 1936) = une misère réelle, cadrée · des mémoires (Maschmann, 1963) = un témoignage direct, avec le recul.",
         beats=[
        "{ph}Les documents de ce chapitre sont de trois sortes, et chacune appelle son réflexe. {ph.1}D'abord, une photographie de commande. "
        "Migrant Mother, de Dorothea Lange, mars 1936 : Florence Owens Thompson, trente-deux ans, mère de sept enfants, dans un camp de cueilleurs de petits pois à Nipomo, en Californie.",
        "{ph.2}Son intérêt : la misère est réelle. La récolte de petits pois avait gelé, il n'y avait pas de travail, et la famille vivait de légumes gelés et d'oiseaux attrapés par les enfants. "
        "{ph.3}Sa limite : l'image est composée, pas prise au hasard. Lange a fait cinq clichés, en s'approchant de plus en plus, pour une agence fédérale, la Resettlement Administration, "
        "qui voulait gagner l'opinion à l'aide aux plus pauvres.",
        "{-ph}{low}Ensuite, un dessin de presse. {low.1}The Doormat, « le paillasson », de David Low, 1933. Un soldat japonais marche sur la Société des Nations, "
        "{low.2}pendant que ses fonctionnaires s'inclinent, et que le ministre britannique des Affaires étrangères, John Simon, lui poudre le nez avec un nécessaire « pour sauver la face ». "
        "{low.3}Le réflexe : un dessin de presse donne l'opinion d'un contemporain. Des perceptions, pas des faits. Mais Low voyait en 1933 ce que disent aujourd'hui les historiens.",
        "Enfin, des mémoires, comme ceux de Maschmann : un témoignage direct, mais écrit avec le recul. {-low}{ref}{ref.1}Donc, trois réflexes. "
        "{ref.2}Un dessin de presse : une opinion. {ref.3}Une photographie de commande : réelle, mais cadrée. {ref.4}Des mémoires : un témoignage direct, mais tardif.",
    ], vis={
        "ph": dict(type="tableau", img="h1-lange-migrant", de=[1.0, .5, .35], a=[1.25, .5, .3],
                   legende="Migrant Mother, Nipomo, Californie, mars 1936, par Dorothea Lange (Library of Congress, Wikimedia Commons, domaine public)"),
        "low": dict(type="liste", titre="David Low, « The Doormat » (« le paillasson »), 1933 (décrit)", items=[
            "Un soldat japonais marche sur la SDN", "Ses fonctionnaires s'inclinent ; John Simon lui poudre le nez : « pour sauver la face »",
            "Réflexe : l'opinion d'un contemporain, des perceptions, pas des faits"], x=150, y=150, w=980),
        "ref": dict(type="liste", titre="Trois réflexes critiques", marques=["→", "✎", "◉", "❝"], items=[
            "Toujours : nature, auteur, date, intention", "Dessin de presse (Low, 1933) : une opinion, des perceptions",
            "Photo de commande (Lange, 1936) : une misère réelle, cadrée", "Mémoires (Maschmann, 1963) : un témoignage direct, avec le recul"],
            x=150, y=130, w=980),
    }),

    # ================================================================ XI. les notions clés
    dict(id="kt", chap="Les notions clés", fond="nuit", humeur="calme",
         retenir="Dépression économique mondiale (années 1930) : chute durable et mondiale de la production, chômage de masse, déflation (États-Unis 25 % en 1933 ; Allemagne 43,8 % en 1932). Apaisement : céder à un agresseur pour éviter la guerre (Rhénanie 1936, Munich 1938).",
         beats=[
        "{kt1}Une notion clé se maîtrise toujours de la même façon : une définition en une phrase, puis des exemples, des dates, et un lien avec un autre chapitre. "
        "Première notion : la dépression économique mondiale des années 1930. "
        "{!une chute durable et mondiale de la production}Une chute durable et mondiale de la production, avec un chômage de masse et une forte déflation.",
        "{-kt1}{ex6}{ex6.1}Les exemples. Aux États-Unis, quatorze millions de chômeurs, un quart des travailleurs, en 1933. "
        "{ex6.2}En Allemagne, quarante-trois virgule huit pour cent des travailleurs assurés en 1932. {ex6.3}Et le commerce mondial réduit des deux tiers entre 1929 et 1934. "
        "{ex6.4}Le lien : la Dépression a donné aux nazis leur public ; c'est le chapitre deux.",
        "{-ex6}{kt2}Deuxième notion : l'apaisement. {!céder aux exigences d'un agresseur}Céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre.",
        "{-kt2}{g5}{g5.1}Les exemples. Mars 1936 : les troupes allemandes entrent en Rhénanie, et la France et le Royaume-Uni n'interviennent pas. "
        "{g5.2}Septembre 1938 : à Munich, Chamberlain et Daladier acceptent la cession des Sudètes. "
        "{g5.3}Mars 1939 : l'Allemagne occupe Prague, et Munich n'a rien acheté ; le premier septembre, la Pologne est envahie.",
        "{-g5}{rai}Et les raisons, parce qu'on te demandera pourquoi. Six raisons. Le pacifisme. Un empire à tenir, et pas d'argent pour réarmer. Une sympathie pour une Allemagne "
        "jugée injustement traitée par le traité de Versailles, en 1919. Leurs propres difficultés économiques, qui passaient d'abord. L'isolationnisme américain, qui les laissait seuls. Et la peur du communisme, plus forte que la peur du fascisme. "
        "{!Aucune de ces raisons n'est absurde}Aucune de ces raisons n'est absurde.",
    ], vis={
        "kt1": dict(type="def", cles=["durable", "chômage", "déflation"], terme="Notion clé · la dépression économique mondiale (années 1930)",
                    t="Une chute durable et mondiale de la production, avec un chômage de masse et une forte déflation.",
                    etape="Définition · exemples · dates · un lien", x=150, y=180, w=980),
        "ex6": dict(type="liste", titre="Exemples", petit=True, items=[
            "États-Unis 1933 : 14 millions de chômeurs, 25 % des travailleurs", "Allemagne 1932 : 43,8 % des travailleurs assurés",
            "Commerce mondial −66 %, 1929-1934", "Lien : le public des nazis → chapitre 2"], x=150, y=140, w=980),
        "kt2": dict(type="def", cles=["Céder", "éviter"], terme="Notion clé · l'apaisement",
                    t="Céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre.",
                    etape="Royaume-Uni et France, 1935-1938", x=150, y=200, w=980),
        "g5": dict(type="globe", code="H1", sc=[29, 30, 31]),
        "rai": dict(type="liste", titre="Six raisons de l'apaisement", petit=True, items=[
            "Le pacifisme", "Un empire à tenir, pas d'argent pour réarmer", "Une sympathie pour l'Allemagne (Versailles, 1919)",
            "Leurs propres difficultés économiques d'abord", "L'isolationnisme américain", "La peur du communisme plus que du fascisme"],
            x=150, y=100, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Deux exercices : la réponse à une question problématisée, et l'analyse de documents. "
        "{carte.2}La question problématisée : expliquer, c'est « parce que » ; discuter, c'est une hiérarchie et un bilan. "
        "{carte.3}L'analyse de documents : la consigne, la présentation, le contexte, l'explication, l'intérêt et les limites. "
        "{carte.4}Les problématiques : possible, pas inévitable ; l'occasion et l'intention. "
        "{carte.5}Et les notions clés : une définition, des exemples, un lien.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode, le dernier : le récap de tout le chapitre, de Wall Street à la guerre.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LA CRISE À L'ÉPREUVE", branches=[
            dict(t="Deux exercices", items=["question problématisée", "analyse de documents"]),
            dict(t="La question problématisée", items=["expliquer : « parce que »", "discuter : hiérarchie, bilan"]),
            dict(t="L'analyse de documents", items=["présenter, situer, expliquer", "intérêt · limites"]),
            dict(t="Problématiques", items=["possible, pas inévitable", "l'occasion et l'intention"]),
            dict(t="Notions clés", items=["Dépression", "Apaisement"])]),
        "fin": dict(type="mot", t="Prochain épisode : le récap", g="Épisode 6 · tout le chapitre", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Que contient l'introduction d'une réponse à une question problématisée ?", r=["Accroche, définitions, contexte, problématique, annonce du plan",
         "La réponse seule", "Un résumé de tout le cours", "Une citation et la conclusion"], ok=0, voir="intro",
         ex="Cinq temps : accroche, définition des termes, contexte, problématique, plan."),
    dict(q="Dans quel ordre mène-t-on une analyse de document ?", r=["Consigne, présentation, contexte et explication, intérêt et limites",
         "Résumé, puis avis personnel", "Intérêt et limites, puis présentation", "Description seule"], ok=0, voir="ora",
         ex="On lit la consigne, on présente et on situe le document, on l'explique, puis on en montre l'intérêt et les limites."),
    dict(q="Que faut-il donner pour présenter un document ?", r=["Sa nature, son auteur, sa date, son destinataire", "Un résumé complet",
         "Ton opinion sur l'auteur", "Une conclusion"], ok=0, voir="str",
         ex="Ensuite viennent le contexte, l'explication, puis l'intérêt et les limites."),
    dict(q="Laquelle est une vraie LIMITE du document 2 (le graphique du chômage allemand) ?", r=["Il ne compte que les travailleurs assurés",
         "C'est un graphique", "Il s'arrête en 1933", "Il montre un pic en 1932"], ok=0, voir="rep",
         ex="Il laisse de côté le reste de la population active. Ses autres traits (un graphique, une fin en 1933, un pic en 1932) ne sont pas des limites en soi."),
    dict(q="Dans le sujet sur les causes du krach, quel facteur est le déclencheur ?", r=["La spéculation", "Le tarif Smoot-Hawley",
         "L'étalon-or", "Le plan Dawes"], ok=0, voir="hi",
         ex="La spéculation explique la soudaineté ; la surproduction et les inégalités expliquent la profondeur."),
    dict(q="Comment juger l'efficacité du tarif douanier de 1930 ?", r=["Au regard de ses propres buts : protéger les agriculteurs et l'industrie",
         "Au regard de ce que savent aujourd'hui les économistes", "Au nombre de produits taxés", "À la seule réaction du Canada"], ok=0, voir="eff",
         ex="Il échoue même au regard de ses buts : les prix agricoles continuent de baisser, le chômage d'augmenter."),
    dict(q="Quelle phrase résume le mieux la problématique 1 (les démocraties responsables) ?", r=["Elles ont rendu la guerre possible, pas inévitable",
         "Elles seules ont causé la guerre", "Elles n'ont aucune responsabilité", "Elles voulaient la guerre"], ok=0, voir="cc3",
         ex="Une responsabilité par omission (isolationnisme, protectionnisme, apaisement) ; la guerre a été voulue par les agresseurs."),
    dict(q="Qu'est-ce que l'apaisement ?", r=["Céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre", "Relever les droits de douane pour protéger l'industrie",
         "Refuser de reconnaître les conquêtes par la force", "Vendre des armes payées comptant"], ok=0, voir="kt2",
         ex="Rhénanie 1936, Munich 1938. Les autres réponses désignent le protectionnisme, la doctrine Stimson et le « cash and carry »."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 1 « Le krach de 1929 et ses conséquences » : sujets, problématiques et notions clés ; le dossier documentaire (documents 2 et 5) ; les descriptions de Migrant Mother et du dessin de David Low « The Doormat ».",
    "Le sujet « Pourquoi le krach… » et les modèles de réponse ont été écrits pour cette vidéo.",
    "Photographie : Dorothea Lange, Migrant Mother, Nipomo, Californie, mars 1936 (Library of Congress ; Wikimedia Commons, domaine public).",
    "Carte animée du chapitre : la carte animée du site.",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
