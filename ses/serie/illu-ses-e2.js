/* Illustrations propres à la vidéo SES É2 (le commerce international), chargées après ses/serie/moteur.js.
   SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; } ; rendu fonction pure du temps.
   elephant : la « courbe de l'éléphant » (Lakner et Milanovic), schéma de principe sans données ; {id.1} le dos
     (classes moyennes des pays émergents), {id.2} le creux (classes populaires et moyennes des pays riches), {id.3} la
     trompe (les plus riches du monde).
   airbus : la chaîne de valeur de l'Airbus A320 ; {id.1} les pays qui produisent les éléments, {id.2} les quatre lignes
     d'assemblage final. */
(function () {
  "use strict";
  var O = window.SERIE_OUTILS, sv = O.sv, etiquette = O.etiquette, C = O.C, E = O.E, EIO = O.EIO, P = O.P, op = O.op,
    et = O.et, trace = O.trace, tr = O.tr;
  window.SERIE_ILLU = window.SERIE_ILLU || {};

  window.SERIE_ILLU.elephant = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s);
    var x0 = 110, x1 = W_ - 40, y0 = H_ - 130, y1 = 40;
    var X = function (c) { return x0 + (x1 - x0) * c / 100; }, Y = function (q) { return y0 - (y0 - y1) * q / 100; };
    var ax = sv("path", { d: "M" + x0 + " " + y1 + " V" + y0 + " H" + x1, fill: "none", stroke: C.iv, "stroke-width": 2.4 }, g);
    var lx = etiquette(g, (x0 + x1) / 2, y0 + 46, "les habitants du monde, du plus pauvre au plus riche →", { fs: 23, c: C.iv2, fw: 500 });
    var ly = sv("text", { x: 0, y: 0, "text-anchor": "middle", fill: C.iv2, "font-size": 23, "font-weight": 500,
      transform: "translate(" + (x0 - 34) + " " + ((y0 + y1) / 2) + ") rotate(-90)" }, g, "hausse du revenu, 1988-2008 →");
    var pts = [[2, 22], [10, 30], [20, 40], [30, 52], [40, 63], [50, 70], [58, 72], [65, 64], [72, 44], [78, 20], [84, 6],
      [88, 4], [92, 12], [96, 30], [99, 58]];
    var d = "M" + X(pts[0][0]) + " " + Y(pts[0][1]);
    for (var i = 1; i < pts.length; i++) {
      var a = pts[i - 1], b = pts[i], mx = (X(a[0]) + X(b[0])) / 2;
      d += " C" + mx + " " + Y(a[1]) + " " + mx + " " + Y(b[1]) + " " + X(b[0]) + " " + Y(b[1]);
    }
    var courbe = sv("path", { d: d, fill: "none", stroke: C.canard, "stroke-width": 7, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
    var lg = etiquette(g, x0, H_ - 22, "Schéma de principe (sans données)", { ancre: "start", fs: 20, c: C.iv2, fw: 500 });
    // [centile, hausse, titre, texte, couleur, ancre, x du texte (décalage), y du titre]
    var reperes = [
      [56, 72, "le dos", "classes moyennes des pays émergents : forte hausse", C.vert, "end", -24, 40],
      [86, 4, "le creux", "classes populaires et moyennes des pays riches : peu de hausse", C.corail, "end", -150, Y(4) - 34],
      [99, 58, "la trompe", "les plus riches du monde : forte hausse", C.mo, "end", 10, 40]
    ].map(function (r) {
      var gg = sv("g", {}, g), cx = X(r[0]), cy = Y(r[1]), tx = cx + r[6], ty = r[7];
      sv("circle", { cx: cx, cy: cy, r: 13, fill: r[4] }, gg);
      var ly2 = ty + 16, lx2 = r[6] < 0 ? tx + 8 : cx;
      if (r[0] === 86) sv("path", { d: "M" + (cx - 15) + " " + (cy - 4) + " L" + lx2 + " " + (ty + 8), stroke: r[4], "stroke-width": 2.4, fill: "none" }, gg);
      else sv("path", { d: "M" + cx + " " + (cy - 16) + " V" + (ty + 44) + (r[6] < 0 ? " H" + (tx + 8) : ""), stroke: r[4], "stroke-width": 2.4, fill: "none" }, gg);
      etiquette(gg, tx, ty, r[2], { ancre: r[5], fs: 30, c: r[4], fw: 700 });
      etiquette(gg, tx, ty + 30, r[3], { ancre: r[5], fs: 21, c: C.iv, fw: 500 });
      return gg;
    });
    return function (t, st) {
      var tl = st.tl;
      op(ax, E(P(tl, 0, .5))); op(lx, E(P(tl, .3, .6))); op(ly, E(P(tl, .3, .6))); op(lg, E(P(tl, .4, .6)) * .9);
      trace(courbe, EIO(P(tl, .6, 2.6)));
      reperes.forEach(function (r, k) {
        var q = E(P(t, et(v, String(k + 1), 4 + k * 3), .7));
        op(r, q); tr(r, "translateY(" + (14 * (1 - q)) + "px)");
      });
    };
  };

  window.SERIE_ILLU.airbus = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), bw = 330, bh = 74, gap = 22;
    var top = (H_ - (4 * bh + 3 * gap)) / 2 + 20, cx = W_ / 2, cy = top + 2 * bh + 1.5 * gap;
    function boite(x, y, t1, t2, col) {
      var gg = sv("g", {}, g);
      sv("rect", { x: x, y: y, width: bw, height: bh, rx: 10, fill: "#FBF8F1", stroke: col, "stroke-width": 2.6 }, gg);
      etiquette(gg, x + bw / 2, y + (t2 ? 33 : 46), t1, { fs: 27, c: C.iv, fw: 700 });
      if (t2) etiquette(gg, x + bw / 2, y + 60, t2, { fs: 20, c: C.iv2, fw: 500 });
      return gg;
    }
    var tg = etiquette(g, 40 + bw / 2, top - 26, "Éléments produits en…", { fs: 23, c: C.canard, fw: 700 });
    var td = etiquette(g, W_ - 40 - bw / 2, top - 26, "Assemblage final à…", { fs: 23, c: C.sa, fw: 700 });
    var gauche = [["France", ""], ["Allemagne", ""], ["Espagne", ""], ["Royaume-Uni", "les ailes"]].map(function (p, k) {
      return boite(40, top + k * (bh + gap), p[0], p[1], C.canard);
    });
    var droite = [["Toulouse", "France"], ["Hambourg", "Allemagne"], ["Tianjin", "Chine"], ["Mobile", "États-Unis"]].map(function (p, k) {
      return boite(W_ - 40 - bw, top + k * (bh + gap), p[0], p[1], C.sa);
    });
    var centre = sv("g", {}, g);
    sv("circle", { cx: cx, cy: cy, r: 74, fill: C.canard }, centre);
    etiquette(centre, cx, cy + 12, "A320", { fs: 40, c: "#fff", fw: 700 });
    var fg = [0, 1, 2, 3].map(function (k) {
      var y = top + k * (bh + gap) + bh / 2;
      return sv("path", { d: "M" + (40 + bw + 8) + " " + y + " C" + (cx - 60) + " " + y + " " + (cx - 110) + " " + cy + " " + (cx - 78) + " " + cy,
        fill: "none", stroke: C.canard, "stroke-width": 3, "stroke-linecap": "round" }, g);
    });
    var fd = [0, 1, 2, 3].map(function (k) {
      var y = top + k * (bh + gap) + bh / 2;
      return sv("path", { d: "M" + (cx + 78) + " " + cy + " C" + (cx + 110) + " " + cy + " " + (cx + 60) + " " + y + " " + (W_ - 40 - bw - 8) + " " + y,
        fill: "none", stroke: C.sa, "stroke-width": 3, "stroke-linecap": "round" }, g);
    });
    return function (t, st) {
      var tl = st.tl, k1 = et(v, "1", 1), k2 = et(v, "2", 5);
      op(centre, E(P(tl, 0, .6)));
      op(tg, E(P(t, k1, .5)));
      gauche.forEach(function (b, k) { var q = E(P(t, k1 + .2 + k * .35, .6)); op(b, q); tr(b, "translateX(" + (-24 * (1 - q)) + "px)"); });
      fg.forEach(function (f, k) { trace(f, P(t, k1 + .6 + k * .35, .9)); });
      op(td, E(P(t, k2, .5)));
      fd.forEach(function (f, k) { trace(f, P(t, k2 + .1 + k * .35, .9)); });
      droite.forEach(function (b, k) { var q = E(P(t, k2 + .6 + k * .35, .6)); op(b, q); tr(b, "translateX(" + (24 * (1 - q)) + "px)"); });
    };
  };
})();
