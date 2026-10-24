"""Scènes de la carte animée H1 « The Wall Street Crash and its Impact » (cours de M. Ros, parties I et II).
Même format que scenes_h3.py ; ce qui vient d'ailleurs que le cours porte la balise [hors].
"""
import scenes_h3 as base
from scenes_h3 import L, F, G33, G38, IT, USSR, DEMO, NEUTRE, UK, JAP, USA, ROUGE, BLEU, NOIR

TITRE = {"fr": "Le krach de 1929 et la crise mondiale : la carte animée", "en": "The Wall Street Crash and the world depression: the animated map"}
PARTIES = {
    "1919": {"fr": "L'ordre libéral de 1919 (voir II.3)", "en": "The liberal order of 1919 (see II.3)"},
    "I.1": {"fr": "Qu'est-ce que le krach de 1929 ?", "en": "What is the 1929 Great Crash?"},
    "I.2": {"fr": "Du krach américain à la crise mondiale", "en": "From the US crash to a world-wide crisis"},
    "I.3": {"fr": "Un traumatisme fondateur du XXe siècle", "en": "A defining trauma of the 20th century"},
    "II.1": {"fr": "Le nationalisme économique", "en": "Economic nationalism"},
    "II.2": {"fr": "Les réponses politiques à la crise", "en": "Political responses to the crisis"},
    "II.3": {"fr": "Des démocraties réticentes à défendre l'ordre de 1919", "en": "Democracies reluctant to defend the 1919 order"},
}

CRISE, CRISE2, OR, VERT = "#D88A80", "#EFC7C0", "#B8924F", "#3E6259"
OVERLAY = base.OVERLAY
OCC = base.OCC
FRONTS = {}

EMPIRE_GB = ["w:Canada", "w:British Raj", "w:Australia", "w:New Zealand", "w:Union of South Africa", "w:Kenya", "w:Nigeria", "w:Ghana", "w:Sudan",
             "w:Mesopotamia (GB)", "w:Mandatory Palestine (GB)", "w:Malaysia", "w:Ceylon", "w:Uganda", "w:Tanzania, United Republic of", "w:Zambia",
             "w:Zimbabwe", "w:Malawi", "w:British Somaliland", "w:Botswana", "w:Lesotho", "w:Swaziland", "w:Guyana", "w:Belize", "w:Sierra Leone",
             "w:Gambia, The", "w:Dominion of Newfoundland", "w:Papua New Guinea", "ru"]
EMPIRE_FR = ["w:French West Africa", "w:French Equatorial Africa", "w:Algeria", "w:Morocco", "w:Tunisia", "w:French Indo-China", "w:Annam",
             "w:Cochin China", "w:Madagascar (France)", "w:Syria (France)", "w:French Cameroons", "w:French Guiana", "w:French Somaliland", "w:Togo", "france"]

CLES = dict(base.CLES)
CLES.update({
    "usa": {"c": [USA, None], "fr": "États-Unis", "en": "United States"},
    "demo19": {"c": [DEMO, None], "fr": "Grandes démocraties de 1919", "en": "The great democracies of 1919"},
    "crise": {"c": [CRISE, None], "fr": "Frappé par la crise", "en": "Hit by the crisis"},
    "crise2": {"c": [CRISE2, None], "fr": "Touché plus tard", "en": "Hit later"},
    "or31": {"c": ["#3E6259", None], "fr": "Sort de l'étalon-or en 1931", "en": "Leaves gold, 1931"},
    "or33": {"c": ["#7FA89F", None], "fr": "Sort de l'étalon-or en 1933", "en": "Leaves gold, 1933"},
    "or36": {"c": ["#C9DCD7", None], "fr": "Sort de l'étalon-or en 1936", "en": "Leaves gold, 1936"},
    "matieres": {"c": [OR, None], "fr": "Pays de matières premières", "en": "Raw-material exporters"},
    "dust": {"c": ["#C9A66B", "#8C6A35"], "fr": "Dust Bowl (cœur, approximatif)", "en": "Dust Bowl (core, approximate)"},
    "empgb": {"c": [UK, None], "fr": "Empire britannique", "en": "British Empire"},
    "empfr": {"c": [DEMO, "#5F86AD"], "fr": "Empire français", "en": "French Empire"},
    "autarcie": {"c": [G33, None], "fr": "Allemagne : autarcie", "en": "Germany: autarky"},
    "weimar": {"c": ["#9DB4CC", None], "fr": "Allemagne (république de Weimar)", "en": "Germany (Weimar Republic)"},
    "milit": {"c": [ROUGE, None], "fr": "Régimes militaristes", "en": "Militarist regimes"},
    "rhen": {"c": [None, "#5E1C19"], "fr": "Rhénanie démilitarisée", "en": "Demilitarised Rhineland"},
    "japon": {"c": [JAP, None], "fr": "Japon", "en": "Japan"},
    "mandch": base.CLES["mandch"],
    "urss": base.CLES["urss"],
    "reich": base.CLES["reich"],
    "ital": base.CLES["ital"],
})

LABELS = dict(base.LABELS)
LABELS.update({
    "newyork": {"p": [-74.0, 40.71], "fr": "New York (Wall Street)", "en": "New York (Wall Street)", "t": "evt", "dx": -7},
    "detroit": {"p": [-83.05, 42.33], "fr": "Detroit (Ford)", "en": "Detroit (Ford)", "t": "ville"},
    "chicago": {"p": [-87.63, 41.88], "fr": "Chicago", "en": "Chicago", "t": "ville", "dx": -7},
    "stlouis": {"p": [-90.20, 38.63], "fr": "Saint-Louis", "en": "St Louis", "t": "evt"},
    "stratford": {"p": [-102.07, 36.34], "fr": "Stratford (Texas)", "en": "Stratford (Texas)", "t": "evt", "dx": -7},
    "nipomo": {"p": [-120.47, 35.04], "fr": "Nipomo (Californie)", "en": "Nipomo (California)", "t": "evt"},
    "tva": {"p": [-86.0, 35.6], "fr": "Vallée du Tennessee (TVA)", "en": "Tennessee Valley (TVA)", "t": "evt"},
    "goldengate": {"p": [-122.48, 37.82], "fr": "Golden Gate", "en": "Golden Gate", "t": "ville"},
    "ottawa": {"p": [-75.70, 45.42], "fr": "Ottawa", "en": "Ottawa", "t": "evt"},
    "vienne": {"p": [16.37, 48.21], "fr": "Vienne (Creditanstalt)", "en": "Vienna (Creditanstalt)", "t": "evt"},
    "addis": {"p": [38.75, 9.03], "fr": "Addis-Abeba", "en": "Addis Ababa", "t": "ville"},
    "munich": {"p": [11.58, 48.14], "fr": "Munich", "en": "Munich", "t": "evt", "dx": -7},
    "prague": {"p": [14.42, 50.09], "fr": "Prague", "en": "Prague", "t": "evt", "dx": -7},
    "vienne38": {"p": [16.37, 48.21], "fr": "Vienne", "en": "Vienna", "t": "evt"},
    "nankin_p": {"p": [118.6, 31.95], "fr": "USS Panay (Yangzi)", "en": "USS Panay (Yangtze)", "t": "evt", "dx": -7},
    "versailles": {"p": [2.13, 48.80], "fr": "Versailles", "en": "Versailles", "t": "evt", "dx": -7},
    "l_bresil": {"p": [-52.0, -10.0], "fr": "Brésil : café", "en": "Brazil: coffee", "t": "evt", "dx": 0, "dy": -12},
    "l_chili": {"p": [-70.0, -24.0], "fr": "Chili : nitrates", "en": "Chile: nitrate", "t": "evt", "dx": 0, "dy": -12},
    "l_can": {"p": [-100.0, 56.0], "fr": "Canada", "en": "Canada"},
    "l_ind": {"p": [79.0, 22.0], "fr": "Inde", "en": "India"},
    "l_aus": {"p": [134.0, -25.0], "fr": "Australie", "en": "Australia"},
    "l_nz": {"p": [172.0, -42.0], "fr": "Nouvelle-Zélande", "en": "New Zealand"},
    "l_ethio": {"p": [36.0, 6.3], "fr": "Éthiopie", "en": "Ethiopia"},
    "l_libye": {"p": [17.0, 27.5], "fr": "Libye (italienne)", "en": "Libya (Italian)"},
    "l_rhen": {"p": [7.2, 50.3], "fr": "Rhénanie", "en": "Rhineland", "t": "evt", "dx": -8},
    "l_sudetes": {"p": [14.0, 50.9], "fr": "Sudètes", "en": "Sudetenland", "t": "evt", "dx": 0, "dy": -12},
    "l_aut": {"p": [14.5, 47.4], "fr": "Autriche", "en": "Austria"},
    "l_tch": {"p": [16.5, 49.4], "fr": "Tchécoslovaquie", "en": "Czechoslovakia"},
    "l_cuba": {"p": [-79.5, 21.8], "fr": "Cuba", "en": "Cuba", "t": "evt", "dx": 0, "dy": 12},
    "l_nica": {"p": [-85.0, 12.9], "fr": "Nicaragua", "en": "Nicaragua", "t": "evt", "dx": 0, "dy": 12},
    "l_plaines": {"p": [-99.0, 41.5], "fr": "Grandes Plaines", "en": "Great Plains", "t": "mer"},
})

ordre = base.ordre

MONDE_1929 = {"w:United States": [USA, None], "ru": [UK, None], "france": [DEMO, None], "germany": ["#9DB4CC", None], "saar": [NEUTRE, None],
              "austria": [CRISE2, None], "italie": [IT, None], "urss": [USSR, None], "w:Empire of Japan": [JAP, None]}


def scenes():
    S = []

    def add(part, d, cam, date, titre, texte, **kw):
        s = {"part": part, "d": d, "cam": cam, "date": date, "titre": titre, "texte": texte}
        s.update(kw)
        S.append(s)

    add("1919", 14, [-30, 38, 1.15], L("1918-1919", "1918–1919"),
        L("L'ordre libéral de 1919", "The liberal order of 1919"),
        L("Les Quatorze Points du président Wilson (1918) portent trois principes : démocratie, droit des peuples à disposer d'eux-mêmes, libre-échange. La conférence de Paris, le traité de Versailles et la SDN, installée à Genève, leur donnent des institutions. Mais le Sénat américain refuse de ratifier le traité : les États-Unis n'entreront jamais à la SDN.",
          "President Wilson's Fourteen Points (1918) carried three principles: democracy, self-determination, free trade. The Paris Peace Conference, the Treaty of Versailles and the League of Nations, seated in Geneva, gave them institutions. But the US Senate refused to ratify the treaty: the United States never joined the League."),
        st={"w:United States": [DEMO, None], "ru": [DEMO, None], "france": [DEMO, None]},
        labels=["l_usa", "washington"], pins=["geneve"], cles=["demo19"])
    add("I.1", 14, [-92, 39, 2.3], L("Années 1920", "The 1920s"),
        L("Les Années folles : une prospérité qui semble éternelle", "The Roaring Twenties: a boom that felt permanent"),
        L("Trois présidents républicains (Harding, Coolidge, Hoover) : impôts bas, trusts, droits de douane. La production de masse (la Ford T à 260 $ en 1925) et le crédit permettent la consommation de masse : voitures, radios, réfrigérateurs entrent dans les foyers.",
          "Three Republican presidents (Harding, Coolidge, Hoover): low taxes, trusts, tariffs. Mass production (the Ford Model T at $260 by 1925) and credit made mass consumption possible: cars, radios and refrigerators entered ordinary homes."),
        st=dict(MONDE_1929), labels=["l_usa", "detroit"], cles=["usa"])
    add("I.2", 15, [-28, 47, 1.5], L("1924", "1924"),
        L("Le plan Dawes : l'Europe suspendue au crédit américain", "The Dawes Plan: Europe hangs on American credit"),
        L("Un circuit en trois flèches : 800 millions de marks prêtés à l'Allemagne par les États-Unis ; des réparations allemandes jusqu'à 2,5 milliards de marks par an vers la France et le Royaume-Uni ; leurs dettes de guerre remboursées aux États-Unis. Tout repose sur le crédit américain.",
          "A circuit in three arrows: 800 million marks lent to Germany by the United States; German reparations of up to 2.5 billion marks a year to France and Britain; their war debts repaid to the United States. Everything rested on American credit."),
        labels=["l_usa", "l_all"], cles=["usa", "weimar"],
        arrows=[F((-74.0, 41.0), (11.0, 52.5), BLEU, -0.12, w=3, id="dw1", dur=2.4), F((10.0, 51.0), (2.5, 47.5), ROUGE, 0.25, w=3, id="dw2"),
                F((-1.5, 51.0), (-73.0, 39.5), "#3E6259", -0.15, w=3, id="dw3", dur=2.4)])
    add("I.1", 15, [-74.0, 40.7, 9], L("1924-1929", "1924–1929"),
        L("La spéculation", "Speculation"),
        L("La Bourse triple en cinq ans ; en 1929, environ 10 % des ménages américains ont des actions. On achète non pour le dividende mais pour revendre plus cher, et à crédit : les courtiers prêtent jusqu'à 90 % du prix. Une baisse de 10 % ruine un tel acheteur.",
          "The stock market tripled in five years; by 1929 about 10% of American households held shares. People bought not for the dividend but to resell higher — and on credit: brokers lent up to 90% of the price. A 10% fall wiped such a buyer out."),
        pins=["newyork"], cles=["usa"])
    add("I.1", 14, [-96, 40, 3.0], L("Dès 1920", "From 1920"),
        L("L'économie réelle ralentit déjà", "The real economy is already slowing"),
        L("Agriculture, charbon, textile, bâtiment : tous sont en difficulté avant le krach. Il y a surproduction : la majorité des Américains sont pauvres et ne peuvent pas acheter, et les Européens, qui se relèvent de la guerre, non plus. Les prix agricoles baissent depuis 1920.",
          "Farming, coal, textiles, construction: all were in trouble before the Crash. There was overproduction: most Americans were poor and could not buy, and Europeans, still recovering from the war, could not either. Farm prices had been falling since 1920."),
        labels=["l_plaines", "chicago"], cles=["usa"])
    add("I.1", 15, [-74.0, 40.7, 12], L("24-29 octobre 1929", "24–29 October 1929"),
        L("Le krach de Wall Street", "The Wall Street Crash"),
        L("Jeudi noir (24 octobre) : la panique commence. Lundi 28 et mardi 29 : la Bourse perd environ 13 % puis 12 % en une séance ; 16 millions d'actions changent de mains le 29. Tout le monde vend, personne n'achète. Le Dow Jones tombe de 381 (septembre 1929) à 41 (juillet 1932).",
          "Black Thursday (24 October): the panic began. Monday 28 and Tuesday 29: the market lost about 13% then 12% in a single session; 16 million shares changed hands on the 29th. Everyone sold, nobody bought. The Dow Jones fell from 381 (September 1929) to 41 (July 1932)."),
        pins=["newyork"], cles=["usa", "crise"], st={"w:United States": [CRISE, None]})
    add("I.2", 14, [-90, 39, 2.4], L("1930-1932", "1930–1932"),
        L("Les faillites bancaires : la Grande Dépression", "Bank failures: the Great Depression"),
        L("La confiance disparaît ; les épargnants retirent leur argent, les banques font faillite (environ 5 000 en 1932, sans garantie des dépôts avant 1933). Entreprises et ménages réduisent leurs dépenses, la production chute, les licenciements s'enchaînent : un krach dure quelques jours, une dépression des années.",
          "Confidence vanished; savers withdrew their money and banks failed (about 5,000 by 1932, with no deposit insurance before 1933). Businesses and households cut spending, output fell, lay-offs followed: a crash lasts days, a depression years."),
        labels=["l_usa", "chicago", "newyork"], cles=["crise"])
    add("I.2", 15, [-25, 47, 1.5], L("1930-1931", "1930–1931"),
        L("Le rappel des prêts américains", "American loans are recalled"),
        L("Les banques américaines rappellent soudain leurs prêts aux banques européennes, qui s'effondrent ; comme elles détenaient aussi des avoirs aux États-Unis, l'effondrement retraverse l'Atlantique. Toutes les économies partageaient déjà les mêmes faiblesses : surproduction, baisse des prix, revenus agricoles en chute.",
          "American banks suddenly recalled their loans to European banks, which collapsed; since they also held assets in American banks, the collapse came back across the Atlantic. All economies already shared the same weaknesses: overproduction, falling prices, falling farm incomes."),
        labels=["l_usa"], cles=["crise"],
        arrows=[F((11.0, 52.0), (-73.0, 41.0), ROUGE, 0.12, w=3, dash=True, id="rap1", dur=2.4), F((16.0, 48.0), (-74.0, 40.0), ROUGE, 0.18, w=3, dash=True, id="rap2", dur=2.4)])
    add("I.2", 15, [12, 50, 4.0], L("Mai - septembre 1931", "May – September 1931"),
        L("L'effet domino en Europe", "The domino effect in Europe"),
        L("La Creditanstalt, première banque d'Autriche, fait faillite en mai 1931 ; les banques allemandes suivent en juillet ; le Royaume-Uni quitte l'étalon-or en septembre. L'Allemagne et l'Autriche, frappées les premières, ne peuvent plus payer les réparations ; les banques britanniques, qui y avaient investi, sont touchées.",
          "The Creditanstalt, Austria's largest bank, failed in May 1931; German banks followed in July; Britain left the gold standard in September. Germany and Austria, hit first, could no longer pay reparations; British banks, which had invested there, were hit in turn."),
        st={"austria": [CRISE, None], "germany": [CRISE, None], "ru": [CRISE, None]},
        pins=["vienne"], labels=["berlin", "londres", "l_fra"], cles=["crise"],
        arrows=[F((16.0, 48.4), (13.2, 52.2), ROUGE, -0.2, w=2.6, id="dom1"), F((12.8, 52.6), (0.3, 51.6), ROUGE, -0.15, w=2.6, id="dom2")])
    add("I.2", 15, [-38, 40, 1.0], L("1931-1936", "1931–1936"),
        L("L'étalon-or, courroie de transmission", "The gold standard, the transmission belt"),
        L("Pour défendre le dollar, la Réserve fédérale relève ses taux : l'or quitte les autres pays, qui doivent relever les leurs, le pire remède en pleine crise. Sortir de l'or est la porte de sortie : Royaume-Uni et Japon en 1931, États-Unis en 1933, France seulement en 1936. Plus on sort tôt, plus tôt on se redresse.",
          "To defend the dollar, the Federal Reserve raised interest rates: gold left other countries, which had to raise theirs — the worst medicine in a slump. Leaving gold was the exit: Britain and Japan in 1931, the United States in 1933, France only in 1936. The earlier a country left, the earlier it recovered."),
        st={"ru": ["#3E6259", None], "w:Empire of Japan": ["#3E6259", None], "w:United States": ["#7FA89F", None], "france": ["#C9DCD7", None],
            "germany": [CRISE, None], "austria": [CRISE, None]},
        labels=["l_usa"], cles=["or31", "or33", "or36"])
    add("I.2", 15, [-62, -14, 1.9], L("1929-1932", "1929–1932"),
        L("La périphérie frappée par la chute des prix", "The periphery hit by falling prices"),
        L("La fin des prêts américains et la chute des importations de matières premières frappent les pays moins développés. Le Brésil brûle quelque 78 millions de sacs de café entre 1931 et 1944 pour soutenir les prix ; les recettes d'exportation du Chili (nitrates) s'effondrent de plus de 80 %. Un pays qui vend un seul produit n'a pas d'amortisseur.",
          "The end of American loans and the fall in raw-material imports struck the less developed countries. Brazil burned some 78 million bags of coffee between 1931 and 1944 to hold up the price; Chile's nitrate export earnings collapsed by more than 80%. A country that sells one commodity has no cushion."),
        st={"w:Brazil": [OR, None], "w:Chile": [OR, None], "w:Argentina": ["#E4CF9E", None]},
        labels=["l_bresil", "l_chili"], cles=["matieres"])
    add("I.2", 14, [100, 5, 1.0], L("Années 1930", "The 1930s"),
        L("Une crise durable dans tout le monde dominé", "A lasting crisis across the dependent world"),
        L("Selon le cours, la crise touche durablement l'Amérique latine, le Canada, l'Inde, la Nouvelle-Zélande et l'Australie. La France, moins endettée envers les États-Unis, n'est touchée qu'en 1932, quand les réparations allemandes cessent d'arriver.",
          "According to the course, the crisis lastingly affected Latin America, Canada, India, New Zealand and Australia. France, less indebted to the United States, was hit only in 1932, as German reparations stopped arriving."),
        st={"w:British Raj": [CRISE, None], "w:Australia": [CRISE, None], "w:New Zealand": [CRISE, None], "w:Canada": [CRISE, None]},
        labels=["l_ind", "l_aus", "l_nz"], cles=["crise", "matieres"])

    # ---------------- I.3 le traumatisme
    add("I.3", 15, [-92, 39, 2.4], L("1929-1933", "1929–1933"),
        L("Des millions de vies brisées, sans filet de sécurité", "Millions of lives broken, with no safety net"),
        L("Production industrielle et agricole : − 40 %. Salaires moyens : − 60 %. 14 millions de chômeurs, 25 % des actifs (3 % en 1929), sans assurance chômage, sans sécurité sociale, sans retraite publique. 5 000 banques en faillite, des exportations en ruine.",
          "Industrial and farm output: −40%. Average wages: −60%. 14 million unemployed, 25% of all workers (3% in 1929), with no unemployment insurance, no social security, no public pension. 5,000 banks bankrupt, exports in ruins."),
        st={"w:United States": [CRISE, None]}, labels=["l_usa"], cles=["crise"])
    add("I.3", 14, [-82, 40.5, 4.6], L("1930-1932", "1930–1932"),
        L("Les Hoovervilles", "The Hoovervilles"),
        L("Les familles expulsées construisent des bidonvilles en planches et en tôle, souvent au cœur des grandes villes, baptisés du nom du président Hoover jugé responsable. Le plus grand est à Saint-Louis ; un autre occupe une partie de Central Park ; à Chicago, Al Capone ouvre une soupe populaire en 1931.",
          "Evicted families built shanty towns of scrap wood and metal, often in the heart of big cities, named after President Hoover, held responsible. The largest was in St Louis; another occupied part of Central Park; in Chicago, Al Capone opened a soup kitchen in 1931."),
        pins=["stlouis", "newyork", "chicago"], cles=["crise"])
    add("I.3", 16, [-104, 37, 4.2], L("14 avril 1935", "14 April 1935"),
        L("Le Dust Bowl : une crise devenue écologique", "The Dust Bowl: an economic crisis turned ecological"),
        L("Sécheresse et labours mécanisés sans méthodes de culture sèche : la terre nue s'envole en tempêtes de poussière (Stratford, Texas, 1935 ; « Black Sunday », 14 avril 1935). Ruinées par les prix et par la poussière, des familles partent vers la Californie.",
          "Drought, and mechanised ploughing without dryland farming methods: the bare soil rose into dust storms (Stratford, Texas, 1935; “Black Sunday”, 14 April 1935). Ruined by prices and by dust, families left for California."),
        st={"dustbowl": ["#C9A66B", "#8C6A35"]}, pins=["stratford"], labels=["l_plaines"], cles=["dust"],
        arrows=[F((-100.0, 35.6), (-119.5, 35.3), "#7D7465", -0.12, w=2.6, dash=True, id="okies", dur=2.6)])
    add("I.3", 15, [-118, 36, 6.5], L("Mars 1936", "March 1936"),
        L("Migrant Mother : la photographie comme argument", "Migrant Mother: photography as an argument"),
        L("Pour une agence fédérale, Dorothea Lange photographie Florence Owens Thompson, 32 ans, et ses enfants dans un camp de cueilleurs de pois à Nipomo, en Californie. L'image, composée (cinq prises), est publiée aussitôt et fait venir l'aide fédérale au camp.",
          "For a federal agency, Dorothea Lange photographed Florence Owens Thompson, 32, and her children in a pea-pickers' camp at Nipomo, California. The composed image (five exposures) was published at once and brought federal relief to the camp."),
        pins=["nipomo"], cles=["dust"], st={"dustbowl": None})
    add("I.3", 14, [70, 50, 1.3], L("Années 1930", "The 1930s"),
        L("Un traumatisme mondial, mais inégal", "A global trauma, but uneven"),
        L("Krach, dépression américaine, puis chute de la production, chômage de masse et déflation dans le monde. Mais les pays peu intégrés aux marchés sont épargnés : l'URSS, hors du commerce capitaliste et en plein premier plan quinquennal, est à peine touchée, et les visiteurs occidentaux en reviennent impressionnés.",
          "Crash, American depression, then falling output, mass unemployment and deflation worldwide. But countries little integrated into world markets were spared: the USSR, outside capitalist trade and in its first Five-Year Plan, was barely touched, and Western visitors came home impressed by planning."),
        st={"urss": [USSR, None]}, labels=["l_urss_m"], cles=["urss", "crise"])

    # ---------------- II.1 nationalisme économique
    add("II.1", 15, [-85, 45, 2.1], L("17 juin 1930", "17 June 1930"),
        L("Le tarif Smoot-Hawley", "The Smoot–Hawley Tariff"),
        L("Avant le krach, l'Amérique de Hoover pratique un « internationalisme indépendant » : du commerce, aucune alliance. Le tarif Smoot-Hawley relève les droits sur plus de 20 000 produits, malgré 1 028 économistes, Henry Ford et 23 pays qui protestent. Le Canada riposte en quelques jours et se tourne vers l'Empire britannique.",
          "Before the Crash, Hoover's America practised “independent internationalism”: trade, but no alliance. The Smoot–Hawley Tariff raised duties on more than 20,000 goods, despite 1,028 economists, Henry Ford and 23 protesting countries. Canada retaliated within days and turned to the British Empire."),
        labels=["l_usa", "l_can", "washington"], cles=["usa"],
        arrows=[F((-79.0, 47.0), (-82.0, 41.5), ROUGE, 0.25, w=3, id="can"), F((-70.0, 48.0), (-10.0, 52.0), UK, -0.12, w=2.6, dash=True, id="can2", dur=2.4)])
    add("II.1", 16, [20, 15, 0.95], L("1931-1932", "1931–1932"),
        L("Les empires deviennent des blocs fermés", "The empires become closed trading blocs"),
        L("Le Royaume-Uni vote l'Import Duties Act (10 %) et, à Ottawa en 1932, la « préférence impériale » ; la France instaure des quotas (1931) ; l'Allemagne vise l'autarcie. Le commerce se replie vers des colonies qui ne peuvent refuser : le commerce mondial perd environ deux tiers de sa valeur entre 1929 et 1934.",
          "Britain passed the Import Duties Act (10%) and, at Ottawa in 1932, “imperial preference”; France set up quotas (1931); Germany aimed at autarky. Trade turned inwards towards colonies that could not refuse: world trade fell by about two thirds in value between 1929 and 1934."),
        st=dict([(k, [UK, None]) for k in EMPIRE_GB] + [(k, [DEMO, "#5F86AD"]) for k in EMPIRE_FR] + [("germany", [G33, None]), ("austria", [NEUTRE, None])]),
        labels=["l_can", "l_ind", "l_aus", "l_afn"], cles=["empgb", "empfr", "autarcie"])
    add("II.1", 15, [-55, 30, 1.25], L("1933-1934", "1933–1934"),
        L("Roosevelt renverse la politique", "Roosevelt reverses the policy"),
        L("Roosevelt sort de l'étalon-or en 1933, puis la loi de 1934 sur les accords tarifaires réciproques (RTAA) lui permet de baisser les droits pays par pays : environ vingt accords en 1939. Il reconnaît l'URSS (novembre 1933) et sa politique de « bon voisinage » retire les troupes de Cuba et du Nicaragua. Hitler et Mussolini, eux, refusent tout accord commercial.",
          "Roosevelt took the US off gold in 1933; the Reciprocal Tariff Agreement Act of 1934 let him cut duties country by country: about twenty agreements by 1939. He recognised the USSR (November 1933), and his “Good Neighbor” policy withdrew troops from Cuba and Nicaragua. Hitler and Mussolini rejected any trade agreement."),
        st=dict([(k, None) for k in EMPIRE_GB + EMPIRE_FR] + [("w:United States", [USA, None]), ("ru", [UK, None]), ("france", [DEMO, None]), ("germany", [G33, None])]),
        labels=["l_usa", "l_cuba", "l_nica", "washington"], cles=["usa"])

    # ---------------- II.2 réponses politiques
    add("II.2", 15, [11, 51, 4.6], L("1928-1932", "1928–1932"),
        L("L'Allemagne, le pays le plus exposé", "Germany, the most exposed country"),
        L("L'industrie allemande dépend du crédit américain : la production chute de 40 %, le chômage des assurés passe de 8,6 % (1928) à 43,8 % (1932). Le vote nazi suit la courbe : 2,6 %, 18,3 %, 37,3 % en juillet 1932, puis 33,1 % en novembre. Les nazis n'ont jamais la majorité.",
          "German industry depended on American credit: output fell by 40%, unemployment among insured workers rose from 8.6% (1928) to 43.8% (1932). The Nazi vote followed the curve: 2.6%, 18.3%, 37.3% in July 1932, then 33.1% in November. The Nazis never won a majority."),
        st={"germany": [CRISE, None]}, labels=["l_all", "berlin"], cles=["crise"])
    add("II.2", 15, [12, 51.5, 5.2], L("Janvier 1933", "January 1933"),
        L("Hitler appelé au pouvoir ; l'économie nazie", "Hitler let in; the Nazi economy"),
        L("Par peur du communisme, les conservateurs nomment Hitler chancelier en janvier 1933. Syndicats interdits, salaires gelés, autoroutes et surtout réarmement malgré Versailles, pillage et spoliation des Juifs : le chômage passe de six millions (1933) à moins d'un million (1937). Une reprise qui n'a de sens que si la guerre suit.",
          "Out of fear of communism, the conservatives appointed Hitler chancellor in January 1933. Unions banned, wages frozen, motorways and above all rearmament despite Versailles, plunder and the dispossession of Jews: unemployment fell from six million (1933) to under one million (1937). A recovery that only made sense if war followed."),
        st={"germany": [G33, None]}, pins=["berlin"], cles=["reich"])
    add("II.2", 15, [-92, 38, 2.4], L("1933-1935", "1933–1935"),
        L("Le New Deal : Relief, Recovery, Reform", "The New Deal: Relief, Recovery, Reform"),
        L("Roosevelt, élu en 1932, lance le New Deal : les « cent jours » créent le Civilian Conservation Corps, la Tennessee Valley Authority et la garantie des dépôts ; en 1935, le Social Security Act (retraites, assurance chômage). Le Golden Gate est construit dès 1933. Comme l'Allemagne, l'État dépense, mais pour des ponts et des droits, pas pour une armée.",
          "Roosevelt, elected in 1932, launched the New Deal: the “hundred days” created the Civilian Conservation Corps, the Tennessee Valley Authority and deposit insurance; in 1935 came the Social Security Act (pensions, unemployment insurance). The Golden Gate Bridge went up from 1933. Like Germany, the state spent — but on bridges and rights, not an army."),
        st={"w:United States": [USA, None]}, pins=["tva"], labels=["goldengate", "washington"], cles=["usa"])
    add("II.2", 15, [2.4, 47.5, 6.5], L("1934-1936", "1934–1936"),
        L("La France : le Front populaire", "France: the Front populaire"),
        L("Le 6 février 1934, les ligues d'extrême droite manifestent à Paris : le cours parle d'un coup d'État manqué. Contre le fascisme, socialistes, communistes et radicaux forment le Front populaire, vainqueur en 1936 avec Léon Blum : 40 heures, deux semaines de congés payés, SNCF, hausse des salaires (accords de Matignon). Mais pas d'argent pour l'armée, et l'apaisement à l'extérieur.",
          "On 6 February 1934 far-right leagues rioted in Paris, a failed coup in the course's words. Against fascism, Socialists, Communists and Radicals formed the Front populaire, which won in 1936 under Léon Blum: the 40-hour week, two weeks' paid holiday, the SNCF, wage rises (Matignon Agreements). But no money for the army, and appeasement abroad."),
        pins=["paris"], labels=["l_fra"], cles=["demo19"])
    add("II.2", 15, [60, 40, 1.0], L("Années 1930", "The 1930s"),
        L("Le militarisme gagne trois régimes", "Militarism spreads to three regimes"),
        L("Hitler, Mussolini et le gouvernement japonais choisissent le militarisme : une armée puissante, le contrôle du gouvernement par les militaires, une politique étrangère agressive. Au Japon, en septembre 1931, l'armée du Guandong agit d'abord en Mandchourie ; le gouvernement de Tokyo explique ensuite. Facteurs économiques ou idéologie ?",
          "Hitler, Mussolini and the Japanese government implemented militarism: a strong army, control of the government by the military, an aggressive foreign policy. In Japan, in September 1931, the Kwantung Army acted first in Manchuria; the government in Tokyo explained afterwards. Economic factors or ideology?"),
        st={"germany": [ROUGE, None], "italie": [ROUGE, None], "w:Empire of Japan": [ROUGE, None]}, labels=["l_all", "l_ita", "l_jap"], cles=["milit"])

    # ---------------- II.3 des démocraties réticentes
    add("II.3", 15, [124, 40, 2.6], L("18 septembre 1931", "18 September 1931"),
        L("La Mandchourie : la SDN impuissante", "Manchuria: the League powerless"),
        L("À Moukden, des soldats japonais organisent un faux attentat contre leur propre voie ferrée pour envahir la Mandchourie, qui devient le Mandchoukouo. La commission Lytton condamne ; le Japon quitte la SDN (mars 1933). Le pacte Briand-Kellogg (1928) avait mis la guerre hors la loi, sans moyen de l'imposer.",
          "At Mukden, Japanese soldiers staged a false-flag attack on their own railway to invade Manchuria, which became Manchukuo. The Lytton Commission condemned it; Japan left the League (March 1933). The Kellogg–Briand Pact (1928) had outlawed war, with no means to enforce it."),
        st={"w:Empire of Japan": [JAP, None], "w:Manchuria": ["#E9D9C4", JAP], "germany": [G33, None], "italie": [IT, None]}, pins=["moukden"], labels=["l_mand", "l_jap", "l_chine"], cles=["japon", "mandch"],
        arrows=[F((129.5, 36.5), (123.6, 41.6), JAP, 0.2, id="jap31")])
    add("II.3", 15, [119, 33, 3.4], L("7 janvier 1932", "7 January 1932"),
        L("La doctrine Stimson, puis Shanghai bombardée", "The Stimson doctrine, then Shanghai bombed"),
        L("Le secrétaire d'État Stimson annonce que les États-Unis ne reconnaîtront aucune conquête par la force en Chine : une doctrine de non-reconnaissance, pas d'action. Le Japon répond en bombardant Shanghai en 1932, avec de lourdes pertes civiles. Aucune riposte américaine.",
          "Secretary of State Stimson announced that the United States would recognise no conquest by force in China: a doctrine of non-recognition, not action. Japan answered by bombing Shanghai in 1932, with heavy civilian casualties. No American response followed."),
        pins=["shanghai"], labels=["l_chine", "nankin"], cles=["japon"],
        arrows=[F((126.5, 30.0), (121.8, 31.2), JAP, 0.2, id="sh32")])
    add("II.3", 15, [118.5, 32, 7.0], L("1935-1937", "1935–1937"),
        L("Les lois de neutralité ; l'USS Panay", "The Neutrality Acts; the USS Panay"),
        L("Le Congrès vote les lois de neutralité : embargo sur les armes (1935), voyages interdits sur les navires des pays en guerre (1936), embargo sur tout commerce avec eux (1937). En décembre 1937, le Japon coule la canonnière USS Panay sur le Yangzi, puis s'excuse et paie : il y lit un permis d'aller plus loin.",
          "Congress passed the Neutrality Acts: an arms embargo (1935), no travel on ships of nations at war (1936), an embargo on all trade with them (1937). In December 1937 Japan sank the gunboat USS Panay on the Yangtze, then apologised and paid — and read the American tone as a licence to go further."),
        pins=["nankin_p"], cles=["japon", "usa"])
    add("II.3", 15, [30, 18, 2.2], L("Octobre 1935", "October 1935"),
        L("L'Italie envahit l'Éthiopie", "Italy invades Ethiopia"),
        L("Mussolini attaque l'Éthiopie. Le Royaume-Uni refuse l'embargo sur le pétrole qui l'aurait arrêté : c'est l'apaisement. Ses raisons : pacifisme, un empire à surveiller, la crise d'abord, l'isolationnisme américain, la peur du communisme plus que du fascisme.",
          "Mussolini attacked Ethiopia. Britain refused the oil embargo that would have stopped him: appeasement. Its reasons: pacifism, an empire to police, its own economic problems first, American isolationism, and a greater fear of communism than of fascism."),
        st={"w:Ethiopia": [IT, "#5A4630"], "w:Libya (IT)": [IT, None], "w:Eritrea": [IT, None], "w:Italian Somaliland": [IT, None]},
        labels=["l_ethio", "l_libye", "rome"], pins=["addis"], cles=["ital"],
        arrows=[F((39.0, 15.5), (38.9, 9.6), IT, 0.15, w=3, id="eth1"), F((45.0, 4.0), (40.0, 8.0), IT, -0.15, w=3, id="eth2")])
    add("II.3", 15, [7.5, 50.3, 6.2], L("7 mars 1936", "7 March 1936"),
        L("La Rhénanie remilitarisée", "The Rhineland remilitarised"),
        L("Hitler envoie ses troupes en Rhénanie, démilitarisée par Versailles, avec l'ordre de se retirer à la première résistance française. Il n'y en a aucune : la France et le Royaume-Uni décident de ne pas intervenir.",
          "Hitler sent troops into the Rhineland, demilitarised by Versailles, with orders to withdraw at the first sign of French resistance. There was none: France and Britain decided not to intervene."),
        st={"germany": [G33, None], "saar": [G33, None], "rhenanie": [None, "#F7F3EA"]}, labels=["l_rhen", "l_fra", "paris"], cles=["reich", "rhen"],
        arrows=[F((10.0, 51.5), (7.4, 50.9), ROUGE, 0.2, w=3, id="rh1"), F((9.8, 49.7), (7.6, 49.6), ROUGE, -0.2, w=3, id="rh2")])
    add("II.3", 16, [14.5, 49.0, 5.0], L("Mars - septembre 1938", "March – September 1938"),
        L("L'Anschluss et Munich", "The Anschluss and Munich"),
        L("L'Allemagne annexe l'Autriche en mars 1938. Puis Hitler exige une partie de la Tchécoslovaquie : à Munich, en septembre, Chamberlain et Daladier acceptent la « cession à l'Allemagne du territoire allemand des Sudètes ». L'axe Rome-Berlin-Tokyo lie les trois puissances militaristes.",
          "Germany annexed Austria in March 1938. Then Hitler demanded part of Czechoslovakia: at Munich in September, Chamberlain and Daladier accepted the “cession to Germany of the Sudeten German territory”. The Rome–Berlin–Tokyo pact tied the three militarist powers together."),
        st={"austria": [G33, None], "sudetes": [G33, None], "rhenanie": [None, None]}, labels=["l_aut", "l_sudetes"], pins=["munich", "vienne38"], cles=["reich"],
        arrows=[F((12.6, 48.3), (16.0, 48.2), ROUGE, -0.15, w=3, id="ans"), F((12.0, 50.0), (13.8, 50.6), ROUGE, 0.2, w=2.6, id="sud1"), F((15.6, 51.0), (16.2, 50.2), ROUGE, -0.2, w=2.6, id="sud2")])
    add("II.3", 15, [17, 51, 4.0], L("Mars - septembre 1939", "March – September 1939"),
        L("Prague, puis la Pologne : la guerre", "Prague, then Poland: war"),
        L("En mars 1939, l'Allemagne occupe toute la Tchécoslovaquie : Munich n'a rien acheté. Le 1er septembre 1939, elle envahit la Pologne ; la France et le Royaume-Uni déclarent la guerre. À chaque concession, la tension européenne s'était aggravée.",
          "In March 1939 Germany occupied the whole of Czechoslovakia: Munich had bought nothing. On 1 September 1939 it invaded Poland; France and Britain declared war. Every concession had made European turmoil worse."),
        st={"boheme": [G33, None], "slovaquie": [base.ALLIE, None], "pologne_all": [G38, None], "danzig": [G33, None]},
        labels=["varsovie"], pins=["prague"], cles=["reich", "occ"],
        arrows=[F((14.4, 52.4), (20.4, 52.2), ROUGE, -0.12, id="pl1"), F((20.6, 54.1), (21.1, 52.5), ROUGE, 0.1, id="pl2"), F((19.6, 49.3), (21.7, 50.8), ROUGE, 0.12, id="pl4")])
    add("II.3", 16, [-40, 40, 1.25], L("Novembre 1939", "November 1939"),
        L("Le « cash and carry » : l'arsenal de la démocratie", "Cash and carry: the Arsenal of Democracy"),
        L("La guerre commencée, Roosevelt obtient la loi de neutralité de 1939 : les démocraties peuvent acheter des armes si elles paient comptant et les transportent elles-mêmes. Les usines américaines, à l'arrêt depuis 1929, repartent : les chars Sherman sortent de l'arsenal de Detroit. La Dépression finit non par le New Deal mais par le réarmement.",
          "Once war had begun, Roosevelt obtained the Neutrality Act of 1939: the democracies could buy weapons if they paid cash and carried them on their own ships. American factories, idle since 1929, restarted: Sherman tanks rolled out of the Detroit Tank Arsenal. The Depression ended not with the New Deal but with rearmament."),
        labels=["l_usa", "l_ru", "l_atl", "detroit"], cles=["usa", "uk", "reich"],
        arrows=[F((-73.5, 40.5), (-5.5, 51.0), BLEU, -0.12, w=2.8, dash=True, id="cc1", dur=2.8), F((-66.0, 44.5), (-1.5, 47.5), BLEU, -0.08, w=2.8, dash=True, id="cc2", dur=2.8)])
    return S
