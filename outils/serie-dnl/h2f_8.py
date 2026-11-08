"""Histoire · H2 « Les régimes totalitaires » — édition française, épisode 8 :
« Le totalitarisme à l'épreuve : question problématisée et analyse de document ».

Édition française adaptée de h2_8.py (voir outils/serie-dnl/EDITION_FR.md, section « Épisode d'épreuve ») : l'épisode
ne présente plus l'essay, le DBQ ni l'oral de la DNL, mais les deux exercices de l'histoire-géographie de Terminale,
la réponse à une question problématisée (analyse du sujet, introduction avec problématique et plan, paragraphes
argument + exemple précis, conclusion) et l'analyse de document(s) (consigne, présentation, contexte, explication,
intérêt et limites, bilan critique). Mêmes sujets et mêmes documents que l'épisode anglais (l'arrivée de Hitler au
pouvoir ; la Première Guerre mondiale et l'essor des régimes totalitaires, avec le plan, l'introduction et la conclusion
du cours ; Mussolini et Hitler comparés ; le contrôle des sociétés ; le télégramme de Roosevelt du 14 avril 1939 et le
discours de l'Obersalzberg du 22 août 1939, étudiés ensemble ; la problématique du chapitre), mêmes scènes, mêmes
identifiants, mêmes pauses « À toi ». La scène de l'oral devient celle des notions clés (totalitarisme, apaisement ;
l'épigraphe d'Arendt). Aucun barème, coefficient ni durée d'épreuve n'est donné.
Carte animée H2 : mêmes numéros de scènes que h2_8.py (la carte passe d'elle-même en français).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-8"
NOTION = "Les régimes totalitaires"
NUM = 8
TITRE = "Le totalitarisme à l'épreuve : question problématisée et analyse de document"
SUIVANT = "Épisode 9 · Récap"
PRONONCIATION = {"Reichstag": "Raïchs-tag", "Hindenburg": "Hinne-dènn-bourg", "Lebensraum": "Lé-benss-raoum",
                 "Biennio Rosso": "Bi-èn-nio Rosso", "D'Annunzio": "Da-nounn-tsio", "Fiume": "Fiou-mé",
                 "Weimar": "Vaï-mar", "Anschluss": "Ann-chlouss", "Obersalzberg": "Obeur-zalts-bèrg",
                 "Roosevelt": "Rouzvelt", "Chamberlain": "Tchèm-beur-line", "Mein Kampf": "Maïn Kammpf",
                 "Jay Winter": "Djé Ouinteur", "Arendt": "A-rennt", "SA": "S. A.", "SS": "S. S.",
                 "NKVD": "N. K. V. D."}

# vote nazi (graphique du cours) : mai 1928, sept. 1930, juillet 1932, nov. 1932
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Le premier septembre mille neuf cent trente-neuf. L'armée allemande envahit la Pologne. Deux jours plus tard, l'Europe est de nouveau en guerre. "
        "Tu sais comment les trois régimes totalitaires en sont arrivés là. Mais sauras-tu t'en servir ?",
        "{-q1}{q2}Le jour de l'épreuve, personne ne te demandera de raconter. Il faudra expliquer. Discuter. "
        "Analyser des documents. Et tenir le temps.{-q2}{-g0}",
        "{plan}Cet épisode est donc un atelier. {plan.1}D'abord, les deux exercices, en une minute. {plan.2}Puis une question problématisée qui demande d'expliquer, "
        "avec des paragraphes modèles. {plan.3}Puis le gros morceau : une question qui demande de discuter. Le plan, l'introduction, un paragraphe, la conclusion. "
        "{plan.4}Puis l'analyse de documents : présenter, critiquer, puis aller plus loin. {plan.5}Et pour finir, les notions clés, et les pièges de ce chapitre.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[37]),
        "q1": dict(type="question", t="Tu connais le chapitre. Sauras-tu t'en servir ?", bande=True),
        "q2": dict(type="question", t="Expliquer · discuter · analyser des documents", bande=True),
        "plan": dict(type="liste", titre="Cet épisode, un atelier", items=[
            "Les deux exercices en une minute", "Question problématisée · expliquer", "Question problématisée · discuter : la méthode complète",
            "L'analyse de documents : présenter, critiquer, aller plus loin", "Les notions clés, et les pièges du chapitre"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 8", t="Le totalitarisme à l'épreuve",
                      sous="question problématisée · analyse de document · les pièges du chapitre"),
    }),

    # ================================================================ I. les deux exercices
    dict(id="format", chap="Les deux exercices", fond="nuit", humeur="calme",
         retenir="Deux exercices : la réponse à une question problématisée et l'analyse de document(s), souvent associés dans un même devoir. Question problématisée : expliquer (« parce que ») ou discuter (pour, contre, hiérarchie, bilan). Analyse : présenter, situer, expliquer, intérêt et limites.",
         beats=[
        "{fmt}Un rappel rapide d'abord, comme dans la série sur la Seconde Guerre mondiale. {fmt.1}En histoire-géographie, le premier exercice est la réponse "
        "à une question problématisée : un texte construit, qui répond à une question précise. "
        "{fmt.2}Le second est l'analyse d'un document, ou de deux : les présenter, les expliquer, les critiquer. "
        "{fmt.3}Dans un même devoir, ils sont souvent associés : l'un porte sur l'histoire, l'autre sur la géographie.",
        "{-fmt}{ess}À quoi ressemblent-ils ? {ess.1}Certaines questions problématisées demandent d'expliquer : pourquoi, comment. Il te faut "
        "plusieurs raisons bien argumentées. Si tu n'écris jamais « parce que », quelque chose ne va pas. {ess.2}D'autres demandent de discuter : dans quelle mesure, quel rôle. "
        "Il faut alors des arguments pour et contre, une hiérarchie, et un bilan. {ess.3}L'analyse de document commence par la consigne : "
        "tu présentes le document, tu le situes, et tu l'expliques avec tes connaissances. "
        "{ess.4}Puis tu en montres l'intérêt et les limites, jusqu'à un bilan critique.",
        "{-ess}{cle}Une règle traverse tout cela. "
        "{!un exemple}Une idée, un exemple. Une date, un chiffre, un nom. Un argument sans exemple ne vaut presque rien.",
        "{-cle}",
    ], vis={
        "fmt": dict(type="liste", titre="Histoire-géographie · deux exercices", items=[
            "La réponse à une question problématisée", "L'analyse de document(s)",
            "Souvent dans un même devoir : l'un en histoire, l'autre en géographie"], x=170, y=140, w=940),
        "ess": dict(type="liste", titre="Deux exercices, deux démarches", cles=["parce que", "bilan"], items=[
            "Expliquer (pourquoi, comment) : plusieurs raisons… « parce que »", "Discuter (dans quelle mesure) : pour, contre, hiérarchie, bilan",
            "Analyse : la consigne, présenter, situer, expliquer", "Puis l'intérêt et les limites, jusqu'au bilan critique"],
            x=150, y=130, w=980),
        "cle": dict(type="mot", t="Une idée · un exemple", g="une date, un chiffre, un nom", y=260, taille=88),
    }),

    # ================================================================ II. expliquer : les raisons
    dict(id="explain", chap="Question problématisée · expliquer", fond="nuit", humeur="tension",
         retenir="Pourquoi Hitler parvient-il au pouvoir en janvier 1933 ? La Dépression fait des nazis le premier parti (2,6 % → 37,4 %) · la violence de rue et un parti mis en scène comme un mouvement (SA, SS) · des élites conservatrices qui croient pouvoir le contrôler (Hindenburg, 30 janv. 1933).",
         beats=[
        "{ex1}Voici un sujet type, écrit pour cette vidéo. {!Pourquoi}Pourquoi Hitler parvient-il au pouvoir en janvier mille neuf cent trente-trois ?",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{g1}Situons d'abord sur la carte. {g1.1}De mille neuf cent trente à mille neuf cent trente-deux, la crise mondiale frappe durement l'Allemagne. "
        "Le parti nazi devient le premier parti du Reichstag. {g1.2}Puis, le trente janvier mille neuf cent trente-trois, "
        "le président Hindenburg nomme Hitler chancelier. {g1.3}Quatre semaines plus tard, le Reichstag brûle. "
        "Et cet incendie donne à Hitler l'état d'urgence dont il a besoin pour suspendre les libertés.",
        "{-g1}{rais}Quelles sont les raisons ? Nous en avons vu trois dans l'épisode deux. {rais.1}La première, c'est la Dépression. "
        "En mille neuf cent trente-deux, l'Allemagne compte cinq millions six cent mille chômeurs. Un parti marginal devient un parti de masse. "
        "{rais.2}La deuxième, c'est la rue. Les SA forment une force de masse : ils combattent les communistes et protègent les réunions. "
        "Les SS sont l'élite. Le parti est mis en scène comme un mouvement, comme au congrès de Nuremberg de mille neuf cent vingt-neuf. "
        "{rais.3}La troisième raison, ce sont les élites. Hitler ne s'empare pas du pouvoir : Hindenburg et les conservateurs qui l'entourent le lui donnent. "
        "Ils sont convaincus de pouvoir le contrôler.",
        "{-rais}{peel}Comment le rédiger ? Chaque raison devient un paragraphe, en quatre temps. {peel.1}L'argument : la raison, en une phrase. "
        "{peel.2}L'exemple précis : une date, un chiffre, un nom. {peel.3}L'explication : en quoi cela a-t-il aidé Hitler ? "
        "{peel.4}Et le lien avec la question.",
        "{-peel}",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Pourquoi Hitler parvient-il au pouvoir en janvier 1933 ?",
                    src="Sujet écrit pour cette vidéo", enonce=["Réponse à une question problématisée · un paragraphe par argument"]),
        "pa1": dict(type="pause", t="Trouve trois raisons, chacune avec un exemple précis.",
                    sous="Mets la vidéo en pause, écris tes trois raisons, puis relance."),
        "g1": dict(type="globe", code="H2", sc=[16, 20, 21]),
        "rais": dict(type="liste", titre="Trois raisons", items=[
            "La Dépression → 5,6 millions de chômeurs (1932), le parti nazi à 37,4 % (juillet 1932)",
            "La rue → les SA, force de masse ; les SS, une élite",
            "Les élites → Hindenburg nomme Hitler, 30 janv. 1933"], x=150, y=140, w=980),
        "peel": dict(type="liste", titre="Une raison = un paragraphe", cles=["argument", "exemple", "explication", "lien"], items=[
            "Argument : la raison en une phrase", "Exemple précis : une date, un chiffre, un nom", "Explication : en quoi cela aide Hitler",
            "Lien : retour à la question"], x=170, y=140, w=940),
    }),

    # ================================================================ III. expliquer : les paragraphes modèles
    dict(id="explain_mod", chap="Question problématisée · paragraphes modèles", fond="nuit", humeur="calme",
         retenir="Paragraphe modèle : argument (la Dépression) · exemple (5,6 millions de chômeurs ; 2,6 % → 18,3 % → 37,4 % → 33,1 %) · explication (le désespoir devient des voix) · lien (premier parti, jamais majoritaire : la crise ouvre la porte, d'autres l'ouvrent plus grand).",
         beats=[
        "{gr}Avant le premier paragraphe, regarde le graphique du cours. {gr.1}Mai mille neuf cent vingt-huit, avant la crise. "
        "Le parti nazi ne recueille que deux virgule six pour cent des voix. {gr.2}Septembre mille neuf cent trente : dix-huit virgule trois. "
        "Sept fois plus. {gr.3}Juillet mille neuf cent trente-deux, au plus fort du chômage : trente-sept virgule quatre. "
        "C'est désormais le premier parti du Reichstag. {gr.4}Mais regarde novembre mille neuf cent trente-deux. Il recule, à trente-trois virgule un.",
        "{-gr}{mod1}Écoute maintenant un paragraphe modèle, pour la première raison.",
        "Hitler parvient d'abord au pouvoir parce que la Grande Dépression transforme un parti marginal en mouvement de masse. "
        "En mai mille neuf cent vingt-huit, le parti nazi n'obtient que deux virgule six pour cent des voix. "
        "En mille neuf cent trente-deux, environ cinq millions six cent mille Allemands sont au chômage. "
        "En juillet de cette année, le parti atteint trente-sept virgule quatre pour cent. "
        "La crise discrédite la république de Weimar, déjà associée à la défaite. Et elle donne aux nazis le public de masse qui leur manquait. "
        "Pourtant, le parti n'obtient jamais la majorité. Il recule même en novembre mille neuf cent trente-deux. "
        "La crise explique donc pourquoi Hitler devient incontournable. Elle n'explique pas pourquoi il est nommé.",
        "{-mod1}{pa2}As-tu remarqué la dernière phrase ? Elle prépare la raison suivante. À toi, maintenant.",
        ("P", 2.0),
        "{-pa2}{mod2}Voici un modèle pour la troisième raison. Hitler parvient au pouvoir avant tout parce que les élites conservatrices choisissent de le lui confier. "
        "Le trente janvier mille neuf cent trente-trois, le président Hindenburg le nomme chancelier, en toute légalité. "
        "Hindenburg est un vieux général de l'Empire. Les conservateurs qui l'entourent pensent pouvoir contrôler Hitler une fois au gouvernement. "
        "Et la façade légale les rassure. Ce choix explique le moment de son arrivée. "
        "Sans lui, un parti en recul depuis novembre mille neuf cent trente-deux n'aurait peut-être jamais atteint le pouvoir.",
        "Argument, exemple, explication, lien. Et écoute ces trois petits mots : avant tout. Même quand il faut expliquer, tu peux hiérarchiser tes raisons.{-mod2}",
    ], vis={
        "gr": dict(type="graphe", titre="Le vote nazi, 1928-1932 (graphique du cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1928, 1933.2], y=[0, 45], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40], lx="année", ly="% des voix"),
                   el=[dict(type="point", x=1928.4, y=2.6, c="sa", lbl="mai 1928 : 2,6 %", lp=[1929.1, 8]),
                       dict(type="courbe", pts=VOTE[:2], c="ca", lbl="sept. 1930 : 18,3 %", lp=[1929.4, 24], dur=1.4),
                       dict(type="courbe", pts=VOTE[1:3], c="ca", lbl="juillet 1932 : 37,4 %", lp=[1930.6, 41], dur=1.4),
                       dict(type="courbe", pts=VOTE[2:], c="el", lbl="nov. 1932 : 33,1 %", lp=[1932.0, 27], dur=0.8)]),
        "mod1": dict(type="note", terme="Paragraphe modèle · raison 1", cles=["parce que", "mouvement de masse", "majorité"],
                     t="Hitler parvient d'abord au pouvoir parce que la Dépression transforme un parti marginal en mouvement de masse : 2,6 % en mai 1928, "
                       "37,4 % en juillet 1932, avec 5,6 millions de chômeurs. Mais jamais la majorité, et 33,1 % en novembre 1932.",
                     etape="Argument · exemple · explication · lien vers la raison suivante", x=150, y=170, w=980),
        "pa2": dict(type="pause", t="Rédige le paragraphe de la troisième raison : les élites.",
                    sous="Argument, exemple, explication, lien. Mets la vidéo en pause, puis relance pour voir un modèle."),
        "mod2": dict(type="note", terme="Paragraphe modèle · raison 3", cles=["avant tout", "Hindenburg", "contrôler"],
                     t="Avant tout, les élites conservatrices confient le pouvoir à Hitler : Hindenburg le nomme légalement le 30 janvier 1933, "
                       "convaincu avec son entourage de pouvoir le contrôler.",
                     etape="Cela explique le moment : un parti en recul depuis nov. 1932", x=150, y=170, w=980),
    }),

    # ================================================================ IV. discuter : méthode et plan
    dict(id="howfar", chap="Question problématisée · discuter : le plan", fond="nuit", humeur="tension",
         retenir="Dans quelle mesure la Première Guerre mondiale est-elle responsable de l'essor des régimes totalitaires ? I. La guerre a créé la violence et les rancœurs · II. Elle a ouvert la voie à la révolution, et à la peur de la révolution · III. Mais elle n'explique pas tout (idéologies, élites, Dépression).",
         beats=[
        "{photo1}{ex2}Passons au gros morceau : un sujet tiré du cours lui-même. "
        "{!Dans quelle mesure}Dans quelle mesure la Première Guerre mondiale est-elle responsable de l'essor des régimes totalitaires ?",
        "{-ex2}{-photo1}{meth}Que veut dire dans quelle mesure ? Qu'il faut peser un facteur. Ni oui, ni non : jusqu'à quel point ? "
        "{meth.1}Il te faut donc les arguments en faveur de ce facteur. {meth.2}Puis les arguments contre, ou les autres facteurs. "
        "{meth.3}Et une réponse qui traverse tout le devoir : la problématique la pose dans l'introduction, la conclusion la tranche. "
        "{meth.4}Et le piège ? Raconter les années mille neuf cent dix-huit à mille neuf cent trente-trois, sans jamais répondre.",
        "{-meth}{g2}Souviens-toi de ce que montrait la carte. {g2.1}Les tranchées : quatre ans de massacre de masse. {g2.2}L'Italie : une victoire mutilée, "
        "puis les années rouges de mille neuf cent dix-neuf et mille neuf cent vingt. {g2.3}L'Allemagne : le Diktat de Versailles, et le mythe du coup de poignard dans le dos.",
        "{-g2}{pl}Voici le plan que propose le cours. Trois parties. "
        "{pl.1}Première partie : la guerre a créé la violence et les rancœurs. L'historien George Mosse parle de brutalisation. "
        "En mille neuf cent dix-neuf, D'Annunzio s'empare de Fiume. En Allemagne viennent la révolte spartakiste, puis Versailles, et le coup de poignard dans le dos. "
        "{pl.2}Deuxième partie : la guerre a aussi ouvert la voie à la révolution, et à la peur de la révolution. "
        "Elle a abattu le tsarisme, et porté les bolcheviks au pouvoir en mille neuf cent dix-sept. "
        "En Italie, la peur du communisme pousse propriétaires et commerçants à payer les Chemises noires, en mille neuf cent dix-neuf et mille neuf cent vingt. "
        "Et en mille neuf cent trente-trois, l'incendie du Reichstag montre que cette peur est toujours à l'œuvre. "
        "{pl.3}Troisième partie : mais la guerre n'explique pas tout. Chaque régime repose sur sa propre idéologie. Des élites ont choisi de céder le pouvoir. "
        "Et en Allemagne, la Dépression a fait d'un parti marginal un mouvement de masse.",
        "Remarque l'ordre. Le facteur d'abord, puis ses limites. C'est dans la troisième partie que se joue la réponse.{-pl}",
    ], vis={
        "photo1": dict(type="tableau", img="h2-ypres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Un soldat néo-zélandais dans les ruines de la cathédrale d'Ypres, Belgique, 1917 · Archives New Zealand, CC BY-SA 2.0"),
        "ex2": dict(type="exo", niveau="essay", titre="Dans quelle mesure la Première Guerre mondiale est-elle responsable de l'essor des régimes totalitaires ?",
                    src="Sujet du chapitre (cours)", enonce=["Réponse à une question problématisée · discuter"]),
        "meth": dict(type="liste", titre="Dans quelle mesure : peser un facteur", cles=["en faveur", "contre", "réponse"], items=[
            "Les arguments en faveur du facteur", "Les arguments contre, ou les autres facteurs",
            "Une réponse : posée par la problématique, tranchée en conclusion", "Piège : raconter 1918-1933 sans jamais répondre"],
            x=150, y=130, w=980),
        "g2": dict(type="globe", code="H2", sc=[1, 4, 5]),
        "pl": dict(type="liste", titre="Un plan en trois parties (cours)", items=[
            "I. La guerre a créé la violence et les rancœurs", "II. Elle a ouvert la voie à la révolution, et à la peur de la révolution",
            "III. Mais la guerre n'explique pas tout"], x=150, y=150, w=980),
    }),

    # ================================================================ V. discuter : l'introduction
    dict(id="intro", chap="Question problématisée · l'introduction", fond="aube", humeur="calme",
         retenir="Introduction : une accroche · la définition du totalitarisme · le contexte et les bornes (trois régimes nés après 1918) · la problématique (naître après la guerre ≠ être causé par elle) · l'annonce du plan.",
         beats=[
        "{ing}Une bonne introduction fait cinq choses. {ing.1}Une accroche : une date, ou un fait. {ing.2}La définition du mot clé du sujet. "
        "{ing.3}Le contexte et les bornes : où, quand, qui. {ing.4}La problématique : pourquoi la question n'est-elle pas évidente ? "
        "{ing.5}Et l'annonce du plan.",
        "{-ing}{pa3}",
        ("P", 2.0),
        "{-pa3}{mod3}Voici un modèle, construit à partir du cours. Écoute les cinq temps.",
        "{mod3.1}En mille neuf cent vingt-deux, Mussolini devient président du Conseil en Italie. En mille neuf cent trente-trois, Hitler devient chancelier en Allemagne. "
        "Les deux régimes naissent dans l'ombre de la Grande Guerre. "
        "{mod3.2}Un régime totalitaire cherche à contrôler totalement la société, par la contrainte, pour transformer l'homme selon une idéologie. "
        "{mod3.3}Les trois régimes étudiés, en Russie, en Italie et en Allemagne, apparaissent tous après mille neuf cent dix-huit. "
        "{mod3.4}Mais naître après la guerre, ce n'est pas être causé par elle. La guerre a-t-elle fait naître ces régimes, ou seulement créé les conditions de leur essor ? "
        "{mod3.5}Nous verrons que la guerre a créé la violence et les rancœurs. Qu'elle a ouvert la voie à la révolution, et à la peur de la révolution. "
        "Mais qu'elle n'explique pas tout.",
        "{-mod3}Cinq temps. Il n'en faut pas plus.",
    ], vis={
        "ing": dict(type="liste", titre="Une introduction en cinq temps", cles=["accroche", "définition", "contexte", "problématique", "plan"], items=[
            "Une accroche : une date, un fait", "La définition du mot clé du sujet", "Le contexte et les bornes : où, quand, qui",
            "La problématique : pourquoi la question n'est pas évidente", "L'annonce du plan"], x=170, y=120, w=940),
        "pa3": dict(type="pause", t="Écris ton introduction en cinq phrases.",
                    sous="Accroche, définition, contexte, problématique, plan. Mets la vidéo en pause, puis relance pour voir un modèle."),
        "mod3": dict(type="liste", titre="Une introduction modèle", items=[
            "Accroche · 1922 Mussolini, 1933 Hitler : nés dans l'ombre de la Grande Guerre",
            "Définition · le contrôle total de la société, par la contrainte, pour transformer l'homme selon une idéologie",
            "Contexte · trois régimes, en Russie, en Italie, en Allemagne, tous nés après 1918",
            "Problématique · naître après la guerre, est-ce être causé par elle ?",
            "Plan · violence et rancœurs · la révolution et sa peur · mais pas tout"], x=130, y=110, w=1020),
    }),

    # ================================================================ VI. discuter : paragraphe et conclusion
    dict(id="paragraphe", chap="Question problématisée · paragraphe et conclusion", fond="nuit", humeur="tension",
         retenir="Partie III : chaque régime repose sur sa propre idéologie (nation, race, classe) · les élites cèdent le pouvoir (Victor-Emmanuel III 1922, Hindenburg 1933) · la Dépression (5,6 millions de chômeurs). Conclusion : la guerre a été le terreau commun, pas la cause suffisante.",
         beats=[
        "{pa4}",
        ("P", 2.0),
        "{-pa4}{mod4}Voici un modèle du troisième paragraphe. C'est celui qui pèse.",
        "{mod4.1}Cependant, la Première Guerre mondiale n'explique pas tout. Chaque régime a été façonné par sa propre idéologie, et par des choix délibérés. "
        "{mod4.2}Les trois régimes reposent sur des idées opposées. La nation et l'État absolu, pour le fascisme. La race, pour le nazisme. La classe, pour le stalinisme. "
        "Une même guerre ne peut pas expliquer des buts aussi différents. "
        "{mod4.3}De plus, le pouvoir a été cédé par les élites. Le roi Victor-Emmanuel trois nomme Mussolini le trente octobre "
        "mille neuf cent vingt-deux. Hindenburg nomme Hitler le trente janvier mille neuf cent trente-trois. "
        "{mod4.4}Enfin, en Allemagne, la Dépression fait d'un parti marginal un mouvement de masse. "
        "Avec cinq millions six cent mille chômeurs en mille neuf cent trente-deux, le vote nazi atteint trente-sept virgule quatre pour cent. "
        "{mod4.5}La guerre a créé les rancœurs. Il a fallu la crise, et les choix des élites, pour les transformer en pouvoir.",
        "{-mod4}{ccl}Et maintenant la conclusion. Elle répond à la question en une phrase claire. Puis elle ouvre.",
        "{ccl.1}La Première Guerre mondiale a été le terreau commun des trois régimes, pas leur cause suffisante. "
        "Sans les choix des élites, et la force de chaque idéologie, ce terreau serait resté en friche. "
        "{ccl.2}Et l'ouverture ? L'historien Jay Winter voit dans les années mille neuf cent quatorze à mille neuf cent quarante-cinq une seule guerre de Trente Ans. "
        "La Seconde Guerre mondiale n'est-elle alors que la suite de la première ?",
        "{-ccl}",
    ], vis={
        "pa4": dict(type="pause", t="Rédige la partie III : « Mais la guerre n'explique pas tout ».",
                    sous="Trois arguments, un exemple chacun. Mets la vidéo en pause, puis relance pour voir un modèle."),
        "mod4": dict(type="liste", titre="Paragraphe modèle · partie III", cles=["Cependant", "idéologie", "élites", "crise"], items=[
            "Cependant : l'idéologie et des choix, pas la guerre seule", "Trois idéologies : la nation et l'État · la race · la classe", "Les élites cèdent le pouvoir : Victor-Emmanuel III (30 oct. 1922), Hindenburg (30 janv. 1933)",
            "La Dépression : 5,6 millions de chômeurs → 37,4 % (juillet 1932)", "Lien : la guerre a créé les rancœurs ; la crise et les élites les ont changées en pouvoir"],
            x=150, y=130, w=980),
        "ccl": dict(type="def", terme="Conclusion modèle", cles=["terreau", "suffisante", "friche"],
                    t="La guerre a été le terreau commun des trois régimes, pas leur cause suffisante : sans les choix des élites et la force de chaque idéologie, le terreau serait resté en friche.",
                    etape="Ouverture : la « guerre de Trente Ans » de Jay Winter, 1914-1945", x=150, y=190, w=980),
    }),

    # ================================================================ VII. deux autres sujets
    dict(id="sujets", chap="Deux autres sujets", fond="nuit", humeur="calme",
         retenir="Mussolini et Hitler comparés : une même méthode (pression de la rue + nomination légale), des circonstances différentes, le même résultat ; le rythme : 2 à 3 ans contre quelques semaines. Le même contrôle ? Identiques dans la méthode et le but, inégaux par l'ampleur et par le critère qui désigne la victime.",
         beats=[
        "{s1}Deux autres sujets du chapitre, avec la clé de chacun. {s1.1}D'abord : comparez la manière dont Mussolini et Hitler arrivent au pouvoir. "
        "Ici, la comparaison te donne le plan. Une même méthode : la pression de la rue, et la légalité au sommet. "
        "Des circonstances différentes : un vainqueur frustré, et un vaincu humilié. Et le même résultat : l'État démantelé de l'intérieur. "
        "{s1.2}Quelle différence souligner ? Le rythme. Mussolini met deux à trois ans, de la marche sur Rome aux lois de "
        "mille neuf cent vingt-cinq. Hitler n'a besoin que de quelques semaines, après l'incendie du Reichstag.",
        "{-s1}{s2}{s2.1}Second sujet : dans quelle mesure les trois régimes contrôlent-ils leur société de la même manière ? "
        "Ils utilisent les mêmes instruments. Le culte du chef. La jeunesse embrigadée tôt. Une police politique au-dessus des lois. Et les camps. "
        "{s2.2}Mais l'ampleur et le critère diffèrent. La terreur soviétique tue à la plus grande échelle : six cent quatre-vingt mille exécutions en deux ans. "
        "La violence nazie est biologique. L'Italie est la moins meurtrière, et elle garde des contre-pouvoirs : la monarchie, et l'Église.",
        "{-s2}{nu}Le cours le résume en une phrase. Apprends-la par cœur.",
        "Identiques dans la méthode et dans le but. Inégaux par l'ampleur, et par le principe qui désigne la victime. "
        "C'est cette nuance qui distingue une bonne réponse d'une liste de ressemblances.",
        "{-nu}",
    ], vis={
        "s1": dict(type="liste", titre="Comparez la manière dont Mussolini et Hitler arrivent au pouvoir", items=[
            "Même méthode · circonstances différentes · même résultat", "La différence : le rythme · 2 à 3 ans contre quelques semaines"],
            x=150, y=160, w=980),
        "s2": dict(type="liste", titre="Dans quelle mesure les trois régimes contrôlent-ils leur société de la même manière ?", items=[
            "Les mêmes instruments : le chef, la jeunesse, la police, les camps", "Ampleur et critère inégaux : URSS 680 000 exécutions · biologie nazie · Italie la moins meurtrière"],
            x=150, y=160, w=980),
        "nu": dict(type="def", terme="La nuance qui fait la différence", cles=["méthode", "ampleur", "victime"],
                   t="Identiques dans la méthode et dans le but, inégaux par l'ampleur et par le principe qui désigne la victime.",
                   etape="La classe en URSS · la race en Allemagne · la politique en Italie", x=150, y=200, w=980),
    }),

    # ================================================================ VIII. analyse de documents : la démarche
    dict(id="dbq_meth", chap="Analyse de documents · la démarche", fond="nuit", humeur="calme",
         retenir="Analyse : la consigne et la présentation (nature, auteur, date, destinataire) · le contexte · l'explication · l'intérêt (auteur, date, ce qu'il dit, ce qu'il sous-entend, son but) et les limites (portée, résultat, silences, nature, instantané), puis un bilan critique. Un texte de propagande prouve sûrement ce que le régime voulait montrer.",
         beats=[
        "{str}Passons à l'analyse de documents. La démarche est toujours la même. {str.1}D'abord, la consigne, lue deux fois, puis la présentation : "
        "la nature du document, son auteur, sa date, son destinataire. {str.2}Ensuite, le contexte : dans quelle situation a-t-il été produit ? "
        "{str.3}Puis l'explication : ce que dit le document, éclairé par tes connaissances. {str.4}Et enfin, l'intérêt et les limites, avec plusieurs arguments, jusqu'à un bilan critique.",
        "{-str}{ang}Où trouver les arguments ? Les fiches de révision du chapitre donnent cinq angles de chaque côté. "
        "{ang.1}Pour l'intérêt : l'auteur, la date, ce que dit le document, avec une courte citation, ce qu'il sous-entend, et son but. "
        "{ang.2}Pour les limites : sa portée, le résultat qu'il ne peut pas montrer, ses silences, sa nature. Et le fait qu'il ne saisit qu'un instant.",
        "{-ang}{prop}Une dernière mise en garde, essentielle dans un chapitre plein de propagande. Un texte de propagande est-il sans valeur ? Non. "
        "C'est une preuve tout à fait sûre de ce que le régime voulait montrer. Ne l'écarte donc jamais. Dis ce qu'il prouve.",
        "{-prop}",
    ], vis={
        "str": dict(type="liste", titre="Analyse de documents : la démarche", cles=["consigne", "contexte", "explication", "intérêt", "limites"], items=[
            "La consigne, puis la présentation : nature, auteur, date, destinataire", "Le contexte : la situation du moment",
            "L'explication : le document éclairé par tes connaissances", "L'intérêt et les limites, puis un bilan critique"], x=150, y=130, w=980),
        "ang": dict(type="cols", g="L'intérêt", gq="auteur · date · ce qu'il dit (citation) · ce qu'il sous-entend · son but",
                    d="Les limites", dq="portée · résultat · silences · nature · un seul instant", vs="/"),
        "prop": dict(type="note", terme="Un texte de propagande", cles=["preuve", "montrer"],
                     t="Il n'est pas « sans valeur » : c'est une preuve sûre de ce que le régime voulait montrer.",
                     etape="Dis ce qu'il prouve, puis ce qu'il ne peut pas prouver", x=150, y=200, w=980),
    }),

    # ================================================================ IX. analyse : intérêt et limites
    dict(id="dbq_a", chap="Analyse de documents · présenter et critiquer", fond="guerre", humeur="tension",
         retenir="A (télégramme de Roosevelt, 14 avril 1939) et B (Hitler à l'Obersalzberg, 22 août 1939) pour comprendre l'échec de l'apaisement : l'échec vu des deux côtés, daté, l'un public, l'autre secret. Limites : aucune voix britannique ou française, des intentions et non des résultats, des notes d'auditeurs, les derniers mois seulement.",
         beats=[
        "{doc}Voici deux documents du cours. {doc.1}Le document A est un télégramme du président Roosevelt à Hitler, "
        "daté du quatorze avril mille neuf cent trente-neuf. Il est publié aussitôt, et un télégramme identique part pour Mussolini. "
        "Roosevelt demande l'assurance qu'ils n'attaqueront pas trente et un États, nommés un par un. "
        "{doc.2}Le document B est un discours de Hitler à ses commandants en chef, à l'Obersalzberg, le vingt-deux août mille neuf cent trente-neuf. "
        "On le connaît par des notes d'auditeurs, produites à Nuremberg.",
        "Roosevelt avertit les agresseurs :{-doc}",
        ("C", "L'histoire les en tiendra pour responsables.", "c_fdr"),
        "Quatre mois plus tard, Hitler dit à ses généraux :{-c_fdr}",
        ("C", "Il n'y a pas de personnalité marquante en Angleterre et en France.", "c_ah"),
        "{-c_ah}{ex3}Voici la consigne, écrite pour cette vidéo. "
        "Présentez les documents A et B, puis montrez {!leur intérêt et leurs limites}leur intérêt et leurs limites pour comprendre l'échec de la politique d'apaisement.",
        "{-ex3}{pa5}",
        ("P", 2.0),
        "{-pa5}{rep}Un modèle. {rep.1}La présentation. Le document A est un télégramme public envoyé par le président Roosevelt à Hitler le quatorze avril mille neuf cent trente-neuf. "
        "Le document B est un discours secret prononcé par Hitler devant ses généraux le vingt-deux août mille neuf cent trente-neuf, dix jours avant l'invasion de la Pologne. "
        "{rep.2}Le contexte : leurs dates encadrent la fin de l'apaisement, du mois qui suit Prague à la veille de la guerre.",
        "{rep.3}Leur intérêt. D'abord, ensemble, ils montrent les deux moitiés de l'échec. Les démocraties ne peuvent que demander des promesses. "
        "Et le dictateur a conclu qu'elles n'agiraient jamais. Ensuite, le document B n'était pas destiné au public : "
        "Hitler n'avait donc aucune raison de cacher ce qu'il pensait des démocraties. "
        "Enfin, le document A en dit long à demi-mot. Une liste de trente et un États à protéger est un aveu : elle montre jusqu'où l'on s'attend à voir aller l'agression.",
        "{rep.4}Leurs limites. Aucun ne donne la voix du Royaume-Uni ou de la France, qui ont mené l'apaisement. Chamberlain et Daladier à Munich "
        "doivent venir de tes connaissances. Les deux documents montrent des intentions, pas des résultats. Le document B vient de notes d'auditeurs, "
        "pas d'une transcription mot pour mot. Et Hitler cherche à rassurer des généraux inquiets. Enfin, les deux ne couvrent que mille neuf cent trente-neuf. "
        "Les étapes antérieures, qui ont appris à Hitler à prendre des risques, comme la Rhénanie en mille neuf cent trente-six, en sont absentes. "
        "Le bilan critique : deux documents d'un grand intérêt, parce qu'ils montrent l'échec des deux côtés.",
    ], vis={
        "doc": dict(type="liste", titre="Deux documents du cours", items=[
            "A · Roosevelt à Hitler, télégramme, 14 avril 1939 : une « assurance » pour 31 États nommés",
            "B · Hitler à ses commandants, Obersalzberg, 22 août 1939 (document 798-PS de Nuremberg)"], x=150, y=150, w=980),
        "c_fdr": dict(type="cit", a="Franklin D. Roosevelt", o="télégramme à Hitler, 14 avril 1939", x=200, y=190, w=880),
        "c_ah": dict(type="cit", a="Adolf Hitler", o="discours de l'Obersalzberg, 22 août 1939", x=200, y=190, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="Présentez les documents A et B, puis montrez leur intérêt et leurs limites pour comprendre l'échec de la politique d'apaisement.",
                    src="Consigne écrite pour cette vidéo, sur deux documents du cours", enonce=["Analyse de documents · présenter, expliquer, critiquer"]),
        "pa5": dict(type="pause", t="Rédige la présentation des deux documents, puis leur contexte.",
                    sous="Mets la vidéo en pause, écris-les, puis relance pour voir un modèle."),
        "rep": dict(type="liste", titre="Un modèle de réponse", items=[
            "Présentation : A, le télégramme public de Roosevelt, 14 avril 1939 · B, le discours secret de Hitler, 22 août 1939",
            "Contexte : de l'après-Prague à la veille de la guerre",
            "Intérêt : les deux moitiés d'un même échec · un discours secret · 31 États sous-entendus",
            "Limites : aucune voix britannique ou française · des intentions · des notes d'auditeurs · 1939 seulement → bilan critique"], x=150, y=130, w=980),
    }),

    # ================================================================ X. analyse : au-delà des documents
    dict(id="dbq_b", chap="Analyse de documents · au-delà des documents", fond="nuit", humeur="tension",
         retenir="Le rôle du totalitarisme dans l'effondrement de la paix : I. les idéologies font de la guerre une valeur (Abyssinie 1935, Lebensraum, Mandchourie 1931, Nankin 1937) · II. les démocraties laissent l'agression réussir (SDN, apaisement, lois de neutralité) · III. une chaîne que seule la guerre peut rompre (Rhénanie 1936 → Prague → le pacte). Le totalitarisme a fourni la volonté ; la réticence des démocraties, l'occasion.",
         beats=[
        "{ex4}La consigne peut aller plus loin : les documents, plus tes connaissances. Et la question est la problématique du chapitre. "
        "À l'aide des documents et de vos connaissances, montrez quel rôle le totalitarisme a joué dans l'effondrement de la paix mondiale, à la fin des années mille neuf cent trente.",
        "{-ex4}{pa6}",
        ("P", 2.0),
        "{-pa6}{g3}D'abord, l'enchaînement des faits, sur la carte. {g3.1}Octobre mille neuf cent trente-cinq. L'Italie envahit l'Abyssinie, au nom de Rome. "
        "{g3.2}Mars mille neuf cent trente-six. Les troupes allemandes entrent en Rhénanie, et personne ne réagit. {g3.3}Mars mille neuf cent trente-huit : l'Anschluss. "
        "{g3.4}Septembre mille neuf cent trente-huit. À Munich, les Sudètes sont livrées, sans les Tchèques. {g3.5}En mars mille neuf cent trente-neuf, Hitler prend Prague. "
        "{g3.6}Août mille neuf cent trente-neuf : le pacte germano-soviétique. {g3.7}Et le premier septembre : la Pologne.",
        "{-g3}{pl2}Maintenant le plan, tiré du cours. {pl2.1}Première partie : les idéologies totalitaires font de la guerre une valeur, et de l'expansion un but. "
        "Le fascisme envahit l'Abyssinie en mille neuf cent trente-cinq. Le nazisme veut le Lebensraum, annoncé dans Mein Kampf en mille neuf cent vingt-cinq. "
        "Le militarisme japonais prend la Mandchourie en mille neuf cent trente et un, et Nankin en mille neuf cent trente-sept. "
        "Le document B a sa place ici : un dictateur qui a décidé d'attaquer. "
        "{pl2.2}Deuxième partie : mais les démocraties laissent l'agression réussir. Face à l'Abyssinie, la SDN épargne le pétrole. "
        "Le Royaume-Uni signe l'accord naval de mille neuf cent trente-cinq. Puis vient Munich, en mille neuf cent trente-huit. Et en Amérique, les lois de neutralité. "
        "Le document A a sa place ici : la plus puissante des démocraties ne peut que demander des promesses. "
        "{pl2.3}Troisième partie : les deux se combinent en une chaîne que seule la guerre peut rompre. Le pari de la Rhénanie apprend à Hitler que les démocraties céderont. "
        "Prague met fin à l'apaisement. Et le pacte ouvre la route de la Pologne.",
        "{-pl2}{jug}Et la réponse, en une phrase du cours. Le totalitarisme a fourni la volonté de faire la guerre. "
        "La réticence des démocraties a fourni l'occasion. Une bonne réponse garde les deux moitiés.",
        "{-jug}",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="À l'aide des documents et de vos connaissances, montrez quel rôle le totalitarisme a joué dans l'effondrement de la paix mondiale à la fin des années 1930.",
                    src="La problématique du chapitre, en consigne d'analyse", enonce=["Documents A et B + tes connaissances"]),
        "pa6": dict(type="pause", t="Écris un plan en trois parties, et places-y les documents A et B.",
                    sous="Mets la vidéo en pause, écris ton plan, puis relance pour voir un modèle."),
        "g3": dict(type="globe", code="H2", sc=[27, 28, 33, 34, 35, 36, 37]),
        "pl2": dict(type="liste", titre="Un plan en trois parties (cours)", items=[
            "I. Les idéologies font de la guerre une valeur → Abyssinie, Lebensraum, Mandchourie · doc. B",
            "II. Les démocraties laissent l'agression réussir → SDN, accord de 1935, Munich, lois de neutralité · doc. A",
            "III. Une chaîne que seule la guerre peut rompre → Rhénanie 1936 … Prague … le pacte"], x=150, y=140, w=980),
        "jug": dict(type="def", terme="La réponse", cles=["volonté", "occasion"],
                    t="Le totalitarisme a fourni la volonté de faire la guerre ; la réticence des démocraties a fourni l'occasion.",
                    etape="Garder les deux moitiés", x=150, y=200, w=980),
    }),

    # ================================================================ XI. les notions clés
    dict(id="oral", chap="Les notions clés", fond="aube", humeur="calme",
         retenir="Une notion clé : une définition, une date, un exemple, un lien avec un autre chapitre. Notions clés du chapitre : le totalitarisme, l'apaisement. Arendt : la propagande fabrique les faits (incendie du Reichstag) ; des masses ont soutenu ces régimes.",
         beats=[
        "{or}Les notions clés servent dans les deux exercices : une définition juste, au bon moment, rapporte toujours. Chacune se maîtrise de la même façon. "
        "{or.1}Une définition, en une phrase. {or.2}Une date. {or.3}Un exemple précis. {or.4}Et un lien avec un autre chapitre.",
        "{-or}{kt}Voici les deux notions clés du chapitre. {kt.1}Le totalitarisme : un régime qui cherche à imposer un contrôle total à la société, par la contrainte, "
        "pour transformer l'homme selon une idéologie. {kt.2}L'apaisement : accepter les exigences des agresseurs, pour éviter la guerre. "
        "C'est la politique de Chamberlain à partir de mille neuf cent trente-sept, et de Daladier, jusqu'à Prague en mars mille neuf cent trente-neuf.",
        "{-kt}{photo2}{ar}Un dernier outil, tiré des fiches de révision : l'épigraphe de Hannah Arendt. "
        "La propagande totalitaire traite les faits comme une chose que le pouvoir peut fabriquer. Utilise-la avec un exemple. "
        "En mille neuf cent trente-trois, l'incendie du Reichstag est imputé aux communistes. Puis ajoute sa seconde leçon. "
        "De larges masses ont soutenu ces régimes. Le tableau n'est pas en noir et blanc.",
        "{-ar}{-photo2}",
    ], vis={
        "or": dict(type="liste", titre="Une notion clé : comment la maîtriser", items=[
            "Une définition en une phrase", "Une date", "Un exemple précis", "Un lien avec un autre chapitre"],
            x=170, y=130, w=940),
        "kt": dict(type="cols", g="Le totalitarisme", gq="le contrôle total de la société, par la contrainte, pour transformer l'homme selon une idéologie",
                   d="L'apaisement", dq="accepter les exigences des agresseurs pour éviter la guerre · Chamberlain, Daladier · Munich 1938", vs="+"),
        "photo2": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, autrice des Origines du totalitarisme (1951), en 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
        "ar": dict(type="note", terme="L'épigraphe d'Arendt · comment s'en servir", cles=["fabriquer", "Reichstag", "masses"],
                   t="La propagande traite les faits comme une chose que le pouvoir peut fabriquer : l'incendie du Reichstag imputé aux communistes (1933).",
                   etape="Sa seconde leçon : de larges masses ont soutenu ces régimes", x=150, y=190, w=980),
    }),

    # ================================================================ XII. les pièges
    dict(id="pieges", chap="Les pièges du chapitre", fond="guerre", humeur="mystere",
                  beats=[
        "{pi}Pour finir, six pièges. Chacun vient d'un document du cours ou d'une erreur fréquente, et chacun peut te coûter des points. "
        "{pi.1}Piège un : Matteotti. Le document du cours date son assassinat de mille neuf cent vingt-cinq. En réalité, il est enlevé et tué "
        "le dix juin mille neuf cent vingt-quatre. Mille neuf cent vingt-cinq, c'est l'année où Mussolini en revendique la responsabilité. "
        "C'est aussi l'année des lois fascistissimes.",
        "{pi.2}Piège deux. On lit souvent que Molotov a été exécuté. Il ne l'a jamais été : il meurt en mille neuf cent quatre-vingt-six. "
        "Le chef du NKVD exécuté à la fin de la Grande Purge, c'est Iejov, en mille neuf cent quarante.",
        "{pi.3}Piège trois : le programme T quatre. Écris qu'environ soixante-dix mille personnes handicapées sont assassinées entre mille neuf cent trente-neuf "
        "et mille neuf cent quarante et un. L'ancien chiffre, deux cent mille, est le bilan jusqu'en mille neuf cent quarante-cinq.",
        "{pi.4}Piège quatre. Le document du cours parle d'un Congrès républicain qui vote les lois de neutralité. Mais les démocrates y sont majoritaires. "
        "Écris donc : un Congrès isolationniste.",
        "{pi.5}Piège cinq. L'incident de Corfou date de mille neuf cent vingt-trois, sous Mussolini. Il ne fait pas partie de la victoire mutilée. Fiume, si.",
        "{pi.6}Et piège six, le plus fréquent de tous. Hitler n'a jamais obtenu la majorité dans une élection libre. Trente-sept virgule quatre pour cent, au plus. "
        "Il a été nommé.",
        "{-pi}La prochaine fois, {fin}le dernier épisode : le récap de tout le chapitre, d'un seul tenant.",
        ("P", 2.0),
    ], vis={
        "pi": dict(type="liste", titre="Six pièges", items=[
            "Matteotti : tué le 10 juin 1924 · revendiqué le 3 janv. 1925", "Exécuté en 1940 : Iejov, pas Molotov",
            "T4 : ≈ 70 000 victimes en 1939-1941", "Lois de neutralité : « un Congrès isolationniste »",
            "Corfou (1923) n'est pas la victoire mutilée : Fiume, si", "Hitler : 37,4 % au plus · nommé, jamais élu par une majorité"],
            x=150, y=110, w=980),
        "fin": dict(type="mot", t="Prochain : le récap", g="Épisode 9 · tout le chapitre", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Quand le sujet demande d'expliquer, comment rédiger chaque raison ?", r=["Un paragraphe : argument, exemple précis, explication, lien",
         "Une phrase par raison", "Une liste de dates", "Une citation et son analyse"], ok=0, voir="peel",
         ex="Une date, un chiffre ou un nom comme exemple, et un lien avec la question."),
    dict(q="Quel est le meilleur score du parti nazi avant la nomination de Hitler ?", r=["37,4 % (juillet 1932)", "51 % (mars 1933)",
         "18,3 % (sept. 1930)", "33,1 % (nov. 1932)"], ok=0, voir="gr",
         ex="Le premier parti, mais jamais la majorité ; il retombe même à 33,1 % en novembre 1932."),
    dict(q="Dans « Dans quelle mesure la Première Guerre mondiale est-elle responsable… », que fait la partie III ?", r=["Elle montre les limites du facteur : idéologies, élites, Dépression",
         "Elle raconte la marche sur Rome", "Elle répète la partie I avec d'autres exemples", "Elle décrit la Seconde Guerre mondiale"], ok=0, voir="pl",
         ex="Le facteur d'abord, puis ses limites : c'est là que se construit la réponse."),
    dict(q="Lequel n'est PAS l'un des cinq temps de l'introduction modèle ?", r=["La liste de toutes les dates du chapitre", "Une accroche",
         "La définition du mot clé", "La problématique"], ok=0, voir="ing",
         ex="Accroche, définition, contexte, problématique, plan."),
    dict(q="Quand on compare Mussolini et Hitler, quelle est la principale différence dans le démantèlement de l'État ?", r=["Le rythme : des années pour Mussolini, des semaines pour Hitler",
         "Mussolini a été élu, Hitler non", "Hitler n'avait pas de forces paramilitaires", "Mussolini a pris le pouvoir par les armes"], ok=0, voir="s1",
         ex="Deux à trois ans (1922-1925) contre quelques semaines après l'incendie du Reichstag."),
    dict(q="Que comprend la présentation d'un document ?", r=["Sa nature, son auteur, sa date, son destinataire", "Ton avis personnel",
         "Une citation de tout le texte", "Une définition"], ok=0, voir="str",
         ex="Puis le contexte, l'explication, et enfin l'intérêt et les limites, jusqu'au bilan critique."),
    dict(q="Laquelle est une vraie LIMITE du discours de Hitler du 22 août 1939 ?", r=["On le connaît par des notes d'auditeurs, pas par une transcription mot pour mot",
         "Il était secret", "Il est daté", "Il s'adressait à des généraux"], ok=0, voir="rep",
         ex="Son caractère secret est un atout ; sa transmission et son but (rassurer des généraux) sont des limites."),
    dict(q="Qui est exécuté à la fin de la Grande Purge, en 1940 ?", r=["Iejov, chef du NKVD", "Molotov", "Beria", "Kirov"], ok=0,
         voir="pi", ex="Molotov meurt en 1986 ; Beria est exécuté en 1953, après la mort de Staline."),
]

CREDITS = [
    "Contenu : la méthode des exercices d'histoire-géographie de Terminale (réponse à une question problématisée, analyse de document(s)) ; "
    "le cours d'histoire de Terminale, chapitre « Les régimes totalitaires » : ses sujets, sa problématique et ses notions clés, les fiches de révision, "
    "deux documents du chapitre (télégramme de Roosevelt du 14 avril 1939 ; discours de Hitler à l'Obersalzberg, 22 août 1939), "
    "le graphique du vote nazi, les points à vérifier du chapitre.",
    "Le sujet « Pourquoi Hitler parvient-il au pouvoir… », la consigne d'analyse et les copies modèles ont été écrits pour cette vidéo.",
    "Photographies (via Wikimedia Commons) : la cathédrale d'Ypres en ruines, 1917 (Henry Armytage Sanders, Archives New Zealand, CC BY-SA 2.0) ; Hannah Arendt en 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0).",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
