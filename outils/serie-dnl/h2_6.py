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
                 "Addis Ababa": "Ad-iss Ab-a-ba", "Abyssinia": "Ab-iss-inn-ia", "Hannibal": "Han-ni-bal"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture6", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}The twelfth of March 1938. German troops cross into Austria, and Hitler enters Vienna in triumph. "
        "Not a single shot is fired.",
        "{-q1}{q2}This is the image Monsieur Ros chose to open part three. Because it asks the real question: "
        "was this aggression an accident, or was it written into the regimes themselves?",
        "{-q2}{q3}Italy in Africa, Germany in Europe, Japan in China: in the nineteen thirties, three regimes go out to conquer. "
        "Why was war so central to what they believed?",
        "{-q3}{-g0}{plan}The plan. {plan.1}First, the decade of aggression on the map. {plan.2}Then the key idea: war as a value. "
        "{plan.3}Case study one: Abyssinia. {plan.4}Lebensraum, the key term, and Mein Kampf. "
        "{plan.5}Japan, and case study two: Nanjing. {plan.6}And practice: the first DBQ of the chapter, and an essay paragraph.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[33]),
        "q1": dict(type="question", t="12 March 1938: Hitler enters Vienna.", bande=True),
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
        "{g1}Let's follow the story on the map first. {g1.1}It starts in Asia. In 1931, Japan occupies Manchuria, "
        "in the north-east of China, for its grain and its minerals. When the League of Nations protests, Japan simply leaves it, in 1933.",
        "{g1.2}Now Europe, 1935. Germany is rearming openly: the Wehrmacht is created. In April, at Stresa, Britain and France "
        "try to keep Mussolini on their side against Hitler. We will come back to Stresa in the next episode.",
        "{g1.3}October 1935: Italy, from its colonies of Eritrea and Somalia, invades Ethiopia, also called Abyssinia. "
        "In May 1936, its troops enter the capital, Addis Ababa. The League debates, and does nothing that matters.",
        "{g1.4}And the seventh of March 1936: German troops march into the Rhineland, demilitarised since the Treaty of Versailles. "
        "France and Britain do not react. Hitler's gamble pays off.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[18, 25, 27, 28]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="decennie2", chap="A decade of aggression: 1936–1938", fond="nuit", humeur="tension",
         retenir="25 Oct. 1936: the Rome–Berlin Axis; Spain, 1936–39 · 1937: Japan attacks China; Dec. 1937: Nanjing · 12 March 1938: the Anschluss.",
         beats=[
        "{g2}{g2.1}1936. The aggressors draw together. On the twenty-fifth of October, Hitler and Mussolini proclaim the Rome–Berlin Axis. "
        "And in Spain, where civil war has broken out, both send help to General Franco.",
        "{g2.2}1937. Japan attacks the rest of China. In December, its army takes Nanjing, then the capital of China, "
        "and massacres civilians and prisoners for weeks.",
        "{g2.3}And the twelfth of March 1938, our opening image: the German army enters Vienna. Austria disappears: "
        "this is the Anschluss.",
        "{-g2}{fr1}So here are the dates of this episode. {fr1.1}1931: Manchuria. {fr1.2}October 1935: Abyssinia invaded. "
        "{fr1.3}March 1936: the Rhineland. {fr1.4}October 1936: the Axis. {fr1.5}December 1937: Nanjing. "
        "{fr1.6}March 1938: the Anschluss. Pause the video if you need to copy them.",
        ("P", 3.0),
        "{-fr1}{exp}The course sums up Europe in one map: authoritarian expansion in the nineteen thirties. "
        "{exp.1}Germany: the Rhineland in 1936, the Anschluss and the Sudetenland in 1938. {exp.2}Italy: Abyssinia, 1935 to 1936. "
        "{exp.3}And Spain, in civil war from 1936 to 1939, where both dictators intervene. The Sudetenland is for episode seven.",
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
        "{q4}Now the course, idea by idea. The question of this part: why was the recourse to war so fundamental to these regimes?",
        "{-q4}{def1}The answer of the course is clear. War was not an accident of totalitarian policy. "
        "It was one of its core values. {def1.1}The answer lies in the ideologies themselves.",
        "{-def1}{trois}{trois.1}Fascism glorified war as the supreme test of a people. "
        "{trois.2}Nazism made the conquest of living space a condition for the survival of the race. "
        "{trois.3}And Japanese militarism presented expansion as a mission.",
        "{trois.4}So, aggression abroad was the logical extension of the regimes built at home. "
        "Think of episodes four and five: a New Man trained for combat, a nation in arms, an enemy everywhere. "
        "Once a regime is built for struggle at home, it looks for struggle abroad.",
        "{-trois}{photo1}And this is why Monsieur Ros opens the part with Vienna. On the twelfth of March 1938, "
        "Hitler fulfils abroad the programme he had announced in Mein Kampf, back in 1925: to bring all Germans into one Reich, "
        "and to expand.{-photo1}",
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
        "{photo2}{def2}Case study number one: Abyssinia. Fascist ideology made war a core value, and this led Italy into an aggressive foreign policy. "
        "{def2.1}And to justify it, Mussolini drew on a glorious past: the Roman Empire.",
        "{-def2}{-photo2}{g4}{g4.1}{eth}{eth.1}First, Libya. Italy had begun to colonise it with the Italo-Turkish war of 1911 to 1912, "
        "and Mussolini completed that colonisation, brutally. "
        "{eth.2}Then he attacked Abyssinia, that is Ethiopia: one of only two independent states left in Africa. "
        "{eth.3}The invasion begins in October 1935. {eth.4}And in May 1936, Italian troops enter Addis Ababa. "
        "Mussolini proclaims an empire, in the name of Rome.",
        "{-eth}{-g4}{film}Propaganda prepared the way. {film.1}Mussolini funded a historical film, Scipione l'africano, Scipio the African, "
        "released in 1937. It told Rome's victory over Hannibal of Carthage, in Africa. "
        "{film.2}The message was transparent: Rome had conquered Africa once, fascist Italy would do it again.",
        "{-film}{motif}Keep the pattern in mind, because it comes back all through the nineteen thirties. "
        "{motif.g}First, an ideological justification. {motif.d}Then, an invasion.",
    ], vis={
        "photo2": dict(type="tableau", img="h2-mussolini", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Benito Mussolini, Duce of Fascist Italy, c. 1937-1940 · Keystone, public domain"),
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
        "{cols1}Abyssinia reveals two weaknesses at once. {cols1.g}The first is Italy's. In Europe, Italy remained a power of lower rank. "
        "Its empire was weak, poorly administered, and in no way comparable to the British and French empires. "
        "{cols1.d}The second is the League of Nations'. The conquest showed that the League was ineffective "
        "whenever its decisions were not supported by the great powers.",
        "{-cols1}{fr2}Look at the calendar. {fr2.1}October 1935: Italy invades. "
        "{fr2.2}From October 1935 to May 1936, the League ponders the question of sanctions. "
        "{fr2.3}May 1936: Addis Ababa falls. Seven months: exactly the time it took Italy to conquer the country.",
        "{-fr2}{petrole}And the sanctions finally voted left out one product: oil. "
        "{petrole.1}The one product that could have stopped the Italian army, whose trucks and planes ran on it.",
        "{-petrole}{prec}A precision, from outside the course. The League did vote limited sanctions quickly, in October 1935, "
        "and they applied from the eighteenth of November. {prec.1}What it kept debating until the spring of 1936 was the oil embargo, "
        "which it never adopted. So in your essay, write: sanctions without oil, and an oil embargo endlessly debated.",
        "{-prec}{mot1}The lesson for the dictators was simple: aggression pays.",
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
        "{mot2}Now Germany, and one of the two key terms of the chapter. Lebensraum: living space.",
        "{-mot2}{def4}{def4.1}It is the theory that a nation needs its own territory and resources to survive. "
        "It came from a German geographer, Friedrich Ratzel, in 1901. {def4.2}For Ratzel, nations had to be self-sufficient "
        "in resources and territory, to protect themselves from external threats.",
        "{-def4}{auta}That self-sufficiency has a name: autarky. An economy that aims to depend on no one else. "
        "Remember chapter one: after 1929, the whole world closes its markets. Autarky becomes a dream of every militarist regime.",
        "{-auta}{g5}{g5.1}The Nazis turned a geographical theory into a programme of conquest. Lebensraum became the backbone "
        "of the Nazi worldview, and it drove their foreign policy. And the dream was old. As early as 1919, Heinrich Himmler, "
        "the future head of the SS, wrote in his diary that he would some day{-g5}",
        ("C", "live my life in the east and fight my battles as a German far from beautiful Germany", "c_him"),
        "{-c_him}{him}In 1919, Himmler is a young man of nineteen. {him.d}Twenty years later, as head of the SS, "
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
         retenir="Mein Kampf (1925), chapter “Eastern Policy”: conquer the Slavic lands, settle Germans as a master race, deport Russians to Siberia, enslave the rest. An old motto: Drang nach Osten.",
         beats=[
        "{nt1}Hitler turned living space into a plan. In Mein Kampf, in 1925, he devoted a whole chapter to it, "
        "called Eastern Policy. He announced{-nt1}",
        ("C", "an eastern policy in the sense of acquiring the necessary soil for our German people", "c_mk"),
        "{-c_mk}{plan2}What did that mean in practice? {plan2.1}Expanding Germany into the Slavic nations. "
        "{plan2.2}Settling Germans there, as a master race. {plan2.3}Deporting most Russians to Siberia. "
        "{plan2.4}And using the rest as slave labour.",
        "{-plan2}{drang}The idea itself was not new. {drang.1}The push eastwards had been a motto of German nationalism "
        "in the nineteenth century: Drang nach Osten, the drive to the East. "
        "{drang.2}What was new was that Hitler made it the centre of state policy.",
        "{-drang}{lien}Keep this in mind for chapter three. {lien.g}Here, in 1925, it is a programme written in a book. "
        "{lien.d}In June 1941, with Operation Barbarossa, it becomes a war of annihilation in the East.",
    ], vis={
        "nt1": dict(type="note", terme="Mein Kampf · 1925", cles=["Eastern Policy"],
                    t="A whole chapter devoted to living space: “Eastern Policy”.", x=170, y=470, w=940),
        "c_mk": dict(type="cit", a="Adolf Hitler", o="Mein Kampf, 1925, “Eastern Policy”", x=200, y=150, w=880),
        "plan2": dict(type="liste", titre="The plan for the East", cles=["Slavic", "master race", "Siberia", "slave"], items=[
            "Expand Germany into the Slavic nations", "Settle Germans there as a master race",
            "Deport most Russians to Siberia", "Use the rest as slave labour"], x=170, y=140, w=940),
        "drang": dict(type="def", cles=["motto", "centre"], terme="Drang nach Osten · “the drive to the East”",
                      t="A motto of nineteenth-century German nationalism.",
                      etape="Hitler made it the centre of state policy", x=170, y=200, w=940),
        "lien": dict(type="cols", g="1925 · a book", gq="Mein Kampf announces the conquest of the East", d="1941 · a war",
                     dq="Barbarossa: a war of annihilation (chapter 3)", vs="→"),
    }),

    # ================================================================ VIII. le Japon : l'autarcie (idée 6)
    dict(id="japon1", chap="Japan (1): the economic dimension", fond="nuit", humeur="tension",
         retenir="Japanese imperialism, economic side: the 1929 crisis hit Japanese trade → autarky; a growing population, an industry short of raw materials and space. Manchuria from 1931: grain and minerals.",
         beats=[
        "{q5}The third imperialism of the course is not European: it is Japan. And it has two dimensions. First, the economy.",
        "{-q5}{g6}{eco}{eco.1}The Great Depression of 1929 hit Japanese trade hard, and in the nineteen thirties it led to a desire "
        "for economic autarky. {eco.2}Expansion answered two needs: those of a growing population, "
        "{eco.3}and those of an industry short of raw materials and of space. "
        "{eco.4}So conquest was presented as the solution to a crisis, made worse by the closing of world markets.",
        "{-eco}{g6.1}The plainest example: Manchuria. From 1931, Japan occupies this region of north-eastern China "
        "for its rich grain fields and its reserves of raw minerals. The economic motive, in its plainest form.",
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
        "{def7.1}Its name: Pan-Asianism. As a superior Asian race, Japan claimed it had to liberate Asian territories "
        "from Western imperialism, and to build a New Order in East Asia, under Japanese leadership.",
        "{-def7}{res}Behind this lay resentment. Despite its growing industrial and military power in the Pacific, "
        "Japan felt despised by the Western powers. {res.g}The proof: at the Paris Peace Conference, in April 1919, "
        "the Western powers rejected the racial equality clause proposed by Japan. "
        "{res.d}Even though Japan received Germany's Pacific islands, as League mandates, in 1920.",
        "{-res}{symb}So militarism grew together with a strong nationalism. And look at the symbols. "
        "{symb.1}The Emperor Hirohito was pictured in military uniform. "
        "{symb.2}And the rising-sun flag was the ensign of the Imperial Navy. "
        "{symb.3}Notice the parallel with Europe: like Fascism and Nazism, Japanese militarism mixes a feeling of superiority "
        "with the humiliation of the peace of 1919.",
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
        "{def8}Case study number two: Nanjing. Its lesson in one sentence: aggression grew because nobody stopped it.",
        "{-def8}{fr3}Follow the steps. {fr3.1}1931: the Mukden incident, an explosion on a Japanese-run railway, staged by the Japanese army itself. "
        "It serves as a pretext to invade Manchuria. {fr3.2}The League sends a commission of inquiry, the Lytton Commission. "
        "{fr3.3}Japan's answer: it simply leaves the League, in 1933. "
        "{fr3.4}And in 1937, Japan attacks the rest of China.",
        "{-fr3}{pk}Why did Japan dare? {pk.1}Because the Japanese understood that the United States would not respond militarily. "
        "{pk.2}And because China was divided by a civil war, between Chiang Kai-shek's nationalists, the Kuomintang, "
        "and Mao Zedong's communists. {pk.3}Exactly as with Abyssinia: weak opponents, and a world that watches.",
        "{-pk}{g7}{g7.1}December 1937. The Japanese army takes Nanjing. For weeks, until January 1938, it kills civilians and prisoners. "
        "A Japanese newspaper even reported, as if it were a sport, a killing contest between two officers, "
        "under the headline Incredible Record.",
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
        "{-q6}{trait}Four features. {trait.1}A violent and racist ideology. {trait.2}Expansionism and militarism. "
        "{trait.3}A sharp increase in the level of violence. {trait.4}And civilians included among the military objectives. "
        "Keep these four in mind: you will find every one of them in Europe after 1939.",
        "{-trait}{bilan}How many victims? {bilan.g}About two hundred thousand, according to the Tokyo war crimes tribunal, after the war. "
        "{bilan.d}Three hundred thousand, the figure retained by China. {bilan.1}The debate is a subject in itself, "
        "and it is still politically sensitive between the two countries. In an essay, give the range.",
        "{-bilan}{date}And one last consequence. {date.1}Nanjing is one reason why some historians date the beginning "
        "of the Second World War to 1937, rather than 1939. {date.2}In Asia, the war had already begun. "
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
        "{gr}Remember Monsieur Ros's synthesis grid, from episode three. Its block International issues has two rows, still empty. "
        "With this part, you can fill them. {gr.1}Will of expansion. Italy: an empire in the name of Rome, Libya, then Ethiopia. "
        "{gr.2}Germany: Lebensraum, the conquest of the East announced in Mein Kampf. "
        "{gr.3}Feeling of superiority. Italy: the heirs of Rome. Germany: a master race over the Slavs.",
        "{gr.4}And the Soviet column? This part of the course says nothing about Soviet expansion: leave it for episode seven, "
        "with the pact of August 1939. Instead, the course adds a third aggressor: Japan, autarky and the superior race.",
    ], vis={
        "gr": dict(type="liste", titre="M. Ros's grid · International issues (suggested, from Part III.1)", petit=True, items=[
            "Will of expansion · Italy: Rome's empire; Libya, then Ethiopia (1935 – 36)",
            "Will of expansion · Germany: Lebensraum, the East (Mein Kampf, 1925)",
            "Feeling of superiority · Italy: heirs of Rome · Germany: a master race over the Slavs",
            "USSR: nothing in Part III.1 (see the pact, episode 7) · the course adds Japan"], x=150, y=140, w=980),
    }),

    # ================================================================ XIII. le DBQ 1
    dict(id="dbq1", chap="Your turn · DBQ 1: The Doctrine of Fascism", fond="aube", humeur="calme",
         retenir="DBQ a): judgement in the first line · the document in one sentence · a paragraph of strengths · a paragraph of limits.",
         beats=[
        "{ex1}Now the first DBQ of the chapter. The document: The Doctrine of Fascism, by Benito Mussolini, with the philosopher "
        "Giovanni Gentile, published in 1932 in the Enciclopedia Italiana. "
        "{ex1.d}Four phrases from it. War alone keys up all human energies to their maximum tension. "
        "Pacifism, a cloak for cowardly supine renunciation. The tendency of nations to expand, a manifestation of their vitality. "
        "And: for Fascism, the State is absolute.",
        "{ex1.1}The question: how useful is this document to a historian studying the role of totalitarian ideology "
        "as an underlying cause of World War Two?",
        "{-ex1}{str}The structure, as always. {str.1}First line: your judgement. Largely, significantly, partly or slightly useful. "
        "{str.2}The document in one sentence. {str.3}A paragraph of strengths, with several arguments. "
        "{str.4}A paragraph of limits, with several arguments.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Here is a model, from the course. {rep1.1}The document is significantly useful to a historian studying "
        "totalitarian ideology as a cause of the war, but it proves intention far better than it proves causation. "
        "{rep1.2}It is the official doctrine of Italian Fascism, written by Mussolini with Giovanni Gentile and published in 1932, "
        "in which war, the absolute State and imperial expansion are presented as the very substance of the regime.",
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
        "{at}The strengths. {at.1}First, its status. Written by the head of the regime himself, as an encyclopaedia entry, "
        "it is not one fascist opinion among others: it is the official self-definition of a state ideology. "
        "{at.2}Second, it states the link between ideology and war bluntly: war keys up all human energies, pacifism is cowardice. "
        "So war is not a means of policy, but a value in itself. "
        "{at.3}Third, it turns that value into a programme: the tendency to expand is a sign of vitality. "
        "Imperialism becomes a duty of national health, which explains Ethiopia in 1935. "
        "{at.4}Fourth, the State is absolute, democracy rejected: such a regime could not live inside the liberal order of 1919. "
        "{at.5}And fifth, propaganda is not unreliable here: it is perfectly reliable evidence of what the regime wanted to project.",
        "{-at}{li}The limits. {li.1}First, a doctrine is a declaration of intent, not a record of action. "
        "Italy did not enter the war until June 1940, and Mussolini hesitated for months. "
        "{li.2}Second, its date: a snapshot of 1932, before the Ethiopian war and before the Axis. "
        "{li.3}Third, its scope: one regime only. Nothing on Nazi racial ideology, on Lebensraum, or on Japanese militarism, "
        "the two powers that actually opened the war, in 1937 and 1939. "
        "{li.4}Fourth, it ignores the economic causes: the crash of 1929, economic nationalism, autarky. "
        "{li.5}Fifth, written for publication, it shows the doctrine the regime wished to display, not what Italians actually believed.",
        "{-li}{ccl}{ccl.1}So, significantly useful as proof that one regime built war into its official doctrine long before 1939. "
        "{ccl.2}Only partly useful to measure how far ideology caused the war: set it beside Mein Kampf, and beside an economic document.",
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
        "{ex2}One more exercise. This is the key issue of the chapter, the one you may draw at the oral: "
        "assess the role of totalitarianism in the collapse of global peace in the late nineteen thirties.",
        "{ex2.1}You will answer the whole question in episode eight. Today, write only the first argument: "
        "a paragraph showing how totalitarian ideologies made war a value and expansion a goal. Three regimes, three examples.",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod}A model paragraph. {mod.1}Totalitarian ideologies were a decisive cause of the collapse of peace, "
        "because they made war a value and expansion a goal. "
        "{mod.2}Fascism glorified war as the supreme test of a people: in October 1935, Italy invaded Abyssinia, "
        "justifying the conquest by the past of the Roman Empire. "
        "{mod.3}Nazism made living space a condition of the race's survival: from Ratzel's theory of 1901, "
        "Hitler drew in Mein Kampf, in 1925, a plan to conquer the East and enslave the Slavs. "
        "{mod.4}And Japanese militarism combined autarky and racial superiority: Manchuria in 1931, then Nanjing in December 1937. "
        "{mod.5}The link sentence: yet these ambitions succeeded only because nobody stopped them. That is the next argument, "
        "and the next episode.",
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
        "{carte}Let's sum up. {carte.1}War was a core value: the logical extension, abroad, of the regimes built at home. "
        "{carte.2}Abyssinia: Rome's past to justify an empire, October 1935 to May 1936; a weak Italy, a powerless League, sanctions without oil. "
        "{carte.3}Lebensraum: Ratzel in 1901, Himmler in 1919, Mein Kampf in 1925: conquer the East. "
        "{carte.4}And Japan: autarky and a superior race; Manchuria in 1931, and Nanjing in 1937, which announced the world war.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: appeasement, and the road to war. From Stresa to Munich and Prague, "
        "why did the democracies give way… until September 1939?",
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
    "Content: M. Ros's course (DNL History, H2 · Part III.1 “Hegemonic ambitions of totalitarian regimes”, the course map “Authoritarian expansion in the 1930s”, DBQ 1 on “The Doctrine of Fascism” and its model answer, the synthesis grid, the key issue) as written on the site; the grid's “International issues” rows are suggested by this video; animated map of chapter 2 (site).",
    "Outside the course: the League's sanctions against Italy were voted in October 1935 and applied from 18 November 1935; the oil embargo was debated until the spring of 1936 and never adopted.",
    "Photographs (via Wikimedia Commons): Hitler on the Heldenplatz, Vienna, 15 March 1938 (Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE); Benito Mussolini, c. 1937-1940 (Keystone, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
