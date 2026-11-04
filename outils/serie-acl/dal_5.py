"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 5 : la danse (PDF de travail, p. 22-25).

Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_5.
De la mise en marche de Marconi (« The Mason's Apron ») à l'arrivée annoncée par Maggie (« Look who's coming up the lane! »,
p. 25) : la longue didascalie de la danse, puis la gêne et la querelle (l'argent des gants, « two unpaid servants »).
Citations courtes, à fin d'analyse ; la didascalie n'est citée que par brèves expressions, le reste est résumé.
Ce qui ne vient pas du texte (Ginger Rogers, la marque Woodbine, le surplis) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-5"
NOTION = "Dancing at Lughnasa"
NUM = 5
TITRE = "The dance"
SUIVANT = "Part 6 · Gerry Evans"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "ceili": "kaylee", "Yaaaah": "Yaaah", "Ardstraw": "Ard-straw",
                 "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rad}{q1}A radio crackles into life. A fast Irish reel fills the kitchen. "
        "And five women who were ironing, knitting and baking a moment ago… start to dance.",
        "{-q1}{fameux}This is the most famous scene of Dancing at Lughnasa. Almost no words are spoken, "
        "and yet it tells us everything about the Mundy sisters.",
        "{-fameux}Part five: the dance, and the quarrel that follows it.",
        ("P", 0.3),
        "{-tab_rad}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Five sisters, one radio, and a dance nobody can stop."),
        "fameux": dict(type="mot", t="Almost no words", g="the most famous scene of the play", y=270, taille=88),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 5", t="The dance",
                      sous="Marconi, the reel, the quarrel · pages 22 – 25"),
    }),

    # ------------------------------------------------------------------ I. Marconi
    dict(id="marconi", chap="Marconi comes back", fond="aube", humeur="mystere",
         retenir="Chris switches on Marconi: “The Mason's Apron”, very fast, very heavy, raucous. Michael's “voodoo” is about to happen.", beats=[
        "{fenetre}Where are we? Maggie has just told the story of a dance at Ardstraw, years ago, and of a lost love. "
        "{fenetre.1}Now she stands motionless at the window, seeing nothing.",
        "{-fenetre}{tab_rad2}{mason}Chris connects the battery. {mason.1}She switches the set on and goes back to her ironing. "
        "{mason.2}The music is The Mason's Apron, played by a ceili band. {mason.3}Very fast, a very heavy beat, a raucous sound.",
        "{-mason}{voodoo}For ten seconds, the women go on working. Remember Michael's warning in the opening: "
        "Marconi's voodoo, turning kind, sensible women into shrieking strangers. {voodoo.1}We are about to watch it happen.",
    ], vis={
        "fenetre": dict(type="note", cles=["motionless", "nothing"], terme="Stage direction · p. 22",
                        t="Maggie stands motionless, staring out of the window, seeing nothing.",
                        etape="Her sadness comes just before her wildest moment.", x=170, y=200, w=940),
        "tab_rad2": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.2, .45, .5], a=[1.05, .5, .5],
                         legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "mason": dict(type="liste", titre="The music · p. 22", items=[
            "Chris switches on Marconi",
            "“The Mason's Apron”, played by a ceili band",
            "Very fast · very heavy beat · a raucous sound"], marques=["1", "2", "3"], x=150, y=190, w=980),
        "voodoo": dict(type="note", cles=["voodoo", "strangers"], terme="Remember · the opening, p. 2",
                       t="“Marconi's voodoo” transforms the sisters into “shrieking strangers”.",
                       etape="The prophecy of page 2 comes true on page 22.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. une par une
    dict(id="danseuses", chap="One by one", fond="nuit", humeur="tension",
         retenir="Maggie, Rose, Agnes, Chris (in Jack's surplice), then Kate: each sister joins the dance in her own way.", beats=[
        "{maggie}Maggie moves first. She turns round, her head cocked to the beat, breathing fast. Her face changes.",
        "{-maggie}",
        ("C", "a look of defiance, of aggression; a crude mask of happiness.", "c_mask"),
        "{-c_mask}{masque}A mask of happiness: not happiness itself. Her hands, covered with flour, pattern her face with a white mask. "
        "{!Yaaaah!}She lets out a wild Yaaaah! and dances, calling: Come on! {masque.1}A white-faced, frantic dervish.",
        "{-masque}{danse}{danse.1}Her sisters watch her. {danse.2}Then Rose flings away her knitting and grabs Maggie's hand, "
        "her Wellingtons pounding out their own erratic rhythm. "
        "{danse.3}Agnes joins them: of all the sisters, she moves most gracefully, most sensuously.",
        "{danse.4}Then Chris tosses Jack's surplice over her head and joins in. Kate cries out: Oh, Christina! "
        "But her protest is drowned. {danse.5}Kate watches with unease, with alarm… until she too leaps up, "
        "flings her head back, and lets out a loud Yaaaah!",
        "{-danse}{surplis}Two details. First, the surplice: outside the text, it is the white garment a priest wears for Mass. "
        "The sacred vestment becomes a carnival costume. That is sacrilege, and Kate knows it.",
        "{-surplis}{reel}Second, the reel, just before Kate leaps up. {reel.1}The four sisters meet, retreat, wheel round in a circle. "
        "{reel.2}But the moves are caricatured, the sound too loud, the beat too fast. "
        "{reel.3}Arms round each other's necks and waists: the familiar dance becomes grotesque.",
    ], vis={
        "maggie": dict(type="mot", t="Maggie first", g="head cocked to the beat, breathing deeply, rapidly · p. 22", y=260, taille=92),
        "c_mask": dict(type="cit", a="Stage direction", o="p. 22", x=170, y=200, w=940),
        "masque": dict(type="note", cles=["mask", "flour"], terme="Maggie · p. 22",
                       t="A mask of flour on her face, a wild “Yaaaah!”, “Come on! Come on!”",
                       etape="“a white-faced, frantic dervish”: joy as a performance.", x=170, y=200, w=940),
        "danse": dict(type="liste", titre="Who dances, and how", items=[
            "Maggie: a flour mask and a wild “Yaaaah!”",
            "Rose: Wellingtons pounding an erratic rhythm",
            "Agnes: the most graceful, the most sensuous",
            "Chris: Jack's surplice over her head",
            "Kate: last of all, the same “Yaaaah!”"], marques=["M", "R", "A", "C", "K"], x=150, y=120, w=980),
        "surplis": dict(type="def", cles=["sacred", "carnival"], terme="The surplice",
                        t="A priest's white vestment for Mass (outside the text). Here, Jack's sacred garment becomes a carnival costume.",
                        etape="Sacrilege: the Church turned upside down.", x=170, y=200, w=940),
        "reel": dict(type="liste", titre="A parodic reel · p. 23", items=[
            "They meet, retreat, wheel round in a circle",
            "Caricatured moves · too loud · too fast",
            "Arms round necks and waists: grotesque"], marques=["1", "2", "3"], x=150, y=190, w=980),
    }),

    # ------------------------------------------------------------------ III. Kate seule
    dict(id="kate", chap="Kate dances alone", fond="aube", humeur="tension",
         retenir="Kate dances alone and silent: “controlled and frantic”. Then silence, embarrassment, shame and defiance.", beats=[
        "{kate_mot}Now comes the most striking moment of the whole play.",
        "{-kate_mot}",
        ("C", "KATE dances alone, totally concentrated, totally private; a moment that is simultaneously controlled and frantic",
         "c_kate"),
        "{-c_kate}{seule}Kate, the guardian of order, dances most intensely of all. "
        "{seule.1}She weaves round the kitchen, out to the garden, round the summer seat, and back. "
        "{seule.2}It is out of character, Friel says, and ominous of some deep and true emotion. "
        "{seule.3}The others call and sing. Kate makes no sound.",
        "Then Friel tells us what the scene means.",
        "{-seule}",
        ("C", "there is a sense of order being consciously subverted, of the women consciously and crudely caricaturing themselves",
         "c_order"),
        "{-c_order}{subvert}To subvert order is to overturn it from the inside. Consciously, twice: "
        "the sisters know what they are doing. They mock their own respectable lives, close to near-hysteria.",
        "{-subvert}{silence}Then the music stops in mid-phrase. Lost in their noise, they keep dancing for a few seconds. "
        "{silence.1}Kate stops first. Rose is the last, dancing her graceless dance alone. "
        "{silence.2}Silence. Only gasping for breath, and static from the radio.",
        "{-silence}{honte}They avoid each other's eyes and half smile in embarrassment: "
        "slightly ashamed, and slightly defiant.",
    ], vis={
        "kate_mot": dict(type="mot", t="And Kate…", g="the most striking moment of the play", y=260, taille=96),
        "c_kate": dict(type="cit", a="Stage direction", o="p. 23", x=170, y=200, w=940),
        "seule": dict(type="liste", titre="Kate's dance · p. 23", items=[
            "Kitchen · garden · summer seat · kitchen",
            "“out of character”, yet “ominous of some deep and true emotion”",
            "The others call and sing: Kate makes no sound"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "c_order": dict(type="cit", a="Stage direction", o="p. 23", x=170, y=190, w=940),
        "subvert": dict(type="def", cles=["overturned", "consciously"], terme="To subvert",
                        t="To undermine an order from the inside: here, consciously, by mocking themselves.",
                        etape="Not a loss of control only: a deliberate revolt.", x=170, y=200, w=940),
        "silence": dict(type="liste", titre="When the music dies", items=[
            "Kate stops first · Rose stops last",
            "Silence: gasping, and static from the radio"], marques=["1", "2"], x=150, y=210, w=980),
        "honte": dict(type="cols", g="slightly ashamed", gq="they avoid each other's eyes", d="slightly defiant",
                      dq="they do not apologise", vs="+", repere="the aftermath · p. 23"),
    }),

    # ------------------------------------------------------------------ IV. la querelle
    dict(id="querelle", chap="The quarrel", fond="nuit", humeur="tension",
         retenir="Order returns through Kate's rebukes; then the money quarrel: “two unpaid servants”, “the Gander”.", beats=[
        "{set}Chris breaks the silence. She slaps the radio: Bloody useless set, that.",
        "{-set}",
        ("C", "No need for corner-boy language, Christina.", "c_corner", {"voix": "F"}),
        "{-c_corner}{ordre}Kate takes back control at once. {ordre.1}She corrects Chris's language. "
        "{ordre.2}She picks on Rose's Wellingtons. {ordre.3}And soon: Please take that surplice off. Have you no sense of propriety?",
        "{-ordre}{ginger}Maggie lights a cigarette: this Ginger Rogers has seen better days. "
        "Outside the text, Ginger Rogers was the Hollywood dancing star of the thirties.",
        "{-ginger}",
        ("C", "Wonderful Wild Woodbine. Next best thing to a wonderful, wild man.", "c_woodbine", {"voix": "F"}),
        "{-c_woodbine}{woodbine}Woodbine, outside the text, was a cheap cigarette brand. The joke says what the dance said: "
        "desire, and the absence of men.",
        "{-woodbine}{michael}Wash your face, says Kate. Yes, miss, answers Maggie, like a pupil. "
        "And Michael has gone from the garden. Chris snaps: Just leave him alone for once.",
        "{-michael}{argent}Then the real quarrel. {argent.1}Kate turns on Agnes: will she buy a new radio out of her glove money, "
        "which barely clothes her and Rose? {argent.2}Agnes answers: This isn't your classroom, Kate. Every meal, every stitch of clothes, the bed…",
        "{-argent}",
        ("C", "What you have here, Kate, are two unpaid servants.", "c_servants", {"voix": "F"}),
        "{-c_servants}{gander}And Rose adds her own blow: Kate's nickname at school is the Gander!",
        "{-gander}{lane}At that moment, Maggie runs in: Look who's coming up the lane! Who it is, we will see in part six.",
    ], vis={
        "set": dict(type="mot", t="“Bloody useless set”", g="Chris swears at Marconi · p. 23", y=260, taille=80),
        "c_corner": dict(type="cit", a="Kate", o="p. 23", x=170, y=220, w=940),
        "ordre": dict(type="liste", titre="Kate restores order", items=[
            "“corner-boy language”",
            "“Are Wellingtons absolutely necessary…?”",
            "“Please take that surplice off”"], marques=["1", "2", "3"], x=150, y=190, w=980),
        "ginger": dict(type="note", cles=["Ginger", "Rogers"], terme="Maggie · p. 24",
                       t="“this Ginger Rogers has seen better days”",
                       etape="Outside the text: the Hollywood dancing star of the 1930s.", x=170, y=200, w=940),
        "c_woodbine": dict(type="cit", a="Maggie", o="p. 24", x=170, y=210, w=940),
        "woodbine": dict(type="note", cles=["desire", "men"], terme="A joke that tells the truth",
                         t="Cheap cigarettes (outside the text) as a substitute for “a wonderful, wild man”.",
                         etape="Desire, and the absence of men.", x=170, y=200, w=940),
        "michael": dict(type="note", cles=["miss", "gone"], terme="Meanwhile · p. 24",
                        t="“Yes, miss.” Maggie answers Kate like a pupil. And Michael has gone from the garden.",
                        etape="The house is tense: everyone snaps at everyone.", x=170, y=200, w=940),
        "argent": dict(type="cols", g="Kate", gq="“your glove money”: barely enough to clothe them", d="Agnes",
                       dq="“This isn't your classroom, Kate.”", vs="≠", repere="money and power · p. 25"),
        "c_servants": dict(type="cit", a="Agnes", o="p. 25", x=170, y=220, w=940),
        "gander": dict(type="note", cles=["Gander"], terme="Rose · p. 25",
                       t="“The Gander! Everybody calls you the Gander!”",
                       etape="Kate's authority, mocked even at school.", x=170, y=200, w=940),
        "lane": dict(type="mot", t="“Look who's coming up the lane!”", g="Maggie runs in · p. 25", y=250, taille=72),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="A language beyond words, pagan against Christian, order subverted, joy followed by conflict.", beats=[
        "{a1}Now the analysis. Four ideas for your essay. "
        "{a1.1}One: a language beyond words. The scene exists almost only as a stage direction: this is non-verbal theatre. "
        "The sisters say with their bodies what they can never say aloud: frustration, desire, anger. "
        "And Kate, who controls every word, dances in silence. At the very end, Michael will remember dancing "
        "as if language had surrendered to movement. This is where we first see it.",
        "{-a1}{a2}{a2.1}Two: pagan against Christian. At Lughnasa, the dance is a wild, almost Dionysian release. "
        "The surplice turns the Church into a costume. And Kate, the guardian of Catholic order, dances most fiercely of all.",
        "{-a2}{a3}{a3.1}Three: order subverted, then restored. The revolt is self-mocking: parody, caricature. "
        "It is brief. Then come embarrassment and Kate's rebukes. A catharsis, a release of feelings, but no escape.",
        "{-a3}{a4}{a4.1}Four: juxtaposition. Right after the joy comes the quarrel: money, work, power. "
        "Two unpaid servants, the Gander. The family is cracking, as Michael feared.",
        "{-a4}{carte}So, in an essay, this scene can support: {carte.1}dance as release and language, "
        "{carte.2}pagan against Christian, {carte.3}order and subversion, {carte.4}and the sisters' frustrated lives.",
    ], vis={
        "a1": dict(type="note", cles=["beyond", "silence"], terme="1 · A language beyond words",
                   t="Non-verbal theatre: the stage direction is the text; the bodies speak. Kate dances in silence.",
                   etape="Final monologue: “as if language had surrendered to movement”.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["pagan", "surplice"], terme="2 · Pagan / Christian",
                   t="A Dionysian release at Lughnasa; the surplice as a costume; Kate's own “Yaaaah!”.",
                   etape="The pagan breaks into the Catholic house.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["subverted", "restored"], terme="3 · Order subverted, then restored",
                   t="“order being consciously subverted”: parody, caricature, near-hysteria… then embarrassment.",
                   etape="A brief catharsis, not an escape.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["quarrel", "money"], terme="4 · Juxtaposition",
                   t="The dance, then the quarrel: “two unpaid servants”, “the Gander”.",
                   etape="Joy hides the tensions only for a moment.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE DANCE", branches=[
            dict(t="Release", items=["non-verbal theatre", "“Yaaaah!”", "Kate's silence"]),
            dict(t="Pagan / Christian", items=["Lughnasa", "the surplice", "“Marconi's voodoo”"]),
            dict(t="Order", items=["“consciously subverted”", "parody, caricature", "embarrassment"]),
            dict(t="Frustrated lives", items=["“wild man”", "“two unpaid servants”", "“the Gander”"])]),
    }),
]

QUIZ = [
    dict(q="What music comes out of Marconi?",
         r=["“The Mason's Apron”, an Irish reel played by a ceili band", "A slow Irish ballad", "Cole Porter's “Anything Goes”",
            "Church music from Dublin"], ok=0, voir="mason",
         ex="Friel describes it as very fast, with a very heavy beat and a raucous sound: the beat first, then the melody."),
    dict(q="What does Maggie do to her face before she dances?",
         r=["She patterns it with flour, like a mask", "She covers it with her apron", "She paints it with ink",
            "She hides it in her hands and cries"], ok=0, voir="masque",
         ex="Her hands are covered with flour: “a crude mask of happiness”, then a “white-faced, frantic dervish”."),
    dict(q="Why is Chris dancing with Jack's surplice over her head so shocking?",
         r=["A priest's sacred vestment becomes a carnival costume", "Because it belongs to Gerry", "Because it is Kate's best dress",
            "Because it is dirty"], ok=0, voir="surplis",
         ex="Kate cries “Oh, Christina!”: the Church's garment is turned into a costume in a pagan dance, a kind of sacrilege."),
    dict(q="How does Kate dance?",
         r=["Alone, silent, “simultaneously controlled and frantic”", "With Rose, laughing", "She refuses to dance",
            "Holding Agnes by the waist"], ok=0, voir="c_kate",
         ex="She dances “totally private”, out of character; while the others call and sing, she “makes no sound”."),
    dict(q="According to the stage direction, the dance gives “a sense of order being…”",
         r=["consciously subverted", "slowly restored", "politely respected", "secretly rewritten"], ok=0, voir="c_order",
         ex="The sisters “consciously and crudely” caricature themselves: a deliberate revolt, close to “near-hysteria”."),
    dict(q="What does Agnes mean by “two unpaid servants”?",
         r=["She and Rose do all the housework without being thanked or paid", "Kate employs two maids",
            "Rose and Michael work for Gerry", "The priests of Ryanga"], ok=0, voir="c_servants",
         ex="Kate attacks the “glove money”; Agnes replies with all the meals, clothes, shoes and beds she and Rose take care of."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
