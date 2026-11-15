/* Illustrations propres à la vidéo S1 (« Comment est structurée la société française actuelle ? »), chargées après
   ses/serie/moteur.js. Rendu fonction pure du temps ; outils du moteur dans window.SERIE_OUTILS.
   toupie   : schéma de principe de la moyennisation (Mendras) : une pyramide (peu de monde en haut, beaucoup en bas)
              qui se transforme en toupie au repère {id.1} ; {id.2} la « constellation centrale » est nommée.
   bourdieu : l'espace social de Bourdieu, schéma de principe : {id.1} axe vertical (volume global de capital),
              {id.2} axe horizontal (structure : capital culturel / capital économique), {id.3} deux positions illustratives. */
(function () {
  var O = window.SERIE_OUTILS, sv = O.sv, et_ = O.etiquette, C = O.C, E = O.E, EIO = O.EIO, P = O.P, op = O.op, et = O.et, trace = O.trace;
  window.SERIE_ILLU = window.SERIE_ILLU || {};

  // demi-largeur (0 à 1) de la silhouette à la hauteur relative y (0 = haut, 1 = bas)
  function pyramide(y) { return 0.06 + 0.94 * y; }
  function toupie(y) {
    if (y < 0.06) return 0.05;
    if (y < 0.42) return 0.05 + 0.95 * Math.sin((y - 0.06) / 0.36 * Math.PI / 2);
    return 0.02 + 0.98 * Math.pow(Math.max(0, 1 - (y - 0.42) / 0.58), 1.15);
  }

  window.SERIE_ILLU.toupie = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), cx = W * 0.30, top = 70, bas = H - 40, L = 220;
    var forme = sv("path", { fill: C.canard, opacity: 0.88, stroke: C.iv, "stroke-width": 2.5 }, g);
    var bande = sv("rect", { x: cx - L - 20, width: 2 * L + 40, rx: 8, fill: "rgba(240,190,79,.30)" }, g);
    g.insertBefore(bande, forme);
    var haut = et_(g, W * 0.58, top + 30, "en haut : peu nombreux", { ancre: "start", fs: 26, c: C.iv2, fw: 600 });
    var basT = et_(g, W * 0.58, bas - 10, "en bas : moins nombreux", { ancre: "start", fs: 26, c: C.iv2, fw: 600 });
    var avant = et_(g, cx, 34, "Une pyramide…", { fs: 34, c: C.iv, fw: 700 });
    var apres = et_(g, cx, 34, "… devenue une toupie", { fs: 34, c: C.sa2, fw: 700 });
    var centre = et_(g, W * 0.58, top + (bas - top) * 0.42, "la constellation centrale", { ancre: "start", fs: 32, c: C.mo, fw: 700 });
    var centre2 = et_(g, W * 0.58, top + (bas - top) * 0.42 + 38, "professions intermédiaires, employés…", { ancre: "start", fs: 24, c: C.iv2, fw: 500 });
    var trait = sv("path", { d: "M" + (cx + L + 30) + " " + (top + (bas - top) * 0.40) + " H" + (W * 0.58 - 14), stroke: C.mo, "stroke-width": 3, fill: "none" }, g);
    var lg = et_(g, W - 10, H - 6, "Schéma de principe (sans données)", { ancre: "end", fs: 20, c: C.iv2, fw: 500 });
    return function (t, st) {
      var tl = st.tl, k1 = et(v, "1", 3), k2 = et(v, "2", 6), q = EIO(P(t, k1, 2.2));
      var n = 40, d = "", pts = [];
      for (var i = 0; i <= n; i++) {
        var y = i / n, w = (1 - q) * pyramide(y) + q * toupie(y);
        pts.push([y, w]);
      }
      pts.forEach(function (p, i) { d += (i ? "L" : "M") + (cx + p[1] * L).toFixed(1) + " " + (top + p[0] * (bas - top)).toFixed(1); });
      for (var j = pts.length - 1; j >= 0; j--) d += "L" + (cx - pts[j][1] * L).toFixed(1) + " " + (top + pts[j][0] * (bas - top)).toFixed(1);
      forme.setAttribute("d", d + "Z");
      op(forme, E(P(tl, 0, .8)));
      op(avant, E(P(tl, .2, .6)) * (1 - E(P(t, k1, .6))));
      op(apres, E(P(t, k1 + 1.2, .8)));
      op(haut, E(P(tl, .6, .6))); op(basT, E(P(t, k1 + 1.6, .8)));
      var qb = E(P(t, k2, .8)), yc = top + (bas - top) * 0.22;
      bande.setAttribute("y", yc.toFixed(1)); bande.setAttribute("height", ((bas - top) * 0.40).toFixed(1));
      op(bande, qb); op(centre, qb); op(centre2, E(P(t, k2 + .5, .7))); trace(trait, P(t, k2 + .2, .8));
      op(lg, E(P(tl, .4, .6)) * .9);
    };
  };

  window.SERIE_ILLU.bourdieu = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), cx = W / 2, cy = H / 2 + 10, ax = W * 0.40, ay = H * 0.40;
    var vert = sv("path", { d: "M" + cx + " " + (cy + ay) + " V" + (cy - ay), stroke: C.iv, "stroke-width": 3.4, fill: "none" }, g);
    var vertP = sv("path", { d: "M" + (cx - 12) + " " + (cy - ay + 18) + " L" + cx + " " + (cy - ay) + " L" + (cx + 12) + " " + (cy - ay + 18), stroke: C.iv, "stroke-width": 3.4, fill: "none" }, g);
    var vH = et_(g, cx + 20, cy - ay + 14, "volume global de capital +", { ancre: "start", fs: 27, c: C.iv, fw: 700 });
    var vB = et_(g, cx + 20, cy + ay - 4, "volume global de capital −", { ancre: "start", fs: 27, c: C.iv, fw: 700 });
    var hor = sv("path", { d: "M" + (cx - ax) + " " + cy + " H" + (cx + ax), stroke: C.iv, "stroke-width": 3.4, fill: "none" }, g);
    var hG = et_(g, cx - ax, cy + 40, "← plus de capital culturel", { ancre: "start", fs: 26, c: C.canard, fw: 700 });
    var hD = et_(g, cx + ax, cy + 40, "plus de capital économique →", { ancre: "end", fs: 26, c: C.sa2, fw: 700 });
    var hT = et_(g, cx - ax, cy - 18, "structure du capital", { ancre: "start", fs: 22, c: C.iv2, fw: 600 });
    var pts = [[cx - ax * 0.55, cy - ay * 0.45, "professeur", C.canard, "start"], [cx + ax * 0.55, cy - ay * 0.45, "commerçant aisé", C.sa2, "end"]].map(function (p) {
      var gg = sv("g", {}, g);
      sv("circle", { cx: p[0], cy: p[1], r: 15, fill: p[3] }, gg);
      et_(gg, p[0] + (p[4] === "start" ? -10 : 10), p[1] - 28, p[2], { ancre: p[4], fs: 28, c: p[3], fw: 700 });
      return gg;
    });
    var lg = et_(g, W - 10, H - 4, "Schéma de principe : positions illustratives", { ancre: "end", fs: 20, c: C.iv2, fw: 500 });
    return function (t, st) {
      var tl = st.tl, k1 = et(v, "1", 1), k2 = et(v, "2", 3), k3 = et(v, "3", 5);
      trace(vert, P(t, k1, .9)); op(vertP, E(P(t, k1 + .7, .4))); op(vH, E(P(t, k1 + .5, .6))); op(vB, E(P(t, k1 + .8, .6)));
      trace(hor, P(t, k2, .9)); op(hG, E(P(t, k2 + .5, .6))); op(hD, E(P(t, k2 + .8, .6))); op(hT, E(P(t, k2 + 1, .6)));
      pts.forEach(function (p, i) { var q = E(P(t, k3 + i * .8, .6)); op(p, q); });
      op(lg, E(P(tl, .4, .6)) * .9);
    };
  };
})();
