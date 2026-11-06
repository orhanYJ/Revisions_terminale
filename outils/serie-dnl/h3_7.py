"""DNL History · H3 « World War Two » — série vidéo, épisode 7 : « Recap » (tout le chapitre).

Même chaîne que l'épisode 1 (voir h3_1.py). Contenu : la synthèse du chapitre dans le site (bigPicture, frise de la fiche
PDF, chiffres et personnages clés, key terms), avec la carte animée H3 (numéros de scènes : voir h3_1.py).
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-7"
NOTION = "World War Two"
NUM = 7
TITRE = "Recap"
SUIVANT = "The end of the series · back to the course and the quiz"
PRONONCIATION = {"Grossraum": "Gross-rowm", "Lebensraum": "Lay-bens-rowm", "Rethondes": "Ruh-tond", "Pétain": "Pay-tan",
                 "Vichy": "Vee-shee", "Wehrmacht": "Vair-markt", "Einsatzgruppen": "Ine-zats-groopen", "Paulus": "Pow-loos",
                 "Treblinka": "Treb-linka", "Chelmno": "Hel-mno", "Reichstag": "Rikes-tahg", "Aglan": "Ag-lan"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{q1}The whole chapter, in one go. Everything you need to remember about the Second World War, from 1931 to 1943, "
        "on the map, then in a few tables.",
        "{-q1}{titre}",
        ("P", 3.0),
    ], vis={
        "q1": dict(type="question", t="The whole chapter, in one go."),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 7", t="Recap",
                      sous="World War Two · 1931 – 1943"),
    }),

    # ================================================================ I. le film de la guerre
    dict(id="film", chap="The war on the map", fond="nuit", humeur="tension",
         retenir="1931 Manchuria · 1937 China · 1 Sept. 1939 Poland · May–June 1940 France · 1940–41 Britain alone · 22 June 1941 Barbarossa · Dec. 1941 global war · 1942 the genocide · 2 Feb. 1943 Stalingrad.",
         beats=[
        "{g1}{g1.1}It begins in Asia. 1931: Japan seizes Manchuria; the League of Nations condemns, and does nothing. "
        "{g1.2}1937: Japan attacks southern China. For Robert Frank and Alya Aglan, the world war begins here.",
        "{g1.3}In Europe, the first of September 1939: Germany invades Poland, after its pact with the Soviet Union. "
        "{g1.4}In the West, the phoney war, then, on the tenth of May 1940, the attack. {g1.5}The breakthrough of the Ardennes. "
        "{g1.6}Dunkirk: three hundred and thirty-eight thousand soldiers evacuated.",
        "{g1.7}On the twenty-second of June 1940, at Rethondes, France signs the armistice: a country cut into zones, "
        "the Vichy regime, and collaboration.",
        "{g1.8}Britain is alone. Churchill refuses to negotiate; the Blitz fails to break it, {g1.9}and the United States becomes its supplier.",
        "{-g1}{g2}{g2.1}On the twenty-second of June 1941, Barbarossa: the war of annihilation in the East. {g2.2}The Einsatzgruppen follow the army "
        "and shoot the Jews: the Shoah by bullets. {g2.3}In December 1941, the Germans are stopped before Moscow, "
        "{g2.4}Japan attacks Pearl Harbor, and the war becomes global.",
        "{g2.5}From December 1941, six killing centres in occupied Poland: the genocide becomes industrial. "
        "{g2.6}In 1942, Germany strikes towards Stalingrad and the Caucasus… {g2.7}and on the thirty-first of January 1943, Paulus surrenders. The battle ends two days later: "
        "the turning point of the war. {g2.8}At the end, six million Jews murdered: two thirds of the Jews of Europe.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[1, 3, 5, 11, 12, 13, 16, 17, 21]),
        "g2": dict(type="globe", code="H3", sc=[25, 27, 30, 31, 32, 36, 42, 45]),
    }),

    # ================================================================ II. dix dates
    dict(id="dates", chap="Ten dates", fond="nuit", humeur="calme",
         retenir="1937 · 1 Sept. 1939 · 18 June 1940 · 22 June 1940 · 22 June 1941 · Dec. 1941 · July 1942 · 11 Nov. 1942 · 31 Jan. 1943 · 19 Apr. 1943.",
         beats=[
        "{fr}Ten dates to know by heart. {fr.1}1937, Japan attacks southern China. {fr.2}The first of September 1939, Germany invades Poland. "
        "{fr.3}The eighteenth of June 1940, de Gaulle's appeal from London. {fr.4}The twenty-second of June 1940, the armistice of Rethondes. "
        "{fr.5}The twenty-second of June 1941, Operation Barbarossa. {fr.6}December 1941, Pearl Harbor, and the first killing centre, Chelmno. "
        "{fr.7}July 1942, Treblinka is built, and Jews are rounded up in France. {fr.8}The eleventh of November 1942, Germany invades the free zone. "
        "{fr.9}The thirty-first of January 1943, Paulus surrenders at Stalingrad. {fr.10}And the nineteenth of April 1943, the Warsaw ghetto uprising.",
        ("P", 3.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="China", d=1937, q="Japan attacks"), dict(nom="Poland", d=1939, q="1 Sept."),
            dict(nom="De Gaulle", d=1940, q="18 June"), dict(nom="Armistice", d=1940, q="22 June"),
            dict(nom="Barbarossa", d=1941, q="22 June"), dict(nom="Pearl Harbor", d=1941, q="7 Dec."),
            dict(nom="Treblinka", d=1942, q="July"), dict(nom="Free zone", d=1942, q="11 Nov."),
            dict(nom="Stalingrad", d=1943, q="31 Jan."), dict(nom="Warsaw ghetto", d=1943, q="19 Apr.")]),
    }),

    # ================================================================ III. les idées
    dict(id="idees", chap="The ideas", fond="guerre", humeur="tension",
         retenir="A world war (1931/1937–1947) · an ideological war · the New European Order and its five driving forces · France exploited · Britain holds · annihilation in the East · the genocide.",
         beats=[
        "{i1}And now the ideas, part by part. {i1.1}The introduction: a world war, which began in Asia; an ideological war, "
        "about sixty million dead; and the New European Order, Nazi rule presented as saving Europe.",
        "{i1.2}Part one, the West. France falls in six weeks: an outdated strategy, the surprise of the Ardennes, the Blitzkrieg. "
        "Cut into zones, governed by Vichy, which chooses collaboration, it is exploited: twenty million Reichsmarks a day, "
        "and some eighty thousand Jews deported, of whom about three per cent survived.",
        "{i1.3}Britain holds: the Luftwaffe never wins control of the air, Churchill and de Gaulle bet on a world war, "
        "and the United States supplies it before entering the war in December 1941.",
        "{i1.4}Part two, the East. Three reasons to invade the Soviet Union: economic, the Grossraum; ideological, Jewish Bolshevism; "
        "racial, the Übermensch against the Untermensch. A war of annihilation: commissars shot, about two point eight million "
        "Soviet prisoners killed, scorched earth. And Stalingrad, the turning point, which fits the definition of total war.",
        "{i1.5}Part three, the genocide. The Jews of Europe, stranded under Nazi rule; the ghettos; the Einsatzgruppen and the Shoah by bullets; "
        "the six killing centres, Treblinka and its eight hundred and seventy-six thousand dead. Six million Jews murdered.",
    ], vis={
        "i1": dict(type="liste", titre="The ideas of the chapter", items=[
            "Intro: a world war · an ideological war · the New European Order",
            "I.1 France: defeat in six weeks, zones, Vichy, exploitation, persecution",
            "I.2 Britain holds: the air battle, Churchill and de Gaulle, American supplies",
            "II The East: three reasons, annihilation, Stalingrad and total war",
            "III The genocide: ghettos, Einsatzgruppen, killing centres, 6 million"], x=130, y=110, w=1020),
    }),

    # ================================================================ IV. chiffres, personnages, mots
    dict(id="chiffres", chap="Figures, people, key terms", fond="nuit", humeur="calme",
         retenir="≈ 60 million dead · 338,000 at Dunkirk · 20 million RM a day · 5 million dead in 200 days · 3/5 on the Eastern Front · 6 million Jews. Key terms: New European Order, Lebensraum.",
         beats=[
        "{ch}Six figures. {ch.1}About sixty million dead in the war. {ch.2}Three hundred and thirty-eight thousand soldiers evacuated from Dunkirk. "
        "{ch.3}Twenty million Reichsmarks a day paid by France. {ch.4}Five million dead in the two hundred days of Barbarossa, a thousand an hour. "
        "{ch.5}Three fifths of all the dead on the Eastern Front. {ch.6}Six million Jews murdered.",
        "{-ch}{pe}Eight people. {pe.1}Pétain, head of Vichy, who chose collaboration. {pe.2}De Gaulle, who refused the armistice. "
        "{pe.3}Churchill, who kept Britain fighting alone. {pe.4}Stalin, and his speech of the sixth of November 1941. "
        "{pe.5}Paulus, who capitulated at Stalingrad. {pe.6}Himmler and {pe.7}Stroop, who crushed the Warsaw ghetto. "
        "{pe.8}And Robert Frank, for the chronology of the world war.",
        "{-pe}{kt}And the two key terms. {kt.1}The New European Order. {kt.2}And Lebensraum, living space in the East.",
    ], vis={
        "ch": dict(type="liste", titre="Six figures", items=[
            "≈ 60 million dead", "338,000 evacuated from Dunkirk", "20 million RM a day paid by France",
            "5 million dead in 200 days of Barbarossa", "3/5 of the dead on the Eastern Front", "6 million Jews murdered"],
            x=170, y=110, w=940),
        "pe": dict(type="nuage", items=["Pétain", "de Gaulle", "Churchill", "Stalin", "Paulus", "Himmler", "Stroop", "Robert Frank"]),
        "kt": dict(type="cols", g="New European Order", gq="Nazi rule over Europe, presented as saving its civilisation",
                   d="Lebensraum", dq="living space in the East, conquered with Barbarossa", vs="+"),
    }),

    # ================================================================ récap final
    dict(id="fin", chap="The whole chapter", fond="nuit", humeur="calme", beats=[
        "{carte}One last map of the chapter. {carte.1}A world war, from Asia to Europe. {carte.2}The West: France defeated and exploited, "
        "Britain holding. {carte.3}The East: a war of annihilation, and the turning point of Stalingrad. "
        "{carte.4}The genocide: six million Jews murdered. {carte.5}And at the centre, the New European Order, with its five driving forces.",
        ("P", 5.0),
        "{-carte}{fin}That is the end of the series. Now go back to the course on the site, do the quiz of the chapter… "
        "and write one essay on this chapter before the exam.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="WORLD WAR TWO", branches=[
            dict(t="A world war", items=["1931 / 1937 – 1947", "ideological · 60 million"]),
            dict(t="The West", items=["France: six weeks, Vichy", "Britain holds"]),
            dict(t="The East", items=["Barbarossa · annihilation", "Stalingrad, Feb. 1943"]),
            dict(t="The genocide", items=["ghettos · bullets · gas", "6 million Jews"]),
            dict(t="New European Order", items=["race · Lebensraum", "Grossraum · total war"])]),
        "fin": dict(type="mot", t="Your turn now", g="the course, the quiz, one essay", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="For Robert Frank and Alya Aglan, when does the world war begin?", r=["1937", "1939", "1941", "1914"], ok=0, voir="g1",
         ex="Japan's attack on southern China; the chronology can even start in 1931."),
    dict(q="When did France sign the armistice?", r=["22 June 1940", "18 June 1940", "10 May 1940", "11 November 1942"], ok=0, voir="fr",
         ex="At Rethondes; de Gaulle's appeal was on 18 June."),
    dict(q="Which is NOT one of the three reasons for invading the USSR?", r=["Restoring the Tsar", "The Grossraum and its resources",
         "The crusade against “Jewish Bolshevism”", "The Übermensch against the Untermensch"], ok=0, voir="i1",
         ex="Economic, ideological, racial."),
    dict(q="When did Paulus surrender at Stalingrad?", r=["31 January 1943", "22 June 1941", "7 December 1941", "19 April 1943"], ok=0,
         voir="fr", ex="The last German troops gave up on 2 February: the turning point of the war."),
    dict(q="How many people were killed at Treblinka?", r=["876,000", "6 million", "338,000", "60,000"], ok=0, voir="i1",
         ex="874,000 Jews and 2,000 Roma (Worksheet 4)."),
    dict(q="What share of all the dead of WWII died on the Eastern Front?", r=["Three fifths", "One tenth", "A quarter", "Half"], ok=0,
         voir="ch", ex="The war of annihilation: armies and civilians."),
    dict(q="Which key term means “living space” in the East?", r=["Lebensraum", "Grossraum", "Blitzkrieg", "Untermensch"], ok=0,
         voir="kt", ex="The Grossraum is the single economic space; Lebensraum, the land to conquer for German settlers."),
    dict(q="How much did occupied France pay in occupation fees?", r=["20 million Reichsmarks a day", "20 million a year",
         "Nothing: it was a partner", "1 million francs a month"], ok=0, voir="ch",
         ex="Plus requisitions and, from 1942, the STO."),
]

CREDITS = [
    "Content: the synthesis of M. Ros's course (DNL History, H3) as written on the site; the animated map of the chapter (site).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
