"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 5 : « Mass terror » (partie II.3 du chapitre).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_5 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 14 « une terreur moins oppressive ? » (Italie, confino, Lipari) · 15 les koulaks · 17 le Goulag, canal de la
       mer Blanche · 19 l'Holodomor · 21 l'incendie du Reichstag · 22 polices politiques et camps (Dachau) ·
       23 la lutte des races (T4) · 30 procès de Moscou et Grande Purge · 38 la terreur dévore les siens (Iejov, Trotski)
Contenu : CHAPTERS.H2 du site (dnl/index.html), section II.3 (8 idées), schéma h2terror (Worksheet 4 : les six
similitudes et les différences), schéma h2table (le tableau des totalitarismes, parcouru en entier comme synthèse des
parties I et II ; les deux blocs de la partie III restent à remplir), idée 5 de l'introduction (Arendt : la confiance
des masses), sujet d'essay « To what extent did the three totalitarian regimes control their societies in the same way? »
(données exam) pour la conclusion de la Worksheet 4.
Corrections et précisions dites dans la vidéo :
  - le cours écrit « Italy had no concentration camps » : vrai pour la répression des opposants en Italie avant la
    guerre (le confino), mais l'Italie fasciste a ouvert des camps de concentration en Libye (Cyrénaïque, 1930-1933),
    puis des camps d'internement pendant la guerre — dit « outside the course » ;
  - le cours dit que Beria « held the post until 1953 » : il dirige le NKVD de 1938 à 1945, puis supervise la police
    jusqu'en 1953 — formulé « in charge of the Soviet police apparatus until 1953 », précision hors cours dite ;
  - procès de Moscou 1936-38 et Grande Purge 1937-38 : deux dates distinctes, rappelées.
Le « Your turn » 1 est la Worksheet 4 (similitudes) ; le « Your turn » 2 un essay « How far » (plan et introduction)
sur « Terror was the main tool of totalitarian regimes », avec un modèle.
Ton : sobre et factuel ; aucune image de victimes ; humeurs « calme », « mystere », « tension ».
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-5"
NOTION = "Totalitarian Regimes"
NUM = 5
TITRE = "Mass terror"
SUIVANT = "Episode 6 · Hegemonic ambitions"
PRONONCIATION = {"Il Duce ha sempre ragione": "Eel Doo-chay ah sem-preh ra-jo-neh", "Biennio Rosso": "Bee-en-nyo Ross-o",
                 "Gulag": "Goo-lag", "Holodomor": "Kho-lo-do-mor", "kulaks": "koo-laks", "kulak": "koo-lak",
                 "Yezhov": "Yeh-zhoff", "Kirov": "Kee-roff", "Zinoviev": "Zee-noh-vyeff", "Kamenev": "Kah-meh-nyeff",
                 "Rykov": "Ree-koff", "Beria": "Bair-ee-ya", "OVRA": "Oh-vrah", "OGPU": "O G P U", "NKVD": "N K V D",
                 "Matteotti": "Mat-teh-ot-tee", "Himmler": "Him-ler", "Dachau": "Dakh-ow", "Reichstag": "Rikes-tahg",
                 "Reichsmarks": "Rikes-marks", "Hergé": "Air-zhay", "confino": "con-fee-no", "Lipari": "Lee-pa-ree",
                 "Arendt": "Ah-rent", "Duce": "Doo-chay", "Führer": "Fyoo-rer", "Balilla": "Ba-lee-la",
                 "Komsomol": "Kom-so-mol", "squadristi": "skwa-dree-stee", "Hindenburg": "Hin-den-burg",
                 "Lebensraum": "Lay-bens-rowm", "Cyrenaica": "Sigh-reh-nay-ika"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Moscow, 1936. On trial, old companions of Lenin confess to crimes they never committed. "
        "Within two years, the Great Purge has carried out six hundred and eighty thousand executions.",
        "{q1}Why would a regime terrorise its own people? And why would it end by striking its own men?",
        "{-q1}{-g0}{plan}Today, Part two point three of the chapter: mass terror. {plan.1}First, the events on the map. "
        "{plan.2}Then the course, idea by idea: the police, the trials, the camps, the purges. "
        "{plan.3}Then Worksheet four: what the three terrors have in common, and what they do not. "
        "{plan.4}Then the whole totalitarianism table, as a synthesis of Parts one and two. "
        "{plan.5}And an essay: was terror the main tool of these regimes?",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[30]),
        "q1": dict(type="question", t="Why terrorise your own people?", bande=True),
        "plan": dict(type="liste", titre="Episode 5 · the plan", items=[
            "Terror on the map, 1929 – 1940", "II.3 · Mass terror: eight ideas",
            "Worksheet 4 · similarities in the use of violence", "The totalitarianism table: Parts I and II",
            "Your turn: was terror the main tool?"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 5", t="Mass terror",
                      sous="Police · trials · camps · purges · Part II.3 of the course"),
    }),

    # ================================================================ la carte : 1929-1933
    dict(id="carte1", chap="On the map: 1929 – 1933", fond="nuit", humeur="mystere",
         retenir="Italy: opponents sent to islands (the confino) · USSR 1929–32: the kulaks deported · 1931–33: the White Sea Canal, dug by Gulag prisoners · 1932–33: the Holodomor in Ukraine.",
         beats=[
        "{g1}Let's start on the map, in chronological order. {g1.1}Italy, from 1929. Mussolini has to come to terms with the Church "
        "and the king. His opponents are usually not executed: they are sent into internal exile, on islands such as Lipari. "
        "Monsieur Ros asks the question with a question mark: a less oppressive terror?",
        "{g1.2}The Soviet Union, 1929 to 1932. Forced collectivisation, seen in episode three. Any peasant who resists is called a kulak, "
        "a class enemy: land and animals confiscated, and many deported.",
        "{g1.3}1931 to 1933, in the far north. Prisoners of the Gulag dig the White Sea to Baltic Canal: two hundred and twenty-seven kilometres, "
        "largely with hand tools. The camp has become a building site.",
        "{g1.4}And 1932 to 1933, in Ukraine: the Holodomor. Grain is requisitioned whatever the harvest, rebellious villages are cut off "
        "from all supplies, and the famine kills millions. A famine made by a political decision.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[14, 15, 17, 19]),
    }),

    # ================================================================ la carte : 1933-1940
    dict(id="carte2", chap="On the map: 1933 – 1940", fond="nuit", humeur="tension",
         retenir="27 Feb. 1933: the Reichstag fire · 1933: Gestapo, Dachau · 1933–39: sterilisation, Nuremberg laws, T4 · 1936–38: Moscow trials, Great Purge · 1940: Yezhov executed, Trotsky murdered in Mexico.",
         beats=[
        "{g2}{g2.1}Germany, the twenty-seventh of February 1933. The Reichstag burns. The Nazis blame the communists, "
        "freedoms are suspended, and thousands of communists are arrested.",
        "{g2.2}The same year, the political police is placed above the law, and the first camp opens at Dachau, near Munich. "
        "In Italy the OVRA exists since 1927; in the Soviet Union, the NKVD from 1934.",
        "{g2.3}From 1933, Nazi violence also strikes Germans in the name of biology: forced sterilisation, "
        "the Nuremberg laws of 1935, and from 1939, the murder of disabled people.",
        "{g2.4}Moscow, 1936 to 1938: the show trials, and the Great Purge. The party is decimated, the army weakened.",
        "{g2.5}And 1940. Yezhov, the head of the Soviet police during the purge, is executed. "
        "And in Mexico, Trotsky, Stalin's great rival, is murdered by an agent of the Soviet police. Terror devours its own, even abroad.",
        "{-g2}{fr1}Six dates to keep. {fr1.1}1927, the OVRA. {fr1.2}1931, the White Sea Canal begins. {fr1.3}1933, Dachau. "
        "{fr1.4}1934, the Night of the Long Knives. {fr1.5}1937 and 1938, the Great Purge. {fr1.6}And 1940, Yezhov and Trotsky.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[21, 22, 23, 30, 38]),
        "fr1": dict(type="frise", items=[
            dict(nom="OVRA", d=1927, q="Italy"), dict(nom="White Sea Canal", d=1931, q="1931–33, Gulag"),
            dict(nom="Dachau", d=1933, q="Germany"), dict(nom="Long Knives", d=1934, q="85 murdered"),
            dict(nom="Great Purge", d=1937, q="1937–38: 680,000"), dict(nom="Yezhov, Trotsky", d=1940, q="executed, murdered")]),
    }),

    # ================================================================ II.3, idée 1 : une méthode de gouvernement
    dict(id="methode", chap="II.3 · Terror, a method of government", fond="nuit", humeur="mystere",
         retenir="Totalitarian violence is permanent, organised, planned. Arendt: “dominating and terrorizing human beings from within”: fear so deep that each person censors himself. Example: Tintin in the Land of the Soviets (1930).",
         beats=[
        "{def1}Now the course, idea by idea. Idea one: in a totalitarian regime, terror is not a failure of order. "
        "It is {!a method of government}a method of government. "
        "{def1.1}Violence is not the exceptional answer to a crisis: it is permanent, organised and planned.",
        "{-def1}Hannah Arendt, whom you met in episode one, wrote that these regimes had found",
        ("C", "a means of dominating and terrorizing human beings from within", "c_ar"),
        "{-c_ar}{fear}So the point is not only to punish. {fear.1}It is to install fear so deeply {fear.2}that each person censors himself. "
        "{fear.3}And so, {fear.4}obedience no longer needs to be commanded.",
        "{-fear}{tin}The example: a comic book. In 1930, Hergé's Tintin in the Land of the Soviets already showed Western readers "
        "a police state, with staged elections and a hidden famine. A caricature, of course. "
        "{tin.1}But it spread the image of Soviet terror long before historians could open the archives.",
    ], vis={
        "def1": dict(type="def", cles=["permanent", "organised", "planned"], terme="Idea 1 · terror as a method",
                     t="Violence is not the exceptional answer to a crisis: it is permanent, organised and planned.",
                     etape="Not a failure of order: a way of governing", x=170, y=200, w=940),
        "c_ar": dict(type="cit", a="Hannah Arendt", o="The Origins of Totalitarianism, 1951", x=200, y=200, w=880),
        "fear": dict(type="liste", titre="How terror works", cles=["punish", "fear", "censors", "obedience"], items=[
            "Not only to punish", "To install fear deep inside", "Each person censors himself",
            "Obedience no longer needs to be commanded"], x=170, y=140, w=940),
        "tin": dict(type="note", terme="Example · Hergé, 1930", cles=["staged", "hidden", "famine"],
                    t="Tintin in the Land of the Soviets: a police state, staged elections, a hidden famine.",
                    etape="A caricature that spread the image of terror long before the archives opened", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 2 : la police politique
    dict(id="police", chap="II.3 · A political police above the law", fond="nuit", humeur="tension",
         retenir="Italy: the OVRA (1927) · Germany: the Gestapo (state police, 1933) and the S.S. (party police), both under Himmler from 1936 · USSR: the OGPU, then the NKVD (1934), which runs the deportations. They answer to the leader, never to a judge.",
         beats=[
        "{g3}{g3.1}Idea two: each regime built a political police that answered to the party, not to the courts. "
        "This is the instrument of terror: {!a police above the law}a police placed above the law.",
        "{pol}{pol.1}In Italy, Mussolini created the OVRA in 1927. "
        "{pol.2}In Germany, two forces: the Gestapo, the state police, from 1933, and the S.S., the police of the party. "
        "{pol.3}In the Soviet Union, the OGPU, then from 1934 the NKVD, which organised the deportations to the labour camps.",
        "{-pol}{-g3}{him}The example to remember: Heinrich Himmler. The Gestapo was placed under his authority, "
        "and from 1936 he held both German police forces at once, the state police and the party police. "
        "{him.1}The party and the state merged in one man.",
        "{-him}{voc}The key point: because these bodies answered to the leader, {!no judge}no judge could protect a citizen from them. "
        "In your copy, call it by its name: a political police.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[22]),
        "pol": dict(type="liste", titre="Three political police forces", petit=True, bande=True, x=60, y=130, w=620, items=[
            "Italy: the OVRA, 1927", "Germany: Gestapo (state, 1933) + S.S. (party)", "USSR: OGPU, then NKVD (1934)"]),
        "him": dict(type="cols", g="The Gestapo", gq="the state police, created in 1933", d="The S.S.", dq="the police of the party",
                    vs="+", repere="Both headed by Himmler from 1936"),
        "voc": dict(type="def", cles=["leader", "courts", "judge"], terme="Vocabulary · political police",
                    t="A police answering to the leader or the party rather than to the courts: OVRA, Gestapo, NKVD.",
                    etape="No judge can protect a citizen from it", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 3 : les procès de Moscou
    dict(id="proces", chap="II.3 · Justice as theatre: the Moscow trials", fond="guerre", humeur="tension",
         retenir="Show trials (1936–38): old Bolsheviks confess to invented crimes after threats to their families. The Great Purge (1937–38): 680,000 executions, the party decimated, the army weakened, Stalin reinforced. Zinoviev and Kamenev shot in 1936, Rykov in 1938.",
         beats=[
        "{g4}{g4.1}Idea three: justice is turned into theatre. Soviet terror culminated in the Moscow trials: "
        "{!show trials}show trials, staged for the public. Old Bolsheviks, companions of Lenin, confessed to crimes they had not committed, "
        "after their families had been threatened.",
        "{-g4}At his trial in 1936, Zinoviev declared himself",
        ("C", "the principal organiser of Kirov's assassination", "c_zi"),
        "{-c_zi}And Kamenev said he had been",
        ("C", "actuated by boundless hatred and by lust of power", "c_ka"),
        "{-c_ka}{photo}Now look at one photograph of 1925. {photo.1}Stalin stands with Zinoviev, Kamenev and Alexei Rykov. "
        "{photo.2}Stalin had all three men in that picture shot: {photo.3}Zinoviev and Kamenev in 1936, Rykov in 1938.",
        "{-photo}{purge}Then the Great Purge of 1937 and 1938. {!680,000}The worksheet counts six hundred and eighty thousand executions. "
        "It decimated the party and weakened the army.",
        "{-purge}{para}And here is the paradox to explain in an essay: the purge reinforced Stalin, "
        "precisely because it destroyed everyone who could have replaced him. "
        "{para.1}One detail of dates: the show trials run from 1936 to 1938; the Great Purge, in 1937 and 1938.",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[30]),
        "c_zi": dict(type="cit", a="Grigory Zinoviev", o="Moscow trial, 1936", x=200, y=210, w=880),
        "c_ka": dict(type="cit", a="Lev Kamenev", o="Moscow trial, 1936", x=200, y=210, w=880),
        "photo": dict(type="liste", titre="One photograph, 1925", items=[
            "Stalin, Zinoviev, Kamenev, Rykov", "All three companions shot on Stalin's orders",
            "Zinoviev and Kamenev in 1936 · Rykov in 1938"], x=170, y=150, w=940),
        "purge": dict(type="mot", t="680,000", g="executions in the Great Purge, 1937–38 · the party decimated, the army weakened", y=240, taille=140),
        "para": dict(type="note", terme="The paradox", cles=["reinforced", "replaced"],
                     t="The purge reinforced Stalin: it destroyed everyone who could have replaced him.",
                     etape="Dates: show trials 1936–38 · Great Purge 1937–38", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 4 : le camp
    dict(id="camps", chap="II.3 · The camp, a permanent institution", fond="nuit", humeur="mystere",
         retenir="The Gulag: camps placed where labour was needed; the White Sea–Baltic Canal (227 km, 1931–33, by hand); over 1.5 million prisoners in the early 1950s. Dachau (1933): prisoners sorted by coloured triangles. M. Ros: the Nazis did not invent the camp; they added the gas chamber.",
         beats=[
        "{g5}{g5.1}Idea four: the camp becomes a permanent institution, and forced labour an economic resource. "
        "Repression is not only judicial: it is territorial. Whole populations are confined.",
        "{g5.2}The Soviet Gulag spread its camps across the whole country, and it chose their places where labour was needed: "
        "mines, timber, canals. So terror also produced. "
        "The example: the White Sea to Baltic Canal, two hundred and twenty-seven kilometres dug between 1931 and 1933, "
        "largely with hand tools: the first great Soviet project built by Gulag prisoners.",
        "{-g5}{gul}And the worksheet's graph gives the scale. {gul.1}{gul.2}{gul.3}In the early 1950s, the camp population passes "
        "{!one and a half million}one and a half million prisoners.",
        "{-gul}{tri}In Germany, Dachau opened in 1933, for everyone deemed incompatible with society. "
        "And the camps classified their prisoners by coloured triangles. "
        "{tri.1}Red for political prisoners. {tri.2}Green for criminals. {tri.3}Pink for homosexuals. "
        "{tri.4}Black for those called anti-social. {tri.5}Purple for Jehovah's Witnesses. {tri.6}And a yellow triangle added for Jews.",
        "{-tri}{ros}And keep Monsieur Ros's sentence. The Nazis did not invent the camp. {ros.1}What they added was the gas chamber.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[17]),
        "gul": dict(type="graphe", titre="Gulag camp population (worksheet graph)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1929.5, 1953.5], y=[0, 2.0], gx=[1930, 1935, 1940, 1945, 1950], gy=[0.5, 1.0, 1.5],
                            lx="year", ly="million prisoners"),
                    el=[dict(type="droite", pts=[[1930, 1.5], [1953, 1.5]], c="iv", tir=True, lbl="1.5 million", lp=[1932.5, 1.6], dur=1.0),
                        dict(type="texte", x=1932, y=0.25, t="1931–33: the White Sea Canal", c="sa"),
                        dict(type="point", x=1952, y=1.6, c="ca", lbl="early 1950s", lp=[1948.5, 1.82])]),
        "tri": dict(type="liste", titre="Nazi camps · coloured triangles", petit=True,
                    marques=["R", "G", "P", "B", "Pu", "Y"], items=[
            "Red: political prisoners", "Green: criminals", "Pink: homosexuals", "Black: “anti-socials”",
            "Purple: Jehovah's Witnesses", "Yellow, added: Jews"], x=170, y=100, w=940),
        "ros": dict(type="note", terme="M. Ros, in class", cles=["invent", "gas"],
                    t="The Nazis did not invent the camp…",
                    etape="… what they added was the gas chamber", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 5 : au nom de la biologie
    dict(id="biologie", chap="II.3 · Germans struck in the name of biology", fond="nuit", humeur="mystere",
         retenir="1933: law on forced sterilisation (nine conditions, e.g. blindness, deafness, schizophrenia): about 400,000 sterilised, 1933–45. Propaganda by cost: 5.50 Reichsmarks a day. T4 (1939–41): about 70,000 disabled Germans killed, mostly in gas chambers.",
         beats=[
        "{g6}{g6.1}Idea five: Nazi violence also struck Germans themselves, in the name of biology. "
        "Racial doctrine produced violence inside the German population.",
        "{-g6}{bio}{bio.1}In 1933, a law allowed the forced sterilisation of Germans with conditions presumed hereditary. "
        "{bio.2}Nine conditions were listed, including blindness, deafness and schizophrenia. "
        "About {!400,000}four hundred thousand people were sterilised between 1933 and 1945.",
        "{bio.3}And propaganda justified it by cost. A poster compared the five Reichsmarks fifty spent every day on one sick person "
        "with the cost of a healthy family.",
        "{bio.4}In 1939, the logic went further, into killing. Between 1939 and 1941, the doctors of the T4 programme, "
        "called euthanasia, killed about {!70,000}seventy thousand disabled Germans, mostly in gas chambers built for the purpose.",
        "{-bio}{lien}Notice the link with episode four: the German New Man was a purified race. "
        "{lien.1}Sterilisation and T4 are that ideology applied to human bodies. "
        "And notice the gas chambers: built here, in Germany, before the war in the East.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[23]),
        "bio": dict(type="liste", titre="Violence in the name of biology", cles=["sterilisation", "400,000", "cost", "70,000"], items=[
            "1933: a law on forced sterilisation", "Nine conditions: blindness, deafness, schizophrenia… → ≈ 400,000 sterilised, 1933–45",
            "Propaganda by cost: 5.50 Reichsmarks a day for one sick person", "T4, 1939–41: ≈ 70,000 disabled Germans killed, mostly by gas"],
            x=150, y=130, w=980),
        "lien": dict(type="def", cles=["purified", "bodies"], terme="Link · the New Man (episode 4)",
                     t="The German New Man was a purified race: sterilisation and T4 apply the ideology to human bodies.",
                     etape="Gas chambers built in Germany for T4, from 1939", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 6 : la terreur dévore les siens
    dict(id="siens", chap="II.3 · Terror strikes the regime's own men", fond="guerre", humeur="tension",
         retenir="No one is safe: Night of the Long Knives (1934, 85 murdered, the SA leadership) · Yezhov, head of the NKVD, executed in 1940 and replaced by Beria · Trotsky murdered in Mexico (1940) by a Soviet agent. When loyalty no longer protects, obedience is anticipated.",
         beats=[
        "{g7}{g7.1}Idea six, the most revealing one: terror turns against the regime's own men. {!No one is safe}No one is safe, "
        "not even those who serve it. And that is what makes it total.",
        "{own}{own.1}In Germany, the Night of the Long Knives, in 1934: the regime purges its own paramilitary ranks. "
        "Eighty-five people are murdered, among them the leadership of the SA. "
        "{own.2}In the Soviet Union, the Great Purge ends by devouring the head of the police himself: Yezhov, "
        "Stalin's most trusted police chief, is executed in 1940. He is replaced by Beria. "
        "{own.3}And terror reaches abroad: Leon Trotsky, Stalin's most influential rival, is assassinated in Mexico in 1940, "
        "by an agent of the Soviet police.",
        "{-own}{-g7}{ber}One precision about Beria, from outside the course: he headed the NKVD from 1938 to 1945, "
        "then stayed in charge of the Soviet police apparatus until 1953.",
        "{-ber}{eff}Now, why is this so important? {eff.1}When loyalty no longer protects you, obeying is not enough. "
        "{eff.2}You must anticipate what the leader wants, before he asks. {eff.3}And that is exactly the effect sought. "
        "Remember the photograph of episode four: Yezhov beside Stalin, then erased from the same image.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[38]),
        "own": dict(type="liste", titre="Terror devours its own", petit=True, bande=True, x=60, y=130, w=620, items=[
            "1934 · Night of the Long Knives: 85 murdered", "1940 · Yezhov, head of the NKVD, executed",
            "1940 · Trotsky murdered in Mexico"]),
        "ber": dict(type="note", terme="A precision · outside the course", cles=["1938", "1945", "1953"],
                    t="Beria headed the NKVD from 1938 to 1945, then stayed in charge of the Soviet police apparatus until 1953.",
                    etape="The course says he “held the post until 1953”", x=170, y=200, w=940),
        "eff": dict(type="liste", titre="The effect sought", items=[
            "Loyalty no longer protects", "Obedience must be anticipated, not just given", "Exactly what the regime wants"],
            x=170, y=150, w=940),
    }),

    # ================================================================ II.3, idée 7 : l'Italie
    dict(id="italie", chap="II.3 · Italian terror: a different scale", fond="nuit", humeur="calme",
         retenir="Matteotti murdered (1924) → the totalitarian state. State Defence Law (1926): death penalty, Special Court for “enemies of the State” · OVRA (1927). Far fewer death sentences; opponents sent to the confino, on islands. Repression legalised rather than industrialised.",
         beats=[
        "{g8}{g8.1}Idea seven: Italian terror was real, but of a different scale, and the comparison must respect that. "
        "Fascist violence founded the regime, then became routine. It never reached the scale of the other two.",
        "{-g8}{it}{it.1}The turning point: the murder of the socialist deputy Matteotti, in 1924. After it, Mussolini abandoned parliament "
        "and built the totalitarian state: the opposition press suppressed, the non-fascist ministers excluded. "
        "{it.2}In 1926, the State Defence Law restored the death penalty, and set up a Special Court for the enemies of the State. "
        "{it.3}In 1927, the OVRA followed. "
        "{it.4}But the Special Court passed far fewer death sentences than the Soviet or German systems. "
        "Opponents were sent to the confino: internal exile, on remote islands.",
        "{-it}{form}So the formula to use: in Italy, repression was {!legalised rather than industrialised}legalised rather than industrialised. "
        "Hence Monsieur Ros's question: a less oppressive terror?",
        "{-form}{lib}One correction. The course says that Italy had no concentration camps. That is true of the repression of opponents "
        "in Italy before the war: they were sent to the confino. {lib.1}But, outside the course: in its colony of Libya, Fascist Italy "
        "confined the population of Cyrenaica in concentration camps, from 1930 to 1933. Write: no camps for opponents in Italy itself.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[14]),
        "it": dict(type="liste", titre="Italy: terror made legal", items=[
            "1924 · Matteotti murdered → the totalitarian state", "1926 · State Defence Law: death penalty, Special Court",
            "1927 · the OVRA", "Far fewer death sentences · opponents sent to the confino"], x=150, y=130, w=980),
        "form": dict(type="mot", t="Legalised, not industrialised", g="“Less oppressive terror?” · M. Ros's question mark", y=250, taille=78),
        "lib": dict(type="note", terme="Watch out · a correction", cles=["opponents", "Libya", "Cyrenaica"],
                    t="No camps for opponents in Italy itself: they were sent to the confino.",
                    etape="Outside the course: in Libya, Italy confined the population of Cyrenaica in camps, 1930–33", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 8 : la logique commune
    dict(id="ennemi", chap="II.3 · The common logic: choose an enemy", fond="nuit", humeur="tension",
         retenir="All three: a secret police, opponents silenced or killed, and above all an enemy of the nation, which makes violence seem justified. USSR: the kulaks · Germany: Jews, Roma, homosexuals, the disabled (conspiracy theory of enemies within) · Italy: “enemies of the State”.",
         beats=[
        "{g9}{g9.1}Idea eight: the common logic of the three terrors. All three used a secret police to threaten the population. "
        "All three silenced or killed their opponents. And above all, all three {!chose an enemy of the nation}chose an enemy of the nation.",
        "{-g9}{en}Once an enemy is chosen, violence against part of the population seems justified to the rest. "
        "{en.1}In the Soviet Union: the kulaks, as in Worksheet two. "
        "{en.2}In Germany: Jews, Roma, prostitutes, homosexuals and disabled people, four hundred thousand of whom were forcibly sterilised. "
        "{en.3}In Italy: the enemies of the State, tried by the Special Court.",
        "{-en}{cons}And in Germany, this rested on a conspiracy theory: the nation was supposedly undermined by {!enemies from within}enemies from within. "
        "{cons.1}You know its origin: the stab-in-the-back myth of 1918, from episode two.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[15]),
        "en": dict(type="liste", titre="One enemy of the nation per regime", cles=["kulaks", "Jews", "enemies"], items=[
            "USSR: the kulaks (Worksheet 2)", "Germany: Jews, Roma, prostitutes, homosexuals, the disabled",
            "Italy: the “enemies of the State” (Special Court)"], x=150, y=150, w=980),
        "cons": dict(type="def", cles=["conspiracy", "within"], terme="Germany · a conspiracy theory",
                     t="The nation was supposedly undermined by enemies from within.",
                     etape="Its root: the stab-in-the-back myth of 1918 (episode 2)", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : la Worksheet 4
    dict(id="ws4", chap="Your turn · Worksheet 4", fond="aube", humeur="calme",
         retenir="Worksheet 4, six similarities: police above the law · terror wearing legality · enemies by category · camps and forced labour · terror striking the regime's men · the same function: to govern. Differences: scale, criterion (social / biological / political), counter-powers in Italy.",
         beats=[
        "{ex1}Your turn. This is the task of Worksheet four: {!find the similarities}find the similarities in the use of violence "
        "by the three regimes. Aim for five or six, each with one example per regime.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{sim}Here are the six similarities on the site. "
        "{sim.1}One: a political police above the law: the OVRA, the Gestapo and the S.S., the NKVD. "
        "{sim.2}Two: terror wearing the mask of legality: the State Defence Law of 1926, the Nuremberg laws of 1935, the Moscow trials. "
        "{sim.3}Three: enemies designated by category, not by act: enemies of the State, Jews, kulaks. Violence becomes preventive. "
        "{sim.4}Four: the camp as a system and forced labour as a resource: Dachau, the Gulag. "
        "{sim.5}Five: terror striking the regime's own men: the Night of the Long Knives, Yezhov. "
        "{sim.6}And six, the same function: to govern. Remove rivals, destroy every autonomous organisation, produce the fear that makes people docile.",
        "{-sim}{dif}But a good answer never stops at similarities. Three differences. "
        "{dif.1}The scale: Italy is by far the least lethal. "
        "{dif.2}The criterion: social in the Soviet Union, biological in Germany, political in Italy. "
        "{dif.3}And Italy left counter-powers standing: the monarchy, and the Church, with the Concordat of 1929.",
        "{-dif}{ccl}The course's essay on this question concludes: {!identical in method, unequal in scale}identical in method and purpose, "
        "unequal in scale and in the principle that designates the victim.",
    ], vis={
        "ex1": dict(type="exo", niveau="quiz", titre="Find the similarities in the use of violence by the three regimes",
                    src="Worksheet 4", enonce=["Five or six similarities", "One example per regime for each"]),
        "pa1": dict(type="pause", t="List the similarities, with one example per regime for each.",
                    sous="Pause the video, write your list, then play on for the answers."),
        "sim": dict(type="liste", titre="Worksheet 4 · six similarities", petit=True, items=[
            "A political police above the law: OVRA · Gestapo and S.S. · NKVD",
            "Terror wearing legality: State Defence Law 1926 · Nuremberg laws 1935 · Moscow trials",
            "Enemies by category, not by act: “enemies of the State” · Jews · kulaks",
            "The camp as a system, forced labour as a resource: Dachau · the Gulag",
            "Terror striking the regime's own men: Long Knives 1934 · Yezhov 1940",
            "The same function: to govern, through fear"], x=110, y=90, w=1060),
        "dif": dict(type="liste", titre="… but three differences", items=[
            "The scale: Italy by far the least lethal", "The criterion: social (USSR) · biological (Germany) · political (Italy)",
            "Counter-powers in Italy: the monarchy, the Church (Concordat, 1929)"], x=150, y=150, w=980),
        "ccl": dict(type="mot", t="Same method, unequal scale", g="identical in method and purpose · unequal in scale and in the principle that designates the victim", y=240, taille=78),
    }),

    # ================================================================ le tableau des totalitarismes (1)
    dict(id="tableau1", chap="The totalitarianism table · seizure of power and ideology", fond="aube", humeur="calme",
         retenir="Seizure of power: Italy Oct. 1922 (squadristi, then the king) · Germany 30 Jan. 1933 (elections, Hindenburg, Reichstag fire decree, Enabling Act) · USSR from 1924, struggle inside the party, no electoral path. Ideology: same method; nation · race · class.",
         beats=[
        "{tb}Now let's put everything together: Monsieur Ros's totalitarianism table, filled in as far as the course has gone. "
        "Five blocks. {tb.1}Seizure of power. {tb.2}Ideology. {tb.3}Dictatorship. {tb.4}State terrorism. {tb.5}A controlled society. "
        "This is a synthesis of Parts one and two: if you can fill it from memory, you are ready.",
        "{-tb}{t1}Block one, seizure of power. The date. {t1.1}Italy: October 1922, the March on Rome, Mussolini appointed prime minister; "
        "a totalitarian state from 1925. {t1.2}Germany: the thirtieth of January 1933, Hitler chancellor; full powers in March 1933. "
        "{t1.3}The Soviet Union: from 1924, the death of Lenin; Stalin's power consolidated by 1928 and 1929.",
        "{-t1}{t2}The causes. {t2.1}Italy: the mutilated victory, the Biennio Rosso, the fear of communism, a weak parliament. "
        "{t2.2}Germany: the defeat of 1918, the Versailles Diktat, the stab-in-the-back myth, and the crisis of 1929, with about six million unemployed. "
        "{t2.3}The Soviet Union: the collapse of the Tsarist state in the war, the revolutions of 1917, and the civil war until 1922.",
        "{-t2}{t3}The process. {t3.1}Italy: squadristi violence, then a legal appointment by the king. "
        "{t3.2}Germany: elections, thirty-seven per cent in July 1932, the appointment by Hindenburg, the Reichstag fire decree, the Enabling Act. "
        "{t3.3}The Soviet Union: a struggle inside the party, Trotsky expelled in 1929. No electoral path at all.",
        "{-t3}{t4}Block two, ideology. {t4.1}The similarities are identical in all three: one single truth, the rejection of liberal democracy, "
        "total control, a New Man, violence held to be legitimate. These shared traits are precisely what the word totalitarianism designates. "
        "{t4.2}The specificities: the nation and the absolute State in Italy, not racist before 1938. "
        "{t4.3}Race struggle, antisemitism and Lebensraum in Germany. "
        "{t4.4}Class struggle, the abolition of private property and socialism in one country in the Soviet Union.",
    ], vis={
        "tb": dict(type="liste", titre="M. Ros's table · five blocks", items=[
            "Seizure of power: date, causes, process", "Ideology: similarities, specificities",
            "Dictatorship: cult, supports, party, symbols, slogans", "State terrorism: police, opponents",
            "A controlled society: youth, thought, economy, administration"], x=150, y=110, w=980),
        "t1": dict(type="liste", titre="Table · seizure of power: the date", marques=["IT", "DE", "SU"], items=[
            "Oct. 1922: March on Rome, appointed PM; totalitarian state from 1925",
            "30 Jan. 1933: chancellor; full powers in March 1933",
            "From 1924 (death of Lenin); power consolidated by 1928–29"], x=150, y=140, w=980),
        "t2": dict(type="liste", titre="Table · seizure of power: the causes", marques=["IT", "DE", "SU"], petit=True, items=[
            "“Mutilated victory”, Biennio Rosso, fear of communism, weak parliament",
            "Defeat of 1918, Versailles “Diktat”, stab-in-the-back myth, crisis of 1929, ≈ 6 million unemployed",
            "Collapse of the Tsarist state in the war, revolutions of 1917, civil war until 1922"], x=130, y=150, w=1020),
        "t3": dict(type="liste", titre="Table · seizure of power: the process", marques=["IT", "DE", "SU"], petit=True, items=[
            "Squadristi violence, then a legal appointment by the king",
            "Elections (37% in July 1932), Hindenburg, Reichstag fire decree, Enabling Act",
            "Struggle inside the party, Trotsky expelled in 1929: no electoral path"], x=130, y=150, w=1020),
        "t4": dict(type="liste", titre="Table · ideology", marques=["=", "IT", "DE", "SU"], petit=True, items=[
            "Common to all three: one truth, no liberal democracy, total control, a New Man, violence legitimate",
            "The nation and the absolute State; not racist before 1938",
            "Race struggle, antisemitism, Lebensraum",
            "Class struggle, no private property, “socialism in one country”"], x=130, y=120, w=1020),
    }),

    # ================================================================ le tableau des totalitarismes (2)
    dict(id="tableau2", chap="The totalitarianism table · dictatorship, terror, society", fond="aube", humeur="calme",
         retenir="Dictatorship: Duce / Führer / little father · PNF / NSDAP / CPSU · fasces / swastika / hammer and sickle. Terror: OVRA and Special Court / Gestapo and S.S. / OGPU, NKVD, Gulag. Society: Balilla / Hitler Youth / Komsomol. Part III blocks still to fill.",
         beats=[
        "{t5}Block three, the dictatorship. {t5.1}The cult of personality: il Duce, der Führer, the little father of the peoples, with Stalingrad in 1925. "
        "{t5.2}The single party: the PNF, the National Fascist Party; the NSDAP; the Communist Party of the Soviet Union. "
        "{t5.3}The symbols: the Roman fasces, the swastika, the hammer and sickle. "
        "{t5.4}The slogans: Il Duce ha sempre ragione; Heil Hitler; and Thank you Comrade Stalin, for our happy childhood.",
        "{-t5}{t6}And the supports, because these regimes did not rest on terror alone. "
        "{t6.1}In Italy: landowners, shopkeepers, veterans, the monarchy and the Church. "
        "{t6.2}In Germany: the middle classes, the conservative elites, the industrialists, the army. "
        "{t6.3}In the Soviet Union: the party apparatus, the bureaucracy, part of the working class.",
        "{-t6}{t7}Block four, state terrorism: today's lesson. {t7.1}The political police: the OVRA and the Special Court; "
        "the Gestapo and the S.S., both under Himmler; the OGPU, then the NKVD, and the Gulag. "
        "{t7.2}The opponents in Italy: socialists and communists, like Matteotti, and Jews from 1938. "
        "{t7.3}In Germany: communists, socialists, Jews, gypsies, homosexuals, the disabled, Jehovah's Witnesses. "
        "{t7.4}In the Soviet Union: kulaks, class enemies, old Bolsheviks, army officers.",
        "{-t7}{t8}Block five, a controlled society, from episode four. {t8.1}Youth: the Balilla, the Hitler Youth from ten to eighteen, the Komsomol. "
        "{t8.2}Thought and culture: the opposition press suppressed; racial instruction from 1933; socialist realism and retouched photographs. "
        "{t8.3}The economy: corporatism and autarky; rearmament and the Four-Year Plan; five-year plans and collectivisation. "
        "{t8.4}And the administration: in all three, the party doubles or controls the state.",
        "{-t8}{rest}Two blocks of the table are still empty: international issues, and on the road to war. "
        "They belong to Part three, the next two episodes.",
    ], vis={
        "t5": dict(type="liste", titre="Table · dictatorship", marques=["★", "P", "S", "“"], petit=True, items=[
            "Cult: il Duce · der Führer · “the little father of the peoples” (Stalingrad, 1925)",
            "Single party: PNF · NSDAP · Communist Party (CPSU)",
            "Symbols: the Roman fasces · the swastika · the hammer and sickle",
            "Slogans: “Il Duce ha sempre ragione” · “Heil Hitler” · “Thank you Comrade Stalin, for our happy childhood”"],
            x=130, y=120, w=1020),
        "t6": dict(type="liste", titre="Table · dictatorship: the supports", marques=["IT", "DE", "SU"], items=[
            "Landowners, shopkeepers, veterans, the monarchy, the Church (1929)",
            "Middle classes, conservative elites, industrialists, the army",
            "Party apparatus, bureaucracy, part of the working class"], x=150, y=140, w=980),
        "t7": dict(type="liste", titre="Table · state terrorism", marques=["⚑", "IT", "DE", "SU"], petit=True, items=[
            "Police: OVRA (1927), Special Court (1926) · Gestapo and S.S. under Himmler · OGPU, NKVD, the Gulag",
            "Opponents: socialists, communists (Matteotti, 1924); Jews from 1938",
            "Communists, socialists, Jews, gypsies, homosexuals, the disabled, Jehovah's Witnesses",
            "Kulaks, “class enemies”, old Bolsheviks, army officers"], x=130, y=120, w=1020),
        "t8": dict(type="liste", titre="Table · a controlled society", marques=["Y", "T", "€", "A"], petit=True, items=[
            "Youth: Balilla · Hitler Youth, 10 to 18 · Komsomol",
            "Thought: opposition press suppressed · racial instruction 1933 · socialist realism, retouched photos",
            "Economy: corporatism, autarky · rearmament, Four-Year Plan · five-year plans, collectivisation",
            "Administration: party and state merged · party officials double it · party controls every level"],
            x=130, y=120, w=1020),
        "rest": dict(type="note", terme="Still to fill · Part III", cles=["international", "war"],
                     t="International issues (will of expansion, feeling of superiority) · On the road to war (military nationalism, alliances).",
                     etape="Episodes 6 and 7", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : un essay « How far »
    dict(id="essai", chap="Your turn · an essay", fond="aube", humeur="calme",
         retenir="“Terror was the main tool”: I. Yes, a central and permanent tool (police, trials, camps, purges) · II. But not alone: propaganda, the cult, the New Man, the confidence of the masses (Arendt) · III. Unequal: Italy legalised rather than industrialised. Judgement: an essential tool, never the only one.",
         beats=[
        "{ex2}Now an essay. {!How far do you agree}“Terror was the main tool of totalitarian regimes.” How far do you agree?",
        "{-ex2}{met}Remember the method. {met.1}“How far” asks you to weigh: never “entirely”, never “not at all”. "
        "{met.2}Define the key word in the introduction. {met.3}Three parts: the case for, the case against, the nuance. "
        "{met.4}And a clear judgement, in the introduction and in the conclusion.",
        "{-met}{pa2}",
        ("P", 2.0),
        "{-pa2}{plan2}Here is a model plan. {plan2.1}Part one: yes, terror was a central tool, and a permanent one: "
        "a political police above the law, the Moscow trials and six hundred and eighty thousand executions, the camps from Dachau to the Gulag, "
        "and terror striking even the regime's own men. "
        "{plan2.2}Part two: but terror was never alone. Totalitarianism means coercion through terror and propaganda together: "
        "the cult of the leader, the rallies, the youth organisations, the New Man. "
        "And Hannah Arendt warns that Hitler and Stalin needed the confidence of the masses. "
        "{plan2.3}Part three: terror was unequal. Italy legalised repression rather than industrialised it, "
        "and Mussolini had to accept the king and the Church.",
        "{-plan2}{intro}And a model introduction. "
        "{intro.1}Totalitarianism is a regime that seeks total control of society, through coercion, to transform man according to an ideology. "
        "In Fascist Italy, Nazi Germany and Stalin's Soviet Union, terror was everywhere: police, trials, camps, purges. "
        "{intro.2}But was it their main tool, or one tool among others? "
        "{intro.3}This essay argues that terror was an essential tool of all three, but never the only one: "
        "it worked together with propaganda and popular support, and its scale varied greatly from one regime to another.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="“Terror was the main tool of totalitarian regimes.” How far do you agree?",
                    src="Essay question written for this video, on Parts I and II", enonce=["A plan in three parts", "Then write the introduction"]),
        "met": dict(type="liste", titre="“How far”: the method", cles=["weigh", "Define", "parts", "judgement"], items=[
            "Weigh: never “entirely”, never “not at all”", "Define the key word in the introduction",
            "Three parts: the case for · the case against · the nuance", "A clear judgement, from the introduction to the conclusion"],
            x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Write your plan in three parts, then your introduction: definition, problem, judgement.",
                    sous="Pause the video, write it on a sheet, then play on for a model."),
        "plan2": dict(type="liste", titre="A model plan", petit=True, items=[
            "Yes: a central, permanent tool · police above the law, Moscow trials (680,000 executions), camps, purges of the regime's own men",
            "But never alone: terror + propaganda · cult, rallies, youth, the New Man · Arendt: “the confidence of the masses”",
            "Unequal: Italy legalised rather than industrialised · the king and the Church remained"], x=110, y=120, w=1060),
        "intro": dict(type="liste", titre="A model introduction", petit=True, items=[
            "Definition: total control of society, through coercion, to transform man according to an ideology",
            "Problem: the main tool, or one tool among others?",
            "Judgement: an essential tool of all three, never the only one; with propaganda and support; unequal in scale"],
            x=110, y=130, w=1060),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Terror is a method of government: permanent, organised, planned, so that each person censors himself. "
        "{carte.2}Its instruments: a political police above the law, show trials, and the camp as a permanent institution, from Dachau to the Gulag. "
        "{carte.3}Its victims: enemies chosen by category, the kulaks, the Jews, the disabled, and even the regime's own men. "
        "{carte.4}And its limits: Italy legalised its repression rather than industrialised it, and terror never ruled alone.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: hegemonic ambitions. War as a value: Abyssinia, Lebensraum, and Japan.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="MASS TERROR", branches=[
            dict(t="A method", items=["permanent, planned", "Arendt: “from within”", "self-censorship"]),
            dict(t="Instruments", items=["OVRA · Gestapo, S.S. · NKVD", "Moscow trials · 680,000", "Dachau · the Gulag"]),
            dict(t="Victims", items=["kulaks · Jews · disabled", "400,000 sterilised · T4", "Long Knives · Yezhov"]),
            dict(t="Limits", items=["Italy: legalised", "confino, Special Court", "terror + support"])]),
        "fin": dict(type="mot", t="Next: hegemonic ambitions", g="Episode 6 · Abyssinia, Lebensraum, Japan", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="According to the course, what is terror in a totalitarian regime?",
         r=["A permanent, organised and planned method of government", "An exceptional answer to a crisis",
            "A sign that the regime is losing control", "A tool used only in wartime"], ok=0, voir="def1",
         ex="Arendt: “a means of dominating and terrorizing human beings from within”."),
    dict(q="Who headed both the Gestapo and the S.S.?",
         r=["Heinrich Himmler", "Nikolai Yezhov", "Joseph Goebbels", "Ernst Röhm"], ok=0, voir="him",
         ex="From 1936 Himmler held both German police forces: the state police and the party police."),
    dict(q="How many executions does the worksheet count for the Great Purge of 1937–38?",
         r=["680,000", "85", "70,000", "400,000"], ok=0, voir="purge",
         ex="85: the Night of the Long Knives · 70,000: T4 · 400,000: forced sterilisations."),
    dict(q="What was the White Sea–Baltic Canal?",
         r=["The first great Soviet project built by Gulag prisoners (1931–33)", "A Nazi camp near Munich",
            "The place of the Moscow trials", "A canal built by Italian opponents in the confino"], ok=0, voir="g5",
         ex="227 km dug largely with hand tools: terror also produced."),
    dict(q="In the Nazi camps, which triangle marked political prisoners?",
         r=["Red", "Green", "Pink", "Purple"], ok=0, voir="tri",
         ex="Green: criminals · pink: homosexuals · black: “anti-socials” · purple: Jehovah's Witnesses · yellow added for Jews."),
    dict(q="What did the T4 programme do between 1939 and 1941?",
         r=["Killed about 70,000 disabled Germans, mostly in gas chambers", "Sterilised 400,000 Germans",
            "Deported the kulaks", "Organised the Moscow trials"], ok=0, voir="bio",
         ex="The sterilisation law dates from 1933: about 400,000 people sterilised, 1933–45."),
    dict(q="Which Soviet police chief was executed in 1940?",
         r=["Nikolai Yezhov", "Lavrenti Beria", "Leon Trotsky", "Alexei Rykov"], ok=0, voir="own",
         ex="Beria replaced him; Trotsky was murdered in Mexico the same year; Rykov was shot in 1938."),
    dict(q="How does the course describe Italian repression?",
         r=["Legalised rather than industrialised", "Larger than the Soviet terror",
            "Based on a racial criterion from 1922", "Organised in concentration camps in Italy"], ok=0, voir="form",
         ex="State Defence Law (1926), Special Court, OVRA (1927), the confino on remote islands."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H2 · Part II.3, Worksheet 4, the totalitarianism table, Arendt in the introduction) as written on the site; Worksheet 4 answers suggested by the site; outside the course: Fascist camps in Libya (Cyrenaica, 1930–33) and Beria's dates at the head of the NKVD (1938–45); animated map of chapter 2 (site).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
