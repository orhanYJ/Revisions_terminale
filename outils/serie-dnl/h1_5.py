"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 5 : « The crisis at the exam: essay and DBQ ».

Même chaîne que la série H3 (voir h3_1.py et h3_6.py) : outils/serie-philo/generer.py h1_5 ; sortie dans dnl/serie/.
Carte animée H1 (dnl/cartes/H1.html), numéros de scènes dans l'ordre chronologique :
  5 krach · 9 rappel des prêts · 13 Allemagne · 15 Smoot-Hawley · 16 blocs impériaux · 18 Mandchourie · 19 étalon-or ·
  26 Neutrality Acts et Panay · 27 Éthiopie · 28 Migrant Mother · 29 Rhénanie · 30 Anschluss et Munich · 31 Prague puis Pologne
Contenu : le format des épreuves (écrit coeff. 10, 4 h, sujet A ou B ; oral : Key Issue et Key Term tirés en croisant
histoire et géographie), les sujets du chapitre dans le site (champ `exam` de H1 : causes du krach, Smoot-Hawley, les deux
Key Issues ; `H1_ESSAY_CARDS`), la structure de la question a) du DBQ imposée par Cengiz (jugement dès la première ligne,
document en une phrase, paragraphe d'atouts, paragraphe de limites), les documents du cours (Worksheet 3 : source 2,
graphique du chômage allemand, et source 5, mémoires de Melita Maschmann, 1963 ; Migrant Mother de Lange, 1936 ;
« The Doormat » de David Low, 1933, décrit et non montré), les deux Key Terms. La question « Explain » et les copies
modèles sont écrites pour la vidéo et dites comme telles.
Lange : la Resettlement Administration (devenue Farm Security Administration en 1937), comme dans le cours.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-5"
NOTION = "The Wall Street Crash"
NUM = 5
TITRE = "The crisis at the exam: essay and DBQ"
SUIVANT = "Episode 6 · Recap"
PRONONCIATION = {"Maschmann": "Mash-man", "Creditanstalt": "Credit-an-shtalt", "Nipomo": "Nee-poh-mo",
                 "Rhineland": "Rine-land", "Anschluss": "Ahn-shloos", "Daladier": "Da-la-dee-ay", "Blum": "Bloom",
                 "Kellogg": "Kel-log", "Briand": "Bree-an", "Smoot": "Smoot", "Hawley": "Haw-lee", "NSDAP": "N S D A P",
                 "Weimar": "Vye-mar", "autarky": "aw-tar-key", "Panay": "Pa-nye"}

# Worksheet 3, source 2 : chômage des travailleurs assurés en Allemagne (H1Germany)
CHOMAGE = [[1928, 8.6], [1929, 13.3], [1930, 22.7], [1931, 34.3], [1932, 43.8], [1933, 36.2]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{g0}{q1}You know the story now: the Crash, the Depression, economic nationalism, and the democracies that would not act. "
        "{-q1}{q2}But on the day of the exam, nobody will ask you to tell that story. You will have to explain, to assess, and to judge documents.",
        "{-q2}{-g0}{plan}So this episode is a workshop. {plan.1}First, the format of the two exams. {plan.2}Then the essay: "
        "an Explain question and two Assess questions from the course, with model answers. {plan.3}Then the two Key Issues of the chapter. "
        "{plan.4}Then the DBQ, on documents of the course. {plan.5}And finally, the two Key Terms, for the oral.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="question", t="You know the story.", bande=True),
        "q2": dict(type="question", t="Can you use it at the exam?", bande=True),
        "plan": dict(type="liste", titre="This episode, a workshop", items=[
            "The format of the exams", "The essay: Explain, then Assess", "The two Key Issues",
            "The DBQ: How useful, then part b)", "The two Key Terms, for the oral"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 5", t="The crisis at the exam",
                      sous="essay · DBQ · Key Issues · Key Terms"),
    }),

    # ================================================================ I. le format
    dict(id="format", chap="The two exams", fond="nuit", humeur="calme",
         retenir="Written exam, coefficient 10, 4 hours: Sujet A (history essay + geography DBQ) or Sujet B (the reverse). Oral, coefficient 10, 35 minutes: a Key Issue and a Key Term, drawn by crossing history and geography.",
         beats=[
        "{ecr}Two exams, and they weigh the same. {ecr.1}The written exam: coefficient ten, four hours. "
        "{ecr.2}You choose between two papers. Sujet A: a history essay and a geography document-based question. "
        "{ecr.3}Sujet B: the reverse, a geography essay and a history DBQ. {ecr.4}So give about two hours to each question.",
        "{-ecr}{ora}The oral: coefficient ten as well, thirty-five minutes. {ora.1}Twenty minutes of preparation. "
        "{ora.2}Five minutes of presentation on a Key Issue. {ora.3}Five minutes of questions. "
        "{ora.4}And five minutes of discussion on a Key Term. The Key Issue and the Key Term are drawn by crossing history and geography.",
        "{-ora}{ch1}For this chapter, that means two Key Issues and two Key Terms. They come at the end of this episode, "
        "but keep them in mind from now on: they are also excellent essay questions.",
    ], vis={
        "ecr": dict(type="liste", titre="The written exam · coefficient 10 · 4 hours", items=[
            "Four hours, two questions", "Sujet A: history essay + geography DBQ", "Sujet B: geography essay + history DBQ",
            "≈ 2 hours per question"], x=170, y=130, w=940),
        "ora": dict(type="liste", titre="The oral · coefficient 10 · 35 minutes", items=[
            "20 min of preparation", "5 min: presentation of a Key Issue", "5 min: questions", "5 min: discussion of a Key Term"],
            x=170, y=130, w=940),
        "ch1": dict(type="cols", g="2 Key Issues", gq="the democracies to blame? · economic nationalism, the key factor?",
                    d="2 Key Terms", dq="World-wide Economic Depression (1930s) · Appeasement", vs="+"),
    }),

    # ================================================================ II. la méthode de l'essay
    dict(id="methode", chap="The essay: the method", fond="aube", humeur="calme",
         retenir="Explain = several reasons, “because”. Assess / How far = for, against, a hierarchy, a judgement. Introduction: hook, definition, context, question, plan. One paragraph = point, evidence, explanation, link. The conclusion judges.",
         beats=[
        "{ess}An essay question has two parts, and two official formats. {ess.1}Part a) usually begins with Explain: "
        "you give several well-argued reasons, and you should find yourself writing the word because. "
        "{ess.2}Part b) asks you to assess, or how far do you agree: arguments for and against, a hierarchy of factors, and a judgement.",
        "{-ess}{intro}Every essay opens with an introduction in five steps. {intro.1}A hook: a fact, a date, a figure that catches the reader. "
        "{intro.2}The definition of the key words of the question. {intro.3}The context: where, when, who. "
        "{intro.4}The question, rephrased as a problem. {intro.5}And the plan: you announce your parts.",
        "{-intro}{peel}Then each paragraph follows the same four steps. {peel.1}A point: one idea, in one sentence. "
        "{peel.2}Evidence from the course: a date, a figure, a name. {peel.3}An explanation: why the evidence proves the point. "
        "{peel.4}And a link back to the question.",
        "{-peel}{ccl}And the conclusion does not repeat: it judges. To what extent? Which factor matters most, and why? "
        "{!Do not sit on the fence}Do not sit on the fence.",
    ], vis={
        "ess": dict(type="liste", titre="Two formats", cles=["because", "judgement"], items=[
            "a) Explain: several reasons… “because”", "b) Assess / How far: for, against, hierarchy, judgement"],
            x=170, y=170, w=940),
        "intro": dict(type="liste", titre="The introduction, in five steps", items=[
            "Hook: a fact, a date, a figure", "Definition of the key words", "Context: where, when, who",
            "The question, as a problem", "The plan"], x=170, y=110, w=940),
        "peel": dict(type="liste", titre="One reason = one paragraph", cles=["point", "evidence", "explanation", "link"], items=[
            "Point: one idea, one sentence", "Evidence: a date, a figure, a name", "Explanation: why it proves the point",
            "Link: back to the question"], x=170, y=130, w=940),
        "ccl": dict(type="note", terme="The conclusion", cles=["judges", "matters"],
                    t="It does not repeat: it judges. To what extent? Which factor matters most, and why?",
                    etape="A clear answer to the question", x=150, y=200, w=980),
    }),

    # ================================================================ III. Explain
    dict(id="explain", chap="Essay a) · Explain", fond="nuit", humeur="tension",
         retenir="Explain why the Crash of 1929 became a world-wide depression: the recall of American loans (Dawes circuit, Creditanstalt May 1931) · the Gold Standard (Britain leaves, Sept. 1931) · protectionism (Smoot–Hawley 1930 → world trade −66% by 1934).",
         beats=[
        "{ex1}Here is a typical part a), written for this video. {!Explain}Explain why the Wall Street Crash of 1929 became a world-wide depression.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{g1}Three channels, one example each. {g1.1}One: the recall of American loans. Under the Dawes Plan of 1924, America lent Germany eight hundred million marks. "
        "From then on, Europe's finances rested on American credit. And after October 1929, the money was called back. "
        "Austria's largest bank, the Creditanstalt, failed in May 1931; German banks followed in July.",
        "{g1.2}Two: the Gold Standard, the transmission belt. To defend the dollar, the Federal Reserve raised its interest rates, "
        "and gold flowed out of every other country, which had to raise its own rates, the worst possible medicine. "
        "Britain left the Gold Standard in September 1931.",
        "{g1.3}Three: protectionism. On the seventeenth of June 1930, Hoover signed the Smoot–Hawley Tariff. "
        "Canada had already retaliated, in May, and world trade fell by about two thirds, in value, between 1929 and 1934.",
        "{-g1}{mod1}A model paragraph, for the first channel.",
        "The Crash became a world crisis first because Europe depended on American credit. Since the Dawes Plan of 1924, American loans "
        "allowed Germany to pay its reparations, and the Allies to repay their war debts to the United States. When American banks recalled "
        "their loans after October 1929, the circuit broke: the Creditanstalt failed in May 1931, and German banks followed in July. "
        "So an American crash travelled to Europe through the money that America had lent.",
        "Point, evidence, explanation, link. Do the same for the Gold Standard and for protectionism, and part a) is done.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explain why the Wall Street Crash of 1929 became a world-wide depression.",
                    src="Question written for this video", enonce=["Part a) of an essay · about 40 minutes"]),
        "pa1": dict(type="pause", t="Find three reasons, each with one precise example from the course.",
                    sous="Pause the video, write your three reasons, then play on."),
        "g1": dict(type="globe", code="H1", sc=[9, 19, 15]),
        "mod1": dict(type="note", terme="Model paragraph · channel 1", cles=["because", "Dawes", "Creditanstalt"],
                     t="The Crash became a world crisis first because Europe depended on American credit: the Dawes Plan (1924), loans recalled "
                       "after Oct. 1929, the Creditanstalt fails (May 1931)…",
                     etape="Point · evidence · explanation · link", x=150, y=170, w=980),
    }),

    # ================================================================ IV. Assess : les causes du krach
    dict(id="assess1", chap="Essay b) · Assess the causes", fond="nuit", humeur="tension",
         retenir="Assess the role of each factor in triggering the Crash: speculation is the trigger (market ×3, 90% on margin) · structural weaknesses explain the depth (overproduction, inequality, farm prices falling since 1920) · panic and policy are amplifiers.",
         beats=[
        "{ex2}Now a question straight from the course. {!Assess}Assess the role of each factor in triggering the Crash of 1929. Which was the most important?",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mi}A model introduction, in five steps. {mi.1}The hook: in five years, between 1924 and 1929, the American stock market tripled; "
        "by July 1932 the Dow Jones had lost eighty-nine per cent of its value. {mi.2}The definition: the Crash is the collapse of American share prices "
        "in late October 1929, not the Depression that followed. {mi.3}The context: the Roaring Twenties, three Republican presidents, mass consumption on credit. "
        "{mi.4}The problem: the factors reinforce each other, so which one did the others depend on? "
        "{mi.5}The plan: a hierarchy, not a list.",
        "{-mi}{hi}Here is that hierarchy. {hi.1}First, speculation, the strongest candidate for the trigger. Brokers lent up to ninety per cent of a share's price, "
        "so a ten per cent fall wiped a buyer out. But speculation explains the suddenness of the fall, not its depth. "
        "{hi.2}Second, structural weaknesses explain why the fall became a catastrophe: overproduction, a majority of Americans too poor to buy what the factories made, "
        "and farm prices falling since 1920. {hi.3}Third, panic and Republican policy were amplifiers, not the origin. "
        "And with no deposit insurance, five thousand banks had failed by 1932.",
        "{-hi}{cc2}And the conclusion judges. Speculation triggered the Crash; overproduction and inequality decided that it would not correct itself. "
        "Ranking the factors matters more than listing them: that is exactly what the word assess asks for.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Assess the role of each factor in triggering the Crash of 1929. Which was the most important?",
                    src="Essay question of the course (H1)", enonce=["Part b) of an essay · about 1 hour 20"]),
        "pa2": dict(type="pause", t="Write your introduction: hook, definition, context, question, plan.",
                    sous="Pause the video, write five sentences, then play on for a model."),
        "mi": dict(type="liste", titre="A model introduction", petit=True, items=[
            "Hook: the market ×3 in five years; the Dow −89% by July 1932", "Definition: the Crash = late October 1929, not the Depression",
            "Context: the Roaring Twenties, Republican policy, credit", "Problem: which factor did the others depend on?",
            "Plan: a hierarchy, not a list"], x=150, y=110, w=980),
        "hi": dict(type="liste", titre="The hierarchy", marques=["1", "2", "3"], items=[
            "The trigger: speculation (up to 90% on margin)", "The depth: overproduction, inequality, farm prices since 1920",
            "The amplifiers: panic, policy, no deposit insurance (5,000 banks)"], x=150, y=150, w=980),
        "cc2": dict(type="note", terme="Model conclusion", cles=["triggered", "Ranking"],
                    t="Speculation triggered the Crash; overproduction and inequality decided that it would not correct itself.",
                    etape="Ranking the factors matters more than listing them", x=150, y=190, w=980),
    }),

    # ================================================================ V. Assess : Smoot-Hawley
    dict(id="assess2", chap="Essay b) · Assess a policy", fond="nuit", humeur="tension",
         retenir="Assess the 1930 Tariff Act: it failed on its own aims · it triggered a trade war (Canada, Import Duties Act 1932, French quotas 1931; world trade −66%) · but it did not cause the Depression. Its real importance: it destroyed the free-trade pillar of 1919.",
         beats=[
        "{ex3}A second Assess question from the course, on a single policy. Assess how effective the 1930 Tariff Act was "
        "in responding to the challenges posed by the Great Depression.",
        "{-ex3}{eff}The trap is the word effective. Measure the act against its own aims: protecting American farmers and industry. "
        "Not against what we know today.",
        "{-eff}{g2}Then three moves. {g2.1}It failed even on its own terms. Duties on more than twenty thousand goods, yet farm prices kept falling "
        "and unemployment kept rising; Smoot and Hawley both lost their seats in 1932. And the failure was predicted: one thousand and twenty-eight economists "
        "had asked for a veto. {g2.2}Second, it triggered a trade war. Canada retaliated even before it was signed, in May 1930; Britain passed the Import Duties Act in 1932, "
        "France set up quotas in 1931, each sparing its empire. The world split into closed blocs.",
        "{-g2}{nu2}Third, the nuance. It did not cause the Depression: the downturn began with the Crash and the bank failures, and the tariff deepened it. "
        "Roosevelt reversed the policy in 1934, but too late. So the judgement: ineffective on its aims, damaging in its consequences, "
        "and politically decisive, because it destroyed the free-trade pillar of the liberal order of 1919.",
    ], vis={
        "ex3": dict(type="exo", niveau="essay", titre="Assess how effective the 1930 Tariff Act was in responding to the challenges posed by the Great Depression.",
                    src="Essay question of the course (H1)", enonce=["Part b) of an essay"]),
        "eff": dict(type="def", cles=["aims", "farmers"], terme="The key word · effective",
                    t="Measured against its own aims: protecting American farmers and industry.",
                    etape="Not against what we know today", x=170, y=200, w=940),
        "g2": dict(type="globe", code="H1", sc=[15, 16]),
        "nu2": dict(type="cols", g="Ineffective · damaging", gq="farm prices still falling · 1,028 economists · trade war · world trade −66%",
                    d="But not the cause", dq="the Crash and the banks came first · reversed in 1934, too late", vs="vs"),
    }),

    # ================================================================ VI. Key Issue 1
    dict(id="ki1", chap="Key Issue 1 · The democracies to blame?", fond="guerre", humeur="tension",
         retenir="KI 1: the democracies built an order they would not underwrite (US Senate, League without an army), weakened it economically (Smoot–Hawley, loans, gold), refused to defend it (Manchuria, Neutrality Acts, Ethiopia, Rhineland, Munich); but the aggressors willed the war. Possible, not inevitable.",
         beats=[
        "{ki}Now the first Key Issue of the chapter: an essay question, and a subject for the oral. "
        "Blame for the origins of the Second World War lies in part with the great democratic powers themselves. How far do you agree?",
        "{-ki}{mots}Read the words. {mots.1}In part: the question already invites a measured answer. "
        "{mots.2}The great democratic powers: Britain, France and the United States, the guarantors of the liberal order of 1919.",
        "{-mots}{g3}Then argue in four moves. {g3.1}One: they built an order they would not underwrite. The American Senate refused to ratify Versailles, "
        "so the United States never joined the League its own president had conceived; and the League had no army. "
        "When Japan seized Manchuria in September 1931, the League condemned it. Japan simply left the League, in March 1933. "
        "{g3.2}Two: they weakened it economically after 1929. Smoot-Hawley, the recall of loans, the defence of gold. "
        "{g3.3}Three: they refused to defend it. America passed the Neutrality Acts, from 1935 to 1937, and did nothing even when the USS Panay was bombed. "
        "{g3.4}Britain refused an oil embargo on Italy in 1935. {g3.5}France and Britain let the Rhineland go in March 1936, "
        "{g3.6}and signed Munich in September 1938.",
        "{-g3}{mais}Four: the counter-argument. The initiative lay with the militarist regimes in Berlin, Rome and Tokyo. "
        "The Depression created an audience for the Nazis; it compelled no one to invade a neighbour.",
        "{-mais}{pa3}",
        ("P", 2.0),
        "{-pa3}{cc3}A model judgement. I agree in part. The democracies share the blame by omission, through isolationism, protectionism and appeasement: "
        "they built an order, weakened it, and would not defend it. But the war was willed by the aggressors. "
        "{!possible, not inevitable}The democracies made the war possible, not inevitable. The course's own word is the right one: they were reluctant.",
    ], vis={
        "ki": dict(type="exo", niveau="essay", titre="Blame for the origins of WWII lies in part with the great democratic powers themselves. How far do you agree?",
                   src="Key Issue 1 of the chapter · essay and oral", enonce=["How far do you agree with this statement?"]),
        "mots": dict(type="liste", titre="Read the question", cles=["measured", "1919"], items=[
            "“In part”: a measured answer is invited", "“The great democratic powers”: Britain, France, the United States, guarantors of 1919"],
            x=170, y=170, w=940),
        "g3": dict(type="globe", code="H1", sc=[18, 15, 26, 27, 29, 30]),
        "mais": dict(type="note", terme="The counter-argument", cles=["initiative", "militarist"],
                     t="The initiative lay with the militarist regimes, in Berlin, Rome and Tokyo.",
                     etape="The Depression created an audience; it compelled no one to invade", x=150, y=200, w=980),
        "pa3": dict(type="pause", t="Your judgement: how far do you agree? Three sentences.",
                    sous="Pause the video, write your conclusion, then play on for a model."),
        "cc3": dict(type="note", terme="Model judgement", cles=["part", "omission", "reluctant"],
                    t="I agree in part: the democracies share the blame by omission (isolationism, protectionism, appeasement), but the war was willed by the aggressors.",
                    etape="They made it possible, not inevitable", x=150, y=180, w=980),
    }),

    # ================================================================ VII. Key Issue 2
    dict(id="ki2", chap="Key Issue 2 · Economic nationalism", fond="guerre", humeur="mystere",
         retenir="KI 2: economic nationalism corroded the order of 1919 (tariffs, quotas, blocs; autarky made conquest look rational) · but it is a symptom of the Depression, and Britain and France practised it too · ideology competes for the same place. A serious contributing factor, not the key one.",
         beats=[
        "{ki2}The second Key Issue. How far do you agree that economic nationalism was the key factor in the slide towards war in 1939?",
        "{-ki2}{def2}Start with a definition. Economic nationalism: putting national economic interest above international cooperation, "
        "through tariffs, quotas and currency manipulation. Then test the word key: was it the factor on which the others depended, or one link in a chain?",
        "{-def2}{pl2}Three parts. {pl2.1}For: it corroded the international order. Smoot-Hawley, the French quotas and the Import Duties Act "
        "cut world trade by two thirds. They divided the world into imperial blocs. And for a state without an empire, autarky and conquest began to look rational: "
        "exactly what Nazi economic policy claimed. {pl2.2}Against: it is a symptom as much as a cause. Protectionism answered the Depression, "
        "which answered the Crash. And Britain and France practised it too, yet they went to war only when Poland was invaded. "
        "{pl2.3}And ideology competes for the same place: militarism in Germany, Italy and Japan, and Nazi plunder and dispossession of Jewish citizens, "
        "crimes that no trade barrier explains.",
        "{-pl2}{cc4}The judgement: a serious contributing factor, but not the key one. It explains why the world could not cooperate, "
        "not why three regimes chose war. Economic factors created the opportunity; ideology supplied the intent. And that leads straight into chapter two.",
    ], vis={
        "ki2": dict(type="exo", niveau="essay", titre="How far do you agree that economic nationalism was the key factor in the slide towards war in 1939?",
                    src="Key Issue 2 of the chapter · essay and oral", enonce=["Test the word “key”"]),
        "def2": dict(type="def", cles=["national", "cooperation"], terme="Key word · economic nationalism",
                     t="Putting national economic interest above international cooperation: tariffs, quotas, currency manipulation.",
                     etape="“Key”: the factor on which the others depended?", x=170, y=200, w=940),
        "pl2": dict(type="liste", titre="Three parts", marques=["+", "−", "?"], items=[
            "For: it corroded the order of 1919 · trade −66% · blocs · autarky", "Against: a symptom of the Depression · Britain and France too",
            "Ideology competes: militarism, Nazi plunder"], x=150, y=150, w=980),
        "cc4": dict(type="note", terme="Model judgement", cles=["contributing", "opportunity", "intent"],
                    t="A serious contributing factor, not the key one: it explains why the world could not cooperate, not why three regimes chose war.",
                    etape="Economic factors: the opportunity · ideology: the intent", x=150, y=180, w=980),
    }),

    # ================================================================ VIII. DBQ a) — Worksheet 3
    dict(id="dbq_a", chap="DBQ a) · How useful", fond="aube", humeur="calme",
         retenir="DBQ a): the judgement in the first line (largely / significantly / partly / slightly useful) · each document in one sentence (nature, author, date, audience) · a paragraph of strengths, several arguments · a paragraph of limits, several arguments.",
         beats=[
        "{str}Now the DBQ. For part a), there is one structure, and you follow it every time. "
        "{str.1}First line: your judgement. Largely, significantly, partly or slightly useful. "
        "{str.2}Then each document in one sentence: its nature, its author, its date, and who it was for. "
        "{str.3}Then a paragraph of strengths, with several arguments. "
        "{str.4}Then a paragraph of limits, with several arguments: the provenance, the purpose, and what is missing.",
        "{-str}{gr}Two documents from Worksheet 3. Source 2: {gr.1}a chart of unemployment in Germany. {gr.2}Eight point six per cent in 1928, "
        "{gr.3}forty-three point eight per cent in 1932, {gr.4}then thirty-six point two in 1933. Careful: these are insured workers only.",
        "{doc}Source 5: the memoir of Melita Maschmann, a former member of the Hitler Youth, published in 1963.{-gr}",
        ("C", "The Nazis promised to end unemployment and poverty, and I believed them.", "c_mas"),
        "{-c_mas}{-doc}{ex4}The question: {!How useful}how useful are Sources 2 and 5 for understanding how the Depression helped the Nazis?",
        "{-ex4}{pa4}",
        ("P", 2.0),
        "{-pa4}{rep}A model answer. {rep.1}Sources 2 and 5 are largely useful for understanding how the Depression helped the Nazis. "
        "{rep.2}Source 2 is a chart of unemployment among insured workers in Germany, from 1928 to 1933. "
        "Source 5 is the memoir of Melita Maschmann, a former member of the Hitler Youth, published in 1963.",
        "{rep.3}Their strengths. First, Source 2 measures the scale of the crisis: unemployment multiplied by five in four years, "
        "and it peaks in 1932, the year before Hitler became chancellor. Second, Source 5 shows the mechanism from the inside: "
        "a young German explains why the Nazi promise worked on her. Third, together they link a figure to a feeling, the crisis to the vote.",
        "{rep.4}Their limits. First, the chart counts insured workers only, not the whole workforce. It gives a rate, not the number of people out of work. "
        "Second, the memoir was written thirty years later, with hindsight, by someone who may want to explain, or excuse, her choice. "
        "Third, what is missing: neither source shows that the Nazis never won a majority, nor that conservatives let Hitler in, in January 1933.",
    ], vis={
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "Each document in one sentence: nature, author, date, audience",
            "A paragraph of strengths, several arguments", "A paragraph of limits: provenance, purpose, what is missing"], x=150, y=120, w=980),
        "gr": dict(type="graphe", titre="Source 2 · unemployment in Germany, insured workers (%)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.5, 1933.5], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="year", ly="%"),
                   el=[dict(type="courbe", pts=CHOMAGE, c="ca", dur=2.2),
                       dict(type="points", pts=[[1928, 8.6]], c="sa", lbl="1928: 8.6%", lp=[1928.2, 15]),
                       dict(type="points", pts=[[1932, 43.8]], c="ca", lbl="1932: 43.8%", lp=[1930.4, 47]),
                       dict(type="points", pts=[[1933, 36.2]], c="sa", lbl="1933: 36.2%", lp=[1932.2, 30])]),
        "doc": dict(type="tag", t="Source 5 · Melita Maschmann, memoir, 1963", x=200, y=650),
        "c_mas": dict(type="cit", a="Melita Maschmann", o="memoir, 1963 (Worksheet 3, Source 5)", x=200, y=210, w=880),
        "ex4": dict(type="exo", niveau="dbq", titre="How useful are Sources 2 and 5 for understanding how the Depression helped the Nazis?",
                    src="Worksheet 3 · Source 2 (chart) and Source 5 (memoir)",
                    donnees=["Source 2: German unemployment, insured workers, 1928–1933", "Source 5: Melita Maschmann, memoir, 1963"],
                    questions=["Judgement in the first line", "Each document in one sentence", "Strengths: several arguments",
                               "Limits: several arguments"]),
        "pa4": dict(type="pause", t="DBQ a): how useful are Sources 2 and 5 for understanding how the Depression helped the Nazis?",
                    sous="Judgement, presentation, strengths, limits. Pause the video, write, then play on for a model."),
        "rep": dict(type="liste", titre="A model answer", petit=True, items=[
            "Judgement: largely useful", "Source 2: chart, insured workers, 1928–33 · Source 5: Maschmann's memoir, 1963",
            "Strengths: the scale (×5, peak in 1932) · the mechanism from inside · figure + feeling",
            "Limits: insured workers only · hindsight · no majority, no Jan. 1933"], x=150, y=120, w=980),
    }),

    # ================================================================ IX. DBQ b)
    dict(id="dbq_b", chap="DBQ b) · Beyond the documents", fond="nuit", humeur="tension",
         retenir="DBQ b): the documents + your own knowledge. The crisis created the audience (43.8% in 1932, “Work! Freedom! Bread!”); a political calculation opened the door (never a majority, conservatives appoint Hitler, Jan. 1933).",
         beats=[
        "{ex5}Part b) goes further. Using the documents and your own knowledge, assess how far the Depression explains Hitler's rise to power.",
        "{-ex5}{g4}Start from the documents, then add the course. {g4.1}German industry depended on American credit: when the loans were recalled, "
        "manufacturing production fell by forty per cent. Hunger marches and soup kitchens became ordinary sights. "
        "The Nazis spoke directly to the unemployed: Work! Freedom! Bread! That is the first half: {!the crisis created the audience}the crisis created the audience.",
        "{-g4}{b2}And the second half, which no document here shows. {b2.1}The Nazis never won more than fifty per cent of the vote. "
        "{b2.2}What brought them to power was the fear of communism, in the middle class and the centre parties. "
        "{b2.3}In January 1933, conservatives appointed Hitler chancellor, thinking they could use him. "
        "So the judgement: the Depression explains the audience; {!a political calculation opened the door}a political calculation opened the door.",
    ], vis={
        "ex5": dict(type="exo", niveau="dbq", titre="Using the documents and your own knowledge, assess how far the Depression explains Hitler's rise to power.",
                    src="Part b) of the DBQ", enonce=["A short essay: the documents, then your own knowledge"]),
        "g4": dict(type="globe", code="H1", sc=[13]),
        "b2": dict(type="liste", titre="What the documents do not show", items=[
            "Never more than 50% of the vote", "The fear of communism: middle class and centre parties",
            "January 1933: conservatives appoint Hitler"], x=150, y=150, w=980),
    }),

    # ================================================================ X. trois réflexes de source
    dict(id="sources", chap="Three kinds of sources", fond="aube", humeur="calme",
         retenir="Source reflexes: a cartoon (Low, 1933) = the opinion of a contemporary, perceptions not facts · a commissioned photo (Lange, 1936) = real poverty, framed to justify reform · a memoir (Maschmann, 1963) = first-hand, but with hindsight.",
         beats=[
        "{ph}The documents of this chapter are of three kinds, and each has its own reflex. {ph.1}First, a commissioned photograph. "
        "Migrant Mother, by Dorothea Lange, March 1936: Florence Owens Thompson, aged thirty-two, mother of seven, in a pea-pickers' camp at Nipomo, in California.",
        "{ph.2}Its strength: the poverty is real. The pea crop had frozen, there was no work, and the family lived on frozen vegetables and on birds the children caught. "
        "{ph.3}Its limit: it is composed, not accidental. Lange made five exposures, working closer and closer, for a federal agency, the Resettlement Administration, "
        "that wanted public support for relief.",
        "{-ph}{low}Second, a cartoon. {low.1}David Low's The Doormat, 1933. A Japanese soldier walks over the League of Nations, "
        "{low.2}while its officials bow, and the British Foreign Secretary, John Simon, powders the League's nose with a face-saving kit. "
        "{low.3}The reflex: a cartoon gives the opinion of a contemporary. Perceptions, not facts. But Low saw in 1933 what historians say today.",
        "{-low}{ref}And third, a memoir, like Maschmann's: first-hand, but written with hindsight. {ref.1}So, three reflexes. "
        "{ref.2}A cartoon: an opinion. {ref.3}A commissioned photograph: real, but framed. {ref.4}A memoir: first-hand, but late.",
    ], vis={
        "ph": dict(type="tableau", img="h1-lange-migrant", de=[1.0, .5, .35], a=[1.25, .5, .3],
                   legende="Migrant Mother, Nipomo, California, March 1936, by Dorothea Lange (Library of Congress, Wikimedia Commons, public domain)"),
        "low": dict(type="liste", titre="David Low, “The Doormat”, 1933 (described)", items=[
            "A Japanese soldier walks over the League", "Its officials bow; John Simon powders its nose: a “face-saving kit”",
            "Reflex: the opinion of a contemporary, perceptions not facts"], x=150, y=150, w=980),
        "ref": dict(type="liste", titre="Three source reflexes", marques=["→", "✎", "◉", "❝"], items=[
            "Always: nature, author, date, purpose", "Cartoon (Low, 1933): an opinion, perceptions",
            "Commissioned photo (Lange, 1936): real poverty, framed", "Memoir (Maschmann, 1963): first-hand, with hindsight"],
            x=150, y=130, w=980),
    }),

    # ================================================================ XI. les Key Terms
    dict(id="kt", chap="The Key Terms, for the oral", fond="nuit", humeur="calme",
         retenir="World-wide Economic Depression (1930s): a prolonged, global fall in output, with mass unemployment and severe deflation (US 25% in 1933; Germany 43.8% in 1932; world trade −66%). Appeasement: conceding to an aggressor's demands in the hope of avoiding war (Rhineland 1936, Munich 1938).",
         beats=[
        "{kt1}At the oral, five minutes on a Key Term. The recipe: a definition in one sentence, then examples, dates, and a link to another chapter. "
        "First Key Term: the World-wide Economic Depression of the 1930s. "
        "{!a prolonged, global fall in output}A prolonged, global fall in output, with mass unemployment and severe deflation.",
        "{-kt1}{ex6}{ex6.1}The examples. In the United States, fourteen million unemployed, a quarter of all workers, in 1933. "
        "{ex6.2}In Germany, forty-three point eight per cent of insured workers in 1932. {ex6.3}And world trade down by two thirds between 1929 and 1934. "
        "{ex6.4}The link: the Depression gave the Nazis their audience, which is chapter two.",
        "{-ex6}{kt2}Second Key Term: appeasement. {!conceding to an aggressor's demands}Conceding to an aggressor's demands in the hope of avoiding war.",
        "{-kt2}{g5}{g5.1}The examples. March 1936: German troops enter the Rhineland, and France and Britain do not intervene. "
        "{g5.2}September 1938: at Munich, Chamberlain and Daladier accept the cession of the Sudetenland. "
        "{g5.3}March 1939: Germany occupies Prague, and Munich has bought nothing; on the first of September, Poland is invaded.",
        "{-g5}{rai}And the reasons, because the examiner will ask why. Six reasons. Pacifism. An empire to police, and no money to rearm. Sympathy for a Germany "
        "treated unfairly by the Treaty of Versailles, in 1919. Their own economic problems, which came first. American isolationism, which left them alone. And the fear of communism, stronger than the fear of fascism. "
        "{!None of these reasons is stupid}None of these reasons is stupid.",
    ], vis={
        "kt1": dict(type="def", cles=["prolonged", "unemployment", "deflation"], terme="Key Term · World-wide Economic Depression (1930s)",
                    t="A prolonged, global fall in output, with mass unemployment and severe deflation.",
                    etape="Definition · examples · dates · a link", x=150, y=180, w=980),
        "ex6": dict(type="liste", titre="Examples", petit=True, items=[
            "United States 1933: 14 million unemployed, 25% of workers", "Germany 1932: 43.8% of insured workers",
            "World trade −66%, 1929–1934", "Link: the Nazis' audience → chapter 2"], x=150, y=140, w=980),
        "kt2": dict(type="def", cles=["conceding", "avoiding"], terme="Key Term · Appeasement",
                    t="Conceding to an aggressor's demands in the hope of avoiding war.",
                    etape="Britain and France, 1935–1938", x=150, y=200, w=980),
        "g5": dict(type="globe", code="H1", sc=[29, 30, 31]),
        "rai": dict(type="liste", titre="Six reasons for appeasement", petit=True, items=[
            "Pacifism", "An empire to police, no money to rearm", "Sympathy for Germany (Versailles, 1919)",
            "Their own economic problems first", "American isolationism", "Fear of communism more than fascism"],
            x=150, y=100, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}The format: four hours for the written exam, thirty-five minutes for the oral, coefficient ten each. "
        "{carte.2}The essay: Explain means because; Assess means a hierarchy and a judgement. "
        "{carte.3}The DBQ: judgement first, the documents in one sentence, strengths, limits. "
        "{carte.4}The Key Issues: possible, not inevitable; the opportunity and the intent. "
        "{carte.5}And the Key Terms: a definition, examples, a link.",
        ("P", 4.0),
        "{-carte}{fin}Next, the last episode: the recap of the whole chapter, from Wall Street to the war.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="THE CRISIS AT THE EXAM", branches=[
            dict(t="The format", items=["written: 4 h, Sujet A or B", "oral: 35 min, coeff. 10"]),
            dict(t="The essay", items=["Explain: “because”", "Assess: hierarchy, judgement"]),
            dict(t="The DBQ", items=["judgement first", "strengths · limits"]),
            dict(t="Key Issues", items=["possible, not inevitable", "opportunity vs intent"]),
            dict(t="Key Terms", items=["Depression", "Appeasement"])]),
        "fin": dict(type="mot", t="Next: the recap", g="Episode 6 · the whole chapter", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="In Sujet A of the written exam, what do you write?", r=["A history essay and a geography DBQ", "Two history essays",
         "A history DBQ and a geography DBQ", "One essay chosen freely"], ok=0, voir="ecr",
         ex="Sujet B is the reverse. Four hours, about two hours per question."),
    dict(q="At the oral, what is the order of the 15 minutes after the preparation?", r=["Key Issue, questions, Key Term",
         "Key Term, Key Issue, questions", "Questions, Key Issue, Key Term", "Key Issue only"], ok=0, voir="ora",
         ex="Five minutes on a Key Issue, five minutes of questions, five minutes on a Key Term."),
    dict(q="What must the first line of a DBQ part a) contain?", r=["A judgement: largely / partly useful…", "The date of the document",
         "A quotation", "A definition"], ok=0, voir="str",
         ex="Then each document in one sentence, a paragraph of strengths and a paragraph of limits."),
    dict(q="Which is a valid LIMIT of Source 2 (the chart of German unemployment)?", r=["It counts insured workers only",
         "It is a chart", "It ends in 1933", "It shows a peak in 1932"], ok=0, voir="rep",
         ex="It leaves out the rest of the workforce. Its other features (a chart, ending in 1933, peaking in 1932) are not limits in themselves."),
    dict(q="In the essay on the causes of the Crash, which factor is the trigger?", r=["Speculation", "Smoot–Hawley",
         "The Gold Standard", "The Dawes Plan"], ok=0, voir="hi",
         ex="Speculation explains the suddenness; overproduction and inequality explain the depth."),
    dict(q="How should you judge the effectiveness of the 1930 Tariff Act?", r=["Against its own aims: protecting farmers and industry",
         "Against what economists know today", "By the number of goods taxed", "By Canada's reaction alone"], ok=0, voir="eff",
         ex="It failed even on its own terms: farm prices kept falling, unemployment kept rising."),
    dict(q="Which sentence best sums up Key Issue 1 (the democracies to blame)?", r=["They made the war possible, not inevitable",
         "They alone caused the war", "They bear no responsibility", "They wanted the war"], ok=0, voir="cc3",
         ex="Blame by omission (isolationism, protectionism, appeasement); the war was willed by the aggressors."),
    dict(q="What is appeasement?", r=["Conceding to an aggressor's demands in the hope of avoiding war", "Raising tariffs to protect industry",
         "Refusing to recognise conquests by force", "Selling arms for cash"], ok=0, voir="kt2",
         ex="Rhineland 1936, Munich 1938. The other answers are protectionism, the Stimson note and cash and carry."),
]

CREDITS = [
    "Content: the format of the DNL exams (written and oral) as presented on the site; the essay questions, Key Issues, Key Terms and essay cards of M. Ros's course (DNL History, H1); Worksheet 3 (Sources 2 and 5); the course's descriptions of Migrant Mother and of David Low's “The Doormat”.",
    "The Explain question and the model answers were written for this video.",
    "Photograph: Dorothea Lange, Migrant Mother, Nipomo, California, March 1936 (Library of Congress; Wikimedia Commons, public domain).",
    "Animated map of the chapter: the site (dnl/cartes/H1).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
