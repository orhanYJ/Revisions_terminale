"""Histoire · H2 « Les régimes totalitaires » — édition française, épisode 9 : « Récap » (tout le chapitre).

Traduction adaptée de h2_9.py, d'après outils/serie-dnl/EDITION_FR.md (modèle : h3f_7.py). Contenu : la synthèse du
chapitre dans le site (frise, grille de synthèse et tableau comparatif des trois régimes, personnages et chiffres, notions
clés, problématique), avec la carte animée H2 (mêmes numéros de scènes que l'édition anglaise : voir h2_9.py ; la carte
passe d'elle-même en français). Rien n'est ajouté au cours.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-9"
NOTION = "Les régimes totalitaires"
NUM = 9
TITRE = "Récap"
SUIVANT = "Fin de la série · retour au cours et au quiz"
PRONONCIATION = {"Reichstag": "Raïchs-tag", "Hindenburg": "Hinne-dènn-bourg", "Biennio Rosso": "Bi-èn-nio Rosso",
                 "Weimar": "Vaï-mar", "Anschluss": "Ann-chlouss", "Lebensraum": "Lé-benss-raoum", "Mein Kampf": "Maïn Kammpf",
                 "Duce": "Doutché", "Führer": "Fu-reur", "Heil": "Haïl", "Volk": "Folk", "OVRA": "Ovra",
                 "Chamberlain": "Tchèm-beur-line", "Arendt": "A-rennt", "Taylor": "Téï-leur", "Hehn": "Hène",
                 "Jay Winter": "Djé Ouinteur", "SS": "S. S.", "NKVD": "N. K. V. D."}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}L'Italie de Mussolini. L'Allemagne de Hitler. L'Union soviétique de Staline. Trois régimes qui voulaient tout contrôler, "
        "et refaire les êtres humains selon une idéologie. Et une route, qui s'achève en septembre mille neuf cent trente-neuf. Dans la guerre.",
        "{-q1}{q2}Ce dernier épisode rassemble tout le chapitre. Et il répond à sa question. L'idéologie totalitaire a-t-elle causé "
        "la Seconde Guerre mondiale ?",
        "{-q2}{-g0}{plan}Voici le plan. {plan.1}Le chapitre sur la carte, des tranchées à la Pologne. {plan.2}Douze dates. "
        "{plan.3}Les trois régimes, côte à côte. {plan.4}Les personnages, et les chiffres. {plan.5}Une carte mentale pour chaque partie. "
        "{plan.6}Et enfin, la réponse à la question. Puis, un dernier quiz.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[0]),
        "q1": dict(type="question", t="Trois régimes. Une route vers la guerre.", bande=True),
        "q2": dict(type="question", t="L'idéologie totalitaire a-t-elle causé la guerre ?", bande=True),
        "plan": dict(type="liste", titre="Le récap, en six étapes", items=[
            "Le chapitre sur la carte, 1914 – 1939", "Douze dates", "Les trois régimes comparés",
            "Personnages et chiffres", "Une carte mentale par partie", "La réponse à la question du chapitre"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 9", t="Récap",
                      sous="Les régimes totalitaires · 1917 – 1939"),
    }),

    # ================================================================ I. des tranchées au pouvoir
    dict(id="film1", chap="Des tranchées au pouvoir", fond="nuit", humeur="tension",
         retenir="Nés dans les tranchées · 1917 les bolcheviks · oct. 1922 la marche sur Rome · 1928 le Plan · 30 janv. 1933 Hitler chancelier.",
         beats=[
        "{g1}{g1.1}Tout commence dans les tranchées. Quatre ans de massacre de masse ont banalisé la violence. George Mosse parle de "
        "{!brutalisation}brutalisation. Pour lui, la Grande Guerre est la matrice du totalitarisme. "
        "{g1.2}En Russie, la guerre fait tomber le tsar, en février mille neuf cent dix-sept. En octobre, les bolcheviks de Lénine et de Trotski prennent le pouvoir. "
        "Puis ils gagnent une guerre civile. Et l'Europe a peur du communisme.",
        "{g1.3}En Allemagne, la défaite met fin à l'Empire. La république de Weimar naît dans la violence : en janvier mille neuf cent dix-neuf, la révolte spartakiste est écrasée. "
        "{g1.4}L'Italie a gagné la guerre. Pourtant, les Italiens parlent de victoire mutilée. Viennent ensuite le Biennio Rosso, les années rouges de mille neuf cent dix-neuf et mille neuf cent vingt. "
        "Des paysans s'emparent des terres. Des ouvriers occupent les usines. Et les propriétaires paient les Chemises noires de Mussolini pour les réprimer. "
        "{g1.5}Puis Versailles. Pour les Allemands, c'est un Diktat. Pour l'armée, un coup de poignard dans le dos.",
        "{g1.6}Octobre mille neuf cent vingt-deux : la marche sur Rome. Environ vingt mille Chemises noires. La menace suffit, et le roi nomme Mussolini. "
        "{g1.7}Novembre mille neuf cent vingt-trois : le putsch de Hitler échoue à Munich. En prison, il écrit Mein Kampf.",
        "{-g1}{g2}{g2.1}En Italie, Matteotti est assassiné en mille neuf cent vingt-quatre. L'année suivante, les lois fascistissimes rendent la dictature légale. "
        "{g2.2}En Union soviétique, Staline lance le premier plan quinquennal en mille neuf cent vingt-huit, avec la collectivisation forcée. "
        "{g2.3}Les koulaks deviennent des ennemis de classe. {g2.4}Et en mille neuf cent trente-deux et trente-trois, l'Holodomor, une famine provoquée, tue des millions de personnes en Ukraine.",
        "{-g2}{g3}{g3.1}En Allemagne, la crise de mille neuf cent vingt-neuf fait des nazis le premier parti. "
        "Trente-sept virgule quatre pour cent en juillet mille neuf cent trente-deux. Mais jamais la majorité. "
        "{g3.2}Le trente janvier mille neuf cent trente-trois, Hindenburg nomme Hitler chancelier, en toute légalité. "
        "{g3.3}Le vingt-sept février, le Reichstag brûle. Les libertés sont suspendues, et les communistes pourchassés.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 3, 4, 5, 6, 7]),
        "g2": dict(type="globe", code="H2", sc=[8, 12, 15, 19]),
        "g3": dict(type="globe", code="H2", sc=[16, 20, 21]),
    }),

    # ================================================================ II. la route de la guerre
    dict(id="film2", chap="La route de la guerre", fond="nuit", humeur="tension",
         retenir="1935 l'Abyssinie · 1936 la Rhénanie · 1938 l'Anschluss et Munich · mars 1939 Prague · 1er sept. 1939 la Pologne.",
         beats=[
        "{g4}{g4.1}En Asie, le Japon veut l'autarcie, et se dit une race supérieure. En mille neuf cent trente et un, il s'empare de la Mandchourie. "
        "{g4.2}Octobre mille neuf cent trente-cinq : Mussolini envahit l'Abyssinie, au nom de Rome. La SDN discute de sanctions pendant sept mois. "
        "Et elle épargne le pétrole. "
        "{g4.3}Mars mille neuf cent trente-six : les troupes de Hitler entrent dans la Rhénanie démilitarisée. C'est un pari : elles avaient l'ordre de se retirer si la France réagissait. "
        "La France n'a pas réagi. "
        "{g4.4}Mille neuf cent trente-six, c'est aussi l'année de l'Axe Rome-Berlin. Et de la guerre d'Espagne, où les dictateurs interviennent, et où les démocraties restent à l'écart.",
        "{g4.5}Décembre mille neuf cent trente-sept, à Nankin. L'armée japonaise tue civils et prisonniers par centaines de milliers. "
        "{g4.6}Mars mille neuf cent trente-huit : l'Anschluss. {g4.7}Septembre mille neuf cent trente-huit, à Munich. Chamberlain et Daladier livrent les Sudètes à Hitler, "
        "sans les Tchèques. C'est l'apogée de l'apaisement. {g4.8}Mars mille neuf cent trente-neuf : Prague. Hitler a menti, et l'apaisement est mort.",
        "{g4.9}Août mille neuf cent trente-neuf : le pacte germano-soviétique. En secret, il prévoit le partage de la Pologne. {g4.10}Et le premier septembre, l'Allemagne attaque la Pologne. "
        "Le trois, la France et le Royaume-Uni déclarent la guerre.",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[18, 27, 28, 29, 32, 33, 34, 35, 36, 37]),
    }),

    # ================================================================ III. douze dates
    dict(id="dates", chap="Douze dates", fond="nuit", humeur="calme",
         retenir="1917 · 1919 · 1922 · 1925 · 1928 · 1932-1933 · 1933 · 1935 · 1936 · 1937-1938 · 1938 · 1939.",
         beats=[
        "{fr}Maintenant, douze dates à savoir par cœur. {fr.1}Octobre mille neuf cent dix-sept : le coup de force bolchevik. {fr.2}Mille neuf cent dix-neuf : le traité de Versailles. "
        "{fr.3}Octobre mille neuf cent vingt-deux : la marche sur Rome. {fr.4}Mille neuf cent vingt-cinq : les lois fascistissimes, et Mein Kampf. "
        "{fr.5}Mille neuf cent vingt-huit : le premier plan quinquennal. "
        "{fr.6}Mille neuf cent trente-deux et trente-trois : l'Holodomor. {fr.7}Le trente janvier mille neuf cent trente-trois : Hitler devient chancelier. "
        "{fr.8}Octobre mille neuf cent trente-cinq : l'Abyssinie. "
        "{fr.9}En mars mille neuf cent trente-six, la Rhénanie. {fr.10}Mille neuf cent trente-sept et trente-huit : la Grande Purge. {fr.11}Septembre mille neuf cent trente-huit : Munich. "
        "{fr.12}Août mille neuf cent trente-neuf : le pacte. Et enfin, la Pologne.",
        ("P", 3.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Bolcheviks", d=1917, q="octobre"), dict(nom="Versailles", d=1919, q="le « Diktat »"),
            dict(nom="Rome", d=1922, q="la marche sur Rome"), dict(nom="Dictatures", d=1925, q="Italie · Mein Kampf"),
            dict(nom="Plan", d=1928, q="plan quinquennal"), dict(nom="Holodomor", d=1932, q="1932-1933, Ukraine"),
            dict(nom="Hitler", d=1933, q="30 janvier"), dict(nom="Abyssinie", d=1935, q="octobre"),
            dict(nom="Rhénanie", d=1936, q="7 mars"), dict(nom="Purge", d=1937, q="1937-1938"),
            dict(nom="Munich", d=1938, q="29-30 sept."), dict(nom="Guerre", d=1939, q="août – sept.")]),
    }),

    # ================================================================ IV. trois régimes : idéologie, chef, parti
    dict(id="comparer1", chap="Trois régimes, une même machine", fond="nuit", humeur="lumiere",
         retenir="La nation, la race, la classe : trois buts suprêmes. Dans chacun, un chef, un parti, un symbole.",
         beats=[
        "{gc}Maintenant, les trois régimes côte à côte, comme dans la grille de synthèse du cours. "
        "F pour le fascisme, N pour le nazisme, S pour le stalinisme. {gc.1}D'abord, l'idéologie : un ensemble de croyances qui fixe un but suprême. "
        "{l1}{l1.1}Pour Mussolini, c'est la nation, et l'État absolu. Tout est dans l'État. L'humanité se divise en nations, pas en classes. "
        "Et le fascisme ne devient raciste qu'en mille neuf cent trente-huit. {l1.2}Pour Hitler, c'est la race. L'histoire est une guerre permanente entre les races. "
        "{l1.3}Pour Staline, c'est la classe. La lutte des classes, pas de propriété privée, et à la fin, une société sans classes.",
        "{-l1}{gc.2}Ensuite, le chef. Il est construit comme un homme idéal, en qui la nation se reconnaît. {l2}{l2.1}Mussolini est il Duce. "
        "Et il Duce a toujours raison. {l2.2}Hitler est der Führer. Le salut officiel devient Heil Hitler. "
        "{l2.3}Staline est le petit père des peuples. En mille neuf cent vingt-cinq, une ville est même rebaptisée Stalingrad.",
        "{-l2}Enfin, un parti unique, avec un symbole. {l3}{l3.1}Le Parti national fasciste, et le faisceau romain. "
        "{l3.2}Le parti nazi, et la croix gammée. {l3.3}Le Parti communiste, et la faucille et le marteau. Pourquoi tout cela ? "
        "Pour confondre la nation, le parti et le chef. Dès lors, critiquer le chef, c'est trahir son pays.",
    ], vis={
        "gc": dict(type="globe", code="H2", sc=[0, 9]),
        "l1": dict(type="liste", titre="1 · Le but suprême", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"],
                   cles=["nation", "race", "classe"], items=[
            "La nation et l'État absolu · raciste seulement à partir de 1938", "La race : l'histoire comme une guerre entre races",
            "La classe : pas de propriété, une société sans classes"]),
        "l2": dict(type="liste", titre="2 · Le chef", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Il Duce · « il Duce ha sempre ragione »", "Der Führer · « Heil Hitler »",
            "Le petit père des peuples · Stalingrad, 1925"]),
        "l3": dict(type="liste", titre="3 · Un parti, un symbole", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Parti national fasciste · le faisceau romain", "NSDAP · la croix gammée", "Parti communiste · la faucille et le marteau"]),
    }),

    # ================================================================ V. homme nouveau, terreur, expansion
    dict(id="comparer2", chap="Homme nouveau, terreur, expansion", fond="nuit", humeur="tension",
         retenir="Même méthode, même homme nouveau — mais pas la même ampleur : l'URSS la plus meurtrière, l'Italie la moins.",
         beats=[
        "{gn}{gn.1}Quatrièmement, l'homme nouveau. Une dictature veut le silence. Un régime totalitaire veut que tu changes. Et cela commence par les enfants. "
        "{l4}{l4.1}En Italie, il y a les Balilla. L'homme nouveau doit être fort et cultivé, au service du Parti. "
        "{l4.2}En Allemagne, les Jeunesses hitlériennes sont obligatoires de dix à dix-huit ans. Le but : une race purifiée, le Volk. "
        "D'où l'enseignement racial à l'école, et les lois de Nuremberg de mille neuf cent trente-cinq. "
        "{gn.2}{l4.3}En Union soviétique, il y a le Komsomol. L'homme nouveau est l'ouvrier, et son héros est le mineur Stakhanov.",
        "{-l4}{gn.3}Cinquièmement, la terreur. Pas un accident : une méthode de gouvernement. {l5}{l5.1}En Italie, l'OVRA et le Tribunal spécial. "
        "Les opposants sont réduits au silence, ou envoyés en relégation, plutôt que tués. {l5.2}En Allemagne, la Gestapo et les SS, tous deux sous Himmler. "
        "Les camps, à partir de Dachau en mille neuf cent trente-trois. Et quatre cent mille Allemands stérilisés. "
        "{gn.4}{l5.3}En Union soviétique, le NKVD, le Goulag, et la Grande Purge : six cent quatre-vingt mille exécutions. "
        "{gn.5}La terreur dévore même les siens. La Nuit des longs couteaux. Iejov, fusillé et effacé des photographies. Trotski, assassiné au Mexique.",
        "{-l5}{l6}{gn.6}Sixièmement, l'expansion. {l6.1}Mussolini veut un empire au nom de Rome : c'est l'Abyssinie. "
        "{l6.2}Hitler veut le Lebensraum : l'espace vital à l'Est, annoncé dans Mein Kampf. "
        "{l6.3}Staline construit le socialisme dans un seul pays. Mais en août mille neuf cent trente-neuf, il partage la Pologne avec Hitler.",
        "{-l6}{-gn}{nu}Alors, que voit-on ? {!la même machine}La même machine dans les trois. Mais pas la même ampleur. "
        "La terreur soviétique tue à la plus grande échelle. La violence nazie est biologique : elle vise une race, et ceux qu'elle juge inaptes. "
        "Et l'Italie est la moins meurtrière. Elle garde des contre-pouvoirs : le roi, et l'Église. "
        "Cette nuance distingue une bonne réponse d'une liste de ressemblances.",
    ], vis={
        "gn": dict(type="globe", code="H2", sc=[11, 26, 22, 17, 38, 10]),
        "l4": dict(type="liste", titre="4 · L'homme nouveau", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Balilla · fort et cultivé, pour le Parti", "Jeunesses hitlériennes (10-18 ans) · le Volk, une race purifiée",
            "Komsomol · l'ouvrier : Stakhanov, 1935"]),
        "l5": dict(type="liste", titre="5 · La terreur de masse", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "OVRA, Tribunal spécial · la relégation", "Gestapo et SS · Dachau · 400 000 stérilisés",
            "NKVD · le Goulag · 680 000 exécutions, 1937-1938"]),
        "l6": dict(type="liste", titre="6 · L'expansion", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Un empire au nom de Rome · l'Abyssinie, 1935", "Le Lebensraum à l'Est · Mein Kampf, 1925",
            "Le socialisme dans un seul pays · la Pologne partagée, 1939"]),
        "nu": dict(type="note", terme="La nuance qui fait la différence", cles=["méthode", "ampleur", "critère"],
                   t="Identiques dans la méthode et dans le but, inégaux par l'ampleur et par le critère qui désigne la victime : "
                     "social en URSS, biologique en Allemagne, politique en Italie."),
    }),

    # ================================================================ VI. personnages et chiffres
    dict(id="gens", chap="Personnages et chiffres", fond="nuit", humeur="calme",
         retenir="37,4 % : jamais la majorité · 7 % → 90 % de foyers collectivisés · 680 000 exécutions dans la Grande Purge.",
         beats=[
        "{pe}Douze personnages. {pe.1}Mussolini, {pe.2}Hitler {pe.3}et Staline. {pe.4}Victor-Emmanuel trois, qui nomme Mussolini. "
        "{pe.5}Hindenburg, qui nomme Hitler. {pe.6}Matteotti, le député socialiste assassiné en mille neuf cent vingt-quatre. "
        "{pe.7}Himmler, chef de la Gestapo et des SS. {pe.8}Iejov, chef du NKVD, exécuté en mille neuf cent quarante. "
        "{pe.9}Stakhanov, l'ouvrier modèle. {pe.10}Chamberlain {pe.11}et Daladier, les hommes de Munich. "
        "{pe.12}Et Hannah Arendt. Pour elle, ces régimes reposaient sur la confiance des masses, pas sur la seule terreur.",
        "{-pe}{ch}Et six chiffres. {ch.1}Environ vingt mille Chemises noires sur la route de Rome. "
        "{ch.2}Trente-sept virgule quatre pour cent pour les nazis en juillet mille neuf cent trente-deux. Jamais la majorité. "
        "{ch.3}Cinq millions six cent mille chômeurs en Allemagne, la même année. "
        "{ch.4}La collectivisation : sept pour cent des foyers paysans soviétiques en mille neuf cent vingt-huit. Quatre-vingt-dix pour cent en mille neuf cent trente-six. "
        "{ch.5}Six cent quatre-vingt mille exécutions dans la Grande Purge. {ch.6}Et quatre cent mille Allemands stérilisés de force.",
    ], vis={
        "pe": dict(type="nuage", items=["Mussolini", "Hitler", "Staline", "Victor-Emmanuel III", "Hindenburg", "Matteotti",
                                        "Himmler", "Iejov", "Stakhanov", "Chamberlain", "Daladier", "Hannah Arendt"]),
        "ch": dict(type="liste", titre="Six chiffres", items=[
            "≈ 20 000 Chemises noires marchent sur Rome (1922)", "37,4 % pour le parti nazi, juillet 1932 — jamais la majorité",
            "5,6 millions de chômeurs en Allemagne (1932)", "7 % → 90 % des foyers paysans collectivisés (1928-1936)",
            "680 000 exécutions dans la Grande Purge (1937-1938)", "400 000 Allemands stérilisés de force (1933-1945)"],
            x=150, y=100, w=980),
    }),

    # ================================================================ VII. trois cartes mentales
    dict(id="cartes", chap="Trois cartes mentales", fond="nuit", humeur="calme",
         retenir="Contrôle total · contrainte · transformation : un homme nouveau, pas seulement l'obéissance.",
         beats=[
        "{photo1}{def}D'abord, la notion clé du chapitre. {def.1}Le totalitarisme : un régime qui cherche à contrôler totalement la société, par la contrainte, "
        "pour transformer l'homme selon une idéologie. Trois éléments, donc. Le contrôle total. La contrainte. La transformation. "
        "C'est le dernier qui le distingue d'une dictature ordinaire.",
        "{-def}{-photo1}{c1}Première partie : d'où viennent ces régimes, et comment ils prennent le pouvoir. {c1.1}L'héritage de la Grande Guerre : "
        "la brutalisation, et la révolution russe. {c1.2}En Italie, la victoire mutilée, les années rouges, et la marche sur Rome. "
        "{c1.3}En Allemagne, Versailles, la crise, et une nomination légale. {c1.4}Puis trois idéologies : la nation, la race, la classe. "
        "{c1.5}Et le stalinisme : la collectivisation, les koulaks, l'Holodomor.",
        ("P", 2.0),
        "{-c1}{c2}Deuxième partie : comment ils contrôlent la société. {c2.1}Le culte du chef, avec les rassemblements, la radio et la censure. "
        "{c2.2}L'homme nouveau, façonné dès l'enfance, par l'école, la loi et le travail. {c2.3}La terreur de masse : la police politique, et les camps. "
        "{c2.4}La terreur contre les hommes du régime lui-même. {c2.5}Et la nuance : la même méthode, à une autre échelle.",
        ("P", 2.0),
        "{-c2}{c3}Troisième partie : pourquoi ils vont à la guerre. {c3.1}La guerre comme valeur : l'Abyssinie, et le Lebensraum. "
        "{c3.2}Le Japon : l'autarcie, et une race supérieure, de la Mandchourie à Nankin. {c3.3}Des démocraties incapables d'agir : une SDN impuissante, "
        "et l'isolationnisme américain. {c3.4}L'apaisement : la Rhénanie, l'Anschluss, Munich. "
        "{c3.5}Et la guerre : Prague, le pacte, la Pologne.",
        ("P", 2.5),
    ], vis={
        "photo1": dict(type="tableau", img="h2-nuremberg-1936", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="La « cathédrale de lumière » au-dessus du Zeppelinfeld, congrès de Nuremberg, septembre 1936 · Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE"),
        "def": dict(type="def", terme="Notion clé · le totalitarisme", cles=["totalement", "contrainte", "transformer"],
                    t="Un régime qui cherche à contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie."),
        "c1": dict(type="carte", centre="PARTIE I · RACINES ET POUVOIR", branches=[
            dict(t="L'héritage de 1914-1918", items=["la brutalisation (Mosse)", "Russie, 1917 : la peur des rouges"]),
            dict(t="L'Italie", items=["victoire mutilée · Biennio Rosso", "marche sur Rome, oct. 1922"]),
            dict(t="L'Allemagne", items=["Diktat · coup de poignard", "37,4 % → chancelier, 30 janv. 1933"]),
            dict(t="Trois idéologies", items=["nation · race · classe", "fascisme raciste à partir de 1938"]),
            dict(t="Le stalinisme", items=["plan quinquennal · collectivisation", "koulaks · Holodomor, 1932-1933"])]),
        "c2": dict(type="carte", centre="PARTIE II · LE CONTRÔLE TOTAL", branches=[
            dict(t="Le culte du chef", items=["Duce · Führer · petit père", "rassemblements, radio, censure"]),
            dict(t="L'homme nouveau", items=["Balilla · Jeunesses hitlériennes · Komsomol", "école, loi, travail"]),
            dict(t="La terreur de masse", items=["OVRA · Gestapo et SS · NKVD", "camps : Dachau, le Goulag"]),
            dict(t="La terreur dévore les siens", items=["Nuit des longs couteaux", "Grande Purge · Iejov effacé"]),
            dict(t="Même méthode, autre échelle", items=["URSS : 680 000 exécutions", "Italie : relégation, l'Église"])]),
        "c3": dict(type="carte", centre="PARTIE III · LA ROUTE DE LA GUERRE", branches=[
            dict(t="La guerre comme valeur", items=["l'Abyssinie, 1935", "Lebensraum · Mein Kampf"]),
            dict(t="Le Japon", items=["autarcie · une « race supérieure »", "Mandchourie 1931 · Nankin 1937"]),
            dict(t="Des démocraties impuissantes", items=["la SDN · l'isolationnisme américain", "Stresa · l'accord naval"]),
            dict(t="L'apaisement", items=["Rhénanie · Anschluss", "Munich, sept. 1938"]),
            dict(t="La guerre", items=["Prague, mars 1939", "le pacte · la Pologne, 1er sept."])]),
    }),

    # ================================================================ VIII. la question du chapitre
    dict(id="question", chap="La question du chapitre", fond="guerre", humeur="mystere",
         retenir="L'idéologie a fourni la volonté de guerre ; la réticence des démocraties, l'occasion.",
         beats=[
        "{hi}Alors, l'idéologie totalitaire a-t-elle causé la guerre ? Au début du chapitre, le cours donnait les réponses de trois historiens. "
        "{hi.1}Pour A. J. P. Taylor, la guerre vient de l'échec des démocraties à arrêter Hitler. Le cours la dit très controversée. "
        "{hi.2}Pour Paul Hehn, c'est un conflit économique, né du krach. "
        "{hi.3}Et pour Jay Winter, les années mille neuf cent quatorze à mille neuf cent quarante-cinq forment une seule guerre de Trente Ans.",
        "{-hi}{tr}Chacun tient une part de la vérité. Et le chapitre montre laquelle. {tr.1}Winter : les régimes sont nés dans les tranchées, "
        "de la brutalisation et de Versailles. {tr.2}Hehn : la crise a fait des nazis un parti de masse, et poussé le Japon vers l'autarcie. "
        "{tr.3}Taylor : l'apaisement a laissé réussir chaque agression.",
        "{-tr}{photo2}{rep}{rep.g}Mais le chapitre ajoute son propre candidat. Voici donc la réponse. L'idéologie totalitaire a fourni "
        "{!la volonté de guerre}la volonté de guerre. La guerre comme valeur pour le fascisme. Le Lebensraum pour le nazisme. Une race supérieure pour le Japon. "
        "{rep.d}Et la réticence des démocraties a fourni l'occasion. Chaque agression impunie a préparé la suivante. "
        "Une bonne réponse garde les deux moitiés.",
        "{-rep}{-photo2}{pa}À toi maintenant, avec la problématique du chapitre.",
        ("P", 2.5),
        "{-pa}{mod}On peut le dire ainsi. {mod.1}Les idéologies totalitaires ont fait de la guerre une valeur, et de l'expansion un but. "
        "Pense à l'Abyssinie en mille neuf cent trente-cinq, et au Lebensraum de Mein Kampf. {mod.2}Mais les démocraties ont laissé l'agression réussir : "
        "la SDN, l'isolationnisme américain, et l'apaisement, de la Rhénanie à Munich. {mod.3}Les deux se sont combinés en une chaîne que seule la guerre pouvait rompre. "
        "Après Prague et le pacte, vint la Pologne.",
        "{-mod}{kt}Et les notions clés du chapitre. {kt.1}Le totalitarisme. {kt.2}Le Lebensraum : l'espace vital. "
        "{kt.3}Et l'apaisement : accepter les exigences des agresseurs, pour éviter la guerre.",
    ], vis={
        "hi": dict(type="liste", titre="Trois historiens, trois causes", items=[
            "A. J. P. Taylor (1961) : l'échec des démocraties — « très controversé »",
            "Paul N. Hehn : un conflit économique, né du krach",
            "Jay Winter : une seule « guerre de Trente Ans », 1914 – 1945"], x=150, y=130, w=980),
        "tr": dict(type="liste", titre="Ce que montre le chapitre", marques=["W", "H", "T"], items=[
            "Winter : des régimes nés dans les tranchées — brutalisation, Versailles",
            "Hehn : la crise fait des nazis un parti de masse ; l'autarcie japonaise",
            "Taylor : l'apaisement laisse réussir chaque agression"], x=150, y=130, w=980),
        "photo2": dict(type="tableau", img="h2-munich", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Chamberlain, Daladier, Hitler, Mussolini et Ciano avant la signature des accords de Munich, 29 septembre 1938 · Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE"),
        "rep": dict(type="cols", g="La volonté de guerre", gq="l'idéologie totalitaire : la guerre comme valeur, le Lebensraum, une « race supérieure »",
                    d="L'occasion", dq="la réticence des démocraties : chaque agression impunie prépare la suivante", vs="+"),
        "pa": dict(type="pause", t="Problématique : quel rôle le totalitarisme a-t-il joué dans l'effondrement de la paix mondiale à la fin des années 1930 ? "
                                   "Ta réponse en trois phrases.",
                   sous="Mets la vidéo en pause, écris tes trois phrases, puis relance pour comparer."),
        "mod": dict(type="liste", titre="Une réponse modèle", items=[
            "Les idéologies totalitaires font de la guerre une valeur : l'Abyssinie (1935), le Lebensraum.",
            "Les démocraties laissent l'agression réussir : la SDN, l'isolationnisme, l'apaisement.",
            "Les deux forment une chaîne que seule la guerre peut rompre : Prague, le pacte, la Pologne."], x=150, y=130, w=980),
        "kt": dict(type="liste", titre="Les notions clés", marques=["1", "2", "3"], items=[
            "Le totalitarisme : contrôle total, contrainte, transformation",
            "Le Lebensraum : l'espace vital, conquis à l'Est",
            "L'apaisement : accepter les exigences des agresseurs pour éviter la guerre"], x=150, y=130, w=980),
    }),

    # ================================================================ fin
    dict(id="fin", chap="La fin", fond="nuit", humeur="calme", beats=[
        "{fin}C'est la fin de la série. Retourne maintenant au cours sur le site. Fais le quiz du chapitre. "
        "Et avant l'épreuve, rédige au moins une réponse à une question problématisée sur les régimes totalitaires.",
        ("P", 2.0),
    ], vis={
        "fin": dict(type="mot", t="À toi maintenant", g="le cours, le quiz, une question problématisée", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="Quelle définition du totalitarisme correspond au cours ?",
         r=["Un régime qui cherche à contrôler totalement la société par la contrainte, pour transformer l'homme selon une idéologie",
            "Un régime qui demande seulement d'obéir et de se taire", "Tout régime à parti unique", "Une monarchie dirigée par un dictateur"],
         ok=0, voir="def", ex="Le mot clé est la transformation : une dictature veut le silence, un régime totalitaire un homme nouveau."),
    dict(q="Qu'est-ce que la « brutalisation » de George Mosse ?", r=["La violence des tranchées transportée dans la politique d'après-guerre",
         "La dureté du traité de Versailles", "La torture policière en URSS", "Les mutineries de 1917"], ok=0, voir="g1",
         ex="Pour Mosse, la Grande Guerre est la « matrice du totalitarisme »."),
    dict(q="Comment Mussolini devient-il président du Conseil en octobre 1922 ?", r=["Il est nommé par le roi après la marche sur Rome",
         "Il gagne la majorité aux élections", "Il prend d'assaut le Parlement avec l'armée", "Il est choisi par le pape"], ok=0, voir="g1",
         ex="L'intimidation, puis une nomination légale — le même schéma que Hitler en 1933."),
    dict(q="Quel est le meilleur score du parti nazi dans une élection libre ?", r=["37,4 % en juillet 1932", "51 % en juillet 1932",
         "18,3 % en 1928", "33,1 % en mars 1933"], ok=0, voir="ch", ex="Le premier parti, jamais la majorité : Hindenburg nomme Hitler."),
    dict(q="Quel est le but suprême de chaque régime ?", r=["La nation (fascisme), la race (nazisme), la classe (stalinisme)",
         "La race (fascisme), la classe (nazisme), la nation (stalinisme)", "La classe pour les trois", "La religion, la race, la nation"], ok=0, voir="l1",
         ex="La même ambition totalitaire, des idéologies opposées."),
    dict(q="L'Holodomor, c'est…", r=["la famine provoquée de 1932-1933 en Ukraine", "le plan quinquennal soviétique",
         "la police politique soviétique", "une ferme collective"], ok=0, voir="g2",
         ex="Le résultat de la collectivisation forcée et des réquisitions de grain."),
    dict(q="Quelle organisation de jeunesse appartient à l'Italie fasciste ?", r=["Les Balilla", "Le Komsomol", "Les Jeunesses hitlériennes", "Les SA"],
         ok=0, voir="l4", ex="Komsomol (URSS), Jeunesses hitlériennes (Allemagne, obligatoires de 10 à 18 ans)."),
    dict(q="Combien d'exécutions la Grande Purge de 1937-1938 a-t-elle causées ?", r=["680 000", "85", "70 000", "6 millions"], ok=0, voir="l5",
         ex="85, c'est la Nuit des longs couteaux ; environ 70 000, les victimes de T4."),
    dict(q="Quelle notion clé signifie « espace vital » ?", r=["Lebensraum", "Anschluss", "Volksgemeinschaft", "Diktat"], ok=0, voir="l6",
         ex="Formulée par Ratzel (1901), transformée en programme de conquête dans Mein Kampf (1925)."),
    dict(q="Qu'est-ce qui met fin à l'apaisement en mars 1939 ?", r=["L'occupation de Prague par l'Allemagne", "L'Anschluss",
         "Le pacte germano-soviétique", "L'invasion de l'Abyssinie"], ok=0, voir="g4",
         ex="Hitler avait menti à Munich ; le Royaume-Uni et la France garantissent alors la Pologne."),
    dict(q="Quel historien impute la guerre à l'échec des démocraties à arrêter Hitler ?", r=["A. J. P. Taylor", "Jay Winter",
         "Paul N. Hehn", "George Mosse"], ok=0, voir="hi", ex="Winter : la « guerre de Trente Ans » ; Hehn : un conflit économique."),
    dict(q="La réponse du chapitre à sa problématique est que…", r=["l'idéologie a fourni la volonté de guerre, la réticence des démocraties l'occasion",
         "seule la crise de 1929 a causé la guerre", "les démocraties voulaient la guerre", "la guerre était un accident"], ok=0, voir="rep",
         ex="Une bonne réponse garde les deux moitiés."),
]

CREDITS = [
    "Contenu : la synthèse du cours d'histoire de Terminale, chapitre « Les régimes totalitaires », telle qu'elle est rédigée sur le site, "
    "avec la grille de synthèse du cours ; la carte animée du chapitre (site).",
    "Photographies (via Wikimedia Commons) : le congrès de Nuremberg de septembre 1936 (Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE) ; les accords de Munich, 29 septembre 1938 (Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE).",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
