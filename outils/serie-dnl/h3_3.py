"""DNL History · H3 « World War Two » — série vidéo, épisode 3 : « Britain alone » (partie I.2 du cours,
« The British resistance supported by the US »).

Même chaîne que l'épisode 1 (voir h3_1.py) : outils/serie-philo/generer.py h3_3 ; sortie dans dnl/serie/.
Cartes animées (sc = numéros de scènes dans l'ordre chronologique de la carte) :
  H3 : 10 Norvège · 11 attaque à l'ouest, Churchill · 13 Dunkerque · 15 appel du 18 Juin · 16 armistice ·
       17 le Royaume-Uni seul, deux stratégies · 20 le Blitz · 21 le Royaume-Uni tient, l'Amérique le fournit ·
       25 Barbarossa · 26 avance allemande · 30 arrêt devant Moscou · 31 Pearl Harbor · 33 la guerre devient mondiale
  H1 : 26 Neutrality Acts · 32 cash and carry, l'arsenal de la démocratie
Contenu : les sept idées de la partie I.2 dans le site (dnl/index.html, CHAPTERS.H3), la Worksheet 2 (H3WS2 : documents,
tableau qui / quand / à qui / pour quoi, bilan — réponse proposée par le site, pas un corrigé de M. Ros), la frise et les
chiffres du chapitre, le point « 43 000 civils » de H3Check ; rappels du chapitre 1 (Neutrality Acts, cash and carry).
Hors cours, dit comme tel : Lend-Lease (mars 1941), opération Sea Lion, bataille d'Angleterre.
La question de DBQ et sa copie modèle sont écrites pour la vidéo et dites comme telles.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h3-3"
NOTION = "World War Two"
NUM = 3
TITRE = "Britain alone"
SUIVANT = "Episode 4 · Barbarossa: a war of annihilation"
PRONONCIATION = {"Jodl": "Yoh-dl", "Luftwaffe": "Looft-vaffa", "Reynaud": "Ray-no", "Pétain": "Pay-tan",
                 "Rethondes": "Ruh-tond", "Wehrmacht": "Vair-markt", "Vichy": "Vee-shee"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False,
         retenir="The question of this episode: how could Britain hold out alone against Nazi Germany, from June 1940 to December 1941?",
         beats=[
        "{g0}{q1}June 1940. In six weeks, France has fallen. Norway, Denmark, the Netherlands and Belgium are occupied. "
        "In the west, only one of Hitler's enemies is still standing: Britain.",
        "{-q1}{q2}Everyone expects Britain to negotiate, or to be invaded. It does neither. "
        "How could an island hold out alone against the Nazi war machine, for a year and a half?",
        "{-q2}{-g0}{plan}Here is the plan of this episode. {plan.1}First, the story on the map, from Dunkirk to Pearl Harbor. "
        "{plan.2}Then the course, idea by idea: Jodl's two strategies, the Blitz, and why Britain held. "
        "{plan.3}Then two men who refused defeat, Churchill and de Gaulle, and Worksheet 2. "
        "{plan.4}Then America, the Arsenal of Democracy, and December 1941, when the war goes global. "
        "{plan.5}And finally, an exam workshop: a DBQ question on Churchill's speech.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[17]),
        "q1": dict(type="question", t="June 1940: Britain stands alone.", bande=True),
        "q2": dict(type="question", t="How could an island hold out?", bande=True),
        "plan": dict(type="liste", titre="Episode 3 · Britain alone", items=[
            "On the map: from Dunkirk to Pearl Harbor", "Jodl's two strategies, the Blitz, why Britain held",
            "Churchill, de Gaulle and Worksheet 2", "The Arsenal of Democracy, December 1941",
            "At the exam: a DBQ question"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H3 · Episode 3", t="Britain alone",
                      sous="1940 – 1941 · the British resistance, supported by the US"),
    }),

    # ================================================================ I. sur la carte : l'été 1940
    dict(id="ete40", chap="Summer 1940, on the map", fond="nuit", humeur="tension",
         retenir="April 1940 Norway · 10 May Churchill prime minister · 26 May – 4 June Dunkirk: 338,000 evacuated · 18 June de Gaulle's appeal · 22 June the armistice: Britain alone.",
         beats=[
        "{g1}{g1.1}April 1940. The phoney war is still on in the west, but Germany occupies Denmark and invades Norway. "
        "Britain fails to prevent it. In London, Prime Minister Neville Chamberlain loses the support of the House of Commons.",
        "{g1.2}The tenth of May 1940: the German attack in the west begins, through the Netherlands, Belgium and Luxembourg. "
        "The same day, Chamberlain resigns, and Winston Churchill becomes prime minister.",
        "{g1.3}At the end of May, the British army is trapped against the coast, at Dunkirk. Operation Dynamo: "
        "from the twenty-sixth of May to the fourth of June, three hundred and thirty-eight thousand Allied soldiers are evacuated by sea to England. "
        "The army is saved, and the Royal Navy and the RAF are intact. On the fourth of June, Churchill tells the Commons: we shall never surrender.",
        "{-g1}{g2}{g2.1}The eighteenth of June. Marshal Pétain, now head of the French government, has asked for an armistice. "
        "From London, a French general almost nobody knows, Charles de Gaulle, speaks on BBC radio: the flame of French resistance must not die.",
        "{g2.2}The twenty-second of June: the armistice is signed at Rethondes. France is cut up, three fifths of it occupied. That was episode two.",
        "{g2.3}And now look at the map. From Norway to the Pyrenees, the coasts facing Britain are in German hands. "
        "The Wehrmacht is just across the Channel. {!Britain is alone}Britain is alone.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[10, 11, 13]),
        "g2": dict(type="globe", code="H3", sc=[15, 16, 17]),
    }),

    # ================================================================ II. sur la carte : du Blitz à Pearl Harbor
    dict(id="blitz41", chap="From the Blitz to Pearl Harbor", fond="nuit", humeur="tension",
         retenir="7 Sept. 1940 the Blitz · Dec. 1940 invasion postponed indefinitely · the US, Arsenal of Democracy · 22 June 1941 Barbarossa · 7 Dec. 1941 Pearl Harbor · 11 Dec. Germany and Italy at war with the US.",
         beats=[
        "{g3}{g3.1}The seventh of September 1940: the Luftwaffe, the German air force, begins its evening raids on London. "
        "This is the Blitz. Docks, factories and whole streets of the East End burn.",
        "{g3.2}But the German air force never wins control of the sky. In December 1940, the invasion of Britain is postponed indefinitely: "
        "Hitler has turned to the East. And across the Atlantic, the United States, still neutral, becomes Britain's supplier: "
        "the Arsenal of Democracy.",
        "{-g3}{g4}{g4.1}The twenty-second of June 1941: Germany invades the Soviet Union. Operation Barbarossa. "
        "Britain is no longer the only country fighting Germany.",
        "{g4.2}The seventh of December 1941: Japan bombs the American base of Pearl Harbor, in Hawaii. "
        "{g4.3}Four days later, Germany and Italy declare war on the United States. The war is now global, and Britain is no longer alone.",
        "{-g4}{fr1}Eighteen months in eight dates. Copy them down. {fr1.1}The tenth of May 1940, Churchill becomes prime minister. "
        "{fr1.2}The end of May, Dunkirk. {fr1.3}The eighteenth of June, de Gaulle's appeal. {fr1.4}The twenty-second of June, the armistice. "
        "{fr1.5}The seventh of September, the Blitz. {fr1.6}December 1940, the invasion postponed. "
        "{fr1.7}The twenty-second of June 1941, Barbarossa. {fr1.8}And the seventh of December 1941, Pearl Harbor.",
        ("P", 2.5),
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[20, 21]),
        "g4": dict(type="globe", code="H3", sc=[25, 31, 33]),
        "fr1": dict(type="frise", items=[
            dict(nom="Churchill", d=1940, q="10 May: prime minister"), dict(nom="Dunkirk", d=1940, q="26 May – 4 June"),
            dict(nom="De Gaulle", d=1940, q="18 June: the appeal"), dict(nom="Armistice", d=1940, q="22 June"),
            dict(nom="The Blitz", d=1940, q="7 Sept.: London"), dict(nom="Invasion off", d=1940, q="Dec.: postponed"),
            dict(nom="Barbarossa", d=1941, q="22 June"), dict(nom="Pearl Harbor", d=1941, q="7 Dec."),
        ]),
    }),

    # ================================================================ III. idée 1 : les deux stratégies de Jodl
    dict(id="jodl", chap="Jodl's choice: two strategies", fond="guerre", humeur="tension",
         retenir="Jodl, June 1940: a direct attack (air and sea offensive + bombing of industry, terror bombing of cities, a landing) or a peripheral war (the Mediterranean, the trade routes).",
         beats=[
        "{q3}Now, the course, idea by idea. France is beaten. How do you beat Britain?",
        "{-q3}{jo}In June 1940, Alfred Jodl, Chief of the Operations Staff of the German Armed Forces, sets out the choice in a memorandum. "
        "Two strategies. Either, in his own words, a direct attack on the English motherland. "
        "{jo.1}Or an extension of the war to peripheral areas: the Mediterranean, and the trade routes, to strangle Britain from the outside.",
        "{-jo}{dir}The direct strategy itself could take three forms. {dir.1}One: an offensive by air and sea against British shipping, "
        "combined with air attacks on centres of industry. {dir.2}Two: terror attacks by air against population centres, that is, the cities. "
        "{dir.3}And three, finally: a landing, to occupy England. Notice the order. The landing comes last: {!first, the air}first, the air.",
        "{-dir}{g5}{g5.1}And look at what happened. The second form, terror from the air, is exactly what the Germans put into practice. "
        "{g5.2}Monsieur Ros's slide shows a Luftwaffe bomber flying over the East End of London, at the start of the evening raids "
        "of the seventh of September 1940. That is the Blitz.",
    ], vis={
        "q3": dict(type="question", t="France is beaten. How do you beat Britain?"),
        "jo": dict(type="cols", g="Direct", gq="“a direct attack on the English motherland”", d="Peripheral",
                   dq="“an extension of the war to peripheral areas”: Mediterranean, trade routes", vs="or",
                   repere="Alfred Jodl's memorandum, June 1940"),
        "dir": dict(type="liste", titre="A direct attack: three forms", cles=["shipping", "terror", "landing"], items=[
            "Air and sea offensive against British shipping + air attacks on industry",
            "Terror attacks by air against population centres", "Finally, a landing to occupy England"], x=170, y=140, w=940),
        "g5": dict(type="globe", code="H3", sc=[17, 20]),
    }),

    # ================================================================ IV. idée 2 : le Blitz
    dict(id="blitz", chap="The Blitz", fond="guerre", humeur="tension",
         retenir="The Blitz (1940–41): defeat the RAF first, then break industry (docks, factories) and the people's will (cities). About 43,000 civilians killed in Britain.",
         beats=[
        "{ph}{def3}A key word of this lesson: the {!Blitz}Blitz. The German bombing campaign against the United Kingdom, in 1940 and 1941. "
        "{def3.1}Its aim: to bomb Britain into submission.",
        "{-def3}{lo}Follow the German logic. {lo.1}An invasion requires the defeat of the Royal Air Force, the RAF. "
        "{lo.2}So the air war comes first. {lo.3}The bombers strike docks and factories, to break British industry. "
        "{lo.4}And above all, cities, to break the will of the population.",
        "{-lo}{civ}This means that civilians are in the front line, as they had been in Spain, during the civil war, and in Poland, in 1939. "
        "{civ.1}Look at these children of East London, sitting in front of what was their home. In this war, the home is a battlefield.",
        "{-civ}{hp}Another photograph on Monsieur Ros's slide: anti-aircraft guns set up in Hyde Park, in the heart of the capital. "
        "The front line runs through the middle of London.",
        "{-hp}{chif}And the toll. The course gives forty-three thousand civilians killed in London. "
        "{chif.1}Be careful: this figure is usually the one for the whole United Kingdom during the Blitz, and about half of them died in London. "
        "In an essay, write: about forty-three thousand civilians killed in Britain.",
        "{-chif}{-ph}",
    ], vis={
        "ph": dict(type="tableau", img="h3-blitz", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .62],
                   legende="Children of an eastern suburb of London made homeless by a night raid, September 1940 · New Times Paris Bureau Collection (USIA), US National Archives 306-NT-3163V, public domain"),
        "def3": dict(type="def", cles=["bombing", "1940", "1941"], terme="Key word · the Blitz",
                     t="The German bombing campaign against the United Kingdom, in 1940 and 1941.",
                     etape="Aim: to bomb Britain into submission", x=170, y=200, w=940),
        "lo": dict(type="liste", titre="The German logic", cles=["RAF", "air", "industry", "will"], items=[
            "An invasion requires the defeat of the RAF", "So the air war comes first",
            "Docks and factories → break British industry", "Above all cities → break the will of the population"],
                   x=170, y=140, w=940),
        "civ": dict(type="note", terme="Civilians in the front line", cles=["Spain", "Poland"],
                    t="As in Spain and in Poland, the bombers target the population itself.",
                    etape="East London, 1940: the home is a battlefield", x=170, y=420, w=940),
        "hp": dict(type="note", terme="On M. Ros's slide", cles=["Hyde", "Park"],
                   t="Anti-aircraft guns set up in Hyde Park, in the heart of the capital.",
                   etape="The front line runs through London", x=170, y=200, w=940),
        "chif": dict(type="note", terme="Watch out · a figure to check", cles=["43,000"],
                     t="The course: 43,000 civilians killed in London during the Blitz.",
                     etape="Usually the figure for the whole UK, about half in London. Write: “in Britain”.", x=170, y=200, w=940),
    }),

    # ================================================================ V. idée 3 : pourquoi le Royaume-Uni tient
    dict(id="tenir", chap="Why Britain held", fond="nuit", humeur="lumiere",
         retenir="No air superiority over south-east England, no landing. Dec. 1940: first order to invade the USSR, invasion of Britain postponed indefinitely. Britain stopped the Nazi machine by holding out.",
         beats=[
        "{g6}{ch1}The third idea answers our question. {ch1.1}An invasion depended on air superiority, control of the air, "
        "over south-eastern England, where the landing would take place. {ch1.2}The German air force failed to win it in 1940. "
        "{ch1.3}So Hitler postponed the invasion, first until the spring of 1941. "
        "{ch1.4}Then, in December 1940, the first operational order for the invasion of the Soviet Union was issued, "
        "and the invasion of Britain was postponed indefinitely. Germany had turned its forces to the East.",
        "{-ch1}{-g6}{hold}So Britain was the first country to stop the Nazi war machine. Not by defeating it. {!By holding out}By holding out. "
        "That is a strong sentence for an essay: Britain did not win in 1940, but it did not lose, and that was enough to change the war.",
        "{-hold}{hors}Two names you will find in books, although they are not in the course. {hors.1}The invasion plan was code-named Operation Sea Lion, "
        "and the air battle of the summer of 1940 is known as the Battle of Britain. "
        "You may use them, but the words of the course are enough: air superiority, the Luftwaffe, the RAF.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[21]),
        "ch1": dict(type="liste", titre="Why there was no invasion", bande=True, petit=True, x=60, y=130, w=620,
                    cles=["air", "superiority", "failed", "indefinitely"], items=[
                        "A landing needs air superiority over south-east England", "1940: the Luftwaffe fails to win it",
                        "Invasion postponed to spring 1941", "Dec. 1940: first order to invade the USSR; invasion postponed indefinitely"]),
        "hold": dict(type="mot", t="Not defeating it: holding out", g="Britain did not win in 1940, but it did not lose — enough to change the war", y=250, taille=76),
        "hors": dict(type="note", terme="Outside the course", cles=["Sea", "Lion", "Battle", "Britain"],
                     t="The invasion plan: Operation Sea Lion. The air battle of summer 1940: the Battle of Britain.",
                     etape="Useful names, but the course's words are enough: air superiority, Luftwaffe, RAF.", x=170, y=200, w=940),
    }),

    # ================================================================ VI. idée 4 : deux hommes refusent la défaite
    dict(id="hommes", chap="Two men refuse defeat", fond="nuit", humeur="tension",
         retenir="Churchill: a Conservative against appeasement, prime minister on 10 May 1940. De Gaulle: a new general in Reynaud's government, refuses Pétain's armistice, flees to London on 17 June.",
         beats=[
        "{pwc}{wc}Fourth idea: in June 1940, two men refuse defeat. Churchill first. "
        "{wc.1}He is already a major figure of the Conservative party, and he had opposed appeasement, the policy of giving way to Hitler. "
        "{wc.2}In April 1940, during the phoney war, Britain fails to prevent the German occupation of Norway. "
        "{wc.3}Chamberlain loses the support of the House of Commons, and when German forces invade Belgium, he resigns. "
        "{wc.4}On the tenth of May 1940, the very day the German offensive in the west begins, Churchill becomes prime minister.",
        "{-wc}{-pwc}{dg}Now de Gaulle. {dg.1}He has just been promoted general, and appointed to Paul Reynaud's government. "
        "{dg.2}But Reynaud resigns, and Marshal Pétain, a hero of the First World War, becomes head of the government, pledging to sign an armistice. "
        "{dg.3}De Gaulle refuses. On the seventeenth of June, he flees France to escape arrest, "
        "{dg.4}and in London he meets Churchill. The next day, he speaks on the BBC.",
        "{-dg}{cmp1}Two men, two very different positions in June 1940. {cmp1.1}One governs a country that is still fighting. "
        "The other is a rebel, almost alone, whose own government has given up. Keep this contrast in mind: it is the key to Worksheet 2.",
    ], vis={
        "pwc": dict(type="tableau", img="h3-churchill", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .28],
                    legende="Winston Churchill, Ottawa, December 1941, by Yousuf Karsh (Library and Archives Canada, Wikimedia Commons, CC BY 2.0)"),
        "wc": dict(type="liste", titre="Winston Churchill", cles=["appeasement", "Norway", "Commons", "10"], items=[
            "A major Conservative, who had opposed appeasement", "April 1940: Britain fails to prevent the occupation of Norway",
            "Chamberlain loses the Commons; Belgium invaded: he resigns", "10 May 1940: prime minister, the day the attack in the west begins"],
                   x=150, y=130, w=980),
        "dg": dict(type="liste", titre="Charles de Gaulle", cles=["general", "Pétain", "refuses", "Churchill"], items=[
            "Newly promoted general, in Paul Reynaud's government", "Reynaud resigns; Pétain, a WWI hero, pledges an armistice",
            "He refuses, and flees France on 17 June to escape arrest", "In London, he meets Churchill"], x=150, y=130, w=980),
        "cmp1": dict(type="cols", g="Churchill", gq="Head of government of a country still fighting", d="De Gaulle",
                     dq="A rebel general, almost alone: his government has given up", vs="≠"),
    }),

    # ================================================================ VII. Worksheet 2 : les deux documents
    dict(id="docs", chap="Worksheet 2: two speeches", fond="guerre", humeur="tension",
         retenir="Doc. B, Churchill, 4 June 1940, Commons: “we shall never surrender”. Doc. A, de Gaulle, 18 June 1940, BBC: “the flame of French resistance must not and shall not die”.",
         beats=[
        "{ws}Worksheet 2 puts their two speeches side by side. The task: compare and contrast their attitudes towards the Axis. "
        "{ws.1}Compare and contrast means: the similarities and the differences, talking about both men all the way through, side by side.",
        "{-ws}{docb}Document B first, because it comes first in time. {docb.1}The fourth of June 1940, before the House of Commons, "
        "at the end of the Dunkirk evacuation. {docb.2}Churchill is confident: Britain will defend the island, if necessary for years, if necessary alone. "
        "{docb.3}The British Empire and the French Republic will defend their soil to the death. "
        "{docb.4}And if the island fell, the Empire and the fleet would carry on the struggle. Then come the most famous lines.",
        "{-docb}",
        ("C", "we shall fight on the beaches … we shall never surrender", "c_wc"),
        "{-c_wc}{doca}Document A. {doca.1}The eighteenth of June 1940, on BBC radio, from London: the day after Pétain asked for an armistice. "
        "{doca.2}For de Gaulle, the defeat came from German tanks, planes and tactics, more than from numbers. "
        "{doca.3}France does not stand alone: she has her empire, the British Empire that commands the seas, and the industry of the United States. "
        "This is a world war. {doca.4}So he calls on the French officers, soldiers, engineers and workers on British soil to join him. And he ends:",
        "{-doca}",
        ("C", "the flame of French resistance must not and shall not die", "c_dg"),
        "{-c_dg}",
    ], vis={
        "ws": dict(type="def", cles=["compare", "contrast"], terme="Worksheet 2 · the task",
                   t="De Gaulle and Churchill: compare and contrast their attitudes towards the Axis.",
                   etape="Similarities and differences, both men all the way through, side by side", x=170, y=200, w=940),
        "docb": dict(type="liste", titre="Document B · Churchill, “We shall never surrender”", items=[
            "4 June 1940 · House of Commons · end of the Dunkirk evacuation", "“if necessary for years, if necessary alone”",
            "The British Empire and the French Republic will defend their soil to the death",
            "If the island fell, the Empire and the fleet would carry on"], x=150, y=130, w=980),
        "c_wc": dict(type="cit", a="Winston Churchill", o="House of Commons, 4 June 1940", x=200, y=200, w=880),
        "doca": dict(type="liste", titre="Document A · De Gaulle, the Appeal of 18 June 1940", items=[
            "BBC radio, London · the day after Pétain asked for an armistice", "Defeat came from German tanks, planes and tactics",
            "“France does not stand alone”: empire, British fleet, American industry",
            "A call to officers, soldiers, engineers and workers on British soil"], x=150, y=130, w=980),
        "c_dg": dict(type="cit", a="Charles de Gaulle", o="Appeal of 18 June 1940, BBC (English translation)", x=200, y=200, w=880),
    }),

    # ================================================================ VIII. idée 5 : comparer
    dict(id="comparer", chap="Compare and contrast", fond="nuit", humeur="lumiere",
         retenir="Similarities: the battle of France does not decide the war; both count on the empires, the British fleet and US industry. Differences: who, when, to whom, what for.",
         beats=[
        "{com}Fifth idea: the two speeches share one analysis. {!a world war}The battle of France does not decide the war. "
        "{com.1}Both men count on empires that remain intact. {com.2}Both count on the British fleet, which commands the seas. "
        "{com.3}And both count on the industrial resources of the United States. Listen to them. De Gaulle first.",
        "{-com}",
        ("C", "This is a world war … Like England, she can draw unreservedly on the immense industrial resources of the United States.", "c_dg2"),
        "{-c_dg2}And Churchill.",
        ("C", "our Empire beyond the seas … would carry on the struggle, until, in God's good time, the New World, "
              "with all its power and might, steps forth to the rescue and the liberation of the old.", "c_wc2"),
        "{-c_wc2}{dif}The differences are just as clear. Use the four questions of the worksheet. "
        "{dif.1}Who? Churchill is the prime minister, a major figure of his party; de Gaulle, a recently promoted general, almost unknown, in exile. "
        "{dif.2}When? Churchill speaks on the fourth of June, before the armistice; de Gaulle on the eighteenth, after his own government has asked for one. "
        "{dif.3}To whom? Churchill speaks to Parliament, and through it to a united nation; de Gaulle to individuals he must rally. "
        "{dif.4}What for? Churchill prepares his country to fight alone; de Gaulle refuses the armistice wanted by his own government.",
        "{-dif}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is one way to build it. {rep1.1}Paragraph one, the similarities: both refuse defeat, and both see a world war, "
        "won with the empires, the fleet and the United States. {rep1.2}Paragraph two, the differences: the speaker, the date, the audience, the aim. "
        "{rep1.3}And in each paragraph, quote both men, side by side. "
        "{rep1.4}A last sentence to conclude: two speeches, one bet, that Britain could hold out until America came in. December 1941 proved them right.",
    ], vis={
        "com": dict(type="liste", titre="What the two speeches share", cles=["empires", "fleet", "United", "States"], items=[
            "Empires that remain intact", "The British fleet, which commands the seas", "The industrial resources of the United States"],
                    x=170, y=150, w=940),
        "c_dg2": dict(type="cit", a="Charles de Gaulle", o="Appeal of 18 June 1940 (English translation)", x=200, y=170, w=880),
        "c_wc2": dict(type="cit", a="Winston Churchill", o="House of Commons, 4 June 1940", x=200, y=150, w=880),
        "dif": dict(type="liste", titre="The differences (Worksheet 2)", cles=["Who", "When", "whom", "What"], items=[
            "Who? A prime minister ≠ an almost unknown general in exile",
            "When? 4 June, before the armistice ≠ 18 June, after the request",
            "To whom? Parliament and a united nation ≠ individuals to rally",
            "What for? To fight alone ≠ to refuse his government's armistice"], x=120, y=130, w=1040),
        "pa1": dict(type="pause", t="Plan a “compare and contrast” answer on the two speeches, in two paragraphs.",
                    sous="Pause the video, write your plan, then play on to compare."),
        "rep1": dict(type="liste", titre="A model plan", items=[
            "Similarities: refusal of defeat, a world war, empires, fleet, USA", "Differences: speaker, date, audience, aim",
            "Quote both men in each paragraph", "Conclude: one bet, proved right in December 1941"], x=170, y=140, w=940),
    }),

    # ================================================================ IX. idée 6 : l'arsenal de la démocratie
    dict(id="arsenal", chap="The Arsenal of Democracy", fond="nuit", humeur="lumiere",
         retenir="Neutrality Acts (1935–37) → cash and carry extended to arms (Nov. 1939) → the Arsenal of Democracy → Lend-Lease (March 1941, outside the course). American factories worked for Britain long before American soldiers fought.",
         beats=[
        "{g7}{g7.1}Sixth idea. The title of the lesson says it: the British resistance, supported by the US. But in 1940 the United States is neutral, by law. "
        "Remember chapter one: the Neutrality Acts. In 1935, an embargo on arms for nations at war. In 1936, a ban on loans to them. "
        "In 1937, the arms embargo made permanent, Americans forbidden to travel on ships of nations at war, "
        "and other goods sold to those nations only for cash, carried away on their own ships: cash and carry.",
        "{g7.2}Then, in November 1939, once war has begun, Roosevelt obtains a new Neutrality Act: the arms embargo is lifted, and cash and carry now applies to weapons. "
        "The democracies can buy American weapons, if they pay in cash and carry them away on their own ships. "
        "The formula favours whoever controls the sea: Britain and France, and after June 1940, Britain alone.",
        "{-g7}{ars}Roosevelt then presents his country as the {!Arsenal of Democracy}Arsenal of Democracy. "
        "Britain could hold out because American factories worked for it long before American soldiers fought.",
        "{ars.1}One example from outside the course, but very useful: the Lend-Lease Act of March 1941. "
        "The United States can now lend or lease war materials to Britain, without immediate payment. That is the end of cash and carry.",
        "{-ars}{et3}So, step by step, America moves towards Britain. {et3.1}1935 to 1937: neutrality, by law. {et3.2}November 1939: cash and carry, for arms too. "
        "{et3.3}Then the Arsenal of Democracy. {et3.4}March 1941: Lend-Lease, outside the course. "
        "{et3.5}And December 1941: the United States is at war.",
    ], vis={
        "g7": dict(type="globe", code="H1", sc=[26, 32]),
        "ars": dict(type="def", cles=["factories", "soldiers"], terme="The Arsenal of Democracy",
                    t="Britain could hold out because American factories worked for it long before American soldiers fought.",
                    etape="Outside the course: the Lend-Lease Act, March 1941 — no immediate payment", x=170, y=200, w=940),
        "et3": dict(type="liste", titre="Step by step towards Britain", items=[
            "1935–1937: the Neutrality Acts", "Nov. 1939: cash and carry for arms", "The “Arsenal of Democracy”",
            "March 1941: Lend-Lease (outside the course)", "Dec. 1941: the United States at war"], x=170, y=120, w=940),
    }),

    # ================================================================ X. idée 7 : décembre 1941
    dict(id="mondiale", chap="December 1941: the war goes global", fond="nuit", humeur="tension",
         retenir="June 1941 Barbarossa, stopped before Moscow in December · 7 Dec. 1941 Pearl Harbor · 11 Dec. Germany and Italy declare war on the US: the war is global, Britain is no longer alone.",
         beats=[
        "{g8}{g8.1}Seventh and last idea. After conquering France, the German army turned east, against the Soviet Union, in June 1941, "
        "{g8.2}until it was abruptly stopped before Moscow, in December 1941. That is episode four.",
        "{g8.3}The same month, on the seventh of December 1941, Japan, one of the Axis powers, bombs the American base of Pearl Harbor, in Hawaii. "
        "The United States immediately declares war on Japan.",
        "{g8.4}And on the eleventh of December, Germany and Italy declare war on the United States. "
        "From then on, the war is fought on every ocean and every continent.",
        "{-g8}{une}Monsieur Ros's slide shows the front page of The Erie Daily Times, on the eleventh of December 1941. Two headlines. "
        "{une.1}U.S. Declares War on Germany, Italy. {une.2}And below: America Lines Up With Britain, Soviet Against Axis In World Struggle.",
        "{-une}{bil2}Look at the words: lines up with Britain. Eighteen months after Dunkirk, {!no longer alone}Britain is no longer alone. "
        "{bil2.1}The bet of Churchill and de Gaulle has paid off: the New World has stepped forth.",
    ], vis={
        "g8": dict(type="globe", code="H3", sc=[26, 30, 31, 33]),
        "une": dict(type="liste", titre="The Erie Daily Times, 11 December 1941", items=[
            "“U.S. Declares War on Germany, Italy”",
            "“America Lines Up With Britain, Soviet Against Axis In World Struggle”"], x=150, y=200, w=980),
        "bil2": dict(type="note", terme="Britain is no longer alone", cles=["bet", "New", "World"],
                     t="December 1941: the war becomes global, and the bet of Churchill and de Gaulle pays off.",
                     etape="“the New World … steps forth to the rescue and the liberation of the old”", x=170, y=200, w=940),
    }),

    # ================================================================ XI. à l'examen : une question de DBQ
    dict(id="dbq", chap="At the exam: a DBQ question", fond="aube", humeur="calme",
         retenir="DBQ a): judgement in the first line · the document in one sentence · strengths (the author, the date, the strategy) · limits (a morale speech, June 1940, the US still neutral, one viewpoint).",
         beats=[
        "{dq}A DBQ question, written for this video. How useful is Churchill's speech of the fourth of June 1940 "
        "for understanding why Britain kept fighting in 1940?",
        "{-dq}{st}Remember the structure of part a). {st.1}Your judgement in the first line: largely, significantly, partly or slightly useful. "
        "{st.2}The document presented in one sentence. {st.3}A paragraph of strengths, with several arguments. "
        "{st.4}And a paragraph of limits, with several arguments.",
        "{-st}{pa2}",
        ("P", 2.0),
        "{-pa2}{m1}Here is a model. {m1.1}The judgement: this speech is significantly useful for understanding why Britain kept fighting, "
        "but it cannot explain, on its own, how Britain held out. {m1.2}The document: a speech by Winston Churchill, prime minister, "
        "before the House of Commons, on the fourth of June 1940, at the end of the Dunkirk evacuation.",
        "{-m1}{fo}The strengths. {fo.1}It comes from the head of government himself: it shows the official resolve to fight on, "
        "if necessary for years, if necessary alone. {fo.2}Its date matters: it is given before the armistice, as France collapses, "
        "so it shows that the choice to fight was made at once. {fo.3}And it reveals the strategy: the Empire, the fleet, "
        "and the hope that the New World would come to the rescue. De Gaulle's appeal makes the same analysis, which confirms it.",
        "{-fo}{li}The limits. {li.1}It is a public speech, meant to keep up morale: it shows determination, not the real military situation. "
        "{li.2}It is given in June: it cannot show what actually saved Britain afterwards, the failure of the Luftwaffe to win control of the air. "
        "{li.3}It hopes for American help, but in 1940 the United States was still neutral, and only sold weapons, through cash and carry. "
        "{li.4}And it gives one point of view, the British government's: cross-check it with another document, such as the slide of the Blitz.",
    ], vis={
        "dq": dict(type="question", t="How useful is Churchill's speech of 4 June 1940 for understanding why Britain kept fighting?"),
        "st": dict(type="liste", titre="DBQ a) · the structure", items=[
            "Judgement in the first line: largely / significantly / partly / slightly useful",
            "The document presented in one sentence", "Strengths: a paragraph, several arguments",
            "Limits: a paragraph, several arguments"], x=150, y=140, w=980),
        "pa2": dict(type="pause", t="Write part a): how useful is Churchill's speech of 4 June 1940 for understanding why Britain kept fighting?",
                    sous="Pause the video, follow the four steps, then play on for a model."),
        "m1": dict(type="liste", titre="A model answer (written for the video)", items=[
            "“Significantly useful … but it cannot explain on its own how Britain held out.”",
            "Churchill, prime minister, House of Commons, 4 June 1940, end of Dunkirk"], x=150, y=170, w=980),
        "fo": dict(type="liste", titre="Strengths", marques=["+", "+", "+"], items=[
            "The head of government: the official resolve, “if necessary alone”",
            "4 June, before the armistice: the choice to fight is made at once",
            "The strategy: Empire, fleet, the New World (confirmed by de Gaulle)"], x=150, y=150, w=980),
        "li": dict(type="liste", titre="Limits", marques=["−", "−", "−", "−"], items=[
            "A public speech for morale, not the military situation",
            "June 1940: cannot show the Luftwaffe's failure in the air",
            "Hopes for US help, but the US is still neutral (cash and carry)",
            "One viewpoint: cross-check with another document"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}In June 1940, Jodl hesitates between a direct attack and a peripheral war; "
        "the Blitz bombs British cities, and about forty-three thousand civilians are killed. "
        "{carte.2}Britain holds because the Luftwaffe never wins control of the air: in December 1940, the invasion is postponed indefinitely. "
        "{carte.3}Two men refuse defeat, Churchill on the fourth of June and de Gaulle on the eighteenth, and both bet on a world war. "
        "{carte.4}And America arms Britain, from cash and carry to the Arsenal of Democracy, until December 1941, when the war becomes global.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: Barbarossa. On the twenty-second of June 1941, Germany invades the Soviet Union, "
        "and a war of annihilation begins in the East.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="BRITAIN ALONE", branches=[
            dict(t="The German attack", items=["Jodl: direct or peripheral", "7 Sept. 1940: the Blitz", "≈ 43,000 civilians (UK)"]),
            dict(t="Why Britain held", items=["no air superiority", "Dec. 1940: invasion off", "Hitler turns east"]),
            dict(t="Two men", items=["Churchill, 4 June 1940", "de Gaulle, 18 June 1940", "a bet on a world war"]),
            dict(t="America", items=["cash and carry for arms (1939)", "Arsenal of Democracy", "Dec. 1941: global war"])]),
        "fin": dict(type="mot", t="Next: Barbarossa", g="Episode 4 · a war of annihilation", y=270, taille=84),
    }),
]

QUIZ = [
    dict(q="In his memorandum of June 1940, what choice did Jodl set out against Britain?",
         r=["A direct attack on England, or a war on the periphery", "An alliance with Britain, or a war with the USSR",
            "A landing first, then air attacks", "A naval blockade of the United States"], ok=0, voir="jo",
         ex="Direct: air and sea offensive, terror bombing, a landing. Peripheral: the Mediterranean and the trade routes."),
    dict(q="Why did the Germans regard the air war as the first step?",
         r=["Any invasion required the defeat of the RAF", "Their army was too weak to fight",
            "The Royal Navy had been destroyed at Dunkirk", "The United States had banned a landing"], ok=0, voir="lo",
         ex="No air superiority over south-east England, no landing: the bombers struck first."),
    dict(q="The course gives 43,000 civilian dead for the Blitz. What should you write in an essay?",
         r=["About 43,000 civilians killed in Britain", "43,000 civilians killed in London alone",
            "43,000 RAF pilots killed", "43,000 German airmen shot down"], ok=0, voir="chif",
         ex="The figure is usually given for the whole UK, about half of the victims in London."),
    dict(q="Why was the invasion of Britain postponed indefinitely in December 1940?",
         r=["The Luftwaffe had failed and Germany turned its forces against the USSR", "Britain had signed an armistice",
            "The United States had declared war on Germany", "Italy refused to take part"], ok=0, voir="ch1",
         ex="December 1940: the first operational order for the invasion of the USSR."),
    dict(q="When did Churchill become prime minister?",
         r=["10 May 1940", "4 June 1940", "18 June 1940", "3 September 1939"], ok=0, voir="wc",
         ex="The day the German attack in the west began; Chamberlain had lost the support of the Commons."),
    dict(q="Which is a DIFFERENCE between the speeches of Churchill and de Gaulle?",
         r=["Churchill spoke before the armistice, de Gaulle after his government had asked for one",
            "Only Churchill counted on the United States", "Only de Gaulle believed in a world war",
            "Both spoke before the House of Commons"], ok=0, voir="dif",
         ex="Both counted on the empires, the fleet and US industry; their position, date, audience and aim differ."),
    dict(q="What did the “cash and carry” Neutrality Act of November 1939 allow?",
         r=["The democracies could buy US weapons if they paid cash and carried them on their own ships",
            "The US could lend weapons without payment", "American soldiers could fight in Europe",
            "Germany could buy American oil"], ok=0, voir="g7",
         ex="Lending without immediate payment is Lend-Lease, March 1941 (outside the course)."),
    dict(q="What happened on 11 December 1941?",
         r=["Germany and Italy declared war on the United States", "Japan bombed Pearl Harbor",
            "Germany invaded the USSR", "The Blitz began"], ok=0, voir="une",
         ex="Pearl Harbor was on 7 December; The Erie Daily Times: “America Lines Up With Britain, Soviet Against Axis”."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H3 · Part I.2, “The British resistance supported by the US”) and Worksheet 2 as written on the site "
    "(the worksheet answers are suggested by the site, not M. Ros's answer key); reminders of chapter 1; animated maps of chapters 1 and 3 (site). "
    "Outside the course: the Lend-Lease Act, Operation Sea Lion, the Battle of Britain. The DBQ question and model answer were written for this video.",
    "Photograph: children of an eastern suburb of London made homeless by a night raid, September 1940 (New Times Paris Bureau Collection, USIA; "
    "US National Archives, 306-NT-3163V; public domain according to its source; Wikimedia Commons file “WWII London Blitz East London.jpg”, "
    "tagged CC BY-SA 2.0 via pingnews.com on Flickr).",
    "Photograph: Winston Churchill, Ottawa, December 1941, by Yousuf Karsh (Library and Archives Canada, Wikimedia Commons, CC BY 2.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
