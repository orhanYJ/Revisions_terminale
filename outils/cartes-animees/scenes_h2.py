"""Scènes de la carte animée H2 « Totalitarian Regimes » (cours de M. Ros, introduction à III.3, jusqu'au 3 septembre 1939).
Même format que scenes_h3.py ; ce qui vient d'ailleurs que le cours porte la balise [hors].
"""
import scenes_h3 as base
import scenes_h1 as h1
from scenes_h3 import L, F, G33, G38, IT, USSR, DEMO, NEUTRE, UK, JAP, ROUGE, BLEU, NOIR, ALLIE, SU

TITRE = {"fr": "Les régimes totalitaires, 1917-1939 : la carte animée", "en": "Totalitarian regimes, 1917–1939: the animated map"}
PARTIES = {
    "Intro": {"fr": "Définir le totalitarisme", "en": "Defining totalitarianism"},
    "I.1": {"fr": "L'héritage de la Première Guerre mondiale", "en": "The legacy of WW1"},
    "I.2": {"fr": "La prise du pouvoir", "en": "The seizure of power"},
    "I.3": {"fr": "Les spécificités de chaque régime", "en": "Specific aspects of each regime"},
    "II.1": {"fr": "Culte du chef et culte du parti", "en": "Cult of personality and of the party"},
    "II.2": {"fr": "Contrôle total et « homme nouveau »", "en": "Total control and the “New Man”"},
    "II.3": {"fr": "La terreur de masse", "en": "Mass terror"},
    "III.1": {"fr": "Les ambitions hégémoniques", "en": "Hegemonic ambitions"},
    "III.2": {"fr": "Des démocraties incapables de les arrêter", "en": "Democracies unable to stop them"},
    "III.3": {"fr": "La marche vers la guerre", "en": "The road to WWII"},
}
OVERLAY = base.OVERLAY
OCC = base.OCC
FRONTS = {}
AUTO = "#EFE3C4"
ordre = base.ordre

CLES = dict(h1.CLES)
CLES.update({
    "demo": {"c": [DEMO, None], "fr": "Démocraties", "en": "Democracies"},
    "auto": {"c": [AUTO, None], "fr": "Autres dictatures", "en": "Other dictatorships"},
    "fasc": {"c": [IT, None], "fr": "Italie fasciste", "en": "Fascist Italy"},
    "nazi": {"c": [G33, None], "fr": "Allemagne nazie", "en": "Nazi Germany"},
    "stal": {"c": [USSR, None], "fr": "URSS", "en": "USSR"},
    "weimar": {"c": ["#9DB4CC", None], "fr": "République de Weimar", "en": "Weimar Republic"},
    "perdu": {"c": [DEMO, "#5E1C19"], "fr": "Perdu par l'Allemagne en 1919", "en": "Lost by Germany in 1919"},
    "sdn": {"c": [NEUTRE, "#6B6350"], "fr": "Sarre, sous la SDN", "en": "Saar, under the League"},
    "holodomor": {"c": ["#3B2F2F", "#8E2F2A"], "fr": "Ukraine soviétique : famine de 1932-33", "en": "Soviet Ukraine: famine of 1932–33"},
    "espagne": {"c": [AUTO, "#B8924F"], "fr": "Espagne en guerre civile", "en": "Spain in civil war"},
    "front18": {"c": ["line", NOIR], "fr": "Front de l'Ouest, 1915-1918 (approximatif)", "en": "Western Front, 1915–1918 (approximate)"},
})

LABELS = dict(h1.LABELS)
LABELS.update({
    "petrograd": {"p": [30.32, 59.93], "fr": "Petrograd", "en": "Petrograd", "t": "evt", "dx": -7},
    "leningrad24": {"p": [30.32, 59.93], "fr": "Leningrad (1924)", "en": "Leningrad (1924)", "t": "evt"},
    "stalingrad25": {"p": [44.50, 48.71], "fr": "Stalingrad (1925)", "en": "Stalingrad (1925)", "t": "evt"},
    "fiume": {"p": [14.44, 45.33], "fr": "Fiume", "en": "Fiume", "t": "evt"},
    "turin": {"p": [7.68, 45.07], "fr": "Turin", "en": "Turin", "t": "evt", "dx": -7},
    "nuremberg": {"p": [11.08, 49.45], "fr": "Nuremberg", "en": "Nuremberg", "t": "evt"},
    "potsdam": {"p": [13.06, 52.39], "fr": "Potsdam", "en": "Potsdam", "t": "ville", "dx": -7},
    "hanovre": {"p": [9.73, 52.37], "fr": "Hanovre", "en": "Hanover", "t": "evt", "dx": -7},
    "dachau": {"p": [11.43, 48.26], "fr": "Dachau", "en": "Dachau", "t": "evt"},
    "lipari": {"p": [14.95, 38.47], "fr": "Lipari (confino)", "en": "Lipari (confino)", "t": "evt"},
    "novosibirsk": {"p": [82.92, 55.03], "fr": "Novossibirsk", "en": "Novosibirsk", "t": "evt"},
    "donbass": {"p": [38.60, 48.50], "fr": "Donbass (Stakhanov)", "en": "Donbas (Stakhanov)", "t": "evt"},
    "mexico": {"p": [-99.16, 19.35], "fr": "Mexico (Trotski, 1940)", "en": "Mexico City (Trotsky, 1940)", "t": "evt"},
    "stresa": {"p": [8.54, 45.88], "fr": "Stresa", "en": "Stresa", "t": "evt", "dx": -7},
    "canal": {"p": [34.8, 63.7], "fr": "Canal mer Blanche-Baltique", "en": "White Sea–Baltic Canal", "t": "evt", "dx": -7},
    "guernica": {"p": [-2.68, 43.31], "fr": "Guernica", "en": "Guernica", "t": "evt"},
    "nanjing37": {"p": [118.80, 32.06], "fr": "Nankin", "en": "Nanjing", "t": "evt"},
    "verdun": {"p": [5.39, 49.16], "fr": "Verdun", "en": "Verdun", "t": "ville"},
    "rome_p": {"p": [12.50, 41.90], "fr": "Rome", "en": "Rome", "t": "evt"},
    "berlin_p": {"p": [13.40, 52.52], "fr": "Berlin", "en": "Berlin", "t": "evt"},
    "moscou_p": {"p": [37.62, 55.75], "fr": "Moscou", "en": "Moscow", "t": "evt"},
    "l_ukr32": {"p": [32.0, 48.6], "fr": "Ukraine", "en": "Ukraine", "c": "w"},
    "l_siberie": {"p": [75.0, 60.0], "fr": "Sibérie", "en": "Siberia", "t": "mer"},
    "l_kaz": {"p": [67.0, 48.0], "fr": "Kazakhstan", "en": "Kazakhstan", "t": "mer"},
    "l_alsace": {"p": [7.0, 48.5], "fr": "Alsace-Lorraine", "en": "Alsace-Lorraine", "t": "evt", "dx": 8},
    "l_danzig": {"p": [18.6, 54.35], "fr": "Dantzig", "en": "Danzig", "t": "evt"},
    "l_sarre": {"p": [6.9, 49.35], "fr": "Sarre", "en": "Saar", "t": "evt", "dx": -8},
    "l_esp2": {"p": [-3.8, 40.0], "fr": "Espagne", "en": "Spain"},
    "l_ita_n": {"p": [12.8, 42.6], "fr": "Italie", "en": "Italy", "c": "w"},
    "l_axe": {"p": [12.5, 47.5], "fr": "L'Axe Rome-Berlin", "en": "The Rome–Berlin Axis", "t": "evt", "dx": 0, "dy": -14},
})

FRONT_OUEST = [(2.75, 51.13), (2.88, 50.85), (2.88, 50.69), (2.78, 50.29), (2.65, 50.0), (3.0, 49.58), (3.32, 49.38), (4.03, 49.26), (5.39, 49.16),
               (5.54, 48.89), (6.06, 48.9), (6.5, 48.6), (7.0, 48.2), (7.1, 47.8), (7.15, 47.5)]

DEMO_K = ("ru", "irlande", "france", "belgium", "netherlands", "luxembourg", "switzerland", "denmark", "norway", "sweden", "finlande", "carelie",
          "iceland", "boheme", "slovaquie", "sudetes")
AUTO_K = ("portugal", "spain", "hungary", "roumanie", "bessarabie", "yugoslavia", "bulgaria", "greece", "albanie", "baltes", "turquie",
          "pologne_all", "pologne_urss", "danzig")


def europe(etape):
    """Couleurs politiques de l'Europe : 1920 (avant Mussolini), 1923, 1933, 1938."""
    col = {k: [DEMO, None] for k in DEMO_K}
    col.update({k: [AUTO, None] for k in AUTO_K})
    col["urss"] = [USSR, None]
    col["germany"] = ["#9DB4CC", None]
    col["austria"] = ["#9DB4CC", None]
    col["saar"] = [NEUTRE, "#6B6350"]
    col["italie"] = [DEMO, None]
    if etape >= 1923:
        col["italie"] = [IT, None]
    if etape >= 1933:
        col["germany"] = [G33, None]
        col["austria"] = [AUTO, None]
    return col


def scenes():
    S = []

    def add(part, d, cam, date, titre, texte, **kw):
        s = {"part": part, "d": d, "cam": cam, "date": date, "titre": titre, "texte": texte}
        s.update(kw)
        S.append(s)

    # ---------------- Introduction
    add("Intro", 14, [-25, 45, 1.2], L("1929", "1929"),
        L("Deux crises s'ouvrent en même temps", "Two crises open at once"),
        L("Deux photographies de la même année ouvrent le chapitre : la foule devant la Bourse de New York après le krach, et Hitler au congrès du parti nazi à Nuremberg. Crise du capitalisme et menace totalitaire : laquelle mène à la guerre, ou les deux ?",
          "Two photographs from the same year open the chapter: the crowd outside the New York Stock Exchange after the crash, and Hitler at the Nazi Party Congress in Nuremberg. The crisis of capitalism and the totalitarian threat: which led to war — or both?"),
        st={"w:United States": ["#4F7CA6", None], "germany": ["#9DB4CC", None]}, pins=["newyork", "nuremberg"], cles=["usa", "weimar"])
    add("Intro", 15, [25, 50, 2.4], L("1922-1953", "1922–1953"),
        L("Trois régimes, une même trajectoire", "Three regimes, one trajectory"),
        L("Le totalitarisme veut le contrôle total de la société, par la contrainte (terreur et propagande), pour transformer l'homme selon une idéologie. Trois régimes : l'URSS de Staline (1924-1953), l'Italie fasciste (1922-1943), l'Allemagne nazie (1933-1945). La classe, la nation, la race : nés du renversement d'un cadre démocratique, ils mènent à la guerre et finissent tous par échouer.",
          "Totalitarianism seeks total control of society, through coercion (terror and propaganda), to transform man according to an ideology. Three regimes: Stalin's USSR (1924–1953), Fascist Italy (1922–1943), Nazi Germany (1933–1945). Class, nation, race: born from the overthrow of a democratic framework, they paved the way to war and all ended in failure."),
        st=europe(1933), labels=["l_urss", "l_ita_n", "l_all"], cles=["stal", "fasc", "nazi", "demo", "auto"])

    # ---------------- I.1 l'héritage de la guerre
    add("I.1", 15, [4.8, 49.4, 7.2], L("1914-1918", "1914–1918"),
        L("La brutalisation : les régimes nés dans les tranchées", "Brutalisation: regimes born in the trenches"),
        L("Pour l'historien George Mosse, quatre ans de tuerie de masse ont habitué les soldats à la violence, qu'ils rapportent dans la vie politique d'après-guerre : la Grande Guerre est la « matrice du totalitarisme ». Uniformes, grades, défilés et mépris de la vie humaine viennent du front. Hitler y est soldat en 1915.",
          "For the historian George Mosse, four years of mass killing accustomed soldiers to violence, which they brought back into post-war politics: the Great War is the “matrix of totalitarianism”. Uniforms, ranks, parades and contempt for human life come from the front. Hitler was a soldier there in 1915."),
        st=europe(1920), labels=["verdun", "l_fra", "l_all"], cles=["front18"],
        arrows=[{"id": "front18", "ligne": FRONT_OUEST, "col": NOIR, "w": 3.4, "nohead": True, "dur": 2.6}])
    add("I.1", 15, [38, 57, 2.6], L("Février - octobre 1917", "February – October 1917"),
        L("Russie : révolution, coup d'État bolchevik, guerre civile", "Russia: revolution, Bolshevik coup, civil war"),
        L("En février 1917, le tsar abdique. En octobre, les bolcheviks de Lénine et Trotski s'emparent du pouvoir avec l'appui des soviets, signent la paix avec l'Allemagne puis gagnent la guerre civile contre les Blancs (jusqu'en 1922). L'URSS est créée en 1922 : la fin de la propriété privée effraie l'Europe, c'est la « peur rouge ».",
          "In February 1917 the Tsar abdicated. In October the Bolsheviks of Lenin and Trotsky seized power with the support of the soviets, made peace with Germany, then won the civil war against the Whites (until 1922). The USSR was created in 1922: the end of private property frightened Europe — the Red Scare."),
        pins=["petrograd"], labels=["moscou", "l_urss"], cles=["stal"])
    add("I.1", 15, [11.5, 44.5, 5.5], L("1919-1920", "1919–1920"),
        L("Italie : la « victoire mutilée » et le Biennio Rosso", "Italy: the “mutilated victory” and the Biennio Rosso"),
        L("L'Italie n'obtient pas toutes les terres promises : les nationalistes parlent de « victoire mutilée », et D'Annunzio occupe Fiume de septembre 1919 à décembre 1920. Pendant les « deux années rouges », paysans et ouvriers occupent terres et usines (grève générale de Turin, 1920) ; payés par les propriétaires, les Chemises noires les répriment.",
          "Italy did not get all the lands it had been promised: nationalists spoke of a “mutilated victory”, and D'Annunzio held Fiume from September 1919 to December 1920. During the “two red years” peasants and workers occupied land and factories (the Turin general strike, 1920); paid by landowners, the Blackshirts crushed them."),
        pins=["fiume", "turin"], labels=["rome"], cles=["demo"])
    add("I.1", 14, [12.5, 52.0, 6.0], L("Novembre 1918 - janvier 1919", "November 1918 – January 1919"),
        L("Allemagne : une république née dans la violence", "Germany: a republic born in violence"),
        L("La défaite met fin à l'Empire allemand ; la république de Weimar est proclamée. En janvier 1919, l'insurrection spartakiste de Rosa Luxemburg et Karl Liebknecht tente une révolution à la russe et échoue ; tous deux sont assassinés par des corps francs le 15 janvier.",
          "Defeat ended the German Empire; the Weimar Republic was proclaimed. In January 1919 the Spartacist uprising of Rosa Luxemburg and Karl Liebknecht attempted a Russian-style revolution and failed; both were murdered by Freikorps soldiers on 15 January."),
        pins=["berlin_p"], labels=["l_all"], cles=["weimar"])
    add("I.1", 16, [12.0, 51.2, 4.9], L("1919", "1919"),
        L("Le « Diktat » de Versailles et le coup de poignard dans le dos", "The Versailles “Diktat” and the stab in the back"),
        L("Le traité est imposé, pas négocié : clause de culpabilité, perte de l'Alsace-Lorraine et des territoires de l'Est, réparations énormes, Rhénanie démilitarisée, Sarre confiée à la SDN. Les militaires répandent le mythe du « coup de poignard dans le dos » : l'armée n'aurait pas été battue mais trahie, par les démocrates, les socialistes ou les Juifs.",
          "The treaty was imposed, not negotiated: the War Guilt Clause, the loss of Alsace-Lorraine and the eastern territories, huge reparations, a demilitarised Rhineland, the Saar placed under the League. The military spread the “stab in the back” myth: the army had not been beaten but betrayed — by democrats, socialists or Jews."),
        st={"fr_annex": [DEMO, "#5E1C19"], "danzig": [NEUTRE, "#6B6350"], "rhenanie": [None, "#17233F"]},
        labels=["l_alsace", "l_danzig", "l_sarre", "l_rhen"], cles=["weimar", "perdu", "sdn", "rhen"])
    add("I.1", 14, [11.6, 48.6, 7.5], L("Novembre 1923", "November 1923"),
        L("Le putsch manqué de Munich ; Mein Kampf", "The failed Munich putsch; Mein Kampf"),
        L("En 1923, Hitler tente de prendre le pouvoir par la force à Munich et échoue : il en tire la leçon qu'il faut conquérir le pouvoir par les institutions. En prison, il écrit Mein Kampf (1924-1925), où il expose déjà ses idées racistes. La guerre a créé les rancœurs ; la crise des années 1930 en fera des voix.",
          "In 1923 Hitler tried to seize power by force in Munich and failed: he drew the lesson that power had to be won through the institutions. In prison he wrote Mein Kampf (1924–1925), already setting out his racist views. The war created the grievances; the crisis of the 1930s would turn them into votes."),
        st={"fr_annex": [None, None], "rhenanie": [None, None]}, pins=["munich"], cles=["weimar"])

    # ---------------- I.2 la prise du pouvoir
    add("I.2", 15, [12.6, 42.4, 7.0], L("22-30 octobre 1922", "22–30 October 1922"),
        L("La marche sur Rome", "The March on Rome"),
        L("Les Chemises noires marchent sur Rome : environ 20 000 selon la classe, bien moins qu'espéré, non violents pendant la marche, mais chacun sait qu'ils peuvent l'être. La menace suffit : le roi Victor-Emmanuel III refuse l'état de siège et nomme Mussolini président du Conseil le 30 octobre. Une intimidation, pas un coup d'État.",
          "The Blackshirts marched on Rome: about 20,000 according to the class, far fewer than hoped — not violent during the march, but everyone knew they could be. The threat was enough: King Victor Emmanuel III refused martial law and appointed Mussolini prime minister on 30 October. Intimidation, not a coup."),
        st=europe(1923), pins=["rome_p"], cles=["fasc"],
        arrows=[F((12.4, 43.3), (12.45, 42.05), ROUGE, 0.12, w=3, id="mr1"), F((11.6, 42.4), (12.35, 41.95), ROUGE, -0.2, w=3, id="mr2"),
                F((13.4, 42.4), (12.6, 41.95), ROUGE, 0.2, w=3, id="mr3")])
    add("I.2", 15, [10.5, 51.5, 5.2], L("1928-1932", "1928–1932"),
        L("La crise fait des nazis le premier parti", "The crisis makes the Nazis the largest party"),
        L("Chômage et vote nazi montent ensemble : 5,6 millions de chômeurs en 1932 ; le NSDAP passe de 2,6 % (1928) à 18,3 % (1930) et 37,4 % (juillet 1932), puis recule à 33,1 % (novembre 1932). Les SA, force de masse, et les SS, élite, conquièrent la rue. Mais les nazis n'ont jamais la majorité.",
          "Unemployment and the Nazi vote rose together: 5.6 million unemployed in 1932; the NSDAP went from 2.6% (1928) to 18.3% (1930) and 37.4% (July 1932), then fell back to 33.1% (November 1932). The SA, a mass force, and the SS, an elite, conquered the street. But the Nazis never won a majority."),
        pins=["hanovre"], labels=["berlin"], cles=["weimar"])
    add("I.2", 15, [13.2, 52.45, 9.0], L("30 janvier 1933", "30 January 1933"),
        L("Hindenburg nomme Hitler chancelier", "Hindenburg appoints Hitler chancellor"),
        L("Comme Mussolini, Hitler arrive au pouvoir légalement : le président Hindenburg, vieux général de l'Empire, le nomme chancelier ; les conservateurs croient pouvoir le contrôler. Le 21 mars à Potsdam, Hitler s'incline devant Hindenburg : le nazisme se présente en héritier de la vieille Prusse.",
          "Like Mussolini, Hitler came to power legally: President Hindenburg, an old general of the Empire, appointed him chancellor; the conservatives thought they could control him. On 21 March at Potsdam, Hitler bowed to Hindenburg: Nazism presented itself as heir to old Prussia."),
        st={"germany": [G33, None], "austria": [AUTO, None]}, pins=["berlin_p"], labels=["potsdam"], cles=["nazi"])
    add("I.2", 14, [13.4, 52.52, 11], L("27 février 1933", "27 February 1933"),
        L("L'incendie du Reichstag", "The Reichstag fire"),
        L("Un mois plus tard, le Reichstag brûle. Les nazis accusent aussitôt les communistes ; le lendemain, un décret suspend les libertés de la presse, de réunion et d'opinion [hors], et des milliers de communistes sont arrêtés. Qui a mis le feu reste débattu ; l'essentiel est l'usage qu'en fait le régime.",
          "A month later the Reichstag burned. The Nazis immediately blamed the communists; the next day a decree suspended freedom of the press, of assembly and of opinion [hors], and thousands of communists were arrested. Who started the fire is still debated; what matters is how the regime used it."),
        pins=["berlin_p"], cles=["nazi"])

    # ---------------- I.3 spécificités
    add("I.3", 15, [12.5, 41.9, 8.5], L("1924-1925", "1924–1925"),
        L("Fascisme : la dictature rendue légale", "Fascism: the dictatorship made legal"),
        L("Le député socialiste Matteotti, qui dénonçait fraudes et violences, est enlevé et assassiné (1924) ; le 3 janvier 1925, Mussolini en revendique la responsabilité, puis les lois « fascistissimes » font de l'Italie un État totalitaire. Le fascisme veut une « révolution nouvelle » et la grandeur de Rome : « tout est dans l'État » (Doctrine du fascisme, 1932).",
          "The socialist deputy Matteotti, who had denounced fraud and violence, was kidnapped and murdered (1924); on 3 January 1925 Mussolini claimed responsibility, then the “fascistissime” laws made Italy a totalitarian state. Fascism wanted a “new revolution” and the greatness of Rome: “everything is in the State” (Doctrine of Fascism, 1932)."),
        pins=["rome_p"], cles=["fasc"])
    add("I.3", 15, [13.5, 40.5, 5.5], L("1929-1938", "1929–1938"),
        L("Une terreur moins oppressive ? Puis le tournant raciste", "A less oppressive terror? Then the racist turn"),
        L("Mussolini doit composer avec l'Église (accords du Latran, 1929) et le roi ; ses opposants sont surtout relégués dans des îles comme Lipari (le confino) plutôt qu'exécutés. Le fascisme n'est pas raciste à l'origine : le tournant vient en 1938 avec l'alliance hitlérienne (La Difesa della Razza, août 1938, lois antisémites).",
          "Mussolini had to come to terms with the Church (Lateran Accords, 1929) and the king; opponents were mostly sent to islands such as Lipari (the confino) rather than executed. Fascism was not racist at first: the turn came in 1938 with the alliance with Hitler (La Difesa della Razza, August 1938, anti-Semitic laws)."),
        pins=["lipari", "rome_p"], cles=["fasc"])
    add("I.3", 15, [45, 52, 2.0], L("1928-1936", "1928–1936"),
        L("Stalinisme : plan quinquennal et collectivisation forcée", "Stalinism: Five-Year Plan and forced collectivisation"),
        L("Pour le marxisme, l'histoire est une lutte des classes. Le premier plan quinquennal (1928) doit faire de l'URSS une puissance industrielle indépendante du capitalisme et éliminer les derniers éléments capitalistes des campagnes : les fermes sont regroupées en kolkhozes et sovkhozes (7 % des foyers en 1928, 57 % en 1930, 90 % en 1936).",
          "For Marxism, history is class struggle. The first Five-Year Plan (1928) was to make the USSR an industrial power independent of capitalism and to eliminate the last capitalist elements in the countryside: farms were merged into kolkhozes and sovkhozes (7% of households in 1928, 57% in 1930, 90% in 1936)."),
        labels=["l_urss", "moscou"], cles=["stal"])
    add("I.3", 15, [55, 52, 1.6], L("1929-1932", "1929–1932"),
        L("Les koulaks, ennemis de classe", "The kulaks, class enemies"),
        L("Sur le papier, un koulak possède plus de 8 acres ; en pratique, l'étiquette frappe tout paysan qui refuse la collectivisation. Terres et bêtes confisquées, beaucoup sont déportés (vers la Sibérie et le Kazakhstan [hors]). La collectivisation ruine l'agriculture : à Novossibirsk, en 1932, les vaches des kolkhozes donnent 1 à 3 litres de lait au lieu de 5 à 7, « les gens meurent de faim ».",
          "On paper a kulak owned more than 8 acres; in practice the label struck any peasant who refused collectivisation. Land and animals were confiscated and many were deported (to Siberia and Kazakhstan [hors]). Collectivisation ruined farming: in Novosibirsk in 1932, kolkhoz cows gave 1 to 3 litres of milk instead of 5 to 7 — “people are starving”."),
        labels=["l_siberie", "l_kaz", "l_ukr32"], pins=["novosibirsk"], cles=["stal"],
        arrows=[F((33.0, 49.5), (62.0, 58.0), NOIR, -0.12, w=2.8, dash=True, id="kul1", dur=2.6), F((35.0, 48.5), (66.0, 48.5), NOIR, 0.08, w=2.8, dash=True, id="kul2", dur=2.6)])
    add("I.3", 16, [32, 48.8, 4.6], L("1932-1933", "1932–1933"),
        L("L'Holodomor : la famine organisée en Ukraine", "The Holodomor: man-made famine in Ukraine"),
        L("Le grain est réquisitionné quelle que soit la récolte ; les paysans le cachent, des brigades appuyées par l'OGPU viennent le « prendre ». Les villages « rebelles » sont privés de tout ravitaillement. En octobre 1932, seuls 22 % de l'objectif sont atteints. La famine tue environ quatre millions de personnes en Ukraine [hors].",
          "Grain was requisitioned whatever the harvest; peasants hid it, and brigades backed by the OGPU came to “take the grain”. “Rebellious” villages were cut off from all supplies. By October 1932 only 22% of the target had been reached. The famine killed about four million people in Ukraine [hors]."),
        st={"ukraine32": ["#3B2F2F", "#8E2F2A"]}, labels=["l_ukr32", "kiev"], cles=["holodomor"])
    add("I.3", 15, [11, 50.5, 5.0], L("1933-1939", "1933–1939"),
        L("Nazisme : la lutte des races", "Nazism: the struggle of races"),
        L("Pour les nazis, l'histoire est une guerre entre races hiérarchisées ; les Juifs sont décrits comme des « bactéries » à éliminer. Enseignement racial obligatoire dans les écoles (septembre 1933) ; lois de Nuremberg (15 septembre 1935) ; programme T4 (1939) : environ 70 000 Allemands handicapés assassinés.",
          "For the Nazis, history is a war between ranked races; Jews were described as “bacteria” to be eliminated. Compulsory racial instruction in schools (September 1933); the Nuremberg laws (15 September 1935); the T4 programme (1939): about 70,000 disabled Germans murdered."),
        st={"ukraine32": [None, None]}, pins=["nuremberg"], labels=["berlin", "l_all"], cles=["nazi"])

    # ---------------- II.1 le culte du chef
    add("II.1", 15, [37, 55, 2.9], L("1924-1925", "1924–1925"),
        L("Le culte du chef : des villes rebaptisées", "The cult of the leader: renamed cities"),
        L("La propagande fabrique un être supérieur, le Guide : « il Duce », « der Führer », « le petit père des peuples ». Petrograd devient Leningrad en 1924 ; une ville est rebaptisée Stalingrad en 1925. Géorgien, Staline impose pourtant le russe à toute l'Union (obligatoire dans les écoles en 1938 [hors]).",
          "Propaganda manufactured a superior being, the Guide: “il Duce”, “der Führer”, “the little father of the peoples”. Petrograd became Leningrad in 1924; a city was renamed Stalingrad in 1925. Though Georgian himself, Stalin imposed Russian on the whole Union (compulsory in schools in 1938 [hors])."),
        pins=["leningrad24", "stalingrad25"], labels=["moscou"], cles=["stal"])
    add("II.1", 15, [8, 49.5, 4.6], L("1934-1937", "1934–1937"),
        L("Rassemblements, médias, arts au service du régime", "Rallies, media and arts in the regime's service"),
        L("Le rassemblement de Nuremberg de 1934 est filmé par Leni Riefenstahl (Le Triomphe de la volonté) ; Goebbels dirige la propagande ; la radio bon marché (Volksempfänger) fait entrer la voix du Führer dans chaque foyer. À l'Exposition de Paris (1937), les pavillons soviétique et allemand se font face.",
          "The 1934 Nuremberg rally was filmed by Leni Riefenstahl (Triumph of the Will); Goebbels ran propaganda; the cheap Volksempfänger radio brought the Führer's voice into every home. At the 1937 Paris World Fair, the Soviet and German pavilions faced each other."),
        pins=["nuremberg", "paris"], cles=["nazi", "stal"])

    # ---------------- II.2 l'homme nouveau
    add("II.2", 15, [22, 49, 2.5], L("1918-1936", "1918–1936"),
        L("La jeunesse d'abord : trois « hommes nouveaux »", "Youth first: three “New Men”"),
        L("Un régime totalitaire ne veut pas des sujets obéissants mais un homme nouveau. Opera Nazionale Balilla (1926) en Italie, Jeunesses hitlériennes obligatoires (loi de 1936, environ 8 millions de membres en 1939), Komsomol (1918) en URSS : la race, la classe, la nation.",
          "A totalitarian regime wants not obedient subjects but a New Man. The Opera Nazionale Balilla (1926) in Italy, the compulsory Hitler Youth (law of 1936, about 8 million members by 1939), the Komsomol (1918) in the USSR: race, class, nation."),
        pins=["rome_p", "berlin_p", "moscou_p"], cles=["fasc", "nazi", "stal"])
    add("II.2", 14, [38.6, 48.5, 7.0], L("1935", "1935"),
        L("Stakhanov, héros du travail soviétique", "Stakhanov, hero of Soviet labour"),
        L("En 1935, le mineur Alexeï Stakhanov aurait dépassé quatorze fois sa norme en une seule équipe : le stakhanovisme impose la compétition dans chaque usine. Syndicats dissous, loisirs encadrés, économie dirigée : rien ne doit rester hors du régime.",
          "In 1935 the miner Alexei Stakhanov was presented as having cut fourteen times his quota in one shift: Stakhanovism imposed competition in every factory. Unions dissolved, leisure organised, the economy directed: nothing was to stay outside the regime."),
        pins=["donbass"], cles=["stal"])

    # ---------------- II.3 la terreur
    add("II.3", 15, [16, 50, 3.0], L("1927-1936", "1927–1936"),
        L("Des polices politiques au-dessus des lois ; les camps", "Political police above the law; the camps"),
        L("OVRA en Italie (1927), Gestapo (1933) et SS dirigées toutes deux par Himmler (1936), NKVD (1934) en URSS. Dachau ouvre en 1933 ; les détenus y sont classés par triangles de couleur. Comme le dit M. Ros, les nazis n'ont pas inventé le camp : ils y ont ajouté la chambre à gaz.",
          "The OVRA in Italy (1927), the Gestapo (1933) and the SS, both headed by Himmler (1936), the NKVD (1934) in the USSR. Dachau opened in 1933; prisoners were sorted by coloured triangles. As M. Ros put it, the Nazis did not invent the camp: what they added was the gas chamber."),
        pins=["dachau"], labels=["rome", "berlin", "moscou"], cles=["fasc", "nazi", "stal"])
    add("II.3", 14, [34.8, 63.6, 6.5], L("1931-1933", "1931–1933"),
        L("Le Goulag : le canal de la mer Blanche", "The Gulag: the White Sea Canal"),
        L("Le Goulag place ses camps là où il faut de la main-d'œuvre : mines, forêts, canaux. Le canal de la mer Blanche à la Baltique, 227 km creusés de 1931 à 1933 presque à la main, est le premier grand chantier des détenus. La population des camps dépassera 1,5 million au début des années 1950.",
          "The Gulag put its camps where labour was needed: mines, forests, canals. The White Sea–Baltic Canal, 227 km dug between 1931 and 1933 largely by hand, was the first great project built by prisoners. The camp population would pass 1.5 million in the early 1950s."),
        pins=["canal"], cles=["stal"],
        arrows=[{"id": "canalw", "ligne": [(34.83, 62.85), (34.5, 63.2), (34.4, 63.6), (34.6, 64.0), (34.78, 64.52)], "col": ROUGE, "w": 4, "nohead": True, "dur": 2.0}])
    add("II.3", 15, [37.6, 55.75, 8.0], L("1936-1938", "1936–1938"),
        L("Les procès de Moscou et la Grande Purge", "The Moscow show trials and the Great Purge"),
        L("De vieux bolcheviks avouent des crimes imaginaires après des menaces sur leur famille (Zinoviev, Kamenev, 1936). La Grande Purge de 1937-38 fait 680 000 exécutions, décime le parti et affaiblit l'armée. En Allemagne, la Nuit des longs couteaux (1934) a déjà fait 85 morts, dont les chefs des SA.",
          "Old Bolsheviks confessed to imaginary crimes after threats to their families (Zinoviev, Kamenev, 1936). The Great Purge of 1937–38 made 680,000 executions, decimated the party and weakened the army. In Germany the Night of the Long Knives (1934) had already left 85 dead, among them the SA leadership."),
        pins=["moscou_p"], cles=["stal"])
    add("II.3", 15, [-99.1, 19.4, 5.0], L("1940", "1940"),
        L("La terreur dévore les siens, jusqu'au Mexique", "Terror devours its own, as far as Mexico"),
        L("Personne n'est à l'abri : Iejov, chef du NKVD, est exécuté en 1940 et effacé des photographies. La terreur va jusqu'à l'étranger : Trotski, principal rival de Staline, est assassiné au Mexique en 1940 par un agent de la police soviétique.",
          "No one was safe: Yezhov, head of the NKVD, was executed in 1940 and erased from the photographs. Terror reached abroad: Trotsky, Stalin's most influential rival, was assassinated in Mexico in 1940 by an agent of the Soviet police."),
        pins=["mexico"], cles=["stal"], lent=1.1)

    # ---------------- III.1 ambitions hégémoniques
    add("III.1", 16, [28, 20, 2.0], L("1911-1936", "1911–1936"),
        L("L'Éthiopie : un empire au nom de Rome", "Abyssinia: an empire in the name of Rome"),
        L("Mussolini invoque l'Empire romain : il achève la colonisation brutale de la Libye (commencée en 1911-1912), puis attaque l'Éthiopie en octobre 1935 ; ses troupes entrent à Addis-Abeba en mai 1936. La SDN débat des sanctions pendant sept mois, et en exclut le pétrole.",
          "Mussolini invoked the Roman Empire: he completed the brutal colonisation of Libya (begun in 1911–1912), then attacked Ethiopia in October 1935; his troops entered Addis Ababa in May 1936. The League debated sanctions for seven months — and left out oil."),
        st={"w:Libya (IT)": [IT, None], "w:Eritrea": [IT, None], "w:Italian Somaliland": [IT, None], "w:Ethiopia": [IT, "#5A4630"]},
        labels=["l_libye", "l_ethio", "rome"], pins=["addis"], cles=["fasc"],
        arrows=[F((39.0, 15.5), (38.9, 9.6), IT, 0.15, w=3, id="eth1"), F((45.0, 4.0), (40.0, 8.0), IT, -0.15, w=3, id="eth2")])
    add("III.1", 15, [28, 52, 2.4], L("1901-1925", "1901–1925"),
        L("Le Lebensraum : conquérir l'Est", "Lebensraum: conquering the East"),
        L("Le géographe Ratzel (1901) : une nation a besoin d'un territoire et de ressources pour survivre (l'autarcie). Dans Mein Kampf (1925), Hitler en fait un plan : conquérir les terres slaves, y installer des colons allemands, déporter les Russes en Sibérie, asservir les autres. Le vieux slogan disait déjà « Drang nach Osten ».",
          "The geographer Ratzel (1901): a nation needs territory and resources to survive (autarky). In Mein Kampf (1925) Hitler turned it into a plan: conquer the Slavic lands, settle German colonists there, deport the Russians to Siberia, enslave the rest. The old slogan already said “Drang nach Osten”."),
        labels=["l_all", "l_urss", "l_pol"], cles=["nazi", "stal"],
        arrows=[F((13.5, 52.0), (38.0, 53.0), G33, -0.1, w=3.6, dash=True, id="leb", dur=2.8)])
    add("III.1", 15, [122, 38, 2.4], L("1931-1937", "1931–1937"),
        L("L'impérialisme japonais : autarcie et « race supérieure »", "Japanese imperialism: autarky and a “superior race”"),
        L("La crise de 1929 frappe le commerce japonais : le Japon veut l'autarcie, et occupe la Mandchourie dès 1931 pour son grain et ses minerais. Il se dit race supérieure destinée à guider l'Asie (panasiatisme), rancunier d'un Occident qui avait rejeté sa clause d'égalité raciale en 1919. Il quitte la SDN en 1933.",
          "The 1929 crisis hit Japanese trade: Japan wanted autarky, and occupied Manchuria from 1931 for its grain and minerals. It claimed to be a superior race destined to lead Asia (Pan-Asianism), resentful of a West that had rejected its racial equality clause in 1919. It left the League in 1933."),
        st={"w:Empire of Japan": [JAP, None], "w:Manchuria": ["#E9D9C4", JAP]}, pins=["moukden"], labels=["l_jap", "l_mand", "l_chine"], cles=["japon", "mandch"])
    add("III.1", 16, [118, 33, 4.0], L("Décembre 1937", "December 1937"),
        L("Nankin : les traits de la guerre à venir", "Nanjing: the features of the coming war"),
        L("Profitant de la guerre civile entre le Kuomintang de Tchang Kaï-chek et les communistes de Mao, le Japon attaque le reste de la Chine en 1937. Le massacre de Nankin (décembre 1937 - janvier 1938) : de 200 000 à 300 000 civils et prisonniers tués. Idéologie raciste, militarisme, civils pris pour cibles : la guerre mondiale s'annonce.",
          "Taking advantage of the civil war between Chiang Kai-shek's Kuomintang and Mao's communists, Japan attacked the rest of China in 1937. The Rape of Nanjing (December 1937 – January 1938): from 200,000 to 300,000 civilians and prisoners killed. Racist ideology, militarism, civilians as targets: the world war was coming."),
        pins=["nanjing37"], labels=["l_chine"], cles=["japon"],
        arrows=[F((121.4, 31.3), (119.0, 32.0), JAP, 0.15, w=3, id="nk1"), F((116.4, 39.5), (117.5, 33.5), JAP, -0.1, w=3, id="nk2")])

    # ---------------- III.2 des démocraties impuissantes
    add("III.2", 16, [8, 47, 4.2], L("1935", "1935"),
        L("Stresa, la Wehrmacht et l'accord naval", "Stresa, the Wehrmacht and the naval agreement"),
        L("En avril 1935, Britanniques et Français tentent à Stresa un front avec l'Italie contre l'Allemagne, et ménagent donc Mussolini sur l'Éthiopie. Mais l'Allemagne réarme : la Wehrmacht est créée en 1935, et dès juin le Royaume-Uni signe seul un accord naval l'autorisant à 35 % de sa flotte. L'Amérique, elle, vote ses lois de neutralité.",
          "In April 1935 Britain and France tried to build a front with Italy at Stresa against Germany, and so spared Mussolini over Ethiopia. But Germany was rearming: the Wehrmacht was created in 1935, and in June Britain alone signed a naval agreement allowing it 35% of the Royal Navy. America, for its part, passed its Neutrality Acts."),
        st=europe(1933), pins=["stresa"], labels=["londres", "paris", "berlin"], cles=["demo", "fasc", "nazi"])
    add("III.2", 15, [2, 50, 3.4], L("1937-1938", "1937–1938"),
        L("L'apaisement : pourquoi les démocraties cèdent", "Appeasement: why the democracies gave way"),
        L("Chamberlain (dès 1937) et Daladier acceptent les exigences de l'Axe pour éviter la guerre. Leurs raisons : le souvenir de 1914-1918 et le pacifisme (le vote de l'Oxford Union, 1933), un empire à surveiller (l'Inde) et un Commonwealth incertain (le Canada), la crise d'abord, l'isolationnisme américain, la peur du communisme plus forte que celle du fascisme.",
          "Chamberlain (from 1937) and Daladier accepted the Axis demands to avoid war. Their reasons: the memory of 1914–1918 and pacifism (the Oxford Union vote, 1933), an empire to police (India) and an uncertain Commonwealth (Canada), their economic problems first, American isolationism, and a greater fear of communism than of fascism."),
        labels=["londres", "paris"], cles=["demo", "nazi", "fasc"])

    # ---------------- III.3 la marche à la guerre
    add("III.3", 16, [3, 45, 3.6], L("1936", "1936"),
        L("L'Axe Rome-Berlin ; la guerre d'Espagne", "The Rome–Berlin Axis; the Spanish Civil War"),
        L("Malgré leur méfiance, Hitler et Mussolini s'allient : l'Axe Rome-Berlin est proclamé le 25 octobre 1936 (pacte d'Acier en 1939, Japon en 1940). En Espagne, l'Allemagne et l'Italie soutiennent Franco, et l'aviation allemande s'y entraîne (Guernica, avril 1937 [hors]) ; la France et le Royaume-Uni n'interviennent pas.",
          "Despite their mistrust, Hitler and Mussolini allied: the Rome–Berlin Axis was declared on 25 October 1936 (Pact of Steel in 1939, Japan in 1940). In Spain, Germany and Italy supported Franco, and the German air force trained there (Guernica, April 1937 [hors]); France and Britain did not intervene."),
        st={"spain": [AUTO, "#B8924F"]}, labels=["l_axe", "l_esp2"], pins=["guernica"], cles=["espagne", "fasc", "nazi"],
        arrows=[{"id": "axe", "ligne": [(12.5, 41.9), (12.2, 44.5), (11.8, 47.5), (12.6, 50.0), (13.4, 52.5)], "col": NOIR, "w": 3, "nohead": True, "dash": True, "dur": 2.2},
                F((12.0, 42.0), (-1.0, 40.0), IT, 0.15, w=2.6, dash=True, id="esp1"), F((11.0, 50.0), (-2.5, 42.6), G33, 0.15, w=2.6, dash=True, id="esp2")])
    add("III.3", 15, [7.5, 50.3, 6.2], L("7 mars 1936", "7 March 1936"),
        L("La Rhénanie : le pari réussi", "The Rhineland: the gamble pays off"),
        L("Les troupes allemandes entrent dans la Rhénanie démilitarisée, avec l'ordre de reculer si la France réagit. Elle ne réagit pas, ni le Royaume-Uni : le pari de Hitler réussit, et lui apprend que les démocraties céderont.",
          "German troops entered the demilitarised Rhineland, with orders to retreat if France reacted. Neither France nor Britain did: Hitler's gamble paid off, and taught him that the democracies would yield."),
        st={"spain": [AUTO, None], "saar": [G33, None], "rhenanie": [None, "#F7F3EA"]}, labels=["l_rhen", "paris"], cles=["nazi", "rhen"],
        arrows=[F((10.0, 51.5), (7.4, 50.9), ROUGE, 0.2, w=3, id="rh1"), F((9.8, 49.7), (7.6, 49.6), ROUGE, -0.2, w=3, id="rh2")])
    add("III.3", 15, [15, 48, 6.0], L("12 mars 1938", "12 March 1938"),
        L("L'Anschluss", "The Anschluss"),
        L("Hitler menace le chancelier autrichien Schuschnigg et masse ses troupes à la frontière ; le nazi Seyss-Inquart devient chancelier et appelle l'armée allemande, qui entre à Vienne le 12 mars 1938. Le plébiscite, d'où opposants et Juifs (8 % de la population) sont exclus, donne 99 % de oui.",
          "Hitler bullied the Austrian chancellor Schuschnigg and massed troops on the border; the Nazi Seyss-Inquart became chancellor and invited the German army in — it entered Vienna on 12 March 1938. The plebiscite, from which opponents and Jews (8% of the population) were excluded, gave 99% yes."),
        st={"rhenanie": [None, None], "austria": [G33, None]}, pins=["vienne38"], labels=["l_aut"], cles=["nazi"],
        arrows=[F((12.6, 48.3), (16.0, 48.2), ROUGE, -0.15, w=3.2, id="ans")])
    add("III.3", 16, [13.5, 50.0, 5.8], L("29-30 septembre 1938", "29–30 September 1938"),
        L("Munich : les Sudètes livrés sans les Tchèques", "Munich: the Sudetenland handed over without the Czechs"),
        L("Hitler exige les Sudètes (environ 3 millions de germanophones) et menace d'envahir la Tchécoslovaquie, dernière démocratie d'Europe centrale. À Munich, Hitler, Chamberlain, Daladier et Mussolini, qui se pose en modéré, les lui accordent ; les Tchèques ne sont pas invités. Hitler promet de ne pas menacer le reste du pays.",
          "Hitler demanded the Sudetenland (about 3 million German speakers) and threatened to invade Czechoslovakia, the last democracy in central Europe. At Munich, Hitler, Chamberlain, Daladier and Mussolini — posing as a moderate — granted it; the Czechs were not invited. Hitler promised not to threaten the rest of the country."),
        st={"sudetes": [G33, None]}, pins=["munich"], labels=["l_sudetes", "prague"], cles=["nazi", "demo"],
        arrows=[F((12.0, 50.0), (13.8, 50.6), ROUGE, 0.2, w=2.6, id="sud1"), F((15.6, 51.0), (16.2, 50.2), ROUGE, -0.2, w=2.6, id="sud2")])
    add("III.3", 15, [18, 50, 4.2], L("15-31 mars 1939", "15–31 March 1939"),
        L("Prague : le mensonge qui met fin à l'apaisement", "Prague: the lie that ended appeasement"),
        L("Le 15 mars 1939, l'Allemagne occupe Prague : ce n'est plus réunir des Allemands, c'est occuper un peuple étranger. La France et le Royaume-Uni changent de cap et garantissent la Pologne (31 mars), la Roumanie et la Grèce.",
          "On 15 March 1939 Germany occupied Prague: no longer uniting Germans, but occupying a foreign people. France and Britain changed course and guaranteed Poland (31 March), Romania and Greece."),
        st={"boheme": [G33, None], "slovaquie": [ALLIE, None], "albanie": [IT, None]}, pins=["prague"], labels=["varsovie"], cles=["nazi", "allie", "demo", "auto"])
    add("III.3", 15, [27, 54, 2.6], L("23 août 1939", "23 August 1939"),
        L("Le pacte germano-soviétique", "The Nazi-Soviet pact"),
        L("Deux ennemis idéologiques signent un pacte de non-agression dont les clauses secrètes partagent la Pologne. Hitler évite une guerre sur deux fronts ; Staline, dont l'armée sort des purges, gagne du temps et des territoires. « Je ne suis pas prêt pour la guerre ! », lui fait dire la caricature du cours.",
          "Two ideological enemies signed a non-aggression pact whose secret terms divided Poland. Hitler avoided a war on two fronts; Stalin, whose army had just been gutted by the purges, gained time and territory. “I am not ready for war!”, says the course's cartoon."),
        pins=["moscou_p", "berlin_p"], cles=["nazi", "stal"])
    add("III.3", 16, [19.5, 52, 4.4], L("1er - 3 septembre 1939", "1–3 September 1939"),
        L("L'attaque de la Pologne : la guerre", "The attack on Poland: war"),
        L("L'Allemagne attaque la Pologne, alliée de la France, le 1er septembre 1939 ; la France et le Royaume-Uni déclarent la guerre le 3. Chaque agression impunie avait préparé la suivante : l'idéologie totalitaire a fourni la volonté d'expansion, la réticence des démocraties l'occasion.",
          "Germany attacked Poland, France's ally, on 1 September 1939; France and Britain declared war on the 3rd. Each unpunished aggression had prepared the next: totalitarian ideology supplied the will to expand, the democracies' reluctance the opportunity."),
        st={"pologne_all": [G38, None], "danzig": [G33, None]}, pins=["varsovie"], labels=["berlin"], cles=["nazi", "occ"],
        arrows=[F((14.4, 52.4), (20.4, 52.2), ROUGE, -0.12, id="pl1"), F((20.6, 54.1), (21.1, 52.5), ROUGE, 0.1, id="pl2"),
                F((15.0, 51.0), (19.6, 51.4), ROUGE, -0.1, id="pl3"), F((19.6, 49.3), (21.7, 50.8), ROUGE, 0.12, id="pl4")])
    return S
