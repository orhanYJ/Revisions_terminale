"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 3 : la fête des moissons (PDF de travail, p. 9-15).

Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_3.
Kate rentre de la ville (cadeaux, médicaments), Rose la taquine sur Austin Morgan, Ballybeg « off its head » à cause
du bal des moissons, la quinine et la confusion de Jack (Okawa), Agnes propose d'y aller toutes, l'élan des sœurs,
puis le refus de Kate. Arrêt juste avant le retour de Maggie (« The fox is back », p. 15).
Citations courtes, à fin d'analyse ; ce qui ne vient pas du texte est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-3"
NOTION = "Dancing at Lughnasa"
NUM = 3
TITRE = "The harvest dance"
SUIVANT = "Part 4 · Jack comes in"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Okawa": "Oh-kah-wa", "Carrickfad": "Carrick-fad",
                 "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture3", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_gle}{q1}This August, everywhere you go in Ballybeg, people ask the same question.",
        "{-q1}{mot_d}In this part, one word turns a quiet afternoon upside down: dance. "
        "The sisters want to go. Kate says no.",
        ("P", 0.3),
        "{-mot_d}{-tab_gle}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "q1": dict(type="question", t="Are you going to the harvest dance?"),
        "mot_d": dict(type="mot", t="dance", g="the word that turns the afternoon upside down", y=260, taille=110),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 3", t="The harvest dance",
                      sous="Kate comes home · pages 9 – 15"),
    }),

    # ------------------------------------------------------------------ I. Kate rentre
    dict(id="retour", chap="Kate comes home", fond="aube", humeur="lumiere",
         retenir="Kate the provider: gifts, books, medicine. Tender with the boy, and clearly in charge.", beats=[
        "{tab_don}{arrive}Page nine. {arrive.1}Kate comes back from the town, laden with shopping bags. "
        "{arrive.2}She sees the boy at his kites, and her face lights up with pleasure. "
        "Remember: the boy is invisible, and the adult Michael speaks his lines. "
        "{arrive.3}Then come the presents: a spinning-top and a whip, and a new library book.",
        "{-arrive}{note_k}Now one stage direction. Kate studies the faces painted on the kites, "
        "faces the audience cannot see. And she plays at being frightened.",
        "{-note_k}",
        ("C", "What are they? Devils? Ghosts?", "c_ghosts", {"voix": "F"}),
        "{-c_ghosts}{fore}A joke. But keep those hidden faces in mind: as we learn later, the play only shows them near the very end. "
        "Something wild and pagan is already painted on the boy's toys.",
        "{-fore}{deux_k}So this is a softer Kate. Chris even says: you have him spoiled. "
        "{deux_k.d}But notice who pays. Kate has the only real salary in the house. "
        "The gifts are love… and a sign of who holds the purse.",
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "arrive": dict(type="liste", titre="Kate comes home · pp. 9 – 10", items=[
            "She enters “laden with shopping bags”",
            "Her face “lights up with pleasure” at the kites",
            "Gifts: a spinning-top, a whip, a library book"], marques=["p. 9", "p. 9", "p. 10"], x=150, y=180, w=980),
        "note_k": dict(type="note", cles=["cannot", "see"], terme="Stage direction · p. 10",
                       t="“She studies the kite faces which the audience cannot see.”",
                       etape="Kate sees the faces. We do not.", x=170, y=200, w=940),
        "c_ghosts": dict(type="cit", a="Kate, with “pretended horror”", o="p. 10", x=170, y=200, w=940),
        "fore": dict(type="def", cles=["hidden", "pagan"], terme="Foreshadowing",
                     t="A hint of what is to come: the hidden faces, devils and ghosts, a pagan world on a child's toy.",
                     etape="The faces are only revealed near the end of the play.", x=170, y=200, w=940),
        "deux_k": dict(type="cols", g="Tender", gq="kisses, kites, a library book at bedtime", d="In charge",
                       dq="she pays, she buys, she decides", vs="+", repere="Kate's two faces"),
    }),

    # ------------------------------------------------------------------ II. Austin Morgan
    dict(id="austin", chap="Austin Morgan", fond="nuit", humeur="tension",
         retenir="Kate's secret: an evasion, a blush, a burst of anger. Her sisters close the subject to protect her.", beats=[
        "{dia_am}Then Rose starts teasing. Kate bought the top at Morgan's Arcade, {dia_am.1}and Rose knows why. "
        "{dia_am.2}Kate answers with the harvest. "
        "{dia_am.3}Rose insists: she's blushing!",
        "{-dia_am}{sub}This is subtext. Kate never says a word about Austin Morgan. But her blush speaks for her. "
        "Then Rose adds that he is going with a wee young thing from Carrickfad. And Kate explodes.",
        "{-sub}",
        ("C", "For God's sake, Rose, shut up, would you!", "c_shut", {"voix": "F"}),
        "{-c_shut}{eclat}Sudden anger, says the stage direction: the control cracks. "
        "{eclat.1}Agnes cuts Rose off: pass me those steel needles. "
        "{eclat.2}A pause. Then Chris, gently: are you tired? "
        "{eclat.3}In this house, painful things are covered with silence and small tasks.",
    ], vis={
        "dia_am": dict(type="dialogue", lignes=["Rose: “You wanted to see Austin Morgan!”",
                                                 "Kate: “Going to be a good harvest by the look of it.”",
                                                 "Rose: “She's blushing! Look! Isn't she blushing?”"],
                       src="p. 11", x=170, y=130, w=980),
        "sub": dict(type="def", cles=["harvest", "blush"], terme="Subtext",
                    t="What a character means but does not say: Kate talks about the harvest, her blush talks about Austin Morgan.",
                    etape="A woman of authority, with a hidden longing.", x=170, y=200, w=940),
        "c_shut": dict(type="cit", a="Kate (sudden anger)", o="p. 11", x=170, y=200, w=940),
        "eclat": dict(type="liste", titre="After the outburst · p. 11", items=[
            "Agnes: “Rosie, pass me those steel needles”",
            "(Pause.) Chris: “Are you tired?”",
            "The subject is closed: silence and small tasks"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ III. Ballybeg perd la tête
    dict(id="fievre", chap="Off its head", fond="aube", humeur="mystere",
         retenir="Ballybeg has caught a “fever”: the dance. In the same speech, Kate hands out quinine for Jack's malaria.", beats=[
        "{tab_gle2}{ville}Kate flops into a seat and gives the news from town. "
        "{ville.1}Ballybeg is off its head: are you going to the harvest dance? Who with? What are you wearing? "
        "{ville.2}A girl of fifteen told her it would be just supreme. You'd think, says Kate, it was heaven she was talking about.",
        "{-ville}",
        ("C", "I'm telling you – off its head – like a fever in the place.", "c_fever", {"voix": "F"}),
        "{-c_fever}{-tab_gle2}{tab_kil}{jux}And her very next words? That's the quinine: for Jack's malaria. "
        "{jux.g}A fever of dancing in the village. {jux.d}A real fever in Father Jack. "
        "This juxtaposition links desire and illness, the festival and the sick priest.",
        "{-jux}{jack}Kate repeats the doctor: {jack.1}after twenty-five years of Swahili, it's not that Jack's mind is confused. "
        "{jack.2}Chris disagrees: he keeps calling her by a strange name. Okawa, says Kate: his house boy. "
        "{jack.3}Kate holds on to the reassuring version. Jack has lost his English: a sign of how far he has drifted from home.",
    ], vis={
        "tab_gle2": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.2, .4, .5], a=[1.05, .55, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "ville": dict(type="liste", titre="News from town · pp. 11 – 12", items=[
            "Ballybeg is “off its head”: one topic, the harvest dance",
            "Sophia, fifteen: “just supreme this year”"], marques=["1", "2"], x=150, y=200, w=980),
        "c_fever": dict(type="cit", a="Kate", o="p. 12", x=170, y=200, w=940),
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "jux": dict(type="cols", g="The village", gq="“like a fever”: the harvest dance", d="Father Jack",
                    dq="malaria: “That's the quinine”", vs="↔", repere="juxtaposition"),
        "jack": dict(type="liste", titre="Father Jack · pp. 12 – 13", items=[
            "The doctor: Swahili for 25 years, “not that his mind is confused”",
            "Chris: he calls her “Okawa”, his house boy",
            "Kate reassures, Chris sees: Jack has lost his English"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ IV. « Wouldn't it be a good one… »
    dict(id="allons", chap="Let's all go!", fond="nuit", humeur="lumiere",
         retenir="Agnes's “I want to dance” sweeps the sisters along. Rose's wild dance makes Kate panic.", beats=[
        "{mot_ag}Agnes has stopped knitting. She stares into the middle distance. Then she speaks.",
        "{-mot_ag}{elan}The idea catches like fire. {elan.1}Rose would go. {elan.2}Chris loved dancing. "
        "{elan.3}Agnes lends her blue dress and her brown shoes. "
        "{elan.4}Even Kate gives way: are we mad? "
        "{elan.5}A ticket costs four and six. Agnes has five pounds saved, a lot for a woman who knits gloves. "
        "Then the heart of this part.",
        "{-elan}",
        ("C", "I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance.", "c_dance",
         {"voix": "F"}),
        "{-c_dance}{rep}{rep.1}I want to dance, at the start and the end, like a refrain. "
        "{rep.2}In between, two reasons. Lughnasa: the pagan festival, the title of the play. "
        "{rep.3}And her age: time is running out. Pure desire, without excuses.",
        "{-rep}{rose}Kate, wretched, almost agrees. It's settled: all five of us together. "
        "Then Rose sings Abyssinia and starts a bizarre and abandoned dance. And Kate panics.",
        "{-rose}{aby}Outside the text: in 1936, Mussolini's Italy had just invaded Abyssinia, today's Ethiopia. "
        "Even Rose's song brings the outside world into the kitchen.",
    ], vis={
        "mot_ag": dict(type="mot", t="Wouldn't it be a good one if we all went?", g="Agnes · p. 13", y=230, taille=64),
        "elan": dict(type="liste", titre="The idea spreads · pp. 13 – 14", items=[
            "Rose: “I'd go, too, Aggie!”",
            "Chris: “you know how I loved dancing”",
            "Agnes: her blue dress, her brown shoes",
            "Kate: “Maybe we're mad – are we mad?”",
            "“four and six” to get in · “I've five pounds saved”"], marques=["R", "C", "A", "K", "£"], x=150, y=120, w=980),
        "c_dance": dict(type="cit", a="Agnes", o="p. 14", x=170, y=200, w=940),
        "rep": dict(type="liste", titre="Agnes's speech", cles=["refrain"], items=[
            "“I want to dance” … “I want to dance”: a refrain",
            "“the Festival of Lughnasa”: the pagan title",
            "“only thirty-five”: time is running out"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "rose": dict(type="note", cles=["abandoned", "panics"], terme="Stage direction · p. 14",
                     t="Rose does “the first steps of a bizarre and abandoned dance. At this KATE panics.”",
                     etape="Too free, too wild: Kate takes back control.", x=170, y=200, w=940),
        "aby": dict(type="mot", t="“Abyssinia”", g="outside the text: Ethiopia, invaded by Mussolini's Italy in 1935 – 36",
                    y=260, taille=96),
    }),

    # ------------------------------------------------------------------ V. le refus
    dict(id="refus", chap="Kate says no", fond="aube", humeur="tension",
         retenir="Kate's refusal: what people will say, and Father Jack's home. Respectability wins, and silence falls.", beats=[
        "{non}No, no, no! We're going nowhere! And Kate's reasons pour out.",
        "{-non}",
        ("C", "Do you want the whole countryside to be laughing at us? – women of our years? – mature women, dancing?",
         "c_laugh", {"voix": "F"}),
        "{-c_laugh}{ital}Her first fear is not sin, but other people's eyes. "
        "And dancing is in italics: she stresses the word, as if it were shameful.",
        "{-ital}",
        ("C", "And this is Father Jack's home – we must never forget that – ever.", "c_home", {"voix": "F"}),
        "{-c_home}{raisons}Three reasons. {raisons.1}The parish is watching. "
        "{raisons.2}A priest's home must be beyond reproach. "
        "{raisons.3}And Kate even reminded Chris: you have a seven-year-old child. "
        "On page nine, Michael said his birth out of wedlock brought shame on the household. This family cannot afford one more scandal.",
        "{-raisons}{fin}I don't want it mentioned again, says Kate. And the stage direction gives one word.",
        "{-fin}{tab_rad}{q2}But remember the opening: Michael saw these women dancing in this kitchen, screaming like schoolgirls. "
        "The forbidden dance will come back. That is dramatic irony.",
    ], vis={
        "non": dict(type="mot", t="No, no, no!", g="Kate · p. 14", y=260, taille=110),
        "c_laugh": dict(type="cit", a="Kate", o="p. 15", x=170, y=200, w=940),
        "ital": dict(type="mot", t="mature women, dancing?", g="in italics in the text: Kate stresses the word, as if it were shameful", y=260, taille=84),
        "c_home": dict(type="cit", a="Kate", o="p. 15", x=170, y=200, w=940),
        "raisons": dict(type="liste", titre="Kate's reasons", items=[
            "“the whole countryside … laughing at us”: the parish is watching",
            "“Father Jack's home”: a priest's house, beyond reproach",
            "“You have a seven-year-old child”: the shame of an unmarried mother"],
                        marques=["1", "2", "3"], x=150, y=180, w=980),
        "fin": dict(type="mot", t="(Silence.)", g="stage direction · p. 15", y=260, taille=110),
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "q2": dict(type="question", t="The dance she forbids will come back to them."),
    }),

    # ------------------------------------------------------------------ VI. l'analyse
    dict(id="analyse3", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Kate's cracks, the dance as fever, subtext and silence, a watched family: four keys to this scene.", beats=[
        "{b1}Now the analysis. Four ideas. "
        "{b1.1}One: Kate's authority, and its cracks. She provides and decides. "
        "But she blushes, she snaps, she asks: are we mad? Her no is not a lack of desire. It is fear.",
        "{-b1}{b2}{b2.1}Two: the dance as fever and release. A fever in Ballybeg, Agnes's Lughnasa, Rose's abandoned dance. "
        "A pagan energy presses against a Catholic house, right next to Jack's malaria.",
        "{-b2}{b3}{b3.1}Three: subtext and silence. The harvest instead of Austin Morgan, the needles, and a final silence. "
        "What is not said matters as much as what is said.",
        "{-b3}{b4}{b4.1}Four: a fragile, watched family. Little money, an unmarried mother, a sick priest, a countryside ready to laugh. "
        "Respectability is the price of survival.",
        "{-b4}{carte}For your essay, this scene supports four themes. {carte.1}Kate and authority. "
        "{carte.2}The dance and Lughnasa. {carte.3}Subtext and silence. {carte.4}Respectability in nineteen thirties Ireland.",
    ], vis={
        "b1": dict(type="note", cles=["cracks", "fear"], terme="1 · Kate's authority and its cracks",
                   t="She provides and decides; she blushes, snaps, is “wretched”, asks “are we mad?”",
                   etape="Her refusal comes from fear, not from a lack of desire.", x=170, y=200, w=940),
        "b2": dict(type="note", cles=["fever", "pagan"], terme="2 · The dance: fever and release",
                   t="“like a fever in the place”; “It's the Festival of Lughnasa”; “a bizarre and abandoned dance”.",
                   etape="A pagan energy pressing against a Catholic house.", x=170, y=200, w=940),
        "b3": dict(type="note", cles=["subtext", "silence"], terme="3 · Subtext and silence",
                   t="The harvest instead of Austin Morgan; the steel needles; “(Silence.)”",
                   etape="What is not said matters as much as what is said.", x=170, y=200, w=940),
        "b4": dict(type="note", cles=["watched", "Respectability"], terme="4 · A fragile, watched family",
                   t="“four and six”, five pounds saved; an unmarried mother; “the whole countryside”.",
                   etape="Respectability is the price of survival.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE HARVEST DANCE", branches=[
            dict(t="Kate", items=["provider and judge", "the blush, the anger", "“are we mad?”"]),
            dict(t="The dance", items=["“like a fever”", "“the Festival of Lughnasa”", "Rose's “abandoned dance”"]),
            dict(t="Silence", items=["subtext: Austin Morgan", "the steel needles", "“(Silence.)”"]),
            dict(t="Respectability", items=["“laughing at us”", "“Father Jack's home”", "money, shame"])]),
    }),
]

QUIZ = [
    dict(q="What does Kate bring back for the boy?",
         r=["A spinning-top, a whip and a new library book", "A kite and some paint", "A wireless set",
            "A ticket for the harvest dance"], ok=0, voir="arrive",
         ex="She produces “a small, wooden spinning top and whip”, then a new library book “with coloured pictures” (p. 10)."),
    dict(q="When Rose says Kate wanted to see Austin Morgan, Kate first…",
         r=["talks about the harvest in the fields", "admits it at once", "laughs and agrees", "leaves the kitchen"], ok=0,
         voir="dia_am",
         ex="Subtext: she answers with “a good harvest”, but she blushes, and ends with “For God's sake, Rose, shut up, would you!”"),
    dict(q="What does Kate mention right after “like a fever in the place”?",
         r=["The quinine for Father Jack's malaria", "Chris's blue dress", "The price of a ticket", "The fox in the henhouse"],
         ok=0, voir="jux",
         ex="A juxtaposition: the village's “fever” for the dance next to Jack's real fever, malaria (p. 12)."),
    dict(q="Which two reasons does Agnes give for wanting to dance?",
         r=["It's the Festival of Lughnasa, and she is only thirty-five", "Gerry will be there, and it is free",
            "Father Jack asked them to go", "Kate needs a rest, and Rose has a new dress"], ok=0, voir="rep",
         ex="“I want to dance, Kate. It's the Festival of Lughnasa. I'm only thirty-five. I want to dance.” (p. 14)"),
    dict(q="What makes Kate panic and say “No, no, no!”?",
         r=["Rose's “bizarre and abandoned dance”", "News that Jack has disappeared", "Chris crying",
            "The radio breaking down"], ok=0, voir="rose",
         ex="Rose sings “Abyssinia” and starts a wild dance: “At this KATE panics.” (p. 14)"),
    dict(q="Which reasons does Kate give for refusing?",
         r=["The countryside would laugh, and it is Father Jack's home", "They have no dresses and no shoes",
            "The dance is too far away", "Maggie does not want to go"], ok=0, voir="raisons",
         ex="Respectability and religion: “the whole countryside … laughing at us” and “this is Father Jack's home” (p. 15)."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
