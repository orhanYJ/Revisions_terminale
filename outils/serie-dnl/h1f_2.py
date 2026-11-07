"""Histoire · chapitre 1 « Le krach de 1929 et ses conséquences » — série vidéo, édition française, épisode 2 :
« D'un krach américain à une crise mondiale » (parties I.2 et I.3 du cours).

Édition française de h1_2.py (cahier des charges : EDITION_FR.md) : mêmes scènes, mêmes visuels, mêmes repères,
mêmes globes (la carte animée passe d'elle-même en français). Chaîne : outils/serie-philo/generer.py h1f_2 ;
sortie dans dnl/serie/.
Carte animée H1 (dnl/cartes/H1.html), scènes utilisées (ordre chronologique de la carte) :
  3 plan Dawes · 5 le krach · 6 des vies brisées · 7 la périphérie et la chute des prix · 8 les faillites bancaires ·
  9 le rappel des prêts · 10 une crise durable dans le monde dominé · 11 les Hoovervilles · 12 un traumatisme inégal ·
  17 l'effet domino en Europe · 19 l'étalon-or · 25 le Dust Bowl · 28 Migrant Mother
Contenu : CHAPTERS.H1 (champs fr), section I.2 (cinq idées) et section I.3 (cinq idées) ; chiffres du cours.
Masse salariale ≈ −60 %, salaire horaire ≈ −20 % (cours corrigé).
Pauses « À toi » : une réponse à une question problématisée (plan en trois parties), puis une analyse de document
sur Migrant Mother (présenter, situer, expliquer, intérêt et limites, bilan critique).
Citations de Dorothea Lange : traduction du cours (récit publié dans Popular Photography, février 1960).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-2"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 2
TITRE = "D'un krach américain à une crise mondiale"
SUIVANT = "Épisode 3 · Nationalisme économique et réponses politiques"
PRONONCIATION = {"Creditanstalt": "Crédit-anne-chtalt", "Hoover": "Houveur", "Hooverville": "Houveur-ville",
                 "Hoovervilles": "Houveur-ville", "Dawes": "Dôze", "Dust": "Deust", "Bowl": "Bôle",
                 "Lange": "Lang", "Dorothea": "Doro-téa", "Migrant": "Maï-grannt", "Mother": "Meu-zeur",
                 "Owens": "Ô-ouènz", "Thompson": "Tomm-sonne", "Capone": "Ca-pône", "Stratford": "Stratt-feurd",
                 "Resettlement": "Ri-sétteul-mennt", "Farm": "Farme", "Security": "Si-kiou-riti",
                 "White": "Ouaïte", "Angel": "Éine-djel", "Roosevelt": "Rouz-vèlt", "Nipomo": "Ni-pô-mô"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Octobre 1929. En quelques jours, la Bourse de New York s'effondre. Dans l'épisode précédent, tu as vu comment, et pourquoi.",
        "{-q1}{q2}Mais un krach, ça dure quelques jours. Alors comment une panique dans une rue de New York "
        "devient-elle une dépression de dix ans, de Berlin à Santiago ?",
        "{-q2}{q3}Et qu'est-ce que la crise a fait aux gens ? Aux familles qui ont perdu leur travail, leur épargne, leur maison… et leur terre ?",
        "{-q3}{-g0}{plan}Cette série couvre tout le chapitre en six épisodes. {plan.1}Le premier, c'était le grand krach lui-même. "
        "{plan.2}Aujourd'hui : d'un krach américain à une crise mondiale, et l'un des traumatismes fondateurs du vingtième siècle. "
        "{plan.3}Ensuite, le nationalisme économique et les réponses politiques, {plan.4}les démocraties et l'ordre libéral, "
        "{plan.5}un épisode pour l'examen, la composition et l'analyse de document, {plan.6}et un récapitulatif.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="note", terme="Octobre 1929", t="Un krach à New York.", x=480, y=470, w=760),
        "q2": dict(type="note", terme="La question", t="Comment devient-il une crise mondiale ?", x=480, y=470, w=760),
        "q3": dict(type="note", terme="Et les gens ?", t="Qu'a-t-il fait à leur vie ?", x=480, y=470, w=760),
        "plan": dict(type="liste", titre="Le krach de 1929 et ses conséquences, en six épisodes", items=[
            "Le grand krach de 1929 (partie I.1)", "D'un krach américain à une crise mondiale (parties I.2 – I.3)",
            "Nationalisme économique et réponses politiques (II.1 – II.2)", "Les démocraties et l'ordre libéral (II.3)",
            "La crise à l'examen : composition et analyse de document", "Récapitulatif"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Chapitre 1 · Épisode 2", t="D'un krach américain à une crise mondiale",
                      sous="banques · prêts · or · un traumatisme du vingtième siècle"),
    }),

    # ================================================================ partie chronologique
    dict(id="chrono", chap="La crise sur la carte", fond="nuit", humeur="tension",
         retenir="1924 plan Dawes · oct. 1929 krach · 1930–1932 faillites bancaires, prêts rappelés · mai–sept. 1931 dominos en Europe · 1931–1936 sorties de l'or · 1935 Dust Bowl · 1936 Migrant Mother.",
         beats=[
        "{g1}Suivons d'abord la crise sur la carte, date par date. {g1.1}Tout commence avant le krach, en mille neuf cent vingt-quatre, avec le plan Dawes. "
        "L'Allemagne reçoit un emprunt de huit cents millions de marks-or, surtout de l'argent américain. Avec lui, elle paie ses réparations à la France et au Royaume-Uni. "
        "Et la France et le Royaume-Uni remboursent leurs dettes de guerre aux États-Unis. Tout repose sur le crédit américain.",
        "{g1.2}Octobre 1929 : le krach. Le jeudi noir, puis le lundi et le mardi noirs. Tout le monde vend, personne n'achète.",
        "{g1.3}De 1929 à 1933, des millions de vies américaines sont brisées, sans aucun filet de sécurité.",
        "{g1.4}Loin de New York, les pays qui vendent des matières premières sont frappés par la chute des prix. "
        "Le Brésil vit du café. Le Chili vit du nitrate.",
        "{g1.5}À partir de 1930, les banques tombent les unes après les autres : environ cinq mille avant 1932. "
        "C'est le moment où le krach devient la Grande Dépression.",
        "{g1.6}Et les banques américaines rappellent leurs prêts à l'Europe. L'argent qui faisait tenir les économies européennes repart de l'autre côté de l'Atlantique.",
        "{g1.7}Dans le monde dominé, la crise s'installe : en Inde, en Australie, en Nouvelle-Zélande.",
        "{g1.8}Dans les villes américaines, les familles expulsées construisent des bidonvilles. On les appelle les Hoovervilles.",
        "{g1.9}Le traumatisme est mondial… mais inégal : l'Union soviétique, hors du commerce mondial, est à peine touchée.",
        "{-g1}{g2}{g2.1}Retour en Europe, en 1931. Les dominos tombent : la plus grande banque autrichienne en mai, les banques allemandes en juillet, "
        "et en septembre, le Royaume-Uni quitte l'étalon-or.",
        "{g2.2}De 1931 à 1936, les pays quittent l'or l'un après l'autre : le Royaume-Uni et le Japon en 1931, les États-Unis en 1933, "
        "la France seulement en 1936. Plus un pays sort tôt, plus il se redresse tôt.",
        "{g2.3}En avril 1935, dans les Grandes Plaines, les tempêtes de poussière du Dust Bowl changent le jour en nuit.",
        "{g2.4}Et en mars 1936, dans un camp de Californie, la photographe Dorothea Lange photographie une mère et ses enfants. "
        "L'image devient le visage de la Dépression.",
        "{-g2}{fr1}La chronologie : {fr1.1}1924, {fr1.2}1929, {fr1.3}1930, {fr1.4}1931, {fr1.5}1935, {fr1.6}1936. Maintenant, expliquons.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[3, 5, 6, 7, 8, 9, 10, 11, 12]),
        "g2": dict(type="globe", code="H1", sc=[17, 19, 25, 28]),
        "fr1": dict(type="frise", items=[
            dict(nom="Plan Dawes", d=1924), dict(nom="Le krach", d=1929, q="24–29 octobre"),
            dict(nom="Faillites bancaires", d=1930), dict(nom="Dominos", d=1931, q="Vienne · Berlin · Londres"),
            dict(nom="Dust Bowl", d=1935), dict(nom="Migrant Mother", d=1936, q="Dorothea Lange")]),
    }),

    # ================================================================ I.2 idée 1 : les banques
    dict(id="banques", chap="I.2 · Quand les banques tombent", fond="nuit", humeur="tension",
         retenir="La Grande Dépression commence vraiment quand de nombreuses banques font faillite. Un krach dure des jours ; une dépression, c'est le système bancaire qui le transmet à l'économie réelle. Pas d'assurance des dépôts avant 1933 : environ 5 000 banques en faillite avant 1932.",
         beats=[
        "{m1}Deuxième partie du chapitre : du krach américain à une crise financière mondiale. "
        "Le cours insiste sur une phrase. Apprends-la par cœur : la Grande Dépression commence vraiment "
        "quand de nombreuses banques font faillite. C'est la charnière de tout le chapitre.",
        "{-m1}{spi}Pourquoi ? À cause d'une spirale. {spi.1}D'abord, la confiance est perdue. {spi.2}On ne croit plus aux banques, "
        "alors on retire son épargne. {spi.3}Et plus les gens retirent, plus les banques tombent… donc plus les gens retirent.",
        "{spi.4}Puis la spirale gagne l'économie réelle. Incertains de leurs revenus futurs, entreprises et ménages réduisent leurs dépenses. "
        "{spi.5}Alors la production chute. {spi.6}Les ouvriers sont licenciés, ou moins payés… donc ils achètent encore moins. Et la spirale repart.",
        "{spi.7}Côté finance, les investisseurs font faillite : leur actif vaut désormais moins que leur passif, c'est-à-dire leurs dettes. "
        "Et l'investissement s'arrête.",
        "{-spi}{ex1}Voici l'exemple qui rend tout cela concret. Avant 1933, il n'existe {!aucune assurance des dépôts}aucune assurance des dépôts "
        "aux États-Unis. Quand une banque tombe, l'épargne de ses clients disparaît, tout simplement. Une simple rumeur peut donc vider une banque. "
        "Voilà pourquoi environ cinq mille banques ont fait faillite avant 1932.",
        "{-ex1}{dc}Retiens cette distinction. Un krach est un événement financier : il dure des jours. "
        "Une dépression, c'est ce qui arrive quand le système bancaire transmet le krach à l'économie réelle : elle dure des années.",
    ], vis={
        "m1": dict(type="mot", t="« La Grande Dépression commence vraiment quand de nombreuses banques font faillite. »",
                   g="la phrase du cours · la charnière du chapitre", y=230, taille=50),
        "spi": dict(type="liste", titre="La spirale des faillites bancaires", cles=["confiance", "retire", "tombent", "dépenses", "licenciés", "faillite"], items=[
            "La confiance est perdue", "Les épargnants retirent leur argent", "Plus de retraits → plus de banques tombent",
            "Entreprises et ménages réduisent leurs dépenses", "La production chute", "Ouvriers licenciés ou moins payés → ils achètent moins",
            "Investisseurs en faillite (actif < passif) : plus d'investissement"], x=150, y=80, w=980),
        "ex1": dict(type="note", terme="Exemple · aucun filet pour les épargnants", cles=["dépôts", "rumeur", "5 000"],
                    t="Pas d'assurance des dépôts avant 1933 : quand une banque tombe, l'épargne de ses clients disparaît. Une simple rumeur peut vider une banque.",
                    etape="Environ 5 000 banques en faillite avant 1932.", x=170, y=200, w=940),
        "dc": dict(type="cols", g="Un krach", gq="un événement financier · il dure des jours · octobre 1929",
                   d="Une dépression", dq="les banques le transmettent à l'économie réelle · elle dure des années", vs="≠"),
    }),

    # ================================================================ I.2 idée 2 : deux canaux
    dict(id="canaux", chap="I.2 · Deux canaux", fond="nuit", humeur="tension",
         retenir="Causes à court terme : les liens internationaux — les banques américaines rappellent leurs prêts, les banques européennes s'effondrent, l'effondrement retraverse l'Atlantique. Causes profondes : des faiblesses partagées (surproduction, baisse des prix, revenus agricoles, surinvestissement) reliées par l'étalon-or.",
         beats=[
        "{q4}Deuxième idée. Comment une crise américaine a-t-elle traversé l'océan ? Le cours distingue deux types de causes, "
        "et cette distinction mérite d'être réutilisée dans toute composition.",
        "{-q4}{cc}D'abord, les causes {!à court terme}à court terme : les liens internationaux. Les banques américaines rappellent brutalement leurs prêts "
        "aux banques européennes. Les banques européennes s'effondrent. Et comme elles détenaient aussi des actifs dans les banques américaines, "
        "l'effondrement retraverse l'Atlantique.",
        "{-cc}{lt}Ensuite, les causes {!profondes}profondes. {lt.1}Partout dans le monde, les économies avaient déjà les mêmes faiblesses. "
        "La surproduction. {lt.2}La baisse des prix. {lt.3}La baisse des revenus agricoles. "
        "{lt.4}Le surinvestissement dans l'industrie, avec un excès de confiance. "
        "{lt.5}Et, pour les relier toutes : l'étalon-or. On y revient dans un instant.",
        "{-lt}{g3}{g3.1}L'exemple : quatre mois de dominos. En mai 1931, la Creditanstalt, "
        "la plus grande banque autrichienne, fait faillite. En juillet, les banques allemandes suivent. Et en septembre, le Royaume-Uni quitte l'étalon-or.",
        "{-g3}{tc}La crise voyage donc par deux canaux à la fois : {tc.1}un choc brutal, le rappel des prêts américains, "
        "{tc.2}qui tombe sur des économies déjà fragiles.",
    ], vis={
        "q4": dict(type="question", t="Comment une crise américaine a-t-elle traversé l'océan ?"),
        "cc": dict(type="note", terme="Causes à court terme · les liens internationaux", cles=["rappellent", "effondrent", "retraverse"],
                   t="Les banques américaines rappellent brutalement leurs prêts aux banques européennes → celles-ci s'effondrent → l'effondrement retraverse l'Atlantique.",
                   etape="Les banques européennes détenaient aussi des actifs dans les banques américaines.", x=170, y=200, w=940),
        "lt": dict(type="liste", titre="Causes profondes : des faiblesses partagées", items=[
            "La surproduction", "La baisse des prix", "La baisse des revenus agricoles",
            "Le surinvestissement dans l'industrie, l'excès de confiance", "Pour les relier : l'étalon-or"], x=170, y=120, w=940),
        "g3": dict(type="globe", code="H1", sc=[17]),
        "tc": dict(type="cols", g="Un choc brutal", gq="le rappel des prêts américains (court terme)",
                   d="Des économies fragiles", dq="surproduction, baisse des prix, or (long terme)", vs="+"),
    }),

    # ================================================================ I.2 idée 3 : le plan Dawes
    dict(id="dawes", chap="I.2 · Le plan Dawes", fond="nuit", humeur="tension",
         retenir="Plan Dawes (1924) : 800 millions de marks-or prêtés à l'Allemagne → réparations jusqu'à 2,5 milliards de marks par an à la France et au Royaume-Uni → dettes de guerre remboursées aux États-Unis. La solvabilité de l'Europe dépend du crédit américain : le rappel des prêts casse les trois côtés.",
         beats=[
        "{g4}Troisième idée : le plan Dawes avait lié les finances européennes au crédit américain. Reviens aux années d'après-guerre. "
        "L'Allemagne doit des réparations à la France et au Royaume-Uni. Et la France et le Royaume-Uni doivent des dettes de guerre aux États-Unis. C'est l'impasse.",
        "{g4.1}Le plan Dawes, en 1924, débloque l'impasse en plaçant l'argent américain au début de la chaîne.",
        "{tri}Suis le circuit. {tri.1}Un : un emprunt de huit cents millions de marks-or pour l'Allemagne, placé surtout à New York. "
        "{tri.2}Deux : les réparations allemandes à la France et au Royaume-Uni, qui montent à deux milliards et demi de marks par an en 1928 et 1929. "
        "{tri.3}Trois : la France et le Royaume-Uni remboursent leurs dettes de guerre à Washington. L'argent fait le tour du triangle.",
        "{-tri}{-g4}{daw}Charles Dawes, le banquier à l'origine du plan, reçoit pour cela le prix Nobel de la paix en 1925, qu'il partage, et devient vice-président "
        "des États-Unis. Et le système fonctionne… tant que l'argent américain continue de couler.",
        "{-daw}{rup}Regarde maintenant ce qui se passe après octobre 1929. {rup.1}Frappées par le krach, les banques américaines rappellent leurs prêts : "
        "le premier côté du triangle casse. {rup.2}Privée du crédit américain, l'Allemagne ne peut plus payer ses réparations : "
        "le deuxième côté cède. {rup.3}Sans réparations, la France et le Royaume-Uni cessent de rembourser leurs dettes de guerre : le troisième côté cède.",
        "{-rup}{le}C'est la leçon du plan Dawes. La crise a traversé l'Atlantique par la chaîne des dettes, "
        "pas seulement par la panique. Dans une composition, c'est ton meilleur exemple d'interdépendance.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[3]),
        "tri": dict(type="liste", titre="Le circuit Dawes, 1924 – 1929", cles=["800 millions", "2,5 milliards", "dettes de guerre"], items=[
            "États-Unis → Allemagne : un emprunt de 800 millions de marks-or (1924)", "Allemagne → France et Royaume-Uni : réparations, jusqu'à 2,5 milliards de marks par an",
            "France et Royaume-Uni → États-Unis : remboursement des dettes de guerre"], x=660, y=330, w=580, petit=True, bande=True),
        "daw": dict(type="note", terme="Charles G. Dawes", cles=["Nobel", "vice-président"],
                    t="Auteur du plan de 1924 ; prix Nobel de la paix 1925 (partagé), puis vice-président des États-Unis (1925–1929).",
                    etape="Le plan fonctionne — tant que le crédit américain continue de couler.", x=170, y=210, w=940),
        "rup": dict(type="liste", titre="Après octobre 1929 : le triangle casse", items=[
            "✕ Les banques américaines rappellent leurs prêts", "✕ L'Allemagne ne peut plus payer ses réparations",
            "✕ La France et le Royaume-Uni cessent de rembourser leurs dettes de guerre"],
            x=170, y=150, w=940),
        "le": dict(type="mot", t="La chaîne des dettes", g="la crise traverse l'Atlantique par les dettes, pas seulement par la panique", y=260, taille=84),
    }),

    # ================================================================ I.2 idée 4 : l'étalon-or
    dict(id="or", chap="I.2 · L'étalon-or", fond="nuit", humeur="tension",
         retenir="L'étalon-or est la courroie de transmission : la Réserve fédérale relève ses taux pour défendre le dollar, l'or quitte les autres pays, qui doivent relever les leurs. Sortir de l'or est la porte de sortie : Royaume-Uni sept. 1931, Japon déc. 1931, États-Unis 1933, France 1936. Plus tôt sorti, plus tôt redressé.",
         beats=[
        "{def1}Quatrième idée, la plus technique. {!courroie de transmission}L'étalon-or est la courroie de transmission. "
        "Avec l'étalon-or, la plupart des pays fixent la valeur de leur monnaie en or.",
        "{-def1}{mec}Voici le mécanisme. {mec.1}Des spéculateurs nerveux commencent à échanger leurs dollars contre de l'or. "
        "{mec.2}Pour préserver la valeur du dollar, la Réserve fédérale, la banque centrale américaine, relève ses taux d'intérêt. "
        "{mec.3}Des taux américains plus élevés attirent l'or de tous les pays où les taux sont plus bas. "
        "{mec.4}Alors des pays que le krach n'a pas touchés sont forcés de relever leurs propres taux, pour garder leur or.",
        "{mec.5}Et c'est le pire remède possible pour une économie qui ralentit déjà. L'argent plus cher, c'est moins d'investissement "
        "et moins de dépenses. Un système conçu pour garantir la stabilité propage la contraction à tout le monde.",
        "{-mec}{fr2}La porte de sortie, c'est donc de quitter l'or. {fr2.1}Le Royaume-Uni, en septembre 1931. {fr2.2}Le Japon, en décembre 1931. "
        "{fr2.3}Les États-Unis, sous Roosevelt, en 1933. {fr2.4}Et la France, seulement en 1936.",
        "{-fr2}{g5}{g5.1}La règle est simple : plus un pays sort tôt, plus il se redresse tôt. La France, sortie la dernière, se redresse la dernière.",
        "{-g5}{ex2}L'exemple compare deux voisins. {ex2.1}La production allemande repart fortement après mille neuf cent trente-deux, "
        "quand la dépense d'État remplace la contrainte monétaire. {ex2.2}La France défend la valeur-or du franc jusqu'en mille neuf cent trente-six. "
        "C'est l'économie développée la moins performante de la décennie.",
    ], vis={
        "def1": dict(type="def", terme="L'étalon-or", cles=["fixent", "or"],
                     t="La plupart des pays fixent la valeur de leur monnaie en or.",
                     etape="Dans la crise, il devient la courroie de transmission de la contraction.", x=170, y=200, w=940),
        "mec": dict(type="liste", titre="Comment l'or propage la crise", cles=["or", "taux d'intérêt", "relever", "pire"], items=[
            "Des spéculateurs échangent leurs dollars contre de l'or", "La Réserve fédérale relève ses taux d'intérêt pour défendre le dollar",
            "Des taux américains plus hauts attirent l'or des autres pays", "Ceux-ci doivent relever leurs propres taux",
            "Argent plus cher → moins d'investissement, moins de dépenses : le pire remède"], x=150, y=110, w=980),
        "fr2": dict(type="frise", items=[
            dict(nom="Royaume-Uni · sept.", d=1931), dict(nom="Japon", d=1931, q="décembre"),
            dict(nom="États-Unis · Roosevelt", d=1933), dict(nom="France", d=1936, q="la dernière")]),
        "g5": dict(type="globe", code="H1", sc=[19]),
        "ex2": dict(type="cols", g="Allemagne", gq="la production repart fortement après 1932 : la dépense d'État remplace la contrainte monétaire",
                    d="France", dq="défend la valeur-or du franc jusqu'en 1936 : l'économie développée la moins performante de la décennie", vs="≠"),
    }),

    # ================================================================ I.2 idée 5 : effet domino et périphérie
    dict(id="domino", chap="I.2 · Dominos et chute des prix", fond="nuit", humeur="tension",
         retenir="L'Europe, par effet domino : Allemagne et Autriche d'abord (plus de réparations), puis les banques britanniques, puis la France en 1932. La périphérie, par la chute des prix : le Brésil brûle quelque 78 millions de sacs de café (1931–1944) ; les recettes du nitrate chilien chutent de plus de 80 % (1929–1932).",
         beats=[
        "{m5}Cinquième idée : la Dépression frappe l'Europe par effet domino, et le reste du monde par la chute des prix. {-m5}{dom}L'Europe d'abord. "
        "{dom.1}Les économies allemande et autrichienne sont touchées les premières, et elles deviennent incapables de payer leurs réparations. "
        "{dom.2}Par effet domino, les banques britanniques, qui avaient investi en Allemagne, sont vite atteintes. "
        "{dom.3}La France, moins endettée envers les États-Unis, n'est touchée qu'en 1932, quand les réparations allemandes cessent d'arriver régulièrement.",
        "{-dom}{g6}{g6.1}Maintenant, la périphérie : les pays moins développés. Deux coups : la fin des prêts américains, "
        "et la baisse des importations de matières premières. Comme les prix des matières premières continuent de baisser, leurs exportations s'effondrent.",
        "{g6.2}La crise frappe durablement l'Amérique latine, le Canada, l'Inde, la Nouvelle-Zélande et l'Australie.",
        "{-g6}{per}Deux exemples. {per.1}Le Brésil, dont l'économie dépend du café, en brûle quelque soixante-dix-huit millions de sacs "
        "entre 1931 et 1944, pour soutenir le prix. {per.2}Le Chili, qui vit du nitrate, voit ses recettes d'exportation s'effondrer de plus de "
        "quatre-vingts pour cent entre 1929 et 1932. {per.3}La leçon : {!aucun amortisseur}un pays qui ne vend qu'une denrée n'a aucun amortisseur.",
        "Rassemblons toute la deuxième partie. {-per}{cha}Voici la chaîne du cours, {cha.1}étape par étape. "
        "Le krach de Wall Street, octobre 1929 : les cours des actions s'effondrent. {cha.2}Les faillites bancaires : le crédit se tarit, l'épargne est détruite. "
        "{cha.3}Les États-Unis rappellent leurs prêts à l'étranger : l'Europe, surtout l'Allemagne, perd les capitaux américains. "
        "{cha.4}Le protectionnisme : des droits de douane, et une chaîne de représailles. Ce sera l'épisode trois. "
        "{cha.5}Le commerce mondial s'effondre : sa valeur baisse d'environ deux tiers entre 1929 et 1934. "
        "{cha.6}Et le résultat : une dépression mondiale dans les années trente, avec un chômage de masse et la déflation.",
    ], vis={
        "m5": dict(type="mot", t="Dominos et chute des prix", g="l'Europe par effet domino · le reste du monde par la chute des prix", y=260, taille=72),
        "dom": dict(type="liste", titre="L'Europe : l'effet domino", items=[
            "Allemagne et Autriche touchées d'abord → plus de réparations", "Les banques britanniques, investies en Allemagne, touchées à leur tour",
            "La France, moins endettée envers les États-Unis, touchée seulement en 1932"], x=170, y=150, w=940),
        "g6": dict(type="globe", code="H1", sc=[7, 10]),
        "per": dict(type="liste", titre="La périphérie : la chute des prix", cles=["café", "nitrate", "amortisseur"], items=[
            "Le Brésil brûle quelque 78 millions de sacs de café (1931–1944)", "Chili : recettes d'exportation du nitrate en baisse de plus de 80 % (1929–1932)",
            "Une seule denrée = aucun amortisseur"], x=170, y=150, w=940),
        "cha": dict(type="liste", titre="Comment le krach devient une dépression mondiale", items=[
            "Krach de Wall Street (oct. 1929) : les cours des actions s'effondrent", "Faillites bancaires : le crédit se tarit, l'épargne est détruite",
            "Les États-Unis rappellent leurs prêts : l'Europe perd les capitaux américains", "Protectionnisme : droits de douane et représailles",
            "Le commerce mondial s'effondre : environ −2/3 en valeur (1929–1934)", "Dépression mondiale (années 1930) : chômage de masse, déflation"],
            x=150, y=100, w=980),
    }),

    # ================================================================ I.2 : hiérarchiser les causes + pause 1
    dict(id="causes", chap="Hiérarchiser les causes", fond="aube", humeur="calme",
         retenir="Pèse chaque facteur : décisif, aggravant ou secondaire — et donne toujours l'argument ET sa limite. La spéculation explique la brutalité de la chute, pas sa durée de dix ans.",
         beats=[
        "{wk}Le cours propose un exercice : hiérarchiser les causes. Pour chacun de neuf facteurs, décide : "
        "{!décisif}décisif, aggravant, ou secondaire. Puis mets ton choix à l'épreuve d'un argument… et de sa limite. "
        "Un bon paragraphe de composition contient les deux.",
        "{-wk}{fac}Quatre exemples. {fac.1}La spéculation : acheter à crédit a multiplié les pertes. "
        "Mais elle explique la brutalité de la chute, pas sa durée de dix ans. "
        "{fac.2}La surproduction : on produisait plus que les salaires ne permettaient d'acheter. Mais c'est une faiblesse de fond, pas un déclencheur : elle existait depuis des années.",
        "{fac.3}L'inégale répartition des richesses : la consommation de masse ne pouvait pas absorber la production de masse. "
        "Mais elle explique la profondeur de la Dépression mieux que la date du krach. "
        "{fac.4}Et la panique : vendre parce que les autres vendent a changé une baisse en effondrement. Mais la panique est une conséquence de la chute, elle ne peut pas en être l'origine.",
        "{-fac}{ex3}À toi, maintenant. Une question problématisée, écrite pour cette vidéo : "
        "comment le krach de Wall Street devient-il une dépression mondiale ?",
        "{-ex3}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Voici un plan modèle, en trois raisons. {rep1.1}D'abord, parce que les banques font faillite et transmettent le krach à l'économie réelle : "
        "environ cinq mille avant 1932, sans assurance des dépôts. {rep1.2}Ensuite, parce que l'Europe dépend du crédit américain : "
        "le circuit Dawes casse quand les prêts sont rappelés, et les dominos tombent de Vienne à Londres en 1931. "
        "{rep1.3}Enfin, à cause de l'or et de la chute des prix. L'étalon-or force chaque pays à relever ses taux d'intérêt. "
        "Et la chute des prix ruine les exportateurs de matières premières, comme le Brésil et le Chili.",
    ], vis={
        "wk": dict(type="note", terme="Exercice · hiérarchiser les causes", cles=["décisif", "aggravant", "secondaire"],
                   t="Neuf facteurs. Pour chacun : décisif, aggravant ou secondaire ? Puis l'épreuve de l'argument et de sa limite.",
                   etape="Un bon paragraphe de composition contient les deux.", x=170, y=200, w=940),
        "fac": dict(type="liste", titre="L'argument … et sa limite", items=[
            "Spéculation : le crédit multiplie les pertes — explique la brutalité, pas la décennie",
            "Surproduction : la production dépasse les salaires — une faiblesse de fond, pas un déclencheur",
            "Inégalités : la consommation de masse n'absorbe pas la production de masse — la profondeur, pas la date",
            "Panique : change une baisse en effondrement — une conséquence, pas une origine"], x=130, y=120, w=1020),
        "ex3": dict(type="exo", niveau="essay", titre="Comment le krach de Wall Street devient-il une dépression mondiale ?",
                    src="Question écrite pour cette vidéo", enonce=["Réponse à une question problématisée · trois parties, chacune avec un exemple précis"]),
        "pa1": dict(type="pause", t="Trouve trois raisons, chacune avec un exemple précis tiré du cours.",
                    sous="Mets la vidéo en pause, écris tes trois raisons, puis relance pour voir un modèle."),
        "rep1": dict(type="liste", titre="Un plan modèle", cles=["parce que"], items=[
            "Parce que les banques font faillite : ≈ 5 000 avant 1932, sans assurance des dépôts",
            "Parce que l'Europe dépend du crédit américain : le circuit Dawes casse, dominos en 1931",
            "Parce que l'or et la chute des prix propagent la crise : taux d'intérêt, Brésil, Chili"], x=150, y=140, w=980),
    }),

    # ================================================================ I.3 idée 1 : emplois, salaires, épargne
    dict(id="vies", chap="I.3 · Sans filet de sécurité", fond="guerre", humeur="mystere",
         retenir="États-Unis : production −40 %, 14 millions de chômeurs (25 % des actifs ; 3 % en 1929), 5 000 banques en faillite — et ni assurance chômage, ni sécurité sociale, ni retraite publique avant 1935.",
         beats=[
        "{pain}La troisième partie du chapitre a un titre fort : {!traumatismes fondateurs}l'un des traumatismes fondateurs du vingtième siècle. "
        "Nous quittons les banques, pour regarder les gens.",
        "{-pain}{gr}{gr.1}D'abord, le chômage aux États-Unis. Trois pour cent en 1929. Vingt-cinq pour cent en 1933. "
        "Un actif sur quatre : quatorze millions d'Américains.",
        "{-gr}{chi}Et les autres chiffres du cours. {chi.1}La production industrielle et agricole chute de quarante pour cent. "
        "{chi.2}La masse salariale baisse d'environ soixante pour cent. Le salaire horaire, lui, ne baisse que d'environ un cinquième, "
        "mais des millions de travailleurs perdent leur emploi, ou passent au chômage partiel. {chi.3}Cinq mille banques ont fait faillite. "
        "{chi.4}Les prix agricoles se sont effondrés, à cause de la surproduction, de la sécheresse et du Dust Bowl. "
        "{chi.5}Et les exportations américaines s'effondrent, car les partenaires ferment leurs marchés.",
        "{-chi}{fil}Mais le pire, c'est ceci. {fil.1}Il n'existe aucune assurance chômage fédérale. {fil.2}Pas de sécurité sociale. "
        "{fil.3}Pas de retraite publique : la première retraite fédérale date de 1935. {fil.4}Et pas d'assurance des dépôts avant 1933.",
        "{-fil}{fm}Une famille pouvait passer de l'aisance à la misère en un mois. "
        "Ici, le mot {!dépression}dépression ne désigne donc pas une statistique : c'est la disparition de tous les filets de sécurité à la fois.",
    ], vis={
        "pain": dict(type="tableau", img="h1-soupkitchen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .45],
                     legende="Chômeurs devant une soupe populaire, Chicago, février 1931 (US National Archives, domaine public)"),
        "gr": dict(type="graphe", titre="Le chômage aux États-Unis (chiffres du cours)", x=300, y=110, w=680, h=500,
                   ax=dict(x=[1928.5, 1933.5], y=[0, 30], gx=[1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30], lx="année", ly="% des actifs"),
                   el=[dict(type="droite", pts=[[1929, 3], [1933, 25]], c="ca", tir=True, dur=1.6),
                       dict(type="points", pts=[[1929, 3], [1933, 25]], c="sa", lbl="3 % → 25 % · 14 millions", lp=[1930.6, 22])]),
        "chi": dict(type="liste", titre="Les États-Unis, 1929 – 1933 (cours)", items=[
            "Production industrielle et agricole : −40 %", "Masse salariale : environ −60 % (salaire horaire : environ −20 %)", "5 000 banques en faillite",
            "Les prix agricoles s'effondrent : surproduction, sécheresse, Dust Bowl", "Les exportations s'effondrent : marchés fermés"], x=150, y=110, w=980),
        "fil": dict(type="liste", titre="Aucun filet de sécurité", items=[
            "Pas d'assurance chômage fédérale", "Pas de sécurité sociale", "Pas de retraite publique (la première, fédérale : 1935)",
            "Pas d'assurance des dépôts (avant 1933)"], x=170, y=130, w=940),
        "fm": dict(type="mot", t="De l'aisance à la misère en un mois", g="tous les filets de sécurité disparus à la fois", y=260, taille=66),
    }),

    # ================================================================ I.3 idée 2 : Hoovervilles
    dict(id="hoover", chap="I.3 · Les Hoovervilles", fond="guerre", humeur="mystere",
         retenir="Hoovervilles : bidonvilles en bois de récupération, pierre et métal construits par des expulsés, souvent au cœur des grandes villes, nommés d'après le président Hoover — un verdict politique. La plus grande à Saint-Louis ; une à Central Park ; la soupe populaire d'Al Capone à Chicago (automne 1930).",
         beats=[
        "{hv}Deuxième idée : les Hoovervilles rendent la pauvreté visible, au cœur des villes américaines. "
        "Les personnes expulsées de leur logement construisent des bidonvilles en bois de récupération, en pierre et en métal, sur des terrains vagues, "
        "souvent au cœur des grandes villes.",
        "{-hv}{nom}Pourquoi ce nom ? On les appelle d'après {!le président Hoover}le président Hoover, que l'opinion tient pour responsable de la crise. "
        "Le nom lui-même est donc un verdict politique.",
        "{-nom}{g7}{g7.1}La plus grande Hooverville se trouve à Saint-Louis. Une autre occupe une partie de Central Park, à New York : "
        "la pauvreté au centre du pays le plus riche du monde.",
        "{-g7}{capf}{cap}Et un détail étonnant du cours. À Chicago, à l'automne mille neuf cent trente, le gangster {!Al Capone}Al Capone ouvre une soupe populaire. "
        "De la charité… mais aussi une opération de sympathie, pour un homme visé par une enquête fédérale.",
        "Les Hoovervilles sont le premier sujet d'exposé oral du cours. {-cap}{-capf}{or1}Prépare quatre questions. "
        "{or1.1}Quoi ? {or1.2}Où ? {or1.3}Qui ? {or1.4}Et quand ? Les réponses sont à l'écran.",
        ("P", 5.0),
    ], vis={
        "hv": dict(type="tableau", img="h1-hooverville", de=[1.0, .5, .5], a=[1.15, .45, .5],
                   legende="Hooverville sur les vasières de Seattle, 7 février 1933 (Seattle Municipal Archives, Wikimedia Commons, CC BY 2.0)"),
        "nom": dict(type="def", terme="Hooverville", cles=["expulsés", "Hoover", "verdict"],
                    t="Un bidonville construit par des expulsés, nommé d'après le président Hoover, tenu pour responsable de la crise.",
                    etape="Le nom lui-même est un verdict politique.", x=170, y=200, w=940),
        "g7": dict(type="globe", code="H1", sc=[11]),
        "capf": dict(type="tableau", img="h1-soupkitchen", fond=True, sombre=True, de=[1.0, .3, .3], a=[1.2, .35, .3],
                     legende="La soupe populaire ouverte par Al Capone, Chicago, février 1931 (US National Archives, domaine public)"),
        "cap": dict(type="note", terme="Chicago, automne 1930", cles=["soupe populaire", "sympathie"],
                    t="Al Capone ouvre une soupe populaire : de la charité, et une opération de sympathie pour un gangster visé par une enquête fédérale.",
                    etape="Un exemple du cours", x=170, y=200, w=940),
        "or1": dict(type="liste", titre="Exposé oral · les Hoovervilles", items=[
            "Quoi : des bidonvilles en bois de récupération, pierre et métal", "Où : des terrains vagues dans les grandes villes — Saint-Louis, Central Park",
            "Qui : des familles expulsées, des chômeurs", "Quand : le début des années 1930, sous Hoover"], x=170, y=130, w=940),
    }),

    # ================================================================ I.3 idée 3 : Lange et la photographie
    dict(id="lange", chap="I.3 · La photographie comme argument", fond="nuit", humeur="calme",
         retenir="L'État fédéral documente la pauvreté : Dorothea Lange (1895–1965), White Angel Soup Kitchen (1933), puis Migrant Mother (mars 1936, Nipomo, Californie) pour une agence fédérale. Une image composée (une série de prises, de plus en plus près), faite pour gagner l'opinion aux programmes d'aide.",
         beats=[
        "{etat}Troisième idée, et elle surprend : l'État fédéral lui-même documente la pauvreté, et fait de la photographie un argument en faveur des réformes.",
        "{-etat}{dl}La photographe s'appelle {!Dorothea Lange}Dorothea Lange, {dl.1}de 1895 à 1965. En 1933, elle photographie la "
        "soupe populaire White Angel, à San Francisco. {dl.2}Puis elle travaille pour une agence fédérale, la Resettlement Administration, "
        "devenue ensuite la Farm Security Administration. Elle photographie les travailleurs agricoles migrants de Californie.",
        "{-dl}{mm}En mars 1936, dans un camp de cueilleurs de pois à Nipomo, en Californie, elle photographie {!Florence Owens Thompson}Florence Owens Thompson, "
        "trente-deux ans, qui vit sous une tente avec ses sept enfants. C'est Migrant Mother, la mère migrante.",
        "Regarde la composition. Le regard de la mère sort du cadre. Les enfants détournent le visage.",
        "{-mm}{rec}Le récit de Lange elle-même compte pour l'analyse du document. Elle raconte qu'elle s'est approchée,",
        ("C", "comme attirée par un aimant", "c_aimant"),
        "{-c_aimant}et qu'elle a fait cinq prises,",
        ("C", "en me rapprochant de plus en plus, du même côté", "c_proche"),
        "{-c_proche}{acc}Elle apprend que la famille vivait de légumes gelés ramassés dans les champs, et d'oiseaux attrapés par les enfants. "
        "La récolte de pois avait gelé, il n'y avait pas de travail. Et ils ne pouvaient pas repartir : la mère avait vendu les pneus de la voiture pour acheter à manger.",
        "{-acc}{-rec}{cmp}Alors, qu'est-ce que cette photographie ? {cmp.1}Elle est composée, pas prise au hasard : une série de prises, de plus en plus près. "
        "{cmp.2}Et elle est faite dans un but : gagner l'opinion aux programmes d'aide. "
        "{cmp.3}Publiée aussitôt, l'image contribue à faire envoyer des secours fédéraux au camp.",
    ], vis={
        "etat": dict(type="question", t="Pourquoi un État photographierait-il sa propre pauvreté ?"),
        "dl": dict(type="liste", titre="Dorothea Lange (1895 – 1965)", items=[
            "1933 : la soupe populaire White Angel, San Francisco", "Pour une agence fédérale, la Resettlement Administration (puis la FSA) : les travailleurs migrants de Californie"],
            x=170, y=160, w=940),
        "mm": dict(type="tableau", img="h1-lange-migrant", de=[1.0, .5, .3], a=[1.12, .5, .28],
                   legende="Dorothea Lange, Migrant Mother, Nipomo, Californie, mars 1936 (Library of Congress, domaine public)"),
        "rec": dict(type="tableau", img="h1-lange-migrant", fond=True, de=[1.12, .5, .28], a=[1.2, .5, .3],
                    legende="Dorothea Lange, Migrant Mother, mars 1936 (domaine public)"),
        "c_aimant": dict(type="cit", a="Dorothea Lange", o="son récit de la prise de vue, Popular Photography, février 1960 (traduction)", x=200, y=190, w=880),
        "c_proche": dict(type="cit", a="Dorothea Lange", o="son récit de la prise de vue, Popular Photography, février 1960 (traduction)", x=200, y=190, w=880),
        "acc": dict(type="note", terme="Le récit de Lange", cles=["gelés", "travail", "pneus"],
                    t="La famille vit de légumes gelés ramassés dans les champs et d'oiseaux attrapés par les enfants. La récolte de pois a gelé : pas de travail.",
                    etape="Impossible de repartir : les pneus ont été vendus pour manger.", x=170, y=250, w=940),
        "cmp": dict(type="liste", titre="Une photographie comme argument", cles=["composée", "but", "secours"], items=[
            "Composée, pas prise au hasard : une série de prises", "Faite dans un but : gagner l'opinion aux programmes d'aide",
            "Publiée aussitôt : des secours fédéraux envoyés au camp"], x=170, y=150, w=940),
    }),

    # ================================================================ pause 2 : analyse de document sur Migrant Mother
    dict(id="dbq", chap="À toi · Analyse de document : Migrant Mother", fond="aube", humeur="tension",
         retenir="Analyse de document : présenter (nature, auteur, date, but) · situer dans le contexte · expliquer avec le cours · intérêt et limites · bilan critique.",
         beats=[
        "{ex4}Maintenant, une analyse de document, écrite pour cette vidéo. La consigne : en présentant Migrant Mother, de Dorothea Lange, "
        "montrez ce que cette photographie apprend sur {!les conséquences sociales}les conséquences sociales de la Grande Dépression aux États-Unis, "
        "puis portez un regard critique sur ce document.",
        "{-ex4}{str}Rappelle-toi la démarche, à chaque fois. {str.1}D'abord, présenter le document : sa nature, son auteur, sa date, son but. "
        "{str.2}Puis le situer dans son contexte. {str.3}Ensuite, l'expliquer : ce qu'il montre, éclairé par le cours. "
        "{str.4}Enfin, son intérêt et ses limites, pour finir par un bilan critique.",
        "{-str}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}Un modèle. {rep2.1}Ce document est une photographie prise par Dorothea Lange pour une agence fédérale, en mars 1936, "
        "dans un camp de cueilleurs de pois à Nipomo, en Californie. Elle montre Florence Owens Thompson, trente-deux ans, et ses enfants. "
        "{rep2.2}Elle est prise en pleine Grande Dépression, quand l'État fédéral fait photographier la misère des campagnes pour justifier ses programmes d'aide.",
        "{-rep2}{fo}Son intérêt. {fo.1}C'est une source précise, datée et située : une vraie famille, dans un vrai camp. "
        "{fo.2}Elle montre ce que les chiffres ne montrent pas : la faim, une tente, une famille sans aucun filet de sécurité. "
        "{fo.3}Avec le récit de Lange, elle montre le versant rural de la crise : récoltes gelées, pas de travail, pneus de la voiture vendus pour manger. "
        "{fo.4}Et sa provenance est elle-même un indice : l'État fédéral documente la pauvreté pour justifier les secours.",
        "{-fo}{li}Ses limites. {li.1}Elle est composée : une série de prises, le regard, les enfants qui se détournent. "
        "{li.2}Elle est faite dans un but, gagner l'opinion aux programmes d'aide : c'est un argument, pas un enregistrement neutre. "
        "{li.3}Elle montre une seule famille, de travailleurs agricoles migrants en Californie : pas les quatorze millions de chômeurs des villes, "
        "ni les Hoovervilles, ni les faillites bancaires. {li.4}Et, hors du cours : Florence Thompson a raconté plus tard que Lange ne lui avait jamais demandé son nom, "
        "et que sa famille était déjà partie quand les secours sont arrivés. Sa propre voix manque.",
        "{-li}{bl}D'où le bilan critique : un document très précieux, mais à condition de le lire comme un argument, et de le confronter aux chiffres du cours.",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="En présentant Migrant Mother (Dorothea Lange, mars 1936), montrez ce que cette photographie apprend sur les conséquences sociales de la Grande Dépression aux États-Unis, puis portez un regard critique sur ce document.",
                    src="Consigne écrite pour cette vidéo, sur un document du cours", enonce=["Analyse de document"]),
        "str": dict(type="liste", titre="L'analyse de document : la démarche", cles=["présenter", "situer", "expliquer", "limites"], items=[
            "Présenter le document : nature, auteur, date, but", "Le situer dans son contexte",
            "L'expliquer : ce qu'il montre, éclairé par le cours", "Intérêt et limites, puis un bilan critique"], x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Écris les premières lignes : présente le document, puis situe-le dans son contexte.",
                    sous="Mets la vidéo en pause, puis continue : intérêt, limites. Relance pour voir un modèle."),
        "rep2": dict(type="note", terme="Une introduction modèle", cles=["fédérale", "Nipomo", "Dépression"],
                     t="Une photographie prise par Dorothea Lange pour une agence fédérale à Nipomo, en Californie, en mars 1936. "
                       "En pleine Grande Dépression, l'État fait photographier la misère des campagnes pour justifier ses aides.",
                     etape="Présenter · situer", x=150, y=180, w=980),
        "fo": dict(type="liste", titre="Intérêt", items=[
            "Précise, datée, située : une vraie famille, un vrai camp", "Montre ce que les chiffres ne montrent pas : la faim, une tente, aucun filet",
            "Avec le récit de Lange : récoltes gelées, pas de travail, pneus vendus", "La provenance comme indice : l'État documente la pauvreté"],
            x=150, y=130, w=980),
        "li": dict(type="liste", titre="Limites", items=[
            "Composée : une série de prises, faite pour émouvoir", "Un but : gagner l'opinion aux aides — un argument",
            "Une famille rurale : ni les 14 millions, ni les villes", "Hors du cours : la voix de la mère elle-même manque"],
            x=150, y=130, w=980),
        "bl": dict(type="mot", t="Un document précieux", g="à lire comme un argument, à confronter aux chiffres", y=260, taille=84),
    }),

    # ================================================================ I.3 idée 4 : Dust Bowl
    dict(id="dust", chap="I.3 · Le Dust Bowl", fond="guerre", humeur="tension",
         retenir="Le Dust Bowl : sécheresse sévère + labour mécanisé sans méthodes de culture sèche → érosion éolienne. Dimanche noir, 14 avril 1935 ; Stratford, Texas, 1935 ; « pneumonie des poussières ». Ruinées deux fois, les familles partent pour la Californie.",
         beats=[
        "{ds}Quatrième idée : le Dust Bowl transforme une crise économique en crise écologique.",
        "{-ds}{cau}Deux causes. {cau.1}Une sécheresse sévère, dans les années trente. {cau.2}Et l'absence de méthodes de culture sèche "
        "pour empêcher l'érosion par le vent. Le labour mécanisé avait privé les Grandes Plaines des herbes profondes qui retenaient le sol. "
        "{cau.3}Quand les pluies manquent, la terre à nu se soulève en tempêtes qui ensevelissent les fermes et rendent des comtés entiers invivables.",
        "{-cau}{nat}Le désastre n'est donc {!pas purement naturel}pas purement naturel. C'est le prix d'une technique agricole "
        "fondée sur la grosse mécanisation, sans égard pour le sol.",
        "{-nat}{ds2}L'exemple. Une tempête de poussière, photographiée à l'approche de Stratford, au Texas, en 1935, remplit le ciel comme un mur. "
        "{-ds2}{g8}{g8.1}Et le dimanche noir, le quatorze avril 1935, change le jour en nuit sur l'Oklahoma et le Texas. "
        "La pneumonie des poussières tue des enfants et des vieillards.",
        "{-g8}{dep}Ruinées deux fois, par les prix et par la poussière, des familles partent pour la Californie. Et c'est là que Dorothea Lange les retrouve.",
    ], vis={
        "ds": dict(type="tableau", img="h1-dustbowl", de=[1.0, .5, .5], a=[1.12, .5, .45],
                   legende="Tempête de poussière à l'approche de Stratford, Texas, 1935 (George E. Marsh Jr., NOAA, Wikimedia Commons, domaine public)"),
        "cau": dict(type="liste", titre="Pourquoi le Dust Bowl ?", items=[
            "Une sécheresse sévère dans les années 1930", "Pas de culture sèche : le labour mécanisé a arraché les herbes profondes",
            "La terre à nu → des tempêtes de poussière ensevelissent fermes et comtés"], x=170, y=140, w=940),
        "nat": dict(type="cols", g="Naturel", gq="la sécheresse : les pluies manquent", d="Humain", dq="la grosse mécanisation, sans égard pour le sol", vs="+"),
        "ds2": dict(type="tableau", img="h1-dustbowl", de=[1.12, .5, .45], a=[1.2, .5, .4],
                    legende="Tempête de poussière à l'approche de Stratford, Texas, 1935 (George E. Marsh Jr., NOAA, Wikimedia Commons, domaine public)"),
        "g8": dict(type="globe", code="H1", sc=[25]),
        "dep": dict(type="note", terme="Ruinées deux fois", cles=["prix", "poussière", "Californie"],
                    t="Par les prix et par la poussière : des familles quittent les Grandes Plaines pour la Californie — où Lange les retrouve.",
                    etape="Dust Bowl → travailleurs migrants → Migrant Mother", x=170, y=200, w=940),
    }),

    # ================================================================ I.3 idée 5 : traumatisme mondial mais inégal
    dict(id="inegal", chap="I.3 · Mondial, mais inégal", fond="nuit", humeur="calme",
         retenir="Notion clé : dépression économique mondiale. Krach → Dépression américaine → chute de la production, chômage massif, déflation aiguë dans le monde. Mais les économies hors des marchés mondiaux sont largement épargnées : l'URSS, en plein premier plan quinquennal, est à peine touchée.",
         beats=[
        "{g9}Dernière idée : le traumatisme est mondial… mais inégalement réparti.",
        "{g9.1}{ch}La chaîne du cours est courte. {ch.1}Le krach américain. {ch.2}La Dépression américaine. "
        "{ch.3}Puis, dans le monde entier : la chute de la production, un chômage massif, et une déflation aiguë.",
        "{-ch}{-g9}{kt}Mais les pays qui n'étaient pas intégrés aux marchés boursiers et au commerce mondial sont largement épargnés. "
        "Et cela compte pour une notion clé : {!dépression économique mondiale}la dépression économique mondiale. "
        "Une dépression mondiale ne veut pas dire que tous les pays souffrent de la même façon.",
        "{-kt}{urss}L'exemple. L'Union soviétique, hors du système d'échanges capitaliste, et en plein premier plan quinquennal, "
        "est à peine touchée. C'est exactement pourquoi des visiteurs occidentaux rentrent impressionnés par la planification, et pourquoi certains modèles politiques gagnent du prestige dans les années trente.",
    ], vis={
        "g9": dict(type="globe", code="H1", sc=[12]),
        "ch": dict(type="liste", titre="La chaîne du cours", items=[
            "Krach américain", "Dépression américaine", "Dans le monde : chute de la production, chômage massif, déflation aiguë"],
            x=640, y=440, w=600, petit=True, bande=True),
        "kt": dict(type="def", terme="Notion clé · dépression économique mondiale", cles=["intégrés", "épargnés", "même façon"],
                   t="Une dépression qui se propage à toute l'économie mondiale — mais les pays qui n'étaient pas intégrés aux marchés et au commerce mondiaux sont largement épargnés.",
                   etape="Mondiale ne veut pas dire que tous les pays souffrent de la même façon.", x=170, y=130, w=940),
        "urss": dict(type="note", terme="L'exception · l'URSS", cles=["plan quinquennal", "planification"],
                     t="Hors du système d'échanges capitaliste, en plein premier plan quinquennal : à peine touchée.",
                     etape="Les visiteurs occidentaux du début des années 1930 rentrent impressionnés par la planification.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Les banques : la Grande Dépression commence vraiment quand de nombreuses banques font faillite, "
        "environ cinq mille avant 1932. {carte.2}Les canaux : le rappel des prêts américains, le circuit Dawes brisé, "
        "et l'étalon-or comme courroie de transmission. {carte.3}Le monde : les dominos en Europe en 1931, la chute des prix dans la périphérie, "
        "le café du Brésil et le nitrate du Chili. {carte.4}Et le traumatisme : quatorze millions de chômeurs sans filet de sécurité, les Hoovervilles, "
        "Migrant Mother, le Dust Bowl… mondial, mais inégal.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : le nationalisme économique et les réponses politiques. Comment les pays réagissent-ils ? "
        "En fermant leurs frontières… et, pour certains, en choisissant le militarisme.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="UNE CRISE MONDIALE", branches=[
            dict(t="Les banques", items=["la charnière du chapitre", "≈ 5 000 faillites avant 1932", "pas d'assurance des dépôts"]),
            dict(t="Les canaux", items=["prêts américains rappelés", "Dawes : 800 M · 2,5 Md de marks", "l'or : la courroie de transmission"]),
            dict(t="Le monde", items=["1931 : Vienne · Berlin · Londres", "café du Brésil, nitrate du Chili", "la France touchée en 1932"]),
            dict(t="Le traumatisme", items=["14 millions · 25 %", "Hoovervilles · Lange", "Dust Bowl · URSS épargnée"])]),
        "fin": dict(type="mot", t="Ensuite : le nationalisme économique", g="Épisode 3 · Nationalisme économique et réponses politiques", y=270, taille=66),
    }),
]

QUIZ = [
    dict(q="D'après le cours, quand la Grande Dépression commence-t-elle vraiment ?",
         r=["Quand de nombreuses banques font faillite", "Le jeudi noir, 24 octobre 1929",
            "Quand le tarif Smoot-Hawley est signé", "Quand le Royaume-Uni quitte l'étalon-or"], ok=0, voir="m1",
         ex="Un krach dure des jours ; les banques l'ont transmis à l'économie réelle. Environ 5 000 avaient fait faillite avant 1932."),
    dict(q="Pourquoi une simple rumeur pouvait-elle vider une banque américaine avant 1933 ?",
         r=["Il n'existait aucune assurance des dépôts", "Les banques n'avaient pas le droit de détenir de l'or",
            "La Réserve fédérale n'existait pas", "L'épargne était placée en Europe"], ok=0, voir="ex1",
         ex="Quand une banque tombait, l'épargne de ses clients disparaissait, tout simplement."),
    dict(q="Laquelle est une cause À COURT TERME de la propagation de la crise, d'après le cours ?",
         r=["Les banques américaines rappellent brutalement leurs prêts aux banques européennes", "La surproduction",
            "La baisse des revenus agricoles", "Le surinvestissement dans l'industrie"], ok=0, voir="cc",
         ex="Les trois autres sont des faiblesses profondes, partagées par toutes les économies."),
    dict(q="Dans le circuit Dawes, que versent la France et le Royaume-Uni aux États-Unis ?",
         r=["Le remboursement de leurs dettes de guerre", "Des réparations", "Un emprunt de 800 millions de marks", "De l'or pour garantir le dollar"], ok=0, voir="tri",
         ex="États-Unis → Allemagne (emprunt) → France et Royaume-Uni (réparations) → États-Unis (dettes de guerre)."),
    dict(q="Pourquoi l'étalon-or est-il une « courroie de transmission » ?",
         r=["Des taux américains plus hauts attirent l'or et forcent les autres pays à relever leurs taux",
            "Il permet aux pays d'imprimer de la monnaie librement", "Il fixe les prix du commerce mondial", "Il garantit les dépôts bancaires"], ok=0, voir="mec",
         ex="De l'argent plus cher en pleine crise : moins d'investissement, moins de dépenses, partout."),
    dict(q="Quel pays quitte l'étalon-or le dernier, et se redresse le dernier ?",
         r=["La France (1936)", "Le Royaume-Uni (1931)", "Le Japon (1931)", "Les États-Unis (1933)"], ok=0, voir="fr2",
         ex="Plus un pays quitte l'or tôt, plus il se redresse tôt."),
    dict(q="Que fait le Brésil de son café entre 1931 et 1944 ?",
         r=["Il en brûle quelque 78 millions de sacs pour soutenir le prix", "Il le vend entièrement à l'URSS",
            "Il cesse d'en cultiver", "Il s'en sert pour rembourser des dettes de guerre"], ok=0, voir="per",
         ex="Un pays qui ne vend qu'une denrée n'a aucun amortisseur."),
    dict(q="Laquelle est une LIMITE valable de Migrant Mother comme document sur la Dépression ?",
         r=["Elle est composée pour gagner l'opinion aux aides, et ne montre qu'une famille rurale", "Elle n'est pas datée",
            "Elle a été prise après la Seconde Guerre mondiale", "Son auteur est inconnu"], ok=0, voir="li",
         ex="Cinq prises, un but, une famille : un argument, pas un enregistrement neutre."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 1 « Le krach de Wall Street et son impact », parties I.2 et I.3, avec les schémas « Le circuit Dawes », « Comment le krach devient une dépression mondiale » et l'exercice sur la hiérarchie des causes, tel qu'il est rédigé sur le site ; carte animée du chapitre 1 (site).",
    "Photographies : chômeurs devant la soupe populaire d'Al Capone, Chicago, février 1931 (US National Archives, domaine public) ; "
    "Hooverville sur les vasières de Seattle, 1933 (Seattle Municipal Archives, CC BY 2.0) ; Dorothea Lange, Migrant Mother, 1936 (Library of Congress, domaine public) ; "
    "George E. Marsh Jr., tempête de poussière à l'approche de Stratford, Texas, 1935 (NOAA, domaine public) ; via Wikimedia Commons.",
    "Citations de Dorothea Lange : son récit de la prise de vue (Popular Photography, février 1960), en traduction française.",
    "Questions et modèles de réponse écrits pour cette vidéo. Hors du cours : le témoignage ultérieur de Florence Owens Thompson.",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
