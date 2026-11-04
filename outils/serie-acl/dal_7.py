"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 7 : « Cracks », la fin de l'acte I (PDF de travail, p. 36-44).

Début : p. 36, didascalie « They dance off… » (Gerry et Chris quittent le jardin, la radio s'arrête net), Kate s'en prend à
Gerry, Agnes éclate et sort (p. 36-37) ; Kate reste seule avec Maggie. Fin : « BLACKOUT », fin de l'acte I (p. 44).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_7. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (les Brigades internationales, la guerre d'Espagne) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-7"
NOTION = "Dancing at Lughnasa"
NUM = 7
TITRE = "Cracks"
SUIVANT = "Part 8 · Three weeks later"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Okawa": "Oh-kah-wa",
                 "Kampala": "Kam-pah-la", "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rad}{q1}Gerry and Chris dance away down the lane. And the music on the wireless stops, suddenly, in mid-phrase.",
        "{-q1}In the silence, Kate, the woman who holds the house together, begins to break.",
        "{-tab_rad}{serie}Part seven: the end of Act One. Kate's fears, Jack's strange new faith… "
        "and a narrator who tells us how it all ends.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="The music stops suddenly in mid-phrase."),
        "serie": dict(type="mot", t="The end of Act One", g="Kate's fears · Jack's faith · the ending, told in advance",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 7", t="Cracks",
                      sous="The end of Act One · pages 36 – 44"),
    }),

    # ------------------------------------------------------------------ I. les fissures
    dict(id="fissures", chap="Hair cracks", fond="aube", humeur="tension",
         retenir="Kate admits that “control is slipping away”: the guardian of order is the first to crack.", beats=[
        "{tab_gle}{p1}Remember how part six ended. {p1.1}Kate had attacked Gerry: he has no sense of ordinary duty. "
        "{p1.2}Agnes exploded, called Kate a damned righteous bitch, and ran out, close to tears. "
        "{p1.3}Now, left alone with Maggie, Kate admits it: Agnes is right.",
        "Then she says this.",
        "{-p1}",
        ("C", "suddenly you realize that hair cracks are appearing everywhere; that control is slipping away; that the whole "
              "thing is so fragile that it can't be held together much longer.", "c_cracks", {"voix": "F"}),
        "{-c_cracks}{-tab_gle}{breche}Hair cracks: tiny lines, almost invisible, until the day everything breaks. "
        "{breche.1}It is Michael's widening breach from Part One. {breche.2}But now a character feels it, "
        "and it is Kate, the voice of duty and good order.",
        "{-breche}{peurs}Her fears pour out. {peurs.1}Chris will fall into depression when Gerry leaves. "
        "{peurs.2}Jack's superiors, says the doctor, had no choice but to send him home. "
        "{peurs.3}And the parish priest claims the school numbers are falling: she may lose her job. "
        "But the numbers aren't falling. Why is he telling me lies?",
        "Then, crying, she reaches the deepest fear.",
        "{-peurs}",
        ("C", "But what worries me most of all is Rose. If I died – if I lost my job – if this house were broken up – "
              "what would become of our Rosie?", "c_rosie", {"voix": "F"}),
        "{-c_rosie}{foi}If, if, if: each clause is a disaster she can already see. "
        "{foi.1}So she clings to God: I believe that… I do believe that. The more she says it, the less sure she sounds. "
        "{foi.2}Maggie rocks her in her arms. Kate, I love… She never finishes the sentence.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "p1": dict(type="liste", titre="After the dance · pages 36 – 37", items=[
            "Kate: Gerry has “no sense of ordinary duty”",
            "Agnes: “such a damned righteous bitch!”",
            "Kate: “She's right: I am a righteous bitch, amn't I?”"], marques=["K", "A", "K"], x=150, y=180, w=980),
        "c_cracks": dict(type="cit", a="Kate", o="p. 37", x=170, y=180, w=940),
        "breche": dict(type="illu", nom="breche", x=140, y=110, w=1000, h=440),
        "peurs": dict(type="liste", titre="Kate's fears · page 38", items=[
            "Chris: another depression when Gerry leaves",
            "Jack: his superiors “had no choice” but to send him home",
            "Her job: “the numbers in the school are falling”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_rosie": dict(type="cit", a="Kate", o="p. 38", x=170, y=190, w=940),
        "foi": dict(type="liste", titre="Holding on", cles=["believe"], items=[
            "“I believe that … I do believe that …”",
            "Maggie: “Kate … Kate, I love …” — unfinished"], marques=["1", "2"], x=170, y=210, w=940),
    }),

    # ------------------------------------------------------------------ II. Chris et l'enfant
    dict(id="chris", chap="A black bike", fond="aube", humeur="lumiere",
         retenir="Chris, eyes closed, chooses to believe Gerry: like Kate with God, she believes her way out of fear.", beats=[
        "{tab_don}{ch}Chris kneels by the boy at his kites. {ch.1}Gerry has a great new job, she whispers. "
        "{ch.2}And he has bought you a bicycle: a black bike, a man's bike. "
        "{ch.3}Is he coming back soon? asks the boy. Chris, eyes closed: Maybe… maybe. Yes! Yes, he is!",
        "{-ch}{-tab_don}{paral}See the parallel. {paral.g}Kate: I do believe that. {paral.d}Chris: yes, he is. "
        "Two sisters, two kinds of faith, one in God, one in Gerry. Both believe their way out of fear.",
        "{-paral}{rose}Gerry, Chris adds, sends his special love to Aggie. For me? says Agnes. "
        "Maggie quickly changes the subject. {rose.1}Roses for Jack's room, with a card saying roses, "
        "so the poor man won't go mad looking for the word.",
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "ch": dict(type="liste", titre="Chris and the boy · pages 38 – 39", items=[
            "Gerry has “a great new job”",
            "A bicycle: “a black bike – a man's bike”",
            "(Eyes closed.) “Maybe – maybe. Yes! Yes, he is!”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "paral": dict(type="cols", g="Kate", gq="“I do believe that …”", d="Chris",
                      dq="eyes closed: “Yes! Yes, he is!”", vs="=", repere="faith as a refuge"),
        "rose": dict(type="note", cles=["word"], terme="The kitchen · p. 39",
                     t="Gerry's “special love” to Agnes; then a card saying “ROSES” for Jack.",
                     etape="So that he “won't be demented looking for the word”.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. les esprits des ancêtres
    dict(id="jack", chap="Ancestral spirits", fond="nuit", humeur="mystere",
         retenir="Jack has taken in the religion of Ryanga: spirits, sacrifice, “ceremony”. Kate answers with routine.", beats=[
        "{tab_kil}{jk}Father Jack shuffles in. {jk.1}For a moment, he does not know where he is. "
        "{jk.2}He remembers the day he left: a picture… a camera-picture… a photograph! Even simple words escape him. "
        "{jk.3}Their mother's face, he says, showed nothing that day.",
        "{-jk}",
        ("C", "Do you think perhaps Mother didn't believe in the ancestral spirits?", "c_spirits"),
        "{-c_spirits}{-tab_kil}{mondes}Kate is shocked. Mother was a saintly woman, she says, going straight to heaven. "
        "Two worlds collide: the spirits of Africa, the Catholic heaven of Donegal.",
        "{-mondes}{ryanga}Jack goes on. {ryanga.1}A local medicine man, he says, saved a German priest the hospital could not save. "
        "{ryanga.2}In Ryanga, you kill a rooster or a goat to please the spirits. "
        "{ryanga.3}He hunts for the word. Exhibition? Show? Spectacle? Lost it.",
        "{-ryanga}{tab_kil2}{dc}The English district commissioner calls him the Irish Outcast and wants to keep him from going native. "
        "Jack refused his money, so he reported him to his superiors. {dc.1}And suddenly, the word comes back.",
        "{-dc}",
        ("C", "Ceremony! That's the word! How could I have forgotten that? The offering, the ritual, the dancing – a ceremony!",
         "c_ceremony"),
        "{-c_ceremony}{-tab_kil2}{langue}The priest forgets English, but remembers the pagan ceremony perfectly. "
        "{langue.1}You can always point, he says. {langue.2}Or make signs, says Maggie. Or dance.",
        "{-langue}{routine}When Jack praises love-children, Kate answers with a timetable: a walk, tea, the paper, medicine, bed. "
        "{routine.1}Until we have you back to what you were. Order, against change.",
    ], vis={
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "jk": dict(type="liste", titre="Jack comes in · page 40", items=[
            "“I'll be down at the bank of the river …”",
            "“a camera-picture? – a photograph!”",
            "Mother's face “showed nothing”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_spirits": dict(type="cit", a="Jack", o="p. 41", x=170, y=200, w=940),
        "mondes": dict(type="cols", g="Jack", gq="“the ancestral spirits”", d="Kate",
                       dq="“going straight to heaven”", vs="≠", repere="Ryanga / Donegal"),
        "ryanga": dict(type="liste", titre="Jack's Ryanga · pages 41 – 42", items=[
            "Okawa, Jack and the local medicine man",
            "A rooster or a goat killed “to please the spirits”",
            "“My vocabulary has deserted me.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "tab_kil2": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.25, .55, .45], a=[1.05, .5, .5],
                         legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "dc": dict(type="note", cles=["native"], terme="The district commissioner · p. 42",
                   t="“The Irish Outcast”: he wants to keep Jack from “going native”.",
                   etape="Jack refuses English money; he is reported to his superiors.", x=170, y=200, w=940),
        "c_ceremony": dict(type="cit", a="Jack", o="p. 42", x=170, y=190, w=940),
        "langue": dict(type="liste", titre="When words fail", items=[
            "Jack: “you can always point, Margaret”",
            "Maggie: “Or make signs.” … “Or dance.”"], marques=["1", "2"], x=150, y=210, w=980),
        "routine": dict(type="note", cles=["walk", "medicine", "bed"], terme="Kate's answer · p. 43",
                        t="A walk · tea · the paper · medicine · bed.",
                        etape="“until we have you back to what you were”", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. la prolepse
    dict(id="prolepse", chap="As it turned out", fond="nuit", humeur="tension",
         retenir="Michael gives the ending in the middle: Kate loses her job, Rose and Agnes leave for ever.", beats=[
        "{tab_don2}{proph}Now Michael turns to us. Kate's forebodings, he says, were not all that inaccurate. "
        "{proph.1}Jack had been sent home, not because his mind was confused, but for reasons that became clear later. "
        "{proph.2}Kate did lose her job, but more because of Jack than falling numbers. "
        "{proph.3}And she was right to worry about Rose… and about Agnes too.",
        "What she couldn't foresee was the speed of it.",
        "{-proph}",
        ("C", "the home would break up quite so quickly and that when she would wake up one morning in early September "
              "both Rose and Agnes would have left for ever.", "c_forever"),
        "{-c_forever}{-tab_don2}{scene}And meanwhile, on stage… {scene.1}Jack strikes two of the boy's kite sticks together. "
        "{scene.2}He beats a rhythm and begins to shuffle-dance, muttering strange sounds. "
        "{scene.3}The sisters watch him. Only Chris has her eyes closed: remembering.",
        "{-scene}{ger}Kate was wrong about one thing, says Michael: his father. {ger.1}Gerry did come back. "
        "{ger.2}He and Chris danced again, without music. No singing, no melody, no words. "
        "{ger.3}Then Gerry went off to fight with the International Brigade.",
        "{-ger}{brig}Outside the text: these were foreign volunteers who fought for the Republic in the Spanish Civil War, "
        "which began in July 1936, the very summer of the play.",
        "{-brig}{baton}Kate gently takes the sticks from Jack.",
        "{-baton}",
        ("C", "We'll leave these back where we found them, Jack. They aren't ours. They belong to the child.", "c_child",
         {"voix": "F"}),
        "{-c_child}{fin}The others watch with expressionless faces. Blackout. End of Act One. "
        "{fin.1}Kate puts the pagan rhythm back in its place, a child's game. But we already know her order will not hold.",
    ], vis={
        "tab_don2": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.15, .4, .5], a=[1.3, .6, .5],
                         legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "proph": dict(type="liste", titre="Kate was right … · page 43", items=[
            "Jack: sent home, “not because his mind was confused”",
            "Her job: lost, because of Jack, not falling numbers",
            "Rose … “and, had she known, about Agnes, too”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_forever": dict(type="cit", a="Michael", o="p. 43", x=170, y=190, w=940),
        "scene": dict(type="liste", titre="On stage, meanwhile · page 44", items=[
            "Jack strikes two kite sticks together",
            "A rhythm, a shuffle-dance, incomprehensible sounds",
            "The sisters watch; only Chris has her eyes closed"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "ger": dict(type="liste", titre="… but wrong about Gerry", items=[
            "He came back “in a couple of weeks”",
            "A dance “without music”: “no singing, no melody, no words”",
            "He leaves to fight with “the International Brigade”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "brig": dict(type="note", cles=["Spanish", "1936"], terme="Outside the text",
                     t="The International Brigades: foreign volunteers for the Republic in the Spanish Civil War (from July 1936).",
                     etape="History enters the play from outside Ballybeg.", x=170, y=200, w=940),
        "baton": dict(type="mot", t="Kate takes the sticks", g="gently", y=270, taille=80),
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
         r=["What would become of Rose", "Gerry's new job", "The broken wireless", "Jack's malaria"], ok=0, voir="c_rosie",
         ex="“If I died – if I lost my job – if this house were broken up – what would become of our Rosie?”"),
    dict(q="Why does Kate react so strongly to Jack's question about their mother?",
         r=["He suggests she might have believed in “the ancestral spirits”, not in heaven", "He says she never loved them",
            "He forgets her name", "He says she was not Catholic"], ok=0, voir="c_spirits",
         ex="Kate answers that Mother “knew she was going straight to heaven”: Ryanga's spirits against Donegal's Catholic heaven."),
    dict(q="Which word does Jack finally remember?",
         r=["Ceremony", "Photograph", "Sacrifice", "Spectacle"], ok=0, voir="c_ceremony",
         ex="“Ceremony! That's the word!”: he forgets simple English words but remembers the pagan ritual perfectly."),
    dict(q="According to Michael, why did Kate really lose her job?",
         r=["It had more to do with Father Jack than with falling numbers", "The school closed", "She left to look after Rose",
            "Gerry Evans complained about her"], ok=0, voir="proph",
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
