"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 6 : Gerry Evans (PDF de travail, p. 25-37).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu : cuisine et jardin vus ensemble, la scène partagée de Friel), en suivant les
didascalies pas à pas ; les répliques courtes s'affichent en bulles et sont lues par les voix des personnages.
L'enfant, « derrière ce buisson » (p. 31), n'est jamais vu : emplacement en pointillé ; Michael adulte n'est pas en scène.
Puis quatre répliques expliquées et l'analyse (inchangée).

De l'arrivée de Gerry (Maggie à la fenêtre, p. 25 : positions reprises de la fin de la partie 5) jusqu'à la sortie
d'Agnes en larmes (début de la p. 37) ; la question de Kate « And what was that all about? » ouvre la partie 7.
Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_6.
Citations courtes, à fin d'analyse ; le contexte hors texte (guerre d'Espagne)
et les révélations ultérieures de Michael (p. 64) sont dits comme tels. La chanson de la radio n'est pas nommée
(le texte dit seulement « An appropriate song of the period »).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-6"
NOTION = "Dancing at Lughnasa"
NUM = 6
TITRE = "Gerry Evans"
SUIVANT = "Part 7 · Cracks"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ballybeg": "Bally-beg", "Oughterard": "Ooh-ter-ard",
                 "Mundy": "Mundy", "Chrissie": "Chrissie", "Sligo": "Sly-go"}

GARCON = [1012, 262]      # « he's watching us from behind that bush » (p. 31) : l'enfant, jamais vu
GERRY_G, CHRIS_G = [880, 392], [790, 392]    # Gerry et Chris dans le jardin

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_lane}{q1}A man in a straw hat comes up the lane, swinging his cane. In the kitchen, five women panic.",
        "{-q1}{qui}He is Gerry Evans, Michael's father. Part six: his visit, his patter, and a dance in the garden.",
        ("P", 0.3),
        "{-qui}{-tab_lane}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_lane": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "q1": dict(type="question", t="Look who's coming up the lane!"),
        "qui": dict(type="mot", t="Gerry Evans", g="Michael's father · Chris's lover · Kate's “creature”", y=270, taille=96),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 6", t="Gerry Evans",
                      sous="The visit, the patter, the dance · pages 25 – 37"),
    }),

    # ------------------------------------------------------------------ I. le chaos dans la cuisine
    dict(id="chaos", chap="Chaos in the kitchen", fond="nuit", humeur="tension", beats=[
        "{jeu1}Page twenty-five. Part five ended in the middle of a row, when Maggie ran straight to the window.",
        ("C", "It's Gerry Evans, Chrissie.", "jeu1.1", {"voix": "F"}),
        ("C", "Oh, Jesus Christ Almighty.", "jeu1.2", {"voix": "F"}),
        "{jeu1.3}The news throws the sisters into chaos. Agnes picks up her knitting and works with excessive concentration. "
        "Rose and Maggie change their footwear. Everybody dashes about, bumping into one another, peeping out the window. "
        "The lines overlap. Only Chris stands absolutely still, too shocked to move.",
        ("C", "There's no welcome for that creature here.", "jeu1.4", {"voix": "F"}),
        "{jeu1.5}Shoes, shoelaces, Woodbine… Kate gives her orders.",
        ("C", "Behave quite normally. Be very calm and very dignified.", "jeu1.6", {"voix": "F"}),
        "{jeu1.7}Rose, at the window: there's nobody coming at all. Silence. {jeu1.8}Then Agnes puts down her knitting, "
        "rushes to the window, pushes Rose aside and looks out.",
        ("C", "Yes, he is. Maggie's right. There he is.", "jeu1.9", {"voix": "F"}),
        "{jeu1.10}A walking stick? A straw hat? It's Mr Evans all right. Rose cannot bear it: I just hate him! "
        "And she rushes off.",
        ("C", "Look at my hands, Kate – I'm shaking.", "jeu1.11", {"voix": "F"}),
        "{jeu1.12}Kate catches her shoulders: meet him outside, and send him packing. "
        "Chris does not move. She is about to cry. And Kate takes her in her arms.",
        ("C", "Of course ask him in. And give the creature his tea.", "jeu1.13", {"voix": "F"}),
        ("C", "But in the outside loft. And alone.", "jeu1.14", {"voix": "F"}),
        "{jeu1.15}Chris rushes to the mirror, and adjusts her hair and her clothes. "
        "{jeu1.16}Kate reads the paper, or pretends to. Agnes sits beside the radio and knits, with total concentration. "
        "Maggie stands at the side of the window.",
    ], vis={
        "jeu1": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Rose", "Chris"], etats=[
            dict(pos={"Kate": [260, 400], "Maggie": "fenetre", "Agnes": [420, 410], "Chris": [250, 470], "Rose": [330, 430]},
                 act={"Kate": "debout", "Maggie": "debout", "Agnes": "debout", "Chris": "debout", "Rose": "debout"},
                 surplis=["Chris"], objets={"kites": "kites"}, note="(MAGGIE runs on and goes straight to the window) (p. 25)"),
            dict(dit=["Maggie", "It's Gerry Evans, Chrissie."]),
            dict(dit=["Chris", "Oh, Jesus Christ Almighty."]),
            dict(pos={"Agnes": "tricot_a", "Chris": [250, 470]}, act={"Agnes": "tricote", "Chris": "fige"},
                 chemin={"Kate": [[260, 400], [400, 330], "fenetre", [200, 330], [300, 360]],
                         "Maggie": ["fenetre", [460, 330], [170, 320], [380, 300], [190, 330]],
                         "Rose": [[330, 430], [200, 340], "fenetre", [420, 320], [292, 250]]}, chemin_duree=12,
                 note="“Only CHRIS stands absolutely still, too shocked to move.” (p. 25)"),
            dict(dit=["Kate", "There's no welcome for that creature here."]),
            dict(note="“Who hid my Sunday shoes?” … “Has anybody got spare shoelaces?” (p. 26)"),
            dict(dit=["Kate", "Behave quite normally. Be very calm and very dignified."]),
            dict(note="“There's nobody coming at all.” (Rose, at window)"),
            dict(pos={"Agnes": "fenetre", "Rose": [360, 262]}, act={"Agnes": "debout"},
                 note="AGNES puts down her knitting, rushes to the window, pushes ROSE aside"),
            dict(dit=["Agnes", "Yes, he is. Maggie's right. There he is."]),
            dict(pos={"Rose": "arriere"}, duree=2.2, note="“I just hate him – hate him!” (As ROSE rushes off.) (p. 27)"),
            dict(pos={"Rose": "off"}, dit=["Chris", "Look at my hands, Kate – I'm shaking."]),
            dict(pos={"Kate": [308, 466]}, note="(KATE catches her shoulders.) … KATE now takes her in her arms."),
            dict(dit=["Kate", "Of course ask him in. And give the creature his tea."]),
            dict(dit=["Kate", "But in the outside loft. And alone."], note="(Firm again.)"),
            dict(pos={"Chris": [150, 350]}, act={"Chris": "range"}, sans_surplis=["Chris"],
                 note="CHRIS now rushes to the mirror and adjusts her hair and her clothes."),
            dict(pos={"Kate": [300, 380], "Agnes": [500, 270], "Maggie": "fenetre"},
                 act={"Kate": "debout", "Agnes": "tricote", "Maggie": "debout", "Chris": "debout"},
                 note="KATE reads the paper – or pretends to. AGNES sits beside the radio and knits. (p. 27)"),
        ]),
    }),

    # ------------------------------------------------------------------ II. Gerry dans le jardin
    dict(id="jardin", chap="Gerry in the garden", fond="nuit", humeur="lumiere", beats=[
        "{jeu2}And Gerry Evans enters, his step jaunty, swinging his cane, his straw hat well back on his head. "
        "He knows he is being watched. He is very ill at ease, but the smile never leaves his face. "
        "{jeu2.1}Chris goes out to the garden, where they meet. Gerry has a Welsh accent.",
        ("C", "How are you, Chrissie? Great to see you.", "jeu2.2"),
        ("C", "And how have you been for the past six months?", "jeu2.3"),
        ("C", "Thirteen months.", "jeu2.4", {"voix": "F"}),
        ("C", "July last year; July the seventh.", "jeu2.5", {"voix": "F"}),
        "{jeu2.6}Where does the time go? And today's visit, he says, was pure luck: a lift from a man he met in a bar in Sligo.",
        "{jeu2.7}Pause. In the kitchen, the sisters watch, and comment.",
        ("C", "Looks terrified, the poor fella.", "jeu2.8", {"voix": "F"}),
        ("C", "Terrified, my foot.", "jeu2.9", {"voix": "F"}),
        ("C", "Not just now.", "jeu2.10", {"voix": "F"}),
        ("C", "I'll give him three minutes.", "jeu2.11", {"voix": "F"}),
        "{jeu2.12}In the garden, Gerry asks after everyone. And one name twice.",
        ("C", "Tell her I was asking for her – Agnes.", "jeu2.13"),
        "{jeu2.14}He has given dancing lessons in Dublin, all last winter. He does a quick step and a pirouette.",
        ("C", "I had thousands of pupils – millions!", "jeu2.15"),
        ("C", "Fifty-three. I'm a liar. Fifty-one.", "jeu2.16"),
        "{jeu2.17}Now he sells gramophones: agent for the whole country. A man near Oughterard took four. Four gramophones? "
        "Four brochures. They both laugh.",
        ("C", "Don't turn round; but he's watching us from behind that bush.", "jeu2.18"),
        "{jeu2.19}Michael. We never see him. Gerry meant to bring him a bicycle, but they only had it in blue. "
        "{jeu2.20}Chris laughs. At the window, Maggie: you'd think he was the biggest toff in the world.",
        ("C", "Tinker, more likely! Loafer! Wastrel!", "jeu2.21", {"voix": "F"}),
    ], vis={
        "jeu2": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Chris", "Gerry"], etats=[
            dict(pos={"Kate": [300, 380], "Agnes": [500, 270], "Maggie": "fenetre", "Chris": [150, 350], "Gerry": "allee"},
                 act={"Kate": "debout", "Agnes": "tricote", "Maggie": "debout", "Chris": "debout", "Gerry": "debout"},
                 objets={"kites": "kites"}, cam="tout",
                 note="“He knows he is being watched.” (p. 27)"),
            dict(pos={"Gerry": GERRY_G, "Chris": CHRIS_G}, duree=4.0, note="CHRIS goes out to the garden where they meet."),
            dict(dit=["Gerry", "How are you, Chrissie? Great to see you."]),
            dict(dit=["Gerry", "And how have you been for the past six months?"], note="(p. 28)"),
            dict(dit=["Chris", "Thirteen months."]),
            dict(dit=["Chris", "July last year; July the seventh."]),
            dict(note="“Bit of good luck that, wasn't it?” (Gerry)"),
            dict(note="(Pause.)"),
            dict(dit=["Maggie", "Looks terrified, the poor fella."]),
            dict(dit=["Kate", "Terrified, my foot."]),
            dict(dit=["Agnes", "Not just now."]),
            dict(dit=["Kate", "I'll give him three minutes."]),
            dict(note="“And Rose and Kate?” … “And Agnes?” (p. 29)"),
            dict(dit=["Gerry", "Tell her I was asking for her – Agnes."]),
            dict(act={"Gerry": "danse"}, note="(He does a quick step and a pirouette.) (p. 30)"),
            dict(act={"Gerry": "debout"}, dit=["Gerry", "I had thousands of pupils – millions!"]),
            dict(dit=["Gerry", "Fifty-three. I'm a liar. Fifty-one."]),
            dict(note="“Minerva Gramophones – The Wise Buy.” … (They both laugh.)"),
            dict(dit=["Gerry", "Don't turn round; but he's watching us from behind that bush."], objets={"garcon": GARCON},
                 note="(p. 31)"),
            dict(note="“He's making kites if you don't mind.” (Chris)"),
            dict(note="“you'd think he was the biggest toff in the world” (Maggie)"),
            dict(dit=["Kate", "Tinker, more likely! Loafer! Wastrel!"]),
        ]),
    }),

    # ------------------------------------------------------------------ III. présages et Espagne
    dict(id="presages", chap="Omens, and Spain", fond="nuit", humeur="lumiere", beats=[
        "{jeu3}Page thirty-two. Gerry met a cow with a single horn on the road, a good omen. And it winked at him.",
        ("C", "That was no cow you met – that was a unicorn.", "jeu3.1", {"voix": "F"}),
        "{jeu3.2}Then: a single magpie! A bad omen, one for sorrow. He raises his stick as a gun. Bang! Missed. They both laugh.",
        "{jeu3.3}In the kitchen, Kate: laughing? Beyond my comprehension. Like so many things, Kate, says Agnes.",
        "{jeu3.4}Then Gerry's news. He is thinking of going away for a while. Home to Wales, asks Chris?",
        ("C", "Wales isn't my home any more. My home is here – well, Ireland.", "jeu3.5"),
        "{jeu3.6}He is going to Spain, to do a spot of fighting, with the International Brigade. Why?",
        ("C", "Give Evans a Big Cause and he won't let you down.", "jeu3.7"),
        ("C", "It's only everyday stuff he's not so successful at.", "jeu3.8"),
        "{jeu3.9}He's still watching us, says Gerry. Does he know my name? Of course he does. A very handsome child. With your eyes.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Chris", "Gerry"], etats=[
            dict(pos={"Kate": [300, 380], "Agnes": [500, 270], "Maggie": "fenetre", "Chris": CHRIS_G, "Gerry": GERRY_G},
                 act={"Kate": "debout", "Agnes": "tricote", "Maggie": "debout", "Chris": "debout", "Gerry": "debout"},
                 objets={"kites": "kites", "garcon": GARCON}, cam="tout",
                 note="“A cow with a single horn coming straight out of the middle of its forehead.” (p. 32)"),
            dict(dit=["Chris", "That was no cow you met – that was a unicorn."]),
            dict(note="“one for sorrow.” (His stick as a gun.) “Bang! Missed.” (p. 33)"),
            dict(note="“Laughing? Absolutely beyond my comprehension.” (Kate)"),
            dict(note="“Thinking of going away for a while, Chrissie.”"),
            dict(dit=["Gerry", "Wales isn't my home any more. My home is here – well, Ireland."]),
            dict(note="“to do a spot of fighting. With the International Brigade.”"),
            dict(dit=["Gerry", "Give Evans a Big Cause and he won't let you down."]),
            dict(dit=["Gerry", "It's only everyday stuff he's not so successful at."]),
            dict(note="“He's still watching us. He thinks we don't see him.”"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. la danse dans le jardin
    dict(id="danse", chap="A dance in the garden", fond="nuit", humeur="lumiere", beats=[
        "{jeu4}Page thirty-four. An appropriate song of the period plays softly from the radio. The text gives no title.",
        ("C", "Good for you, Aggie. What did you do to it?", "jeu4.1", {"voix": "F"}),
        ("C", "I didn't touch it.", "jeu4.2", {"voix": "F"}),
        "{jeu4.3}Turn that thing off, Aggie, says Kate. Agnes does not. "
        "{jeu4.4}In the garden, Gerry asks after Agnes again: she was the one that seemed to object least to me. "
        "They listen to the music.",
        "{jeu4.5}Suddenly he takes Chris in his arms, and dances.",
        ("C", "They're watching us.", "jeu4.6", {"voix": "F"}),
        ("C", "Hope so. And Kate.", "jeu4.7"),
        "{jeu4.8}He swings her round and round, and dances her lightly, elegantly across the garden, singing the song to her.",
        ("C", "They're dancing.", "jeu4.9", {"voix": "F"}),
        ("C", "He has not! The animal!", "jeu4.10", {"voix": "F"}),
        "{jeu4.11}Kate flings the paper aside, and joins Maggie at the window. Maggie calls Agnes over.",
        ("C", "I'm busy! For God's sake can't you see I'm busy!", "jeu4.12", {"voix": "F"}),
        "{jeu4.13}Maggie turns and looks at her in amazement. And Kate, at the window, slowly changes.",
        ("C", "Her whole face alters when she's happy, doesn't it?", "jeu4.14", {"voix": "F"}),
        ("C", "They dance so well together. They're such a beautiful couple.", "jeu4.15", {"voix": "F"}),
        "{jeu4.16}She's as beautiful as Bernie O'Donnell any day, isn't she? "
        "And Maggie moves slowly away from the window, and sits motionless.",
        "{jeu4.17}In the garden, Gerry asks: do you know the words? I never know any words, says Chris. "
        "Neither do I, he says. Doesn't matter. This is more important. Then: marry me, Chrissie. I don't think so, Gerry.",
        ("C", "But you'd walk out on me again.", "jeu4.18", {"voix": "F"}),
        ("C", "Don't talk any more; no more words. Just dance me down the lane and then you'll leave.", "jeu4.19", {"voix": "F"}),
        "{jeu4.20}They dance off. The music continues for a few seconds, {jeu4.21}and stops suddenly, in mid-phrase. "
        "Maggie goes to the set, slaps it, turns it off. Kate moves away from the window.",
        ("C", "Whatever's wrong with it, that's all it seems to last – a few minutes at a time.", "jeu4.22", {"voix": "F"}),
        "{jeu4.23}Kate goes on: Christina's heart gets crushed again; the creature has no sense of ordinary duty. "
        "{jeu4.24}Agnes rises, and goes to the back door. Kate does not stop.",
        ("C", "You are such a damned righteous bitch! And his name is Gerry! – Gerry! Gerry!", "jeu4.25", {"voix": "F"}),
        "{jeu4.26}Now to the point of tears, Agnes runs off. Kate and Maggie are left alone. Part seven starts here.",
    ], vis={
        "jeu4": dict(type="jeu", persos=["Kate", "Maggie", "Agnes", "Chris", "Gerry"], etats=[
            dict(pos={"Kate": [300, 380], "Agnes": [500, 270], "Maggie": "fenetre", "Chris": CHRIS_G, "Gerry": GERRY_G},
                 act={"Kate": "debout", "Agnes": "tricote", "Maggie": "debout", "Chris": "debout", "Gerry": "debout"},
                 objets={"kites": "kites", "garcon": GARCON}, cam="tout", radio=True,
                 note="(An appropriate song of the period plays softly from the radio.) (p. 34)"),
            dict(dit=["Maggie", "Good for you, Aggie. What did you do to it?"]),
            dict(dit=["Agnes", "I didn't touch it."]),
            dict(note="“Turn that thing off, Aggie, would you?” (AGNES does not.)"),
            dict(note="“Of all your sisters Agnes was the one that seemed to object least to me.”"),
            dict(pos={"Chris": [808, 392], "Gerry": [862, 392]}, act={"Chris": "danse_douce", "Gerry": "danse_douce"},
                 note="(Suddenly he takes her in his arms and dances.)"),
            dict(dit=["Chris", "They're watching us."], note="(p. 35)"),
            dict(dit=["Gerry", "Hope so. And Kate."], note="“And Father Jack.” “Better still! Terrific!”"),
            dict(chemin={"Chris": [[808, 392], [690, 440], [750, 500], [930, 470], [950, 380], [808, 392]],
                         "Gerry": [[862, 392], [744, 440], [804, 500], [984, 470], [1004, 380], [862, 392]]},
                 chemin_duree=14, note="He dances her lightly, elegantly across the garden. He sings the song to her."),
            dict(dit=["Maggie", "They're dancing."]),
            dict(dit=["Kate", "He has not! The animal!"], note="“He has her in his arms.” (Maggie)"),
            dict(pos={"Kate": [345, 250]}, duree=1.8, note="She flings the paper aside and joins MAGGIE at the window."),
            dict(dit=["Agnes", "I'm busy! For God's sake can't you see I'm busy!"]),
            dict(note="(MAGGIE turns and looks at her in amazement.)"),
            dict(dit=["Kate", "Her whole face alters when she's happy, doesn't it?"]),
            dict(dit=["Kate", "They dance so well together. They're such a beautiful couple."]),
            dict(pos={"Maggie": [400, 330]}, act={"Maggie": "assis"}, duree=3.0,
                 note="(MAGGIE moves slowly away from the window and sits motionless.)"),
            dict(note="“Marry me, Chrissie.” … “I don't think so, Gerry.” (p. 36)"),
            dict(dit=["Chris", "But you'd walk out on me again."]),
            dict(dit=["Chris", "Don't talk any more; no more words. Just dance me down the lane and then you'll leave."]),
            dict(pos={"Chris": [1110, 330], "Gerry": [1110, 300]}, duree=5.0, note="(They dance off.)"),
            dict(pos={"Chris": "off", "Gerry": "off", "Maggie": "radio", "Kate": [300, 380]},
                 act={"Chris": "debout", "Gerry": "debout", "Maggie": "debout", "Kate": "debout"}, radio=False, duree=2.0,
                 note="The music stops suddenly in mid-phrase. MAGGIE slaps the set, turns it off."),
            dict(dit=["Maggie", "Whatever's wrong with it, that's all it seems to last – a few minutes at a time."]),
            dict(note="“the creature has no sense of ordinary duty” (Kate)"),
            dict(pos={"Agnes": "porte"}, act={"Agnes": "debout"}, duree=2.0, note="(AGNES rises and goes to the back door.)"),
            dict(dit=["Agnes", "You are such a damned righteous bitch! And his name is Gerry! – Gerry! Gerry!"]),
            dict(pos={"Agnes": "off"}, note="(Now to the point of tears, she runs off.) (p. 37)"),
        ]),
    }),

    # ------------------------------------------------------------------ V. répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="Kate's “outside loft”, Gerry's “Big Cause”, Kate's “beautiful couple”, Chris's “no more words”.", beats=[
        "{quatre}Four lines from this part are worth knowing by heart.",
        "First, Kate, holding Chris in her arms.{-quatre}",
        ("C", "Of course ask him in. And give the creature his tea. And stay the night if he wants to. But in the outside loft. "
              "And alone.", "c_tea", {"voix": "F"}),
        "{-c_tea}{deux}First, tenderness. Then, firm again: the outside loft, and alone. Love, but respectability first. "
        "And creature: she will not even use his first name.",
        "Then Gerry.{-deux}",
        ("C", "Give Evans a Big Cause and he won't let you down. It's only everyday stuff he's not so successful at.", "c_cause"),
        "{-c_cause}{cause}His most honest line. A big cause, yes. Everyday duty, a son behind a bush: no. "
        "Context, from outside the play: the Spanish Civil War began in July nineteen thirty-six. The outside world walks into Ballybeg.",
        "Then Kate again, at the window.{-cause}",
        ("C", "Her whole face alters when she's happy, doesn't it? They dance so well together. They're such a beautiful couple.",
         "c_face", {"voix": "F"}),
        "{-c_face}{face}From the animal to a beautiful couple, in a few pauses. Under the judgement, love.",
        "And Chris.{-face}",
        ("C", "Don't talk any more; no more words. Just dance me down the lane and then you'll leave.", "c_lane", {"voix": "F"}),
        "{-c_lane}{lane}Chris knows who he is, and chooses the dance anyway: no more words. "
        "And Maggie's verdict on the radio fits them too: a few minutes at a time.",
    ], vis={
        "quatre": dict(type="mot", t="Four lines to know", g="Kate · Gerry · Kate · Chris · pages 27 – 36", y=250, taille=80),
        "c_tea": dict(type="cit", a="Kate", o="p. 27", x=170, y=170, w=940),
        "deux": dict(type="cols", g="Tenderness", gq="“Of course ask him in”", d="The rules",
                     dq="“in the outside loft. And alone.”", vs="→", repere="love / respectability"),
        "c_cause": dict(type="cit", a="Gerry", o="p. 33", x=170, y=200, w=940),
        "cause": dict(type="cols", g="A Big Cause", gq="Spain, the International Brigade", d="Everyday stuff",
                      dq="a son, a home, ordinary duty", vs="≠", repere="context (outside the play): Spain, July 1936"),
        "c_face": dict(type="cit", a="Kate", o="p. 35", x=170, y=170, w=940),
        "face": dict(type="note", cles=["animal", "love"], terme="Kate · p. 35",
                     t="From “The animal!” to “such a beautiful couple”.",
                     etape="Under the judgement, love.", x=170, y=200, w=940),
        "c_lane": dict(type="cit", a="Chris", o="p. 36", x=170, y=170, w=940),
        "lane": dict(type="note", cles=["words", "minutes"], terme="Chris · p. 36",
                     t="She refuses to marry him, and chooses the dance: “no more words”.",
                     etape="Like the radio: “a few minutes at a time”.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Gerry the performer, the watchers in the kitchen, the dance as escape, and the subtext of Agnes and Kate.", beats=[
        "{a1}Now the analysis. Four ideas. One: Gerry is a performer. He knows he is being watched, and everything is a show. "
        "His charm is unreliable, and we see through it.",
        "Irony in hindsight too: on page sixty-four, Michael reveals that Gerry had a wife and three children in Wales. "
        "So much for: Wales isn't my home any more.",
        "{-a1}{a2}Two: the watchers. The split stage makes the sisters an audience inside the play, almost a chorus. "
        "We watch them watching, and their comments reveal them more than Gerry.",
        "{-a2}{a3}Three: the dance. Chris and Gerry cannot talk honestly, but they can dance: courtship and escape, "
        "beyond words. But it is brief, like happiness in this house. And Chris's joy comes with humiliation, "
        "in front of her sisters.",
        "{-a3}{a4}Four: subtext. Agnes never says she loves Gerry. But she will not look, she snaps, she defends his name. "
        "This is subtext, not a stated fact: write that her reactions suggest a secret attachment.",
        "{-a4}{carte}So, this part can support essays on {carte.1}performance and truth, {carte.2}watching and judging, "
        "{carte.3}dance as escape, {carte.4}and the outside world breaking into Ballybeg.",
    ], vis={
        "a1": dict(type="note", cles=["performer", "unreliable"], terme="1 · Gerry, the performer",
                   t="“He knows he is being watched”: six months for thirteen, “I'm a liar”, four brochures.",
                   etape="Unreliable charm, and irony in hindsight: his family in Wales (p. 64).", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["split", "chorus"], terme="2 · The watchers",
                   t="A split stage: the garden performs, the kitchen comments, like a chorus.",
                   etape="We watch the sisters watching. Michael watches too.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["words", "escape"], terme="3 · The dance",
                   t="“no more words. Just dance me down the lane”",
                   etape="Courtship and escape… “a few minutes at a time”.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["subtext"], terme="4 · Subtext",
                   t="Agnes: “Not just now”, “I'm busy!”, “his name is Gerry!”",
                   etape="Never said: Agnes's feelings. Kate's tenderness under her anger.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="GERRY'S VISIT", branches=[
            dict(t="Performance", items=["“He knows he is being watched”", "“I'm a liar”", "irony: Wales (p. 64)"]),
            dict(t="Watching", items=["a split stage", "the kitchen as chorus", "Michael behind the bush"]),
            dict(t="The dance", items=["“no more words”", "courtship and escape", "“a few minutes at a time”"]),
            dict(t="Outside world", items=["Spain, the International Brigade", "gramophones, the radio", "Kate's respectability"])]),
    }),
]

QUIZ = [
    dict(q="How long has it been since Gerry's last visit?",
         r=["Thirteen months, though he says six", "Six months, as he says", "Two weeks", "Seven years"], ok=0, voir="jeu2.4",
         ex="Gerry asks about “the past six months”; Chris corrects him: “Thirteen months… July the seventh.” She counts, he does not."),
    dict(q="What does Kate finally allow Gerry to do?",
         r=["Have his tea and stay the night, but in the outside loft, alone", "Marry Chris at once",
            "Take Michael to Wales", "Nothing: she throws him out herself"], ok=0, voir="c_tea",
         ex="Tenderness first (“Of course ask him in”), then the rules: “But in the outside loft. And alone.”"),
    dict(q="Who is watching Gerry and Chris from behind a bush?",
         r=["Michael, their son", "Father Jack", "Rose", "Kate"], ok=0, voir="jeu2.18",
         ex="“Don't turn round; but he's watching us from behind that bush.” The future narrator observes his father."),
    dict(q="Why is Gerry going to Spain?",
         r=["To fight with the International Brigade", "To sell gramophones", "To find work as a dance teacher",
            "To visit his family"], ok=0, voir="c_cause",
         ex="“to do a spot of fighting. With the International Brigade.” Context (outside the play): the Spanish Civil War began in July 1936."),
    dict(q="How does Chris answer Gerry's proposal?",
         r=["“Just dance me down the lane and then you'll leave.”", "She says yes, for after his return",
            "She asks Kate's permission", "She runs into the house"], ok=0, voir="c_lane",
         ex="She refuses (“you'd walk out on me again”) but chooses the dance: “no more words”."),
    dict(q="What do Agnes's reactions in this part suggest?",
         r=["A hidden attachment to Gerry: subtext, never stated", "That she hates music",
            "That she wants to marry Father Jack", "Nothing: she is not on stage"], ok=0, voir="a4",
         ex="She refuses to look, snaps “I'm busy!”, defends “his name is Gerry!” and runs off in tears."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Glenties (Thpohl, public domain); valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
