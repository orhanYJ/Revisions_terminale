/* Illustrations propres à la vidéo maths-ch2 (« Limites de suites »), chargées après maths/serie/moteur.js.
   Rendu fonction pure du temps ; outils du moteur dans window.SERIE_OUTILS.

   nuage : un repère à la craie et des suites de points.
     v.ax = {x: [x0, x1], y: [y0, y1], gx: [...], gy: [...]} (graduations écrites) ;
     v.series = [{pts: [[n, u], ...], c: "sa", r: 6, pas: .08, trait: false, pts_: true, lab: "$u_n$", lp: [x, y],
                  o: [["s1", 1], ["s2", .25], ["tous", 1]]}] : opacité de la série, réglée à chaque repère {id.clé}
                  (par défaut : apparaît au repère {id.s<i+1>}, sinon au début) ; les points arrivent un à un ;
     v.ligne = {y: 2, lab: "$\\ell=2$"} : droite horizontale en pointillés, au repère {id.l} (ou au premier palier) ;
     v.etapes = [{type: "bande", l: 2, e: 1, N: 3, lab: "..."} | {type: "seuil", A: 4, N: 16, lab: "..."} | {fin: true}] :
                palier j au repère {id.b<j>} ; la bande (ou la zone au-dessus de A) se règle en douceur d'un palier à
                l'autre ; trait vertical au rang N ; les points de la première série sont verts s'ils sont dans la
                zone à partir du rang N, roses s'ils sont dehors ; N: null = « aucun rang ne convient ».
   zenon : la pièce à traverser ; le morceau k (la moitié du reste) se colorie au repère {id.k} (k = 1…4), les suivants
     à partir du repère {id.go} ; la somme partielle s'écrit dessous ; {id.fin} : le bandeau v.fin. */
(function () {
  var O = window.SERIE_OUTILS, sv = O.sv, lbl = O.lbl, C = O.C, E = O.E, EIO = O.EIO, P = O.P, cl = O.cl, op = O.op,
    trace = O.trace, wob = O.wob, dPts = O.dPts, rng = O.rng;
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  function col(c) { return C[c] || c || C.iv; }
  function quand(v, k, repli) { return v.et && v.et[k] != null ? v.et[k] : repli; }
  var NID = 0;

  window.SERIE_ILLU.nuage = function (s, v) {
    var Wd = v.w, Hd = v.h, m = v.marges || [96, 40, 36, 64], pw = Wd - m[0] - m[1], ph = Hd - m[2] - m[3], ax = v.ax;
    function X(x) { return m[0] + (x - ax.x[0]) / (ax.x[1] - ax.x[0]) * pw; }
    function Y(y) { return m[2] + (1 - (y - ax.y[0]) / (ax.y[1] - ax.y[0])) * ph; }
    var id = "nu" + (++NID) + Math.round((v.t0 || 0) * 100), R = rng(Math.round(Wd + Hd + (v.t0 || 0) * 10));
    var defs = sv("defs", {}, s);
    var cp = sv("clipPath", { id: id + "c" }, defs);
    sv("rect", { x: m[0] - 8, y: m[2] - 8, width: pw + 16, height: ph + 16 }, cp);
    var pat = sv("pattern", { id: id + "h", patternUnits: "userSpaceOnUse", width: 14, height: 14, patternTransform: "rotate(-45)" }, defs);
    sv("line", { x1: 0, y1: 0, x2: 0, y2: 14, stroke: C.sa, "stroke-width": 2.4, opacity: .45 }, pat);
    var x0 = cl(0, ax.x[0], ax.x[1]), y0 = cl(0, ax.y[0], ax.y[1]);
    // graduations
    var grille = [], ticks = [];
    (ax.gx || []).forEach(function (x) {
      grille.push(sv("path", { d: dPts(wob(X(x), m[2] + ph, X(x), m[2], 1, R)), stroke: "rgba(238,240,230,.10)", "stroke-width": 1.6, fill: "none" }, s));
      var d = lbl(s, X(x), Y(y0) + 8, String(x).replace(".", ","), "tk"); d.style.fontSize = "26px"; d.style.color = C.iv2; ticks.push(d);
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("path", { d: dPts(wob(m[0], Y(y), m[0] + pw, Y(y), 1, R)), stroke: "rgba(238,240,230,.10)", "stroke-width": 1.6, fill: "none" }, s));
      var d = lbl(s, X(x0) - 30, Y(y) - 17, String(y).replace(".", ","), "tk"); d.style.fontSize = "26px"; d.style.color = C.iv2; ticks.push(d);
    });
    var axX = sv("path", { d: dPts(wob(m[0] - 4, Y(y0), m[0] + pw + 14, Y(y0) - 1, .8, R)), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, s);
    var axY = sv("path", { d: dPts(wob(X(x0), m[2] + ph + 4, X(x0) + 1, m[2] - 14, .8, R)), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, s);
    var lx = lbl(s, m[0] + pw + 18, Y(y0) + 6, ax.lx || "$n$", "tk"); lx.style.fontSize = "30px";
    var plot = sv("g", { "clip-path": "url(#" + id + "c)" }, s);
    // zone (bande ou seuil), droite ℓ, rang N
    var zone = sv("rect", { x: m[0], y: 0, width: pw, height: 0, fill: "url(#" + id + "h)", stroke: C.sa, "stroke-width": 2.4, "stroke-dasharray": "2 0", opacity: 0 }, plot);
    var ligne = v.ligne ? sv("path", { d: "M" + m[0] + " " + Y(v.ligne.y) + " H" + (m[0] + pw), stroke: C.sa, "stroke-width": 2.6, "stroke-dasharray": "10 9", fill: "none", opacity: 0 }, plot) : null;
    var lLab = v.ligne && v.ligne.lab ? lbl(s, m[0] + pw - 46, Y(v.ligne.y) - 52, v.ligne.lab, "tk") : null;
    if (lLab) { lLab.style.fontSize = "32px"; lLab.style.color = C.sa; }
    var rangL = sv("path", { d: "", stroke: C.ca, "stroke-width": 3, "stroke-dasharray": "8 8", fill: "none", opacity: 0 }, plot);
    var etapes = (v.etapes || []).map(function (e_, j) {
      var x = { e: e_, t: quand(v, "b" + (j + 1), 1e9) };
      if (e_.lab) {
        x.l = lbl(s, e_.lp ? X(e_.lp[0]) : m[0] + pw * .62, e_.lp ? Y(e_.lp[1]) : m[2] + 4, e_.lab, "bulle");
        x.l.style.fontSize = "28px";
      }
      if (e_.N != null) { x.n = lbl(s, X(e_.N), m[2] + ph + 2, "$N=" + e_.N + "$", "tk"); x.n.style.fontSize = "30px"; x.n.style.color = C.ca; }
      return x;
    });
    // séries
    var series = (v.series || []).map(function (sr, i) {
      var g = sv("g", { opacity: 0 }, plot), c = col(sr.c), x = { sr: sr, g: g, col: c };
      var o = sr.o || [["s" + (i + 1), 1]];
      x.o = o.map(function (p) { return [quand(v, p[0], p[0] === "debut" || !sr.o ? v.t0 + .9 : 1e9), p[1]]; });
      x.t1 = x.o[0][0];
      if (sr.trait) x.p = sv("path", { d: "M" + sr.pts.map(function (p) { return X(p[0]).toFixed(1) + " " + Y(p[1]).toFixed(1); }).join(" L"),
        stroke: c, "stroke-width": sr.ep || 2.4, fill: "none", "stroke-linejoin": "round", opacity: sr.trait === "pale" ? .55 : 1 }, g);
      x.c = sr.points === false ? [] : sr.pts.map(function (p) { return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: 0, fill: c }, g); });
      if (sr.lab) { x.l = lbl(s, X(sr.lp[0]), Y(sr.lp[1]), sr.lab, "tk"); x.l.style.fontSize = (sr.fs || 32) + "px"; x.l.style.color = c; }
      return x;
    });
    function opac(x, t) {
      var a = 0;
      x.o.forEach(function (p, k) { var prev = k ? x.o[k - 1][1] : 0; if (t >= p[0]) a = prev + (p[1] - prev) * E(P(t, p[0], .5)); });
      return a;
    }
    return function (t, st) {
      var tl = st.tl;
      trace(axX, P(tl, .05, .5)); trace(axY, P(tl, .35, .5));
      grille.forEach(function (gg) { trace(gg, P(tl, .6, .4)); });
      ticks.forEach(function (d) { op(d, E(P(tl, .7, .4))); });
      op(lx, E(P(tl, .5, .4)));
      // palier courant et zone interpolée
      var cur = -1;
      etapes.forEach(function (x, j) { if (t >= x.t) cur = j; });
      var lo = null, hi = null, N = null, za = 0, typ = null;
      if (cur >= 0 && !etapes[cur].e.fin) {
        var e_ = etapes[cur].e, pr = cur > 0 && !etapes[cur - 1].e.fin ? etapes[cur - 1].e : null, u = EIO(P(t, etapes[cur].t, .9));
        typ = e_.type;
        if (typ === "bande") {
          var eps = pr && pr.type === "bande" ? pr.e + (e_.e - pr.e) * u : e_.e;
          lo = e_.l - eps; hi = e_.l + eps;
        } else {
          var A = pr && pr.type === "seuil" ? pr.A + (e_.A - pr.A) * u : e_.A;
          lo = A; hi = ax.y[1] + 10;
        }
        za = pr ? 1 : E(P(t, etapes[cur].t, .6));
        N = e_.N;
        var tN = etapes[cur].t + (pr ? .9 : .5);
        if (N != null) {
          rangL.setAttribute("d", "M" + X(N) + " " + (m[2] + ph) + " V" + m[2]);
          op(rangL, E(P(t, tN, .4)));
        } else op(rangL, 0);
      } else { op(rangL, 0); }
      var fin = cur >= 0 && etapes[cur].e.fin;
      if (lo != null) {
        var ya = Y(Math.min(hi, ax.y[1] + 1)), yb = Y(Math.max(lo, ax.y[0] - 1));
        zone.setAttribute("y", Math.min(ya, yb).toFixed(1)); zone.setAttribute("height", Math.abs(yb - ya).toFixed(1));
        op(zone, za);
      } else if (fin) op(zone, 1 - E(P(t, etapes[cur].t, .5)));
      else op(zone, 0);
      if (ligne) { var tl_ = quand(v, "l", etapes.length ? etapes[0].t : v.t0 + 1); op(ligne, E(P(t, tl_, .5))); if (lLab) op(lLab, E(P(t, tl_ + .2, .5))); }
      etapes.forEach(function (x, j) {
        var on = j === cur ? E(P(t, x.t + .3, .5)) : 0;
        if (x.l) op(x.l, on);
        if (x.n) op(x.n, j === cur ? E(P(t, x.t + (j && !etapes[j - 1].e.fin ? 1 : .6), .4)) : 0);
      });
      series.forEach(function (x, i) {
        var a = opac(x, t);
        op(x.g, a); if (x.l) op(x.l, a * E(P(t, x.t1 + .6, .5)));
        var pas = x.sr.pas != null ? x.sr.pas : .07;
        if (x.p) { x.p.style.visibility = a > 0 ? "" : "hidden"; trace(x.p, P(t, x.t1, Math.max(.6, pas * x.sr.pts.length))); }
        x.c.forEach(function (c, j) {
          var q = P(t, x.t1 + j * pas, .25), pt = x.sr.pts[j];
          c.setAttribute("r", ((x.sr.r || 6) * E(q)).toFixed(2));
          var cc = x.col;
          if (i === 0 && lo != null && za > .5) {
            var dedans = typ === "seuil" ? pt[1] >= lo - 1e-9 : pt[1] > lo && pt[1] < hi;
            if (!dedans) cc = C.ca;
            else if (N != null ? pt[0] >= N : typ === "seuil") cc = C.vert;
          }
          c.setAttribute("fill", cc);
        });
      });
    };
  };

  window.SERIE_ILLU.zenon = function (s, v) {
    var Wd = v.w, Hd = v.h, xa = 70, xb = Wd - 70, y = Hd * .42, L = xb - xa, R = rng(41);
    var defs = sv("defs", {}, s), id = "ze" + (++NID);
    function pat(n, c) {
      var p = sv("pattern", { id: id + n, patternUnits: "userSpaceOnUse", width: 12, height: 12, patternTransform: "rotate(-45)" }, defs);
      sv("line", { x1: 0, y1: 0, x2: 0, y2: 12, stroke: c, "stroke-width": 3, opacity: .75 }, p);
      return "url(#" + id + n + ")";
    }
    var HJ = [pat("a", C.sa), pat("b", C.te)];
    var seg = sv("path", { d: dPts(wob(xa, y, xb, y, 1.2, R)), stroke: C.iv, "stroke-width": 3.4, fill: "none", "stroke-linecap": "round" }, s);
    var bornes = [xa, xb].map(function (x) { return sv("path", { d: "M" + x + " " + (y - 26) + " V" + (y + 26), stroke: C.iv, "stroke-width": 3.4, "stroke-linecap": "round" }, s); });
    var l0 = lbl(s, xa, y + 36, "$0$", "pv"), l1 = lbl(s, xb, y + 36, "$1$", "pv");
    var dep = lbl(s, xa + 20, y - 150, "départ", "tk"), arr = lbl(s, xb - 30, y - 150, "le mur", "tk");
    [dep, arr].forEach(function (d) { d.style.fontSize = "30px"; d.style.color = C.iv2; });
    var NP = 12, pieces = [];
    for (var k = 1; k <= NP; k++) {
      var a = 1 - Math.pow(2, -(k - 1)), b = 1 - Math.pow(2, -k);
      var r = sv("rect", { x: xa + a * L + 1.5, y: y - 22, width: Math.max(0.6, (b - a) * L - 3), height: 44, fill: HJ[(k - 1) % 2], stroke: k % 2 ? C.sa : C.te, "stroke-width": k < 7 ? 2.4 : 1, rx: 3, opacity: 0 }, s);
      var f = null;
      if (k <= 4) { f = lbl(s, xa + (a + b) / 2 * L, y - 98, k === 4 ? "$\\frac1{16}$" : "$\\frac1{" + Math.pow(2, k) + "}$", "pv"); f.style.color = k % 2 ? C.sa : C.te; }
      pieces.push({ r: r, f: f, b: b });
    }
    var SOM = ["$\\frac12$", "$\\frac12+\\frac14=\\frac34$", "$\\frac12+\\frac14+\\frac18=\\frac78$",
      "$\\frac12+\\frac14+\\frac18+\\frac1{16}=\\frac{15}{16}$", "$\\frac12+\\frac14+\\dots+\\frac1{2^n}=1-\\frac1{2^n}$"];
    var sl = SOM.map(function (x) { var d = lbl(s, Wd / 2, y + 100, x, "som"); d.style.transform = "translate(-50%,0)"; d.style.fontSize = "46px"; return d; });
    var pion = sv("circle", { cx: xa, cy: y, r: 13, fill: C.ca }, s);
    var bf = v.fin ? lbl(s, Wd / 2, Hd - 92, v.fin, "ban") : null;
    function tk(k) {
      if (k <= 4) return quand(v, String(k), v.t0 + .6 + k);
      return quand(v, "go", v.t0 + 6) + (k - 5) * .4;
    }
    return function (t, st) {
      var tl = st.tl;
      trace(seg, P(tl, .05, .7)); bornes.forEach(function (b, i) { trace(b, P(tl, .5 + i * .2, .25)); });
      op(l0, E(P(tl, .6, .4))); op(l1, E(P(tl, .8, .4))); op(dep, E(P(tl, .7, .4))); op(arr, E(P(tl, .9, .4)));
      var pos = 0;
      pieces.forEach(function (p, i) {
        var q = P(t, tk(i + 1), .45);
        op(p.r, E(q));
        if (p.f) op(p.f, E(P(t, tk(i + 1) + .2, .4)));
        if (q > 0) pos = (i ? pieces[i - 1].b : 0) + (p.b - (i ? pieces[i - 1].b : 0)) * EIO(q);
      });
      pion.setAttribute("cx", (xa + pos * L).toFixed(1));
      op(pion, E(P(t, tk(1) - .3, .3)));
      var tg = quand(v, "go", 1e9);
      sl.forEach(function (d, i) {
        var a = i < 4 ? E(P(t, tk(i + 1) + .3, .4)) * (1 - E(P(t, i < 3 ? tk(i + 2) : tg, .3))) : E(P(t, tg + .3, .5));
        op(d, a);
      });
      if (bf) op(bf, E(P(t, quand(v, "fin", 1e9), .6)));
    };
  };
})();
