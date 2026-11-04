"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 4 : Jack entre en scène (PDF de travail, p. 15-22).

Du retour de Maggie (« The fox is back ») jusqu'au branchement de la batterie, juste avant la musique (p. 22).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_4. Citations courtes, à fin d'analyse ;
ce qui ne vient pas du texte est dit comme tel. Coquilles du PDF non reproduites dans les citations
(p. 19 : « 00 what's the word? » lu comme un tiret).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-4"
NOTION = "Dancing at Lughnasa"
NUM = 4
TITRE = "Jack comes in"
SUIVANT = "Part 5 · The dance"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Okawa": "Oh-kah-wa", "Ardstraw": "Ard-straw", "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture4", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{q4}A woman comes in from the garden with her hands cupped around something fragile. "
        "She opens them, and her eyes follow something up into the sky.",
        "{-q4}{trois4}Part four. Kate has just cancelled the harvest dance. Now the house is shaken three times: "
        "by a fire in the hills, by Father Jack, and by an old friend's name.",
        ("P", 0.3),
        "{-trois4}{titre4}",
        ("P", 3.2),
    ], vis={
        "q4": dict(type="question", t="Did you see it?"),
        "trois4": dict(type="mot", t="Three shocks", g="a fire in the hills · Father Jack · an old friend's name", y=270, taille=88),
        "titre4": dict(type="titre", sur="Dancing at Lughnasa · Part 4", t="Jack comes in",
                       sous="Act One · pages 15 – 22"),
    }),

    # ------------------------------------------------------------------ I. l'oiseau
    dict(id="oiseau", chap="The bird in Maggie's hands", fond="aube", humeur="lumiere",
         retenir="Maggie's invisible bird: “one quick glimpse – that's all you ever get”. A game that hides a regret.", beats=[
        "{retour}Page fifteen. Silence after Kate's ban. {retour.1}Maggie comes back from the hens: the fox is back. "
        "{retour.2}Her hands are cupped around something fragile. She teases Michael: say please three times… in Swahili. "
        "{retour.3}Then she opens her hands, and her eyes follow something up into the sky.",
        "Was it a bird? Maggie answers:",
        "{-retour}",
        ("C", "Trouble is – just one quick glimpse – that's all you ever get. And if you miss that ...", "c_glimpse", {"voix": "F"}),
        "On the surface, a game with a child. But listen to the dashes, and the sentence that breaks off. "
        "Keep this line in mind: by the end of this part, it sounds like Maggie's own life.",
        "{-c_glimpse}{mind}And what was it? It was all in your mind. The bird may never have existed: "
        "in a memory play, a little joke about the whole play.",
        "{-mind}{menage}Then routine takes over. {menage.1}Kate unpacks the shopping: tea, soap, jelly. "
        "{menage.2}Rose's white rooster has bitten Maggie. "
        "{menage.3}And Kate has brought a new battery for Marconi.",
        "{-menage}{okawa}One joke matters: Jack sometimes calls Maggie Okawa, the name of his house boy in Africa. "
        "Jack is mixing up his two worlds.",
    ], vis={
        "retour": dict(type="liste", titre="Maggie comes back · pages 15 – 16", items=[
            "“The fox is back”: a hole in the henhouse door",
            "Hands cupped around something fragile",
            "She opens them: an imaginary flight to the sky"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_glimpse": dict(type="cit", a="Maggie", o="p. 16", x=170, y=200, w=940),
        "mind": dict(type="mot", t="“It was all in your mind.”", g="Maggie to Michael · p. 16 · was there ever a bird?", y=250, taille=80),
        "menage": dict(type="liste", titre="Back to the routine · pages 16 – 17", items=[
            "Kate unpacks: tea… soap… Indian meal… jelly…",
            "Rose's white rooster attacked Maggie",
            "A new battery for Marconi"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "okawa": dict(type="note", cles=["Okawa", "house"], terme="Okawa · p. 17",
                      t="Jack calls Maggie “Okawa”: the name of his house boy in Africa.",
                      etape="Jack's two worlds are already mixed up.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. le feu des collines
    dict(id="collines", chap="Fire in the back hills", fond="nuit", humeur="tension",
         retenir="Rose describes the pagan Lughnasa rite; Kate calls it the work of “savages” in “a Catholic home”.", beats=[
        "{tab_hil}{sw}Then Kate brings bad news. {sw.1}The young Sweeney boy from the back hills was anointed last night: "
        "the last rites. {sw.2}Not an inch of his body isn't burned. "
        "{sw.3}What happened? Some silly prank, says Kate. She knows no more.",
        "{-sw}{rose}And then Rose, the sister the others treat like a child, speaks up, quietly, resolutely: "
        "it was the Festival of Lughnasa.",
        "{-rose}",
        ("C", "First they light a bonfire beside a spring well. Then they dance round it. Then they drive their cattle through the flames "
              "to banish the devil out of them.", "c_rite", {"voix": "F"}),
        "First, then, then: three short sentences, as simple as a ritual. Fire, dance, purification. "
        "This year the crowd was drunk, and young Sweeney went up like a torch.",
        "{-c_rite}{rite}Notice who knows this: not Kate the schoolteacher, but Rose. The pagan world is closer than Kate admits. "
        "And dancing at harvest time is exactly what the sisters wanted, minutes ago.",
        "{-rite}{sav}Kate explodes, almost shouting. Savages! She knows those people; she has taught them.",
        "{-sav}",
        ("C", "It's a sorry day to hear talk like that in a Christian home, a Catholic home!", "c_home", {"voix": "F"}),
        "A Christian home, a Catholic home: the repetition builds a wall of words around the house. But her anger looks a lot like fear.",
        "{-c_home}{kc}Rose does not give in: that's what happened, I'm telling you. "
        "{kc.1}Kate has the authority, but not the truth. "
        "{-kc}{-tab_hil}{poule}And Maggie breaks the tension, as always, with a joke about the hens.",
    ], vis={
        "tab_hil": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.2, .4, .5], a=[1.0, .5, .5],
                        legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "sw": dict(type="liste", titre="The Sweeney boy · pages 17 – 18", items=[
            "Anointed last night: the last rites",
            "“Not an inch of his body that isn't burned”",
            "Kate: “Some silly prank up in the hills”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "rose": dict(type="def", cles=["pagan", "harvest"], terme="Rose speaks · p. 18",
                     t="“Quietly, resolutely”: Rose explains what really happened in the back hills.",
                     etape="The Festival of Lughnasa: a pagan harvest rite.", x=170, y=200, w=940),
        "c_rite": dict(type="cit", a="Rose", o="p. 18", x=170, y=180, w=940),
        "rite": dict(type="note", cles=["Rose", "closer"], terme="The back hills · p. 18",
                     t="Fire, dance, purification: the pagan rite is told by Rose, not by Kate.",
                     etape="The same impulse as the harvest dance the sisters wanted.", x=170, y=200, w=940),
        "sav": dict(type="mot", t="“Savages!”", g="Kate · “very angry, almost shouting” · p. 18", y=250, taille=96),
        "c_home": dict(type="cit", a="Kate", o="p. 18", x=170, y=200, w=940),
        "kc": dict(type="cols", g="Rose", gq="“That's what happened. I'm telling you.”", d="Kate",
                   dq="“savages”, “a Catholic home”", vs="≠", repere="pagan / Christian"),
        "poule": dict(type="mot", t="Tchook-tchook-tchook!", g="Maggie's jokes: a way out of every quarrel", y=260, taille=84),
    }),

    # ------------------------------------------------------------------ III. Jack entre
    dict(id="jack4", chap="Father Jack enters", fond="nuit", humeur="mystere",
         retenir="Jack arrives with no collar, no accent, no words: the priest is not what Kate needs him to be.", beats=[
        "{sd}At that very moment, Father Jack walks in. Read the stage direction. "
        "{sd.1}Frail, older than his fifty-three years. {sd.2}A heavy coat, trousers too short… "
        "{sd.3}and no clerical collar. {sd.4}He shuffles, uneasy, confused, with scarcely any Irish accent.",
        "{-sd}{ironie}Look at the timing. Kate has just shouted: a Catholic home! And in comes the priest, without his collar. "
        "This juxtaposition creates dramatic irony: the family's pillar of faith is already slipping.",
        "{-ironie}{dlg}{dlg.1}He apologises: the wrong apartment. He cannot find his own bedroom. "
        "{dlg.2}He calls Kate Agnes. {dlg.3}It's Kate, she corrects him. Then:",
        "{-dlg}",
        ("C", "I don't remember the – the architecture? – the planning? – what's the word? – the lay-out!", "c_layout"),
        "He hunts for a simple word: big formal ones first, then the plain one. "
        "English escapes him, and so does the house he grew up in.",
        "{-c_layout}{welcome}{welcome.1}Kate promises a public welcome: flags, bands, speeches. "
        "{welcome.2}Jack asks: why would they do this? {welcome.3}He feels the climate so cold, and shuffles off.",
        "{-welcome}{gene}A sense of unease, almost embarrassment. Kate, briskly: he'll be fine. "
        "But the opening told us: Jack came home to die.",
    ], vis={
        "sd": dict(type="liste", titre="Stage direction · pages 18 – 19", items=[
            "Frail, older than his fifty-three years",
            "Heavy grey coat, trousers too short, thick socks",
            "No clerical collar",
            "Shuffles · uneasy, confused · scarcely any Irish accent"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "ironie": dict(type="cols", g="Kate", gq="“a Christian home, a Catholic home!”", d="Jack",
                       dq="no collar, no accent, confused", vs="→", repere="juxtaposition · dramatic irony"),
        "dlg": dict(type="dialogue", lignes=[
            "JACK. … the wrong apartment … forgive me …",
            "JACK. You walked to the village to buy stores, Agnes?",
            "KATE. It's Kate."], src="page 19", x=300, y=200, w=680),
        "c_layout": dict(type="cit", a="Jack", o="p. 19", x=170, y=200, w=940),
        "welcome": dict(type="liste", titre="Kate's plan, Jack's answer · p. 19", items=[
            "Kate: “flags, bands, speeches, everything!”",
            "Jack: “Why would they do this?”",
            "Jack: “I feel the climate so cold”"], marques=["K", "J", "J"], x=150, y=180, w=980),
        "gene": dict(type="note", cles=["unease", "fine"], terme="After Jack leaves · pp. 19 – 20",
                     t="“A sense of unease, almost embarrassment.” Kate: “he'll be fine.”",
                     etape="Dramatic irony: the opening told us he came home to die.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. Bernie O'Donnell
    dict(id="bernie", chap="Bernie O'Donnell", fond="aube", humeur="calme",
         retenir="Bernie's return wakes Maggie's memory of Ardstraw: the boy she loved, the chance she missed.", beats=[
        "{tab_gle4}{bern}Kate moves on to happier news. {bern.1}Maggie's old pal, Bernie O'Donnell, is home from London "
        "after twenty years. {bern.2}Gorgeous, says Kate: a film star. "
        "{bern.3}With blond twin girls: their father is from Stockholm.",
        "{-bern}{-tab_gle4}{fen}Maggie says almost nothing. She goes to the window, so that the others cannot see her face, "
        "her hands covered with flour.",
        "{-fen}{wise}Bernie asked if none of them were thinking of getting married. And weren't we wise, says Kate. "
        "A joke, from five unmarried sisters. Not as light as it sounds.",
        "{-wise}{ard}Then Maggie tells her own story. {ard.1}At sixteen, at the beginning of August, "
        "she and Bernie slipped out to a dance in Ardstraw. "
        "{ard.2}Maggie was keen on Brian McGuinness. But he was crazy about Bernie. "
        "{ard.3}At the end of the night: a competition, the Best Military Two-step.",
        "{-ard}",
        ("C", "And they were just so beautiful together, so stylish; you couldn't take your eyes off them.", "c_beau", {"voix": "F"}),
        "Maggie admires Bernie, dancing with the boy Maggie loved. The judges, probably blind drunk, put them third. "
        "And Brian left for Australia.",
        "{-c_beau}{fair}It wasn't fair, she repeats. On the surface, a dance contest. "
        "In the subtext, her whole life: the one quick glimpse she missed.",
        "{-fair}{tab_rad4}{fin4}{fin4.1}Maggie stands motionless at the window, seeing nothing. "
        "{fin4.2}The others drift back to their tasks. {fin4.3}And Chris connects the battery. "
        "Marconi is ready. In the next part, the music starts.",
    ], vis={
        "tab_gle4": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "bern": dict(type="liste", titre="Kate's news · page 20", items=[
            "Bernie O'Donnell, home from London after twenty years",
            "“Absolutely gorgeous” · “a film star!”",
            "Twin girls, pure blond: the father is from Stockholm"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "fen": dict(type="note", cles=["window", "face"], terme="Stage direction · p. 20",
                    t="Maggie goes to the window so that the others cannot see her face.",
                    etape="What she feels stays hidden: this is subtext.", x=170, y=200, w=940),
        "wise": dict(type="mot", t="“and weren't we wise!”", g="Kate · p. 20 · a joke from five unmarried sisters", y=250, taille=80),
        "ard": dict(type="liste", titre="Maggie remembers Ardstraw · pages 21 – 22", items=[
            "Sixteen, the beginning of August: a dance in Ardstraw",
            "Brian McGuinness… “crazy about Bernie”",
            "The Best Military Two-step competition"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_beau": dict(type="cit", a="Maggie", o="p. 22", x=170, y=200, w=940),
        "fair": dict(type="mot", t="“it wasn't fair at all”", g="a dance contest… or a life?", y=250, taille=84),
        "tab_rad4": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                         legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "fin4": dict(type="liste", titre="Stage direction · page 22", items=[
            "Maggie, motionless at the window, “seeing nothing”",
            "The others drift back to their tasks",
            "Chris connects the battery: Marconi is ready"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse4", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Maggie's mask, pagan against Christian, Jack's broken words, memory: four ideas for your essay.", beats=[
        "{b1}Now the analysis. Four ideas. "
        "{b1.1}One: Maggie's mask. The joker of the house hides a wound. "
        "The bird's one quick glimpse foreshadows Ardstraw, and her silence at the window says more than any line.",
        "{-b1}{b2}{b2.1}Two: pagan against Christian. Rose's bonfire mirrors the harvest dance the sisters wanted. "
        "Kate shouts back. And Kate tells us the parish priest can hardly look her in the eye since Jack came home. Her authority is cracking.",
        "{-b2}{b3}{b3.1}Three: Jack, the broken pillar. No collar, no accent, no words. "
        "As we learn later, Africa has changed his faith itself. Here, it is only foreshadowed.",
        "{-b3}{b4}{b4.1}Four: memory. Bernie remembers everyone, Jack almost nothing, Maggie too much. "
        "And it was all in your mind: a perfect line on a memory play.",
        "{-b4}{carte4}For your essay, this part supports: {carte4.1}lost love and missed chances. "
        "{carte4.2}Pagan against Christian. {carte4.3}Jack and the failure of language. {carte4.4}Memory and what it hides.",
    ], vis={
        "b1": dict(type="note", cles=["mask", "foreshadows"], terme="1 · Maggie's mask",
                   t="The joker hides a wound: the bird's “one quick glimpse” foreshadows Ardstraw.",
                   etape="Subtext: her silence at the window says it all.", x=170, y=200, w=940),
        "b2": dict(type="note", cles=["pagan", "crack"], terme="2 · Pagan / Christian",
                   t="Rose's bonfire against Kate's “savages” and “a Catholic home”.",
                   etape="Kate shouts: her authority is starting to crack.", x=170, y=200, w=940),
        "b3": dict(type="note", cles=["collar", "words"], terme="3 · Jack, a broken pillar",
                   t="No collar, no accent, no words: “what's the word? – the lay-out!”",
                   etape="Foreshadowing: Africa has changed him.", x=170, y=200, w=940),
        "b4": dict(type="note", cles=["remembers", "mind"], terme="4 · Memory",
                   t="Bernie remembers everyone, Jack almost nothing, Maggie too much.",
                   etape="“It was all in your mind”: a memory play in one line.", x=170, y=200, w=940),
        "carte4": dict(type="carte", centre="PART 4", branches=[
            dict(t="Missed chances", items=["“one quick glimpse”", "Brian and Bernie", "“it wasn't fair”"]),
            dict(t="Pagan / Christian", items=["Rose's bonfire", "“savages”", "“a Catholic home”"]),
            dict(t="Jack", items=["no collar, no accent", "“the lay-out!”", "“he'll be fine”: irony"]),
            dict(t="Memory", items=["“all in your mind”", "Bernie remembers all", "Jack forgets"])]),
    }),
]

QUIZ = [
    dict(q="What does Maggie say after the boy asks what flew out of her hands?",
         r=["“It was all in your mind”", "“It was the fox”", "“It was Jack's parrot”", "“It was a white rooster”"], ok=0,
         voir="mind", ex="The bird may never have existed: “It was all in your mind. Now we're quits.” A small joke about memory itself."),
    dict(q="Why is the “one quick glimpse” line important?",
         r=["It foreshadows Maggie's own missed chance with Brian McGuinness", "It announces Jack's death",
            "It explains the Lughnasa rite", "It is Kate's warning to Rose"], ok=0, voir="c_glimpse",
         ex="“Trouble is – just one quick glimpse – that's all you ever get.” By the end of the part, it sounds like Maggie's life."),
    dict(q="Who explains what happened to the Sweeney boy?",
         r=["Rose, quietly and resolutely", "Kate, after meeting the parish priest", "Father Jack", "Chris"], ok=0,
         voir="c_rite", ex="Kate calls it “some silly prank”; Rose describes the bonfire, the dance and the cattle driven through the flames."),
    dict(q="How does Kate react to Rose's account?",
         r=["She calls the hill people “savages” and defends “a Catholic home”", "She laughs and changes the subject",
            "She agrees and wants to go to the bonfire", "She asks Jack to bless the house"], ok=0, voir="c_home",
         ex="“Very angry, almost shouting”: “It's a sorry day to hear talk like that in a Christian home, a Catholic home!”"),
    dict(q="What is missing from Father Jack's appearance in the stage direction?",
         r=["His clerical collar", "His hat", "His boots", "His coat"], ok=0, voir="sd",
         ex="No clerical collar, scarcely any Irish accent: he enters just after Kate's “Catholic home”, a juxtaposition full of dramatic irony."),
    dict(q="Why does Maggie go to the window when Kate talks about Bernie?",
         r=["So that the others cannot see her face", "To look for the fox", "To call the hens", "To see if Gerry is coming"], ok=0,
         voir="fen", ex="Her feelings stay hidden (subtext); the part ends with her “staring out of the window, seeing nothing”."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
