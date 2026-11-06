"""Histoire · H1 « Le krach de Wall Street et son impact » — édition française, épisode 6 : « Récap » (tout le chapitre).

Traduction et adaptation de h1_6.py (cahier des charges : EDITION_FR.md) ; même chaîne : outils/serie-philo/generer.py h1f_6 ;
sortie dans dnl/serie/. Mêmes scènes, mêmes visuels, mêmes repères, mêmes globes (la carte animée passe d'elle-même
en français). Key terms → notions clés, key issues → problématiques ; plus de mention de la DNL ni du professeur.
Contenu : la synthèse du chapitre H1 dans le site (dnl/index.html, CHAPTERS.H1, champs fr), avec la carte animée H1 :
  H1 : 0 ordre libéral 1919 · 3 Dawes · 5 krach · 8 faillites bancaires · 9 prêts rappelés · 15 Smoot-Hawley ·
       17 effet domino 1931 · 18 Mandchourie · 21 Hitler 1933 · 22 New Deal · 29 Rhénanie · 30 Anschluss et Munich ·
       31 Prague puis Pologne · 32 cash and carry
  H2 : 0 trois régimes, une trajectoire · 20 Hitler chancelier (30 janvier 1933)
Axe : axe Rome-Berlin 1936, pacte tripartite septembre 1940, comme dans le cours corrigé.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-6"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 6
TITRE = "Récap"
SUIVANT = "Chapitre suivant · H2 Les régimes totalitaires"
PRONONCIATION = {"Creditanstalt": "Krédit-anchtalt", "Anschluss": "Anchlouss", "Mukden": "Moukdène",
                 "Kwantung": "Kouan-toung", "Lytton": "Liteune", "Hoovervilles": "Houveur-villes", "Hoover": "Houveur",
                 "Smoot-Hawley": "Smoute-Hôlé", "Smoot": "Smoute", "Hawley": "Hôlé", "Dawes": "Dôze",
                 "Briand-Kellogg": "Briand-Kélog", "Roosevelt": "Rouzvelt", "Coolidge": "Coulidje", "Lange": "Lang",
                 "Owens": "Ôwennz", "Chamberlain": "Tchèmbeurlinne", "Panay": "Panaï", "Low": "Lô",
                 "Dow Jones": "Dao Djonce", "Migrant Mother": "Maïgrante Mazeur", "RCA": "R. C. A.",
                 "USS": "U. S. S.", "Stimson": "Stimsonne", "Ottawa": "Otaoua", "Nipomo": "Nipômo",
                 "Dust Bowl": "Deust Bôl", "Import Duties Act": "Importe Diouti-z Acte", "cash and carry": "cache ènde carri",
                 "Tennessee Valley Authority": "Ténéssi Vali Otorité", "Civilian Conservation Corps": "Civilianne Conservation Corps",
                 "Stepping Stones to Glory": "Stèpingue Stônz tou Glori", "Sherman": "Chèrmane"}

# Étude de cas, document 2 : chômage allemand (travailleurs assurés, %) ; vote nazi (cours, II.2 idée 2)
CHOMAGE = [[1928, 8.6], [1929, 13.3], [1930, 22.7], [1931, 34.3], [1932, 43.8], [1933, 36.2]]
VOTE_NSDAP = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.3], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Octobre 1929. Une foule silencieuse attend devant la Bourse de New York. "
        "Dix ans plus tard, l'Europe est de nouveau en guerre. Alors, comment passe-t-on de l'un à l'autre ?",
        "{-q1}{q2}Cette question, c'est tout le chapitre un. Et cet épisode le reprend en entier.",
        "{-q2}{-g0}{plan}Voici le plan. {plan.1}D'abord, l'histoire sur la carte. "
        "{plan.2}Puis la frise, et l'enchaînement de la crise. {plan.3}Puis les six parties, avec un exemple pour chacune. "
        "{plan.4}Les personnages et les chiffres. {plan.5}Et pour finir, l'épreuve.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="question", t="D'un krach à New York… à une guerre mondiale ?", bande=True),
        "q2": dict(type="question", t="Tout le chapitre, en un épisode.", bande=True),
        "plan": dict(type="liste", titre="Ce récap", items=[
            "L'histoire sur la carte, 1919 – 1939", "La frise et l'enchaînement de la crise",
            "Les six parties : une idée, un exemple", "Personnages et chiffres", "L'épreuve : notions clés et problématiques"],
            x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · H1 · Épisode 6", t="Récap",
                      sous="Le krach de Wall Street et son impact · 1919 – 1939"),
    }),

    # ================================================================ I. le film du chapitre
    dict(id="film", chap="L'histoire sur la carte", fond="nuit", humeur="tension",
         retenir="1919 l'ordre libéral · 1924 plan Dawes · oct. 1929 le krach · 1930–32 faillites bancaires · 1930 Smoot–Hawley · 1931 dominos et Mandchourie · 1933 Hitler et le New Deal · 1936 Rhénanie · 1938 Munich.",
         beats=[
        "{g1}{g1.1}Tout commence par une paix. Paris, 1919. Les Quatorze Points du président Wilson deviennent un ordre mondial libéral. "
        "La démocratie. Le droit des peuples à disposer d'eux-mêmes. Le libre-échange. Et une Société des Nations, à Genève. "
        "Mais le Sénat américain refuse le traité, et les États-Unis n'y entreront jamais.",
        "{g1.2}1924 : le plan Dawes. L'Allemagne emprunte huit cents millions de marks. L'argent américain paie les réparations allemandes, "
        "et les dettes de guerre des Alliés reviennent à Washington. Désormais, l'Europe dépend du crédit américain.",
        "{g1.3}Octobre 1929 : le krach. Le jeudi noir, le vingt-quatre. Puis le lundi noir, et le mardi noir. "
        "La Bourse avait triplé en cinq ans, portée par la spéculation. Maintenant, elle s'effondre.",
        "{g1.4}À partir de 1930, les banques font faillite. Environ cinq mille d'entre elles, jusqu'en 1932. "
        "Et c'est là que la Grande Dépression commence vraiment. "
        "{g1.5}Les banques américaines rappellent leurs prêts à l'Europe. L'Allemagne, la plus exposée, est frappée la première.",
        "{g1.6}Le dix-sept juin 1930, Hoover signe le tarif Smoot-Hawley. Le Canada avait déjà riposté, en mai. "
        "La guerre commerciale a commencé.",
        "{-g1}{g2}{g2.1}1931 : les dominos tombent en Europe. La Creditanstalt, à Vienne, en mai. Les banques allemandes en juillet. "
        "Et en septembre, le Royaume-Uni abandonne l'étalon-or. {g2.2}Le même mois, le dix-huit, "
        "survient l'incident de Mukden. Le Japon envahit la Mandchourie, et la Société des Nations ne peut rien faire.",
        "{g2.3}Janvier 1933 : Hitler est nommé chancelier. Pourtant, les nazis n'ont jamais obtenu la majorité. "
        "{g2.4}La même année, aux États-Unis, Roosevelt lance le New Deal. Secourir, relancer, réformer.",
        "{g2.5}Le sept mars 1936, l'armée allemande entre en Rhénanie. La France et le Royaume-Uni ne font rien. "
        "{g2.6}1938 : l'Anschluss, puis Munich. Les Sudètes sont livrés à Hitler. C'est l'apaisement.",
        ("P", 1.5),
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[0, 3, 5, 8, 9, 15]),
        "g2": dict(type="globe", code="H1", sc=[17, 18, 21, 22, 29, 30]),
    }),

    # ================================================================ II. la frise
    dict(id="dates", chap="La frise", fond="nuit", humeur="calme",
         retenir="1919 · 1924 · 1928 · oct. 1929 · juin 1930 · 1931 · 1932 · 1933 · 1935 · 1936 · 1938 · 1939.",
         beats=[
        "{fr}Voici maintenant la frise du cours, en douze étapes. {fr.1}1919 : Versailles, et la Société des Nations. "
        "{fr.2}1924 : le plan Dawes. {fr.3}1928 : le pacte Briand-Kellogg met la guerre hors la loi. "
        "{fr.4}Octobre 1929 : le krach. {fr.5}Juin 1930 : Smoot-Hawley. "
        "{fr.6}1931 : la Creditanstalt fait faillite. Le Royaume-Uni quitte l'or. Le Japon prend la Mandchourie. "
        "{fr.7}1932 : l'Import Duties Act, la note Stimson… et Roosevelt est élu. "
        "{fr.8}1933 : Hitler devient chancelier. Le New Deal a ses cent jours. Le Japon quitte la SDN. "
        "{fr.9}1935 : l'Italie envahit l'Éthiopie, et l'Amérique vote sa première loi de neutralité. "
        "{fr.10}1936 : la Rhénanie, et le Front populaire. "
        "{fr.11}1938 : l'Anschluss, puis Munich. {fr.12}Et 1939. Prague en mars. La Pologne le premier septembre. "
        "Et le cash and carry en novembre.",
        ("P", 7.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Versailles", d=1919, q="Société des Nations"), dict(nom="Plan Dawes", d=1924, q="800 millions de marks"),
            dict(nom="Briand–Kellogg", d=1928, q="guerre hors la loi"), dict(nom="Le krach", d=1929, q="24–29 oct."),
            dict(nom="Smoot–Hawley", d=1930, q="17 juin"), dict(nom="Dominos", d=1931, q="or · Mandchourie"),
            dict(nom="Roosevelt élu", d=1932, q="Import Duties Act"), dict(nom="Hitler · New Deal", d=1933, q="janv. · 100 jours"),
            dict(nom="Éthiopie", d=1935, q="loi de neutralité"), dict(nom="Rhénanie", d=1936, q="Front populaire"),
            dict(nom="Munich", d=1938, q="Anschluss · sept."), dict(nom="La guerre", d=1939, q="Pologne · cash and carry")]),
    }),

    # ================================================================ III. la chaîne de la crise
    dict(id="chaine", chap="L'enchaînement de la crise", fond="nuit", humeur="tension",
         retenir="Krach → faillites bancaires → prêts rappelés → protectionnisme → commerce mondial −66 % → dépression mondiale. Puis deux voies : les démocraties se replient, trois régimes choisissent le militarisme.",
         beats=[
        "{ch}Un schéma tient toute la première partie. Comment un krach est-il devenu une dépression mondiale ? En six maillons. "
        "{ch.1}Le krach de Wall Street, en octobre 1929 : le cours des actions s'effondre. "
        "{ch.2}Puis les banques font faillite. Le crédit se tarit, l'épargne est anéantie. "
        "{ch.3}Les États-Unis rappellent leurs prêts à l'étranger. L'Europe perd les capitaux américains, et l'Allemagne avant tout. "
        "{ch.4}Vient le protectionnisme : des droits de douane, et une chaîne de représailles. "
        "{ch.5}Le commerce mondial s'effondre. Sa valeur baisse d'environ deux tiers, entre 1929 et 1934. "
        "{ch.6}Et le résultat, c'est une dépression mondiale, avec un chômage de masse et des prix qui chutent.",
        "{-ch}{deux}La deuxième partie en découle. Face à la Dépression, le monde prend deux voies. "
        "Les grandes démocraties se replient. Nationalisme économique, isolement, apaisement. "
        "Et trois régimes, en Allemagne, en Italie et au Japon, choisissent le militarisme.",
    ], vis={
        "ch": dict(type="liste", titre="Comment le krach est devenu une dépression mondiale", items=[
            "Krach de Wall Street (oct. 1929) : les actions s'effondrent", "Faillites bancaires : le crédit se tarit, l'épargne disparaît",
            "Les États-Unis rappellent leurs prêts : l'Allemagne perd ses capitaux", "Protectionnisme : droits de douane et représailles",
            "Le commerce mondial s'effondre : environ −66 % (1929–1934)", "Dépression mondiale : chômage de masse, déflation"],
            x=150, y=105, w=980),
        "deux": dict(type="cols", g="Les démocraties", gq="nationalisme économique, puis repli : isolement et apaisement",
                     d="Trois régimes", dq="Allemagne, Italie, Japon : le militarisme", vs="ou"),
    }),

    # ================================================================ IV. I.1
    dict(id="p11", chap="I.1 · Le grand krach", fond="nuit", humeur="tension",
         retenir="La Bourse · les Années folles · production de masse · spéculation (crédit : 90 %) · une économie réelle qui ralentit déjà · la panique : −89 % (381 → 41).",
         beats=[
        "{ph}{i1}Passons aux idées, partie par partie, avec un exemple pour chacune. Première partie, section un : qu'est-ce que le krach de 1929 ? "
        "{i1.1}La Bourse, c'est là où les entreprises lèvent de l'argent, et où les investisseurs achètent une part des bénéfices. "
        "Un exemple, pris hors du cours : RCA ne versait aucun dividende. Et pourtant, son action s'est envolée.",
        "{i1.2}Les Années folles apportent croissance et optimisme, sur fond de politique républicaine. Trois présidents républicains de suite : "
        "Harding, Coolidge, puis Hoover. Peu d'impôts. Des trusts. Des droits de douane. {i1.3}La production de masse rend possible la consommation de masse. "
        "En 1925, une Ford modèle T ne coûte plus qu'environ deux cent soixante dollars.",
        "{i1.4}La spéculation fait gonfler la Bourse. Les courtiers prêtent jusqu'à quatre-vingt-dix pour cent du prix d'une action. "
        "Alors une baisse de dix pour cent suffit à ruiner l'acheteur. {i1.5}Pendant ce temps, l'économie réelle ralentit déjà. "
        "Les prix agricoles baissent depuis 1920. {i1.6}Puis, fin octobre 1929, c'est la panique. "
        "Et les ventes s'entretiennent elles-mêmes.",
        "{-i1}{-ph}{dj}Retiens un chiffre. En septembre 1929, le Dow Jones culmine à trois cent quatre-vingt-un points. "
        "En juillet 1932, il tombe à quarante et un. Une perte de quatre-vingt-neuf pour cent.",
        "{-dj}{fac}Dans une réponse à une question problématisée sur les causes, hiérarchise les facteurs. Ne te contente pas de les énumérer. "
        "{fac.1}La spéculation est le déclencheur. "
        "{fac.2}La surproduction et les inégalités de richesse expliquent pourquoi la chute ne s'arrête pas. "
        "{fac.3}Et la panique et la politique l'aggravent. Ce sont des amplificateurs, pas l'origine.",
    ], vis={
        "ph": dict(type="tableau", img="h1-wallstreet", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .6],
                   legende="Foule devant la Bourse de New York après le krach, octobre 1929 (Wikimedia Commons, domaine public)"),
        "i1": dict(type="liste", titre="I.1 · Qu'est-ce que le krach de 1929 ?", items=[
            "La Bourse : actions, dividendes · RCA (hors cours)", "Les Années folles : Harding, Coolidge, Hoover",
            "Production de masse : la Ford T à environ 260 $ (1925)", "Spéculation : achat à crédit, jusqu'à 90 %",
            "L'économie réelle ralentit : prix agricoles en baisse depuis 1920", "La panique : 24–29 oct. 1929, 16 millions d'actions le 29"],
            x=130, y=105, w=1020),
        "dj": dict(type="mot", t="−89 %", g="Dow Jones : 381 (sept. 1929) → 41 (juillet 1932) · retrouvé seulement en 1954", y=250, taille=150),
        "fac": dict(type="liste", titre="Les causes du krach : une hiérarchie", items=[
            "Déclencheur : la spéculation (la Bourse ×3 en 1924–29)", "Profondeur : surproduction, inégalités, pas de débouchés",
            "Amplificateurs : panique, politique républicaine, dépôts non garantis"], x=150, y=150, w=980),
    }),

    # ================================================================ V. I.2 et I.3
    dict(id="p12", chap="I.2 · Une crise mondiale", fond="nuit", humeur="tension",
         retenir="Faillites bancaires (5 000 en 1932) · prêts rappelés · le circuit Dawes · l'étalon-or · dominos en Europe, chute des prix à la périphérie.",
         beats=[
        "{i2}Section deux : du krach américain à une crise mondiale. {i2.1}La Grande Dépression commence vraiment quand les banques font faillite. "
        "Avant 1933, les dépôts ne sont pas garantis. Une rumeur peut vider une banque. Environ cinq mille ont fait faillite en 1932.",
        "{i2.2}La crise se propage par deux canaux. Le rappel des prêts américains, et des faiblesses communes à toutes les économies. "
        "Regarde les dominos : la Creditanstalt en mai 1931. Les banques allemandes en juillet. Le Royaume-Uni quitte l'or en septembre. "
        "{i2.3}Pourquoi l'Europe est-elle si fragile ? Parce que le plan Dawes l'a attachée au crédit américain. "
        "Huit cents millions de marks prêtés en 1924. Et en 1928, "
        "les réparations atteignent deux milliards et demi de marks par an.",
        "{i2.4}L'étalon-or sert de courroie de transmission. La France s'accroche à la valeur-or du franc jusqu'en 1936. "
        "C'est l'économie développée la moins performante de la décennie. {i2.5}L'Europe est frappée par un effet domino. "
        "Et le reste du monde, par la chute des prix. Le Brésil brûle quelque soixante-dix-huit millions de sacs de café. "
        "Les recettes du nitrate chilien chutent de plus de quatre-vingts pour cent.",
    ], vis={
        "i2": dict(type="liste", titre="I.2 · Du krach américain à une crise financière mondiale", items=[
            "Faillites bancaires : dépôts non garantis, 5 000 en 1932", "Deux canaux : Creditanstalt (mai 1931) → Allemagne → Royaume-Uni",
            "Le circuit Dawes : 800 millions de marks, réparations 2,5 milliards par an", "L'étalon-or : la France, la moins performante jusqu'en 1936",
            "Dominos et chute des prix : le café brésilien, le nitrate chilien"], x=130, y=110, w=1020),
    }),

    dict(id="p13", chap="I.3 · Un traumatisme fondateur", fond="nuit", humeur="calme",
         retenir="14 millions de chômeurs (25 %) · Hoovervilles · Migrant Mother de Lange (1936) · le Dust Bowl (14 avril 1935) · un traumatisme mondial, mais inégal : l'URSS à peine touchée.",
         beats=[
        "{hv}{i3}Section trois : l'un des traumatismes fondateurs du vingtième siècle. {i3.1}Emplois, salaires, épargne : tout est détruit, "
        "et il n'y a aucun filet de sécurité. Le chômage passe de trois pour cent en 1929 à vingt-cinq pour cent en 1933. "
        "Soit quatorze millions d'Américains.",
        "{i3.2}Les Hoovervilles rendent la misère visible, au cœur même des villes. La plus grande est à Saint-Louis. Une autre se dresse dans Central Park.",
        "{-hv}{mm}{i3.3}L'État fédéral photographie lui-même la pauvreté. Voici Migrant Mother, de Dorothea Lange, mars 1936. "
        "Florence Owens Thompson, trente-deux ans, dans un camp de cueilleurs de pois à Nipomo, en Californie. "
        "{i3.4}Puis le Dust Bowl transforme la crise économique en crise écologique. Le dimanche noir, le quatorze avril 1935, "
        "le jour devient la nuit. {i3.5}Le traumatisme est donc mondial. Mais il est inégal. L'Union soviétique, hors du commerce mondial "
        "et en plein premier plan quinquennal, est à peine touchée.",
        "{-mm}",
    ], vis={
        "hv": dict(type="tableau", img="h1-hooverville-seattle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .4, .5],
                   legende="Hooverville sur le front de mer de Seattle, 1933 · Seattle Municipal Archives (Wikimedia Commons, CC BY 2.0)"),
        "mm": dict(type="tableau", img="h1-lange-migrant", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.2, .5, .3],
                   legende="Dorothea Lange, Migrant Mother, Nipomo, mars 1936 (Library of Congress, domaine public)"),
        "i3": dict(type="liste", titre="I.3 · L'un des traumatismes fondateurs du XXe siècle", items=[
            "Aucun filet de sécurité : chômage 3 % (1929) → 25 % (1933)", "Hoovervilles : Saint-Louis, Central Park",
            "La photographie comme argument : Migrant Mother (1936)", "Le Dust Bowl : le dimanche noir, 14 avril 1935",
            "Mondial mais inégal : l'URSS à peine touchée"], x=130, y=110, w=1020),
    }),

    # ================================================================ VI. II.1 et II.2
    dict(id="p21", chap="II.1 · Le nationalisme économique", fond="nuit", humeur="tension",
         retenir="Internationalisme indépendant · Smoot–Hawley (17 juin 1930, 20 000 produits) · représailles et blocs impériaux (Ottawa 1932) · Roosevelt change de cap (or 1933, accords de 1934).",
         beats=[
        "{i4}Deuxième partie, section un : le nationalisme économique. {i4.1}Avant le krach, l'Amérique de Hoover pratique un internationalisme indépendant. "
        "Les banques américaines prêtent à l'Allemagne. Mais Washington ne signe aucune alliance. {i4.2}Puis vient le protectionnisme. Smoot-Hawley relève les droits "
        "sur plus de vingt mille produits. Deux ans plus tard, Smoot et Hawley perdent tous deux leur siège.",
        "{i4.3}Le protectionnisme se répand par représailles, et les empires se ferment en blocs. À Ottawa, en 1932, "
        "le Royaume-Uni et ses dominions choisissent la préférence impériale. Le commerce mondial perd deux tiers de sa valeur. "
        "{i4.4}Roosevelt change de cap. Il quitte l'or en 1933, et signe des accords commerciaux réciproques à partir de 1934. "
        "Une vingtaine, en 1939. Et aucun avec l'Allemagne, l'Italie ou le Japon.",
    ], vis={
        "i4": dict(type="liste", titre="II.1 · Le nationalisme économique", items=[
            "Internationalisme indépendant : des prêts, mais aucune alliance", "Smoot–Hawley (1930) : 20 000 produits, 23 protestations",
            "Représailles et blocs impériaux : Ottawa, 1932", "Roosevelt change de cap : une vingtaine d'accords en 1939"],
            x=150, y=130, w=980),
    }),

    dict(id="p22", chap="II.2 · Les réponses politiques", fond="nuit", humeur="tension",
         retenir="L'Allemagne brisée : 43,8 % de chômeurs (1932) · les nazis appelés au pouvoir, jamais majoritaires · autarcie et réarmement · le militarisme dans trois régimes · le New Deal · sa diplomatie · le Front populaire.",
         beats=[
        "{gr}Section deux : les réponses politiques. Et d'abord l'Allemagne, le pays qui s'est brisé. {gr.1}Regarde l'étude de cas. "
        "Chez les travailleurs assurés, le chômage grimpe de huit virgule six pour cent en 1928… "
        "à quarante-trois virgule huit pour cent en 1932. "
        "{gr.2}Maintenant, le vote nazi. Il suit la courbe. Deux virgule six pour cent en 1928. Dix-huit virgule trois en 1930. "
        "Trente-sept virgule trois en juillet 1932. Puis, en novembre, il retombe à trente-trois virgule un.",
        "{-gr}{i5}{i5.1}Les nazis n'ont donc jamais eu la majorité. On les a fait entrer, en janvier 1933 : des conservateurs "
        "croyaient pouvoir se servir de Hitler. {i5.2}La politique économique nazie veut la stabilité, le plein emploi et l'autarcie, à tout prix. "
        "Le réarmement fait passer le chômage de six millions en 1933 à moins d'un million en 1937. "
        "{i5.3}Et le militarisme gagne trois régimes. C'est un effort d'armement, des militaires qui contrôlent le gouvernement, "
        "et une politique étrangère agressive. Au Japon, l'armée du Kwantung frappe la première en Mandchourie. Tokyo s'explique après.",
        "{-i5}{i6}Maintenant, trois autres réponses. {i6.1}Le New Deal : secourir, relancer, réformer. Il crée le Civilian Conservation Corps, la Tennessee "
        "Valley Authority, et, en 1935, la Sécurité sociale. {i6.2}La diplomatie du New Deal reconnaît l'Union soviétique, en novembre 1933. "
        "Elle signe des accords commerciaux, mais aucune alliance. {i6.3}Et en France, le Front populaire de 1936, avec Léon Blum. "
        "Les accords Matignon augmentent les salaires de sept à quinze pour cent, en une semaine. De nouvelles lois apportent la semaine de quarante heures, "
        "et deux semaines de congés payés. Mais à l'extérieur, il choisit l'apaisement.",
    ], vis={
        "gr": dict(type="graphe", titre="Allemagne : chômage et vote nazi (%)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50],
                           lx="année", ly="%"),
                   el=[dict(type="courbe", pts=CHOMAGE, c="ca", lbl="Chômeurs (travailleurs assurés)", lp=[1928.1, 47], dur=2.0),
                       dict(type="courbe", pts=VOTE_NSDAP, c="el", lbl="Vote NSDAP", lp=[1930.9, 12], dur=2.0)]),
        "i5": dict(type="liste", titre="II.2 · L'Allemagne, le régime qui s'est brisé", items=[
            "Appelés, jamais élus : Hitler chancelier, janv. 1933", "Autarcie et réarmement : 6 millions → moins d'1 million de chômeurs",
            "Le militarisme dans trois régimes : l'armée du Kwantung en Mandchourie"], x=150, y=140, w=980),
        "i6": dict(type="liste", titre="II.2 · Les autres réponses", items=[
            "Le New Deal : CCC, TVA, Sécurité sociale (1935)", "La diplomatie du New Deal : l'URSS reconnue, nov. 1933",
            "Le Front populaire (1936) : Matignon, salaires +7 à 15 %"], x=150, y=140, w=980),
    }),

    # ================================================================ VII. II.3
    dict(id="p23", chap="II.3 · Des démocraties réticentes", fond="nuit", humeur="tension",
         retenir="Wilsonisme · une SDN faible dès sa naissance · la Mandchourie · la note Stimson · les lois de neutralité · le cash and carry · l'apaisement (six raisons) · Munich, Prague, la Pologne.",
         beats=[
        "{i7}Dernière section : de grandes démocraties réticentes à défendre l'ordre libéral de 1919. "
        "{i7.1}Cet ordre repose sur les idées de Wilson. Un dessin de Punch, en décembre 1919, montre déjà la faille. "
        "La clé de voûte marquée U. S. A. manque à l'arche de la Société des Nations. {i7.2}La SDN est faible dès sa naissance. Pas d'armée. Un droit de veto pour chaque membre. "
        "Dans le dessin de David Low, Le Paillasson, en 1933, un soldat japonais lui marche simplement dessus.",
        "{i7.3}Elle ne peut donc pas arrêter une grande puissance. Regarde la Mandchourie, de 1931 à 1933. La commission Lytton condamne le Japon. "
        "Et le Japon quitte tout simplement la SDN. {i7.4}Les États-Unis le condamnent aussi, mais seulement en paroles. "
        "La note Stimson tombe le sept janvier 1932… et le Japon bombarde Shanghai.",
        "{-i7}{i8}{i8.1}De 1935 à 1937, les lois de neutralité tiennent la plus grande démocratie hors du jeu. "
        "Même après le bombardement de l'USS Panay par le Japon, en décembre 1937. "
        "{i8.2}Il faut attendre 1939, avec le cash and carry, pour que l'Amérique commence à armer les démocraties. "
        "Plus tard, elle deviendra l'arsenal de la démocratie, avec les chars Sherman de l'arsenal de Detroit. "
        "Au bout du compte, c'est le réarmement, et non le New Deal, qui met fin à la Dépression.",
        "{i8.3}De l'autre côté de l'Atlantique, la réponse, c'est l'apaisement. En 1936, les troupes allemandes entrent en Rhénanie, "
        "avec l'ordre de se replier au premier signe de résistance française. Il n'y en a aucun. "
        "{i8.4}Et l'apaisement laisse les dictateurs aller plus loin. Mussolini prend l'Éthiopie. Puis Hitler prend l'Autriche, "
        "les Sudètes à Munich, Prague… et il envahit la Pologne. "
        "David Low l'avait vu venir dès 1936. Dans Stepping Stones to Glory, Hitler grimpe sur le dos courbé des démocraties.",
        "{-i8}{rais}Alors, pourquoi l'apaisement ? Le cours donne six raisons. Et aucune n'est absurde. {rais.1}Le pacifisme : éviter une nouvelle guerre mondiale. "
        "{rais.2}Le Royaume-Uni doit tenir son empire, et n'a pas les moyens de réarmer en grand. {rais.3}Beaucoup de Britanniques pensent que l'Allemagne "
        "a été traitée injustement à Versailles. {rais.4}Leurs propres difficultés économiques passent d'abord. {rais.5}L'isolationnisme américain les laisse seuls. "
        "{rais.6}Et ils craignent le communisme plus que le fascisme.",
        "{-rais}{axe}Pendant ce temps, les dictatures se rapprochent. L'axe Rome-Berlin date de 1936. "
        "Mais les trois puissances ne signent leur alliance en bonne et due forme, le pacte tripartite, "
        "qu'en septembre 1940, une fois la guerre commencée.",
    ], vis={
        "i7": dict(type="liste", titre="II.3 · L'ordre libéral sans défenseurs (1)", items=[
            "Wilsonisme : les États-Unis, clé de voûte absente (Punch, 1919)", "Une SDN faible : pas d'armée, un veto chacun · Le Paillasson (1933)",
            "Mandchourie 1931–33 : Lytton condamne, le Japon s'en va", "Note Stimson (7 janv. 1932) : des mots, puis Shanghai bombardée"],
            x=130, y=125, w=1020),
        "i8": dict(type="liste", titre="II.3 · L'ordre libéral sans défenseurs (2)", items=[
            "Lois de neutralité 1935–37 : même après l'USS Panay", "Cash and carry (1939), puis l'arsenal de la démocratie",
            "L'apaisement : la Rhénanie, 7 mars 1936", "Conséquences : Munich (sept. 1938) → Pologne (1er sept. 1939)"],
            x=130, y=125, w=1020),
        "rais": dict(type="liste", titre="Six raisons de l'apaisement", items=[
            "Le pacifisme : éviter une nouvelle guerre mondiale", "Un empire à tenir, pas d'argent pour réarmer", "L'Allemagne traitée injustement à Versailles ?",
            "Leurs propres difficultés économiques d'abord", "L'isolationnisme américain : aucune protection", "Le communisme plus craint que le fascisme"],
            x=150, y=105, w=980),
        "axe": dict(type="note", terme="L'Axe", cles=["1936", "tripartite"],
                    t="Axe Rome–Berlin : 1936.",
                    etape="Pacte tripartite (Allemagne, Italie, Japon) : septembre 1940, après la Pologne.", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. personnes et chiffres
    dict(id="gens", chap="Personnages et chiffres", fond="nuit", humeur="calme",
         retenir="Roosevelt · Hoover · Dawes · Smoot et Hawley · Lange · Wilson · Stimson · Hitler · Blum · Chamberlain et Daladier. ×3 · −89 % · 14 millions · −66 % · 43,8 %.",
         beats=[
        "{pe}Maintenant, les noms à connaître. {pe.1}Roosevelt, et le New Deal. {pe.2}Hoover, qui a donné son nom aux bidonvilles. "
        "{pe.3}Charles Dawes, et son plan. {pe.4}Smoot et Hawley, et leur tarif. {pe.5}Dorothea Lange, la photographe. "
        "{pe.6}Et Florence Owens Thompson, le visage de Migrant Mother. {pe.7}Wilson, et les Quatorze Points. "
        "{pe.8}Stimson, et sa note. {pe.9}Hitler, chancelier sans majorité. {pe.10}Léon Blum, et le Front populaire. "
        "{pe.11}Chamberlain et Daladier, à Munich. {pe.12}Et David Low, le caricaturiste.",
        "{-pe}{chf}Et sept chiffres. {chf.1}Fois trois : la Bourse, de 1924 à 1929. "
        "{chf.2}Moins quatre-vingt-neuf pour cent : la chute du Dow Jones, jusqu'en 1932. "
        "{chf.3}Quatorze millions : les chômeurs américains. Un quart des travailleurs. "
        "{chf.4}Vingt mille : les produits taxés par Smoot-Hawley. {chf.5}Moins deux tiers : le commerce mondial, de 1929 à 1934. "
        "{chf.6}Quarante-trois virgule huit pour cent : le chômage allemand en 1932. "
        "{chf.7}Et dix pour cent : le tarif général britannique, en 1932 lui aussi.",
    ], vis={
        "pe": dict(type="nuage", items=["Roosevelt", "Hoover", "Dawes", "Smoot & Hawley", "Dorothea Lange", "F. Owens Thompson",
                                        "Wilson", "Stimson", "Hitler", "Léon Blum", "Chamberlain & Daladier", "David Low"]),
        "chf": dict(type="liste", titre="Sept chiffres", items=[
            "×3 · la Bourse, 1924–1929", "−89 % · le Dow Jones, 1929–1932", "14 millions de chômeurs · 25 % des actifs américains",
            "20 000 produits · Smoot–Hawley", "−66 % · le commerce mondial, 1929–1934",
            "43,8 % · chômage allemand, 1932", "10 % · le tarif britannique, 1932"], x=170, y=95, w=940),
    }),

    # ================================================================ IX. à toi
    dict(id="atoi", chap="À toi", fond="nuit", humeur="calme",
         retenir="24 oct. 1929 · 17 juin 1930 · 18 sept. 1931 · janv. 1933 · sept. 1938.",
         beats=[
        "{pa}À toi. Sans regarder en arrière. Donne cinq dates clés du chapitre, et dis ce qui s'est passé, en une ligne chacune.",
        ("P", 2.0),
        "{-pa}{rep}Voici une réponse possible. {rep.1}Le vingt-quatre octobre 1929 : le jeudi noir. Le krach commence. "
        "{rep.2}Le dix-sept juin 1930 : le tarif Smoot-Hawley. {rep.3}Le dix-huit septembre 1931 : "
        "l'incident de Mukden. Le Japon envahit la Mandchourie. {rep.4}Janvier 1933 : Hitler est nommé chancelier. "
        "{rep.5}Et septembre 1938 : Munich. L'acte qui définit l'apaisement.",
    ], vis={
        "pa": dict(type="pause", t="Cinq dates clés du chapitre, avec ce qui s'est passé.",
                   sous="Mets la vidéo en pause, écris-les, puis relance pour comparer."),
        "rep": dict(type="liste", titre="Une réponse modèle", items=[
            "24 oct. 1929 · jeudi noir : le krach commence", "17 juin 1930 · le tarif Smoot–Hawley",
            "18 sept. 1931 · Mukden : le Japon envahit la Mandchourie", "Janv. 1933 · Hitler nommé chancelier",
            "Sept. 1938 · Munich : l'acte qui définit l'apaisement"], x=170, y=130, w=940),
    }),

    # ================================================================ X. l'épreuve
    dict(id="examen", chap="Notions clés et problématiques", fond="nuit", humeur="lumiere",
         retenir="Notions clés : la dépression économique mondiale · l'apaisement. Problématiques : la part de responsabilité des démocraties · le nationalisme économique, facteur décisif ?",
         beats=[
        "{kt}Maintenant, l'épreuve. Il y a deux notions clés. D'abord, la dépression économique mondiale des années 1930. "
        "C'est une baisse longue et générale de la production, avec un chômage de masse et une forte déflation. "
        "Ensuite, l'apaisement. Céder aux exigences d'un agresseur, dans l'espoir d'éviter la guerre.",
        "{-kt}{ki1}Il y a aussi deux problématiques, et l'une comme l'autre peut tomber. Voici la première. "
        "La responsabilité des origines de la Seconde Guerre mondiale incombe en partie aux grandes démocraties elles-mêmes. Dans quelle mesure es-tu d'accord ?",
        "{-ki1}{pl1}Voici un plan en trois parties. {pl1.1}Un. Les démocraties ont bâti un ordre qu'elles refusaient de garantir, et après 1929, "
        "elles l'ont affaibli. Le Sénat américain refuse Versailles. Smoot-Hawley, et les représailles qui suivent, réduisent le commerce mondial des deux tiers. "
        "{pl1.2}Deux. Quand l'ordre est mis à l'épreuve, elles refusent de le défendre. La Mandchourie. Les lois de neutralité. Pas d'embargo sur le pétrole contre l'Italie. "
        "La Rhénanie. Munich. "
        "{pl1.3}Trois. Mais l'initiative revient aux régimes militaristes, à Berlin, à Rome et à Tokyo. "
        "{pl1.4}Donc, d'accord en partie. Et reprends le mot du cours : réticentes. Elles pouvaient agir, et elles ont choisi de ne pas le faire.",
        "{-pl1}{ki2}Maintenant, la deuxième problématique. Dans quelle mesure le nationalisme économique a-t-il été le facteur décisif du glissement vers la guerre en 1939 ?",
        "{-ki2}{pl2}Là encore, trois parties. {pl2.1}Un. Le nationalisme économique ronge l'ordre international. Droits de douane, quotas, "
        "blocs impériaux. Et l'autarcie fait paraître la conquête rationnelle. {pl2.2}Deux. Mais c'est un symptôme autant qu'une cause. "
        "La chaîne commence à Wall Street, pas aux douanes. {pl2.3}Trois. L'idéologie lui dispute la première place. "
        "Le militarisme, dans trois régimes. Et le pillage nazi, qu'aucune barrière douanière ne peut expliquer. "
        "{pl2.4}Ta conclusion : les facteurs économiques ont créé l'occasion. L'idéologie a fourni l'intention.",
    ], vis={
        "kt": dict(type="cols", g="La dépression économique mondiale", gq="une baisse longue et générale de la production : chômage de masse, forte déflation",
                   d="L'apaisement", dq="céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre", vs="+"),
        "ki1": dict(type="question", t="Problématique 1 · La part des démocraties dans les origines de la guerre : dans quelle mesure es-tu d'accord ?"),
        "pl1": dict(type="liste", titre="Problématique 1 · un plan en trois parties", items=[
            "I. Un ordre qu'elles refusaient de garantir, puis affaibli (Versailles refusé, Smoot–Hawley)",
            "II. Elles refusent de le défendre : Mandchourie, lois de neutralité, Rhénanie, Munich",
            "III. Mais l'initiative revient à Berlin, Rome et Tokyo",
            "D'accord en partie : « réticentes » — elles pouvaient agir, et ont choisi de ne pas le faire"], x=130, y=120, w=1020),
        "ki2": dict(type="question", t="Problématique 2 · Le nationalisme économique, facteur décisif du glissement vers la guerre ?"),
        "pl2": dict(type="liste", titre="Problématique 2 · un plan en trois parties", items=[
            "I. Il ronge l'ordre : droits de douane, quotas, blocs, autarcie",
            "II. Un symptôme autant qu'une cause : la chaîne part de Wall Street",
            "III. L'idéologie lui dispute la place : militarisme, pillage nazi",
            "L'économie a donné l'occasion ; l'idéologie, l'intention"], x=130, y=120, w=1020),
    }),

    # ================================================================ XI. vers le chapitre 2
    dict(id="suite", chap="Vers le chapitre 2", fond="nuit", humeur="tension",
         retenir="Mars 1939 Prague · 1er sept. 1939 Pologne · nov. 1939 cash and carry. Chapitre 2 : les régimes totalitaires.",
         beats=[
        "{g3}{g3.1}Et maintenant, la fin de l'histoire. En mars 1939, l'Allemagne occupe Prague. Munich n'a rien acheté. "
        "Le premier septembre, l'Allemagne envahit la Pologne. La France et le Royaume-Uni déclarent la guerre. "
        "{g3.2}En novembre arrive le cash and carry. Les États-Unis commencent à ravitailler les démocraties.",
        "{-g3}{g4}{g4.1}Le chapitre deux reprend exactement ici. Il étudie les régimes totalitaires, dont les démocraties réticentes "
        "n'ont pas su contenir le militarisme. Trois régimes, une trajectoire. {g4.2}Et une date relie les deux chapitres. Le trente janvier 1933 : "
        "Hitler est nommé chancelier, au plus profond de la Dépression.",
        "{-g4}",
    ], vis={
        "g3": dict(type="globe", code="H1", sc=[31, 32]),
        "g4": dict(type="globe", code="H2", sc=[0, 20]),
    }),

    # ================================================================ récap final
    dict(id="fin", chap="Tout le chapitre", fond="nuit", humeur="calme", beats=[
        "{carte}Une dernière carte de tout le chapitre. {carte.1}Le krach : la spéculation, puis la panique, en octobre 1929. "
        "{carte.2}La crise mondiale : les banques, les prêts, l'or… et quatorze millions de chômeurs, les Hoovervilles, le Dust Bowl. "
        "{carte.3}Le nationalisme économique : Smoot-Hawley, et les blocs impériaux. "
        "{carte.4}Les réponses politiques : Hitler, le New Deal, le Front populaire. {carte.5}Et l'ordre libéral, laissé sans défense. "
        "La SDN. La neutralité. L'apaisement.",
        ("P", 5.0),
        "{-carte}{fin}Et c'est la fin de la série sur le chapitre un. Maintenant, fais le quiz. Puis, place au chapitre deux.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LE KRACH ET SES CONSÉQUENCES", branches=[
            dict(t="Le krach", items=["spéculation · achat à crédit", "24–29 oct. 1929 · −89 %"]),
            dict(t="Une crise mondiale", items=["banques · prêts · or", "14 millions de chômeurs · Dust Bowl"]),
            dict(t="Nationalisme économique", items=["Smoot–Hawley (1930)", "blocs impériaux · commerce −66 %"]),
            dict(t="Réponses politiques", items=["Hitler · militarisme", "New Deal · Front populaire"]),
            dict(t="L'ordre sans défense", items=["SDN · lois de neutralité", "apaisement · Munich"])]),
        "fin": dict(type="mot", t="Suite : le chapitre 2", g="H2 · Les régimes totalitaires", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="Combien le plan Dawes prête-t-il à l'Allemagne en 1924 ?", r=["800 millions de marks", "2,5 milliards de marks par an",
         "20 millions de Reichsmarks par jour", "14 millions de dollars"], ok=0, voir="g1",
         ex="L'argent américain au début de la chaîne : les réparations, puis les dettes de guerre qui reviennent à Washington."),
    dict(q="Selon le cours, quand la Grande Dépression commence-t-elle vraiment ?", r=["Quand de nombreuses banques font faillite",
         "Le jeudi noir", "Quand Hitler arrive au pouvoir", "Avec le Dust Bowl"], ok=0, voir="ch",
         ex="Pas de garantie des dépôts avant 1933 : environ 5 000 banques ont fait faillite en 1932."),
    dict(q="De combien le Dow Jones chute-t-il entre septembre 1929 et juillet 1932 ?", r=["−89 %", "−40 %", "−25 %", "−66 %"],
         ok=0, voir="dj", ex="De 381 à 41 ; −66 %, c'est le commerce mondial, 1929–1934."),
    dict(q="Quel facteur est le mieux décrit comme le déclencheur du krach ?", r=["La spéculation", "Le Dust Bowl", "Les lois de neutralité",
         "L'étalon-or"], ok=0, voir="fac",
         ex="La spéculation explique la soudaineté ; la surproduction et les inégalités, la profondeur."),
    dict(q="Dans quel ordre les dominos tombent-ils en 1931 ?", r=["Creditanstalt → banques allemandes → Royaume-Uni hors de l'or",
         "Royaume-Uni hors de l'or → Creditanstalt → banques allemandes", "Banques allemandes → France → Creditanstalt", "France → Royaume-Uni → Allemagne"],
         ok=0, voir="i2", ex="Mai, juillet, septembre 1931."),
    dict(q="Qui est la femme de Migrant Mother, la photographie de Dorothea Lange (1936) ?", r=["Florence Owens Thompson", "Melita Maschmann",
         "Eleanor Roosevelt", "Une actrice payée par le gouvernement"], ok=0, voir="i3",
         ex="32 ans, dans un camp de cueilleurs de pois à Nipomo, en Californie."),
    dict(q="Que fait le tarif Smoot–Hawley (17 juin 1930) ?", r=["Il relève les droits sur plus de 20 000 produits importés",
         "Il garantit les dépôts bancaires", "Il fait sortir les États-Unis de l'or", "Il prête de l'argent à l'Allemagne"], ok=0, voir="i4",
         ex="Le Canada avait déjà riposté en mai 1930 ; le commerce mondial a perdu deux tiers de sa valeur."),
    dict(q="Chômage allemand chez les travailleurs assurés en 1932 (étude de cas) ?", r=["43,8 %", "8,6 %", "25 %", "37,3 %"], ok=0,
         voir="gr", ex="37,3 %, c'est le vote nazi en juillet 1932 ; 25 %, le chômage américain en 1933."),
    dict(q="Laquelle n'est PAS l'une des six raisons de l'apaisement ?", r=["La peur d'une invasion japonaise du Royaume-Uni",
         "Le pacifisme", "La peur du communisme plus que du fascisme", "Leurs propres difficultés économiques"], ok=0, voir="rais",
         ex="Aussi : un empire à tenir, l'Allemagne traitée injustement, l'isolationnisme américain."),
    dict(q="Qu'est-ce que l'apaisement ?", r=["Céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre",
         "Refuser de commercer avec les dictatures", "Une alliance contre l'Allemagne", "La politique de neutralité américaine"], ok=0,
         voir="kt", ex="Une notion clé du chapitre ; son acte emblématique est Munich, septembre 1938."),
]

CREDITS = [
    "Contenu : la synthèse du cours d'histoire de Terminale, chapitre 1, « Le krach de Wall Street et son impact », telle que le site la rédige : "
    "frise, enchaînement de la crise, idées des parties I.1 à II.3, chiffres clés, notions clés et problématiques, étude de cas sur l'Allemagne ; "
    "cartes animées des chapitres 1 et 2 (site).",
    "Photographies : foule devant la Bourse de New York, octobre 1929 (Wikimedia Commons, domaine public) ; "
    "Hooverville sur le front de mer de Seattle, 1933 (Seattle Municipal Archives, via Wikimedia Commons, CC BY 2.0) ; "
    "Dorothea Lange, Migrant Mother, 1936 (Library of Congress, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
