"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 12 : « The last afternoon » (PDF de travail, p. 64-74).

Début : p. 64, juste après la didascalie « MICHAEL exits » (Chris appelle Gerry, perché dans le sycomore).
Fin : p. 74, juste avant « (MAGGIE moves into the kitchen. MICHAEL enters. …) » (la devinette oubliée de Maggie).
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_12. Citations courtes, à fin d'analyse ; le reste est résumé.
Les paroles de la chanson (« Anything Goes », nommée p. 66) ne sont pas citées. Ce qui ne vient pas du texte
(Cole Porter, 1934) est dit comme tel. La perte de l'emploi de Kate n'est pas annoncée dans ces pages : elle n'est
rappelée que par la prolepse de Michael (p. 43).
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-12"
NOTION = "Dancing at Lughnasa"
NUM = 12
TITRE = "The last afternoon"
SUIVANT = "Part 13 · The final tableau"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Okawa": "Oh-kah-wa",
                 "McLaughlin": "Mac-Lock-lin", "Pius": "Pie-us", "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Michael has just told us how every one of them will end. And then the light comes back… "
        "on one more warm afternoon.",
        "{-q1}We watch it the way Michael remembers it: knowing that it is the last.",
        "{-tab_don}{serie}Part twelve: a radio that comes and goes, one more dance, a dead rooster, "
        "an exchange of hats… and the kites, at last.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="One more warm afternoon… the last."),
        "serie": dict(type="mot", t="The last afternoon", g="the radio · a dance · a rooster · two hats · the kites",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 12", t="The last afternoon",
                      sous="Act Two · pages 64 – 74"),
    }),

    # ------------------------------------------------------------------ I. le sycomore
    dict(id="sycomore", chap="On the sycamore", fond="aube", humeur="lumiere",
         retenir="Maggie's plans and Jack's “system”: comedy on the surface, the end already visible underneath.", beats=[
        "{tab_gle}{debut}The sisters go back to their tasks. {debut.1}Gerry is up the sycamore tree, fixing the aerial. "
        "We never made love on top of a sycamore tree, he calls down. Chris looks round: did her sisters hear?",
        "{debut.2}Maggie has a brilliant idea: Agnes, with her clever hands, should be a dressmaker. "
        "No more ruining her eyes on grey wool. {debut.3}But remember part eleven: Vera McLaughlin will soon stop buying "
        "the gloves. We know the plan will never happen.",
        "{-debut}{-tab_gle}{jack}Then Jack comes in through the garden. {jack.1}In Ryanga, he says, he could find one husband "
        "for all four of you. {jack.2}One principal wife, the others in his enclosure. "
        "{jack.3}A small commune, where everybody helps everybody. I'm completely in favour of it.",
        "Kate has heard enough.",
        "{-jack}",
        ("C", "It may be efficient and you may be in favour of it, Jack, but I don't think it's what Pope Pius XI "
              "considers to be the holy sacrament of matrimony.", "c_pius", {"voix": "F"}),
        "{-c_pius}{pius}The Pope against Ryanga. {pius.g}Kate stands for Rome and the sacrament. "
        "{pius.d}Jack, she adds, pays too much attention to the Great Goddess… Iggie. "
        "And here is the dramatic irony: Michael told us that Kate will lose her job more because of Jack "
        "than because of falling numbers. His pagan talk is already costing her.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "debut": dict(type="liste", titre="The afternoon begins · pages 64 – 65", items=[
            "Gerry up the sycamore: “We never made love on top of a sycamore tree.”",
            "Maggie: Agnes should be a dressmaker, not stare at “grey wool”",
            "Dramatic irony: the glove work is about to end"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "jack": dict(type="liste", titre="Jack's “system” · pages 65 – 66", items=[
            "“one husband for all of you”",
            "a “principal wife”, the others “in his enclosure”",
            "“a small commune where everybody helps everybody”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_pius": dict(type="cit", a="Kate", o="p. 66", x=170, y=190, w=940),
        "pius": dict(type="cols", g="Kate", gq="Pope Pius XI, “the holy sacrament of matrimony”", d="Jack",
                     dq="“the Great Goddess … Iggie”", vs="≠", repere="Rome / Ryanga"),
    }),

    # ------------------------------------------------------------------ II. Anything Goes
    dict(id="danse", chap="Anything Goes", fond="aube", humeur="lumiere",
         retenir="Gerry dances with Agnes, Chris watches, then switches the radio off: a dance cut short.", beats=[
        "{tab_rad}{song}Gerry has fixed the radio. Very softly, it plays a song the text names: Anything Goes. "
        "Outside the text: a Cole Porter song from 1934, American, modern, a little daring.",
        "{-song}{ag}Gerry asks Agnes to dance. {ag.1}Have a bit of sense, she says. But he pulls her to her feet. "
        "{ag.2}With style and with easy elegance, they dance round the kitchen and out into the garden. "
        "{ag.3}You should be a professional dancer, he tells her. Too late for that, she answers.",
        "{-ag}{-tab_rad}{fenetre}{fenetre.1}Then he kisses her on the forehead. Chris sees it from the kitchen window… "
        "but she cannot hear. {fenetre.2}When Gerry turns to her, now Chrissie, she snaps: Not now. Are you thick?",
        "{-fenetre}{maggie}Maggie kicks off her Wellingtons. Shirley Temple needs a lot of space! "
        "She and Gerry sing and dance… {maggie.1}and Chris suddenly turns the radio off. Sick of that damned thing. "
        "We're only wasting the battery.",
        "Kate, of course, is delighted.",
        "{-maggie}",
        ("C", "Peace, thanks be to God! D'you know what that thing has done? Killed all Christian conversation in this country.",
         "c_radio", {"voix": "F"}),
        "{-c_radio}{silence}For Kate, the radio is the enemy of the Church. For Chris, it is Gerry's music, "
        "and it hurts. Two reasons, one silence. Joy has become a source of jealousy.",
    ], vis={
        "tab_rad": dict(type="tableau", img="dal-radio", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="A 1930s valve wireless set (Museo della scienza e della tecnologia, Milan, CC BY-SA 4.0)"),
        "song": dict(type="note", cles=["Anything", "1934"], terme="Stage direction · p. 66",
                     t="Music of “Anything Goes” very softly on the radio.",
                     etape="Outside the text: Cole Porter, 1934.", x=170, y=200, w=940),
        "ag": dict(type="liste", titre="Gerry and Agnes · pages 67 – 68", items=[
            "Agnes: “Have a bit of sense, Gerry Evans.”",
            "“With style and with easy elegance they dance”",
            "“You should be a professional dancer.” “Too late for that.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "fenetre": dict(type="liste", titre="Seen, not heard · page 68", items=[
            "A kiss on the forehead, seen by Chris at the window",
            "Chris: “Not now, I said. Are you thick?”"], marques=["1", "2"], x=150, y=210, w=980),
        "maggie": dict(type="note", cles=["damned", "battery"], terme="Maggie dances · p. 69",
                       t="Chris turns the radio off: “Sick of that damned thing.”",
                       etape="“We're only wasting the battery.”", x=170, y=200, w=940),
        "c_radio": dict(type="cit", a="Kate", o="p. 69", x=170, y=190, w=940),
        "silence": dict(type="cols", g="Kate", gq="the radio kills “Christian conversation”", d="Chris",
                        dq="jealous: Gerry danced with Agnes", vs="+", repere="one silence, two reasons"),
    }),

    # ------------------------------------------------------------------ III. le coq
    dict(id="coq", chap="The fox", fond="nuit", humeur="tension",
         retenir="Rose brings in her dead white rooster, calm: a sacrifice-like image on the last day of Lughnasa.", beats=[
        "{tab_gle2}{vera}Chris, icily, tells Agnes: Vera McLaughlin is calling tomorrow, to talk to you and Rose. "
        "{vera.1}Kate quickly changes the subject: Vera's daughter is engaged, at fifteen! Indecent! "
        "{vera.2}What about? asks Agnes. Something about wool, says Chris. Didn't sound important. We know it is.",
        "Maggie decides they will eat outside.",
        "{-vera}",
        ("C", "Lughnasa's almost over, girls. There aren't going to be many warm evenings left.", "c_over", {"voix": "F"}),
        "{-c_over}{-tab_gle2}{fin}On the surface, a remark about the weather. Underneath, an elegy: "
        "the summer, the festival and the family are all ending together. "
        "{fin.1}Maggie spreads a cloth on the grass, in the middle of the garden.",
        "{-fin}{rose}And Rose comes in from the back of the house.",
        "{-rose}",
        ("C", "Its feathers are ruffled and it is stained with blood. ROSE is calm, almost matter-of-fact.", "c_coq"),
        "{-c_coq}{coq}She holds her pet rooster by the feet. {coq.1}The fox must have got him, she says. "
        "{coq.2}She lays it carefully on the tablecloth. {coq.3}Agnes offers her another white rooster. "
        "I don't want another.",
        "{-coq}{echo}Think back to part seven: in Ryanga, says Jack, you kill a rooster to please the spirits. "
        "Here a white bird lies bleeding in the middle of the feast, just after Rose came back from the back hills, "
        "with Danny Bradley. You can read it as a sacrifice, or as innocence lost. Friel does not explain it.",
    ], vis={
        "tab_gle2": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.2, .55, .45], a=[1.0, .5, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "vera": dict(type="liste", titre="Vera McLaughlin · pages 69 – 70", items=[
            "Kate: her daughter engaged at fifteen, “indecent”",
            "Chris: “Something about wool. Didn't sound important.”"], marques=["1", "2"], x=150, y=200, w=980),
        "c_over": dict(type="cit", a="Maggie", o="p. 70", x=170, y=200, w=940),
        "fin": dict(type="note", cles=["elegy"], terme="Subtext · p. 70",
                    t="The weather, the festival, the family: all ending together.",
                    etape="A cloth spread “in the middle of the garden”.", x=170, y=200, w=940),
        "rose": dict(type="mot", t="Rose enters", g="from the back of the house", y=270, taille=80),
        "c_coq": dict(type="cit", a="Stage direction", o="p. 71", x=170, y=200, w=940),
        "coq": dict(type="liste", titre="The dead rooster · page 71", items=[
            "“The fox must have got him.”",
            "Laid “carefully on the tablecloth”",
            "“We'll get another white rooster” … “I don't want another.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "echo": dict(type="cols", g="Ryanga", gq="a rooster killed “to please the spirits”", d="Ballybeg",
                     dq="a white rooster, bleeding, on the feast cloth", vs="↔", repere="sacrifice? innocence lost?"),
    }),

    # ------------------------------------------------------------------ IV. l'échange
    dict(id="echange", chap="The exchange", fond="aube", humeur="mystere",
         retenir="Jack and Gerry swap hats in a Ryanga ritual; then the kites show their “cruel, grinning” faces.", beats=[
        "{tab_kil}{uni}Jesus, Mary and Joseph! cries Maggie. Jack appears in his old white uniform, "
        "the one he wore as chaplain to the British army in the Great War. {uni.1}It is soiled, crumpled, far too large: "
        "his hands are lost in the sleeves. {uni.2}On his head, the tricorn hat, its plumage broken.",
        "{-uni}{rite}Now the formal exchange. {rite.1}Each man puts his hat on the grass. "
        "{rite.2}Three steps back: a symbolic distancing from what you once possessed. "
        "{rite.3}Turn round once, a complete circle: the formal rejection. {rite.4}Then each crosses to the other's place.",
        "{-rite}",
        ("C", "Excellent. The exchange is now formally and irrevocably complete.", "c_exchange"),
        "{-c_exchange}{-tab_kil}{chapeaux}Gerry gets the tricorn, Jack the straw hat. "
        "{chapeaux.1}Gerry does a Charlie Chaplin walk; strutting like a pair of peacocks, says Maggie. "
        "{chapeaux.2}And remember part eleven: the last time Michael saw his father, he was dancing down the lane "
        "with Jack's tricorn over his left eye.",
        "{-chapeaux}{sept}The radio is broken again. Possessed, says Chris. Kate: I wish you wouldn't use words like that. "
        "{sept.1}I love September, says Kate. {sept.2}Agnes promises Rose bilberries next Sunday. "
        "We know there will be no next Sunday together.",
        "{-sept}{kites}Then Gerry picks up the boy's kites. Not bad for a kid of seven. Maggie: I hate them.",
        "{-kites}",
        ("C", "For the first time we all see the images. On each kite is painted a crude, cruel, grinning face, "
              "primitively drawn, garishly painted.", "c_kites"),
        "{-c_kites}{masque}The kites were built all through the play. Now they turn their faces to us, like pagan masks. "
        "{masque.1}And the last word goes to Maggie's riddle: why is a gramophone like a parrot? "
        "Because it… God, I've forgotten! The joke never arrives.",
    ], vis={
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "uni": dict(type="liste", titre="Jack's uniform · page 72", items=[
            "“so large that it looks as if it were made for a much larger man”",
            "“a tricorn, ceremonial hat”, “the plumage broken and tatty”"], marques=["1", "2"], x=150, y=200, w=980),
        "rite": dict(type="liste", titre="The ritual · page 72", items=[
            "Each possession placed on the ground",
            "Three steps away: “a symbolic distancing”",
            "Turn round once, “a complete circle”: “the formal rejection”",
            "Each crosses to the other's place"], marques=["1", "2", "3", "4"], x=150, y=160, w=980),
        "c_exchange": dict(type="cit", a="Jack", o="p. 72", x=170, y=210, w=940),
        "chapeaux": dict(type="liste", titre="Two hats · pages 72 – 73", items=[
            "Gerry: a Charlie Chaplin walk; “a pair of peacocks!”",
            "p. 64: Gerry leaves for Spain wearing Jack's tricorn"], marques=["1", "2"], x=150, y=200, w=980),
        "sept": dict(type="liste", titre="Last plans · page 73", items=[
            "Kate: “I love September.”",
            "Agnes to Rose: “Next Sunday, then.” Bilberries."], marques=["1", "2"], x=150, y=200, w=980),
        "kites": dict(type="mot", t="The kites", g="“Not bad for a kid of seven.” · “I hate them.”", y=270, taille=84),
        "c_kites": dict(type="cit", a="Stage direction", o="p. 73", x=170, y=190, w=940),
        "masque": dict(type="note", cles=["masks", "forgotten"], terme="The end of the afternoon · pp. 73 – 74",
                       t="Grinning faces, like pagan masks, turned to the audience.",
                       etape="Maggie's riddle: “God I've forgotten!”", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Tragic irony, ritual, symbols of the end, a dance cut short: the last afternoon, seen from the end.", beats=[
        "{a1}Now the analysis. Four ideas. "
        "{a1.1}One: tragic irony. A dressmaking plan, bilberries next Sunday, I love September. "
        "Because Michael has just told us the ending, every hopeful line hurts. The scene is an elegy disguised as a picnic.",
        "{-a1}{a2}{a2.1}Two: ritual replaces sacrament. Kate defends the holy sacrament of matrimony; "
        "Jack answers with a Ryanga ceremony, formal and irrevocable. He gives away the uniform of the British army and the "
        "Church that sent him. Pagan ritual, here, is what gives meaning to a goodbye.",
        "{-a2}{a3}{a3.1}Three: symbols of the end. The dead white rooster on the feast cloth, the broken radio, "
        "the kites' cruel, grinning faces. None of them is explained. They are images a child stored, "
        "and an adult still cannot put into words.",
        "{-a3}{a4}{a4.1}Four: the dance, and its limits. Gerry and Agnes dance with easy elegance; "
        "Chris watches, then switches the music off. Dance still frees the sisters, "
        "but it also divides them. Even Maggie's joke stops halfway.",
        "{-a4}{carte}Here is the last afternoon for your essay. {carte.1}Tragic irony. {carte.2}Ritual against sacrament. "
        "{carte.3}Symbols. {carte.4}And the dance, cut short.",
    ], vis={
        "a1": dict(type="note", cles=["irony", "elegy"], terme="1 · Tragic irony",
                   t="Dressmaking, bilberries, “I love September”: hopes we know are doomed.",
                   etape="An elegy disguised as a picnic.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["ritual", "sacrament"], terme="2 · Ritual replaces sacrament",
                   t="“the holy sacrament of matrimony” against “formally and irrevocably complete”.",
                   etape="Jack gives away the uniform of the army and the Church.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["rooster", "kites"], terme="3 · Symbols of the end",
                   t="The dead white rooster, the broken radio, the “cruel, grinning” kites.",
                   etape="Images a child stored, never explained.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["elegance", "divides"], terme="4 · A dance cut short",
                   t="Gerry and Agnes dance; Chris switches the radio off.",
                   etape="Dance frees the sisters, but also divides them.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="THE LAST AFTERNOON", branches=[
            dict(t="Tragic irony", items=["the dressmaker plan", "“I love September”", "“Next Sunday”"]),
            dict(t="Ritual", items=["Pius XI / “the Great Goddess”", "the hat exchange", "“irrevocably complete”"]),
            dict(t="Symbols", items=["the dead white rooster", "the broken radio", "the grinning kites"]),
            dict(t="Dance", items=["“Anything Goes”", "Chris at the window", "the forgotten riddle"])]),
    }),
]

QUIZ = [
    dict(q="What does Kate oppose to Jack's Ryanga “system” of one husband for several wives?",
         r=["What Pope Pius XI considers the holy sacrament of matrimony", "The laws of the Irish Free State",
            "Maggie's dressmaking plan", "The rules of the knitting factory"], ok=0, voir="c_pius",
         ex="“I don't think it's what Pope Pius XI considers to be the holy sacrament of matrimony”: Rome against Ryanga."),
    dict(q="Which song plays on the radio when Gerry dances with Agnes?",
         r=["“Anything Goes”", "“Abyssinia”", "“The Isle of Capri”", "No song is named"], ok=0, voir="song",
         ex="The stage direction on p. 66: Music of “Anything Goes” very softly on the radio."),
    dict(q="Why does Chris turn the radio off?",
         r=["She has seen Gerry kiss Agnes, and says she is sick of “that damned thing”", "Kate orders her to",
            "The music is too loud for Jack", "Michael has broken it"], ok=0, voir="fenetre",
         ex="She saw the kiss from the window without hearing it; officially, she is only “wasting the battery”."),
    dict(q="How does Rose behave when she brings in her dead rooster?",
         r=["She is calm, almost matter-of-fact", "She screams and runs away", "She blames Gerry", "She hides it from Kate"],
         ok=0, voir="c_coq",
         ex="“ROSE is calm, almost matter-of-fact.” She lays the bird on the tablecloth and refuses another white rooster."),
    dict(q="In Jack's exchange ritual, what does turning round once in a complete circle mean?",
         r=["The formal rejection of what you once had", "A blessing from the spirits", "A promise to come back",
            "The start of a dance"], ok=0, voir="rite",
         ex="Three steps away: “a symbolic distancing”; a complete circle: “the formal rejection”; then each takes the other's place."),
    dict(q="What do we see on the kites “for the first time”?",
         r=["A crude, cruel, grinning face on each one", "The names of the five sisters", "A cross and a sun",
            "Michael's initials"], ok=0, voir="c_kites",
         ex="“On each kite is painted a crude, cruel, grinning face, primitively drawn, garishly painted”: like pagan masks."),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "valve table radio, Museo della scienza e della tecnologia, Milan (CC BY-SA 4.0); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
