"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 7 : « Appeasement and the road to war »
(parties III.2 « Democracies unable to stop totalitarian regimes » et III.3 « The road to WWII »).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_7 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 25 Stresa, Wehrmacht, accord naval · 28 Rhénanie · 29 Axe Rome-Berlin, guerre d'Espagne · 31 l'apaisement ·
       33 Anschluss · 34 Munich · 35 Prague · 36 pacte germano-soviétique · 37 attaque de la Pologne
Contenu : CHAPTERS.H2 du site (dnl/index.html), sections III.2 (7 idées) et III.3 (7 idées) ; schémas h2appease
(H2Appease : ce qui a été cédé, les sept raisons), h1slide (H1SlideAnim : les marches de Low, 1931-1939, redessinées en
escalier par un graphe), DBQ 2 (télégramme de Roosevelt, 14 avril 1939 : présenté plus brièvement, corrigé a) du site
résumé) et DBQ 3 (discours de Hitler à l'Obersalzberg, 22 août 1939 : traité en entier en « Your turn », a) avec le
corrigé du site résumé, b) question écrite pour la vidéo sur le Key Issue du chapitre, plan tiré de l'essay du site
« Assess the role of totalitarianism in the collapse of global peace in the late 1930s »).
Hors cours, dit comme tel : Guernica (le cours le donne lui-même comme « complementary example, not in the lesson »),
la part des Juifs dans la population autrichienne (environ 3 %). Corrections signalées : « Republican Congress » →
« an isolationist Congress » (déjà dans le cours) ; Anschluss : les 8 % du cours sont la part des exclus du vote
(opposants et Juifs ensemble), pas celle des seuls Juifs ; les « 700 000 officiers » de la caricature de Staline :
chiffre de caricature, le cours donne 680 000 exécutions pour toute la Grande Purge.
Révision « pour l'oreille » (06/11/2026) : le corrigé du DBQ 3 place le discours de l'Obersalzberg (22 août) « nine days
before the invasion of Poland » : dix jours (1er septembre), corrigé ; l'Axe du 25 octobre 1936 dit comme un accord ;
le 12 mars 1938, l'armée allemande entre en Autriche (Hitler n'arrive à Vienne que le 14).
Fin de l'histoire du chapitre : lien vers H3 (World War Two) et la question du chapitre (l'idéologie totalitaire
a-t-elle causé la guerre ?).
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-7"
NOTION = "Totalitarian Regimes"
NUM = 7
TITRE = "Appeasement and the road to war"
SUIVANT = "Episode 8 · Totalitarianism at the exam: essay and DBQ"
PRONONCIATION = {"Anschluss": "Ahn-shloos", "Sudetenland": "Soo-day-ten-land", "Wehrmacht": "Vair-markt",
                 "Kriegsmarine": "Kreegs-ma-reena", "Luftwaffe": "Looft-vaffa", "Heer": "Hair",
                 "Schuschnigg": "Shoosh-nik", "Seyss-Inquart": "Zice-Inkvart", "Obersalzberg": "Oh-ber-zalts-bairk",
                 "Daladier": "Da-la-dyay", "Stresa": "Stray-za", "Guernica": "Gair-nee-ka", "Lebensraum": "Lay-bens-rowm",
                 "Ribbentrop": "Ribben-trop", "Molotov": "Mollo-toff", "Krampus": "Kram-poos", "Memel": "May-mel",
                 "Führer": "Fyoo-rer", "Duce": "Doo-chay", "Mein Kampf": "Mine Kampf", "Reichstag": "Rikes-tahg",
                 "Abyssinia": "Abbi-sinnia", "Mukden": "Mook-den",
                 "798-PS": "seven nine eight P S"}


def marches(etapes):
    """L'escalier de Low (schéma h1slide) : pour chaque marche, une barre épaisse qui monte d'un cran (l'année en haut),
    puis le nom en dessous de l'axe. Les extrémités arrondies (ep 60 px) sont rentrées de 0,75 unité pour partir de
    l'axe. La dernière marche (la Pologne) est en rouge."""
    el = []
    for i, (an, nom) in enumerate(etapes, start=1):
        h_ = i + 1
        c = "ca" if i == len(etapes) else "sa"
        el.append(dict(type="droite", pts=[[i, 0.75], [i, h_ - 0.75]], c=c, ep=60, dur=0.8, lbl=an, lp=[i, h_ + 0.45]))
        el.append(dict(type="texte", x=i, y=-0.75, t=nom, c="iv"))
    return el


MARCHES = [("1931", "Manchuria"), ("1935", "Ethiopia"), ("1936", "Rhineland"), ("1938", "Anschluss"),
           ("1938", "Munich"), ("1939", "Prague"), ("1939", "Poland")]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}The first of September, nineteen thirty-nine. German troops cross into Poland. "
        "Two days later, France and Britain declare war. Twenty-one years after the Great War, Europe is at war again.",
        "{q1}Since nineteen thirty-five, Hitler had broken the Treaty of Versailles again and again. So why did nobody stop him?",
        "{-q1}{q2}And behind it, the question of the whole chapter. Did totalitarian ideology cause the war?",
        "{-q2}{-g0}{plan}Today, the last part of the chapter. {plan.1}First, the story on the map, from nineteen thirty-five to nineteen thirty-nine. "
        "{plan.2}Then part three point two: democracies unable to stop totalitarian regimes. In other words, appeasement. "
        "{plan.3}Then part three point three: the road to the Second World War, step by step. "
        "{plan.4}Then the exam: two DBQs, and one of them is for you to write. {plan.5}And finally, the answer to the chapter's question.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[37]),
        "q1": dict(type="question", t="Why did nobody stop him?", bande=True),
        "q2": dict(type="question", t="Did totalitarian ideology cause the war?", bande=True),
        "plan": dict(type="liste", titre="Episode 7 · the plan", items=[
            "The road to war on the map, 1935–1939", "III.2 · Democracies unable to stop totalitarian regimes",
            "III.3 · The road to WWII, step by step", "At the exam: DBQ 2, then DBQ 3 for you to write",
            "Did totalitarian ideology cause the war?"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 7", t="Appeasement and the road to war",
                      sous="1935 – 1939 · Parts III.2 and III.3 of the course"),
    }),

    # ================================================================ la carte : 1935-1936
    dict(id="carte1", chap="On the map: 1935 – 1936", fond="nuit", humeur="tension",
         retenir="Apr. 1935 Stresa · 1935 the Wehrmacht · June 1935 the naval agreement · 7 Mar. 1936 the Rhineland · 25 Oct. 1936 the Rome–Berlin Axis · 1936 the Spanish Civil War.",
         beats=[
        "{g1}{g1.1}Nineteen thirty-five. At Stresa, Britain and France try to build a front with Italy, against Germany. "
        "But Germany is rearming openly. And in June, Britain alone signs a naval agreement with it. "
        "Across the Atlantic, America passes its Neutrality Acts.",
        "{g1.2}The seventh of March, nineteen thirty-six. German troops march into the demilitarised Rhineland. "
        "France does not react. Neither does Britain.",
        "{g1.3}In the summer of nineteen thirty-six, civil war breaks out in Spain. Germany and Italy support General Franco. "
        "France and Britain stay out. And on the twenty-fifth of October, Germany and Italy agree on the Rome–Berlin Axis.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[25, 28, 29]),
    }),

    # ================================================================ la carte : 1937-1939
    dict(id="carte2", chap="On the map: 1937 – 1939", fond="nuit", humeur="tension",
         retenir="12 Mar. 1938 Anschluss · 29–30 Sept. 1938 Munich · 15 Mar. 1939 Prague · 31 Mar. 1939 guarantee to Poland · 23 Aug. 1939 the Nazi-Soviet pact · 1–3 Sept. 1939 war.",
         beats=[
        "{g2}{g2.1}From nineteen thirty-seven, London and Paris follow one policy. Accept the dictators' demands, in order to avoid war. "
        "It is called appeasement.",
        "{g2.2}The twelfth of March, nineteen thirty-eight. The German army marches into Austria. Austria is annexed. This is the Anschluss.",
        "{g2.3}September nineteen thirty-eight. At Munich, Britain and France hand Hitler the Sudetenland. The Czechs are not even invited.",
        "{g2.4}The fifteenth of March, nineteen thirty-nine. Germany occupies Prague, and the rest of the Czech lands. Appeasement is dead. "
        "On the thirty-first of March, France and Britain guarantee Poland.",
        "{g2.5}The twenty-third of August, nineteen thirty-nine. Two sworn enemies, Nazi Germany and the Soviet Union, sign a pact. "
        "In secret, they divide Poland between them.",
        "{g2.6}And on the first of September, Germany attacks Poland. On the third, France and Britain declare war.",
        "{-g2}{fr1}Seven dates to know by heart. {fr1.1}Nineteen thirty-five: Stresa, and the naval agreement. {fr1.2}March nineteen thirty-six: the Rhineland. "
        "{fr1.3}October nineteen thirty-six: the Axis. {fr1.4}March nineteen thirty-eight: the Anschluss. {fr1.5}September nineteen thirty-eight: Munich. "
        "{fr1.6}March nineteen thirty-nine: Prague. {fr1.7}And from August to September nineteen thirty-nine: the pact, and then the war.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[31, 33, 34, 35, 36, 37]),
        "fr1": dict(type="frise", items=[
            dict(nom="Stresa · naval agreement", d=1935, q="April–June"), dict(nom="Rhineland", d=1936, q="7 March"),
            dict(nom="The Axis", d=1936, q="25 October"), dict(nom="Anschluss", d=1938, q="12 March"),
            dict(nom="Munich", d=1938, q="29–30 Sept."), dict(nom="Prague", d=1939, q="15 March"),
            dict(nom="Pact · war", d=1939, q="23 Aug. · 1–3 Sept.")]),
    }),

    # ================================================================ III.2, idée 1 : une Europe divisée, une SDN muette
    dict(id="europe", chap="III.2 · A divided Europe, a silent League", fond="nuit", humeur="tension",
         retenir="1930s Europe: democracies (France, Britain) · dictatorships (Germany, Italy; Japan in Asia) · the USSR, vast and isolated. The League could not act without the great powers. Low, “On the Throne of Justice”, 24 July 1935.",
         beats=[
        "{eu}Now the course. Part three point two, idea one. In the nineteen-thirties, Europe is {!divided}divided into three camps. "
        "{eu.1}The democracies: France and Britain. {eu.2}The dictatorships: Germany and Italy, with Japan in Asia. "
        "{eu.3}And the Soviet Union, vast and isolated.",
        "{-eu}{sdn}Between them stands the League of Nations. It was created in nineteen nineteen to stop aggression. "
        "{sdn.1}But whenever the great powers will not back it, it {!cannot act}cannot act.",
        "{-sdn}{low1}The British cartoonist David Low made that failure his subject. In July nineteen thirty-five, "
        "Mussolini is preparing to invade Abyssinia. Low draws {low1.1}three monkeys, seated on the throne of International Law. "
        "One covers its eyes. One covers its ears. One covers its mouth. {low1.2}See no Abyssinia. Hear no Abyssinia. Speak no Abyssinia.",
    ], vis={
        "eu": dict(type="liste", titre="Europe in the 1930s: three camps", cles=["democracies", "dictatorships", "isolated"], items=[
            "The democracies: France, Britain", "The dictatorships: Germany, Italy (and Japan in Asia)",
            "The USSR: a vast and isolated totalitarian regime"], x=170, y=150, w=940),
        "sdn": dict(type="def", cles=["aggression", "great powers"], terme="The League of Nations (1919)",
                    t="The institution created in 1919 to stop aggression.",
                    etape="Unable to act whenever the great powers would not back it", x=170, y=200, w=940),
        "low1": dict(type="liste", titre="David Low, “On the Throne of Justice”, Evening Standard, 24 July 1935", items=[
            "Three monkeys labelled “Abyssinia” on the throne of International Law",
            "See no Abyssinia, hear no Abyssinia, speak no Abyssinia: the League sees, hears and says nothing"],
            x=150, y=160, w=980),
    }),

    # ================================================================ III.2, idée 2 : l'isolationnisme américain
    dict(id="usa", chap="III.2 · American isolationism", fond="nuit", humeur="calme",
         retenir="Roosevelt tried to break with isolationism, but Congress passed Neutrality Acts (1935, 1936, 1937): no arms sales, no loans to countries at war. Write “an isolationist Congress”, not “a Republican Congress”.",
         beats=[
        "{usq}Idea two. The strongest democracy stays out of Europe's crises. In the United States, President Roosevelt tries "
        "to break with isolationism. But Congress holds him back. {-usq}{us}{us.1}It passes the {!Neutrality Acts}Neutrality Acts. "
        "They forbid arms sales and loans to countries at war. {us.2}One in nineteen thirty-five. {us.3}Another in thirty-six. {us.4}And a third in thirty-seven.",
        "{-us}{rep}Watch out: here, the course corrects itself. The course slide speaks of a Republican Congress. "
        "In fact, the Democrats held the majority from nineteen thirty-five to nineteen thirty-nine. Isolationism ran across both parties. "
        "{rep.1}So in an essay, write: {!an isolationist Congress}an isolationist Congress.",
    ], vis={
        "usq": dict(type="question", t="The strongest democracy stays out."),
        "us": dict(type="liste", titre="The Neutrality Acts", cles=["arms", "loans"], items=[
            "No arms sales, no loans to countries at war", "1935: the first Neutrality Act", "1936: a second",
            "1937: a third"], x=170, y=140, w=940),
        "rep": dict(type="note", terme="Watch out · a formulation", cles=["Democrats", "both parties"],
                    t="The slide says “a Republican Congress”; the Democrats held the majority from 1935 to 1939.",
                    etape="Isolationism ran across both parties: write “an isolationist Congress”", x=170, y=200, w=940),
    }),

    # ================================================================ III.2, idées 3 et 4 : Stresa et le réarmement
    dict(id="stresa", chap="III.2 · The Stresa Front and German rearmament", fond="nuit", humeur="tension",
         retenir="April 1935: the Stresa Front (Britain, France, Italy) against Germany → Mussolini spared over Abyssinia; it collapsed. 1935: the Wehrmacht (Heer, Kriegsmarine, Luftwaffe). June 1935: the naval agreement, 35% of the Royal Navy.",
         beats=[
        "{g3}{g3.1}Idea three: the Stresa Front. In April nineteen thirty-five, at Stresa, in northern Italy, Britain and France try to build a front "
        "with Italy, against German ambitions. {sf}{sf.1}It is a calculation that weighs on everything that follows. "
        "{sf.2}To keep Mussolini away from Hitler, London and Paris are reluctant to punish him over Abyssinia. "
        "{sf.3}And the front collapses anyway. Italy turns towards Germany.",
        "{-sf}{-g3}{wm}Idea four. Germany breaks the Treaty of Versailles, openly. From nineteen thirty-five, it rearms on a massive scale. "
        "It creates a single armed force, the {!Wehrmacht}Wehrmacht, with three branches. "
        "{wm.1}The army, called the Heer. {wm.2}The navy, the Kriegsmarine. {wm.3}And the air force, the Luftwaffe. "
        "Each breach that goes unpunished makes the next one easier.",
        "{-wm}{pct}Here is the example. In June nineteen thirty-five, two months after Stresa, Britain alone signs a naval agreement with Germany. "
        "It allows the Kriegsmarine to reach {!thirty-five per cent}thirty-five per cent of the Royal Navy's tonnage. "
        "Britain itself makes a breach of Versailles legal.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[25]),
        "sf": dict(type="liste", titre="The Stresa Front, April 1935", petit=True, bande=True, x=700, y=110, w=540, items=[
            "Britain, France and Italy against German ambitions", "So Mussolini is spared over Abyssinia",
            "The front collapses: Italy turns towards Germany"]),
        "wm": dict(type="liste", titre="1935 · the Wehrmacht, a unified armed force", items=[
            "The army: the Heer", "The navy: the Kriegsmarine", "The air force: the Luftwaffe"], x=170, y=150, w=940),
        "pct": dict(type="mot", t="35%", g="June 1935 · the Kriegsmarine allowed 35% of the Royal Navy's tonnage", y=240, taille=150),
    }),

    # ================================================================ III.2, idée 5 : l'appeasement
    dict(id="appease", chap="III.2 · Appeasement, case study 3", fond="nuit", humeur="tension",
         retenir="Key term · appeasement: Chamberlain (from 1937) and Daladier accepted the Axis demands to avoid war. What it gave away: 1935 naval agreement · 1935 no oil embargo on Italy · 1936 no reaction in the Rhineland · 1938 Munich.",
         beats=[
        "{photo1}{def1}Idea five. This is case study number three, and a key term of the chapter: {!appeasement}appeasement. "
        "It means the efforts of the British prime minister, Neville Chamberlain, from nineteen thirty-seven. "
        "And those of his French counterpart, Édouard Daladier. Both tried to avoid war, by accepting the demands of the Axis powers. "
        "{def1.1}In doing so, the democracies gave up the goals they had set themselves in nineteen nineteen. Germany, Italy and Japan were not halted. "
        "And yet their militarism openly contradicted the peace settlement.",
        "{-def1}{-photo1}{ced}Here is the first column of the course's schema: what appeasement gave away. "
        "{ced.1}In nineteen thirty-five, the Anglo-German Naval Agreement. "
        "{ced.2}The same year, Britain refuses an oil embargo. It was the one sanction that would have stopped Mussolini in Ethiopia. "
        "{ced.3}In March nineteen thirty-six, no reaction when Hitler sends troops into the demilitarised Rhineland. "
        "{ced.4}And in nineteen thirty-eight, Munich. The Sudetenland is handed over, without the Czechs.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-munich", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Chamberlain, Daladier, Hitler, Mussolini and Ciano before signing the Munich Agreement, 29 September 1938 · Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE"),
        "def1": dict(type="def", cles=["avoid war", "demands"], terme="Key term · appeasement",
                     t="Avoiding war by accepting the demands of the Axis powers: Chamberlain (from 1937), Daladier.",
                     etape="The goals of 1919 abandoned: Germany, Italy and Japan not halted", x=170, y=200, w=940),
        "ced": dict(type="liste", titre="Appeasement · what was given away", items=[
            "1935 · Anglo-German Naval Agreement: the Kriegsmarine at 35% of the Royal Navy",
            "1935 · Refusal of the oil embargo that would have stopped Mussolini in Ethiopia",
            "1936 · No reaction to the remilitarisation of the Rhineland",
            "1938 · Munich: the Sudetenland handed over without the Czechs"], x=130, y=130, w=1020),
    }),

    # ================================================================ III.2, idée 6 : pourquoi l'appeasement
    dict(id="pourquoi", chap="III.2 · Why appeasement seemed reasonable", fond="aube", humeur="calme",
         retenir="Seven reasons: pacifism (1914–18; the Oxford Union, Feb. 1933) · the Commonwealth (Canada) · an empire to police (India) · Germany mistreated in 1919 · the Depression first · American isolationism · fear of communism. Discredited today, popular then.",
         beats=[
        "{qw}Idea six. Today, appeasement is widely seen as a policy of weakness. But at the time, it was popular. And it seemed pragmatic. "
        "{-qw}{wh}The second column of the schema gives seven reasons. "
        "{wh.1}One. The memory of the slaughter of nineteen fourteen to eighteen. Both countries were deeply pacifist. "
        "{wh.2}Two. Britain feared that the Commonwealth would not follow it a second time. The course's example is Canada. "
        "{wh.3}Three. Britain was busy policing its empire, India for example. It could not afford a major rearmament.",
        "{wh.4}Four. Many Britons felt that Germany had been treated unfairly in nineteen nineteen. "
        "{wh.5}Five. Both countries gave priority to their own economic problems: the Depression. "
        "{wh.6}Six. They felt unprotected, because America was isolationist. "
        "{wh.7}And seven. Many feared communism more than fascism.",
        "{-wh}In February nineteen thirty-three, the Oxford Union votes:",
        ("C", "This House will in no circumstances fight for its King and Country.", "c_ox"),
        "So, in an essay, say both. {-c_ox}{deux}{deux.g}Discredited today, because each concession was followed by a larger demand. "
        "{deux.d}But popular then, because it rested on solid reasons, and on public opinion.",
    ], vis={
        "qw": dict(type="question", t="Weakness… or pragmatism?"),
        "wh": dict(type="liste", titre="Why appeasement? The seven reasons of the course", petit=True, items=[
            "The memory of 1914–1918: pacifism", "Fear that the Commonwealth (Canada) would not follow a second time",
            "An empire to police (India): no massive rearmament", "Sympathy for a Germany felt mistreated in 1919",
            "The economic problems of the Depression, given priority", "American isolationism, which left them unprotected",
            "Fear of communism, stronger than fear of fascism"], x=130, y=90, w=1020),
        "c_ox": dict(type="cit", a="The Oxford Union", o="motion voted in February 1933", x=200, y=210, w=880),
        "deux": dict(type="cols", g="Discredited today", gq="a policy of weakness: each concession, a larger demand",
                     d="Popular then", dq="pacifism, empire, the Depression, fear of communism", vs="+",
                     repere="A good essay says both"),
    }),

    # ================================================================ III.2, idée 7 : Munich
    dict(id="munich", chap="III.2 · Munich, 1938", fond="guerre", humeur="tension",
         retenir="29–30 Sept. 1938, Munich: Hitler, Chamberlain, Daladier, Mussolini. The Sudetenland (≈ 3 million German speakers) handed over; the Czechs not invited; Hitler promises not to threaten the rest of Czechoslovakia. Low: Hitler as Krampus (10 Oct. 1938).",
         beats=[
        "{g4}{g4.1}Idea seven: Munich, nineteen thirty-eight. Hitler demands the Sudetenland, the German-speaking region of Czechoslovakia. "
        "About three million German speakers live there. {mu}{mu.1}Czechoslovakia is the only democracy left in central Europe. "
        "And Hitler threatens to invade the whole country.",
        "{mu.2}The conference meets on the twenty-ninth and thirtieth of September. Around the table: Hitler, Chamberlain, Daladier, and Mussolini. "
        "Mussolini poses as a moderate working for peace. In fact, he helps Germany get what it wants. "
        "{mu.3}And the Czechs? They are {!not invited}not invited. "
        "{mu.4}Britain and Germany promise not to go to war. And Hitler promises he will never threaten the rest of Czechoslovakia.",
        "{-mu}{-g4}{low2}David Low did not believe that promise. On the tenth of October, ten days after Munich, he draws Hitler as Krampus. "
        "Krampus is the demon who terrorises children at Christmas. {-low2}And the caption reads:",
        ("C", "Europe can look forward to a Christmas of Peace", "c_low"),
        "{-c_low}{photo2}{iro}The irony is bitter. The peace bought at Munich would last {!less than six months}less than six months.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[34]),
        "mu": dict(type="liste", titre="Munich, 29–30 September 1938", petit=True, bande=True, x=700, y=110, w=540, items=[
            "Czechoslovakia: the last democracy in central Europe", "Hitler, Chamberlain, Daladier, Mussolini “the moderate”",
            "The Czechs are not invited", "Hitler promises not to threaten the rest of the country"]),
        "low2": dict(type="note", terme="David Low, cartoon of 10 October 1938", cles=["Krampus"],
                     t="Hitler drawn as Krampus, the demon who terrorises children at Christmas.",
                     etape="Ten days after Munich: the cartoonist does not believe the promise", x=170, y=120, w=940),
        "c_low": dict(type="cit", a="David Low", o="cartoon caption, 10 October 1938", x=200, y=330, w=880),
        "photo2": dict(type="tableau", img="h2-heston", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Chamberlain waves the Anglo-German declaration at Heston airport, 30 September 1938 · Imperial War Museums, D 2239, public domain"),
        "iro": dict(type="mot", t="< 6 months", g="Munich, 30 Sept. 1938 → Prague, 15 March 1939", y=250, taille=110),
    }),

    # ================================================================ DBQ 2 (présenté plus brièvement)
    dict(id="dbq2", chap="DBQ 2 · Roosevelt's telegram", fond="aube", humeur="calme",
         retenir="DBQ 2: largely useful for the American response in spring 1939 (author, date, method: “assurance” without sanction, a tally of failures, public diplomacy) · limits: one neutral democracy, no outcome, silent on the Neutrality Acts, written for publication.",
         beats=[
        "{doc2}Now, the second DBQ of the chapter. {doc2.1}It is a telegram from President Roosevelt to Hitler, "
        "dated the fourteenth of April, nineteen thirty-nine. The same text went to Mussolini. "
        "{doc2.2}One month after Prague, Roosevelt asks the dictators for an assurance. "
        "They must promise not to attack thirty-one named states, from Finland to Iran. "
        "{doc2.3}But there is no sanction. No alliance. No threat of force. {-doc2}He writes:",
        ("C", "Three nations in Europe and one in Africa have seen their independent existence terminated.", "c_fdr1"),
        "That means Austria, Czechoslovakia, Albania and Ethiopia. {-c_fdr1}And he warns the dictators:",
        ("C", "History will hold them accountable.", "c_fdr2"),
        "{-c_fdr2}{ex2}The question: {!How useful}how useful is this document to a historian studying the democracies' response to Hitler's ambitions?",
        "{-ex2}{m2}Here is the site's model, in short. {m2.1}Largely useful, although it lights only one corner of that response. "
        "{m2.2}The strengths. The author is the head of the most powerful neutral democracy. The date comes just after Prague. "
        "It asks for assurances, without any constraint. Its list of thirty-one states admits how far aggression was expected to reach. "
        "And it is a public message.",
        "{m2.3}The limits. Nothing on Britain and France. No outcome, since Hitler's reply of the twenty-eighth of April is missing. "
        "Nothing on the Neutrality Acts. And it was written for publication.",
        "{-m2}{pie}{!Watch out}And watch out for the trap. The question says the democracies, plural. A document from just one of them "
        "can only be partly representative. Say so, and bring in Britain and France from your own knowledge.",
    ], vis={
        "doc2": dict(type="liste", titre="DBQ 2 · Document A", items=[
            "Roosevelt to Hitler, telegram, the White House, 14 April 1939 (the same to Mussolini)",
            "An “assurance” requested for 31 named states, from Finland to Iran",
            "No sanction, no alliance, no threat of force"], x=150, y=140, w=980),
        "c_fdr1": dict(type="cit", a="Franklin D. Roosevelt", o="telegram to Hitler, 14 April 1939 (DBQ 2)", x=200, y=210, w=880),
        "c_fdr2": dict(type="cit", a="Franklin D. Roosevelt", o="telegram to Hitler, 14 April 1939 (DBQ 2)", x=200, y=230, w=880),
        "ex2": dict(type="exo", niveau="dbq", titre="How useful is Document A to a historian studying the democracies' response to Hitler's ambitions?",
                    src="DBQ 2 of the site (chapter H2)", enonce=["Part a) of a DBQ · 10 marks, about 35 minutes"]),
        "m2": dict(type="liste", titre="DBQ 2 · the model answer in short", petit=True, items=[
            "Largely useful… but it lights only one corner of the response",
            "Strengths: author · date (after Prague, Albania) · “assurance” without sanction · 31 states · public diplomacy",
            "Limits: one neutral democracy · no outcome (Hitler's reply, 28 April) · silent on the Neutrality Acts · written for publication"],
            x=130, y=130, w=1020),
        "pie": dict(type="note", terme="Watch out · the trap", cles=["plural", "Britain and France"],
                    t="“The democracies”, plural: one document from one democracy can only be partly representative.",
                    etape="Say so, and bring in Britain and France from your own knowledge", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idées 1 et 2 : l'Axe et l'Espagne
    dict(id="axe", chap="III.3 · The Axis and the Spanish Civil War", fond="guerre", humeur="tension",
         retenir="25 Oct. 1936: the Rome–Berlin Axis, an alliance of interest between two dictators who distrusted each other (Pact of Steel 1939, Japan 1940). Spain 1936: Germany and Italy back Franco, the Luftwaffe tests itself; France and Britain stay out.",
         beats=[
        "{g5}{g5.1}Part three point three: the road to the Second World War. Idea one, the Axis. Hitler needed allies. "
        "He found one in Mussolini, despite a certain mutual disdain. "
        "Hitler had long admired Fascism. But Mussolini saw him as an ambitious and pretentious rival. "
        "In nineteen thirty-two, he even mocked Nazi racism:",
        "{-g5}",
        ("C", "Racism is blondes' stuff!", "c_mus"),
        "{-c_mus}{ax}{ax.g}So why become allies? Because Italy was economically too weak to face the democracies alone. Mussolini needed German support. "
        "The Rome–Berlin Axis was declared on the twenty-fifth of October, nineteen thirty-six. {ax.d}It became a military alliance, the Pact of Steel, in nineteen thirty-nine. "
        "And Japan joined in nineteen forty. An alliance of interest, not of friendship.",
        "{-ax}{g6}{g6.1}{es}Idea two: Spain. {es.1}Civil war broke out in Spain in nineteen thirty-six. Germany and Italy supported General Franco's nationalists. "
        "{es.2}And Germany used the conflict to test its air force. "
        "{es.3}France and Britain did not intervene to help the Spanish Republic. "
        "{es.4}Here is an example the course adds, from outside the lesson. In April nineteen thirty-seven, German bombers destroyed "
        "the Basque town of Guernica. Picasso painted it that same year.",
        "{-es}{-g6}{photo3}{rep2}Spain was a rehearsal of the coming war. And one more proof that the democracies would not act.{-photo3}",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[29]),
        "c_mus": dict(type="cit", a="Benito Mussolini", o="1932, quoted in the course", x=200, y=230, w=880),
        "ax": dict(type="cols", g="Mutual disdain", gq="Hitler admired Fascism; Mussolini saw a pretentious rival",
                   d="Mutual need", dq="Italy too weak alone: the Axis (Oct. 1936), the Pact of Steel (1939), Japan (1940)", vs="→",
                   repere="An alliance of interest"),
        "g6": dict(type="globe", code="H2", sc=[29]),
        "es": dict(type="liste", titre="Spain, 1936", petit=True, bande=True, x=780, y=110, w=470, items=[
            "Germany and Italy back Franco's nationalists", "The German air force tested in Spain",
            "France and Britain do not help the Republic", "Guernica, 26 April 1937 (not in the lesson)"]),
        "photo3": dict(type="tableau", img="h2-guernica", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="The ruins of Guernica after the bombing of 26 April 1937 (not in the lesson) · Bundesarchiv, Bild 183-H25224, CC BY-SA 3.0 DE"),
        "rep2": dict(type="mot", t="A rehearsal", g="of the coming war · the democracies would not act", y=260, taille=100),
    }),

    # ================================================================ III.3, idée 3 : la Rhénanie
    dict(id="rhenanie", chap="III.3 · The Rhineland, 1936", fond="nuit", humeur="tension",
         retenir="7 Mar. 1936: a calculated risk. Troops too weak to resist the French army, under orders to retreat if France reacted. No reaction: the gamble paid off, and taught Hitler that the democracies would yield. Low, “Stepping Stones to Glory” (1936).",
         beats=[
        "{g7}{g7.1}Idea three: the Rhineland, on the seventh of March, nineteen thirty-six. Reoccupying this demilitarised zone was a calculated risk.",
        "{rh}{rh.1}The German troops were not strong enough to resist the French army, if France reacted. "
        "{rh.2}They had strict orders to retreat if it did. "
        "{rh.3}But France and Britain were not keen to fight Germany. There was no resistance.",
        "{-rh}{-g7}{pari}Hitler's gamble paid off. And above all, {!it taught him}it taught him that the democracies would yield.",
        "{-pari}{low3}That same year, David Low drew a cartoon called Stepping Stones to Glory. Hitler climbs towards his goals "
        "on the bent backs of the democracies' leaders. Low calls them the spineless leaders of democracy. "
        "{low3.1}Each back is a step. Keep that image in mind. We will climb those steps at the end of this part.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[28]),
        "rh": dict(type="liste", titre="7 March 1936 · a calculated risk", petit=True, bande=True, x=700, y=110, w=540, items=[
            "German troops too weak to resist the French army", "Strict orders to retreat if France reacted",
            "France and Britain did not move"]),
        "pari": dict(type="question", t="The gamble paid off."),
        "low3": dict(type="note", terme="David Low, “Stepping Stones to Glory”, 1936", cles=["bent backs", "spineless"],
                     t="Hitler climbs towards his goals on the bent backs of “the spineless leaders of democracy”.",
                     etape="Each concession, a step: the schema at the end of this part follows them to 1939", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idée 4 : l'Anschluss
    dict(id="anschluss", chap="III.3 · The Anschluss, 1938", fond="nuit", humeur="tension",
         retenir="Hitler bullied Schuschnigg and massed troops on the border → Seyss-Inquart chancellor, invites the German army → Austria, 12 Mar. 1938 → a plebiscite without opponents and Jews: 99% yes. Britain and France did nothing.",
         beats=[
        "{g8}{g8.1}Idea four: the Anschluss, the annexation of Austria. It happens in four steps. "
        "{an}{an.1}First, pressure. In speech after speech, Hitler bullies the Austrian chancellor, Schuschnigg. He moves troops to the border. "
        "And he threatens to invade, unless Schuschnigg resigns in favour of a Nazi, Seyss-Inquart. "
        "{an.2}Second, Seyss-Inquart becomes chancellor, and he invites German troops into Austria. "
        "{an.3}Third, on the twelfth of March, nineteen thirty-eight, the German army marches in. "
        "Hitler has broken Versailles once again. And Britain and France do nothing.",
        "{an.4}Fourth, a referendum approves the annexation. But political enemies and Jews are not allowed to vote.",
        "{-an}{-g8}{photo4}{oui}And the result?",
        ("P", 0.6),
        "{-oui}{pct2}{!99 per cent}Ninety-nine per cent yes. A controlled vote, to dress up an annexation made by pressure.",
        "{-pct2}{-photo4}{huit}Handle one figure with care. The course says that Jewish Austrians, eight per cent of the population, could not vote. "
        "{huit.1}Eight per cent is best read as the share of people excluded from the vote: opponents and Jews together. "
        "Jews alone were about three Austrians in a hundred, most of them in Vienna. That figure is from outside the course.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[33]),
        "an": dict(type="liste", titre="The Anschluss in four steps", petit=True, bande=True, x=780, y=110, w=470, items=[
            "Pressure: Schuschnigg bullied, troops on the border", "Seyss-Inquart chancellor: he invites the German army",
            "12 March 1938: the German army enters Austria", "A plebiscite without opponents and Jews"]),
        "photo4": dict(type="tableau", img="h2-anschluss", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Hitler addresses the crowd on the Heldenplatz, Vienna, 15 March 1938 · Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE"),
        "oui": dict(type="question", t="The plebiscite: the result?"),
        "pct2": dict(type="mot", t="99% yes", g="a controlled vote · opponents and Jews excluded", y=240, taille=140),
        "huit": dict(type="note", terme="Watch out · a figure", cles=["excluded", "three"],
                     t="8%: the share of people excluded from the vote, opponents and Jews together, not of Jews alone.",
                     etape="Jews: about 3% of Austrians, most of them in Vienna (outside the course)", x=170, y=200, w=940),
    }),

    # ================================================================ III.3, idée 5 : Prague
    dict(id="prague", chap="III.3 · Prague, March 1939", fond="guerre", humeur="tension",
         retenir="15 Mar. 1939: Germany occupies Prague. Hitler had lied at Munich; no longer uniting Germans but occupying a foreign people → end of appeasement: guarantees to Poland (31 Mar.), Romania, Greece.",
         beats=[
        "{g9}{g9.1}Idea five: Prague. On the fifteenth of March, nineteen thirty-nine, Germany occupies Prague and invades the rest of Czechoslovakia. "
        "Hitler has proved that he {!lied at Munich}lied at Munich.",
        "{-g9}{diff}{diff.g}And this time, the conquest cannot be presented as uniting Germans. "
        "{diff.d}It is the occupation of a foreign people. Appeasement is over.",
        "{-diff}{gar}Britain and France change course. {gar.1}They pledge to protect Romania, Greece and Poland, "
        "if Germany or Italy attacks them. {gar.2}The guarantee to Poland is given on the thirty-first of March. "
        "{gar.3}And it is this commitment that will bring both countries into the war, five months later.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[35]),
        "diff": dict(type="cols", g="Until Munich", gq="Rhineland, Austria, Sudetenland: “uniting Germans”",
                     d="Prague, 15 March 1939", dq="the occupation of a foreign people", vs="≠",
                     repere="The lie of Munich ends appeasement"),
        "gar": dict(type="liste", titre="The democracies change course", items=[
            "Guarantees to Romania, Greece and Poland, if attacked by Germany or Italy",
            "31 March 1939: the guarantee to Poland", "The commitment that brings them into the war in September"],
            x=150, y=150, w=980),
    }),

    # ================================================================ III.3, idée 6 : le pacte germano-soviétique
    dict(id="pacte", chap="III.3 · The Nazi-Soviet pact", fond="guerre", humeur="tension",
         retenir="23 Aug. 1939: a non-aggression pact; in secret, Poland divided. Hitler: no war on two fronts. Stalin, his army gutted by the purges: time and territory. 1 Sept. 1939: Poland attacked; 3 Sept.: France and Britain declare war.",
         beats=[
        "{g10}{g10.1}Idea six. On the twenty-third of August, nineteen thirty-nine, Germany signs a non-aggression pact with the Soviet Union. "
        "Its secret terms plan to divide Poland between them. Two ideological enemies make a deal of {!pure interest}pure interest.",
        "{-g10}{photo5}{gain}{gain.g}For Hitler, it removes the threat of a war on two fronts. "
        "{gain.d}For Stalin, whose army has just been gutted by the purges, it buys time, and territory.",
        "{-gain}The cartoon in the course gives Stalin this line:",
        ("C", "I am not ready for war! I just killed 700,000 of my finest officers and communist leaders!", "c_car"),
        "{-c_car}{-photo5}{chif}That is a cartoon's figure. The course gives about six hundred and eighty thousand executions "
        "for the whole Great Purge. And far from all of them were officers. But the point stands: the Red Army was not ready.",
        "{-chif}{g11}{g11.1}Now nothing stands in the way. On the first of September, Germany attacks Poland, France's ally. "
        "On the third, France and Britain declare war. {!War}The war has begun.",
    ], vis={
        "g10": dict(type="globe", code="H2", sc=[36]),
        "photo5": dict(type="tableau", img="h2-pact", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .3],
                       legende="Stalin and Ribbentrop after signing the German-Soviet Non-Aggression Pact, Moscow, 23 August 1939 · Bundesarchiv, Bild 183-H27337 / Helmut Laux, CC BY-SA 3.0 DE"),
        "gain": dict(type="cols", g="Hitler", gq="no war on two fronts: the attack on Poland can begin",
                     d="Stalin", dq="an army gutted by the purges: time and territory", vs="+",
                     repere="23 August 1939 · a deal of pure interest"),
        "c_car": dict(type="cit", a="Stalin, in a cartoon", o="cartoon shown in the course", x=200, y=210, w=880),
        "chif": dict(type="note", terme="Watch out · a cartoon's figure", cles=["680,000", "officers"],
                     t="The course: ≈ 680,000 executions in the whole Great Purge (1937–38), far from all officers.",
                     etape="The point stands: the Red Army was not ready", x=170, y=200, w=940),
        "g11": dict(type="globe", code="H2", sc=[37]),
    }),

    # ================================================================ III.3, idée 7 : la chaîne
    dict(id="chaine", chap="III.3 · Each aggression prepared the next", fond="nuit", humeur="tension",
         retenir="The chain: 1931 Manchuria · 1933 Germany and Japan leave the League · 1935 Ethiopia · 1936 Rhineland, Spain · 1937 China, Italy leaves the League · 1938 Anschluss, Munich · March 1939 Prague · 1 Sept. 1939 Poland. Ideology = the will; the democracies' reluctance = the opportunity.",
         beats=[
        "{st}Idea seven: the consequence of appeasement. Let's climb David Low's steps, as the course's schema does. "
        "{st.1}{st.2}Nineteen thirty-one: Manchuria. No sanction. "
        "{st.3}{st.4}Nineteen thirty-five: Ethiopia. Britain refuses the oil embargo. "
        "{st.5}{st.6}Nineteen thirty-six: the Rhineland. France and Britain do not move.",
        "{st.7}{st.8}March nineteen thirty-eight: the Anschluss. {st.9}{st.10}September nineteen thirty-eight: Munich. "
        "{st.11}{st.12}March nineteen thirty-nine: Prague. Munich bought nothing. "
        "{st.13}{st.14}And the first of September, nineteen thirty-nine: Poland. War. "
        "Every concession was followed by a {!larger demand}larger demand. That is the central argument against appeasement.",
        "{-st}{ch}The course's chain fills in the years between. {ch.1}Nineteen thirty-three: Germany and Japan leave the League. {ch.2}Nineteen thirty-five: Ethiopia. "
        "{ch.3}Nineteen thirty-six: the Rhineland, and Spain. {ch.4}Nineteen thirty-seven: Japan invades southern China, and Italy leaves the League. "
        "{ch.5}{ch.6}{ch.7}Then Austria, Munich, Prague, and Poland. Each time, the lack of any reaction encouraged the next step.",
        "{-ch}{vo}Here is the sentence that answers the chapter's key issue. "
        "{vo.g}Totalitarian ideology supplied {!the will}the will to expand. "
        "{vo.d}The democracies' reluctance supplied {!the opportunity}the opportunity.",
        ("P", 2.0),
    ], vis={
        "st": dict(type="graphe", titre="Stepping stones to war, 1931–1939 (after David Low, 1936)", x=140, y=100, w=1000, h=540,
                   ax=dict(x=[0.4, 7.6], y=[0, 9.2], gx=[], gy=[], lx="", ly=""), el=marches(MARCHES)),
        "ch": dict(type="liste", titre="The chain in the course", petit=True, items=[
            "1933 · Germany and Japan leave the League", "1935 · Italy invades Ethiopia", "1936 · The Rhineland; Spain",
            "1937 · Japan invades southern China; Italy leaves the League", "1938 · The Anschluss; Munich", "March 1939 · Prague",
            "1 September 1939 · Poland"], x=150, y=100, w=980),
        "vo": dict(type="cols", g="Totalitarian ideology", gq="the will to expand: war as a value, Lebensraum, empire",
                   d="The democracies' reluctance", dq="the opportunity: the League, appeasement, isolationism", vs="+",
                   repere="The answer to the key issue"),
    }),

    # ================================================================ à toi : DBQ 3 a)
    dict(id="dbq3a", chap="Your turn · DBQ 3, part a)", fond="guerre", humeur="tension",
         retenir="DBQ 3 a): largely useful · Hitler to his commanders, Obersalzberg, 22 Aug. 1939 · strengths: closed audience, date, planning, his reading of the democracies, near-silence on Lebensraum · limits: listeners' notes (798-PS), purpose, immediate not underlying, silences, intention only.",
         beats=[
        "{doc3}Now it is your turn, with the third DBQ of the chapter. {doc3.1}The document is a speech by Adolf Hitler to his commanders-in-chief. "
        "He gave it at the Obersalzberg, his mountain residence, on the twenty-second of August, nineteen thirty-nine. Ten days before the invasion of Poland. "
        "{doc3.2}It was a closed military briefing. We know it through notes taken by listeners, which were produced at the Nuremberg trials "
        "as document 798-PS. {-doc3}Hitler says:",
        ("C", "A conflict with Poland had to come sooner or later.", "c_h1"),
        "{-c_h1}About his opponents, he says:",
        ("C", "There is no outstanding personality in England and France.", "c_h2"),
        "{-c_h2}And finally:",
        ("C", "We have nothing to lose; we have everything to gain.", "c_h3"),
        "{-c_h3}{ex3}The question: {!How useful}how useful is this document to a historian studying the role of territorial expansionism "
        "as an underlying cause of World War Two?",
        "{-ex3}{str}Remember the structure. {str.1}Your judgement in the first line: largely, significantly, partly, or slightly useful. "
        "{str.2}Then the document, in one sentence. {str.3}A paragraph of strengths, with several arguments. {str.4}And a paragraph of limits, with several arguments.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep3}Here is a model, from the site's answer. {rep3.1}Document A is largely useful to a historian studying territorial expansionism "
        "as an underlying cause of the war. But it captures the last step, rather than the road. "
        "{rep3.2}It is a speech delivered by Hitler to his commanders-in-chief on the twenty-second of August, nineteen thirty-nine. "
        "In it, he tells them he has decided to attack Poland.",
        "{rep3.3}Now the strengths. A closed audience: Hitler had no reason to soften his intentions. "
        "The date: the exact point where expansion became war. Planning, not improvisation: a conflict had to come sooner or later. "
        "The effect of appeasement: no outstanding personality in England and France. "
        "And something he did not mean to reveal. He barely mentions Lebensraum, or race.",
        "{rep3.4}Then the limits. These are listeners' notes, in several versions, produced at Nuremberg. So it is not a word-for-word text. "
        "Its purpose was to reassure the generals, so Hitler overstates German advantages. "
        "It shows an immediate decision, not an underlying cause. For that, you need Mein Kampf. "
        "It says nothing on the economy, on race, or on the League. And it shows an intention, never what actually happened.",
    ], vis={
        "doc3": dict(type="liste", titre="DBQ 3 · Document A", items=[
            "Hitler to his commanders-in-chief, Obersalzberg, 22 August 1939: ten days before Poland",
            "A closed briefing, known through listeners' notes (Nuremberg document 798-PS)"], x=150, y=150, w=980),
        "c_h1": dict(type="cit", a="Adolf Hitler", o="speech at the Obersalzberg, 22 August 1939 (DBQ 3)", x=200, y=210, w=880),
        "c_h2": dict(type="cit", a="Adolf Hitler", o="speech at the Obersalzberg, 22 August 1939 (DBQ 3)", x=200, y=210, w=880),
        "c_h3": dict(type="cit", a="Adolf Hitler", o="speech at the Obersalzberg, 22 August 1939 (DBQ 3)", x=200, y=210, w=880),
        "ex3": dict(type="exo", niveau="dbq", titre="How useful is Document A to a historian studying the role of territorial expansionism as an underlying cause of World War Two?",
                    src="DBQ 3 of the site (chapter H2)", enonce=["Part a) of a DBQ · 10 marks, about 35 minutes"],
                    donnees=["Hitler, Obersalzberg, 22 Aug. 1939: “a conflict with Poland had to come sooner or later” … “We have nothing to lose; we have everything to gain”"]),
        "str": dict(type="liste", titre="DBQ a): the structure", cles=["judgement", "sentence", "strengths", "limits"], items=[
            "First line: the judgement (largely / significantly / partly / slightly useful)", "The document in one sentence",
            "A paragraph of strengths, several arguments", "A paragraph of limits, several arguments"], x=150, y=130, w=980),
        "pa1": dict(type="pause", t="Write your first line, the sentence that presents the document, then the strengths and the limits.",
                    sous="Pause the video, write your answer, then play on for a model."),
        "rep3": dict(type="liste", titre="A model answer", petit=True, items=[
            "Largely useful… but the last step rather than the road", "Hitler to his commanders-in-chief, 22 Aug. 1939: he has decided to attack Poland",
            "Strengths: closed audience · date · planning · his reading of the democracies · near-silence on Lebensraum",
            "Limits: listeners' notes (798-PS) · purpose · immediate, not underlying · silences · intention only"],
            x=130, y=130, w=1020),
    }),

    # ================================================================ à toi : DBQ 3 b)
    dict(id="dbq3b", chap="Your turn · DBQ 3, part b)", fond="nuit", humeur="tension",
         retenir="DBQ 3 b): ideology made war a value and expansion a goal (Fascism, Lebensraum, Japan) · but the democracies let aggression succeed (League, appeasement, isolationism) · the two combined into a chain only war could break → ideology the will, the democracies the opportunity.",
         beats=[
        "{ex4}Now part b). It goes beyond the document, with your own knowledge. Here is a question written for this video, on the chapter's key issue. "
        "{!To what extent}To what extent was totalitarian ideology the main cause of the Second World War?",
        "{-ex4}{pa2}",
        ("P", 2.0),
        "{-pa2}{pb}A model plan, taken from the course's essay on the key issue. {pb.1}In the introduction, define totalitarianism. "
        "Then define the peace it threatened: the order of nineteen nineteen, guarded by the League of Nations. Then, three parts.",
        "{pb.2}Part one. Totalitarian ideologies made war a value, and expansion a goal. Fascism made war the supreme test: Abyssinia, in nineteen thirty-five. "
        "Nazism turned Lebensraum into a plan, in Mein Kampf. Japan sought autarky: Manchuria, then Nanjing.",
        "{pb.3}Part two. But the democracies let aggression succeed. Over Abyssinia, the League debated sanctions, and spared oil. "
        "Then came appeasement: the naval agreement, the Rhineland, Munich. And American isolationism, with the Neutrality Acts of nineteen thirty-five to thirty-seven.",
        "{pb.4}Part three. The two combined into a chain that only war could break. The Rhineland taught Hitler that the democracies would yield. "
        "Prague ended appeasement. And the Nazi-Soviet pact opened the way to Poland.",
        "{pb.5}And the judgement. Totalitarian ideology was the main cause, because it supplied the will to war. "
        "But it was not the only one. The democracies' reluctance supplied the opportunity.",
    ], vis={
        "ex4": dict(type="exo", niveau="dbq", titre="To what extent was totalitarian ideology the main cause of the Second World War?",
                    src="Question written for this video, on the chapter's key issue", enonce=["Part b) of a DBQ · the document + your own knowledge"]),
        "pa2": dict(type="pause", t="Write a plan: three parts, one example each, and a judgement.",
                    sous="Pause the video, write your plan, then play on for a model."),
        "pb": dict(type="liste", titre="A model plan", petit=True, items=[
            "Introduction: define totalitarianism · the peace of 1919, guarded by the League",
            "Ideology made war a value: Abyssinia 1935 · Lebensraum (Mein Kampf) · Japan's autarky · the Obersalzberg speech",
            "But the democracies let aggression succeed: the League and oil · appeasement · the Neutrality Acts",
            "The two formed a chain only war could break: Rhineland → Prague → the pact → Poland",
            "Judgement: the main cause (the will), not the only one (the opportunity)"], x=130, y=120, w=1020),
    }),

    # ================================================================ conclusion : l'idéologie a-t-elle causé la guerre ?
    dict(id="conclusion", chap="Did totalitarian ideology cause the war?", fond="aube", humeur="lumiere",
         retenir="The chapter's answer: totalitarian ideology supplied the will to war; the democracies' reluctance supplied the opportunity. Keep both halves. Next: chapter H3, World War Two.",
         beats=[
        "{qc}So, back to the question of the whole chapter. Did totalitarian ideology cause the war?",
        "{-qc}{rep4}{rep4.g}Yes, to a large extent. The three regimes were built on ideologies that made war a value, and expansion a goal. "
        "The nation and Rome's empire. The race and its living space. And Japan's empire in Asia. "
        "{rep4.d}But not alone. Between nineteen thirty-five and nineteen thirty-nine, each aggression succeeded because the democracies let it succeed. "
        "A strong answer keeps {!both halves}both halves.",
        "{-rep4}{lien}And this is where the next chapter begins. Chapter three: World War Two. "
        "{lien.1}The war that starts in Poland is the war of these regimes. "
        "{lien.2}The fall of France, in nineteen forty. {lien.3}Barbarossa, in nineteen forty-one: a war of annihilation for living space in the East. "
        "{lien.4}And the genocide of the Jews of Europe. The ideologies of this chapter, put into practice by war.",
    ], vis={
        "qc": dict(type="question", t="Did totalitarian ideology cause the war?"),
        "rep4": dict(type="cols", g="Yes, largely", gq="ideologies that made war a value and expansion a goal",
                     d="But not alone", dq="each aggression succeeded because the democracies let it", vs="+",
                     repere="The will + the opportunity"),
        "lien": dict(type="liste", titre="Next chapter · H3 World War Two", items=[
            "September 1939: the war of these regimes begins", "1940: the fall of France",
            "1941: Barbarossa, a war of annihilation for Lebensraum", "The genocide of the Jews of Europe"], x=170, y=140, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}A silent League, and an isolationist America. "
        "{carte.2}Appeasement: Chamberlain and Daladier, seven reasons, and Munich. "
        "{carte.3}The steps: the Axis, the Rhineland, the Anschluss, Prague, and the pact. "
        "{carte.4}And the answer: ideology supplied the will, the democracies the opportunity.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the whole chapter at the exam. Essays, DBQs, model answers. And the traps.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="THE ROAD TO WAR", branches=[
            dict(t="III.2 · Powerless", items=["a silent League", "Neutrality Acts 1935–37", "Stresa · 35% naval deal"]),
            dict(t="Appeasement", items=["Chamberlain, Daladier", "seven reasons", "Munich, Sept. 1938"]),
            dict(t="III.3 · Steps", items=["Axis · Spain 1936", "Rhineland · Anschluss", "Prague · the pact 1939"]),
            dict(t="The answer", items=["ideology: the will", "democracies: the opportunity", "3 Sept. 1939: war"])]),
        "fin": dict(type="mot", t="Next: the chapter at the exam", g="Episode 8 · essay and DBQ", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="What does David Low's cartoon of 24 July 1935, “On the Throne of Justice”, denounce?",
         r=["The League of Nations seeing, hearing and saying nothing about Abyssinia", "The Anschluss",
            "The Nazi-Soviet pact", "American isolationism"], ok=0, voir="low1",
         ex="Three monkeys labelled “Abyssinia” on the throne of International Law: see no, hear no, speak no Abyssinia."),
    dict(q="What did the US Neutrality Acts of 1935, 1936 and 1937 forbid?",
         r=["Arms sales and loans to countries at war", "Any trade with Germany", "Membership of the League of Nations",
            "Rearmament of the US Navy"], ok=0, voir="us",
         ex="Write “an isolationist Congress”: the Democrats held the majority from 1935 to 1939."),
    dict(q="What did the Anglo-German Naval Agreement of June 1935 allow?",
         r=["A German navy at 35% of the Royal Navy's tonnage", "The remilitarisation of the Rhineland",
            "A German navy equal to the Royal Navy", "An Anglo-German alliance against Italy"], ok=0, voir="pct",
         ex="Signed by Britain alone, two months after Stresa: Britain itself legalised a breach of Versailles."),
    dict(q="Which of these is NOT one of the course's reasons for appeasement?",
         r=["A military alliance with the USSR", "The memory of 1914–1918 and pacifism", "Fear of communism",
            "American isolationism"], ok=0, voir="wh",
         ex="Many in Britain and France feared communism more than fascism."),
    dict(q="Who was NOT at the Munich conference of 29–30 September 1938?",
         r=["The Czechs", "Mussolini", "Daladier", "Chamberlain"], ok=0, voir="mu",
         ex="The Sudetenland was handed over without the Czechs being invited."),
    dict(q="What did the Rhineland (7 March 1936) teach Hitler?",
         r=["That the democracies would yield", "That the French army was stronger than his", "That Italy would always follow him",
            "That the League could impose sanctions"], ok=0, voir="pari",
         ex="His troops had orders to retreat if France reacted; it did not."),
    dict(q="Why did Prague (15 March 1939) end appeasement?",
         r=["It was no longer uniting Germans but occupying a foreign people", "It was the first breach of Versailles",
            "Germany attacked France", "The USSR joined the Axis"], ok=0, voir="diff",
         ex="On 31 March 1939, France and Britain guaranteed Poland."),
    dict(q="According to the course, what did the democracies' reluctance supply on the road to war?",
         r=["The opportunity", "The will to expand", "The ideology", "The alliances"], ok=0, voir="vo",
         ex="Totalitarian ideology supplied the will to expand; the democracies' reluctance supplied the opportunity."),
]

CREDITS = [
    "Content: the DNL History course (chapter H2 · Parts III.2 and III.3, schemas “Appeasement: what it gave away, and why” and “Stepping stones to war”, DBQ 2 and DBQ 3 with the site's model answers) as written on the site; DBQ 3 b) written for this video on the chapter's key issue; Guernica given as a complementary example, not in the lesson; the share of Jews in Austria's population added from outside the course; animated map of chapter 2 (site).",
    "Photographs (via Wikimedia Commons): the Munich Agreement, 29 September 1938 (Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE); Chamberlain at Heston airport, 30 September 1938 (Imperial War Museums, D 2239, public domain); the ruins of Guernica, 1937 (Bundesarchiv, Bild 183-H25224, CC BY-SA 3.0 DE); Hitler on the Heldenplatz, Vienna, 15 March 1938 (Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE); Stalin and Ribbentrop, Moscow, 23 August 1939 (Helmut Laux, Bundesarchiv, Bild 183-H27337, CC BY-SA 3.0 DE).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
