GRAPHES["e1-pib"] = {
  type: "barres", t: "Taux de croissance du PIB de la France en volume, 1950-2025",
  s: "En % par rapport à l’année précédente. Touche une barre pour lire la valeur.",
  src: "Source : Insee, comptes nationaux annuels, base 2020 (mai 2026). Données 2024 semi-définitives, 2025 provisoires.",
  unite: " %", x: [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
  y: [8.6,5.7,3.1,3.4,5.7,5.4,5.0,5.6,2.8,2.8,8.0,4.9,6.9,6.1,6.6,4.8,5.2,4.8,4.5,7.1,6.2,5.3,4.5,6.2,4.4,-0.9,4.3,3.6,3.9,3.7,1.7,1.2,2.4,1.3,1.6,1.6,2.4,2.6,4.8,4.4,2.8,1.2,1.5,-0.4,2.4,2.3,1.4,2.5,3.5,3.4,4.1,1.9,1.1,1.0,2.9,1.9,2.7,2.5,0.4,-2.8,2.0,2.4,0.2,0.8,1.0,1.1,0.9,2.1,1.6,2.0,-7.4,6.9,2.7,1.6,1.5,0.8],
  bandes: [{ de: 1950, a: 1973, l: "1950-1973 : 5,2 %/an" }],
  notes: [{ x: 1975, y: -0.9, t: "1975" }, { x: 2009, y: -2.8, t: "2009" }, { x: 2020, y: -7.4, t: "2020 Covid" }],
  pasX: 10, h: 300, min: -8, max: 10
};
GRAPHES["e1-periodes"] = {
  type: "hbarres", t: "Croissance annuelle moyenne du PIB en volume, par période",
  s: "En % par an, calculé à partir des niveaux du PIB en volume (euros 2020).",
  src: "Source : Insee, comptes nationaux annuels, base 2020 ; calculs du site (taux annuel moyen).",
  unite: " %", cats: ["1950-1973", "1973-2007", "2007-2019", "2019-2025"], series: [{ n: "Croissance moyenne", v: [5.2, 2.4, 1.0, 0.9], c: 1 }], lab: 110
};
GRAPHES["e1-decouplage"] = {
  type: "hbarres", t: "France, 1990-2025 : la production augmente, les émissions baissent",
  s: "Variation entre 1990 et 2025, en %.",
  src: "Sources : Insee, PIB en volume, base 2020 (1 566,2 puis 2 646,7 milliards d’euros 2020) ; Citepa, rapport Secten 2026, émissions territoriales de gaz à effet de serre hors puits de carbone (−34,3 %, 359,4 Mt CO₂e en 2025, estimation provisoire).",
  unite: " %", cats: ["PIB en volume", "Émissions de gaz à effet de serre"], series: [{ n: "Variation 1990-2025", v: [69.0, -34.3], c: 1 }], lab: 150
};

CHAINES["e1-pgf"] = { t: "Des gains de productivité à la croissance", e: [
  { t: "Progrès technique : la productivité globale des facteurs augmente", k: "cause" },
  { t: "On produit davantage avec les mêmes quantités de travail et de capital", a: "donc" },
  { t: "Le coût unitaire de production baisse", a: "donc" },
  { f: [{ t: "Les prix peuvent baisser : le pouvoir d’achat augmente" }, { t: "Les salaires et les profits peuvent augmenter" }], a: "partage des gains" },
  { t: "La demande augmente : consommation et investissement", a: "donc" },
  { t: "Les entreprises produisent plus : croissance du PIB", k: "effet" }
] };
CHAINES["e1-endo"] = { t: "Le cercle vertueux de la croissance endogène", n: "La dernière étape relance la première : c’est pour cela que le progrès technique est dit « endogène », produit par la croissance elle-même.", e: [
  { t: "Croissance économique", k: "cause" },
  { t: "Les profits des entreprises et les recettes publiques augmentent", a: "donc" },
  { f: [{ t: "Les entreprises investissent en R&D" }, { t: "L’État finance éducation, recherche publique, infrastructures" }], a: "ce qui permet" },
  { t: "Innovations et capital humain supplémentaires", a: "donc" },
  { t: "Les connaissances, non rivales, se diffusent : externalités positives", a: "or" },
  { t: "La productivité globale des facteurs augmente : nouvelle croissance", k: "effet", a: "donc" }
] };
CHAINES["e1-inst"] = { t: "Des droits de propriété à la croissance", e: [
  { t: "Institutions : droits de propriété garantis (brevets, État de droit, justice indépendante)", k: "cause" },
  { t: "L’innovateur peut s’approprier les gains de son innovation (rente de monopole temporaire)", a: "donc" },
  { t: "Il est incité à investir et à prendre le risque d’innover", a: "donc" },
  { t: "Davantage d’innovations de produit et de procédé", a: "donc" },
  { t: "Gains de productivité et nouveaux marchés : croissance", k: "effet", a: "donc" }
] };
CHAINES["e1-dc"] = { t: "La destruction créatrice", e: [
  { t: "Une innovation majeure apparaît (ex. : l’appareil photo numérique, puis le smartphone)", k: "cause" },
  { f: [{ t: "Création : nouvelles entreprises, nouveaux produits, nouveaux emplois", k: "effet" }, { t: "Destruction : produits, entreprises et emplois anciens deviennent obsolètes", k: "frein" }], a: "en même temps" },
  { t: "Le travail et le capital se réallouent vers les activités les plus productives", a: "donc" },
  { t: "La productivité globale augmente : croissance à long terme, mais coûts pour les perdants (chômage, reconversion)", k: "effet", a: "donc" }
] };
CHAINES["e1-biais"] = { t: "Progrès technique biaisé et inégalités de revenus", e: [
  { t: "Progrès technique biaisé : numérique, automatisation, intelligence artificielle", k: "cause" },
  { f: [{ t: "Demande de travail qualifié en hausse (complémentaire des machines)" }, { t: "Demande de travail peu qualifié et routinier en baisse (remplaçable)" }], a: "donc" },
  { t: "Si l’offre de diplômés progresse moins vite que cette demande…", k: "frein", a: "or" },
  { t: "…l’écart de salaire entre qualifiés et peu qualifiés se creuse", a: "donc" },
  { t: "Les inégalités de revenus augmentent", k: "effet", a: "donc" }
] };
CHAINES["e1-limites"] = { t: "Croissance et limites écologiques", e: [
  { t: "Croissance de la production et de la consommation", k: "cause" },
  { f: [{ t: "Plus de prélèvements : énergies fossiles, minerais, eau, poissons" }, { t: "Plus de rejets : déchets, polluants, gaz à effet de serre" }], a: "donc" },
  { t: "Épuisement des ressources, pollution, réchauffement climatique", a: "donc" },
  { t: "Le capital naturel se dégrade", a: "donc" },
  { t: "La croissance future est menacée : catastrophes, pénuries, coûts de réparation", k: "effet", a: "donc" }
] };
CHAINES["e1-rebond"] = { t: "L’effet rebond", e: [
  { t: "Innovation qui améliore l’efficacité énergétique (moteur plus sobre, éclairage LED)", k: "cause" },
  { t: "Moins d’énergie consommée par unité produite ou utilisée", a: "donc" },
  { t: "Le coût d’usage baisse", a: "donc" },
  { t: "On utilise davantage le bien (plus de kilomètres, plus d’équipements)", a: "donc" },
  { t: "Les économies d’énergie sont en partie, voire totalement, annulées", k: "frein", a: "donc" }
] };

CH.e1 = {
  chapo: "Pourquoi la production française a-t-elle été multipliée par 8,6 depuis 1950 ? Grâce au travail et au capital, mais surtout au progrès technique. Ce chapitre explique d’où il vient, ce qu’il détruit, qui il enrichit et s’il peut rendre la croissance compatible avec la planète.",
  essentiel: [
    "La croissance est l’augmentation durable de la production, mesurée par le taux de variation du PIB en volume. Elle vient de l’accumulation des facteurs (travail, capital) et surtout de la hausse de la <b>productivité globale des facteurs</b> (PGF), qui reflète le progrès technique.",
    "Le progrès technique est <b>endogène</b> : il résulte de l’innovation, produite par des investissements (R&D, capital humain, infrastructures) que la croissance elle-même finance (Romer, Lucas, Barro).",
    "Les <b>institutions</b>, notamment les droits de propriété, incitent à investir et à innover (North). L’innovation s’accompagne d’une <b>destruction créatrice</b> (Schumpeter ; Aghion et Howitt, Nobel 2025).",
    "Le progrès technique peut <b>accroître les inégalités de revenus</b> : il est biaisé en faveur du travail qualifié, polarise les emplois et procure des rentes aux innovateurs.",
    "La croissance se heurte à des <b>limites écologiques</b> (ressources, pollution, climat). L’innovation peut les reculer (découplage), mais l’effet rebond et le débat soutenabilité faible / forte en montrent les limites."
  ],
  chiffres: [
    { n: "5,2 %", l: "de croissance annuelle moyenne du PIB entre 1950 et 1973, contre 1,0 % entre 2007 et 2019.", s: "Insee, base 2020 ; calcul du site" },
    { n: "2,18 %", l: "du PIB consacrés à la recherche et développement en France en 2023 (61,5 milliards d’euros).", s: "Ministère de l’Enseignement supérieur et de la Recherche, SIES, note n° 2025-12" },
    { n: "−34,3 %", l: "d’émissions de gaz à effet de serre en France entre 1990 et 2025, pendant que le PIB en volume progressait d’environ 69 %.", s: "Citepa, Secten 2026 ; Insee" }
  ],
  objectifs: [
    { bo: "Comprendre le processus de croissance économique et les sources de la croissance : accumulation des facteurs et accroissement de la productivité globale des facteurs ; comprendre le lien entre le progrès technique et l’accroissement de la productivité globale des facteurs.", clair: "Savoir expliquer d’où vient la croissance : plus de travail et de capital, et surtout une meilleure efficacité de leur combinaison grâce au progrès technique.", voir: "e1-2" },
    { bo: "Comprendre que le progrès technique est endogène et qu’il résulte en particulier de l’innovation.", clair: "Montrer que le progrès technique ne tombe pas du ciel : il est produit par l’investissement en R&D, en capital humain et en infrastructures.", voir: "e1-3" },
    { bo: "Comprendre comment les institutions (notamment les droits de propriété) influent sur la croissance en affectant l’incitation à investir et innover ; savoir que l’innovation s’accompagne d’un processus de destruction créatrice.", clair: "Expliquer pourquoi des règles du jeu sûres (droits de propriété, brevets, État de droit) favorisent l’innovation, et que celle-ci détruit des activités en même temps qu’elle en crée.", voir: "e1-4" },
    { bo: "Comprendre comment le progrès technique peut engendrer des inégalités de revenus.", clair: "Expliquer pourquoi le progrès technique favorise les plus qualifiés et ceux qui innovent.", voir: "e1-5" },
    { bo: "Comprendre qu’une croissance économique soutenable se heurte à des limites écologiques (notamment l’épuisement des ressources, la pollution et le réchauffement climatique) et que l’innovation peut aider à reculer ces limites.", clair: "Expliquer pourquoi la croissance abîme le capital naturel, et comment (et jusqu’où) l’innovation peut l’éviter.", voir: "e1-6" }
  ],
  notions: ["croissance économique", "PIB", "valeur et volume", "facteurs de production", "productivité du travail", "productivité globale des facteurs (PGF)", "progrès technique", "innovation", "croissance endogène", "recherche et développement", "capital humain", "externalités positives", "institutions", "droits de propriété", "brevet", "destruction créatrice", "inégalités de revenus", "progrès technique biaisé", "polarisation des emplois", "croissance soutenable", "capital naturel", "soutenabilité faible / forte", "découplage", "effet rebond"],
  sections: [
    { id: "e1-1", t: "Mesurer la croissance", h:
      '<p class="lede">La croissance économique est l’<b>augmentation durable de la production</b> de biens et de services d’un pays. On la mesure par le taux de variation du <b>produit intérieur brut (PIB) en volume</b>.</p>' +
      '<div class="def"><b>PIB</b> — somme des valeurs ajoutées produites sur le territoire pendant un an (plus les impôts sur les produits, moins les subventions). <b>En volume</b>, il est corrigé de la hausse des prix : on mesure les quantités produites, pas l’inflation.</div>' +
      '<p>Rappel de Première : un PIB qui augmente <b>en valeur</b> peut stagner en volume si seuls les prix montent. C’est donc toujours le PIB en volume qui mesure la croissance.</p>' +
      '<div data-graph="e1-pib"></div>' +
      '<p>Le graphique montre trois âges de la croissance française. Pendant les « Trente Glorieuses », la croissance est forte et régulière (5,2 % par an en moyenne de 1950 à 1973). Après les chocs pétroliers (1975 : −0,9 %), elle ralentit nettement. Depuis 2008, elle dépasse rarement 2 %, avec deux récessions : 2009 (−2,8 %, crise financière) et 2020 (−7,4 %, Covid), suivie d’un rattrapage en 2021 (+6,9 %).</p>' +
      '<div data-graph="e1-periodes"></div>' +
      '<div class="ex"><p>Le PIB en volume passe de 309,1 milliards d’euros 2020 en 1950 à 2 646,7 milliards en 2025 : il est multiplié par 8,6 (Insee). En 2025, il augmente de 0,8 %, après +1,5 % en 2024.</p></div>' +
      '<p>Croissance n’est pas <b>développement</b> : le développement est l’amélioration durable du bien-être (santé, éducation, niveau de vie). La croissance en fournit les moyens, sans le garantir. On distingue aussi la croissance <b>effective</b> (observée) de la croissance <b>potentielle</b> (celle que permettraient tous les facteurs pleinement employés), qui dépend des sources étudiées ci-dessous.</p>' },

    { id: "e1-2", t: "Les sources : des facteurs plus nombreux et mieux combinés", h:
      '<p class="lede">Pour produire plus, il n’y a que deux moyens : utiliser <b>plus de facteurs de production</b>, ou les utiliser <b>plus efficacement</b>.</p>' +
      '<div class="def"><b>Croissance extensive</b> — croissance due à l’augmentation des quantités de facteurs : plus de travailleurs ou d’heures travaillées, plus de capital (machines, bâtiments, logiciels).</div>' +
      '<div class="def"><b>Croissance intensive</b> — croissance due à la hausse de la productivité : on obtient plus de production avec les mêmes quantités de facteurs.</div>' +
      '<p>Il faut distinguer deux mesures de la productivité :</p>' +
      '<ul><li>la <b>productivité (apparente) du travail</b> = production ÷ quantité de travail (par emploi ou par heure). Elle augmente aussi quand chaque travailleur dispose de plus de capital ;</li><li>la <b>productivité globale des facteurs (PGF)</b> mesure l’efficacité de la <b>combinaison</b> du travail et du capital. C’est la part de la croissance que l’augmentation des quantités de facteurs n’explique pas.</li></ul>' +
      '<div class="aut"><span class="mono">RS</span><span class="an">Robert Solow<small>1924-2023 · Nobel 1987</small></span><span class="ad">Dans son modèle (1956), l’accumulation du capital seule s’essouffle : chaque machine supplémentaire rapporte moins que la précédente (rendements décroissants). Seul le progrès technique permet une croissance durable. En 1957, il mesure qu’aux États-Unis, de 1909 à 1949, environ 87,5 % de la hausse de la production par heure de travail vient du progrès technique et non du capital. Ce « <b>résidu</b> » est la PGF.</span></div>' +
      '<p>Le lien avec le <b>progrès technique</b> est direct : le progrès technique désigne l’ensemble des innovations qui améliorent les produits, les procédés et l’organisation. Il fait augmenter la PGF, donc permet de produire plus avec autant de facteurs. Les gains de productivité se transforment ensuite en croissance par la demande :</p>' +
      '<div data-chain="e1-pgf"></div>' +
      '<details class="pli"><summary>Activité : décomposer une croissance (exemple chiffré inventé)</summary><div><p>Une économie imaginaire croît de 2,0 % par an. Les économistes estiment que la hausse du travail contribue pour 0,4 point et celle du capital pour 0,6 point. La contribution de la PGF est le reste : 2,0 − 0,4 − 0,6 = <b>1,0 point</b>, soit la moitié de la croissance. C’est exactement la démarche de Solow : la PGF se mesure « en creux », comme un résidu. Ce résidu mesure aussi, en partie, notre ignorance : qualité du travail, organisation, institutions s’y mélangent.</p></div></details>' },

    { id: "e1-3", t: "Le progrès technique est endogène", h:
      '<p class="lede">Chez Solow, le progrès technique est <b>exogène</b> : il vient de l’extérieur du modèle, comme une « manne tombée du ciel ». Les théories de la <b>croissance endogène</b>, à partir des années 1980, expliquent au contraire qu’il est <b>produit par des décisions économiques</b>.</p>' +
      '<div class="def"><b>Innovation</b> — application économique d’une invention : nouveau produit, nouveau procédé de production, nouvelle organisation, nouveau débouché. L’<b>invention</b> est la découverte ; l’innovation est sa mise sur le marché.</div>' +
      '<p>Trois sources d’innovation sont mises en avant par les économistes :</p>' +
      '<div class="aut"><span class="mono">PR</span><span class="an">Paul Romer<small>né en 1955 · Nobel 2018</small></span><span class="ad">L’investissement en <b>recherche et développement</b> produit des connaissances. Or une connaissance est <b>non rivale</b> : l’utiliser n’empêche pas les autres de l’utiliser. Elle se diffuse et profite à d’autres entreprises : ce sont des <b>externalités positives</b>, qui rendent les rendements croissants.</span></div>' +
      '<div class="aut"><span class="mono">RL</span><span class="an">Robert Lucas<small>1937-2023 · Nobel 1995</small></span><span class="ad">Le <b>capital humain</b> (connaissances et compétences acquises par la formation et l’expérience) rend chacun plus productif, et rend aussi plus productifs ceux qui travaillent avec lui.</span></div>' +
      '<div class="aut"><span class="mono">RB</span><span class="an">Robert Barro<small>né en 1944</small></span><span class="ad">Les <b>dépenses publiques productives</b> (infrastructures de transport et de communication, recherche publique, éducation) augmentent la productivité des entreprises privées.</span></div>' +
      '<div data-chain="e1-endo"></div>' +
      '<div class="ex"><p>Les vaccins à ARN messager contre le Covid-19, mis sur le marché fin 2020 par BioNTech-Pfizer et Moderna, reposent sur des décennies de recherche, en grande partie publique et universitaire. Les travaux de Katalin Karikó et Drew Weissman sur la modification de l’ARN (article de 2005) leur ont valu le prix Nobel de médecine 2023. Recherche publique, R&D privée et capital humain se sont combinés : c’est la croissance endogène en action.</p></div>' +
      '<p>En France, l’effort de recherche atteint <b>2,18 % du PIB en 2023</b> (61,5 milliards d’euros de dépense intérieure de R&D, dont environ deux tiers exécutés par les entreprises), selon le ministère de l’Enseignement supérieur et de la Recherche.</p>' +
      '<p>Conséquence importante : si la croissance dépend de l’investissement en connaissances, l’<b>État a un rôle</b> à jouer, parce que le marché seul sous-investit dans les activités dont les bénéfices profitent aussi aux autres (externalités) : financement de la recherche fondamentale, de l’éducation, crédit d’impôt recherche.</p>' },

    { id: "e1-4", t: "Les institutions et la destruction créatrice", h:
      '<div class="def"><b>Institutions</b> — ensemble des règles qui encadrent les comportements dans une société : règles formelles (Constitution, lois, droits de propriété, contrats) et informelles (normes, coutumes). Douglass North (Nobel 1993) les appelle les « <b>règles du jeu</b> ».</div>' +
      '<p>Pourquoi investir ou innover si le fruit de l’effort peut être confisqué, copié sans contrepartie ou détruit par l’arbitraire ? Les <b>droits de propriété</b> (droit d’utiliser un bien, d’en tirer un revenu et de le céder) garantis par un <b>État de droit</b> sécurisent les gains futurs. Le <b>brevet</b> donne à l’innovateur un monopole d’exploitation temporaire (au plus vingt ans) en échange de la publication de son invention.</p>' +
      '<div data-chain="e1-inst"></div>' +
      '<div class="aut"><span class="mono">AR</span><span class="an">Daron Acemoglu et James Robinson<small>Nobel 2024 avec Simon Johnson</small></span><span class="ad">Des institutions <b>inclusives</b> (droits de propriété pour tous, concurrence, pouvoir politique partagé) favorisent la croissance ; des institutions <b>extractives</b>, qui permettent à une élite de capter les richesses, la bloquent.</span></div>' +
      '<div class="ex"><p>La Corée, divisée depuis la fin des années 1940, en est l’illustration la plus citée : même peuple, même culture et même géographie au départ, mais des institutions opposées. La Corée du Sud, économie de marché devenue démocratique, est aujourd’hui un pays riche et innovant ; la Corée du Nord, économie planifiée sous dictature, reste l’un des pays les plus pauvres du monde.</p></div>' +
      '<p>Mais la protection a un revers : un brevet trop long ou trop large freine la diffusion des connaissances. Les institutions doivent donc arbitrer entre <b>inciter</b> l’innovateur et <b>diffuser</b> l’innovation.</p>' +
      '<h3>La destruction créatrice</h3>' +
      '<div class="aut"><span class="mono">JS</span><span class="an">Joseph Schumpeter<small>1883-1950</small></span><span class="ad">L’<b>entrepreneur innovateur</b> est le moteur du capitalisme. Les innovations majeures arrivent <b>en grappes</b> et provoquent une « <b>destruction créatrice</b> » : les activités nouvelles remplacent les anciennes (<i>Capitalisme, socialisme et démocratie</i>, 1942).</span></div>' +
      '<div data-chain="e1-dc"></div>' +
      '<div class="ex"><p>Kodak, leader mondial de la pellicule photo, avait pourtant fabriqué dès 1975 le premier prototype d’appareil photo numérique. L’entreprise a tardé à basculer vers le numérique et s’est déclarée en faillite aux États-Unis en janvier 2012, pendant que le numérique, puis le smartphone, créaient de nouvelles entreprises et de nouveaux métiers.</p></div>' +
      '<div class="aut"><span class="mono">AH</span><span class="an">Philippe Aghion et Peter Howitt<small>Nobel 2025 avec Joel Mokyr</small></span><span class="ad">Leur modèle de 1992 fait de la destruction créatrice le cœur de la croissance : chaque innovation rend la précédente obsolète et procure à son auteur une rente temporaire. Le prix Nobel 2025 récompense cette « théorie de la croissance durable par la destruction créatrice ».</span></div>' +
      '<p>La destruction créatrice a un <b>coût social</b> : faillites, licenciements, reconversions difficiles, territoires en déclin. D’où l’idée de politiques qui l’accompagnent (formation, indemnisation du chômage, aide à la mobilité) sans la bloquer. Alfred Sauvy décrivait un <b>déversement</b> des emplois : les gains de productivité suppriment des postes dans un secteur, mais la hausse des revenus crée de nouveaux besoins, donc des emplois ailleurs.</p>' },

    { id: "e1-5", t: "Progrès technique et inégalités de revenus", h:
      '<p class="lede">Le progrès technique enrichit le pays dans son ensemble, mais pas tout le monde de la même façon. Trois mécanismes l’expliquent.</p>' +
      '<h3>1. Un progrès technique biaisé en faveur du travail qualifié</h3>' +
      '<p>Les technologies numériques sont <b>complémentaires</b> du travail qualifié (elles rendent un ingénieur, un analyste ou un médecin plus productifs) et <b>substituables</b> au travail peu qualifié et répétitif. La demande de travail qualifié augmente plus vite que celle de travail peu qualifié.</p>' +
      '<div data-chain="e1-biais"></div>' +
      '<div class="aut"><span class="mono">GK</span><span class="an">Claudia Goldin et Lawrence Katz<small><i>The Race between Education and Technology</i>, 2008</small></span><span class="ad">Les inégalités de salaires dépendent d’une <b>course</b> : si l’offre de diplômés augmente plus vite que la demande de qualifications, les écarts se réduisent ; sinon, ils se creusent. Claudia Goldin a reçu le prix Nobel en 2023 (pour ses travaux sur le travail des femmes).</span></div>' +
      '<h3>2. La polarisation des emplois</h3>' +
      '<p>L’automatisation remplace d’abord les <b>tâches routinières</b>, faciles à coder : saisie, guichet, travail à la chaîne. Ces emplois sont souvent au milieu de l’échelle des salaires. Les emplois très qualifiés (conception, encadrement) et certains emplois peu qualifiés non routiniers (aide à domicile, livraison, restauration) résistent mieux. L’emploi se <b>polarise</b> aux deux extrémités, et les salaires du milieu stagnent. L’économiste David Autor a documenté ce mécanisme aux États-Unis.</p>' +
      '<div class="ex"><p>Caisses automatiques dans les supermarchés, distributeurs de billets et banque en ligne, logiciels de comptabilité : ces innovations ont réduit le besoin de caissiers, guichetiers et employés de saisie, tandis que les emplois de développeurs et d’analystes de données augmentaient.</p></div>' +
      '<h3>3. Les rentes de l’innovation</h3>' +
      '<p>L’innovateur qui réussit obtient un pouvoir de marché temporaire (brevet, effet de réseau) : des revenus très élevés pour un petit nombre d’entrepreneurs, de dirigeants et d’actionnaires. Avec le numérique, un produit peut conquérir un marché mondial à coût presque nul : « le gagnant rafle presque tout ». Ces rentes nourrissent la hausse des très hauts revenus.</p>' +
      '<div class="plus"><p>Ces inégalités ne sont pas une fatalité : leur ampleur dépend de l’éducation (la « course » de Goldin et Katz), de la formation continue, de la fiscalité et de la concurrence (qui limite la durée des rentes). Philippe Aghion souligne que les inégalités nées de l’innovation s’accompagnent souvent de davantage de mobilité sociale que les rentes héritées.</p></div>' },

    { id: "e1-6", t: "Les limites écologiques de la croissance", h:
      '<div class="def"><b>Croissance soutenable</b> — croissance qui répond aux besoins du présent sans compromettre la capacité des générations futures à répondre aux leurs. Elle suppose de préserver un stock de capital (physique, humain, naturel, institutionnel) transmissible.</div>' +
      '<div class="def"><b>Capital naturel</b> — ensemble des ressources naturelles (sols, eau, forêts, énergies fossiles, minerais, biodiversité, climat stable) qui rendent des services à l’économie.</div>' +
      '<p>Produire, c’est prélever des ressources et rejeter des déchets. La croissance se heurte donc à trois limites, que le programme cite explicitement :</p>' +
      '<ul><li>l’<b>épuisement des ressources</b> non renouvelables (pétrole, gaz, minerais) et la surexploitation des ressources renouvelables (forêts, poissons, nappes d’eau) ;</li><li>la <b>pollution</b> de l’air, de l’eau et des sols ;</li><li>le <b>réchauffement climatique</b>, dû aux émissions de gaz à effet de serre.</li></ul>' +
      '<div data-chain="e1-limites"></div>' +
      '<div class="aut"><span class="mono">DM</span><span class="an">Donella Meadows (dir.)<small>rapport au Club de Rome, 1972</small></span><span class="ad"><i>The Limits to Growth</i> : dans un monde fini, une croissance exponentielle de la production et de la population conduit à l’épuisement des ressources et à une pollution croissante.</span></div>' +
      '<p>Ces dommages sont des <b>externalités négatives</b> : le pollueur ne paie pas le coût qu’il impose aux autres, donc le marché seul produit trop de pollution.</p>' +
      '<h3>L’innovation peut reculer ces limites</h3>' +
      '<ul><li>Elle améliore l’<b>efficacité</b> : produire autant avec moins d’énergie et de matières (moteurs plus sobres, isolation, recyclage).</li><li>Elle permet des <b>substitutions</b> : énergies renouvelables et nucléaire à la place des énergies fossiles, matériaux nouveaux.</li><li>Elle permet de <b>réparer</b> ou de <b>capter</b> : dépollution, captage du carbone (encore peu développé).</li></ul>' +
      '<div data-graph="e1-decouplage"></div>' +
      '<p>La France connaît un <b>découplage absolu</b> : ses émissions territoriales baissent pendant que son PIB augmente. Un découplage <b>relatif</b> serait une hausse des émissions moins rapide que celle du PIB.</p>' +
      '<div class="attn"><p>Ces émissions sont mesurées <b>sur le territoire</b>. Elles ne comptent pas les gaz émis à l’étranger pour fabriquer les biens que la France importe. L’empreinte carbone, qui les inclut, est plus élevée, et sa baisse doit être vérifiée séparément.</p></div>' +
      '<h3>Mais l’innovation a des limites</h3>' +
      '<div data-chain="e1-rebond"></div>' +
      '<div class="aut"><span class="mono">WJ</span><span class="an">William Stanley Jevons<small>1835-1882</small></span><span class="ad"><i>The Coal Question</i> (1865) : les machines à vapeur plus économes en charbon ont fait augmenter la consommation totale de charbon en Angleterre. C’est le « paradoxe de Jevons », forme extrême de l’effet rebond.</span></div>' +
      '<p>Le débat oppose deux conceptions de la soutenabilité :</p>' +
      '<div class="tbl"><table><thead><tr><th></th><th>Soutenabilité faible</th><th>Soutenabilité forte</th></tr></thead><tbody>' +
      '<tr><td><b>Idée</b></td><td>Les capitaux sont <b>substituables</b> : on peut compenser la perte de capital naturel par plus de capital physique, humain ou technologique.</td><td>Une partie du capital naturel est <b>critique</b> et irremplaçable (climat, biodiversité) : elle doit être préservée.</td></tr>' +
      '<tr><td><b>Place de l’innovation</b></td><td>Centrale : le progrès technique reculera les limites.</td><td>Insuffisante seule : il faut aussi des normes, des quotas, une sobriété.</td></tr>' +
      '<tr><td><b>Conséquence</b></td><td>La croissance peut continuer si l’on investit assez.</td><td>Certaines productions doivent baisser ; la croissance doit changer de contenu.</td></tr>' +
      '</tbody></table></div>' +
      '<p>L’action publique (taxes carbone, quotas d’émission, normes, subventions à l’innovation verte) est étudiée dans la question <a href="#r2">R2 Environnement</a>.</p>' }
  ],
  pieges: [
    { f: "« Le PIB a augmenté de 3 %, donc la production a augmenté de 3 %. »", v: "Seulement si c’est le PIB en <b>volume</b>. En valeur, une partie de la hausse peut être due aux prix." },
    { f: "Confondre productivité du travail et productivité globale des facteurs.", v: "La productivité du travail rapporte la production au seul travail ; la PGF mesure l’efficacité de la combinaison travail + capital : c’est elle qui reflète le progrès technique." },
    { f: "« Invention » et « innovation » sont synonymes.", v: "L’invention est une découverte ; l’innovation est sa mise en œuvre économique (produit ou procédé vendu ou utilisé)." },
    { f: "« Endogène » veut dire que le progrès technique vient de l’intérieur du pays.", v: "Endogène signifie qu’il est <b>expliqué par le modèle</b> : produit par des décisions économiques (investir en R&D, en éducation), et non donné de l’extérieur." },
    { f: "« La destruction créatrice, c’est la disparition d’emplois. »", v: "C’est un processus <b>double</b> : des activités disparaissent pendant que d’autres apparaissent. L’effet net sur l’emploi dépend de la vitesse de création et de l’accompagnement des reconversions." },
    { f: "« Le progrès technique crée du chômage, donc il réduit la croissance. »", v: "À long terme, les gains de productivité financent de nouveaux besoins et de nouveaux emplois (déversement de Sauvy) ; les coûts sont réels mais concentrés sur certains travailleurs et territoires." },
    { f: "« La France a découplé : le problème climatique est réglé. »", v: "Le découplage porte sur les émissions territoriales ; il faut aussi regarder l’empreinte (importations) et le rythme : l’objectif de −50 % en 2030 par rapport à 1990 suppose une baisse plus rapide." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Croissance économique</b> : augmentation durable de la production, mesurée par le taux de variation du PIB en volume.</li>' +
    '<li><b>Productivité globale des facteurs</b> : efficacité de la combinaison du travail et du capital ; part de la croissance non expliquée par la hausse des quantités de facteurs (résidu de Solow).</li>' +
    '<li><b>Progrès technique</b> : ensemble des innovations (produit, procédé, organisation) qui augmentent la PGF.</li>' +
    '<li><b>Croissance endogène</b> : le progrès technique est produit par la croissance elle-même via la R&D (Romer), le capital humain (Lucas), les infrastructures publiques (Barro) ; externalités positives.</li>' +
    '<li><b>Institutions</b> : « règles du jeu » formelles et informelles (North) ; droits de propriété et brevets incitent à innover.</li>' +
    '<li><b>Destruction créatrice</b> : l’innovation détruit des activités anciennes en en créant de nouvelles (Schumpeter ; Aghion et Howitt).</li>' +
    '<li><b>Progrès technique biaisé</b> : il favorise la demande de travail qualifié ; polarisation des emplois ; rentes d’innovation.</li>' +
    '<li><b>Soutenabilité faible / forte</b> : substituabilité ou non du capital naturel. <b>Découplage</b> absolu ou relatif. <b>Effet rebond</b> (Jevons).</li></ul>' +
    '<h3>Chiffres à citer</h3><ul>' +
    '<li>PIB en volume ×8,6 entre 1950 et 2025 ; 5,2 %/an en 1950-1973, environ 1 %/an depuis 2007 ; +0,8 % en 2025 (Insee).</li>' +
    '<li>R&D : 2,18 % du PIB en 2023 (SIES).</li>' +
    '<li>Émissions de GES : −34,3 % entre 1990 et 2025 (Citepa) pour un PIB en hausse d’environ 69 %.</li></ul>' +
    '<h3>Auteurs</h3><ul><li>Solow (résidu, 1956-1957) · Romer, Lucas, Barro (croissance endogène) · North (institutions) · Acemoglu et Robinson (institutions inclusives) · Schumpeter (destruction créatrice) · Aghion et Howitt (Nobel 2025) · Sauvy (déversement) · Goldin et Katz (course éducation / technologie) · Meadows (1972) · Jevons (1865).</li></ul>',
  chainesFiche: ["e1-pgf", "e1-endo", "e1-inst", "e1-dc", "e1-biais", "e1-limites", "e1-rebond"],
  quiz: [
    { q: "La croissance économique se mesure par le taux de variation…", c: ["du PIB en volume", "du PIB en valeur", "du PIB par habitant en valeur", "de l’indice des prix"], r: 0, e: "Le PIB en volume neutralise la hausse des prix : il mesure l’évolution des quantités produites.", s: "e1-1" },
    { q: "Entre 1950 et 1973, le PIB français a crû en moyenne d’environ…", c: ["5 % par an", "1 % par an", "10 % par an", "2,5 % par an"], r: 0, e: "5,2 % par an en moyenne selon les niveaux Insee, contre environ 1 % par an entre 2007 et 2019.", s: "e1-1" },
    { q: "La productivité globale des facteurs mesure…", c: ["l’efficacité de la combinaison du travail et du capital", "la production par travailleur", "la quantité de capital par travailleur", "le nombre d’heures travaillées"], r: 0, e: "La PGF rapporte la production à l’ensemble des facteurs : c’est la part de la croissance non expliquée par la hausse des quantités de facteurs.", s: "e1-2" },
    { q: "Chez Solow, pourquoi l’accumulation de capital ne suffit-elle pas à une croissance durable ?", c: ["Parce que ses rendements sont décroissants", "Parce que le capital est non rival", "Parce que l’État la freine", "Parce que le travail est fixe"], r: 0, e: "Chaque machine supplémentaire rapporte moins que la précédente : sans progrès technique, la croissance s’essouffle.", s: "e1-2" },
    { q: "Une croissance « intensive » est due…", c: ["à la hausse de la productivité", "à la hausse de la population active", "à la hausse du stock de capital", "à la hausse des prix"], r: 0, e: "Intensive = produire plus avec les mêmes facteurs. Extensive = utiliser plus de facteurs.", s: "e1-2" },
    { q: "Pour Paul Romer, les connaissances favorisent la croissance parce qu’elles sont…", c: ["non rivales et génèrent des externalités positives", "rares et coûteuses", "protégées à vie par des brevets", "produites uniquement par l’État"], r: 0, e: "Une connaissance peut être utilisée par tous sans s’épuiser : elle se diffuse et profite à d’autres entreprises.", s: "e1-3" },
    { q: "Quel auteur associe la croissance endogène au capital humain ?", c: ["Robert Lucas", "Robert Barro", "Douglass North", "Joseph Schumpeter"], r: 0, e: "Lucas (1988) : l’éducation et la formation rendent les travailleurs plus productifs. Barro insiste sur les infrastructures publiques.", s: "e1-3" },
    { q: "Selon Douglass North, les institutions sont…", c: ["les règles du jeu, formelles et informelles, d’une société", "les seules administrations publiques", "les grandes entreprises", "les banques centrales"], r: 0, e: "Les institutions incluent les lois, les droits de propriété, mais aussi les normes et coutumes.", s: "e1-4" },
    { q: "Un brevet incite à innover parce qu’il…", c: ["accorde un monopole d’exploitation temporaire à l’innovateur", "rend l’innovation gratuite pour tous", "interdit la concurrence pour toujours", "subventionne toutes les entreprises"], r: 0, e: "L’innovateur peut s’approprier les gains de son invention pendant une durée limitée (au plus vingt ans), en échange de sa publication.", s: "e1-4" },
    { q: "La « destruction créatrice » désigne…", c: ["le remplacement d’activités anciennes par des activités nouvelles issues de l’innovation", "la destruction de capital lors des guerres", "la baisse du PIB pendant une récession", "la délocalisation des usines"], r: 0, e: "Schumpeter : les innovations créent de nouvelles activités et en rendent d’autres obsolètes.", s: "e1-4" },
    { q: "Le prix Nobel d’économie 2025 a récompensé Aghion et Howitt pour…", c: ["la théorie de la croissance durable par la destruction créatrice", "la théorie du commerce intra-branche", "l’étude des institutions inclusives", "le modèle de croissance exogène"], r: 0, e: "Leur modèle de 1992 fait de la destruction créatrice le moteur de la croissance. Joel Mokyr a reçu l’autre moitié du prix.", s: "e1-4" },
    { q: "Pourquoi le progrès technique peut-il accroître les inégalités de salaires ?", c: ["Il augmente la demande de travail qualifié plus que celle de travail peu qualifié", "Il fait baisser tous les salaires", "Il supprime surtout les emplois très qualifiés", "Il augmente le temps de travail"], r: 0, e: "C’est le progrès technique biaisé : complémentaire des qualifiés, substituable aux peu qualifiés.", s: "e1-5" },
    { q: "La « polarisation des emplois » signifie que…", c: ["les emplois intermédiaires routiniers reculent au profit des emplois très qualifiés et peu qualifiés non routiniers", "tous les emplois deviennent qualifiés", "l’emploi se concentre dans l’industrie", "les emplois se concentrent dans les grandes villes"], r: 0, e: "L’automatisation remplace d’abord les tâches routinières, souvent au milieu de l’échelle des salaires.", s: "e1-5" },
    { q: "La soutenabilité « forte » considère que…", c: ["une partie du capital naturel est irremplaçable", "tous les capitaux sont substituables", "la croissance doit être maximale", "l’innovation suffit à tout résoudre"], r: 0, e: "Pour la soutenabilité forte, le capital naturel critique (climat, biodiversité) doit être préservé.", s: "e1-6" },
    { q: "L’effet rebond désigne…", c: ["une hausse de l’usage qui annule une partie des économies permises par une innovation plus efficace", "la reprise de la croissance après une récession", "la hausse des prix de l’énergie", "le retour des industries délocalisées"], r: 0, e: "Moins de coût d’usage → plus d’usage : c’est le paradoxe observé par Jevons dès 1865.", s: "e1-6" }
  ],
  cartes: [
    { r: "Croissance économique", v: "Augmentation durable de la production de biens et services, mesurée par le taux de variation du PIB en volume." },
    { r: "PIB en volume", v: "PIB corrigé de la hausse des prix (calculé aux prix d’une année de référence) : il mesure les quantités produites." },
    { r: "Productivité globale des facteurs", v: "Efficacité de la combinaison du travail et du capital ; part de la croissance non expliquée par la hausse des facteurs (résidu)." },
    { r: "Croissance extensive / intensive", v: "Extensive : plus de facteurs (travail, capital). Intensive : plus de productivité." },
    { r: "Résidu de Solow", v: "Part de la croissance que l’accumulation des facteurs n’explique pas, attribuée au progrès technique (Solow, 1957)." },
    { r: "Progrès technique", v: "Ensemble des innovations qui améliorent les produits, les procédés et l’organisation, et font croître la PGF." },
    { r: "Innovation (vs invention)", v: "Application économique d’une invention : nouveau produit, procédé, organisation ou débouché. L’invention n’est que la découverte." },
    { r: "Croissance endogène", v: "Le progrès technique est produit par des décisions économiques (R&D, capital humain, infrastructures), financées par la croissance : cercle vertueux." },
    { r: "Externalité positive", v: "Effet favorable de l’activité d’un agent sur d’autres, sans contrepartie monétaire (ex. : diffusion des connaissances)." },
    { r: "Capital humain", v: "Connaissances et compétences acquises par la formation et l’expérience, qui augmentent la productivité (Lucas)." },
    { r: "Institutions", v: "Règles du jeu formelles (lois, droits de propriété) et informelles (normes) qui encadrent les comportements (North)." },
    { r: "Droits de propriété", v: "Droits d’utiliser un bien, d’en tirer un revenu et de le céder ; leur garantie incite à investir et innover." },
    { r: "Destruction créatrice", v: "Processus par lequel l’innovation fait disparaître des activités anciennes et en crée de nouvelles (Schumpeter, 1942)." },
    { r: "Progrès technique biaisé", v: "Progrès technique qui augmente surtout la demande de travail qualifié, et creuse les écarts de salaires." },
    { r: "Polarisation des emplois", v: "Recul des emplois intermédiaires routiniers au profit des emplois très qualifiés et des emplois peu qualifiés non routiniers." },
    { r: "Croissance soutenable", v: "Croissance qui répond aux besoins présents sans compromettre ceux des générations futures (préservation du capital transmis)." },
    { r: "Soutenabilité faible / forte", v: "Faible : capitaux substituables. Forte : une partie du capital naturel est irremplaçable." },
    { r: "Découplage absolu", v: "La production augmente pendant que les émissions ou prélèvements baissent (France 1990-2025 : PIB +69 %, GES −34,3 %)." },
    { r: "Effet rebond", v: "Les gains d’efficacité baissent le coût d’usage, d’où plus d’usage, qui annule une partie des économies (Jevons, 1865)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site, données Insee", t: "Calculer avec le PIB", enonce:
      '<p>PIB de la France en volume (milliards d’euros 2020) : 1950 : 309,1 ; 1973 : 999,1 ; 2007 : 2 233,0 ; 2019 : 2 504,6 ; 2024 : 2 625,6 ; 2025 : 2 646,7. Source : Insee.</p><ol><li>Calcule le coefficient multiplicateur entre 1950 et 1973, puis entre 2007 et 2019.</li><li>Calcule le taux de croissance de 2025.</li><li>Sachant que (999,1 / 309,1)<sup>1/23</sup> ≈ 1,052, rédige une phrase sur la croissance des Trente Glorieuses.</li></ol>',
      corrige: '<ol><li>1950-1973 : 999,1 ÷ 309,1 ≈ 3,23 : le PIB a été multiplié par 3,2 en 23 ans. 2007-2019 : 2 504,6 ÷ 2 233,0 ≈ 1,12 : +12 % en 12 ans seulement.</li><li>(2 646,7 − 2 625,6) ÷ 2 625,6 × 100 ≈ +0,8 %.</li><li>« Entre 1950 et 1973, selon l’Insee, le PIB de la France en volume a crû en moyenne d’environ 5,2 % par an : il a été multiplié par 3,2. »</li></ol><div class="marge"><b>Méthode :</b> un coefficient multiplicateur se lit « multiplié par » ; pour comparer deux périodes de longueurs différentes, on compare des taux <b>annuels moyens</b>, pas des taux globaux.</div>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que les institutions peuvent favoriser la croissance économique.", enonce: "<p>3,5 points. Réponds en une vingtaine de lignes, sans document.</p>",
      methode: "<p>Définir institutions et croissance ; deux mécanismes distincts, chacun en AEI : droits de propriété → incitation à innover ; institutions inclusives / État de droit → investissement et concurrence. Un exemple chacun.</p>",
      corrige: '<div class="copie"><p>Les institutions sont, selon Douglass North, les « règles du jeu » d’une société, formelles (lois, droits de propriété) ou informelles (normes). Elles peuvent favoriser la croissance, c’est-à-dire l’augmentation durable de la production, de deux façons.</p><p>D’abord, des droits de propriété garantis incitent à innover. Le brevet accorde à l’innovateur un monopole d’exploitation temporaire : il peut s’approprier les gains de son invention, ce qui l’incite à investir en recherche et développement. Les innovations augmentent la productivité globale des facteurs, donc la croissance. Sans cette protection, l’innovation serait copiée sans contrepartie et personne ne prendrait le risque de la financer.</p><p>Ensuite, des institutions inclusives favorisent l’investissement de tous. Selon Acemoglu et Robinson, quand l’État de droit protège chacun contre l’arbitraire et que la concurrence est ouverte, entrepreneurs et ménages investissent car leurs gains futurs sont sûrs. À l’inverse, des institutions extractives captent la richesse au profit d’une élite. La comparaison entre la Corée du Sud, riche et innovante, et la Corée du Nord, restée très pauvre, montre l’effet de ces institutions sur des populations au départ comparables.</p></div><div class="marge"><b>Barème indicatif :</b> définitions (0,5) ; deux mécanismes expliqués (2) ; exemples précis (1).</div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, document Insee", t: "La croissance française depuis 1950", enonce:
      '<p>Document : le graphique « Taux de croissance du PIB de la France en volume, 1950-2025 » (Insee) dans <a href="#e1:e1-1">le cours</a>.</p><ol><li>À l’aide du document, comparez la croissance de 1950-1973 à celle des années 2010.</li><li>À l’aide du document et de vos connaissances, montrez que le ralentissement de la croissance peut s’expliquer par celui des gains de productivité.</li></ol>',
      corrige: '<ol><li>Selon l’Insee, la croissance du PIB en volume dépasse le plus souvent 4 % par an entre 1950 et 1973 (8,0 % en 1960, 7,1 % en 1969), soit 5,2 % par an en moyenne. Dans les années 2010, elle reste presque toujours sous 2,5 % (0,2 % en 2012, 2,1 % en 2017). En moyenne, elle est de 1,4 % par an de 2010 à 2019, soit près de quatre fois moins qu’entre 1950 et 1973.</li><li>La croissance intensive repose sur la hausse de la productivité globale des facteurs. Pendant les Trente Glorieuses, la France rattrapait le retard technologique sur les États-Unis : elle adoptait des techniques déjà inventées (production de masse, mécanisation agricole), d’où des gains de productivité très rapides et une croissance forte. Une fois le rattrapage achevé, il faut innover soi-même, ce qui est plus lent ; la tertiarisation pèse aussi, car les gains de productivité sont plus difficiles dans beaucoup de services. Moins de gains de productivité, c’est moins de baisse des coûts, moins de hausse du pouvoir d’achat et de la demande : la croissance ralentit, comme le montre le document après 1974 et surtout après 2008.</li></ol><div class="marge"><b>Méthode :</b> question 1 = données précises avec année, unité et source ; question 2 = un mécanisme (chaîne causale) relié au document.</div>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet inventé pour le site", t: "À l’aide du dossier, montrez que l’innovation est une source de croissance économique.", enonce:
      '<p><b>Document 1</b> : effort de recherche de la France, 2,18 % du PIB en 2023 (61,5 milliards d’euros ; SIES). <b>Document 2</b> : graphique de la croissance française 1950-2025 (Insee). <b>Document 3</b> (texte factuel) : la mise au point des vaccins à ARN messager, fondée sur des recherches universitaires financées sur fonds publics, puis industrialisée par des entreprises en 2020.</p>',
      corrige: '<p><b>Introduction.</b> L’innovation est l’application économique d’une invention ; la croissance, l’augmentation durable de la production mesurée par le PIB en volume. On montrera que l’innovation stimule la croissance parce qu’elle accroît la productivité, puis parce qu’elle crée de nouveaux produits et entretient un cercle vertueux.</p><p><b>I. L’innovation accroît la productivité globale des facteurs.</b> Innovations de procédé → produire plus avec autant de facteurs → baisse des coûts → baisse des prix et hausse des revenus → hausse de la demande. Le document 2 montre une croissance forte quand les gains de productivité étaient élevés (5,2 % par an de 1950 à 1973). Solow : le résidu.</p><p><b>II. L’innovation crée de nouveaux produits et de nouveaux marchés.</b> Destruction créatrice (Schumpeter) : de nouvelles activités, de nouveaux emplois, de nouveaux investissements. Document 3 : les vaccins à ARN, nouveaux produits, nouvelle industrie.</p><p><b>III. Un cercle vertueux : la croissance finance l’innovation.</b> Croissance endogène : R&D (Romer), capital humain (Lucas), recherche publique (Barro). Document 1 : 61,5 milliards d’euros de R&D en 2023. Document 3 : la recherche publique a précédé l’innovation privée (externalités).</p><p><b>Conclusion.</b> L’innovation est une source majeure de croissance par la productivité et la création de nouveaux marchés, et la croissance lui fournit en retour ses moyens.</p><div class="marge"><b>Attendus :</b> chaque partie mobilise au moins un document cité précisément et un mécanisme. Pas de partie « limites » : on ne discute pas un « Montrez que ».</div>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Le progrès technique suffit-il à rendre la croissance soutenable ?", enonce: "<p>Construis la problématique et le plan détaillé, puis compare au corrigé.</p>",
      corrige: '<p><b>Problématique.</b> La croissance dégrade le capital naturel. Le progrès technique, qui repousse depuis deux siècles les limites de la production, peut-il à lui seul concilier croissance et préservation de l’environnement, ou faut-il d’autres leviers ?</p><p><b>I. Le progrès technique peut reculer les limites écologiques</b><br>A. Il améliore l’efficacité : moins d’énergie et de matières par unité produite (procédés, isolation, recyclage).<br>B. Il permet des substitutions : énergies bas carbone à la place des fossiles ; nouveaux matériaux.<br>C. Il permet un découplage : France 1990-2025, PIB en volume +69 %, émissions territoriales −34,3 % (Insee, Citepa). Soutenabilité faible : les capitaux sont substituables.</p><p><b>II. Mais il ne suffit pas</b><br>A. L’effet rebond annule une partie des gains (Jevons, 1865).<br>B. Le découplage est fragile : émissions importées (empreinte), rythme insuffisant au regard des objectifs (−50 % en 2030 par rapport à 1990).<br>C. Une partie du capital naturel est irremplaçable (soutenabilité forte) : biodiversité, climat.</p><p><b>III. Il doit être orienté et complété par l’action publique</b><br>A. Les externalités négatives appellent des instruments : taxation, quotas, normes (question R2).<br>B. Subventionner l’innovation verte, car le marché sous-investit dans les technologies propres (externalités).<br>C. Changer le contenu de la croissance : sobriété, services, réparation.</p><div class="marge"><b>Pourquoi ce plan ?</b> « Suffit-il » appelle un plan qui reconnaît le rôle du progrès technique (oui), montre ses limites (pas seul), puis propose une réponse construite (orienté et complété).</div>' }
  ]
};
