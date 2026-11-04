"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 2 : un après-midi d'août (PDF de travail, p. 2-9).

Même format que la partie 1 (voir dal_1.py) : ce qui se passe, citations clés lues et expliquées, analyse en fin de partie.
Citations courtes, vérifiées sur les images des pages ; le contexte extérieur au texte est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-2"
NOTION = "Dancing at Lughnasa"
NUM = 2
TITRE = "An August afternoon"
SUIVANT = "Part 3 · The harvest dance"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Abyssinia": "Abby-sinnia", "Valera": "Va-lair-a"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{tab_don}{q1}The light changes. It is a warm summer afternoon, and four sisters are working in silence. "
        "Nothing dramatic is happening… and that is exactly the point.",
        "{-q1}In this part, we watch an ordinary afternoon in the Mundy kitchen, and we learn to read everything "
        "that lies under the surface: desire, shame, money, and a child who isn't really there.",
        ("P", 0.3),
        "{-tab_don}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.1, .45, .5], a=[1.25, .6, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Nothing dramatic is happening… and that is the point."),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 2", t="An August afternoon",
                      sous="The kitchen, the songs, the boy, the leper priest · pages 2 – 9"),
    }),

    # ------------------------------------------------------------------ I. le travail et le miroir
    dict(id="miroir", chap="Work and the mirror", fond="aube", humeur="lumiere",
         retenir="Small talk, big subtext: desire and Kate's authority are present even when Kate is not.", beats=[
        "{taches}Look first at the stage directions. Michael, Kate, Gerry and Jack go off. The others busy themselves. "
        "{taches.1}Maggie makes a mash for the hens. {taches.2}Agnes knits gloves. {taches.3}Rose carries turf for the fire. "
        "{taches.4}Chris irons at the kitchen table. And they all work in silence.",
        "Then Chris stops, goes to the tiny mirror on the wall, and looks at her face.",
        "{-taches}",
        ("C", "When are we going to get a decent mirror to see ourselves in?", "c_mirror", {"voix": "F"}),
        "{-c_mirror}{mirror}It is a cracked mirror, and Maggie won't throw it away: she broke it, and the only way to avoid "
        "seven years' bad luck is to keep using it. Superstition, already. "
        "And notice the image: these women cannot see themselves properly. Their lives are reflected back to them broken.",
        "Then Chris says she might start wearing lipstick. Maggie teases her.",
        "{-mirror}",
        ("C", "Steady on, girl. Today it's lipstick; tomorrow it's the gin bottle.", "c_lip", {"voix": "F"}),
        "And Agnes adds a line in someone else's voice.",
        "{-c_lip}",
        ("C", "As long as Kate's not around. 'Do you want to make a pagan of yourself?'", "c_pagan", {"voix": "F"}),
        "{-c_pagan}{kate}Kate is not even on stage, and she is already in the room. Agnes imitates her, word for word. "
        "Lipstick is enough to be called pagan in this house. That tells you how tight the rules are, "
        "and how much desire the sisters have to hide.",
        "{-kate}{surplice}And watch the last gesture: Chris holds up a surplice, a priest's white vestment she is ironing, "
        "and jokes that it would make a nice dress… then adds: God forgive me. "
        "Even a joke about clothes runs straight into religion.",
    ], vis={
        "taches": dict(type="liste", titre="They all work in silence · p. 2", items=[
            "Maggie: a mash for the hens",
            "Agnes: knits gloves",
            "Rose: carries turf for the fire",
            "Chris: irons at the kitchen table"], marques=["M", "A", "R", "C"], x=150, y=180, w=980),
        "c_mirror": dict(type="cit", a="Chris", o="p. 2", x=170, y=200, w=940),
        "mirror": dict(type="note", cles=["cracked", "broken"], terme="Symbol · the cracked mirror",
                       t="Kept out of superstition, it can only show the sisters a broken reflection of themselves.",
                       etape="How do these women see their own lives?", x=170, y=200, w=940),
        "c_lip": dict(type="cit", a="Maggie", o="p. 2", x=170, y=200, w=940),
        "c_pagan": dict(type="cit", a="Agnes, imitating Kate", o="p. 2", x=170, y=200, w=940),
        "kate": dict(type="def", cles=["absent", "pagan"], terme="Kate's voice",
                     t="Absent from the stage, but present in Agnes's mouth: even lipstick is “pagan”.",
                     etape="Desire has to hide under the rules of a Catholic house.", x=170, y=200, w=940),
        "surplice": dict(type="mot", t="God forgive me…", g="a priest's surplice imagined as a dress (p. 3)", y=250, taille=84),
    }),

    # ------------------------------------------------------------------ II. chansons et secrets
    dict(id="chansons", chap="Songs and secrets", fond="nuit", humeur="tension",
         retenir="Comic songs carry the outside world; Rose's love for a married man shows the women's longing, and its risk.", beats=[
        "{tab_rad}{songs}Suddenly, Rose bursts into song. {songs.1}Will you come to Abyssinia, will you come? "
        "Mussolini will be there with his airplanes in the air.",
        "A detail from outside the text: Italy had invaded Abyssinia, today's Ethiopia, the year before, in 1935. "
        "So a real war arrives in this kitchen… as a comic song. "
        "{songs.2}Maggie answers with another one, about voting for De Valera, the Irish leader of the time.",
        "{-songs}{-tab_rad}{radio}Rose wants the radio on, but Chris says the battery is dead. "
        "Three seconds of music, then nothing. The wireless works only when it wants: remember that.",
        "{-radio}{lough}Then a secret comes out. Rose says she may meet someone at the pictures, "
        "and that he wants to take her up to the back hills, to Lough Anna, where his father has a boat. "
        "{-lough}{danny}Chris guesses: Danny Bradley. {danny.1}A scut, she says, {danny.2}a married man with three young children. "
        "{danny.3}Rose insists his wife has left him and gone to England.",
        "{-danny}{charm}Rose shows them what he gave her: a little silver charm, pinned to her jumper, "
        "right beside her miraculous medal. A love token next to a holy medal. Pagan and Christian, side by side, on one woman's heart.",
        "{-charm}",
        ("C", "I love him, Aggie.", "c_love", {"voix": "F"}),
        "{-charm}{-c_love}{bastard}And Chris answers, softly, with one word: bastard. "
        "Rose is on the point of tears. Silence.",
        "{-bastard}{tango}Who breaks it? Maggie. She grabs her hen bucket as a dancing partner and does a wild, exaggerated tango "
        "across the floor, singing The Isle of Capri, then calls her hens: tchook, tchook, tchook. "
        "This is Maggie's role in the family: when the pain gets too close, she turns it into a joke, or a dance.",
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "songs": dict(type="liste", titre="Two comic songs · pp. 3 – 4", items=[
            "Rose: “Will you come to Abyssinia…”: Mussolini's war",
            "Maggie: “Will you vote for De Valera…”: Irish politics"], marques=["♪", "♪"], x=150, y=200, w=980),
        "radio": dict(type="mot", t="three seconds of music…", g="then silence: the wireless works only when it wants (p. 3)", y=250, taille=80),
        "lough": dict(type="mot", t="Lough Anna", g="“up to the back hills”: his father has a boat there (p. 5)", y=250, taille=96),
        "danny": dict(type="liste", titre="Danny Bradley · p. 5", items=[
            "“a scut”, says Chris",
            "“a married man with three young children”",
            "Rose: his wife has left for England"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "charm": dict(type="cols", g="The silver charm", gq="a love token from Danny", d="The miraculous medal",
                      dq="a Catholic holy medal", vs="+", repere="pagan / Christian, side by side"),
        "c_love": dict(type="cit", a="Rose", o="p. 6", x=170, y=470, w=940),
        "bastard": dict(type="mot", t="“Bastard.”", g="Chris, softly · Rose on the point of tears (p. 6)", y=250, taille=96),
        "tango": dict(type="note", cles=["joke", "dance"], terme="Maggie · p. 6",
                      t="A tango with the hen bucket, then the hens: she turns pain into comedy.",
                      etape="Dance as a way out of what cannot be said.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. l'enfant invisible
    dict(id="enfant", chap="The boy who isn't there", fond="aube", humeur="mystere",
         retenir="The boy Michael is invisible: the adult narrator speaks his lines. Memory performs the past.", beats=[
        "{conv}Now comes one of the strangest choices in the play. Friel writes it in a stage direction. "
        "{conv.1}Michael the boy is imaginary. {conv.2}Nobody on stage sees a child. {conv.3}When the sisters talk to the boy, "
        "the adult Michael, standing to the side, answers them, in his ordinary narrator's voice.",
        "{-conv}{tab_kit}So Maggie bends over kites that are not there, and a grown man answers for the child he used to be. "
        "She plays riddles with him: what goes round the house and sits in the corner? A broom. "
        "He fools her with a fake rat, and she screams.",
        "{-tab_kit}{effet}Why do this? Because the boy only exists in memory. {effet.1}We never see the child, only the adult remembering him. "
        "{effet.2}And it means the narrator is inside every scene: he is not just telling the story, he is replaying it.",
        "{-effet}{kites}Notice the kites, too. The boy is making two of them, and Maggie bets him a penny they will never leave the ground. "
        "Keep them in mind: they will come back at the very end of the play.",
    ], vis={
        "conv": dict(type="liste", titre="Stage direction · p. 6", items=[
            "The boy Michael is imaginary",
            "No one on stage sees a child",
            "Adult Michael speaks the boy's lines"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "tab_kit": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.2, .3, .4], a=[1.35, .4, .45],
                        legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "effet": dict(type="cols", g="We never see the child", gq="only the adult who remembers him", d="The narrator in every scene",
                      dq="he replays the past, he doesn't just tell it", vs="→", repere="memory play"),
        "kites": dict(type="mot", t="two kites", g="a motif to follow until the final scene (p. 7)", y=250, taille=96),
    }),

    # ------------------------------------------------------------------ IV. le prêtre des lépreux
    dict(id="pretre", chap="Our own leper priest", fond="nuit", humeur="calme",
         retenir="Jack's fame gives the family status; it also covers the “shame” of Chris's child.", beats=[
        "{tab_kil}Then Michael speaks to us again. He explains why Jack's appearance shocked him: he expected "
        "the hero from a schoolboy's book.",
        "{photo}Once, he saw a photograph of Jack, radiant and splendid in his officer's uniform, a chaplain to the British forces "
        "in East Africa in 1917. {photo.1}But Kate snatched it away. {photo.2}She had been involved in the War of Independence against Britain, "
        "so Jack's time in the British army was never mentioned in that house.",
        "{-photo}{-tab_kil}{saint}To the sisters, Jack was a hero and a saint. They prayed for him every night, "
        "and saved sixpence here, a shilling there, to send him money. The local paper called him our own leper priest, "
        "and the whole of Donegal was proud of him. That gave the family a little status in the parish.",
        "And then, the most important sentence of this part.",
        "{-saint}",
        ("C", "it must have helped my aunts to bear the shame Mother brought on the household by having me – as it was called then – "
              "out of wedlock.", "c_shame"),
        "{-c_shame}{shame}The shame: that is the word the parish used for Chris's child, Michael himself. "
        "Notice the distance in as it was called then: the adult narrator quotes the judgement of 1936 without sharing it. "
        "And see the balance: Jack's holiness protects the family's reputation. "
        "So what happens if the saint comes home… changed? That is the question the rest of the play will answer.",
    ], vis={
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "photo": dict(type="liste", titre="The photograph · p. 9", items=[
            "Kate snatched it from the boy",
            "Kate had fought for Irish independence: Jack's British army past is never mentioned"],
            marques=["1", "2"], x=150, y=200, w=980),
        "saint": dict(type="mot", t="“our own leper priest”", g="Jack's fame gives the family status in the parish (p. 9)", y=250, taille=80),
        "c_shame": dict(type="cit", a="Michael", o="p. 9", x=170, y=200, w=940),
        "shame": dict(type="cols", g="Jack's fame", gq="“a hero and a saint”, status in the parish", d="Chris's child",
                      dq="“the shame”, born “out of wedlock”", vs="⚖", repere="reputation"),
    }),

    # ------------------------------------------------------------------ V. analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Subtext, the outside world in songs, the invisible boy, reputation: the house is held together by fragile balances.", beats=[
        "{a1}Time for the analysis. Four ideas to take from this afternoon. "
        "{a1.1}One: subtext. Almost nothing happens, but every small exchange carries something bigger: a cracked mirror, "
        "a lipstick, a surplice. This is Friel's Chekhovian method: the drama is under the surface, in what the characters do not say.",
        "{-a1}{a2}{a2.1}Two: desire under surveillance. Lipstick is pagan, Rose's love is for a married man, Chris has a child "
        "outside marriage. Each sister wants something, and Kate's rules, even when Kate is absent, keep watch.",
        "{-a2}{a3}{a3.1}Three: the outside world gets in, but only in fragments. A war in Abyssinia, an Irish election, "
        "all turned into comic songs; a radio that dies after three seconds. The world is changing, "
        "and the kitchen hears it only as noise and jokes.",
        "{-a3}{a4}{a4.1}Four: memory as theatre. The boy is invisible and the adult speaks his lines. "
        "And Michael's narration shows how the family's reputation rests on a balance: Jack's fame against Chris's shame. "
        "Remember the widening breach of part one: here you can see exactly where it will open.",
        "{-a4}{carte}For your essay, this part can support: {carte.1}the subtext and the Chekhovian method, "
        "{carte.2}desire and repression, {carte.3}the outside world, {carte.4}and memory with its stage conventions.",
    ], vis={
        "a1": dict(type="note", cles=["subtext", "surface"], terme="1 · Subtext",
                   t="Mirror, lipstick, surplice: small things that carry big tensions.",
                   etape="Chekhovian method: the drama is under the surface.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["desire", "rules"], terme="2 · Desire under surveillance",
                   t="Lipstick is “pagan”; Rose loves a married man; Chris's child is “the shame”.",
                   etape="Kate's rules keep watch, even when she is absent.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["fragments", "noise"], terme="3 · The outside world",
                   t="Abyssinia and De Valera as comic songs; a wireless that dies after three seconds.",
                   etape="Change reaches the kitchen only as noise and jokes.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["invisible", "balance"], terme="4 · Memory as theatre",
                   t="The invisible boy voiced by the adult; Jack's fame balancing Chris's “shame”.",
                   etape="Where the “widening breach” will open.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="AN AUGUST AFTERNOON", branches=[
            dict(t="Subtext", items=["the cracked mirror", "the surplice “dress”", "Chekhovian method"]),
            dict(t="Desire", items=["“make a pagan of yourself”", "Rose and Danny Bradley", "“out of wedlock”"]),
            dict(t="Outside world", items=["Abyssinia, De Valera", "the dying wireless"]),
            dict(t="Memory", items=["the invisible boy", "“our own leper priest”"])]),
    }),
]

QUIZ = [
    dict(q="Why does Maggie refuse to throw away the cracked mirror?",
         r=["She broke it, and using it avoids seven years' bad luck", "It belonged to their mother", "Kate forbids new mirrors",
            "They cannot afford a new one"], ok=0, voir="mirror",
         ex="Superstition: she broke it, so she must keep using it. Symbolically, the sisters only see a broken reflection of themselves."),
    dict(q="When Agnes says “Do you want to make a pagan of yourself?”, she is…",
         r=["imitating what Kate would say about lipstick", "quoting Father Jack", "insulting Rose", "reading from a novel"], ok=0,
         voir="c_pagan", ex="Kate is offstage, but her voice and her rules are present: even lipstick counts as pagan."),
    dict(q="What does Rose wear beside her miraculous medal?",
         r=["A silver charm given by Danny Bradley", "Jack's cross from Africa", "Her mother's ring", "A kite string"], ok=0,
         voir="charm", ex="A love token next to a holy medal: pagan and Christian side by side."),
    dict(q="How is the boy Michael shown on stage?",
         r=["He is imaginary: the adult narrator speaks his lines", "A child actor plays him", "He is a puppet",
            "He never speaks at all"], ok=0, voir="conv",
         ex="Stage direction p. 6: no child appears; adult Michael answers the sisters in his narrator's voice."),
    dict(q="Why was Jack's photograph in uniform never mentioned in the house?",
         r=["Kate had fought in the War of Independence against Britain", "Jack had deserted",
            "The photo was of another priest", "Maggie had broken the frame"], ok=0, voir="photo",
         ex="He had been a chaplain to the British forces; Kate had been involved in the War of Independence."),
    dict(q="According to Michael, what did Jack's fame help the aunts to bear?",
         r=["The shame of Chris's child born out of wedlock", "Their poverty", "Kate losing her job", "Rose's illness"], ok=0,
         voir="c_shame", ex="Jack's status as “our own leper priest” balanced the parish's judgement of Chris: a fragile balance."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); valve table radio, Museo della scienza e della "
    "tecnologia, Milan (CC BY-SA 4.0); troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
