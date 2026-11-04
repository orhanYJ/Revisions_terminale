"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 6 : Gerry Evans (PDF de travail, p. 25-37).

De l'arrivée de Gerry (Maggie à la fenêtre, p. 25) jusqu'à la sortie d'Agnes en larmes (début de la p. 37) ;
la confidence de Kate à Maggie (« hair cracks », p. 37) ouvre la partie 7.
Vidéo en anglais, même chaîne que les séries philo : outils/serie-philo/generer.py dal_6.
Citations courtes, à fin d'analyse ; le contexte hors texte (guerre d'Espagne)
et les révélations ultérieures de Michael (p. 64) sont dits comme tels.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-6"
NOTION = "Dancing at Lughnasa"
NUM = 6
TITRE = "Gerry Evans"
SUIVANT = "Part 7 · Cracks"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ballybeg": "Bally-beg", "Oughterard": "Ooh-ter-ard",
                 "Mundy": "Mundy", "Chrissie": "Chrissie", "Sligo": "Sly-go"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_lane}{q1}A man in a straw hat comes up the lane, swinging his cane. In the kitchen, five women panic.",
        "{-q1}{qui}He is Gerry Evans, Michael's father. Part six: his visit, his patter, and a dance in the garden.",
        ("P", 0.3),
        "{-qui}{-tab_lane}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_lane": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "q1": dict(type="question", t="Look who's coming up the lane!"),
        "qui": dict(type="mot", t="Gerry Evans", g="Michael's father · Chris's lover · Kate's “creature”", y=270, taille=96),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 6", t="Gerry Evans",
                      sous="The visit, the patter, the dance · pages 25 – 37"),
    }),

    # ------------------------------------------------------------------ I. le chaos dans la cuisine
    dict(id="chaos", chap="Chaos in the kitchen", fond="aube", humeur="tension",
         retenir="Gerry's arrival throws the house into chaos. Kate moves from orders to tenderness… and back to the rules.", beats=[
        "{tab_cot}{lane}Part five ended in the middle of a row, when Maggie ran to the window. Look who's coming up the lane! "
        "It's Gerry Evans.",
        "{-lane}{-tab_cot}{chaos}Pure chaos. {chaos.1}Everybody dashes about: mirror, shoes, hair. "
        "{chaos.2}The lines overlap. {chaos.3}Agnes knits with excessive concentration. "
        "{chaos.4}And Chris stands absolutely still, too shocked to move.",
        "{-chaos}{ordres}Kate takes command: meet him outside, and send him packing. "
        "But Chris is about to cry. So Kate takes her in her arms.",
        "{-ordres}",
        ("C", "Of course ask him in. And give the creature his tea. And stay the night if he wants to. But in the outside loft. "
              "And alone.", "c_tea", {"voix": "F"}),
        "{-c_tea}{deux}Listen to the turn. First, tenderness. Then, firm again: the outside loft, and alone. "
        "Kate loves her sister, but respectability comes first. And creature: she will not even say his name.",
        "{-deux}{entree}{entree.1}Gerry enters: a jaunty step, a cane, a straw hat. "
        "{entree.2}Friel adds: he knows he is being watched. "
        "{entree.3}He is very ill at ease, but the smile never leaves his face.",
    ], vis={
        "tab_cot": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.2, .4, .5], a=[1.05, .5, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "lane": dict(type="mot", t="“Look who's coming up the lane!”", g="Maggie, at the window · p. 25", y=250, taille=76),
        "chaos": dict(type="liste", titre="Stage direction · p. 25", cles=["overlap", "still"], items=[
            "Everybody dashes about: mirror, shoes, hair",
            "They talk over each other: the lines overlap",
            "Agnes knits with “excessive concentration”",
            "Chris stands absolutely still, too shocked to move"], marques=["1", "2", "3", "4"], x=150, y=140, w=980),
        "ordres": dict(type="note", cles=["packing"], terme="Kate's orders · p. 27",
                       t="“And then you'll send him packing”",
                       etape="Chris does not move. She is about to cry.", x=170, y=200, w=940),
        "c_tea": dict(type="cit", a="Kate", o="p. 27", x=170, y=170, w=940),
        "deux": dict(type="cols", g="Tenderness", gq="“Of course ask him in”", d="The rules",
                     dq="“in the outside loft. And alone.”", vs="→", repere="love / respectability"),
        "entree": dict(type="liste", titre="Gerry's entrance · p. 27", cles=["watched"], items=[
            "A jaunty step, a cane, a straw hat",
            "“He knows he is being watched”",
            "Very ill at ease… but the smile never leaves his face"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ II. le baratin de Gerry
    dict(id="patter", chap="Gerry's patter", fond="nuit", humeur="lumiere",
         retenir="Gerry's talk is a performance: lies, boasts and omens that Chris, and the audience, can see through.", beats=[
        "{dia}His first question gives him away. {dia.1}How have you been for the past six months? "
        "{dia.2}Thirteen months, says Chris. {dia.3}July the seventh. She has counted. He has not.",
        "{-dia}{recits}Then comes his patter, a flood of charming talk. "
        "{recits.1}His visit was pure luck: a lift from a man in a bar in Sligo. "
        "{recits.2}He gave dancing lessons in Dublin: thousands of pupils, millions! Then, in the same breath:",
        "{-recits}",
        ("C", "Fifty-three. I'm a liar. Fifty-one.", "c_liar"),
        "He says it himself, with a smile. Gerry exaggerates, corrects himself, and charms us because he knows we know.",
        "{-c_liar}{ventes}{ventes.1}His new career: gramophone salesman. A customer took four, he says. "
        "Four gramophones? No: four brochures. They both laugh. "
        "{ventes.2}And a bicycle for his son? They only had it in blue. So, no bicycle. Not this time.",
        "{-ventes}{bush}Then: don't turn round. Michael is watching them from behind a bush. "
        "Our narrator, as a child, hidden, observing his father.",
        "{-bush}{omens}Then the omens. A cow with a single horn: a unicorn, laughs Chris. A good omen, says Gerry. "
        "Then a single magpie: one for sorrow. Gerry lives by chance, not by plans. "
        "And that magpie quietly foreshadows how this visit will end.",
    ], vis={
        "dia": dict(type="dialogue", lignes=["“And how have you been for the past six months?”", "“Thirteen months.”",
                                             "“July last year; July the seventh.”"],
                    src="Gerry and Chris · p. 28 (extracts)", x=170, y=110, w=980),
        "recits": dict(type="liste", titre="Gerry's stories · p. 28 – 30", items=[
            "A lucky lift from a bar in Sligo",
            "Dancing lessons in Dublin: “thousands of pupils – millions!”"], marques=["1", "2"], x=150, y=200, w=980),
        "c_liar": dict(type="cit", a="Gerry", o="p. 30", x=170, y=200, w=940),
        "ventes": dict(type="liste", titre="More stories · p. 30 – 31", items=[
            "“Minerva Gramophones – The Wise Buy”… four brochures",
            "A bicycle for Michael… but only in blue"], marques=["3", "4"], x=150, y=200, w=980),
        "bush": dict(type="note", cles=["watching"], terme="Gerry to Chris · p. 31",
                     t="“he's watching us from behind that bush”",
                     etape="The narrator, as a child, spying on his own father.", x=170, y=200, w=940),
        "omens": dict(type="cols", g="The one-horned cow", gq="“a good omen”… and it winked", d="The single magpie",
                      dq="“one for sorrow”", vs="≠", repere="good luck / bad luck · p. 32 – 33"),
    }),

    # ------------------------------------------------------------------ III. les spectatrices de la cuisine
    dict(id="watchers", chap="The watchers in the kitchen", fond="aube", humeur="tension",
         retenir="A split stage: we watch Gerry and Chris, and we watch the sisters watching them.", beats=[
        "{split}Look at the staging. In the garden, Gerry and Chris. In the kitchen, the sisters at the window, "
        "watching and commenting. A split stage: two scenes, cut together like a film.",
        "{-split}{voix}{voix.1}Maggie is kind: the poor fella. "
        "{voix.2}Agnes will not look: not just now. {voix.3}Kate counts: I'll give him three minutes.",
        "{-voix}{toff}Chris looks at him, says Maggie, as if he were the biggest toff in the world. Kate explodes.",
        "{-toff}",
        ("C", "Tinker, more likely! Loafer! Wastrel!", "c_tinker", {"voix": "F"}),
        "{-c_tinker}{insultes}{insultes.1}A tinker: a wanderer with no home. {insultes.2}A loafer: an idler. "
        "{insultes.3}A wastrel: a good-for-nothing. Social contempt: Kate judges by respectability.",
        "{-insultes}{spain}Then Gerry's news. {spain.1}He is going to Spain, with the International Brigade. "
        "{spain.2}Context, from outside the play: the Spanish Civil War broke out in July nineteen thirty-six. "
        "{spain.3}Volunteers from many countries went to fight for the Republic, against Franco. "
        "{-spain}Why does Gerry go?",
        ("C", "Give Evans a Big Cause and he won't let you down. It's only everyday stuff he's not so successful at.", "c_cause"),
        "{-c_cause}{cause}His most honest line. A big cause, yes. Everyday duty, a son behind a bush: no. "
        "With Gerry, the outside world walks into Ballybeg.",
    ], vis={
        "split": dict(type="cols", g="The garden", gq="Gerry performs, Chris laughs", d="The kitchen",
                      dq="the sisters watch and comment", vs="↔", repere="a split stage"),
        "voix": dict(type="liste", titre="The voices at the window · p. 28", items=[
            "Maggie: “Looks terrified, the poor fella.”",
            "Agnes: “Not just now.”",
            "Kate: “I'll give him three minutes.”"], marques=["M", "A", "K"], x=150, y=180, w=980),
        "toff": dict(type="mot", t="“the biggest toff in the world”", g="Maggie, about the way Chris looks at him · p. 31",
                     y=250, taille=76),
        "c_tinker": dict(type="cit", a="Kate", o="p. 31", x=170, y=200, w=940),
        "insultes": dict(type="liste", titre="Kate's verdict", cles=["contempt"], items=[
            "Tinker: a wanderer, no home, no standing",
            "Loafer: an idler",
            "Wastrel: a good-for-nothing"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "spain": dict(type="liste", titre="Spain · p. 33", items=[
            "Gerry will join “the International Brigade”",
            "Context: the Spanish Civil War began in July 1936",
            "Context: foreign volunteers fought for the Republic, against Franco"],
                      marques=["1", "✻", "✻"], x=150, y=180, w=980),
        "c_cause": dict(type="cit", a="Gerry", o="p. 33", x=170, y=200, w=940),
        "cause": dict(type="cols", g="A Big Cause", gq="Spain, fighting, adventure", d="Everyday stuff",
                      dq="a son, a home, ordinary duty", vs="≠", repere="the outside world arrives"),
    }),

    # ------------------------------------------------------------------ IV. la danse dans le jardin
    dict(id="danse", chap="A dance in the garden", fond="nuit", humeur="lumiere",
         retenir="The dance says what words cannot. The sisters' reactions reveal Kate's buried tenderness and Agnes's hidden pain.", beats=[
        "{tab_rad}{radio}{radio.1}Suddenly the radio plays. Agnes didn't touch it. "
        "{radio.2}Turn that thing off, says Kate. Agnes does not.",
        "{-radio}{chanson}Your text simply says: an appropriate song of the period. "
        "What matters is not the title, but the timing: for once, the radio works, just for them.",
        "{-chanson}{-tab_rad}{agnes_g}And twice, Gerry asks after one sister: Agnes. "
        "She was the one, he says, that seemed to object least to me.",
        "{-agnes_g}{watch}He takes Chris in his arms. {watch.1}They're watching us. {watch.2}Hope so. And Kate. "
        "{watch.3}And Father Jack. {watch.4}Better still! Even his romance is a show.",
        "{-watch}{cuisine}{cuisine.1}In the kitchen: they're dancing. The animal! cries Kate. "
        "{cuisine.2}Agnes, asked to look, snaps: I'm busy! "
        "{cuisine.3}And Kate, at the window, slowly changes.",
        "{-cuisine}",
        ("C", "Her whole face alters when she's happy, doesn't it? They dance so well together. They're such a beautiful couple.",
         "c_face", {"voix": "F"}),
        "From the animal to a beautiful couple. Under the judgement, love. "
        "{-c_face}{bernie}Then: as beautiful as Bernie O'Donnell, Maggie's old friend from the dance competition. "
        "Maggie leaves the window and sits motionless.",
        "{-bernie}{prop}{prop.1}Gerry proposes. Marry me, Chrissie. {prop.2}I don't think so. "
        "{prop.3}You'd walk out on me again: that's your nature. And then:",
        "{-prop}",
        ("C", "Don't talk any more; no more words. Just dance me down the lane and then you'll leave.", "c_lane", {"voix": "F"}),
        "Chris knows who he is, and chooses the dance anyway. "
        "{-c_lane}{minutes}They dance off. The music stops in mid-phrase. "
        "That's all it seems to last, says Maggie: a few minutes at a time.",
        "{-minutes}{agnes}Kate goes back to her verdict: Christina's heart gets crushed again. "
        "And Agnes, almost silent until now, explodes: a damned righteous bitch, she calls her. His name is Gerry! "
        "Close to tears, she runs off, leaving Kate and Maggie alone. Part six ends there, at the top of page thirty-seven.",
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "radio": dict(type="liste", titre="The radio · p. 34", items=[
            "It starts playing: Agnes “didn't touch it”",
            "Kate: “Turn that thing off”… Agnes does not"], marques=["1", "2"], x=150, y=200, w=980),
        "chanson": dict(type="mot", t="“an appropriate song of the period”", g="your text names no title: what matters is the timing (p. 34)",
                        y=250, taille=84),
        "agnes_g": dict(type="note", cles=["Agnes"], terme="Gerry · p. 34",
                        t="“Of all your sisters Agnes was the one that seemed to object least to me.”",
                        etape="Already on p. 29: “Tell her I was asking for her – Agnes.”", x=170, y=200, w=940),
        "watch": dict(type="dialogue", lignes=["“They're watching us.”", "“Hope so. And Kate.”", "“And Father Jack.”",
                                               "“Better still! Terrific!”"],
                      src="Chris and Gerry · p. 35 (extracts)", x=170, y=90, w=980),
        "cuisine": dict(type="liste", titre="At the kitchen window · p. 35", items=[
            "Maggie: “They're dancing.”  Kate: “The animal!”",
            "Agnes: “I'm busy!”",
            "Kate, at the window, slowly softens"], marques=["M", "A", "K"], x=150, y=180, w=980),
        "c_face": dict(type="cit", a="Kate", o="p. 35", x=170, y=170, w=940),
        "bernie": dict(type="note", cles=["motionless"], terme="Kate · p. 35",
                       t="“She's as beautiful as Bernie O'Donnell any day, isn't she?”",
                       etape="Maggie sits motionless: her own lost youth comes back.", x=170, y=200, w=940),
        "prop": dict(type="dialogue", lignes=["“Marry me, Chrissie.”", "“I don't think so, Gerry.”",
                                              "“But you'd walk out on me again.”"],
                     src="Gerry and Chris · p. 35 – 36 (extracts)", x=170, y=110, w=980),
        "c_lane": dict(type="cit", a="Chris", o="p. 36", x=170, y=170, w=940),
        "minutes": dict(type="note", cles=["minutes"], terme="Maggie, about the radio · p. 36",
                        t="“that's all it seems to last – a few minutes at a time”",
                        etape="Like the radio, like Gerry's visits: happiness never lasts.", x=170, y=200, w=940),
        "agnes": dict(type="note", cles=["Gerry"], terme="Agnes · p. 36",
                      t="“And his name is Gerry! – Gerry! Gerry!”",
                      etape="The quiet sister breaks her silence, then runs off in tears.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Gerry the performer, the watchers in the kitchen, the dance as escape, and the subtext of Agnes and Kate.", beats=[
        "{a1}Now the analysis. Four ideas. One: Gerry is a performer. He knows he is being watched, and everything is a show. "
        "His charm is unreliable, and we see through it.",
        "Dramatic irony too: on page sixty-four, Michael reveals that Gerry had a wife and three children in Wales. "
        "So much for: Wales isn't my home any more.",
        "{-a1}{a2}Two: the watchers. The split stage makes the sisters an audience inside the play, almost a chorus. "
        "We watch them watching, and their comments reveal them more than Gerry.",
        "{-a2}{a3}Three: the dance. Chris and Gerry cannot talk honestly, but they can dance: courtship and escape, "
        "beyond words. But it is brief, like happiness in this house. And Chris's joy comes with humiliation, "
        "in front of her sisters.",
        "{-a3}{a4}Four: subtext. Agnes never says she loves Gerry. But she will not look, she snaps, she defends his name. "
        "This is subtext, not a stated fact: write that her reactions suggest a secret attachment.",
        "{-a4}{carte}So, this part can support essays on {carte.1}performance and truth, {carte.2}watching and judging, "
        "{carte.3}dance as escape, {carte.4}and the outside world breaking into Ballybeg.",
    ], vis={
        "a1": dict(type="note", cles=["performer", "unreliable"], terme="1 · Gerry, the performer",
                   t="“He knows he is being watched”: six months for thirteen, “I'm a liar”, four brochures.",
                   etape="Unreliable charm, and dramatic irony: his family in Wales (p. 64).", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["split", "chorus"], terme="2 · The watchers",
                   t="A split stage: the garden performs, the kitchen comments, like a chorus.",
                   etape="We watch the sisters watching. Michael watches too.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["words", "escape"], terme="3 · The dance",
                   t="“no more words. Just dance me down the lane”",
                   etape="Courtship and escape… “a few minutes at a time”.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["subtext"], terme="4 · Subtext",
                   t="Agnes: “Not just now”, “I'm busy!”, “his name is Gerry!”",
                   etape="Never said: Agnes's feelings. Kate's tenderness under her anger.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="GERRY'S VISIT", branches=[
            dict(t="Performance", items=["“He knows he is being watched”", "“I'm a liar”", "irony: Wales (p. 64)"]),
            dict(t="Watching", items=["a split stage", "the kitchen as chorus", "Michael behind the bush"]),
            dict(t="The dance", items=["“no more words”", "courtship and escape", "“a few minutes at a time”"]),
            dict(t="Outside world", items=["Spain, the International Brigade", "gramophones, the radio", "Kate's respectability"])]),
    }),
]

QUIZ = [
    dict(q="How long has it been since Gerry's last visit?",
         r=["Thirteen months, though he says six", "Six months, as he says", "Two weeks", "Seven years"], ok=0, voir="dia",
         ex="Gerry asks about “the past six months”; Chris corrects him: “Thirteen months… July the seventh.” She counts, he does not."),
    dict(q="What does Kate finally allow Gerry to do?",
         r=["Have his tea and stay the night, but in the outside loft, alone", "Marry Chris at once",
            "Take Michael to Wales", "Nothing: she throws him out herself"], ok=0, voir="c_tea",
         ex="Tenderness first (“Of course ask him in”), then the rules: “But in the outside loft. And alone.”"),
    dict(q="Who is watching Gerry and Chris from behind a bush?",
         r=["Michael, their son", "Father Jack", "Rose", "Kate"], ok=0, voir="bush",
         ex="“Don't turn round; but he's watching us from behind that bush.” The future narrator observes his father."),
    dict(q="Why is Gerry going to Spain?",
         r=["To fight with the International Brigade", "To sell gramophones", "To find work as a dance teacher",
            "To visit his family"], ok=0, voir="spain",
         ex="“to do a spot of fighting. With the International Brigade.” Context: the Spanish Civil War began in July 1936."),
    dict(q="How does Chris answer Gerry's proposal?",
         r=["“Just dance me down the lane and then you'll leave.”", "She says yes, for after his return",
            "She asks Kate's permission", "She runs into the house"], ok=0, voir="c_lane",
         ex="She refuses (“you'd walk out on me again”) but chooses the dance: “no more words”."),
    dict(q="What do Agnes's reactions in this part suggest?",
         r=["A hidden attachment to Gerry: subtext, never stated", "That she hates music",
            "That she wants to marry Father Jack", "Nothing: she is not on stage"], ok=0, voir="a4",
         ex="She refuses to look, snaps “I'm busy!”, defends “his name is Gerry!” and runs off in tears."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Glenties (Thpohl, public domain); valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
