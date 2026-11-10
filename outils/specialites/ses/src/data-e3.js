GRAPHES["e3-chomage"] = {
  type: "lignes", t: "Le taux de chômage en France, 1975-2025", spark: 0,
  s: "Taux de chômage au sens du BIT, en % de la population active. Touche le graphique pour lire une année.",
  src: "Source : Insee, enquête Emploi 2025, séries longues sur le marché du travail (juillet 2026). Champ : France, personnes vivant dans un logement ordinaire, actives.",
  unite: " %", pasX: 10, h: 300, min: 0, max: 12,
  x: [1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
  series: [
    { n: "Ensemble", c: 2, v: [3.6,4.0,4.5,4.7,5.3,5.6,6.6,7.1,7.4,8.7,9.1,9.1,9.2,8.9,8.2,8.0,8.2,9.0,10.0,10.6,10.0,10.5,10.6,10.2,9.9,8.5,7.8,7.9,8.5,8.9,8.9,8.9,8.0,7.4,9.1,9.3,9.2,9.8,10.3,10.3,10.4,10.1,9.4,9.1,8.5,8.1,7.9,7.3,7.4,7.4,7.7] },
    { n: "Femmes", c: 3, v: [5.0,5.8,6.4,6.6,7.4,8.2,9.1,9.5,9.7,10.8,11.1,11.0,11.4,11.1,10.6,10.1,10.2,11.0,11.5,12.0,11.5,11.8,11.8,11.5,11.1,9.8,9.0,8.7,9.3,9.7,9.6,9.5,8.4,7.8,9.2,9.5,9.5,9.7,10.2,10.0,9.9,9.9,9.4,9.1,8.4,8.0,7.8,7.2,7.3,7.3,7.6] },
    { n: "Hommes", c: 1, v: [2.7,2.8,3.2,3.4,3.8,3.8,4.8,5.4,5.8,7.0,7.7,7.7,7.5,7.1,6.4,6.3,6.5,7.5,8.8,9.4,8.7,9.3,9.6,9.1,8.9,7.4,6.7,7.2,7.8,8.2,8.2,8.3,7.6,7.1,9.0,9.1,8.9,9.8,10.4,10.6,10.8,10.3,9.5,9.0,8.5,8.1,8.0,7.5,7.5,7.6,7.8] }
  ]
};
GRAPHES["e3-diplome"] = {
  type: "hbarres", t: "Qui est le plus exposé au chômage ? (2025)",
  s: "Taux de chômage au sens du BIT selon le diplôme et la catégorie socioprofessionnelle du dernier emploi, en %.",
  src: "Source : Insee, enquête Emploi 2025 (Emploi, chômage, revenus du travail, juillet 2026).",
  unite: " %", lab: 170,
  cats: ["Aucun diplôme ou brevet", "CAP, BEP ou équivalent", "Baccalauréat", "Bac + 2 ou plus", "Ouvriers peu qualifiés", "Employés peu qualifiés", "Cadres"],
  series: [{ n: "Taux de chômage", v: [14.7, 7.6, 9.1, 5.3, 17.1, 11.4, 4.0], c: 2 }]
};

CHAINES["e3-frictions"] = { t: "D’où vient le chômage structurel d’appariement ?", e: [
  { t: "Des emplois sont vacants pendant que des personnes cherchent un emploi", k: "cause" },
  { f: [{ t: "Frictions : il faut du temps pour se trouver (information, candidatures, entretiens)" }, { t: "Inadéquations : les emplois ne sont pas là où sont les chômeurs, ou demandent d’autres qualifications" }], a: "car" },
  { t: "Offres et demandes de travail ne se rencontrent pas, même quand l’activité est bonne", a: "donc" },
  { t: "Chômage structurel, qui persiste indépendamment de la conjoncture", k: "effet", a: "donc" }
] };
CHAINES["e3-efficience"] = { t: "Le salaire d’efficience", e: [
  { t: "L’employeur ne peut pas observer parfaitement l’effort de ses salariés (asymétrie d’information)", k: "cause" },
  { t: "Il verse un salaire supérieur au salaire d’équilibre pour motiver, fidéliser et attirer les meilleurs", a: "donc" },
  { t: "Perdre son emploi coûte plus cher au salarié : il fournit plus d’effort", a: "donc" },
  { t: "Mais à ce salaire, les entreprises embauchent moins que ce que souhaitent offrir les travailleurs", k: "frein", a: "or" },
  { t: "Un chômage involontaire durable apparaît, sans que le salaire baisse", k: "effet", a: "donc" }
] };
CHAINES["e3-smic"] = { t: "Les deux effets possibles d’un salaire minimum", e: [
  { t: "Hausse du salaire minimum", k: "cause" },
  { f: [{ t: "Coût du travail peu qualifié en hausse : s’il dépasse sa productivité, moins d’embauches", k: "frein" }, { t: "Pouvoir d’achat et incitation à travailler en hausse ; salariés plus stables et plus productifs", k: "effet" }], a: "deux effets" },
  { t: "L’effet net sur le chômage dépend du niveau du salaire minimum par rapport au salaire médian et à la productivité", a: "donc" }
] };
CHAINES["e3-protection"] = { t: "Règles de protection de l’emploi : un effet ambigu", e: [
  { t: "Licencier devient plus long et plus coûteux", k: "cause" },
  { f: [{ t: "En récession, les entreprises licencient moins : le chômage monte moins vite", k: "effet" }, { t: "En reprise, elles hésitent à embaucher en CDI : le chômage baisse moins vite", k: "frein" }], a: "donc" },
  { t: "Effet global incertain sur le niveau du chômage, mais des chômeurs qui restent plus longtemps sans emploi", a: "donc" },
  { t: "Dualisme : salariés en CDI protégés, jeunes et peu qualifiés en contrats courts", k: "frein", a: "et" }
] };
CHAINES["e3-conj"] = { t: "La spirale du chômage conjoncturel", e: [
  { t: "Choc : la demande baisse (crise financière, hausse des prix de l’énergie, incertitude)", k: "cause" },
  { t: "Les entreprises produisent moins et réduisent les heures, l’intérim, puis les emplois", a: "donc" },
  { t: "Le chômage augmente", a: "donc" },
  { t: "Les revenus et la confiance baissent : les ménages consomment moins, les entreprises investissent moins", a: "donc" },
  { t: "La demande baisse encore : le chômage conjoncturel s’auto-entretient", k: "effet", a: "donc" }
] };
CHAINES["e3-relance"] = { t: "La relance de la demande globale", e: [
  { f: [{ t: "Politique budgétaire : dépenses publiques en hausse ou impôts en baisse", k: "cause" }, { t: "Politique monétaire : baisse des taux d’intérêt directeurs", k: "cause" }] },
  { t: "Consommation et investissement augmentent", a: "donc" },
  { t: "Les entreprises anticipent plus de ventes et produisent davantage", a: "donc" },
  { t: "Elles embauchent : le chômage conjoncturel recule ; les revenus distribués relancent encore la demande (multiplicateur)", k: "effet", a: "donc" }
] };

ANIMS["e3-spirale"] = {
  t: "Le cercle vicieux du chômage conjoncturel… et la relance",
  h: 330,
  src: "Schéma de principe (mécanisme keynésien de la demande effective). La jauge est illustrative ; repère réel : en France, 7,4 % de chômage en 2008, 9,1 % en 2009 (Insee).",
  etapes: [
    { l: "Un choc frappe l’économie : la demande de biens et de services baisse (en 2009, crise financière mondiale).", d: 3 },
    { l: "Les entreprises vendent moins : elles produisent moins, réduisent l’intérim et les heures, puis l’emploi.", d: 3 },
    { l: "Le chômage augmente : des ménages perdent leurs revenus, les autres s’inquiètent et épargnent par précaution.", d: 3 },
    { l: "La consommation recule encore, donc la demande baisse de nouveau : le cercle vicieux s’auto-entretient.", d: 3.5 },
    { l: "La relance : l’État dépense plus ou baisse les impôts, la banque centrale baisse ses taux. La demande repart.", d: 3.5 },
    { l: "Le cercle tourne dans l’autre sens : production, embauches, revenus et consommation se renforcent. Le chômage conjoncturel recule.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var cx = 180, cy = 150, R = 100, RX = 128, s = "";
    var noeuds = [{ a: -90, t: "Demande" }, { a: 0, t: "Production" }, { a: 90, t: "Emploi" }, { a: 180, t: "Revenus et consommation" }];
    var sens = i >= 4 ? 1 : -1, actif = i <= 3 ? i : (i === 4 ? 0 : 3);
    function pos(a) { return [cx + RX * Math.cos(a * Math.PI / 180), cy + R * Math.sin(a * Math.PI / 180)]; }
    for (var k = 0; k < 4; k++) {
      var a1 = noeuds[k].a + (k % 2 ? 28 : 34), a2 = noeuds[(k + 1) % 4].a - (k % 2 ? 34 : 28), pts = [];
      for (var t = 0; t <= 1.0001; t += 0.04) { var aa = (a1 + (a2 - a1) * t) * Math.PI / 180; pts.push([cx + RX * Math.cos(aa), cy + R * Math.sin(aa)]); }
      var montre = i >= 3 ? 1 : (k < i ? 1 : (k === i ? A.s(p, 0.3, 1) : 0));
      var coul = i >= 4 ? "vert" : "corail";
      if (i === 5) montre = 1;
      if (montre > 0) {
        s += A.pl(pts, i === 4 ? A.s(p, 0.3, 1) : montre, { c: i === 4 ? "gris" : coul, sw: 2.4, tir: i === 4 });
        var fin = pts[pts.length - 1], av = pts[pts.length - 3];
        if ((i === 4 ? A.s(p, 0.3, 1) : montre) >= 1) s += A.fl(av[0], av[1], fin[0], fin[1], { c: i === 4 ? "gris" : coul, sw: 0.1 });
      }
    }
    noeuds.forEach(function (n, k) {
      var q = pos(n.a), act = (i <= 3 && k <= i) || i >= 4;
      s += A.boite(q[0] - 50, q[1] - 19, 100, 38, n.t + (act ? (sens < 0 ? " ↓" : (i === 5 || k === 0 ? " ↑" : "")) : ""), { k: act ? (sens < 0 ? "effet" : "cause") : "neutre", t: 12.5, g: true });
    });
    var ch = i <= 1 ? 7.4 : i === 2 ? A.l(7.4, 9.1, A.s(p, 0, 1)) : i === 3 ? A.l(9.1, 9.8, A.s(p, 0, 1)) : i === 4 ? 9.8 : A.l(9.8, 8.4, A.s(p, 0, 1));
    s += A.jauge(110, 300, 140, ch, 12, { c: i >= 5 ? "vert" : "corail", l: "chômage (illustratif)", val: A.fr(ch, 1) + " %" });
    if (i === 0) s += A.t(cx, cy - 4, "choc de demande", { t: 12.5, g: true, a: "middle", c: "corail", op: A.s(p, 0, 0.5), w: 90 });
    if (i === 3) s += A.t(cx, cy - 4, "cercle vicieux", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.3, 0.8), w: 90 });
    if (i >= 4) {
      s += A.t(cx, cy - 4, "relance", { t: 14, g: true, a: "middle", c: "vert", op: i === 4 ? A.s(p, 0, 0.4) : 1 });
      s += A.t(cx, cy + 13, "budgétaire et monétaire", { t: 10.5, a: "middle", c: "gris", op: i === 4 ? A.s(p, 0.2, 0.6) : 1, w: 90 });
      if (i === 4) s += A.fl(cx, 10, cx, cy - R - 22, { c: "vert", sw: 3, p: A.s(p, 0, 0.5) });
    }
    return s;
  }
};

ANIMS["e3-appariement"] = {
  t: "Des chômeurs et des emplois vacants en même temps",
  h: 310,
  src: "Schéma de principe. Repère : en 2025, 14,7 % de chômage pour les actifs sans diplôme ou avec le brevet, 5,3 % pour les diplômés du supérieur (Insee).",
  etapes: [
    { l: "Sur le marché du travail, des personnes cherchent un emploi (à gauche) et des entreprises ont des postes vacants (à droite).", d: 3 },
    { l: "Une partie se rencontre vite : ces postes sont pourvus.", d: 3 },
    { l: "Frictions : d’autres mettent du temps à se trouver (recherche, candidatures, entretiens). C’est le chômage frictionnel.", d: 3.5 },
    { l: "Inadéquation de qualification : un poste de technicien informatique ne convient pas à un ancien ouvrier du textile sans formation.", d: 3.5 },
    { l: "Inadéquation spatiale : l’emploi est à Lyon, le chômeur à 400 km et ne peut pas déménager facilement (logement, conjoint).", d: 3.5 },
    { l: "Résultat : chômeurs et emplois vacants coexistent durablement. C’est du chômage structurel ; la formation et la mobilité peuvent le réduire.", d: 3.5 }
  ],
  rendu: function (A, i, p) {
    var s = A.t(70, 22, "Demandeurs d’emploi", { t: 13, g: true, a: "middle", f: true }) + A.t(290, 22, "Postes vacants", { t: 13, g: true, a: "middle", f: true });
    var cand = [["vendeur", "", 0], ["comptable", "", 0], ["cariste", "", 0], ["infirmière", "", 1], ["ouvrier textile", "qualif", 2], ["soudeur (Lille)", "lieu", 3]];
    var postes = [["vendeur", 0], ["comptable", 0], ["cariste", 0], ["infirmière", 1], ["technicien informatique", 2], ["soudeur (Lyon)", 3]];
    cand.forEach(function (c, k) {
      var y = 40 + k * 40, x = 12, op = 1;
      var apparie = (k < 3 && i >= 1) || (k === 3 && i >= 2);
      var tx = 0;
      if (k < 3 && i === 1) tx = A.s(p, 0.1 + k * 0.15, 0.6 + k * 0.15);
      else if (k < 3 && i > 1) tx = 1;
      if (k === 3 && i === 2) tx = A.s(p, 0.4, 1);
      else if (k === 3 && i > 2) tx = 1;
      var x2 = A.l(x, 234, tx);
      if (apparie && tx >= 1) op = 0.35;
      s += A.boite(x2, y, 116, 30, c[0], { k: tx >= 1 ? "cause" : "neutre", op: op, t: 12 });
    });
    postes.forEach(function (c, k) {
      var y = 40 + k * 40, pris = (k < 3 && i >= 1 && (i > 1 || A.s(p, 0.1 + k * 0.15, 0.6 + k * 0.15) >= 1)) || (k === 3 && (i > 2 || (i === 2 && A.s(p, 0.4, 1) >= 1)));
      s += A.boite(234, y, 116, 30, c[0], { k: pris ? "cause" : "meca", t: 12, op: pris ? 0.35 : 1 });
    });
    if (i === 2) s += A.t(180, 296, "frictions : le temps de se trouver", { t: 12, a: "middle", c: "moutarde", g: true, op: A.s(p, 0, 0.4), h: true });
    if (i >= 3) {
      var q = i === 3 ? A.s(p, 0, 0.6) : 1;
      s += A.fl(130, 215, 230, 215, { c: "corail", sw: 2, p: q, tir: true }) + A.t(180, 208, "qualification ≠", { t: 11.5, a: "middle", c: "corail", g: true, op: q, h: true });
      s += A.t(180, 232, "✕", { t: 16, a: "middle", c: "corail", g: true, op: q });
    }
    if (i >= 4) {
      var q2 = i === 4 ? A.s(p, 0, 0.6) : 1;
      s += A.fl(130, 255, 230, 255, { c: "corail", sw: 2, p: q2, tir: true }) + A.t(180, 248, "distance ≠", { t: 11.5, a: "middle", c: "corail", g: true, op: q2, h: true });
      s += A.t(180, 272, "✕", { t: 16, a: "middle", c: "corail", g: true, op: q2 });
    }
    if (i === 5) s += A.r(6, 196, 348, 88, { f: "none", s: "moutarde", sw: 2.5, op: A.s(p, 0, 0.5), r: 10 }) + A.t(180, 302, "chômage structurel", { t: 12.5, g: true, a: "middle", c: "moutarde", op: A.s(p, 0.3, 0.8), h: true });
    return s;
  }
};

CH.e3 = {
  chapo: "En 2025, 2,5 millions de personnes sont au chômage en France, et presque autant tournent autour. Pourtant, des entreprises peinent à recruter. Ce chapitre explique comment on mesure le chômage, pourquoi une partie persiste même quand l’activité va bien, et ce que valent les politiques pour le combattre.",
  essentiel: [
    "Un <b>chômeur au sens du BIT</b> est sans emploi, disponible et en recherche active. En 2025, le <b>taux de chômage</b> est de 7,7 % ; le <b>taux d’emploi</b> des 15-64 ans de 69,3 % (Insee). Le <b>sous-emploi</b> et le <b>halo</b> du chômage complètent le tableau.",
    "Le <b>chômage structurel</b> persiste quelle que soit la conjoncture : problèmes d’<b>appariement</b> (frictions, inadéquations spatiales et de qualifications) et <b>asymétries d’information</b> (salaire d’efficience).",
    "Les <b>institutions</b> du marché du travail ont des effets ambigus : le <b>salaire minimum</b> et les <b>règles de protection de l’emploi</b> peuvent réduire ou accroître le chômage structurel selon leur niveau et leur forme.",
    "Le <b>chômage conjoncturel</b> vient d’une demande insuffisante : quand l’activité ralentit, les entreprises produisent et embauchent moins (Keynes).",
    "Quatre familles de politiques : <b>soutien de la demande globale</b>, <b>allègement du coût du travail</b>, <b>formation</b>, <b>flexibilisation</b>. Chacune vise un type de chômage et a ses limites."
  ],
  chiffres: [
    { n: "7,7 %", l: "de chômage au sens du BIT en 2025, soit 2,5 millions de personnes, en hausse de 0,3 point en un an.", s: "Insee, enquête Emploi 2025" },
    { n: "19,8 %", l: "de chômage chez les 15-24 ans actifs en 2025, contre 5,0 % chez les 50 ans ou plus.", s: "Insee, enquête Emploi 2025" },
    { n: "1,9 M", l: "de personnes dans le « halo » du chômage en 2025 : sans emploi, elles souhaitent travailler mais ne remplissent pas tous les critères du BIT.", s: "Insee, enquête Emploi 2025" }
  ],
  objectifs: [
    { bo: "Savoir définir le chômage et le sous-emploi et connaître les indicateurs de taux de chômage et de taux d’emploi.", clair: "Définir chômeur BIT, sous-emploi, halo ; calculer et lire taux de chômage et taux d’emploi.", voir: "e3-1" },
    { bo: "Comprendre que les problèmes d’appariements (frictions, inadéquations spatiales et de qualifications) et les asymétries d’information (salaire d’efficience) sont des sources de chômage structurel.", clair: "Expliquer pourquoi des chômeurs et des emplois vacants coexistent, et pourquoi un salaire élevé peut être voulu par l’employeur.", voir: "e3-2" },
    { bo: "Comprendre les effets (positifs ou négatifs) des institutions sur le chômage structurel (notamment salaire minimum et règles de protection de l’emploi).", clair: "Présenter les deux effets possibles du salaire minimum et des règles de protection de l’emploi.", voir: "e3-3" },
    { bo: "Comprendre les effets des fluctuations de l’activité économique sur le chômage conjoncturel.", clair: "Montrer comment un ralentissement de la demande crée du chômage, et comment il s’auto-entretient.", voir: "e3-4" },
    { bo: "Connaître les principales politiques mises en œuvre pour lutter contre le chômage : politiques macroéconomiques de soutien de la demande globale, politiques d’allégement du coût du travail, politiques de formation et politiques de flexibilisation pour lutter contre les rigidités du marché du travail.", clair: "Présenter les quatre familles de politiques, ce qu’elles visent, un exemple et une limite chacune.", voir: "e3-5" }
  ],
  notions: ["chômage (au sens du BIT)", "population active", "taux de chômage", "taux d’emploi", "sous-emploi", "halo du chômage", "chômage structurel", "chômage conjoncturel", "appariement", "chômage frictionnel", "inadéquations spatiales et de qualifications", "asymétrie d’information", "salaire d’efficience", "salaire minimum", "règles de protection de l’emploi", "demande globale", "coût du travail", "formation", "flexibilisation", "rigidités du marché du travail"],
  sections: [
    { id: "e3-1", t: "Définir et mesurer le chômage", h:
      '<div class="def"><b>Chômeur au sens du BIT</b> — personne de 15 ans ou plus qui remplit trois conditions à la fois : être <b>sans emploi</b> pendant une semaine donnée (pas même une heure de travail) ; être <b>disponible</b> pour travailler dans les deux semaines ; avoir <b>cherché activement</b> un emploi dans les quatre dernières semaines (ou en avoir trouvé un qui commence dans moins de trois mois).</div>' +
      '<p>L’Insee le mesure chaque trimestre par l’<b>enquête Emploi</b>, selon cette définition internationale du Bureau international du travail. Il ne faut pas le confondre avec le nombre d’inscrits à France Travail (ex-Pôle emploi, devenu France Travail le 1er janvier 2024), qui repose sur des règles administratives.</p>' +
      '<div class="tbl"><table><thead><tr><th>Indicateur</th><th>Calcul</th><th class="n">2025</th></tr></thead><tbody>' +
      '<tr><td><b>Taux de chômage</b></td><td>chômeurs ÷ population active (personnes en emploi + chômeurs) × 100</td><td class="n">7,7 %</td></tr>' +
      '<tr><td><b>Taux d’emploi</b> (15-64 ans)</td><td>personnes en emploi ÷ population du même âge × 100</td><td class="n">69,3 %</td></tr>' +
      '</tbody></table></div><p class="src-l">Source : Insee, enquête Emploi 2025. Le taux d’emploi atteint son plus haut niveau depuis que l’Insee le mesure (1975).</p>' +
      '<div class="ex"><p>En 2025, 2 451 000 chômeurs et 29 383 000 personnes en emploi : 2 451 ÷ (29 383 + 2 451) × 100 ≈ 7,7 %. Le taux de chômage des 15-24 ans atteint 19,8 %, mais comme beaucoup de jeunes sont étudiants (inactifs), la <b>part</b> de chômeurs dans toute leur classe d’âge n’est que de 8,5 %.</p></div>' +
      '<div data-graph="e3-chomage"></div>' +
      '<p>Le chômage français a fortement augmenté après les chocs pétroliers (3,6 % en 1975, 10,6 % en 1994), puis il a fluctué au gré de la conjoncture : 7,4 % en 2008, 10,4 % en 2015, 7,3 % en 2022, 7,7 % en 2025. Les hommes, longtemps moins touchés que les femmes, ont désormais un taux proche du leur.</p>' +
      '<h3>Aux frontières du chômage</h3>' +
      '<div class="def"><b>Sous-emploi</b> — situation de personnes en emploi qui travaillent moins qu’elles ne le souhaitent : temps partiel subi (souhait de travailler plus et disponibilité) ou chômage partiel ou technique. En 2025, 4,4 % des personnes en emploi (Insee).</div>' +
      '<div class="def"><b>Halo autour du chômage</b> — personnes sans emploi, classées inactives par le BIT, mais proches du chômage : elles souhaitent travailler mais n’ont pas cherché, ou ne sont pas disponibles tout de suite. En 2025, 1,9 million de personnes (Insee).</div>' +
      '<div class="ex"><p>En 2020, pendant les confinements, de nombreux chômeurs n’ont pas pu chercher d’emploi : ils sont sortis du chômage BIT vers le halo, et le chômage partiel a concerné 4,3 % des personnes en emploi. Le taux de chômage a donc paradoxalement baissé (8,1 % contre 8,5 % en 2019) alors que l’activité s’effondrait.</p></div>' },

    { id: "e3-2", t: "Le chômage structurel : appariement et salaire d’efficience", h:
      '<div class="def"><b>Chômage structurel</b> — part du chômage qui ne dépend pas de la conjoncture : il persiste même quand l’activité est soutenue, à cause du fonctionnement du marché du travail et de ses institutions. Le <b>chômage conjoncturel</b>, lui, vient d’un ralentissement de l’activité.</div>' +
      '<h3>1. Les problèmes d’appariement</h3>' +
      '<p>L’<b>appariement</b> est la rencontre entre une offre d’emploi et un demandeur. Elle n’est ni immédiate ni automatique.</p>' +
      '<ul><li><b>Frictions</b> : chercher un emploi, comparer, postuler, passer des entretiens prend du temps, même quand il existe un poste qui convient. C’est le <b>chômage frictionnel</b>, inévitable dans une économie où les gens changent d’emploi.</li><li><b>Inadéquation de qualifications</b> : les emplois disponibles demandent des compétences que les chômeurs n’ont pas (et inversement), notamment quand la destruction créatrice déplace les emplois d’un secteur à l’autre.</li><li><b>Inadéquation spatiale</b> : les emplois ne sont pas là où vivent les chômeurs ; déménager coûte cher (logement, emploi du conjoint).</li></ul>' +
      '<div data-anim="e3-appariement"></div>' +
      '<div data-chain="e3-frictions"></div>' +
      '<div class="ex"><p>Le risque de chômage dépend fortement de la qualification : en 2025, 14,7 % des actifs sans diplôme ou avec le seul brevet sont au chômage, contre 5,3 % des diplômés du supérieur (Bac + 2 ou plus) ; 17,1 % des ouvriers peu qualifiés contre 4,0 % des cadres (Insee). Le progrès technique biaisé (<a href="#e1:e1-5">É1</a>) renforce ces écarts.</p></div>' +
      '<div data-graph="e3-diplome"></div>' +
      '<div class="plus"><p>La <b>courbe de Beveridge</b> relie le taux d’emplois vacants et le taux de chômage : si les deux augmentent ensemble, c’est le signe d’un appariement moins efficace. Peter Diamond, Dale Mortensen et Christopher Pissarides ont reçu le prix Nobel 2010 pour leurs travaux sur les marchés avec frictions de recherche.</p></div>' +
      '<h3>2. Les asymétries d’information : le salaire d’efficience</h3>' +
      '<p>Une <b>asymétrie d’information</b> existe quand une partie à un contrat en sait plus que l’autre. L’employeur ne connaît pas parfaitement l’effort ni la motivation de ses salariés. Selon la théorie du <b>salaire d’efficience</b>, il a alors intérêt à payer <b>plus</b> que le salaire du marché : cela motive (perdre cet emploi coûterait cher), réduit le départ des salariés formés et attire les meilleurs candidats.</p>' +
      '<div data-chain="e3-efficience"></div>' +
      '<div class="ex src"><p>Le 5 janvier 1914, Henry Ford annonce le « Five Dollar Day » à l’usine de Highland Park : 5 dollars pour une journée de 8 heures, contre environ 2,34 dollars pour 9 heures auparavant. Une partie de la somme est versée comme participation aux bénéfices, sous conditions de conduite. Le travail à la chaîne était si pénible que la rotation de la main-d’œuvre était énorme (environ 370 % en 1913, selon l’entreprise) ; avec ce salaire, les démissions et l’absentéisme chutent. Les historiens discutent encore de la part de ce motif. Exemple classique d’histoire économique, hors des documents du programme.</p></div>' +
      '<div class="aut"><span class="mono">SS</span><span class="an">Carl Shapiro et Joseph Stiglitz<small>1984</small></span><span class="ad">Leur modèle montre qu’avec un salaire d’efficience, le chômage est <b>involontaire</b> et durable : il sert même de « discipline » qui incite les salariés à l’effort. Stiglitz a reçu le prix Nobel 2001 (avec Akerlof et Spence) pour ses travaux sur les asymétries d’information.</span></div>' },

    { id: "e3-3", t: "Les institutions : salaire minimum et protection de l’emploi", h:
      '<p class="lede">Les <b>institutions du marché du travail</b> sont les règles qui l’encadrent : salaire minimum, contrats de travail, règles de licenciement, assurance chômage, négociation collective. Leurs effets sur le chômage structurel peuvent être positifs ou négatifs.</p>' +
      '<h3>1. Le salaire minimum</h3>' +
      '<div class="def"><b>SMIC</b> (salaire minimum interprofessionnel de croissance) — salaire horaire en dessous duquel aucun salarié ne peut être payé en France. Il est revalorisé chaque 1er janvier et automatiquement en cours d’année si l’inflation dépasse 2 % : 12,31 € brut de l’heure, soit 1 867,02 € brut par mois à temps plein (montant en vigueur en novembre 2026, service-public.fr).</div>' +
      '<div data-chain="e3-smic"></div>' +
      '<ul><li><b>Effet négatif possible</b> : si le salaire minimum dépasse la productivité de certains travailleurs (jeunes, peu qualifiés), les employeurs ne les embauchent pas.</li><li><b>Effets positifs possibles</b> : il soutient le pouvoir d’achat, donc la demande ; il rend le travail plus attractif que l’inactivité ; il fonctionne comme un salaire d’efficience (moins de départs, plus de motivation).</li></ul>' +
      '<div class="aut"><span class="mono">CK</span><span class="an">David Card et Alan Krueger<small>1994</small></span><span class="ad">En comparant les fast-foods du New Jersey, où le salaire minimum a augmenté en 1992, à ceux de la Pennsylvanie voisine, ils ne trouvent pas de baisse de l’emploi. Cette « expérience naturelle » a relancé le débat ; Card a reçu le prix Nobel 2021.</span></div>' +
      '<p>Pour limiter l’effet négatif sur l’emploi peu qualifié sans baisser le salaire du salarié, la France allège les cotisations sociales patronales au niveau du SMIC (voir plus bas).</p>' +
      '<h3>2. Les règles de protection de l’emploi</h3>' +
      '<div class="def"><b>Règles de protection de l’emploi</b> — ensemble des règles qui encadrent les licenciements et le recours aux contrats temporaires : préavis, motifs, indemnités, procédures, limites aux CDD et à l’intérim.</div>' +
      '<div data-chain="e3-protection"></div>' +
      '<p>Elles protègent les salariés contre les licenciements abusifs et stabilisent l’emploi en récession. Mais elles peuvent freiner les embauches en CDI et créer un <b>dualisme</b> du marché du travail : des salariés « insiders » protégés et des « outsiders » (jeunes, peu qualifiés) qui enchaînent contrats courts et chômage. Assar Lindbeck et Dennis Snower ont formalisé cette opposition (1988).</p>' +
      '<div class="ex"><p>En 2025, le chômage de longue durée (plus d’un an) touche 1,8 % des actifs, soit 23,1 % des chômeurs ; il concerne 39,1 % des chômeurs de 50 ans ou plus (Insee). Les règles qui protègent l’emploi en place peuvent rendre plus difficile le retour à l’emploi des chômeurs âgés.</p></div>' },

    { id: "e3-4", t: "Le chômage conjoncturel", h:
      '<div class="def"><b>Chômage conjoncturel</b> — chômage dû à un ralentissement de l’activité économique : la demande de biens et services baisse, les entreprises produisent moins et ont besoin de moins de travail.</div>' +
      '<div class="aut"><span class="mono">JK</span><span class="an">John Maynard Keynes<small>1883-1946</small></span><span class="ad"><i>Théorie générale de l’emploi, de l’intérêt et de la monnaie</i> (1936) : le niveau de l’emploi dépend de la <b>demande effective</b>, c’est-à-dire de la demande que les entreprises anticipent. Si elle est insuffisante, le chômage peut durer : c’est un chômage involontaire, que la baisse des salaires ne résout pas (elle réduirait encore la demande).</span></div>' +
      '<div data-anim="e3-spirale"></div>' +
      '<div data-chain="e3-conj"></div>' +
      '<div class="ex"><p>La crise de 2008-2009 : le PIB français recule de 2,8 % en 2009 (Insee) ; le taux de chômage passe de 7,4 % en 2008 à 9,1 % en 2009, puis continue de monter jusqu’à 10,4 % en 2015, car la reprise est lente et la zone euro connaît une seconde crise en 2011-2012.</p></div>' +
      '<p>L’emploi réagit avec retard : les entreprises commencent par réduire les heures supplémentaires et l’intérim, puis ne remplacent pas les départs, avant de licencier. À l’inverse, en reprise, elles attendent d’être sûres que l’activité repart avant d’embaucher. Les jeunes et les salariés en contrats courts sont les premiers touchés.</p>' +
      '<div class="attn"><p>Structurel et conjoncturel s’entremêlent : un chômage conjoncturel qui dure peut devenir structurel (les compétences des chômeurs de longue durée s’érodent, les employeurs s’en méfient). C’est l’effet d’<b>hystérèse</b>.</p></div>' },

    { id: "e3-5", t: "Quelles politiques contre le chômage ?", h:
      '<div class="tbl"><table><thead><tr><th>Politique</th><th>Chômage visé</th><th>Exemple en France</th><th>Limite</th></tr></thead><tbody>' +
      '<tr><td><b>Soutien de la demande globale</b> (budgétaire, monétaire)</td><td>Conjoncturel</td><td>Plan de relance de 2020 ; prise en charge massive du chômage partiel pendant la crise sanitaire.</td><td>Hausse de la dette publique ; une partie de la demande part en importations ; inefficace contre le chômage structurel.</td></tr>' +
      '<tr><td><b>Allègement du coût du travail</b></td><td>Structurel (peu qualifiés)</td><td>Réduction générale des cotisations patronales sur les bas salaires (depuis 2003) ; CICE (2013), transformé en baisse de cotisations en 2019.</td><td>Coût élevé pour les finances publiques ; effets d’aubaine ; risque de « trappe à bas salaires ».</td></tr>' +
      '<tr><td><b>Formation</b></td><td>Structurel (inadéquation des qualifications)</td><td>Compte personnel de formation (2015) ; apprentissage ; Plan d’investissement dans les compétences (2018).</td><td>Effets lents ; les formations profitent plus souvent aux plus qualifiés.</td></tr>' +
      '<tr><td><b>Flexibilisation</b></td><td>Structurel (rigidités)</td><td>Rupture conventionnelle (2008) ; ordonnances de septembre 2017 (barème des indemnités prud’homales).</td><td>Précarisation ; effet incertain sur le niveau de l’emploi ; les ajustements sont plus rapides dans les deux sens.</td></tr>' +
      '</tbody></table></div>' +
      '<h3>1. Soutenir la demande globale</h3><p>Contre le chômage conjoncturel, l’État peut augmenter ses dépenses ou baisser les impôts (politique <b>budgétaire</b>), la banque centrale baisser ses taux (politique <b>monétaire</b>). L’effet est amplifié par le <b>multiplicateur</b> : les revenus distribués sont en partie dépensés, ce qui crée d’autres revenus. Dans la zone euro, la politique monétaire est commune et les budgets nationaux sont encadrés (<a href="#e5">É5</a>).</p>' +
      '<div data-chain="e3-relance"></div>' +
      '<h3>2. Alléger le coût du travail</h3><p>Baisser les cotisations sociales patronales sur les bas salaires réduit le coût du travail peu qualifié <b>sans baisser le salaire net</b> : cela vise les emplois dont la productivité est proche du SMIC. Les évaluations trouvent des effets positifs sur l’emploi surtout pour les allègements ciblés au voisinage du SMIC.</p>' +
      '<h3>3. Former</h3><p>La formation améliore l’appariement en rapprochant les compétences des chômeurs de celles que demandent les entreprises. Elle agit sur la cause du chômage structurel, mais lentement.</p>' +
      '<h3>4. Flexibiliser</h3><p>Assouplir les règles d’embauche et de licenciement doit inciter les entreprises à embaucher. La <b>flexicurité</b> danoise combine licenciements faciles, indemnisation généreuse et politiques actives de retour à l’emploi : flexibilité pour l’entreprise, sécurité pour la personne plutôt que pour le poste.</p>' +
      '<div class="cle"><p><b>À retenir :</b> on choisit la politique selon le diagnostic. Contre un chômage conjoncturel, la relance de la demande ; contre un chômage structurel, des politiques de l’offre (coût du travail, formation, flexibilité). En pratique, les gouvernements combinent les deux.</p></div>' }
  ],
  pieges: [
    { f: "« Chômeur = inscrit à France Travail. »", v: "Le chômeur au sens du BIT répond à trois critères mesurés par l’enquête Emploi ; les inscriptions à France Travail suivent d’autres règles. Les deux chiffres diffèrent." },
    { f: "« Le taux de chômage des jeunes est de 19,8 %, donc un jeune sur cinq est chômeur. »", v: "Non : 19,8 % des jeunes <b>actifs</b>. Rapporté à tous les 15-24 ans (beaucoup sont étudiants), la part de chômeurs est de 8,5 %." },
    { f: "« Si le taux de chômage baisse, l’emploi augmente forcément. »", v: "Le chômage peut baisser parce que des chômeurs deviennent inactifs (découragement, halo) : en 2020, il a baissé alors que l’activité s’effondrait." },
    { f: "Confondre chômage structurel et chômage de longue durée.", v: "Le chômage structurel désigne une <b>cause</b> (fonctionnement du marché du travail) ; le chômage de longue durée, une <b>durée</b> (plus d’un an)." },
    { f: "« Le salaire minimum crée toujours du chômage. »", v: "Son effet dépend de son niveau par rapport à la productivité ; il peut aussi soutenir la demande et jouer comme un salaire d’efficience (Card et Krueger)." },
    { f: "« La relance budgétaire fait baisser tout chômage. »", v: "Elle agit sur le chômage conjoncturel ; elle ne résout pas les inadéquations de qualifications ou les frictions." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Chômeur BIT</b> : sans emploi, disponible sous 15 jours, en recherche active (4 dernières semaines). <b>Taux de chômage</b> = chômeurs ÷ actifs. <b>Taux d’emploi</b> = emploi ÷ population de la classe d’âge.</li>' +
    '<li><b>Sous-emploi</b> : temps partiel subi, chômage partiel (4,4 % de l’emploi en 2025). <b>Halo</b> : inactifs proches du chômage (1,9 million en 2025).</li>' +
    '<li><b>Chômage structurel</b> : appariement (frictions ; inadéquations spatiales et de qualifications) ; asymétries d’information et <b>salaire d’efficience</b> (Shapiro et Stiglitz, 1984 ; Ford, 1914).</li>' +
    '<li><b>Institutions</b> : salaire minimum (effet coût / effet demande et efficience ; Card et Krueger, 1994) ; protection de l’emploi (moins de licenciements en crise, moins d’embauches en reprise, dualisme insiders / outsiders).</li>' +
    '<li><b>Chômage conjoncturel</b> : demande effective insuffisante (Keynes, 1936) ; cercle vicieux ; hystérèse.</li>' +
    '<li><b>Politiques</b> : relance de la demande ; allègements de cotisations ; formation ; flexibilisation (flexicurité).</li></ul>' +
    '<h3>Chiffres à citer (Insee, 2025)</h3><ul><li>Chômage 7,7 % (2,5 millions) ; 15-24 ans 19,8 % ; sans diplôme 14,7 % contre 5,3 % pour Bac + 2 ou plus.</li><li>Taux d’emploi des 15-64 ans 69,3 %, record depuis 1975 ; chômage 2008 7,4 % → 2009 9,1 % → 2015 10,4 %.</li><li>SMIC : 12,31 € brut de l’heure (novembre 2026).</li></ul>',
  chainesFiche: ["e3-frictions", "e3-efficience", "e3-smic", "e3-protection", "e3-conj", "e3-relance"],
  quiz: [
    { q: "Pour être chômeur au sens du BIT, il faut notamment…", c: ["être sans emploi, disponible et en recherche active d’emploi", "être inscrit à France Travail", "toucher une allocation chômage", "avoir perdu son emploi depuis plus d’un an"], r: 0, e: "Trois critères cumulés ; l’inscription et l’indemnisation n’en font pas partie.", s: "e3-1" },
    { q: "Le taux de chômage se calcule en rapportant le nombre de chômeurs…", c: ["à la population active", "à la population totale", "à la population en âge de travailler", "au nombre de personnes en emploi"], r: 0, e: "Population active = personnes en emploi + chômeurs.", s: "e3-1" },
    { q: "En 2025, le taux de chômage en France est d’environ…", c: ["7,7 %", "3,6 %", "12 %", "19,8 %"], r: 0, e: "7,7 % selon l’Insee ; 19,8 % est le taux des 15-24 ans actifs.", s: "e3-1" },
    { q: "Une personne à temps partiel qui souhaite travailler plus et est disponible est…", c: ["en sous-emploi", "au chômage", "dans le halo du chômage", "inactive"], r: 0, e: "Elle a un emploi, donc elle n’est pas chômeuse ; elle est en sous-emploi.", s: "e3-1" },
    { q: "Le halo autour du chômage regroupe des personnes…", c: ["sans emploi, classées inactives, mais proches du chômage", "en emploi à temps partiel", "au chômage depuis plus d’un an", "inscrites à France Travail"], r: 0, e: "Elles souhaitent travailler mais n’ont pas cherché ou ne sont pas disponibles tout de suite.", s: "e3-1" },
    { q: "Le chômage frictionnel s’explique par…", c: ["le temps nécessaire pour qu’offres et demandes d’emploi se rencontrent", "une baisse de la demande globale", "un salaire minimum trop élevé", "la concurrence internationale"], r: 0, e: "C’est un problème d’appariement, une composante du chômage structurel.", s: "e3-2" },
    { q: "Selon la théorie du salaire d’efficience, l’employeur paie plus que le salaire du marché pour…", c: ["motiver, fidéliser et attirer les meilleurs salariés", "respecter le SMIC", "baisser ses coûts", "réduire ses impôts"], r: 0, e: "Il ne peut pas observer parfaitement l’effort (asymétrie d’information) ; un salaire élevé rend la perte d’emploi coûteuse.", s: "e3-2" },
    { q: "Un emploi vacant à Lyon et un chômeur qualifié pour ce poste à Lille illustrent…", c: ["une inadéquation spatiale", "un chômage conjoncturel", "un salaire d’efficience", "du sous-emploi"], r: 0, e: "L’emploi et la personne ne sont pas au même endroit.", s: "e3-2" },
    { q: "Quel effet POSITIF un salaire minimum peut-il avoir sur l’emploi ?", c: ["Soutenir le pouvoir d’achat et donc la demande", "Réduire le coût du travail", "Faciliter les licenciements", "Supprimer les frictions"], r: 0, e: "Il peut aussi rendre le travail plus attractif et jouer comme un salaire d’efficience.", s: "e3-3" },
    { q: "Card et Krueger (1994) ont montré qu’une hausse du salaire minimum au New Jersey…", c: ["n’avait pas entraîné de baisse de l’emploi dans les fast-foods", "avait fait doubler le chômage", "avait fait fermer tous les fast-foods", "avait fait baisser les prix"], r: 0, e: "Comparaison avec la Pennsylvanie voisine : une expérience naturelle.", s: "e3-3" },
    { q: "Des règles de protection de l’emploi fortes ont tendance à…", c: ["réduire les licenciements en récession mais freiner les embauches en reprise", "faire baisser fortement le chômage dans tous les cas", "supprimer le chômage de longue durée", "augmenter la demande globale"], r: 0, e: "D’où un effet ambigu sur le niveau du chômage et un risque de dualisme.", s: "e3-3" },
    { q: "Le chômage conjoncturel est lié à…", c: ["un ralentissement de l’activité économique", "l’inadéquation des qualifications", "les asymétries d’information", "le salaire minimum"], r: 0, e: "Moins de demande, moins de production, moins d’emplois (Keynes).", s: "e3-4" },
    { q: "Entre 2008 et 2009, le taux de chômage en France est passé de…", c: ["7,4 % à 9,1 %", "3,6 % à 5,0 %", "9,1 % à 7,4 %", "10,4 % à 12 %"], r: 0, e: "La récession de 2009 (PIB −2,8 %) a fait monter le chômage conjoncturel.", s: "e3-4" },
    { q: "Pour lutter contre un chômage d’inadéquation des qualifications, la politique la plus adaptée est…", c: ["la formation", "la baisse des taux d’intérêt", "la hausse des dépenses publiques", "la hausse du salaire minimum"], r: 0, e: "La formation rapproche les compétences des besoins des entreprises.", s: "e3-5" },
    { q: "Les allègements de cotisations patronales sur les bas salaires visent à…", c: ["baisser le coût du travail peu qualifié sans baisser le salaire net", "baisser le SMIC", "augmenter les recettes de l’État", "relancer la demande globale"], r: 0, e: "Ils ciblent les emplois proches du SMIC.", s: "e3-5" }
  ],
  cartes: [
    { r: "Chômeur au sens du BIT", v: "Sans emploi (pas même une heure), disponible dans les 15 jours, en recherche active dans les 4 dernières semaines." },
    { r: "Population active", v: "Personnes en emploi + chômeurs." },
    { r: "Taux de chômage", v: "Chômeurs ÷ population active × 100 (7,7 % en 2025)." },
    { r: "Taux d’emploi", v: "Personnes en emploi ÷ population de la classe d’âge × 100 (69,3 % des 15-64 ans en 2025)." },
    { r: "Sous-emploi", v: "Personnes en emploi qui travaillent moins qu’elles le souhaitent (temps partiel subi) ou en chômage partiel." },
    { r: "Halo autour du chômage", v: "Inactifs proches du chômage : souhaitent travailler mais ne cherchent pas ou ne sont pas disponibles (1,9 million en 2025)." },
    { r: "Chômage structurel", v: "Chômage indépendant de la conjoncture, dû au fonctionnement du marché du travail et à ses institutions." },
    { r: "Chômage conjoncturel", v: "Chômage dû à un ralentissement de l’activité et de la demande." },
    { r: "Appariement", v: "Rencontre entre une offre d’emploi et un demandeur ; elle peut être freinée par des frictions et des inadéquations." },
    { r: "Inadéquations spatiales et de qualifications", v: "Les emplois vacants ne sont pas là où sont les chômeurs, ou demandent d’autres compétences." },
    { r: "Asymétrie d’information", v: "Situation où une partie à un échange en sait plus que l’autre (ex. : l’employeur ignore l’effort réel du salarié)." },
    { r: "Salaire d’efficience", v: "Salaire supérieur au salaire du marché, versé pour motiver et fidéliser ; il peut créer un chômage involontaire (Shapiro et Stiglitz)." },
    { r: "Règles de protection de l’emploi", v: "Règles qui encadrent licenciements et contrats temporaires ; effets ambigus sur le chômage, risque de dualisme." },
    { r: "Demande effective", v: "Demande anticipée par les entreprises, qui détermine la production et l’emploi (Keynes, 1936)." },
    { r: "Flexicurité", v: "Modèle danois : licenciements faciles, indemnisation généreuse, accompagnement actif vers l’emploi." },
    { r: "Hystérèse du chômage", v: "Un chômage conjoncturel qui dure devient structurel (perte de compétences, méfiance des employeurs)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site, données Insee", t: "Calculer un taux de chômage", enonce: '<p>En 2025, en France, l’Insee compte 2 451 000 chômeurs au sens du BIT et 29 383 000 personnes en emploi.</p><ol><li>Calcule la population active, puis le taux de chômage.</li><li>Les 15-24 ans ont un taux de chômage de 19,8 % mais une « part de chômage » de 8,5 %. Explique la différence.</li></ol>',
      corrige: '<ol><li>Population active = 29 383 000 + 2 451 000 = 31 834 000. Taux de chômage = 2 451 ÷ 31 834 × 100 ≈ 7,7 %.</li><li>Le taux de chômage rapporte les chômeurs aux <b>actifs</b> ; la part de chômage les rapporte à <b>toute</b> la classe d’âge. Beaucoup de 15-24 ans étudient et sont inactifs : le dénominateur est bien plus grand, la part est donc plus faible.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que les problèmes d’appariement peuvent être à l’origine d’un chômage structurel.", enonce: "<p>3,5 points, sans document.</p>",
      corrige: '<div class="copie"><p>Le chômage structurel est la part du chômage qui ne dépend pas de la conjoncture. L’appariement est la rencontre entre une offre d’emploi et un demandeur d’emploi ; lorsqu’elle se fait mal, chômeurs et emplois vacants coexistent.</p><p>D’abord, les frictions : même lorsqu’un poste correspond à un chômeur, il faut du temps pour que l’information circule, que les candidatures soient examinées et que l’embauche se fasse. Pendant ce temps, la personne est au chômage : c’est le chômage frictionnel, qui existe même en période de forte activité.</p><p>Ensuite, les inadéquations. Inadéquation de qualifications : avec la destruction créatrice, les emplois créés demandent souvent des compétences que n’ont pas les personnes dont l’emploi a disparu ; en 2025, selon l’Insee, 14,7 % des actifs sans diplôme ou avec le brevet sont au chômage, contre 5,3 % des diplômés du supérieur. Inadéquation spatiale : les emplois sont concentrés dans certaines métropoles alors que des chômeurs vivent dans des territoires en déclin et ne peuvent pas déménager facilement. Dans ces deux cas, le chômage persiste même si la demande globale est soutenue : il est structurel.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, document Insee", t: "Le chômage selon le diplôme", enonce: '<p>Document : le graphique « Qui est le plus exposé au chômage ? (2025) » dans <a href="#e3:e3-2">le cours</a>.</p><ol><li>Comparez le taux de chômage des actifs sans diplôme (ou avec le brevet) et celui des diplômés de Bac + 2 ou plus.</li><li>À l’aide du document et de vos connaissances, montrez que le chômage touche inégalement les actifs.</li></ol>',
      corrige: '<ol><li>Selon l’Insee, en 2025 en France, le taux de chômage des actifs sans diplôme ou avec le brevet est de 14,7 %, contre 5,3 % pour les diplômés de Bac + 2 ou plus : il est environ 2,8 fois plus élevé (9,4 points d’écart).</li><li>Le document montre une forte inégalité selon le diplôme et la qualification : 17,1 % de chômage pour les ouvriers peu qualifiés contre 4,0 % pour les cadres. Deux mécanismes l’expliquent. L’inadéquation des qualifications : le progrès technique biaisé et la tertiarisation augmentent la demande de travail qualifié et réduisent celle de travail peu qualifié et routinier. Le coût du travail : quand la productivité d’un emploi est proche du salaire minimum, l’employeur hésite à embaucher, d’où les allègements de cotisations ciblés sur les bas salaires. On peut ajouter que les jeunes (19,8 % de chômage) sont exposés car ils sont en phase d’insertion et occupent plus souvent des contrats courts, premiers supprimés quand l’activité ralentit.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet inventé pour le site", t: "À l’aide du dossier, montrez que le chômage peut avoir des causes conjoncturelles.", enonce: '<p><b>Document 1</b> : le graphique « Le taux de chômage en France, 1975-2025 » (Insee). <b>Document 2</b> : le PIB en volume recule de 2,8 % en 2009 (Insee). <b>Document 3</b> (texte factuel) : en 2009, les entreprises réduisent l’intérim et les heures supplémentaires avant de supprimer des emplois.</p>',
      corrige: '<p><b>Introduction.</b> Le chômage conjoncturel est la part du chômage due à un ralentissement de l’activité. On montrera qu’un choc de demande réduit la production et l’emploi, puis que ce chômage peut s’auto-entretenir.</p><p><b>I. Un ralentissement de la demande réduit la production et l’emploi.</b> Demande effective (Keynes) : les entreprises produisent selon les ventes anticipées. Document 2 : récession de 2009. Document 3 : ajustement par l’intérim et les heures, puis l’emploi. Document 1 : 7,4 % en 2008, 9,1 % en 2009.</p><p><b>II. Le chômage conjoncturel s’auto-entretient.</b> Moins d’emplois → moins de revenus, épargne de précaution → moins de consommation et d’investissement → nouvelle baisse de la demande. Document 1 : la hausse continue jusqu’à 10,4 % en 2015 avec la crise de la zone euro. Risque d’hystérèse.</p><p><b>Conclusion.</b> Les fluctuations de l’activité expliquent une partie des variations du chômage, d’où les politiques de relance de la demande globale.</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Les politiques de l’offre sont-elles suffisantes pour lutter contre le chômage ?", enonce: "<p>Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> Les politiques de l’offre (coût du travail, formation, flexibilité) visent le chômage structurel. Peuvent-elles à elles seules faire baisser durablement le chômage, alors qu’une partie de celui-ci dépend de la demande ?</p><p><b>I. Les politiques de l’offre agissent sur le chômage structurel</b><br>A. Alléger le coût du travail peu qualifié (cotisations ; CICE devenu baisse de cotisations en 2019).<br>B. Former pour réduire les inadéquations (CPF, apprentissage).<br>C. Flexibiliser pour lever les rigidités (rupture conventionnelle, ordonnances de 2017 ; flexicurité).</p><p><b>II. Mais elles ont des limites</b><br>A. Effets d’aubaine, coût budgétaire, trappes à bas salaires.<br>B. Précarisation, dualisme du marché du travail.<br>C. Elles sont impuissantes face au chômage conjoncturel : 2009, PIB −2,8 %, chômage 7,4 % → 9,1 %.</p><p><b>III. Elles doivent être combinées à des politiques de la demande</b><br>A. Relance budgétaire et monétaire en récession (multiplicateur ; chômage partiel en 2020).<br>B. Éviter l’hystérèse : un chômage conjoncturel durable devient structurel.<br>C. Coordination européenne de la demande (<a href="#e5">É5</a>).</p>' }
  ]
};

AUTEURS.push(
  { ch: "e3", n: "John Maynard Keynes", d: "1883-1946", th: "Chômage involontaire dû à une demande effective insuffisante", l: "<i>Théorie générale de l’emploi, de l’intérêt et de la monnaie</i> (1936) : l’emploi dépend de la <b>demande effective</b> anticipée par les entreprises ; un chômage involontaire peut durer, d’où les politiques de relance." },
  { ch: "e3", n: "Carl Shapiro et Joseph Stiglitz", d: "1984 · Nobel 2001 pour Stiglitz", th: "Le salaire d’efficience crée un chômage involontaire qui discipline les salariés", l: "Modèle du <b>salaire d’efficience</b> : l’employeur, qui observe mal l’effort, paie au-dessus du marché ; le chômage involontaire qui en résulte incite à l’effort." },
  { ch: "e3", n: "David Card et Alan Krueger", d: "1994 · Nobel 2021 pour Card", th: "Une hausse du salaire minimum sans baisse de l’emploi (New Jersey)", l: "Expérience naturelle des fast-foods du New Jersey et de la Pennsylvanie : la hausse du <b>salaire minimum</b> de 1992 n’a pas réduit l’emploi." },
  { ch: "e3", n: "Assar Lindbeck et Dennis Snower", d: "1988", th: "Insiders protégés contre outsiders exclus", l: "Théorie <b>insiders / outsiders</b> : les salariés en place, protégés, obtiennent des salaires élevés au détriment des chômeurs et des précaires." },
  { ch: "e3", n: "Diamond, Mortensen et Pissarides", d: "Nobel 2010", th: "Les frictions de recherche expliquent la coexistence de chômeurs et d’emplois vacants", l: "Analyse des marchés avec <b>frictions de recherche</b> : trouver un emploi ou un salarié prend du temps, d’où un chômage d’appariement." }
);
