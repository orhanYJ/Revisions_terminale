"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 2 :
« From an American crash to a world crisis » (parties I.2 et I.3 du cours).

Même chaîne que la série H3 (voir h3_1.py) : outils/serie-philo/generer.py h1_2 ; sortie dans dnl/serie/.
Carte animée H1 (dnl/cartes/H1.html), scènes utilisées (ordre chronologique de la carte) :
  3 plan Dawes · 5 le krach · 6 des vies brisées · 7 la périphérie et la chute des prix · 8 les faillites bancaires ·
  9 le rappel des prêts · 10 une crise durable dans le monde dominé · 11 les Hoovervilles · 12 un traumatisme inégal ·
  17 l'effet domino en Europe · 19 l'étalon-or · 25 le Dust Bowl · 28 Migrant Mother
Contenu : CHAPTERS.H1, section I.2 (cinq idées ; schémas h1dawes H1DawesAnim, crisis H1Chain, h1factors H1Factors)
et section I.3 (cinq idées) ; chiffres du cours. Ce qui vient d'ailleurs est dit « outside the course ».
Le cours dit « average wages fell by 60% » : corrigé à l'oral (≈ masse salariale de l'industrie, plus que divisée par deux ; salaire horaire ≈ −20 %).
Pauses « Your turn » : un paragraphe Explain, puis un DBQ a) « How useful » sur Migrant Mother (structure imposée :
jugement dès la première ligne, document en une phrase, atouts, limites).
Plan de la série H1 : 1 The Great Crash of 1929 · 2 From an American crash to a world crisis ·
3 Economic nationalism and political responses · 4 Democracies and the liberal order · 5 The crisis at the exam · 6 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-2"
NOTION = "The Wall Street Crash"
NUM = 2
TITRE = "From an American crash to a world crisis"
SUIVANT = "Episode 3 · Economic nationalism and political responses"
PRONONCIATION = {"Creditanstalt": "Credit-an-shtalt", "Nipomo": "Nee-po-mo", "Hoovervilles": "Hoover-villes",
                 "Hooverville": "Hoover-ville", "Capone": "Ka-pone", "Dawes": "Daws", "Stratford": "Strat-ford"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{q1}October 1929. In a few days, the New York stock market collapses. In the last episode, you saw how and why.",
        "{-q1}{q2}But a crash lasts days. So how did a panic in one street of New York "
        "become a depression that lasted ten years, from Berlin to Santiago?",
        "{-q2}{q3}And what did it do to people's lives? To the families who lost their jobs, their savings, their homes… and their land?",
        "{-q3}{-g0}{plan}This series covers the whole chapter in six episodes. {plan.1}Episode one was the Great Crash itself. "
        "{plan.2}Today: from an American crash to a world crisis, and one of the defining traumas of the twentieth century. "
        "{plan.3}Then economic nationalism and political responses, {plan.4}the democracies and the liberal order, "
        "{plan.5}an episode for the exam, essay and DBQ, {plan.6}and a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[5]),
        "q1": dict(type="question", t="October 1929: a crash in New York.", bande=True),
        "q2": dict(type="question", t="How did it become a world crisis?", bande=True),
        "q3": dict(type="question", t="What did it do to people's lives?", bande=True),
        "plan": dict(type="liste", titre="H1 · The Wall Street Crash, in six episodes", items=[
            "The Great Crash of 1929 (Part I.1)", "From an American crash to a world crisis (Parts I.2 – I.3)",
            "Economic nationalism and political responses (II.1 – II.2)", "Democracies and the liberal order (II.3)",
            "The crisis at the exam: essay and DBQ", "Recap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 2", t="From an American crash to a world crisis",
                      sous="banks · loans · gold · a trauma of the twentieth century"),
    }),

    # ================================================================ partie chronologique
    dict(id="chrono", chap="The crisis on the map", fond="nuit", humeur="tension",
         retenir="1924 Dawes Plan · Oct. 1929 Crash · 1930–32 bank failures, loans recalled · May–Sept. 1931 dominoes in Europe · 1931–36 leaving gold · 1935 Dust Bowl · 1936 Migrant Mother.",
         beats=[
        "{g1}Let's follow the crisis on the map first, date by date. {g1.1}It starts before the crash, in nineteen twenty-four, with the Dawes Plan. "
        "Germany receives a loan of eight hundred million marks, largely American money. With it, Germany pays reparations to France and Britain. "
        "And France and Britain repay their war debts to the United States. Everything rests on American credit.",
        "{g1.2}October 1929: the Crash. Black Thursday, then Black Monday and Black Tuesday. Everyone sells, nobody buys.",
        "{g1.3}From 1929 to 1933, millions of American lives are broken, with no safety net.",
        "{g1.4}Far from New York, the countries that sell raw materials are hit by falling prices. "
        "Brazil lives on coffee. Chile lives on nitrate.",
        "{g1.5}From 1930, the banks fail one after another: about five thousand by 1932. "
        "This is the moment the crash becomes the Great Depression.",
        "{g1.6}And American banks recall their loans to Europe. The money that kept the European economies afloat goes back across the Atlantic.",
        "{g1.7}Across the dependent world, the crisis lasts: Latin America, Canada, India, Australia, New Zealand.",
        "{g1.8}In American cities, evicted families build shanty towns. People call them Hoovervilles.",
        "{g1.9}The trauma is global… but uneven: the Soviet Union, outside world trade, is barely touched.",
        "{-g1}{g2}{g2.1}Back to Europe, in 1931. The dominoes fall: Austria's largest bank in May, the German banks in July, "
        "and in September, Britain leaves the gold standard.",
        "{g2.2}From 1931 to 1936, one country after another leaves gold: Britain and Japan in 1931, the United States in 1933, "
        "France only in 1936. The earlier a country left, the earlier it recovered.",
        "{g2.3}In April 1935, on the Great Plains, the dust storms of the Dust Bowl turn day into night.",
        "{g2.4}And in March 1936, in a camp in California, the photographer Dorothea Lange takes a picture of a mother and her children. "
        "It becomes the face of the Depression.",
        "{-g2}{fr1}The chronology: {fr1.1}1924, {fr1.2}1929, {fr1.3}1930, {fr1.4}1931, {fr1.5}1935, {fr1.6}1936. Now let's explain it.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[3, 5, 6, 7, 8, 9, 10, 11, 12]),
        "g2": dict(type="globe", code="H1", sc=[17, 19, 25, 28]),
        "fr1": dict(type="frise", items=[
            dict(nom="Dawes Plan", d=1924, q="Europe hangs on US credit"), dict(nom="The Crash", d=1929, q="24–29 October"),
            dict(nom="Bank failures", d=1930, q="≈ 5,000 by 1932"), dict(nom="Dominoes", d=1931, q="Vienna · Berlin · London"),
            dict(nom="Black Sunday", d=1935, q="the Dust Bowl"), dict(nom="Migrant Mother", d=1936, q="Dorothea Lange")]),
    }),

    # ================================================================ I.2 idée 1 : les banques
    dict(id="banques", chap="I.2 · When the banks fail", fond="nuit", humeur="tension",
         retenir="The Great Depression really began when numerous banks started failing. A crash lasts days; a depression is what happens when the banks carry it into the real economy. No deposit insurance before 1933: about 5,000 banks failed by 1932.",
         beats=[
        "{m1}Part two of the chapter: from the US Great Crash to a world-wide financial crisis. "
        "Monsieur Ros's slides insist on one sentence. Learn it by heart: the Great Depression really began "
        "when numerous banks started failing. This is the hinge of the whole chapter.",
        "{-m1}{spi}Why? Because of a spiral. {spi.1}First, confidence is lost. {spi.2}People stop trusting the banks, "
        "so they withdraw their savings. {spi.3}And the more people withdraw, the more banks fail… so even more people withdraw.",
        "{spi.4}Then the spiral reaches the real economy. Uncertain about their future income, businesses and households cut their spending. "
        "{spi.5}So production falls. {spi.6}Workers are laid off, or paid less… so they buy even less. And the spiral turns again.",
        "{spi.7}On the financial side, investors go bankrupt: their assets are now worth less than their liabilities, their debts. "
        "And investment stops.",
        "{-spi}{ex1}Here is the example that makes it concrete. Before 1933, there was {!no deposit insurance}no deposit insurance "
        "in the United States. When a bank failed, its customers' savings were simply gone. So a rumour alone could empty a bank. "
        "That is why about five thousand banks had failed by 1932.",
        "{-ex1}{dc}Keep this distinction. A crash is a financial event: it lasts days. "
        "A depression is what happens when the banking system carries the crash into the real economy: it lasts years.",
    ], vis={
        "m1": dict(type="mot", t="“The Great Depression really began when numerous banks started failing.”",
                   g="the sentence of the slides · the hinge of the chapter", y=230, taille=54),
        "spi": dict(type="liste", titre="The spiral of bank failures", cles=["confidence", "withdraw", "fail", "spending", "laid off", "bankrupt"], items=[
            "Confidence is lost", "Savers withdraw their money", "More withdrawals → more banks fail",
            "Businesses and households cut spending", "Production and output fall", "Workers laid off or paid less → they buy even less",
            "Investors bankrupt (assets < liabilities): investment halts"], x=150, y=100, w=980),
        "ex1": dict(type="note", terme="Example · no safety net for savers", cles=["deposit", "rumour", "5,000"],
                    t="No deposit insurance before 1933: when a bank failed, its customers' savings were gone. A rumour alone could empty a bank.",
                    etape="About 5,000 banks had failed by 1932.", x=170, y=200, w=940),
        "dc": dict(type="cols", g="A crash", gq="a financial event · it lasts days · October 1929",
                   d="A depression", dq="the banks carry it into the real economy · it lasts years", vs="≠"),
    }),

    # ================================================================ I.2 idée 2 : deux canaux
    dict(id="canaux", chap="I.2 · Two channels", fond="nuit", humeur="tension",
         retenir="Short-term causes: the international linkages — US banks recall their loans, European banks collapse, the collapse crosses back. Long-term causes: shared weaknesses (overproduction, falling prices, farm incomes, over-investment) held together by the gold standard.",
         beats=[
        "{q4}Second idea. How did an American crisis cross the ocean? The slides separate two kinds of cause, "
        "and this distinction is worth reusing in any essay.",
        "{-q4}{cc}{!short-term}Short-term causes, first: the important international linkages. American banks suddenly recall their loans "
        "to European banks. The European banks collapse. And because the European banks also held assets in American banks, "
        "the collapse comes back across the Atlantic.",
        "{-cc}{lt}Then the {!long-term}long-term, underlying causes. Economies all over the world already shared the same weaknesses. "
        "{lt.1}Overproduction. {lt.2}Falling prices. {lt.3}Decreasing incomes for farmers. "
        "{lt.4}Over-investment in industry, with overconfidence in its development. "
        "{lt.5}And, holding them all together: the gold standard. We'll come back to it in a minute.",
        "{-lt}{g3}{g3.1}The example: four months of dominoes. In May 1931, the Creditanstalt, "
        "Austria's largest bank, fails. In July, the German banks follow. And in September, Britain leaves the gold standard.",
        "{-g3}{tc}So the crisis travels through two channels at once: {tc.1}a sudden shock, the recall of American loans, "
        "{tc.2}which falls on economies that were already fragile.",
    ], vis={
        "q4": dict(type="question", t="How did an American crisis cross the ocean?"),
        "cc": dict(type="note", terme="Short-term causes · international linkages", cles=["recall", "collapse", "back"],
                   t="US banks suddenly recall their loans to European banks → European banks collapse → the collapse comes back across the Atlantic.",
                   etape="European banks also held assets in American banks.", x=170, y=200, w=940),
        "lt": dict(type="liste", titre="Long-term underlying causes: shared weaknesses", items=[
            "Overproduction", "Falling prices", "Decreasing incomes for farmers",
            "Over-investment in industry, overconfidence", "Holding them together: the gold standard"], x=170, y=120, w=940),
        "g3": dict(type="globe", code="H1", sc=[17]),
        "tc": dict(type="cols", g="A sudden shock", gq="the recall of American loans (short term)",
                   d="Fragile economies", dq="overproduction, falling prices, gold (long term)", vs="+"),
    }),

    # ================================================================ I.2 idée 3 : le plan Dawes
    dict(id="dawes", chap="I.2 · The Dawes Plan", fond="nuit", humeur="tension",
         retenir="Dawes Plan (1924): 800 million marks lent to Germany → reparations up to 2.5 billion marks a year to France and Britain → war debts repaid to the USA. Europe's solvency hung on American credit: the recall of loans broke all three sides.",
         beats=[
        "{g4}Third idea: the Dawes Plan had tied Europe's finances to American credit. Go back to the years after the war. "
        "Germany owes reparations to France and Britain. And France and Britain owe war debts to the United States. Deadlock.",
        "{g4.1}The Dawes Plan of 1924 breaks the deadlock by putting American money at the start of the chain.",
        "{tri}Follow the circuit. {tri.1}One: a loan of eight hundred million marks to Germany, largely raised in New York. "
        "{tri.2}Two: German reparations to France and Britain, rising to two and a half billion marks a year by 1928 and 1929. "
        "{tri.3}Three: France and Britain repay their war debts to Washington. The money goes round the triangle.",
        "{-tri}{-g4}{daw}Charles G. Dawes, the banker behind the plan, shared the Nobel Peace Prize in 1925 for it, and became Vice-President "
        "of the United States. And it worked… as long as American money kept flowing.",
        "{-daw}{rup}Now watch what happens after October 1929. {rup.1}Hit by the Crash, American banks recall their loans: "
        "the first side of the triangle breaks. {rup.2}Cut off from American credit, Germany can no longer pay its reparations: "
        "the second side gives way. {rup.3}Without reparations, France and Britain stop repaying their war debts: the third side gives way.",
        "{-rup}{le}That is the lesson of the Dawes Plan. The crisis crossed the Atlantic through the chain of debt, "
        "not through panic alone. In an essay, this is your best example of interdependence.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[3]),
        "tri": dict(type="liste", titre="The Dawes circuit, 1924 – 1929", cles=["800 million", "2.5 billion", "war debts"], items=[
            "USA → Germany: a loan of 800 million marks (1924)", "Germany → France and Britain: reparations, up to 2.5 billion marks a year",
            "France and Britain → USA: war-debt repayments"], x=540, y=400, w=720, petit=True, bande=True),
        "daw": dict(type="note", terme="Charles G. Dawes", cles=["Nobel", "Vice-President"],
                    t="Author of the 1924 plan; shared the Nobel Peace Prize in 1925 and became Vice-President (1925–1929).",
                    etape="The plan worked — as long as American credit kept flowing.", x=170, y=210, w=940),
        "rup": dict(type="liste", titre="After October 1929: the triangle breaks", items=[
            "✕ US banks recall their loans", "✕ Germany can no longer pay reparations", "✕ France and Britain stop repaying war debts"],
            x=170, y=150, w=940),
        "le": dict(type="mot", t="The chain of debt", g="the crisis crossed the Atlantic through debt, not panic alone", y=260, taille=84),
    }),

    # ================================================================ I.2 idée 4 : l'étalon-or
    dict(id="or", chap="I.2 · The gold standard", fond="nuit", humeur="tension",
         retenir="The gold standard was the transmission belt: the Fed raised rates to defend the dollar, gold left other countries, which had to raise theirs. Leaving gold was the exit: Britain Sept. 1931, Japan Dec. 1931, USA 1933, France 1936. The earlier out, the earlier the recovery.",
         beats=[
        "{def1}Fourth idea, and the most technical one. {!transmission belt}The gold standard was the transmission belt. "
        "Under the gold standard, most countries fixed the value of their currency to gold.",
        "{-def1}{mec}Here is the mechanism. {mec.1}Nervous speculators start trading their dollars for gold. "
        "{mec.2}To preserve the dollar's value, the Federal Reserve, the American central bank, raises its interest rates. "
        "{mec.3}Higher American rates draw gold out of every country with lower rates. "
        "{mec.4}So countries untouched by the crash are forced to raise their own rates, to keep their gold.",
        "{mec.5}And that is the worst possible medicine for an economy that is already slowing down. Dearer money means less investment "
        "and less spending. A system built to guarantee stability spread the contraction to everyone.",
        "{-mec}{fr2}So the exit was to leave gold. {fr2.1}Britain, in September 1931. {fr2.2}Japan, in December 1931. "
        "{fr2.3}The United States, under Roosevelt, in 1933. {fr2.4}And France, only in 1936.",
        "{-fr2}{g5}{g5.1}The rule is simple: the earlier a country left, the earlier it recovered. France, last out, recovered last.",
        "{-g5}{ex2}The example compares two neighbours. {ex2.1}Germany's output recovered strongly after nineteen thirty-two, "
        "when state spending replaced tight money. {ex2.2}France defended the gold value of the franc until nineteen thirty-six. "
        "It was the worst-performing developed economy of the decade.",
    ], vis={
        "def1": dict(type="def", terme="The gold standard", cles=["fixed", "gold"],
                     t="Most countries fixed the value of their currency to gold.",
                     etape="In the crisis, it became the transmission belt of the contraction.", x=170, y=200, w=940),
        "mec": dict(type="liste", titre="How gold spread the crisis", cles=["gold", "interest rates", "raise", "worst"], items=[
            "Speculators trade dollars for gold", "The Federal Reserve raises interest rates to defend the dollar",
            "Higher US rates draw gold out of other countries", "They must raise their own rates",
            "Dearer money → less investment, less spending: the worst medicine"], x=150, y=110, w=980),
        "fr2": dict(type="frise", items=[
            dict(nom="Britain", d=1931, q="September"), dict(nom="Japan", d=1931.9, q="December"),
            dict(nom="United States", d=1933, q="Roosevelt"), dict(nom="France", d=1936, q="last out")]),
        "g5": dict(type="globe", code="H1", sc=[19]),
        "ex2": dict(type="cols", g="Germany", gq="output recovers strongly after 1932: state spending replaces monetary constraint",
                    d="France", dq="defends the franc's gold value until 1936: the worst-performing developed economy of the decade", vs="≠"),
    }),

    # ================================================================ I.2 idée 5 : effet domino et périphérie
    dict(id="domino", chap="I.2 · Dominoes and falling prices", fond="nuit", humeur="tension",
         retenir="Europe, by domino effect: Germany and Austria first (no more reparations), then British banks, then France in 1932. The periphery, by falling prices: Brazil burned some 78 million bags of coffee (1931–1944); Chile's nitrate earnings fell by more than 80% (1929–1932).",
         beats=[
        "{dom}Fifth idea: the Depression hits Europe by domino effect, and the rest of the world by falling prices. Europe first. "
        "{dom.1}The German and Austrian economies are hit first, and they become unable to pay their reparations. "
        "{dom.2}By domino effect, the British banks, which had invested in Germany, are rapidly affected. "
        "{dom.3}France, less indebted to the United States, is affected only in 1932, when the German reparation payments stop flowing smoothly.",
        "{-dom}{g6}{g6.1}Now the periphery: the less developed countries. Two blows: the end of American loans, "
        "and the fall in imports of raw materials. As raw-material prices keep dropping, their exports plummet.",
        "{g6.2}The crisis lastingly affects Latin America, Canada, India, New Zealand and Australia.",
        "{-g6}{per}Two examples. {per.1}Brazil, whose economy depended on coffee, burned some seventy-eight million bags of it "
        "between 1931 and 1944, to hold the price up. {per.2}Chile, which lived on nitrate, saw its export earnings collapse by more than "
        "eighty per cent between 1929 and 1932. {per.3}The lesson: {!no cushion}a country that sells one commodity has no cushion.",
        "{-per}{cha}Let's put the whole of part two together. This is the chain from the course, step by step. "
        "{cha.1}The Wall Street Crash, October 1929: share prices collapse. {cha.2}Banking failures: credit dries up, savings are destroyed. "
        "{cha.3}The United States recalls its foreign loans: Europe, especially Germany, loses American capital. "
        "{cha.4}Protectionism: tariffs and a chain of retaliation. That is episode three. "
        "{cha.5}World trade collapses: its value falls by about two thirds between 1929 and 1934. "
        "{cha.6}And the result: a global depression in the 1930s, with mass unemployment and deflation.",
    ], vis={
        "dom": dict(type="liste", titre="Europe: the domino effect", items=[
            "Germany and Austria hit first → no more reparations", "British banks, invested in Germany, hit in turn",
            "France, less indebted to the US, hit only in 1932"], x=170, y=150, w=940),
        "g6": dict(type="globe", code="H1", sc=[7, 10]),
        "per": dict(type="liste", titre="The periphery: falling prices", cles=["coffee", "nitrate", "cushion"], items=[
            "Brazil burned some 78 million bags of coffee (1931–1944)", "Chile: nitrate export earnings down more than 80% (1929–1932)",
            "One commodity = no cushion"], x=170, y=150, w=940),
        "cha": dict(type="liste", titre="How the crash became a global depression", items=[
            "Wall Street Crash (Oct. 1929): share prices collapse", "Banking failures: credit dries up, savings destroyed",
            "The US recalls its foreign loans: Europe loses US capital", "Protectionism: tariffs and retaliation",
            "World trade collapses: about −2/3 in value (1929–1934)", "Global Depression (1930s): mass unemployment, deflation"],
            x=150, y=100, w=980),
    }),

    # ================================================================ I.2 : peser les causes (worksheet) + pause 1
    dict(id="causes", chap="Weighing the causes", fond="aube", humeur="calme",
         retenir="Weigh each factor: decisive, contributing or minor — and always give the argument AND its limit. Speculation explains the suddenness of the fall, not why it lasted a decade.",
         beats=[
        "{wk}The course adds a worksheet: weighing the causes. For each of nine factors, decide: "
        "{!decisive}decisive, contributing, or minor. Then test your choice against an argument… and its limit. "
        "A good essay paragraph contains both.",
        "{-wk}{fac}Four examples. {fac.1}Speculation: buying on credit multiplied the losses. "
        "But it explains the suddenness of the fall, not why it lasted a decade. "
        "{fac.2}Overproduction: output outran what wages could buy. But it is a structural weakness, not a trigger: it had existed for years.",
        "{fac.3}The unequal distribution of wealth: mass consumption could not absorb mass production. "
        "But it explains the depth of the Depression better than the timing of the Crash. "
        "{fac.4}And panic: selling because others sell turned a fall into a collapse. But panic is a consequence of the fall, so it cannot be its origin.",
        "{-fac}{ex3}Your turn now. A part a), written for this video: "
        "explain how the Wall Street Crash became a world-wide depression.",
        "{-ex3}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is a model plan, in three reasons. {rep1.1}First, because the banks failed, carrying the crash into the real economy: "
        "about five thousand by 1932, with no deposit insurance. {rep1.2}Second, because Europe depended on American credit: "
        "the Dawes circuit broke when the loans were recalled, and the dominoes fell from Vienna to London in 1931. "
        "{rep1.3}Third, because of gold and falling prices. The gold standard forced every country to raise its interest rates. "
        "And falling prices ruined the exporters of raw materials, like Brazil and Chile.",
    ], vis={
        "wk": dict(type="note", terme="Worksheet · weighing the causes", cles=["decisive", "contributing", "minor"],
                   t="Nine factors. For each one: decisive, contributing or minor? Then test it against the argument and its limit.",
                   etape="A good essay paragraph contains both.", x=170, y=200, w=940),
        "fac": dict(type="liste", titre="Argument … and limit", items=[
            "Speculation: credit multiplied losses — but explains the suddenness, not the decade",
            "Overproduction: output outran wages — a structural weakness, not a trigger",
            "Unequal wealth: mass consumption could not absorb mass production — depth, not timing",
            "Panic: turned a fall into a collapse — a consequence, not an origin"], x=130, y=120, w=1020),
        "ex3": dict(type="exo", niveau="essay", titre="Explain how the Wall Street Crash became a world-wide depression.",
                    src="Question written for this video", enonce=["Part a) of an essay · three reasons, each with an example"]),
        "pa1": dict(type="pause", t="Find three reasons, each with a precise example from the course.",
                    sous="Pause the video, write your three reasons, then play on for a model."),
        "rep1": dict(type="liste", titre="A model plan", cles=["because"], items=[
            "Because the banks failed: ≈ 5,000 by 1932, no deposit insurance",
            "Because Europe hung on US credit: the Dawes circuit broke, dominoes in 1931",
            "Because gold and falling prices spread it: interest rates, Brazil, Chile"], x=150, y=140, w=980),
    }),

    # ================================================================ I.3 idée 1 : emplois, salaires, épargne
    dict(id="vies", chap="I.3 · No safety net", fond="guerre", humeur="mystere",
         retenir="USA: production −40%, 14 million unemployed (25% of workers; 3% in 1929), 5,000 banks bankrupt — and no unemployment insurance, no social security, no public pension before 1935.",
         beats=[
        "{pain}Part three of the chapter has a strong title: {!defining traumas}one of the defining traumas of the twentieth century. "
        "Now we leave the banks, and look at people.",
        "{-pain}{gr}{gr.1}First, unemployment in the United States. Three per cent in 1929. Twenty-five per cent in 1933. "
        "One worker in four: fourteen million Americans.",
        "{-gr}{chi}And the other figures of the course. {chi.1}Industrial and farm production fell by forty per cent. "
        "{chi.2}Wages, says the course, fell by sixty per cent. Careful with that figure. Outside the course: "
        "it is close to the fall in the total wage bill of industry, which more than halved because of lay-offs and short hours. "
        "The hourly pay of a worker who kept his job fell much less: by about a fifth. {chi.3}Five thousand banks had gone bankrupt. "
        "{chi.4}Farm prices had plummeted, because of overproduction, drought and the Dust Bowl. "
        "{chi.5}And American exports broke down, as trading partners closed their markets.",
        "{-chi}{fil}But the worst is this. {fil.1}There was no federal unemployment insurance. {fil.2}No social security. "
        "{fil.3}No public pension: the first federal pension came in 1935. {fil.4}And no deposit insurance before 1933.",
        "{-fil}{fm}A family could go from comfortable to destitute in a month. "
        "So {!depression}depression means here not a statistic, but the disappearance of every safety net at once.",
    ], vis={
        "pain": dict(type="tableau", img="h1-soupkitchen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .45],
                     legende="Unemployed men queued outside a soup kitchen, Chicago, February 1931 (US National Archives, public domain)"),
        "gr": dict(type="graphe", titre="US unemployment (course figures)", x=300, y=110, w=680, h=500,
                   ax=dict(x=[1928.5, 1933.5], y=[0, 30], gx=[1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30], lx="year", ly="% of workers"),
                   el=[dict(type="droite", pts=[[1929, 3], [1933, 25]], c="ca", tir=True, dur=1.6),
                       dict(type="points", pts=[[1929, 3], [1933, 25]], c="sa", lbl="3% → 25% · 14 million", lp=[1930.6, 22])]),
        "chi": dict(type="liste", titre="The United States, 1929 – 1933 (course)", items=[
            "Industrial and farm production: −40%", "Wages: −60% (course) — the total wage bill; hourly pay ≈ −20%", "5,000 banks bankrupt",
            "Farm prices collapse: overproduction, drought, Dust Bowl", "Exports break down: markets closed"], x=150, y=110, w=980),
        "fil": dict(type="liste", titre="No safety net", items=[
            "No federal unemployment insurance", "No social security", "No public pension (first federal one: 1935)",
            "No deposit insurance (before 1933)"], x=170, y=130, w=940),
        "fm": dict(type="mot", t="Comfortable → destitute in a month", g="every safety net gone at once", y=260, taille=70),
    }),

    # ================================================================ I.3 idée 2 : Hoovervilles
    dict(id="hoover", chap="I.3 · Hoovervilles", fond="guerre", humeur="mystere",
         retenir="Hoovervilles: shanty towns of scrap wood, stone and metal built by evicted people, often in the heart of big cities, named after President Hoover — a political verdict. Largest in St Louis; one in Central Park; Al Capone's soup kitchen in Chicago (winter 1930–31).",
         beats=[
        "{hv}Second idea: the Hoovervilles made poverty visible, in the middle of American cities. "
        "People evicted from their homes built shanty towns out of scrap wood, stone and metal, on waste ground, "
        "often in the heart of major cities.",
        "{-hv}{nom}Why that name? They were named after {!President Hoover}President Hoover, whom public opinion held responsible for the crisis. "
        "So the name itself is a political verdict.",
        "{-nom}{g7}{g7.1}The largest Hooverville was in St Louis. Another one occupied part of Central Park, in New York: "
        "poverty in the centre of the wealthiest country in the world.",
        "{-g7}{capf}{cap}And a strange detail of the course. In Chicago, in the winter of nineteen thirty to thirty-one, the gangster {!Al Capone}Al Capone ran a soup kitchen. "
        "Charity… but also a bid for public sympathy, from a man under federal investigation.",
        "{-cap}{-capf}{or1}The Hoovervilles are the first oral topic of the course. Prepare four questions. "
        "{or1.1}What? {or1.2}Where? {or1.3}Who? {or1.4}And when? The answers are on the screen.",
    ], vis={
        "hv": dict(type="tableau", img="h1-hooverville", de=[1.0, .5, .5], a=[1.15, .45, .5],
                   legende="Hooverville on the Seattle tideflats, 7 February 1933 (Seattle Municipal Archives, Wikimedia Commons, CC BY 2.0)"),
        "nom": dict(type="def", terme="Hooverville", cles=["evicted", "Hoover", "verdict"],
                    t="A shanty town built by evicted people, named after President Hoover, held responsible for the crisis.",
                    etape="The name itself is a political verdict.", x=170, y=200, w=940),
        "g7": dict(type="globe", code="H1", sc=[11]),
        "capf": dict(type="tableau", img="h1-soupkitchen", fond=True, sombre=True, de=[1.0, .3, .3], a=[1.2, .35, .3],
                     legende="The soup kitchen opened by Al Capone, Chicago, February 1931 (US National Archives, public domain)"),
        "cap": dict(type="note", terme="Chicago, winter 1930 – 1931", cles=["soup kitchen", "sympathy"],
                    t="Al Capone runs a soup kitchen: charity, and a bid for public sympathy from a gangster under federal investigation.",
                    etape="An example from the course", x=170, y=200, w=940),
        "or1": dict(type="liste", titre="Oral topic · the Hoovervilles", items=[
            "What: shanty towns of scrap wood, stone and metal", "Where: waste ground in big cities — St Louis, Central Park",
            "Who: evicted families, the unemployed", "When: the early 1930s, under Hoover"], x=170, y=130, w=940),
    }),

    # ================================================================ I.3 idée 3 : Lange et la photographie
    dict(id="lange", chap="I.3 · Photography as an argument", fond="nuit", humeur="calme",
         retenir="The federal state documented poverty: Dorothea Lange (1895–1965), White Angel Breadline (1933), then Migrant Mother (March 1936, Nipomo, California) for a federal agency. A composed image (a series of exposures, closer and closer), made to win support for relief.",
         beats=[
        "{etat}Third idea, and a surprising one: the federal state itself documented poverty, and turned photography into an argument for reform.",
        "{-etat}{dl}The photographer is {!Dorothea Lange}Dorothea Lange, from 1895 to 1965. {dl.1}In 1933 she photographs the "
        "White Angel soup kitchen in San Francisco. {dl.2}Then she works for a federal agency, the Resettlement Administration, "
        "which later became the Farm Security Administration. She photographs the migrant farm workers of California.",
        "{-dl}{mm}In March 1936, at a pea-pickers' camp in Nipomo, California, she photographs {!Florence Owens Thompson}Florence Owens Thompson, "
        "thirty-two years old, living in a tent with her seven children. This is Migrant Mother.",
        "Look at the composition. The mother's gaze goes out of the frame. The children turn their faces away.",
        "{-mm}{rec}Lange's own account matters for source analysis. She says she approached",
        ("C", "as if drawn by a magnet", "c_aimant"),
        "{-c_aimant}and that she made five exposures,",
        ("C", "working closer and closer from the same direction", "c_proche"),
        "{-c_proche}She learned that the family had been living on frozen vegetables from the field and on birds the children caught. "
        "The pea crop had frozen, and there was no work. And they could not move on: the mother had sold the tyres of the car to buy food.",
        "{-rec}{cmp}So what is this photograph? {cmp.1}It is composed, not accidental: a series of exposures, closer and closer. "
        "{cmp.2}And it was made with a purpose: to win public support for relief programmes. "
        "{cmp.3}Published at once, the image helped bring federal relief to the camp.",
    ], vis={
        "etat": dict(type="question", t="Why would a state photograph its own poverty?"),
        "dl": dict(type="liste", titre="Dorothea Lange (1895 – 1965)", items=[
            "1933: the White Angel soup kitchen, San Francisco", "For a federal agency, the Resettlement Administration (later the FSA): migrant workers in California"],
            x=170, y=160, w=940),
        "mm": dict(type="tableau", img="h1-lange-migrant", de=[1.0, .5, .3], a=[1.12, .5, .28],
                   legende="Dorothea Lange, Migrant Mother, Nipomo, California, March 1936 (Library of Congress, public domain)"),
        "rec": dict(type="tableau", img="h1-lange-migrant", fond=True, sombre=True, de=[1.12, .5, .28], a=[1.2, .5, .3],
                    legende="Dorothea Lange, Migrant Mother, March 1936 (public domain)"),
        "c_aimant": dict(type="cit", a="Dorothea Lange", o="her account of the photograph", x=200, y=190, w=880),
        "c_proche": dict(type="cit", a="Dorothea Lange", o="her account of the photograph", x=200, y=190, w=880),
        "cmp": dict(type="liste", titre="A photograph as an argument", cles=["composed", "purpose", "relief"], items=[
            "Composed, not accidental: a series of exposures", "Made with a purpose: support for relief programmes",
            "Published at once: federal relief sent to the camp"], x=170, y=150, w=940),
    }),

    # ================================================================ pause 2 : DBQ Migrant Mother
    dict(id="dbq", chap="Your turn · DBQ on Migrant Mother", fond="aube", humeur="tension",
         retenir="DBQ a): judgement first (largely / significantly / partly / slightly useful) · the document in one sentence · strengths (several arguments) · limits (several arguments).",
         beats=[
        "{ex4}Now a DBQ, written for this video. {!How useful}How useful is Migrant Mother, by Dorothea Lange, for understanding "
        "the social impact of the Great Depression in the United States?",
        "{-ex4}{str}Remember the structure, every time. {str.1}First line: your judgement. Largely, significantly, partly or slightly useful. "
        "{str.2}Then the document in one sentence. {str.3}Then a paragraph of strengths, with several arguments. "
        "{str.4}Then a paragraph of limits, also with several arguments.",
        "{-str}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}A model. {rep2.1}Migrant Mother is significantly useful for understanding the social impact of the Great Depression in the United States. "
        "{rep2.2}It is a photograph taken by Dorothea Lange for a federal agency, in March 1936, at a pea-pickers' camp in Nipomo, California, "
        "showing Florence Owens Thompson, aged thirty-two, and her children.",
        "{-rep2}{fo}Its strengths. {fo.1}It is a precise, dated and located source: a real family, in a real camp. "
        "{fo.2}It shows what the figures cannot: hunger, a tent, a family with no safety net. "
        "{fo.3}With Lange's account, it shows the rural side of the crisis: frozen crops, no work, the car's tyres sold for food. "
        "{fo.4}And its provenance is itself evidence: the federal state was documenting poverty to justify relief.",
        "{-fo}{li}Its limits. {li.1}It is composed: a series of exposures, the gaze, the children turned away. "
        "{li.2}It was made with a purpose, to win support for relief programmes: it is an argument, not a neutral record. "
        "{li.3}It shows one family, of migrant farm workers in California: not the fourteen million unemployed in the cities, "
        "not the Hoovervilles, not the bank failures. {li.4}And, outside the course: Florence Thompson said later that Lange never asked her name, "
        "and her family had already left when the food arrived. Her own voice is missing.",
        "{-li}{bl}So the judgement holds: significantly useful, but only if you read it as an argument, and set it beside the figures of the course.",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="How useful is Migrant Mother (Dorothea Lange, March 1936) for understanding the social impact of the Great Depression in the United States?",
                    src="Question written for this video, on a document of the course", enonce=["Part a) of a DBQ"]),
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Write the first two lines: your judgement, then the document in one sentence.",
                    sous="Pause the video, then go on: strengths, limits. Play on for a model."),
        "rep2": dict(type="note", terme="A model opening", cles=["significantly", "federal", "Nipomo"],
                     t="Migrant Mother is significantly useful for understanding the social impact of the Depression. "
                       "It is a photograph taken by Dorothea Lange for a federal agency at Nipomo, California, in March 1936.",
                     etape="Judgement · the document in one sentence", x=150, y=180, w=980),
        "fo": dict(type="liste", titre="Strengths", items=[
            "Precise, dated, located: a real family, a real camp", "Shows what figures cannot: hunger, a tent, no safety net",
            "With Lange's account: frozen crops, no work, tyres sold", "Provenance as evidence: the state documents poverty"],
            x=150, y=130, w=980),
        "li": dict(type="liste", titre="Limits", items=[
            "Composed: a series of exposures, made to move", "A purpose: support for relief — an argument",
            "One rural family: not the 14 million, not the cities", "Outside the course: the mother's own voice is missing"],
            x=150, y=130, w=980),
        "bl": dict(type="mot", t="Significantly useful", g="read it as an argument, beside the figures", y=260, taille=84),
    }),

    # ================================================================ I.3 idée 4 : Dust Bowl
    dict(id="dust", chap="I.3 · The Dust Bowl", fond="guerre", humeur="tension",
         retenir="The Dust Bowl: severe drought + mechanised ploughing without dryland farming methods → wind erosion. Black Sunday, 14 April 1935; Stratford, Texas, 1935; “dust pneumonia”. Families ruined twice left for California.",
         beats=[
        "{ds}Fourth idea: the Dust Bowl turned an economic crisis into an ecological one.",
        "{-ds}{cau}Two causes. {cau.1}A severe drought, in the 1930s. {cau.2}And a failure to apply dryland farming methods "
        "to prevent wind erosion. Mechanised ploughing had stripped the Great Plains of the deep grasses that held the soil. "
        "{cau.3}When the rains failed, the exposed topsoil rose into storms that buried farms and made whole counties unliveable.",
        "{-cau}{nat}So the disaster was {!not simply natural}not simply natural. It was the price of a farming technique "
        "that relied on heavy machinery, without regard for the soil.",
        "{-nat}{g8}{g8.1}The example. A dust storm photographed approaching Stratford, Texas, in 1935, fills the sky like a wall. "
        "And Black Sunday, the fourteenth of April 1935, turned day into night across Oklahoma and Texas. "
        "Dust pneumonia killed children and the old.",
        "{-g8}{dep}Ruined twice over, by prices and by dust, families left for California. And that is where Dorothea Lange found them.",
    ], vis={
        "ds": dict(type="tableau", img="h1-dustbowl", de=[1.0, .5, .5], a=[1.12, .5, .45],
                   legende="Dust storm approaching Stratford, Texas, 1935 (George E. Marsh Jr., NOAA, Wikimedia Commons, public domain)"),
        "cau": dict(type="liste", titre="Why the Dust Bowl?", items=[
            "Severe drought in the 1930s", "No dryland farming methods: mechanised ploughing stripped the deep grasses",
            "Exposed topsoil → dust storms bury farms and counties"], x=170, y=140, w=940),
        "nat": dict(type="cols", g="Natural", gq="drought: the rains failed", d="Human", dq="heavy machinery, no regard for the soil", vs="+"),
        "g8": dict(type="globe", code="H1", sc=[25]),
        "dep": dict(type="note", terme="Ruined twice over", cles=["prices", "dust", "California"],
                    t="By prices and by dust: families left the Great Plains for California — where Lange found them.",
                    etape="Dust Bowl → migrant workers → Migrant Mother", x=170, y=200, w=940),
    }),

    # ================================================================ I.3 idée 5 : traumatisme mondial mais inégal
    dict(id="inegal", chap="I.3 · Global, but uneven", fond="nuit", humeur="calme",
         retenir="Key term: World-wide Economic Depression. Crash → US Depression → decline in output, mass unemployment, acute deflation worldwide. But economies outside world markets were largely spared: the USSR, in its first Five-Year Plan, barely touched.",
         beats=[
        "{g9}Last idea: the trauma was global… but not evenly distributed.",
        "{g9.1}{ch}The chain of the slides is short. {ch.1}The US Great Crash. {ch.2}The US Great Depression. "
        "{ch.3}Then, worldwide: decline in output, massive unemployment, and acute deflation.",
        "{-ch}{-g9}{kt}But countries not integrated into world stock markets and trade were largely spared. "
        "And that matters for the Key Term: {!World-wide Economic Depression}World-wide Economic Depression. "
        "A world-wide depression does not mean that every country suffered identically.",
        "{-kt}{urss}The example. The Soviet Union, outside the capitalist trading system, and in the middle of its first Five-Year Plan, "
        "was barely touched. That is exactly why Western visitors came home impressed by planning, and why some political models gained prestige in the 1930s.",
    ], vis={
        "g9": dict(type="globe", code="H1", sc=[12]),
        "ch": dict(type="liste", titre="The chain of the slides", items=[
            "US Great Crash", "US Great Depression", "Worldwide: output falls, mass unemployment, acute deflation"],
            x=640, y=440, w=600, petit=True, bande=True),
        "kt": dict(type="def", terme="Key term · World-wide Economic Depression", cles=["integrated", "spared", "identically"],
                   t="A depression that spread across the world economy — but countries not integrated into world markets and trade were largely spared.",
                   etape="World-wide does not mean that every country suffered identically.", x=170, y=200, w=940),
        "urss": dict(type="note", terme="The exception · the USSR", cles=["Five-Year Plan", "planning"],
                     t="Outside the capitalist trading system, in its first Five-Year Plan: barely touched.",
                     etape="Western visitors of the early 1930s came home impressed by planning.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}The banks: the Great Depression really began when numerous banks started failing, "
        "about five thousand by 1932. {carte.2}The channels: the recall of American loans, the broken Dawes circuit, "
        "and the gold standard as the transmission belt. {carte.3}The world: dominoes in Europe in 1931, falling prices in the periphery, "
        "Brazil's coffee and Chile's nitrate. {carte.4}And the trauma: fourteen million unemployed with no safety net, the Hoovervilles, "
        "Migrant Mother, the Dust Bowl… global, but uneven.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: economic nationalism and political responses. How did the countries react? "
        "By closing their borders… and some of them by choosing militarism.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="A WORLD CRISIS", branches=[
            dict(t="The banks", items=["the hinge of the chapter", "≈ 5,000 failed by 1932", "no deposit insurance"]),
            dict(t="The channels", items=["US loans recalled", "Dawes: 800 M · 2.5 bn marks", "gold: the transmission belt"]),
            dict(t="The world", items=["1931: Vienna · Berlin · London", "Brazil's coffee, Chile's nitrate", "France hit in 1932"]),
            dict(t="The trauma", items=["14 million · 25%", "Hoovervilles · Lange", "Dust Bowl · USSR spared"])]),
        "fin": dict(type="mot", t="Next: economic nationalism", g="Episode 3 · Economic nationalism and political responses", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="According to the slides, when did the Great Depression really begin?",
         r=["When numerous banks started failing", "On Black Thursday, 24 October 1929",
            "When Smoot–Hawley was signed", "When Britain left the gold standard"], ok=0, voir="m1",
         ex="A crash lasts days; the banks carried it into the real economy. About 5,000 had failed by 1932."),
    dict(q="Why could a rumour alone empty an American bank before 1933?",
         r=["There was no deposit insurance", "Banks were forbidden to hold gold",
            "The Federal Reserve did not exist", "Savings were held in Europe"], ok=0, voir="ex1",
         ex="When a bank failed, its customers' savings were simply gone."),
    dict(q="Which is a SHORT-TERM cause of the spread of the crisis, according to the course?",
         r=["American banks suddenly recalled their loans to European banks", "Overproduction",
            "Decreasing incomes for farmers", "Over-investment in industry"], ok=0, voir="cc",
         ex="The other three are long-term underlying weaknesses shared by all economies."),
    dict(q="In the Dawes circuit, what did France and Britain pay to the United States?",
         r=["War-debt repayments", "Reparations", "An 800-million-mark loan", "Gold to back the dollar"], ok=0, voir="tri",
         ex="USA → Germany (loan) → France and Britain (reparations) → USA (war debts)."),
    dict(q="Why was the gold standard a ‘transmission belt’?",
         r=["Higher US interest rates drew gold out, forcing other countries to raise their rates",
            "It let countries print money freely", "It fixed world trade prices", "It guaranteed bank deposits"], ok=0, voir="mec",
         ex="Dearer money in a slump: less investment, less spending, everywhere."),
    dict(q="Which country left the gold standard last, and recovered last?",
         r=["France (1936)", "Britain (1931)", "Japan (1931)", "The United States (1933)"], ok=0, voir="fr2",
         ex="The earlier a country left gold, the earlier it recovered."),
    dict(q="What did Brazil do with its coffee between 1931 and 1944?",
         r=["It burned some 78 million bags to hold the price up", "It sold it all to the USSR",
            "It stopped growing coffee", "It used it to repay war debts"], ok=0, voir="per",
         ex="A country that sells one commodity has no cushion."),
    dict(q="Which is a valid LIMIT of Migrant Mother as a source on the Depression?",
         r=["It was composed to win support for relief, and shows one rural family", "It is undated",
            "It was taken after the Second World War", "Its author is unknown"], ok=0, voir="li",
         ex="Five exposures, a purpose, one family: an argument, not a neutral record."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H1 · Parts I.2 and I.3, with the schemas “The Dawes circuit”, “How the crash became a global depression” and the worksheet on weighing the causes) as written on the site; animated map of chapter 1 (site).",
    "Photographs: unemployed men queued outside Al Capone's soup kitchen, Chicago, February 1931 (US National Archives, public domain); "
    "Hooverville on the Seattle tideflats, 1933 (Seattle Municipal Archives, CC BY 2.0); Dorothea Lange, Migrant Mother, 1936 (Library of Congress, public domain); "
    "George E. Marsh Jr., dust storm approaching Stratford, Texas, 1935 (NOAA, public domain); via Wikimedia Commons.",
    "Questions and model answers written for this video. Outside the course: the note on the wage figure (total wage bill vs hourly pay); the Resettlement Administration, Lange's employer in 1936 (the FSA from 1937); the dating of Capone's soup kitchen (winter 1930–31); Florence Owens Thompson's later account.",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
