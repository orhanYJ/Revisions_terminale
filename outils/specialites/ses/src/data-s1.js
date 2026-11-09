GRAPHES["s1-pcs"] = {
  type: "lignes", t: "La structure socioprofessionnelle de l’emploi en France, 1982-2024", spark: 2,
  s: "Part de chaque catégorie dans l’emploi, en %. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.",
  src: "Source : Insee, enquête Emploi 2024, séries longues sur le marché du travail. Champ : France, personnes vivant dans un logement ordinaire, en emploi. L’enquête a connu des changements de méthode (ruptures de série).",
  unite: " %", pasX: 7, h: 320, min: 0, max: 32,
  x: [1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
  series: [
    { n: "Agriculteurs", c: 4, v: [7.5,7.5,7.8,7.4,6.9,6.8,6.4,6.1,5.6,5.4,5.0,4.5,4.2,3.9,3.7,3.6,3.3,3.2,3.0,2.9,3.0,3.3,3.0,2.8,2.9,2.5,2.2,2.4,2.4,2.4,2.3,2.4,2.3,2.1,2.2,2.0,1.9,1.8,1.7,1.5,1.6,1.5,1.3] },
    { n: "Artisans, commerçants, chefs d’entreprise", c: 6, v: [7.7,7.6,7.7,7.4,7.6,7.4,7.5,7.2,7.7,7.5,7.4,7.1,7.2,7.0,6.8,6.8,6.6,6.4,6.0,5.7,5.5,5.7,5.5,5.6,5.8,5.8,5.7,5.8,6.1,6.0,5.9,5.7,5.8,5.7,5.9,5.8,5.8,6.0,6.1,6.5,6.8,6.7,6.8] },
    { n: "Cadres", c: 2, v: [8.0,8.5,8.8,8.7,9.3,9.5,10.2,10.0,10.8,11.4,12.0,12.2,12.7,12.8,12.9,13.1,13.2,13.5,13.7,14.2,14.7,15.1,15.4,15.9,16.1,16.2,16.5,16.8,17.1,17.9,18.3,17.8,17.5,18.1,18.4,18.6,19.0,20.0,21.1,21.5,21.6,22.4,23.0] },
    { n: "Professions intermédiaires", c: 3, v: [18.8,19.4,19.9,20.2,20.2,20.4,20.3,20.4,19.9,20.6,20.6,21.5,21.3,21.4,21.3,21.5,21.5,21.6,21.5,21.7,21.9,21.8,22.1,22.0,22.0,22.0,22.7,23.1,23.3,23.3,23.6,24.3,24.7,24.5,24.9,24.8,24.9,24.8,25.1,24.7,24.7,25.1,25.2] },
    { n: "Employés", c: 5, v: [26.4,26.3,26.4,26.7,27.1,27.4,27.7,28.2,27.9,27.2,27.4,28.5,28.7,29.0,29.3,29.4,29.5,29.7,29.7,29.8,30.1,30.3,30.1,30.2,30.0,30.3,30.3,30.1,29.7,29.2,29.0,29.1,29.2,29.0,28.1,27.9,27.9,27.5,26.5,26.2,25.9,25.2,24.8] },
    { n: "Ouvriers", c: 1, v: [29.9,28.9,27.8,28.0,27.2,26.9,26.2,26.5,26.6,26.5,26.0,24.7,24.4,24.5,24.6,24.4,24.7,24.7,25.3,25.2,24.4,23.4,23.6,23.0,22.8,22.8,22.3,21.5,21.0,20.8,20.6,20.3,20.2,20.1,20.1,20.5,20.1,19.4,19.1,19.1,18.9,18.6,18.0] }
  ]
};
GRAPHES["s1-sexe"] = {
  type: "hbarres", t: "Femmes et hommes en emploi selon la catégorie socioprofessionnelle, 2024",
  s: "Répartition de chaque sexe, en % (chaque série totalise 100 % avec 0,9 % de non-renseignés).",
  src: "Source : Insee, enquête Emploi 2024 (Emploi, chômage, revenus du travail, édition 2025).",
  unite: " %", lab: 150,
  cats: ["Agriculteurs", "Artisans, commerçants, chefs d’entreprise", "Cadres", "Professions intermédiaires", "Employés", "Ouvriers"],
  series: [{ n: "Femmes", v: [0.7, 4.8, 20.4, 27.3, 38.8, 7.2], c: 2 }, { n: "Hommes", v: [1.9, 8.8, 25.4, 23.2, 11.6, 28.2], c: 1 }]
};
GRAPHES["s1-niveau"] = {
  type: "hbarres", t: "L’échelle des niveaux de vie en 2024", s: "Niveau de vie annuel par unité de consommation, en euros.",
  src: "Source : Insee Première n° 2117, juillet 2026. Champ : France métropolitaine, personnes vivant dans un logement ordinaire.",
  unite: " €", dec: 0, lab: 160,
  cats: ["Plafond des 10 % les plus modestes (D1)", "Médiane (D5)", "Plancher des 10 % les plus aisés (D9)"], series: [{ n: "2024", v: [13970, 26740, 48580], c: 1 }]
};

CHAINES["s1-tert"] = { t: "Pourquoi l’emploi s’est tertiarisé et salarisé", e: [
  { t: "Forts gains de productivité dans l’agriculture puis dans l’industrie", k: "cause" },
  { f: [{ t: "Il faut moins de travailleurs pour produire autant dans ces secteurs" }, { t: "Les revenus augmentent : nouveaux besoins de santé, éducation, loisirs, commerce" }], a: "donc" },
  { t: "Les emplois se déversent vers les services (Sauvy)", a: "donc" },
  { t: "Les petites exploitations et les petits commerces indépendants reculent face aux grandes entreprises", a: "en même temps" },
  { t: "Tertiarisation et salarisation de l’emploi", k: "effet", a: "donc" }
] };
CHAINES["s1-qualif"] = { t: "L’élévation du niveau de qualification", e: [
  { t: "Allongement des études : massification scolaire", k: "cause" },
  { t: "Plus de diplômés arrivent sur le marché du travail", a: "donc" },
  { t: "Le progrès technique et la tertiarisation demandent davantage de qualifications", a: "et" },
  { t: "Les emplois de cadres et de professions intermédiaires se multiplient ; les emplois peu qualifiés reculent", k: "effet", a: "donc" }
] };
CHAINES["s1-marx"] = { t: "La logique des classes chez Marx", e: [
  { t: "Propriété ou non des moyens de production (usines, machines, terres)", k: "cause" },
  { t: "Le prolétariat doit vendre sa force de travail à la bourgeoisie", a: "donc" },
  { t: "Exploitation : la bourgeoisie s’approprie la plus-value créée par le travail", a: "donc" },
  { t: "Des intérêts opposés : la « classe en soi » existe objectivement", a: "donc" },
  { t: "Par la prise de conscience, elle devient « classe pour soi » : lutte des classes", k: "effet", a: "si" }
] };
CHAINES["s1-indiv"] = { t: "La multiplication des facteurs d’individualisation", e: [
  { t: "Hausse du niveau de vie et de l’éducation, protection sociale", k: "cause" },
  { t: "Les individus dépendent moins de leur groupe d’origine", a: "donc" },
  { t: "Trajectoires plus diverses : mobilités, études, familles recomposées, consommations, loisirs", a: "donc" },
  { t: "Identités plurielles (métier, genre, génération, territoire, goûts)", a: "donc" },
  { t: "Le sentiment d’appartenance à une classe s’affaiblit", k: "frein", a: "donc" }
] };

CH.s1 = {
  chapo: "Cadres, ouvriers, employés : la société française se décrit souvent par les professions. Mais le revenu, le diplôme, le sexe, l’âge ou le quartier comptent aussi. Ce chapitre montre comment l’espace social est structuré et hiérarchisé, comment il a changé depuis 1950, et s’il est encore pertinent de parler de classes sociales.",
  essentiel: [
    "L’espace social est structuré et <b>hiérarchisé par plusieurs facteurs</b> : catégorie socioprofessionnelle, revenu, diplôme, composition du ménage, âge (cycle de vie), sexe, lieu de résidence.",
    "Depuis les années 1950, la structure socioprofessionnelle se transforme : <b>salarisation</b> (86,7 % des emplois en 2024), <b>tertiarisation</b> (76,6 %), <b>élévation des qualifications</b> (8,0 % de cadres en 1982, 23,0 % en 2024), <b>féminisation</b> des emplois.",
    "<b>Marx</b> définit les classes par la place dans les rapports de production et la conscience de classe ; <b>Weber</b> propose une approche multidimensionnelle (classes, groupes de statut, partis).",
    "La pertinence des classes fait débat : <b>moyennisation</b> (Mendras) ou maintien des écarts entre classes (Bourdieu, Chauvel) ; classes de plus en plus <b>hétérogènes</b> ; poids des <b>rapports de genre</b>.",
    "Les <b>identifications subjectives</b> à une classe s’affaiblissent (sauf peut-être en haut de l’échelle) et les facteurs d’<b>individualisation</b> se multiplient : d’où le débat sur des « classes sans conscience »."
  ],
  chiffres: [
    { n: "23,0 %", l: "des personnes en emploi sont cadres en 2024, presque trois fois plus qu’en 1982 (8,0 %).", s: "Insee, enquête Emploi 2024" },
    { n: "86,7 %", l: "des personnes en emploi sont salariées en 2024 ; 13,3 % sont indépendantes.", s: "Insee, enquête Emploi 2024" },
    { n: "3,48", l: "le rapport entre le plancher des 10 % les plus aisés et le plafond des 10 % les plus modestes (niveau de vie, 2024).", s: "Insee Première n° 2117" }
  ],
  objectifs: [
    { bo: "Savoir identifier les multiples facteurs de structuration et de hiérarchisation de l’espace social (catégorie socioprofessionnelle, revenu, diplôme, composition du ménage, position dans le cycle de vie, sexe, lieu de résidence).", clair: "Savoir citer et illustrer les sept facteurs qui organisent et hiérarchisent la société.", voir: "s1-1" },
    { bo: "Comprendre les principales évolutions de la structure socioprofessionnelle en France depuis la seconde moitié du XXe siècle (salarisation, tertiarisation, élévation du niveau de qualification, féminisation des emplois).", clair: "Décrire et expliquer quatre grandes évolutions, chiffres à l’appui.", voir: "s1-3" },
    { bo: "Connaître les théories des classes et de la stratification sociale dans la tradition sociologique (Marx, Weber) ; comprendre que la pertinence d’une approche en termes de classes sociales pour rendre compte de la société française fait l’objet de débats théoriques et statistiques : évolution des distances inter- et intra-classes, articulation avec les rapports sociaux de genre, identifications subjectives à un groupe social, multiplication des facteurs d’individualisation.", clair: "Connaître Marx et Weber, puis les arguments pour et contre l’existence de classes sociales aujourd’hui.", voir: "s1-4" }
  ],
  notions: ["espace social", "structure sociale", "hiérarchisation", "catégorie socioprofessionnelle (PCS)", "niveau de vie", "diplôme", "ménage", "cycle de vie", "salarisation", "tertiarisation", "qualification", "féminisation", "classe sociale", "classe en soi / classe pour soi", "conscience de classe", "rapports de production", "stratification sociale", "groupe de statut", "moyennisation", "distances inter-classes / intra-classes", "rapports sociaux de genre", "identification subjective", "individualisation"],
  sections: [
    { id: "s1-1", t: "Un espace social structuré par de multiples facteurs", h:
      '<p class="lede">Les sociologues parlent d’<b>espace social</b> : les individus y occupent des positions différentes, plus ou moins proches et plus ou moins élevées. Cet espace est <b>structuré</b> (il existe des groupes qui se ressemblent) et <b>hiérarchisé</b> (ces positions donnent un accès inégal aux ressources : revenu, pouvoir, prestige).</p>' +
      '<p>Le programme cite sept facteurs.</p>' +
      '<h3>1. La catégorie socioprofessionnelle</h3><p>La profession résume beaucoup : revenu, diplôme, conditions de travail, mode de vie. C’est pourquoi l’Insee classe la population en PCS (section suivante).</p>' +
      '<h3>2. Le revenu</h3>' +
      '<div data-graph="s1-niveau"></div>' +
      '<p>En 2024, la moitié de la population vit avec moins de 26 740 euros par an et par unité de consommation (2 228 euros par mois pour une personne seule). Le seuil des 10 % les plus aisés est 3,48 fois plus élevé que le plafond des 10 % les plus modestes. Le taux de pauvreté atteint 15,4 % (9,8 millions de personnes), son plus haut niveau depuis 1996, et l’indice de Gini (0,302) est au plus haut depuis le début de la série (Insee). Le <b>patrimoine</b> est encore plus inégalement réparti que le revenu.</p>' +
      '<h3>3. Le diplôme</h3><p>Il conditionne l’accès aux emplois qualifiés, le salaire, le risque de chômage, et aussi les pratiques culturelles et la participation politique. Il est lui-même lié à l’origine sociale (question <a href="#s2">S2</a>).</p>' +
      '<h3>4. La composition du ménage</h3><p>Vivre seul, en couple, avec ou sans enfants change le niveau de vie (qui se calcule par unité de consommation). Les <b>familles monoparentales</b>, le plus souvent une mère avec ses enfants, sont avec les chômeurs les plus touchées par la pauvreté (Insee, 2024).</p>' +
      '<h3>5. La position dans le cycle de vie</h3><p>À diplôme égal, on gagne plus en milieu de carrière qu’au début ; le patrimoine s’accumule avec l’âge. Les jeunes cumulent emplois précaires et faible patrimoine. En 2024, le taux de pauvreté des retraités revient au niveau de celui des actifs (10,4 %).</p>' +
      '<h3>6. Le sexe</h3><p>Femmes et hommes n’occupent pas les mêmes positions : en 2024, 38,8 % des femmes en emploi sont employées contre 11,6 % des hommes, et 28,2 % des hommes sont ouvriers contre 7,2 % des femmes (Insee). Les femmes sont plus souvent à temps partiel et moins rémunérées.</p>' +
      '<h3>7. Le lieu de résidence</h3><p>Grandes métropoles, villes moyennes, espaces ruraux, quartiers prioritaires ou « beaux quartiers » : le territoire concentre les ressources (emplois qualifiés, grandes écoles, services) et façonne les fréquentations. Michel Pinçon et Monique Pinçon-Charlot ont montré comment la grande bourgeoisie entretient son entre-soi dans quelques quartiers et communes.</p>' +
      '<div class="attn"><p>Ces facteurs se <b>cumulent</b> et se renforcent : un diplôme élevé donne accès à un emploi de cadre, donc à un revenu élevé, qui permet d’habiter un quartier favorisé, où les enfants fréquentent des établissements réputés. C’est ce qu’a demandé le sujet du bac 2026 (jour 2, partie 3) : montrer que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l’espace social.</p></div>' },

    { id: "s1-2", t: "Les PCS, l’outil de l’Insee", h:
      '<div class="def"><b>Professions et catégories socioprofessionnelles (PCS)</b> — nomenclature de l’Insee qui classe la population selon la profession actuelle (ou l’ancienne), le statut (salarié ou non), la qualification, la taille de l’entreprise pour les indépendants et la nature de l’employeur (public ou privé) pour les salariés.</div>' +
      '<p>Créée en 1954 sous le nom de CSP, refondue en 1982 (PCS), rénovée en 2003 puis en 2020 (PCS 2020), elle regroupe des personnes à la situation sociale proche, qui ont souvent des comportements semblables. Au niveau le plus agrégé, six groupes pour les personnes en emploi :</p>' +
      '<div class="tbl"><table><thead><tr><th>Groupe socioprofessionnel</th><th class="n">Part de l’emploi en 2024</th></tr></thead><tbody>' +
      '<tr><td>1. Agriculteurs exploitants</td><td class="n">1,3 %</td></tr><tr><td>2. Artisans, commerçants et chefs d’entreprise</td><td class="n">6,8 %</td></tr><tr><td>3. Cadres et professions intellectuelles supérieures</td><td class="n">23,0 %</td></tr><tr><td>4. Professions intermédiaires</td><td class="n">25,2 %</td></tr><tr><td>5. Employés</td><td class="n">24,8 %</td></tr><tr><td>6. Ouvriers</td><td class="n">18,0 %</td></tr><tr><td><i>Non renseigné</i></td><td class="n">0,9 %</td></tr></tbody></table></div>' +
      '<p class="src-l">Source : Insee, enquête Emploi 2024.</p>' +
      '<p>La PCS 2020 propose aussi une <b>PCS Ménage</b>, qui classe les ménages d’après la profession de leurs membres : une manière de tenir compte du fait que la position sociale se joue souvent au niveau du couple.</p>' +
      '<div class="attn"><p>Les PCS ne sont pas des classes sociales. Elles sont construites pour la statistique, sans hypothèse sur la conscience ou les conflits de groupes. Mais elles servent à vérifier si des classes existent : les écarts de revenu, de diplôme ou de pratiques entre PCS sont-ils grands et durables ?</p></div>' },

    { id: "s1-3", t: "Les grandes évolutions depuis 1950", h:
      '<div data-graph="s1-pcs"></div>' +
      '<p>Le graphique résume quarante ans de transformations : les ouvriers passent de 29,9 % à 18,0 % de l’emploi, les agriculteurs de 7,5 % à 1,3 %, tandis que les cadres passent de 8,0 % à 23,0 %. En 2024, pour la première fois depuis 1982, les professions intermédiaires dépassent les employés (Insee). Quatre évolutions sont au programme.</p>' +
      '<h3>1. La salarisation</h3><p>La part des salariés dans l’emploi a fortement augmenté depuis les années 1950 avec le recul des agriculteurs exploitants et des petits commerçants et artisans. En 2024, 86,7 % des personnes en emploi sont salariées, dont 72,9 % en CDI ou fonctionnaires. On observe toutefois un léger regain des indépendants (13,3 %, plus haut niveau depuis 1999), porté par les micro-entrepreneurs (3,6 % de l’emploi) : plateformes de livraison, VTC, services.</p>' +
      '<h3>2. La tertiarisation</h3><p>En 2024, le tertiaire (commerce, transports, santé, éducation, administration, services aux entreprises) rassemble 76,6 % des emplois, contre 12,6 % pour l’industrie, 6,6 % pour la construction et 2,3 % pour l’agriculture (Insee). Ce mouvement concerne surtout les femmes : 87,0 % d’entre elles travaillent dans le tertiaire.</p>' +
      '<div data-chain="s1-tert"></div>' +
      '<h3>3. L’élévation du niveau de qualification</h3><p>Les cadres et professions intermédiaires représentent 48,1 % des personnes en emploi en 2024 (Insee). Les emplois d’ouvriers non qualifiés reculent avec l’automatisation et les délocalisations.</p>' +
      '<div data-chain="s1-qualif"></div>' +
      '<h3>4. La féminisation des emplois</h3><p>Les femmes représentent 48,8 % des personnes en emploi en 2024 (14,2 millions sur 29,0 millions). Leur taux d’emploi (66,2 % chez les 15-64 ans) reste inférieur à celui des hommes (71,5 %). Leur entrée massive dans l’emploi depuis les années 1960 s’explique par l’allongement de leurs études, la tertiarisation, la maîtrise de la fécondité et l’évolution des normes. Mais les emplois restent <b>genrés</b> :</p>' +
      '<div data-graph="s1-sexe"></div>' +
      '<p>Lecture : en 2024, 38,8 % des femmes en emploi sont employées (aides à domicile, secrétaires, agentes d’entretien, vendeuses), contre 11,6 % des hommes. La part des cadres progresse chez les femmes, mais reste plus faible que chez les hommes (20,4 % contre 25,4 %).</p>' },

    { id: "s1-4", t: "Les classes sociales : Marx et Weber", h:
      '<div class="def"><b>Classe sociale</b> — grand groupe d’individus qui partagent une position comparable dans la hiérarchie sociale (revenus, patrimoine, pouvoir, prestige) et, selon les approches, des intérêts, un mode de vie et une conscience communs.</div>' +
      '<div class="aut"><span class="mono">KM</span><span class="an">Karl Marx<small>1818-1883</small></span><span class="ad">Les classes se définissent par leur place dans les <b>rapports de production</b> : la <b>bourgeoisie</b> possède les moyens de production, le <b>prolétariat</b> n’a que sa force de travail à vendre. La société capitaliste tend à se <b>bipolariser</b> entre ces deux classes, dont les intérêts sont opposés.</span></div>' +
      '<div data-chain="s1-marx"></div>' +
      '<p>Pour Marx, une classe n’existe pleinement que si elle est à la fois <b>classe en soi</b> (une position objective commune) et <b>classe pour soi</b> (une conscience de ses intérêts et une mobilisation collective). C’est une approche <b>réaliste</b> : les classes existent réellement et sont en conflit (lutte des classes), moteur de l’histoire (<i>Manifeste du parti communiste</i>, avec Engels, 1848).</p>' +
      '<div class="aut"><span class="mono">MW</span><span class="an">Max Weber<small>1864-1920</small></span><span class="ad">La hiérarchie sociale a <b>trois dimensions</b> indépendantes : l’ordre <b>économique</b> (les <b>classes</b>, définies par les chances d’accès aux biens et aux revenus sur le marché), l’ordre <b>social</b> (les <b>groupes de statut</b>, définis par le prestige et l’honneur social, qui se traduisent par des styles de vie) et l’ordre <b>politique</b> (les <b>partis</b>, qui visent le pouvoir). <i>Économie et société</i>, 1922.</span></div>' +
      '<div class="tbl"><table><thead><tr><th></th><th>Marx</th><th>Weber</th></tr></thead><tbody>' +
      '<tr><td><b>Critère</b></td><td>Place dans les rapports de production</td><td>Trois ordres : économique, social, politique</td></tr>' +
      '<tr><td><b>Approche</b></td><td>Réaliste : les classes existent et s’opposent</td><td>Nominaliste : les classes sont des regroupements construits par le chercheur</td></tr>' +
      '<tr><td><b>Conscience</b></td><td>Indispensable (classe pour soi)</td><td>Pas nécessaire ; les classes ne sont pas forcément des communautés</td></tr>' +
      '<tr><td><b>Relations</b></td><td>Conflit, lutte des classes</td><td>Hiérarchie graduée : <b>stratification</b></td></tr>' +
      '</tbody></table></div>' +
      '<div class="ex"><p>Un professeur des écoles a un revenu moyen (ordre économique) mais un prestige plutôt élevé (ordre social) ; un commerçant aisé peut avoir un revenu supérieur et moins de prestige. Weber permet de penser ces décalages, que l’approche de Marx, centrée sur la propriété, laisse de côté.</p></div>' +
      '<div class="aut"><span class="mono">PB</span><span class="an">Pierre Bourdieu<small>1930-2002</small></span><span class="ad">Synthèse des deux traditions : l’espace social se lit selon le <b>volume</b> global de capital et sa <b>structure</b> (part du capital économique et du capital culturel). Les classes se distinguent aussi par leurs goûts et styles de vie (<i>La Distinction</i>, 1979).</span></div>' },

    { id: "s1-5", t: "Les classes sociales sont-elles encore pertinentes ?", h:
      '<p class="lede">Le programme cite quatre terrains de débat. Pour chacun, il faut connaître les arguments des deux côtés.</p>' +
      '<h3>1. Les distances entre classes (inter-classes)</h3>' +
      '<div class="aut"><span class="mono">HM</span><span class="an">Henri Mendras<small>1927-2003</small></span><span class="ad"><i>La Seconde Révolution française 1965-1984</i> (1988) : la hausse des revenus, la diffusion de la consommation de masse et la croissance des professions intermédiaires font émerger une vaste <b>constellation centrale</b>. La société prend la forme d’une <b>toupie</b> : c’est la <b>moyennisation</b>.</span></div>' +
      '<p>Mais d’autres constats montrent que les écarts ne disparaissent pas : les inégalités de niveau de vie atteignent en 2024 leur plus haut niveau depuis le début des séries en 1996 (Insee) ; le patrimoine est très concentré ; les écarts de réussite scolaire et d’accès aux grandes écoles restent forts.</p>' +
      '<div class="aut"><span class="mono">LC</span><span class="an">Louis Chauvel<small>né en 1967</small></span><span class="ad">« Le retour des classes sociales ? » (2001) : depuis les années 1980, la réduction des inégalités s’est arrêtée. Il parle de « <b>classes sans conscience</b> » : les écarts objectifs persistent, mais la conscience de classe s’est affaiblie.</span></div>' +
      '<h3>2. Les distances au sein des classes (intra-classes)</h3>' +
      '<p>Les grands groupes sont devenus <b>hétérogènes</b>. Les ouvriers ne sont plus surtout des hommes de la grande industrie : beaucoup travaillent dans la logistique, le transport, l’entretien. Les employés se divisent entre qualifiés et peu qualifiés (en 2024, 17,0 % des femmes en emploi sont employées peu qualifiées). Les cadres du public et ceux du privé n’ont ni les mêmes revenus ni les mêmes votes. Cette hétérogénéité affaiblit l’unité de chaque classe. À l’inverse, on peut regrouper ouvriers et employés en <b>classes populaires</b> : 42,8 % des personnes en emploi en 2024 (Insee), dont les conditions de vie restent proches.</p>' +
      '<h3>3. L’articulation avec les rapports sociaux de genre</h3>' +
      '<p>Raisonner seulement en classes oublie que les femmes et les hommes d’une même classe n’ont pas la même position : écarts de salaires, temps partiel, tâches domestiques, plafond de verre. La position sociale d’une femme a longtemps été mesurée par celle de son conjoint. Les rapports de genre <b>se combinent</b> aux rapports de classe : une ouvrière cumule deux formes de domination.</p>' +
      '<div class="plus"><p>La juriste Kimberlé Crenshaw a proposé en 1989 la notion d’<b>intersectionnalité</b> pour penser le croisement des rapports de classe, de genre et de race.</p></div>' +
      '<h3>4. Les identifications subjectives et l’individualisation</h3>' +
      '<p>Peu de personnes se disent aujourd’hui « ouvrier » ou « bourgeois » ; beaucoup se rangent dans une vaste « classe moyenne ». Les organisations qui portaient la conscience de classe ont reculé : environ un salarié sur dix est syndiqué en France (Dares, 2019).</p>' +
      '<div data-chain="s1-indiv"></div>' +
      '<div class="aut"><span class="mono">UB</span><span class="an">Ulrich Beck<small>1944-2015</small></span><span class="ad"><i>La Société du risque</i> (1986) : l’individu doit construire lui-même sa trajectoire ; les appartenances collectives, dont la classe, perdent de leur force.</span></div>' +
      '<p>À l’inverse, Michel Pinçon et Monique Pinçon-Charlot voient dans la <b>grande bourgeoisie</b> une classe encore pleinement « en soi et pour soi » : patrimoine transmis, réseaux, entre-soi résidentiel et scolaire, défense collective de ses intérêts.</p>' +
      '<div class="cle"><p><b>Conclusion à retenir :</b> les classes sociales au sens de Marx (conscience et lutte) sont moins visibles ; mais des écarts objectifs durables, cumulatifs et transmis entre générations existent toujours. D’où des positions intermédiaires : « classes sans conscience » (Chauvel), ou analyse multidimensionnelle de l’espace social (Weber, Bourdieu).</p></div>' }
  ],
  pieges: [
    { f: "« Les PCS sont les classes sociales de la France. »", v: "Les PCS sont une nomenclature statistique de l’Insee ; les classes sont un concept sociologique qui suppose des écarts durables, et chez Marx une conscience et un conflit." },
    { f: "« Chez Weber, le statut, c’est le statut d’emploi (salarié ou non). »", v: "Le groupe de statut wébérien désigne le <b>prestige</b> (honneur social) et le style de vie associé." },
    { f: "« La moyennisation signifie que les inégalités ont disparu. »", v: "Elle désigne le gonflement des catégories du milieu et le rapprochement des modes de vie ; les inégalités de revenu et surtout de patrimoine persistent." },
    { f: "« La part des cadres a augmenté de 15 %. »", v: "Elle a augmenté de 15 <b>points</b> (8,0 % → 23,0 %), soit une multiplication par 2,9." },
    { f: "« 38,8 % des employés sont des femmes. »", v: "Faux sens de lecture : 38,8 % des <b>femmes en emploi</b> sont employées. La part des femmes parmi les employés est une autre information (beaucoup plus élevée)." },
    { f: "Ne citer que la PCS et le revenu pour structurer l’espace social.", v: "Le programme en cite sept : PCS, revenu, diplôme, composition du ménage, cycle de vie, sexe, lieu de résidence. Ils se cumulent." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Espace social</b> : ensemble des positions sociales, structuré (groupes) et hiérarchisé (accès inégal aux ressources).</li>' +
    '<li><b>Sept facteurs</b> : PCS, revenu, diplôme, composition du ménage, cycle de vie, sexe, lieu de résidence ; ils se cumulent.</li>' +
    '<li><b>PCS</b> : nomenclature de l’Insee (1954 CSP, 1982, 2003, 2020) ; profession, statut, qualification ; six groupes d’actifs ; PCS Ménage.</li>' +
    '<li><b>Évolutions</b> : salarisation (86,7 %), tertiarisation (76,6 %), qualification (cadres 8,0 % → 23,0 % de 1982 à 2024), féminisation (48,8 % des emplois).</li>' +
    '<li><b>Marx</b> : rapports de production ; bourgeoisie / prolétariat ; exploitation ; classe en soi / pour soi ; lutte des classes ; approche réaliste.</li>' +
    '<li><b>Weber</b> : trois ordres (classes, groupes de statut, partis) ; approche nominaliste ; stratification.</li>' +
    '<li><b>Débats</b> : moyennisation (Mendras, toupie) / retour des classes (Chauvel) ; hétérogénéité intra-classe ; genre (intersectionnalité) ; identification subjective faible ; individualisation (Beck) ; grande bourgeoisie mobilisée (Pinçon et Pinçon-Charlot).</li></ul>' +
    '<h3>Chiffres à citer</h3><ul><li>Niveau de vie 2024 : médiane 26 740 €/an, D9/D1 = 3,48, Gini 0,302, pauvreté 15,4 % (Insee).</li><li>Ouvriers 29,9 % → 18,0 % de l’emploi (1982-2024) ; agriculteurs 7,5 % → 1,3 % (Insee).</li></ul>',
  chainesFiche: ["s1-tert", "s1-qualif", "s1-marx", "s1-indiv"],
  quiz: [
    { q: "Lequel de ces facteurs n’est PAS cité par le programme parmi les facteurs de structuration de l’espace social ?", c: ["La religion", "Le lieu de résidence", "La position dans le cycle de vie", "La composition du ménage"], r: 0, e: "Le programme cite : PCS, revenu, diplôme, composition du ménage, cycle de vie, sexe, lieu de résidence.", s: "s1-1" },
    { q: "En 2024, le rapport interdécile D9/D1 des niveaux de vie est d’environ…", c: ["3,5", "1,5", "10", "35"], r: 0, e: "48 580 € ÷ 13 970 € ≈ 3,48 (Insee Première n° 2117).", s: "s1-1" },
    { q: "La nomenclature des PCS classe les personnes notamment selon…", c: ["leur profession, leur statut et leur qualification", "leur revenu uniquement", "leur conscience de classe", "leur lieu de naissance"], r: 0, e: "Profession, statut (salarié ou non), qualification, taille de l’entreprise, employeur public ou privé.", s: "s1-2" },
    { q: "Entre 1982 et 2024, la part des cadres dans l’emploi est passée de 8,0 % à 23,0 %. Elle a donc…", c: ["augmenté de 15 points de pourcentage", "augmenté de 15 %", "doublé exactement", "augmenté de 23 points"], r: 0, e: "On compare deux pourcentages : l’écart s’exprime en points. En taux de variation, c’est +187,5 %.", s: "s1-3" },
    { q: "En 2024, quelle part des personnes en emploi est salariée ?", c: ["86,7 %", "50 %", "99 %", "65 %"], r: 0, e: "Insee, enquête Emploi 2024 : 86,7 % de salariés, 13,3 % d’indépendants.", s: "s1-3" },
    { q: "La tertiarisation de l’emploi s’explique notamment par…", c: ["les gains de productivité dans l’agriculture et l’industrie et les nouveaux besoins de services", "la baisse des revenus", "la disparition des grandes entreprises", "la hausse du nombre d’agriculteurs"], r: 0, e: "Les gains de productivité libèrent de la main-d’œuvre ; la hausse des revenus crée une demande de services (déversement).", s: "s1-3" },
    { q: "Pour Marx, les classes sociales se définissent d’abord par…", c: ["la place dans les rapports de production", "le prestige social", "le niveau de diplôme", "le lieu de résidence"], r: 0, e: "Propriétaires des moyens de production (bourgeoisie) contre vendeurs de leur force de travail (prolétariat).", s: "s1-4" },
    { q: "Une « classe pour soi », chez Marx, est une classe…", c: ["consciente de ses intérêts et mobilisée", "définie seulement par sa position objective", "qui ne travaille pas", "créée par l’Insee"], r: 0, e: "La classe en soi a une position commune ; la classe pour soi y ajoute la conscience et la lutte.", s: "s1-4" },
    { q: "Chez Weber, les groupes de statut correspondent à…", c: ["l’ordre social : prestige et honneur", "l’ordre économique : revenus", "l’ordre politique : pouvoir", "la propriété des moyens de production"], r: 0, e: "Classes = ordre économique ; groupes de statut = ordre social ; partis = ordre politique.", s: "s1-4" },
    { q: "L’approche de Weber est dite…", c: ["multidimensionnelle et nominaliste", "unidimensionnelle et réaliste", "fondée sur la lutte des classes", "purement statistique"], r: 0, e: "Plusieurs dimensions de la hiérarchie ; les classes sont des catégories construites par l’analyste.", s: "s1-4" },
    { q: "La thèse de la « moyennisation » est associée à…", c: ["Henri Mendras", "Louis Chauvel", "Karl Marx", "Michel Pinçon et Monique Pinçon-Charlot"], r: 0, e: "Mendras (1988) : la société en forme de toupie, avec une large constellation centrale.", s: "s1-5" },
    { q: "Louis Chauvel parle de « classes sans conscience » pour dire que…", c: ["les écarts objectifs persistent mais la conscience de classe s’est affaiblie", "les classes ont disparu", "seule la bourgeoisie existe", "les inégalités ont fortement baissé"], r: 0, e: "C’est un argument pour le maintien des classes en soi, sans classes pour soi.", s: "s1-5" },
    { q: "Quel argument va CONTRE la pertinence des classes sociales aujourd’hui ?", c: ["La multiplication des facteurs d’individualisation", "Le maintien d’inégalités de patrimoine élevées", "L’entre-soi de la grande bourgeoisie", "La hausse des inégalités de niveau de vie depuis 1996"], r: 0, e: "Les trajectoires et identités se diversifient (Beck), ce qui affaiblit le sentiment d’appartenance de classe.", s: "s1-5" }
  ],
  cartes: [
    { r: "Espace social", v: "Ensemble des positions sociales occupées par les individus ; structuré en groupes et hiérarchisé selon l’accès aux ressources." },
    { r: "Les 7 facteurs de structuration", v: "PCS, revenu, diplôme, composition du ménage, position dans le cycle de vie, sexe, lieu de résidence." },
    { r: "PCS", v: "Nomenclature de l’Insee classant la population selon la profession, le statut, la qualification… (CSP 1954, PCS 1982, rénovée 2003 et 2020)." },
    { r: "Salarisation", v: "Hausse de la part des salariés dans l’emploi (86,7 % en 2024)." },
    { r: "Tertiarisation", v: "Hausse de la part des services dans l’emploi (76,6 % en 2024)." },
    { r: "Féminisation des emplois", v: "Hausse de la part des femmes dans l’emploi (48,8 % en 2024), avec des emplois restés genrés." },
    { r: "Classe sociale", v: "Grand groupe partageant une position comparable dans la hiérarchie sociale et, selon les approches, des intérêts et une conscience communs." },
    { r: "Classe en soi / classe pour soi", v: "En soi : position objective commune. Pour soi : conscience de ses intérêts et mobilisation (Marx)." },
    { r: "Rapports de production (Marx)", v: "Relations entre propriétaires des moyens de production (bourgeoisie) et vendeurs de leur force de travail (prolétariat)." },
    { r: "Les trois ordres de Weber", v: "Économique (classes), social (groupes de statut : prestige), politique (partis : pouvoir)." },
    { r: "Stratification sociale", v: "Vision d’une société hiérarchisée en strates graduées, sans conflit nécessaire entre elles (tradition wébérienne)." },
    { r: "Moyennisation", v: "Gonflement des catégories intermédiaires et rapprochement des modes de vie (Mendras, la toupie, 1988)." },
    { r: "Distances inter- / intra-classes", v: "Inter : écarts entre classes. Intra : écarts au sein d’une même classe (hétérogénéité)." },
    { r: "Classes sans conscience", v: "Écarts objectifs durables, mais conscience de classe affaiblie (Chauvel, 2001)." },
    { r: "Individualisation", v: "Les individus construisent davantage leur trajectoire et leur identité, moins déterminées par les appartenances collectives (Beck)." },
    { r: "Intersectionnalité", v: "Croisement des rapports de classe, de genre et de race (Crenshaw, 1989)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site, données Insee", t: "Lire l’évolution des PCS", enonce: '<p>D’après l’Insee, la part des ouvriers dans l’emploi est de 29,9 % en 1982 et de 18,0 % en 2024 ; celle des cadres de 8,0 % et de 23,0 %.</p><ol><li>Calcule l’écart en points pour chaque catégorie.</li><li>Calcule le coefficient multiplicateur de la part des cadres.</li><li>Rédige une phrase de lecture pour 2024.</li></ol>',
      corrige: '<ol><li>Ouvriers : 18,0 − 29,9 = −11,9 points. Cadres : 23,0 − 8,0 = +15,0 points.</li><li>23,0 ÷ 8,0 ≈ 2,9 : la part des cadres a presque triplé.</li><li>« Selon l’Insee, en 2024, en France, 23,0 % des personnes en emploi sont cadres. »</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Distinguez l’analyse des classes sociales de Marx et celle de Weber.", enonce: "<p>3,5 points, sans document.</p>",
      corrige: '<div class="copie"><p>Une classe sociale est un grand groupe d’individus qui occupent une position comparable dans la hiérarchie sociale. Marx et Weber en proposent deux analyses différentes.</p><p>Pour Marx, les classes se définissent par un critère unique : la place dans les rapports de production. La bourgeoisie possède les moyens de production, le prolétariat ne possède que sa force de travail, qu’il vend contre un salaire. La bourgeoisie s’approprie la plus-value : c’est l’exploitation. Les deux classes ont des intérêts opposés et entrent en conflit. Une classe n’existe pleinement que si elle passe de « classe en soi » (position commune) à « classe pour soi » (conscience et mobilisation) : l’approche est réaliste et conflictuelle.</p><p>Weber, au contraire, distingue trois dimensions de la hiérarchie sociale : l’ordre économique, où les classes se définissent par les chances d’accès aux biens et aux revenus ; l’ordre social, où les groupes de statut se définissent par le prestige ; l’ordre politique, où les partis visent le pouvoir. Ces dimensions ne coïncident pas toujours : un enseignant a plus de prestige que de revenu. L’approche est nominaliste : les classes sont des catégories construites par le sociologue, sans conscience ni conflit nécessaires. Elle conduit à une vision en termes de stratification.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, document Insee", t: "Femmes, hommes et catégories socioprofessionnelles", enonce:
      '<p>Document : le graphique « Femmes et hommes en emploi selon la catégorie socioprofessionnelle, 2024 » (Insee) dans <a href="#s1:s1-3">le cours</a>.</p><ol><li>Comparez la part des employés parmi les femmes et parmi les hommes en emploi.</li><li>À l’aide du document et de vos connaissances, montrez que le sexe est un facteur de structuration de l’espace social.</li></ol>',
      corrige: '<ol><li>Selon l’Insee, en France en 2024, 38,8 % des femmes en emploi sont employées, contre 11,6 % des hommes en emploi : la proportion est 3,3 fois plus élevée chez les femmes (27,2 points d’écart).</li><li>Le sexe structure l’espace social car femmes et hommes n’occupent pas les mêmes positions. Le document montre une forte <b>ségrégation professionnelle</b> : les femmes sont concentrées dans les emplois d’employées (38,8 %) et les professions intermédiaires (27,3 %, santé, enseignement, social), les hommes chez les ouvriers (28,2 % contre 7,2 %). Le sexe <b>hiérarchise</b> aussi : les hommes sont plus souvent cadres (25,4 % contre 20,4 %) et chefs d’entreprise. Ces écarts s’expliquent par une socialisation différenciée qui oriente filles et garçons vers des formations et métiers différents, et par la répartition inégale des tâches domestiques, qui pèse sur les carrières féminines (temps partiel, plafond de verre). Il en résulte des écarts de salaire et de pouvoir.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet officiel : bac 2026, jour 2 (France), partie 3 · corrigé du site", officiel: true, t: "Montrez que le revenu et le diplôme ne sont pas les seuls facteurs qui structurent et hiérarchisent l’espace social.", enonce: '<p>Les documents du sujet officiel ne sont pas reproduits ici : appuie-toi sur les données du cours (catégories selon le sexe, niveau de vie, pauvreté des familles monoparentales).</p>',
      corrige: '<p><b>Introduction.</b> L’espace social est l’ensemble des positions sociales, structuré en groupes et hiérarchisé selon l’accès aux ressources. Le revenu et le diplôme y jouent un rôle central, mais d’autres facteurs interviennent : la profession, le sexe, l’âge et la composition du ménage, le lieu de résidence.</p><p><b>I. La profession et le sexe structurent et hiérarchisent.</b> PCS : conditions de travail, prestige, mode de vie (cadres 23,0 % de l’emploi en 2024). Sexe : femmes employées 38,8 % contre 11,6 % des hommes (Insee) ; écarts de salaire, temps partiel.</p><p><b>II. La composition du ménage et le cycle de vie.</b> Familles monoparentales parmi les plus touchées par la pauvreté (Insee, 2024) ; jeunes plus exposés à la précarité ; patrimoine qui s’accumule avec l’âge.</p><p><b>III. Le lieu de résidence.</b> Concentration des ressources dans les métropoles ; quartiers prioritaires contre beaux quartiers ; entre-soi de la grande bourgeoisie (Pinçon et Pinçon-Charlot) ; effet sur la scolarité et les réseaux.</p><p><b>Conclusion.</b> Ces facteurs se cumulent avec le revenu et le diplôme : l’espace social est multidimensionnel.</p><div class="marge"><b>Piège du sujet :</b> ne pas faire une partie sur le revenu et le diplôme ; le sujet demande les <b>autres</b> facteurs.</div>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Les classes sociales permettent-elles encore de rendre compte de la société française actuelle ?", enonce: "<p>Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> La société française a profondément changé depuis les années 1950 (salarisation, tertiarisation, qualification, féminisation). Les classes sociales, définies par Marx ou Weber, décrivent-elles encore une société où les identités semblent plus individuelles, ou faut-il d’autres outils ?</p><p><b>I. Des classes sociales qui restent pertinentes</b><br>A. Des écarts objectifs durables et cumulatifs : niveau de vie (D9/D1 = 3,48 en 2024, Gini au plus haut depuis 1996), patrimoine, diplôme.<br>B. Une reproduction et un entre-soi : grande bourgeoisie « en soi et pour soi » (Pinçon et Pinçon-Charlot) ; classes populaires (42,8 % de l’emploi).<br>C. Des styles de vie qui restent distincts (Bourdieu).</p><p><b>II. Une pertinence remise en cause</b><br>A. Moyennisation (Mendras) et tertiarisation brouillent les frontières.<br>B. Hétérogénéité des classes : ouvriers des services, employés qualifiés ou non.<br>C. Affaiblissement de la conscience de classe et individualisation (Beck ; syndicalisation autour de 10 %).</p><p><b>III. Une analyse à enrichir</b><br>A. Des « classes sans conscience » (Chauvel) : classes en soi sans classes pour soi.<br>B. Articuler classe et genre (intersectionnalité), âge et territoire.<br>C. Une approche multidimensionnelle (Weber, Bourdieu) plutôt qu’une bipolarisation.</p>' }
  ]
};
