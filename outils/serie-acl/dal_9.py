"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 9 : le retour de Gerry (PDF de travail, p. 52-58).

Début : p. 52, didascalie « (CHRIS and GERRY enter L. …) » (juste après « not a syllable! » de Kate).
Fin : p. 58, « AGNES. That's what she said. », juste avant « (MAGGIE enters.) ».
Contenu : le récit de l'engagement de Gerry dans la Brigade internationale, la moto, l'Espagne ; Jack « a new man » et
l'échange des chapeaux ; Kate et le « godless Communism » ; la nouvelle usine de gants de Donegal Town (Vera McLaughlin) ;
Gerry dans le sycomore, l'antenne, la chanson du trapèze ; le retour d'Agnes sans Rose.
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_9. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'Irlande catholique et la guerre d'Espagne, l'origine de la chanson) est dit comme tel.
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-9"
NOTION = "Dancing at Lughnasa"
NUM = 9
TITRE = "Gerry comes back"
SUIVANT = "Part 10 · Rose goes missing"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Armagh": "Ar-mah",
                 "McLaughlin": "Mac-Lochlin", "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}A man climbs to the top of a tree and calls down: from up here, you can see into the future.",
        "{-q1}The audience smiles. Because we can see into the future too: Michael has already told us how this summer ends.",
        "{-tab_don}{serie}Part nine: Gerry comes back. Spain, a factory, a dead branch… and a sister who does not come home.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="From up here, you can see into the future."),
        "serie": dict(type="mot", t="Gerry comes back", g="Spain · the factory · the sycamore · Rose", y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 9", t="Gerry comes back",
                      sous="Spain, the factory, the sycamore · pages 52 – 58"),
    }),

    # ------------------------------------------------------------------ I. une destination
    dict(id="espagne", chap="A named destination", fond="aube", humeur="lumiere",
         retenir="Gerry has joined the International Brigade: a comic story, but a real choice. A man needs “a named destination”.", beats=[
        "{tab_gle}{entree}Kate has just begged Maggie: not a syllable about Jack must leave these walls. "
        "{entree.1}At that moment Chris and Gerry come in, laughing. He keeps trying to embrace her; she keeps avoiding him. "
        "{entree.2}They have danced down the lane and back, without music, just as Michael told us at the end of Act One.",
        "{-entree}{-tab_gle}{recrue}Chris asks about signing up, and Gerry tells it like a comic sketch. "
        "{recrue.1}It happened in a church: a Catholic church, as a matter of interest. "
        "{recrue.2}The recruiting officer was Spanish, he thought. From Armagh, as it turned out. "
        "{recrue.3}Do you speak Spanish? No. Can you make explosives? No. Can you ride a motor-bike? Yes. You're in.",
        "{-recrue}{moto}So he will be a dispatch rider. He mimes the motor-bike. He sails on Saturday. "
        "Everybody says it will be over by Christmas. They always say that, answers Chris. "
        "Keep that motor-bike in mind.",
        "{-moto}{pourquoi}Then the real question: why are you going? Who wants salesmen that can't sell, says Gerry. And then:",
        "{-pourquoi}",
        ("C", "Maybe that's the important thing for a man: a named destination – democracy, Ballybeg, heaven.", "c_dest"),
        "{-c_dest}{drift}Democracy, Ballybeg, heaven: a cause, a village, a religion, all on the same level. "
        "It hardly matters where he goes, as long as the place has a name. "
        "{drift.1}Women, he adds, make better drifters. A strange thing to say in a house where five women can go nowhere at all.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "entree": dict(type="liste", titre="Chris and Gerry come in · pages 52 – 53", items=[
            "He keeps trying to embrace her; she keeps avoiding him",
            "“down the lane and up again – without music”"], marques=["1", "2"], x=150, y=200, w=980),
        "recrue": dict(type="liste", titre="Signing up · page 53", items=[
            "“A Catholic church as a matter of interest.”",
            "“Naturally I thought he was Spanish. From Armagh, as it turned out.”",
            "“Can you ride a motor-bike” “Yes.” “You're in. Sign here.”"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "moto": dict(type="mot", t="a dispatch rider", g="“First tide.” · “it will be over by Christmas” (pp. 53 – 54)",
                     y=250, taille=88),
        "pourquoi": dict(type="note", cles=["sell"], terme="Chris · p. 54",
                         t="“I still don't know why you're going.”",
                         etape="Gerry: “Who wants salesmen that can't sell?”", x=170, y=200, w=940),
        "c_dest": dict(type="cit", a="Gerry", o="p. 54", x=170, y=190, w=940),
        "drift": dict(type="cols", g="Men", gq="need “a named destination”", d="Women",
                      dq="“they make better drifters”", vs="≠", repere="Gerry's view of the sexes"),
    }),

    # ------------------------------------------------------------------ II. le communisme sans Dieu
    dict(id="kate", chap="Godless Communism", fond="nuit", humeur="tension",
         retenir="Two blows from the outside world: Spain divides the kitchen, and the new factory ends Agnes and Rose's work.", beats=[
        "{tab_rad}{antenne}Chris pulls Gerry inside to fix the wireless. I know nothing about radios, he protests. "
        "But he plays the expert: let me check the aerial, then the ignition and sparking plugs. "
        "Those are parts of a car engine! He winks at Chris and goes out.",
        "{-antenne}{-tab_rad}{morale}At once, Kate speaks. It would be on her conscience to stay silent.",
        "{-morale}",
        ("C", "It's a sorry day for Ireland when we send young men off to Spain to fight for godless Communism.", "c_sorry",
         {"voix": "F"}),
        "{-c_sorry}{espagne}Outside the text: in 1936, most of Catholic Ireland, and its Church, sided against the Spanish Republic. "
        "Kate speaks with the voice of her Church.",
        "{-espagne}{reponse}But Chris answers back. {reponse.1}For democracy, Kate. "
        "{reponse.2}I just want to clear my conscience. {reponse.3}That's the important thing, of course. And now you've cleared it. "
        "Pure irony: the youngest sister no longer simply obeys.",
        "{-reponse}{tab_gle2}{vera}Then Chris brings news. Vera McLaughlin, the knitting agent, "
        "is not buying any more of the gloves Agnes and Rose knit at home. Too dear, she says.",
        "{-vera}",
        ("C", "There's a new factory started up in Donegal Town. They make machine gloves more quickly there and far more cheaply.",
         "c_factory", {"voix": "F"}),
        "{-c_factory}{usine}The economic collapse, in two sentences. {usine.1}Buses will take the workers to the factory. "
        "{usine.2}Vera herself was told she was too old. She's forty-one. "
        "{usine.3}Poor Aggie, says Maggie. Poor Rose. What'll they do?",
        "{-usine}{silence}Agnes appears in the garden. Shhh, says Kate. Let them have their tea in peace. Tell them later. "
        "Now there are two secrets in the house: Jack's lost faith, and the end of the knitting.",
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "antenne": dict(type="note", cles=["aerial", "ignition"], terme="Gerry the expert · pp. 54 – 55",
                        t="“Let me check the aerial first. … Then I'll have a look at the ignition and sparking plugs.”",
                        etape="Car words for a radio: he is bluffing.", x=170, y=200, w=940),
        "morale": dict(type="mot", t="“on my conscience”", g="Kate to Christina (p. 55)", y=260, taille=84),
        "c_sorry": dict(type="cit", a="Kate", o="p. 55", x=170, y=190, w=940),
        "espagne": dict(type="note", cles=["Catholic", "Republic"], terme="Outside the text",
                        t="In 1936, most of Catholic Ireland and its Church sided against the Spanish Republic.",
                        etape="Kate speaks with the voice of her Church.", x=170, y=200, w=940),
        "reponse": dict(type="liste", titre="Chris answers back · p. 55", items=[
            "Chris: “For democracy, Kate.”",
            "Kate: “I just want to clear my conscience.”",
            "Chris: “That's the important thing, of course. And now you've cleared it.”"], marques=["C", "K", "C"],
                        x=150, y=180, w=980),
        "tab_gle2": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.2, .4, .5], a=[1.05, .5, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "vera": dict(type="note", cles=["gloves"], terme="Vera McLaughlin, the knitting agent · pp. 55 – 56",
                     t="“She's not buying any more hand-made gloves.”",
                     etape="Kate: “Too dear! She pays them a pittance!”", x=170, y=200, w=940),
        "c_factory": dict(type="cit", a="Chris", o="p. 56", x=170, y=180, w=940),
        "usine": dict(type="liste", titre="The factory · page 56", items=[
            "Buses bring the workers “to the factory and back every day”",
            "Vera: “too old. She's forty-one.”",
            "Maggie: “poor Aggie … poor Rose … what'll they do?”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "silence": dict(type="note", cles=["later"], terme="Kate · p. 56",
                        t="“Shhh. They're back. Let them have their tea in peace. Tell them later.”",
                        etape="A second secret: Jack's faith, and now the knitting.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. le sycomore
    dict(id="sycomore", chap="On top of the sycamore", fond="aube", humeur="mystere",
         retenir="Gerry in the tree, “into the future”: comedy full of dramatic irony. Then Agnes asks: where is Rose?", beats=[
        "{tab_don2}{appel}{appel.1}Agnes comes back with two pails of bilberries. A voice calls: Who is that beautiful woman! "
        "{appel.2}It's Gerry, on top of the sycamore. Agnes sees him; we, the audience, do not. "
        "What are you doing up there?",
        "{-appel}",
        ("C", "You can see into the future from here, Aggie!", "c_future"),
        "{-c_future}{-tab_don2}{ironie}A joke… and perfect dramatic irony. "
        "{ironie.1}He adds: come up and see what's going to happen to you! "
        "{ironie.2}But we already know: in early September, Agnes and Rose will leave for ever. "
        "And we have just heard why: the factory.",
        "{-ironie}{cirque}The branch is dead, warns Agnes. It sways. {cirque.1}Gerry sings: He flies through the air with the greatest of ease. "
        "{cirque.2}Outside the text: an old music-hall song from the eighteen-sixties. "
        "{cirque.3}Agnes covers her eyes. You're going to fall! I'm not looking! I'm not watching!",
        "{-cirque}{clown}She runs inside: he's going to break his neck! As long as he fixes the wireless first, says Maggie. "
        "Even fear becomes a joke in this house. And notice how much Agnes cares about Gerry.",
        "{-clown}{mures}{mures.1}The bilberries? Just that bit too ripe. We should have picked them a week ago. "
        "Like these women's lives: always a little too late. "
        "{mures.2}Then Agnes asks: is Rosie still in bed? She wasn't feeling well. She went home to lie down. A pause.",
        "{-mures}",
        ("C", "She's here, isn't she?", "c_here", {"voix": "F"}),
        "{-c_here}{fuite}No one has seen her. {fuite.1}Maggie rushes to the bedroom. "
        "{fuite.2}Rose left Agnes hours ago, at the old quarry. She felt out of sorts. "
        "{fuite.3}She went off alone? To come home? That's what she said. "
        "Part nine stops here.",
    ], vis={
        "tab_don2": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.15, .4, .5], a=[1.3, .6, .5],
                         legende="Donegal (photo dconvertini, CC BY-SA 4.0)"),
        "appel": dict(type="liste", titre="A voice off · page 56", items=[
            "Gerry: “Who is that beautiful woman!”",
            "“On top of the sycamore.” The audience does not see him."], marques=["1", "2"], x=150, y=200, w=980),
        "c_future": dict(type="cit", a="Gerry", o="p. 56", x=170, y=200, w=940),
        "ironie": dict(type="liste", titre="Dramatic irony", cles=["irony"], items=[
            "Gerry: “Come up and see what's going to happen to you!”",
            "Act One: “both Rose and Agnes would have left for ever”"], marques=["1", "2"], x=150, y=200, w=980),
        "cirque": dict(type="liste", titre="The circus · pages 56 – 57", items=[
            "“He flies through the air with the greatest of ease –”",
            "Outside the text: a music-hall song of the 1860s",
            "Agnes: “You're going to fall! I'm not looking! I'm not watching!”"], marques=["♪", "+", "A"],
                       x=150, y=180, w=980),
        "clown": dict(type="dialogue", lignes=["Agnes: “He's going to break his neck – I'm telling you!”",
                                               "Maggie: “As long as he fixes the wireless first.”"],
                      src="The kitchen · p. 57", x=170, y=200, w=980),
        "mures": dict(type="liste", titre="Back from the quarry · page 57", items=[
            "“Just that bit too ripe. We should have picked them a week ago.”",
            "“She left me and went home to lie down.”"], marques=["1", "2"], x=150, y=200, w=980),
        "c_here": dict(type="cit", a="Agnes", o="p. 57", x=170, y=220, w=940),
        "fuite": dict(type="liste", titre="Where is Rose? · pages 57 – 58", items=[
            "Maggie rushes off to the bedroom",
            "“almost immediately after we got to the old quarry”",
            "“To come home?” “That's what she said.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ------------------------------------------------------------------ IV. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Gerry the drifter, the outside world breaking in, dramatic irony, and comedy that turns to fear.", beats=[
        "{a1}Now the analysis. Four ideas. "
        "{a1.1}One: Gerry the drifter. Dancing teacher, gramophone salesman, now a soldier: he moves freely, the sisters cannot. "
        "Useful for an essay on gender: men leave, women stay and wait.",
        "{-a1}{a2}{a2.1}Two: the outside world breaks in. History, with the Spanish war and the Church's view of it. "
        "Industry, with machines and buses. Kate answers both with silence: tell them later. But silence stops nothing.",
        "{-a2}{a3}{a3.1}Three: dramatic irony and foreshadowing. Only the audience can really see into the future. "
        "And the motor-bike? On page sixty-four, Michael tells us Gerry was wounded in Barcelona: he fell off his motor-bike. "
        "You're going to fall, cried Agnes.",
        "{-a3}{a4}{a4.1}Four: comedy turning to fear. A farce, a clown in a tree, a circus song… "
        "then the end of the sisters' work, and a sister who has not come home. The tone is tragicomic: the laughter makes the loss sharper.",
        "{-a4}{carte}Here is part nine for your essay. {carte.1}Gerry the drifter. {carte.2}The outside world. "
        "{carte.3}Dramatic irony. {carte.4}And laughter and fear, side by side.",
    ], vis={
        "a1": dict(type="note", cles=["drifter", "destination"], terme="1 · Gerry the drifter",
                   t="“a named destination – democracy, Ballybeg, heaven”: any cause will do.",
                   etape="Men leave; the women stay and wait.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["History", "industry"], terme="2 · The outside world breaks in",
                   t="Spain and “godless Communism”; a factory that makes gloves “far more cheaply”.",
                   etape="Kate answers with silence: “Tell them later.”", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["irony", "foreshadowing"], terme="3 · Seeing into the future",
                   t="“You can see into the future from here”: only the audience really can.",
                   etape="The motor-bike; “You're going to fall!”; p. 64: wounded in Barcelona.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["tragicomic"], terme="4 · Comedy turning to fear",
                   t="A farce, a clown in a tree, a circus song… then “She's here, isn't she?”",
                   etape="A tragicomic tone: laughter makes the loss sharper.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="GERRY COMES BACK", branches=[
            dict(t="The drifter", items=["“a named destination”", "“better drifters”", "a dispatch rider"]),
            dict(t="Outside world", items=["“godless Communism”", "the factory", "“Tell them later”"]),
            dict(t="Dramatic irony", items=["“into the future”", "the motor-bike", "“left for ever”"]),
            dict(t="Tone", items=["a clown in a tree", "the circus song", "“She's here, isn't she?”"])]),
    }),
]

QUIZ = [
    dict(q="Where, according to Gerry, did he sign up for the International Brigade?",
         r=["In a Catholic church", "In a pub in Ballybeg", "On a ship to Spain", "In the district commissioner's office"], ok=0,
         voir="recrue",
         ex="“A Catholic church as a matter of interest”: a comic irony, since Kate calls the cause “godless Communism”."),
    dict(q="Why is Gerry accepted, in his story?",
         r=["He can ride a motor-bike", "He speaks Spanish", "He can make explosives", "He is a Communist"], ok=0, voir="recrue",
         ex="He answers “No” to everything else; “Can you ride a motor-bike” “Yes.” “You're in.” He will be a dispatch rider."),
    dict(q="What does Gerry say is “the important thing for a man”?",
         r=["A named destination", "A steady job", "A family", "A good conscience"], ok=0, voir="c_dest",
         ex="“a named destination – democracy, Ballybeg, heaven”: for Gerry, any cause will do, as long as it has a name."),
    dict(q="Why will Vera McLaughlin stop buying the sisters' gloves?",
         r=["A new factory in Donegal Town makes machine gloves faster and cheaper", "The gloves are badly made",
            "Kate has quarrelled with her", "She is moving to England"], ok=0, voir="c_factory",
         ex="Industrialisation reaches Ballybeg: Agnes and Rose lose their only income. Kate decides to “tell them later”."),
    dict(q="What is the dramatic irony of “You can see into the future from here, Aggie!”?",
         r=["The audience already knows Agnes and Rose will leave for ever", "Gerry really is a fortune-teller",
            "Agnes knows Gerry is lying", "It tells us the wireless will never work"], ok=0, voir="c_future",
         ex="Michael's prolepsis at the end of Act One told us that both Rose and Agnes would leave in early September."),
    dict(q="How does part nine end?",
         r=["Agnes comes back alone and asks if Rose is in the house", "Gerry falls from the sycamore",
            "Kate tells Agnes about the factory", "Jack says Mass in the kitchen"], ok=0, voir="c_here",
         ex="Rose left Agnes at the old quarry hours ago: “She's here, isn't she?” No one has seen her."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
