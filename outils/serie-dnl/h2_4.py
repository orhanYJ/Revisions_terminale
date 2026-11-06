"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 4 : « The leader, the party and the New Man »
(parties II.1 et II.2).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_4 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 6 marche sur Rome · 8 la dictature rendue légale · 9 le culte du chef, villes rebaptisées · 11 la jeunesse
       d'abord, trois « hommes nouveaux » · 12 plan quinquennal et collectivisation · 20 Hitler chancelier ·
       23 nazisme, lutte des races · 24 rassemblements, médias, arts · 26 Stakhanov
Contenu : CHAPTERS.H2 du site (dnl/index.html), sections II.1 (6 idées) et II.2 (6 idées), schémas h2cult (H2Cult :
trois chefs, trois cultes) et h2newman (H2NewMan : le modèle et les moyens), comparés colonne par colonne ; Worksheet 3
(les trois organisations de jeunesse, sources résumées par le cours) ; points de H2_CHECKS (la langue géorgienne n'a pas
été interdite ; Iejov et non Beria ou Molotov ; mot illisible devant « the crowd »).
Hors cours, dit comme tel : date du décret de mars 1938 sur le russe (déjà signalée par le site), record de Stakhanov
préparé à l'avance avec des mineurs qui l'assistaient, Jeunesses hitlériennes rendues réellement obligatoires en 1939.
Le DBQ porte sur le discours de Hitler de 1938 (Worksheet 3, source 2), tel que le cours le résume ; question et copies
modèles écrites pour la vidéo et dites comme telles.
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-4"
NOTION = "Totalitarian Regimes"
NUM = 4
TITRE = "The leader, the party and the New Man"
SUIVANT = "Episode 5 · Mass terror"
PRONONCIATION = {"Duce": "Doo-chay", "Führer": "Fyoo-rer", "Volksempfänger": "Folks-emp-feng-er",
                 "Riefenstahl": "Reefen-shtahl", "Goebbels": "Gurr-bels", "Mukhina": "Moo-khee-na", "Yezhov": "Yezh-off",
                 "Stakhanov": "Sta-khah-noff", "Stakhanovism": "Sta-khah-no-vism", "Balilla": "Ba-lee-la",
                 "Komsomol": "Kom-so-mol", "Giftpilz": "Gift-pilts", "Mischling": "Mish-ling", "Volk": "Folk",
                 "Lanzinger": "Lants-ing-er", "ha sempre ragione": "ah sem-pray ra-jo-nay",
                 "Credere, obbedire, combattere": "Cray-deh-ray, ob-beh-dee-ray, com-bah-teh-ray",
                 "Nazionale": "Nats-yo-nah-lay", "Reichstag": "Rikes-tahg", "Hindenburg": "Hin-den-boorg",
                 "Matteotti": "Mat-teh-ot-tee", "kolkhozes": "kol-hozes", "Kolkhoz": "Kol-hoz", "Wehrmacht": "Vair-markt",
                 "Ambrosi": "Am-bro-zee", "Heil": "Hile", "Beria": "Beh-ree-a", "Molotov": "Mollo-toff",
                 "Smolensk": "Smo-lensk", "Hoffmann": "Hoff-man", "NSDAP": "N S D A P"}

REG = ["IT", "DE", "SU"]     # marques des listes de comparaison : Italie fasciste, Allemagne nazie, URSS de Staline

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Nuremberg, September 1934. Hundreds of thousands of men in uniform, in perfect lines. Searchlights, flags, "
        "and one man on a platform. A film crew records everything, so that the whole of Germany can see it.",
        "{q1}Why build a cult around one man?",
        "{-q1}{q2}And why did these regimes want to take children from the age of ten?",
        "{-q2}{-g0}{plan}Today, part two of the chapter, points one and two. {plan.1}First, the story on the map, from 1922 to 1936. "
        "{plan.2}Then the cult of personality and the cult of the party: six ideas. "
        "{plan.3}Then total control over society and the creation of a New Man: six ideas, and Worksheet three. "
        "{plan.4}And the exam: an essay paragraph and a DBQ.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[24]),
        "q1": dict(type="question", t="Why a cult around one man?", bande=True),
        "q2": dict(type="question", t="Why take children at ten?", bande=True),
        "plan": dict(type="liste", titre="Episode 4 · the plan", items=[
            "On the map: leaders, parties and youth, 1922–1936", "II.1 · Cult of personality and cult of the party",
            "II.2 · Total control over society and the creation of a “New Man”",
            "At the exam: an essay paragraph and a DBQ"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 4", t="The leader, the party and the New Man",
                      sous="Cult, propaganda, youth · 1922 – 1936 · Part II.1 and II.2 of the course"),
    }),

    # ================================================================ la carte : 1922-1928
    dict(id="carte1", chap="On the map: 1922 – 1928", fond="nuit", humeur="tension",
         retenir="Oct. 1922 March on Rome · 1925 the dictatorship made legal · 1924–25 Leningrad, Stalingrad · 1926 Balilla · 1928 the first Five-Year Plan.",
         beats=[
        "{g1}{g1.1}October 1922. In Italy, the fascists march on Rome, and Mussolini becomes Prime Minister.",
        "{g1.2}In 1924, the socialist deputy Matteotti is murdered; in 1925, the fascistissime laws make the dictatorship legal. "
        "From now on there is one party, and one man: il Duce.",
        "{g1.3}At the same time, in the Soviet Union, Lenin dies, and his name is given to a city. "
        "Petrograd becomes Leningrad in 1924. And in 1925, another city is renamed after the new master: Stalingrad. "
        "The leader's name is written on the map itself.",
        "{g1.4}The next target is youth. In 1926, Italy founds the Opera Nazionale Balilla. The Soviet Union already has its Komsomol, "
        "created in 1918. Germany will follow.",
        "{g1.5}And in 1928, Stalin launches the first Five-Year Plan: the economy itself is now directed by the party.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[6, 8, 9, 11, 12]),
    }),

    # ================================================================ la carte : 1933-1936
    dict(id="carte2", chap="On the map: 1933 – 1936", fond="nuit", humeur="tension",
         retenir="30 Jan. 1933 Hitler chancellor · Sept. 1933 racial instruction in schools · 1934 Nuremberg rally filmed · 1935 Nuremberg laws · 1935 Stakhanov · 1936 Hitler Youth law.",
         beats=[
        "{g2}{g2.1}The thirtieth of January 1933. In Berlin, President Hindenburg appoints Hitler chancellor. "
        "Within months, the Nazis control the state, and they turn to society.",
        "{g2.2}In September 1933, racial instruction becomes compulsory in German schools. "
        "In September 1935, the Nuremberg laws define who is a citizen, and who is not, by ancestry.",
        "{g2.3}Nuremberg is also the city of the rallies. In 1934, Leni Riefenstahl films the party rally: Triumph of the Will. "
        "And a cheap people's radio brings the Führer's voice into every home.",
        "{g2.4}Meanwhile, in the Donbas, in 1935, a miner called Alexei Stakhanov is presented as a hero: "
        "he is said to have cut fourteen times his quota in one shift. The Soviet New Man is a worker.",
        "{-g2}{fr1}So, six dates to know. {fr1.1}1924 and 1925, Leningrad and Stalingrad. {fr1.2}1926, the Balilla. "
        "{fr1.3}September 1933, racial instruction in German schools. {fr1.4}1934, the Nuremberg rally filmed by Riefenstahl. "
        "{fr1.5}1935, the Nuremberg laws, and Stakhanov. {fr1.6}And 1936, the law on the Hitler Youth.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[20, 23, 24, 26]),
        "fr1": dict(type="frise", items=[
            dict(nom="Leningrad, Stalingrad", d=1924, q="1924–1925"), dict(nom="Balilla", d=1926, q="Italy"),
            dict(nom="Racial instruction", d=1933, q="September"), dict(nom="Triumph of the Will", d=1934, q="Nuremberg rally"),
            dict(nom="Nuremberg laws · Stakhanov", d=1935, q="1935"),
            dict(nom="Hitler Youth law", d=1936, q="Germany")]),
    }),

    # ================================================================ II.1, idée 1 : le Guide
    dict(id="guide", chap="II.1 · The leader, the Guide", fond="nuit", humeur="lumiere",
         retenir="The leader = an ideal man, the Guide, the incarnation of the nation: “il Duce”, “der Führer”, “the little father of the peoples”. Leningrad (1924), Stalingrad (1925). Lanzinger, The Standard Bearer (1934–36).",
         beats=[
        "{photo1}{def1}Now the course, idea by idea. Part two point one: the cult of personality and the cult of the party. "
        "Idea one. Totalitarian propaganda does not simply praise a politician: it manufactures {!a superior being}a superior being, "
        "the Guide. His qualities are those the people should acquire. "
        "{def1.1}He is soldier, worker, father and visionary at once. He is not the head of a government that could be replaced: "
        "he is the incarnation of the nation.",
        "{-def1}{noms}So the leader receives a title. {noms.1}Mussolini is il Duce, the leader. {noms.2}Hitler is der Führer, the guide. "
        "{noms.3}And Stalin is the little father of the peoples. {noms.4}Hubert Lanzinger even painted Hitler as a medieval knight "
        "in armour, carrying the flag: The Standard Bearer, painted between 1934 and 1936.",
        "{-noms}{-photo1}{g3}{g3.1}And the name goes onto the map. Petrograd had become Leningrad in 1924, after Lenin's death. "
        "In 1925, a city on the Volga was renamed Stalingrad. A city is no longer a place: it is a monument to a living man.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-stalin", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.15, .5, .3],
                       legende="Joseph Stalin on a tribune, Moscow, 1937 · Unknown photographer, public domain"),
        "def1": dict(type="def", cles=["superior", "Guide", "nation"], terme="Key term · cult of personality",
                     t="The systematic glorification of the leader: a superior being, the Guide, presented as the incarnation of the nation.",
                     etape="Soldier, worker, father and visionary at once: not a head of government who could be replaced", x=170, y=190, w=940),
        "noms": dict(type="liste", titre="Three leaders, three titles", marques=REG + ["✻"], items=[
            "Mussolini: “il Duce”, the leader", "Hitler: “der Führer”, the guide",
            "Stalin: “the little father of the peoples”",
            "Lanzinger: Hitler as a knight carrying the flag, The Standard Bearer (1934–36)"], x=150, y=130, w=980),
        "g3": dict(type="globe", code="H2", sc=[9]),
    }),

    # ================================================================ II.1, idée 2 : rassemblements et rituels
    dict(id="rituels", chap="II.1 · Rallies and rituals", fond="guerre", humeur="tension",
         retenir="Rallies, parades, salutes, mottos: an emotional bond with the leader. “Heil Hitler” · “Il Duce ha sempre ragione” · “Credere, obbedire, combattere” · Nuremberg 1934, Triumph of the Will · speeches of 3–4 hours.",
         beats=[
        "{g4}{g4.1}Idea two. The regimes govern by {!staging}staging. Rallies, parades, salutes and mottos turn political support "
        "into a collective physical experience. The individual feels dissolved into a disciplined crowd.",
        "{rit}{rit.1}In Germany, the official greeting becomes Heil Hitler, with the Nazi salute. "
        "{rit.2}In Italy, the motto says it all: il Duce ha sempre ragione, Mussolini is always right. "
        "{rit.3}Another fascist motto noted in class: Credere, obbedire, combattere. Believe, obey, fight. "
        "{rit.4}And the Nuremberg rally of 1934 is filmed by Leni Riefenstahl, in Triumph of the Will.",
        "{-rit}{-g4}{photo2}{disc}The class notes add one detail: Hitler's speeches lasted three to four hours, and held the crowd spellbound. "
        "{disc.1}The ritual is repeated until it becomes ordinary: a greeting, a gesture, a sentence learned by heart.",
        "{-disc}{mot1}Obedience is produced {!by emotion}by emotion, rather than by argument.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[24]),
        "rit": dict(type="liste", titre="Rituals of obedience", petit=True, bande=True, x=60, y=120, w=600,
                    marques=["DE", "IT", "IT", "DE"], items=[
            "“Heil Hitler” and the Nazi salute: the official greeting", "“Il Duce ha sempre ragione”: Mussolini is always right",
            "“Credere, obbedire, combattere”: believe, obey, fight", "Nuremberg rally, 1934: Riefenstahl, Triumph of the Will"]),
        "photo2": dict(type="tableau", img="h2-nuremberg-1936", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="The 'cathedral of light' over the Zeppelin Field, Nuremberg rally, September 1936 · Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE"),
        "disc": dict(type="note", terme="From the class notes", cles=["three", "spellbound"],
                     t="Hitler's speeches lasted three to four hours and held the crowd spellbound.",
                     etape="Repeated until it becomes ordinary: a greeting, a gesture, a sentence learned by heart", x=170, y=200, w=940),
        "mot1": dict(type="mot", t="Emotion, not argument", g="the ritual makes the crowd obey", y=260, taille=90),
    }),

    # ================================================================ II.1, idée 3 : médias et arts
    dict(id="medias", chap="II.1 · Media and arts in the regime's service", fond="nuit", humeur="tension",
         retenir="Propaganda everywhere: cinema, radio, painting, sculpture. The Volksempfänger (1938 advert). Paris 1937: Mukhina's Worker and Kolkhoz Woman facing the German pavilion. Goebbels, Hoffmann, Riefenstahl.",
         beats=[
        "{def2}Idea three. Propaganda works because it is {!everywhere}everywhere. Cinema, radio, painting and sculpture serve the regime. "
        "{def2.1}Art is judged not by its quality, but by its usefulness: it must show the ideal society as if it already existed.",
        "New technologies are made affordable on purpose, so that the leader's voice enters each household. "
        "A German advertisement of 1938, for the cheap people's radio, the Volksempfänger, promised:",
        "{-def2}",
        ("C", "Germany listens to the Führer thanks to the people's radio", "c_radio"),
        "{-c_radio}{paris}The arts too become a battlefield. At the Paris World Fair of 1937, {paris.g}the Soviet pavilion, "
        "crowned by Vera Mukhina's statue, the Worker and Kolkhoz Woman, {paris.d}stood directly facing the German pavilion. "
        "Two regimes, two ideal societies, in stone and steel.",
        "{-paris}{equipe}In Germany, the whole machine had a director. {equipe.1}Joseph Goebbels, the propaganda specialist. "
        "{equipe.2}Heinrich Hoffmann, Hitler's personal photographer. {equipe.3}And Leni Riefenstahl, for the films.",
    ], vis={
        "def2": dict(type="def", cles=["everywhere", "usefulness"], terme="Key term · propaganda",
                     t="Controlled information designed to shape opinion rather than to inform it: cinema, radio, painting, sculpture.",
                     etape="Art judged by its usefulness: the ideal society shown as if it already existed", x=170, y=190, w=940),
        "c_radio": dict(type="cit", a="Advertisement for the Volksempfänger", o="Germany, 1938", x=200, y=210, w=880),
        "paris": dict(type="cols", g="USSR", gq="Mukhina's Worker and Kolkhoz Woman on the Soviet pavilion",
                      d="Germany", dq="the German pavilion, directly facing it", vs="↔",
                      repere="Paris World Fair, 1937"),
        "equipe": dict(type="liste", titre="Nazi Germany · the propaganda machine", items=[
            "Joseph Goebbels, the propaganda specialist", "Heinrich Hoffmann, Hitler's personal photographer",
            "Leni Riefenstahl, the films (Triumph of the Will, 1934)"], x=170, y=170, w=940),
    }),

    # ================================================================ II.1, idée 4 : la censure
    dict(id="censure", chap="II.1 · Censorship rewrites the past", fond="nuit", humeur="mystere",
         retenir="The press controlled, criticism punished, the archive corrected. Yezhov, head of the NKVD, beside Stalin at the Moscow–Volga canal; executed in 1940, erased from the photograph.",
         beats=[
        "{photo3}{def3}Idea four. The cult only holds if nothing contradicts it. The press is controlled, and criticism is punished. "
        "{-photo3}{def3.1}And in the Soviet case, even the archive is corrected. The regime does not only forbid opposing opinions: "
        "it tries to make them {!unthinkable}unthinkable, by erasing the evidence that they ever existed.",
        "{-def3}{photo}The example is famous. A photograph shows Stalin at the Moscow–Volga canal, with Nikolai Yezhov, "
        "head of the NKVD, the political police, standing beside him. {photo.d}Yezhov is executed in 1940. "
        "And in the same image, retouched, he has simply disappeared. Only the water of the canal remains.",
        "{-photo}{err}Watch out: the class notes say that Beria and Molotov were executed. "
        "{err.1}In fact, Molotov never was, and Beria only in 1953. The head of the NKVD executed in 1940 was Yezhov, as Worksheet four says.",
    ], vis={
        "photo3": dict(type="tableau", img="h2-book-burning", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Nazi students burn books on the Opernplatz, Berlin, 10-11 May 1933 (outside the course) · Bundesarchiv, Bild 102-14597 / Georg Pahl, CC BY-SA 3.0 DE"),
        "def3": dict(type="def", cles=["press", "archive", "unthinkable"], terme="Key term · censorship",
                     t="The suppression of anything that contradicts the regime: the press controlled, criticism punished, the archive corrected.",
                     etape="Not only forbidden: opposing opinions made unthinkable", x=170, y=190, w=940),
        "photo": dict(type="cols", g="Before", gq="Stalin at the Moscow–Volga canal, Yezhov, head of the NKVD, beside him",
                      d="After 1940", dq="Yezhov executed… and erased from the same photograph", vs="→",
                      repere="The archive itself is corrected"),
        "err": dict(type="note", terme="Watch out · the class notes", cles=["Yezhov", "1940"],
                    t="Executed head of the NKVD: Yezhov, in 1940. Not Molotov (never executed), not Beria (executed in 1953).",
                    etape="Worksheet 4 gives Yezhov, executed in 1940", x=170, y=200, w=940),
    }),

    # ================================================================ II.1, idée 5 : le but
    dict(id="but", chap="II.1 · The purpose: nation, party, leader as one", fond="aube", humeur="tension",
         retenir="Nation = party = leader: opposition becomes treason, legitimacy no longer comes from elections. Symbols: the fasces (PNF, 1921), the swastika (NSDAP, 1920), the hammer and sickle (Soviet emblem, 1923).",
         beats=[
        "{eq}Idea five: the purpose. The cult of personality is not vanity: it is {!a technique of government}a technique of government. "
        "{eq.1}The regime identifies the nation with the party, {eq.2}and the party with one man.",
        "{eq.3}So any opposition looks like treason against the country itself, and the leader no longer needs an election.",
        "{-eq}{sym}Each regime condensed this identification into one symbol, adopted at the party's foundation or soon after. "
        "{sym.1}The Roman fasces, for the Fascist Party, in 1921. {sym.2}The swastika, for the NSDAP, in 1920. "
        "{sym.3}And the hammer and sickle, on the Soviet state emblem, in 1923.",
        "{-sym}{mot2}Remember the formula of the schema: criticising the leader becomes {!betraying the country}betraying the country.",
    ], vis={
        "eq": dict(type="liste", titre="A technique of government", cles=["nation", "party", "treason"], marques=["1", "2", "→"], items=[
            "The nation = the party", "The party = one man",
            "Opposition = treason against the country; no need for elections"], x=170, y=160, w=940),
        "sym": dict(type="liste", titre="One symbol for each party", marques=REG, items=[
            "The Roman fasces: National Fascist Party, 1921", "The swastika: NSDAP, 1920",
            "The hammer and sickle: Soviet state emblem, 1923"], x=170, y=170, w=940),
        "mot2": dict(type="mot", t="Leader = party = nation", g="criticising the leader becomes betraying the country", y=260, taille=86),
    }),

    # ================================================================ II.1, idée 6 : le petit père des peuples
    dict(id="langue", chap="II.1 · The “little father of the peoples”", fond="nuit", humeur="tension",
         retenir="Stalin, the protective father of all the nations of the USSR… who imposed one language: Russian, compulsory in every school from March 1938 (date outside the course). Georgian was not banned.",
         beats=[
        "{g5}{g5.1}Idea six. Stalin's cult presented him as the protective father of all the nations of the Soviet Union, "
        "a multinational union, from Ukraine to Central Asia.",
        "{-g5}{fam}But behind the image, the father imposed {!one culture}one culture. {fam.g}Stalin was Georgian himself. "
        "{fam.d}Yet he made Russian the language of the whole Union, and the Georgians were pushed to study even their own texts "
        "in Russian, and to speak Russian. The cult of one man went together with the forced unification of a whole empire.",
        "{-fam}{dat}The example. From March 1938, learning Russian became compulsory in every school of the Soviet Union, "
        "including in the national republics, such as Georgia. The date of that decree comes from outside the course. "
        "{dat.1}And one correction: the class notes say that Stalin banned the Georgian language. He did not. "
        "Georgian remained the official language of the Georgian republic: what was imposed was Russian, as the common language.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[9]),
        "fam": dict(type="cols", g="The image", gq="a protective father of all the nations of the USSR",
                    d="The reality", dq="one language for all: Russian, even for the Georgians", vs="≠",
                    repere="Stalin, a Georgian, imposed Russian"),
        "dat": dict(type="note", terme="Watch out · a correction", cles=["compulsory", "banned"],
                    t="March 1938: Russian compulsory in every school of the USSR (date outside the course).",
                    etape="Georgian was not banned: it remained the official language of the Georgian SSR", x=170, y=200, w=940),
    }),

    # ================================================================ h2cult : trois chefs, trois cultes
    dict(id="h2cult", chap="Schema · Three leaders, three cults", fond="aube", humeur="calme",
         retenir="Same machinery, three contents: Duce / Führer / little father · “Il Duce ha sempre ragione” / “Heil Hitler” / “Thank you Comrade Stalin, for our happy childhood” · fasces / swastika / hammer and sickle · aviator portrait / Riefenstahl / retouched photographs.",
         beats=[
        "{c1}Now the schema of the course: three leaders, three cults, compared row by row. "
        "{c1.1}The name: il Duce, {c1.2}der Führer, {c1.3}the little father of the peoples.",
        "{-c1}{c2}{c2.1}The motto: il Duce ha sempre ragione. {c2.2}Heil Hitler. "
        "{c2.3}And in the Soviet Union: Thank you Comrade Stalin, for our happy childhood.",
        "{-c2}{c3}{c3.1}The symbol: the fasces, {c3.2}the swastika, {c3.3}the hammer and sickle.",
        "{-c3}{c4}{c4.1}The staging: Mussolini painted as an aviator, by Ambrosi, in 1930. "
        "{c4.2}The Nuremberg rallies and the people's radio. "
        "{c4.3}Socialist realism, retouched photographs, and Stalingrad.",
        "{-c4}{bil}The conclusion of the schema. {!The contents differ, the procedure is identical}The contents differ, "
        "the procedure is identical: identify the nation with the party, and the party with one man.",
        ("P", 2.5),
    ], vis={
        "c1": dict(type="liste", titre="1 · The name of the leader", marques=REG, items=[
            "“il Duce”", "“der Führer”", "“the little father of the peoples”"], x=170, y=150, w=940),
        "c2": dict(type="liste", titre="2 · Greeting / motto", marques=REG, items=[
            "“Il Duce ha sempre ragione” (Mussolini is always right)", "“Heil Hitler” with the Nazi salute, the official greeting",
            "“Thank you Comrade Stalin, for our happy childhood”"], x=150, y=150, w=980),
        "c3": dict(type="liste", titre="3 · The party symbol", marques=REG, items=[
            "The Roman fasces", "The swastika", "The hammer and sickle"], x=170, y=150, w=940),
        "c4": dict(type="liste", titre="4 · The staging", marques=REG, items=[
            "Portrait as an aviator (Ambrosi, 1930); party parades",
            "Nuremberg rallies filmed by Riefenstahl (1934); the people's radio (1938)",
            "Socialist realism; retouched photographs; Stalingrad (1925)"], x=150, y=150, w=980),
        "bil": dict(type="note", terme="Three leaders, three cults · the same machinery", cles=["identical", "nation", "one"],
                    t="The contents differ, the procedure is identical: identify the nation with the party, and the party with one man.",
                    etape="So that criticising the leader becomes betraying the country", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 1 : produire un homme nouveau
    dict(id="nouveau", chap="II.2 · Not obedient subjects: a New Man", fond="nuit", humeur="lumiere",
         retenir="A dictatorship demands that you keep quiet; a totalitarian regime demands that you change. Three models: the German Volk, a purified race (sterilisation law, 1933) · the Soviet worker (Stakhanov, 1935) · the fascist, strong and cultured, serving the Party.",
         beats=[
        "{cmp}Part two point two: total control over society, and the creation of a New Man. Idea one: "
        "what separates a totalitarian regime from an ordinary dictatorship. "
        "A dictatorship demands that you {!keep quiet}keep quiet. {cmp.d}A totalitarian regime demands that you {!change}change.",
        "{-cmp}{def4}The ideology defines a model of humanity, and the whole machinery of the state, school, leisure, work, family, law, "
        "is turned towards producing it. {def4.1}Private life has no protected space left.",
        "{-def4}{mod}And each regime had its own model. {mod.1}In Germany, the New Man was a purified race, the Volk. "
        "That led to the sterilisation law of 1933. {mod.2}In the Soviet Union, a worker, celebrated from 1935 through the miner Stakhanov. "
        "{mod.3}In Italy, a man strong and cultured, in the service of the Party.",
    ], vis={
        "cmp": dict(type="cols", g="Dictatorship", gq="demands that you keep quiet", d="Totalitarianism", dq="demands that you change",
                    vs="≠", repere="The New Man: the human being remade by the ideology"),
        "def4": dict(type="def", cles=["model", "machinery", "Private"], terme="Key term · “New Man”",
                     t="The model human being each ideology claims to produce; the whole machinery of the state is turned towards it.",
                     etape="School, leisure, work, family, law: private life has no protected space left", x=170, y=190, w=940),
        "mod": dict(type="liste", titre="Three models of the New Man", marques=REG, items=[
            "Strong and cultured, in the service of the Party",
            "A purified race, the Volk → the sterilisation law (1933)",
            "A worker → celebrated through Stakhanov (1935)"], x=150, y=160, w=980),
    }),

    # ================================================================ II.2, idée 2 : la jeunesse
    dict(id="jeunesse", chap="II.2 · Youth comes first", fond="guerre", humeur="tension",
         retenir="Balilla (1926) · Hitler Youth, law of 1936, ≈ 8 million members by 1939 · Komsomol (1918). Mussolini: “I take men in the cradle…”. Hitler, 1938: ten years old → Young Folk (4 years) → Hitler Youth (4 years) → Labour Service → Wehrmacht.",
         beats=[
        "{g6}{g6.1}Idea two: youth comes first, because children can be shaped {!before they can judge}before they can judge. "
        "All three regimes built youth organisations that took over the time outside school: "
        "uniforms, camps, sport, songs, and political instruction.",
        "{org}{org.1}Italy founded the Opera Nazionale Balilla in 1926. {org.2}Germany made the Hitler Youth compulsory by the law of 1936, "
        "and it counted about eight million members by 1939. {org.3}The Soviet Union had the Komsomol, created in 1918. "
        "{org.4}The aim: to form the next generation directly, bypassing the family and the church.",
        "{-org}{-g6}{nuance}A precision from outside the course: the law of 1936 made the Hitler Youth the official youth of the state, "
        "but membership became truly compulsory only in 1939. {nuance.1}Mussolini summed up the ambition:",
        "{-nuance}",
        ("C", "I take men in the cradle and I do not return them to the pope until after their death.", "c_muss"),
        "{-c_muss}{chaine}And Hitler described the chain himself, in a speech of 1938: Worksheet three, source two. "
        "{chaine.1}Children enter at ten. {chaine.2}Four years in the Young Folk. {chaine.3}Four years in the Hitler Youth. "
        "{chaine.4}Then the Labour Service. {chaine.5}And whatever class consciousness or pride of status is still left, "
        "the Wehrmacht will take care of it. From the age of ten, the regime never lets go.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[11]),
        "org": dict(type="liste", titre="Youth organisations", petit=True, bande=True, x=60, y=120, w=600,
                    marques=REG + ["→"], items=[
            "Opera Nazionale Balilla, 1926", "Hitler Youth: law of 1936, ≈ 8 million members by 1939",
            "Komsomol, 1918", "Bypassing the family and the church"]),
        "nuance": dict(type="note", terme="A precision · outside the course", cles=["official", "1939"],
                       t="The 1936 law made the Hitler Youth the state's official youth; membership became truly compulsory in 1939.",
                       etape="The course writes “compulsory by the law of 1936”: both dates can be quoted", x=170, y=200, w=940),
        "c_muss": dict(type="cit", a="Benito Mussolini", o="quoted in the course", x=200, y=200, w=880),
        "chaine": dict(type="liste", titre="Hitler, 1938 · the chain (Worksheet 3, source 2)", items=[
            "Age 10: children enter", "4 years in the Young Folk", "4 years in the Hitler Youth", "Then the Labour Service",
            "“The Wehrmacht will take care of” what is left"], x=170, y=120, w=940),
    }),

    # ================================================================ II.2, idée 3 : l'école
    dict(id="ecole", chap="II.2 · School: ideology taught as science", fond="nuit", humeur="tension",
         retenir="Education rewritten: textbooks, children's books, lessons carry the ideology. Germany: racial instruction compulsory from September 1933; Der Giftpilz (Nuremberg, 1938). A child learns to see the enemy before meeting one.",
         beats=[
        "{g7}{g7.1}Idea three. Thought, culture and information are controlled, and the school teaches the ideology {!as science}as science. "
        "Education is not merely censored: it is rewritten.",
        "{-g7}{eco1}{eco1.1}Textbooks, children's books and lessons carry the ideology, in a form suitable for the youngest. "
        "{eco1.2}In Germany, racial doctrine was taught as if it were a natural science, with charts, measurements and classifications. "
        "{eco1.3}Racial instruction became compulsory in German schools in September 1933.",
        "{eco1.4}The course's example is an antisemitic children's book, Der Giftpilz, The Poisonous Mushroom, published in Nuremberg in 1938. "
        "It taught children to recognise Jews by invented physical features. {-eco1}{mot3}A child thus learns {!to see the enemy}to see the enemy, "
        "before ever meeting one.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[23]),
        "eco1": dict(type="liste", titre="The school of the ideology", cles=["children's", "science", "compulsory"], items=[
            "Textbooks, children's books and lessons carry the ideology", "Racial doctrine taught as a natural science: charts, measurements",
            "Racial instruction compulsory in German schools, September 1933",
            "Der Giftpilz, “The Poisonous Mushroom” (Nuremberg, 1938)"], x=150, y=130, w=980),
        "mot3": dict(type="mot", t="The enemy, taught", g="seen before ever being met", y=260, taille=96),
    }),

    # ================================================================ II.2, idée 4 : la loi
    dict(id="loi", chap="II.2 · The law sorts human beings", fond="guerre", humeur="tension",
         retenir="Nuremberg laws, 15 Sept. 1935: no marriage or relations between Jews and “persons of German blood”; citizenship by descent. Official table: German-blooded · Mischling 2nd degree (1/4) · Mischling 1st degree (1/2) · Jew (3/4 or more): refused Reich citizenship.",
         beats=[
        "{def5}Idea four. In Nazi Germany, the ideology became {!legislation}legislation. The Nuremberg laws of the fifteenth of September 1935 "
        "forbade marriage and sexual relations between Jews and what they called persons of German blood. "
        "{def5.1}They banned Jewish households from employing young German women, and forbade Jews to fly the Reich flag.",
        "{-def5}{tab}So the state defined citizenship by descent, and the administration produced the tables to apply it. "
        "An official table of 1935 classified people by fractions of ancestry. {tab.1}German-blooded. "
        "{tab.2}Mischling of the second degree: one quarter Jewish, one Jewish grandparent. "
        "{tab.3}Mischling of the first degree: half Jewish, two Jewish grandparents. "
        "{tab.4}And Jew: three quarters or more. That last category was refused Reich citizenship altogether.",
        "{-tab}{lien}At school, the child learns the categories; in the law, the state applies them. "
        "{lien.1}A human being is defined by his ancestry.",
    ], vis={
        "def5": dict(type="def", cles=["marriage", "descent"], terme="Key term · the Nuremberg laws (15 September 1935)",
                     t="No marriage or sexual relations between Jews and “persons of German blood”: citizenship defined by descent.",
                     etape="Also: no young German women employed by Jewish households; Jews forbidden to fly the Reich flag", x=170, y=190, w=940),
        "tab": dict(type="liste", titre="An official table of 1935", marques=["0", "¼", "½", "¾"], items=[
            "German-blooded", "Mischling of the 2nd degree: one Jewish grandparent", "Mischling of the 1st degree: two Jewish grandparents",
            "“Jew”: three or four Jewish grandparents → refused Reich citizenship"], x=150, y=140, w=980),
        "lien": dict(type="note", terme="For the essay", cles=["school", "law", "ancestry"],
                     t="At school the child learns the categories; in the law the state applies them.",
                     etape="A human being defined by his ancestry, not by what he does", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 5 : travail, loisirs, économie
    dict(id="travail", chap="II.2 · Work, leisure and the economy absorbed", fond="nuit", humeur="lumiere",
         retenir="Unions dissolved, leisure organised by the state, the economy directed (USSR: Five-Year Plans, collectivisation; Germany: rearmament, autarky). Stakhanov, 1935: 14 times his quota in one shift → Stakhanovism.",
         beats=[
        "{abs}Idea five. Work, leisure and the economy are absorbed too, so that {!nothing stands outside the regime}nothing stands outside the regime. "
        "{abs.1}Independent trade unions are dissolved. {abs.2}Leisure organisations are created by the state. "
        "{abs.3}The economy is directed towards the regime's goals: collectivisation and Five-Year Plans in the Soviet Union, rearmament and autarky in Germany. "
        "{abs.4}Even sports clubs and charities are absorbed or suppressed.",
        "{-abs}{g8}{g8.1}The example: the Soviet New Man had his hero. In 1935, in the Donbas, the miner Alexei Stakhanov was presented "
        "as having cut fourteen times his quota of coal in one shift.",
        "{-g8}{gs}Look at the scale. {gs.1}{gs.2}The quota of one shift. {gs.3}{gs.4}And the record announced by the regime: fourteen times more.",
        "{-gs}{photo4}{stak}His name became a word: {!Stakhanovism}Stakhanovism, the cult of the record-breaking worker, "
        "{stak.1}and competitions were imposed in every factory. "
        "From outside the course: the record was prepared in advance, with other miners assisting him.{-photo4}",
    ], vis={
        "abs": dict(type="liste", titre="Nothing outside the regime", cles=["unions", "Leisure", "directed", "absorbed"], items=[
            "Independent trade unions dissolved", "Leisure organisations created by the state",
            "The economy directed: Five-Year Plans, collectivisation · rearmament, autarky",
            "Civil society absorbed or suppressed: no one between the individual and the party"], x=150, y=130, w=980),
        "g8": dict(type="globe", code="H2", sc=[26]),
        "gs": dict(type="graphe", titre="Stakhanov's record, 1935 (as presented by the regime)", x=340, y=110, w=600, h=520,
                   ax=dict(x=[0.35, 2.65], y=[0, 16], gx=[], gy=[], lx="", ly=""),
                   el=[dict(type="texte", x=1.0, y=-1.1, t="The quota", c="iv"),
                       dict(type="droite", pts=[[1.0, 0.68], [1.0, 0.75]], c="el", ep=34, dur=0.6, lbl="× 1", lp=[1.0, 2.0]),
                       dict(type="texte", x=2.0, y=-1.1, t="Stakhanov's shift", c="iv"),
                       dict(type="droite", pts=[[2.0, 0.68], [2.0, 13.3]], c="ca", ep=34, dur=1.4, lbl="× 14", lp=[2.0, 15.0])]),
        "photo4": dict(type="tableau", img="h2-stakhanov", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.15, .5, .4],
                       legende="Alexei Stakhanov (centre) explains his method to a fellow miner, USSR, 1930s · Eleazar Langman, public domain"),
        "stak": dict(type="def", cles=["record", "factory"], terme="Key term · Stakhanovism",
                     t="The Soviet cult of the record-breaking worker, named after the miner Stakhanov (1935).",
                     etape="Competitions imposed in every factory · the record prepared in advance (outside the course)", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 6 : trois hommes nouveaux
    dict(id="trois", chap="II.2 · Three New Men for three supreme goals", fond="aube", humeur="calme",
         retenir="Same method (children taken early, uniforms, camps, ideology), different ideals: race (strong, obedient, “Aryan”, social Darwinism) · class (a well-educated worker who studied Marx and Lenin) · nation (ready to fight, cold-blooded, Latin and Plutarch, heir of Rome).",
         beats=[
        "{nuage}Idea six: three New Men, for three supreme goals. Worksheet three compares the three youth organisations. "
        "The method is the same: {nuage.1}take the children early, {nuage.2}uniforms, {nuage.3}camps, {nuage.4}ideology. But the ideal differs.",
        "{-nuage}{buts}{buts.1}The Nazis wanted strong, obedient, educated and Aryan children, in the service of the Volk. "
        "The basis is {!social Darwinism}social Darwinism: the stronger races survive. The goal: {!race}race. "
        "{buts.2}The Soviet New Man was a well-educated worker, who had studied Marx and Lenin. The goal: {!class}class. "
        "{buts.3}The Fascist New Man was ready to fight, calm and cold-blooded, nourished on Latin and Plutarch, as the heir of Rome. "
        "The goal: {!nation}the nation.",
        "{-buts}{src}The sources of the Worksheet. {src.1}A Hitler Youth poster of 1935: Youth serves the Führer! "
        "All ten-year-olds into the Hitler Youth. {src.2}The programme of the Smolensk Komsomol, in 1919: turn young "
        "workers and peasants into revolutionaries. "
        "{src.3}And a photograph of 1936 of the Opera Nazionale Balilla: boys in black uniforms, carrying rifles.",
    ], vis={
        "nuage": dict(type="nuage", centre="The same method", items=["children taken early", "uniforms", "camps", "ideology"]),
        "buts": dict(type="liste", titre="Three supreme goals", marques=["DE", "SU", "IT"], cles=["race", "class", "nation"], items=[
            "Race: strong, obedient, “Aryan” children for the Volk (social Darwinism)",
            "Class: a well-educated worker who studied Marx and Lenin",
            "Nation: ready to fight, cold-blooded, Latin and Plutarch, heir of Rome"], x=150, y=150, w=980),
        "src": dict(type="liste", titre="Worksheet 3 · the sources", marques=["DE", "SU", "IT"], items=[
            "Hitler Youth poster, 1935: “Youth serves the Führer! All ten-year-olds into the Hitler Youth”",
            "Smolensk Komsomol programme, 1919: young workers and peasants turned into “revolutionaries”",
            "Opera Nazionale Balilla, photograph, 1936: boys in black uniforms, carrying rifles"], x=150, y=140, w=980),
    }),

    # ================================================================ h2newman : le modèle et les moyens
    dict(id="h2newman", chap="Schema · Manufacturing a “New Man”", fond="aube", humeur="calme",
         retenir="Model: servant of the Party / the Volk, eugenics / the worker, Stakhanovism · Youth: Balilla / Hitler Youth 10–18 / Komsomol · School: race taught from 1938 / racial instruction 1933, Der Giftpilz / socialist realism · Economy: corporatism, autarky after 1935 / rearmament, Four-Year Plan 1936 / Five-Year Plans, kolkhozes.",
         beats=[
        "{n1}The second schema: manufacturing a New Man, the model and the means. Again, row by row. "
        "{n1.1}The model: a servant of the Party, {n1.2}a purified race and eugenics, {n1.3}a worker and Stakhanovism.",
        "{-n1}{n2}{n2.1}Youth: the Balilla, then the fascist youth up to eighteen. "
        "{n2.2}The Hitler Youth, from ten to eighteen. {n2.3}The Komsomol, down to the villages.",
        "{-n2}{n3}{n3.1}School and culture: in Italy, the opposition press suppressed, and from 1938, the teaching of race. "
        "{n3.2}Racial instruction in Germany from 1933. {n3.3}Socialist realism imposed on Soviet arts.",
        "{-n3}{n4}{n4.1}The economy: corporatism, and autarky after 1935. "
        "{n4.2}Rearmament, and the Four-Year Plan of 1936. "
        "{n4.3}Five-Year Plans, collectivisation, kolkhozes.",
        "{-n4}{bil2}And the conclusion of the schema: {!a dictatorship demands silence, totalitarianism demands transformation}"
        "a dictatorship demands silence, totalitarianism demands transformation.",
        ("P", 2.5),
    ], vis={
        "n1": dict(type="liste", titre="1 · The model of the New Man", marques=REG, items=[
            "Strong and cultured, in the service of the Party", "A purified race, the Volk → eugenics", "A worker → Stakhanovism"],
            x=170, y=150, w=940),
        "n2": dict(type="liste", titre="2 · Organised youth", marques=REG, items=[
            "Balilla, then fascist youth up to 18", "Hitler Youth, compulsory from 10 to 18",
            "Komsomol, political instruction down to the villages"], x=170, y=150, w=940),
        "n3": dict(type="liste", titre="3 · School and culture", marques=REG, items=[
            "Opposition press suppressed; from 1938, teaching of “race”",
            "Racial instruction compulsory from Sept. 1933; Der Giftpilz (1938)", "Socialist realism imposed on the arts"],
            x=150, y=150, w=980),
        "n4": dict(type="liste", titre="4 · The economy", marques=REG, items=[
            "Corporatism, autarky after 1935", "Rearmament, autarky, Four-Year Plan (1936)",
            "Five-Year Plans from 1928, collectivisation, kolkhozes"], x=170, y=150, w=940),
        "bil2": dict(type="note", terme="Manufacturing a “New Man” · the conclusion", cles=["silence", "transformation"],
                     t="A dictatorship demands silence; totalitarianism demands transformation.",
                     etape="Mussolini: “I take men in the cradle…”", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : un paragraphe d'essay
    dict(id="essai", chap="Your turn · an essay paragraph", fond="aube", humeur="calme",
         retenir="Explain: a topic sentence (one aim, a New Man) · youth (Balilla, Hitler Youth, Komsomol; Hitler 1938) · school and law (1933, Nuremberg laws) · work (Stakhanov) · the link back (transformation, not only obedience).",
         beats=[
        "{ex1}Your turn. Here is an Explain question, written for this video. "
        "{!Explain}Explain how the totalitarian regimes tried to create a New Man.",
        "{-ex1}{met}The method. {met.1}A topic sentence that answers the question. "
        "{met.2}Several means, each with a precise example. {met.3}A sentence that links back.",
        "{-met}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod1}Here is a model paragraph. "
        "{mod1.1}The totalitarian regimes did not want obedient subjects: they tried to manufacture a New Man, shaped by their ideology. "
        "{mod1.2}First, they captured youth before it could judge: the Balilla in 1926, the Komsomol, "
        "and the Hitler Youth, about eight million members by 1939. "
        "{mod1.3}Second, they rewrote education and the law: racial instruction in German schools from September 1933, "
        "the Nuremberg laws of 1935. "
        "{mod1.4}Third, they absorbed work: in 1935, the miner Stakhanov became the model of the Soviet worker. "
        "{mod1.5}The ideals differed, race, class or nation, but the aim was the same: total transformation, not only obedience.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explain how the totalitarian regimes tried to create a “New Man”.",
                    src="Question written for this video, on Part II.2", enonce=["One paragraph: topic sentence, means and examples, link back"]),
        "met": dict(type="liste", titre="An Explain paragraph", cles=["topic", "example", "links"], items=[
            "A topic sentence that answers the question", "Several means, each with a precise example from the three regimes",
            "A final sentence that links back to the question"], x=150, y=150, w=980),
        "pa1": dict(type="pause", t="Write the paragraph: a topic sentence, three means with examples, a link back.",
                    sous="Pause the video, write it on a sheet, then play on for a model."),
        "mod1": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "Not obedient subjects: a New Man shaped by the ideology",
            "Youth: Balilla (1926), Komsomol, Hitler Youth (≈ 8 million by 1939); Hitler's chain, 1938",
            "School and law: racial instruction (Sept. 1933); Nuremberg laws (1935)",
            "Work: Stakhanov, model of the Soviet worker (1935)",
            "Race, class or nation: the same aim, transformation"], x=130, y=110, w=1020),
    }),

    # ================================================================ à toi : un DBQ a)
    dict(id="dbq", chap="Your turn · a DBQ", fond="guerre", humeur="tension",
         retenir="DBQ a): judgement in the first line · the document in one sentence · strengths (the dictator himself, the whole chain, the intention) · limits (a speech, not the reality; one regime; no figures; no voice of the young).",
         beats=[
        "{ex2}Now a DBQ, part a), on a source of Worksheet three. {!How useful}How useful is Hitler's speech of 1938, describing the path "
        "of German youth, for understanding how the Nazi regime controlled young people?",
        "{-ex2}{str}The structure. {str.1}First line: the judgement. "
        "{str.2}The document in one sentence. {str.3}Strengths. {str.4}Limits.",
        "{-str}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep}A model. {rep.1}This speech is significantly useful for understanding how the Nazi regime controlled young people. "
        "{rep.2}It is a speech given by Hitler himself in 1938, describing the path of a German child from the age of ten to the army.",
        "{rep.3}Its strengths. It comes from the dictator himself, so it shows the intention of the regime at the highest level. "
        "It describes the whole chain, from the Young Folk to the Wehrmacht. "
        "And its last words show that the aim was to erase any other loyalty, of class or status.",
        "{rep.4}Its limits. It is a speech, so it shows what the regime wanted, not what young people actually lived. "
        "No figures: the course's eight million members by 1939 are needed. Only Germany. "
        "And no voice of the families or of the young. Useful for the aims, much less for the reality.",
    ], vis={
        "ex2": dict(type="exo", niveau="dbq", titre="How useful is Hitler's 1938 speech for understanding how the Nazi regime controlled young people?",
                    src="Question written for this video, on Worksheet 3 (source 2, as summarised in the course)", enonce=["Part a) of a DBQ"],
                    donnees=["Hitler, 1938: children enter at ten · 4 years in the Young Folk · 4 years in the Hitler Youth · the Labour Service · “the Wehrmacht will take care of” what is left"]),
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Write the first line and the sentence that presents the document, then the strengths and the limits.",
                    sous="Pause the video, write your answer, then play on for a model."),
        "rep": dict(type="liste", titre="A model answer", items=[
            "Significantly useful for understanding how the regime controlled young people",
            "A speech by Hitler himself, 1938: the path of a German child from ten to the army",
            "Strengths: the dictator's own intention · the whole chain · erase every other loyalty",
            "Limits: aims, not reality · no figures (8 million) · Germany only · no voice of the young"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}The leader: a Guide, il Duce, der Führer, the little father of the peoples; cities renamed, "
        "Leningrad and Stalingrad. {carte.2}The means of the cult: rallies and rituals, media and arts, censorship that rewrites the past, "
        "Yezhov erased. {carte.3}The purpose: leader, party and nation as one, so that opposition becomes treason. "
        "{carte.4}And the New Man: youth taken at ten, school and law, Nuremberg 1935, work and Stakhanov; race, class, nation.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: mass terror. The political police, the show trials, the camps… and the terror that devours its own.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LEADER · PARTY · NEW MAN", branches=[
            dict(t="The Guide", items=["Duce · Führer · little father", "Leningrad 1924 · Stalingrad 1925", "The Standard Bearer"]),
            dict(t="The cult's means", items=["rallies · “Heil Hitler”", "radio · Riefenstahl · Paris 1937", "Yezhov erased (1940)"]),
            dict(t="Purpose", items=["nation = party = leader", "opposition = treason", "fasces · swastika · hammer and sickle"]),
            dict(t="The New Man", items=["Balilla · Hitler Youth · Komsomol", "Sept. 1933 · Nuremberg laws 1935", "Stakhanov · race, class, nation"])]),
        "fin": dict(type="mot", t="Next: mass terror", g="Episode 5 · police, show trials, camps", y=270, taille=80),
    }),
]

QUIZ = [
    dict(q="According to the course, what does totalitarian propaganda make of the leader?",
         r=["A superior being, the Guide, the incarnation of the nation", "A head of government who can be replaced at the next election",
            "A constitutional monarch", "A spokesman of the parliament"], ok=0, voir="def1",
         ex="He is shown as soldier, worker, father and visionary at once."),
    dict(q="Which city was renamed after the Soviet leader in 1925?",
         r=["Stalingrad", "Leningrad", "Petrograd", "Smolensk"], ok=0, voir="noms",
         ex="Petrograd had become Leningrad in 1924, after Lenin's death."),
    dict(q="What does the fascist motto “Il Duce ha sempre ragione” mean?",
         r=["Mussolini is always right", "Believe, obey, fight", "Everything is in the State", "Youth serves the leader"], ok=0, voir="rit",
         ex="“Credere, obbedire, combattere” means believe, obey, fight."),
    dict(q="What happened to Yezhov, head of the NKVD, after his execution in 1940?",
         r=["He was erased from a photograph taken beside Stalin", "He was replaced by Molotov", "He became a hero of Soviet labour",
            "His name was given to a city"], ok=0, voir="photo",
         ex="Molotov was never executed; Beria was executed only in 1953."),
    dict(q="Which symbol did the NSDAP adopt in 1920?",
         r=["The swastika", "The Roman fasces", "The hammer and sickle", "The black shirt"], ok=0, voir="sym",
         ex="The fasces: Fascist Party (1921); the hammer and sickle: Soviet emblem (1923)."),
    dict(q="What separates a totalitarian regime from an ordinary dictatorship, according to the course?",
         r=["It demands that you change, not only that you keep quiet", "It has a single party", "It has a political police",
            "It holds no elections"], ok=0, voir="cmp",
         ex="The aim is a New Man: private life has no protected space left."),
    dict(q="Which youth organisation was founded in Italy in 1926?",
         r=["The Opera Nazionale Balilla", "The Komsomol", "The Hitler Youth", "The Young Folk"], ok=0, voir="org",
         ex="The Komsomol dates from 1918; the Hitler Youth law from 1936."),
    dict(q="What did the Nuremberg laws of 15 September 1935 do?",
         r=["Define citizenship by descent and forbid marriage between Jews and “persons of German blood”",
            "Make racial instruction compulsory in schools", "Create the Hitler Youth", "Launch the Four-Year Plan"], ok=0, voir="def5",
         ex="Racial instruction became compulsory in September 1933."),
    dict(q="What was Stakhanov presented as having done in 1935?",
         r=["Cut fourteen times his quota of coal in one shift", "Built the White Sea Canal", "Founded the Komsomol",
            "Painted the Soviet pavilion of 1937"], ok=0, voir="gs",
         ex="His name gave Stakhanovism, the cult of the record-breaking worker."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H2 · Parts II.1 and II.2, Worksheet 3, schemas “Three leaders, three cults” and “Manufacturing a New Man”) as written on the site; corrections of the class notes from the site's checks; outside the course and said so: the date of the 1938 decree on Russian, the preparation of Stakhanov's record, the Hitler Youth made truly compulsory in 1939; the essay and DBQ questions and model answers written for this video; animated map of chapter 2 (site).",
    "Photographs (via Wikimedia Commons): Joseph Stalin, Moscow, 1937 (unknown photographer, public domain); the Nuremberg rally of September 1936 (Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE); the book burning on the Opernplatz, Berlin, May 1933 (Georg Pahl, Bundesarchiv, Bild 102-14597, CC BY-SA 3.0 DE; the event is outside the course); Alexei Stakhanov explaining his method (Eleazar Langman, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
