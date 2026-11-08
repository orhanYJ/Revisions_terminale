"""Histoire · chapitre 2 « Les régimes totalitaires » — série vidéo, édition française, épisode 1 :
« Qu'est-ce que le totalitarisme ? » (l'introduction du chapitre : un débat et une définition, six idées,
schémas h2wheel, h2europe, h2reads).

Édition française de h2_1.py (cahier des charges : EDITION_FR.md ; l'anglais est gardé intact) : histoire-géographie
classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes visuels, mêmes repères,
mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 0 définition, trois régimes · 1 brutalisation · 2 Russie 1917 · 6 marche sur Rome · 13 deux crises (1929) ·
       16 les nazis premier parti · 19 Holodomor · 20 Hitler chancelier · 28 Rhénanie · 29 Axe, Espagne ·
       31 apaisement (l'Europe des régimes, 1937-1938) · 33 Anschluss · 34 Munich · 36 pacte germano-soviétique ·
       37 attaque de la Pologne
Adaptations : « Key term » → notion clé ; « key issue » → problématique ; Worksheet 2 → le dossier documentaire ;
essay → réponse à une question problématisée ; DBQ → analyse de document. Titres des œuvres de la bibliographie sous
leur titre français (L'Âge des extrêmes, De la Grande Guerre au totalitarisme, Les Origines du totalitarisme, Récits de
la Kolyma, La vie est belle, La Vague…). Citations d'Arendt et de Staline en traduction française fidèle (la première
traduite au plus près de la phrase citée par le cours). Hors du cours, comme dans l'anglais : nuance sur « l'échec »,
chute de l'URSS en 1991, phrases de présentation des œuvres. Erreur du cours corrigée : « MacDougal Littell ».
Chaîne : outils/serie-philo/generer.py h2f_1 ; sortie dans dnl/serie/ (h2f-1.*).
Plan de la série : 1 Qu'est-ce que le totalitarisme ? · 2 De la Grande Guerre au pouvoir · 3 Trois régimes, trois
idéologies · 4 Le chef, le parti et l'homme nouveau · 5 La terreur de masse · 6 Les ambitions hégémoniques ·
7 L'apaisement et la marche à la guerre · 8 Le totalitarisme à l'épreuve (composition et analyse de document) ·
9 Récapitulatif.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-1"
NOTION = "Les régimes totalitaires"
NUM = 1
TITRE = "Qu'est-ce que le totalitarisme ?"
SUIVANT = "Épisode 2 · De la Grande Guerre au pouvoir"
PRONONCIATION = {"Arendt": "A-rennte", "Hehn": "Hène", "Hindenburg": "Hinne-dène-bourg", "Weimar": "Vaï-mar",
                 "Holodomor": "Ho-lo-do-mor", "Anschluss": "Anne-chlouss", "URSS": "u-èr-èss-èss",
                 "McDougal": "Mac-Dou-gueul", "Littell": "Li-tèl", "Taylor": "Tè-leur", "Winter": "Ouinn-teur",
                 "Jay": "Djé", "Hobsbawm": "Hobz-bôme", "Eisner": "Aïz-neur", "Will": "Ouil",
                 "Cohen-Scali": "Coène-Scali", "Benigni": "Bé-ni-nyi", "Gansel": "Gann-zèl", "Dennis": "Dè-niss",
                 "George": "Djordj", "Hannah": "Ha-na", "Eric": "É-rik"}

# vote nazi (cours, I.2, graphiques du cours) : mai 1928, septembre 1930, juillet 1932, novembre 1932
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Mille neuf cent vingt-neuf. À New York, une foule silencieuse attend devant la Bourse. Le krach a commencé. "
        "La même année, à Nuremberg, Adolf Hitler salue ses partisans au congrès du parti nazi. Deux photographies. Une seule année.",
        "{-q1}{q2}Entre mille neuf cent dix-sept et mille neuf cent trente-neuf, trois régimes tentent ce qu'aucune tyrannie n'avait tenté. "
        "Contrôler non seulement l'État, mais toute la société. Et refaire l'être humain.",
        "{-q2}{q3}Alors, qu'est-ce que le totalitarisme, exactement ? Et a-t-il entraîné le monde dans la Seconde Guerre mondiale ? "
        "Ce sont les deux questions de ce chapitre.",
        "{-q3}{-g0}{plan}Cette série couvre tout le chapitre, en neuf épisodes. {plan.1}Aujourd'hui : qu'est-ce que le totalitarisme ? "
        "{plan.2}Puis, de la Grande Guerre au pouvoir. {plan.3}Trois régimes, trois idéologies. {plan.4}Le chef, le parti et l'homme nouveau. "
        "{plan.5}La terreur de masse. {plan.6}Les ambitions hégémoniques. {plan.7}L'apaisement, et la marche à la guerre. "
        "{plan.8}Ensuite, un épisode pour l'examen : la réponse à une question problématisée et l'analyse de document. {plan.9}Et un récapitulatif final.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[13]),
        "q1": dict(type="question", t="1929 : deux photographies, une seule année.", bande=True),
        "q2": dict(type="question", t="Contrôler toute la société… et refaire l'être humain ?", bande=True),
        "q3": dict(type="question", t="Qu'est-ce que le totalitarisme ? A-t-il mené à la guerre ?", bande=True),
        "plan": dict(type="liste", titre="Les régimes totalitaires, en neuf épisodes", petit=True, items=[
            "Qu'est-ce que le totalitarisme ? (introduction)", "De la Grande Guerre au pouvoir (I.1 – I.2)",
            "Trois régimes, trois idéologies (I.3)", "Le chef, le parti et l'homme nouveau (II.1 – II.2)",
            "La terreur de masse (II.3)", "Les ambitions hégémoniques (III.1)", "L'apaisement et la marche à la guerre (III.2 – III.3)",
            "Le totalitarisme à l'épreuve : composition et analyse de document", "Récapitulatif"], x=190, y=80, w=900),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 1", t="Qu'est-ce que le totalitarisme ?",
                      sous="1917 – 1939 · un débat · une définition · trois régimes"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="naissance", chap="1914 – 1933 sur la carte", fond="nuit", humeur="tension",
         retenir="1914-1918 : les tranchées, matrice des régimes · 1917 : les bolcheviks prennent le pouvoir · 1922 : l'URSS et la marche sur Rome · 1929 : deux crises · 30 janv. 1933 : Hitler chancelier.",
         beats=[
        "{g1}Avant toute définition, parcourons toute l'histoire sur la carte. Chaque épisode reviendra sur ces dates. "
        "{g1.1}Tout commence dans les tranchées de la Première Guerre mondiale. Quatre ans de massacres de masse ont banalisé la violence. "
        "Pour l'historien George Mosse, la Grande Guerre est la matrice du totalitarisme. On le verra dans l'épisode deux.",
        "{g1.2}Mille neuf cent dix-sept, en Russie. En février, la guerre fait tomber le tsar. En octobre, les bolcheviks de Lénine et de Trotski prennent le pouvoir. "
        "Puis ils gagnent une guerre civile. L'Union soviétique naît en mille neuf cent vingt-deux. Et à partir de mille neuf cent vingt-quatre, c'est l'Union soviétique de Staline.",
        "{g1.3}Mille neuf cent vingt-deux, en Italie. Le pays a gagné la guerre, mais il se sent floué. Et il a peur d'une révolution communiste. "
        "En octobre, les Chemises noires de Mussolini marchent sur Rome. Le roi le nomme chef du gouvernement. L'Italie fasciste durera jusqu'en mille neuf cent quarante-trois.",
        "{g1.4}Mille neuf cent vingt-neuf. Le krach de New York, et la crise mondiale du chapitre un. En Allemagne, le parti nazi n'est encore qu'un petit parti. "
        "Mais la crise va tout changer.",
        "{g1.5}Le trente janvier mille neuf cent trente-trois. Le président Hindenburg nomme Hitler chancelier. Légalement. "
        "L'Allemagne nazie est née. Elle durera jusqu'en mille neuf cent quarante-cinq.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 6, 13, 20]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="versguerre", chap="1933 – 1939 sur la carte", fond="nuit", humeur="tension",
         retenir="7 mars 1936 : la Rhénanie · oct. 1936 : l'axe Rome-Berlin · 12 mars 1938 : l'Anschluss · sept. 1938 : Munich · 23 août 1939 : le pacte germano-soviétique · 1er-3 sept. 1939 : la guerre.",
         beats=[
        "{g2}Et de là, la route mène à la guerre. {g2.1}Le sept mars mille neuf cent trente-six, les troupes allemandes entrent dans la Rhénanie démilitarisée. "
        "La France et le Royaume-Uni ne font rien. Le pari de Hitler est gagné.",
        "{g2.2}Octobre mille neuf cent trente-six : l'axe Rome-Berlin. Les deux dictateurs fascistes se méfient l'un de l'autre, et pourtant ils s'allient. "
        "Et tous deux soutiennent Franco dans la guerre d'Espagne.",
        "{g2.3}Mars mille neuf cent trente-huit : l'Anschluss. L'armée allemande entre dans Vienne, et l'Autriche est annexée. "
        "{g2.4}Septembre mille neuf cent trente-huit. À Munich, la France et le Royaume-Uni livrent les Sudètes à Hitler. Les Tchèques ne sont même pas invités. "
        "C'est l'apaisement. La deuxième notion clé du chapitre.",
        "{g2.5}Août mille neuf cent trente-neuf. Et voici le choc. L'Allemagne nazie et l'Union soviétique de Staline sont des ennemies idéologiques jurées. Et elles signent un pacte. "
        "{g2.6}Le premier septembre, l'Allemagne attaque la Pologne. Deux jours plus tard, la France et le Royaume-Uni lui déclarent la guerre.",
        "{-g2}{frise}Fixons les dates. {frise.1}Mille neuf cent dix-sept : les bolcheviks prennent le pouvoir. "
        "{frise.2}Mille neuf cent vingt-deux : la marche sur Rome. {frise.3}Mille neuf cent vingt-neuf : deux crises à la fois. "
        "{frise.4}Mille neuf cent trente-trois : Hitler devient chancelier. {frise.5}Mille neuf cent trente-six : la Rhénanie, et l'Axe. "
        "{frise.6}Mille neuf cent trente-huit : l'Anschluss, et Munich. {frise.7}Mille neuf cent trente-neuf : le pacte. Et la guerre.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[28, 29, 33, 34, 36, 37]),
        "frise": dict(type="frise", items=[
            dict(nom="Russie", d=1917, q="les bolcheviks prennent le pouvoir"), dict(nom="Italie", d=1922, q="la marche sur Rome"),
            dict(nom="Deux crises", d=1929, q="capitalisme · totalitarisme"), dict(nom="Allemagne", d=1933, q="Hitler chancelier"),
            dict(nom="Rhénanie", d=1936, q="et l'axe Rome-Berlin"), dict(nom="Munich", d=1938, q="l'Anschluss, les Sudètes"),
            dict(nom="La guerre", d=1939, q="le pacte, puis la Pologne")]),
    }),

    # ================================================================ III. deux crises (idée 1)
    dict(id="deuxcrises", chap="1929 : deux crises à la fois", fond="nuit", humeur="mystere",
         retenir="1929 ouvre deux crises : la crise du capitalisme (chapitre 1) et la menace totalitaire (chapitre 2). Laquelle a mené à la guerre : l'une, l'autre, ou les deux ?",
         beats=[
        "{photos}Passons au cours. Le chapitre s'ouvre sur ces deux photographies de mille neuf cent vingt-neuf. "
        "{photos.1}Sur l'une, une foule grave se tient devant la Bourse de New York, après le krach. Sur l'autre, Adolf Hitler salue ses partisans "
        "au quatrième congrès du parti nazi, à Nuremberg.",
        "{-photos}{deux}{deux.g}Pourquoi les mettre côte à côte ? Parce que mille neuf cent vingt-neuf ouvre deux crises à la fois. "
        "La première, c'est la crise du capitalisme. Le krach, la dépression, le recul de la démocratie. C'était le chapitre un. "
        "{deux.d}La seconde, c'est la menace totalitaire. C'est ce chapitre. Et les deux routes mènent au même endroit : la Seconde Guerre mondiale.",
        "{-deux}{etou}Entre les deux images, le cours n'écrit que trois mots. {!et ou}Et, ou ? "
        "Une seule crise a-t-elle causé la guerre ? Ou les deux ont-elles agi ensemble ? Garde cette question en tête. C'est le fil de tout le chapitre.",
        "{-etou}{gr}L'Allemagne montre comment les deux routes se rejoignent. {gr.1}Mai mille neuf cent vingt-huit, avant la crise. Le parti nazi obtient deux virgule six pour cent des voix. "
        "C'est un parti marginal. {gr.2}Septembre mille neuf cent trente : dix-huit virgule trois pour cent. "
        "{gr.3}Juillet mille neuf cent trente-deux : trente-sept virgule quatre pour cent. C'est désormais le premier parti d'Allemagne. Et l'Allemagne compte cinq virgule six millions de chômeurs. "
        "{gr.4}En novembre, les nazis retombent à trente-trois virgule un. Donc jamais la majorité. Retiens-le : ce sera important avec Arendt.",
        "{-gr}La crise mondiale des années trente est donc double. {crise}{crise.1}C'est une crise de la démocratie, qui recule. "
        "{crise.2}Et c'est la progression continue du totalitarisme.",
    ], vis={
        "photos": dict(type="note", terme="Deux photographies, 1929", cles=["krach", "Nuremberg"],
                       t="Une foule grave devant la Bourse de New York après le krach ; Hitler au congrès du parti nazi à Nuremberg.",
                       etape="La même année : la crise du capitalisme et la menace totalitaire (décrites ici, non montrées).", x=170, y=200, w=940),
        "deux": dict(type="cols", g="La crise du capitalisme", gq="le krach, la dépression, le recul de la démocratie · chapitre 1",
                     d="La menace totalitaire", dq="fascisme, nazisme, stalinisme · chapitre 2", vs="&",
                     repere="Les deux routes partent de 1929 et mènent à la Seconde Guerre mondiale"),
        "etou": dict(type="mot", t="et / ou ?", g="une seule crise a-t-elle causé la guerre, ou les deux ensemble ?", y=250, taille=120),
        "gr": dict(type="graphe", titre="Le vote nazi aux élections au Reichstag (%, cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.8, 1933.2], y=[0, 45], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40], lx="année", ly="% des voix"),
                   el=[dict(type="point", x=1928.4, y=2.6, c="sa", lbl="mai 1928 : 2,6 %", lp=[1928.5, 9]),
                       dict(type="courbe", pts=VOTE[:2], c="ca", lbl="sept. 1930 : 18,3 %", lp=[1929.2, 22], dur=1.6),
                       dict(type="courbe", pts=VOTE[1:3], c="ca", lbl="juillet 1932 : 37,4 %", lp=[1930.6, 41], dur=1.4),
                       dict(type="courbe", pts=VOTE[2:], c="el", lbl="nov. 1932 : 33,1 %", lp=[1931.6, 27], dur=1.0)]),
        "crise": dict(type="liste", titre="La crise mondiale des années 1930", items=[
            "Une crise de la démocratie, qui recule", "La progression continue du totalitarisme"], x=170, y=200, w=940),
    }),

    # ================================================================ IV. le débat des historiens (idée 2)
    dict(id="historiens", chap="Les historiens ne sont pas d'accord", fond="nuit", humeur="calme",
         retenir="Causes profondes de la guerre : Taylor (1961), l'échec des démocraties, « thèse très controversée » · Hehn, un conflit économique · Winter, une « guerre de Trente Ans » 1914-1945 · ce chapitre : l'idéologie totalitaire.",
         beats=[
        "{q4}Tout le thème un a pour but d'évaluer les causes profondes de la Seconde Guerre mondiale. "
        "Et là, les historiens ne sont pas d'accord. Le cours en met trois côte à côte.",
        "{-q4}{g3}{hist}{g3.1}{hist.1}Le premier, c'est A. J. P. Taylor, un historien britannique, qui a vécu de mille neuf cent six à mille neuf cent quatre-vingt-dix. "
        "Son livre, Les Origines de la Seconde Guerre mondiale, paraît en mille neuf cent soixante et un. Il accuse les démocraties de n'avoir pas arrêté Hitler. "
        "Pense à l'apaisement, à Munich. Hitler est allé plus loin parce que personne ne l'a arrêté.",
        "{g3.2}{hist.2}Le deuxième, c'est Paul N. Hehn, de mille neuf cent vingt-sept à deux mille quatorze. Pour lui, la guerre est un conflit économique. "
        "Elle naît du krach : des marchés qui se ferment, et une course aux ressources.",
        "{g3.3}{hist.3}Le troisième, c'est Jay Winter, né en mille neuf cent quarante-cinq. Il voit dans les années mille neuf cent quatorze à mille neuf cent quarante-cinq une seule "
        "{!guerre de Trente Ans}guerre de Trente Ans. Le second conflit prolonge simplement le premier.",
        "{-hist}{-g3}{taylor}Maintenant, regarde l'avertissement de la bibliographie. Le livre de Taylor y figure, avec trois mots à côté. {!thèse très controversée}Thèse très controversée. "
        "{taylor.1}Pourquoi ? Parce que si les démocraties sont coupables, la volonté de guerre de Hitler lui-même disparaît presque. "
        "Cite Taylor, mais discute-le.",
        "{-taylor}{quatre}Et ce chapitre ajoute un quatrième candidat à la liste. {!l'idéologie totalitaire}L'idéologie totalitaire. "
        "Les idéologies de ces régimes ont-elles rendu la guerre inévitable ? C'est la question de la troisième partie. Et c'est la problématique du chapitre.",
    ], vis={
        "q4": dict(type="question", t="Quelles sont les causes profondes de la Seconde Guerre mondiale ?"),
        "g3": dict(type="globe", code="H2", sc=[31, 13, 1]),
        "hist": dict(type="liste", titre="Trois historiens, trois réponses", x=60, y=110, w=620, petit=True, bande=True,
                     cles=["démocraties", "économique", "Trente"], items=[
            "A. J. P. Taylor (1906-1990) : l'échec des démocraties à arrêter Hitler",
            "Paul N. Hehn (1927-2014) : un conflit économique, né du krach",
            "Jay Winter (né en 1945) : 1914-1945, une seule « guerre de Trente Ans »"]),
        "taylor": dict(type="note", terme="Dans la bibliographie du cours", cles=["controversée"],
                       t="A. J. P. Taylor, Les Origines de la Seconde Guerre mondiale (1961) : « thèse très controversée ».",
                       etape="Accuser les démocraties… et la volonté de guerre de Hitler disparaît presque.", x=170, y=200, w=940),
        "quatre": dict(type="mot", t="+ l'idéologie totalitaire ?", g="le quatrième candidat, mis à l'épreuve dans ce chapitre", y=250, taille=88),
    }),

    # ================================================================ V. la définition (idée 3)
    dict(id="definition", chap="Une définition en trois parties", fond="aube", humeur="lumiere",
         retenir="Notion clé. Le totalitarisme : un régime qui cherche à contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie.",
         beats=[
        "{def1}Voici la première notion clé du chapitre. Tu dois la connaître mot pour mot. Le totalitarisme : "
        "un régime qui cherche à contrôler totalement la société, par la contrainte, afin de transformer l'homme selon une idéologie.",
        "{-def1}{trois}La définition a trois parties. {trois.1}Un. Le contrôle est {!total}total. Il ne s'arrête pas à la politique. "
        "Il atteint le travail, les loisirs, la famille, l'école, la religion. Et même la pensée.",
        "{trois.2}Deux. Il repose sur la {!contrainte}contrainte. Et la contrainte, ce sont deux choses à la fois : la terreur et la propagande. "
        "La peur, et la persuasion.",
        "{trois.3}Trois, le plus important. Le but n'est pas l'obéissance. C'est la {!transformation}transformation. "
        "Le régime veut créer un homme nouveau, façonné par son idéologie.",
        "{-trois}{photo3}{dict}{dict.g}C'est cette troisième partie qui distingue un régime totalitaire d'une dictature ordinaire. "
        "Une dictature ordinaire se contente que les gens se taisent. {dict.d}Un régime totalitaire veut qu'ils croient. "
        "Qu'ils acclament. Qu'ils changent. Le silence ne suffit pas. Il veut ton âme.{-photo3}",
    ], vis={
        "def1": dict(type="def", cles=["totalement", "contrainte", "transformer", "idéologie"], terme="Notion clé · Le totalitarisme",
                     t="Un régime qui cherche à contrôler totalement la société, par la contrainte, afin de transformer l'homme selon une idéologie.",
                     etape="À savoir mot pour mot : elle ouvre presque toute composition sur ce chapitre.", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="La définition, partie par partie", cles=["total", "Contrainte", "Transformation"], items=[
            "Un contrôle total : travail, loisirs, famille, école, religion, pensée",
            "Contrainte : la terreur et la propagande ensemble",
            "Transformation : non pas l'obéissance, mais un « homme nouveau » façonné par l'idéologie"], x=170, y=140, w=940),
        "photo3": dict(type="tableau", img="h2-nuremberg-1936", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="La « cathédrale de lumière » au-dessus du Zeppelinfeld, congrès de Nuremberg, septembre 1936 · Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE"),
        "dict": dict(type="cols", g="Une dictature ordinaire", gq="se contente que les gens se taisent",
                     d="Un régime totalitaire", dq="veut qu'ils croient, acclament et changent : un « homme nouveau »", vs="≠"),
    }),

    # ================================================================ VI. la roue des sept traits (h2wheel)
    dict(id="roue", chap="Les sept traits clés", fond="nuit", humeur="calme",
         retenir="Sept traits : une idéologie · un chef charismatique · dictature et parti unique · contrôle des individus par l'État · contrôle de la société par l'État · moyens de coercition · technologie moderne.",
         beats=[
        "{src}Le cours montre une roue. Elle donne les traits clés du totalitarisme. Elle vient d'un manuel américain, "
        "World History, publié par McDougal Littell en deux mille neuf. Il y a sept traits. "
        "{-src}{roue}{roue.1}Un : une idéologie. Elle fixe les buts de l'État, les glorifie, et justifie tout ce que fait le gouvernement. "
        "{roue.2}Deux : un chef charismatique. Il unit le peuple, incarne le gouvernement, et soulève l'adhésion populaire.",
        "{roue.3}Trois : la dictature et le parti unique. L'autorité est absolue, et le parti domine le gouvernement. "
        "{roue.4}Quatre : le contrôle des individus par l'État. Le régime exige la loyauté. Il nie les libertés fondamentales. Et il attend de chacun qu'il se sacrifie pour l'État.",
        "{roue.5}Cinq : le contrôle de la société par l'État. L'économie, le travail et le logement. L'éducation, la religion et les arts. Même la vie privée, et les mouvements de jeunesse. "
        "{roue.6}Six : les moyens de coercition. La terreur policière, l'endoctrinement, la censure, la persécution.",
        "{roue.7}Et sept : la technologie moderne. Les moyens de communication de masse, pour diffuser la propagande. Et des armes perfectionnées.",
        "{-roue}Sept, c'est beaucoup. Alors voici un moyen de les retenir. {memo}{memo.1}L'idéologie fixe le but. "
        "{memo.2}Le chef et le parti l'incarnent. {memo.3}Le contrôle et la coercition l'imposent. {memo.4}Et la technologie moderne le diffuse.",
        "{-memo}{techno}Regarde bien ce dernier trait. C'est lui qui sépare le totalitarisme des tyrannies du passé. "
        "{techno.1}Un tyran antique pouvait terroriser une cité. Mais un régime du vingtième siècle a la radio, le cinéma et les armes modernes. "
        "Il peut atteindre chaque foyer, chaque jour.",
    ], vis={
        "roue": dict(type="liste", titre="Les sept traits clés du totalitarisme (d'après McDougal Littell, 2009)", petit=True,
                     cles=["idéologie", "chef", "parti unique", "individus", "société", "coercition", "technologie"], items=[
            "Une idéologie : fixe, glorifie et justifie les buts de l'État",
            "Un chef charismatique : unit le peuple, incarne le gouvernement",
            "Dictature et parti unique : une autorité absolue",
            "Contrôle des individus par l'État : loyauté, pas de libertés, sacrifice",
            "Contrôle de la société par l'État : économie, école, religion, arts, jeunesse",
            "Moyens de coercition : terreur policière, endoctrinement, censure, persécution",
            "Technologie moderne : communication de masse, armes perfectionnées"], x=150, y=90, w=980),
        "src": dict(type="note", terme="Le cours · les traits clés du totalitarisme", cles=["roue", "sept"],
                    t="Une roue de sept traits, tirée de World History (McDougal Littell, 2009), un manuel américain.",
                    etape="Le cours écrit « MacDougal Littell » : l'éditeur s'appelle McDougal Littell.", x=170, y=200, w=940),
        "memo": dict(type="liste", titre="Pour retenir", cles=["fixe", "incarnent", "imposent", "diffuse"], items=[
            "L'idéologie fixe le but", "Le chef et le parti l'incarnent",
            "Le contrôle et la coercition l'imposent", "La technologie moderne le diffuse"], x=170, y=150, w=940),
        "techno": dict(type="note", terme="Le trait décisif", cles=["radio", "cinéma", "armes"],
                       t="La technologie moderne sépare le totalitarisme des tyrannies anciennes : la radio, le cinéma, les armes modernes.",
                       etape="Le régime atteint chaque foyer, chaque jour.", x=170, y=200, w=940),
    }),

    # ================================================================ VII. l'idéologie (idée 4)
    dict(id="ideologie", chap="L'idéologie : un but suprême", fond="nuit", humeur="tension",
         retenir="Idéologie : un ensemble de croyances qui fixe un but suprême. URSS : une société sans classes · Italie fasciste : la nation et l'État · Allemagne nazie : la pureté et la domination de la race. Un but suprême justifie tous les moyens.",
         beats=[
        "{def2}Le premier trait de la roue est la clé de tout le chapitre. Qu'est-ce qu'une {!idéologie}idéologie ? Un ensemble de croyances qui fixe un but suprême à atteindre.",
        "{-def2}{g4}{buts}Et chaque régime a son propre but suprême. {buts.1}Pour l'Union soviétique, une société sans classes. "
        "{buts.2}Pour l'Italie fasciste, la grandeur de la nation et de l'État. "
        "{buts.3}Pour l'Allemagne nazie, la pureté et la domination de la race. La classe, la nation, la race. Retiens ces trois mots. "
        "Ils reviennent dans chaque épisode.",
        "{-buts}{-g4}{moyens}Pourquoi est-ce si important ? Parce qu'un but {!suprême}suprême justifie tous les moyens. "
        "{moyens.1}Même la souffrance de millions de personnes.",
        "{-moyens}{photo1}{g5}Le cours en donne un exemple glaçant. Un discours de Staline, le sept janvier mille neuf cent trente-trois, dans le dossier documentaire. "
        "Staline y présente son plan quinquennal comme le chemin vers{-g5}",
        ("C", "l'abolition des classes en URSS", "c_staline"),
        "{-c_staline}{-photo1}{g5b}{g5b.1}Et dans ces mêmes mois, l'Ukraine meurt de faim. C'est la famine de mille neuf cent trente-deux et trente-trois, l'Holodomor. "
        "Elle tue les paysans dont le régime prend le grain. D'un côté, le but suprême. De l'autre, des millions de victimes. "
        "On y revient dans l'épisode trois.",
        "{-g5b}{dedans}L'idéologie explique donc deux choses. {dedans.1}Ce que ces régimes font à l'intérieur de leurs frontières : ce sont les parties un et deux. "
        "{dedans.2}Et pourquoi ils vont chercher la guerre au-dehors : c'est la troisième partie.",
    ], vis={
        "def2": dict(type="def", cles=["croyances", "suprême"], terme="L'idéologie",
                     t="Un ensemble de croyances qui fixe un but suprême à atteindre.",
                     etape="Le premier trait de la roue, et la clé du chapitre", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H2", sc=[0]),
        "buts": dict(type="liste", titre="Trois buts suprêmes", x=60, y=120, w=620, petit=True, bande=True,
                     cles=["sans classes", "nation", "race"], items=[
            "URSS : une société sans classes", "Italie fasciste : la grandeur de la nation et de l'État",
            "Allemagne nazie : la pureté et la domination de la race"]),
        "moyens": dict(type="note", terme="Pourquoi l'idéologie compte", cles=["suprême", "tous"],
                       t="Un but présenté comme suprême justifie tous les moyens, même la souffrance de millions de personnes.",
                       x=170, y=200, w=940),
        "photo1": dict(type="tableau", img="h2-fyp-poster", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.1, .5, .45],
                       legende="« L'arithmétique d'un contre-plan : 2 + 2 plus l'enthousiasme des travailleurs = 5 », affiche du plan quinquennal, 1931 · Yakov Guminer, domaine public"),
        "g5": dict(type="note", terme="Dossier documentaire · document 1", cles=["quinquennal"],
                   t="Le discours de Staline du 7 janvier 1933 sur les résultats du premier plan quinquennal.", x=170, y=480, w=940),
        "c_staline": dict(type="cit", a="Joseph Staline", o="discours du 7 janvier 1933 (dossier documentaire, traduction)", x=200, y=190, w=880),
        "g5b": dict(type="globe", code="H2", sc=[19]),
        "dedans": dict(type="cols", g="À l'intérieur des frontières", gq="contrôle, homme nouveau, terreur · parties I et II",
                       d="Au-dehors", dq="l'expansion et la marche à la guerre · partie III", vs="→"),
    }),

    # ================================================================ VIII. Arendt (idée 5)
    dict(id="arendt", chap="Arendt : la confiance des masses", fond="guerre", humeur="mystere",
         retenir="Arendt, Les Origines du totalitarisme (1951) : l'arrivée de Hitler au pouvoir « fut légale au regard de la règle majoritaire » ; les deux dictateurs avaient besoin de « la confiance des masses ». Expliquer l'adhésion autant que la terreur.",
         beats=[
        "{photo2}{ar}Attention maintenant à une vision en noir et blanc. L'avertissement vient de Hannah Arendt, qui a vécu de mille neuf cent six à mille neuf cent soixante-quinze. "
        "Cette philosophe politique germano-américaine écrit, dans Les Origines du totalitarisme, paru en mille neuf cent cinquante et un, que{-ar}",
        ("C", "l'arrivée de Hitler au pouvoir fut légale au regard de la règle majoritaire", "c_ar1"),
        "{-c_ar1}{ar2}Elle ajoute que ni Hitler ni Staline n'auraient pu garder le pouvoir, à travers tant de crises, sans{-ar2}",
        ("C", "la confiance des masses", "c_ar2"),
        "{-c_ar2}{sens}Que veut-elle dire ? {sens.1}Que de larges masses faisaient confiance à ces régimes. {sens.2}Que tout le monde ne se sentait pas opprimé. "
        "{sens.3}Donc, pour comprendre le totalitarisme, il faut expliquer l'adhésion. Pas seulement la terreur.",
        "{-sens}{-photo2}{g6}{g6.1}L'Allemagne en est le meilleur exemple. Souviens-toi de la courbe. Trente-sept virgule quatre pour cent, en juillet mille neuf cent trente-deux. "
        "Des millions d'Allemands ont voté librement pour Hitler. {g6.2}Puis, le trente janvier mille neuf cent trente-trois, le président Hindenburg l'a nommé chancelier. "
        "Tout s'est fait par les institutions.",
        "{-g6}{nuance}Mais sois précis dans une copie. {nuance.1}Était-ce légal ? Oui. Hitler a été nommé. Il n'a pas pris le pouvoir par un coup d'État. "
        "{nuance.2}Mais les nazis ont-ils jamais obtenu la majorité à une élection libre ? Non. Leur meilleur score : trente-sept virgule quatre pour cent. "
        "Écris donc ceci : une nomination légale, avec un soutien de masse, mais sans majorité.",
        "{-nuance}{deuxfaces}{deuxfaces.g}Garde ensemble les deux visages de ces régimes. La terreur, pour les ennemis. "
        "{deuxfaces.d}Et le consentement, l'enthousiasme et la confiance, pour des millions d'autres.",
        "{-deuxfaces}{faits}Arendt ajoute une dernière idée. C'est l'épigraphe placée en tête du chapitre. {faits.1}La propagande totalitaire "
        "traite les faits comme une chose que le pouvoir peut fabriquer. Elle méprise les faits. Ce que dit le chef devient vrai.",
    ], vis={
        "photo2": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, autrice des Origines du totalitarisme (1951), en 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
        "ar": dict(type="note", terme="Hannah Arendt (1906-1975)", cles=["Origines"],
                   t="Philosophe politique germano-américaine, autrice des Origines du totalitarisme (1951).", x=170, y=200, w=940),
        "c_ar1": dict(type="cit", a="Hannah Arendt", o="Les Origines du totalitarisme, 1951 (traduction)", x=200, y=190, w=880),
        "ar2": dict(type="note", terme="Ni Hitler ni Staline…", t="…n'auraient pu garder le pouvoir à travers tant de crises sans…",
                    x=170, y=200, w=940),
        "c_ar2": dict(type="cit", a="Hannah Arendt", o="Les Origines du totalitarisme, 1951 (traduction)", x=200, y=220, w=880),
        "sens": dict(type="liste", titre="L'avertissement d'Arendt", cles=["confiance", "opprimé", "adhésion"], items=[
            "De larges masses faisaient confiance à ces régimes", "Tout le monde ne se sentait pas opprimé",
            "Expliquer l'adhésion autant que la terreur"], x=170, y=150, w=940),
        "g6": dict(type="globe", code="H2", sc=[16, 20]),
        "nuance": dict(type="liste", titre="Sois précis", cles=["Légal", "majorité"], items=[
            "Légal : nommé par Hindenburg le 30 janvier 1933, pas de coup d'État",
            "Mais jamais la majorité : 37,4 % au mieux (juillet 1932)"], x=170, y=150, w=940),
        "deuxfaces": dict(type="cols", g="La terreur", gq="pour les ennemis du régime", d="La confiance",
                          dq="le consentement et l'enthousiasme de millions de personnes", vs="+", repere="Arendt : expliquer l'adhésion autant que la terreur"),
        "faits": dict(type="def", cles=["faits", "fabriquer"], terme="La propagande, selon Arendt",
                      t="La diffusion organisée d'idées et d'images pour gagner ou contrôler l'opinion, marquée par le mépris des faits.",
                      etape="L'épigraphe du chapitre : les faits deviennent une chose que le pouvoir peut fabriquer.", x=170, y=200, w=940),
    }),

    # ================================================================ IX. trois régimes, une trajectoire (idée 6)
    dict(id="trajectoire", chap="Trois régimes, une trajectoire", fond="nuit", humeur="tension",
         retenir="URSS de Staline (1924-1953), Italie fasciste (1922-1943), Allemagne nazie (1933-1945) : nés du renversement d'un cadre démocratique, ils ont ouvert la voie à la guerre et ont tous fini par échouer.",
         beats=[
        "{fr2}{fr2.1}Le chapitre étudie donc trois régimes côte à côte. Le cours date chacun d'eux, sous son drapeau. "
        "D'abord l'Italie fasciste, sous l'aigle fasciste, de mille neuf cent vingt-deux à mille neuf cent quarante-trois. "
        "{fr2.2}Puis l'Union soviétique de Staline, sous la faucille et le marteau, à partir de mille neuf cent vingt-quatre. "
        "{fr2.3}Puis l'Allemagne nazie, sous la croix gammée, à partir de mille neuf cent trente-trois. "
        "{fr2.4}L'Italie fasciste tombe en mille neuf cent quarante-trois. {fr2.5}L'Allemagne nazie, en mille neuf cent quarante-cinq. "
        "{fr2.6}Et l'Union soviétique de Staline dure jusqu'à sa mort, en mille neuf cent cinquante-trois.",
        "{-fr2}Ils partagent la même ambition totalitaire. Mais leurs idéologies s'opposent. {meme}{meme.1}La nation, pour le fascisme. "
        "{meme.2}La race, pour le nazisme. {meme.3}La classe, pour le stalinisme. Voilà pourquoi Staline et Hitler sont des ennemis jurés. Du moins jusqu'à leur pacte, en mille neuf cent trente-neuf.",
        "{-meme}{g7}Et pourtant, ils suivent un même chemin, en trois étapes. {traj}{traj.1}Première étape : chacun naît du renversement d'un cadre démocratique. "
        "En Allemagne, la république de Weimar. En Italie, la monarchie parlementaire. En Russie, les fragiles libertés nées en février mille neuf cent dix-sept, "
        "que les bolcheviks balaient. {traj.2}Deuxième étape : tous trois ouvrent la voie à la Seconde Guerre mondiale. "
        "{traj.3}Troisième étape : tous trois finissent par échouer.",
        "{-traj}{-g7}{nu}Une nuance sur cette dernière étape. {nu.1}Pour l'Italie et l'Allemagne, l'échec, c'est la défaite totale dans la guerre. "
        "{nu.2}L'Union soviétique, au contraire, est parmi les vainqueurs de mille neuf cent quarante-cinq. Le stalinisme s'achève avec la mort de Staline, en mille neuf cent cinquante-trois. "
        "Et l'Union soviétique elle-même s'effondre en mille neuf cent quatre-vingt-onze. Cette dernière date est hors du cours. Mais elle t'aide à discuter le mot échec.",
        "{-nu}{g8}Une dernière carte du cours. L'Europe et ses régimes, vers mille neuf cent trente-huit. {g8.1}À l'ouest, les démocraties. "
        "Le Royaume-Uni, la France, et quelques petits pays. Au centre, les deux régimes fascistes, l'Allemagne et l'Italie. À l'est, l'Union soviétique communiste. "
        "Et presque partout ailleurs, d'autres régimes autoritaires, comme la Pologne, l'Autriche ou l'Espagne. {g8.2}À la fin des années trente, "
        "les démocraties forment un îlot, à l'ouest du continent.",
    ], vis={
        "fr2": dict(type="frise", items=[
            dict(nom="Italie fasciste", d=1922, q="la marche sur Rome"), dict(nom="L'URSS de Staline", d=1924, q="Staline au pouvoir"),
            dict(nom="Allemagne nazie", d=1933, q="Hitler chancelier"), dict(nom="Chute de l'Italie", d=1943, q="fin de l'Italie fasciste"),
            dict(nom="Chute de l'Allemagne", d=1945, q="fin de l'Allemagne nazie"), dict(nom="Mort de Staline", d=1953, q="fin de l'URSS stalinienne")]),
        "meme": dict(type="liste", titre="Une ambition, trois idéologies", cles=["nation", "race", "classe"], items=[
            "Fascisme → la nation", "Nazisme → la race", "Stalinisme → la classe"], x=170, y=150, w=940),
        "g7": dict(type="globe", code="H2", sc=[0]),
        "traj": dict(type="liste", titre="Une trajectoire, trois étapes", x=60, y=120, w=620, petit=True, bande=True,
                     cles=["renversement", "guerre", "échouer"], items=[
            "Nés du renversement d'un cadre démocratique", "Tous ont ouvert la voie à la Seconde Guerre mondiale",
            "Tous ont fini par échouer"]),
        "nu": dict(type="cols", g="L'Italie, l'Allemagne", gq="échec = défaite totale dans la guerre (1943, 1945)",
                   d="L'URSS", dq="vainqueur en 1945 ; Staline meurt en 1953 ; l'URSS s'effondre en 1991 (hors du cours)", vs="≠"),
        "g8": dict(type="globe", code="H2", sc=[31]),
    }),

    # ================================================================ X. lire et voir (h2reads)
    dict(id="lectures", chap="Lire et voir", fond="aube", humeur="calme",
         retenir="Cite une œuvre de la bibliographie du cours, avec une phrase sur ce qu'elle montre : par exemple Arendt (1951), les Récits de la Kolyma de Chalamov, La vie est belle, La Vague.",
         beats=[
        "{lire}{lire.1}Le cours donne aussi une bibliographie. Les présentations d'une ligne viennent du site, pas du cours. "
        "D'abord, Eric Hobsbawm, L'Âge des extrêmes, de mille neuf cent quatre-vingt-quatorze. Il raconte le court vingtième siècle, de mille neuf cent quatorze à mille neuf cent quatre-vingt-onze, comme un âge de catastrophes. "
        "{lire.2}George Mosse, De la Grande Guerre au totalitarisme. La brutalisation, et la mémoire des guerres mondiales. "
        "{lire.3}Hannah Arendt, Les Origines du totalitarisme. La théorie, et l'épigraphe du chapitre. "
        "{lire.4}A. J. P. Taylor, Les Origines de la Seconde Guerre mondiale. La thèse très controversée.",
        "{lire.5}La bande dessinée de Will Eisner, Le Complot. L'histoire d'un faux, les Protocoles des Sages de Sion. La propagande, et l'antisémitisme. "
        "{lire.6}Les Récits de la Kolyma, de Varlam Chalamov. Le Goulag, vu de l'intérieur. "
        "{lire.7}Et Max, de Sarah Cohen-Scali. Un garçon né dans l'Allemagne nazie, pour les jeunes lecteurs.",
        "{-lire}{voir}Et quatre films. {voir.1}La vie est belle, de Roberto Benigni. Les Juifs italiens, sous les lois raciales, et la déportation. "
        "{voir.2}La Vague, de Dennis Gansel. Avec quelle facilité un groupe glisse vers une discipline autoritaire. "
        "{voir.3}Le documentaire de Daniel Costelle, Apocalypse, Hitler. Son ascension vers le pouvoir. "
        "{voir.4}Et Amarcord, de Federico Fellini. La vie de province dans l'Italie fasciste, vue à travers le souvenir.",
        "{-voir}{astuce}Un conseil pour l'examen. Cite l'une de ces œuvres, avec une phrase sur ce qu'elle montre. "
        "Cela prouve que tu as lu au-delà du cours.",
    ], vis={
        "lire": dict(type="liste", titre="Lire · la bibliographie du cours", petit=True, items=[
            "Hobsbawm, L'Âge des extrêmes (1994) : un âge de catastrophes", "Mosse, De la Grande Guerre au totalitarisme : la brutalisation",
            "Arendt, Les Origines du totalitarisme (1951) : la théorie", "Taylor, Les Origines de la Seconde Guerre mondiale (1961) : « très controversée »",
            "Eisner, Le Complot (2005) : les faux Protocoles, l'antisémitisme", "Chalamov, Récits de la Kolyma (1954) : le Goulag de l'intérieur",
            "Cohen-Scali, Max (2012) : un garçon né dans l'Allemagne nazie"], x=150, y=90, w=980),
        "voir": dict(type="liste", titre="Voir · la filmographie du cours", items=[
            "Benigni, La vie est belle (1997) : les Juifs italiens, les lois raciales", "Gansel, La Vague (2008) : glisser vers une discipline autoritaire",
            "Costelle, Apocalypse, Hitler (2011) : l'ascension vers le pouvoir", "Fellini, Amarcord (1973) : la province de l'Italie fasciste"],
                     x=150, y=140, w=980),
        "astuce": dict(type="note", terme="Conseil pour l'examen", cles=["phrase", "au-delà"],
                       t="Cite une œuvre, avec une phrase sur ce qu'elle montre : la preuve d'une lecture au-delà du cours.", x=170, y=200, w=940),
    }),

    # ================================================================ XI. à toi : définir (pause)
    dict(id="atoi", chap="À toi : définir le totalitarisme", fond="aube", humeur="calme",
         retenir="Un paragraphe de définition : la notion clé mot pour mot · ses trois parties · la différence avec une dictature · un exemple précis · la nuance d'Arendt.",
         beats=[
        "{pa1}À toi. Rédige un paragraphe qui définit le totalitarisme, avec un exemple précis. "
        "Utilise les trois parties de la définition. Et montre ce qui le distingue d'une dictature ordinaire.",
        ("P", 2.0),
        "{-pa1}{rep1}On peut le rédiger ainsi. {rep1.1}Le totalitarisme est un régime qui cherche à contrôler totalement la société, "
        "par la contrainte, afin de transformer l'homme selon une idéologie. "
        "{rep1.2}Son contrôle est total, puisqu'il atteint le travail, les loisirs, l'école, la religion, et même la pensée. "
        "Et sa contrainte associe la terreur à la propagande. "
        "{rep1.3}Une dictature ordinaire se contente de l'obéissance. Un régime totalitaire veut créer un homme nouveau. "
        "{rep1.4}Par exemple, en janvier mille neuf cent trente-trois, Staline présente le plan quinquennal comme le chemin vers l'abolition des classes. "
        "Au même moment, la famine tue les paysans d'Ukraine. Un but suprême justifie tous les moyens. "
        "{rep1.5}Pourtant, comme le rappelle Hannah Arendt, ces régimes ne reposent pas sur la seule terreur. Ils reposent aussi sur la confiance des masses.",
        "{-rep1}{ki}À quoi te servira cette définition ? À la problématique du chapitre. {!Quel rôle le totalitarisme}"
        "Quel rôle le totalitarisme a-t-il joué dans l'effondrement de la paix mondiale, à la fin des années trente ? "
        "{ki.1}Et aux deux notions clés : le totalitarisme, et l'apaisement. "
        "La définition que tu viens d'écrire, c'est la première étape de ton introduction.",
    ], vis={
        "pa1": dict(type="pause", t="Définis le totalitarisme en un paragraphe, avec un exemple précis.",
                    sous="Trois parties, la différence avec une dictature, un exemple. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "rep1": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "Définition : contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie",
            "Total (travail, loisirs, école, religion, pensée) ; contrainte = terreur + propagande",
            "Pas la simple obéissance d'une dictature : un « homme nouveau »",
            "Exemple : Staline, 7 janv. 1933, « l'abolition des classes », pendant la famine en Ukraine",
            "Nuance : Arendt, « la confiance des masses »"], x=150, y=110, w=980),
        "ki": dict(type="def", cles=["rôle", "effondrement"], terme="La problématique du chapitre",
                   t="Quel rôle le totalitarisme a-t-il joué dans l'effondrement de la paix mondiale à la fin des années 1930 ?",
                   etape="Notions clés : le totalitarisme · l'apaisement", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Mille neuf cent vingt-neuf ouvre deux crises à la fois : le capitalisme, et le totalitarisme. "
        "Les historiens débattent des causes de la guerre : Taylor, Hehn, Winter. "
        "{carte.2}Puis, la définition. Contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie. Et ses sept traits. "
        "{carte.3}L'idéologie fixe un but suprême : la classe, la nation, la race. Et Arendt nous le rappelle : la confiance des masses, pas la seule terreur. "
        "{carte.4}Trois régimes, une trajectoire. Nés du renversement de la démocratie, ils ont ouvert la voie à la guerre. Et ils ont fini par échouer.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : de la Grande Guerre au pouvoir. Les tranchées. Les révolutions de mille neuf cent dix-sept à mille neuf cent vingt. "
        "La marche sur Rome. Et comment on a remis le pouvoir à Hitler.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LE TOTALITARISME", branches=[
            dict(t="1929 · un débat", items=["deux crises : et / ou ?", "Taylor · Hehn · Winter", "+ l'idéologie totalitaire ?"]),
            dict(t="Définition", items=["contrôle total · contrainte", "transformer l'homme : un homme nouveau", "sept traits"]),
            dict(t="Idéologie · adhésion", items=["classe · nation · race", "un but suprême, tous les moyens", "Arendt : la confiance des masses"]),
            dict(t="Une trajectoire", items=["URSS 1924-53 · Italie 1922-43", "Allemagne 1933-45", "démocratie renversée → guerre → échec"])]),
        "fin": dict(type="mot", t="Prochain épisode : de la Grande Guerre au pouvoir", g="Épisode 2 · 1914 – 1933", y=270, taille=62),
    }),
]

QUIZ = [
    dict(q="Pourquoi le chapitre s'ouvre-t-il sur deux photographies de 1929 ?",
         r=["1929 ouvre deux crises à la fois : celle du capitalisme et la menace totalitaire", "1929 est l'année où Hitler arrive au pouvoir",
            "1929 est l'année où la guerre commence", "1929 est l'année de la marche sur Rome"], ok=0, voir="deux",
         ex="Le krach de New York et le congrès du parti nazi à Nuremberg : une crise a-t-elle mené à la guerre, l'autre, ou les deux ?"),
    dict(q="Quel historien attribue la Seconde Guerre mondiale à l'échec des démocraties à arrêter Hitler ?",
         r=["A. J. P. Taylor", "Paul N. Hehn", "Jay Winter", "Hannah Arendt"], ok=0, voir="hist",
         ex="Les Origines de la Seconde Guerre mondiale (1961) : une « thèse très controversée », dit le cours."),
    dict(q="Pour Jay Winter, qu'est-ce que la période 1914-1945 ?",
         r=["Une seule « guerre de Trente Ans »", "Un conflit économique", "Un âge de prospérité", "Le seul échec de l'apaisement"], ok=0, voir="hist",
         ex="Le second conflit prolonge directement le premier. Hehn, lui, voit un conflit économique."),
    dict(q="Quelle est la définition du totalitarisme donnée par le cours ?",
         r=["Un régime qui cherche à contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie",
            "Tout régime dirigé par un seul homme", "Un régime qui ne contrôle que la vie politique", "Un régime fondé sur des élections libres"], ok=0, voir="def1",
         ex="Trois parties : contrôle total, contrainte (terreur et propagande), transformation (un homme nouveau)."),
    dict(q="Qu'est-ce qui distingue un régime totalitaire d'une dictature ordinaire ?",
         r=["Il veut transformer les gens, pas seulement les faire taire", "Il n'a pas de police", "Il n'a pas de chef",
            "Il n'utilise jamais la propagande"], ok=0, voir="dict",
         ex="Une dictature ordinaire se contente de l'obéissance ; un régime totalitaire veut un « homme nouveau »."),
    dict(q="Quel trait de la roue sépare le totalitarisme des tyrannies anciennes ?",
         r=["La technologie moderne : la communication de masse et les armes modernes", "Un chef", "Une armée", "Les impôts"], ok=0, voir="techno",
         ex="La radio, le cinéma et les armes modernes permettent au régime d'atteindre chaque foyer, chaque jour."),
    dict(q="Quel but suprême correspond à quel régime ?",
         r=["URSS : une société sans classes · Italie : la nation et l'État · Allemagne : la race",
            "URSS : la race · Italie : une société sans classes · Allemagne : la nation",
            "Les trois : la race", "Les trois : une société sans classes"], ok=0, voir="buts",
         ex="La classe, la nation, la race : parce que le but est suprême, il justifie tous les moyens."),
    dict(q="Que soutient Hannah Arendt dans Les Origines du totalitarisme (1951) ?",
         r=["Hitler et Staline avaient besoin de « la confiance des masses », pas de la seule terreur", "Ces régimes ne reposaient que sur la terreur",
            "Hitler a pris le pouvoir par un coup d'État", "Staline a été élu par une majorité"], ok=0, voir="c_ar2",
         ex="Comprendre le totalitarisme, c'est expliquer l'adhésion autant que la terreur. Mais attention : les nazis n'ont jamais eu la majorité (37,4 % au mieux)."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », introduction « Définir le totalitarisme : un débat et une définition », avec la roue des sept traits clés, l'Europe des régimes vers 1938 et la bibliographie (chiffres du vote nazi tirés de la partie I.2), tel qu'il est rédigé sur le site ; carte animée du chapitre (site).",
    "Correction du cours : la roue des traits clés vient de l'éditeur McDougal Littell (World History, 2009), écrit « MacDougal Littell » dans le cours.",
    "Hors du cours : l'effondrement de l'URSS en 1991 ; les présentations d'une ligne de la bibliographie.",
    "Citations : Hannah Arendt (Les Origines du totalitarisme, 1951) et Staline (discours du 7 janvier 1933), en traduction française.",
    "Photographies et affiches (via Wikimedia Commons) : affiche du plan quinquennal « 2 + 2 = 5 », 1931 (Yakov Guminer, domaine public) ; Hannah Arendt en 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0) ; le congrès de Nuremberg de septembre 1936 (Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
