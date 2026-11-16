"""SES, S1 : « Comment est structurée la société française actuelle ? » — le chapitre en vidéo.

Même chaîne que le pilote ses_e1.py (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ; moteur
ses/serie/moteur.js. Illustrations propres à la vidéo (toupie de Mendras, espace social de Bourdieu) dans
ses/serie/illu-ses-s1.js.
Contenu : le chapitre S1 du site « Faits & Courbes » (outils/specialites/ses/src/data-s1.js, animations s1-pcs et
s1-marx-weber de data-anim-s1s2.js), rien au-delà. Graphiques, chaînes causales et animations lus dans les sources du
site (site_ses.py) ; les sujets corrigés sont ceux du site. Les nombres lus par la voix sont écrits en lettres.
Usage : python3 outils/serie-philo/verifier.py ses_s1 ; SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py ses_s1
(brouillon sans voix) ; chevauchements.py ses-s1.
"""
import site_ses

SITE = "ses"
CODE = "ses-s1"
NOTION = "La structure sociale"
NUM = 1
TITRE = "Comment est structurée la société française actuelle ?"
SUIVANT = "S2 · L'École et la société"
RYTHME = "vivant"
PRONONCIATION = {"Weber": "Vébère", "Max": "Maxe", "Karl": "Karle", "Engels": "Enguèlse", "Mendras": "Maindrasse",
                 "Chauvel": "Chovèl", "Ulrich": "Oulrik", "Beck": "Bèk", "Kimberlé": "Kimbèrlé", "Crenshaw": "Krènchô",
                 "Pinçon-Charlot": "Pinçon-Charlo", "Insee": "Inssé", "Dares": "Darèsse", "PCS": "pé-cé-èss",
                 "CSP": "cé-èss-pé", "CDI": "cé-dé-i", "VTC": "vé-té-cé", "Gini": "Djini", "Sauvy": "Sovi", "SES": "èss-eu-èss",
                 "AEI": "a-eu-i"}

D = site_ses.donnees()
G, CHN, CH = D["graphes"], D["chaines"], D["ch"]["s1"]
CHIF = CH["chiffres"]          # les trois « En chiffres » du chapitre

# les six groupes socioprofessionnels en 2024 : dernière année des séries du graphique s1-pcs du site (Insee)
G_GROUPES = dict(type="hbarres", t="Les six groupes socioprofessionnels en 2024",
                 s="Part de chaque groupe dans l'emploi, en % (0,9 % non renseigné).",
                 src="Source : Insee, enquête Emploi 2024.", unite=" %",
                 cats=["Agriculteurs exploitants", "Artisans, commerçants, chefs d'entreprise", "Cadres",
                       "Professions intermédiaires", "Employés", "Ouvriers"],
                 series=[dict(n="2024", v=[s["v"][-1] for s in G["s1-pcs"]["series"]])])
assert [s["n"][:5] for s in G["s1-pcs"]["series"]] == ["Agric", "Artis", "Cadre", "Profe", "Emplo", "Ouvri"]

# femmes et hommes en emploi, trois catégories : valeurs du graphique s1-sexe du site (Insee), rangées deux à deux
_F, _H = G["s1-sexe"]["series"][0]["v"], G["s1-sexe"]["series"][1]["v"]
_CATS = G["s1-sexe"]["cats"]
_IDX = [_CATS.index("Employés"), _CATS.index("Ouvriers"), _CATS.index("Cadres")]
G_SEXE = dict(type="hbarres", t="Femmes et hommes en emploi : trois catégories, 2024",
              s="Part de la catégorie parmi les femmes, puis parmi les hommes en emploi, en %.",
              src=G["s1-sexe"]["src"], unite=" %",
              cats=["Employées · parmi les femmes", "Employés · parmi les hommes", "Ouvrières · parmi les femmes",
                    "Ouvriers · parmi les hommes", "Cadres · parmi les femmes", "Cadres · parmi les hommes"],
              series=[dict(n="2024", v=[x for i in _IDX for x in (_F[i], _H[i])])])
assert G_SEXE["series"][0]["v"] == [38.8, 11.6, 7.2, 28.2, 20.4, 25.4]
assert G["s1-niveau"]["series"][0]["v"] == [13970, 26740, 48580]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="canard", humeur="mystere", carton=False, beats=[
        "{q_qui}Cadre, ouvrier, employé, agriculteur… Pour décrire quelqu'un, on cite souvent son métier. "
        "Mais est-ce que ça suffit pour savoir où il se situe dans la société ?",
        "{-q_qui}{cf_ouv}{cf_ouv.1}Un chiffre pour commencer. En deux mille vingt-quatre, vingt-trois pour cent des personnes en emploi sont cadres. "
        "En mille neuf cent quatre-vingt-deux, elles n'étaient que huit pour cent. Presque trois fois plus.",
        "{-cf_ouv}{q_ouv}La société française a changé à toute vitesse. Alors, est-ce qu'on peut encore parler de classes sociales, "
        "comme au temps de Marx ? Ou est-ce que tout le monde est devenu… classe moyenne ?",
        "{-q_ouv}{plan}Voilà le chemin. {plan.1}D'abord, les facteurs qui structurent et hiérarchisent la société. "
        "{plan.2}Ensuite, l'outil de l'Insee pour la décrire : les PCS. {plan.3}Puis les grandes transformations de l'emploi depuis les années cinquante. "
        "{plan.4}Les deux grandes théories des classes, Marx et Weber. {plan.5}Le débat : les classes sociales existent-elles encore ? "
        "{plan.6}Et pour finir, le bac, avec des sujets corrigés.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q_qui": dict(type="question", t="Ton métier suffit-il à dire où tu te situes dans la société ?"),
        "cf_ouv": dict(type="chiffres", titre="En chiffres", x=110, y=150, w=1060, items=[
            dict(n=CHIF[0]["n"], l=CHIF[0]["l"], s=CHIF[0]["s"])]),
        "q_ouv": dict(type="question", t="Des classes sociales… ou une immense classe moyenne ?"),
        "plan": dict(type="liste", titre="Le chemin", x=170, y=96, w=940, items=[
            "Un espace social structuré par sept facteurs", "Les PCS, l'outil de l'Insee",
            "Les grandes évolutions depuis 1950", "Les classes sociales : Marx et Weber",
            "Les classes sont-elles encore pertinentes ?", "Au bac : calcul, épreuve composée, dissertation"]),
        "titre": dict(type="titre", sur="SES · Terminale · S1", t="Comment est structurée la société française ?",
                      sous="Le chapitre complet, de zéro au bac"),
    }),

    # ================================================================ I. l'espace social
    dict(id="espace", chap="Un espace social, sept facteurs", fond="nuit", humeur="lumiere",
         retenir="L'espace social est structuré (des groupes qui se ressemblent) et hiérarchisé (un accès inégal aux ressources). "
                 "Sept facteurs : PCS, revenu, diplôme, composition du ménage, cycle de vie, sexe, lieu de résidence. Ils se cumulent.",
         beats=[
        "{def_esp}Les sociologues ont un mot pour ça : l'{!espace social}espace social. Chacun y occupe une position. "
        "Des positions plus ou moins proches, et plus ou moins élevées.",
        "{def_esp.1}Cet espace est structuré : il existe des groupes de gens qui se ressemblent. Et il est hiérarchisé : "
        "ces positions donnent un accès inégal aux ressources. Le revenu, le pouvoir, le prestige.",
        "{-def_esp}{li_fac}Qu'est-ce qui fixe ta position ? Le programme cite sept facteurs. Il faut les connaître tous les sept. "
        "{li_fac.1}La catégorie socioprofessionnelle. {li_fac.2}Le revenu. {li_fac.3}Le diplôme. {li_fac.4}La composition du ménage. "
        "{li_fac.5}La position dans le cycle de vie, c'est-à-dire l'âge. {li_fac.6}Le sexe. {li_fac.7}Et le lieu de résidence.",
        "On les prend un par un. La profession d'abord : elle résume beaucoup de choses. Le revenu, le diplôme, les conditions de travail, le mode de vie. "
        "C'est pour ça que l'Insee classe la population par professions. On y revient juste après.",
        ("P", 0.4),
        "{-li_fac}{gr_niv}Le revenu, ensuite. Regarde l'échelle des niveaux de vie en deux mille vingt-quatre, par unité de consommation. "
        "{gr_niv.2}Au milieu, la médiane : vingt-six mille sept cent quarante euros par an. La moitié de la population vit avec moins. "
        "Pour une personne seule, ça fait deux mille deux cent vingt-huit euros par mois.",
        "{gr_niv.1}Les dix pour cent les plus modestes vivent avec moins de treize mille neuf cent soixante-dix euros par an. "
        "{gr_niv.3}Et les dix pour cent les plus aisés, avec plus de quarante-huit mille cinq cent quatre-vingts euros.",
        "{-gr_niv}{cf_niv}{cf_niv.1}Divise l'un par l'autre : trois virgule quarante-huit. C'est le rapport interdécile. "
        "Le seuil des plus aisés est trois virgule quarante-huit fois plus élevé que le plafond des plus modestes.",
        "{cf_niv.2}Le taux de pauvreté atteint quinze virgule quatre pour cent : neuf virgule huit millions de personnes. "
        "C'est son plus haut niveau depuis mille neuf cent quatre-vingt-seize. {cf_niv.3}Et l'indice de Gini, zéro virgule trois cent deux, "
        "est au plus haut depuis le début de la série. Et le patrimoine ? Il est encore plus inégalement réparti que le revenu.",
        "{-cf_niv}{cols_dm}Troisième et quatrième facteurs. {cols_dm.g}Le diplôme conditionne l'accès aux emplois qualifiés, le salaire, le risque de chômage. "
        "Et même les pratiques culturelles, et la participation politique. Or il dépend lui-même de l'origine sociale.",
        "{cols_dm.d}La composition du ménage, maintenant. Vivre seul, en couple, avec ou sans enfants : ça change le niveau de vie. "
        "Les familles monoparentales, le plus souvent une mère avec ses enfants, sont, avec les chômeurs, les plus touchées par la pauvreté.",
        "{-cols_dm}{cols_as}{cols_as.g}Cinquième facteur : l'âge, la position dans le cycle de vie. À diplôme égal, on gagne plus en milieu de carrière qu'au début. "
        "Et le patrimoine s'accumule avec les années. Les jeunes, eux, cumulent emplois précaires et faible patrimoine.",
        "En deux mille vingt-quatre, d'ailleurs, le taux de pauvreté des retraités rejoint celui des actifs : dix virgule quatre pour cent.",
        "{cols_as.d}Sixième : le sexe. Femmes et hommes n'occupent pas les mêmes positions. Trente-huit virgule huit pour cent des femmes en emploi sont employées, "
        "contre onze virgule six pour cent des hommes. On y reviendra en détail.",
        "{-cols_as}{note_lieu}Et septième : le lieu de résidence. Une grande métropole, une ville moyenne, un village, un quartier prioritaire, ou les beaux quartiers. "
        "Le territoire concentre les ressources : les emplois qualifiés, les grandes écoles, les services. Et il façonne les fréquentations.",
        "Michel Pinçon et Monique Pinçon-Charlot ont montré comment la grande bourgeoisie entretient son {!entre-soi}entre-soi, "
        "dans quelques quartiers et quelques communes.",
        "{-note_lieu}{li_cum}Le plus important, maintenant. Ces facteurs ne s'additionnent pas seulement : ils se cumulent, et se renforcent. "
        "{li_cum.1}Un diplôme élevé donne accès à un emploi de cadre. {li_cum.2}Donc à un revenu élevé. "
        "{li_cum.3}Qui permet d'habiter un quartier favorisé. {li_cum.4}Où les enfants fréquentent des établissements réputés… et la boucle recommence.",
        "{-li_cum}{note_b26}Et retiens bien ce point, parce qu'il est déjà tombé. Le sujet du bac deux mille vingt-six, jour deux, partie trois, demandait de montrer "
        "que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l'espace social. On le corrigera à la fin.",
        "{-note_b26}",
    ], vis={
        "def_esp": dict(type="def", terme="Espace social", cles=["position", "structuré", "hiérarchisé"],
                        t="L'ensemble des positions sociales occupées par les individus, plus ou moins proches et plus ou moins élevées.",
                        etape="Structuré : des groupes qui se ressemblent · hiérarchisé : un accès inégal au revenu, au pouvoir, au prestige.",
                        x=170, y=170, w=940),
        "li_fac": dict(type="liste", titre="Les sept facteurs du programme", x=200, y=70, w=880, items=[
            "La catégorie socioprofessionnelle (PCS)", "Le revenu", "Le diplôme", "La composition du ménage",
            "La position dans le cycle de vie (l'âge)", "Le sexe", "Le lieu de résidence"]),
        "gr_niv": dict(type="donnees", g=G["s1-niveau"], kicker="Le revenu", x=60, y=110, w=1160, h=500, lab=330, dec=0, signe=False),
        "cf_niv": dict(type="chiffres", titre="Des écarts de niveau de vie", x=90, y=150, w=1100, items=[
            dict(n="3,48", l="Le plancher des 10 % les plus aisés ÷ le plafond des 10 % les plus modestes (D9 / D1), 2024.", s="Insee Première n° 2117"),
            dict(n="15,4 %", l="Taux de pauvreté en 2024 : 9,8 millions de personnes, le plus haut niveau depuis 1996.", s="Insee"),
            dict(n="0,302", l="L'indice de Gini en 2024 : au plus haut depuis le début de la série.", s="Insee")]),
        "cols_dm": dict(type="cols", g="Le diplôme", gq="Emplois qualifiés, salaire, risque de chômage, culture, vote ; lui-même lié à l'origine sociale.",
                        d="La composition du ménage", dq="Seul, en couple, avec ou sans enfants : les familles monoparentales sont parmi les plus pauvres.", vs="+"),
        "cols_as": dict(type="cols", g="Le cycle de vie", gq="Salaire plus élevé en milieu de carrière, patrimoine qui s'accumule ; jeunes précaires.",
                        d="Le sexe", dq="38,8 % des femmes en emploi sont employées, contre 11,6 % des hommes (2024).", vs="+"),
        "note_lieu": dict(type="note", titre="Le lieu de résidence", cles=["ressources", "entre-soi"],
                          t="Métropoles, villes moyennes, rural, quartiers prioritaires ou beaux quartiers : le territoire concentre les ressources. "
                            "La grande bourgeoisie entretient son entre-soi (Pinçon et Pinçon-Charlot).", x=170, y=180, w=940),
        "li_cum": dict(type="liste", titre="Des facteurs qui se cumulent", x=170, y=150, w=940, items=[
            "Un diplôme élevé → un emploi de cadre", "→ un revenu élevé", "→ un quartier favorisé",
            "→ des établissements réputés pour les enfants"], marques=["1", "2", "3", "4"]),
        "note_b26": dict(type="note", titre="Déjà tombé au bac", cles=["revenu", "diplôme"],
                         t="Bac 2026, jour 2, partie 3 : « Vous montrerez que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l'espace social. »",
                         x=170, y=200, w=940),
    }),

    # ================================================================ II. les PCS
    dict(id="pcs", chap="Les PCS, l'outil de l'Insee", fond="canard", humeur="calme",
         retenir="PCS : nomenclature de l'Insee (CSP en 1954, PCS en 1982, rénovée en 2003 et 2020) : profession, statut, qualification. "
                 "Six groupes en emploi. Les PCS ne sont pas des classes sociales.",
         beats=[
        "{def_pcs}Pour décrire cet espace, l'Insee a un outil : les {!PCS}PCS, les professions et catégories socioprofessionnelles. "
        "C'est une nomenclature : elle classe la population selon sa profession actuelle, ou l'ancienne.",
        "{def_pcs.1}Mais pas seulement le métier. Elle tient compte du statut, salarié ou non. De la qualification. "
        "De la taille de l'entreprise pour les indépendants. Et, pour les salariés, de l'employeur : public ou privé.",
        "{-def_pcs}{fr_pcs}Un peu d'histoire. {fr_pcs.1}Elle naît en mille neuf cent cinquante-quatre, sous le nom de CSP. "
        "{fr_pcs.2}Elle est refondue en mille neuf cent quatre-vingt-deux et devient la PCS. {fr_pcs.3}Puis rénovée en deux mille trois, "
        "{fr_pcs.4}et encore en deux mille vingt.",
        "L'idée : regrouper des personnes à la situation sociale proche, qui ont souvent des comportements semblables.",
        "{-fr_pcs}{gr_grp}Au niveau le plus agrégé, il y a six groupes pour les personnes en emploi. Voici leur poids en deux mille vingt-quatre. "
        "{gr_grp.1}Les agriculteurs exploitants : un virgule trois pour cent seulement. {gr_grp.2}Les artisans, commerçants et chefs d'entreprise : six virgule huit.",
        "{gr_grp.3}Les cadres et professions intellectuelles supérieures : vingt-trois pour cent. {gr_grp.4}Les professions intermédiaires : vingt-cinq virgule deux. "
        "{gr_grp.5}Les employés : vingt-quatre virgule huit. {gr_grp.6}Et les ouvriers : dix-huit pour cent.",
        "Le reste, zéro virgule neuf pour cent, n'est pas renseigné.",
        "{-gr_grp}{note_men}Une nouveauté de deux mille vingt : la PCS Ménage. Elle classe les ménages d'après la profession de leurs membres. "
        "Pourquoi ? Parce que la position sociale se joue souvent au niveau du couple.",
        "{-note_men}{cols_pc}Et maintenant, une distinction qui tombe souvent. {cols_pc.g}Les PCS sont un outil statistique. "
        "Elles sont construites sans aucune hypothèse sur la conscience ou les conflits des groupes. "
        "{cols_pc.d}Une classe sociale, c'est un concept sociologique, qui suppose des écarts durables. Et chez Marx, une conscience et une lutte.",
        "Les PCS ne sont donc pas des classes sociales. Mais elles servent à vérifier si des classes existent. "
        "Les écarts entre PCS, de revenu, de diplôme ou de pratiques, sont-ils grands ? Et durables ?",
        "{-cols_pc}",
    ], vis={
        "def_pcs": dict(type="def", terme="PCS · professions et catégories socioprofessionnelles", cles=["nomenclature", "profession"],
                        t="Nomenclature de l'Insee qui classe la population selon la profession, actuelle ou ancienne.",
                        etape="Aussi : le statut (salarié ou non), la qualification, la taille de l'entreprise, l'employeur public ou privé.",
                        x=170, y=170, w=940),
        "fr_pcs": dict(type="frise", de=1950, a=2025, items=[
            dict(d=1954, nom="CSP", q="la naissance"), dict(d=1982, nom="PCS", q="la refonte"),
            dict(d=2003, nom="Rénovation", q=""), dict(d=2020, nom="PCS 2020", q="et la PCS Ménage")]),
        "gr_grp": dict(type="donnees", g=G_GROUPES, kicker="Les six groupes", x=60, y=90, w=1160, h=560, lab=620, signe=False),
        "note_men": dict(type="note", titre="La PCS Ménage (2020)", cles=["ménages", "couple"],
                         t="Elle classe les ménages d'après la profession de leurs membres : la position sociale se joue souvent au niveau du couple.",
                         x=170, y=200, w=940),
        "cols_pc": dict(type="cols", g="Les PCS", gq="Un outil statistique, sans hypothèse sur la conscience ou les conflits des groupes.",
                        d="Les classes sociales", dq="Un concept sociologique : des écarts durables ; chez Marx, une conscience et un conflit.", vs="≠",
                        repere="Les PCS servent à vérifier si des classes existent"),
    }),

    # ================================================================ III. les évolutions
    dict(id="evolutions", chap="Quarante ans de transformations", fond="moutarde", humeur="lumiere",
         retenir="Quatre évolutions : salarisation (86,7 % de salariés en 2024), tertiarisation (76,6 % des emplois), élévation des qualifications "
                 "(cadres : 8,0 % en 1982, 23,0 % en 2024), féminisation (48,8 % des emplois), avec des emplois restés genrés.",
         beats=[
        "{an_pcs}Maintenant, faisons tourner le film. L'évolution des groupes, de mille neuf cent quatre-vingt-deux à deux mille vingt-quatre. "
        "{an_pcs.1}En mille neuf cent quatre-vingt-deux, les ouvriers sont le premier groupe : vingt-neuf virgule neuf pour cent des personnes en emploi. "
        "Les cadres ne sont que huit pour cent. Et les agriculteurs encore sept virgule cinq.",
        "{an_pcs.2}Les années quatre-vingt-dix : les employés grimpent, près de trente pour cent de l'emploi. Les ouvriers et les agriculteurs reculent.",
        "{an_pcs.3}Les années deux mille : la montée des qualifications s'accélère. Les cadres passent de quatorze virgule sept à dix-huit virgule trois pour cent, "
        "entre deux mille deux et deux mille douze.",
        "{an_pcs.4}Et en deux mille vingt-quatre : vingt-trois pour cent de cadres, dix-huit pour cent d'ouvriers. Les agriculteurs, un virgule trois pour cent. "
        "Et pour la première fois depuis mille neuf cent quatre-vingt-deux, les professions intermédiaires dépassent les employés.",
        ("P", 0.8),
        "{-an_pcs}{ca_ev}Derrière ces courbes, le programme retient quatre grandes évolutions. {ca_ev.1}La salarisation. "
        "{ca_ev.2}La tertiarisation. {ca_ev.3}L'élévation du niveau de qualification. Et une quatrième, la féminisation, qu'on verra juste après.",
        "{-ca_ev}{cf_sal}{cf_sal.1}La salarisation, d'abord. C'est la hausse de la part des salariés dans l'emploi. "
        "En deux mille vingt-quatre, quatre-vingt-six virgule sept pour cent des personnes en emploi sont salariées. "
        "Et soixante-douze virgule neuf pour cent sont en CDI, ou fonctionnaires.",
        "Pourquoi ? Parce que les agriculteurs exploitants, les petits commerçants et les artisans ont reculé depuis les années cinquante.",
        "{cf_sal.2}Mais attention, une nuance. Les indépendants regagnent un peu de terrain : treize virgule trois pour cent, leur plus haut niveau depuis mille neuf cent quatre-vingt-dix-neuf. "
        "{cf_sal.3}Portés par les micro-entrepreneurs : trois virgule six pour cent de l'emploi. Les plateformes de livraison, les VTC, les services.",
        "{-cf_sal}{cf_ter}{cf_ter.1}La tertiarisation, ensuite. Le commerce, les transports, la santé, l'éducation, l'administration, les services aux entreprises : "
        "le tertiaire rassemble soixante-seize virgule six pour cent des emplois. {cf_ter.2}L'industrie, douze virgule six pour cent. "
        "La construction, six virgule six. Et l'agriculture, deux virgule trois.",
        "{cf_ter.3}Et ce mouvement concerne surtout les femmes : quatre-vingt-sept pour cent d'entre elles travaillent dans le tertiaire.",
        "{-cf_ter}{vi_ter}Mais pourquoi ce basculement vers les services ? Suivons-le dans une petite économie. "
        "{vi_ter.1}Au départ, d'énormes gains de productivité dans l'agriculture, puis dans l'industrie. Des machines, des tracteurs, des robots.",
        "{vi_ter.2}Résultat : il faut moins de travailleurs pour produire autant.",
        "{vi_ter.3}En même temps, les revenus augmentent. Et avec eux, de nouveaux besoins : la santé, l'éducation, les loisirs, le commerce.",
        "{vi_ter.4}Alors les emplois se déversent vers les services. C'est le déversement, l'idée d'Alfred Sauvy.",
        "{-vi_ter}{ch_ter}{ch_ter.1}En chaîne causale, pour ta copie. Des gains de productivité forts dans l'agriculture, puis dans l'industrie. "
        "{ch_ter.2}Donc, d'un côté, il faut moins de travailleurs pour produire autant. Et de l'autre, les revenus augmentent : de nouveaux besoins de services apparaissent.",
        "{ch_ter.3}Donc les emplois se déversent vers les services. {ch_ter.4}Et en même temps, les petites exploitations et les petits commerces reculent "
        "face aux grandes entreprises. {ch_ter.5}Résultat : tertiarisation… et salarisation.",
        "{ch_ter.tout}",
        ("P", 1.2),
        "{-ch_ter}{ch_qua}{ch_qua.1}Troisième évolution : l'élévation du niveau de qualification. Au départ, l'allongement des études : la massification scolaire. "
        "{ch_qua.2}Donc plus de diplômés arrivent sur le marché du travail. {ch_qua.3}Et en même temps, le progrès technique et la tertiarisation "
        "demandent davantage de qualifications.",
        "{ch_qua.4}Donc les emplois de cadres et de professions intermédiaires se multiplient, et les emplois peu qualifiés reculent.",
        "Cadres et professions intermédiaires, ensemble, c'est un peu plus de quarante-huit pour cent des personnes en emploi en deux mille vingt-quatre. "
        "Près de la moitié. Et les ouvriers non qualifiés reculent, avec l'automatisation et les délocalisations.",
        "{-ch_qua}",
    ], vis={
        "an_pcs": dict(type="sanim", nom="s1-pcs", x=60, y=88, h=520),
        "ca_ev": dict(type="cartes", items=[
            dict(ic="loi", t="Salarisation", q="Plus de salariés, moins d'indépendants."),
            dict(ic="infra", t="Tertiarisation", q="Les services dominent l'emploi."),
            dict(ic="humain", t="Qualification", q="Plus de cadres et de professions intermédiaires.")]),
        "cf_sal": dict(type="chiffres", titre="La salarisation", x=90, y=150, w=1100, items=[
            dict(n="86,7 %", l="des personnes en emploi sont salariées en 2024 (72,9 % en CDI ou fonctionnaires).", s="Insee, enquête Emploi 2024"),
            dict(n="13,3 %", l="d'indépendants : leur plus haut niveau depuis 1999.", s="Insee, enquête Emploi 2024"),
            dict(n="3,6 %", l="de l'emploi : les micro-entrepreneurs (livraison, VTC, services).", s="Insee, enquête Emploi 2024")]),
        "cf_ter": dict(type="chiffres", titre="La tertiarisation", x=90, y=150, w=1100, items=[
            dict(n="76,6 %", l="des emplois sont dans le tertiaire en 2024.", s="Insee"),
            dict(n="12,6 %", l="dans l'industrie, contre 6,6 % dans la construction et 2,3 % dans l'agriculture.", s="Insee"),
            dict(n="87,0 %", l="des femmes en emploi travaillent dans le tertiaire.", s="Insee")]),
        "vi_ter": dict(type="ville", titre="Pourquoi l'emploi s'est tertiarisé", kicker="Le déversement",
                       base=["usine", "magasin", "maisons"],
                       noms=dict(usine="Agriculture, industrie", magasin="Services", maisons="Ménages"),
                       flux=[dict(de="usine", a="magasin", k="biens"), dict(de="usine", a="maisons", k="revenus", l="salaires"),
                             dict(de="maisons", a="magasin", k="achats")],
                       etapes=[
                           dict(machine="usine", etiquette=dict(h="Gains de productivité", s="dans l'agriculture, puis dans l'industrie", sur="usine")),
                           dict(etiquette=dict(h="Moins de travailleurs", s="pour produire autant", sur="usine")),
                           dict(flux=[dict(de="usine", a="maisons", k="revenus", l="salaires", n=1.6)], foule=2.4,
                                etiquette=dict(h="Les revenus augmentent", s="nouveaux besoins : santé, éducation, loisirs", sur="maisons")),
                           dict(flux=[dict(de="usine", a="magasin", k="emplois", l="déversement")], grandit=["magasin"],
                                etiquette=dict(h="Les emplois se déversent", s="vers les services (Alfred Sauvy)", sur="magasin"), cam="tout")]),
        "ch_ter": dict(type="chaine", c=CHN["s1-tert"], x=170, w=940),
        "ch_qua": dict(type="chaine", c=CHN["s1-qualif"], x=190, w=900),
    }),

    # ================================================================ IV. la féminisation
    dict(id="feminisation", chap="La féminisation des emplois", fond="corail", humeur="mystere",
         retenir="Féminisation : 48,8 % des personnes en emploi sont des femmes (2024). Mais des emplois genrés : 38,8 % des femmes en emploi "
                 "sont employées contre 11,6 % des hommes ; 28,2 % des hommes sont ouvriers contre 7,2 % des femmes.",
         beats=[
        "{cf_fem}{cf_fem.1}Quatrième évolution : la féminisation des emplois. En deux mille vingt-quatre, les femmes représentent quarante-huit virgule huit pour cent "
        "des personnes en emploi. Quatorze virgule deux millions, sur vingt-neuf millions.",
        "{cf_fem.2}Leur taux d'emploi reste pourtant inférieur à celui des hommes : soixante-six virgule deux pour cent chez les quinze à soixante-quatre ans, "
        "contre soixante et onze virgule cinq pour cent.",
        "{-cf_fem}{li_fem}Comment expliquer leur entrée massive dans l'emploi, depuis les années soixante ? Quatre raisons. "
        "{li_fem.1}L'allongement de leurs études. {li_fem.2}La tertiarisation, qui crée des emplois de services. "
        "{li_fem.3}La maîtrise de la fécondité. {li_fem.4}Et l'évolution des normes.",
        "{-li_fem}{gr_sexe}Mais les femmes et les hommes ne font pas les mêmes métiers. Les emplois restent {!genrés}genrés. Regarde. "
        "{gr_sexe.1}Trente-huit virgule huit pour cent des femmes en emploi sont employées : aides à domicile, secrétaires, agentes d'entretien, vendeuses. "
        "{gr_sexe.2}Chez les hommes ? Onze virgule six pour cent seulement.",
        "{gr_sexe.3}À l'inverse, sept virgule deux pour cent des femmes sont ouvrières. {gr_sexe.4}Contre vingt-huit virgule deux pour cent des hommes.",
        "{gr_sexe.5}Et les cadres ? La part progresse chez les femmes : vingt virgule quatre pour cent. {gr_sexe.6}Mais elle reste plus faible que chez les hommes : vingt-cinq virgule quatre.",
        "{-gr_sexe}{note_lec}Et attention à la lecture, c'est un piège classique. Trente-huit virgule huit pour cent, c'est la part des employées parmi les femmes en emploi. "
        "Ce n'est pas la part des femmes parmi les employés ! Ça, c'est une autre information, beaucoup plus élevée.",
        "Une astuce : commence toujours ta phrase par le groupe qui fait cent pour cent. Ici : « sur cent femmes en emploi »…",
        "{-note_lec}",
    ], vis={
        "cf_fem": dict(type="chiffres", titre="La féminisation", x=90, y=150, w=1100, items=[
            dict(n="48,8 %", l="des personnes en emploi sont des femmes en 2024 (14,2 millions sur 29,0 millions).", s="Insee"),
            dict(n="66,2 %", l="taux d'emploi des femmes de 15 à 64 ans, contre 71,5 % pour les hommes.", s="Insee")]),
        "li_fem": dict(type="liste", titre="Pourquoi les femmes sont entrées dans l'emploi", x=170, y=160, w=940, items=[
            "L'allongement de leurs études", "La tertiarisation", "La maîtrise de la fécondité", "L'évolution des normes"]),
        "gr_sexe": dict(type="donnees", g=G_SEXE, kicker="Des emplois genrés", x=60, y=90, w=1160, h=560, lab=430, signe=False,
                        couleurs=["sa", "canard", "sa", "canard", "sa", "canard"]),
        "note_lec": dict(type="note", titre="Le piège du sens de lecture", cles=["femmes", "employés"],
                         t="38,8 % des femmes en emploi sont employées. Ce n'est pas « 38,8 % des employés sont des femmes » (une part beaucoup plus élevée).",
                         x=170, y=200, w=940),
    }),

    # ================================================================ V. Marx et Weber
    dict(id="marxweber", chap="Les classes sociales : Marx et Weber", fond="nuit", humeur="tension",
         retenir="Marx : classes définies par les rapports de production, bourgeoisie / prolétariat, classe en soi et pour soi, approche réaliste. "
                 "Weber : trois ordres (classes, groupes de statut, partis), approche nominaliste, stratification.",
         beats=[
        "{def_cl}Venons-en aux classes sociales. Une classe sociale, c'est un grand groupe d'individus qui partagent une position comparable dans la hiérarchie sociale : "
        "revenus, patrimoine, pouvoir, prestige.",
        "{def_cl.1}Et, selon les approches, des intérêts, un mode de vie, une conscience communs. Ce « selon les approches », c'est tout le débat entre Marx et Weber.",
        "{-def_cl}{au_marx}Karl Marx, d'abord. Pour lui, les classes se définissent par leur place dans les {!rapports de production}rapports de production. "
        "Une seule question : possèdes-tu les moyens de production ? Les usines, les machines, les terres.",
        "La bourgeoisie les possède. Le prolétariat, lui, n'a que sa force de travail à vendre. Et la société capitaliste tend à se bipolariser entre ces deux classes, "
        "aux intérêts opposés.",
        "{-au_marx}{an_mw}Voyons ça en mouvement. {an_mw.1}Une seule ligne de partage : la propriété des moyens de production. "
        "D'un côté, la bourgeoisie, peu nombreuse. De l'autre, le prolétariat.",
        "{an_mw.2}Le prolétaire vend sa force de travail. Le bourgeois s'approprie la {!plus-value}plus-value : la valeur créée par le travail, au-delà du salaire versé. "
        "C'est l'exploitation.",
        "{an_mw.3}Et quand les ouvriers prennent conscience de leurs intérêts communs, ils se mobilisent : c'est la lutte des classes.",
        "{an_mw.4}{an_mw.5}{-an_mw}{cols_soi}Ce passage est essentiel chez Marx. {cols_soi.g}Une classe en soi, c'est une position objective commune. "
        "Des gens qui occupent la même place dans la production… qu'ils le sachent ou non.",
        "{cols_soi.d}Une classe pour soi, c'est une classe qui a pris conscience de ses intérêts, et qui se mobilise collectivement. "
        "Pour Marx, une classe n'existe pleinement que si elle est à la fois en soi et pour soi.",
        "{-cols_soi}{ch_marx}{ch_marx.1}En chaîne causale. La propriété, ou non, des moyens de production. "
        "{ch_marx.2}Donc le prolétariat doit vendre sa force de travail à la bourgeoisie. {ch_marx.3}Donc la bourgeoisie s'approprie la plus-value : l'exploitation.",
        "{ch_marx.4}Donc des intérêts opposés : la classe en soi existe objectivement. {ch_marx.5}Et si elle prend conscience, elle devient classe pour soi : la lutte des classes.",
        "{-ch_marx}{note_real}C'est une approche {!réaliste}réaliste : les classes existent réellement, et elles sont en conflit. "
        "Pour Marx, la lutte des classes est même le moteur de l'histoire. C'est la thèse du Manifeste du parti communiste, écrit avec Engels en mille huit cent quarante-huit.",
        "{-note_real}{au_web}Max Weber, maintenant, plus d'un demi-siècle plus tard. Pour lui, la hiérarchie sociale n'a pas une dimension, mais {!trois}trois, indépendantes.",
        "{-au_web}{an_mw2}{an_mw2.1}{an_mw2.2}{an_mw2.3}{an_mw2.4}Trois échelles. L'ordre économique, d'abord : les classes, définies par les chances d'accès aux biens et aux revenus sur le marché. "
        "L'ordre social : les groupes de statut, définis par le prestige, l'honneur social, qui se traduisent par des styles de vie. "
        "Et l'ordre politique : les partis, qui visent le pouvoir.",
        "{an_mw2.5}Et ces échelles ne coïncident pas toujours. Prends un professeur des écoles : un revenu moyen, sur l'échelle économique. "
        "Mais un prestige plutôt élevé, sur l'échelle sociale. Et un commerçant aisé ? Un revenu supérieur… mais moins de prestige.",
        "Ces décalages, Weber permet de les penser. L'approche de Marx, centrée sur la propriété, les laisse de côté. Tout ça est dans Économie et société, en mille neuf cent vingt-deux.",
        "{-an_mw2}{cmp_mw}Faisons le tableau, celui qu'il faut avoir en tête. {cmp_mw.1}Le critère : chez Marx, la place dans les rapports de production. "
        "Chez Weber, trois ordres : économique, social, politique.",
        "{cmp_mw.2}L'approche : réaliste chez Marx, les classes existent et s'opposent. {!nominaliste}Nominaliste chez Weber : les classes sont des regroupements construits par le chercheur.",
        "{cmp_mw.3}La conscience : indispensable chez Marx, c'est la classe pour soi. Pas nécessaire chez Weber : les classes ne sont pas forcément des communautés.",
        "{cmp_mw.4}Et les relations : le conflit, la lutte des classes, chez Marx. Une hiérarchie graduée chez Weber : on parle de {!stratification}stratification sociale.",
        ("P", 1.0),
        "{-cmp_mw}{au_bou}Et un troisième nom, qui fait la synthèse : Pierre Bourdieu. Dans La Distinction, en mille neuf cent soixante-dix-neuf.",
        "{-au_bou}{ill_bou}Son espace social se lit selon deux axes. {ill_bou.1}Verticalement, le volume global de capital : beaucoup, ou peu. "
        "{ill_bou.2}Horizontalement, sa structure : la part du capital économique, et la part du capital culturel.",
        "{ill_bou.3}Le professeur a plus de capital culturel. Le commerçant aisé, plus de capital économique. Et les classes se distinguent aussi par leurs goûts, "
        "leurs styles de vie. D'où le titre : La Distinction.",
        "{-ill_bou}",
    ], vis={
        "def_cl": dict(type="def", terme="Classe sociale", cles=["position", "conscience"],
                       t="Grand groupe d'individus qui partagent une position comparable dans la hiérarchie sociale (revenus, patrimoine, pouvoir, prestige).",
                       etape="Et, selon les approches, des intérêts, un mode de vie et une conscience communs.", x=170, y=170, w=940),
        "au_marx": dict(type="auteur", mono="KM", nom="Karl Marx", info="1818-1883 · Manifeste du parti communiste, avec Engels, 1848",
                        cles=["rapports", "bourgeoisie", "prolétariat"],
                        t="Les classes se définissent par leur place dans les rapports de production : la bourgeoisie possède les moyens de production, le prolétariat n'a que sa force de travail.",
                        x=170, y=210, w=940),
        "an_mw": dict(type="sanim", nom="s1-marx-weber", x=60, y=88, h=520),
        "cols_soi": dict(type="cols", g="Classe en soi", gq="Une position objective commune dans la production.",
                         d="Classe pour soi", dq="La conscience de ses intérêts et la mobilisation collective.", vs="→",
                         repere="Chez Marx, une classe n'existe pleinement que si elle est les deux"),
        "ch_marx": dict(type="chaine", c=CHN["s1-marx"], x=190, w=900),
        "note_real": dict(type="note", titre="Une approche réaliste", cles=["réaliste", "conflit", "histoire"],
                          t="Les classes existent réellement et sont en conflit : la lutte des classes, moteur de l'histoire (Manifeste du parti communiste, 1848).",
                          x=170, y=200, w=940),
        "au_web": dict(type="auteur", mono="MW", nom="Max Weber", info="1864-1920 · Économie et société, 1922", cles=["trois"],
                       t="La hiérarchie sociale a trois dimensions indépendantes : économique (les classes), sociale (les groupes de statut), politique (les partis).",
                       x=170, y=210, w=940),
        "an_mw2": dict(type="sanim", nom="s1-marx-weber", x=60, y=88, h=520),
        "cmp_mw": dict(type="compare", titre="Marx et Weber", x=70, y=96, w=1140, cols=["Marx", "Weber"], lignes=[
            ["Critère", "La place dans les rapports de production", "Trois ordres : économique, social, politique"],
            ["Approche", "Réaliste : les classes existent et s'opposent", "Nominaliste : des regroupements construits par le chercheur"],
            ["Conscience", "Indispensable (classe pour soi)", "Pas nécessaire : pas forcément des communautés"],
            ["Relations", "Conflit, lutte des classes", "Hiérarchie graduée : stratification"]]),
        "au_bou": dict(type="auteur", mono="PB", nom="Pierre Bourdieu", info="1930-2002 · La Distinction, 1979", cles=["volume", "structure"],
                       t="L'espace social se lit selon le volume global de capital et sa structure (capital économique, capital culturel) ; les classes se distinguent aussi par leurs goûts.",
                       x=170, y=210, w=940),
        "ill_bou": dict(type="illu", nom="bourdieu", x=110, y=100, w=1060, h=540),
    }),

    # ================================================================ VI. le débat
    dict(id="debat", chap="Les classes sociales existent-elles encore ?", fond="corail", humeur="tension",
         retenir="Quatre terrains de débat : distances inter-classes (moyennisation de Mendras / retour des classes de Chauvel), "
                 "distances intra-classes (hétérogénéité), rapports de genre, identifications subjectives et individualisation (Beck).",
         beats=[
        "{q_deb}Alors, la grande question : les classes sociales permettent-elles encore de décrire la France d'aujourd'hui ?",
        "{-q_deb}{li_deb}Le programme cite quatre terrains de débat. Et pour chacun, il faut connaître les arguments des deux côtés. "
        "{li_deb.1}Les distances entre classes. {li_deb.2}Les distances au sein des classes. {li_deb.3}L'articulation avec les rapports de genre. "
        "{li_deb.4}Et les identifications subjectives, avec l'individualisation.",
        "{-li_deb}{au_men}Premier terrain : les distances entre les classes. Henri Mendras, en mille neuf cent quatre-vingt-huit, dans La Seconde Révolution française.",
        "Selon lui, la hausse des revenus, la consommation de masse et la croissance des professions intermédiaires font émerger une immense "
        "{!constellation centrale}constellation centrale.",
        "{-au_men}{ill_top}Imagine la forme de la société. {ill_top.1}Elle ressemblait à une pyramide : peu de monde en haut, beaucoup en bas. "
        "Elle prend la forme d'une {!toupie}toupie : un ventre énorme au milieu.",
        "{ill_top.2}Ce gonflement des catégories du milieu, et le rapprochement des modes de vie, c'est la {!moyennisation}moyennisation.",
        "{-ill_top}{li_ecart}Mais d'autres constats montrent que les écarts ne disparaissent pas. {li_ecart.1}Les inégalités de niveau de vie atteignent, en deux mille vingt-quatre, "
        "leur plus haut niveau depuis le début des séries, en mille neuf cent quatre-vingt-seize. {li_ecart.2}Le patrimoine est très concentré. "
        "{li_ecart.3}Et les écarts de réussite scolaire, et d'accès aux grandes écoles, restent forts.",
        "{-li_ecart}{au_chau}D'où la thèse de Louis Chauvel, en deux mille un : « Le retour des classes sociales ? ». "
        "Depuis les années quatre-vingt, la réduction des inégalités s'est arrêtée.",
        "Il parle de {!classes sans conscience}classes sans conscience. Les écarts objectifs persistent. Mais la conscience de classe, elle, s'est affaiblie. "
        "En langage de Marx : des classes en soi… sans classes pour soi.",
        "{-au_chau}{cols_intra}Deuxième terrain : les distances au sein des classes. {cols_intra.g}Les grands groupes sont devenus hétérogènes. "
        "Les ouvriers ne sont plus surtout des hommes de la grande industrie : beaucoup travaillent dans la logistique, le transport, l'entretien.",
        "Les employés se divisent entre qualifiés et peu qualifiés : en deux mille vingt-quatre, dix-sept pour cent des femmes en emploi sont employées peu qualifiées. "
        "Et les cadres du public et ceux du privé n'ont ni les mêmes revenus, ni les mêmes votes. Cette hétérogénéité affaiblit l'unité de chaque classe.",
        "{cols_intra.d}Mais on peut aussi regrouper ouvriers et employés en classes populaires. Quarante-deux virgule huit pour cent des personnes en emploi, en deux mille vingt-quatre. "
        "Et leurs conditions de vie restent proches.",
        "{-cols_intra}{note_gen}Troisième terrain : le genre. Raisonner seulement en classes oublie une chose. "
        "Les femmes et les hommes d'une même classe n'ont pas la même position : écarts de salaire, temps partiel, tâches domestiques, {!plafond de verre}plafond de verre.",
        "Pendant longtemps, la position sociale d'une femme a même été mesurée… par celle de son conjoint. "
        "Les rapports de genre se combinent aux rapports de classe : une ouvrière cumule deux formes de domination.",
        "{-note_gen}{def_inter}Pour aller plus loin : la juriste Kimberlé Crenshaw a proposé en mille neuf cent quatre-vingt-neuf la notion d'{!intersectionnalité}intersectionnalité, "
        "pour penser le croisement des rapports de classe, de genre et de race.",
        "{-def_inter}{q_cm}Et quatrième terrain : les identifications subjectives. Pose-toi la question : qui, autour de toi, se dit « ouvrier », ou « bourgeois » ?",
        "{-q_cm}{cf_syn}Peu de monde. Beaucoup se rangent dans une vaste « classe moyenne ». Et les organisations qui portaient la conscience de classe ont reculé. "
        "{cf_syn.1}En France, environ dix pour cent des salariés sont syndiqués. Un sur dix, seulement.",
        "{-cf_syn}{ch_ind}{ch_ind.1}Pourquoi ? Parce que les facteurs d'individualisation se multiplient. La hausse du niveau de vie, de l'éducation, la protection sociale. "
        "{ch_ind.2}Donc les individus dépendent moins de leur groupe d'origine.",
        "{ch_ind.3}Donc les trajectoires se diversifient : les mobilités, les études, les familles recomposées, les consommations, les loisirs. "
        "{ch_ind.4}Donc les identités deviennent plurielles : le métier, le genre, la génération, le territoire, les goûts. "
        "{ch_ind.5}Et le sentiment d'appartenir à une classe s'affaiblit.",
        "{-ch_ind}{au_beck}C'est la thèse d'Ulrich Beck, dans La Société du risque, en mille neuf cent quatre-vingt-six. "
        "L'individu doit construire lui-même sa trajectoire. Les appartenances collectives, dont la classe, perdent de leur force.",
        "{-au_beck}{note_pin}Sauf peut-être… tout en haut. Michel Pinçon et Monique Pinçon-Charlot voient dans la grande bourgeoisie une classe encore pleinement "
        "« en soi et pour soi ». Un patrimoine transmis. Des réseaux. Un entre-soi résidentiel et scolaire. Et une défense collective de ses intérêts.",
        "{-note_pin}{def_concl}Alors, que conclure ? Les classes sociales au sens de Marx, avec la conscience et la lutte, sont moins visibles. "
        "{def_concl.1}Mais des écarts objectifs durables, cumulatifs, et transmis entre générations existent toujours.",
        "D'où des positions intermédiaires : des classes sans conscience, avec Chauvel. Ou une analyse multidimensionnelle de l'espace social, avec Weber et Bourdieu.",
        "{-def_concl}",
    ], vis={
        "q_deb": dict(type="question", t="Les classes sociales décrivent-elles encore la France d'aujourd'hui ?"),
        "li_deb": dict(type="liste", titre="Quatre terrains de débat", x=170, y=160, w=940, items=[
            "Les distances entre classes (inter-classes)", "Les distances au sein des classes (intra-classes)",
            "L'articulation avec les rapports de genre", "Les identifications subjectives et l'individualisation"]),
        "au_men": dict(type="auteur", mono="HM", nom="Henri Mendras", info="1927-2003 · La Seconde Révolution française 1965-1984, 1988",
                       cles=["constellation"],
                       t="Hausse des revenus, consommation de masse, croissance des professions intermédiaires : une vaste constellation centrale émerge.",
                       x=170, y=210, w=940),
        "ill_top": dict(type="illu", nom="toupie", x=110, y=100, w=1060, h=540),
        "li_ecart": dict(type="liste", titre="Mais les écarts persistent", x=170, y=160, w=940, items=[
            "Inégalités de niveau de vie au plus haut depuis 1996 (Insee, 2024)", "Un patrimoine très concentré",
            "Des écarts de réussite scolaire et d'accès aux grandes écoles"]),
        "au_chau": dict(type="auteur", mono="LC", nom="Louis Chauvel", info="né en 1967 · « Le retour des classes sociales ? », 2001",
                        cles=["conscience"],
                        t="Depuis les années 1980, la réduction des inégalités s'est arrêtée : des « classes sans conscience ».",
                        x=170, y=210, w=940),
        "cols_intra": dict(type="cols", g="Des classes hétérogènes", gq="Ouvriers de la logistique, employés qualifiés ou non, cadres du public ou du privé.",
                           d="Des classes populaires", dq="Ouvriers et employés : 42,8 % des personnes en emploi (2024), des conditions de vie proches.", vs="↔"),
        "note_gen": dict(type="note", titre="Classe et genre", cles=["salaire", "domination"],
                         t="Dans une même classe, femmes et hommes n'ont pas la même position : salaire, temps partiel, tâches domestiques, plafond de verre. "
                           "Une ouvrière cumule deux formes de domination.", x=170, y=190, w=940),
        "def_inter": dict(type="def", terme="Intersectionnalité", plus=True, cles=["croisement"],
                          t="Notion proposée par la juriste Kimberlé Crenshaw en 1989 : le croisement des rapports de classe, de genre et de race.",
                          x=170, y=200, w=940),
        "q_cm": dict(type="question", t="Qui, autour de toi, se dit « ouvrier » ou « bourgeois » ?"),
        "cf_syn": dict(type="chiffres", titre="Une conscience qui s'efface", x=170, y=170, w=940, items=[
            dict(n="1 sur 10", l="Environ un salarié sur dix est syndiqué en France.", s="Dares, 2019")]),
        "ch_ind": dict(type="chaine", c=CHN["s1-indiv"], x=170, w=940),
        "au_beck": dict(type="auteur", mono="UB", nom="Ulrich Beck", info="1944-2015 · La Société du risque, 1986", cles=["trajectoire", "collectives"],
                        t="L'individu doit construire lui-même sa trajectoire ; les appartenances collectives, dont la classe, perdent de leur force.",
                        x=170, y=210, w=940),
        "note_pin": dict(type="note", titre="En haut de l'échelle", cles=["bourgeoisie", "soi"],
                         t="Pour Pinçon et Pinçon-Charlot, la grande bourgeoisie reste une classe « en soi et pour soi » : patrimoine, réseaux, entre-soi, défense de ses intérêts.",
                         x=170, y=190, w=940),
        "def_concl": dict(type="def", terme="Conclusion à retenir", cles=["visibles", "durables"],
                          t="Les classes au sens de Marx (conscience et lutte) sont moins visibles.",
                          etape="Mais des écarts objectifs durables, cumulatifs et transmis existent toujours : « classes sans conscience » ou analyse multidimensionnelle.",
                          x=170, y=170, w=940),
    }),

    # ================================================================ VII. pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="nuit", humeur="tension", beats=[
        "{cmp_p1}Avant le bac, six pièges qui coûtent des points. {cmp_p1.1}Un : « les PCS sont les classes sociales de la France ». "
        "Non. Les PCS sont une nomenclature statistique. Les classes, un concept sociologique.",
        "{cmp_p1.2}Deux : chez Weber, le statut, ce n'est pas le statut d'emploi, salarié ou non. C'est le prestige, l'honneur social, et le style de vie qui va avec.",
        "{cmp_p1.3}Trois : la moyennisation ne veut pas dire que les inégalités ont disparu. C'est le gonflement du milieu, et le rapprochement des modes de vie. "
        "Les inégalités de revenu, et surtout de patrimoine, persistent.",
        "{-cmp_p1}{cmp_p2}{cmp_p2.1}Quatre : « la part des cadres a augmenté de quinze pour cent ». Faux ! Elle a augmenté de quinze {!points}points. "
        "De huit à vingt-trois pour cent : une multiplication par deux virgule neuf.",
        "{cmp_p2.2}Cinq : le sens de lecture. Trente-huit virgule huit pour cent des femmes en emploi sont employées. Pas trente-huit virgule huit pour cent des employés.",
        "{cmp_p2.3}Et six : ne citer que la profession et le revenu. Le programme cite sept facteurs, et ils se cumulent.",
        "{-cmp_p2}",
    ], vis={
        "cmp_p1": dict(type="compare", titre="Les pièges · 1 à 3", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["1 · PCS", "« Les PCS sont les classes sociales. »", "Une nomenclature statistique ; les classes : un concept sociologique."],
            ["2 · Statut", "« Chez Weber, le statut, c'est salarié ou non. »", "Le groupe de statut : le prestige et le style de vie."],
            ["3 · Moyennisation", "« Les inégalités ont disparu. »", "Le milieu gonfle ; les inégalités de revenu et de patrimoine persistent."]]),
        "cmp_p2": dict(type="compare", titre="Les pièges · 4 à 6", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["4 · Points", "« La part des cadres a augmenté de 15 %. »", "De 15 points (8,0 % → 23,0 %) : ×2,9."],
            ["5 · Lecture", "« 38,8 % des employés sont des femmes. »", "38,8 % des femmes en emploi sont employées."],
            ["6 · Facteurs", "Ne citer que la PCS et le revenu.", "Sept facteurs, qui se cumulent."]]),
    }),

    # ================================================================ VIII. au bac
    dict(id="epreuve", chap="Ce chapitre au bac", fond="canard", humeur="lumiere", beats=[
        "{li_ep}Passons au bac. L'écrit de SES dure quatre heures, au coefficient seize, et tu choisis entre deux sujets. "
        "Soit l'épreuve composée, en trois parties : {li_ep.1}la mobilisation des connaissances, sur trois virgule cinq points, "
        "{li_ep.2}l'étude d'un document, sur cinq virgule cinq points, {li_ep.3}et le raisonnement sur un dossier documentaire, sur neuf points. "
        "{li_ep.4}Soit la dissertation, appuyée sur un dossier documentaire.",
        "Ce barème s'applique à partir de la session deux mille vingt-sept. Et dans les deux sujets, deux points sur vingt sont réservés à l'orthographe et à la syntaxe.",
        "{-li_ep}{li_aei}Une méthode revient partout : le paragraphe {!AEI}AEI. "
        "{li_aei.1}A : affirmer l'idée. {li_aei.2}E : expliquer le mécanisme, avec une chaîne causale. "
        "{li_aei.3}I : illustrer, par un exemple précis, chiffré ou daté. Dans ce chapitre, tu as tous les chiffres de l'Insee qu'il faut.",
        "Mais d'abord, un savoir-faire indispensable : lire et calculer avec des pourcentages.",
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

    # ================================================================ IX. savoir-faire : lire l'évolution des PCS
    # 18,0 − 29,9 = −11,9 ; 23,0 − 8,0 = +15,0 ; 23,0 / 8,0 = 2,875 (≈ 2,9) ; (23,0 − 8,0) / 8,0 = +187,5 % (exercice du site)
    dict(id="calcul", chap="Savoir-faire · points et pourcentages", fond="nuit", humeur="calme", beats=[
        "{ex_c}Voici l'exercice, avec les données de l'Insee. La part des ouvriers dans l'emploi : vingt-neuf virgule neuf pour cent en mille neuf cent quatre-vingt-deux, "
        "dix-huit pour cent en deux mille vingt-quatre. Celle des cadres : huit pour cent, puis vingt-trois pour cent.",
        "Trois questions. {ex_c.1}Un : calcule l'écart en points pour chaque catégorie. {ex_c.2}Deux : calcule le coefficient multiplicateur de la part des cadres. "
        "{ex_c.3}Trois : rédige une phrase de lecture pour deux mille vingt-quatre.",
        "{-ex_c}{pa_c}À toi. Mets la vidéo sur pause, et fais les calculs à la main.",
        "{pa_c.stop}{-pa_c}{ex_cc}{ex_cc.q1}Correction. {s_c1}{s_c1.1}Quand on compare deux pourcentages, l'écart s'exprime en points de pourcentage. "
        "{s_c1.2}Ouvriers : dix-huit, moins vingt-neuf virgule neuf. Moins onze virgule neuf points. "
        "{s_c1.3}Cadres : vingt-trois, moins huit. Plus quinze points.",
        "{-s_c1}{ex_cc.q2}{s_c2}{s_c2.1}Deux : le coefficient multiplicateur, c'est l'arrivée divisée par le départ. Vingt-trois divisé par huit. "
        "Huit fois trois, vingt-quatre : c'est un peu moins de trois. Deux virgule huit cent soixante-quinze, environ deux virgule neuf. La part des cadres a presque triplé.",
        "{s_c2.2}Et en taux de variation ? Plus cent quatre-vingt-sept virgule cinq pour cent. Tu vois pourquoi « plus quinze pour cent » serait une énorme erreur.",
        "{-s_c2}{ex_cc.q3}{s_c3}{s_c3.1}Trois, la phrase de lecture. Elle donne la source, le lieu, la date, et ce que mesure le chiffre : "
        "« Selon l'Insee, en deux mille vingt-quatre, en France, vingt-trois pour cent des personnes en emploi sont cadres. »",
        "{-s_c3}{-ex_cc}",
    ], vis={
        "ex_c": dict(type="exo", niveau="calcul", titre="Lire l'évolution des PCS", src="Exercice du site, données Insee", y=90,
                     enonce=["Part dans l'emploi (Insee) : ouvriers 29,9 % en 1982, 18,0 % en 2024 · cadres 8,0 % en 1982, 23,0 % en 2024."],
                     questions=["Calcule l'écart en points pour chaque catégorie.",
                                "Calcule le coefficient multiplicateur de la part des cadres.",
                                "Rédige une phrase de lecture pour 2024."]),
        "pa_c": dict(type="pause", t="Deux écarts en points, un coefficient multiplicateur, une phrase."),
        "ex_cc": dict(type="exo", mode="coin", niveau="calcul", titre="Lire l'évolution des PCS",
                      donnees=["Ouvriers : 29,9 % → 18,0 %", "Cadres : 8,0 % → 23,0 %"],
                      questions=["Écarts en points ?", "Coefficient multiplicateur ?", "Phrase de lecture ?"]),
        "s_c1": dict(type="formule", titre="1 · Les écarts en points", x=540, y=150, w=700, lignes=[
            dict(f="écart = arrivée − départ (en points)", taille=34),
            dict(f="Ouvriers : 18,0 − 29,9 = −11,9 points", cadre=True, taille=34),
            dict(f="Cadres : 23,0 − 8,0 = +15,0 points", cadre=True, taille=34)]),
        "s_c2": dict(type="formule", titre="2 · Le coefficient multiplicateur", x=540, y=170, w=700, lignes=[
            dict(f="23,0 ÷ 8,0 ≈ 2,9", cadre=True, taille=36, n="la part a presque triplé"),
            dict(f="taux de variation : +187,5 % (pas +15 %)", taille=32)]),
        "s_c3": dict(type="formule", titre="3 · La phrase de lecture", x=540, y=170, w=700, lignes=[
            dict(f="« Selon l'Insee, en 2024, en France, 23,0 % des personnes en emploi sont cadres. »", txt=True),
            dict(f="Source, lieu, date, ce que mesure le chiffre.", txt=True, pt=True)]),
    }),

    # ================================================================ X. partie 1
    dict(id="partie1", chap="Partie 1 · mobiliser ses connaissances", fond="canard", humeur="tension", beats=[
        "{ex_p1}Partie un : la mobilisation des connaissances. Le sujet : « Distinguez l'analyse des classes sociales de Marx et celle de Weber. » "
        "Trois virgule cinq points, sans document.",
        "{ex_p1.1}Le verbe, c'est « distinguez » : il faut deux analyses, nettement séparées, et montrer en quoi elles diffèrent. "
        "{ex_p1.2}Une phrase de définition pour commencer. {ex_p1.3}Puis un paragraphe pour Marx, un paragraphe pour Weber.",
        "{-ex_p1}{pa_p1}À toi. Mets sur pause et rédige : une définition, deux paragraphes.",
        "{pa_p1.stop}{-pa_p1}{ex_p1c}{ex_p1c.q1}Correction. {s_p11}{s_p11.1}On définit : une classe sociale est un grand groupe d'individus "
        "qui occupent une position comparable dans la hiérarchie sociale. {s_p11.2}Et on annonce : Marx et Weber en proposent deux analyses différentes.",
        "{-s_p11}{ex_p1c.q2}{s_p12}{s_p12.1}Marx, d'abord. Un critère unique : la place dans les rapports de production. "
        "{s_p12.2}La bourgeoisie possède les moyens de production, le prolétariat ne possède que sa force de travail, qu'il vend contre un salaire. "
        "La bourgeoisie s'approprie la plus-value : c'est l'exploitation. D'où des intérêts opposés, et un conflit.",
        "{s_p12.3}Et une classe n'existe pleinement que si elle passe de classe en soi à classe pour soi. L'approche est réaliste et conflictuelle.",
        "{-s_p12}{ex_p1c.q3}{s_p13}{s_p13.1}Weber, au contraire, distingue trois dimensions. {s_p13.2}L'ordre économique, avec les classes : les chances d'accès aux biens et aux revenus. "
        "L'ordre social, avec les groupes de statut : le prestige. L'ordre politique, avec les partis : le pouvoir.",
        "{s_p13.3}Ces dimensions ne coïncident pas toujours : un enseignant a plus de prestige que de revenu. "
        "{s_p13.4}L'approche est nominaliste : les classes sont des catégories construites par le sociologue, sans conscience ni conflit nécessaires. "
        "Elle conduit à une vision en termes de stratification.",
        "{-s_p13}{-ex_p1c}",
    ], vis={
        "ex_p1": dict(type="exo", niveau="p1", titre="Distinguez l'analyse des classes sociales de Marx et celle de Weber.",
                      src="Sujet inventé pour le site · 3,5 points · sans document",
                      enonce=["Une réponse organisée, qui répond exactement à la consigne."],
                      questions=["Repérer le verbe : « distinguez » = deux analyses nettement séparées", "Définir la notion du sujet",
                                 "Un paragraphe Marx, un paragraphe Weber"]),
        "pa_p1": dict(type="pause", t="Une définition, un paragraphe Marx, un paragraphe Weber."),
        "ex_p1c": dict(type="exo", mode="coin", niveau="p1", titre="Marx et Weber",
                       questions=["Définir et annoncer", "Paragraphe 1 : Marx", "Paragraphe 2 : Weber"]),
        "s_p11": dict(type="liste", titre="Définir et annoncer", x=540, y=170, w=700, petit=True, items=[
            "Classe sociale : un grand groupe qui occupe une position comparable dans la hiérarchie sociale",
            "Marx et Weber : deux analyses différentes"]),
        "s_p12": dict(type="liste", titre="Paragraphe 1 · Marx", x=540, y=130, w=700, petit=True, items=[
            "Un critère unique : la place dans les rapports de production",
            "Bourgeoisie / prolétariat → plus-value, exploitation → intérêts opposés, conflit",
            "Classe en soi → classe pour soi : approche réaliste et conflictuelle"], marques=["1", "2", "3"]),
        "s_p13": dict(type="liste", titre="Paragraphe 2 · Weber", x=540, y=110, w=700, petit=True, items=[
            "Trois dimensions de la hiérarchie sociale",
            "Classes (revenus) · groupes de statut (prestige) · partis (pouvoir)",
            "Elles ne coïncident pas : un enseignant a plus de prestige que de revenu",
            "Approche nominaliste : la stratification"], marques=["1", "2", "3", "4"]),
    }),

    # ================================================================ XI. partie 2
    # 38,8 / 11,6 = 3,345 (≈ 3,3) ; 38,8 − 11,6 = 27,2 points (exercice du site)
    dict(id="partie2", chap="Partie 2 · étudier un document", fond="nuit", humeur="tension", beats=[
        "{ex_p2}Place à la partie deux, l'étude d'un document, notée sur cinq points et demi.",
        "Le document, tu le connais : femmes et hommes en emploi selon la catégorie socioprofessionnelle, "
        "en deux mille vingt-quatre, d'après l'Insee. Deux questions.",
        "{ex_p2.1}Un : compare la part des employés parmi les femmes et parmi les hommes en emploi. "
        "{ex_p2.2}Deux : à l'aide du document et de tes connaissances, montre que le sexe est un facteur de structuration de l'espace social.",
        "{-ex_p2}{pa_p2}À toi. Mets sur pause : un calcul pour la question un, un raisonnement pour la question deux.",
        "{pa_p2.stop}{-pa_p2}{ex_p2c}{ex_p2c.q1}{s_p21}{s_p21.1}Correction de la question un. Une phrase qui donne la source, la date, les deux chiffres : "
        "selon l'Insee, en France en deux mille vingt-quatre, trente-huit virgule huit pour cent des femmes en emploi sont employées, contre onze virgule six pour cent des hommes.",
        "{s_p21.2}Puis on compare. Trente-huit virgule huit divisé par onze virgule six : environ trois virgule trois. La proportion est trois virgule trois fois plus élevée chez les femmes. "
        "{s_p21.3}Et l'écart : vingt-sept virgule deux points.",
        "{-s_p21}{ex_p2c.q2}{s_p22}Question deux. {s_p22.1}Le sexe structure l'espace social, parce que femmes et hommes n'occupent pas les mêmes positions. "
        "Le document montre une forte ségrégation professionnelle : les femmes sont concentrées chez les employées et dans les professions intermédiaires, "
        "vingt-sept virgule trois pour cent, dans la santé, l'enseignement, le social. Les hommes, chez les ouvriers : vingt-huit virgule deux pour cent, contre sept virgule deux.",
        "{s_p22.2}Le sexe hiérarchise aussi : les hommes sont plus souvent cadres, vingt-cinq virgule quatre pour cent contre vingt virgule quatre, et chefs d'entreprise.",
        "{s_p22.3}Pourquoi ? Une socialisation différenciée oriente filles et garçons vers des formations et des métiers différents. "
        "Et la répartition inégale des tâches domestiques pèse sur les carrières des femmes : temps partiel, plafond de verre. "
        "{s_p22.4}Résultat : des écarts de salaire et de pouvoir.",
        "{-s_p22}{-ex_p2c}",
    ], vis={
        "ex_p2": dict(type="exo", niveau="p2", titre="Femmes, hommes et catégories socioprofessionnelles", src="Exercice du site, document Insee · 5,5 points",
                      enonce=["Document : « Femmes et hommes en emploi selon la catégorie socioprofessionnelle, 2024 » (Insee, enquête Emploi)."],
                      questions=["Comparez la part des employés parmi les femmes et parmi les hommes en emploi.",
                                 "À l'aide du document et de vos connaissances, montrez que le sexe est un facteur de structuration de l'espace social."]),
        "pa_p2": dict(type="pause", t="Question 1 : un calcul. Question 2 : un raisonnement appuyé sur le document."),
        "ex_p2c": dict(type="exo", mode="coin", niveau="p2", titre="Femmes, hommes et PCS",
                       donnees=["Employés : F 38,8 % · H 11,6 %", "Ouvriers : F 7,2 % · H 28,2 %", "Cadres : F 20,4 % · H 25,4 %",
                                "Prof. intermédiaires : F 27,3 %"],
                       questions=["Comparer la part des employés", "Le sexe structure l'espace social"]),
        "s_p21": dict(type="liste", titre="Question 1 · comparer", x=540, y=150, w=700, petit=True, items=[
            "Insee, France, 2024 : 38,8 % des femmes en emploi sont employées, contre 11,6 % des hommes",
            "38,8 ÷ 11,6 ≈ 3,3 : une proportion 3,3 fois plus élevée chez les femmes",
            "38,8 − 11,6 = 27,2 points d'écart"]),
        "s_p22": dict(type="liste", titre="Question 2 · le raisonnement", x=540, y=110, w=700, petit=True, items=[
            "Structure : ségrégation professionnelle (employées, professions intermédiaires 27,3 % / ouvriers 28,2 % contre 7,2 %)",
            "Hiérarchise : hommes plus souvent cadres (25,4 % contre 20,4 %) et chefs d'entreprise",
            "Socialisation différenciée ; tâches domestiques : temps partiel, plafond de verre",
            "→ des écarts de salaire et de pouvoir"]),
    }),

    # ================================================================ XII. partie 3 (sujet officiel 2026)
    dict(id="partie3", chap="Partie 3 · le sujet de 2026", fond="moutarde", humeur="tension", beats=[
        "{ex_p3}Partie trois : le raisonnement sur un dossier documentaire. Et cette fois, un vrai sujet : celui du bac deux mille vingt-six, jour deux, "
        "où cette partie valait dix points. Elle en vaudra neuf à partir de deux mille vingt-sept. Le sujet : « Vous montrerez que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l'espace social. »",
        "Les documents du sujet officiel ne sont pas reproduits ici. On s'appuie sur les données de ce chapitre : les catégories selon le sexe, le niveau de vie, "
        "la pauvreté des familles monoparentales.",
        "{-ex_p3}{note_pg}Mais d'abord, le piège du sujet. Il est énorme. {note_pg.1}Ne fais pas une partie sur le revenu et le diplôme ! "
        "Le sujet demande les autres facteurs. Lis bien : « ne sont pas les seuls ».",
        "{-note_pg}{pa_p3}À toi. Mets sur pause et construis le plan : quels facteurs, avec quels exemples ?",
        "{pa_p3.stop}{-pa_p3}{li_p3}Correction. {li_p3.1}En introduction, on définit l'espace social : l'ensemble des positions sociales, structuré en groupes "
        "et hiérarchisé selon l'accès aux ressources. Le revenu et le diplôme y jouent un rôle central. Mais d'autres facteurs interviennent.",
        "{li_p3.2}Un : la profession et le sexe structurent et hiérarchisent. La PCS, avec ses conditions de travail, son prestige, son mode de vie : "
        "les cadres représentent vingt-trois pour cent de l'emploi. Le sexe : trente-huit virgule huit pour cent des femmes sont employées, contre onze virgule six pour cent des hommes. "
        "Avec des écarts de salaire, et le temps partiel.",
        "{li_p3.3}Deux : la composition du ménage et le cycle de vie. Les familles monoparentales sont parmi les plus touchées par la pauvreté. "
        "Les jeunes sont plus exposés à la précarité. Et le patrimoine s'accumule avec l'âge.",
        "{li_p3.4}Trois : le lieu de résidence. Les ressources se concentrent dans les métropoles. Quartiers prioritaires contre beaux quartiers. "
        "L'entre-soi de la grande bourgeoisie, avec Pinçon et Pinçon-Charlot. Et un effet sur la scolarité, et les réseaux.",
        "{li_p3.5}En conclusion : ces facteurs se cumulent avec le revenu et le diplôme. L'espace social est multidimensionnel.",
        "{-li_p3}",
    ], vis={
        "ex_p3": dict(type="exo", niveau="p3", titre="Montrez que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l'espace social.",
                      src="Sujet officiel : bac 2026, jour 2 (France), partie 3 · 10 points en 2026, 9 points à partir de 2027", y=90,
                      enonce=["Les documents du sujet officiel ne sont pas reproduits : appuie-toi sur les données du chapitre "
                              "(catégories selon le sexe, niveau de vie, pauvreté des familles monoparentales)."]),
        "note_pg": dict(type="def", terme="Le piège du sujet", cles=["autres"],
                        t="Ne pas faire une partie sur le revenu et le diplôme.",
                        etape="Le sujet demande les autres facteurs : « ne sont pas les seuls ».", x=170, y=180, w=940),
        "pa_p3": dict(type="pause", t="Quels autres facteurs ? Chacun avec un mécanisme et un exemple."),
        "li_p3": dict(type="liste", titre="Le plan corrigé", x=110, y=90, w=1060, items=[
            "Introduction : définir l'espace social ; revenu et diplôme centraux, mais pas seuls",
            "I. La profession et le sexe : cadres 23,0 % ; femmes employées 38,8 % contre 11,6 %",
            "II. Le ménage et le cycle de vie : familles monoparentales, jeunes précaires, patrimoine et âge",
            "III. Le lieu de résidence : métropoles, quartiers, entre-soi (Pinçon et Pinçon-Charlot)",
            "Conclusion : des facteurs qui se cumulent ; un espace multidimensionnel"],
            marques=["→", "I", "II", "III", "✓"]),
    }),

    # ================================================================ XIII. dissertation
    dict(id="dissertation", chap="La dissertation", fond="corail", humeur="tension", beats=[
        "{ex_d}Et la dissertation. Le sujet : « Les classes sociales permettent-elles encore de rendre compte de la société française actuelle ? »",
        "{ex_d.1}« Permettent-elles encore » : le mot encore est capital. Il appelle une comparaison dans le temps. "
        "{ex_d.2}Et la question est ouverte : on attend un oui, un non… et une réponse construite.",
        "{-ex_d}{pa_d}À toi. Mets sur pause : la problématique, puis le plan détaillé, en trois parties.",
        "{pa_d.stop}{-pa_d}{def_pb}Correction. La problématique. La société française a profondément changé depuis les années cinquante : "
        "salarisation, tertiarisation, qualification, féminisation. Les classes sociales, définies par Marx ou Weber, décrivent-elles encore une société "
        "où les identités semblent plus individuelles ? Ou faut-il d'autres outils ?",
        "{-def_pb}{cm_d}Et le plan. {cm_d.1}Un : des classes sociales qui restent pertinentes. Des écarts objectifs durables et cumulatifs : "
        "le rapport interdécile de trois virgule quarante-huit, un indice de Gini au plus haut, le patrimoine, le diplôme. "
        "Une reproduction et un entre-soi : la grande bourgeoisie, et des classes populaires qui pèsent quarante-deux virgule huit pour cent de l'emploi. "
        "Et des styles de vie qui restent distincts, avec Bourdieu.",
        "{cm_d.2}Deux : une pertinence remise en cause. La moyennisation, avec Mendras, et la tertiarisation brouillent les frontières. "
        "Les classes sont hétérogènes. Et la conscience de classe s'affaiblit : l'individualisation, avec Beck, et une syndicalisation autour de dix pour cent.",
        "{cm_d.3}Trois : une analyse à enrichir. Des classes sans conscience, avec Chauvel. Articuler la classe avec le genre, l'âge, le territoire. "
        "Et une approche multidimensionnelle, avec Weber et Bourdieu, plutôt qu'une simple bipolarisation.",
        ("P", 1.0),
        "{-cm_d}",
    ], vis={
        "ex_d": dict(type="exo", niveau="dissert", titre="Les classes sociales permettent-elles encore de rendre compte de la société française actuelle ?",
                     src="Sujet inventé pour le site",
                     enonce=["Construis la problématique et le plan détaillé."],
                     questions=["« Encore » : une comparaison dans le temps", "Une question ouverte : une réponse nuancée et construite"]),
        "pa_d": dict(type="pause", t="La problématique, puis le plan détaillé en trois parties."),
        "def_pb": dict(type="def", terme="Problématique", cles=["changé", "outils"],
                       t="La société a profondément changé depuis les années 1950. Les classes sociales décrivent-elles encore une société aux identités plus individuelles, ou faut-il d'autres outils ?",
                       x=150, y=170, w=980),
        "cm_d": dict(type="plan", titre="Les classes sociales permettent-elles encore de rendre compte de la société ?", x=70, y=110, w=1140, parties=[
            dict(t="I. Des classes encore pertinentes", items=["A. Écarts durables : D9/D1 = 3,48, Gini au plus haut",
                                                              "B. Reproduction, entre-soi ; classes populaires 42,8 %", "C. Styles de vie distincts (Bourdieu)"]),
            dict(t="II. Une pertinence remise en cause", items=["A. Moyennisation (Mendras), tertiarisation", "B. Des classes hétérogènes",
                                                               "C. Individualisation (Beck), syndicalisation ≈ 10 %"]),
            dict(t="III. Une analyse à enrichir", items=["A. Classes sans conscience (Chauvel)", "B. Classe et genre, âge, territoire",
                                                        "C. Approche multidimensionnelle (Weber, Bourdieu)"])]),
    }),

    # ================================================================ XIV. récap
    dict(id="recap", chap="Pour le bac", fond="canard", humeur="lumiere", beats=[
        "{cm_r}On récapitule. Au centre, l'espace social, structuré et hiérarchisé. {cm_r.1}Sept facteurs, qui se cumulent : la PCS, le revenu, le diplôme, "
        "le ménage, l'âge, le sexe, le lieu de résidence. {cm_r.2}Quatre évolutions : salarisation, tertiarisation, qualification, féminisation.",
        "{cm_r.3}Deux théories des classes : Marx et les rapports de production, Weber et ses trois ordres. "
        "{cm_r.4}Et le débat : moyennisation ou classes sans conscience, hétérogénéité, genre, individualisation.",
        "{-cm_r}{fr_r}Les auteurs, dans l'ordre. {fr_r.1}Marx et Engels, mille huit cent quarante-huit. {fr_r.2}Weber, mille neuf cent vingt-deux. "
        "{fr_r.3}Bourdieu, mille neuf cent soixante-dix-neuf. {fr_r.4}Beck, mille neuf cent quatre-vingt-six. {fr_r.5}Mendras, mille neuf cent quatre-vingt-huit. "
        "{fr_r.6}Crenshaw, mille neuf cent quatre-vingt-neuf. {fr_r.7}Et Chauvel, deux mille un.",
        ("P", 4.0),
        "{-fr_r}{cf_r}{cf_r.1}Et trois chiffres à citer dans une copie. Vingt-trois pour cent de cadres en deux mille vingt-quatre, contre huit pour cent en mille neuf cent quatre-vingt-deux. "
        "{cf_r.2}Quatre-vingt-six virgule sept pour cent de salariés. {cf_r.3}Et un rapport interdécile des niveaux de vie de trois virgule quarante-huit.",
        ("P", 1.5),
        "{-cf_r}{fin}Les fiches à imprimer, le quiz, les cartes de révision et les animations de ce chapitre sont sur le site Faits et Courbes. "
        "Le lien est dans la description. Prochain dossier : l'École et la société.",
        ("P", 2.5),
        "{-fin}",
    ], vis={
        "cm_r": dict(type="plan", titre="L'espace social : structuré et hiérarchisé", x=60, y=140, w=1160, parties=[
            dict(t="Sept facteurs", items=["PCS, revenu, diplôme, ménage", "Âge, sexe, lieu de résidence : ils se cumulent"]),
            dict(t="Quatre évolutions", items=["Salarisation, tertiarisation", "Qualification, féminisation"]),
            dict(t="Marx et Weber", items=["Rapports de production, classe en soi / pour soi", "Trois ordres, stratification"]),
            dict(t="Le débat", items=["Moyennisation (Mendras) / classes sans conscience (Chauvel)", "Hétérogénéité, genre, individualisation (Beck)"])]),
        "fr_r": dict(type="frise", de=1840, a=2010, items=[
            dict(d=1848, nom="Marx, Engels", q="le Manifeste"), dict(d=1922, nom="Weber", q="trois ordres"),
            dict(d=1979, nom="Bourdieu", q="La Distinction"), dict(d=1986, nom="Beck", q="individualisation"),
            dict(d=1988, nom="Mendras", q="la toupie"), dict(d=1989, nom="Crenshaw", q="intersectionnalité"),
            dict(d=2001, nom="Chauvel", q="classes sans conscience")]),
        "cf_r": dict(type="chiffres", titre="Trois chiffres à citer", x=90, y=150, w=1100,
                     items=[dict(n=c["n"], l=c["l"], s=c["s"]) for c in CHIF]),
        "fin": dict(type="titre", sur="Faits & Courbes · SES Terminale", t="Fiches, quiz et animations",
                    sous="Le lien est dans la description · prochain dossier : l'École et la société"),
    }),
]

QUIZ = [
    dict(q="Lequel de ces facteurs n'est PAS cité par le programme parmi les facteurs de structuration de l'espace social ?",
         r=["la religion", "le lieu de résidence", "la composition du ménage"], ok=0,
         ex="Le programme cite : PCS, revenu, diplôme, composition du ménage, cycle de vie, sexe, lieu de résidence.", voir="li_fac"),
    dict(q="En 2024, le rapport interdécile D9/D1 des niveaux de vie est d'environ…",
         r=["1,5", "3,5", "10"], ok=1,
         ex="48 580 € ÷ 13 970 € ≈ 3,48 (Insee Première n° 2117).", voir="cf_niv"),
    dict(q="La nomenclature des PCS classe les personnes notamment selon…",
         r=["leur revenu uniquement", "leur conscience de classe", "leur profession, leur statut et leur qualification"], ok=2,
         ex="Profession, statut (salarié ou non), qualification, taille de l'entreprise, employeur public ou privé.", voir="def_pcs"),
    dict(q="Entre 1982 et 2024, la part des cadres dans l'emploi est passée de 8,0 % à 23,0 %. Elle a donc…",
         r=["augmenté de 15 points de pourcentage", "augmenté de 15 %", "doublé exactement"], ok=0,
         ex="On compare deux pourcentages : l'écart s'exprime en points. En taux de variation, c'est +187,5 %.", voir="s_c1"),
    dict(q="La tertiarisation de l'emploi s'explique notamment par…",
         r=["la baisse des revenus", "les gains de productivité dans l'agriculture et l'industrie et les nouveaux besoins de services",
            "la hausse du nombre d'agriculteurs"], ok=1,
         ex="Les gains de productivité libèrent de la main-d'œuvre ; la hausse des revenus crée une demande de services (déversement).", voir="ch_ter"),
    dict(q="Une « classe pour soi », chez Marx, est une classe…",
         r=["consciente de ses intérêts et mobilisée", "définie seulement par sa position objective", "créée par l'Insee"], ok=0,
         ex="La classe en soi a une position commune ; la classe pour soi y ajoute la conscience et la lutte.", voir="cols_soi"),
    dict(q="Chez Weber, les groupes de statut correspondent à…",
         r=["l'ordre économique : les revenus", "l'ordre social : le prestige et l'honneur", "l'ordre politique : le pouvoir"], ok=1,
         ex="Classes = ordre économique ; groupes de statut = ordre social ; partis = ordre politique.", voir="an_mw2"),
    dict(q="La thèse de la « moyennisation » est associée à…",
         r=["Louis Chauvel", "Karl Marx", "Henri Mendras"], ok=2,
         ex="Mendras (1988) : la société en forme de toupie, avec une large constellation centrale.", voir="ill_top"),
    dict(q="Louis Chauvel parle de « classes sans conscience » pour dire que…",
         r=["les écarts objectifs persistent mais la conscience de classe s'est affaiblie", "les classes ont disparu", "les inégalités ont fortement baissé"], ok=0,
         ex="C'est un argument pour le maintien des classes en soi, sans classes pour soi.", voir="au_chau"),
    dict(q="Quel argument va CONTRE la pertinence des classes sociales aujourd'hui ?",
         r=["le maintien d'inégalités de patrimoine élevées", "l'entre-soi de la grande bourgeoisie", "la multiplication des facteurs d'individualisation"], ok=2,
         ex="Les trajectoires et identités se diversifient (Beck), ce qui affaiblit le sentiment d'appartenance de classe.", voir="ch_ind"),
]

CREDITS = [
    "Données : Insee, enquête Emploi 2024 (séries longues sur le marché du travail ; Emploi, chômage, revenus du travail, édition 2025) ; "
    "Insee Première n° 2117, juillet 2026 (niveaux de vie 2024) ; Dares (syndicalisation, 2019).",
    "Graphiques, chaînes causales, animations et sujets : site Faits & Courbes (SES Terminale) ; les sujets sont inventés pour le site, "
    "sauf la partie 3 (bac 2026, jour 2), corrigée par le site.",
    "Polices : IBM Plex Sans Condensed, Archivo, Spectral, JetBrains Mono (SIL Open Font License).",
]
