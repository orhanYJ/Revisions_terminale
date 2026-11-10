GRAPHES["s3-mob"] = {
  type: "lignes", t: "La mobilité sociale observée en France, 1977-2015", spark: 0,
  s: "En % des personnes de 35 à 59 ans en emploi ou anciennement en emploi. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.",
  src: "Source : Insee, enquêtes Formation et qualification professionnelle (FQP) 1977 à 2014-2015 ; Insee Première n° 1739, février 2019. Champ : France métropolitaine, Français de 35 à 59 ans actifs occupés ou anciens actifs occupés. La FQP 2014-2015 est la dernière enquête publiée.",
  unite: " %", pasX: 1, h: 300, min: 0, max: 70,
  x: [1977, 1985, 1993, 2003, 2015],
  series: [
    { n: "Mobilité observée des hommes (par rapport au père)", c: 1, v: [63.8, 66.2, 67.4, 66.4, 65.2] },
    { n: "Mobilité ascendante des hommes", c: 2, v: [23.5, 26.6, 30.3, 30.8, 27.6] },
    { n: "Mobilité descendante des hommes", c: 3, v: [7.2, 7.7, 9.7, 10.9, 15.0] },
    { n: "Mobilité ascendante des femmes (par rapport à la mère)", c: 4, v: [16.8, 24.6, 30.8, 35.2, 39.8] }
  ]
};
GRAPHES["s3-dest"] = {
  type: "hbarres", t: "Que deviennent les fils ? Deux origines comparées, 2015",
  s: "Position des fils de 35 à 59 ans selon la catégorie de leur père, en %. Chaque série totalise 100 %.",
  src: "Source : Insee, enquête FQP 2014-2015 (Insee Première n° 1739, figure 2). Catégories regroupées par l’Insee : les employés et les ouvriers sont classés ensemble selon leur qualification.",
  unite: " %", lab: 150,
  cats: ["Agriculteurs exploitants", "Artisans, commerçants, chefs d’entreprise", "Cadres", "Professions intermédiaires", "Employés et ouvriers qualifiés", "Employés et ouvriers non qualifiés"],
  series: [{ n: "Fils de cadres", v: [0.2, 7.9, 49.0, 25.4, 13.7, 3.8], c: 1 }, { n: "Fils d’employés ou d’ouvriers non qualifiés", v: [0.6, 6.5, 8.3, 18.7, 43.9, 22.1], c: 2 }]
};
GRAPHES["s3-or"] = {
  type: "barres", t: "La fluidité sociale progresse : le rapport des chances relatives, 1977-2015",
  s: "Rapport des chances relatives (odds ratio) d’être cadre plutôt qu’employé ou ouvrier non qualifié, entre fils de cadres et fils d’employés ou d’ouvriers non qualifiés. 1 = parfaite fluidité.",
  src: "Source : Marc Collet et Émilie Pénicaud, « La mobilité sociale des femmes et des hommes : évolutions entre 1977 et 2015 », Insee, Économie et Statistique n° 510-511-512, 2019 (figure 7). Champ : hommes de 35 à 59 ans comparés à leur père.",
  unite: "", dec: 1, h: 260, pasX: 1,
  x: [1977, 1985, 1993, 2003, 2015], y: [165.0, 92.3, 65.3, 29.3, 34.7], etiquette: "fois"
};

CHAINES["s3-struct"] = { t: "D’où vient la mobilité structurelle ?", e: [
  { t: "Tertiarisation, salarisation, élévation des qualifications : la structure des emplois change d’une génération à l’autre", k: "cause" },
  { f: [{ t: "Moins de places d’agriculteurs, d’artisans, d’ouvriers non qualifiés que de pères dans ces groupes" }, { t: "Plus de places de cadres et de professions intermédiaires que de pères dans ces groupes" }], a: "donc" },
  { t: "Une partie des fils et des filles est obligée de changer de groupe, quelle que soit l’origine", a: "donc" },
  { t: "Mobilité structurelle, surtout ascendante (environ un quart de la mobilité des hommes en 2015)", k: "effet", a: "donc" }
] };
CHAINES["s3-anderson"] = { t: "Plus de diplômés, mais pas forcément plus de mobilité (Boudon, Anderson)", e: [
  { t: "Massification scolaire : les enfants de milieu populaire sont plus diplômés que leurs parents", k: "cause" },
  { t: "Mais tous les groupes progressent : les écarts relatifs de diplôme selon l’origine se réduisent peu", a: "or" },
  { t: "Les places élevées augmentent moins vite que les diplômes : la valeur d’un diplôme donné baisse (inflation scolaire)", a: "et" },
  { t: "À diplôme égal, l’origine sociale continue de jouer (réseau, information, aisance)", a: "et" },
  { t: "Être plus diplômé que son père ne garantit pas une position plus élevée : la mobilité change peu", k: "frein", a: "donc" }
] };
CHAINES["s3-famille"] = { t: "Comment la famille pèse sur le destin social", e: [
  { f: [{ t: "Capital économique : patrimoine, aide au logement, études longues financées", k: "cause" }, { t: "Capital culturel : langage, rapport à l’école, information sur les filières", k: "cause" }, { t: "Capital social : réseau de relations, stages, premiers emplois", k: "cause" }] },
  { t: "Ces ressources se transmettent et se convertissent en diplômes puis en positions", a: "donc" },
  { t: "Reproduction sociale aux deux extrémités de l’échelle", k: "effet", a: "donc" },
  { t: "Mais la configuration familiale (attentes, mobilisation, fratrie, place de l’écrit) peut produire des trajectoires ascendantes « improbables »", k: "frein", a: "mais" }
] };
CHAINES["s3-declass"] = { t: "Le déclassement intergénérationnel (Peugny)", e: [
  { t: "Les enfants de cadres et de professions intermédiaires sont de plus en plus nombreux", k: "cause" },
  { t: "Le nombre de places de cadres augmente, mais pas assez pour tous les accueillir", a: "or" },
  { t: "Une partie d’entre eux occupe une position inférieure à celle de leur père", a: "donc" },
  { t: "Mobilité descendante des hommes : 7,2 % en 1977, 15,0 % en 2015 (Insee)", k: "effet", a: "donc" }
] };

CH.s3 = {
  chapo: "Un fils d’ouvrier devient-il plus souvent cadre qu’il y a quarante ans ? La société française est-elle plus « ouverte » ? Pour répondre, les sociologues construisent des tables de mobilité. Ce chapitre apprend à les fabriquer, à les lire sans se tromper de sens, à distinguer mobilité observée et fluidité, et à expliquer la mobilité par la structure des emplois, l’École et la famille.",
  essentiel: [
    "La <b>mobilité sociale intergénérationnelle</b> compare la position sociale d’un individu à celle de ses parents. Ne la confonds pas avec la mobilité <b>professionnelle</b> (au cours de la carrière) ni avec la mobilité <b>géographique</b>.",
    "La <b>table de mobilité</b> croise origine (catégorie du père ou de la mère) et position (catégorie de l’individu). On en tire une <b>table de destinée</b> (lecture en ligne : que deviennent les enfants d’une origine ?) et une <b>table de recrutement</b> (lecture en colonne : d’où viennent les membres d’un groupe ?).",
    "En 2015, 65 % des hommes et 71 % des femmes ne sont pas dans la même catégorie que leur père ou leur mère (<b>mobilité observée</b>, Insee). Une partie est <b>structurelle</b> : elle vient du changement de la structure des emplois (24 % de la mobilité des hommes).",
    "La <b>fluidité sociale</b> mesure l’égalité des chances relatives d’accès aux positions, indépendamment de la structure. Une société plus mobile n’est pas forcément plus fluide. En France, la fluidité progresse lentement mais la <b>reproduction</b> reste forte : 49 % des fils de cadres sont cadres, contre 8 % des fils d’employés ou ouvriers non qualifiés.",
    "La mobilité s’explique par l’<b>évolution de la structure socioprofessionnelle</b>, les <b>niveaux de formation</b> (dont l’effet est ambigu : paradoxe d’Anderson, Boudon) et les <b>ressources et configurations familiales</b> (capitaux, mobilisation des parents, fratrie)."
  ],
  chiffres: [
    { n: "65 %", l: "des hommes de 35 à 59 ans appartiennent en 2015 à une autre catégorie que leur père ; 71 % des femmes à une autre catégorie que leur mère.", s: "Insee Première n° 1739 (FQP 2014-2015)" },
    { n: "49,0 %", l: "des fils de cadres sont cadres en 2015 ; 8,3 % des fils d’employés ou d’ouvriers non qualifiés.", s: "Insee, FQP 2014-2015" },
    { n: "15,0 %", l: "des hommes connaissent une mobilité descendante par rapport à leur père en 2015, contre 7,2 % en 1977.", s: "Insee Première n° 1739" }
  ],
  objectifs: [
    { bo: "Savoir distinguer la mobilité sociale intergénérationnelle des autres formes de mobilité (géographique, professionnelle).", clair: "Définir la mobilité intergénérationnelle et la distinguer, exemples à l’appui, de la mobilité professionnelle et géographique.", voir: "s3-1" },
    { bo: "Comprendre les principes de construction, les intérêts et les limites des tables de mobilité comme instrument de mesure de la mobilité sociale.", clair: "Savoir comment l’Insee construit une table, passer d’une table d’effectifs aux tables de destinée et de recrutement, citer deux intérêts et deux limites.", voir: "s3-2" },
    { bo: "Comprendre que la mobilité observée comporte une composante structurelle (mobilité structurelle) ; comprendre que la mobilité peut aussi se mesurer de manière relative indépendamment des différences de structure entre origine et position sociales (fluidité sociale) et qu’une société plus mobile n’est pas nécessairement une société plus fluide.", clair: "Distinguer mobilité observée, mobilité structurelle et fluidité (rapport des chances relatives), et expliquer pourquoi plus de mobilité ne veut pas dire plus d’égalité des chances.", voir: "s3-3" },
    { bo: "À partir de la lecture des tables de mobilité, être capable de mettre en évidence des situations de mobilité ascendante, de reproduction sociale et de déclassement, et de retrouver les spécificités de la mobilité sociale des hommes et de celles des femmes.", clair: "Lire une table pour repérer mobilité ascendante, reproduction et déclassement, et comparer hommes et femmes.", voir: "s3-4" },
    { bo: "Comprendre comment l’évolution de la structure socioprofessionnelle, les niveaux de formation et les ressources et configurations familiales contribuent à expliquer la mobilité sociale.", clair: "Expliquer la mobilité par trois familles de facteurs et savoir montrer leurs limites.", voir: "s3-5" }
  ],
  notions: ["mobilité sociale", "mobilité intergénérationnelle", "mobilité intragénérationnelle (professionnelle)", "mobilité géographique", "mobilité verticale (ascendante, descendante)", "mobilité horizontale", "table de mobilité", "table de destinée", "table de recrutement", "autorecrutement", "mobilité observée", "mobilité structurelle", "fluidité sociale", "rapport des chances relatives (odds ratio)", "reproduction sociale", "déclassement", "paradoxe d’Anderson", "capital économique, culturel, social", "configurations familiales"],
  sections: [
    { id: "s3-1", t: "Trois mobilités à ne pas confondre", h:
      '<p class="lede">La <b>mobilité sociale</b> désigne le changement de position sociale d’un individu. Le sociologue Pitirim Sorokin a posé le cadre dès 1927 (<i>Social Mobility</i>) : on peut circuler entre les groupes de la hiérarchie sociale, vers le haut ou vers le bas.</p>' +
      '<div class="def"><b>Mobilité intergénérationnelle</b> — changement de position sociale d’un individu par rapport à celle de ses parents (en France, on compare souvent la catégorie socioprofessionnelle du fils ou de la fille à celle du père, et de plus en plus à celle de la mère).</div>' +
      '<div class="ex"><p>Une fille d’agricultrice exploitante devenue infirmière (profession intermédiaire) connaît une mobilité intergénérationnelle ascendante. En 2015, 19,1 % des filles d’agricultrices sont dans ce cas (Insee, FQP 2014-2015).</p></div>' +
      '<div class="def"><b>Mobilité intragénérationnelle (ou professionnelle)</b> — changement de position au cours de la vie active d’un même individu : promotion, changement de métier, passage du salariat à l’indépendance, chômage.</div>' +
      '<div class="ex"><p>Un technicien promu ingénieur après une formation continue passe de profession intermédiaire à cadre : mobilité professionnelle ascendante, sans rien dire de ses parents.</p></div>' +
      '<div class="def"><b>Mobilité géographique</b> — changement de lieu de résidence (d’une commune, d’une région ou d’un pays à l’autre).</div>' +
      '<p>Les trois se combinent souvent : quitter une région peu dynamique pour une métropole facilite l’accès à un emploi qualifié. Une étude de l’Institut des politiques publiques (Kenedi et Sirugue, note n° 95, 2023) montre que les enfants des familles les plus modestes qui partent vers un département à hauts revenus atteignent en moyenne le même revenu que les enfants de familles aisées restés dans leur département.</p>' +
      '<h3>Le sens de la mobilité</h3><ul><li><b>Verticale ascendante</b> : position plus élevée que celle du parent (fils d’employé devenu cadre).</li><li><b>Verticale descendante</b> : position moins élevée (fille de cadre devenue employée) ; on parle de <b>déclassement</b>.</li><li><b>Horizontale</b> ou « non verticale » : changement de groupe sans hiérarchie nette, par exemple d’agriculteur à ouvrier qualifié, ou d’artisan à profession intermédiaire. L’Insee distingue ici une mobilité « de statut » (salarié / indépendant).</li><li><b>Immobilité</b> ou <b>reproduction sociale</b> : même groupe que le parent.</li></ul>' +
      '<div class="attn"><p>Une mobilité géographique ou professionnelle n’est pas une mobilité sociale intergénérationnelle. Dans une copie, nomme précisément la mobilité dont tu parles et l’<b>étalon</b> de comparaison (le père ? la mère ? le premier emploi ?).</p></div>' },

    { id: "s3-2", t: "Les tables de mobilité : construction, intérêts, limites", h:
      '<p class="lede">Une <b>table de mobilité</b> est un tableau à double entrée qui croise l’origine sociale (en ligne, en général) et la position sociale (en colonne) d’un ensemble d’individus.</p>' +
      '<h3>Comment l’Insee les construit</h3><p>Les tables françaises viennent de l’enquête <b>Formation et qualification professionnelle (FQP)</b> : 1964, 1970, 1977, 1985, 1993, 2003 et 2014-2015 (dernière publiée). On interroge des personnes de <b>35 à 59 ans</b>, en emploi ou anciennement en emploi : à cet âge, la position est en principe stabilisée. On leur demande leur profession et celle qu’exerçaient leur père et leur mère pendant leur jeunesse. On obtient d’abord une <b>table d’effectifs</b>, puis deux tables de pourcentages.</p>' +
      '<div data-anim="s3-table"></div>' +
      '<div class="tbl"><table><thead><tr><th>Lecture</th><th>Table de destinée</th><th>Table de recrutement</th></tr></thead><tbody>' +
      '<tr><td><b>Calcul</b></td><td>Chaque case ÷ total de sa <b>ligne</b> (origine)</td><td>Chaque case ÷ total de sa <b>colonne</b> (position)</td></tr>' +
      '<tr><td><b>Question</b></td><td>Que deviennent les enfants d’une origine donnée ?</td><td>D’où viennent les membres d’un groupe ?</td></tr>' +
      '<tr><td><b>Phrase type</b></td><td>« Sur 100 fils de cadres, 49 sont cadres. »</td><td>« Sur 100 cadres, environ 33 sont fils de cadres. »</td></tr>' +
      '<tr><td><b>Diagonale</b></td><td>Taux d’<b>immobilité</b> (reproduction)</td><td>Taux d’<b>autorecrutement</b></td></tr></tbody></table></div>' +
      '<h3>La table de destinée des hommes en 2015</h3>' +
      '<div class="tbl"><table><thead><tr><th>Père \\ fils (en %)</th><th class="n">Agri.</th><th class="n">Art., comm.</th><th class="n">Cadres</th><th class="n">Prof. int.</th><th class="n">Emp. et ouv. qualifiés</th><th class="n">Emp. et ouv. non qualifiés</th><th class="n">Total</th></tr></thead><tbody>' +
      '<tr><td>Agriculteurs exploitants</td><td class="n"><b>26,7</b></td><td class="n">7,9</td><td class="n">8,5</td><td class="n">20,4</td><td class="n">27,4</td><td class="n">9,1</td><td class="n">100</td></tr>' +
      '<tr><td>Artisans, commerçants, chefs d’entreprise</td><td class="n">0,9</td><td class="n"><b>20,6</b></td><td class="n">23,1</td><td class="n">23,8</td><td class="n">23,6</td><td class="n">7,9</td><td class="n">100</td></tr>' +
      '<tr><td>Cadres</td><td class="n">0,2</td><td class="n">7,9</td><td class="n"><b>49,0</b></td><td class="n">25,4</td><td class="n">13,7</td><td class="n">3,8</td><td class="n">100</td></tr>' +
      '<tr><td>Professions intermédiaires</td><td class="n">0,6</td><td class="n">7,8</td><td class="n">26,5</td><td class="n"><b>31,1</b></td><td class="n">26,2</td><td class="n">7,7</td><td class="n">100</td></tr>' +
      '<tr><td>Employés et ouvriers qualifiés</td><td class="n">0,6</td><td class="n">7,2</td><td class="n">12,7</td><td class="n">26,8</td><td class="n"><b>42,6</b></td><td class="n">10,1</td><td class="n">100</td></tr>' +
      '<tr><td>Employés et ouvriers non qualifiés</td><td class="n">0,6</td><td class="n">6,5</td><td class="n">8,3</td><td class="n">18,7</td><td class="n">43,9</td><td class="n"><b>22,1</b></td><td class="n">100</td></tr>' +
      '<tr><td><i>Ensemble des fils</i></td><td class="n">2,8</td><td class="n">9,1</td><td class="n">20,4</td><td class="n">25,3</td><td class="n">32,4</td><td class="n">10,1</td><td class="n">100</td></tr></tbody></table></div>' +
      '<p class="src-l">Source : Insee, enquête FQP 2014-2015, Insee Première n° 1739 (février 2019). Champ : France métropolitaine, hommes de 35 à 59 ans actifs occupés ou anciens actifs occupés. Lecture : en 2015, 49,0 % des fils de cadres sont eux-mêmes cadres.</p>' +
      '<div data-graph="s3-dest"></div>' +
      '<details class="pli"><summary>Calculer la table de recrutement à partir de la destinée (méthode et résultat)</summary><div>' +
      '<p>En 2015, les pères des hommes de 35 à 59 ans se répartissent ainsi : agriculteurs 8,3 %, artisans et commerçants 13,0 %, cadres 13,9 %, professions intermédiaires 15,9 %, employés et ouvriers qualifiés 35,6 %, non qualifiés 13,1 % (Insee). Pour 1 000 fils, il y a donc 139 fils de cadres, dont 49,0 % sont cadres : 139 × 0,49 ≈ 68 cadres fils de cadres. En faisant de même pour toute la colonne, on trouve environ 203 cadres sur 1 000 hommes. D’où : 68 ÷ 203 ≈ <b>33,5 %</b> des cadres sont fils de cadres.</p>' +
      '<div class="tbl"><table><thead><tr><th>Origine \\ position (recrutement, en %)</th><th class="n">Agri.</th><th class="n">Art., comm.</th><th class="n">Cadres</th><th class="n">Prof. int.</th><th class="n">Emp. et ouv. qual.</th><th class="n">Emp. et ouv. non qual.</th></tr></thead><tbody>' +
      '<tr><td>Agriculteurs</td><td class="n"><b>80,6</b></td><td class="n">7,2</td><td class="n">3,5</td><td class="n">6,7</td><td class="n">7,0</td><td class="n">7,5</td></tr>' +
      '<tr><td>Artisans, commerçants</td><td class="n">4,3</td><td class="n"><b>29,5</b></td><td class="n">14,8</td><td class="n">12,3</td><td class="n">9,5</td><td class="n">10,2</td></tr>' +
      '<tr><td>Cadres</td><td class="n">1,0</td><td class="n">12,1</td><td class="n"><b>33,5</b></td><td class="n">14,0</td><td class="n">5,9</td><td class="n">5,3</td></tr>' +
      '<tr><td>Professions intermédiaires</td><td class="n">3,5</td><td class="n">13,6</td><td class="n">20,7</td><td class="n"><b>19,6</b></td><td class="n">12,9</td><td class="n">12,2</td></tr>' +
      '<tr><td>Emp. et ouv. qualifiés</td><td class="n">7,8</td><td class="n">28,2</td><td class="n">22,2</td><td class="n">37,8</td><td class="n"><b>46,9</b></td><td class="n">35,9</td></tr>' +
      '<tr><td>Emp. et ouv. non qualifiés</td><td class="n">2,9</td><td class="n">9,4</td><td class="n">5,3</td><td class="n">9,7</td><td class="n">17,8</td><td class="n"><b>28,9</b></td></tr>' +
      '<tr><td><i>Total</i></td><td class="n">100</td><td class="n">100</td><td class="n">100</td><td class="n">100</td><td class="n">100</td><td class="n">100</td></tr></tbody></table></div>' +
      '<p class="src-l">Calcul du site à partir des tables publiées par l’Insee (origines × destinées) ; les arrondis peuvent décaler certains chiffres de quelques dixièmes. L’Insee publie une autoreproduction des agriculteurs de 81 % en 2015.</p>' +
      '<p>Lecture : en 2015, environ 80 % des agriculteurs sont fils d’agriculteurs (fort <b>autorecrutement</b>), alors que les cadres viennent de tous les milieux : un tiers sont fils de cadres, mais plus d’un quart (27,5 %) sont fils d’employés ou d’ouvriers. C’est l’effet de la croissance du nombre de cadres : il faut bien les « recruter » ailleurs.</p></div></details>' +
      '<h3>Intérêts</h3><ul><li><b>Mesurer</b> l’ampleur de la mobilité et de la reproduction, et les <b>comparer dans le temps</b> (enquêtes répétées depuis 1964) et entre pays.</li><li>Distinguer deux questions : le <b>destin</b> des enfants d’une origine (égalité des chances) et la <b>composition</b> d’un groupe (homogénéité, conscience de classe possible).</li><li>Mettre en évidence la mobilité ascendante, descendante, la reproduction, les différences entre hommes et femmes.</li></ul>' +
      '<h3>Limites</h3><ul><li><b>Des catégories larges</b> : six groupes masquent beaucoup de mobilité interne (un fils d’ouvrier non qualifié devenu ouvrier qualifié est classé immobile dans la table habituelle en PCS).</li><li><b>Une hiérarchie discutable</b> : agriculteurs ou artisans ne se classent pas facilement au-dessus ou au-dessous des salariés ; la mobilité est alors dite « non verticale ».</li><li><b>Les nomenclatures changent</b> (PCS 1982, 2003, 2020) et le contenu d’une catégorie évolue : être cadre en 1977 et en 2015 n’a pas la même rareté.</li><li><b>Le choix de l’étalon</b> : longtemps, les études ont surtout comparé les fils à leur père ; or la comparaison des filles avec leur mère ou avec leur père change les conclusions (section 4).</li><li><b>Une photographie tardive</b> : les 35-59 ans d’aujourd’hui ont eu leurs parents en activité il y a 30 à 50 ans ; et la table ne dit rien des <b>causes</b> de la mobilité.</li><li>La table ne mesure que la catégorie socioprofessionnelle : ni le revenu, ni le patrimoine (voir la corrélation des revenus parents-enfants en <a href="#r1:r1-2">R1</a>).</li></ul>' },

    { id: "s3-3", t: "Mobilité observée, mobilité structurelle, fluidité sociale", h:
      '<div class="def"><b>Mobilité observée (ou brute)</b> — part des individus dont la position diffère de celle de leur parent. Elle se lit hors de la diagonale de la table d’effectifs.</div>' +
      '<div data-graph="s3-mob"></div>' +
      '<p>Lecture : selon l’Insee, la mobilité observée des hommes par rapport à leur père est presque stable depuis 40 ans (63,8 % en 1977, 65,2 % en 2015). Celle des femmes par rapport à leur mère progresse fortement (59,1 % en 1977, 70,5 % en 2015). Chez les hommes, la mobilité descendante double (7,2 % → 15,0 %).</p>' +
      '<h3>La composante structurelle</h3><div class="def"><b>Mobilité structurelle</b> — partie de la mobilité observée imposée par la différence entre la structure des emplois des pères (origines) et celle des fils (positions). Elle se mesure par l’écart entre les marges de la table.</div>' +
      '<div class="ex"><p>En 2015, 13,9 % des pères étaient cadres, mais 20,4 % des fils le sont ; 8,3 % des pères étaient agriculteurs, 2,8 % des fils. Même si chacun héritait autant que possible du groupe de son père, au moins 15,8 % des hommes auraient changé de groupe (indice de dissimilarité de l’Insee : la moitié de la somme des écarts entre les deux marges). Cela représente 24,2 % de la mobilité observée des hommes (15,8 ÷ 65,2) ; c’était 39,6 % en 1977. Pour les femmes par rapport à leur mère : 24,5 %, soit 34,8 % de leur mobilité.</p></div>' +
      '<div data-chain="s3-struct"></div>' +
      '<p>Le reste de la mobilité observée est parfois appelé mobilité <b>nette</b> (ou de circulation) : celle qui ne s’explique pas mécaniquement par l’évolution des emplois. Cette décomposition est simple mais imparfaite ; les sociologues lui préfèrent aujourd’hui la mesure de la fluidité.</p>' +
      '<h3>La fluidité sociale : raisonner en chances relatives</h3>' +
      '<div class="def"><b>Fluidité sociale</b> — degré d’indépendance entre l’origine et la position sociale, une fois neutralisés les changements de structure. Une société parfaitement fluide est une société où les chances relatives d’accéder à une position ne dépendent pas de l’origine (égalité des chances).</div>' +
      '<p>On la mesure par le <b>rapport des chances relatives</b> (en anglais <i>odds ratio</i>). On compare deux origines et deux positions :</p>' +
      '<div class="ex"><p>En 2015, un fils de cadre a 49,0 % de chances d’être cadre et 3,8 % d’être employé ou ouvrier non qualifié, soit 12,9 fois plus de chances d’être cadre que non qualifié. Pour un fils d’employé ou d’ouvrier non qualifié : 8,3 % contre 22,1 %, soit 0,38. Le rapport des chances relatives vaut 12,9 ÷ 0,38 ≈ 34 (l’Insee publie 34,7 avec les données non arrondies). Il valait 165 en 1977.</p></div>' +
      '<div data-graph="s3-or"></div>' +
      '<p>Plus le rapport se rapproche de 1, plus la société est fluide. Il a beaucoup baissé depuis 1977 (avec une légère remontée entre 2003 et 2015), mais reste très loin de 1. Le sociologue <b>Louis-André Vallet</b> a montré dès la fin des années 1990 une hausse lente et régulière de la fluidité en France depuis les années 1950 ; à l’échelle internationale, <b>Robert Erikson et John Goldthorpe</b> (<i>The Constant Flux</i>, 1992) concluaient que la fluidité varie peu entre pays industrialisés et dans le temps.</p>' +
      '<h3>Plus mobile ne veut pas dire plus fluide</h3>' +
      '<div class="cle"><p>La mobilité observée peut augmenter <b>seulement parce que la structure change</b> (beaucoup de places de cadres créées) sans que les chances relatives des enfants d’ouvriers et de cadres se rapprochent. À l’inverse, une société dont la structure ne bouge plus peut devenir plus fluide sans que la mobilité observée augmente. C’est ce que suggère la France de 1977 à 2015 : mobilité des hommes presque stable (63,8 % → 65,2 %), fluidité en hausse (rapport de 165 à 34,7).</p></div>' +
      '<div class="aut"><span class="mono">CT</span><span class="an">Claude Thélot<small><i>Tel père, tel fils ?</i>, 1982</small></span><span class="ad">À partir des enquêtes FQP, il montre que la mobilité observée a augmenté pendant les Trente Glorieuses surtout sous l’effet de la mobilité structurelle, et que l’hérédité sociale reste forte. Il insiste sur la différence entre la mobilité « brute » et l’inégalité des chances.</span></div>' },

    { id: "s3-4", t: "Lire les tables : ascension, reproduction, déclassement, femmes et hommes", h:
      '<h3>1. La reproduction sociale reste forte aux deux extrémités</h3><p>La diagonale de la table de destinée de 2015 montre que 49,0 % des fils de cadres sont cadres et 42,6 % des fils d’employés ou d’ouvriers qualifiés sont dans le même groupe que leur père. Si l’on regroupe cadres et professions intermédiaires, <b>74,4 %</b> des fils de cadres occupent une position d’encadrement (calcul : 49,0 + 25,4). Le sociologue <b>Camille Peugny</b> parle de « destin au berceau » (<i>Le Destin au berceau</i>, 2013) pour souligner cette persistance.</p>' +
      '<h3>2. Une mobilité ascendante réelle mais souvent « courte »</h3><p>En 2015, 27,6 % des hommes sont en position plus élevée que leur père (Insee). Mais l’ascension se fait surtout vers le groupe juste au-dessus : 26,8 % des fils d’employés ou ouvriers qualifiés deviennent professions intermédiaires, seulement 12,7 % deviennent cadres. Les trajectoires longues (d’ouvrier non qualifié à cadre) restent rares : 8,3 %.</p>' +
      '<div class="ex"><p>Les « <b>transclasses</b> » (mot de la philosophe Chantal Jaquet, <i>Les Transclasses</i>, 2014) ou « transfuges de classe » sont ces personnes qui ont fait une longue ascension ; leurs récits (Annie Ernaux, Didier Eribon) décrivent le décalage culturel qu’elle provoque. Ces parcours existent, mais statistiquement ils restent des exceptions.</p></div>' +
      '<h3>3. Le déclassement</h3><div class="def"><b>Déclassement intergénérationnel</b> — situation d’un individu dont la position est inférieure à celle de son parent (mobilité descendante). On parle aussi de déclassement <b>scolaire</b> quand l’emploi occupé est moins qualifié que ce que permettrait le diplôme.</div>' +
      '<p>La mobilité descendante des hommes passe de 7,2 % (1977) à 15,0 % (2015). En 2015, 42,9 % des fils de cadres occupent une position inférieure à celle de leur père (calcul à partir de la table : 25,4 + 13,7 + 3,8), mais la plupart deviennent professions intermédiaires.</p>' +
      '<div data-chain="s3-declass"></div>' +
      '<div class="aut"><span class="mono">CP</span><span class="an">Camille Peugny<small><i>Le Déclassement</i>, 2009</small></span><span class="ad">Les générations nées dans les années 1960 connaissent davantage de déclassement que celles nées dans les années 1940 : elles sont plus diplômées, mais les places élevées n’ont pas augmenté au même rythme. Le déclassement nourrit frustration et défiance politique.</span></div>' +
      '<h3>4. Les spécificités de la mobilité des femmes</h3>' +
      '<div class="tbl"><table><thead><tr><th>En 2015 (en %)</th><th class="n">Hommes / père</th><th class="n">Femmes / mère</th><th class="n">Femmes / père</th></tr></thead><tbody>' +
      '<tr><td>Mobilité observée</td><td class="n">65,2</td><td class="n">70,5</td><td class="n">70,1</td></tr><tr><td>dont ascendante</td><td class="n">27,6</td><td class="n">39,8</td><td class="n">21,8</td></tr><tr><td>dont descendante</td><td class="n">15,0</td><td class="n">11,7</td><td class="n">25,0</td></tr><tr><td>Immobilité</td><td class="n">34,8</td><td class="n">29,5</td><td class="n">29,9</td></tr></tbody></table></div>' +
      '<p class="src-l">Source : Insee Première n° 1739, février 2019 (FQP 2014-2015). Le reste de la mobilité observée est « non verticale ».</p>' +
      '<ul><li><b>Comparées à leur mère</b>, les femmes connaissent beaucoup de mobilité ascendante (39,8 %) : les mères étaient souvent agricultrices ou employées peu qualifiées, et les filles ont profité de l’allongement des études et de la tertiarisation. Une part importante de cette mobilité est structurelle (34,8 %).</li><li><b>Comparées à leur père</b>, elles connaissent plus de mobilité descendante qu’ascendante (25,0 % contre 21,8 %) : à origine égale, elles occupent plus souvent des emplois d’employées, moins souvent de cadres. Seules 35,0 % des filles de cadres sont cadres, contre 49,0 % des fils.</li><li>Ces écarts traduisent la <b>ségrégation professionnelle</b> (emplois féminisés du tertiaire), le temps partiel et les carrières freinées par les charges familiales (voir <a href="#s1:s1-3">S1</a>).</li></ul>' +
      '<div class="attn"><p>Pour juger de la mobilité des femmes, précise toujours l’étalon : « par rapport à leur mère » ou « par rapport à leur père ». Les deux lectures sont justes, mais elles ne disent pas la même chose.</p></div>' },

    { id: "s3-5", t: "Les facteurs de la mobilité sociale", h:
      '<p class="lede">Le programme cite trois familles de facteurs. Une bonne copie les relie et montre leurs limites.</p>' +
      '<h3>1. L’évolution de la structure socioprofessionnelle</h3><p>La tertiarisation et l’élévation des qualifications ont créé des places en haut de l’échelle (cadres : 8,0 % de l’emploi en 1982, 23,8 % en 2025, Insee) et supprimé des places d’agriculteurs et d’ouvriers. C’est le moteur de la <b>mobilité structurelle</b>, majoritairement ascendante. Quand la structure se transforme moins vite, cette mobilité diminue : sa part dans la mobilité des hommes passe de 39,6 % en 1977 à 24,2 % en 2015.</p>' +
      '<div class="ex"><p>Pendant les Trente Glorieuses, l’exode rural fait passer les fils d’agriculteurs vers le salariat : en 2015 encore, seuls 26,7 % des fils d’agriculteurs sont agriculteurs, 27,4 % sont devenus employés ou ouvriers qualifiés et 20,4 % professions intermédiaires (Insee).</p></div>' +
      '<h3>2. Les niveaux de formation</h3><p>Le diplôme est le principal canal de l’ascension dans une société salariale : il donne accès aux emplois qualifiés. La <b>massification scolaire</b> (20,1 % de bacheliers dans une génération en 1970, 80,1 % en 2025 : voir <a href="#s2">S2</a>) a permis à de nombreux enfants de milieu populaire d’être plus diplômés que leurs parents.</p>' +
      '<p>Mais l’effet est ambigu :</p>' +
      '<div data-chain="s3-anderson"></div>' +
      '<div class="aut"><span class="mono">RB</span><span class="an">Raymond Boudon<small><i>L’Inégalité des chances</i>, 1973</small></span><span class="ad">Les choix scolaires des familles dépendent de leur position (calcul coûts / avantages / risques). Même si les inégalités face à l’école diminuent, la mobilité sociale peut rester stable, car la structure des positions et la concurrence pour les places ne changent pas au même rythme : la démocratisation scolaire n’entraîne pas automatiquement plus de mobilité.</span></div>' +
      '<div class="plus"><p>Le <b>paradoxe d’Anderson</b> (le sociologue américain C. Arnold Anderson, 1961) : un fils plus diplômé que son père n’occupe pas forcément une position plus élevée. En France, Marie Duru-Bellat a analysé cette « inflation scolaire » (<i>L’Inflation scolaire</i>, 2006) : quand tout le monde est plus diplômé, le diplôme protège moins.</p></div>' +
      '<p>Le diplôme reste pourtant décisif : il réduit fortement le risque de déclassement et de chômage, et son absence pèse plus lourd qu’hier.</p>' +
      '<h3>3. Les ressources et configurations familiales</h3>' +
      '<div data-chain="s3-famille"></div>' +
      '<div class="aut"><span class="mono">PB</span><span class="an">Pierre Bourdieu<small>1930-2002</small></span><span class="ad">Les familles transmettent un <b>capital économique</b> (patrimoine), <b>culturel</b> (savoirs, diplômes, aisance avec la culture scolaire) et <b>social</b> (relations). Ces capitaux se convertissent les uns dans les autres et assurent la <b>reproduction sociale</b> (<i>La Reproduction</i>, avec Jean-Claude Passeron, 1970).</span></div>' +
      '<div class="ex"><p>Le capital social joue dès l’entrée sur le marché du travail : stage obtenu par une connaissance, conseil d’orientation, premier emploi. Le sociologue américain Mark Granovetter a montré (« La force des liens faibles », 1973) que les relations éloignées (connaissances, anciens collègues) apportent des informations utiles pour trouver un emploi ; or l’étendue de ce réseau dépend du milieu social.</p></div>' +
      '<p>Mais la famille n’est pas un simple réservoir de capitaux : sa <b>configuration</b> compte. Bernard Lahire (<i>Tableaux de familles</i>, 1995) explique des réussites « paradoxales » en milieu populaire par l’ordre domestique, l’autorité, la place de l’écrit, la mobilisation d’un parent ou d’un aîné. La <b>taille de la fratrie</b>, le rang de naissance, la séparation des parents ou la <b>monoparentalité</b> (niveau de vie plus faible : voir <a href="#s1:s1-1">S1</a>) modifient aussi les ressources disponibles.</p>' +
      '<div class="cle"><p><b>Pour la dissertation</b> (sujet tombé au bac 2026 : « Les ressources et configurations familiales suffisent-elles à expliquer la mobilité sociale ? ») : la famille explique beaucoup de la reproduction, mais elle ne suffit pas. La structure des emplois crée ou ferme des places, l’École et le diplôme transforment les ressources familiales, et les politiques publiques (bourses, éducation prioritaire) pèsent aussi.</p></div>' }
  ],
  pieges: [
    { f: "« La table de destinée dit que 49 % des cadres sont fils de cadres. »", v: "Non : elle dit que 49,0 % des <b>fils de cadres</b> sont cadres (lecture en ligne). La part des cadres qui sont fils de cadres se lit dans la table de <b>recrutement</b> (environ 33 % en 2015)." },
    { f: "« La mobilité sociale augmente, donc l’égalité des chances progresse. »", v: "La mobilité observée peut venir de la seule <b>mobilité structurelle</b>. L’égalité des chances se mesure par la <b>fluidité</b> (rapport des chances relatives)." },
    { f: "« Un rapport des chances relatives de 34,7 signifie que les fils de cadres ont 34,7 % de chances de plus. »", v: "C’est un rapport de rapports : les chances d’être cadre plutôt que non qualifié sont environ 35 <b>fois</b> plus élevées pour un fils de cadre que pour un fils de non qualifié." },
    { f: "Confondre mobilité professionnelle et mobilité intergénérationnelle.", v: "La mobilité professionnelle se déroule au cours de la carrière d’un même individu ; l’intergénérationnelle compare deux générations." },
    { f: "« Les femmes connaissent surtout de la mobilité descendante. »", v: "C’est vrai <b>par rapport à leur père</b> (25,0 % de descendante). Par rapport à leur mère, elles connaissent surtout de la mobilité ascendante (39,8 %)." },
    { f: "« Plus de diplômés entraîne mécaniquement plus de mobilité. »", v: "Paradoxe d’Anderson et analyse de Boudon : si tout le monde progresse et que les places élevées n’augmentent pas au même rythme, la mobilité change peu." },
    { f: "Calculer une table de recrutement en divisant par le total des lignes.", v: "Recrutement : on divise par le total de la <b>colonne</b>. Destinée : par le total de la <b>ligne</b>. Vérifie que tes pourcentages totalisent 100 dans le bon sens." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Mobilité intergénérationnelle</b> : position de l’individu comparée à celle de son parent. <b>Professionnelle</b> (intragénérationnelle) : au cours de la carrière. <b>Géographique</b> : changement de lieu.</li>' +
    '<li><b>Table de mobilité</b> : croise origine et position (enquête FQP de l’Insee, 35-59 ans). <b>Destinée</b> : ÷ ligne, « que deviennent les fils de… ? ». <b>Recrutement</b> : ÷ colonne, « d’où viennent les… ? ».</li>' +
    '<li><b>Mobilité observée</b> : hors diagonale. <b>Structurelle</b> : imposée par l’écart entre les marges (½ Σ |origine − position|). <b>Fluidité</b> : chances relatives (odds ratio), 1 = égalité des chances.</li>' +
    '<li><b>Plus mobile ≠ plus fluide</b> : la mobilité peut venir de la seule structure.</li>' +
    '<li><b>Lectures</b> : reproduction (diagonale), mobilité ascendante souvent « courte », déclassement (Peugny), femmes : ascendantes par rapport à la mère, descendantes par rapport au père.</li>' +
    '<li><b>Facteurs</b> : structure socioprofessionnelle (tertiarisation) ; formation (massification, paradoxe d’Anderson, Boudon) ; famille (capitaux de Bourdieu, configurations de Lahire, fratrie, monoparentalité).</li></ul>' +
    '<h3>Chiffres à citer (Insee, FQP 2014-2015)</h3><ul><li>Mobilité observée 2015 : hommes / père 65,2 % ; femmes / mère 70,5 % ; part structurelle 24,2 % et 34,8 %.</li><li>Hommes : ascendante 27,6 %, descendante 15,0 % (7,2 % en 1977).</li><li>49,0 % des fils de cadres sont cadres ; 8,3 % des fils d’employés ou ouvriers non qualifiés.</li><li>Rapport des chances relatives cadres / non qualifiés : 165 (1977) → 34,7 (2015).</li></ul>',
  chainesFiche: ["s3-struct", "s3-anderson", "s3-famille", "s3-declass"],
  quiz: [
    { q: "Un technicien devenu ingénieur au cours de sa carrière connaît une mobilité…", c: ["professionnelle (intragénérationnelle) ascendante", "intergénérationnelle ascendante", "géographique", "structurelle"], r: 0, e: "On compare deux positions d’un même individu au cours de sa vie active, pas avec ses parents.", s: "s3-1" },
    { q: "Dans une table de destinée, chaque case est divisée par…", c: ["le total de sa ligne (l’origine)", "le total de sa colonne (la position)", "l’effectif total de la table", "la case de la diagonale"], r: 0, e: "Destinée : que deviennent les enfants d’une origine ? On raisonne sur 100 enfants de cette origine.", s: "s3-2" },
    { q: "« En 2015, 49,0 % des fils de cadres sont cadres. » Ce chiffre vient…", c: ["d’une table de destinée", "d’une table de recrutement", "d’un calcul de mobilité structurelle", "d’un rapport des chances relatives"], r: 0, e: "On part de l’origine (fils de cadres) et on regarde leur position : lecture en ligne.", s: "s3-2" },
    { q: "La diagonale d’une table de recrutement donne…", c: ["le taux d’autorecrutement de chaque groupe", "le taux de mobilité observée", "la mobilité structurelle", "la part des femmes"], r: 0, e: "Elle indique la part des membres d’un groupe qui ont une origine dans ce même groupe (ex. environ 80 % des agriculteurs sont fils d’agriculteurs).", s: "s3-2" },
    { q: "Laquelle est une limite des tables de mobilité ?", c: ["Des catégories larges masquent la mobilité à l’intérieur de chaque groupe", "Elles ne permettent aucune comparaison dans le temps", "Elles ne portent que sur les moins de 25 ans", "Elles mesurent directement l’égalité des chances"], r: 0, e: "Six groupes seulement : passer d’ouvrier non qualifié à qualifié peut être invisible ; la hiérarchie entre indépendants et salariés est aussi discutable.", s: "s3-2" },
    { q: "La mobilité structurelle est la part de la mobilité…", c: ["imposée par l’écart entre la structure des emplois des pères et celle des fils", "due au seul mérite scolaire", "des personnes qui changent de région", "mesurée par le rapport des chances relatives"], r: 0, e: "Elle se calcule à partir des marges de la table (indice de dissimilarité : 15,8 % pour les hommes en 2015).", s: "s3-3" },
    { q: "Une société « plus mobile » n’est pas nécessairement « plus fluide » parce que…", c: ["la mobilité observée peut augmenter sous le seul effet de la structure, sans rapprochement des chances relatives", "la fluidité ne concerne que les femmes", "la mobilité se mesure en euros", "la fluidité exclut la mobilité ascendante"], r: 0, e: "La fluidité neutralise la structure : elle compare les chances relatives d’enfants d’origines différentes.", s: "s3-3" },
    { q: "En 2015, le rapport des chances relatives (cadres / employés ou ouvriers non qualifiés) vaut 34,7 pour les hommes. Il valait 165 en 1977. On peut en conclure que…", c: ["la fluidité sociale a progressé, mais l’égalité des chances reste très loin d’être atteinte", "l’égalité des chances est atteinte", "la mobilité structurelle a disparu", "la reproduction sociale a augmenté"], r: 0, e: "Plus le rapport est proche de 1, plus la société est fluide. 34,7 reste très éloigné de 1.", s: "s3-3" },
    { q: "Selon l’Insee, la mobilité observée des hommes par rapport à leur père entre 1977 et 2015…", c: ["est presque stable (63,8 % puis 65,2 %)", "a doublé", "a été divisée par deux", "est passée de 30 % à 90 %"], r: 0, e: "La mobilité des hommes est quasi stable ; celle des femmes par rapport à leur mère progresse (59,1 % → 70,5 %).", s: "s3-3" },
    { q: "Par rapport à leur père, les femmes de 35 à 59 ans connaissent en 2015…", c: ["plus de mobilité descendante (25,0 %) qu’ascendante (21,8 %)", "surtout de la mobilité ascendante (39,8 %)", "aucune mobilité", "autant de mobilité que les hommes dans tous les sens"], r: 0, e: "Les 39,8 % de mobilité ascendante concernent la comparaison avec la mère. Avec le père, la ségrégation professionnelle pèse.", s: "s3-4" },
    { q: "Le déclassement intergénérationnel désigne…", c: ["une position inférieure à celle de son parent", "un changement de région", "une mobilité horizontale", "la perte d’un emploi en cours de carrière uniquement"], r: 0, e: "C’est une mobilité descendante entre générations. Peugny montre sa hausse pour les générations nées dans les années 1960.", s: "s3-4" },
    { q: "Le paradoxe d’Anderson signifie que…", c: ["être plus diplômé que son père ne garantit pas une position sociale plus élevée", "les diplômés sont toujours plus mobiles", "les femmes sont plus diplômées que les hommes", "la mobilité structurelle augmente avec le chômage"], r: 0, e: "Si les diplômes progressent plus vite que les places élevées, leur valeur relative baisse (inflation scolaire).", s: "s3-5" },
    { q: "Pour Raymond Boudon, la démocratisation de l’école…", c: ["n’entraîne pas automatiquement une hausse de la mobilité sociale", "supprime la reproduction sociale", "est impossible", "dépend uniquement du capital culturel"], r: 0, e: "La structure des positions et la concurrence pour les places ne changent pas au même rythme que l’accès aux diplômes.", s: "s3-5" },
    { q: "Lequel est un exemple de « configuration familiale » au sens de Lahire ?", c: ["Un aîné qui suit de près la scolarité de ses frères et sœurs", "Le montant du patrimoine hérité", "Le taux de chômage de la région", "La création de postes de cadres"], r: 0, e: "Lahire insiste sur l’organisation concrète de la famille (ordre, autorité, rapport à l’écrit, mobilisation), pas seulement sur les capitaux.", s: "s3-5" }
  ],
  cartes: [
    { r: "Mobilité intergénérationnelle", v: "Changement de position sociale d’un individu par rapport à celle de ses parents." },
    { r: "Mobilité intragénérationnelle (professionnelle)", v: "Changement de position d’un individu au cours de sa vie active (promotion, reconversion)." },
    { r: "Mobilité géographique", v: "Changement de lieu de résidence ; elle peut favoriser la mobilité sociale." },
    { r: "Table de mobilité", v: "Tableau à double entrée qui croise l’origine sociale et la position sociale (Insee, enquête FQP, 35-59 ans)." },
    { r: "Table de destinée", v: "Chaque case ÷ total de la ligne : que deviennent les enfants d’une origine ? Diagonale = immobilité." },
    { r: "Table de recrutement", v: "Chaque case ÷ total de la colonne : d’où viennent les membres d’un groupe ? Diagonale = autorecrutement." },
    { r: "Mobilité observée", v: "Part des individus dont la position diffère de celle de leur parent (hommes / père : 65,2 % en 2015)." },
    { r: "Mobilité structurelle", v: "Mobilité imposée par l’écart entre la structure des emplois des parents et celle des enfants (15,8 % des hommes en 2015, 24,2 % de leur mobilité)." },
    { r: "Fluidité sociale", v: "Indépendance entre origine et position une fois neutralisée la structure : égalité des chances relatives." },
    { r: "Rapport des chances relatives (odds ratio)", v: "Rapport entre les chances relatives de deux origines d’accéder à une position plutôt qu’à une autre. 1 = parfaite fluidité. Cadres / non qualifiés : 34,7 en 2015." },
    { r: "Reproduction sociale", v: "Transmission des positions sociales d’une génération à l’autre (49,0 % des fils de cadres sont cadres en 2015)." },
    { r: "Déclassement", v: "Mobilité descendante : position inférieure à celle du parent (hommes : 15,0 % en 2015). Peugny, <i>Le Déclassement</i>, 2009." },
    { r: "Paradoxe d’Anderson", v: "Être plus diplômé que son père ne garantit pas une position plus élevée (Anderson, 1961)." },
    { r: "Boudon, <i>L’Inégalité des chances</i> (1973)", v: "La démocratisation scolaire n’entraîne pas automatiquement plus de mobilité sociale." },
    { r: "Capitaux (Bourdieu)", v: "Économique, culturel, social : transmis par la famille, ils se convertissent en diplômes et en positions." },
    { r: "Configurations familiales (Lahire)", v: "Organisation concrète de la famille (ordre, autorité, rapport à l’écrit, mobilisation) qui explique des réussites « paradoxales »." },
    { r: "Thélot, <i>Tel père, tel fils ?</i> (1982)", v: "Mobilité des Trente Glorieuses surtout structurelle ; hérédité sociale forte." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice inventé pour le site, données Insee", t: "Passer d’une table de destinée à une table de recrutement", enonce:
      '<p>En 2015 (Insee, FQP), pour 1 000 hommes de 35 à 59 ans : 139 sont fils de cadres et 131 sont fils d’employés ou d’ouvriers non qualifiés. 49,0 % des fils de cadres et 8,3 % des fils de non qualifiés sont cadres. Au total, 203 hommes sur 1 000 sont cadres.</p><ol><li>Combien de cadres sont fils de cadres ? fils de non qualifiés ?</li><li>Calcule la part des cadres qui sont fils de cadres, puis fils de non qualifiés. Comment s’appelle ce type de pourcentage ?</li><li>Calcule le rapport des chances brutes d’être cadre entre fils de cadres et fils de non qualifiés, et rédige une phrase.</li></ol>',
      corrige: '<ol><li>139 × 0,490 ≈ 68 cadres fils de cadres ; 131 × 0,083 ≈ 11 cadres fils de non qualifiés.</li><li>68 ÷ 203 ≈ 33,5 % ; 11 ÷ 203 ≈ 5,4 % (5,3 % avec les données non arrondies). Ce sont des pourcentages de <b>recrutement</b> (lecture en colonne).</li><li>49,0 ÷ 8,3 ≈ 5,9 : « En 2015, selon l’Insee, un fils de cadre a environ 5,9 fois plus de chances d’être cadre qu’un fils d’employé ou d’ouvrier non qualifié. » Ce n’est pas encore un rapport des chances <b>relatives</b> (odds ratio), qui compare aussi les chances d’être non qualifié.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que la mobilité sociale observée comporte une composante structurelle.", enonce: "<p>4 points en 2026, 3,5 points à partir de la session 2027. Sans document.</p>",
      methode: "<p>Définis les deux notions, explique le mécanisme (changement de structure → places imposées), illustre par un exemple chiffré, puis nuance (la structure n’explique pas tout : fluidité).</p>",
      corrige: '<div class="copie"><p>La mobilité sociale observée est la part des individus qui occupent une position sociale différente de celle de leur parent. Selon l’Insee, elle concerne 65,2 % des hommes de 35 à 59 ans par rapport à leur père en 2015.</p><p>Une partie de cette mobilité est structurelle : elle s’explique par l’évolution de la structure des emplois entre la génération des parents et celle des enfants. Depuis les années 1950, la tertiarisation et l’élévation des qualifications ont fait reculer les emplois d’agriculteurs et d’ouvriers et multiplié ceux de cadres et de professions intermédiaires. Comme il y a moins de places d’agriculteurs pour les fils d’agriculteurs et plus de places de cadres que de pères cadres, une partie des enfants est obligée de changer de groupe. En 2015, 13,9 % des pères étaient cadres mais 20,4 % des fils le sont, et 8,3 % des pères étaient agriculteurs contre 2,8 % des fils. L’Insee estime ainsi que 15,8 % des hommes devaient changer de groupe, soit 24,2 % de leur mobilité observée.</p><p>Cette composante structurelle, surtout ascendante, explique qu’une société puisse être plus mobile sans être plus fluide : la mobilité structurelle ne dit rien de l’égalité des chances relatives.</p></div>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Présentez deux limites des tables de mobilité comme instrument de mesure de la mobilité sociale.", enonce: "<p>Sans document.</p>",
      corrige: '<div class="copie"><p>Les tables de mobilité croisent l’origine sociale (la catégorie socioprofessionnelle du père ou de la mère) et la position sociale des individus, à partir de l’enquête FQP de l’Insee. Elles mesurent la mobilité, mais imparfaitement.</p><p>D’abord, elles utilisent un petit nombre de catégories larges. La mobilité à l’intérieur d’une catégorie est invisible : un fils d’employé peu qualifié devenu employé qualifié est classé comme immobile. De plus, ces catégories ne sont pas toutes hiérarchisées : passer d’agriculteur à artisan n’est ni une ascension ni un déclassement, d’où une mobilité dite « non verticale ».</p><p>Ensuite, les comparaisons dans le temps sont fragiles, car la valeur d’une position change : être cadre était plus rare en 1977 (5,0 % des pères des hommes interrogés) qu’en 2015 (20,4 % des fils). Enfin, le choix de l’étalon modifie les conclusions : par rapport à leur mère, 39,8 % des femmes connaissent une mobilité ascendante en 2015, mais seulement 21,8 % par rapport à leur père (Insee).</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice inventé pour le site, document Insee", t: "La mobilité des femmes et des hommes en 2015", enonce:
      '<p>Document : le tableau « En 2015 (en %) : hommes / père, femmes / mère, femmes / père » du <a href="#s3:s3-4">cours</a> (Insee Première n° 1739).</p><ol><li>Comparez la mobilité ascendante des femmes selon qu’on les compare à leur mère ou à leur père. (2 points)</li><li>À l’aide du document et de vos connaissances, montrez que la mobilité sociale des femmes présente des spécificités. (4 points)</li></ol>',
      corrige: '<ol><li>Selon l’Insee, en 2015, 39,8 % des femmes de 35 à 59 ans occupent une position plus élevée que celle de leur mère, contre 21,8 % par rapport à leur père : 18 points d’écart, soit environ 1,8 fois plus.</li><li>La mobilité des femmes dépend d’abord de l’étalon choisi. Par rapport à leur mère, elles connaissent une forte mobilité ascendante, en partie <b>structurelle</b> (34,8 % de leur mobilité) : leurs mères étaient souvent agricultrices ou employées peu qualifiées, alors qu’elles ont profité de la massification scolaire, de la tertiarisation et de la hausse de l’emploi qualifié féminin. Par rapport à leur père, en revanche, la mobilité descendante (25,0 %) l’emporte sur l’ascendante (21,8 %), et elle est bien plus forte que celle des hommes (15,0 %). À origine égale, les femmes occupent plus souvent des emplois d’employées et moins souvent des emplois de cadres : seules 35,0 % des filles de cadres sont cadres, contre 49,0 % des fils. Cela s’explique par la <b>ségrégation professionnelle</b> issue d’une socialisation différenciée, et par des carrières freinées par le temps partiel et la répartition inégale des tâches domestiques.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet inventé pour le site", t: "Montrez que l’évolution de la structure socioprofessionnelle contribue à expliquer la mobilité sociale.", enonce: '<p>Appuie-toi sur le graphique de la mobilité observée, la table de destinée de 2015 et le graphique des PCS de 1982 à 2024 (<a href="#s1:s1-3">S1</a>).</p>',
      corrige: '<p><b>Introduction.</b> Définir mobilité sociale (intergénérationnelle) et structure socioprofessionnelle. Annonce : la transformation des emplois crée une mobilité structurelle, surtout ascendante ; son ralentissement explique aussi la montée du déclassement.</p><p><b>I. La transformation des emplois impose une mobilité.</b> Tertiarisation et qualification : cadres 8,0 % de l’emploi en 1982, 23,0 % en 2024 ; ouvriers 29,9 % → 18,0 % (Insee). Écart entre marges : 13,9 % de pères cadres, 20,4 % de fils cadres. Mobilité structurelle de 15,8 %, soit 24,2 % de la mobilité des hommes en 2015.</p><p><b>II. Une mobilité surtout ascendante.</b> Recul des agriculteurs (seuls 26,7 % des fils d’agriculteurs le restent) ; recrutement des cadres dans tous les milieux (plus d’un quart sont fils d’employés ou d’ouvriers) ; mobilité ascendante des femmes par rapport à leur mère (39,8 %).</p><p><b>III. Quand la structure bouge moins, d’autres effets apparaissent.</b> La part structurelle baisse (39,6 % en 1977, 24,2 % en 2015) ; le nombre de places élevées ne suit pas le nombre d’enfants de cadres : déclassement (descendante 7,2 % → 15,0 %).</p><p><b>Conclusion.</b> La structure explique une large part de la mobilité observée, mais pas l’égalité des chances, qui se mesure par la fluidité.</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet officiel : bac 2026, sujet 26-SESJ1JA1 (dissertation) · corrigé du site", officiel: true, t: "Les ressources et configurations familiales suffisent-elles à expliquer la mobilité sociale ?", enonce: "<p>Les quatre documents du sujet officiel ne sont pas reproduits ici. Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> La famille transmet des ressources (économiques, culturelles, sociales) et s’organise de manière plus ou moins favorable à la réussite. Ces ressources expliquent-elles à elles seules les trajectoires de mobilité, ou faut-il tenir compte de la structure des emplois et du système de formation ?</p><p><b>I. Les ressources et configurations familiales expliquent une grande part de la mobilité et de la reproduction.</b><br>A. Les capitaux transmis (Bourdieu) : 49,0 % des fils de cadres sont cadres, 8,3 % des fils de non qualifiés (Insee, 2015).<br>B. Les stratégies et l’information des familles (Boudon : calcul coûts / avantages selon la position ; capital social, Granovetter).<br>C. Les configurations familiales : réussites paradoxales (Lahire), fratrie, monoparentalité et niveau de vie plus faible.</p><p><b>II. Mais elles ne suffisent pas.</b><br>A. La structure des emplois crée ou ferme des places : mobilité structurelle (24,2 % de la mobilité des hommes en 2015 ; 39,6 % en 1977).<br>B. Le niveau de formation : massification (80,1 % de bacheliers en 2025), mais paradoxe d’Anderson et inflation scolaire.<br>C. Le genre et l’action publique : mobilité des femmes différente à origine égale ; politiques scolaires et sociales.</p><p><b>Conclusion.</b> La famille est un facteur central, mais ses effets passent par l’École et dépendent de la structure des emplois : c’est la combinaison des trois qui explique la mobilité.</p><div class="marge"><b>Piège :</b> ne pas traiter seulement de la reproduction ; le sujet porte sur la <b>mobilité</b>, donc aussi sur les ascensions et les déclassements.</div>' }
  ]
};

AUTEURS.push(
  { ch: "s3", n: "Pitirim Sorokin", d: "1889-1968", th: "Pose le cadre de l’étude de la mobilité sociale (1927)", l: "<i>Social Mobility</i> (1927) : la société est un espace où l’on circule verticalement (ascension, chute) et horizontalement ; les « canaux » de la mobilité sont notamment l’école, l’armée, l’Église." },
  { ch: "s3", n: "Claude Thélot", d: "<i>Tel père, tel fils ?</i>, 1982", th: "Mobilité des Trente Glorieuses surtout structurelle, hérédité forte", l: "À partir des enquêtes FQP, montre que la hausse de la mobilité observée vient surtout de la <b>mobilité structurelle</b> et que l’hérédité sociale reste forte." },
  { ch: "s3", n: "Robert Erikson et John Goldthorpe", d: "<i>The Constant Flux</i>, 1992", th: "La fluidité sociale varie peu entre pays industrialisés", l: "Comparaison internationale des tables : une fois la structure neutralisée, la <b>fluidité</b> (chances relatives) est assez semblable d’un pays industrialisé à l’autre et change lentement." },
  { ch: "s3", n: "Louis-André Vallet", d: "sociologue, CNRS", th: "Hausse lente et régulière de la fluidité sociale en France", l: "Ses travaux sur les enquêtes FQP montrent une progression lente mais régulière de la <b>fluidité sociale</b> en France depuis les années 1950." },
  { ch: "s3", n: "Camille Peugny", d: "<i>Le Déclassement</i>, 2009", th: "Le déclassement intergénérationnel des générations nées dans les années 1960", l: "Les générations nées dans les années 1960, plus diplômées, connaissent davantage de <b>mobilité descendante</b> ; dans <i>Le Destin au berceau</i> (2013), il souligne la persistance de la reproduction." },
  { ch: "s3", n: "C. Arnold Anderson", d: "1961", th: "Paradoxe : plus diplômé que son père, pas forcément mieux placé", l: "Sociologue américain : un fils plus diplômé que son père n’occupe pas forcément une position sociale plus élevée, car la valeur des diplômes baisse quand ils se diffusent : le <b>paradoxe d’Anderson</b>." }
);

ANIMS["s3-table"] = {
  t: "Construire et lire une table de mobilité",
  h: 340,
  src: "Exemple fictif construit pour le site : 1 000 hommes classés en trois groupes (calculs vérifiés). Les vraies tables de l’Insee comptent six groupes et sont tirées de l’enquête FQP.",
  etapes: [
    { l: "On interroge 1 000 hommes de 35 à 59 ans. On les classe d’abord selon la position de leur père : c’est l’origine, en ligne (100 fils du haut, 300 du milieu, 600 du bas).", d: 4 },
    { l: "Puis selon leur propre position, en colonne. Chaque case croise les deux : c’est la table d’effectifs. Exemple : 225 hommes sont fils du bas et occupent une position du milieu.", d: 5 },
    { l: "La diagonale regroupe ceux qui sont restés dans le groupe de leur père : 545 hommes (immobilité). Tous les autres ont changé de groupe : la mobilité observée est de 455 sur 1 000, soit 45,5 %.", d: 4.5 },
    { l: "Comparons les marges : 100 pères en haut, mais 200 fils en haut. Même sans autre circulation, au moins 200 hommes devaient changer de groupe : c’est la mobilité structurelle (20 %, soit 44 % de la mobilité observée).", d: 5 },
    { l: "Table de destinée : on divise chaque case par le total de sa ligne. Sur 100 fils du haut, 60 sont restés en haut ; sur 100 fils du bas, 55,8 sont restés en bas.", d: 4.5 },
    { l: "Table de recrutement : on divise par le total de la colonne. Seuls 30 % des hommes du haut sont fils du haut (le groupe s’est élargi), mais 83,8 % des hommes du bas sont fils du bas.", d: 4.5 },
    { l: "Fluidité : un fils du haut a 4 fois plus de chances d’être en haut qu’en bas (60 ÷ 15) ; un fils du bas, 0,12 fois (40 ÷ 335). Le rapport des chances relatives vaut 4 ÷ 0,119 ≈ 33,5. Plus il est proche de 1, plus la société est fluide.", d: 5.5 }
  ],
  rendu: function (A, i, p) {
    var E = [[60, 25, 15], [100, 150, 50], [40, 225, 335]], L = [100, 300, 600], C = [200, 400, 400];
    var noms = ["Haut", "Milieu", "Bas"];
    var x0 = 96, cw = 66, y0 = 74, rh = 34, s = "";
    var D = E.map(function (r, k) { return r.map(function (v) { return 100 * v / L[k]; }); });
    var R = E.map(function (r) { return r.map(function (v, j) { return 100 * v / C[j]; }); });
    s += A.t(x0 + 1.5 * cw, 20, "Position du fils →", { t: 11.5, g: true, a: "middle", c: "canard" });
    s += A.t(6, 20, "Origine ↓", { t: 11.5, g: true, c: "corail" }) + A.t(6, 34, "(groupe du père)", { t: 10, c: "gris" });
    noms.forEach(function (n, j) { s += A.t(x0 + j * cw + cw / 2, y0 - 10, n, { t: 11.5, g: true, a: "middle", c: "canard", op: i >= 1 ? 1 : 0.35 }); });
    s += A.t(x0 + 3 * cw + 28, y0 - 10, "Total", { t: 11, g: true, a: "middle", c: "gris" });
    var qL = i === 0 ? A.s(p, 0, 0.8) : 1;
    noms.forEach(function (n, k) {
      var y = y0 + k * rh;
      s += A.t(8, y + 22, n, { t: 12, g: true, c: "corail" });
      s += A.r(x0 + 3 * cw + 4, y + 3, 48, rh - 6, { f: "corailc", r: 6, op: qL });
      s += A.t(x0 + 3 * cw + 28, y + 22, String(Math.round(L[k] * qL)), { t: 12.5, g: true, a: "middle", op: qL });
    });
    var qC = i < 3 ? 0 : i === 3 ? A.s(p, 0.05, 0.5) : 1;
    var yT = y0 + 3 * rh;
    s += A.t(8, yT + 22, "Total", { t: 11, g: true, c: "gris", op: qC });
    C.forEach(function (v, j) { s += A.r(x0 + j * cw + 4, yT + 3, cw - 8, rh - 6, { f: "canardc", r: 6, op: qC }) + A.t(x0 + j * cw + cw / 2, yT + 22, String(Math.round(v * qC)), { t: 12.5, g: true, a: "middle", op: qC }); });
    for (var k = 0; k < 3; k++) for (var j = 0; j < 3; j++) {
      var x = x0 + j * cw, y = y0 + k * rh;
      var q = i === 0 ? 0 : i === 1 ? A.s(p, k / 3, (k + 1) / 3) : 1;
      var diag = j === k, fond = "carte";
      if (i >= 2 && i <= 3) fond = diag ? "moutardec" : "canardc";
      var opF = i === 2 ? A.s(p, 0, 0.4) : 1;
      s += A.r(x + 2, y + 2, cw - 4, rh - 4, { f: "carte", s: "ligne", r: 5 });
      if (fond !== "carte") s += A.r(x + 2, y + 2, cw - 4, rh - 4, { f: fond, r: 5, op: opF });
      if (i === 4 && k < 3) s += A.r(x + 2, y + 2, cw - 4, rh - 4, { f: (k === 0 || k === 2) ? "moutardec" : "carte2", r: 5, op: A.s(p, 0.1, 0.5) * 0.9 });
      if (i === 5) s += A.r(x + 2, y + 2, cw - 4, rh - 4, { f: (j === 0 || j === 2) ? "canardc" : "carte2", r: 5, op: A.s(p, 0.1, 0.5) * 0.9 });
      if (i === 6 && (k === 0 || k === 2) && (j === 0 || j === 2)) s += A.r(x + 2, y + 2, cw - 4, rh - 4, { f: "corailc", s: "corail", r: 5, op: A.s(p, 0, 0.3) });
      var val, txt;
      if (i <= 3) { val = Math.round(E[k][j] * q); txt = String(val); }
      else if (i === 4) { var m = A.s(p, 0.15, 0.7); val = A.l(E[k][j], D[k][j], m); txt = m < 1 ? A.fr(val, 0) : A.fr(val, 1) + " %"; }
      else if (i === 5) { var m2 = A.s(p, 0.15, 0.7); val = A.l(D[k][j], R[k][j], m2); txt = A.fr(val, 1) + " %"; }
      else { txt = A.fr(D[k][j], 1) + " %"; }
      s += A.t(x + cw / 2, y + 22, txt, { t: i >= 4 ? 11.5 : 12.5, g: (i === 2 && diag) || (i === 6 && (k === 0 || k === 2) && (j === 0 || j === 2)), a: "middle", op: i === 0 ? 0 : (i === 1 ? q : 1) });
    }
    var yb = yT + rh + 14;
    if (i === 0) {
      var tot = 0;
      L.forEach(function (v, k) { s += A.r(20 + 320 * tot / 1000, yb + 8, 320 * v / 1000 * qL, 22, { f: ["corail", "moutarde", "canard"][k], r: 3 }) + A.t(20 + 320 * (tot + v / 2) / 1000, yb + 48, noms[k] + " : " + v, { t: 11, a: "middle", c: "gris", op: qL }); tot += v; });
    } else if (i === 1) {
      s += A.t(180, yb + 22, "Lecture : 225 hommes sont fils du bas", { t: 12, a: "middle", op: A.s(p, 0.75, 1) }) + A.t(180, yb + 40, "et occupent une position du milieu.", { t: 12, a: "middle", op: A.s(p, 0.75, 1) });
    } else if (i === 2) {
      var g = A.s(p, 0.3, 1);
      s += A.jauge(20, yb + 18, 320, 545 * g, 1000, { c: "moutarde", l: "Immobilité (diagonale)", val: Math.round(545 * g) + " / 1 000" });
      s += A.jauge(20, yb + 52, 320, 455 * g, 1000, { c: "canard", l: "Mobilité observée (hors diagonale)", val: A.fr(45.5 * g, 1) + " %" });
    } else if (i === 3) {
      var g3 = A.s(p, 0.45, 1);
      s += A.t(180, yb + 14, "½ × (|100 − 200| + |300 − 400| + |600 − 400|) = 200", { t: 12, g: true, a: "middle", op: g3 });
      s += A.jauge(20, yb + 40, 320, 200 * g3, 455, { c: "corail", l: "Mobilité structurelle dans la mobilité observée", val: Math.round(200 * g3) + " / 455" });
    } else if (i === 4) {
      s += A.fl(14, y0 + rh, 300, y0 + rh, { c: "corail", p: A.s(p, 0, 0.3), sw: 2 }) + A.t(180, yb + 22, "Lecture en ligne : chaque ligne totalise 100 %.", { t: 12, a: "middle", op: A.s(p, 0.5, 0.9) }) + A.t(180, yb + 42, "« Sur 100 fils du bas, 55,8 restent en bas. »", { t: 12, g: true, a: "middle", op: A.s(p, 0.6, 1) });
    } else if (i === 5) {
      s += A.fl(x0 + 3 * cw + 1, y0 - 2, x0 + 3 * cw + 1, yT + 2, { c: "canard", p: A.s(p, 0, 0.3), sw: 2 }) + A.t(180, yb + 22, "Lecture en colonne : chaque colonne totalise 100 %.", { t: 12, a: "middle", op: A.s(p, 0.5, 0.9) }) + A.t(180, yb + 42, "« Sur 100 hommes du bas, 83,8 sont fils du bas. »", { t: 12, g: true, a: "middle", op: A.s(p, 0.6, 1) });
    } else {
      var g6 = A.s(p, 0.25, 0.6), g7 = A.s(p, 0.55, 0.9);
      s += A.t(180, yb + 6, "Fils du haut : 60 ÷ 15 = 4", { t: 11.5, a: "middle", op: g6 }) + A.t(180, yb + 22, "Fils du bas : 40 ÷ 335 ≈ 0,119", { t: 11.5, a: "middle", op: g6 });
      s += A.t(180, yb + 44, "Rapport des chances relatives ≈ 33,5", { t: 15, g: true, a: "middle", c: "corail", op: g7, f: true });
      s += A.t(180, yb + 62, "(France 2015, vraies données : 34,7)", { t: 10.5, a: "middle", c: "gris", op: g7 });
    }
    return s;
  }
};
