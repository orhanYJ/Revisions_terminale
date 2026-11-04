"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 13 : le tableau final (PDF de travail, p. 74-75).

Début : p. 74, didascalie « (MAGGIE moves into the kitchen. MICHAEL enters. The characters are now in positions similar to
their positions at the beginning of the play … ) ». Fin : « (Slowly bring up the music. Slowly bring down the lights.) »,
THE END (p. 75). Dernière partie de la série : analyse de la fin, puis « The whole play for your essay » (carte de la pièce
entière et huit citations à savoir par cœur, toutes vérifiées sur les images des pages 2, 14, 23, 37, 42, 43, 63 et 75).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_13. Citations courtes, à fin d'analyse ; le reste est résumé.
Coquilles du PDF évitées dans les citations (« GERR », « Agnes an Rose », « that is owes nothing », « I that memory »).
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

    # ------------------------------------------------------------------ I. retour au point de départ
    dict(id="tableau", chap="Back where we began", fond="nuit", humeur="mystere",
         retenir="The play ends almost as it began: the same tableau, with changes. Agnes and Rose have swapped places.", beats=[
        "{plateau}Remember the very first image? {plateau.1}Michael in a pool of light… {plateau.2}the others, frozen.",
        "{-plateau}{pos}Now, on page seventy-four, the characters stand in positions similar to the opening… "
        "with some changes, says Friel. {pos.g}On page one, Rose sat on the garden seat with Gerry, and Agnes stood upstage. "
        "{pos.d}Now it is Agnes on the seat with Gerry, and Rose upstage. The two sisters who will leave have swapped places.",
        "{-pos}{det}{det.1}Jack stands stiffly to attention at Agnes's elbow, like the army chaplain he once was. "
        "{det.2}The two kites stand between them, facing boldly out front. "
        "{det.3}And Kate, downstage right, cries quietly during the whole speech.",
        "Then the light.",
        "{-det}",
        ("C", "the stage is lit in a very soft, golden light so that the tableau we see is almost, but not quite, in a haze.",
         "c_haze"),
        "{-c_haze}{haze}Golden is the colour of nostalgia. "
        "{haze.1}A haze is a mist: we see the family almost, but not quite, clearly. Just like a memory.",
    ], vis={
        "plateau": dict(type="illu", nom="plateau", x=140, y=90, w=1000, h=490),
        "pos": dict(type="cols", g="Page 1", gq="Rose and Gerry on the seat · Agnes upstage", d="Page 74",
                    dq="Agnes and Gerry on the seat · Rose upstage", vs="→", repere="the same picture, changed"),
        "det": dict(type="liste", titre="The final picture · page 74", items=[
            "Jack: “stiffly to attention at AGNES's elbow”",
            "The kites, “facing boldly out front”",
            "Kate, downstage right: she “cries quietly”"], marques=["J", "K", "K"], x=150, y=180, w=980),
        "c_haze": dict(type="cit", a="Stage direction", o="p. 74", x=170, y=200, w=940),
        "haze": dict(type="note", cles=["golden", "haze"], terme="Light as memory",
                     t="Golden: nostalgia. A haze: “almost, but not quite” clear.",
                     etape="The stage itself looks like a memory.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. ce qu'ils sont devenus
    dict(id="devenir", chap="The heart of the house", fond="aube", humeur="calme",
         retenir="Jack dies, Agnes and Rose are gone, Chris works in the factory, Michael escapes: the family scatters.", beats=[
        "{tab_gle}{mi}First, the facts, in flat, short sentences. "
        "{mi.1}As I said, Father Jack was dead within twelve months. "
        "{mi.2}With Jack, Agnes and Rose all gone, the heart seemed to go out of the house.",
        "{-mi}{-tab_gle}{fates}Then, one by one, the sisters who stayed. "
        "{fates.1}Maggie took on Rose and Agnes's tasks, and pretended to believe that nothing had changed. "
        "{fates.2}Chris spent the rest of her life in the knitting factory, and hated every day of it. "
        "{fates.3}And Kate, after a few years doing nothing, became the tutor of Austin Morgan's young family. "
        "Yes: the man Rose teased her about, back in part three.",
        "{-fates}{ironie}Feel the irony. {ironie.1}The factory ruined Agnes and Rose. "
        "{ironie.2}Now Chris works there for life. "
        "{ironie.3}And Kate teaches the children of the man she loved in silence.",
        "And Michael himself?",
        "{-ironie}",
        ("C", "when my time came to go away, in the selfish way of young men I was happy to escape.", "c_escape"),
        "{-c_escape}{fuite}Escape. He leaves, like Agnes and Rose, like Gerry, like Jack long ago. "
        "{fuite.1}Emigration runs through the whole family. "
        "And selfish carries his guilt.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "mi": dict(type="liste", titre="As I said … · page 74", items=[
            "“Father Jack was dead within twelve months”",
            "“the heart seemed to go out of the house”"], marques=["1", "2"], x=150, y=210, w=980),
        "fates": dict(type="liste", titre="The sisters who stayed", items=[
            "Maggie: “pretended to believe that nothing had changed”",
            "Chris: the knitting factory, “and hated every day of it”",
            "Kate: tutor to the family of Austin Morgan"], marques=["M", "C", "K"], x=150, y=180, w=980),
        "ironie": dict(type="liste", titre="Irony", cles=["irony"], items=[
            "The factory ruined Agnes and Rose",
            "Chris works in it for the rest of her life",
            "Kate teaches the children of the man she loved"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_escape": dict(type="cit", a="Michael", o="p. 74", x=170, y=200, w=940),
        "fuite": dict(type="note", cles=["Emigration", "selfish"], terme="Leaving Ballybeg",
                      t="Michael “happy to escape”, like Agnes, Rose, Gerry, Jack.",
                      etape="Emigration, and the narrator's guilt.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. la musique du souvenir
    dict(id="musique", chap="A dream music", fond="nuit", humeur="mystere",
         retenir="The music comes from memory, not the radio; the play repeats its first sentence; atmosphere beats incident.", beats=[
        "{son}Now, very softly, music fades in. The class text names it: It is Time to Say Goodnight. "
        "{son.1}And it is not from the radio speaker. Marconi is silent: this music comes from memory.",
        "{-son}{sway}Everybody begins to sway, very slightly, from side to side… even the grinning kites. "
        "{sway.1}The movement is so small, says Friel, that we cannot be sure if it is happening, or if we imagine it.",
        "Then Michael says a sentence we already know.",
        "{-sway}",
        ("C", "And so, when I cast my mind back to that summer of 1936, different kinds of memories offer themselves to me.",
         "c_cast"),
        "{-c_cast}{cercle}It is the very first sentence of the play, almost word for word. "
        "{cercle.1}Page one, and now page seventy-four. The play comes full circle.",
        "{-cercle}{une}But one memory, he says, visits him most often. And it owes nothing to fact.",
        "{-une}",
        ("C", "In that memory atmosphere is more real than incident and everything is simultaneously actual and illusory.",
         "c_atmo"),
        "{-c_atmo}{atmo}Atmosphere: the feeling of a moment. Incident: what actually happens. "
        "For Michael, the feeling is more real than the facts. Facts get three flat sentences; the feeling gets his finest prose.",
        "{-atmo}{para}Look at the pairs. {para.1}Actual and illusory. {para.2}A music heard and imagined. "
        "{para.3}Itself and its own echo. {para.4}An afternoon bewitched, maybe haunted. "
        "Each pair holds two things at once, like Kate's dance in part five: simultaneously controlled and frantic.",
    ], vis={
        "son": dict(type="note", cles=["memory", "radio"], terme="Stage direction · p. 74",
                    t="“It is Time to Say Goodnight”, “not from the radio speaker”.",
                    etape="Marconi is silent: the music comes from memory.", x=170, y=200, w=940),
        "sway": dict(type="mot", t="everybody sways", g="“even the grinning kites” · happening, or imagined?", y=250, taille=88),
        "c_cast": dict(type="cit", a="Michael", o="p. 74 (and p. 1)", x=170, y=190, w=940),
        "cercle": dict(type="cols", g="Page 1", gq="“When I cast my mind back to that summer of 1936 …”", d="Page 74",
                       dq="“And so, when I cast my mind back …”", vs="=", repere="full circle"),
        "une": dict(type="mot", t="one memory", g="“that visits me most often” · it “owes nothing to fact”", y=250, taille=88),
        "c_atmo": dict(type="cit", a="Michael", o="p. 74", x=170, y=200, w=940),
        "atmo": dict(type="cols", g="Atmosphere", gq="the feeling of a moment", d="Incident",
                     dq="what actually happens", vs=">", repere="memory over fact"),
        "para": dict(type="liste", titre="Paradoxes of memory · pages 74 – 75", cles=["and"], items=[
            "“actual and illusory”",
            "“both heard and imagined”",
            "“both itself and its own echo”",
            "“bewitched, maybe haunted”"], marques=["1", "2", "3", "4"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ IV. danser sans les mots
    dict(id="danse", chap="Words no longer necessary", fond="aube", humeur="lumiere",
         retenir="The last words: dance as a “wordless ceremony” where “words were no longer necessary”.", beats=[
        "{flot}In that memory, everybody seems to be floating on the music, {flot.1}moving languorously, in complete isolation. "
        "{flot.2}Together, and yet each one alone. "
        "{flot.3}Dancing with eyes half closed, because to open them would break the spell.",
        "Then the sentences start with the same words, again and again.",
        "{-flot}",
        ("C", "Dancing as if language had surrendered to movement – as if this ritual, this wordless ceremony, was now the way to speak",
         "c_surr"),
        "{-c_surr}{rite}{rite.1}Language surrenders, like an army laying down its arms. "
        "{rite.2}The dance becomes a ritual, a wordless ceremony. "
        "{rite.3}A way to whisper private and sacred things, to be in touch with some otherness.",
        "{-rite}{anaph}Dancing as if, dancing as if: this repetition is called anaphora. "
        "The sentences rise like music, to the last words.",
        "{-anaph}",
        ("C", "Dancing as if language no longer existed because words were no longer necessary …", "c_words"),
        "{-c_words}{fin}The sentence does not end: three dots. "
        "{fin.1}Slowly bring up the music. Slowly bring down the lights. The end.",
    ], vis={
        "flot": dict(type="liste", titre="Floating · page 75", items=[
            "“moving rhythmically, languorously”",
            "“in complete isolation”",
            "“with eyes half closed”: not to “break the spell”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_surr": dict(type="cit", a="Michael", o="p. 75", x=170, y=180, w=940),
        "rite": dict(type="liste", titre="A wordless ceremony", cles=["ritual", "sacred"], items=[
            "language “surrendered to movement”",
            "“this ritual, this wordless ceremony”",
            "“private and sacred things” · “some otherness”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "anaph": dict(type="mot", t="Dancing as if …", g="anaphora: four sentences, one beginning", y=250, taille=88),
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
            "Everyone is now sitting in the kitchen"], ok=0, voir="pos",
         ex="On page 1 Rose sits on the garden seat with Gerry and Agnes is upstage; on page 74 it is the reverse: the two sisters who leave have swapped."),
    dict(q="Where does the final music come from?",
         r=["Not from the radio: it comes from memory", "From Marconi, finally repaired", "From Gerry's gramophone",
            "From the harvest dance in the village"], ok=0, voir="son",
         ex="The stage direction says “not from the radio speaker”: the music now belongs to Michael's memory."),
    dict(q="Which sentence does Michael repeat from the very start of the play?",
         r=["“When I cast my mind back to that summer of 1936 …”", "“As it turned out – to die”",
            "“A widening breach between what seemed to be and what was”", "“Ceremony! That's the word!”"], ok=0, voir="c_cast",
         ex="The first sentence of page 1 comes back on page 74: the play comes full circle."),
    dict(q="“Atmosphere is more real than incident” means that…",
         r=["the feeling of the memory matters more than the facts", "the weather was very hot in 1936",
            "Michael invents events that never happened", "the plot of the play is very dramatic"], ok=0, voir="c_atmo",
         ex="Incident is what happens; atmosphere is the feeling. The facts take three flat sentences, the feeling gets Michael's best prose."),
    dict(q="What does Michael do when his “time came to go away”?",
         r=["He was “happy to escape”, “in the selfish way of young men”", "He stayed to look after Kate",
            "He joined Gerry in Spain", "He became a priest like Jack"], ok=0, voir="c_escape",
         ex="Michael emigrates too, like Agnes and Rose; the word “selfish” shows the narrator's guilt."),
    dict(q="What are the very last words Michael speaks?",
         r=["“words were no longer necessary …”", "“It is time to say goodnight”", "“I was happy to escape”",
            "“the heart seemed to go out of the house”"], ok=0, voir="c_words",
         ex="“Dancing as if language no longer existed because words were no longer necessary …”: the sentence trails off and the music takes over."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
