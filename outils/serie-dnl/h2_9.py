"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 9 : « Recap » (tout le chapitre).

Même chaîne que les épisodes de H3 (voir outils/serie-dnl/h3_1.py) : outils/serie-philo/generer.py h2_9 ; sortie dans
dnl/serie/ ; modèle : h3_7.py (récapitulatif de H3).
Contenu : la synthèse du chapitre dans le site (dnl/index.html, CHAPTERS.H2 : objective, big picture, timeline, key figures,
idées des parties Intro, I.1 à I.3, II.1 à II.3, III.1 à III.3, key issue, key terms ; grille de synthèse de M. Ros H2_GRID et
tableau comparatif H2_TABLE ; QCM H2_QCM). Rien n'est ajouté au cours ; seul le décret de 1938 sur l'enseignement du russe
n'est pas repris (sa date vient d'ailleurs dans le site).
Carte animée H2 (numéros de scènes, ordre chronologique de la carte) :
  0 définition · 1 brutalisation · 2 Russie 1917 · 3 Allemagne 1918-19 · 4 Italie 1919-20 · 5 Versailles · 6 marche sur Rome ·
  7 putsch de Munich · 8 dictature fasciste légale · 9 culte du chef · 10 Lebensraum · 11 jeunesse · 12 plan quinquennal ·
  15 koulaks · 16 les nazis premier parti · 17 Goulag · 18 impérialisme japonais · 19 Holodomor · 20 Hitler chancelier ·
  21 incendie du Reichstag · 22 police politique et camps · 26 Stakhanov · 27 Abyssinie · 28 Rhénanie · 29 Axe et Espagne ·
  30 procès de Moscou · 32 Nankin · 33 Anschluss · 34 Munich · 35 Prague · 36 pacte germano-soviétique · 37 Pologne.
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-9"
NOTION = "Totalitarian Regimes"
NUM = 9
TITRE = "Recap"
SUIVANT = "The end of the series · back to the course and the quiz"
PRONONCIATION = {"Reichstag": "Rikes-tahg", "Hindenburg": "Hin-den-burg", "Biennio": "Bee-en-nyo", "Rosso": "Ross-o",
                 "Matteotti": "Mat-teh-ot-tee", "Balilla": "Ba-lee-la", "Komsomol": "Kom-so-mol",
                 "Holodomor": "Holo-do-more", "kulak": "koo-lak", "kulaks": "koo-laks", "Gulag": "Goo-lag",
                 "Yezhov": "Yezh-off", "Anschluss": "Ahn-shloos", "Sudetenland": "Soo-day-ten-land",
                 "Stakhanov": "Sta-kha-noff", "Duce": "Doo-chay", "Führer": "Fyoo-rer", "OVRA": "Ov-ra",
                 "fascistissime": "fa-shis-tee-see-meh", "Lebensraum": "Lay-bens-rowm", "Abyssinia": "Abby-sinnia",
                 "Daladier": "Da-la-dyay", "Hehn": "Hayn", "Mosse": "Mossy", "Volk": "Folk",
                 "Riefenstahl": "Ree-fen-shtahl", "Himmler": "Him-ler", "Gestapo": "Geh-stah-po",
                 "Mussolini": "Moos-so-lee-nee"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Mussolini's Italy, Hitler's Germany, Stalin's Soviet Union. Three regimes that wanted to control everything, "
        "and to remake human beings according to an ideology. And one road, which ends in September 1939… in war.",
        "{-q1}{q2}This last episode puts the whole chapter together, and answers its question: did totalitarian ideology cause "
        "the Second World War?",
        "{-q2}{-g0}{plan}Here is the plan. {plan.1}The chapter on the map, from the trenches to Poland. {plan.2}Twelve dates. "
        "{plan.3}The three regimes, side by side. {plan.4}The people and the figures. {plan.5}One mind map for each part. "
        "{plan.6}And the answer to the question… before a final quiz.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[0]),
        "q1": dict(type="question", t="Three regimes. One road to war.", bande=True),
        "q2": dict(type="question", t="Did totalitarian ideology cause the war?", bande=True),
        "plan": dict(type="liste", titre="The recap, in six steps", items=[
            "The chapter on the map, 1914 – 1939", "Twelve dates", "The three regimes compared",
            "People and figures", "One mind map per part", "The answer to the chapter's question"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 9", t="Recap",
                      sous="Totalitarian Regimes · 1917 – 1939"),
    }),

    # ================================================================ I. des tranchées au pouvoir
    dict(id="film1", chap="From the trenches to power", fond="nuit", humeur="tension",
         retenir="WW1 brutalisation · 1917 Bolsheviks · 1919 Versailles and the Biennio Rosso · Oct. 1922 March on Rome · 1928 Five-Year Plan · 1932–33 Holodomor · 30 Jan. 1933 Hitler chancellor.",
         beats=[
        "{g1}{g1.1}It all begins in the trenches. Four years of mass killing made violence ordinary: George Mosse calls it "
        "{!brutalisation}brutalisation, and sees the Great War as the matrix of totalitarianism. "
        "{g1.2}In Russia, the war brings down the Tsar in February 1917; in October, Lenin and Trotsky's Bolsheviks seize power, "
        "then win a civil war. Europe is afraid of communism.",
        "{g1.3}In Germany, defeat ends the Empire, and the Weimar Republic is born in violence: the Spartacist uprising is crushed in January 1919. "
        "{g1.4}Italy has won the war, but speaks of a mutilated victory. In the Biennio Rosso, the red years of 1919 and 1920, "
        "peasants seize land and workers occupy the factories, and landowners pay Mussolini's Blackshirts to repress them. "
        "{g1.5}And Versailles: for the Germans, a Diktat; for the army, a stab in the back.",
        "{g1.6}October 1922: the March on Rome. About twenty thousand Blackshirts; the threat is enough, and the king appoints Mussolini. "
        "{g1.7}November 1923: Hitler's putsch fails in Munich. In prison, he writes Mein Kampf.",
        "{-g1}{g2}{g2.1}In Italy, after the murder of Matteotti in 1924, the fascistissime laws of 1925 make the dictatorship legal. "
        "{g2.2}In the Soviet Union, Stalin launches the first Five-Year Plan in 1928, and forced collectivisation. "
        "{g2.3}The kulaks become class enemies, {g2.4}and in 1932 and 1933 the Holodomor, a man-made famine, kills millions in Ukraine.",
        "{-g2}{g3}{g3.1}In Germany, the crisis of 1929 turns the Nazis into the largest party: thirty-seven point four per cent in July 1932… "
        "never a majority. {g3.2}On the thirtieth of January 1933, Hindenburg appoints Hitler chancellor, legally. "
        "{g3.3}On the twenty-seventh of February, the Reichstag burns: freedoms are suspended, and the communists are hunted down.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 3, 4, 5, 6, 7]),
        "g2": dict(type="globe", code="H2", sc=[8, 12, 15, 19]),
        "g3": dict(type="globe", code="H2", sc=[16, 20, 21]),
    }),

    # ================================================================ II. la route de la guerre
    dict(id="film2", chap="The road to war", fond="nuit", humeur="tension",
         retenir="1931 Manchuria · Oct. 1935 Abyssinia · Mar. 1936 Rhineland · 1936 Axis and Spain · 1937 Nanjing · Mar. 1938 Anschluss · Sept. 1938 Munich · Mar. 1939 Prague · Aug. 1939 the pact · 1 Sept. 1939 Poland.",
         beats=[
        "{g4}{g4.1}In Asia, Japan wants autarky and claims to be a superior race: it seizes Manchuria in 1931. "
        "{g4.2}October 1935: Mussolini invades Abyssinia, in the name of Rome. The League debates sanctions for seven months… and spares oil. "
        "{g4.3}March 1936: Hitler's troops enter the demilitarised Rhineland. A gamble: they had orders to retreat if France reacted. It did not. "
        "{g4.4}1936: the Rome–Berlin Axis, and the Spanish Civil War, where the dictators intervene and the democracies stay out.",
        "{g4.5}December 1937: at Nanjing, the Japanese army kills civilians and prisoners by the hundred thousand. "
        "{g4.6}March 1938: the Anschluss. {g4.7}September 1938: at Munich, Chamberlain and Daladier hand the Sudetenland to Hitler, "
        "without the Czechs. Appeasement at its height. {g4.8}March 1939: Prague. Hitler had lied, and appeasement is dead.",
        "{g4.9}August 1939: the Nazi-Soviet pact secretly plans to divide Poland. {g4.10}And on the first of September, Germany attacks Poland. "
        "On the third, France and Britain declare war.",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[18, 27, 28, 29, 32, 33, 34, 35, 36, 37]),
    }),

    # ================================================================ III. douze dates
    dict(id="dates", chap="Twelve dates", fond="nuit", humeur="calme",
         retenir="Oct. 1917 · 1919 · Oct. 1922 · 1925 · 1928 · 1932–33 · 30 Jan. 1933 · Oct. 1935 · Mar. 1936 · 1937–38 · Sept. 1938 · 23 Aug. – 1 Sept. 1939.",
         beats=[
        "{fr}Twelve dates to know by heart. {fr.1}October 1917, the Bolshevik coup. {fr.2}1919, the Treaty of Versailles. "
        "{fr.3}October 1922, the March on Rome. {fr.4}1925, the fascistissime laws, and Mein Kampf. {fr.5}1928, the first Five-Year Plan. "
        "{fr.6}1932 and 1933, the Holodomor. {fr.7}The thirtieth of January 1933, Hitler chancellor. {fr.8}October 1935, Abyssinia. "
        "{fr.9}March 1936, the Rhineland. {fr.10}1937 and 1938, the Great Purge. {fr.11}September 1938, Munich. "
        "{fr.12}And the end of August 1939: the pact, then Poland.",
        ("P", 3.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Bolsheviks", d=1917.8, q="Oct. 1917"), dict(nom="Versailles", d=1919.5, q="1919"),
            dict(nom="Rome", d=1922.8, q="Oct. 1922"), dict(nom="Dictatorships", d=1925, q="1925"),
            dict(nom="Plan", d=1928, q="1928"), dict(nom="Holodomor", d=1932.5, q="1932–33"),
            dict(nom="Hitler", d=1933.08, q="30 Jan. 1933"), dict(nom="Abyssinia", d=1935.8, q="Oct. 1935"),
            dict(nom="Rhineland", d=1936.2, q="Mar. 1936"), dict(nom="Purge", d=1937, q="1937–38"),
            dict(nom="Munich", d=1938.7, q="Sept. 1938"), dict(nom="War", d=1939.65, q="Aug.–Sept. 1939")]),
    }),

    # ================================================================ IV. trois régimes : idéologie, chef, parti
    dict(id="comparer1", chap="Three regimes, one machine", fond="nuit", humeur="lumiere",
         retenir="Supreme goal: the nation (Fascism), the race (Nazism), the class (Stalinism). Leader: il Duce, der Führer, the little father of the peoples. One single party, one symbol.",
         beats=[
        "{gc}{l1}Now the three regimes, side by side, as in Monsieur Ros's synthesis grid. "
        "F for Fascism, N for Nazism, S for Stalinism. {gc.1}First, the ideology: a set of beliefs that sets a supreme goal. "
        "{l1.1}For Mussolini, the nation and the absolute State: everything is in the State. Divided into nations, not classes, "
        "and racist only from 1938. {l1.2}For Hitler, the race: history as a permanent war between races. "
        "{l1.3}For Stalin, the class: class struggle, no private property, a classless society.",
        "{-l1}{l2}{gc.2}Second, the leader, built as an ideal man in whom the nation recognises itself. {l2.1}Mussolini is il Duce, "
        "and il Duce is always right. {l2.2}Hitler is der Führer; the official greeting becomes Heil Hitler. "
        "{l2.3}Stalin is the little father of the peoples, and in 1925 a city is renamed Stalingrad.",
        "{-l2}{l3}Third, one single party, with one symbol. {l3.1}The National Fascist Party, and the Roman fasces. "
        "{l3.2}The NSDAP, and the swastika. {l3.3}The Communist Party, and the hammer and sickle. The purpose is the same: "
        "to make the nation, the party and the leader one and the same, so that criticising the leader means betraying the country.",
    ], vis={
        "gc": dict(type="globe", code="H2", sc=[0, 9]),
        "l1": dict(type="liste", titre="1 · The supreme goal", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"],
                   cles=["nation", "race", "class"], items=[
            "The nation and the absolute State · racist only from 1938", "The race: history as a war between races",
            "The class: no property, a classless society"]),
        "l2": dict(type="liste", titre="2 · The leader", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Il Duce · “il Duce ha sempre ragione”", "Der Führer · “Heil Hitler”",
            "The little father of the peoples · Stalingrad, 1925"]),
        "l3": dict(type="liste", titre="3 · One party, one symbol", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "National Fascist Party · the Roman fasces", "NSDAP · the swastika", "Communist Party · the hammer and sickle"]),
    }),

    # ================================================================ V. homme nouveau, terreur, expansion
    dict(id="comparer2", chap="New Man, terror, expansion", fond="nuit", humeur="tension",
         retenir="Same method, same ambition — a New Man — but unequal scale: Soviet terror the deadliest, Nazi violence biological, Italy the least lethal, with counter-powers.",
         beats=[
        "{gn}{l4}{gn.1}Fourth, the New Man. A dictatorship wants silence; a totalitarian regime wants you to change, and it starts with children. "
        "{l4.1}In Italy, the Balilla, and a New Man strong and cultured, in the service of the Party. "
        "{l4.2}In Germany, the Hitler Youth, compulsory from ten to eighteen, and a purified race, the Volk: racial instruction in schools, "
        "the Nuremberg laws of 1935. {gn.2}{l4.3}In the Soviet Union, the Komsomol, and the worker, whose hero is the miner Stakhanov.",
        "{-l4}{l5}{gn.3}Fifth, terror, which is a method of government. {l5.1}In Italy, the OVRA and the Special Court; opponents are "
        "silenced, sent into internal exile, rather than killed. {l5.2}In Germany, the Gestapo and the S.S., both under Himmler, "
        "the camps from Dachau in 1933, and four hundred thousand Germans sterilised. "
        "{gn.4}{l5.3}In the Soviet Union, the NKVD, the Gulag, and the Great Purge: six hundred and eighty thousand executions. "
        "{gn.5}Terror even devours its own: the Night of the Long Knives, Yezhov shot and erased from the photographs, Trotsky murdered in Mexico.",
        "{-l5}{l6}{gn.6}Sixth, expansion. {l6.1}Mussolini wants an empire in the name of Rome: Abyssinia. "
        "{l6.2}Hitler wants Lebensraum, living space in the East, announced in Mein Kampf. "
        "{l6.3}Stalin builds socialism in one country, but in August 1939 he shares Poland with Hitler.",
        "{-l6}{-gn}{nu}So, {!the same machine}the same machine in all three, but not the same scale. Soviet terror killed on the largest scale; "
        "Nazi violence was biological, aimed at a race and at the unfit; and Italy was the least lethal, and kept counter-powers: "
        "the king and the Church. That nuance separates a good answer from a list of similarities.",
    ], vis={
        "gn": dict(type="globe", code="H2", sc=[11, 26, 22, 17, 38, 10]),
        "l4": dict(type="liste", titre="4 · The New Man", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "Balilla · strong and cultured, for the Party", "Hitler Youth (10–18) · the Volk, a purified race",
            "Komsomol · the worker: Stakhanov, 1935"]),
        "l5": dict(type="liste", titre="5 · Mass terror", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "OVRA, Special Court · internal exile", "Gestapo and S.S. · Dachau · 400,000 sterilised",
            "NKVD · the Gulag · 680,000 executions, 1937–38"]),
        "l6": dict(type="liste", titre="6 · Expansion", x=60, y=110, w=620, petit=True, bande=True, marques=["F", "N", "S"], items=[
            "An empire in the name of Rome · Abyssinia, 1935", "Lebensraum in the East · Mein Kampf, 1925",
            "Socialism in one country · Poland shared, 1939"]),
        "nu": dict(type="note", terme="The nuance that makes the difference", cles=["method", "scale", "criterion"],
                   t="Identical in method and purpose, unequal in scale and in the criterion that designates the victim: "
                     "social in the USSR, biological in Germany, political in Italy."),
    }),

    # ================================================================ VI. personnages et chiffres
    dict(id="gens", chap="People and figures", fond="nuit", humeur="calme",
         retenir="≈ 20,000 Blackshirts · 37.4% (July 1932) · 5.6 million unemployed · 7% → 90% collectivised · 680,000 executions · 400,000 sterilised.",
         beats=[
        "{pe}Twelve people. {pe.1}Mussolini, {pe.2}Hitler {pe.3}and Stalin. {pe.4}Victor Emmanuel the Third, who appointed Mussolini, "
        "{pe.5}and Hindenburg, who appointed Hitler. {pe.6}Matteotti, the socialist deputy murdered in 1924. "
        "{pe.7}Himmler, head of the Gestapo and the S.S. {pe.8}Yezhov, head of the NKVD, executed in 1940. "
        "{pe.9}Stakhanov, the worker-hero. {pe.10}Chamberlain {pe.11}and Daladier, the men of Munich. "
        "{pe.12}And Hannah Arendt: these regimes rested on the confidence of the masses, not on terror alone.",
        "{-pe}{ch}And six figures. {ch.1}About twenty thousand Blackshirts on the road to Rome. "
        "{ch.2}Thirty-seven point four per cent for the Nazis in July 1932: never a majority. {ch.3}Five point six million unemployed "
        "in Germany in 1932. {ch.4}Seven per cent of Soviet peasant households collectivised in 1928… ninety per cent in 1936. "
        "{ch.5}Six hundred and eighty thousand executions in the Great Purge. {ch.6}Four hundred thousand Germans forcibly sterilised.",
    ], vis={
        "pe": dict(type="nuage", items=["Mussolini", "Hitler", "Stalin", "Victor Emmanuel III", "Hindenburg", "Matteotti",
                                        "Himmler", "Yezhov", "Stakhanov", "Chamberlain", "Daladier", "Hannah Arendt"]),
        "ch": dict(type="liste", titre="Six figures", items=[
            "≈ 20,000 Blackshirts march on Rome (1922)", "37.4% for the NSDAP, July 1932 — never a majority",
            "5.6 million unemployed in Germany (1932)", "7% → 90% of peasant households collectivised (1928–36)",
            "680,000 executions in the Great Purge (1937–38)", "400,000 Germans forcibly sterilised (1933–45)"],
            x=150, y=100, w=980),
    }),

    # ================================================================ VII. trois cartes mentales
    dict(id="cartes", chap="Three mind maps", fond="nuit", humeur="calme",
         retenir="Totalitarianism: total control of society, through coercion, to transform man according to an ideology.",
         beats=[
        "{def}First, the key term of the chapter. {def.1}Totalitarianism: a regime that seeks total control of society, through coercion, "
        "to transform man according to an ideology. Three parts: total control, coercion, transformation. "
        "The last one is what separates it from an ordinary dictatorship.",
        "{-def}{c1}Part one: where the regimes came from, and how they took power. {c1.1}The legacy of the Great War: "
        "brutalisation, and the Russian revolution. {c1.2}In Italy, the mutilated victory, the red years, and the March on Rome. "
        "{c1.3}In Germany, Versailles, the crisis, and a legal appointment. {c1.4}Then three ideologies: nation, race, class. "
        "{c1.5}And Stalinism: collectivisation, the kulaks, the Holodomor.",
        ("P", 2.0),
        "{-c1}{c2}Part two: how they controlled society. {c2.1}The cult of the leader, with rallies, radio and censorship. "
        "{c2.2}The New Man, shaped from childhood, by the school, the law and work. {c2.3}Mass terror: political police and camps. "
        "{c2.4}Terror against the regime's own men. {c2.5}And the nuance: the same method, at a different scale.",
        ("P", 2.0),
        "{-c2}{c3}Part three: why they went to war. {c3.1}War as a value: Abyssinia, and Lebensraum. "
        "{c3.2}Japan: autarky and a superior race, from Manchuria to Nanjing. {c3.3}Democracies unable to act: a powerless League, "
        "American isolationism. {c3.4}Appeasement: the Rhineland, the Anschluss, Munich. "
        "{c3.5}And war: Prague, the pact, Poland.",
        ("P", 2.5),
    ], vis={
        "def": dict(type="def", terme="Key term · Totalitarianism", cles=["total", "coercion", "transform"],
                    t="A regime that seeks total control of society, through coercion, to transform man according to an ideology."),
        "c1": dict(type="carte", centre="PART I · ROOTS AND POWER", branches=[
            dict(t="The legacy of WW1", items=["brutalisation (Mosse)", "Russia, 1917: the Red Scare"]),
            dict(t="Italy", items=["mutilated victory · Biennio Rosso", "March on Rome, Oct. 1922"]),
            dict(t="Germany", items=["Diktat · stab in the back", "37.4% → chancellor, 30 Jan. 1933"]),
            dict(t="Three ideologies", items=["nation · race · class", "Fascism racist only from 1938"]),
            dict(t="Stalinism", items=["Five-Year Plan · collectivisation", "kulaks · Holodomor, 1932–33"])]),
        "c2": dict(type="carte", centre="PART II · TOTAL CONTROL", branches=[
            dict(t="The cult of the leader", items=["Duce · Führer · little father", "rallies, radio, censorship"]),
            dict(t="The New Man", items=["Balilla · Hitler Youth · Komsomol", "school, law, work"]),
            dict(t="Mass terror", items=["OVRA · Gestapo and S.S. · NKVD", "camps: Dachau, the Gulag"]),
            dict(t="Terror devours its own", items=["Night of the Long Knives", "Great Purge · Yezhov erased"]),
            dict(t="Same method, other scale", items=["USSR: 680,000 executions", "Italy: exile, the Church"])]),
        "c3": dict(type="carte", centre="PART III · THE ROAD TO WAR", branches=[
            dict(t="War as a value", items=["Abyssinia, 1935", "Lebensraum · Mein Kampf"]),
            dict(t="Japan", items=["autarky · a “superior race”", "Manchuria 1931 · Nanjing 1937"]),
            dict(t="Powerless democracies", items=["the League · US isolationism", "Stresa · naval agreement"]),
            dict(t="Appeasement", items=["Rhineland · Anschluss", "Munich, Sept. 1938"]),
            dict(t="War", items=["Prague, March 1939", "the pact · Poland, 1 Sept."])]),
    }),

    # ================================================================ VIII. la question du chapitre
    dict(id="question", chap="The chapter's question", fond="guerre", humeur="mystere",
         retenir="Totalitarian ideology supplied the will to war; the democracies' reluctance supplied the opportunity. Key terms: totalitarianism, Lebensraum, appeasement.",
         beats=[
        "{hi}So, did totalitarian ideology cause the war? At the start of the chapter, Monsieur Ros gave three historians' answers. "
        "{hi.1}For A. J. P. Taylor, the war came from the failure of the democracies to stop Hitler: a very controversial thesis. "
        "{hi.2}For Paul Hehn, it was an economic conflict, born of the crash. "
        "{hi.3}For Jay Winter, 1914 to 1945 is one single thirty years' war.",
        "{-hi}{tr}Each of them holds part of the truth, and the chapter shows where. {tr.1}Winter: the regimes were born in the trenches, "
        "out of brutalisation and Versailles. {tr.2}Hehn: the crisis made the Nazis a mass party, and pushed Japan towards autarky. "
        "{tr.3}Taylor: appeasement let every aggression succeed.",
        "{-tr}{rep}But the chapter adds its own candidate, and here is the answer. {rep.g}Totalitarian ideology supplied "
        "{!the will to war}the will to war: war as a value for Fascism, Lebensraum for Nazism, a superior race for Japan. "
        "{rep.d}The democracies' reluctance supplied the opportunity: each unpunished aggression prepared the next. "
        "A strong answer keeps both halves.",
        "{-rep}{pa}Now it is your turn, with the key issue of the chapter.",
        ("P", 2.5),
        "{-pa}{mod}Here is one way to say it. {mod.1}Totalitarian ideologies made war a value and expansion a goal: Abyssinia in 1935, "
        "Lebensraum in Mein Kampf. {mod.2}But the democracies let aggression succeed: the League, American isolationism, "
        "and appeasement, from the Rhineland to Munich. {mod.3}The two combined into a chain that only war could break: "
        "after Prague and the pact, Poland.",
        "{-mod}{kt}And the key terms of the chapter. {kt.1}Totalitarianism. {kt.2}Lebensraum, living space. "
        "{kt.3}And appeasement: accepting the aggressors' demands in order to avoid war.",
    ], vis={
        "hi": dict(type="liste", titre="Three historians, three causes", items=[
            "A. J. P. Taylor (1961): the democracies' failure — “very controversial”",
            "Paul N. Hehn: an economic conflict, born of the crash",
            "Jay Winter: one “thirty years' war”, 1914 – 1945"], x=150, y=130, w=980),
        "tr": dict(type="liste", titre="What the chapter shows", marques=["W", "H", "T"], items=[
            "Winter: regimes born in the trenches — brutalisation, Versailles",
            "Hehn: the crisis made the Nazis a mass party; Japan's autarky",
            "Taylor: appeasement let every aggression succeed"], x=150, y=130, w=980),
        "rep": dict(type="cols", g="The will to war", gq="totalitarian ideology: war as a value, Lebensraum, a “superior race”",
                    d="The opportunity", dq="the democracies' reluctance: each unpunished aggression prepared the next", vs="+"),
        "pa": dict(type="pause", t="Key issue: assess the role of totalitarianism in the collapse of global peace in the late 1930s. "
                                   "Your answer in three sentences.",
                   sous="Pause the video, write your three sentences, then play on to compare."),
        "mod": dict(type="liste", titre="A model answer", items=[
            "Totalitarian ideologies made war a value: Abyssinia (1935), Lebensraum.",
            "The democracies let aggression succeed: the League, isolationism, appeasement.",
            "The two formed a chain only war could break: Prague, the pact, Poland."], x=150, y=130, w=980),
        "kt": dict(type="liste", titre="Key terms", marques=["1", "2", "3"], items=[
            "Totalitarianism: total control, coercion, transformation",
            "Lebensraum: living space, conquered in the East",
            "Appeasement: accepting the aggressors' demands to avoid war"], x=150, y=130, w=980),
    }),

    # ================================================================ fin
    dict(id="fin", chap="The end", fond="nuit", humeur="calme", beats=[
        "{fin}That is the end of the series. Go back to the course on the site, do the quiz of the chapter… "
        "and write one essay on totalitarian regimes before the exam.",
        ("P", 2.0),
    ], vis={
        "fin": dict(type="mot", t="Your turn now", g="the course, the quiz, one essay", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="Which definition of totalitarianism matches the course?",
         r=["A regime that seeks total control of society through coercion, to transform man according to an ideology",
            "A regime that only asks people to obey and keep quiet", "Any regime with a single party", "A monarchy ruled by a dictator"],
         ok=0, voir="def", ex="The key word is transformation: a dictatorship wants silence, a totalitarian regime a New Man."),
    dict(q="What is George Mosse's “brutalisation”?", r=["The violence of the trenches carried into post-war politics",
         "The harshness of the Treaty of Versailles", "Police torture in the USSR", "The mutinies of 1917"], ok=0, voir="g1",
         ex="For Mosse, WW1 is the “matrix of totalitarianism”."),
    dict(q="How did Mussolini become Prime Minister in October 1922?", r=["He was appointed by the king after the March on Rome",
         "He won a majority in the elections", "He stormed Parliament with the army", "He was chosen by the Pope"], ok=0, voir="g1",
         ex="Intimidation, then a legal appointment — the same pattern as Hitler in 1933."),
    dict(q="What was the NSDAP's best score in a free election?", r=["37.4% in July 1932", "51% in July 1932",
         "18.3% in 1928", "33.1% in March 1933"], ok=0, voir="ch", ex="The largest party, never a majority: Hindenburg appointed Hitler."),
    dict(q="What is the supreme goal of each regime?", r=["Nation (Fascism), race (Nazism), class (Stalinism)",
         "Race (Fascism), class (Nazism), nation (Stalinism)", "Class for all three", "Religion, race, nation"], ok=0, voir="l1",
         ex="Same totalitarian ambition, opposite ideologies."),
    dict(q="The Holodomor is…", r=["the man-made famine of 1932–33 in Ukraine", "the Soviet Five-Year Plan",
         "the Soviet political police", "a collective farm"], ok=0, voir="g2",
         ex="The result of forced collectivisation and of grain requisitions."),
    dict(q="Which youth organisation belongs to Fascist Italy?", r=["The Balilla", "The Komsomol", "The Hitler Youth", "The S.A."],
         ok=0, voir="l4", ex="Komsomol (USSR), Hitler Youth (Germany, compulsory from 10 to 18)."),
    dict(q="How many executions did the Great Purge of 1937–38 cause?", r=["680,000", "85", "70,000", "6 million"], ok=0, voir="l5",
         ex="85 is the Night of the Long Knives; about 70,000 the victims of T4."),
    dict(q="Which key term means “living space”?", r=["Lebensraum", "Anschluss", "Volksgemeinschaft", "Diktat"], ok=0, voir="l6",
         ex="Formulated by Ratzel (1901), turned into a plan of conquest in Mein Kampf (1925)."),
    dict(q="What ended appeasement in March 1939?", r=["Germany's occupation of Prague", "The Anschluss",
         "The Nazi-Soviet pact", "The invasion of Abyssinia"], ok=0, voir="g4",
         ex="Hitler had lied at Munich; Britain and France then guaranteed Poland."),
    dict(q="Which historian blamed the war on the democracies' failure to stop Hitler?", r=["A. J. P. Taylor", "Jay Winter",
         "Paul N. Hehn", "George Mosse"], ok=0, voir="hi", ex="Winter: the “thirty years' war”; Hehn: an economic conflict."),
    dict(q="The chapter's answer to its key issue is that…", r=["ideology supplied the will to war, the democracies' reluctance the opportunity",
         "only the crisis of 1929 caused the war", "the democracies wanted the war", "the war was an accident"], ok=0, voir="rep",
         ex="A strong answer keeps both halves."),
]

CREDITS = [
    "Content: the synthesis of M. Ros's course (DNL History, H2) as written on the site, with M. Ros's synthesis grid; "
    "the animated map of the chapter (site).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
