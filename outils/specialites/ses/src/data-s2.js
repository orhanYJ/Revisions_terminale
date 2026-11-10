GRAPHES["s2-bac"] = {
  type: "lignes", t: "Proportion de bacheliers dans une génération, 1970-2025",
  s: "En %, tous baccalauréats. Touche le graphique pour lire une année.",
  src: "Source : ministère de l’Éducation nationale, DEPP (série publiée sur data.gouv.fr ; Note d’information n° 26-05). Champ : France hors DROM jusqu’en 2000, puis France hors Mayotte. 2020 et 2021 : épreuves remplacées en partie par le contrôle continu (crise sanitaire). 2024-2025 : données provisoires.",
  unite: " %", pasX: 8, h: 300, min: 0, max: 100,
  x: [1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
  series: [{ n: "Bacheliers dans une génération", c: 2, v: [20.1,21.4,22.2,23.0,23.7,24.2,23.9,24.6,25.3,25.2,25.9,26.0,27.2,28.1,28.6,29.4,31.2,32.6,36.3,39.8,43.5,47.5,51.1,54.7,58.9,62.7,61.3,61.8,62.6,61.6,62.9,61.9,61.6,62.3,60.8,61.1,62.6,62.7,62.3,65.2,65.0,71.2,78.3,74.9,78.6,77.7,78.7,79.6,80.6,79.0,86.7,83.6,80.2,80.7,80.5,80.1] }]
};
GRAPHES["s2-filieres"] = {
  type: "hbarres", t: "Qui étudie où ? Origine sociale des étudiants selon la filière",
  s: "Part des enfants de cadres et d’ouvriers parmi les étudiants, en %, année 2023-2024.",
  src: "Source : Observatoire des inégalités (février 2025), d’après le ministère de l’Éducation nationale et de l’Enseignement supérieur, données 2023-2024. À comparer avec la part des cadres (23,0 %) et des ouvriers (18,0 %) dans l’emploi en 2024 (Insee).",
  unite: " %", lab: 150,
  cats: ["Écoles normales supérieures", "Classes préparatoires (CPGE)", "Université", "Sections de technicien supérieur (BTS)"],
  series: [{ n: "Enfants de cadres", v: [64.9, 53.7, 34.9, 15.9], c: 1 }, { n: "Enfants d’ouvriers", v: [2.0, 6.4, 8.7, 21.6], c: 2 }]
};
GRAPHES["s2-sexe"] = {
  type: "hbarres", t: "Filles et garçons bacheliers en 2025", s: "Proportion de bacheliers dans une génération, en %.",
  src: "Source : DEPP, données provisoires 2025 (data.gouv.fr). Champ : France hors Mayotte.",
  unite: " %", lab: 130,
  cats: ["Tous baccalauréats", "Bac général", "Bac technologique", "Bac professionnel"],
  series: [{ n: "Filles", v: [85.4, 49.9, 16.8, 18.7], c: 2 }, { n: "Garçons", v: [75.1, 37.0, 15.0, 23.1], c: 1 }]
};

CHAINES["s2-massif"] = { t: "Les ressorts de la massification scolaire", e: [
  { f: [{ t: "Politiques publiques : scolarité obligatoire à 16 ans (1959), collège unique (1975), objectif de 80 % d’une génération au niveau du bac (1985), bac professionnel" , k: "cause" }, { t: "Demande des familles : le diplôme protège du chômage et ouvre l’accès aux emplois qualifiés", k: "cause" }] },
  { t: "Besoins de qualification d’une économie tertiarisée", a: "et" },
  { t: "Les scolarités s’allongent", a: "donc" },
  { t: "Les taux d’accès au bac et au supérieur augmentent fortement : massification", k: "effet", a: "donc" }
] };
CHAINES["s2-bourdieu"] = { t: "Capital culturel et reproduction (Bourdieu et Passeron)", e: [
  { t: "Les familles favorisées transmettent un capital culturel : langage, pratiques culturelles, connaissance du système scolaire", k: "cause" },
  { t: "L’École attend et évalue justement ces savoirs et ces manières d’être", a: "or" },
  { t: "Les « héritiers » réussissent mieux ; les autres échouent plus souvent", a: "donc" },
  { t: "La réussite paraît due au seul mérite, ce qui la rend légitime (violence symbolique)", a: "et" },
  { t: "L’École contribue à la reproduction sociale", k: "effet", a: "donc" }
] };
CHAINES["s2-boudon"] = { t: "Stratégies des familles et inégalités (Boudon)", e: [
  { t: "À chaque palier d’orientation, la famille compare coûts, avantages et risques d’une poursuite d’études", k: "cause" },
  { t: "Ce calcul dépend de la position sociale : des études longues coûtent relativement plus et rapportent relativement moins aux milieux populaires", a: "or" },
  { t: "À résultats scolaires égaux, les enfants de milieu populaire choisissent plus souvent des études courtes", a: "donc" },
  { t: "Les écarts s’additionnent palier après palier (effet d’agrégation)", a: "donc" },
  { t: "Inégalités d’accès aux diplômes, sans que personne ne le veuille", k: "effet", a: "donc" }
] };
CHAINES["s2-genre"] = { t: "Socialisation de genre et parcours scolaires", e: [
  { t: "Socialisation différenciée des filles et des garçons : jouets, attentes, stéréotypes, modèles", k: "cause" },
  { f: [{ t: "Les filles s’ajustent mieux aux attentes scolaires : elles réussissent mieux", k: "effet" }, { t: "Elles se sentent moins légitimes en sciences et anticipent davantage leurs futurs rôles familiaux", k: "frein" }], a: "donc" },
  { t: "Elles sont plus nombreuses à décrocher le bac, mais moins nombreuses dans les filières d’ingénieurs et de numérique, souvent les plus rémunératrices", k: "effet", a: "donc" }
] };

CH.s2 = {
  horsEcrit: "elle est indispensable pour comprendre la mobilité sociale (question évaluable), elle nourrit les copies sur la structure sociale et peut servir au Grand oral",
  chapo: "En 1970, un jeune sur cinq obtenait le bac ; en 2025, quatre sur cinq. L’École s’est ouverte à tous. Mais les enfants de cadres restent plus de huit fois plus nombreux que les enfants d’ouvriers en classes préparatoires. Ce chapitre explique ce que fait l’École, ce qui a changé, et pourquoi la réussite reste inégale.",
  essentiel: [
    "Dans une société démocratique, l’École <b>transmet des savoirs</b>, socialise et vise à favoriser l’<b>égalité des chances</b> : la position sociale doit dépendre du mérite et non de l’origine.",
    "Depuis les années 1950, l’accès à l’école s’est massivement ouvert : 20,1 % d’une génération obtient le bac en 1970, 80,1 % en 2025 (DEPP). C’est la <b>massification</b>.",
    "La massification n’est pas une pleine <b>démocratisation</b> : les écarts selon l’origine sociale se sont déplacés vers les filières et les diplômes (démocratisation <b>ségrégative</b>, Merle) : 53,7 % d’enfants de cadres en classes préparatoires, 6,4 % d’enfants d’ouvriers.",
    "Les inégalités de réussite ont de <b>multiples facteurs</b> : le rôle de l’École elle-même, le <b>capital culturel</b> (Bourdieu et Passeron) et les <b>investissements familiaux</b>, la <b>socialisation selon le genre</b>, les <b>stratégies des ménages</b> (Boudon).",
    "Ces facteurs se combinent dans des <b>trajectoires individuelles</b> : il existe des réussites « paradoxales » (Lahire) et rien n’est automatique."
  ],
  chiffres: [
    { n: "× 4", l: "la proportion de bacheliers dans une génération entre 1970 (20,1 %) et 2025 (80,1 %).", s: "DEPP, Note d’information n° 26-05" },
    { n: "113", l: "points d’écart en mathématiques entre élèves favorisés et défavorisés en France (PISA 2022), contre 93 en moyenne dans l’OCDE.", s: "OCDE, PISA 2022, note pays France" },
    { n: "53,7 %", l: "des élèves de classes préparatoires sont enfants de cadres, contre 6,4 % enfants d’ouvriers (2023-2024).", s: "Observatoire des inégalités, d’après le ministère" }
  ],
  objectifs: [
    { bo: "Comprendre que, dans les sociétés démocratiques, l’École transmet des savoirs et vise à favoriser l’égalité des chances ; comprendre l’évolution, depuis les années 1950, des principaux indicateurs mesurant l’accès à l’école et à l’enseignement supérieur (taux de scolarisation, taux d’accès à un diplôme ou à un type de formation) en distinguant les processus de massification et de démocratisation.", clair: "Connaître les missions de l’École, savoir lire les indicateurs d’accès et distinguer massification et démocratisation.", voir: "s2-1" },
    { bo: "Comprendre la multiplicité des facteurs d’inégalités de réussite scolaire (notamment, rôle de l’École, rôle du capital culturel et des investissements familiaux, socialisation selon le genre, effets des stratégies des ménages) dans la construction des trajectoires individuelles de formation.", clair: "Expliquer les quatre familles de facteurs des inégalités de réussite et savoir les combiner.", voir: "s2-4" }
  ],
  notions: ["École", "socialisation", "égalité des chances", "méritocratie", "taux de scolarisation", "taux d’accès à un diplôme", "massification", "démocratisation (quantitative, qualitative, ségrégative)", "inégalités de réussite scolaire", "capital culturel", "investissements familiaux", "socialisation selon le genre", "stratégies des ménages", "reproduction sociale", "trajectoire individuelle"],
  sections: [
    { id: "s2-1", t: "Ce que fait l’École dans une société démocratique", h:
      '<p class="lede">L’École n’est pas qu’un lieu d’apprentissage : c’est une institution qui façonne les individus et la société.</p>' +
      '<ul><li><b>Transmettre des savoirs</b> : lire, écrire, compter, raisonner, et des connaissances générales et professionnelles.</li><li><b>Socialiser</b> : transmettre les normes et les valeurs communes, former des citoyens. Pour Émile Durkheim, l’éducation est une « socialisation méthodique de la jeune génération » (<i>Éducation et sociologie</i>, 1922).</li><li><b>Qualifier et certifier</b> : délivrer des diplômes reconnus sur le marché du travail.</li><li><b>Favoriser l’égalité des chances</b> : dans une société démocratique, les positions sociales doivent être attribuées selon le <b>mérite</b> (le travail, les talents) et non selon la naissance. C’est l’idéal <b>méritocratique</b>.</li></ul>' +
      '<div class="def"><b>Égalité des chances</b> — situation où chacun, quelle que soit son origine, a la même probabilité d’accéder aux différentes positions sociales. À distinguer de l’égalité des <b>droits</b> (mêmes règles pour tous) et de l’égalité des <b>situations</b> (mêmes résultats).</div>' +
      '<div class="ex"><p>Quelques jalons : lois Ferry de 1881 (gratuité de l’école primaire publique) et de 1882 (instruction obligatoire de 6 à 13 ans, laïcité) ; scolarité obligatoire portée à 16 ans par la réforme Berthoin (1959) ; collège unique (réforme Haby, 1975) ; instruction obligatoire dès 3 ans et obligation de formation de 16 à 18 ans (loi de 2019, appliquée à partir de 2020 pour la formation).</p></div>' },

    { id: "s2-2", t: "Mesurer l’accès à l’École : la massification", h:
      '<div class="def"><b>Taux de scolarisation</b> — part des jeunes d’un âge donné qui sont scolarisés. <b>Taux d’accès à un diplôme</b> (ou à une formation) — part d’une génération qui obtient ce diplôme (ou entre dans cette formation).</div>' +
      '<div data-graph="s2-bac"></div>' +
      '<p>La proportion de bacheliers dans une génération passe de 20,1 % en 1970 à 62,7 % en 1995, puis à 80,1 % en 2025 (DEPP) : elle a gagné 60 points. La hausse est spectaculaire entre 1985 et 1995, après l’objectif fixé en 1985 de mener 80 % d’une génération au niveau du baccalauréat et la création du <b>bac professionnel</b> (premiers diplômés en 1987). Après un palier autour de 62 % de 1995 à 2008, elle repart avec la réforme de la voie professionnelle (bac pro en trois ans, à partir de 2009).</p>' +
      '<div class="def"><b>Massification scolaire</b> — forte hausse du nombre d’élèves et d’étudiants et de l’accès aux niveaux élevés d’enseignement.</div>' +
      '<div data-chain="s2-massif"></div>' +
      '<div class="attn"><p>Taux d’accès et taux de réussite sont différents : le taux de réussite au bac (part des candidats qui l’obtiennent) est bien plus élevé que la proportion de bacheliers dans une génération (part de <b>tous</b> les jeunes du même âge, y compris ceux qui ne se présentent pas).</p></div>' },

    { id: "s2-3", t: "Massification n’est pas démocratisation", h:
      '<div class="def"><b>Démocratisation scolaire</b> — réduction des inégalités d’accès aux diplômes et aux filières selon l’origine sociale. Antoine Prost distingue démocratisation <b>quantitative</b> (tout le monde accède plus loin : c’est la massification) et <b>qualitative</b> (les chances d’accès se rapprochent entre milieux sociaux).</div>' +
      '<p>Les inégalités d’accès au bac se sont réduites : selon la DEPP (2020), l’écart d’accès au bac entre enfants de cadres et enfants d’ouvriers non qualifiés passe de 28 points pour les élèves entrés en sixième en 1995 à 15 points pour ceux entrés en 2007. Mais les écarts se sont <b>déplacés</b> vers les filières.</p>' +
      '<div class="aut"><span class="mono">PM</span><span class="an">Pierre Merle<small>sociologue</small></span><span class="ad">Distingue la démocratisation <b>égalisatrice</b> (les écarts se réduisent), <b>uniforme</b> (tous progressent, écarts stables) et <b>ségrégative</b> (l’accès s’ouvre, mais les enfants des milieux populaires sont orientés vers les filières les moins valorisées).</span></div>' +
      '<div data-anim="s2-mass"></div>' +
      '<div data-graph="s2-filieres"></div>' +
      '<p>En 2023-2024, les enfants de cadres représentent 53,7 % des élèves de classes préparatoires et 64,9 % des élèves des écoles normales supérieures, alors que les cadres représentent 23,0 % des personnes en emploi en 2024. Les enfants d’ouvriers sont 6,4 % en classes préparatoires, mais 21,6 % en sections de technicien supérieur. À l’université, la part des enfants de cadres (34,9 %) est la même qu’en 2009 (Observatoire des inégalités). Le bac s’est ouvert, mais les filières restent hiérarchisées socialement : c’est une démocratisation <b>ségrégative</b>.</p>' +
      '<div class="attn"><p>Comparer la part des enfants de cadres en CPGE à la part des cadres dans l’emploi donne un <b>ordre de grandeur</b> de la surreprésentation, pas une mesure exacte : la population de référence (les parents de jeunes de 20 ans) n’est pas exactement celle des personnes en emploi.</p></div>' },

    { id: "s2-4", t: "Les facteurs d’inégalités de réussite : École et familles", h:
      '<p class="lede">Les inégalités de réussite scolaire selon l’origine sociale sont précoces et cumulatives. En France, l’écart de score en mathématiques entre élèves favorisés et défavorisés (quart supérieur et quart inférieur de l’indice socio-économique) atteint 113 points dans l’enquête PISA 2022, contre 93 en moyenne dans l’OCDE.</p>' +
      '<h3>1. Le rôle de l’École elle-même</h3>' +
      '<p>L’École n’est pas neutre :</p><ul><li><b>Effet établissement et ségrégation scolaire</b> : les élèves de milieux populaires sont concentrés dans certains établissements, où les enseignants sont souvent plus jeunes et changent plus souvent.</li><li><b>Attentes des enseignants</b> : l’« effet Pygmalion » (Rosenthal et Jacobson, 1968) montre que les attentes d’un enseignant envers un élève influencent ses progrès.</li><li><b>Orientation</b> : selon la DEPP, à résultats comparables en fin de troisième (moyenne entre 10 et 12), 91 % des enfants de cadres demandent une seconde générale et technologique, contre 59 % des enfants d’ouvriers non qualifiés.</li><li>Les savoirs et les codes valorisés (implicites, aisance à l’oral) sont plus proches de la culture des familles favorisées.</li></ul>' +
      '<h3>2. Le capital culturel</h3>' +
      '<div class="def"><b>Capital culturel</b> — ensemble des ressources culturelles d’un individu : connaissances, langage, goûts, diplômes, biens culturels. Pour Bourdieu, il existe à l’état <b>incorporé</b> (savoirs, manières de parler), <b>objectivé</b> (livres, instruments) et <b>institutionnalisé</b> (diplômes).</div>' +
      '<div class="aut"><span class="mono">BP</span><span class="an">Pierre Bourdieu et Jean-Claude Passeron<small><i>Les Héritiers</i>, 1964 ; <i>La Reproduction</i>, 1970</small></span><span class="ad">L’École évalue des compétences que certains élèves ont reçues dans leur famille. Ces « héritiers » réussissent, et leur réussite passe pour du talent : l’École légitime ainsi la reproduction des positions sociales.</span></div>' +
      '<div data-chain="s2-bourdieu"></div>' +
      '<h3>3. Les investissements familiaux</h3>' +
      '<p>Au-delà de ce qui se transmet sans y penser, les familles <b>investissent</b> : temps passé à aider aux devoirs, cours particuliers, activités culturelles et sportives, séjours linguistiques, connaissance des filières et de Parcoursup. Ces investissements demandent du temps, de l’argent et de l’information, inégalement répartis.</p>' +
      '<div class="aut"><span class="mono">BL</span><span class="an">Bernard Lahire<small><i>Tableaux de familles</i>, 1995</small></span><span class="ad">En étudiant des familles populaires, il montre que la transmission n’est jamais automatique : des <b>configurations familiales</b> (régularité, autorité, place de l’écrit, attention portée à la scolarité) expliquent des <b>réussites « paradoxales »</b> et, à l’inverse, des échecs en milieu favorisé.</span></div>' },

    { id: "s2-5", t: "Genre et stratégies des ménages", h:
      '<h3>4. La socialisation selon le genre</h3>' +
      '<div data-graph="s2-sexe"></div>' +
      '<p>En 2025, 85,4 % des filles d’une génération obtiennent le bac, contre 75,1 % des garçons ; l’écart est encore plus net pour le bac général (49,9 % contre 37,0 %), tandis que les garçons sont plus nombreux en bac professionnel (DEPP). Pourtant, les filles restent minoritaires dans les formations d’ingénieurs, le numérique et les classes préparatoires scientifiques.</p>' +
      '<div class="aut"><span class="mono">BE</span><span class="an">Christian Baudelot et Roger Establet<small><i>Allez les filles !</i>, 1992</small></span><span class="ad">Les filles ont dépassé les garçons dans la réussite scolaire, mais leurs choix d’orientation restent moins tournés vers les filières scientifiques et les plus rentables.</span></div>' +
      '<div data-chain="s2-genre"></div>' +
      '<p>Marie Duru-Bellat (<i>L’École des filles</i>, 1990) explique ces choix par une socialisation différenciée et par l’anticipation des rôles futurs. L’École participe aussi, souvent sans le vouloir, à ces écarts (attentes, conseils d’orientation, manuels).</p>' +
      '<h3>5. Les stratégies des ménages</h3>' +
      '<div class="aut"><span class="mono">RB</span><span class="an">Raymond Boudon<small><i>L’Inégalité des chances</i>, 1973</small></span><span class="ad">Approche par l’<b>individualisme méthodologique</b> : les inégalités résultent de l’agrégation de choix rationnels de familles qui, à chaque palier, comparent coûts, avantages et risques selon leur position sociale.</span></div>' +
      '<div data-chain="s2-boudon"></div>' +
      '<p>Les familles les mieux informées développent aussi des <b>stratégies</b> : choix de l’établissement (privé, contournement de la carte scolaire), options rares, classes à horaires aménagés. Agnès van Zanten (<i>Choisir son école</i>, 2009) montre que ces stratégies des classes moyennes et supérieures renforcent la ségrégation entre établissements. Une note de la DEPP montre de même que le choix du latin au collège est lié à l’origine sociale.</p>' +
      '<div class="cle"><p><b>À retenir :</b> aucun facteur n’explique seul les inégalités. Ils se cumulent et se combinent dans des <b>trajectoires individuelles</b> : un même capital culturel, des stratégies différentes, une configuration familiale particulière ou un enseignant décisif peuvent produire des parcours très différents.</p></div>' }
  ],
  pieges: [
    { f: "« La massification a démocratisé l’École. »", v: "La massification (plus d’élèves plus loin) ne garantit pas la démocratisation (réduction des écarts selon l’origine). Les inégalités se sont déplacées vers les filières : démocratisation ségrégative." },
    { f: "« La proportion de bacheliers a augmenté de 60 %. »", v: "Elle a gagné 60 <b>points</b> (20,1 % → 80,1 %) ; elle a été multipliée par 4 environ." },
    { f: "« Pour Bourdieu, les enfants de milieu populaire sont moins doués. »", v: "C’est l’inverse : Bourdieu critique l’« idéologie du don ». La réussite vient d’un capital culturel hérité que l’École valorise." },
    { f: "« Pour Boudon, les familles populaires ne veulent pas la réussite de leurs enfants. »", v: "Elles font des choix rationnels compte tenu de leur position : coûts et risques plus élevés, bénéfices relatifs plus faibles." },
    { f: "Confondre taux de réussite au bac et proportion de bacheliers dans une génération.", v: "Le taux de réussite rapporte les admis aux candidats ; la proportion dans une génération rapporte les bacheliers à tous les jeunes de cet âge." },
    { f: "« Les filles réussissent mieux, donc l’École ne produit pas d’inégalités de genre. »", v: "Elles réussissent mieux mais s’orientent moins vers les filières sélectives scientifiques, souvent les plus rémunératrices." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Fonctions de l’École</b> : transmettre des savoirs, socialiser (Durkheim), qualifier, favoriser l’égalité des chances (méritocratie).</li>' +
    '<li><b>Taux de scolarisation</b> ; <b>taux d’accès à un diplôme</b> (proportion de bacheliers dans une génération : 20,1 % en 1970, 62,7 % en 1995, 80,1 % en 2025).</li>' +
    '<li><b>Massification</b> : hausse du nombre d’élèves et de l’accès. <b>Démocratisation</b> : réduction des écarts selon l’origine ; quantitative / qualitative (Prost) ; égalisatrice, uniforme, <b>ségrégative</b> (Merle).</li>' +
    '<li><b>Rôle de l’École</b> : ségrégation, attentes (effet Pygmalion), orientation, codes implicites.</li>' +
    '<li><b>Capital culturel</b> (incorporé, objectivé, institutionnalisé) ; héritiers et reproduction (Bourdieu et Passeron, 1964 et 1970).</li>' +
    '<li><b>Investissements familiaux</b> ; configurations familiales et réussites paradoxales (Lahire, 1995).</li>' +
    '<li><b>Socialisation de genre</b> : filles meilleures au bac, moins en sciences (Baudelot et Establet ; Duru-Bellat).</li>' +
    '<li><b>Stratégies des ménages</b> : coûts / avantages / risques, effet d’agrégation (Boudon, 1973) ; choix d’établissement (van Zanten).</li></ul>' +
    '<h3>Chiffres à citer</h3><ul><li>CPGE 2023-2024 : 53,7 % d’enfants de cadres, 6,4 % d’enfants d’ouvriers (Observatoire des inégalités, d’après le ministère).</li><li>PISA 2022 : 113 points d’écart favorisés / défavorisés en maths (OCDE : 93).</li><li>Bac 2025 : filles 85,4 %, garçons 75,1 % d’une génération (DEPP).</li></ul>',
  chainesFiche: ["s2-massif", "s2-bourdieu", "s2-boudon", "s2-genre"],
  quiz: [
    { q: "Pour Durkheim, l’éducation est…", c: ["une socialisation méthodique de la jeune génération", "un moyen de sélectionner les plus doués", "un investissement en capital humain", "un instrument de domination"], r: 0, e: "Elle transmet les normes et valeurs communes qui font tenir la société.", s: "s2-1" },
    { q: "L’égalité des chances signifie que…", c: ["chacun a la même probabilité d’accéder aux positions sociales, quelle que soit son origine", "tout le monde a le même revenu", "tout le monde a le même diplôme", "les mêmes règles s’appliquent à tous"], r: 0, e: "Les mêmes règles pour tous, c’est l’égalité des droits ; les mêmes résultats, l’égalité des situations.", s: "s2-1" },
    { q: "Entre 1970 et 2025, la proportion de bacheliers dans une génération est passée d’environ…", c: ["20 % à 80 %", "50 % à 80 %", "5 % à 50 %", "40 % à 95 %"], r: 0, e: "20,1 % en 1970, 80,1 % en 2025 (DEPP) : 60 points de plus, une multiplication par 4.", s: "s2-2" },
    { q: "La massification scolaire désigne…", c: ["la forte hausse du nombre d’élèves et de l’accès aux niveaux élevés d’enseignement", "la réduction des inégalités d’accès selon l’origine sociale", "la création du collège unique", "la baisse du niveau des élèves"], r: 0, e: "La massification est quantitative ; la démocratisation concerne l’égalité entre milieux sociaux.", s: "s2-2" },
    { q: "Le bac professionnel a été créé…", c: ["en 1985", "en 1959", "en 2009", "en 1975"], r: 0, e: "Créé en 1985, premiers diplômés en 1987 ; il a beaucoup contribué à la massification.", s: "s2-2" },
    { q: "Une démocratisation « ségrégative » (Merle) signifie que…", c: ["l’accès s’ouvre mais les milieux populaires sont orientés vers les filières les moins valorisées", "les écarts entre milieux sociaux disparaissent", "les écoles sont séparées par sexe", "seuls les enfants de cadres progressent"], r: 0, e: "Exemple : enfants d’ouvriers 21,6 % en BTS mais 6,4 % en classes préparatoires (2023-2024).", s: "s2-3" },
    { q: "En 2023-2024, quelle part des élèves de classes préparatoires sont enfants de cadres ?", c: ["Environ 54 %", "Environ 23 %", "Environ 10 %", "Environ 80 %"], r: 0, e: "53,7 % (Observatoire des inégalités, d’après le ministère), alors que les cadres sont 23,0 % de l’emploi.", s: "s2-3" },
    { q: "Dans PISA 2022, l’écart en mathématiques entre élèves favorisés et défavorisés en France est…", c: ["supérieur à la moyenne de l’OCDE (113 points contre 93)", "inférieur à la moyenne de l’OCDE", "nul", "égal à la moyenne de l’OCDE"], r: 0, e: "La France fait partie des pays où l’origine sociale pèse le plus sur les résultats.", s: "s2-4" },
    { q: "Le capital culturel à l’état « institutionnalisé » correspond…", c: ["aux diplômes", "aux livres et instruments de musique", "aux manières de parler", "au réseau de relations"], r: 0, e: "Incorporé = savoirs et dispositions ; objectivé = biens culturels ; institutionnalisé = titres scolaires.", s: "s2-4" },
    { q: "Pour Bourdieu et Passeron, l’École contribue à la reproduction sociale parce qu’elle…", c: ["valorise une culture proche de celle des classes favorisées et fait passer la réussite pour du mérite", "est payante", "interdit l’accès aux enfants d’ouvriers", "n’enseigne que des savoirs techniques"], r: 0, e: "C’est la violence symbolique : une domination qui paraît légitime.", s: "s2-4" },
    { q: "Bernard Lahire explique les « réussites paradoxales » en milieu populaire par…", c: ["des configurations familiales favorables", "le hasard", "les dons naturels", "les cours particuliers payants"], r: 0, e: "Régularité, autorité, rapport à l’écrit : la transmission culturelle n’est pas automatique.", s: "s2-4" },
    { q: "Pour Raymond Boudon, les inégalités scolaires s’expliquent surtout par…", c: ["des choix rationnels des familles, qui dépendent de leur position sociale", "le capital culturel transmis", "la discrimination des enseignants", "les différences de dons"], r: 0, e: "Coûts, avantages et risques sont évalués différemment selon le milieu ; les choix s’agrègent.", s: "s2-5" },
    { q: "En 2025, la proportion de bacheliers est…", c: ["plus élevée chez les filles (85,4 %) que chez les garçons (75,1 %)", "plus élevée chez les garçons", "identique pour les deux sexes", "plus élevée chez les garçons en bac général"], r: 0, e: "Mais les garçons sont plus nombreux en bac professionnel (23,1 % contre 18,7 %), et les filles restent minoritaires dans les formations d’ingénieurs.", s: "s2-5" }
  ],
  cartes: [
    { r: "Fonctions de l’École", v: "Transmettre des savoirs, socialiser, qualifier et certifier, favoriser l’égalité des chances." },
    { r: "Socialisation méthodique", v: "Définition de l’éducation par Durkheim : transmission organisée des normes et valeurs à la jeune génération." },
    { r: "Égalité des chances", v: "Même probabilité pour tous d’accéder aux positions sociales, quelle que soit l’origine." },
    { r: "Méritocratie", v: "Organisation sociale où les positions sont attribuées selon le mérite (travail, talents) et non la naissance." },
    { r: "Taux d’accès à un diplôme", v: "Part d’une génération qui obtient ce diplôme (bac : 80,1 % en 2025)." },
    { r: "Massification scolaire", v: "Forte hausse du nombre d’élèves et de l’accès aux niveaux élevés d’enseignement." },
    { r: "Démocratisation scolaire", v: "Réduction des inégalités d’accès aux diplômes et filières selon l’origine sociale." },
    { r: "Démocratisation ségrégative", v: "L’accès s’ouvre, mais les milieux populaires vont vers les filières les moins valorisées (Merle)." },
    { r: "Capital culturel", v: "Ressources culturelles (savoirs, langage, goûts, biens, diplômes) ; incorporé, objectivé, institutionnalisé (Bourdieu)." },
    { r: "Les Héritiers", v: "Bourdieu et Passeron, 1964 : les étudiants issus de milieux favorisés héritent d’un capital culturel valorisé par l’École." },
    { r: "Réussites paradoxales", v: "Réussites scolaires en milieu populaire expliquées par des configurations familiales (Lahire, 1995)." },
    { r: "Stratégies des ménages (Boudon)", v: "Choix d’orientation fondés sur coûts, avantages et risques, qui varient selon la position sociale ; effet d’agrégation (1973)." },
    { r: "Effet Pygmalion", v: "Les attentes de l’enseignant influencent les résultats de l’élève (Rosenthal et Jacobson, 1968)." },
    { r: "Socialisation selon le genre", v: "Transmission de normes différentes aux filles et aux garçons, qui oriente leurs choix scolaires (Baudelot et Establet ; Duru-Bellat)." },
    { r: "Collège unique", v: "Réforme Haby (1975) : tous les élèves suivent le même collège." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site, données DEPP", t: "Mesurer la massification", enonce: '<p>Proportion de bacheliers dans une génération (DEPP) : 1970 : 20,1 % ; 1985 : 29,4 % ; 1995 : 62,7 % ; 2025 : 80,1 %.</p><ol><li>Calcule l’indice de 2025, base 100 en 1970.</li><li>Compare les hausses de 1970-1985 et de 1985-1995 en points.</li><li>Pourquoi ces chiffres ne suffisent-ils pas à conclure à une démocratisation ?</li></ol>',
      corrige: '<ol><li>80,1 ÷ 20,1 × 100 ≈ 398,5 : la proportion a presque quadruplé.</li><li>1970-1985 : +9,3 points en 15 ans ; 1985-1995 : +33,3 points en 10 ans. La massification s’accélère fortement après 1985 (objectif de 80 % au niveau du bac, bac professionnel).</li><li>Ils mesurent l’accès de l’ensemble d’une génération (massification), pas les écarts entre milieux sociaux ni la répartition dans les filières. Il faudrait comparer les taux d’accès des enfants de cadres et d’ouvriers, et leur présence dans les filières sélectives.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que la massification scolaire ne s’est pas accompagnée d’une démocratisation complète.", enonce: "<p>3,5 points, sans document. Rappel : cette question n’est pas évaluée à l’écrit en 2027 ; l’exercice entraîne la méthode.</p>",
      corrige: '<div class="copie"><p>La massification scolaire est la forte hausse de l’accès aux niveaux élevés d’enseignement : la proportion de bacheliers dans une génération passe de 20,1 % en 1970 à 80,1 % en 2025 selon la DEPP. La démocratisation est la réduction des inégalités d’accès selon l’origine sociale. La première n’a entraîné la seconde que partiellement.</p><p>D’abord, les écarts d’accès au bac se sont réduits mais n’ont pas disparu : selon la DEPP, l’écart entre enfants de cadres et d’ouvriers non qualifiés atteint encore 15 points pour les élèves entrés en sixième en 2007.</p><p>Surtout, les inégalités se sont déplacées vers les filières : c’est la démocratisation ségrégative décrite par Pierre Merle. Les enfants de milieux populaires accèdent davantage au bac, mais plus souvent au bac professionnel et aux formations courtes, tandis que les enfants de cadres dominent les filières sélectives. En 2023-2024, ils représentent 53,7 % des élèves de classes préparatoires, contre 6,4 % pour les enfants d’ouvriers, qui sont en revanche 21,6 % en sections de technicien supérieur (Observatoire des inégalités, d’après le ministère). Ces écarts s’expliquent notamment par le capital culturel et par les stratégies d’orientation des familles.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, données ministère / Observatoire des inégalités", t: "Origine sociale et filières du supérieur", enonce: '<p>Document : le graphique « Qui étudie où ? » dans <a href="#s2:s2-3">le cours</a>.</p><ol><li>Comparez la part des enfants de cadres et d’ouvriers en classes préparatoires.</li><li>À l’aide du document et de vos connaissances, montrez que l’origine sociale influence les trajectoires de formation.</li></ol>',
      corrige: '<ol><li>Selon le ministère (repris par l’Observatoire des inégalités), en 2023-2024, 53,7 % des élèves de classes préparatoires sont enfants de cadres contre 6,4 % enfants d’ouvriers : environ 8,4 fois plus.</li><li>Le document montre une forte hiérarchie sociale des filières : plus une filière est sélective et prestigieuse, plus les enfants de cadres y sont nombreux (64,9 % en ENS) et les enfants d’ouvriers rares (2,0 %) ; à l’inverse, les enfants d’ouvriers sont mieux représentés en BTS (21,6 %), filière courte et professionnelle. Deux mécanismes l’expliquent. Le capital culturel transmis par les familles favorisées (Bourdieu et Passeron) facilite la réussite dans un système qui valorise leurs savoirs et leurs codes. Et les stratégies des familles (Boudon) : à résultats égaux, les familles populaires évaluent plus fortement les coûts et les risques d’études longues et choisissent plus souvent des formations courtes, ce que confirme la DEPP sur les vœux d’orientation en fin de troisième.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet inventé pour le site", t: "À l’aide du dossier, montrez que la famille joue un rôle dans les inégalités de réussite scolaire.", enonce: '<p><b>Document 1</b> : PISA 2022, écart de 113 points en mathématiques entre élèves favorisés et défavorisés en France (OCDE : 93). <b>Document 2</b> : vœux d’orientation en fin de troisième, à moyenne de 10 à 12 : 91 % des enfants de cadres demandent une seconde générale et technologique contre 59 % des enfants d’ouvriers non qualifiés (DEPP). <b>Document 3</b> : graphique « Qui étudie où ? ».</p>',
      corrige: '<p><b>Introduction.</b> Les inégalités de réussite scolaire sont les écarts de résultats et de parcours entre élèves. La famille y contribue par ce qu’elle transmet, par ce qu’elle investit et par les choix qu’elle fait.</p><p><b>I. La famille transmet un capital culturel.</b> Langage, rapport à la lecture, connaissance des attentes scolaires (Bourdieu et Passeron). Document 1 : 113 points d’écart en mathématiques dès 15 ans.</p><p><b>II. La famille investit dans la scolarité.</b> Temps, aide aux devoirs, cours particuliers, activités ; configurations familiales (Lahire), qui expliquent aussi des réussites paradoxales.</p><p><b>III. La famille fait des choix d’orientation.</b> Coûts, avantages et risques selon la position sociale (Boudon). Document 2 : 91 % contre 59 % à résultats égaux. Document 3 : aboutissement de ces choix dans le supérieur (53,7 % contre 6,4 % en CPGE).</p><p><b>Conclusion.</b> La famille pèse par la transmission, l’investissement et la stratégie ; ces effets s’ajoutent au rôle de l’École elle-même.</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Comment expliquer les inégalités de réussite scolaire selon le milieu social ?", enonce: "<p>« Comment expliquer » appelle un plan explicatif (pas un oui / non).</p>",
      corrige: '<p><b>Problématique.</b> Malgré la massification, la réussite scolaire reste fortement liée à l’origine sociale. Ces inégalités tiennent-elles d’abord à ce que les familles transmettent, aux choix qu’elles font, ou au fonctionnement de l’École elle-même ?</p><p><b>I. Des inégalités héritées : le capital culturel et les investissements familiaux</b><br>A. Le capital culturel et la reproduction (Bourdieu et Passeron) ; PISA 2022.<br>B. Les investissements familiaux (temps, argent, information).<br>C. Des transmissions non mécaniques : configurations familiales (Lahire).</p><p><b>II. Des inégalités construites par les choix des familles</b><br>A. Le calcul coûts / avantages / risques et l’effet d’agrégation (Boudon) ; vœux en fin de troisième (DEPP).<br>B. Les stratégies d’établissement et d’options (van Zanten).<br>C. Le résultat : une démocratisation ségrégative (Merle) ; CPGE.</p><p><b>III. Des inégalités renforcées par l’École et croisées avec le genre</b><br>A. Ségrégation scolaire, attentes des enseignants (effet Pygmalion), orientation.<br>B. Les codes implicites valorisés par l’institution.<br>C. Le genre croise l’origine sociale : filles meilleures au bac, moins présentes en sciences (Baudelot et Establet).</p>' }
  ]
};
