"""Histoire · chapitre 2 « Les régimes totalitaires » — série vidéo, édition française, épisode 2 :
« De la Grande Guerre au pouvoir » (parties I.1 « L'héritage de la Première Guerre mondiale » et I.2 « La prise du
pouvoir » du cours).

Édition française de h2_2.py (cahier des charges : EDITION_FR.md ; l'anglais est gardé intact) : histoire-géographie
classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes visuels, mêmes repères,
mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 1 brutalisation (1914-1918) · 2 Russie 1917 · 3 Allemagne, nov. 1918 - janv. 1919 · 4 Italie, victoire mutilée et
       Biennio Rosso · 5 Versailles et coup de poignard · 6 marche sur Rome · 7 putsch de Munich, Mein Kampf ·
       13 deux crises en 1929 · 16 la crise fait des nazis le premier parti · 20 Hitler chancelier · 21 incendie du Reichstag
Adaptations : paragraphe d'essay « Explain » → paragraphe de réponse à une question problématisée (« Explique
comment ») ; « How far… legally? » → « Dans quelle mesure… légalement ? » (pour et contre, puis bilan). Vocabulaire
français : Red Scare → la peur rouge (distinguée de la Terreur rouge), stab in the back → le coup de poignard dans le
dos, Law and Order → la loi et l'ordre, fasces → les faisceaux, Blackshirts → les Chemises noires. Faits identiques à
l'anglais ; dit « hors du cours » comme dans l'anglais : effectifs de la SA, décret du 28 février 1933, date de Potsdam,
programme en 25 points de 1920. Points du site repris : dates et effectifs de la marche sur Rome, croix gammée
expliquée par Hitler dans Mein Kampf.
Chaîne : outils/serie-philo/generer.py h2f_2 ; sortie dans dnl/serie/ (h2f-2.*).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-2"
NOTION = "Les régimes totalitaires"
NUM = 2
TITRE = "De la Grande Guerre au pouvoir"
SUIVANT = "Épisode 3 · Trois régimes, trois idéologies"
PRONONCIATION = {"Reichstag": "Raïks-tag", "Hindenburg": "Hinne-dène-bourg", "Weimar": "Vaï-mar",
                 "Liebknecht": "Lib-knècht", "Freikorps": "Fraï-korps", "D'Annunzio": "Da-nounn-tsio",
                 "Fiume": "Fiou-mé", "Biennio Rosso": "Bi-èn-nio Rosso", "Mein Kampf": "Maïne Kampf",
                 "Diktat": "Dik-tatt", "Mosse": "Moss", "De Vecchi": "Dé Vèk-ki", "De Bono": "Dé Bo-no",
                 "Potsdam": "Pots-dam", "Matteotti": "Mat-té-otti", "fascistissimes": "fa-chis-tis-si-mé",
                 "Gabriele": "Ga-bri-èlé", "George": "Djordj", "Paul von": "Paul fonn", "SA": "èss-a", "SS": "èss-èss"}

# chômage en Allemagne (millions), lu sur le graphique du cours (H2Weimar), arrondi
CHOMAGE = [[1921, .35], [1922, .2], [1923, .75], [1924, 1.0], [1925, .65], [1926, 2.0], [1927, 1.35], [1928, 1.4],
           [1929, 1.9], [1930, 3.1], [1931, 4.5], [1932, 5.6]]
# vote NSDAP aux élections au Reichstag (mai 1928, sept. 1930, juillet 1932, nov. 1932), placé en année décimale
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Berlin, le trente janvier mille neuf cent trente-trois. Le président de la République est un vieux maréchal, Hindenburg. "
        "Ce jour-là, il nomme Adolf Hitler chancelier d'Allemagne. {q1}Pas de coup d'État. Tout est parfaitement légal.",
        "{-q1}{q2}Onze ans plus tôt, le roi d'Italie avait fait de même pour Mussolini. Alors comment ces hommes sont-ils arrivés au pouvoir ?",
        "{-q2}{q3}Pour répondre, il faut remonter plus loin. Jusqu'aux tranchées de mille neuf cent quatorze. Car les régimes totalitaires "
        "sont nés de la Première Guerre mondiale.",
        "{-q3}{-g0}Aujourd'hui, la première partie du chapitre, points un et deux. {plan}{plan.1}D'abord, l'histoire sur la carte, de mille neuf cent quatorze à mille neuf cent trente-trois. "
        "{plan.2}Puis l'héritage de la guerre, en Russie, en Italie et en Allemagne. {plan.3}Ensuite, la prise du pouvoir, à commencer par le fascisme de Mussolini. "
        "{plan.4}Puis le nazisme de Hitler : la crise, et la nomination légale. {plan.5}Et pour finir, deux exercices de composition.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[20]),
        "q1": dict(type="question", t="30 janvier 1933 : Hitler chancelier. Sans coup d'État.", bande=True),
        "q2": dict(type="question", t="Comment Mussolini et Hitler sont-ils arrivés au pouvoir ?", bande=True),
        "q3": dict(type="question", t="Retour aux tranchées de 1914.", bande=True),
        "plan": dict(type="liste", titre="Épisode 2 · parties I.1 et I.2 du cours", items=[
            "L'histoire sur la carte : 1914 – 1933", "I.1 · L'héritage de la guerre : Russie, Italie, Allemagne",
            "I.2 · Le fascisme de Mussolini : des squadre à la marche sur Rome",
            "I.2 · Le nazisme de Hitler : la rue, la crise, la nomination", "À toi : deux exercices de composition"],
            x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 2", t="De la Grande Guerre au pouvoir",
                      sous="1914 – 1933 · l'héritage de la guerre · la prise du pouvoir"),
    }),

    # ================================================================ la carte : 1914-1923
    dict(id="carte1", chap="Sur la carte : 1914 – 1923", fond="nuit", humeur="tension",
         retenir="1914-1918 les tranchées · 1917 les bolcheviks · nov. 1918 – janv. 1919 Weimar, les spartakistes · 1919 Versailles · 1919-1920 Biennio Rosso · oct. 1922 marche sur Rome · nov. 1923 putsch de Munich.",
         beats=[
        "{g1}Suivons d'abord l'histoire sur la carte. {g1.1}De mille neuf cent quatorze à mille neuf cent dix-huit : quatre ans de guerre des tranchées, et de massacres de masse. "
        "Parmi les soldats, un Allemand nommé Adolf Hitler.",
        "{g1.2}Mille neuf cent dix-sept. La guerre fait tomber l'empire russe. En février, le tsar abdique. En octobre, les bolcheviks de Lénine prennent le pouvoir. "
        "Puis ils gagnent une guerre civile, qui dure jusqu'en mille neuf cent vingt-deux.",
        "{g1.3}Novembre mille neuf cent dix-huit. L'Allemagne est vaincue. L'Empire tombe, et une république est proclamée : la république de Weimar. "
        "En janvier mille neuf cent dix-neuf, un soulèvement communiste à Berlin est écrasé dans le sang.",
        "{g1.4}En Italie, la guerre a été gagnée. Mais les nationalistes se sentent floués. Et en mille neuf cent dix-neuf et mille neuf cent vingt, les paysans occupent les terres, et les ouvriers "
        "occupent les usines. Ce sont les années rouges.",
        "{g1.5}Mille neuf cent dix-neuf : le traité de Versailles. L'Allemagne doit accepter un traité qu'elle n'a jamais négocié. Un Diktat.",
        "{g1.6}Octobre mille neuf cent vingt-deux. Les Chemises noires de Mussolini marchent sur Rome, et le roi le nomme chef du gouvernement. "
        "{g1.7}Novembre mille neuf cent vingt-trois. À Munich, Hitler tente de prendre le pouvoir par la force. Il échoue, et va en prison.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 3, 4, 5, 6, 7]),
    }),

    # ================================================================ la carte : 1929-1933
    dict(id="carte2", chap="Sur la carte : 1929 – 1933", fond="nuit", humeur="tension",
         retenir="1929 la crise · juillet 1932 : NSDAP 37,4 %, premier parti · 30 janv. 1933 : Hitler nommé chancelier · 27 févr. 1933 : l'incendie du Reichstag.",
         beats=[
        "{g2}{g2.1}Vient ensuite mille neuf cent vingt-neuf. Le krach ouvre la crise du capitalisme. Et les nazis tiennent leur congrès à Nuremberg. Deux crises à la fois.",
        "{g2.2}En Allemagne, des millions de gens perdent leur emploi. En juillet mille neuf cent trente-deux, les nazis deviennent le premier parti.",
        "{g2.3}Le trente janvier mille neuf cent trente-trois, Hindenburg nomme Hitler chancelier. "
        "{g2.4}Quatre semaines plus tard, le Reichstag brûle. Et les libertés sont suspendues.",
        "{-g2}{fr1}Voici donc les dates à connaître. {fr1.1}Octobre mille neuf cent dix-sept : les bolcheviks prennent le pouvoir. {fr1.2}Mille neuf cent dix-neuf : le traité de Versailles. "
        "{fr1.3}Octobre mille neuf cent vingt-deux : la marche sur Rome. {fr1.4}Novembre mille neuf cent vingt-trois : l'échec du putsch de Munich. "
        "{fr1.5}Juillet mille neuf cent trente-deux : les nazis deviennent le premier parti. {fr1.6}Et le trente janvier mille neuf cent trente-trois : Hitler est chancelier.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[13, 16, 20, 21]),
        "fr1": dict(type="frise", items=[
            dict(nom="Bolcheviks", d=1917, q="octobre"), dict(nom="Versailles", d=1919, q="le « Diktat »"),
            dict(nom="Marche sur Rome", d=1922, q="octobre"), dict(nom="Putsch de Munich", d=1923, q="novembre"),
            dict(nom="NSDAP 37,4 %", d=1932, q="juillet"), dict(nom="Chancelier", d=1933, q="30 janvier")]),
    }),

    # ================================================================ I.1, idée 1 : la brutalisation
    dict(id="brutal", chap="I.1 · La brutalisation", fond="guerre", humeur="tension",
         retenir="Brutalisation (George Mosse) : la guerre a banalisé la violence ; la Grande Guerre est la « matrice du totalitarisme ». Exemple : Hitler soldat en 1915.",
         beats=[
        "{photo1}{def1}Passons au cours, idée par idée. Première partie, point un : l'héritage de la Première Guerre mondiale. "
        "Idée un. L'historien George Mosse a forgé un mot pour cela. La {!brutalisation}brutalisation. "
        "{def1.1}Quatre ans de massacres de masse ont habitué les soldats à la violence. Après mille neuf cent dix-huit, ils l'ont ramenée dans la vie civile. "
        "Et dans la politique. Les traumatismes de la guerre ont élevé le niveau de violence des sociétés d'après-guerre.",
        "{-def1}Pour Mosse, la guerre est la matrice du totalitarisme. Regarde les nouveaux régimes. {mat}{mat.1}Les uniformes. {mat.2}Les grades. "
        "{mat.3}Les défilés. {mat.4}Le mépris de la vie humaine. Tout cela vient du front.",
        "{-mat}{-photo1}{ex1}Le cours en donne un exemple : une photographie d'Adolf Hitler soldat, en mille neuf cent quinze, assis parmi ses camarades. "
        "{ex1.1}Mosse développe cette idée dans son livre De la Grande Guerre au totalitarisme.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-ypres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Un soldat néo-zélandais dans les ruines de la cathédrale d'Ypres, Belgique, 1917 · Archives New Zealand, CC BY-SA 2.0"),
        "def1": dict(type="def", cles=["violence", "politique"], terme="La brutalisation · George Mosse",
                     t="Quatre ans de massacres de masse ont banalisé la violence ; les soldats l'ont ramenée dans la vie civile et dans la politique.",
                     etape="Les traumatismes de la guerre élèvent le niveau de violence après 1918", x=170, y=200, w=940),
        "mat": dict(type="liste", titre="La Grande Guerre, « matrice du totalitarisme »", items=[
            "Les uniformes", "Les grades", "Les défilés", "Le mépris de la vie humaine"], x=170, y=140, w=940),
        "ex1": dict(type="note", terme="Exemple · le cours", cles=["soldat", "camarades"],
                    t="Adolf Hitler soldat en 1915, assis parmi ses camarades.",
                    etape="George Mosse, De la Grande Guerre au totalitarisme (Fallen Soldiers)", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 2 : la Russie
    dict(id="russie", chap="I.1 · La Russie : du tsar aux bolcheviks", fond="nuit", humeur="tension",
         retenir="Févr. 1917 le tsar abdique · oct. 1917 coup de force bolchevik (Lénine, Trotski) avec les soviets · paix avec l'Allemagne · guerre civile gagnée par l'Armée rouge (jusqu'en 1922) · URSS 1922 · la peur rouge.",
         beats=[
        "{g3}{g3.1}Idée deux : la Russie. C'est un rappel de Première, et il est au programme. "
        "{rus}La guerre a ruiné l'empire russe. {rus.1}En février mille neuf cent dix-sept, une révolution force le tsar à abdiquer. "
        "{rus.2}En octobre, les bolcheviks, menés par Lénine et Trotski, réalisent ce que le cours appelle un coup de force communiste. "
        "Ils sont soutenus par les {!soviets}soviets, les conseils d'ouvriers et de paysans, dans les usines et dans les campagnes.",
        "{rus.3}Les bolcheviks signent la paix avec l'Allemagne. {rus.4}Puis ils mènent une guerre civile contre les Blancs. L'Armée rouge la gagne, en mille neuf cent vingt-deux. "
        "{rus.5}Et la même année, l'Union soviétique est créée.",
        "{-rus}{-g3}{photo2}{rs}Pourquoi est-ce important pour l'Italie et l'Allemagne ? Parce que le bolchevisme, c'est le marxisme. Et le marxisme, c'est la fin de la propriété privée. "
        "{rs.1}Toute l'Europe a peur. C'est la {!peur rouge}peur rouge.",
        "{-rs}{mots1}Attention au vocabulaire. {mots1.g}La peur rouge, c'est la crainte du communisme à l'Ouest. "
        "{mots1.d}La Terreur rouge, c'est autre chose : la violence des bolcheviks contre leurs ennemis, en Russie même, à partir de mille neuf cent dix-huit.{-photo2}",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[2]),
        "rus": dict(type="liste", titre="La Russie, 1917 – 1922", x=790, y=110, w=460, petit=True, bande=True, items=[
            "Févr. 1917 : le tsar abdique", "Oct. 1917 : le coup de force bolchevik (Lénine, Trotski), avec les soviets",
            "La paix avec l'Allemagne", "Guerre civile contre les Blancs, gagnée par l'Armée rouge (jusqu'en 1922)", "1922 : création de l'URSS"]),
        "photo2": dict(type="tableau", img="h2-lenin-putilov", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .35, .45],
                       legende="Lénine parle aux ouvriers de l'usine Poutilov, Petrograd, mai 1917 · Tableau d'Isaak Brodsky, 1929, domaine public"),
        "rs": dict(type="def", cles=["propriété", "Europe"], terme="La peur rouge",
                   t="Le bolchevisme, c'est la fin de la propriété privée : la peur du communisme gagne toute l'Europe.",
                   etape="Exemple : Lénine parle aux ouvriers, aux soldats et aux marins à Petrograd, avril 1917 (cours)",
                   x=170, y=200, w=940),
        "mots1": dict(type="cols", g="La peur rouge", gq="la crainte du communisme à l'Ouest", d="La Terreur rouge",
                      dq="la violence bolchevique en Russie même, à partir de 1918", vs="≠", repere="Attention au vocabulaire"),
    }),

    # ================================================================ I.1, idées 3 et 4 : l'Italie
    dict(id="italie", chap="I.1 · L'Italie : une victoire mutilée, deux années rouges", fond="nuit", humeur="tension",
         retenir="« Victoire mutilée » : pas toutes les terres promises → irrédentisme ; troubles, inflation, chômage. Fiume (D'Annunzio, 1919-1920). Biennio Rosso (1919-1920) : terres et usines occupées ; Chemises noires payées par les propriétaires.",
         beats=[
        "{g4}{g4.1}Idée trois : l'Italie. En mille neuf cent dix-huit, l'Italie est dans le camp des vainqueurs. Mais elle n'obtient pas toutes les terres promises. "
        "Les nationalistes parlent de {!victoire mutilée}victoire mutilée. Le pays a gagné. Il a payé le prix du sang. Et pourtant il se sent floué. "
        "{vm}{vm.1}Cela nourrit un mouvement {!irrédentiste}irrédentiste, qui réclame les terres irrédentes, celles qui ne sont pas encore rattachées. "
        "{vm.2}Et cette frustration s'ajoute aux troubles sociaux, à l'inflation et au chômage de masse.",
        "{-vm}L'exemple, c'est Fiume. {fiu}{fiu.1}En septembre mille neuf cent dix-neuf, le poète Gabriele D'Annunzio s'empare de la ville avec des volontaires nationalistes. "
        "{fiu.2}Il la tient jusqu'en décembre mille neuf cent vingt. {fiu.3}Mussolini lui empruntera plus tard ses rituels.",
        "{-fiu}{-g4}{photo3}{br}Idée quatre : le {!Biennio Rosso}Biennio Rosso. Les deux années rouges, mille neuf cent dix-neuf et mille neuf cent vingt. "
        "{br.g}Les paysans occupent les terres. Les ouvriers font grève, ou prennent les usines. Les possédants croient qu'un mille neuf cent dix-sept italien approche. "
        "{br.d}Les Chemises noires de Mussolini, la milice fasciste, répondent par une répression violente. Et les grands propriétaires les paient pour reprendre les terres.",
        "{-br}{tur}Le cours en donne l'exemple. {tur.1}La grève générale de mille neuf cent vingt, à Turin. Les ouvriers occupent les usines, et les font tourner eux-mêmes. "
        "{tur.2}La peur était donc réelle. Et le fascisme a grandi comme le bras armé des possédants effrayés.{-photo3}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[4]),
        "vm": dict(type="liste", titre="L'Italie : une « victoire mutilée »", x=60, y=110, w=620, petit=True, bande=True, items=[
            "L'irrédentisme : réclamer les terres « irrédentes »", "Troubles, inflation, chômage de masse"]),
        "fiu": dict(type="liste", titre="Exemple : Fiume", x=60, y=110, w=620, petit=True, bande=True, items=[
            "Sept. 1919 : D'Annunzio s'empare de la ville", "Tenue jusqu'en décembre 1920", "Des rituels repris ensuite par Mussolini"]),
        "photo3": dict(type="tableau", img="h2-biennio-rosso", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Des gardes rouges ouvriers occupent les usines, Italie, septembre 1920 · Photographe inconnu, domaine public"),
        "br": dict(type="cols", g="Les années rouges · 1919 – 1920", gq="terres occupées, grèves, usines prises : « un 1917 italien » ?",
                   d="Les Chemises noires", dq="une répression violente, payée par les grands propriétaires", vs="→", repere="Biennio Rosso"),
        "tur": dict(type="note", terme="Exemple · Turin, 1920", cles=["grève", "usines", "réelle"],
                    t="La grève générale : les ouvriers occupent les usines et les font tourner eux-mêmes.",
                    etape="La peur était réelle → le fascisme, bras armé des possédants", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 5 : l'Allemagne, une république dans la violence
    dict(id="weimar", chap="I.1 · L'Allemagne : une république née dans la violence", fond="guerre", humeur="tension",
         retenir="1918 : la défaite met fin à l'Empire allemand → la république de Weimar. Janv. 1919 : le soulèvement spartakiste (Luxemburg, Liebknecht) échoue ; tous deux assassinés par les corps francs, 15 janv. 1919.",
         beats=[
        "{g5}{g5.1}Idée cinq : l'Allemagne. En mille neuf cent dix-huit, la défaite militaire met fin à l'Empire allemand. Un nouveau régime naît : "
        "la {!république de Weimar}république de Weimar.",
        "Mais dans les villes, des révolutionnaires veulent aller plus loin. {spa}{spa.1}En janvier mille neuf cent dix-neuf éclate le soulèvement {!spartakiste}spartakiste. "
        "C'est une révolte communiste, menée par Rosa Luxemburg et Karl Liebknecht. Ils veulent une révolution sur le modèle russe. "
        "{spa.2}Elle échoue. {spa.3}Le quinze janvier mille neuf cent dix-neuf, Luxemburg et Liebknecht sont assassinés par des soldats des corps francs, les Freikorps. "
        "Ce sont des volontaires armés, souvent d'anciens soldats.",
        "{-spa}{-g5}{photo4}{wr}Dans le cours, l'exemple est une barricade à Berlin, pendant le soulèvement. "
        "{wr.1}Dès ses premières semaines, la république est donc liée à deux choses. La défaite. Et le sang versé, des deux côtés.{-photo4}",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[3]),
        "spa": dict(type="liste", titre="Le soulèvement spartakiste", x=60, y=110, w=620, petit=True, bande=True, items=[
            "Janv. 1919 : Luxemburg et Liebknecht, une révolution sur le modèle russe", "Elle échoue",
            "15 janv. 1919 : tous deux assassinés par les corps francs"]),
        "photo4": dict(type="tableau", img="h2-spartacist", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Une barricade de rouleaux de papier journal pendant le soulèvement spartakiste, Berlin, janvier 1919 · Illustrirte Zeitung, domaine public"),
        "wr": dict(type="def", cles=["défaite", "sang"], terme="La république de Weimar · 1918",
                   t="Une république née de la défaite, dans la violence civile.",
                   etape="Liée dès ses premières semaines à la défaite et au sang versé des deux côtés", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 6 : Versailles et le coup de poignard
    dict(id="versailles", chap="I.1 · Le Diktat et le coup de poignard dans le dos", fond="nuit", humeur="tension",
         retenir="Versailles (1919), imposé et non négocié : clause de culpabilité, Alsace-Lorraine et territoires de l'Est perdus, réparations énormes → le « Diktat ». Le mythe du coup de poignard dans le dos : trahie de l'intérieur.",
         beats=[
        "{g6}{g6.1}Idée six : le traité de Versailles, en mille neuf cent dix-neuf. Il est imposé, pas négocié. Si l'Allemagne refuse de signer, elle sera envahie. "
        "{ver}{ver.1}Il contient la clause de culpabilité : l'Allemagne est tenue pour responsable de la guerre. "
        "{ver.2}Il lui enlève l'Alsace-Lorraine et les territoires de l'Est. {ver.3}Il lui impose des réparations énormes. "
        "{ver.4}Les Allemands l'appellent donc un {!Diktat}Diktat. Une paix dictée.",
        "{-ver}{-g6}{dol}Au même moment, les milieux militaires répandent une théorie du complot : le {!coup de poignard dans le dos}coup de poignard dans le dos. "
        "{dol.1}L'armée, disent-ils, n'a pas été battue au front. Elle a été trahie de l'intérieur.",
        "{-dol}{cp}Le cours montre une carte postale allemande de mille neuf cent dix-neuf. {cp.1}Un soldat est poignardé dans le dos par un Juif caricaturé. "
        "{cp.2}Le mythe accuse les démocrates, les pacifistes et les socialistes. Ou, comme ici, les Juifs. "
        "{cp.3}Il transforme la défaite en rancœur. Et il fournit à l'extrême droite des ennemis tout trouvés.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[5]),
        "ver": dict(type="liste", titre="Versailles, 1919 : un « Diktat »", x=60, y=110, w=620, petit=True, bande=True, items=[
            "La clause de culpabilité", "L'Alsace-Lorraine et les territoires de l'Est perdus", "Des réparations énormes",
            "Imposé, pas négocié : un « Diktat »"]),
        "dol": dict(type="def", cles=["battue", "trahie"], terme="Le mythe du coup de poignard dans le dos",
                    t="L'armée n'a pas été battue au front, mais trahie de l'intérieur.",
                    etape="Répandu par les milieux militaires dès 1919", x=170, y=200, w=940),
        "cp": dict(type="liste", titre="Exemple · une carte postale allemande, 1919", cles=["Juif", "ennemis"], items=[
            "Un soldat poignardé dans le dos par un Juif caricaturé",
            "Accusés : démocrates, pacifistes, socialistes, Juifs",
            "La défaite changée en rancœur ; des ennemis tout trouvés"], x=170, y=150, w=940),
    }),

    # ================================================================ I.1, idée 7 : le putsch de Munich
    dict(id="munich", chap="I.1 · Du putsch de Munich à la crise", fond="guerre", humeur="tension",
         retenir="Nov. 1923 : échec du coup de force de Hitler à Munich → la leçon : conquérir le pouvoir par les institutions. En prison : Mein Kampf (1924-1925). Puis la crise : « la guerre a créé les rancœurs ; la crise les a changées en voix ».",
         beats=[
        "{g7}{g7.1}Idée sept. La république de Weimar n'a jamais rallié ses ennemis. En novembre mille neuf cent vingt-trois, à Munich, "
        "Hitler tente de prendre le pouvoir par la force. C'est un échec.",
        "{-g7}{les}Il est envoyé en prison. Et il tire une leçon de son échec. {les.1}Le pouvoir doit se conquérir par les institutions. "
        "{!Pas contre elles}Pas contre elles. {les.2}En prison, il écrit Mein Kampf. Comme le note le cours, "
        "il y expose ses idées racistes dès mille neuf cent vingt-quatre et vingt-cinq.",
        "{-les}{cr}Puis viennent les années trente. La crise économique extrême du chapitre un donne à son parti l'audience de masse qui lui manquait. "
        "{cr.1}Voici une phrase à retenir, et à utiliser dans tes copies.",
        "{-cr}{phr}La guerre a créé les rancœurs. La crise les a changées en voix.",
        ("P", 2.0),
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[7]),
        "les": dict(type="cols", g="Nov. 1923 · le putsch manqué", gq="le pouvoir par la force, à Munich : un échec",
                    d="La leçon", dq="conquérir le pouvoir par les institutions · Mein Kampf, 1924-1925", vs="→"),
        "cr": dict(type="note", terme="Puis les années 1930", cles=["crise", "masse"],
                   t="La crise économique extrême (chapitre 1) donne au parti nazi l'audience de masse qui lui manquait.",
                   etape="Une phrase à retenir", x=170, y=200, w=940),
        "phr": dict(type="mot", t="Rancœurs → voix", g="La guerre a créé les rancœurs ; la crise les a changées en voix.",
                    y=250, taille=96),
    }),

    # ================================================================ schéma h2legacy
    dict(id="legacy", chap="Trois blessures de la guerre", fond="aube", humeur="calme",
         retenir="Russie : guerre → bolcheviks → parti unique, propriété abolie, peur du communisme. Italie : victoire mutilée → Fiume, Chemises noires → nationalisme armé. Allemagne : défaite, Diktat, coup de poignard → une république liée à la défaite.",
         beats=[
        "{bl}Voici le schéma du cours : trois blessures de la guerre. {bl.1}Commence par la blessure elle-même. En Russie, la guerre ruine l'empire des tsars. "
        "{bl.2}En Italie, elle laisse une victoire mutilée. {bl.3}En Allemagne, la défaite, la fin de l'Empire, et le Diktat.",
        "{-bl}{rp}Puis la réponse. {rp.1}En Russie, la révolution bolchevique. {rp.2}En Italie, Fiume, et les Chemises noires payées. "
        "{rp.3}En Allemagne, les spartakistes sont écrasés, et le mythe du coup de poignard se répand.",
        "{-rp}{lg}Et enfin, l'héritage. {lg.1}En Russie, un parti unique, et la peur du communisme. "
        "{lg.2}En Italie, un nationalisme armé. "
        "{lg.3}En Allemagne, une république liée à la défaite, et des ennemis tout trouvés.",
        "{-lg}{rem}Retiens-le donc. Partout, la guerre prépare le terrain : la violence, les rancœurs, la peur de la révolution. "
        "{rem.1}Mais elle ne décide pas encore quel régime y poussera.",
    ], vis={
        "bl": dict(type="cartes", petit=True, items=[
            dict(t="Russie", q="Blessure : la guerre ruine l'empire des tsars"),
            dict(t="Italie", q="Blessure : une « victoire mutilée », ni Fiume ni la Dalmatie"),
            dict(t="Allemagne", q="Blessure : la défaite, la fin de l'Empire, le Diktat")]),
        "rp": dict(type="cartes", petit=True, items=[
            dict(t="Russie", q="Réponse : la révolution bolchevique, oct. 1917"),
            dict(t="Italie", q="Réponse : D'Annunzio à Fiume ; Chemises noires payées par les propriétaires"),
            dict(t="Allemagne", q="Réponse : spartakistes écrasés ; le mythe du coup de poignard")]),
        "lg": dict(type="cartes", petit=True, items=[
            dict(t="Russie", q="Héritage : parti unique, propriété abolie, peur du communisme"),
            dict(t="Italie", q="Héritage : un nationalisme armé contre la peur de la révolution"),
            dict(t="Allemagne", q="Héritage : une république liée à la défaite ; des ennemis tout trouvés")]),
        "rem": dict(type="note", terme="À retenir", cles=["terrain", "décide"],
                    t="Partout, la guerre prépare le terrain : la violence, les rancœurs, la peur de la révolution.",
                    etape="Elle ne décide pas encore quel régime y poussera", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : un paragraphe de composition
    dict(id="essai1", chap="À toi · la guerre, une matrice", fond="aube", humeur="calme",
         retenir="Modèle : la brutalisation (Mosse, Hitler en 1915) · la peur de la révolution (bolcheviks, Biennio Rosso, Turin 1920) · les rancœurs (victoire mutilée, Diktat, coup de poignard) · nuance : le terrain, pas la cause (la crise).",
         beats=[
        "{ex1q}À toi. Voici un sujet de question problématisée. {!Explique}Explique comment la Première Guerre mondiale a préparé le terrain aux régimes totalitaires. "
        "Rédige un paragraphe, avec trois arguments, et un exemple précis pour chacun.",
        "{-ex1q}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod1}Voici un modèle. {mod1.1}La Première Guerre mondiale a préparé le terrain aux régimes totalitaires de trois façons. "
        "D'abord, elle a brutalisé les sociétés. Comme l'a montré George Mosse, quatre ans de massacres de masse ont banalisé la violence. "
        "Et des hommes comme Hitler, soldat en mille neuf cent quinze, l'ont ramenée dans la politique. "
        "{mod1.2}Ensuite, elle a fait naître la peur de la révolution. Les bolcheviks prennent le pouvoir en Russie en octobre mille neuf cent dix-sept. "
        "Et pendant le Biennio Rosso, les ouvriers italiens occupent les usines de Turin. Les grands propriétaires paient alors les Chemises noires pour les réprimer. "
        "{mod1.3}Enfin, elle a laissé de profondes rancœurs. En Italie, la victoire mutilée. En Allemagne, le Diktat de Versailles, et le mythe du coup de poignard dans le dos. "
        "{mod1.4}Mais la guerre n'a fait que préparer le terrain. En Allemagne, il a fallu la crise des années trente pour changer ces rancœurs en voix.",
    ], vis={
        "ex1q": dict(type="exo", niveau="essay", titre="Explique comment la Première Guerre mondiale a préparé le terrain aux régimes totalitaires.",
                     src="Sujet écrit pour cette vidéo, sur la partie I.1 du cours",
                     enonce=["Un paragraphe : trois arguments, un exemple précis pour chacun"]),
        "pa1": dict(type="pause", t="Question problématisée : comment la Grande Guerre a-t-elle préparé le terrain aux régimes totalitaires ?",
                    sous="Trois arguments, un exemple précis pour chacun. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "mod1": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "La brutalisation → George Mosse ; Hitler soldat en 1915",
            "La peur de la révolution → octobre 1917 ; Turin, 1920 ; Chemises noires payées par les propriétaires",
            "Les rancœurs → la victoire mutilée ; le Diktat ; le coup de poignard dans le dos",
            "Nuance : le terrain, pas la cause → la crise change les rancœurs en voix"], x=150, y=140, w=980),
    }),

    # ================================================================ I.2, idée 1 : les composantes du fascisme
    dict(id="fascisme", chap="I.2 · Le fascisme de Mussolini : ses composantes", fond="nuit", humeur="tension",
         retenir="Le fascisme : un parti en croissance + un chef (Mussolini) · un programme : « la loi et l'ordre » · un symbole : les faisceaux · des escouades (Chemises noires). Soutenu par propriétaires et commerçants terrifiés par le communisme.",
         beats=[
        "{fa}Première partie, point deux : la prise du pouvoir. Idée un. Le cours décompose le fascisme en ses composantes. "
        "{fa.1}Un parti à l'influence croissante, avec de plus en plus de partisans. Et un chef, Mussolini. "
        "{fa.2}Un programme qui séduit les électeurs : {!la loi et l'ordre}la loi et l'ordre. "
        "{fa.3}Un symbole. {fa.4}Et des escouades paramilitaires, menées par des chefs fascistes.",
        "{-fa}{fs}Le symbole donne son nom au mouvement. {fs.1}Le mot fasciste vient des {!faisceaux}faisceaux. "
        "Un faisceau, c'est un paquet de verges liées autour d'une hache, porté devant les magistrats de la Rome antique. Un objet de la Rome impériale.",
        "{-fs}{sup}Et qui soutient le fascisme ? {sup.1}Les propriétaires et les commerçants, terrifiés par le communisme. "
        "{sup.2}La loi et l'ordre, c'est à eux que ça parle.",
    ], vis={
        "fa": dict(type="liste", titre="Le fascisme : ses composantes", cles=["chef", "l'ordre", "symbole", "escouades"], items=[
            "Un parti en pleine croissance, et un chef : Mussolini", "Un programme : « la loi et l'ordre »", "Un symbole : les faisceaux",
            "Des escouades paramilitaires : les Chemises noires"], x=170, y=140, w=940),
        "fs": dict(type="def", cles=["verges", "hache", "Rome"], terme="Les faisceaux",
                   t="Un paquet de verges liées autour d'une hache, porté devant les magistrats romains.",
                   etape="Il donne au mouvement son nom et son emblème", x=170, y=200, w=940),
        "sup": dict(type="note", terme="Qui soutient le fascisme ?", cles=["propriétaires", "commerçants"],
                    t="Les propriétaires et les commerçants, terrifiés par le communisme après le Biennio Rosso.",
                    etape="« La loi et l'ordre » leur parle directement", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 2 : la marche sur Rome
    dict(id="marche", chap="I.2 · La marche sur Rome", fond="guerre", humeur="tension",
         retenir="Oct. 1922 : la marche sur Rome (≈ 20 000 Chemises noires, chiffre du cours). Une intimidation, pas un coup d'État : le roi refuse l'état de siège et nomme Mussolini chef du gouvernement le 30 oct. 1922.",
         beats=[
        "{g8}{g8.1}Idée deux. En octobre mille neuf cent vingt-deux, les Chemises noires marchent sur Rome. Mais Mussolini n'organise pas la marche "
        "pour prendre le pouvoir par les armes. {mr}{mr.1}Il l'organise pour pousser le roi à le nommer chef du gouvernement.",
        "{mr.2}Il ne vient que quelques milliers d'hommes. Environ vingt mille, selon le cours. Bien moins qu'il ne l'espérait. "
        "{mr.3}La plupart sont soupçonnés de meurtre. Ils ne sont pas violents pendant la marche. Mais chacun sait qu'ils pourraient l'être.",
        "{mr.4}Et la menace suffit. Le roi Victor-Emmanuel trois refuse de proclamer l'état de siège. Le trente octobre mille neuf cent vingt-deux, "
        "il nomme Mussolini chef du gouvernement.",
        "{-mr}{-g8}{photo5}{int}Retiens donc la formule. {!une intimidation, pas un coup d'État}Une intimidation, pas un coup d'État. "
        "{int.1}La menace de la violence a imposé une nomination légale. Dans le cours, Mussolini pose parmi ses chefs d'escouades : De Bono, Balbo et De Vecchi.",
        "{-int}{-photo5}{att1}Attention à deux détails. {att1.1}Le cours date la marche du vingt-deux au vingt-neuf octobre. "
        "Les historiens disent d'ordinaire du vingt-sept au trente et un. "
        "{att1.2}Et beaucoup d'estimations montent jusqu'à trente mille marcheurs. La réponse la plus sûre ? Octobre mille neuf cent vingt-deux, et quelque vingt mille Chemises noires.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[6]),
        "mr": dict(type="liste", titre="La marche sur Rome · octobre 1922", x=40, y=110, w=520, petit=True, bande=True, items=[
            "Le but : pousser le roi à le nommer", "≈ 20 000 Chemises noires, moins qu'espéré (chiffre du cours)",
            "Pas violents pendant la marche… mais redoutés", "30 oct. : le roi refuse l'état de siège, nomme Mussolini"]),
        "photo5": dict(type="tableau", img="h2-march-rome", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .35],
                       legende="Mussolini et les quatre quadrumvirs de la marche sur Rome, 1922, tableau commémoratif · Photo Silvio Galimberti, CC BY-SA 4.0"),
        "int": dict(type="def", cles=["menace", "légale"], terme="Une intimidation, pas un coup d'État",
                    t="La menace de la violence a imposé une nomination légale.",
                    etape="Cours : Mussolini avec De Bono, Balbo et De Vecchi", x=170, y=200, w=940),
        "att1": dict(type="note", terme="Attention · dates et chiffres", cles=["d'ordinaire", "estimations"],
                     t="Cours : 22-29 oct. 1922. D'ordinaire : 27-31 oct. Cours : ≈ 20 000 ; autres estimations : 25 000 à 30 000.",
                     etape="Le plus sûr dans une copie : octobre 1922, quelque 20 000 Chemises noires", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 3 : le nazisme, mêmes composantes
    dict(id="nazisme", chap="I.2 · Le nazisme de Hitler : les mêmes composantes", fond="nuit", humeur="tension",
         retenir="Le nazisme : NSDAP + un chef (Hitler) · Mein Kampf : abolir Versailles, unir Allemagne et Autriche, nationaliser les grandes industries, exclure les Juifs · la croix gammée · la SA et la SS. Ce qui le distingue du fascisme : la race.",
         beats=[
        "{pg}Idée trois. Le nazisme de Hitler a les mêmes composantes. {pg.1}Un parti à l'influence croissante, le parti nazi. Et un chef, Hitler. "
        "{pg.2}Un programme, fondé sur Mein Kampf. Il prévoit d'abolir le traité de Versailles. "
        "{pg.3}D'unir l'Allemagne et l'Autriche. {pg.4}De nationaliser les grandes industries et les grandes entreprises. "
        "{pg.5}Et d'exclure les Juifs de la société allemande.",
        "{-pg}{hk}Un point hors du cours. Ces revendications figuraient déjà dans le programme en vingt-cinq points du parti, en mille neuf cent vingt. "
        "{hk.1}Mein Kampf les développe.",
        "{-hk}{sw}Le symbole, c'est la {!croix gammée}croix gammée noire. {sw.1}Un signe ancien, longtemps vu comme un porte-bonheur. Les nazis en font un signe aryen. "
        "{sw.2}Certaines fiches de révision disent qu'elle a été choisie sans raison particulière. En réalité, Hitler explique son symbolisme dans Mein Kampf. "
        "{sw.3}Et les organisations paramilitaires sont la SA et la SS.",
        "{-sw}{tb}Voici donc le tableau du cours. Deux mouvements, les mêmes composantes. {tb.g}Le fascisme d'un côté. "
        "{tb.d}Le nazisme de l'autre.",
        "{-tb}{dif}Deux choses à ajouter. {dif.1}Mussolini arrive au pouvoir onze ans avant Hitler. Pour le cours, le fascisme est donc le premier totalitarisme. "
        "{dif.2}Et qu'est-ce qui sépare les deux mouvements ? La {!race}race. Elle est au cœur du programme nazi, dès Mein Kampf.",
    ], vis={
        "pg": dict(type="liste", titre="Le nazisme : parti, chef, programme", cles=["Versailles", "Autriche", "nationaliser", "exclure"], items=[
            "Le NSDAP, et un chef : Hitler", "Programme (Mein Kampf) : abolir Versailles", "Unir l'Allemagne et l'Autriche",
            "Nationaliser les grandes industries et entreprises", "Exclure les Juifs de la société allemande"], x=170, y=110, w=940),
        "hk": dict(type="note", terme="Hors du cours", cles=["1920", "développe"],
                   t="Ces revendications figuraient déjà dans le programme en 25 points du parti, en février 1920.",
                   etape="Mein Kampf (1924-1925) les développe", x=170, y=200, w=940),
        "sw": dict(type="liste", titre="Symbole et paramilitaires", items=[
            "La croix gammée noire : un signe ancien, rendu « aryen » par les nazis",
            "Nuance : Hitler explique son symbolisme dans Mein Kampf", "La SA et la SS"], x=170, y=150, w=940),
        "tb": dict(type="cols", g="Le fascisme de Mussolini", gq="Parti national fasciste, Mussolini · « la loi et l'ordre » · les faisceaux · les Chemises noires",
                   d="Le nazisme de Hitler", dq="NSDAP, Hitler · Mein Kampf · la croix gammée · la SA et la SS", vs="=",
                   repere="Deux mouvements, les mêmes composantes"),
        "dif": dict(type="liste", titre="Ce que dit aussi le tableau", cles=["premier", "race"], items=[
            "Mussolini au pouvoir onze ans avant Hitler : le fascisme, « le premier totalitarisme »",
            "Ce qui les sépare : la race, au cœur du nazisme dès Mein Kampf"], x=170, y=170, w=940),
    }),

    # ================================================================ I.2, idée 4 : la SA et la SS
    dict(id="rue", chap="I.2 · Conquérir la rue : la SA et la SS", fond="guerre", humeur="tension",
         retenir="SA : une force de masse, des hommes sans emploi et peu instruits, certains avec un casier judiciaire ; bagarres de rue avec les communistes. SS : une élite sélectionnée, plus instruite. La violence comme outil de conquête.",
         beats=[
        "{photo6}{sa}Idée quatre. Le mouvement nazi a deux bras armés. {sa.g}D'abord, la {!SA}SA, les sections d'assaut. C'est une force de masse. "
        "La plupart sont des hommes sans emploi et peu instruits, et certains ont un casier judiciaire. "
        "Ils se battent contre les communistes dans la rue, et protègent les réunions nazies. "
        "{sa.d}Ensuite, la SS. C'est une élite : sélectionnée, plus instruite, et souvent issue de milieux plus aisés.",
        "{-sa}{ord}Voici un ordre de grandeur, hors du cours. En mille neuf cent trente-trois, la SA compte plusieurs centaines de milliers d'hommes. "
        "{ord.1}C'est plusieurs fois l'armée que le traité de Versailles laissait à l'Allemagne : cent mille hommes.",
        "{-ord}{-photo6}{vio}La violence n'est donc pas un effet secondaire du nazisme. C'est {!un outil de conquête}un outil de conquête.",
    ], vis={
        "photo6": dict(type="tableau", img="h2-unemployed-sa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Des SA sans emploi sur un banc à Berlin, 1932 · Bundesarchiv, Bild 146-1985-054-02, CC BY-SA 3.0 DE"),
        "sa": dict(type="cols", g="La SA · les sections d'assaut", gq="une force de masse : hommes sans emploi, peu instruits ; bagarres de rue, réunions protégées",
                   d="La SS", dq="une élite : sélectionnée, plus instruite, souvent plus aisée", vs="+"),
        "ord": dict(type="note", terme="Hors du cours · un ordre de grandeur", cles=["centaines", "Versailles"],
                    t="En 1933, la SA compte plusieurs centaines de milliers d'hommes.",
                    etape="Plusieurs fois l'armée de 100 000 hommes permise par Versailles", x=170, y=200, w=940),
        "vio": dict(type="question", t="La violence : pas un effet secondaire, un outil de conquête."),
    }),

    # ================================================================ I.2, idée 5 : la crise et le vote nazi
    dict(id="crise", chap="I.2 · La crise et le vote nazi", fond="nuit", humeur="tension",
         retenir="Chômage ≈ 5,6 millions (1932). NSDAP : 2,6 % (mai 1928) → 18,3 % (sept. 1930) → 37,4 % (juillet 1932, premier parti) → 33,1 % (nov. 1932). Jamais la majorité à une élection libre.",
         beats=[
        "{g9}{g9.1}Idée cinq. La crise a fait des nazis, parti marginal, le premier parti d'Allemagne. "
        "Le cours montre des chômeurs qui font la queue pour une aide alimentaire, à Hanovre, en mille neuf cent trente-deux.",
        "{-g9}{gu}Regarde d'abord le chômage en Allemagne, sur le graphique du cours. {gu.1}Dans les années vingt, il reste autour de deux millions au plus. "
        "{gu.2}Puis la crise frappe. En mille neuf cent trente-deux, environ cinq virgule six millions d'Allemands sont sans travail.",
        ("P", 2.5),
        "{-gu}{gv}Maintenant, le vote nazi. {gv.1}Cette ligne rouge, c'est la majorité : cinquante pour cent. "
        "{gv.2}En mai mille neuf cent vingt-huit, avant la crise, les nazis sont un parti marginal : deux virgule six pour cent. {gv.3}{gv.4}En septembre mille neuf cent trente, dix-huit virgule trois. "
        "{gv.5}En juillet mille neuf cent trente-deux, trente-sept virgule quatre pour cent. Ils forment désormais le premier groupe du Reichstag.",
        "{gv.6}Mais en novembre mille neuf cent trente-deux, ils reculent : trente-trois virgule un pour cent.",
        "{-gv}{maj}Et voici le point essentiel. {maj.1}Les nazis n'ont jamais obtenu la majorité à une élection libre. "
        "{maj.2}Hitler n'est pas arrivé au pouvoir parce que la plupart des Allemands ont voté pour lui. "
        "{maj.3}Il a été nommé le trente janvier mille neuf cent trente-trois. Et son parti perdait alors des voix.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[16]),
        "gu": dict(type="graphe", titre="Chômeurs en Allemagne, en millions (graphique du cours, arrondi)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1920.5, 1932.8], y=[0, 6.5], gx=[1922, 1924, 1926, 1928, 1930, 1932], gy=[1, 2, 3, 4, 5, 6],
                           lx="année", ly="millions"),
                   el=[dict(type="courbe", pts=CHOMAGE[:9], c="iv2", lbl="les années 1920", lp=[1924.5, 2.3], dur=2.0),
                       dict(type="courbe", pts=CHOMAGE[8:], c="ca", lbl="1932 : ≈ 5,6 millions", lp=[1929.6, 5.8], dur=1.6)]),
        "gv": dict(type="graphe", titre="Le vote NSDAP aux élections au Reichstag (graphique du cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 60], gx=[1928, 1930, 1932], gy=[10, 20, 30, 40, 50], lx="année", ly="%"),
                   el=[dict(type="droite", pts=[[1927.6, 50], [1933.4, 50]], c="rouge", tir=True, ep=2.4,
                            lbl="majorité : 50 %", lp=[1929.3, 53.5]),
                       dict(type="point", x=1928.4, y=2.6, c="sa", lbl="2,6 %", lp=[1928.4, 10]),
                       dict(type="courbe", pts=VOTE[:2], c="sa", dur=1.2),
                       dict(type="point", x=1930.7, y=18.3, c="sa", lbl="18,3 %", lp=[1930.4, 26]),
                       dict(type="courbe", pts=VOTE[1:3], c="sa", lbl="37,4 %", lp=[1932.0, 45], dur=1.2),
                       dict(type="courbe", pts=VOTE[2:], c="ca", lbl="33,1 %", lp=[1933.05, 29], dur=1.0)]),
        "maj": dict(type="liste", titre="Jamais la majorité", cles=["libre", "majorité", "perdait"], items=[
            "Aucune majorité à une élection libre", "Pas porté au pouvoir par une majorité d'Allemands",
            "Nommé le 30 janv. 1933, alors que son parti perdait des voix"], x=170, y=150, w=940),
    }),

    # ================================================================ I.2, idée 6 : la nomination légale
    dict(id="nomination", chap="I.2 · Une nomination légale", fond="guerre", humeur="tension",
         retenir="30 janv. 1933 : le président Hindenburg, vieux général de l'Empire, nomme Hitler chancelier. Les conservateurs croient pouvoir le contrôler. Potsdam, mars 1933 : Hitler s'incline devant Hindenburg.",
         beats=[
        "{g10}{g10.1}Idée six. Comme Mussolini, Hitler n'a pas pris le pouvoir par un coup d'État. Le trente janvier mille neuf cent trente-trois, il est nommé chancelier "
        "par le président de la République, Paul von Hindenburg.",
        "{-g10}{hb}Qui est Hindenburg ? {hb.1}Un vieux général de l'Empire, qui a soutenu la monarchie. "
        "{hb.2}Les conservateurs qui l'entourent croient pouvoir contrôler Hitler, une fois au gouvernement. "
        "{hb.3}La façade légale permet aux nazis de démanteler la république {!de l'intérieur}de l'intérieur.",
        "{-hb}{photo7}{pot}Une photographie ouvre cette partie du cours, et elle montre exactement cela. {pot.1}Hitler s'incline pour saluer Hindenburg, à Potsdam. "
        "La date, le vingt et un mars mille neuf cent trente-trois, est hors du cours. "
        "{pot.2}L'image veut présenter le nazisme comme l'héritier du vieil ordre prussien.{-photo7}",
    ], vis={
        "g10": dict(type="globe", code="H2", sc=[20]),
        "hb": dict(type="liste", titre="Pourquoi les élites le laissent entrer", cles=["monarchie", "contrôler", "façade"], items=[
            "Hindenburg : un vieux général de l'Empire, monarchiste", "Les conservateurs : « nous pourrons le contrôler »",
            "Une façade légale : la république démantelée de l'intérieur"], x=170, y=150, w=940),
        "photo7": dict(type="tableau", img="h2-potsdam", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.15, .5, .4],
                       legende="Hitler s'incline devant Hindenburg, Potsdam, 21 mars 1933 · Bundesarchiv, Bild 183-S38324, CC BY-SA 3.0 DE"),
        "pot": dict(type="note", terme="Exemple · Potsdam, 21 mars 1933", cles=["incline", "héritier"],
                    t="Hitler s'incline pour saluer le président Hindenburg : le nazisme en héritier du vieil ordre prussien.",
                    etape="La photographie ouvre cette partie du cours · date exacte hors du cours", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 7 : l'incendie du Reichstag
    dict(id="reichstag", chap="I.2 · L'incendie du Reichstag", fond="nuit", humeur="tension",
         retenir="27 févr. 1933 : incendie du Reichstag ; les nazis accusent les communistes. Le lendemain, un décret suspend les libertés de presse, de réunion et d'opinion ; des milliers de communistes arrêtés. L'auteur reste débattu ; l'usage compte.",
         beats=[
        "{g11}{g11.1}Idée sept. Le vingt-sept février mille neuf cent trente-trois, un mois après la nomination de Hitler, le parlement allemand est incendié. Le Reichstag.",
        "{rf}{rf.1}Les nazis accusent aussitôt les communistes. Ils prétendent que l'incendie est le signal d'une révolution. "
        "{rf.2}Hitler et Hindenburg s'en servent pour frapper le communisme. Dès le lendemain, Hindenburg signe un décret. Cette date est hors du cours. "
        "Il suspend la liberté de la presse, de réunion et d'opinion. "
        "{rf.3}En quelques jours, des milliers de communistes sont arrêtés.",
        "{-rf}{-g11}{qui}Qui a mis le feu ? On en débat encore. Peut-être les nazis eux-mêmes. "
        "{qui.1}{!Ce qui compte}Mais ce qui compte, c'est l'usage qu'en fait le régime. Suspendre les libertés, et écraser ses premiers ennemis.",
    ], vis={
        "g11": dict(type="globe", code="H2", sc=[21]),
        "rf": dict(type="liste", titre="27 février 1933 → l'état d'urgence", x=770, y=110, w=480, petit=True, bande=True, items=[
            "Les nazis accusent les communistes : « une révolution »",
            "28 févr. : un décret suspend presse, réunion, opinion (date hors du cours)",
            "Des milliers de communistes arrêtés en quelques jours"]),
        "qui": dict(type="note", terme="Qui a mis le feu ?", cles=["débat", "usage"],
                    t="On en débat encore, peut-être les nazis eux-mêmes. Ce qui compte, c'est l'usage qu'en fait le régime.",
                    etape="Un état d'urgence → libertés suspendues, communistes écrasés", x=170, y=200, w=940),
    }),

    # ================================================================ schéma h2seizure : deux chemins vers le pouvoir
    dict(id="seizure", chap="Deux chemins vers le pouvoir", fond="aube", humeur="calme",
         retenir="Italie : escouades → marche sur Rome → le roi (oct. 1922) → lois fascistissimes. Allemagne : putsch raté (1923) → 37,4 % → Hindenburg (30 janv. 1933) → Reichstag. Commun : violence + nomination légale + élites. Différence : le rythme.",
         beats=[
        "{it}Comparons maintenant les deux chemins vers le pouvoir, avec le schéma du cours. La rue menace. Le sommet nomme. "
        "{it.1}En Italie, d'abord les escouades payées. {it.2}Puis la marche sur Rome. {it.3}Puis la nomination par le roi. "
        "{it.4}Et ensuite, l'assassinat de Matteotti et les lois fascistissimes. Ce sera pour l'épisode trois.",
        "{al}{al.1}En Allemagne, d'abord le putsch manqué. {al.2}Puis le vote de la crise. "
        "{al.3}Puis la nomination par Hindenburg. {al.4}Et ensuite, l'incendie du Reichstag, et le décret d'urgence. Lis les deux colonnes côte à côte.",
        ("P", 3.0),
        "{-it}{-al}{cd}Alors, qu'ont-ils en commun ? Et qu'est-ce qui diffère ? {cd.g}En commun : la violence paramilitaire, une nomination légale par le chef de l'État, "
        "et le soutien des élites conservatrices. {cd.d}La différence, c'est le rythme. Mussolini met deux à trois ans à bâtir sa dictature. "
        "Hitler, quelques semaines.",
    ], vis={
        "it": dict(type="liste", titre="Italie · Mussolini", petit=True, x=40, y=110, w=580, items=[
            "1919-1920 · peur des occupations ; escouades payées", "22-29 oct. 1922 · marche sur Rome (≈ 20 000)",
            "30 oct. 1922 · le roi le nomme", "1924-1926 · Matteotti → lois fascistissimes"]),
        "al": dict(type="liste", titre="Allemagne · Hitler", petit=True, x=660, y=110, w=580, items=[
            "Nov. 1923 · putsch manqué à Munich", "1930-1932 · la crise : 18,3 % → 37,4 %",
            "30 janv. 1933 · Hindenburg le nomme", "27-28 févr. 1933 · Reichstag → décret d'urgence"]),
        "cd": dict(type="cols", g="En commun", gq="violence paramilitaire + nomination légale par le chef de l'État + élites conservatrices",
                   d="La différence", dq="le rythme : 2 à 3 ans pour Mussolini, quelques semaines pour Hitler", vs="≠",
                   repere="La rue menace, le sommet nomme"),
    }),

    # ================================================================ à toi : « Dans quelle mesure… légalement ? »
    dict(id="essai2", chap="À toi · dans quelle mesure légalement ?", fond="aube", humeur="calme",
         retenir="Légal dans la forme (Hindenburg, 30 janv. 1933 ; 37,4 % ; la leçon de 1923) · mais préparé et achevé par la violence (SA, incendie du Reichstag, décret, arrestations), jamais majoritaire · bilan : légal dans la forme, pas démocratique.",
         beats=[
        "{ex2}À toi de nouveau. Cette fois, un sujet qui demande de mesurer. {!Dans quelle mesure}Dans quelle mesure Hitler est-il arrivé au pouvoir légalement ? "
        "{ex2.1}Pour ce type de sujet, tu pèses le pour et le contre. Puis tu donnes un bilan clair.",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod2}Voici un modèle. {mod2.1}Pour l'essentiel, Hitler est arrivé au pouvoir légalement. Après l'échec du putsch de Munich en mille neuf cent vingt-trois, "
        "il a choisi les institutions. En juillet mille neuf cent trente-deux, son parti obtient trente-sept virgule quatre pour cent des voix, et devient le premier parti du Reichstag. "
        "Puis, le trente janvier mille neuf cent trente-trois, le président Hindenburg le nomme chancelier, comme la constitution le permet.",
        "{mod2.2}Cependant, ce chemin légal a été préparé par la violence, puisque la SA se battait contre les communistes dans la rue. "
        "Et il n'a jamais reposé sur une majorité. En novembre mille neuf cent trente-deux, le vote nazi retombe à trente-trois virgule un pour cent. "
        "{mod2.3}Une fois au pouvoir, Hitler se sert de l'incendie du Reichstag pour suspendre les libertés, et faire arrêter des milliers de communistes. "
        "{mod2.4}Sa nomination était donc légale dans la forme. Mais elle n'était pas démocratique. Et la façade légale a servi à détruire la république de l'intérieur.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Dans quelle mesure Hitler est-il arrivé au pouvoir légalement ?",
                    src="Sujet écrit pour cette vidéo, sur la partie I.2 du cours",
                    enonce=["Peser le pour et le contre, puis donner un bilan clair"]),
        "pa2": dict(type="pause", t="Dans quelle mesure Hitler est-il arrivé au pouvoir légalement ?",
                    sous="Le pour, le contre, un bilan. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "mod2": dict(type="liste", titre="Un modèle de réponse", petit=True, items=[
            "Pour l'essentiel légal : la leçon de 1923 ; 37,4 % en juillet 1932 ; nommé par Hindenburg le 30 janv. 1933",
            "Mais : la violence de la SA ; jamais la majorité (33,1 % en nov. 1932) ; les élites conservatrices",
            "Puis : l'incendie du Reichstag → libertés suspendues, communistes arrêtés",
            "Bilan : légal dans la forme, pas démocratique ; une façade pour détruire la république"], x=150, y=140, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}La guerre a été une matrice. La brutalisation, selon le mot de Mosse, a ramené la violence dans la politique. "
        "{carte.2}Elle a laissé trois blessures. En Russie, la révolution bolchevique, et la peur rouge. En Italie, la victoire mutilée, et les années rouges. "
        "En Allemagne, la défaite, le Diktat, et le coup de poignard dans le dos. "
        "{carte.3}Mussolini avait un parti, la loi et l'ordre, les faisceaux et les Chemises noires. La marche sur Rome fut une intimidation, pas un coup d'État. "
        "{carte.4}Et Hitler ? La leçon de mille neuf cent vingt-trois. La SA et la SS. La crise, et trente-sept virgule quatre pour cent. "
        "La nomination légale du trente janvier mille neuf cent trente-trois. Et l'incendie du Reichstag.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : trois régimes, trois idéologies. La nation. La classe. La race.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="DE LA GUERRE AU POUVOIR", branches=[
            dict(t="La guerre, une matrice", items=["brutalisation (Mosse)", "Hitler soldat, 1915", "la violence en politique"]),
            dict(t="Trois blessures", items=["Russie : oct. 1917, peur rouge", "Italie : victoire mutilée", "Allemagne : Diktat, coup de poignard"]),
            dict(t="Mussolini", items=["la loi et l'ordre · faisceaux", "Chemises noires, propriétaires", "marche sur Rome, oct. 1922"]),
            dict(t="Hitler", items=["putsch de 1923 → institutions", "37,4 % · jamais la majorité", "30 janv. 1933 · Reichstag"])]),
        "fin": dict(type="mot", t="Prochain épisode : trois régimes, trois idéologies", g="Épisode 3 · nation, classe, race", y=270, taille=60),
    }),
]

QUIZ = [
    dict(q="Qu'entend George Mosse par « brutalisation » ?",
         r=["La guerre a banalisé la violence, et les soldats l'ont ramenée dans la politique", "Les conditions brutales du traité de Versailles",
            "La répression des spartakistes", "La terreur bolchevique en Russie"], ok=0, voir="def1",
         ex="Pour Mosse, la Grande Guerre est la « matrice du totalitarisme » : uniformes, grades, défilés, mépris de la vie humaine."),
    dict(q="Quelle est la différence entre la peur rouge et la Terreur rouge ?",
         r=["La peur rouge est la crainte du communisme à l'Ouest ; la Terreur rouge, la violence bolchevique en Russie même",
            "C'est la même chose", "La peur rouge désigne les purges de Staline", "La Terreur rouge désigne le Biennio Rosso"], ok=0, voir="mots1",
         ex="Le marxisme des bolcheviks signifiait la fin de la propriété privée : il effrayait l'Europe."),
    dict(q="Qui paie les Chemises noires pendant le Biennio Rosso ?",
         r=["Les grands propriétaires", "Le roi", "Le Parti socialiste", "Les ouvriers de Turin"], ok=0, voir="br",
         ex="Le fascisme a grandi comme le bras armé des possédants effrayés."),
    dict(q="Que prétend le mythe du coup de poignard dans le dos ?",
         r=["L'armée allemande n'a pas été battue au front, mais trahie de l'intérieur", "L'Allemagne a commencé la guerre",
            "Les spartakistes ont gagné en 1919", "L'Italie a trahi l'Allemagne"], ok=0, voir="dol",
         ex="Il accusait les démocrates, les pacifistes, les socialistes ou les Juifs, comme sur la carte postale allemande de 1919."),
    dict(q="Quelle leçon Hitler tire-t-il de l'échec du putsch de Munich en 1923 ?",
         r=["Le pouvoir doit se conquérir par les institutions", "Il faut un coup d'État plus grand",
            "Le parti doit s'allier aux communistes", "Il doit quitter la politique"], ok=0, voir="les",
         ex="En prison, il écrit Mein Kampf (1924-1925), où il expose ses idées racistes."),
    dict(q="Comment Mussolini arrive-t-il au pouvoir en octobre 1922 ?",
         r=["Par l'intimidation : la menace de la marche sur Rome pousse le roi à le nommer", "En gagnant la majorité aux élections",
            "Par un coup d'État armé qui prend Rome", "Après l'abdication du roi"], ok=0, voir="int",
         ex="Le roi Victor-Emmanuel III refuse l'état de siège et le nomme chef du gouvernement le 30 octobre 1922."),
    dict(q="Quel est le meilleur score du NSDAP à une élection libre ?",
         r=["37,4 % en juillet 1932", "51 % en novembre 1932", "18,3 % en septembre 1930", "2,6 % en mai 1928"], ok=0, voir="gv",
         ex="Le premier parti, mais jamais la majorité ; il retombe à 33,1 % en novembre 1932."),
    dict(q="Que font les nazis après l'incendie du Reichstag du 27 février 1933 ?",
         r=["Ils accusent les communistes, suspendent les libertés et arrêtent des milliers de communistes", "Ils organisent de nouvelles élections libres",
            "Ils arrêtent les chefs de la SA", "Ils rétablissent la monarchie"], ok=0, voir="rf",
         ex="Qui a mis le feu reste débattu : ce qui compte, c'est l'usage qu'en fait le régime."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », parties I.1 « L'héritage de la Première Guerre mondiale » et I.2 « La prise du pouvoir », avec les schémas « Trois blessures de la guerre », « Deux mouvements, les mêmes composantes », « La fin de Weimar » (valeurs du chômage lues sur le graphique du cours, arrondies) et « Deux chemins vers le pouvoir », tel qu'il est rédigé sur le site ; carte animée du chapitre (site).",
    "Points à manier avec soin (vérifications du site) : peur rouge et Terreur rouge ; la marche sur Rome datée d'ordinaire du 27 au 31 octobre 1922, avec des estimations allant jusqu'à 25 000 à 30 000 marcheurs ; Hitler explique la croix gammée dans Mein Kampf.",
    "Ajouté hors du cours : le programme en 25 points de 1920 ; les effectifs de la SA en 1933 ; la date de la cérémonie de Potsdam (21 mars 1933) et du décret d'urgence (28 février 1933).",
    "Photographies (via Wikimedia Commons) : la cathédrale d'Ypres en ruines, 1917 (Henry Armytage Sanders, Archives New Zealand, CC BY-SA 2.0) ; une barricade spartakiste, Berlin, janvier 1919 (Illustrirte Zeitung, domaine public) ; des gardes rouges occupant les usines, Italie, 1920 (photographe inconnu, domaine public) ; des SA sans emploi, Berlin, 1932 (Bundesarchiv, Bild 146-1985-054-02, CC BY-SA 3.0 DE) ; Hitler et Hindenburg à Potsdam, 21 mars 1933 (Bundesarchiv, Bild 183-S38324, CC BY-SA 3.0 DE).",
    "Tableaux : Lénine à l'usine Poutilov, mai 1917, par Isaak Brodsky, 1929 (domaine public) ; Mussolini et les quadrumvirs de la marche sur Rome, tableau commémoratif d'un artiste inconnu (photographie Silvio Galimberti, CC BY-SA 4.0).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
