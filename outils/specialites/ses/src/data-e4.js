GRAPHES["e4-pib"] = {
  type: "barres", t: "La France dans la crise de 2008-2009",
  s: "Taux de croissance du PIB en volume, en %.",
  src: "Source : Insee, comptes nationaux annuels, base 2020 (mai 2026).",
  unite: " %", x: [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013],
  y: [2.9, 1.9, 2.7, 2.5, 0.4, -2.8, 2.0, 2.4, 0.2, 0.8], pasX: 1, h: 240, min: -4, max: 4,
  notes: [{ x: 2009, y: -2.8, t: "−2,8 %" }]
};

CHAINES["e4-bulle"] = { t: "Formation et éclatement d’une bulle spéculative", e: [
  { t: "Le prix d’un actif monte (bonne nouvelle, crédit abondant)", k: "cause" },
  { t: "Des acheteurs achètent parce que le prix monte et que les autres achètent : mimétisme", a: "donc" },
  { t: "Chacun anticipant la hausse, la demande la provoque : prophétie autoréalisatrice", a: "donc" },
  { t: "Le prix s’écarte de la valeur fondamentale : c’est la bulle", a: "donc" },
  { t: "Un signal fait vendre les premiers ; tous veulent vendre en même temps", k: "frein", a: "puis" },
  { t: "Le prix s’effondre : le krach", k: "effet", a: "donc" }
] };
CHAINES["e4-panique"] = { t: "La panique bancaire", e: [
  { t: "Une banque prête à long terme l’argent déposé à vue (transformation des échéances)", k: "cause" },
  { t: "Une rumeur fait craindre pour sa solidité", a: "or" },
  { t: "Chaque déposant a intérêt à retirer son argent avant les autres", a: "donc" },
  { t: "Retraits massifs : la banque doit vendre ses actifs à perte ou ne peut plus rembourser", a: "donc" },
  { t: "Faillite, même si la banque était solvable au départ : la crainte s’est autoréalisée", k: "effet", a: "donc" }
] };
CHAINES["e4-chaine"] = { t: "Les faillites bancaires en chaîne", e: [
  { t: "Une banque fait faillite", k: "cause" },
  { t: "Elle ne rembourse plus ce qu’elle doit aux autres banques (prêts interbancaires)", a: "donc" },
  { t: "Ses créanciers subissent des pertes et leurs fonds propres baissent", a: "donc" },
  { t: "La méfiance gagne : les banques cessent de se prêter, les déposants se ruent aux guichets", a: "donc" },
  { t: "D’autres faillites suivent : la crise devient systémique", k: "effet", a: "donc" }
] };
CHAINES["e4-reel"] = { t: "De la crise financière à l’économie réelle", e: [
  { t: "Krach boursier ou immobilier, faillites bancaires", k: "cause" },
  { f: [{ t: "Effet de richesse négatif : patrimoine en baisse, ménages qui consomment moins" }, { t: "Baisse du prix du collatéral : les emprunteurs vendent leurs actifs en urgence, ce qui fait encore baisser les prix" }, { t: "Contraction du crédit : les banques fragilisées prêtent moins" }], a: "trois canaux" },
  { t: "Consommation et investissement reculent", a: "donc" },
  { t: "Le PIB baisse et le chômage augmente", k: "effet", a: "donc" }
] };
CHAINES["e4-alea"] = { t: "L’aléa moral des banques", e: [
  { t: "Les banques savent qu’en cas de difficulté, l’État ou la banque centrale les sauvera (« trop grosses pour faire faillite »)", k: "cause" },
  { t: "Elles prennent plus de risques : leurs gains sont privés, leurs pertes en partie publiques", a: "donc" },
  { t: "Le risque de crise augmente", k: "frein", a: "donc" },
  { t: "Réponse : supervision par la banque centrale et ratio de solvabilité (plus de fonds propres pour absorber les pertes)", k: "effet", a: "d’où" }
] };

ANIMS["e4-bulle"] = {
  t: "Une bulle se forme, puis éclate",
  h: 312,
  src: "Schéma de principe (valeurs illustratives). Exemples réels : bulle des tulipes (Provinces-Unies, 1637) ; bulle internet (indice Nasdaq, sommet le 10 mars 2000) ; immobilier américain (sommet des prix en 2006).",
  etapes: [
    { l: "Un actif (une action, un logement) a une valeur fondamentale : ce que rapportent ses revenus futurs (dividendes, loyers). Au départ, son prix en est proche.", d: 3.5 },
    { l: "Une bonne nouvelle fait monter le prix. D’autres achètent parce que le prix monte et que tout le monde achète : c’est le comportement mimétique.", d: 3.5 },
    { l: "Prophétie autoréalisatrice : chacun anticipe la hausse, achète, et la hausse se produit. Le prix s’envole loin de la valeur fondamentale : c’est la bulle.", d: 4 },
    { l: "Un signal (hausse des taux, mauvaise nouvelle, défauts de paiement) pousse les premiers à vendre pour encaisser leurs gains.", d: 3 },
    { l: "Le mimétisme joue à la baisse : tout le monde vend en même temps. Le prix s’effondre, souvent sous la valeur fondamentale : c’est le krach.", d: 3.5 }
  ],
  rendu: function (A, i, p) {
    var x0 = 40, y0 = 250, s = A.axes(x0, y0, 300, 220, { lx: "temps", ly: "prix de l’actif" });
    var fond = 70, pts = [];
    function prix(t) {
      if (t < 0.18) return fond + 6 * Math.sin(t * 30);
      if (t < 0.38) return fond + (t - 0.18) / 0.2 * 30;
      if (t < 0.62) return fond + 30 + Math.pow((t - 0.38) / 0.24, 2.2) * 125;
      if (t < 0.70) return 225 - (t - 0.62) / 0.08 * 20;
      return Math.max(38, 205 - Math.pow((t - 0.70) / 0.12, 1.4) * 170);
    }
    var bornes = [[0, 0.18], [0.18, 0.38], [0.38, 0.62], [0.62, 0.70], [0.70, 0.86]];
    var tmax = bornes[i][0] + (bornes[i][1] - bornes[i][0]) * p;
    var X = function (t) { return x0 + t * 340; }, Y = function (v) { return y0 - v; };
    s += '<line x1="' + x0 + '" x2="' + (x0 + 300) + '" y1="' + Y(fond) + '" y2="' + Y(fond) + '" style="stroke:var(--canard);stroke-width:2;stroke-dasharray:6 4"/>';
    s += A.t(x0 + 300, Y(fond) + 16, "valeur fondamentale", { t: 11, a: "end", c: "canard", g: true });
    for (var t = 0; t <= tmax + 1e-9; t += 0.005) pts.push([X(t), Y(prix(t))]);
    if (pts.length > 1) {
      if (i >= 2) {
        var zone = pts.filter(function (q, k) { var tt = k * 0.005; return tt >= 0.38 && tt <= Math.min(tmax, 0.70); });
        if (zone.length > 1) s += '<path d="M' + zone.map(function (q) { return q[0].toFixed(1) + " " + q[1].toFixed(1); }).join("L") + "L" + zone[zone.length - 1][0].toFixed(1) + " " + Y(fond) + "L" + zone[0][0].toFixed(1) + " " + Y(fond) + 'z" style="fill:var(--corail);opacity:.15"/>';
      }
      s += A.pl(pts, 1, { c: "corail", sw: 3 });
      var der = pts[pts.length - 1];
      s += A.cercle(der[0], der[1], 5, { f: "corail", s: "carte", sw: 2 });
    }
    var acheteurs = i === 0 ? 1 : i === 1 ? 1 + Math.round(4 * p) : i === 2 ? 5 + Math.round(9 * p) : i === 3 ? 14 - Math.round(4 * p) : 0;
    var vendeurs = i === 3 ? Math.round(4 * p) : i === 4 ? 4 + Math.round(12 * p) : 0;
    for (var k = 0; k < acheteurs; k++) s += A.cercle(118 + (k % 7) * 11, 282 + Math.floor(k / 7) * 11, 4.2, { f: "vert" });
    for (var m = 0; m < vendeurs; m++) s += A.cercle(270 + (m % 8) * 11, 282 + Math.floor(m / 8) * 11, 4.2, { f: "corail" });
    s += A.t(110, 286, "acheteurs", { t: 11, c: "vert", g: true, a: "end", op: acheteurs ? 1 : 0.35 });
    s += A.t(262, 286, "vendeurs", { t: 11, c: "corail", g: true, a: "end", op: vendeurs ? 1 : 0.35 });
    if (i === 2) s += A.t(X(0.52), Y(115), "bulle", { t: 16, g: true, a: "middle", c: "corail", op: A.s(p, 0.5, 1), f: true, h: true });
    if (i === 4) s += A.t(X(0.80), Y(150), "krach", { t: 18, g: true, a: "middle", c: "corail", op: A.s(p, 0.4, 0.9), f: true, h: true });
    return s;
  }
};

ANIMS["e4-contagion"] = {
  t: "Comment une faillite bancaire devient une crise",
  h: 320,
  src: "Schéma de principe. Repères : environ 9 000 faillites bancaires aux États-Unis de 1930 à mars 1933 ; faillite de Lehman Brothers le 15 septembre 2008 ; panique sur Silicon Valley Bank le 9 mars 2023.",
  etapes: [
    { l: "Les banques se prêtent entre elles sur le marché interbancaire : chacune détient des créances sur les autres.", d: 3 },
    { l: "La banque A subit de lourdes pertes (crédits immobiliers non remboursés) : ses fonds propres fondent.", d: 3 },
    { l: "A fait faillite et ne rembourse pas ses dettes : les banques B et C, qui lui avaient prêté, perdent à leur tour.", d: 3.5 },
    { l: "Les déposants de B, inquiets, viennent tous retirer leur argent : panique bancaire. Une banque prête à long terme : elle ne peut pas rembourser tout le monde d’un coup.", d: 4 },
    { l: "La méfiance devient générale : les banques cessent de se prêter, le crédit se tarit, d’autres faillites suivent. La crise est systémique.", d: 3.5 },
    { l: "Pour arrêter la contagion : la banque centrale prête en dernier ressort, la garantie des dépôts rassure ; en amont, supervision et fonds propres limitent les risques.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var B = { A: [70, 70], B: [180, 46], C: [290, 70], D: [70, 190], E: [180, 214], F: [290, 190] };
    var liens = [["A", "B"], ["A", "C"], ["B", "C"], ["A", "D"], ["B", "E"], ["C", "F"], ["D", "E"], ["E", "F"], ["B", "D"]];
    var s = "";
    var touche = { A: i >= 1, B: i >= 2, C: i >= 2, E: i >= 4, F: i >= 4, D: false };
    var faillite = { A: i >= 2, B: i >= 3 && i < 5, E: i === 4, F: false, C: false, D: false };
    if (i === 5) touche = { A: true, B: true, C: true };
    liens.forEach(function (l) {
      var a = B[l[0]], b = B[l[1]], coupe = i === 4;
      var q = i === 0 ? A.s(p, 0, 0.8) : 1;
      s += A.fl(a[0], a[1], a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q, { c: coupe ? "corail" : (i === 5 ? "vert" : "gris"), sw: 1.6, tete: false, tir: coupe, op: coupe ? 0.6 : (i === 3 ? 0.25 : 1) });
    });
    if (i === 2) [["A", "B"], ["A", "C"]].forEach(function (l) {
      var a = B[l[0]], b = B[l[1]], q = A.s(p, 0.1, 0.8);
      s += A.cercle(a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q, 6, { f: "corail" });
    });
    Object.keys(B).forEach(function (k) {
      var c = B[k], f = faillite[k] ? "corail" : touche[k] ? "moutarde" : "canard";
      if (i === 5) f = k === "A" ? "gris" : "canard";
      var r = 24;
      if (k === "A" && i === 1) r = 24 - 4 * A.s(p, 0, 1);
      s += A.cercle(c[0], c[1], r, { f: f, s: "carte", sw: 3 });
      s += A.t(c[0], c[1] + 6, k, { t: 17, g: true, a: "middle", c: "carte", f: true });
      if (faillite[k]) s += A.t(c[0], c[1] + (k === "E" ? 40 : -31), "faillite", { t: 11, g: true, a: "middle", c: "corail", h: true });
    });
    if (i === 1) s += A.jauge(14, 120, 84, 10 * (1 - A.s(p, 0, 1)) + 1, 11, { c: "corail", l: "fonds propres de A" });
    if (i === 3) {
      for (var k = 0; k < 12; k++) {
        var q = A.s(p, k * 0.05, 0.4 + k * 0.05), gauche = k < 6, j = k % 6;
        var dx = gauche ? 22 : 338, dy = 110 + j * 26;
        s += A.cercle(dx, dy, 6, { f: "moutarde" });
        s += A.fl(dx + (gauche ? 8 : -8), dy, 180 + (gauche ? -20 : 20), 58, { c: "moutarde", sw: 1.4, p: q, op: 0.8 });
      }
      s += A.t(180, 296, "déposants qui retirent leur argent", { t: 12, g: true, a: "middle", c: "moutarde", op: A.s(p, 0.2, 0.6), h: true });
    }
    if (i === 4) s += A.t(180, 290, "plus personne ne prête : crise systémique", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.3, 0.8), h: true });
    if (i === 5) {
      s += A.boite(20, 250, 150, 54, "banque centrale : prêteur en dernier ressort", { k: "cause", t: 11.5, op: A.s(p, 0, 0.4) });
      s += A.boite(190, 250, 150, 54, "garantie des dépôts : 100 000 € par client", { k: "cause", t: 11.5, op: A.s(p, 0.3, 0.7) });
    }
    return s;
  }
};

CH.e4 = {
  horsEcrit: "elle éclaire la conjoncture, le chômage conjoncturel (É3) et la politique monétaire (É5), et peut servir au Grand oral",
  chapo: "Un jeudi d’octobre 1929, un lundi de septembre 2008 : en quelques jours, la finance s’effondre et entraîne l’économie entière. Ce chapitre explique comment naissent les bulles, pourquoi les banques tombent en chaîne, comment la crise contamine l’emploi, et comment on régule les banques pour éviter la suivante.",
  essentiel: [
    "Les crises de <b>1929</b> et de <b>2008</b> partagent les mêmes étapes : effondrement boursier, faillites bancaires en chaîne, chute du PIB et hausse du chômage.",
    "Une <b>bulle spéculative</b> se forme quand le prix d’un actif s’écarte durablement de sa valeur fondamentale, sous l’effet de <b>comportements mimétiques</b> et de <b>prophéties autoréalisatrices</b> ; elle finit par éclater (krach).",
    "Les banques prêtent à long terme l’argent déposé à court terme : une rumeur peut provoquer une <b>panique bancaire</b> ; leurs prêts mutuels propagent les <b>faillites en chaîne</b>.",
    "La crise passe à l’<b>économie réelle</b> par trois canaux : <b>effet de richesse négatif</b>, <b>baisse du prix du collatéral et ventes forcées</b>, <b>contraction du crédit</b>.",
    "Pour réduire l’<b>aléa moral</b> des banques, on les <b>supervise</b> (banque centrale) et on leur impose un <b>ratio de solvabilité</b> (fonds propres suffisants)."
  ],
  chiffres: [
    { n: "−89 %", l: "la chute de l’indice Dow Jones entre son sommet du 3 septembre 1929 et son point bas du 8 juillet 1932.", s: "Données historiques de l’indice Dow Jones" },
    { n: "≈ 9 000", l: "faillites bancaires aux États-Unis entre 1930 et mars 1933.", s: "Ordre de grandeur couramment retenu par les historiens" },
    { n: "−2,8 %", l: "le recul du PIB français en 2009, la plus forte récession depuis 1950 avant celle de 2020.", s: "Insee, comptes nationaux" }
  ],
  objectifs: [
    { bo: "Connaître les principales caractéristiques de la crise financière des années 1930 et de celle de 2008 (effondrement boursier, faillites en chaîne, chute du PIB et accroissement du chômage).", clair: "Savoir raconter les deux crises avec leurs dates et leurs chiffres clés.", voir: "e4-1" },
    { bo: "Comprendre et savoir illustrer la formation et l’éclatement d’une bulle spéculative (comportements mimétiques et prophéties auto réalisatrices).", clair: "Expliquer pas à pas comment une bulle gonfle et éclate, avec un exemple.", voir: "e4-2" },
    { bo: "Comprendre les phénomènes de panique bancaire et de faillites bancaires en chaîne.", clair: "Expliquer pourquoi une banque saine peut tomber et comment une faillite en entraîne d’autres.", voir: "e4-3" },
    { bo: "Connaître les principaux canaux de transmission d’une crise financière à l’économie réelle : effets de richesse négatif, baisse du prix du collatéral et ventes forcées, contraction du crédit.", clair: "Présenter les trois canaux par lesquels la crise financière fait baisser production et emploi.", voir: "e4-4" },
    { bo: "Connaître les principaux instruments de régulation du système bancaire et financier qui permettent de réduire l’aléa moral des banques : supervision des banques par la banque centrale, ratio de solvabilité.", clair: "Définir l’aléa moral et expliquer comment supervision et ratio de solvabilité le limitent.", voir: "e4-5" }
  ],
  notions: ["crise financière", "krach boursier", "bulle spéculative", "valeur fondamentale", "comportement mimétique", "prophétie autoréalisatrice", "panique bancaire", "transformation des échéances", "faillites bancaires en chaîne", "risque systémique", "effet de richesse négatif", "collatéral", "ventes forcées", "contraction du crédit", "aléa moral", "prêteur en dernier ressort", "supervision bancaire", "ratio de solvabilité", "fonds propres"],
  sections: [
    { id: "e4-1", t: "Deux grandes crises : 1929 et 2008", h:
      '<div class="def"><b>Crise financière</b> — perturbation grave des marchés financiers et du système bancaire : chute brutale du prix des actifs (krach), faillites d’établissements financiers, blocage du crédit.</div>' +
      '<div class="tbl"><table><thead><tr><th></th><th>Crise des années 1930</th><th>Crise de 2008</th></tr></thead><tbody>' +
      '<tr><td><b>Bulle</b></td><td>Actions à Wall Street, achetées à crédit dans les années 1920</td><td>Immobilier américain, financé par des crédits risqués (<i>subprimes</i>) revendus sous forme de titres</td></tr>' +
      '<tr><td><b>Effondrement boursier</b></td><td>« Jeudi noir » du 24 octobre 1929 et « mardi noir » du 29 ; le Dow Jones perd 89 % entre septembre 1929 et juillet 1932</td><td>Prix immobiliers en baisse à partir de 2006 ; chute des Bourses mondiales à l’automne 2008</td></tr>' +
      '<tr><td><b>Faillites en chaîne</b></td><td>Environ 9 000 banques américaines de 1930 à 1933 ; faillite du Creditanstalt de Vienne en mai 1931 ; « vacances bancaires » décrétées par Roosevelt en mars 1933</td><td>Gel de trois fonds de BNP Paribas (9 août 2007) ; panique sur Northern Rock (septembre 2007) ; faillite de Lehman Brothers le 15 septembre 2008 ; sauvetage d’AIG, de Dexia</td></tr>' +
      '<tr><td><b>Chute du PIB</b></td><td>États-Unis : PIB réel en baisse d’environ un quart de 1929 à 1933</td><td>France : −2,8 % en 2009 (Insee)</td></tr>' +
      '<tr><td><b>Chômage</b></td><td>États-Unis : environ 25 % de la population active en 1933</td><td>États-Unis : 10 % en octobre 2009 ; France : de 7,4 % en 2008 à 9,1 % en 2009 (Insee)</td></tr>' +
      '</tbody></table></div>' +
      '<div data-graph="e4-pib"></div>' +
      '<p>Les deux crises n’ont pas eu la même ampleur : en 2008, les banques centrales et les États sont intervenus massivement (baisses de taux, prêts aux banques, plans de relance), alors qu’au début des années 1930 ils avaient laissé les banques tomber et resserré leurs budgets. L’ancien président de la Réserve fédérale Ben Bernanke, spécialiste de la Grande Dépression, a reçu le prix Nobel 2022 pour avoir montré le rôle des faillites bancaires dans l’aggravation de la crise des années 1930.</p>' },

    { id: "e4-2", t: "La formation et l’éclatement d’une bulle spéculative", h:
      '<div class="def"><b>Bulle spéculative</b> — hausse durable du prix d’un actif (actions, immobilier, matières premières) très au-dessus de sa <b>valeur fondamentale</b>, c’est-à-dire de la valeur actualisée des revenus qu’il rapportera (dividendes, loyers).</div>' +
      '<div data-anim="e4-bulle"></div>' +
      '<p>Deux mécanismes alimentent la bulle :</p>' +
      '<ul><li><b>Le comportement mimétique</b> : faute d’information sûre, chacun imite les autres ; si tout le monde achète, c’est sans doute qu’il faut acheter. Keynes comparait la Bourse à un concours de beauté où il faut deviner, non le plus beau visage, mais celui que les autres vont choisir.</li><li><b>La prophétie autoréalisatrice</b> : une croyance provoque elle-même sa réalisation. Si tout le monde pense que le prix va monter et achète, le prix monte. La notion vient du sociologue Robert K. Merton (1948).</li></ul>' +
      '<div data-chain="e4-bulle"></div>' +
      '<p>Le crédit joue souvent un rôle clé : on achète en empruntant, en espérant revendre plus cher. Quand les prix baissent, les emprunteurs doivent vendre pour rembourser, ce qui accélère le krach.</p>' +
      '<div class="ex"><p>La bulle internet : l’indice Nasdaq, riche en valeurs technologiques, atteint son sommet le 10 mars 2000, porté par des entreprises sans bénéfices dont on attendait des profits futurs considérables ; il perd environ 78 % jusqu’en octobre 2002.</p></div>' +
      '<div class="ex src"><p>La « tulipomanie » : dans les Provinces-Unies (actuels Pays-Bas), des bulbes de tulipes rares s’échangent à des prix extravagants, avant un effondrement en février 1637. Exemple classique, dont l’ampleur réelle est discutée par les historiens.</p></div>' },

    { id: "e4-3", t: "Paniques bancaires et faillites en chaîne", h:
      '<p class="lede">Une banque collecte des dépôts que les clients peuvent retirer à tout moment, et prête cet argent à long terme (crédits immobiliers, prêts aux entreprises). C’est la <b>transformation des échéances</b> : utile à l’économie, mais fragile.</p>' +
      '<div class="def"><b>Panique bancaire</b> (ruée bancaire) — retraits massifs et simultanés des déposants qui craignent de ne plus pouvoir récupérer leur argent. Comme la banque n’a pas toutes ses ressources disponibles, la crainte peut provoquer la faillite qu’elle redoutait.</div>' +
      '<div data-chain="e4-panique"></div>' +
      '<div class="aut"><span class="mono">DD</span><span class="an">Douglas Diamond et Philip Dybvig<small>1983 · Nobel 2022 avec Ben Bernanke</small></span><span class="ad">Leur modèle montre qu’une panique bancaire peut toucher une banque saine : si chacun croit que les autres vont retirer leurs dépôts, il est rationnel de se précipiter aussi. D’où l’utilité d’une garantie des dépôts.</span></div>' +
      '<div class="ex"><p>Le 9 mars 2023, les clients de Silicon Valley Bank, en Californie, demandent à retirer environ 42 milliards de dollars en une seule journée, alertés par des messages sur les réseaux sociaux. La banque est fermée par les autorités le lendemain, 10 mars 2023.</p></div>' +
      '<div class="def"><b>Faillites en chaîne</b> — les banques se prêtent entre elles et détiennent les mêmes types de titres : la faillite de l’une fait subir des pertes aux autres et répand la méfiance. On parle de <b>risque systémique</b>.</div>' +
      '<div data-anim="e4-contagion"></div>' +
      '<div data-chain="e4-chaine"></div>' +
      '<div class="ex"><p>Après la faillite de Lehman Brothers, le 15 septembre 2008, les banques ne savent plus lesquelles détiennent des titres toxiques : elles cessent de se prêter. Les banques centrales doivent fournir elles-mêmes les liquidités, et les États recapitalisent ou nationalisent des banques.</p></div>' },

    { id: "e4-4", t: "De la crise financière à l’économie réelle", h:
      '<p class="lede">L’<b>économie réelle</b> désigne la production de biens et de services, l’emploi et les revenus. Une crise financière la contamine par trois canaux.</p>' +
      '<h3>1. L’effet de richesse négatif</h3><p>La valeur des actions et des logements des ménages baisse : ils se sentent moins riches et consomment moins, surtout s’ils sont endettés. Les entreprises dont le cours s’effondre investissent moins.</p>' +
      '<h3>2. La baisse du prix du collatéral et les ventes forcées</h3><p>Le <b>collatéral</b> est un bien donné en garantie d’un prêt (le logement pour un crédit immobilier, des titres pour un prêt financier). Quand son prix baisse, la garantie ne couvre plus la dette : le prêteur exige un remboursement ou plus de garanties, et l’emprunteur doit <b>vendre en urgence</b>, ce qui fait encore baisser les prix. L’économiste Irving Fisher a décrit en 1933 cette spirale de la « déflation par la dette ».</p>' +
      '<h3>3. La contraction du crédit</h3><p>Les banques, qui ont subi des pertes et se méfient, réduisent leurs prêts et durcissent leurs conditions (<i>credit crunch</i>). Les entreprises ne peuvent plus financer leurs investissements ni même leur trésorerie ; les ménages n’obtiennent plus de crédits.</p>' +
      '<div data-chain="e4-reel"></div>' +
      '<div class="ex"><p>2008-2009 : avec la chute du commerce mondial et du crédit, le PIB de la France recule de 2,8 % en 2009 et son taux de chômage passe de 7,4 % à 9,1 % (Insee). La crise financière est devenue une crise économique et sociale.</p></div>' },

    { id: "e4-5", t: "Réguler le système bancaire et financier", h:
      '<div class="def"><b>Aléa moral</b> — situation où un agent, protégé contre les conséquences de ses actes, prend davantage de risques. Une banque qui sait qu’elle sera sauvée (« trop grosse pour faire faillite ») est incitée à prendre trop de risques.</div>' +
      '<div data-chain="e4-alea"></div>' +
      '<p>Le sauvetage des banques en 2008 a évité l’effondrement, mais il a renforcé cet aléa moral. D’où deux instruments, au programme :</p>' +
      '<h3>1. La supervision des banques par la banque centrale</h3><p>Une autorité contrôle la situation des banques : leurs risques, leurs fonds propres, leur organisation, et peut imposer des mesures. Dans la zone euro, la Banque centrale européenne supervise directement les grandes banques depuis le 4 novembre 2014 (mécanisme de surveillance unique), avec les autorités nationales comme l’ACPR en France. Des « tests de résistance » simulent des crises pour vérifier que les banques tiendraient.</p>' +
      '<h3>2. Le ratio de solvabilité</h3><div class="def"><b>Ratio de solvabilité</b> — rapport entre les <b>fonds propres</b> d’une banque (l’argent de ses actionnaires, qui absorbe les pertes) et ses actifs pondérés par leur risque. Plus il est élevé, plus la banque peut encaisser de pertes sans faire faillite.</div>' +
      '<p>Les accords de Bâle III (2010), négociés après la crise, exigent au minimum 4,5 % de fonds propres « durs » et 8 % de fonds propres au total, plus un coussin de conservation de 2,5 %. Plus de fonds propres, c’est aussi plus de « peau dans le jeu » pour les actionnaires : ils perdent leur mise si la banque prend trop de risques, ce qui réduit l’aléa moral.</p>' +
      '<div class="ex"><p>Après la crise de 1929, les États-Unis créent en 1933 une assurance fédérale des dépôts et séparent banques de dépôt et banques d’investissement (loi Glass-Steagall, abrogée en 1999). Aujourd’hui, dans l’Union européenne, les dépôts sont garantis jusqu’à 100 000 € par client et par banque.</p></div>' +
      '<div class="plus"><p>La <b>banque centrale prêteur en dernier ressort</b> fournit des liquidités aux banques solvables en difficulté passagère, pour éviter la contagion. Mais si elle sauve tout le monde, elle nourrit l’aléa moral : c’est pourquoi la supervision et les fonds propres viennent en amont.</p></div>' }
  ],
  pieges: [
    { f: "« Une bulle, c’est quand le prix monte beaucoup. »", v: "C’est quand le prix s’écarte durablement de la <b>valeur fondamentale</b> de l’actif, alimenté par le mimétisme et les anticipations." },
    { f: "« Une banque qui subit une panique était forcément mal gérée. »", v: "Une banque solvable peut tomber par manque de liquidités : elle a prêté à long terme ce qu’on peut lui réclamer à vue (Diamond et Dybvig)." },
    { f: "Confondre liquidité et solvabilité.", v: "Problème de liquidité : pas assez d’argent disponible tout de suite. Problème de solvabilité : les dettes dépassent ce que vaut ce qu’on possède." },
    { f: "« La crise financière ne touche que les riches qui ont des actions. »", v: "Elle passe à l’économie réelle par le crédit, la consommation et l’investissement : baisse du PIB et hausse du chômage." },
    { f: "« L’aléa moral, c’est quand une banque fraude. »", v: "C’est une incitation à prendre trop de risques parce qu’on est protégé des conséquences, sans qu’il y ait fraude." },
    { f: "« Cette question peut tomber à l’écrit. »", v: "Non en 2027 : elle n’est pas dans la liste des questions évaluables. Elle reste au programme et utile pour comprendre la conjoncture et les politiques économiques." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Bulle spéculative</b> : prix très au-dessus de la valeur fondamentale ; <b>mimétisme</b> ; <b>prophétie autoréalisatrice</b> (Merton, 1948) ; krach.</li>' +
    '<li><b>Panique bancaire</b> : retraits massifs ; transformation des échéances (Diamond et Dybvig, 1983). <b>Faillites en chaîne</b> : prêts interbancaires, risque systémique.</li>' +
    '<li><b>Transmission à l’économie réelle</b> : effet de richesse négatif ; baisse du collatéral et ventes forcées (Fisher, 1933) ; contraction du crédit.</li>' +
    '<li><b>Aléa moral</b> : prise de risque excessive d’un agent protégé. <b>Supervision</b> (BCE depuis le 4 novembre 2014) ; <b>ratio de solvabilité</b> = fonds propres ÷ actifs pondérés par les risques (Bâle III : 4,5 % de fonds propres durs, 8 % au total, + 2,5 % de coussin).</li></ul>' +
    '<h3>Dates et chiffres</h3><ul><li>1929 : jeudi noir 24 octobre ; Dow Jones −89 % (sept. 1929 → juil. 1932) ; environ 9 000 faillites bancaires (1930-1933) ; chômage américain autour de 25 % en 1933.</li><li>2008 : Lehman Brothers, 15 septembre ; France 2009 : PIB −2,8 %, chômage 7,4 % → 9,1 %.</li><li>2023 : panique sur Silicon Valley Bank (9-10 mars).</li></ul>',
  chainesFiche: ["e4-bulle", "e4-panique", "e4-chaine", "e4-reel", "e4-alea"],
  quiz: [
    { q: "Le « jeudi noir » de Wall Street a eu lieu le…", c: ["24 octobre 1929", "15 septembre 2008", "29 octobre 1933", "10 mars 2000"], r: 0, e: "Suivi du « mardi noir » du 29 octobre 1929.", s: "e4-1" },
    { q: "La faillite de Lehman Brothers, symbole de la crise de 2008, date du…", c: ["15 septembre 2008", "9 août 2007", "24 octobre 2008", "1er janvier 2009"], r: 0, e: "Le 9 août 2007 correspond au gel de trois fonds de BNP Paribas, premier signal de la crise.", s: "e4-1" },
    { q: "En 2009, le PIB de la France a…", c: ["reculé de 2,8 %", "progressé de 2,8 %", "reculé de 26 %", "stagné"], r: 0, e: "Insee : −2,8 % en volume, la plus forte récession depuis 1950 avant 2020.", s: "e4-1" },
    { q: "Une bulle spéculative se définit comme…", c: ["un prix très supérieur à la valeur fondamentale de l’actif", "toute hausse rapide d’un prix", "une baisse brutale des cours", "un excès de crédit aux entreprises"], r: 0, e: "La valeur fondamentale dépend des revenus futurs de l’actif.", s: "e4-2" },
    { q: "Acheter parce que les autres achètent est un comportement…", c: ["mimétique", "rationnel au sens de la valeur fondamentale", "d’aléa moral", "de collatéral"], r: 0, e: "Le mimétisme alimente la bulle à la hausse, puis le krach à la baisse.", s: "e4-2" },
    { q: "Une prophétie autoréalisatrice est…", c: ["une croyance qui provoque elle-même sa réalisation", "une prévision exacte d’un économiste", "une rumeur fausse", "une règle de la banque centrale"], r: 0, e: "Notion de Robert K. Merton (1948) : si tous anticipent la hausse et achètent, le prix monte.", s: "e4-2" },
    { q: "Pourquoi une banque saine peut-elle faire faillite lors d’une panique ?", c: ["Elle a prêté à long terme l’argent qu’on peut lui réclamer à tout moment", "Elle n’a pas de clients", "Elle fraude", "La banque centrale lui interdit de prêter"], r: 0, e: "C’est un problème de liquidité, pas forcément de solvabilité.", s: "e4-3" },
    { q: "Le risque systémique désigne…", c: ["le risque que la défaillance d’un établissement entraîne celle de tout le système", "le risque qu’une entreprise fasse faillite", "le risque de hausse des taux", "le risque de change"], r: 0, e: "Les banques sont liées par leurs prêts mutuels et leurs titres communs.", s: "e4-3" },
    { q: "L’effet de richesse négatif signifie que…", c: ["la baisse de la valeur du patrimoine réduit la consommation", "les riches deviennent pauvres", "les banques prêtent davantage", "les salaires augmentent"], r: 0, e: "Moins riches, les ménages consomment moins : la demande baisse.", s: "e4-4" },
    { q: "Les ventes forcées s’expliquent par…", c: ["la baisse du prix du collatéral, qui oblige à vendre pour rembourser", "la hausse des salaires", "la garantie des dépôts", "la hausse du PIB"], r: 0, e: "Les ventes en urgence font encore baisser les prix (déflation par la dette, Fisher, 1933).", s: "e4-4" },
    { q: "La contraction du crédit (credit crunch) touche l’économie réelle car…", c: ["entreprises et ménages ne peuvent plus financer investissements et achats", "les prix augmentent", "les impôts baissent", "le chômage diminue"], r: 0, e: "Les banques fragilisées prêtent moins et plus cher.", s: "e4-4" },
    { q: "L’aléa moral des banques vient de ce que…", c: ["elles comptent sur un sauvetage public et prennent donc plus de risques", "les déposants retirent leur argent", "les prix des actifs montent", "la banque centrale augmente les taux"], r: 0, e: "« Trop grosses pour faire faillite » : gains privés, pertes en partie publiques.", s: "e4-5" },
    { q: "Le ratio de solvabilité rapporte…", c: ["les fonds propres aux actifs pondérés par les risques", "les dépôts aux crédits", "les profits au chiffre d’affaires", "la dette publique au PIB"], r: 0, e: "Plus de fonds propres = plus de capacité à absorber les pertes.", s: "e4-5" },
    { q: "Dans la zone euro, la BCE supervise directement les grandes banques depuis…", c: ["novembre 2014", "1999", "2008", "1957"], r: 0, e: "Mécanisme de surveillance unique, entré en fonction le 4 novembre 2014.", s: "e4-5" }
  ],
  cartes: [
    { r: "Crise financière", v: "Perturbation grave des marchés financiers et des banques : krach, faillites, blocage du crédit." },
    { r: "Valeur fondamentale", v: "Valeur actualisée des revenus futurs d’un actif (dividendes, loyers)." },
    { r: "Bulle spéculative", v: "Hausse durable du prix d’un actif très au-dessus de sa valeur fondamentale." },
    { r: "Krach", v: "Effondrement brutal des cours (ex. : jeudi noir, 24 octobre 1929)." },
    { r: "Comportement mimétique", v: "Imiter les autres faute d’information sûre (acheter parce que tout le monde achète)." },
    { r: "Prophétie autoréalisatrice", v: "Croyance qui provoque sa propre réalisation (Merton, 1948)." },
    { r: "Transformation des échéances", v: "La banque prête à long terme des ressources disponibles à court terme (dépôts à vue)." },
    { r: "Panique bancaire", v: "Retraits massifs et simultanés des déposants, qui peuvent faire tomber même une banque saine." },
    { r: "Faillites en chaîne", v: "La faillite d’une banque cause des pertes et de la méfiance chez les autres : risque systémique." },
    { r: "Effet de richesse négatif", v: "Baisse du patrimoine qui réduit la consommation." },
    { r: "Collatéral", v: "Bien donné en garantie d’un prêt ; si son prix baisse, l’emprunteur doit souvent vendre en urgence." },
    { r: "Contraction du crédit", v: "Les banques réduisent leurs prêts et durcissent leurs conditions (credit crunch)." },
    { r: "Aléa moral", v: "Prise de risque excessive d’un agent protégé des conséquences (banques « trop grosses pour faire faillite »)." },
    { r: "Ratio de solvabilité", v: "Fonds propres ÷ actifs pondérés par les risques ; Bâle III : 8 % minimum au total." },
    { r: "Prêteur en dernier ressort", v: "Rôle de la banque centrale qui prête aux banques en manque de liquidités pour éviter la contagion." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site", t: "Lire un krach en pourcentages", enonce: '<p>Le Dow Jones vaut 381,17 points le 3 septembre 1929 et 41,22 points le 8 juillet 1932.</p><ol><li>Calcule le taux de variation.</li><li>Quelle hausse faudrait-il ensuite pour revenir au sommet ?</li></ol>',
      corrige: '<ol><li>(41,22 − 381,17) ÷ 381,17 × 100 ≈ −89,2 %.</li><li>381,17 ÷ 41,22 ≈ 9,25 : il faudrait que l’indice soit multiplié par 9,25, soit une hausse de 825 %. Une baisse de 89 % ne se compense pas par une hausse de 89 % : les deux taux ne s’appliquent pas à la même base.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez qu’une crise financière peut se transmettre à l’économie réelle.", enonce: "<p>3,5 points, sans document. Rappel : question non évaluée à l’écrit en 2027 ; l’exercice entraîne la méthode.</p>",
      corrige: '<div class="copie"><p>Une crise financière est une perturbation grave des marchés financiers et des banques ; l’économie réelle désigne la production, l’emploi et les revenus. La crise se transmet par trois canaux.</p><p>D’abord, l’effet de richesse négatif : la chute des cours boursiers et immobiliers réduit le patrimoine des ménages, qui consomment moins pour reconstituer leur épargne ou rembourser leurs dettes.</p><p>Ensuite, la baisse du prix du collatéral : les biens donnés en garantie des prêts perdent de la valeur, les emprunteurs doivent vendre en urgence, ce qui accentue la baisse des prix et les pertes (déflation par la dette décrite par Fisher en 1933).</p><p>Enfin, la contraction du crédit : les banques fragilisées prêtent moins, si bien que les entreprises réduisent leurs investissements. La demande baisse, la production recule et le chômage augmente : en France, le PIB a reculé de 2,8 % en 2009 et le chômage est passé de 7,4 % à 9,1 % (Insee).</p></div>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Comment expliquer les crises financières ?", enonce: "<p>« Comment expliquer » : plan explicatif.</p>",
      corrige: '<p><b>Problématique.</b> Les crises financières semblent surgir brutalement. Elles résultent pourtant de mécanismes identifiables : des comportements qui alimentent les bulles, une fragilité propre aux banques, et une régulation parfois défaillante.</p><p><b>I. Des bulles alimentées par le mimétisme et les anticipations</b><br>A. Valeur fondamentale et bulle ; exemples (1929, internet 2000, immobilier américain 2006).<br>B. Mimétisme et prophéties autoréalisatrices.<br>C. Le rôle du crédit dans le gonflement puis l’éclatement.</p><p><b>II. Un système bancaire fragile qui propage la crise</b><br>A. Transformation des échéances et paniques (Diamond et Dybvig ; Silicon Valley Bank 2023).<br>B. Faillites en chaîne et risque systémique (1930-1933 ; Lehman 2008).<br>C. Transmission à l’économie réelle : richesse, collatéral, crédit.</p><p><b>III. Des crises favorisées par une régulation insuffisante</b><br>A. L’aléa moral des banques « trop grosses pour faire faillite ».<br>B. Une supervision en retard sur l’innovation financière (titrisation des subprimes).<br>C. Les réponses : supervision par la BCE (2014), ratios de solvabilité de Bâle III, garantie des dépôts.</p>' }
  ]
};

AUTEURS.push(
  { ch: "e4", n: "Robert K. Merton", d: "1910-2003", th: "La prophétie autoréalisatrice", l: "Sociologue américain qui définit en 1948 la <b>prophétie autoréalisatrice</b> : une croyance, même fausse au départ, provoque des comportements qui la rendent vraie (exemple : la panique bancaire)." },
  { ch: "e4", n: "Irving Fisher", d: "1867-1947", th: "La déflation par la dette", l: "En 1933, il décrit la <b>déflation par la dette</b> : les emprunteurs vendent en urgence pour rembourser, ce qui fait baisser les prix et alourdit encore leurs dettes." },
  { ch: "e4", n: "Douglas Diamond et Philip Dybvig", d: "1983 · Nobel 2022", th: "Une panique peut faire tomber une banque saine", l: "Modèle des <b>paniques bancaires</b> : une banque qui transforme des dépôts à vue en prêts à long terme peut tomber si tous les déposants retirent leur argent en même temps." },
  { ch: "e4", n: "Ben Bernanke", d: "Nobel 2022", th: "Les faillites bancaires ont aggravé la Grande Dépression", l: "Il montre que les <b>faillites bancaires</b> des années 1930, en détruisant le crédit, ont transformé une récession en dépression. Président de la Réserve fédérale pendant la crise de 2008." }
);
