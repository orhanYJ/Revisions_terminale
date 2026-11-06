"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 8 : « Totalitarianism at the exam: essay and DBQ ».

Même chaîne que la série H3 (voir h3_1.py, h3_6.py) : outils/serie-philo/generer.py h2_8 ; sortie dans dnl/serie/
(type globe : la carte animée du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo).
  Scènes de la carte H2 utilisées : 1 brutalisation · 4 victoire mutilée et Biennio Rosso · 5 Diktat de Versailles ·
  16 la crise fait des nazis le premier parti · 20 Hindenburg nomme Hitler · 21 incendie du Reichstag ·
  27 Abyssinie · 28 Rhénanie · 33 Anschluss · 34 Munich · 35 Prague · 36 pacte germano-soviétique · 37 Pologne.
Contenu : le format de l'écrit BFI tel que le site le présente (comme dans h3_6.py) ; les sujets du chapitre
(CHAPTERS.H2.exam : « How far was the First World War responsible… » avec son plan, son introduction et sa conclusion,
« Compare the ways Mussolini and Hitler came to power », « To what extent did the three regimes control their societies
in the same way? », « Assess the role of totalitarianism… », qui est aussi le key issue) ; les key terms (Appeasement,
Totalitarianism) ; les cartes d'essai H2_ESSAY_CARDS (cinq angles d'utilité, cinq de limites, phrase d'ouverture,
épigraphe d'Arendt) ; deux documents des DBQ du chapitre (h2dbq2 : télégramme de Roosevelt du 14 avril 1939 ;
h2dbq3 : discours de Hitler à l'Obersalzberg, 22 août 1939), étudiés ici ENSEMBLE et sous un autre angle (l'échec de
l'apaisement) que les corrigés a) du site, repris dans les épisodes 6 et 7 ; les points à vérifier (H2_CHECKS).
La question « Explain » (accession de Hitler au pouvoir), la question a) du DBQ et les copies modèles sont écrites
pour la vidéo et dites comme telles.
Révision « pour l'oreille » du 06/11/2026 : phrases courtes, nombres écrits comme ils se disent ; le discours de
l'Obersalzberg (22 août) est dit « dix jours » avant l'invasion de la Pologne (1er septembre), le site dit « neuf jours ». Les « Your turn » : raisons (Explain), paragraphe, introduction, paragraphe
(How far), deux premières lignes du DBQ a), plan du DBQ b).
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-8"
NOTION = "Totalitarian Regimes"
NUM = 8
TITRE = "Totalitarianism at the exam: essay and DBQ"
SUIVANT = "Episode 9 · Recap"
PRONONCIATION = {"Reichstag": "Rikes-tahg", "Hindenburg": "Hin-den-burg", "Lebensraum": "Lay-bens-rowm",
                 "Biennio Rosso": "Bee-en-nyo Ross-o", "Matteotti": "Mat-tay-ot-tee", "Duce": "Doo-chay",
                 "Führer": "Fyoo-rer", "Anschluss": "An-shloos", "Sudetenland": "Soo-day-ten-land",
                 "Obersalzberg": "Oh-ber-zalts-berg", "D'Annunzio": "Dan-noon-tsyo", "Fiume": "Fyoo-may",
                 "Spartacist": "Spar-ta-sist", "Daladier": "Da-la-dyay", "Yezhov": "Yezh-off", "Molotov": "Mol-o-toff",
                 "NSDAP": "N S D A P", "Weimar": "Vy-mar", "Wehrmacht": "Vair-markt", "Victor Emmanuel": "Victor Emmanuel",
                 "Arendt": "Ah-rent", "Mosse": "Moss-ee", "Komsomol": "Kom-so-mol", "Balilla": "Ba-lee-la",
                 "Corfu": "Kor-foo", "kulaks": "koo-lacks", "Gulag": "Goo-lag", "Stakhanov": "Sta-ka-noff",
                 "Sujet": "Soo-zhay", "fascistissime": "fa-shis-tee-see-may"}

# vote NSDAP (graphique de M. Ros) : mai 1928, sept. 1930, juillet 1932, nov. 1932
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}The first of September, nineteen thirty-nine. The German army invades Poland. Two days later, Europe is at war again. "
        "You know how the three totalitarian regimes got there. But can you use it?",
        "{-q1}{q2}On the day of the exam, nobody will ask you to tell the story. You will have to explain. To assess. "
        "To judge documents. In English, against the clock.{-q2}{-g0}",
        "{plan}So this episode is a workshop. {plan.1}First, a reminder of the written exam. {plan.2}Then an Explain question, "
        "with model paragraphs. {plan.3}Then the big one, a How far question. Plan, introduction, paragraph, conclusion. "
        "{plan.4}Then the DBQ: how useful, and then part B. {plan.5}And to finish, the oral, and the traps of this chapter.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[37]),
        "q1": dict(type="question", t="You know the chapter. Can you use it?", bande=True),
        "q2": dict(type="question", t="Explain · assess · judge documents", bande=True),
        "plan": dict(type="liste", titre="This episode, a workshop", items=[
            "The written exam in one minute", "Essay a) · Explain", "Essay b) · How far: the full method",
            "The DBQ: How useful, then part b)", "The oral, and the traps of the chapter"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 8", t="Totalitarianism at the exam",
                      sous="essay · DBQ · oral · the traps of the chapter"),
    }),

    # ================================================================ I. le format
    dict(id="format", chap="The written exam", fond="nuit", humeur="calme",
         retenir="4 hours. Sujet A: history essay + geography DBQ. Sujet B: geography essay + history DBQ. Essay: a) Explain, b) Assess / How far. DBQ: a) How useful, b) a short essay with the documents and your own knowledge.",
         beats=[
        "{fmt}A quick reminder first, as in the series on the Second World War. {fmt.1}The written exam lasts four hours. You choose "
        "between two papers. Sujet A is a history essay, plus a geography document-based question. "
        "{fmt.2}Sujet B is the reverse: a geography essay, and a history DBQ. "
        "{fmt.3}About two hours for each. History and geography each count for half the mark.",
        "{-fmt}{ess}What does the essay look like? It has two parts. {ess.1}Part A is usually an Explain question. You need several "
        "well-argued reasons. If you never write the word because, something is wrong. {ess.2}Part B asks you to assess, or how far you agree. "
        "That means arguments for and against, a hierarchy, and a judgement. {ess.3}The DBQ has two parts as well. Part A: how useful are the documents? "
        "{ess.4}Part B: a short essay, using the documents and your own knowledge.",
        "{-ess}{cle}One rule runs through all of it, from the chapter's revision cards. "
        "{!one example}One idea, one example. A date, a figure, a name. An argument without an example is worth almost nothing.",
        "{-cle}",
    ], vis={
        "fmt": dict(type="liste", titre="The written exam · 4 hours", items=[
            "Sujet A: history essay + geography DBQ", "Sujet B: geography essay + history DBQ",
            "≈ 2 hours per question · half the mark each"], x=170, y=140, w=940),
        "ess": dict(type="liste", titre="Two exercises, two parts each", cles=["because", "judgement"], items=[
            "Essay a) Explain: several reasons… “because”", "Essay b) Assess / How far: for, against, hierarchy, judgement",
            "DBQ a) How useful are the documents?", "DBQ b) A short essay: documents + your own knowledge"],
            x=150, y=130, w=980),
        "cle": dict(type="mot", t="One idea · one example", g="a date, a figure, a name", y=260, taille=88),
    }),

    # ================================================================ II. Explain : les raisons
    dict(id="explain", chap="Essay a) · Explain", fond="nuit", humeur="tension",
         retenir="Explain why Hitler was appointed chancellor in January 1933: the Depression made the NSDAP the largest party (2.6% → 37.4%) · street violence and a party staged as a movement (SA, SS) · conservative elites who thought they could control him (Hindenburg, 30 Jan. 1933).",
         beats=[
        "{ex1}Here is a typical part A, written for this video. {!Explain}Explain why Hitler was able to come to power in January nineteen thirty-three.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{g1}Let's place it on the map first. {g1.1}From nineteen thirty to nineteen thirty-two, the world crisis hits Germany hard. "
        "The Nazi party becomes the largest party in the Reichstag. {g1.2}Then, on the thirtieth of January nineteen thirty-three, "
        "President Hindenburg appoints Hitler chancellor. {g1.3}Four weeks later, the Reichstag burns. "
        "And that fire gives Hitler the emergency he needs to suspend freedoms.",
        "{-g1}{rais}What were the reasons? We met three in episode two. {rais.1}The first is the Depression. "
        "In nineteen thirty-two, Germany had five point six million unemployed. A fringe party became a mass party. "
        "{rais.2}The second is the street. The SA was a mass force. It fought the communists and protected the meetings. "
        "The SS was the elite. The party was staged as a movement, as at the Nuremberg congress of nineteen twenty-nine. "
        "{rais.3}The third reason is the elites. Hitler did not seize power. Hindenburg and the conservatives around him handed it to him. "
        "They were convinced they could control him.",
        "{-rais}{peel}How do you write it? Each reason becomes one paragraph, in four steps. {peel.1}A point: the reason, in one sentence. "
        "{peel.2}Evidence: a date, a figure, a name. {peel.3}An explanation: why did it help Hitler? "
        "{peel.4}And a link back to the question.",
        "{-peel}",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explain why Hitler was able to come to power in January 1933.",
                    src="Question written for this video", enonce=["Part a) of an essay · about 25 minutes"]),
        "pa1": dict(type="pause", t="Find three reasons, each with a precise example.",
                    sous="Pause the video, write your three reasons, then play on."),
        "g1": dict(type="globe", code="H2", sc=[16, 20, 21]),
        "rais": dict(type="liste", titre="Three reasons", items=[
            "The Depression → 5.6 million unemployed (1932), NSDAP 37.4% (July 1932)",
            "The street → the SA as a mass force, the SS as an elite",
            "The elites → Hindenburg appoints Hitler, 30 Jan. 1933"], x=150, y=140, w=980),
        "peel": dict(type="liste", titre="One reason = one paragraph", cles=["point", "evidence", "explanation", "link"], items=[
            "Point: the reason in one sentence", "Evidence: a date, a figure, a name", "Explanation: why it helped Hitler",
            "Link: back to the question"], x=170, y=140, w=940),
    }),

    # ================================================================ III. Explain : les paragraphes modèles
    dict(id="explain_mod", chap="Essay a) · Model paragraphs", fond="nuit", humeur="calme",
         retenir="Model paragraph: point (the Depression) · evidence (5.6 million unemployed; 2.6% → 18.3% → 37.4% → 33.1%) · explanation (despair turned into votes) · link (largest party, never a majority: the crisis opened the door, others opened it wider).",
         beats=[
        "{gr}Before the first paragraph, look at Mister Ros's chart. {gr.1}May nineteen twenty-eight, before the crisis. "
        "The Nazi party wins just two point six per cent of the vote. {gr.2}September nineteen thirty: eighteen point three. "
        "Seven times more. {gr.3}July nineteen thirty-two, at the height of unemployment: thirty-seven point four. "
        "Now it is the largest party in the Reichstag. {gr.4}But look at November nineteen thirty-two. It falls back, to thirty-three point one.",
        "{-gr}{mod1}Now listen to a model paragraph, for the first reason.",
        "Hitler first came to power because the Great Depression turned a fringe party into a mass movement. "
        "In May nineteen twenty-eight, the Nazi Party won only two point six per cent of the vote. "
        "By nineteen thirty-two, about five point six million Germans were out of work. "
        "In July of that year, the party reached thirty-seven point four per cent. "
        "The crisis discredited the Weimar Republic, already associated with defeat. And it gave the Nazis the mass audience they had lacked. "
        "Yet the party never won a majority. It even lost ground in November nineteen thirty-two. "
        "So the crisis explains why Hitler became unavoidable. It does not explain why he was appointed.",
        "{-mod1}{pa2}Did you notice the last sentence? It prepares the next reason. Your turn now.",
        ("P", 2.0),
        "{-pa2}{mod2}Here is a model for the third reason. Hitler came to power above all because the conservative elites chose to give it to him. "
        "On the thirtieth of January nineteen thirty-three, President Hindenburg appointed him chancellor, quite legally. "
        "Hindenburg was an old general of the Empire. The conservatives around him thought they could control Hitler once he was in government. "
        "And the legal façade reassured them. This choice explains the timing. "
        "Without it, a party in decline since November nineteen thirty-two might never have reached power.",
        "Point, evidence, explanation, link. And listen to two little words: above all. Even in an Explain answer, you can rank your reasons.{-mod2}",
    ], vis={
        "gr": dict(type="graphe", titre="The NSDAP vote, 1928–1932 (M. Ros's chart)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1928, 1933.2], y=[0, 45], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40], lx="year", ly="% of the vote"),
                   el=[dict(type="point", x=1928.4, y=2.6, c="sa", lbl="May 1928: 2.6%", lp=[1929.1, 8]),
                       dict(type="courbe", pts=VOTE[:2], c="ca", lbl="Sept. 1930: 18.3%", lp=[1929.4, 24], dur=1.4),
                       dict(type="courbe", pts=VOTE[1:3], c="ca", lbl="July 1932: 37.4%", lp=[1930.6, 41], dur=1.4),
                       dict(type="courbe", pts=VOTE[2:], c="el", lbl="Nov. 1932: 33.1%", lp=[1932.0, 27], dur=0.8)]),
        "mod1": dict(type="note", terme="Model paragraph · reason 1", cles=["because", "mass movement", "majority"],
                     t="Hitler first came to power because the Depression turned a fringe party into a mass movement: 2.6% in May 1928, "
                       "37.4% in July 1932, with 5.6 million unemployed. Yet never a majority, and down to 33.1% in November 1932.",
                     etape="Point · evidence · explanation · link to the next reason", x=150, y=170, w=980),
        "pa2": dict(type="pause", t="Write the paragraph for the third reason: the elites.",
                    sous="Point, evidence, explanation, link. Pause the video, then play on for a model."),
        "mod2": dict(type="note", terme="Model paragraph · reason 3", cles=["above all", "Hindenburg", "control"],
                     t="Above all, the conservative elites handed power to Hitler: Hindenburg appointed him legally on 30 January 1933, "
                       "convinced with those around him that they could control him.",
                     etape="This explains the timing: a party in decline since Nov. 1932", x=150, y=170, w=980),
    }),

    # ================================================================ IV. How far : méthode et plan
    dict(id="howfar", chap="Essay b) · How far: the plan", fond="nuit", humeur="tension",
         retenir="How far was WW1 responsible for the rise of totalitarian regimes? I. The war created the violence and the grievances · II. It opened the way to revolution, and to the fear of it · III. But it does not explain everything (ideologies, elites, the Depression).",
         beats=[
        "{photo1}{ex2}Now the big question: a part B, from the chapter's own exam subjects. "
        "{!How far}How far was the First World War responsible for the rise of totalitarian regimes?",
        "{-ex2}{-photo1}{meth}What does how far mean? It means you weigh one factor. Not yes. Not no. To what extent? "
        "{meth.1}So you need the case for the factor. {meth.2}Then the case against, or the other factors. "
        "{meth.3}And a judgement that runs through the whole essay. You announce it in the introduction, and you prove it in the conclusion. "
        "{meth.4}And the trap? Telling the story of nineteen eighteen to nineteen thirty-three, and never answering.",
        "{-meth}{g2}Remember what the map showed. {g2.1}The trenches: four years of mass killing. {g2.2}Italy: a mutilated victory, "
        "then the red years of nineteen nineteen and nineteen twenty. {g2.3}Germany: the Versailles Diktat, and the stab-in-the-back myth.",
        "{-g2}{pl}Here is the plan the course proposes. Three parts. "
        "{pl.1}Part one: the war created the violence and the grievances. George Mosse called it brutalisation. "
        "In nineteen nineteen, D'Annunzio seized Fiume. In Germany came the Spartacist revolt, then Versailles, and the stab in the back. "
        "{pl.2}Part two: the war also opened the way to revolution, and to the fear of it. "
        "It destroyed Tsarism, and brought the Bolsheviks to power in nineteen seventeen. "
        "In Italy, fear of communism made landowners and shopkeepers pay the Blackshirts, in nineteen nineteen and nineteen twenty. "
        "And in nineteen thirty-three, the Reichstag fire shows the same fear still at work. "
        "{pl.3}Part three: but the war does not explain everything. Each regime rests on its own ideology. Elites chose to hand over power. "
        "And in Germany, the Depression turned a marginal party into a mass movement.",
        "Notice the order. The factor first, then its limits. Part three is where you win the marks.{-pl}",
    ], vis={
        "photo1": dict(type="tableau", img="h2-ypres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="A New Zealand soldier among the ruins of Ypres cathedral, Belgium, 1917 · Archives New Zealand, CC BY-SA 2.0"),
        "ex2": dict(type="exo", niveau="essay", titre="How far was the First World War responsible for the rise of totalitarian regimes?",
                    src="Essay subject of the chapter (course)", enonce=["Part b) of an essay · about 45 minutes"]),
        "meth": dict(type="liste", titre="How far: weigh one factor", cles=["for", "against", "judgement"], items=[
            "The case for the factor", "The case against, or the other factors",
            "A judgement: in the introduction, proved in the conclusion", "Trap: a story of 1918–1933 that never answers"],
            x=150, y=130, w=980),
        "g2": dict(type="globe", code="H2", sc=[1, 4, 5]),
        "pl": dict(type="liste", titre="A plan in three parts (course)", items=[
            "I. The war created the violence and the grievances", "II. It opened the way to revolution, and to the fear of it",
            "III. But the war does not explain everything"], x=150, y=150, w=980),
    }),

    # ================================================================ V. How far : l'introduction
    dict(id="intro", chap="Essay b) · The introduction", fond="aube", humeur="calme",
         retenir="Introduction: a hook · the definition of totalitarianism · the problem (born after 1918 ≠ caused by the war) · the line of argument (the war created the conditions; ideology and circumstances decided) · the plan.",
         beats=[
        "{ing}A good introduction does five things. {ing.1}A hook: a date, or a fact. {ing.2}The definition of the key word. "
        "{ing.3}The problem: why is the question not obvious? {ing.4}Your line of argument: your answer, in one sentence. "
        "{ing.5}And the plan.",
        "{-ing}{pa3}",
        ("P", 2.0),
        "{-pa3}{mod3}Here is a model, built from the course. Listen for the five steps.",
        "{mod3.1}In nineteen twenty-two, Mussolini became Prime Minister of Italy. In nineteen thirty-three, Hitler became chancellor of Germany. "
        "Both regimes were born in the shadow of the Great War. "
        "{mod3.2}A totalitarian regime seeks total control of society, through coercion, in order to transform man according to an ideology. "
        "{mod3.3}The three regimes studied all appeared after nineteen eighteen. But being born after the war is not the same as being caused by it. "
        "{mod3.4}The war created the conditions everywhere. Ideology and local circumstances decided the outcome. "
        "{mod3.5}We will see that the war created violence and grievances. That it opened the way to revolution, and to the fear of it. "
        "But that it does not explain everything.",
        "{-mod3}Five steps. No more is needed.",
    ], vis={
        "ing": dict(type="liste", titre="An introduction in five steps", cles=["hook", "definition", "problem", "line", "plan"], items=[
            "A hook: a date, a fact", "The definition of the key word", "The problem: why it is not obvious",
            "Your line of argument, in one sentence", "The plan"], x=170, y=120, w=940),
        "pa3": dict(type="pause", t="Write your introduction in five sentences.",
                    sous="Hook, definition, problem, line, plan. Pause the video, then play on for a model."),
        "mod3": dict(type="liste", titre="A model introduction", items=[
            "Hook · 1922 Mussolini, 1933 Hitler: born in the shadow of the Great War",
            "Definition · total control of society, through coercion, to transform man according to an ideology",
            "Problem · born after 1918 is not the same as caused by the war",
            "Line · the war created the conditions; ideology and local circumstances decided the outcome",
            "Plan · violence and grievances · revolution and its fear · but not everything"], x=130, y=110, w=1020),
    }),

    # ================================================================ VI. How far : paragraphe et conclusion
    dict(id="paragraphe", chap="Essay b) · Paragraph and conclusion", fond="nuit", humeur="tension",
         retenir="Part III: each regime rests on its own ideology (nation, race, class) · elites handed over power (Victor Emmanuel III 1922, Hindenburg 1933) · the Depression (5.6 million unemployed). Conclusion: the war was the common soil, not the sufficient cause.",
         beats=[
        "{pa4}",
        ("P", 2.0),
        "{-pa4}{mod4}Here is a model of the third paragraph. This is the one that weighs.",
        "{mod4.1}However, the First World War does not explain everything. Each regime was shaped by its own ideology, and by deliberate choices. "
        "{mod4.2}The three regimes rest on opposite ideas. The nation and the absolute State, for Fascism. Race, for Nazism. Class, for Stalinism. "
        "A common war cannot explain such different goals. "
        "{mod4.3}Moreover, power was handed over by the elites. King Victor Emmanuel the Third appointed Mussolini on the thirtieth of October "
        "nineteen twenty-two. Hindenburg appointed Hitler on the thirtieth of January nineteen thirty-three. "
        "{mod4.4}Finally, in Germany, the Depression turned a marginal party into a mass movement. "
        "With five point six million unemployed in nineteen thirty-two, the Nazi vote reached thirty-seven point four per cent. "
        "{mod4.5}The war created the grievances. It took the crisis, and the choices of the elites, to turn them into power.",
        "{-mod4}{ccl}And now the conclusion. It answers the question in one clear sentence. Then it opens.",
        "{ccl.1}The First World War was the common soil of the three regimes, not their sufficient cause. "
        "Without the choices of the elites, and the force of each ideology, the soil would have stayed fallow. "
        "{ccl.2}And for the opening? The historian Jay Winter calls the years nineteen fourteen to nineteen forty-five a single Thirty Years War. "
        "So was the Second World War simply the continuation of the first?",
        "{-ccl}",
    ], vis={
        "pa4": dict(type="pause", t="Write paragraph III: “But the war does not explain everything”.",
                    sous="Three arguments, one example each. Pause the video, then play on for a model."),
        "mod4": dict(type="liste", titre="Model paragraph · part III", cles=["However", "ideology", "elites", "crisis"], items=[
            "However: ideology and choices, not the war alone", "Three ideologies: nation and State · race · class", "Elites hand over power: Victor Emmanuel III (30 Oct. 1922), Hindenburg (30 Jan. 1933)",
            "The Depression: 5.6 million unemployed → 37.4% (July 1932)", "Link: the war created the grievances; crisis and elites turned them into power"],
            x=150, y=130, w=980),
        "ccl": dict(type="def", terme="Model conclusion", cles=["soil", "sufficient", "fallow"],
                    t="The war was the common soil of the three regimes, not their sufficient cause: without the elites' choices and each ideology, the soil would have stayed fallow.",
                    etape="Opening: Jay Winter's “Thirty Years War”, 1914–1945", x=150, y=190, w=980),
    }),

    # ================================================================ VII. autres sujets
    dict(id="sujets", chap="Two more subjects", fond="nuit", humeur="calme",
         retenir="Compare Mussolini and Hitler: a common method (street pressure + legal appointment), different circumstances, the same result; pace: 2–3 years vs a few weeks. To what extent the same control? Identical in method and purpose, unequal in scale and in the criterion that designates the victim.",
         beats=[
        "{s1}Two more subjects from the chapter, with the key to each. {s1.1}First: compare the ways Mussolini and Hitler came to power. "
        "Here, the comparison gives you the plan. A common method: pressure from the street, and legality at the top. "
        "Different circumstances: a frustrated victor, and a humiliated loser. And the same result: the State dismantled from inside. "
        "{s1.2}Which difference should you underline? The pace. Mussolini took two to three years, from the March on Rome to the laws of "
        "nineteen twenty-five. Hitler needed only a few weeks, after the Reichstag fire.",
        "{-s1}{s2}{s2.1}Second subject: to what extent did the three regimes control their societies in the same way? "
        "They used the same instruments. The cult of the leader. Youth captured young. A political police above the law. And the camps. "
        "{s2.2}But the scale and the criterion differ. Soviet terror killed on the largest scale: six hundred and eighty thousand executions in two years. "
        "Nazi violence was biological. Italy was the least lethal, and it kept counter-powers: the monarchy, and the Church.",
        "{-s2}{nu}The course sums it up in one sentence. Learn it by heart.",
        "Identical in method and purpose. Unequal in scale, and in the principle that designates the victim. "
        "That nuance is what separates a good answer from a list of similarities.",
        "{-nu}",
    ], vis={
        "s1": dict(type="liste", titre="Compare the ways Mussolini and Hitler came to power", items=[
            "Common method · different circumstances · same result", "The difference: the pace · 2–3 years vs a few weeks"],
            x=150, y=160, w=980),
        "s2": dict(type="liste", titre="To what extent did the three regimes control their societies in the same way?", items=[
            "The same instruments: leader, youth, police, camps", "Unequal scale and criterion: USSR 680,000 executions · Nazi biology · Italy least lethal"],
            x=150, y=160, w=980),
        "nu": dict(type="def", terme="The nuance that makes the mark", cles=["method", "scale", "victim"],
                   t="Identical in method and purpose, unequal in scale and in the principle that designates the victim.",
                   etape="Class in the USSR · race in Germany · politics in Italy", x=150, y=200, w=980),
    }),

    # ================================================================ VIII. DBQ : la méthode
    dict(id="dbq_meth", chap="DBQ a) · The method", fond="nuit", humeur="calme",
         retenir="DBQ a): judgement in the first line · the document in one sentence · strengths (author, date, what it says, what it implies, purpose) · limits (scope, outcome, silences, nature, snapshot). A propaganda text is reliable evidence of what the regime wanted to project.",
         beats=[
        "{str}Now, the DBQ. Part A always follows the same structure. {str.1}First line: your judgement. Largely, significantly, "
        "partly, or slightly useful. {str.2}Then the document, in one sentence. Who, when, what, and for whom. "
        "{str.3}Then a paragraph of strengths, with several arguments. {str.4}And a paragraph of limits, again with several arguments.",
        "{-str}{ang}Where do you find the arguments? The revision cards of the chapter give you five angles for each side. "
        "{ang.1}For usefulness: the author, the date, what it says, with a short quotation, what it implies, and its purpose. "
        "{ang.2}For limitations: its scope, the outcome it cannot show, its silences, its nature. And the fact that it is only a snapshot of one moment.",
        "{-ang}{prop}One last warning, vital in a chapter full of propaganda. Is a propaganda text unreliable? No. "
        "It is perfectly reliable evidence of what the regime wanted to project. So never throw it away. Say what it proves.",
        "{-prop}",
    ], vis={
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "ang": dict(type="cols", g="Usefulness", gq="author · date · what it says (quote) · what it implies · purpose",
                    d="Limitations", dq="scope · outcome · silences · nature · snapshot", vs="vs"),
        "prop": dict(type="note", terme="A propaganda text", cles=["reliable", "project"],
                     t="It is not “unreliable”: it is reliable evidence of what the regime wanted to project.",
                     etape="Say what it proves, then what it cannot prove", x=150, y=200, w=980),
    }),

    # ================================================================ IX. DBQ a)
    dict(id="dbq_a", chap="DBQ a) · How useful", fond="guerre", humeur="tension",
         retenir="How useful are A (Roosevelt's telegram, 14 April 1939) and B (Hitler at the Obersalzberg, 22 Aug. 1939) for understanding why appeasement failed? Largely useful: both sides of the same failure, dated, one public and one secret. Limits: no British or French voice, intentions not outcomes, notes of listeners, the last months only.",
         beats=[
        "{doc}Here are two documents from the course. {doc.1}Document A is a telegram from President Roosevelt to Hitler, "
        "dated the fourteenth of April nineteen thirty-nine. It was published at once, and an identical telegram went to Mussolini. "
        "Roosevelt asks for an assurance that they will not attack thirty-one named states. "
        "{doc.2}Document B is a speech by Hitler to his commanders-in-chief, at the Obersalzberg, on the twenty-second of August nineteen thirty-nine. "
        "We know it through listeners' notes, produced at Nuremberg.",
        "Roosevelt warns the aggressors:{-doc}",
        ("C", "History will hold them accountable.", "c_fdr"),
        "Four months later, Hitler tells his generals:{-c_fdr}",
        ("C", "There is no outstanding personality in England and France.", "c_ah"),
        "{-c_ah}{ex3}Here is the question, written for this video. "
        "{!How useful}How useful are Documents A and B for understanding why the policy of appeasement failed?",
        "{-ex3}{pa5}",
        ("P", 2.0),
        "{-pa5}{rep}A model. {rep.1}Documents A and B are largely useful for understanding why appeasement failed, because they show the failure "
        "from both sides. {rep.2}Document A is a public telegram sent by President Roosevelt to Hitler on the fourteenth of April nineteen thirty-nine. "
        "Document B is a secret speech given by Hitler to his generals on the twenty-second of August nineteen thirty-nine, ten days before the invasion of Poland.",
        "{rep.3}What are their strengths? First, together they show the two halves of the failure. The democracies could only ask for promises. "
        "And the dictator had concluded that they would never act. Second, their dates frame the end of appeasement: from the month after Prague, "
        "to the eve of the war. Third, Document B was never meant for the public. So Hitler had no reason to hide his reading of the democracies. "
        "And finally, Document A implies a great deal. A list of thirty-one states to protect is an admission. It shows how far aggression was expected to go.",
        "{rep.4}Now, their limits. Neither gives the voice of Britain or France, who led appeasement. Chamberlain and Daladier at Munich "
        "must come from your own knowledge. Both documents show intentions, not outcomes. Document B comes from listeners' notes, "
        "not a word-for-word transcript. And Hitler was trying to reassure worried generals. Finally, both cover only nineteen thirty-nine. "
        "The earlier steps that taught Hitler to gamble, like the Rhineland in nineteen thirty-six, are absent.",
    ], vis={
        "doc": dict(type="liste", titre="Two documents of the course", items=[
            "A · Roosevelt to Hitler, telegram, 14 April 1939: an “assurance” for 31 named states",
            "B · Hitler to his commanders, Obersalzberg, 22 Aug. 1939 (Nuremberg document 798-PS)"], x=150, y=150, w=980),
        "c_fdr": dict(type="cit", a="Franklin D. Roosevelt", o="telegram to Hitler, 14 April 1939", x=200, y=190, w=880),
        "c_ah": dict(type="cit", a="Adolf Hitler", o="speech at the Obersalzberg, 22 August 1939", x=200, y=190, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="How useful are Documents A and B for understanding why the policy of appeasement failed?",
                    src="Question written for this video, on two documents of the course", enonce=["Part a) of a DBQ"]),
        "pa5": dict(type="pause", t="Write the first two lines: your judgement, then the documents in one sentence each.",
                    sous="Pause the video, write them, then play on for a model."),
        "rep": dict(type="liste", titre="A model answer", items=[
            "Largely useful: the failure seen from both sides", "A: Roosevelt's public telegram, 14 April 1939 · B: Hitler's secret speech, 22 Aug. 1939",
            "Strengths: two halves of one failure · dates · a secret speech · 31 states implied",
            "Limits: no British or French voice · intentions only · listeners' notes · 1939 only"], x=150, y=130, w=980),
    }),

    # ================================================================ X. DBQ b)
    dict(id="dbq_b", chap="DBQ b) · Beyond the documents", fond="nuit", humeur="tension",
         retenir="Assess the role of totalitarianism in the collapse of global peace: I. ideologies made war a value (Abyssinia 1935, Lebensraum, Manchuria 1931, Nanjing 1937) · II. the democracies let aggression succeed (League, appeasement, Neutrality Acts) · III. a chain only war could break (Rhineland 1936 → Prague → the pact). Totalitarianism supplied the will; the democracies' reluctance the opportunity.",
         beats=[
        "{ex4}Part B goes further: the documents, plus your own knowledge. And the question is the key issue of the chapter. "
        "Assess the role of totalitarianism in the collapse of global peace in the late nineteen thirties.",
        "{-ex4}{pa6}",
        ("P", 2.0),
        "{-pa6}{g3}First, the chain of events, on the map. {g3.1}October nineteen thirty-five. Italy invades Abyssinia, in the name of Rome. "
        "{g3.2}March nineteen thirty-six. German troops enter the Rhineland, and nobody reacts. {g3.3}March nineteen thirty-eight: the Anschluss. "
        "{g3.4}September nineteen thirty-eight. At Munich, the Sudetenland is handed over, without the Czechs. {g3.5}In March nineteen thirty-nine, Hitler takes Prague. "
        "{g3.6}August nineteen thirty-nine: the Nazi-Soviet pact. {g3.7}And on the first of September: Poland.",
        "{-g3}{pl2}Now the plan, from the course. {pl2.1}Part one: totalitarian ideologies made war a value, and expansion a goal. "
        "Fascism invades Abyssinia in nineteen thirty-five. Nazism wants Lebensraum, announced in Mein Kampf in nineteen twenty-five. "
        "Japanese militarism takes Manchuria in nineteen thirty-one, and Nanjing in nineteen thirty-seven. "
        "Document B belongs here: a dictator who has decided to attack. "
        "{pl2.2}Part two: but the democracies let aggression succeed. Over Abyssinia, the League spared oil. "
        "Britain signed the naval agreement of nineteen thirty-five. Then came Munich, in nineteen thirty-eight. And in America, the Neutrality Acts. "
        "Document A belongs here: the strongest democracy can only ask for promises. "
        "{pl2.3}Part three: the two combined into a chain that only war could break. The Rhineland gamble taught Hitler that the democracies would yield. "
        "Prague ended appeasement. And the pact opened the way to Poland.",
        "{-pl2}{jug}And the judgement, in one sentence from the course. Totalitarianism supplied the will to war. "
        "The democracies' reluctance supplied the opportunity. A strong answer keeps both halves.",
        "{-jug}",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="Assess the role of totalitarianism in the collapse of global peace in the late 1930s.",
                    src="Key Issue of the chapter, as part b) of a DBQ", enonce=["Documents A and B + your own knowledge · about 1 hour"]),
        "pa6": dict(type="pause", t="Write a plan in three parts, and place Documents A and B in it.",
                    sous="Pause the video, write your plan, then play on for a model."),
        "g3": dict(type="globe", code="H2", sc=[27, 28, 33, 34, 35, 36, 37]),
        "pl2": dict(type="liste", titre="A plan in three parts (course)", items=[
            "I. Ideologies made war a value → Abyssinia, Lebensraum, Manchuria · Doc. B",
            "II. The democracies let aggression succeed → League, 1935 agreement, Munich, Neutrality Acts · Doc. A",
            "III. A chain only war could break → Rhineland 1936 … Prague … the pact"], x=150, y=140, w=980),
        "jug": dict(type="def", terme="The judgement", cles=["will", "opportunity"],
                    t="Totalitarianism supplied the will to war; the democracies' reluctance supplied the opportunity.",
                    etape="Keep both halves", x=150, y=200, w=980),
    }),

    # ================================================================ XI. l'oral
    dict(id="oral", chap="The oral: Key Issue and Key Terms", fond="aube", humeur="calme",
         retenir="Oral, 35 min: 20 min preparation, 5 min on a Key Issue, 5 min of questions, 5 min on a Key Term. Key Terms of H2: Totalitarianism, Appeasement. Arendt: propaganda manufactures facts (Reichstag fire); masses supported these regimes.",
         beats=[
        "{or}The oral counts as much as the written exam: coefficient ten. {or.1}You get twenty minutes of preparation. "
        "{or.2}Then five minutes on a Key Issue. {or.3}Five minutes of questions. {or.4}And five minutes of discussion on a Key Term. "
        "Both are drawn by crossing history and geography. And the Key Issue of this chapter is the one we have just planned.",
        "{-or}{kt}Now, the two Key Terms. {kt.1}Totalitarianism: a regime that strives to impose total control on society, through coercion, "
        "in order to transform man according to an ideology. {kt.2}Appeasement: accepting the aggressors' demands, in order to avoid war. "
        "It was the policy of Chamberlain from nineteen thirty-seven, and of Daladier, until Prague in March nineteen thirty-nine. "
        "For each term: a definition, a date, an example, and a link to another chapter.",
        "{-kt}{photo2}{ar}One last tool for the oral, from the revision cards: Hannah Arendt's epigraph. "
        "Totalitarian propaganda treats facts as something power can manufacture. Use it with an example. "
        "In nineteen thirty-three, the Reichstag fire was blamed on the communists. Then add her second lesson. "
        "Large masses supported these regimes. The picture is not black and white.",
        "{-ar}{-photo2}",
    ], vis={
        "or": dict(type="liste", titre="The oral · 35 minutes", items=[
            "20 min of preparation", "5 min: presentation of a Key Issue", "5 min: questions", "5 min: discussion of a Key Term"],
            x=170, y=130, w=940),
        "kt": dict(type="cols", g="Totalitarianism", gq="total control of society, through coercion, to transform man according to an ideology",
                   d="Appeasement", dq="accepting the aggressors' demands to avoid war · Chamberlain, Daladier · Munich 1938", vs="+"),
        "photo2": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, author of The Origins of Totalitarianism (1951), in 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
        "ar": dict(type="note", terme="Arendt's epigraph · how to use it", cles=["manufacture", "Reichstag", "masses"],
                   t="Propaganda treats facts as something power can manufacture: the Reichstag fire blamed on the communists (1933).",
                   etape="Her second lesson: large masses supported these regimes", x=150, y=190, w=980),
    }),

    # ================================================================ XII. les pièges
    dict(id="pieges", chap="The traps of this chapter", fond="guerre", humeur="mystere",
         retenir="Matteotti killed in 1924 (claimed 3 Jan. 1925) · Yezhov executed in 1940, Molotov never · T4: ≈ 70,000 killed 1939–41 · “an isolationist Congress” · Corfu 1923 is not the mutilated victory · Hitler never won a majority.",
         beats=[
        "{pi}Finally, six traps. Each comes from a slide or the class notes, and each can cost you points. "
        "{pi.1}Trap one: Matteotti. The slide dates his murder to nineteen twenty-five. In fact, he was kidnapped and killed "
        "on the tenth of June nineteen twenty-four. Nineteen twenty-five is the year Mussolini claimed responsibility. "
        "It is also the year of the fascistissime laws.",
        "{pi.2}Trap two. The class notes say that Molotov was executed. He never was. He died in nineteen eighty-six. "
        "The head of the NKVD executed at the end of the Great Purge is Yezhov, in nineteen forty.",
        "{pi.3}Trap three: the T four programme. Write that about seventy thousand disabled people were murdered between nineteen thirty-nine "
        "and nineteen forty-one. The older figure, two hundred thousand, is the toll up to nineteen forty-five.",
        "{pi.4}Trap four. The slide speaks of a Republican Congress passing the Neutrality Acts. But the Democrats held the majority. "
        "So write: an isolationist Congress.",
        "{pi.5}Trap five. The Corfu incident dates from nineteen twenty-three, under Mussolini. It is not part of the mutilated victory. Fiume is.",
        "{pi.6}And trap six, the most common of all. Hitler never won a majority in a free election. Thirty-seven point four per cent, at most. "
        "He was appointed.",
        "{-pi}Next time, {fin}the last episode: the recap of the whole chapter, in one go.",
        ("P", 2.0),
    ], vis={
        "pi": dict(type="liste", titre="Six traps", items=[
            "Matteotti: killed 10 June 1924 · claimed 3 Jan. 1925", "Executed in 1940: Yezhov, not Molotov",
            "T4: ≈ 70,000 killed in 1939–41", "Neutrality Acts: “an isolationist Congress”",
            "Corfu (1923) is not the mutilated victory: Fiume is", "Hitler: 37.4% at most · appointed, never elected by a majority"],
            x=150, y=110, w=980),
        "fin": dict(type="mot", t="Next: the recap", g="Episode 9 · the whole chapter", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="In an Explain answer, how is each reason written?", r=["One paragraph: point, evidence, explanation, link",
         "One sentence per reason", "A list of dates", "A quotation and its analysis"], ok=0, voir="peel",
         ex="A date, a figure or a name as evidence, and a link back to the question."),
    dict(q="What is the highest share of the vote the NSDAP won before Hitler's appointment?", r=["37.4% (July 1932)", "51% (March 1933)",
         "18.3% (Sept. 1930)", "33.1% (Nov. 1932)"], ok=0, voir="gr",
         ex="It was the largest party, but never a majority; it even fell to 33.1% in November 1932."),
    dict(q="In “How far was WW1 responsible…”, what does part III do?", r=["It shows the limits of the factor: ideologies, elites, the Depression",
         "It tells the story of the March on Rome", "It repeats part I with other examples", "It describes the Second World War"], ok=0, voir="pl",
         ex="The factor first, then its limits: that is where the judgement is built."),
    dict(q="Which is NOT one of the five steps of the model introduction?", r=["A list of every date of the chapter", "A hook",
         "The definition of the key word", "The line of argument"], ok=0, voir="ing",
         ex="Hook, definition, problem, line, plan."),
    dict(q="Comparing Mussolini and Hitler, what is the main difference in how they dismantled the State?", r=["The pace: years for Mussolini, weeks for Hitler",
         "Mussolini was elected, Hitler was not", "Hitler had no paramilitary forces", "Mussolini seized power by force of arms"], ok=0, voir="s1",
         ex="Two to three years (1922–1925) against a few weeks after the Reichstag fire."),
    dict(q="What must the first line of a DBQ part a) contain?", r=["A judgement: largely / partly useful…", "The date of the document",
         "A quotation", "A definition"], ok=0, voir="str",
         ex="Then the document in one sentence, a paragraph of strengths, a paragraph of limits."),
    dict(q="Which is a valid LIMIT of Hitler's speech of 22 August 1939?", r=["It is known through listeners' notes, not a verbatim transcript",
         "It was secret", "It is dated", "It was given to generals"], ok=0, voir="rep",
         ex="Its secrecy is a strength; its transmission and purpose (reassuring generals) are limits."),
    dict(q="Who was executed at the end of the Great Purge, in 1940?", r=["Yezhov, head of the NKVD", "Molotov", "Beria", "Kirov"], ok=0,
         voir="pi", ex="Molotov died in 1986; Beria was executed in 1953, after Stalin's death."),
]

CREDITS = [
    "Content: the essay subjects of chapter H2 (course exam data), its Key Issue and Key Terms, the revision cards (essay and DBQ), two documents of the course DBQs (Roosevelt's telegram of 14 April 1939; Hitler's speech at the Obersalzberg, 22 August 1939), M. Ros's chart of the NSDAP vote, the points to check of the chapter.",
    "The Explain question, the DBQ a) question and the model answers were written for this video.",
    "Photographs (via Wikimedia Commons): Ypres cathedral in ruins, 1917 (Henry Armytage Sanders, Archives New Zealand, CC BY-SA 2.0); Hannah Arendt in 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
