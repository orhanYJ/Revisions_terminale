/* Courbes qui se tracent année par année (utilitaire commun aux animations de séries) */
function ANIM_SERIES(A, x0, y0, w, h, xs, series, ymax, jusqua, opts) {
  opts = opts || {};
  var n = xs.length, X = function (k) { return x0 + w * k / (n - 1); }, Y = function (v) { return y0 - h * v / ymax; };
  var s = "";
  (opts.ticks || []).forEach(function (t) { s += '<line x1="' + x0 + '" x2="' + (x0 + w) + '" y1="' + Y(t) + '" y2="' + Y(t) + '" style="stroke:var(--ligne);stroke-width:1"/>' + A.t(x0 - 4, Y(t) + 4, t + (opts.u || ""), { t: 9.5, a: "end", c: "gris" }); });
  (opts.annees || []).forEach(function (yr) { var k = xs.indexOf(yr); if (k >= 0) s += A.t(X(k), y0 + 16, String(yr), { t: 9.5, a: "middle", c: "gris" }); });
  var kmax = Math.floor(jusqua), fr = jusqua - kmax;
  series.forEach(function (sr) {
    var pts = [];
    for (var k = 0; k <= Math.min(kmax, n - 1); k++) pts.push([X(k), Y(sr.v[k])]);
    if (kmax < n - 1 && fr > 0) pts.push([X(kmax) + (X(kmax + 1) - X(kmax)) * fr, Y(sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr)]);
    if (pts.length < 2) pts.push(pts[0]);
    s += A.pl(pts, 1, { c: sr.c, sw: sr.sw || 2.4, op: sr.op });
    var der = pts[pts.length - 1], kv = Math.min(kmax, n - 1), val = kmax < n - 1 ? sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr : sr.v[n - 1];
    s += A.cercle(der[0], der[1], 3.6, { f: sr.c });
    if (sr.lab !== false) s += A.t(der[0] + 6, der[1] + 4 + (sr.dy || 0), (sr.court ? sr.court + " " : "") + A.fr(val, 1) + (opts.u || ""), { t: 10.5, g: true, c: sr.c });
  });
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
    s += A.g(opC, ANIM_SERIES(A, 34, 270, 280, 240, xs, [{ v: g.series[0].v, c: "corail", sw: 3 }], 100, jusqua, { ticks: [0, 20, 40, 60, 80, 100], u: " %", annees: [1970, 1985, 1995, 2009, 2025] }));
    var jalons = [[1975, "collège unique"], [1985, "objectif 80 %, bac pro"], [2009, "bac pro en 3 ans"]];
    jalons.forEach(function (j) {
      var k = j[0] - 1970; if (k > jusqua) return;
      var x = 34 + 280 * k / (xs.length - 1);
      s += A.g(opC, '<line x1="' + x + '" x2="' + x + '" y1="40" y2="270" style="stroke:var(--moutarde);stroke-width:1.5;stroke-dasharray:3 3"/>' + A.t(x + 4, 48 + (j[0] === 1985 ? 16 : 0), j[1], { t: 10.5, g: true, c: "moutarde" }));
    });
    if (i === 4) {
      var q = A.s(p, 0.25, 0.75);
      s += A.r(20, 60, 320, 170, { f: "carte", s: "ligne", r: 12, op: A.s(p, 0.15, 0.4) });
      s += A.t(180, 86, "Élèves de classes préparatoires (2023-2024)", { t: 13, g: true, a: "middle", op: A.s(p, 0.2, 0.45) });
      s += A.t(36, 124, "enfants de cadres", { t: 12, c: "gris", op: q }) + A.r(36, 130, 260 * 0.537 * q, 22, { f: "canard" }) + A.t(42 + 260 * 0.537 * q, 146, A.fr(53.7 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(36, 178, "enfants d’ouvriers", { t: 12, c: "gris", op: q }) + A.r(36, 184, 260 * 0.064 * q, 22, { f: "corail" }) + A.t(42 + 260 * 0.064 * q, 200, A.fr(6.4 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(180, 222, "pour 23,0 % de cadres et 18,0 % d’ouvriers dans l’emploi (2024)", { t: 10.5, a: "middle", c: "gris", op: A.s(p, 0.7, 1) });
    }
    return s;
  }
};
