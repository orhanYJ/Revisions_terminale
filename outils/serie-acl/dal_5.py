"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 5 : la danse (PDF de travail, p. 22-25).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu : cuisine, jardin, Marconi), en suivant les didascalies pas à pas ;
les répliques courtes s'affichent en bulles et sont lues par la voix des sœurs ; la danse se fait sur un reel original
(humeur « reel », coupure nette au repère coupe). Puis trois didascalies expliquées et l'analyse.

Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_5.
De la mise en marche de Marconi (« The Mason's Apron ») à l'arrivée annoncée par Maggie (« Look who's coming up the lane! »,
p. 25) : la longue didascalie de la danse, puis la gêne et la querelle (l'argent des gants, « two unpaid servants »).
Citations courtes, à fin d'analyse ; la didascalie n'est citée que par brèves expressions, le reste est résumé.
Ce qui ne vient pas du texte (Ginger Rogers, la marque Woodbine, le surplis) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-5"
NOTION = "Dancing at Lughnasa"
NUM = 5
TITRE = "The dance"
SUIVANT = "Part 6 · Gerry Evans"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "ceili": "kaylee", "Yaaaah": "Yaaah", "Ardstraw": "Ard-straw",
                 "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rad}{q1}A radio crackles into life. A fast Irish reel fills the kitchen. "
        "And five women who were ironing, knitting and baking a moment ago… start to dance.",
        "{-q1}{fameux}This is the most famous scene of Dancing at Lughnasa. Almost no words are spoken, "
        "and yet it tells us everything about the Mundy sisters.",
        "{-fameux}Part five: the dance, and the quarrel that follows it.",
        ("P", 0.3),
        "{-tab_rad}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Five sisters, one radio, and a dance nobody can stop."),
        "fameux": dict(type="mot", t="Almost no words", g="the most famous scene of the play", y=270, taille=88),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 5", t="The dance",
                      sous="Marconi, the reel, the quarrel · pages 22 – 25"),
    }),

    # ------------------------------------------------------------------ I. Marconi (la pièce jouée sur le plateau)
    dict(id="marconi", chap="Marconi comes back", fond="nuit", humeur="mystere", beats=[
        "{jeu1}Page twenty-two. Maggie has just told her sisters about the dance at Ardstraw, and the boy she lost to Bernie. "
        "Now she stands at the window, motionless, staring out, seeing nothing.",
        "The others drift back to their tasks. Rose and Agnes knit. Kate puts the groceries away. "
        "{jeu1.1}And Chris connects the new battery to the wireless.",
        ("C", "Is it working now, Christina?", "jeu1.2", {"voix": "F"}),
        "{jeu1.3}Chris switches the set on, and goes back to her ironing.",
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Maggie": "fenetre", "Rose": "tricot_r", "Agnes": "tricot_a", "Kate": "buffet", "Chris": "table"},
                 act={"Maggie": "fige", "Rose": "tricote", "Agnes": "tricote", "Kate": "range", "Chris": "debout"},
                 note="Maggie stands motionless, staring out of the window, seeing nothing. (p. 22)"),
            dict(pos={"Chris": "radio"}, act={"Chris": "range"}),
            dict(dit=["Kate", "Is it working now, Christina?"]),
            dict(pos={"Chris": "table"}, act={"Chris": "repasse"}, radio=True,
                 note="“The Mason's Apron”, played by a ceili band: very fast, very heavy beat, a raucous sound."),
        ]),
    }),

    # ------------------------------------------------------------------ II. la danse (même plateau, la radio joue)
    dict(id="danse", chap="The dance", fond="nuit", humeur="reel", carton=False, coupe="jeu2.13", beats=[
        "{jeu2}The music fills the kitchen. For about ten seconds, the women go on with their tasks.",
        ("P", 2.5),
        "{jeu2.1}Then Maggie turns round. Her head is cocked to the beat. She is breathing deeply, rapidly. "
        "Her face shows a look of defiance, of aggression: a crude mask of happiness.",
        "{jeu2.2}She spreads her fingers, white with flour, pulls her hands down her cheeks, and patterns her face with a mask.",
        ("C", "Yaaaah!", "jeu2.3", {"voix": "F"}),
        ("P", 1.5),
        ("C", "Come on! Come on!", "jeu2.4", {"voix": "F"}),
        ("P", 3.0),
        "{jeu2.5}Her sisters watch her. Then Rose's face lights up. She flings away her knitting, leaps to her feet "
        "and grabs Maggie's hand. Her Wellingtons pound out their own erratic rhythm.",
        ("P", 2.5),
        "{jeu2.6}Agnes joins them. Of all the sisters, she moves most gracefully, most sensuously.",
        ("P", 2.0),
        "{jeu2.7}Then Chris, who has been folding Jack's surplice, tosses it over her head, and joins in.",
        ("C", "Oh, Christina –!", "jeu2.8", {"voix": "F"}),
        "{jeu2.9}But Kate's protest is drowned. The four sisters meet, retreat, form a circle and wheel round and round. "
        "The sound is too loud, the beat too fast, the dance almost grotesque.",
        ("P", 3.0),
        "{jeu2.10}Kate has been watching, with unease, with alarm. Suddenly she leaps to her feet and flings her head back.",
        ("C", "Yaaaah!", "jeu2.11", {"voix": "F"}),
        "{jeu2.12}And Kate dances alone, totally concentrated, totally private: out to the garden, round the summer seat, "
        "and back into the kitchen. The others shout and sing. Kate makes no sound.",
        ("P", 4.0),
        "{jeu2.13}Then the music stops, abruptly, in mid-phrase. But they are making so much noise "
        "that they keep dancing for a few seconds.",
        "{jeu2.14}Kate notices, and stops. {jeu2.15}Then Agnes. {jeu2.16}Then Chris and Maggie. "
        "{jeu2.17}Now only Rose is dancing her graceless dance, by herself. {jeu2.18}Then she too stops.",
        ("P", 1.5),
        "{jeu2.19}Silence. Only their gasping, and short bursts of static from the radio. They look at each other, "
        "half smile in embarrassment: slightly ashamed, and slightly defiant.",
        ("P", 1.5),
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Maggie": "fenetre", "Rose": "tricot_r", "Agnes": "tricot_a", "Kate": "buffet", "Chris": "table"},
                 act={"Maggie": "fige", "Rose": "tricote", "Agnes": "tricote", "Kate": "range", "Chris": "repasse"}, radio=True),
            dict(pos={"Maggie": [292, 300]}, act={"Maggie": "halete", "Kate": "assis"}, note="“a crude mask of happiness” (p. 22)"),
            dict(masque=["Maggie"], note="She patterns her face with flour: a white mask."),
            dict(pos={"Maggie": "centre"}, act={"Maggie": "danse"}, dit=["Maggie", "Yaaaah!"]),
            dict(dit=["Maggie", "Come on! Come on!"], note="“a white-faced, frantic dervish”"),
            dict(pos={"Rose": [270, 430], "Maggie": [330, 420]}, act={"Rose": "danse_lourde"}),
            dict(pos={"Agnes": [410, 400]}, act={"Agnes": "danse_douce"}),
            dict(pos={"Chris": [250, 400]}, act={"Chris": "danse"}, surplis=["Chris"], note="Jack's surplice over her head"),
            dict(dit=["Kate", "Oh, Christina –!"]),
            dict(ronde=["Maggie", "Rose", "Agnes", "Chris"], note="They meet, retreat, form a circle and wheel round and round."),
            dict(act={"Kate": "debout"}, note="Kate has been watching “with unease, with alarm”"),
            dict(dit=["Kate", "Yaaaah!"], act={"Kate": "seule"},
                 chemin={"Kate": ["buffet", "porte", "jardin", [930, 400], [880, 300], [740, 330], "porte", [200, 380]]},
                 chemin_duree=16, cam="tout", note="“totally concentrated, totally private” (p. 23)"),
            dict(note="Kate makes no sound."),
            dict(pos={"Kate": [200, 380]}, radio=False, cam="cuisine", note="The music stops abruptly in mid-phrase."),
            dict(act={"Kate": "halete"}),
            dict(ronde=["Maggie", "Rose", "Chris"], pos={"Agnes": [440, 455]}, act={"Agnes": "halete"}),
            dict(ronde=["Rose"], pos={"Chris": [250, 470], "Maggie": [380, 380]}, act={"Chris": "halete", "Maggie": "halete"}),
            dict(note="Only Rose is dancing, her graceless dance, by herself."),
            dict(ronde=None, pos={"Rose": [330, 430]}, act={"Rose": "halete"}),
            dict(radio="parasites", note="slightly ashamed and slightly defiant"),
        ]),
    }),

    # ------------------------------------------------------------------ III. la querelle
    dict(id="querelle", chap="The quarrel", fond="nuit", humeur="tension", beats=[
        "{jeu3}Chris moves first. She goes to the radio.",
        ("C", "It's away again, that aul thing.", "jeu3.1", {"voix": "F"}),
        "{jeu3.2}It is roasting hot. She turns it off, and slaps it.",
        ("C", "Bloody useless set, that.", "jeu3.3", {"voix": "F"}),
        ("C", "No need for corner-boy language, Christina.", "jeu3.4", {"voix": "F"}),
        "{jeu3.5}Kate is back in charge. She picks on Rose's Wellingtons, and Rose answers that she has only her Wellingtons "
        "and her Sunday shoes. Maggie lights a cigarette.",
        ("C", "I'll tell you something, girls: this Ginger Rogers has seen better days.", "jeu3.6", {"voix": "F"}),
        "{jeu3.7}Kate sends her to wash her face. Yes, miss, says Maggie. At the window, she notices that the boy has gone "
        "from the garden. Chris snaps: leave him alone for once. Maggie shrugs, and goes out the back door.",
        ("C", "Please take that surplice off, Christina.", "jeu3.8", {"voix": "F"}),
        "{jeu3.9}Chris wants to throw the wireless out. Agnes agrees: it's junk. And Kate turns on Agnes.",
        ("C", "You'll buy it out of your glove money, will you?", "jeu3.10", {"voix": "F"}),
        ("C", "This isn't your classroom, Kate.", "jeu3.11", {"voix": "F"}),
        "{jeu3.12}Agnes lists everything she and Rose do: every meal, every stitch of clothes, the shoes, the beds, "
        "the house, the chimney, the grass, the turf.",
        ("C", "What you have here, Kate, are two unpaid servants.", "jeu3.13", {"voix": "F"}),
        ("C", "The Gander! Everybody calls you the Gander!", "jeu3.14", {"voix": "F"}),
        "{jeu3.15}And at that moment, Maggie runs back in, straight to the window.",
        ("C", "Look who's coming up the lane!", "jeu3.16", {"voix": "F"}),
        "Who it is, we will see in part six.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Kate": [200, 380], "Maggie": [380, 380], "Agnes": [440, 455], "Chris": [250, 470], "Rose": [330, 430]},
                 act={"Kate": "halete", "Maggie": "halete", "Agnes": "halete", "Chris": "halete", "Rose": "halete"},
                 masque=["Maggie"], surplis=["Chris"], radio="parasites"),
            dict(pos={"Chris": "radio"}, act={"Chris": "debout"}, dit=["Chris", "It's away again, that aul thing."]),
            dict(radio=False, act={"Chris": "range"}),
            dict(dit=["Chris", "Bloody useless set, that."], act={"Chris": "debout"}),
            dict(dit=["Kate", "No need for corner-boy language, Christina."], act={"Kate": "debout"}),
            dict(note="“Are Wellingtons absolutely necessary on a day like this, Rose?” (p. 24)", act={"Maggie": "debout", "Rose": "debout", "Agnes": "debout"}),
            dict(dit=["Maggie", "I'll tell you something, girls: this Ginger Rogers has seen better days."]),
            dict(pos={"Maggie": "fenetre"}, note="“Yes, miss.” … “Just leave him alone for once, will you, please?”"),
            dict(pos={"Maggie": "off"}, dit=["Kate", "Please take that surplice off, Christina."]),
            dict(pos={"Kate": [260, 400], "Agnes": [420, 410]}, note="“It's junk, that set.”"),
            dict(dit=["Kate", "You'll buy it out of your glove money, will you?"]),
            dict(dit=["Agnes", "This isn't your classroom, Kate."]),
            dict(note="Every meal, every stitch of clothes, the shoes, the beds, the chimney, the grass, the turf…"),
            dict(dit=["Agnes", "What you have here, Kate, are two unpaid servants."]),
            dict(dit=["Rose", "The Gander! Everybody calls you the Gander!"]),
            dict(pos={"Maggie": "fenetre"}, act={"Maggie": "debout"}),
            dict(dit=["Maggie", "Look who's coming up the lane!"], note="(p. 25)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. trois didascalies à connaître
    dict(id="didascalies", chap="Three stage directions", fond="aube", humeur="calme",
         retenir="Maggie's “mask of happiness”, Kate's “controlled and frantic” dance, “order being consciously subverted”.", beats=[
        "{trois}In this scene, almost nothing is said. The stage directions are the text. Three of them are worth knowing by heart.",
        "{-trois}First, Maggie.",
        ("C", "a look of defiance, of aggression; a crude mask of happiness.", "c_mask"),
        "{-c_mask}{mask}A mask of happiness, not happiness itself. The joker of the house performs joy, and the flour on her face makes the mask visible.",
        "{-mask}Then Kate.",
        ("C", "KATE dances alone, totally concentrated, totally private; a moment that is simultaneously controlled and frantic",
         "c_kate"),
        "{-c_kate}{kate}Controlled and frantic: an oxymoron. The guardian of order lets go, but in silence, alone, as if she could not share it. "
        "Friel adds that her dance is out of character, and ominous of some deep and true emotion.",
        "{-kate}And the meaning of the whole scene.",
        ("C", "there is a sense of order being consciously subverted, of the women consciously and crudely caricaturing themselves",
         "c_order"),
        "{-c_order}{order}To subvert is to overturn from the inside. Consciously, twice: the sisters know what they are doing. "
        "They mock their own respectable lives, to the point of near-hysteria.",
    ], vis={
        "trois": dict(type="mot", t="The stage directions are the text", g="three to know by heart · pp. 22 – 23", y=250, taille=72),
        "c_mask": dict(type="cit", a="Stage direction", o="p. 22", x=170, y=200, w=940),
        "mask": dict(type="note", cles=["mask", "performs"], terme="Maggie · p. 22",
                     t="A mask of happiness, not happiness itself: the joker performs joy.",
                     etape="The flour makes the mask visible.", x=170, y=200, w=940),
        "c_kate": dict(type="cit", a="Stage direction", o="p. 23", x=170, y=170, w=940),
        "kate": dict(type="note", cles=["oxymoron", "silence"], terme="Kate · p. 23",
                     t="“controlled and frantic”: an oxymoron. The guardian of order lets go, in silence, alone.",
                     etape="“out of character”, yet “ominous of some deep and true emotion”.", x=170, y=200, w=940),
        "c_order": dict(type="cit", a="Stage direction", o="p. 23", x=170, y=170, w=940),
        "order": dict(type="note", cles=["subvert", "consciously"], terme="The meaning of the dance · p. 23",
                      t="To subvert: to overturn an order from the inside. The sisters mock their own respectable lives.",
                      etape="A deliberate revolt, “near-hysteria”.", x=170, y=200, w=940),
    }),

    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="A language beyond words, pagan against Christian, order subverted, joy followed by conflict.", beats=[
        "{a1}Now the analysis. Four ideas for your essay. "
        "{a1.1}One: a language beyond words. The scene exists almost only as a stage direction: this is non-verbal theatre. "
        "The sisters say with their bodies what they can never say aloud: frustration, desire, anger. "
        "And Kate, who controls every word, dances in silence. At the very end, Michael will remember dancing "
        "as if language had surrendered to movement. This is where we first see it.",
        "{-a1}{a2}{a2.1}Two: pagan against Christian. At Lughnasa, the dance is a wild, almost Dionysian release. "
        "The surplice turns the Church into a costume. And even Kate, the guardian of Catholic order, dances: alone, and in silence.",
        "{-a2}{a3}{a3.1}Three: order subverted, then restored. The revolt is self-mocking: parody, caricature. "
        "It is brief. Then come embarrassment and Kate's rebukes. A catharsis, a release of feelings, but no escape.",
        "{-a3}{a4}{a4.1}Four: juxtaposition. Right after the joy comes the quarrel: money, work, power. "
        "Two unpaid servants, the Gander. The family is cracking, as Michael feared.",
        "{-a4}{carte}So, in an essay, this scene can support: {carte.1}dance as release and language, "
        "{carte.2}pagan against Christian, {carte.3}order and subversion, {carte.4}and the sisters' frustrated lives.",
    ], vis={
        "a1": dict(type="note", cles=["beyond", "silence"], terme="1 · A language beyond words",
                   t="Non-verbal theatre: the stage direction is the text; the bodies speak. Kate dances in silence.",
                   etape="Final monologue: “as if language had surrendered to movement”.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["pagan", "surplice"], terme="2 · Pagan / Christian",
                   t="A Dionysian release at Lughnasa; the surplice as a costume; Kate's own “Yaaaah!”.",
                   etape="The pagan breaks into the Catholic house.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["subverted", "restored"], terme="3 · Order subverted, then restored",
                   t="“order being consciously subverted”: parody, caricature, near-hysteria… then embarrassment.",
                   etape="A brief catharsis, not an escape.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["quarrel", "money"], terme="4 · Juxtaposition",
                   t="The dance, then the quarrel: “two unpaid servants”, “the Gander”.",
                   etape="Joy hides the tensions only for a moment.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE DANCE", branches=[
            dict(t="Release", items=["non-verbal theatre", "“Yaaaah!”", "Kate's silence"]),
            dict(t="Pagan / Christian", items=["Lughnasa", "the surplice", "“Marconi's voodoo”"]),
            dict(t="Order", items=["“consciously subverted”", "parody, caricature", "embarrassment"]),
            dict(t="Frustrated lives", items=["“wild man”", "“two unpaid servants”", "“the Gander”"])]),
    }),
]

QUIZ = [
    dict(q="What music comes out of Marconi?",
         r=["“The Mason's Apron”, an Irish reel played by a ceili band", "A slow Irish ballad", "Cole Porter's “Anything Goes”",
            "Church music from Dublin"], ok=0, voir="jeu1.3",
         ex="Friel describes it as very fast, with a very heavy beat and a raucous sound: the beat first, then the melody."),
    dict(q="What does Maggie do to her face before she dances?",
         r=["She patterns it with flour, like a mask", "She covers it with her apron", "She paints it with ink",
            "She hides it in her hands and cries"], ok=0, voir="jeu2.2",
         ex="Her hands are covered with flour: “a crude mask of happiness”, then a “white-faced, frantic dervish”."),
    dict(q="Why is Chris dancing with Jack's surplice over her head so shocking?",
         r=["A priest's sacred vestment becomes a carnival costume", "Because it belongs to Gerry", "Because it is Kate's best dress",
            "Because it is dirty"], ok=0, voir="jeu2.7",
         ex="Kate cries “Oh, Christina!”: the Church's garment is turned into a costume in a pagan dance, a kind of sacrilege."),
    dict(q="How does Kate dance?",
         r=["Alone, silent, “simultaneously controlled and frantic”", "With Rose, laughing", "She refuses to dance",
            "Holding Agnes by the waist"], ok=0, voir="c_kate",
         ex="She dances “totally private”, out of character; while the others call and sing, she “makes no sound”."),
    dict(q="According to the stage direction, the dance gives “a sense of order being…”",
         r=["consciously subverted", "slowly restored", "politely respected", "secretly rewritten"], ok=0, voir="c_order",
         ex="The sisters “consciously and crudely” caricature themselves: a deliberate revolt, close to “near-hysteria”."),
    dict(q="What does Agnes mean by “two unpaid servants”?",
         r=["She and Rose do all the housework without being thanked or paid", "Kate employs two maids",
            "Rose and Michael work for Gerry", "The priests of Ryanga"], ok=0, voir="jeu3.13",
         ex="Kate attacks the “glove money”; Agnes replies with all the meals, clothes, shoes and beds she and Rose take care of."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
