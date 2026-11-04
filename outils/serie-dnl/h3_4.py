"""DNL History · H3 « World War Two » — série vidéo, épisode 4 : « Barbarossa: a war of annihilation » (parties II.1 et II.2).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h3_4 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H3.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H3 : 4 pacte · 7 partage de la Pologne · 19 annexions soviétiques de 1940 · 24 pourquoi l'URSS · 25 Barbarossa ·
       26 avance et terre brûlée · 27 Einsatzgruppen · 28 anéantissement · 29 Staline, 7 nov. 1941 · 30 arrêtés devant
       Leningrad et Moscou · 36 seconde offensive (été 1942) · 38 Stalingrad · 40 encerclement · 42 capitulation de Paulus
Contenu : CHAPTERS.H3 du site (dnl/index.html), sections II.1 (4 idées) et II.2 (8 idées), schémas h3forces (H3_FORCES)
et h3ws3 (Worksheet 3 : sources et réponses ; réponses 1, 2, 3 et 5 « proposées par le site », réponse 4 donnée par le
cours), points de H3Check (Stalingrad objectif de 1942 et non de 1941 ; purges surtout en 1937-38 ; deux chiffres pour
les prisonniers soviétiques : citer le document utilisé). Tukhachevsky : exemple ajouté hors cours, dit comme tel.
Le DBQ porte sur la source 6 (lettres d'un soldat allemand), l'épisode 6 traitant déjà Reichenau et Staline.
Plan de la série H3 : 1 A world war · 2 The fall of France · 3 Britain alone · 4 Barbarossa · 5 Towards the genocide ·
6 WWII at the exam (essay and DBQ) · 7 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-4"
NOTION = "World War Two"
NUM = 4
TITRE = "Barbarossa: a war of annihilation"
SUIVANT = "Episode 5 · Towards the genocide"
PRONONCIATION = {"Grossraum": "Gross-rowm", "Lebensraum": "Lay-bens-rowm", "Wehrmacht": "Vair-markt",
                 "Einsatzgruppen": "Ine-zats-groopen", "Übermensch": "Oober-mensh", "Untermensch": "Oonter-mensh",
                 "Untermenschen": "Oonter-menshen", "Vernichtungskrieg": "Fair-nikh-toongs-kreeg",
                 "Reichenau": "Rike-en-ow", "Paulus": "Pow-loos", "Jodl": "Yoh-dl", "Białystok": "Bya-wiss-tok",
                 "Lvov": "Lvoff", "Bukovina": "Boo-ko-veena", "Tukhachevsky": "Too-ka-chef-ski", "Birkenau": "Beer-ken-ow",
                 "Mein Kampf": "Mine Kampf", "Ribbentrop": "Ribben-trop", "Molotov": "Mollo-toff"}


def barres(cats, cG, cS, lp_leg=124):
    """Graphique en barres : pour chaque catégorie (nom, Allemands, Soviétiques), le texte puis deux barres.
    Les barres sont des droites épaisses (34 px) ; la hauteur est rapportée au plus grand des deux (100), comme sur
    le site ; les extrémités arrondies sont rentrées de 5,5 unités pour que la barre parte de l'axe. Quand les deux
    barres ont presque la même hauteur, l'étiquette de la plus haute monte pour ne pas chevaucher l'autre."""
    el = [dict(type="texte", x=1.0, y=lp_leg, t="Germans", c=cG), dict(type="texte", x=2.0, y=lp_leg, t="Soviets", c=cS)]
    for i, (nom, g, s) in enumerate(cats, start=1):
        m = max(g, s)
        hg, hs = 100 * g / m, 100 * s / m
        bas = min(hg, hs) + 8
        el.append(dict(type="texte", x=i, y=-9, t=nom, c="iv"))
        for dx, v, h_, c in ((-0.17, g, hg, cG), (0.17, s, hs, cS)):
            lab = h_ + 8 if h_ == min(hg, hs) else max(h_ + 8, bas + 12)
            el.append(dict(type="droite", pts=[[i + dx, 5.5], [i + dx, max(6, h_ - 5.5)]], c=c, ep=34, dur=1.0,
                           lbl=f"{v:,}", lp=[i + dx, lab]))
    return el


AX_BARRES = dict(x=[0.35, 4.65], y=[0, 130], gx=[], gy=[], lx="", ly="")
FORCES = [("Men", 1011500, 1143500), ("Guns", 10290, 13541), ("Tanks", 675, 894), ("Planes", 1216, 1115)]
PERTES = [("Casualties", 760000, 1130000), ("Tanks lost", 500, 4341), ("Aircraft lost", 900, 2769)]

ANS = [1940, 1942, 1943, 1944, 1945]
DIV_URSS = list(zip(ANS, [200, 250, 350, 400, 488]))
DIV_ALL = list(zip(ANS, [189, 261, 327, 347, 319]))
DIV_AXE = list(zip(ANS, [272, 350, 413, 349, 328]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}The twenty-second of June, 1941. On a front running from the Baltic to the Black Sea, "
        "the German army invades the Soviet Union. Its code name: Operation Barbarossa.",
        "{q1}In the first two hundred days, five million people die. A thousand every hour, most of them civilians.",
        "{-q1}{q2}Why did Hitler break his pact with Stalin? And why did this war become, on both sides, a war without mercy?",
        "{-q2}{-g0}{plan}Today, part two of the chapter. {plan.1}First, the story on the map. "
        "{plan.2}Then German plans for Eastern Europe. {plan.3}Then Barbarossa, case study number two. "
        "{plan.4}Then Stalingrad and Worksheet three. {plan.5}And the exam: an essay paragraph and a DBQ.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[25]),
        "q1": dict(type="question", t="5 million dead in 200 days.", bande=True),
        "q2": dict(type="question", t="Why a war without mercy?", bande=True),
        "plan": dict(type="liste", titre="Episode 4 · the plan", items=[
            "The war in the East on the map, 1939–1943", "II.1 · German plans for Eastern Europe: three reasons",
            "II.2 · Barbarossa: a war of annihilation", "Stalingrad, the turning point · Worksheet 3",
            "At the exam: an essay paragraph and a DBQ"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 4", t="Barbarossa",
                      sous="A war of annihilation · 1939 – 1943 · Part II of the course"),
    }),

    # ================================================================ la carte : 1939-1941
    dict(id="carte1", chap="On the map: 1939 – 1941", fond="nuit", humeur="tension",
         retenir="Aug. 1939 the pact · Sept. 1939 Poland partitioned · summer 1940 Soviet annexations · 22 June 1941 Barbarossa · Dec. 1941 stopped before Leningrad and Moscow.",
         beats=[
        "{g1}{g1.1}August 1939. Nazi Germany and the Soviet Union, sworn ideological enemies, sign a pact. "
        "Hitler secures the neutrality of the Soviet Union, and in secret the two powers plan to carve up Poland. "
        "Germany feels ready to conquer its living space in the East.",
        "{g1.2}On the first of September, Germany invades Poland. On the seventeenth, the Red Army enters eastern Poland. "
        "Within a month, Poland is defeated and partitioned, on either side of a demarcation line between Warsaw and Białystok.",
        "{g1.3}In the summer of 1940, while Germany crushes the West, the Soviet Union takes its share. "
        "It annexes Estonia, Latvia and Lithuania, and it takes Northern Bukovina and Bessarabia from Romania.",
        "{-g1}{g2}{g2.1}Then, on the twenty-second of June 1941, Hitler breaks the pact. Operation Barbarossa: three German thrusts, "
        "on a front from the Baltic to the Black Sea. In the north towards Leningrad, in the centre towards Moscow, "
        "in the south through Ukraine, towards Kiev and Rostov.",
        "{g2.2}From June to December 1941, the German army advances deep into the Soviet Union. The Red Army retreats. "
        "And ahead of the invader, the peasants burn their crops, drive their cattle away and destroy their villages. Scorched earth.",
        "{g2.3}Behind the army come the Einsatzgruppen, the mobile killing squads that shoot the Jews: that will be episode five. "
        "{g2.4}And on this front, the rules of war disappear. Prisoners and civilians are murdered as a matter of routine. "
        "This is already a war of annihilation.",
        "{g2.5}The seventh of November, in Moscow, with the Germans still advancing on the capital, Stalin answers: "
        "if the Germans want a war of annihilation, they will get it. "
        "{g2.6}And in December 1941, the Germans are stopped, before Leningrad, now besieged, and before Moscow. "
        "The lightning war has failed: the war in the East will be long.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[4, 7, 19]),
        "g2": dict(type="globe", code="H3", sc=[25, 26, 27, 28, 29, 30]),
    }),

    # ================================================================ la carte : 1942-1943
    dict(id="carte2", chap="On the map: 1942 – 1943", fond="nuit", humeur="tension",
         retenir="Summer 1942: the second offensive, towards Stalingrad and the Caucasus · Nov. 1942: the German army encircled · 2 Feb. 1943: Paulus capitulates.",
         beats=[
        "{g3}{g3.1}Summer 1942. Stopped before Moscow, the Germans strike in the south: a second offensive, "
        "towards the Volga and the oil of the Caucasus. On the twenty-eighth of July, Stalin's Order number 227 demands: "
        "not one step back.",
        "{g3.2}From August, the Germans reach Stalingrad, on the Volga. The Russians defend the city at all costs, "
        "street by street, factory by factory. Here, the German advance reaches its furthest point.",
        "{g3.3}November 1942. The Red Army now lines up more men, more guns and more tanks than the Germans. "
        "And that same month, the Soviet counter-attack closes around the German army: it is encircled.",
        "{g3.4}The second of February 1943. Paulus, the German commander, capitulates. Ninety-five thousand German soldiers "
        "are taken prisoner. A resounding defeat for the Wehrmacht: the turning point of the war.",
        "{-g3}{fr1}So, six dates to know by heart. {fr1.1}August 1939, the pact. {fr1.2}The twenty-second of June 1941, Barbarossa. "
        "{fr1.3}December 1941, stopped before Moscow. {fr1.4}Summer 1942, the second offensive. "
        "{fr1.5}November 1942, the encirclement. {fr1.6}And the second of February 1943, Paulus capitulates.",
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[36, 38, 40, 42]),
        "fr1": dict(type="frise", items=[
            dict(nom="The pact", d=1939, q="August"), dict(nom="Barbarossa", d=1941, q="22 June"),
            dict(nom="Moscow", d=1941, q="December: stopped"), dict(nom="Second offensive", d=1942, q="summer"),
            dict(nom="Encirclement", d=1942, q="November"), dict(nom="Capitulation", d=1943, q="2 February")]),
    }),

    # ================================================================ II.1, idée 1 : le pacte
    dict(id="pacte", chap="II.1 · The pact opens the road to the East", fond="nuit", humeur="tension",
         retenir="The pact (Aug. 1939): Soviet neutrality + a secret plan to carve up Poland. Poland partitioned (17 Sept. 1939). The USSR annexes the Baltic states, Northern Bukovina and Bessarabia (1940).",
         beats=[
        "{def3}Now the course, idea by idea. Part two point one: German plans for Eastern Europe. "
        "Idea one: the Nazi-Soviet pact {!opened the road to the East}opened the road to the East. "
        "Hitler secured the neutrality of the Soviet Union, and the two powers secretly planned to share Poland. "
        "{def3.1}So Germany felt ready to conquer its {!Lebensraum}Lebensraum, the living space in the East announced in Mein Kampf.",
        "{-def3}{sl}Monsieur Ros's slide shows it in three images. {sl.1}Stalin and Ribbentrop shaking hands after the signing. "
        "{sl.2}The German invasion routes of the first of September 1939. "
        "{sl.3}And Eastern Europe after the pact: the German-Soviet line runs between Warsaw and Białystok, "
        "and between Lublin and Lvov. {sl.4}On that map, the Soviet annexations of 1940: Estonia, Latvia and Lithuania, "
        "and Northern Bukovina and Bessarabia, taken from Romania.",
        "{-sl}{lec2}For your essay: the two dictatorships share Eastern Europe. But for Hitler, it is only a step: "
        "the living space he wants in the East is Soviet land.",
    ], vis={
        "def3": dict(type="def", cles=["neutrality", "secret", "Poland"], terme="The Nazi-Soviet pact · August 1939",
                     t="Hitler secures the neutrality of the USSR; in secret, the two powers plan to carve up Poland.",
                     etape="Next step: the Lebensraum, the living space in the East announced in Mein Kampf", x=170, y=200, w=940),
        "sl": dict(type="liste", titre="M. Ros's slide", items=[
            "Stalin and Ribbentrop shake hands after the signing", "The German invasion routes, 1 September 1939",
            "The German-Soviet line: Warsaw–Białystok, Lublin–Lvov", "1940: the Baltic states, N. Bukovina, Bessarabia annexed by the USSR"],
            x=150, y=130, w=980),
        "lec2": dict(type="note", terme="For the essay", cles=["step", "Soviet"],
                     t="The pact is only a step: the living space Hitler wants in the East is Soviet land.",
                     etape="1939–1941: the two dictatorships share Eastern Europe", x=170, y=200, w=940),
    }),

    # ================================================================ II.1, idée 2 : la raison économique
    dict(id="raisons", chap="II.1 · Why invade the USSR? The economic reason", fond="nuit", humeur="tension",
         retenir="Economic reason: the Grossraum, a larger, self-sufficient Reich · Germanisation: German settlers, Slavs enslaved · resources (farmland, minerals, oil) for autarky and a long war. Example: Stalingrad and Caucasus oil.",
         beats=[
        "{g4}{g4.1}So why did Hitler invade the Soviet Union? The course gives three reasons, and they are the backbone "
        "of any essay on this part: {!economic, ideological, racial}an economic reason, an ideological reason, and a racial reason. "
        "Look at the map: Ukraine, the Caucasus, Moscow. Everything Germany wanted was there.",
        "{-g4}{eco}Reason one, the economic reason. {eco.1}Hitler wanted a {!Grossraum}Grossraum, a greater space: "
        "a larger Third Reich, able to live on its own resources. "
        "{eco.2}In the East, German settlers would be installed, and the Slavic populations enslaved: "
        "this was the plan of {!Germanisation}Germanisation of the East. "
        "{eco.3}And the natural resources of the Soviet Union, its farmland, its minerals, its oil, were an economic necessity: "
        "to achieve autarky, and to fight a long war.",
        "{eco.4}The example comes from Worksheet three. Stalingrad mattered because it was a major industrial and transport hub on the Volga, "
        "which ensured Soviet access to the oil of the Caucasus. Oil that the German war economy needed.",
    ], vis={
        "g4": dict(type="globe", code="H3", sc=[24]),
        "eco": dict(type="liste", titre="1 · The economic reason", cles=["Grossraum", "Germanisation", "resources"], items=[
            "The Grossraum: a larger, self-sufficient Third Reich", "Germanisation: German settlers, Slavs enslaved",
            "The resources: farmland, minerals, oil → autarky, a long war", "Example: Stalingrad, the Volga, Caucasus oil (Worksheet 3)"],
            x=150, y=130, w=980),
    }),

    # ================================================================ II.1, idées 3 et 4 : idéologique et raciale
    dict(id="raisons2", chap="II.1 · The ideological and the racial reasons", fond="guerre", humeur="tension",
         retenir="Ideological: the crusade against “Jewish Bolshevism” (Jodl's order, May 1941: commissars “dispatched by firearms”). Racial: Übermensch against Untermensch (Reichenau's Severity Order, 10 Oct. 1941).",
         beats=[
        "{def6}Reason two, the ideological reason. Two populations were seen as hostile and dangerous to German rule in the East: "
        "the communist leaders, and the Jews. Nazi rhetoric called the Soviet Union a {!Jewish Bolshevik}Jewish Bolshevik regime, "
        "merging the political enemy and the racial enemy into one. "
        "{def6.1}So this war was not only a conquest. It was a war against a worldview.",
        "{-def6}The example: Source one of Worksheet three, an order signed by General Alfred Jodl in May 1941. "
        "It calls the political commissars, the communist leaders,",
        ("C", "the originators of barbaric, Asiatic methods of warfare", "c_jodl"),
        "{-c_jodl}{jodl}When captured, they must be dispatched by firearms, as a matter of routine. Shot on the spot.",
        "{-jodl}{def7}Reason three, the racial reason. The Nazis were convinced that they belonged to the Aryan {!Übermensch}Übermensch, "
        "the superior man, above the Slavic Untermensch, the inferior man. "
        "The Slavs were to be enslaved, or driven out to make room for German settlers. And the Jews were to be eliminated. "
        "{def7.1}This racial hierarchy, seen in chapter two, turns the Eastern campaign into a war of destruction from the start.",
        "{-def7}The example: Source two, the Severity Order of Field Marshal Walther von Reichenau, the tenth of October 1941. It calls for",
        ("C", "the extermination of the Asiatic influence in European civilisation", "c_rei1"),
        "{-c_rei1}and for severe but just retribution against what it calls",
        ("C", "the subhuman species of Jewry", "c_rei2"),
        "{-c_rei2}{tab3}So here is the table to copy: three reasons, one example each. "
        "{tab3.1}Economic: Stalingrad and Caucasus oil. {tab3.2}Ideological: Jodl's order. {tab3.3}Racial: Reichenau's Severity Order. "
        "And notice the link: the words Jewish Bolshevism already mix the ideological enemy and the racial enemy.",
        ("P", 4.0),
    ], vis={
        "def6": dict(type="def", cles=["communist", "Jews", "one"], terme="2 · The ideological reason: “Jewish Bolshevism”",
                     t="Communist leaders and Jews: the political enemy and the racial enemy merged into one.",
                     etape="Not only a conquest: a war against a worldview", x=170, y=200, w=940),
        "c_jodl": dict(type="cit", a="General Alfred Jodl", o="order on the political commissars, May 1941 (Worksheet 3, Source 1)", x=200, y=190, w=880),
        "jodl": dict(type="note", terme="Source 1 · Jodl's order, May 1941", cles=["firearms", "routine"],
                     t="Captured political commissars are to be “dispatched by firearms”, as a matter of routine.",
                     etape="Shot on the spot: the laws of war no longer apply", x=170, y=200, w=940),
        "def7": dict(type="def", cles=["Übermensch", "Untermensch", "eliminated"], terme="3 · The racial reason",
                     t="The Aryan “Übermensch” above the Slavic “Untermensch”: Slavs enslaved or driven out, Jews eliminated.",
                     etape="A racial hierarchy (chapter 2) → a war of destruction from the start", x=170, y=200, w=940),
        "c_rei1": dict(type="cit", a="Field Marshal Walther von Reichenau", o="Severity Order, 10 October 1941 (Worksheet 3, Source 2)", x=200, y=190, w=880),
        "c_rei2": dict(type="cit", a="Field Marshal Walther von Reichenau", o="Severity Order, 10 October 1941 (Worksheet 3, Source 2)", x=200, y=210, w=880),
        "tab3": dict(type="liste", titre="Why invade the USSR? · reason → example", items=[
            "Economic: Grossraum, Germanisation, resources → Stalingrad, Caucasus oil",
            "Ideological: the crusade against “Jewish Bolshevism” → Jodl's order, May 1941",
            "Racial: Übermensch / Untermensch → Reichenau's Severity Order, 10 Oct. 1941"], x=130, y=150, w=1020),
    }),

    # ================================================================ II.2, idées 1 et 2 : Barbarossa
    dict(id="barbarossa", chap="II.2 · Operation Barbarossa", fond="guerre", humeur="tension",
         retenir="22 June 1941: Barbarossa, a crusade against communism. Three thrusts: Leningrad · Moscow · Kiev and Rostov, with Germany's allies. Stalled before Leningrad and Moscow: 200 days, 5 million dead.",
         beats=[
        "{g5}{g5.1}Part two point two: Operation Barbarossa, a war of annihilation. Case study number two. "
        "Idea one. On the twenty-second of June 1941, Hitler breaks the Molotov-Ribbentrop pact. "
        "The Wehrmacht sees this war as a {!crusade against communism}crusade against communism.",
        "{thr}Idea two: three thrusts across an immense front, from the Baltic to the Black Sea. "
        "{thr.1}In the north, through the Baltic states, towards Leningrad. {thr.2}In the centre, through Minsk and Smolensk, towards Moscow. "
        "{thr.3}In the south, through Ukraine and Kiev, towards Rostov. "
        "{thr.4}And Germany does not fight alone: Monsieur Ros's map labels Finland, Romania, Hungary, Slovakia, Italy and Croatia as its allies.",
        "{-thr}{-g5}{att}Watch out. A second course map, Operation Barbarossa, stars Stalingrad as one of the three objectives. "
        "But in 1941, the southern thrust aims at Ukraine, Kiev and Rostov. "
        "{att.1}Stalingrad and the Caucasus are the targets of the second offensive, in the summer of 1942. In an essay, write it that way.",
        "{-att}{bil2}Until December 1941, the Germans advance deep into the Soviet Union, but stiffening Red Army resistance "
        "stops them before Leningrad and Moscow. The Blitzkrieg that had won in six weeks in France fails in the immensity of Russia. "
        "And the toll of these first two hundred days: five million dead. On average, {!a thousand an hour}a thousand people killed every hour, "
        "mostly civilians.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[25]),
        "thr": dict(type="liste", titre="Three thrusts, June 1941", petit=True, bande=True, x=60, y=130, w=560, items=[
            "North: Baltic states → Leningrad", "Centre: Minsk, Smolensk → Moscow", "South: Ukraine, Kiev → Rostov",
            "Allies: Finland, Romania, Hungary, Slovakia, Italy, Croatia"]),
        "att": dict(type="note", terme="Watch out · a course map", cles=["Rostov", "second"],
                    t="1941: Leningrad, Moscow, Kiev and Rostov. Stalingrad and the Caucasus: the second offensive, summer 1942.",
                    etape="The map “Operation Barbarossa” stars Stalingrad among the objectives: not in 1941", x=170, y=200, w=940),
        "bil2": dict(type="mot", t="5 million dead", g="200 days of war · a thousand an hour, mostly civilians", y=250, taille=100),
    }),

    # ================================================================ II.2, idée 3 : du côté soviétique
    dict(id="sovietique", chap="II.2 · The Soviet side", fond="nuit", humeur="tension",
         retenir="The Red Army, “beheaded” by the Great Purges (mainly 1937–38), retreated but did not collapse. Scorched earth: crops burnt, cattle driven away, villages destroyed.",
         beats=[
        "{sov}Idea three: what happens on the Soviet side? Two things. {sov.g}First, a weakened army. The Red Army is disorganised, "
        "{!beheaded}beheaded, says the course, by the Great Purges, which destroyed much of its officer corps. "
        "An example from outside the course: Marshal Tukhachevsky, its leading strategist, was shot in June 1937, "
        "and thousands of officers were dismissed or arrested.",
        "{sov.d}Second, a population that leaves nothing behind. Russian peasants flee ahead of the German troops, "
        "burning their harvested crops, driving their cattle away and destroying the buildings of their villages: "
        "the {!scorched earth}scorched-earth policy. The invader finds nothing to live on.",
        "{-sov}{dat}One date to correct: the course places these purges in 1938. The great purge of the army ran mainly "
        "in 1937 and 1938, as chapter two says.",
        "{-dat}{res}And the key point of this idea: the Red Army retreats… but it does not collapse. "
        "Its resistance stops the Germans before Leningrad and Moscow.",
    ], vis={
        "sov": dict(type="cols", g="A weakened army", gq="“beheaded” by the Great Purges: much of its officer corps destroyed",
                    d="Scorched earth", dq="crops burnt, cattle driven away, villages destroyed", vs="+",
                    repere="Tukhachevsky shot, June 1937 (outside the course)"),
        "dat": dict(type="note", terme="Watch out · a date", cles=["purge", "mainly"],
                    t="The great purge of the army: mainly 1937–38 (the course says 1938).",
                    etape="Chapter 2 gives 1937–38", x=170, y=200, w=940),
        "res": dict(type="question", t="It retreated… but it did not collapse."),
    }),

    # ================================================================ II.2, idée 4 : la réponse de Staline
    dict(id="staline", chap="II.2 · Stalin's answer", fond="guerre", humeur="tension",
         retenir="7 Nov. 1941, Moscow: Stalin turns the Nazis' own word, Vernichtungskrieg, against them: destroy the invaders “to the last man”. On both sides, a war without mercy.",
         beats=[
        "{g6}{g6.1}Idea four: Stalin's answer. The seventh of November 1941, in Moscow. The German troops are still advancing on the capital. "
        "Stalin takes up the Nazis' own word, {!Vernichtungskrieg}Vernichtungskrieg, war of annihilation… and turns it against them.",
        "{-g6}",
        ("C", "Well, if the Germans want a war of annihilation, they will get it.", "c_st1"),
        "{-c_st1}In the lesson notes, this sentence is followed by stormy, prolonged applause. Then: the task is",
        ("C", "to destroy all invading Germans occupying the territory of our homeland to the last man. No mercy to the German occupiers!", "c_st2"),
        "{-c_st2}{miroir}All the peoples of the Soviet Union must now destroy the invaders to the last man. {miroir.g}On the German side, the enemy is subhuman: Jodl, Reichenau. "
        "{miroir.d}On the Soviet side: no mercy. {!Annihilation for annihilation}Annihilation for annihilation. "
        "On both sides, the war in the East is declared a war without mercy: that is why it is called a war of annihilation.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[29]),
        "c_st1": dict(type="cit", a="Joseph Stalin", o="speech, Moscow, 7 November 1941", x=200, y=210, w=880),
        "c_st2": dict(type="cit", a="Joseph Stalin", o="speech, Moscow, 7 November 1941", x=200, y=170, w=880),
        "miroir": dict(type="cols", g="Germany", gq="the enemy as “subhuman”: Jodl's order, Reichenau's Severity Order",
                       d="USSR", dq="“No mercy to the German occupiers!” Stalin, 7 Nov. 1941", vs="=",
                       repere="Annihilation for annihilation"),
    }),

    # ================================================================ II.2, idée 5 : une guerre d'anéantissement
    dict(id="aneantissement", chap="II.2 · A war of annihilation", fond="guerre", humeur="tension",
         retenir="No rules of war: war crimes became the normal course of the war. Soviet POWs: about 2.8 million killed (June 1941 – Feb. 1942), 3 in 100 survived; Auschwitz-Birkenau first built for them. 3/5 of WWII dead on the Eastern Front.",
         beats=[
        "{def4}Idea five. On the Eastern Front, the rules of war disappear. The violence is unprecedented in history: "
        "the sole aim is the total destruction of the enemy… or resistance until death. "
        "{def4.1}War crimes become the normal course of the war: the murder or ill-treatment of civilians and prisoners, "
        "and violence without any clear military objective.",
        "{-def4}{pow}The clearest example: the Soviet prisoners of war. {pow.1}About two point eight million of them were killed "
        "by the German armed forces and special units between June 1941 and February 1942, mainly through starvation. "
        "{pow.2}Out of every hundred Soviet prisoners, only three would survive the war. "
        "{pow.3}And Worksheet three, Source eight: the camp of Auschwitz-Birkenau was first built for Soviet prisoners, "
        "and gassing was applied first to them… then to the Jews.",
        "{-pow}{fig}Careful: the course text gives about two point eight million; Source eight of the Worksheet gives "
        "two million dead by February 1942. Always quote the document you are using.",
        "{-fig}{frac}The result: {!three fifths}three fifths of all the dead of the Second World War "
        "died on the Eastern Front.",
    ], vis={
        "def4": dict(type="def", cles=["total", "destruction", "rules"], terme="Key term · war of annihilation (Vernichtungskrieg)",
                     t="A war aiming at the total destruction of the enemy, without rules.",
                     etape="War crimes as the normal course of the war: civilians and prisoners murdered or ill-treated", x=170, y=200, w=940),
        "pow": dict(type="liste", titre="Soviet prisoners of war", cles=["starvation", "survived", "gassing"], items=[
            "≈ 2.8 million killed, June 1941 – Feb. 1942, mainly through starvation", "3 in 100 survived the war",
            "Auschwitz-Birkenau first built for them; gassing applied to them first, then to the Jews (Source 8)"],
            x=150, y=140, w=980),
        "fig": dict(type="note", terme="Watch out · two figures", cles=["course", "document"],
                    t="Course text: ≈ 2.8 million killed (June 1941 – Feb. 1942). Worksheet 3, Source 8: 2 million dead by Feb. 1942.",
                    etape="Quote the document you are using", x=170, y=200, w=940),
        "frac": dict(type="mot", t="3/5", g="of all the dead of WWII died on the Eastern Front", y=240, taille=150),
    }),

    # ================================================================ II.2, idée 6 : Stalingrad, le tournant
    dict(id="stalingrad", chap="II.2 · Stalingrad, the turning point", fond="nuit", humeur="tension",
         retenir="Why defend Stalingrad? A stronghold of Stalin's defensive strategy · an industrial and transport hub on the Volga · access to Caucasus oil · Stalin's city. Order No. 227 · encircled Nov. 1942 · Paulus capitulates 2 Feb. 1943: 95,000 prisoners.",
         beats=[
        "{g7}{g7.1}Idea six: Stalingrad, the turning point of the war. Leningrad, Moscow and Stalingrad are the strongholds of the Soviet defence. "
        "In the summer of 1942, the Germans, euphoric, drive towards the Volga and the Caucasus. And Stalingrad stands in their way.",
        "{g7.2}The Russians defend the city at all costs. Why? Four reasons, to learn as a list: "
        "it is also a question of Worksheet three.",
        "{-g7}{why}{why.1}One: Stalingrad is a stronghold of Stalin's defensive strategy. "
        "{why.2}Two: it is a major industrial and transport hub on the Volga. "
        "{why.3}Three: it ensures Soviet access to the oil of the Caucasus, strategic for the future of the conflict, and for the German supply of oil. "
        "{why.4}And four: it is a symbol. The city bears Stalin's name.",
        "{-why}Hence Stalin's Order number 227, of the twenty-eighth of July 1942.",
        ("C", "It is time to finish retreating. Not one step back!", "c_227"),
        "{-c_227}{eta}The battle, in stages. {eta.1}Summer 1942: euphoria. The Germans reach the Volga on the twenty-third of August. "
        "{eta.2}September and October: fighting street by street, factory by factory: the Barricade factory, Red October. "
        "{eta.3}Late November: the German army is encircled. {eta.4}Then the winter, and starvation. "
        "{eta.5}And on the second of February 1943, Paulus, commander of the German army, capitulates. Ninety-five thousand German soldiers "
        "are taken prisoner. A resounding defeat for the Wehrmacht.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[36, 38]),
        "why": dict(type="liste", titre="Why defend Stalingrad at all costs?", cles=["strategy", "Volga", "oil", "symbol"], items=[
            "A stronghold of Stalin's defensive strategy", "A major industrial and transport hub on the Volga",
            "Access to Caucasus oil: strategic for both sides", "A symbol: the city bearing Stalin's name"], x=170, y=140, w=940),
        "c_227": dict(type="cit", a="Joseph Stalin", o="Order No. 227, 28 July 1942 (Worksheet 3, Source 3)", x=200, y=210, w=880),
        "eta": dict(type="liste", titre="The battle in five stages", items=[
            "Summer 1942: euphoria; the Volga reached on 23 August", "Sept.–Oct.: street by street, factory by factory",
            "Late November: the German army encircled", "Winter: starvation",
            "2 Feb. 1943: Paulus capitulates · 95,000 prisoners"], x=150, y=130, w=980),
    }),

    # ================================================================ II.2, idée 7 : le rapport de forces
    dict(id="forces", chap="II.2 · The balance of forces has turned", fond="nuit", humeur="lumiere",
         retenir="Stalingrad, Nov. 1942 (Germans / Soviets): men 1,011,500 / 1,143,500 · guns 10,290 / 13,541 · tanks 675 / 894 · planes 1,216 / 1,115. In 1944 the USSR alone fields more divisions than the whole Axis: 400 against 349.",
         beats=[
        "{gf}Idea seven: by November 1942, the balance of forces has turned in favour of the Soviets. "
        "Here is Monsieur Ros's table of the forces facing each other at Stalingrad. {gf.1}The Germans in red, {gf.2}the Soviets in blue. "
        "{gf.3}{gf.4}{gf.5}Men: about one million and eleven thousand Germans, against one million one hundred and forty-three thousand Soviets.",
        "{gf.6}{gf.7}{gf.8}Artillery guns: about ten thousand, against thirteen and a half thousand. "
        "{gf.9}{gf.10}{gf.11}Tanks: six hundred and seventy-five, against eight hundred and ninety-four. "
        "{gf.12}{gf.13}{gf.14}Only in planes are the Germans slightly ahead.",
        "{-gf}{gd2}Despite its enormous losses of 1941, the Soviet Union is mobilising faster than Germany. "
        "The divisions table of the introduction shows the same trend. {gd2.1}Soviet divisions: two hundred in 1940, three hundred and fifty in 1943, four hundred and eighty-eight in 1945. "
        "{gd2.2}Germany peaks at three hundred and forty-seven, in 1944. "
        "{gd2.3}And in 1944, the Soviet Union alone fields more divisions than the whole Axis: four hundred against three hundred and forty-nine, "
        "Japan excluded. {gd2.4}And in that same month of November 1942, the German army is encircled.",
    ], vis={
        "gf": dict(type="graphe", titre="Forces at Stalingrad, November 1942 (course table)", x=300, y=110, w=680, h=520,
                   ax=AX_BARRES, el=barres(FORCES, "ca", "el")),
        "gd2": dict(type="graphe", titre="Divisions, 1940–1945 (course table)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1939.5, 1945.5], y=[0, 520], gx=ANS, gy=[100, 200, 300, 400, 500], lx="year", ly="divisions"),
                    el=[dict(type="courbe", pts=[list(p) for p in DIV_URSS], c="el", lbl="USSR", lp=[1944.8, 505], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_ALL], c="ca", lbl="Germany", lp=[1942.3, 205], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_AXE], c="sa", tir=True, lbl="whole Axis", lp=[1941.2, 380], dur=1.8),
                        dict(type="points", pts=[[1944, 400], [1944, 349]], c="iv", lbl="1944: 400 / 349", lp=[1943.6, 455])]),
    }),

    # ================================================================ II.2, idée 8 : une guerre totale
    dict(id="totale", chap="II.2 · Stalingrad, a total war", fond="guerre", humeur="tension",
         retenir="Total war = all of a society's resources mobilised + front and rear blurred (Première, H10). Stalingrad: factories in the rear, street fighting among civilians, propaganda, no surrender. Toll (Source 7): USSR 1.13 million (500,000 killed), Germany and allies 760,000. USSR in the war: 27–28 million, one in seven.",
         beats=[
        "{def5}Idea eight: Stalingrad fits the definition of total war. Remember the definition from Première, chapter H10: "
        "total war is {!the mobilisation of all of a society's resources}the mobilisation of all of a society's resources, "
        "{def5.1}and the blurring of the line between front and rear.",
        "{-def5}{crit}Stalingrad meets every criterion. {crit.1}The whole economy is behind the front: in Source three, factories in the rear "
        "send ever more aircraft, tanks and guns. "
        "{crit.2}The fighting goes street by street and factory by factory, with civilians inside the battlefield. "
        "{crit.3}Propaganda on both sides: Source five, a Bolshevik poster of 1943, with Stalingrad written on the flag. "
        "{crit.4}And the refusal of any surrender, until death or capture.",
        "{-crit}A German soldier's letters, Source six, show the descent. At first:",
        ("C", "to take Stalingrad is not difficult", "c_l1"),
        "{-c_l1}Then weeks of fighting for the Barricade factory, the encirclement, and on the twenty-sixth of December:",
        ("C", "the horses have already been eaten", "c_l2"),
        "{-c_l2}{gt}And the toll of the battle, Source seven. {gt.1}{gt.2}{gt.3}{gt.4}{gt.5}The Soviet Union lost one point one three million soldiers and civilians, "
        "killed, wounded or captured, including five hundred thousand killed. Germany and its allies lost seven hundred and sixty thousand. "
        "{gt.6}{gt.7}{gt.8}Tanks lost: four thousand three hundred and forty-one, against five hundred. "
        "{gt.9}{gt.10}{gt.11}Aircraft: two thousand seven hundred and sixty-nine, against nine hundred.",
        "{-gt}{urss}The Soviet Union paid the highest price of the whole war. Official estimates of Soviet losses are now "
        "twenty-seven to twenty-eight million: {!one in seven}one in seven of the pre-war population.",
    ], vis={
        "def5": dict(type="def", cles=["resources", "front", "rear"], terme="Key term · total war (Première, H10)",
                     t="The mobilisation of all of a society's resources…",
                     etape="… and the blurring of the line between front and rear", x=170, y=200, w=940),
        "crit": dict(type="liste", titre="Stalingrad, a total war: four criteria", cles=["economy", "civilians", "Propaganda", "surrender"], items=[
            "The whole economy behind the front: factories in the rear (Source 3)", "Street by street, factory by factory: civilians inside the battlefield",
            "Propaganda on both sides: the 1943 poster (Source 5)", "No surrender, until death or capture"], x=150, y=130, w=980),
        "c_l1": dict(type="cit", a="A German soldier", o="letters, July–December 1942 (Worksheet 3, Source 6)", x=200, y=230, w=880),
        "c_l2": dict(type="cit", a="A German soldier", o="letter, 26 December 1942 (Worksheet 3, Source 6)", x=200, y=230, w=880),
        "gt": dict(type="graphe", titre="The toll of Stalingrad (Worksheet 3, Source 7)", x=300, y=110, w=680, h=520,
                   ax=dict(AX_BARRES, x=[0.35, 3.65]), el=barres(PERTES, "ca", "el")),
        "urss": dict(type="mot", t="27–28 million", g="Soviet losses in the war: one in seven of the pre-war population", y=250, taille=100),
    }),

    # ================================================================ la Worksheet 3
    dict(id="ws3", chap="Worksheet 3 · the key answers", fond="aube", humeur="calme",
         retenir="Worksheet 3: the enemy dehumanised and murdered (Sources 1, 2, 8) · five stages of the battle · extreme brutality · four reasons to defend the city · total war: largely.",
         beats=[
        "{wsrc}Now, Worksheet three: the Battle of Stalingrad, a war of annihilation. Seven sources: "
        "{wsrc.1}the orders of Jodl {wsrc.2}and Reichenau, {wsrc.3}Stalin's Order number 227, "
        "{wsrc.4}a poster and photographs, {wsrc.5}a soldier's letters, {wsrc.6}the toll, {wsrc.7}the Soviet prisoners.",
        "{-wsrc}{wq}Five questions, with their key answers, suggested by the site except the fourth, given by the course. "
        "{wq.1}One: in the German orders, the enemy is dehumanised: barbaric, Asiatic, subhuman; commissars shot, prisoners starved, "
        "the first to be gassed. {wq.2}Two: the stages, which you know now. "
        "{wq.3}Three: the brutality: many crosses with our helmets on top, writes the soldier; men eating the horses, "
        "looking like corpses or lunatics. {wq.4}Four: the four reasons to defend the city. "
        "{wq.5}And five: total war. That one, you are going to write.",
    ], vis={
        "wsrc": dict(type="liste", titre="Worksheet 3 · the sources", marques=["1", "2", "3", "5", "6", "7", "8"], petit=True, items=[
            "Jodl's order on the commissars, May 1941", "Reichenau's Severity Order, 10 Oct. 1941", "Stalin's Order No. 227, 28 July 1942",
            "A Bolshevik poster (1943); photographs of soldiers", "A German soldier's letters, July–Dec. 1942",
            "The toll of the battle", "The Soviet prisoners of war"], x=170, y=90, w=940),
        "wq": dict(type="liste", titre="Worksheet 3 · the key answers", petit=True, items=[
            "Enemies dehumanised: “barbaric”, “Asiatic”, “subhuman” · commissars shot, POWs starved, first gassed",
            "Context and stages: Barbarossa stalled → euphoria → streets → encirclement → hunger → 2 Feb. 1943",
            "Brutality: factory by factory, “crosses with our helmets on top”, horses eaten",
            "Why defend it: strategy, Volga hub, Caucasus oil, Stalin's city (course answer)",
            "Total war? → your turn"], x=130, y=110, w=1020),
    }),

    # ================================================================ à toi : un paragraphe d'essay
    dict(id="essai", chap="Your turn · an essay paragraph", fond="aube", humeur="calme",
         retenir="A paragraph: judgement (largely) · definition · evidence (factories in the rear, street fighting, propaganda and Order No. 227, the toll) · nuance (a localised battle, but the heart of a total war).",
         beats=[
        "{ex5}Here is question five of the Worksheet, written as an essay paragraph. "
        "{!To what extent}To what extent does the Battle of Stalingrad fit the definition of total war?",
        "{-ex5}{pa4}",
        ("P", 2.0),
        "{-pa4}{mod4}Here is a model paragraph. The Battle of Stalingrad largely fits the definition of total war, "
        "the mobilisation of all of a society's resources and the blurring of front and rear. "
        "First, the whole Soviet economy was behind the front: in Source three, the factories in the rear send ever more planes, "
        "tanks and guns. Second, the fighting took place inside an inhabited city, street by street and factory by factory, "
        "as in the struggle for the Barricade factory. Third, propaganda mobilised minds on both sides, and no surrender was accepted: "
        "Order number 227 demanded not one step back. "
        "{mod4.1}One nuance: Stalingrad remained a localised military battle. But it was the heart of a total war, "
        "fought across the whole Eastern Front.",
    ], vis={
        "ex5": dict(type="exo", niveau="essay", titre="To what extent does the Battle of Stalingrad fit the definition of total war?",
                    src="Worksheet 3, question 5", enonce=["One paragraph: judgement, definition, evidence, nuance"]),
        "pa4": dict(type="pause", t="Write the paragraph: a judgement, the definition, three pieces of evidence, a nuance.",
                    sous="Pause the video, write it on a sheet, then play on for a model."),
        "mod4": dict(type="note", terme="Model paragraph", cles=["largely", "economy", "city", "propaganda"],
                     t="Largely: the economy behind the front (Source 3), fighting inside an inhabited city (the Barricade factory), "
                       "propaganda and “Not one step back!”, 1.13 million Soviet casualties.",
                     etape="Nuance: a localised battle… but the heart of a total war on the whole Eastern Front", x=150, y=170, w=980),
    }),

    # ================================================================ à toi : un DBQ a)
    dict(id="dbq", chap="Your turn · a DBQ", fond="guerre", humeur="tension",
         retenir="DBQ a): judgement in the first line · the document in one sentence · strengths (an eyewitness, dated stages, the human cost) · limits (one German soldier, no figures, stops in December, letters to a family).",
         beats=[
        "{ex6}Now a DBQ, part a), on a source of the Worksheet. {!How useful}How useful is Source six, a German soldier's letters "
        "from July to December 1942, for understanding the Battle of Stalingrad?",
        "{-ex6}{str2}The structure. {str2.1}First line: the judgement: largely, significantly, partly or slightly useful. "
        "{str2.2}The document in one sentence. {str2.3}Strengths, several arguments. {str2.4}Limits, several arguments.",
        "{-str2}{pa5}",
        ("P", 2.0),
        "{-pa5}{rep5}A model. {rep5.1}Source six is significantly useful for understanding the Battle of Stalingrad. "
        "{rep5.2}It is a series of letters written by a German soldier between July and December 1942, during the battle itself.",
        "{rep5.3}Its strengths. It is an eyewitness account, from inside the battle. Its dates follow the stages: "
        "the summer euphoria, the weeks at the Barricade factory, the encirclement on the twenty-ninth of November, the hunger of December. "
        "And it shows the human cost, the crosses with helmets on top, which no table of figures can show.",
        "{rep5.4}Its limits. It is the view of one German soldier: nothing on the Soviet side, the civilians or the strategy. "
        "No figures: Source seven and the table of forces are needed for that. It stops in December, before the capitulation. "
        "And a letter to a family may hide the worst. Useful for the experience of the battle, much less for its scale.",
    ], vis={
        "ex6": dict(type="exo", niveau="dbq", titre="How useful is Source 6 for understanding the Battle of Stalingrad?",
                    src="Question written for this video, on Worksheet 3", enonce=["Part a) of a DBQ"],
                    donnees=["A German soldier's letters, July–December 1942: “to take Stalingrad is not difficult” … encircled (29 November) … “the horses have already been eaten”"]),
        "str2": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa5": dict(type="pause", t="Write the first line and the sentence that presents the document, then the strengths and the limits.",
                    sous="Pause the video, write your answer, then play on for a model."),
        "rep5": dict(type="liste", titre="A model answer", items=[
            "Significantly useful for understanding the Battle of Stalingrad", "Letters of a German soldier, July–Dec. 1942, during the battle",
            "Strengths: an eyewitness · dates that follow the stages · the human cost",
            "Limits: one German soldier · no figures · stops in December · a letter home"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}The plans: the pact of 1939 opened the road to the East, and three reasons to invade the Soviet Union, "
        "economic, ideological, racial, each with its example. "
        "{carte.2}Barbarossa: the twenty-second of June 1941, three thrusts, stopped before Leningrad and Moscow; five million dead in two hundred days. "
        "{carte.3}A war of annihilation: no rules, Stalin's no mercy, the Soviet prisoners starved, three fifths of all the dead in the East. "
        "{carte.4}And Stalingrad: the turning point, encircled in November 1942, Paulus capitulates on the second of February 1943. A total war.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: towards the genocide. The ghettos, the Einsatzgruppen, the killing centres… and Treblinka.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="BARBAROSSA", branches=[
            dict(t="II.1 · The plans", items=["Aug. 1939 pact · Poland shared", "economic: Grossraum, oil", "ideological · racial"]),
            dict(t="Barbarossa", items=["22 June 1941 · three thrusts", "purges · scorched earth", "Dec. 1941: Moscow holds"]),
            dict(t="Annihilation", items=["Stalin, 7 Nov. 1941", "≈ 2.8 million POWs killed", "3/5 of the dead in the East"]),
            dict(t="Stalingrad", items=["Order No. 227", "Nov. 1942: forces turned", "2 Feb. 1943 · total war"])]),
        "fin": dict(type="mot", t="Next: towards the genocide", g="Episode 5 · ghettos, Einsatzgruppen, killing centres", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="What did the Nazi-Soviet pact of August 1939 give Hitler?",
         r=["The neutrality of the USSR and a secret plan to carve up Poland", "A military alliance against Britain",
            "The Baltic states and Bessarabia", "Soviet oil in exchange for the Sudetenland"], ok=0, voir="def3",
         ex="It was the USSR that annexed the Baltic states, Northern Bukovina and Bessarabia in 1940."),
    dict(q="Which example illustrates the economic reason for invading the USSR?",
         r=["Stalingrad, a hub on the Volga ensuring access to Caucasus oil", "Jodl's order on the political commissars",
            "Reichenau's Severity Order", "Stalin's speech of 7 November 1941"], ok=0, voir="eco",
         ex="The Grossraum needed the USSR's resources: farmland, minerals, oil."),
    dict(q="What did Jodl's order of May 1941 prescribe for captured political commissars?",
         r=["To be “dispatched by firearms” as a matter of routine", "To be exchanged for German prisoners",
            "To be sent to labour camps in Germany", "To be tried by military courts"], ok=0, voir="jodl",
         ex="An example of the ideological reason: the crusade against “Jewish Bolshevism”."),
    dict(q="In 1941, where did the southern German thrust aim?",
         r=["Ukraine, Kiev and Rostov", "Stalingrad and the Caucasus", "Moscow", "Leningrad"], ok=0, voir="att",
         ex="Stalingrad and the Caucasus were the targets of the second offensive, in the summer of 1942."),
    dict(q="What was the toll of the first 200 days of Barbarossa, according to the course?",
         r=["5 million dead, a thousand an hour", "60 million dead", "95,000 prisoners", "27–28 million dead"], ok=0, voir="bil2",
         ex="27–28 million is the Soviet toll for the whole war; 95,000 the Germans captured at Stalingrad."),
    dict(q="How did Stalin answer the Nazis on 7 November 1941?",
         r=["“If the Germans want a war of annihilation, they will get it”", "“Not one step back!”",
            "“We shall never surrender”", "He offered an armistice"], ok=0, voir="c_st1",
         ex="“Not one step back!” is Order No. 227, of 28 July 1942."),
    dict(q="How many Soviet prisoners in 100 survived the war?",
         r=["3", "30", "50", "97"], ok=0, voir="pow",
         ex="About 2.8 million were killed between June 1941 and February 1942, mainly through starvation (course text)."),
    dict(q="At Stalingrad in November 1942, in which category were the Germans still ahead?",
         r=["Planes", "Men", "Artillery guns", "Tanks"], ok=0, voir="gf",
         ex="1,216 German planes against 1,115; the Soviets led in men, guns and tanks."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H3 · Parts II.1 and II.2, Worksheet 3, table of the forces at Stalingrad, divisions table of the introduction) as written on the site; answers to Worksheet 3 questions 1, 2, 3 and 5 suggested by the site; the example of Tukhachevsky added from outside the course; animated map of chapter 3 (site).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
