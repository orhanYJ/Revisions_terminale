"""DNL History · H3 « World War Two » — série vidéo, épisode 6 : « WWII at the exam: essay and DBQ ».

Même chaîne que l'épisode 1 (voir h3_1.py). Contenu : le format officiel de l'écrit BFI tel que le site le présente
(TRAIN_QCM, « Réflexes d'épreuve », guide élève de l'ASIBA), la structure de la question a) du DBQ imposée par Cengiz
(jugement dès la première ligne, document en une phrase, paragraphe d'atouts, paragraphe de limites), les documents du
cours (ordre de sévérité de Reichenau, 10 octobre 1941 ; discours de Staline, 7 novembre 1941 ; Worksheet 3), les points
à vérifier du chapitre (H3Check). Les sujets et les copies modèles sont écrits pour la vidéo et dits comme tels.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-6"
NOTION = "World War Two"
NUM = 6
TITRE = "WWII at the exam: essay and DBQ"
SUIVANT = "Episode 7 · Recap"
PRONONCIATION = {"Grossraum": "Gross-rowm", "Lebensraum": "Lay-bens-rowm", "Reichenau": "Rike-en-ow",
                 "Wehrmacht": "Vair-markt", "Ardennes": "Ar-den", "Rethondes": "Ruh-tond", "Pétain": "Pay-tan",
                 "Vichy": "Vee-shee", "Untermensch": "Oonter-mensh", "Reichstag": "Rikes-tahg", "Milice": "Mee-leece",
                 "Toukhatchevski": "Too-ka-chev-ski", "Paulus": "Pow-loos"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="aube", humeur="lumiere", carton=False, beats=[
        "{q1}You know the chapter. Now, can you use it? On the day of the exam, nobody will ask you to tell the story of the war. "
        "You will have to explain, to assess, to judge documents.",
        "{-q1}{plan}So this episode is a workshop. {plan.1}First, the format of the written exam. {plan.2}Then the essay: "
        "an Explain question and an Assess question, with model answers. {plan.3}Then the DBQ, the document-based question, "
        "on two documents of the course. {plan.4}And finally, the traps of this chapter: the mistakes that cost points.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "q1": dict(type="question", t="You know the chapter. Can you use it?"),
        "plan": dict(type="liste", titre="This episode, a workshop", items=[
            "The format of the written exam", "The essay: Explain, then Assess", "The DBQ: How useful, then part b)",
            "The traps of this chapter"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 6", t="WWII at the exam",
                      sous="essay · DBQ · the traps of the chapter"),
    }),

    # ================================================================ I. le format
    dict(id="format", chap="The written exam", fond="nuit", humeur="calme",
         retenir="4 hours. Sujet A: history essay + geography DBQ. Sujet B: geography essay + history DBQ. About 2 hours per question; history and geography count half each.",
         beats=[
        "{fmt}The written exam lasts four hours. {fmt.1}You choose between two papers. Sujet A: a history essay and a geography document-based question. "
        "{fmt.2}Sujet B: the reverse, a geography essay and a history DBQ. You cannot mix A and B. "
        "{fmt.3}Give about two hours to each question: history and geography each count for half the mark.",
        "{-fmt}{ess}The essay has two parts. {ess.1}Part a) usually begins with Explain: you give several well-argued reasons… "
        "and you should find yourself writing the word because. {ess.2}Part b) asks you to assess, or how far do you agree: "
        "arguments for and against, a hierarchy of factors, and a judgement. {ess.3}Treat them as two separate questions: "
        "leave a line, or write a) and b), even if the paper does not.",
        "{-ess}{dbq}The DBQ also has two parts. {dbq.1}Part a): how useful are the documents, in a given context. "
        "Strengths, limits, provenance, and the documents taken together. {dbq.2}Part b): a short essay that uses the documents "
        "and your own knowledge, going beyond what the documents say.",
        "{-dbq}All of this is from the student guide of the ASIBA and the 2024 paper, as presented on the site.",
    ], vis={
        "fmt": dict(type="liste", titre="The written exam · 4 hours", items=[
            "Sujet A: history essay + geography DBQ", "Sujet B: geography essay + history DBQ", "≈ 2 hours per question · half the mark each"],
            x=170, y=140, w=940),
        "ess": dict(type="liste", titre="The essay", cles=["because", "judgement"], items=[
            "a) Explain: several reasons… “because”", "b) Assess / How far: for, against, hierarchy, judgement",
            "Two separate questions: a) and b)"], x=170, y=140, w=940),
        "dbq": dict(type="liste", titre="The DBQ", items=[
            "a) How useful: strengths, limits, provenance, together", "b) A short essay: documents + your own knowledge"],
            x=170, y=160, w=940),
    }),

    # ================================================================ II. Explain
    dict(id="explain", chap="Essay a) · Explain", fond="nuit", humeur="tension",
         retenir="Explain why France was defeated so quickly in 1940: an outdated defensive strategy · the surprise of the Ardennes · the Blitzkrieg. One reason = one paragraph: point, evidence, explanation, link.",
         beats=[
        "{ex1}Here is a typical part a), written for this video. {!Explain}Explain why France was defeated so quickly in 1940.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{rais}Three reasons, from episode two. {rais.1}One: an outdated defensive strategy. France had the Maginot Line, "
        "and waited behind it during the phoney war. {rais.2}Two: the surprise of the Ardennes. The main German attack came through the forest, "
        "where nobody expected it, between the thirteenth and the twentieth of May 1940. "
        "{rais.3}Three: the Blitzkrieg. Tanks and aircraft working together, like Rommel's seventh Panzer division racing to the Somme.",
        "{-rais}{peel}And each reason becomes one paragraph, built in four steps. {peel.1}A point: the reason, in one sentence. "
        "{peel.2}Evidence: a date, a figure, a name. {peel.3}An explanation: why it caused the defeat. "
        "{peel.4}And a link back to the question.",
        "{-peel}{mod1}Listen to a model paragraph, for the first reason.",
        "France was first defeated because its military strategy was out of date. Its leaders, remembering 1914 to 1918, "
        "built the Maginot Line along the German border and waited behind it: from September 1939 to May 1940, during the phoney war, "
        "there was almost no fighting in the west. But the line did not cover the Belgian border, and a defensive army could not react "
        "to a war of movement. This old-fashioned strategy left France unable to stop a rapid offensive, which explains the speed of its collapse in six weeks.",
        "{-mod1}Point, evidence, explanation, link. Do the same for the Ardennes and for the Blitzkrieg, and part a) is done.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explain why France was defeated so quickly in 1940.",
                    src="Question written for this video", enonce=["Part a) of an essay · about 25 minutes"]),
        "pa1": dict(type="pause", t="Find three reasons, each with a precise example.",
                    sous="Pause the video, write your three reasons, then play on."),
        "rais": dict(type="liste", titre="Three reasons", items=[
            "An outdated defensive strategy → Maginot Line, phoney war", "The surprise of the Ardennes → 13–20 May 1940",
            "The Blitzkrieg → tanks + aircraft, Rommel's 7th Panzer"], x=170, y=140, w=940),
        "peel": dict(type="liste", titre="One reason = one paragraph", cles=["point", "evidence", "explanation", "link"], items=[
            "Point: the reason in one sentence", "Evidence: a date, a figure, a name", "Explanation: why it caused the defeat",
            "Link: back to the question"], x=170, y=140, w=940),
        "mod1": dict(type="note", terme="Model paragraph · reason 1", cles=["because", "Maginot", "explains"],
                     t="France was first defeated because its strategy was out of date: the Maginot Line, the phoney war (Sept. 1939 – May 1940), "
                       "no cover of the Belgian border… This explains a collapse in six weeks.",
                     etape="Point · evidence · explanation · link", x=150, y=170, w=980),
    }),

    # ================================================================ III. Assess
    dict(id="assess", chap="Essay b) · Assess", fond="nuit", humeur="tension",
         retenir="How far was the New European Order above all a racial order? For: genocide, Lebensraum, Untermensch. Against: economic exploitation, anti-communism, total war. Judgement: race was the organising principle.",
         beats=[
        "{ex2}Now a part b), also written for this video. {!How far}How far do you agree that the New European Order was above all a racial order?",
        "{-ex2}{gd}An assess question needs two sides. {gd.1}For: the racial entity. Six million Jews murdered; the Slavs as Untermenschen; "
        "Hitler's own words of the eleventh of December 1941, the absolute elimination of the Jews. "
        "{gd.2}Against: the order was also economic and military. France pays twenty million Reichsmarks a day; the East must feed Germany "
        "with Ukrainian wheat and Caucasus oil; and the war in the East is also a crusade against communism.",
        "{-gd}{jug}Then comes the most important part: the judgement. Do not sit on the fence. {jug.1}Weigh the factors: "
        "which one explains the others? {jug.2}A possible answer: race was the organising principle. It decides who is exploited, "
        "like France, treated as a partner on the surface, and who is to be enslaved or exterminated, in the East. "
        "{jug.3}So the economic aims are real, but they serve a racial hierarchy.",
        "{-jug}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod2}A model conclusion. To a large extent, the New European Order was a racial order. Its economic and military aims were real, "
        "from the occupation fees paid by France to the wheat of Ukraine, but they were organised by a racial hierarchy: "
        "partners in the West, slaves in the East, and for the Jews, murder. "
        "That is why the genocide was not a side effect of the war, but one of its declared aims.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="How far do you agree that the New European Order was above all a racial order?",
                    src="Question written for this video", enonce=["Part b) of an essay · about 45 minutes"]),
        "gd": dict(type="cols", g="For", gq="genocide: 6 million · Slavs as “Untermenschen” · Hitler, 11 Dec. 1941",
                   d="Against", dq="France's 20 million RM a day · Ukrainian wheat, Caucasus oil · anti-communism", vs="vs"),
        "jug": dict(type="liste", titre="The judgement", items=[
            "Weigh: which factor explains the others?", "Race as the organising principle: partners in the West, slaves in the East",
            "The economic aims serve a racial hierarchy"], x=170, y=140, w=940),
        "pa2": dict(type="pause", t="Write your conclusion: to what extent? Choose, and justify in three sentences.",
                    sous="Pause the video, write it, then play on for a model."),
        "mod2": dict(type="note", terme="Model conclusion", cles=["large", "hierarchy", "declared"],
                     t="To a large extent: the economic and military aims were real, but organised by a racial hierarchy — partners in the West, "
                       "slaves in the East, murder for the Jews.",
                     etape="Judgement · weighing · the strongest evidence", x=150, y=170, w=980),
    }),

    # ================================================================ IV. DBQ a)
    dict(id="dbq_a", chap="DBQ a) · How useful", fond="guerre", humeur="tension",
         retenir="Judgement first (largely / significantly / partly / slightly useful) · the documents in one sentence · strengths (several arguments) · limits (several arguments) · the documents together.",
         beats=[
        "{doc}Now the DBQ, on two documents of the course. {doc.1}Document A: the Severity Order of Field Marshal von Reichenau, "
        "the tenth of October 1941. It calls on German soldiers to destroy the Jewish-Bolshevik system and to punish what it calls "
        "the subhuman species of Jewry. {doc.2}Document B: Stalin's speech in Moscow, on the seventh of November 1941.",
        "{-doc}",
        ("C", "Well, if the Germans want a war of annihilation, they will get it.", "c_stal"),
        "{-c_stal}{ex3}The question: {!How useful}how useful are Documents A and B for understanding the war of annihilation on the Eastern Front?",
        "{-ex3}{str}Here is the structure to follow, every time. {str.1}First line: your judgement. Largely, significantly, partly or slightly useful. "
        "{str.2}Then each document in one sentence: who, when, what, for whom. {str.3}Then a paragraph of strengths, with several arguments. "
        "{str.4}Then a paragraph of limits, also with several arguments.",
        "{-str}{pa3}",
        ("P", 2.0),
        "{-pa3}{rep}A model. {rep.1}Documents A and B are largely useful for understanding the war of annihilation on the Eastern Front. "
        "{rep.2}Document A is an order given by a German field marshal to his troops in October 1941; Document B is a speech given by Stalin "
        "in Moscow a month later, while the Germans were still advancing on the capital.",
        "{rep.3}Their strengths. They show both sides of the same logic: the German order dehumanises the enemy, with words like subhuman, "
        "and Stalin answers annihilation with annihilation, no mercy to the occupiers. They are official texts, written by leaders, "
        "so they show intentions, not rumours. And their dates matter: autumn 1941, at the height of the German advance.",
        "{rep.4}Their limits. They are propaganda: words, not facts; they do not show what happened on the ground, the shootings, "
        "the starving prisoners. Each one shows only one side's intentions. And they say nothing about the civilians, the main victims of this war. "
        "Taken together, though, they explain why no rules remained on the Eastern Front.",
    ], vis={
        "doc": dict(type="liste", titre="Two documents of the course", items=[
            "A · Reichenau's Severity Order, 10 Oct. 1941: “the subhuman species of Jewry”", "B · Stalin's speech, Moscow, 7 Nov. 1941"],
            x=170, y=150, w=940),
        "c_stal": dict(type="cit", a="Joseph Stalin", o="speech, Moscow, 7 November 1941", x=200, y=190, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="How useful are Documents A and B for understanding the war of annihilation on the Eastern Front?",
                    src="Question written for this video, on two documents of the course", enonce=["Part a) of a DBQ"]),
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "Each document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa3": dict(type="pause", t="Write the first two lines: your judgement, then the documents in one sentence each.",
                    sous="Pause the video, write them, then play on for a model."),
        "rep": dict(type="liste", titre="A model answer", items=[
            "Largely useful for understanding the war of annihilation", "A: a field marshal's order, Oct. 1941 · B: Stalin, Moscow, Nov. 1941",
            "Strengths: both sides of one logic · official texts · dates", "Limits: propaganda · one side each · no civilians"],
            x=150, y=130, w=980),
    }),

    # ================================================================ V. DBQ b)
    dict(id="dbq_b", chap="DBQ b) · Beyond the documents", fond="nuit", humeur="tension",
         retenir="Assess the extent to which the war in the East was a war of annihilation: documents + own knowledge (Jodl's order, 2.8 million Soviet POWs, scorched earth, Einsatzgruppen, Stalingrad).",
         beats=[
        "{ex4}Part b) goes further. Assess the extent to which the war in the East was a war of annihilation.",
        "{-ex4}{g1}Use the documents, then your own knowledge from episodes four and five. {g1.1}Jodl's order of May 1941: "
        "political commissars shot on capture. About two point eight million Soviet prisoners of war killed between June 1941 and February 1942, "
        "mainly by starvation; only three in a hundred survived the war. {g1.2}Scorched earth on the Soviet side. "
        "{g1.3}The Einsatzgruppen shooting the Jews behind the front. {g1.4}And Stalingrad, where the fighting went street by street.",
        "{-g1}{nua}And to assess, add a nuance. The war in the East was still a war between armies, with a front, offensives and a turning point. "
        "But on this front, the war of armies and the war against civilians were the same war. "
        "That is why three fifths of all the dead of the Second World War died there.",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="Assess the extent to which the war in the East was a war of annihilation.",
                    src="Question written for this video", enonce=["Part b) of a DBQ · documents + your own knowledge"]),
        "g1": dict(type="globe", code="H3", sc=[28, 26, 27, 38]),
        "nua": dict(type="note", terme="The nuance", cles=["armies", "civilians", "fifths"],
                    t="Still a war between armies, with a front and a turning point; but the war of armies and the war against civilians were the same war.",
                    etape="3/5 of all the dead of WWII died on the Eastern Front", x=150, y=200, w=980),
    }),

    # ================================================================ VI. l'oral
    dict(id="oral", chap="The oral: Key Issue and Key Terms", fond="aube", humeur="calme",
         retenir="Oral, 35 min: 20 min preparation, 5 min on a Key Issue, 5 min of questions, 5 min on a Key Term. H3: Key Issue “Assess the aims of the New European Order”; Key Terms New European Order, Lebensraum.",
         beats=[
        "{or}Do not forget the oral: it counts as much as the written exam, coefficient ten. {or.1}Twenty minutes of preparation. "
        "{or.2}Then five minutes of presentation on a Key Issue, {or.3}five minutes of questions, {or.4}and five minutes of discussion on a Key Term. "
        "The Key Issue and the Key Term are drawn by crossing history and geography.",
        "{-or}{ki}For this chapter, the Key Issue is: assess the aims of the New European Order. Five minutes is short: "
        "{ki.1}one sentence of definition, {ki.2}the five driving forces grouped in three aims, racial, economic, total war, each with one example, "
        "{ki.3}and a judgement to finish, with a limit: Stalingrad, February 1943.",
        "{-ki}{kt}And the two Key Terms. {kt.1}The New European Order: Nazi rule over Europe, presented by its supporters as saving European civilisation. "
        "{kt.2}Lebensraum: living space, the conquest of land in the East for German settlers, announced in Mein Kampf and pursued with Barbarossa. "
        "For each term: a definition, a date, an example, and a link to another chapter.",
    ], vis={
        "or": dict(type="liste", titre="The oral · 35 minutes", items=[
            "20 min of preparation", "5 min: presentation of a Key Issue", "5 min: questions", "5 min: discussion of a Key Term"],
            x=170, y=130, w=940),
        "ki": dict(type="liste", titre="Key Issue · Assess the aims of the New European Order", items=[
            "One sentence of definition", "Three aims (racial · economic · total war), one example each",
            "A judgement, with a limit: Stalingrad, Feb. 1943"], x=150, y=140, w=980),
        "kt": dict(type="cols", g="New European Order", gq="Nazi rule over Europe, presented as saving its civilisation",
                   d="Lebensraum", dq="living space in the East, from Mein Kampf to Barbarossa", vs="+"),
    }),

    # ================================================================ VI. les pièges
    dict(id="pieges", chap="The traps of this chapter", fond="guerre", humeur="mystere",
         retenir="French police (not the Milice) in summer 1942 · ≈ 43,000 civilians killed in the whole UK · Stalingrad: the 1942 offensive · purges 1937–38 · Romania with the Axis until Aug. 1944.",
         beats=[
        "{pi}Finally, five traps. Each one comes from a slide or a figure of the chapter, and each one can cost you points. "
        "{pi.1}One: the arrests of Jews in France in the summer of 1942, the Vel' d'Hiv round-up, were carried out by the French police. "
        "Not by the Milice, which was only created in January 1943.",
        "{pi.2}Two: the course gives forty-three thousand civilians killed in London in the Blitz. That figure is usually the one for the whole United Kingdom, "
        "about half of them in London. Write: about forty-three thousand civilians killed in the United Kingdom.",
        "{pi.3}Three: in 1941, the southern thrust of Barbarossa aimed at Ukraine, Kiev and Rostov. Stalingrad and the Caucasus were the targets "
        "of the second offensive, in the summer of 1942.",
        "{pi.4}Four: the purges that beheaded the Red Army took place mainly in 1937 and 1938; Tukhachevsky was shot in June 1937.",
        "{pi.5}And five: the table of divisions counts Romania among the Allies, but it fought with the Axis until August 1944. "
        "A perfect limit for a DBQ.",
        "{-pi}{fin}Next, the last episode: the recap of the whole chapter, in one go.",
        ("P", 2.0),
    ], vis={
        "pi": dict(type="liste", titre="Five traps", items=[
            "Summer 1942: the French police, not the Milice (created Jan. 1943)", "Blitz: ≈ 43,000 civilians killed in the whole UK",
            "Stalingrad: the target of 1942, not of 1941", "The purges: mainly 1937–38", "Romania: with the Axis until Aug. 1944"],
            x=150, y=120, w=980),
        "fin": dict(type="mot", t="Next: the recap", g="Episode 7 · the whole chapter", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="In Sujet A of the written exam, what do you write?", r=["A history essay and a geography DBQ", "Two history essays",
         "A history DBQ and a geography DBQ", "One essay chosen freely"], ok=0, voir="fmt",
         ex="Sujet B is the reverse; you cannot mix them. About two hours per question."),
    dict(q="What word should you find yourself writing in an Explain answer?", r=["because", "however", "firstly", "in conclusion"], ok=0,
         voir="ess", ex="Explain calls for several well-argued reasons."),
    dict(q="What must the first line of a DBQ part a) contain?", r=["A judgement: largely / partly useful…", "The date of Document A",
         "A quotation", "A definition"], ok=0, voir="str",
         ex="Then each document in one sentence, a paragraph of strengths and a paragraph of limits."),
    dict(q="Which is a valid LIMIT of Reichenau's Severity Order for this question?", r=["It shows intentions, not what happened on the ground",
         "It was written in 1941", "It is an official document", "It mentions the Jews"], ok=0, voir="rep",
         ex="Propaganda shows words, not facts; and it gives one side only."),
    dict(q="Who carried out the round-ups of Jews in France in July 1942?", r=["The French police", "The Milice", "The Gestapo alone",
         "The Einsatzgruppen"], ok=0, voir="pi", ex="The Milice was only created in January 1943."),
    dict(q="In an Assess answer, what matters most?", r=["A substantiated judgement after weighing the factors", "A full chronology",
         "As many quotations as possible", "Avoiding any clear position"], ok=0, voir="jug",
         ex="Do not sit on the fence: weigh the factors and decide."),
]

CREDITS = [
    "Content: the format of the BFI written exam as presented on the site (ASIBA student guide, 2024 paper); documents of M. Ros's course (Reichenau's Severity Order, Stalin's speech of 7 November 1941); the points to check of chapter H3.",
    "Questions and model answers written for this video.",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
