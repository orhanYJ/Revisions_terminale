"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 3 : la fête des moissons (PDF de travail, p. 9-15).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés sur le plateau) :
la scène est jouée pas à pas d'après les didascalies (visuel jeu) : Kate entre par la gauche du plateau (à droite vu de la
salle), chargée de sacs, va au garçon (invisible : Michael adulte dit ses répliques), regarde les visages des cerfs-volants
que le public ne voit pas (cerfs-volants montrés sans visage), rentre dans la cuisine ; Michael sort ; Austin Morgan,
la colère de Kate ; elle s'effondre sur un siège ; Ballybeg « off its head », la quinine, Okawa ; Agnes cesse de tricoter,
« Wouldn't it be a good one if we all went? », l'élan, « I want to dance », la danse de Rose, la panique et le refus de
Kate, (Silence.). Arrêt juste avant le retour de Maggie (« The fox is back », p. 15). Les répliques courtes s'affichent
en bulles et sont lues par les voix des personnages ; puis cinq répliques expliquées et l'analyse.

Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_3.
Citations courtes, à fin d'analyse ; ce qui ne vient pas du texte est dit comme tel.
Coquilles du PDF non reproduites dans les citations (p. 14 : « love you more » lu « I love you more »).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-3"
NOTION = "Dancing at Lughnasa"
NUM = 3
TITRE = "The harvest dance"
SUIVANT = "Part 4 · Jack comes in"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Okawa": "Oh-kah-wa", "Carrickfad": "Carrick-fad",
                 "Mundy": "Mundy"}

PERSOS = ["Kate", "Agnes", "Rose", "Chris", "Michael"]
MICHAEL = [1000, 552]          # là où la partie 2 l'a laissé (« stands L », p. 6)
GARCON = [780, 460]            # l'enfant imaginaire, aux cerfs-volants (même place que dans les parties 2 et 4)
AU_GARCON = [850, 440]         # Kate « goes to him » (p. 9)
SIEGE = [480, 410]             # « KATE flops into a seat » (p. 11) ; place reprise au début de la partie 4
OBJ = {"kites": "kites", "garcon": GARCON}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture3", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_gle}{q1}This August, everywhere you go in Ballybeg, people ask the same question.",
        "{-q1}{mot_d}In this part, one word turns a quiet afternoon upside down: dance. "
        "The sisters want to go. Kate says no.",
        ("P", 0.3),
        "{-mot_d}{-tab_gle}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "q1": dict(type="question", t="Are you going to the harvest dance?"),
        "mot_d": dict(type="mot", t="dance", g="the word that turns the afternoon upside down", y=260, taille=110),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 3", t="The harvest dance",
                      sous="Kate comes home · pages 9 – 15"),
    }),

    # ------------------------------------------------------------------ I. Kate rentre (p. 9-10)
    dict(id="retour", chap="Kate comes home", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page nine. Michael has finished speaking. {jeu1.1}Kate enters, laden with shopping bags. "
        "When she sees the boy working at his kites, her face lights up with pleasure. She watches him for a few seconds. "
        "{jeu1.2}Then she goes to him.",
        ("C", "Well, that's what I call a busy man. Come here and give your Aunt Kate a big kiss.", "jeu1.3", {"voix": "F"}),
        "{jeu1.4}She kisses the crown of his head. Remember: the boy is invisible, and the adult Michael speaks his lines.",
        ("C", "It's two kites.", "jeu1.5"),
        "{jeu1.6}Kate studies the faces painted on the kites: faces which the audience cannot see. "
        "And she plays at being frightened.",
        ("C", "What are they? Devils? Ghosts?", "jeu1.7", {"voix": "F"}),
        "{jeu1.8}Then the presents: a small wooden spinning-top and a whip, and a new library book, with coloured pictures. "
        "{jeu1.9}She goes into the kitchen, and Michael exits.",
        ("C", "Oh, Kate, you have him spoiled. Where did you get it?", "jeu1.10", {"voix": "F"}),
        ("C", "Morgan's Arcade.", "jeu1.11", {"voix": "F"}),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Michael": MICHAEL},
                 act={"Agnes": "tricote", "Rose": "tricote", "Chris": "repasse", "Michael": "debout"},
                 objets=OBJ, cam="tout", note="“…out of wedlock.” (Michael, p. 9)"),
            dict(pos={"Kate": [1010, 330]}, act={"Kate": "debout"}, tient={"Kate": "sac"}, duree=2.5,
                 note="“KATE enters left, laden with shopping bags.” Her face “lights up with pleasure”."),
            dict(pos={"Kate": AU_GARCON}, duree=2.5, note="“She watches him for a few seconds. Then she goes to him.”"),
            dict(dit=["Kate", "Well, that's what I call a busy man. Come here and give your Aunt Kate a big kiss."]),
            dict(note="“She catches his head between her hands and kisses the crown of his head.”"),
            dict(dit=["Michael", "It's two kites."], note="The boy's line, spoken by adult Michael"),
            dict(note="“She studies the kite faces which the audience cannot see.” (p. 10)"),
            dict(dit=["Kate", "What are they? Devils? Ghosts?"], note="(Pretended Horror.)"),
            dict(note="A spinning-top and a whip · “A New library book! With coloured pictures!”"),
            dict(chemin={"Kate": [AU_GARCON, [720, 330], "porte", SIEGE]}, chemin_duree=5, pos={"Michael": "off"},
                 note="“She goes into the kitchen.” · “MICHAEL exits left.”"),
            dict(dit=["Chris", "Oh, Kate, you have him spoiled. Where did you get it?"]),
            dict(pos={"Kate": SIEGE}, dit=["Kate", "Morgan's Arcade."]),
        ]),
    }),

    # ------------------------------------------------------------------ II. Austin Morgan (p. 10-11)
    dict(id="austin", chap="Austin Morgan", fond="nuit", humeur="tension", beats=[
        "{jeu2}Then Rose starts teasing.",
        ("C", "I know why you went into Morgans!", "jeu2.1", {"voix": "F"}),
        ("C", "You wanted to see Austin Morgan!", "jeu2.2", {"voix": "F"}),
        "{jeu2.3}Kate answers with the fields and the hay.",
        ("C", "Because you have a notion of that aul Austin Morgan!", "jeu2.4", {"voix": "F"}),
        ("C", "Going to be a good harvest by the look of it.", "jeu2.5", {"voix": "F"}),
        ("C", "I know you have! She's blushing! Look! Isn't she blushing?", "jeu2.6", {"voix": "F"}),
        "{jeu2.7}Then Rose adds that Austin is going with a wee young thing from Carrickfad. Why are you blushing then? "
        "Why, why, why, Kate?",
        ("C", "For God's sake, Rose, shut up, would you!", "jeu2.8", {"voix": "F"}),
        "{jeu2.9}Agnes cuts Rose off: pass me those steel needles. A pause. Then Chris: are you tired? "
        "{jeu2.10}And Kate flops into a seat.",
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Kate": SIEGE, "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table"},
                 act={"Kate": "debout", "Agnes": "tricote", "Rose": "tricote", "Chris": "repasse"},
                 tient={"Kate": "sac"}, objets=OBJ, cam="cuisine", note="(p. 10)"),
            dict(dit=["Rose", "I know why you went into Morgans!"]),
            dict(dit=["Rose", "You wanted to see Austin Morgan!"], note="(p. 11)"),
            dict(note="“Every field along the road – they're all out at the hay and the corn.”"),
            dict(dit=["Rose", "Because you have a notion of that aul Austin Morgan!"]),
            dict(dit=["Kate", "Going to be a good harvest by the look of it."]),
            dict(dit=["Rose", "I know you have! She's blushing! Look! Isn't she blushing?"]),
            dict(note="“he's going with a wee young thing from Carrickfad” · “Why—why—why, Kate?”"),
            dict(dit=["Kate", "For God's sake, Rose, shut up, would you!"], note="(Sudden anger.)"),
            dict(note="“Rosie, pass me those steel needles – would you, please?” (Pause.) “Are you tired?”"),
            dict(act={"Kate": "assis"}, tient={"Kate": None}, note="“KATE flops into a seat.”"),
        ]),
    }),

    # ------------------------------------------------------------------ III. Ballybeg perd la tête (p. 11-13)
    dict(id="fievre", chap="Off its head", fond="nuit", humeur="mystere", beats=[
        "{jeu3}Kate gives the news from town. Everywhere you go, it's the one topic: are you going to the harvest dance? "
        "Who are you going with? What are you wearing?",
        "{jeu3.1}She unpacks: a novel for Agnes, cod-liver oil for Chris. And a girl of fifteen told her the dance "
        "would be just supreme this year.",
        ("C", "I'm telling you – off its head – like a fever in the place.", "jeu3.2", {"voix": "F"}),
        "{jeu3.3}And her very next words: That's the quinine. For Jack's malaria. Where is he? Wandering about out the back, says Chris.",
        "{jeu3.4}Meanwhile, Agnes has stopped knitting. She is looking abstractedly into the middle distance.",
        "{jeu3.5}Kate repeats the doctor: Swahili has been Jack's language for twenty-five years; it's not that his mind is confused. "
        "{jeu3.6}Chris disagrees: he keeps calling her some strange name.",
        ("C", "Okawa.", "jeu3.7", {"voix": "F"}),
        "{jeu3.8}His house boy, says Kate. And she takes off her shoe: she is getting corns.",
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Kate": SIEGE, "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table"},
                 act={"Kate": "assis", "Agnes": "tricote", "Rose": "tricote", "Chris": "repasse"}, objets=OBJ, cam="cuisine",
                 note="“Ballybeg's off its head.” (p. 11)"),
            dict(note="“It's going to be just supreme this year.” (Sophia, “all of fifteen”, p. 12)"),
            dict(dit=["Kate", "I'm telling you – off its head – like a fever in the place."]),
            dict(note="“That's the quinine. The doctor says it won't cure the malaria…”"),
            dict(act={"Agnes": "assis"}, note="“AGNES had stopped knitting and is looking abstractedly into the middle distance.”"),
            dict(note="“it's not that his mind is confused” (the doctor, through Kate)"),
            dict(note="Chris: “he keeps calling me some strange name like –” (p. 13)"),
            dict(dit=["Kate", "Okawa."]),
            dict(note="“Okawa was his house boy.” (Taking off her shoe.)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. « Wouldn't it be a good one… » (p. 13-14)
    dict(id="allons", chap="Let's all go!", fond="nuit", humeur="lumiere", beats=[
        "{jeu4}Then Agnes speaks, still looking into the distance.",
        ("C", "Wouldn't it be a good one if we all went?", "jeu4.1", {"voix": "F"}),
        "{jeu4.2}To the harvest dance. Just like they used to. All dressed up.",
        ("C", "I'd go, too, Aggie! I'd go with you!", "jeu4.3", {"voix": "F"}),
        "{jeu4.4}Kate objects: the place will be crawling with cheeky young brats she taught years ago. I'm game, says Agnes.",
        ("C", "Oh God, you know how I loved dancing, Aggie.", "jeu4.5", {"voix": "F"}),
        ("C", "You have a seven-year-old child – have you forgotten that?", "jeu4.6", {"voix": "F"}),
        "{jeu4.7}Agnes offers Chris her blue dress, and Kate her brown shoes with the crossover straps.",
        ("C", "Maybe we're mad – are we mad?", "jeu4.8", {"voix": "F"}),
        "{jeu4.9}It costs four and six to get in. Agnes has five pounds saved: I'll take us all.",
        ("C", "I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance.", "jeu4.10",
         {"voix": "F"}),
        ("C", "I know, I know, Agnes, I know.", "jeu4.11", {"voix": "F"}),
        "{jeu4.12}It's settled, says Agnes: the Mundy girls, all five of us together.",
        ("C", "I love you, Aggie! I love you more than chocolate biscuits!", "jeu4.13", {"voix": "F"}),
    ], vis={
        "jeu4": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Kate": SIEGE, "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table"},
                 act={"Kate": "assis", "Agnes": "assis", "Rose": "tricote", "Chris": "repasse"}, objets=OBJ, cam="cuisine",
                 note="(p. 13)"),
            dict(dit=["Agnes", "Wouldn't it be a good one if we all went?"]),
            dict(note="“To the harvest dance.” · “Just like we used to. All dressed up. I think I'd go.”"),
            dict(dit=["Rose", "I'd go, too, Aggie! I'd go with you!"]),
            dict(note="“Crawling with cheeky young brats that I taught years ago.” · “I'm game.”"),
            dict(dit=["Chris", "Oh God, you know how I loved dancing, Aggie."]),
            dict(dit=["Kate", "You have a seven-year-old child – have you forgotten that?"], note="(To CHRIS.)"),
            dict(note="“that blue dress of mine” · “my brown shoes with the crossover straps” (p. 14)"),
            dict(dit=["Kate", "Maybe we're mad – are we mad?"]),
            dict(note="“It costs four and six to get in.” · “I've five pounds saved.”"),
            dict(dit=["Agnes", "I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance."]),
            dict(dit=["Kate", "I know, I know, Agnes, I know."], note="(Wretched.)"),
            dict(note="“It's settled. We're going – the Mundy girls – all five of us together.”"),
            dict(dit=["Rose", "I love you, Aggie! I love you more than chocolate biscuits!"]),
        ]),
    }),

    # ------------------------------------------------------------------ V. le refus (p. 14-15)
    dict(id="refus", chap="Kate says no", fond="nuit", humeur="tension", beats=[
        "{jeu5}Rose {jeu5.1}kisses Agnes impetuously, {jeu5.2}flings her arms above her head, begins singing Abyssinia, "
        "{jeu5.3}and does the first steps of a bizarre and abandoned dance. {jeu5.4}At this, Kate panics.",
        ("C", "No, no, no! We're going nowhere!", "jeu5.5", {"voix": "F"}),
        "{jeu5.6}Look at yourselves, she says. Dancing at our time of day? That's for young people with nothing in their heads but pleasure.",
        ("C", "Do you want the whole countryside to be laughing at us?", "jeu5.7", {"voix": "F"}),
        ("C", "women of our years? – mature women, dancing?", "jeu5.8", {"voix": "F"}),
        ("C", "And this is Father Jack's home – we must never forget that – ever.", "jeu5.9", {"voix": "F"}),
        ("C", "The matter's over. I don't want it mentioned again.", "jeu5.10", {"voix": "F"}),
        "{jeu5.11}And the stage direction gives one word: silence.",
        ("P", 3.0),
    ], vis={
        "jeu5": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Kate": SIEGE, "Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table"},
                 act={"Kate": "assis", "Agnes": "assis", "Rose": "tricote", "Chris": "repasse"}, objets=OBJ, cam="cuisine"),
            dict(pos={"Rose": [535, 500]}, act={"Rose": "debout"}, note="“ROSE kisses AGNES impetuously” (p. 14)"),
            dict(act={"Rose": "leve"}, note="She “flings her arms above her head, begins singing ‘Abyssinia’”"),
            dict(act={"Rose": "danse_lourde"}, note="“the first steps of a bizarre and abandoned dance”"),
            dict(note="“At this KATE panics.”"),
            dict(dit=["Kate", "No, no, no! We're going nowhere!"]),
            dict(act={"Rose": "debout"}, note="“Look at yourselves, will you! Just look at yourselves!” (p. 15)"),
            dict(dit=["Kate", "Do you want the whole countryside to be laughing at us?"]),
            dict(dit=["Kate", "women of our years? – mature women, dancing?"], note="“dancing” is in italics in the text"),
            dict(dit=["Kate", "And this is Father Jack's home – we must never forget that – ever."]),
            dict(dit=["Kate", "The matter's over. I don't want it mentioned again."]),
            dict(note="(Silence.)"),
        ]),
    }),

    # ------------------------------------------------------------------ VI. cinq répliques à connaître
    dict(id="repliques3", chap="Five lines to know", fond="aube", humeur="calme",
         retenir="Hidden faces, a blush and an outburst, a fever, “I want to dance”, “laughing at us”: desire and its guardian.", beats=[
        "{cinq3}One afternoon, one word, dance… and five lines to remember.",
        "First, the kites.{-cinq3}",
        ("C", "What are they? Devils? Ghosts?", "c_ghosts", {"voix": "F"}),
        "{-c_ghosts}{fore}A joke. But keep those hidden faces in mind: the play only shows them near the very end. "
        "Something wild and pagan is already painted on the boy's toys.",
        "Second, Kate's outburst.{-fore}",
        ("C", "For God's sake, Rose, shut up, would you!", "c_shut", {"voix": "F"}),
        "{-c_shut}{sub}This is subtext. Kate never says a word about Austin Morgan: she talks about the harvest. "
        "But her blush speaks for her, and then the control cracks. In this house, painful things are covered "
        "with silence and small tasks: the steel needles.",
        "Third, the village.{-sub}",
        ("C", "I'm telling you – off its head – like a fever in the place.", "c_fever", {"voix": "F"}),
        "{-c_fever}{jux}And her very next words? That's the quinine. {jux.g}A fever of dancing in the village. "
        "{jux.d}A real fever in Father Jack. This juxtaposition links desire and illness, the festival and the sick priest.",
        "Fourth, Agnes.{-jux}",
        ("C", "I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance.", "c_dance",
         {"voix": "F"}),
        "{-c_dance}{rep}{rep.1}I want to dance, at the start and the end, like a refrain. "
        "{rep.2}In between, two reasons. Lughnasa: the pagan festival, the title of the play. "
        "{rep.3}And her age: time is running out. Pure desire, without excuses.",
        "And fifth, Kate's answer.{-rep}",
        ("C", "Do you want the whole countryside to be laughing at us? – women of our years? – mature women, dancing?",
         "c_laugh", {"voix": "F"}),
        "{-c_laugh}{raisons}Her first fear is not sin, but other people's eyes, and dancing is in italics, as if the word were shameful. "
        "{raisons.1}The parish is watching. {raisons.2}A priest's home must be beyond reproach. "
        "{raisons.3}And Chris has a child born out of wedlock: this family cannot afford one more scandal. "
        "But remember the opening: Michael saw these women dancing in this kitchen. The forbidden dance will come back.",
    ], vis={
        "cinq3": dict(type="mot", t="One word: dance", g="five lines to know · pages 9 – 15", y=250, taille=88),
        "c_ghosts": dict(type="cit", a="Kate, with “pretended horror”", o="p. 10", x=170, y=200, w=940),
        "fore": dict(type="def", cles=["hidden", "pagan"], terme="Foreshadowing",
                     t="“She studies the kite faces which the audience cannot see”: devils and ghosts on a child's toy.",
                     etape="The faces are only revealed near the end of the play.", x=170, y=200, w=940),
        "c_shut": dict(type="cit", a="Kate (sudden anger)", o="p. 11", x=170, y=200, w=940),
        "sub": dict(type="def", cles=["harvest", "blush"], terme="Subtext",
                    t="What a character means but does not say: Kate talks about the harvest, her blush talks about Austin Morgan.",
                    etape="A woman of authority, with a hidden longing.", x=170, y=200, w=940),
        "c_fever": dict(type="cit", a="Kate", o="p. 12", x=170, y=200, w=940),
        "jux": dict(type="cols", g="The village", gq="“like a fever”: the harvest dance", d="Father Jack",
                    dq="malaria: “That's the quinine”", vs="↔", repere="juxtaposition"),
        "c_dance": dict(type="cit", a="Agnes", o="p. 14", x=170, y=200, w=940),
        "rep": dict(type="liste", titre="Agnes's speech", cles=["refrain"], items=[
            "“I want to dance” … “I want to dance”: a refrain",
            "“the Festival of Lughnasa”: the pagan title",
            "“only thirty-five”: time is running out"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_laugh": dict(type="cit", a="Kate", o="p. 15", x=170, y=200, w=940),
        "raisons": dict(type="liste", titre="Kate's reasons", items=[
            "“the whole countryside … laughing at us”: the parish is watching",
            "“Father Jack's home”: a priest's house, beyond reproach",
            "“You have a seven-year-old child”: the shame of an unmarried mother"],
                        marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ VI. l'analyse
    dict(id="analyse3", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Kate's cracks, the dance as fever, subtext and silence, a watched family: four keys to this scene.", beats=[
        "{b1}Now the analysis. Four ideas. "
        "{b1.1}One: Kate's authority, and its cracks. She provides and decides. "
        "But she blushes, she snaps, she asks: are we mad? Her no is not a lack of desire. It is fear.",
        "{-b1}{b2}{b2.1}Two: the dance as fever and release. A fever in Ballybeg, Agnes's Lughnasa, Rose's abandoned dance. "
        "A pagan energy presses against a Catholic house, right next to Jack's malaria.",
        "{-b2}{b3}{b3.1}Three: subtext and silence. The harvest instead of Austin Morgan, the needles, and a final silence. "
        "What is not said matters as much as what is said.",
        "{-b3}{b4}{b4.1}Four: a fragile, watched family. Little money, an unmarried mother, a sick priest, a countryside ready to laugh. "
        "Respectability is the price of survival.",
        "{-b4}{carte}For your essay, this scene supports four themes. {carte.1}Kate and authority. "
        "{carte.2}The dance and Lughnasa. {carte.3}Subtext and silence. {carte.4}Respectability in nineteen thirties Ireland.",
    ], vis={
        "b1": dict(type="note", cles=["cracks", "fear"], terme="1 · Kate's authority and its cracks",
                   t="She provides and decides; she blushes, snaps, is “wretched”, asks “are we mad?”",
                   etape="Her refusal comes from fear, not from a lack of desire.", x=170, y=200, w=940),
        "b2": dict(type="note", cles=["fever", "pagan"], terme="2 · The dance: fever and release",
                   t="“like a fever in the place”; “It's the Festival of Lughnasa”; “a bizarre and abandoned dance”.",
                   etape="A pagan energy pressing against a Catholic house.", x=170, y=200, w=940),
        "b3": dict(type="note", cles=["subtext", "silence"], terme="3 · Subtext and silence",
                   t="The harvest instead of Austin Morgan; the steel needles; “(Silence.)”",
                   etape="What is not said matters as much as what is said.", x=170, y=200, w=940),
        "b4": dict(type="note", cles=["watched", "Respectability"], terme="4 · A fragile, watched family",
                   t="“four and six”, five pounds saved; an unmarried mother; “the whole countryside”.",
                   etape="Respectability is the price of survival.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE HARVEST DANCE", branches=[
            dict(t="Kate", items=["provider and judge", "the blush, the anger", "“are we mad?”"]),
            dict(t="The dance", items=["“like a fever”", "“the Festival of Lughnasa”", "Rose's “abandoned dance”"]),
            dict(t="Silence", items=["subtext: Austin Morgan", "the steel needles", "“(Silence.)”"]),
            dict(t="Respectability", items=["“laughing at us”", "“Father Jack's home”", "money, shame"])]),
    }),
]

QUIZ = [
    dict(q="What does Kate bring back for the boy?",
         r=["A spinning-top, a whip and a new library book", "A kite and some paint", "A wireless set",
            "A ticket for the harvest dance"], ok=0, voir="jeu1.8",
         ex="She produces “a small, wooden spinning top and whip”, then a new library book “with coloured pictures” (p. 10)."),
    dict(q="When Rose says Kate wanted to see Austin Morgan, Kate first…",
         r=["talks about the harvest in the fields", "admits it at once", "laughs and agrees", "leaves the kitchen"], ok=0,
         voir="jeu2.5",
         ex="Subtext: she answers with “a good harvest”, but she blushes, and ends with “For God's sake, Rose, shut up, would you!”"),
    dict(q="What does Kate mention right after “like a fever in the place”?",
         r=["The quinine for Father Jack's malaria", "Chris's blue dress", "The price of a ticket", "The fox in the henhouse"],
         ok=0, voir="c_fever",
         ex="A juxtaposition: the village's “fever” for the dance next to Jack's real fever, malaria (p. 12)."),
    dict(q="Which two reasons does Agnes give for wanting to dance?",
         r=["It's the Festival of Lughnasa, and she is only thirty-five", "Gerry will be there, and it is free",
            "Father Jack asked them to go", "Kate needs a rest, and Rose has a new dress"], ok=0, voir="c_dance",
         ex="“I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance.” (p. 14)"),
    dict(q="What makes Kate panic and say “No, no, no!”?",
         r=["Rose's “bizarre and abandoned dance”", "News that Jack has disappeared", "Chris crying",
            "The radio breaking down"], ok=0, voir="jeu5.3",
         ex="Rose sings “Abyssinia” and starts a wild dance: “At this KATE panics.” (p. 14)"),
    dict(q="Which reasons does Kate give for refusing?",
         r=["The countryside would laugh, and it is Father Jack's home", "They have no dresses and no shoes",
            "The dance is too far away", "Maggie does not want to go"], ok=0, voir="c_laugh",
         ex="Respectability and religion: “the whole countryside … laughing at us” and “this is Father Jack's home” (p. 15)."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: Glenties, County Donegal (Thpohl, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
