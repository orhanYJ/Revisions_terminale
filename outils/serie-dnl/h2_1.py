"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 1 : « What is totalitarianism? » (l'introduction du
chapitre : « Defining totalitarianism: a debate and a definition », six idées, schémas h2wheel, h2europe, h2reads).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo et la série H3 :
outils/serie-philo/generer.py h2_1 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 0 définition, trois régimes · 1 brutalisation · 2 Russie 1917 · 6 marche sur Rome · 13 deux crises (1929) ·
       16 les nazis premier parti · 19 Holodomor · 20 Hitler chancelier · 28 Rhénanie · 29 Axe, Espagne ·
       31 apaisement (l'Europe des régimes, 1937-1938) · 33 Anschluss · 34 Munich · 36 pacte germano-soviétique ·
       37 attaque de la Pologne
Contenu : section « Intro » du chapitre dans le site (dnl/index.html, CHAPTERS.H2) : 1929 et les deux crises, le débat
des historiens (Taylor, Hehn, Winter), la définition en trois parties et la roue des sept traits (H2Wheel), l'idéologie
et le discours de Staline du 7 janvier 1933, Arendt et la confiance des masses, trois régimes et une trajectoire,
l'Europe des régimes vers 1938 (H2EuropeMap), la bibliographie de M. Ros (H2Reads) ; chiffres du vote nazi tirés de I.2.
Ce qui n'est pas dans le cours est dit « outside the course » (nuance sur « all ended in failure », chute de l'URSS en 1991).
Erreur du cours corrigée : la roue des traits est attribuée à « MacDougal Littell » ; l'éditeur s'appelle McDougal Littell.
Plan : ouverture (questions sur le globe, plan des neuf épisodes, titre) → la chronologie 1914-1939 sur la carte →
le cours (idées 1 à 6) → la bibliographie → une pause « Your turn » (définir le totalitarisme en un paragraphe) → récap.
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-1"
NOTION = "Totalitarian Regimes"
NUM = 1
TITRE = "What is totalitarianism?"
SUIVANT = "Episode 2 · From the Great War to power"
PRONONCIATION = {"Arendt": "Ah-rent", "Hehn": "Hayn", "Duce": "Doo-chay", "Führer": "Fyoo-rer", "Weimar": "Vy-mar",
                 "Holodomor": "Kho-lo-do-mor", "Reichstag": "Rikes-tahg", "Anschluss": "Ahn-shloos",
                 "Sudetenland": "Soo-day-ten-land", "Hindenburg": "Hin-den-boorg", "U.S.S.R.": "U S S R",
                 "Littell": "Lih-tell", "Amarcord": "Ah-mar-cord", "Shalamov": "Sha-la-mov", "Kolyma": "Ko-ly-ma",
                 "Benigni": "Ben-een-yee", "Gansel": "Gahn-zel", "Costelle": "Coss-tell", "Cohen-Scali": "Co-en Scah-lee",
                 "Riefenstahl": "Reef-en-shtahl", "DBQ": "D B Q"}

# vote nazi (cours, I.2, graphiques de M. Ros) : mai 1928, septembre 1930, juillet 1932, novembre 1932
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Nineteen twenty-nine. In New York, a silent crowd waits outside the Stock Exchange. The crash has begun. "
        "That same year, in Nuremberg, Adolf Hitler greets his supporters at a congress of the Nazi Party. Two photographs. One year.",
        "{-q1}{q2}Between nineteen seventeen and nineteen thirty-nine, three regimes tried something no tyranny had tried before. "
        "They wanted to control not only the state, but the whole of society. And they wanted to remake human beings.",
        "{-q2}{q3}So what exactly is totalitarianism? And did it drag the world into the Second World War? "
        "Those are the two questions of this chapter.",
        "{-q3}{-g0}{plan}This series covers the whole chapter, in nine episodes. {plan.1}Today: what is totalitarianism? "
        "{plan.2}Then, from the Great War to power. {plan.3}Three regimes, three ideologies. {plan.4}The leader, the party and the New Man. "
        "{plan.5}Mass terror. {plan.6}Hegemonic ambitions. {plan.7}Appeasement, and the road to war. "
        "{plan.8}After that comes an episode just for the exam, with the essay and the DBQ. {plan.9}And a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[13]),
        "q1": dict(type="question", t="1929: two photographs, one year.", bande=True),
        "q2": dict(type="question", t="Control the whole of society… and remake human beings?", bande=True),
        "q3": dict(type="question", t="What is totalitarianism? Did it lead to war?", bande=True),
        "plan": dict(type="liste", titre="H2 · Totalitarian Regimes, in nine episodes", petit=True, items=[
            "What is totalitarianism? (Introduction)", "From the Great War to power (I.1 – I.2)",
            "Three regimes, three ideologies (I.3)", "The leader, the party and the New Man (II.1 – II.2)",
            "Mass terror (II.3)", "Hegemonic ambitions (III.1)", "Appeasement and the road to war (III.2 – III.3)",
            "Totalitarianism at the exam: essay and DBQ", "Recap"], x=190, y=80, w=900),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 1", t="What is totalitarianism?",
                      sous="1917 – 1939 · a debate · a definition · three regimes"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="naissance", chap="1914 – 1933 on the map", fond="nuit", humeur="tension",
         retenir="1914–1918: the trenches, matrix of the regimes · 1917: the Bolsheviks seize power · 1922: the USSR and the March on Rome · 1929: two crises · 30 Jan. 1933: Hitler chancellor.",
         beats=[
        "{g1}Before any definition, let's run through the whole story on the map. Every episode will come back to these dates. "
        "{g1.1}It all begins in the trenches of the First World War. Four years of mass killing made violence ordinary. "
        "For the historian George Mosse, the Great War is the matrix of totalitarianism. We'll see it in episode two.",
        "{g1.2}Nineteen seventeen, in Russia. In February, the war brings down the Tsar. In October, Lenin and Trotsky's Bolsheviks seize power. "
        "Then they win a civil war. The Soviet Union is created in nineteen twenty-two. And from nineteen twenty-four, it is Stalin's Soviet Union.",
        "{g1.3}Nineteen twenty-two, in Italy. The country won the war, but it feels cheated. And it is afraid of a communist revolution. "
        "In October, Mussolini's Blackshirts march on Rome. The king appoints him prime minister. Fascist Italy will last until nineteen forty-three.",
        "{g1.4}Nineteen twenty-nine. The crash in New York, and the world crisis of chapter one. In Germany, the Nazi Party is still a small party. "
        "But the crisis is about to change everything.",
        "{g1.5}The thirtieth of January, nineteen thirty-three. President Hindenburg appoints Hitler chancellor. Legally. "
        "Nazi Germany is born. It will last until nineteen forty-five.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 6, 13, 20]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="versguerre", chap="1933 – 1939 on the map", fond="nuit", humeur="tension",
         retenir="7 March 1936: the Rhineland · Oct. 1936: the Rome–Berlin Axis · 12 March 1938: the Anschluss · Sept. 1938: Munich · 23 Aug. 1939: the Nazi-Soviet pact · 1–3 Sept. 1939: war.",
         beats=[
        "{g2}And from there, the road leads to war. {g2.1}The seventh of March, nineteen thirty-six. German troops march into the demilitarised Rhineland. "
        "France and Britain do nothing. Hitler's gamble pays off.",
        "{g2.2}October nineteen thirty-six: the Rome-Berlin Axis. The two fascist dictators mistrust each other, yet they become allies. "
        "And both of them back Franco in the Spanish Civil War.",
        "{g2.3}March nineteen thirty-eight: the Anschluss. The German army enters Vienna, and Austria is annexed. "
        "{g2.4}September nineteen thirty-eight. At Munich, France and Britain hand the Sudetenland over to Hitler. The Czechs are not even invited. "
        "This is appeasement. It is the second key term of the chapter.",
        "{g2.5}August nineteen thirty-nine. Now comes the shock. Nazi Germany and Stalin's Soviet Union are sworn ideological enemies. And they sign a pact. "
        "{g2.6}On the first of September, Germany attacks Poland. Two days later, France and Britain declare war.",
        "{-g2}{frise}Let's fix the dates in your mind. {frise.1}Nineteen seventeen: the Bolsheviks take power. "
        "{frise.2}Nineteen twenty-two: the March on Rome. {frise.3}Nineteen twenty-nine: two crises at once. "
        "{frise.4}Nineteen thirty-three: Hitler becomes chancellor. {frise.5}Nineteen thirty-six: the Rhineland, and the Axis. "
        "{frise.6}Nineteen thirty-eight: the Anschluss, and Munich. {frise.7}Nineteen thirty-nine: the pact. And war.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[28, 29, 33, 34, 36, 37]),
        "frise": dict(type="frise", items=[
            dict(nom="Russia", d=1917, q="the Bolsheviks seize power"), dict(nom="Italy", d=1922, q="the March on Rome"),
            dict(nom="Two crises", d=1929, q="capitalism · totalitarianism"), dict(nom="Germany", d=1933, q="Hitler chancellor"),
            dict(nom="Rhineland", d=1936, q="and the Rome–Berlin Axis"), dict(nom="Munich", d=1938, q="the Anschluss, the Sudetenland"),
            dict(nom="War", d=1939, q="the pact, then Poland")]),
    }),

    # ================================================================ III. deux crises (idée 1)
    dict(id="deuxcrises", chap="1929: two crises at once", fond="nuit", humeur="mystere",
         retenir="1929 opens two crises: the crisis of capitalism (chapter 1) and the threat of totalitarianism (chapter 2). Which one led to war: one, the other, or both?",
         beats=[
        "{photos}Now for the course. The chapter opens with those two photographs from nineteen twenty-nine. "
        "{photos.1}On one, a solemn crowd stands outside the New York Stock Exchange, after the crash. On the other, Adolf Hitler greets his supporters "
        "at the fourth Nazi Party Congress, in Nuremberg.",
        "{-photos}{deux}{deux.g}Why put them side by side? Because nineteen twenty-nine opens two crises at once. "
        "The first is the crisis of capitalism. The crash, the Depression, democracy in retreat. That was chapter one. "
        "{deux.d}The second is the threat of totalitarianism. That is this chapter. And both roads end in the same place. The Second World War.",
        "{-deux}{etou}On the slide, between the two pictures, there are just three words. {!and or}And, or? "
        "Did one crisis cause the war? Or did the two work together? Keep that question in mind. It is the thread of the whole chapter.",
        "{-etou}{gr}Germany shows how the two roads met. {gr.1}May nineteen twenty-eight, before the crisis. The Nazi Party wins two point six per cent of the vote. "
        "It is a fringe party. {gr.2}September nineteen thirty: eighteen point three per cent. "
        "{gr.3}July nineteen thirty-two: thirty-seven point four per cent. Now it is the first party in Germany. And Germany has five point six million unemployed. "
        "{gr.4}In November, the Nazis fall back to thirty-three point one. So, never a majority. Remember that. It will matter when we get to Arendt.",
        "{-gr}{crise}So the world crisis of the nineteen thirties is two things at once. {crise.1}It is a crisis of democracy, in retreat. "
        "{crise.2}And it is the steady advance of totalitarianism.",
    ], vis={
        "photos": dict(type="note", terme="Two photographs, 1929", cles=["crash", "Nuremberg"],
                       t="A solemn crowd outside the New York Stock Exchange after the crash; Hitler at the Nazi Party Congress in Nuremberg.",
                       etape="Same year: the crisis of capitalism and the totalitarian threat (described here, not shown).", x=170, y=200, w=940),
        "deux": dict(type="cols", g="The crisis of capitalism", gq="the crash, the Depression, democracy in retreat · chapter 1",
                     d="The threat of totalitarianism", dq="Fascism, Nazism, Stalinism · chapter 2", vs="&",
                     repere="Both roads start in 1929 and end in the Second World War"),
        "etou": dict(type="mot", t="and / or ?", g="did one crisis cause the war, or did the two work together?", y=250, taille=120),
        "gr": dict(type="graphe", titre="The Nazi vote in Reichstag elections (%, course)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.8, 1933.2], y=[0, 45], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40], lx="year", ly="% of votes"),
                   el=[dict(type="point", x=1928.4, y=2.6, c="sa", lbl="May 1928: 2.6%", lp=[1928.5, 9]),
                       dict(type="courbe", pts=VOTE[:2], c="ca", lbl="Sept. 1930: 18.3%", lp=[1929.2, 22], dur=1.6),
                       dict(type="courbe", pts=VOTE[1:3], c="ca", lbl="July 1932: 37.4%", lp=[1930.6, 41], dur=1.4),
                       dict(type="courbe", pts=VOTE[2:], c="el", lbl="Nov. 1932: 33.1%", lp=[1931.6, 27], dur=1.0)]),
        "crise": dict(type="liste", titre="The world crisis of the 1930s", items=[
            "A crisis of democracy in retreat", "The steady advance of totalitarianism"], x=170, y=200, w=940),
    }),

    # ================================================================ IV. le débat des historiens (idée 2)
    dict(id="historiens", chap="Historians disagree", fond="nuit", humeur="calme",
         retenir="Underlying causes of WWII: Taylor (1961), the democracies' failure, “very controversial” · Hehn, an economic conflict · Winter, a “Thirty Years War” 1914–1945 · this chapter: totalitarian ideology.",
         beats=[
        "{q4}The aim of the whole of Theme one is to assess the underlying causes of the Second World War. "
        "And here, historians disagree. The course slide puts three of them side by side.",
        "{-q4}{g3}{hist}{g3.1}{hist.1}The first is A. J. P. Taylor, a British historian, who lived from nineteen-oh-six to nineteen ninety. "
        "His book, The Origins of the Second World War, came out in nineteen sixty-one. He blames the democracies, for failing to stop Hitler. "
        "Think of appeasement, of Munich. Hitler went further because nobody stopped him.",
        "{g3.2}{hist.2}The second is Paul N. Hehn, from nineteen twenty-seven to two thousand and fourteen. For him, the war was an economic conflict. "
        "It was born of the crash. Markets closing, and a scramble for resources.",
        "{g3.3}{hist.3}The third is Jay Winter, born in nineteen forty-five. He sees nineteen fourteen to nineteen forty-five as one single "
        "{!Thirty Years War}Thirty Years War. The second conflict simply continues the first.",
        "{-hist}{-g3}{taylor}Now, notice the warning on the reading list. Taylor's book is there, with three words beside it. {!very controversial thesis}Very controversial thesis. "
        "{taylor.1}Why? Because if the democracies are to blame, Hitler's own will to war almost vanishes. "
        "Quote Taylor, but discuss him.",
        "{-taylor}{quatre}And this chapter adds a fourth candidate to the list. {!totalitarian ideology}Totalitarian ideology. "
        "Did the ideologies of these regimes make war inevitable? That is the question of Part three. And it is the key issue of the chapter.",
    ], vis={
        "q4": dict(type="question", t="What were the underlying causes of the Second World War?"),
        "g3": dict(type="globe", code="H2", sc=[31, 13, 1]),
        "hist": dict(type="liste", titre="Three historians, three answers", x=60, y=110, w=620, petit=True, bande=True,
                     cles=["democracies", "economic", "Thirty"], items=[
            "A. J. P. Taylor (1906–1990): the failure of the democracies to stop Hitler",
            "Paul N. Hehn (1927–2014): an economic conflict, born of the crash",
            "Jay Winter (b. 1945): 1914–1945, one “Thirty Years War”"]),
        "taylor": dict(type="note", terme="On the reading list of the course", cles=["controversial"],
                       t="A. J. P. Taylor, The Origins of the Second World War (1961): “very controversial thesis”.",
                       etape="Blame the democracies… and Hitler's own will to war almost disappears.", x=170, y=200, w=940),
        "quatre": dict(type="mot", t="+ totalitarian ideology?", g="the fourth candidate, tested in this chapter", y=250, taille=88),
    }),

    # ================================================================ V. la définition (idée 3)
    dict(id="definition", chap="A definition in three parts", fond="aube", humeur="lumiere",
         retenir="Key term. Totalitarianism: a regime that seeks total control of society, through coercion, to transform man according to an ideology.",
         beats=[
        "{def1}Here is the first key term of the chapter. You must know it word for word. {!Totalitarianism}Totalitarianism: "
        "a regime that seeks total control of society, through coercion, in order to transform man according to an ideology.",
        "{-def1}{trois}The definition has three parts. {trois.1}Part one. The control is {!total}total. It does not stop at politics. "
        "It reaches work, leisure, the family, the school, religion. Even thought.",
        "{trois.2}Part two. It relies on {!coercion}coercion. And coercion means two things together. Terror, and propaganda. "
        "Fear, and persuasion.",
        "{trois.3}Part three, the most important one. The aim is not obedience. It is {!transformation}transformation. "
        "The regime wants to create a New Man, shaped by its ideology.",
        "{-trois}{photo3}{dict}{dict.g}That third part is what sets a totalitarian regime apart from an ordinary dictatorship. "
        "An ordinary dictatorship is happy if people keep quiet. {dict.d}A totalitarian regime wants them to believe. "
        "To cheer. To change. Silence is not enough. It wants your soul.{-photo3}",
    ], vis={
        "def1": dict(type="def", cles=["total", "coercion", "transform", "ideology"], terme="Key term · Totalitarianism",
                     t="A regime that seeks total control of society, through coercion, in order to transform man according to an ideology.",
                     etape="Learn it word for word: it opens almost every essay on this chapter.", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="The definition, part by part", cles=["Total", "Coercion", "Transformation"], items=[
            "Total control: work, leisure, family, school, religion, thought",
            "Coercion: terror and propaganda together",
            "Transformation: not obedience, but a “New Man” shaped by the ideology"], x=170, y=140, w=940),
        "photo3": dict(type="tableau", img="h2-nuremberg-1936", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="The 'cathedral of light' over the Zeppelin Field, Nuremberg rally, September 1936 · Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE"),
        "dict": dict(type="cols", g="An ordinary dictatorship", gq="content if people keep quiet",
                     d="A totalitarian regime", dq="wants people to believe, cheer and change: a “New Man”", vs="≠"),
    }),

    # ================================================================ VI. la roue des sept traits (h2wheel)
    dict(id="roue", chap="The seven key traits", fond="nuit", humeur="calme",
         retenir="Seven traits: ideology · dynamic leader · dictatorship and one-party rule · state control of individuals · state control of society · methods of enforcement · modern technology.",
         beats=[
        "{src}The course slide shows a wheel. It gives the key traits of totalitarianism. It comes from an American textbook, "
        "World History, published by McDougal Littell in two thousand and nine. There are seven traits. "
        "{-src}{roue}{roue.1}One: an ideology. It sets the goals of the state, glorifies them, and justifies everything the government does. "
        "{roue.2}Two: a dynamic leader. He unites the people, symbolises the government, and stirs up popular support.",
        "{roue.3}Three: dictatorship and one-party rule. The authority is absolute, and the party dominates the government. "
        "{roue.4}Four: state control of individuals. The regime demands loyalty. It denies basic liberties. And it expects personal sacrifice for the state.",
        "{roue.5}Five: state control of society. Business, labour and housing. Education, religion and the arts. Even private life, and youth groups. "
        "{roue.6}Six: methods of enforcement. Police terror, indoctrination, censorship, persecution.",
        "{roue.7}And seven: modern technology. Mass communication, to spread propaganda. And advanced military weapons.",
        "{-roue}{memo}Seven is a lot to remember. So here is a memory aid. {memo.1}The ideology sets the goal. "
        "{memo.2}The leader and the party embody it. {memo.3}Control and enforcement impose it. {memo.4}And modern technology spreads it.",
        "{-memo}{techno}Look closely at that last trait. It is what separates totalitarianism from the tyrannies of the past. "
        "{techno.1}An ancient tyrant could frighten a city. But a twentieth-century regime has the radio, film, and modern weapons. "
        "It can reach every home, every single day.",
    ], vis={
        "roue": dict(type="liste", titre="The seven key traits of totalitarianism (after McDougal Littell, 2009)", petit=True,
                     cles=["Ideology", "leader", "one-party", "individuals", "society", "enforcement", "technology"], items=[
            "Ideology: sets, glorifies and justifies the goals of the state",
            "A dynamic leader: unites the people, symbolises the government",
            "Dictatorship and one-party rule: absolute authority",
            "State control of individuals: loyalty, no basic liberties, sacrifice",
            "State control of society: economy, school, religion, arts, youth",
            "Methods of enforcement: police terror, indoctrination, censorship, persecution",
            "Modern technology: mass communication, advanced weapons"], x=150, y=90, w=980),
        "src": dict(type="note", terme="The course slide · Key Traits of Totalitarianism", cles=["wheel", "Seven"],
                    t="A wheel of seven traits, from World History (McDougal Littell, 2009), an American textbook.",
                    etape="The course spells it “MacDougal Littell”: the publisher is McDougal Littell.", x=170, y=200, w=940),
        "memo": dict(type="liste", titre="A memory aid", cles=["sets", "embody", "impose", "spreads"], items=[
            "The ideology sets the goal", "The leader and the party embody it",
            "Control and enforcement impose it", "Modern technology spreads it"], x=170, y=150, w=940),
        "techno": dict(type="note", terme="The decisive trait", cles=["radio", "film", "weapons"],
                       t="Modern technology separates totalitarianism from older tyrannies: radio, film and modern weapons.",
                       etape="The regime reaches every home, every day.", x=170, y=200, w=940),
    }),

    # ================================================================ VII. l'idéologie (idée 4)
    dict(id="ideologie", chap="Ideology: a supreme goal", fond="nuit", humeur="tension",
         retenir="Ideology: a set of beliefs that sets a supreme goal. USSR: a classless society · Fascist Italy: the nation and the State · Nazi Germany: the purity and domination of the race. A supreme goal justifies any means.",
         beats=[
        "{def2}The first trait of the wheel is the key to the whole chapter. What is an {!ideology}ideology? It is a set of beliefs that sets a supreme goal to be achieved.",
        "{-def2}{g4}{buts}And each regime has its own supreme goal. {buts.1}For the Soviet Union, it is a classless society. "
        "{buts.2}For Fascist Italy, the greatness of the nation and of the State. "
        "{buts.3}For Nazi Germany, the purity and the domination of the race. Class, nation, race. Remember these three words. "
        "They come back in every episode.",
        "{-buts}{-g4}{moyens}Why does it matter so much? Because when a goal is {!supreme}supreme, it justifies any means. "
        "{moyens.1}Even the suffering of millions of people.",
        "{-moyens}{photo1}{g5}The course gives a chilling example. It is a speech by Stalin, on the seventh of January, nineteen thirty-three. It is in Worksheet two. "
        "Stalin presents his Five-Year Plan as the road to{-g5}",
        ("C", "the abolition of classes in the U.S.S.R.", "c_staline"),
        "{-c_staline}{-photo1}{g5b}{g5b.1}And in those very months, Ukraine is starving. This is the famine of nineteen thirty-two and thirty-three, the Holodomor. "
        "It kills the peasants whose grain the regime is taking. On one side, the supreme goal. On the other, millions of victims. "
        "We come back to it in episode three.",
        "{-g5b}{dedans}So ideology explains two things. {dedans.1}What these regimes did inside their borders. That is Parts one and two. "
        "{dedans.2}And why they went looking for war outside them. That is Part three.",
    ], vis={
        "def2": dict(type="def", cles=["beliefs", "supreme"], terme="Ideology",
                     t="A set of beliefs that sets a supreme goal to be achieved.",
                     etape="The first trait of the wheel, and the key to the chapter", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H2", sc=[0]),
        "buts": dict(type="liste", titre="Three supreme goals", x=60, y=120, w=620, petit=True, bande=True,
                     cles=["classless", "nation", "race"], items=[
            "USSR: a classless society", "Fascist Italy: the greatness of the nation and the State",
            "Nazi Germany: the purity and domination of the race"]),
        "moyens": dict(type="note", terme="Why ideology matters", cles=["supreme", "any"],
                       t="A goal presented as supreme justifies any means, including the suffering of millions.",
                       x=170, y=200, w=940),
        "photo1": dict(type="tableau", img="h2-fyp-poster", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.1, .5, .45],
                       legende="'The arithmetic of a counter-plan: 2 + 2 plus the enthusiasm of the workers = 5', Five-Year Plan poster, 1931 · Yakov Guminer, public domain"),
        "g5": dict(type="note", terme="Worksheet 2 · source 1", cles=["Five-Year"],
                   t="Stalin's speech of 7 January 1933 on the results of the first Five-Year Plan.", x=170, y=480, w=940),
        "c_staline": dict(type="cit", a="Joseph Stalin", o="speech of 7 January 1933 (Worksheet 2)", x=200, y=190, w=880),
        "g5b": dict(type="globe", code="H2", sc=[19]),
        "dedans": dict(type="cols", g="Inside their borders", gq="control, New Man, terror · Parts I and II",
                       d="Outside their borders", dq="expansion and the road to war · Part III", vs="→"),
    }),

    # ================================================================ VIII. Arendt (idée 5)
    dict(id="arendt", chap="Arendt: the confidence of the masses", fond="guerre", humeur="mystere",
         retenir="Arendt, The Origins of Totalitarianism (1951): Hitler's rise “was legal in terms of majority rule”; both dictators needed “the confidence of the masses”. Explain support as well as terror.",
         beats=[
        "{photo2}{ar}Now, a warning against a black-and-white picture. It comes from Hannah Arendt, who lived from nineteen-oh-six to nineteen seventy-five. "
        "She was a German American political theorist. In The Origins of Totalitarianism, published in nineteen fifty-one, she writes that{-ar}",
        ("C", "Hitler's rise to power was legal in terms of majority rule", "c_ar1"),
        "{-c_ar1}{ar2}She adds that neither Hitler nor Stalin could have kept power, through so many crises, without{-ar2}",
        ("C", "the confidence of the masses", "c_ar2"),
        "{-c_ar2}{sens}What does she mean? {sens.1}That large masses trusted these regimes. {sens.2}That not everyone felt oppressed. "
        "{sens.3}So, to understand totalitarianism, you have to explain support. Not only terror.",
        "{-sens}{-photo2}{g6}{g6.1}Germany is the best example. Remember the curve. Thirty-seven point four per cent, in July nineteen thirty-two. "
        "Millions of Germans voted for Hitler, freely. {g6.2}Then, on the thirtieth of January, nineteen thirty-three, President Hindenburg appointed him chancellor. "
        "It happened through the institutions.",
        "{-g6}{nuance}But be precise in an essay. {nuance.1}Was it legal? Yes. Hitler was appointed. He did not seize power in a coup. "
        "{nuance.2}But did the Nazis ever win a majority in a free election? No. Their best score was thirty-seven point four per cent. "
        "So write this. A legal appointment, with mass support, but without a majority.",
        "{-nuance}{deuxfaces}{deuxfaces.g}Keep both faces of these regimes together. Terror, for the enemies. "
        "{deuxfaces.d}And consent, enthusiasm and confidence, for millions of others.",
        "{-deuxfaces}{faits}Arendt adds one last idea. It is the epigraph on the cover sheet of the chapter. {faits.1}Totalitarian propaganda "
        "treats facts as something power can manufacture. It despises facts. Whatever the leader says becomes true.",
    ], vis={
        "photo2": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, author of The Origins of Totalitarianism (1951), in 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
        "ar": dict(type="note", terme="Hannah Arendt (1906–1975)", cles=["Origins"],
                   t="German American political theorist, author of The Origins of Totalitarianism (1951).", x=170, y=200, w=940),
        "c_ar1": dict(type="cit", a="Hannah Arendt", o="The Origins of Totalitarianism, 1951", x=200, y=190, w=880),
        "ar2": dict(type="note", terme="Neither Hitler nor Stalin…", t="…could have kept power through so many crises without…",
                    x=170, y=200, w=940),
        "c_ar2": dict(type="cit", a="Hannah Arendt", o="The Origins of Totalitarianism, 1951", x=200, y=220, w=880),
        "sens": dict(type="liste", titre="Arendt's warning", cles=["trusted", "oppressed", "support"], items=[
            "Large masses trusted these regimes", "Not everyone felt oppressed",
            "Explain support as well as terror"], x=170, y=150, w=940),
        "g6": dict(type="globe", code="H2", sc=[16, 20]),
        "nuance": dict(type="liste", titre="Be precise", cles=["Legal", "majority"], items=[
            "Legal: appointed by Hindenburg, 30 January 1933, not a coup",
            "But never a majority: 37.4% at best (July 1932)"], x=170, y=150, w=940),
        "deuxfaces": dict(type="cols", g="Terror", gq="for the enemies of the regime", d="Confidence",
                          dq="consent and enthusiasm of millions", vs="+", repere="Arendt: explain support as well as terror"),
        "faits": dict(type="def", cles=["facts", "manufacture"], terme="Propaganda, according to Arendt",
                      t="The organised spreading of ideas and images to win or control opinion, marked by contempt for facts.",
                      etape="The chapter's epigraph: facts become something power can manufacture.", x=170, y=200, w=940),
    }),

    # ================================================================ IX. trois régimes, une trajectoire (idée 6)
    dict(id="trajectoire", chap="Three regimes, one trajectory", fond="nuit", humeur="tension",
         retenir="Stalin's USSR (1924–1953), Fascist Italy (1922–1943), Nazi Germany (1933–1945): born from the overthrow of a democratic framework, they paved the way to war, all ended in failure.",
         beats=[
        "{fr2}{fr2.1}So the chapter studies three regimes side by side. The course slide dates each one, under its flag. "
        "First, Fascist Italy, under the fascist eagle, from nineteen twenty-two to nineteen forty-three. "
        "{fr2.2}Next, Stalin's Soviet Union, under the hammer and sickle, from nineteen twenty-four. "
        "{fr2.3}Then Nazi Germany, under the swastika, from nineteen thirty-three. "
        "{fr2.4}Fascist Italy falls in nineteen forty-three. {fr2.5}Nazi Germany, in nineteen forty-five. "
        "{fr2.6}And Stalin's Soviet Union lasts until his death, in nineteen fifty-three.",
        "{-fr2}{meme}They share the same totalitarian ambition. But their ideologies are opposites. {meme.1}The nation, for Fascism. "
        "{meme.2}The race, for Nazism. {meme.3}The class, for Stalinism. That is why Stalin and Hitler are sworn enemies. At least until their pact, in nineteen thirty-nine.",
        "{-meme}{g7}{traj}And yet they follow one common path, in three steps. {traj.1}Step one. Each was born from the overthrow of a democratic framework. "
        "In Germany, the Weimar Republic. In Italy, the parliamentary monarchy. In Russia, the fragile freedoms born in February nineteen seventeen, "
        "which the Bolsheviks swept away. {traj.2}Step two. All three paved the way to the Second World War. "
        "{traj.3}Step three. All three ended in failure.",
        "{-traj}{-g7}{nu}One nuance on that last step. {nu.1}For Italy and Germany, failure means total defeat in war. "
        "{nu.2}The Soviet Union, on the contrary, was among the victors of nineteen forty-five. Stalinism ended with Stalin's death, in nineteen fifty-three. "
        "And the Soviet Union itself collapsed in nineteen ninety-one. That last date is outside the course. But it helps you discuss the word failure.",
        "{-nu}{g8}One last map from the course. Europe and its regimes, around nineteen thirty-eight. {g8.1}In the west, the democracies. "
        "Britain, France, and a few smaller countries. In the centre, the two fascist regimes, Germany and Italy. In the east, the communist Soviet Union. "
        "And almost everywhere else, other authoritarian regimes, such as Poland, Austria, or Spain. {g8.2}By the end of the nineteen thirties, "
        "the democracies are an island, in the west of the continent.",
    ], vis={
        "fr2": dict(type="frise", items=[
            dict(nom="Fascist Italy", d=1922, q="the March on Rome"), dict(nom="Stalin's USSR", d=1924, q="Stalin in power"),
            dict(nom="Nazi Germany", d=1933, q="Hitler chancellor"), dict(nom="Italy falls", d=1943, q="end of Fascist Italy"),
            dict(nom="Germany falls", d=1945, q="end of Nazi Germany"), dict(nom="Stalin dies", d=1953, q="end of Stalin's USSR")]),
        "meme": dict(type="liste", titre="One ambition, three ideologies", cles=["nation", "race", "class"], items=[
            "Fascism → the nation", "Nazism → the race", "Stalinism → the class"], x=170, y=150, w=940),
        "g7": dict(type="globe", code="H2", sc=[0]),
        "traj": dict(type="liste", titre="One trajectory, three steps", x=60, y=120, w=620, petit=True, bande=True,
                     cles=["overthrow", "war", "failure"], items=[
            "Born from the overthrow of a democratic framework", "All paved the way to the Second World War",
            "All ended in failure"]),
        "nu": dict(type="cols", g="Italy, Germany", gq="failure = total defeat in war (1943, 1945)",
                   d="The USSR", dq="a victor in 1945; Stalin dies in 1953; the USSR collapses in 1991 (outside the course)", vs="≠"),
        "g8": dict(type="globe", code="H2", sc=[31]),
    }),

    # ================================================================ X. lire et voir (h2reads)
    dict(id="lectures", chap="Read and watch", fond="aube", humeur="calme",
         retenir="Quote a work from the reading list of the course, with one sentence on what it shows: e.g. Arendt (1951), Shalamov's Kolyma Tales, Life is Beautiful, The Wave.",
         beats=[
        "{lire}{lire.1}The course also gives a reading list. The one-line descriptions come from the site, not from the course. "
        "First, Eric Hobsbawm, The Age of Extremes, from nineteen ninety-four. It tells the short twentieth century, nineteen fourteen to nineteen ninety-one, as an age of catastrophes. "
        "{lire.2}George Mosse, Fallen Soldiers. Brutalisation, and the memory of the world wars. "
        "{lire.3}Hannah Arendt, The Origins of Totalitarianism. The theory, and the chapter's epigraph. "
        "{lire.4}A. J. P. Taylor, The Origins of the Second World War. The very controversial thesis.",
        "{lire.5}Will Eisner's comic, The Plot. It tells the story of a forgery, the Protocols of the Elders of Zion. Propaganda, and antisemitism. "
        "{lire.6}Varlam Shalamov's Kolyma Tales. The Gulag, from inside. "
        "{lire.7}And Sarah Cohen-Scali's Max. A boy born in Nazi Germany, for young readers.",
        "{-lire}{voir}And four films. {voir.1}Roberto Benigni's Life is Beautiful. Italian Jews, under the racial laws, and deportation. "
        "{voir.2}Dennis Gansel's The Wave. How easily a group slides into authoritarian discipline. "
        "{voir.3}Daniel Costelle's documentary, Apocalypse: Hitler. His rise to power. "
        "{voir.4}And Federico Fellini's Amarcord. Provincial life in Fascist Italy, seen through memory.",
        "{-voir}{astuce}A tip for the exam. Quote one of these works, with one sentence on what it shows. "
        "It proves that you have read beyond the course.",
    ], vis={
        "lire": dict(type="liste", titre="Read · the course list", petit=True, items=[
            "Hobsbawm, The Age of Extremes (1994): an age of catastrophes", "Mosse, Fallen Soldiers: brutalisation",
            "Arendt, The Origins of Totalitarianism (1951): the theory", "Taylor, The Origins of the Second World War (1961): “very controversial”",
            "Eisner, The Plot (2005): the forged Protocols, antisemitism", "Shalamov, Kolyma Tales (1954): the Gulag from inside",
            "Cohen-Scali, Max (2012): a boy born in Nazi Germany"], x=150, y=90, w=980),
        "voir": dict(type="liste", titre="Watch · the course list", items=[
            "Benigni, Life is Beautiful (1997): Italian Jews, racial laws", "Gansel, The Wave (2008): sliding into authoritarian discipline",
            "Costelle, Apocalypse: Hitler (2011): the rise to power", "Fellini, Amarcord (1973): provincial Fascist Italy"],
                     x=150, y=140, w=980),
        "astuce": dict(type="note", terme="Exam tip", cles=["sentence", "beyond"],
                       t="Quote one work, with one sentence on what it shows: it proves reading beyond the course.", x=170, y=200, w=940),
    }),

    # ================================================================ XI. à toi : définir (pause)
    dict(id="atoi", chap="Your turn: define totalitarianism", fond="aube", humeur="calme",
         retenir="A definition paragraph: the key term word for word · its three parts · the difference from a dictatorship · one precise example · Arendt's nuance.",
         beats=[
        "{pa1}Your turn. Write one paragraph that defines totalitarianism, with a precise example. "
        "Use the three parts of the definition. And show how it differs from an ordinary dictatorship.",
        ("P", 2.0),
        "{-pa1}{rep1}Here is one way to write it. {rep1.1}Totalitarianism is a regime that seeks total control of society, "
        "through coercion, in order to transform man according to an ideology. "
        "{rep1.2}Its control is total, since it reaches work, leisure, school, religion, and even thought. "
        "And its coercion combines terror with propaganda. "
        "{rep1.3}An ordinary dictatorship is content with obedience. A totalitarian regime wants to create a New Man. "
        "{rep1.4}For example, in January nineteen thirty-three, Stalin presented the Five-Year Plan as the road to the abolition of classes. "
        "Meanwhile, famine was killing the peasants of Ukraine. A supreme goal justified any means. "
        "{rep1.5}Yet, as Hannah Arendt warned, these regimes did not rest on terror alone. They also rested on the confidence of the masses.",
        "{-rep1}{ki}Where will this definition serve you? In the key issue of the chapter. {!Assess the role of totalitarianism}"
        "Assess the role of totalitarianism in the collapse of global peace in the late nineteen thirties. "
        "{ki.1}And in the two key terms: totalitarianism, and appeasement. "
        "The definition you have just written is the first step of your introduction.",
    ], vis={
        "pa1": dict(type="pause", t="Define totalitarianism in one paragraph, with a precise example.",
                    sous="Three parts, the difference from a dictatorship, one example. Pause the video, write, then play on for a model."),
        "rep1": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "Definition: total control of society, through coercion, to transform man according to an ideology",
            "Total (work, leisure, school, religion, thought); coercion = terror + propaganda",
            "Not mere obedience, as in a dictatorship: a “New Man”",
            "Example: Stalin, 7 Jan. 1933, “the abolition of classes”, during the famine in Ukraine",
            "Nuance: Arendt, “the confidence of the masses”"], x=150, y=110, w=980),
        "ki": dict(type="def", cles=["role", "collapse"], terme="Key issue of the chapter",
                   t="Assess the role of totalitarianism in the collapse of global peace in the late 1930s.",
                   etape="Key terms: Totalitarianism · Appeasement", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Nineteen twenty-nine opens two crises at once. Capitalism, and totalitarianism. "
        "Historians disagree on the causes of the war. Taylor, Hehn, Winter. "
        "{carte.2}Then, the definition. Total control of society, through coercion, to transform man according to an ideology. And its seven traits. "
        "{carte.3}Ideology sets a supreme goal. Class, nation, race. And Arendt reminds us: the confidence of the masses, not terror alone. "
        "{carte.4}Three regimes, one trajectory. Born from the overthrow of democracy, they paved the way to war. And they ended in failure.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: from the Great War to power. The trenches. The revolutions of nineteen seventeen to nineteen twenty. "
        "The March on Rome. And how Hitler was handed power.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="TOTALITARIANISM", branches=[
            dict(t="1929 · a debate", items=["two crises: and / or?", "Taylor · Hehn · Winter", "+ totalitarian ideology?"]),
            dict(t="Definition", items=["total control · coercion", "transform man: a New Man", "seven traits"]),
            dict(t="Ideology · support", items=["class · nation · race", "a supreme goal, any means", "Arendt: confidence of the masses"]),
            dict(t="One trajectory", items=["USSR 1924–53 · Italy 1922–43", "Germany 1933–45", "democracy overthrown → war → failure"])]),
        "fin": dict(type="mot", t="Next: from the Great War to power", g="Episode 2 · 1914 – 1933", y=270, taille=70),
    }),
]

QUIZ = [
    dict(q="Why does the chapter open with two photographs from 1929?",
         r=["1929 opened two crises at once: capitalism and totalitarianism", "1929 is the year Hitler came to power",
            "1929 is the year the war began", "1929 is the year of the March on Rome"], ok=0, voir="deux",
         ex="The crash in New York and the Nazi Party Congress in Nuremberg: did one crisis lead to war, the other, or both?"),
    dict(q="Which historian blamed the Second World War on the failure of the democracies to stop Hitler?",
         r=["A. J. P. Taylor", "Paul N. Hehn", "Jay Winter", "Hannah Arendt"], ok=0, voir="hist",
         ex="The Origins of the Second World War (1961): a “very controversial thesis”, says the course."),
    dict(q="For Jay Winter, what was the period 1914–1945?",
         r=["A single “Thirty Years War”", "An economic conflict", "An age of prosperity", "The failure of appeasement only"], ok=0, voir="hist",
         ex="The second conflict is the direct continuation of the first. Hehn sees an economic conflict."),
    dict(q="Which is the course definition of totalitarianism?",
         r=["A regime that seeks total control of society, through coercion, to transform man according to an ideology",
            "Any regime led by a single man", "A regime that only controls political life", "A regime based on free elections"], ok=0, voir="def1",
         ex="Three parts: total control, coercion (terror and propaganda), transformation (a New Man)."),
    dict(q="What separates a totalitarian regime from an ordinary dictatorship?",
         r=["It wants to transform people, not only to keep them quiet", "It has no police", "It has no leader",
            "It never uses propaganda"], ok=0, voir="dict",
         ex="An ordinary dictatorship is content with obedience; a totalitarian regime wants a “New Man”."),
    dict(q="Which trait of the wheel separates totalitarianism from older tyrannies?",
         r=["Modern technology: mass communication and modern weapons", "A leader", "An army", "Taxes"], ok=0, voir="techno",
         ex="Radio, film and modern weapons let the regime reach every home, every day."),
    dict(q="Which supreme goal belongs to which regime?",
         r=["USSR: a classless society · Italy: the nation and the State · Germany: the race",
            "USSR: the race · Italy: a classless society · Germany: the nation",
            "All three: the race", "All three: a classless society"], ok=0, voir="buts",
         ex="Class, nation, race: because the goal is supreme, it justifies any means."),
    dict(q="What did Hannah Arendt argue in The Origins of Totalitarianism (1951)?",
         r=["Hitler and Stalin needed “the confidence of the masses”, not terror alone", "These regimes rested on terror alone",
            "Hitler seized power by a coup", "Stalin was elected by a majority"], ok=0, voir="c_ar2",
         ex="Understanding totalitarianism means explaining support as well as terror. But careful: the Nazis never won a majority (37.4% at best)."),
]

CREDITS = [
    "Content: the DNL History course (chapter H2 · Introduction “Defining totalitarianism: a debate and a definition”, the seven key traits wheel, Europe of regimes c. 1938, the reading list; Nazi vote figures from Part I.2) as written on the site; animated map of chapter 2 (site).",
    "Course correction: the key traits wheel comes from the publisher McDougal Littell (World History, 2009), spelled “MacDougal Littell” in the course.",
    "Outside the course: the collapse of the USSR in 1991; the one-line descriptions of the reading list.",
    "Photographs and posters (via Wikimedia Commons): Five-Year Plan poster “2 + 2 = 5”, 1931 (Yakov Guminer, public domain); Hannah Arendt in 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0); the Nuremberg rally of September 1936 (Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
