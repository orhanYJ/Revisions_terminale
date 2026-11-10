"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 7 : « Cracks », la fin de l'acte I (PDF de travail, p. 37-44).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu), en suivant les didascalies pas à pas ; les répliques courtes s'affichent en
bulles et sont lues par les voix des personnages ; l'enfant n'est jamais vu (emplacement en pointillé près des
cerfs-volants), Michael adulte, entré à gauche p. 38, dit ses répliques depuis le bord du plateau. La prolepse finale de
Michael (p. 43-44) est racontée, pas jouée : projecteur sur Michael, notes pour ce qu'il raconte ; seul est joué ce que
la didascalie montre pendant qu'il parle (Jack et les baguettes, Kate qui regarde, les sœurs aux portes et à la fenêtre).
Puis quatre répliques expliquées et l'analyse (inchangée).

Début : p. 37, « And what was that all about? » (Kate et Maggie seules après la sortie d'Agnes, fin de la partie 6).
Fin : « BLACKOUT », fin de l'acte I (p. 44). Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_7.
Citations courtes, à fin d'analyse ; le reste est résumé. Ce qui ne vient pas du texte (les Brigades internationales,
la guerre d'Espagne) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-7"
NOTION = "Dancing at Lughnasa"
NUM = 7
TITRE = "Cracks"
SUIVANT = "Part 8 · Three weeks later"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Okawa": "Oh-kah-wa",
                 "Kampala": "Kam-pah-la", "Mundy": "Mundy", "Capri": "Ca-pree"}

GARCON = [790, 455]                      # l'enfant à ses cerfs-volants, jamais vu
KATE_S, MAGGIE_S = [300, 384], [366, 388]   # Kate assise, Maggie assise à côté d'elle (p. 38)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rad}{q1}Gerry and Chris have danced away down the lane. Agnes has run out, close to tears. "
        "Kate and Maggie are alone in the kitchen.",
        "{-q1}In the silence, Kate, the woman who holds the house together, begins to break.",
        "{-tab_rad}{serie}Part seven: the end of Act One. Kate's fears, Jack's strange new faith… "
        "and a narrator who tells us how it all ends.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="“And what was that all about?”"),
        "serie": dict(type="mot", t="The end of Act One", g="Kate's fears · Jack's faith · the ending, told in advance",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 7", t="Cracks",
                      sous="The end of Act One · pages 37 – 44"),
    }),

    # ------------------------------------------------------------------ I. les fissures
    dict(id="fissures", chap="Hair cracks", fond="nuit", humeur="tension", beats=[
        "{jeu1}Page thirty-seven. Agnes has just run off.",
        ("C", "And what was that all about?", "jeu1.1", {"voix": "F"}),
        "{jeu1.2}Who's to say? Kate rages at Mr Evans: God forgive him, the bastard! And at once: God forgive me!",
        "{jeu1.3}Maggie puts her boots back on, singing listlessly: 'Twas on the Isle of Capri.",
        ("C", "She's right: I am a righteous bitch, amn't I?", "jeu1.4", {"voix": "F"}),
        "{jeu1.5}Maggie stands up and looks at her feet. Now. Who's for a fox-trot? But Kate goes on.",
        ("C", "suddenly you realize that hair cracks are appearing everywhere; that control is slipping away", "jeu1.6",
         {"voix": "F"}),
        ("C", "It's all about to collapse, Maggie.", "jeu1.7", {"voix": "F"}),
        ("C", "Nothing's about to collapse, Kate.", "jeu1.8", {"voix": "F"}),
        "{jeu1.9}Then Kate admits the truth about the Sweeney boy: a goat, a sacrifice for the Lughnasa Festival, "
        "and Sweeney, drunk, toppled into the bonfire.",
        "{jeu1.10}Maggie goes to her, and sits beside her. {jeu1.11}And Kate's fears pour out: Christina's depressions, "
        "Jack's superiors, who probably had no choice but to send him home, and the parish priest: there may be no job for her after the summer.",
        "{jeu1.12}She tries to laugh. {jeu1.13}Now she cries. Maggie puts her arm around her. And Michael enters.",
        ("C", "If I died – if I lost my job – if this house were broken up – what would become of our Rosie?", "jeu1.14",
         {"voix": "F"}),
        "{jeu1.15}I must put my trust in God, Maggie, mustn't I?",
        ("C", "Kate … Kate … Kate, I love …", "jeu1.16", {"voix": "F"}),
        ("C", "I believe that, too … I believe that … I do believe that …", "jeu1.17", {"voix": "F"}),
        "{jeu1.18}Maggie holds her, and rocks her.",
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Michael"], etats=[
            dict(pos={"Kate": [300, 380], "Maggie": "radio", "Michael": "off"}, act={"Kate": "debout", "Maggie": "debout"},
                 objets={"kites": "kites", "garcon": GARCON}, note="Kate and Maggie, alone (p. 37)"),
            dict(dit=["Kate", "And what was that all about?"]),
            dict(note="“God forgive him, the bastard! There! That's what I mean! God forgive me!”"),
            dict(act={"Maggie": "assis"}, note="MAGGIE begins putting on her long-laced boots again."),
            dict(dit=["Kate", "She's right: I am a righteous bitch, amn't I?"]),
            dict(act={"Maggie": "debout"}, note="“Now. Who's for a fox-trot?” (She stands up and looks at her feet.)"),
            dict(dit=["Kate", "suddenly you realize that hair cracks are appearing everywhere; that control is slipping away"]),
            dict(dit=["Kate", "It's all about to collapse, Maggie."]),
            dict(dit=["Maggie", "Nothing's about to collapse, Kate."], note="(Wearily.)"),
            dict(note="“some devilish thing with a goat – some sort of sacrifice for the Lughnasa Festival”"),
            dict(pos={"Kate": KATE_S, "Maggie": MAGGIE_S}, act={"Kate": "assis", "Maggie": "assis"}, duree=2.2,
                 note="(MAGGIE goes to her and sits beside her.) (p. 38)"),
            dict(note="Christina's depressions · Father Jack's superiors · “the numbers in the school are falling”"),
            dict(note="(She tries to laugh.) “we can spend the day dancing to Marconi.”"),
            dict(pos={"Michael": "michael"}, act={"Kate": "pleure"}, cam="tout", note="(Now she cries. MAGGIE puts her arm around her. MICHAEL enters L.)"),
            dict(dit=["Kate", "If I died – if I lost my job – if this house were broken up – what would become of our Rosie?"]),
            dict(note="“I must put my trust in God, Maggie” (p. 38)"),
            dict(dit=["Maggie", "Kate … Kate … Kate, I love …"]),
            dict(dit=["Kate", "I believe that, too … I believe that … I do believe that …"]),
            dict(act={"Maggie": "balance"}, note="(MAGGIE holds her and rocks her.)"),
        ]),
    }),

    # ------------------------------------------------------------------ II. Chris et l'enfant
    dict(id="chris", chap="A black bike", fond="nuit", humeur="lumiere", beats=[
        "{jeu2}Chris enters quickly, hugging herself. {jeu2.1}She sees the boy at his kites, goes to him and gets down beside him. "
        "She speaks eagerly, excitedly, confidentially. Michael speaks the boy's lines.",
        ("C", "Well. Now you've had a good look at him. What do you think of him?", "jeu2.2", {"voix": "F"}),
        ("C", "I never saw him before.", "jeu2.3"),
        "{jeu2.4}He has got a great new job, Chris whispers. It's a secret.",
        ("C", "And he has bought a bicycle for you – a black bike – a man's bike", "jeu2.5", {"voix": "F"}),
        "{jeu2.6}She suddenly embraces him, and hugs him.",
        ("C", "Is he coming back soon?", "jeu2.7"),
        ("C", "Maybe – maybe. Yes! Yes, he is!", "jeu2.8", {"voix": "F"}),
        "{jeu2.9}Her eyes are closed. Next week, the week after, soon, soon! She gets to her feet, bends down again and kisses "
        "him lightly. {jeu2.10}She laughs, pirouettes flirtatiously before him, and dances into the kitchen.",
        "{jeu2.11}Agnes enters through the back door, carrying some roses. And Gerry sends his love to them all.",
        ("C", "His special love to you, Aggie; and a big kiss.", "jeu2.12", {"voix": "F"}),
        ("C", "For me?", "jeu2.13", {"voix": "F"}),
        "{jeu2.14}Maggie, quickly: roses for Jack's windowsill, with a wee card, ROSES, so he won't be demented looking for the word. "
        "{jeu2.15}Then: who makes the tea?",
        ("C", "I make the tea every evening, don't I?", "jeu2.16", {"voix": "F"}),
        "{jeu2.17}Agnes says it almost aggressively. Aggie's the chef, says Maggie. She sings raucously, {jeu2.18}and goes to the radio.",
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Chris", "Michael"], etats=[
            dict(pos={"Kate": KATE_S, "Maggie": MAGGIE_S, "Michael": "michael", "Chris": [1110, 300]},
                 act={"Kate": "assis", "Maggie": "balance", "Chris": "debout"},
                 objets={"kites": "kites", "garcon": GARCON}, cam="tout", note="CHRIS enters quickly L., hugging herself. (p. 38)"),
            dict(pos={"Chris": [845, 440]}, act={"Chris": "agenouille", "Maggie": "assis"}, duree=3.0,
                 note="She sees the boy at his kites, goes to him and gets down beside him."),
            dict(dit=["Chris", "Well. Now you've had a good look at him. What do you think of him?"]),
            dict(dit=["Michael", "I never saw him before."], note="BOY. (Bored.)"),
            dict(note="“I'll tell you a secret. The others aren't to know.”"),
            dict(dit=["Chris", "And he has bought a bicycle for you – a black bike – a man's bike"], note="(p. 39)"),
            dict(note="(She suddenly embraces him and hugs him.)"),
            dict(dit=["Michael", "Is he coming back soon?"]),
            dict(dit=["Chris", "Maybe – maybe. Yes! Yes, he is!"], note="CHRIS. (Eyes closed.)"),
            dict(act={"Chris": "debout"}, note="(She gets to her feet, then bends down again and kisses him lightly.)"),
            dict(pos={"Chris": [452, 418]}, act={"Chris": "danse_douce"}, duree=4.0,
                 note="(She laughs, pirouettes flirtatiously before him and dances into the kitchen.)"),
            dict(pos={"Agnes": [530, 330]}, act={"Chris": "debout", "Agnes": "debout"}, tient={"Agnes": "bouquet"},
                 note="(AGNES enters through the back door. She is carrying some roses.)"),
            dict(dit=["Chris", "His special love to you, Aggie; and a big kiss."]),
            dict(dit=["Agnes", "For me?"]),
            dict(note="“a wee card – ‘ROSES’ – so that the poor man's head won't be demented looking for the word”"),
            dict(note="“And now, girls, the daily dilemma: what's for the tea?” (p. 40)"),
            dict(dit=["Agnes", "I make the tea every evening, don't I?"], note="AGNES. (Almost aggressively.)"),
            dict(act={"Maggie": "debout"}, note="“Aggie's the chef.” (Sings raucously.)"),
            dict(pos={"Maggie": "radio"}, note="(Now at the radio.) “Marconi, my friend, you're not still asleep, are you?”"),
        ]),
    }),

    # ------------------------------------------------------------------ III. les esprits des ancêtres
    dict(id="jack", chap="Ancestral spirits", fond="nuit", humeur="mystere", beats=[
        "{jeu3}Father Jack enters. He shuffles quickly across the kitchen floor, hands behind his back, eyes on the ground, "
        "as if he were going somewhere else.",
        ("C", "If anybody is looking for me, I'll be down at the bank of the river for the rest of the …", "jeu3.1"),
        "{jeu3.2}He trails off, and looks around. Now he knows where he is. He remembers the day he left: "
        "a picture… a camera-picture… a photograph! And Mother's face, he says, showed nothing.",
        ("C", "Do you think perhaps Mother didn't believe in the ancestral spirits?", "jeu3.3"),
        "{jeu3.4}Kate is shocked: Mother knew she was going straight to heaven. "
        "{jeu3.5}Jack answers with a story: a German priest saved by the local medicine man.",
        "{jeu3.6}In Ryanga, he says, to please the spirits, we kill a rooster or a young goat. He hunts for the word. Spectacle? Lost it.",
        "{jeu3.7}The English district commissioner calls him the Irish Outcast, and wants to keep him from going native. "
        "His parting present: the last governor's ceremonial hat.",
        ("C", "Ceremony! That's the word! How could I have forgotten that?", "jeu3.8"),
        ("C", "The offering, the ritual, the dancing – a ceremony!", "jeu3.9"),
        "{jeu3.10}On the boat home, he lost even the simplest words.",
        ("C", "And you can always point, Margaret, can't you?", "jeu3.11"),
        ("C", "Or make signs.", "jeu3.12", {"voix": "F"}),
        ("C", "Or dance.", "jeu3.13", {"voix": "F"}),
        "{jeu3.14}Then: so Michael is a love-child? In Ryanga, says Jack, women were eager to have love-children.",
        "{jeu3.15}Kate stops him: you're home in Donegal now. A walk, tea, the paper, medicine, bed, "
        "until we have you back to what you were. "
        "{jeu3.16}Jack goes out to the garden. Kate gets her cardigan.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Chris", "Jack", "Michael"], etats=[
            dict(pos={"Kate": KATE_S, "Maggie": "radio", "Agnes": [530, 330], "Chris": [452, 418], "Michael": "michael",
                      "Jack": "arriere"},
                 act={"Kate": "assis", "Maggie": "debout", "Agnes": "debout", "Chris": "debout", "Jack": "voute"},
                 tient={"Agnes": "bouquet"}, objets={"kites": "kites", "garcon": GARCON}, cam="tout",
                 note="“hands behind his back, eyes on the ground” (p. 40)"),
            dict(pos={"Jack": [200, 440]}, duree=2.5,
                 dit=["Jack", "If anybody is looking for me, I'll be down at the bank of the river for the rest of the …"]),
            dict(act={"Jack": "debout"}, note="(He trails off and looks around. Now he knows where he is. He smiles.)"),
            dict(dit=["Jack", "Do you think perhaps Mother didn't believe in the ancestral spirits?"], note="(p. 41)"),
            dict(note="“Ancestral – ! What are you blathering about, Jack?”"),
            dict(note="“Okawa and I brought him to our local medicine man”"),
            dict(note="“we kill a rooster or a young goat” … “My vocabulary has deserted me.”"),
            dict(note="“The Irish Outcast” … “to keep me from ‘going native’” (p. 42)"),
            dict(dit=["Jack", "Ceremony! That's the word! How could I have forgotten that?"]),
            dict(dit=["Jack", "The offering, the ritual, the dancing – a ceremony!"]),
            dict(note="“days when I couldn't remember even the simplest words”"),
            dict(dit=["Jack", "And you can always point, Margaret, can't you?"]),
            dict(dit=["Maggie", "Or make signs."]),
            dict(dit=["Maggie", "Or dance."]),
            dict(note="“So Michael is a love-child?” (p. 43)"),
            dict(note="“until we have you back to what you were” (Kate)"),
            dict(pos={"Jack": [615, 440]}, duree=4.0, note="(JACK goes out to the garden. KATE gets her cardigan.)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. la prolepse (racontée)
    dict(id="prolepse", chap="As it turned out", fond="nuit", humeur="tension", beats=[
        "{jeu4}And now Michael turns to us. Some of Aunt Kate's forebodings, he says, weren't all that inaccurate. "
        "{jeu4.1}She was right about Uncle Jack: he had been sent home, not because his mind was confused, "
        "but for reasons that became clearer as the summer drew to a close.",
        "{jeu4.2}Right about her job, lost more because of Father Jack than falling numbers. "
        "{jeu4.3}Right about Rose, and, had she known, about Agnes too. But not the speed of it.",
        ("C", "… one morning in early September both Rose and Agnes would have left for ever.", "jeu4.4"),
        "{jeu4.5}None of this is shown, only told. But on stage, Jack picks up two pieces of wood from the kites, "
        "and strikes them together. Again, and again.",
        "{jeu4.6}He beats out a rhythm, and shuffle-dances, bent over, eyes on the ground, muttering. {jeu4.7}Kate comes out to the garden and stands still, watching him. "
        "{jeu4.8}Rose enters. Now Rose, Maggie and Agnes are all watching, some at the door, some through the window. "
        "Only Chris has her eyes closed, her face raised: remembering.",
        "{jeu4.9}Michael goes on. Kate was wrong about my father: he did come back, in a couple of weeks. "
        "{jeu4.10}And once more, he and Chris danced together, this time without music. "
        "No singing, no melody, no words. Michael even calls it a ceremony: Jack's word. {jeu4.11}Then he went off to fight with the International Brigade.",
        "{jeu4.12}Kate now goes to Jack, and gently takes the sticks from him. She places them on the ground.",
        ("C", "We'll leave these back where we found them, Jack. They aren't ours. They belong to the child.", "jeu4.13",
         {"voix": "F"}),
        "{jeu4.14}She takes his arm, and leads him off. Now we'll go for our walk. "
        "{jeu4.15}The others watch with expressionless faces. Blackout. End of Act One.",
        ("P", 2.0),
    ], vis={
        "jeu4": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack", "Michael"], etats=[
            dict(pos={"Kate": [300, 380], "Maggie": "radio", "Agnes": [530, 330], "Chris": [452, 418], "Michael": "michael",
                      "Jack": [615, 440], "Rose": "off"},
                 act={"Kate": "debout", "Maggie": "debout", "Agnes": "debout", "Chris": "debout", "Jack": "debout"},
                 tient={"Agnes": "bouquet"}, objets={"kites": "kites", "garcon": GARCON}, cam="tout",
                 lumiere="spot", eclaire=["Michael", "Jack"], note="Michael speaks to us (told, not shown). (p. 43)"),
            dict(note="He tells us: Jack was sent home “not because his mind was confused”"),
            dict(note="He tells us: Kate lost her job, “more to do with Father Jack”"),
            dict(note="He tells us: Rose and Agnes will leave (told, not shown)"),
            dict(dit=["Michael", "… one morning in early September both Rose and Agnes would have left for ever."]),
            dict(note="JACK picks up two pieces of wood, portions of the kites, and strikes them together. (p. 44)"),
            dict(act={"Jack": "voute"}, note="JACK begins to shuffle-dance in time to his tattoo"),
            dict(pos={"Kate": [705, 350]}, eclaire=["Michael", "Jack", "Kate"], duree=3.0,
                 note="KATE comes out to the garden and stands still, watching him."),
            dict(pos={"Rose": [560, 340], "Agnes": [590, 300], "Maggie": "fenetre"}, act={"Chris": "fige"},
                 eclaire=["Michael", "Jack", "Kate", "Chris"],
                 note="Only CHRIS has her eyes closed, her face raised, her mouth slightly open; remembering."),
            dict(note="He tells us: Gerry came back “in a couple of weeks” (told, not shown)"),
            dict(note="“No singing, no melody, no words.” (Michael, told, not shown)"),
            dict(note="He tells us: Gerry went to fight with “the International Brigade”"),
            dict(pos={"Kate": [566, 424]}, duree=2.0, eclaire=["Michael", "Jack", "Kate"], lumiere=None,
                 act={"Jack": "debout"}, note="KATE gently takes the sticks from him and places them on the ground."),
            dict(dit=["Kate", "We'll leave these back where we found them, Jack. They aren't ours. They belong to the child."]),
            dict(pos={"Kate": [1110, 330], "Jack": [1110, 300]}, duree=6.0,
                 note="(She takes his arm and leads him off.) “Now we'll go for our walk.”"),
            dict(pos={"Kate": "off", "Jack": "off"}, lumiere="spot", eclaire=[],
                 note="(The others watch with expressionless faces.) BLACKOUT"),
        ]),
    }),

    # ------------------------------------------------------------------ V. répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="Kate's “hair cracks”, Jack's “Ceremony!”, Michael's “for ever”, Kate's “They belong to the child.”", beats=[
        "{quatre}Four lines close Act One. Know them by heart.",
        "First, Kate.{-quatre}",
        ("C", "suddenly you realize that hair cracks are appearing everywhere; that control is slipping away; that the whole "
              "thing is so fragile that it can't be held together much longer.", "c_cracks", {"voix": "F"}),
        "{-c_cracks}{breche}Hair cracks: tiny lines, almost invisible, until the day everything breaks. "
        "{breche.1}It is Michael's widening breach from Part One. {breche.2}But now a character feels it, "
        "and it is Kate, the voice of duty and good order.",
        "Then Jack.{-breche}",
        ("C", "Ceremony! That's the word! How could I have forgotten that? The offering, the ritual, the dancing – a ceremony!",
         "c_ceremony"),
        "{-c_ceremony}{langue}The priest forgets simple English words, but remembers the pagan ceremony perfectly. "
        "The missionary has been converted by the people he went to convert.",
        "Then Michael.{-langue}",
        ("C", "the home would break up quite so quickly and that when she would wake up one morning in early September "
              "both Rose and Agnes would have left for ever.", "c_forever"),
        "{-c_forever}{forever}A prolepsis: the ending, told in the middle. From now on, we watch with tragic knowledge.",
        "And Kate, last of all.{-forever}",
        ("C", "We'll leave these back where we found them, Jack. They aren't ours. They belong to the child.", "c_child",
         {"voix": "F"}),
        "{-c_child}{fin}Kate puts the pagan rhythm back in its place, a child's game. "
        "But we already know her order will not hold.",
    ], vis={
        "quatre": dict(type="mot", t="Four lines to know", g="Kate · Jack · Michael · Kate · pages 37 – 44", y=250, taille=80),
        "c_cracks": dict(type="cit", a="Kate", o="p. 37", x=170, y=180, w=940),
        "breche": dict(type="illu", nom="breche", x=140, y=110, w=1000, h=440),
        "c_ceremony": dict(type="cit", a="Jack", o="p. 42", x=170, y=190, w=940),
        "langue": dict(type="note", cles=["ceremony", "converted"], terme="Jack · p. 42",
                       t="He loses the word, then finds it by chance: the governor's “ceremonial hat”.",
                       etape="The missionary converted by Ryanga.", x=170, y=200, w=940),
        "c_forever": dict(type="cit", a="Michael", o="p. 43", x=170, y=190, w=940),
        "forever": dict(type="note", cles=["prolepsis", "tragic"], terme="Michael · p. 43",
                        t="The ending, told in the middle: a prolepsis.",
                        etape="We watch Act Two with tragic knowledge.", x=170, y=200, w=940),
        "c_child": dict(type="cit", a="Kate", o="p. 44", x=170, y=200, w=940),
        "fin": dict(type="note", cles=["expressionless", "Blackout"], terme="End of Act One · p. 44",
                    t="“The others watch with expressionless faces.” Blackout.",
                    etape="Order restored for now… but we know it will not hold.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Act One ends on cracks: Kate's order, the family's future, words themselves. And we already know the end.", beats=[
        "{a1}Now the analysis: four ideas that close Act One. "
        "{a1.1}One: Kate's authority is cracking. Money, the Church, scandal, Rose's future: everything threatens the house, "
        "and the woman of good order admits that control is slipping away.",
        "{-a1}{a2}{a2.1}Two: pagan against Catholic. The missionary sent to convert Africa has been converted himself. "
        "This blending of beliefs is called syncretism; the colonial commissioner calls it going native. "
        "And Ryanga's goat echoes the Lughnasa bonfire in the back hills of Donegal.",
        "{-a2}{a3}{a3.1}Three: language fails. Jack loses his words, Maggie suggests dance, Gerry and Chris dance with no words. "
        "What matters most is said by the body.",
        "{-a3}{a4}{a4.1}Four, Friel's masterstroke: the ending comes in the middle. "
        "This prolepsis gives us tragic knowledge. We watch Act Two already knowing that the home will break up. "
        "The question is no longer what will happen, but how.",
        "{-a4}{carte}Here is Act One for your essay. {carte.1}The cracks. {carte.2}Pagan against Catholic. "
        "{carte.3}Language and dance. {carte.4}And memory: a narrator who already knows the end.",
    ], vis={
        "a1": dict(type="note", cles=["cracks", "slipping"], terme="1 · Kate's authority cracking",
                   t="“hair cracks are appearing everywhere”: duty, faith and order no longer hold.",
                   etape="The fragility of the household: her job, the Church, Jack, Rose.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["syncretism", "native"], terme="2 · Pagan / Catholic",
                   t="The missionary now speaks of “the ancestral spirits” and a “ceremony”.",
                   etape="Syncretism; “going native”; Ryanga echoes the Lughnasa fires.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["words", "body"], terme="3 · When words fail",
                   t="Jack's lost words; “Or dance.”; “No singing, no melody, no words.”",
                   etape="Dance and ritual say what language cannot.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["prolepsis", "tragic"], terme="4 · The ending in the middle",
                   t="“both Rose and Agnes would have left for ever”: a prolepsis at the end of Act One.",
                   etape="Tragic knowledge: we watch Act Two already knowing.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="ACT ONE", branches=[
            dict(t="Cracks", items=["“hair cracks … everywhere”", "job, Church, Jack, Rose", "“a righteous bitch”"]),
            dict(t="Pagan / Catholic", items=["“the ancestral spirits”", "“Ceremony!”", "the Lughnasa bonfire"]),
            dict(t="Language", items=["Jack's lost words", "“Or dance.”", "“no words”"]),
            dict(t="Memory", items=["prolepsis: “for ever”", "tragic knowledge", "the ending in the middle"])]),
    }),
]

QUIZ = [
    dict(q="What does Kate say is “appearing everywhere”?",
         r=["Hair cracks", "Pagan songs", "Strangers from the back hills", "Love-children"], ok=0, voir="c_cracks",
         ex="“hair cracks are appearing everywhere; that control is slipping away”: Kate feels the household is about to collapse."),
    dict(q="What worries Kate “most of all”?",
         r=["What would become of Rose", "Gerry's new job", "The broken wireless", "Jack's malaria"], ok=0, voir="jeu1.14",
         ex="“If I died – if I lost my job – if this house were broken up – what would become of our Rosie?”"),
    dict(q="Why does Kate react so strongly to Jack's question about their mother?",
         r=["He talks as if Mother should have believed in “the ancestral spirits”", "He says she never loved them",
            "He forgets her name", "He says she was not Catholic"], ok=0, voir="jeu3.3",
         ex="Kate answers that Mother “knew she was going straight to heaven”: Ryanga's spirits against Donegal's Catholic heaven."),
    dict(q="Which word does Jack finally remember?",
         r=["Ceremony", "Photograph", "Sacrifice", "Spectacle"], ok=0, voir="c_ceremony",
         ex="“Ceremony! That's the word!”: he forgets simple English words but remembers the pagan ritual perfectly."),
    dict(q="According to Michael, why did Kate really lose her job?",
         r=["It had more to do with Father Jack than with falling numbers", "The school closed", "She left to look after Rose",
            "Gerry Evans complained about her"], ok=0, voir="jeu4.2",
         ex="The parish priest spoke of falling numbers; Michael reveals that Jack was the real reason."),
    dict(q="What does Michael reveal at the end of Act One?",
         r=["In early September, Rose and Agnes will have left for ever", "Gerry will marry Chris in church",
            "Jack will go back to Ryanga", "Kate will open a new school"], ok=0, voir="c_forever",
         ex="A prolepsis: the ending is given in the middle, so we watch Act Two with tragic knowledge."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
