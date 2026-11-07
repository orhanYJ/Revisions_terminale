"""DNL History · H3 « World War Two » — série vidéo, épisode 2 : « The fall of France » (partie I.1 du cours,
« Nazi invasion of Western Europe: the French case »).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h3_2 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H3.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H3 : 6 drôle de guerre · 7 partage de la Pologne · 10 Danemark et Norvège · 11 attaque à l'ouest · 12 Ardennes ·
       13 Dunkerque · 14 chute de Paris, exode · 15 appel du 18 juin · 16 armistice, zones · 18 Vichy ·
       19 annexions soviétiques de l'été 1940 · 23 Balkans · 34 France exploitée · 35 étoile jaune et rafles ·
       39 Torch, zone libre envahie
Contenu : partie I.1 du chapitre dans le site (dnl/index.html, CHAPTERS.H3, onze idées), Worksheet 1 (H3WS1),
les cinq zones (H3Zones), les trois sources sur la France occupée (H3Sources), le tableau des divisions (H3_DIV) et
les points à vérifier (H3Check : arrestations de l'été 1942 par la police française, non par la Milice).
Ce qui n'est pas dans le cours est dit « outside the course ». Plan : d'abord la chronologie sur la carte (de la drôle
de guerre à l'invasion de la zone libre), puis le cours structuré (pourquoi la France tombe, idées 1 à 5 ; la France
occupée, idées 6 à 11), avec deux pauses « Your turn » (paragraphe d'essay, DBQ a) « How useful »).
Plan de la série H3 : 1 A world war · 2 The fall of France · 3 Britain alone · 4 Barbarossa · 5 Towards the genocide ·
6 WWII at the exam (essay and DBQ) · 7 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-2"
NOTION = "World War Two"
NUM = 2
TITRE = "The fall of France"
SUIVANT = "Episode 3 · Britain alone"
PRONONCIATION = {"Pétain": "Pay-tan", "Vichy": "Vee-shee", "Rethondes": "Ruh-tond", "Compiègne": "Kom-pyen",
                 "Wehrmacht": "Vair-markt", "Maginot": "Mah-zhee-no", "Reichsmarks": "Rikes-marks",
                 "Alsace": "Al-zass", "Moselle": "Mo-zell", "Pas-de-Calais": "Pah-duh-Kah-lay",
                 "Alpes-Maritimes": "Alp-Mah-ree-teem", "Milice": "Mee-leess", "Vel' d'Hiv": "Vel Deev",
                 "Pariser Zeitung": "Pa-ree-zer Tsy-toong", "Herrenvolk": "Hair-en-folk", "Gestapo": "Geh-stah-po",
                 "Service du travail obligatoire": "Ser-veess dü trah-vye ob-lee-gah-twahr",
                 "Rousso": "Roo-so", "Panzer": "Pants-er", "Blitzkrieg": "Blits-kreeg", "Relève": "Ruh-lev"}

# tableau des divisions du cours (H3_DIV) : 1940, 1942, 1943, 1944, 1945
ANS = [1940, 1942, 1943, 1944, 1945]
DIV_FRA = list(zip(ANS, [105, 0, 5, 7, 14]))
DIV_GB = list(zip(ANS, [34, 38, 39, 37, 31]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture2", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}The fourteenth of June 1940. German troops enter Paris. On the tenth of May, France still had "
        "one of the biggest armies in the world.",
        "{-q1}{q2}So how could it collapse in only six weeks? That is the first question of this episode.",
        "{-q2}{q3}And the second: what did Germany do with France afterwards? Occupation, collaboration, exploitation, "
        "persecution. France is the first case study of the New European Order.",
        "{-q3}{-g0}{plan}The plan. {plan.1}The story on the map. {plan.2}Why France fell. {plan.3}Dunkirk and the defeat. "
        "{plan.4}France cut up, and Vichy. {plan.5}Exploitation and persecution. {plan.6}And practice for the essay and the DBQ.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[14]),
        "q1": dict(type="question", t="14 June 1940: the Germans enter Paris.", bande=True),
        "q2": dict(type="question", t="How could France fall in six weeks?", bande=True),
        "q3": dict(type="question", t="And what did Germany do with France?", bande=True),
        "plan": dict(type="liste", titre="Episode 2 · Part I.1 of the course", items=[
            "The story on the map: 1939 – 1942", "Why France fell: strategy and Blitzkrieg",
            "Dunkirk, defeat, exodus", "France cut up; the Vichy regime",
            "Exploited, persecuted, repressed, seduced", "Essay and DBQ practice"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 2", t="The fall of France",
                      sous="May 1940 – November 1942 · defeat · occupation · collaboration"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="sixsemaines", chap="Six weeks on the map", fond="nuit", humeur="tension",
         retenir="Phoney war (Sept. 1939 – May 1940) · 10 May: the attack · 13–20 May: the Ardennes · 26 May – 4 June: Dunkirk · 14 June: Paris falls.",
         beats=[
        "{g1}Let's follow the story on the map first. {g1.1}September 1939: after the invasion of Poland, Britain and France "
        "declare war on Germany. And then… almost nothing. The French army waits behind the Maginot Line: this is the phoney war.",
        "{g1.2}April 1940: Germany strikes first in the north. It occupies Denmark and invades Norway.",
        "{g1.3}The tenth of May 1940: the real attack. The German army invades the Netherlands, Belgium and Luxembourg. "
        "And the same day, in London, Winston Churchill becomes prime minister.",
        "{g1.4}From the thirteenth to the twentieth of May: the surprise. German tanks come through the Ardennes forest, "
        "break through the French lines and race to the Channel coast. The best Allied troops, sent into Belgium, are trapped in the north.",
        "{g1.5}From the twenty-sixth of May to the fourth of June: Dunkirk. Operation Dynamo takes 338,000 Allied soldiers "
        "across the Channel to England.",
        "{g1.6}Then comes the offensive from the Somme towards Paris. The French government leaves the capital, "
        "and on the fourteenth of June 1940, Paris falls. Some eight million civilians flee south: {!the exodus}the exodus.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[6, 10, 11, 12, 13, 14]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="armistice", chap="Armistice and zones", fond="nuit", humeur="tension",
         retenir="18 June 1940: de Gaulle's appeal · 22 June: armistice at Rethondes, France cut up · Vichy collaborates · 11 Nov. 1942: the free zone invaded.",
         beats=[
        "{g2}The government is now led by Marshal Pétain, one of the victors of the First World War, and he asks for an armistice. "
        "One general refuses: Charles de Gaulle. He flees to London, and on the eighteenth of June, on BBC radio, "
        "he calls on the French to fight on. Listen to how his appeal ends.{-g2}",
        ("C", "the flame of French resistance must not and shall not die", "c_gaulle"),
        "{-c_gaulle}{g2b}{g2b.1}But on the twenty-second of June 1940, at Rethondes, in the forest of Compiègne, France signs the armistice. "
        "And the country is cut up: an occupied zone, in the north and along the whole Atlantic coast; "
        "and a so-called free zone in the south, governed from Vichy.",
        "{g2b.2}In that free zone, Marshal Pétain sets up a new regime in the spa town of Vichy: an authoritarian French State, "
        "which chooses to collaborate with Germany.",
        "{g2b.3}This division lasts two years. On the eighth of November 1942, the Allies land in French North Africa: "
        "Operation Torch. In response, on the eleventh of November, German forces invade the free zone, "
        "and Italian troops occupy a large part of the south-east. From now on, the whole of France is occupied.",
        "{-g2b}{dates}So, before the course itself, here are the dates to copy. Pause the video if you need to.",
        ("P", 5.0),
    ], vis={
        "g2": dict(type="globe", code="H3", sc=[15]),
        "g2b": dict(type="globe", code="H3", sc=[16, 18, 39]),
        "c_gaulle": dict(type="cit", a="Charles de Gaulle", o="appeal of 18 June 1940, BBC, London", x=200, y=190, w=880),
        "dates": dict(type="liste", titre="The dates to know", petit=True, items=[
            "Sept. 1939 – May 1940 · the phoney war", "10 May 1940 · the German attack; Churchill prime minister",
            "13–20 May · the breakthrough in the Ardennes", "26 May – 4 June · Dunkirk, Operation Dynamo",
            "14 June · Paris falls; the exodus", "22 June · the armistice at Rethondes",
            "11 Nov. 1942 · the free zone invaded (after Torch)"], x=170, y=100, w=940),
    }),

    # ================================================================ III. l'Europe submergée (idée 1)
    dict(id="europe41", chap="Europe overrun, 1939–1941", fond="nuit", humeur="tension",
         retenir="1939–1941: Germany and the USSR attack first; the Axis overruns continental Europe; the USSR takes a share of the east; only Britain still resists.",
         beats=[
        "{g3}Now the course, idea by idea. It starts with a map of Europe between 1939 and 1941, and in the exam you may be asked to describe it. "
        "{g3.1}Germany and the Soviet Union are the two powers that attack first, in 1939. In September, they share Poland between them.",
        "{g3.2}The USSR goes on taking its share of eastern Europe: in the summer of 1940, it annexes the Baltic states "
        "and takes Bessarabia from Romania.",
        "{g3.3}And by the spring of 1941, the Axis has made rapid progress everywhere: Yugoslavia and Greece are invaded, "
        "while Hungary, Romania and Bulgaria side with Germany.",
        "{-g3}{l1}So, the situation to describe. {l1.1}Continental Europe is overcome by the Axis. "
        "{l1.2}The USSR has taken a share of eastern Europe. {l1.3}And in 1941, only Britain still resists. "
        "{l1.4}The example to quote: Belgium, the Netherlands, Luxembourg and France overrun in six weeks from May 1940.",
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[7, 19, 23]),
        "l1": dict(type="liste", titre="Europe, 1939 – 1941", cles=["Axis", "share", "Britain"], items=[
            "The Axis overruns continental Europe", "The USSR takes a share of the east",
            "1941: only Britain still resists", "Example: four countries overrun in six weeks"], x=170, y=130, w=940),
    }),

    # ================================================================ IV. une armée immense, une stratégie dépassée (idée 2)
    dict(id="strategie", chap="A huge army, an old strategy", fond="nuit", humeur="calme",
         retenir="France: 105 divisions in 1940, Britain 34. But an army led by the victors of WWI, a defensive strategy, the Maginot Line (not on the Belgian border), the phoney war.",
         beats=[
        "{q5}First paradox. In 1940, France had one of the biggest armies in the world. So the defeat was not a question of numbers.",
        "{-q5}{gr}Look at the course table of divisions. {gr.1}France: 105 divisions in 1940. {gr.2}Britain: only 34. "
        "Remember from episode one: the Allies had 393 divisions in all, against 272 for the Axis. "
        "{gr.3}And now look at France in 1942: zero. In two years, the French army has disappeared.",
        "{-gr}{def3}So what went wrong? This army was led by the victors of the First World War, and it was not very modern. "
        "And France and Britain chose a {!defensive strategy}defensive strategy. {def3.1}Their plan: avoid a new trench war and its death toll, "
        "and withstand a massive German attack behind fortifications.",
        "{-def3}{mag}The symbol of this strategy is the Maginot Line: a sophisticated chain of fortifications along the border with Germany. "
        "{mag.1}But it had one weakness, and it was fatal: it did not cover the Franco-Belgian border.",
        "{-mag}{drole}And so, from September 1939 to May 1940, France and Britain wait: war declared, but almost no fighting. "
        "{drole.1}The phoney war.",
    ], vis={
        "q5": dict(type="question", t="One of the biggest armies in the world… beaten in six weeks?"),
        "gr": dict(type="graphe", titre="Divisions available (course table)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1939.5, 1945.5], y=[0, 120], gx=ANS, gy=[20, 40, 60, 80, 100], lx="year", ly="divisions"),
                   el=[dict(type="point", x=1940, y=105, c="el", lbl="France 1940: 105", lp=[1941.3, 98], proj=True),
                       dict(type="point", x=1940, y=34, c="vert", lbl="Britain: 34", lp=[1940.7, 40]),
                       dict(type="courbe", pts=[list(p) for p in DIV_FRA], c="ca", lbl="France: 0 in 1942", lp=[1943.0, 26], dur=2.0)]),
        "def3": dict(type="def", cles=["trench", "withstand", "fortifications"], terme="A defensive strategy",
                     t="Avoid a new trench war and its death toll; withstand a massive German attack behind fortifications.",
                     etape="An army led by the victors of WWI, and not very modern", x=170, y=200, w=940),
        "mag": dict(type="def", cles=["fortifications", "Germany"], terme="The Maginot Line",
                    t="A sophisticated chain of fortifications along the French border with Germany.",
                    etape="Its weakness: it did not cover the Franco-Belgian border.", x=170, y=200, w=940),
        "drole": dict(type="def", cles=["declared", "fighting"], terme="The phoney war · Sept. 1939 – May 1940",
                      t="War declared, but almost no fighting in the west.",
                      etape="France waits for the attack behind the Maginot Line.", x=170, y=200, w=940),
    }),

    # ================================================================ V. la Blitzkrieg par les Ardennes (idée 3)
    dict(id="ardennes", chap="Blitzkrieg through the Ardennes", fond="guerre", humeur="tension",
         retenir="Blitzkrieg: tanks and aircraft for a rapid victory. The Allies expected central Belgium, as in 1914; the attack came through the Ardennes (13–20 May 1940).",
         beats=[
        "{def4}Germany, on the other hand, wants a rapid victory. Its method is the {!Blitzkrieg}Blitzkrieg, the lightning war: "
        "a rapid offensive combining tanks and aircraft. {def4.1}Air raids had already been tested in Belgium and in the Netherlands.",
        "{-def4}{cmp1}And Germany adds surprise. {cmp1.g}The British and French commanders believed the Germans would attack through central Belgium, "
        "as in 1914. So, on the tenth of May, they rushed their best forces there. "
        "{cmp1.d}But the main attack went through the hilly Ardennes forest, in south-eastern Belgium and northern Luxembourg: "
        "exactly where nobody expected it.",
        "{-cmp1}{g4}{g4.1}Between the thirteenth and the twentieth of May, the German tanks come out of the Ardennes, "
        "break through the French lines, and advance to the Channel coast. Erwin Rommel's Seventh Panzer Division "
        "crosses the French countryside towards the Somme.",
        "The best Allied forces, in Belgium, are now cut off from the rest of France. {!A trap}It is a trap.",
    ], vis={
        "def4": dict(type="def", cles=["rapid", "tanks", "aircraft"], terme="Blitzkrieg · “lightning war”",
                     t="A rapid offensive combining tanks and aircraft, to win a quick victory.",
                     etape="Air raids already tested in Belgium and the Netherlands", x=170, y=200, w=940),
        "cmp1": dict(type="cols", g="Expected", gq="an attack through central Belgium, as in 1914", d="Reality",
                     dq="the main attack through the hilly Ardennes forest", vs="≠", repere="10 May: the best Allied forces rushed into Belgium"),
        "g4": dict(type="globe", code="H3", sc=[12]),
    }),

    # ================================================================ VI. Dunkerque (idée 4)
    dict(id="dunkerque", chap="Dunkirk", fond="nuit", humeur="tension",
         retenir="Operation Dynamo, 26 May – 4 June 1940: 338,000 Allied soldiers evacuated. A betrayal for the French; for Britain, the Royal Navy and the RAF saved.",
         beats=[
        "{g5}{g5.1}Trapped against the coast, the British Expeditionary Force organises a hasty evacuation by sea: {!Operation Dynamo}Operation Dynamo. "
        "From the twenty-sixth of May to the fourth of June 1940, 338,000 Allied soldiers are lifted from the beaches of Dunkirk to Britain.",
        "{-g5}{cols2}Was Dunkirk a defeat or a success? It depends on where you stand. "
        "{cols2.g}For the French troops, it was a betrayal: their ally was sailing home and leaving them to fight alone. "
        "{cols2.d}For Britain, it saved what mattered: the Royal Navy and the RAF were intact.",
        "{-cols2}{chu}And Winston Churchill, prime minister since the tenth of May, the very day of the German attack, "
        "insisted that Britain would fight on, later, with American aid. On the fourth of June, he tells the House of Commons:{-chu}",
        ("C", "we shall fight on the beaches … we shall never surrender", "c_church"),
        "{-c_church}A speech for episode three.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[13]),
        "cols2": dict(type="cols", g="For the French", gq="a betrayal: the British leave them to fight alone", d="For Britain",
                      dq="the army saved; the Royal Navy and the RAF intact", vs="≠"),
        "chu": dict(type="note", terme="Churchill · prime minister from 10 May 1940", cles=["fight", "American"],
                    t="Britain will fight on, and win later, with American aid.", x=170, y=470, w=940),
        "c_church": dict(type="cit", a="Winston Churchill", o="House of Commons, 4 June 1940", x=200, y=150, w=880),
    }),

    # ================================================================ VII. la défaite en six semaines (idée 5)
    dict(id="defaite", chap="Defeat in six weeks", fond="guerre", humeur="tension",
         retenir="Paris falls on 14 June 1940. ≈ 100,000 French soldiers killed (recent research: ≈ 60,000), 200,000 wounded, 1,850,000 prisoners; 8 million on the roads. Armistice: 22 June, Rethondes.",
         beats=[
        "{g6}{g6.1}From the fifth of June, the German forces strike from the Somme towards Paris. The government flees the capital, "
        "and Paris falls on the fourteenth, five weeks after the campaign began. Millions of panic-stricken civilians take the roads south.",
        "{-g6}{toll}The human cost is huge. {toll.1}About 100,000 French soldiers killed in combat, according to the course; "
        "recent research says about sixty thousand. {toll.2}200,000 wounded. "
        "{toll.3}1,850,000 taken prisoner. Keep that figure in mind: it comes back with the STO. "
        "{toll.4}And some eight million people in the exodus.",
        "{-toll}{arm}On the twenty-second of June 1940, France signs an armistice at Rethondes, in the forest of Compiègne. "
        "{arm.1}Not a peace treaty: an agreement that ends the fighting. And Britain is now alone against Germany.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[14]),
        "toll": dict(type="liste", titre="The cost of six weeks (course figures)", items=[
            "≈ 100,000 French soldiers killed (recent research: ≈ 60,000)", "200,000 wounded", "1,850,000 prisoners of war",
            "≈ 8 million civilians in the exodus"], x=170, y=130, w=940),
        "arm": dict(type="def", cles=["ends", "fighting"], terme="Armistice · 22 June 1940, Rethondes",
                    t="An agreement that ends the fighting, signed by France in the forest of Compiègne.",
                    etape="Not a peace treaty · Britain is now alone against Germany", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. Worksheet 1 et premier « Your turn »
    dict(id="worksheet1", chap="Worksheet 1: two strategies", fond="aube", humeur="calme",
         retenir="Why France fell: an old defensive strategy (Maginot Line, phoney war), the surprise of the Ardennes (13–20 May), the Blitzkrieg of tanks and aircraft (Rommel's 7th Panzer).",
         beats=[
        "{ws_plan}Worksheet one sums all this up in a table: two sides face to face, and three rows. "
        "{ws_plan.g}Row one, the plan. For France, Britain and their allies: avoid a new trench war and its death toll, "
        "and withstand a massive German attack. {ws_plan.d}For Nazi Germany: a rapid victory through Blitzkrieg.",
        "{-ws_plan}{ws_meth}Row two, the methods. {ws_meth.1}Allied side: the Maginot Line and the phoney war. "
        "{ws_meth.2}Then the best forces sent into central Belgium; Dunkirk; and the hope of a later British intervention, with American aid. "
        "{ws_meth.3}German side: the breakthrough through the Ardennes to the Channel, and air raids already tested. "
        "{ws_meth.4}Then the offensive from the Somme to Paris, from the fifth to the thirteenth of June.",
        "{-ws_meth}{ws_res}Row three, the outcome. {ws_res.g}For France: the government leaves Paris for Vichy, under Pétain, "
        "and the human cost you know. {ws_res.d}For Germany: Paris occupied on the fourteenth of June, and the armistice of Rethondes.",
        "{-ws_res}{pa1}Now it's your turn. An essay question you could get: explain why France was defeated so quickly in 1940. "
        "Write one paragraph, with three reasons and one precise example for each.",
        ("P", 2.0),
        "{-pa1}{rep1}Here is one way to write it. {rep1.1}France was defeated in six weeks for three main reasons. "
        "First, it relied on an old defensive strategy: the Maginot Line protected the border with Germany but not the Belgian border, "
        "and during the phoney war the army simply waited. "
        "{rep1.2}Second, the Germans attacked where nobody expected them: while the best Allied forces rushed into central Belgium, "
        "the tanks came through the Ardennes, between the thirteenth and the twentieth of May. "
        "{rep1.3}Third, the Blitzkrieg combined tanks and aircraft in a rapid offensive: Rommel's Seventh Panzer Division raced towards the Somme. "
        "{rep1.4}So the defeat was not a matter of numbers, since France had 105 divisions, but of strategy and surprise.",
    ], vis={
        "ws_plan": dict(type="cols", g="Allies · the plan", gq="avoid a new trench war; withstand a massive attack",
                        d="Germany · the plan", dq="a rapid victory through Blitzkrieg", vs="vs", repere="Worksheet 1 · row 1"),
        "ws_meth": dict(type="liste", titre="Worksheet 1 · row 2: the methods", petit=True, items=[
            "Allies: the Maginot Line (no Belgian border); the phoney war",
            "Allies: best forces into central Belgium (10 May); Dunkirk, 338,000 evacuated",
            "Germany: armoured breakthrough via the Ardennes to the Channel (13–20 May); air raids tested",
            "Germany: offensive from the Somme to Paris (5–13 June)"], x=170, y=140, w=940),
        "ws_res": dict(type="cols", g="Allies · outcome", gq="government to Vichy (Pétain); ≈ 100,000 dead, 1,850,000 POWs; 8 million in the exodus",
                       d="Germany · outcome", dq="Paris occupied, 14 June; armistice, 22 June", vs="vs", repere="Worksheet 1 · row 3"),
        "pa1": dict(type="pause", t="Essay paragraph: explain why France was defeated so quickly in 1940.",
                    sous="Three reasons, one precise example each. Pause the video, write, then play on for a model."),
        "rep1": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "An old defensive strategy → Maginot Line, phoney war",
            "Surprise → the Ardennes, 13–20 May, while the Allies rushed into Belgium",
            "Blitzkrieg → tanks and aircraft; Rommel's 7th Panzer towards the Somme",
            "Conclusion: not numbers (105 divisions), but strategy and surprise"], x=170, y=140, w=940),
    }),

    # ================================================================ IX. la France découpée (idée 6)
    dict(id="zones", chap="France cut into zones", fond="nuit", humeur="tension",
         retenir="Five zones: occupied (3/5, MBF), “free” (Vichy), Italian (≈ 15 communes), Nord–Pas-de-Calais (Brussels), Alsace-Moselle annexed. The free zone invaded on 11 Nov. 1942.",
         beats=[
        "{g7}{g7.1}Now, occupied France. The armistice cuts the country into five zones, each with a different master.",
        "{zones}{zones.1}One: the occupied zone. Germany occupies three fifths of mainland France: the areas with the highest economic potential, "
        "and the Atlantic and northern coasts, to watch for any landing. It is run by a German Military Command, the MBF. "
        "{zones.2}Two: the so-called free zone, in the south, governed from Vichy. A {!demarcation line}demarcation line separates the two, "
        "like a border inside the country.",
        "{zones.3}Three: a small Italian zone, about fifteen communes, mainly in the Alpes-Maritimes. "
        "{zones.4}Four: the Nord and the Pas-de-Calais, attached to the German Military Command in Brussels. "
        "{zones.5}And five: Alsace and Moselle, annexed outright to Germany. Back to the borders of 1871.",
        "{-zones}{g7.2}Why put quotation marks around the word free? Because this freedom does not last. On the eleventh of November 1942, "
        "after the Allied landing in French North Africa, Operation Torch, German forces invade the free zone. "
        "And from November 1942 to September 1943, Italian troops occupy a much larger part of the south-east.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[16, 39]),
        "zones": dict(type="liste", titre="France cut up: five zones", x=905, y=24, w=362, petit=True, bande=True, items=[
            "Occupied zone: 3/5, the richest areas and the coasts (MBF)", "“Free zone”, governed from Vichy",
            "Italian zone: ≈ 15 communes (Alpes-Maritimes)", "Nord and Pas-de-Calais: attached to Brussels",
            "Alsace and Moselle: annexed (borders of 1871)"]),
    }),

    # ================================================================ X. Vichy (idée 7)
    dict(id="vichy", chap="Vichy: a state that chose to collaborate", fond="guerre", humeur="tension",
         retenir="Vichy: Pétain's authoritarian French State, keen to collaborate. Oct. 1940: decree defining who is a Jew; March 1941: Office for Jewish Affairs. De Gaulle: Free France, from London.",
         beats=[
        "{photo1}{def5}In the free zone, a new government takes over, led by Marshal Pétain, and established in the spa town of Vichy. "
        "{def5.1}It calls itself the French State, and it is an authoritarian regime.",
        "{-def5}{collab}From the armistice onwards, it seeks {!collaboration}collaboration with the German authorities. "
        "Behind, the image of it: Pétain shaking Hitler's hand at Montoire, in October 1940, a meeting outside the course. "
        "And be careful with the nuance the course makes. {collab.1}Vichy is under Nazi pressure, yes. But it is often keen to collaborate.",
        "{-collab}{antij}The proof: Vichy begins persecuting Jews even before the Germans demand it. "
        "{antij.1}In October 1940, a Vichy decree defines who is a Jew, and limits their place in French society. "
        "{antij.2}In March 1941, Vichy creates an Office for Jewish Affairs. "
        "{antij.3}These are French initiatives, not German orders. That is a precise, powerful argument in any essay on collaboration.",
        "{-antij}{-photo1}{dg}Facing Vichy, one man says no. {dg.g}On one side, Vichy: Pétain and collaboration. "
        "{dg.d}On the other, London: General de Gaulle, who rejected the surrender and launched Free France.",
    ], vis={
        "photo1": dict(type="tableau", img="h3-montoire", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .3, .45],
                       legende="Pétain shakes Hitler's hand, Montoire, 24 October 1940 (outside the course) · Heinrich Hoffmann, Bundesarchiv, Bild 183-H25217, CC BY-SA 3.0 DE"),
        "def5": dict(type="def", cles=["Pétain", "Vichy"], terme="The Vichy regime",
                     t="Marshal Pétain's new government, established in the spa town of Vichy.",
                     etape="“The French State”: an authoritarian regime", x=170, y=200, w=940),
        "collab": dict(type="note", terme="Watch the nuance", cles=["pressure", "keen"],
                       t="Collaboration: sought by Vichy from the armistice onwards.",
                       etape="Under Nazi pressure… but often keen to collaborate.", x=170, y=200, w=940),
        "antij": dict(type="liste", titre="Before the Germans demanded it", cles=["decree", "Office", "initiatives"], items=[
            "October 1940: a decree defines who is a Jew", "March 1941: an Office for Jewish Affairs",
            "French initiatives, not German orders"], x=170, y=150, w=940),
        "dg": dict(type="cols", g="Vichy", gq="Marshal Pétain · an authoritarian state · collaboration", d="London",
                   dq="General de Gaulle · Free France · resistance", vs="≠"),
    }),

    # ================================================================ XI. la France exploitée (idée 8)
    dict(id="exploitation", chap="France exploited", fond="nuit", humeur="tension",
         retenir="Exploitation: 20 million Reichsmarks a day, requisitions (coal, food, fuel), rationing and black market. Workers: the Relève (June 1942), then forced labour, the STO (Feb. 1943), created by Vichy: men 18–50, single women 21–35.",
         beats=[
        "{g9}{g9.1}For Germany, France is above all a resource. The occupation is first of all an economic exploitation. "
        "{expl}{expl.1}Money: France must pay heavy occupation fees, twenty million Reichsmarks a day. "
        "{expl.2}This money finances German requisitions, and the plundering of French resources: coal, food, fuel. "
        "{expl.3}The result for the French: rationing, and a {!black market}black market. "
        "{expl.4}And workers: from 1942, French workers are sent to Germany, first as volunteers, then, from February 1943, as forced labour, with the STO.",
        "{-expl}{-g9}{sto}Look closely at the STO, the Service du travail obligatoire: it was created by Vichy, not by Germany. {sto.1}Under the labour law of September 1942 and the STO law of February 1943, all able-bodied men aged eighteen to fifty, "
        "and single women aged twenty-one to thirty-five, could be sent.",
        "Before that, from June 1942, the Relève had promised to free one French prisoner of war for every three volunteer workers. Remember the 1,850,000 prisoners of 1940: "
        "here they are, used as a bargaining tool.",
    ], vis={
        "g9": dict(type="globe", code="H3", sc=[34]),
        "expl": dict(type="liste", titre="Exploited: money, goods, workers", x=850, y=330, w=400, petit=True, bande=True, items=[
            "20 million Reichsmarks a day in occupation fees", "Requisitions: coal, food, fuel",
            "Rationing and the black market", "1942: the Relève; Feb. 1943: the STO, forced labour"]),
        "sto": dict(type="def", cles=["Vichy", "women"], terme="STO · Service du travail obligatoire",
                    t="Created by Vichy in February 1943: French workers sent to Germany as forced labour.",
                    etape="Men aged 18–50, single women aged 21–35 · before it, the Relève (June 1942): one POW freed for three volunteers", x=170, y=200, w=940),
    }),

    # ================================================================ XII. les Juifs persécutés (idée 9)
    dict(id="persecution", chap="Persecuted, dispossessed, deported", fond="guerre", humeur="tension",
         retenir="≈ 350,000 Jews in France in 1940. Aryanisation, the yellow star (June 1942), arrests from summer 1942 by the French police. ≈ 80,000 deported; about 3% survived.",
         beats=[
        "{g10}{g10.1}In 1940, about 350,000 Jews live in France, more than half of them foreign refugees. In the occupied zone, "
        "they face immediate persecution, comparable to that in Poland. {pers}It happens in steps. "
        "{pers.1}Dispossession: under the {!Aryanisation}Aryanisation laws, their businesses and property are confiscated, "
        "and families are left without home or work. {pers.2}Marking: from June 1942, they must wear the yellow star. "
        "{pers.3}Arrest: from the summer of 1942, they are arrested for deportation to the east, mainly by the French police. "
        "{pers.4}And from 1942, Jews are deported from the Vichy zone too.",
        "{-pers}{-g10}{bilj}The toll: some 80,000 Jews deported from France during the war. Only about three per cent of them survived.",
        "{-bilj}{milice}A warning: the course makes a mistake here. It says the arrests of 1942 were carried out by the Milice. {milice.1}But the Milice was only created in January 1943. The great round-up of July 1942 in Paris, "
        "the Vel' d'Hiv round-up, on the sixteenth and seventeenth of July, was the work of the French police. "
        "In your essay, write: the French police.",
    ], vis={
        "g10": dict(type="globe", code="H3", sc=[35]),
        "pers": dict(type="liste", titre="Persecution, step by step", x=850, y=70, w=400, petit=True, bande=True, items=[
            "Dispossession: “Aryanisation” of businesses and property", "Marking: the yellow star, June 1942",
            "Arrest for deportation, summer 1942: the French police", "From 1942: deportations from the Vichy zone too"]),
        "bilj": dict(type="mot", t="≈ 80,000 deported", g="Jews deported from France · about 3% survived", y=250, taille=96),
        "milice": dict(type="note", terme="Watch out · an error in the course", cles=["Milice", "police"],
                       t="Not “the Milice” (created only in January 1943), but the French police.",
                       etape="Vel' d'Hiv round-up, Paris, 16–17 July 1942", x=170, y=200, w=940),
    }),

    # ================================================================ XIII. répression et séduction (idée 10)
    dict(id="seduction", chap="Repression and seduction", fond="nuit", humeur="mystere",
         retenir="Terror for opponents (Jews, communists, “terrorists”: Gestapo and Vichy police); flattery for the rest. The Observer, 7 Sept. 1941: winning Paris “by flattery instead of by repression”.",
         beats=[
        "{cols3}The occupier uses two weapons at the same time. {cols3.g}Terror for opponents. Jews, communists and “terrorists”, "
        "the occupier's word for Resistance fighters, are targeted both by the Gestapo and by Vichy's police forces. "
        "{cols3.d}And flattery for everyone else. German propaganda praises French culture, flatters French business, "
        "and presents collaboration as the natural place of France in the new Europe.",
        "{-cols3}{obs}A British newspaper saw this very clearly. On the seventh of September 1941, the weekly The Observer "
        "described the Pariser Zeitung, a German-language daily published in Paris. {obs.1}It presented Paris as the future holiday resort "
        "of the Nazi Herrenvolk, the master race. And collaboration was its daily theme. "
        "The Observer's conclusion: the Germans were trying to win Paris…{-obs}",
        ("C", "by flattery instead of by repression", "c_obs"),
        "{-c_obs}So repression and seduction work together: terror for the few who resist, flattery for the many.",
    ], vis={
        "cols3": dict(type="cols", g="Repression", gq="Jews, communists, “terrorists”: the Gestapo and Vichy's police",
                      d="Seduction", dq="praise French culture, flatter business, sell collaboration", vs="+"),
        "obs": dict(type="note", terme="The Observer · 7 September 1941", cles=["Paris", "collaboration"],
                    t="The German-run Pariser Zeitung presents Paris as the holiday resort of the Nazi “Herrenvolk”.",
                    etape="“Collaboration”: its daily theme", x=170, y=200, w=940),
        "c_obs": dict(type="cit", a="The Observer", o="7 September 1941, on the Pariser Zeitung", x=200, y=220, w=880),
    }),

    # ================================================================ XIV. trois sources sur la France occupée
    dict(id="sources", chap="Life in occupied France: three sources", fond="aube", humeur="calme",
         retenir="Source 1 (The Observer, 1941): division and seduction · Source 2 (Aryanisation poster, 1942): persecution, ≈ 10,000 businesses · Source 3 (STO poster, 1943): exploitation organised by Vichy.",
         beats=[
        "{src}The course then gives you three sources on life in occupied France. The task: find in each one the division of the territory, "
        "and the policies of repression or persecution. {src.1}Source one: the Observer article we have just read, September 1941. "
        "{src.2}Source two: an Aryanisation poster, Paris, April 1942: a Jewish-owned shop handed to a non-Jewish provisional administrator. "
        "{src.3}Source three: an STO propaganda poster, 1943, calling on the French to go and work in Germany.",
        "{-src}{srep}And the answers. {srep.1}Source one shows the division of the territory: the paper does not circulate in the unoccupied zone, "
        "and treats the Vichy press as the press of a foreign country. Its line is anti-British, anti-communist and antisemitic. "
        "But above all, it shows seduction.",
        "{srep.2}Source two shows persecution: dispossession, decided by the Germans in October 1940 in the occupied zone, "
        "then made mandatory by Vichy in July 1941 in the rest of France. The historian Henry Rousso counts about ten thousand Aryanised businesses: "
        "racial measures also served economic exploitation.",
        "{srep.3}Source three shows exploitation and constraint: Vichy's own labour laws: September 1942, signed by Pétain; February 1943, the STO, signed by Laval. Collaboration served the German war effort.",
    ], vis={
        "src": dict(type="liste", titre="Life in occupied France · three sources", items=[
            "The Observer, 7 September 1941", "An “Aryanisation” poster, Paris, April 1942",
            "An STO propaganda poster, 1943"], x=170, y=150, w=940),
        "srep": dict(type="liste", titre="The answers", petit=True, items=[
            "Source 1 → division (not sold in the free zone; Vichy press as “foreign”), an antisemitic line, above all seduction",
            "Source 2 → persecution: Aryanisation (Oct. 1940, then Vichy, July 1941); ≈ 10,000 businesses (Henry Rousso)",
            "Source 3 → exploitation: labour laws of Sept. 1942 (Pétain) and Feb. 1943 (STO, Laval); Vichy organises forced labour"], x=150, y=140, w=980),
    }),

    # ================================================================ XV. le DBQ : « How useful… ? »
    dict(id="dbq", chap="DBQ: how useful is Source 1?", fond="aube", humeur="calme",
         retenir="DBQ a): judgement in the first line, the document in one sentence, strengths (several arguments), limits (several arguments).",
         beats=[
        "{dbq}Your turn again, with a DBQ. How useful is Source 1 for understanding German policy in occupied France? The structure: {dbq.q1}your judgement in the first line, "
        "{dbq.q2}the document presented in one sentence, {dbq.q3}a paragraph of strengths, with several arguments, "
        "{dbq.q4}and a paragraph of limits, with several arguments.",
        "{-dbq}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}Here is a model. {rep2.1}Source 1 is significantly useful for understanding German policy in occupied France. "
        "{rep2.2}It is an article from The Observer, a British weekly, published on the seventh of September 1941, "
        "which describes the Pariser Zeitung, a German-language daily published in Paris.",
        "{rep2.3}Its strengths. First, it reveals the strategy of seduction: Paris as the future holiday resort of the Herrenvolk, "
        "collaboration as the daily theme. Second, it shows the division of the territory: the paper is not sold in the unoccupied zone. "
        "Third, it shows the occupier's line: anti-British, anti-communist and antisemitic. And it was written during the occupation itself.",
        "{rep2.4}Its limits. First, it is a British, hence hostile, view of German propaganda. "
        "Second, it describes one Paris newspaper, not the whole of France, and not Vichy. "
        "Third, it shows what the propaganda wanted, not what the French thought of it. "
        "And it says nothing about the twenty million Reichsmarks a day, the STO or the round-ups of 1942.",
    ], vis={
        "dbq": dict(type="exo", niveau="dbq", titre="How useful is Source 1 for understanding German policy in occupied France?",
                    src="Source 1 · The Observer (British weekly), 7 September 1941, on the Pariser Zeitung",
                    enonce=["The German-run Pariser Zeitung presents Paris as the future holiday resort of the Nazi “Herrenvolk”; "
                            "“collaboration” is its daily theme: an attempt to win Paris “by flattery instead of by repression”."],
                    questions=["Judgement in the first line: largely / significantly / partly / slightly useful",
                               "The document presented in one sentence",
                               "Strengths: several arguments", "Limits: several arguments"]),
        "pa2": dict(type="pause", t="DBQ a): how useful is Source 1 for understanding German policy in occupied France?",
                    sous="Judgement, presentation, strengths, limits. Pause the video, write, then play on for a model."),
        "rep2": dict(type="liste", titre="A model answer", petit=True, items=[
            "Judgement: significantly useful", "Document: The Observer, British weekly, 7 Sept. 1941, on the Pariser Zeitung",
            "Strengths: seduction (Herrenvolk, “collaboration”); division; the antisemitic line; written at the time",
            "Limits: a hostile British view; one Paris paper; aims, not reception; nothing on money, STO, round-ups"],
                     x=150, y=130, w=980),
    }),

    # ================================================================ XVI. conclusion sur la France (idée 11)
    dict(id="casparticulier", chap="A special case", fond="nuit", humeur="lumiere",
         retenir="France, a special case: decision-making not unified (occupier and Vichy). Repression, racism and resources for total war: 20 million RM a day, the STO, ≈ 80,000 Jews deported.",
         beats=[
        "{q6}So, to conclude: why is France a special case?",
        "{-q6}{def6}Because decision-making was not unified. German occupation forces and French authorities coexisted: "
        "{!two masters}two masters on the same territory.",
        "{-def6}{trois}And yet, from France, you can see what the New European Order was for. {trois.1}Repression and terror against opponents, "
        "used both by the Nazis and by Vichy. {trois.2}Racist policies, implemented by both. "
        "{trois.3}And the use of French territory and population to supply Germany with the human, material and financial resources "
        "it needed for total war.",
        "{-trois}{chif}Three figures sum it up. {chif.1}Twenty million Reichsmarks a day: the money. {chif.2}The Relève, then the STO: the workers. "
        "{chif.3}Some 80,000 Jews deported: the racial policy.",
        "{-chif}{lien2}That is the fifth driving force of the New European Order, from episode one: supplying total war. "
        "In the West, France is exploited, but treated as a partner on the surface. In the East, episode four, it is a war of annihilation.",
    ], vis={
        "q6": dict(type="question", t="Why is France a special case?"),
        "def6": dict(type="def", cles=["unified", "coexisted"], terme="A special case",
                     t="Decision-making was not unified: German occupation forces and French authorities coexisted.",
                     etape="Two masters on the same territory", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="The New European Order seen from France", cles=["terror", "Racist", "resources"], items=[
            "Repression and terror: Nazis and Vichy", "Racist policies: implemented by both",
            "Resources for total war: people, goods, money"], x=170, y=150, w=940),
        "chif": dict(type="liste", titre="Three figures, three dimensions", items=[
            "20 million Reichsmarks a day → the money", "The Relève (1942), the STO (1943) → the workers",
            "≈ 80,000 Jews deported → the racial policy"], x=170, y=150, w=940),
        "lien2": dict(type="cols", g="In the West", gq="France exploited, a “partner” on the surface", d="In the East",
                      dq="a war of annihilation (episode 4)", vs="≠"),
    }),

    # ================================================================ récap
    dict(id="recap2", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Why France fell: 105 divisions, but an old defensive strategy, against the Blitzkrieg and the surprise of the Ardennes. "
        "{carte.2}Six weeks: Dunkirk, Paris on the fourteenth of June, the exodus, the armistice on the twenty-second. "
        "{carte.3}France cut into five zones, and Vichy, keen to collaborate, until November 1942. "
        "{carte.4}And France exploited and persecuted: twenty million Reichsmarks a day, the STO, the yellow star, eighty thousand Jews deported.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: Britain alone. From the fourth of June 1940, Churchill's island faces Germany by itself… "
        "with the Blitz, and with America behind it.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="THE FALL OF FRANCE", branches=[
            dict(t="Why France fell", items=["105 divisions, old strategy", "Maginot Line · phoney war", "Ardennes · Blitzkrieg"]),
            dict(t="Six weeks", items=["Dunkirk: 338,000", "Paris 14 June · exodus", "armistice 22 June"]),
            dict(t="Cut up · Vichy", items=["5 zones · 3/5 occupied", "Pétain: collaboration", "free zone invaded 11/1942"]),
            dict(t="Exploited · persecuted", items=["20 million RM a day", "STO · yellow star", "≈ 80,000 Jews deported"])]),
        "fin": dict(type="mot", t="Next: Britain alone", g="Episode 3 · 1940 – 1941", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="What was the “phoney war”?",
         r=["Sept. 1939 – May 1940: war declared, but almost no fighting in the west", "The German attack through the Ardennes",
            "The evacuation of Dunkirk", "The war between Vichy and de Gaulle"], ok=0, voir="drole",
         ex="France and Britain waited behind the Maginot Line: a defensive strategy."),
    dict(q="What was the weakness of the Maginot Line?",
         r=["It did not cover the Franco-Belgian border", "It was built after 1940", "It faced Italy, not Germany",
            "It had no artillery"], ok=0, voir="mag",
         ex="The main German attack came through the Ardennes, in south-eastern Belgium and northern Luxembourg."),
    dict(q="Where did the main German attack of May 1940 go through?",
         r=["The Ardennes forest", "Central Belgium, as in 1914", "The Maginot Line", "Switzerland"], ok=0, voir="cmp1",
         ex="The Allies rushed their best forces into central Belgium; the tanks broke through in the Ardennes, 13–20 May 1940."),
    dict(q="Why did French troops see Operation Dynamo as a betrayal?",
         r=["The British evacuated their army and left them to fight alone", "The British surrendered first",
            "The British signed the armistice", "The British invaded Normandy"], ok=0, voir="cols2",
         ex="26 May – 4 June 1940: 338,000 Allied soldiers evacuated; for Britain, the Royal Navy and the RAF were saved."),
    dict(q="Which figures give the human cost of the defeat of 1940?",
         r=["≈ 100,000 killed, 200,000 wounded, 1,850,000 prisoners", "338,000 killed and 8 million prisoners",
            "20 million dead", "1,850,000 killed"], ok=0, voir="toll",
         ex="The course's figure is ≈ 100,000 dead (recent research: ≈ 60,000). 338,000 is Dunkirk; 8 million is the exodus; 20 million is the daily occupation fee in Reichsmarks."),
    dict(q="Which territory was annexed outright to Germany in 1940?",
         r=["Alsace and Moselle", "The Nord and the Pas-de-Calais", "The Alpes-Maritimes", "The free zone"], ok=0, voir="zones",
         ex="Back to the borders of 1871; the Nord and Pas-de-Calais were attached to the German command in Brussels."),
    dict(q="Which measure shows that Vichy persecuted Jews before the Germans demanded it?",
         r=["The October 1940 decree defining who was a Jew", "The STO", "The armistice of Rethondes",
            "The demarcation line"], ok=0, voir="antij",
         ex="And in March 1941, Vichy created an Office for Jewish Affairs: French initiatives, not German orders."),
    dict(q="Who carried out the round-up of July 1942 in Paris?",
         r=["The French police", "The Milice", "The Wehrmacht alone", "De Gaulle's Free French"], ok=0, voir="milice",
         ex="The course says “the Milice”, but the Milice was only created in January 1943: write “the French police”."),
]

CREDITS = [
    "Content: the DNL History course (DNL History, H3 · Part I.1 “Nazi invasion of Western Europe: the French case”, Worksheet 1, the course map of the zones, three sources on occupied France, the divisions table) as written on the site; animated map of chapter 3 (site).",
    "Course correction: the arrests of summer 1942 (Vel' d'Hiv, 16–17 July 1942) were carried out by the French police, not by the Milice (created in January 1943).",
    "Photograph: Marshal Pétain and Adolf Hitler at Montoire, 24 October 1940 (Heinrich Hoffmann, Bundesarchiv, Bild 183-H25217, via Wikimedia Commons, CC BY-SA 3.0 DE); the meeting itself is outside the course.",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
