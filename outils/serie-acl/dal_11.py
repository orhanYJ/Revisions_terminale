"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 11 : « What happened next », la seconde prolepse (PDF de travail, p. 62-64).

Début : p. 62, didascalie « She exits, her shoes in one hand, the poppy in the other. MICHAEL enters. » et la plainte de Kate
(« What has happened to this house? … », p. 62-63). Michael raconte la suite : Vera McLaughlin et l'usine, le départ d'Agnes et
de Rose, leur fin à Londres, Jack, Gerry en Espagne et sa famille au pays de Galles (p. 63-64). Fin : p. 64, « She now goes outside
and calls up to GERRY. MICHAEL exits. » (après « Well, at least that's good news » et l'appel de Chris).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_11. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'émigration irlandaise vers la Grande-Bretagne, le sens de « notionate ») est dit comme tel.
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

    # ------------------------------------------------------------------ I. l'usine
    dict(id="usine", chap="The factory", fond="aube", humeur="tension",
         retenir="The glove factory ends Agnes and Rose's income. They refuse it, and leave a note: “We are gone for good.”", beats=[
        "{tab_gle}{vera}Remember part ten: Vera McLaughlin, the knitting agent, would buy no more hand-made gloves. "
        "{vera.1}The following night, Michael says, she came to explain it herself. "
        "{vera.2}Most of her home knitters were already working in the new factory. "
        "{vera.3}She advised Agnes and Rose to apply immediately. Then one dry sentence:",
        "{-vera}",
        ("C", "The Industrial Revolution had finally caught up with Ballybeg.", "c_indus"),
        "{-c_indus}{-tab_gle}{indus}A huge historical phrase for one small glove factory. Gentle irony, hard meaning: "
        "hand work is over, and with it, the sisters' only money.",
        "{-indus}{perhaps}They didn't apply. Michael does not know why, so he offers three guesses. "
        "{perhaps.1}Perhaps Agnes knew Rose would never get work there. "
        "{perhaps.2}Perhaps, as Kate believed, Agnes was too notionate, an Irish word, outside the text, for proud and headstrong. "
        "{perhaps.3}Or perhaps the two of them just wanted… away.",
        "{-perhaps}{note_lait}On Michael's first day back at school, there was a note propped against the milk jug, "
        "in Agnes's resolute hand.",
        "{-note_lait}",
        ("C", "We are gone for good. This is best for all. Do not try to find us.", "c_note", {"voix": "F"}),
        "{-c_note}{trois}Three short sentences, no names, no goodbye. {trois.1}Agnes, so quiet all through the play, "
        "makes the boldest decision of anyone. {trois.2}And she makes it in writing, in silence, like so much in this house.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "vera": dict(type="liste", titre="Vera McLaughlin · page 63", items=[
            "She can't buy their “hand-knitted gloves” any more",
            "Most home knitters already work “in the new factory”",
            "She advises Agnes and Rose to apply"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_indus": dict(type="cit", a="Michael", o="p. 63", x=170, y=210, w=940),
        "indus": dict(type="note", cles=["hand", "money"], terme="Irony · a grand phrase",
                      t="The hand-made world is over, and so is the sisters' only income.",
                      etape="History arrives in Ballybeg as a glove factory.", x=170, y=200, w=940),
        "perhaps": dict(type="liste", titre="Why didn't they apply? Three guesses", items=[
            "Rose “wouldn't have got work there anyway”",
            "Kate: Agnes was “too notionate” for a factory",
            "“Or perhaps the two of them just wanted … away.”"], marques=["?", "?", "?"], x=150, y=180, w=980),
        "note_lait": dict(type="mot", t="A note against the milk jug", g="Michael's first day back at school", y=260, taille=80),
        "c_note": dict(type="cit", a="Agnes's note", o="p. 63", x=170, y=210, w=940),
        "trois": dict(type="liste", titre="Agnes's note", cles=["boldest", "silence"], items=[
            "the quiet sister makes the boldest choice",
            "in writing, in silence: nothing is discussed"], marques=["1", "2"], x=170, y=210, w=940),
    }),

    # ------------------------------------------------------------------ II. Londres
    dict(id="londres", chap="London", fond="nuit", humeur="tension",
         retenir="Twenty-five years later, in London: Agnes dead of exposure, Rose dying in a hospice for the destitute.", beats=[
        "{search}Of course they tried to find them: the family, the police, the neighbours with relatives all over England and America. "
        "{search.1}They had vanished without trace.",
        "{search.2}Twenty-five years later, Michael tracked them down in London. Agnes was dead. "
        "Rose was dying in a hospice for the destitute in Southwark.",
        "{-search}{scraps}What he learned was only scraps, too sparse to be coherent. "
        "{scraps.1}They moved about a lot. {scraps.2}They worked as cleaning women, in public toilets, in factories, in the Underground. "
        "{scraps.3}When Rose could no longer get work, Agnes tried to support them both, but couldn't.",
        "{-scraps}",
        ("C", "They took to drink; slept in parks, in doorways, on the Thames Embankment. Then Agnes died of exposure.", "c_drink"),
        "{-c_drink}{rose}Two days after Michael found Rose, she died in her sleep. She didn't recognise me, he adds… of course.",
        "{-rose}{ironie}Feel the irony. {ironie.1}They left to escape the factory, and ended up cleaning toilets in factories. "
        "{ironie.2}They left to be free, and died homeless. "
        "{ironie.3}And Kate's terrible question from Act One, what would become of our Rosie, gets its answer here.",
        "{-ironie}{emig}Outside the text: for decades, many thousands of Irish people left for Britain, "
        "often for low-paid work. Agnes and Rose belong to that silent story.",
    ], vis={
        "search": dict(type="liste", titre="Gone for good · page 63", items=[
            "“they had vanished without trace”",
            "Twenty-five years later, in London: Agnes dead, Rose dying"], marques=["1", "25"], x=150, y=200, w=980),
        "scraps": dict(type="liste", titre="“Scraps of information” · page 63", items=[
            "“They had moved about a lot.”",
            "Cleaning women: public toilets, factories, the Underground",
            "Rose out of work; Agnes can't support them both"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_drink": dict(type="cit", a="Michael", o="p. 63", x=170, y=200, w=940),
        "rose": dict(type="mot", t="“she didn't recognize me, of course”", g="Rose dies in her sleep, two days later",
                     y=260, taille=72),
        "ironie": dict(type="liste", titre="Irony", cles=["irony"], items=[
            "they flee the factory … and clean toilets in factories",
            "they leave to be free … and die homeless",
            "Kate's question, “what would become of our Rosie?”, is answered"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "emig": dict(type="note", cles=["Britain", "low-paid"], terme="Outside the text",
                     t="Irish emigration to Britain: many thousands left for low-paid work in the big cities.",
                     etape="Agnes and Rose belong to that silent history.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. Jack et Gerry
    dict(id="hommes", chap="Jack and Gerry", fond="aube", humeur="mystere",
         retenir="Jack never says Mass again and dies within a year; Gerry is wounded falling off his motorbike, and has a family in Wales.", beats=[
        "{tab_kil}{jack}Then Father Jack. {jack.1}His health improved quickly; he recovered his full vocabulary. "
        "{jack.2}But he never said Mass again. "
        "{jack.3}No civic reception, no bands and flags and speeches. The neighbours simply stopped asking about him.",
        "{-jack}{kate}Kate finally found a phrase to make peace with it: his own distinctive spiritual search. "
        "{kate.1}A polite formula to cover a priest who dances round a fire.",
        "{-kate}{-tab_kil}{mort}Jack died suddenly of a heart attack, within a year of his homecoming, "
        "on the very eve of the following Lughnasa. And for months, Kate was inconsolable.",
        "{-mort}{gerry}And Gerry? He sailed for Spain that Saturday. {gerry.1}The last Michael saw of him: "
        "dancing down the lane like Fred Astaire, Jack's tricorn hat on his head, "
        "{gerry.2}blowing a dozen theatrical kisses back to Chris and the boy.",
        "{-gerry}",
        ("C", "He was wounded in Barcelona – he fell off his motor-bike – so that for the rest of his life he walked with a limp.",
         "c_limp"),
        "{-c_limp}{limp}Listen to the dash: wounded in Barcelona… then the truth: he fell off his motorbike. "
        "The war hero turns into a comic accident. And the limp ends his dancing days.",
        "{-limp}{galles}{galles.1}He visited once a year, always about to start a new career, always proposing, always promising a new bike. "
        "{galles.2}After the war came in 1939, he stopped coming. "
        "{galles.3}In the mid-fifties, a letter came from a tiny village in Wales, from a young man also called Michael Evans: "
        "Michael's half-brother. Gerry had died peacefully, nursed by his wife and three grown children. "
        "Michael never told his mother.",
        "{-galles}",
        ("C", "I decided to tell her – decided not to – vacillated for years as my father would have done", "c_vacill"),
        "{-c_vacill}{pere}The narrator hesitates like Gerry. And he chooses what Chris will know, "
        "just as he chooses what we see.",
    ], vis={
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "jack": dict(type="liste", titre="Father Jack · page 63", items=[
            "His health and his “full vocabulary” come back",
            "“In fact he never said Mass again.”",
            "No “bands and flags and speeches”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "kate": dict(type="note", cles=["distinctive", "polite"], terme="Kate's phrase · p. 63",
                     t="“his own distinctive spiritual search”",
                     etape="A polite formula for a priest who dances round a fire.", x=170, y=200, w=940),
        "mort": dict(type="mot", t="On the very eve of Lughnasa", g="Jack dies within a year · Kate is inconsolable",
                     y=260, taille=80),
        "gerry": dict(type="liste", titre="Gerry leaves · page 64", items=[
            "Dancing down the lane “in imitation of Fred Astaire”",
            "“a dozen theatrical kisses back to Mother and me”"], marques=["1", "2"], x=150, y=200, w=980),
        "c_limp": dict(type="cit", a="Michael", o="p. 64", x=170, y=200, w=940),
        "limp": dict(type="note", cles=["motorbike", "dancing"], terme="Anticlimax · p. 64",
                     t="Not a battle wound: a fall from a motorbike.",
                     etape="The limp “put an end to his dancing days”.", x=170, y=200, w=940),
        "galles": dict(type="liste", titre="What Michael learned later · page 64", items=[
            "Once a year: a new career, a proposal, a new bike",
            "1939: the war; then he stops coming",
            "Mid-fifties: a letter from Wales, a half-brother"], marques=["1", "1939", "W"], x=150, y=180, w=980),
        "c_vacill": dict(type="cit", a="Michael", o="p. 64", x=170, y=210, w=940),
        "pere": dict(type="mot", t="Like father, like son", g="the narrator chooses what others know", y=260, taille=84),
    }),

    # ------------------------------------------------------------------ IV. retour dans la cuisine
    dict(id="cuisine", chap="Back to their tasks", fond="aube", humeur="calme",
         retenir="The sisters resume their tasks; Chris calls it “good news” that the Sweeney boy will live.", beats=[
        "{taches}Then the stage direction: Maggie, Chris, Kate and Agnes now resume their tasks. "
        "The kitchen, 1936, comes back to life, as if nothing had been said.",
        "{-taches}",
        ("C", "Well, at least that's good news.", "c_good", {"voix": "F"}),
        "{-c_good}{sweeney}{sweeney.1}Chris means the Sweeney boy, burned at the Lughnasa fires: he is going to live. "
        "{sweeney.2}But we have just heard who will not. Agnes, standing right there, will die of exposure in London.",
        "{-sweeney}{fin}{fin.1}Chris calls Michael to bring in some turf, then goes out to call up to Gerry. "
        "{fin.2}And Michael exits. The memory takes over again.",
    ], vis={
        "taches": dict(type="mot", t="They resume their tasks", g="the kitchen, 1936, as if nothing had been said", y=260, taille=80),
        "c_good": dict(type="cit", a="Chris", o="p. 64", x=170, y=220, w=940),
        "sweeney": dict(type="cols", g="The Sweeney boy", gq="“going to live”", d="Agnes and Rose",
                        dq="we know how they will die", vs="≠", repere="dramatic irony"),
        "fin": dict(type="liste", titre="Stage directions · page 64", items=[
            "Chris: “We need some turf brought in!”",
            "“She now goes outside and calls up to GERRY. MICHAEL exits.”"], marques=["1", "2"], x=150, y=200, w=980),
    }),

    # ------------------------------------------------------------------ V. l'analyse
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
        "Spain, London, Wales: the world beyond Ballybeg brings no happy endings.",
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
         r=["Her home knitters are already working in the new factory", "Kate has forbidden it", "The wool has become too expensive",
            "She is leaving for America"], ok=0, voir="vera",
         ex="“Most of her home knitters were already working in the new factory”: “The Industrial Revolution had finally caught up with Ballybeg.”"),
    dict(q="What does Agnes's note say?",
         r=["“We are gone for good. This is best for all. Do not try to find us.”", "“We will write from London.”",
            "“Forgive us, Kate.”", "“We have gone to the factory.”"], ok=0, voir="c_note",
         ex="Three short sentences in “Agnes's resolute hand”, propped against the milk jug on Michael's first day back at school."),
    dict(q="When and where does Michael find Agnes and Rose again?",
         r=["Twenty-five years later, in London", "One year later, in Donegal Town", "In the mid-fifties, in Wales",
            "Never: they vanished for good"], ok=0, voir="search",
         ex="By then “Agnes was dead and Rose was dying in a hospice for the destitute in Southwark”."),
    dict(q="How was Gerry “wounded in Barcelona”?",
         r=["He fell off his motorbike", "In a battle against Franco's army", "During a dance", "He was never wounded"], ok=0,
         voir="c_limp",
         ex="An anticlimax: the hero's wound is an accident. The limp “put an end to his dancing days”."),
    dict(q="What does the letter from Wales reveal?",
         r=["Gerry had a wife and three children there, and has died", "Gerry is coming back to marry Chris",
            "Agnes and Rose are living in Wales", "Jack's superiors want him back"], ok=0, voir="galles",
         ex="His half-brother, also called Michael Evans, writes that Gerry died peacefully, nursed by his wife and three grown children."),
    dict(q="Why is Chris's line “Well, at least that's good news” so painful?",
         r=["We have just heard how Agnes and Rose will die", "Chris is being sarcastic about Rose", "The Sweeney boy is actually dead",
            "Kate has just lost her job"], ok=0, voir="sweeney",
         ex="Dramatic irony: the characters resume their tasks; the audience now carries the knowledge of their future."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
