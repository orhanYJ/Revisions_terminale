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
  - le cours dit que Beria « held the post until 1953 » : il dirige le NKVD de 1938 à 1945 seulement, puis reste
    l'un des hommes les plus puissants autour de Staline jusqu'à sa chute en 1953 — précision hors cours dite ;
  - Iejov est remplacé par Beria (novembre 1938) avant d'être exécuté (1940) : ordre rétabli dans la narration ;
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
                 "Lebensraum": "Lay-bens-rowm", "Cyrenaica": "Sigh-reh-nay-ika",
                 "S.S.": "Ess Ess", "SA": "Ess Ay", "T4": "T four"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Moscow, nineteen thirty-six. In the dock stand old companions of Lenin. "
        "They confess to crimes they never committed. "
        "By the end of nineteen thirty-eight, the Great Purge has carried out six hundred and eighty thousand executions.",
        "{q1}Why would a regime terrorise its own people? And why would it end up striking its own men?",
        "{-q1}{-g0}{plan}Today: part two point three of the chapter. Mass terror. {plan.1}We start with the events, on the map. "
        "{plan.2}Then the course, idea by idea. The police, the trials, the camps, the purges. "
        "{plan.3}Then Worksheet four. What do the three terrors have in common? And what sets them apart? "
        "{plan.4}After that, the whole totalitarianism table, as a synthesis of parts one and two. "
        "{plan.5}Finally, an essay. Was terror the main tool of these regimes?",
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
        "{g1}Let's start on the map, in chronological order. {g1.1}Italy, from nineteen twenty-nine. "
        "Mussolini has to come to terms with the Church, and with the king. His opponents are usually not executed. "
        "They are sent into internal exile, on islands such as Lipari. "
        "The course asks it with a question mark. A less oppressive terror?",
        "{g1.2}Now the Soviet Union, from nineteen twenty-nine to nineteen thirty-two. This is forced collectivisation, "
        "which you saw in episode three. Any peasant who resists is called a kulak. A class enemy. "
        "His land and his animals are confiscated. And many are deported.",
        "{g1.3}Then the far north, from nineteen thirty-one to nineteen thirty-three. Prisoners of the Gulag dig the White Sea to Baltic Canal. "
        "Two hundred and twenty-seven kilometres, largely with hand tools. The camp has become a building site.",
        "{g1.4}And Ukraine, in nineteen thirty-two and thirty-three. This is the Holodomor. Grain is requisitioned, whatever the harvest. "
        "Rebellious villages are cut off from all supplies. The famine kills millions. "
        "It is a famine made by a political decision.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[14, 15, 17, 19]),
    }),

    # ================================================================ la carte : 1933-1940
    dict(id="carte2", chap="On the map: 1933 – 1940", fond="nuit", humeur="tension",
         retenir="27 Feb. 1933: the Reichstag fire · 1933: Gestapo, Dachau · 1933–39: sterilisation, Nuremberg laws, T4 · 1936–38: Moscow trials, Great Purge · 1940: Yezhov executed, Trotsky murdered in Mexico.",
         beats=[
        "{g2}{g2.1}Germany, the twenty-seventh of February, nineteen thirty-three. The Reichstag is on fire. "
        "The Nazis blame the communists. Freedoms are suspended. Thousands of communists are arrested.",
        "{g2.2}The same year, the political police is placed above the law. And the first camp opens at Dachau, near Munich. "
        "Italy has had its own political police, the OVRA, since nineteen twenty-seven. The Soviet Union gets the NKVD in nineteen thirty-four.",
        "{g2.3}From nineteen thirty-three, Nazi violence also strikes Germans, in the name of biology. "
        "First comes forced sterilisation. Then the Nuremberg laws, in nineteen thirty-five. "
        "And from nineteen thirty-nine, the murder of disabled people.",
        "{g2.4}Moscow, from nineteen thirty-six to nineteen thirty-eight. These are the show trials, and the Great Purge. "
        "The party is decimated. The army is weakened.",
        "{g2.5}And then, nineteen forty. Yezhov, who ran the Soviet police during the purge, is executed. "
        "In Mexico, Trotsky, Stalin's great rival, is murdered by an agent of the Soviet police. Terror devours its own. Even abroad.",
        "{-g2}{fr1}Six dates to keep. {fr1.1}Nineteen twenty-seven: the OVRA. {fr1.2}Nineteen thirty-one: work starts on the White Sea Canal. "
        "{fr1.3}Nineteen thirty-three: Dachau. {fr1.4}Nineteen thirty-four: the Night of the Long Knives. "
        "{fr1.5}Nineteen thirty-seven and thirty-eight: the Great Purge. {fr1.6}And nineteen forty: Yezhov, and Trotsky.",
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
        "{def1}Now the course, idea by idea. Idea one. In a totalitarian regime, terror is not a failure of order. "
        "It is {!a method of government}a method of government. "
        "{def1.1}Violence is not an exceptional answer to a crisis. It is permanent. It is organised. It is planned.",
        "{photo1}Hannah Arendt, whom you met in episode one, wrote that these regimes had found{-def1}",
        ("C", "a means of dominating and terrorizing human beings from within", "c_ar"),
        "{-c_ar}{-photo1}{fear}So what is terror for? {fear.1}Not only to punish. {fear.2}It plants fear deep inside each person. "
        "{fear.3}So deep that everyone censors himself. "
        "{fear.4}And then, obedience no longer needs to be commanded.",
        "{-fear}{tin}The example is a comic book. In nineteen thirty, Hergé's Tintin in the Land of the Soviets "
        "already showed Western readers a police state. Staged elections. A hidden famine. A caricature, of course. "
        "{tin.1}But it spread the image of Soviet terror long before historians could open the archives.",
    ], vis={
        "def1": dict(type="def", cles=["permanent", "organised", "planned"], terme="Idea 1 · terror as a method",
                     t="Violence is not the exceptional answer to a crisis: it is permanent, organised and planned.",
                     etape="Not a failure of order: a way of governing", x=170, y=200, w=940),
        "photo1": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, author of The Origins of Totalitarianism (1951), in 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
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
        "{g3}{g3.1}Idea two. Each regime built a political police. It answered to the party, not to the courts. "
        "This is the instrument of terror: {!a police above the law}a police placed above the law.",
        "{pol}{pol.1}In Italy, Mussolini created the OVRA in nineteen twenty-seven. "
        "{pol.2}Germany had two forces. The Gestapo, the state police, from nineteen thirty-three. And the S.S., the police of the party. "
        "{pol.3}In the Soviet Union, there was first the OGPU. Then, from nineteen thirty-four, the NKVD. "
        "It organised the deportations to the labour camps.",
        "{-pol}{-g3}{him}The example to remember is Heinrich Himmler. The Gestapo was placed under his authority. "
        "And from nineteen thirty-six, he held both German police forces at once: the state police, and the party police. "
        "{him.1}In one man, party and state had merged.",
        "{-him}{voc}Why? Because these bodies answered to the leader. "
        "So {!no judge}no judge could protect a citizen from them. "
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
        "{g4}{g4.1}Idea three. Justice is turned into theatre. Soviet terror reached its peak with the Moscow trials. "
        "These were {!show trials}show trials, staged for the public. Old Bolsheviks, companions of Lenin, "
        "confessed to crimes they had not committed. Why? Because their families had been threatened.",
        "At his trial in nineteen thirty-six, Zinoviev declared himself{-g4}",
        ("C", "the principal organiser of Kirov's assassination", "c_zi"),
        "{-c_zi}And Kamenev said he had been",
        ("C", "actuated by boundless hatred and by lust of power", "c_ka"),
        "{-c_ka}{photo}Now look at one photograph, taken in nineteen twenty-five. {photo.1}Stalin stands with Zinoviev, Kamenev, and Alexei Rykov. "
        "{photo.2}Stalin had all three of those men shot. {photo.3}Zinoviev and Kamenev in nineteen thirty-six. Rykov in nineteen thirty-eight.",
        "{-photo}{photo2}{purge}Then came the Great Purge, in nineteen thirty-seven and thirty-eight. "
        "{!680,000}The worksheet counts six hundred and eighty thousand executions. "
        "The party was decimated. The army was weakened.",
        "{-purge}{para}Here is the paradox to explain in an essay. The purge made Stalin stronger. Why? "
        "Precisely because it destroyed everyone who could have replaced him. "
        "{para.1}And one detail of dates. The show trials run from nineteen thirty-six to thirty-eight. "
        "The Great Purge covers nineteen thirty-seven and thirty-eight.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[30]),
        "c_zi": dict(type="cit", a="Grigory Zinoviev", o="Moscow trial, 1936", x=200, y=210, w=880),
        "c_ka": dict(type="cit", a="Lev Kamenev", o="Moscow trial, 1936", x=200, y=210, w=880),
        "photo": dict(type="liste", titre="One photograph, 1925", items=[
            "Stalin, Zinoviev, Kamenev, Rykov", "All three companions shot on Stalin's orders",
            "Zinoviev and Kamenev in 1936 · Rykov in 1938"], x=170, y=150, w=940),
        "photo2": dict(type="tableau", img="h2-moscow-trial", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.1, .5, .45],
                       legende="The defendants of the second Moscow trial in court, January 1937 · Unknown photographer, public domain"),
        "purge": dict(type="mot", t="680,000", g="executions in the Great Purge, 1937–38 · the party decimated, the army weakened", y=240, taille=140),
        "para": dict(type="note", terme="The paradox", cles=["reinforced", "replaced"],
                     t="The purge reinforced Stalin: it destroyed everyone who could have replaced him.",
                     etape="Dates: show trials 1936–38 · Great Purge 1937–38", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 4 : le camp
    dict(id="camps", chap="II.3 · The camp, a permanent institution", fond="nuit", humeur="mystere",
         retenir="The Gulag: camps placed where labour was needed; the White Sea–Baltic Canal (227 km, 1931–33, by hand); over 1.5 million prisoners in the early 1950s. Dachau (1933): prisoners sorted by coloured triangles. The course: the Nazis did not invent the camp; they added the gas chamber.",
         beats=[
        "{g5}{g5.1}Idea four. The camp becomes a permanent institution, and forced labour becomes an economic resource. "
        "Repression is not only judicial. It is territorial. Whole populations are confined.",
        "{g5.2}The Soviet Gulag spread its camps across the whole country. And it placed them where labour was needed. "
        "In mines, in forests, along canals. So terror also produced. "
        "{-g5}{photo3}The example is the White Sea to Baltic Canal. Two hundred and twenty-seven kilometres, "
        "dug between nineteen thirty-one and nineteen thirty-three, largely with hand tools. "
        "It was the first great Soviet project built by Gulag prisoners.",
        "{-photo3}{gul}The worksheet's graph gives the scale. {gul.1}{gul.2}{gul.3}By the early nineteen-fifties, "
        "the camps hold more than {!one and a half million}one and a half million prisoners.",
        "{-gul}{tri}Germany opened Dachau in nineteen thirty-three. It was meant for everyone judged incompatible with society. "
        "Inside, prisoners were sorted by coloured triangles. "
        "{tri.1}Red for political prisoners. {tri.2}Green for criminals. {tri.3}Pink for homosexuals. "
        "{tri.4}Black for those called anti-social. {tri.5}Purple for Jehovah's Witnesses. {tri.6}And a yellow triangle was added for Jews.",
        "{-tri}{phr}Keep this sentence of the course. The Nazis did not invent the camp. {phr.1}What they added was the gas chamber.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[17]),
        "photo3": dict(type="tableau", img="h2-belomorkanal", de=[1.0, .3, .5], a=[1.05, .7, .5],
                       legende="Gulag prisoners digging the White Sea-Baltic Canal, summer 1932 · Unknown photographer, public domain"),
        "gul": dict(type="graphe", titre="Gulag camp population (worksheet graph)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1929.5, 1953.5], y=[0, 2.0], gx=[1930, 1935, 1940, 1945, 1950], gy=[0.5, 1.0, 1.5],
                            lx="year", ly="million prisoners"),
                    el=[dict(type="droite", pts=[[1947, 1.5], [1953, 1.5]], c="iv", tir=True, lbl="1.5 million", lp=[1944, 1.62], dur=1.0),
                        dict(type="texte", x=1932, y=0.25, t="1931–33: the White Sea Canal", c="sa"),
                        dict(type="point", x=1952, y=1.6, c="ca", lbl="early 1950s", lp=[1948.5, 1.82])]),
        "tri": dict(type="liste", titre="Nazi camps · coloured triangles", petit=True,
                    marques=["R", "G", "P", "B", "Pu", "Y"], items=[
            "Red: political prisoners", "Green: criminals", "Pink: homosexuals", "Black: “anti-socials”",
            "Purple: Jehovah's Witnesses", "Yellow, added: Jews"], x=170, y=100, w=940),
        "phr": dict(type="note", terme="The course sums it up", cles=["invent", "gas"],
                    t="The Nazis did not invent the camp…",
                    etape="… what they added was the gas chamber", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 5 : au nom de la biologie
    dict(id="biologie", chap="II.3 · Germans struck in the name of biology", fond="nuit", humeur="mystere",
         retenir="1933: law on forced sterilisation (nine conditions, e.g. blindness, deafness, schizophrenia): about 400,000 sterilised, 1933–45. Propaganda by cost: 5.50 Reichsmarks a day. T4 (1939–41): about 70,000 disabled Germans killed, mostly in gas chambers.",
         beats=[
        "{g6}{g6.1}Idea five. Nazi violence also struck Germans themselves, in the name of biology. "
        "Racial doctrine produced violence inside the German population.",
        "{-g6}{bio}{bio.1}In nineteen thirty-three, a law allowed forced sterilisation. It targeted Germans with conditions presumed to be hereditary. "
        "{bio.2}The law listed nine conditions. Among them: blindness, deafness, and schizophrenia. "
        "Between nineteen thirty-three and nineteen forty-five, about {!400,000}four hundred thousand people were sterilised.",
        "{bio.3}Propaganda justified it by cost. One poster showed what one sick person cost every day: five Reichsmarks fifty. "
        "And it set that sum against the cost of a healthy family.",
        "{bio.4}In nineteen thirty-nine, the logic went further. Into killing. "
        "From nineteen thirty-nine to nineteen forty-one, the doctors of the T4 programme, called euthanasia, "
        "killed about {!70,000}seventy thousand disabled Germans. Most of them died in gas chambers built for the purpose.",
        "{-bio}{lien}Notice the link with episode four. The German New Man was a purified race. "
        "{lien.1}Sterilisation and T4 are that ideology, applied to human bodies. "
        "And notice the gas chambers. They were built here, in Germany, before the war in the East.",
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
        "{g7}{g7.1}Idea six is the most revealing one. Terror turns against the regime's own men. "
        "{!No one is safe}No one is safe, not even those who serve it. And that is what makes it total.",
        "{own}{own.1}Germany, nineteen thirty-four: the Night of the Long Knives. The regime purges its own paramilitary ranks. "
        "Eighty-five people are murdered, among them the leaders of the SA. "
        "{own.2}In the Soviet Union, the Great Purge ends by devouring the police chief himself. "
        "Yezhov was Stalin's most trusted police chief. He is replaced by Beria, and executed in nineteen forty. "
        "{own.3}Terror even reaches abroad. Leon Trotsky, Stalin's most influential rival, is assassinated in Mexico in nineteen forty. "
        "The killer is an agent of the Soviet police.",
        "{-own}{-g7}{ber}A precision about Beria, from outside the course. He headed the NKVD from nineteen thirty-eight to nineteen forty-five. "
        "Then he stayed among Stalin's most powerful men, until his fall in nineteen fifty-three.",
        "{-ber}{eff}Now, why is this so important? {eff.1}When loyalty no longer protects you, obeying is not enough. "
        "{eff.2}You must guess what the leader wants, before he even asks. {eff.3}And that is exactly the effect the regime is looking for. "
        "Remember the photograph from episode four? Yezhov beside Stalin. Then erased from the very same image.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[38]),
        "own": dict(type="liste", titre="Terror devours its own", petit=True, bande=True, x=60, y=130, w=620, items=[
            "1934 · Night of the Long Knives: 85 murdered", "1940 · Yezhov, head of the NKVD, executed",
            "1940 · Trotsky murdered in Mexico"]),
        "ber": dict(type="note", terme="A precision · outside the course", cles=["1938", "1945", "1953"],
                    t="Beria headed the NKVD from 1938 to 1945, then remained one of Stalin's most powerful men until his fall in 1953.",
                    etape="The course says he “held the post until 1953”", x=170, y=200, w=940),
        "eff": dict(type="liste", titre="The effect sought", items=[
            "Loyalty no longer protects", "Obedience must be anticipated, not just given", "Exactly what the regime wants"],
            x=170, y=150, w=940),
    }),

    # ================================================================ II.3, idée 7 : l'Italie
    dict(id="italie", chap="II.3 · Italian terror: a different scale", fond="nuit", humeur="calme",
         retenir="Matteotti murdered (1924) → the totalitarian state. State Defence Law (1926): death penalty, Special Court for “enemies of the State” · OVRA (1927). Far fewer death sentences; opponents sent to the confino, on islands. Repression legalised rather than industrialised.",
         beats=[
        "{g8}{g8.1}Idea seven. Italian terror was real. But its scale was different, and a fair comparison must respect that. "
        "Fascist violence founded the regime, and then it became routine. It never reached the scale of the other two.",
        "{-g8}{it}{it.1}The turning point came in nineteen twenty-four, with the murder of the socialist deputy Matteotti. "
        "After it, Mussolini abandoned parliament and built the totalitarian state. The opposition press was suppressed. "
        "The non-fascist ministers were excluded. "
        "{it.2}In nineteen twenty-six, the State Defence Law restored the death penalty. "
        "It also set up a Special Court for the enemies of the State. "
        "{it.3}The OVRA followed, in nineteen twenty-seven. "
        "{it.4}But the Special Court passed far fewer death sentences than the Soviet or German systems. "
        "Opponents were sent to the confino. That meant internal exile, on remote islands.",
        "{-it}{form}So use this formula. In Italy, repression was {!legalised rather than industrialised}legalised rather than industrialised. "
        "Hence the course's question: a less oppressive terror?",
        "{-form}{lib}Now, one correction. The course says that Italy had no concentration camps. "
        "That is true of the way opponents were punished in Italy before the war. They were sent to the confino. "
        "{lib.1}But here is a fact from outside the course. In its colony of Libya, Fascist Italy locked up the population of Cyrenaica "
        "in concentration camps, from nineteen thirty to nineteen thirty-three. "
        "So write it precisely: no camps for opponents in Italy itself.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[14]),
        "it": dict(type="liste", titre="Italy: terror made legal", items=[
            "1924 · Matteotti murdered → the totalitarian state", "1926 · State Defence Law: death penalty, Special Court",
            "1927 · the OVRA", "Far fewer death sentences · opponents sent to the confino"], x=150, y=130, w=980),
        "form": dict(type="mot", t="Legalised, not industrialised", g="“Less oppressive terror?” · the course's question mark", y=250, taille=78),
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
        "{-g9}{en}Once an enemy is chosen, violence against it seems justified to the rest of the population. "
        "{en.1}In the Soviet Union, the enemy was the kulaks, as in Worksheet two. "
        "{en.2}In Germany: Jews, Roma, prostitutes, homosexuals, and disabled people. Four hundred thousand people were forcibly sterilised. "
        "{en.3}In Italy: the enemies of the State, tried by the Special Court.",
        "{-en}{cons}In Germany, all this rested on a conspiracy theory. The nation was supposedly undermined by {!enemies from within}enemies from within. "
        "{cons.1}You know where that comes from. It is the stab-in-the-back myth of nineteen eighteen, from episode two.",
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
        "{ex1}Your turn. Here is the task of Worksheet four. {!find the similarities}Find the similarities in the use of violence "
        "by the three regimes. Aim for five or six. For each one, give an example from each regime.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{sim}Here are the six similarities. "
        "{sim.1}One. A political police above the law: the OVRA, the Gestapo and the S.S., the NKVD. "
        "{sim.2}Two. Terror wearing the mask of legality. Think of the State Defence Law of nineteen twenty-six, "
        "the Nuremberg laws of nineteen thirty-five, and the Moscow trials. "
        "{sim.3}Three. Enemies designated by category, not by what they did: enemies of the State, Jews, kulaks. Violence becomes preventive. "
        "{sim.4}Four. The camp as a system, and forced labour as a resource: Dachau, the Gulag. "
        "{sim.5}Five. Terror striking the regime's own men: the Night of the Long Knives, and Yezhov. "
        "{sim.6}And six. The same function, which is to govern. Remove rivals. Destroy every autonomous organisation. "
        "Produce the fear that makes people docile.",
        "{-sim}{dif}But a good answer never stops at similarities. "
        "{dif.1}First, the scale. Italy is by far the least lethal. "
        "{dif.2}Then, the criterion. It is social in the Soviet Union, biological in Germany, and political in Italy. "
        "{dif.3}And finally, Italy left counter-powers standing: the monarchy, and the Church, with the Concordat of nineteen twenty-nine.",
        "{-dif}{ccl}The course's essay concludes: the three terrors were "
        "{!identical in method, unequal in scale}identical in method and purpose. But they were unequal in scale, "
        "and in the principle that designates the victim.",
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
        "{tb}Let's put everything together in the totalitarianism table of the course, filled in as far as the course has gone. "
        "It has five blocks. {tb.1}Seizure of power. {tb.2}Ideology. {tb.3}Dictatorship. {tb.4}State terrorism. {tb.5}A controlled society. "
        "It is a synthesis of parts one and two. If you can fill it in from memory, you are ready.",
        "{-tb}{t1}Block one: the seizure of power. First, the date. {t1.1}Italy: October nineteen twenty-two. "
        "After the March on Rome, Mussolini is appointed prime minister. The state becomes totalitarian from nineteen twenty-five. "
        "{t1.2}Germany: the thirtieth of January, nineteen thirty-three. Hitler becomes chancellor. He gets full powers in March. "
        "{t1.3}The Soviet Union: it starts in nineteen twenty-four, with the death of Lenin. "
        "Stalin's power is consolidated by nineteen twenty-eight or twenty-nine.",
        "{-t1}{t2}Next, the causes. {t2.1}In Italy: the mutilated victory, the Biennio Rosso, the fear of communism, and a weak parliament. "
        "{t2.2}In Germany: the defeat of nineteen eighteen, the Versailles Diktat, and the stab-in-the-back myth. "
        "Then the crisis of nineteen twenty-nine, with about six million unemployed. "
        "{t2.3}In the Soviet Union: the Tsarist state collapses in the war. Then come the revolutions of nineteen seventeen, "
        "and a civil war that lasts until nineteen twenty-two.",
        "{-t2}{t3}Then, the process. {t3.1}Italy: squadristi violence first, and then a legal appointment by the king. "
        "{t3.2}Germany: elections, with thirty-seven per cent of the vote in July nineteen thirty-two. "
        "Then the appointment by Hindenburg, the Reichstag fire decree, and the Enabling Act. "
        "{t3.3}The Soviet Union: a struggle inside the party, and Trotsky expelled in nineteen twenty-nine. No electoral path at all.",
        "{-t3}{t4}Block two: ideology. {t4.1}Here, the similarities are the same in all three. One single truth. "
        "The rejection of liberal democracy. Total control. A New Man. And violence held to be legitimate. "
        "These shared traits are exactly what the word totalitarianism means. "
        "{t4.2}Then, the specificities. Italy: the nation and the absolute State, and no racism before nineteen thirty-eight. "
        "{t4.3}Germany: race struggle, antisemitism, and Lebensraum. "
        "{t4.4}The Soviet Union: class struggle, the abolition of private property, and socialism in one country.",
    ], vis={
        "tb": dict(type="liste", titre="The course table · five blocks", items=[
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
        "{t5}Block three: the dictatorship. {t5.1}The cult of personality. Il Duce. Der Führer. "
        "And the little father of the peoples, with a city renamed Stalingrad in nineteen twenty-five. "
        "{t5.2}The single party. In Italy, the National Fascist Party. In Germany, the Nazi Party. In the Soviet Union, the Communist Party. "
        "{t5.3}The symbols: the Roman fasces, the swastika, the hammer and sickle. "
        "{t5.4}And the slogans. Il Duce ha sempre ragione: the Duce is always right. Heil Hitler. "
        "And: Thank you, Comrade Stalin, for our happy childhood.",
        "{-t5}{t6}Next, the supports. These regimes did not rest on terror alone. "
        "{t6.1}In Italy: landowners, shopkeepers, veterans, the monarchy, and the Church. "
        "{t6.2}In Germany: the middle classes, the conservative elites, the industrialists, and the army. "
        "{t6.3}In the Soviet Union: the party apparatus, the bureaucracy, and part of the working class.",
        "{-t6}{t7}Block four, state terrorism: today's lesson. {t7.1}The political police. "
        "In Italy, the OVRA and the Special Court. In Germany, the Gestapo and the S.S., both under Himmler. "
        "In the Soviet Union, the OGPU, then the NKVD, and the Gulag. "
        "{t7.2}The opponents. In Italy: socialists and communists, like Matteotti. And Jews, from nineteen thirty-eight. "
        "{t7.3}In Germany: communists, socialists, Jews, Roma, homosexuals, the disabled, and Jehovah's Witnesses. "
        "{t7.4}In the Soviet Union: kulaks, class enemies, old Bolsheviks, and army officers.",
        "{-t7}{t8}Block five: a controlled society, from episode four. {t8.1}Youth: the Balilla, the Hitler Youth from ten to eighteen, and the Komsomol. "
        "{t8.2}Thought and culture. In Italy, the opposition press is suppressed. "
        "In Germany, racial instruction is compulsory from nineteen thirty-three. "
        "In the Soviet Union, socialist realism, and retouched photographs. "
        "{t8.3}The economy. Corporatism and autarky in Italy. Rearmament and the Four-Year Plan in Germany. "
        "Five-year plans and collectivisation in the Soviet Union. "
        "{t8.4}And the administration. In all three, the party doubles or controls the state.",
        "{-t8}{rest}Two blocks of the table are still empty: international issues, and the road to war. "
        "They belong to part three, in the next two episodes.",
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
            "Communists, socialists, Jews, Roma, homosexuals, the disabled, Jehovah's Witnesses",
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
        "{ex2}Now, an essay. {!How far do you agree}“Terror was the main tool of totalitarian regimes.” How far do you agree?",
        "{-ex2}{met}Remember the method. {met.1}How far asks you to weigh. Never entirely. Never not at all. "
        "{met.2}Define the key word in the introduction. {met.3}Write three parts: the case for, the case against, and the nuance. "
        "{met.4}And give a clear judgement, both in the introduction and in the conclusion.",
        "{-met}{pa2}",
        ("P", 2.0),
        "{-pa2}{plan2}Here is a model plan. {plan2.1}Part one. Yes, terror was a central tool, and a permanent one. "
        "Think of the political police above the law. The Moscow trials, and the Great Purge with its six hundred and eighty thousand executions. "
        "The camps, from Dachau to the Gulag. And terror striking even the regime's own men. "
        "{plan2.2}Part two. But terror never worked alone. Totalitarianism means coercion through terror and propaganda together. "
        "The cult of the leader, the rallies, the youth organisations, the New Man. "
        "And Hannah Arendt warns us: Hitler and Stalin needed the confidence of the masses. "
        "{plan2.3}Part three. Terror was unequal. Italy legalised repression rather than industrialising it. "
        "And Mussolini had to accept the king and the Church.",
        "{-plan2}{intro}And here is a model introduction. "
        "{intro.1}Totalitarianism is a regime that seeks total control of society, through coercion, in order to transform man according to an ideology. "
        "In Fascist Italy, Nazi Germany and Stalin's Soviet Union, terror was everywhere. Police, trials, camps, purges. "
        "{intro.2}But was it their main tool? Or one tool among others? "
        "{intro.3}This essay argues that terror was an essential tool for all three, but never the only one. "
        "It worked together with propaganda and popular support. And its scale varied greatly from one regime to another.",
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
            "Yes: a central, permanent tool · police above the law, Moscow trials, Great Purge (680,000 executions), camps, the regime's own men",
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
        "{carte}Let's sum up. {carte.1}Terror is a method of government. It is permanent, organised and planned, so that each person censors himself. "
        "{carte.2}Its instruments: a political police above the law, show trials, and the camp as a permanent institution, from Dachau to the Gulag. "
        "{carte.3}Its victims: enemies chosen by category. The kulaks, the Jews, the disabled. And even the regime's own men. "
        "{carte.4}Its limits: Italy legalised its repression rather than industrialising it. And nowhere did terror rule alone.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: hegemonic ambitions. War as a value: Abyssinia, Lebensraum, and Japan.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="MASS TERROR", branches=[
            dict(t="A method", items=["permanent, planned", "Arendt: “from within”", "self-censorship"]),
            dict(t="Instruments", items=["OVRA · Gestapo, S.S. · NKVD", "Moscow trials · Great Purge", "Dachau · the Gulag"]),
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
    "Content: the DNL History course (chapter H2 · Part II.3, Worksheet 4, the totalitarianism table, Arendt in the introduction) as written on the site; Worksheet 4 answers suggested by the site; outside the course: Fascist camps in Libya (Cyrenaica, 1930–33) and Beria's dates at the head of the NKVD (1938–45); animated map of chapter 2 (site).",
    "Photographs (via Wikimedia Commons): Hannah Arendt in 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0); the defendants of the second Moscow trial, January 1937 (unknown photographer, public domain); Gulag prisoners digging the White Sea-Baltic Canal, 1932 (unknown photographer, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
