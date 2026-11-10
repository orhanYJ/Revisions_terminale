"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 11 : « What happened next », la seconde prolepse (PDF de travail, p. 62-64).

Version « jouée » (05/11/2026, demande de l'élève : « comme Parable of the Sower », personnages représentés, mouvements) :
le résumé est joué sur le plateau (visuel jeu). Rose sort, Michael entre (p. 62) ; pendant son long récit (p. 63-64),
Michael est seul dans la lumière, au bord du plateau, les sœurs immobiles : tout ce qu'il raconte (l'usine, Londres, Jack,
Gerry, le pays de Galles) est dit, jamais joué (bandeaux « told, not shown »). Puis les sœurs « resume their tasks » et
Chris appelle Gerry (p. 64). Ensuite cinq répliques à connaître, l'analyse et le quiz.

Début : p. 62, didascalie « She exits, her shoes in one hand, the poppy in the other. MICHAEL enters. » et la plainte de Kate
(« What has happened to this house? … », p. 62-63). Fin : p. 64, « She now goes outside and calls up to GERRY. MICHAEL exits. »
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_11. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'émigration irlandaise vers la Grande-Bretagne, le sens de « notionate ») est dit comme tel.
Coquille du PDF évitée dans les citations (« the young Sweeney boy from he back hills » : coupé par « … »).
Les cerfs-volants sont posés contre le banc du jardin depuis la didascalie de l'acte II (p. 45), visages cachés.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-11"
NOTION = "Dancing at Lughnasa"
NUM = 11
TITRE = "What happened next"
SUIVANT = "Part 12 · The last afternoon"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "McLaughlin": "Mac-Lock-lin",
                 "Southwark": "Suthuck", "Thames": "Tems", "Mundy": "Mundy"}

PERSOS = ["Kate", "Maggie", "Agnes", "Rose", "Chris", "Michael"]
# positions des sœurs pendant tout le récit de Michael (elles « reprennent leurs tâches » p. 64)
FIGEES = {"Maggie": "buffet", "Chris": "table", "Kate": [290, 515], "Agnes": [450, 450], "Michael": "michael"}
KITES = {"kites": "banc"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Rose walks out of the kitchen, her shoes in one hand, a poppy in the other. "
        "Kate cries out: what has happened to this house?",
        "{-q1}{q2}And Michael steps forward and answers her. Not with comfort: with the future.",
        "{-q2}{-tab_don}{serie}Part eleven: the second prolepsis. In two pages, Michael tells us what became of everyone.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="What has happened to this house?"),
        "q2": dict(type="question", t="Michael answers her with the future."),
        "serie": dict(type="mot", t="The second prolepsis", g="the factory · London · Jack · Gerry",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 11", t="What happened next",
                      sous="Michael's second prolepsis · pages 62 – 64"),
    }),

    # ------------------------------------------------------------------ I. Rose sort, Michael entre (joué)
    dict(id="entree", chap="Michael steps forward", fond="nuit", humeur="mystere", beats=[
        "{jeu1}Page sixty-two. Maggie is preparing the evening meal; Chris is making the toast. "
        "Rose has just told Kate where she spent the afternoon: Lough Anna, Danny Bradley, his father's blue boat.",
        "And that's all any of you are going to hear, she says. {jeu1.1}Then she walks out, towards the bedroom.",
        "{jeu1.2}Her shoes in one hand, the poppy in the other. And, at the edge of the stage, Michael enters.",
        ("C", "What has happened to this house?", "jeu1.3", {"voix": "F"}),
        ("C", "Mother of God, will we ever be able to lift our heads ever again … ?", "jeu1.4", {"voix": "F"}),
        "{jeu1.5}A pause. The sisters stop where they are. Nobody in the kitchen answers Kate. "
        "Michael does, but he speaks to us, not to her.",
        ("P", 1.0),
    ], vis={
        "jeu1": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos={"Maggie": "buffet", "Chris": "table", "Kate": [290, 515], "Agnes": [450, 450], "Rose": [160, 470]},
                 act={"Maggie": "range", "Chris": "range", "Kate": "debout", "Agnes": "debout", "Rose": "debout"},
                 objets=KITES, note="Rose: “That's all any of you are going to hear.” (p. 62)"),
            dict(pos={"Rose": "arriere"}, duree=3.0),
            dict(pos={"Rose": "off", "Michael": "michael"}, cam="tout",
                 note="“She exits, her shoes in one hand, the poppy in the other. MICHAEL enters.” (p. 62)"),
            dict(dit=["Kate", "What has happened to this house?"]),
            dict(dit=["Kate", "Mother of God, will we ever be able to lift our heads ever again … ?"], note="(p. 62 – 63)"),
            dict(act={"Maggie": "fige", "Chris": "fige", "Kate": "fige", "Agnes": "fige"}, lumiere="spot",
                 note="(Pause.)  Michael speaks to the audience."),
        ]),
    }),

    # ------------------------------------------------------------------ II. l'usine (raconté)
    dict(id="usine", chap="The factory", fond="nuit", humeur="tension", beats=[
        "{jeu2}None of what follows is acted. Michael tells it, alone in the light. "
        "The following night, Vera McLaughlin arrived, and explained to Agnes and Rose why she couldn't buy their hand-knitted gloves any more.",
        "{jeu2.1}Most of her home knitters were already working in the new factory. "
        "She advised Agnes and Rose to apply immediately. Then one dry sentence:",
        ("C", "The Industrial Revolution had finally caught up with Ballybeg.", "jeu2.2"),
        "{jeu2.3}They didn't apply, even though they had no other means of making a living. "
        "And they never discussed it with their sisters. Michael does not know why, so he offers three guesses.",
        "{jeu2.4}Perhaps Agnes knew Rose would never get work there. "
        "Perhaps, as Kate believed, Agnes was too notionate: an Irish word, outside the text, for proud and headstrong.",
        ("C", "Or perhaps the two of them just wanted … away.", "jeu2.5"),
        "{jeu2.6}On Michael's first day back at school, there was a note propped against the milk jug.",
        ("C", "We are gone for good. This is best for all. Do not try to find us.", "jeu2.7"),
        "{jeu2.8}It was written in Agnes's resolute hand. And Agnes stands silent in the kitchen as we hear it.",
        ("P", 1.0),
    ], vis={
        "jeu2": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=FIGEES, act={"Maggie": "fige", "Chris": "fige", "Kate": "fige", "Agnes": "fige"}, lumiere="spot",
                 cam="tout", objets=KITES, note="He tells us: the following night, Vera McLaughlin came (told, not shown)"),
            dict(note="Most of her home knitters already worked “in the new factory” (p. 63)"),
            dict(dit=["Michael", "The Industrial Revolution had finally caught up with Ballybeg."]),
            dict(note="“They didn't apply” · they “never discussed their situation with their sisters”"),
            dict(note="Perhaps Rose “wouldn't have got work there” · perhaps Agnes was “too notionate”"),
            dict(dit=["Michael", "Or perhaps the two of them just wanted … away."]),
            dict(note="His first day back at school: “a note propped up against the milk jug” (told, not shown)"),
            dict(dit=["Michael", "We are gone for good. This is best for all. Do not try to find us."]),
            dict(note="“It was written in Agnes's resolute hand.” (p. 63)"),
        ]),
    }),

    # ------------------------------------------------------------------ III. Londres (raconté)
    dict(id="londres", chap="London", fond="nuit", humeur="tension", beats=[
        "{jeu3}Of course they tried to find them: the family, the police, the neighbours with relatives all over England and America. "
        "{jeu3.1}But they had vanished without trace.",
        "{jeu3.2}Twenty-five years later, Michael tracked them down in London. Agnes was dead. "
        "Rose was dying in a hospice for the destitute, in Southwark.",
        "{jeu3.3}What he learned was only scraps, too sparse to be coherent. They had moved about a lot. "
        "{jeu3.4}They worked as cleaning women, in public toilets, in factories, in the Underground. "
        "When Rose could no longer get work, Agnes tried to support them both, but couldn't.",
        ("C", "They took to drink; slept in parks, in doorways, on the Thames Embankment.", "jeu3.5"),
        ("C", "Then Agnes died of exposure.", "jeu3.6"),
        "{jeu3.7}Two days after Michael found Rose in that grim hospice, she died in her sleep. "
        "She didn't recognise me, he adds… of course.",
        ("P", 1.0),
    ], vis={
        "jeu3": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=FIGEES, act={"Maggie": "fige", "Chris": "fige", "Kate": "fige", "Agnes": "fige"}, lumiere="spot",
                 cam="tout", objets=KITES, note="The family, the police, the neighbours search for them (told, not shown)"),
            dict(note="“they had vanished without trace” (p. 63)"),
            dict(note="Twenty-five years later, in London: Agnes dead, Rose dying in a hospice in Southwark"),
            dict(note="“The scraps of information … were too sparse to be coherent.”"),
            dict(note="Cleaning women: public toilets, factories, the Underground"),
            dict(dit=["Michael", "They took to drink; slept in parks, in doorways, on the Thames Embankment."]),
            dict(dit=["Michael", "Then Agnes died of exposure."]),
            dict(note="Rose dies two days later: “she didn't recognize me, of course” (p. 63)"),
        ]),
    }),

    # ------------------------------------------------------------------ IV. Jack et Gerry (raconté)
    dict(id="hommes", chap="Jack and Gerry", fond="nuit", humeur="mystere", beats=[
        "{jeu4}Then Father Jack. His health improved quickly. He recovered his full vocabulary, and all his old bounce and vigour. "
        "But he didn't say Mass that following Monday.",
        ("C", "In fact he never said Mass again.", "jeu4.1"),
        "{jeu4.2}The neighbours stopped asking about him. And there was never a civic reception, with bands and flags and speeches.",
        "{jeu4.3}His tales of the lepers shocked poor Aunt Kate, until she hit on a phrase that appeased her:",
        ("C", "his own distinctive spiritual search.", "jeu4.4"),
        "{jeu4.5}Jack died suddenly of a heart attack, within a year of his homecoming, "
        "on the very eve of the following Lughnasa. For months, Kate was inconsolable.",
        "{jeu4.6}And Gerry? He sailed for Spain that Saturday. The last Michael saw of him: "
        "dancing down the lane like Fred Astaire, Uncle Jack's ceremonial tricorn over his left eye, "
        "blowing a dozen theatrical kisses back to Chris and the boy.",
        ("C", "He was wounded in Barcelona – he fell off his motor-bike – so that for the rest of his life he walked with a limp.",
         "jeu4.7"),
        "{jeu4.8}He still visited about once a year: a new career, a proposal to Chris, a new bike promised to the boy. After the war came in 1939, his visits grew rarer, and finally he stopped coming.",
        "{jeu4.9}In the mid-fifties, a letter came from a tiny village in the south of Wales, "
        "from a young man of Michael's own age, also called Michael Evans: Michael's half-brother. "
        "Gerry had died peacefully, nursed by his wife and his three grown children.",
        ("C", "My mother never knew of that letter.", "jeu4.10"),
        "{jeu4.11}Michael hesitated for years, as his father would have done. And in the end, rightly or wrongly, he kept it to himself.",
        ("P", 1.0),
    ], vis={
        "jeu4": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=FIGEES, act={"Maggie": "fige", "Chris": "fige", "Kate": "fige", "Agnes": "fige"}, lumiere="spot",
                 cam="tout", objets=KITES, note="Father Jack recovers his “full vocabulary” (told, not shown)"),
            dict(dit=["Michael", "In fact he never said Mass again."]),
            dict(note="Never “a civic reception with bands and flags and speeches” (p. 63)"),
            dict(note="Each new revelation “startled – shocked – stunned poor Aunt Kate”"),
            dict(dit=["Michael", "his own distinctive spiritual search."], note="Kate's phrase, as Michael quotes it"),
            dict(note="Jack dies within a year, “on the very eve of the following La Lughnasa” (p. 63 – 64)"),
            dict(note="Gerry dances down the lane “in imitation of Fred Astaire”, Jack's tricorn on his head (told)"),
            dict(dit=["Michael", "He was wounded in Barcelona – he fell off his motor-bike – …"], note="(p. 64)"),
            dict(note="Once a year: a new career, a proposal, a new bike · 1939: rarer visits, then none"),
            dict(note="Mid-fifties: a letter from Wales · a half-brother · Gerry's wife and three children"),
            dict(dit=["Michael", "My mother never knew of that letter."]),
            dict(note="“… and eventually, rightly or wrongly, kept the information to myself.” (p. 64)"),
        ]),
    }),

    # ------------------------------------------------------------------ V. retour dans la cuisine (joué)
    dict(id="cuisine", chap="Back to their tasks", fond="nuit", humeur="calme", beats=[
        "{jeu5}Then the stage direction: Maggie, Chris, Kate and Agnes now resume their tasks. "
        "The kitchen of 1936 comes back to life, as if nothing had been said.",
        ("C", "Well, at least that's good news.", "jeu5.1", {"voix": "F"}),
        ("C", "What's that?", "jeu5.2", {"voix": "F"}),
        ("C", "That the young Sweeney boy … is going to live.", "jeu5.3", {"voix": "F"}),
        ("C", "Good news indeed.", "jeu5.4", {"voix": "F"}),
        "{jeu5.5}The Sweeney boy, burned at the Lughnasa fires, will live. "
        "But we have just heard who will not: Agnes, standing right there, will die of exposure in London.",
        "{jeu5.6}Chris goes to the door and calls.",
        ("C", "Michael! Where are you? We need some turf brought in!", "jeu5.7", {"voix": "F"}),
        "{jeu5.8}She goes outside, and calls up to Gerry, at the top of the sycamore. "
        "And Michael exits. The memory takes over again.",
        ("P", 1.0),
    ], vis={
        "jeu5": dict(type="jeu", persos=PERSOS, etats=[
            dict(pos=FIGEES, act={"Maggie": "range", "Chris": "range", "Kate": "debout", "Agnes": "debout"}, lumiere=None,
                 cam="tout", objets=KITES, note="“MAGGIE, CHRIS, KATE, and AGNES now resume their tasks.” (p. 64)"),
            dict(dit=["Chris", "Well, at least that's good news."]),
            dict(dit=["Maggie", "What's that?"]),
            dict(dit=["Chris", "That the young Sweeney boy … is going to live."]),
            dict(dit=["Maggie", "Good news indeed."]),
            dict(note="Dramatic irony: the audience now knows how Agnes and Rose will die."),
            dict(pos={"Chris": "porte"}, act={"Chris": "debout"}, note="“CHRIS goes to the door and calls.”"),
            dict(dit=["Chris", "Michael! Where are you? We need some turf brought in!"]),
            dict(pos={"Chris": [700, 330], "Michael": "off"},
                 note="“She now goes outside and calls up to GERRY. MICHAEL exits.” (p. 64)"),
        ]),
    }),

    # ------------------------------------------------------------------ VI. cinq répliques à connaître
    dict(id="repliques", chap="Key lines to know", fond="aube", humeur="calme",
         retenir="“The Industrial Revolution…”, Agnes's note, the Thames Embankment, the motor-bike, “vacillated”.", beats=[
        "{cinq}Michael's speech is pure narration: no stage directions, only his voice. Five lines are worth knowing by heart.",
        "{-cinq}First, the factory.",
        ("C", "The Industrial Revolution had finally caught up with Ballybeg.", "c_indus"),
        "{-c_indus}{indus}A huge historical phrase for one new glove factory. Gentle irony, hard meaning: "
        "hand work is over, and with it, the sisters' only money.",
        "{-indus}Then, Agnes's note.",
        ("C", "We are gone for good. This is best for all. Do not try to find us.", "c_note", {"voix": "F"}),
        "{-c_note}{trois}Three short sentences, no names, no goodbye. Agnes, so quiet all through the play, "
        "makes the boldest decision of anyone. And she makes it in writing, in silence, like so much in this house.",
        "{-trois}Then, London.",
        ("C", "They took to drink; slept in parks, in doorways, on the Thames Embankment. Then Agnes died of exposure.", "c_drink"),
        "{-c_drink}{ironie}Feel the irony. Perhaps they left to avoid the factory; they ended up cleaning in factories. "
        "They left to be free, and died homeless. And Kate's question from Act One, what would become of our Rosie, "
        "gets its answer here. Outside the text: many thousands of Irish people left for Britain, "
        "often for low-paid work. Agnes and Rose belong to that silent story.",
        "{-ironie}Then, Gerry.",
        ("C", "He was wounded in Barcelona – he fell off his motor-bike – so that for the rest of his life he walked with a limp.",
         "c_limp"),
        "{-c_limp}{limp}Listen to the dash: wounded in Barcelona… then the truth: he fell off his motorbike. "
        "The war hero turns into a comic accident. And the limp ends his dancing days.",
        "{-limp}And last, Michael himself.",
        ("C", "I decided to tell her – decided not to – vacillated for years as my father would have done", "c_vacill"),
        "{-c_vacill}{pere}The narrator hesitates like Gerry. And he chooses what Chris will know, "
        "just as he chooses what we see.",
    ], vis={
        "cinq": dict(type="mot", t="Five lines to know", g="Michael's second prolepsis · pages 63 – 64", y=250, taille=80),
        "c_indus": dict(type="cit", a="Michael", o="p. 63", x=170, y=210, w=940),
        "indus": dict(type="note", cles=["hand", "money"], terme="Irony · a grand phrase",
                      t="The hand-made world is over, and so is the sisters' only income.",
                      etape="History arrives in Ballybeg as a glove factory.", x=170, y=200, w=940),
        "c_note": dict(type="cit", a="Agnes's note", o="p. 63", x=170, y=210, w=940),
        "trois": dict(type="note", cles=["boldest", "silence"], terme="Agnes's note",
                      t="The quiet sister makes the boldest choice.",
                      etape="In writing, in silence: nothing is discussed.", x=170, y=200, w=940),
        "c_drink": dict(type="cit", a="Michael", o="p. 63", x=170, y=200, w=940),
        "ironie": dict(type="note", cles=["irony", "free"], terme="Irony · and history",
                       t="They refuse the factory… and end up cleaning in factories; they leave to be free… and die homeless.",
                       etape="Outside the text: Irish emigration to Britain, often for low-paid work.", x=170, y=200, w=940),
        "c_limp": dict(type="cit", a="Michael", o="p. 64", x=170, y=200, w=940),
        "limp": dict(type="note", cles=["motorbike", "dancing"], terme="Anticlimax · p. 64",
                     t="Not a battle wound: a fall from a motorbike.",
                     etape="The limp “put an end to his dancing days”.", x=170, y=200, w=940),
        "c_vacill": dict(type="cit", a="Michael", o="p. 64", x=170, y=210, w=940),
        "pere": dict(type="mot", t="Like father, like son", g="the narrator chooses what others know", y=260, taille=84),
    }),

    # ------------------------------------------------------------------ VII. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Prolepsis, flat narrative prose, the factory and emigration, irony: the future is told before the last afternoon.", beats=[
        "{a1}Now the analysis. Four ideas. "
        "{a1.1}One: the second prolepsis. In Act One, we learned that Agnes and Rose would leave. "
        "Now we learn how they die, just before the last gentle scenes of the play. "
        "From now on, every smile of Agnes and Rose is watched with tragic knowledge.",
        "{-a1}{a2}{a2.1}Two: narrative prose against drama. On stage, the play is warm, comic, alive. "
        "Here, Michael speaks in flat, factual sentences: drink, parks, doorways, exposure. Twenty-five years in one paragraph. "
        "And his knowledge has holes: perhaps, perhaps, perhaps; mere scraps. Memory, again, is incomplete and selective.",
        "{-a2}{a3}{a3.1}Three: economics and the outside world. Industrialisation kills the cottage economy; emigration finishes the job. "
        "The modern world arrives in Ballybeg as a factory, and takes its people away. "
        "Spain and London bring the Mundys no happy endings; Wales gives Gerry a peace he never gave Chris.",
        "{-a3}{a4}{a4.1}Four: irony. No bands and flags for Jack. A motorbike, not a battle, for Gerry. "
        "Good news about the Sweeney boy, right after the deaths. "
        "The gap between hopes and outcomes is the tragedy.",
        "{-a4}{carte}For your essay, this passage supports four ideas. {carte.1}Prolepsis and tragic knowledge. "
        "{carte.2}The narrator and his limited memory. {carte.3}The economy, the factory and emigration. "
        "{carte.4}And irony: the outside world cuts every dream down to size.",
    ], vis={
        "a1": dict(type="note", cles=["prolepsis", "tragic"], terme="1 · The second prolepsis",
                   t="After “left for ever” (Act One), Michael now tells how Agnes and Rose die.",
                   etape="Placed just before the last scenes: tragic knowledge.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["flat", "perhaps"], terme="2 · Narrative prose",
                   t="Flat, factual sentences: “parks, … doorways, … the Thames Embankment”.",
                   etape="Gaps in his knowledge: “perhaps” three times; “scraps”.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["factory", "emigration"], terme="3 · Economy and the outside world",
                   t="“The Industrial Revolution had finally caught up with Ballybeg.”",
                   etape="The factory, then emigration: the cottage economy collapses.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["irony", "motorbike"], terme="4 · Irony",
                   t="No “bands and flags” for Jack; a motorbike for Gerry; “good news” after the deaths.",
                   etape="The gap between hopes and outcomes is the tragedy.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="WHAT HAPPENED NEXT", branches=[
            dict(t="Prolepsis", items=["“gone for good”", "tragic knowledge", "“at least that's good news”"]),
            dict(t="Narrator", items=["“perhaps” × 3", "“scraps … too sparse”", "he keeps Gerry's secret"]),
            dict(t="Economy", items=["“the Industrial Revolution”", "the glove factory", "emigration to London"]),
            dict(t="Irony", items=["“fell off his motor-bike”", "no “bands and flags”", "the Thames Embankment"])]),
    }),
]

QUIZ = [
    dict(q="Why can Vera McLaughlin no longer buy Agnes and Rose's gloves?",
         r=["A new factory in Donegal Town makes gloves more cheaply", "Kate has forbidden it", "The wool has become too expensive",
            "She is leaving for America"], ok=0, voir="jeu2.1",
         ex="Chris (p. 56): “Too dear”; the new factory sells gloves cheaply. “The Industrial Revolution had finally caught up with Ballybeg.” (p. 63)"),
    dict(q="What does Agnes's note say?",
         r=["“We are gone for good. This is best for all. Do not try to find us.”", "“We will write from London.”",
            "“Forgive us, Kate.”", "“We have gone to the factory.”"], ok=0, voir="c_note",
         ex="Three short sentences in “Agnes's resolute hand”, propped against the milk jug on Michael's first day back at school."),
    dict(q="When and where does Michael find Agnes and Rose again?",
         r=["Twenty-five years later, in London", "One year later, in Donegal Town", "In the mid-fifties, in Wales",
            "Never: they vanished for good"], ok=0, voir="jeu3.2",
         ex="By then “Agnes was dead and Rose was dying in a hospice for the destitute in Southwark”."),
    dict(q="How was Gerry “wounded in Barcelona”?",
         r=["He fell off his motorbike", "In a battle against Franco's army", "During a dance", "He was never wounded"], ok=0,
         voir="c_limp",
         ex="An anticlimax: the hero's wound is an accident. The limp “put an end to his dancing days”."),
    dict(q="What does the letter from Wales reveal?",
         r=["Gerry had a wife and three children there, and has died", "Gerry is coming back to marry Chris",
            "Agnes and Rose are living in Wales", "Jack's superiors want him back"], ok=0, voir="jeu4.9",
         ex="His half-brother, also called Michael Evans, writes that Gerry died peacefully, nursed by his wife and three grown children."),
    dict(q="Why is Chris's line “Well, at least that's good news” so painful?",
         r=["We have just heard how Agnes and Rose will die", "Chris is being sarcastic about Rose", "The Sweeney boy is actually dead",
            "Kate has just lost her job"], ok=0, voir="jeu5.5",
         ex="Dramatic irony: the characters resume their tasks; the audience now carries the knowledge of their future."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
