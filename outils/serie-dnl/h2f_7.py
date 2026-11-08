"""Histoire · H2 « Les régimes totalitaires » — édition française, épisode 7 : « L'apaisement et la marche à la guerre »
(parties III.2 « Des démocraties incapables d'arrêter les régimes totalitaires » et III.3 « La marche à la Seconde Guerre mondiale »).

Traduction adaptée de h2_7.py, d'après outils/serie-dnl/EDITION_FR.md : mêmes scènes, mêmes identifiants, mêmes repères,
mêmes globe (carte animée H2, mêmes numéros de scènes : la carte passe d'elle-même en français), mêmes images.
Les deux DBQ de l'édition anglaise deviennent des analyses de document (présentation, contexte, explication, intérêt et
limites, bilan critique) ; la partie b) du DBQ 3 devient une réponse à une question problématisée, écrite pour la vidéo
sur la problématique du chapitre. Aucun barème.
Hors cours, dit comme tel : Guernica (exemple complémentaire, que le cours signale lui-même comme hors de la leçon), la part
des Juifs dans la population autrichienne (environ 3 %). Corrections reprises de l'édition anglaise : « un Congrès
républicain » → « un Congrès isolationniste » ; Anschluss : les 8 % du cours sont la part des exclus du vote (opposants et
Juifs ensemble) ; les « 700 000 officiers » de la caricature de Staline : chiffre de caricature, le cours donne 680 000
exécutions pour toute la Grande Purge ; le discours de l'Obersalzberg (22 août) dix jours avant l'invasion de la Pologne.
Citations : traductions françaises fidèles des textes cités par le cours (Oxford Union, Low, Mussolini, Roosevelt, Hitler,
caricature de Staline) ; sources affichées.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-7"
NOTION = "Les régimes totalitaires"
NUM = 7
TITRE = "L'apaisement et la marche à la guerre"
SUIVANT = "Épisode 8 · Le totalitarisme à l'épreuve : question problématisée et analyse de document"
PRONONCIATION = {"Anschluss": "Ann-chlouss", "Wehrmacht": "Vèr-markt", "Kriegsmarine": "Krigs-marine",
                 "Luftwaffe": "Louft-vaffe", "Heer": "Hère", "Schuschnigg": "Chouch-nig", "Seyss-Inquart": "Zaïss-Inn-kvart",
                 "Obersalzberg": "Obeur-zalts-bèrg", "Stresa": "Stréza", "Lebensraum": "Lé-benss-raoum",
                 "Krampus": "Kramm-pouss", "Chamberlain": "Tchèm-beur-line", "Neville": "Névil", "Roosevelt": "Rouzvelt",
                 "Royal Navy": "Roï-al Né-vi", "Mein Kampf": "Maïn Kammpf", "Low": "Lô", "Commonwealth": "Ko-mmonn-ouèls",
                 "Oxford Union": "Oxford Iou-nieune", "Ribbentrop": "Ribbène-trop"}


def marches(etapes):
    """L'escalier de Low (schéma h1slide) : pour chaque marche, une barre épaisse qui monte d'un cran (l'année en haut),
    puis le nom en dessous de l'axe. Les extrémités arrondies (ep 60 px) sont rentrées de 0,75 unité pour partir de
    l'axe. La dernière marche (la Pologne) est en rouge."""
    el = []
    for i, (an, nom) in enumerate(etapes, start=1):
        h_ = i + 1
        c = "ca" if i == len(etapes) else "sa"
        el.append(dict(type="droite", pts=[[i, 0.75], [i, h_ - 0.75]], c=c, ep=60, dur=0.8, lbl=an, lp=[i, h_ + 0.45]))
        el.append(dict(type="texte", x=i, y=-0.75, t=nom, c="iv"))
    return el


MARCHES = [("1931", "Mandchourie"), ("1935", "Éthiopie"), ("1936", "Rhénanie"), ("1938", "Anschluss"),
           ("1938", "Munich"), ("1939", "Prague"), ("1939", "Pologne")]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Le premier septembre mille neuf cent trente-neuf. Les troupes allemandes entrent en Pologne. "
        "Deux jours plus tard, la France et le Royaume-Uni déclarent la guerre. Vingt et un ans après la Grande Guerre, l'Europe se bat de nouveau.",
        "{q1}Depuis mille neuf cent trente-cinq, Hitler viole sans cesse le traité de Versailles. Pourquoi personne ne l'a-t-il arrêté ?",
        "{-q1}{q2}Et derrière, il y a la question de tout le chapitre. L'idéologie totalitaire a-t-elle causé la guerre ?",
        "{-q2}{-g0}{plan}Aujourd'hui, la dernière partie du chapitre. {plan.1}D'abord, l'histoire sur la carte, de mille neuf cent trente-cinq à mille neuf cent trente-neuf. "
        "{plan.2}Puis la partie trois point deux : des démocraties incapables d'arrêter les régimes totalitaires. Autrement dit, l'apaisement. "
        "{plan.3}Puis la partie trois point trois : la marche à la Seconde Guerre mondiale, étape par étape. "
        "{plan.4}Puis l'épreuve : deux analyses de document, dont une que tu rédigeras toi-même. {plan.5}Et enfin, la réponse à la question du chapitre.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[37]),
        "q1": dict(type="question", t="Pourquoi personne ne l'a-t-il arrêté ?", bande=True),
        "q2": dict(type="question", t="L'idéologie totalitaire a-t-elle causé la guerre ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 7 · le plan", items=[
            "La marche à la guerre sur la carte, 1935-1939", "III.2 · Des démocraties incapables d'arrêter les régimes totalitaires",
            "III.3 · La marche à la guerre, étape par étape", "À l'épreuve : deux analyses de document, dont une à rédiger",
            "L'idéologie totalitaire a-t-elle causé la guerre ?"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 7", t="L'apaisement et la marche à la guerre",
                      sous="1935 – 1939 · Parties III.2 et III.3 du cours"),
    }),

    # ================================================================ la carte : 1935-1936
    dict(id="carte1", chap="Sur la carte : 1935 – 1936", fond="nuit", humeur="tension",
         retenir="Avril 1935 Stresa · 1935 la Wehrmacht · juin 1935 l'accord naval · 7 mars 1936 la Rhénanie · 25 oct. 1936 l'Axe Rome-Berlin · 1936 la guerre d'Espagne.",
         beats=[
        "{g1}{g1.1}Mille neuf cent trente-cinq. À Stresa, le Royaume-Uni et la France tentent de former un front avec l'Italie, contre l'Allemagne. "
        "Mais l'Allemagne réarme ouvertement. Et en juin, le Royaume-Uni signe seul avec elle un accord naval. "
        "De l'autre côté de l'Atlantique, les États-Unis votent leurs lois de neutralité.",
        "{g1.2}Le sept mars mille neuf cent trente-six, les troupes allemandes entrent dans la Rhénanie démilitarisée. "
        "La France ne réagit pas. Le Royaume-Uni non plus.",
        "{g1.3}À l'été mille neuf cent trente-six, la guerre civile éclate en Espagne. L'Allemagne et l'Italie soutiennent le général Franco. "
        "La France et le Royaume-Uni restent à l'écart. Et le vingt-cinq octobre, l'Allemagne et l'Italie s'entendent sur l'Axe Rome-Berlin.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[25, 28, 29]),
    }),

    # ================================================================ la carte : 1937-1939
    dict(id="carte2", chap="Sur la carte : 1937 – 1939", fond="nuit", humeur="tension",
         retenir="12 mars 1938 l'Anschluss · 29-30 sept. 1938 Munich · 15 mars 1939 Prague · 31 mars 1939 garantie à la Pologne · 23 août 1939 le pacte germano-soviétique · 1er-3 sept. 1939 la guerre.",
         beats=[
        "{g2}{g2.1}À partir de mille neuf cent trente-sept, Londres et Paris suivent une seule politique : accepter les exigences des dictateurs, pour éviter la guerre. "
        "On l'appelle l'apaisement.",
        "{g2.2}Le douze mars mille neuf cent trente-huit, l'armée allemande entre en Autriche. L'Autriche est annexée : c'est l'Anschluss.",
        "{g2.3}Septembre mille neuf cent trente-huit. À Munich, le Royaume-Uni et la France livrent les Sudètes à Hitler. Les Tchèques ne sont même pas invités.",
        "{g2.4}Le quinze mars mille neuf cent trente-neuf, l'Allemagne occupe Prague et le reste des pays tchèques. L'apaisement est mort. "
        "Le trente et un mars, la France et le Royaume-Uni garantissent la Pologne.",
        "{g2.5}Le vingt-trois août mille neuf cent trente-neuf, deux ennemis jurés, l'Allemagne nazie et l'Union soviétique, signent un pacte. "
        "En secret, ils se partagent la Pologne.",
        "{g2.6}Et le premier septembre, l'Allemagne attaque la Pologne. Le trois, la France et le Royaume-Uni déclarent la guerre.",
        "{-g2}{fr1}Sept dates à savoir par cœur. {fr1.1}Mille neuf cent trente-cinq : Stresa, et l'accord naval. {fr1.2}Mars mille neuf cent trente-six : la Rhénanie. "
        "{fr1.3}Octobre mille neuf cent trente-six : l'Axe. {fr1.4}Mars mille neuf cent trente-huit : l'Anschluss. {fr1.5}Septembre mille neuf cent trente-huit : Munich. "
        "{fr1.6}Mars mille neuf cent trente-neuf : Prague. {fr1.7}Et d'août à septembre mille neuf cent trente-neuf : le pacte, puis la guerre.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[31, 33, 34, 35, 36, 37]),
        "fr1": dict(type="frise", items=[
            dict(nom="Stresa · accord naval", d=1935, q="avril-juin"), dict(nom="Rhénanie", d=1936, q="7 mars"),
            dict(nom="L'Axe", d=1936, q="25 octobre"), dict(nom="Anschluss", d=1938, q="12 mars"),
            dict(nom="Munich", d=1938, q="29-30 sept."), dict(nom="Prague", d=1939, q="15 mars"),
            dict(nom="Pacte · guerre", d=1939, q="23 août · 1er-3 sept.")]),
    }),

    # ================================================================ III.2, idée 1 : une Europe divisée, une SDN muette
    dict(id="europe", chap="III.2 · Une Europe divisée, une SDN muette", fond="nuit", humeur="tension",
         retenir="L'Europe des années 1930 : les démocraties (France, Royaume-Uni) · les dictatures (Allemagne, Italie ; le Japon en Asie) · l'URSS, immense et isolée. La SDN ne peut agir sans les grandes puissances. Low, « Sur le trône de la Justice », 24 juillet 1935.",
         beats=[
        "{eu}Place au cours. Partie trois point deux, première idée. Dans les années mille neuf cent trente, l'Europe est {!divisée}divisée en trois camps. "
        "{eu.1}Les démocraties : la France et le Royaume-Uni. {eu.2}Les dictatures : l'Allemagne et l'Italie, avec le Japon en Asie. "
        "{eu.3}Et l'Union soviétique, immense et isolée.",
        "{-eu}{sdn}Entre eux, la Société des Nations. Elle a été créée en mille neuf cent dix-neuf pour empêcher les agressions. "
        "{sdn.1}Mais chaque fois que les grandes puissances ne la soutiennent pas, elle {!ne peut pas agir}ne peut pas agir.",
        "{-sdn}{low1}Le dessinateur britannique David Low a fait de cet échec son sujet. En juillet mille neuf cent trente-cinq, "
        "Mussolini prépare l'invasion de l'Abyssinie. Low dessine {low1.1}trois singes, assis sur le trône du droit international. "
        "L'un se cache les yeux. L'autre les oreilles. Le troisième la bouche. {low1.2}Ne rien voir de l'Abyssinie. N'en rien entendre. N'en rien dire.",
    ], vis={
        "eu": dict(type="liste", titre="L'Europe des années 1930 : trois camps", cles=["démocraties", "dictatures", "isolé"], items=[
            "Les démocraties : la France, le Royaume-Uni", "Les dictatures : l'Allemagne, l'Italie (et le Japon en Asie)",
            "L'URSS : un régime totalitaire immense et isolé"], x=170, y=150, w=940),
        "sdn": dict(type="def", cles=["agressions", "grandes puissances"], terme="La Société des Nations (1919)",
                    t="L'institution créée en 1919 pour empêcher les agressions.",
                    etape="Impuissante chaque fois que les grandes puissances ne la soutiennent pas", x=170, y=200, w=940),
        "low1": dict(type="liste", titre="David Low, « Sur le trône de la Justice », Evening Standard, 24 juillet 1935", items=[
            "Trois singes marqués « Abyssinie » sur le trône du droit international",
            "Ne rien voir, ne rien entendre, ne rien dire de l'Abyssinie : la SDN voit, entend et se tait"],
            x=150, y=160, w=980),
    }),

    # ================================================================ III.2, idée 2 : l'isolationnisme américain
    dict(id="usa", chap="III.2 · L'isolationnisme américain", fond="nuit", humeur="calme",
         retenir="Roosevelt tente de rompre avec l'isolationnisme, mais le Congrès vote les lois de neutralité (1935, 1936, 1937) : ni ventes d'armes, ni prêts aux pays en guerre. Écrire « un Congrès isolationniste », pas « un Congrès républicain ».",
         beats=[
        "{usq}Deuxième idée. La plus puissante des démocraties reste à l'écart des crises européennes. Aux États-Unis, le président Roosevelt tente "
        "de rompre avec l'isolationnisme. Mais le Congrès le retient. {-usq}{us}{us.1}Il vote les {!lois de neutralité}lois de neutralité. "
        "Elles interdisent les ventes d'armes et les prêts aux pays en guerre. {us.2}Une en mille neuf cent trente-cinq. {us.3}Une autre en trente-six. {us.4}Et une troisième en trente-sept.",
        "{-us}{rep}Attention : ici, le cours se corrige lui-même. Le document du cours parle d'un Congrès républicain. "
        "En réalité, les démocrates y sont majoritaires de mille neuf cent trente-cinq à mille neuf cent trente-neuf. L'isolationnisme traverse les deux partis. "
        "{rep.1}Dans ta copie, écris donc : {!un Congrès isolationniste}un Congrès isolationniste.",
    ], vis={
        "usq": dict(type="question", t="La plus puissante des démocraties reste à l'écart."),
        "us": dict(type="liste", titre="Les lois de neutralité", cles=["armes", "prêts"], items=[
            "Ni ventes d'armes, ni prêts aux pays en guerre", "1935 : la première loi de neutralité", "1936 : une deuxième",
            "1937 : une troisième"], x=170, y=140, w=940),
        "rep": dict(type="note", terme="Attention · une formulation", cles=["démocrates", "deux partis"],
                    t="Le document dit « un Congrès républicain » ; les démocrates y sont majoritaires de 1935 à 1939.",
                    etape="L'isolationnisme traverse les deux partis : écrire « un Congrès isolationniste »", x=170, y=200, w=940),
    }),

    # ================================================================ III.2, idées 3 et 4 : Stresa et le réarmement
    dict(id="stresa", chap="III.2 · Le front de Stresa et le réarmement allemand", fond="nuit", humeur="tension",
         retenir="Avril 1935 : le front de Stresa (Royaume-Uni, France, Italie) contre l'Allemagne → Mussolini ménagé sur l'Abyssinie ; le front s'effondre. 1935 : la Wehrmacht (Heer, Kriegsmarine, Luftwaffe). Juin 1935 : l'accord naval, 35 % de la Royal Navy.",
         beats=[
        "{g3}{g3.1}Troisième idée : le front de Stresa. En avril mille neuf cent trente-cinq, à Stresa, dans le nord de l'Italie, le Royaume-Uni et la France tentent de former un front "
        "avec l'Italie, contre les ambitions allemandes. {sf}{sf.1}C'est un calcul qui pèse sur toute la suite. "
        "{sf.2}Pour garder Mussolini loin de Hitler, Londres et Paris hésitent à le punir pour l'Abyssinie. "
        "{sf.3}Et le front s'effondre quand même. L'Italie se tourne vers l'Allemagne.",
        "{-sf}{-g3}{wm}Quatrième idée. L'Allemagne viole ouvertement le traité de Versailles. À partir de mille neuf cent trente-cinq, elle réarme massivement. "
        "Elle crée une force armée unique, la {!Wehrmacht}Wehrmacht, avec trois branches. "
        "{wm.1}L'armée de terre, la Heer. {wm.2}La marine, la Kriegsmarine. {wm.3}Et l'armée de l'air, la Luftwaffe. "
        "Chaque violation impunie rend la suivante plus facile.",
        "{-wm}{pct}Voici l'exemple. En juin mille neuf cent trente-cinq, deux mois après Stresa, le Royaume-Uni signe seul un accord naval avec l'Allemagne. "
        "Il autorise la Kriegsmarine à atteindre {!35 %}trente-cinq pour cent du tonnage de la Royal Navy. "
        "Le Royaume-Uni rend lui-même légale une violation de Versailles.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[25]),
        "sf": dict(type="liste", titre="Le front de Stresa, avril 1935", petit=True, bande=True, x=700, y=110, w=540, items=[
            "Royaume-Uni, France et Italie contre les ambitions allemandes", "Donc Mussolini ménagé sur l'Abyssinie",
            "Le front s'effondre : l'Italie se tourne vers l'Allemagne"]),
        "wm": dict(type="liste", titre="1935 · la Wehrmacht, une force armée unique", items=[
            "L'armée de terre : la Heer", "La marine : la Kriegsmarine", "L'armée de l'air : la Luftwaffe"], x=170, y=150, w=940),
        "pct": dict(type="mot", t="35 %", g="Juin 1935 · la Kriegsmarine autorisée à 35 % du tonnage de la Royal Navy", y=240, taille=150),
    }),

    # ================================================================ III.2, idée 5 : l'apaisement
    dict(id="appease", chap="III.2 · L'apaisement, étude de cas 3", fond="nuit", humeur="tension",
         retenir="Notion clé · l'apaisement : Chamberlain (à partir de 1937) et Daladier acceptent les exigences de l'Axe pour éviter la guerre. Ce qu'il a cédé : 1935 l'accord naval · 1935 pas d'embargo pétrolier contre l'Italie · 1936 aucune réaction en Rhénanie · 1938 Munich.",
         beats=[
        "{photo1}{def1}Cinquième idée. C'est l'étude de cas numéro trois, et une notion clé du chapitre : {!l'apaisement}l'apaisement. "
        "Ce sont les efforts du Premier ministre britannique, Neville Chamberlain, à partir de mille neuf cent trente-sept. "
        "Et ceux de son homologue français, Édouard Daladier. Tous deux cherchent à éviter la guerre en acceptant les exigences des puissances de l'Axe. "
        "{def1.1}Ce faisant, les démocraties renoncent aux buts qu'elles s'étaient fixés en mille neuf cent dix-neuf. L'Allemagne, l'Italie et le Japon ne sont pas arrêtés. "
        "Pourtant, leur militarisme contredit ouvertement les traités de paix.",
        "{-def1}{-photo1}{ced}Voici la première colonne du schéma du cours : ce que l'apaisement a cédé. "
        "{ced.1}En mille neuf cent trente-cinq, l'accord naval germano-britannique. "
        "{ced.2}La même année, le Royaume-Uni refuse un embargo sur le pétrole. C'était la seule sanction qui aurait arrêté Mussolini en Éthiopie. "
        "{ced.3}En mars mille neuf cent trente-six, aucune réaction quand Hitler envoie ses troupes dans la Rhénanie démilitarisée. "
        "{ced.4}Et en mille neuf cent trente-huit, Munich. Les Sudètes sont livrées, sans les Tchèques.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-munich", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Chamberlain, Daladier, Hitler, Mussolini et Ciano avant la signature des accords de Munich, 29 septembre 1938 · Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE"),
        "def1": dict(type="def", cles=["éviter la guerre", "exigences"], terme="Notion clé · l'apaisement",
                     t="Éviter la guerre en acceptant les exigences des puissances de l'Axe : Chamberlain (à partir de 1937), Daladier.",
                     etape="Les buts de 1919 abandonnés : l'Allemagne, l'Italie et le Japon ne sont pas arrêtés", x=170, y=200, w=940),
        "ced": dict(type="liste", titre="L'apaisement · ce qui a été cédé", items=[
            "1935 · Accord naval germano-britannique : la Kriegsmarine à 35 % de la Royal Navy",
            "1935 · Refus de l'embargo pétrolier qui aurait arrêté Mussolini en Éthiopie",
            "1936 · Aucune réaction à la remilitarisation de la Rhénanie",
            "1938 · Munich : les Sudètes livrées sans les Tchèques"], x=130, y=130, w=1020),
    }),

    # ================================================================ III.2, idée 6 : pourquoi l'apaisement
    dict(id="pourquoi", chap="III.2 · Pourquoi l'apaisement semblait raisonnable", fond="aube", humeur="calme",
         retenir="Sept raisons : le pacifisme (1914-1918 ; l'Oxford Union, févr. 1933) · le Commonwealth (le Canada) · un empire à tenir (l'Inde) · une Allemagne maltraitée en 1919 · la Dépression d'abord · l'isolationnisme américain · la peur du communisme. Discrédité aujourd'hui, populaire à l'époque.",
         beats=[
        "{qw}Sixième idée. Aujourd'hui, on voit souvent dans l'apaisement une politique de faiblesse. Mais à l'époque, il est populaire. Et il paraît pragmatique. "
        "{-qw}{wh}La deuxième colonne du schéma donne sept raisons. "
        "{wh.1}Un : le souvenir du massacre de quatorze-dix-huit. Les deux pays sont profondément pacifistes. "
        "{wh.2}Deux : le Royaume-Uni craint que le Commonwealth ne le suive pas une seconde fois. L'exemple du cours, c'est le Canada. "
        "{wh.3}Trois : le Royaume-Uni est occupé à tenir son empire, l'Inde par exemple. Il ne peut pas se permettre un grand réarmement.",
        "{wh.4}Quatre : beaucoup de Britanniques pensent que l'Allemagne a été injustement traitée en mille neuf cent dix-neuf. "
        "{wh.5}Cinq : les deux pays font passer d'abord leurs propres difficultés économiques, celles de la Dépression. "
        "{wh.6}Six : ils se sentent sans protection, car l'Amérique est isolationniste. "
        "{wh.7}Et sept : beaucoup craignent le communisme plus que le fascisme.",
        "{-wh}En février mille neuf cent trente-trois, l'Oxford Union vote cette motion :",
        ("C", "Cette assemblée refuse, en toutes circonstances, de se battre pour son roi et pour son pays.", "c_ox"),
        "Dans ta copie, dis donc les deux. {-c_ox}{deux}{deux.g}Discrédité aujourd'hui, parce que chaque concession a été suivie d'une exigence plus grande. "
        "{deux.d}Mais populaire à l'époque, parce qu'il reposait sur des raisons solides, et sur l'opinion publique.",
    ], vis={
        "qw": dict(type="question", t="Faiblesse… ou pragmatisme ?"),
        "wh": dict(type="liste", titre="Pourquoi l'apaisement ? Les sept raisons du cours", petit=True, items=[
            "Le souvenir de 1914-1918 : le pacifisme", "La crainte que le Commonwealth (le Canada) ne suive pas une seconde fois",
            "Un empire à tenir (l'Inde) : pas de réarmement massif", "La sympathie pour une Allemagne jugée maltraitée en 1919",
            "Les difficultés économiques de la Dépression, prioritaires", "L'isolationnisme américain, qui les laisse sans protection",
            "La peur du communisme, plus forte que celle du fascisme"], x=130, y=90, w=1020),
        "c_ox": dict(type="cit", a="L'Oxford Union", o="motion votée en février 1933", x=200, y=210, w=880),
        "deux": dict(type="cols", g="Discrédité aujourd'hui", gq="une politique de faiblesse : à chaque concession, une exigence plus grande",
                     d="Populaire à l'époque", dq="pacifisme, empire, Dépression, peur du communisme", vs="+",
                     repere="Une bonne copie dit les deux"),
    }),

    # ================================================================ III.2, idée 7 : Munich
    dict(id="munich", chap="III.2 · Munich, 1938", fond="guerre", humeur="tension",
         retenir="29-30 sept. 1938, Munich : Hitler, Chamberlain, Daladier, Mussolini. Les Sudètes (≈ 3 millions de germanophones) livrées ; les Tchèques pas invités ; Hitler promet de ne pas menacer le reste de la Tchécoslovaquie. Low : Hitler en Krampus (10 oct. 1938).",
         beats=[
        "{g4}{g4.1}Septième idée : Munich, mille neuf cent trente-huit. Hitler réclame les Sudètes, la région germanophone de la Tchécoslovaquie. "
        "Environ trois millions de germanophones y vivent. {mu}{mu.1}La Tchécoslovaquie est la dernière démocratie d'Europe centrale. "
        "Et Hitler menace d'envahir tout le pays.",
        "{mu.2}La conférence se réunit les vingt-neuf et trente septembre. Autour de la table : Hitler, Chamberlain, Daladier et Mussolini. "
        "Mussolini se pose en modéré, en artisan de la paix. En réalité, il aide l'Allemagne à obtenir ce qu'elle veut. "
        "{mu.3}Et les Tchèques ? Ils ne sont {!pas invités}pas invités. "
        "{mu.4}Le Royaume-Uni et l'Allemagne promettent de ne pas se faire la guerre. Et Hitler promet de ne jamais menacer le reste de la Tchécoslovaquie.",
        "{-mu}{-g4}{low2}David Low ne croit pas à cette promesse. Le dix octobre, dix jours après Munich, il dessine Hitler en Krampus. "
        "Le Krampus, c'est le démon qui terrorise les enfants à Noël. {-low2}Et la légende dit :",
        ("C", "L'Europe peut s'attendre à un Noël de paix", "c_low"),
        "{-c_low}{photo2}{iro}L'ironie est amère. La paix achetée à Munich durera {!moins de six mois}moins de six mois.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[34]),
        "mu": dict(type="liste", titre="Munich, 29-30 septembre 1938", petit=True, bande=True, x=700, y=110, w=540, items=[
            "La Tchécoslovaquie : la dernière démocratie d'Europe centrale", "Hitler, Chamberlain, Daladier, Mussolini « le modéré »",
            "Les Tchèques ne sont pas invités", "Hitler promet de ne pas menacer le reste du pays"]),
        "low2": dict(type="note", terme="David Low, dessin du 10 octobre 1938", cles=["Krampus"],
                     t="Hitler dessiné en Krampus, le démon qui terrorise les enfants à Noël.",
                     etape="Dix jours après Munich : le dessinateur ne croit pas à la promesse", x=170, y=120, w=940),
        "c_low": dict(type="cit", a="David Low", o="légende du dessin, 10 octobre 1938", x=200, y=330, w=880),
        "photo2": dict(type="tableau", img="h2-heston", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Chamberlain brandit la déclaration germano-britannique à l'aéroport de Heston, 30 septembre 1938 · Imperial War Museums, D 2239, domaine public"),
        "iro": dict(type="mot", t="< 6 mois", g="Munich, 30 sept. 1938 → Prague, 15 mars 1939", y=250, taille=110),
    }),

    # ================================================================ analyse de document : le télégramme de Roosevelt (DBQ 2)
    dict(id="dbq2", chap="Analyse de document · le télégramme de Roosevelt", fond="aube", humeur="calme",
         retenir="Le télégramme de Roosevelt (14 avril 1939) : d'un grand intérêt pour la réponse américaine au printemps 1939 (auteur, date, méthode : une « assurance » sans sanction, un bilan des échecs, une diplomatie publique) · limites : une seule démocratie, neutre, aucun résultat, rien sur les lois de neutralité, un texte écrit pour être publié.",
         beats=[
        "{doc2}Voici maintenant un document du chapitre. {doc2.1}C'est un télégramme du président Roosevelt à Hitler, "
        "daté du quatorze avril mille neuf cent trente-neuf. Le même texte est envoyé à Mussolini. "
        "{doc2.2}Un mois après Prague, Roosevelt demande aux dictateurs une assurance. "
        "Ils doivent promettre de ne pas attaquer trente et un États, nommés un par un, de la Finlande à l'Iran. "
        "{doc2.3}Mais aucune sanction. Aucune alliance. Aucune menace de recourir à la force. {-doc2}Il écrit :",
        ("C", "Trois nations d'Europe et une d'Afrique ont vu leur existence indépendante prendre fin.", "c_fdr1"),
        "C'est-à-dire l'Autriche, la Tchécoslovaquie, l'Albanie et l'Éthiopie. {-c_fdr1}Et il avertit les dictateurs :",
        ("C", "L'histoire les en tiendra pour responsables.", "c_fdr2"),
        "{-c_fdr2}{ex2}La consigne : présentez le document, puis montrez {!son intérêt et ses limites}son intérêt et ses limites "
        "pour comprendre la réponse des démocraties aux ambitions de Hitler.",
        "{-ex2}{m2}Voici le modèle du site, en bref. {m2.1}Le bilan critique d'abord : un document d'un grand intérêt, même s'il n'éclaire qu'un aspect de cette réponse. "
        "{m2.2}Son intérêt. L'auteur est le chef de la plus puissante démocratie neutre. La date tombe juste après Prague. "
        "Il demande des assurances, sans aucune contrainte. Sa liste de trente et un États avoue jusqu'où l'on s'attend à voir l'agression aller. "
        "Et c'est un message public.",
        "{m2.3}Ses limites. Rien sur le Royaume-Uni et la France. Aucun résultat, puisque la réponse de Hitler, le vingt-huit avril, manque. "
        "Rien sur les lois de neutralité. Et le texte est écrit pour être publié.",
        "{-m2}{pie}{!Attention}Et attention au piège. La consigne dit les démocraties, au pluriel. Le document d'une seule d'entre elles "
        "ne peut être que partiellement représentatif. Dis-le, et fais intervenir le Royaume-Uni et la France grâce à tes connaissances.",
    ], vis={
        "doc2": dict(type="liste", titre="Le document · un télégramme de Roosevelt", items=[
            "Roosevelt à Hitler, télégramme, la Maison-Blanche, 14 avril 1939 (le même à Mussolini)",
            "Une « assurance » demandée pour 31 États nommés, de la Finlande à l'Iran",
            "Aucune sanction, aucune alliance, aucune menace de recourir à la force"], x=150, y=140, w=980),
        "c_fdr1": dict(type="cit", a="Franklin D. Roosevelt", o="télégramme à Hitler, 14 avril 1939", x=200, y=210, w=880),
        "c_fdr2": dict(type="cit", a="Franklin D. Roosevelt", o="télégramme à Hitler, 14 avril 1939", x=200, y=230, w=880),
        "ex2": dict(type="exo", niveau="dbq", titre="Présentez le document, puis montrez son intérêt et ses limites pour comprendre la réponse des démocraties aux ambitions de Hitler.",
                    src="Document du chapitre (télégramme de Roosevelt) ; consigne écrite pour cette vidéo",
                    enonce=["Analyse de document · présenter, expliquer, critiquer"]),
        "m2": dict(type="liste", titre="Le modèle, en bref", petit=True, items=[
            "Bilan critique : d'un grand intérêt… mais il n'éclaire qu'un aspect de la réponse",
            "Intérêt : l'auteur · la date (après Prague, l'Albanie) · une « assurance » sans sanction · 31 États · une diplomatie publique",
            "Limites : une seule démocratie, neutre · aucun résultat (réponse de Hitler, 28 avril) · rien sur les lois de neutralité · écrit pour être publié"],
            x=130, y=130, w=1020),
        "pie": dict(type="note", terme="Attention · le piège", cles=["pluriel", "Royaume-Uni et la France"],
                    t="« Les démocraties », au pluriel : le document d'une seule démocratie ne peut être que partiellement représentatif.",
                    etape="Dis-le, et fais intervenir le Royaume-Uni et la France grâce à tes connaissances", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idées 1 et 2 : l'Axe et l'Espagne
    dict(id="axe", chap="III.3 · L'Axe et la guerre d'Espagne", fond="guerre", humeur="tension",
         retenir="25 oct. 1936 : l'Axe Rome-Berlin, une alliance d'intérêt entre deux dictateurs qui se méfient l'un de l'autre (pacte d'Acier 1939, le Japon 1940). Espagne 1936 : l'Allemagne et l'Italie soutiennent Franco, la Luftwaffe s'y essaie ; la France et le Royaume-Uni restent à l'écart.",
         beats=[
        "{g5}{g5.1}Partie trois point trois : la marche à la Seconde Guerre mondiale. Première idée, l'Axe. Hitler a besoin d'alliés. "
        "Il en trouve un en Mussolini, malgré un certain mépris réciproque. "
        "Hitler admire depuis longtemps le fascisme. Mais Mussolini voit en lui un rival ambitieux et prétentieux. "
        "En mille neuf cent trente-deux, il se moque même du racisme nazi :",
        "{-g5}",
        ("C", "Le racisme, c'est une affaire de blonds !", "c_mus"),
        "{-c_mus}{ax}{ax.g}Alors pourquoi s'allier ? Parce que l'Italie est économiquement trop faible pour affronter seule les démocraties. Mussolini a besoin de l'appui allemand. "
        "L'Axe Rome-Berlin est proclamé le vingt-cinq octobre mille neuf cent trente-six. {ax.d}Il devient une alliance militaire, le pacte d'Acier, en mille neuf cent trente-neuf. "
        "Le Japon rejoint l'alliance en mille neuf cent quarante. Une alliance d'intérêt, pas d'amitié.",
        "{-ax}{g6}{g6.1}{es}Deuxième idée : l'Espagne. {es.1}La guerre civile éclate en Espagne en mille neuf cent trente-six. L'Allemagne et l'Italie soutiennent les nationalistes du général Franco. "
        "{es.2}Et l'Allemagne profite du conflit pour mettre à l'essai son aviation. "
        "{es.3}La France et le Royaume-Uni n'interviennent pas pour aider la République espagnole. "
        "{es.4}Voici un exemple que le cours ajoute, en dehors de la leçon. En avril mille neuf cent trente-sept, des bombardiers allemands détruisent "
        "la ville basque de Guernica. Picasso la peint la même année.",
        "{-es}{-g6}{photo3}{rep2}L'Espagne est une répétition de la guerre à venir. Et une preuve de plus que les démocraties n'agiront pas.{-photo3}",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[29]),
        "c_mus": dict(type="cit", a="Benito Mussolini", o="1932, cité dans le cours", x=200, y=230, w=880),
        "ax": dict(type="cols", g="Un mépris réciproque", gq="Hitler admire le fascisme ; Mussolini voit un rival prétentieux",
                   d="Un besoin réciproque", dq="l'Italie trop faible seule : l'Axe (oct. 1936), le pacte d'Acier (1939), le Japon (1940)", vs="→",
                   repere="Une alliance d'intérêt"),
        "g6": dict(type="globe", code="H2", sc=[29]),
        "es": dict(type="liste", titre="L'Espagne, 1936", petit=True, bande=True, x=780, y=110, w=470, items=[
            "L'Allemagne et l'Italie soutiennent les nationalistes de Franco", "L'aviation allemande mise à l'essai en Espagne",
            "La France et le Royaume-Uni n'aident pas la République", "Guernica, 26 avril 1937 (hors de la leçon)"]),
        "photo3": dict(type="tableau", img="h2-guernica", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Les ruines de Guernica après le bombardement du 26 avril 1937 (hors de la leçon) · Bundesarchiv, Bild 183-H25224, CC BY-SA 3.0 DE"),
        "rep2": dict(type="mot", t="Une répétition", g="de la guerre à venir · les démocraties n'agiront pas", y=260, taille=100),
    }),

    # ================================================================ III.3, idée 3 : la Rhénanie
    dict(id="rhenanie", chap="III.3 · La Rhénanie, 1936", fond="nuit", humeur="tension",
         retenir="7 mars 1936 : un risque calculé. Des troupes trop faibles pour résister à l'armée française, avec l'ordre de se retirer si la France réagissait. Aucune réaction : le pari réussit, et apprend à Hitler que les démocraties céderont. Low, « Les marchepieds de la gloire » (1936).",
         beats=[
        "{g7}{g7.1}Troisième idée : la Rhénanie, le sept mars mille neuf cent trente-six. Réoccuper cette zone démilitarisée est un risque calculé.",
        "{rh}{rh.1}Les troupes allemandes ne sont pas assez fortes pour résister à l'armée française, si la France réagit. "
        "{rh.2}Elles ont l'ordre strict de se retirer dans ce cas. "
        "{rh.3}Mais la France et le Royaume-Uni n'ont aucune envie de combattre l'Allemagne. Personne ne résiste.",
        "{-rh}{-g7}{pari}Le pari de Hitler réussit. Et surtout, {!il lui apprend}il lui apprend que les démocraties céderont.",
        "{-pari}{low3}La même année, David Low dessine une caricature intitulée Les marchepieds de la gloire. Hitler monte vers ses objectifs "
        "sur le dos courbé des dirigeants des démocraties. Low les appelle les dirigeants sans colonne vertébrale de la démocratie. "
        "{low3.1}Chaque dos est une marche. Garde cette image en tête : nous monterons ces marches à la fin de cette partie.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[28]),
        "rh": dict(type="liste", titre="7 mars 1936 · un risque calculé", petit=True, bande=True, x=700, y=110, w=540, items=[
            "Des troupes allemandes trop faibles face à l'armée française", "L'ordre strict de se retirer si la France réagit",
            "La France et le Royaume-Uni ne bougent pas"]),
        "pari": dict(type="question", t="Le pari a réussi."),
        "low3": dict(type="note", terme="David Low, « Stepping Stones to Glory » (Les marchepieds de la gloire), 1936", cles=["dos courbé", "colonne vertébrale"],
                     t="Hitler monte vers ses objectifs sur le dos courbé des « dirigeants sans colonne vertébrale de la démocratie ».",
                     etape="À chaque concession, une marche : le schéma de la fin de cette partie les suit jusqu'en 1939", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idée 4 : l'Anschluss
    dict(id="anschluss", chap="III.3 · L'Anschluss, 1938", fond="nuit", humeur="tension",
         retenir="Hitler fait pression sur Schuschnigg et masse des troupes à la frontière → Seyss-Inquart chancelier, il appelle l'armée allemande → l'Autriche, 12 mars 1938 → un plébiscite sans les opposants ni les Juifs : 99 % de oui. Le Royaume-Uni et la France ne font rien.",
         beats=[
        "{g8}{g8.1}Quatrième idée : l'Anschluss, l'annexion de l'Autriche. Elle se fait en quatre étapes. "
        "{an}{an.1}D'abord, la pression. Discours après discours, Hitler malmène le chancelier autrichien, Schuschnigg. Il masse des troupes à la frontière. "
        "Et il menace d'envahir le pays, à moins que Schuschnigg ne cède la place à un nazi, Seyss-Inquart. "
        "{an.2}Ensuite, Seyss-Inquart devient chancelier, et il appelle les troupes allemandes en Autriche. "
        "{an.3}Puis, le douze mars mille neuf cent trente-huit, l'armée allemande entre dans le pays. "
        "Hitler a de nouveau violé Versailles. Et le Royaume-Uni et la France ne font rien.",
        "{an.4}Enfin, un référendum approuve l'annexion. Mais les opposants politiques et les Juifs n'ont pas le droit de voter.",
        "{-an}{-g8}{photo4}{oui}Et le résultat ?",
        ("P", 0.6),
        "{-oui}{pct2}{!99 % de oui}Quatre-vingt-dix-neuf pour cent de oui. Un vote contrôlé, pour habiller une annexion obtenue par la pression.",
        "{-pct2}{-photo4}{huit}Un chiffre à manier avec précaution. Le cours dit que les Juifs autrichiens, huit pour cent de la population, n'ont pas pu voter. "
        "{huit.1}Mieux vaut lire ces huit pour cent comme la part des exclus du vote : opposants et Juifs ensemble. "
        "Les Juifs seuls représentent environ trois Autrichiens sur cent, la plupart à Vienne. Ce chiffre vient d'en dehors du cours.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[33]),
        "an": dict(type="liste", titre="L'Anschluss en quatre étapes", petit=True, bande=True, x=780, y=110, w=470, items=[
            "La pression : Schuschnigg malmené, des troupes à la frontière", "Seyss-Inquart chancelier : il appelle l'armée allemande",
            "12 mars 1938 : l'armée allemande entre en Autriche", "Un plébiscite sans les opposants ni les Juifs"]),
        "photo4": dict(type="tableau", img="h2-anschluss", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Hitler s'adresse à la foule sur la Heldenplatz, Vienne, 15 mars 1938 · Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE"),
        "oui": dict(type="question", t="Le plébiscite : le résultat ?"),
        "pct2": dict(type="mot", t="99 % de oui", g="un vote contrôlé · opposants et Juifs exclus", y=240, taille=140),
        "huit": dict(type="note", terme="Attention · un chiffre", cles=["exclus", "trois"],
                     t="8 % : la part des exclus du vote, opposants et Juifs ensemble, et non celle des seuls Juifs.",
                     etape="Les Juifs : environ 3 % des Autrichiens, la plupart à Vienne (hors du cours)", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idée 5 : Prague
    dict(id="prague", chap="III.3 · Prague, mars 1939", fond="guerre", humeur="tension",
         retenir="15 mars 1939 : l'Allemagne occupe Prague. Hitler a menti à Munich ; il ne s'agit plus de réunir des Allemands mais d'occuper un peuple étranger → fin de l'apaisement : garanties à la Pologne (31 mars), à la Roumanie, à la Grèce.",
         beats=[
        "{g9}{g9.1}Cinquième idée : Prague. Le quinze mars mille neuf cent trente-neuf, l'Allemagne occupe Prague et envahit le reste de la Tchécoslovaquie. "
        "Hitler a prouvé qu'il {!avait menti à Munich}avait menti à Munich.",
        "{-g9}{diff}{diff.g}Et cette fois, la conquête ne peut pas se présenter comme la réunion d'Allemands. "
        "{diff.d}C'est l'occupation d'un peuple étranger. L'apaisement est terminé.",
        "{-diff}{gar}Le Royaume-Uni et la France changent de cap. {gar.1}Ils s'engagent à protéger la Roumanie, la Grèce et la Pologne, "
        "si l'Allemagne ou l'Italie les attaque. {gar.2}La garantie à la Pologne est donnée le trente et un mars. "
        "{gar.3}Et c'est cet engagement qui fera entrer les deux pays dans la guerre, cinq mois plus tard.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[35]),
        "diff": dict(type="cols", g="Jusqu'à Munich", gq="Rhénanie, Autriche, Sudètes : « réunir des Allemands »",
                     d="Prague, 15 mars 1939", dq="l'occupation d'un peuple étranger", vs="≠",
                     repere="Le mensonge de Munich met fin à l'apaisement"),
        "gar": dict(type="liste", titre="Les démocraties changent de cap", items=[
            "Garanties à la Roumanie, à la Grèce et à la Pologne, en cas d'attaque allemande ou italienne",
            "31 mars 1939 : la garantie à la Pologne", "L'engagement qui les fait entrer en guerre en septembre"],
            x=150, y=150, w=980),
    }),

    # ================================================================ III.3, idée 6 : le pacte germano-soviétique
    dict(id="pacte", chap="III.3 · Le pacte germano-soviétique", fond="guerre", humeur="tension",
         retenir="23 août 1939 : un pacte de non-agression ; en secret, le partage de la Pologne. Hitler : pas de guerre sur deux fronts. Staline, son armée décimée par les purges : du temps et des territoires. 1er sept. 1939 : la Pologne attaquée ; 3 sept. : la France et le Royaume-Uni déclarent la guerre.",
         beats=[
        "{g10}{g10.1}Sixième idée. Le vingt-trois août mille neuf cent trente-neuf, l'Allemagne signe un pacte de non-agression avec l'Union soviétique. "
        "Ses clauses secrètes prévoient de se partager la Pologne. Deux ennemis idéologiques concluent un accord de {!pur intérêt}pur intérêt.",
        "{-g10}{photo5}{gain}{gain.g}Pour Hitler, il écarte la menace d'une guerre sur deux fronts. "
        "{gain.d}Pour Staline, dont l'armée vient d'être décimée par les purges, il fait gagner du temps, et des territoires.",
        "{-gain}La caricature du cours prête à Staline cette réplique :",
        ("C", "Je ne suis pas prêt pour la guerre ! Je viens de tuer sept cent mille de mes meilleurs officiers et dirigeants communistes !", "c_car"),
        "{-c_car}{-photo5}{chif}C'est un chiffre de caricature. Le cours donne environ six cent quatre-vingt mille exécutions "
        "pour toute la Grande Purge, loin d'être tous des officiers. Mais l'idée tient : l'Armée rouge n'était pas prête.",
        "{-chif}{g11}{g11.1}Désormais, plus rien ne fait obstacle. Le premier septembre, l'Allemagne attaque la Pologne, l'alliée de la France. "
        "Le trois, la France et le Royaume-Uni déclarent la guerre. {!La guerre}La guerre a commencé.",
    ], vis={
        "g10": dict(type="globe", code="H2", sc=[36]),
        "photo5": dict(type="tableau", img="h2-pact", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .3],
                       legende="Staline et Ribbentrop après la signature du pacte germano-soviétique de non-agression, Moscou, 23 août 1939 · Bundesarchiv, Bild 183-H27337 / Helmut Laux, CC BY-SA 3.0 DE"),
        "gain": dict(type="cols", g="Hitler", gq="pas de guerre sur deux fronts : l'attaque de la Pologne peut commencer",
                     d="Staline", dq="une armée décimée par les purges : du temps et des territoires", vs="+",
                     repere="23 août 1939 · un accord de pur intérêt"),
        "c_car": dict(type="cit", a="Staline, dans une caricature", o="caricature présentée dans le cours", x=200, y=210, w=880),
        "chif": dict(type="note", terme="Attention · un chiffre de caricature", cles=["680 000", "officiers"],
                     t="Le cours : ≈ 680 000 exécutions pour toute la Grande Purge (1937-1938), loin d'être tous des officiers.",
                     etape="L'idée tient : l'Armée rouge n'était pas prête", x=170, y=200, w=940),
        "g11": dict(type="globe", code="H2", sc=[37]),
    }),

    # ================================================================ III.3, idée 7 : la chaîne
    dict(id="chaine", chap="III.3 · Chaque agression prépare la suivante", fond="nuit", humeur="tension",
         retenir="La chaîne : 1931 la Mandchourie · 1933 l'Allemagne et le Japon quittent la SDN · 1935 l'Éthiopie · 1936 la Rhénanie, l'Espagne · 1937 la Chine, l'Italie quitte la SDN · 1938 l'Anschluss, Munich · mars 1939 Prague · 1er sept. 1939 la Pologne. L'idéologie = la volonté ; la réticence des démocraties = l'occasion.",
         beats=[
        "{st}Septième idée : la conséquence de l'apaisement. Montons les marches de David Low, comme le fait le schéma du cours. "
        "{st.1}{st.2}Mille neuf cent trente et un : la Mandchourie. Aucune sanction. "
        "{st.3}{st.4}Mille neuf cent trente-cinq : l'Éthiopie. Le Royaume-Uni refuse l'embargo sur le pétrole. "
        "{st.5}{st.6}Mille neuf cent trente-six : la Rhénanie. La France et le Royaume-Uni ne bougent pas.",
        "{st.7}{st.8}Mars mille neuf cent trente-huit : l'Anschluss. {st.9}{st.10}Septembre mille neuf cent trente-huit : Munich. "
        "{st.11}{st.12}Mars mille neuf cent trente-neuf : Prague. Munich n'a rien acheté. "
        "{st.13}{st.14}Et le premier septembre mille neuf cent trente-neuf : la Pologne. La guerre. "
        "Chaque concession a été suivie d'une {!exigence plus grande}exigence plus grande. C'est l'argument central contre l'apaisement.",
        "{-st}{ch}La chaîne du cours comble les années intermédiaires. {ch.1}Mille neuf cent trente-trois : l'Allemagne et le Japon quittent la SDN. {ch.2}Mille neuf cent trente-cinq : l'Éthiopie. "
        "{ch.3}Mille neuf cent trente-six : la Rhénanie, et l'Espagne. {ch.4}Mille neuf cent trente-sept : le Japon envahit le sud de la Chine, et l'Italie quitte la SDN. "
        "{ch.5}{ch.6}{ch.7}Puis l'Autriche, Munich, Prague et la Pologne. À chaque fois, l'absence de réaction encourage l'étape suivante.",
        "{-ch}{vo}Voici la phrase qui répond à la problématique du chapitre. "
        "{vo.g}L'idéologie totalitaire a fourni {!la volonté}la volonté d'expansion. "
        "{vo.d}La réticence des démocraties a fourni {!l'occasion}l'occasion.",
        ("P", 2.0),
    ], vis={
        "st": dict(type="graphe", titre="Les marches vers la guerre, 1931-1939 (d'après David Low, 1936)", x=140, y=100, w=1000, h=540,
                   ax=dict(x=[0.4, 7.6], y=[0, 9.2], gx=[], gy=[], lx="", ly=""), el=marches(MARCHES)),
        "ch": dict(type="liste", titre="La chaîne du cours", petit=True, items=[
            "1933 · L'Allemagne et le Japon quittent la SDN", "1935 · L'Italie envahit l'Éthiopie", "1936 · La Rhénanie ; l'Espagne",
            "1937 · Le Japon envahit le sud de la Chine ; l'Italie quitte la SDN", "1938 · L'Anschluss ; Munich", "Mars 1939 · Prague",
            "1er septembre 1939 · La Pologne"], x=150, y=100, w=980),
        "vo": dict(type="cols", g="L'idéologie totalitaire", gq="la volonté d'expansion : la guerre comme valeur, le Lebensraum, l'empire",
                   d="La réticence des démocraties", dq="l'occasion : la SDN, l'apaisement, l'isolationnisme", vs="+",
                   repere="La réponse à la problématique"),
    }),

    # ================================================================ à toi : analyse du discours de l'Obersalzberg (DBQ 3 a)
    dict(id="dbq3a", chap="À toi · analyse de document", fond="guerre", humeur="tension",
         retenir="Le discours de l'Obersalzberg (22 août 1939) : Hitler à ses commandants en chef, dix jours avant la Pologne · intérêt : un auditoire fermé, la date, une guerre préparée, sa lecture des démocraties, un quasi-silence sur le Lebensraum · limites : des notes d'auditeurs (798-PS), le but du discours, une cause immédiate et non profonde, des silences, une intention seulement.",
         beats=[
        "{doc3}À toi maintenant, avec un autre document du chapitre. {doc3.1}C'est un discours d'Adolf Hitler à ses commandants en chef. "
        "Il le prononce à l'Obersalzberg, sa résidence de montagne, le vingt-deux août mille neuf cent trente-neuf. Dix jours avant l'invasion de la Pologne. "
        "{doc3.2}C'est une réunion militaire à huis clos. On le connaît par des notes prises par des auditeurs, produites au procès de Nuremberg "
        "sous la cote sept cent quatre-vingt-dix-huit P S. {-doc3}Hitler déclare :",
        ("C", "Un conflit avec la Pologne devait éclater tôt ou tard.", "c_h1"),
        "{-c_h1}De ses adversaires, il dit :",
        ("C", "Il n'y a pas de personnalité marquante en Angleterre et en France.", "c_h2"),
        "{-c_h2}Et enfin :",
        ("C", "Nous n'avons rien à perdre ; nous avons tout à gagner.", "c_h3"),
        "{-c_h3}{ex3}La consigne : présentez le document, puis montrez {!son intérêt et ses limites}son intérêt et ses limites pour comprendre le rôle "
        "de l'expansionnisme territorial parmi les causes profondes de la Seconde Guerre mondiale.",
        "{-ex3}{str}Rappelle-toi la démarche. {str.1}D'abord, la présentation : la nature du document, son auteur, sa date, son destinataire. "
        "{str.2}Ensuite, le contexte : où en est l'Europe, ce jour-là ? {str.3}Puis l'intérêt du document, avec plusieurs arguments. "
        "{str.4}Et enfin ses limites, avec plusieurs arguments, jusqu'à un bilan critique.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep3}Voici un modèle, tiré de la réponse du site. {rep3.1}Ce document est un discours prononcé par Hitler devant ses commandants en chef, "
        "le vingt-deux août mille neuf cent trente-neuf. Il leur annonce qu'il a décidé d'attaquer la Pologne. "
        "{rep3.2}Le contexte : Prague est occupée depuis mars, le Royaume-Uni et la France ont garanti la Pologne, "
        "et le pacte avec l'Union soviétique est signé le lendemain.",
        "{rep3.3}Son intérêt. Un auditoire fermé : Hitler n'a aucune raison d'adoucir ses intentions. "
        "La date : le moment exact où l'expansion devient la guerre. Une guerre préparée, pas improvisée : un conflit devait éclater tôt ou tard. "
        "L'effet de l'apaisement : pas de personnalité marquante en Angleterre et en France. "
        "Et ce qu'il ne voulait pas dire : il parle à peine du Lebensraum, ou de la race.",
        "{rep3.4}Ses limites. Ce sont des notes d'auditeurs, en plusieurs versions, produites à Nuremberg : pas un texte mot pour mot. "
        "Le discours veut rassurer les généraux, donc Hitler exagère les atouts allemands. "
        "Il montre une décision immédiate, pas une cause profonde : pour cela, il faut Mein Kampf. "
        "Il ne dit rien de l'économie, de la race ou de la SDN. Et il montre une intention, jamais ce qui s'est réellement passé. "
        "Le bilan critique : un document d'un grand intérêt, mais qui saisit la dernière marche plutôt que tout le chemin.",
    ], vis={
        "doc3": dict(type="liste", titre="Le document · le discours de l'Obersalzberg", items=[
            "Hitler à ses commandants en chef, Obersalzberg, 22 août 1939 : dix jours avant la Pologne",
            "Une réunion à huis clos, connue par des notes d'auditeurs (document 798-PS de Nuremberg)"], x=150, y=150, w=980),
        "c_h1": dict(type="cit", a="Adolf Hitler", o="discours de l'Obersalzberg, 22 août 1939", x=200, y=210, w=880),
        "c_h2": dict(type="cit", a="Adolf Hitler", o="discours de l'Obersalzberg, 22 août 1939", x=200, y=210, w=880),
        "c_h3": dict(type="cit", a="Adolf Hitler", o="discours de l'Obersalzberg, 22 août 1939", x=200, y=210, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="Présentez le document, puis montrez son intérêt et ses limites pour comprendre le rôle de l'expansionnisme territorial parmi les causes profondes de la Seconde Guerre mondiale.",
                    src="Document du chapitre (discours de l'Obersalzberg) ; consigne écrite pour cette vidéo",
                    enonce=["Analyse de document · présenter, expliquer, critiquer"],
                    donnees=["Hitler, Obersalzberg, 22 août 1939 : « un conflit avec la Pologne devait éclater tôt ou tard » … « Nous n'avons rien à perdre ; nous avons tout à gagner »"]),
        "str": dict(type="liste", titre="Analyse de document : la démarche", cles=["présentation", "contexte", "intérêt", "limites"], items=[
            "La présentation : nature, auteur, date, destinataire", "Le contexte : la situation du moment",
            "L'intérêt : plusieurs arguments", "Les limites : plusieurs arguments, puis un bilan critique"], x=150, y=130, w=980),
        "pa1": dict(type="pause", t="Rédige la présentation et le contexte, puis l'intérêt et les limites du document.",
                    sous="Mets la vidéo en pause, écris ta réponse, puis relance pour voir un modèle."),
        "rep3": dict(type="liste", titre="Un modèle de réponse", petit=True, items=[
            "Présentation : Hitler à ses commandants en chef, 22 août 1939 : il a décidé d'attaquer la Pologne",
            "Contexte : Prague occupée, la Pologne garantie, le pacte signé le lendemain",
            "Intérêt : auditoire fermé · date · guerre préparée · sa lecture des démocraties · quasi-silence sur le Lebensraum",
            "Limites : notes d'auditeurs (798-PS) · but du discours · immédiat, pas profond · silences · une intention seulement → bilan critique"],
            x=130, y=130, w=1020),
    }),

    # ================================================================ à toi : question problématisée (DBQ 3 b)
    dict(id="dbq3b", chap="À toi · question problématisée", fond="nuit", humeur="tension",
         retenir="L'idéologie a fait de la guerre une valeur et de l'expansion un but (fascisme, Lebensraum, Japon) · mais les démocraties ont laissé l'agression réussir (SDN, apaisement, isolationnisme) · les deux ont formé une chaîne que seule la guerre pouvait rompre → l'idéologie la volonté, les démocraties l'occasion.",
         beats=[
        "{ex4}Allons plus loin que le document, avec tes connaissances. Voici une question problématisée, écrite pour cette vidéo, sur la problématique du chapitre. "
        "{!Dans quelle mesure}Dans quelle mesure l'idéologie totalitaire est-elle la cause principale de la Seconde Guerre mondiale ?",
        "{-ex4}{pa2}",
        ("P", 2.0),
        "{-pa2}{pb}Un plan modèle, tiré de la composition du cours sur cette problématique. {pb.1}En introduction, définis le totalitarisme. "
        "Puis définis la paix qu'il menace : l'ordre de mille neuf cent dix-neuf, garanti par la Société des Nations. Ensuite, trois parties.",
        "{pb.2}Première partie. Les idéologies totalitaires font de la guerre une valeur, et de l'expansion un but. Le fascisme fait de la guerre l'épreuve suprême : l'Abyssinie, en mille neuf cent trente-cinq. "
        "Le nazisme transforme le Lebensraum en programme, dans Mein Kampf. Le Japon cherche l'autarcie : la Mandchourie, puis Nankin.",
        "{pb.3}Deuxième partie. Mais les démocraties laissent l'agression réussir. Face à l'Abyssinie, la SDN discute de sanctions, et épargne le pétrole. "
        "Puis vient l'apaisement : l'accord naval, la Rhénanie, Munich. Et l'isolationnisme américain, avec les lois de neutralité de mille neuf cent trente-cinq à trente-sept.",
        "{pb.4}Troisième partie. Les deux se combinent en une chaîne que seule la guerre peut rompre. La Rhénanie apprend à Hitler que les démocraties céderont. "
        "Prague met fin à l'apaisement. Et le pacte germano-soviétique ouvre la route de la Pologne.",
        "{pb.5}Et la conclusion. L'idéologie totalitaire est la cause principale, parce qu'elle fournit la volonté de faire la guerre. "
        "Mais elle n'est pas la seule. La réticence des démocraties fournit l'occasion.",
    ], vis={
        "ex4": dict(type="exo", niveau="essay", titre="Dans quelle mesure l'idéologie totalitaire est-elle la cause principale de la Seconde Guerre mondiale ?",
                    src="Question écrite pour cette vidéo, sur la problématique du chapitre", enonce=["Réponse à une question problématisée · tes connaissances"]),
        "pa2": dict(type="pause", t="Écris un plan : trois parties, un exemple précis chacune, et une conclusion qui répond.",
                    sous="Mets la vidéo en pause, écris ton plan, puis relance pour voir un modèle."),
        "pb": dict(type="liste", titre="Un plan modèle", petit=True, items=[
            "Introduction : définir le totalitarisme · la paix de 1919, garantie par la SDN",
            "L'idéologie fait de la guerre une valeur : l'Abyssinie 1935 · le Lebensraum (Mein Kampf) · l'autarcie japonaise · le discours de l'Obersalzberg",
            "Mais les démocraties laissent l'agression réussir : la SDN et le pétrole · l'apaisement · les lois de neutralité",
            "Les deux forment une chaîne que seule la guerre peut rompre : Rhénanie → Prague → le pacte → la Pologne",
            "Conclusion : la cause principale (la volonté), pas la seule (l'occasion)"], x=130, y=120, w=1020),
    }),

    # ================================================================ conclusion : l'idéologie a-t-elle causé la guerre ?
    dict(id="conclusion", chap="L'idéologie totalitaire a-t-elle causé la guerre ?", fond="aube", humeur="lumiere",
         retenir="La réponse du chapitre : l'idéologie totalitaire a fourni la volonté de guerre ; la réticence des démocraties a fourni l'occasion. Garder les deux moitiés. Ensuite : le chapitre 3, la Seconde Guerre mondiale.",
         beats=[
        "{qc}Revenons donc à la question de tout le chapitre. L'idéologie totalitaire a-t-elle causé la guerre ?",
        "{-qc}{rep4}{rep4.g}Oui, dans une large mesure. Les trois régimes reposent sur des idéologies qui font de la guerre une valeur, et de l'expansion un but. "
        "La nation et l'empire de Rome. La race et son espace vital. Et l'empire du Japon en Asie. "
        "{rep4.d}Mais pas à elle seule. Entre mille neuf cent trente-cinq et mille neuf cent trente-neuf, chaque agression réussit parce que les démocraties la laissent réussir. "
        "Une bonne réponse garde {!les deux moitiés}les deux moitiés.",
        "{-rep4}{lien}Et c'est là que commence le chapitre suivant. Chapitre trois : la Seconde Guerre mondiale. "
        "{lien.1}La guerre qui commence en Pologne est la guerre de ces régimes. "
        "{lien.2}La défaite de la France, en mille neuf cent quarante. {lien.3}Barbarossa, en mille neuf cent quarante et un : une guerre d'anéantissement pour l'espace vital à l'Est. "
        "{lien.4}Et le génocide des Juifs d'Europe. Les idéologies de ce chapitre, mises en pratique par la guerre.",
    ], vis={
        "qc": dict(type="question", t="L'idéologie totalitaire a-t-elle causé la guerre ?"),
        "rep4": dict(type="cols", g="Oui, largement", gq="des idéologies qui font de la guerre une valeur et de l'expansion un but",
                     d="Mais pas à elle seule", dq="chaque agression réussit parce que les démocraties la laissent réussir", vs="+",
                     repere="La volonté + l'occasion"),
        "lien": dict(type="liste", titre="Chapitre suivant · la Seconde Guerre mondiale", items=[
            "Septembre 1939 : la guerre de ces régimes commence", "1940 : la défaite de la France",
            "1941 : Barbarossa, une guerre d'anéantissement pour le Lebensraum", "Le génocide des Juifs d'Europe"], x=170, y=140, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Une SDN muette, et une Amérique isolationniste. "
        "{carte.2}L'apaisement : Chamberlain et Daladier, sept raisons, et Munich. "
        "{carte.3}Les étapes : l'Axe, la Rhénanie, l'Anschluss, Prague, et le pacte. "
        "{carte.4}Et la réponse : l'idéologie a fourni la volonté, les démocraties l'occasion.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : tout le chapitre à l'épreuve. La question problématisée, l'analyse de document, des modèles. Et les pièges.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LA MARCHE À LA GUERRE", branches=[
            dict(t="III.2 · Impuissantes", items=["une SDN muette", "lois de neutralité 1935-1937", "Stresa · accord naval à 35 %"]),
            dict(t="L'apaisement", items=["Chamberlain, Daladier", "sept raisons", "Munich, sept. 1938"]),
            dict(t="III.3 · Les étapes", items=["l'Axe · l'Espagne 1936", "Rhénanie · Anschluss", "Prague · le pacte 1939"]),
            dict(t="La réponse", items=["l'idéologie : la volonté", "les démocraties : l'occasion", "3 sept. 1939 : la guerre"])]),
        "fin": dict(type="mot", t="Prochain : le chapitre à l'épreuve", g="Épisode 8 · question problématisée et analyse de document", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="Que dénonce le dessin de David Low du 24 juillet 1935, « Sur le trône de la Justice » ?",
         r=["La SDN qui ne voit, n'entend et ne dit rien de l'Abyssinie", "L'Anschluss",
            "Le pacte germano-soviétique", "L'isolationnisme américain"], ok=0, voir="low1",
         ex="Trois singes marqués « Abyssinie » sur le trône du droit international : ne rien voir, ne rien entendre, ne rien dire."),
    dict(q="Qu'interdisent les lois de neutralité américaines de 1935, 1936 et 1937 ?",
         r=["Les ventes d'armes et les prêts aux pays en guerre", "Tout commerce avec l'Allemagne", "L'adhésion à la SDN",
            "Le réarmement de la marine américaine"], ok=0, voir="us",
         ex="Écrire « un Congrès isolationniste » : les démocrates y sont majoritaires de 1935 à 1939."),
    dict(q="Qu'autorise l'accord naval germano-britannique de juin 1935 ?",
         r=["Une marine allemande à 35 % du tonnage de la Royal Navy", "La remilitarisation de la Rhénanie",
            "Une marine allemande égale à la Royal Navy", "Une alliance germano-britannique contre l'Italie"], ok=0, voir="pct",
         ex="Signé par le Royaume-Uni seul, deux mois après Stresa : le Royaume-Uni rend lui-même légale une violation de Versailles."),
    dict(q="Laquelle n'est PAS l'une des raisons de l'apaisement données par le cours ?",
         r=["Une alliance militaire avec l'URSS", "Le souvenir de 1914-1918 et le pacifisme", "La peur du communisme",
            "L'isolationnisme américain"], ok=0, voir="wh",
         ex="Beaucoup, au Royaume-Uni et en France, craignent le communisme plus que le fascisme."),
    dict(q="Qui n'est PAS présent à la conférence de Munich des 29 et 30 septembre 1938 ?",
         r=["Les Tchèques", "Mussolini", "Daladier", "Chamberlain"], ok=0, voir="mu",
         ex="Les Sudètes sont livrées sans que les Tchèques soient invités."),
    dict(q="Qu'apprend la Rhénanie (7 mars 1936) à Hitler ?",
         r=["Que les démocraties céderont", "Que l'armée française est plus forte que la sienne", "Que l'Italie le suivra toujours",
            "Que la SDN peut imposer des sanctions"], ok=0, voir="pari",
         ex="Ses troupes avaient l'ordre de se retirer si la France réagissait ; elle n'a pas réagi."),
    dict(q="Pourquoi Prague (15 mars 1939) met-elle fin à l'apaisement ?",
         r=["Il ne s'agit plus de réunir des Allemands mais d'occuper un peuple étranger", "C'est la première violation de Versailles",
            "L'Allemagne attaque la France", "L'URSS rejoint l'Axe"], ok=0, voir="diff",
         ex="Le 31 mars 1939, la France et le Royaume-Uni garantissent la Pologne."),
    dict(q="Selon le cours, qu'a fourni la réticence des démocraties sur la route de la guerre ?",
         r=["L'occasion", "La volonté d'expansion", "L'idéologie", "Les alliances"], ok=0, voir="vo",
         ex="L'idéologie totalitaire a fourni la volonté d'expansion ; la réticence des démocraties, l'occasion."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre « Les régimes totalitaires » (parties III.2 et III.3, schémas « L'apaisement : ce qu'il a cédé, et pourquoi » "
    "et « Les marches vers la guerre », le télégramme de Roosevelt du 14 avril 1939 et le discours de l'Obersalzberg du 22 août 1939, avec les réponses modèles du site) ; "
    "la question problématisée écrite pour cette vidéo sur la problématique du chapitre ; Guernica donné comme exemple complémentaire, hors de la leçon ; "
    "la part des Juifs dans la population autrichienne ajoutée hors du cours ; la carte animée du chapitre (site).",
    "Photographies (via Wikimedia Commons) : les accords de Munich, 29 septembre 1938 (Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE) ; Chamberlain à l'aéroport de Heston, 30 septembre 1938 (Imperial War Museums, D 2239, domaine public) ; les ruines de Guernica, 1937 (Bundesarchiv, Bild 183-H25224, CC BY-SA 3.0 DE) ; Hitler sur la Heldenplatz, Vienne, 15 mars 1938 (Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE) ; Staline et Ribbentrop, Moscou, 23 août 1939 (Helmut Laux, Bundesarchiv, Bild 183-H27337, CC BY-SA 3.0 DE).",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
