"""Histoire · H3 « La Seconde Guerre mondiale » — édition française, épisode 7 : « Récap » (tout le chapitre).

Traduction adaptée de h3_7.py, d'après outils/serie-dnl/EDITION_FR.md. Contenu : la synthèse du chapitre dans le site
(frise, chiffres et personnages clés, notions clés), avec la carte animée H3 (mêmes numéros de scènes que l'édition anglaise :
voir h3_1.py ; la carte passe d'elle-même en français).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-7"
NOTION = "La Seconde Guerre mondiale"
NUM = 7
TITRE = "Récap"
SUIVANT = "Fin de la série · retour au cours et au quiz"
PRONONCIATION = {"Grossraum": "Gross-raoum", "Lebensraum": "Lé-benss-raoum", "Übermensch": "Ubeur-mènch",
                 "Untermensch": "Ountère-mènch", "Einsatzgruppen": "Aïne-zats-groupen", "Luftwaffe": "Louft-vaffe",
                 "Reichsmarks": "Raïchs-marks", "Chelmno": "Khèlm-no", "Stroop": "Strôp", "Pearl Harbor": "Peurl Arbor"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{q1}Tout le chapitre, d'un seul tenant. Tout ce qu'il faut retenir de la Seconde Guerre mondiale, de 1931 à 1943, "
        "sur la carte, puis en quelques tableaux.",
        "{-q1}{titre}",
        ("P", 3.0),
    ], vis={
        "q1": dict(type="question", t="Tout le chapitre, d'un seul tenant."),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 7", t="Récap",
                      sous="La Seconde Guerre mondiale · 1931 – 1943"),
    }),

    # ================================================================ I. le film de la guerre
    dict(id="film", chap="La guerre sur la carte", fond="nuit", humeur="tension",
         retenir="1931 Mandchourie · 1937 Chine · 1er sept. 1939 Pologne · mai-juin 1940 France · 1940-1941 le Royaume-Uni seul · 22 juin 1941 Barbarossa · déc. 1941 guerre mondiale · 1942 le génocide · 2 févr. 1943 Stalingrad.",
         beats=[
        "{g1}{g1.1}Tout commence en Asie. 1931 : le Japon s'empare de la Mandchourie ; la Société des Nations condamne, et ne fait rien. "
        "{g1.2}1937 : le Japon envahit la Chine, au sud de la Mandchourie. Pour Robert Frank et Alya Aglan, c'est là que commence la guerre mondiale.",
        "{g1.3}En Europe, le premier septembre 1939 : l'Allemagne envahit la Pologne, après son pacte avec l'Union soviétique. "
        "{g1.4}À l'Ouest, la drôle de guerre, puis, le dix mai 1940, l'attaque. {g1.5}La percée des Ardennes. "
        "{g1.6}Dunkerque : trois cent trente-huit mille soldats évacués.",
        "{g1.7}Le vingt-deux juin 1940, à Rethondes, la France signe l'armistice : un pays découpé en zones, "
        "le régime de Vichy, et la collaboration.",
        "{g1.8}Le Royaume-Uni est seul. Churchill refuse de négocier ; le Blitz ne parvient pas à le briser, {g1.9}et les États-Unis deviennent son fournisseur.",
        "{-g1}{g2}{g2.1}Le vingt-deux juin 1941, Barbarossa : la guerre d'anéantissement à l'Est. {g2.2}Les Einsatzgruppen suivent l'armée "
        "et fusillent les Juifs : c'est la Shoah par balles. {g2.3}En décembre 1941, les Allemands sont arrêtés devant Moscou, "
        "{g2.4}le Japon attaque Pearl Harbor, et la guerre devient mondiale.",
        "{g2.5}À partir de décembre 1941, six centres de mise à mort en Pologne occupée : le génocide devient industriel. "
        "{g2.6}En 1942, l'Allemagne frappe vers Stalingrad et le Caucase… {g2.7}et le trente et un janvier 1943, Paulus capitule. "
        "La bataille s'achève deux jours plus tard : c'est le tournant de la guerre. {g2.8}Au bout du compte, six millions de Juifs assassinés : "
        "les deux tiers des Juifs d'Europe.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[1, 3, 5, 11, 12, 13, 16, 17, 21]),
        "g2": dict(type="globe", code="H3", sc=[25, 27, 30, 31, 32, 36, 42, 45]),
    }),

    # ================================================================ II. dix dates
    dict(id="dates", chap="Dix dates", fond="nuit", humeur="calme",
         retenir="1937 · 1er sept. 1939 · 18 juin 1940 · 22 juin 1940 · 22 juin 1941 · déc. 1941 · juillet 1942 · 11 nov. 1942 · 31 janv. 1943 · 19 avr. 1943.",
         beats=[
        "{fr}Dix dates à savoir par cœur. {fr.1}1937, le Japon attaque la Chine. {fr.2}Le premier septembre 1939, l'Allemagne envahit la Pologne. "
        "{fr.3}Le dix-huit juin 1940, l'appel du général de Gaulle, depuis Londres. {fr.4}Le vingt-deux juin 1940, l'armistice de Rethondes. "
        "{fr.5}Le vingt-deux juin 1941, l'opération Barbarossa. {fr.6}Décembre 1941, Pearl Harbor, et le premier centre de mise à mort, Chelmno. "
        "{fr.7}Juillet 1942, Treblinka entre en service, et des Juifs sont raflés en France. {fr.8}Le onze novembre 1942, l'Allemagne envahit la zone libre. "
        "{fr.9}Le trente et un janvier 1943, Paulus capitule à Stalingrad. {fr.10}Et le dix-neuf avril 1943, le soulèvement du ghetto de Varsovie.",
        ("P", 3.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Chine", d=1937, q="le Japon attaque"), dict(nom="Pologne", d=1939, q="1er sept."),
            dict(nom="De Gaulle", d=1940, q="18 juin"), dict(nom="Armistice", d=1940, q="22 juin"),
            dict(nom="Barbarossa", d=1941, q="22 juin"), dict(nom="Pearl Harbor", d=1941, q="7 déc."),
            dict(nom="Treblinka", d=1942, q="juillet"), dict(nom="Zone libre", d=1942, q="11 nov."),
            dict(nom="Stalingrad", d=1943, q="31 janv."), dict(nom="Varsovie", d=1943, q="ghetto, 19 avr.")]),
    }),

    # ================================================================ III. les idées
    dict(id="idees", chap="Les idées", fond="guerre", humeur="tension",
         retenir="Une guerre mondiale (1931/1937-1947) · une guerre idéologique · le nouvel ordre européen et ses cinq moteurs · la France exploitée · le Royaume-Uni tient · l'anéantissement à l'Est · le génocide.",
         beats=[
        "{i1}Et maintenant, les idées, partie par partie. {i1.1}L'introduction : une guerre mondiale, qui commence en Asie ; une guerre idéologique, "
        "environ soixante millions de morts ; et le nouvel ordre européen, la domination nazie présentée comme le salut de l'Europe.",
        "{i1.2}Première partie, l'Ouest. La France tombe en six semaines : une stratégie dépassée, la surprise des Ardennes, la guerre éclair. "
        "Découpée en zones, gouvernée par Vichy, qui choisit la collaboration, elle est exploitée : vingt millions de Reichsmarks par jour, "
        "et quelque quatre-vingt mille Juifs déportés, dont environ trois pour cent ont survécu.",
        "{i1.3}Le Royaume-Uni tient : la Luftwaffe ne gagne jamais la maîtrise du ciel, Churchill et de Gaulle parient sur une guerre mondiale, "
        "et les États-Unis le ravitaillent avant d'entrer en guerre, en décembre 1941.",
        "{i1.4}Deuxième partie, l'Est. Trois raisons d'envahir l'Union soviétique : économique, le Grossraum ; idéologique, le judéo-bolchevisme ; "
        "raciale, l'Übermensch, le surhomme, contre l'Untermensch, le sous-homme. Une guerre d'anéantissement : commissaires fusillés, "
        "environ deux millions huit cent mille prisonniers soviétiques tués, terre brûlée. Et Stalingrad, le tournant, "
        "qui répond à la définition de la guerre totale.",
        "{i1.5}Troisième partie, le génocide. Les Juifs d'Europe, pris au piège sous la domination nazie ; les ghettos ; les Einsatzgruppen "
        "et la Shoah par balles ; les six centres de mise à mort, Treblinka et ses huit cent soixante-seize mille morts. Six millions de Juifs assassinés.",
    ], vis={
        "i1": dict(type="liste", titre="Les idées du chapitre", items=[
            "Intro : guerre mondiale, guerre idéologique, nouvel ordre européen",
            "I.1 La France : défaite, zones, Vichy, exploitation, persécution",
            "I.2 Le Royaume-Uni tient : le Blitz, Churchill et de Gaulle, l'aide américaine",
            "II L'Est : trois raisons, anéantissement, Stalingrad, guerre totale",
            "III Le génocide : ghettos, Einsatzgruppen, centres de mise à mort, 6 millions"], x=110, y=96, w=1060),
    }),

    # ================================================================ IV. chiffres, personnages, notions
    dict(id="chiffres", chap="Chiffres, personnages, notions clés", fond="nuit", humeur="calme",
         retenir="≈ 60 millions de morts · 338 000 à Dunkerque · 20 millions de RM par jour · 5 millions de morts en 200 jours · 3/5 sur le front de l'Est · 6 millions de Juifs. Notions clés : nouvel ordre européen, Lebensraum.",
         beats=[
        "{ch}Six chiffres. {ch.1}Environ soixante millions de morts dans la guerre. {ch.2}Trois cent trente-huit mille soldats évacués de Dunkerque. "
        "{ch.3}Vingt millions de Reichsmarks par jour payés par la France. {ch.4}Cinq millions de morts dans les deux cents jours de Barbarossa, "
        "mille par heure. {ch.5}Trois cinquièmes de tous les morts, sur le front de l'Est. {ch.6}Six millions de Juifs assassinés.",
        "{-ch}{pe}Huit personnages. {pe.1}Pétain, chef de Vichy, qui choisit la collaboration. {pe.2}De Gaulle, qui refuse l'armistice. "
        "{pe.3}Churchill, qui fait tenir le Royaume-Uni seul dans la guerre. {pe.4}Staline, et son discours du six novembre 1941. "
        "{pe.5}Paulus, qui capitule à Stalingrad. {pe.6}Himmler et {pe.7}Stroop, qui écrasent le ghetto de Varsovie. "
        "{pe.8}Et Robert Frank, pour la chronologie de la guerre mondiale.",
        "{-pe}{kt}Et les deux notions clés. {kt.1}Le nouvel ordre européen. {kt.2}Et le Lebensraum, l'espace vital à l'Est.",
    ], vis={
        "ch": dict(type="liste", titre="Six chiffres", items=[
            "≈ 60 millions de morts", "338 000 évacués de Dunkerque", "20 millions de RM par jour payés par la France",
            "5 millions de morts en 200 jours de Barbarossa", "3/5 des morts sur le front de l'Est", "6 millions de Juifs assassinés"],
            x=170, y=110, w=940),
        "pe": dict(type="nuage", items=["Pétain", "de Gaulle", "Churchill", "Staline", "Paulus", "Himmler", "Stroop", "Robert Frank"]),
        "kt": dict(type="cols", g="Nouvel ordre européen", gq="la domination nazie sur l'Europe, présentée comme le salut de sa civilisation",
                   d="Lebensraum", dq="l'espace vital à l'Est, conquis avec Barbarossa", vs="+"),
    }),

    # ================================================================ récap final
    dict(id="fin", chap="Tout le chapitre", fond="nuit", humeur="calme", beats=[
        "{carte}Une dernière carte du chapitre. {carte.1}Une guerre mondiale, de l'Asie à l'Europe. {carte.2}L'Ouest : la France vaincue et exploitée, "
        "le Royaume-Uni qui tient. {carte.3}L'Est : une guerre d'anéantissement, et le tournant de Stalingrad. "
        "{carte.4}Le génocide : six millions de Juifs assassinés. {carte.5}Et au centre, le nouvel ordre européen, avec ses cinq moteurs.",
        ("P", 5.0),
        "{-carte}{fin}C'est la fin de la série. Retourne maintenant au cours sur le site, fais le quiz du chapitre… "
        "et rédige une réponse à une question problématisée sur ce chapitre avant l'épreuve.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LA SECONDE GUERRE MONDIALE", branches=[
            dict(t="Une guerre mondiale", items=["1931 / 1937 – 1947", "idéologique · 60 millions"]),
            dict(t="L'Ouest", items=["France : six semaines, Vichy", "le Royaume-Uni tient"]),
            dict(t="L'Est", items=["Barbarossa · anéantissement", "Stalingrad, févr. 1943"]),
            dict(t="Le génocide", items=["ghettos · balles · gaz", "6 millions de Juifs"]),
            dict(t="Nouvel ordre européen", items=["race · Lebensraum", "Grossraum · guerre totale"])]),
        "fin": dict(type="mot", t="À toi maintenant", g="le cours, le quiz, une composition", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="Pour Robert Frank et Alya Aglan, quand commence la guerre mondiale ?", r=["1937", "1939", "1941", "1914"], ok=0, voir="g1",
         ex="Avec l'invasion de la Chine par le Japon ; la chronologie peut même commencer en 1931."),
    dict(q="Quand la France signe-t-elle l'armistice ?", r=["22 juin 1940", "18 juin 1940", "10 mai 1940", "11 novembre 1942"], ok=0, voir="fr",
         ex="À Rethondes ; l'appel du général de Gaulle date du 18 juin."),
    dict(q="Laquelle n'est PAS l'une des trois raisons d'envahir l'URSS ?", r=["Rétablir le tsar", "Le Grossraum et ses ressources",
         "La croisade contre le « judéo-bolchevisme »", "Le surhomme contre le sous-homme"], ok=0, voir="i1",
         ex="Économique, idéologique, raciale."),
    dict(q="Quand Paulus capitule-t-il à Stalingrad ?", r=["31 janvier 1943", "22 juin 1941", "7 décembre 1941", "19 avril 1943"], ok=0,
         voir="fr", ex="Les dernières troupes allemandes se rendent le 2 février : le tournant de la guerre."),
    dict(q="Combien de personnes sont tuées à Treblinka ?", r=["876 000", "6 millions", "338 000", "60 000"], ok=0, voir="i1",
         ex="874 000 Juifs et 2 000 Roms (étude de cas sur Treblinka)."),
    dict(q="Quelle part de tous les morts de la Seconde Guerre mondiale tombe sur le front de l'Est ?",
         r=["Trois cinquièmes", "Un dixième", "Un quart", "La moitié"], ok=0,
         voir="ch", ex="La guerre d'anéantissement : les armées et les civils."),
    dict(q="Quelle notion clé désigne l'« espace vital » à l'Est ?", r=["Lebensraum", "Grossraum", "Blitzkrieg", "Untermensch"], ok=0,
         voir="kt", ex="Le Grossraum est l'espace économique unique ; le Lebensraum, les terres à conquérir pour des colons allemands."),
    dict(q="Combien la France occupée paie-t-elle en frais d'occupation ?", r=["20 millions de Reichsmarks par jour", "20 millions par an",
         "Rien : c'est un partenaire", "1 million de francs par mois"], ok=0, voir="ch",
         ex="Sans compter les réquisitions, puis la Relève (1942) et le STO (1943)."),
]

CREDITS = [
    "Contenu : la synthèse du cours d'histoire de Terminale, chapitre « La Seconde Guerre mondiale », telle qu'elle est rédigée sur le site ; "
    "la carte animée du chapitre (site).",
    "Voix : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
