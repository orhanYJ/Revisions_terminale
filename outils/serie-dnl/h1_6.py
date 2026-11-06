"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 6 : « Recap » (tout le chapitre).

Même chaîne que la série H3 (voir h3_1.py) : outils/serie-philo/generer.py h1_6 ; sortie dans dnl/serie/.
Contenu : la synthèse du chapitre H1 dans le site (dnl/index.html, CHAPTERS.H1 : timeline, schéma `crisis` H1Chain,
idées des parties I.1 à II.3 avec un exemple chacune, keyFigures, keyTerms, keyIssues et les plans de `exam`,
Worksheet 3 pour la courbe allemande), avec la carte animée H1 (numéros de scènes, ordre chronologique) :
  H1 : 0 ordre libéral 1919 · 3 Dawes · 5 krach · 8 faillites bancaires · 9 prêts rappelés · 15 Smoot-Hawley ·
       17 effet domino 1931 · 18 Mandchourie · 21 Hitler 1933 · 22 New Deal · 29 Rhénanie · 30 Anschluss et Munich ·
       31 Prague puis Pologne · 32 cash and carry
  H2 : 0 trois régimes, une trajectoire · 20 Hitler chancelier (30 janvier 1933)
Plan de la série H1 : 1 The Great Crash of 1929 · 2 From an American crash to a world crisis · 3 Economic nationalism and
political responses · 4 Democracies and the liberal order · 5 The crisis at the exam · 6 Recap.
Correction du cours : la chaîne de II.3 place le pacte Rome-Berlin-Tokyo entre Munich et Prague ; le pacte tripartite date
de septembre 1940 (dit « outside the course » dans la vidéo).
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-6"
NOTION = "The Wall Street Crash"
NUM = 6
TITRE = "Recap"
SUIVANT = "Next chapter · H2 Totalitarian regimes"
PRONONCIATION = {"Creditanstalt": "Kred-it-an-shtalt", "Anschluss": "Ahn-shloos", "Sudetenland": "Soo-day-ten-land",
                 "Mukden": "Mook-den", "Manchukuo": "Man-choo-kwo", "Matignon": "Mah-tee-nyon", "Nipomo": "Nee-poh-moh",
                 "Daladier": "Dah-lah-dyay", "Maschmann": "Mash-man", "Keynes": "Kaynz", "Kellogg–Briand": "Kellogg-Bree-on",
                 "Léon Blum": "Lay-on Bloom", "Front populaire": "Front poppu-lair", "Kwantung": "Kwan-tung",
                 "Lytton": "Litton", "Hoovervilles": "Hoover-villes", "Weimar": "Vy-mar"}

# Worksheet 3, source 2 : chômage allemand (travailleurs assurés, %) ; vote nazi (course, II.2 idée 2)
CHOMAGE = [[1928, 8.6], [1929, 13.3], [1930, 22.7], [1931, 34.3], [1932, 43.8], [1933, 36.2]]
VOTE_NSDAP = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.3], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{q1}October, nineteen twenty-nine. A silent crowd waits outside the New York Stock Exchange. "
        "Ten years later, Europe is at war again. So how do we get from one to the other?",
        "{-q1}{q2}That question is the whole of chapter one. And this episode goes through all of it.",
        "{-q2}{-g0}{plan}Here is the plan. {plan.1}First, the story on the map. "
        "{plan.2}Then the timeline, and the chain of the crisis. {plan.3}Then the six parts, with one example each. "
        "{plan.4}The people and the figures. {plan.5}And finally, the exam.",
        "{-plan}{titre}",
        ("P", 3.0),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="question", t="From a crash in New York… to a world war?", bande=True),
        "q2": dict(type="question", t="The whole chapter, in one episode.", bande=True),
        "plan": dict(type="liste", titre="This recap", items=[
            "The story on the map, 1919 – 1939", "The timeline and the chain of the crisis",
            "The six parts: one idea, one example", "People and figures", "The exam: key terms and key issues"],
            x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 6", t="Recap",
                      sous="The Wall Street Crash and its Impact · 1919 – 1939"),
    }),

    # ================================================================ I. le film du chapitre
    dict(id="film", chap="The story on the map", fond="nuit", humeur="tension",
         retenir="1919 the liberal order · 1924 Dawes · Oct. 1929 the Crash · 1930–32 bank failures · 1930 Smoot–Hawley · 1931 dominoes and Manchuria · 1933 Hitler and the New Deal · 1936 Rhineland · 1938 Munich.",
         beats=[
        "{g1}{g1.1}It all starts with a peace. Paris, nineteen nineteen. President Wilson's Fourteen Points become a liberal world order. "
        "Democracy. The self-determination of peoples. Free trade. And a League of Nations, in Geneva. "
        "But the American Senate refuses the treaty, and the United States never joins.",
        "{g1.2}Nineteen twenty-four: the Dawes Plan. Germany borrows eight hundred million marks. American money pays German reparations, "
        "and the Allies' war debts flow back to Washington. From now on, Europe hangs on American credit.",
        "{g1.3}October, nineteen twenty-nine: the Crash. Black Thursday, on the twenty-fourth. Then Black Monday, and Black Tuesday. "
        "The market had tripled in five years, on speculation. Now it collapses.",
        "{g1.4}From nineteen thirty, the banks start to fail. About five thousand of them, by nineteen thirty-two. "
        "And that is when the Great Depression really begins. "
        "{g1.5}American banks call back their loans to Europe. Germany, the most exposed, is hit first.",
        "{g1.6}The seventeenth of June, nineteen thirty: Hoover signs the Smoot–Hawley Tariff. Within days, Canada hits back. "
        "The trade war has begun.",
        "{-g1}{g2}{g2.1}Nineteen thirty-one: the dominoes fall in Europe. The Creditanstalt, in Vienna, in May. The German banks in July. "
        "And in September, Britain leaves the Gold Standard. {g2.2}That same month, on the eighteenth, "
        "comes the Mukden incident. Japan invades Manchuria, and the League of Nations can do nothing.",
        "{g2.3}January, nineteen thirty-three: Hitler is appointed chancellor. Yet the Nazis never won a majority. "
        "{g2.4}That same year, in the United States, Roosevelt launches the New Deal. Relief, recovery, reform.",
        "{g2.5}The seventh of March, nineteen thirty-six: the German army marches into the Rhineland. France and Britain do nothing. "
        "{g2.6}Nineteen thirty-eight: the Anschluss, and then Munich. The Sudetenland is handed over to Hitler. That is appeasement.",
        ("P", 1.5),
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[0, 3, 5, 8, 9, 15]),
        "g2": dict(type="globe", code="H1", sc=[17, 18, 21, 22, 29, 30]),
    }),

    # ================================================================ II. la frise
    dict(id="dates", chap="The timeline", fond="nuit", humeur="calme",
         retenir="1919 · 1924 · 1928 · Oct. 1929 · June 1930 · 1931 · 1932 · 1933 · 1935 · 1936 · 1938 · 1939.",
         beats=[
        "{fr}Now the timeline of the course, in twelve steps. {fr.1}Nineteen nineteen: Versailles, and the League of Nations. "
        "{fr.2}Nineteen twenty-four: the Dawes Plan. {fr.3}Nineteen twenty-eight: the Kellogg–Briand Pact declares war illegal. "
        "{fr.4}October, nineteen twenty-nine: the Crash. {fr.5}June, nineteen thirty: Smoot–Hawley. "
        "{fr.6}Nineteen thirty-one: the Creditanstalt fails. Britain leaves gold. Japan takes Manchuria. "
        "{fr.7}Nineteen thirty-two: the Import Duties Act, the Stimson note… and Roosevelt is elected. "
        "{fr.8}Nineteen thirty-three: Hitler becomes chancellor. The New Deal has its hundred days. Japan quits the League. "
        "{fr.9}Nineteen thirty-five: Italy invades Ethiopia, and America passes its first Neutrality Act. "
        "{fr.10}Nineteen thirty-six: the Rhineland, and the Front populaire. "
        "{fr.11}Nineteen thirty-eight: the Anschluss, then Munich. {fr.12}And nineteen thirty-nine. Prague in March. Poland on the first of September. "
        "And cash and carry in November.",
        ("P", 7.0),
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Versailles", d=1919, q="League of Nations"), dict(nom="Dawes Plan", d=1924, q="800 million marks"),
            dict(nom="Kellogg–Briand", d=1928, q="war illegal"), dict(nom="The Crash", d=1929, q="24–29 Oct."),
            dict(nom="Smoot–Hawley", d=1930, q="17 June"), dict(nom="Dominoes", d=1931, q="gold · Manchuria"),
            dict(nom="Roosevelt elected", d=1932, q="Import Duties Act"), dict(nom="Hitler · New Deal", d=1933, q="Jan. · 100 days"),
            dict(nom="Ethiopia", d=1935, q="Neutrality Act"), dict(nom="Rhineland", d=1936, q="Front populaire"),
            dict(nom="Munich", d=1938, q="Anschluss · Sept."), dict(nom="War", d=1939, q="Poland · cash and carry")]),
    }),

    # ================================================================ III. la chaîne de la crise
    dict(id="chaine", chap="The chain of the crisis", fond="nuit", humeur="tension",
         retenir="Crash → bank failures → loans recalled → protectionism → world trade −66% → global Depression. Then two roads: democracies retreat, three regimes choose militarism.",
         beats=[
        "{ch}One schema holds part one together. How did a crash become a global depression? Six links. "
        "{ch.1}The Wall Street Crash, in October, nineteen twenty-nine: share prices collapse. "
        "{ch.2}Then the banks fail. Credit dries up, and savings are wiped out. "
        "{ch.3}The United States calls back its foreign loans. Europe loses American capital, and Germany above all. "
        "{ch.4}Protectionism follows: tariffs, and a chain of retaliation. "
        "{ch.5}World trade collapses. Its value falls by about two thirds, between nineteen twenty-nine and nineteen thirty-four. "
        "{ch.6}And the result is a global Depression, with mass unemployment and falling prices.",
        "{-ch}{deux}Part two follows from that. Faced with the Depression, the world takes two roads. "
        "The great democracies retreat. Economic nationalism, isolation, appeasement. "
        "And three regimes, in Germany, Italy and Japan, choose militarism.",
    ], vis={
        "ch": dict(type="liste", titre="How the crash became a global depression", items=[
            "Wall Street Crash (Oct. 1929): share prices collapse", "Banking failures: credit dries up, savings destroyed",
            "The US recalls its loans: Germany loses American capital", "Protectionism: tariffs and retaliation",
            "World trade collapses: about −66% (1929–1934)", "Global Depression: mass unemployment, deflation"],
            x=150, y=105, w=980),
        "deux": dict(type="cols", g="The democracies", gq="economic nationalism, then retreat: isolation and appeasement",
                     d="Three regimes", dq="Germany, Italy, Japan: militarism", vs="or"),
    }),

    # ================================================================ IV. I.1
    dict(id="p11", chap="I.1 · The Great Crash", fond="nuit", humeur="tension",
         retenir="Stock market · Roaring Twenties · mass production · speculation (margin: 90%) · a real economy already slowing · the panic: −89% (381 → 41).",
         beats=[
        "{ph}{i1}Now the ideas, part by part, with one example each. Part one, section one: what was the Great Crash? "
        "{i1.1}A stock market is where companies raise money, and investors buy a claim on profits. "
        "One example, from outside the course: RCA paid no dividend at all. Yet its share price multiplied.",
        "{i1.2}The Roaring Twenties brought growth and optimism, built on Republican policy. Three Republican presidents in a row: "
        "Harding, Coolidge, and Hoover. Low taxes. Trusts. Tariffs. {i1.3}Mass production made mass consumption possible. "
        "By nineteen twenty-five, a Ford Model T cost only about two hundred and sixty dollars.",
        "{i1.4}Speculation inflated the market. Brokers lent up to ninety per cent of a share's price. "
        "So a fall of just ten per cent wiped the buyer out. {i1.5}Meanwhile, the real economy was already slowing. "
        "Farm prices had been falling since nineteen twenty. {i1.6}Then, in late October, nineteen twenty-nine, came the panic. "
        "And the selling fed on itself.",
        "{-i1}{-ph}{dj}Remember one figure. In September, nineteen twenty-nine, the Dow Jones peaked at three hundred and eighty-one. "
        "By July, nineteen thirty-two, it was down to forty-one. A loss of eighty-nine per cent.",
        "{-dj}{fac}For an essay on the causes, rank the factors. Don't just list them. {fac.1}Speculation is the trigger. "
        "{fac.2}Overproduction and unequal wealth explain why the fall did not stop. "
        "{fac.3}And panic and policy made it worse. They are amplifiers, not the origin.",
    ], vis={
        "ph": dict(type="tableau", img="h1-wallstreet", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .6],
                   legende="Crowd outside the New York Stock Exchange after the Crash, October 1929 (Wikimedia Commons, public domain)"),
        "i1": dict(type="liste", titre="I.1 · What is the 1929 Great Crash?", items=[
            "A stock market: shares, dividends · RCA (outside the course)", "Roaring Twenties: Harding, Coolidge, Hoover",
            "Mass production: the Model T at about $260 (1925)", "Speculation: buying on margin, up to 90%",
            "Real economy slowing: farm prices falling since 1920", "The panic: 24–29 Oct. 1929, 16 million shares on the 29th"],
            x=130, y=105, w=1020),
        "dj": dict(type="mot", t="−89%", g="Dow Jones: 381 (Sept. 1929) → 41 (July 1932) · back only in 1954", y=250, taille=150),
        "fac": dict(type="liste", titre="The causes of the Crash: a hierarchy", items=[
            "Trigger: speculation (the market ×3 in 1924–29)", "Depth: overproduction, unequal wealth, no export markets",
            "Amplifiers: panic, Republican policy, no deposit insurance"], x=150, y=150, w=980),
    }),

    # ================================================================ V. I.2 et I.3
    dict(id="p12", chap="I.2 · A world-wide crisis", fond="nuit", humeur="tension",
         retenir="Bank failures (5,000 by 1932) · loans recalled · the Dawes circuit · the Gold Standard · dominoes in Europe, falling prices in the periphery.",
         beats=[
        "{i2}Section two: from the American crash to a world-wide crisis. {i2.1}The Great Depression really began when the banks failed. "
        "Before nineteen thirty-three, deposits were not insured. A rumour could empty a bank. About five thousand had failed by nineteen thirty-two.",
        "{i2.2}The crisis spread through two channels. The recall of American loans, and weaknesses that every economy shared. "
        "Watch the dominoes: the Creditanstalt in May, nineteen thirty-one. The German banks in July. Britain off gold in September. "
        "{i2.3}Why was Europe so fragile? Because the Dawes Plan had tied it to American credit. "
        "Eight hundred million marks were lent in nineteen twenty-four. And by nineteen twenty-eight, "
        "reparations had reached two and a half billion marks a year.",
        "{i2.4}The Gold Standard was the transmission belt. France clung to the franc's gold value until nineteen thirty-six. "
        "It was the worst-performing developed economy of the decade. {i2.5}Europe was hit by a domino effect. "
        "And the rest of the world, by falling prices. Brazil burned some seventy-eight million bags of coffee. "
        "Chile's nitrate earnings fell by more than eighty per cent.",
    ], vis={
        "i2": dict(type="liste", titre="I.2 · From the US Crash to a world-wide financial crisis", items=[
            "Bank failures: no deposit insurance, 5,000 by 1932", "Two channels: Creditanstalt (May 1931) → Germany → Britain",
            "The Dawes circuit: 800 million marks, reparations 2.5 billion a year", "The Gold Standard: France, worst performer until 1936",
            "Dominoes and falling prices: Brazil's coffee, Chile's nitrate"], x=130, y=110, w=1020),
    }),

    dict(id="p13", chap="I.3 · A defining trauma", fond="nuit", humeur="calme",
         retenir="14 million unemployed (25%) · Hoovervilles · Lange's Migrant Mother (1936) · the Dust Bowl (14 April 1935) · a global trauma, but uneven: the USSR barely touched.",
         beats=[
        "{hv}{i3}Section three: one of the defining traumas of the twentieth century. {i3.1}Jobs, wages and savings were destroyed, "
        "and there was no safety net. Unemployment rose from three per cent in nineteen twenty-nine to twenty-five per cent in nineteen thirty-three. "
        "That is fourteen million Americans.",
        "{i3.2}The Hoovervilles made poverty visible, right in the heart of the cities. The largest was in St Louis. Another stood in Central Park.",
        "{-hv}{mm}{i3.3}The federal state itself photographed poverty. This is Migrant Mother, by Dorothea Lange, March, nineteen thirty-six. "
        "Florence Owens Thompson, aged thirty-two, at a pea-pickers' camp in Nipomo, California. "
        "{i3.4}Then the Dust Bowl turned the economic crisis into an ecological one. On Black Sunday, the fourteenth of April, nineteen thirty-five, "
        "day turned into night. {i3.5}So the trauma was global. But it was uneven. The Soviet Union, outside world trade "
        "and in its first Five-Year Plan, was barely touched.",
        "{-mm}",
    ], vis={
        "hv": dict(type="tableau", img="h1-hooverville-seattle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .4, .5],
                   legende="Hooverville on the Seattle waterfront, 1933 · Seattle Municipal Archives (Wikimedia Commons, CC BY 2.0)"),
        "mm": dict(type="tableau", img="h1-lange-migrant", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.2, .5, .3],
                   legende="Dorothea Lange, Migrant Mother, Nipomo, March 1936 (Library of Congress, public domain)"),
        "i3": dict(type="liste", titre="I.3 · One of the defining traumas of the 20th century", items=[
            "No safety net: unemployment 3% (1929) → 25% (1933)", "Hoovervilles: St Louis, Central Park",
            "Photography as an argument: Migrant Mother (1936)", "The Dust Bowl: Black Sunday, 14 April 1935",
            "Global but uneven: the USSR barely touched"], x=130, y=110, w=1020),
    }),

    # ================================================================ VI. II.1 et II.2
    dict(id="p21", chap="II.1 · Economic nationalism", fond="nuit", humeur="tension",
         retenir="Independent internationalism · Smoot–Hawley (17 June 1930, 20,000 goods) · retaliation and imperial blocs (Ottawa 1932) · Roosevelt reverses the policy (gold 1933, RTAA 1934).",
         beats=[
        "{i4}Part two, section one: economic nationalism. {i4.1}Before the Crash, Hoover's America practised independent internationalism. "
        "American banks lent to Germany. But Washington signed no alliance. {i4.2}Then came protectionism. Smoot–Hawley raised duties "
        "on more than twenty thousand goods. Two years later, Smoot and Hawley both lost their seats.",
        "{i4.3}Protectionism spread by retaliation, and the empires closed into blocs. At Ottawa, in nineteen thirty-two, "
        "Britain and its dominions chose imperial preference. World trade lost two thirds of its value. "
        "{i4.4}Roosevelt reversed the policy. He left gold in nineteen thirty-three, and signed reciprocal trade agreements from nineteen thirty-four. "
        "About twenty, by nineteen thirty-nine. And not one with Germany, Italy or Japan.",
    ], vis={
        "i4": dict(type="liste", titre="II.1 · Economic nationalism", items=[
            "Independent internationalism: loans, but no alliance", "Smoot–Hawley (1930): 20,000 goods, 23 protests",
            "Retaliation and imperial blocs: Ottawa, 1932", "Roosevelt reverses it: about 20 agreements by 1939"],
            x=150, y=130, w=980),
    }),

    dict(id="p22", chap="II.2 · Political responses", fond="nuit", humeur="tension",
         retenir="Germany broke: 43.8% unemployed (1932) · the Nazis let in, never a majority · autarky and rearmament · militarism in three regimes · the New Deal · New Deal diplomacy · the Front populaire.",
         beats=[
        "{gr}Section two: the political responses. And first, Germany, the country that broke. {gr.1}Look at Worksheet three. "
        "Among insured workers, unemployment climbs from eight point six per cent in nineteen twenty-eight… "
        "to forty-three point eight per cent in nineteen thirty-two. "
        "{gr.2}Now the Nazi vote. It follows the curve. Two point six per cent in nineteen twenty-eight. Eighteen point three in nineteen thirty. "
        "Thirty-seven point three in July, nineteen thirty-two. Then, in November, it drops to thirty-three point one.",
        "{-gr}{i5}{i5.1}So the Nazis never won a majority. They were let in, in January, nineteen thirty-three, by conservatives "
        "who thought they could use Hitler. {i5.2}Nazi economic policy wanted stability, full employment and autarky, at any price. "
        "Rearmament cut unemployment from six million in nineteen thirty-three to under one million by nineteen thirty-seven. "
        "{i5.3}And militarism spread to three regimes. It means an armed build-up, the military in control of government, "
        "and an aggressive foreign policy. In Japan, the Kwantung Army struck first in Manchuria. Tokyo explained afterwards.",
        "{-i5}{i6}Now, three other answers. {i6.1}The New Deal: relief, recovery, reform. It brought the Civilian Conservation Corps, the Tennessee "
        "Valley Authority, and, in nineteen thirty-five, Social Security. {i6.2}New Deal diplomacy recognised the Soviet Union, in November, nineteen thirty-three. "
        "It signed trade agreements, but no alliance. {i6.3}And in France, the Front populaire of nineteen thirty-six, under Léon Blum. "
        "The Matignon Agreements raised wages by seven to fifteen per cent, in a week. New laws brought the forty-hour week, "
        "and two weeks of paid holiday. But abroad, it chose appeasement.",
    ], vis={
        "gr": dict(type="graphe", titre="Germany: unemployment and the Nazi vote (%)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50],
                           lx="year", ly="%"),
                   el=[dict(type="courbe", pts=CHOMAGE, c="ca", lbl="Unemployed (insured workers)", lp=[1928.1, 47], dur=2.0),
                       dict(type="courbe", pts=VOTE_NSDAP, c="el", lbl="NSDAP vote", lp=[1930.9, 12], dur=2.0)]),
        "i5": dict(type="liste", titre="II.2 · Germany, the regime that broke", items=[
            "Let in, never elected: Hitler chancellor, Jan. 1933", "Autarky and rearmament: 6 million → under 1 million unemployed",
            "Militarism in three regimes: the Kwantung Army in Manchuria"], x=150, y=140, w=980),
        "i6": dict(type="liste", titre="II.2 · The other answers", items=[
            "The New Deal: CCC, TVA, Social Security (1935)", "New Deal diplomacy: the USSR recognised, Nov. 1933",
            "The Front populaire (1936): Matignon, +7 to 15% wages"], x=150, y=140, w=980),
    }),

    # ================================================================ VII. II.3
    dict(id="p23", chap="II.3 · Reluctant democracies", fond="nuit", humeur="tension",
         retenir="Wilsonianism · a League weak from birth · Manchuria · the Stimson note · the Neutrality Acts · cash and carry · appeasement (six reasons) · Munich, Prague, Poland.",
         beats=[
        "{i7}Last part, II.3: great democracies reluctant to defend the liberal order of 1919. "
        "{i7.1}The order rested on Wilsonianism. A Punch cartoon of December 1919 already shows the keystone marked USA "
        "missing from the League's arch. {i7.2}The League had structural weaknesses: no army, a veto for every member. "
        "David Low's cartoon The Doormat, in 1933, shows a Japanese soldier stepping over it.",
        "{i7.3}It could not stop a great power: Manchuria, 1931 to 1933. The Lytton Commission condemned, and Japan simply left the League. "
        "{i7.4}The United States condemned in words only: the Stimson note of the seventh of January 1932… and Japan bombed Shanghai.",
        "{-i7}{i8}{i8.1}The Neutrality Acts, from 1935 to 1937, made the largest democracy unavailable, even after the USS Panay was bombed "
        "in December 1937. {i8.2}Only in 1939 did cash and carry turn America into the Arsenal of Democracy: "
        "the Sherman tanks of the Detroit Tank Arsenal. Rearmament, not the New Deal, ended the Depression.",
        "{i8.3}On the other side of the Atlantic, appeasement. In 1936, the German army entered the Rhineland with orders to withdraw "
        "at the first sign of French resistance. There was none. {i8.4}And appeasement let Hitler go further: Ethiopia, the Anschluss, "
        "Munich, Prague, Poland. Low drew it in 1936: Stepping Stones to Glory, Hitler climbing on the bent backs of the democracies.",
        "{-i8}{rais}Why appease? The course gives six reasons, and none of them is stupid. {rais.1}Pacifism: avoid another world war. "
        "{rais.2}Britain was policing its empire and could not afford major rearmament. {rais.3}Many Britons felt Germany had been "
        "treated unfairly in 1918. {rais.4}Their own economic problems came first. {rais.5}American isolationism left them unprotected. "
        "{rais.6}And they feared communism more than fascism.",
        "{-rais}{axe}One correction. The course places the Rome–Berlin–Tokyo pact between Munich and Prague. "
        "In fact, it was signed in September 1940, a date outside the course.",
    ], vis={
        "i7": dict(type="liste", titre="II.3 · The liberal order, undefended (1)", items=[
            "Wilsonianism: the USA, missing keystone (Punch, 1919)", "A weak League: no army, a veto each · The Doormat (1933)",
            "Manchuria 1931–33: Lytton condemns, Japan leaves", "Stimson note (7 Jan. 1932): words, then Shanghai bombed"],
            x=130, y=125, w=1020),
        "i8": dict(type="liste", titre="II.3 · The liberal order, undefended (2)", items=[
            "Neutrality Acts 1935–37: even after the USS Panay", "Cash and carry (1939): the Arsenal of Democracy",
            "Appeasement: the Rhineland, 7 March 1936", "Consequences: Munich (Sept. 1938) → Poland (1 Sept. 1939)"],
            x=130, y=125, w=1020),
        "rais": dict(type="liste", titre="Six reasons for appeasement", items=[
            "Pacifism: avoid another world war", "An empire to police, no money to rearm", "Germany treated unfairly in 1918?",
            "Their own economic problems first", "American isolationism: no protection", "Communism feared more than fascism"],
            x=150, y=105, w=980),
        "axe": dict(type="note", terme="A correction", cles=["1940", "1936"],
                    t="The three-power pact (Germany, Italy, Japan) was signed in September 1940, after Poland; the Rome–Berlin Axis dates from 1936.",
                    etape="Dates outside the course: the course places the pact between Munich and Prague.", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. personnes et chiffres
    dict(id="gens", chap="People and figures", fond="nuit", humeur="calme",
         retenir="Roosevelt · Hoover · Dawes · Smoot and Hawley · Lange · Wilson · Stimson · Hitler · Blum · Chamberlain and Daladier. ×3 · −89% · 14 million · −66% · 43.8%.",
         beats=[
        "{pe}Twelve people to know. {pe.1}Roosevelt, and the New Deal. {pe.2}Hoover, whose name went to the shanty towns. "
        "{pe.3}Charles Dawes and his plan. {pe.4}Smoot and Hawley, and their tariff. {pe.5}Dorothea Lange, the photographer, "
        "{pe.6}and Florence Owens Thompson, the face of Migrant Mother. {pe.7}Wilson, and the Fourteen Points. "
        "{pe.8}Stimson, and his note. {pe.9}Hitler, chancellor without a majority. {pe.10}Léon Blum, and the Front populaire. "
        "{pe.11}Chamberlain and Daladier, at Munich. {pe.12}And David Low, the cartoonist.",
        "{-pe}{chf}And seven figures. {chf.1}Times three: the stock market between 1924 and 1929. {chf.2}Minus eighty-nine per cent: "
        "the Dow Jones, to 1932. {chf.3}Fourteen million unemployed Americans, a quarter of all workers. "
        "{chf.4}Twenty thousand goods taxed by Smoot–Hawley. {chf.5}Minus sixty-six per cent: world trade, 1929 to 1934. "
        "{chf.6}Forty-three point eight per cent: German unemployment in 1932. {chf.7}And ten per cent: the British general tariff of 1932.",
    ], vis={
        "pe": dict(type="nuage", items=["Roosevelt", "Hoover", "Dawes", "Smoot & Hawley", "Dorothea Lange", "F. Owens Thompson",
                                        "Wilson", "Stimson", "Hitler", "Léon Blum", "Chamberlain & Daladier", "David Low"]),
        "chf": dict(type="liste", titre="Seven figures", items=[
            "×3 · the stock market, 1924–1929", "−89% · the Dow Jones, 1929–1932", "14 million unemployed · 25% of US workers",
            "20,000 goods · Smoot–Hawley", "−66% · world trade, 1929–1934",
            "43.8% · German unemployment, 1932", "10% · the British tariff, 1932"], x=170, y=95, w=940),
    }),

    # ================================================================ IX. à toi
    dict(id="atoi", chap="Your turn", fond="nuit", humeur="calme",
         retenir="24 Oct. 1929 · 17 June 1930 · 18 Sept. 1931 · Jan. 1933 · Sept. 1938.",
         beats=[
        "{pa}Your turn. Without looking: give five key dates of the chapter, with what happened, in one line each.",
        ("P", 2.0),
        "{-pa}{rep}Here is one answer. {rep.1}The twenty-fourth of October 1929: Black Thursday, the Crash begins. "
        "{rep.2}The seventeenth of June 1930: the Smoot–Hawley Tariff. {rep.3}The eighteenth of September 1931: the Mukden incident, "
        "Japan invades Manchuria. {rep.4}January 1933: Hitler is appointed chancellor. {rep.5}And September 1938: Munich, "
        "appeasement's defining act.",
    ], vis={
        "pa": dict(type="pause", t="Five key dates of the chapter, with what happened.",
                   sous="Pause the video, write them down, then play on to compare."),
        "rep": dict(type="liste", titre="A model answer", items=[
            "24 Oct. 1929 · Black Thursday: the Crash begins", "17 June 1930 · the Smoot–Hawley Tariff",
            "18 Sept. 1931 · Mukden: Japan invades Manchuria", "Jan. 1933 · Hitler appointed chancellor",
            "Sept. 1938 · Munich: appeasement's defining act"], x=170, y=130, w=940),
    }),

    # ================================================================ X. l'examen
    dict(id="examen", chap="Key terms and key issues", fond="nuit", humeur="lumiere",
         retenir="Key terms: World-wide Economic Depression · Appeasement. Key issues: the democracies' share of blame · economic nationalism, a key factor?",
         beats=[
        "{kt}Now the exam. Two key terms. The World-wide Economic Depression of the 1930s: "
        "a prolonged, global fall in output, with mass unemployment and severe deflation. "
        "And appeasement: conceding to an aggressor's demands in the hope of avoiding war.",
        "{-kt}{ki1}And two key issues, which can come up at the oral. The first one: "
        "blame for the origins of the Second World War lies in part with the great democratic powers themselves. How far do you agree?",
        "{-ki1}{pl1}A plan in three parts. {pl1.1}One: the democracies built an order they would not underwrite, and weakened it "
        "after 1929: the Senate refused Versailles; Smoot–Hawley cut world trade by two thirds. "
        "{pl1.2}Two: they refused to defend it when tested: Manchuria, the Neutrality Acts, no oil embargo on Italy, the Rhineland, Munich. "
        "{pl1.3}Three: but the initiative lay with the militarist regimes, in Berlin, Rome and Tokyo. "
        "{pl1.4}So, agree in part. The course's own word is the right one: reluctant. They could have acted, and chose not to.",
        "{-pl1}{ki2}The second key issue: how far do you agree that economic nationalism was the key factor in the slide towards war in 1939?",
        "{-ki2}{pl2}Again, three parts. {pl2.1}One: economic nationalism corroded the international order: tariffs, quotas, "
        "imperial blocs, and autarky made conquest look rational. {pl2.2}Two: but it is a symptom as much as a cause: "
        "the chain starts on Wall Street, not in the customs houses. {pl2.3}Three: ideology competes for the same place: "
        "militarism in three regimes, and Nazi plunder that no trade barrier explains. "
        "{pl2.4}Conclusion: economic factors created the opportunity; ideology supplied the intent.",
    ], vis={
        "kt": dict(type="cols", g="World-wide Economic Depression", gq="a prolonged, global fall in output: mass unemployment, severe deflation",
                   d="Appeasement", dq="conceding to an aggressor's demands in the hope of avoiding war", vs="+"),
        "ki1": dict(type="question", t="Key issue 1 · The democracies' share of the blame for WWII: how far do you agree?"),
        "pl1": dict(type="liste", titre="Key issue 1 · a plan in three parts", items=[
            "I. An order they would not underwrite, then weakened (Versailles refused, Smoot–Hawley)",
            "II. They refused to defend it: Manchuria, Neutrality Acts, Rhineland, Munich",
            "III. But the initiative lay with Berlin, Rome and Tokyo",
            "Agree in part: “reluctant” — they could act, and chose not to"], x=130, y=120, w=1020),
        "ki2": dict(type="question", t="Key issue 2 · Economic nationalism, the key factor in the slide towards war?"),
        "pl2": dict(type="liste", titre="Key issue 2 · a plan in three parts", items=[
            "I. It corroded the order: tariffs, quotas, blocs, autarky",
            "II. A symptom as much as a cause: the chain starts on Wall Street",
            "III. Ideology competes: militarism, Nazi plunder",
            "Economic factors gave the opportunity; ideology, the intent"], x=130, y=120, w=1020),
    }),

    # ================================================================ XI. vers le chapitre 2
    dict(id="suite", chap="Towards chapter 2", fond="nuit", humeur="tension",
         retenir="March 1939 Prague · 1 Sept. 1939 Poland · Nov. 1939 cash and carry. Chapter 2: the totalitarian regimes.",
         beats=[
        "{g3}{g3.1}And the end of the story. In March 1939, Germany occupies Prague: Munich bought nothing. "
        "On the first of September 1939, Germany invades Poland; France and Britain declare war. "
        "{g3.2}In November, cash and carry: the United States starts to supply the democracies.",
        "{-g3}{g4}{g4.1}Chapter two picks up exactly here: the totalitarian regimes whose militarism the reluctant democracies "
        "failed to check. Three regimes, one trajectory. {g4.2}And one date links the two chapters: the thirtieth of January 1933, "
        "when Hitler is appointed chancellor, in the middle of the Depression.",
        "{-g4}",
    ], vis={
        "g3": dict(type="globe", code="H1", sc=[31, 32]),
        "g4": dict(type="globe", code="H2", sc=[0, 20]),
    }),

    # ================================================================ récap final
    dict(id="fin", chap="The whole chapter", fond="nuit", humeur="calme", beats=[
        "{carte}One last map of the chapter. {carte.1}The Crash: speculation, then panic, in October 1929. "
        "{carte.2}The world crisis: banks, loans, gold… and fourteen million unemployed, the Hoovervilles, the Dust Bowl. "
        "{carte.3}Economic nationalism: Smoot–Hawley, and the imperial blocs. "
        "{carte.4}The political answers: Hitler, the New Deal, the Front populaire. {carte.5}And the liberal order, undefended: "
        "the League, neutrality, appeasement.",
        ("P", 5.0),
        "{-carte}{fin}That is the end of the series on chapter one. Now, do the quiz… and on to chapter two.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="THE CRASH AND ITS IMPACT", branches=[
            dict(t="The Crash", items=["speculation · margin", "24–29 Oct. 1929 · −89%"]),
            dict(t="A world crisis", items=["banks · loans · gold", "14 million unemployed · Dust Bowl"]),
            dict(t="Economic nationalism", items=["Smoot–Hawley (1930)", "imperial blocs · trade −66%"]),
            dict(t="Political answers", items=["Hitler · militarism", "New Deal · Front populaire"]),
            dict(t="The order undefended", items=["League · Neutrality Acts", "appeasement · Munich"])]),
        "fin": dict(type="mot", t="Next: chapter 2", g="H2 · Totalitarian regimes", y=270, taille=88),
    }),
]

QUIZ = [
    dict(q="How much did the Dawes Plan lend to Germany in 1924?", r=["800 million marks", "2.5 billion marks a year",
         "20 million Reichsmarks a day", "14 million dollars"], ok=0, voir="g1",
         ex="American money at the start of the chain: reparations, then war debts back to Washington."),
    dict(q="When did the Great Depression really begin, according to the course?", r=["When numerous banks started failing",
         "On Black Thursday", "When Hitler came to power", "With the Dust Bowl"], ok=0, voir="ch",
         ex="No deposit insurance before 1933: about 5,000 banks had failed by 1932."),
    dict(q="By how much did the Dow Jones fall between September 1929 and July 1932?", r=["−89%", "−40%", "−25%", "−66%"],
         ok=0, voir="dj", ex="From 381 to 41; −66% is world trade, 1929–1934."),
    dict(q="Which factor is best described as the trigger of the Crash?", r=["Speculation", "The Dust Bowl", "The Neutrality Acts",
         "The Gold Standard"], ok=0, voir="fac",
         ex="Speculation explains the suddenness; overproduction and inequality explain the depth."),
    dict(q="In which order did the dominoes fall in 1931?", r=["Creditanstalt → German banks → Britain off gold",
         "Britain off gold → Creditanstalt → German banks", "German banks → France → Creditanstalt", "France → Britain → Germany"],
         ok=0, voir="i2", ex="May, July, September 1931."),
    dict(q="Who is the woman in Dorothea Lange's Migrant Mother (1936)?", r=["Florence Owens Thompson", "Melita Maschmann",
         "Eleanor Roosevelt", "An actress paid by the government"], ok=0, voir="i3",
         ex="Aged 32, at a pea-pickers' camp in Nipomo, California."),
    dict(q="What did the Smoot–Hawley Tariff (17 June 1930) do?", r=["Raised duties on over 20,000 imported goods",
         "Insured bank deposits", "Took the US off gold", "Lent money to Germany"], ok=0, voir="i4",
         ex="Canada retaliated within days; world trade lost two thirds of its value."),
    dict(q="German unemployment among insured workers in 1932 (Worksheet 3)?", r=["43.8%", "8.6%", "25%", "37.3%"], ok=0,
         voir="gr", ex="37.3% is the Nazi vote in July 1932; 25% is US unemployment in 1933."),
    dict(q="Which is NOT one of the six reasons for appeasement?", r=["Fear of a Japanese invasion of Britain",
         "Pacifism", "Fear of communism more than fascism", "Their own economic problems"], ok=0, voir="rais",
         ex="Also: an empire to police, Germany treated unfairly, American isolationism."),
    dict(q="What is appeasement?", r=["Conceding to an aggressor's demands in the hope of avoiding war",
         "A refusal to trade with dictatorships", "An alliance against Germany", "The American policy of neutrality"], ok=0,
         voir="kt", ex="A key term of the chapter; its defining act is Munich, September 1938."),
]

CREDITS = [
    "Content: the synthesis of M. Ros's course (DNL History, H1 “The Wall Street Crash and its Impact”) as written on the site: "
    "timeline, the chain of the crisis, the ideas of Parts I.1 to II.3, key figures, key terms and key issues, Worksheet 3; "
    "the animated maps of chapters 1 and 2 (site).",
    "Course correction: the three-power (Rome–Berlin–Tokyo) pact dates from September 1940, not between Munich and Prague; "
    "the Rome–Berlin Axis from 1936 (outside the course).",
    "Photographs: crowd outside the New York Stock Exchange, October 1929 (Wikimedia Commons, public domain); "
    "Hooverville on the Seattle waterfront, 1933 (Seattle Municipal Archives, via Wikimedia Commons, CC BY 2.0); "
    "Dorothea Lange, Migrant Mother, 1936 (Library of Congress, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
