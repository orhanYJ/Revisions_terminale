ANIMS["e1-solow"] = {
  t: "Pourquoi le progrès technique est indispensable",
  h: 300,
  src: "Schéma de principe (fonction de production à rendements décroissants, valeurs illustratives). Résidu : R. Solow, 1957, données des États-Unis 1909-1949.",
  etapes: [
    { l: "Avec plus de capital par travailleur (machines, outils, logiciels), chacun produit davantage : c’est la fonction de production.", d: 3.5 },
    { l: "Mais les rendements sont décroissants : chaque nouvelle machine rapporte moins que la précédente.", d: 4.5 },
    { l: "Accumuler du capital seul mène à un plafond : la production par travailleur augmente de moins en moins (modèle de Solow, 1956).", d: 4 },
    { l: "Le progrès technique déplace toute la courbe vers le haut : avec le même capital, on produit plus. C’est la hausse de la productivité globale des facteurs.", d: 4 },
    { l: "Ce supplément qui ne vient pas des facteurs, Solow l’appelle le « résidu » : environ 87,5 % de la hausse de la production par heure aux États-Unis de 1909 à 1949.", d: 3.5 }
  ],
  rendu: function (A, i, p) {
    var x0 = 46, y0 = 262, X = function (k) { return x0 + k * 29; }, Y = function (v) { return y0 - v * 60; };
    function f(k, a) { return a * Math.pow(k, 0.4); }
    function courbe(a) { var pts = []; for (var k = 0; k <= 10.001; k += 0.25) pts.push([X(k), Y(f(k, a))]); return pts; }
    var s = A.axes(x0, y0, 300, 236, { lx: "capital par travailleur", ly: "production par travailleur" });
    var pa = i === 0 ? p : 1;
    s += A.pl(courbe(1), pa, { c: i >= 3 ? "gris" : "canard", tir: i >= 3, sw: i >= 3 ? 1.8 : 2.8 });
    if (i === 0) s += A.t(X(9.4), Y(f(9.4, 1)) - 10, "fonction de production", { t: 11.5, a: "end", c: "canard", op: A.s(p, 0.6, 1) });
    if (i >= 1) {
      var marches = [[1, 3], [3, 5], [5, 7], [7, 9]];
      marches.forEach(function (m, j) {
        var q = i === 1 ? A.s(p, j * 0.22, j * 0.22 + 0.3) : 1;
        if (q <= 0) return;
        var ya = Y(f(m[0], 1)), yb = Y(f(m[1], 1)), op = i >= 3 ? 0.35 : 1;
        s += A.g(op, A.fl(X(m[0]), ya, X(m[0]) + (X(m[1]) - X(m[0])) * q, ya, { c: "gris", sw: 1.2, tete: false }) +
          (q > 0.5 ? A.r(X(m[1]) - 3, yb, 6, (ya - yb) * A.s(q, 0.5, 1), { f: "corail", r: 2 }) : "") +
          A.t(X(m[1]) + 6, (ya + yb) / 2 + 4, "+" + A.fr(f(m[1], 1) - f(m[0], 1), 2), { t: 10.5, g: true, c: "corail", op: A.s(q, 0.7, 1) }));
      });
      if (i === 1) s += A.t(X(3.2), Y(0.75), "même ajout de capital, gain de production qui diminue", { t: 11, c: "corail", op: A.s(p, 0.85, 1), w: 190, h: true });
    }
    if (i === 2) {
      var k = A.l(2, 9, A.s(p, 0, 0.9));
      s += A.cercle(X(k), Y(f(k, 1)), 7, { f: "corail", s: "carte", sw: 2 });
      s += A.t(X(5.5), Y(0.45), "la croissance s’essouffle", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.6, 1) });
    }
    if (i >= 3) {
      var a = i === 3 ? A.l(1, 1.35, A.s(p, 0, 0.8)) : 1.35;
      s += A.pl(courbe(a), 1, { c: "canard", sw: 2.8 });
      var yh = Y(f(9, a));
      s += A.cercle(X(9), yh, 7, { f: "corail", s: "carte", sw: 2 });
      s += A.t(X(0.6), Y(2.75), "après progrès technique", { t: 11.5, c: "canard", g: true, op: i === 3 ? A.s(p, 0.6, 1) : 1, h: true });
      s += A.fl(X(4), Y(f(4, 1)) - 4, X(4), Y(f(4, a)) + 6, { c: "canard", sw: 2, op: i === 3 ? A.s(p, 0.3, 0.7) : 1 });
    }
    if (i === 4) {
      var ya1 = Y(f(9, 1)), ya2 = Y(f(9, 1.35)), q = A.s(p, 0, 0.6);
      s += A.r(X(9) - 22, ya2, 44, (ya1 - ya2) * q, { f: "moutarde", op: 0.35, r: 3 });
      s += A.t(X(5.6), Y(0.9), "PGF : le « résidu »", { t: 13, g: true, a: "middle", c: "encre", op: A.s(p, 0.4, 1), h: true });
      s += A.fl(X(6.6), Y(0.98), X(9) - 22, (ya1 + ya2) / 2 + 6, { c: "moutarde", sw: 2, p: A.s(p, 0.5, 1) });
    }
    return s;
  }
};

ANIMS["e1-pib"] = {
  t: "75 ans de croissance française, année par année",
  h: 290,
  src: "Source : Insee, comptes nationaux annuels, base 2020 (mai 2026). Taux de croissance du PIB en volume ; moyennes calculées à partir des niveaux.",
  etapes: [
    { l: "1950-1973, les « Trente Glorieuses » : la France rattrape son retard, la croissance dépasse souvent 5 % (5,2 % par an en moyenne).", d: 5, de: 1950, a: 1973 },
    { l: "Les chocs pétroliers : en 1975, le PIB recule (−0,9 %). La croissance ne retrouvera plus ce rythme.", d: 2.5, de: 1974, a: 1975 },
    { l: "1976-2007 : une croissance ralentie et heurtée (2,4 % par an en moyenne de 1973 à 2007), avec une récession en 1993 (−0,4 %).", d: 5, de: 1976, a: 2007 },
    { l: "La crise financière : −2,8 % en 2009, la plus forte récession depuis 1950 jusque-là.", d: 2.5, de: 2008, a: 2009 },
    { l: "Les années 2010 : une croissance faible, 1,4 % par an en moyenne de 2010 à 2019.", d: 4, de: 2010, a: 2019 },
    { l: "Covid : −7,4 % en 2020, rebond de +6,9 % en 2021, puis +1,6 %, +1,5 % et +0,8 % de 2023 à 2025.", d: 4, de: 2020, a: 2025 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["e1-pib"], xs = g.x, ys = g.y, n = xs.length;
    var x0 = 34, w = 316, yz = 158, sc = 12, bw = w / n;
    var Y = function (v) { return yz - v * sc; };
    var s = "";
    [-8, -4, 0, 4, 8].forEach(function (t) { s += '<line x1="' + x0 + '" x2="' + (x0 + w) + '" y1="' + Y(t) + '" y2="' + Y(t) + '" style="stroke:var(--' + (t === 0 ? "encre2" : "ligne") + ');stroke-width:1"/>' + A.t(x0 - 5, Y(t) + 4, (t > 0 ? "+" : "") + t + " %", { t: 9.5, a: "end", c: "gris" }); });
    [1950, 1970, 1990, 2010, 2025].forEach(function (yr) { s += A.t(x0 + (yr - 1950 + 0.5) * bw, 282, String(yr), { t: 9.5, a: "middle", c: "gris" }); });
    var etapes = this.etapes;
    var et = etapes[i], fin = et.a, debut = et.de, nb = fin - debut + 1;
    var courant = debut + (nb) * p;
    if (i >= 0) {
      var bande = etapes[i];
      s += A.r(x0 + (bande.de - 1950) * bw, 10, (bande.a - bande.de + 1) * bw, 255, { f: "moutardec", op: 0.6, r: 0 });
    }
    for (var k = 0; k < n; k++) {
      var yr = xs[k], q;
      if (yr < debut) q = 1; else if (yr > fin) q = 0; else q = Math.max(0, Math.min(1, courant - yr));
      if (q <= 0) continue;
      var v = ys[k] * A.s(q, 0, 1), y1 = Y(Math.max(0, v)), y2 = Y(Math.min(0, v));
      s += A.r(x0 + k * bw + 0.5, y1, bw - 1, Math.max(0.6, y2 - y1), { f: ys[k] < 0 ? "corail" : "canard", r: 1 });
    }
    var dernier = Math.min(fin, Math.floor(courant));
    if (dernier >= debut) {
      var kk = dernier - 1950, val = ys[kk];
      s += A.t(x0 + (kk + 0.5) * bw, val >= 0 ? Y(val) - 6 : Y(val) + 14, String(dernier) + " : " + (val > 0 ? "+" : "") + A.fr(val, 1) + " %", { t: 11, g: true, a: kk > 60 ? "end" : kk < 6 ? "start" : "middle", c: val < 0 ? "corail" : "encre", h: true });
    }
    return s;
  }
};
