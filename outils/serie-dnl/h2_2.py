"""DNL History · H2 « Totalitarian Regimes » — série vidéo, épisode 2 : « From the Great War to power » (parties I.1
« The legacy of WW1 » et I.2 « The seizure of power » du cours).

Vidéo en anglais (l'essay et le DBQ se rédigent en anglais), même chaîne que les séries philo :
outils/serie-philo/generer.py h2_2 ; sortie dans dnl/serie/ (moteur dnl/serie/moteur.js, type globe : la carte animée
du chapitre, dnl/cartes/H2.html, pilotée par le temps de la vidéo ; sc = numéros de scènes de la carte, dans l'ordre
chronologique de la carte).
  H2 : 1 brutalisation (1914-1918) · 2 Russie 1917 · 3 Allemagne, nov. 1918 - janv. 1919 · 4 Italie, victoire mutilée et
       Biennio Rosso · 5 Versailles et coup de poignard · 6 marche sur Rome · 7 putsch de Munich, Mein Kampf ·
       13 deux crises en 1929 · 16 la crise fait des nazis le premier parti · 20 Hitler chancelier · 21 incendie du Reichstag
Contenu : CHAPTERS.H2 du site (dnl/index.html), sections I.1 (7 idées) et I.2 (7 idées), schémas h2legacy (H2Legacy :
trois blessures de la guerre), h2parties (H2Parties : deux mouvements, mêmes composantes), h2weimar (H2Weimar :
chômage et vote NSDAP ; valeurs du chômage lues sur le graphique de M. Ros, arrondies) et h2seizure (H2Seizure : deux
chemins vers le pouvoir) ; points de H2Check repris : « Red Scare » / Terreur rouge, dates et effectifs de la marche
sur Rome (27-31 octobre d'ordinaire, 25 000 à 30 000 selon d'autres estimations ; chiffres du cours conservés),
croix gammée expliquée par Hitler dans Mein Kampf. Ce qui n'est pas dans le cours est dit « outside the course »
(effectifs de la SA, décret du 28 février 1933, date de Potsdam, programme en 25 points de 1920).
Plan : chronologie sur la carte (1914-1923, puis 1929-1933), cours structuré (I.1 idées 1 à 7, schéma h2legacy,
pause « Your turn » : paragraphe d'essay ; I.2 idées 1 à 7, schémas h2parties, h2weimar, h2seizure, pause « Your
turn » : « How far did Hitler come to power legally? »), récapitulatif.
Plan de la série H2 : 1 What is totalitarianism? · 2 From the Great War to power · 3 Three regimes, three ideologies ·
4 The leader, the party and the New Man · 5 Mass terror · 6 Hegemonic ambitions · 7 Appeasement and the road to war ·
8 Totalitarianism at the exam · 9 Recap.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h2-2"
NOTION = "Totalitarian Regimes"
NUM = 2
TITRE = "From the Great War to power"
SUIVANT = "Episode 3 · Three regimes, three ideologies"
PRONONCIATION = {"Reichstag": "Rikes-tahg", "Hindenburg": "Hin-den-boorg", "Weimar": "Vy-mar",
                 "Liebknecht": "Leeb-knekht", "Freikorps": "Fry-korps", "D'Annunzio": "Dan-noon-tsio",
                 "Fiume": "Fyoo-meh", "Biennio Rosso": "Bee-en-nyo Ross-o", "Mein Kampf": "Mine Kampf",
                 "Diktat": "Dik-taht", "Mosse": "Moss", "NSDAP": "N. S. D. A. P.", "De Vecchi": "Deh Vek-kee",
                 "Balbo": "Bal-bo", "De Bono": "Deh Bo-no", "Potsdam": "Pots-dam", "Duce": "Doo-chay",
                 "Petrograd": "Peh-tro-grad", "Trotsky": "Trot-skee", "Matteotti": "Mat-teh-ot-tee",
                 "fascistissime": "fa-shis-tee-see-meh", "Hanover": "Han-o-ver", "Spartacist": "Spar-ta-sist"}

# chômage en Allemagne (millions), lu sur le graphique de M. Ros (H2Weimar), arrondi
CHOMAGE = [[1921, .35], [1922, .2], [1923, .75], [1924, 1.0], [1925, .65], [1926, 2.0], [1927, 1.35], [1928, 1.4],
           [1929, 1.9], [1930, 3.1], [1931, 4.5], [1932, 5.6]]
# vote NSDAP aux élections au Reichstag (mai 1928, sept. 1930, juillet 1932, nov. 1932), placé en année décimale
VOTE = [[1928.4, 2.6], [1930.7, 18.3], [1932.55, 37.4], [1932.85, 33.1]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Berlin, the thirtieth of January, nineteen thirty-three. The President of the Republic is an old field marshal, Hindenburg. "
        "Today he appoints Adolf Hitler chancellor of Germany. {q1}There is no coup. It is perfectly legal.",
        "{-q1}{q2}Eleven years earlier, the king of Italy had done the same for Mussolini. So how did these men reach power?",
        "{-q2}{q3}To answer, we have to go further back. Back to the trenches of nineteen fourteen. Because the totalitarian regimes "
        "were born from the First World War.",
        "{-q3}{-g0}{plan}Today, we cover part one of the chapter, sections one and two. {plan.1}First, the story on the map, from nineteen fourteen to nineteen thirty-three. "
        "{plan.2}Then, the legacy of the war, in Russia, Italy and Germany. {plan.3}Next, the seizure of power, starting with Mussolini's fascism. "
        "{plan.4}Then Hitler's Nazism. The crisis, and the legal appointment. {plan.5}And finally, two exercises for the essay.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[20]),
        "q1": dict(type="question", t="30 January 1933: Hitler chancellor. No coup.", bande=True),
        "q2": dict(type="question", t="How did Mussolini and Hitler reach power?", bande=True),
        "q3": dict(type="question", t="Back to the trenches of 1914.", bande=True),
        "plan": dict(type="liste", titre="Episode 2 · Parts I.1 and I.2 of the course", items=[
            "The story on the map: 1914 – 1933", "I.1 · The legacy of WW1: Russia, Italy, Germany",
            "I.2 · Mussolini's fascism: from the squads to the March on Rome",
            "I.2 · Hitler's Nazism: the street, the crisis, the appointment", "Your turn: two essay exercises"],
            x=170, y=110, w=940),
        "titre": dict(type="titre", sur="DNL History · H2 · Episode 2", t="From the Great War to power",
                      sous="1914 – 1933 · the legacy of the war · the seizure of power"),
    }),

    # ================================================================ la carte : 1914-1923
    dict(id="carte1", chap="On the map: 1914 – 1923", fond="nuit", humeur="tension",
         retenir="1914–18 the trenches · 1917 the Bolsheviks · Nov. 1918 – Jan. 1919 Weimar, the Spartacists · 1919 Versailles · 1919–20 Biennio Rosso · Oct. 1922 March on Rome · Nov. 1923 Munich putsch.",
         beats=[
        "{g1}Let's follow the story on the map first. {g1.1}Nineteen fourteen to nineteen eighteen. Four years of trench warfare, and of mass killing. "
        "Among the soldiers is a German called Adolf Hitler.",
        "{g1.2}Nineteen seventeen. The war brings down the Russian empire. In February, the Tsar abdicates. In October, Lenin's Bolsheviks seize power. "
        "Then they win a civil war, which lasts until nineteen twenty-two.",
        "{g1.3}November nineteen eighteen. Germany is defeated. The Empire falls, and a republic is proclaimed. The Weimar Republic. "
        "In January nineteen nineteen, a communist uprising in Berlin is crushed in blood.",
        "{g1.4}In Italy, the war was won. But the nationalists feel cheated. And in nineteen nineteen and nineteen twenty, peasants seize land, and workers "
        "occupy the factories. These are the red years.",
        "{g1.5}Nineteen nineteen: the Treaty of Versailles. Germany must accept a treaty it never negotiated. A Diktat.",
        "{g1.6}October nineteen twenty-two. Mussolini's Blackshirts march on Rome, and the king appoints him prime minister. "
        "{g1.7}November nineteen twenty-three. In Munich, Hitler tries to seize power by force. He fails, and goes to prison.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[1, 2, 3, 4, 5, 6, 7]),
    }),

    # ================================================================ la carte : 1929-1933
    dict(id="carte2", chap="On the map: 1929 – 1933", fond="nuit", humeur="tension",
         retenir="1929 the crisis · July 1932: NSDAP 37.4%, the first party · 30 Jan. 1933: Hitler appointed chancellor · 27 Feb. 1933: the Reichstag fire.",
         beats=[
        "{g2}{g2.1}Then comes nineteen twenty-nine. The crash opens the crisis of capitalism. And the Nazis hold their congress in Nuremberg. Two crises at once.",
        "{g2.2}In Germany, millions lose their jobs. In July nineteen thirty-two, the Nazis become the largest party.",
        "{g2.3}On the thirtieth of January, nineteen thirty-three, Hindenburg appoints Hitler chancellor. "
        "{g2.4}Four weeks later, the Reichstag is on fire. And freedoms are suspended.",
        "{-g2}{fr1}So, here are the dates to know. {fr1.1}October nineteen seventeen: the Bolsheviks seize power. {fr1.2}Nineteen nineteen: the Treaty of Versailles. "
        "{fr1.3}October nineteen twenty-two: the March on Rome. {fr1.4}November nineteen twenty-three: the failed Munich putsch. "
        "{fr1.5}July nineteen thirty-two: the Nazis become the first party. {fr1.6}And the thirtieth of January, nineteen thirty-three: Hitler is chancellor.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[13, 16, 20, 21]),
        "fr1": dict(type="frise", items=[
            dict(nom="Bolsheviks", d=1917, q="October"), dict(nom="Versailles", d=1919, q="the “Diktat”"),
            dict(nom="March on Rome", d=1922, q="October"), dict(nom="Munich putsch", d=1923, q="November"),
            dict(nom="NSDAP 37.4%", d=1932, q="July"), dict(nom="Chancellor", d=1933, q="30 January")]),
    }),

    # ================================================================ I.1, idée 1 : la brutalisation
    dict(id="brutal", chap="I.1 · Brutalisation", fond="guerre", humeur="tension",
         retenir="Brutalisation (George Mosse): the war made violence ordinary; WW1 is the “matrix of totalitarianism”. Example: Hitler, a soldier in 1915.",
         beats=[
        "{photo1}{def1}Now for the course, idea by idea. Part one, point one: the legacy of the First World War. "
        "Idea one. The historian George Mosse coined a word for it. {!brutalisation}Brutalisation. "
        "{def1.1}Four years of mass killing got soldiers used to violence. After nineteen eighteen, they brought it home, into civilian life. "
        "And into politics. The traumas of the war raised the level of violence in post-war societies.",
        "{-def1}{mat}For Mosse, the war is the matrix of totalitarianism. Look at the new regimes. {mat.1}The uniforms. {mat.2}The ranks. "
        "{mat.3}The parades. {mat.4}The contempt for human life. They all come from the front.",
        "{-mat}{-photo1}{ex1}Monsieur Ros gives an example on his slide. It is a photograph of Adolf Hitler as a soldier, in nineteen fifteen, sitting among his comrades. "
        "{ex1.1}Mosse develops the idea in his book, Fallen Soldiers.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-ypres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="A New Zealand soldier among the ruins of Ypres cathedral, Belgium, 1917 · Archives New Zealand, CC BY-SA 2.0"),
        "def1": dict(type="def", cles=["violence", "politics"], terme="Brutalisation · George Mosse",
                     t="Four years of mass killing made violence ordinary; the soldiers brought it back into civilian life and politics.",
                     etape="The traumas of the war raised the level of violence after 1918", x=170, y=200, w=940),
        "mat": dict(type="liste", titre="WW1, “the matrix of totalitarianism”", items=[
            "Uniforms", "Ranks", "Parades", "Contempt for human life"], x=170, y=140, w=940),
        "ex1": dict(type="note", terme="Example · M. Ros's slide", cles=["soldier", "trenches"],
                    t="Adolf Hitler as a soldier in 1915, sitting among his comrades.",
                    etape="George Mosse, Fallen Soldiers: Reshaping the Memory of the World Wars", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 2 : la Russie
    dict(id="russie", chap="I.1 · Russia: from the Tsar to the Bolsheviks", fond="nuit", humeur="tension",
         retenir="Feb. 1917 the Tsar abdicates · Oct. 1917 Bolshevik coup (Lenin, Trotsky) with the soviets · peace with Germany · civil war won by the Red Army (to 1922) · USSR 1922 · the Red Scare.",
         beats=[
        "{g3}{g3.1}Idea two: Russia. This is a recap from Première, and it is on the programme. "
        "{rus}The war ruined the Russian empire. {rus.1}In February nineteen seventeen, a revolution forces the Tsar to abdicate. "
        "{rus.2}In October, the Bolsheviks, led by Lenin and Trotsky, carry out what Monsieur Ros calls a communist coup. "
        "They are supported by the {!soviets}soviets. Those are the workers' councils, in the factories and in the countryside.",
        "{rus.3}The Bolsheviks sign peace with Germany. {rus.4}Then they fight a civil war against the Whites. The Red Army wins it, in nineteen twenty-two. "
        "{rus.5}And that same year, the Soviet Union is created.",
        "{-rus}{-g3}{photo2}{rs}Why does this matter for Italy and Germany? Because Bolshevism is Marxism. And Marxism means the end of private property. "
        "{rs.1}It frightens the whole of Europe. This is the {!Red Scare}Red Scare.",
        "{-rs}{mots1}Be careful with the words here. {mots1.g}The Red Scare is the fear of communism in the West. "
        "{mots1.d}The Red Terror is something else. It is the violence of the Bolsheviks against their enemies, inside Russia, from nineteen eighteen.{-photo2}",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[2]),
        "rus": dict(type="liste", titre="Russia, 1917 – 1922", x=700, y=110, w=540, petit=True, bande=True, items=[
            "Feb. 1917: the Tsar abdicates", "Oct. 1917: the Bolshevik coup (Lenin, Trotsky), with the soviets",
            "Peace with Germany", "Civil war against the Whites, won by the Red Army (to 1922)", "1922: the USSR is created"]),
        "photo2": dict(type="tableau", img="h2-lenin-putilov", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .35, .45],
                       legende="Lenin speaks to the workers of the Putilov factory, Petrograd, May 1917 · Painting by Isaak Brodsky, 1929, public domain"),
        "rs": dict(type="def", cles=["property", "Europe"], terme="The Red Scare",
                   t="Bolshevism means the end of private property: the fear of communism spreads all over Europe.",
                   etape="Example: Lenin speaks to workers, soldiers and sailors in Petrograd, April 1917 (M. Ros's slide)",
                   x=170, y=200, w=940),
        "mots1": dict(type="cols", g="Red Scare", gq="the fear of communism in the West", d="Red Terror",
                      dq="Bolshevik violence inside Russia, from 1918", vs="≠", repere="Watch the vocabulary"),
    }),

    # ================================================================ I.1, idées 3 et 4 : l'Italie
    dict(id="italie", chap="I.1 · Italy: a mutilated victory, two red years", fond="nuit", humeur="tension",
         retenir="“Mutilated victory”: Italy did not get all the promised lands → irredentism; turmoil, inflation, mass unemployment. Fiume (D'Annunzio, Sept. 1919 – Dec. 1920). Biennio Rosso (1919–20): land and factory occupations (Turin, 1920); Blackshirts paid by landowners.",
         beats=[
        "{g4}{g4.1}Idea three: Italy. In nineteen eighteen, Italy is on the winning side. But it does not get all the lands it was promised. "
        "{vm}The nationalists speak of a {!mutilated victory}mutilated victory. The country won. It paid in blood. And yet it feels cheated. "
        "{vm.1}This feeds an {!irredentist}irredentist movement, which demands the unredeemed territories. "
        "{vm.2}And the frustration comes on top of social turmoil, inflation, and mass unemployment.",
        "{-vm}{fiu}The example is Fiume. {fiu.1}In September nineteen nineteen, the poet Gabriele D'Annunzio seizes the city with nationalist volunteers. "
        "{fiu.2}He holds it until December nineteen twenty. {fiu.3}Mussolini will later borrow his rituals.",
        "{-fiu}{-g4}{photo3}{br}Idea four: the {!Biennio Rosso}Biennio Rosso. The two red years, nineteen nineteen and nineteen twenty. "
        "{br.g}Peasants seize land. Workers go on strike, or take over the factories. The property owners believe an Italian nineteen seventeen is coming. "
        "{br.d}Mussolini's Blackshirts, the fascist militia, answer with violent repression. And the landowners pay them to take back the land.",
        "{-br}{tur}Monsieur Ros's slide gives the example. {tur.1}The general strike of nineteen twenty, in Turin. The workers occupied the factories, and ran them themselves. "
        "{tur.2}So the fear was real. And fascism grew as the armed wing of the frightened propertied classes.{-photo3}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[4]),
        "vm": dict(type="liste", titre="Italy: a “mutilated victory”", x=60, y=110, w=620, petit=True, bande=True, items=[
            "Irredentism: demanding the “unredeemed” lands", "Turmoil, inflation, mass unemployment"]),
        "fiu": dict(type="liste", titre="Example: Fiume", x=60, y=110, w=620, petit=True, bande=True, items=[
            "Sept. 1919: D'Annunzio seizes the city", "Held until December 1920", "Rituals later borrowed by Mussolini"]),
        "photo3": dict(type="tableau", img="h2-biennio-rosso", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Workers' Red Guards occupy the factories, Italy, September 1920 · Unknown photographer, public domain"),
        "br": dict(type="cols", g="The red years · 1919 – 1920", gq="land seized, strikes, factories occupied: “an Italian 1917”?",
                   d="The Blackshirts", dq="violent repression, paid by the landowners", vs="→", repere="Biennio Rosso"),
        "tur": dict(type="note", terme="Example · Turin, 1920", cles=["strike", "factories", "real"],
                    t="The general strike: the workers occupy and run the factories themselves.",
                    etape="The fear was real → fascism, the armed wing of the propertied classes", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 5 : l'Allemagne, une république dans la violence
    dict(id="weimar", chap="I.1 · Germany: a republic born in violence", fond="guerre", humeur="tension",
         retenir="1918: defeat ends the German Empire → the Weimar Republic. Jan. 1919: the Spartacist uprising (Luxemburg, Liebknecht) fails; both murdered by the Freikorps, 15 Jan. 1919.",
         beats=[
        "{g5}{g5.1}Idea five: Germany. In nineteen eighteen, military defeat brings the end of the German Empire. A new regime is born. "
        "The {!Weimar Republic}Weimar Republic.",
        "{spa}But in the cities, some revolutionaries want to go further. {spa.1}In January nineteen nineteen comes the {!Spartacist}Spartacist uprising. "
        "It is a communist revolt, led by Rosa Luxemburg and Karl Liebknecht. They want a revolution on the Russian model. "
        "{spa.2}It fails. {spa.3}On the fifteenth of January, nineteen nineteen, Luxemburg and Liebknecht are murdered by Freikorps soldiers. "
        "The Freikorps are armed volunteers, many of them former soldiers.",
        "{-spa}{-g5}{photo4}{wr}On the slide, the example is a barricade in Berlin, during the uprising. "
        "{wr.1}So, from its very first weeks, the republic is tied to two things. Defeat. And bloodshed, on both sides.{-photo4}",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[3]),
        "spa": dict(type="liste", titre="The Spartacist uprising", x=60, y=110, w=620, petit=True, bande=True, items=[
            "Jan. 1919: Luxemburg and Liebknecht, a revolution on the Russian model", "It fails",
            "15 Jan. 1919: both murdered by the Freikorps"]),
        "photo4": dict(type="tableau", img="h2-spartacist", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="A barricade of newsprint rolls during the Spartacist uprising, Berlin, January 1919 · Illustrirte Zeitung, public domain"),
        "wr": dict(type="def", cles=["defeat", "bloodshed"], terme="The Weimar Republic · 1918",
                   t="A republic born from defeat, in civil violence.",
                   etape="Associated from its first weeks with defeat and bloodshed on both sides", x=170, y=200, w=940),
    }),

    # ================================================================ I.1, idée 6 : Versailles et le coup de poignard
    dict(id="versailles", chap="I.1 · The Diktat and the stab in the back", fond="nuit", humeur="tension",
         retenir="Versailles (1919), imposed not negotiated: War Guilt Clause, Alsace-Lorraine and the eastern territories lost, huge reparations → the “Diktat”. The stab-in-the-back myth: betrayed at home (example: the 1919 postcard).",
         beats=[
        "{g6}{g6.1}Idea six: the Treaty of Versailles, in nineteen nineteen. {ver}It was imposed, not negotiated. If Germany refused to sign, it would be invaded. "
        "{ver.1}It contained the War Guilt Clause. Germany was held responsible for the war. "
        "{ver.2}It took away Alsace-Lorraine, and the eastern territories. {ver.3}It imposed huge reparations. "
        "{ver.4}So the Germans called it a {!Diktat}Diktat. A dictated peace.",
        "{-ver}{-g6}{dol}At the same time, military circles spread a conspiracy theory. The {!stab in the back}stab in the back. "
        "{dol.1}The army, they said, had not been beaten at the front. It had been betrayed at home.",
        "{-dol}{cp}Monsieur Ros shows a German postcard from nineteen nineteen. {cp.1}A soldier is stabbed from behind by a caricatured Jew. "
        "{cp.2}The myth blamed democrats, pacifists and socialists. Or, as here, Jews. "
        "{cp.3}It turned defeat into a grievance. And it gave the far right its enemies, ready-made.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[5]),
        "ver": dict(type="liste", titre="Versailles, 1919: a “Diktat”", x=60, y=110, w=620, petit=True, bande=True, items=[
            "The War Guilt Clause", "Alsace-Lorraine and the eastern territories lost", "Huge reparations",
            "Imposed, not negotiated: a “Diktat”"]),
        "dol": dict(type="def", cles=["beaten", "betrayed"], terme="The stab-in-the-back myth",
                    t="The army was not beaten at the front, but betrayed at home.",
                    etape="Spread by military circles from 1919", x=170, y=200, w=940),
        "cp": dict(type="liste", titre="Example · a German postcard, 1919", cles=["Jew", "enemies"], items=[
            "A soldier stabbed from behind by a caricatured Jew",
            "Blamed: democrats, pacifists, socialists, Jews",
            "Defeat turned into a grievance; enemies ready-made"], x=170, y=150, w=940),
    }),

    # ================================================================ I.1, idée 7 : le putsch de Munich
    dict(id="munich", chap="I.1 · From the Munich putsch to the crisis", fond="guerre", humeur="tension",
         retenir="Nov. 1923: Hitler's failed coup in Munich → lesson: win power through the institutions. In prison: Mein Kampf (1924–25), his racist views. Then the crisis of the 1930s: “the war created the grievances; the crisis turned them into votes.”",
         beats=[
        "{g7}{g7.1}Idea seven. The Weimar Republic never won over its enemies. In November nineteen twenty-three, in Munich, "
        "Hitler tries to seize power by force. It is a failure.",
        "{-g7}{les}He is sent to prison. And he learns a lesson from his failure. {les.1}Power must be won through the institutions. "
        "{!not against them}Not against them. {les.2}In prison, he writes Mein Kampf. As Monsieur Ros's slides note, "
        "he sets out his racist views there as early as nineteen twenty-four and twenty-five.",
        "{-les}{cr}Then come the nineteen thirties. The extreme economic crisis of chapter one gives his party the mass audience it had lacked. "
        "{cr.1}Here is one sentence to remember, and to use in your essays.",
        "{-cr}{phr}The war created the grievances. The crisis turned them into votes.",
        ("P", 2.0),
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[7]),
        "les": dict(type="cols", g="Nov. 1923 · the failed coup", gq="power by force, in Munich: a failure",
                    d="The lesson", dq="win power through the institutions · Mein Kampf, 1924–25", vs="→"),
        "cr": dict(type="note", terme="Then the 1930s", cles=["crisis", "mass"],
                   t="The extreme economic crisis (chapter 1) gives the Nazi party the mass audience it lacked.",
                   etape="One sentence to remember", x=170, y=200, w=940),
        "phr": dict(type="mot", t="Grievances → votes", g="The war created the grievances; the crisis turned them into votes.",
                    y=250, taille=96),
    }),

    # ================================================================ schéma h2legacy
    dict(id="legacy", chap="Three wounds of the war", fond="aube", humeur="calme",
         retenir="Russia: war ruins the empire → Bolshevik Revolution → single party, property abolished, fear of communism. Italy: mutilated victory → Fiume, paid Blackshirts → armed nationalism. Germany: defeat, Diktat → Spartacists crushed, stab-in-the-back → a republic tied to defeat.",
         beats=[
        "{bl}Here is Monsieur Ros's schema: three wounds of the war. {bl.1}Start with the wound itself. In Russia, the war ruins the Tsarist empire. "
        "{bl.2}In Italy, it leaves a mutilated victory. {bl.3}In Germany, defeat, the end of the Empire, and the Diktat.",
        "{-bl}{rp}Next, the response. {rp.1}In Russia, the Bolshevik Revolution. {rp.2}In Italy, Fiume, and the paid Blackshirts. "
        "{rp.3}In Germany, the Spartacists are crushed, and the stab-in-the-back myth spreads.",
        "{-rp}{lg}And finally, the legacy. {lg.1}In Russia, a single party, and the fear of communism. "
        "{lg.2}In Italy, an armed nationalism. "
        "{lg.3}In Germany, a republic tied to defeat, and enemies ready-made.",
        "{-lg}{rem}So remember. Everywhere, the war prepares the soil. Violence. Grievances. Fear of revolution. "
        "{rem.1}But it does not yet decide which regime will grow there.",
    ], vis={
        "bl": dict(type="cartes", petit=True, items=[
            dict(t="Russia", q="Wound: the war ruins the Tsarist empire"),
            dict(t="Italy", q="Wound: a “mutilated victory”, neither Fiume nor Dalmatia"),
            dict(t="Germany", q="Wound: defeat, end of the Empire, the Diktat")]),
        "rp": dict(type="cartes", petit=True, items=[
            dict(t="Russia", q="Response: the Bolshevik Revolution, Oct. 1917"),
            dict(t="Italy", q="Response: D'Annunzio in Fiume; Blackshirts paid by landowners"),
            dict(t="Germany", q="Response: Spartacists crushed; the stab-in-the-back myth")]),
        "lg": dict(type="cartes", petit=True, items=[
            dict(t="Russia", q="Legacy: single party, property abolished, fear of communism"),
            dict(t="Italy", q="Legacy: armed nationalism against the fear of revolution"),
            dict(t="Germany", q="Legacy: a republic tied to defeat; enemies ready-made")]),
        "rem": dict(type="note", terme="Remember", cles=["soil", "decide"],
                    t="The war supplies the soil everywhere: violence, grievances, fear of revolution.",
                    etape="It does not yet decide which regime will grow in it", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : un paragraphe d'essay
    dict(id="essai1", chap="Your turn · the war as a matrix", fond="aube", humeur="calme",
         retenir="Model: brutalisation (Mosse, Hitler 1915) · the fear of revolution (Bolsheviks, Biennio Rosso, Turin 1920) · grievances (mutilated victory, Diktat, stab in the back) · nuance: soil, not cause (the crisis).",
         beats=[
        "{ex1q}Your turn. Here is an essay question. {!explain}Explain how the First World War prepared the ground for the totalitarian regimes. "
        "Write one paragraph, with three arguments, and a precise example for each.",
        "{-ex1q}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod1}Here is a model. {mod1.1}The First World War prepared the ground for the totalitarian regimes in three ways. "
        "First, it brutalised societies. As George Mosse showed, four years of mass killing made violence ordinary. "
        "And men like Hitler, a soldier in nineteen fifteen, brought it back into politics. "
        "{mod1.2}Second, it created the fear of revolution. The Bolsheviks seized power in Russia in October nineteen seventeen. "
        "And during the Biennio Rosso, Italian workers occupied the factories of Turin. So the landowners paid the Blackshirts to repress them. "
        "{mod1.3}Third, it left deep grievances. In Italy, the mutilated victory. In Germany, the Versailles Diktat, and the stab-in-the-back myth. "
        "{mod1.4}Yet the war only prepared the soil. In Germany, it took the crisis of the nineteen thirties to turn these grievances into votes.",
    ], vis={
        "ex1q": dict(type="exo", niveau="essay", titre="Explain how the First World War prepared the ground for the totalitarian regimes.",
                     src="Question written for this video, on Part I.1 of the course",
                     enonce=["One paragraph: three arguments, one precise example each"]),
        "pa1": dict(type="pause", t="Essay paragraph: how did WW1 prepare the ground for the totalitarian regimes?",
                    sous="Three arguments, one precise example each. Pause the video, write, then play on for a model."),
        "mod1": dict(type="liste", titre="A model paragraph", petit=True, items=[
            "Brutalisation → George Mosse; Hitler, a soldier in 1915",
            "The fear of revolution → October 1917; Turin, 1920; Blackshirts paid by landowners",
            "Grievances → the mutilated victory; the Diktat; the stab in the back",
            "Nuance: the soil, not the cause → the crisis turns grievances into votes"], x=150, y=140, w=980),
    }),

    # ================================================================ I.2, idée 1 : les composantes du fascisme
    dict(id="fascisme", chap="I.2 · Mussolini's fascism: the building blocks", fond="nuit", humeur="tension",
         retenir="Fascism: a growing party + one leader (Mussolini) · a programme: “Law and Order” · a symbol: the fasces · paramilitary squads (Blackshirts). Supported by landowners and shopkeepers terrified by communism.",
         beats=[
        "{fa}Part one, point two: the seizure of power. Idea one. Monsieur Ros breaks fascism down into its building blocks. "
        "{fa.1}A party with a growing influence, and more and more supporters. And one leader, Mussolini. "
        "{fa.2}A programme that appealed to voters: {!Law and Order}Law and Order. "
        "{fa.3}A symbol. {fa.4}And paramilitary squads, led by fascist squad leaders.",
        "{-fa}{fs}The symbol gives the movement its name. {fs.1}The word fascist comes from the {!fasces}fasces. "
        "It is a bundle of rods around an axe, carried before the magistrates of ancient Rome. An imperial Roman object.",
        "{-fs}{sup}And who supported fascism? {sup.1}Landowners and shopkeepers, terrified by communism. "
        "{sup.2}Law and Order spoke directly to them.",
    ], vis={
        "fa": dict(type="liste", titre="Fascism: the building blocks", cles=["leader", "Order", "symbol", "squads"], items=[
            "A growing party, and one leader: Mussolini", "A programme: “Law and Order”", "A symbol: the fasces",
            "Paramilitary squads: the Blackshirts"], x=170, y=140, w=940),
        "fs": dict(type="def", cles=["rods", "axe", "Rome"], terme="The fasces",
                   t="A bundle of rods around an axe, carried before Roman magistrates.",
                   etape="It gave the movement its name and its emblem", x=170, y=200, w=940),
        "sup": dict(type="note", terme="Who supported fascism?", cles=["landowners", "shopkeepers"],
                    t="Landowners and shopkeepers, terrified by communism after the Biennio Rosso.",
                    etape="“Law and Order” spoke directly to them", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 2 : la marche sur Rome
    dict(id="marche", chap="I.2 · The March on Rome", fond="guerre", humeur="tension",
         retenir="Oct. 1922: the March on Rome (≈ 20,000 Blackshirts, course figure). Intimidation, not a coup: the king refuses martial law and appoints Mussolini prime minister on 30 Oct. 1922.",
         beats=[
        "{g8}{g8.1}Idea two. In October nineteen twenty-two, the Blackshirts march on Rome. {mr}But Mussolini does not organise the march "
        "to take power by arms. {mr.1}He organises it to push the king into appointing him prime minister.",
        "{mr.2}Only a few thousand come. About twenty thousand, according to the class. Far fewer than he had hoped. "
        "{mr.3}Most of them are suspected of murder. They are not violent during the march. But everyone knows they could be.",
        "{mr.4}And the threat is enough. King Victor Emmanuel the Third refuses to declare martial law. On the thirtieth of October, nineteen twenty-two, "
        "he appoints Mussolini prime minister.",
        "{-mr}{-g8}{photo5}{int}So remember the formula. {!intimidation, not a coup}Intimidation, not a coup. "
        "{int.1}The threat of violence forced a legal appointment. On the slide, Mussolini stands among his squad leaders. De Bono, Balbo, and De Vecchi.",
        "{-int}{-photo5}{att1}Watch out for two details. {att1.1}The slide dates the march from the twenty-second to the twenty-ninth of October. "
        "Historians usually say the twenty-seventh to the thirty-first. "
        "{att1.2}And many estimates go up to thirty thousand marchers. The safest answer? October nineteen twenty-two, and some twenty thousand Blackshirts.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[6]),
        "mr": dict(type="liste", titre="The March on Rome · October 1922", x=40, y=110, w=520, petit=True, bande=True, items=[
            "The aim: push the king to appoint him", "≈ 20,000 Blackshirts, fewer than hoped (course figure)",
            "Not violent during the march… but feared", "30 Oct.: the king refuses martial law, appoints Mussolini"]),
        "photo5": dict(type="tableau", img="h2-march-rome", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .35],
                       legende="Mussolini with the four quadrumvirs of the March on Rome, 1922, commemorative painting · Photo Silvio Galimberti, CC BY-SA 4.0"),
        "int": dict(type="def", cles=["threat", "legal"], terme="Intimidation, not a coup",
                    t="The threat of violence forced a legal appointment.",
                    etape="M. Ros's slide: Mussolini with De Bono, Balbo and De Vecchi", x=170, y=200, w=940),
        "att1": dict(type="note", terme="Watch out · dates and numbers", cles=["usually", "estimates"],
                     t="Slide: 22–29 Oct. 1922. Usually dated 27–31 Oct. Course: ≈ 20,000; other estimates: 25,000–30,000.",
                     etape="Safest in an essay: October 1922, some 20,000 Blackshirts", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 3 : le nazisme, mêmes composantes
    dict(id="nazisme", chap="I.2 · Hitler's Nazism: the same building blocks", fond="nuit", humeur="tension",
         retenir="Nazism: NSDAP + one leader (Hitler) · a programme from Mein Kampf: abolish Versailles, unite Germany and Austria, nationalise large industries, exclude Jews · the black swastika (“Aryan”) · the SA and the SS. What separates it from fascism: race.",
         beats=[
        "{pg}Idea three. Hitler's Nazism has the same building blocks. {pg.1}A party with a growing influence, the Nazi Party. And one leader, Hitler. "
        "{pg.2}A programme, based on Mein Kampf. It plans to abolish the Treaty of Versailles. "
        "{pg.3}To unite Germany and Austria. {pg.4}To nationalise large industries and businesses. "
        "{pg.5}And to exclude Jews from German society.",
        "{-pg}{hk}A point from outside the course. These demands were already in the party's twenty-five point programme, in nineteen twenty. "
        "{hk.1}Mein Kampf develops them.",
        "{-hk}{sw}The symbol is the black {!swastika}swastika. {sw.1}It was an ancient sign, long seen as lucky. The Nazis made it Aryan. "
        "{sw.2}The class noted that it was chosen for no particular reason. In fact, Hitler does explain its symbolism, in Mein Kampf. "
        "{sw.3}And the paramilitary organisations are the S. A. and the S. S.",
        "{-sw}{tb}So here is Monsieur Ros's table. Two movements, the same building blocks. {tb.g}Fascism on one side. "
        "{tb.d}Nazism on the other.",
        "{-tb}{dif}Two things to add. {dif.1}Mussolini came to power eleven years before Hitler. So, for Monsieur Ros, fascism is the first totalitarianism. "
        "{dif.2}And what separates the two movements? {!race}Race. It is at the heart of the Nazi programme, from Mein Kampf onwards.",
    ], vis={
        "pg": dict(type="liste", titre="Nazism: party, leader, programme", cles=["Versailles", "Austria", "nationalise", "exclude"], items=[
            "The NSDAP, and one leader: Hitler", "Programme (Mein Kampf): abolish Versailles", "Unite Germany and Austria",
            "Nationalise large industries and businesses", "Exclude Jews from German society"], x=170, y=110, w=940),
        "hk": dict(type="note", terme="Outside the course", cles=["1920", "develops"],
                   t="These demands were already in the party's 25-point programme of February 1920.",
                   etape="Mein Kampf (1924–25) develops them", x=170, y=200, w=940),
        "sw": dict(type="liste", titre="Symbol and paramilitaries", items=[
            "The black swastika: an ancient sign, made “Aryan” by the Nazis",
            "Nuance: Hitler explains its symbolism in Mein Kampf", "The SA and the SS"], x=170, y=150, w=940),
        "tb": dict(type="cols", g="Mussolini's fascism", gq="National Fascist Party, Mussolini · “Law and Order” · the fasces · the Blackshirts",
                   d="Hitler's Nazism", dq="NSDAP, Hitler · Mein Kampf · the swastika · the SA and the SS", vs="=",
                   repere="Two movements, the same building blocks"),
        "dif": dict(type="liste", titre="What the table also says", cles=["first", "race"], items=[
            "Mussolini in power eleven years before Hitler: fascism, “the first totalitarianism”",
            "What separates them: race, at the heart of Nazism from Mein Kampf onwards"], x=170, y=170, w=940),
    }),

    # ================================================================ I.2, idée 4 : la SA et la SS
    dict(id="rue", chap="I.2 · Conquering the street: the SA and the SS", fond="guerre", humeur="tension",
         retenir="SA (storm troopers): a mass force, unemployed and uneducated men, some with criminal records; street fights with communists. SS: an elite, selected, better educated. Violence as a tool of conquest. By 1933, several hundred thousand SA (outside the course).",
         beats=[
        "{photo6}{sa}Idea four. The Nazi movement has two armed wings. {sa.g}First, the {!SA}S. A., the storm troopers. They are a mass force. "
        "Most are unemployed and uneducated men, and some have criminal records. "
        "They fight communists in the streets, and they protect Nazi meetings. "
        "{sa.d}Second, the S. S. They are an elite. Selected, better educated, and often from wealthier backgrounds.",
        "{-sa}{ord}Here is an order of magnitude, from outside the course. By nineteen thirty-three, the S. A. counted several hundred thousand men. "
        "{ord.1}That is several times the army that the Treaty of Versailles allowed Germany. One hundred thousand men.",
        "{-ord}{-photo6}{vio}So violence was not a side effect of Nazism. It was {!a tool of conquest}a tool of conquest.",
    ], vis={
        "photo6": dict(type="tableau", img="h2-unemployed-sa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Unemployed SA men on a bench in Berlin, 1932 · Bundesarchiv, Bild 146-1985-054-02, CC BY-SA 3.0 DE"),
        "sa": dict(type="cols", g="The SA · storm troopers", gq="a mass force: unemployed, uneducated men; street fights, meetings protected",
                   d="The SS", dq="an elite: selected, better educated, often wealthier", vs="+"),
        "ord": dict(type="note", terme="Outside the course · an order of magnitude", cles=["hundred", "Versailles"],
                    t="By 1933, the SA counted several hundred thousand men.",
                    etape="Several times the 100,000-man army allowed by Versailles", x=170, y=200, w=940),
        "vio": dict(type="question", t="Violence: not a side effect, a tool of conquest."),
    }),

    # ================================================================ I.2, idée 5 : la crise et le vote nazi
    dict(id="crise", chap="I.2 · The crisis and the Nazi vote", fond="nuit", humeur="tension",
         retenir="Unemployment ≈ 5.6 million (1932). NSDAP: 2.6% (May 1928) → 18.3% (Sept. 1930) → 37.4% (July 1932, first party) → 33.1% (Nov. 1932). Never a majority in a free election.",
         beats=[
        "{g9}{g9.1}Idea five. The crisis turned the Nazis from a fringe party into the first party in Germany. "
        "Monsieur Ros's slide shows unemployed men queuing for food aid, in Hanover, in nineteen thirty-two.",
        "{-g9}{gu}Look first at unemployment in Germany, on Monsieur Ros's chart. {gu.1}In the nineteen twenties, it stays around two million at most. "
        "{gu.2}Then the crisis hits. By nineteen thirty-two, about five point six million Germans are out of work.",
        ("P", 2.5),
        "{-gu}{gv}Now, the Nazi vote. {gv.1}This red line is the majority. Fifty per cent. "
        "{gv.2}In May nineteen twenty-eight, before the crisis, the Nazis are a fringe party. Two point six per cent. {gv.3}{gv.4}In September nineteen thirty, eighteen point three. "
        "{gv.5}In July nineteen thirty-two, thirty-seven point four per cent. Now they are the largest party in the Reichstag.",
        "{gv.6}But in November nineteen thirty-two, they lose ground. Thirty-three point one per cent.",
        "{-gv}{maj}And here is the key point. {maj.1}The Nazis never won a majority in a free election. "
        "{maj.2}Hitler did not come to power because most Germans voted for him. "
        "{maj.3}He was appointed on the thirtieth of January, nineteen thirty-three. And his party was losing votes at the time.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[16]),
        "gu": dict(type="graphe", titre="Unemployed in Germany, millions (M. Ros's chart, rounded)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1920.5, 1932.8], y=[0, 6.5], gx=[1922, 1924, 1926, 1928, 1930, 1932], gy=[1, 2, 3, 4, 5, 6],
                           lx="year", ly="millions"),
                   el=[dict(type="courbe", pts=CHOMAGE[:9], c="iv2", lbl="the 1920s", lp=[1924.5, 2.3], dur=2.0),
                       dict(type="courbe", pts=CHOMAGE[8:], c="ca", lbl="1932: ≈ 5.6 million", lp=[1929.6, 5.8], dur=1.6)]),
        "gv": dict(type="graphe", titre="NSDAP vote in Reichstag elections (M. Ros's chart)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 60], gx=[1928, 1930, 1932], gy=[10, 20, 30, 40, 50], lx="year", ly="%"),
                   el=[dict(type="droite", pts=[[1927.6, 50], [1933.4, 50]], c="rouge", tir=True, ep=2.4,
                            lbl="majority: 50%", lp=[1929.3, 53.5]),
                       dict(type="point", x=1928.4, y=2.6, c="sa", lbl="2.6%", lp=[1928.4, 10]),
                       dict(type="courbe", pts=VOTE[:2], c="sa", dur=1.2),
                       dict(type="point", x=1930.7, y=18.3, c="sa", lbl="18.3%", lp=[1930.4, 26]),
                       dict(type="courbe", pts=VOTE[1:3], c="sa", lbl="37.4%", lp=[1932.0, 45], dur=1.2),
                       dict(type="courbe", pts=VOTE[2:], c="ca", lbl="33.1%", lp=[1933.05, 29], dur=1.0)]),
        "maj": dict(type="liste", titre="Never a majority", cles=["free", "majority", "losing"], items=[
            "No majority in any free election", "Not brought to power by a majority of Germans",
            "Appointed on 30 Jan. 1933, just as his party was losing votes"], x=170, y=150, w=940),
    }),

    # ================================================================ I.2, idée 6 : la nomination légale
    dict(id="nomination", chap="I.2 · A legal appointment", fond="guerre", humeur="tension",
         retenir="30 Jan. 1933: President Hindenburg, an old general of the Empire, appoints Hitler chancellor. The conservatives think they can control him. Potsdam, March 1933: Hitler bows to Hindenburg.",
         beats=[
        "{g10}{g10.1}Idea six. Like Mussolini, Hitler did not take power by a coup. On the thirtieth of January, nineteen thirty-three, he was appointed chancellor "
        "by the President of the Republic, Paul von Hindenburg.",
        "{-g10}{hb}So who was Hindenburg? {hb.1}An old general of the Empire, who had supported the monarchy. "
        "{hb.2}The conservatives around him thought they could control Hitler, once he was in government. "
        "{hb.3}The legal façade let the Nazis dismantle the republic {!from inside}from inside.",
        "{-hb}{photo7}{pot}A photograph opens Monsieur Ros's section, and it shows exactly this. {pot.1}Hitler bows to greet Hindenburg, at Potsdam. "
        "The date, the twenty-first of March, nineteen thirty-three, is from outside the course. "
        "{pot.2}The image is designed to present Nazism as the heir of the old Prussian order.{-photo7}",
    ], vis={
        "g10": dict(type="globe", code="H2", sc=[20]),
        "hb": dict(type="liste", titre="Why the elites let him in", cles=["monarchy", "control", "façade"], items=[
            "Hindenburg: an old general of the Empire, a monarchist", "The conservatives: “we can control him”",
            "A legal façade: the republic dismantled from inside"], x=170, y=150, w=940),
        "photo7": dict(type="tableau", img="h2-potsdam", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.15, .5, .4],
                       legende="Hitler bows to Hindenburg, Potsdam, 21 March 1933 · Bundesarchiv, Bild 183-S38324, CC BY-SA 3.0 DE"),
        "pot": dict(type="note", terme="Example · Potsdam, 21 March 1933", cles=["bows", "heir"],
                    t="Hitler bows to greet President Hindenburg: Nazism as the heir of the old Prussian order.",
                    etape="The photograph opens M. Ros's section · exact date outside the course", x=170, y=200, w=940),
    }),

    # ================================================================ I.2, idée 7 : l'incendie du Reichstag
    dict(id="reichstag", chap="I.2 · The Reichstag fire", fond="nuit", humeur="tension",
         retenir="27 Feb. 1933: the Reichstag fire; the Nazis blame the communists. The next day, a decree suspends freedom of the press, of assembly and of opinion (date outside the course); thousands of communists arrested. Who started it is debated: what matters is how it was used.",
         beats=[
        "{g11}{g11.1}Idea seven. On the twenty-seventh of February, nineteen thirty-three, a month after Hitler's appointment, the German parliament is set on fire. The Reichstag.",
        "{rf}{rf.1}The Nazis immediately blame the communists. They claim the fire is the signal for a revolution. "
        "{rf.2}Hitler and Hindenburg use it to strike at communism. The very next day, Hindenburg signs a decree. That date is from outside the course. "
        "It suspends freedom of the press, of assembly, and of opinion. "
        "{rf.3}Within days, thousands of communists are arrested.",
        "{-rf}{-g11}{qui}Who started the fire? It is still debated. It may have been the Nazis themselves. "
        "{qui.1}{!What matters}But what matters is how the regime used it. To suspend freedoms, and to crush its first enemies.",
    ], vis={
        "g11": dict(type="globe", code="H2", sc=[21]),
        "rf": dict(type="liste", titre="27 February 1933 → the emergency", x=730, y=110, w=510, petit=True, bande=True, items=[
            "The Nazis blame the communists: “a revolution”",
            "28 Feb.: a decree suspends press, assembly, opinion (date outside the course)",
            "Thousands of communists arrested within days"]),
        "qui": dict(type="note", terme="Who started the fire?", cles=["debated", "used"],
                    t="Still debated, possibly the Nazis themselves. What matters is how the regime used it.",
                    etape="An emergency → freedoms suspended, communists crushed", x=170, y=200, w=940),
    }),

    # ================================================================ schéma h2seizure : deux chemins vers le pouvoir
    dict(id="seizure", chap="Two roads to power", fond="aube", humeur="calme",
         retenir="Italy: squads paid (1919–20) → March on Rome (Oct. 1922) → appointed by the king (30 Oct. 1922) → Matteotti, fascistissime laws (1924–26). Germany: failed coup (Nov. 1923) → crisis, 18.3% → 37.4% → appointed by Hindenburg (30 Jan. 1933) → Reichstag fire, emergency decree. Common: paramilitary violence + legal appointment + conservative elites. Different: the pace.",
         beats=[
        "{it}Now, let's compare the two roads to power, with Monsieur Ros's schema. The street threatens. The top appoints. "
        "{it.1}In Italy, first the paid squads. {it.2}Then the March on Rome. {it.3}Then the king's appointment. "
        "{it.4}And then, the murder of Matteotti and the fascistissime laws. That is for episode three.",
        "{al}{al.1}In Germany, first the failed coup. {al.2}Then the crisis vote. "
        "{al.3}Then Hindenburg's appointment. {al.4}And then the Reichstag fire, and the emergency decree. Read the two lines side by side.",
        ("P", 3.0),
        "{-it}{-al}{cd}So what do they have in common? And what is different? {cd.g}In common, paramilitary violence. A legal appointment by the head of State. "
        "And the support of conservative elites. {cd.d}The difference is the pace. Mussolini took two to three years to build his dictatorship. "
        "Hitler took a few weeks.",
    ], vis={
        "it": dict(type="liste", titre="Italy · Mussolini", petit=True, x=40, y=110, w=580, items=[
            "1919–20 · fear of occupations; squads paid", "22–29 Oct. 1922 · March on Rome (≈ 20,000)",
            "30 Oct. 1922 · the king appoints him", "1924–26 · Matteotti → fascistissime laws"]),
        "al": dict(type="liste", titre="Germany · Hitler", petit=True, x=660, y=110, w=580, items=[
            "Nov. 1923 · failed coup in Munich", "1930–32 · crisis: 18.3% → 37.4%",
            "30 Jan. 1933 · Hindenburg appoints him", "27–28 Feb. 1933 · Reichstag → emergency decree"]),
        "cd": dict(type="cols", g="Common", gq="paramilitary violence + legal appointment by the head of State + conservative elites",
                   d="Different", dq="the pace: 2–3 years for Mussolini, a few weeks for Hitler", vs="≠",
                   repere="The street threatens, the top appoints"),
    }),

    # ================================================================ à toi : « How far… legally? »
    dict(id="essai2", chap="Your turn · how far legally?", fond="aube", humeur="calme",
         retenir="Assess: largely legal in form (Hindenburg, 30 Jan. 1933; 37.4%; the 1923 lesson) · but prepared and completed by violence (SA, Reichstag fire, decree, arrests) and never a majority · judgement: legal in form, not democratic.",
         beats=[
        "{ex2}Your turn again. This time, it is an {!Assess}Assess question. How far did Hitler come to power legally? "
        "{ex2.1}For an Assess or How far question, you weigh both sides. Then you give a clear judgement.",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod2}Here is a model. {mod2.1}To a large extent, Hitler came to power legally. After the failed Munich putsch of nineteen twenty-three, "
        "he chose the institutions. In July nineteen thirty-two, his party won thirty-seven point four per cent, and became the first party in the Reichstag. "
        "Then, on the thirtieth of January, nineteen thirty-three, President Hindenburg appointed him chancellor, as the constitution allowed.",
        "{mod2.2}However, this legal path was prepared by violence, since the S. A. fought the communists in the streets. "
        "And it never rested on a majority. In November nineteen thirty-two, the Nazi vote fell to thirty-three point one per cent. "
        "{mod2.3}Once in office, Hitler used the Reichstag fire to suspend freedoms, and to arrest thousands of communists. "
        "{mod2.4}So his appointment was legal in form. But it was not democratic. And the legal façade served to destroy the republic from inside.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="How far did Hitler come to power legally?",
                    src="Question written for this video, on Part I.2 of the course",
                    enonce=["Assess: weigh both sides, then give a clear judgement"]),
        "pa2": dict(type="pause", t="How far did Hitler come to power legally?",
                    sous="One side, the other side, a judgement. Pause the video, write, then play on for a model."),
        "mod2": dict(type="liste", titre="A model answer", petit=True, items=[
            "Largely legal: the 1923 lesson; 37.4% in July 1932; appointed by Hindenburg, 30 Jan. 1933",
            "But: SA violence; never a majority (33.1% in Nov. 1932); conservative elites",
            "Then: the Reichstag fire → freedoms suspended, communists arrested",
            "Judgement: legal in form, not democratic; a façade to destroy the republic"], x=150, y=140, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}The war was a matrix. Brutalisation, in Mosse's word, brought violence back into politics. "
        "{carte.2}It left three wounds. In Russia, the Bolshevik Revolution, and the Red Scare. In Italy, the mutilated victory, and the red years. "
        "In Germany, defeat, the Diktat, and the stab in the back. "
        "{carte.3}Mussolini had a party, Law and Order, the fasces and the Blackshirts. The March on Rome was intimidation, not a coup. "
        "{carte.4}And Hitler? The lesson of nineteen twenty-three. The S. A. and the S. S. The crisis, and thirty-seven point four per cent. "
        "The legal appointment of the thirtieth of January, nineteen thirty-three. And the Reichstag fire.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: three regimes, three ideologies. The nation. The class. The race.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="FROM THE WAR TO POWER", branches=[
            dict(t="The war as a matrix", items=["brutalisation (Mosse)", "Hitler, soldier 1915", "violence into politics"]),
            dict(t="Three wounds", items=["Russia: Oct. 1917, Red Scare", "Italy: mutilated victory", "Germany: Diktat, stab in back"]),
            dict(t="Mussolini", items=["Law and Order · fasces", "Blackshirts, landowners", "March on Rome, Oct. 1922"]),
            dict(t="Hitler", items=["1923 putsch → institutions", "37.4% · never a majority", "30 Jan. 1933 · Reichstag fire"])]),
        "fin": dict(type="mot", t="Next: three regimes, three ideologies", g="Episode 3 · nation, class, race", y=270, taille=66),
    }),
]

QUIZ = [
    dict(q="What did George Mosse mean by “brutalisation”?",
         r=["The war made violence ordinary, and soldiers brought it back into politics", "The brutal conditions of the Versailles treaty",
            "The repression of the Spartacists", "The Bolshevik terror in Russia"], ok=0, voir="def1",
         ex="For Mosse, WW1 is the “matrix of totalitarianism”: uniforms, ranks, parades, contempt for human life."),
    dict(q="What is the difference between the Red Scare and the Red Terror?",
         r=["The Red Scare is the fear of communism in the West; the Red Terror is Bolshevik violence inside Russia",
            "They are the same thing", "The Red Scare is Stalin's purges", "The Red Terror is the Biennio Rosso"], ok=0, voir="mots1",
         ex="The Bolsheviks' Marxism meant the end of private property: it frightened Europe."),
    dict(q="Who paid the Blackshirts during the Biennio Rosso?",
         r=["The landowners", "The king", "The Socialist Party", "The workers of Turin"], ok=0, voir="br",
         ex="Fascism grew as the armed wing of the frightened propertied classes."),
    dict(q="What did the stab-in-the-back myth claim?",
         r=["The German army had not been beaten at the front but betrayed at home", "Germany had started the war",
            "The Spartacists had won in 1919", "Italy had betrayed Germany"], ok=0, voir="dol",
         ex="It blamed democrats, pacifists, socialists or Jews, as on the German postcard of 1919."),
    dict(q="What lesson did Hitler draw from the failed Munich putsch of 1923?",
         r=["Power had to be won through the institutions", "Power had to be won by a larger coup",
            "The party should ally with the communists", "He should leave politics"], ok=0, voir="les",
         ex="In prison he wrote Mein Kampf (1924–25), setting out his racist views."),
    dict(q="How did Mussolini come to power in October 1922?",
         r=["By intimidation: the threat of the March on Rome pushed the king to appoint him", "By winning a majority in elections",
            "By an armed coup that took Rome", "After the king's abdication"], ok=0, voir="int",
         ex="King Victor Emmanuel III refused martial law and appointed him prime minister on 30 October 1922."),
    dict(q="What was the NSDAP's best score in a free election?",
         r=["37.4% in July 1932", "51% in November 1932", "18.3% in September 1930", "2.6% in May 1928"], ok=0, voir="gv",
         ex="The largest party, but never a majority; it fell to 33.1% in November 1932."),
    dict(q="What did the Nazis do after the Reichstag fire of 27 February 1933?",
         r=["Blamed the communists, suspended civil liberties and arrested thousands of communists", "Called new free elections",
            "Arrested the SA leaders", "Restored the monarchy"], ok=0, voir="rf",
         ex="Who started the fire is still debated: what matters is how the regime used it."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H2 · Parts I.1 “The legacy of WW1” and I.2 “The seizure of power”), with the schemas “Three wounds of the war”, “Two movements, the same building blocks”, “The end of Weimar” (unemployment values read off M. Ros's chart, rounded) and “Two roads to power”, as written on the site; animated map of chapter 2 (site).",
    "Points to handle with care (site's checks): Red Scare and Red Terror; the March on Rome usually dated 27–31 October 1922, with estimates up to 25,000–30,000 marchers; Hitler explains the swastika in Mein Kampf.",
    "Added from outside the course: the 25-point programme of 1920; the size of the SA by 1933; the date of the Potsdam ceremony (21 March 1933) and of the emergency decree (28 February 1933).",
    "Photographs (via Wikimedia Commons): Ypres cathedral in ruins, 1917 (Henry Armytage Sanders, Archives New Zealand, CC BY-SA 2.0); a Spartacist barricade, Berlin, January 1919 (Illustrirte Zeitung, public domain); Red Guards occupying the factories, Italy, 1920 (unknown photographer, public domain); unemployed SA men, Berlin, 1932 (Bundesarchiv, Bild 146-1985-054-02, CC BY-SA 3.0 DE); Hitler and Hindenburg at Potsdam, 21 March 1933 (Bundesarchiv, Bild 183-S38324, CC BY-SA 3.0 DE).",
    "Paintings: Lenin at the Putilov factory, May 1917, by Isaak Brodsky, 1929 (public domain); Mussolini and the quadrumvirs of the March on Rome, commemorative painting by an unknown artist (photograph Silvio Galimberti, CC BY-SA 4.0).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
