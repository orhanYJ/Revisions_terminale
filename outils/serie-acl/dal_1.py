"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 1 : le monologue d'ouverture (PDF de travail, p. 1-2).

Vidéo en anglais (l'essay se rédige en anglais), même chaîne que les séries philo : outils/serie-philo/generer.py dal_1.
Une partie par scène de la pièce : ce qui se passe, les citations clés lues et expliquées, puis l'analyse en fin de
partie. Citations courtes, à fin d'analyse (droit d'auteur : le texte de Friel n'est pas reproduit dans le site).
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

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}A man stands alone in a pool of light. Behind him, in the dark, seven people are standing perfectly still. "
        "He turns to us, and he starts to remember.",
        "{-q1}That is how Dancing at Lughnasa begins. Before a single character speaks to another, "
        "the play tells us one thing: everything we are about to see is a memory.",
        "{-tab_don}{serie}In this series, we go through the play scene by scene. For each one: what happens, "
        "the key quotations explained, and at the end, the analysis you can use in your essay.",
        "Part one: the opening monologue. Only two pages… but they hold the whole play in miniature.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Everything we are about to see is a memory."),
        "serie": dict(type="mot", t="Scene by scene", g="what happens · the key quotations · the analysis", y=270, taille=88),
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
        "{-fiche}{-tab_abb}{tab_gle}A detail from outside the text, but worth knowing: Friel dedicated the play to the memory of "
        "five women from Glenties, in Donegal: his own mother and his aunts. "
        "So the play is fiction, but it grows out of a real family memory.",
        "{-tab_gle}{gens}Who lives in the house? {gens.1}Five unmarried sisters, the Mundy sisters. "
        "{gens.2}Kate, the eldest, a schoolteacher, and the only one with a real salary. "
        "{gens.3}Maggie, the joker, who keeps the house running. "
        "{gens.4}Agnes and Rose, who knit gloves to earn a little money. "
        "{gens.5}And Chris, the youngest, who has a seven-year-old son, Michael, without being married.",
        "{-gens}{gens2}Three men complete the picture. {gens2.1}Father Jack, their brother, a missionary priest "
        "just back from Africa. {gens2.2}Gerry Evans, Michael's father, who turns up only now and then. "
        "{gens2.3}And Michael himself: a boy of seven in 1936… and the adult who tells the story.",
        "{-gens2}{lug}And the title? {lug.1}Lughnasa is the old Celtic harvest festival, held at the start of August, "
        "in honour of the pagan god Lugh. Keep that word pagan in mind: it will come back, again and again.",
    ], vis={
        "tab_fri": dict(type="tableau", img="dal-friel-statue", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .4],
                        legende="Brian Friel and John B. Keane, sculpture in Dublin (photo Spleodrach, CC BY-SA 4.0)"),
        "tab_abb": dict(type="tableau", img="dal-abbey", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                        legende="The Abbey Theatre, Dublin (photo bjaglin, CC BY 2.0)"),
        "fiche": dict(type="liste", titre="Dancing at Lughnasa · Brian Friel", items=[
            "First staged in 1990, Abbey Theatre, Dublin",
            "Set in August 1936, near Ballybeg, County Donegal"], marques=["1990", "1936"], x=170, y=200, w=940),
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=False, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "gens": dict(type="liste", titre="The Mundy household", items=[
            "Five unmarried sisters, the Mundys",
            "Kate: the eldest, a schoolteacher",
            "Maggie: the joker, runs the house",
            "Agnes and Rose: knit gloves for money",
            "Chris: the youngest, Michael's mother"], marques=["5", "K", "M", "A·R", "C"], x=150, y=130, w=980),
        "gens2": dict(type="liste", titre="And the men", items=[
            "Father Jack: their brother, a missionary priest",
            "Gerry Evans: Michael's absent father",
            "Michael: seven years old in 1936, the narrator now"], marques=["J", "G", "M"], x=150, y=170, w=980),
        "lug": dict(type="def", cles=["harvest", "pagan"], terme="Lughnasa",
                    t="The old Celtic harvest festival, at the start of August, in honour of the pagan god Lugh.",
                    etape="A pagan word in a Catholic house: the tension starts with the title.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. un cercle de lumière
    dict(id="plateau", chap="A pool of light", fond="nuit", humeur="mystere",
         retenir="The play opens on a frozen tableau: we meet the characters as images in Michael's mind.", beats=[
        "{plateau}Now, the very first stage direction. The whole stage is dark. "
        "{plateau.1}Michael stands downstage, at the front, in a pool of light.",
        "{plateau.2}Then the lights come up slowly, and we see the others: the five sisters, Jack and Gerry, "
        "standing motionless, in what Friel calls a formal tableau. Like figures in an old photograph.",
        "They hold these positions the whole time Michael talks to the audience. "
        "They do not move, they do not speak. They are waiting to be remembered.",
        "{plateau.3}Only when he has finished does the light change to a warm summer afternoon. "
        "Michael, Kate, Gerry and Jack go off, and the others come to life, busy with their everyday tasks.",
        "{-plateau}{note1}Notice what this does. Before the story even starts, we see every character at once, "
        "frozen, arranged by someone. Nothing here is happening for the first time: it is being called back.",
    ], vis={
        "plateau": dict(type="illu", nom="plateau", x=140, y=90, w=1000, h=490),
        "note1": dict(type="note", cles=["frozen", "arranged"], terme="Stage direction · page 1",
                      t="All the characters are on stage at once, motionless, arranged like a photograph.",
                      etape="We are inside a memory before the story begins.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. deux souvenirs
    dict(id="souvenirs", chap="Two memories", fond="aube", humeur="lumiere",
         retenir="The wireless (Marconi) and Jack's return: two memories of summer 1936, always linked.", beats=[
        "{tab_rad}Michael's first sentence sets the tone.",
        ("C", "When I cast my mind back to that summer of 1936 different kinds of memories offer themselves to me.", "c_cast"),
        "{-tab_rad}He does not say: this is what happened. He says: memories offer themselves to me. "
        "They come to him, several of them, of different kinds. Memory here is not a record. It is a choice.",
        "{tab_rad2}{-c_cast}{radio}The first memory: the wireless. That summer, the family got their first radio set, "
        "and, he says, it obsessed us.",
        "{radio.1}Aunt Maggie, the joker, wanted to give it a name: Lugh, after the god of the harvest. "
        "{radio.2}But Aunt Kate, the schoolteacher, refused.",
        "{-c_cast}",
        "{-radio}",
        ("C", "she said it would be sinful to christen an inanimate object with any kind of name, not to talk of a pagan god.",
         "c_sinful"),
        "{-radio}So they simply called it Marconi, the brand name on the set. "
        "A tiny family quarrel… but look at it closely. Maggie plays with the pagan. Kate stands guard for the Church. "
        "That conflict, in a single joke about a radio, is the conflict of the whole play.",
        "{-tab_rad2}{tab_kil}{-c_cast}{-c_sinful}{jack}The second memory: Uncle Jack. {jack.1}Three weeks before the radio, Michael's uncle came home "
        "from Africa for the first time ever. {jack.2}For twenty-five years he had worked in a leper colony in a village "
        "called Ryanga, in Uganda. {jack.3}He left it only once, for about six months during the First World War, "
        "as a chaplain to the British army in East Africa.",
        "{-jack}And then comes a sentence that seems almost casual.",
        "{-c_cast}",
        "{-c_sinful}",
        ("C", "And now in his early fifties and in bad health he had come home to Ballybeg – as it turned out – to die.",
         "c_die"),
        "{-tab_kil}Three small words: as it turned out. The adult Michael already knows the ending, and he gives it away "
        "in the first minute. Jack will die. The question will never be whether, only how we watch him until then.",
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.15, .4, .5], a=[1.3, .6, .5],
                        legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "c_cast": dict(type="cit", a="Michael", o="opening monologue, p. 1", x=170, y=200, w=940),
        "tab_rad2": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                         legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "radio": dict(type="cols", g="Maggie", gq="wants to call it Lugh, the pagan god", d="Kate",
                      dq="“sinful”: a Catholic refusal", vs="≠", repere="pagan / Christian"),
        "c_sinful": dict(type="cit", a="Michael, about Kate", o="p. 1", x=170, y=200, w=940),
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "jack": dict(type="liste", titre="Father Jack", items=[
            "Home from Africa for the first time ever",
            "25 years in a leper colony: Ryanga, Uganda",
            "WWI: chaplain to the British army in East Africa"], marques=["1", "25", "WWI"], x=150, y=180, w=980),
        "c_die": dict(type="cit", a="Michael", o="p. 1", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. toujours liés
    dict(id="lies", chap="Always linked", fond="nuit", humeur="tension",
         retenir="Michael's memory works by juxtaposition: the radio's joy always comes with Jack's decline.", beats=[
        "{liens}Here is the key move of the monologue. Michael tells us that these two memories, {liens.1}the wireless and Jack, "
        "are always linked. When one comes back, the other comes with it.",
        "{liens.2}So when he remembers his shock at Jack's appearance, shrunken and jaundiced with malaria, "
        "{liens.3}at the same moment he remembers his delight, his awe, at the sheer magic of the radio.",
        "{-liens}{tab_rad3}And then the most famous image: the kitchen throbbing with Irish dance music, beamed all the way from Athlone.",
        ("C", "my mother and her sisters suddenly catching hands and dancing a spontaneous step-dance and laughing – screaming! – "
              "like excited schoolgirls", "c_dance"),
        "{-tab_rad3}{-c_dance}{scream}Listen to the correction in the middle: laughing… no: screaming. Joy is already tipping into something wilder. "
        "{-scream}{forlorn}And at the very same time, Michael sees that forlorn figure of Father Jack, shuffling from room to room, "
        "as if he were searching for something but couldn't remember what.",
        "{-forlorn}{jux}This is juxtaposition: {jux.1}the dance and the decline, {jux.2}life and death, {jux.3}noise and silence, "
        "set side by side in one breath. Michael cannot remember the happiness without the loss. "
        "That is exactly how the play will work: every moment of joy carries its shadow.",
    ], vis={
        "liens": dict(type="illu", nom="liens", x=140, y=90, w=1000, h=480),
        "tab_rad3": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.25, .5, .4], a=[1.05, .5, .5],
                         legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "c_dance": dict(type="cit", a="Michael", o="p. 1", x=170, y=170, w=940),
        "scream": dict(type="mot", t="laughing – screaming!", g="joy already tipping into something wilder", y=250, taille=84),
        "forlorn": dict(type="note", cles=["forlorn", "shuffling"], terme="At the same time · p. 1",
                        t="“that forlorn figure of Father Jack shuffling from room to room”",
                        etape="searching for something he cannot remember", x=170, y=200, w=940),
        "jux": dict(type="liste", titre="Juxtaposition", cles=["juxtaposition"], items=[
            "the sisters' dance  ↔  Jack's decline",
            "life, music  ↔  illness, death",
            "noise, laughter  ↔  silence, confusion"], marques=["1", "2", "3"], x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. la brèche
    dict(id="breche", chap="A widening breach", fond="aube", humeur="tension",
         retenir="“A widening breach between what seemed to be and what was”: the play's subject in one phrase.", beats=[
        "{unease}Even though he was only seven, Michael says, he had a sense of unease. And then comes the sentence "
        "that you should know by heart.",
        "{-unease}",
        ("C", "some awareness of a widening breach between what seemed to be and what was, of things changing too quickly "
              "before my eyes, of becoming what they ought not to be.", "c_breach"),
        "{-c_breach}{-unease}{breche}A breach is a gap, a crack. {breche.1}On the surface, the house seems stable: a family, a routine, a faith. "
        "{breche.2}Underneath, things are changing too quickly, becoming what they ought not to be. "
        "The whole play lives in that gap between appearance and reality.",
        "{-breche}{-c_breach}{-unease}{trois}Michael offers three possible reasons for his unease. {trois.1}First: Uncle Jack had not turned out at all "
        "like the resplendent figure in his head. The hero was a sick, confused old man.",
        "{trois.2}Second, and this is a striking line:",
        "{-c_breach}",
        "{-trois}",
        "{-unease}",
        ("C", "I had witnessed Marconi's voodoo derange those kind, sensible women and transform them into shrieking strangers.",
         "c_voodoo"),
        "Voodoo: a word of magic, of possession. The radio is seen as a pagan force that takes hold of the sisters. "
        "Kind and sensible on one side, shrieking strangers on the other: the breach again, inside the women themselves.",
        "{trois.3}Third: during those Lughnasa weeks, his father, Gerry Evans, visited twice, and for the first time in his life, "
        "Michael had a chance to observe him.",
        "{-trois}Then the light changes. The memory comes to life. And the play begins.",
    ], vis={
        "unease": dict(type="mot", t="a sense of unease", g="felt by a child of seven, named by the adult", y=250, taille=88),
        "c_breach": dict(type="cit", a="Michael", o="p. 2", x=170, y=170, w=940),
        "breche": dict(type="illu", nom="breche", x=140, y=110, w=1000, h=440),
        "trois": dict(type="liste", titre="Three reasons for his unease", items=[
            "Jack is not the “resplendent figure” he imagined",
            "“Marconi's voodoo” turns the sisters into strangers",
            "Gerry Evans, his father, visits twice"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_voodoo": dict(type="cit", a="Michael", o="p. 2", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VI. l'analyse
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
            "Offstage: we only hear his voice"], ok=0, voir="plateau",
         ex="The rest of the stage is dark; the other characters stand motionless in a “formal tableau” while he speaks to the audience."),
    dict(q="Why do they call the wireless “Marconi”?",
         r=["Because Kate refused to name it after the pagan god Lugh", "Because Jack brought it from Africa",
            "Because Gerry sold it to them", "Because Maggie loved Italian music"], ok=0, voir="radio",
         ex="Maggie wanted to call it Lugh; Kate said it would be “sinful” to christen an object, let alone after a pagan god. So it kept its brand name."),
    dict(q="What does “as it turned out – to die” do to the audience?",
         r=["It creates dramatic irony: we know Jack's fate before the characters do", "It shows that Michael is lying",
            "It announces a comic ending", "It tells us Jack is already dead when the play starts"], ok=0, voir="c_die",
         ex="This is a prolepsis: the adult narrator gives away the ending, and we watch everything that follows with that knowledge."),
    dict(q="Which two memories are “always linked” in Michael's mind?",
         r=["The first wireless and Father Jack's return", "Lughnasa and Christmas", "His father and his mother",
            "The harvest dance and the kites"], ok=0, voir="liens",
         ex="The radio's “sheer magic” always comes back with Jack's shock appearance, “shrunken and jaundiced with malaria”: a juxtaposition."),
    dict(q="The “widening breach” is a gap between…",
         r=["what seemed to be and what was", "the kitchen and the garden", "Ireland and Africa", "Kate and Maggie"], ok=0,
         voir="c_breach", ex="Appearance against reality: on the surface a stable house, underneath “things changing too quickly”."),
    dict(q="Why does Michael use the word “voodoo” about the radio?",
         r=["It presents the music as a pagan, possessing force over the sisters", "Because the radio came from Haiti",
            "To mock Father Jack's religion", "Because the radio is broken"], ok=0, voir="c_voodoo",
         ex="“Marconi's voodoo” “derange[s]” the “kind, sensible women” into “shrieking strangers”: magic, possession, loss of control."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Brian Friel and John B. Keane, sculpture, Dublin (Spleodrach, CC BY-SA 4.0); Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Abbey Theatre exterior (bjaglin, CC BY 2.0); "
    "Glenties (Thpohl, public domain); valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
