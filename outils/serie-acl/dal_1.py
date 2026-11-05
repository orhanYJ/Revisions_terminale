"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 1 : le monologue d'ouverture (PDF de travail, p. 1-2).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés sur le plateau) :
la didascalie d'ouverture est jouée pas à pas (visuel jeu : Michael seul dans un cercle de lumière, puis le tableau figé,
chacun à la place que donne le texte : Maggie à la fenêtre, Chris à la porte, Kate à l'extrême droite du plateau, Rose et
Gerry sur le banc du jardin, Jack à côté de Rose, Agnes au fond à gauche) ; Jack porte l'uniforme blanc d'aumônier
(p. 72 : « a version of the uniform we saw him in at the very beginning of the play »). Les souvenirs de Michael sont
racontés, pas joués : les personnages restent figés, ses phrases courtes s'affichent en bulles. Puis cinq répliques
expliquées et l'analyse.

Vidéo en anglais (l'essay se rédige en anglais), même chaîne que les séries philo : outils/serie-philo/generer.py dal_1.
Citations courtes, à fin d'analyse (droit d'auteur : le texte de Friel n'est pas reproduit dans le site).
Ce qui ne vient pas du texte (contexte, création de la pièce) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-1"
NOTION = "Dancing at Lughnasa"
NUM = 1
TITRE = "The memory begins"
SUIVANT = "Part 2 · An August afternoon in the kitchen"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Glenties": "Glen-cheese",
                 "Athlone": "Ath-lone", "Mundy": "Mundy"}

PERSOS = ["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack", "Gerry", "Michael"]
# le tableau de la p. 1 (vu de la salle : « stage left » est à droite de l'écran, « stage right » à gauche)
MICHAEL = [1000, 552]   # « downstage left » : au bord du plateau, à droite vu de la salle
TABLEAU = {"Michael": MICHAEL, "Maggie": "fenetre", "Chris": "porte", "Kate": [150, 455],
           "Rose": "banc_g", "Gerry": "banc_d", "Jack": [762, 362], "Agnes": [925, 238]}
FIGES = {"Michael": "debout", "Maggie": "fige", "Chris": "fige", "Kate": "fige", "Rose": "assis", "Gerry": "assis",
         "Jack": "fige", "Agnes": "fige"}
JACK = dict(costume={"Jack": "blanc"}, chapeau={"Jack": "aucun"})
# état de départ des chapitres où Michael parle devant le tableau figé
FIGE = dict(pos=TABLEAU, act=FIGES, lumiere="sombre", cam="tout", **JACK)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}A man stands alone in a pool of light. Behind him, in the dark, seven people are standing perfectly still. "
        "He turns to us, and he starts to remember.",
        "{-q1}That is how Dancing at Lughnasa begins. Before a single character speaks to another, "
        "the play tells us one thing: everything we are about to see is a memory.",
        "{-tab_don}{serie}In this series, the play is performed on a small stage, scene by scene, as Friel's text sets it out. "
        "Then the key lines, and the analysis for your essay. Part one: the opening monologue.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Everything we are about to see is a memory."),
        "serie": dict(type="mot", t="Scene by scene", g="the play performed · the key quotations · the analysis", y=270, taille=88),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 1", t="The memory begins",
                      sous="Michael's opening monologue · pages 1 – 2"),
    }),

    # ------------------------------------------------------------------ I. avant le rideau
    dict(id="contexte", chap="Before the curtain", fond="aube", humeur="lumiere",
         retenir="Friel, 1990. A memory play set in August 1936, in a Donegal cottage: five sisters, a priest, a child.", beats=[
        "{tab_fri}{fiche}First, the essentials. Dancing at Lughnasa is a play by the Irish writer Brian Friel. "
        "{-tab_fri}{tab_abb}{fiche.1}It was first staged in 1990, at the Abbey Theatre in Dublin.",
        "{fiche.2}But it is set more than fifty years earlier: in August 1936, in and around a cottage near Ballybeg, "
        "a small village in County Donegal, in the north-west of Ireland.",
        "{-fiche}{-tab_abb}{lug}And the title? {lug.1}Lughnasa is the old Celtic harvest festival, held at the start of August, "
        "in honour of the pagan god Lugh. Keep that word pagan in mind: it will come back, again and again.",
    ], vis={
        "tab_fri": dict(type="tableau", img="dal-friel-statue", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .4],
                        legende="Brian Friel and John B. Keane, sculpture in Dublin (photo Spleodrach, CC BY-SA 4.0)"),
        "tab_abb": dict(type="tableau", img="dal-abbey", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                        legende="The Abbey Theatre, Dublin (photo bjaglin, CC BY 2.0)"),
        "fiche": dict(type="liste", titre="Dancing at Lughnasa · Brian Friel", items=[
            "First staged in 1990, Abbey Theatre, Dublin",
            "Set in August 1936, near Ballybeg, County Donegal"], marques=["1990", "1936"], x=170, y=200, w=940),
        "lug": dict(type="def", cles=["harvest", "pagan"], terme="Lughnasa",
                    t="The old Celtic harvest festival, at the start of August, in honour of the pagan god Lugh.",
                    etape="A pagan word in a Catholic house: the tension starts with the title.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. le cercle de lumière et le tableau (p. 1)
    dict(id="plateau", chap="A pool of light", fond="nuit", humeur="mystere",
         retenir="The play opens on a frozen tableau: we meet the characters as images in Michael's mind.", beats=[
        "{jeu1}Page one. The stage is dark. Downstage left, Michael stands alone, in a pool of light: "
        "the boy of 1936, grown up.",
        "{jeu1.1}As he begins to speak, the lights come up slowly on the rest of the stage. "
        "{jeu1.2}The other characters stand motionless, in a formal tableau.",
        "{jeu1.3}In the kitchen, Maggie is at the window. Chris is at the front door. "
        "And Kate, the eldest, stands at the extreme edge of the stage.",
        "{jeu1.4}In the garden, Rose and Gerry Evans, Michael's father, sit on the garden seat. Jack, the sisters' brother, "
        "stands beside Rose. {jeu1.5}He wears a white uniform: we learn it only at the end of the play, "
        "when he comes back in a soiled version of the uniform we saw him in at the very beginning.",
        "{jeu1.6}And Agnes stands upstage, at the back. {jeu1.7}They hold these positions the whole time Michael talks to the audience.",
        ("C", "When I cast my mind back to that summer of 1936 different kinds of memories offer themselves to me.", "jeu1.8"),
        ("P", 0.8),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Michael": MICHAEL}, act={"Michael": "debout"}, lumiere="spot", cam="michael", **JACK,
                 note="“MICHAEL is standing downstage left in a pool of light.” (p. 1)"),
            dict(pos=TABLEAU, act=FIGES, duree=3.5, lumiere="sombre", cam="tout",
                 note="“slowly bring up the lights on the rest of the stage”"),
            dict(note="“the other characters stand motionless in formal tableau”"),
            dict(cam="cuisine", note="Maggie at the kitchen window. Chris at the front door. Kate at extreme stage right."),
            dict(cam="jardin", note="Rose and Gerry sit on the garden seat. Jack stands beside Rose."),
            dict(note="Jack's white uniform (p. 72: “the uniform we saw him in at the very beginning”)"),
            dict(cam="tout", note="Agnes is upstage left."),
            dict(note="“They hold these positions while MICHAEL talks to the audience.”"),
            dict(cam="tout", dit=["Michael", "When I cast my mind back to that summer of 1936… memories offer themselves to me."]),
        ]),
    }),

    # ------------------------------------------------------------------ III. deux souvenirs : Marconi et Jack (p. 1)
    dict(id="souvenirs", chap="Two memories", fond="nuit", humeur="lumiere",
         retenir="The wireless (Marconi) and Jack's return: two memories of summer 1936, always linked.", beats=[
        "{jeu2}Michael speaks. Behind him, nobody moves: everything he describes is told, not shown. "
        "His first memory is the wireless.",
        ("C", "We got our first wireless set that summer – well, a sort of set; and it obsessed us.", "jeu2.1"),
        "{jeu2.2}Maggie, the joker of the family, wanted to give the set a name: Lugh, after the old Celtic god of the harvest. "
        "{jeu2.3}But Kate, a national schoolteacher and a very proper woman, said no: it would be sinful, "
        "not to talk of a pagan god.",
        ("C", "So we just called it Marconi because that was the name emblazoned on the set.", "jeu2.4"),
        "{jeu2.5}The second memory: three weeks before the wireless, his Uncle Jack, his mother's brother, "
        "came home from Africa for the first time ever.",
        "{jeu2.6}For twenty-five years he had worked in a leper colony in Ryanga, in Uganda, "
        "leaving it only once, as a chaplain to the British army in the First World War.",
        ("C", "And now in his early fifties and in bad health he had come home to Ballybeg – as it turned out – to die.", "jeu2.7"),
        ("P", 0.8),
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(**FIGE, note="Michael's memories are told, not acted: the tableau stays frozen."),
            dict(cam="tout", dit=["Michael", "We got our first wireless set that summer – well, a sort of set; and it obsessed us."]),
            dict(cam="tout", note="He tells us: Maggie wanted to call the set Lugh, the pagan god of the harvest."),
            dict(note="Kate: “it would be sinful to christen an inanimate object with any kind of name” (p. 1)"),
            dict(cam="tout", dit=["Michael", "So we just called it Marconi because that was the name emblazoned on the set."]),
            dict(cam="tout", note="He tells us: Uncle Jack came home from Africa, “for the first time ever”."),
            dict(note="25 years in a leper colony in Ryanga, Uganda; a chaplain in East Africa in World War One."),
            dict(cam="tout", dit=["Michael", "…he had come home to Ballybeg – as it turned out – to die."]),
        ]),
    }),

    # ------------------------------------------------------------------ IV. toujours liés (p. 1)
    dict(id="lies", chap="Always linked", fond="nuit", humeur="tension",
         retenir="Michael's memory works by juxtaposition: the radio's joy always comes with Jack's decline.", beats=[
        "{jeu3}Now the key move of the monologue.",
        ("C", "these two memories – of our first wireless and of Father Jack's return – are always linked.", "jeu3.1"),
        "{jeu3.2}His shock at Jack's appearance {jeu3.3}comes back with his awe at the magic of the radio. "
        "{jeu3.4}And the kitchen throbbing with Irish dance music…",
        ("C", "my mother and her sisters suddenly catching hands and dancing a spontaneous step-dance", "jeu3.5"),
        ("C", "and laughing – screaming! – like excited schoolgirls", "jeu3.6"),
        "{jeu3.7}Look at the stage: the sisters do not dance. The dance is a memory; we will see it only on page twenty-two. "
        "{jeu3.8}And at the same time…",
        ("C", "that forlorn figure of Father Jack shuffling from room to room", "jeu3.9"),
        "{jeu3.10}…as if he were searching for something, but couldn't remember what.",
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(**FIGE),
            dict(cam="tout", dit=["Michael", "these two memories – of our first wireless and of Father Jack's return – are always linked."]),
            dict(cam="tout", note="Jack's appearance: “shrunken and jaundiced with malaria” (p. 1)"),
            dict(note="…and “the sheer magic of that radio”"),
            dict(note="“the kitchen throbbing with the beat of Irish dance music beamed to us all the way from Athlone”"),
            dict(cam="tout", dit=["Michael", "my mother and her sisters suddenly catching hands and dancing a spontaneous step-dance"]),
            dict(dit=["Michael", "and laughing – screaming! – like excited schoolgirls"]),
            dict(cam="tout", note="Told, not shown: the sisters do not move."),
            dict(cam="jardin", note="Jack, beside Rose, frozen in his white uniform."),
            dict(cam="tout", dit=["Michael", "that forlorn figure of Father Jack shuffling from room to room"]),
            dict(note="“as if he were searching for something but couldn't remember what”"),
        ]),
    }),

    # ------------------------------------------------------------------ V. la brèche, puis la lumière change (p. 2)
    dict(id="breche", chap="A widening breach", fond="nuit", humeur="tension",
         retenir="“A widening breach between what seemed to be and what was”: the play's subject in one phrase.", beats=[
        "{jeu4}Page two. Even though he was only a child of seven, Michael says, he had a sense of unease…",
        ("C", "some awareness of a widening breach between what seemed to be and what was", "jeu4.1"),
        "{jeu4.2}…of things changing too quickly. Three possible reasons. "
        "{jeu4.3}One: Uncle Jack was not the resplendent figure in his head. Two:",
        ("C", "Or maybe because I had witnessed Marconi's voodoo derange those kind, sensible women", "jeu4.4"),
        ("C", "and transform them into shrieking strangers.", "jeu4.5"),
        "{jeu4.6}Three: his father, Gerry Evans, visited twice, and for the first time Michael could observe him.",
        "{jeu4.7}The lighting changes: a warm summer afternoon.",
        "{jeu4.8}Michael, Kate, Gerry and Father Jack go off. {jeu4.9}Maggie, Chris, Rose and Agnes remain. "
        "The memory comes to life, and the play begins.",
        ("P", 1.5),
    ], vis={
        "jeu4": dict(type="jeu", persos=PERSOS, etats=[
            dict(**FIGE, note="“a sense of unease” (p. 2)"),
            dict(cam="tout", dit=["Michael", "…a widening breach between what seemed to be and what was"]),
            dict(note="“of things changing too quickly before my eyes”"),
            dict(cam="tout", note="1 · Jack is not “the resplendent figure in my head”."),
            dict(cam="tout", dit=["Michael", "Or maybe because I had witnessed Marconi's voodoo derange those kind, sensible women"]),
            dict(dit=["Michael", "and transform them into shrieking strangers."]),
            dict(cam="tout", note="3 · His father, Gerry Evans, visited twice: “I had a chance to observe him.”"),
            dict(lumiere=None, duree=3, note="“The kitchen and garden are now lit as for a warm summer afternoon.” (p. 2)"),
            dict(pos={"Michael": "off", "Kate": "off", "Gerry": "off", "Jack": "off"}, duree=2.2,
                 note="“MICHAEL, KATE, GERRY and FATHER JACK go off.”"),
            dict(cam="cuisine"),
        ]),
    }),

    # ------------------------------------------------------------------ VI. cinq répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="“sinful”, “as it turned out – to die”, “screaming!”, “a widening breach”.", beats=[
        "{cinq}In these two pages, Michael is the only one who speaks. Four of his lines are worth knowing by heart.",
        "{-cinq}First, the name of the radio.",
        ("C", "she said it would be sinful to christen an inanimate object with any kind of name, not to talk of a pagan god.",
         "c_sinful"),
        "{-c_sinful}{radio}A tiny family quarrel… but look at it closely. Maggie plays with the pagan. Kate stands guard for the Church. "
        "That conflict, in a single joke about a radio, is the conflict of the whole play.",
        "Second, Jack.{-radio}",
        ("C", "And now in his early fifties and in bad health he had come home to Ballybeg – as it turned out – to die.",
         "c_die"),
        "{-c_die}{die}Three small words: as it turned out. The adult Michael already knows the ending, and he gives it away "
        "in the first minute. The question will never be whether Jack dies, only how we watch him until then.",
        "Third, the dance he remembers.{-die}",
        ("C", "my mother and her sisters suddenly catching hands and dancing a spontaneous step-dance and laughing – screaming! – "
              "like excited schoolgirls", "c_dance"),
        "{-c_dance}{scream}Listen to the correction in the middle: laughing… no: screaming. Joy is already tipping into something wilder. "
        "And in the same breath, the forlorn figure of Jack: juxtaposition, the dance and the decline side by side.",
        "Fourth, the sentence you should know by heart.{-scream}",
        ("C", "some awareness of a widening breach between what seemed to be and what was, of things changing too quickly "
              "before my eyes, of becoming what they ought not to be.", "c_breach"),
        "{-c_breach}{breach}A breach is a gap, a crack. On the surface, the house seems stable: a family, a routine, a faith. "
        "Underneath, things are changing too quickly. The whole play lives in that gap between appearance and reality. "
        "Even inside the sisters: Marconi's voodoo, a word of magic and possession, turns kind, sensible women into shrieking strangers.",
    ], vis={
        "cinq": dict(type="mot", t="Michael is the only voice", g="four lines to know · pages 1 – 2", y=250, taille=80),
        "c_sinful": dict(type="cit", a="Michael, about Kate", o="p. 1", x=170, y=200, w=940),
        "radio": dict(type="cols", g="Maggie", gq="wants to call it Lugh, the pagan god", d="Kate",
                      dq="“sinful”: a Catholic refusal", vs="≠", repere="pagan / Christian"),
        "c_die": dict(type="cit", a="Michael", o="p. 1", x=170, y=200, w=940),
        "die": dict(type="note", cles=["prolepsis", "ending"], terme="Jack · p. 1",
                    t="“as it turned out”: the adult narrator gives the ending away in the first minute.",
                    etape="A prolepsis: we know Jack will die.", x=170, y=200, w=940),
        "c_dance": dict(type="cit", a="Michael", o="p. 1", x=170, y=170, w=940),
        "scream": dict(type="mot", t="laughing – screaming!", g="joy already tipping into something wilder", y=250, taille=84),
        "c_breach": dict(type="cit", a="Michael", o="p. 2", x=170, y=170, w=940),
        "breach": dict(type="illu", nom="breche", x=140, y=110, w=1000, h=440),
    }),

    # ------------------------------------------------------------------ VII. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Memory play, prolepsis, pagan / Christian, the dance as release: all four are set up on page 1.", beats=[
        "{a1}Now the analysis. Four ideas to take from these two pages. "
        "{a1.1}One: this is a memory play, told by a retrospective narrator. The adult Michael reconstructs the summer "
        "he lived as a child of seven. So we see the events through a double lens: a child who did not understand, "
        "and an adult who knows how it all ended.",
        "Michael even admits it: memories offer themselves to me. He selects, he arranges, like the frozen tableau behind him. "
        "In an essay on memory, this is your starting point: the play does not show the past, it shows remembering.",
        "{-a1}{a2}{a2.1}Two: prolepsis. As it turned out, to die. By giving away Jack's death in the first minute, "
        "Friel creates dramatic irony. We know more than the characters do. "
        "Every joke, every dance, every plan we see will be watched with that knowledge.",
        "{-a2}{a3}{a3.1}Three: the pagan and the Christian. Lugh against Kate's sinful. Marconi's voodoo against kind, sensible women. "
        "In a few lines, Friel sets up the play's central tension: an old pagan energy pressing against the rules of a Catholic house.",
        "{-a3}{a4}{a4.1}Four: the dance. The very first image of the sisters is a dance, and it is ambiguous. "
        "It is joy, laughing like schoolgirls… and it is loss of control, screaming, shrieking strangers. "
        "Dance in this play is a release, a way of saying what cannot be said, and a sign that order is cracking.",
        "{-a4}{carte}So, if you use this scene in an essay, here is what it can support. {carte.1}Memory and narration. "
        "{carte.2}The structure of the play, which ends almost where it began. {carte.3}Pagan against Christian. "
        "{carte.4}Change, and a world about to break.",
    ], vis={
        "a1": dict(type="note", cles=["retrospective", "double"], terme="1 · A memory play",
                   t="A retrospective narrator: the adult Michael reconstructs what the child lived.",
                   etape="Not the past itself, but the act of remembering.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["prolepsis", "irony"], terme="2 · Prolepsis",
                   t="“as it turned out – to die”: the ending is given at the start.",
                   etape="Dramatic irony: the audience knows more than the characters.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["pagan", "Catholic"], terme="3 · Pagan / Christian",
                   t="Lugh against “sinful”; “Marconi's voodoo” against “kind, sensible women”.",
                   etape="An old pagan energy pressing against a Catholic house.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["release", "cracking"], terme="4 · The dance",
                   t="Joy (“like excited schoolgirls”) and loss of control (“shrieking strangers”).",
                   etape="A release, and a sign that order is cracking.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE OPENING", branches=[
            dict(t="Memory", items=["“memories offer themselves”", "retrospective narrator", "child / adult"]),
            dict(t="Structure", items=["a frozen tableau", "prolepsis: “to die”", "the play comes full circle"]),
            dict(t="Pagan / Christian", items=["Lugh / “sinful”", "“Marconi's voodoo”"]),
            dict(t="Change", items=["“a widening breach”", "“things changing too quickly”"])]),
    }),
]

QUIZ = [
    dict(q="Where is Michael at the very start of the play?",
         r=["Downstage, alone in a pool of light", "In the kitchen, ironing with Chris", "In the garden, making kites",
            "Offstage: we only hear his voice"], ok=0, voir="jeu1.1",
         ex="The rest of the stage is dark; the other characters stand motionless in a “formal tableau” while he speaks to the audience."),
    dict(q="Why do they call the wireless “Marconi”?",
         r=["Because Kate refused to name it after the pagan god Lugh", "Because Jack brought it from Africa",
            "Because Gerry sold it to them", "Because Maggie loved Italian music"], ok=0, voir="c_sinful",
         ex="Maggie wanted to call it Lugh; Kate said it would be “sinful” to christen an object, let alone after a pagan god. So it kept its brand name."),
    dict(q="What does “as it turned out – to die” do to the audience?",
         r=["It creates dramatic irony: we know Jack's fate before the characters do", "It shows that Michael is lying",
            "It announces a comic ending", "It tells us Jack is already dead when the play starts"], ok=0, voir="c_die",
         ex="This is a prolepsis: the adult narrator gives away the ending, and we watch everything that follows with that knowledge."),
    dict(q="Which two memories are “always linked” in Michael's mind?",
         r=["The first wireless and Father Jack's return", "Lughnasa and Christmas", "His father and his mother",
            "The harvest dance and the kites"], ok=0, voir="jeu3.1",
         ex="The radio's “sheer magic” always comes back with Jack's shock appearance, “shrunken and jaundiced with malaria”: a juxtaposition."),
    dict(q="The “widening breach” is a gap between…",
         r=["what seemed to be and what was", "the kitchen and the garden", "Ireland and Africa", "Kate and Maggie"], ok=0,
         voir="c_breach", ex="Appearance against reality: on the surface a stable house, underneath “things changing too quickly”."),
    dict(q="Why does Michael use the word “voodoo” about the radio?",
         r=["It presents the music as a pagan, possessing force over the sisters", "Because the radio came from Haiti",
            "To mock Father Jack's religion", "Because the radio is broken"], ok=0, voir="jeu4.4",
         ex="“Marconi's voodoo” “derange[s]” the “kind, sensible women” into “shrieking strangers”: magic, possession, loss of control."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Brian Friel and John B. Keane, sculpture, Dublin (Spleodrach, CC BY-SA 4.0); Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Abbey Theatre exterior (bjaglin, CC BY 2.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
