"""Dancing at Lughnasa — résumé-analyse en vidéo, partie 8 : « Three weeks later », l'ouverture de l'acte II (PDF de travail, p. 45-52).

Début : p. 45, « ACT TWO » (début septembre, trois semaines plus tard ; Maggie, l'enfant, les cerfs-volants, la lettre au
père Noël et la bicyclette promise par Gerry). Jack, plus fort et alerte, la noce d'Austin Morgan, les myrtilles de
Lughnasa, Okawa, le gong, la fête de la nouvelle igname et les sacrifices à Obi ; Kate et la messe ; Kate et Maggie à voix
basse (« He's not our Jack at all »). Fin : p. 52, juste avant la didascalie « (CHRIS and GERRY enter L. … ) ».
Même chaîne que la partie 1 : outils/serie-philo/generer.py dal_8. Citations courtes, à fin d'analyse ; le reste est résumé.
Ce qui ne vient pas du texte (l'air de Haendel, l'Irlande catholique des années 1930) est dit comme tel.
Coquilles du PDF évitées dans les citations : « Casva », « we pas », « bee asking », « latter of lepers ».
"""

SITE = "acl-lughnasa"
LANGUE = "en"
CODE = "dal-8"
NOTION = "Dancing at Lughnasa"
NUM = 8
TITRE = "Three weeks later"
SUIVANT = "Part 9 · Gerry comes back"
PRONONCIATION = {"Lughnasa": "Loo-na-sa", "Lugh": "Loo", "Ryanga": "Ree-anga", "Ryangans": "Ree-angans",
                 "Okawa": "Oh-kah-wa", "Obi": "Oh-bee", "Carrickfad": "Carrick-fad", "Mundy": "Mundy"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_don}{q1}Act Two. Early September: three weeks later. Remember Michael's warning at the end of Act One: "
        "one morning in early September, Rose and Agnes would be gone for ever.",
        "{-q1}{serie}So we are there. And on stage, all looks calm: a song, a letter, a priest getting better.",
        ("P", 0.3),
        "{-serie}{-tab_don}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_don": dict(type="tableau", img="dal-donegal", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Donegal, Five Finger Strand (photo dconvertini, CC BY-SA 4.0)"),
        "q1": dict(type="question", t="Early September: the month Michael warned us about."),
        "serie": dict(type="mot", t="The opening of Act Two", g="Maggie and the boy · a new Jack · the harvest in Ryanga",
                      y=270, taille=84),
        "titre": dict(type="titre", sur="Dancing at Lughnasa · Part 8", t="Three weeks later",
                      sous="The opening of Act Two · pages 45 – 52"),
    }),

    # ------------------------------------------------------------------ I. Maggie et l'enfant
    dict(id="maggie", chap="A bell for a bicycle", fond="aube", humeur="lumiere",
         retenir="The boy believes in Gerry's black bike. Maggie's manner changes: she knows promises from Gerry.", beats=[
        "{tab_gle}{decor}Page forty-five. {decor.1}On the kitchen table, ink and paper. "
        "{decor.2}Two finished kites lean against the garden seat, their artwork still unseen. "
        "{decor.3}Maggie comes in with two buckets of water, singing in her usual parodic style: a song about a gypsy, a vagabond, a caravan.",
        "{-decor}{pari}As in Act One, the boy is invisible, and the adult Michael speaks his lines. "
        "{pari.1}Maggie claims her penny: three weeks ago she bet him the kites would never get off the ground. And they never did. "
        "{pari.2}There was never enough wind, says the boy.",
        "{-pari}{-tab_gle}{velo}He is writing to Santa Claus, in September. What for? {velo.1}A bell. For his bicycle. "
        "{velo.2}The bike his daddy has bought him: in Kilkenny, a black bike, a man's bike, delivered next week. He promised.",
        "{velo.3}Then the stage direction: her manner changes. Softly, Maggie asks: your daddy told you that? "
        "Remember part six: Gerry told Chris the bike only came in blue. So, no bicycle.",
        "{-velo}{bar}Maggie quickly changes the tone. Who will teach you to ride? Put me on the bar, cub: magnificent! "
        "You never sat on the bar of a bike in your life, says the boy.",
        "{-bar}",
        ("C", "Oh yes, I did, Michael. Oh yes, indeed I did.", "c_bar", {"voix": "F"}),
        "{-c_bar}{sous}A tiny line, repeated. Behind the joke, a memory of her own youth: think of the boy she loved at the Ardstraw dance, "
        "in part four. Maggie does not explain. It is subtext. Then she sends the child out with a riddle.",
    ], vis={
        "tab_gle": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .45, .5],
                        legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "decor": dict(type="liste", titre="Act Two opens · page 45", items=[
            "“Early September; three weeks later.”",
            "Two finished kites, “their artwork still unseen”",
            "Maggie sings “in her usual parodic style”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "pari": dict(type="liste", titre="Maggie and the boy · page 46", items=[
            "The penny bet: the kites “never did” get off the ground",
            "Boy: “there was never enough wind”"], marques=["1", "2"], x=150, y=200, w=980),
        "velo": dict(type="liste", titre="A letter to Santa · page 47", items=[
            "He asks for “A bell.” “For my bicycle.”",
            "Gerry's promise: Kilkenny, “a black bike – a man's bike”",
            "(Her manner changes.) “Your daddy told you that?”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "bar": dict(type="note", cles=["bar", "magnificent"], terme="Maggie and the boy · p. 47",
                    t="“put me on the bar, cub – magnificent!”",
                    etape="Boy: “You never sat on the bar of a bike in your life”", x=170, y=200, w=940),
        "c_bar": dict(type="cit", a="Maggie", o="p. 47", x=170, y=200, w=940),
        "sous": dict(type="def", cles=["youth", "subtext"], terme="Subtext",
                     t="A joke on the surface; underneath, a memory of Maggie's own youth.",
                     etape="She never explains: the line carries her past in silence.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. un nouveau Jack
    dict(id="jack", chap="A new Jack", fond="aube", humeur="lumiere",
         retenir="Jack is stronger, his words and memories come back… and with them, the Lughnasa ritual of his childhood.", beats=[
        "{tab_kil}Then Jack enters, and the stage direction insists on the change.",
        "{-tab_kil}",
        ("C", "He looks much stronger and is very sprightly and alert.", "c_alert"),
        "{-c_alert}{tab_kil2}{jk}No more top coat and hat: he wears a garish sweater, probably a sister's. "
        "{jk.1}He heard the church bell: a big posh wedding, says Maggie. "
        "{jk.2}Austin Morgan and a girl from Carrickfad. Remember part three: Kate's blush when Rose teased her about Austin Morgan.",
        "{jk.3}Off on his fourth walk, so Kate won't nag at him… nag? He tests the word. My English vocabulary is coming back.",
        "{-jk}{-tab_kil2}{baies}{baies.1}Kate asks: no sign of Rose and Agnes yet? They are picking bilberries, back for tea. "
        "A quiet line. But in early September, after Michael's warning, it sends a shiver.",
        "{baies.2}Jack remembers the bilberries too: picking them with Mother, every Lughnasa, the annual ritual. "
        "{baies.3}Then a song comes back to him: O ruddier than the cherry. It's all coming back to me, he laughs.",
        "{-baies}{handel}Outside the text: he wonders if it's Gilbert and Sullivan. In fact, it is an aria from Handel's Acis and Galatea.",
        "{-handel}{messe}Kate seizes the moment. So you'll soon begin saying Mass again? Yes, indeed, says Jack. "
        "Perhaps next Monday, here in the house. The neighbours would join us.",
    ], vis={
        "tab_kil": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .5],
                        legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "c_alert": dict(type="cit", a="Stage direction", o="p. 48", x=170, y=200, w=940),
        "tab_kil2": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.25, .55, .45], a=[1.05, .5, .5],
                         legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "jk": dict(type="liste", titre="Jack, three weeks later · page 48", items=[
            "The church bell: “A big posh wedding today.”",
            "“A man called Austin Morgan and a girl from Carrickfad”",
            "“So my English vocabulary is coming back, too.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "baies": dict(type="liste", titre="Bilberries · page 49", items=[
            "Rose and Agnes: “away picking bilberries”, back for tea",
            "Jack: “Mother and myself; every Lughnasa; the annual ritual.”",
            "“You see, Kate, it's all coming back to me.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "handel": dict(type="note", cles=["Handel"], terme="Outside the text",
                       t="“O ruddier than the cherry”: an aria from Handel's Acis and Galatea, not Gilbert and Sullivan.",
                       etape="Jack's memory returns in fragments.", x=170, y=200, w=940),
        "messe": dict(type="dialogue", lignes=["Kate: “So you'll soon begin saying Mass again?”", "Jack: “Yes, indeed.”",
                                               "Jack: “Perhaps I'll start next Monday.”"],
                      src="p. 49", x=170, y=150, w=980),
    }),

    # ------------------------------------------------------------------ III. la fête de l'igname
    dict(id="ryanga", chap="The Festival of the New Yam", fond="nuit", humeur="mystere",
         retenir="In Ryanga, sacrifice, harvest and dance form one ceremony: “no distinction between the religious and the secular”.", beats=[
        "{tab_kil3}{oka}But how will the neighbours know? Jack thinks of Okawa. {oka.1}My friend, my mentor, my counselor, "
        "and yes, my house boy as well. {oka.2}Okawa summons the people with a huge iron gong, which carries four times as far as the wedding bell.",
        "{oka.3}Your church? When I had a church, he says: now they gather in the village common. "
        "All gathered for Mass? asks Kate. Maybe, he says. Or maybe…",
        "{-oka}",
        ("C", "Or maybe to offer sacrifice to Obi, our Great Goddess of the Earth, so that the crops will flourish.", "c_obi"),
        "{-c_obi}{-tab_kil3}{fetes}Listen to that our. Our Great Goddess. The missionary now speaks from inside the tribe. "
        "{fetes.1}At harvest time, he says, there are two ceremonies: the Festival of the New Yam and the Festival of the Sweet Cassava. "
        "{fetes.2}Kate: but these aren't Christian ceremonies, Jack, are they? {fetes.3}Oh, no, he says happily.",
        "{-fetes}{rite}And he describes them, step by step. {rite.1}The ritual sacrifice of a fowl, a goat or a calf by the river. "
        "{rite.2}The first yams anointed and passed round. {rite.3}A chant, which becomes the rhythm for the ritual dance. "
        "{rite.4}Then fires, painted faces, palm wine… and lepers dancing for days on end.",
        "{-rite}",
        ("C", "there is no distinction between the religious and the secular in their culture.", "c_secular"),
        "{-c_secular}{deux}That is the key line. {deux.g}In Ryanga, worship flows into celebration, almost imperceptibly. "
        "{deux.d}In Kate's Ballybeg, the Church and the dance hall are kept strictly apart. You'd love them, Maggie, says Jack.",
        "{-deux}{gong}One last twist. Mass next Monday? At first light, says Jack, when Rose's white cock crows. "
        "{gong.1}A harvest ceremony. You'll have to find a big gong somewhere, Kate.",
    ], vis={
        "tab_kil3": dict(type="tableau", img="dal-kilwa", fond=True, sombre=True, de=[1.15, .4, .5], a=[1.3, .6, .5],
                         legende="East African campaign, Kilwa, 1917 (Imperial War Museums, public domain)"),
        "oka": dict(type="liste", titre="Okawa and the gong · page 50", items=[
            "“My friend – my mentor – my counselor”",
            "A huge iron gong: “four times as far” as the bell",
            "“When I had a church.” Now: the common"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_obi": dict(type="cit", a="Jack", o="p. 50", x=170, y=190, w=940),
        "fetes": dict(type="liste", titre="Harvest in Ryanga · page 50", items=[
            "“the Festival of the New Yam” and the Sweet Cassava",
            "Kate: “But these aren't Christian ceremonies, Jack, are they?”",
            "Jack: “Oh, no.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "rite": dict(type="liste", titre="The ceremony · pages 50 – 51", items=[
            "A sacrifice: “a fowl or a goat or a calf”",
            "The first yams anointed, passed round in wooden bowls",
            "A chant: the rhythm “for the ritual dance”",
            "Fires, painted faces, palm wine: dancing “for days on end”"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "c_secular": dict(type="cit", a="Jack", o="p. 51", x=170, y=200, w=940),
        "deux": dict(type="cols", g="Ryanga", gq="worship grows into celebration", d="Ballybeg",
                     dq="the Church apart from the dance", vs="≠", repere="religious / secular"),
        "gong": dict(type="note", cles=["harvest", "gong"], terme="Jack · p. 51",
                     t="“A harvest ceremony. You'll have to find a big gong somewhere, Kate.”",
                     etape="The Mass Kate hopes for is turning into a Ryangan rite.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. pas notre Jack
    dict(id="peur", chap="Not our Jack", fond="nuit", humeur="tension",
         retenir="Kate is frightened by what Jack has become, and orders silence: “not a syllable” outside these walls.", beats=[
        "{tab_gle2}{chut}He leaves. Kate and Maggie stare at each other, in alarm. They speak in hushed voices. "
        "{chut.1}I told you, says Kate. {chut.2}Yesterday, a medicine man who brought a woman back from death; "
        "this morning, the spirits of the tribe. {chut.3}He needs more time, says Maggie.",
        "But Kate is sure.",
        "{-chut}",
        ("C", "He's not our Jack at all. And it's what he's changed into that frightens me.", "c_frightens", {"voix": "F"}),
        "{-c_frightens}{-tab_gle2}{corps}Doesn't frighten me, says Maggie. Then watch the stage directions. "
        "{corps.1}Kate wipes the table with excessive vigour. {corps.2}She stops, slumps into a seat, covers her face. "
        "{corps.3}Maggie stands behind her and holds her shoulders. The body says what Kate cannot.",
        "{-corps}{rire}Maggie tries a joke: lepers trying to do the Military Two-step. God forgive you, Maggie Mundy! "
        "{rire.1}Then Chris laughs offstage, and Kate jumps to her feet: this must be kept in the family. Not a syllable!",
    ], vis={
        "tab_gle2": dict(type="tableau", img="dal-glenties", fond=True, sombre=True, de=[1.15, .55, .45], a=[1.0, .5, .5],
                         legende="Glenties, County Donegal (photo Thpohl, public domain)"),
        "chut": dict(type="liste", titre="In hushed voices · pages 51 – 52", items=[
            "Kate: “I told you – you wouldn't believe me – I told you.”",
            "A medicine man; “the spirits of the tribe!”",
            "Maggie: “He needs more time.”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "c_frightens": dict(type="cit", a="Kate", o="p. 52", x=170, y=200, w=940),
        "corps": dict(type="liste", titre="Stage directions · page 52", items=[
            "She wipes the table “with excessive vigour”",
            "She “slumps into a seat and covers her face”",
            "Maggie “holds her shoulders with her hands”"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "rire": dict(type="note", cles=["family", "syllable"], terme="Kate · p. 52",
                     t="“This must be kept in the family, Maggie!”",
                     etape="“Not a word of this must go outside these walls”", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ V. l'analyse
    dict(id="analyse", chap="Analysis", fond="nuit", humeur="calme",
         retenir="Tragic knowledge, two harvest festivals, dance as community, and Kate's secret: Act Two opens on borrowed calm.", beats=[
        "{a1}Now the analysis: four ideas for the opening of Act Two. "
        "{a1.1}One: tragic knowledge. We know what the characters don't. Rose and Agnes back for tea, a black bike next week, "
        "Mass next Monday: every promise in these pages is shadowed by Michael's prolepsis.",
        "{-a1}{a2}{a2.1}Two: two harvest festivals. The bilberries of Lughnasa, Mother's annual ritual, "
        "and the Festival of the New Yam in Ryanga. Friel draws a parallel between Donegal and Uganda. "
        "Jack's Mass becomes a harvest ceremony: syncretism, Christian and pagan blending.",
        "{-a2}{a3}{a3.1}Three: dance as community. In Ryanga, everyone dances, even lepers with missing limbs, for days. "
        "Think back to the sisters' dance in part five: frantic, defiant, and followed by shame. In Ryanga, the dance belongs to everyone, and nobody is ashamed.",
        "{-a3}{a4}{a4.1}Four: Kate's authority and the outside world. Kate guards reputation: not a syllable outside these walls. "
        "Outside the text: in nineteen-thirties Ireland, the Church dominated public life, so a priest gone native meant scandal. "
        "And part seven told us: it will cost Kate her job.",
        "{-a4}{carte}Here is the opening of Act Two for your essay. {carte.1}Tragic knowledge. {carte.2}Pagan and Christian harvests. "
        "{carte.3}Dance and community. {carte.4}And Kate's fear: control, secrecy, change.",
    ], vis={
        "a1": dict(type="note", cles=["tragic", "prolepsis"], terme="1 · Tragic knowledge",
                   t="“back for tea”, a black bike “next week”, Mass “next Monday”.",
                   etape="Every promise is shadowed by Michael's prolepsis.", x=170, y=200, w=940),
        "a2": dict(type="note", cles=["harvest", "syncretism"], terme="2 · Two harvest festivals",
                   t="Lughnasa bilberries, “the annual ritual” ↔ “the Festival of the New Yam”.",
                   etape="Syncretism: the Mass becomes “A harvest ceremony”.", x=170, y=200, w=940),
        "a3": dict(type="note", cles=["community", "dance"], terme="3 · Dance as community",
                   t="Lepers dancing “for days on end”: worship and celebration in one.",
                   etape="In Ballybeg, the sisters' dance ended in shame.", x=170, y=200, w=940),
        "a4": dict(type="note", cles=["reputation", "Church"], terme="4 · Kate's authority",
                   t="“This must be kept in the family”: “not a syllable!”",
                   etape="Outside the text: 1930s Ireland, a Church-dominated society.", x=170, y=200, w=940),
        "carte": dict(type="carte", centre="ACT TWO OPENS", branches=[
            dict(t="Tragic knowledge", items=["“back for tea”", "the black bike", "Mass “next Monday”"]),
            dict(t="Harvests", items=["“every Lughnasa”", "“the Festival of the New Yam”", "“A harvest ceremony”"]),
            dict(t="Dance", items=["lepers dancing “for days on end”", "religious = secular"]),
            dict(t="Kate's fear", items=["“not our Jack at all”", "“kept in the family”", "“not a syllable!”"])]),
    }),
]

QUIZ = [
    dict(q="When does Act Two take place?",
         r=["Early September, three weeks after Act One", "The next morning", "At Christmas", "A year later, in August 1937"],
         ok=0, voir="decor",
         ex="“Early September; three weeks later.” The very month Michael announced Rose and Agnes would leave."),
    dict(q="Why does Maggie's manner change when the boy talks about his bicycle?",
         r=["She doubts Gerry's promise of a black bike", "She is jealous of the boy", "She hates bicycles",
            "She knows Kate will forbid it"], ok=0, voir="velo",
         ex="“(Softly.) Your daddy told you that?” In part six, Gerry admitted the bike only came in blue."),
    dict(q="How does the stage direction describe Jack in Act Two?",
         r=["Much stronger, “very sprightly and alert”", "Weaker and confused", "Dressed in his white uniform",
            "Silent and motionless"], ok=0, voir="c_alert",
         ex="He has lost his top coat and hat and wears a garish sweater, “probably a sister's”."),
    dict(q="Why does Jack want to offer sacrifice to Obi?",
         r=["So that the crops will flourish", "To cure the lepers", "To bring the rain for the kites", "To please the bishop"],
         ok=0, voir="c_obi", ex="Obi is “our Great Goddess of the Earth”: note the possessive “our”, the priest speaks from inside the tribe."),
    dict(q="What, according to Jack, is remarkable about Ryangan culture?",
         r=["There is no distinction between the religious and the secular", "It forbids dancing",
            "It has accepted the Catholic Mass completely", "It has no festivals"], ok=0, voir="c_secular",
         ex="The ceremony “grows naturally into a secular celebration”: the opposite of Kate's Ballybeg."),
    dict(q="What does Kate demand at the end of the scene?",
         r=["That Jack's change be kept in the family", "That Jack leave the house", "That Maggie fetch the priest",
            "That Rose and Agnes come home at once"], ok=0, voir="rire",
         ex="“Not a word of this must go outside these walls – d'you hear? – not a syllable!”"),
]

CREDITS = [
    "Brian Friel, Dancing at Lughnasa (1990): short quotations for analysis, page numbers from the class PDF",
    "Photographs: Five Finger Strand, Donegal (dconvertini, CC BY-SA 4.0); Glenties (Thpohl, public domain); "
    "troops at Kilwa, 1917 (Lt L. A. W. Powell, Imperial War Museums, public domain)",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music",
]
