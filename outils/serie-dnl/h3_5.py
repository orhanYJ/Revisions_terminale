"""DNL History · H3 « World War Two » — série vidéo, épisode 5 : « Towards the genocide » (partie III du chapitre).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h3_5 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H3.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H3 : 2 population juive vers 1933 · 8 ghettos de Pologne · 22 ghetto de Varsovie · 27 Einsatzgruppen ·
       32 six centres de mise à mort · 37 Treblinka · 41 Nouvel Ordre européen fin 1942 (carte « German administration
       of Europe 1942 » du cours) · 43 soulèvement du ghetto · 44 révolte de Treblinka · 45 bilan du génocide
Contenu : CHAPTERS.H3, sections III.1 à III.3 (15 idées), panneaux h3hilberg et h3einsatz (questions des deux vidéos
du cours, réponses proposées par le site), h3etapes (les étapes du génocide), h3ws4 (Worksheet 4, Treblinka) ;
ce qui n'est pas dans le cours est dit « outside the course ». La diapositive date les sélections d'Auschwitz
« after 1944 » : la vidéo dit qu'elles commencent en 1942 et culminent en 1944, comme le site.
Ton : sobre ; aucune image des victimes (les photographies du cours sont décrites, jamais montrées) ; humeurs
« calme » et « mystere » seulement.
Plan de la série H3 : 1 A world war · 2 The fall of France · 3 Britain alone · 4 Barbarossa · 5 Towards the genocide ·
6 WWII at the exam (essay and DBQ) · 7 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-5"
NOTION = "World War Two"
NUM = 5
TITRE = "Towards the genocide"
SUIVANT = "Episode 6 · WWII at the exam: essay and DBQ"
PRONONCIATION = {"Einsatzgruppen": "Ine-zats-groopen", "Einsatzgruppe": "Ine-zats-groopa", "Chelmno": "Hel-mno",
                 "Sobibor": "So-bee-bor", "Majdanek": "My-dah-nek", "Belzec": "Bel-zhets", "Czestochowa": "Chen-sto-ho-va",
                 "Lodz": "Woodge", "Stroop": "Shtrope", "Jürgen": "Yoor-gen", "Stangl": "Shtahng-el",
                 "Willenberg": "Villen-berg", "Lindwasser": "Lind-vasser", "Lanzmann": "Lahnz-mann",
                 "Sonderkommando": "Zonder-kommando", "Zyklon": "Zee-klon", "Liepaja": "Lee-eh-pah-ya",
                 "Chłodna": "Hwod-na", "Ivangorod": "Ee-van-go-rod", "Siedlce": "Shed-ltseh", "Wehrmacht": "Vair-markt",
                 "Heydrich": "Hide-rick", "Auschwitz-Birkenau": "Owsh-vits Beer-ken-ow", "Auschwitz": "Owsh-vits",
                 "Babi": "Bah-bee", "Eichmann": "Ike-mann", "Himmler": "Him-ler", "Kielce": "Kyel-tseh",
                 "Breslau": "Bress-lau", "5–7": "five to seven"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Six million. Six million Jewish men, women and children, murdered by Nazi Germany and its helpers. "
        "Two thirds of the Jews of Europe.",
        "{-q1}{q2}How did a modern state come to organise the murder of a whole people? Not in one day, and not by accident: "
        "step by step, from the ghettos to the killing centres.",
        "{-q2}{-g0}{sobre}Maps, figures, short extracts of testimonies: the photographs of the course are described in words, never shown.",
        "{-sobre}{plan}This is Part three of the chapter: the Nazi racial policy. {plan.1}First, the events on the map. "
        "{plan.2}Then the course: the Jews stranded, and the ghettos. {plan.3}The Einsatzgruppen. "
        "{plan.4}The killing centres, and Treblinka. {plan.5}And finally: how do we know, and how to use it at the exam.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[45]),
        "q1": dict(type="question", t="Six million.", bande=True),
        "q2": dict(type="question", t="How did a modern state organise the murder of a whole people?", bande=True),
        "sobre": dict(type="note", terme="Before we start", cles=["maps", "figures", "testimonies"],
                      t="Maps, figures and short extracts of testimonies. No images of the victims.",
                      etape="The photographs of the course are described in words, never shown.", x=170, y=200, w=940),
        "plan": dict(type="liste", titre="Episode 5 · Part III of the course", items=[
            "The events on the map, 1933 – 1943", "III.1 · The Jews stranded and persecuted: the ghettos",
            "III.2 · The Einsatzgruppen: the “Shoah by bullets”", "III.3 · The killing centres: case study, Treblinka",
            "How do we know? The sources at the exam"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 5", t="Towards the genocide",
                      sous="1933 – 1943 · ghettos · bullets · gas · 6 million murdered"),
    }),

    # ================================================================ la carte, 1933-1941
    dict(id="carte1", chap="On the map, 1933 – 1941", fond="nuit", humeur="mystere",
         retenir="c. 1933: 9.5 million Jews in Europe, mostly in the East · 1939–41: ghettos in occupied Poland · Warsaw: 440,000 Jews in 4 km² · from June 1941: the Einsatzgruppen in the USSR.",
         beats=[
        "{g1}Let's start on the map, in chronological order. {g1.1}Around 1933, about nine and a half million Jews live in Europe. "
        "Most of them live in the East: three million in Poland, two and a half million in the Soviet Union. "
        "Germany, where Nazi persecution begins in 1933, has only five hundred and sixty-five thousand.",
        "{g1.2}September 1939: Germany conquers western Poland. From then until 1941, the Jews of occupied Poland are locked into ghettos, "
        "closed districts of the cities: Warsaw, Lodz, Krakow, Lublin, Kielce, Czestochowa.",
        "{g1.3}The largest is in Warsaw: four hundred and forty thousand Jews, crammed into about four square kilometres, behind a wall.",
        "{g1.4}Then, on the twenty-second of June 1941, Germany invades the Soviet Union. Behind the army come four mobile killing squads, "
        "the Einsatzgruppen. Town after town, they shoot the Jews at the edge of pits. Historians call it the Shoah by bullets.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[2, 8, 22, 27]),
    }),

    # ================================================================ la carte, 1941-1943
    dict(id="carte2", chap="On the map, 1941 – 1943", fond="nuit", humeur="mystere",
         retenir="Dec. 1941: the first killing centre · July 1942: Treblinka · 19 April – 16 May 1943: the Warsaw ghetto uprising · 2 August 1943: the Treblinka revolt · 6 million Jews murdered.",
         beats=[
        "{g2}{g2.1}From December 1941, a new method: gas. The Nazis operate six killing centres, all of them in occupied Poland: "
        "Chelmno, Belzec, Sobibor, Treblinka, Majdanek and Auschwitz. They are built to kill people on arrival.",
        "{g2.2}July 1942: Treblinka is built, north-east of Warsaw. Trains bring the Jews of the Warsaw ghetto and of the other ghettos. "
        "In fifteen months, eight hundred and seventy-six thousand people are murdered there.",
        "{g2.3}The nineteenth of April 1943: German troops enter the Warsaw ghetto to deport its last inhabitants, and the Jews rise up. "
        "The uprising lasts almost a month, until the sixteenth of May, before it is crushed by the SS.",
        "{g2.4}The second of August 1943: at Treblinka itself, seven hundred Jewish slaves rise up and set the camp on fire. "
        "The camp is closed in October.",
        "{g2.5}The toll: six million Jews murdered. Ninety per cent of the Jews of Poland. Ninety-seven per cent of the Jews of Lithuania.",
        "{-g2}{fr2}The dates to keep: {fr2.1}1933, {fr2.2}1939, the ghettos; {fr2.3}June 1941, the Einsatzgruppen; "
        "{fr2.4}December 1941, the first killing centre; {fr2.5}July 1942, Treblinka; {fr2.6}April 1943, the Warsaw uprising; "
        "{fr2.7}August 1943, the Treblinka revolt.",
    ], vis={
        "g2": dict(type="globe", code="H3", sc=[32, 37, 43, 44, 45]),
        "fr2": dict(type="frise", items=[
            dict(nom="9.5 million Jews", d=1933, q="mostly in the East"), dict(nom="Ghettos", d=1939, q="Poland, 1939–41"),
            dict(nom="Einsatzgruppen", d=1941, q="from June"), dict(nom="Killing centres", d=1941, q="from December"),
            dict(nom="Treblinka", d=1942, q="built in July"), dict(nom="Warsaw uprising", d=1943, q="19 April – 16 May"),
            dict(nom="Treblinka revolt", d=1943, q="2 August")]),
    }),

    # ================================================================ III.1 pris au piège
    dict(id="piege", chap="III.1 · Stranded", fond="nuit", humeur="calme",
         retenir="c. 1933: 9.5 million Jews in Europe, over two thirds in the East (Poland 3 million, USSR 2,525,000, Germany 565,000). By 1942 Germany ruled almost the whole continent: the Jews were trapped.",
         beats=[
        "{q3}Part three, section one: the Jews stranded and persecuted. Why stranded?",
        "{-q3}{pop}The course map of the Jewish population around 1933 counts: {pop.1}in Eastern Europe, almost six point eight million; "
        "{pop.2}in Central Europe, one point six million; {pop.3}in Northern and Western Europe, less than eight hundred thousand; "
        "{pop.4}in Southern Europe, about three hundred thousand. More than two thirds live in the East.",
        "{-pop}So when Germany conquers Poland in 1939, and invades the Soviet Union in 1941, it brings the heart of European Jewry under its rule. "
        "{!Stranded}That is what stranded means.",
        "{g3}A second course map, the German administration of Europe in 1942, shows the trap: from France to Ukraine, "
        "Greater Germany and the occupied territories, surrounded by allied or dependent states: Hungary, Romania, Slovakia, Croatia, Vichy France.",
        "{out}Who is left outside? {out.1}Only Britain, {out.2}and a few neutral states: Spain, Switzerland and Sweden. "
        "For the Jews of Europe, by 1942, there is almost nowhere left to escape to.",
    ], vis={
        "q3": dict(type="question", t="Why were the Jews of Europe “stranded”?"),
        "pop": dict(type="liste", titre="European Jewish population, c. 1933 (course map)", items=[
            "Eastern Europe: 6,760,000", "Central Europe: 1,644,200", "Northern and Western Europe: 766,600",
            "Southern Europe: 329,200"], x=170, y=130, w=940),
        "g3": dict(type="globe", code="H3", sc=[41]),
        "out": dict(type="liste", titre="Outside German rule in 1942", x=700, y=60, w=540, petit=True, bande=True, items=[
            "Britain", "Neutral states: Spain, Switzerland, Sweden"]),
    }),

    # ================================================================ III.1 les ghettos
    dict(id="ghettos", chap="III.1 · Locked into ghettos", fond="nuit", humeur="calme",
         retenir="From 1939, ghettos in occupied Poland: isolate, impoverish, weaken, gather for deportation. Warsaw: 440,000 Jews in 4 km², a wall 3 m high and 18 km long, 146,000 per km² in 1941.",
         beats=[
        "{def3}From 1939, in occupied Poland, the Germans concentrate the Jews in {!ghettos}ghettos. A ghetto is a closed district of a city, "
        "cut off from the rest of the population. The Jews are forced to move into it with almost nothing.",
        "{-def3}{g4}The course map places them mainly in the General Government, "
        "the part of Poland run by a German civil administration: Warsaw, Lodz, Krakow, Lublin, Czestochowa. "
        "After June 1941, the system spreads east, from Riga and Vilna to Minsk and Odessa.",
        "{-g4}{lst4}Be precise in an essay. {lst4.1}The ghetto is not yet extermination. {lst4.2}But it isolates the Jews, impoverishes them and weakens them, "
        "{lst4.3}and it gathers them in places from which they can later be deported.",
        "{-lst4}{war}The largest ghetto is in Warsaw: four hundred and forty thousand Jews, in about four square kilometres.",
        "{-war}{wl}{wl.1}They can take only the bare minimum: they are dispossessed overnight. "
        "{wl.2}The ghetto is surrounded by a wall three metres high and eighteen kilometres long. "
        "{wl.3}Reduced in 1941, it reaches a density of one hundred and forty-six thousand inhabitants per square kilometre: "
        "about seven times the density of Paris today, a comparison added from outside the course. "
        "{wl.4}And Chłodna Street stays outside the ghetto and cuts it in two: a wooden footbridge over the street "
        "connects the small ghetto and the large ghetto.",
    ], vis={
        "def3": dict(type="def", cles=["closed", "district"], terme="Ghetto",
                     t="A closed district of a city where the Nazis locked up the Jews, cut off from the rest of the population.",
                     etape="Occupied Poland, from 1939 · Warsaw, Lodz, Krakow, Lublin, Czestochowa", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H3", sc=[8]),
        "lst4": dict(type="liste", titre="What the ghetto does", cles=["extermination", "isolates", "deported"], items=[
            "It is not yet extermination", "It isolates, impoverishes and weakens the Jews",
            "It gathers them where they can later be deported"], x=170, y=150, w=940),
        "war": dict(type="mot", t="440,000 Jews · 4 km²", g="The Warsaw ghetto (course)", y=250, taille=96),
        "wl": dict(type="liste", titre="The Warsaw ghetto", items=[
            "Dispossessed overnight: only the bare minimum", "A wall 3 m high and 18 km long",
            "146,000 inhabitants per km² in 1941 (Paris today ≈ 20,000: outside the course)",
            "Chłodna Street: a footbridge joins the small and the large ghetto"], x=150, y=120, w=980),
    }),

    # ================================================================ III.1 la mort au ghetto, le soulèvement
    dict(id="varsovie", chap="III.1 · Death in the ghetto, and the uprising", fond="guerre", humeur="calme",
         retenir="In the ghetto, death was part of daily life: hunger, cold, disease, 1 birth for 45 deaths in 1942. Uprising: 19 April – 16 May 1943, crushed by Stroop: “The Jewish Quarter of Warsaw is No More!”",
         beats=[
        "{mort}In the ghetto, death becomes part of daily life. {mort.1}Hunger, cold, overcrowding and disease kill on a massive scale. "
        "{mort.2}Food has to be smuggled in, often by children, at the risk of arrest. {mort.3}Every day, usually at night, "
        "the Jewish death care service picks up the corpses in the streets; many end in mass graves. "
        "{mort.4}In the end, the population no longer even pays attention to the bodies lying in the streets.",
        "{-mort}{n45}One figure sums it up. In 1942, the Warsaw ghetto records one birth for every forty-five deaths.",
        "{-n45}{up}{up.1}In 1942, most of the inhabitants are deported to Treblinka. "
        "{up.2}In April 1943, German troops and police enter the ghetto to deport the survivors. The Jews rise up: "
        "the Warsaw ghetto uprising lasts from the nineteenth of April to the sixteenth of May 1943. "
        "{up.3}The Germans crush it by destroying the ghetto house by house. On the sixteenth of May, the SS commander Jürgen Stroop "
        "sends Himmler a message announcing the result.{-up}",
        ("C", "The Jewish Quarter of Warsaw is No More!", "c_stroop"),
        "{-c_stroop}{nur}The cover of Stroop's report, shown in the course, bears the stamp of the International Military Tribunal: "
        "the perpetrator's own report was used as evidence against the Nazi leaders at Nuremberg.",
    ], vis={
        "mort": dict(type="liste", titre="Death in the ghetto", cles=["Hunger", "smuggled", "night", "bodies"], items=[
            "Hunger, cold, overcrowding, disease", "Food smuggled in, often by children, at the risk of arrest",
            "Corpses picked up every day, usually at night", "People no longer noticed the bodies in the streets"], x=150, y=120, w=980),
        "n45": dict(type="mot", t="1 birth · 45 deaths", g="The Warsaw ghetto in 1942 (course)", y=250, taille=100),
        "up": dict(type="liste", titre="The Warsaw ghetto uprising", items=[
            "1942: most inhabitants deported to Treblinka", "19 April – 16 May 1943: the Jews rise up",
            "Crushed house by house; Stroop reports to Himmler"], x=150, y=140, w=980),
        "c_stroop": dict(type="cit", a="Jürgen Stroop", o="report to Himmler, 16 May 1943", x=200, y=200, w=880),
        "nur": dict(type="note", terme="Why this document matters", cles=["perpetrator's", "evidence"],
                    t="The perpetrator's own report was used as evidence at Nuremberg.",
                    etape="Its cover bears the stamp of the International Military Tribunal (course).", x=170, y=200, w=940),
    }),

    # ================================================================ III.1 Hilberg
    dict(id="hilberg", chap="III.1 · Raul Hilberg: three stages", fond="nuit", humeur="calme",
         retenir="Hilberg: conversion (“no right to live among us as Jews”) → expulsion (“no right to live among us”) → destruction (“no right to live”). Badge and ghetto had precedents; the only Nazi “invention”: the Final Solution.",
         beats=[
        "{hil}Where does the genocide come from? The course answers with a historian, Raul Hilberg, author of The Destruction of the European Jews, in 1961. "
        "In Claude Lanzmann's film Shoah, he places Nazi policy in a long history of persecution.",
        "{-hil}{st}{st.1}First, conversion. The Christian missionaries told the Jews, in effect: you have no right to live among us as Jews. "
        "{st.2}Then, expulsion. The secular rulers who followed told them: you have no right to live among us. "
        "{st.3}Finally, destruction. The Nazis decreed: you have no right to live.",
        "{-st}{can}Before the twentieth century, the Church and Christian states had already invented most of the measures the Nazis reused: "
        "the badge, the ghetto, the ban on mixed marriages. {can.g}Hilberg sets canon law {can.d}against Nazi measures: "
        "the badge of the Lateran Council, in 1215, and the Jewish star of 1941; the ghettos of the Synod of Breslau, "
        "in 1267, and Heydrich's order of 1939. These dates come from Hilberg's book, outside the slides.",
        "{-can}{inv}So what did the Nazis invent? Only the last step: the decision to kill all the Jews, "
        "and the organisation of their murder. {!The Final Solution}The Final Solution.",
        "{-inv}{vq1}So, the three questions of the course video, with the answers suggested by the site: "
        "{vq1.1}three stages, conversion, expulsion, destruction; {vq1.2}before the twentieth century, the Church and the Christian states; "
        "{vq1.3}and the only Nazi invention, the Final Solution.",
    ], vis={
        "hil": dict(type="mot", t="Raul Hilberg", g="The Destruction of the European Jews (1961) · interviewed in Shoah (Lanzmann, 1985)",
                    y=250, taille=96),
        "st": dict(type="liste", titre="Hilberg: three stages of anti-Jewish policy", cles=["Conversion", "Expulsion", "Destruction"], items=[
            "Conversion: “you have no right to live among us as Jews”", "Expulsion: “you have no right to live among us”",
            "Destruction: “you have no right to live”"], x=150, y=150, w=980),
        "can": dict(type="cols", g="Canon law", gq="badge: Lateran Council, 1215 · ghetto: Synod of Breslau, 1267 · ban on mixed marriages",
                    d="Nazi measures", dq="Jewish star: 1 Sept. 1941 · ghetto order: 21 Sept. 1939 (dates outside the slides)", vs="→"),
        "inv": dict(type="def", cles=["kill", "murder"], terme="Key term · the Final Solution",
                    t="The Nazi euphemism for the murder of all the Jews of Europe: their only “invention”, for Hilberg.",
                    etape="Badge, ghetto, dispossession had precedents; the systematic murder did not.", x=170, y=200, w=940),
        "vq1": dict(type="liste", titre="Course video · Hilberg in Shoah (suggested answers)", items=[
            "Three stages? → conversion, expulsion, destruction",
            "Who persecuted before? → the Church (canon law), Christian states",
            "The only Nazi “invention”? → the Final Solution"], x=150, y=150, w=980),
    }),

    # ================================================================ III.2 les Einsatzgruppen
    dict(id="einsatz", chap="III.2 · The Einsatzgruppen", fond="guerre", humeur="calme",
         retenir="From 22 June 1941: four Einsatzgruppen (A, B, C, D) behind the army in the USSR. Jews above all, also communist officials and Roma, shot at the edge of pits: the “Shoah by bullets”, the first step of the Final Solution.",
         beats=[
        "{g7}Section two: the role of the Einsatzgruppen. When Germany invades the Soviet Union, on the twenty-second of June 1941, "
        "four groups follow the army. {ein}On the course map: {ein.1}group A crosses the Baltic states, {ein.2}B heads for Belarus and Moscow, "
        "{ein.3}C goes into Ukraine, {ein.4}and D into southern Ukraine and the Crimea.",
        "{-ein}{-g7}{def7}Mobile killing squads of the SS and the police: about three thousand men, a figure added from outside the course. "
        "The course calls their work {!the first step}the first step of the Final Solution: from its first days, "
        "the war of annihilation was also a war against the Jews.",
        "{-def7}{tg}Their targets: {tg.1}the Jews above all, {tg.2}but also communist officials and Roma. "
        "{tg.3}First the men; from August 1941, whole communities, women and children included, which is added from outside the course. "
        "{tg.4}The method: the victims are led out of town and shot at the edge of pits or ravines. "
        "Hence the expression on the course map: {!the Shoah by bullets}the Shoah by bullets.",
        "{-tg}{ph}The course shows a photograph inscribed: Ukraine 1942, Jewish Action, Ivangorod. "
        "A soldier aims his rifle at a woman holding a child. Mailed home from the Eastern Front, it was intercepted in Warsaw by the Polish resistance. "
        "Outside the course: at Babi Yar, near Kiev, more than thirty-three thousand Jews were shot in two days, in September 1941.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[27]),
        "ein": dict(type="liste", titre="Four Einsatzgruppen, June 1941", x=40, y=70, w=340, petit=True, bande=True, items=[
            "A: the Baltic states", "B: Belarus, towards Moscow", "C: Ukraine", "D: southern Ukraine, the Crimea"]),
        "def7": dict(type="def", cles=["Mobile", "SS", "police"], terme="Einsatzgruppen",
                     t="Mobile killing squads of the SS and the police that followed the army into the USSR.",
                     etape="≈ 3,000 men (outside the course) · “the first step of the Final Solution” (course)", x=170, y=200, w=940),
        "tg": dict(type="liste", titre="Targets and method", cles=["Jews", "Roma", "August", "pits"], items=[
            "The Jews above all", "Also communist officials and Roma",
            "First men; from August 1941, whole communities (outside the course)",
            "Mass shooting at pits and ravines: the “Shoah by bullets”"], x=150, y=120, w=980),
        "ph": dict(type="note", terme="A document of the course (described, not shown)", cles=["Ivangorod", "soldier"],
                   t="“Ukraine 1942, Jewish Action, Ivangorod”: a soldier aims at a woman holding a child.",
                   etape="Mailed home from the Eastern Front, intercepted in Warsaw by the Polish resistance.", x=170, y=180, w=940),
    }),

    # ================================================================ III.2 plus d'un million
    dict(id="einsatz2", chap="III.2 · More than a million victims", fond="nuit", humeur="calme",
         retenir="Helped by the Order Police, the Wehrmacht and local auxiliaries, the Einsatzgruppen shot more than a million Soviet Jews by spring 1943. Lithuania: 97% of Jews killed; Latvia: 75%.",
         beats=[
        "{aid}The Einsatzgruppen are few, but they do not act alone. {aid.1}Battalions of the Order Police, {aid.2}units of the Wehrmacht, "
        "{aid.3}and local auxiliaries recruited in the occupied territories, Lithuanians, Latvians, Ukrainians, help them round up, guard and shoot the victims.",
        "{-aid}{mil}By the spring of 1943, they have killed more than a million Soviet Jews: the helpers and this figure are added from outside the course. "
        "On the course map, one million of the three million Jews of the USSR, almost all by shooting, since the killing centres were in Poland.",
        "{-mil}{bal}In the Baltic states, crossed by group A, the communities are almost wiped out: "
        "{bal.1}ninety-seven per cent of the Jews of Lithuania killed, "
        "{bal.2}seventy-five per cent in Latvia. "
        "{bal.3}And German footage of a shooting at Liepaja, in Latvia, in 1941, shown in the course, proves that these killings were seen, even filmed.",
        "{-bal}{vq2}The five questions of the second course video, with the answers suggested by the site: "
        "{vq2.1}the members, SS and police; {vq2.2}the targets, Jews above all; {vq2.3}four groups; "
        "{vq2.4}helped by the army, the police and local auxiliaries; {vq2.5}more than a million victims, shot.",
    ], vis={
        "aid": dict(type="liste", titre="They did not act alone (outside the course)", items=[
            "Order Police battalions", "Units of the Wehrmacht", "Local auxiliaries: Lithuanians, Latvians, Ukrainians"],
            x=150, y=150, w=980),
        "mil": dict(type="mot", t="1,000,000", g="of the 3,020,000 Jews of the USSR killed, almost all by shooting (course map)", y=240, taille=120),
        "bal": dict(type="liste", titre="The Baltic states (course map)", items=[
            "Lithuania: 140,000 of 145,000 Jews killed (97%)", "Latvia: 70,000 of 95,000 (75%)",
            "Liepaja, 1941: a shooting filmed by German soldiers"], x=150, y=150, w=980),
        "vq2": dict(type="liste", titre="Course video · the first step of the Final Solution", petit=True, items=[
            "Members? → SS and police, about 3,000 men", "Targets? → Jews above all, communist officials, Roma",
            "How many groups? → four, A to D", "Helpers? → Wehrmacht, Order Police, local auxiliaries",
            "How many, how? → over a million Soviet Jews, by mass shooting"], x=150, y=120, w=980),
    }),

    # ================================================================ III.3 six centres de mise à mort
    dict(id="centres", chap="III.3 · Six killing centres", fond="nuit", humeur="calme",
         retenir="From December 1941, six killing centres, all in occupied Poland: Chelmno, Treblinka, Sobibor, Belzec, Majdanek, Auschwitz. Gassed on arrival; the Sonderkommando; Treblinka: 3,000 people an hour from October 1942.",
         beats=[
        "{g9}Section three. From December 1941, six killing centres: in the words of the course, sophisticated centres of mass murder. {six}All of them in occupied Poland: {six.1}Chelmno, in the part annexed to Greater Germany; "
        "{six.2}Treblinka, {six.3}Sobibor, {six.4}Belzec {six.5}and Majdanek, in the General Government; {six.6}and Auschwitz, at the edge of Greater Germany.",
        "{-six}Why Poland? At the heart of the largest Jewish community in Europe, close to the ghettos, on the railway network. "
        "Chelmno began gassing on the eighth of December 1941, a date added from outside the course.",
        "{-g9}{cmp9}Do not confuse two words. {cmp9.g}A concentration camp imprisons and exploits its inmates. {cmp9.d}A killing centre exists to kill.",
        "{-cmp9}{gaz}{gaz.1}In the killing centres, the Jews are gassed upon arrival: first the men, then the women and children. "
        "{gaz.2}Only a small group of slaves is kept alive, to work in the camp and to dispose of the bodies: the {!Sonderkommando}Sonderkommando. "
        "{gaz.3}The corpses are burned, in the open air or, at Auschwitz, in ovens. "
        "{gaz.4}It is organised like an industry: at Treblinka, from October 1942, three thousand people an hour, "
        "and six to seven thousand per train.",
        "{-gaz}{bom}Avraham Bomba, a survivor of Treblinka, describes a concrete gas chamber of about six metres by six, "
        "with no windows, and pipes that made it look like a shower. And he says:{-bom}",
        ("C", "the whole thing took I would say between 5–7 minutes", "c_bomba"),
    ], vis={
        "g9": dict(type="globe", code="H3", sc=[32]),
        "six": dict(type="liste", titre="Six killing centres, occupied Poland", x=40, y=60, w=340, petit=True, bande=True, items=[
            "Chelmno", "Treblinka", "Sobibor", "Belzec", "Majdanek", "Auschwitz"]),
        "cmp9": dict(type="cols", g="Concentration camp", gq="imprisons and exploits its inmates", d="Killing centre",
                     dq="exists to kill, on arrival", vs="≠"),
        "gaz": dict(type="liste", titre="Murder organised like an industry", cles=["arrival", "Sonderkommando", "burned", "hour"], items=[
            "Gassed upon arrival: men first, then women and children", "A few slaves kept alive: the Sonderkommando",
            "Corpses burned: in the open air, or in ovens at Auschwitz",
            "Treblinka, Oct. 1942: 3,000 an hour; 6,000 – 7,000 per train"], x=150, y=120, w=980),
        "bom": dict(type="note", terme="Avraham Bomba (1990, Worksheet 4)", cles=["concrete", "windows", "pipes"],
                    t="A concrete room, about 6 m × 6 m, no windows, pipes that looked like a shower.",
                    etape="A barber deported from Czestochowa in September 1942; escaped in January 1943.", x=170, y=200, w=940),
        "c_bomba": dict(type="cit", a="Avraham Bomba", o="testimony, 1990 (Worksheet 4)", x=200, y=210, w=880),
    }),

    # ================================================================ III.3 Auschwitz et Majdanek
    dict(id="auschwitz", chap="III.3 · Auschwitz and Majdanek", fond="nuit", humeur="calme",
         retenir="Auschwitz and Majdanek: killing centre + concentration and labour camp; Zyklon B; selections on arrival (about 80% sent to the gas). Selections began in 1942 and peaked in 1944 (Hungary).",
         beats=[
        "{am}Two of the six centres are different: Auschwitz and Majdanek. {am.1}They combine a killing centre with a concentration and labour camp. "
        "{am.2}A new gas is used there: {!Zyklon B}Zyklon B. {am.3}And on arrival, the Nazis organise selections: the healthy become slaves "
        "for the German war effort; the others, about eighty per cent, are immediately driven to the gas chambers. "
        "{am.4}Auschwitz-Birkenau was first built for Soviet prisoners of war, the first to be gassed there, as Worksheet 3 showed.",
        "{-am}{dat}One correction about the dates. {dat.1}The slide places the selections after 1944. "
        "{dat.2}In fact, they began at Auschwitz in 1942. {dat.3}And 1944 was their peak, with the deportation of the Jews of Hungary. "
        "This is added from outside the course. On the course map, Hungary lost seventy-six per cent of its Jews.",
    ], vis={
        "am": dict(type="liste", titre="Auschwitz and Majdanek: a different kind of centre", cles=["labour", "Zyklon", "selections", "Soviet"], items=[
            "Killing centre + concentration and labour camp", "A new gas: Zyklon B",
            "Selections: slaves for the war effort; about 80% gassed at once",
            "Birkenau first built for Soviet POWs, the first gassed there"], x=150, y=120, w=980),
        "dat": dict(type="liste", titre="Selections: get the dates right", marques=["✗", "✓", "✓"], items=[
            "The slide: selections “after 1944”", "In fact: from 1942 at Auschwitz (outside the course)",
            "Peak in 1944: the Jews of Hungary (550,000 of 725,000 killed, 76%)"], x=150, y=150, w=980),
    }),

    # ================================================================ III.3 Treblinka
    dict(id="treblinka", chap="Case study #3: Treblinka", fond="nuit", humeur="calme",
         retenir="Treblinka: built July 1942 NE of Warsaw; 876,000 dead (874,000 Jews, 2,000 Roma); victims deceived until the end; revolt of 700 slaves on 2 August 1943 (about 70 survived the war); closed October 1943.",
         beats=[
        "{g11}Now the case study of Worksheet 4: Treblinka, built in July 1942 in the General Government, about eighty kilometres north-east of Warsaw, "
        "a distance added from outside the course. {tb}{tb.1}Until it closes, in October 1943, "
        "{tb.2}it kills eight hundred and seventy-six thousand people: eight hundred and seventy-four thousand Jews, mostly from the ghettos, and two thousand Roma.",
        "{-tb}{-g11}{arr}The victims arrive by train, in freight cars, under guard: a photograph of the worksheet shows Jews "
        "boarding trains at Siedlce, in August 1942. Everything is designed to deceive them until the last moment. "
        "A notice announces that after bathing and changing their clothes, the Jews will continue their journey to the east, to work.",
        "{-arr}Avraham Lindwasser arrives from Warsaw on the twenty-eighth of August 1942; he testified at the Eichmann trial in 1961. "
        "At the ramp, the order:",
        ("C", "Get out", "c_lind"),
        "{-c_lind}{ram}{ram.1}Then shouts and blows. {ram.2}Money and jewellery handed over, shoes removed. "
        "{ram.3}Rows of three. {ram.4}And an officer, the captain with the glasses, asks for professions: a few men are picked to become slaves. "
        "Lindwasser is one of them. He is kept alive as a slave for a year.",
        "{-ram}{g11b}On the second of August 1943, seven hundred slave Jews rise up and set the camp on fire. Lindwasser escapes. "
        "{rv}{rv.1}Of those who broke through, about seventy are known to have survived until the end of the war. "
        "{rv.2}In October 1943, the camp is closed.",
    ], vis={
        "g11": dict(type="globe", code="H3", sc=[37]),
        "tb": dict(type="liste", titre="Treblinka (Worksheet 4)", x=700, y=60, w=540, petit=True, bande=True, items=[
            "July 1942 – October 1943", "876,000 dead: 874,000 Jews, 2,000 Roma"]),
        "arr": dict(type="note", terme="Deceived until the end", cles=["notice", "east"],
                    t="A notice: after bathing, the Jews would continue their journey “to the east, to work”.",
                    etape="Doc. 3: Jews boarding trains under guard at Siedlce, August 1942 (described).", x=170, y=200, w=940),
        "c_lind": dict(type="cit", a="Avraham Lindwasser", o="Eichmann trial, 1961 (Worksheet 4)", x=200, y=230, w=880),
        "ram": dict(type="liste", titre="Arrival at the ramp (Lindwasser)", items=[
            "Shouts and blows: no time to understand", "Money, jewellery and shoes handed over", "Rows of three",
            "“The captain with the glasses” picks a few slaves by profession"], x=150, y=130, w=980),
        "g11b": dict(type="globe", code="H3", sc=[44]),
        "rv": dict(type="liste", titre="The revolt, 2 August 1943", x=700, y=60, w=540, petit=True, bande=True, items=[
            "About 70 known to have survived the war", "October 1943: the camp closed"]),
    }),

    # ================================================================ Worksheet 4
    dict(id="ws4", chap="Worksheet 4: the key answers", fond="aube", humeur="calme",
         retenir="Worksheet 4: present Treblinka (dates, place, toll) · the victims (ghettos, trains, deception) · the slaves' tasks · the killing process, from the ramp to the burning of the bodies.",
         beats=[
        "{ws}The four questions of Worksheet 4, with the key points suggested by the site, not an official answer key. "
        "{ws.1}One: present Treblinka, with its dates, its place and its toll. "
        "{ws.2}Two: the victims: from the ghettos, Lindwasser from Warsaw, Bomba from Czestochowa; by train, deceived. "
        "{ws.3}Three: the tasks of the slave Jews. Barbers like Bomba, inside the gas chamber itself; sorting the victims' belongings; "
        "camouflaging the camp; and, in Treblinka two, the extermination area, taking the corpses to the ditches. "
        "{ws.4}Four: describe the killing process. Here is the chain to follow.",
        "{-ws}{proc}{proc.1}The train stops at the ramp: “Get out”, shouts and blows. "
        "{proc.2}Money, jewellery and shoes handed over; rows of three; a few men picked as slaves. "
        "{proc.3}The others undress, reassured by the notice. "
        "{proc.4}The gas chamber: crammed in as tightly as possible; death in five to seven minutes. "
        "{proc.5}The slaves drag the corpses to the ditches; later, the corpses are burned in the open air. "
        "Three thousand people an hour, from October 1942.",
    ], vis={
        "ws": dict(type="liste", titre="Worksheet 4 · Treblinka (suggested answers)", petit=True, items=[
            "Present it → killing centre, July 1942 – Oct. 1943, NE of Warsaw, 876,000 dead",
            "Victims? → Warsaw and other ghettos; by train, under guard, deceived",
            "Slaves' tasks → barbers, sorting belongings, camouflage, corpses (“Treblinka 2”)",
            "The killing process → from the ramp to the burning of the corpses"], x=130, y=120, w=1020),
        "proc": dict(type="liste", titre="Question 4 · the chain to follow", petit=True, items=[
            "The ramp: “Get out”, shouts and blows", "Money, jewellery, shoes; rows of three; slaves picked",
            "Undressing, reassured by the deceptive notice", "The gas chamber: death in 5 to 7 minutes",
            "Corpses to the ditches, then burned · 3,000 an hour from Oct. 1942"], x=130, y=120, w=1020),
    }),

    # ================================================================ III.3 le bilan, les étapes
    dict(id="bilan", chap="Six million", fond="guerre", humeur="calme",
         retenir="6 million Jews murdered, two thirds of Europe's Jews: Poland 90%, Lithuania 97%, Netherlands 71%, France 28%, Italy 16%. The stages: ghettos → bullets → gas → revolts.",
         beats=[
        "{g13}The Shoah killed six million Jews, two thirds of the Jews of Europe: gassed, shot, "
        "or killed by the work and living conditions of the ghettos and the camps.",
        "{pays}The course map shows huge differences between countries. {pays.1}Poland: three million killed, ninety per cent. "
        "{pays.2}Lithuania: ninety-seven per cent. {pays.3}The Netherlands: seventy-one per cent. {pays.4}France: twenty-eight per cent. "
        "{pays.5}Italy: sixteen per cent. Under direct German occupation, in Poland and the Baltic states, the communities were almost wiped out.",
        "{-pays}{-g13}{lien13}And link this to episode one. The genocide carried out the first driving force of the New European Order: "
        "Europe as a racial entity, purified by murder.",
        "{-lien13}{eta}So here is the whole process, in four stages. {eta.1}From 1939: the ghettos, to concentrate, isolate and starve. "
        "{eta.2}From June 1941: the bullets, the Einsatzgruppen behind the army. {eta.3}From December 1941: the gas, six killing centres in occupied Poland. "
        "{eta.4}And in 1943: the revolts, when the victims fight back, in the Warsaw ghetto and at Treblinka.",
        "{-eta}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}One way to say it. {rep1.1}From 1939, the Jews of Poland were locked into ghettos, isolated and starved. "
        "{rep1.2}From June 1941, the Einsatzgruppen shot more than a million Soviet Jews. "
        "{rep1.3}From December 1941, six killing centres gassed them on arrival: six million murdered in all.",
    ], vis={
        "g13": dict(type="globe", code="H3", sc=[45]),
        "pays": dict(type="liste", titre="Share of Jews killed (course map)", x=880, y=380, w=370, petit=True, bande=True, items=[
            "Poland: 3,000,000 of 3,350,000 (90%)", "Lithuania: 97%", "Netherlands: 100,000 of 140,000 (71%)",
            "France: 75,000 of 270,000 (28%)", "Italy: 8,000 of 50,000 (16%)"]),
        "lien13": dict(type="note", terme="Link to episode 1", cles=["racial", "murder"],
                       t="The genocide carried out the first driving force of the New European Order: Europe as a racial entity.",
                       etape="“The absolute elimination of the Jews” (Hitler, 11 December 1941, as quoted in the course).", x=170, y=200, w=940),
        "eta": dict(type="liste", titre="From persecution to genocide: the stages", items=[
            "1939 – 41 · Ghettos: concentrate, isolate, starve", "From June 1941 · Bullets: Einsatzgruppen A–D",
            "From Dec. 1941 · Gas: six killing centres in Poland", "1943 · Revolts: Warsaw ghetto (April – May), Treblinka (2 August)"],
            x=150, y=130, w=980),
        "pa1": dict(type="pause", t="In three sentences: how did Nazi policy move from persecution to genocide?",
                    sous="Pause the video, write your answer, then play on to compare."),
        "rep1": dict(type="liste", titre="A model answer", items=[
            "From 1939: ghettos in Poland: isolated, starved, gathered.",
            "From June 1941: the Einsatzgruppen shoot over a million Soviet Jews.",
            "From Dec. 1941: six killing centres gas them on arrival; 6 million murdered."], x=150, y=150, w=980),
    }),

    # ================================================================ comment le sait-on ?
    dict(id="sources", chap="How do we know?", fond="nuit", humeur="calme",
         retenir="How do we know? Survivors (Lindwasser 1961; Bomba in Shoah, 1985, and in 1990), perpetrators (Stroop's report; Stangl's sketch, after his arrest in 1967), survivors' plans (Willenberg: to scale, but he never saw the extermination area).",
         beats=[
        "{q14}The last question of the course, and a very important one for the exam: how do we know?",
        "{-q14}{src}Three kinds of sources, each with its value and its limits. "
        "{src.1}The testimonies of survivors: Lindwasser in 1961; Bomba in Claude Lanzmann's film Shoah, in 1985, and in an interview of 1990. "
        "{src.2}The documents of the perpetrators: Stroop's report; the sketch plan of Treblinka drawn by Franz Stangl, its commandant, "
        "after his arrest in 1967; he was tried in 1970. {src.3}And the plans drawn by survivors.",
        "{-src}{wil}The most famous is by Samuel Willenberg. A member of the camouflage commando, he had access to most of the camp. "
        "He drew a plan of Treblinka to scale, with every detail: it is considered one of the most reliable. "
        "{wil.1}Except for one area: the extermination area, which he never saw.",
        "{-wil}{vl}For any source, two columns: {vl.g}its value, {vl.d}its limits. A survivor saw with his own eyes, "
        "but only what he saw; a perpetrator knows the system, but may hide or excuse his crimes.",
    ], vis={
        "q14": dict(type="question", t="How do we know?"),
        "src": dict(type="liste", titre="Three kinds of sources", cles=["survivors", "perpetrators", "plans"], items=[
            "Testimonies of survivors: Lindwasser (1961), Bomba (Shoah, 1985; 1990)",
            "Documents of the perpetrators: Stroop's report; Stangl's sketch (after his arrest, 1967)",
            "Plans drawn by survivors: Samuel Willenberg"], x=150, y=150, w=980),
        "wil": dict(type="note", terme="Samuel Willenberg's plan", cles=["scale", "reliable"],
                    t="Drawn to scale by a survivor of the camouflage commando: one of the most reliable plans of Treblinka.",
                    etape="Limit: the extermination area, which he never saw.", x=170, y=200, w=940),
        "vl": dict(type="cols", g="Value", gq="an eyewitness · a perpetrator who knows the system · a precise plan",
                   d="Limits", dq="only what the witness saw · a perpetrator may hide or excuse his crimes", vs="↔"),
    }),

    # ================================================================ à l'examen : DBQ
    dict(id="dbq", chap="At the exam: a DBQ", fond="aube", humeur="calme",
         retenir="DBQ a): judgement in the first line (largely useful) · the document in one sentence · strengths (eyewitness, to scale, confirmed by other sources) · limits (never saw the extermination area, one witness, places not numbers).",
         beats=[
        "{ex}An exam exercise. {ex.p1}In a DBQ: the plan of Treblinka drawn by Samuel Willenberg. "
        "{ex.1}Question a: how useful is this document for understanding how the Treblinka killing centre worked?",
        "{-ex}{struc}The structure to follow: {struc.1}your judgement in the first line: largely, significantly, partly or slightly useful. "
        "{struc.2}The document, presented in one sentence. {struc.3}A paragraph of strengths, with several arguments. "
        "{struc.4}A paragraph of limits, with several arguments.",
        "{-struc}{pa2}",
        ("P", 2.0),
        "{-pa2}{m1}Here is a model. First line: this document is largely useful for understanding how Treblinka worked. "
        "{m1.1}Then one sentence: it is a plan of the Treblinka killing centre, drawn to scale by Samuel Willenberg, a survivor who worked in the camouflage commando.",
        "{-m1}{fort}The strengths. {fort.1}It is the work of an eyewitness, who had access to most of the camp. "
        "{fort.2}It is drawn to scale, with every detail: the outer shape of the camp almost matches the actual site. "
        "{fort.3}And it can be checked against other sources: Lindwasser, Bomba, even the commandant Stangl's sketch.",
        "{-fort}{lim}The limits. {lim.1}Willenberg never saw the extermination area. "
        "{lim.2}It is the view of a single witness: compare it with other sources. "
        "{lim.3}And a plan shows places, not the scale of the murder: for that, add the toll, eight hundred and seventy-six thousand dead, and the testimonies.",
    ], vis={
        "ex": dict(type="exo", niveau="dbq", titre="Samuel Willenberg's plan of Treblinka",
                   enonce=["A plan of the Treblinka killing centre, drawn to scale by Samuel Willenberg, a survivor who worked in the camouflage commando."],
                   questions=["a) How useful is this document for understanding how the Treblinka killing centre worked?"]),
        "struc": dict(type="liste", titre="DBQ a) · the structure", items=[
            "Judgement in the first line: largely / significantly / partly / slightly useful",
            "The document presented in one sentence", "Strengths: several arguments", "Limits: several arguments"],
            x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Write answer a): how useful is Willenberg's plan for understanding how Treblinka worked?",
                    sous="Pause the video, follow the four steps, then play on for a model."),
        "m1": dict(type="note", terme="A model · judgement and presentation", cles=["largely"],
                   t="This document is largely useful for understanding how Treblinka worked.",
                   etape="A plan of Treblinka drawn to scale by Samuel Willenberg, a survivor of the camouflage commando.", x=150, y=180, w=980),
        "fort": dict(type="liste", titre="Strengths", marques=["✓", "✓", "✓"], items=[
            "An eyewitness, with access to most of the camp", "Drawn to scale: the outer shape matches the actual site",
            "Can be checked: Lindwasser, Bomba, Stangl's sketch"], x=150, y=150, w=980),
        "lim": dict(type="liste", titre="Limits", marques=["✗", "✗", "✗"], items=[
            "He never saw the extermination area", "One witness: compare with other sources",
            "Places, not numbers: add 876,000 dead and the testimonies"], x=150, y=150, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Ghettos: from 1939, the Jews of Poland, stranded, are locked up, four hundred and forty thousand in Warsaw; "
        "for Hilberg, the only Nazi invention was the Final Solution. "
        "{carte.2}Bullets: from June 1941, the Einsatzgruppen shoot more than a million Soviet Jews. "
        "{carte.3}Gas: from December 1941, six killing centres in Poland; Treblinka, eight hundred and seventy-six thousand dead; "
        "in all, six million. {carte.4}And the sources: survivors, perpetrators, plans, each with its value and its limits.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the Second World War at the exam, the essay and the DBQ, step by step.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="TOWARDS THE GENOCIDE", branches=[
            dict(t="Ghettos · III.1", items=["9.5 million Jews, mostly in the East", "Warsaw: 440,000 in 4 km²", "Hilberg: the Final Solution"]),
            dict(t="Bullets · III.2", items=["Einsatzgruppen A–D, June 1941", "Jews, communists, Roma", "over 1 million Soviet Jews"]),
            dict(t="Gas · III.3", items=["6 killing centres in Poland", "Treblinka: 876,000 dead", "6 million: 2/3 of Europe's Jews"]),
            dict(t="Sources", items=["survivors: Lindwasser, Bomba", "perpetrators: Stroop, Stangl", "plans: Willenberg"])]),
        "fin": dict(type="mot", t="Next: WWII at the exam", g="Episode 6 · essay and DBQ", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Around 1933, where did most of Europe's 9.5 million Jews live?",
         r=["In Eastern Europe (6.76 million)", "In Germany", "In Western Europe", "In Southern Europe"], ok=0, voir="pop",
         ex="Poland had 3 million Jews, the USSR 2,525,000, Germany only 565,000: conquering the East trapped them."),
    dict(q="How many Jews were locked up in the Warsaw ghetto, and on what area?",
         r=["440,000 in about 4 km²", "44,000 in 40 km²", "4.4 million in 4 km²", "146,000 in 18 km²"], ok=0, voir="war",
         ex="146,000 inhabitants per km² in 1941; the wall was 3 m high and 18 km long."),
    dict(q="What were Raul Hilberg's three stages of anti-Jewish policy?",
         r=["Conversion, expulsion, destruction", "Ghettos, bullets, gas", "Badge, ghetto, star", "Persecution, deportation, liberation"],
         ok=0, voir="st",
         ex="“No right to live among us as Jews”, “no right to live among us”, “no right to live”. The only Nazi invention: the Final Solution."),
    dict(q="What did the Einsatzgruppen do?",
         r=["Mobile SS and police squads that shot Jews behind the front in the USSR", "They ran the killing centres in Poland",
            "They guarded the Warsaw ghetto", "They were Polish resistance fighters"], ok=0, voir="def7",
         ex="Four groups, A to D, from June 1941: the “Shoah by bullets”, more than a million Soviet Jews killed."),
    dict(q="Where were the six killing centres?",
         r=["All in occupied Poland", "In Germany", "In the occupied USSR", "In France and Belgium"], ok=0, voir="six",
         ex="Chelmno, Treblinka, Sobibor, Belzec, Majdanek, Auschwitz: close to the ghettos and on the railway network."),
    dict(q="When did the selections at Auschwitz begin?",
         r=["In 1942, with a peak in 1944", "Only after 1944", "In 1939", "In 1945"], ok=0, voir="dat",
         ex="The slide says “after 1944”; in fact they began in 1942 and peaked in 1944 with the deportation of the Jews of Hungary."),
    dict(q="How many people were killed at Treblinka?",
         r=["876,000, including 874,000 Jews and 2,000 Roma", "6 million", "70,000", "3,000"], ok=0, voir="tb",
         ex="July 1942 – October 1943; 3,000 is the hourly capacity of the gas chambers from October 1942."),
    dict(q="What is the main limit of Willenberg's plan of Treblinka?",
         r=["He never saw the extermination area", "It is not to scale", "It was drawn by the commandant",
            "It shows the Warsaw ghetto, not Treblinka"], ok=0, voir="wil",
         ex="A survivor of the camouflage commando, he drew the camp to scale: largely useful, but limited for that area."),
]

CREDITS = [
    "Content: the DNL History course (DNL History, H3 · Part III: the Nazi racial policy, towards the genocide; Worksheet 4 · Treblinka; the course videos on Raul Hilberg and the Einsatzgruppen) as written on the site, with additions marked “outside the course” (US Holocaust Memorial Museum); animated map of chapter 3 (site).",
    "Answers to the worksheet and to the video questions: suggested by the site, not an official answer key.",
    "No photographs of the victims: the documents of the course are described in words.",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
