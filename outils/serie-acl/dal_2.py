"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 2 : un après-midi d'août (PDF de travail, p. 2-9).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés sur le plateau) :
l'après-midi est joué pas à pas d'après les didascalies (visuel jeu) : les tâches en silence, le miroir, les chansons
(« Abyssinia », « De Valera »), les trois secondes des « British Grenadiers » sur Marconi, le secret de Rose
(Danny Bradley, le charme et la médaille), le tango de Maggie, puis la convention de l'enfant invisible (p. 6 : le garçon
n'est jamais joué, Michael adulte dit ses répliques ; ici une silhouette en pointillé près des cerfs-volants) et le
monologue de Michael sur Jack (p. 9). Les répliques courtes s'affichent en bulles et sont lues par les voix des
personnages. Puis cinq répliques expliquées et l'analyse.

Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_2.
Citations courtes, vérifiées sur les images des pages ; le contexte extérieur au texte est dit comme tel.
Coquilles du PDF non reproduites (p. 3 : « wouldn't it?.. » ; p. 4 : « HE's »).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-2"
NOTION = "Dancing at Lughnasa"
NUM = 2
TITRE = "An August afternoon"
SUIVANT = "Part 3 · The harvest dance"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Abyssinia": "Abby-sinnia", "Valera": "Va-lair-a",
                 "Tchook": "Chook", "tchook": "chook"}

PERSOS = ["Maggie", "Agnes", "Rose", "Chris", "Michael"]
MICHAEL = [1000, 552]          # « downstage left » (p. 1), « stands L » (p. 6) : au bord du plateau, à droite vu de la salle
FOURNEAU = [240, 262]          # « the large box beside the range » (p. 2)
MIROIR = [378, 234]            # « the tiny mirror on the wall » (p. 2)
PATEE = [482, 352]             # Maggie prépare la pâtée des poules (p. 2) : lieu non précisé par le texte
GARCON = [780, 460]            # l'enfant imaginaire, aux cerfs-volants (p. 4 et 6) ; même place que dans les parties 3 et 4
# où chacune travaille quand Maggie sort (p. 6)
TACHES = dict(pos={"Chris": "table", "Agnes": "tricot_a", "Rose": FOURNEAU, "Maggie": PATEE},
              act={"Chris": "repasse", "Agnes": "tricote", "Rose": "debout", "Maggie": "range"})

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

    # ------------------------------------------------------------------ I. le travail et le miroir (p. 2-3)
    dict(id="miroir", chap="Work and the mirror", fond="nuit", humeur="lumiere", beats=[
        "{jeu1}Page two. The four sisters who stayed on stage busy themselves with their tasks. "
        "{jeu1.1}Maggie makes a mash for the hens, Agnes knits gloves, Chris irons, "
        "{jeu1.2}and Rose empties a basket of turf into the box beside the range. They all work in silence.",
        "{jeu1.3}Then Chris goes to the tiny mirror on the wall.",
        ("C", "When are we going to get a decent mirror to see ourselves in?", "jeu1.4", {"voix": "F"}),
        "{jeu1.5}It is cracked. But Maggie broke it, and:",
        ("C", "the only way to avoid seven years bad luck is to keep on using it.", "jeu1.6", {"voix": "F"}),
        "A cracked mirror: they cannot see themselves properly. {jeu1.7}Then Chris thinks she might start wearing lipstick.",
        ("C", "Steady on, girl. Today it's lipstick; tomorrow it's the gin bottle.", "jeu1.8", {"voix": "F"}),
        ("C", "As long as Kate's not around. 'Do you want to make a pagan of yourself?'", "jeu1.9", {"voix": "F"}),
        "{jeu1.10}Chris goes back to her ironing, and holds up a surplice: a priest's white vestment.",
        ("C", "Make a nice dress that, wouldn't it? … God forgive me…", "jeu1.11", {"voix": "F"}),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Maggie": "fenetre", "Chris": "porte", "Rose": "banc_g", "Agnes": [925, 238]},
                 act={"Maggie": "fige", "Chris": "fige", "Rose": "assis", "Agnes": "fige"}, cam="tout",
                 note="“The kitchen and garden are now lit as for a warm summer afternoon.” (p. 2)"),
            dict(pos={"Maggie": PATEE, "Chris": "table"}, act={"Maggie": "range", "Chris": "repasse", "Rose": "debout"},
                 chemin={"Agnes": [[925, 238], "porte", "tricot_a"], "Rose": ["banc_g", "porte", FOURNEAU]},
                 chemin_duree=6, tient={"Rose": "sac"}, note="Maggie: a mash for hens. Agnes knits gloves. Chris irons."),
            dict(pos={"Agnes": "tricot_a", "Rose": FOURNEAU}, act={"Agnes": "tricote", "Rose": "range"}, cam="cuisine",
                 note="Rose empties a basket of turf into the box beside the range. “They all work in silence.”"),
            dict(pos={"Chris": MIROIR}, act={"Chris": "debout", "Rose": "debout"}, tient={"Rose": None},
                 note="Chris “goes to the tiny mirror on the wall and scrutinizes her face”"),
            dict(dit=["Chris", "When are we going to get a decent mirror to see ourselves in?"]),
            dict(note="“I'm going to throw this aul cracked thing out.” · Maggie: “I'm the one that broke it…”"),
            dict(dit=["Maggie", "…the only way to avoid seven years bad luck is to keep on using it."]),
            dict(note="“I think I just might start wearing lipstick.”"),
            dict(dit=["Maggie", "Steady on, girl. Today it's lipstick; tomorrow it's the gin bottle."]),
            dict(dit=["Agnes", "As long as Kate's not around. 'Do you want to make a pagan of yourself?'"]),
            dict(pos={"Chris": "table"}, act={"Chris": "repasse"}, note="She goes back to her ironing. “She holds up a surplice.”"),
            dict(dit=["Chris", "Make a nice dress that, wouldn't it? … God forgive me…"]),
        ]),
    }),

    # ------------------------------------------------------------------ II. chansons et Marconi (p. 3-4)
    dict(id="chansons", chap="Songs and the wireless", fond="nuit", humeur="lumiere", beats=[
        "{jeu2}Page three. Nobody speaks. Then, suddenly, Rose bursts into raucous song.",
        ("C", "Will you come to Abyssinia, will you come? Bring your own cup and saucer and a bun…", "jeu2.1", {"voix": "F"}),
        "{jeu2.2}She dances a gauche, graceless shuffle.",
        ("C", "Mussolini will be there with his airplanes in the air,", "jeu2.3", {"voix": "F"}),
        "{jeu2.4}Maggie, trying to light a very short cigarette butt, hitches her own skirt even higher than Rose's, "
        "and does a similar shuffle.",
        ("C", "A right pair of pagans, the two of you.", "jeu2.5", {"voix": "F"}),
        "{jeu2.6}Rose switches Marconi on: a sudden, loud, three-second blast of The British Grenadiers… "
        "{jeu2.7}and the music suddenly dies. The battery is dead.",
        "{jeu2.8}Is Abyssinia in Africa, Rose asks. Is that where Father Jack was?",
        ("C", "Jack was in Uganda, Rosie. That's a different part of Africa. You know that.", "jeu2.9", {"voix": "F"}),
        "{jeu2.10}Then Maggie catches her hand, and sings softly into her ear, to the same melody:",
        ("C", "Will you vote for De Valera, will you vote?", "jeu2.11", {"voix": "F"}),
        "{jeu2.12}And the two of them dance the last line together.",
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(**TACHES, cam="cuisine", note="“Work continues. Nobody speaks.” (p. 3)"),
            dict(dit=["Rose", "Will you come to Abyssinia, will you come? Bring your own cup and saucer and a bun…"]),
            dict(act={"Rose": "danse_lourde"}, note="“a gauche, graceless shuffle that defies the rhythm of the song”"),
            dict(dit=["Rose", "Mussolini will be there with his airplanes in the air,"]),
            dict(act={"Maggie": "danse_lourde"}, tient={"Maggie": "cigarette"},
                 note="Maggie hitches her skirt “even higher than Rose's” and does a similar shuffle."),
            dict(dit=["Agnes", "A right pair of pagans, the two of you."]),
            dict(pos={"Rose": "radio"}, act={"Maggie": "debout", "Rose": "debout"}, tient={"Maggie": None}, radio=True,
                 note="“a sudden, loud three-second blast of ‘The British Grenadiers’”"),
            dict(radio=False, note="“and the music suddenly dies” · “Told you.”"),
            dict(note="“Is Abyssinia in Africa, Aggie?” … “But that's not where Father Jack was, is it?” (pp. 3 – 4)"),
            dict(dit=["Agnes", "Jack was in Uganda, Rosie. That's a different part of Africa. You know that."]),
            dict(pos={"Maggie": [418, 250]}, note="“MAGGIE catches her hand and sings softly into her ear”"),
            dict(dit=["Maggie", "Will you vote for De Valera, will you vote?"]),
            dict(act={"Maggie": "danse_lourde", "Rose": "danse_lourde"}, note="They dance as they sing the final line of the song."),
        ]),
    }),

    # ------------------------------------------------------------------ III. le secret de Rose (p. 4-6)
    dict(id="secret", chap="Rose's secret", fond="nuit", humeur="tension", beats=[
        "{jeu3}Back to work. Agnes looks out of the window, {jeu3.1}on to the garden.",
        ("C", "What's that son of yours at out there?", "jeu3.2", {"voix": "F"}),
        "{jeu3.3}The boy is making something that looks like a kite. Agnes taps on the window and blows a kiss "
        "to the imaginary child. {jeu3.4}Then she goes back to her seat.",
        "{jeu3.5}Page five. Rose may go to the pictures next Saturday, and meet somebody there.",
        ("C", "And he wants to bring me up to the back hills next Sunday – up to Lough Anna.", "jeu3.6", {"voix": "F"}),
        ("C", "Danny Bradley is a scut, Rose.", "jeu3.7", {"voix": "F"}),
        ("C", "He's a married man with three young children.", "jeu3.8", {"voix": "F"}),
        "{jeu3.9}His wife has left him and gone to England, says Rose: you're all jealous of me! "
        "{jeu3.10}And she opens the front of her apron. A charm and a medal are pinned to her jumper. "
        "The charm is from Danny.",
        ("C", "I wear it all the time – beside my miraculous medal.", "jeu3.11", {"voix": "F"}),
        "A love token next to a holy medal.",
        ("C", "I love him, Aggie.", "jeu3.12", {"voix": "F"}),
        ("C", "Bastard.", "jeu3.13", {"voix": "F"}),
        "{jeu3.14}Rose is on the point of tears. Silence.",
        ("P", 1.2),
        "{jeu3.15}Then Maggie takes her hen-bucket as a dancing partner, and does a very fast, very exaggerated tango "
        "across the kitchen floor, singing The Isle of Capri.",
        ("C", "Summer time was nearly over; Blue Italian skies above.", "jeu3.16", {"voix": "F"}),
        "{jeu3.17}And she exits by the back door, calling her hens.",
        ("C", "Tchook-tchook-tchook-tchook…", "jeu3.18", {"voix": "F"}),
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Agnes": "buffet", "Rose": FOURNEAU, "Maggie": PATEE, "Chris": "table"},
                 act={"Agnes": "range", "Rose": "debout", "Maggie": "range", "Chris": "repasse"}, cam="tout",
                 objets={"kites": "kites", "garcon": GARCON}, note="“AGNES goes to the cupboard for wool.” (p. 4)"),
            dict(pos={"Agnes": "fenetre"}, act={"Agnes": "debout"}),
            dict(dit=["Agnes", "What's that son of yours at out there?"]),
            dict(note="“She taps on the window, calls ‘Michael!’ and blows a kiss to the imaginary child.”"),
            dict(cam="cuisine", note="“Pity there aren't some boys about to play with.” · “Couldn't we all do with that?”"),
            dict(pos={"Agnes": "tricot_a"}, act={"Agnes": "tricote"}, note="“There's going to be pictures in the hall next Saturday, Aggie.” (p. 5)"),
            dict(dit=["Rose", "And he wants to bring me up to the back hills next Sunday – up to Lough Anna."]),
            dict(dit=["Chris", "Danny Bradley is a scut, Rose."]),
            dict(dit=["Chris", "He's a married man with three young children."]),
            dict(note="“And you're jealous, too! … you're jealous of me!”"),
            dict(note="“She opens the front of her apron. A charm and a medal are pinned to her jumper.”"),
            dict(dit=["Rose", "I wear it all the time – beside my miraculous medal."], note="(p. 6)"),
            dict(dit=["Rose", "I love him, Aggie."]),
            dict(dit=["Chris", "Bastard."], note="(Softly.)"),
            dict(act={"Rose": "fige"}, note="“She is on the point of tears. Silence.”"),
            dict(act={"Maggie": "danse"}, chemin={"Maggie": [PATEE, [530, 505], [190, 505]]}, chemin_duree=6,
                 note="Maggie's tango with her hen-bucket: “very fast and very exaggerated”"),
            dict(dit=["Maggie", "Summer time was nearly over; Blue Italian skies above."]),
            dict(pos={"Maggie": "arriere"}, act={"Maggie": "debout"}, duree=2.5, note="She exits by the back door, calling her hens."),
            dict(pos={"Maggie": "off"}, dit=["Maggie", "Tchook-tchook-tchook-tchook…"]),
        ]),
    }),

    # ------------------------------------------------------------------ IV. l'enfant invisible (p. 6-8)
    dict(id="enfant", chap="The boy who isn't there", fond="nuit", humeur="mystere", beats=[
        "{jeu4}Michael, the adult narrator, enters, and stands at the side of the stage. "
        "{jeu4.1}Rose throws turf into the range, where Chris had an iron; {jeu4.2}then she helps Agnes with the wool.",
        "{jeu4.3}Now Friel sets up a convention. The boy Michael is imaginary: he is working at the kite materials "
        "lying on the ground. {jeu4.4}When the sisters talk to him, the adult Michael answers, in his ordinary narrator's voice.",
        "{jeu4.5}Maggie enters the garden from the back of the house.",
        ("C", "What are these supposed to be?", "jeu4.6", {"voix": "F"}),
        ("C", "Kites.", "jeu4.7"),
        ("C", "I'll give you a penny if those things ever leave the ground. Right?", "jeu4.8", {"voix": "F"}),
        ("C", "You're on.", "jeu4.9"),
        "{jeu4.10}She squats down beside him and tries her riddles on him. He gives up, again and again.",
        ("C", "Look out – there's a rat!", "jeu4.11"),
        "{jeu4.12}She screams, and leaps to her feet in terror.",
        ("C", "Caught you again, Aunt Maggie.", "jeu4.13"),
        "{jeu4.14}Maggie moves off towards the back of the house, stops, and throws him a sweet.",
        ("C", "There. I hope it chokes you.", "jeu4.15", {"voix": "F"}),
        "{jeu4.16}And she exits.",
    ], vis={
        "jeu4": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Agnes": "tricot_a", "Rose": FOURNEAU, "Chris": "table", "Michael": MICHAEL},
                 act={"Agnes": "tricote", "Rose": "fige", "Chris": "repasse", "Michael": "debout"}, cam="tout",
                 objets={"kites": "kites", "garcon": GARCON}, note="“MICHAEL enters and stands L.” (p. 6)"),
            dict(act={"Rose": "range"}, note="“ROSE takes the lid off the range and throws turf into the fire.”"),
            dict(pos={"Rose": "tricot_r"}, act={"Rose": "tricote"}, note="“For God's sake, I have an iron in there!” · “Rosie, love, would you give me a hand with this.”"),
            dict(note="“the imaginary BOY MICHAEL is working at the kite materials lying on the ground”"),
            dict(note="“MICHAEL responds to MAGGIE in his ordinary narrator's voice.”"),
            dict(pos={"Maggie": [740, 290]}, act={"Maggie": "debout"}, note="“MAGGIE enters the garden from the back of the house.”"),
            dict(pos={"Maggie": [615, 440]}, dit=["Maggie", "What are these supposed to be?"]),
            dict(dit=["Michael", "Kites."], note="The boy's lines, spoken by adult Michael"),
            dict(dit=["Maggie", "I'll give you a penny if those things ever leave the ground. Right?"], note="(p. 7)"),
            dict(dit=["Michael", "You're on."], note="(p. 8)"),
            dict(pos={"Maggie": [738, 520]}, act={"Maggie": "agenouille"}, note="“She now squats down beside him.” · “Give up.”"),
            dict(dit=["Michael", "Look out – there's a rat!"]),
            dict(act={"Maggie": "debout"}, note="“She screams and leaps to her feet in terror.”"),
            dict(dit=["Michael", "Caught you again, Aunt Maggie."]),
            dict(pos={"Maggie": [740, 290]}, duree=2, note="“Again she stops and throws him a sweet.”"),
            dict(dit=["Maggie", "There. I hope it chokes you."]),
            dict(pos={"Maggie": "off"}, note="(Exits.)"),
        ]),
    }),

    # ------------------------------------------------------------------ V. le prêtre des lépreux (p. 9)
    dict(id="pretre", chap="Our own leper priest", fond="nuit", humeur="calme", beats=[
        "{jeu5}Page nine. Michael speaks to us again; in the kitchen, the women go on working. "
        "Why was he so shocked by Jack's appearance?",
        ("C", "I expected – well, I suppose, the hero from a schoolboy's book.", "jeu5.1"),
        "{jeu5.2}He had once seen a photograph of Jack in his officer's uniform, a chaplain to the British forces in 1917. "
        "{jeu5.3}But Kate snatched it from him: she had been involved in the War of Independence, so Jack's British army career "
        "was never referred to in that house.",
        "{jeu5.4}To the sisters, Jack was a hero and a saint. They prayed for him and saved for him. "
        "{jeu5.5}The local paper called him our own leper priest, and the family enjoyed a little status in the parish.",
        ("C", "And it must have helped my aunts to bear the shame Mother brought on the household", "jeu5.6"),
        ("C", "by having me – as it was called then – out of wedlock.", "jeu5.7"),
        ("P", 1.0),
    ], vis={
        "jeu5": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Agnes": "tricot_a", "Rose": "tricot_r", "Chris": "table", "Michael": MICHAEL},
                 act={"Agnes": "tricote", "Rose": "tricote", "Chris": "repasse", "Michael": "debout"}, cam="tout",
                 objets={"kites": "kites", "garcon": GARCON}, lumiere="spot", note="Michael speaks to the audience. (p. 9)"),
            dict(dit=["Michael", "I expected – well, I suppose, the hero from a schoolboy's book."]),
            dict(note="A photograph of Jack “radiant and splendid in his officer's uniform”, 1917"),
            dict(note="Kate snatched it: she had been involved in the War of Independence."),
            dict(note="“a hero and a saint to my mother and to my aunts” · “sixpence here, a shilling there”"),
            dict(note="“‘our own leper priest,’ as they called him”: “that little bit of status”"),
            dict(dit=["Michael", "And it must have helped my aunts to bear the shame Mother brought on the household"]),
            dict(dit=["Michael", "by having me – as it was called then – out of wedlock."]),
        ]),
    }),

    # ------------------------------------------------------------------ VI. cinq répliques à connaître
    dict(id="repliques2", chap="Three lines to know", fond="aube", humeur="calme",
         retenir="Kate's voice in Agnes's mouth, the invisible boy, “the shame”: rules, memory, reputation.", beats=[
        "{cinq2}An afternoon of small talk… and three lines that carry the whole play.",
        "First, Kate, who is not even there.{-cinq2}",
        ("C", "As long as Kate's not around. 'Do you want to make a pagan of yourself?'", "c_pagan", {"voix": "F"}),
        "{-c_pagan}{kate}Agnes imitates her, word for word. Lipstick is enough to be called pagan in this house. "
        "That tells you how tight the rules are, and how much desire the sisters have to hide.",
        "Second, a stage direction.{-kate}",
        ("C", "No dialogue with the BOY MICHAEL must ever be addressed directly to adult MICHAEL, the narrator.", "c_conv"),
        "{-c_conv}{effet}Why do this? Because the boy only exists in memory. {effet.1}We never see the child, only the adult remembering him. "
        "{effet.2}And the narrator is inside every scene: he is not just telling the story, he is replaying it. "
        "Notice the kites, too: Maggie bets they will never leave the ground. Keep them in mind until the very end.",
        "And third, Michael himself.{-effet}",
        ("C", "it must have helped my aunts to bear the shame Mother brought on the household by having me – as it was called then – "
              "out of wedlock.", "c_shame"),
        "{-c_shame}{shame}The shame: that is how the household was made to feel about Chris's child, Michael himself. "
        "Notice the distance in as it was called then: the adult narrator quotes the judgement of 1936 without sharing it. "
        "And see the balance: Jack's holiness protects the family's reputation. "
        "So what happens if the saint comes home… changed?",
    ], vis={
        "cinq2": dict(type="mot", t="Small talk, big subtext", g="three lines to know · pages 2 – 9", y=250, taille=80),
        "c_pagan": dict(type="cit", a="Agnes, imitating Kate", o="p. 2", x=170, y=200, w=940),
        "kate": dict(type="def", cles=["absent", "pagan"], terme="Kate's voice",
                     t="Absent from the stage, but present in Agnes's mouth: even lipstick is “pagan”.",
                     etape="Desire has to hide under the rules of a Catholic house.", x=170, y=200, w=940),
        "c_conv": dict(type="cit", a="Stage direction", o="p. 6", x=170, y=200, w=940),
        "effet": dict(type="cols", g="We never see the child", gq="only the adult who remembers him", d="The narrator in every scene",
                      dq="he replays the past, he doesn't just tell it", vs="→", repere="memory play"),
        "c_shame": dict(type="cit", a="Michael", o="p. 9", x=170, y=200, w=940),
        "shame": dict(type="cols", g="Jack's fame", gq="“a hero and a saint”, status in the parish", d="Chris's child",
                      dq="“the shame”, born “out of wedlock”", vs="⚖", repere="reputation"),
    }),

    # ------------------------------------------------------------------ VII. analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Subtext, the outside world in songs, the invisible boy, reputation: the house is held together by fragile balances.", beats=[
        "{a1}Time for the analysis. Four ideas to take from this afternoon. "
        "{a1.1}One: subtext. Almost nothing happens, but every small exchange carries something bigger: a cracked mirror, "
        "a lipstick, a surplice. Critics often call this Friel's Chekhovian method: the drama is under the surface, in what the characters do not say.",
        "{-a1}{a2}{a2.1}Two: desire under surveillance. Lipstick is pagan, Rose's love is for a married man, Chris has a child "
        "outside marriage. Each sister wants something, and Kate's rules, even when Kate is absent, keep watch.",
        "{-a2}{a3}{a3.1}Three: the outside world gets in, but only in fragments. A detail from outside the text: Italy had invaded "
        "Abyssinia, today's Ethiopia, in 1935; De Valera led the Irish government. Here a war and an election "
        "become comic songs, and the radio dies after three seconds. The world is changing, "
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
            "They cannot afford a new one"], ok=0, voir="jeu1.6",
         ex="Superstition: she broke it, so she must keep using it. Symbolically, the sisters only see a broken reflection of themselves."),
    dict(q="When Agnes says “Do you want to make a pagan of yourself?”, she is…",
         r=["imitating what Kate would say about lipstick", "quoting Father Jack", "insulting Rose", "reading from a novel"], ok=0,
         voir="c_pagan", ex="Kate is offstage, but her voice and her rules are present: even lipstick counts as pagan."),
    dict(q="What does Rose wear beside her miraculous medal?",
         r=["A silver charm given by Danny Bradley", "Jack's cross from Africa", "Her mother's ring", "A kite string"], ok=0,
         voir="jeu3.11", ex="A love token next to a holy medal: pagan and Christian side by side."),
    dict(q="How is the boy Michael shown on stage?",
         r=["He is imaginary: the adult narrator speaks his lines", "A child actor plays him", "He is a puppet",
            "He never speaks at all"], ok=0, voir="c_conv",
         ex="Stage direction p. 6: no child appears; adult Michael answers the sisters in his narrator's voice."),
    dict(q="Why was Jack's British army career never mentioned in the house?",
         r=["Kate had been involved locally in the War of Independence", "Jack had deserted",
            "The photo was of another priest", "Maggie had broken the frame"], ok=0, voir="jeu5.3",
         ex="He had been a chaplain to the British forces; Kate had been involved in the War of Independence."),
    dict(q="According to Michael, what did Jack's fame help the aunts to bear?",
         r=["The shame of Chris's child born out of wedlock", "Their poverty", "Kate losing her job", "Rose's illness"], ok=0,
         voir="c_shame", ex="Jack's status as “our own leper priest” balanced the parish's judgement of Chris: a fragile balance."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photograph: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
