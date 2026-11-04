"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 10 : « Rose goes missing » (PDF de travail, p. 58-62).

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

    # ------------------------------------------------------------------ I. où est Rose ?
    dict(id="absente", chap="Not in her bed", fond="aube", humeur="tension",
         retenir="Rose left Agnes at the quarry, in her good clothes, with milk and money: Maggie guesses Danny Bradley.", beats=[
        "{tab_gle}{rappel}Just before, {rappel.1}Kate and Chris learned that the glove money is gone: "
        "a new factory in Donegal Town. {rappel.2}They will tell Agnes and Rose later. "
        "{rappel.3}Then Agnes comes back from the bilberries… alone.",
        "{-rappel}{recit}Rose is not in her bed. Kate takes charge: start at the beginning. "
        "{recit.1}They left together just after one o'clock and walked to the old quarry. "
        "{recit.2}Rose said she wasn't feeling well, and sat in the sun. "
        "{recit.3}Agnes fell into a bush, Rose laughed, then said she would go home and sleep.",
        "{-recit}{indices}Agnes begins to cry. And the clues come out. "
        "{indices.1}Rose was wearing her good shoes, her blue cardigan, her good skirt. I'm some toff, she said. "
        "{indices.2}A bottle of milk in one of her cans. {indices.3}Half a crown: all the money she has.",
        "{-indices}{-tab_gle}{danny}Then Maggie, softly, puts it together: Danny Bradley… Lough Anna… up in the back hills.",
        "Remember part two? Rose told them her plan: a boat on Lough Anna, a bottle of milk, chocolate biscuits. "
        "Chris warned her then: Danny Bradley is a married man. Now they understand.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "rappel": dict(type="liste", titre="Just before · pages 56 – 57", items=[
            "The gloves: a new factory in Donegal Town",
            "Kate: “Tell them later.”",
            "Agnes comes back with the bilberries, alone"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "recit": dict(type="liste", titre="Agnes's account · page 58", items=[
            "Just after one o'clock: the walk to the quarry",
            "Rose “wasn't feeling well”: she sits in the sun",
            "Agnes falls into a bush; Rose laughs, goes “home”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "indices": dict(type="liste", titre="The clues · page 59", items=[
            "Her good shoes, blue cardigan, good skirt: “I'm some toff”",
            "A bottle of milk in one of her cans",
            "“She had half-a-crown. That's all she has.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "danny": dict(type="mot", t="Danny Bradley…", g="“Lough Anna … up in the back hills” · Maggie, softly (p. 59)",
                      y=250, taille=92),
    }),

    # ------------------------------------------------------------------ II. l'affaire Bradley
    dict(id="bradley", chap="This Bradley business", fond="nuit", humeur="tension",
         retenir="Kate interrogates Agnes and fears a scandal; Maggie takes command. The head of the house loses control.", beats=[
        "{chris}Chris explains: Rose has some silly notion about that scamp, Bradley. She believes he's in love with her. "
        "And Kate turns, not on Bradley, but on Agnes.",
        "{-chris}",
        ("C", "I've often seen you and Rose whispering together. What plot has been hatched between Rose and Mr. Bradley?",
         "c_plot", {"voix": "F"}),
        "{-c_plot}{interro}Plot, hatched: Kate speaks like a judge facing a conspiracy. "
        "{interro.1}You're lying to me, Agnes! You're withholding! {interro.2}Agnes swears she knows nothing. "
        "{interro.3}Kate: I want to know everything you know! Now!",
        "{-interro}{maggie}And then, something new. Maggie, the joker, stops her: That'll do, Kate! Stop that at once! "
        "{maggie.1}Calmly, she organises the search. {maggie.2}Chris takes the upper fields, Agnes the lower side, "
        "Kate the old well. {maggie.3}And Maggie will go to the police. Kate refuses.",
        "{-maggie}",
        ("C", "You're going to no police, Maggie. If she's mixed up with that Bradley creature, I'm not going to have it "
              "broadcast all over –", "c_police", {"voix": "F"}),
        "{-c_police}{honte}Rose may be hurt, but Kate's first fear is the parish. Broadcast: the language of the wireless. "
        "In this small Catholic world, shame travels fast. "
        "{honte.1}Maggie does not even argue: I'm going to the police, and you'll do what I told you to do. "
        "In part seven, Kate felt that control was slipping away. Here, it slips out of her hands.",
    ], vis={
        "chris": dict(type="note", cles=["scamp", "love"], terme="Chris · p. 59",
                      t="“She has some silly notion about that scamp, Bradley.”",
                      etape="“She believes he's in love with her.”", x=170, y=200, w=940),
        "c_plot": dict(type="cit", a="Kate, to Agnes", o="p. 59", x=170, y=200, w=940),
        "interro": dict(type="dialogue", lignes=["Kate: “You're lying to me, Agnes! You're withholding!”",
                                                  "Agnes: “Honest to God, all I know is what Chris has just –”",
                                                  "Kate: “I want to know everything you know! Now!”"],
                        src="p. 59", x=170, y=170, w=980),
        "maggie": dict(type="liste", titre="Maggie takes command · page 59", items=[
            "“That'll do, Kate! Stop that at once!” — then, calmly",
            "Chris: upper fields · Agnes: lower side · Kate: the old well",
            "Maggie: “I'm going into the town to tell the police.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_police": dict(type="cit", a="Kate", o="p. 59", x=170, y=200, w=940),
        "honte": dict(type="cols", g="Kate", gq="“I'm not going to have it broadcast”: the parish, the shame", d="Maggie",
                      dq="“you'll do what I told you to do”: find Rose", vs="≠", repere="reputation / Rose herself"),
    }),

    # ------------------------------------------------------------------ III. le retour
    dict(id="retour", chap="The return", fond="aube", humeur="mystere",
         retenir="Rose returns calm, in her good clothes, a red poppy in her hand: “Her face reveals nothing”.", beats=[
        "{tab_don2}{vue}Suddenly Chris cries: There she is! Look! {vue.1}Maggie holds her back. "
        "{vue.2}The four sisters watch Rose cross the garden, two from the window, two from the door. "
        "{vue.3}Rose has no idea she is being watched. And the stage direction says something remarkable.",
        "{-vue}",
        ("C", "Indeed, had we not seen the Rose of Act One, we might not now be immediately aware of her disability.", "c_disab"),
        "{-c_disab}{femme}In her good clothes, she might be any youngish country woman, returning from a long walk on a summer day. "
        "{femme.1}For a moment, Friel lets us see Rose as Danny may see her: a woman, not a problem to be managed. "
        "{femme.2}From her right hand hangs a red poppy, picked along the road.",
        "{-femme}",
        ("C", "Her face reveals nothing – but nothing is being deliberately concealed.", "c_face"),
        "{-c_face}{baies}A beautiful paradox. Rose is not hiding anything… and yet we learn nothing. "
        "{baies.1}She thrusts a fistful of Agnes's bilberries into her mouth, {baies.2}looks at her stained fingers, "
        "wipes them on her skirt. {baies.3}All of it calmly, naturally.",
        "{-baies}{-tab_don2}{questions}Agnes rushes out, wants to hug her, but only catches her arm. "
        "{questions.1}Rose: They're nice, Aggie. They're sweet. {questions.2}Your stomach? Oh, I'm fine now. "
        "{questions.3}You went into Ballybeg, didn't you? Pause. Rose looks from one to the other.",
        "{-questions}{menu}So Maggie fills the silence: she's home safe and sound. "
        "{menu.1}Then she performs tonight's menu like a grand chef: three eggs for seven, {menu.2}no, eight, says Chris: "
        "Gerry is up the sycamore. {menu.3}Eggs Ballybeg! Comedy, once again, to cover the fear.",
    ], vis={
        "tab_don2": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.15, .4, .5], a=[1.3, .6, .5],
                         legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "vue": dict(type="liste", titre="“There she is!” · page 60", items=[
            "Maggie catches Chris's arm and restrains her",
            "The four sisters watch: two at the window, two at the door",
            "Rose “is unaware of their anxious scrutiny”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_disab": dict(type="cit", a="Stage direction", o="p. 60", x=170, y=200, w=940),
        "femme": dict(type="liste", titre="Rose, seen differently", items=[
            "“any youngish country woman, carefully dressed, not unattractive”",
            "From her right hand: a red poppy, “plucked casually along the road”"], marques=["1", "2"],
                      x=150, y=200, w=980),
        "c_face": dict(type="cit", a="Stage direction", o="p. 60", x=170, y=200, w=940),
        "baies": dict(type="liste", titre="The bilberries · page 60", items=[
            "a fistful of berries thrust into her mouth",
            "she looks at her stained fingers, wipes them on her skirt",
            "“not dreamily, abstractedly, but calmly, naturally”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "questions": dict(type="dialogue", lignes=["Rose: “They're nice, Aggie. They're sweet.”",
                                                    "Rose: “Oh, yes. Oh, I'm fine now, thanks.”",
                                                    "Chris: “You went into Ballybeg, didn't you?” (Pause.)"],
                          src="pp. 60 – 61", x=170, y=170, w=980),
        "menu": dict(type="liste", titre="Maggie's menu · page 61", items=[
            "“three eggs between the seven of us”",
            "Chris: “There are eight of us, Maggie.” (Gerry)",
            "“Eggs Ballybeg”: Maggie's comedy covers the fear"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ IV. Lough Anna
    dict(id="lough", chap="Lough Anna", fond="nuit", humeur="tension",
         retenir="Rose tells the facts on her own terms (boat, picnic, fires, Rosebud) then stops: “that's all I'm going to tell you.”",
         beats=[
        "{kate}Rose heads for the bedroom door. Just as she is about to go out, Kate speaks. "
        "I want to know where you have been, Rose. {kate.1}Rose stops. Almost inaudible: Lough Anna. "
        "{kate.2}Kate fires short questions, like a prosecutor. Did you meet somebody? Yes. Had you arranged it? "
        "{kate.3}And Rose, very simply: I had arranged to meet Danny Bradley there, Kate.",
        "{-kate}{recit2}Then she tells her story, turning to each sister in turn. "
        "{recit2.1}He brought her out in his father's blue boat; a picnic on the lake, milk and chocolate biscuits. "
        "{recit2.2}Then up through the back hills, where he showed her what was left of the Lughnasa fires. "
        "{recit2.3}Young Sweeney, the boy who got burned, is on the mend. "
        "{recit2.4}A very peaceful place: nobody there but Danny and me. He calls me his Rosebud.",
        "Then he walked her down to the workhouse gate, and she came home alone. And she ends with this.",
        "{-recit2}",
        ("C", "And that's all I'm going to tell you.", "c_all", {"voix": "F"}),
        "{-c_all}{sortie}To all of them: that's all any of you are going to hear. "
        "{sortie.1}She exits, her shoes in one hand, the poppy in the other. "
        "Rose, the sister everyone protects, has just set the limits of what Kate can know.",
    ], vis={
        "kate": dict(type="dialogue", lignes=["Rose: (inaudible) “Lough Anna.”",
                                               "Kate: “Had you arranged to meet somebody there?”",
                                               "Rose: “I had arranged to meet Danny Bradley there, Kate.”"],
                     src="p. 62", x=170, y=170, w=980),
        "recit2": dict(type="liste", titre="Rose's account · page 62", items=[
            "“his father's blue boat”: a picnic on the lake",
            "the back hills: “what was left of the Lughnasa fires”",
            "young Sweeney “on the mend”: his legs will be scarred",
            "“nobody there but Danny and me” · “his Rosebud”"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "c_all": dict(type="cit", a="Rose, to Kate", o="p. 62", x=170, y=200, w=940),
        "sortie": dict(type="note", cles=["shoes", "poppy"], terme="Stage direction · p. 62",
                       t="“She exits, her shoes in one hand, the poppy in the other.”",
                       etape="Rose decides what the others will know.", x=170, y=200, w=940),
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
            "Danny Bradley came to the house that morning", "Agnes saw them together at the quarry"], ok=0, voir="indices",
         ex="Good shoes, blue cardigan, good skirt, milk, half-a-crown: exactly the plan Rose described in Act One (p. 5)."),
    dict(q="Whom does Kate accuse of hiding the truth?",
         r=["Agnes", "Chris", "Maggie", "Father Jack"], ok=0, voir="c_plot",
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
         r=["A red poppy", "Danny's silver charm", "A bottle of milk", "A kite"], ok=0, voir="femme",
         ex="“From her right hand hangs a red poppy that she plucked casually along the road.” She exits with it."),
    dict(q="How does Rose end her account to Kate?",
         r=["“And that's all I'm going to tell you.”", "She begs Kate for forgiveness", "She runs out crying",
            "She promises never to see Danny again"], ok=0, voir="c_all",
         ex="Rose tells the facts on her own terms, then sets a limit: what happened at Lough Anna stays unsaid."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
