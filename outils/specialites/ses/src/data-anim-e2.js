ANIMS["e2-ricardo"] = {
  t: "L’avantage comparatif se construit",
  h: 345,
  src: "Exemple de David Ricardo, <i>Des principes de l’économie politique et de l’impôt</i>, 1817 (heures de travail pour une unité de chaque bien).",
  etapes: [
    { l: "Heures de travail pour produire une unité : en Angleterre, 100 h pour le drap et 120 h pour le vin ; au Portugal, 90 h et 80 h.", d: 3.5 },
    { l: "Le Portugal est plus productif dans les deux biens : il a un avantage absolu partout. L’échange serait-il inutile ?", d: 3 },
    { l: "Comparons les coûts relatifs. En Angleterre, un drap coûte 100/120 = 0,83 vin ; au Portugal, 90/80 = 1,125 vin. L’Angleterre a un avantage comparatif en drap, le Portugal en vin.", d: 4.5 },
    { l: "Sans échange, chaque pays produit une unité de chaque bien : le monde dispose de 2 draps et de 2 vins.", d: 3 },
    { l: "Chacun se spécialise : l’Angleterre met ses 220 h dans le drap (2,2 draps), le Portugal ses 170 h dans le vin (2,125 vins).", d: 4 },
    { l: "Avec le même travail, le monde produit 0,2 drap et 0,125 vin de plus. L’échange partage ce gain : les deux pays y gagnent.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", pays = [{ n: "Angleterre", x: 12, h: [100, 120], aut: [1, 1], spe: [2.2, 0] }, { n: "Portugal", x: 186, h: [90, 80], aut: [1, 1], spe: [0, 2.125] }];
    var biens = [{ n: "drap", c: "canard" }, { n: "vin", c: "corail" }];
    pays.forEach(function (P, j) {
      s += A.t(P.x + 81, 20, P.n, { t: 15, g: true, a: "middle", f: true });
      s += '<line x1="' + P.x + '" x2="' + (P.x + 162) + '" y1="28" y2="28" style="stroke:var(--encre);stroke-width:2"/>';
      biens.forEach(function (b, k) {
        var y = 44 + k * 30, q = i === 0 ? A.s(p, k * 0.3 + j * 0.15, k * 0.3 + j * 0.15 + 0.5) : 1;
        var hl = (i === 1 && j === 1) ? 1 : 0;
        s += A.t(P.x, y + 13, b.n, { t: 11.5, c: "gris" });
        s += A.r(P.x + 34, y, P.h[k] * 0.8 * q, 18, { f: b.c, op: i === 1 && j === 0 ? 0.45 : 1, s: hl ? "moutarde" : null, sw: 3 });
        s += A.t(P.x + 40 + P.h[k] * 0.8 * q, y + 13, A.fr(P.h[k] * q, 0) + " h", { t: 11.5, g: true, op: q });
      });
      if (i === 1 && j === 1) s += A.t(P.x + 81, 120, "avantage absolu dans les deux biens", { t: 11.5, g: true, a: "middle", c: "moutarde", op: A.s(p, 0.3, 0.8) });
      if (i >= 2) {
        var ratio = P.h[0] / P.h[1], q2 = i === 2 ? A.s(p, j * 0.3, j * 0.3 + 0.5) : 1;
        s += A.t(P.x + 81, 120, "1 drap = " + A.fr(ratio, ratio === 1.125 ? 3 : 2) + " vin", { t: 13, g: true, a: "middle", op: q2 });
        s += A.t(P.x + 81, 138, j === 0 ? "avantage comparatif : drap" : "avantage comparatif : vin", { t: 11.5, a: "middle", c: j === 0 ? "canard" : "corail", g: true, op: i === 2 ? A.s(p, 0.6 + j * 0.15, 0.95) : 1 });
      }
      if (i >= 3) {
        var q3 = i === 3 ? A.s(p, 0, 0.6) : 1, t4 = i === 4 ? A.s(p, 0.1, 0.8) : (i > 4 ? 1 : 0);
        s += A.g(q3, A.t(P.x, 172, "Production", { t: 11, c: "gris", g: true }));
        biens.forEach(function (b, k) {
          var qte = A.l(P.aut[k], P.spe[k], t4), y = 180 + k * 28;
          s += A.g(q3, A.t(P.x, y + 13, b.n, { t: 11.5, c: "gris" }) + A.r(P.x + 34, y, qte * 46, 18, { f: b.c }) + (qte > 0.02 ? A.t(P.x + 40 + qte * 46, y + 13, A.fr(qte, Math.abs(qte - 2.125) < 1e-9 ? 3 : (Math.abs(qte * 10 - Math.round(qte * 10)) < 1e-9 ? (qte % 1 ? 1 : 0) : 2)), { t: 11.5, g: true }) : ""));
        });
      }
    });
    if (i >= 3) {
      var t4b = i === 4 ? A.s(p, 0.1, 0.8) : (i > 4 ? 1 : 0), q3b = i === 3 ? A.s(p, 0.4, 1) : 1;
      var dr = A.l(2, 2.2, t4b), vi = A.l(2, 2.125, t4b);
      s += A.g(q3b, A.r(12, 244, 336, 34, { f: "carte2", r: 8 }) + A.t(180, 266, "Monde : " + A.fr(dr, dr === 2 ? 0 : (dr > 2.19 ? 1 : 2)) + " draps et " + A.fr(vi, vi === 2 ? 0 : 3) + " vins", { t: 14, g: true, a: "middle" }));
    }
    if (i === 5) {
      s += A.fl(70, 296, 290, 296, { c: "canard", sw: 2.4, p: A.s(p, 0, 0.4) }) + A.t(180, 291, "drap anglais", { t: 11, a: "middle", c: "canard", g: true, op: A.s(p, 0.2, 0.4), h: true });
      s += A.fl(290, 312, 70, 312, { c: "corail", sw: 2.4, p: A.s(p, 0.2, 0.6) }) + A.t(180, 325, "vin portugais", { t: 11, a: "middle", c: "corail", g: true, op: A.s(p, 0.4, 0.6), h: true });
      s += A.t(180, 342, "gain : +0,2 drap et +0,125 vin, à partager par l’échange", { t: 12.5, g: true, a: "middle", c: "encre", op: A.s(p, 0.6, 1) });
    }
    return s;
  }
};

ANIMS["e2-iphone"] = {
  t: "Le voyage d’un iPhone 3G (2009)",
  h: 300,
  src: "Source : Y. Xing et N. Detert, ADBI Working Paper n° 257, décembre 2010, d’après des estimations d’iSuppli (2009). Coût de fabrication : 178,96 $, dont 6,50 $ d’assemblage en Chine.",
  etapes: [
    { l: "Apple conçoit l’iPhone aux États-Unis. Ses composants viennent de fournisseurs de plusieurs pays : Japon, Allemagne, Corée du Sud, États-Unis…", d: 3 },
    { l: "Les composants, 172,46 $ par appareil, sont expédiés vers l’usine d’assemblage en Chine.", d: 3.5 },
    { l: "En Chine, l’usine assemble le téléphone : 6,50 $ de valeur ajoutée, soit 3,6 % du coût de fabrication.", d: 3.5 },
    { l: "L’iPhone part vers les États-Unis : la statistique douanière enregistre une importation de 178,96 $ en provenance de Chine.", d: 3.5 },
    { l: "En valeur ajoutée, la Chine n’a produit que 6,50 $ sur 178,96 $. Le commerce mesuré en valeur brute exagère son rôle : d’où le commerce en valeur ajoutée.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", four = ["Japon", "Allemagne", "Corée du Sud", "États-Unis"];
    four.forEach(function (n, k) {
      var q = i === 0 ? A.s(p, k * 0.18, k * 0.18 + 0.4) : 1;
      s += A.boite(6, 18 + k * 46, 96, 36, n, { k: "neutre", op: q, t: 12 });
    });
    s += A.t(54, 205, "fournisseurs", { t: 10.5, a: "middle", c: "gris", op: i === 0 ? A.s(p, 0.7, 1) : 1 });
    var chine = i >= 1 ? (i === 1 ? A.s(p, 0, 0.3) : 1) : 0;
    s += A.boite(146, 80, 84, 52, "Chine : assemblage", { k: i >= 2 ? "effet" : "meca", op: chine, t: 12.5, g: true });
    var us = i >= 3 ? (i === 3 ? A.s(p, 0, 0.3) : 1) : 0;
    s += A.boite(270, 80, 84, 52, "États-Unis : vente", { k: "cause", op: us, t: 12.5, g: true });
    if (i >= 1) {
      four.forEach(function (n, k) {
        var y = 36 + k * 46, q = i === 1 ? A.s(p, 0.15 + k * 0.1, 0.65 + k * 0.1) : 1;
        s += A.fl(104, y, 144, 106, { c: "gris", p: q, sw: 1.4 });
        if (i === 1 && q > 0 && q < 1) s += A.r(104 + 40 * q - 5, y + (106 - y) * q - 5, 10, 10, { f: "canard", r: 2 });
      });
    }
    if (i >= 3) {
      var q3 = i === 3 ? A.s(p, 0.2, 0.8) : 1;
      s += A.fl(232, 106, 268, 106, { c: "corail", sw: 2.4, p: q3 });
      if (i === 3) s += A.t(352, 160, "importation : 178,96 $", { t: 12, g: true, a: "end", c: "corail", op: A.s(p, 0.6, 1), h: true });
    }
    var x0 = 20, L = 320, sc = L / 178.96, yb = 238;
    if (i >= 1) {
      var qc = i === 1 ? A.s(p, 0.4, 1) : 1;
      s += A.t(x0, yb - 8, "Coût de fabrication d’un appareil", { t: 11, c: "gris", g: true });
      s += A.r(x0, yb, 172.46 * sc * qc, 26, { f: "canard", r: 3 });
      if (qc > 0.6) s += A.t(x0 + 8, yb + 17, "composants 172,46 $", { t: 12, g: true, c: "carte" });
    }
    if (i >= 2) {
      var qa = i === 2 ? A.s(p, 0.3, 0.8) : 1;
      s += A.r(x0 + 172.46 * sc, yb, 6.5 * sc * qa, 26, { f: "corail", r: 2 });
      s += A.t(x0 + L, yb + 44, "assemblage chinois : 6,50 $ (3,6 %)", { t: 12, g: true, a: "end", c: "corail", op: i === 2 ? A.s(p, 0.6, 1) : 1 });
    }
    if (i === 4) {
      s += A.r(x0 - 3, yb - 3, L + 6, 32, { f: "none", s: "moutarde", sw: 2.5, op: A.s(p, 0, 0.4) });
      s += A.t(352, 160, "valeur ajoutée chinoise : 3,6 %", { t: 13.5, g: true, a: "end", c: "corail", op: A.s(p, 0.2, 0.7), h: true });
      s += A.t(352, 178, "valeur brute comptée : 100 %", { t: 12, a: "end", c: "gris", op: A.s(p, 0.4, 0.9), h: true });
    }
    return s;
  }
};
