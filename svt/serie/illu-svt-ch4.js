/* Vidéo du chapitre 4 de SVT (« Mécanismes de diversité non génétique du vivant ») : illustrations propres au chapitre.
   Chargé par svt/serie/svt-ch4.html (generer.py l'ajoute s'il existe). Chaque illustration : SERIE_ILLU.nom = function (svg, v)
   { … return function (t, st) { … }; } ; rendu fonction pure du temps (t : temps de la vidéo, st.tl : temps depuis l'apparition).
   Étapes calées sur la voix par les repères {id.k} (O.et(v, "k", repli)). Schémas simplifiés, faits pour la vidéo. */
(function () {
  "use strict";
  // ce fichier est chargé avant moteur.js : les outils (window.SERIE_OUTILS) ne sont lus qu'au premier dessin
  var O, C, sv, P, E, EIO, EB, op, trace, et, alea;
  function prep() {
    if (O) return;
    O = window.SERIE_OUTILS; C = O.C; sv = O.sv; P = O.P; E = O.E; EIO = O.EIO; EB = O.EB; op = O.op; trace = O.trace; et = O.et; alea = O.alea;
  }
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var SERIE_ILLU = window.SERIE_ILLU;
  var VERT_ALGUE = "#6fd17a", PEAU = "rgba(231,242,218,.16)";

  function txt(g, x, y, s, o) { o = o || {}; return O.etiquette(g, x, y, s, { fs: o.fs || 24, c: o.c || C.iv, fw: o.fw || 600, ancre: o.ancre, cls: o.cls || "" }); }
  function apparait(e, t, t0, d) { var p = E(P(t, t0, d || .6)); op(e, p); return p; }
  function decale(e, p, dy) { e.setAttribute("transform", "translate(0," + ((1 - p) * (dy || 14)).toFixed(1) + ")"); }
  // flèche courbe qui se trace (chemin + pointe), pour les cycles et les échanges
  function fleche(g, d, col, ep) {
    var p = sv("path", { d: d, fill: "none", stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round" }, g);
    var tri = sv("path", { d: "", fill: col }, g), fait = false;
    function pointe() {
      if (fait) return;
      var L = p.getTotalLength(); if (!L) return;
      var a = p.getPointAtLength(L), b = p.getPointAtLength(Math.max(0, L - 4)), ux = a.x - b.x, uy = a.y - b.y, n = Math.hypot(ux, uy) || 1;
      ux /= n; uy /= n; var px = -uy, py = ux, k = 16, l = 8;
      tri.setAttribute("d", "M" + (a.x + ux * 4) + " " + (a.y + uy * 4) + " L" + (a.x - ux * k + px * l) + " " + (a.y - uy * k + py * l) +
        " L" + (a.x - ux * k - px * l) + " " + (a.y - uy * k - py * l) + " Z");
      fait = true;
    }
    return function (q) { pointe(); trace(p, q); op(tri, q > .97 ? 1 : 0); };
  }
  // ver plat (ver de Roscoff) centré en (x, y), longueur L
  function ver(g, x, y, L, remplissage) {
    var a = L / 2, b = L * .2;
    return sv("path", { d: "M" + (x - a) + " " + y + " C" + (x - a) + " " + (y - b) + " " + (x + a * .55) + " " + (y - b * 1.25) + " " + (x + a) + " " + y +
      " C" + (x + a * .55) + " " + (y + b * 1.25) + " " + (x - a) + " " + (y + b) + " " + (x - a) + " " + y + " Z",
      fill: remplissage || PEAU, stroke: C.iv, "stroke-width": 2.4 }, g);
  }
  function algues(g, x, y, L, n, graine) {
    var out = [];
    for (var i = 0; i < n; i++) {
      var u = alea(graine + i) * 2 - 1, w = alea(graine + 50 + i) * 2 - 1;
      var px = x + u * L * .42, larg = L * .19 * Math.sqrt(Math.max(0, 1 - u * u)) * (u > 0 ? 1.05 : .95);
      out.push(sv("circle", { cx: px.toFixed(1), cy: (y + w * larg * .8).toFixed(1), r: 3.2 + alea(graine + 90 + i) * 2, fill: VERT_ALGUE }, g));
    }
    return out;
  }

  /* 1 · Le génome ne change pas, le phénotype si : trois sources de diversité non génétique ({id.1} à {id.3}) */
  SERIE_ILLU.c4_trois = function (s, v) {
    var W = v.w, g = sv("g", {}, s), cx = W / 2;
    var adn = sv("g", {}, g), d1 = "", d2 = "";
    for (var i = 0; i <= 60; i++) { var x = cx - 150 + i * 5, y1 = 70 + 26 * Math.sin(i * .32), y2 = 70 - 26 * Math.sin(i * .32); d1 += (i ? " L" : "M") + x + " " + y1.toFixed(1); d2 += (i ? " L" : "M") + x + " " + y2.toFixed(1); }
    var b1 = sv("path", { d: d1, fill: "none", stroke: C.te, "stroke-width": 4 }, adn), b2 = sv("path", { d: d2, fill: "none", stroke: C.sa, "stroke-width": 4 }, adn);
    var barres = []; for (var j = 0; j < 20; j++) { var xx = cx - 147 + j * 15, a = 26 * Math.sin((xx - cx + 150) / 5 * .32); barres.push(sv("line", { x1: xx, x2: xx, y1: 70 - a, y2: 70 + a, stroke: "rgba(231,242,218,.35)", "stroke-width": 2 }, adn)); }
    var l0 = txt(g, cx, 136, "Le génome : inchangé", { fs: 26, c: C.iv });
    var cad = sv("rect", { x: cx - 200, y: 30, width: 400, height: 120, rx: 18, fill: "none", stroke: "rgba(231,242,218,.3)", "stroke-width": 2, "stroke-dasharray": "7 6" }, g);
    var fl = fleche(g, "M" + cx + " 160 V212", C.iv2, 3);
    var ph = txt(g, cx, 250, "… et pourtant le phénotype se diversifie, par :", { fs: 26, c: C.sa });
    var X = [W * .17, W * .5, W * .83], T = [["des associations", "entre êtres vivants"], ["ce que l'animal", "construit hors de son corps"], ["des comportements", "appris"]];
    var cols = [C.vert, C.or, C.te], blocs = [];
    X.forEach(function (x, k) {
      var b = sv("g", {}, g);
      sv("rect", { x: x - 165, y: 290, width: 330, height: 210, rx: 20, fill: "rgba(10,23,16,.72)", stroke: cols[k], "stroke-width": 2.4 }, b);
      var ic = sv("g", { transform: "translate(" + x + ",360)" }, b);
      if (k === 0) { sv("circle", { cx: -26, cy: 0, r: 26, fill: "none", stroke: cols[k], "stroke-width": 4 }, ic); sv("circle", { cx: 22, cy: 0, r: 18, fill: "none", stroke: cols[k], "stroke-width": 4 }, ic); sv("path", { d: "M-2 -6 C4 -14 8 -14 6 -2", fill: "none", stroke: cols[k], "stroke-width": 3 }, ic); }
      if (k === 1) { sv("path", { d: "M-46 10 Q0 52 46 10", fill: "none", stroke: cols[k], "stroke-width": 5, "stroke-linecap": "round" }, ic); sv("path", { d: "M-40 6 L40 -2 M-34 18 L36 12 M-24 28 L28 24", stroke: cols[k], "stroke-width": 2.5, opacity: .7 }, ic); sv("circle", { cx: -10, cy: -6, r: 7, fill: cols[k] }, ic); sv("circle", { cx: 10, cy: -8, r: 7, fill: cols[k] }, ic); }
      if (k === 2) { sv("circle", { cx: -30, cy: -14, r: 12, fill: "none", stroke: cols[k], "stroke-width": 4 }, ic); sv("path", { d: "M-30 -2 V30 M-46 10 H-14", stroke: cols[k], "stroke-width": 4, "stroke-linecap": "round" }, ic); sv("circle", { cx: 30, cy: -4, r: 9, fill: "none", stroke: cols[k], "stroke-width": 4 }, ic); sv("path", { d: "M30 5 V30 M18 14 H42", stroke: cols[k], "stroke-width": 4, "stroke-linecap": "round" }, ic); sv("path", { d: "M-12 -26 Q0 -40 14 -24", fill: "none", stroke: cols[k], "stroke-width": 2.5, "stroke-dasharray": "4 4" }, ic); }
      txt(b, x, 438, T[k][0], { fs: 25, c: C.iv }); txt(b, x, 470, T[k][1], { fs: 25, c: C.iv });
      blocs.push(b);
    });
    return function (t, st) {
      var p = P(st.tl, 0, 1.2); trace(b1, p); trace(b2, p); barres.forEach(function (bb, i) { op(bb, E(P(st.tl, .3 + i * .03, .3))); });
      apparait(l0, st.tl, .9); apparait(cad, st.tl, 1.1);
      var t1 = et(v, "1", 2.5);
      fl(EIO(P(t, t1 - .9, .6))); apparait(ph, t, t1 - .6);
      blocs.forEach(function (b, k) { var q = apparait(b, t, et(v, String(k + 1), 2.5 + k * 1.2), .7); decale(b, q, 24); });
    };
  };

  /* 2 · Le ver de Roscoff : le jeune ingère des micro-algues {id.1}, elles se multiplient et le tube digestif régresse {id.2},
     l'adulte vert, sans tube digestif, vit de la photosynthèse des algues {id.3} ; échanges entre partenaires {id.4} */
  SERIE_ILLU.c4_roscoff = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), X = [W * .17, W * .5, W * .83], Y = H * .44, L = 260;
    var titres = [["Le jeune ver", "translucide, il a un tube digestif"], ["Il ingère des micro-algues", "une seule fois ; elles se multiplient"], ["L'adulte", "vert, sans tube digestif"]];
    var st_ = X.map(function (x, k) {
      var b = sv("g", {}, g);
      var corps = ver(b, x, Y, L, k === 0 ? "rgba(231,242,218,.10)" : k === 1 ? "rgba(111,209,122,.18)" : "rgba(111,209,122,.42)");
      var tube = sv("path", { d: "M" + (x - L * .42) + " " + Y + " H" + (x + L * .25) + " M" + (x - L * .2) + " " + Y + " l-14 -14 M" + (x - L * .2) + " " + Y + " l-14 14 M" + (x + .05 * L) + " " + Y + " l-14 -14 M" + (x + .05 * L) + " " + Y + " l-14 14",
        fill: "none", stroke: C.ca, "stroke-width": 3.4, "stroke-linecap": "round", opacity: k === 0 ? .9 : k === 1 ? .45 : 0 }, b);
      var al = k === 0 ? [] : algues(b, x, Y, L, k === 1 ? 14 : 46, 10 + k * 100);
      txt(b, x, Y + 96, titres[k][0], { fs: 25, c: C.iv }); txt(b, x, Y + 128, titres[k][1], { fs: 20, c: C.iv2, fw: 400 });
      return { b: b, al: al, tube: tube };
    });
    var entrants = [];
    for (var i = 0; i < 6; i++) entrants.push(sv("circle", { r: 5, fill: VERT_ALGUE }, g));
    var soleil = sv("g", { transform: "translate(" + X[2] + "," + (Y - 150) + ")" }, g);
    sv("circle", { r: 22, fill: C.or }, soleil);
    for (var r = 0; r < 8; r++) sv("line", { x1: 0, y1: -30, x2: 0, y2: -42, stroke: C.or, "stroke-width": 3.5, "stroke-linecap": "round", transform: "rotate(" + r * 45 + ")" }, soleil);
    var rayons = sv("path", { d: "M" + (X[2] - 30) + " " + (Y - 118) + " L" + (X[2] - 60) + " " + (Y - 50) + " M" + X[2] + " " + (Y - 118) + " V" + (Y - 52) + " M" + (X[2] + 30) + " " + (Y - 118) + " L" + (X[2] + 60) + " " + (Y - 50),
      stroke: C.or, "stroke-width": 2.5, "stroke-dasharray": "6 6", fill: "none" }, g);
    var ech = sv("g", {}, g), xb = W * .5, yb = H - 34;
    sv("rect", { x: 40, y: yb - 40, width: W - 80, height: 62, rx: 14, fill: "rgba(10,23,16,.8)", stroke: "rgba(183,217,76,.5)", "stroke-width": 2 }, ech);
    txt(ech, xb - 270, yb, "algues → ver : nutriments (photosynthèse)", { fs: 22, c: VERT_ALGUE });
    txt(ech, xb + 280, yb, "ver → algues : habitat stable", { fs: 22, c: C.te });
    var f12 = fleche(g, "M" + (X[0] + 145) + " " + Y + " H" + (X[1] - 148), C.iv2, 3), f23 = fleche(g, "M" + (X[1] + 145) + " " + Y + " H" + (X[2] - 148), C.iv2, 3);
    return function (t, st) {
      var t1 = et(v, "1", 2), t2 = et(v, "2", 5), t3 = et(v, "3", 8), t4 = et(v, "4", 11);
      apparait(st_[0].b, st.tl, .2);
      f12(EIO(P(t, t1, .6))); apparait(st_[1].b, t, t1 + .3);
      entrants.forEach(function (c, i) { // micro-algues qui entrent dans le jeune ver
        var u = EIO(P(t, t1 + .4 + i * .18, 1.1)), x0 = X[1] - 220 + i * 14, y0 = Y - 120 - (i % 3) * 18;
        c.setAttribute("cx", (x0 + (X[1] - 90 - x0) * u).toFixed(1)); c.setAttribute("cy", (y0 + (Y - y0) * u).toFixed(1));
        op(c, u <= 0 || u >= 1 ? 0 : 1);
      });
      st_[1].al.forEach(function (c, i) { op(c, E(P(t, t1 + 1.2 + i * .12, .4))); });
      f23(EIO(P(t, t2, .6))); apparait(st_[2].b, t, t2 + .3);
      st_[2].al.forEach(function (c, i) { op(c, E(P(t, t2 + .5 + i * .04, .4))); });
      st_[1].tube.setAttribute("opacity", (.9 - .5 * E(P(t, t2 - .2, 1))).toFixed(2));
      var ps = apparait(soleil, t, t3); op(rayons, ps * (.6 + .4 * Math.sin(t * 3)));
      var pe = apparait(ech, t, t4); decale(ech, pe, 16);
    };
  };

  /* 3 · Gammare sain et gammare parasité : le parasité monte vers la lumière {id.1}, tournoie en surface {id.2}, l'oiseau le mange {id.3} */
  function gammare(g, col) {
    var b = sv("g", {}, g);
    sv("path", { d: "M-34 6 C-30 -18 20 -24 34 -6 C38 2 30 10 22 8 C8 2 -18 4 -34 6 Z", fill: col, stroke: "rgba(4,12,8,.6)", "stroke-width": 1.5 }, b);
    for (var i = 0; i < 6; i++) sv("path", { d: "M" + (-24 + i * 9) + " 5 l" + (-3 + i) + " 13", stroke: col, "stroke-width": 2.2, "stroke-linecap": "round" }, b);
    sv("path", { d: "M30 -8 q14 -12 22 -26 M32 -4 q18 -4 26 -12", fill: "none", stroke: col, "stroke-width": 2 }, b);
    for (var j = 0; j < 4; j++) sv("path", { d: "M" + (-20 + j * 12) + " -14 q2 10 0 18", fill: "none", stroke: "rgba(4,12,8,.35)", "stroke-width": 1.4 }, b);
    return b;
  }
  SERIE_ILLU.c4_comport = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), surf = 90, fond = H - 50;
    var eau = sv("rect", { x: 30, y: surf, width: W - 60, height: fond - surf, rx: 12, fill: "rgba(116,185,216,.12)", stroke: "rgba(116,185,216,.45)", "stroke-width": 2 }, g);
    var vague = sv("path", { d: "", fill: "none", stroke: C.eau, "stroke-width": 3 }, g);
    sv("path", { d: "M30 " + fond + " Q" + W * .3 + " " + (fond - 26) + " " + W * .55 + " " + (fond - 8) + " T" + (W - 30) + " " + (fond - 14) + " V" + fond + " Z", fill: "rgba(140,110,70,.5)" }, g);
    var lum = sv("g", {}, g);
    for (var i = 0; i < 5; i++) sv("path", { d: "M" + (W * .62 + i * 46) + " 0 L" + (W * .56 + i * 60) + " " + (fond - 40), stroke: "rgba(255,210,74,.12)", "stroke-width": 26 }, lum);
    txt(g, W * .73, 40, "lumière", { fs: 22, c: C.or });
    var sain = gammare(g, "#c7a27a"), para = gammare(g, "#ff9f5b");
    var kyste = sv("circle", { r: 6, fill: "#ff6b5b", stroke: "#fff", "stroke-width": 1.5 }, para);
    var lS = txt(g, 200, fond - 90, "gammare sain : reste au fond, à l'abri", { fs: 22, c: C.iv2, fw: 400, ancre: "start" });
    var lP = txt(g, W * .42, surf + 120, "gammare parasité : attiré par la lumière", { fs: 22, c: "#ffb27a", fw: 500, ancre: "start" });
    var lT = txt(g, 60, surf + 40, "il remonte et tournoie à la surface", { fs: 22, c: "#ffb27a", fw: 500, ancre: "start" });
    var oiseau = sv("g", {}, g);
    sv("path", { d: "M-60 -6 C-30 -30 10 -30 30 -12 L58 -8 L30 0 C10 20 -30 16 -60 -6 Z", fill: "#e7f2da" }, oiseau);
    sv("path", { d: "M-10 -20 C0 -70 30 -80 40 -78 C20 -60 12 -40 10 -20 Z", fill: "#b4cb9c" }, oiseau);
    sv("circle", { cx: 20, cy: -12, r: 3, fill: "#0a1710" }, oiseau);
    var lO = txt(g, W * .2, 44, "proie facile pour un oiseau", { fs: 22, c: C.iv, ancre: "start" });
    return function (t, st) {
      var tl = st.tl, d = "";
      for (var x = 30; x <= W - 30; x += 10) d += (x === 30 ? "M" : " L") + x + " " + (surf + 4 * Math.sin(x * .03 + t * 2)).toFixed(1);
      vague.setAttribute("d", d);
      op(eau, E(P(tl, 0, .6))); op(lum, E(P(tl, .4, .8)) * (.7 + .3 * Math.sin(t * 1.5)));
      var t1 = et(v, "1", 3), t2 = et(v, "2", 7), t3 = et(v, "3", 11);
      // le sain se déplace lentement près du fond
      var xs = 240 + 60 * Math.sin(t * .5), ys = fond - 44 + 4 * Math.sin(t * 2);
      sain.setAttribute("transform", "translate(" + xs.toFixed(1) + "," + ys.toFixed(1) + ") scale(" + (Math.cos(t * .5) >= 0 ? 1 : -1) + ",1)");
      op(sain, E(P(tl, .5, .6))); apparait(lS, tl, 1);
      // le parasité : au fond, puis monte vers la lumière, puis tourne en surface
      var u = EIO(P(t, t1, 3.2)), xp = W * .45 + u * W * .2, yp = fond - 50 - u * (fond - surf - 80), ang = 0;
      if (t > t2) { var w = (t - t2) * 4.2; xp += 30 * Math.cos(w); yp += 18 * Math.sin(w); ang = (w * 57.3) % 360; }
      var pris = P(t, t3 + .8, 1.3);
      if (pris > 0) { yp -= 420 * EIO(pris); }
      para.setAttribute("transform", "translate(" + xp.toFixed(1) + "," + yp.toFixed(1) + ") rotate(" + ang.toFixed(1) + ")");
      kyste.setAttribute("cx", -6); kyste.setAttribute("cy", -6);
      op(para, E(P(tl, .7, .6)) * (pris >= 1 ? 0 : 1)); op(kyste, .6 + .4 * Math.sin(t * 5));
      apparait(lP, t, t1 + .3); op(lT, E(P(t, t2, .6))); if (t > t3) op(lP, 1 - E(P(t, t3, .5)));
      // l'oiseau plonge sur le gammare
      var q = EIO(P(t, t3, 1)), ox = W + 80 - (W + 80 - (xp + 40)) * q, oy = -40 + (surf - 20 + 40) * q - 420 * EIO(pris);
      oiseau.setAttribute("transform", "translate(" + ox.toFixed(1) + "," + oy.toFixed(1) + ") scale(-1,1)");
      op(oiseau, t >= t3 ? 1 - E(P(t, t3 + 1.6, .5)) : 0); apparait(lO, t, t3 + .6);
    };
  };

  /* 4 · Le cycle du parasite : 1er hôte intermédiaire {id.1}, gammare {id.2}, oiseau hôte définitif {id.3}, retour {id.4} */
  SERIE_ILLU.c4_cycle = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s);
    var N = [[W * .2, H * .62], [W * .5, H * .24], [W * .8, H * .62]];
    var nom = [["1er hôte intermédiaire", "multiplication asexuée"], ["Gammare : 2e hôte intermédiaire", "larves enkystées, comportement modifié"], ["Oiseau : hôte définitif", "adulte, reproduction sexuée (intestin)"]];
    var col = [C.te, "#ff9f5b", C.iv];
    var nds = N.map(function (p, k) {
      var b = sv("g", {}, g);
      sv("circle", { cx: p[0], cy: p[1], r: 64, fill: "rgba(10,23,16,.85)", stroke: col[k], "stroke-width": 3 }, b);
      var ic = sv("g", { transform: "translate(" + p[0] + "," + p[1] + ")" }, b);
      if (k === 0) { sv("path", { d: "M-30 14 C-30 -16 10 -30 26 -8 C36 6 22 22 4 16 C-10 12 -8 -4 6 -4", fill: "none", stroke: col[k], "stroke-width": 4 }, ic); sv("path", { d: "M-36 18 H34", stroke: col[k], "stroke-width": 4, "stroke-linecap": "round" }, ic); }
      if (k === 1) { var gm = gammare(ic, "#ff9f5b"); gm.setAttribute("transform", "scale(1.1)"); }
      if (k === 2) { sv("path", { d: "M-34 0 C-16 -20 8 -18 20 -6 L36 -4 L20 4 C8 16 -16 14 -34 0 Z", fill: col[k] }, ic); sv("path", { d: "M-6 -12 C0 -40 18 -46 24 -44 C12 -34 8 -22 6 -12 Z", fill: C.iv2 }, ic); }
      txt(b, p[0], p[1] + (k === 1 ? -100 : 100), nom[k][0], { fs: 23, c: col[k] });
      txt(b, p[0], p[1] + (k === 1 ? -74 : 128), nom[k][1], { fs: 19, c: C.iv2, fw: 400 });
      return b;
    });
    var f1 = fleche(g, "M" + (N[0][0] + 30) + " " + (N[0][1] - 66) + " Q" + (W * .28) + " " + (H * .24) + " " + (N[1][0] - 74) + " " + (N[1][1] + 6), C.iv2, 3);
    var f2 = fleche(g, "M" + (N[1][0] + 74) + " " + (N[1][1] + 6) + " Q" + (W * .72) + " " + (H * .24) + " " + (N[2][0] - 30) + " " + (N[2][1] - 66), C.iv2, 3);
    var f3 = fleche(g, "M" + (N[2][0] - 70) + " " + (N[2][1] + 20) + " Q" + (W * .5) + " " + (H * .86) + " " + (N[0][0] + 70) + " " + (N[0][1] + 20), "rgba(180,203,156,.6)", 2.6);
    var e1 = txt(g, W * .17, H * .24, "larves", { fs: 20, c: C.iv2, fw: 400 }), e2 = txt(g, W * .84, H * .24, "mangé en surface", { fs: 20, c: C.iv2, fw: 400 });
    var ti = txt(g, 20, H - 6, "Le cycle du parasite : trois hôtes", { fs: 22, c: C.sa, ancre: "start" });
    var e3 = txt(g, W * .5, H * .9, "œufs rejetés dans l'eau (précision hors cours)", { fs: 19, c: "rgba(180,203,156,.85)", fw: 400 });
    return function (t, st) {
      var tk = [1, 2, 3].map(function (k) { return et(v, String(k), 1 + (k - 1) * 2.5); }), t4 = et(v, "4", 9);
      apparait(ti, st.tl, .2);
      nds.forEach(function (b, k) { var q = E(P(t, tk[k], .7)), pre = .3 * E(P(st.tl, .4 + k * .4, .6)); op(b, Math.max(pre, q)); decale(b, Math.max(pre / .3 * .6, q), 18); });
      f1(EIO(P(t, tk[1] - .2, .9))); apparait(e1, t, tk[1] + .4);
      f2(EIO(P(t, tk[2] - .2, .9))); apparait(e2, t, tk[2] + .4);
      f3(EIO(P(t, t4, 1.1))); apparait(e3, t, t4 + .6);
    };
  };

  /* 5 · Mutualisme, parasitisme et les deux sens du mot « symbiose » : {id.1} mutualisme, {id.2} parasitisme, {id.3} sens large, {id.4} sens restreint */
  SERIE_ILLU.c4_symbiose = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s);
    var large = sv("g", {}, g);
    sv("rect", { x: 30, y: 60, width: W - 60, height: H - 90, rx: 26, fill: "rgba(183,217,76,.05)", stroke: C.sa, "stroke-width": 2.6, "stroke-dasharray": "10 7" }, large);
    txt(large, W / 2, 46, "Symbiose au sens large (bilan du chapitre 4) : association étroite, intime et durable", { fs: 22, c: C.sa });
    function boite(x, titre, signe, ex, col) {
      var b = sv("g", {}, g);
      sv("rect", { x: x, y: 110, width: W / 2 - 90, height: H - 240, rx: 20, fill: "rgba(10,23,16,.85)", stroke: col, "stroke-width": 2.6 }, b);
      txt(b, x + (W / 2 - 90) / 2, 160, titre, { fs: 30, c: col }); txt(b, x + (W / 2 - 90) / 2, 230, signe, { fs: 46, c: C.iv, fw: 700 });
      ex.forEach(function (l, i) { txt(b, x + (W / 2 - 90) / 2, 290 + i * 34, l, { fs: 21, c: C.iv2, fw: 400 }); });
      return b;
    }
    var mu = boite(60, "Mutualisme", "+ / +", ["bénéfices réciproques", "ver de Roscoff et micro-algues", "microbiote et être humain"], C.vert);
    var pa = boite(W / 2 + 30, "Parasitisme", "+ / −", ["le parasite profite, l'hôte subit", "parasite du gammare"], "#ff9f5b");
    var res = sv("g", {}, g);
    sv("rect", { x: 60, y: H - 116, width: W / 2 - 90, height: 46, rx: 12, fill: "rgba(124,224,138,.16)", stroke: C.vert, "stroke-width": 2 }, res);
    txt(res, 60 + (W / 2 - 90) / 2, H - 85, "sens restreint (ch. 2) : mutualisme + interdépendance", { fs: 18, c: C.vert });
    return function (t, st) {
      var q1 = apparait(mu, t, et(v, "1", .3)); decale(mu, q1, 18);
      var q2 = apparait(pa, t, et(v, "2", 2)); decale(pa, q2, 18);
      apparait(large, st.tl, .3);
      apparait(res, t, et(v, "4", 6));
    };
  };

  /* 6 · La larve de phrygane : soie {id.1}, graviers et débris collés {id.2}, fourreau abandonné quand il devient trop petit {id.3} */
  SERIE_ILLU.c4_phrygane = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), y = H * .5, x0 = W * .28;
    sv("path", { d: "M20 " + (H - 40) + " Q" + W / 2 + " " + (H - 70) + " " + (W - 20) + " " + (H - 44), fill: "none", stroke: "rgba(140,110,70,.7)", "stroke-width": 6 }, g);
    var larve = sv("g", {}, g);
    for (var i = 0; i < 9; i++) sv("ellipse", { cx: x0 + i * 26, cy: y, rx: 18, ry: 22 - i * .6, fill: "#e8d9b8", stroke: "#9b8660", "stroke-width": 1.5 }, larve);
    sv("ellipse", { cx: x0 - 22, cy: y, rx: 20, ry: 17, fill: "#5a4630" }, larve);
    for (var j = 0; j < 3; j++) sv("path", { d: "M" + (x0 + 4 + j * 20) + " " + (y + 16) + " l-10 26 l-8 4", fill: "none", stroke: "#5a4630", "stroke-width": 3, "stroke-linecap": "round" }, larve);
    var soie = sv("path", { d: "", fill: "none", stroke: "rgba(240,240,255,.85)", "stroke-width": 1.6 }, g);
    var dS = ""; for (var k = 0; k <= 60; k++) { var xx = x0 + 10 + k * 3.8, yy = y + 30 * Math.sin(k * 1.05); dS += (k ? " L" : "M") + xx.toFixed(1) + " " + yy.toFixed(1); }
    soie.setAttribute("d", dS);
    var tube = sv("rect", { x: x0 + 2, y: y - 34, width: 240, height: 68, rx: 30, fill: "rgba(240,240,255,.10)", stroke: "rgba(240,240,255,.6)", "stroke-width": 2 }, g);
    var grains = [];
    for (var n = 0; n < 34; n++) {
      var gx = x0 + 14 + alea(n + 7) * 220, gy = y + (alea(n + 70) > .5 ? -1 : 1) * (22 + alea(n + 140) * 12);
      var forme = n % 3 === 0 ? sv("rect", { x: gx - 9, y: gy - 3, width: 22, height: 6, rx: 2, fill: "#8a6f45", transform: "rotate(" + (alea(n) * 40 - 20) + " " + gx + " " + gy + ")" }, g)
        : sv("circle", { cx: gx, cy: gy, r: 6 + alea(n + 3) * 5, fill: ["#9c8e7a", "#7d7466", "#b3a58c"][n % 3] }, g);
      grains.push({ e: forme, x: gx, y: gy, x0: gx + (alea(n + 9) - .5) * 300, y0: H - 50 });
    }
    var l1 = txt(g, W * .72, y - 120, "1 · un fourreau de soie", { fs: 24, c: C.iv, ancre: "start" }), l1b = txt(g, W * .72, y - 90, "(sécrétions de ses glandes)", { fs: 19, c: C.iv2, fw: 400, ancre: "start" });
    var l2 = txt(g, W * .72, y - 20, "2 · recouvert de graviers", { fs: 24, c: C.iv, ancre: "start" }), l2b = txt(g, W * .72, y + 10, "et de débris du fond de l'eau", { fs: 19, c: C.iv2, fw: 400, ancre: "start" });
    var l3 = txt(g, W * .72, y + 80, "3 · trop petit : abandonné", { fs: 24, c: C.iv, ancre: "start" });
    return function (t, st) {
      var t1 = et(v, "1", 1.5), t2 = et(v, "2", 4.5), t3 = et(v, "3", 9);
      op(larve, E(P(st.tl, 0, .6)));
      var ond = Math.sin(t * 3) * 3; larve.setAttribute("transform", "translate(0," + ond.toFixed(1) + ")");
      trace(soie, EIO(P(t, t1, 2.2))); op(soie, 1 - .6 * E(P(t, t1 + 2.4, .8)) * 1); apparait(tube, t, t1 + 1.8, .8);
      apparait(l1, t, t1 + .2); apparait(l1b, t, t1 + .5);
      grains.forEach(function (gr, i) {
        var u = EIO(P(t, t2 + i * .1, .7));
        gr.e.setAttribute("transform", "translate(" + ((gr.x0 - gr.x) * (1 - u)).toFixed(1) + "," + ((gr.y0 - gr.y) * (1 - u)).toFixed(1) + ")" +
          (gr.e.tagName === "rect" ? " rotate(" + (alea(i) * 40 - 20) + " " + gr.x + " " + gr.y + ")" : ""));
        op(gr.e, t >= t2 + i * .1 ? 1 : 0);
      });
      apparait(l2, t, t2 + .2); apparait(l2b, t, t2 + .5);
      var sort = EIO(P(t, t3, 2)); larve.setAttribute("transform", "translate(" + (-330 * sort).toFixed(1) + "," + ond.toFixed(1) + ")");
      apparait(l3, t, t3 + .3);
    };
  };

  /* 7 · Le phénotype étendu : le corps (phénotype « classique »), puis ce qui est hors du corps {id.1} … {id.4} */
  SERIE_ILLU.c4_etendu = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), cx = W / 2, cy = H / 2 + 10;
    var halo = sv("ellipse", { cx: cx, cy: cy, rx: W * .44, ry: H * .42, fill: "rgba(183,217,76,.05)", stroke: C.sa, "stroke-width": 2.6, "stroke-dasharray": "10 8" }, g);
    var lh = txt(g, cx, cy - H * .42 + 34, "phénotype étendu : hors du corps", { fs: 23, c: C.sa });
    var corps = sv("g", {}, g);
    sv("ellipse", { cx: cx, cy: cy, rx: 150, ry: 92, fill: "rgba(10,23,16,.9)", stroke: C.iv, "stroke-width": 2.6 }, corps);
    txt(corps, cx, cy - 18, "le corps", { fs: 26, c: C.iv }); txt(corps, cx, cy + 14, "couleur, taille, organes…", { fs: 19, c: C.iv2, fw: 400 });
    txt(corps, cx, cy + 42, "phénotype « classique »", { fs: 19, c: C.iv2, fw: 400 });
    var it = [["fourreau", "phrygane", -1, -1], ["tonnelle", "jardinier satiné", 1, -1], ["toile, cocon", "araignée", -1, 1], ["port", "espèce humaine", 1, 1]];
    var bl = it.map(function (x) {
      var b = sv("g", {}, g), px = cx + x[2] * W * .3, py = cy + x[3] * H * .22;
      sv("rect", { x: px - 120, y: py - 38, width: 240, height: 76, rx: 16, fill: "rgba(10,23,16,.85)", stroke: C.or, "stroke-width": 2.2 }, b);
      txt(b, px, py - 6, x[0], { fs: 25, c: C.or }); txt(b, px, py + 22, x[1], { fs: 19, c: C.iv2, fw: 400 });
      var l = sv("line", { x1: cx + x[2] * 150 * .8, y1: cy + x[3] * 92 * .7, x2: px - x[2] * 120, y2: py - x[3] * 10, stroke: "rgba(255,210,74,.5)", "stroke-width": 2, "stroke-dasharray": "5 5" }, b);
      return b;
    });
    return function (t, st) {
      apparait(corps, st.tl, .1); var ph = apparait(halo, t, et(v, "1", 1.5) - .5, .9); op(lh, ph);
      bl.forEach(function (b, k) { var q = apparait(b, t, et(v, String(k + 1), 1.5 + k * .8)); decale(b, q, 16); });
    };
  };

  /* 8 · Casse des noix : la noix sur l'enclume {id.1}, le percuteur frappe {id.2}, la noix s'ouvre {id.3} */
  SERIE_ILLU.c4_noix = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), cx = W * .42, sol = H - 70;
    sv("path", { d: "M20 " + sol + " H" + (W - 20), stroke: "rgba(140,110,70,.8)", "stroke-width": 5 }, g);
    var encl = sv("g", {}, g);
    sv("path", { d: "M" + (cx - 140) + " " + sol + " L" + (cx - 120) + " " + (sol - 90) + " C" + (cx - 60) + " " + (sol - 104) + " " + (cx + 60) + " " + (sol - 104) + " " + (cx + 130) + " " + (sol - 88) + " L" + (cx + 150) + " " + sol + " Z", fill: "#7d7466", stroke: "#5c554a", "stroke-width": 3 }, encl);
    var lE = txt(g, cx + 190, sol - 40, "l'enclume : un support en bois ou en pierre", { fs: 22, c: C.iv2, fw: 500, ancre: "start" });
    var noix = sv("g", {}, g), ny = sol - 126;
    var n1 = sv("path", { d: "M" + cx + " " + (ny - 24) + " A24 24 0 0 0 " + cx + " " + (ny + 24) + " Z", fill: "#8a5a2b", stroke: "#4a2e14", "stroke-width": 2.5 }, noix);
    var n2 = sv("path", { d: "M" + cx + " " + (ny - 24) + " A24 24 0 0 1 " + cx + " " + (ny + 24) + " Z", fill: "#8a5a2b", stroke: "#4a2e14", "stroke-width": 2.5 }, noix);
    var amande = sv("ellipse", { cx: cx, cy: ny, rx: 13, ry: 17, fill: "#f2dfb0" }, g);
    var lN = txt(g, cx - 190, ny - 10, "la noix de Coula, très dure", { fs: 22, c: C.iv2, fw: 500, ancre: "end" });
    var perc = sv("g", {}, g);
    sv("path", { d: "M-46 -26 C-20 -44 30 -40 50 -18 C60 0 40 26 0 28 C-40 30 -60 4 -46 -26 Z", fill: "#9c8e7a", stroke: "#5c554a", "stroke-width": 3 }, perc);
    var bras = sv("path", { d: "", fill: "none", stroke: "#3b2a1e", "stroke-width": 26, "stroke-linecap": "round" }, g);
    var lP = txt(g, cx + 190, ny - 150, "le percuteur, tenu à la main", { fs: 22, c: C.iv2, fw: 500, ancre: "start" });
    var choc = sv("path", { d: "M" + (cx - 50) + " " + (ny - 30) + " l-24 -10 M" + (cx + 50) + " " + (ny - 30) + " l24 -10 M" + (cx - 44) + " " + (ny + 4) + " l-28 4 M" + (cx + 44) + " " + (ny + 4) + " l28 4", stroke: C.or, "stroke-width": 3.5, "stroke-linecap": "round" }, g);
    return function (t, st) {
      var t1 = et(v, "1", .8), t2 = et(v, "2", 2.5), t3 = et(v, "3", 6);
      op(encl, E(P(st.tl, 0, .6))); apparait(lE, st.tl, .5);
      var pn = apparait(noix, t, t1); noix.setAttribute("transform", "translate(0," + (-40 * (1 - pn)).toFixed(1) + ")"); apparait(lN, t, t1 + .3);
      // le percuteur se lève et retombe (période 1,4 s) jusqu'à l'ouverture de la noix
      var dt = t - t2, per = 1.4, ph = dt > 0 ? (dt % per) / per : 0, cyc = function (tt) { var d = tt - t2, f = d > 0 ? (d % per) / per : 0; return d > 0 ? (f < .7 ? EIO(f / .7) : 1 - Math.pow((f - .7) / .3, 2)) : 0; },
        haut = t < t3 ? cyc(t) : cyc(t3) + (1 - cyc(t3)) * EIO(P(t, t3, .6));
      var px = cx + 10, py = ny - 54 - 150 * haut;
      perc.setAttribute("transform", "translate(" + px.toFixed(1) + "," + py.toFixed(1) + ") rotate(" + (-12 * haut).toFixed(1) + ")");
      bras.setAttribute("d", "M" + (px + 30) + " " + (py - 10) + " Q" + (px + 160) + " " + (py - 120) + " " + (W - 40) + " " + (py - 180));
      op(perc, E(P(t, t2 - .6, .5))); op(bras, E(P(t, t2 - .6, .5)) * .9); apparait(lP, t, t2);
      op(choc, dt > 0 && ph > .9 && t < t3 ? 1 : 0);
      var ouv = EIO(P(t, t3, .6));
      n1.setAttribute("transform", "translate(" + (-34 * ouv).toFixed(1) + "," + (18 * ouv).toFixed(1) + ") rotate(" + (-40 * ouv) + " " + cx + " " + ny + ")");
      n2.setAttribute("transform", "translate(" + (34 * ouv).toFixed(1) + "," + (18 * ouv).toFixed(1) + ") rotate(" + (40 * ouv) + " " + cx + " " + ny + ")");
      op(amande, t >= t3 ? 1 : 0);
    };
  };

  /* 9 · Le chant appris : sonogrammes schématiques de l'adulte {id.1}, du jeune élevé avec des adultes {id.2}, du jeune isolé {id.3} */
  SERIE_ILLU.c4_chant = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s), x0 = 330, x1 = W - 30, hh = 110;
    var lig = [["Chant de l'espèce", "un adulte", C.sa], ["Jeune élevé avec ses congénères", "après entraînement", C.vert], ["Jeune élevé isolé", "très éloigné du chant de l'espèce", C.ca]];
    // motif de notes de l'espèce : (début, durée, fréquence haute, fréquence basse) en fractions
    var motif = [[.02, .07, .8, .45], [.12, .05, .9, .7], [.2, .05, .9, .7], [.28, .05, .9, .7], [.38, .12, .55, .3], [.55, .04, .85, .4], [.62, .04, .85, .4], [.7, .14, .65, .6], [.88, .08, .5, .2]];
    var rangs = lig.map(function (l, k) {
      var b = sv("g", {}, g), y = 40 + k * (hh + 52);
      sv("rect", { x: x0, y: y, width: x1 - x0, height: hh, rx: 10, fill: "rgba(4,12,8,.7)", stroke: "rgba(231,242,218,.25)", "stroke-width": 1.5 }, b);
      txt(b, x0 - 20, y + hh / 2 - 6, l[0], { fs: 21, c: l[2], ancre: "end" }); txt(b, x0 - 20, y + hh / 2 + 22, l[1], { fs: 17, c: C.iv2, fw: 400, ancre: "end" });
      var notes = motif.map(function (m, i) {
        var a = m.slice();
        if (k === 1) { a[0] += (alea(i + 3) - .5) * .02; a[2] += (alea(i + 13) - .5) * .06; }
        if (k === 2) { a[0] = .04 + i * .1 + (alea(i + 23) - .5) * .04; a[1] = .03 + alea(i + 33) * .08; a[2] = .3 + alea(i + 43) * .6; a[3] = a[2] - .05 - alea(i + 53) * .2; }
        var nx = x0 + 10 + a[0] * (x1 - x0 - 20), nw = a[1] * (x1 - x0 - 20), yh = y + hh - 8 - a[2] * (hh - 16), yb = y + hh - 8 - a[3] * (hh - 16);
        return sv("path", { d: "M" + nx.toFixed(1) + " " + yh.toFixed(1) + " L" + (nx + nw).toFixed(1) + " " + yb.toFixed(1), stroke: l[2], "stroke-width": 7, "stroke-linecap": "round" }, b);
      });
      var tete = sv("line", { x1: x0, x2: x0, y1: y + 4, y2: y + hh - 4, stroke: "rgba(231,242,218,.7)", "stroke-width": 2 }, b);
      return { b: b, notes: notes, tete: tete };
    });
    var ax = txt(g, (x0 + x1) / 2, H - 6, "sonogrammes schématiques : le temps en abscisse, la hauteur du son en ordonnée", { fs: 17, c: C.iv2, fw: 400 });
    return function (t, st) {
      apparait(ax, st.tl, .3);
      rangs.forEach(function (r, k) {
        var tk = et(v, String(k + 1), .5 + k * 2.5), q = apparait(r.b, st.tl, .3 + k * .3, .5), u = P(t, tk + .3, 2.4);
        r.notes.forEach(function (n, i) { var q = P(u, motif[i][0], .08); trace(n, q); op(n, q > 0 ? 1 : 0); });
        r.tete.setAttribute("transform", "translate(" + (u * (x1 - x0)).toFixed(1) + ",0)"); op(r.tete, u > 0 && u < 1 ? 1 : 0);
      });
    };
  };

  /* 10 · Baleines à bosse du Pacifique Sud : un nouveau chant apparaît en Australie {id.1} et gagne les populations plus à l'est {id.2} */
  SERIE_ILLU.c4_baleines = function (s, v) {
    var W = v.w, H = v.h, g = sv("g", {}, s);
    function X(lon) { if (lon < 0) lon += 360; return 40 + (lon - 140) / (215 - 140) * (W - 80); }
    function Y(lat) { return 60 + (-lat - 5) / (40 - 5) * (H - 140); }
    var mer = sv("rect", { x: 30, y: 40, width: W - 60, height: H - 110, rx: 14, fill: "rgba(116,185,216,.08)", stroke: "rgba(116,185,216,.35)", "stroke-width": 2 }, g);
    // côte est de l'Australie, simplifiée
    var aus = [[140, -10.7], [142.5, -10.7], [143.5, -14], [145.4, -15.5], [146.3, -19], [149, -21.5], [150.8, -23.5], [153.1, -25.5], [153.6, -28.5], [153, -31.5], [151.3, -33.8], [150, -37.5], [140, -38]];
    sv("path", { d: "M" + aus.map(function (p) { return X(p[0]).toFixed(1) + " " + Y(p[1]).toFixed(1); }).join(" L") + " Z", fill: "rgba(198,170,120,.35)", stroke: "rgba(198,170,120,.8)", "stroke-width": 2 }, g);
    txt(g, X(144.5), Y(-27), "Australie", { fs: 24, c: "#d9c49a" });
    var pops = [["Australie (est)", 153.5, -27, 0], ["Nouvelle-Calédonie", 166, -21.5, 1], ["Tonga", -175, -20, 1], ["Samoa américaines", -170.5, -14.3, 2], ["Îles Cook", -159.8, -21.2, 2], ["Polynésie française", -149.5, -17.6, 3]];
    var V1 = "#7fe3ff", V2 = "#ff9f5b";
    var pts = pops.map(function (p, k) {
      var b = sv("g", {}, g), x = X(p[1]) + (k === 0 ? 34 : 0), y = Y(p[2]);
      var c = sv("circle", { cx: x, cy: y, r: 15, fill: V1, stroke: "#04111a", "stroke-width": 2 }, b);
      var o = sv("circle", { cx: x, cy: y, r: 15, fill: "none", stroke: V1, "stroke-width": 2 }, b);
      txt(b, x, y + (k % 2 ? -26 : 44), p[0], { fs: 19, c: C.iv });
      return { b: b, c: c, o: o, d: p[3] };
    });
    var an = txt(g, W - 60, H - 30, "", { fs: 26, c: C.iv, ancre: "end" });
    var leg = sv("g", {}, g);
    sv("circle", { cx: 70, cy: H - 40, r: 10, fill: V1 }, leg); txt(leg, 88, H - 33, "chant ancien", { fs: 19, c: C.iv2, fw: 400, ancre: "start" });
    sv("circle", { cx: 250, cy: H - 40, r: 10, fill: V2 }, leg); txt(leg, 268, H - 33, "nouveau chant", { fs: 19, c: C.iv2, fw: 400, ancre: "start" });
    var fl = fleche(g, "M" + (X(156)) + " " + (Y(-33)) + " Q" + X(180) + " " + Y(-38) + " " + X(205) + " " + Y(-30), V2, 3.5);
    return function (t, st) {
      op(mer, E(P(st.tl, 0, .6))); apparait(leg, st.tl, .6);
      var t1 = et(v, "1", 2), t2 = et(v, "2", 5), an_ = 3.2; // une « année » de l'animation, en secondes
      pts.forEach(function (p, k) {
        apparait(p.b, st.tl, .4 + k * .15);
        var tc = p.d === 0 ? t1 : t2 + (p.d - 1) * an_, q = E(P(t, tc, .8));
        p.c.setAttribute("fill", q > .5 ? V2 : V1);
        var r = t > tc ? ((t - tc) % 1.6) / 1.6 : 0;
        p.o.setAttribute("r", (15 + 26 * r).toFixed(1)); p.o.setAttribute("stroke", q > .5 ? V2 : V1); op(p.o, t > tc && t < tc + 4.8 ? 1 - r : 0);
      });
      var n = t < t1 ? 0 : t < t2 ? 1 : Math.min(4, 2 + Math.floor((t - t2) / an_));
      an.textContent = n ? "année " + n : ""; op(an, E(P(t, t1, .5)));
      fl(EIO(P(t, t2, 2.5 * an_)));
    };
  };
  Object.keys(SERIE_ILLU).forEach(function (k) {
    if (k.indexOf("c4_") !== 0 || SERIE_ILLU[k]._prep) return;
    var f = SERIE_ILLU[k], g = function (svg, v) { prep(); return f(svg, v); };
    g._prep = true; SERIE_ILLU[k] = g;
  });
})();
