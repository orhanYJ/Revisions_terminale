"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 3 :
« Economic nationalism and political responses » (parties II.1 et II.2 du cours).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h1_3 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H1.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H1 : 13 Allemagne la plus exposée · 14 militarisme de trois régimes · 15 Smoot-Hawley · 16 blocs impériaux ·
       18 Mandchourie · 20 doctrine Stimson, Shanghai · 21 Hitler appelé, économie nazie · 22 New Deal ·
       23 Roosevelt renverse la politique · 24 Front populaire
Contenu : CHAPTERS.H1 du site (dnl/index.html), sections II.1 (4 idées) et II.2 (7 idées), schémas h1tariff (H1Tariff :
les six entrées de la fiche Smoot-Hawley) et h1germany (H1Germany : chômage allemand 1928-1933, Worksheet 3, et ses
trois questions), sujet d'essay « Assess how effective the 1930 Tariff Act was… » et key issue « economic nationalism »
(champ exam de H1). Ce qui n'est pas dans le cours est dit « outside the course ».
Précisions apportées au cours (dites dans la vidéo) : le pont du Golden Gate est un projet local, financé par
emprunt du district, pas un chantier fédéral du New Deal ; les derniers marines quittent le Nicaragua en janvier 1933,
avant l'entrée en fonctions de Roosevelt (sous Roosevelt : renonciation au droit d'intervention à Cuba, 1934, et départ
de Haïti, 1934) ; le Front populaire vote aussi un plan de réarmement en septembre 1936 (le cours dit « no money for
the army »).
Plan de la série H1 : 1 The Great Crash of 1929 · 2 From an American crash to a world crisis ·
3 Economic nationalism and political responses · 4 Democracies and the liberal order · 5 The crisis at the exam · 6 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-3"
NOTION = "The Wall Street Crash"
NUM = 3
TITRE = "Economic nationalism and political responses"
SUIVANT = "Episode 4 · Democracies and the liberal order"
PRONONCIATION = {"Smoot": "Smoot", "Hawley": "Haw-lee", "Lamont": "La-mont", "Kwantung": "Kwahn-toong",
                 "Maschmann": "Mash-mann", "Matignon": "Ma-tee-nyon", "Léon Blum": "Lay-on Bloom", "Blum": "Bloom",
                 "NSDAP": "N S D A P", "Autobahn": "Ow-to-bahn", "Weimar": "Vy-mar", "Mussolini": "Moosso-leeny",
                 "SNCF": "S N C F", "Huttérites": "Hutterites", "Manchukuo": "Man-choo-kwo", "Mukden": "Mook-den",
                 "RTAA": "R T double A"}

# Worksheet 3, source 2 (schéma h1germany) : chômage chez les travailleurs assurés, en %
CHOMAGE = [(1928, 8.6), (1929, 13.3), (1930, 22.7), (1931, 34.3), (1932, 43.8), (1933, 36.2)]
# vote nazi (idée 2 de II.2) : 1928, septembre 1930, juillet 1932, novembre 1932
VOTE = [(1928.4, 2.6), (1930.7, 18.3), (1932.55, 37.3), (1932.85, 33.1)]


def barres_ans(donnees, c="sa", c_pic="ca", pic=1932, ep=34, retrait=2.1):
    """Barres verticales (droites épaisses) sur un axe en années ; retrait = demi-épaisseur en unités de l'axe y."""
    el = []
    for an, v in donnees:
        el.append(dict(type="droite", pts=[[an, retrait], [an, max(retrait + .1, v - retrait)]], c=c_pic if an == pic else c,
                       ep=ep, dur=.8, lbl=f"{v}%", lp=[an, v + 4.5]))
    return el


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}Nineteen thirty. The crash of Wall Street has become a world depression. Every government faces the same question.",
        "{q1}When the world economy collapses, what do you do? Close your doors to protect your own people… "
        "or open them, and try to rebuild the world market together?",
        "{-q1}{q2}And why did the same crisis produce a New Deal in America, "
        "a Front populaire in France… and Hitler in Germany?",
        "{-q2}{-g0}{plan}This is episode three of our series on chapter one. {plan.1}Episode one was the Great Crash, "
        "{plan.2}episode two how an American crash became a world crisis. {plan.3}Today: economic nationalism, and the political "
        "answers to the crisis. {plan.4}Next time, the democracies and the liberal order. {plan.5}Then the exam, essay and DBQ, "
        "{plan.6}and a final recap.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[12]),
        "q1": dict(type="question", t="Close the doors… or open them?", bande=True),
        "q2": dict(type="question", t="One crisis: a New Deal, a Front populaire… and Hitler. Why?", bande=True),
        "plan": dict(type="liste", titre="H1 · The Wall Street Crash, in six episodes", items=[
            "The Great Crash of 1929 (I.1)", "From an American crash to a world crisis (I.2 – I.3)",
            "Economic nationalism and political responses (II.1 – II.2)", "Democracies and the liberal order (II.3)",
            "The crisis at the exam: essay and DBQ", "Recap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 3", t="Economic nationalism and political responses",
                      sous="1930 – 1936 · tariffs · closed blocs · Nazism · the New Deal · the Front populaire"),
    }),

    # ================================================================ la chronologie sur la carte (1)
    dict(id="carte1", chap="On the map · 1930 – 1932", fond="nuit", humeur="tension",
         retenir="1930–32: Germany the most exposed · militarism in Berlin, Rome, Tokyo · 17 June 1930 Smoot–Hawley · 1931–32 closed imperial blocs · 18 Sept. 1931 Manchuria.",
         beats=[
        "{g1}Let's follow the story on the map first. {g1.1}From 1930 to 1932, look at Germany. Its industry lived on American credit. "
        "When the loans are recalled, output falls by forty per cent, and unemployment explodes. "
        "In the same years, the Nazi vote climbs.",
        "{g1.2}Across the decade, three regimes choose the same road: Hitler's Germany, Mussolini's Italy and Japan. "
        "A strong army, the military in control, and an aggressive foreign policy. That is {!militarism}militarism.",
        "{g1.3}Now the United States. On the seventeenth of June 1930, President Hoover signs the Smoot–Hawley Tariff. "
        "Duties go up on more than twenty thousand imported goods. Canada, America's closest partner, retaliates within days.",
        "{g1.4}In 1931 and 1932, the great empires close up. Britain and its dominions trade among themselves, "
        "France sets quotas, Germany aims at autarky. World trade falls by about two thirds in value between 1929 and 1934.",
        "{g1.5}And in Asia, on the eighteenth of September 1931, the Japanese army invades Manchuria. "
        "The League of Nations condemns, and can do nothing more.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[13, 14, 15, 16, 18]),
    }),

    # ================================================================ la chronologie sur la carte (2)
    dict(id="carte2", chap="On the map · 1932 – 1936", fond="nuit", humeur="tension",
         retenir="Jan. 1932 Stimson note, Shanghai bombed · Jan. 1933 Hitler chancellor · 1933–35 the New Deal · 1933–34 off gold, RTAA, USSR recognised · 1934–36 6 February riots, then the Front populaire.",
         beats=[
        "{g2}{g2.1}January 1932. The American Secretary of State, Henry Stimson, announces that the United States will recognise "
        "no conquest by force in China. Japan answers by bombing Shanghai. And Washington does nothing.",
        "{g2.2}January 1933, Berlin. The conservatives appoint Adolf Hitler chancellor. His regime will end unemployment… "
        "by preparing for war.",
        "{g2.3}March 1933, Washington. Franklin Roosevelt takes office and launches the New Deal: relief, recovery, reform.",
        "{g2.4}In 1933 and 1934, Roosevelt reverses Hoover's policy. He takes the dollar off gold, and from 1934 he signs trade agreements "
        "country by country. He also recognises the Soviet Union.",
        "{g2.5}And France. On the sixth of February 1934, far-right leagues riot in Paris. Against the fear of fascism, the left unites: "
        "in 1936, the Front populaire wins the elections, under Léon Blum.",
        "{-g2}{dates}Here are the dates to copy. Pause the video if you need to.",
        ("P", 5.0),
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[20, 21, 22, 23, 24]),
        "dates": dict(type="liste", titre="The dates to know", petit=True, items=[
            "17 June 1930 · Smoot–Hawley; Canada retaliates", "1931 · French quotas · 18 Sept.: Manchuria",
            "1932 · Import Duties Act · Ottawa · Stimson note", "Jan. 1933 · Hitler chancellor",
            "1933 · the hundred days · off gold · USSR recognised (Nov.)", "1934 · 6 February riots · Reciprocal Tariff Act",
            "1935 · Second New Deal", "June 1936 · Front populaire, Matignon"], x=170, y=90, w=940),
    }),

    # ================================================================ II.1, idée 1 : l'internationalisme indépendant
    dict(id="hoover", chap="II.1 · Independent internationalism", fond="aube", humeur="calme",
         retenir="Hoover's “independent internationalism”: engaged in the world economy (exports, investment), absent from its political institutions (no alliance, no League). Not isolationism. After the Crash: domestic survival.",
         beats=[
        "{q3}Now the course, idea by idea. Part two, section one: {!economic nationalism}economic nationalism. "
        "And to understand it, we start before the Crash.",
        "{-q3}{def1}Under President Hoover, America practised what the course calls {!independent internationalism}independent internationalism. "
        "The label matters, because it is not isolationism.",
        "{-def1}{cmp1}{cmp1.g}On one side, America is fully engaged in the world economy: exports, foreign investment, "
        "economic and technological leadership. {cmp1.d}On the other, it is deliberately absent from its political institutions: "
        "no alliance, and outside the League of Nations.",
        "{-cmp1}{ex1}The example: you saw it in episode two. Under the Dawes Plan, American banks lend to Germany, "
        "and American firms invest across Europe. But Washington signs no alliance and joins no collective-security body. "
        "{ex1.1}So when the money goes home, in 1930, nothing political is left behind.",
        "{-ex1}{surv}After the Crash, the priority becomes {!domestic survival}domestic survival. The United States cuts off most of its "
        "international commitments, and keeps only a minimum of trade.",
    ], vis={
        "q3": dict(type="question", t="II.1 · Economic nationalism"),
        "def1": dict(type="def", cles=["engaged", "absent"], terme="Independent internationalism (Hoover, 1920s)",
                     t="Fully engaged in the world economy, deliberately absent from its political institutions.",
                     etape="Not isolationism: trade and investment, yes; alliances and the League, no.", x=170, y=200, w=940),
        "cmp1": dict(type="cols", g="Engaged", gq="exports · foreign investment · economic and technological leadership",
                     d="Absent", dq="no political or military alliance · outside the League of Nations", vs="+"),
        "ex1": dict(type="note", terme="Example · the Dawes loans", cles=["lend", "invest", "no alliance"],
                    t="American banks lend to Germany, American firms invest across Europe… but no alliance, no collective security.",
                    etape="1930: the money goes home, and nothing political is left behind.", x=170, y=200, w=940),
        "surv": dict(type="mot", t="Domestic survival", g="after the Crash: commitments cut off, a minimum of trade", y=260, taille=86),
    }),

    # ================================================================ II.1, idée 2 : Smoot-Hawley
    dict(id="smoot", chap="II.1 · The Smoot–Hawley Tariff", fond="nuit", humeur="tension",
         retenir="Smoot–Hawley, signed by Hoover on 17 June 1930: duties raised on 20,000+ goods, the 2nd-highest level in US history. Ideology: economic nationalism. Opposed by 1,028 economists, Henry Ford, Thomas Lamont, 23 countries.",
         beats=[
        "{mot1}Idea two: the United States answered the crisis with {!protectionism}protectionism. "
        "Its name: the Smoot–Hawley Tariff Act. The slides ask you to outline its features in six boxes. Here they are.",
        "{-mot1}{fiche}{fiche.1}What is it? A tariff law, signed by Hoover on the seventeenth of June 1930. It raises duties on more than "
        "twenty thousand imported goods, to the second-highest level in American history.",
        "{fiche.2}What ideology does it convey? Economic nationalism: recovery by shutting out foreign competition, rather than by cooperating.",
        "{fiche.3}Who promoted it? Senator Reed Smoot and Representative Willis Hawley, both Republicans. It began as a promise to farmers "
        "in the 1928 campaign, then grew through vote-trading in Congress: support my tariff, and I'll support yours. "
        "In the end, every industry was protected.",
        "{fiche.4}Who opposed it? A petition of one thousand and twenty-eight economists begged Hoover to veto it. "
        "Henry Ford called it an economic stupidity. And the banker Thomas Lamont said he almost went down on his knees to stop it. "
        "{fiche.5}Its aims: protect farms and industry, support jobs, raise customs revenue: a bet on the home market. "
        "{fiche.6}And its consequences: we come to them in a moment.",
        "{-fiche}{ex2}Hoover signed anyway, under pressure from his party and from business. "
        "{ex2.1}The example to quote: twenty-three countries had lodged formal protests before the bill was even law. "
        "{ex2.2}And two years later, in the 1932 election, both Smoot and Hawley lost their seats. "
        "The voters they had promised prosperity to had received the opposite.",
    ], vis={
        "mot1": dict(type="mot", t="20,000 goods", g="Smoot–Hawley Tariff Act · signed 17 June 1930", y=250, taille=100),
        "fiche": dict(type="liste", titre="Fact file · the Smoot–Hawley Tariff (June 1930)", petit=True,
                      cles=["20,000", "nationalism", "Republicans", "1,028", "home market", "consequences"], items=[
            "What? Duties on 20,000+ goods, the 2nd-highest level in US history",
            "Ideology: economic nationalism, shut out foreign competition",
            "Promoted by Smoot and Hawley (Republicans), from a 1928 promise to farmers",
            "Opposed by 1,028 economists, Henry Ford (“an economic stupidity”), Thomas Lamont",
            "Aims: protect farms and industry, jobs, customs revenue",
            "Consequences: see the next idea…"], x=130, y=100, w=1020),
        "ex2": dict(type="liste", titre="A law that failed before it began", cles=["protests", "lost"], items=[
            "23 countries protest before the vote", "1932: Smoot and Hawley both lose their seats"], x=170, y=170, w=940),
    }),

    # ================================================================ II.1, idée 3 : représailles et blocs
    dict(id="blocs", chap="II.1 · Retaliation and closed blocs", fond="nuit", humeur="tension",
         retenir="Retaliation: Canada (30% of US exports to it), French quotas (1931), British Import Duties Act (10%, 1932), Ottawa “imperial preference” (1932), German autarky. World trade −66% in value, 1929–1934. Free trade is gone.",
         beats=[
        "{q5}Idea three. Did it work? The slides answer their own question with a cartoon, and a caption:",
        ("C", "I'm not sure we nailed it, pal.", "c_pal"),
        "{-c_pal}{-q5}{chaine}Because protectionism spreads by {!retaliation}retaliation. {chaine.1}Canada, America's closest trading partner, "
        "retaliates within days, with new duties on products worth about thirty per cent of American exports to Canada. "
        "And it turns towards the British Empire instead. {chaine.2}France sets up an import quota system in 1931. "
        "{chaine.3}Britain passes the Import Duties Act in 1932: a general tariff of ten per cent on most imports. "
        "{chaine.4}Both exempt their own empires. And Germany builds a system of autarky.",
        "{-chaine}{def2}Here is the pattern to understand. The great trading powers did not simply close their doors. "
        "They redirected trade inwards, towards colonies that could not refuse them. "
        "{def2.1}So the world economy became {!a set of rival imperial blocs}a set of rival imperial blocs, rather than one market.",
        "{-def2}{gc}The result: {gc.1}World trade in 1929… {gc.2}and in 1934: down by about two thirds in value.",
        "{-gc}{ott}The example: the Ottawa Conference of 1932 formalised {!imperial preference}imperial preference. "
        "Britain and its dominions cut tariffs for each other, and kept them high for everyone else. "
        "{ott.1}Free trade, the pillar of the 1919 liberal order, was gone.",
        "{-ott}{jug}So, did the tariff cause the Depression? Many historians hold that the Act worsened it. "
        "The more careful judgement, the one to write, is this: {!a downturn into a trade war}it turned a downturn into a trade war.",
    ], vis={
        "q5": dict(type="question", t="Did it work?"),
        "c_pal": dict(type="cit", a="Caption of a cartoon", o="M. Ros's slides, on Smoot–Hawley", x=200, y=230, w=880),
        "chaine": dict(type="liste", titre="Protectionism spreads by retaliation", cles=["Canada", "quotas", "ten per cent", "autarky"], items=[
            "Canada retaliates within days: 30% of US exports to it", "France: import quotas (1931)",
            "Britain: Import Duties Act, 10% on most imports (1932)", "Empires exempted · Germany: autarky"], x=150, y=130, w=980),
        "def2": dict(type="def", cles=["inwards", "colonies"], terme="Closed imperial blocs",
                     t="Trade redirected inwards, towards colonies that could not refuse.",
                     etape="A set of rival imperial blocs, rather than one world market", x=170, y=200, w=940),
        "gc": dict(type="graphe", titre="World trade in value (1929 = 100, course figure: about −66%)", x=340, y=110, w=600, h=520,
                   ax=dict(x=[1927.5, 1935.5], y=[0, 120], gx=[], gy=[50, 100], lx="", ly="index"),
                   el=[dict(type="droite", pts=[[1929, 5], [1929, 95]], c="sa", ep=60, dur=1.0, lbl="1929: 100", lp=[1929, 108]),
                       dict(type="droite", pts=[[1934, 5], [1934, 29]], c="ca", ep=60, dur=1.0, lbl="1934: about 34", lp=[1934, 45])]),
        "ott": dict(type="note", terme="Example · Ottawa, 1932", cles=["each other", "everyone else"],
                    t="“Imperial preference”: low tariffs between Britain and its dominions, high tariffs for everyone else.",
                    etape="Free trade, the pillar of the 1919 liberal order, is gone.", x=170, y=200, w=940),
        "jug": dict(type="mot", t="A downturn → a trade war", g="the careful judgement on Smoot–Hawley", y=260, taille=80),
    }),

    # ================================================================ II.1, idée 4 : Roosevelt renverse la politique
    dict(id="fdr", chap="II.1 · Roosevelt reverses the policy", fond="aube", humeur="lumiere",
         retenir="Roosevelt: off gold in 1933, the Reciprocal Tariff Agreement Act (1934), about twenty agreements by 1939. None with Germany, Italy or Japan: the fascist leaders rejected trade agreements.",
         beats=[
        "{photo}Idea four. The fourth of March 1933: in the same car, on the way to the Capitol, the outgoing president, Herbert Hoover, "
        "and the new one, Franklin Roosevelt. Two men, two policies.",
        "{-photo}{rev}The slides pair Smoot–Hawley with a second box: off the gold standard. {rev.1}In 1933, Roosevelt takes the United States off gold. "
        "The dollar is free to fall, and prices to rise. {rev.2}In 1934, the {!Reciprocal Tariff Agreement Act}Reciprocal Tariff Agreement Act, "
        "the RTAA, allows him to negotiate tariff cuts, country by country. {rev.3}The aim: rebuild trade relations and liberalise global markets.",
        "{-rev}{lim}But the world had already changed. {lim.1}By 1939, the United States had signed reciprocal agreements with about twenty countries. "
        "{lim.2}None of them was Germany, Italy or Japan. Hitler and Mussolini rejected foreign trade agreements altogether: "
        "their economies were organised for autarky and war, not for exchange.",
    ], vis={
        "photo": dict(type="tableau", img="h1-hoover-fdr", de=[1.0, .5, .25], a=[1.15, .55, .2],
                      legende="Herbert Hoover and Franklin D. Roosevelt on the way to the inauguration, 4 March 1933 (Architect of the Capitol, public domain)"),
        "rev": dict(type="liste", titre="Roosevelt reverses the policy", cles=["gold", "RTAA", "liberalise"], items=[
            "1933: off the gold standard, the dollar falls, prices rise", "1934: the RTAA, tariff cuts country by country",
            "Aim: rebuild trade, liberalise global markets"], x=170, y=140, w=940),
        "lim": dict(type="cols", g="By 1939", gq="reciprocal agreements with about twenty countries", d="But",
                    dq="none with Germany, Italy or Japan: autarky and war, not exchange", vs="≠"),
    }),

    # ================================================================ à toi : l'essay sur le tarif
    dict(id="essai", chap="Your turn · an essay on the tariff", fond="aube", humeur="calme",
         retenir="Smoot–Hawley: ineffective on its own aims (farm prices, jobs, seats lost), damaging (trade war, −66%, blocs), but not the cause of the Depression. Its real importance: it destroyed the free-trade pillar of 1919.",
         beats=[
        "{ex3}Your turn. This is the course's own closing question on Smoot–Hawley: "
        "{!Assess how effective}assess how effective the 1930 Tariff Act was in responding to the challenges posed by the Great Depression.",
        "One tip: effective must be measured against the Act's own aims, protecting American farmers and industry. "
        "Find three arguments, then pause.",
        "{-ex3}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is a model plan. {rep1.1}First, it failed even on its own terms. Farm prices kept falling, unemployment kept rising, "
        "and Smoot and Hawley lost their seats in 1932. The failure was predicted, not discovered: one thousand and twenty-eight economists, "
        "twenty-three countries. {rep1.2}Second, it triggered a trade war: Canada within days, French quotas, the British Import Duties Act, "
        "German autarky, and world trade down by about two thirds. "
        "{rep1.3}Third, a nuance: it did not cause the Depression, which began with the Crash and the bank failures. "
        "And the reversal, the RTAA of 1934, came too late: Hitler and Mussolini rejected trade agreements.",
        "{rep1.4}The conclusion: ineffective on its aims, damaging in its consequences, but not the origin of the Depression. "
        "Its real importance is political: it destroyed the free-trade pillar of the 1919 liberal order.",
    ], vis={
        "ex3": dict(type="exo", niveau="essay", titre="Assess how effective the 1930 Tariff Act was in responding to the challenges posed by the Great Depression.",
                    src="M. Ros's slides, closing question on Smoot–Hawley", enonce=["Measure “effective” against the Act's own aims",
                                                                                     "Three arguments, then a judgement"]),
        "pa1": dict(type="pause", t="Find three arguments, each with a precise example, and a judgement.",
                    sous="Pause the video, write your plan, then play on for a model."),
        "rep1": dict(type="liste", titre="A model plan", cles=["own terms", "trade war", "did not cause", "political"], items=[
            "I. It failed on its own terms: farm prices, jobs, seats lost in 1932",
            "II. It triggered a trade war: Canada, quotas, Import Duties Act, −66%",
            "III. But it did not cause the Depression, and the RTAA (1934) came too late",
            "Judgement: ineffective, damaging, and political: the end of free trade"], x=130, y=120, w=1020),
    }),

    # ================================================================ II.2, idée 1 : l'Allemagne, la plus exposée
    dict(id="allemagne", chap="II.2 · Germany, the most exposed", fond="guerre", humeur="tension",
         retenir="Germany: industry dependent on American credit, output −40%, unemployment among insured workers 8.6% (1928) → 43.8% (1932). Reparations: no way out. Workers first, then the middle class.",
         beats=[
        "{q4}Section two: {!political responses}political responses to the crisis. And first, the country most exposed… and the one that broke.",
        "{-q4}{cause}{cause.1}German industry depended on American credit. So the recall of the loans hit it first, and hardest. "
        "{cause.2}Manufacturing production fell by forty per cent, and prices collapsed. "
        "{cause.3}And because Germany owed reparations to Europe and repayments to the United States, it could neither borrow nor spend its way out.",
        "{-cause}{gch}Here is the chart of Worksheet three, source two: unemployment among insured workers. "
        "{gch.1}Eight point six per cent in 1928. {gch.2}Thirteen point three in 1929. {gch.3}Twenty-two point seven in 1930. "
        "{gch.4}Thirty-four point three in 1931. {gch.5}And forty-three point eight per cent in 1932: the peak. "
        "{gch.6}It falls back to thirty-six point two in 1933.",
        "{gch.7}Be careful when you quote it: these figures concern insured workers. Across the whole workforce, the rate was lower, "
        "about thirty per cent at the peak. Cite the source when you use the figure.",
        "{-gch}{arb}{soc}Who is hit? {soc.1}The proletariat first: workers who lose their jobs, their income, their food and their homes. "
        "{soc.2}Then part of the middle class. {soc.3}Hunger marches, soup kitchens, street protests become ordinary sights, "
        "like the soup kitchens of Hanover in 1932. {soc.4}And the loss of hope feeds protest. As the course puts it: the protest found a party.",
        "{-soc}{-arb}{masch}Melita Maschmann, a teenager at the time, remembered adults talking of six million unemployed… "
        "and blaming the reparations, not the world crisis.",
    ], vis={
        "q4": dict(type="question", t="II.2 · Political responses to the crisis"),
        "cause": dict(type="liste", titre="Why Germany broke", cles=["credit", "forty", "reparations"], items=[
            "Industry dependent on American credit: the loans recalled", "Manufacturing −40%, prices collapse",
            "Reparations and repayments: no way to borrow or spend"], x=170, y=140, w=940),
        "gch": dict(type="graphe", titre="German unemployment among insured workers, % (Worksheet 3, Source 2)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1927.4, 1933.6], y=[0, 52], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="", ly="%"),
                    el=barres_ans(CHOMAGE) + [dict(type="texte", x=1930.5, y=49.5, t="insured workers only: about 30% across the whole workforce", c="iv")]),
        "arb": dict(type="tableau", img="h1-arbeitsamt-1932", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .6, .55],
                    legende="Unemployed outside the employment office Berlin-Nordost, 4 May 1932 (Bundesarchiv, Bild 146-1976-033-23, Seiler, CC BY-SA 3.0 de)"),
        "soc": dict(type="liste", titre="Who is hit?", cles=["proletariat", "middle class", "soup kitchens", "party"], items=[
            "Workers first: jobs, income, food, homes", "Then part of the middle class",
            "Hunger marches, soup kitchens (Hanover, 1932)", "Loss of hope → protest → a party"], x=170, y=130, w=940),
        "masch": dict(type="note", terme="Example · Melita Maschmann (Worksheet 3)", cles=["six million", "reparations"],
                      t="Adults talked of “six million unemployed”… and blamed the reparations, not the world crisis.",
                      etape="A former Hitler Youth member, memoir of 1963", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 2 : jamais majoritaires
    dict(id="nazis", chap="II.2 · Never a majority, but let in", fond="guerre", humeur="tension",
         retenir="The Nazi vote followed unemployment: 2.6% (1928), 18.3% (1930), 37.3% (July 1932), 33.1% (Nov. 1932). Never a majority: Hitler appointed in January 1933 by conservatives, out of fear of communism. The crisis created the audience; a calculation opened the door.",
         beats=[
        "{nsdap}Idea two. The NSDAP, the Nazi party, used the discontent. {nsdap.1}It blamed the weakness of the young Weimar Republic. "
        "{nsdap.2}It offered simple solutions to complex problems. {nsdap.3}And it spoke directly to the unemployed, even to the communist worker: "
        "a slogan of 1933 promised work, freedom, bread.",
        "{-nsdap}Melita Maschmann again, in her memoir:",
        ("C", "The Nazis promised to end unemployment and poverty, and I believed them.", "c_masch"),
        "{-c_masch}{gv}Now watch two curves on the same chart. {gv.1}Unemployment. {gv.2}And the Nazi vote: two point six per cent in 1928, "
        "eighteen point three in 1930, thirty-seven point three in July 1932. The vote follows the curve almost exactly. "
        "{gv.3}Then, in November 1932, it falls: thirty-three point one per cent.",
        "{-gv}{maj}So remember this: the Nazis {!never won a majority}never won a majority. Never more than fifty per cent of the vote.",
        "{-maj}{porte}What brought them to power? {porte.1}The fear of communism, among the middle class and the centre parties. "
        "They preferred to work with the Nazis rather than risk a revolution from the left. "
        "{porte.2}And in January 1933, Hitler was appointed chancellor by conservatives who thought they could use him.",
        "{-porte}{dist}This is a very useful distinction for an essay. {dist.g}The crisis created the audience. "
        "{dist.d}But a political calculation opened the door.",
    ], vis={
        "nsdap": dict(type="liste", titre="How the NSDAP used the crisis", cles=["Weimar", "simple", "unemployed"], items=[
            "It blamed the weakness of the Weimar Republic", "Simple solutions to complex problems",
            "It spoke to the unemployed, even communists: “Work! Freedom! Bread!” (1933)"], x=170, y=140, w=940),
        "c_masch": dict(type="cit", a="Melita Maschmann", o="memoir, 1963 (Worksheet 3, Source 5)", x=200, y=230, w=880),
        "gv": dict(type="graphe", titre="Unemployment (insured workers) and the Nazi vote, % (course)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="", ly="%"),
                   el=[dict(type="courbe", pts=[list(p) for p in CHOMAGE], c="sa", lbl="unemployment", lp=[1929.0, 22], dur=1.8),
                       dict(type="courbe", pts=[list(p) for p in VOTE[:3]], c="ca", lbl="Nazi vote", lp=[1931.0, 14], dur=1.8),
                       dict(type="courbe", pts=[list(p) for p in VOTE[2:]], c="ca", lbl="Nov. 1932: 33.1%", lp=[1932.0, 27], dur=.8)]),
        "maj": dict(type="mot", t="Never a majority", g="the Nazi vote never passed 50%", y=260, taille=96),
        "porte": dict(type="liste", titre="Let in, not elected", cles=["fear of communism", "conservatives"], items=[
            "The fear of communism: middle class and centre parties side with the Nazis",
            "January 1933: Hitler appointed by conservatives who thought they could use him"], x=170, y=160, w=940),
        "dist": dict(type="cols", g="The crisis", gq="created the audience", d="A political calculation", dq="opened the door", vs="→"),
    }),

    # ================================================================ II.2, idée 3 : la politique économique nazie
    dict(id="econazie", chap="II.2 · The Nazi economy", fond="guerre", humeur="tension",
         retenir="Nazi economy. Goals: stability, full employment, autarky. Means: unions banned, wages frozen, longer hours · tariffs · public works (the Autobahn) · rearmament despite Versailles · privatisations · plunder and the dispossession of Jews. Unemployment: 6 million (1933) → under 1 million (1937).",
         beats=[
        "{buts}Idea three: Nazi economic policy. {buts.1}Three goals: economic stability, {buts.2}an end to unemployment, {buts.3}and autarky.",
        "{-buts}{moy}And the means, in the order of the course. {moy.1}Coercion: trade unions banned, wages frozen, working hours lengthened. "
        "{moy.2}Tariffs on imports. {moy.3}Public investment, continuing Weimar's policy: schools, hospitals, roads, and the Autobahn, the motorways. "
        "{moy.4}Rearmament, even though the Treaty of Versailles prohibited it. "
        "{moy.5}Mass privatisation: banks like the Deutsche Bank, railways, shipyards. "
        "{moy.6}And the last two items are not economics, but crime: the plundering of conquered nations, and the dispossession of Jewish property.",
        "{-moy}{six}The example: rearmament absorbed the unemployed and pleased industry. Registered unemployment fell from six million in 1933 "
        "to under one million by 1937.",
        "{-six}{lec}So read the list together. {!a regime that solved unemployment by preparing for war}A regime that solved unemployment "
        "by preparing for war, and paid for it with theft. {lec.1}A recovery that only made sense if war followed.",
    ], vis={
        "buts": dict(type="liste", titre="Three goals", cles=["stability", "unemployment", "autarky"], items=[
            "Economic stability", "An end to unemployment", "Autarky"], x=170, y=160, w=940),
        "moy": dict(type="liste", titre="The means (course order)", petit=True, cles=["banned", "Tariffs", "Autobahn", "Rearmament", "privatisation", "crime"], items=[
            "Unions banned · wages frozen · longer hours", "Tariffs on imports",
            "Public works, as under Weimar: schools, hospitals, the Autobahn", "Rearmament, despite Versailles",
            "Privatisations: Deutsche Bank, railways, shipyards", "Crime: plunder of conquered nations, Jewish property seized"], x=130, y=100, w=1020),
        "six": dict(type="mot", t="6 million → under 1 million", g="registered unemployment in Germany, 1933 → 1937", y=250, taille=80),
        "lec": dict(type="note", terme="Read the list together", cles=["war", "theft"],
                    t="A regime that solved unemployment by preparing for war, and paid for it with theft.",
                    etape="A recovery that only made sense if war followed.", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 4 : le militarisme
    dict(id="militarisme", chap="II.2 · Militarism in three regimes", fond="nuit", humeur="tension",
         retenir="Key notion. Militarism: a strong military, ready to be used aggressively. Three dimensions: armed build-up (budget), military control of government (constitution), aggressive foreign policy (war). Germany, Italy, Japan.",
         beats=[
        "{def3}Idea four: {!militarism}militarism, which spreads to three regimes at once: Hitler's, Mussolini's and the Japanese government. "
        "The definition: the belief that a government should maintain a strong military force, and be prepared to use it aggressively "
        "to defend or promote national interests.",
        "{-def3}{dims}It has three dimensions, and an essay should name all three. {dims.1}The building up of armed forces: a budget choice. "
        "{dims.2}Control of the government by the military: a constitutional choice. "
        "{dims.3}And an aggressive foreign policy: the one that ends in war.",
        "{-dims}{g3}{g3.1}Japan illustrates the second dimension most clearly. In September 1931, the Kwantung Army acted in Manchuria first, "
        "and left the civilian government in Tokyo to explain afterwards. The army decided; the government followed.",
        "{-g3}{ki}And the course's key issue sits on this slide: economic factors… and, or, ideology? We answer it at the end of this episode.",
    ], vis={
        "def3": dict(type="def", cles=["strong military", "aggressively"], terme="Militarism",
                     t="A government should maintain a strong military force and be prepared to use it aggressively.",
                     etape="Germany · Italy · Japan, in the 1930s", x=170, y=200, w=940),
        "dims": dict(type="liste", titre="The three dimensions of militarism", cles=["budget", "constitutional", "war"], items=[
            "Building up armed forces → a budget choice", "The military controls the government → a constitutional choice",
            "An aggressive foreign policy → the one that ends in war"], x=150, y=140, w=980),
        "g3": dict(type="globe", code="H1", sc=[18]),
        "ki": dict(type="question", t="Economic factors and / or ideology?"),
    }),

    # ================================================================ II.2, idée 5 : le New Deal
    dict(id="newdeal", chap="II.2 · The New Deal", fond="aube", humeur="lumiere",
         retenir="Roosevelt, Democrat, elected 1932: the New Deal, Relief, Recovery, Reform. First New Deal (1933–35): the hundred days, CCC, TVA, deposits insured. Second New Deal (1935): Social Security Act, WPA. Public money for bridges and rights, not an army.",
         beats=[
        "{rrr}Idea five. The United States chose the opposite road. Hoover's protectionist policy had proved ineffective. "
        "Roosevelt, a Democrat elected in 1932, promoted a {!New Deal}New Deal and a welfare state: expansionary economics, in three words. "
        "{rrr.1}Relief, for the destitute. {rrr.2}Recovery, for the economy. {rrr.3}Reform, of the system that had failed.",
        "{-rrr}It came in two stages. The First New Deal, from 1933 to 1935, opens with the emergency laws of the first hundred days. "
        "Their aim, in Roosevelt's words, quoted by the course:",
        ("C", "helping the millions who never had a chance: men at starvation wages, women in sweatshops, children at looms", "c_fdr"),
        "{-c_fdr}{fr1}{fr1.1}Roosevelt, elected in 1932. {fr1.2}The hundred days created the Civilian Conservation Corps and the Tennessee Valley Authority, and insured bank deposits. "
        "{fr1.3}Then the Second New Deal, in 1935, turned relief into rights: the Social Security Act, with pensions and unemployment insurance, "
        "and the Works Progress Administration.",
        "{fr1.4}The course also mentions the Golden Gate Bridge, in San Francisco, which went up from 1933 under the same impulse. "
        "One precision, outside the course: it was a local project, paid for by bonds of a regional district, not a federal New Deal programme.",
        "{-fr1}{cmp2}And now the point of the comparison. {cmp2.g}Both states spent public money against unemployment. "
        "{cmp2.d}But one built bridges and social insurance… while the other built an army.",
    ], vis={
        "rrr": dict(type="liste", titre="The New Deal: three words", cles=["Relief", "Recovery", "Reform"], items=[
            "Relief · for the destitute", "Recovery · for the economy", "Reform · of the system that failed"], x=170, y=160, w=940),
        "fr1": dict(type="frise", items=[
            dict(nom="Elected", d=1932, q="Roosevelt, a Democrat"), dict(nom="Hundred days", d=1933, q="CCC · TVA · deposits insured"),
            dict(nom="Second New Deal", d=1935, q="Social Security Act · WPA"), dict(nom="Golden Gate", d=1937, q="built from 1933 (local project)")]),
        "c_fdr": dict(type="cit", a="Franklin D. Roosevelt", o="quoted in M. Ros's course", x=200, y=200, w=880),
        "cmp2": dict(type="cols", g="USA · the New Deal", gq="public money for bridges, dams and social insurance",
                     d="Germany · Nazism", dq="public money for motorways and, above all, an army", vs="≠"),
    }),

    # ================================================================ II.2, idée 6 : la diplomatie du New Deal
    dict(id="diplo", chap="II.2 · New Deal diplomacy", fond="aube", humeur="calme",
         retenir="New Deal diplomacy: the RTAA (1934) to liberalise trade; the USSR recognised (Nov. 1933); the “Good Neighbor” policy in Latin America. Trade and new partners, but no alliance.",
         beats=[
        "{dip}Idea six. The New Deal also had a foreign policy, and it ran against economic nationalism. "
        "{dip.1}The Reciprocal Tariff Agreement Act of 1934, which you already know: trade deals, country by country. Its limit: the fascist leaders refused them.",
        "{dip.2}In November 1933, Roosevelt recognised the Soviet Union, sixteen years after the revolution. His calculation: "
        "the USSR might help against Japan, and trade with it might help the American economy.",
        "{dip.3}And the {!Good Neighbor}Good Neighbor policy ended the American interventions of the previous decades in Latin America. "
        "The course says it withdrew American forces from Cuba and Nicaragua. A precision: the last Marines left Nicaragua in January 1933, "
        "just before Roosevelt took office. Under Roosevelt, in 1934, the United States gave up its right to intervene in Cuba, "
        "and withdrew its Marines from Haiti.",
        "{-dip}{bil2}So the picture is this: a president trying to reopen the world economically, {!while his Congress was closing it politically}"
        "while his Congress was closing it politically. Trade and new partners… {bil2.1}but no alliance. That is episode four.",
    ], vis={
        "dip": dict(type="liste", titre="New Deal diplomacy", cles=["1934", "Soviet Union", "Good Neighbor"], items=[
            "1934 · the RTAA: liberalise trade, deal by deal", "Nov. 1933 · the USSR recognised: against Japan, for trade",
            "The “Good Neighbor” policy: interventions ended (Nicaragua Jan. 1933; Cuba and Haiti 1934)"], x=150, y=140, w=980),
        "bil2": dict(type="note", terme="The paradox", cles=["reopen", "closing"],
                     t="A president reopening the world economically, a Congress closing it politically.",
                     etape="Trade and new partners, but no alliance.", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 7 : le Front populaire
    dict(id="frontpop", chap="II.2 · The Front populaire", fond="nuit", humeur="lumiere",
         retenir="France: 6 Feb. 1934 riots → Socialists, Communists, Radicals unite → Front populaire wins in 1936 (Léon Blum): 40-hour week, two weeks' paid holiday, the SNCF, Matignon (+7 to 15%). Keynesian deficits; appeasement and non-intervention in Spain. Gains eaten by the franc's fall.",
         beats=[
        "{g4}Idea seven: France answered late, and from the left. {g4.1}On the sixth of February 1934, the far-right leagues riot in Paris, "
        "in what the course calls a failed coup. The fear of fascism brings Socialists, Communists and Radicals together: "
        "the {!Front populaire}Front populaire, which wins the 1936 elections under Léon Blum.",
        "{-g4}{blum}{fp}What does it do? {fp.1}The forty-hour week. {fp.2}Two weeks' paid holiday. "
        "{fp.3}The nationalisation of the railway companies into the SNCF. "
        "{fp.4}And its economics are {!Keynesian}Keynesian: spending and deficits to revive demand. "
        "The exact opposite of Germany's path: austerity, then rearmament.",
        "{-fp}{-blum}{intl}{intl.g}Abroad, it chooses appeasement, and non-intervention in the Spanish Civil War. "
        "{intl.d}The course adds: no money for the army. A precision: in September 1936, Blum's government did vote a large rearmament plan. "
        "But deficits and a falling franc limited what it could do.",
        "{-intl}{mat}The example. {mat.1}The Matignon Agreements, in June 1936, raised wages by seven to fifteen per cent in a week. "
        "{mat.2}But France left the gold standard only that autumn, and the franc's fall ate the gains. "
        "{mat.3}By 1938, the forty-hour week was being dismantled.",
        "{-mat}{trois}So, one crisis, three answers. {trois.1}Germany: coercion, rearmament, autarky, and war. "
        "{trois.2}The United States: the New Deal, relief, recovery, reform. "
        "{trois.3}France: social reform at home, appeasement abroad.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[24]),
        "blum": dict(type="tableau", img="h1-blum-1936", fond=True, sombre=True, de=[1.0, .7, .4], a=[1.15, .72, .35],
                     legende="Léon Blum at the microphone, 1936 (Agence Meurisse, public domain)"),
        "fp": dict(type="liste", titre="The Front populaire (Léon Blum, 1936)", cles=["forty-hour", "paid holiday", "SNCF", "Keynesian"], items=[
            "The 40-hour week", "Two weeks' paid holiday", "Railways nationalised: the SNCF",
            "Keynesian: spending and deficits to revive demand"], x=170, y=130, w=940),
        "intl": dict(type="cols", g="Abroad", gq="appeasement · non-intervention in Spain", d="The army",
                     dq="course: “no money for the army” · in fact a rearmament plan, Sept. 1936, limited by deficits", vs="·"),
        "mat": dict(type="liste", titre="Example · the Matignon Agreements", cles=["seven to fifteen", "franc", "dismantled"], items=[
            "June 1936: wages +7 to 15% in a week", "Autumn 1936: off gold, the franc's fall eats the gains",
            "1938: the 40-hour week dismantled"], x=170, y=150, w=940),
        "trois": dict(type="liste", titre="One crisis, three answers", cles=["Germany", "United States", "France"], items=[
            "Germany: coercion, rearmament, autarky… war", "United States: the New Deal, Relief, Recovery, Reform",
            "France: social reform at home, appeasement abroad"], x=150, y=150, w=980),
    }),

    # ================================================================ à toi : le key issue
    dict(id="keyissue", chap="Your turn · the key issue", fond="aube", humeur="calme",
         retenir="Economic nationalism: a serious contributing factor but not the key one. It explains why the world could not cooperate, not why three regimes chose war. Economic factors created the opportunity; ideology supplied the intent.",
         beats=[
        "{ex4}Now the key issue of the chapter, the one you may draw at the oral. "
        "{!How far do you agree}How far do you agree that economic nationalism was the key factor in the slide towards war in 1939?",
        "Define economic nationalism: national economic interest above international cooperation, "
        "through tariffs, quotas and currency choices. Then test the word key.",
        "{-ex4}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}A model plan. {rep2.1}Part one: yes, economic nationalism corroded the international order. "
        "Smoot–Hawley, French quotas, the Import Duties Act: world trade down by two thirds, a world of imperial blocs. "
        "And it made autarky and conquest look rational to a state without an empire, which is exactly what Nazi policy claimed.",
        "{rep2.2}Part two: but it is a symptom as much as a cause. Protectionism answered the Depression, which answered the Crash: "
        "the chain starts on Wall Street, not in customs houses. And Britain and France practised economic nationalism too, "
        "without choosing war.",
        "{rep2.3}Part three: ideology competes for the same place. Militarism, with its three dimensions, in Berlin, Rome and Tokyo. "
        "And the plunder of conquered nations and the dispossession of Jewish property: crimes no trade barrier explains.",
        "{rep2.4}Judgement: a serious contributing factor, but not the key one. It explains why the world could not cooperate, "
        "not why three regimes chose war. {!economic factors created the opportunity}Economic factors created the opportunity; "
        "ideology supplied the intent.",
    ], vis={
        "ex4": dict(type="exo", niveau="essay", titre="How far do you agree that economic nationalism was the key factor in the slide towards war in 1939?",
                    src="Key issue of the chapter (oral)", enonce=["Define economic nationalism", "Test the word “key”",
                                                                   "Three parts and a judgement"]),
        "pa2": dict(type="pause", t="Plan three parts, with evidence, and a judgement: how far?",
                    sous="Pause the video, write your plan, then play on for a model."),
        "rep2": dict(type="liste", titre="A model plan", cles=["corroded", "symptom", "ideology", "opportunity"], items=[
            "I. It corroded the order: tariffs, quotas, blocs, −66%, autarky looks rational",
            "II. A symptom as much as a cause: the chain starts on Wall Street",
            "III. Ideology competes: militarism in three regimes, plunder, dispossession",
            "Judgement: economic factors created the opportunity; ideology supplied the intent"], x=130, y=120, w=1020),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Economic nationalism: from Hoover's independent internationalism to Smoot–Hawley, "
        "retaliation, closed imperial blocs and world trade down by two thirds; Roosevelt reverses the policy, too late. "
        "{carte.2}Germany, the most exposed: the Nazis never a majority, but let in, and an economy built for war. "
        "{carte.3}Militarism in three regimes, with its three dimensions. "
        "{carte.4}And the democracies' answers: the New Deal and its diplomacy, and the Front populaire.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the democracies and the liberal order. The League of Nations, Manchuria, the Neutrality Acts… "
        "and the road to Munich.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="ECONOMIC NATIONALISM AND POLITICAL RESPONSES", branches=[
            dict(t="II.1 · Nationalism", items=["Smoot–Hawley, 17 June 1930", "blocs · Ottawa 1932 · −66%", "FDR: off gold, RTAA 1934"]),
            dict(t="Germany", items=["43.8% unemployed (1932)", "never a majority · Jan. 1933", "rearmament · plunder"]),
            dict(t="Militarism", items=["build-up · military rule", "aggressive foreign policy", "Germany · Italy · Japan"]),
            dict(t="Democracies", items=["New Deal: 3 R's · 1933–35", "USSR recognised · Good Neighbor", "Front populaire 1936"])]),
        "fin": dict(type="mot", t="Next: democracies and the liberal order", g="Episode 4 · the League, neutrality, appeasement", y=270, taille=70),
    }),
]

QUIZ = [
    dict(q="What does the course mean by Hoover's “independent internationalism”?",
         r=["Engaged in the world economy, absent from its political institutions", "Total isolation from world trade",
            "Membership of the League without alliances", "Military alliances without trade"], ok=0, voir="def1",
         ex="Exports and investment, yes; alliances and the League, no. It is not isolationism."),
    dict(q="What did the Smoot–Hawley Tariff (17 June 1930) do?",
         r=["It raised duties on more than 20,000 imported goods", "It took the dollar off gold",
            "It cut tariffs country by country", "It insured bank deposits"], ok=0, voir="fiche",
         ex="The second-highest tariff level in American history, despite 1,028 economists and 23 protesting countries."),
    dict(q="What did the Ottawa Conference of 1932 formalise?",
         r=["Imperial preference between Britain and its dominions", "The end of reparations",
            "A world free-trade agreement", "French import quotas"], ok=0, voir="ott",
         ex="Low tariffs inside the Empire, high ones for everyone else: free trade, the pillar of 1919, was gone."),
    dict(q="By how much did world trade fall in value between 1929 and 1934, according to the course?",
         r=["About two thirds", "About 10%", "About a quarter", "It doubled"], ok=0, voir="gc",
         ex="About −66%: the world economy became a set of rival imperial blocs."),
    dict(q="What did the Reciprocal Tariff Agreement Act of 1934 allow?",
         r=["Tariff cuts negotiated country by country", "A general tariff of 10%",
            "The recognition of the USSR", "The withdrawal from the gold standard"], ok=0, voir="rev",
         ex="About twenty agreements by 1939, none with Germany, Italy or Japan."),
    dict(q="What was German unemployment among insured workers in 1932 (Worksheet 3)?",
         r=["43.8%", "8.6%", "25%", "13.3%"], ok=0, voir="gch",
         ex="8.6% in 1928, 43.8% in 1932: across the whole workforce, the rate was lower, about 30%."),
    dict(q="How did Hitler come to power?",
         r=["Appointed chancellor by conservatives in January 1933, without a majority", "Elected with 52% of the vote in 1932",
            "By a coup in November 1932", "Appointed by the League of Nations"], ok=0, voir="porte",
         ex="The Nazi vote peaked at 37.3% (July 1932); fear of communism opened the door."),
    dict(q="Which are the three words of the New Deal?",
         r=["Relief, Recovery, Reform", "Work, Freedom, Bread", "Stability, Employment, Autarky", "Cash and carry"], ok=0, voir="rrr",
         ex="Relief for the destitute, recovery for the economy, reform of the system that had failed."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H1 · Parts II.1 and II.2: the Smoot–Hawley fact file, Worksheet 3) as written on the site; animated map of chapter 1 (site).",
    "Photograph: Herbert Hoover and Franklin D. Roosevelt on the way to the inauguration, 4 March 1933 (Architect of the Capitol, public domain, Wikimedia Commons).",
    "Photograph: unemployed outside the employment office Berlin-Nordost, 4 May 1932 (Bundesarchiv, Bild 146-1976-033-23, photographer Seiler, CC BY-SA 3.0 de, Wikimedia Commons).",
    "Photograph: Léon Blum at the microphone, 1936 (Agence de presse Meurisse, public domain, Wikimedia Commons).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
