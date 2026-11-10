"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 4 : Jack entre en scène (PDF de travail, p. 15-22).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu : cuisine, jardin), en suivant les didascalies pas à pas ;
les répliques courtes s'affichent en bulles et sont lues par les voix des personnages ; l'enfant n'est jamais vu
(emplacement en pointillé près des cerfs-volants), Michael adulte dit ses répliques depuis le bord du plateau.
Puis quatre répliques expliquées et l'analyse (inchangée).

Du silence qui suit l'interdiction de Kate (p. 15) jusqu'au récit d'Ardstraw, Maggie à la fenêtre (p. 22) ;
la partie 5 commence à la didascalie « MAGGIE stands motionless… ». Même chaîne que la partie 1 :
outils/serie-philo/generer.py dal_4. Citations courtes, à fin d'analyse ; ce qui ne vient pas du texte est dit comme tel.
Coquilles du PDF non reproduites dans les citations (p. 19 : « 00 what's the word? » lu comme un tiret ;
« I beg our pardon » : seule la suite « the wrong apartment » est citée).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-4"
NOTION = "Dancing at Lughnasa"
NUM = 4
TITRE = "Jack comes in"
SUIVANT = "Part 5 · The dance"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Okawa": "Oh-kah-wa", "Ardstraw": "Ard-straw", "Mundy": "Mundy",
                 "Tchook": "Chook", "McGuinness": "Mac-Guinness"}

# positions de départ (cuisine, p. 15) : Kate vient d'interdire le bal ; Agnes et Rose à leur tricot, Chris au repassage
DEPART = dict(pos={"Kate": [480, 410], "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Maggie": "off", "Michael": "off"},
              act={"Kate": "debout", "Agnes": "assis", "Rose": "assis", "Chris": "repasse"})

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture4", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{q4}A woman walks into the garden with her hands cupped around something fragile. "
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

    # ------------------------------------------------------------------ I. l'oiseau (jardin)
    dict(id="oiseau", chap="The bird in Maggie's hands", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page fifteen. Kate has just said no: the Mundy girls are going to no harvest dance. Silence.",
        "{jeu1.1}Maggie comes back to the garden from the back of the house, the hen bucket on her arm, "
        "her hands cupped as if she were holding something fragile. {jeu1.2}She goes to the kite materials, "
        "where the boy is working. We never see the boy: the adult Michael, at the edge of the stage, speaks his lines.",
        ("C", "The fox is back.", "jeu1.3", {"voix": "F"}),
        ("C", "What's that you have in your hands?", "jeu1.4"),
        "{jeu1.5}Something I found, says Maggie. And she makes him work for it.",
        ("C", "Say please three times.", "jeu1.6", {"voix": "F"}),
        ("C", "Please – please – please.", "jeu1.7"),
        ("C", "In Swahili.", "jeu1.8", {"voix": "F"}),
        "{jeu1.9}Then she crouches down beside him.",
        ("C", "Now cub, put your ear over here. Listen. Shhh. D'you hear it?", "jeu1.10", {"voix": "F"}),
        "{jeu1.11}Suddenly she opens her hands, and her eyes follow the rapid and imaginary flight of something "
        "up to the sky and out of sight.",
        ("P", 1.2),
        ("C", "Was it a bird?", "jeu1.12"),
        "{jeu1.13}The colours are so beautiful, says Maggie. And she gets to her feet.",
        ("C", "Trouble is – just one quick glimpse – that's all you ever get. And if you miss that ...", "jeu1.14", {"voix": "F"}),
        "{jeu1.15}She moves off towards the back door of the kitchen. What was it, Aunt Maggie?",
        ("C", "Don't you know what it was? It was all in your mind. Now we're quits.", "jeu1.16", {"voix": "F"}),
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris", "Michael"], etats=[
            dict(pos=DEPART["pos"], act=DEPART["act"], objets={"kites": "kites", "garcon": [780, 460]}, cam="tout",
                 note="“The matter's over. I don't want it mentioned again.” (Kate, p. 15)"),
            dict(pos={"Maggie": [960, 250]}, note="“her hands are cupped as if she were holding something fragile” (p. 15)"),
            dict(pos={"Maggie": [845, 392], "Michael": "michael"}, duree=3.0, note="She goes to the kite materials."),
            dict(dit=["Maggie", "The fox is back."]),
            dict(dit=["Michael", "What's that you have in your hands?"], note="Michael speaks the boy's lines."),
            dict(note="“Sitting very still at the foot of the holly tree.” (p. 15)"),
            dict(dit=["Maggie", "Say please three times."]),
            dict(dit=["Michael", "Please – please – please."]),
            dict(dit=["Maggie", "In Swahili."]),
            dict(pos={"Maggie": [850, 420]}, act={"Maggie": "agenouille"}, note="“Crouching down beside him” (p. 15)"),
            dict(dit=["Maggie", "Now cub, put your ear over here. Listen. Shhh. D'you hear it?"]),
            dict(note="“the rapid and imaginary flight of something up to the sky” (p. 16)"),
            dict(dit=["Michael", "Was it a bird?"]),
            dict(act={"Maggie": "debout"}, note="“The colours are so beautiful.” (She gets to her feet.)"),
            dict(dit=["Maggie", "Trouble is – just one quick glimpse – that's all you ever get. And if you miss that ..."]),
            dict(pos={"Maggie": [585, 330]}, duree=3.0, note="She moves off towards the back door of the kitchen."),
            dict(dit=["Maggie", "Don't you know what it was? It was all in your mind. Now we're quits."]),
        ]),
    }),

    # ------------------------------------------------------------------ II. les courses (cuisine)
    dict(id="courses", chap="Back to the routine", fond="nuit", humeur="calme", beats=[
        "{jeu2}Back in the kitchen. Kate unpacks the shopping: tea, soap, Indian meal, jelly. "
        "{jeu2.1}Maggie, pecked by Rose's white rooster, washes her hands and begins baking soda bread.",
        "{jeu2.2}Then Chris remembers a name.",
        ("C", "Doesn't Jack sometimes call you Okawa, too, Maggie?", "jeu2.3", {"voix": "F"}),
        ("C", "Okawa was his house boy, Kate says.", "jeu2.4", {"voix": "F"}),
        ("C", "Dammit. I thought it was Swahili for gorgeous.", "jeu2.5", {"voix": "F"}),
        "{jeu2.6}And the battery, says Kate. {jeu2.7}Chris takes it, and leaves it beside Marconi.",
        "{jeu2.8}Kate has met the parish priest.",
        ("C", "But ever since Father Jack came home he can hardly look me in the eye.", "jeu2.9", {"voix": "F"}),
        ("C", "That's because you keep winking at him, Kate.", "jeu2.10", {"voix": "F"}),
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Kate": "buffet", "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Maggie": [585, 330]},
                 act={"Kate": "range", "Agnes": "assis", "Rose": "assis", "Chris": "repasse", "Maggie": "debout"},
                 objets={"kites": "kites", "garcon": [780, 460]}, note="“Tea…soap…Indian meal…jelly…” (Kate, unpacking, p. 16)"),
            dict(pos={"Maggie": [495, 335]}, act={"Maggie": "repasse"}, note="(MAGGIE washes her hands and begins baking.)"),
            dict(note="“Look at the lump he took out of my arm.” (Maggie)"),
            dict(dit=["Chris", "Doesn't Jack sometimes call you Okawa, too, Maggie?"], note="(p. 17)"),
            dict(dit=["Chris", "Okawa was his house boy, Kate says."]),
            dict(dit=["Maggie", "Dammit. I thought it was Swahili for gorgeous."]),
            dict(note="“And the battery.” (Kate)"),
            dict(pos={"Chris": "radio"}, act={"Chris": "debout"}, note="Chris leaves the battery beside Marconi."),
            dict(pos={"Chris": "table"}, act={"Chris": "repasse"}, note="“I met the parish priest.”"),
            dict(dit=["Kate", "But ever since Father Jack came home he can hardly look me in the eye."]),
            dict(dit=["Maggie", "That's because you keep winking at him, Kate."]),
        ]),
    }),

    # ------------------------------------------------------------------ III. le feu des collines
    dict(id="collines", chap="Fire in the back hills", fond="nuit", humeur="tension", beats=[
        "{jeu3}Then bad news. The young Sweeney boy from the back hills was anointed last night: "
        "the last rites, for someone dying.",
        ("C", "Not an inch of his body that isn't burned.", "jeu3.1", {"voix": "F"}),
        "{jeu3.2}Some silly prank up in the hills, says Kate. She knows no more. "
        "{jeu3.3}And then Rose speaks, quietly, resolutely. It was the first night of the Festival of Lughnasa.",
        ("C", "First they light a bonfire beside a spring well. Then they dance round it.", "jeu3.4", {"voix": "F"}),
        ("C", "Then they drive their cattle through the flames to banish the devil out of them.", "jeu3.5", {"voix": "F"}),
        "{jeu3.6}This year, the crowd was off their heads with drink, and young Sweeney went up like a torch.",
        "{jeu3.7}Kate is very angry, almost shouting.",
        ("C", "And they're savages! I know those people from the back hills! I've taught them!", "jeu3.8", {"voix": "F"}),
        ("C", "It's a sorry day to hear talk like that in a Christian home, a Catholic home!", "jeu3.9", {"voix": "F"}),
        ("C", "That's what happened. I'm telling you.", "jeu3.10", {"voix": "F"}),
        "{jeu3.11}Pause. And Maggie breaks the tension, as always, calling imaginary hens: tchook, tchook, tchook…",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Kate": "buffet", "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Maggie": [495, 335]},
                 act={"Kate": "range", "Agnes": "assis", "Rose": "assis", "Chris": "repasse", "Maggie": "repasse"},
                 objets={"kites": "kites", "garcon": [780, 460]},
                 note="“The word's not good on that young Sweeney boy from the back hills.” (p. 17)"),
            dict(dit=["Kate", "Not an inch of his body that isn't burned."], act={"Kate": "debout"}),
            dict(note="“Some silly prank up in the hills.” (Kate, p. 18)"),
            dict(note="ROSE (Quietly, resolutely.)"),
            dict(dit=["Rose", "First they light a bonfire beside a spring well. Then they dance round it."]),
            dict(dit=["Rose", "Then they drive their cattle through the flames to banish the devil out of them."]),
            dict(note="“young Sweeney's trousers caught fire and he went up like a torch” (Rose)"),
            dict(note="KATE (Very angry, almost shouting.)"),
            dict(dit=["Kate", "And they're savages! I know those people from the back hills! I've taught them!"]),
            dict(dit=["Kate", "It's a sorry day to hear talk like that in a Christian home, a Catholic home!"]),
            dict(dit=["Rose", "That's what happened. I'm telling you."], note="ROSE (Quietly, resolutely.)"),
            dict(note="“a wee house boy to feed the hens: ‘Tchook-tchook-tchook…’” (Maggie, p. 18)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. Jack entre
    dict(id="jack4", chap="Father Jack enters", fond="nuit", humeur="mystere", beats=[
        "{jeu4}At that very moment, Father Jack enters by the back door. He looks frail, older than his fifty-three years. "
        "Broad-brimmed black hat, heavy grey top coat, trousers well short of his ankles. And no clerical collar.",
        "{jeu4.1}He shuffles quickly, his hands behind his back, uneasy, confused, with scarcely any Irish accent.",
        ("C", "… the wrong apartment … forgive me …", "jeu4.2"),
        "{jeu4.3}He expected to enter his bedroom. He has lost his handkerchief, and Chris takes one from the ironing pile.",
        ("C", "I don't remember the – the architecture? – the planning? – what's the word? – the lay-out!", "jeu4.4"),
        "{jeu4.5}Then he turns to Kate.",
        ("C", "You walked to the village to buy stores, Agnes?", "jeu4.6"),
        ("C", "It's Kate. And dozens of people were asking for you.", "jeu4.7", {"voix": "F"}),
        "{jeu4.8}When he is stronger, Kate promises, there will be a great public welcome: flags, bands, speeches, everything!",
        ("C", "Why would they do this?", "jeu4.9"),
        ("C", "Perhaps … I feel the climate so cold … if you'll forgive me …", "jeu4.10"),
        "{jeu4.11}Why don't you lie down for a while, says Agnes. {jeu4.12}And he shuffles off.",
        ("P", 1.2),
        "{jeu4.13}Pause. A sense of unease, almost embarrassment. Kate, briskly: it will be a slow process, but he'll be fine.",
    ], vis={
        "jeu4": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack"], etats=[
            dict(pos={"Kate": "buffet", "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Maggie": [495, 335],
                      "Jack": [640, 300]},
                 act={"Kate": "debout", "Agnes": "assis", "Rose": "assis", "Chris": "repasse", "Maggie": "repasse", "Jack": "debout"},
                 objets={"kites": "kites", "garcon": [780, 460]}, note="“Heavy grey top coat… No clerical collar.” (p. 18)"),
            dict(pos={"Jack": [565, 290]}, duree=2.0, note="“He seems uneasy, confused.” (p. 19)"),
            dict(dit=["Jack", "… the wrong apartment … forgive me …"]),
            dict(note="“Here's a handkerchief.” (Chris, taking one from the ironing pile)"),
            dict(dit=["Jack", "I don't remember the – the architecture? – the planning? – what's the word? – the lay-out!"]),
            dict(note="“I thought the front door was there.” (To KATE.)"),
            dict(dit=["Jack", "You walked to the village to buy stores, Agnes?"]),
            dict(dit=["Kate", "It's Kate. And dozens of people were asking for you."]),
            dict(note="“flags, bands, speeches, everything!” (Kate)"),
            dict(dit=["Jack", "Why would they do this?"]),
            dict(dit=["Jack", "Perhaps … I feel the climate so cold … if you'll forgive me …"]),
            dict(note="“Why don't you lie down for a while?” (Agnes)"),
            dict(pos={"Jack": "arriere"}, duree=3.0, note="(He shuffles off.)"),
            dict(pos={"Jack": "off"}, note="“Pause. A sense of unease, almost embarrassment.” (p. 19)"),
        ]),
    }),

    # ------------------------------------------------------------------ V. Bernie O'Donnell
    dict(id="bernie", chap="Bernie O'Donnell", fond="nuit", humeur="calme", beats=[
        "{jeu5}Page twenty. And wait till you hear, says Kate, who she met in the post office!",
        ("C", "You'll never believe it – your old pal, Bernie O'Donnell! Home from London!", "jeu5.1", {"voix": "F"}),
        "{jeu5.2}First time back in twenty years. Absolutely gorgeous, a film star, with twin girls, pure blond: "
        "their father is from Stockholm.",
        ("C", "Bernie O'Donnell … oh my goodness …", "jeu5.3", {"voix": "F"}),
        "{jeu5.4}Maggie goes to the window and looks out, so that the others cannot see her face. "
        "She holds her hands, covered with flour, out from her body.",
        ("C", "Were none of us thinking of getting married? – and weren't we wise!", "jeu5.5", {"voix": "F"}),
        "{jeu5.6}Bernie asked specifically for Maggie: was she as light-hearted as ever? Pause.",
        ("C", "You've got some flour on your nose, Maggie.", "jeu5.7", {"voix": "F"}),
        "{jeu5.8}And Maggie, still at the window, tells a story. We do not see it: we only hear it. "
        "At sixteen, at the beginning of August, she and Bernie slipped out to a dance in Ardstraw. "
        "{jeu5.9}Maggie was keen on Brian McGuinness, but of course he was crazy about Bernie. "
        "{jeu5.10}At the end of the night came a competition, the Best Military Two-step.",
        ("C", "And they were just so beautiful together, so stylish; you couldn't take your eyes off them.", "jeu5.11", {"voix": "F"}),
        "{jeu5.12}The judges, probably blind drunk, put them third. And the next thing Maggie heard, Brian had left for Australia.",
        ("C", "I know it wasn't fair – it wasn't fair at all.", "jeu5.13", {"voix": "F"}),
        "{jeu5.14}Maggie stands at the window. Part five begins exactly here.",
    ], vis={
        "jeu5": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Kate": "buffet", "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Maggie": [495, 335]},
                 act={"Kate": "range", "Agnes": "assis", "Rose": "assis", "Chris": "repasse", "Maggie": "repasse"},
                 objets={"kites": "kites", "garcon": [780, 460]}, note="“Who did I meet in the post office!” (Kate, p. 20)"),
            dict(dit=["Kate", "You'll never believe it – your old pal, Bernie O'Donnell! Home from London!"], act={"Kate": "debout"}),
            dict(note="“Absolutely gorgeous… a film star!” (Kate)"),
            dict(dit=["Maggie", "Bernie O'Donnell … oh my goodness …"], act={"Maggie": "debout"}),
            dict(pos={"Maggie": "fenetre"}, duree=2.5, note="“so that the others cannot see her face” (p. 20)"),
            dict(note="“Were none of us thinking of getting married? – and weren't we wise!” (Kate)"),
            dict(note="“were you as light-hearted as ever?” (p. 21)"),
            dict(note="“You've got some flour on your nose, Maggie.” (Chris, after a pause)"),
            dict(note="Maggie remembers (told, not shown): Ardstraw, at sixteen."),
            dict(note="Brian McGuinness, “crazy about Bernie” (told, not shown)"),
            dict(note="“the Best Military Two-step” (p. 22, told, not shown)"),
            dict(dit=["Maggie", "And they were just so beautiful together, so stylish; you couldn't take your eyes off them."]),
            dict(note="Third place; Brian left for Australia (told, not shown)."),
            dict(dit=["Maggie", "I know it wasn't fair – it wasn't fair at all."]),
            dict(act={"Maggie": "fige"}, note="Maggie, at the window (p. 22)."),
        ]),
    }),

    # ------------------------------------------------------------------ VI. répliques à connaître
    dict(id="repliques4", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="Maggie's “one quick glimpse”, Rose's rite, Kate's “Catholic home”, Jack's lost word.", beats=[
        "{quatre4}Four lines from this part are worth knowing by heart.",
        "{-quatre4}First, Maggie and the bird.",
        ("C", "Trouble is – just one quick glimpse – that's all you ever get. And if you miss that ...", "c_glimpse", {"voix": "F"}),
        "{-c_glimpse}{glimpse}On the surface, a game with a child. But listen to the dashes, and the sentence that breaks off. "
        "By the end of this part, it sounds like Maggie's own life.",
        "{-glimpse}Then Rose.",
        ("C", "First they light a bonfire beside a spring well. Then they dance round it.", "c_rite", {"voix": "F"}),
        "{-c_rite}{rite}First, then: short sentences, as simple as a ritual. And notice who knows this: "
        "not Kate the schoolteacher, but Rose. The pagan world is closer than Kate admits.",
        "{-rite}Then Kate.",
        ("C", "It's a sorry day to hear talk like that in a Christian home, a Catholic home!", "c_home", {"voix": "F"}),
        "{-c_home}{home}A Christian home, a Catholic home: the repetition builds a wall of words around the house. "
        "But her anger looks a lot like fear.",
        "{-home}And Jack.",
        ("C", "I don't remember the – the architecture? – the planning? – what's the word? – the lay-out!", "c_layout"),
        "{-c_layout}{layout}He hunts for a simple word: big formal ones first, then the plain one. "
        "And he arrives just after Kate's Catholic home, without his collar: an ironic juxtaposition.",
    ], vis={
        "quatre4": dict(type="mot", t="Four lines to know", g="Maggie · Rose · Kate · Jack · pages 16 – 19", y=250, taille=80),
        "c_glimpse": dict(type="cit", a="Maggie", o="p. 16", x=170, y=200, w=940),
        "glimpse": dict(type="note", cles=["glimpse", "mind"], terme="Maggie · p. 16",
                        t="A game with a child… and a sentence that breaks off: Maggie's own life.",
                        etape="“It was all in your mind”: a memory play in one line.", x=170, y=200, w=940),
        "c_rite": dict(type="cit", a="Rose", o="p. 18", x=170, y=200, w=940),
        "rite": dict(type="note", cles=["Rose", "closer"], terme="The back hills · p. 18",
                     t="Fire, dance, purification: the pagan rite is told by Rose, not by Kate.",
                     etape="The same impulse as the harvest dance the sisters wanted.", x=170, y=200, w=940),
        "c_home": dict(type="cit", a="Kate", o="p. 18", x=170, y=200, w=940),
        "home": dict(type="note", cles=["repetition", "fear"], terme="Kate · p. 18",
                     t="“a Christian home, a Catholic home”: a wall of words around the house.",
                     etape="Her anger looks a lot like fear.", x=170, y=200, w=940),
        "c_layout": dict(type="cit", a="Jack", o="p. 19", x=170, y=200, w=940),
        "layout": dict(type="note", cles=["word", "irony"], terme="Jack · p. 19",
                       t="Formal words first, then the plain one: English and the house escape him.",
                       etape="No collar, just after “a Catholic home”: ironic juxtaposition.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VII. l'analyse
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
        "And it was all in your mind: a perfect line for a memory play.",
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
         voir="jeu1.16", ex="The bird may never have existed: “It was all in your mind. Now we're quits.” A small joke about memory itself."),
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
         r=["His clerical collar", "His hat", "His boots", "His coat"], ok=0, voir="jeu4",
         ex="No clerical collar, scarcely any Irish accent: he enters just after Kate's “Catholic home”, a juxtaposition full of irony."),
    dict(q="Why does Maggie go to the window when Kate talks about Bernie?",
         r=["So that the others cannot see her face", "To look for the fox", "To call the hens", "To see if Gerry is coming"], ok=0,
         voir="jeu5.4", ex="Her feelings stay hidden (subtext); the part ends with her “staring out of the window, seeing nothing”."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
