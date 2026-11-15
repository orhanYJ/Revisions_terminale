"""SES, É3 : « Comment lutter contre le chômage ? » — le chapitre en vidéo.

Même chaîne que le pilote ses_e1.py (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ; moteur
ses/serie/moteur.js. Illustrations propres à la vidéo dans ses/serie/illu-ses-e3.js : la courbe du chômage 1975-2025
(graphique « lignes » du site, que le type donnees ne dessine pas) et les deux animations du chapitre (e3-spirale,
e3-appariement), recopiées de data-e3.js parce que site-ses.js ne reprend que les fichiers data-anim-*.js.
Contenu : le chapitre É3 du site « Faits & Courbes » (outils/specialites/ses/src/data-e3.js), rien au-delà. Graphiques et
chaînes causales lus dans les sources du site (site_ses.py) ; sujets corrigés : ceux du site ; nombres lus écrits en lettres.
Usage : python3 outils/serie-philo/verifier.py ses_e3 ; SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py ses_e3
(brouillon sans voix) ; chevauchements.py ses-e3.
"""
import site_ses

SITE = "ses"
CODE = "ses-e3"
NOTION = "Le chômage"
NUM = 3
TITRE = "Comment lutter contre le chômage ?"
SUIVANT = "É4 · Les crises financières"
RYTHME = "vivant"
PRONONCIATION = {"Highland Park": "Haïlande Parque", "Five Dollar Day": "Faïve Dolar Dé", "New Jersey": "Niou Djersé",
                 "fast-foods": "fast-foudes", "insiders": "inn-saïdeurze", "outsiders": "aoute-saïdeurze",
                 "Maynard": "Mé-narde", "John": "Djone", "Keynes": "Kéïnze", "Shapiro": "Chapiro", "Stiglitz": "Stiglitse",
                 "Carl": "Carle", "Joseph": "Djozèf", "Card": "Carde", "Krueger": "Crougueure", "Alan": "Alane",
                 "David": "Dévid", "Lindbeck": "Lindbèque", "Snower": "Sno-eure", "Assar": "Assare", "Dennis": "Dénisse",
                 "Diamond": "Daïmonde", "Mortensen": "Mortènnsène", "Pissarides": "Pissaridisse", "Peter": "Piteur",
                 "Dale": "Dèle", "Christopher": "Christofeur", "Beveridge": "Bévéridje", "Henry": "Henri", "Ford": "Forde",
                 "Akerlof": "Akeurlof", "Spence": "Spènce", "Insee": "Inssé", "BIT": "bé-i-té", "CDI": "cé-dé-i",
                 "CDD": "cé-dé-dé", "CICE": "cé-i-cé-eu", "PIB": "pé-i-bé", "SES": "èss-eu-èss", "AEI": "a, eu, i",
                 "SMIC": "smic", "CAP": "cé-a-pé", "BEP": "bé-eu-pé"}

D = site_ses.donnees()
G, CHN, CH = D["graphes"], D["chaines"], D["ch"]["e3"]
CHIF = CH["chiffres"]          # les trois « En chiffres » du chapitre

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="canard", humeur="mystere", carton=False, beats=[
        "{cf_ouv}{cf_ouv.1}Sept virgule sept pour cent. C'est le taux de chômage en France en deux mille vingt-cinq. "
        "Deux millions et demi de personnes. En hausse de zéro virgule trois point en un an.",
        "{-cf_ouv}{q_ouv}Et pourtant… au même moment, des entreprises n'arrivent pas à recruter. Des chômeurs d'un côté, des postes vides de l'autre. "
        "Comment est-ce possible ?",
        "{-q_ouv}{q_ouv2}Et d'abord : c'est quoi, exactement, un chômeur ? Pourquoi le chômage monte-t-il pendant les crises ? "
        "Et surtout : que peut-on faire contre lui ?",
        "{-q_ouv2}{plan}Voilà le chemin. {plan.1}D'abord, définir et mesurer le chômage. "
        "{plan.2}Ensuite, le chômage structurel : les problèmes d'appariement et le salaire d'efficience. "
        "{plan.3}Puis le rôle des institutions : le salaire minimum, la protection de l'emploi. "
        "{plan.4}Le chômage conjoncturel, celui des crises. {plan.5}Les politiques pour lutter contre le chômage. "
        "{plan.6}Et pour finir, le bac : un calcul, les trois parties de l'épreuve composée et la dissertation, avec des sujets corrigés.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "cf_ouv": dict(type="chiffres", x=110, y=150, w=1060, items=[dict(n=CHIF[0]["n"], l=CHIF[0]["l"], s=CHIF[0]["s"])]),
        "q_ouv": dict(type="question", t="Des chômeurs d'un côté, des postes vacants de l'autre : comment est-ce possible ?"),
        "q_ouv2": dict(type="question", t="Qu'est-ce qu'un chômeur ? Pourquoi les crises ? Que faire ?"),
        "plan": dict(type="liste", titre="Le chemin", x=170, y=96, w=940, items=[
            "Définir et mesurer le chômage", "Le chômage structurel : appariement, salaire d'efficience",
            "Les institutions : salaire minimum, protection de l'emploi", "Le chômage conjoncturel",
            "Les politiques contre le chômage", "Au bac : calcul, épreuve composée, dissertation"]),
        "titre": dict(type="titre", sur="SES · Terminale · É3", t="Comment lutter contre le chômage ?",
                      sous="Le chapitre complet, de zéro au bac"),
    }),

    # ================================================================ I. définir et mesurer
    dict(id="mesurer", chap="Définir et mesurer le chômage", fond="nuit", humeur="lumiere",
         retenir="Chômeur au sens du BIT : sans emploi, disponible, en recherche active. Taux de chômage = chômeurs ÷ actifs "
                 "(7,7 % en 2025). Taux d'emploi des 15-64 ans : 69,3 %. Sous-emploi : 4,4 % de l'emploi ; halo : 1,9 million (Insee).",
         beats=[
        "{q_def}Commençons par une question simple, en apparence. Tu n'as pas d'emploi. Es-tu forcément chômeur ?",
        "{-q_def}{li_bit}Non. Pour être chômeur au sens du {!BIT}BIT, le Bureau international du travail, il faut remplir trois conditions, toutes à la fois. "
        "{li_bit.1}Un : être sans emploi pendant une semaine donnée. Pas même une heure de travail. "
        "{li_bit.2}Deux : être disponible pour travailler dans les deux semaines.",
        "{li_bit.3}Trois : avoir cherché activement un emploi dans les quatre dernières semaines. Ou en avoir trouvé un qui commence dans moins de trois mois. "
        "Tout cela, à partir de quinze ans.",
        "{-li_bit}{cols_ft}Qui compte ces chômeurs ? {cols_ft.g}L'Insee, chaque trimestre, par une grande enquête : l'enquête Emploi. "
        "Avec cette définition internationale. {cols_ft.d}Attention, ce n'est pas le nombre d'inscrits à France Travail, l'ancien Pôle emploi. "
        "Les inscriptions suivent des règles administratives. Les deux chiffres sont différents.",
        "{-cols_ft}{fo_taux}Maintenant, les deux indicateurs à savoir calculer. {fo_taux.1}D'abord, la population active : "
        "les personnes en emploi, plus les chômeurs. {fo_taux.2}Le taux de chômage, c'est le nombre de chômeurs divisé par la population active. Pas par toute la population !",
        "{fo_taux.3}Et le taux d'emploi, c'est le nombre de personnes en emploi divisé par toute la population du même âge.",
        "{-fo_taux}{fo_calc}Faisons le calcul avec les vrais chiffres de deux mille vingt-cinq. {fo_calc.1}Deux millions quatre cent cinquante et un mille chômeurs. "
        "Vingt-neuf millions trois cent quatre-vingt-trois mille personnes en emploi. "
        "{fo_calc.2}La population active : trente et un millions huit cent trente-quatre mille. "
        "{fo_calc.3}Et le taux de chômage : sept virgule sept pour cent.",
        "{-fo_calc}{cf_emp}Et le taux d'emploi des quinze à soixante-quatre ans ? {cf_emp.1}Soixante-neuf virgule trois pour cent. "
        "Son plus haut niveau depuis le début de la série, en mille neuf cent soixante-quinze.",
        "Tu vois ? Le chômage monte un peu… et l'emploi est au plus haut. Les deux indicateurs ne disent pas la même chose.",
        "{-cf_emp}{cols_jeunes}Un piège classique, maintenant. Le taux de chômage des quinze-vingt-quatre ans atteint dix-neuf virgule huit pour cent. "
        "Est-ce qu'un jeune sur cinq est au chômage ? {cols_jeunes.g}Non ! Dix-neuf virgule huit pour cent des jeunes {!actifs}actifs. "
        "{cols_jeunes.d}Or beaucoup de jeunes sont étudiants, donc inactifs. Rapportés à toute la classe d'âge, les chômeurs ne sont que huit virgule cinq pour cent.",
        ("P", 0.5),
        "{-cols_jeunes}{gr_ch}Prenons du recul : cinquante ans de chômage en France. La source, encore l'Insee. "
        "{gr_ch.1}En mille neuf cent soixante-quinze, le taux de chômage n'est que de trois virgule six pour cent. "
        "Puis les chocs pétroliers passent par là. Il grimpe, presque sans s'arrêter, jusqu'à dix virgule six pour cent en mille neuf cent quatre-vingt-quatorze.",
        "{gr_ch.2}Ensuite, il fluctue au gré de la conjoncture. Il redescend à sept virgule quatre pour cent en deux mille huit…",
        "{gr_ch.3}Puis la crise financière le fait remonter, jusqu'à dix virgule quatre pour cent en deux mille quinze.",
        "{gr_ch.4}Et il redescend : sept virgule trois en deux mille vingt-deux, sept virgule sept en deux mille vingt-cinq.",
        "{gr_ch.fh}Un dernier détail. Les femmes ont longtemps été bien plus touchées que les hommes. Aujourd'hui, leurs taux sont très proches.",
        "{-gr_ch}{def_se}Mais le chômage ne dit pas tout. Il y a des situations à ses frontières. D'abord, le {!sous-emploi}sous-emploi : "
        "des personnes qui ont un emploi, mais travaillent moins qu'elles ne le souhaitent. "
        "{def_se.1}Le temps partiel subi, ou le chômage partiel. En deux mille vingt-cinq : quatre virgule quatre pour cent des personnes en emploi.",
        "{-def_se}{def_halo}Ensuite, le {!halo}halo autour du chômage. Des personnes sans emploi, qui voudraient travailler, mais que le BIT classe inactives. "
        "Elles n'ont pas cherché, ou elles ne sont pas disponibles tout de suite. {def_halo.1}Un virgule neuf million de personnes en deux mille vingt-cinq.",
        "{-def_halo}{ex_2020}Et ça crée un vrai paradoxe. Deux mille vingt : les confinements. {ex_2020.1}L'activité s'effondre. "
        "{ex_2020.2}Mais beaucoup de chômeurs ne peuvent pas chercher d'emploi : ils sortent du chômage au sens du BIT, et passent dans le halo. "
        "{ex_2020.3}Et le chômage partiel concerne quatre virgule trois pour cent des personnes en emploi.",
        "{ex_2020.4}Résultat : le taux de chômage baisse ! Huit virgule un pour cent, contre huit virgule cinq en deux mille dix-neuf. Alors que l'économie est à l'arrêt.",
        "Retiens la leçon : un taux de chômage qui baisse, ce n'est pas forcément de l'emploi qui augmente.",
        "{-ex_2020}",
    ], vis={
        "q_def": dict(type="question", t="Sans emploi = forcément chômeur ?"),
        "li_bit": dict(type="liste", titre="Chômeur au sens du BIT · 15 ans ou plus", x=150, y=150, w=980, items=[
            "Sans emploi pendant une semaine donnée (pas même une heure)",
            "Disponible pour travailler dans les deux semaines",
            "En recherche active dans les quatre dernières semaines (ou un emploi trouvé qui commence dans moins de trois mois)"]),
        "cols_ft": dict(type="cols", g="Chômeur au sens du BIT", gq="Mesuré par l'Insee chaque trimestre : l'enquête Emploi, définition internationale.",
                        d="Inscrit à France Travail", dq="Règles administratives (ex-Pôle emploi, devenu France Travail en 2024).", vs="≠",
                        repere="Deux chiffres différents"),
        "fo_taux": dict(type="formule", titre="Les deux indicateurs", x=150, y=150, w=980, lignes=[
            dict(f="Population active = personnes en emploi + chômeurs", taille=34),
            dict(f="Taux de chômage = [[chômeurs|population active]] × 100", cadre=True, taille=36),
            dict(f="Taux d'emploi = [[personnes en emploi|population du même âge]] × 100", cadre=True, taille=36)]),
        "fo_calc": dict(type="formule", titre="Le calcul · France, 2025 (Insee)", x=150, y=170, w=980, lignes=[
            dict(f="2 451 000 chômeurs · 29 383 000 personnes en emploi", taille=32),
            dict(f="Population active = 29 383 000 + 2 451 000 = 31 834 000", taille=32),
            dict(f="[[2 451|31 834]] × 100 ≈ 7,7 %", cadre=True, taille=38)]),
        "cf_emp": dict(type="chiffres", x=170, y=170, w=940, items=[
            dict(n="69,3 %", l="Taux d'emploi des 15-64 ans en 2025 : record depuis le début de la mesure (1975).", s="Insee, enquête Emploi 2025")]),
        "cols_jeunes": dict(type="cols", g="Taux de chômage : 19,8 %", gq="Chômeurs ÷ jeunes actifs de 15 à 24 ans.",
                            d="Part de chômage : 8,5 %", dq="Chômeurs ÷ tous les 15-24 ans, étudiants compris.", vs="≠",
                            repere="15-24 ans, 2025 (Insee)"),
        "gr_ch": dict(type="illu", nom="chomage", x=70, y=80, w=1140, h=580,
                      phases=[[1975, 1994, "Après les chocs pétroliers", 4.5], [1994, 2008, "Fluctuations", 3.0],
                              [2008, 2015, "Crise financière, zone euro", 2.5], [2015, 2025, "Décrue", 2.8]],
                      points=[[1975, "", 0, -20], [1994, "10,6 %", 0, -22], [2008, "7,4 %", 0, 38], [2015, "10,4 %", 0, -22],
                              [2022, "7,3 %", -14, 40]]),
        "def_se": dict(type="def", terme="Sous-emploi", cles=["moins", "partiel"],
                       t="Des personnes en emploi qui travaillent moins qu'elles ne le souhaitent.",
                       etape="Temps partiel subi ou chômage partiel : 4,4 % des personnes en emploi en 2025 (Insee).", x=170, y=180, w=940),
        "def_halo": dict(type="def", terme="Halo autour du chômage", cles=["inactives", "travailler"],
                         t="Des personnes sans emploi, classées inactives par le BIT, mais qui souhaitent travailler : elles n'ont pas cherché, ou ne sont pas disponibles tout de suite.",
                         etape="1,9 million de personnes en 2025 (Insee).", x=170, y=170, w=940),
        "ex_2020": dict(type="liste", titre="Exemple · le paradoxe de 2020", x=150, y=140, w=980, items=[
            "Les confinements : l'activité s'effondre",
            "Des chômeurs ne peuvent pas chercher : ils passent du chômage BIT au halo",
            "Chômage partiel : 4,3 % des personnes en emploi",
            "Le taux de chômage baisse : 8,1 % contre 8,5 % en 2019"], marques=["1", "2", "3", "→"]),
    }),

    # ================================================================ II. le chômage structurel
    dict(id="structurel", chap="Le chômage structurel", fond="canard", humeur="mystere",
         retenir="Chômage structurel : indépendant de la conjoncture. Appariement (frictions ; inadéquations spatiales et de qualifications) "
                 "et asymétries d'information : le salaire d'efficience (Shapiro et Stiglitz, 1984 ; Ford, 1914).",
         beats=[
        "{cols_sc}Il existe deux grandes familles de chômage. Il faut les distinguer dès le départ. "
        "{cols_sc.g}Le chômage {!structurel}structurel : il ne dépend pas de la conjoncture. Il persiste même quand l'activité est soutenue, "
        "à cause du fonctionnement du marché du travail et de ses institutions. "
        "{cols_sc.d}Et le chômage conjoncturel : celui qui vient d'un ralentissement de l'activité. On y reviendra.",
        "{-cols_sc}{def_app}Première source de chômage structurel : les problèmes d'appariement. L'{!appariement}appariement, "
        "c'est la rencontre entre une offre d'emploi et un demandeur d'emploi. Et cette rencontre n'est ni immédiate, ni automatique.",
        "{-def_app}{an_app}Regarde. {an_app.1}D'un côté, des personnes qui cherchent un emploi. De l'autre, des entreprises qui ont des postes vacants. "
        "{an_app.2}Une partie se rencontre vite : vendeur, comptable, cariste. Ces postes sont pourvus.",
        "{an_app.3}Mais d'autres mettent du temps à se trouver. Chercher, comparer, postuler, passer des entretiens… "
        "Même quand le bon poste existe, il faut du temps. C'est le chômage {!frictionnel}frictionnel. Inévitable, dans une économie où les gens changent d'emploi.",
        "{an_app.4}Ensuite, l'inadéquation de qualifications. Un poste de technicien informatique ne convient pas à un ancien ouvrier du textile sans formation. "
        "C'est souvent l'effet de la destruction créatrice : les emplois se déplacent d'un secteur à l'autre.",
        "{an_app.5}Et l'inadéquation spatiale. L'emploi est à Lyon. Le chômeur, à Lille, à des centaines de kilomètres. Déménager coûte cher : "
        "il faut un logement, et le conjoint a peut-être son propre emploi.",
        "{an_app.6}Résultat : des chômeurs et des emplois vacants coexistent, durablement. C'est du chômage structurel.",
        "{-an_app}{ch_fr}{ch_fr.1}La chaîne causale, à savoir dérouler. Des emplois sont vacants, pendant que des personnes cherchent un emploi. "
        "{ch_fr.2}Pourquoi ? Les frictions : il faut du temps pour se trouver. Et les inadéquations : les emplois ne sont pas là où sont les chômeurs, "
        "ou ils demandent d'autres qualifications.",
        "{ch_fr.3}Donc offres et demandes de travail ne se rencontrent pas, même quand l'activité est bonne. "
        "{ch_fr.4}Donc un chômage structurel, qui persiste, quelle que soit la conjoncture.",
        "{ch_fr.tout}",
        ("P", 1.2),
        "{-ch_fr}{gr_dip}Et la qualification compte énormément. Regarde ces taux de chômage en deux mille vingt-cinq. "
        "{gr_dip.1}Sans diplôme, ou avec le seul brevet : quatorze virgule sept pour cent. "
        "{gr_dip.2}Avec un CAP ou un BEP : sept virgule six. {gr_dip.3}Avec le baccalauréat : neuf virgule un. "
        "{gr_dip.4}Et à partir de bac plus deux : cinq virgule trois pour cent seulement.",
        "{gr_dip.5}Même contraste selon le métier : dix-sept virgule un pour cent chez les ouvriers peu qualifiés. "
        "{gr_dip.6}Onze virgule quatre chez les employés peu qualifiés. {gr_dip.7}Et quatre pour cent chez les cadres.",
        "Le progrès technique biaisé en faveur du travail qualifié, vu dans le chapitre sur la croissance, renforce encore ces écarts.",
        "{-gr_dip}{note_bev}Pour aller plus loin. La courbe de Beveridge relie le taux d'emplois vacants et le taux de chômage. "
        "Si les deux augmentent ensemble, c'est le signe que l'appariement fonctionne moins bien. "
        "Et trois économistes, Peter Diamond, Dale Mortensen et Christopher Pissarides, ont reçu le prix Nobel en deux mille dix "
        "pour leurs travaux sur ces marchés avec frictions de recherche.",
        "{-note_bev}{q_eff}Deuxième source de chômage structurel, plus surprenante. Pourquoi un patron paierait-il ses salariés plus cher que nécessaire ?",
        "{-q_eff}{def_asy}Il faut partir d'une {!asymétrie}asymétrie d'information : une partie à un contrat en sait plus que l'autre. "
        "Ici, l'employeur ne connaît pas parfaitement l'effort de ses salariés, ni leur motivation. Il ne peut pas surveiller tout le monde, tout le temps.",
        "{-def_asy}{ch_eff}{ch_eff.1}Alors, la théorie du {!salaire d'efficience}salaire d'efficience. L'employeur ne peut pas observer parfaitement l'effort. "
        "{ch_eff.2}Donc il verse un salaire supérieur au salaire d'équilibre : pour motiver, pour fidéliser, et pour attirer les meilleurs.",
        "{ch_eff.3}Avec ce salaire, perdre son emploi coûte plus cher au salarié. Donc il fournit plus d'effort. "
        "{ch_eff.4}Or, à ce salaire élevé, les entreprises embauchent moins que ce que les travailleurs souhaitent offrir. "
        "{ch_eff.5}Donc un chômage involontaire, durable, apparaît. Et le salaire ne baisse pas, puisque l'employeur a intérêt à le garder haut.",
        "{-ch_eff}{li_ford}L'exemple le plus célèbre ? {li_ford.1}Le cinq janvier mille neuf cent quatorze, Henry Ford annonce le Five Dollar Day, "
        "à l'usine de Highland Park. Cinq dollars pour une journée de huit heures. {li_ford.2}Avant : environ deux dollars trente-quatre, pour neuf heures.",
        "{li_ford.3}Pourquoi ? Le travail à la chaîne était si pénible que les ouvriers partaient sans cesse. "
        "La rotation de la main-d'œuvre atteignait environ trois cent soixante-dix pour cent en mille neuf cent treize, selon l'entreprise. "
        "{li_ford.4}Avec ce salaire, les démissions et l'absentéisme chutent.",
        "Une nuance, quand même. Une partie de la somme était versée comme participation aux bénéfices, sous conditions de conduite. "
        "Et les historiens discutent encore de la part de ce motif. C'est un exemple classique d'histoire économique, pour aller plus loin : le programme ne le cite pas.",
        "{-li_ford}{au_ss}La théorie, elle, a été formalisée en mille neuf cent quatre-vingt-quatre par Carl Shapiro et Joseph Stiglitz. "
        "Leur modèle montre qu'avec un salaire d'efficience, le chômage est {!involontaire}involontaire et durable. "
        "Il sert même de discipline : la peur du chômage incite les salariés à l'effort. "
        "Stiglitz a reçu le prix Nobel en deux mille un, avec Akerlof et Spence, pour ses travaux sur les asymétries d'information.",
        "{-au_ss}",
    ], vis={
        "cols_sc": dict(type="cols", g="Chômage structurel", gq="Indépendant de la conjoncture : le fonctionnement du marché du travail et ses institutions.",
                        d="Chômage conjoncturel", dq="Dû à un ralentissement de l'activité économique.", vs="≠"),
        "def_app": dict(type="def", terme="Appariement", cles=["rencontre", "automatique"],
                        t="La rencontre entre une offre d'emploi et un demandeur d'emploi. Elle n'est ni immédiate, ni automatique.",
                        x=170, y=200, w=940),
        "an_app": dict(type="sanim", nom="e3-appariement", x=60, y=88, h=530, w=1160),
        "ch_fr": dict(type="chaine", c=CHN["e3-frictions"], x=170, w=940),
        "gr_dip": dict(type="donnees", g=G["e3-diplome"], x=90, y=90, w=1100, h=560, lab=330, signe=False,
                       couleurs=["corail", "moutarde", "moutarde", "canard", "corail", "moutarde", "canard"]),
        "note_bev": dict(type="note", titre="Pour aller plus loin · la courbe de Beveridge", cles=["vacants", "frictions"],
                         t="Emplois vacants et chômage qui augmentent ensemble : l'appariement est moins efficace. Diamond, Mortensen et Pissarides, Nobel 2010 : les marchés avec frictions de recherche.",
                         x=170, y=190, w=940),
        "q_eff": dict(type="question", t="Pourquoi payer ses salariés plus cher que nécessaire ?"),
        "def_asy": dict(type="def", terme="Asymétrie d'information", cles=["sait", "effort"],
                        t="Une partie à un contrat en sait plus que l'autre : l'employeur ne connaît pas parfaitement l'effort ni la motivation de ses salariés.",
                        x=170, y=190, w=940),
        "ch_eff": dict(type="chaine", c=CHN["e3-efficience"], x=170, w=940),
        "li_ford": dict(type="liste", titre="Exemple · le « Five Dollar Day » de Ford", x=150, y=130, w=980, items=[
            "5 janvier 1914, Highland Park : 5 dollars pour une journée de 8 heures",
            "Avant : environ 2,34 dollars pour 9 heures",
            "Le travail à la chaîne épuise : rotation d'environ 370 % en 1913 (selon l'entreprise)",
            "Démissions et absentéisme chutent"], marques=["1", "2", "3", "→"]),
        "au_ss": dict(type="auteur", mono="SS", nom="Carl Shapiro et Joseph Stiglitz", info="1984 · Nobel 2001 pour Stiglitz", cles=["involontaire", "discipline"],
                      t="Avec un salaire d'efficience, le chômage est involontaire et durable : il sert même de « discipline » qui incite les salariés à l'effort.",
                      x=170, y=210, w=940),
    }),

    # ================================================================ III. les institutions
    dict(id="institutions", chap="Salaire minimum et protection de l'emploi", fond="moutarde", humeur="calme",
         retenir="Institutions du marché du travail : effets ambigus. Salaire minimum : coût du travail contre pouvoir d'achat et efficience "
                 "(Card et Krueger, 1994). Protection de l'emploi : moins de licenciements en crise, moins d'embauches en reprise, dualisme.",
         beats=[
        "{def_inst}Troisième pièce du puzzle : les institutions du marché du travail. Ce sont les règles qui l'encadrent. "
        "{def_inst.1}Le salaire minimum, les contrats de travail, les règles de licenciement, l'assurance chômage, la négociation collective.",
        "Et voici l'idée clé : leurs effets sur le chômage structurel peuvent être positifs… ou négatifs. Le programme insiste sur deux d'entre elles.",
        "{-def_inst}{def_smic}La première, c'est le salaire minimum. En France, le {!SMIC}SMIC, le salaire minimum interprofessionnel de croissance. "
        "C'est le salaire horaire en dessous duquel aucun salarié ne peut être payé.",
        "{def_smic.1}Il est revalorisé chaque premier janvier, et automatiquement en cours d'année si l'inflation dépasse deux pour cent. "
        "Depuis juin deux mille vingt-six : douze euros trente et un brut de l'heure. Soit mille huit cent soixante-sept euros brut par mois, à temps plein.",
        "{-def_smic}{ch_smic}{ch_smic.1}Alors, un salaire minimum plus élevé, ça crée du chômage, ou pas ? Ça dépend. Et c'est toute la subtilité. "
        "{ch_smic.2}Il y a deux effets possibles, en même temps. D'un côté, le coût du travail peu qualifié augmente. "
        "S'il dépasse la productivité de certains travailleurs, les jeunes, les peu qualifiés, les employeurs ne les embauchent pas.",
        "De l'autre côté, le pouvoir d'achat augmente, donc la demande. Le travail devient plus attractif que l'inactivité. "
        "Et le salaire minimum fonctionne comme un salaire d'efficience : des salariés plus stables, plus motivés, plus productifs.",
        "{ch_smic.3}Donc l'effet net sur le chômage dépend du niveau du salaire minimum : par rapport au salaire médian, et par rapport à la productivité.",
        "{-ch_smic}{au_ck}Une étude célèbre a relancé ce débat. David Card et Alan Krueger, en mille neuf cent quatre-vingt-quatorze. "
        "En mille neuf cent quatre-vingt-douze, le salaire minimum augmente au New Jersey. Pas en Pennsylvanie, juste à côté. "
        "Ils comparent les fast-foods des deux côtés de la frontière… et ils ne trouvent pas de baisse de l'emploi au New Jersey.",
        "C'est une {!expérience naturelle}expérience naturelle : deux régions semblables, une seule différence. Card a reçu le prix Nobel en deux mille vingt et un.",
        "{-au_ck}{note_all}Et en France ? Pour limiter l'effet négatif sur l'emploi peu qualifié sans baisser le salaire du salarié, "
        "l'État allège les cotisations sociales patronales au niveau du SMIC. On y reviendra avec les politiques.",
        "{-note_all}{def_pe}Deuxième institution : les {!règles de protection de l'emploi}règles de protection de l'emploi. "
        "Elles encadrent les licenciements et le recours aux contrats temporaires. "
        "{def_pe.1}Préavis, motifs, indemnités, procédures, limites aux CDD et à l'intérim.",
        "{-def_pe}{ch_pe}{ch_pe.1}Quel effet sur le chômage ? Encore une fois, il est ambigu. Avec ces règles, licencier devient plus long et plus coûteux. "
        "{ch_pe.2}Donc, en récession, les entreprises licencient moins : le chômage monte moins vite. "
        "Mais en reprise, elles hésitent à embaucher en CDI : le chômage baisse moins vite.",
        "{ch_pe.3}Au total, l'effet sur le niveau du chômage est incertain. Mais les chômeurs restent plus longtemps sans emploi. "
        "{ch_pe.4}Et un {!dualisme}dualisme apparaît : des salariés en CDI protégés, et des jeunes et des peu qualifiés qui enchaînent les contrats courts.",
        "{-ch_pe}{au_ls}Ce dualisme a un nom : la théorie des insiders et des outsiders, formalisée par Assar Lindbeck et Dennis Snower en mille neuf cent quatre-vingt-huit. "
        "Les insiders, les salariés en place, protégés, obtiennent des salaires élevés. "
        "Au détriment des outsiders : les chômeurs et les précaires.",
        "{-au_ls}{cf_ld}Un chiffre l'illustre. {cf_ld.1}En deux mille vingt-cinq, le chômage de longue durée, plus d'un an, touche un virgule huit pour cent des actifs. "
        "Soit vingt-trois virgule un pour cent des chômeurs. {cf_ld.2}Et trente-neuf virgule un pour cent des chômeurs de cinquante ans ou plus.",
        "Les règles qui protègent l'emploi en place peuvent rendre plus difficile le retour à l'emploi des chômeurs âgés.",
        "{-cf_ld}",
    ], vis={
        "def_inst": dict(type="def", terme="Institutions du marché du travail", cles=["règles"],
                         t="Les règles qui encadrent le marché du travail. Leurs effets sur le chômage structurel peuvent être positifs ou négatifs.",
                         etape="Salaire minimum, contrats, licenciements, assurance chômage, négociation collective.", x=170, y=180, w=940),
        "def_smic": dict(type="def", terme="SMIC · salaire minimum interprofessionnel de croissance", cles=["horaire"],
                         t="Le salaire horaire en dessous duquel aucun salarié ne peut être payé en France.",
                         etape="12,31 € brut de l'heure, soit 1 867,02 € brut par mois à temps plein (depuis juin 2026, service-public.fr).",
                         x=150, y=170, w=980),
        "ch_smic": dict(type="chaine", c=CHN["e3-smic"], x=150, w=980),
        "au_ck": dict(type="auteur", mono="CK", nom="David Card et Alan Krueger", info="1994 · Nobel 2021 pour Card", cles=["New", "baisse"],
                      t="Hausse du salaire minimum au New Jersey en 1992, pas en Pennsylvanie voisine : pas de baisse de l'emploi dans les fast-foods. Une « expérience naturelle ».",
                      x=170, y=210, w=940),
        "note_all": dict(type="note", titre="En France", cles=["allège", "cotisations"],
                         t="L'État allège les cotisations sociales patronales au niveau du SMIC : moins de coût du travail, sans baisser le salaire.",
                         x=170, y=200, w=940),
        "def_pe": dict(type="def", terme="Règles de protection de l'emploi", cles=["licenciements", "temporaires"],
                       t="Les règles qui encadrent les licenciements et le recours aux contrats temporaires.",
                       etape="Préavis, motifs, indemnités, procédures, limites aux CDD et à l'intérim.", x=170, y=180, w=940),
        "ch_pe": dict(type="chaine", c=CHN["e3-protection"], x=150, w=980),
        "au_ls": dict(type="auteur", mono="LS", nom="Assar Lindbeck et Dennis Snower", info="1988", cles=["insiders", "outsiders"],
                      t="Les insiders, salariés en place et protégés, obtiennent des salaires élevés au détriment des outsiders : chômeurs et précaires.",
                      x=170, y=210, w=940),
        "cf_ld": dict(type="chiffres", titre="Le chômage de longue durée (2025)", x=110, y=160, w=1060, items=[
            dict(n="23,1 %", l="des chômeurs le sont depuis plus d'un an (1,8 % des actifs).", s="Insee, enquête Emploi 2025"),
            dict(n="39,1 %", l="des chômeurs de 50 ans ou plus sont au chômage depuis plus d'un an.", s="Insee, enquête Emploi 2025")]),
    }),

    # ================================================================ IV. le chômage conjoncturel
    dict(id="conjoncturel", chap="Le chômage conjoncturel", fond="corail", humeur="tension",
         retenir="Chômage conjoncturel : demande effective insuffisante (Keynes, 1936). Un cercle vicieux qui s'auto-entretient : "
                 "2009, PIB −2,8 %, chômage 7,4 % → 9,1 %, puis 10,4 % en 2015. Hystérèse : le conjoncturel peut devenir structurel.",
         beats=[
        "{def_cj}Changeons de famille. Le chômage {!conjoncturel}conjoncturel, c'est le chômage dû à un ralentissement de l'activité économique. "
        "La demande de biens et de services baisse. Les entreprises produisent moins… et ont besoin de moins de travail.",
        "{-def_cj}{au_keynes}L'économiste de référence, c'est John Maynard Keynes. En mille neuf cent trente-six, il publie la Théorie générale de l'emploi, de l'intérêt et de la monnaie. "
        "Son idée : le niveau de l'emploi dépend de la {!demande effective}demande effective. La demande que les entreprises anticipent.",
        "Si elle est insuffisante, le chômage peut durer. C'est un chômage involontaire. Et baisser les salaires ne le résout pas : "
        "ça réduirait encore la demande.",
        "{-au_keynes}{vi_rec}Voyons le mécanisme sur une petite économie. Des ménages, une entreprise, un magasin. Tout tourne. "
        "{vi_rec.1}Un choc arrive : la demande baisse. En deux mille neuf, c'est la crise financière mondiale. Les clients achètent moins.",
        "{vi_rec.2}L'entreprise vend moins, donc elle produit moins. Elle commence par réduire les heures et l'intérim.",
        "{vi_rec.3}Puis elle supprime des emplois. Le chômage augmente.",
        "{vi_rec.4}Les ménages qui perdent leur emploi perdent leurs revenus. Et les autres s'inquiètent : ils épargnent par précaution. Ils consomment moins.",
        "{vi_rec.5}Et donc… la demande baisse encore. La boucle est bouclée.",
        "{-vi_rec}{ch_cj}{ch_cj.1}C'est la spirale du chômage conjoncturel. Un choc : la demande baisse, à cause d'une crise financière, d'une hausse des prix de l'énergie, de l'incertitude. "
        "{ch_cj.2}Donc les entreprises produisent moins, et réduisent les heures, l'intérim, puis les emplois. {ch_cj.3}Donc le chômage augmente.",
        "{ch_cj.4}Donc les revenus et la confiance baissent : les ménages consomment moins, les entreprises investissent moins. "
        "{ch_cj.5}Donc la demande baisse encore. Le chômage conjoncturel s'{!auto-entretient}auto-entretient.",
        "{ch_cj.tout}",
        ("P", 1.2),
        "{-ch_cj}{li_09}Le cas réel : la crise de deux mille huit, deux mille neuf. {li_09.1}En deux mille neuf, le PIB français recule de deux virgule huit pour cent. "
        "{li_09.2}Le taux de chômage passe de sept virgule quatre pour cent en deux mille huit, à neuf virgule un pour cent en deux mille neuf.",
        "{li_09.3}Et il continue de monter, jusqu'à dix virgule quatre pour cent en deux mille quinze. Pourquoi si longtemps ? "
        "Parce que la reprise est lente, et que la zone euro connaît une seconde crise en deux mille onze, deux mille douze.",
        "{-li_09}{note_ret}Remarque aussi le rythme. L'emploi réagit avec retard. Les entreprises réduisent d'abord les heures supplémentaires et l'intérim. "
        "Puis elles ne remplacent pas les départs. Et seulement ensuite, elles licencient.",
        "À l'inverse, en reprise, elles attendent d'être sûres que l'activité repart avant d'embaucher. "
        "Et les premiers touchés, ce sont les jeunes et les salariés en contrats courts.",
        "{-note_ret}{def_hys}Dernière idée, très importante en dissertation : structurel et conjoncturel s'entremêlent. "
        "Un chômage conjoncturel qui dure peut devenir structurel. {def_hys.1}Les compétences des chômeurs de longue durée s'érodent. Les employeurs s'en méfient. "
        "C'est l'effet d'{!hystérèse}hystérèse.",
        "{-def_hys}",
    ], vis={
        "def_cj": dict(type="def", terme="Chômage conjoncturel", cles=["ralentissement", "demande"],
                       t="Le chômage dû à un ralentissement de l'activité économique : la demande baisse, les entreprises produisent moins et ont besoin de moins de travail.",
                       x=170, y=190, w=940),
        "au_keynes": dict(type="auteur", mono="JK", nom="John Maynard Keynes", info="1883-1946 · Théorie générale, 1936", cles=["demande", "involontaire"],
                          t="Le niveau de l'emploi dépend de la demande effective anticipée par les entreprises. Si elle est insuffisante, un chômage involontaire peut durer.",
                          x=170, y=210, w=940),
        "vi_rec": dict(type="ville", titre="Un choc de demande : le cercle vicieux", kicker="La maquette · exemple de 2009",
                       base=["usine", "magasin", "maisons", "banque"],
                       flux=[dict(de="usine", a="magasin", k="biens", n=1.4), dict(de="usine", a="maisons", k="revenus", l="salaires", n=1.4),
                             dict(de="maisons", a="magasin", k="achats")],
                       etapes=[
                           dict(foule=0.9, etiquette=dict(h="Choc de demande", s="crise financière : les clients achètent moins", sur="magasin")),
                           dict(flux=[dict(de="usine", a="magasin", k="biens", n=0.6)],
                                etiquette=dict(h="Production ↓", s="moins d'heures, moins d'intérim", sur="usine")),
                           dict(flux=[dict(de="usine", a="maisons", k="emplois", l="licenciements")],
                                etiquette=dict(h="Chômage ↑", s="des emplois sont supprimés", sur="maisons")),
                           dict(flux=[dict(de="usine", a="maisons", k="revenus", l="salaires", n=0.6)], foule=0.5,
                                etiquette=dict(h="Revenus ↓", s="on consomme moins, on épargne par précaution", sur="maisons"), cam="tout"),
                           dict(foule=0.35, flux=[dict(de="usine", a="magasin", k="biens", n=0.35)],
                                etiquette=dict(h="Demande ↓ encore", s="le cercle vicieux s'auto-entretient", sur="magasin"), cam="tout")]),
        "ch_cj": dict(type="chaine", c=CHN["e3-conj"], x=170, w=940),
        "li_09": dict(type="liste", titre="Exemple · la crise de 2008-2009 (Insee)", x=150, y=150, w=980, items=[
            "2009 : le PIB recule de 2,8 %", "Chômage : 7,4 % en 2008 → 9,1 % en 2009",
            "Puis 10,4 % en 2015 : reprise lente, crise de la zone euro en 2011-2012"]),
        "note_ret": dict(type="note", titre="L'emploi réagit avec retard", cles=["intérim", "départs", "licencient"],
                         t="D'abord les heures supplémentaires et l'intérim, puis les départs non remplacés, enfin les licenciements. Jeunes et contrats courts en première ligne.",
                         x=170, y=190, w=940),
        "def_hys": dict(type="def", terme="Hystérèse du chômage", cles=["structurel"],
                        t="Un chômage conjoncturel qui dure devient structurel.",
                        etape="Les compétences des chômeurs de longue durée s'érodent ; les employeurs s'en méfient.", x=170, y=190, w=940),
    }),

    # ================================================================ V. les politiques
    dict(id="politiques", chap="Quelles politiques contre le chômage ?", fond="vert", humeur="lumiere",
         retenir="Le diagnostic décide. Chômage conjoncturel : relance de la demande (budgétaire, monétaire, multiplicateur). "
                 "Chômage structurel : allègement du coût du travail, formation, flexibilisation (flexicurité). En pratique, on combine.",
         beats=[
        "{q_pol}Alors, que faire ? La réponse dépend d'abord du diagnostic. Quel chômage veut-on combattre ?",
        "{-q_pol}{ca_pol}Le programme distingue quatre familles de politiques. {ca_pol.1}Le soutien de la demande globale. "
        "{ca_pol.2}L'allègement du coût du travail. {ca_pol.3}La formation. {ca_pol.4}Et la flexibilisation du marché du travail.",
        "{-ca_pol}{an_sp}Commençons par le chômage conjoncturel. Revoyons le cercle vicieux, puis la sortie. "
        "{an_sp.1}Un choc frappe l'économie : la demande baisse. {an_sp.2}Les entreprises produisent moins. "
        "{an_sp.3}Le chômage augmente, et les ménages consomment moins. {an_sp.4}La demande baisse encore.",
        "{an_sp.5}La relance : l'État dépense plus, ou baisse les impôts. La banque centrale baisse ses taux. La demande repart. "
        "{an_sp.6}Et le cercle tourne dans l'autre sens : production, embauches, revenus, consommation. Le chômage conjoncturel recule.",
        "{-an_sp}{ch_rel}{ch_rel.1}En chaîne causale. Deux leviers. La politique {!budgétaire}budgétaire : plus de dépenses publiques, ou moins d'impôts. "
        "Et la politique monétaire : la baisse des taux d'intérêt directeurs. {ch_rel.2}Donc la consommation et l'investissement augmentent.",
        "{ch_rel.3}Donc les entreprises anticipent plus de ventes, et produisent davantage. "
        "{ch_rel.4}Donc elles embauchent : le chômage conjoncturel recule. Et les revenus distribués relancent encore la demande. C'est le {!multiplicateur}multiplicateur.",
        "{-ch_rel}{note_rel}Exemples en France : le plan de relance de deux mille vingt, et la prise en charge massive du chômage partiel pendant la crise sanitaire. "
        "{note_rel.1}Mais trois limites. La dette publique augmente. Une partie de la demande part en importations. "
        "Et surtout, la relance est inefficace contre le chômage structurel. N'oublie pas non plus que dans la zone euro, la politique monétaire est commune, "
        "et les budgets nationaux sont encadrés.",
        "{-note_rel}{def_all}Passons au chômage structurel. Premier outil : alléger le coût du travail. "
        "On baisse les cotisations sociales patronales sur les bas salaires. {def_all.1}Le coût du travail peu qualifié diminue, "
        "{!sans baisser le salaire net}sans baisser le salaire net. On vise les emplois dont la productivité est proche du SMIC.",
        "{-def_all}{li_all}{li_all.1}En France : la réduction générale des cotisations patronales sur les bas salaires, depuis deux mille trois. "
        "{li_all.2}Le CICE, en deux mille treize, transformé en baisse de cotisations en deux mille dix-neuf. "
        "{li_all.3}Les évaluations trouvent des effets positifs sur l'emploi, surtout pour les allègements ciblés au voisinage du SMIC.",
        "{li_all.4}Les limites : un coût élevé pour les finances publiques. Des effets d'aubaine : l'entreprise aurait embauché de toute façon. "
        "Et le risque de trappe à bas salaires : augmenter un salarié fait perdre l'allègement.",
        "{-li_all}{def_form}Deuxième outil : la formation. Elle améliore l'appariement, en rapprochant les compétences des chômeurs de celles que demandent les entreprises. "
        "Elle agit sur la cause même du chômage structurel. {def_form.1}En France : le compte personnel de formation en deux mille quinze, l'apprentissage, "
        "et le plan d'investissement dans les compétences en deux mille dix-huit.",
        "Mais ses effets sont lents. Et les formations profitent plus souvent… aux plus qualifiés.",
        "{-def_form}{def_flex}Troisième outil : la flexibilisation. Assouplir les règles d'embauche et de licenciement, pour inciter les entreprises à embaucher. "
        "{def_flex.1}En France : la rupture conventionnelle en deux mille huit, et les ordonnances de septembre deux mille dix-sept, "
        "avec un barème des indemnités prud'homales.",
        "Les limites : la précarisation, un effet incertain sur le niveau de l'emploi. Et des ajustements plus rapides, dans les deux sens.",
        "{-def_flex}{li_flexi}Un modèle souvent cité : la {!flexicurité}flexicurité danoise. Elle combine trois éléments. "
        "{li_flexi.1}Des licenciements faciles. {li_flexi.2}Une indemnisation généreuse. {li_flexi.3}Et des politiques actives de retour à l'emploi. "
        "{li_flexi.4}De la flexibilité pour l'entreprise, et de la sécurité pour la personne, plutôt que pour le poste.",
        "{-li_flexi}{cmp_pol}Récapitulons les quatre politiques. {cmp_pol.1}Le soutien de la demande vise le chômage conjoncturel. "
        "{cmp_pol.2}L'allègement du coût du travail vise le chômage structurel des peu qualifiés. "
        "{cmp_pol.3}La formation vise l'inadéquation des qualifications. {cmp_pol.4}Et la flexibilisation vise les rigidités.",
        "{-cmp_pol}{note_diag}Et voilà la règle d'or. On choisit la politique selon le {!diagnostic}diagnostic. "
        "Contre un chômage conjoncturel, la relance de la demande. Contre un chômage structurel, des politiques de l'offre. "
        "En pratique, les gouvernements combinent les deux.",
        "{-note_diag}",
    ], vis={
        "q_pol": dict(type="question", t="Quel chômage veut-on combattre ?"),
        "ca_pol": dict(type="liste", titre="Quatre familles de politiques", x=170, y=170, w=940, items=[
            "Soutenir la demande globale", "Alléger le coût du travail", "Former", "Flexibiliser le marché du travail"]),
        "an_sp": dict(type="sanim", nom="e3-spirale", x=60, y=88, h=530, w=1160),
        "ch_rel": dict(type="chaine", c=CHN["e3-relance"], x=150, w=980),
        "note_rel": dict(type="note", titre="Relancer la demande", cles=["relance", "partiel"],
                         t="Plan de relance de 2020 ; prise en charge massive du chômage partiel pendant la crise sanitaire.",
                         etape="Limites : dette publique, fuite par les importations, inefficace contre le chômage structurel.",
                         x=170, y=180, w=940),
        "def_all": dict(type="def", terme="Alléger le coût du travail", cles=["cotisations", "net"],
                        t="Baisser les cotisations sociales patronales sur les bas salaires.",
                        etape="Le coût du travail peu qualifié baisse, sans baisser le salaire net.", x=170, y=190, w=940),
        "li_all": dict(type="liste", titre="Les allègements en France", x=150, y=140, w=980, items=[
            "Réduction générale des cotisations patronales sur les bas salaires (depuis 2003)",
            "CICE (2013), transformé en baisse de cotisations en 2019",
            "Effets positifs surtout pour les allègements ciblés près du SMIC",
            "Limites : coût public, effets d'aubaine, trappe à bas salaires"], marques=["1", "2", "+", "−"]),
        "def_form": dict(type="def", terme="Former", cles=["appariement", "compétences"],
                         t="Améliorer l'appariement en rapprochant les compétences des chômeurs de celles que demandent les entreprises.",
                         etape="Compte personnel de formation (2015), apprentissage, plan d'investissement dans les compétences (2018).",
                         x=170, y=180, w=940),
        "def_flex": dict(type="def", terme="Flexibiliser", cles=["embauche", "licenciement"],
                         t="Assouplir les règles d'embauche et de licenciement pour inciter les entreprises à embaucher.",
                         etape="Rupture conventionnelle (2008) ; ordonnances de septembre 2017 (barème des indemnités prud'homales).",
                         x=170, y=180, w=940),
        "li_flexi": dict(type="liste", titre="La flexicurité danoise", x=170, y=160, w=940, items=[
            "Licenciements faciles", "Indemnisation généreuse", "Politiques actives de retour à l'emploi",
            "Sécurité pour la personne plutôt que pour le poste"], marques=["1", "2", "3", "→"]),
        "cmp_pol": dict(type="compare", titre="Quatre politiques contre le chômage", x=60, y=90, w=1160, cols=["Chômage visé", "Limite"], lignes=[
            ["Soutien de la demande", "Conjoncturel", "Dette publique ; importations ; inefficace contre le structurel"],
            ["Allègement du coût du travail", "Structurel (peu qualifiés)", "Coût public ; effets d'aubaine ; trappe à bas salaires"],
            ["Formation", "Structurel (inadéquation des qualifications)", "Effets lents ; profite plus aux plus qualifiés"],
            ["Flexibilisation", "Structurel (rigidités)", "Précarisation ; effet incertain sur l'emploi"]]),
        "note_diag": dict(type="note", titre="À retenir", cles=["diagnostic", "combinent"],
                          t="On choisit la politique selon le diagnostic : relance contre le conjoncturel, politiques de l'offre contre le structurel. En pratique, on combine.",
                          x=170, y=200, w=940),
    }),

    # ================================================================ VI. pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="nuit", humeur="tension", beats=[
        "{cmp_p1}Avant le bac, six pièges qui coûtent des points. {cmp_p1.1}Un : « chômeur, c'est inscrit à France Travail ». "
        "Non. Le chômeur au sens du BIT répond à trois critères, mesurés par l'enquête Emploi. Les inscriptions suivent d'autres règles.",
        "{cmp_p1.2}Deux : « dix-neuf virgule huit pour cent de chômage chez les jeunes, donc un jeune sur cinq est chômeur ». "
        "Non : dix-neuf virgule huit pour cent des jeunes actifs. Sur toute la classe d'âge, c'est huit virgule cinq pour cent.",
        "{cmp_p1.3}Trois : « si le taux de chômage baisse, l'emploi augmente forcément ». Faux. Des chômeurs peuvent devenir inactifs, "
        "par découragement, et passer dans le halo. Souviens-toi de deux mille vingt.",
        "{-cmp_p1}{cmp_p2}{cmp_p2.1}Quatre : confondre chômage structurel et chômage de longue durée. Le structurel désigne une cause : "
        "le fonctionnement du marché du travail. La longue durée désigne une durée : plus d'un an.",
        "{cmp_p2.2}Cinq : « le salaire minimum crée toujours du chômage ». Son effet dépend de son niveau par rapport à la productivité. "
        "Il peut aussi soutenir la demande, et jouer comme un salaire d'efficience. Pense à Card et Krueger.",
        "{cmp_p2.3}Et six : « la relance budgétaire fait baisser tout chômage ». Non : elle agit sur le chômage conjoncturel. "
        "Elle ne résout ni les frictions, ni les inadéquations de qualifications.",
        "{-cmp_p2}",
    ], vis={
        "cmp_p1": dict(type="compare", titre="Les pièges · 1 à 3", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["1 · Mesure", "« Chômeur = inscrit à France Travail. »", "Chômeur BIT : trois critères, enquête Emploi. Les deux chiffres diffèrent."],
            ["2 · Jeunes", "« 19,8 % : un jeune sur cinq est chômeur. »", "19,8 % des jeunes actifs ; 8,5 % de toute la classe d'âge."],
            ["3 · Emploi", "« Le chômage baisse, donc l'emploi augmente. »", "Des chômeurs peuvent devenir inactifs (halo) : 2020."]]),
        "cmp_p2": dict(type="compare", titre="Les pièges · 4 à 6", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["4 · Structurel", "Confondre structurel et longue durée.", "Structurel = une cause ; longue durée = une durée (plus d'un an)."],
            ["5 · Salaire minimum", "« Il crée toujours du chômage. »", "Effet selon son niveau ; demande et efficience (Card et Krueger)."],
            ["6 · Relance", "« La relance fait baisser tout chômage. »", "Seulement le conjoncturel : ni frictions, ni inadéquations."]]),
    }),

    # ================================================================ VII. au bac
    dict(id="epreuve", chap="Ce chapitre au bac", fond="canard", humeur="lumiere", beats=[
        "{li_ep}Passons au bac. L'écrit de SES dure quatre heures, au coefficient seize. Et tu choisis entre deux sujets. "
        "Soit l'épreuve composée, en trois parties : {li_ep.1}la mobilisation des connaissances, sur trois virgule cinq points, "
        "{li_ep.2}l'étude d'un document, sur cinq virgule cinq points, {li_ep.3}et le raisonnement sur un dossier documentaire, sur neuf points. "
        "{li_ep.4}Soit la dissertation, appuyée sur un dossier documentaire.",
        "Ce barème s'applique à partir de la session deux mille vingt-sept. Et dans les deux sujets, deux points sur vingt sont réservés à l'orthographe et à la syntaxe.",
        "Le chômage fait partie des questions du programme qui peuvent tomber à l'écrit.",
        "{-li_ep}{li_aei}Et une méthode revient partout : le paragraphe {!AEI}A, E, I. "
        "{li_aei.1}A : affirmer l'idée. {li_aei.2}E : expliquer le mécanisme, avec une chaîne causale, comme celles de ce chapitre. "
        "{li_aei.3}I : illustrer, par un exemple précis, chiffré ou daté. Ford en mille neuf cent quatorze, Card et Krueger, la crise de deux mille neuf.",
        "On commence par un savoir-faire indispensable : calculer un taux de chômage.",
        "{-li_aei}",
    ], vis={
        "li_ep": dict(type="liste", titre="L'écrit de SES · 4 heures · coefficient 16", x=150, y=120, w=980, items=[
            "Partie 1 · Mobilisation des connaissances : 3,5 points", "Partie 2 · Étude d'un document : 5,5 points",
            "Partie 3 · Raisonnement sur un dossier documentaire : 9 points", "Ou : la dissertation, appuyée sur un dossier documentaire"],
            marques=["1", "2", "3", "D"]),
        "li_aei": dict(type="liste", titre="Le paragraphe AEI", x=170, y=170, w=940, items=[
            "Affirmer l'idée", "Expliquer le mécanisme : une chaîne causale", "Illustrer : un exemple précis, chiffré ou daté"],
            marques=["A", "E", "I"]),
    }),

    # ================================================================ VIII. savoir-faire : calculer un taux de chômage
    # 29 383 000 + 2 451 000 = 31 834 000 ; 2 451 / 31 834 = 0,07699 → 7,7 % (exercice du site, données Insee)
    dict(id="calcul", chap="Savoir-faire · calculer un taux de chômage", fond="nuit", humeur="calme", beats=[
        "{ex_c}Voici l'exercice, avec les données de l'Insee. En deux mille vingt-cinq, la France compte deux millions quatre cent cinquante et un mille chômeurs "
        "au sens du BIT, et vingt-neuf millions trois cent quatre-vingt-trois mille personnes en emploi. "
        "{ex_c.1}Un : calcule la population active, puis le taux de chômage. "
        "{ex_c.2}Deux : les quinze-vingt-quatre ans ont un taux de chômage de dix-neuf virgule huit pour cent, mais une part de chômage de huit virgule cinq pour cent. "
        "Explique la différence.",
        "{-ex_c}{pa_c}À toi. Mets la vidéo sur pause, et fais le calcul à la main.",
        "{pa_c.stop}{-pa_c}{ex_cc}{ex_cc.q1}Correction. {s_c1}{s_c1.1}La population active, c'est l'emploi plus le chômage : "
        "vingt-neuf millions trois cent quatre-vingt-trois mille, plus deux millions quatre cent cinquante et un mille. "
        "{s_c1.2}Trente et un millions huit cent trente-quatre mille.",
        "{s_c1.3}Le taux de chômage : deux mille quatre cent cinquante et un, divisé par trente et un mille huit cent trente-quatre, en milliers. "
        "À la main : dix pour cent, ce serait environ trois mille cent quatre-vingts. On est en dessous. Sept pour cent, environ deux mille deux cent vingt-huit. "
        "Il reste environ deux cent vingt-trois. Or un pour cent, c'est environ trois cent dix-huit. Deux cent vingt-trois, c'est à peu près sept dixièmes de trois cent dix-huit : zéro virgule sept point. Donc environ sept virgule sept pour cent.",
        "{-s_c1}{ex_cc.q2}{s_c2}{s_c2.1}Deux. Le taux de chômage rapporte les chômeurs aux actifs. {s_c2.2}La part de chômage les rapporte à toute la classe d'âge. "
        "{s_c2.3}Or beaucoup de quinze-vingt-quatre ans étudient : ils sont inactifs. Le dénominateur est bien plus grand, donc la part est plus faible.",
        "{-s_c2}{-ex_cc}",
    ], vis={
        "ex_c": dict(type="exo", niveau="calcul", titre="Calculer un taux de chômage", src="Exercice du site, données Insee", y=80,
                     enonce=["France, 2025 : 2 451 000 chômeurs au sens du BIT et 29 383 000 personnes en emploi (Insee)."],
                     questions=["Calcule la population active, puis le taux de chômage.",
                                "Les 15-24 ans ont un taux de chômage de 19,8 % mais une « part de chômage » de 8,5 %. Explique la différence."]),
        "pa_c": dict(type="pause", t="La population active, le taux de chômage, puis la différence entre taux et part."),
        "ex_cc": dict(type="exo", mode="coin", niveau="calcul", titre="Calculer un taux de chômage",
                      donnees=["2 451 000 chômeurs", "29 383 000 en emploi", "15-24 ans : 19,8 % / 8,5 %"],
                      questions=["Population active et taux de chômage ?", "Taux ou part : la différence ?"]),
        "s_c1": dict(type="formule", titre="1 · Le taux de chômage", x=540, y=140, w=700, lignes=[
            dict(f="Actifs = 29 383 000 + 2 451 000", taille=34),
            dict(f="= 31 834 000", taille=34),
            dict(f="[[2 451|31 834]] × 100 ≈ 7,7 %", cadre=True, taille=38)]),
        "s_c2": dict(type="liste", titre="2 · Taux ou part ?", x=540, y=140, w=700, petit=True, items=[
            "Taux de chômage : chômeurs ÷ actifs",
            "Part de chômage : chômeurs ÷ toute la classe d'âge",
            "Beaucoup d'étudiants inactifs : dénominateur plus grand, part plus faible"]),
    }),

    # ================================================================ IX. partie 1
    dict(id="partie1", chap="Partie 1 · mobiliser ses connaissances", fond="canard", humeur="tension", beats=[
        "{ex_p1}Partie un de l'épreuve composée. Une question, sans document. Le sujet : "
        "« Montrez que les problèmes d'appariement peuvent être à l'origine d'un chômage structurel. » Trois virgule cinq points.",
        "{ex_p1.1}La méthode. « Montrez que » : un mécanisme qui va dans un sens. On ne discute pas. "
        "{ex_p1.2}On définit les notions du sujet. {ex_p1.3}Puis deux paragraphes bien séparés, avec chacun un mécanisme et un exemple.",
        "{-ex_p1}{pa_p1}À toi. Mets sur pause, et rédige : les définitions, puis deux paragraphes.",
        "{pa_p1.stop}{-pa_p1}{ex_p1c}{ex_p1c.q1}Correction. {s_p11}{s_p11.1}On définit. Le chômage structurel, c'est la part du chômage qui ne dépend pas de la conjoncture. "
        "{s_p11.2}L'appariement, c'est la rencontre entre une offre d'emploi et un demandeur. Quand elle se fait mal, chômeurs et emplois vacants coexistent.",
        "{-s_p11}{ex_p1c.q2}{s_p12}Premier paragraphe : les frictions. {s_p12.1}Même quand un poste correspond à un chômeur, il faut du temps : "
        "que l'information circule, que les candidatures soient examinées, que l'embauche se fasse. "
        "{s_p12.2}Pendant ce temps, la personne est au chômage. C'est le chômage frictionnel, qui existe même en période de forte activité.",
        "{-s_p12}{ex_p1c.q3}{s_p13}Deuxième paragraphe : les inadéquations. {s_p13.1}De qualifications : avec la destruction créatrice, "
        "les emplois créés demandent souvent des compétences que n'ont pas les personnes dont l'emploi a disparu. "
        "{s_p13.2}L'exemple chiffré : en deux mille vingt-cinq, selon l'Insee, quatorze virgule sept pour cent de chômage chez les actifs sans diplôme ou avec le brevet, "
        "contre cinq virgule trois pour les diplômés de bac plus deux ou plus.",
        "{s_p13.3}Et l'inadéquation spatiale : les emplois sont concentrés dans certaines métropoles, et des chômeurs vivent dans des territoires en déclin, "
        "sans pouvoir déménager facilement. {s_p13.4}Dans ces deux cas, le chômage persiste même si la demande globale est soutenue : il est structurel.",
        "{-s_p13}{-ex_p1c}",
    ], vis={
        "ex_p1": dict(type="exo", niveau="p1", titre="Montrez que les problèmes d'appariement peuvent être à l'origine d'un chômage structurel.",
                      src="Sujet inventé pour le site · 3,5 points · sans document",
                      enonce=["Une vingtaine de lignes, qui répondent exactement à la consigne."],
                      questions=["« Montrez que » : un mécanisme, dans un sens", "Définir les notions du sujet",
                                 "Deux paragraphes bien séparés : mécanisme et exemple"]),
        "pa_p1": dict(type="pause", t="Les définitions, puis deux paragraphes : les frictions, les inadéquations."),
        "ex_p1c": dict(type="exo", mode="coin", niveau="p1", titre="L'appariement et le chômage structurel",
                       questions=["Définir", "Paragraphe 1 : les frictions", "Paragraphe 2 : les inadéquations"]),
        "s_p11": dict(type="liste", titre="Définir", x=540, y=150, w=700, petit=True, items=[
            "Chômage structurel : la part du chômage indépendante de la conjoncture",
            "Appariement : rencontre d'une offre d'emploi et d'un demandeur"]),
        "s_p12": dict(type="liste", titre="Paragraphe 1 · les frictions", x=540, y=150, w=700, petit=True, items=[
            "Information, candidatures, embauche : il faut du temps",
            "Chômage frictionnel, même en forte activité"]),
        "s_p13": dict(type="liste", titre="Paragraphe 2 · les inadéquations", x=540, y=120, w=700, petit=True, items=[
            "Qualifications : la destruction créatrice déplace les emplois",
            "2025 : 14,7 % sans diplôme ou brevet, 5,3 % à bac + 2 ou plus (Insee)",
            "Spatiale : emplois dans les métropoles, chômeurs dans des territoires en déclin",
            "Le chômage persiste même avec une demande soutenue : structurel"], marques=["1", "+", "2", "→"]),
    }),

    # ================================================================ X. partie 2
    # 14,7 / 5,3 = 2,77 ; 14,7 − 5,3 = 9,4 points (graphique du site)
    dict(id="partie2", chap="Partie 2 · étudier un document", fond="nuit", humeur="tension", beats=[
        "{ex_p2}Partie deux : l'étude d'un document, cinq virgule cinq points. Le document : le graphique « Qui est le plus exposé au chômage ? », "
        "en deux mille vingt-cinq, d'après l'Insee. {ex_p2.1}Un : compare le taux de chômage des actifs sans diplôme, ou avec le brevet, "
        "et celui des diplômés de bac plus deux ou plus. {ex_p2.2}Deux : à l'aide du document et de tes connaissances, montre que le chômage touche inégalement les actifs.",
        "{-ex_p2}{pa_p2}À toi. Mets sur pause. Pour la question un, une donnée précise et un calcul. Pour la deux, des mécanismes.",
        "{pa_p2.stop}{-pa_p2}{ex_p2c}{ex_p2c.q1}{s_p21}Correction de la question un. {s_p21.1}Selon l'Insee, en deux mille vingt-cinq, en France, "
        "le taux de chômage des actifs sans diplôme ou avec le brevet est de quatorze virgule sept pour cent. Contre cinq virgule trois pour cent pour les diplômés de bac plus deux ou plus.",
        "{s_p21.2}Il est donc environ deux virgule huit fois plus élevé. {s_p21.3}Soit neuf virgule quatre points d'écart. "
        "Remarque : on écrit « points » pour une différence entre deux pourcentages.",
        "{-s_p21}{ex_p2c.q2}{s_p22}Question deux. {s_p22.1}D'abord, le constat : dix-sept virgule un pour cent de chômage chez les ouvriers peu qualifiés, contre quatre virgule zéro chez les cadres. "
        "{s_p22.2}Premier mécanisme : l'inadéquation des qualifications. Le progrès technique biaisé et la tertiarisation augmentent la demande de travail qualifié, "
        "et réduisent celle de travail peu qualifié et routinier.",
        "{s_p22.3}Deuxième mécanisme : le coût du travail. Quand la productivité d'un emploi est proche du salaire minimum, l'employeur hésite à embaucher. "
        "D'où les allègements de cotisations ciblés sur les bas salaires. "
        "{s_p22.4}Et on peut ajouter les jeunes : dix-neuf virgule huit pour cent de chômage. Ils sont en phase d'insertion, "
        "et occupent plus souvent des contrats courts, les premiers supprimés quand l'activité ralentit.",
        "{-s_p22}{-ex_p2c}",
    ], vis={
        "ex_p2": dict(type="exo", niveau="p2", titre="Le chômage selon le diplôme", src="Exercice du site, document Insee · 5,5 points",
                      enonce=["Document : « Qui est le plus exposé au chômage ? (2025) », Insee, enquête Emploi 2025."],
                      questions=["Comparez le taux de chômage des actifs sans diplôme (ou avec le brevet) et celui des diplômés de Bac + 2 ou plus.",
                                 "À l'aide du document et de vos connaissances, montrez que le chômage touche inégalement les actifs."]),
        "pa_p2": dict(type="pause", t="Question 1 : une donnée précise et un calcul. Question 2 : des mécanismes."),
        "ex_p2c": dict(type="exo", mode="coin", niveau="p2", titre="Le chômage selon le diplôme",
                       questions=["Comparer sans diplôme et Bac + 2", "Un chômage inégal : pourquoi ?"]),
        "s_p21": dict(type="formule", titre="Question 1 · comparer", x=540, y=150, w=700, lignes=[
            dict(f="Sans diplôme ou brevet : 14,7 % · Bac + 2 ou plus : 5,3 %", txt=True),
            dict(f="14,7 ÷ 5,3 ≈ 2,8 fois plus", cadre=True, taille=36),
            dict(f="14,7 − 5,3 = 9,4 points d'écart", cadre=True, taille=36)]),
        "s_p22": dict(type="liste", titre="Question 2 · un chômage inégal", x=540, y=110, w=700, petit=True, items=[
            "Constat : ouvriers peu qualifiés 17,1 %, cadres 4,0 %",
            "Inadéquation : progrès technique biaisé, tertiarisation",
            "Coût du travail : productivité proche du salaire minimum ; allègements ciblés",
            "Jeunes 19,8 % : insertion, contrats courts"]),
    }),

    # ================================================================ XI. partie 3
    dict(id="partie3", chap="Partie 3 · raisonner sur un dossier", fond="moutarde", humeur="tension", beats=[
        "{ex_p3}Partie trois : le raisonnement sur un dossier documentaire. Neuf points. Le sujet : "
        "« À l'aide du dossier, montrez que le chômage peut avoir des causes conjoncturelles. »",
        "{ex_p3.p1}Trois documents. Le graphique du taux de chômage en France, de mille neuf cent soixante-quinze à deux mille vingt-cinq. "
        "{ex_p3.p2}Le PIB en volume, qui recule de deux virgule huit pour cent en deux mille neuf. "
        "{ex_p3.p3}Et un texte : en deux mille neuf, les entreprises réduisent l'intérim et les heures supplémentaires avant de supprimer des emplois.",
        "{-ex_p3}{pa_p3}À toi. Mets sur pause et construis le plan : une introduction, deux parties avec leurs mécanismes et leurs documents, une conclusion.",
        "{pa_p3.stop}{-pa_p3}{li_p3}Correction. {li_p3.1}En introduction : le chômage conjoncturel est la part du chômage due à un ralentissement de l'activité. "
        "On montrera qu'un choc de demande réduit la production et l'emploi, puis que ce chômage peut s'auto-entretenir.",
        "{li_p3.2}Première partie : un ralentissement de la demande réduit la production et l'emploi. Le mécanisme, c'est la demande effective de Keynes : "
        "les entreprises produisent selon les ventes qu'elles anticipent. Le document deux montre la récession de deux mille neuf. "
        "Le document trois, l'ajustement par l'intérim et les heures, puis par l'emploi. Et le document un : sept virgule quatre pour cent en deux mille huit, neuf virgule un en deux mille neuf.",
        "{li_p3.3}Deuxième partie : le chômage conjoncturel s'auto-entretient. Moins d'emplois, donc moins de revenus, et une épargne de précaution. "
        "Donc moins de consommation et d'investissement, donc une nouvelle baisse de la demande. "
        "Le document un montre que la hausse continue jusqu'à dix virgule quatre pour cent en deux mille quinze, avec la crise de la zone euro. Et il y a un risque d'hystérèse.",
        "{li_p3.4}En conclusion : les fluctuations de l'activité expliquent une partie des variations du chômage. D'où les politiques de relance de la demande globale.",
        "{-li_p3}{note_p3}Et la règle d'or : pas de partie « limites » ! Un « montrez que » ne se discute pas. Il se démontre.",
        "{-note_p3}",
    ], vis={
        "ex_p3": dict(type="exo", niveau="p3", titre="Montrez que le chômage peut avoir des causes conjoncturelles.",
                      src="Sujet inventé pour le site · 9 points", y=80,
                      enonce=["Document 1 : le taux de chômage en France, 1975-2025 (Insee).",
                              "Document 2 : le PIB en volume recule de 2,8 % en 2009 (Insee).",
                              "Document 3 (texte factuel) : en 2009, les entreprises réduisent l'intérim et les heures supplémentaires avant de supprimer des emplois."]),
        "pa_p3": dict(type="pause", t="Introduction, deux parties (mécanisme et documents), conclusion."),
        "li_p3": dict(type="liste", titre="Le plan corrigé", x=110, y=100, w=1060, items=[
            "Introduction : définir le chômage conjoncturel, annoncer les deux idées",
            "I. Moins de demande, moins de production et d'emploi : Keynes · documents 2, 3 et 1",
            "II. Un chômage qui s'auto-entretient : revenus, consommation, demande · document 1, hystérèse",
            "Conclusion : les fluctuations expliquent une partie du chômage ; d'où la relance"],
            marques=["→", "I", "II", "✓"]),
        "note_p3": dict(type="note", titre="Règle d'or de la partie 3", cles=["démontre"],
                        t="Pas de partie « limites » : un « montrez que » ne se discute pas, il se démontre.", x=170, y=220, w=940),
    }),

    # ================================================================ XII. dissertation
    dict(id="dissertation", chap="La dissertation", fond="corail", humeur="tension", beats=[
        "{ex_d}Et la dissertation. Le sujet : « Les politiques de l'offre sont-elles suffisantes pour lutter contre le chômage ? »",
        "{ex_d.1}Analyse chaque mot : les politiques de l'offre, ce sont le coût du travail, la formation, la flexibilité. "
        "{ex_d.2}« Sont-elles suffisantes » appelle une réponse nuancée. {ex_d.3}Et mobilise tes connaissances, sans commenter le dossier document par document.",
        "{-ex_d}{pa_d}À toi. Mets sur pause : la problématique, puis le plan détaillé, en trois parties.",
        "{pa_d.stop}{-pa_d}{def_pb}Correction. La problématique. Les politiques de l'offre visent le chômage structurel. "
        "Peuvent-elles, à elles seules, faire baisser durablement le chômage… alors qu'une partie de celui-ci dépend de la demande ?",
        "{-def_pb}{cm_d}Le plan. {cm_d.1}Un : les politiques de l'offre agissent sur le chômage structurel. Alléger le coût du travail peu qualifié : "
        "les cotisations, le CICE devenu baisse de cotisations en deux mille dix-neuf. Former, pour réduire les inadéquations : le compte personnel de formation, l'apprentissage. "
        "Et flexibiliser, pour lever les rigidités : la rupture conventionnelle, les ordonnances de deux mille dix-sept, la flexicurité.",
        "{cm_d.2}Deux : mais elles ont des limites. Effets d'aubaine, coût budgétaire, trappes à bas salaires. La précarisation, et le dualisme du marché du travail. "
        "Et surtout, elles sont impuissantes face au chômage conjoncturel : en deux mille neuf, le PIB recule de deux virgule huit pour cent, "
        "et le chômage passe de sept virgule quatre à neuf virgule un pour cent.",
        "{cm_d.3}Trois : elles doivent donc être combinées à des politiques de la demande. La relance budgétaire et monétaire en récession, avec le multiplicateur, "
        "et le chômage partiel en deux mille vingt. Il faut éviter l'hystérèse : un chômage conjoncturel durable devient structurel. "
        "Et coordonner la demande au niveau européen.",
        ("P", 1.0),
        "Pourquoi ce plan ? Parce que « sont-elles suffisantes » appelle d'abord un oui, puis un « pas seules », puis une réponse construite.",
        "{-cm_d}",
    ], vis={
        "ex_d": dict(type="exo", niveau="dissert", titre="Les politiques de l'offre sont-elles suffisantes pour lutter contre le chômage ?",
                     src="Sujet inventé pour le site",
                     enonce=["Construis la problématique et le plan détaillé."],
                     questions=["Analyser chaque mot du sujet", "« Sont-elles suffisantes » appelle une réponse nuancée",
                                "Mobiliser ses connaissances, sans commenter le dossier document par document"]),
        "pa_d": dict(type="pause", t="La problématique, puis le plan détaillé : trois parties, deux ou trois sous-parties chacune."),
        "def_pb": dict(type="def", terme="Problématique", cles=["structurel", "durablement", "demande"],
                       t="Les politiques de l'offre visent le chômage structurel. Peuvent-elles à elles seules faire baisser durablement le chômage, alors qu'une partie de celui-ci dépend de la demande ?",
                       x=150, y=170, w=980),
        "cm_d": dict(type="plan", titre="Les politiques de l'offre sont-elles suffisantes contre le chômage ?", x=70, y=120, w=1140, parties=[
            dict(t="I. Elles agissent sur le structurel", items=["A. Coût du travail : cotisations, CICE (2013 → 2019)", "B. Formation : CPF, apprentissage",
                                                                  "C. Flexibilité : rupture conventionnelle, 2017, flexicurité"]),
            dict(t="II. Mais elles ont des limites", items=["A. Aubaine, coût budgétaire, trappes à bas salaires", "B. Précarisation, dualisme",
                                                            "C. Impuissantes face au conjoncturel : 2009, 7,4 % → 9,1 %"]),
            dict(t="III. À combiner avec la demande", items=["A. Relance en récession : multiplicateur, chômage partiel 2020", "B. Éviter l'hystérèse",
                                                             "C. Coordination européenne de la demande"])]),
    }),

    # ================================================================ XIII. récap
    dict(id="recap", chap="Pour le bac", fond="canard", humeur="lumiere", beats=[
        "{cm_r}On récapitule. {cm_r.1}Mesurer : le chômeur au sens du BIT, le taux de chômage, le taux d'emploi, le sous-emploi, le halo. "
        "{cm_r.2}Le chômage structurel : l'appariement, avec les frictions et les inadéquations. Et le salaire d'efficience.",
        "{cm_r.3}Les institutions : le salaire minimum et la protection de l'emploi, aux effets ambigus. Et le chômage conjoncturel : la demande effective, le cercle vicieux, l'hystérèse. "
        "{cm_r.4}Enfin, les politiques : la relance, les allègements, la formation, la flexibilisation.",
        "{-cm_r}{fr_r}Les repères, dans l'ordre. {fr_r.1}Ford et ses cinq dollars par jour, mille neuf cent quatorze. "
        "{fr_r.2}Keynes et la demande effective, mille neuf cent trente-six. {fr_r.3}Shapiro et Stiglitz, le salaire d'efficience, mille neuf cent quatre-vingt-quatre. "
        "{fr_r.4}Lindbeck et Snower, insiders et outsiders, mille neuf cent quatre-vingt-huit. {fr_r.5}Card et Krueger, le salaire minimum, mille neuf cent quatre-vingt-quatorze. "
        "{fr_r.6}Et Diamond, Mortensen et Pissarides, prix Nobel deux mille dix pour les frictions.",
        ("P", 4.0),
        "{-fr_r}{cf_r}{cf_r.1}Et trois chiffres à citer dans une copie. Sept virgule sept pour cent de chômage en deux mille vingt-cinq : deux millions et demi de personnes. "
        "{cf_r.2}Dix-neuf virgule huit pour cent chez les quinze-vingt-quatre ans actifs, contre cinq pour cent chez les cinquante ans ou plus. "
        "{cf_r.3}Et un virgule neuf million de personnes dans le halo du chômage.",
        ("P", 1.5),
        "{-cf_r}{fin}Les fiches à imprimer, le quiz, les cartes de révision et les animations de ce chapitre sont sur le site Faits et Courbes. "
        "Le lien est dans la description. Prochain dossier : les crises financières.",
        ("P", 2.5),
        "{-fin}",
    ], vis={
        "cm_r": dict(type="plan", titre="Le chômage : causes et politiques", x=60, y=140, w=1160, parties=[
            dict(t="Mesurer", items=["Chômeur BIT : trois critères", "Taux de chômage, taux d'emploi, sous-emploi, halo"]),
            dict(t="Le structurel", items=["Appariement : frictions, inadéquations", "Salaire d'efficience (Shapiro et Stiglitz)"]),
            dict(t="Institutions et conjoncture", items=["Salaire minimum, protection : effets ambigus", "Demande effective (Keynes), hystérèse"]),
            dict(t="Les politiques", items=["Relance de la demande", "Coût du travail, formation, flexibilité"])]),
        "fr_r": dict(type="frise", de=1900, a=2030, items=[
            dict(d=1914, nom="Ford", q="5 dollars par jour"), dict(d=1936, nom="Keynes", q="demande effective"),
            dict(d=1984, nom="Shapiro, Stiglitz", q="salaire d'efficience"), dict(d=1988, nom="Lindbeck, Snower", q="insiders / outsiders"),
            dict(d=1994, nom="Card, Krueger", q="salaire minimum"), dict(d=2010, nom="Diamond et al.", q="Nobel : frictions")]),
        "cf_r": dict(type="chiffres", titre="Trois chiffres à citer", x=90, y=150, w=1100,
                     items=[dict(n=c["n"], l=c["l"], s=c["s"]) for c in CHIF]),
        "fin": dict(type="titre", sur="Faits & Courbes · SES Terminale", t="Fiches, quiz et animations",
                    sous="Le lien est dans la description · prochain dossier : les crises financières"),
    }),
]

QUIZ = [
    dict(q="Pour être chômeur au sens du BIT, il faut notamment…",
         r=["être inscrit à France Travail", "être sans emploi, disponible et en recherche active", "toucher une allocation chômage"], ok=1,
         ex="Trois critères cumulés ; l'inscription et l'indemnisation n'en font pas partie.", voir="li_bit"),
    dict(q="Le taux de chômage rapporte le nombre de chômeurs…",
         r=["à la population totale", "à la population active", "au nombre de personnes en emploi"], ok=1,
         ex="Population active = personnes en emploi + chômeurs.", voir="fo_taux"),
    dict(q="Une personne à temps partiel qui souhaite travailler plus et est disponible est…",
         r=["en sous-emploi", "au chômage", "dans le halo du chômage"], ok=0,
         ex="Elle a un emploi, donc elle n'est pas chômeuse : elle est en sous-emploi.", voir="def_se"),
    dict(q="En 2020, le taux de chômage a baissé alors que l'activité s'effondrait, parce que…",
         r=["l'emploi a fortement augmenté", "des chômeurs ne pouvaient pas chercher et sont passés dans le halo", "le BIT a changé sa définition"], ok=1,
         ex="Sans recherche active, on n'est plus chômeur au sens du BIT : 8,1 % en 2020 contre 8,5 % en 2019.", voir="ex_2020"),
    dict(q="Le chômage frictionnel s'explique par…",
         r=["le temps nécessaire pour qu'offres et demandes d'emploi se rencontrent", "une baisse de la demande globale", "un salaire minimum trop élevé"], ok=0,
         ex="C'est un problème d'appariement, une composante du chômage structurel.", voir="an_app"),
    dict(q="Selon la théorie du salaire d'efficience, l'employeur paie plus que le salaire du marché pour…",
         r=["respecter le SMIC", "motiver, fidéliser et attirer les meilleurs salariés", "réduire ses impôts"], ok=1,
         ex="Il observe mal l'effort (asymétrie d'information) : un salaire élevé rend la perte d'emploi coûteuse.", voir="ch_eff"),
    dict(q="Card et Krueger (1994) ont montré qu'une hausse du salaire minimum au New Jersey…",
         r=["avait fait doubler le chômage", "n'avait pas entraîné de baisse de l'emploi dans les fast-foods", "avait fait fermer les fast-foods"], ok=1,
         ex="Comparaison avec la Pennsylvanie voisine : une expérience naturelle.", voir="au_ck"),
    dict(q="Des règles de protection de l'emploi fortes ont tendance à…",
         r=["réduire les licenciements en récession mais freiner les embauches en reprise", "faire baisser le chômage dans tous les cas", "augmenter la demande globale"], ok=0,
         ex="D'où un effet ambigu sur le niveau du chômage et un risque de dualisme.", voir="ch_pe"),
    dict(q="Entre 2008 et 2009, le taux de chômage en France est passé de…",
         r=["9,1 % à 7,4 %", "7,4 % à 9,1 %", "3,6 % à 5,0 %"], ok=1,
         ex="La récession de 2009 (PIB −2,8 %) a fait monter le chômage conjoncturel.", voir="li_09"),
    dict(q="Contre un chômage d'inadéquation des qualifications, la politique la plus adaptée est…",
         r=["la baisse des taux d'intérêt", "la formation", "la hausse des dépenses publiques"], ok=1,
         ex="La formation rapproche les compétences des besoins des entreprises.", voir="def_form"),
]

CREDITS = [
    "Données : Insee, enquête Emploi 2025 (Emploi, chômage, revenus du travail, juillet 2026 ; séries longues sur le marché du travail) ; "
    "Insee, comptes nationaux ; SMIC : service-public.fr (montant en vigueur depuis juin 2026).",
    "Graphiques, chaînes causales, animations et sujets : site Faits & Courbes (SES Terminale) ; les sujets sont inventés pour le site.",
    "Polices : IBM Plex Sans Condensed, Archivo, Spectral, JetBrains Mono (SIL Open Font License).",
]
