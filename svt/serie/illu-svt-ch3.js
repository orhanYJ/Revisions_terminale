/* Vidéo du chapitre 3 de SVT (« L'évolution du génome au sein des populations ») : illustrations propres au chapitre.
   Chargé par svt/serie/svt-ch3.html avant le moteur ; chaque illustration est une fonction pure du temps :
   SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; }  (repères {id.k} dans v.et, temps local st.tl).
   Données des simulations (dérive, Buri) calculées par outils/serie-svt/svt_ch3.py et passées dans v. */
(function () {
  "use strict";
  var SERIE_ILLU = window.SERIE_ILLU = window.SERIE_ILLU || {};
  function O() { return window.SERIE_OUTILS; }
  var COUL = { A: "#b7d94c", m: "#ff8a5c", B: "#5cc8d6", O: "#e7f2da", X: "#b48cff" };

  // générique : le moteur SVT, copié du moteur PC, écrit « Physique-chimie · Terminale » ; on corrige le libellé ici
  document.addEventListener("DOMContentLoaded", function () {
    var n = document.querySelectorAll(".g-haut");
    for (var i = 0; i < n.length; i++) n[i].textContent = "SVT · Terminale";
  });

  function apparait(o, el, t, t0, d) { var p = o.E(o.P(t, t0, d || .5)); el.setAttribute("opacity", p.toFixed(3)); return p; }
  function bille(o, g, x, y, r, c, trait) {
    return o.sv("circle", { cx: x, cy: y, r: r, fill: c, stroke: trait || "#06120b", "stroke-width": 1.6 }, g);
  }
  // individu diploïde : un disque coupé en deux, une moitié par allèle
  function individu(o, g, x, y, r, a1, a2) {
    var gg = o.sv("g", { transform: "translate(" + x + "," + y + ")" }, g);
    o.sv("path", { d: "M0 " + (-r) + " A" + r + " " + r + " 0 0 0 0 " + r + " Z", fill: COUL[a1] }, gg);
    o.sv("path", { d: "M0 " + (-r) + " A" + r + " " + r + " 0 0 1 0 " + r + " Z", fill: COUL[a2] }, gg);
    o.sv("circle", { cx: 0, cy: 0, r: r, fill: "none", stroke: "#06120b", "stroke-width": 2 }, gg);
    return gg;
  }

  // l'hérédité par mélange : {id.1} la souris grise attendue, {id.2} les générations suivantes toutes grises,
  // {id.3} la réalité : deux allèles intacts chez l'hybride, {id.4} ils se séparent dans les gamètes
  SERIE_ILLU.melange = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s);
    function souris(x, y, c, k) {
      var gg = o.sv("g", { transform: "translate(" + x + "," + y + ") scale(" + (k || 1) + ")" }, g);
      o.sv("ellipse", { cx: 0, cy: 0, rx: 46, ry: 30, fill: c, stroke: "#06120b", "stroke-width": 2 }, gg);
      o.sv("circle", { cx: 38, cy: -24, r: 13, fill: c, stroke: "#06120b", "stroke-width": 2 }, gg);
      o.sv("circle", { cx: 50, cy: -6, r: 4, fill: "#06120b" }, gg);
      o.sv("path", { d: "M-46 6 C-80 10 -86 -20 -110 -8", fill: "none", stroke: c === "#16181a" ? "#5a5f63" : c, "stroke-width": 4, "stroke-linecap": "round" }, gg);
      return gg;
    }
    var noire = souris(W * .2, 120, "#16181a"), blanche = souris(W * .8, 120, "#f4f1ea");
    var x1 = o.etiquette(g, W * .5, 132, "×", { fs: 54, c: o.C.iv });
    var l1 = o.sv("path", { d: "M" + W * .5 + " 160 V215", stroke: o.C.iv2, "stroke-width": 3, fill: "none" }, g);
    var grise = souris(W * .5, 270, "#8b8f8c"), q = o.etiquette(g, W * .5 + 110, 280, "?", { fs: 46, c: o.C.or });
    var lab1 = o.etiquette(g, W * .5, 340, "Hérédité par mélange : une souris grise", { fs: 26, c: o.C.iv2 });
    var gens = o.sv("g", {}, g);
    for (var i = 0; i < 5; i++) souris(W * .22 + i * W * .14, 430, "#8b8f8c", .7);
    var lab2 = o.etiquette(g, W * .5, 495, "… puis toutes grises : la diversité disparaîtrait", { fs: 24, c: o.C.ca });
    var vrai = o.sv("g", {}, g);
    o.sv("rect", { x: 30, y: 380, width: W - 60, height: 150, rx: 18, fill: "#0a1a11", stroke: o.C.sa, "stroke-width": 2 }, vrai);
    o.etiquette(vrai, W * .5, 416, "En réalité : les allèles se transmettent intacts", { fs: 26, c: o.C.sa });
    individu(o, vrai, W * .3, 475, 30, "X", "O");
    o.etiquette(vrai, W * .3, 528, "hybride : deux allèles distincts", { fs: 18, c: o.C.iv2 });
    var gam = o.sv("g", {}, vrai);
    o.sv("path", { d: "M" + (W * .3 + 44) + " 475 H" + (W * .52), stroke: o.C.iv2, "stroke-width": 2.5, fill: "none" }, gam);
    o.sv("circle", { cx: W * .6, cy: 460, r: 18, fill: COUL.X, stroke: "#06120b", "stroke-width": 2 }, gam);
    o.sv("circle", { cx: W * .7, cy: 490, r: 18, fill: COUL.O, stroke: "#06120b", "stroke-width": 2 }, gam);
    o.etiquette(gam, W * .78, 470, "gamètes", { fs: 20, c: o.C.iv2, ancre: "start" });
    o.etiquette(gam, W * .78, 498, "les deux variants restent", { fs: 20, c: o.C.iv2, ancre: "start" });
    return function (t, st) {
      var tl = st.tl;
      apparait(o, noire, t, v.t0, .6); apparait(o, blanche, t, v.t0 + .3, .6); apparait(o, x1, t, v.t0 + .6, .4);
      var t1 = o.et(v, "1", 2), t2 = o.et(v, "2", 4), t3 = o.et(v, "3", 6), t4 = o.et(v, "4", 8);
      apparait(o, l1, t, t1, .4); apparait(o, grise, t, t1 + .2, .6); apparait(o, lab1, t, t1 + .5, .5);
      q.setAttribute("opacity", (o.E(o.P(t, t1 + .6, .4)) * (1 - o.E(o.P(t, t3, .4)))).toFixed(3));
      var g2 = o.E(o.P(t, t2, .8)) * (1 - o.E(o.P(t, t3, .5)));
      gens.setAttribute("opacity", g2.toFixed(3)); lab2.setAttribute("opacity", g2.toFixed(3));
      apparait(o, vrai, t, t3, .7); apparait(o, gam, t, t4, .6);
    };
  };

  // une population de 25 individus (9 A//A, 12 A//m, 4 m//m) : {id.1} les individus, {id.2} les A//A (deux A chacun),
  // {id.3} les A//m (un A chacun), {id.4} le compte : 30 allèles A sur 50
  SERIE_ILLU.population = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s);
    var gen = [], i;
    for (i = 0; i < 9; i++) gen.push(["A", "A"]);
    for (i = 0; i < 12; i++) gen.push(["A", "m"]);
    for (i = 0; i < 4; i++) gen.push(["m", "m"]);
    var ordre = [3, 17, 8, 22, 0, 12, 5, 19, 10, 24, 2, 14, 7, 20, 1, 16, 9, 23, 4, 13, 18, 6, 21, 11, 15];
    var col = 5, dx = 92, dy = 90, x0 = 70, y0 = 70;
    var inds = ordre.map(function (k, j) {
      var a = gen[k], x = x0 + (j % col) * dx, y = y0 + Math.floor(j / col) * dy;
      var gg = individu(o, g, x, y, 30, a[0], a[1]); gg.setAttribute("opacity", 0);
      var halo = o.sv("circle", { cx: x, cy: y, r: 38, fill: "none", stroke: o.C.or, "stroke-width": 3.5, opacity: 0 }, g);
      return { g: gg, h: halo, a: a, x: x, y: y };
    });
    var lx = x0 + col * dx + 30;
    var leg = o.sv("g", {}, g);
    individu(o, leg, lx + 20, 70, 20, "A", "A"); o.etiquette(leg, lx + 52, 78, "A//A", { fs: 24, ancre: "start" });
    individu(o, leg, lx + 20, 120, 20, "A", "m"); o.etiquette(leg, lx + 52, 128, "A//m", { fs: 24, ancre: "start" });
    individu(o, leg, lx + 20, 170, 20, "m", "m"); o.etiquette(leg, lx + 52, 178, "m//m", { fs: 24, ancre: "start" });
    var c1 = o.etiquette(g, lx, 260, "9 A//A → 9 × 2 = 18 allèles A", { fs: 25, c: o.C.sa, ancre: "start" });
    var c2 = o.etiquette(g, lx, 305, "12 A//m → 12 allèles A", { fs: 25, c: o.C.sa, ancre: "start" });
    var c3 = o.etiquette(g, lx, 350, "25 individus → 50 allèles", { fs: 25, c: o.C.iv, ancre: "start" });
    var c4 = o.etiquette(g, lx, 410, "f(A) = 30 / 50 = 0,6", { fs: 34, c: o.C.or, ancre: "start", cls: "ser" });
    var c5 = o.etiquette(g, lx, 452, "f(m) = 1 − 0,6 = 0,4", { fs: 28, c: o.C.iv, ancre: "start", cls: "ser" });
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 5), t4 = o.et(v, "4", 7);
      apparait(o, leg, t, t1, .6);
      inds.forEach(function (d, j) {
        d.g.setAttribute("opacity", o.E(o.P(t, t1 + j * .05, .4)).toFixed(3));
        var on = d.a[0] === "A" && d.a[1] === "A" ? t2 : d.a[0] === "A" ? t3 : 1e9;
        var p = o.P(t, on, .5), fin = o.P(t, on + 2.2, .6);
        d.h.setAttribute("opacity", (o.E(p) * (1 - fin * .7)).toFixed(3));
      });
      apparait(o, c1, t, t2 + .4, .5); apparait(o, c2, t, t3 + .4, .5);
      apparait(o, c3, t, t4, .5); apparait(o, c4, t, t4 + .7, .6); apparait(o, c5, t, t4 + 1.4, .6);
    };
  };

  // tableau de croisement en surfaces : un carré de côté 1 coupé à p (v.p) ; {id.1} gamètes, {id.2} p², {id.3} les deux pq,
  // {id.4} q², {id.5} p² + 2pq + q² = (p + q)² = 1
  SERIE_ILLU.croisement = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), p = v.p || .6, L = Math.min(H - 150, 420), x0 = 210, y0 = 110;
    var a = L * p, b = L * (1 - p);
    function bande(x, y, w, h, c) { return o.sv("rect", { x: x, y: y, width: w, height: h, fill: c, "fill-opacity": .9, stroke: "#06120b", "stroke-width": 2 }, g); }
    var ga = o.sv("g", {}, g);
    o.etiquette(ga, x0 + L / 2, y0 - 66, "gamètes mâles", { fs: 22, c: o.C.iv2 });
    o.sv("rect", { x: x0, y: y0 - 34, width: a, height: 20, fill: COUL.A }, ga); o.sv("rect", { x: x0 + a, y: y0 - 34, width: b, height: 20, fill: COUL.m }, ga);
    o.etiquette(ga, x0 + a / 2, y0 - 40, "A : p", { fs: 20, c: "#06120b" }); o.etiquette(ga, x0 + a + b / 2, y0 - 40, "m : q", { fs: 20, c: o.C.iv });
    o.sv("rect", { x: x0 - 34, y: y0, width: 20, height: a, fill: COUL.A }, ga); o.sv("rect", { x: x0 - 34, y: y0 + a, width: 20, height: b, fill: COUL.m }, ga);
    o.etiquette(ga, x0 - 46, y0 + a / 2 + 7, "A : p", { fs: 20, c: o.C.iv, ancre: "end" }); o.etiquette(ga, x0 - 46, y0 + a + b / 2 + 7, "m : q", { fs: 20, c: o.C.iv, ancre: "end" });
    var gf = o.etiquette(ga, x0 - 120, y0 + L + 34, "gamètes femelles", { fs: 22, c: o.C.iv2 });
    var cAA = bande(x0, y0, a, a, "#5f7a24"), cAm1 = bande(x0 + a, y0, b, a, "#7b5a3a"), cAm2 = bande(x0, y0 + a, a, b, "#7b5a3a"), cmm = bande(x0 + a, y0 + a, b, b, "#8a3d2a");
    var tAA = o.etiquette(g, x0 + a / 2, y0 + a / 2 + 4, "A//A", { fs: 26 }), tAA2 = o.etiquette(g, x0 + a / 2, y0 + a / 2 + 38, "p × p = p²", { fs: 24, c: o.C.or, cls: "ser" });
    var tAm1 = o.etiquette(g, x0 + a + b / 2, y0 + a / 2 + 4, "A//m", { fs: 22 }), tAm1b = o.etiquette(g, x0 + a + b / 2, y0 + a / 2 + 34, "pq", { fs: 24, c: o.C.or, cls: "ser" });
    var tAm2 = o.etiquette(g, x0 + a / 2, y0 + a + b / 2 + 4, "A//m", { fs: 22 }), tAm2b = o.etiquette(g, x0 + a / 2, y0 + a + b / 2 + 34, "pq", { fs: 24, c: o.C.or, cls: "ser" });
    var tmm = o.etiquette(g, x0 + a + b / 2, y0 + a + b / 2 + 4, "m//m", { fs: 22 }), tmmb = o.etiquette(g, x0 + a + b / 2, y0 + a + b / 2 + 34, "q²", { fs: 24, c: o.C.or, cls: "ser" });
    var xr = x0 + L + 70;
    var r1 = o.etiquette(g, xr, y0 + 40, "f(A//A) = p²", { fs: 32, ancre: "start", cls: "ser" });
    var r2 = o.etiquette(g, xr, y0 + 100, "f(A//m) = 2pq", { fs: 32, ancre: "start", cls: "ser" });
    var r2b = o.etiquette(g, xr, y0 + 136, "deux cases : A du père et m de la mère, ou l'inverse", { fs: 19, c: o.C.iv2, ancre: "start" });
    var r3 = o.etiquette(g, xr, y0 + 196, "f(m//m) = q²", { fs: 32, ancre: "start", cls: "ser" });
    var r4 = o.etiquette(g, xr, y0 + 280, "p² + 2pq + q² = 1", { fs: 40, c: o.C.sa, ancre: "start", cls: "ser" });
    var r5 = o.etiquette(g, xr, y0 + 326, "c'est (p + q)² = 1² : l'aire du carré", { fs: 21, c: o.C.iv2, ancre: "start" });
    var cad = o.sv("rect", { x: x0 - 6, y: y0 - 6, width: L + 12, height: L + 12, rx: 6, fill: "none", stroke: o.C.sa, "stroke-width": 4 }, g);
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 2.5), t3 = o.et(v, "3", 4.5), t4 = o.et(v, "4", 6.5), t5 = o.et(v, "5", 8.5);
      apparait(o, ga, t, t1, .7);
      [cAA, tAA, tAA2, r1].forEach(function (e, i) { apparait(o, e, t, t2 + i * .15, .5); });
      [cAm1, cAm2, tAm1, tAm1b, tAm2, tAm2b, r2, r2b].forEach(function (e, i) { apparait(o, e, t, t3 + (i % 2) * .3 + (i > 5 ? .6 : 0), .5); });
      [cmm, tmm, tmmb, r3].forEach(function (e, i) { apparait(o, e, t, t4 + i * .15, .5); });
      apparait(o, r4, t, t5, .6); apparait(o, r5, t, t5 + .6, .6);
      var q = o.P(t, t5, 1.2); cad.setAttribute("opacity", (o.E(q) * (.6 + .4 * Math.sin(t * 3))).toFixed(3));
    };
  };

  // effectifs observés et attendus, génotype par génotype : v.obs, v.att (mêmes unités), v.max ;
  // {id.1} observés, {id.2} attendus, {id.3} verdict (v.verdict, v.ok)
  SERIE_ILLU.barres = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), noms = v.noms || ["A//A", "A//m", "m//m"];
    var base = H - 90, haut = H - 190, mx = v.max || Math.max.apply(null, v.obs.concat(v.att)), pas = (W - 160) / noms.length, bw = Math.min(70, pas * .3);
    var axe = o.sv("path", { d: "M70 " + base + " H" + (W - 40), stroke: o.C.iv, "stroke-width": 2.2, fill: "none" }, g);
    if (v.titre) o.etiquette(g, W / 2, 36, v.titre, { fs: 26, c: o.C.iv });
    var leg = o.sv("g", {}, g);
    o.sv("rect", { x: W - 360, y: 62, width: 22, height: 22, fill: o.C.te }, leg); o.etiquette(leg, W - 330, 81, "observé", { fs: 21, ancre: "start" });
    o.sv("rect", { x: W - 220, y: 62, width: 22, height: 22, fill: "none", stroke: o.C.or, "stroke-width": 3, "stroke-dasharray": "6 4" }, leg); o.etiquette(leg, W - 190, 81, "attendu (H-W)", { fs: 21, ancre: "start" });
    var bs = noms.map(function (n, i) {
      var cx = 110 + pas * (i + .5);
      o.etiquette(g, cx, base + 38, n, { fs: 26, cls: "ser" });
      var ho = haut * v.obs[i] / mx, ha = haut * v.att[i] / mx;
      var ro = o.sv("rect", { x: cx - bw - 6, y: base, width: bw, height: 0, fill: o.C.te, rx: 4 }, g);
      var ra = o.sv("rect", { x: cx + 6, y: base, width: bw, height: 0, fill: "none", stroke: o.C.or, "stroke-width": 3, "stroke-dasharray": "7 5", rx: 4 }, g);
      var to = o.etiquette(g, cx - bw / 2 - 6, base - ho - 12, String(v.obs[i]).replace(".", ","), { fs: 22, c: o.C.te });
      var ta = o.etiquette(g, cx + bw / 2 + 6, base - ha - 12, String(v.att[i]).replace(".", ","), { fs: 22, c: o.C.or });
      return { ro: ro, ra: ra, to: to, ta: ta, ho: ho, ha: ha };
    });
    var ver = o.etiquette(g, W / 2, H - 14, v.verdict || "", { fs: 26, c: v.ok ? o.C.vert : o.C.ca });
    return function (t, st) {
      var t1 = o.et(v, "1", .4), t2 = o.et(v, "2", 2.5), t3 = o.et(v, "3", 4.5);
      apparait(o, leg, t, t1, .5);
      bs.forEach(function (b, i) {
        var po = o.EIO(o.P(t, t1 + i * .25, .8)), pa = o.EIO(o.P(t, t2 + i * .25, .8));
        b.ro.setAttribute("y", base - b.ho * po); b.ro.setAttribute("height", b.ho * po);
        b.ra.setAttribute("y", base - b.ha * pa); b.ra.setAttribute("height", b.ha * pa);
        b.to.setAttribute("opacity", o.E(o.P(t, t1 + i * .25 + .6, .4))); b.ta.setAttribute("opacity", o.E(o.P(t, t2 + i * .25 + .6, .4)));
      });
      apparait(o, ver, t, t3, .6);
    };
  };

  // le schéma de la diapositive 20 : 9 individus, 5 se reproduisent (2, 1, 1, 1 et 3 descendants), puis 8, puis 10 ;
  // {id.1} génération 1, {id.2} les reproducteurs, {id.3} génération 2, {id.4} génération 3, {id.5} « génération 10 : ? »
  SERIE_ILLU.derive9 = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), cc = [COUL.A, COUL.B, COUL.X];
    var G1 = [0, 1, 0, 2, 1, 0, 2, 1, 0], REP = [[0, 2], [2, 1], [4, 1], [6, 1], [7, 3]];
    var G2 = []; REP.forEach(function (r) { for (var k = 0; k < r[1]; k++) G2.push([G1[r[0]], r[0]]); });
    var G3c = [0, 0, 2, 0, 1, 0, 0, 2, 0, 0], G3p = [0, 0, 1, 2, 3, 3, 4, 6, 7, 7];
    var ys = [90, 270, 450], xs = function (n, i) { return W / 2 + 60 + (i - (n - 1) / 2) * 74; };
    var et1 = o.etiquette(g, 26, ys[0] + 8, "Génération 1", { fs: 22, ancre: "start", c: o.C.iv2 });
    var et2 = o.etiquette(g, 26, ys[1] + 8, "Génération 2", { fs: 22, ancre: "start", c: o.C.iv2 });
    var et3 = o.etiquette(g, 26, ys[2] + 8, "Génération 3", { fs: 22, ancre: "start", c: o.C.iv2 });
    var liens = o.sv("g", {}, g), liens2 = o.sv("g", {}, g);
    var b1 = G1.map(function (c, i) { return bille(o, g, xs(9, i), ys[0], 24, cc[c]); });
    var rep = REP.map(function (r) { return o.sv("circle", { cx: xs(9, r[0]), cy: ys[0], r: 31, fill: "none", stroke: o.C.or, "stroke-width": 3.5 }, g); });
    var nb = REP.map(function (r) { return o.etiquette(g, xs(9, r[0]), ys[0] - 42, r[1] + "", { fs: 22, c: o.C.or }); });
    var b2 = G2.map(function (d, i) {
      o.sv("path", { d: "M" + xs(9, d[1]) + " " + (ys[0] + 26) + " L" + xs(8, i) + " " + (ys[1] - 26), stroke: "rgba(255,210,74,.55)", "stroke-width": 2, fill: "none" }, liens);
      return bille(o, g, xs(8, i), ys[1], 24, cc[d[0]]);
    });
    var b3 = G3c.map(function (c, i) {
      o.sv("path", { d: "M" + xs(8, G3p[i]) + " " + (ys[1] + 26) + " L" + xs(10, i) + " " + (ys[2] - 26), stroke: "rgba(255,210,74,.45)", "stroke-width": 2, fill: "none" }, liens2);
      return bille(o, g, xs(10, i), ys[2], 24, cc[c]);
    });
    var pert = o.etiquette(g, W - 30, ys[0] + 60, "4 individus sans descendant", { fs: 20, c: o.C.ca, ancre: "end" });
    var fin = o.etiquette(g, W / 2, H - 22, "Génération 10 : composition impossible à prévoir", { fs: 28, c: o.C.or });
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 2.5), t3 = o.et(v, "3", 4.5), t4 = o.et(v, "4", 6.5), t5 = o.et(v, "5", 8.5);
      apparait(o, et1, t, t1, .5);
      b1.forEach(function (b, i) {
        var r = REP.some(function (x) { return x[0] === i; });
        b.setAttribute("opacity", (o.E(o.P(t, t1 + i * .07, .4)) * (r ? 1 : 1 - .65 * o.E(o.P(t, t2 + .4, .6)))).toFixed(3));
      });
      rep.forEach(function (r, i) { apparait(o, r, t, t2 + i * .12, .4); apparait(o, nb[i], t, t2 + .3 + i * .12, .4); });
      apparait(o, pert, t, t2 + 1, .5);
      apparait(o, et2, t, t3, .4); apparait(o, liens, t, t3, .6);
      b2.forEach(function (b, i) { apparait(o, b, t, t3 + .2 + i * .06, .4); });
      apparait(o, et3, t, t4, .4); apparait(o, liens2, t, t4, .6);
      b3.forEach(function (b, i) { apparait(o, b, t, t4 + .2 + i * .06, .4); });
      apparait(o, fin, t, t5, .6);
    };
  };

  // Buri : histogramme des 107 populations (v.hist[g][k] = nombre de populations ayant k allèles bw75 sur 32, génération g)
  // {id.1} départ (toutes à 16), puis les générations défilent jusqu'à {id.2} (génération 19), {id.3} fixées et perdues
  SERIE_ILLU.buri = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), hist = v.hist, NG = hist.length - 1, K = hist[0].length;
    var x0 = 80, x1 = W - 30, base = H - 80, top = 70, mx = v.max || 40, bw = (x1 - x0) / K;
    o.sv("path", { d: "M" + x0 + " " + base + " H" + x1, stroke: o.C.iv, "stroke-width": 2, fill: "none" }, g);
    o.sv("path", { d: "M" + x0 + " " + base + " V" + top, stroke: o.C.iv, "stroke-width": 2, fill: "none" }, g);
    [0, 8, 16, 24, 32].forEach(function (k) { o.etiquette(g, x0 + (k + .5) * bw, base + 28, (k / 32).toFixed(2).replace(".", ","), { fs: 18, c: o.C.iv2 }); });
    o.etiquette(g, (x0 + x1) / 2, base + 60, "fréquence de l'allèle bw75 dans la population", { fs: 20, c: o.C.iv2 });
    [10, 20, 30, 40].forEach(function (y) {
      var yy = base - (base - top) * y / mx;
      o.sv("path", { d: "M" + x0 + " " + yy + " H" + x1, stroke: "rgba(231,242,218,.08)", "stroke-width": 1 }, g);
      o.etiquette(g, x0 - 12, yy + 6, String(y), { fs: 17, c: o.C.iv2, ancre: "end" });
    });
    o.etiquette(g, x0 - 50, top - 22, "nombre de populations", { fs: 18, c: o.C.iv2, ancre: "start" });
    var rs = [];
    for (var k = 0; k < K; k++) rs.push(o.sv("rect", { x: x0 + k * bw + 1, y: base, width: bw - 2, height: 0, fill: k === 0 || k === K - 1 ? o.C.or : o.C.sa }, g));
    var gl = o.etiquette(g, x1, top - 10, "", { fs: 30, c: o.C.iv, ancre: "end", cls: "ser" });
    var lf = o.etiquette(g, x1 - 6, top + 40, "", { fs: 22, c: o.C.or, ancre: "end" });
    var lp = o.etiquette(g, x0 + 10, top + 40, "", { fs: 22, c: o.C.or, ancre: "start" });
    var l0 = o.etiquette(g, x0 + 16.5 * bw + 24, top + 30, "les 107 populations à 0,5", { fs: 22, c: o.C.sa, ancre: "start" });
    return function (t, st) {
      var t1 = o.et(v, "1", .5), t2 = o.et(v, "2", t1 - v.t0 + 12), t3 = o.et(v, "3", t2 - v.t0 + 2);
      var u = o.cl((t - t1) / Math.max(1, t2 - t1), 0, 1) * NG, ga = Math.floor(u), f = u - ga, gb = Math.min(NG, ga + 1);
      f = o.EIO(f);
      for (var k = 0; k < K; k++) {
        var val = hist[ga][k] * (1 - f) + hist[gb][k] * f, hh = (base - top) * Math.min(val, mx) / mx;
        rs[k].setAttribute("y", base - hh); rs[k].setAttribute("height", hh);
      }
      var gen = Math.round(u);
      gl.textContent = "génération " + gen; gl.setAttribute("opacity", o.E(o.P(t, t1, .4)));
      lf.textContent = "fixé (1) : " + hist[NG][K - 1] + " populations"; lp.textContent = "perdu (0) : " + hist[NG][0] + " populations";
      apparait(o, lf, t, t3, .5); apparait(o, lp, t, t3 + .3, .5);
      l0.setAttribute("opacity", (o.E(o.P(t, v.t0 + .3, .5)) * (1 - o.E(o.P(t, t1 + .4, .5)))).toFixed(3));
    };
  };

  // effet fondateur : une grande population (v.mere : allèles A, B, X en proportions), un petit groupe part (8 individus),
  // {id.1} la population mère, {id.2} le départ, {id.3} les fréquences comparées, {id.4} la colonie s'accroît (dérive)
  SERIE_ILLU.fondateur = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), N = 90, cols = ["A", "B", "X"];
    var mere = [], i;
    for (i = 0; i < N; i++) mere.push(i < 40 ? 0 : i < 76 ? 1 : 2);
    var place = [], pid = [3, 11, 19, 26, 44, 52, 61, 70];       // les fondateurs : 4 A, 4 B, aucun X
    for (i = 0; i < N; i++) {
      var a = o.alea(i * 3.1) * Math.PI * 2, r = 150 * Math.sqrt(o.alea(i * 7.7 + 1));
      place.push([250 + Math.cos(a) * r * 1.15, H / 2 - 10 + Math.sin(a) * r * .95]);
    }
    var ile = o.sv("ellipse", { cx: W - 250, cy: H / 2 - 10, rx: 200, ry: 160, fill: "rgba(92,200,214,.08)", stroke: o.C.te, "stroke-width": 2, "stroke-dasharray": "8 6" }, g);
    var lile = o.etiquette(g, W - 250, H / 2 - 185, "nouveau milieu", { fs: 22, c: o.C.te });
    var lm = o.etiquette(g, 250, H / 2 - 185, "population de départ", { fs: 22, c: o.C.iv2 });
    var bs = mere.map(function (c, j) { return bille(o, g, place[j][0], place[j][1], 13, COUL[cols[c]]); });
    var fl = o.sv("path", { d: "M440 " + (H / 2 - 10) + " C520 " + (H / 2 - 90) + " " + (W - 520) + " " + (H / 2 - 90) + " " + (W - 440) + " " + (H / 2 - 10), stroke: o.C.or, "stroke-width": 3, fill: "none", "stroke-dasharray": "10 8" }, g);
    var dest = pid.map(function (_, k) { return [W - 250 + ((k % 4) - 1.5) * 40, H / 2 - 30 + Math.floor(k / 4) * 40]; });
    // la colonie qui s'accroît : 32 descendants tirés dans les fondateurs (graine fixe), sans X
    var colo = [], seed = 0;
    for (i = 0; i < 32; i++) { var a2 = o.alea(i * 5.3 + 40) * Math.PI * 2, r2 = 145 * Math.sqrt(o.alea(i * 2.9 + 9)); colo.push([W - 250 + Math.cos(a2) * r2, H / 2 - 10 + Math.sin(a2) * r2 * .85, o.alea(i * 13.1) < .7 ? 0 : 1]); }
    var cb = colo.map(function (c) { return bille(o, g, c[0], c[1], 12, COUL[cols[c[2]]]); });
    var tab = o.sv("g", {}, g);
    function barres(x, titre, fr) {
      o.etiquette(tab, x + 72, H - 4, titre, { fs: 20, c: o.C.iv2 });
      fr.forEach(function (f, k) {
        o.sv("rect", { x: x + k * 52, y: H - 30 - f * 90, width: 40, height: f * 90, fill: COUL[cols[k]] }, tab);
        o.etiquette(tab, x + k * 52 + 20, H - 36 - f * 90, Math.round(f * 100) + " %", { fs: 17, c: o.C.iv });
      });
    }
    barres(150, "départ", [40 / 90, 36 / 90, 14 / 90]); barres(W - 330, "fondateurs", [4 / 8, 4 / 8, 0]);
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 6), t4 = o.et(v, "4", 9);
      apparait(o, lm, t, t1, .5);
      var mv = o.EIO(o.P(t, t2 + .6, 1.6));
      bs.forEach(function (b, j) {
        b.setAttribute("opacity", o.E(o.P(t, t1 + j * .012, .4)).toFixed(3));
        var k = pid.indexOf(j);
        if (k >= 0) {
          b.setAttribute("cx", place[j][0] + (dest[k][0] - place[j][0]) * mv); b.setAttribute("cy", place[j][1] + (dest[k][1] - place[j][1]) * mv - Math.sin(mv * Math.PI) * 80);
          b.setAttribute("stroke", t >= t2 ? o.C.or : "#06120b"); b.setAttribute("stroke-width", t >= t2 ? 3 : 1.6);
        }
      });
      apparait(o, ile, t, t2, .5); apparait(o, lile, t, t2, .5); fl.setAttribute("opacity", (o.E(o.P(t, t2, .5)) * (1 - o.E(o.P(t, t3, .5))) * .8).toFixed(3));
      apparait(o, tab, t, t3, .7);
      cb.forEach(function (b, k) { apparait(o, b, t, t4 + k * .07, .4); });
    };
  };

  // le peuplement de l'Amérique (explication proposée) : {id.1} l'Asie (allèles A, B, O), {id.2} un petit groupe passe la
  // Béringie, {id.3} l'Amérique peuplée presque seulement d'allèles O
  SERIE_ILLU.beringie = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), cols = ["A", "B", "O"];
    var asie = o.sv("path", { d: "M30 80 C200 40 420 70 520 150 C560 260 520 420 380 470 C240 520 80 470 40 360 C10 260 10 150 30 80 Z", fill: "rgba(183,217,76,.07)", stroke: o.C.iv2, "stroke-width": 2 }, g);
    var amer = o.sv("path", { d: "M" + (W - 40) + " 70 C" + (W - 240) + " 50 " + (W - 470) + " 90 " + (W - 520) + " 170 C" + (W - 560) + " 280 " + (W - 470) + " 400 " + (W - 330) + " 460 C" + (W - 250) + " 520 " + (W - 200) + " 560 " + (W - 140) + " " + (H - 20) + " C" + (W - 60) + " 480 " + (W - 30) + " 300 " + (W - 40) + " 70 Z", fill: "rgba(92,200,214,.07)", stroke: o.C.iv2, "stroke-width": 2 }, g);
    var la = o.etiquette(g, 250, 50, "Asie", { fs: 28, c: o.C.iv }), lb = o.etiquette(g, W - 260, 44, "Amérique", { fs: 28, c: o.C.iv });
    var pont = o.sv("path", { d: "M520 140 Q" + W / 2 + " 60 " + (W - 520) + " 150", stroke: o.C.or, "stroke-width": 3, fill: "none", "stroke-dasharray": "10 8" }, g);
    var lp = o.etiquette(g, W / 2, 70, "Béringie", { fs: 22, c: o.C.or });
    var as = [], i;
    for (i = 0; i < 60; i++) { var a = o.alea(i * 1.7) * 6.283, r = 140 * Math.sqrt(o.alea(i * 4.1 + 2)); as.push([280 + Math.cos(a) * r * 1.2, 280 + Math.sin(a) * r, i % 10 < 3 ? 0 : i % 10 < 5 ? 1 : 2]); }
    var ba = as.map(function (p) { return bille(o, g, p[0], p[1], 11, COUL[cols[p[2]]]); });
    var grp = [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [0, 5]].map(function (c, k) {
      return bille(o, g, 0, 0, 11, COUL[cols[c[0]]]);
    });
    var am = [];
    for (i = 0; i < 46; i++) { var a3 = o.alea(i * 2.3 + 77) * 6.283, r3 = 120 * Math.sqrt(o.alea(i * 6.1 + 5)); am.push([W - 300 + Math.cos(a3) * r3, 290 + Math.sin(a3) * r3 * 1.3, i === 17 ? 0 : 2]); }
    var bm = am.map(function (p) { return bille(o, g, p[0], p[1], 11, COUL[cols[p[2]]]); });
    var leg = o.sv("g", {}, g);
    [["A", "allèle A"], ["B", "allèle B"], ["O", "allèle O"]].forEach(function (x, k) {
      bille(o, leg, 60 + k * 150, H - 30, 10, COUL[x[0]]); o.etiquette(leg, 78 + k * 150, H - 23, x[1], { fs: 19, ancre: "start", c: o.C.iv2 });
    });
    var res = o.etiquette(g, W - 290, H - 30, "groupe O : 90 à 100 %", { fs: 26, c: o.C.or });
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 6);
      apparait(o, asie, t, t1, .6); apparait(o, la, t, t1, .6); apparait(o, leg, t, t1 + .4, .6);
      ba.forEach(function (b, k) { apparait(o, b, t, t1 + .3 + k * .015, .4); });
      apparait(o, amer, t, t2, .6); apparait(o, lb, t, t2, .6); apparait(o, pont, t, t2, .6); apparait(o, lp, t, t2 + .3, .5);
      var u = o.EIO(o.P(t, t2 + .5, 2.4));
      grp.forEach(function (b, k) {
        var x = 470 + (k % 3) * 24 + (W - 470 - 470 - 40) * u, y = 200 + Math.floor(k / 3) * 24 - Math.sin(u * Math.PI) * 110;
        b.setAttribute("cx", x); b.setAttribute("cy", y); b.setAttribute("opacity", (o.E(o.P(t, t2 + .3, .4)) * (1 - o.E(o.P(t, t3 + .6, .5)))).toFixed(3));
      });
      bm.forEach(function (b, k) { apparait(o, b, t, t3 + k * .03, .4); });
      apparait(o, res, t, t3 + 1.2, .6);
    };
  };

  // fréquences (%) chez les Européens, les Huttérites et les Amish (diapositive 29, d'après McLellan et coll., 1987) :
  // {id.k} le marqueur k ; la valeur européenne est une fourchette (moyenne dessinée, fourchette en trait)
  SERIE_ILLU.amish = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s);
    var M = [["Groupe sanguin A", [25, 32], 35, 66], ["Allèle HLA A11", [4.5, 7.4], 0, 14], ["Groupe Kell (K)", [3, 5], 14, .2]];
    var pops = [["Europe, États-Unis", o.C.iv2], ["Huttérites", o.C.te], ["Amish", o.C.or]];
    var lw = (W - 60) / 3, base = H - 70, top = 100;
    var leg = o.sv("g", {}, g);
    pops.forEach(function (p, k) { o.sv("rect", { x: 40 + k * 250, y: 18, width: 22, height: 22, fill: p[1] }, leg); o.etiquette(leg, 70 + k * 250, 37, p[0], { fs: 21, ancre: "start" }); });
    var grps = M.map(function (m, i) {
      var gg = o.sv("g", {}, g), cx = 30 + lw * (i + .5), mx = i === 0 ? 70 : 16;
      o.etiquette(gg, cx, base + 40, m[0], { fs: 22, c: o.C.iv });
      o.sv("path", { d: "M" + (cx - lw / 2 + 20) + " " + base + " H" + (cx + lw / 2 - 20), stroke: o.C.iv, "stroke-width": 2 }, gg);
      var vals = [(m[1][0] + m[1][1]) / 2, m[2], m[3]];
      var rs = vals.map(function (val, k) {
        var x = cx - 90 + k * 64, hh = (base - top) * val / mx;
        var r = o.sv("rect", { x: x, y: base, width: 52, height: 0, fill: pops[k][1], rx: 4 }, gg);
        var txt = k === 0 ? m[1][0].toString().replace(".", ",") + "–" + m[1][1].toString().replace(".", ",") : String(val).replace(".", ",");
        var l = o.etiquette(gg, x + 26, base - hh - 10, txt, { fs: 19, c: pops[k][1] });
        return { r: r, l: l, hh: hh };
      });
      return { g: gg, rs: rs };
    });
    var unite = o.etiquette(g, W - 20, 72, "fréquences en %", { fs: 18, c: o.C.iv2, ancre: "end" });
    return function (t, st) {
      apparait(o, leg, t, v.t0 + .2, .5); apparait(o, unite, t, v.t0 + .4, .5);
      grps.forEach(function (gr, i) {
        var t1 = o.et(v, String(i + 1), 1 + i * 2.5);
        gr.g.setAttribute("opacity", o.E(o.P(t, t1, .4)));
        gr.rs.forEach(function (r, k) {
          var u = o.EIO(o.P(t, t1 + .2 + k * .3, .7));
          r.r.setAttribute("y", base - r.hh * u); r.r.setAttribute("height", r.hh * u);
          r.l.setAttribute("opacity", o.E(o.P(t, t1 + .7 + k * .3, .4)));
        });
      });
    };
  };

  // la sélection par l'insecticide : {id.1} les larves (AceR rares), {id.2} l'épandage, {id.3} les larves AceS meurent,
  // {id.4} les survivantes se reproduisent : la génération suivante compte bien plus d'AceR
  SERIE_ILLU.tri = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s);
    var eau = o.sv("rect", { x: 30, y: 150, width: W / 2 - 60, height: H - 190, rx: 30, fill: "rgba(116,185,216,.14)", stroke: o.C.eau, "stroke-width": 2 }, g);
    var eau2 = o.sv("rect", { x: W / 2 + 30, y: 150, width: W / 2 - 60, height: H - 190, rx: 30, fill: "rgba(116,185,216,.14)", stroke: o.C.eau, "stroke-width": 2 }, g);
    var l1 = o.etiquette(g, W / 4, 130, "génération traitée", { fs: 22, c: o.C.iv2 }), l2 = o.etiquette(g, 3 * W / 4, 130, "génération suivante", { fs: 22, c: o.C.iv2 });
    function larve(x, y, c) {
      return o.sv("path", { d: "M" + (x - 16) + " " + y + " q8 -9 16 0 t16 0", stroke: c, "stroke-width": 7, "stroke-linecap": "round", fill: "none" }, g);
    }
    var L = [], i;
    for (i = 0; i < 24; i++) L.push([60 + (i % 6) * ((W / 2 - 120) / 5), 200 + Math.floor(i / 6) * ((H - 270) / 3) + (o.alea(i) - .5) * 20, i === 4 || i === 15 || i === 21]);
    var lv = L.map(function (p) { return larve(p[0], p[1], p[2] ? o.C.or : o.C.te); });
    var gouttes = [];
    for (i = 0; i < 14; i++) gouttes.push(o.sv("path", { d: "M0 -10 q6 10 0 14 q-6 -4 0 -14 Z", fill: "#e05a8a" }, g));
    var croix = L.map(function (p) { return p[2] ? null : o.etiquette(g, p[0], p[1] + 10, "✕", { fs: 30, c: o.C.ca }); });
    var N2 = [];
    for (i = 0; i < 24; i++) N2.push([W / 2 + 60 + (i % 6) * ((W / 2 - 120) / 5), 200 + Math.floor(i / 6) * ((H - 270) / 3) + (o.alea(i + 50) - .5) * 20, o.alea(i * 3.3 + 8) < .55]);
    var lv2 = N2.map(function (p) { return larve(p[0], p[1], p[2] ? o.C.or : o.C.te); });
    larve(80, H - 12, o.C.or);
    var t1l = o.etiquette(g, 105, H - 4, "AceR (résistante)", { fs: 19, ancre: "start", c: o.C.or });
    larve(330, H - 12, o.C.te);
    var t2l = o.etiquette(g, 355, H - 4, "AceS (sensible)", { fs: 19, ancre: "start", c: o.C.te });
    var fl = o.sv("path", { d: "M" + (W / 2 - 24) + " " + (H / 2 + 30) + " H" + (W / 2 + 24), stroke: o.C.iv, "stroke-width": 3 }, g);
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 5), t4 = o.et(v, "4", 7);
      apparait(o, eau, t, t1, .5); apparait(o, l1, t, t1, .5); apparait(o, t1l, t, t1 + .5, .5); apparait(o, t2l, t, t1 + .5, .5);
      lv.forEach(function (l, k) {
        var mort = !L[k][2], d = mort ? o.E(o.P(t, t3 + k * .03, .6)) : 0;
        l.setAttribute("opacity", (o.E(o.P(t, t1 + k * .03, .4)) * (1 - .8 * d)).toFixed(3));
        l.setAttribute("transform", "translate(0," + (Math.sin(t * 3 + k) * 3 * (1 - d)).toFixed(1) + ")");
      });
      gouttes.forEach(function (gt, k) {
        var u = o.P(t, t2 + k * .1, 1.1), x = 60 + (k * 37) % (W / 2 - 120), y = 140 + u * (H - 320);
        gt.setAttribute("transform", "translate(" + x + "," + y + ")"); gt.setAttribute("opacity", (u > 0 && u < 1 ? 1 : 0));
      });
      croix.forEach(function (c, k) { if (c) apparait(o, c, t, t3 + .3 + k * .03, .4); });
      apparait(o, eau2, t, t4, .5); apparait(o, l2, t, t4, .5); apparait(o, fl, t, t4, .4);
      lv2.forEach(function (l, k) { apparait(o, l, t, t4 + .3 + k * .04, .4); });
    };
  };

  // arbre des espèces puis réseau du vivant : {id.1} l'arbre, {id.2} des transferts horizontaux, {id.3} « réseau »
  SERIE_ILLU.reseau = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), yF = 96;
    var F = [W * .12, W * .3, W * .48, W * .66, W * .84], noms = v.noms || ["espèce 1", "espèce 2", "espèce 3", "espèce 4", "espèce 5"];
    var x1 = (F[0] + F[1]) / 2, x2 = (F[3] + F[4]) / 2, x3 = (F[2] + x2) / 2, xR = (x1 + x3) / 2;
    var y1 = 260, y2 = 240, y3 = 340, yR = 440;
    var D = ["M" + F[0] + " " + yF + " V" + y1 + " H" + F[1] + " V" + yF, "M" + F[3] + " " + yF + " V" + y2 + " H" + F[4] + " V" + yF,
      "M" + F[2] + " " + yF + " V" + y3 + " H" + x2 + " V" + y2, "M" + x1 + " " + y1 + " V" + yR + " H" + x3 + " V" + y3, "M" + xR + " " + yR + " V" + (yR + 60)];
    var arb = D.map(function (d) { return o.sv("path", { d: d, stroke: o.C.sa, "stroke-width": 4, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round" }, g); });
    var ls = noms.map(function (n, k) { return o.etiquette(g, F[k], yF - 18, n, { fs: 21, c: o.C.iv }); });
    var anc = o.etiquette(g, xR + 14, yR + 52, "ancêtre commun", { fs: 20, c: o.C.iv2, ancre: "start" });
    var tr = [[1, 3, 150], [0, 2, 200], [2, 4, 130], [1, 4, 215]].map(function (x) {
      var xa = F[x[0]], xb = F[x[1]], y = x[2];
      var p = o.sv("path", { d: "M" + xa + " " + y + " Q" + (xa + xb) / 2 + " " + (y - 60) + " " + xb + " " + y, stroke: o.C.or, "stroke-width": 3, fill: "none", "stroke-dasharray": "9 7" }, g);
      var a = o.sv("circle", { cx: xa, cy: y, r: 6, fill: o.C.or }, g), b = o.sv("circle", { cx: xb, cy: y, r: 6, fill: o.C.or }, g);
      return [p, a, b];
    });
    var L1 = v.legende1 || "arbre : les branches ne se croisent jamais", L2 = v.legende2 || "réseau du vivant : des transferts horizontaux relient les branches";
    var tx = o.etiquette(g, W / 2, H - 10, L1, { fs: 23, c: o.C.sa });
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 4), t3 = v.et && v.et["3"] != null ? v.et["3"] : t2 + 1.5;
      arb.forEach(function (a, k) { o.trace(a, o.P(t, t1 + k * .25, .9)); });
      ls.forEach(function (l, k) { apparait(o, l, t, t1 + 1.2 + k * .1, .4); }); apparait(o, anc, t, t1 + 1.6, .4);
      var deux = t >= t3;
      tx.textContent = deux ? L2 : L1; tx.setAttribute("fill", deux ? o.C.or : o.C.sa);
      tx.setAttribute("opacity", (deux ? o.E(o.P(t, t3, .5)) : o.E(o.P(t, t1 + 1.5, .5)) * (1 - o.E(o.P(t, t2, .4)))).toFixed(3));
      tr.forEach(function (x, k) { x.forEach(function (e) { apparait(o, e, t, t2 + k * .5, .5); }); });
    };
  };

  // l'arbre de la diapositive 44 : {id.1} les sapiens actuels, {id.2} les Néandertaliens, {id.3} Denisova, à côté d'eux
  SERIE_ILLU.denisova = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s);
    var F = [["San", 0], ["Yoruba", 0], ["Français", 0], ["Han", 0], ["Papous", 0], ["Mezmaiskaya", 1], ["Vindija", 1], ["Denisova", 2]];
    var x0 = 60, xF = W - 260, pas = (H - 90) / F.length, Yk = function (k) { return 50 + k * pas; };
    var cS = (Yk(0) + Yk(4)) / 2, cN = (Yk(5) + Yk(6)) / 2, cND = (cN + Yk(7)) / 2, cR = (cS + cND) / 2;
    var xS = xF - 260, xN = xF - 150, xND = xF - 330, xR = x0 + 40;
    function ligne(d, c) { return o.sv("path", { d: d, stroke: c, "stroke-width": 4, fill: "none", "stroke-linecap": "round" }, g); }
    var sap = [ligne("M" + xS + " " + Yk(0) + " V" + Yk(4), o.C.te)].concat(F.slice(0, 5).map(function (f, k) { return ligne("M" + xS + " " + Yk(k) + " H" + xF, o.C.te); }));
    var nea = [ligne("M" + xN + " " + Yk(5) + " V" + Yk(6), o.C.sa), ligne("M" + xN + " " + Yk(5) + " H" + xF, o.C.sa), ligne("M" + xN + " " + Yk(6) + " H" + xF, o.C.sa)];
    var den = [ligne("M" + xND + " " + cN + " V" + Yk(7), o.C.or), ligne("M" + xND + " " + cN + " H" + xN, o.C.sa), ligne("M" + xND + " " + Yk(7) + " H" + xF, o.C.or)];
    var rac = [ligne("M" + xR + " " + cS + " V" + cND, o.C.iv2), ligne("M" + xR + " " + cS + " H" + xS, o.C.te), ligne("M" + xR + " " + cND + " H" + xND, o.C.iv2), ligne("M" + (xR - 30) + " " + cR + " H" + xR, o.C.iv2)];
    var ls = F.map(function (f, k) { return o.etiquette(g, xF + 14, Yk(k) + 7, f[0], { fs: 22, ancre: "start", c: [o.C.te, o.C.sa, o.C.or][f[1]] }); });
    var gS = o.etiquette(g, xS - 16, cS - 14, "Homo sapiens actuels", { fs: 21, c: o.C.te, ancre: "end" });
    var gN = o.etiquette(g, xND - 14, cN + 7, "Néandertaliens", { fs: 21, c: o.C.sa, ancre: "end" });
    var gD = o.etiquette(g, xND - 12, Yk(7) + 32, "Dénisoviens : une phalange et une molaire", { fs: 20, c: o.C.or, ancre: "start" });
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 6);
      rac.concat(sap).forEach(function (l, k) { o.trace(l, o.P(t, t1 + k * .1, .7)); });
      F.forEach(function (f, k) { apparait(o, ls[k], t, [t1, t2, t3][f[1]] + .6 + k * .05, .4); });
      apparait(o, gS, t, t1 + 1, .5);
      nea.forEach(function (l, k) { o.trace(l, o.P(t, t2 + k * .2, .7)); }); apparait(o, gN, t, t2 + .8, .5);
      den.forEach(function (l, k) { o.trace(l, o.P(t, t3 + k * .2, .7)); }); apparait(o, gD, t, t3 + 1, .5);
    };
  };

  // espèce en devenir : {id.1} une population, {id.2} une barrière la coupe, {id.3} les deux moitiés se différencient
  // (dérive, sélection), {id.4} plus d'échange de gènes
  SERIE_ILLU.speciation = function (s, v) {
    var o = O(), W = v.w, H = v.h, g = o.sv("g", {}, s), P = [], i;
    for (i = 0; i < 70; i++) P.push([60 + o.alea(i * 1.3) * (W - 120), 70 + o.alea(i * 2.7 + 3) * (H - 170)]);
    var bs = P.map(function (p, k) { return bille(o, g, p[0], p[1], 12, k % 2 ? COUL.A : COUL.B); });
    var bar = o.sv("path", { d: "M" + W / 2 + " 40 C" + (W / 2 - 40) + " 200 " + (W / 2 + 40) + " 360 " + W / 2 + " " + (H - 80), stroke: o.C.eau, "stroke-width": 16, fill: "none", "stroke-linecap": "round" }, g);
    var lb = o.etiquette(g, W / 2, 26, v.barriere || "une barrière naturelle (fleuve, montagne…)", { fs: 21, c: o.C.eau });
    var fl = o.sv("g", {}, g);
    o.sv("path", { d: "M" + (W / 2 - 90) + " " + (H / 2) + " H" + (W / 2 + 90), stroke: o.C.iv, "stroke-width": 3, "stroke-dasharray": "8 6" }, fl);
    o.etiquette(fl, W / 2, H / 2 + 14, "✕", { fs: 46, c: o.C.ca });
    o.etiquette(fl, W / 2, H / 2 + 54, "plus de reproduction entre elles", { fs: 20, c: o.C.ca });
    var cap = o.etiquette(g, W / 2, H - 20, "", { fs: 24, c: o.C.or });
    // couleur finale : à gauche surtout A puis X, à droite surtout B
    var fin = P.map(function (p, k) { var gauche = p[0] < W / 2; var r = o.alea(k * 9.1); return gauche ? (r < .6 ? COUL.X : COUL.A) : (r < .8 ? COUL.B : COUL.O); });
    function mix(a, b, u) {
      function c(h) { return [parseInt(h.substr(1, 2), 16), parseInt(h.substr(3, 2), 16), parseInt(h.substr(5, 2), 16)]; }
      var x = c(a), y = c(b); return "rgb(" + x.map(function (v_, k) { return Math.round(v_ + (y[k] - v_) * u); }).join(",") + ")";
    }
    return function (t, st) {
      var t1 = o.et(v, "1", .3), t2 = o.et(v, "2", 3), t3 = o.et(v, "3", 6), t4 = o.et(v, "4", 9);
      var u = o.EIO(o.P(t, t3, 3));
      bs.forEach(function (b, k) {
        apparait(o, b, t, t1 + k * .015, .4);
        var x = P[k][0], dx = Math.sin(t * .7 + k) * 6;
        if (t < t2) x += Math.sin(t * .4 + k * 2) * 30;
        else x += (x < W / 2 ? -1 : 1) * 30 * o.E(o.P(t, t2, 1));
        b.setAttribute("cx", (x + dx).toFixed(1));
        b.setAttribute("fill", mix(k % 2 ? COUL.A : COUL.B, fin[k], u));
      });
      o.trace(bar, o.P(t, t2, 1.2)); apparait(o, lb, t, t2 + .4, .5);
      apparait(o, fl, t, t4, .6);
      cap.textContent = t >= t4 ? "une population isolée génétiquement : une espèce en devenir" : t >= t3 ? "dérive et sélection : chaque moitié évolue à sa façon" : "";
      cap.setAttribute("opacity", o.E(o.P(t, t >= t4 ? t4 : t3, .5)));
    };
  };
})();
