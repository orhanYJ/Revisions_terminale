"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 12 : « The last afternoon » (PDF de travail, p. 64-74).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu), en suivant les didascalies pas à pas ; les répliques courtes s'affichent en
bulles et sont lues (voix des sœurs, voix d'homme pour Jack et Gerry). Gerry, perché dans le sycomore, est « Off » : on ne le
voit pas, ses répliques sont en bandeau. Quatre tableaux : le sycomore et le « système » de Jack (p. 64-66) ; « Anything Goes »
à la radio, Gerry danse avec Agnes, Chris coupe la radio (p. 66-69) ; Vera McLaughlin, la nappe au jardin, le coq mort
(p. 69-71) ; l'uniforme blanc de Jack, l'échange des chapeaux, les cerfs-volants enfin montrés, la devinette oubliée (p. 71-74).
Puis cinq répliques à connaître, l'analyse et le quiz.

Début : p. 64, juste après la didascalie « MICHAEL exits » (Chris appelle Gerry, perché dans le sycomore).
Fin : p. 74, juste avant « (MAGGIE moves into the kitchen. MICHAEL enters. …) » (la devinette oubliée de Maggie).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_12. Citations courtes, à fin d'analyse ; le reste est résumé.
Les paroles de la chanson (« Anything Goes », nommée p. 66) ne sont pas citées. Ce qui ne vient pas du texte
(Cole Porter, 1934) est dit comme tel. La perte de l'emploi de Kate n'est pas annoncée dans ces pages : elle n'est
rappelée que par la prolepse de Michael (p. 43).
Choix de mise en scène : Agnes assise dès le début (Gerry « pulls her to her feet », p. 67) ; les chapeaux posés au sol pendant
le rituel ne sont pas dessinés (le moteur ne sait pas poser un chapeau) : les deux hommes s'inclinent, puis les chapeaux
reparaissent échangés ; la nappe et la canne ne sont pas dessinées. Les cerfs-volants, posés contre le banc depuis la p. 45,
ne montrent leurs visages qu'à la didascalie « For the first time we all see the images » (p. 73).
Coquille du PDF évitée (« Yes. Yes Whatever you say » : coupé à « Whatever you say, Aggie. »).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-12"
NOTION = "Dancing at Lughnasa"
NUM = 12
TITRE = "The last afternoon"
SUIVANT = "Part 13 · The final tableau"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Okawa": "Oh-kah-wa",
                 "McLaughlin": "Mac-Lock-lin", "Pius": "Pie-us", "Mundy": "Mundy"}

PERSOS = ["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack", "Gerry"]
KITES = [915, 362]     # contre le banc du jardin, à droite (p. 45)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Michael has just told us how every one of them will end. And then the light comes back… "
        "on one more warm afternoon.",
        "{-q1}We watch it the way Michael remembers it: knowing that it is the last.",
        "{-tab_don}{serie}Part twelve: a radio that comes and goes, one more dance, a dead rooster, "
        "an exchange of hats… and the kites, at last.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="One more warm afternoon… the last."),
        "serie": dict(type="mot", t="The last afternoon", g="the radio · a dance · a rooster · two hats · the kites",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 12", t="The last afternoon",
                      sous="Act Two · pages 64 – 74"),
    }),

    # ------------------------------------------------------------------ I. le sycomore et le « système » de Jack
    dict(id="sycomore", chap="On the sycamore", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page sixty-four. Chris is out in the garden, calling up to Gerry, at the top of the sycamore. We only hear his voice.",
        ("C", "Are you still up there?", "jeu1.1", {"voix": "F"}),
        ("C", "We never made love on top of a sycamore tree.", "jeu1.2"),
        ("C", "If you fall and break your neck it'll be too good for you.", "jeu1.3", {"voix": "F"}),
        "{jeu1.4}She goes inside. Maggie has a brilliant idea: Agnes, with her clever hands, should be a dressmaker.",
        ("C", "It's the job for you, Aggie; I'm telling you.", "jeu1.5", {"voix": "F"}),
        "{jeu1.6}Maggie is out of cigarettes. Chris finds her a single one on the mantelpiece.",
        "{jeu1.7}Then Jack enters through the garden.",
        ("C", "Maybe I should go to Ryanga with you, Jack.", "jeu1.8", {"voix": "F"}),
        ("C", "I couldn't promise four men but I should be able to get one husband for all of you.", "jeu1.9"),
        ("C", "I'm completely in favour of it.", "jeu1.10"),
        "Kate has heard enough.",
        ("C", "I don't think it's what Pope Pius XI considers to be the holy sacrament of matrimony.", "jeu1.11", {"voix": "F"}),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Chris": [1010, 262], "Maggie": "buffet", "Kate": [290, 515], "Agnes": "tricot_a"},
                 act={"Chris": "debout", "Maggie": "range", "Kate": "debout", "Agnes": "assis"}, cam="tout",
                 objets={"kites": KITES}, note="GERRY is up the sycamore, (Off.): we only hear him. (p. 64)"),
            dict(dit=["Chris", "Are you still up there?"]),
            dict(note="GERRY (Off.): “We never made love on top of a sycamore tree.” (p. 65)"),
            dict(dit=["Chris", "If you fall and break your neck it'll be too good for you."], note="(She looks quickly around: did her sisters hear that?)"),
            dict(pos={"Chris": "table"}, note="Maggie: “what is it that Ballybeg badly needs…?” A dressmaker!"),
            dict(dit=["Maggie", "It's the job for you, Aggie; I'm telling you."]),
            dict(pos={"Chris": [225, 320]}, tient={"Maggie": "cigarette"},
                 note="(CHRIS goes to the mantelpiece and produces a single cigarette.)"),
            dict(pos={"Chris": "table"}, chemin={"Jack": ["allee", [880, 420], "seuil"]}, chemin_duree=6,
                 note="(JACK enters through the garden.)"),
            dict(dit=["Maggie", "Maybe I should go to Ryanga with you, Jack."]),
            dict(pos={"Jack": "seuil"}, dit=["Jack", "I couldn't promise four men but I should be able to get one husband for all of you."]),
            dict(dit=["Jack", "I'm completely in favour of it."]),
            dict(dit=["Kate", "I don't think it's what Pope Pius XI considers to be the holy sacrament of matrimony."]),
        ]),
    }),

    # ------------------------------------------------------------------ II. Anything Goes
    dict(id="danse", chap="Anything Goes", fond="nuit", humeur="lumiere", beats=[
        "{jeu2}Gerry has fixed the radio. Very softly, it plays a song the text names: Anything Goes. "
        "Outside the text: Cole Porter, 1934.",
        "{jeu2.1}Gerry runs on. And Jack remembers their deal.",
        ("C", "The plumed hat – the ceremonial hat – remember? We agreed to swap.", "jeu2.2"),
        "{jeu2.3}He goes to his bedroom. {jeu2.4}Gerry listens, sings a line of the song, and turns to Agnes.",
        ("C", "Dance with me, Agnes.", "jeu2.5"),
        ("C", "Have a bit of sense, Gerry Evans.", "jeu2.6", {"voix": "F"}),
        "{jeu2.7}But he pulls her to her feet and takes her in his arms. {jeu2.8}With style and with easy elegance, "
        "they dance once around the kitchen, and then out to the garden.",
        ("P", 3.0),
        ("C", "You should be a professional dancer.", "jeu2.9"),
        ("C", "Too late for that.", "jeu2.10", {"voix": "F"}),
        "{jeu2.11}He bends down and kisses her on the forehead. All this is seen, but not heard, by Chris at the kitchen window.",
        "{jeu2.12}Gerry bursts into song again, turns Agnes four or five times, and dances her back to the kitchen. "
        "Now, Chrissie, you and I, he says.",
        ("C", "Not now, I said. Are you thick?", "jeu2.13", {"voix": "F"}),
        "{jeu2.14}So Maggie kicks her Wellingtons off: I'll dance with you, Gerry! She and Gerry sing and dance.",
        ("P", 2.0),
        "{jeu2.15}And Chris suddenly turns the radio off.",
        ("C", "Sick of that damned thing.", "jeu2.16", {"voix": "F"}),
        "{jeu2.17}Gerry goes to Chris at the radio: not a bad little set, that. And Kate, of course, is delighted.",
        ("C", "Peace, thanks be to God! D'you know what that thing has done? Killed all Christian conversation in this country.",
         "jeu2.18", {"voix": "F"}),
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Chris": "table", "Maggie": "buffet", "Kate": [290, 515], "Agnes": "tricot_a", "Jack": "seuil"},
                 act={"Chris": "debout", "Maggie": "debout", "Kate": "debout", "Agnes": "assis"}, tient={"Maggie": "cigarette"},
                 radio=True, cam="tout", objets={"kites": KITES},
                 note="(Music of “Anything Goes” very softly on the radio.) (p. 66)"),
            dict(chemin={"Gerry": [[880, 330], "porte", [500, 340]]}, chemin_duree=3, note="(GERRY runs on.) “Well? Any good?”"),
            dict(dit=["Jack", "The plumed hat – the ceremonial hat – remember? We agreed to swap."], pos={"Gerry": [500, 340]}),
            dict(pos={"Jack": "arriere"}, duree=4, note="(He goes to his bedroom.) (p. 67)"),
            dict(pos={"Jack": "off", "Gerry": [470, 430]}, note="(Listens. Sings a line of the song.)"),
            dict(dit=["Gerry", "Dance with me, Agnes."]),
            dict(dit=["Agnes", "Have a bit of sense, Gerry Evans."]),
            dict(act={"Agnes": "debout"}, pos={"Agnes": [404, 440]},
                 note="(GERRY pulls her to her feet and takes her in his arms.)"),
            dict(act={"Agnes": "danse_douce", "Gerry": "danse_douce"},
                 chemin={"Gerry": [[470, 430], [300, 460], [250, 400], [400, 380], "porte", "jardin", [1030, 520]],
                         "Agnes": [[404, 440], [275, 480], [225, 420], [375, 400], [540, 320], [745, 450], [1070, 530]]},
                 chemin_duree=14, note="“With style and with easy elegance they dance once around the kitchen and then out to the garden”"),
            dict(pos={"Gerry": [1030, 520], "Agnes": [1070, 530]}, act={"Agnes": "debout", "Gerry": "debout"},
                 dit=["Gerry", "You should be a professional dancer."], note="(They are now in the far corner of the garden.) (p. 68)"),
            dict(dit=["Agnes", "Too late for that."]),
            dict(pos={"Chris": "fenetre"}, note="“He bends down and kisses her on the forehead.” Seen, not heard, by Chris at the window."),
            dict(act={"Agnes": "danse_douce", "Gerry": "danse_douce"},
                 chemin={"Gerry": [[1030, 520], [800, 470], "porte", [420, 410]], "Agnes": [[1070, 530], [830, 490], [560, 330], [370, 450]]},
                 chemin_duree=7, note="“turns AGNES four or five times very rapidly and dances her back to the kitchen”"),
            dict(pos={"Gerry": [420, 410], "Agnes": [370, 450]}, act={"Agnes": "halete", "Gerry": "debout"},
                 dit=["Chris", "Not now, I said. Are you thick?"]),
            dict(pos={"Maggie": [500, 460], "Gerry": [455, 440]}, act={"Maggie": "danse", "Gerry": "danse"}, tient={"Maggie": None},
                 note="(She kicks her Wellingtons off.) “Shirley Temple needs a lot of space.” (p. 69)"),
            dict(pos={"Chris": "radio"}, note="(CHRIS suddenly turns the radio off.)"),
            dict(radio=False, act={"Maggie": "debout", "Gerry": "debout"}, dit=["Chris", "Sick of that damned thing."]),
            dict(pos={"Gerry": [420, 290]}, note="(He goes to CHRIS at the radio.) “Not a bad little set, that.”"),
            dict(dit=["Kate", "Peace, thanks be to God! … Killed all Christian conversation in this country."]),
        ]),
    }),

    # ------------------------------------------------------------------ III. le coq mort
    dict(id="coq", chap="The fox", fond="nuit", humeur="tension", beats=[
        "{jeu3}Then Chris turns to Agnes. Icily.",
        ("C", "Vera McLaughlin's calling here tomorrow. She wants to talk to you and Rose.", "jeu3.1", {"voix": "F"}),
        ("C", "Something about wool. Didn't sound important.", "jeu3.2", {"voix": "F"}),
        "We know it is. And Maggie decides they will eat outside.",
        ("C", "Lughnasa's almost over, girls. There aren't going to be many warm evenings left.", "jeu3.3", {"voix": "F"}),
        "{jeu3.4}The weather, the festival, the family: all ending together. Maggie spreads a cloth in the middle of the garden. Inside, at the radio, Gerry kisses Chris lightly on the back of the neck.",
        "{jeu3.5}Then Rose enters the garden from the back of the house. In her right hand, she holds her rooster by the feet. Dead.",
        "{jeu3.6}Agnes sees her first and goes to her. Chris and Gerry join the others in the garden.",
        ("C", "My rooster's dead.", "jeu3.7", {"voix": "F"}),
        ("C", "The fox must have got him.", "jeu3.8", {"voix": "F"}),
        "{jeu3.9}She places it carefully on the tablecloth, in the middle of the garden.",
        ("C", "We'll get another white rooster for you, Rosie.", "jeu3.10", {"voix": "F"}),
        ("C", "I don't want another.", "jeu3.11", {"voix": "F"}),
        "{jeu3.12}Maggie gives her a quick hug. Rose sits on the garden seat. Then Maggie sees Jack, coming through the kitchen.",
        ("C", "Jesus, Mary, and Joseph!", "jeu3.13", {"voix": "F"}),
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Chris": "radio", "Gerry": [420, 290], "Maggie": [500, 460], "Kate": [290, 515], "Agnes": [370, 450]},
                 act={"Chris": "debout", "Gerry": "debout", "Maggie": "debout", "Kate": "debout", "Agnes": "debout"},
                 cam="tout", objets={"kites": KITES}, note="CHRIS. (To AGNES, icily.) (p. 69)"),
            dict(dit=["Chris", "Vera McLaughlin's calling here tomorrow. She wants to talk to you and Rose."]),
            dict(dit=["Chris", "Something about wool. Didn't sound important."]),
            dict(dit=["Maggie", "Lughnasa's almost over, girls. There aren't going to be many warm evenings left."]),
            dict(pos={"Maggie": [720, 545], "Kate": [660, 410], "Agnes": [700, 400]},
                 note="(MAGGIE exits with the cloth which she spreads in the middle of the garden.)"),
            dict(chemin={"Rose": [[620, 215], [700, 300], [800, 395]]}, chemin_duree=6, tient={"Rose": "coq"},
                 note="“In her right hand she holds the dead rooster by the feet.” (p. 71)"),
            dict(pos={"Rose": [800, 395], "Agnes": [750, 400], "Chris": [1075, 505], "Gerry": [960, 500]},
                 note="“Its feathers are ruffled and it is stained with blood. ROSE is calm, almost matter-of-fact.”"),
            dict(dit=["Rose", "My rooster's dead."]),
            dict(dit=["Rose", "The fox must have got him."]),
            dict(tient={"Rose": None}, objets={"coq": [800, 455]},
                 note="(She places it carefully on the tablecloth in the middle of the garden.)"),
            dict(dit=["Agnes", "We'll get another white rooster for you, Rosie."]),
            dict(dit=["Rose", "I don't want another."]),
            dict(pos={"Rose": "banc_g"}, act={"Rose": "assis"}, note="MAGGIE. (Quick hug.) … (ROSE sits on the garden seat.)"),
            dict(dit=["Maggie", "Jesus, Mary, and Joseph!"], note="(She sees JACK coming through the kitchen.)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. l'échange des chapeaux, les cerfs-volants
    dict(id="echange", chap="The exchange", fond="nuit", humeur="mystere", beats=[
        "{jeu4}Page seventy-two. Jack wears a very soiled, very crumpled white uniform, far too large: his hands are lost in the sleeves. "
        "On his head, a tricorn ceremonial hat, the plumage broken and tatty.",
        ("C", "Gerry, my friend, where are you?", "jeu4.1"),
        "{jeu4.2}It was his uniform as chaplain to the British army, in the Great War.",
        "{jeu4.3}Now the formal exchange, as in Ryanga. Each man holds his possession: Jack his tricorn, Gerry his straw hat. "
        "{jeu4.4}Each places it on the ground, at his feet.",
        "{jeu4.5}Three steps away from it: a symbolic distancing from what you once possessed. "
        "{jeu4.6}Turn round once, a complete circle: the formal rejection of what you once had.",
        "{jeu4.7}Then each man crosses over to the position the other has left.",
        ("C", "Excellent. The exchange is now formally and irrevocably complete.", "jeu4.8"),
        "{jeu4.9}Gerry gets the tricorn, Jack the straw hat. "
        "{jeu4.10}And Gerry does a Charlie Chaplin walk across the garden.",
        ("C", "Would you look at them! Strutting about like a pair of peacocks!", "jeu4.11", {"voix": "F"}),
        ("C", "I love September.", "jeu4.12", {"voix": "F"}),
        "{jeu4.13}Agnes moves beside Rose. Next Sunday, she promises, they will get some bilberries.",
        ("C", "Whatever you say, Aggie.", "jeu4.14", {"voix": "F"}),
        "{jeu4.15}Then Gerry examines the kites.",
        ("C", "Not bad for a kid of seven. Very neatly made.", "jeu4.16"),
        ("C", "I hate them.", "jeu4.17", {"voix": "F"}),
        ("C", "I think they're just wonderful. Look, Jack.", "jeu4.18"),
        "{jeu4.19}And for the first time, we all see the images. On each kite, a crude, cruel, grinning face.",
        ("P", 2.0),
        "And Maggie has one last riddle: why is a gramophone like a parrot?",
        ("C", "Because it … because it always … because a parrot … God I've forgotten!", "jeu4.20", {"voix": "F"}),
    ], vis={
        "jeu4": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Jack": "porte", "Rose": "banc_g", "Maggie": [720, 545], "Kate": [660, 410], "Agnes": [750, 400],
                      "Chris": [1075, 505], "Gerry": [960, 500]},
                 act={"Rose": "assis", "Jack": "debout"}, costume={"Jack": "blanc"}, chapeau={"Jack": "tricorne"},
                 cam="tout", objets={"kites": KITES, "coq": [800, 455]},
                 note="“a very soiled, very crumpled white uniform” · a tricorn, “the plumage broken and tatty” (p. 72)"),
            dict(dit=["Jack", "Gerry, my friend, where are you?"]),
            dict(pos={"Jack": [600, 500]}, note="“It was my uniform when I was chaplain to the British army during the Great War.”"),
            dict(pos={"Jack": [610, 495], "Gerry": [860, 490]},
                 chapeau={"Jack": "aucun", "Gerry": "aucun"}, tient={"Jack": "tricorne", "Gerry": "paille"},
                 note="(He and GERRY enact this ritual.)"),
            dict(act={"Jack": "voute", "Gerry": "voute"}, tient={"Jack": None, "Gerry": None},
                 note="“I place my possession on the ground” · “Put it on the grass – anywhere – just at your feet.”"),
            dict(pos={"Jack": [555, 515], "Gerry": [915, 505]}, act={"Jack": "debout", "Gerry": "debout"}, duree=2.5,
                 note="“take three steps” away: “a symbolic distancing of yourself from what you once possessed”"),
            dict(note="“turn round once … a complete circle … the formal rejection of what you once had”"),
            dict(pos={"Jack": [860, 490], "Gerry": [610, 495]}, duree=3.0,
                 note="“Now I cross over to where you stand … And you come over to the position I have left.”"),
            dict(chapeau={"Jack": "paille", "Gerry": "tricorne"},
                 dit=["Jack", "Excellent. The exchange is now formally and irrevocably complete."]),
            dict(note="“This is my straw hat. And that is your tricorn hat. Put it on.” · Agnes: “You're lovely.”"),
            dict(chemin={"Gerry": [[610, 495], [700, 470], [900, 470], [960, 500]]}, chemin_duree=6,
                 note="(GERRY does a Charlie Chaplin walk across the garden, his feet spread, his cane twirling.)"),
            dict(pos={"Gerry": [960, 500]}, dit=["Maggie", "Would you look at them! Strutting about like a pair of peacocks!"],
                 note="(p. 73)"),
            dict(dit=["Kate", "I love September."]),
            dict(pos={"Agnes": [745, 372]}, note="(AGNES moves beside ROSE.) “Next Sunday, then.” · “We'll get some bilberries.”"),
            dict(dit=["Rose", "Whatever you say, Aggie."]),
            dict(pos={"Gerry": [965, 395]}, note="(GERRY examines the kites.)"),
            dict(dit=["Gerry", "Not bad for a kid of seven. Very neatly made."]),
            dict(dit=["Maggie", "I hate them."]),
            dict(dit=["Gerry", "I think they're just wonderful. Look, Jack."]),
            dict(objets={"kites": None, "kites_faces": KITES}, cam="jardin",
                 note="“For the first time we all see the images. On each kite is painted a crude, cruel, grinning face”"),
            dict(dit=["Maggie", "Because it … because it always … because a parrot … God I've forgotten!"], cam="tout"),
        ]),
    }),

    # ------------------------------------------------------------------ V. cinq répliques à connaître
    dict(id="repliques", chap="Key lines to know", fond="aube", humeur="calme",
         retenir="Pius XI against Ryanga, the dead rooster, the exchange of hats, the grinning kites.", beats=[
        "{cinq}Four lines carry the meaning of this long, light afternoon.",
        "{-cinq}First, Kate against Jack.",
        ("C", "It may be efficient and you may be in favour of it, Jack, but I don't think it's what Pope Pius XI "
              "considers to be the holy sacrament of matrimony.", "c_pius", {"voix": "F"}),
        "{-c_pius}{pius}The Pope against Ryanga, the sacrament against the Great Goddess. And the dramatic irony: Michael told us "
        "that Kate will lose her job more because of Jack than because of falling numbers.",
        "{-pius}Then, the rooster.",
        ("C", "Its feathers are ruffled and it is stained with blood. ROSE is calm, almost matter-of-fact.", "c_coq"),
        "{-c_coq}{echo}Think back to part seven: in Ryanga, says Jack, you kill a rooster to please the spirits. "
        "Here a white bird lies bleeding in the middle of the feast, on the evening of Rose's afternoon with Danny Bradley. "
        "A sacrifice, or innocence lost? Friel does not explain it.",
        "{-echo}Then, Jack.",
        ("C", "Excellent. The exchange is now formally and irrevocably complete.", "c_exchange"),
        "{-c_exchange}{chapeaux}A Ryanga swap ritual, on the eve of Gerry's departure for Spain: Jack gives away the British governor's ceremonial hat, the district commissioner's present. "
        "And in part eleven, Gerry danced down the lane with that tricorn over his left eye.",
        "{-chapeaux}And last, the kites.",
        ("C", "For the first time we all see the images. On each kite is painted a crude, cruel, grinning face, "
              "primitively drawn, garishly painted.", "c_kites"),
        "{-c_kites}{masque}The kites were built all through the play. Now they turn their faces to us, like pagan masks. "
        "And the last word goes to Maggie's riddle. The joke never arrives.",
    ], vis={
        "cinq": dict(type="mot", t="Four lines to know", g="the last afternoon · pages 66 – 73", y=250, taille=80),
        "c_pius": dict(type="cit", a="Kate", o="p. 66", x=170, y=190, w=940),
        "pius": dict(type="cols", g="Kate", gq="Pope Pius XI, “the holy sacrament of matrimony”", d="Jack",
                     dq="“That's our system… I'm completely in favour of it.”", vs="≠", repere="Rome / Ryanga"),
        "c_coq": dict(type="cit", a="Stage direction", o="p. 71", x=170, y=200, w=940),
        "echo": dict(type="cols", g="Ryanga", gq="a rooster killed “to please the spirits”", d="Ballybeg",
                     dq="a white rooster, bleeding, on the feast cloth", vs="↔", repere="sacrifice? innocence lost?"),
        "c_exchange": dict(type="cit", a="Jack", o="p. 72", x=170, y=210, w=940),
        "chapeaux": dict(type="note", cles=["ritual", "tricorn"], terme="Two hats · pages 64 and 72",
                         t="A Ryanga ritual: Jack gives away the last British governor's ceremonial hat (p. 42).",
                         etape="p. 64: Gerry leaves for Spain wearing Jack's tricorn.", x=170, y=200, w=940),
        "c_kites": dict(type="cit", a="Stage direction", o="p. 73", x=170, y=190, w=940),
        "masque": dict(type="note", cles=["masks", "forgotten"], terme="The end of the afternoon · pp. 73 – 74",
                       t="Grinning faces, like pagan masks, turned to the audience.",
                       etape="Maggie's riddle: “God I've forgotten!”", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VI. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Tragic irony, ritual, symbols of the end, a dance cut short: the last afternoon, seen from the end.", beats=[
        "{a1}Now the analysis. Four ideas. "
        "{a1.1}One: tragic irony. A dressmaking plan, bilberries next Sunday, I love September. "
        "Because Michael has just told us the ending, every hopeful line hurts. The scene is an elegy disguised as a picnic.",
        "{-a1}{a2}{a2.1}Two: ritual replaces sacrament. Kate defends the holy sacrament of matrimony; "
        "Jack answers with a Ryanga ceremony, formal and irrevocable. He gives away the colonial governor's ceremonial hat, "
        "the district commissioner's present. Pagan ritual, here, is what gives meaning to a farewell.",
        "{-a2}{a3}{a3.1}Three: symbols of the end. The dead white rooster on the feast cloth, the broken radio, "
        "the kites' cruel, grinning faces. None of them is explained. They are images a child stored, "
        "and an adult still cannot put into words.",
        "{-a3}{a4}{a4.1}Four: the dance, and its limits. Gerry and Agnes dance with easy elegance; "
        "Chris watches, then switches the music off. Dance still frees the sisters, "
        "but it also divides them. Even Maggie's joke stops halfway.",
        "{-a4}{carte}Here is the last afternoon for your essay. {carte.1}Tragic irony. {carte.2}Ritual against sacrament. "
        "{carte.3}Symbols. {carte.4}And the dance, cut short.",
    ], vis={
        "a1": dict(type="note", cles=["irony", "elegy"], terme="1 · Tragic irony",
                   t="Dressmaking, bilberries, “I love September”: hopes we know are doomed.",
                   etape="An elegy disguised as a picnic.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["ritual", "sacrament"], terme="2 · Ritual replaces sacrament",
                   t="“the holy sacrament of matrimony” against “formally and irrevocably complete”.",
                   etape="Jack gives away the governor's tricorn: an empire's symbol, bartered away.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["rooster", "kites"], terme="3 · Symbols of the end",
                   t="The dead white rooster, the broken radio, the “cruel, grinning” kites.",
                   etape="Images a child stored, never explained.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["elegance", "divides"], terme="4 · A dance cut short",
                   t="Gerry and Agnes dance; Chris switches the radio off.",
                   etape="Dance frees the sisters, but also divides them.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE LAST AFTERNOON", branches=[
            dict(t="Tragic irony", items=["the dressmaker plan", "“I love September”", "“Next Sunday”"]),
            dict(t="Ritual", items=["Pius XI / “the Great Goddess”", "the hat exchange", "“irrevocably complete”"]),
            dict(t="Symbols", items=["the dead white rooster", "the broken radio", "the grinning kites"]),
            dict(t="Dance", items=["“Anything Goes”", "Chris at the window", "the forgotten riddle"])]),
    }),
]

QUIZ = [
    dict(q="What does Kate oppose to Jack's Ryanga “system” of one husband for several wives?",
         r=["What Pope Pius XI considers the holy sacrament of matrimony", "The laws of the Irish Free State",
            "Maggie's dressmaking plan", "The rules of the knitting factory"], ok=0, voir="c_pius",
         ex="“I don't think it's what Pope Pius XI considers to be the holy sacrament of matrimony”: Rome against Ryanga."),
    dict(q="Which song plays on the radio when Gerry dances with Agnes?",
         r=["“Anything Goes”", "“Abyssinia”", "“The Isle of Capri”", "No song is named"], ok=0, voir="jeu2",
         ex="The stage direction on p. 66: Music of “Anything Goes” very softly on the radio."),
    dict(q="What has Chris just seen before she turns the radio off?",
         r=["Gerry kissing Agnes in the garden", "Kate taking the battery out",
            "Jack dancing with Rose", "Michael breaking a kite"], ok=0, voir="jeu2.11",
         ex="She saw the kiss from the window. The text gives no reason for switching off; her only stated reason is “wasting the battery”."),
    dict(q="How does Rose behave when she brings in her dead rooster?",
         r=["She is calm, almost matter-of-fact", "She screams and runs away", "She blames Gerry", "She hides it from Kate"],
         ok=0, voir="c_coq",
         ex="“ROSE is calm, almost matter-of-fact.” She lays the bird on the tablecloth and refuses another white rooster."),
    dict(q="In Jack's exchange ritual, what does turning round once in a complete circle mean?",
         r=["The formal rejection of what you once had", "A blessing from the spirits", "A promise to come back",
            "The start of a dance"], ok=0, voir="jeu4.6",
         ex="Three steps away: “a symbolic distancing”; a complete circle: “the formal rejection”; then each takes the other's place."),
    dict(q="What do we see on the kites “for the first time”?",
         r=["A crude, cruel, grinning face on each one", "The names of the five sisters", "A cross and a sun",
            "Michael's initials"], ok=0, voir="c_kites",
         ex="“On each kite is painted a crude, cruel, grinning face, primitively drawn, garishly painted”: like pagan masks."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
