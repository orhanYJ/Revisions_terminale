"""DNL History · H3 « World War Two » — série vidéo, épisode 1 : « A world war » (l'introduction du chapitre).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h3_1 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
d'un chapitre, dnl/cartes/<code>.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans
l'ordre chronologique de la carte).
  H3 : 0 guerre-monde · 1 Mandchourie · 3 Chine 1937 · 4 pacte · 5 Pologne · 11 attaque à l'ouest · 16 armistice ·
       24 pourquoi l'URSS · 25 Barbarossa · 28 anéantissement · 31 Pearl Harbor · 33 guerre mondiale · 34 France exploitée ·
       41 Nouvel Ordre européen fin 1942 · 42 Stalingrad · 45 bilan du génocide
  H2 : 27 Abyssinie · 28 Rhénanie · 33 Anschluss · 34 Munich · 35 Prague · 37 Pologne
Contenu : l'introduction du chapitre dans le site (dnl/index.html, CHAPTERS.H3, section « Intro », tableau des divisions),
reliée aux chapitres 1 et 2 et aux exemples des parties I à III (chiffres du cours) ; ce qui n'est pas dans le cours est
dit « outside the course ».
Retour du responsable du projet sur la première version (8 min) : « rajoute plus de détails, trop résumé » → version longue.
Plan de la série H3 : 1 A world war · 2 The fall of France · 3 Britain alone · 4 Barbarossa · 5 Towards the genocide ·
6 WWII at the exam (essay and DBQ) · 7 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-1"
NOTION = "World War Two"
NUM = 1
TITRE = "A world war"
SUIVANT = "Episode 2 · The fall of France"
PRONONCIATION = {"Grossraum": "Gross-rowm", "Lebensraum": "Lay-bens-rowm", "Aglan": "Ag-lan", "Mukden": "Mook-den",
                 "Reichstag": "Rikes-tahg", "Wehrmacht": "Vair-markt", "Einsatzgruppen": "Ine-zats-groopen",
                 "Übermensch": "Oober-mensh", "Untermensch": "Oonter-mensh", "Anschluss": "Ahn-shloos",
                 "Sudetenland": "Soo-day-ten-land", "Reichsmarks": "Rikes-marks", "Abyssinia": "Abby-sinnia",
                 "Puyi": "Poo-yee", "Relève": "Ruh-lev"}

# tableau des divisions du cours (introduction) : 1940, 1942, 1943, 1944, 1945
ANS = [1940, 1942, 1943, 1944, 1945]
DIV_ALLIES = list(zip(ANS, [393, 397, 524, 575, 656]))
DIV_AXE = list(zip(ANS, [272, 350, 413, 349, 328]))
DIV_URSS = list(zip(ANS, [200, 250, 350, 400, 488]))
DIV_ALL = list(zip(ANS, [189, 261, 327, 347, 319]))
DIV_USA = list(zip(ANS, [24, 76, 95, 94, 94]))
DIV_FRA = list(zip(ANS, [105, 0, 5, 7, 14]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Sixty million dead. Battles from the Atlantic to the Pacific, from the Arctic to the deserts of Africa, "
        "from the streets of Stalingrad to the islands of the Pacific. The Second World War is the deadliest conflict in human history.",
        "{-q1}{q2}But when did it start? Most people would answer: on the first of September, 1939, when Germany invaded Poland. "
        "In this chapter, the course gives a different answer… and that answer is your first argument in an essay.",
        "{-q2}{q3}And a second question, even more important: what did the Nazis want to build with this war? "
        "Not just a bigger Germany. A whole new continent. That is what this episode is about.",
        "{-q3}{-g0}{plan}This series covers the whole chapter, in seven episodes. {plan.1}Today: why this was a world war, "
        "why it was so deadly, and what the Nazis wanted to build with it. {plan.2}Then the fall of France, {plan.3}Britain alone, "
        "{plan.4}Operation Barbarossa, {plan.5}and the racial policy that led to genocide. "
        "{plan.6}After that, an episode only for the exam: essay and DBQ. {plan.7}And a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[0]),
        "q1": dict(type="question", t="60 million dead.", bande=True),
        "q2": dict(type="question", t="When did the war really begin?", bande=True),
        "q3": dict(type="question", t="What did the Nazis want to build?", bande=True),
        "plan": dict(type="liste", titre="H3 · World War Two, in seven episodes", items=[
            "A world war: dates, ideology, the New European Order", "The fall of France (Part I.1)",
            "Britain alone, supported by the US (Part I.2)", "Barbarossa: a war of annihilation (Part II)",
            "Towards the genocide (Part III)", "WWII at the exam: essay and DBQ", "Recap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 1", t="A world war",
                      sous="1931 – 1947 · an ideological war · the New European Order"),
    }),

    # ================================================================ I. en Asie, dès 1931
    dict(id="asie", chap="It began in Asia", fond="nuit", humeur="tension",
         retenir="The war began in Asia: Manchuria in 1931, southern China in 1937. Each time, the League of Nations failed to stop Japan.",
         beats=[
        "{g1}Many historians, among them Jay Winter and Robert Frank, have shown that the war began before 1939. "
        "Its chronology can be stretched from 1931… all the way to 1947. To understand why, we have to look east.",
        "{g1.1}September 1931. You saw it in chapter one: the Great Depression hits Japan hard, and its army wants raw materials "
        "and markets of its own. After the Mukden incident, the Japanese army conquers Manchuria, in north-eastern China.",
        "Manchuria is rich in coal and iron: exactly what an industrial power without resources needs. "
        "Japan turns it into a puppet state, Manchukuo, with the last emperor of China, Puyi, as its nominal head, but controlled from Tokyo.",
        "{lig1}What does the League of Nations do? {lig1.1}It condemns the invasion. {lig1.2}Japan simply leaves the League, in 1933. "
        "{lig1.3}And nothing else happens: no sanctions, no army. The lesson is clear for every aggressive regime: "
        "collective security has no teeth.",
        "{-lig1}{g1.2}And 1937 is the turning point. Japan attacks southern China, in a full-scale war. "
        "China immediately appeals to the League of Nations for help… and once again, the League proves incapable of regulating the tension.",
        "{-g1}{g1b}{g1b.1}Behind this expansion, chapter two showed you an ideology. Japan wants autarky, its own resources, "
        "and claims to be a superior race destined to lead Asia. {g1b.2}And in December 1937, at Nanjing, Japanese troops kill "
        "between two hundred thousand and three hundred thousand civilians and prisoners. Racist ideology, militarism, civilians as targets: "
        "{!the features of the coming war}the features of the coming world war are already there.",
        "{-g1b}{livre}That is why Robert Frank and Alya Aglan put the dates on the cover of their book, in 2015: "
        "La Guerre-monde, nineteen thirty-seven to nineteen forty-seven. The world war. {!The dates are an argument}The dates themselves are an argument: "
        "the war started in Asia, two years before it started in Europe.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[1, 3]),
        "lig1": dict(type="liste", titre="Manchuria, 1931: the League's response", x=60, y=150, w=600, petit=True, bande=True, items=[
            "It condemns the invasion", "Japan leaves the League (1933)", "No sanctions, no army: collective security fails"]),
        "g1b": dict(type="globe", code="H2", sc=[18, 32]),
        "livre": dict(type="mot", t="1937 – 1947", g="Robert Frank & Alya Aglan, La Guerre-monde (2015)", y=250, taille=110),
    }),

    # ================================================================ II. en Europe, la marche à la guerre
    dict(id="europe", chap="The road to war in Europe", fond="nuit", humeur="tension",
         retenir="1935 Ethiopia · 1936 Rhineland · 1938 Anschluss and Munich · March 1939 Prague · August 1939 the pact · 1 September 1939 Poland.",
         beats=[
        "{g2}In Europe, the road to war is a series of tests, and each time the democracies give way. Chapter two in sixty seconds.",
        "{g2.1}October 1935: Fascist Italy invades Abyssinia, Ethiopia. The League imposes weak sanctions… that change nothing.",
        "{g2.2}March 1936: Hitler sends troops into the Rhineland, demilitarised since Versailles. A gamble. France and Britain do nothing, and the gamble pays off.",
        "{g2.3}March 1938: the Anschluss. Austria is annexed to Germany. {g2.4}September 1938: at Munich, France and Britain hand over "
        "the Sudetenland to Hitler, without even asking the Czechs. This is appeasement.",
        "{g2.5}March 1939: Hitler takes Prague. This time, it is not Germans he is uniting: it is a conquest. Appeasement is dead.",
        "{-g2}{g3}{g3.1}August 1939: the shock. Nazi Germany and the Soviet Union, sworn ideological enemies, sign a pact. "
        "In a secret protocol, they plan to share Poland. {g3.2}And on the first of September 1939, Germany invades Poland. "
        "Two days later, Britain and France declare war. The war in Europe has begun.",
        "{-g3}{g4}But even then, it is not yet a world war. That happens in 1941. {g4.1}In June, Germany invades the Soviet Union. "
        "{g4.2}In December, Japan attacks the American fleet at Pearl Harbor, {g4.3}and Germany and Italy declare war on the United States. "
        "Now the war is fought on every ocean and every continent.",
        "{-g4}{frise}So here is the chronology to keep in mind. {frise.1}1931, Manchuria. {frise.2}1937, Japan attacks southern China. "
        "{frise.3}1939, Germany invades Poland: the war begins in Europe. {frise.4}1941, Barbarossa in June, Pearl Harbor in December: "
        "the war becomes truly global. {frise.5}1945, the end of the fighting. {frise.6}And 1947, the end of the world war for Frank and Aglan: "
        "the moment when a new conflict, the Cold War, takes over. That is chapter four.",
        "{-frise}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is one way to say it. {rep1.1}The war did not start in Europe, but in Asia. "
        "{rep1.2}It started with Japanese aggression in Manchuria in 1931, and above all against China in 1937. "
        "{rep1.3}And the League of Nations' failure, in Asia as in Europe, let it spread to the whole world.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[27, 28, 33, 34, 35]),
        "g3": dict(type="globe", code="H3", sc=[4, 5]),
        "g4": dict(type="globe", code="H3", sc=[25, 31, 33]),
        "frise": dict(type="frise", items=[
            dict(nom="Manchuria", d=1931, q="Japan seizes it"), dict(nom="China", d=1937, q="the turning point"),
            dict(nom="Poland", d=1939, q="war in Europe"), dict(nom="Global war", d=1941, q="Barbarossa · Pearl Harbor"),
            dict(nom="Fighting ends", d=1945, q="Europe, then Asia"), dict(nom="War ends", d=1947, q="for Frank & Aglan")]),
        "pa1": dict(type="pause", t="In two sentences: why can we say the war began before 1939?",
                    sous="Pause the video, write your answer, then play on to compare."),
        "rep1": dict(type="liste", titre="A model answer", items=[
            "It began in Asia, not in Europe.", "Japanese aggression: Manchuria (1931), southern China (1937).",
            "The League of Nations' failure let it spread to the world."], x=170, y=150, w=940),
    }),

    # ================================================================ III. une guerre idéologique
    dict(id="ideologie", chap="An ideological war", fond="guerre", humeur="tension",
         retenir="Not only defeating armies, but destroying the enemy's civilisation: an ideological war, about 60 million dead, three fifths of them on the Eastern Front.",
         beats=[
        "{q4}Why was this war so deadly? Because it was not like other wars.",
        "{-q4}{def1}In most wars, the aim is to defeat the enemy's armies, then to negotiate a peace. "
        "Here, the aim was to destroy the enemy's civilisation. It was an {!ideological war}ideological war, "
        "in which no side would give up until death.",
        "{-def1}{photo}The course opens the chapter with a photograph that says this better than any definition. "
        "Einsatzgruppen killers, around 1941 or 1942, shooting men standing in a pit. A photograph probably taken by one of the killers. "
        "The killers photograph their own crimes: they are not ashamed, they think they are building something. "
        "We will come back to these mobile killing squads in episode five.",
        "{-photo}{ideo}The course calls this war {!the ideological crucible}the ideological crucible of the twentieth century: "
        "the moment when the great ideologies of the century met, in total war. {ideo.1}Nazism, which sees history as a struggle of races. "
        "{ideo.2}Fascism, the Italian model of the all-powerful state. {ideo.3}Soviet communism, which sees it as a struggle of classes. "
        "{ideo.4}And liberal democracy, Britain and the United States, which fight for freedom… and for their empires.",
        "{-ideo}{bil}And the toll is without precedent. {bil.1}About sixty million dead in total. "
        "{bil.2}Three fifths of all the dead of the war died on the Eastern Front. "
        "{bil.3}The Soviet Union alone lost twenty-seven to twenty-eight million people: one in seven of its population. "
        "{bil.4}And six million Jews were murdered in the genocide. "
        "Most of the victims were civilians: that is the mark of an ideological war.",
    ], vis={
        "q4": dict(type="question", t="Why was this war so deadly?"),
        "def1": dict(type="def", cles=["armies", "civilisation"], terme="An ideological war",
                     t="The aim is not only to defeat the enemy's armies, but to destroy its civilisation.",
                     etape="No side gives up until death · no limits on violence", x=170, y=200, w=940),
        "photo": dict(type="note", cles=["Einsatzgruppen", "killers"], terme="The first document of the chapter",
                      t="Einsatzgruppen killers shooting men standing in a pit, around 1941–1942.",
                      etape="A photograph probably taken by one of the killers (described here, not shown).", x=170, y=200, w=940),
        "ideo": dict(type="liste", titre="The ideologies in the crucible", cles=["races", "state", "classes", "freedom"], items=[
            "Nazism: history as a struggle of races", "Fascism: the all-powerful state", "Communism: history as a struggle of classes",
            "Liberal democracy: freedom… and empires"], x=170, y=130, w=940),
        "bil": dict(type="liste", titre="The toll (course figures)", items=[
            "≈ 60 million dead", "3/5 of them on the Eastern Front", "USSR: 27–28 million, one in seven",
            "6 million Jews murdered"], x=170, y=130, w=940),
    }),

    # ================================================================ IV. une guerre de nombres
    dict(id="nombres", chap="A war of numbers", fond="nuit", humeur="lumiere",
         retenir="1940: the Axis wins with fewer divisions (surprise, Blitzkrieg). After 1942 the Allies outnumber it, up to 656 against 328 in 1945. The USSR carries the weight.",
         beats=[
        "{gr}One more document from the introduction: the number of divisions on each side. A division is a large army unit, "
        "about ten to twenty thousand men (outside the course). {gr.1}The Allies, in blue. {gr.2}The Axis, in red.",
        "{gr.3}Look at 1940: 393 Allied divisions against 272 for the Axis. The Allies are more numerous… and yet the Axis wins everything. "
        "Why? Surprise, speed, tanks and aircraft working together: the Blitzkrieg. That is episode two.",
        "{gr.4}Then, after 1942, the gap opens and never closes. 524 against 413 in 1943, 575 against 349 in 1944, "
        "656 against 328 in 1945. Two to one.",
        "{-gr}{gr2}Now look country by country. {gr2.1}The Soviet Union: 200 divisions in 1940, 350 in 1943, 488 in 1945. "
        "{gr2.2}Germany peaks at 347, in 1944, then falls back. {gr2.3}The United States climbs from 24 to 95: its army is built during the war. "
        "{gr2.4}And France: 105 divisions in 1940… zero in 1942. In two years, the French army disappears. That too is episode two.",
        "{-gr2}{lec}So, three lessons from this table. {lec.1}In 1940, numbers are not enough: the Axis wins with fewer divisions. "
        "{lec.2}From 1942, when the Soviet Union and the United States are fully in the war, numbers decide: the Axis cannot win a long war. "
        "{lec.3}And it is the Soviet Union that carries most of the weight on land.",
        "{lec.4}One detail to know: the course table counts Romania among the Allies, although it fought with the Axis until August 1944. "
        "If you use the table in a DBQ, that is a limit worth mentioning.",
    ], vis={
        "gr": dict(type="graphe", titre="Divisions on each side, 1940–1945 (course)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1939.5, 1945.5], y=[0, 700], gx=ANS, gy=[200, 400, 600], lx="year", ly="divisions"),
                   el=[dict(type="courbe", pts=[list(p) for p in DIV_ALLIES], c="el", lbl="Allies", lp=[1944.6, 690], dur=2.0),
                       dict(type="courbe", pts=[list(p) for p in DIV_AXE], c="ca", lbl="Axis", lp=[1944.7, 280], dur=2.0),
                       dict(type="points", pts=[[1940, 393], [1940, 272]], c="sa", lbl="1940: 393 / 272", lp=[1941.0, 470]),
                       dict(type="points", pts=[[1945, 656], [1945, 328]], c="sa", lbl="1945: 656 / 328", lp=[1943.6, 600])]),
        "gr2": dict(type="graphe", titre="Divisions by country (course)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1939.5, 1945.5], y=[0, 520], gx=ANS, gy=[100, 200, 300, 400, 500], lx="year", ly="divisions"),
                    el=[dict(type="courbe", pts=[list(p) for p in DIV_URSS], c="el", lbl="USSR", lp=[1944.8, 505], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_ALL], c="ca", lbl="Germany", lp=[1944.6, 375], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_USA], c="vert", lbl="USA", lp=[1944.8, 120], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_FRA], c="sa", lbl="France", lp=[1941.0, 120], dur=1.8)]),
        "lec": dict(type="liste", titre="What the table shows", items=[
            "1940: the Axis wins with fewer divisions", "From 1942: numbers decide, a long war is lost for the Axis",
            "The USSR carries the weight on land", "Limit: Romania counted as an Ally"], x=170, y=130, w=940),
    }),

    # ================================================================ V. le Nouvel Ordre européen
    dict(id="ordre", chap="The New European Order", fond="nuit", humeur="tension",
         retenir="Key term. The New European Order: Nazi rule over Europe, presented as saving European civilisation. Five driving forces.",
         beats=[
        "{g5}For the Nazis, war and conquest were an opportunity. {g5.1}The opportunity to build a grandiose political and economic apparatus "
        "that would entrench their domination of Europe. Look at the map at the end of 1942: from the Atlantic to the Volga, "
        "from Norway to the Mediterranean.",
        "{-g5}{def2}This is a {!key term}key term of the chapter: the {!New European Order}New European Order. "
        "Nazi rule over the continent, which its supporters presented as saving European civilisation from collapse. "
        "Notice the word presented: it is propaganda. In reality, Europe is organised for Germany.",
        "{-def2}{forces}The course gives it five driving forces. Learn them: they are a ready-made plan. "
        "{forces.1}One: Europe as a racial entity, and racial purification through genocide. "
        "{forces.2}Two: the quest for Lebensraum, living space, in the East. "
        "{forces.3}Three: the crusade against communism. "
        "{forces.4}Four: the Grossraum, a single European economic unit, serving Germany. "
        "{forces.5}And five: supplying Germany with the people, the materials and the money that total war requires.",
        "{-forces}{unex}Now, one example for each, taken from the rest of the chapter. In an essay, a force without an example is worth nothing.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[41]),
        "def2": dict(type="def", cles=["rule", "presented", "saving"], terme="Key term · New European Order",
                     t="Nazi rule over Europe, presented by its supporters as saving European civilisation from collapse.",
                     etape="“Presented”: propaganda. In reality, Europe is organised for Germany.", x=170, y=200, w=940),
        "unex": dict(type="mot", t="One force · one example", g="in an essay, a force without an example is worth nothing", y=260, taille=80),
        "forces": dict(type="liste", titre="The five driving forces", cles=["racial", "Lebensraum", "communism", "Grossraum", "total"], items=[
            "Europe as a racial entity: purification through genocide", "Lebensraum: living space in the East",
            "A crusade against communism", "The Grossraum: one economic unit serving Germany",
            "Supplying total war: people, materials, money"], x=170, y=110, w=940),
    }),

    # ================================================================ VI. cinq forces, cinq exemples
    dict(id="exemples", chap="Five forces, five examples", fond="nuit", humeur="tension",
         retenir="Racial: 6 million Jews murdered · Lebensraum: Barbarossa · anti-communism: commissars shot (Commissar Order, June 1941) · Grossraum: Ukrainian wheat, Caucasus oil · total war: 20 million Reichsmarks a day from France.",
         beats=[
        "{g6}{g6.1}One: the racial entity. The Nazis wanted a Europe purified by race. The result: six million Jews murdered, "
        "two thirds of the Jews of Europe. On the map, the share of Jews killed: ninety per cent in Poland, ninety-seven in Lithuania.",
        "{g6.2}Two: Lebensraum. In Mein Kampf, Hitler already wanted to conquer living space in the East. On the twenty-second of June 1941, "
        "Operation Barbarossa launches the German army towards Leningrad, Moscow and Kiev. "
        "The Slavs are seen as Untermenschen, sub-humans, to be enslaved or driven out to make room for German settlers.",
        "{g6.3}Three: the crusade against communism. The Nazis speak of Jewish Bolshevism, as if communists and Jews were one enemy. "
        "The Commissar Order, issued by the Wehrmacht high command on the sixth of June 1941: Soviet political commissars are to be shot as soon as they are captured. "
        "No prisoners, no rules: a war of annihilation.",
        "{g6.4}Four: the Grossraum, the great economic space. The East must feed Germany: the wheat of Ukraine, the oil of the Caucasus. "
        "That is why, in 1942, the German army heads for Stalingrad and the Caucasus.",
        "{g6.5}And five: supplying total war. Occupied France pays twenty million Reichsmarks a day in occupation fees. "
        "Its coal, its food, its fuel are requisitioned. And from 1942, French workers are sent to Germany: first volunteers, through the Relève, then, from February 1943, forced labourers, with the STO.",
        "{-g6}{tab5}So here is your table: five forces, five examples. Pause the video and copy it: it is the backbone of any essay on this chapter.",
        ("P", 4.0),
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[45, 25, 28, 24, 34]),
        "tab5": dict(type="liste", titre="Five forces · five examples", items=[
            "Racial entity → 6 million Jews murdered (90% in Poland)", "Lebensraum → Barbarossa, 22 June 1941; Slavs as “Untermenschen”",
            "Anti-communism → the Commissar Order (June 1941): commissars shot", "Grossraum → Ukrainian wheat, Caucasus oil",
            "Total war → France: 20 million RM a day, the STO"], x=150, y=110, w=980),
    }),

    # ================================================================ VII. Hitler le dit lui-même
    dict(id="hitler", chap="In Hitler's own words", fond="guerre", humeur="tension",
         retenir="Hitler, 11 December 1941, as the course quotes him: “the absolute elimination of the Jews, the establishment of the supremacy of the German people, and the creation of a real community of nations under German leadership”.",
         beats=[
        "{reich}And Hitler himself said it, according to the course, before the Reichstag, on the eleventh of December 1941, "
        "the day Germany declared war on the United States. Here is the sentence as the course quotes it. Listen carefully.",
        ("C", "the absolute elimination of the Jews, the establishment of the supremacy of the German people, "
              "and the creation of a real community of nations under German leadership", "c_hitler"),
        "{-c_hitler}{-reich}{ana}Let's take it apart. {ana.1}First, the absolute elimination of the Jews: the racial goal, "
        "announced in public, at the very moment when the mass killings are under way in the East. "
        "{ana.2}Second, the supremacy of the German people: the national goal, the master race ruling the others. "
        "{ana.3}Third, a community of nations under German leadership: the European goal. It sounds like cooperation… "
        "but leadership means domination.",
        "{-ana}{lien}Three goals in one sentence: racial, national, European. Keep this quotation: "
        "it fits the opening of almost any essay on the New European Order. And remember the date: it shows that the genocide "
        "was not a secret side effect of the war, but one of its declared aims.",
    ], vis={
        "reich": dict(type="tableau", img="h3-reichstag", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                      legende="Hitler declares war on the United States, Reichstag, 11 December 1941 (Wikimedia Commons, CC BY-SA 3.0)"),
        "c_hitler": dict(type="cit", a="Adolf Hitler", o="speech to the Reichstag, 11 December 1941, as quoted in the course", x=200, y=170, w=880),
        "ana": dict(type="liste", titre="Three goals in one sentence", cles=["racial", "national", "European"], items=[
            "“the absolute elimination of the Jews” → the racial goal", "“the supremacy of the German people” → the national goal",
            "“a community of nations under German leadership” → the European goal"], x=150, y=130, w=980),
        "lien": dict(type="note", terme="Why this quotation matters", cles=["declared", "aims"],
                     t="The genocide was not a hidden side effect of the war, but one of its declared aims.",
                     etape="A public speech, 11 December 1941, while the killings are under way in the East.", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. trois études de cas
    dict(id="cas", chap="Three case studies", fond="nuit", humeur="calme",
         retenir="The chapter tests the New European Order on three cases: France in the West, Barbarossa in the East, the genocide.",
         beats=[
        "{g7}So the chapter assesses this order through three cases. {g7.1}In the West, the invasion and occupation of France: "
        "a defeat in six weeks, a country cut into zones, a regime that collaborates.",
        "{g7.2}In the East, the quest for Lebensraum and the war against the Soviet Union: a war of annihilation, "
        "five million dead in the first two hundred days, and the turning point of Stalingrad.",
        "{g7.3}And everywhere, the racial policy that led to genocide: the ghettos, the shootings, the killing centres.",
        "{-g7}{cmp}Notice the contrast. {cmp.1}In the West, France is exploited but treated as a partner, at least on the surface. "
        "{cmp.2}In the East, the conquered peoples are to be enslaved or exterminated. The same order, two faces: "
        "this contrast is an excellent argument for the essay.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[16, 25, 32]),
        "cmp": dict(type="cols", g="In the West", gq="France exploited, a “partner” on the surface: collaboration", d="In the East",
                    dq="peoples enslaved or exterminated: a war of annihilation", vs="≠"),
    }),

    # ================================================================ IX. pour l'essay
    dict(id="essay", chap="Using it in an essay", fond="aube", humeur="calme",
         retenir="Key issue: “Assess the aims of the New European Order.” Introduction: hook, definition, context, question, plan. Three parts: racial-ideological, economic-colonial, total war.",
         beats=[
        "{ki}The key issue of this chapter is exactly this: {!Assess the aims}assess the aims of the New European Order. "
        "And the two key terms: New European Order, and Lebensraum.",
        "{-ki}{intro}A good introduction has five steps. {intro.1}A hook: a date, a quotation, a figure. "
        "{intro.2}The definition of the key term. {intro.3}The context: dates and places. "
        "{intro.4}The question, rephrased. {intro.5}And the plan, announced.",
        "{-intro}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}Here is a model. On the eleventh of December 1941, Hitler announced, as the course quotes him, the absolute elimination of the Jews "
        "and the creation of a community of nations under German leadership. This was the New European Order: Nazi rule over Europe, "
        "presented as saving European civilisation. Between 1939 and 1942, Germany built it by conquest, from France to the Volga. "
        "What were its aims, and to what extent were they achieved? We will see that it was a racial and ideological order, "
        "a colonial and economic order, and an order designed for total war.",
        "{-rep2}{plan2}And the plan, with the evidence for each part. {plan2.1}Part one: a racial and ideological order. "
        "The genocide, six million Jews; the crusade against Jewish Bolshevism. "
        "{plan2.2}Part two: a colonial and economic order. Lebensraum and Barbarossa; the Grossraum, Ukrainian wheat and Caucasus oil. "
        "{plan2.3}Part three: an order for total war. France pays twenty million Reichsmarks a day; the STO; Soviet prisoners starved to death.",
        "{plan2.4}And to assess, not just describe: show the limits. The order collapses on the battlefield, at Stalingrad, "
        "in February 1943; and it meets resistance, from London to Warsaw.",
    ], vis={
        "ki": dict(type="question", t="Key issue: assess the aims of the New European Order."),
        "intro": dict(type="liste", titre="An introduction in five steps", items=[
            "A hook: date, quotation, figure", "Define the key term", "Context: dates and places", "The question, rephrased",
            "The plan, announced"], x=170, y=120, w=940),
        "pa2": dict(type="pause", t="Write the introduction of an essay on the aims of the New European Order.",
                    sous="Pause the video, use the five steps, then play on for a model."),
        "rep2": dict(type="note", terme="A model introduction", cles=["hook", "racial", "colonial", "total"],
                     t="11 Dec. 1941: Hitler announces (as the course quotes him) “the absolute elimination of the Jews”… The New European Order: Nazi rule presented as saving Europe. "
                       "1939–1942, from France to the Volga. What were its aims? A racial order, a colonial order, an order for total war.",
                     etape="Hook · definition · context · question · plan", x=150, y=150, w=980),
        "plan2": dict(type="liste", titre="A three-part plan, with evidence", items=[
            "I. Racial and ideological: genocide (6 million), “Jewish Bolshevism”",
            "II. Colonial and economic: Lebensraum, Barbarossa, the Grossraum",
            "III. Total war: France's 20 million RM a day, the STO, Soviet POWs",
            "Assess: the limits — Stalingrad (Feb. 1943), resistance"], x=150, y=110, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}A world war, which began in Asia, in 1931 and 1937, and spread to Europe in 1939 and to the whole world in 1941. "
        "{carte.2}An ideological war, about sixty million dead, the crucible of the century. "
        "{carte.3}A war of numbers, that the Allies won after 1942, with the Soviet Union carrying the weight. "
        "{carte.4}And the key term: the New European Order, with its five driving forces and one example each.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the fall of France. Six weeks in May and June 1940, an armistice, a country cut in two… "
        "and a regime that chose collaboration.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="A WORLD WAR", branches=[
            dict(t="Dates", items=["1931 Manchuria · 1937 China", "1939 Poland · 1941 global", "1937–1947: Frank & Aglan"]),
            dict(t="Ideology", items=["destroy a civilisation", "≈ 60 million dead", "3/5 on the Eastern Front"]),
            dict(t="Numbers", items=["1940: 393 / 272", "1945: 656 / 328", "USSR: 488"]),
            dict(t="New European Order", items=["race · Lebensraum", "anti-communism", "Grossraum · total war"])]),
        "fin": dict(type="mot", t="Next: the fall of France", g="Episode 2 · May – June 1940", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Why do historians such as Robert Frank date the war from 1937?",
         r=["Japan attacked southern China and the League proved powerless", "Germany invaded Poland",
            "Italy invaded Ethiopia", "Germany declared war on the United States"], ok=0, voir="livre",
         ex="Their book is titled La Guerre-monde 1937–1947 (2015); its chronology can even start in 1931, with Manchuria."),
    dict(q="What did the League of Nations do after Japan invaded Manchuria in 1931?",
         r=["It condemned the invasion, and Japan left the League", "It sent an international army",
            "It imposed an oil embargo on Japan", "It recognised Manchuria as Japanese"], ok=0, voir="lig1",
         ex="Condemnation without sanctions: collective security had no teeth."),
    dict(q="Which event of March 1939 ended appeasement?",
         r=["Hitler took Prague", "The Anschluss", "The Munich conference", "The remilitarisation of the Rhineland"], ok=0, voir="g2",
         ex="Prague was not a German-speaking territory: it was a conquest, and Britain and France stopped giving way."),
    dict(q="What makes the Second World War an ideological war?",
         r=["The aim was to destroy the enemy's civilisation, not only its armies", "It was fought only by dictatorships",
            "It was fought only in Europe", "It ended with a negotiated peace"], ok=0, voir="def1",
         ex="No side would give up until death: hence about 60 million dead, most of them civilians."),
    dict(q="In 1945, how many divisions did the Allies and the Axis have, according to the course table?",
         r=["656 against 328", "328 against 656", "393 against 272", "488 against 347"], ok=0, voir="gr",
         ex="393 against 272 is 1940; 488 is the USSR alone in 1945, 347 Germany's peak in 1944."),
    dict(q="What is the New European Order?",
         r=["Nazi rule over Europe, presented as saving its civilisation", "The Allied plan for peace after 1945",
            "The League of Nations reformed in 1940", "The Vichy constitution"], ok=0, voir="def2",
         ex="It is a key term of the chapter: define it, then give its five driving forces with an example each."),
    dict(q="Which example illustrates the Grossraum?",
         r=["Ukrainian wheat and Caucasus oil for Germany", "The Commissar Order of June 1941",
            "The Warsaw ghetto", "De Gaulle's appeal of 18 June 1940"], ok=0, voir="g6",
         ex="The Grossraum is Europe as one economic unit serving Germany: the East had to feed the Reich."),
    dict(q="When did Hitler define the “new order” before the Reichstag?",
         r=["11 December 1941", "1 September 1939", "22 June 1941", "30 January 1933"], ok=0, voir="c_hitler",
         ex="The day Germany declared war on the United States: “the absolute elimination of the Jews…”, as the course quotes him."),
]

CREDITS = [
    "Content: the DNL History course (DNL History, H3 · introduction, with examples from Parts I to III, and reminders of chapters 1 and 2) as written on the site; animated maps of chapters 2 and 3 (site).",
    "Photograph: Hitler declares war on the United States, Reichstag, 11 December 1941 (unknown photographer, Wikimedia Commons, CC BY-SA 3.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
