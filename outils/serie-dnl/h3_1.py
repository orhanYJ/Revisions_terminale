"""DNL History · H3 « World War Two » — série vidéo, épisode 1 : « A world war » (l'introduction du chapitre).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h3_1 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H3.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte : 0 guerre-monde, 1 Mandchourie, 3 Chine 1937, 25 Barbarossa, 31 Pearl Harbor, 33 guerre
mondiale, 41 Nouvel Ordre européen fin 1942, 42 Stalingrad).
Contenu : l'introduction du chapitre dans le site (dnl/index.html, CHAPTERS.H3, section « Intro ») et le tableau des
divisions ; rien au-delà du cours, sauf ce qui est dit « outside the course ».
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
                 "Reichstag": "Rikes-tahg", "Wehrmacht": "Vair-markt", "Einsatzgruppen": "Ine-zats-groopen"}

# tableau des divisions du cours (introduction) : Alliés et Axe, 1940-1945
DIV_ALLIES = [(1940, 393), (1942, 397), (1943, 524), (1944, 575), (1945, 656)]
DIV_AXE = [(1940, 272), (1942, 350), (1943, 413), (1944, 349), (1945, 328)]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Sixty million dead. Battles from the Atlantic to the Pacific, from the Arctic to the deserts of Africa. "
        "The Second World War is the deadliest conflict in human history.",
        "{-q1}{q2}But when did it start? Most people would answer: on the first of September, 1939. "
        "In this chapter, Monsieur Ros gives you a different answer… and that answer is your first argument in an essay.",
        "{-q2}{-g0}{plan}This series covers the whole chapter, in seven episodes. {plan.1}Today: why this was a world war, "
        "and what the Nazis wanted to build with it. {plan.2}Then the fall of France, {plan.3}Britain alone, "
        "{plan.4}Operation Barbarossa, {plan.5}and the racial policy that led to genocide. "
        "{plan.6}After that, an episode only for the exam: essay and DBQ. {plan.7}And a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[0]),
        "q1": dict(type="question", t="60 million dead.", bande=True),
        "q2": dict(type="question", t="When did the war really begin?", bande=True),
        "plan": dict(type="liste", titre="H3 · World War Two, in seven episodes", items=[
            "A world war: dates, ideology, the New European Order", "The fall of France (Part I.1)",
            "Britain alone, supported by the US (Part I.2)", "Barbarossa: a war of annihilation (Part II)",
            "Towards the genocide (Part III)", "WWII at the exam: essay and DBQ", "Recap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 1", t="A world war",
                      sous="1931 – 1947 · an ideological war · the New European Order"),
    }),

    # ================================================================ I. 1931-1947
    dict(id="dates", chap="It began before 1939", fond="nuit", humeur="tension",
         retenir="For Robert Frank and Alya Aglan, a “world war” from 1937 to 1947; its chronology can be stretched from 1931 (Manchuria). 1937: Japan attacks southern China and the League does nothing.",
         beats=[
        "{g1}Many historians, among them Jay Winter and Robert Frank, have shown that the war began before 1939. "
        "Its chronology can be stretched from 1931… to 1947.",
        "{g1.1}Look east. September 1931: after the Mukden incident, the Japanese army conquers Manchuria, "
        "rich in coal and iron, and turns it into a puppet state. The League of Nations condemns it. Japan simply leaves the League.",
        "{g1.2}And 1937 is the turning point. Japan attacks southern China. China immediately appeals to the League of Nations for help… "
        "and the League proves incapable of regulating the tension. From there, the conflict spreads to a global scale.",
        "{-g1}{livre}Robert Frank and Alya Aglan even put the dates on the cover of their book, in 2015: "
        "La Guerre-monde, nineteen thirty-seven to nineteen forty-seven. The world war. {!The dates are an argument}The dates themselves are an argument.",
        "{-livre}{frise}So keep this chronology in mind. {frise.1}1931, Manchuria. {frise.2}1937, Japan attacks southern China. "
        "{frise.3}1939, Germany invades Poland: the war begins in Europe. {frise.4}1941, Barbarossa in June, Pearl Harbor in December: "
        "the war becomes truly global. {frise.5}1945, the end of the fighting. {frise.6}And 1947, the end of the world war for Frank and Aglan.",
        "{-frise}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is one way to say it. {rep1.1}The war did not start in Europe, but in Asia. "
        "{rep1.2}It started with Japanese aggression in Manchuria in 1931, and above all against China in 1937. "
        "{rep1.3}And the League of Nations' failure to react let it spread to the whole world.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[1, 3]),
        "livre": dict(type="mot", t="1937 – 1947", g="Robert Frank & Alya Aglan, La Guerre-monde (2015)", y=250, taille=110),
        "frise": dict(type="frise", items=[
            dict(nom="Manchuria", d=1931, q="Japan seizes it"), dict(nom="China", d=1937, q="the turning point"),
            dict(nom="Poland", d=1939, q="war in Europe"), dict(nom="Global war", d=1941, q="Barbarossa · Pearl Harbor"),
            dict(nom="Fighting ends", d=1945, q="Europe, then Asia"), dict(nom="War ends", d=1947, q="for Frank & Aglan")]),
        "pa1": dict(type="pause", t="In one sentence: why can we say the war began before 1939?",
                    sous="Pause the video, write your sentence, then play on to compare."),
        "rep1": dict(type="liste", titre="A model answer", items=[
            "It began in Asia, not in Europe.", "Japanese aggression: Manchuria (1931), southern China (1937).",
            "The League of Nations' failure let it spread to the world."], x=170, y=150, w=940),
    }),

    # ================================================================ II. une guerre idéologique
    dict(id="ideologie", chap="An ideological war", fond="guerre", humeur="tension",
         retenir="Not only defeating armies, but destroying the enemy's civilisation: an ideological war, about 60 million dead.",
         beats=[
        "{q3}Why was this war so deadly? Because it was not like other wars.",
        "{-q3}{def1}In other wars, the aim is to defeat the enemy's armies, then to negotiate. "
        "Here, the aim was to destroy the enemy's civilisation. It was an {!ideological war}ideological war, "
        "in which no side would give up until death.",
        "{-def1}{photo}Monsieur Ros opens the chapter with a photograph that says this better than any definition. "
        "Einsatzgruppen killers, around 1941 or 1942, shooting men standing in a pit. A photograph probably taken by one of the killers. "
        "We will come back to these mobile killing squads in episode five.",
        "{-photo}{n60}The final toll is about sixty million dead. In the course's words, "
        "the Second World War is {!the ideological crucible}the ideological crucible of the twentieth century: "
        "the moment when the great ideologies of the century, fascism, Nazism, communism, liberal democracy, met… in total war.",
        "{-n60}{gr}One more document from the introduction: the number of divisions on each side. {gr.1}The Allies, in blue. "
        "{gr.2}The Axis, in red. In 1940, the Axis is far from dominant in numbers, but it wins anyway, thanks to surprise and the Blitzkrieg. "
        "{gr.3}After 1942, the gap opens and never closes: 656 Allied divisions in 1945, against 328 for the Axis.",
        "{-gr}{urss}And look at who carries the weight. The Soviet Union alone goes from 200 divisions in 1940 to 488 in 1945. "
        "Germany peaks at 347, in 1944. {!numbers}A war of numbers, that the Axis could not win in the long run.",
    ], vis={
        "q3": dict(type="question", t="Why was this war so deadly?"),
        "def1": dict(type="def", cles=["armies", "civilisation"], terme="An ideological war",
                     t="The aim is not only to defeat the enemy's armies, but to destroy its civilisation.",
                     etape="No side gives up until death · no limits on violence", x=170, y=200, w=940),
        "photo": dict(type="note", cles=["Einsatzgruppen", "killers"], terme="The first document of the chapter",
                      t="Einsatzgruppen killers shooting men standing in a pit, around 1941–1942.",
                      etape="A photograph probably taken by one of the killers (described here, not shown).", x=170, y=200, w=940),
        "n60": dict(type="mot", t="≈ 60 million dead", g="“the ideological crucible of the twentieth century”", y=250, taille=96),
        "gr": dict(type="graphe", titre="Divisions on each side, 1940–1945 (course)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1939.5, 1945.5], y=[0, 700], gx=[1940, 1942, 1943, 1944, 1945], gy=[200, 400, 600], lx="year", ly="divisions"),
                   el=[dict(type="courbe", pts=[list(p) for p in DIV_ALLIES], c="el", lbl="Allies", lp=[1944.6, 690], dur=2.0),
                       dict(type="courbe", pts=[list(p) for p in DIV_AXE], c="ca", lbl="Axis", lp=[1944.7, 280], dur=2.0),
                       dict(type="points", pts=[[1945, 656], [1945, 328]], c="sa", lbl="656 against 328", lp=[1943.6, 520])]),
        "urss": dict(type="cols", g="USSR", gq="200 divisions in 1940 → 488 in 1945", d="Germany", dq="peaks at 347, in 1944",
                     vs="vs"),
    }),

    # ================================================================ III. le Nouvel Ordre européen
    dict(id="ordre", chap="The New European Order", fond="nuit", humeur="tension",
         retenir="Key term. The New European Order: Nazi rule over Europe, presented as saving European civilisation. Five driving forces.",
         beats=[
        "{g2}For the Nazis, war and conquest were an opportunity. {g2.1}The opportunity to build a grandiose political and economic apparatus "
        "that would entrench their domination of Europe. Look at the map at the end of 1942: from the Atlantic to the Volga, "
        "from Norway to the Mediterranean.",
        "{-g2}{def2}This is a {!key term}key term of the chapter: the {!New European Order}New European Order. "
        "Nazi rule over the continent, which its supporters presented as saving European civilisation from collapse.",
        "{-def2}{forces}The course gives it five driving forces. Learn them: they are a ready-made plan. "
        "{forces.1}One: Europe as a racial entity, and racial purification through genocide. "
        "{forces.2}Two: the quest for Lebensraum, living space, in the East. "
        "{forces.3}Three: the crusade against communism. "
        "{forces.4}Four: the Grossraum, a single European economic unit, serving Germany. "
        "{forces.5}And five: supplying Germany with the people, the materials and the money that total war requires.",
        "{-forces}{reich}And Hitler himself said it, before the Reichstag, on the eleventh of December 1941, "
        "the day Germany declared war on the United States.",
        ("C", "the absolute elimination of the Jews, the establishment of the supremacy of the German people, "
              "and the creation of a real community of nations under German leadership", "c_hitler"),
        "{-c_hitler}{-reich}{lien}Three goals in one sentence: racial, national, European. Keep this quotation: "
        "it fits the opening of almost any essay on the New European Order.",
        "{-lien}{g3}So the chapter assesses this order through three cases. {g3.1}In the West, the invasion and occupation of France. "
        "{g3.2}In the East, the quest for Lebensraum and the war against the Soviet Union. "
        "{g3.3}And everywhere, the racial policy that led to genocide.",
    ], vis={
        "g2": dict(type="globe", code="H3", sc=[33, 41]),
        "def2": dict(type="def", cles=["rule", "saving"], terme="Key term · New European Order",
                     t="Nazi rule over Europe, presented by its supporters as saving European civilisation from collapse.",
                     etape="A political and economic apparatus to entrench German domination", x=170, y=200, w=940),
        "forces": dict(type="liste", titre="The five driving forces", cles=["racial", "Lebensraum", "communism", "Grossraum", "total"], items=[
            "Europe as a racial entity: purification through genocide", "Lebensraum: living space in the East",
            "A crusade against communism", "The Grossraum: one economic unit serving Germany",
            "Supplying total war: people, materials, money"], x=170, y=110, w=940),
        "reich": dict(type="tableau", img="h3-reichstag", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                      legende="Hitler declares war on the United States, Reichstag, 11 December 1941 (Wikimedia Commons, CC BY-SA 3.0)"),
        "c_hitler": dict(type="cit", a="Adolf Hitler", o="speech to the Reichstag, 11 December 1941", x=200, y=170, w=880),
        "lien": dict(type="cols", g="Racial", gq="eliminate the Jews", d="National · European", dq="German supremacy · a community under German leadership",
                     vs="+"),
        "g3": dict(type="globe", code="H3", sc=[16, 25, 32]),
    }),

    # ================================================================ IV. pour l'essay
    dict(id="essay", chap="Using it in an essay", fond="aube", humeur="calme",
         retenir="Key issue: “Assess the aims of the New European Order.” Define the key term, then judge the five forces against reality.",
         beats=[
        "{ki}The key issue of this chapter is exactly this: {!Assess the aims}assess the aims of the New European Order.",
        "{-ki}{plan2}Here is how the introduction helps you. {plan2.1}Start with the definition of the key term, in one sentence. "
        "{plan2.2}Give the chronology: a world war from 1931 or 1937, not just 1939. "
        "{plan2.3}Announce the aims with the five driving forces: racial, territorial, ideological, economic, and total war. "
        "{plan2.4}Then use the three cases of the chapter as your evidence: France in the West, Barbarossa in the East, the genocide.",
        "{-plan2}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}A possible opening sentence. Between 1939 and 1942, Nazi Germany built a New European Order: "
        "a continent ruled by Germany, organised by race, colonised in the East and drained for total war.",
        "Short, precise, and it already contains your plan.",
    ], vis={
        "ki": dict(type="question", t="Key issue: assess the aims of the New European Order."),
        "plan2": dict(type="liste", titre="From the introduction to your essay", items=[
            "Define the key term in one sentence", "Date it: a world war from 1931 / 1937", "Announce the five driving forces",
            "Evidence: France · Barbarossa · the genocide"], x=170, y=130, w=940),
        "pa2": dict(type="pause", t="Write the first sentence of an essay on the aims of the New European Order.",
                    sous="Pause the video, write it, then play on for a model."),
        "rep2": dict(type="note", cles=["race", "East", "total"], terme="A model opening",
                     t="Between 1939 and 1942, Nazi Germany built a New European Order: a continent ruled by Germany, organised by race, colonised in the East and drained for total war.",
                     etape="One sentence: definition, dates and plan.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}A world war, which began in Asia, in 1931 and 1937. "
        "{carte.2}An ideological war, about sixty million dead, the crucible of the century. "
        "{carte.3}A war of numbers, that the Allies won after 1942. "
        "{carte.4}And the key term: the New European Order, with its five driving forces.",
        "{-carte}{fin}Next episode: the fall of France. Six weeks in May and June 1940, an armistice, a country cut in two… "
        "and a regime that chose collaboration.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="A WORLD WAR", branches=[
            dict(t="Dates", items=["1931 Manchuria", "1937 China", "1937–1947: Frank & Aglan"]),
            dict(t="Ideology", items=["destroy a civilisation", "≈ 60 million dead"]),
            dict(t="Numbers", items=["656 / 328 divisions in 1945", "USSR: 488"]),
            dict(t="New European Order", items=["race · Lebensraum", "anti-communism", "Grossraum · total war"])]),
        "fin": dict(type="mot", t="Next: the fall of France", g="Episode 2 · May – June 1940", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Why do historians such as Robert Frank date the war from 1937?",
         r=["Japan attacked southern China and the League proved powerless", "Germany invaded Poland",
            "Italy invaded Ethiopia", "Germany declared war on the United States"], ok=0, voir="g1",
         ex="Their book is titled La Guerre-monde 1937–1947 (2015); its chronology can even start in 1931, with Manchuria."),
    dict(q="What makes the Second World War an ideological war?",
         r=["The aim was to destroy the enemy's civilisation, not only its armies", "It was fought only by dictatorships",
            "It was fought only in Europe", "It ended with a negotiated peace"], ok=0, voir="def1",
         ex="No side would give up until death: hence a toll of about 60 million dead."),
    dict(q="In 1945, how many divisions did the Allies and the Axis have, according to the course table?",
         r=["656 against 328", "328 against 656", "393 against 272", "488 against 347"], ok=0, voir="gr",
         ex="393 against 272 is 1940; 488 is the USSR alone in 1945, 347 Germany's peak in 1944."),
    dict(q="What is the New European Order?",
         r=["Nazi rule over Europe, presented as saving its civilisation", "The Allied plan for peace after 1945",
            "The League of Nations reformed in 1940", "The Vichy constitution"], ok=0, voir="def2",
         ex="It is a key term of the chapter: define it, then give its five driving forces."),
    dict(q="Which is NOT one of the five driving forces of the New European Order?",
         r=["Restoring the European monarchies", "The quest for Lebensraum in the East", "The crusade against communism",
            "Supplying Germany for total war"], ok=0, voir="forces",
         ex="The five: racial entity and genocide, Lebensraum, anti-communism, the Grossraum, supplying total war."),
    dict(q="When did Hitler define the “new order” before the Reichstag?",
         r=["11 December 1941", "1 September 1939", "22 June 1941", "30 January 1933"], ok=0, voir="c_hitler",
         ex="The day Germany declared war on the United States: “the absolute elimination of the Jews…”."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H3 · introduction) as written on the site; animated map of the chapter (site).",
    "Photograph: Hitler declares war on the United States, Reichstag, 11 December 1941 (unknown photographer, Wikimedia Commons, CC BY-SA 3.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
