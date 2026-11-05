"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 3 : « Three regimes, three ideologies »
(partie I.3 du cours, « Specific aspects of each regime », quinze idées).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_3 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 7 putsch manqué, Mein Kampf · 8 fascisme, la dictature rendue légale · 12 stalinisme, plan et collectivisation ·
       14 une terreur moins oppressive ? puis le tournant raciste · 15 les koulaks · 19 l'Holodomor ·
       23 nazisme, la lutte des races
Contenu : CHAPTERS.H2 du site (dnl/index.html), section I.3 (15 idées : fascisme 1 à 7, stalinisme 8 à 12, nazisme 13
à 15), idée 4 de l'introduction (définition de l'idéologie), schémas h2collect (Worksheet 2 : le processus de
collectivisation, foyers collectivisés 7 % → 15 % → 57 % → 90 %, 1928-1936), h2ideo (trois idéologies comparées),
h2grid (bloc « Ideology » du tableau de synthèse de M. Ros) et h2check (points à confirmer : Matteotti 1924 et non 1925,
collectivisation « dès 1928 », T4 70 000 en 1939-1941, exemples pris hors du cours). Dits « outside the course » :
le bilan d'environ quatre millions de morts de l'Holodomor, la relégation à Lipari, la déportation des koulaks vers la
Sibérie et le Kazakhstan (carte), le « grand tournant » de 1929.
Plan : chronologie sur la carte (1923-1939), puis le cours régime par régime (fascisme, stalinisme, nazisme), puis la
comparaison (h2ideo, h2grid, h2check) et une pause « Your turn » (paragraphe d'essay comparant nation / race / classe).
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-3"
NOTION = "Totalitarian Regimes"
NUM = 3
TITRE = "Three regimes, three ideologies"
SUIVANT = "Episode 4 · The leader, the party and the New Man"
PRONONCIATION = {"Matteotti": "Mat-teh-ot-tee", "Duce": "Doo-cheh", "Gentile": "Jen-tee-leh", "Lipari": "Lee-pa-ree",
                 "fascistissime": "fa-shee-stee-see-meh", "Mostra": "Moss-tra", "Rivoluzione": "Ree-vo-loo-tsyo-neh",
                 "Fascista": "Fa-shee-sta", "Difesa": "Dee-feh-za", "Razza": "Rat-tsa", "Benigni": "Ben-ee-nyee",
                 "kulak": "koo-lak", "kulaks": "koo-laks", "kolkhoz": "kol-hoz", "kolkhozes": "kol-ho-zes",
                 "sovkhozes": "sov-ho-zes", "Holodomor": "Ho-lo-do-mor", "OGPU": "O G P U", "Molotov": "Mollo-toff",
                 "Kaganovich": "Ka-ga-no-vich", "Ordzhonikidze": "Or-jo-nee-keed-zeh", "Feigin": "Fay-gin",
                 "Werth": "Vairt", "Giftpilz": "Gift-pilts", "Bauer": "Bow-er", "Mein Kampf": "Mine Kampf",
                 "Reichstag": "Rikes-tahg", "Lebensraum": "Lay-bens-rowm", "Arendt": "Ah-rent"}

# Worksheet 2, source 2 : part des foyers paysans collectivisés (h2collect)
COLLECT = [(1928, 7), (1929, 15), (1930, 57), (1936, 90)]


def barres_collect():
    """Barres verticales (droites épaisses, comme dans h3_4) : l'année sous l'axe, la valeur au-dessus de la barre."""
    el = [dict(type="texte", x=i, y=-8, t=str(an), c="iv") for i, (an, _) in enumerate(COLLECT, start=1)]
    for i, (an, v) in enumerate(COLLECT, start=1):
        el.append(dict(type="droite", pts=[[i, 4.5], [i, max(5, v - 4.5)]], c="sa", ep=46, dur=1.0,
                       lbl=f"{v}%", lp=[i, v + 7]))
    el.append(dict(type="texte", x=2.5, y=78, t="1929–30: coercion, not consent", c="ca"))
    return el


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Three regimes. The same single party, the same leader, the same police, the same propaganda.",
        "{-q1}{q2}And yet they did not want the same thing. Mussolini dreamed of the nation, Hitler of the race, Stalin of the class.",
        "{-q2}{q3}So what made each of them specific? And why does the difference matter so much? Because the goal decides "
        "who the enemy is… and the enemy decides who the victims are.",
        "{-q3}{-g0}{plan}The plan. {plan.1}The story on the map. {plan.2}Then Fascism: the nation and the State. "
        "{plan.3}Then Stalinism: the class, collectivisation, and the famine. {plan.4}Then Nazism: the race. "
        "{plan.5}Then the comparison, with Monsieur Ros's synthesis grid. {plan.6}And your turn: an essay paragraph.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[0]),
        "q1": dict(type="question", t="One method of power…", bande=True),
        "q2": dict(type="question", t="… three different goals: nation, race, class.", bande=True),
        "q3": dict(type="question", t="The goal decides the enemy.", bande=True),
        "plan": dict(type="liste", titre="Episode 3 · Part I.3 of the course", items=[
            "The story on the map: 1923 – 1939", "Fascism: the nation and the absolute State",
            "Stalinism: class struggle, collectivisation, the Holodomor", "Nazism: race struggle",
            "The comparison: M. Ros's synthesis grid", "Your turn: an essay paragraph"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 3", t="Three regimes, three ideologies",
                      sous="Fascism · Stalinism · Nazism · Part I.3 of the course"),
    }),

    # ================================================================ la carte (1) : 1923-1938
    dict(id="carte1", chap="On the map: Rome and Moscow", fond="nuit", humeur="tension",
         retenir="1924–25: Matteotti murdered, the “fascistissime” laws · 1928: the first Five-Year Plan · 1929: the Lateran Accords · 1938: Fascist Italy turns racist.",
         beats=[
        "{g1}Let's follow the story on the map first. {g1.1}November 1923, in Munich: Hitler's coup fails. "
        "In prison, he writes Mein Kampf: his racist views are already on paper, ten years before power.",
        "{g1.2}Meanwhile, in Rome, Mussolini has been in power since 1922. In 1924, the socialist deputy Matteotti is kidnapped and murdered. "
        "In January 1925, Mussolini claims responsibility, and the fascistissime laws turn Italy into a totalitarian State.",
        "{g1.3}Now the Soviet Union, where Stalin rules from 1924. In 1928, he launches the first Five-Year Plan: "
        "industry, and the forced collectivisation of the countryside. Seven per cent of peasant households are collectivised in 1928. "
        "Ninety per cent in 1936.",
        "{g1.4}Back to Italy. In 1929, Mussolini signs an agreement with the Pope: the Lateran Accords. "
        "And Fascism is not racist… until 1938, when Mussolini allies with Hitler.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[7, 8, 12, 14]),
    }),

    # ================================================================ la carte (2) : 1929-1939
    dict(id="carte2", chap="On the map: the countryside and the race", fond="nuit", humeur="tension",
         retenir="1929–32: the kulaks, class enemies · 1932–33: the Holodomor in Ukraine · 1933–39: Nazi race struggle, racial instruction (1933), T4 (1939).",
         beats=[
        "{g2}{g2.1}In the Soviet countryside, from 1929, any peasant who resists collectivisation is labelled a kulak: a class enemy. "
        "Land and animals are confiscated, and many are deported.",
        "{g2.2}In 1932 and 1933, in Ukraine, the grain is requisitioned whatever the harvest. Villages that resist are cut off from all supplies. "
        "The result is a man-made famine: the Holodomor.",
        "{g2.3}And in Germany, from 1933, the Nazis turn their race struggle into laws and school lessons, "
        "and in 1939, into the murder of disabled Germans.",
        "{-g2}{fr}So here are the dates of this episode. {fr.1}1924, {fr.2}1925, {fr.3}1928, {fr.4}1929, "
        "{fr.5}1932, {fr.6}1933, {fr.7}1938, {fr.8}and 1939. Pause the video to copy them.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[15, 19, 23]),
        "fr": dict(type="frise", items=[
            dict(nom="Matteotti", d=1924, q="murdered"), dict(nom="Fascistissime laws", d=1925, q="Mein Kampf"),
            dict(nom="Five-Year Plan", d=1928, q="collectivisation"), dict(nom="Lateran Accords", d=1929, q="the Church"),
            dict(nom="Doctrine of Fascism", d=1932, q="Holodomor 1932–33"), dict(nom="Racial instruction", d=1933, q="German schools"),
            dict(nom="La Difesa della Razza", d=1938, q="Italy turns racist"), dict(nom="T4", d=1939, q="disabled Germans")]),
    }),

    # ================================================================ trois idéologies
    dict(id="ideologie", chap="What is an ideology?", fond="aube", humeur="calme",
         retenir="An ideology: a set of beliefs that sets a supreme goal. Fascism → the nation · Nazism → the race · Stalinism → the class.",
         beats=[
        "{def1}Before the course, one word to master: {!ideology}ideology. Remember the definition from episode one: "
        "a set of beliefs that sets a supreme goal to be achieved. {def1.1}And a supreme goal justifies any means.",
        "{-def1}{trois}Now, the three supreme goals. {trois.1}For Fascism: the nation, embodied in an absolute State. "
        "{trois.2}For Nazism: the race. {trois.3}For Stalinism: the class. "
        "Keep these three words in mind for the whole episode: nation, race, class.",
    ], vis={
        "def1": dict(type="def", cles=["beliefs", "supreme"], terme="Ideology",
                     t="A set of beliefs that sets a supreme goal to be achieved.",
                     etape="A supreme goal justifies any means", x=170, y=200, w=940),
        "trois": dict(type="cartes", petit=True, items=[
            dict(t="Nation", q="Fascism · the absolute State"), dict(t="Race", q="Nazism · a pure race"),
            dict(t="Class", q="Stalinism · a classless society")]),
    }),

    # ================================================================ fascisme, idée 1
    dict(id="fas1", chap="Fascism · a “new revolution”", fond="nuit", humeur="lumiere",
         retenir="Fascism: a “new revolution”, neither liberal nor socialist, to transform civilisation and recreate the glory of Rome. The Fascist calendar: 1922 = year I.",
         beats=[
        "{def2}Fascism first. Idea one: Fascism presented itself as a {!new revolution}new revolution, neither liberal nor socialist. "
        "{def2.1}Its aim: to transform Italian civilisation, and to recreate the greatness of ancient Rome. "
        "Mussolini wanted a disciplined, warlike people, united behind the State.",
        "{-def2}{an11}And the ambition was total: history itself was to start again with Fascism. "
        "The proof is on Monsieur Ros's slide: the poster of the Exhibition of the Fascist Revolution, the Mostra della Rivoluzione Fascista, "
        "Rome, 1932. It is dated year eleven. {an11.1}Because the Fascist calendar starts in 1922, the year Mussolini seized power. "
        "Year one. A new era.",
    ], vis={
        "def2": dict(type="def", cles=["revolution", "Rome"], terme="Fascism · a “new revolution”",
                     t="Neither liberal nor socialist: transform Italian civilisation and recreate the glory of ancient Rome.",
                     etape="A disciplined, warlike people, united behind the State", x=170, y=200, w=940),
        "an11": dict(type="cols", g="The poster", gq="Mostra della Rivoluzione Fascista, Rome, 1932: “year XI”",
                     d="The calendar", dq="1922, the seizure of power = year I", vs="=", repere="History starts again with Fascism"),
    }),

    # ================================================================ fascisme, idée 2
    dict(id="fas2", chap="Fascism · from murder to legal dictatorship", fond="guerre", humeur="tension",
         retenir="Matteotti kidnapped and killed, 10 June 1924 · 3 Jan. 1925: Mussolini claims responsibility · 1925: “fascistissime” laws · the king stays, Parliament no longer counts.",
         beats=[
        "{g3}{g3.1}Idea two. Once in power, Mussolini still had to face the left. {mat}{mat.1}Giacomo Matteotti, a socialist deputy, "
        "denounced electoral fraud and violence openly in Parliament. On the tenth of June 1924, he was kidnapped. His body was found later.",
        "{mat.2}On the third of January 1925, before the Chamber, Mussolini publicly claimed responsibility, and called Matteotti an enemy of peace. "
        "{mat.3}Then came the fascistissime laws, the most fascist laws, which turned Italy into a totalitarian State.",
        "{mat.4}So this is the end of the parliamentary monarchy. The king remained, but Parliament no longer counted. "
        "{!Violence first, then the law}Violence first, then the law.",
        "{-mat}{-g3}{att1}One point to watch. Monsieur Ros's slide dates the murder 1925. {att1.1}Matteotti was in fact kidnapped and killed in June 1924; "
        "1925 is the year the murder bore fruit. In your copy, write 1924, or 1924 to 1925.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[8]),
        "mat": dict(type="liste", titre="The Matteotti affair", petit=True, bande=True, x=60, y=120, w=620, items=[
            "10 June 1924: Matteotti, socialist deputy, kidnapped and killed", "3 Jan. 1925: Mussolini claims responsibility",
            "1925: the “fascistissime” laws, a totalitarian State", "The king remains; Parliament no longer counts"]),
        "att1": dict(type="note", terme="Watch out · a date", cles=["1924"],
                     t="The slide dates the murder 1925: Matteotti was killed in June 1924.",
                     etape="1925: the claim of responsibility and the fascistissime laws · write 1924, or 1924–1925", x=170, y=200, w=940),
    }),

    # ================================================================ fascisme, idées 3, 4 et 5
    dict(id="doctrine", chap="Fascism · the Doctrine of 1932", fond="aube", humeur="calme",
         retenir="Doctrine of Fascism (Mussolini and Gentile, 1932): “everything is in the State” · nations, not classes · against parliamentarism, liberalism, Marxism and human rights · nationalist, militaristic.",
         beats=[
        "{doc}Ideas three, four and five come from one text, studied on Monsieur Ros's slide: the {!Doctrine of Fascism}Doctrine of Fascism, "
        "written in 1932 by Mussolini and the philosopher Giovanni Gentile. {doc.1}Idea three: the word totalitarian. "
        "Today it is an accusation. But the fascists used it with pride, for a State that swallows everything.{-doc}",
        ("C", "everything is in the State … in this sense Fascism is totalitarian", "c_doc1"),
        "{-c_doc1}{tot}For them, totalitarian meant complete, united, strong: the opposite of a divided liberal society. "
        "{tot.1}The word took on its accusing meaning only after the war, when historians and philosophers such as Hannah Arendt "
        "applied it to Nazism and Stalinism.",
        "{-tot}{cl}Idea four: Fascism divides humanity into nations, not classes. {cl.g}Marxism says: society is divided into classes in struggle. {cl.d}Fascism says the opposite: what divides humanity is nations, and inside the nation, all classes must be united "
        "under the State. So the Doctrine attacks Socialism, which{-cl}",
        ("C", "confines the movement of history within the class struggle", "c_doc2"),
        "{-c_doc2}{own}Class struggle is banned, not encouraged. {own.1}That is why Fascism attracted owners frightened by socialism: "
        "it promised national unity instead of revolution.",
        "{-own}{contre}Idea five. For Monsieur Ros, Fascism is the first totalitarianism, and it is defined by what it rejects. "
        "{contre.1}It rejects parliamentarism, the rule of elected assemblies. {contre.2}It does not believe in human rights. "
        "{contre.3}It is against liberalism and against Marxism alike. {contre.4}And it is nationalist and militaristic.",
        "{-contre}{ind}Where liberalism starts from the individual and his rights, Fascism starts from the State, "
        "which alone gives the individual his value. In the words of the Doctrine:{-ind}",
        ("C", "Liberalism denied the State in the interests of the particular individual", "c_doc3"),
            ], vis={
        "doc": dict(type="def", cles=["Mussolini", "Gentile"], terme="The Doctrine of Fascism · 1932",
                    t="Written by Mussolini and the philosopher Giovanni Gentile.",
                    etape="Idea 3: “totalitarian”, a word the fascists used with pride", x=170, y=200, w=940),
        "c_doc1": dict(type="cit", a="Mussolini and Gentile", o="The Doctrine of Fascism, 1932 (M. Ros's slide)", x=200, y=200, w=880),
        "tot": dict(type="cols", g="For the fascists", gq="“totalitarian” = complete, united, strong",
                    d="After the war", dq="an accusation: Arendt, on Nazism and Stalinism", vs="→"),
        "cl": dict(type="cols", g="Marxism", gq="society divided into classes, locked in struggle", d="Fascism",
                   dq="humanity divided into nations; all classes united under the State", vs="≠", repere="Idea 4: nations, not classes"),
        "c_doc2": dict(type="cit", a="Mussolini and Gentile", o="The Doctrine of Fascism, 1932, on Socialism", x=200, y=220, w=880),
        "own": dict(type="note", terme="Why owners liked it", cles=["owners", "unity"],
                    t="Class struggle banned: national unity instead of revolution.",
                    etape="Owners frightened by socialism rallied to Fascism", x=170, y=200, w=940),
        "contre": dict(type="liste", titre="Idea 5 · the first totalitarianism is against…", cles=["parliamentarism", "rights", "liberalism", "nationalist"], items=[
            "Parliamentarism: the rule of elected assemblies", "Human rights: it does not believe they exist",
            "Liberalism and Marxism alike", "… and it is nationalist and militaristic"], x=170, y=140, w=940),
        "ind": dict(type="cols", g="Liberalism", gq="starts from the individual and his rights", d="Fascism",
                    dq="starts from the State, which alone gives the individual his value", vs="≠"),
        "c_doc3": dict(type="cit", a="Mussolini and Gentile", o="The Doctrine of Fascism, 1932 (M. Ros's slide)", x=200, y=220, w=880),
    }),

    # ================================================================ fascisme, idées 6 et 7
    dict(id="fas67", chap="Fascism · a less oppressive terror?", fond="nuit", humeur="mystere",
         retenir="Less oppressive: opponents silenced, not all killed · a counter-power: the Church (Lateran Accords, 1929), and the king · not racist before 1938: La Difesa della Razza (Aug. 1938), anti-Semitic laws.",
         beats=[
        "{g4}{g4.1}Idea six. Monsieur Ros asks a question, with a question mark: {!a less oppressive terror}a less oppressive terror? "
        "{lim}{lim.1}Yes, in one sense: Fascism wanted to silence its opponents, not to kill them all. "
        "Most were sent into internal exile on islands, such as Lipari: an example from outside Monsieur Ros's notes.",
        "{lim.2}And its power was incomplete. Mussolini did not have enough power to take control of the Church, so he came to terms with the Pope: "
        "a concordat, the Lateran Accords, in 1929. {lim.3}And the king remained head of the State.",
        "{-lim}{-g4}{amb}Remember this sentence for an essay: {amb.1}a totalitarian ambition does not always mean totalitarian control.",
        "{-amb}{rac}Idea seven. Unlike Nazism, Italian Fascism was not founded on racism, and anti-Semitism was not part of its early programme. "
        "{rac.1}The turn came in 1938. Allied with Hitler, Mussolini introduced anti-Semitic laws, and the nation became officially racist. "
        "{rac.2}{rac.3}The example: La Difesa della Razza, the Defence of the Race, a magazine published from August 1938, which set a Roman profile "
        "against Jewish and African faces. Specialists of race came into schools to teach the superiority of the fascist race.",
        "{-rac}{nuance}So racism in Italy was a late turn, tied to the German alliance, rather than the core of the ideology. "
        "{nuance.1}Which makes it no less real for its victims. Roberto Benigni's film Life is Beautiful, of 1997, mocks this racism.",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[14]),
        "lim": dict(type="liste", titre="Idea 6 · less oppressive, less complete", petit=True, bande=True, x=60, y=120, w=620, items=[
            "Opponents silenced rather than all killed: exile on islands such as Lipari (outside the notes)",
            "A counter-power: the Church · Lateran Accords, 1929", "The king remains head of the State"]),
        "amb": dict(type="mot", t="Ambition ≠ control", g="a totalitarian ambition does not always mean totalitarian control", y=250, taille=96),
        "rac": dict(type="liste", titre="Idea 7 · the racist turn of 1938", cles=["1938", "anti-Semitic", "Difesa"], items=[
            "Before 1938: not founded on racism; no anti-Semitism in the early programme",
            "1938: allied with Hitler, anti-Semitic laws; officially racist",
            "La Difesa della Razza (Aug. 1938); “race” specialists in schools"], x=150, y=140, w=980),
        "nuance": dict(type="note", terme="The nuance", cles=["late", "victims"],
                       t="A late turn tied to the German alliance, not the core of the ideology.",
                       etape="No less real for its victims · mocked in Benigni's Life is Beautiful (1997)", x=170, y=200, w=940),
    }),

    # ================================================================ stalinisme, idée 8
    dict(id="sta8", chap="Stalinism · class struggle as the engine", fond="nuit", humeur="tension",
         retenir="Marxism: history = class struggle, ending in a society without classes, property or profit. The Five-Year Plan (1928): an industrial USSR, independent of world capitalism, and the last capitalist elements ousted.",
         beats=[
        "{g5}{g5.1}Now Stalinism. Idea eight. Soviet ideology is Marxist: history is a {!struggle between classes}struggle between classes, "
        "and it ends with a society without classes, without private property, and without profit.",
        "{-g5}{plan5}Stalin's Five-Year Plan, launched in 1928, turned this into a programme with two goals. "
        "{plan5.g}First, the Soviet Union had to become an industrial and powerful country, independent of world capitalism. "
        "{plan5.d}Second, it had to oust the last capitalist elements. Above all in the countryside, where most people still farmed their own land.",
        "{-plan5}The example comes from Worksheet two, source one: Stalin's speech to the Central Committee, the seventh of January 1933. "
        "The Plan had to transform a country with",
        ("C", "backward, and in part medieval, technology", "c_st1"),
        "{-c_st1}into a country",
        ("C", "fully self-reliant and independent of the caprices of world capitalism", "c_st2"),
        "{-c_st2}Notice the date: January 1933. The very months when the famine was killing peasants in Ukraine.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[12]),
        "plan5": dict(type="cols", g="Goal 1 · industry", gq="an industrial, powerful USSR, independent of world capitalism",
                      d="Goal 2 · the countryside", dq="oust the last capitalist elements: the peasants' own farms",
                      vs="+", repere="The first Five-Year Plan, 1928"),
        "c_st1": dict(type="cit", a="Joseph Stalin", o="speech to the Central Committee, 7 January 1933 (Worksheet 2, source 1)", x=200, y=210, w=880),
        "c_st2": dict(type="cit", a="Joseph Stalin", o="speech to the Central Committee, 7 January 1933 (Worksheet 2, source 1)", x=200, y=210, w=880),
    }),

    # ================================================================ stalinisme, idée 9
    dict(id="sta9", chap="Stalinism · forced collectivisation", fond="nuit", humeur="tension",
         retenir="Collectivisation: small scattered farms merged into kolkhozes (collective) and sovkhozes (state). Households collectivised: 7% (1928) · 15% (1929) · 57% (1930) · 90% (1936).",
         beats=[
        "{def3}Idea nine: {!collectivisation}collectivisation. It meant merging small and scattered farms into large collective ones. "
        "{def3.1}Independent households were suppressed, and the peasants were grouped in kolkhozes, collective farms, or sovkhozes, "
        "state-owned farms. The aim of the Plan: total collectivisation in five years, and no possible return to capitalism in the countryside.",
        "{-def3}{poster}The propaganda was cheerful. A Soviet poster of 1930, on Monsieur Ros's slide, calls: "
        "{!Come with us to the kolkhoz, comrades!}Come with us to the kolkhoz, comrades!",
        "{-poster}{gc}But look at the figures of Worksheet two, source two: the share of peasant households collectivised. "
        "{gc.1}{gc.2}{gc.3}{gc.4}{gc.5}In 1928: seven per cent. {gc.6}In 1929: fifteen per cent. "
        "{gc.7}In 1930: fifty-seven per cent. {gc.8}And in 1936: ninety per cent.",
        "{gc.9}Look at the leap between 1929 and 1930: from fifteen to fifty-seven per cent in a year. "
        "That is the leap of coercion, not of consent. It is also the moment when peasants slaughtered their livestock rather than hand it over.",
        "{-gc}{att2}{att2.1}A detail to check: the Worksheet dates forced collectivisation from 1928; many historians place the mass campaign "
        "in late 1929, the Great Turn: outside the course. The course date is kept.",
    ], vis={
        "def3": dict(type="def", cles=["merging", "kolkhozes", "sovkhozes"], terme="Collectivisation",
                     t="Small, scattered farms merged into large collective ones; independent households suppressed.",
                     etape="Kolkhozes (collective farms) · sovkhozes (state-owned farms) · total collectivisation in 5 years", x=170, y=200, w=940),
        "poster": dict(type="mot", t="“Come with us to the kolkhoz, comrades!”", g="Soviet poster, 1930 (M. Ros's slide)", y=260, taille=64),
        "gc": dict(type="graphe", titre="Peasant households collectivised (Worksheet 2, source 2)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[0.4, 4.6], y=[0, 105], gx=[], gy=[25, 50, 75, 100], lx="", ly="%"), el=barres_collect()),
        "att2": dict(type="note", terme="To confirm with M. Ros", cles=["1928", "1929"],
                     t="Worksheet 2: forced collectivisation from 1928. Many historians: the mass campaign from late 1929.",
                     etape="The “Great Turn” (outside the course) · the course date is kept", x=170, y=200, w=940),
    }),

    # ================================================================ stalinisme, idée 10
    dict(id="sta10", chap="Stalinism · the kulaks", fond="nuit", humeur="tension",
         retenir="Kulak: on paper a peasant owning more than 8 acres; in practice any peasant who refused collectivisation. Persecuted as a class: land and animals confiscated, many deported. “Kulak sabotage”.",
         beats=[
        "{g6}{g6.1}Idea ten: the {!kulak}kulak label. {kul}{kul.1}On paper, a kulak was a peasant who owned more than eight acres of land. "
        "{kul.2}In practice, the label was given to any peasant who refused collectivisation, accused of being too selfish to share.",
        "{kul.3}So the kulaks were persecuted {!as a class}as a class: their land and animals were confiscated, and many were deported. "
        "The arrows on the map show deportations to Siberia and Kazakhstan: that detail is outside the course. "
        "{kul.4}And their resistance was described by the regime as kulak sabotage, to be broken.",
        "{-kul}{-g6}{ex10}Two examples. {ex10.g}Monsieur Ros's slide: in 1929, farmers of the kolkhozes protest against the kulaks, "
        "under a banner calling for their liquidation as a class. {ex10.d}And in Ukraine, in 1932, according to the historian Nicolas Werth, "
        "peasants who hid grain were accused of kulak sabotage, whatever the size of their land.",
        "{-ex10}{lec10}So a kulak is not a size of farm. {lec10.1}It is an enemy defined by the ideology: the class enemy.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[15]),
        "kul": dict(type="liste", titre="The kulak label", petit=True, bande=True, x=60, y=120, w=620, items=[
            "On paper: a peasant owning more than 8 acres", "In practice: any peasant refusing collectivisation",
            "Persecuted as a class: land, animals confiscated; deported", "Resistance branded “kulak sabotage”"]),
        "ex10": dict(type="cols", g="1929 · M. Ros's slide", gq="kolkhoz farmers under a banner: liquidate the kulaks as a class",
                     d="1932 · Ukraine (Werth)", dq="peasants who hid grain accused of “kulak sabotage”", vs="+"),
        "lec10": dict(type="note", terme="For the essay", cles=["enemy", "class"],
                      t="A kulak is not a size of farm: an enemy defined by the ideology.",
                      etape="Stalinism's enemy within: the class enemy", x=170, y=200, w=940),
    }),

    # ================================================================ stalinisme, idée 11
    dict(id="sta11", chap="Stalinism · the Holodomor", fond="guerre", humeur="tension",
         retenir="Grain requisitioned whatever the harvest · OGPU brigades to “take the grain” · Molotov and Kaganovich: “rebellious” villages cut off from all supplies · Sept. 1932: 32% of the target, 25 Oct.: 22% · the Holodomor, 1932–33.",
         beats=[
        "{g7}{g7.1}Idea eleven: the result. Ukraine, 1932. The grain is {!requisitioned}requisitioned, whatever the harvest. "
        "{hol}It happens in steps. {hol.1}The peasants resist: they hide grain in pits and secret granaries, "
        "or send children and the elderly to cut stalks at night. "
        "{hol.2}The regime answers with brigades, backed by the political police, the OGPU, sent to take the grain.",
        "{hol.3}Molotov and Kaganovich, sent by the Politburo, first halt deliveries of manufactured goods to the districts that have not fulfilled the plan. "
        "{hol.4}Then the most rebellious villages are placed on the blackboard: cut off from all supplies, including food.",
        "{-hol}{-g7}{pct}The historian Nicolas Werth, source four, gives the figures. {pct.g}In September 1932, only thirty-two per cent "
        "of the monthly grain target was reached in Ukraine. {pct.d}By the twenty-fifth of October, only twenty-two per cent.",
        "{-pct}{bil}The result is a man-made famine: the {!Holodomor}Holodomor, in 1932 and 1933. "
        "It killed about four million people in Ukraine. That death toll is added from outside the class notes.",
        "{-bil}{lec11}Remember the logic: the famine was not a natural disaster. It came from a policy: requisitions, and villages cut off as a punishment.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[19]),
        "hol": dict(type="liste", titre="Ukraine, 1932: step by step", petit=True, bande=True, x=60, y=120, w=620, items=[
            "Peasants hide grain in pits; children cut stalks at night", "OGPU-backed brigades sent to “take the grain”",
            "Molotov and Kaganovich halt manufactured goods to failing districts", "“Rebellious” villages “placed on the blackboard”: no food"]),
        "pct": dict(type="cols", g="September 1932", gq="32% of the monthly grain target reached", d="25 October 1932",
                    dq="only 22%", vs="→", repere="Nicolas Werth (Worksheet 2, source 4)"),
        "bil": dict(type="mot", t="≈ 4 million dead", g="the Holodomor, Ukraine, 1932–33 · toll added from outside the class notes", y=250, taille=96),
        "lec11": dict(type="note", terme="Key term · Holodomor", cles=["man-made", "policy"],
                      t="The man-made famine of 1932–33 in Ukraine.",
                      etape="Not a natural disaster: requisitions, and villages cut off as a punishment", x=170, y=200, w=940),
    }),

    # ================================================================ stalinisme, idée 12 et Worksheet 2
    dict(id="sta12", chap="Stalinism · an economic failure", fond="aube", humeur="calme",
         retenir="Collectivisation ruined agriculture: no motivation, livestock slaughtered, production down. Feigin, 9 April 1932: kolkhoz cows give 1–3 litres of milk a day instead of 5–7; “people are starving”.",
         beats=[
        "{def4}Idea twelve. Beyond the famine, collectivisation was an {!economic failure}economic failure. "
        "{def4.1}Peasants who lost their land and animals had no reason to work hard for the kolkhoz, and many slaughtered their livestock "
        "rather than hand it over. Production fell, resources became scarcer, and the countryside turned hostile.",
        "{-def4}{lait}The example: source five, a letter written from Novosibirsk on the ninth of April 1932, by an official named Feigin, "
        "to the Soviet leader Ordzhonikidze. {lait.g}Normally, a cow gives five to seven litres of milk a day. "
        "{lait.d}The kolkhoz cows give one to three. The peasants are slaughtering their last animals. And Feigin writes:{-lait}",
        ("C", "people are starving", "c_fei"),
        "{-c_fei}{choix}So the regime made a choice: {!ideology and control}ideology and control, rather than the food supply of its own people.",
        "{-choix}{ws2}Worksheet two sums up the whole process in four boxes: {ws2.1}the ideology, Marxism; {ws2.2}the objective, "
        "total collectivisation in five years; {ws2.3}the implementation, collective farms and the kulaks persecuted; "
        "{ws2.4}and the results: the Holodomor, resistance, and economic failure.",
        ("P", 3.0),
    ], vis={
        "def4": dict(type="def", cles=["motivation", "slaughtered", "fell"], terme="Idea 12 · an economic failure",
                     t="No motivation in the kolkhoz, livestock slaughtered, production down.",
                     etape="The countryside turns hostile", x=170, y=200, w=940),
        "lait": dict(type="cols", g="A normal cow", gq="5 to 7 litres of milk a day", d="A kolkhoz cow, 1932",
                     dq="1 to 3 litres a day", vs="≠", repere="Feigin to Ordzhonikidze, Novosibirsk, 9 April 1932 (source 5)"),
        "c_fei": dict(type="cit", a="Feigin, letter to Ordzhonikidze", o="Novosibirsk, 9 April 1932 (Worksheet 2, source 5)", x=200, y=230, w=880),
        "choix": dict(type="mot", t="Ideology before bread", g="the regime chose control over its people's food supply", y=260, taille=84),
        "ws2": dict(type="liste", titre="Worksheet 2 · the collectivisation process", petit=True, items=[
            "Ideology: Marxism · no private property, profit or classes · against capitalism",
            "Objective: total collectivisation in 5 years · a modern industrial USSR · autarky",
            "Implementation: collective farms (kolkhozes, sovkhozes) · kulaks persecuted",
            "Results: the Holodomor (1932–33) · grain hidden, livestock slaughtered · economic failure"], x=130, y=130, w=1020),
    }),

    # ================================================================ nazisme, idée 13
    dict(id="naz13", chap="Nazism · race struggle", fond="nuit", humeur="tension",
         retenir="Nazism: history as a struggle between races, ranked in a hierarchy, the “Aryans” the purest. Survival through race purity (ban on mixed relations) and territory. Mein Kampf, 1924–25.",
         beats=[
        "{g8}{g8.1}Now Nazism. Idea thirteen. For the Nazis, the history of humankind is a {!struggle between races}struggle between races. "
        "{race}{race.1}Races form a hierarchy, some more valuable than others, and it is crucial to recognise and study them. "
        "The so-called Aryans are the purest.",
        "{race.2}Every individual shares a collective instinct for survival. {race.3}And the survival of the race depends on two things. "
        "Race purity: hence the ban on relations between races. {race.4}And the seizure of territory, to expand the population. "
        "Hitler had set out these racist views as early as 1924 and 1925, in Mein Kampf.",
        "{-race}{-g8}{hum}The example, on Monsieur Ros's slide: {hum.g}a scene of public humiliation in 1935. A non-Jewish woman and a Jewish man, "
        "surrounded by SA men, forced to wear placards denouncing their relationship. "
        "{hum.d}And a chart of the Nazi health ministry, from Bamberg, which ranked the racial groups of the earth.",
        "{-hum}{lien}Notice the second condition: territory. {lien.1}This is the root of Lebensraum, the living space, which you will see in episode six.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[23]),
        "race": dict(type="liste", titre="Idea 13 · the Nazi view of history", petit=True, bande=True, x=60, y=120, w=620, items=[
            "History = a struggle between races, ranked in a hierarchy", "A collective instinct for survival",
            "Survival 1: race purity · relations between “races” banned", "Survival 2: territory, to expand the population"]),
        "hum": dict(type="cols", g="1935 · public humiliation", gq="a couple forced by SA men to wear placards denouncing their relationship",
                    d="Bamberg · a health-ministry chart", dq="the “racial groups of the earth” ranked", vs="+", repere="M. Ros's slide"),
        "lien": dict(type="note", terme="Purity and territory", cles=["territory", "Lebensraum"],
                     t="The second condition of survival, territory, is the root of Lebensraum.",
                     etape="Mein Kampf, 1924–1925 · episode 6", x=170, y=200, w=940),
    }),

    # ================================================================ nazisme, idée 14
    dict(id="naz14", chap="Nazism · the language of “bacteria”", fond="guerre", humeur="tension",
         retenir="Jews, the “most dangerous race” in Nazi ideology; described as “bacteria”, a “virus” to be eliminated: elimination presented as hygiene. Racial instruction mandatory, Sept. 1933; Der Giftpilz (1938).",
         beats=[
        "{dang}Idea fourteen. In Nazi ideology, the Jews were the most dangerous race. {dang.1}Why? Because, unlike the others, "
        "they supposedly had no living space of their own. {dang.2}So they were accused of seeking to dominate their host peoples, "
        "by destroying the nation-state, {dang.3}and of aiming at the bastardisation of all peoples, and the elimination of all states.",
        "{-dang}{bio}The class noted the {!biological language}biological language that followed. {bio.1}Jews described as bacteria infecting "
        "the body of the nation. A virus, to be eliminated. {bio.2}And if a people is described as a disease, eliminating it becomes hygiene, "
        "not crime. {!Words prepared deeds}Words prepared deeds.",
        "{-bio}{eco14}The example: the school. {eco14.1}In September 1933, racial instruction became mandatory in German schools. "
        "{eco14.2}Children's books carried the message: Elvira Bauer's book of 1936, whose title promised that all the Jews must leave, "
        "{eco14.3}and Der Giftpilz, The Poisonous Mushroom, Nuremberg, 1938.",
    ], vis={
        "dang": dict(type="liste", titre="Idea 14 · the “most dangerous race”, in Nazi ideology", items=[
            "No living space of their own, said the Nazis", "So supposedly out to dominate host peoples and destroy the nation-state",
            "And aiming at the “bastardisation” of all peoples, the end of all states"], x=150, y=150, w=980),
        "bio": dict(type="def", cles=["bacteria", "virus", "hygiene"], terme="A biological language",
                    t="Jews described as “bacteria” infecting the nation, a “virus” to be eliminated.",
                    etape="If a people is a disease, elimination becomes “hygiene”: words prepared deeds", x=170, y=200, w=940),
        "eco14": dict(type="liste", titre="The message carried to children", items=[
            "September 1933: racial instruction mandatory in German schools",
            "Elvira Bauer's children's book, 1936: “all the Jews must leave”",
            "Der Giftpilz (“The Poisonous Mushroom”), Nuremberg, 1938"], x=150, y=150, w=980),
    }),

    # ================================================================ nazisme, idée 15
    dict(id="naz15", chap="Nazism · Germans judged “unfit”", fond="nuit", humeur="tension",
         retenir="Nazi racism also struck Germans: disabled people, people with genetic diseases. T4, launched in 1939: about 70,000 disabled Germans murdered, 1939–41, mostly in gas chambers.",
         beats=[
        "{unfit}Idea fifteen. The list of those to be eliminated went beyond the Jews. {unfit.1}Disabled people. "
        "{unfit.2}People with genetic diseases. {unfit.3}And anyone who had a sexual relationship with those the Nazis called viruses.",
        "{-unfit}{t4}The example: the {!T4 programme}T4 programme, launched in 1939: the murder of disabled people in Germany itself, "
        "in specially built gas chambers. {t4.1}About seventy thousand between 1939 and 1941, according to Monsieur Ros's revised slides. "
        "{t4.2}An earlier version said two hundred thousand: that figure is the toll up to 1945. For the course, keep seventy thousand, for 1939 to 1941.",
        "{-t4}{lec15}So Nazi racism attacked Germans too, when they did not fit the ideal of the pure race. "
        "{lec15.1}The enemy was not only outside the nation. It could be inside every family.",
    ], vis={
        "unfit": dict(type="liste", titre="Idea 15 · also targeted", items=[
            "Disabled people", "People with genetic diseases", "Anyone in a relationship with these so-called “viruses”"],
            x=170, y=170, w=940),
        "t4": dict(type="def", cles=["1939", "gas"], terme="The T4 programme · 1939",
                   t="The murder of disabled Germans, in specially built gas chambers: about 70,000 in 1939–1941.",
                   etape="Earlier slides: 200,000 = the toll up to 1945 · keep 70,000 for 1939–41", x=170, y=200, w=940),
        "lec15": dict(type="note", terme="For the essay", cles=["Germans", "pure"],
                      t="Nazi racism struck Germans too, when they did not fit the ideal of the pure race.",
                      etape="The enemy could be inside every family", x=170, y=200, w=940),
    }),

    # ================================================================ comparaison : h2ideo
    dict(id="compare", chap="Three ideologies compared", fond="aube", humeur="lumiere",
         retenir="Common: rejection of liberal democracy, a supreme goal that justifies any means, total control through coercion, a “New Man”. Different: the goal (nation / race / class), hence the enemy and its fate.",
         beats=[
        "{com}Now let's compare. First, what the three have in common. {com.1}They reject liberal democracy. "
        "{com.2}They set a supreme goal that justifies any means. {com.3}They seek total control of society through coercion. "
        "{com.4}And they want to create a New Man: that will be episode four.",
        "{-com}{but}But the supreme goals are opposite. {but.1}Fascism: a united, disciplined, great nation. "
        "{but.2}Nazism: a pure race, which expands its territory and its population. "
        "{but.3}Stalinism: a socialist, industrial and self-sufficient Soviet Union, with no capitalist elements left.",
        "{-but}{enn}And so the enemy within is not the same. {enn.1}In Italy: the left and its critics, like the socialist Matteotti. "
        "{enn.2}In Germany: Jews, disabled people, people with hereditary illnesses, the so-called virus. "
        "{enn.3}In the Soviet Union: the kulaks and all the capitalist elements.",
        "{-enn}{sort}Nor its fate. {sort.1}Silenced rather than killed, in Italy. {sort.2}To be eliminated, to purge the race, in Germany. "
        "{sort.3}Persecuted as a class, in the Soviet Union, with the Holodomor of 1932 and 1933.",
        "{-sort}{rule}So here is the rule for an essay. {rule.g}What is common is the method of power. "
        "{rule.d}What differs is the goal it serves, and therefore the target of terror.",
    ], vis={
        "com": dict(type="liste", titre="Common to all three", cles=["democracy", "supreme", "coercion", "New"], items=[
            "Rejection of liberal democracy", "A supreme goal that justifies any means",
            "Total control of society through coercion", "The will to create a “New Man”"], x=170, y=140, w=940),
        "but": dict(type="cartes", petit=True, items=[
            dict(t="Fascism", q="supreme goal: a united, disciplined, great nation"),
            dict(t="Nazism", q="supreme goal: a pure race that expands its territory"),
            dict(t="Stalinism", q="supreme goal: a socialist, industrial, self-sufficient USSR")]),
        "enn": dict(type="cartes", petit=True, items=[
            dict(t="Fascism", q="enemy within: the left and its critics (Matteotti, 1924)"),
            dict(t="Nazism", q="enemy within: Jews, disabled people (T4, 1939)"),
            dict(t="Stalinism", q="enemy within: the kulaks, “capitalist elements” (1932)")]),
        "sort": dict(type="cartes", petit=True, items=[
            dict(t="Fascism", q="the enemy silenced rather than killed"),
            dict(t="Nazism", q="the enemy to be eliminated, to “purge” the race"),
            dict(t="Stalinism", q="the enemy persecuted as a class; the Holodomor")]),
        "rule": dict(type="cols", g="Common", gq="the method of power", d="Different", dq="the goal it serves → the target of terror",
                     vs="≠", repere="The key sentence of the comparison"),
    }),

    # ================================================================ la grille de M. Ros et les points à confirmer
    dict(id="grille", chap="M. Ros's synthesis grid", fond="aube", humeur="calme",
         retenir="The grid, “Ideology” block: similarities (rejects liberal democracy; a supreme goal; total control for a New Man) · specificities: absolute State / race struggle / class struggle.",
         beats=[
        "{gr}Monsieur Ros sums up the chapter in a synthesis grid, Fascism, Nazism, Stalinism: on the site, you can hide the cells and recite them. "
        "Here is its ideology block. "
        "{gr.1}Similarities, the same for the three: they reject liberal democracy, they have a supreme goal, and they want total control to create a New Man.",
        "{gr.2}Then the specificities of Fascism, {gr.3}of Nazism, {gr.4}and of Stalinism: everything you have just seen. "
        "Pause the video, and recite each column aloud.",
        "{-gr}{chk}And three points to confirm with Monsieur Ros. {chk.1}Matteotti: 1924, not 1925. {chk.2}Collectivisation: 1928, or late 1929. "
        "{chk.3}And the examples from outside the course: accurate, but in an essay, prefer Monsieur Ros's own.",
        ("P", 3.0),
    ], vis={
        "gr": dict(type="liste", titre="M. Ros's grid · Ideology", petit=True, items=[
            "Similarities (all three): reject liberal democracy · a supreme goal · total control to create a New Man",
            "Fascism: the absolute State · against liberalism, Marxism, parliamentarism, human rights · nationalist, militaristic · racist only from 1938",
            "Nazism: race struggle · hierarchy of races, “Aryans” the purest · purity and territory · Jews, the “most dangerous race” · T4",
            "Stalinism: class struggle · no property, no classes · Five-Year Plan, collectivisation · kulaks as class enemies"],
            x=110, y=110, w=1060),
        "chk": dict(type="liste", titre="To confirm with M. Ros", items=[
            "Matteotti: killed on 10 June 1924, not 1925", "Collectivisation: “from 1928” (Worksheet 2); late 1929 for many historians",
            "Outside the course: Lipari, ≈ 4 million Holodomor deaths, 1.8 million kulaks deported"], x=150, y=150, w=980),
    }),

    # ================================================================ à toi : un paragraphe d'essay
    dict(id="essai", chap="Your turn · an essay paragraph", fond="aube", humeur="calme",
         retenir="A comparison paragraph: the common ground (a supreme goal, total control) · nation / race / class, one example each · the conclusion: the goal decides the enemy.",
         beats=[
        "{ex1}Now it's your turn. A question you could get, in the spirit of the course's essay on control: "
        "{!Explain how}Explain how the ideologies of Fascism, Nazism and Stalinism differed.",
        "{-ex1}{str}The structure of a comparison paragraph. {str.1}A topic sentence: the common ground. "
        "{str.2}Then each regime: its supreme goal, and one precise example. {str.3}Then the consequence: the enemy. "
        "{str.4}And a closing sentence that answers the question.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod}Here is a model. {mod.1}All three regimes rejected liberal democracy and set a supreme goal that justified total control, "
        "but each goal was different. {mod.2}Fascism put the nation, embodied in an absolute State, above everything: the Doctrine of 1932 says "
        "that everything is in the State, and it united all classes instead of setting them against each other. "
        "{mod.3}Nazism saw history as a struggle between races: it banned relations between races, and from September 1933 it taught racism in schools. "
        "{mod.4}Stalinism, on the contrary, was Marxist: history was class struggle, so the Five-Year Plan of 1928 collectivised the land, "
        "from seven per cent of peasant households to ninety per cent in 1936. "
        "{mod.5}As a result, the enemy differed: the critics of the State in Italy, like Matteotti; the Jews and the disabled in Germany, "
        "murdered under T4 from 1939; the kulaks in the Soviet Union, persecuted as a class. The goal decided the enemy.",
        ("P", 2.0),
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explain how the ideologies of Fascism, Nazism and Stalinism differed.",
                    src="Question written for this video, on Part I.3", enonce=["One comparison paragraph: nation, race, class"]),
        "str": dict(type="liste", titre="A comparison paragraph", cles=["common", "goal", "enemy", "answers"], items=[
            "Topic sentence: the common ground", "Each regime: its supreme goal + one precise example",
            "The consequence: the enemy", "A closing sentence that answers the question"], x=170, y=140, w=940),
        "pa1": dict(type="pause", t="Essay paragraph: explain how the ideologies of Fascism, Nazism and Stalinism differed.",
                    sous="Nation, race, class: one example each. Pause the video, write, then play on for a model."),
        "mod": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "Common ground: no liberal democracy; a supreme goal justifying total control",
            "Fascism → the nation and the State: “everything is in the State” (1932); classes united",
            "Nazism → the race: relations between “races” banned; racial instruction, Sept. 1933",
            "Stalinism → the class: Five-Year Plan (1928); 7% → 90% collectivised (1936)",
            "So the enemy differs: Matteotti · Jews and the disabled (T4) · the kulaks"], x=130, y=120, w=1020),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}Fascism: a new revolution for the nation and the absolute State; Matteotti and the fascistissime laws; "
        "a word used with pride, totalitarian; a less complete control, with the Church and the king; racist only from 1938. "
        "{carte.2}Stalinism: class struggle; the Five-Year Plan and forced collectivisation, seven to ninety per cent; the kulaks; "
        "the Holodomor; an economic failure. "
        "{carte.3}Nazism: race struggle, purity and territory; the Jews described as bacteria; T4. "
        "{carte.4}And the comparison: the same method, three goals; and the goal decides the enemy.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the leader, the party and the New Man. How the Duce, the Führer and the little father of the peoples "
        "were turned into idols… and how each regime set out to remake human beings.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="NATION · RACE · CLASS", branches=[
            dict(t="Fascism", items=["new revolution · Rome", "Matteotti 1924 · laws 1925", "Church, king · racist 1938"]),
            dict(t="Stalinism", items=["class struggle · Plan 1928", "7% → 90% · kulaks", "Holodomor · failure"]),
            dict(t="Nazism", items=["race struggle", "Jews as “bacteria”", "T4, 1939"]),
            dict(t="Compared", items=["same method", "three goals", "the goal decides the enemy"])]),
        "fin": dict(type="mot", t="Next: the leader and the New Man", g="Episode 4 · cult of personality · total control", y=270, taille=70),
    }),
]

QUIZ = [
    dict(q="Why is the 1932 poster of the Exhibition of the Fascist Revolution dated “year XI”?",
         r=["The Fascist calendar starts in 1922, the year Mussolini seized power", "Fascism began in 1921",
            "It was the eleventh exhibition", "Rome was founded in year XI"], ok=0, voir="an11",
         ex="History was to start again with Fascism: 1922 = year I."),
    dict(q="In what sense did the fascists use the word “totalitarian”?",
         r=["Positively: a complete, united, strong State in which “everything is in the State”", "As an insult against Stalin",
            "To describe a democracy", "Only after 1945"], ok=0, voir="c_doc1",
         ex="The accusing meaning came after the war, with historians and philosophers such as Arendt."),
    dict(q="According to the Doctrine of Fascism, what divides humanity?",
         r=["Nations, not classes", "Classes, not nations", "Races", "Religions"], ok=0, voir="cl",
         ex="Class struggle is banned; all classes are united inside the nation, under the State."),
    dict(q="Which counter-power limited Mussolini's control?",
         r=["The Catholic Church (Lateran Accords, 1929)", "The trade unions", "The Communist Party", "The League of Nations"], ok=0, voir="lim",
         ex="And the king remained head of the State: a totalitarian ambition is not always totalitarian control."),
    dict(q="What share of Soviet peasant households was collectivised in 1930?",
         r=["57%", "7%", "15%", "90%"], ok=0, voir="gc",
         ex="7% in 1928, 15% in 1929, 57% in 1930, 90% in 1936: the leap of 1929–30 is one of coercion."),
    dict(q="In practice, who was labelled a kulak?",
         r=["Any peasant who refused collectivisation", "Only peasants owning more than 8 acres", "A member of a kolkhoz",
            "An officer of the OGPU"], ok=0, voir="kul",
         ex="On paper, more than 8 acres; in practice, any resisting peasant, “too selfish to share”."),
    dict(q="What was the Holodomor?",
         r=["The man-made famine of 1932–33 in Ukraine", "The first Five-Year Plan", "A Soviet collective farm",
            "A purge of the Red Army"], ok=0, voir="lec11",
         ex="Requisitions and “rebellious” villages cut off from all supplies: by 25 Oct. 1932, only 22% of the grain target was reached."),
    dict(q="What did the T4 programme, launched in 1939, do?",
         r=["It murdered disabled Germans, about 70,000 in 1939–41", "It made racial instruction compulsory",
            "It banned relations between “races”", "It deported the kulaks"], ok=0, voir="t4",
         ex="Nazi racism also struck Germans who did not fit the ideal of the pure race."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H2 · Part I.3 “Specific aspects of each regime”, Worksheet 2 on collectivisation, the comparison of the three ideologies, the synthesis grid, the points to confirm) as written on the site; animated map of chapter 2 (site).",
    "Added from outside the course, and said so: the Holodomor death toll (≈ 4 million), internal exile on Lipari, the deportation of the kulaks to Siberia and Kazakhstan, the “Great Turn” of late 1929, the figure of 1.8 million kulaks deported.",
    "Course correction: Matteotti was kidnapped and killed on 10 June 1924 (the slide says 1925, the year of Mussolini's claim of responsibility and of the fascistissime laws).",
    "Quotations: The Doctrine of Fascism (Mussolini and Gentile, 1932) and Stalin's speech of 7 January 1933, as quoted in the course; Feigin's letter of 9 April 1932 (Worksheet 2, source 5).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
