"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 6 : « Hegemonic ambitions » (partie III.1 du cours,
« Hegemonic ambitions of totalitarian regimes »).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_6 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 10 Lebensraum, conquérir l'Est · 18 impérialisme japonais (Mandchourie) · 25 Stresa, Wehrmacht, accord naval ·
       27 Éthiopie · 28 Rhénanie · 29 Axe Rome-Berlin, guerre d'Espagne · 32 Nankin · 33 Anschluss
Contenu : partie III.1 du chapitre dans le site (dnl/index.html, CHAPTERS.H2, neuf idées), la carte du cours
« Authoritarian expansion in the 1930s » (h2expansion : Rhénanie 1936, Anschluss 1938, Sudètes 1938, guerre d'Espagne,
Éthiopie 1935-36), le DBQ 1 (H2_DBQ.h2dbq1 : « The Doctrine of Fascism », question a) « How useful », corrigé du site
résumé ; pas de question b) dans le cours), la grille de synthèse de M. Ros (bloc « International issues », laissé vide
sur le site : proposé ici à partir de la partie III.1), le key issue du chapitre (premier argument, en paragraphe d'essay).
Ce qui n'est pas dans le cours est dit « outside the course » : le calendrier précis des sanctions de la SDN
(sanctions votées en octobre 1935, appliquées le 18 novembre ; c'est l'embargo pétrolier qui est débattu jusqu'au
printemps 1936 et jamais adopté) — précision apportée à la formule du cours « debating sanctions for seven months ».
Corrections dites dans la vidéo (révision « pour l'oreille » du 06/11/2026) :
  - le cours fait entrer Hitler à Vienne le 12 mars 1938 : ce jour-là, l'armée allemande franchit la frontière ;
    Hitler entre à Vienne le 14 mars (discours du Heldenplatz le 15) ;
  - le chapitre « Eastern Policy » de Mein Kampf est dans le second volume (1926), le premier date de 1925 ;
  - l'Axe Rome-Berlin du 25 octobre 1936 : dit comme un accord, Mussolini ne le nomme « axe » que le 1er novembre.
Plan : la décennie d'agression sur la carte (1931-1938), puis le cours structuré (idée 1 ; Éthiopie, idées 2-3 ;
Lebensraum, idées 4-5 ; Japon, idées 6-7 ; Nankin, idées 8-9), la grille, deux pauses « Your turn » (DBQ a), paragraphe
d'essay sur le key issue).
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-6"
NOTION = "Totalitarian Regimes"
NUM = 6
TITRE = "Hegemonic ambitions"
SUIVANT = "Episode 7 · Appeasement and the road to war"
PRONONCIATION = {"Lebensraum": "Lay-bens-rowm", "Mein Kampf": "Mine Kampf", "Drang nach Osten": "Drahng nahkh Ost-en",
                 "Anschluss": "Ahn-shloos", "Ratzel": "Rat-sel", "Himmler": "Him-ler", "Wehrmacht": "Vair-markt",
                 "Duce": "Doo-cheh", "Führer": "Fyoo-rer", "Scipione l'africano": "Shee-pyo-neh lah-free-kah-no",
                 "Gentile": "Jen-tee-leh", "Enciclopedia Italiana": "En-chee-clo-peh-dee-a Ee-tah-lyah-na",
                 "Stresa": "Stray-za", "Mukden": "Mook-den", "Kuomintang": "Gwo-min-dang", "Mao Zedong": "Mao Dzuh-dong",
                 "Nanjing": "Nahn-jing", "Hirohito": "Hee-ro-hee-to", "Mukai": "Moo-kye", "Noda": "No-dah",
                 "Addis Ababa": "Ad-iss Ab-a-ba", "Abyssinia": "Ab-iss-inn-ia", "Hannibal": "Han-ni-bal", "SS": "Ess Ess"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture6", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}The twelfth of March, nineteen thirty-eight. German troops cross into Austria. "
        "Two days later, Hitler enters Vienna in triumph.",
        "{-q1}{q2}This is the image the course chose to open part three. Because it raises the real question. "
        "Was this aggression an accident? Or was it written into the regimes themselves?",
        "{-q2}{q3}Italy in Africa. Germany in Europe. Japan in China. In the nineteen thirties, three regimes set out to conquer. "
        "So why was war so central to what they believed?",
        "{-q3}{-g0}{plan}Here is the plan. {plan.1}First, the decade of aggression, on the map. {plan.2}Then the key idea: war as a value. "
        "{plan.3}Case study one: Abyssinia. {plan.4}Then Lebensraum, the key term, and Mein Kampf. "
        "{plan.5}Then Japan, with case study two: Nanjing. {plan.6}And some practice: the first DBQ of the chapter, and an essay paragraph.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[33]),
        "q1": dict(type="question", t="12 March 1938: the Anschluss.", bande=True),
        "q2": dict(type="question", t="An accident… or the programme of the regime?", bande=True),
        "q3": dict(type="question", t="Why was war so central to these regimes?", bande=True),
        "plan": dict(type="liste", titre="Episode 6 · Part III.1 of the course", items=[
            "The decade of aggression on the map: 1931 – 1938", "War: a core value of the regimes",
            "Case study 1: Abyssinia, 1935 – 1936", "Lebensraum and Mein Kampf: conquer the East",
            "Japan: autarky, race… and case study 2, Nanjing", "Practice: DBQ 1 and an essay paragraph"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 6", t="Hegemonic ambitions",
                      sous="Part III.1 · Abyssinia · Lebensraum · Japan · Nanjing"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="decennie1", chap="A decade of aggression: 1931–1936", fond="nuit", humeur="tension",
         retenir="1931: Japan in Manchuria · 1935: German rearmament, Stresa · Oct. 1935 – May 1936: Italy conquers Ethiopia · 7 March 1936: the Rhineland.",
         beats=[
        "{g1}Let's follow the story on the map first. {g1.1}It starts in Asia. In nineteen thirty-one, Japan occupies Manchuria, "
        "in the north-east of China. It wants the grain, and the minerals. The League of Nations protests. "
        "So Japan simply leaves the League, in nineteen thirty-three.",
        "{g1.2}Now Europe, in nineteen thirty-five. Germany is rearming openly, and the Wehrmacht is created. "
        "In April, at Stresa, Britain and France try to keep Mussolini on their side against Hitler. "
        "We will come back to Stresa in the next episode.",
        "{g1.3}October nineteen thirty-five. Italy invades Ethiopia, also called Abyssinia. It attacks from its colonies of Eritrea and Somalia. "
        "In May nineteen thirty-six, its troops enter the capital, Addis Ababa. The League debates. It does nothing that matters.",
        "{g1.4}And on the seventh of March, nineteen thirty-six, German troops march into the Rhineland. "
        "It had been demilitarised since the Treaty of Versailles. France and Britain do not react. Hitler's gamble pays off.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[18, 25, 27, 28]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="decennie2", chap="A decade of aggression: 1936–1938", fond="nuit", humeur="tension",
         retenir="25 Oct. 1936: the Rome–Berlin Axis; Spain, 1936–39 · 1937: Japan attacks China; Dec. 1937: Nanjing · 12 March 1938: the Anschluss.",
         beats=[
        "{g2}{g2.1}Nineteen thirty-six. The aggressors draw together. On the twenty-fifth of October, Germany and Italy come to an agreement: "
        "the Rome–Berlin Axis. In Spain, civil war has broken out. Both dictators send help to General Franco.",
        "{g2.2}Nineteen thirty-seven. Japan attacks the rest of China. In December, its army takes Nanjing. "
        "For weeks, it massacres civilians and prisoners.",
        "{g2.3}And the twelfth of March, nineteen thirty-eight: our opening image. The German army marches into Austria, "
        "and Austria disappears. This is the Anschluss.",
        "{-g2}{fr1}So here are the dates of this episode. {fr1.1}Nineteen thirty-one: Manchuria. {fr1.2}October nineteen thirty-five: Abyssinia is invaded. "
        "{fr1.3}March nineteen thirty-six: the Rhineland. {fr1.4}October nineteen thirty-six: the Axis. {fr1.5}December nineteen thirty-seven: Nanjing. "
        "{fr1.6}March nineteen thirty-eight: the Anschluss. Pause the video if you need to copy them.",
        ("P", 3.0),
        "{-fr1}The course sums up Europe in a single map: authoritarian expansion in the nineteen thirties. "
        "{exp}{exp.1}Germany takes the Rhineland in nineteen thirty-six. Then the Anschluss, and the Sudetenland, in nineteen thirty-eight. "
        "{exp.2}Italy conquers Abyssinia, between nineteen thirty-five and thirty-six. "
        "{exp.3}And Spain is in civil war from nineteen thirty-six to thirty-nine, with both dictators involved. "
        "The Sudetenland is for episode seven.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[29, 32, 33]),
        "fr1": dict(type="frise", items=[
            dict(nom="Manchuria", d=1931, q="Japan"), dict(nom="Abyssinia", d=1935, q="October: Italy"),
            dict(nom="Rhineland", d=1936, q="7 March: Germany"), dict(nom="The Axis", d=1936, q="25 October"),
            dict(nom="Nanjing", d=1937, q="December: Japan"), dict(nom="Anschluss", d=1938, q="12 March")]),
        "exp": dict(type="liste", titre="The course map · Authoritarian expansion in the 1930s", items=[
            "Germany: Rhineland 1936 · Anschluss 1938 · Sudetenland 1938", "Italy: invades Abyssinia (Ethiopia), 1935 – 1936",
            "Spain: civil war, 1936 – 1939"], x=170, y=150, w=940),
    }),

    # ================================================================ III. la guerre, valeur centrale (idée 1)
    dict(id="valeur", chap="War: a core value", fond="guerre", humeur="tension",
         retenir="War was not an accident but a core value: fascism glorified war, Nazism needed living space, Japanese militarism saw expansion as a mission. Aggression abroad = the logical extension of the regime at home.",
         beats=[
        "{q4}Now the course, idea by idea. Here is the question of this part. Why was the recourse to war so fundamental to these regimes?",
        "{-q4}{def1}The course gives a clear answer. War was not an accident of totalitarian policy. "
        "It was one of its core values. {def1.1}And the answer lies in the ideologies themselves.",
        "{-def1}{trois}{trois.1}Fascism glorified war as the supreme test of a people. "
        "{trois.2}Nazism made the conquest of living space a condition for the survival of the race. "
        "{trois.3}And Japanese militarism presented expansion as a mission.",
        "{trois.4}So aggression abroad was the logical extension of the regimes built at home. "
        "Think back to episodes four and five. A New Man trained for combat. A nation in arms. An enemy everywhere. "
        "A regime built for struggle at home will look for struggle abroad.",
        "{-trois}{photo1}That is why the course opens the part with the Anschluss, in March nineteen thirty-eight. "
        "Here, Hitler carries out abroad the programme he had announced in Mein Kampf, back in nineteen twenty-five. "
        "Bring all Germans into one Reich. And expand.{-photo1}",
    ], vis={
        "q4": dict(type="question", t="Why was war so fundamental to these regimes?"),
        "def1": dict(type="def", cles=["accident", "core values"], terme="War: a core value",
                     t="War was not an accident of totalitarian policy but one of its core values.",
                     etape="The answer lies in the ideologies themselves", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="Three ideologies, three reasons for war", cles=["supreme test", "living space", "mission"], items=[
            "Fascism: war, the supreme test of a people", "Nazism: living space, a condition of the race's survival",
            "Japanese militarism: expansion as a mission", "Aggression abroad = the regime at home, extended"], x=170, y=140, w=940),
        "photo1": dict(type="tableau", img="h2-anschluss", de=[1.0, .5, .5], a=[1.12, .5, .4],
                       legende="Hitler addresses the crowd on the Heldenplatz, Vienna, 15 March 1938 · Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE"),
    }),

    # ================================================================ IV. l'Éthiopie (idée 2)
    dict(id="abyssinie", chap="Case study 1 · Abyssinia", fond="nuit", humeur="tension",
         retenir="Mussolini used Rome's past to justify an empire: Libya (from 1911–12), then Ethiopia, one of only two independent African states. Scipione l'africano (1937). Invasion Oct. 1935; Addis Ababa, May 1936.",
         beats=[
        "{photo2}{def2}Case study number one: Abyssinia. Fascist ideology made war a core value. And that led Italy into an aggressive foreign policy. "
        "{def2.1}To justify it, Mussolini drew on a glorious past: the Roman Empire.",
        "{-def2}{-photo2}{g4}{g4.1}{eth}{eth.1}First, Libya. Italy had begun to colonise it in the Italo-Turkish war of nineteen eleven and twelve. "
        "Mussolini completed that colonisation, brutally. "
        "{eth.2}Then he attacked Abyssinia, that is, Ethiopia. It was one of only two independent states left in Africa. "
        "{eth.3}The invasion began in October nineteen thirty-five. {eth.4}In May nineteen thirty-six, Italian troops entered Addis Ababa. "
        "And Mussolini proclaimed an empire, in the name of Rome.",
        "{-eth}{-g4}{film}Propaganda prepared the way. {film.1}Mussolini funded a historical film, Scipione l'africano. Scipio the African. "
        "It came out in nineteen thirty-seven, and it told the story of Rome's victory over Hannibal of Carthage. In Africa. "
        "{film.2}The message was clear. Rome had conquered Africa once. Fascist Italy would do it again.",
        "Keep this pattern in mind. It comes back again and again in the nineteen thirties. "
        "{-film}{motif}{motif.g}First, an ideological justification. {motif.d}Then, an invasion.",
    ], vis={
        "photo2": dict(type="tableau", img="h2-mussolini", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Benito Mussolini, Duce of Fascist Italy, 1930s · Keystone, public domain"),
        "def2": dict(type="def", cles=["core value", "Roman Empire"], terme="Fascism and the past of Rome",
                     t="War as a core value → an aggressive foreign policy.",
                     etape="Mussolini uses the Roman Empire to justify his ambitions", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H2", sc=[27]),
        "eth": dict(type="liste", titre="Italy in Africa", x=740, y=80, w=500, petit=True, bande=True, items=[
            "Libya: colonised from 1911 – 12", "Ethiopia: one of two free African states",
            "October 1935: the invasion", "May 1936: Addis Ababa; an “empire”"]),
        "film": dict(type="note", terme="Scipione l'africano · 1937", cles=["Hannibal", "Africa"],
                     t="A historical film funded by Mussolini: Rome's victory over Hannibal.",
                     etape="Propaganda for fascist ambitions in Africa", x=170, y=200, w=940),
        "motif": dict(type="cols", g="1 · Justify", gq="an ideology: the glory of Rome", d="2 · Invade",
                      dq="Abyssinia, October 1935", vs="→", repere="The pattern of the 1930s"),
    }),

    # ================================================================ V. faiblesse italienne, impuissance de la SDN (idée 3)
    dict(id="sdn", chap="A weak empire, a powerless League", fond="nuit", humeur="calme",
         retenir="Italy: a power of lower rank, a weak empire. The League: ineffective without the great powers; it played for time (Oct. 1935 – May 1936) and its sanctions excluded oil.",
         beats=[
        "{cols1}Abyssinia reveals two weaknesses at once. {cols1.g}The first is Italy's own. In Europe, Italy remained a power of lower rank. "
        "Its empire was weak and poorly run. It was in no way comparable to the British and French empires. "
        "{cols1.d}The second weakness is the League of Nations'. The conquest showed that the League was powerless "
        "whenever the great powers did not back its decisions.",
        "{-cols1}{fr2}Look at the calendar. {fr2.1}October nineteen thirty-five: Italy invades. "
        "{fr2.2}From October to the following May, the League ponders the question of sanctions. "
        "{fr2.3}May nineteen thirty-six: Addis Ababa falls. Seven months. Exactly the time it took Italy to conquer the country.",
        "{-fr2}{petrole}And the sanctions that were finally voted left out one product: oil. "
        "{petrole.1}Yet oil was the one product that could have stopped the Italian army. Its trucks and its planes ran on it.",
        "{-petrole}{prec}Here is a precision from outside the course. The League did vote limited sanctions quickly, in October nineteen thirty-five. "
        "They applied from the eighteenth of November. {prec.1}What it kept debating until the spring of nineteen thirty-six was an oil embargo. "
        "And it never adopted one. So in your essay, write this: sanctions without oil, and an oil embargo endlessly debated.",
        "{-prec}{mot1}For the dictators, the lesson was simple. Aggression pays.",
        ("P", 1.5),
    ], vis={
        "cols1": dict(type="cols", g="Italy", gq="a power of lower rank; a weak, poorly administered empire", d="The League of Nations",
                      dq="ineffective without the support of the great powers", vs="+"),
        "fr2": dict(type="liste", titre="Seven months: the League plays for time", cles=["sanctions", "seven months"], items=[
            "October 1935: Italy invades Ethiopia", "October 1935 – May 1936: the League ponders sanctions",
            "May 1936: Addis Ababa falls · seven months"], x=170, y=150, w=940),
        "petrole": dict(type="def", cles=["oil"], terme="Sanctions… without oil",
                        t="The sanctions finally voted excluded oil.",
                        etape="The one product that could have stopped the Italian army", x=170, y=200, w=940),
        "prec": dict(type="note", terme="A precision · outside the course", cles=["October", "embargo"],
                     t="Limited sanctions voted in October 1935, applied from 18 November.",
                     etape="What was debated until spring 1936: the oil embargo, never adopted", x=170, y=200, w=940),
        "mot1": dict(type="mot", t="Aggression pays", g="The lesson of Abyssinia, for every dictator", y=260, taille=90),
    }),

    # ================================================================ VI. Lebensraum (idée 4)
    dict(id="lebensraum", chap="Lebensraum · the key term", fond="guerre", humeur="mystere",
         retenir="Lebensraum (key term): Ratzel (1901), a nation needs its own territory and resources to survive (autarky). The backbone of the Nazi worldview. Himmler, 1919: “live my life in the east”.",
         beats=[
        "{mot2}Now, Germany. And one of the two key terms of the chapter. Lebensraum. Living space.",
        "{-mot2}{def4}{def4.1}It is the theory that a nation needs its own territory and its own resources in order to survive. "
        "It came from a German geographer, Friedrich Ratzel, in nineteen hundred and one. "
        "{def4.2}For Ratzel, nations had to be self-sufficient, in resources and in territory. That was how they could protect themselves from external threats.",
        "{-def4}{auta}That self-sufficiency has a name: autarky. An economy that tries to depend on no one else. "
        "Remember chapter one. After nineteen twenty-nine, the whole world closes its markets. "
        "Autarky becomes the dream of every militarist regime.",
        "{-auta}{g5}{g5.1}The Nazis turned a geographical theory into a programme of conquest. Lebensraum became the backbone "
        "of the Nazi worldview, and it drove their foreign policy. The dream was an old one. "
        "As early as nineteen nineteen, Heinrich Himmler, the future head of the SS, wrote in his diary that he would some day{-g5}",
        ("C", "live my life in the east and fight my battles as a German far from beautiful Germany", "c_him"),
        "{-c_him}{him}Himmler wrote this in nineteen nineteen. He was still a teenager. {him.d}Twenty years later, at the head of the SS, "
        "he will be one of the men who carry out that plan in the East.",
    ], vis={
        "mot2": dict(type="mot", t="Lebensraum", g="“living space” · key term of the chapter", y=250, taille=110),
        "def4": dict(type="def", cles=["territory", "resources", "survive"], terme="Lebensraum · Friedrich Ratzel, 1901",
                     t="The theory that a nation needs its own territory and resources to survive.",
                     etape="Self-sufficiency in resources and territory, against external threats", x=170, y=200, w=940),
        "auta": dict(type="def", cles=["no one"], terme="Autarky",
                     t="An economy that aims to depend on no one else.",
                     etape="After 1929: a world closing its markets (chapter 1)", x=170, y=200, w=940),
        "g5": dict(type="globe", code="H2", sc=[10]),
        "c_him": dict(type="cit", a="Heinrich Himmler, future head of the SS", o="diary, 1919", x=200, y=190, w=880),
        "him": dict(type="cols", g="1919 · a dream", gq="a young man's diary: “live my life in the east”", d="1939 – 1945 · a plan",
                    dq="the head of the SS carries it out in the East (chapter 3)", vs="→"),
    }),

    # ================================================================ VII. Mein Kampf (idée 5)
    dict(id="meinkampf", chap="Mein Kampf: conquer the East", fond="guerre", humeur="tension",
         retenir="Mein Kampf (1925–26), chapter “Eastern Policy” (vol. 2): conquer the Slavic lands, settle Germans as a master race, deport Russians to Siberia, enslave the rest. An old motto: Drang nach Osten.",
         beats=[
        "{nt1}Hitler turned living space into a plan. Mein Kampf came out in nineteen twenty-five. "
        "In its second volume, a whole chapter is devoted to it, called Eastern Policy. Hitler announced{-nt1}",
        ("C", "an eastern policy in the sense of acquiring the necessary soil for our German people", "c_mk"),
        "{-c_mk}{plan2}What did that mean in practice? {plan2.1}Expanding Germany into the Slavic nations. "
        "{plan2.2}Settling Germans there, as a master race. {plan2.3}Deporting most Russians to Siberia. "
        "{plan2.4}And using the rest as slave labour.",
        "{-plan2}{drang}The idea itself was not new. {drang.1}In the nineteenth century, the push eastwards was already a motto of German nationalism: "
        "Drang nach Osten. The drive to the East. "
        "{drang.2}What was new was that Hitler made it the centre of state policy.",
        "Keep this in mind for chapter three. {-drang}{lien}{lien.g}In the nineteen twenties, it is a programme, written in a book. "
        "{lien.d}In June nineteen forty-one, with Operation Barbarossa, it becomes a war of annihilation in the East.",
    ], vis={
        "nt1": dict(type="note", terme="Mein Kampf · 1925 – 1926", cles=["Eastern Policy"],
                    t="Volume 2 (1926): a whole chapter devoted to living space, “Eastern Policy”.", x=170, y=470, w=940),
        "c_mk": dict(type="cit", a="Adolf Hitler", o="Mein Kampf, vol. 2 (1926), “Eastern Policy”", x=200, y=150, w=880),
        "plan2": dict(type="liste", titre="The plan for the East", cles=["Slavic", "master race", "Siberia", "slave"], items=[
            "Expand Germany into the Slavic nations", "Settle Germans there as a master race",
            "Deport most Russians to Siberia", "Use the rest as slave labour"], x=170, y=140, w=940),
        "drang": dict(type="def", cles=["motto", "centre"], terme="Drang nach Osten · “the drive to the East”",
                      t="A motto of nineteenth-century German nationalism.",
                      etape="Hitler made it the centre of state policy", x=170, y=200, w=940),
        "lien": dict(type="cols", g="1925 – 26 · a book", gq="Mein Kampf announces the conquest of the East", d="1941 · a war",
                     dq="Barbarossa: a war of annihilation (chapter 3)", vs="→"),
    }),

    # ================================================================ VIII. le Japon : l'autarcie (idée 6)
    dict(id="japon1", chap="Japan (1): the economic dimension", fond="nuit", humeur="tension",
         retenir="Japanese imperialism, economic side: the 1929 crisis hit Japanese trade → autarky; a growing population, an industry short of raw materials and space. Manchuria from 1931: grain and minerals.",
         beats=[
        "{q5}The third imperialism of the course is not European. It is Japan's. And it has two dimensions. First, the economy.",
        "{-q5}{g6}{eco}{eco.1}The Great Depression of nineteen twenty-nine hit Japanese trade hard. "
        "In the nineteen thirties, it led to a desire for economic autarky. {eco.2}Expansion answered two needs. First, those of a growing population. "
        "{eco.3}Second, those of an industry short of raw materials, and of space. "
        "{eco.4}So conquest was presented as the solution to a crisis. A crisis made worse by the closing of world markets.",
        "{-eco}{g6.1}The clearest example is Manchuria. From nineteen thirty-one, Japan occupies this region of north-eastern China. "
        "Why? For its rich grain fields, and its reserves of raw minerals. This is the economic motive, in its plainest form.",
    ], vis={
        "q5": dict(type="question", t="Japan: why conquer?"),
        "g6": dict(type="globe", code="H2", sc=[18]),
        "eco": dict(type="liste", titre="The economic dimension", x=40, y=100, w=520, petit=True, bande=True, items=[
            "1929: the Depression hits Japanese trade → autarky", "A growing population",
            "An industry short of raw materials and space", "Conquest sold as the cure for the crisis"]),
    }),

    # ================================================================ IX. le Japon : la race (idée 7)
    dict(id="japon2", chap="Japan (2): the racial dimension", fond="nuit", humeur="mystere",
         retenir="Japan, racial side: a “superior race” destined to lead Asia; Pan-Asianism, a “New Order in East Asia”. Resentment: the racial equality clause rejected in April 1919. Hirohito in uniform; the rising-sun flag.",
         beats=[
        "{def7}The second dimension is racial. Japanese imperialism was fuelled by a strong sense of racial superiority. "
        "{def7.1}Its name: Pan-Asianism. Japan saw itself as a superior Asian race. So, it claimed, it had to free Asian territories "
        "from Western imperialism. And it had to build a New Order in East Asia, under Japanese leadership.",
        "Behind this lay resentment. Japan's industrial and military power in the Pacific was growing. "
        "And yet Japan felt despised by the Western powers. {-def7}{res}{res.g}The proof came at the Paris Peace Conference, in April nineteen nineteen. "
        "The Western powers rejected the racial equality clause proposed by Japan. "
        "{res.d}This, even though Japan received Germany's Pacific islands, as League mandates, in nineteen twenty.",
        "{-res}{symb}So militarism grew together with a strong nationalism. Now look at the symbols. "
        "{symb.1}The Emperor Hirohito was pictured in military uniform. "
        "{symb.2}And the rising-sun flag was the ensign of the Imperial Navy. "
        "{symb.3}Do you see the parallel with Europe? Like Fascism and Nazism, Japanese militarism mixes a feeling of superiority "
        "with the humiliation of the peace of nineteen nineteen.",
    ], vis={
        "def7": dict(type="def", cles=["superior", "liberate", "New Order"], terme="Pan-Asianism",
                     t="Japan, as a superior Asian race, must liberate Asia from Western imperialism.",
                     etape="… and build a “New Order in East Asia” under Japanese leadership", x=170, y=200, w=940),
        "res": dict(type="cols", g="Rejected", gq="April 1919: the racial equality clause refused by the West", d="Rewarded",
                    dq="1920: Germany's Pacific islands as League mandates", vs="≠", repere="A resentful great power"),
        "symb": dict(type="liste", titre="Militarism and nationalism", cles=["uniform", "ensign", "humiliation"], items=[
            "Emperor Hirohito pictured in military uniform", "The rising-sun flag: ensign of the Imperial Navy",
            "As in Europe: superiority + the humiliation of 1919"], x=170, y=150, w=940),
    }),

    # ================================================================ X. Nankin (idée 8)
    dict(id="nankin1", chap="Case study 2 · Nanjing: unchecked aggression", fond="guerre", humeur="tension",
         retenir="Mukden incident (1931), staged → Manchuria; the Lytton Commission; Japan leaves the League (1933); no US military response; China's civil war (Kuomintang vs Mao) → 1937: the rest of China attacked.",
         beats=[
        "{def8}Case study number two: Nanjing. Its lesson fits in one sentence. Aggression grew, because nobody stopped it.",
        "{-def8}{fr3}Follow the steps. {fr3.1}Nineteen thirty-one: the Mukden incident. An explosion on a railway run by the Japanese. "
        "It was staged by the Japanese army itself, and it served as a pretext to invade Manchuria. "
        "{fr3.2}The League sends a commission of inquiry: the Lytton Commission. "
        "{fr3.3}Japan's answer? It simply leaves the League, in nineteen thirty-three. "
        "{fr3.4}And in nineteen thirty-seven, Japan attacks the rest of China.",
        "{-fr3}{pk}Why did Japan dare? {pk.1}Because the Japanese understood that the United States would not respond militarily. "
        "{pk.2}And because China was split by a civil war. On one side, Chiang Kai-shek's nationalists, the Kuomintang. "
        "On the other, Mao Zedong's communists. {pk.3}Exactly as with Abyssinia: weak opponents, and a world that watches.",
        "{-pk}{g7}{g7.1}December nineteen thirty-seven. The Japanese army takes Nanjing. For weeks, until January nineteen thirty-eight, "
        "it kills civilians and prisoners. A Japanese newspaper even reported a killing contest between two officers, "
        "as if it were a sport. The headline read: Incredible Record.",
    ], vis={
        "def8": dict(type="def", cles=["nobody stopped"], terme="Case study 2 · Nanjing",
                     t="Aggression grew because nobody stopped it.", x=170, y=220, w=940),
        "fr3": dict(type="frise", items=[
            dict(nom="Mukden incident", d=1931, q="staged pretext"), dict(nom="Lytton Commission", d=1932, q="League inquiry"),
            dict(nom="Japan leaves the League", d=1933, q=""), dict(nom="War on China", d=1937, q="the rest of China")]),
        "pk": dict(type="liste", titre="Why Japan dared", cles=["United States", "civil war", "watches"], items=[
            "The United States would not respond militarily", "China divided: the Kuomintang (Chiang Kai-shek) vs Mao's communists",
            "As with Abyssinia: weak opponents, a world that watches"], x=170, y=150, w=940),
        "g7": dict(type="globe", code="H2", sc=[32]),
    }),

    # ================================================================ XI. Nankin annonce la guerre mondiale (idée 9)
    dict(id="nankin2", chap="Nanjing announced the world war", fond="guerre", humeur="tension",
         retenir="Nanjing (Dec. 1937 – Jan. 1938) concentrates the features of WWII: a violent, racist ideology; expansionism and militarism; more violence; civilians as targets. ≈ 200,000 (Tokyo tribunal) to 300,000 (China) killed. A reason to date the war from 1937.",
         beats=[
        "{q6}Why is Nanjing a case study? Because it concentrates what the world war would become.",
        "{-q6}{trait}It shows four features. {trait.1}A violent and racist ideology. {trait.2}Expansionism and militarism. "
        "{trait.3}A sharp rise in the level of violence. {trait.4}And civilians included among the military objectives. "
        "Keep these four in mind. You will find every one of them in Europe after nineteen thirty-nine.",
        "{-trait}{bilan}How many victims? {bilan.g}About two hundred thousand, according to the Tokyo war crimes tribunal, after the war. "
        "{bilan.d}Three hundred thousand, according to the figure retained by China. {bilan.1}The debate is a subject in itself. "
        "It is still politically sensitive between the two countries. In an essay, give the range.",
        "{-bilan}{date}And one last consequence. {date.1}Nanjing is one reason why some historians date the beginning "
        "of the Second World War to nineteen thirty-seven, rather than nineteen thirty-nine. {date.2}In Asia, the war had already begun. "
        "That debate opens chapter three.",
    ], vis={
        "q6": dict(type="question", t="Why is Nanjing a case study?"),
        "trait": dict(type="liste", titre="Nanjing: the features of the coming war", cles=["racist", "militarism", "violence", "civilians"], items=[
            "A violent and racist ideology", "Expansionism and militarism",
            "A sharp increase in the level of violence", "Civilians among the military objectives"], x=170, y=140, w=940),
        "bilan": dict(type="cols", g="≈ 200,000", gq="the Tokyo war crimes tribunal", d="≈ 300,000",
                      dq="the figure retained by China", vs="–", repere="Civilians and prisoners killed · a debate still sensitive"),
        "date": dict(type="def", cles=["1937", "1939"], terme="When did the war begin?",
                     t="Nanjing is one reason to date the start of the war to 1937 rather than 1939.",
                     etape="In Asia, the war had already begun · chapter 3", x=170, y=200, w=940),
    }),

    # ================================================================ XII. la grille de M. Ros
    dict(id="grille", chap="Filling the grid: international issues", fond="aube", humeur="calme",
         retenir="Will of expansion: Italy → Rome's empire, Libya, Ethiopia · Germany → Lebensraum in the East · Japan → Manchuria, China. Feeling of superiority: the glory of Rome · the master race · the “superior” Asian race.",
         beats=[
        "Remember the synthesis grid of the course, from episode three? Its block called International issues has two rows, still empty. "
        "With this part, you can fill them in. {gr}{gr.1}First row: the will of expansion. For Italy, an empire in the name of Rome. Libya, then Ethiopia. "
        "{gr.2}For Germany, Lebensraum: the conquest of the East, announced in Mein Kampf. "
        "{gr.3}Second row: the feeling of superiority. Italy sees itself as the heir of Rome. Germany, as a master race over the Slavs.",
        "{gr.4}And the Soviet column? This part of the course says nothing about Soviet expansion. Leave it for episode seven, "
        "and the pact of August nineteen thirty-nine. Instead, the course adds a third aggressor. Japan, with its autarky, and its superior race.",
    ], vis={
        "gr": dict(type="liste", titre="The course grid · International issues (suggested, from Part III.1)", petit=True, items=[
            "Will of expansion · Italy: Rome's empire; Libya, then Ethiopia (1935 – 36)",
            "Will of expansion · Germany: Lebensraum, the East (Mein Kampf, 1925)",
            "Feeling of superiority · Italy: heirs of Rome · Germany: a master race over the Slavs",
            "USSR: nothing in Part III.1 (see the pact, episode 7) · the course adds Japan"], x=150, y=140, w=980),
    }),

    # ================================================================ XIII. le DBQ 1
    dict(id="dbq1", chap="Your turn · DBQ 1: The Doctrine of Fascism", fond="aube", humeur="calme",
         retenir="DBQ a): judgement in the first line · the document in one sentence · a paragraph of strengths · a paragraph of limits.",
         beats=[
        "{ex1}Now, the first DBQ of the chapter. The document is The Doctrine of Fascism, by Benito Mussolini, "
        "written with the philosopher Giovanni Gentile. It was published in nineteen thirty-two, in the Enciclopedia Italiana. "
        "{ex1.d}Here are four phrases from it. War alone keys up all human energies to their maximum tension. "
        "Pacifism is a cloak for cowardly supine renunciation. The tendency of nations to expand is a manifestation of their vitality. "
        "And: for Fascism, the State is absolute.",
        "{ex1.1}The question. How useful is this document to a historian studying the role of totalitarian ideology "
        "as an underlying cause of World War Two?",
        "{-ex1}{str}The structure, as always. {str.1}First line: your judgement. Largely, significantly, partly, or slightly useful. "
        "{str.2}Then the document, in one sentence. {str.3}Then a paragraph of strengths, with several arguments. "
        "{str.4}And a paragraph of limits, with several arguments.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is a model, from the course. {rep1.1}The document is significantly useful to a historian studying "
        "totalitarian ideology as a cause of the war. But it proves intention far better than it proves causation. "
        "{rep1.2}It is the official doctrine of Italian Fascism, written by Mussolini with Giovanni Gentile and published in nineteen thirty-two. "
        "In it, war, the absolute State and imperial expansion are presented as the very substance of the regime.",
    ], vis={
        "ex1": dict(type="exo", niveau="dbq", titre="How useful is Document A to a historian studying the role of totalitarian ideology as an underlying cause of World War Two?",
                    src="DBQ 1 · Document A: Mussolini (with Giovanni Gentile), “The Doctrine of Fascism”, Enciclopedia Italiana, 1932",
                    donnees=["“War alone keys up all human energies to their maximum tension”",
                             "pacifism, “a cloak for cowardly supine renunciation”",
                             "“the tendency of nations to expand”, a “manifestation of their vitality”",
                             "“for Fascism the State is absolute”"]),
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa1": dict(type="pause", t="DBQ 1 a): how useful is The Doctrine of Fascism for studying ideology as an underlying cause of WWII?",
                    sous="Judgement, presentation, strengths, limits. Pause the video, write, then play on for a model."),
        "rep1": dict(type="liste", titre="A model answer · the opening", petit=True, items=[
            "Judgement: significantly useful… it proves intention better than causation",
            "Document: the official doctrine of Fascism, Mussolini and Gentile, Enciclopedia Italiana, 1932"],
                     x=150, y=150, w=980),
    }),

    # ================================================================ XIV. le DBQ 1 : atouts et limites
    dict(id="dbq1b", chap="DBQ 1: strengths and limits", fond="aube", humeur="calme",
         retenir="Strengths: the regime's own voice; war and expansion as values. Limits: intention, not action (Italy at war in June 1940); one date, one regime; no economic cause.",
         beats=[
        "{at}Now the strengths. {at.1}First, its status. It was written by the head of the regime himself, as an encyclopaedia entry. "
        "So it is not one fascist opinion among others. It is the official self-definition of a state ideology. "
        "{at.2}Second, it states the link between ideology and war bluntly. War keys up all human energies. Pacifism is cowardice. "
        "So war is not a means of policy. It is a value in itself. "
        "{at.3}Third, it turns that value into a programme. The tendency to expand is a sign of vitality. "
        "Imperialism becomes a duty of national health. And that explains Ethiopia, in nineteen thirty-five. "
        "{at.4}Fourth, the State is absolute, and democracy is rejected. Such a regime could not live inside the liberal order of nineteen nineteen. "
        "{at.5}And fifth, this is propaganda, but here that is not a weakness. It is perfectly reliable evidence of what the regime wanted to project.",
        "{-at}{li}Now the limits. {li.1}First, a doctrine is a declaration of intent. It is not a record of action. "
        "Italy did not enter the war until June nineteen forty, and Mussolini hesitated for months. "
        "{li.2}Second, its date. It is a snapshot of nineteen thirty-two, before the Ethiopian war, and before the Axis. "
        "{li.3}Third, its scope. It covers one regime only. Nothing on Nazi racial ideology, on Lebensraum, or on Japanese militarism. "
        "Yet those were the two powers that actually opened the war, in nineteen thirty-seven and nineteen thirty-nine. "
        "{li.4}Fourth, it ignores the economic causes: the crash of nineteen twenty-nine, economic nationalism, autarky. "
        "{li.5}Fifth, it was written for publication. It shows the doctrine the regime wished to display, not what Italians actually believed.",
        "{-li}{ccl}{ccl.1}So, the document is significantly useful. It proves that one regime built war into its official doctrine, long before nineteen thirty-nine. "
        "{ccl.2}But it is only partly useful to measure how far ideology caused the war. Set it beside Mein Kampf, and beside an economic document.",
    ], vis={
        "at": dict(type="liste", titre="Strengths · several arguments", petit=True, items=[
            "Status: the regime's official self-definition, by the Duce himself",
            "War as a value in itself: “maximum tension”; pacifism as cowardice",
            "Expansion as a duty: “vitality” → Ethiopia, 1935",
            "“The State is absolute”: incompatible with the liberal order of 1919",
            "Propaganda = reliable evidence of what the regime professed"], x=150, y=110, w=980),
        "li": dict(type="liste", titre="Limits · several arguments", petit=True, items=[
            "Intention, not action: Italy at war only in June 1940",
            "One date: 1932, before Ethiopia and the Axis",
            "One regime: no Lebensraum, no Japan",
            "No economic cause: 1929, economic nationalism, autarky",
            "Written for display, not what Italians believed"], x=150, y=110, w=980),
        "ccl": dict(type="cols", g="Significantly useful", gq="war written into an official doctrine, long before 1939",
                    d="Only partly useful", dq="to measure causation: add Mein Kampf and an economic source", vs="but"),
    }),

    # ================================================================ XV. paragraphe d'essay (key issue)
    dict(id="essai", chap="Your turn · an essay paragraph", fond="aube", humeur="calme",
         retenir="Key issue, argument 1: totalitarian ideologies made war a value and expansion a goal — Abyssinia 1935 (Rome), Lebensraum (Ratzel 1901, Mein Kampf 1925), Japan (Manchuria 1931, Nanjing 1937). Nuance: the democracies let it happen (episode 7).",
         beats=[
        "{ex2}One more exercise. This is the key issue of the chapter, the one you may draw at the oral. "
        "Assess the role of totalitarianism in the collapse of global peace in the late nineteen thirties.",
        "{ex2.1}You will answer the whole question in episode eight. Today, write only the first argument. "
        "One paragraph, showing how totalitarian ideologies made war a value and expansion a goal. Three regimes, three examples.",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod}Here is a model paragraph. {mod.1}Totalitarian ideologies were a decisive cause of the collapse of peace, "
        "because they made war a value and expansion a goal. "
        "{mod.2}Fascism glorified war as the supreme test of a people. In October nineteen thirty-five, Italy invaded Abyssinia, "
        "and justified the conquest by the past of the Roman Empire. "
        "{mod.3}Nazism made living space a condition of the race's survival. From Ratzel's theory of nineteen hundred and one, "
        "Hitler drew a plan in Mein Kampf: conquer the East, and enslave the Slavs. "
        "{mod.4}And Japanese militarism combined autarky and racial superiority. Manchuria in nineteen thirty-one. Then Nanjing, in December nineteen thirty-seven. "
        "{mod.5}And the link sentence: yet these ambitions succeeded only because nobody stopped them. That is the next argument. "
        "And the next episode.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Assess the role of totalitarianism in the collapse of global peace in the late 1930s.",
                    src="Key issue of the chapter (oral) · argument 1 only", enonce=["One paragraph: ideologies made war a value and expansion a goal"]),
        "pa2": dict(type="pause", t="Write argument 1: how did totalitarian ideologies make war a value and expansion a goal?",
                    sous="A topic sentence, three regimes, one precise example each. Pause, write, then play on."),
        "mod": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "Topic sentence: ideologies made war a value and expansion a goal",
            "Fascism → Abyssinia, October 1935, in the name of Rome",
            "Nazism → Lebensraum: Ratzel (1901), Mein Kampf (1925)",
            "Japan → autarky and race: Manchuria 1931, Nanjing 1937",
            "Link: … they succeeded because nobody stopped them"], x=150, y=120, w=980),
    }),

    # ================================================================ récap
    dict(id="recap6", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}War was a core value. It was the logical extension, abroad, of the regimes built at home. "
        "{carte.2}Abyssinia: Rome's past, used to justify an empire, from October nineteen thirty-five to May nineteen thirty-six. "
        "A weak Italy, a powerless League, and sanctions without oil. "
        "{carte.3}Lebensraum: Ratzel in nineteen hundred and one. Himmler in nineteen nineteen. Mein Kampf in nineteen twenty-five. The goal: conquer the East. "
        "{carte.4}And Japan: autarky, and a superior race. Manchuria in nineteen thirty-one. And Nanjing in nineteen thirty-seven, which announced the world war.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: appeasement, and the road to war. From Stresa to Munich and Prague. "
        "Why did the democracies give way, until September nineteen thirty-nine?",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="HEGEMONIC AMBITIONS", branches=[
            dict(t="War, a core value", items=["fascism: the supreme test", "Nazism: living space", "Vienna, 12 March 1938"]),
            dict(t="Abyssinia", items=["Rome's past · Scipio", "Oct. 1935 – May 1936", "League: no oil sanctions"]),
            dict(t="Lebensraum", items=["Ratzel, 1901 · autarky", "Mein Kampf, 1925", "Drang nach Osten"]),
            dict(t="Japan · Nanjing", items=["autarky · Manchuria 1931", "Pan-Asianism · 1919", "Nanjing, Dec. 1937"])]),
        "fin": dict(type="mot", t="Next: the road to war", g="Episode 7 · appeasement, Munich, September 1939", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="According to the course, what was war for the totalitarian regimes?",
         r=["One of their core values, the logical extension of the regime at home", "An accident forced on them by the democracies",
            "A last resort after the failure of diplomacy", "A purely economic necessity"], ok=0, voir="def1",
         ex="Fascism glorified war, Nazism needed living space, Japanese militarism saw expansion as a mission."),
    dict(q="How did Mussolini justify the conquest of Abyssinia?",
         r=["By the past of the Roman Empire", "By the need for living space in the East", "By Pan-Asianism",
            "By a League of Nations mandate"], ok=0, voir="def2",
         ex="He even funded the film Scipione l'africano (1937), on Rome's victory over Hannibal."),
    dict(q="Which product did the League's sanctions against Italy leave out?",
         r=["Oil", "Wheat", "Coal", "Weapons"], ok=0, voir="petrole",
         ex="Oil could have stopped the Italian army; the oil embargo was debated but never adopted."),
    dict(q="Who formulated the theory of Lebensraum, and when?",
         r=["The geographer Friedrich Ratzel, in 1901", "Hitler, in Mein Kampf (1925)", "Himmler, in 1919",
            "Mussolini, in 1932"], ok=0, voir="def4",
         ex="Hitler turned Ratzel's theory into a plan of conquest in Mein Kampf, chapter “Eastern Policy”."),
    dict(q="What did Hitler's “Eastern Policy” plan for the Russians?",
         r=["Deport most of them to Siberia and use the rest as slave labour", "Make them equal allies of Germany",
            "Leave them in peace in exchange for oil", "Turn them into German citizens"], ok=0, voir="plan2",
         ex="Germans were to settle the Slavic lands as a master race; the old motto was Drang nach Osten."),
    dict(q="Why did Japan occupy Manchuria from 1931, according to the course?",
         r=["For its grain fields and raw minerals", "To protect it from the Soviet Union",
            "To answer a League of Nations request", "To fight Mao's communists only"], ok=0, voir="g6",
         ex="The economic dimension: autarky, after the 1929 crisis hit Japanese trade."),
    dict(q="What did the Western powers reject at the Paris Peace Conference in April 1919?",
         r=["Japan's racial equality clause", "Italy's claim to Ethiopia", "Germany's claim to Austria",
            "The creation of the League"], ok=0, voir="res",
         ex="A source of Japanese resentment, even though Japan received Germany's Pacific islands as mandates in 1920."),
    dict(q="Why is Nanjing a reason to date the start of the Second World War to 1937?",
         r=["It already showed racist ideology, extreme violence and civilians as targets", "It was the first German victory",
            "The USA declared war on Japan after it", "It ended the League of Nations"], ok=0, voir="date",
         ex="≈ 200,000 (Tokyo tribunal) to 300,000 (China) civilians and prisoners killed, Dec. 1937 – Jan. 1938."),
]

CREDITS = [
    "Content: the DNL History course (chapter H2 · Part III.1 “Hegemonic ambitions of totalitarian regimes”, the course map “Authoritarian expansion in the 1930s”, DBQ 1 on “The Doctrine of Fascism” and its model answer, the synthesis grid, the key issue) as written on the site; the grid's “International issues” rows are suggested by this video; animated map of chapter 2 (site).",
    "Outside the course: the League's sanctions against Italy were voted in October 1935 and applied from 18 November 1935; the oil embargo was debated until the spring of 1936 and never adopted.",
    "Photographs (via Wikimedia Commons): Hitler on the Heldenplatz, Vienna, 15 March 1938 (Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE); Benito Mussolini, 1930s (Keystone, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
