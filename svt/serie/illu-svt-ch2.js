/* Vidéo du chapitre 2 de SVT (« La complexification des génomes ») : illustrations propres au chapitre.
   Chargé par svt/serie/svt-ch2.html s'il existe ; outils du moteur dans window.SERIE_OUTILS.
   Rendu fonction pure du temps : SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; }
   griffith : les quatre lots de l'expérience de 1928 ; grille : tableau comparatif dont les lignes entrent une à une ;
   barres : pourcentages ou nombres comparés (avec seuil) ; lignee : transfert horizontal dans une cellule germinale,
   puis transmission verticale aux espèces descendantes (syncytine). */
(function () {
  "use strict";
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var O = window.SERIE_OUTILS;   // défini par moteur.js, chargé après ce fichier : relu à chaque construction

  // texte SVG coupé en lignes (largeur approchée : 0,52 × taille par caractère)
  function bloc(g, x, y, txt, opt) {
    opt = opt || {};
    var fs = opt.fs || 24, max = opt.max || 300, lh = opt.lh || fs * 1.22, par = Math.max(4, Math.floor(max / (fs * 0.52)));
    var mots = String(txt).split(" "), lignes = [], l = "";
    mots.forEach(function (m) { var e = l ? l + " " + m : m; if (l && e.length > par) { lignes.push(l); l = m; } else l = e; });
    if (l) lignes.push(l);
    var y0 = opt.centreV ? y - (lignes.length - 1) * lh / 2 : y;
    var el = O.sv("text", { x: x, y: y0, "text-anchor": opt.ancre || "start", fill: opt.c || O.C.iv, "font-size": fs,
      "font-weight": opt.fw || 500, "font-family": opt.serif ? "Spectral, Georgia, serif" : "Archivo, sans-serif" }, g);
    lignes.forEach(function (li, i) { O.sv("tspan", { x: x, dy: i ? lh : 0 }, el, li); });
    el._n = lignes.length;
    return el;
  }
  function apparait(e, p, dy) { O.op(e, p); e.setAttribute("transform", "translate(0," + ((dy == null ? 14 : dy) * (1 - p)).toFixed(1) + ")"); }

  /* ---------- Griffith, 1928 : quatre lots de souris ---------- */
  function bacterie(g, x, y, type) {
    var b = O.sv("g", { transform: "translate(" + x + "," + y + ")" }, g);
    [[-26, -8], [6, -20], [22, 10], [-8, 18]].forEach(function (p, i) {
      var c = O.sv("g", { transform: "translate(" + p[0] + "," + p[1] + ") rotate(" + (i * 40) + ")" }, b);
      if (type === "S" || type === "Smort") O.sv("ellipse", { rx: 21, ry: 15, fill: "none", stroke: type === "S" ? "#7fbecb" : "rgba(180,203,156,.45)", "stroke-width": 5 }, c);
      O.sv("ellipse", { rx: 14, ry: 9, fill: type === "Smort" ? "rgba(180,203,156,.25)" : type === "S" ? "#2f9d62" : "#b7d94c",
        stroke: type === "Smort" ? "rgba(180,203,156,.6)" : "none", "stroke-width": 2 }, c);
    });
    if (type === "Smort") O.sv("path", { d: "M-34 -30 L34 30 M34 -30 L-34 30", stroke: "#ff6b5b", "stroke-width": 4, "stroke-linecap": "round", opacity: .85 }, b);
    return b;
  }
  function souris(g, x, y, morte) {
    var s = O.sv("g", { transform: "translate(" + x + "," + y + ")" }, g), col = morte ? "rgba(231,242,218,.42)" : "#e7f2da";
    O.sv("path", { d: "M44 6 C70 4 84 -10 96 -24", fill: "none", stroke: col, "stroke-width": 4, "stroke-linecap": "round" }, s);
    O.sv("ellipse", { cx: 8, cy: 0, rx: 42, ry: 25, fill: col }, s);
    O.sv("circle", { cx: -36, cy: -8, r: 18, fill: col }, s);
    O.sv("circle", { cx: -30, cy: -28, r: 10, fill: col }, s);
    O.sv("circle", { cx: -48, cy: -26, r: 9, fill: col }, s);
    if (morte) O.sv("path", { d: "M-47 -14 l8 8 m0 -8 l-8 8", stroke: "#0a1710", "stroke-width": 3, "stroke-linecap": "round" }, s);
    else O.sv("circle", { cx: -42, cy: -10, r: 3.4, fill: "#0a1710" }, s);
    return s;
  }
  window.SERIE_ILLU.griffith = function (svg, v) {
    O = window.SERIE_OUTILS;
    var W = v.w, cadres = O.sv("g", {}, svg), g = O.sv("g", {}, svg), cw = W / 4;
    var lots = [
      { b: [["S", 0]], txt: "S vivants", res: "meurt", morte: true },
      { b: [["R", 0]], txt: "R vivants", res: "survit", morte: false },
      { b: [["Smort", 0]], txt: "S tués par la chaleur", res: "survit", morte: false },
      { b: [["Smort", -46], ["R", 46]], txt: "S tués + R vivants", res: "meurt", morte: true, sang: true }];
    var cols = lots.map(function (L, i) {
      var cx = cw * i + cw / 2, f = O.sv("g", {}, cadres), c = O.sv("g", {}, g);
      // le cadre et le numéro du lot sont là dès le début (pas d'écran vide) ; le contenu entre au repère du lot
      O.sv("rect", { x: cw * i + 10, y: 8, width: cw - 20, height: v.h - 16, rx: 18, fill: "rgba(231,242,218,.05)", stroke: "rgba(231,242,218,.16)", "stroke-width": 1.5 }, f);
      O.etiquette(f, cx, 50, "Lot " + (i + 1), { fs: 22, c: O.C.sa, fw: 700, ls: ".12em" });
      O.etiquette(f, cx, v.h / 2, "?", { fs: 64, c: "rgba(231,242,218,.18)", fw: 700, cls: "attente" });
      L.b.forEach(function (b) { bacterie(c, cx + b[1], 125, b[0]); });
      bloc(c, cx, 200, L.txt, { fs: 23, max: cw - 40, ancre: "middle", fw: 600 });
      var fl = O.sv("path", { d: "M" + cx + " 258 V318", stroke: O.C.iv2, "stroke-width": 3, "marker-end": "" }, c);
      O.sv("path", { d: "M" + (cx - 9) + " 306 L" + cx + " 322 L" + (cx + 9) + " 306", fill: "none", stroke: O.C.iv2, "stroke-width": 3 }, c);
      var so = souris(c, cx - 10, 368, L.morte);
      var r = O.etiquette(c, cx, 432, "la souris " + L.res, { fs: 25, c: L.morte ? "#ff6b5b" : "#7ce08a", fw: 700 });
      var sg = null;
      if (L.sang) {
        sg = O.sv("g", {}, c);
        bloc(sg, cx, 470, "dans son sang : des S vivants", { fs: 21, max: cw - 36, ancre: "middle", c: O.C.or, fw: 600 });
      }
      return { c: c, sg: sg, fl: fl, q: f.querySelector(".attente") };
    });
    var cadre = O.sv("rect", { x: cw * 3 + 4, y: 2, width: cw - 8, height: v.h - 4, rx: 22, fill: "none", stroke: O.C.or, "stroke-width": 4 }, g);
    return function (t, st) {
      O.op(cadres, O.E(O.P(st.tl, 0, .6)));
      cols.forEach(function (c, i) {
        var k = O.et(v, String(i + 1), .4 + i * 1.2), p = O.E(O.P(t, k, .7));
        apparait(c.c, p, 24);
        if (c.q) O.op(c.q, 1 - p);
        if (c.sg) O.op(c.sg, O.E(O.P(t, O.et(v, "5", 6), .7)));
      });
      var q = O.P(t, O.et(v, "5", 6) + .2, .8);
      O.op(cadre, O.E(q) * (.65 + .35 * Math.sin(t * 3)));
    };
  };

  /* ---------- grille : tableau comparatif ---------- */
  // v.cols : en-têtes (la première peut être vide : colonne des intitulés) ; v.rows : lignes ; v.larg : largeurs relatives ;
  // la ligne k entre au repère {id.k} ; v.fs : taille du texte
  window.SERIE_ILLU.grille = function (svg, v) {
    O = window.SERIE_OUTILS;
    var W = v.w, g = O.sv("g", {}, svg), fs = v.fs || 23, nc = v.cols.length;
    var larg = v.larg || v.cols.map(function () { return 1; }), tot = larg.reduce(function (a, b) { return a + b; }, 0);
    var xs = [0]; larg.forEach(function (l, i) { xs.push(xs[i] + W * l / tot); });
    var y = 0, hh = fs * 2.3;
    var tete = O.sv("g", {}, g);
    O.sv("rect", { x: 0, y: 0, width: W, height: hh, rx: 12, fill: "rgba(183,217,76,.14)" }, tete);
    v.cols.forEach(function (c, i) { if (c) bloc(tete, (xs[i] + xs[i + 1]) / 2, hh / 2 + fs * .35, c, { fs: fs * .9, max: xs[i + 1] - xs[i] - 20, ancre: "middle", c: O.C.sa, fw: 700, centreV: true }); });
    y = hh + 6;
    var lignes = v.rows.map(function (r, k) {
      var lg = O.sv("g", {}, g), n = 1, els = [];
      r.forEach(function (cell, i) {
        var e = bloc(lg, xs[i] + 16, 0, cell, { fs: i === 0 && v.cols[0] === "" ? fs * .92 : fs, max: xs[i + 1] - xs[i] - 30,
          fw: i === 0 && v.cols[0] === "" ? 700 : 500, c: i === 0 && v.cols[0] === "" ? O.C.iv2 : O.C.iv, serif: i > 0 || v.cols[0] !== "" });
        els.push(e); n = Math.max(n, e._n);
      });
      var hr = n * fs * 1.22 + fs * 1.1;
      var fond = O.sv("rect", { x: 0, y: y, width: W, height: hr, rx: 10, fill: k % 2 ? "rgba(231,242,218,.035)" : "rgba(231,242,218,.07)" }, lg);
      lg.insertBefore(fond, lg.firstChild);
      els.forEach(function (e) { e.setAttribute("y", y + fs * 1.25); });
      for (var i = 1; i < nc; i++) O.sv("line", { x1: xs[i], x2: xs[i], y1: y + 8, y2: y + hr - 8, stroke: "rgba(231,242,218,.18)", "stroke-width": 1.4 }, lg);
      y += hr + 6;
      return { g: lg, fond: fond };
    });
    return function (t, st) {
      O.op(tete, O.E(O.P(st.tl, 0, .6)));
      var hl = v.et && v.et.hl != null ? v.et.hl : null;
      lignes.forEach(function (l, k) {
        var tk = O.et(v, String(k + 1), .5 + k * .7), p = O.E(O.P(t, tk, .6));
        apparait(l.g, p, 16);
        var actif = hl != null && t >= hl && (v.hlr || []).indexOf(k + 1) >= 0;
        l.fond.setAttribute("stroke", actif ? "rgba(255,210,74," + (.55 + .35 * Math.sin(t * 3)).toFixed(2) + ")" : "none");
        l.fond.setAttribute("stroke-width", 3);
      });
    };
  };

  /* ---------- barres : valeurs comparées, seuil éventuel ---------- */
  // v.items : [{t, v, lbl?, c?, plus?}] ; v.max ; v.seuil (+ v.lseuil) ; la barre k pousse au repère {id.k}, le seuil au repère {id.s}
  window.SERIE_ILLU.barres = function (svg, v) {
    O = window.SERIE_OUTILS;
    var W = v.w, g = O.sv("g", {}, svg), n = v.items.length, x0 = v.x0 || 330, x1 = W - 150, bh = v.bh || 46;
    var gap = (v.h - 60 - n * bh) / Math.max(1, n), X = function (val) { return x0 + (x1 - x0) * Math.min(1, val / v.max); };
    var bs = v.items.map(function (it, k) {
      var y = 30 + k * (bh + gap) + gap / 2, bg = O.sv("g", {}, g);
      bloc(bg, x0 - 22, y + bh / 2 + 8, it.t, { fs: v.fs || 23, max: x0 - 30, ancre: "end", fw: 600, centreV: true });
      O.sv("rect", { x: x0, y: y, width: x1 - x0, height: bh, rx: 8, fill: "rgba(231,242,218,.06)" }, bg);
      var r = O.sv("rect", { x: x0, y: y, width: 0, height: bh, rx: 8, fill: it.c || O.C.sa2 }, bg);
      var fl = it.plus ? O.sv("path", { d: "M" + (x1 + 4) + " " + (y + 6) + " l26 " + (bh / 2 - 6) + " l-26 " + (bh / 2 - 6), fill: it.c || O.C.sa2 }, bg) : null;
      var lb = O.etiquette(bg, X(it.v) + 14, y + bh / 2 + 9, it.lbl || (it.v + (v.unite || "")), { fs: 28, ancre: "start", c: O.C.iv, fw: 700 });
      if (it.plus) lb.setAttribute("x", x0 + 16), lb.setAttribute("fill", "#0a1710");
      return { g: bg, r: r, lb: lb, fl: fl, it: it };
    });
    var sl = null;
    if (v.seuil != null) {
      sl = O.sv("g", {}, g);
      O.sv("line", { x1: X(v.seuil), x2: X(v.seuil), y1: 14, y2: v.h - 24, stroke: O.C.or, "stroke-width": 3, "stroke-dasharray": "9 7" }, sl);
      O.etiquette(sl, X(v.seuil), v.h - 2, v.lseuil || ("seuil : " + v.seuil + (v.unite || "")), { fs: 22, c: O.C.or, fw: 700 });
    }
    return function (t, st) {
      bs.forEach(function (b, k) {
        var tk = O.et(v, String(k + 1), .4 + k * 1.1);
        O.op(b.g, O.E(O.P(t, tk, .5)));
        var p = O.EIO(O.P(t, tk + .2, 1.2));
        b.r.setAttribute("width", Math.max(0, (X(b.it.v) - x0) * p));
        O.op(b.lb, O.E(O.P(t, tk + 1.1, .5)));
        if (b.fl) O.op(b.fl, O.E(O.P(t, tk + 1.3, .5)));
      });
      if (sl) O.op(sl, O.E(O.P(t, O.et(v, "s", 1e9), .6)));
    };
  };

  /* ---------- lignée : transfert horizontal dans une cellule germinale, puis transmission verticale ---------- */
  // {id.1} le rétrovirus infecte une cellule germinale de l'ancêtre ; {id.2} son ADN s'intègre ; {id.3} la lignée se ramifie,
  // chaque espèce hérite du gène ; {id.4} les deux mots « horizontal » / « vertical »
  window.SERIE_ILLU.lignee = function (svg, v) {
    O = window.SERIE_OUTILS;
    var W = v.w, H = v.h, g = O.sv("g", {}, svg), ax = W * .5, ay = 120;
    var anc = O.sv("g", {}, g);
    O.sv("circle", { cx: ax, cy: ay, r: 56, fill: "rgba(127,190,203,.14)", stroke: "#7fbecb", "stroke-width": 3 }, anc);
    O.sv("circle", { cx: ax, cy: ay, r: 22, fill: "rgba(127,190,203,.25)", stroke: "#7fbecb", "stroke-width": 2 }, anc);
    O.sv("rect", { x: ax - 16, y: ay - 4, width: 32, height: 8, rx: 4, fill: "#b4cb9c" }, anc);
    var bande = O.sv("rect", { x: ax - 4, y: ay - 6, width: 8, height: 12, rx: 2, fill: "#ff6b5b" }, anc);
    bloc(anc, ax + 76, ay - 18, "cellule germinale d'un ancêtre des primates", { fs: 22, max: 300, fw: 600 });
    var vir = O.sv("g", {}, g);
    O.sv("circle", { r: 20, fill: "rgba(255,107,91,.18)", stroke: "#ff6b5b", "stroke-width": 3 }, vir);
    for (var i = 0; i < 8; i++) { var a = i * Math.PI / 4; O.sv("line", { x1: Math.cos(a) * 20, y1: Math.sin(a) * 20, x2: Math.cos(a) * 29, y2: Math.sin(a) * 29, stroke: "#ff6b5b", "stroke-width": 3, "stroke-linecap": "round" }, vir); }
    var lv = O.etiquette(g, ax - 330, ay - 50, "rétrovirus", { fs: 24, c: "#ff6b5b", fw: 700 });
    var mh = O.sv("g", {}, g);
    O.sv("path", { d: "M" + (ax - 300) + " " + (ay + 8) + " H" + (ax - 70), stroke: O.C.or, "stroke-width": 3, "stroke-dasharray": "8 6" }, mh);
    O.sv("path", { d: "M" + (ax - 82) + " " + (ay - 2) + " L" + (ax - 66) + " " + (ay + 8) + " L" + (ax - 82) + " " + (ay + 18), fill: "none", stroke: O.C.or, "stroke-width": 3 }, mh);
    O.etiquette(mh, ax - 185, ay - 14, "transfert horizontal", { fs: 24, c: O.C.or, fw: 700 });
    // arbre (topologie classique des hominoïdes)
    var esp = ["gibbon", "orang-outan", "gorille", "chimpanzé", "humain"], ly = H - 70, lx0 = W * .14, lx1 = W * .86;
    var feuilles = esp.map(function (n, i) { return lx0 + (lx1 - lx0) * i / (esp.length - 1); });
    var noeuds = [[ax, ay + 70]];
    var arbre = O.sv("g", {}, g), branches = [];
    function br(x1_, y1_, x2_, y2_) { var p = O.sv("path", { d: "M" + x1_ + " " + y1_ + " L" + x2_ + " " + y1_ + " L" + x2_ + " " + y2_, fill: "none", stroke: "#b4cb9c", "stroke-width": 4, "stroke-linecap": "round", "stroke-linejoin": "round" }, arbre); branches.push(p); return p; }
    var yA = ay + 70, yB = yA + 70, yC = yB + 60, yD = yC + 55;
    br(ax, yA, ax, yA);
    O.sv("line", { x1: ax, y1: ay + 56, x2: ax, y2: yA, stroke: "#b4cb9c", "stroke-width": 4 }, arbre);
    br(ax, yA, feuilles[0], ly); br(ax, yA, (feuilles[1] + feuilles[4]) / 2, yB);
    var xb = (feuilles[1] + feuilles[4]) / 2, xc = (feuilles[2] + feuilles[4]) / 2, xd = (feuilles[3] + feuilles[4]) / 2;
    br(xb, yB, feuilles[1], ly); br(xb, yB, xc, yC); br(xc, yC, feuilles[2], ly); br(xc, yC, xd, yD); br(xd, yD, feuilles[3], ly); br(xd, yD, feuilles[4], ly);
    var fg = esp.map(function (n, i) {
      var f = O.sv("g", {}, g), x = feuilles[i];
      O.sv("rect", { x: x - 30, y: ly + 6, width: 60, height: 12, rx: 6, fill: "#b4cb9c" }, f);
      O.sv("rect", { x: x - 4, y: ly + 4, width: 8, height: 16, rx: 2, fill: "#ff6b5b" }, f);
      O.etiquette(f, x, ly + 52, n, { fs: 24, fw: 600 });
      return f;
    });
    var mv = O.sv("g", {}, g);
    O.etiquette(mv, W * .9, ay + 150, "transmission", { fs: 24, c: O.C.sa, fw: 700, ancre: "end" });
    O.etiquette(mv, W * .9, ay + 180, "verticale", { fs: 24, c: O.C.sa, fw: 700, ancre: "end" });
    O.sv("path", { d: "M" + (W * .92) + " " + (ay + 110) + " V" + (ly - 20), stroke: O.C.sa, "stroke-width": 3, "stroke-dasharray": "8 6" }, mv);
    var leg = O.sv("g", {}, g);
    O.sv("rect", { x: 0, y: ly + 74, width: 18, height: 14, rx: 3, fill: "#ff6b5b" }, leg);
    O.etiquette(leg, 28, ly + 87, "le gène viral devenu gène de la syncytine 1", { fs: 20, ancre: "start", c: O.C.iv2 });
    return function (t, st) {
      var t2 = O.et(v, "2", 3), t3 = O.et(v, "3", 5), t4 = O.et(v, "4", 8);
      O.op(anc, O.E(O.P(st.tl, 0, .7)));
      var u = O.EIO(O.P(t, v.t0 + .8, Math.max(1.8, t2 - v.t0 - 1))), vx = ax - 330 + 290 * u, vy = ay + 10 - 10 * u;
      vir.setAttribute("transform", "translate(" + vx.toFixed(1) + "," + vy.toFixed(1) + ") scale(" + (1 - .5 * O.P(t, t2, .6)) + ")");
      O.op(vir, O.E(O.P(st.tl, .5, .6)) * (1 - O.E(O.P(t, t2, .6))));
      O.op(lv, O.E(O.P(st.tl, .5, .6)) * (1 - O.E(O.P(t, t2, .6))));
      O.op(bande, O.E(O.P(t, t2, .5)));
      O.op(mh, O.E(O.P(t, t4, .6)));
      branches.forEach(function (b, i) { O.trace(b, O.P(t, t3 + i * .18, .9)); });
      fg.forEach(function (f, i) { apparait(f, O.E(O.P(t, t3 + 1 + i * .2, .6)), 10); });
      O.op(mv, O.E(O.P(t, t4 + .6, .6)));
      O.op(leg, O.E(O.P(t, t3 + 2, .6)));
    };
  };

  // contournements : le générique du moteur SVT (copié du moteur PC) écrit « Physique-chimie · Terminale » en tête
  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".g-haut"), function (e) { e.textContent = "SVT · Terminale"; });
    // l'étiquette du niveau « bac » du moteur est numérotée « Exercice 3 » (vidéos PC à trois exercices) : ici, un seul exercice
    Array.prototype.forEach.call(document.querySelectorAll(".ex-nv"), function (e) { e.textContent = e.textContent.replace(/^Exercice \d+ · /i, "Exercice · "); });
  });
})();
