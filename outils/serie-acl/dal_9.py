"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 9 : le retour de Gerry (PDF de travail, p. 52-58).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu), en suivant les didascalies pas à pas ; les répliques courtes s'affichent en
bulles et sont lues par la voix des sœurs (F) ou la voix d'homme (Gerry). Dans le sycomore, Gerry n'est qu'une voix :
« (Now she sees him. The audience does not see him.) » (p. 56) ; il est placé hors cadre au-dessus de l'arbre, ses bulles
tombent du haut de l'image, la caméra montre la cime vide. L'appel par la fenêtre (p. 55) n'est qu'une note. Puis quatre
répliques à connaître et l'analyse.

Début : p. 52, didascalie « (CHRIS and GERRY enter L. …) » (juste après « not a syllable! » de Kate).
Fin : p. 58, « AGNES. That's what she said. », juste avant « (MAGGIE enters.) ».
Contenu : le récit de l'engagement de Gerry dans la Brigade internationale, la moto, l'Espagne ; Jack « a new man » et
l'échange des chapeaux ; Kate et le « godless Communism » ; la nouvelle usine de gants de Donegal Town (Vera McLaughlin) ;
Gerry dans le sycomore, l'antenne, la chanson du trapèze ; le retour d'Agnes sans Rose.
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_9. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'Irlande catholique et la guerre d'Espagne, l'origine de la chanson) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-9"
NOTION = "Dancing at Lughnasa"
NUM = 9
TITRE = "Gerry comes back"
SUIVANT = "Part 10 · Rose goes missing"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Armagh": "Ar-mah",
                 "McLaughlin": "Mac-Lochlin", "Mundy": "Mundy"}

ARBRE = [1010, -70]   # Gerry dans le sycomore : au-dessus du cadre, jamais vu (« The audience does not see him. », p. 56)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}A man climbs to the top of a tree and calls down: from up here, you can see into the future.",
        "{-q1}The audience smiles. Because we can see into the future too: Michael has already told us how this summer ends.",
        "{-tab_don}{serie}Part nine: Gerry comes back. Spain, a factory, a dead branch… and a sister who has not come home.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="From up here, you can see into the future."),
        "serie": dict(type="mot", t="Gerry comes back", g="Spain · the factory · the sycamore · Rose", y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 9", t="Gerry comes back",
                      sous="Spain, the factory, the sycamore · pages 52 – 58"),
    }),

    # ------------------------------------------------------------------ I. une destination (pp. 52-54)
    dict(id="espagne", chap="A named destination", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page fifty-two. Kate has just demanded silence about Jack. Then Chris and Gerry enter from the lane. "
        "{jeu1.1}He enters backwards, pulling Chris, who holds the end of his walking stick. "
        "All through the scene, he keeps trying to embrace her; she keeps avoiding him.",
        ("C", "No false modesty. You know you're a great dancer, Chrissie.", "jeu1.2"),
        ("C", "Let's dance round the garden again.", "jeu1.3"),
        ("C", "We've done that; and down the lane and up again – without music.", "jeu1.4", {"voix": "F"}),
        "{jeu1.5}Without music: just as Michael told us at the end of Act One. Then Chris asks about signing up. "
        "Was it really in a church?",
        ("C", "A Catholic church as a matter of interest.", "jeu1.6"),
        "{jeu1.7}Page fifty-three. "
        "Naturally I thought he was Spanish, says Gerry. From Armagh, as it turned out. {jeu1.8}She laughs, and avoids his embrace. "
        "Then the questions: a Marxist? No. A Republican, a Socialist, a Communist? No. "
        "Do you speak Spanish? No. Can you make explosives? No.",
        ("C", "Can you ride a motor-bike? Yes. You're in. Sign here.", "jeu1.9"),
        ("C", "So you'll be a dispatch rider?", "jeu1.10", {"voix": "F"}),
        "{jeu1.11}Gerry imitates riding a motor-bike. He leaves on Saturday: first tide. Keep that motor-bike in mind.",
        ("C", "Maybe a couple of months. Everybody says it will be over by Christmas.", "jeu1.12"),
        ("C", "They always say it will be over by Christmas. I still don't know why you're going.", "jeu1.13", {"voix": "F"}),
        "{jeu1.14}Page fifty-four. Not so sure I know either, says Gerry. And then:",
        ("C", "Maybe that's the important thing for a man: a named destination – democracy, Ballybeg, heaven.", "jeu1.15"),
        ("C", "Women's illusions aren't so easily satisfied – they make better drifters.", "jeu1.16"),
        "{jeu1.17}Come inside and look at this wireless, says Chris. I know nothing about radios, he protests. "
        "{jeu1.18}She runs into the kitchen. {jeu1.19}He follows.",
        ("P", 2.0),
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Gerry"], etats=[
            dict(pos={"Kate": [295, 430], "Maggie": [205, 430], "Chris": "off", "Gerry": "off"},
                 act={"Kate": "debout", "Maggie": "debout"}, cam="tout", objets={"kites": "banc"},
                 note="(CHRIS and GERRY enter L.) p. 52"),
            dict(chemin={"Gerry": ["allee", [715, 460]], "Chris": ["allee", [810, 460]]}, chemin_duree=5,
                 note="He enters backwards, pulling CHRIS, who holds the end of his walking stick."),
            dict(pos={"Gerry": [715, 460], "Chris": [810, 460]},
                 dit=["Gerry", "No false modesty. You know you're a great dancer, Chrissie."]),
            dict(dit=["Gerry", "Let's dance round the garden again."]),
            dict(dit=["Chris", "We've done that; and down the lane and up again – without music."]),
            dict(note="“Tell me about signing up. Was it really in a church?”"),
            dict(dit=["Gerry", "A Catholic church as a matter of interest."], note="(p. 53)"),
            dict(dit=["Gerry", "Naturally I thought he was Spanish. From Armagh, as it turned out."]),
            dict(pos={"Chris": [905, 450]}, note="(She laughs – and avoids his embrace.)"),
            dict(dit=["Gerry", "‘Can you ride a motor-bike’ ‘Yes.’ ‘You're in. Sign here.’"]),
            dict(dit=["Chris", "So you'll be a dispatch rider?"]),
            dict(note="(GERRY imitates riding a motor-bike.) “First tide.”"),
            dict(dit=["Gerry", "Maybe a couple of months. Everybody says it will be over by Christmas."], note="(p. 54)"),
            dict(dit=["Chris", "They always say it will be over by Christmas. I still don't know why you're going."]),
            dict(note="“Not so sure I know either.”"),
            dict(dit=["Gerry", "… the important thing for a man: a named destination – democracy, Ballybeg, heaven."]),
            dict(dit=["Gerry", "Women's illusions aren't so easily satisfied – they make better drifters."], note="(Laughs.)"),
            dict(note="“Come inside and take a look at this wireless.” — “I know nothing about radios.”"),
            dict(chemin={"Chris": [[905, 450], "seuil", "porte", [385, 430]]}, chemin_duree=3.5,
                 note="(She runs into the kitchen. He follows.)"),
            dict(chemin={"Gerry": [[715, 460], "seuil", "porte", [475, 430]]}, chemin_duree=3.5, cam="cuisine",
                 note="(She runs into the kitchen. He follows.)"),
        ]),
    }),

    # ------------------------------------------------------------------ II. le communisme sans Dieu (pp. 54-56)
    dict(id="kate", chap="Godless Communism", fond="nuit", humeur="tension", beats=[
        "{jeu2}In the kitchen: Jack has been seen striding through the meadow. He looks like a new man.",
        ("C", "Were you talking to him?", "jeu2.1", {"voix": "F"}),
        ("C", "He wants to do a swap with me: I'm to give him this hat and he's to give me some sort of a three-cornered hat "
              "with feathers", "jeu2.2"),
        "{jeu2.3}Page fifty-five. Chrissie says you're great with radios, says Maggie. And Gerry plays the expert.",
        ("C", "Let me check the aerial first. Very often that's where the trouble lies.", "jeu2.4"),
        ("C", "Then I'll have a look at the ignition and sparking plugs. Leave it to Gerry.", "jeu2.5"),
        "{jeu2.6}Car words, for a radio: he is bluffing. He winks at Chris as he goes out the front door. "
        "{jeu2.7}Then Kate speaks. It would be on her conscience, she says, to stay silent.",
        ("C", "It's a sorry day for Ireland when we send young men off to Spain to fight for godless Communism.", "jeu2.8",
         {"voix": "F"}),
        ("C", "For democracy, Kate.", "jeu2.9", {"voix": "F"}),
        ("C", "I'm not going to argue. I just want to clear my conscience.", "jeu2.10", {"voix": "F"}),
        ("C", "That's the important thing, of course. And now you've cleared it.", "jeu2.11", {"voix": "F"}),
        "{jeu2.12}Pure irony: the youngest sister no longer simply obeys. Gerry runs on and calls through the window: "
        "turn the radio on! It's on, says Maggie. And he runs off again.",
        "{jeu2.13}Then Chris tells her news. They met Vera McLaughlin, the knitting agent.",
        ("C", "She's not buying any more hand-made gloves.", "jeu2.14", {"voix": "F"}),
        "Too dear, she says.",
        ("C", "Too dear! She pays them a pittance!", "jeu2.15", {"voix": "F"}),
        ("C", "There's a new factory started up in Donegal Town. They make machine gloves more quickly there and far more cheaply.",
         "jeu2.16", {"voix": "F"}),
        "{jeu2.17}Page fifty-six. Buses will bring the workers to the factory. Vera tried to get a job there herself: "
        "she was told she was too old. She's forty-one.",
        ("C", "Oh God … poor Aggie … poor Rose … what'll they do?", "jeu2.18", {"voix": "F"}),
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Gerry"], etats=[
            dict(pos={"Kate": [295, 430], "Maggie": [205, 430], "Chris": [385, 430], "Gerry": [475, 430]},
                 act={"Kate": "debout", "Maggie": "debout"}, cam="cuisine", objets={"kites": "banc"},
                 note="“You should see Jack striding through the meadow. He looks like a new man.”"),
            dict(dit=["Kate", "Were you talking to him?"], note="(to GERRY)"),
            dict(dit=["Gerry", "He wants to do a swap with me: I'm to give him this hat …"],
                 note="… for “a three-cornered hat with feathers” (p. 54)"),
            dict(note="MAGGIE: “Chrissie says you're great with radios, Gerry” (p. 55)"),
            dict(dit=["Gerry", "Let me check the aerial first. Very often that's where the trouble lies."]),
            dict(dit=["Gerry", "Then I'll have a look at the ignition and sparking plugs. Leave it to Gerry."]),
            dict(chemin={"Gerry": ["porte", "seuil", [700, 250]]}, chemin_duree=4,
                 note="(He winks at Chris as he goes out the front door and off R.)"),
            dict(pos={"Gerry": "off"}, note="“it would be on my conscience if I didn't tell you”"),
            dict(dit=["Kate", "… a sorry day for Ireland when we send young men off to Spain to fight for godless Communism."]),
            dict(dit=["Chris", "For democracy, Kate."]),
            dict(dit=["Kate", "I'm not going to argue. I just want to clear my conscience."]),
            dict(dit=["Chris", "That's the important thing, of course. And now you've cleared it."]),
            dict(note="(GERRY runs on and calls through the window.) “Turn the radio on, Chrissie, would you?”"),
            dict(note="“we met Vera McLaughlin, the knitting agent”"),
            dict(dit=["Chris", "She's not buying any more hand-made gloves."]),
            dict(dit=["Kate", "Too dear! She pays them a pittance!"], note="(p. 56)"),
            dict(dit=["Chris", "There's a new factory started up in Donegal Town. They make machine gloves …"]),
            dict(note="Vera was told “she was too old. She's forty-one.”"),
            dict(dit=["Maggie", "Oh God … poor Aggie … poor Rose … what'll they do?"]),
        ]),
    }),

    # ------------------------------------------------------------------ III. le sycomore (pp. 56-58)
    dict(id="sycomore", chap="On top of the sycamore", fond="nuit", humeur="mystere", beats=[
        "{jeu3}Agnes enters the garden, and Kate sees her.",
        ("C", "Shhh. They're back. Let them have their tea in peace. Tell them later.", "jeu3.1", {"voix": "F"}),
        "{jeu3.2}They busy themselves with their tasks. Agnes leaves two small pails of bilberries outside the door. "
        "Just as she is about to come in, a voice off calls her.",
        ("C", "Who is that beautiful woman!", "jeu3.3"),
        ("C", "Gerry?", "jeu3.4", {"voix": "F"}),
        ("C", "Up here, Aggie!", "jeu3.5"),
        ("C", "On top of the sycamore.", "jeu3.6"),
        "{jeu3.7}Now she sees him. The audience does not: on stage, Gerry is only a voice, up in the tree.",
        ("C", "What are you doing up there?", "jeu3.8", {"voix": "F"}),
        ("C", "You can see into the future from here, Aggie!", "jeu3.9"),
        ("C", "The tree isn't safe, Gerry. Please come down.", "jeu3.10", {"voix": "F"}),
        ("C", "Come up and see what's going to happen to you!", "jeu3.11"),
        ("C", "That branch is dead, Gerry. I'm telling you.", "jeu3.12", {"voix": "F"}),
        "{jeu3.13}The branch begins to sway. Page fifty-seven. Gerry sings. Outside the text: an old music-hall song.",
        ("C", "He flies through the air with the greatest of ease –", "jeu3.14"),
        "{jeu3.15}Agnes covers her eyes in terror.",
        ("C", "You're going to fall! I'm not looking! I'm not watching!", "jeu3.16", {"voix": "F"}),
        "{jeu3.17}She dashes into the house: that clown of a man is up on top of the sycamore! He's fixing the aerial, says Maggie.",
        ("C", "He's going to break his neck – I'm telling you!", "jeu3.18", {"voix": "F"}),
        ("C", "As long as he fixes the wireless first.", "jeu3.19", {"voix": "F"}),
        "{jeu3.20}The bilberries? Just that bit too ripe, says Agnes: we should have picked them a week ago. "
        "Then she asks about Rose. She wasn't feeling well; she went home to lie down. A pause.",
        ("C", "She's here, isn't she?", "jeu3.21", {"voix": "F"}),
        "{jeu3.22}Maggie rushes off to the bedroom. {jeu3.23}No one has seen Rose. She left Agnes hours ago, at the old quarry.",
        ("C", "To come home?", "jeu3.24", {"voix": "F"}),
        ("C", "That's what she said.", "jeu3.25", {"voix": "F"}),
        "Part nine stops here.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Agnes", "Gerry"], etats=[
            dict(pos={"Kate": [295, 430], "Maggie": [205, 430], "Chris": [385, 430], "Agnes": "off", "Gerry": "off"},
                 act={"Kate": "debout", "Maggie": "debout"}, cam="tout", objets={"kites": "banc"},
                 chemin={"Agnes": ["allee", "jardin", [640, 420]]}, chemin_duree=6,
                 note="(AGNES enters the garden. KATE sees her.) p. 56"),
            dict(pos={"Agnes": [640, 420]}, dit=["Kate", "Shhh. They're back. Let them have their tea in peace. Tell them later."]),
            dict(act={"Kate": "range", "Maggie": "range", "Chris": "repasse"},
                 note="(They busy themselves with their tasks.) Two small pails of bilberries left at the door"),
            dict(pos={"Gerry": ARBRE}, cam="jardin", dit=["Gerry", "Who is that beautiful woman!"]),
            dict(dit=["Agnes", "Gerry?"]),
            dict(dit=["Gerry", "Up here, Aggie!"]),
            dict(dit=["Gerry", "On top of the sycamore."]),
            dict(cam="arbre", note="(Now she sees him. The audience does not see him.)"),
            dict(cam="jardin", dit=["Agnes", "What are you doing up there?"]),
            dict(dit=["Gerry", "You can see into the future from here, Aggie!"]),
            dict(dit=["Agnes", "The tree isn't safe, Gerry. Please come down."]),
            dict(dit=["Gerry", "Come up and see what's going to happen to you!"]),
            dict(dit=["Agnes", "That branch is dead, Gerry. I'm telling you."]),
            dict(cam="arbre", note="(The branch begins to sway.)"),
            dict(cam="jardin", dit=["Gerry", "‘He flies through the air with the greatest of ease –’ Wheeeeeee!"]),
            dict(act={"Agnes": "pleure"}, note="(She covers her eyes in terror.) p. 57"),
            dict(dit=["Agnes", "You're going to fall! I'm not looking! I'm not watching!"]),
            dict(pos={"Agnes": [475, 430]}, act={"Agnes": "debout", "Kate": "debout", "Maggie": "debout", "Chris": "debout"},
                 cam="cuisine", note="(She dashes into the house.) “That clown of a man is up on top of the sycamore.”"),
            dict(dit=["Agnes", "He's going to break his neck – I'm telling you!"]),
            dict(dit=["Maggie", "As long as he fixes the wireless first."]),
            dict(note="“Just that bit too ripe. We should have picked them a week ago.”"),
            dict(dit=["Agnes", "She's here, isn't she?"]),
            dict(pos={"Maggie": "arriere"}, duree=1.6, note="(MAGGIE rushes off to the bedroom.)"),
            dict(pos={"Maggie": "off"}, note="“Hours ago … almost immediately after we got to the old quarry.”"),
            dict(dit=["Kate", "To come home?"], note="(p. 58)"),
            dict(dit=["Agnes", "That's what she said."]),
        ]),
    }),

    # ------------------------------------------------------------------ IV. quatre répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="“a named destination”; “godless Communism”; the factory; “see into the future”.", beats=[
        "{quatre}Four lines from these pages are worth knowing by heart. First, Gerry.",
        "{-quatre}",
        ("C", "Maybe that's the important thing for a man: a named destination – democracy, Ballybeg, heaven.", "c_dest"),
        "{-c_dest}{drift}Democracy, Ballybeg, heaven: a cause, a village, a religion, all on the same level. "
        ""
        "{drift.1}Women, he adds, make better drifters. Bitter irony: Agnes and Rose will end their lives drifting through London.",
        "{-drift}Then Kate.",
        ("C", "It's a sorry day for Ireland when we send young men off to Spain to fight for godless Communism.", "c_sorry",
         {"voix": "F"}),
        "{-c_sorry}{espagne}Outside the text: in 1936, most of Catholic Ireland, and its Church, sided against the Spanish Republic. "
        "Kate speaks with the voice of her Church.",
        "{-espagne}Then Chris, with the news.",
        ("C", "There's a new factory started up in Donegal Town. They make machine gloves more quickly there and far more cheaply.",
         "c_factory", {"voix": "F"}),
        "{-c_factory}{usine}The economic collapse, in two sentences. Agnes and Rose lose their only income. "
        "And Kate's answer is silence: tell them later.",
        "{-usine}And Gerry, up in the tree.",
        ("C", "You can see into the future from here, Aggie!", "c_future"),
        "{-c_future}{ironie}A joke… and perfect dramatic irony. {ironie.1}Come up and see what's going to happen to you! "
        "{ironie.2}But we already know: in early September, Agnes and Rose will leave for ever.",
    ], vis={
        "quatre": dict(type="mot", t="Four lines to know", g="pages 54 – 56", y=260, taille=84),
        "c_dest": dict(type="cit", a="Gerry", o="p. 54", x=170, y=190, w=940),
        "drift": dict(type="cols", g="Men", gq="need “a named destination”", d="Women",
                      dq="“they make better drifters”", vs="≠", repere="Gerry's view of the sexes"),
        "c_sorry": dict(type="cit", a="Kate", o="p. 55", x=170, y=190, w=940),
        "espagne": dict(type="note", cles=["Catholic", "Republic"], terme="Outside the text",
                        t="In 1936, most of Catholic Ireland and its Church sided against the Spanish Republic.",
                        etape="Kate speaks with the voice of her Church.", x=170, y=200, w=940),
        "c_factory": dict(type="cit", a="Chris", o="p. 56", x=170, y=180, w=940),
        "usine": dict(type="note", cles=["income", "silence"], terme="Chris · p. 56",
                      t="Machine gloves, “more quickly” and “far more cheaply”: Agnes and Rose lose their only income.",
                      etape="Kate: “Tell them later.”", x=170, y=200, w=940),
        "c_future": dict(type="cit", a="Gerry", o="p. 56", x=170, y=200, w=940),
        "ironie": dict(type="liste", titre="Dramatic irony", cles=["irony"], items=[
            "Gerry: “Come up and see what's going to happen to you!”",
            "Act One: “both Rose and Agnes would have left for ever”"], marques=["1", "2"], x=150, y=200, w=980),
    }),

    # ------------------------------------------------------------------ IV. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Gerry the drifter, the outside world breaking in, dramatic irony, and comedy that turns to fear.", beats=[
        "{a1}Now the analysis. Four ideas. "
        "{a1.1}One: Gerry the drifter. Dancing teacher, gramophone salesman, now a soldier: he moves freely, the sisters cannot. "
        "Useful for an essay on gender: men leave freely; for the women, leaving means exile, as Agnes and Rose will show.",
        "{-a1}{a2}{a2.1}Two: the outside world breaks in. History, with the Spanish war and the Church's view of it. "
        "Industry, with machines and buses. Kate answers both with silence: tell them later. But silence stops nothing.",
        "{-a2}{a3}{a3.1}Three: dramatic irony and foreshadowing. Only the audience can really see into the future. "
        "And the motor-bike? On page sixty-four, Michael tells us Gerry was wounded in Barcelona: he fell off his motor-bike. "
        "You're going to fall, cried Agnes.",
        "{-a3}{a4}{a4.1}Four: comedy turning to fear. A farce, a clown in a tree, a circus song… "
        "then the end of the sisters' work, and a sister who has not come home. The tone is tragicomic: the laughter makes the loss sharper.",
        "{-a4}{carte}Here is part nine for your essay. {carte.1}Gerry the drifter. {carte.2}The outside world. "
        "{carte.3}Dramatic irony. {carte.4}And laughter and fear, side by side.",
    ], vis={
        "a1": dict(type="note", cles=["drifter", "destination"], terme="1 · Gerry the drifter",
                   t="“a named destination – democracy, Ballybeg, heaven”: any cause will do.",
                   etape="Men leave freely; for the women, leaving means exile.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["History", "industry"], terme="2 · The outside world breaks in",
                   t="Spain and “godless Communism”; a factory that makes gloves “far more cheaply”.",
                   etape="Kate answers with silence: “Tell them later.”", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["irony", "foreshadowing"], terme="3 · Seeing into the future",
                   t="“You can see into the future from here”: only the audience really can.",
                   etape="The motor-bike; “You're going to fall!”; p. 64: wounded in Barcelona.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["tragicomic"], terme="4 · Comedy turning to fear",
                   t="A farce, a clown in a tree, a circus song… then “She's here, isn't she?”",
                   etape="A tragicomic tone: laughter makes the loss sharper.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="GERRY COMES BACK", branches=[
            dict(t="The drifter", items=["“a named destination”", "“better drifters”", "a dispatch rider"]),
            dict(t="Outside world", items=["“godless Communism”", "the factory", "“Tell them later”"]),
            dict(t="Dramatic irony", items=["“into the future”", "the motor-bike", "“left for ever”"]),
            dict(t="Tone", items=["a clown in a tree", "the circus song", "“She's here, isn't she?”"])]),
    }),
]

QUIZ = [
    dict(q="Where, according to Gerry, did he sign up for the International Brigade?",
         r=["In a Catholic church", "In a pub in Ballybeg", "On a ship to Spain", "In the district commissioner's office"], ok=0,
         voir="jeu1.6",
         ex="“A Catholic church as a matter of interest”: a comic irony, since Kate calls the cause “godless Communism”."),
    dict(q="Why is Gerry accepted, in his story?",
         r=["He can ride a motor-bike", "He speaks Spanish", "He can make explosives", "He is a Communist"], ok=0, voir="jeu1.9",
         ex="He answers “No” to everything else; “Can you ride a motor-bike” “Yes.” “You're in.” He will be a dispatch rider."),
    dict(q="What does Gerry say is “the important thing for a man”?",
         r=["A named destination", "A steady job", "A family", "A good conscience"], ok=0, voir="c_dest",
         ex="“a named destination – democracy, Ballybeg, heaven”: for Gerry, any cause will do, as long as it has a name."),
    dict(q="Why will Vera McLaughlin stop buying the sisters' gloves?",
         r=["A new factory in Donegal Town makes machine gloves faster and cheaper", "The gloves are badly made",
            "Kate has quarrelled with her", "She is moving to England"], ok=0, voir="c_factory",
         ex="Industrialisation reaches Ballybeg: Agnes and Rose lose their only income. Kate decides to “tell them later”."),
    dict(q="What is the dramatic irony of “You can see into the future from here, Aggie!”?",
         r=["The audience already knows Agnes and Rose will leave for ever", "Gerry really is a fortune-teller",
            "Agnes knows Gerry is lying", "It tells us the wireless will never work"], ok=0, voir="c_future",
         ex="Michael's prolepsis at the end of Act One told us that both Rose and Agnes would leave in early September."),
    dict(q="How does part nine end?",
         r=["Agnes comes back alone and asks if Rose is in the house", "Gerry falls from the sycamore",
            "Kate tells Agnes about the factory", "Jack says Mass in the kitchen"], ok=0, voir="jeu3.21",
         ex="Rose left Agnes at the old quarry hours ago: “She's here, isn't she?” No one has seen her."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
