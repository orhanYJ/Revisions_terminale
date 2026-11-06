"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 13 : le tableau final (PDF de travail, p. 74-75).

Version « jouée » (05/11/2026, demande d'Orhan : « comme Parable of the Sower », personnages représentés, mouvements) :
le tableau final est joué sur le plateau (visuel jeu) en suivant la didascalie de la p. 74 point par point : Maggie rentre dans
la cuisine, Michael entre ; positions « similar to their positions at the beginning of the play — with some changes » :
Agnes et Gerry sur le banc du jardin, Jack au garde-à-vous au coude d'Agnes, un cerf-volant (visage tourné vers la salle) entre
Gerry et Agnes, l'autre entre Agnes et Jack, Rose au fond à gauche du plateau (UL : au fond à droite vu de la salle), Maggie à
la fenêtre de la cuisine, Kate à l'avant-scène droite (DR : à gauche vu de la salle), Chris à la porte ; Kate pleure doucement ;
lumière dorée très douce dès que Michael parle. Puis la musique « It is Time to Say Goodnight » (pas de la radio : radio éteinte),
tout le monde oscille très légèrement, et à la fin « Slowly bring up the music. Slowly bring down the lights. ».
Le dernier monologue est dit par Michael (bulles), rien de ce qu'il raconte n'est joué. Puis cinq citations à connaître,
l'analyse de la fin et « The whole play for your essay » (carte de la pièce entière et huit citations à savoir par cœur,
toutes vérifiées sur les images des pages 2, 14, 23, 37, 42, 43, 63 et 75).

Début : p. 74, didascalie « (MAGGIE moves into the kitchen. MICHAEL enters. … ) ». Fin : « (Slowly bring up the music.
Slowly bring down the lights.) », THE END (p. 75). Dernière partie de la série.
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_13. Citations courtes, à fin d'analyse ; le reste est résumé.
Coquilles du PDF évitées dans les citations (« GERR », « Agnes an Rose », « that is owes nothing », « I that memory »).
Limites du moteur : les cerfs-volants ne peuvent pas osciller (la didascalie « even the grinning kites » est dite en bandeau) ;
la porte du plateau tient lieu de « front door ». Costumes et chapeaux gardés de la partie 12 (Jack en uniforme blanc et
chapeau de paille, Gerry en tricorne), le coq resté sur la nappe : le texte ne dit pas qu'ils changent.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-13"
NOTION = "Dancing at Lughnasa"
NUM = 13
TITRE = "The final tableau"
SUIVANT = ""
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Mundy": "Mundy",
                 "Ballybeg": "Bally-beg"}

PERSOS = ["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack", "Gerry", "Michael"]
# fin de la partie 12 : chacun où il était à la devinette de Maggie
FIN_12 = {"Maggie": [720, 545], "Kate": [660, 410], "Agnes": [745, 372], "Rose": "banc_g", "Chris": [1075, 505],
          "Jack": [860, 490], "Gerry": [965, 395]}
# le tableau final (p. 74) ; Michael à l'extrême avant-scène gauche (vu de la salle : à droite), devant Jack
MICHAEL = [1065, 545]
TABLEAU = {"Gerry": [835, 352], "Agnes": [915, 352], "Jack": [995, 372], "Rose": [1035, 232], "Maggie": "fenetre",
           "Kate": [150, 520], "Chris": "porte", "Michael": MICHAEL}
TOUS = ["Kate", "Maggie", "Agnes", "Rose", "Chris", "Jack", "Gerry", "Michael"]
COSTUMES = dict(costume={"Jack": "blanc"}, chapeau={"Jack": "paille", "Gerry": "tricorne"})

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Maggie has forgotten the answer to her own riddle. She moves into the kitchen. "
        "And for the last time, Michael steps forward.",
        "{-q1}Two pages left, to close the circle that opened on page one.",
        "{-tab_don}{serie}Part thirteen, the last part: the final stage picture, Michael's last monologue… "
        "and then the whole play, ready for your essay.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="For the last time, Michael steps forward."),
        "serie": dict(type="mot", t="The end of the play", g="the final tableau · the last monologue · the whole play",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 13", t="The final tableau",
                      sous="The end of Act Two · pages 74 – 75"),
    }),

    # ------------------------------------------------------------------ I. le tableau (joué)
    dict(id="tableau", chap="Back where we began", fond="nuit", humeur="mystere", beats=[
        "{jeu1}Page seventy-four. The family is in the garden, around the cloth, Jack in his white uniform and the straw hat, "
        "Gerry in the tricorn. Maggie gives up on her riddle.",
        "{jeu1.1}She moves into the kitchen. And Michael enters.",
        "{jeu1.2}Now, says Friel, the characters are in positions similar to their positions at the beginning of the play… "
        "with some changes.",
        "{jeu1.3}Agnes and Gerry are on the garden seat. Jack stands stiffly to attention at Agnes's elbow. "
        "{jeu1.4}One kite, facing boldly out front, stands between Gerry and Agnes; the other, between Agnes and Jack. "
        "The grinning faces look straight at us.",
        "{jeu1.5}Rose is upstage left. Maggie is at the kitchen window. Kate is downstage right. Chris is at the front door.",
        "{jeu1.6}On page one, it was Rose who sat on the seat with Gerry, and Agnes who stood upstage left. "
        "The two sisters who will leave have swapped places.",
        "{jeu1.7}And as Michael begins to speak, the stage is lit in a very soft, golden light. "
        "During the whole speech, Kate cries quietly.",
        ("P", 1.5),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=FIN_12, act={"Rose": "assis"}, cam="tout", objets={"kites_faces": [915, 362], "coq": [800, 455]},
                 note="MAGGIE. “… God I've forgotten!” (p. 74)", **COSTUMES),
            dict(pos={"Maggie": "fenetre", "Michael": MICHAEL}, duree=3.0,
                 note="(MAGGIE moves into the kitchen. MICHAEL enters.)"),
            dict(pos=TABLEAU, act={"Rose": "debout", "Gerry": "assis", "Agnes": "assis"}, duree=4.0,
                 note="“positions similar to their positions at the beginning of the play — with some changes”"),
            dict(note="AGNES and GERRY are on the garden seat. JACK stands stiffly to attention at AGNES's elbow."),
            dict(cam="jardin", note="“One kite, facing boldly out front, stands between GERRY and AGNES; the other between AGNES and JACK.”"),
            dict(cam="tout", note="ROSE is UL. MAGGIE is at the kitchen window. KATE is DR. CHRIS is at the front door."),
            dict(note="Page 1: ROSE and GERRY on the seat, AGNES upstage left · Page 74: the other way round"),
            dict(lumiere="or", act={"Kate": "pleure"},
                 note="“the stage is lit in a very soft, golden light” · “During MICHAEL's speech KATE cries quietly.”"),
        ]),
    }),

    # ------------------------------------------------------------------ II. ce qu'ils sont devenus (raconté)
    dict(id="devenir", chap="The heart of the house", fond="nuit", humeur="calme", beats=[
        "{jeu2}Michael speaks. First, the facts, in flat, short sentences. Nothing is acted: the tableau stays still.",
        ("C", "As I said, Father Jack was dead within twelve months.", "jeu2.1"),
        "{jeu2.2}With Jack, Agnes and Rose all gone, the heart seemed to go out of the house. "
        "{jeu2.3}Maggie took on Rose and Agnes's tasks, and pretended to believe that nothing had changed.",
        ("C", "My mother spent the rest of her life in the knitting factory – and hated every day of it.", "jeu2.4"),
        "{jeu2.5}And Kate, after a few years doing nothing, became the tutor of Austin Morgan's young family. "
        "Yes: the man Rose teased her about, back in part three.",
        "{jeu2.6}Feel the irony. The factory ruined Agnes and Rose; Chris works there for life. "
        "And Kate teaches the children of the man she seemed to love in silence. And Michael himself?",
        ("C", "when my time came to go away, in the selfish way of young men I was happy to escape.", "jeu2.7"),
        "{jeu2.8}Escape. He leaves, like Agnes and Rose, like Gerry, like Jack long ago. "
        "Emigration runs through the whole family. And selfish carries his guilt.",
        ("P", 1.0),
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=TABLEAU, act={"Rose": "debout", "Gerry": "assis", "Agnes": "assis", "Kate": "pleure"}, lumiere="or",
                 cam="tout", objets={"kites_faces": [915, 362], "coq": [800, 455]},
                 note="Michael tells what became of them (told, not shown)", **COSTUMES),
            dict(dit=["Michael", "As I said, Father Jack was dead within twelve months."]),
            dict(note="With Jack, Agnes and Rose gone, “the heart seemed to go out of the house” (p. 74)"),
            dict(note="Maggie “pretended to believe that nothing had changed”"),
            dict(dit=["Michael", "My mother spent the rest of her life in the knitting factory – and hated every day of it."]),
            dict(note="Kate: “the job of tutoring the young family of Austin Morgan of the Arcade”"),
            dict(note="“But much of the spirit and fun had gone out of their lives”"),
            dict(dit=["Michael", "when my time came to go away, in the selfish way of young men I was happy to escape."]),
            dict(note="Michael leaves too: like Agnes and Rose, like Gerry, like Jack long ago."),
        ]),
    }),

    # ------------------------------------------------------------------ III. la musique du souvenir, la danse sans les mots
    dict(id="musique", chap="A dream music", fond="nuit", humeur="calme", beats=[
        "{jeu3}Now, very softly, just audible, music fades in. The class text names it: It is Time to Say Goodnight. "
        "And it is not from the radio speaker. Marconi is silent: this music comes from memory.",
        "{jeu3.1}As Michael continues, everybody sways very slightly from side to side… even the grinning kites. "
        "The movement is so minimal, says Friel, that we cannot be quite certain if it is happening, or if we imagine it.",
        ("C", "And so, when I cast my mind back to that summer of 1936, different kinds of memories offer themselves to me.",
         "jeu3.2"),
        "{jeu3.3}The first sentence of the play, almost word for word. But one memory visits him most often, "
        "and it owes nothing to fact.",
        ("C", "In that memory atmosphere is more real than incident and everything is simultaneously actual and illusory.",
         "jeu3.4"),
        "{jeu3.5}The air is nostalgic with the music of the thirties: a mirage of sound, a dream music, both heard and imagined. "
        "{jeu3.6}And everybody seems to be floating on it, moving rhythmically, languorously, in complete isolation.",
        ("C", "When I remember it, I think of it as dancing.", "jeu3.7"),
        ("C", "Dancing with eyes half closed because to open them would break the spell.", "jeu3.8"),
        ("C", "Dancing as if language had surrendered to movement", "jeu3.9"),
        "{jeu3.10}As if this ritual, this wordless ceremony, was now the way to speak, to whisper private and sacred things.",
        ("C", "Dancing as if language no longer existed because words were no longer necessary …", "jeu3.11"),
        ("P", 1.5),
        "{jeu3.12}Slowly bring up the music. Slowly bring down the lights.",
        ("P", 3.0),
        "{jeu3.13}The end.",
        ("P", 2.5),
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=TABLEAU, act={"Rose": "debout", "Gerry": "assis", "Agnes": "assis", "Kate": "pleure"}, lumiere="or",
                 radio=False, cam="tout", objets={"kites_faces": [915, 362], "coq": [800, 455]},
                 note="(Now fade in very softly, just audible, the music – “It is Time to Say Goodnight” [not from the radio speaker].)",
                 **COSTUMES),
            dict(act={n: "balance" for n in TOUS},
                 note="“everybody sways very slightly from side to side – even the grinning kites”"),
            dict(dit=["Michael", "And so, when I cast my mind back to that summer of 1936, …"], note="(p. 74, and p. 1)"),
            dict(note="one memory “that visits me most often” · it “owes nothing to fact”"),
            dict(dit=["Michael", "In that memory atmosphere is more real than incident …"]),
            dict(note="“a mirage of sound – a dream music that is both heard and imagined”"),
            dict(note="“floating on those sweet sounds, moving rhythmically, languorously, in complete isolation” (p. 75)"),
            dict(dit=["Michael", "When I remember it, I think of it as dancing."]),
            dict(dit=["Michael", "Dancing with eyes half closed because to open them would break the spell."]),
            dict(dit=["Michael", "Dancing as if language had surrendered to movement"]),
            dict(note="“this ritual, this wordless ceremony” · “to whisper private and sacred things”"),
            dict(dit=["Michael", "Dancing as if language no longer existed because words were no longer necessary …"]),
            dict(lumiere="sombre", eclaire=[], note="(Slowly bring up the music. Slowly bring down the lights.)"),
            dict(note="THE END"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. cinq citations à connaître
    dict(id="repliques", chap="Key lines to know", fond="aube", humeur="calme",
         retenir="The golden haze, the first sentence again, atmosphere over incident, language surrendered, words no longer necessary.", beats=[
        "{cinq}The ending is short, but every line counts. Five of them are worth knowing by heart.",
        "{-cinq}First, the light.",
        ("C", "the stage is lit in a very soft, golden light so that the tableau we see is almost, but not quite, in a haze.",
         "c_haze"),
        "{-c_haze}{haze}Golden is the colour of nostalgia. "
        "{haze.1}A haze is a mist: we see the family almost, but not quite, clearly. Just like a memory.",
        "{-haze}Then, the first sentence, again.",
        ("C", "And so, when I cast my mind back to that summer of 1936, different kinds of memories offer themselves to me.",
         "c_cast"),
        "{-c_cast}{cercle}Page one, and now page seventy-four. The play comes full circle.",
        "{-cercle}Then, memory against fact.",
        ("C", "In that memory atmosphere is more real than incident and everything is simultaneously actual and illusory.",
         "c_atmo"),
        "{-c_atmo}{atmo}Atmosphere: the feeling of a moment. Incident: what actually happens. "
        "For Michael, the feeling is more real than the facts. Facts get a few flat sentences; the feeling gets his finest prose.",
        "{-atmo}{para}Look at the pairs. {para.1}Actual and illusory. {para.2}A music heard and imagined. "
        "{para.3}Itself and its own echo. {para.4}An afternoon bewitched, maybe haunted. "
        "Each pair holds two things at once, like Kate's dance in part five: simultaneously controlled and frantic.",
        "{-para}Then, the dance.",
        ("C", "Dancing as if language had surrendered to movement – as if this ritual, this wordless ceremony, was now the way to speak",
         "c_surr"),
        "{-c_surr}{rite}{rite.1}Language surrenders, like an army laying down its arms. "
        "{rite.2}The dance becomes a ritual, a wordless ceremony. "
        "{rite.3}A way to whisper private and sacred things, to be in touch with some otherness. "
        "{rite.4}As if the very heart of life and all its hopes might be found in those assuaging notes. "
        "Dancing as if, dancing as if: this repetition is called anaphora. The sentences rise like music, to the last words.",
        "{-rite}",
        ("C", "Dancing as if language no longer existed because words were no longer necessary …", "c_words"),
        "{-c_words}{fin}The sentence does not end: three dots. The music takes over from words.",
    ], vis={
        "cinq": dict(type="mot", t="Five lines to know", g="the ending · pages 74 – 75", y=250, taille=80),
        "c_haze": dict(type="cit", a="Stage direction", o="p. 74", x=170, y=200, w=940),
        "haze": dict(type="note", cles=["golden", "haze"], terme="Light as memory",
                     t="Golden: nostalgia. A haze: “almost, but not quite” clear.",
                     etape="The stage itself looks like a memory.", x=170, y=200, w=940),
        "c_cast": dict(type="cit", a="Michael", o="p. 74 (and p. 1)", x=170, y=190, w=940),
        "cercle": dict(type="cols", g="Page 1", gq="“When I cast my mind back to that summer of 1936 …”", d="Page 74",
                       dq="“And so, when I cast my mind back …”", vs="=", repere="full circle"),
        "c_atmo": dict(type="cit", a="Michael", o="p. 74", x=170, y=200, w=940),
        "atmo": dict(type="cols", g="Atmosphere", gq="the feeling of a moment", d="Incident",
                     dq="what actually happens", vs=">", repere="memory over fact"),
        "para": dict(type="liste", titre="Paradoxes of memory · pages 74 – 75", cles=["and"], items=[
            "“actual and illusory”",
            "“both heard and imagined”",
            "“both itself and its own echo”",
            "“bewitched, maybe haunted”"], marques=["1", "2", "3", "4"], x=170, y=160, w=940),
        "c_surr": dict(type="cit", a="Michael", o="p. 75", x=170, y=180, w=940),
        "rite": dict(type="liste", titre="A wordless ceremony · anaphora: “Dancing as if …”", cles=["ritual", "sacred"], items=[
            "language “surrendered to movement”",
            "“this ritual, this wordless ceremony”",
            "“private and sacred things” · “some otherness”",
            "“the very heart of life and all its hopes”"], marques=["1", "2", "3", "4"], x=150, y=180, w=980),
        "c_words": dict(type="cit", a="Michael · the last words of the play", o="p. 75", x=170, y=200, w=940),
        "fin": dict(type="note", cles=["music", "lights"], terme="The last stage direction · p. 75",
                    t="“Slowly bring up the music. Slowly bring down the lights.”",
                    etape="An unfinished sentence; the music takes over from words.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Circle, memory over fact, dance beyond words, ritual: the ending gathers the whole play.", beats=[
        "{a1}Now the analysis of the ending. Four ideas. "
        "{a1.1}One: a circular structure. The same first sentence, the same tableau, almost the same positions. "
        "But the circle is not perfect: Agnes and Rose have swapped places, Kate cries. "
        "Something has been lost on the way.",
        "{-a1}{a2}{a2.1}Two: memory over fact. Atmosphere is more real than incident. "
        "Deaths and departures get a few dry lines; the feeling gets the light, the music, the poetry. "
        "A memory play shows how the past lives in us.",
        "{-a2}{a3}{a3.1}Three: dance and language. All through the play, words fail: Jack loses his English, Gerry lies, "
        "Kate cannot say what she feels. Remember Maggie's answer to Jack: Or dance. "
        "The last speech says it fully: words were no longer necessary.",
        "{-a3}{a4}{a4.1}Four: ritual. Ritual, ceremony, sacred, otherness: the vocabulary of religion. "
        "Jack's ceremony, the Lughnasa fires, the sisters' wild dance… "
        "In the end, pagan and Christian meet in one human ritual: the dance of memory.",
        "{-a4}{carte}Here is the ending for your essay. {carte.1}The circle. {carte.2}Memory over fact. "
        "{carte.3}Dance and language. {carte.4}Ritual and the sacred.",
    ], vis={
        "a1": dict(type="note", cles=["circular", "swapped"], terme="1 · A circular structure",
                   t="Page 1 = page 74: the same sentence, the same tableau, with changes.",
                   etape="A circle that is not perfect: something has been lost.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["atmosphere", "memory"], terme="2 · Memory over fact",
                   t="“atmosphere is more real than incident”: facts in dry lines, feeling in poetry.",
                   etape="A memory play shows how the past lives in us.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["words", "dance"], terme="3 · Dance and language",
                   t="Jack's lost words, Gerry's lies, Kate's silences; “Or dance.”",
                   etape="“words were no longer necessary”", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["ritual", "sacred"], terme="4 · Ritual",
                   t="“this ritual, this wordless ceremony”, “private and sacred things”.",
                   etape="Pagan and Christian meet in the dance of memory.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE ENDING", branches=[
            dict(t="The circle", items=["first sentence repeated", "the tableau again", "Agnes and Rose swapped"]),
            dict(t="Memory over fact", items=["“a very soft, golden light”", "“atmosphere … more real than incident”",
                                              "“actual and illusory”"]),
            dict(t="Dance and language", items=["“language had surrendered”", "“Or dance.”", "“no longer necessary”"]),
            dict(t="Ritual", items=["“this wordless ceremony”", "“private and sacred things”", "“some otherness”"])]),
    }),

    # ------------------------------------------------------------------ VI. la pièce entière
    dict(id="piece", chap="The whole play for your essay", fond="aube", humeur="lumiere",
         retenir="Four themes, eight quotations: memory, order cracking, pagan and Christian, dance beyond words.", beats=[
        "{tout}Thirteen parts, one summer. The whole play, in four themes. "
        "{tout.1}Memory: a narrator who knows the ending, and a circle from page one to page seventy-four. "
        "{tout.2}Order cracking: Kate's authority, the factory, emigration.",
        "{tout.3}Pagan and Christian: the Lughnasa fires, Jack's ceremony. "
        "{tout.4}And dance beyond words, from the sisters' wild dance to the last speech.",
        "{-tout}{kh1}Now, eight lines to know by heart. Four for Act One. "
        "{kh1.1}Michael, page two: a widening breach between what seemed to be and what was. "
        "{kh1.2}Agnes, page fourteen: I'm only thirty-five. I want to dance. "
        "{kh1.3}The stage direction, page twenty-three: a sense of order being consciously subverted. "
        "{kh1.4}Kate, page thirty-seven: hair cracks are appearing everywhere.",
        "{-kh1}{kh2}And four more. "
        "{kh2.1}Jack, page forty-two: Ceremony! That's the word! "
        "{kh2.2}Michael, page forty-three: both Rose and Agnes would have left for ever. "
        "{kh2.3}Michael, page sixty-three: The Industrial Revolution had finally caught up with Ballybeg. "
        "{kh2.4}And Michael, page seventy-five: dancing as if language had surrendered to movement.",
        "{-kh2}{bonne}Learn them, link them to these four themes, and always answer the question you are given. "
        "That's the end of Dancing at Lughnasa. Good luck with your essay.",
        ("P", 1.5),
    ], vis={
        "tout": dict(type="carte", centre="DANCING AT LUGHNASA", branches=[
            dict(t="Memory", items=["a narrator who knows", "prolepsis, Acts One and Two", "page 1 = page 74"]),
            dict(t="Order cracking", items=["Kate's authority", "the factory", "emigration"]),
            dict(t="Pagan / Christian", items=["the Lughnasa fires", "“Ceremony!”", "syncretism"]),
            dict(t="Dance and language", items=["the sisters' wild dance", "a dance with no words", "the last speech"])]),
        "kh1": dict(type="liste", titre="Know by heart · Act One (page numbers)", items=[
            "“a widening breach between what seemed to be and what was”",
            "“I'm only thirty-five. I want to dance.”",
            "“a sense of order being consciously subverted”",
            "“hair cracks are appearing everywhere”"], marques=["2", "14", "23", "37"], x=150, y=150, w=980),
        "kh2": dict(type="liste", titre="Know by heart · and the rest (page numbers)", items=[
            "“Ceremony! That's the word!”",
            "“both Rose and Agnes would have left for ever”",
            "“The Industrial Revolution had finally caught up with Ballybeg.”",
            "“Dancing as if language had surrendered to movement”"], marques=["42", "43", "63", "75"], x=150, y=150, w=980),
        "bonne": dict(type="mot", t="Good luck", g="learn the lines · link them to a theme · answer the question",
                      y=260, taille=96),
    }),
]

QUIZ = [
    dict(q="How do the final positions differ from the opening tableau?",
         r=["Agnes and Rose have swapped places", "Michael has disappeared", "Kate and Maggie have left the stage",
            "Everyone is now sitting in the kitchen"], ok=0, voir="jeu1.6",
         ex="On page 1 Rose sits on the garden seat with Gerry and Agnes is upstage; on page 74 it is the reverse: the two sisters who leave have swapped."),
    dict(q="Where does the final music come from?",
         r=["Not from the radio: it comes from memory", "From Marconi, finally repaired", "From Gerry's gramophone",
            "From the harvest dance in the village"], ok=0, voir="jeu3",
         ex="The stage direction says “not from the radio speaker”: the music now belongs to Michael's memory."),
    dict(q="Which sentence does Michael repeat from the very start of the play?",
         r=["“When I cast my mind back to that summer of 1936 …”", "“As it turned out – to die”",
            "“A widening breach between what seemed to be and what was”", "“Ceremony! That's the word!”"], ok=0, voir="c_cast",
         ex="The first sentence of page 1 comes back on page 74: the play comes full circle."),
    dict(q="“Atmosphere is more real than incident” means that…",
         r=["the feeling of the memory matters more than the facts", "the weather was very hot in 1936",
            "Michael invents events that never happened", "the plot of the play is very dramatic"], ok=0, voir="c_atmo",
         ex="Incident is what happens; atmosphere is the feeling. The facts take a few flat sentences, the feeling gets Michael's best prose."),
    dict(q="What does Michael do when his “time came to go away”?",
         r=["He was “happy to escape”, “in the selfish way of young men”", "He stayed to look after Kate",
            "He joined Gerry in Spain", "He became a priest like Jack"], ok=0, voir="jeu2.7",
         ex="Michael emigrates too, like Agnes and Rose; the word “selfish” shows the narrator's guilt."),
    dict(q="What are the very last words Michael speaks?",
         r=["“words were no longer necessary …”", "“It is time to say goodnight”", "“I was happy to escape”",
            "“the heart seemed to go out of the house”"], ok=0, voir="c_words",
         ex="“Dancing as if language no longer existed because words were no longer necessary …”: the sentence trails off and the music takes over."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
