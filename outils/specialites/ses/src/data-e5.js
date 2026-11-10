GRAPHES["e5-bce"] = {
  type: "lignes", t: "Le taux de la facilité de dépôt de la BCE, 2021-2026",
  s: "Taux en vigueur à la fin de chaque trimestre, en %. Touche le graphique pour lire un trimestre.",
  src: "Source : Banque centrale européenne, taux directeurs (dates d’effet des décisions). Dernière valeur : 2,50 % depuis le 16 septembre 2026 (taux inchangé le 29 octobre 2026).",
  unite: " %", pasX: 4, h: 260, min: -1, max: 5, dec: 2,
  x: ["2021 T1","T2","T3","T4","2022 T1","T2","T3","T4","2023 T1","T2","T3","T4","2024 T1","T2","T3","T4","2025 T1","T2","T3","T4","2026 T1","T2","T3","T4"],
  series: [{ n: "Facilité de dépôt", c: 1, v: [-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.75,2,3,3.5,4,4,4,3.75,3.5,3,2.5,2,2,2,2,2.25,2.5,2.5] }]
};
GRAPHES["e5-budget"] = {
  type: "hbarres", t: "Les finances publiques françaises face aux règles européennes",
  s: "En % du PIB, 2025, comparé aux valeurs de référence des traités.",
  src: "Sources : Insee, comptes des administrations publiques (première estimation, mars 2026) : déficit 5,1 %, dette 115,6 % du PIB ; valeurs de référence du traité de Maastricht (1992) : 3 % et 60 %.",
  unite: " %", lab: 120,
  cats: ["Déficit public", "Dette publique"],
  series: [{ n: "France 2025", v: [5.1, 115.6], c: 2 }, { n: "Référence européenne", v: [3, 60], c: 1 }]
};

CHAINES["e5-marche"] = { t: "Les effets du marché unique sur la croissance", e: [
  { t: "Suppression des obstacles aux échanges : libre circulation des biens, des services, des capitaux et des personnes", k: "cause" },
  { f: [{ t: "Marché plus vaste : économies d’échelle, spécialisation" }, { t: "Concurrence accrue : baisse des prix, incitation à innover" }], a: "donc" },
  { t: "Gains de productivité, plus d’échanges et d’investissements entre pays membres", a: "donc" },
  { t: "Croissance plus forte, mais gains inégalement répartis entre régions et secteurs", k: "effet", a: "donc" }
] };
CHAINES["e5-monetaire"] = { t: "Comment la politique monétaire agit sur la conjoncture", e: [
  { t: "La banque centrale relève ses taux directeurs", k: "cause" },
  { t: "Les banques se refinancent plus cher et relèvent leurs taux de crédit", a: "donc" },
  { t: "Ménages et entreprises empruntent moins : immobilier, investissement et consommation ralentissent", a: "donc" },
  { t: "La demande ralentit : les prix augmentent moins vite, mais la croissance et l’emploi peuvent ralentir aussi", k: "effet", a: "donc" }
] };
CHAINES["e5-budgetaire"] = { t: "Comment la politique budgétaire agit sur la conjoncture", e: [
  { f: [{ t: "L’État augmente ses dépenses (investissement, prestations)", k: "cause" }, { t: "ou baisse les impôts", k: "cause" }] },
  { t: "La demande augmente directement, ou via le revenu disponible des ménages", a: "donc" },
  { t: "Les entreprises produisent et embauchent : de nouveaux revenus sont dépensés (multiplicateur)", a: "donc" },
  { t: "Croissance et emploi soutenus, mais déficit et dette publics en hausse", k: "effet", a: "donc" }
] };
CHAINES["e5-choc"] = { t: "Le problème du choc asymétrique dans la zone euro", e: [
  { t: "Un choc frappe un seul pays (éclatement d’une bulle, perte d’un secteur clé)", k: "cause" },
  { t: "Il aurait besoin de taux plus bas ou d’une dévaluation", a: "or" },
  { t: "La BCE fixe un taux unique adapté à la moyenne de la zone ; la monnaie nationale n’existe plus", k: "frein", a: "mais" },
  { t: "Il ne reste que le budget national, encadré par les règles européennes", k: "frein", a: "et" },
  { t: "Récession et chômage plus longs dans ce pays : divergences dans la zone", k: "effet", a: "donc" }
] };

ANIMS["e5-transmission"] = {
  t: "Comment la BCE a combattu l’inflation de 2022",
  h: 320,
  src: "Sources : BCE (taux de la facilité de dépôt : −0,50 % jusqu’en juillet 2022, 4,00 % de septembre 2023 à juin 2024) ; Eurostat (inflation de la zone euro : 10,6 % en octobre 2022, 2,4 % en moyenne en 2024). Délais de transmission : plusieurs trimestres.",
  etapes: [
    { l: "Automne 2022 : l’inflation de la zone euro atteint 10,6 % (octobre), loin de l’objectif de 2 % de la BCE.", d: 3 },
    { l: "La BCE relève ses taux directeurs : le taux de la facilité de dépôt passe de −0,50 % (juillet 2022) à 4 % (septembre 2023).", d: 4 },
    { l: "Les banques se refinancent plus cher : elles relèvent les taux de leurs crédits aux ménages et aux entreprises.", d: 3 },
    { l: "On emprunte moins : achats de logements, investissement des entreprises et consommation à crédit ralentissent.", d: 3.5 },
    { l: "La demande ralentit, les prix augmentent moins vite : l’inflation retombe à 2,4 % en moyenne en 2024. Le prix à payer : une croissance plus faible.", d: 4 },
    { l: "À l’inverse, quand l’inflation est maîtrisée et l’activité faible, la BCE baisse ses taux pour relancer le crédit : de juin 2024 à juin 2025, de 4 % à 2 %.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", et = [["Taux directeur de la BCE", 30], ["Taux des crédits bancaires", 98], ["Crédit, investissement, consommation", 166], ["Inflation", 234]];
    et.forEach(function (e, k) {
      var actif = i >= 5 ? true : (k === 0 ? i >= 1 : k === 3 ? i === 0 || i >= 4 : i >= k + 1);
      s += A.boite(12, e[1], 168, 46, e[0], { k: actif ? (k === 3 ? "effet" : "cause") : "neutre", t: 12.5, g: true });
      if (k < 3) {
        var q = i >= 5 ? 1 : (i > k + 1 ? 1 : (i === k + 1 ? A.s(p, 0.5, 1) : 0));
        s += A.fl(96, e[1] + 48, 96, e[1] + 66, { c: i >= 5 ? "vert" : "corail", sw: 2.4, p: q });
      }
    });
    var taux = i === 0 ? -0.5 : i === 1 ? A.l(-0.5, 4, A.s(p, 0, 0.9)) : i < 5 ? 4 : A.l(4, 2, A.s(p, 0, 0.9));
    s += A.jauge(196, 50, 150, taux + 1, 6, { c: "canard", l: "facilité de dépôt", val: (taux > 0 ? "+" : "") + A.fr(taux, 2) + " %" });
    var cred = i < 2 ? 0.3 : i === 2 ? A.l(0.3, 0.8, A.s(p, 0, 1)) : i < 5 ? 0.8 : A.l(0.8, 0.5, A.s(p, 0, 1));
    s += A.jauge(196, 118, 150, cred, 1, { c: "canard", l: "coût du crédit" });
    var dem = i < 3 ? 0.85 : i === 3 ? A.l(0.85, 0.45, A.s(p, 0, 1)) : i < 5 ? 0.45 : A.l(0.45, 0.65, A.s(p, 0, 1));
    s += A.jauge(196, 186, 150, dem, 1, { c: "moutarde", l: "demande" });
    var inf = i < 4 ? 10.6 : i === 4 ? A.l(10.6, 2.4, A.s(p, 0, 1)) : 2.4;
    s += A.jauge(196, 254, 150, inf, 12, { c: "corail", l: "inflation", val: A.fr(inf, 1) + " %" });
    s += '<line x1="' + (196 + 150 * 2 / 12) + '" x2="' + (196 + 150 * 2 / 12) + '" y1="248" y2="270" style="stroke:var(--encre);stroke-width:2"/>' + A.t(196 + 150 * 2 / 12, 284, "objectif 2 %", { t: 10.5, a: "middle", c: "gris" });
    if (i === 5) s += A.t(180, 312, "le même mécanisme joue dans l’autre sens", { t: 12, g: true, a: "middle", c: "vert", op: A.s(p, 0.5, 1) });
    return s;
  }
};

ANIMS["e5-choc"] = {
  t: "Un choc asymétrique dans une union monétaire",
  h: 330,
  src: "Schéma de principe (valeurs illustratives). Repère réel : en 2013, taux de chômage de 26,1 % en Espagne et de 5,2 % en Allemagne (Eurostat), avec le même taux directeur de la BCE.",
  etapes: [
    { l: "Dans la zone euro, 21 pays depuis le 1er janvier 2026, une seule politique monétaire : la BCE fixe le même taux pour tous.", d: 3 },
    { l: "Un choc asymétrique frappe le pays A seulement (par exemple l’éclatement d’une bulle immobilière) : son activité chute, son chômage monte.", d: 3.5 },
    { l: "Au même moment, le pays B est en surchauffe : son économie tourne à plein régime et ses prix accélèrent.", d: 3 },
    { l: "A aurait besoin d’une baisse des taux, B d’une hausse. La BCE fixe un taux adapté à la moyenne de la zone : il ne convient vraiment à aucun des deux.", d: 4 },
    { l: "A ne peut pas dévaluer : il n’a plus de monnaie nationale. Il peut augmenter ses dépenses publiques, mais les règles européennes encadrent son déficit.", d: 4 },
    { l: "Résultat : des écarts qui durent. Remèdes discutés : coordonner les budgets, faciliter la mobilité des travailleurs, financer des plans communs comme NextGenerationEU (2020).", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "";
    var bce = i === 0 ? A.s(p, 0, 0.6) : 1;
    s += A.boite(120, 8, 120, 40, "BCE : un taux unique", { k: "cause", t: 12.5, g: true, op: bce });
    s += A.fl(160, 50, 90, 86, { c: "gris", p: bce }) + A.fl(200, 50, 270, 86, { c: "gris", p: bce });
    [["Pays A", 20], ["Pays B", 196]].forEach(function (P, j) {
      var x = P[1];
      s += A.r(x, 88, 144, 170, { f: "carte", s: j === 0 && i >= 1 ? "corail" : (j === 1 && i >= 2 ? "moutarde" : "ligne"), r: 12, sw: 2 });
      s += A.t(x + 72, 110, P[0], { t: 15, g: true, a: "middle", f: true });
      var act = 0.6, cho = 0.35, inf = 0.3;
      if (j === 0 && i >= 1) { var q = i === 1 ? A.s(p, 0, 1) : 1; act = A.l(0.6, 0.2, q); cho = A.l(0.35, 0.8, q); inf = A.l(0.3, 0.12, q); }
      if (j === 1 && i >= 2) { var q2 = i === 2 ? A.s(p, 0, 1) : 1; act = A.l(0.6, 0.92, q2); cho = A.l(0.35, 0.2, q2); inf = A.l(0.3, 0.8, q2); }
      s += A.jauge(x + 12, 140, 120, act, 1, { c: "canard", l: "activité" });
      s += A.jauge(x + 12, 180, 120, cho, 1, { c: "corail", l: "chômage" });
      s += A.jauge(x + 12, 220, 120, inf, 1, { c: "moutarde", l: "inflation" });
      if (i >= 3) {
        var q3 = i === 3 ? A.s(p, 0, 0.6) : 1;
        s += A.t(x + 72, 248, j === 0 ? "besoin : taux ↓" : "besoin : taux ↑", { t: 11.5, g: true, a: "middle", c: j === 0 ? "corail" : "moutarde", op: q3 });
      }
    });
    if (i === 3) s += A.t(180, 74, "taux moyen : trop haut pour A, trop bas pour B", { t: 11.5, g: true, a: "middle", c: "encre", op: A.s(p, 0.4, 1), h: true });
    if (i >= 4) {
      var q4 = i === 4 ? A.s(p, 0, 0.7) : 1;
      s += A.r(20, 268, 144, 18, { f: "carte2", r: 5, op: q4 }) + A.r(20, 268, 144 * 0.6 * q4, 18, { f: "corail", r: 5 }) + A.t(92, 300, "budget de A : relance encadrée", { t: 11, a: "middle", c: "gris", op: q4 });
      s += '<line x1="' + (20 + 144 * 0.6) + '" x2="' + (20 + 144 * 0.6) + '" y1="262" y2="292" style="stroke:var(--encre);stroke-width:2;opacity:' + q4 + '"/>';
      s += A.t(268, 282, "pas de dévaluation possible", { t: 11.5, g: true, a: "middle", c: "corail", op: q4 });
    }
    if (i === 5) s += A.t(180, 322, "divergences durables entre pays", { t: 13, g: true, a: "middle", c: "encre", op: A.s(p, 0.3, 0.8) });
    return s;
  }
};

CH.e5 = {
  chapo: "Une monnaie pour 21 pays, une Banque centrale indépendante, mais 21 budgets nationaux tenus par des règles communes : la zone euro est une construction unique au monde. Ce chapitre explique ce que le marché unique a changé, comment Bruxelles surveille la concurrence, et pourquoi piloter la conjoncture à plusieurs est si difficile.",
  essentiel: [
    "L’<b>intégration européenne</b> repose sur le <b>marché unique</b> (1993 : libre circulation des biens, services, capitaux et personnes) et sur la <b>zone euro</b> (1999 ; 21 pays depuis 2026). Le marché unique stimule la croissance par la concurrence, les économies d’échelle et les échanges.",
    "La <b>politique européenne de la concurrence</b> sanctionne les ententes et les abus de position dominante, contrôle les fusions et les aides d’État, au profit des consommateurs ; elle est critiquée pour freiner l’émergence de « champions » européens.",
    "La <b>politique monétaire</b> (taux directeurs) et la <b>politique budgétaire</b> (dépenses, impôts) agissent sur la <b>conjoncture</b> en modifiant la demande globale.",
    "Dans la zone euro, la politique monétaire est <b>unique</b> et conduite par une <b>BCE indépendante</b> ; la politique budgétaire reste <b>nationale</b> mais <b>encadrée par les traités</b> (3 % de déficit, 60 % de dette).",
    "D’où deux difficultés : le <b>défaut de coordination</b> entre budgets nationaux et les <b>chocs asymétriques</b>, qui ne frappent qu’une partie de la zone alors que le taux est le même pour tous."
  ],
  chiffres: [
    { n: "21", l: "pays membres de la zone euro depuis l’entrée de la Bulgarie le 1er janvier 2026.", s: "Banque de France ; Commission européenne" },
    { n: "10,6 %", l: "d’inflation dans la zone euro en octobre 2022 ; la BCE a relevé son taux de dépôt de −0,50 % à 4 % en un an.", s: "Eurostat ; BCE" },
    { n: "5,1 %", l: "du PIB : le déficit public de la France en 2025, pour une dette de 115,6 % du PIB.", s: "Insee, mars 2026" }
  ],
  objectifs: [
    { bo: "Connaître les grandes caractéristiques de l’intégration européenne (marché unique et zone euro) ; comprendre les effets du marché unique sur la croissance.", clair: "Retracer les étapes du marché unique et de l’euro ; expliquer comment le marché unique favorise la croissance.", voir: "e5-1" },
    { bo: "Comprendre les objectifs, les modalités et les limites de la politique européenne de la concurrence.", clair: "Dire pourquoi l’Union protège la concurrence, avec quels outils, et ce qu’on lui reproche.", voir: "e5-2" },
    { bo: "Comprendre comment la politique monétaire et la politique budgétaire agissent sur la conjoncture.", clair: "Dérouler les mécanismes d’une hausse de taux et d’une relance budgétaire.", voir: "e5-3" },
    { bo: "Savoir que la politique monétaire dans la zone euro, conduite de façon indépendante par la Banque centrale européenne, est unique alors que la politique budgétaire est du ressort de chaque pays membre mais contrainte par les traités européens ; comprendre les difficultés soulevées par cette situation (défaut de coordination, chocs asymétriques).", clair: "Expliquer la répartition des rôles dans la zone euro et pourquoi elle pose des problèmes de coordination et face aux chocs asymétriques.", voir: "e5-4" }
  ],
  notions: ["intégration européenne", "marché unique", "union douanière", "zone euro", "politique de la concurrence", "entente", "abus de position dominante", "contrôle des concentrations", "aides d’État", "politique monétaire", "taux directeur", "inflation", "politique budgétaire", "multiplicateur", "stabilisateurs automatiques", "déficit public", "dette publique", "conjoncture", "Banque centrale européenne", "indépendance de la banque centrale", "Pacte de stabilité et de croissance", "coordination des politiques", "choc asymétrique"],
  sections: [
    { id: "e5-1", t: "L’intégration européenne : marché unique et zone euro", h:
      '<div class="def"><b>Intégration économique</b> — processus par lequel des pays suppriment progressivement les obstacles à leurs échanges, jusqu’à mettre en commun des politiques. Bela Balassa (1961) en distinguait les étapes : zone de libre-échange, union douanière, marché commun, union économique et monétaire.</div>' +
      '<div class="tbl"><table><thead><tr><th>Date</th><th>Étape</th></tr></thead><tbody>' +
      '<tr><td>1957</td><td>Traité de Rome : Communauté économique européenne (six pays)</td></tr>' +
      '<tr><td>1968</td><td>Union douanière : plus de droits de douane entre membres, un tarif extérieur commun</td></tr>' +
      '<tr><td>1986</td><td>Acte unique européen : programme d’achèvement du marché intérieur</td></tr>' +
      '<tr><td>1er janvier 1993</td><td><b>Marché unique</b> : libre circulation des biens, des services, des capitaux et des personnes</td></tr>' +
      '<tr><td>1992</td><td>Traité de Maastricht : Union européenne, projet de monnaie unique, critères de convergence</td></tr>' +
      '<tr><td>1er janvier 1999</td><td><b>Euro</b> pour 11 pays (pièces et billets le 1er janvier 2002)</td></tr>' +
      '<tr><td>1er janvier 2026</td><td>La Bulgarie devient le 21e pays de la zone euro (l’Union compte 27 membres)</td></tr>' +
      '</tbody></table></div>' +
      '<div class="def"><b>Marché unique</b> — espace sans frontières intérieures où circulent librement les biens, les services, les capitaux et les personnes, avec des règles communes (normes, concurrence).</div>' +
      '<div data-chain="e5-marche"></div>' +
      '<p>Le marché unique favorise la croissance par les mécanismes du commerce entre pays comparables (<a href="#e2:e2-3">É2</a>) : un marché de plus de 400 millions de consommateurs permet des économies d’échelle ; la concurrence pousse à baisser les prix et à innover ; les entreprises s’implantent dans les autres pays membres. La libre circulation des capitaux facilite le financement des investissements.</p>' +
      '<div class="ex"><p>Avant 1993, un camion qui traversait l’Europe s’arrêtait à chaque frontière pour des contrôles et des formalités douanières. Avec le marché unique, ces contrôles disparaissent, et une norme technique reconnue dans un pays permet de vendre dans tous les autres.</p></div>' +
      '<div class="attn"><p>Les gains sont réels mais inégalement répartis : certaines régions et certains secteurs exposés à la concurrence ont perdu des emplois, et le marché des services reste moins intégré que celui des biens.</p></div>' },

    { id: "e5-2", t: "La politique européenne de la concurrence", h:
      '<p class="lede">La Commission européenne veille à ce que la concurrence ne soit pas faussée dans le marché unique. Objectif : des prix plus bas, plus de choix et plus d’innovation pour les consommateurs, et des règles du jeu égales pour toutes les entreprises.</p>' +
      '<div class="tbl"><table><thead><tr><th>Outil</th><th>Ce qui est interdit ou contrôlé</th><th>Exemple</th></tr></thead><tbody>' +
      '<tr><td><b>Ententes</b></td><td>Accords entre concurrents pour fixer les prix ou se partager les marchés</td><td>En 2016, amende de 2,93 milliards d’euros contre un cartel de constructeurs de camions qui s’étaient entendus sur les prix.</td></tr>' +
      '<tr><td><b>Abus de position dominante</b></td><td>Une entreprise dominante qui évince ses concurrents</td><td>Google sanctionné de 2,42 milliards d’euros en 2017 pour avoir favorisé son comparateur de prix ; amende confirmée par la Cour de justice de l’Union le 10 septembre 2024.</td></tr>' +
      '<tr><td><b>Contrôle des concentrations</b></td><td>Fusions qui réduiraient trop la concurrence</td><td>Fusion Siemens-Alstom (trains à grande vitesse, signalisation) interdite le 6 février 2019.</td></tr>' +
      '<tr><td><b>Aides d’État</b></td><td>Aides publiques qui avantagent certaines entreprises</td><td>Avantages fiscaux accordés par l’Irlande à Apple : récupération de 13 milliards d’euros, confirmée par la Cour de justice le 10 septembre 2024.</td></tr>' +
      '</tbody></table></div>' +
      '<h3>Les limites</h3>' +
      '<ul><li><b>Les « champions européens »</b> : en interdisant certaines fusions, l’Union empêcherait l’émergence de grandes entreprises capables de rivaliser avec les géants américains et chinois. Le refus de la fusion Siemens-Alstom a relancé ce débat ; le rapport de Mario Draghi sur la compétitivité européenne (septembre 2024) appelle à mieux tenir compte de l’innovation et de la taille mondiale.</li><li><b>La lenteur</b> : les procédures durent des années, alors que les marchés numériques évoluent très vite ; d’où le règlement sur les marchés numériques (DMA, 2022), qui fixe des obligations à l’avance aux très grandes plateformes.</li><li><b>Les aides d’État encadrées</b> limitent les politiques industrielles nationales, alors que les États-Unis et la Chine subventionnent massivement leurs industries.</li></ul>' +
      '<div class="ex"><p>Le sujet de dissertation du bac 2026 (jour 2) portait exactement sur ce point : « Dans quelle mesure la politique européenne de la concurrence atteint-elle ses objectifs ? ». Voir l’onglet <a href="#e5/bac">Sujets bac</a>.</p></div>' },

    { id: "e5-3", t: "Politique monétaire et politique budgétaire face à la conjoncture", h:
      '<div class="def"><b>Conjoncture</b> — situation économique à court terme : croissance, emploi, inflation. Les politiques conjoncturelles cherchent à la stabiliser : soutenir l’activité en récession, freiner l’inflation en surchauffe.</div>' +
      '<h3>1. La politique monétaire</h3>' +
      '<p>La banque centrale fixe ses <b>taux directeurs</b>, les taux auxquels les banques se refinancent auprès d’elle ou y déposent leurs liquidités. Ils se transmettent aux taux des crédits, donc à la demande.</p>' +
      '<div data-anim="e5-transmission"></div>' +
      '<div data-chain="e5-monetaire"></div>' +
      '<div data-graph="e5-bce"></div>' +
      '<p>Après la hausse de 2022-2023 puis les baisses de 2024-2025, la BCE a de nouveau relevé ses taux en juin et en septembre 2026 face au regain d’inflation : le taux de la facilité de dépôt est de 2,50 % depuis le 16 septembre 2026.</p>' +
      '<h3>2. La politique budgétaire</h3>' +
      '<p>L’État agit sur la demande par ses <b>dépenses</b> (investissements, prestations, salaires des fonctionnaires) et ses <b>recettes</b> (impôts, cotisations). Un <b>déficit public</b> apparaît quand les dépenses dépassent les recettes ; il s’ajoute à la <b>dette publique</b>.</p>' +
      '<div data-chain="e5-budgetaire"></div>' +
      '<p>L’effet est amplifié par le <b>multiplicateur keynésien</b> : un euro de dépense publique devient un revenu qui sera en partie dépensé, créant d’autres revenus. Il est réduit si une partie de la demande part en importations ou si les ménages épargnent par crainte des impôts futurs. Les <b>stabilisateurs automatiques</b> jouent sans décision nouvelle : en récession, les recettes fiscales baissent et les allocations chômage augmentent, ce qui soutient la demande.</p>' +
      '<div class="ex"><p>Pendant la crise sanitaire, la France a pris en charge le chômage partiel et lancé le plan France Relance (100 milliards d’euros, 2020) ; la BCE a lancé un programme d’achats d’urgence. En 2021, le PIB rebondit de 6,9 % (Insee).</p></div>' },

    { id: "e5-4", t: "Une monnaie, vingt et un budgets : les difficultés de la zone euro", h:
      '<h3>Une politique monétaire unique et indépendante</h3>' +
      '<p>La <b>Banque centrale européenne</b> (BCE), à Francfort, conduit la politique monétaire de toute la zone euro. Son mandat principal est la <b>stabilité des prix</b> : une inflation de 2 % à moyen terme. Elle est <b>indépendante</b> : ni les gouvernements ni les institutions européennes ne peuvent lui donner d’instructions. L’idée est de la protéger de la tentation de financer les États ou de stimuler l’économie avant une élection au prix de l’inflation.</p>' +
      '<h3>Des politiques budgétaires nationales mais encadrées</h3>' +
      '<p>Chaque État décide de son budget, mais les traités l’encadrent : le traité de Maastricht (1992) fixe des valeurs de référence de 3 % du PIB pour le déficit public et de 60 % pour la dette ; le Pacte de stabilité et de croissance (1997), réformé en 2024, organise la surveillance et peut aboutir à une procédure pour déficit excessif, ouverte contre la France en juillet 2024.</p>' +
      '<div data-graph="e5-budget"></div>' +
      '<p>Pourquoi ces règles ? Dans une union monétaire, un État trop endetté peut provoquer une crise qui touche tous les autres (comme la Grèce en 2010) et pousser la BCE à le secourir : les règles budgétaires évitent ce comportement de <b>passager clandestin</b>.</p>' +
      '<h3>Deux difficultés</h3>' +
      '<p><b>1. Le défaut de coordination.</b> Chaque État fixe son budget en fonction de sa situation, sans tenir compte des effets sur ses voisins (une relance allemande profite aussi aux exportations françaises). Le <b>policy mix</b> (combinaison des politiques monétaire et budgétaire) de la zone n’est donc le résultat d’aucune décision d’ensemble ; le budget de l’Union reste petit (environ 1 % de son revenu national).</p>' +
      '<p><b>2. Les chocs asymétriques.</b></p>' +
      '<div class="def"><b>Choc asymétrique</b> — événement qui touche un pays ou un groupe de pays de la zone, et pas les autres (ou pas de la même façon).</div>' +
      '<div data-anim="e5-choc"></div>' +
      '<div data-chain="e5-choc"></div>' +
      '<div class="aut"><span class="mono">RM</span><span class="an">Robert Mundell<small>1932-2021 · Nobel 1999</small></span><span class="ad">Sa théorie des <b>zones monétaires optimales</b> (1961) montre qu’une monnaie commune fonctionne bien si les pays subissent des chocs semblables, ou s’ils peuvent s’ajuster autrement : mobilité des travailleurs, flexibilité des salaires, transferts budgétaires.</span></div>' +
      '<div class="ex"><p>Après l’éclatement de la bulle immobilière espagnole en 2008, le taux de chômage atteint 26,1 % en Espagne en 2013, contre 5,2 % en Allemagne (Eurostat), avec le même taux directeur pour les deux. En 2020, face à la crise sanitaire, l’Union lance un plan commun, <b>NextGenerationEU</b> (750 milliards d’euros, aux prix de 2018), financé par un emprunt européen : une forme nouvelle de solidarité budgétaire.</p></div>' +
      '<div class="ex"><p>La partie 1 de l’épreuve composée du bac 2026 (jour 1) demandait d’expliquer une difficulté soulevée par les chocs asymétriques dans la zone euro. Corrigé dans l’onglet <a href="#e5/bac">Sujets bac</a>.</p></div>' }
  ],
  pieges: [
    { f: "« Marché unique et zone euro, c’est la même chose. »", v: "Le marché unique concerne les 27 pays de l’Union (et quelques autres) ; la zone euro, les 21 pays qui ont adopté l’euro. La Suède ou la Pologne sont dans le marché unique sans être dans la zone euro." },
    { f: "« La BCE fixe les budgets des États. »", v: "Elle conduit la politique monétaire ; les budgets sont nationaux, encadrés par les règles européennes que surveillent la Commission et le Conseil." },
    { f: "« Une hausse des taux fait baisser les prix immédiatement. »", v: "La transmission prend plusieurs trimestres : crédit, puis demande, puis prix." },
    { f: "« La politique de la concurrence protège les entreprises européennes. »", v: "Elle protège la concurrence et les consommateurs, parfois contre des entreprises européennes (Siemens-Alstom)." },
    { f: "« Un choc asymétrique est un choc très fort. »", v: "C’est un choc qui ne touche pas tous les pays de la même façon, quelle que soit son intensité." },
    { f: "« Les critères de 3 % et 60 % portent sur la croissance. »", v: "Ils portent sur le déficit public et la dette publique, en pourcentage du PIB." }
  ],
  retenir:
    '<h3>Repères</h3><ul><li>1957 traité de Rome ; 1968 union douanière ; 1986 Acte unique ; 1993 marché unique ; 1992 Maastricht ; 1999 euro (2002 pièces et billets) ; 2026 : 21 pays dans la zone euro.</li></ul>' +
    '<h3>Définitions</h3><ul>' +
    '<li><b>Marché unique</b> : libre circulation des biens, services, capitaux, personnes ; effets sur la croissance : économies d’échelle, concurrence, échanges.</li>' +
    '<li><b>Politique de la concurrence</b> : ententes, abus de position dominante, concentrations, aides d’État ; limites : champions européens, lenteur, politique industrielle.</li>' +
    '<li><b>Politique monétaire</b> : taux directeurs → crédit → demande → inflation. <b>Politique budgétaire</b> : dépenses et impôts → demande ; multiplicateur ; stabilisateurs automatiques.</li>' +
    '<li><b>BCE</b> indépendante, mandat de stabilité des prix (2 %). <b>Règles budgétaires</b> : 3 % de déficit, 60 % de dette ; Pacte de stabilité (1997, réformé en 2024).</li>' +
    '<li><b>Difficultés</b> : défaut de coordination ; <b>chocs asymétriques</b> (Mundell, zones monétaires optimales, 1961) ; réponse : NextGenerationEU (2020).</li></ul>' +
    '<h3>Chiffres à citer</h3><ul><li>Inflation zone euro 10,6 % (octobre 2022) ; taux de dépôt −0,50 % → 4 % (2022-2023) → 2 % (juin 2025) → 2,50 % (septembre 2026).</li><li>France 2025 : déficit 5,1 % du PIB, dette 115,6 % (Insee).</li></ul>',
  chainesFiche: ["e5-marche", "e5-monetaire", "e5-budgetaire", "e5-choc"],
  quiz: [
    { q: "Le marché unique européen est entré en vigueur le…", c: ["1er janvier 1993", "1er janvier 1999", "25 mars 1957", "1er janvier 2002"], r: 0, e: "1999 : euro (monnaie scripturale) ; 2002 : pièces et billets ; 1957 : traité de Rome.", s: "e5-1" },
    { q: "Combien de pays utilisent l’euro depuis le 1er janvier 2026 ?", c: ["21", "27", "19", "11"], r: 0, e: "La Bulgarie est devenue le 21e membre ; l’Union compte 27 pays.", s: "e5-1" },
    { q: "Le marché unique favorise la croissance notamment par…", c: ["les économies d’échelle et la concurrence", "la hausse des droits de douane", "la création de monopoles nationaux", "la baisse des salaires"], r: 0, e: "Un marché plus vaste et plus concurrentiel pousse à produire moins cher et à innover.", s: "e5-1" },
    { q: "Un accord secret entre concurrents pour fixer leurs prix est…", c: ["une entente", "un abus de position dominante", "une aide d’État", "une concentration"], r: 0, e: "Exemple : le cartel des camions sanctionné en 2016.", s: "e5-2" },
    { q: "En 2019, la Commission européenne a interdit…", c: ["la fusion Siemens-Alstom", "l’entrée de la Bulgarie dans l’euro", "les aides du plan de relance", "le rachat de BNP Paribas"], r: 0, e: "Elle jugeait que la fusion réduisait trop la concurrence dans le ferroviaire.", s: "e5-2" },
    { q: "Une critique adressée à la politique européenne de la concurrence est qu’elle…", c: ["freine l’émergence de champions européens de taille mondiale", "fait monter les prix", "favorise les ententes", "supprime le marché unique"], r: 0, e: "Débat relancé par Siemens-Alstom et le rapport Draghi (2024).", s: "e5-2" },
    { q: "Quand la BCE relève ses taux directeurs, elle cherche en principe à…", c: ["ralentir la demande pour freiner l’inflation", "relancer la consommation", "augmenter le déficit public", "dévaluer l’euro"], r: 0, e: "Crédit plus cher → moins d’emprunts → demande et inflation en recul.", s: "e5-3" },
    { q: "Entre juillet 2022 et septembre 2023, le taux de la facilité de dépôt de la BCE est passé de…", c: ["−0,50 % à 4 %", "4 % à −0,50 %", "0 % à 10,6 %", "2 % à 3 %"], r: 0, e: "Pour combattre une inflation qui a atteint 10,6 % en octobre 2022.", s: "e5-3" },
    { q: "Le multiplicateur budgétaire signifie que…", c: ["une dépense publique crée des revenus qui sont en partie dépensés à leur tour", "la dette double tous les ans", "les impôts augmentent automatiquement", "les prix montent avec la dépense"], r: 0, e: "D’où un effet sur le PIB supérieur à la dépense initiale, réduit par les importations et l’épargne.", s: "e5-3" },
    { q: "Les stabilisateurs automatiques…", c: ["soutiennent la demande en récession sans nouvelle décision", "sont des taux fixés par la BCE", "obligent les États à réduire leur dette", "sont des taxes européennes"], r: 0, e: "En récession, les impôts rentrent moins et les allocations augmentent.", s: "e5-3" },
    { q: "Le mandat principal de la BCE est…", c: ["la stabilité des prix", "le plein emploi", "l’équilibre budgétaire des États", "la croissance la plus forte possible"], r: 0, e: "Une inflation de 2 % à moyen terme.", s: "e5-4" },
    { q: "Les valeurs de référence du traité de Maastricht sont…", c: ["3 % du PIB pour le déficit public et 60 % pour la dette", "2 % d’inflation et 5 % de chômage", "3 % de croissance et 60 % d’épargne", "1 % de déficit et 100 % de dette"], r: 0, e: "La France est à 5,1 % et 115,6 % en 2025 (Insee).", s: "e5-4" },
    { q: "Un choc asymétrique est un choc qui…", c: ["ne touche pas tous les pays de la zone de la même façon", "est très violent", "touche toute la zone en même temps", "vient de l’extérieur de l’Europe"], r: 0, e: "Le taux unique de la BCE ne peut alors convenir à tous.", s: "e5-4" },
    { q: "Selon Mundell, une union monétaire supporte mieux les chocs asymétriques si…", c: ["les travailleurs sont mobiles et des transferts budgétaires existent", "chaque pays garde sa monnaie", "les taux d’intérêt diffèrent selon les pays", "les budgets sont interdits"], r: 0, e: "Ce sont les critères d’une zone monétaire optimale.", s: "e5-4" }
  ],
  cartes: [
    { r: "Marché unique", v: "Libre circulation des biens, services, capitaux et personnes dans l’Union, depuis le 1er janvier 1993." },
    { r: "Zone euro", v: "Pays qui ont adopté l’euro (1999 ; pièces et billets en 2002) : 21 depuis le 1er janvier 2026." },
    { r: "Politique de la concurrence", v: "Action de la Commission contre les ententes, les abus de position dominante, les concentrations excessives et les aides d’État." },
    { r: "Abus de position dominante", v: "Une entreprise dominante utilise sa puissance pour évincer ses concurrents (ex. : Google, 2017)." },
    { r: "Aide d’État", v: "Avantage accordé par un État à certaines entreprises, interdit s’il fausse la concurrence (ex. : Apple en Irlande)." },
    { r: "Politique monétaire", v: "Action de la banque centrale sur les taux et la quantité de monnaie pour stabiliser les prix et la conjoncture." },
    { r: "Taux directeur", v: "Taux auquel les banques se refinancent auprès de la banque centrale ou y déposent leurs liquidités." },
    { r: "Politique budgétaire", v: "Utilisation des dépenses et des recettes publiques pour agir sur la conjoncture." },
    { r: "Multiplicateur keynésien", v: "Une dépense supplémentaire crée des revenus dépensés à leur tour : effet sur le PIB supérieur à la dépense initiale." },
    { r: "Stabilisateurs automatiques", v: "Recettes et dépenses publiques qui varient d’elles-mêmes avec la conjoncture et l’amortissent." },
    { r: "Indépendance de la BCE", v: "Elle ne reçoit d’instructions ni des gouvernements ni des institutions européennes ; mandat : stabilité des prix (2 %)." },
    { r: "Pacte de stabilité et de croissance", v: "Règles budgétaires européennes (1997, réformées en 2024) : référence de 3 % de déficit et 60 % de dette." },
    { r: "Policy mix", v: "Combinaison des politiques monétaire et budgétaire ; dans la zone euro, faute de coordination, il n’est voulu par personne." },
    { r: "Choc asymétrique", v: "Choc qui touche certains pays de la zone et pas les autres ; le taux unique ne convient pas à tous." },
    { r: "Zone monétaire optimale", v: "Zone où une monnaie commune est avantageuse : chocs semblables ou mécanismes d’ajustement (mobilité, transferts) (Mundell, 1961)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site, données BCE et Insee", t: "Points de pourcentage et ratios", enonce: '<p>Le taux de dépôt de la BCE passe de −0,50 % à 4,00 % entre juillet 2022 et septembre 2023. En 2025, le déficit public français est de 5,1 % du PIB et la dette de 115,6 % (Insee).</p><ol><li>De combien de points le taux a-t-il augmenté ? Pourquoi ne peut-on pas calculer de taux de variation ?</li><li>De combien de points le déficit dépasse-t-il la valeur de référence ? Et la dette ?</li></ol>',
      corrige: '<ol><li>4,00 − (−0,50) = +4,5 points. On ne calcule pas de taux de variation à partir d’une valeur négative ou nulle : il n’aurait pas de sens. Pour des taux, on raisonne en points.</li><li>Déficit : 5,1 − 3 = 2,1 points au-dessus de 3 %. Dette : 115,6 − 60 = 55,6 points au-dessus de 60 % ; elle représente près du double de la référence (115,6 ÷ 60 ≈ 1,93).</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet officiel : bac 2026, jour 1 (France), partie 1 · corrigé du site", officiel: true, t: "Expliquez une difficulté soulevée par les chocs asymétriques dans la zone euro.", enonce: "<p>3,5 points, sans document.</p>",
      methode: "<p>Une seule difficulté, mais complètement expliquée : définir choc asymétrique et zone euro, dérouler le mécanisme, illustrer.</p>",
      corrige: '<div class="copie"><p>La zone euro regroupe 21 pays qui partagent une même monnaie et donc une même politique monétaire, conduite par la Banque centrale européenne. Un choc asymétrique est un événement qui touche un ou plusieurs pays de la zone, mais pas les autres.</p><p>La difficulté principale est que la politique monétaire unique ne peut pas répondre à un tel choc. Si un pays entre en récession alors que les autres sont en croissance, il aurait besoin d’une baisse des taux d’intérêt pour relancer le crédit, l’investissement et la consommation. Mais la BCE fixe un taux unique en fonction de la situation moyenne de la zone, qui ne correspond pas à la sienne. Il ne peut pas non plus dévaluer sa monnaie pour regagner en compétitivité, puisqu’il n’en a plus. Il ne lui reste que sa politique budgétaire, elle-même encadrée par les règles européennes (valeur de référence de 3 % du PIB pour le déficit). La récession et le chômage risquent donc d’y être plus longs.</p><p>Ainsi, après l’éclatement de sa bulle immobilière en 2008, l’Espagne a connu un taux de chômage de 26,1 % en 2013, contre 5,2 % en Allemagne (Eurostat), alors que les deux pays avaient le même taux directeur.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, données BCE", t: "Les taux de la BCE depuis 2021", enonce: '<p>Document : le graphique « Le taux de la facilité de dépôt de la BCE, 2021-2026 » dans <a href="#e5:e5-3">le cours</a>.</p><ol><li>Décrivez l’évolution du taux entre 2022 et 2025.</li><li>À l’aide du document et de vos connaissances, montrez comment la politique monétaire agit sur la conjoncture.</li></ol>',
      corrige: '<ol><li>Selon la BCE, le taux de la facilité de dépôt, négatif (−0,50 %) jusqu’au deuxième trimestre 2022, monte rapidement à partir de juillet 2022 pour atteindre 4 % au troisième trimestre 2023 (+4,5 points). Il reste à ce niveau jusqu’au printemps 2024, puis baisse par étapes jusqu’à 2 % au deuxième trimestre 2025.</li><li>En relevant ses taux, la BCE renchérit le refinancement des banques, qui augmentent les taux de leurs crédits. Ménages et entreprises empruntent moins : l’immobilier, l’investissement et la consommation ralentissent, la demande globale aussi, et les prix augmentent moins vite. C’est ce qui était recherché en 2022, quand l’inflation de la zone euro atteignait 10,6 % ; elle est revenue à 2,4 % en moyenne en 2024. Une fois l’inflation maîtrisée, la BCE a baissé ses taux à partir de juin 2024 pour soutenir une activité faible : le mécanisme joue alors dans l’autre sens. Les effets ne sont pas immédiats : il faut plusieurs trimestres pour qu’une décision se transmette aux prix.</li></ol>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet officiel : bac 2026, jour 2 (France), dissertation · plan du site", officiel: true, t: "Dans quelle mesure la politique européenne de la concurrence atteint-elle ses objectifs ?", enonce: "<p>Les documents du sujet officiel ne sont pas reproduits ici. Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> La politique européenne de la concurrence veut protéger les consommateurs (prix bas, choix, innovation) et garantir des règles égales dans le marché unique. Y parvient-elle, alors qu’on lui reproche d’affaiblir l’industrie européenne face aux géants américains et chinois ?</p><p><b>I. Une politique qui atteint largement ses objectifs</b><br>A. Elle sanctionne les ententes qui font monter les prix (cartel des camions, 2,93 milliards d’euros en 2016).<br>B. Elle limite les abus des entreprises dominantes, y compris étrangères (Google, 2017, confirmé en 2024).<br>C. Elle empêche les aides d’État qui faussent la concurrence entre pays membres (Apple en Irlande, 13 milliards, 2024) et contribue aux gains du marché unique.</p><p><b>II. Mais ses résultats sont limités</b><br>A. Des procédures lentes face aux marchés numériques, d’où le DMA (2022).<br>B. Elle peut empêcher l’émergence de champions européens (Siemens-Alstom, 2019 ; rapport Draghi, 2024).<br>C. Elle encadre les aides publiques quand les autres puissances subventionnent massivement leurs industries.</p><p><b>III. Des objectifs qu’il faut articuler avec d’autres politiques</b><br>A. Concilier concurrence et politique industrielle (assouplissement des aides pour la transition écologique).<br>B. Intégrer l’innovation et la dimension mondiale dans l’analyse des fusions.<br>C. Coordonner avec la politique commerciale (défense contre les subventions étrangères).</p>' }
  ]
};

AUTEURS.push(
  { ch: "e5", n: "Robert Mundell", d: "1932-2021 · Nobel 1999", th: "Les zones monétaires optimales", l: "Théorie des <b>zones monétaires optimales</b> (1961) : une monnaie commune convient à des pays qui subissent des chocs semblables ou peuvent s’ajuster par la mobilité du travail et des transferts." },
  { ch: "e5", n: "Bela Balassa", d: "1928-1991", th: "Les étapes de l’intégration économique", l: "Il décrit en 1961 les étapes de l’<b>intégration économique</b> : zone de libre-échange, union douanière, marché commun, union économique, intégration totale." }
);
