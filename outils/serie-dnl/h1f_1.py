"""Histoire · chapitre 1 « Le krach de 1929 et ses conséquences » — édition française, épisode 1 : « Le grand krach de 1929 ».

Traduction et adaptation de h1_1.py (édition anglaise, gardée intacte), selon outils/serie-dnl/EDITION_FR.md :
mêmes scènes, mêmes identifiants de visuels, mêmes repères, mêmes globes (la carte animée passe d'elle-même en français),
mêmes graphes et données, mêmes images (légendes traduites). Aucune mention de la DNL : histoire-géographie de Terminale.
Vocabulaire repris des champs français du cours (dnl/index.html, CHAPTERS.H1, partie I.1 « Qu'est-ce que le krach de 1929 ? »).
Chaîne : outils/serie-philo/generer.py h1f_1 ; sortie dans dnl/serie/.
Type globe, sc = numéros de scènes de la carte H1 dans l'ordre chronologique :
  0 ordre libéral de 1919 · 1 Roaring Twenties · 2 l'économie réelle ralentit · 3 plan Dawes · 4 spéculation · 5 krach
Courbe du Dow Jones : 100 (1924), 381 (septembre 1929), 41 (juillet 1932) sont les chiffres du cours ; les points
intermédiaires sont des valeurs approchées de l'indice (hors cours), comme dans l'animation du site.
Plan de la série : 1 Le grand krach de 1929 · 2 D'un krach américain à une crise mondiale ·
3 Nationalisme économique et réponses politiques · 4 Les démocraties et l'ordre libéral ·
5 La crise à l'épreuve : question problématisée et analyse de document · 6 Récap.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-1"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 1
TITRE = "Le grand krach de 1929"
SUIVANT = "Épisode 2 · D'un krach américain à une crise mondiale"
PRONONCIATION = {
    "Wall Street": "Wol-Strite",
    "Dow Jones": "Dao-Djonze",
    "Jay Winter": "Djé Ouinteur",
    "Coolidge": "Coulidje",
    "Hoover": "Houveur",
    "Dawes": "Dôze",
    "Carnegie": "Carnégui",
    "Standard Oil": "Standarde-Oïl",
    "US Steel": "U. S. Stil",
    "RCA": "R. C. A.",
    "Radio Corporation of America": "Radio Corporécheunne ov Amérika",
    "Roaring Twenties": "Rôring Touènntize",
    "Gatsby": "Gatsbi",
}

# indice Dow Jones (repères du cours : 100, 381, 41 ; points intermédiaires approchés, hors cours)
DOW_MONTEE = [[1924.0, 100], [1925.0, 122], [1926.0, 157], [1927.0, 155], [1928.0, 200], [1929.0, 300], [1929.67, 381]]
DOW_CHUTE = [[1929.67, 381], [1929.87, 198], [1930.3, 294], [1931.0, 165], [1932.0, 75], [1932.5, 41]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{ph1}Mille neuf cent vingt-neuf. Deux photographies ouvrent ce chapitre. La première : une foule, silencieuse, grave, "
        "massée dans la rue devant la Bourse de New York. Des milliers de gens qui attendent des nouvelles… de leur argent.",
        "{-ph1}{ph1b}{ph2}La seconde, la même année, en Allemagne : Adolf Hitler salue ses partisans au congrès du parti nazi, à Nuremberg. "
        "En vingt-neuf, son parti est encore petit. Dix ans plus tard, il plonge l'Europe dans la guerre.",
        "{-ph2}{q2}Voici donc la question sur laquelle les historiens débattent encore. Qu'est-ce qui a causé la Seconde Guerre mondiale ? "
        "La crise du capitalisme qui suit le krach ? La menace totalitaire ? {!Ou les deux}Ou les deux ?",
        "{-q2}{-ph1b}{winter}L'historien Jay Winter donne une réponse audacieuse. Pour lui, il n'y a eu qu'une seule guerre, "
        "une {!guerre de trente ans}guerre de trente ans, de mille neuf cent quatorze à mille neuf cent quarante-cinq. Pourquoi ? Parce qu'entre les deux, "
        "la paix n'a jamais vraiment été établie. Les canons se taisent en dix-huit… mais le conflit continue, par d'autres moyens.",
        "Cette série suit le premier maillon de cette chaîne, {-winter}{plan}en six épisodes. {plan.1}Aujourd'hui : le grand krach de mille neuf cent vingt-neuf. "
        "Ce que c'est, et pourquoi il se produit. {plan.2}Ensuite, comment un krach américain devient une crise mondiale. "
        "{plan.3}Puis le nationalisme économique, et les réponses politiques à la crise. {plan.4}Puis les démocraties et l'ordre libéral. "
        "{plan.5}Après cela, un épisode rien que pour l'épreuve : la question problématisée et l'analyse de document. {plan.6}Et un récap final.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "ph1": dict(type="tableau", img="h1-wallstreet", de=[1.0, .5, .55], a=[1.08, .48, .53],
                    legende="Foule devant la Bourse de New York, octobre 1929 (Wikimedia Commons, domaine public)"),
        "ph1b": dict(type="tableau", img="h1-wallstreet", fond=True, sombre=True, de=[1.08, .48, .53], a=[1.2, .45, .5],
                     legende="Foule devant la Bourse de New York, octobre 1929 (Wikimedia Commons, domaine public)"),
        "ph2": dict(type="note", terme="La seconde photographie de 1929", cles=["Hitler", "Nuremberg"],
                    t="Adolf Hitler salue ses partisans au congrès du parti nazi, à Nuremberg.",
                    etape="Décrite ici, pas montrée. En 1929, le parti nazi est encore petit.", x=170, y=200, w=940),
        "q2": dict(type="question", t="La crise du capitalisme, le totalitarisme… ou les deux ?", bande=True),
        "winter": dict(type="mot", t="1914 – 1945", g="Jay Winter : une seule « guerre de trente ans » — la paix n'a jamais vraiment été établie",
                       y=250, taille=110),
        "plan": dict(type="liste", titre="Le krach de 1929 et ses conséquences, en six épisodes", items=[
            "Le grand krach de 1929 (partie I.1)", "D'un krach américain à une crise mondiale (I.2–I.3)",
            "Nationalisme économique et réponses politiques (II.1–II.2)", "Les démocraties et l'ordre libéral (II.3)",
            "La crise à l'épreuve : question problématisée et analyse de document", "Récap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Chapitre 1 · Épisode 1", t="Le grand krach de 1929",
                      sous="la Bourse · les années vingt · la spéculation · la panique d'octobre"),
    }),

    # ================================================================ I. le chapitre et l'ordre de 1919
    dict(id="ordre", chap="L'ordre libéral de 1919", fond="nuit", humeur="calme",
         retenir="Le chapitre : comment l'effondrement boursier d'un seul pays devient une dépression mondiale, qui pousse les démocraties au repli tandis que trois régimes choisissent le militarisme.",
         beats=[
        "{g0}{g0.1}Ce chapitre ouvre le thème un, et il vient juste après le règlement de la paix de mille neuf cent dix-neuf. "
        "Alors partons de là. {lib}{lib.1}En mille neuf cent dix-huit, les Quatorze Points du président Wilson portent trois principes : "
        "la démocratie, le droit des peuples à disposer d'eux-mêmes, et le libre-échange.",
        "{lib.2}La conférence de la paix de Paris, le traité de Versailles et la Société des Nations, installée à Genève, leur donnent des institutions. "
        "{lib.3}Mais le Sénat américain refuse de ratifier le traité. Les États-Unis n'entrent jamais dans la Société des Nations que leur propre président avait imaginée.",
        "{lib.4}Voilà l'{!ordre libéral}ordre libéral de dix-neuf. Puis vient la prospérité fragile des années vingt. "
        "Et ce chapitre va montrer à quel point cet ordre était fragile.",
        "{-lib}{-g0}{obj}Quel est donc l'objectif du chapitre ? D'abord, expliquer comment l'effondrement de la Bourse "
        "dans un seul pays devient une dépression mondiale. Ensuite, expliquer pourquoi cette dépression pousse les grandes démocraties au nationalisme économique "
        "et au repli… tandis que trois régimes choisissent le militarisme.",
        "{-obj}{chaine}Vois-le comme une chaîne. {chaine.1}Un effondrement financier américain. "
        "{chaine.2}Il se propage par les prêts, le commerce et les monnaies. {chaine.3}Il devient une dépression mondiale. "
        "{chaine.4}Et au bout de la chaîne, l'ordre libéral bâti en dix-neuf est vaincu. "
        "Aujourd'hui, on regarde le tout premier maillon : le krach lui-même.",
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[0]),
        "lib": dict(type="liste", titre="L'ordre libéral de 1919", x=640, y=290, w=620, petit=True, bande=True,
                    cles=["démocratie", "libre-échange", "jamais"], items=[
                        "Les Quatorze Points de Wilson (1918) : démocratie, droit des peuples, libre-échange",
                        "Versailles et la Société des Nations (Genève)",
                        "Le Sénat américain refuse : les États-Unis n'entrent jamais à la SDN",
                        "Puis la prospérité fragile des années 1920"]),
        "obj": dict(type="def", terme="L'objectif du chapitre", cles=["un seul pays", "dépression mondiale", "militarisme"],
                    t="Expliquer comment l'effondrement boursier d'un seul pays devient une dépression mondiale.",
                    etape="…et pourquoi elle pousse les démocraties au nationalisme économique et au repli, tandis que trois régimes choisissent le militarisme.",
                    x=170, y=200, w=940),
        "chaine": dict(type="liste", titre="La chaîne du chapitre", items=[
            "Un effondrement financier américain", "Propagé par les prêts, le commerce et les monnaies", "Une dépression mondiale",
            "L'ordre libéral de 1919 vaincu"], x=170, y=140, w=940),
    }),

    # ================================================================ II. la chronologie sur la carte
    dict(id="chrono", chap="Le récit sur la carte", fond="nuit", humeur="lumiere",
         retenir="Années 1920 : un boom fondé sur la production de masse et le crédit · dès 1920 : l'agriculture déjà en crise · 1924 : plan Dawes · 1924-1929 : la Bourse triple · 24-29 oct. 1929 : le krach.",
         beats=[
        "{g1}Avant le cours lui-même, racontons l'histoire sur la carte, en cinq étapes. {g1.1}Première étape : les années vingt, "
        "les {!Roaring Twenties}Roaring Twenties, les années rugissantes. Trois présidents républicains se succèdent : Harding, Coolidge, Hoover. "
        "Des impôts bas, des entreprises géantes, une protection contre les produits étrangers.",
        "À Detroit, les usines d'Henry Ford produisent des voitures en série. Voitures, radios, réfrigérateurs entrent dans les foyers ordinaires. "
        "L'Amérique vit un boom fondé sur la production et la consommation de masse. Il paraît permanent.",
        "{g1.2}Deuxième étape. Quittons maintenant les villes, direction les Grandes Plaines. Ici, le boom n'est jamais vraiment arrivé. "
        "Les prix agricoles baissent depuis mille neuf cent vingt. Et le charbon, le textile, le bâtiment sont eux aussi en difficulté.",
        "{fr2}Pourquoi ? {fr2.1}La plupart des Américains sont pauvres : ils ne peuvent pas acheter tout ce que produisent les usines. "
        "{fr2.2}Et les Européens se relèvent encore de la guerre : eux non plus ne peuvent pas acheter. C'est la surproduction.",
        "{-fr2}{g1.3}Troisième étape, mille neuf cent vingt-quatre : le plan Dawes. L'Allemagne reçoit un prêt de huit cents millions de marks, "
        "en grande partie levé aux États-Unis. Avec cet argent, l'Allemagne paie ses réparations à la France et au Royaume-Uni. Et la France et le Royaume-Uni remboursent leurs dettes de guerre aux États-Unis. "
        "Un circuit de l'argent… qui repose entièrement sur le crédit américain. Garde-le en tête : c'est la clé de l'épisode deux.",
        "{g1.4}Quatrième étape, de vingt-quatre à vingt-neuf, à New York. À Wall Street, la Bourse triple en cinq ans. "
        "En mille neuf cent vingt-neuf, environ un ménage américain sur dix possède des actions. On achète des actions non pour les bénéfices, "
        "mais pour les revendre plus cher. Et souvent avec de l'argent emprunté.",
        "{g1.5}Et cinquième étape. Octobre mille neuf cent vingt-neuf. Le jeudi vingt-quatre, les ventes de panique commencent. "
        "Le lundi vingt-huit et le mardi vingt-neuf, la Bourse s'effondre. Tout le monde vend. Personne n'achète. "
        "{!Le krach de Wall Street}C'est le krach de Wall Street.",
        "Cinq étapes : un boom, une faiblesse cachée, un circuit du crédit, une bulle… et la bulle éclate. "
        "Reprenons maintenant chacune, lentement, comme le fait le cours.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[1, 2, 3, 4, 5]),
        "fr2": dict(type="liste", titre="Pourquoi la surproduction ?", x=860, y=250, w=400, petit=True, bande=True, items=[
            "La plupart des Américains sont pauvres : ils ne peuvent pas acheter", "L'Europe se relève encore de la guerre"]),
    }),

    # ================================================================ III. idée 1 : la Bourse
    dict(id="bourse", chap="Qu'est-ce qu'une Bourse ?", fond="nuit", humeur="calme",
         retenir="Une Bourse : les entreprises lèvent des fonds en vendant des actions. Deux récompenses : le dividende (une part des bénéfices) ou la revente plus chère, qui ne dépend que de l'acheteur suivant.",
         beats=[
        "{q3}Première idée du cours. Qu'est-ce qu'une Bourse, exactement ?",
        "{-q3}{def3}Une Bourse, c'est un lieu où les entreprises lèvent des fonds, et où les investisseurs achètent un droit sur leurs bénéfices. "
        "La {!Bourse}Bourse, c'est aussi le bâtiment, l'équipement. Ceux qui y travaillent sont les traders.",
        "Voici comment ça marche. {-def3}{mec}{mec.1}Les grandes entreprises ont besoin d'argent pour grandir : il leur faut des investisseurs. "
        "{mec.2}Alors elles vendent des {!actions}actions, de petits morceaux de l'entreprise. Celui qui en achète une devient actionnaire.",
        "{mec.3}Et un actionnaire est récompensé de deux façons. {mec.4}Première façon : le {!dividende}dividende, une part des bénéfices de l'entreprise, "
        "versée chaque année. {mec.5}Deuxième façon : revendre l'action à quelqu'un d'autre, plus cher qu'on ne l'a payée.",
        "{-mec}{deux}{deux.g}Regarde bien ces deux façons, parce que tout le chapitre commence ici. Le dividende dépend de l'entreprise : "
        "si elle fait des bénéfices, tu es payé. {deux.d}Mais revendre plus cher ne dépend pas du tout de l'entreprise. "
        "Ça dépend seulement de ce que le prochain acheteur est prêt à payer. {!C'est là que les ennuis commencent}C'est là que les ennuis commencent.",
        "{-deux}{rca}Un exemple, dont le cours précise lui-même qu'il vient d'ailleurs : Radio Corporation of America, RCA, "
        "la valeur vedette de la fin des années vingt. RCA ne verse aucun dividende. Aucun. Et pourtant son cours "
        "est multiplié plusieurs fois en vingt-huit et vingt-neuf.",
        "Alors, que payaient les acheteurs ? Pas des bénéfices. Ils payaient ce que paierait l'acheteur suivant. "
        "Retiens-le : c'est la définition d'une bulle.",
    ], vis={
        "q3": dict(type="question", t="Qu'est-ce qu'une Bourse, exactement ?"),
        "def3": dict(type="def", terme="La Bourse", cles=["lèvent des fonds", "bénéfices"],
                     t="Un lieu où les entreprises lèvent des fonds et où les investisseurs achètent un droit sur leurs bénéfices.",
                     etape="La Bourse est aussi un équipement ; ceux qui y travaillent sont les traders.", x=170, y=200, w=940),
        "mec": dict(type="liste", titre="Comment fonctionne une Bourse", cles=["actions", "dividende", "revendre"], items=[
            "Les grandes entreprises ont besoin d'investisseurs", "Elles vendent des actions : l'acheteur devient actionnaire",
            "Deux récompenses pour l'actionnaire :", "Première : le dividende, une part des bénéfices versée chaque année",
            "Seconde : revendre l'action à quelqu'un d'autre plus cher qu'elle n'a coûté"], x=170, y=110, w=940),
        "deux": dict(type="cols", g="Le dividende", gq="dépend de l'entreprise : de ses bénéfices", d="Revendre plus cher",
                     dq="ne dépend que de l'acheteur suivant : les ennuis commencent ici", vs="≠"),
        "rca": dict(type="note", terme="Exemple · RCA (hors cours)", cles=["aucun dividende", "plusieurs fois"],
                    t="Radio Corporation of America ne verse aucun dividende, et pourtant son cours est multiplié plusieurs fois en 1928-1929.",
                    etape="Les acheteurs paient ce que paiera l'acheteur suivant, non des bénéfices.", x=170, y=200, w=940),
    }),

    # ================================================================ IV. idée 2 : les Roaring Twenties
    dict(id="twenties", chap="Les années vingt", fond="aube", humeur="lumiere",
         retenir="La politique républicaine (Harding, Coolidge, Hoover) : impôts bas, trusts, droits de douane ; s'y ajoutent le crédit et le marketing, et d'immenses ressources. Un boom qui paraît permanent : 8 → 23 millions de voitures, 1920-1929.",
         beats=[
        "{mt}Deuxième idée. Les {!années vingt}années vingt : croissance, optimisme et opulence… sur fond de politique républicaine.",
        "Trois présidents républicains d'affilée : Harding, Coolidge, puis Hoover. {rep}Leur politique repose sur trois piliers. "
        "{rep.1}Un : ils maintiennent une fiscalité basse. "
        "{rep.2}Deux : ils laissent se développer les {!trusts}trusts, de gigantesques concentrations d'entreprises. "
        "{rep.3}Trois : ils protègent l'industrie américaine par des droits de douane, des taxes sur les produits importés.",
        "{rep.4}La décennie y ajoute de nouvelles techniques : de nouvelles façons de vendre, de faire crédit, de faire de la publicité. "
        "Avec la {!vente à tempérament}vente à tempérament, une famille peut acheter une voiture ou un réfrigérateur avant de pouvoir se l'offrir, et payer mois par mois. "
        "{rep.5}Et l'Amérique dispose de ressources naturelles et de matières premières immenses.",
        "{-rep}{-mt}Résultat : un boom qui paraît permanent. {voit}C'est dans l'automobile qu'il se voit le mieux. "
        "{voit.1}En mille neuf cent vingt, environ huit millions de voitures sont immatriculées aux États-Unis. "
        "{voit.2}En mille neuf cent vingt-neuf, environ vingt-trois millions. Presque trois fois plus, en neuf ans. "
        "Et la plupart sont achetées à crédit. Ces chiffres viennent d'en dehors du cours, mais ce sont l'image la plus claire du boom.",
        "{-voit}{gat}Et si tu veux un roman : Gatsby le Magnifique, publié en mille neuf cent vingt-cinq, est le portrait littéraire de la décennie. "
        "Des fêtes, des voitures, de l'argent… et personne ne se demande d'où tout cela vient.",
    ], vis={
        "mt": dict(type="tableau", img="h1-modelt", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .55, .55],
                   legende="Ford T torpédo de 1925, restaurée (ModelTMitch, Wikimedia Commons, CC BY-SA 4.0)"),
        "rep": dict(type="liste", titre="Pourquoi le boom ? La politique républicaine, et plus encore", cles=["fiscalité", "trusts", "douane", "crédit"], items=[
            "Une fiscalité basse", "Les trusts autorisés : de gigantesques concentrations d'entreprises", "Des droits de douane qui protègent l'industrie",
            "Vente, crédit et marketing nouveaux : la vente à tempérament", "D'immenses ressources naturelles et matières premières"], x=170, y=110, w=940),
        "voit": dict(type="graphe", titre="Voitures immatriculées aux États-Unis (hors cours)", x=300, y=110, w=680, h=520,
                     ax=dict(x=[1919, 1930], y=[0, 26], gx=[1920, 1925, 1929], gy=[5, 10, 15, 20, 25], lx="année", ly="millions de voitures"),
                     el=[dict(type="point", x=1920, y=8, c="el", lbl="1920 : ≈ 8 millions", lp=[1920.4, 10.5]),
                         dict(type="droite", pts=[[1920, 8], [1929, 23]], c="sa", lbl="1929 : ≈ 23 millions", lp=[1925.6, 24.5], dur=1.6)]),
        "gat": dict(type="mot", t="Gatsby le Magnifique", g="F. Scott Fitzgerald, 1925 · le portrait de la décennie", y=260, taille=92),
    }),

    # ================================================================ V. idée 3 : production et consommation de masse
    dict(id="masse", chap="Production de masse, consommation de masse", fond="nuit", humeur="lumiere",
         retenir="Le travail à la chaîne abaisse les coûts : voitures, radios, réfrigérateurs entrent dans les foyers ordinaires (Ford T ≈ 260 $ en 1925). Trusts et monopoles, sur le modèle de la Standard Oil et de l'acier de Carnegie, donnent au boom une solidité trompeuse.",
         beats=[
        "{chn}Troisième idée. La {!production de masse}production de masse rend possible la consommation de masse… et concentre le pouvoir économique.",
        "Regarde cette photographie : une chaîne de montage Ford. Le produit défile devant les ouvriers ; chaque ouvrier répète une seule tâche simple. "
        "Le travail à la chaîne abaisse tellement le coût des produits manufacturés que les classes moyennes peuvent désormais les acheter.",
        "{-chn}{bien}{bien.1}Les voitures. {bien.2}Les radios. {bien.3}Les aspirateurs. {bien.4}Les réfrigérateurs. {bien.5}Les machines à laver. "
        "Pour la première fois, ils entrent dans les foyers ordinaires. Les biens de consommation sont produits en masse, et massivement disponibles.",
        "{-bien}{fordt}L'exemple principal : la Ford T. En mille neuf cent vingt-cinq, son prix est tombé à environ "
        "{!deux cent soixante dollars}deux cent soixante dollars. À la portée d'une famille de classe moyenne.",
        "Mais la production de masse a une seconde face. {-fordt}{trust}Les industries se concentrent en {!trusts}trusts et en monopoles. "
        "Des trusts plus anciens ont donné le modèle. {trust.1}La Standard Oil de Rockefeller contrôle tout le pétrole, du puits jusqu'à la pompe, "
        "jusqu'à son démantèlement en mille neuf cent onze. "
        "{trust.2}Et Carnegie fait de même pour l'acier, avant de vendre ses aciéries pour former US Steel, en mille neuf cent un. "
        "{trust.3}Dans les années vingt, des géants comme US Steel et General Motors sont assez puissants pour fixer leurs propres prix.",
        "{trust.4}Et c'est là le piège. Des firmes géantes, des ventes qui montent, des bénéfices qui montent : le boom paraît bien plus solide qu'il ne l'est. "
        "Ce faux sentiment de sécurité, c'est exactement ce qui nourrit l'idée suivante : la spéculation.",
    ], vis={
        "chn": dict(type="tableau", img="h1-assembly", de=[1.0, .5, .5], a=[1.2, .55, .5],
                    legende="Chaîne de montage Ford, Highland Park, Michigan, 1913 (Wikimedia Commons, domaine public)"),
        "bien": dict(type="liste", titre="Les biens de consommation entrent dans les foyers", items=[
            "Les voitures", "Les radios", "Les aspirateurs", "Les réfrigérateurs", "Les machines à laver"], x=170, y=110, w=940),
        "fordt": dict(type="mot", t="≈ 260 $", g="le prix d'une Ford T en 1925 : à la portée d'une famille de classe moyenne", y=250, taille=120),
        "trust": dict(type="liste", titre="L'autre face : trusts et monopoles", cles=["Standard Oil", "Carnegie", "prix", "solide"], items=[
            "La Standard Oil de Rockefeller : du puits à la pompe (démantelée en 1911)", "Carnegie : de même pour l'acier (US Steel en 1901)",
            "Années 1920 : US Steel, General Motors fixent leurs prix", "Le boom paraît plus solide qu'il ne l'est"], x=170, y=130, w=940),
    }),

    # ================================================================ VI. idée 4 : la spéculation (schéma h1speculation)
    dict(id="specu", chap="La spéculation : la bulle", fond="nuit", humeur="tension",
         retenir="Spéculer : acheter pour revendre plus cher, souvent à crédit. La Bourse triple de 1924 à 1929 ; 10 % des ménages ont des actions ; les courtiers prêtent jusqu'à 90 % : une baisse de 10 % ruine l'acheteur.",
         beats=[
        "{def4}Quatrième idée, le cœur de l'épisode. La {!spéculation}spéculation. Qu'est-ce que ça veut dire, spéculer ? "
        "C'est traiter la Bourse comme un moyen facile de s'enrichir, vite. On achète une action non pour le dividende… mais pour la revendre plus cher.",
        "C'est une tendance nouvelle dans les années vingt, et elle se répand vite. {-def4}{bul}Regarde le Dow Jones, l'indice des grandes actions américaines. "
        "{bul.1}En mille neuf cent vingt-quatre, il est à environ cent. On achète encore les actions pour leurs dividendes. "
        "{bul.2}Puis les cours montent plus vite que les bénéfices. Entre vingt-quatre et vingt-neuf, la Bourse {!triple}triple en cinq ans.",
        "{bul.3}En mille neuf cent vingt-neuf, environ dix pour cent des ménages américains possèdent des actions, et la demande d'actions est à son plus haut. "
        "En septembre vingt-neuf, l'indice atteint trois cent quatre-vingt-un. La bulle est à son maximum.",
        "Pourquoi personne ne s'arrête ? Parce que les cours n'ont jamais fait que monter. Alors acheter à crédit paraît parfaitement rationnel. "
        "{-bul}{cred}{cred.1}Emprunter. {cred.2}Acheter. {cred.3}Revendre plus cher. {cred.4}Rembourser, et garder la différence. Ça marche… tant que les cours montent.",
        "Voici l'exemple du cours. Les courtiers prêtent à leurs clients jusqu'à quatre-vingt-dix pour cent du prix d'une action. "
        "C'est ce qu'on appelle l'{!achat sur marge}achat sur marge. Faisons le calcul. {-cred}{marg}{marg.1}Une action coûte cent dollars. "
        "{marg.2}Tu paies dix dollars ; le courtier t'en prête quatre-vingt-dix.",
        "{marg.3}Maintenant, la Bourse baisse de dix pour cent seulement. Ton action vaut quatre-vingt-dix dollars. "
        "{marg.4}Tu dois toujours quatre-vingt-dix dollars au courtier. Tes dix dollars ont disparu. Avec une baisse de dix pour cent seulement, tu es {!ruiné}ruiné.",
        "{-marg}{fin4}Et voilà pourquoi une baisse modérée devient une débandade. Dès que les cours cessent de monter, l'argent emprunté reste à rembourser… "
        "avec des actions qui valent moins. Alors il faut vendre. Et quand on vend, les cours baissent encore.",
    ], vis={
        "def4": dict(type="def", terme="La spéculation", cles=["revendre", "plus cher"],
                     t="Acheter un bien dans l'espoir de le revendre plus cher, plutôt que pour le revenu qu'il rapporte.",
                     etape="Une tendance nouvelle des années 1920, souvent financée à crédit.", x=170, y=200, w=940),
        "bul": dict(type="graphe", titre="La bulle · indice Dow Jones, 1924-1929", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1923.6, 1930.2], y=[0, 420], gx=[1924, 1925, 1926, 1927, 1928, 1929], gy=[100, 200, 300, 400],
                            lx="année", ly="indice"),
                    el=[dict(type="point", x=1924, y=100, c="el", lbl="1924 : ≈ 100", lp=[1924.2, 130]),
                        dict(type="courbe", pts=DOW_MONTEE, c="sa", dur=3.0),
                        dict(type="point", x=1929.67, y=381, c="ca", lbl="sept. 1929 : 381", lp=[1928.6, 405])]),
        "cred": dict(type="liste", titre="Acheter à crédit : un cercle", items=["Emprunter", "Acheter des actions", "Revendre plus cher", "Rembourser, garder le gain"],
                     x=170, y=130, w=940),
        "marg": dict(type="formule", titre="L'achat sur marge : l'exemple du cours", lignes=[
            dict(f="Une action coûte 100 $", n="le prix"),
            dict(f="Tu paies 10 $ · le courtier prête 90 $", n="jusqu'à 90 % prêtés"),
            dict(f="La Bourse baisse de 10 % → l'action vaut 90 $", n="une baisse modérée"),
            dict(f="Tu dois 90 $ : tes 10 $ ont disparu", n="ruiné", cadre=True)]),
        "fin4": dict(type="mot", t="Une baisse → une débandade", g="l'argent emprunté se rembourse avec des actions qui valent moins", y=260, taille=86),
    }),

    # ================================================================ VII. idée 5 : l'économie réelle
    dict(id="reelle", chap="L'économie réelle ralentissait déjà", fond="nuit", humeur="mystere",
         retenir="Avant le krach, l'agriculture, le charbon, le textile et le bâtiment sont en difficulté : surproduction, car la plupart des Américains sont pauvres et l'Europe se relève encore. Les prix agricoles baissent depuis 1920.",
         beats=[
        "{g2}Cinquième idée, et c'est celle que les élèves oublient. {!Pendant ce temps}Pendant ce temps, l'économie réelle avait déjà entamé son déclin.",
        "Le cours le montre en un seul schéma. {sec}Avant le krach, plusieurs secteurs sont déjà en difficulté. "
        "{sec.1}L'agriculture. {sec.2}Le charbon. {sec.3}Le textile, et les autres industries traditionnelles. {sec.4}Et le bâtiment.",
        "{-sec}{-g2}{para0}Pourquoi ? Parce que les biens de consommation sont massivement disponibles… plus que le marché ne peut en absorber. "
        "C'est la surproduction, et la surproduction mène à la récession. {-para0}{surp}{surp.g}Deux faits l'expliquent. "
        "D'abord, la majorité des Américains sont pauvres : ils ne peuvent pas acheter ce que produisent les usines. "
        "{surp.d}Ensuite, les Européens se relèvent encore de la Première Guerre mondiale : eux non plus ne peuvent pas acheter.",
        "L'exemple principal, c'est l'agriculteur. Pendant la guerre, les fermiers américains se sont endettés pour se mécaniser, "
        "pour nourrir l'Europe. Puis la paix est venue. {-surp}{ferme}{ferme.1}Les prix ont baissé. {ferme.2}Les dettes, non. "
        "{ferme.3}Les prix agricoles baissent depuis mille neuf cent vingt. La crise rurale a {!neuf ans de plus}neuf ans de plus que le krach.",
        "{-ferme}{para}Voici donc le paradoxe à retenir. {para.g}La Bourse monte tout au long de mille neuf cent vingt-neuf… "
        "{para.d}sur une économie qui rétrécit déjà. Les cours des actions et l'économie réelle se sont séparés. Tôt ou tard, ils doivent se rejoindre.",
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[2], dt=1.5),
        "sec": dict(type="liste", titre="Déjà en difficulté avant le krach", x=860, y=250, w=400, petit=True, bande=True, items=[
            "L'agriculture", "Le charbon", "Le textile, les industries traditionnelles", "Le bâtiment"]),
        "para0": dict(type="mot", t="Surproduction", g="plus de biens que le marché ne peut en absorber → récession", y=260, taille=96),
        "surp": dict(type="cols", g="La plupart des Américains sont pauvres", gq="ils ne peuvent pas acheter ce que produisent les usines", d="L'Europe se relève",
                     dq="de la Première Guerre mondiale : elle ne peut pas acheter non plus", vs="+", repere="→ surproduction et récession"),
        "ferme": dict(type="liste", titre="Exemple · les agriculteurs", cles=["1920", "neuf ans"], items=[
            "Endettés pour se mécaniser pendant la guerre", "La paix : des prix plus bas… et des dettes inchangées",
            "Prix agricoles en baisse depuis 1920 : la crise rurale a neuf ans de plus que le krach"], x=170, y=140, w=940),
        "para": dict(type="cols", g="La Bourse", gq="monte tout au long de 1929", d="L'économie réelle", dq="rétrécit déjà", vs="≠"),
    }),

    # ================================================================ VIII. idée 6 : la panique d'octobre
    dict(id="panique", chap="Octobre 1929 : la panique", fond="guerre", humeur="tension",
         retenir="Jeudi noir 24 oct. · lundi noir 28 oct. (≈ −13 %) · mardi noir 29 oct. (≈ −12 %, 16 millions d'actions). Tout le monde vend, personne n'achète. Dow Jones : 381 (sept. 1929) → 41 (juillet 1932), −89 % ; retour au niveau de 1929 seulement en 1954.",
         beats=[
        "{g3}Sixième idée. Fin octobre mille neuf cent vingt-neuf, la panique financière commence… et les ventes se nourrissent d'elles-mêmes.",
        "{-g3}{trois}Trois jours portent le récit. {trois.1}Le jeudi vingt-quatre octobre : le {!jeudi noir}jeudi noir. "
        "Les ventes de panique commencent, et une foule se rassemble devant la Bourse, comme celle de notre première photographie.",
        "{trois.2}Le lundi vingt-huit : la Bourse perd environ treize pour cent, en une seule séance. "
        "{trois.3}Le mardi vingt-neuf : encore environ douze pour cent. En une journée, quelque seize millions d'actions changent de mains, "
        "un record qui tiendra quarante ans.",
        "La logique est circulaire. {-trois}{cerc}{cerc.1}Tout le monde veut vendre en même temps. {cerc.2}Donc il n'y a plus d'acheteurs. "
        "{cerc.3}Donc les cours baissent encore. {cerc.4}Donc davantage de gens vendent, à n'importe quel prix… et le cercle recommence.",
        "{-cerc}{cle6}Et voici la phrase clé pour une copie. Les actionnaires ne vendent pas parce qu'ils ont changé d'avis "
        "sur l'industrie américaine. {!parce que tous les autres vendent}Ils vendent parce que tous les autres vendent. C'est cela, une panique.",
        "{-cle6}{chute}Regarde maintenant toute la chute. {chute.1}De son sommet de trois cent quatre-vingt-un en septembre mille neuf cent vingt-neuf… "
        "{chute.2}le Dow Jones descend. Il y a un bref rebond au printemps mille neuf cent trente ; ce détail est hors cours. "
        "Puis la chute reprend… {chute.3}jusqu'à quarante et un en juillet mille neuf cent trente-deux. Une perte de {!quatre-vingt-neuf pour cent}quatre-vingt-neuf pour cent.",
        "Et l'indice ne retrouvera son niveau de vingt-neuf qu'en mille neuf cent cinquante-quatre. Un quart de siècle. "
        "Les actions achetées à crédit ne valent presque plus rien.",
        "{-chute}{def6}Tu peux maintenant définir précisément la notion clé. {!Le grand krach}Le grand krach de mille neuf cent vingt-neuf, c'est l'effondrement des cours des actions américaines "
        "à la fin d'octobre mille neuf cent vingt-neuf. Attention : ce n'est pas la même chose que la Dépression qui suit. "
        "Le krach dure quelques jours, en octobre. La Dépression dure une dizaine d'années. C'est l'épisode deux.",
    ], vis={
        "g3": dict(type="globe", code="H1", sc=[5], dt=1.5),
        "trois": dict(type="liste", titre="Trois jours d'octobre 1929", cles=["jeudi noir", "13 %", "12 %", "16 millions"], items=[
            "Jeudi 24 oct. · jeudi noir : ventes de panique, une foule devant la Bourse",
            "Lundi 28 oct. · lundi noir : ≈ −13 % en une séance",
            "Mardi 29 oct. · mardi noir : ≈ −12 % ; 16 millions d'actions, un record pour 40 ans"], x=150, y=140, w=980),
        "cerc": dict(type="liste", titre="Un cercle de panique", items=[
            "Tout le monde veut vendre en même temps", "Plus d'acheteurs", "Les cours baissent encore", "Davantage de gens vendent, à n'importe quel prix ↺"], x=170, y=130, w=940),
        "cle6": dict(type="note", terme="La phrase clé pour une copie", cles=["changé d'avis", "tous les autres"],
                     t="Les actionnaires ne vendent pas parce qu'ils ont changé d'avis sur l'industrie américaine, mais parce que tous les autres vendent.",
                     etape="C'est cela, une panique.", x=170, y=200, w=940),
        "chute": dict(type="graphe", titre="L'effondrement · indice Dow Jones, 1929-1932", x=300, y=110, w=680, h=520,
                      ax=dict(x=[1929.4, 1932.8], y=[0, 420], gx=[1930, 1931, 1932], gy=[100, 200, 300, 400], lx="année", ly="indice"),
                      el=[dict(type="point", x=1929.67, y=381, c="sa", lbl="sept. 1929 : 381", lp=[1930.1, 395]),
                          dict(type="courbe", pts=DOW_CHUTE, c="ca", dur=3.0),
                          dict(type="point", x=1932.5, y=41, c="ca", lbl="juillet 1932 : 41 (−89 %)", lp=[1931.4, 5])]),
        "def6": dict(type="def", terme="Notion clé · le grand krach (1929)", cles=["fin octobre 1929", "pas"],
                     t="L'effondrement des cours des actions américaines à la fin d'octobre 1929.",
                     etape="Pas la même chose que la Dépression qui suit : quelques jours, contre dix ans.", x=170, y=200, w=940),
    }),

    # ================================================================ IX. à toi : une question problématisée
    dict(id="essay", chap="À toi : une question problématisée", fond="aube", humeur="calme",
         retenir="Évaluer = hiérarchiser les facteurs. La spéculation est le déclencheur ; les faiblesses structurelles (surproduction, inégalités, crise agricole) expliquent la profondeur ; la panique et la politique sont des amplificateurs.",
         beats=[
        "{ki}À toi, maintenant. Voici la question problématisée que le site propose pour cette partie. "
        "{!Quel rôle}Quel rôle chacun des facteurs a-t-il joué dans le déclenchement du krach de mille neuf cent vingt-neuf ? Lequel fut le plus important ?",
        "Tu as tous les facteurs. {-ki}{fac}{fac.1}La politique républicaine. {fac.2}La production de masse et les trusts. {fac.3}La spéculation à crédit. "
        "{fac.4}L'économie réelle déjà en déclin. {fac.5}Et la panique. La question te demande d'évaluer : ne les énumère pas. {!Hiérarchise-les}Hiérarchise-les.",
        "{-fac}{pa1}",
        ("P", 3.0),
        "On peut s'y prendre ainsi. {-pa1}{intro1}L'introduction, en trois temps. {intro1.1}Définis précisément le krach : "
        "l'effondrement des cours des actions américaines à la fin d'octobre vingt-neuf, distinct de la Dépression qui suit. "
        "{intro1.2}Pose la problématique : les facteurs ne sont pas indépendants, ils se renforcent les uns les autres. La question devient donc : duquel les autres dépendent-ils ? "
        "{intro1.3}Et annonce une hiérarchie, pas une liste.",
        "{-intro1}{arg}Ensuite, trois parties. {arg.1}Un : la spéculation est le meilleur candidat au rôle de déclencheur. La Bourse a triplé entre "
        "vingt-quatre et vingt-neuf. Les courtiers prêtaient jusqu'à quatre-vingt-dix pour cent. Donc une baisse de dix pour cent ruinait un acheteur. "
        "Mais la spéculation explique la soudaineté de la chute… pas sa profondeur.",
        "{arg.2}Deux : les faiblesses structurelles expliquent pourquoi la chute devient catastrophique. La surproduction, et une répartition inégale des richesses : "
        "la plupart des Américains étaient trop pauvres pour acheter ce que produisaient les usines. L'Europe ne pouvait pas acheter non plus. Et l'agriculture était en crise depuis mille neuf cent vingt.",
        "{arg.3}Trois : la confiance et la politique sont des amplificateurs, pas l'origine. La panique explique le mécanisme : on vend parce que les autres vendent. "
        "Mais la panique est elle-même une conséquence de la chute. Quant à la politique républicaine, impôts bas, trusts et droits de douane, elle a créé les conditions. "
        "Elle n'a pas causé l'effondrement directement.",
        "{-arg}{ccl}Et la conclusion, en une phrase. La spéculation a {!déclenché}déclenché le krach ; la surproduction structurelle et les inégalités "
        "ont {!décidé}décidé qu'il ne se corrigerait pas de lui-même. Hiérarchiser les facteurs compte plus que les énumérer : c'est ce que demande la question.",
    ], vis={
        "ki": dict(type="question", t="Quel rôle chacun des facteurs a-t-il joué dans le déclenchement du krach de 1929 ? Lequel fut le plus important ?"),
        "fac": dict(type="liste", titre="Les facteurs sur la table", items=[
            "La politique républicaine : impôts bas, trusts, droits de douane, crédit", "La production de masse et les trusts", "La spéculation à crédit (achat sur marge)",
            "L'économie réelle déjà en déclin", "La panique d'octobre"], x=170, y=110, w=940),
        "pa1": dict(type="pause", t="Quel rôle chacun des facteurs a-t-il joué dans le déclenchement du krach de 1929 ? Lequel fut le plus important ?",
                    sous="Mets la vidéo en pause. Rédige ton introduction et un plan en trois parties, hiérarchisé, puis relance pour voir un modèle."),
        "intro1": dict(type="liste", titre="Une introduction modèle : trois temps", items=[
            "Définir le krach : fin octobre 1929 — pas la Dépression", "La problématique : les facteurs se renforcent les uns les autres",
            "Annoncer une hiérarchie, pas une liste"], x=170, y=140, w=940),
        "arg": dict(type="liste", titre="Un plan modèle, avec des exemples précis", cles=["déclencheur", "catastrophique", "amplificateurs"], items=[
            "La spéculation, déclencheur : ×3 en cinq ans, 90 % prêtés · limite : explique la soudaineté, pas la profondeur",
            "Les faiblesses structurelles la rendent catastrophique : surproduction, majorité pauvre, Europe, agriculture depuis 1920",
            "Panique et politique républicaine : amplificateurs et conditions, pas l'origine"], x=150, y=130, w=980),
        "ccl": dict(type="note", terme="Conclusion", cles=["déclenché", "décidé"],
                    t="La spéculation a déclenché le krach ; la surproduction structurelle et les inégalités ont décidé qu'il ne se corrigerait pas de lui-même.",
                    etape="Évaluer = hiérarchiser les facteurs, pas les énumérer.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Une Bourse : deux récompenses, le dividende… ou la revente plus chère, qui ne dépend que de l'acheteur suivant. "
        "{carte.2}Le boom : la politique républicaine, la production de masse, la Ford T à deux cent soixante dollars, les voitures à crédit. "
        "{carte.3}La faiblesse : la spéculation sur marge, avec jusqu'à quatre-vingt-dix pour cent emprunté. Et des prix agricoles en baisse depuis mille neuf cent vingt. "
        "{carte.4}Et la panique : le vingt-quatre, le vingt-huit et le vingt-neuf octobre. Puis une chute de trois cent quatre-vingt-un… à quarante et un.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : comment ce krach américain devient une crise mondiale. Des banques qui font faillite, des prêts rappelés d'Europe… "
        "et le circuit du plan Dawes qui se rompt.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LE GRAND KRACH", branches=[
            dict(t="La Bourse", items=["actions · actionnaires", "dividende ou revente", "RCA : aucun dividende"]),
            dict(t="Le boom", items=["impôts bas · trusts · douane", "Ford T ≈ 260 $ (1925)", "Standard Oil · Carnegie"]),
            dict(t="La faiblesse", items=["Bourse ×3, 1924-1929", "marge : jusqu'à 90 % prêtés", "agriculture en crise dès 1920"]),
            dict(t="La panique", items=["24 · 28 · 29 oct. 1929", "381 → 41 (−89 %)", "niveau de 1929 retrouvé : 1954"])]),
        "fin": dict(type="mot", t="Ensuite : une crise mondiale", g="Épisode 2 · D'un krach américain à une crise mondiale", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="De quelles deux façons un actionnaire peut-il être récompensé ?",
         r=["Par le dividende, ou en revendant l'action plus cher qu'elle n'a coûté", "Par un salaire et une retraite", "Par des intérêts et des allègements d'impôt",
            "Par le dividende et une prime de l'État"], ok=0, voir="mec",
         ex="La seconde façon, revendre plus cher, ne dépend que de l'acheteur suivant : c'est là que commence la spéculation."),
    dict(q="Pourquoi l'exemple de RCA est-il le signe d'une bulle ?",
         r=["Elle ne versait aucun dividende, et pourtant son cours a été multiplié plusieurs fois", "Elle a fait faillite en 1925",
            "Ses bénéfices triplaient chaque année", "L'État fixait son cours"], ok=0, voir="rca",
         ex="Les acheteurs payaient ce que paierait l'acheteur suivant, non des bénéfices (exemple pris hors du cours)."),
    dict(q="Lequel de ces éléments ne faisait PAS partie de la politique républicaine des années 1920 ?",
         r=["Des impôts élevés sur les riches", "Une fiscalité basse", "Laisser se développer les trusts", "Des droits de douane sur les importations"], ok=0, voir="rep",
         ex="Harding, Coolidge et Hoover maintiennent des impôts bas, laissent grandir les trusts et protègent l'industrie par des droits de douane."),
    dict(q="En 1925, combien coûtait environ une Ford T ?",
         r=["Environ 260 $", "Environ 2 600 $", "Environ 26 $", "Environ 26 000 $"], ok=0, voir="fordt",
         ex="La production de masse abaisse tellement les coûts qu'une famille de classe moyenne peut en acheter une."),
    dict(q="Un acheteur sur marge a emprunté 90 % du prix d'une action. Que lui fait une baisse de 10 % ?",
         r=["Elle le ruine entièrement", "Elle lui coûte 1 %", "Rien, tant que l'action n'est pas vendue",
            "Le courtier paie la perte"], ok=0, voir="marg",
         ex="Action à 100 $, 10 $ payés, 90 $ empruntés : à 90 $, l'action couvre tout juste la dette. Voilà pourquoi une baisse modérée devient une débandade."),
    dict(q="Depuis quand les prix agricoles baissaient-ils aux États-Unis ?",
         r=["Depuis 1920", "Depuis octobre 1929", "Depuis 1932", "Depuis 1914"], ok=0, voir="ferme",
         ex="La crise rurale a neuf ans de plus que le krach : surproduction, majorité pauvre, Europe qui se relève encore."),
    dict(q="Que se passe-t-il le mardi 29 octobre 1929 ?",
         r=["La Bourse perd environ 12 % et 16 millions d'actions changent de mains", "Les ventes de panique commencent pour la première fois",
            "Le Dow Jones atteint son sommet de 381", "Roosevelt ferme les banques"], ok=0, voir="trois",
         ex="Le jeudi noir, c'est le 24 octobre ; le lundi 28 coûte environ 13 %, le mardi 29 environ 12 %."),
    dict(q="De combien le Dow Jones chute-t-il entre septembre 1929 et juillet 1932 ?",
         r=["De 381 à 41, environ −89 %", "De 381 à 250, environ −35 %", "De 100 à 41, environ −60 %", "De 300 à 200, environ −33 %"],
         ok=0, voir="chute",
         ex="Et il ne retrouve son niveau de 1929 qu'en 1954."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 1 « Le krach de 1929 et ses conséquences » (vue d'ensemble, objectif, lien et partie I.1), tel qu'il est rédigé sur le site ; la carte animée du chapitre et son schéma de la bulle spéculative.",
    "Hors cours (signalé dans la vidéo) : RCA (comme sur le site), immatriculations de voitures 1920-1929 (comme sur le site), Gatsby le Magnifique, valeurs intermédiaires de la courbe du Dow Jones, rebond de 1930.",
    "Photographie : foule devant la Bourse de New York, octobre 1929 (Wikimedia Commons, domaine public).",
    "Photographie : chaîne de montage Ford, Highland Park, 1913 (Wikimedia Commons, domaine public).",
    "Photographie : Ford T torpédo de 1925, restaurée (ModelTMitch, Wikimedia Commons, CC BY-SA 4.0).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
