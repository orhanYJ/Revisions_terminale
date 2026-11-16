/* Vidéo du chapitre 4 de maths (« Dérivation, convexité, continuité ») : illustrations propres au chapitre.
   Chargé par maths/serie/maths-ch4.html après moteur.js (generer.py l'ajoute s'il existe). Chaque illustration :
   SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; } ; rendu fonction pure du temps
   (t : temps de la vidéo, st.tl : temps depuis l'apparition). Étapes calées sur la voix par les repères {id.k}. */
(function () {
  "use strict";
  var O, C, sv, P, E, EIO, op, trace, et, lbl, h, esc;
  function prep() {
    if (O) return;
    O = window.SERIE_OUTILS; C = O.C; sv = O.sv; P = O.P; E = O.E; EIO = O.EIO; op = O.op; trace = O.trace; et = O.et;
    lbl = O.lbl; h = O.h; esc = O.esc;
  }
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var SERIE_ILLU = window.SERIE_ILLU;

  // fonctions tracées et leurs dérivées
  var FN = {
    x2: [function (x) { return x * x; }, function (x) { return 2 * x; }],
    exp: [Math.exp, Math.exp],
    sqrt: [Math.sqrt, function (x) { return 1 / (2 * Math.sqrt(x)); }],
    x3: [function (x) { return x * x * x; }, function (x) { return 3 * x * x; }],
    expm: [function (x) { return Math.exp(-x); }, function (x) { return -Math.exp(-x); }],
    cube: [function (x) { return x * x * x + x - 1; }, function (x) { return 3 * x * x + 1; }]
  };
  function dec(x) { return String(x).replace(".", "{,}"); }
  function fmt(x, n) { return (Math.round(x * Math.pow(10, n)) / Math.pow(10, n)).toFixed(n).replace(".", ",").replace("-", "−"); }

  // repère commun : cadre (l, t, w, h) dans la boîte, intervalles v.x, v.y ; axes tracés à la craie
  function repere(s, v, R) {
    var X = function (x) { return R.l + (x - v.x[0]) / (v.x[1] - v.x[0]) * R.w; };
    var Y = function (y) { return R.t + (1 - (y - v.y[0]) / (v.y[1] - v.y[0])) * R.h; };
    var x0 = Math.min(Math.max(0, v.x[0]), v.x[1]), y0 = Math.min(Math.max(0, v.y[0]), v.y[1]);
    var g = sv("g", {}, s);
    var ax = sv("path", { d: "M" + (R.l - 6) + " " + Y(y0) + " H" + (R.l + R.w + 10), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, g);
    var ay = sv("path", { d: "M" + X(x0) + " " + (R.t + R.h + 6) + " V" + (R.t - 10), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, g);
    var id = "clip" + Math.round(Math.random() * 1e9);
    var cp = sv("clipPath", { id: id }, sv("defs", {}, s));
    sv("rect", { x: R.l, y: R.t - 6, width: R.w, height: R.h + 12 }, cp);
    return { X: X, Y: Y, ax: ax, ay: ay, clip: "url(#" + id + ")", x0: x0, y0: y0 };
  }
  function courbe(s, F, v, Rp, n, col, ep, clip) {
    var d = "";
    for (var i = 0; i <= n; i++) {
      var x = v.x[0] + (v.x[1] - v.x[0]) * i / n;
      if (v.dom && (x < v.dom[0] || x > v.dom[1])) continue;
      var y = F(x);
      d += (d ? " L" : "M") + Rp.X(x).toFixed(1) + " " + Rp.Y(y).toFixed(1);
    }
    return sv("path", { d: d, stroke: col, "stroke-width": ep, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round", "clip-path": clip }, s);
  }
  function num(parent, x, y, couleur, taille) {
    var d = h("div", "", parent);
    d.style.cssText = "position:absolute;left:" + x + "px;top:" + y + "px;font-size:" + (taille || 34) + "px;color:" + couleur +
      ";white-space:nowrap;opacity:0;font-family:inherit;font-variant-numeric:tabular-nums";
    return d;
  }

  /* tangentes : la courbe de v.f (x2, exp, sqrt, x3, expm), puis
     {id.corde} une corde [AB] entre v.corde[0] et v.corde[1] (effacée à {id.tan}) ;
     {id.tan} la tangente au point d'abscisse v.de ; de {id.go} à {id.go} + v.dur, le point glisse jusqu'à v.a,
     la pente est lue en haut à gauche (v.pente = false : pas de lecture) ;
     intervalles du repère v.rx, v.ry ; v.dom : domaine de la courbe ;
     {id.fixes} tangentes fixes aux abscisses v.fixes ; {id.inf} point d'inflexion à l'origine (tangente y = 0). */
  SERIE_ILLU.tangentes = function (s, v) {
    prep();
    var F = FN[v.f][0], D = FN[v.f][1], W = v.w, H = v.h;
    var R = { l: 50, t: 40, w: W - 100, h: H - 90 };
    var V = { x: v.rx, y: v.ry, dom: v.dom };
    var Rp = repere(s, V, R);
    var cb = courbe(s, F, V, Rp, 220, C.iv, 4, Rp.clip);
    // corde
    var gc = sv("g", { opacity: 0 }, s), cA = null;
    if (v.corde) {
      var a = v.corde[0], b = v.corde[1];
      cA = sv("path", { d: "M" + Rp.X(a) + " " + Rp.Y(F(a)) + " L" + Rp.X(b) + " " + Rp.Y(F(b)), stroke: C.ca, "stroke-width": 3.4, fill: "none", "stroke-linecap": "round" }, gc);
      sv("circle", { cx: Rp.X(a), cy: Rp.Y(F(a)), r: 7, fill: C.ca }, gc);
      sv("circle", { cx: Rp.X(b), cy: Rp.Y(F(b)), r: 7, fill: C.ca }, gc);
    }
    var lA = v.corde ? lbl(s, Rp.X(v.corde[0]) - 26, Rp.Y(F(v.corde[0])) - 56, "$A$", "gr") : null;
    var lB = v.corde ? lbl(s, Rp.X(v.corde[1]) + 26, Rp.Y(F(v.corde[1])) - 56, "$B$", "gr") : null;
    var lC = v.corde && v.lcorde ? lbl(s, v.lcorde[0], v.lcorde[1], v.tcorde || "la courbe passe sous la corde", "gr") : null;
    // tangentes fixes
    var fx = (v.fixes || []).map(function (x) {
      var m = D(x), L = (V.x[1] - V.x[0]) * .5;
      return sv("path", { d: "M" + Rp.X(x - L) + " " + Rp.Y(F(x) - m * L) + " L" + Rp.X(x + L) + " " + Rp.Y(F(x) + m * L), stroke: C.te,
        "stroke-width": 2.4, "stroke-dasharray": "9 8", fill: "none", opacity: 0, "clip-path": Rp.clip }, s);
    });
    var lF = v.fixes && v.lfixes ? lbl(s, v.lfixes[0], v.lfixes[1], v.tfixes || "", "pc") : null;
    // tangente mobile
    var tg = sv("path", { d: "", stroke: C.sa, "stroke-width": 3.6, fill: "none", "stroke-linecap": "round", "clip-path": Rp.clip, opacity: 0 }, s);
    var pt = sv("circle", { r: 8, fill: C.sa, opacity: 0 }, s);
    var lP = v.pente !== false && v.de != null ? num(s.parentNode, 70, 0, C.te, 34) : null;
    // inflexion
    var gi = sv("g", { opacity: 0 }, s), lI = null;
    if (v.inf) {
      sv("path", { d: "M" + R.l + " " + Rp.Y(0) + " H" + (R.l + R.w), stroke: C.sa, "stroke-width": 3.6, fill: "none" }, gi);
      sv("circle", { cx: Rp.X(0), cy: Rp.Y(0), r: 10, fill: "none", stroke: C.ca, "stroke-width": 3.4 }, gi);
      lI = lbl(s, v.linf[0], v.linf[1], v.tinf || "point d'inflexion", "gr");
    }
    var lZ = v.zones ? v.zones.map(function (z) { return lbl(s, z[0], z[1], z[2], z[3] || "pc"); }) : [];
    return function (t, st) {
      var tl = st.tl;
      trace(Rp.ax, P(tl, 0, .5)); trace(Rp.ay, P(tl, .3, .5)); trace(cb, EIO(P(tl, .6, 1.6)));
      if (v.corde) {
        var tc = et(v, "corde", 1e9), tt = et(v, "tan", 1e9);
        var q = E(P(t, tc, .4)) * (1 - E(P(t, tt, .5)));
        gc.setAttribute("opacity", q); trace(cA, EIO(P(t, tc, .8)));
        lA.style.opacity = lB.style.opacity = q;
        if (lC) lC.style.opacity = E(P(t, tc + .9, .5)) * (1 - E(P(t, tt, .5)));
      }
      var tf = et(v, "fixes", 1e9);
      fx.forEach(function (p, i) { p.setAttribute("opacity", .85 * E(P(t, tf + i * .35, .4))); trace(p, P(t, tf + i * .35, .5)); });
      if (lF) lF.style.opacity = E(P(t, tf + .4 * fx.length, .5));
      lZ.forEach(function (l, i) { l.style.opacity = E(P(t, et(v, "z" + (i + 1), 1e9), .5)); });
      if (v.tan != null || v.de != null) {
        var t1 = et(v, "tan", 1e9), tg0 = et(v, "go", 1e9), dur = v.dur || 6, tfin = et(v, "fin", 1e9);
        var u = EIO(P(t, tg0, dur)), x = v.de + (v.a - v.de) * u, m = D(x), y = F(x);
        var dxs = R.w / (V.x[1] - V.x[0]), dys = R.h / (V.y[1] - V.y[0]);
        var vx = dxs, vy = -m * dys, n = Math.hypot(vx, vy), L = v.lt || 260;
        vx = vx / n * L; vy = vy / n * L;
        var px = Rp.X(x), py = Rp.Y(y);
        tg.setAttribute("d", "M" + (px - vx).toFixed(1) + " " + (py - vy).toFixed(1) + " L" + (px + vx).toFixed(1) + " " + (py + vy).toFixed(1));
        var qa = E(P(t, t1, .5)) * (1 - E(P(t, tfin, .5)));
        tg.setAttribute("opacity", qa); pt.setAttribute("opacity", qa);
        pt.setAttribute("cx", px.toFixed(1)); pt.setAttribute("cy", py.toFixed(1));
        if (lP) { lP.style.opacity = qa; lP.textContent = "pente de la tangente : " + fmt(m, 2); }
      }
      if (v.inf) {
        var ti = et(v, "inf", 1e9);
        gi.setAttribute("opacity", E(P(t, ti, .5)));
        lI.style.opacity = E(P(t, ti + .3, .5));
      }
    };
  };

  /* dicho : la dichotomie sur f(x) = x³ + x − 1, intervalle de départ [0 ; 1] ({id.1}) ;
     à chaque repère {id.k} (k = 2…v.n), on prend le milieu m, on lit le signe de f(m), on garde la moitié qui change de signe.
     À droite, le tableau des intervalles, une ligne par étape. */
  SERIE_ILLU.dicho = function (s, v) {
    prep();
    var F = FN.cube[0], W = v.w, H = v.h, n = v.n || 6;
    var R = { l: 40, t: 40, w: 560, h: H - 110 };
    var vv = { x: [-0.08, 1.12], y: [-1.15, 1.25] };
    var Rp = repere(s, vv, R);
    var cb = courbe(s, F, vv, Rp, 160, C.iv, 4, Rp.clip);
    var l0 = lbl(s, Rp.X(0.3), Rp.Y(1.0), "$y=x^3+x-1$", "pc");
    var steps = [[0, 1]], mids = [];
    for (var k = 1; k < n; k++) {
      var a = steps[k - 1][0], b = steps[k - 1][1], m = (a + b) / 2;
      mids.push(m);
      steps.push(F(a) * F(m) <= 0 ? [a, m] : [m, b]);
    }
    // intervalle (barre jaune sur l'axe des abscisses) et milieu
    var Y0 = Rp.Y(0);
    var bar = sv("path", { d: "", stroke: C.sa, "stroke-width": 10, "stroke-linecap": "round", fill: "none", opacity: 0 }, s);
    var ga = sv("path", { d: "", stroke: C.sa, "stroke-width": 3, fill: "none", opacity: 0 }, s);
    var mv = sv("path", { d: "", stroke: C.te, "stroke-width": 2.6, "stroke-dasharray": "7 7", fill: "none", opacity: 0 }, s);
    var mp = sv("circle", { r: 8, fill: C.te, opacity: 0 }, s);
    var sg = num(s.parentNode, 0, 0, C.te, 32);
    var ti = lbl(s, 860, 6, "Intervalle, étape par étape", "pc");
    var lignes = steps.map(function (iv, k) {
      return lbl(s, 860, 64 + k * 64, "$[" + dec(iv[0]) + "\\,;\\," + dec(iv[1]) + "]$ · largeur $" + dec(iv[1] - iv[0]) + "$", "pk");
    });
    lignes.forEach(function (l) { l.style.fontSize = "30px"; });
    return function (t, st) {
      var tl = st.tl;
      trace(Rp.ax, P(tl, 0, .5)); trace(Rp.ay, P(tl, .3, .5)); trace(cb, EIO(P(tl, .6, 1.4)));
      l0.style.opacity = E(P(tl, 1.4, .5)); ti.style.opacity = E(P(tl, .4, .5));
      var tk = [];
      for (var k = 0; k < n; k++) tk.push(et(v, String(k + 1), .8 + 3.2 * k));
      // étape courante
      var cur = -1;
      for (k = 0; k < n; k++) if (t >= tk[k]) cur = k;
      lignes.forEach(function (l, k) { l.style.opacity = E(P(t, tk[k] + (k ? 1.6 : .2), .5)); l.style.color = k === cur ? C.sa : ""; });
      if (cur < 0) { op(bar, 0); op(ga, 0); op(mv, 0); op(mp, 0); sg.style.opacity = 0; return; }
      var iv = steps[Math.max(0, cur - 1)];
      var x1 = iv[0], x2 = iv[1];
      if (cur >= 1) {
        // le milieu apparaît, puis l'intervalle se resserre (1,6 s après le repère)
        var m = mids[cur - 1], fm = F(m), u = EIO(P(t, tk[cur] + 1.6, .8)), nv = steps[cur];
        x1 = iv[0] + (nv[0] - iv[0]) * u; x2 = iv[1] + (nv[1] - iv[1]) * u;
        var qm = E(P(t, tk[cur], .4)) * (1 - E(P(t, tk[cur] + 2.6, .4)));
        mv.setAttribute("d", "M" + Rp.X(m) + " " + Y0 + " V" + Rp.Y(fm)); op(mv, qm);
        mp.setAttribute("cx", Rp.X(m)); mp.setAttribute("cy", Rp.Y(fm)); op(mp, qm);
        sg.textContent = "f(m) " + (fm < 0 ? "< 0" : "> 0");
        sg.style.color = fm < 0 ? C.ca : C.vert;
        sg.style.left = (Rp.X(m) + (fm < 0 ? 16 : -150)) + "px"; sg.style.top = (Rp.Y(fm) + (fm < 0 ? 10 : -56)) + "px";
        sg.style.opacity = qm;
      } else { op(mv, 0); op(mp, 0); sg.style.opacity = 0; }
      bar.setAttribute("d", "M" + Rp.X(x1).toFixed(1) + " " + Y0 + " H" + Rp.X(x2).toFixed(1));
      ga.setAttribute("d", "M" + Rp.X(x1) + " " + Rp.Y(F(x1)) + " V" + Y0 + " M" + Rp.X(x2) + " " + Rp.Y(F(x2)) + " V" + Y0);
      op(bar, E(P(t, tk[0], .5))); op(ga, .6 * E(P(t, tk[0], .5)));
    };
  };
})();
