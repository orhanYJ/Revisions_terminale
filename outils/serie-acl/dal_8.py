"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 8 : « Three weeks later », l'ouverture de l'acte II (PDF de travail, p. 45-52).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu), en suivant les didascalies pas à pas ; les répliques courtes s'affichent en
bulles et sont lues par la voix des sœurs (F) ou la voix d'homme (Michael, Jack). L'enfant n'est jamais vu : Michael, au bord
du plateau (« MICHAEL stands downstage left », p. 45), dit ses répliques ; l'enfant n'est qu'un emplacement en pointillé à la
table où il écrit (« She dances … across to the table and tousles the BOY's hair », p. 46). Ce que Jack raconte (Okawa, le
gong, la fête de l'igname) n'est pas joué : notes « told, not shown ». Puis quatre répliques à connaître et l'analyse.

Début : p. 45, « ACT TWO » (début septembre, trois semaines plus tard ; Maggie, l'enfant, les cerfs-volants, la lettre au
père Noël et la bicyclette promise par Gerry). Jack, plus fort et alerte, la noce d'Austin Morgan, les myrtilles de
Lughnasa, Okawa, le gong, la fête de la nouvelle igname et les sacrifices à Obi ; Kate et la messe ; Kate et Maggie à voix
basse (« He's not our Jack at all »). Fin : p. 52, juste avant la didascalie « (CHRIS and GERRY enter L. … ) ».
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_8. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'air de Haendel, l'Irlande catholique des années 1930) est dit comme tel.
Coquilles du PDF évitées dans les citations : « Casva », « we pas », « bee asking », « latter of lepers », « We've agree ».
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-8"
NOTION = "Dancing at Lughnasa"
NUM = 8
TITRE = "Three weeks later"
SUIVANT = "Part 9 · Gerry comes back"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Ryangans": "Ree-angans",
                 "Okawa": "Oh-kah-wa", "Obi": "Oh-bee", "Carrickfad": "Carrick-fad", "Mundy": "Mundy"}

PULL = "#d0532f"   # « a garish-coloured – probably a sister's – sweater » (p. 48)

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Act Two. Early September: three weeks later. Remember Michael's warning at the end of Act One: "
        "one morning in early September, Rose and Agnes would be gone for ever.",
        "{-q1}{serie}So we are there. And on stage, all looks calm: a song, a letter, a priest getting better.",
        ("P", 0.3),
        "{-serie}{-tab_don}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Early September: the month Michael warned us about."),
        "serie": dict(type="mot", t="The opening of Act Two", g="Maggie and the boy · a new Jack · the harvest in Ryanga",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 8", t="Three weeks later",
                      sous="The opening of Act Two · pages 45 – 52"),
    }),

    # ------------------------------------------------------------------ I. Maggie et l'enfant (pp. 45-48)
    dict(id="maggie", chap="A bell for a bicycle", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page forty-five. Ink and paper on the kitchen table. Two finished kites lean against the garden seat, "
        "their artwork still unseen. Michael stands at the edge of the stage, listening.",
        "{jeu1.1}Maggie enters with two zinc buckets of water, singing in her usual parodic style.",
        ("C", "Oh play to me, Gypsy; the moon's high above.", "jeu1.2", {"voix": "F"}),
        "{jeu1.3}She fills the kettle and the saucepan on the range. The boy is at the table, writing. "
        "As in Act One, we never see him: adult Michael speaks his lines. Maggie claims a debt.",
        ("C", "Three weeks ago I bet you a penny those aul kites would never get off the ground.", "jeu1.4", {"voix": "F"}),
        ("C", "Because there was never enough wind; that's why.", "jeu1.5"),
        "{jeu1.6}She dances her exaggerated dance across to the table and tousles his hair. "
        "He is writing to Santa Claus, in September. Asking for what?",
        ("C", "A bell.", "jeu1.7"),
        ("C", "For my bicycle.", "jeu1.8"),
        ("C", "He told me today. He bought it in Kilkenny. So there!", "jeu1.9"),
        "{jeu1.10}Page forty-seven. Her manner changes. She returns to the table.",
        ("C", "Your daddy told you that?", "jeu1.11", {"voix": "F"}),
        ("C", "It's coming next week. It's a black bike – a man's bike.", "jeu1.12"),
        "{jeu1.13}Remember part six: Gerry told Chris the bike only came in blue. "
        "Very brisk, Maggie changes the subject: who will teach you to ride?",
        ("C", "Maybe not by myself. But put me on the bar, cub – magnificent!", "jeu1.14", {"voix": "F"}),
        ("C", "You never sat on the bar of a bike in your life, Aunt Maggie!", "jeu1.15"),
        ("C", "Oh yes, I did, Michael. Oh yes, indeed I did.", "jeu1.16", {"voix": "F"}),
        "{jeu1.17}A tiny line, repeated: behind the joke, a memory of her own youth, perhaps the boy she loved at Ardstraw. "
        "She does not explain. It is subtext. She gathers up the papers, {jeu1.18}and tries a new riddle on him: two apples on a tree. He gives up.",
    ], vis={
        "jeu1": dict(type="jeu", persos=["Maggie", "Michael"], etats=[
            dict(pos={"Michael": "michael", "Maggie": "off"}, act={"Michael": "debout"}, cam="tout",
                 objets={"kites": "banc", "garcon": [275, 410]},
                 note="ACT TWO. “Early September; three weeks later.” (p. 45)"),
            dict(chemin={"Maggie": ["allee", "jardin", "seuil", "porte", "buffet"]}, chemin_duree=10,
                 note="She enters “carrying two zinc buckets of water”, singing “in her usual parodic style”"),
            dict(dit=["Maggie", "‘Oh play to me, Gypsy; The moon's high above.’"]),
            dict(pos={"Maggie": "buffet"}, act={"Maggie": "range"},
                 note="She fills the kettle and the saucepan on the range. (p. 46)"),
            dict(act={"Maggie": "debout"},
                 dit=["Maggie", "Three weeks ago I bet you a penny those aul kites would never get off the ground."]),
            dict(dit=["Michael", "Because there was never enough wind; that's why."]),
            dict(pos={"Maggie": [375, 410]}, act={"Maggie": "danse"},
                 note="She dances her exaggerated dance across to the table and tousles the BOY's hair."),
            dict(act={"Maggie": "debout"}, dit=["Michael", "A bell."], note="“It's to Santa Claus.” (p. 46)"),
            dict(dit=["Michael", "For my bicycle."]),
            dict(dit=["Michael", "He told me today. He bought it in Kilkenny. So there!"]),
            dict(note="(Her manner changes. She returns to the table.) p. 47"),
            dict(dit=["Maggie", "Your daddy told you that?"], note="(Softly.)"),
            dict(dit=["Michael", "It's coming next week. It's a black bike – a man's bike."]),
            dict(note="“Well, if he promised you …” (Very brisk.)"),
            dict(dit=["Maggie", "Maybe not by myself. But put me on the bar, cub – magnificent!"]),
            dict(dit=["Michael", "You never sat on the bar of a bike in your life, Aunt Maggie!"]),
            dict(dit=["Maggie", "Oh yes, I did, Michael. Oh yes, indeed I did."]),
            dict(act={"Maggie": "range"}, note="(She gathers up the papers.)"),
            dict(act={"Maggie": "debout"}, note="“A man goes to an apple tree with two apples on it.” (p. 47)"),
        ]),
    }),

    # ------------------------------------------------------------------ II. un nouveau Jack (pp. 48-49)
    dict(id="jack", chap="A new Jack", fond="nuit", humeur="lumiere", beats=[
        "{jeu2}Page forty-eight. Jack enters. He looks much stronger, very sprightly and alert.",
        "{jeu2.1}No top coat, no hat: a garish-coloured sweater, probably a sister's.",
        ("C", "Did I hear the church bell ringing?", "jeu2.2"),
        "A big posh wedding, says Maggie. Not one of my sisters? asks Jack.",
        ("C", "No such luck. A man called Austin Morgan and a girl from Carrickfad.", "jeu2.3", {"voix": "F"}),
        "{jeu2.4}Remember Kate's blush about Austin Morgan, in part three. Michael leaves the stage. "
        "And Jack is off for his walk, number four, so that Kate won't have to nag at him. Nag? He tests the word.",
        ("C", "So my English vocabulary is coming back, too.", "jeu2.5"),
        "{jeu2.6}Kate enters, with an armful of clothes from the clothes line.",
        ("C", "No sign of Rose and Agnes yet?", "jeu2.7", {"voix": "F"}),
        ("C", "They said they'd be back for tea.", "jeu2.8", {"voix": "F"}),
        "{jeu2.9}They are picking bilberries. A quiet line; but after Michael's warning, it sends a shiver. And Jack remembers.",
        ("C", "Mother and myself; every Lughnasa; the annual ritual.", "jeu2.10"),
        ("C", "O ruddier than the cherry, O sweeter than the berry.", "jeu2.11"),
        ("C", "You see, Kate, it's all coming back to me.", "jeu2.12"),
        ("C", "So you'll soon begin saying Mass again?", "jeu2.13", {"voix": "F"}),
        "Yes, indeed, says Jack. Here in the house? asks Maggie.",
        ("C", "Why not? Perhaps I'll start next Monday.", "jeu2.14"),
    ], vis={
        "jeu2": dict(type="jeu", persos=["Maggie", "Michael", "Jack", "Kate"], etats=[
            dict(pos={"Michael": "michael", "Maggie": [375, 410], "Jack": "off", "Kate": "off"}, cam="tout",
                 objets={"kites": "banc", "garcon": [275, 410]}, chapeau={"Jack": "aucun"}, costume={"Jack": PULL},
                 note="“He looks much stronger and is very sprightly and alert.” (p. 48)"),
            dict(chemin={"Jack": ["seuil", "porte", [465, 410]]}, chemin_duree=5,
                 note="No top coat, no hat: “a garish-coloured – probably a sister's – sweater”"),
            dict(dit=["Jack", "Did I hear the church bell ringing?"]),
            dict(dit=["Maggie", "No such luck. A man called Austin Morgan and a girl from Carrickfad."]),
            dict(pos={"Michael": "off"}, objets={"garcon": None}, cam="cuisine", note="(MICHAEL exits.) p. 48"),
            dict(dit=["Jack", "So my English vocabulary is coming back, too."]),
            dict(chemin={"Kate": ["seuil", "porte", [545, 410]]}, chemin_duree=4,
                 note="KATE enters with an armful of clothes from the clothes line."),
            dict(pos={"Kate": [545, 410]}, dit=["Kate", "No sign of Rose and Agnes yet?"], note="(p. 49)"),
            dict(dit=["Maggie", "They said they'd be back for tea."]),
            dict(note="“They're away picking bilberries.”"),
            dict(dit=["Jack", "Mother and myself; every Lughnasa; the annual ritual."]),
            dict(dit=["Jack", "‘O ruddier than the cherry, O sweeter than the berry …’"],
                 note="Outside the text: an aria from Handel's Acis and Galatea"),
            dict(dit=["Jack", "You see, Kate, it's all coming back to me."], note="(Laughs.)"),
            dict(dit=["Kate", "So you'll soon begin saying Mass again?"]),
            dict(dit=["Jack", "Why not? Perhaps I'll start next Monday."]),
        ]),
    }),

    # ------------------------------------------------------------------ III. la fête de l'igname (pp. 49-51)
    dict(id="ryanga", chap="The Festival of the New Yam", fond="nuit", humeur="mystere", beats=[
        "{jeu3}How will the neighbours know? Jack thinks of Okawa. Your house boy? asks Maggie.",
        ("C", "My friend – my mentor – my counselor – and yes, my house boy as well.", "jeu3.1"),
        "{jeu3.2}Page fifty. Okawa summons the people with a huge iron gong, says Jack. We hear this; we never see it.",
        ("C", "And they all meet in your church?", "jeu3.3", {"voix": "F"}),
        ("C", "When I had a church.", "jeu3.4"),
        ("C", "All gathered together for Mass?", "jeu3.5", {"voix": "F"}),
        ("C", "Maybe. Or maybe to offer sacrifice to Obi, our Great Goddess of the Earth, so that the crops will flourish.",
         "jeu3.6"),
        "{jeu3.7}At the Ugandan harvest time, two ceremonies: the Festival of the New Yam, and the Festival of the Sweet Cassava.",
        ("C", "But these aren't Christian ceremonies, Jack, are they?", "jeu3.8", {"voix": "F"}),
        ("C", "Oh, no.", "jeu3.9"),
        "And he describes them. {jeu3.10}A sacrifice by the river. {jeu3.11}The first yams anointed and passed round. "
        "{jeu3.12}A chant, which becomes the rhythm of the dance. "
        "{jeu3.13}Then fires, painted faces, palm wine, and lepers dancing for days on end.",
        ("C", "there is no distinction between the religious and the secular in their culture.", "jeu3.14"),
        "{jeu3.15}Page fifty-one. He moves off, then stops: it's not Gilbert and Sullivan, is it? "
        "{jeu3.16}Again he moves off. Kate calls him back: Mass? Next Monday, he says.",
        ("C", "At first light. The moment Rose's white cock crows.", "jeu3.17"),
        ("C", "A harvest ceremony. You'll have to find a big gong somewhere, Kate.", "jeu3.18"),
        "{jeu3.19}And he leaves.",
    ], vis={
        "jeu3": dict(type="jeu", persos=["Maggie", "Jack", "Kate"], etats=[
            dict(pos={"Maggie": [375, 410], "Jack": [465, 410], "Kate": [545, 410]},
                 chapeau={"Jack": "aucun"}, costume={"Jack": PULL}, objets={"kites": "banc"}, cam="cuisine",
                 note="“What Okawa does – you know Okawa, don't you?” (p. 49)"),
            dict(dit=["Jack", "My friend – my mentor – my counselor – and yes, my house boy as well"]),
            dict(note="He tells us: Okawa's huge iron gong carries “four times as far” as the bell (told, not shown)"),
            dict(dit=["Maggie", "And they all meet in your church?"]),
            dict(dit=["Jack", "When I had a church."]),
            dict(dit=["Kate", "All gathered together for Mass?"]),
            dict(dit=["Jack", "Or maybe to offer sacrifice to Obi, our Great Goddess of the Earth …"]),
            dict(note="Harvest time: the Festival of the New Yam and the Festival of the Sweet Cassava"),
            dict(dit=["Kate", "But these aren't Christian ceremonies, Jack, are they?"]),
            dict(dit=["Jack", "Oh, no."]),
            dict(note="1 · “the ritual sacrifice of a fowl or a goat or a calf” (told, not shown)"),
            dict(note="2 · the first yams anointed and passed round “in huge wooden bowls”"),
            dict(note="3 · a chant: “a rhythm or percussion for the ritual dance”"),
            dict(note="4 · fires, painted faces, palm wine… dancing “for days on end” (p. 51)"),
            dict(dit=["Jack", "there is no distinction between the religious and the secular in their culture."]),
            dict(pos={"Jack": [495, 330]}, note="(He moves off – then stops.) “It's not Gilbert and Sullivan, is it?”"),
            dict(pos={"Jack": [585, 295]}, note="(Again, he moves off.) KATE: “Jack.”"),
            dict(dit=["Jack", "At first light. The moment Rose's white cock crows."]),
            dict(dit=["Jack", "A harvest ceremony. You'll have to find a big gong somewhere, Kate."]),
            dict(pos={"Jack": "off"}, note="(He leaves.) p. 51"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. pas notre Jack (pp. 51-52)
    dict(id="peur", chap="Not our Jack", fond="nuit", humeur="tension", beats=[
        "{jeu4}Pause. Kate and Maggie stare at each other, in concern, in alarm. They speak in hushed voices.",
        ("C", "I told you – you wouldn't believe me – I told you.", "jeu4.1", {"voix": "F"}),
        "{jeu4.2}Page fifty-two. Yesterday, a medicine man who brought a woman back from death, says Kate. "
        "This morning, the spirits of the tribe.",
        ("C", "He needs more time.", "jeu4.3", {"voix": "F"}),
        ("C", "Completely changed. He's not our Jack at all. And it's what he's changed into that frightens me.", "jeu4.4",
         {"voix": "F"}),
        ("C", "Doesn't frighten me.", "jeu4.5", {"voix": "F"}),
        "{jeu4.6}Now watch the stage directions. Maggie drifts back to the range. Kate wipes the table with excessive vigour. "
        "{jeu4.7}Then she slumps into a seat, and covers her face with her hands. "
        "{jeu4.8}Maggie stands behind her and holds her shoulders. Kate grasps her hands. The body says what Kate cannot.",
        "{jeu4.9}Maggie tries a joke: lepers trying to do the Military Two-step.",
        ("C", "God forgive you, Maggie Mundy!", "jeu4.10", {"voix": "F"}),
        "{jeu4.11}Chris's laughter is heard, off. Kate jumps to her feet.",
        ("C", "This must be kept in the family, Maggie! Not a word of this must go outside these walls – d'you hear? – "
              "not a syllable!", "jeu4.12", {"voix": "F"}),
        "Who is laughing with Chris, we will see in part nine.",
    ], vis={
        "jeu4": dict(type="jeu", persos=["Maggie", "Kate"], etats=[
            dict(pos={"Maggie": [375, 410], "Kate": [545, 410]}, act={"Maggie": "fige", "Kate": "fige"}, cam="cuisine",
                 objets={"kites": "banc"}, note="They stare at each other “in concern, in alarm”. Hushed voices. (p. 51)"),
            dict(dit=["Kate", "I told you – you wouldn't believe me – I told you."], act={"Maggie": "debout", "Kate": "debout"}),
            dict(note="“And this morning it was ‘the spirits of the tribe!’” (p. 52)"),
            dict(dit=["Maggie", "He needs more time."]),
            dict(dit=["Kate", "He's not our Jack at all. And it's what he's changed into that frightens me."]),
            dict(dit=["Maggie", "Doesn't frighten me."]),
            dict(pos={"Maggie": "buffet", "Kate": [330, 402]}, act={"Kate": "repasse"},
                 note="KATE wipes the table with a damp cloth, “with excessive vigour”"),
            dict(pos={"Kate": [300, 412]}, act={"Kate": "assis"},
                 note="She “slumps into a seat and covers her face with her hands”"),
            dict(pos={"Maggie": [335, 380]}, note="MAGGIE holds her shoulders. KATE grasps MAGGIE's hands in hers."),
            dict(note="“… lepers trying to do the Military Two-step.”"),
            dict(dit=["Kate", "God forgive you, Maggie Mundy!"]),
            dict(pos={"Kate": [225, 432]}, act={"Kate": "debout"},
                 note="CHRIS's laughter is heard off. KATE jumps to her feet."),
            dict(dit=["Kate", "… not a syllable!"]),
        ]),
    }),

    # ------------------------------------------------------------------ V. quatre répliques à connaître
    dict(id="repliques", chap="Four lines to know", fond="aube", humeur="calme",
         retenir="Jack “sprightly and alert”; “our Great Goddess”; religious = secular; “not our Jack at all”.", beats=[
        "{quatre}Four lines from these pages are worth knowing by heart. First, the new Jack.",
        "{-quatre}",
        ("C", "He looks much stronger and is very sprightly and alert.", "c_alert"),
        "{-c_alert}{alert}His body is getting better: no more top coat and hat. "
        "We are about to discover what his mind has become.",
        "{-alert}",
        ("C", "Or maybe to offer sacrifice to Obi, our Great Goddess of the Earth, so that the crops will flourish.", "c_obi"),
        "{-c_obi}{notre}Listen to that our. Our Great Goddess. The missionary now speaks from inside the tribe.",
        "{-notre}",
        ("C", "there is no distinction between the religious and the secular in their culture.", "c_secular"),
        "{-c_secular}{deux}That is the key line. {deux.g}In Ryanga, worship flows into celebration, almost imperceptibly. "
        "{deux.d}In Kate's Ballybeg, the Church and the dance hall are kept strictly apart.",
        "{-deux}And Kate's answer.",
        ("C", "He's not our Jack at all. And it's what he's changed into that frightens me.", "c_frightens", {"voix": "F"}),
        "{-c_frightens}{corps}One line, and then the body: the table wiped with excessive vigour, the slump, the face in her hands.",
    ], vis={
        "quatre": dict(type="mot", t="Four lines to know", g="pages 48 – 52", y=260, taille=84),
        "c_alert": dict(type="cit", a="Stage direction", o="p. 48", x=170, y=200, w=940),
        "alert": dict(type="note", cles=["stronger", "mind"], terme="Jack · p. 48",
                      t="No top coat, no hat: a garish sweater, “probably a sister's”.",
                      etape="The body recovers; the mind has changed.", x=170, y=200, w=940),
        "c_obi": dict(type="cit", a="Jack", o="p. 50", x=170, y=190, w=940),
        "notre": dict(type="note", cles=["our", "inside"], terme="Jack · p. 50",
                      t="“our Great Goddess of the Earth”: the possessive says where Jack now belongs.",
                      etape="The missionary speaks from inside the tribe.", x=170, y=200, w=940),
        "c_secular": dict(type="cit", a="Jack", o="p. 51", x=170, y=200, w=940),
        "deux": dict(type="cols", g="Ryanga", gq="worship grows into celebration", d="Ballybeg",
                     dq="the Church apart from the dance", vs="≠", repere="religious / secular"),
        "c_frightens": dict(type="cit", a="Kate", o="p. 52", x=170, y=200, w=940),
        "corps": dict(type="note", cles=["vigour", "body"], terme="Kate · p. 52",
                      t="She wipes the table “with excessive vigour”, “slumps into a seat and covers her face”.",
                      etape="The body says what Kate cannot.", x=170, y=200, w=940),
    }),
    # ------------------------------------------------------------------ VI. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Tragic knowledge, two harvest festivals, dance as community, and Kate's secret: Act Two opens on borrowed calm.", beats=[
        "{a1}Now the analysis: four ideas for the opening of Act Two. "
        "{a1.1}One: tragic knowledge. We know what the characters don't. Rose and Agnes back for tea, a black bike next week, "
        "Mass next Monday: every promise in these pages is shadowed by Michael's prolepsis.",
        "{-a1}{a2}{a2.1}Two: two harvest festivals. The bilberries of Lughnasa, Mother's annual ritual, "
        "and the Festival of the New Yam in Ryanga. Friel draws a parallel between Donegal and Uganda. "
        "Jack's Mass becomes a harvest ceremony: syncretism, Christian and pagan blending.",
        "{-a2}{a3}{a3.1}Three: dance as community. In Ryanga, everyone dances, even lepers with missing limbs, for days. "
        "Think back to the sisters' dance in part five: frantic, defiant, and followed by shame. In Ryanga, the dance belongs to everyone, and nobody is ashamed.",
        "{-a3}{a4}{a4.1}Four: Kate's authority and the outside world. Kate guards reputation: not a syllable outside these walls. "
        "Outside the text: in nineteen-thirties Ireland, the Church dominated public life, so a priest gone native meant scandal. "
        "And part seven told us: it will cost Kate her job.",
        "{-a4}{carte}Here is the opening of Act Two for your essay. {carte.1}Tragic knowledge. {carte.2}Pagan and Christian harvests. "
        "{carte.3}Dance and community. {carte.4}And Kate's fear: control, secrecy, change.",
    ], vis={
        "a1": dict(type="note", cles=["tragic", "prolepsis"], terme="1 · Tragic knowledge",
                   t="“back for tea”, a black bike “next week”, Mass “next Monday”.",
                   etape="Every promise is shadowed by Michael's prolepsis.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["harvest", "syncretism"], terme="2 · Two harvest festivals",
                   t="Lughnasa bilberries, “the annual ritual” ↔ “the Festival of the New Yam”.",
                   etape="Syncretism: the Mass becomes “A harvest ceremony”.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["community", "dance"], terme="3 · Dance as community",
                   t="Lepers dancing “for days on end”: worship and celebration in one.",
                   etape="In Ballybeg, the sisters' dance ended in shame.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["reputation", "Church"], terme="4 · Kate's authority",
                   t="“This must be kept in the family”: “not a syllable!”",
                   etape="Outside the text: 1930s Ireland, a Church-dominated society.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="ACT TWO OPENS", branches=[
            dict(t="Tragic knowledge", items=["“back for tea”", "the black bike", "Mass “next Monday”"]),
            dict(t="Harvests", items=["“every Lughnasa”", "“the Festival of the New Yam”", "“A harvest ceremony”"]),
            dict(t="Dance", items=["lepers dancing “for days on end”", "religious = secular"]),
            dict(t="Kate's fear", items=["“not our Jack at all”", "“kept in the family”", "“not a syllable!”"])]),
    }),
]

QUIZ = [
    dict(q="When does Act Two take place?",
         r=["Early September, three weeks after Act One", "The next morning", "At Christmas", "A year later, in August 1937"],
         ok=0, voir="jeu1",
         ex="“Early September; three weeks later.” The very month Michael announced Rose and Agnes would leave."),
    dict(q="Why does Maggie's manner change when the boy talks about his bicycle?",
         r=["She doubts Gerry's promise of a black bike", "She is jealous of the boy", "She hates bicycles",
            "She knows Kate will forbid it"], ok=0, voir="jeu1.10",
         ex="“(Softly.) Your daddy told you that?” In part six, Gerry admitted the bike only came in blue."),
    dict(q="How does the stage direction describe Jack in Act Two?",
         r=["Much stronger, “very sprightly and alert”", "Weaker and confused", "Dressed in his white uniform",
            "Silent and motionless"], ok=0, voir="c_alert",
         ex="He has lost his top coat and hat and wears a garish sweater, “probably a sister's”."),
    dict(q="Why does Jack want to offer sacrifice to Obi?",
         r=["So that the crops will flourish", "To cure the lepers", "To bring the rain for the kites", "To please the bishop"],
         ok=0, voir="c_obi", ex="Obi is “our Great Goddess of the Earth”: note the possessive “our”, the priest speaks from inside the tribe."),
    dict(q="What, according to Jack, is remarkable about Ryangan culture?",
         r=["There is no distinction between the religious and the secular", "It forbids dancing",
            "It has accepted the Catholic Mass completely", "It has no festivals"], ok=0, voir="c_secular",
         ex="The ceremony “grows naturally into a secular celebration”: the opposite of Kate's Ballybeg."),
    dict(q="What does Kate demand at the end of the scene?",
         r=["That Jack's change be kept in the family", "That Jack leave the house", "That Maggie fetch the priest",
            "That Rose and Agnes come home at once"], ok=0, voir="jeu4.12",
         ex="“Not a word of this must go outside these walls – d'you hear? – not a syllable!”"),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
