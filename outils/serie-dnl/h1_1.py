"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 1 : « The Great Crash of 1929 ».

Même chaîne que la série H3 (voir h3_1.py) : outils/serie-philo/generer.py h1_1 ; sortie dans dnl/serie/.
Type globe : la carte animée du chapitre (dnl/cartes/H1.html), sc = numéros de scènes dans l'ordre chronologique :
  H1 : 0 ordre libéral de 1919 · 1 Roaring Twenties · 2 l'économie réelle ralentit · 3 plan Dawes · 4 spéculation · 5 krach
Contenu : bigPicture, objective et link.introEn du chapitre H1 (dnl/index.html, CHAPTERS.H1), puis la partie I.1
« What is the 1929 Great Crash? », ses six idées avec leur exemple principal et le schéma h1speculation (H1BubbleAnim).
Ce qui n'est pas dans le cours est dit « outside the course » (le cours le signale lui-même pour RCA et les voitures).
Courbe du Dow Jones : 100 (1924), 381 (septembre 1929), 41 (juillet 1932) sont les chiffres du cours ; les points
intermédiaires sont des valeurs approchées de l'indice (hors cours), comme dans l'animation du site.
Plan de la série H1 : 1 The Great Crash of 1929 · 2 From an American crash to a world crisis ·
3 Economic nationalism and political responses · 4 Democracies and the liberal order · 5 The crisis at the exam · 6 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-1"
NOTION = "The Wall Street Crash"
NUM = 1
TITRE = "The Great Crash of 1929"
SUIVANT = "Episode 2 · From an American crash to a world crisis"
PRONONCIATION = {"RCA": "R. C. A.", "Coolidge": "Cool-idge", "Nuremberg": "Nyoor-em-berg", "Dawes": "Daws"}

# indice Dow Jones (repères du cours : 100, 381, 41 ; points intermédiaires approchés, hors cours)
DOW_MONTEE = [[1924.0, 100], [1925.0, 122], [1926.0, 157], [1927.0, 155], [1928.0, 200], [1929.0, 300], [1929.67, 381]]
DOW_CHUTE = [[1929.67, 381], [1929.87, 198], [1930.3, 294], [1931.0, 165], [1932.0, 75], [1932.5, 41]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{ph1}{q1}Nineteen twenty-nine. Two photographs open this chapter. The first one: a crowd, silent and solemn, "
        "standing in the street outside the New York Stock Exchange. Thousands of people waiting for news… of their money.",
        "{-q1}{ph2}The second one, the same year, in Germany: Adolf Hitler greeting his supporters at the Nuremberg party congress. "
        "In nineteen twenty-nine, he is still the leader of a small party. Ten years later, he is at war with half of Europe.",
        "{-ph2}{q2}So here is the question that historians still argue about. What caused the Second World War? "
        "The crisis of capitalism that followed the Crash? The threat of totalitarianism? {!Or both}Or both?",
        "{-q2}{-ph1}{winter}The historian Jay Winter gives a bold answer. For him, there was one single war, "
        "a {!thirty years' war}thirty years' war, from nineteen fourteen to nineteen forty-five. Why? Because in between, "
        "peace was never really achieved. The guns stopped in nineteen eighteen… but the conflict went on, by other means.",
        "{-winter}{plan}This series follows the first link in that chain, in six episodes. {plan.1}Today: the Great Crash of 1929, "
        "what it was and why it happened. {plan.2}Then how an American crash became a world crisis. "
        "{plan.3}Then economic nationalism, and the political answers to the crisis. {plan.4}Then the democracies and the liberal order. "
        "{plan.5}After that, an episode only for the exam: essay and DBQ. {plan.6}And a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "ph1": dict(type="tableau", img="h1-wallstreet", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.2, .45, .5],
                    legende="Crowd outside the New York Stock Exchange, October 1929 (Wikimedia Commons, public domain)"),
        "q1": dict(type="question", t="1929: a crowd outside the Stock Exchange.", bande=True),
        "ph2": dict(type="note", terme="The second photograph of 1929", cles=["Hitler", "Nuremberg"],
                    t="Adolf Hitler greeting his supporters at the Nuremberg party congress.",
                    etape="Described here, not shown. In 1929 the Nazi party is still small.", x=170, y=200, w=940),
        "q2": dict(type="question", t="The crisis of capitalism, totalitarianism… or both?", bande=True),
        "winter": dict(type="mot", t="1914 – 1945", g="Jay Winter: one “thirty years' war” — peace was never really achieved",
                       y=250, taille=110),
        "plan": dict(type="liste", titre="H1 · The Wall Street Crash, in six episodes", items=[
            "The Great Crash of 1929 (Part I.1)", "From an American crash to a world crisis (I.2–I.3)",
            "Economic nationalism and political responses (II.1–II.2)", "Democracies and the liberal order (II.3)",
            "The crisis at the exam: essay and DBQ", "Recap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 1", t="The Great Crash of 1929",
                      sous="the stock market · the Roaring Twenties · speculation · the panic of October"),
    }),

    # ================================================================ I. le chapitre et l'ordre de 1919
    dict(id="ordre", chap="The liberal order of 1919", fond="nuit", humeur="calme",
         retenir="The chapter: how a stock-market collapse in one country became a world depression, which pushed the democracies into retreat while three regimes chose militarism.",
         beats=[
        "{g0}{g0.1}This chapter opens Theme One, and it comes right after the peace settlement of nineteen nineteen. "
        "So let's start there. {lib}{lib.1}In nineteen eighteen, President Wilson's Fourteen Points carried three principles: "
        "democracy, self-determination, and free trade.",
        "{lib.2}The Paris Peace Conference, the Treaty of Versailles and the League of Nations, seated in Geneva, gave them institutions. "
        "{lib.3}But the American Senate refused to ratify the treaty. The United States never joined the League that its own president had imagined.",
        "{lib.4}This is the {!liberal order}liberal order of nineteen nineteen. Then came the fragile prosperity of the nineteen twenties. "
        "And this chapter will expose how fragile that order really was.",
        "{-lib}{-g0}{obj}So here is the objective of the whole chapter, in one sentence. Explain how a stock-market collapse "
        "in one country became a world depression… and why that depression pushed the great democracies into economic nationalism "
        "and retreat, while three regimes chose militarism.",
        "{-obj}{chaine}Think of it as a chain. {chaine.1}An American financial collapse. "
        "{chaine.2}It spreads through loans, trade and currencies. {chaine.3}It becomes a world depression. "
        "{chaine.4}And at the end of the chain, the liberal order built in nineteen nineteen is defeated. "
        "Today, we look at the very first link: the Crash itself.",
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[0]),
        "lib": dict(type="liste", titre="The liberal order of 1919", x=60, y=130, w=600, petit=True, bande=True,
                    cles=["democracy", "free trade", "never"], items=[
                        "Wilson's Fourteen Points (1918): democracy, self-determination, free trade",
                        "Versailles and the League of Nations, in Geneva",
                        "The US Senate refuses: the US never joins the League",
                        "Then the fragile prosperity of the 1920s"]),
        "obj": dict(type="def", terme="The chapter's objective", cles=["one country", "world depression", "militarism"],
                    t="Explain how a stock-market collapse in one country became a world depression.",
                    etape="…and why it pushed the democracies into economic nationalism and retreat, while three regimes chose militarism.",
                    x=170, y=200, w=940),
        "chaine": dict(type="liste", titre="The chain of the chapter", items=[
            "An American financial collapse", "Spread through loans, trade and currencies", "A world depression",
            "The liberal order of 1919 defeated"], x=170, y=140, w=940),
    }),

    # ================================================================ II. la chronologie sur la carte
    dict(id="chrono", chap="The story on the map", fond="nuit", humeur="lumiere",
         retenir="1920s: a boom built on mass production and credit · from 1920: farming already in crisis · 1924: Dawes Plan · 1924–29: the market triples · 24–29 Oct. 1929: the Crash.",
         beats=[
        "{g1}Before the course itself, let's tell the story on the map, in five steps. {g1.1}Step one: the nineteen twenties, "
        "the {!Roaring Twenties}Roaring Twenties. Three Republican presidents follow one another: Harding, Coolidge, Hoover. "
        "Low taxes, giant companies, protection against foreign goods.",
        "In Detroit, Henry Ford's factories mass-produce cars. Cars, radios, refrigerators enter ordinary homes. "
        "America enjoys a boom built on mass production and mass consumption. It feels permanent.",
        "{g1.2}Step two. But look away from the cities, to the Great Plains. From nineteen twenty, the real economy is already slowing down. "
        "Farm prices have been falling since the end of the war. Coal, textiles and construction are in trouble too.",
        "{fr2}Why? {fr2.1}Most Americans are poor: they cannot buy everything the factories produce. "
        "{fr2.2}And the Europeans are still recovering from the war: they cannot buy it either. That is overproduction.",
        "{-fr2}{g1.3}Step three, nineteen twenty-four: the Dawes Plan. The United States lends eight hundred million marks to Germany. "
        "Germany pays its reparations to France and Britain. And France and Britain repay their war debts to the United States. "
        "A circle of money… that rests entirely on American credit. Keep this in mind: it is the key to episode two.",
        "{g1.4}Step four, from nineteen twenty-four to nineteen twenty-nine, in New York. On Wall Street, the stock market triples in five years. "
        "By nineteen twenty-nine, about one American household in ten owns shares. People buy shares not for the profits, "
        "but to resell them higher. And often with borrowed money.",
        "{g1.5}And step five. October nineteen twenty-nine. On Thursday the twenty-fourth, panic selling begins. "
        "On Monday the twenty-eighth and Tuesday the twenty-ninth, the market collapses. Everyone sells. Nobody buys. "
        "{!The Wall Street Crash}This is the Wall Street Crash.",
        "Five steps: a boom, a hidden weakness, a circle of credit, a bubble… and the bubble bursts. "
        "Now let's go back over each one, slowly, as the course does.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[1, 2, 3, 4, 5]),
        "fr2": dict(type="liste", titre="Why overproduction?", x=60, y=130, w=600, petit=True, bande=True, items=[
            "Most Americans are poor: they cannot buy", "Europe is still recovering from the war"]),
    }),

    # ================================================================ III. idée 1 : la Bourse
    dict(id="bourse", chap="What is a stock market?", fond="nuit", humeur="calme",
         retenir="A stock market: companies raise money by selling shares. Two rewards: the dividend (a share of profits) or reselling higher, which depends only on the next buyer.",
         beats=[
        "{q3}First idea of the course. What exactly is a stock market?",
        "{-q3}{def3}A stock market is a place where companies raise money, and where investors buy a claim on their profits. "
        "The {!Stock Exchange}Stock Exchange is the building, the facility. The people who work there are traders.",
        "Here is how it works. {-def3}{mec}{mec.1}Large companies need money to grow: they need investors. "
        "{mec.2}So they sell {!shares}shares, small pieces of the company. Whoever buys one becomes a shareholder.",
        "{mec.3}And a shareholder is rewarded in two ways. {mec.4}First way: the {!dividend}dividend, a share of the company's profits, "
        "paid out every year. {mec.5}Second way: selling the share to someone else, for more than it cost.",
        "{-mec}{deux}Look closely at these two ways, because the whole chapter starts here. {deux.g}The dividend depends on the company: "
        "if it makes profits, you are paid. {deux.d}But reselling higher does not depend on the company at all. "
        "It depends only on what the next buyer is prepared to pay. {!That is where the trouble starts}That is where the trouble starts.",
        "{-deux}{rca}An example, which the course itself says comes from outside the course: Radio Corporation of America, RCA, "
        "the star stock of the late nineteen twenties. RCA paid no dividend at all. None. And yet its share price "
        "was multiplied several times in nineteen twenty-eight and nineteen twenty-nine.",
        "So what were buyers paying for? Not for profits. They were paying for what the next buyer would pay. "
        "Remember this: it is the definition of a bubble.",
    ], vis={
        "q3": dict(type="question", t="What exactly is a stock market?"),
        "def3": dict(type="def", terme="Stock market · stock exchange", cles=["raise money", "profits"],
                     t="A place where companies raise money and investors buy a claim on their profits.",
                     etape="The Stock Exchange is the facility; the people who work there are traders.", x=170, y=200, w=940),
        "mec": dict(type="liste", titre="How a stock market works", cles=["shares", "dividend", "resell"], items=[
            "Large companies need investors", "They sell shares: the buyer becomes a shareholder",
            "Two rewards for a shareholder:", "1. the dividend: a share of profits, paid every year",
            "2. selling the share to someone else for more than it cost"], x=170, y=110, w=940),
        "deux": dict(type="cols", g="The dividend", gq="depends on the company: its profits", d="Reselling higher",
                     dq="depends only on the next buyer: the trouble starts here", vs="≠"),
        "rca": dict(type="note", terme="Example · RCA (outside the course)", cles=["no dividend", "several times"],
                    t="Radio Corporation of America paid no dividend at all, yet its share price was multiplied several times in 1928–29.",
                    etape="Buyers paid for what the next buyer would pay, not for profits.", x=170, y=200, w=940),
    }),

    # ================================================================ IV. idée 2 : les Roaring Twenties
    dict(id="twenties", chap="The Roaring Twenties", fond="aube", humeur="lumiere",
         retenir="Republican policy (Harding, Coolidge, Hoover): low taxes, trusts, tariffs; plus credit and marketing, and vast resources. A boom that felt permanent: 8 → 23 million cars, 1920–1929.",
         beats=[
        "{mt}Second idea. The {!Roaring Twenties}Roaring Twenties: growth, optimism and affluence… built on Republican policy.",
        "{rep}Three Republican presidents in a row: Harding, Coolidge, then Hoover. Their policy has three pillars. "
        "{rep.1}One: they keep taxation low. "
        "{rep.2}Two: they allow the development of {!trusts}trusts, giant combinations of companies. "
        "{rep.3}Three: they protect American industry with tariffs, taxes on imported goods.",
        "{rep.4}To this, the decade adds new techniques: new ways to sell, to give credit, to advertise. "
        "With {!instalment plans}instalment plans, a family can buy a car or a refrigerator before it can afford one, and pay month by month. "
        "{rep.5}And America sits on vast natural resources and raw materials.",
        "{-rep}{-mt}The result: a boom that felt permanent. {voit}The best place to see it is the car. "
        "{voit.1}In nineteen twenty, about eight million cars are registered in the United States. "
        "{voit.2}In nineteen twenty-nine, about twenty-three million. Almost three times more, in nine years. "
        "And most of them were bought on credit. These figures come from outside the course, but they are the clearest picture of the boom.",
        "{-voit}{gat}And if you want a novel: The Great Gatsby, published in nineteen twenty-five, is the literary portrait of the decade. "
        "Parties, cars, money… and nobody asking where it all comes from.",
    ], vis={
        "mt": dict(type="tableau", img="h1-modelt", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .55, .55],
                   legende="A 1925 Ford Model T touring, restored (ModelTMitch, Wikimedia Commons, CC BY-SA 4.0)"),
        "rep": dict(type="liste", titre="Why the boom? Republican policy, and more", cles=["taxation", "trusts", "tariffs", "credit"], items=[
            "Low taxation", "Trusts allowed: giant combinations of companies", "Tariffs on imported goods protect industry",
            "New sales, credit and marketing: instalment plans", "Vast natural resources and raw materials"], x=170, y=110, w=940),
        "voit": dict(type="graphe", titre="Cars registered in the United States (outside the course)", x=300, y=110, w=680, h=520,
                     ax=dict(x=[1919, 1930], y=[0, 26], gx=[1920, 1925, 1929], gy=[5, 10, 15, 20, 25], lx="year", ly="million cars"),
                     el=[dict(type="point", x=1920, y=8, c="el", lbl="1920: ≈ 8 million", lp=[1920.4, 10.5]),
                         dict(type="droite", pts=[[1920, 8], [1929, 23]], c="sa", lbl="1929: ≈ 23 million", lp=[1925.6, 24.5], dur=1.6)]),
        "gat": dict(type="mot", t="The Great Gatsby", g="F. Scott Fitzgerald, 1925 · the portrait of the decade", y=260, taille=92),
    }),

    # ================================================================ V. idée 3 : production et consommation de masse
    dict(id="masse", chap="Mass production, mass consumption", fond="nuit", humeur="lumiere",
         retenir="The assembly line cut costs: cars, radios, refrigerators entered ordinary homes (Model T ≈ $260 by 1925). Trusts and monopolies (Standard Oil, Carnegie) made the boom look safer than it was.",
         beats=[
        "{chn}Third idea. {!Mass production}Mass production made mass consumption possible… and concentrated economic power.",
        "Look at this photograph: a Ford assembly line. The product moves past the workers; each worker repeats one simple task. "
        "Assembly-line methods cut the cost of manufactured goods so far that middle-class households can now buy them.",
        "{-chn}{bien}{bien.1}Cars. {bien.2}Radios. {bien.3}Vacuum cleaners. {bien.4}Refrigerators. {bien.5}Washing machines. "
        "For the first time, they enter ordinary homes. Consumer goods are mass-produced, and massively available.",
        "{-bien}{fordt}The main example: the Ford Model T. By nineteen twenty-five, its price has fallen to roughly "
        "{!two hundred and sixty dollars}two hundred and sixty dollars. Within reach of a middle-class family.",
        "{-fordt}{trust}But mass production has a second face. Industries concentrate into {!trusts}trusts and monopolies. "
        "{trust.1}Rockefeller's Standard Oil controls everything in oil: extraction, refining, distribution, and the pumps. "
        "{trust.2}Carnegie does the same for steel. {trust.3}These giants are large enough to set their own prices.",
        "{trust.4}And that is the trap. Giant firms, rising sales, rising profits: the boom looks much more secure than it really is. "
        "That false sense of security is exactly what feeds the next idea: speculation.",
    ], vis={
        "chn": dict(type="tableau", img="h1-assembly", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .5],
                    legende="Ford assembly line, Highland Park, Michigan, 1913 (Wikimedia Commons, public domain)"),
        "bien": dict(type="liste", titre="Consumer goods enter ordinary homes", items=[
            "Cars", "Radios", "Vacuum cleaners", "Refrigerators", "Washing machines"], x=170, y=110, w=940),
        "fordt": dict(type="mot", t="≈ $260", g="the price of a Ford Model T by 1925: within reach of a middle-class family", y=250, taille=120),
        "trust": dict(type="liste", titre="The other face: trusts and monopolies", cles=["Standard Oil", "Carnegie", "prices", "secure"], items=[
            "Rockefeller's Standard Oil: extraction, refining, distribution, pumping", "Carnegie: the same for steel",
            "Large enough to set their own prices", "The boom looks more secure than it is"], x=170, y=130, w=940),
    }),

    # ================================================================ VI. idée 4 : la spéculation (schéma h1speculation)
    dict(id="specu", chap="Speculation: the bubble", fond="nuit", humeur="tension",
         retenir="Speculation: buying to resell higher, often on credit. The market tripled 1924–29; 10% of households held shares; brokers lent up to 90%: a 10% fall wiped a buyer out.",
         beats=[
        "{def4}Fourth idea, the heart of the episode. {!Speculation}Speculation. To speculate is to treat the stock market "
        "as an easy way to increase your income quickly: you buy a share not for the dividend, but to resell it higher.",
        "{-def4}{bul}It is a new trend in the nineteen twenties, and it spreads fast. Watch the Dow Jones, the index of the big American shares. "
        "{bul.1}In nineteen twenty-four, it stands at about one hundred. Shares are still bought for their dividends. "
        "{bul.2}Then prices rise faster than profits. Between nineteen twenty-four and nineteen twenty-nine, the market {!triples}triples in five years.",
        "{bul.3}By nineteen twenty-nine, about ten per cent of American households own shares, and demand for shares is at an all-time high. "
        "In September nineteen twenty-nine, the index reaches three hundred and eighty-one. The bubble is at its largest.",
        "Why does nobody stop? Because prices have only ever risen. So buying on credit seems perfectly rational. "
        "{-bul}{cred}{cred.1}Borrow. {cred.2}Buy. {cred.3}Resell higher. {cred.4}Repay, and keep the difference. It works… as long as prices rise.",
        "Here is the example of the course. Brokers lend their clients up to ninety per cent of a share's price. "
        "This is called {!buying on margin}buying on margin. Let's do the sum. {-cred}{marg}{marg.1}A share costs one hundred dollars. "
        "{marg.2}You pay ten dollars; the broker lends you ninety.",
        "{marg.3}Now the market falls by just ten per cent. Your share is worth ninety dollars. "
        "{marg.4}You still owe the broker ninety. Your ten dollars are gone. With a fall of only ten per cent, you are {!wiped out}wiped out.",
        "{-marg}{fin4}And that is why a moderate fall became a stampede. The moment prices stop rising, the borrowed money still has to be repaid… "
        "out of shares worth less. So people must sell. And when they sell, prices fall further.",
    ], vis={
        "def4": dict(type="def", terme="Speculation", cles=["resell", "higher"],
                     t="Buying an asset in the hope of reselling it at a higher price, rather than for the income it produces.",
                     etape="A new trend of the 1920s, often financed on credit.", x=170, y=200, w=940),
        "bul": dict(type="graphe", titre="The bubble · Dow Jones index, 1924–1929", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1923.6, 1930.2], y=[0, 420], gx=[1924, 1925, 1926, 1927, 1928, 1929], gy=[100, 200, 300, 400],
                            lx="year", ly="index"),
                    el=[dict(type="point", x=1924, y=100, c="el", lbl="1924: ≈ 100", lp=[1924.2, 130]),
                        dict(type="courbe", pts=DOW_MONTEE, c="sa", dur=3.0),
                        dict(type="point", x=1929.67, y=381, c="ca", lbl="Sept. 1929: 381", lp=[1927.4, 405])]),
        "cred": dict(type="liste", titre="Buying on credit: a circle", items=["Borrow", "Buy shares", "Resell higher", "Repay, keep the profit"],
                     x=170, y=130, w=940),
        "marg": dict(type="formule", titre="Buying on margin: the course's example", lignes=[
            dict(f="A share costs $100", n="the price"),
            dict(f="You pay $10 · the broker lends $90", n="up to 90% lent"),
            dict(f="The market falls 10% → the share is worth $90", n="a moderate fall"),
            dict(f="You owe $90: your $10 is gone", n="wiped out", cadre=True)]),
        "fin4": dict(type="mot", t="A fall → a stampede", g="borrowed money must be repaid out of shares worth less", y=260, taille=86),
    }),

    # ================================================================ VII. idée 5 : l'économie réelle
    dict(id="reelle", chap="The real economy was already slowing", fond="nuit", humeur="mystere",
         retenir="Before the Crash, farming, coal, textiles and construction were in trouble: overproduction, because most Americans were poor and Europe was still recovering. Farm prices had fallen since 1920.",
         beats=[
        "{g2}Fifth idea, and it is the one students forget. {!Meanwhile}Meanwhile, the real economy had already started its downturn.",
        "{sec}The slides make the point in one diagram. Before the Crash, several sectors are already in trouble. "
        "{sec.1}Farming. {sec.2}Coal. {sec.3}Textiles, and the other traditional trades. {sec.4}And the construction industry.",
        "{-sec}{-g2}{para0}Why? Because consumer goods are massively available… more than the market can absorb. "
        "That is overproduction, and overproduction leads to recession. {-para0}{surp}{surp.g}Two facts explain it. "
        "First, the majority of Americans are poor: they cannot buy what the factories produce. "
        "{surp.d}Second, the Europeans are still recovering from the First World War: they cannot buy it either.",
        "The main example is the farmer. During the war, American farmers borrowed money to mechanise, "
        "to feed Europe. Then peace came. {-surp}{ferme}{ferme.1}Prices fell. {ferme.2}The debts did not. "
        "{ferme.3}Farm prices have been falling since nineteen twenty. The rural crisis is {!nine years older}nine years older than the Crash.",
        "{-ferme}{para}So here is the paradox to remember. {para.g}The stock market rises all through nineteen twenty-nine… "
        "{para.d}on an economy that is already shrinking. Share prices and the real economy have separated. Sooner or later, they must meet again.",
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[2], dt=1.5),
        "sec": dict(type="liste", titre="Already in trouble before the Crash", x=60, y=130, w=600, petit=True, bande=True, items=[
            "Farming", "Coal", "Textiles and other traditional trades", "Construction"]),
        "para0": dict(type="mot", t="Overproduction", g="more goods than the market can absorb → recession", y=260, taille=96),
        "surp": dict(type="cols", g="Most Americans are poor", gq="they cannot buy what the factories produce", d="Europe is recovering",
                     dq="from the First World War: it cannot buy either", vs="+", repere="→ overproduction and recession"),
        "ferme": dict(type="liste", titre="Example · the farmers", cles=["1920", "nine years"], items=[
            "They borrowed to mechanise during the war", "Peace: lower prices… and unchanged debts",
            "Farm prices falling since 1920: the rural crisis is nine years older than the Crash"], x=170, y=140, w=940),
        "para": dict(type="cols", g="The stock market", gq="rises all through 1929", d="The real economy", dq="is already shrinking", vs="≠"),
    }),

    # ================================================================ VIII. idée 6 : la panique d'octobre
    dict(id="panique", chap="October 1929: the panic", fond="guerre", humeur="tension",
         retenir="Black Thursday 24 Oct. · Black Monday 28 Oct. (≈ −13%) · Black Tuesday 29 Oct. (≈ −12%, 16 million shares). Everyone sells, nobody buys. Dow Jones: 381 (Sept. 1929) → 41 (July 1932), −89%; back to its 1929 level only in 1954.",
         beats=[
        "{g3}Sixth idea. In late October nineteen twenty-nine, the financial panic begins… and the selling feeds on itself.",
        "{-g3}{trois}Three days carry the story. {trois.1}Thursday the twenty-fourth of October: {!Black Thursday}Black Thursday. "
        "Panic selling begins, and a crowd gathers outside the Exchange, like the one in our first photograph.",
        "{trois.2}Monday the twenty-eighth: the market loses roughly thirteen per cent, in a single session. "
        "{trois.3}Tuesday the twenty-ninth: roughly twelve per cent more. In one day, about sixteen million shares change hands, "
        "a record that stands for forty years.",
        "The logic is circular. {-trois}{cerc}{cerc.1}Everyone tries to sell at once. {cerc.2}So there are no buyers. "
        "{cerc.3}So prices fall further. {cerc.4}So more people sell, at any price… and the circle starts again.",
        "{-cerc}{cle6}And here is the key sentence for an essay. Shareholders were not selling because they had changed their minds "
        "about American industry. {!because everyone else was}They were selling because everyone else was. That is what a panic is.",
        "{-cle6}{chute}Now look at the whole fall. {chute.1}From its peak of three hundred and eighty-one in September nineteen twenty-nine… "
        "{chute.2}the Dow Jones goes down, with a brief rebound in nineteen thirty, outside the course… "
        "{chute.3}to forty-one in July nineteen thirty-two. A loss of {!eighty-nine per cent}eighty-nine per cent.",
        "And the index will not regain its nineteen twenty-nine level until nineteen fifty-four. A quarter of a century. "
        "Shares bought on credit are now worth almost nothing.",
        "{-chute}{def6}So you can now define the key term precisely. {!The Great Crash}The Great Crash of 1929 is the collapse of American share prices "
        "in late October nineteen twenty-nine. Be careful: it is not the same thing as the Depression that followed. "
        "The Crash is a few days in October; the Depression lasts ten years. That is episode two.",
    ], vis={
        "g3": dict(type="globe", code="H1", sc=[5], dt=1.5),
        "trois": dict(type="liste", titre="Three days in October 1929", cles=["Black Thursday", "13%", "12%", "16 million"], items=[
            "Thursday 24 Oct. · Black Thursday: panic selling, a crowd outside the Exchange",
            "Monday 28 Oct. · Black Monday: ≈ −13% in one session",
            "Tuesday 29 Oct. · Black Tuesday: ≈ −12%; 16 million shares, a record for 40 years"], x=150, y=140, w=980),
        "cerc": dict(type="liste", titre="A circle of panic", items=[
            "Everyone tries to sell at once", "No buyers", "Prices fall further", "More people sell, at any price ↺"], x=170, y=130, w=940),
        "cle6": dict(type="note", terme="The key sentence for an essay", cles=["changed their minds", "everyone else"],
                     t="Shareholders did not sell because they had changed their minds about American industry, but because everyone else was selling.",
                     etape="That is what a panic is.", x=170, y=200, w=940),
        "chute": dict(type="graphe", titre="The collapse · Dow Jones index, 1929–1932", x=300, y=110, w=680, h=520,
                      ax=dict(x=[1929.4, 1932.8], y=[0, 420], gx=[1930, 1931, 1932], gy=[100, 200, 300, 400], lx="year", ly="index"),
                      el=[dict(type="point", x=1929.67, y=381, c="sa", lbl="Sept. 1929: 381", lp=[1929.9, 405]),
                          dict(type="courbe", pts=DOW_CHUTE, c="ca", dur=3.0),
                          dict(type="point", x=1932.5, y=41, c="ca", lbl="July 1932: 41 (−89%)", lp=[1931.3, 95])]),
        "def6": dict(type="def", terme="Key term · the Great Crash (1929)", cles=["late October 1929", "not"],
                     t="The collapse of American share prices in late October 1929.",
                     etape="Not the same as the Depression that followed: a few days, against ten years.", x=170, y=200, w=940),
    }),

    # ================================================================ IX. à toi : un sujet d'essay
    dict(id="essay", chap="Your turn: an essay question", fond="aube", humeur="calme",
         retenir="Assess = rank the factors. Speculation is the trigger; structural weaknesses (overproduction, inequality, the farm crisis) explain the depth; panic and policy are amplifiers.",
         beats=[
        "{ki}Now, your turn. Here is the essay question that the site gives for this part. "
        "{!Assess}Assess the role of each factor in triggering the Crash of nineteen twenty-nine. Which was the most important?",
        "You have all the factors. {-ki}{fac}{fac.1}Republican policy. {fac.2}Mass production and the trusts. {fac.3}Speculation on credit. "
        "{fac.4}The real economy already in decline. {fac.5}And the panic. The word assess means: do not list them. {!Rank them}Rank them.",
        "{-fac}{pa1}",
        ("P", 3.0),
        "{-pa1}{intro1}Here is one way to do it. Start the introduction with three moves. {intro1.1}Define the Crash precisely: "
        "the collapse of American share prices in late October nineteen twenty-nine, distinct from the Depression that followed. "
        "{intro1.2}State the problem: the factors are not independent, they reinforce each other. So the question is: which one do the others depend on? "
        "{intro1.3}And announce a hierarchy, not a list.",
        "{-intro1}{arg}Then three parts. {arg.1}One: speculation is the strongest candidate for the trigger. The market tripled between "
        "nineteen twenty-four and nineteen twenty-nine; brokers lent up to ninety per cent, so a ten per cent fall wiped a buyer out. "
        "But speculation explains the suddenness of the fall… not its depth.",
        "{arg.2}Two: structural weaknesses explain why the fall became catastrophic. Overproduction, and an unequal distribution of wealth: "
        "most Americans were too poor to buy what the factories made. Europe could not buy either. And farming had been in crisis since nineteen twenty.",
        "{arg.3}Three: confidence and policy were amplifiers, not the origin. The panic explains the mechanism, selling because others sell, "
        "but it is itself a consequence of the fall. Republican policy, low taxes, trusts, tariffs, easy credit, created the conditions, "
        "without causing the collapse directly.",
        "{-arg}{ccl}And the conclusion, in one sentence. Speculation {!triggered}triggered the Crash; structural overproduction and inequality "
        "{!determined}determined that it would not correct itself. Ranking the factors matters more than listing them: that is what assess asks for.",
    ], vis={
        "ki": dict(type="question", t="Assess the role of each factor in triggering the Crash of 1929. Which was the most important?"),
        "fac": dict(type="liste", titre="The factors on the table", items=[
            "Republican policy: low taxes, trusts, tariffs, credit", "Mass production and the trusts", "Speculation on credit (margin)",
            "The real economy already in decline", "The panic of October"], x=170, y=110, w=940),
        "pa1": dict(type="pause", t="Assess the role of each factor in triggering the Crash of 1929. Which was the most important?",
                    sous="Pause the video. Write your introduction and a three-part plan, with a hierarchy, then play on for a model."),
        "intro1": dict(type="liste", titre="A model introduction: three moves", items=[
            "Define the Crash: late October 1929 — not the Depression", "The problem: the factors reinforce each other",
            "Announce a hierarchy, not a list"], x=170, y=140, w=940),
        "arg": dict(type="liste", titre="A model plan, with evidence", cles=["trigger", "catastrophic", "amplifiers"], items=[
            "I. Speculation, the trigger: ×3 in five years, 90% lent · limit: explains the suddenness, not the depth",
            "II. Structural weaknesses made it catastrophic: overproduction, poor majority, Europe, farms since 1920",
            "III. Panic and Republican policy: amplifiers and conditions, not the origin"], x=150, y=130, w=980),
        "ccl": dict(type="note", terme="Conclusion", cles=["triggered", "determined"],
                    t="Speculation triggered the Crash; structural overproduction and inequality determined that it would not correct itself.",
                    etape="Assess = rank the factors, not list them.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}A stock market: two rewards, the dividend… or reselling higher, which depends only on the next buyer. "
        "{carte.2}The boom: Republican policy, mass production, the Model T at two hundred and sixty dollars, cars on credit. "
        "{carte.3}The weakness: speculation on margin, ninety per cent borrowed, and a real economy already shrinking since nineteen twenty. "
        "{carte.4}And the panic: twenty-four, twenty-eight, twenty-nine October nineteen twenty-nine, and a fall from three hundred and eighty-one to forty-one.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: how this American crash became a world crisis. Banks that fail, loans recalled from Europe… "
        "and the circle of the Dawes Plan that breaks.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="THE GREAT CRASH", branches=[
            dict(t="Stock market", items=["shares · shareholders", "dividend or resale", "RCA: no dividend"]),
            dict(t="The boom", items=["low taxes · trusts · tariffs", "Model T ≈ $260 (1925)", "Standard Oil · Carnegie"]),
            dict(t="The weakness", items=["market ×3, 1924–29", "margin: up to 90% lent", "farms in crisis since 1920"]),
            dict(t="The panic", items=["24 · 28 · 29 Oct. 1929", "381 → 41 (−89%)", "back to 1929 level: 1954"])]),
        "fin": dict(type="mot", t="Next: a world crisis", g="Episode 2 · From an American crash to a world crisis", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="What are the two ways a shareholder can be rewarded?",
         r=["The dividend, or reselling the share for more than it cost", "A salary and a pension", "Interest and tax relief",
            "The dividend and a government bonus"], ok=0, voir="mec",
         ex="The second way, reselling higher, depends only on the next buyer: that is where speculation starts."),
    dict(q="Why is the RCA example a sign of a bubble?",
         r=["It paid no dividend, yet its price multiplied several times", "It went bankrupt in 1925",
            "Its profits tripled every year", "The government fixed its price"], ok=0, voir="rca",
         ex="Buyers paid for what the next buyer would pay, not for profits (example from outside the course)."),
    dict(q="Which of these was NOT part of Republican policy in the 1920s?",
         r=["High taxes on the rich", "Low taxation", "Allowing trusts", "Tariffs on imported goods"], ok=0, voir="rep",
         ex="Harding, Coolidge and Hoover kept taxes low, let trusts grow and protected industry with tariffs."),
    dict(q="By 1925, roughly how much did a Ford Model T cost?",
         r=["About $260", "About $2,600", "About $26", "About $26,000"], ok=0, voir="fordt",
         ex="Mass production cut costs so far that a middle-class family could buy one."),
    dict(q="A buyer on margin has borrowed 90% of a share's price. What does a 10% fall do?",
         r=["It wipes the buyer out entirely", "It costs the buyer 1%", "It has no effect until the share is sold",
            "The broker pays the loss"], ok=0, voir="marg",
         ex="$100 share, $10 paid, $90 borrowed: at $90 the share only covers the debt. That is why a moderate fall became a stampede."),
    dict(q="Since when had farm prices been falling in the United States?",
         r=["Since 1920", "Since October 1929", "Since 1932", "Since 1914"], ok=0, voir="ferme",
         ex="The rural crisis is nine years older than the Crash: overproduction, a poor majority, Europe still recovering."),
    dict(q="What happened on Tuesday 29 October 1929?",
         r=["The market lost about 12% and 16 million shares changed hands", "Panic selling began for the first time",
            "The Dow Jones reached its peak of 381", "Roosevelt closed the banks"], ok=0, voir="trois",
         ex="Black Thursday was 24 October; Black Monday (28) cost about 13%, Black Tuesday (29) about 12%."),
    dict(q="How far did the Dow Jones fall between September 1929 and July 1932?",
         r=["From 381 to 41, about −89%", "From 381 to 250, about −35%", "From 100 to 41, about −60%", "From 300 to 200, about −33%"],
         ok=0, voir="chute",
         ex="And it did not regain its 1929 level until 1954."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H1 · big picture, objective, link and Part I.1) as written on the site; the site's animated map of chapter 1 and its bubble diagram (h1speculation).",
    "Outside the course (flagged in the video): RCA (as on the site), car registrations 1920–1929 (as on the site), The Great Gatsby, intermediate values of the Dow Jones curve, the 1930 rebound.",
    "Photograph: crowd outside the New York Stock Exchange, October 1929 (Wikimedia Commons, public domain).",
    "Photograph: Ford assembly line, Highland Park, 1913 (Wikimedia Commons, public domain).",
    "Photograph: 1925 Ford Model T touring, restored (ModelTMitch, Wikimedia Commons, CC BY-SA 4.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
