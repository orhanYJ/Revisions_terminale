/* Vidéo HLP, entrée I (« Éducation, transmission et émancipation ») : illustrations propres à l'entrée, gravées à l'encre.
   Chargé par hlp/serie/hlp-e1.html après moteur.js (generer.py l'ajoute s'il existe). Chaque illustration :
   SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; } ; rendu fonction pure du temps
   (t : temps de la vidéo, st.tl : temps depuis l'apparition) ; étapes calées sur la voix par les repères {id.k}.
   Les étiquettes (lbl) s'écrivent d'elles-mêmes quand leur opacité monte (voir TYPES.illu du moteur). */
(function () {
  "use strict";
  var O, C, sv, P, E, EIO, EB, op, tr, et, lbl, trace, cl;
  function prep() {
    if (O) return;
    O = window.SERIE_OUTILS; C = O.C; sv = O.sv; P = O.P; E = O.E; EIO = O.EIO; EB = O.EB; op = O.op; tr = O.tr; et = O.et;
    lbl = O.lbl; trace = O.trace; cl = O.cl;
  }
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var SERIE_ILLU = window.SERIE_ILLU;

  // trait d'encre (chemin SVG) ; renvoie l'élément, à tracer avec trace(el, u)
  function encre(g, d, opt) {
    opt = opt || {};
    return sv("path", { d: d, fill: opt.f || "none", stroke: opt.c || C.iv, "stroke-width": opt.ep || 2.6, "stroke-linecap": "round", "stroke-linejoin": "round", opacity: opt.o == null ? 1 : opt.o }, g);
  }
  // étiquette qui apparaît (et s'écrit) à l'instant t0
  function montre(l, t, t0, d) { op(l, E(P(t, t0, d || .5))); }
  // cellule de texte qui revient à la ligne (largeur fixe)
  function bloc(s, x, y, w, html, cls) {
    var d = lbl(s, x, y, html, "lg " + (cls || ""));
    d.style.whiteSpace = "normal"; d.style.width = w + "px"; d.style.lineHeight = "1.2";
    return d;
  }

  /* balance : Montaigne, « la tête bien faite plutôt que bien pleine ». {id.1} la tête bien faite (former le jugement) ;
     {id.2} la tête bien pleine (remplir la mémoire) ; {id.3} la balance se dessine et penche du côté du jugement,
     « plutôt… que » ; {id.4} la glose en marge (l'étamine du jugement). */
  SERIE_ILLU.balance = function (s, v) {
    prep();
    var W_ = v.w, g = sv("g", {}, s);
    var la = lbl(s, 200, 0, "tête bien faite", "sc r g"), a1 = lbl(s, 200, 52, "former", "tt"), a2 = lbl(s, 200, 104, "le jugement", "tt");
    var ap = lbl(s, 316, 96, "a", "r p");
    var lb = lbl(s, W_ - 220, 0, "tête bien pleine", "sc r g"), b1 = lbl(s, W_ - 220, 52, "remplir", "tt"), b2 = lbl(s, W_ - 220, 104, "la mémoire", "tt");
    b1.style.color = b2.style.color = "#7a644e";
    var cx = 470, py = 250, L_ = 175;
    var base = encre(g, "M" + (cx - 70) + " 500 H" + (cx + 70) + " M" + (cx - 46) + " 500 Q" + cx + " 470 " + (cx + 46) + " 500");
    var mat = encre(g, "M" + cx + " " + (py + 8) + " V492");
    var piv = sv("circle", { cx: cx, cy: py, r: 8, fill: "none", stroke: C.iv, "stroke-width": 2.6 }, g);
    var fl = sv("g", {}, g), fleau = encre(fl, "M" + (cx - L_) + " " + py + " H" + (cx + L_));
    function plateau(nom) {
      var p = sv("g", {}, g);
      return { g: p, fils: encre(p, "M0 0 L-38 78 M0 0 L38 78"), bol: encre(p, "M-48 78 Q0 112 48 78 Z", { f: "rgba(156,42,27,.08)" }) };
    }
    var pg = plateau("g"), pd = plateau("d");
    var lg_ = lbl(s, cx - L_, py + 120, "jugement", "it r"), ld = lbl(s, cx + L_, py + 120, "mémoire", "it");
    var plq = lbl(s, cx, py - 92, "plutôt… que", "it g");
    var gl = [lbl(s, W_ - 150, 300, "a. faire passer", "it"), lbl(s, W_ - 150, 340, "les idées des livres", "it"),
      lbl(s, W_ - 150, 380, "par l'*étamine*", "it"), lbl(s, W_ - 150, 420, "(le tamis)", "it"), lbl(s, W_ - 150, 460, "du jugement.", "it")];
    gl.forEach(function (x) { x.style.color = "#5b3a20"; });
    gl[0].innerHTML = '<span style="color:#9c2a1b;font-style:normal">a.</span> faire passer';
    var traits = [base, mat, fleau, pg.fils, pg.bol, pd.fils, pd.bol];
    return function (t, st) {
      var t1 = et(v, "1", .2), t2 = et(v, "2", 1.4), t3 = et(v, "3", 2.6), t4 = et(v, "4", 5);
      montre(la, t, t1); montre(a1, t, t1 + .15); montre(a2, t, t1 + .35);
      montre(lb, t, t2); montre(b1, t, t2 + .15); montre(b2, t, t2 + .35);
      traits.forEach(function (x, i) { trace(x, EIO(P(t, t3 + i * .08, .55))); });
      op(piv, E(P(t, t3, .3)));
      var sx = Math.max(0, t - t3 - .9), ang = t < t3 + .9 ? 0 : -10 * (1 - Math.exp(-2.4 * sx) * Math.cos(5 * sx));
      fl.setAttribute("transform", "rotate(" + ang.toFixed(3) + " " + cx + " " + py + ")");
      var c = Math.cos(ang * Math.PI / 180), sn = Math.sin(ang * Math.PI / 180);
      pg.g.setAttribute("transform", "translate(" + (cx - L_ * c).toFixed(2) + " " + (py - L_ * sn).toFixed(2) + ")");
      pd.g.setAttribute("transform", "translate(" + (cx + L_ * c).toFixed(2) + " " + (py + L_ * sn).toFixed(2) + ")");
      lg_.style.top = (py - L_ * sn + 120).toFixed(1) + "px"; ld.style.top = (py + L_ * sn + 120).toFixed(1) + "px";
      montre(lg_, t, t3 + .8); montre(ld, t, t3 + .9); montre(plq, t, t3 + 1.2);
      montre(ap, t, t4);
      gl.forEach(function (x, i) { montre(x, t, t4 + .2 + i * .3, .45); });
    };
  };

  /* maîtres : les trois maîtres de l'Émile (livre I). {id.1} {id.2} {id.3} la nature, les hommes, les choses ;
     {id.4} l'élève au croisement ; {id.5} l'accord des trois ; {id.6} seule l'éducation des hommes dépend de nous, mais on règle les deux autres sur la nature. */
  SERIE_ILLU.maitres = function (s, v) {
    prep();
    var g = sv("g", {}, s), X = [130, 470, 810], noms = ["La nature", "Les hommes", "Les choses"],
      sous = ["le développement des organes", "l'usage qu'on nous apprend", "l'expérience des objets"];
    var bx = X.map(function (x, i) {
      var r = encre(g, "M" + (x - 150) + " 20 H" + (x + 150) + " V126 H" + (x - 150) + " Z", { c: i === 1 ? C.sa : C.iv, ep: i === 1 ? 3 : 2.2 });
      return { r: r, n: lbl(s, x, 34, noms[i], "tt"), q: lbl(s, x, 88, sous[i], "it p") };
    });
    var ti = lbl(s, 470, -64, "Les trois maîtres de l'*Émile*", "titre");
    var cy = 300, cxe = 470;
    var fils = [encre(g, "M130 128 C130 220 380 230 440 280"), encre(g, "M470 128 V270", { c: C.sa, ep: 3 }), encre(g, "M810 128 C810 220 560 230 500 280")];
    var el = sv("circle", { cx: cxe, cy: cy, r: 50, fill: "rgba(156,42,27,.1)", stroke: C.sa, "stroke-width": 2.6 }, g);
    var le = lbl(s, cxe, cy - 20, "l'élève", "it r");
    var fl = encre(g, "M" + (cxe + 56) + " " + cy + " H640");
    var pt = encre(g, "M626 " + (cy - 10) + " L642 " + cy + " L626 " + (cy + 10));
    var ac = lbl(s, 660, cy - 44, "l'accord des trois :", "lg it"), ac2 = lbl(s, 660, cy - 4, "un homme « bien élevé »", "lg it r");
    var nb = bloc(s, 100, 400, 740, "Seule l'éducation des hommes dépend vraiment de nous ; mais c'est sur celle de la nature qu'il faut régler les deux autres.", "it");
    nb.style.textAlign = "center"; nb.style.fontSize = "30px";
    return function (t, st) {
      montre(ti, t, v.t0 + .2);
      bx.forEach(function (b, i) {
        var tk = et(v, String(i + 1), .3 + i * .8);
        trace(b.r, EIO(P(t, tk, .6))); montre(b.n, t, tk + .2); montre(b.q, t, tk + .5);
      });
      var t4 = et(v, "4", 3);
      fils.forEach(function (f, i) { trace(f, EIO(P(t, t4 + i * .12, .6))); });
      op(el, E(P(t, t4 + .4, .4))); montre(le, t, t4 + .5);
      var t5 = et(v, "5", 4.5);
      trace(fl, EIO(P(t, t5, .5))); trace(pt, P(t, t5 + .45, .2)); montre(ac, t, t5 + .4); montre(ac2, t, t5 + .7);
      montre(nb, t, et(v, "6", 6), .6);
    };
  };

  // un arbuste gravé : tronc et ramure ; flex (radians) le plie, h (0 à 1) le fait pousser
  function arbuste(g, x, y, ht) {
    var gr = sv("g", {}, g);
    var tronc = encre(gr, "", { ep: 3.2 }), b1 = encre(gr, "", { ep: 2.2 }), b2 = encre(gr, "", { ep: 2.2 }),
      cime = sv("path", { d: "", fill: "rgba(61,107,58,.16)", stroke: C.vert, "stroke-width": 2.2, "stroke-linejoin": "round" }, gr);
    function pose(flex, h) {
      h = h == null ? 1 : h;
      var H_ = ht * (.45 + .55 * h), n = 8, pts = [], xx = x, yy = y, a = -Math.PI / 2;
      for (var i = 0; i <= n; i++) { pts.push([xx, yy]); a += flex / n; xx += Math.cos(a) * H_ / n; yy += Math.sin(a) * H_ / n; }
      var d = "M" + pts.map(function (p) { return p[0].toFixed(1) + " " + p[1].toFixed(1); }).join(" L");
      tronc.setAttribute("d", d);
      var m = pts[4], m2 = pts[6], top = pts[n], ang = a;
      b1.setAttribute("d", "M" + m[0].toFixed(1) + " " + m[1].toFixed(1) + " q" + (-18 * h - 6) + " " + (-10) + " " + (-26 * h - 10) + " " + (-30 * h - 6));
      b2.setAttribute("d", "M" + m2[0].toFixed(1) + " " + m2[1].toFixed(1) + " q" + (16 * h + 6) + " " + (-8) + " " + (22 * h + 8) + " " + (-26 * h - 6));
      var r = 18 + 22 * h, cxx = top[0] + Math.cos(ang) * r * .4, cyy = top[1] + Math.sin(ang) * r * .4, dd = "";
      for (var k = 0; k <= 10; k++) {
        var u = k / 10 * Math.PI * 2, rr = r * (1 + .16 * Math.sin(u * 5));
        dd += (k ? " L" : "M") + (cxx + Math.cos(u) * rr).toFixed(1) + " " + (cyy + Math.sin(u) * rr * .8).toFixed(1);
      }
      cime.setAttribute("d", dd + " Z");
    }
    return { g: gr, pose: pose };
  }
  /* arbrisseau : Rousseau, livre I. {id.1} dresser (l'arbre « contourné à sa mode », lié à son treillage) ;
     {id.2} abandonner (l'arbrisseau au milieu du chemin, heurté par les passants) ; {id.3} cultiver (une enceinte, l'arbre
     pousse droit) ; v.titres = trois titres, v.legs = trois légendes. */
  SERIE_ILLU.arbrisseau = function (s, v) {
    prep();
    var g = sv("g", {}, s), X = [160, 490, 820], sol = 400;
    var tit = (v.titres || ["Dresser", "Abandonner", "Cultiver"]).map(function (x, i) { return lbl(s, X[i], 0, x, "tt" + (i === 2 ? " r" : "")); });
    var leg = (v.legs || ["", "", ""]).map(function (x, i) { var b = bloc(s, X[i] - 150, sol + 30, 300, x, "it"); b.style.textAlign = "center"; return b; });
    var sols = X.map(function (x) { return encre(g, "M" + (x - 130) + " " + sol + " H" + (x + 130), { ep: 2 }); });
    // 1. le treillage et l'arbre plié
    var treil = encre(g, "M" + (X[0] - 70) + " " + sol + " V180 M" + (X[0] + 70) + " " + sol + " V180 M" + (X[0] - 90) + " 230 H" + (X[0] + 90) + " M" + (X[0] - 90) + " 300 H" + (X[0] + 90), { c: "#7a5a3a", ep: 2 });
    var a1 = arbuste(g, X[0], sol, 210);
    var liens = encre(g, "M" + (X[0] - 60) + " 300 l12 8 M" + (X[0] + 40) + " 230 l12 8", { c: C.sa, ep: 3 });
    // 2. le chemin, l'arbrisseau, les pas des passants
    var chemin = encre(g, "M" + (X[1] - 120) + " " + (sol + 2) + " L" + (X[1] - 40) + " 230 M" + (X[1] + 120) + " " + (sol + 2) + " L" + (X[1] + 40) + " 230", { c: "#7a5a3a", ep: 2 });
    var a2 = arbuste(g, X[1], sol - 20, 170);
    var pas = [-1, 1, -1, 1].map(function (c, i) { return encre(g, "M" + (X[1] + c * 90) + " " + (sol - 70 - i * 30) + " l" + (-c * 34) + " 6", { c: C.sa, ep: 3 }); });
    // 3. l'enceinte et l'arbre qui pousse droit
    var enc = encre(g, "M" + (X[2] - 80) + " " + sol + " V320 M" + (X[2] - 50) + " " + sol + " V315 M" + (X[2] - 20) + " " + sol + " V320 M" + (X[2] + 20) + " " + sol + " V320 M" + (X[2] + 50) + " " + sol + " V315 M" + (X[2] + 80) + " " + sol + " V320 M" + (X[2] - 88) + " 345 H" + (X[2] + 88), { c: "#7a5a3a", ep: 2.4 });
    var a3 = arbuste(g, X[2], sol, 230);
    return function (t, st) {
      var t1 = et(v, "1", .3), t2 = et(v, "2", 2.5), t3 = et(v, "3", 4.5);
      [t1, t2, t3].forEach(function (tk, i) { montre(tit[i], t, tk); trace(sols[i], EIO(P(t, tk, .5))); montre(leg[i], t, tk + 1, .6); });
      trace(treil, EIO(P(t, t1 + .2, .7))); op(a1.g, E(P(t, t1 + .5, .5)));
      a1.pose(1.25 * E(P(t, t1 + .7, 1.2)), 1); trace(liens, P(t, t1 + 1.6, .4));
      trace(chemin, EIO(P(t, t2 + .2, .6))); op(a2.g, E(P(t, t2 + .5, .4)));
      var hit = 0;
      pas.forEach(function (p, i) { var tk = t2 + 1 + i * .55; trace(p, P(t, tk, .2)); op(p, 1 - P(t, tk + .5, .5) * .6); hit += (i % 2 ? -1 : 1) * Math.exp(-Math.max(0, t - tk) * 3) * (t >= tk ? 1 : 0); });
      a2.pose(.9 * hit + (t > t2 + 1 ? .45 : 0), .5);
      trace(enc, EIO(P(t, t3 + .2, .7))); op(a3.g, E(P(t, t3 + .5, .4)));
      a3.pose(.04 * Math.sin(t * 1.2), .2 + .8 * EIO(P(t, t3 + .8, 2.4)));
    };
  };

  // silhouette gravée : assise (k = 0) ou debout (k = 1), en (x, y) = pieds
  function silhouette(g, col) {
    var gr = sv("g", {}, g), tete = sv("circle", { r: 17, fill: "none", stroke: col, "stroke-width": 3 }, gr), corps = encre(gr, "", { c: col, ep: 3.4 });
    return { g: gr, pose: function (x, y, k) {
      function m(a, b) { return a + (b - a) * k; }
      var hanche = [x, m(y - 52, y - 92)], cou = [x, m(y - 112, y - 162)], genou = [m(x + 40, x + 2), m(y - 54, y - 46)], pied = [m(x + 40, x + 8), y],
        genou2 = [m(x + 36, x - 8), m(y - 52, y - 46)], pied2 = [m(x + 32, x - 14), y], main = [m(x + 34, x + 30), m(y - 76, y - 110)], main2 = [m(x + 26, x - 26), m(y - 70, y - 104)];
      tete.setAttribute("cx", cou[0]); tete.setAttribute("cy", cou[1] - 20);
      gr.setAttribute("transform", "translate(" + x + " " + y + ") scale(1.4) translate(" + (-x) + " " + (-y) + ")");
      function f(p) { return p[0].toFixed(1) + " " + p[1].toFixed(1); }
      corps.setAttribute("d", "M" + f(cou) + " L" + f(hanche) + " L" + f(genou) + " L" + f(pied) + " M" + f(hanche) + " L" + f(genou2) + " L" + f(pied2) +
        " M" + f([cou[0], cou[1] + 14]) + " L" + f(main) + " M" + f([cou[0], cou[1] + 14]) + " L" + f(main2));
    } };
  }
  /* minorité : Kant, « Qu'est-ce que les Lumières ? ». Un homme assis, tenu par trois tuteurs (fils pointillés) :
     {id.1} un livre, {id.2} un directeur, {id.3} un médecin ; {id.4} « minorité : paresse et lâcheté » ;
     {id.5} Sapere aude : les fils se rompent, il se lève et avance. */
  SERIE_ILLU.minorite = function (s, v) {
    prep();
    var g = sv("g", {}, s), cx = 470, sol = 420;
    var tut = [[150, 70, "un livre", "qui a de l'esprit pour moi"], [470, 0, "un directeur", "qui a de la conscience pour moi"], [800, 70, "un médecin", "qui juge pour moi du régime"]];
    var T_ = tut.map(function (u) {
      var c = lbl(s, u[0], u[1], u[2], "sc r g"), q = lbl(s, u[0], u[1] + 44, u[3], "it p");
      var f = sv("path", { d: "M" + u[0] + " " + (u[1] + 84) + " Q" + ((u[0] + cx) / 2) + " " + (u[1] + 200) + " " + (cx - 4) + " " + (sol - 158), fill: "none", stroke: C.iv, "stroke-width": 2, "stroke-dasharray": "3 7", "stroke-linecap": "round" }, g);
      return { c: c, q: q, f: f };
    });
    var banc = encre(g, "M" + (cx - 62) + " " + (sol - 72) + " H" + (cx + 40) + " M" + (cx - 55) + " " + (sol - 72) + " V" + sol + " M" + (cx + 33) + " " + (sol - 72) + " V" + sol, { c: "#7a5a3a", ep: 3.4 });
    var solL = encre(g, "M60 " + sol + " H920", { ep: 1.6, o: .6 });
    var p = silhouette(g, C.iv);
    var mi = lbl(s, cx, sol + 20, "minorité : paresse et lâcheté", "it r");
    var ma = lbl(s, 640, sol + 20, "penser par soi-même", "it r");
    var sa = lbl(s, 470, 150, "*Sapere aude !*", "ban");
    return function (t, st) {
      trace(solL, EIO(P(st.tl, 0, .6)));
      trace(banc, EIO(P(t, v.t0 + .1, .5)));
      var t4 = et(v, "4", 4), t5 = et(v, "5", 6);
      T_.forEach(function (x, i) {
        var tk = et(v, String(i + 1), .6 + i * .9);
        montre(x.c, t, tk); montre(x.q, t, tk + .3);
        var a = E(P(t, tk + .2, .6)), rompu = P(t, t5 + .3 + i * .12, .5);
        op(x.f, a * (1 - rompu));
        x.f.setAttribute("stroke-dashoffset", (-12 * t).toFixed(1));
        tr(x.f, "translate(0," + (24 * rompu * rompu).toFixed(1) + "px)");
      });
      montre(mi, t, t4); op(mi, E(P(t, t4, .5)) * (1 - E(P(t, t5 + .6, .5))));
      var lev = EIO(P(t, t5 + .6, 1)), va = EIO(P(t, t5 + 1.6, 2));
      op(p.g, E(P(t, v.t0 + .3, .5)));
      p.pose(cx - 10 + 170 * va + (lev < 1 && lev > 0 ? 0 : 0), sol, lev);
      op(sa, E(P(t, t5, .4)) * (1 - E(P(t, t5 + 2.8, .6))));
      tr(sa, "translate(-50%,0) scale(" + (1.25 - .25 * EB(P(t, t5, .5))).toFixed(3) + ")");
      montre(ma, t, t5 + 2.4);
    };
  };

  /* jalons : une frise de dates à l'encre. v.de, v.a : bornes (années) ; v.items = [[année, titre, précision], …] ;
     l'item k au repère {id.k} ; au-dessus et au-dessous de l'axe en alternance (v.haut = indices forcés au-dessus). */
  SERIE_ILLU.jalons = function (s, v) {
    prep();
    var g = sv("g", {}, s), W_ = v.w, y0 = Math.round(v.h / 2), x0 = 40, x1 = W_ - 40;
    function X(a) {
      if (v.regulier) { var k = v.items.map(function (it) { return it[0]; }).indexOf(a); return x0 + 90 + k * (x1 - x0 - 180) / Math.max(1, v.items.length - 1); }
      return x0 + (a - v.de) / (v.a - v.de) * (x1 - x0);
    }
    var axe = encre(g, "M" + x0 + " " + y0 + " H" + x1, { c: C.sa, ep: 2.6 }), axe2 = encre(g, "M" + x0 + " " + (y0 + 5) + " H" + x1, { c: C.sa, ep: 1 });
    var its = v.items.map(function (it, i) {
      var x = X(it[0]), haut = v.cote ? v.cote[i] > 0 : i % 2 === 0, dy = haut ? -1 : 1;
      var tige = encre(g, "M" + x + " " + y0 + " V" + (y0 + dy * 46), { ep: 1.6 });
      var pt = sv("circle", { cx: x, cy: y0 + 2, r: 6, fill: C.sa }, g);
      var an = lbl(s, x, haut ? y0 - 92 : y0 + 52, String(it[3] || it[0]), "r g");
      var ti = lbl(s, x, haut ? y0 - 146 : y0 + 96, it[1], "");
      var pr = it[2] ? lbl(s, x, haut ? y0 - 186 : y0 + 136, it[2], "it p") : null;
      if (!haut && pr) pr.style.top = (y0 + 136) + "px";
      if (haut && pr) { ti.style.top = (y0 - 186) + "px"; pr.style.top = (y0 - 146) + "px"; }
      return { tige: tige, pt: pt, an: an, ti: ti, pr: pr };
    });
    return function (t, st) {
      trace(axe, EIO(P(st.tl, 0, .9))); trace(axe2, EIO(P(st.tl, .1, .9)));
      its.forEach(function (x, i) {
        var tk = et(v, String(i + 1), .8 + i * .6);
        trace(x.tige, P(t, tk, .25)); op(x.pt, E(P(t, tk, .3)));
        montre(x.an, t, tk + .1); montre(x.ti, t, tk + .25); if (x.pr) montre(x.pr, t, tk + .45);
      });
    };
  };

  /* courbes : le roman d'apprentissage. {id.1} le modèle : le héros se forme (courbe qui monte : Goethe, Stendhal) ;
     {id.2} Flaubert : le chemin erre et revient à son point de départ ; {id.3} « C'est là ce que nous avons eu de meilleur ! » */
  SERIE_ILLU.courbes = function (s, v) {
    prep();
    var g = sv("g", {}, s), y0 = 420;
    var ax = encre(g, "M60 " + y0 + " H930", { ep: 1.6, o: .7 }), axp = encre(g, "M918 " + (y0 - 8) + " L932 " + y0 + " L918 " + (y0 + 8), { ep: 1.6, o: .7 });
    var lx = lbl(s, 880, y0 + 12, "le temps du roman", "it p");
    var monte = encre(g, "M80 " + (y0 - 20) + " C260 " + (y0 - 30) + " 380 " + (y0 - 140) + " 520 " + (y0 - 220) + " S760 " + (y0 - 330) + " 880 " + (y0 - 350), { c: C.vert, ep: 3.4 });
    var mp = encre(g, "M862 " + (y0 - 356) + " L884 " + (y0 - 351) + " L870 " + (y0 - 334), { c: C.vert, ep: 3.4 });
    var l1 = lbl(s, 560, y0 - 410, "le modèle : on se forme au contact du monde", "it");
    var l1b = lbl(s, 560, y0 - 372, "Goethe (1795-1796), Stendhal (1830)", "p");
    l1.style.color = l1b.style.color = C.vert;
    var erre = encre(g, "M110 " + (y0 - 60) + " C200 " + (y0 - 180) + " 330 " + (y0 - 120) + " 380 " + (y0 - 190) + " S520 " + (y0 - 60) + " 600 " + (y0 - 140) +
      " S760 " + (y0 - 40) + " 640 " + (y0 + 10) + " S300 " + (y0 - 10) + " 130 " + (y0 - 52), { c: C.sa, ep: 3.4 });
    var d0 = sv("circle", { cx: 110, cy: y0 - 60, r: 8, fill: C.sa }, g);
    var l2 = lbl(s, 300, y0 - 260, "Flaubert (1869) : on ne devient rien", "it r");
    var c1 = lbl(s, 60, y0 + 24, "au début : « Ce fut comme une apparition »", "lg it p");
    var c2 = lbl(s, 60, y0 + 60, "à la fin : « C'est là ce que nous avons eu de meilleur ! »", "lg it p r");
    return function (t, st) {
      trace(ax, EIO(P(st.tl, 0, .7))); trace(axp, P(st.tl, .6, .2)); montre(lx, t, v.t0 + .6);
      var t1 = et(v, "1", .5), t2 = et(v, "2", 3), t3 = et(v, "3", 6);
      trace(monte, EIO(P(t, t1, 1.6))); trace(mp, P(t, t1 + 1.5, .2)); montre(l1, t, t1 + .9); montre(l1b, t, t1 + 1.2);
      var dim = 1 - .55 * E(P(t, t2, .5));
      op(monte, dim); op(mp, dim); op(l1, l1.style.opacity * dim); op(l1b, l1b.style.opacity * dim);
      op(d0, E(P(t, t2, .3))); montre(c1, t, t2 + .2);
      trace(erre, EIO(P(t, t2 + .4, 2.6))); montre(l2, t, t2 + .8);
      montre(c2, t, t3);
    };
  };

  /* épreuve : un texte, deux questions, deux copies. {id.1} le texte ; {id.2} la question 1, l'interprétation ;
     {id.3} la question 2, l'essai ; {id.4} si l'une est littéraire, l'autre est philosophique ; {id.5} 4 heures. */
  SERIE_ILLU.epreuve = function (s, v) {
    prep();
    var g = sv("g", {}, s);
    function feuille(x, y, w, hh, col) {
      var r = encre(g, "M" + x + " " + y + " H" + (x + w) + " V" + (y + hh) + " H" + x + " Z", { c: col || C.iv, ep: 2.4, f: "rgba(255,250,236,.55)" });
      var ls = [];
      for (var yy = y + 26; yy < y + hh - 16; yy += 18) ls.push(encre(g, "M" + (x + 16) + " " + yy + " H" + (x + w - 16 - ((yy * 7) % 40)), { ep: 1.4, o: .45 }));
      return { r: r, ls: ls };
    }
    var tx = feuille(40, 130, 180, 250), ltx = lbl(s, 130, 396, "un texte", "tt");
    var f1 = feuille(330, 20, 150, 190, C.sa), f2 = feuille(330, 290, 150, 190, C.bleu);
    var fl1 = encre(g, "M230 220 C280 190 290 120 322 115"), fl2 = encre(g, "M230 290 C280 320 290 380 322 385");
    var q1 = [lbl(s, 510, 40, "Question 1 · l'interprétation", "lg sc r"), lbl(s, 510, 86, "littéraire *ou* philosophique", "lg it"), lbl(s, 510, 128, "sur 10 points", "lg")];
    var q2 = [lbl(s, 510, 310, "Question 2 · l'essai", "lg sc"), lbl(s, 510, 356, "philosophique *ou* littéraire", "lg it"), lbl(s, 510, 398, "sur 10 points", "lg")];
    q2[0].style.color = C.bleu;
    var croix = encre(g, "M405 222 C385 240 385 262 405 280", { c: C.sa, ep: 2.6 }), cp1 = encre(g, "M398 232 L406 220 L414 232", { c: C.sa, ep: 2.6 }), cp2 = encre(g, "M398 270 L406 282 L414 270", { c: C.sa, ep: 2.6 });
    var lc = lbl(s, 510, 232, "si l'une est littéraire, l'autre est philosophique", "lg it r p");
    var hr = lbl(s, 130, 450, "4 heures · deux copies", "it");
    return function (t, st) {
      var t1 = et(v, "1", .3), t2 = et(v, "2", 1.5), t3 = et(v, "3", 2.8), t4 = et(v, "4", 4.2), t5 = et(v, "5", 5.6);
      trace(tx.r, EIO(P(t, t1, .5))); tx.ls.forEach(function (l, i) { trace(l, P(t, t1 + .3 + i * .05, .25)); }); montre(ltx, t, t1 + .4);
      trace(fl1, EIO(P(t, t2, .5))); trace(f1.r, EIO(P(t, t2 + .3, .5))); f1.ls.forEach(function (l, i) { trace(l, P(t, t2 + .5 + i * .04, .2)); });
      q1.forEach(function (x, i) { montre(x, t, t2 + .5 + i * .35); });
      trace(fl2, EIO(P(t, t3, .5))); trace(f2.r, EIO(P(t, t3 + .3, .5))); f2.ls.forEach(function (l, i) { trace(l, P(t, t3 + .5 + i * .04, .2)); });
      q2.forEach(function (x, i) { montre(x, t, t3 + .5 + i * .35); });
      trace(croix, EIO(P(t, t4, .5))); trace(cp1, P(t, t4 + .45, .2)); trace(cp2, P(t, t4 + .45, .2)); montre(lc, t, t4 + .3);
      montre(hr, t, t5);
    };
  };

  /* brouillon : le tableau du brouillon de l'interprétation (citation · ce que je remarque · ce que ça signifie).
     v.lignes = [[citation, remarque, sens], …] remplies aux repères {id.k} ; {id.g} : on regroupe en idées. */
  SERIE_ILLU.brouillon = function (s, v) {
    prep();
    var g = sv("g", {}, s), CX = [0, Math.round(v.w * .32), Math.round(v.w * .66), v.w], HY = 56, RH = v.rh || 112;
    var nl = v.lignes.length, Hh = HY + nl * RH;
    var cad = encre(g, "M0 0 H" + v.w + " V" + Hh + " H0 Z", { ep: 2.2 }), cols = [encre(g, "M" + CX[1] + " 0 V" + Hh, { ep: 1.4 }), encre(g, "M" + CX[2] + " 0 V" + Hh, { ep: 1.4 })];
    var hl = encre(g, "M0 " + HY + " H" + v.w, { c: C.sa, ep: 2.2 });
    var tetes = ["citation (ligne)", "ce que je remarque", "ce que ça signifie"].map(function (x, i) { return lbl(s, (CX[i] + CX[i + 1]) / 2, 14, x, "sc r p"); });
    var rows = v.lignes.map(function (l, k) {
      var y = HY + k * RH, sep = k ? encre(g, "M0 " + y + " H" + v.w, { ep: 1, o: .5 }) : null;
      var cs = l.map(function (txt, i) { var b = bloc(s, CX[i] + 14, y + 10, CX[i + 1] - CX[i] - 28, txt, i === 0 ? "it p" : "p"); return b; });
      cs[0].style.fontSize = cs[1].style.fontSize = cs[2].style.fontSize = (v.taille || 25) + "px";
      return { sep: sep, cs: cs };
    });
    var acc = encre(g, "M" + (v.w + 14) + " " + (HY + 6) + " q14 0 14 14 V" + (Hh / 2 + 10) + " q0 12 12 12 q-12 0 -12 12 V" + (Hh - 20) + " q0 14 -14 14", { c: C.sa, ep: 2.6 });
    var lg = bloc(s, v.w + 50, Hh / 2 - 26, 150, "deux ou trois idées : tes parties", "it r");
    return function (t, st) {
      trace(cad, EIO(P(st.tl, 0, .8))); cols.forEach(function (c) { trace(c, EIO(P(st.tl, .3, .6))); }); trace(hl, EIO(P(st.tl, .4, .5)));
      tetes.forEach(function (x, i) { montre(x, t, v.t0 + .5 + i * .2); });
      rows.forEach(function (r, k) {
        var tk = et(v, String(k + 1), 1.4 + k * 1.6);
        if (r.sep) trace(r.sep, EIO(P(t, tk - .2, .4)));
        r.cs.forEach(function (c, i) { montre(c, t, tk + i * .7, .5); });
      });
      var tg = et(v, "g", 1e9);
      trace(acc, EIO(P(t, tg, .7))); montre(lg, t, tg + .4);
    };
  };
})();
