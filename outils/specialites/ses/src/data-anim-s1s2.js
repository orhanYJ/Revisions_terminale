/* Courbes qui se tracent année par année (utilitaire commun aux animations de séries) */
function ANIM_SERIES(A, x0, y0, w, h, xs, series, ymax, jusqua, opts) {
  opts = opts || {};
  var n = xs.length, X = function (k) { return x0 + w * k / (n - 1); }, Y = function (v) { return y0 - h * v / ymax; };
  var s = "";
  (opts.ticks || []).forEach(function (t) { s += '<line x1="' + x0 + '" x2="' + (x0 + w) + '" y1="' + Y(t) + '" y2="' + Y(t) + '" style="stroke:var(--ligne);stroke-width:1"/>' + A.t(x0 - 4, Y(t) + 4, t + (opts.u || ""), { t: 10.5, a: "end", c: "gris" }); });
  (opts.annees || []).forEach(function (yr) { var k = xs.indexOf(yr); if (k >= 0) s += A.t(X(k), y0 + 16, String(yr), { t: 10.5, a: "middle", c: "gris" }); });
  var kmax = Math.floor(jusqua), fr = jusqua - kmax, labs = [];
  series.forEach(function (sr) {
    var pts = [];
    for (var k = 0; k <= Math.min(kmax, n - 1); k++) pts.push([X(k), Y(sr.v[k])]);
    if (kmax < n - 1 && fr > 0) pts.push([X(kmax) + (X(kmax + 1) - X(kmax)) * fr, Y(sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr)]);
    if (pts.length < 2) pts.push(pts[0]);
    s += A.pl(pts, 1, { c: sr.c, sw: sr.sw || 2.4, op: sr.op });
    var der = pts[pts.length - 1], kv = Math.min(kmax, n - 1), val = kmax < n - 1 ? sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr : sr.v[n - 1];
    s += A.cercle(der[0], der[1], 3.6, { f: sr.c });
    if (sr.lab !== false) labs.push({ x: der[0] + 6, y: der[1] + 4 + (sr.dy || 0), t: (sr.court ? sr.court + " " : "") + A.fr(val, 1) + (opts.u || ""), c: sr.c });
  });
  /* étiquettes de fin de courbe : écartées d’au moins 12 px pour ne jamais se chevaucher */
  labs.sort(function (a, b) { return a.y - b.y; });
  for (var m = 1; m < labs.length; m++) if (labs[m].y - labs[m - 1].y < 12) labs[m].y = labs[m - 1].y + 12;
  labs.forEach(function (l) { s += A.t(l.x, l.y, l.t, { t: 10.5, g: true, c: l.c }); });
  return s;
}

ANIMS["s1-pcs"] = {
  t: "Quarante ans de transformations de l’emploi",
  h: 300,
  src: "Source : Insee, enquête Emploi 2024, séries longues (part de chaque catégorie dans l’emploi, en %). Ruptures de série liées aux changements de l’enquête.",
  etapes: [
    { l: "1982 : les ouvriers sont le premier groupe (29,9 % des personnes en emploi) ; les cadres ne sont que 8,0 %, les agriculteurs encore 7,5 %.", d: 3.5, a: 1990 },
    { l: "Années 1990 : la tertiarisation fait grimper les employés (près de 30 % de l’emploi) pendant que les ouvriers et les agriculteurs reculent.", d: 4, a: 2002 },
    { l: "Années 2000 : la montée des qualifications s’accélère. Les cadres passent de 14,7 % à 18,3 % de 2002 à 2012, les ouvriers tombent à 20,6 %.", d: 4, a: 2012 },
    { l: "2024 : 23,0 % de cadres et 18,0 % d’ouvriers. Pour la première fois depuis 1982, les professions intermédiaires (25,2 %) dépassent les employés (24,8 %).", d: 4.5, a: 2024 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["s1-pcs"], xs = g.x, debut = i === 0 ? 1982 : this.etapes[i - 1].a, fin = this.etapes[i].a;
    var jusqua = (debut - 1982) + (fin - debut) * (i === 0 ? A.s(p, 0, 1) : p);
    var noms = ["Agri.", "Artisans", "Cadres", "Prof. int.", "Employés", "Ouvriers"], dys = [6, -2, 0, -6, -6, 4];
    var ser = g.series.map(function (sr, k) { return { v: sr.v, c: ["vert", "gris", "corail", "moutarde", "#7B5EA7", "canard"][k], court: noms[k], dy: dys[k], sw: k === 2 || k === 5 ? 3 : 2 }; });
    var s = ANIM_SERIES(A, 34, 270, 232, 250, xs, ser, 32, jusqua, { ticks: [0, 10, 20, 30], u: " %", annees: [1982, 1990, 2000, 2010, 2024] });
    var an = Math.round(1982 + jusqua);
    s += A.t(300, 26, String(an), { t: 26, g: true, a: "middle", c: "encre", f: true, op: 0.85 });
    return s;
  }
};

ANIMS["s2-mass"] = {
  t: "Massification… et démocratisation ?",
  h: 300,
  src: "Sources : DEPP, proportion de bacheliers dans une génération (France hors DROM jusqu’en 2000, puis hors Mayotte) ; Observatoire des inégalités d’après le ministère, origine sociale des élèves de CPGE en 2023-2024.",
  etapes: [
    { l: "1970 : 20,1 % d’une génération obtient le bac. Le collège unique (1975) ouvre le secondaire à tous, la hausse reste lente.", d: 4, a: 1985 },
    { l: "1985 : objectif de 80 % d’une génération au niveau du bac et création du bac professionnel. En dix ans, la proportion passe de 29,4 % à 62,7 %.", d: 3.5, a: 1995 },
    { l: "1995-2008 : un palier autour de 62 %.", d: 3, a: 2008 },
    { l: "Réforme du bac professionnel en trois ans (2009) : nouvelle hausse, jusqu’à 80,1 % en 2025. C’est la massification.", d: 4, a: 2025 },
    { l: "Mais qui va où ? En classes préparatoires, 53,7 % des élèves sont enfants de cadres et 6,4 % enfants d’ouvriers : la démocratisation reste ségrégative.", d: 4.5 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["s2-bac"], xs = g.x, s = "";
    var fin = i < 4 ? this.etapes[i].a : 2025, debut = i === 0 ? 1970 : (i < 4 ? this.etapes[i - 1].a : 2025);
    var jusqua = (debut - 1970) + (fin - debut) * (i < 4 ? p : 1);
    var opC = i === 4 ? 1 - 0.75 * A.s(p, 0, 0.4) : 1;
    s += A.g(opC, ANIM_SERIES(A, 38, 270, 276, 240, xs, [{ v: g.series[0].v, c: "corail", sw: 3 }], 100, jusqua, { ticks: [0, 20, 40, 60, 80, 100], u: " %", annees: [1970, 1985, 1995, 2009, 2025] }));
    var jalons = [[1975, "collège unique"], [1985, "objectif 80 %, bac pro"], [2009, "bac pro en 3 ans"]];
    jalons.forEach(function (j) {
      var k = j[0] - 1970; if (k > jusqua) return;
      var x = 34 + 280 * k / (xs.length - 1);
      s += A.g(opC, '<line x1="' + x + '" x2="' + x + '" y1="40" y2="270" style="stroke:var(--moutarde);stroke-width:1.5;stroke-dasharray:3 3"/>' + A.t(x + 4, 48 + (j[0] === 1985 ? 16 : 0), j[1], { t: 10.5, g: true, c: "moutarde" }));
    });
    if (i === 4) {
      var q = A.s(p, 0.25, 0.75);
      s += A.r(20, 60, 320, 182, { f: "carte", s: "ligne", r: 12, op: A.s(p, 0.15, 0.4) });
      s += A.t(180, 86, "Élèves de classes préparatoires (2023-2024)", { t: 13, g: true, a: "middle", op: A.s(p, 0.2, 0.45) });
      s += A.t(36, 124, "enfants de cadres", { t: 12, c: "gris", op: q }) + A.r(36, 130, 260 * 0.537 * q, 22, { f: "canard" }) + A.t(42 + 260 * 0.537 * q, 146, A.fr(53.7 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(36, 178, "enfants d’ouvriers", { t: 12, c: "gris", op: q }) + A.r(36, 184, 260 * 0.064 * q, 22, { f: "corail" }) + A.t(42 + 260 * 0.064 * q, 200, A.fr(6.4 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(180, 222, "pour 23,0 % de cadres et 18,0 % d’ouvriers dans l’emploi (2024)", { t: 10.5, a: "middle", c: "gris", op: A.s(p, 0.7, 1), w: 270, v: true });
    }
    return s;
  }
};

ANIMS["s2-boudon"] = {
  t: "À notes égales, des choix différents",
  h: 320,
  src: "Source du chiffre : ministère de l’Éducation nationale, DEPP, note sur l’orientation en fin de troisième (élèves ayant entre 10 et 12 de moyenne). Mécanisme : R. Boudon, <i>L’Inégalité des chances</i>, 1973.",
  etapes: [
    { l: "Deux élèves ont la même moyenne en fin de troisième, entre 10 et 12.", d: 3 },
    { l: "L’un est enfant de cadre, l’autre enfant d’ouvrier non qualifié. Pour la première famille, une seconde générale coûte peu et ouvre beaucoup ; pour l’autre, le coût et le risque d’échec pèsent plus lourd.", d: 4.5 },
    { l: "Résultat observé : 91 % des enfants de cadres demandent une seconde générale et technologique, contre 59 % des enfants d’ouvriers non qualifiés.", d: 4 },
    { l: "Le même calcul se répète à chaque palier (seconde, bac, études supérieures) : les écarts s’additionnent.", d: 3.5 },
    { l: "C’est l’effet d’agrégation décrit par Raymond Boudon : des choix individuels raisonnables produisent des inégalités collectives que personne n’a voulues.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", E = [{ n: "Enfant de cadre", x: 20, c: "canard", v: 91 }, { n: "Enfant d’ouvrier non qualifié", x: 190, c: "corail", v: 59 }];
    E.forEach(function (e, k) {
      s += A.cercle(e.x + 75, 34, 13, { f: e.c }) + A.r(e.x + 62, 50, 26, 30, { f: e.c, r: 8 });
      s += A.t(e.x + 75, 98, e.n, { t: 12, g: true, a: "middle", w: 150 });
      s += A.jauge(e.x + 10, 132, 130, 11, 20, { c: "moutarde", l: "moyenne en 3e", val: "10 à 12" });
      if (i >= 1) {
        var q = i === 1 ? A.s(p, 0.1 + k * 0.2, 0.6 + k * 0.2) : 1, pente = k === 0 ? -8 : 8;
        s += A.g(q, '<line x1="' + (e.x + 25) + '" x2="' + (e.x + 125) + '" y1="' + (176 - pente) + '" y2="' + (176 + pente) + '" style="stroke:var(--encre);stroke-width:2.5"/>' +
          A.t(e.x + 25, 162 - pente, "gains", { t: 11, a: "middle", c: "vert", g: true }) + A.t(e.x + 125, 162 + pente, "coûts", { t: 11, a: "middle", c: "corail", g: true }) +
          '<path d="M' + (e.x + 70) + ' 196L' + (e.x + 80) + ' 196L' + (e.x + 75) + ' 178z" style="fill:var(--encre2)"/>');
      }
      if (i >= 2) {
        var q2 = i === 2 ? A.s(p, 0.1, 0.8) : 1;
        s += A.t(e.x + 10, 222, "2de générale demandée", { t: 11, c: "gris" });
        s += A.r(e.x + 10, 228, 110, 14, { f: "carte2", r: 6 }) + A.r(e.x + 10, 228, 110 * e.v / 100 * q2, 14, { f: e.c, r: 6 });
        s += A.t(e.x + 125, 240, A.fr(e.v * q2, 0) + " %", { t: 12.5, g: true });
      }
    });
    if (i >= 3) {
      var q3 = i === 3 ? A.s(p, 0, 0.8) : 1;
      ["3e → 2de", "2de → bac", "bac → supérieur"].forEach(function (pal, k) {
        var x = 30 + k * 108;
        s += A.boite(x, 262, 96, 28, pal, { k: "neutre", t: 11, op: A.s(q3, k * 0.25, k * 0.25 + 0.4) });
        if (k < 2) s += A.fl(x + 98, 276, x + 106, 276, { c: "gris", p: A.s(q3, k * 0.25 + 0.2, k * 0.25 + 0.5) });
      });
    }
    if (i === 4) s += A.t(180, 310, "des choix individuels → une inégalité collective", { t: 12.5, g: true, a: "middle", c: "corail", op: A.s(p, 0.3, 0.8) });
    return s;
  }
};

ANIMS["s1-marx-weber"] = {
  t: "Deux façons de découper la société : Marx et Weber",
  h: 320,
  src: "Schéma de principe. Positions illustratives sur les échelles de Weber.",
  etapes: [
    { l: "Marx : une seule ligne de partage, la propriété des moyens de production. D’un côté la bourgeoisie, peu nombreuse ; de l’autre le prolétariat.", d: 3.5 },
    { l: "Le prolétaire vend sa force de travail ; le bourgeois s’approprie la plus-value. Leurs intérêts sont opposés.", d: 3.5 },
    { l: "Classe en soi, puis classe pour soi : quand les ouvriers prennent conscience de leurs intérêts communs, ils se mobilisent. C’est la lutte des classes.", d: 3.5 },
    { l: "Weber : non pas une mais trois échelles, indépendantes. Ordre économique (classes), ordre social (prestige des groupes de statut), ordre politique (partis).", d: 4 },
    { l: "Une même personne peut être haut sur une échelle et bas sur une autre : un professeur a plus de prestige que de revenu, un commerçant aisé l’inverse.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "";
    function pers(x, y, c, op) { return A.cercle(x, y - 8, 4.5, { f: c, op: op }) + A.r(x - 5, y - 3, 10, 11, { f: c, r: 3, op: op }); }
    var opM = i <= 2 ? 1 : 1 - A.s(p, 0, 0.5);
    if (opM > 0.02) {
      var m = A.boite(110, 20, 140, 40, "Bourgeoisie : propriétaires", { k: "cause", t: 12, g: true }) ;
      for (var k = 0; k < 3; k++) m += pers(150 + k * 30, 84, "canard");
      m += '<line x1="20" x2="340" y1="112" y2="112" style="stroke:var(--encre);stroke-width:3"/>' + A.t(20, 101, "propriété des moyens de production", { t: 10.5, c: "gris", w: 118, v: true });
      var conscience = i >= 2 ? (i === 2 ? A.s(p, 0.2, 0.8) : 1) : 0;
      for (var j = 0; j < 12; j++) {
        var x0 = 30 + j * 26, y0 = 160 + (j % 2) * 26, xf = 120 + (j % 6) * 24, yf = 158 + Math.floor(j / 6) * 26;
        m += pers(A.l(x0, xf, conscience), A.l(y0, yf, conscience), "corail");
      }
      m += A.boite(110, 214, 140, 38, "Prolétariat : vend sa force de travail", { k: "effet", t: 11.5, g: true });
      if (i >= 1) m += A.fl(180, 150, 180, 96, { c: "moutarde", sw: 3, p: i === 1 ? A.s(p, 0.1, 0.7) : 1 }) + A.t(188, 130, "plus-value", { t: 11.5, g: true, c: "moutarde", op: i === 1 ? A.s(p, 0.4, 0.9) : 1, h: true });
      if (i >= 2) m += A.t(180, 278, "classe pour soi : conscience et lutte", { t: 12.5, g: true, a: "middle", c: "corail", op: conscience });
      s += A.g(opM, m);
    }
    if (i >= 3) {
      var opW = i === 3 ? A.s(p, 0.3, 0.9) : 1, axes = [["Économique : revenus, patrimoine", 70], ["Social : prestige", 150], ["Politique : pouvoir", 230]];
      var w = "";
      axes.forEach(function (ax, k) {
        w += A.t(20, ax[1] - 14, ax[0], { t: 12, g: true }) + A.fl(20, ax[1], 340, ax[1], { c: "gris", sw: 2 }) + A.t(20, ax[1] + 16, "bas", { t: 10, c: "gris" }) + A.t(340, ax[1] + 16, "haut", { t: 10, c: "gris", a: "end" });
      });
      if (i === 4) {
        var q = A.s(p, 0.1, 0.8), prof = [150, 280, 170], comm = [270, 140, 150];
        axes.forEach(function (ax, k) {
          w += A.cercle(A.l(180, prof[k], q), ax[1], 8, { f: "canard", s: "carte", sw: 2 }) + A.cercle(A.l(180, comm[k], q), ax[1], 8, { f: "moutarde", s: "carte", sw: 2 });
        });
        w += A.cercle(40, 296, 7, { f: "canard" }) + A.t(52, 300, "professeur", { t: 11.5, g: true }) + A.cercle(170, 296, 7, { f: "moutarde" }) + A.t(182, 300, "commerçant aisé", { t: 11.5, g: true });
      }
      s += A.g(opW, w);
    }
    return s;
  }
};
