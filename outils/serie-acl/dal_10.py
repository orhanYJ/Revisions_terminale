"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 10 : « Rose goes missing » (PDF de travail, p. 58-62).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu), en suivant les didascalies pas à pas ; les répliques courtes s'affichent en
bulles et sont lues par la voix des sœurs. Le retour de Rose suit la grande didascalie de la p. 60 (Chris et Kate à la
fenêtre, Maggie et Agnes à la porte, Rose qui traverse lentement le jardin, s'arrête près des bidons) ; ce que le moteur ne
sait pas montrer (le coquelicot, les baies mangées, la chaussure ôtée) passe en notes citées, sans geste inventé. Ce que Rose
raconte (le bateau, les feux) n'est pas joué. Rose porte ses « good » clothes (cardigan bleu) ; le moteur lui dessine
toujours ses bottes. Puis quatre répliques à connaître et l'analyse.

Début : p. 58, « (MAGGIE enters.) MAGGIE. She's not in her bed. » Kate interroge Agnes, Maggie devine Danny Bradley et
Lough Anna, Kate refuse la police (p. 59), Rose revient (grande didascalie p. 60), le menu de Maggie (p. 61), le récit de
Rose à Kate (p. 62). Fin : p. 62, « (She exits, her shoes in one hand, the poppy in the other. » — juste avant
« MICHAEL enters. » et la réplique de Kate « What has happened to this house? » (partie 11).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_10. Citations courtes, à fin d'analyse ; le reste est résumé.
Coquilles du PDF évitées dans les citations (« I cam on home », « That's al any of you »).
Ce qui ne vient pas du texte (symbolique traditionnelle du coquelicot) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-10"
NOTION = "Dancing at Lughnasa"
NUM = 10
TITRE = "Rose goes missing"
SUIVANT = "Part 11 · What happened next"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Lough": "Lock", "Mundy": "Mundy",
                 "Ballybeg": "Bally-beg"}

BLEU = "#4f6fb8"   # « her blue cardigan and her good skirt » (p. 59)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Rose has been gone for more than three hours. She is not in her bed, and nobody knows where she is.",
        "{-q1}For the first time, the sisters' fear has a name… and a face.",
        "{-tab_don}{serie}Part ten: the search for Rose, Kate's interrogation, and a return that explains nothing.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Where is Rose?"),
        "serie": dict(type="mot", t="Act Two", g="the search · the interrogation · the return", y=270, taille=88),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 10", t="Rose goes missing",
                      sous="Act Two · pages 58 – 62"),
    }),

    # ------------------------------------------------------------------ I. où est Rose ? (pp. 58-59)
    dict(id="absente", chap="Not in her bed", fond="nuit", humeur="tension", beats=[
        "{jeu1}Page fifty-eight. Rose told Agnes she was going home to lie down. {jeu1.1}Maggie comes back from the bedroom.",
        ("C", "She's not in her bed.", "jeu1.2", {"voix": "F"}),
        ("C", "Start at the beginning, Agnes. What exactly happened?", "jeu1.3", {"voix": "F"}),
        "{jeu1.4}They left together just after one o'clock and walked to the quarry. Rose wasn't feeling well, "
        "so she sat in the sun. Agnes fell into a bush, Rose laughed, and said she'd go home and sleep.",
        ("C", "That means she's missing for over three hours.", "jeu1.5", {"voix": "F"}),
        "{jeu1.6}Agnes begins to cry.",
        ("C", "Where is she? What's happened to our Rosie?", "jeu1.7", {"voix": "F"}),
        ("C", "Stop sniveling, Agnes! Did she go towards home?", "jeu1.8", {"voix": "F"}),
        "She may have gone into the town, says Maggie.",
        ("C", "She wouldn't have gone into town in her Wellingtons.", "jeu1.9", {"voix": "F"}),
        ("C", "She was wearing her good shoes.", "jeu1.10", {"voix": "F"}),
        "{jeu1.11}Page fifty-nine. And her blue cardigan, and her good skirt. I'm some toff, Rose said. "
        "A bottle of milk in one of her cans.",
        ("C", "She had half-a-crown. That's all she has.", "jeu1.12", {"voix": "F"}),
        "Then Maggie, softly, puts it together.",
        ("C", "Danny Bradley … Lough Anna … up in the back hills.", "jeu1.13", {"voix": "F"}),
        ("C", "Oh God, no.", "jeu1.14", {"voix": "F"}),
        "{jeu1.15}Remember part two: Rose told them her plan, a boat on Lough Anna, a bottle of milk, chocolate biscuits. "
        "Chris warned her then: Danny Bradley is a married man. Now they understand.",
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Agnes"], etats=[
            dict(pos={"Kate": [295, 430], "Chris": [385, 430], "Agnes": [475, 430], "Maggie": "off"}, cam="cuisine", objets={"kites": "banc"},
                 note="“She left me and went home to lie down.” (p. 57)"),
            dict(chemin={"Maggie": ["arriere", [205, 430]]}, chemin_duree=2.5, note="(MAGGIE enters.) p. 58"),
            dict(pos={"Maggie": [205, 430]}, dit=["Maggie", "She's not in her bed."]),
            dict(dit=["Kate", "Start at the beginning, Agnes. What exactly happened?"]),
            dict(note="“I told her not to bother about the bilberries -- just to sit in the sun.”"),
            dict(dit=["Chris", "That means she's missing for over three hours."]),
            dict(act={"Agnes": "pleure"}, note="(AGNES begins to cry.)"),
            dict(dit=["Agnes", "Where is she? What's happened to our Rosie?"]),
            dict(dit=["Kate", "Stop sniveling, Agnes! Did she go towards home?"]),
            dict(dit=["Chris", "She wouldn't have gone into town in her Wellingtons."]),
            dict(act={"Agnes": "debout"}, dit=["Agnes", "She was wearing her good shoes."]),
            dict(note="“her blue cardigan and her good skirt” — “I'm some toff, Aggie” (p. 59)"),
            dict(dit=["Agnes", "She had half-a-crown. That's all she has."]),
            dict(dit=["Maggie", "Danny Bradley … Lough Anna … up in the back hills."], note="(Softly.)"),
            dict(dit=["Chris", "Oh God, no."]),
            dict(note="Part two: Rose's plan, a boat on Lough Anna (told, not shown)"),
        ]),
    }),

    # ------------------------------------------------------------------ II. l'affaire Bradley (pp. 59-60)
    dict(id="bradley", chap="This Bradley business", fond="nuit", humeur="tension", beats=[
        "{jeu2}Chris explains: Rose has some silly notion about that scamp, Bradley. She believes he's in love with her. "
        "And Kate turns, not on Bradley, but on Agnes.",
        ("C", "I've often seen you and Rose whispering together. What plot has been hatched between Rose and Mr. Bradley?",
         "jeu2.1", {"voix": "F"}),
        "{jeu2.2}Plot, hatched: Kate speaks like a judge facing a conspiracy. No plot, please, Kate, says Agnes.",
        ("C", "You're lying to me, Agnes! You're withholding! I want the truth!", "jeu2.3", {"voix": "F"}),
        ("C", "I want to know everything you know! Now! I want to –", "jeu2.4", {"voix": "F"}),
        "And then, something new. Maggie, the joker, stops her.",
        ("C", "That'll do, Kate! Stop that at once!", "jeu2.5", {"voix": "F"}),
        "{jeu2.6}Calmly, she organises the search. Chris takes the upper fields, Agnes the lower side, Kate the old well.",
        ("C", "I'm going into the town to tell the police.", "jeu2.7", {"voix": "F"}),
        ("C", "You're going to no police, Maggie. If she's mixed up with that Bradley creature, I'm not going to have it "
              "broadcast all over –", "jeu2.8", {"voix": "F"}),
        ("C", "I'm going to the police and you'll do what I told you to do.", "jeu2.9", {"voix": "F"}),
        "{jeu2.10}In part seven, Kate felt that control was slipping away. Here, it slips out of her hands.",
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Agnes"], etats=[
            dict(pos={"Kate": [295, 430], "Chris": [385, 430], "Agnes": [475, 430], "Maggie": [205, 430]}, cam="cuisine", objets={"kites": "banc"},
                 note="“She has some silly notion about that scamp, Bradley.”"),
            dict(dit=["Kate", "… What plot has been hatched between Rose and Mr. Bradley?"], note="(To AGNES.)"),
            dict(note="AGNES: “No plot … please, Kate --”"),
            dict(dit=["Kate", "You're lying to me, Agnes! You're withholding! I want the truth!"]),
            dict(dit=["Kate", "I want to know everything you know! Now! I want to –"]),
            dict(dit=["Maggie", "That'll do, Kate! Stop that at once!"]),
            dict(note="(Calmly.) Chris: the upper side of the lane · Agnes: the lower side · Kate: the old well"),
            dict(dit=["Maggie", "I'm going into the town to tell the police."]),
            dict(dit=["Kate", "You're going to no police, Maggie. If she's mixed up with that Bradley creature …"]),
            dict(dit=["Maggie", "I'm going to the police and you'll do what I told you to do."], note="(p. 60)"),
            dict(note="Kate gives orders; now Maggie gives them."),
        ]),
    }),

    # ------------------------------------------------------------------ III. le retour (pp. 60-61)
    dict(id="retour", chap="The return", fond="nuit", humeur="mystere", beats=[
        "{jeu3}Page sixty. Suddenly, through the window, Chris sees someone.",
        ("C", "There she is! Look – look! There she is!", "jeu3.1", {"voix": "F"}),
        "{jeu3.2}She is about to rush out, but Maggie catches her arm and restrains her. "
        "{jeu3.3}The four sisters watch Rose cross the garden: Chris and Kate from the window, Maggie and Agnes from the door.",
        "{jeu3.4}Rose is unaware of their anxious scrutiny. In her good clothes, she might be any youngish country woman, "
        "returning from a long walk on a summer day. She walks slowly, lethargically.",
        "{jeu3.5}From her right hand hangs a red poppy, plucked casually along the road. Her face reveals nothing.",
        "{jeu3.6}She sees Agnes's cans of fruit, stops beside them, and looks at them. "
        "{jeu3.7}She takes a fistful of berries, thrusts it into her mouth, looks at her stained fingers, wipes them on her skirt. "
        "{jeu3.8}All of it calmly, naturally.",
        "{jeu3.9}Agnes rushes to meet her. She wants to hug her; instead, she catches her arm.",
        ("C", "Rosie, love, we were beginning to get worried about you.", "jeu3.10", {"voix": "F"}),
        ("C", "They're nice, Aggie. They're sweet. And you got two canfuls. Good for you.", "jeu3.11", {"voix": "F"}),
        "{jeu3.12}Agnes leads her into the house. Your stomach? Oh, I'm fine now, says Rose.",
        ("C", "But you didn't come home, Rosie.", "jeu3.13", {"voix": "F"}),
        ("C", "Well … here I am.", "jeu3.14", {"voix": "F"}),
        ("C", "You went into Ballybeg, didn't you?", "jeu3.15", {"voix": "F"}),
        "{jeu3.16}Page sixty-one. A pause. Rose looks from one to the other. So Maggie, briskly, fills the silence.",
        ("C", "She's home safe and sound and that's all that matters.", "jeu3.17", {"voix": "F"}),
        "{jeu3.18}Then she performs tonight's menu like a grand chef: three eggs between the seven of us.",
        ("C", "There are eight of us, Maggie.", "jeu3.19", {"voix": "F"}),
        "{jeu3.20}Of course: the soldier up the sycamore. Eggs Ballybeg! Comedy, once again, to cover the fear. "
        "{jeu3.21}Rose has taken off her shoe and is examining it carefully. Her cans? Hidden at the quarry, she says, "
        "behind a stone wall.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Agnes", "Rose"], etats=[
            dict(pos={"Kate": [295, 430], "Chris": [385, 430], "Agnes": [475, 430], "Maggie": [205, 430], "Rose": "off"},
                 costume={"Rose": BLEU}, bottes={"Rose": False}, cam="tout", objets={"kites": "banc"}),
            dict(chemin={"Rose": ["allee", [900, 430], [700, 425]]}, chemin_duree=20,
                 dit=["Chris", "There she is! Look – look! There she is!"]),
            dict(pos={"Chris": [520, 375], "Maggie": [435, 375]}, note="(MAGGIE catches her arm and restrains her.)"),
            dict(pos={"Chris": [265, 238], "Kate": [325, 238], "Maggie": [545, 295], "Agnes": [600, 330]},
                 note="CHRIS and KATE watch from the window, MAGGIE and AGNES from the door."),
            dict(note="“ROSE is unaware of their anxious scrutiny.” She walks “slowly, lethargically”."),
            dict(note="“From her right hand hangs a red poppy that she plucked casually along the road.”"),
            dict(pos={"Rose": [700, 425]}, duree=2.5, note="She sees Agnes's cans of fruit. She stops beside them."),
            dict(note="a fistful of berries … her stained fingers … she wipes them on her skirt"),
            dict(note="“not dreamily, abstractedly, but calmly, naturally”"),
            dict(pos={"Agnes": [650, 420]}, note="AGNES rushes to meet her. Instead of hugging her, she catches her arm."),
            dict(dit=["Agnes", "Rosie, love, we were beginning to get worried about you."]),
            dict(dit=["Rose", "They're nice, Aggie. They're sweet. And you got two canfuls. Good for you."]),
            dict(pos={"Agnes": [440, 430], "Rose": [520, 430]}, duree=3, cam="cuisine",
                 note="(AGNES leads her into the house.)"),
            dict(dit=["Chris", "But you didn't come home, Rosie."]),
            dict(dit=["Rose", "Well … here I am."]),
            dict(dit=["Chris", "You went into Ballybeg, didn't you?"], note="(p. 61)"),
            dict(note="(Pause. ROSE looks from one to the other.)"),
            dict(dit=["Maggie", "She's home safe and sound and that's all that matters."], note="(Briskly.)"),
            dict(note="“there's only three eggs between the seven of us”"),
            dict(dit=["Chris", "There are eight of us, Maggie."]),
            dict(note="“Of course – the soldier up the sycamore!” … “Eggs Ballybeg”"),
            dict(note="(ROSE has taken off her shoe and is examining it carefully.)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. Lough Anna (p. 62)
    dict(id="lough", chap="Lough Anna", fond="nuit", humeur="tension", beats=[
        "{jeu4}Page sixty-two. {jeu4.1}Rose moves towards the bedroom door. Just as she is about to exit, Kate speaks.",
        ("C", "I want to know where you have been, Rose.", "jeu4.2", {"voix": "F"}),
        "{jeu4.3}Rose stops. A pause.",
        ("C", "Where have you been for the past three hours?", "jeu4.4", {"voix": "F"}),
        ("C", "Lough Anna.", "jeu4.5", {"voix": "F"}),
        "Almost inaudible. Kate fires short questions, like a prosecutor. You walked to Lough Anna? Yes.",
        ("C", "Did you meet somebody there?", "jeu4.6", {"voix": "F"}),
        "Yes.",
        ("C", "Had you arranged to meet somebody there?", "jeu4.7", {"voix": "F"}),
        ("C", "I had arranged to meet Danny Bradley there, Kate.", "jeu4.8", {"voix": "F"}),
        "Then she tells her story, turning to each sister in turn. We hear it; we never see it. "
        "{jeu4.9}His father's blue boat, a picnic on the lake. {jeu4.10}Then up through the back hills, "
        "where he showed her what was left of the Lughnasa fires. {jeu4.11}Young Sweeney, the boy who got burned, is on the mend.",
        ("C", "It's a very peaceful place up there. There was nobody there but Danny and me.", "jeu4.12", {"voix": "F"}),
        ("C", "He calls me his Rosebud, Aggie.", "jeu4.13", {"voix": "F"}),
        "He walked her down as far as the workhouse gate, and she came home by herself. And to Kate:",
        ("C", "And that's all I'm going to tell you.", "jeu4.14", {"voix": "F"}),
        "{jeu4.15}She exits, her shoes in one hand, the poppy in the other. "
        "Rose, the sister everyone protects, has just set the limits of what Kate can know.",
    ], vis={
        "jeu4": dict(type="jeu", persos=["Kate", "Maggie", "Chris", "Agnes", "Rose"], etats=[
            dict(pos={"Kate": [325, 238], "Chris": [265, 238], "Maggie": [545, 295], "Agnes": [440, 430], "Rose": [520, 430]},
                 costume={"Rose": BLEU}, bottes={"Rose": False}, cam="cuisine", objets={"kites": "banc"}),
            dict(pos={"Rose": [160, 470]}, duree=3, note="(ROSE moves towards the bedroom door.)"),
            dict(dit=["Kate", "I want to know where you have been, Rose."]),
            dict(note="(ROSE stops. Pause.)"),
            dict(dit=["Kate", "Where have you been for the past three hours?"]),
            dict(dit=["Rose", "Lough Anna."], note="(inaudible.)"),
            dict(dit=["Kate", "Did you meet somebody there?"]),
            dict(dit=["Kate", "Had you arranged to meet somebody there?"]),
            dict(dit=["Rose", "I had arranged to meet Danny Bradley there, Kate."]),
            dict(note="“He brought me out in his father's blue boat.” A picnic on the lake (told, not shown)"),
            dict(note="“He showed me what was left of the Lughnasa fires” (told, not shown)"),
            dict(note="Young Sweeney, “the boy who got burned”: “he's on the mend, Danny says”"),
            dict(dit=["Rose", "It's a very peaceful place up there. There was nobody there but Danny and me."], note="(To all.)"),
            dict(dit=["Rose", "He calls me his Rosebud, Aggie."], note="(To AGNES.)"),
            dict(dit=["Rose", "And that's all I'm going to tell you."], note="(To KATE.)"),
            dict(pos={"Rose": "off"}, note="(She exits, her shoes in one hand, the poppy in the other.)"),
        ]),
    }),

    # ------------------------------------------------------------------ V. quatre répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="“broadcast all over”; Rose seen without her disability; “Her face reveals nothing”; “that's all I'm going to tell you”.",
         beats=[
        "{quatre}Four lines from these pages are worth knowing by heart. First, Kate.",
        "{-quatre}",
        ("C", "If she's mixed up with that Bradley creature, I'm not going to have it broadcast all over –", "c_police",
         {"voix": "F"}),
        "{-c_police}{honte}Rose may be hurt, but Kate's first fear is the parish. Broadcast: the language of the wireless. "
        "In this small Catholic world, shame travels fast.",
        "{-honte}Then Rose's return.",
        ("C", "Indeed, had we not seen the Rose of Act One, we might not now be immediately aware of her disability.", "c_disab"),
        "{-c_disab}{femme}For a moment, Friel lets us see Rose as Danny may see her: a woman, not a problem to be managed.",
        "{-femme}",
        ("C", "Her face reveals nothing – but nothing is being deliberately concealed.", "c_face"),
        "{-c_face}{paradoxe}A beautiful paradox. Rose is not hiding anything… and yet we learn nothing.",
        "{-paradoxe}And Rose's last word to Kate.",
        ("C", "And that's all I'm going to tell you.", "c_all", {"voix": "F"}),
        "{-c_all}{sortie}Rose tells the facts on her own terms, then sets a limit. What happened at Lough Anna stays unsaid.",
    ], vis={
        "quatre": dict(type="mot", t="Four lines to know", g="pages 59 – 62", y=260, taille=84),
        "c_police": dict(type="cit", a="Kate", o="p. 59", x=170, y=200, w=940),
        "honte": dict(type="cols", g="Kate", gq="“I'm not going to have it broadcast”: the parish, the shame", d="Maggie",
                      dq="“you'll do what I told you to do”: find Rose", vs="≠", repere="reputation / Rose herself"),
        "c_disab": dict(type="cit", a="Stage direction", o="p. 60", x=170, y=200, w=940),
        "femme": dict(type="note", cles=["woman", "Danny"], terme="Stage direction · p. 60",
                      t="“any youngish country woman, carefully dressed, not unattractive”",
                      etape="Rose seen as a woman, not a problem to be managed.", x=170, y=200, w=940),
        "c_face": dict(type="cit", a="Stage direction", o="p. 60", x=170, y=200, w=940),
        "paradoxe": dict(type="note", cles=["paradox", "nothing"], terme="Stage direction · p. 60",
                         t="Nothing concealed, nothing revealed: Rose hides nothing, and we learn nothing.",
                         etape="“calmly, naturally”: her secret is simply her own.", x=170, y=200, w=940),
        "c_all": dict(type="cit", a="Rose, to Kate", o="p. 62", x=170, y=200, w=940),
        "sortie": dict(type="note", cles=["limit", "unsaid"], terme="Rose · p. 62",
                       t="The facts on her own terms: the boat, the picnic, the fires, “his Rosebud”.",
                       etape="Then a limit: what happened stays unsaid.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Kate's authority fails, Rose keeps her secret, the pagan back hills claim her, and we already know the end.", beats=[
        "{a1}Now the analysis: four ideas from this scene. "
        "{a1.1}One: Kate's authority collapses. She interrogates and accuses, "
        "but Maggie gives the orders, and Rose sets the limits. The guardian of order has lost control.",
        "{-a1}{a2}{a2.1}Two: silence and subtext. Rose tells the facts, the boat, the picnic, the fires, "
        "but not what they meant to her. Her face reveals nothing. Friel leaves a gap at the heart of the scene, "
        "and we, like the sisters, must fill it.",
        "{-a2}{a3}{a3.1}Three: the pagan world. Rose goes up into the back hills, among the last Lughnasa fires, "
        "and she comes back with stained fingers and a red poppy. "
        "Outside the text: the red poppy is often read as a sign of passion, or of sleep and forgetting. "
        "The play does not explain it: it is an image, not a message.",
        "{-a3}{a4}{a4.1}Four: dramatic irony. We know what the sisters do not: the glove money is gone, "
        "and, Michael told us, in early September Rose and Agnes will leave for ever. "
        "So Rose's one afternoon of freedom is shadowed by our tragic knowledge.",
        "{-a4}{carte}Here is this scene for your essay. {carte.1}Kate's authority. {carte.2}Silence and subtext. "
        "{carte.3}The pagan back hills. {carte.4}And Rose's desire, her own, set against a future we already know.",
    ], vis={
        "a1": dict(type="note", cles=["interrogates", "Maggie"], terme="1 · Kate's authority collapses",
                   t="“What plot has been hatched …?” · “You're going to no police”.",
                   etape="Maggie commands; Rose refuses: control slips away.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["subtext", "gap"], terme="2 · Silence and subtext",
                   t="“Her face reveals nothing” · “that's all I'm going to tell you”.",
                   etape="A gap at the heart of the scene: what happened is never said.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["pagan", "poppy"], terme="3 · The pagan back hills",
                   t="“what was left of the Lughnasa fires”; stained fingers; a red poppy.",
                   etape="An image, not a message: desire beyond Kate's Catholic order.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["irony", "tragic"], terme="4 · Dramatic irony",
                   t="The gloves are finished; in September, Rose and Agnes will leave for ever.",
                   etape="Tragic knowledge shadows Rose's afternoon of freedom.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="ROSE GOES MISSING", branches=[
            dict(t="Kate's authority", items=["“What plot has been hatched”", "“broadcast all over”", "Maggie in command"]),
            dict(t="Subtext", items=["“Her face reveals nothing”", "“that's all I'm going to tell you”"]),
            dict(t="Pagan world", items=["the back hills", "“the Lughnasa fires”", "the red poppy"]),
            dict(t="Desire & fate", items=["“his Rosebud”", "the lost gloves", "September: “for ever”"])]),
    }),
]

QUIZ = [
    dict(q="What clue makes Maggie think of Danny Bradley?",
         r=["Rose took her good clothes, a bottle of milk and her half-crown", "Rose left a letter on her bed",
            "Danny Bradley came to the house that morning", "Agnes saw them together at the quarry"], ok=0, voir="jeu1.11",
         ex="Good shoes, blue cardigan, good skirt, milk, half-a-crown: exactly the plan Rose described in Act One (p. 5)."),
    dict(q="Whom does Kate accuse of hiding the truth?",
         r=["Agnes", "Chris", "Maggie", "Father Jack"], ok=0, voir="jeu2.1",
         ex="“What plot has been hatched between Rose and Mr. Bradley?” … “You're lying to me, Agnes! You're withholding!”"),
    dict(q="Why does Kate refuse to go to the police?",
         r=["She does not want the affair “broadcast all over”", "She thinks Rose is at the pictures",
            "The police station is closed on Sundays", "Maggie has already been"], ok=0, voir="c_police",
         ex="Her first fear is scandal in the parish. Maggie overrules her: “you'll do what I told you to do.”"),
    dict(q="What does the long stage direction suggest about Rose as she returns?",
         r=["In her good clothes, we might not notice her disability at first", "She is crying and frightened",
            "She is hiding something on purpose", "She is drunk"], ok=0, voir="c_disab",
         ex="She looks like “any youngish country woman”; “Her face reveals nothing – but nothing is being deliberately concealed.”"),
    dict(q="What does Rose carry in her right hand?",
         r=["A red poppy", "Danny's silver charm", "A bottle of milk", "A kite"], ok=0, voir="jeu3.5",
         ex="“From her right hand hangs a red poppy that she plucked casually along the road.” She exits with it."),
    dict(q="How does Rose end her account to Kate?",
         r=["“And that's all I'm going to tell you.”", "She begs Kate for forgiveness", "She runs out crying",
            "She promises never to see Danny again"], ok=0, voir="c_all",
         ex="Rose tells the facts on her own terms, then sets a limit: what happened at Lough Anna stays unsaid."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
