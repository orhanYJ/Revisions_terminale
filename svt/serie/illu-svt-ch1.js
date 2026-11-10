/* Vidéo SVT, chapitre 1 « L'origine du génotype des individus » : illustrations propres au chapitre.
   Chargé par svt/serie/svt-ch1.html après le moteur. Chaque illustration : SERIE_ILLU.nom = function (svg, v) {…
   return function (t, st) {…}} ; rendu fonction pure du temps, repères {id.k} lus par O.et(v, "k", repli).
   Couleurs des chromosomes comme dans les animations du site : maternel magenta, paternel cyan. */
(function () {
  "use strict";
  // la page charge ce fichier avant le moteur : les outils (window.SERIE_OUTILS) sont lus au premier dessin
  var O, sv, E, EB, EIO, P, op, et, lab, C;
  function init() {
    if (O) return;
    O = window.SERIE_OUTILS; sv = O.sv; E = O.E; EB = O.EB; EIO = O.EIO; P = O.P; op = O.op; et = O.et; lab = O.etiquette; C = O.C;
  }
  var MAG = "#f27ab8", CYA = "#6fd3e8", OR = "#ffd24a", ROUGE = "#ff6b5b", VERT = "#7ce08a", GRIS = "#8d9a86";
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var SERIE_ILLU = window.SERIE_ILLU;

  function trace(e, p) { O.trace(e, p); }
  // flèche : tracé + pointe ; renvoie {g, p, maj(p)}
  function fleche(g, d, col, ep) {
    var gg = sv("g", {}, g), p = sv("path", { d: d, fill: "none", stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round" }, gg);
    var tri = sv("path", { d: "", fill: col }, gg), L = 0;
    return { g: gg, p: p, maj: function (q) {
      trace(p, q);
      if (!L) L = p.getTotalLength ? p.getTotalLength() : 0;
      if (!L || q <= 0.02) { tri.setAttribute("d", ""); return; }
      var a = p.getPointAtLength(L * q), b = p.getPointAtLength(Math.max(0, L * q - 4)), ux = a.x - b.x, uy = a.y - b.y, n = Math.hypot(ux, uy) || 1, s = (ep || 3) * 3.6;
      ux /= n; uy /= n;
      tri.setAttribute("d", "M" + (a.x + ux * 3) + " " + (a.y + uy * 3) + " L" + (a.x - ux * s - uy * s * .55) + " " + (a.y - uy * s + ux * s * .55) +
        " L" + (a.x - ux * s + uy * s * .55) + " " + (a.y - uy * s - ux * s * .55) + " Z");
    } };
  }
  // chromosome à une chromatide (bâtonnet arrondi) ; bandes optionnelles [[y0, y1, couleur]] en fraction de la longueur
  function chromo(g, x, y, L, col, larg, bandes) {
    var gg = sv("g", {}, g), w = larg || 16;
    sv("rect", { x: x - w / 2, y: y, width: w, height: L, rx: w / 2, fill: col }, gg);
    (bandes || []).forEach(function (b) { sv("rect", { x: x - w / 2, y: y + b[0] * L, width: w, height: (b[1] - b[0]) * L, fill: b[2] }, gg); });
    return gg;
  }
  function boite(g, x, y, w, h, opt) {
    opt = opt || {};
    return sv("rect", { x: x, y: y, width: w, height: h, rx: opt.r != null ? opt.r : 14, fill: opt.f || "rgba(10,28,18,.82)",
      stroke: opt.s || "rgba(231,242,218,.35)", "stroke-width": opt.ep || 2 }, g);
  }
  function apparait(e, t, t1, d) { var p = E(P(t, t1, d || .6)); op(e, p); return p; }

  /* ------------------------------------------------------------------ cycle méiose / fécondation (★)
     {id.1} l'individu 2n ; {id.2} la méiose et les gamètes n ; {id.3} la fécondation et le zygote 2n ;
     {id.4} les mitoses qui ramènent à l'individu ; {id.5} phases haploïde / diploïde */
  SERIE_ILLU.cycle = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s), cx = W / 2 - 40, cy = H / 2 - 22, R = Math.min(W, H) * .31;
    function cellule(x, y, r, paires, titre, sous) {
      var c = sv("g", {}, g);
      sv("circle", { cx: x, cy: y, r: r, fill: "rgba(127,190,203,.10)", stroke: "rgba(231,242,218,.55)", "stroke-width": 2.5 }, c);
      paires.forEach(function (p, i) {
        var dx = (i - (paires.length - 1) / 2) * 26;
        chromo(c, x + dx, y - p[1] / 2, p[1], p[0], 11);
      });
      lab(c, x, y + r + 32, titre, { fs: 25, c: C.iv, fw: 700 });
      if (sous) lab(c, x, y + r + 60, sous, { fs: 20, c: C.iv2 });
      return c;
    }
    var P2n = [[MAG, 62], [CYA, 62], [MAG, 34], [CYA, 34]];
    var ind = cellule(cx, cy - R, 62, P2n, "Cellule de l'individu · 2n", "2n = 46 chez l'humain");
    var gam1 = cellule(cx + R * 1.05, cy + 10, 42, [[CYA, 52], [MAG, 30]], "", "");
    var gam2 = cellule(cx + R * 1.02 - 10, cy + 10, 0.1, [], "", "");
    var gamB = cellule(cx + R * 1.05 + 104, cy + 10, 42, [[MAG, 52], [CYA, 30]], "", "");
    lab(gamB, cx + R * 1.05 + 52, cy + 84, "Gamètes · n", { fs: 25, c: C.iv, fw: 700 }); lab(gamB, cx + R * 1.05 + 52, cy + 110, "n = 23", { fs: 20, c: C.iv2 });
    var zyg = cellule(cx, cy + R, 56, [[CYA, 58], [MAG, 58], [MAG, 32], [CYA, 32]], "Zygote (cellule-œuf) · 2n", "");
    gam2.setAttribute("opacity", 0);
    var f1 = fleche(g, "M" + (cx + 80) + " " + (cy - R + 30) + " Q" + (cx + R * .95) + " " + (cy - R * .9) + " " + (cx + R * 1.05) + " " + (cy - 40), C.sa, 4);
    var t1 = lab(g, cx + R * .98, cy - R * .78, "MÉIOSE", { fs: 28, c: C.sa, fw: 800, ancre: "start" });
    var t1b = lab(g, cx + R * .98, cy - R * .78 + 30, "2n → n (dans les gonades)", { fs: 21, c: C.iv2, ancre: "start" });
    var f2 = fleche(g, "M" + (cx + R * 1.05 + 40) + " " + (cy + 124) + " Q" + (cx + R * .9) + " " + (cy + R * .95) + " " + (cx + 72) + " " + (cy + R - 4), OR, 4);
    var t2 = lab(g, cx + R * 1.05 + 150, cy + R * .78, "FÉCONDATION", { fs: 28, c: OR, fw: 800 });
    var t2b = lab(g, cx + R * 1.05 + 150, cy + R * .78 + 28, "n + n → 2n", { fs: 21, c: C.iv2 });
    var f3 = fleche(g, "M" + (cx - 78) + " " + (cy + R - 10) + " Q" + (cx - R * 1.75) + " " + (cy - R) + " " + (cx - 70) + " " + (cy - R), VERT, 4);
    var t3 = lab(g, cx - R * 1.08, cy - 10, "MITOSES", { fs: 28, c: VERT, fw: 800, ancre: "end" });
    var t3b = lab(g, cx - R * 1.08, cy + 20, "2n → 2n : un clone", { fs: 21, c: C.iv2, ancre: "end" });
    var ph = sv("g", {}, g);
    sv("path", { d: "M" + (cx + R * 1.05 + 170) + " " + (cy - 30) + " v80", stroke: CYA, "stroke-width": 8, "stroke-linecap": "round" }, ph);
    lab(ph, cx + R * 1.05 + 186, cy + 16, "phase haploïde", { fs: 20, c: CYA, ancre: "start" });
    lab(ph, cx - R * 1.08, cy + 56, "phase diploïde", { fs: 20, c: MAG, ancre: "end", fw: 700 });
    var k1 = et(v, "1", .3), k2 = et(v, "2", 2.5), k3 = et(v, "3", 5), k4 = et(v, "4", 7.5), k5 = et(v, "5", 9.5);
    return function (t) {
      apparait(ind, t, k1);
      f1.maj(EIO(P(t, k2, 1.2))); op(t1, E(P(t, k2 + .4, .6))); op(t1b, E(P(t, k2 + .6, .6)));
      apparait(gam1, t, k2 + 1); apparait(gamB, t, k2 + 1.4);
      f2.maj(EIO(P(t, k3, 1.2))); op(t2, E(P(t, k3 + .4, .6))); op(t2b, E(P(t, k3 + .6, .6)));
      var z = apparait(zyg, t, k3 + 1); 
      f3.maj(EIO(P(t, k4, 1.4))); op(t3, E(P(t, k4 + .5, .6))); op(t3b, E(P(t, k4 + .7, .6)));
      op(ph, E(P(t, k5, .8)));
    };
  };

  /* ------------------------------------------------------------------ échiquier de croisement
     v.titre ; v.col = gamètes du parent 1 (en-têtes de colonnes) ; v.lig = gamètes du parent 2 ;
     v.cases = [[génotype, phénotype, couleur], …] ligne par ligne ; v.bas = conclusion ;
     {id.1} en-têtes de colonnes ; {id.2} en-têtes de lignes ; {id.3} les cases une à une ; {id.4} la conclusion */
  SERIE_ILLU.echiquier = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s), nc = v.col.length, nl = v.lig.length;
    var cw = Math.min(270, (W - 200) / nc), ch = Math.min(138, (H - 190) / nl), x0 = (W - cw * nc) / 2 + 60, y0 = Math.max(120, (H - nl * ch) / 2);
    var ti = lab(g, W / 2, 40, v.titre || "", { fs: 30, c: C.iv, fw: 700, cls: "ser" });
    var coin = sv("g", {}, g);
    boite(coin, x0 - 130, y0 - 74, 126, 70, { f: "rgba(183,217,76,.08)", s: "rgba(183,217,76,.35)", r: 10 });
    lab(coin, x0 - 67, y0 - 32, "gamètes", { fs: 20, c: C.sa });
    var cols = v.col.map(function (c, i) {
      var gg = sv("g", {}, g); boite(gg, x0 + i * cw + 6, y0 - 74, cw - 12, 70, { f: "rgba(111,211,232,.12)", s: CYA, r: 10 });
      lab(gg, x0 + i * cw + cw / 2, y0 - 30, c, { fs: 28, c: CYA, fw: 700 }); return gg;
    });
    var ligs = v.lig.map(function (c, i) {
      var gg = sv("g", {}, g); boite(gg, x0 - 130, y0 + i * ch + 6, 126, ch - 12, { f: "rgba(242,122,184,.12)", s: MAG, r: 10 });
      lab(gg, x0 - 67, y0 + i * ch + ch / 2 + 10, c, { fs: 28, c: MAG, fw: 700 }); return gg;
    });
    var cases = v.cases.map(function (c, i) {
      var r = Math.floor(i / nc), k = i % nc, gg = sv("g", {}, g), col = c[2] || C.sa;
      var bx = boite(gg, x0 + k * cw + 6, y0 + r * ch + 6, cw - 12, ch - 12, { f: "rgba(10,28,18,.9)", s: col, r: 10 });
      lab(gg, x0 + k * cw + cw / 2, y0 + r * ch + ch / 2 - 4, c[0], { fs: 26, c: C.iv, fw: 600 });
      lab(gg, x0 + k * cw + cw / 2, y0 + r * ch + ch / 2 + 28, c[1], { fs: 24, c: col, fw: 700 });
      return { g: gg, b: bx };
    });
    var bas = v.bas ? lab(g, W / 2, y0 + nl * ch + 52, v.bas, { fs: 26, c: C.sa, fw: 700 }) : null;
    var k1 = et(v, "1", .5), k2 = et(v, "2", 1.4), k3 = et(v, "3", 2.4), k4 = et(v, "4", 2.4 + v.cases.length * .7 + 1);
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6))); op(coin, E(P(st.tl, .2, .6)));
      cols.forEach(function (c, i) { apparait(c, t, k1 + i * .25); });
      ligs.forEach(function (c, i) { apparait(c, t, k2 + i * .25); });
      cases.forEach(function (c, i) {
        var p = apparait(c.g, t, k3 + i * .6, .5);
        var hl = (v.hl || []).indexOf(i) >= 0 && t >= k4;
        c.b.setAttribute("stroke-width", hl ? 5 : 2);
        c.g.setAttribute("transform", "translate(0 " + (10 * (1 - p)).toFixed(1) + ")");
      });
      if (bas) op(bas, E(P(t, k4, .7)));
    };
  };

  /* ------------------------------------------------------------------ résultats d'un test-cross (histogramme)
     v.classes = [[phénotype, effectif, "p" | "r" | ""], …] ; v.total ; v.titre ;
     {id.1} les barres montent ; {id.2} la ligne des 25 % attendus ; {id.3} parentaux / recombinés colorés et sommés */
  SERIE_ILLU.barres = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s), n = v.classes.length, x0 = 90, y0 = H - 120, hmax = H - 230, bw = (W - 140) / n;
    var max = v.max || 50, Y = function (pc) { return y0 - pc / max * hmax; };
    var ti = lab(g, W / 2, 36, v.titre || "", { fs: 28, c: C.iv, fw: 700, cls: "ser" });
    var axe = sv("g", {}, g);
    sv("line", { x1: x0 - 10, x2: W - 30, y1: y0, y2: y0, stroke: C.iv, "stroke-width": 2 }, axe);
    sv("line", { x1: x0 - 10, x2: x0 - 10, y1: y0, y2: Y(max) - 10, stroke: C.iv, "stroke-width": 2 }, axe);
    [10, 20, 30, 40, 50].filter(function (x) { return x <= max; }).forEach(function (x) {
      lab(axe, x0 - 22, Y(x) + 7, x + " %", { fs: 18, c: C.iv2, ancre: "end" });
      sv("line", { x1: x0 - 10, x2: W - 30, y1: Y(x), y2: Y(x), stroke: "rgba(231,242,218,.08)" }, axe);
    });
    var bars = v.classes.map(function (c, i) {
      var pc = 100 * c[1] / v.total, x = x0 + i * bw + bw * .14, w = bw * .72, gg = sv("g", {}, g);
      var r = sv("rect", { x: x, y: y0, width: w, height: 0, rx: 6, fill: "rgba(183,217,76,.55)" }, gg);
      var val = lab(gg, x + w / 2, y0 - 12, "", { fs: 22, c: C.iv, fw: 700 });
      var nom = c[0].split(" ; "), l1 = lab(gg, x + w / 2, y0 + 32, nom[0], { fs: 19, c: C.iv2 }), l2 = lab(gg, x + w / 2, y0 + 56, nom[1] || "", { fs: 19, c: C.iv2 });
      var ty = lab(gg, x + w / 2, y0 + 86, c[2] === "p" ? "parental" : c[2] === "r" ? "recombiné" : "", { fs: 20, c: c[2] === "p" ? CYA : OR, fw: 800 });
      return { r: r, val: val, pc: pc, x: x, w: w, ty: ty, c: c, eff: c[1] };
    });
    var att = sv("g", {}, g);
    sv("line", { x1: x0 - 10, x2: W - 30, y1: Y(25), y2: Y(25), stroke: ROUGE, "stroke-width": 2.5, "stroke-dasharray": "10 8" }, att);
    lab(att, W - 34, Y(25) - 10, "attendu si indépendants : 25 %", { fs: 19, c: ROUGE, ancre: "end", fw: 700 });
    var som = v.somme ? lab(g, W / 2, H - 6, v.somme, { fs: 23, c: C.sa, fw: 700 }) : null;
    var k1 = et(v, "1", .6), k2 = et(v, "2", 3), k3 = et(v, "3", 5);
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6))); op(axe, E(P(st.tl, .2, .6)));
      bars.forEach(function (b, i) {
        var p = EIO(P(t, k1 + i * .35, 1.1)), hh = (y0 - Y(b.pc)) * p;
        b.r.setAttribute("y", (y0 - hh).toFixed(1)); b.r.setAttribute("height", hh.toFixed(1));
        var dedans = t >= k2 && Math.abs(y0 - hh - 18 - Y(25)) < 18 && hh > 60, vy = dedans ? y0 - hh + 30 : y0 - hh - 12; b.val.setAttribute("y", vy.toFixed(1));
        b.val.textContent = p > .05 ? b.eff + " · " + b.pc.toFixed(v.dec != null ? v.dec : (b.pc % 1 ? 1 : 0)).replace(".", ",") + " %" : "";
        var col = t >= k3 ? (b.c[2] === "p" ? CYA : b.c[2] === "r" ? OR : "rgba(183,217,76,.55)") : "rgba(183,217,76,.55)";
        b.r.setAttribute("fill", col); b.r.setAttribute("fill-opacity", t >= k3 ? .8 : 1);
        op(b.ty, E(P(t, k3 + .3, .6)));
      });
      op(att, E(P(t, k2, .7)));
      if (som) op(som, E(P(t, k3 + .8, .7)));
    };
  };

  /* ------------------------------------------------------------------ translocation robertsonienne 14-21 et descendance
     {id.1} le 21 se fixe sur le 14 (porteur sain, 45 chromosomes) ; {id.2} gamètes normal et porteur ;
     {id.3} gamète 14-21 + 21 → trisomie 21 ; {id.4} les trois gamètes non viables */
  SERIE_ILLU.transloc = function (s, v) {
    init();
    var W = v.w, g = sv("g", {}, s), L14 = 150, L21 = 70;
    var ti = lab(g, W / 2, 36, "Un parent porteur d'une translocation 14-21", { fs: 28, c: C.iv, fw: 700, cls: "ser" });
    var par = sv("g", {}, g), px = W / 2 - 170, py = 70;
    boite(par, px - 60, py, 460, 250, { r: 18 });
    var c14 = chromo(par, px + 20, py + 40, L14, MAG, 22); lab(par, px + 20, py + 222, "14", { fs: 22, c: C.iv });
    var c21 = chromo(par, px + 90, py + 120, L21, CYA, 22); lab(par, px + 90, py + 222, "21", { fs: 22, c: C.iv });
    var f14 = chromo(par, px + 230, py + 20, L14, MAG, 22);
    var mob = chromo(par, 0, 0, L21, CYA, 22);
    var tf = lab(par, px + 262, py + 120, "« 14-21 »", { fs: 22, c: OR, fw: 700, ancre: "start" });
    var bilan = lab(par, px + 170, py + 270, "45 chromosomes, tous les gènes en double : porteur sain", { fs: 21, c: C.iv2 });
    var GAM = [
      { a: [[MAG, L14], [CYA, L21]], t: "14 + 21", r: "caryotype normal", c: VERT, k: "2" },
      { a: [["F", 0]], t: "14-21 seul", r: "porteur sain", c: CYA, k: "2" },
      { a: [["F", 0], [CYA, L21]], t: "14-21 + 21", r: "TRISOMIE 21", c: ROUGE, k: "3" },
      { a: [[MAG, L14]], t: "14 seul", r: "monosomie 21 : non viable", c: GRIS, k: "4" },
      { a: [["F", 0], [MAG, L14]], t: "14-21 + 14", r: "trisomie 14 : non viable", c: GRIS, k: "4" },
      { a: [[CYA, L21]], t: "21 seul", r: "monosomie 14 : non viable", c: GRIS, k: "4" }
    ];
    var gw = (W - 60) / 6, gy = 376;
    var gams = GAM.map(function (G, i) {
      var gg = sv("g", {}, g), x = 30 + i * gw + gw / 2;
      var bx = boite(gg, x - gw / 2 + 4, gy, gw - 8, 222, { r: 16, s: G.c });
      var n = G.a.length;
      G.a.forEach(function (c, j) {
        var xx = x + (j - (n - 1) / 2) * 34, s_ = .62;
        if (c[0] === "F") { chromo(gg, xx, gy + 20, L14 * s_, MAG, 15); chromo(gg, xx, gy + 20 + L14 * s_ - 4, L21 * s_, CYA, 15); }
        else chromo(gg, xx, gy + 20, c[1] * s_, c[0], 15);
      });
      lab(gg, x, gy + 168, G.t, { fs: 18, c: C.iv });
      var rr = G.r.split(" : ");
      lab(gg, x, gy + 192, rr[0], { fs: rr[0].length > 14 ? 15 : 17, c: G.c, fw: 800 });
      if (rr[1]) lab(gg, x, gy + 212, rr[1], { fs: 16, c: G.c, fw: 700 });
      return { g: gg, k: G.k, b: bx };
    });
    var gti = lab(g, W / 2, gy - 12, "Ses gamètes possibles, fécondés par un gamète normal", { fs: 22, c: C.sa, fw: 700 });
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6))); op(par, E(P(st.tl, .2, .6)));
      var k1 = et(v, "1", 1), u = EIO(P(t, k1, 1.6));
      var x = (px + 90) + (px + 230 - px - 90) * u, y = (py + 120) + (py + 20 + L14 - 4 - py - 120) * u;
      mob.setAttribute("transform", "translate(" + x.toFixed(1) + " " + y.toFixed(1) + ")");
      op(mob, E(P(t, k1, .4))); op(tf, E(P(t, k1 + 1.4, .6))); op(bilan, E(P(t, k1 + 1.8, .6)));
      op(f14, E(P(t, k1, .4)));
      op(gti, E(P(t, et(v, "2", 4), .6)));
      gams.forEach(function (G, i) { apparait(G.g, t, et(v, G.k, 4 + i) + (i % 3) * .3); });
      var k3 = et(v, "3", 8); gams[2].b.setAttribute("stroke-width", t >= k3 ? 2 + 2 * (1 + Math.sin((t - k3) * 4)) : 2);
    };
  };

  /* ------------------------------------------------------------------ les opsines, une famille multigénique
     {id.1} gène ancestral dupliqué ; {id.2} une copie transposée sur le chromosome 7 (S) ; {id.3} mutations, divergence ;
     {id.4} nouvelle duplication sur le X : M et L côte à côte ; {id.5} trois pigments, trois couleurs absorbées */
  SERIE_ILLU.opsines = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s), yA = 110, yB = 260;
    var ti = lab(g, W / 2, 36, "Histoire de la famille des opsines (schéma)", { fs: 28, c: C.iv, fw: 700, cls: "ser" });
    function chr(y, nom, col) {
      var gg = sv("g", {}, g);
      sv("rect", { x: 140, y: y, width: 560, height: 46, rx: 23, fill: "rgba(231,242,218,.10)", stroke: "rgba(231,242,218,.5)", "stroke-width": 2 }, gg);
      lab(gg, 120, y + 32, nom, { fs: 24, c: col || C.iv, fw: 700, ancre: "end" });
      return gg;
    }
    var cX = chr(yA, "X"), c7 = chr(yB, "7");
    function gene(x, y, t, col) {
      var gg = sv("g", {}, g); sv("rect", { x: x - 36, y: y + 4, width: 72, height: 38, rx: 6, fill: col, stroke: "#040c08", "stroke-width": 1.5 }, gg);
      var tt = lab(gg, x, y + 31, t, { fs: 22, c: "#081109", fw: 800 }); gg._t = tt; return gg;
    }
    var gA = gene(330, yA, "anc.", "#c9c3a8"), gD = gene(410, yA, "anc.", "#c9c3a8");
    var gS = gene(410, yB, "S", "#6c8dff"), gM = gene(330, yA, "M", "#7ce08a"), gL = gene(410, yA, "L", "#ff6b5b");
    var mut = sv("g", {}, g);
    [[300, yA], [345, yA], [380, yB], [430, yB]].forEach(function (p) { lab(mut, p[0], p[1] - 6, "★", { fs: 20, c: OR }); });
    var l1 = lab(g, 420, yA + 82, "", { fs: 21, c: C.iv2 }), l2 = lab(g, 420, yB + 82, "", { fs: 21, c: C.iv2 });
    // trois courbes d'absorption schématiques
    var sp = sv("g", {}, g), xs = 160, xw = 620, ys = H - 40, hs = 150;
    sv("line", { x1: xs, x2: xs + xw, y1: ys, y2: ys, stroke: C.iv, "stroke-width": 2 }, sp);
    lab(sp, xs + xw + 10, ys + 6, "longueur d'onde", { fs: 19, c: C.iv2, ancre: "start" });
    var cour = [[.18, "#6c8dff", "S : bleu"], [.5, "#7ce08a", "M : vert"], [.74, "#ff6b5b", "L : rouge"]].map(function (c) {
      var d = "", i; for (i = 0; i <= 60; i++) { var x = i / 60, y = Math.exp(-Math.pow((x - c[0]) / .11, 2)); d += (i ? " L" : "M") + (xs + x * xw).toFixed(1) + " " + (ys - y * hs).toFixed(1); }
      var p = sv("path", { d: d, fill: "none", stroke: c[1], "stroke-width": 4 }, sp);
      var tl = lab(sp, xs + c[0] * xw, ys - hs - 12, c[2], { fs: 20, c: c[1], fw: 800 });
      return { p: p, l: tl };
    });
    var k1 = et(v, "1", 1), k2 = et(v, "2", 3), k3 = et(v, "3", 5), k4 = et(v, "4", 7), k5 = et(v, "5", 9);
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6))); op(cX, E(P(st.tl, .2, .6))); op(c7, E(P(t, k2 - .3, .6)));
      // ancêtre : un gène, puis duplication (la copie glisse à côté), puis transposition vers le 7
      op(gA, t < k4 ? E(P(st.tl, .4, .6)) : 1 - E(P(t, k4, .5)));
      var d1 = EIO(P(t, k1, 1)), d2 = EIO(P(t, k2, 1.4));
      gD.setAttribute("transform", "translate(" + (-80 * (1 - d1)) + " " + ((yB - yA) * d2) + ")");
      op(gD, t < k1 ? 0 : (t < k3 ? 1 : 1 - E(P(t, k3, .5))));
      op(gS, E(P(t, k3, .6)));
      op(mut, E(P(t, k3, .6)) * (t < k4 + 1 ? 1 : 1));
      op(gM, E(P(t, k4, .6))); op(gL, E(P(t, k4 + .5, .6)));
      l1.textContent = t >= k4 ? "X : M et L côte à côte (nouveau crossing-over inégal)" : t >= k1 ? "duplication par crossing-over inégal" : "un seul gène ancestral";
      l2.textContent = t >= k3 ? "7 : gène S (copie transposée, puis mutée)" : t >= k2 ? "transposition d'une copie" : "";
      op(l1, E(P(st.tl, .6, .6))); op(l2, E(P(t, k2, .6)));
      op(sp, E(P(t, k5, .6)));
      cour.forEach(function (c, i) { trace(c.p, EIO(P(t, k5 + .3 + i * .5, 1))); op(c.l, E(P(t, k5 + .8 + i * .5, .5))); });
    };
  };

  /* ------------------------------------------------------------------ chimpanzé / humain : fusion du chromosome 2, inversion
     {id.1} deux chromosomes du chimpanzé ; {id.2} ils se soudent bout à bout : le chromosome 2 humain ; {id.3} 48 → 46 ;
     {id.4} une inversion : un segment retourné */
  SERIE_ILLU.fusion = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s), L1 = 150, L2 = 170, cx = 330, y = 90;
    var ti = lab(g, W / 2, 36, "Comparer les caryotypes, bande par bande", { fs: 28, c: C.iv, fw: 700, cls: "ser" });
    var B1 = [[.1, .18, "#2c3a30"], [.4, .5, "#2c3a30"], [.7, .78, "#2c3a30"]], B2 = [[.15, .24, "#2c3a30"], [.5, .58, "#2c3a30"], [.8, .9, "#2c3a30"]];
    var a = chromo(g, 0, 0, L1, "#c9c3a8", 28, B1), b = chromo(g, 0, 0, L2, "#c9c3a8", 28, B2);
    var la = lab(g, 0, 0, "2A", { fs: 22, c: C.iv }), lb = lab(g, 0, 0, "2B", { fs: 22, c: C.iv });
    var chi = lab(g, cx, y + L2 + 70, "chimpanzé : 2n = 48", { fs: 24, c: C.iv2 });
    var hum = lab(g, cx, y + L1 + L2 + 60, "humain : chromosome 2 · 2n = 46", { fs: 24, c: C.sa, fw: 700 });
    var fl = lab(g, cx + 70, y + L1 + 6, "← soudure", { fs: 21, c: OR, fw: 700, ancre: "start" });
    // inversion
    var inv = sv("g", {}, g), ix = 600, iy = 120, seg = ["A", "B", "C", "D", "E"], cols = ["#6c8dff", "#7ce08a", "#ffd24a", "#ff6b5b", "#b48cff"];
    lab(inv, ix + 150, iy - 20, "Une inversion", { fs: 26, c: C.iv, fw: 700 });
    var blocs = seg.map(function (n, i) {
      var gg = sv("g", {}, inv); sv("rect", { x: -28, y: -24, width: 56, height: 48, rx: 6, fill: cols[i] }, gg);
      lab(gg, 0, 9, n, { fs: 24, c: "#081109", fw: 800 }); return gg;
    });
    var tinv = lab(inv, ix + 150, iy + 200, "B, C, D retournés : l'ordre des gènes est inversé", { fs: 20, c: C.iv2 });
    var k1 = et(v, "1", .5), k2 = et(v, "2", 3), k3 = et(v, "3", 5), k4 = et(v, "4", 7);
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6)));
      var u = EIO(P(t, k2, 1.6)), pa = E(P(t, k1, .6));
      var ax = (cx - 50) + 50 * u, bx = (cx + 50) - 50 * u, ay = y, by = y + (L1 - 4) * u;
      a.setAttribute("transform", "translate(" + ax + " " + ay + ")"); b.setAttribute("transform", "translate(" + bx + " " + by + ")");
      op(a, pa); op(b, pa);
      la.setAttribute("x", ax - 34); la.setAttribute("y", ay + L1 / 2); lb.setAttribute("x", bx + 34 + (u > .5 ? -68 : 0)); lb.setAttribute("y", by + L2 / 2);
      op(la, pa * (1 - u)); op(lb, pa * (1 - u));
      op(chi, pa * (1 - E(P(t, k2, .5)))); op(fl, E(P(t, k2 + 1.4, .5))); op(hum, E(P(t, k3, .7)));
      op(inv, E(P(t, k4, .6)));
      var w = EIO(P(t, k4 + 1, 1.4));
      blocs.forEach(function (bl, i) {
        var pos = i >= 1 && i <= 3 ? i + (4 - 2 * i) * w : i, rot = i >= 1 && i <= 3 ? 180 * w : 0;
        bl.setAttribute("transform", "translate(" + (ix + 10 + pos * 70) + " " + (iy + 60 + Math.sin(w * Math.PI) * (i >= 1 && i <= 3 ? -40 : 0)) + ") rotate(" + rot + ")");
      });
      op(tinv, E(P(t, k4 + 2.4, .6)));
    };
  };

  /* ------------------------------------------------------------------ amylase salivaire : plus de copies d'AMY1, plus d'amylase (schéma)
     {id.1} {id.2} {id.3} trois individus ; {id.4} la conclusion */
  SERIE_ILLU.amylase = function (s, v) {
    init();
    var W = v.w, g = sv("g", {}, s);
    var ti = lab(g, W / 2, 36, "Nombre de copies du gène AMY1 et quantité d'amylase (schéma)", { fs: 26, c: C.iv, fw: 700, cls: "ser" });
    var IND = [2, 5, 9].map(function (n, i) {
      var gg = sv("g", {}, g), y = 100 + i * 130;
      lab(gg, 60, y + 34, "Individu " + (i + 1), { fs: 22, c: C.iv, ancre: "start" });
      sv("rect", { x: 220, y: y + 8, width: 420, height: 40, rx: 20, fill: "rgba(231,242,218,.10)", stroke: "rgba(231,242,218,.45)", "stroke-width": 2 }, gg);
      for (var j = 0; j < n; j++) sv("rect", { x: 240 + j * 42, y: y + 14, width: 34, height: 28, rx: 4, fill: OR }, gg);
      lab(gg, 430, y + 76, n + " copies (illustratif)", { fs: 18, c: C.iv2 });
      var bar = sv("rect", { x: 700, y: y + 10, width: 0, height: 36, rx: 8, fill: VERT }, gg);
      return { g: gg, b: bar, n: n };
    });
    var leg = lab(g, 840, 84, "amylase dans la salive", { fs: 20, c: VERT, fw: 700 });
    var co = lab(g, W / 2, 520, "Plus un individu possède de copies, plus il produit d'amylase.", { fs: 25, c: C.sa, fw: 700 });
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6))); op(leg, E(P(st.tl, .4, .6)));
      IND.forEach(function (I_, i) {
        var k = et(v, String(i + 1), .6 + i * 1.2); op(I_.g, E(P(t, k, .6)));
        I_.b.setAttribute("width", (I_.n * 30 * EIO(P(t, k + .4, 1))).toFixed(1));
      });
      op(co, E(P(t, et(v, "4", 5), .7)));
    };
  };

  /* ------------------------------------------------------------------ p53, le gardien du génome
     {id.1} lésion de l'ADN ; {id.2} p53 échappe à mdm2 et s'accumule ; {id.3} arrêt de la division → réparation ;
     {id.4} apoptose si irréparable ; {id.5} sans p53 : la cellule se divise et accumule les mutations */
  SERIE_ILLU.p53 = function (s, v) {
    init();
    var W = v.w, g = sv("g", {}, s);
    function noeud(x, y, w, t1, t2, col) {
      var gg = sv("g", {}, g); boite(gg, x - w / 2, y, w, t2 ? 82 : 58, { s: col || "rgba(231,242,218,.45)" });
      lab(gg, x, y + 36, t1, { fs: 24, c: col || C.iv, fw: 700 }); if (t2) lab(gg, x, y + 66, t2, { fs: 19, c: C.iv2 }); return gg;
    }
    var n1 = noeud(W / 2, 20, 360, "Lésion de l'ADN", "", OR);
    var n2 = noeud(W / 2, 140, 520, "p53 échappe à mdm2 et s'accumule", "facteur de transcription : commande d'autres gènes", CYA);
    var n3 = noeud(W * .26, 300, 420, "Arrêt de la division", "le temps de réparer l'ADN", VERT);
    var n4 = noeud(W * .74, 300, 420, "Apoptose", "mort programmée si irréparable", ROUGE);
    var f1 = fleche(g, "M" + W / 2 + " 82 V136", C.iv, 3), f2 = fleche(g, "M" + (W / 2 - 80) + " 226 L" + (W * .3) + " 296", VERT, 3),
      f3 = fleche(g, "M" + (W / 2 + 80) + " 226 L" + (W * .7) + " 296", ROUGE, 3);
    var sans = sv("g", {}, g);
    boite(sans, 60, 430, W - 120, 120, { f: "rgba(60,14,10,.85)", s: ROUGE });
    lab(sans, W / 2, 476, "Sans p53 fonctionnelle : ni arrêt, ni apoptose", { fs: 26, c: ROUGE, fw: 800 });
    lab(sans, W / 2, 516, "la cellule endommagée se divise et accumule les mutations suivantes", { fs: 22, c: C.iv });
    var barre = sv("path", { d: "M" + (W * .1) + " 290 L" + (W * .9) + " 400", stroke: ROUGE, "stroke-width": 7, "stroke-linecap": "round" }, g);
    var norm = sv("g", {}, g);
    boite(norm, W / 2 - 330, 170, 660, 150, { s: CYA });
    lab(norm, W / 2, 222, "En temps normal", { fs: 22, c: C.iv2 });
    lab(norm, W / 2, 262, "p53 maintenue très basse :", { fs: 27, c: CYA, fw: 700 });
    lab(norm, W / 2, 298, "mdm2 l'envoie en permanence à la destruction", { fs: 23, c: C.iv });
    var k = [1, 2, 3, 4, 5].map(function (i) { return et(v, String(i), .4 + (i - 1) * 1.6); });
    return function (t, st) {
      op(norm, E(P(st.tl, .2, .7)) * (1 - E(P(t, k[0] - .2, .5))));
      op(n1, E(P(t, k[0], .6))); f1.maj(EIO(P(t, k[1], .6))); op(n2, E(P(t, k[1] + .3, .6)));
      f2.maj(EIO(P(t, k[2], .7))); op(n3, E(P(t, k[2] + .3, .6)));
      f3.maj(EIO(P(t, k[3], .7))); op(n4, E(P(t, k[3] + .3, .6)));
      trace(barre, EIO(P(t, k[4], .6))); op(sans, E(P(t, k[4] + .4, .6)));
      [n3, n4].forEach(function (n) { if (t >= k[4]) op(n, .35); });
    };
  };

  /* ------------------------------------------------------------------ caryotype schématique 47, XY, +21
     les 23 paires rangées par taille décroissante ; {id.1} la paire 21 s'allume (trois chromosomes) */
  SERIE_ILLU.caryo21 = function (s, v) {
    init();
    var W = v.w, H = v.h, g = sv("g", {}, s);
    var ti = lab(g, W / 2, 34, "Caryotype schématique : 47, XY, +21", { fs: 28, c: C.iv, fw: 700, cls: "ser" });
    var LONG = [248, 242, 198, 190, 181, 171, 159, 145, 138, 134, 135, 133, 114, 107, 102, 90, 83, 80, 59, 64, 47, 51];
    var RANGS = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, "XY"]];
    var k = 0.42, hl = null, items = [];
    RANGS.forEach(function (r, ri) {
      var yb = 60 + (ri + 1) * 118, pas = (W - 80) / r.length;
      r.forEach(function (n, i) {
        var x = 40 + pas * (i + .5), gg = sv("g", {}, g), nb = n === 21 ? 3 : 2;
        var Ls = n === "XY" ? [LONG[6] * k, 58 * k] : [LONG[n - 1] * k, LONG[n - 1] * k];
        if (nb === 3) Ls.push(Ls[0]);
        Ls.forEach(function (L, j) {
          var xx = x + (j - (nb - 1) / 2) * 16;
          sv("rect", { x: xx - 6, y: yb - L, width: 12, height: L, rx: 6, fill: n === 21 ? "#ffd24a" : "#c9c3a8" }, gg);
          sv("rect", { x: xx - 6, y: yb - L * .62, width: 12, height: 3, fill: "rgba(8,17,9,.6)" }, gg);
        });
        lab(gg, x, yb + 24, String(n), { fs: 17, c: n === 21 ? "#ffd24a" : C.iv2, fw: n === 21 ? 800 : 500 });
        if (n === 21) { hl = sv("rect", { x: x - 36, y: yb - 50, width: 72, height: 84, rx: 10, fill: "none", stroke: "#ffd24a", "stroke-width": 3 }, g); }
        items.push({ g: gg, i: items.length });
      });
    });
    var bas = lab(g, W / 2, H - 6, "trois chromosomes 21 : 47 chromosomes", { fs: 24, c: "#ffd24a", fw: 700 });
    var k1 = et(v, "1", 3);
    return function (t, st) {
      op(ti, E(P(st.tl, 0, .6)));
      items.forEach(function (it) { op(it.g, E(P(st.tl, .3 + it.i * .06, .4))); });
      op(hl, E(P(t, k1, .5)) * (0.7 + 0.3 * Math.sin((t - k1) * 4)));
      op(bas, E(P(t, k1 + .3, .6)));
    };
  };
})();
