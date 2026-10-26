/* Cartes animées DNL — moteur commun (globe d3-geo sur canvas, lecteur type vidéo).
   Données : window.CARTE, produites par outils/cartes-animees/generer.py.
   Le rendu est une fonction pure du temps t : on peut lire, mettre en pause, revenir, glisser sans à-coup. */
(function () {
  "use strict";
  var C = window.CARTE, d3 = window.d3;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.get("embed") === "1";
  var LANG = Q.get("lang") === "en" ? "en" : "fr";
  var UI = {
    fr: { lancer: "Lancer la carte animée", lire: "Lecture", pause: "Pause", prec: "Date précédente", suiv: "Date suivante",
          arret: "Pause à chaque date", voix: "Voix", plein: "Plein écran", quitter: "Quitter le plein écran", partie: "Partie",
          sansVoix: "La voix n'est pas disponible sur cet appareil.", hors: "hors cours", ouvrir: "Ouvrir en grand" },
    en: { lancer: "Play the animated map", lire: "Play", pause: "Pause", prec: "Previous date", suiv: "Next date",
          arret: "Pause at each date", voix: "Voice", plein: "Full screen", quitter: "Exit full screen", partie: "Part",
          sansVoix: "Voice is not available on this device.", hors: "outside the course", ouvrir: "Open full size" }
  };
  var SEA = "#D9E5EB", LAND = "#EFE8D8", EDGE = "#B9AB89", INK = "#17233F", PAPER = "#F7F3EA";

  /* ---------- couleurs ---------- */
  function hex(h) {
    if (!h) return null;
    var n = parseInt(h.slice(1), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  }
  // style = [r, g, b, a, hr, hg, hb, ha] : remplissage puis hachures
  function style(spec, defaut) {
    if (!spec) return defaut.slice();
    var f = hex(spec[0]), h = hex(spec[1]);
    return [f ? f[0] : 0, f ? f[1] : 0, f ? f[2] : 0, f ? 1 : 0, h ? h[0] : 0, h ? h[1] : 0, h ? h[2] : 0, h ? 1 : 0];
  }
  function mix(a, b, t, o) {
    for (var k = 0; k < 8; k += 4) {
      var a0 = a[k + 3], a1 = b[k + 3];
      for (var j = 0; j < 3; j++) {
        var x = a0 === 0 ? b[k + j] : a[k + j], y = a1 === 0 ? a[k + j] : b[k + j];
        o[k + j] = x + (y - x) * t;
      }
      o[k + 3] = a0 + (a1 - a0) * t;
    }
    return o;
  }
  function rgba(s, k, al) { return "rgba(" + (s[k] | 0) + "," + (s[k + 1] | 0) + "," + (s[k + 2] | 0) + "," + (s[k + 3] * (al == null ? 1 : al)).toFixed(3) + ")"; }
  function same(a, b) { for (var k = 0; k < 8; k++) if (Math.abs(a[k] - b[k]) > 0.01) return false; return true; }

  /* ---------- données ---------- */
  function feat(mp) {
    return { type: "Feature", geometry: { type: "MultiPolygon", coordinates: mp.map(function (poly) { return poly.map(function (r) { return r.map(function (p) { return [p[0] / 100, p[1] / 100]; }); }); }) } };
  }
  var OV = {}; (C.overlay || []).forEach(function (id) { OV[id] = 1; });
  var PIECES = C.pieces.map(function (p, i) {
    var g = feat(p.g), m = feat(p.m), f = p.f ? feat(p.f) : m;
    var c = d3.geoCentroid(g), r = 0;
    g.geometry.coordinates.forEach(function (poly) { poly[0].forEach(function (q) { r = Math.max(r, d3.geoDistance(c, q)); }); });
    return { id: p.id, i: i, g: g, m: m, f: f, c: c, r: r, ov: !!OV[p.id], clip: p.id === "sov41" };
  });
  var IDX = {}; PIECES.forEach(function (p) { IDX[p.id] = p.i; });
  var DEF_BASE = style([LAND, null], null), DEF_OV = [0, 0, 0, 0, 0, 0, 0, 0];
  var SC = C.scenes, N = SC.length;
  var STY = [], cur = PIECES.map(function (p) { return p.ov ? DEF_OV.slice() : DEF_BASE.slice(); });
  SC.forEach(function (s) {
    Object.keys(s.st || {}).forEach(function (id) {
      if (IDX[id] == null) throw new Error("pièce inconnue : " + id);
      cur[IDX[id]] = style(s.st[id], PIECES[IDX[id]].ov ? DEF_OV : DEF_BASE);
    });
    STY.push(cur.map(function (x) { return x.slice(); }));
  });
  var FR = {}; Object.keys(C.fronts || {}).forEach(function (k) { FR[k] = { pts: C.fronts[k].pts.map(function (p) { return [p[0] / 100, p[1] / 100]; }), occ: C.fronts[k].occ }; });
  var LB = C.labels || {};
  SC.forEach(function (s) {
    (s.arrows || []).forEach(function (a) { a.P = a.pts.map(function (p) { return [p[0] / 100, p[1] / 100]; }); });
    s.labels = s.labels || []; s.pins = s.pins || []; s.arrows = s.arrows || [];
  });

  /* ---------- temps ---------- */
  var RHO = 1.42, RHO2 = RHO * RHO, RHO4 = RHO2 * RHO2;
  function zoomPath(c0, k0, c1, k1) {
    var w0 = 2 / k0, w1 = 2 / k1, d1 = d3.geoDistance(c0, c1), S, f;
    var gi = d3.geoInterpolate(c0, c1);
    if (d1 < 1e-5) {
      S = Math.log(w1 / w0) / RHO;
      f = function (s) { return { c: c1, k: 2 / (w0 * Math.exp(RHO * s * S)) }; };
    } else {
      var d2 = d1 * d1, b0 = (w1 * w1 - w0 * w0 + RHO4 * d2) / (2 * w0 * RHO2 * d1), b1 = (w1 * w1 - w0 * w0 - RHO4 * d2) / (2 * w1 * RHO2 * d1);
      var r0 = Math.log(Math.sqrt(b0 * b0 + 1) - b0), r1 = Math.log(Math.sqrt(b1 * b1 + 1) - b1);
      S = (r1 - r0) / RHO;
      f = function (s) {
        s *= S;
        var ch = Math.cosh(r0), u = w0 / (RHO2 * d1) * (ch * Math.tanh(RHO * s + r0) - Math.sinh(r0));
        return { c: gi(Math.max(0, Math.min(1, u))), k: 2 / (w0 * ch / Math.cosh(RHO * s + r0)) };
      };
    }
    return { S: Math.abs(S) || 0, f: f };
  }
  var START = [], TOT = 0, ZP = [], TC = [];
  SC.forEach(function (s, i) {
    START.push(TOT); TOT += s.d;
    if (i === 0) { ZP.push(null); TC.push(0); return; }
    var a = SC[i - 1].cam, b = s.cam;
    var z = zoomPath([a[0], a[1]], a[2], [b[0], b[1]], b[2]);
    ZP.push(z);
    TC.push(z.S < 0.02 ? 0 : Math.max(1.3, Math.min(5.2, z.S * 0.8 + 0.7)) * (s.lent || 1));
  });
  START.push(TOT);
  function sceneAt(t) { var i = 0; while (i < N - 1 && t >= START[i + 1]) i++; return i; }
  var ease = function (x) { x = Math.max(0, Math.min(1, x)); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  var clamp01 = function (x) { return Math.max(0, Math.min(1, x)); };
  function cdelay(i) { return Math.min(TC[i] * 0.55, 2.4); }

  /* ---------- page ---------- */
  var root = document.getElementById("carte");
  root.className = "carte" + (EMBED ? " embed" : "");
  root.innerHTML =
    '<div class="vue"><canvas></canvas>' +
      '<div class="chip"><span class="chip-p"></span><span class="chip-d"></span></div>' +
      '<button class="go" type="button"><span class="go-i">▶</span><span class="go-t"></span></button>' +
      '<div class="leg"><div class="leg-d"></div><div class="leg-t"></div><div class="leg-x"></div><div class="leg-k"></div></div>' +
    '</div>' +
    '<div class="ctl">' +
      '<div class="barre"><div class="rail"><div class="plein"></div></div><div class="ticks"></div><input type="range" min="0" step="0.01" aria-label="timeline"></div>' +
      '<div class="btns">' +
        '<button class="b-prec" type="button">⏮</button><button class="b-lire" type="button">▶</button><button class="b-suiv" type="button">⏭</button>' +
        '<span class="tps"></span><span class="sp"></span>' +
        '<label class="opt"><input type="checkbox" class="o-arret"> <span class="o-arret-t"></span></label>' +
        '<label class="opt"><input type="checkbox" class="o-voix"> <span class="o-voix-t"></span></label>' +
        '<button class="b-plein" type="button">⛶</button>' +
      '</div>' +
    '</div>';
  var $ = function (s) { return root.querySelector(s); };
  var vue = $(".vue"), cv = $("canvas"), ctx = cv.getContext("2d");
  var range = $(".barre input"), plein = $(".plein"), ticks = $(".ticks");
  var legD = $(".leg-d"), legT = $(".leg-t"), legX = $(".leg-x"), legK = $(".leg-k"), leg = $(".leg");
  var chipP = $(".chip-p"), chipD = $(".chip-d");
  range.max = TOT;
  SC.forEach(function (s, i) {
    var m = document.createElement("button");
    m.type = "button"; m.className = "tick" + (s.part !== (SC[i - 1] || {}).part ? " tick-p" : "");
    m.style.left = (START[i] / TOT * 100) + "%";
    m.addEventListener("click", function () { aller(START[i] + 0.001); });
    ticks.appendChild(m);
  });

  var proj = d3.geoOrthographic().clipAngle(90).precision(0.8);
  var path = d3.geoPath(proj, ctx), chaine = d3.geoPath(proj);
  // cache des tracés : tant que la caméra ne bouge pas, chaque pièce est projetée une seule fois (Path2D)
  var cache = null, cacheKey = null, prevKey = null, useCache = false;
  function trace(id, geom) {
    if (!useCache) { ctx.beginPath(); path(geom); return true; }
    var p = cache[id];
    if (p === undefined) { var st = chaine(geom); p = cache[id] = st ? new Path2D(st) : null; }
    return p;
  }
  function remplir(p) { if (p === true) ctx.fill(); else ctx.fill(p); }
  function contour(p) { if (p === true) ctx.stroke(); else ctx.stroke(p); }
  function decouper(p) { if (p === true) ctx.clip(); else ctx.clip(p); }
  var W = 0, H = 0, DPR = 1, R0 = 1, DPRMAX = 2, lent = 0;
  var grat = d3.geoGraticule().step([15, 15])();
  var pats = {};
  function motif(rgb) {
    var k = rgb.join(",");
    if (pats[k]) return pats[k];
    var c = document.createElement("canvas"), s = Math.round(8 * DPR);
    c.width = c.height = s;
    var x = c.getContext("2d");
    x.strokeStyle = "rgb(" + k + ")"; x.lineWidth = 2.2 * DPR;
    x.beginPath(); x.moveTo(-1, s + 1); x.lineTo(s + 1, -1); x.moveTo(-1 - s, s + 1); x.lineTo(1, -1); x.moveTo(s - 1, 2 * s + 1); x.lineTo(2 * s + 1, s - 1); x.stroke();
    return (pats[k] = ctx.createPattern(c, "repeat"));
  }
  function taille() {
    var w = vue.clientWidth;
    var narrow = w < 640;
    var full = document.fullscreenElement === root;
    var h = full ? Math.max(240, window.innerHeight - $(".ctl").offsetHeight - (narrow ? leg.offsetHeight : 0)) : (narrow ? Math.round(Math.min(w * 1.05, window.innerHeight * 0.62)) : Math.round(w * 9 / 16));
    root.classList.toggle("etroit", narrow);
    DPR = Math.min(DPRMAX, window.devicePixelRatio || 1);
    W = w; H = h;
    cv.style.width = w + "px"; cv.style.height = h + "px";
    cv.width = Math.round(w * DPR); cv.height = Math.round(h * DPR);
    R0 = Math.min(w, h) * 0.46;
    pats = {};
    proj.clipExtent([[-20, -20], [w + 20, h + 20]]);
    hauteurLeg();
    rendre(T);
    hauteur();
  }

  /* ---------- rendu ---------- */
  var T = 0, playing = false, last = 0, lastScene = -1, tmp = [0, 0, 0, 0, 0, 0, 0, 0];
  function camAt(t) {
    var i = sceneAt(t), u = t - START[i], b = SC[i].cam;
    if (i > 0 && TC[i] > 0 && u < TC[i]) {
      var z = ZP[i].f(ease(u / TC[i]));
      return { c: z.c, k: z.k, i: i, u: u };
    }
    return { c: [b[0], b[1]], k: b[2], i: i, u: u };
  }
  function vis(p, cam, marge) { return d3.geoDistance(p, cam.c) < Math.PI / 2 - (marge || 0.02); }
  function frontAt(i, u) {
    var a = i > 0 ? SC[i - 1].front : null, b = SC[i].front;
    var t0 = cdelay(i) + (SC[i].fdelay || 0), dur = SC[i].fdur || 1.6;
    var x = i === 0 ? 1 : ease((u - t0) / dur);
    if (!a && !b) return null;
    if (a && b && a !== b) {
      var A = FR[a].pts, B = FR[b].pts, P = new Array(A.length);
      for (var j = 0; j < A.length; j++) P[j] = [A[j][0] + (B[j][0] - A[j][0]) * x, A[j][1] + (B[j][1] - A[j][1]) * x];
      var occ = FR[a].occ + (FR[b].occ - FR[a].occ) * clamp01(x * 6);
      return { P: P, al: 1, occ: occ };
    }
    var k = b || a, al = b ? (a ? 1 : x) : 1 - x;
    return { P: FR[k].pts, al: al, occ: FR[k].occ };
  }
  function ligneEcran(P, n) {
    var out = [];
    for (var j = 0; j < n; j++) out.push(proj(P[j]));
    return out;
  }
  function fleche(a, cam, p, al) {
    if (p <= 0 || al <= 0) return;
    var P = a.P, n = P.length, vu = 0;
    for (var j = 0; j < n; j++) if (vis(P[j], cam, 0.05)) vu++;
    if (vu < n * 0.6) return;
    var S = ligneEcran(P, n), L = [0];
    for (j = 1; j < n; j++) L.push(L[j - 1] + Math.hypot(S[j][0] - S[j - 1][0], S[j][1] - S[j - 1][1]));
    var lim = L[n - 1] * p, w = (a.w || 3) * Math.min(1.25, Math.max(0.8, Math.sqrt(cam.k / 3)));
    var pts = [S[0]];
    for (j = 1; j < n; j++) {
      if (L[j] <= lim) { pts.push(S[j]); continue; }
      var f = (lim - L[j - 1]) / (L[j] - L[j - 1] || 1);
      pts.push([S[j - 1][0] + (S[j][0] - S[j - 1][0]) * f, S[j - 1][1] + (S[j][1] - S[j - 1][1]) * f]);
      break;
    }
    if (pts.length < 2) return;
    var e = pts[pts.length - 1], q = pts[pts.length - 2];
    var ang = Math.atan2(e[1] - q[1], e[0] - q[0]), hl = a.nohead ? 0 : w * 3.2;
    var base = [e[0] - Math.cos(ang) * hl * 0.6, e[1] - Math.sin(ang) * hl * 0.6];
    ctx.save();
    ctx.globalAlpha = al;
    ctx.lineCap = "round"; ctx.lineJoin = "round";
    if (a.dash) ctx.setLineDash([w * 2.4, w * 1.8]);
    for (var pass = 0; pass < 2; pass++) {
      ctx.strokeStyle = pass ? a.col : "rgba(247,243,234,.9)";
      ctx.lineWidth = pass ? w : w + 3.2;
      ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
      for (j = 1; j < pts.length - 1; j++) ctx.lineTo(pts[j][0], pts[j][1]);
      ctx.lineTo(base[0], base[1]);
      ctx.stroke();
    }
    ctx.setLineDash([]);
    if (a.nohead) { ctx.restore(); return; }
    ctx.fillStyle = a.col; ctx.strokeStyle = "rgba(247,243,234,.9)"; ctx.lineWidth = 1.6;
    ctx.beginPath();
    ctx.moveTo(e[0], e[1]);
    ctx.lineTo(e[0] - Math.cos(ang - 0.45) * hl, e[1] - Math.sin(ang - 0.45) * hl);
    ctx.lineTo(e[0] - Math.cos(ang + 0.45) * hl, e[1] - Math.sin(ang + 0.45) * hl);
    ctx.closePath(); ctx.stroke(); ctx.fill();
    ctx.restore();
  }
  function texte(t, x, y, opt) {
    ctx.font = opt.font;
    ctx.textAlign = opt.align || "center"; ctx.textBaseline = "middle";
    var lignes = String(t).split("\n"), lh = opt.lh || 14;
    lignes.forEach(function (l, j) {
      var yy = y + (j - (lignes.length - 1) / 2) * lh;
      if (opt.halo) { ctx.lineWidth = 3.4; ctx.strokeStyle = opt.halo; ctx.lineJoin = "round"; ctx.strokeText(l, x, yy); }
      ctx.fillStyle = opt.col; ctx.fillText(l, x, yy);
    });
  }
  function alphaMembre(i, u, id, cle) {
    var ici = SC[i][cle].indexOf(id) >= 0, avant = i > 0 && SC[i - 1][cle].indexOf(id) >= 0;
    if (ici) return avant ? 1 : clamp01((u - cdelay(i) * 0.6) / 0.8);
    return avant ? 1 - clamp01(u / 0.7) : 0;
  }
  function rendre(t) {
    if (!W) return;
    var cam = camAt(t), i = cam.i, u = cam.u;
    var OFF = W >= 640 ? Math.min(W * 0.13, 170) : 0;
    proj.rotate([-cam.c[0], -cam.c[1]]).scale(R0 * cam.k).translate([W / 2 + OFF, H / 2]);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.fillStyle = PAPER; ctx.fillRect(0, 0, W, H);
    var dpx = R0 * cam.k * Math.PI / 180, fin = dpx < 6 ? "g" : (dpx < 26 ? "m" : "f");
    var key = cam.c[0].toFixed(5) + "," + cam.c[1].toFixed(5) + "," + cam.k.toFixed(5) + "," + W + "," + H + "," + fin;
    useCache = key === prevKey;
    if (useCache && cacheKey !== key) { cache = {}; cacheKey = key; }
    prevKey = key;
    // mer et graticule
    var SPH = trace("_sph", { type: "Sphere" });
    var R = R0 * cam.k, gr = ctx.createRadialGradient(W / 2 + OFF - R * 0.3, H / 2 - R * 0.35, R * 0.1, W / 2 + OFF, H / 2, R * 1.02);
    gr.addColorStop(0, "#E6EEF2"); gr.addColorStop(1, "#C9D9E1");
    ctx.fillStyle = cam.k > 3 ? SEA : gr; remplir(SPH);
    var GR = trace("_grat", grat); ctx.strokeStyle = "rgba(23,35,63,.07)"; ctx.lineWidth = 0.7; contour(GR);
    // pièces
    var vueAng = Math.asin(Math.min(1, Math.hypot(W, H) / 2 / R));
    var t0 = cdelay(i), cx = i === 0 ? 1 : ease((u - t0) / 1.6);
    var A = i > 0 ? STY[i - 1] : STY[0], B = STY[i];
    var bord = cam.k > 6 ? 0.8 : 0.55;
    for (var j = 0; j < PIECES.length; j++) {
      var p = PIECES[j];
      if (p.clip) continue;
      var s = same(A[j], B[j]) ? B[j] : mix(A[j], B[j], cx, tmp);
      if (s[3] < 0.003 && s[7] < 0.003) continue;
      if (d3.geoDistance(p.c, cam.c) - p.r > Math.min(Math.PI / 2, vueAng) + 0.05) continue;
      var tr = trace(p.id, p[fin]);
      if (!tr) continue;
      if (s[3] > 0.003) { ctx.fillStyle = rgba(s, 0); remplir(tr); }
      if (s[7] > 0.003) { ctx.save(); ctx.globalAlpha = s[7]; ctx.fillStyle = motif([s[4] | 0, s[5] | 0, s[6] | 0]); remplir(tr); ctx.restore(); }
      ctx.lineWidth = bord; ctx.strokeStyle = p.ov ? "rgba(255,255,255," + (0.75 * Math.max(s[3], s[7])).toFixed(2) + ")" : EDGE; contour(tr);
    }
    // front de l'Est et territoire occupé
    var fr = frontAt(i, u);
    if (fr && fr.al > 0.003) {
      var P = fr.P, n = P.length, sov = PIECES[IDX.sov41];
      if (fr.occ > 0.003 && sov) {
        var poly = P.slice();
        var nord = P[0], sud = P[n - 1];
        poly.push([sud[0], 42.5], [18.5, 42.5], [18.5, 62.5], [nord[0], 62.5], nord);
        ctx.save();
        var tc = trace("sov41", sov[fin]);
        if (tc) decouper(tc); else { ctx.beginPath(); ctx.rect(0, 0, 0, 0); ctx.clip(); }
        ctx.beginPath(); path({ type: "Polygon", coordinates: [poly] });
        ctx.globalAlpha = fr.al * fr.occ; ctx.fillStyle = C.occ || "#B8564C"; ctx.fill();
        ctx.restore();
      }
      var S = [];
      for (var q = 0; q < n; q++) if (vis(P[q], cam)) S.push(proj(P[q])); else S.push(null);
      ctx.save(); ctx.globalAlpha = fr.al; ctx.lineJoin = "round"; ctx.lineCap = "round";
      for (var pass = 0; pass < 2; pass++) {
        ctx.strokeStyle = pass ? "#2B0E0C" : "rgba(247,243,234,.95)"; ctx.lineWidth = pass ? 2.6 : 5.6;
        ctx.beginPath(); var on = false;
        S.forEach(function (pt) { if (!pt) { on = false; return; } if (on) ctx.lineTo(pt[0], pt[1]); else { ctx.moveTo(pt[0], pt[1]); on = true; } });
        ctx.stroke();
      }
      ctx.restore();
    }
    // flèches : celles de la scène précédente s'effacent, les nouvelles se tracent
    if (i > 0) SC[i - 1].arrows.forEach(function (a) {
      if (SC[i].arrows.some(function (b) { return b.id === a.id; })) return;
      fleche(a, cam, 1, 1 - clamp01(u / 0.8));
    });
    SC[i].arrows.forEach(function (a, k) {
      var deja = i > 0 && SC[i - 1].arrows.some(function (b) { return b.id === a.id; });
      var d0 = cdelay(i) + 0.35 + k * (a.dt != null ? a.dt : 0.45);
      fleche(a, cam, deja ? 1 : ease((u - d0) / (a.dur || 1.9)), 1);
    });
    // repères d'événements (pastilles qui pulsent)
    var ids = SC[i].pins.concat(i > 0 ? SC[i - 1].pins : []);
    ids.forEach(function (id, k) {
      if (ids.indexOf(id) !== k) return;
      var L = LB[id], al = alphaMembre(i, u, id, "pins");
      if (!L || al <= 0 || !vis(L.p, cam)) return;
      var xy = proj(L.p), ph = ((t * 0.8) % 1);
      ctx.save(); ctx.globalAlpha = al;
      ctx.beginPath(); ctx.arc(xy[0], xy[1], 6 + ph * 16, 0, 2 * Math.PI);
      ctx.strokeStyle = "rgba(142,47,42," + (0.55 * (1 - ph)).toFixed(2) + ")"; ctx.lineWidth = 2.2; ctx.stroke();
      ctx.beginPath(); ctx.arc(xy[0], xy[1], 5.5, 0, 2 * Math.PI);
      ctx.fillStyle = "#8E2F2A"; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = "#fff"; ctx.stroke();
      var dx = L.dx != null ? (L.dx < 0 ? -11 : (L.dx === 0 ? 0 : 11)) : 11, nomP = L[LANG] || L.fr;
      texte(nomP, xy[0] + dx, xy[1] + (L.dx === 0 ? (L.dy || -16) : 0), { font: "700 " + Math.round((W < 640 ? 13 : 14)) + "px Inter, system-ui, sans-serif",
        col: "#8E2F2A", halo: "rgba(247,243,234,.96)", align: dx < 0 ? "right" : (dx === 0 ? "center" : "left"), lh: 15 });
      ctx.restore();
    });
    // étiquettes
    var lids = SC[i].labels.concat(i > 0 ? SC[i - 1].labels : []);
    var petit = W < 640;
    lids.forEach(function (id, k) {
      if (lids.indexOf(id) !== k || SC[i].pins.indexOf(id) >= 0) return;
      var L = LB[id], al = alphaMembre(i, u, id, "labels");
      if (!L || al <= 0 || !vis(L.p, cam, 0.12)) return;
      var xy = proj(L.p), nom = L[LANG] || L.fr, z = petit ? 0.88 : 1;
      ctx.save(); ctx.globalAlpha = al;
      if (L.t === "ville" || L.t === "evt") {
        ctx.beginPath(); ctx.arc(xy[0], xy[1], 3.2, 0, 2 * Math.PI); ctx.fillStyle = INK; ctx.fill();
        ctx.lineWidth = 1.4; ctx.strokeStyle = "#fff"; ctx.stroke();
        var dx = L.dx != null ? L.dx : 7, dy = L.dy || 0;
        texte(nom, xy[0] + dx, xy[1] + dy, { font: (L.t === "evt" ? "700 " : "600 ") + Math.round(12.5 * z) + "px Inter, system-ui, sans-serif",
          col: L.t === "evt" ? "#8E2F2A" : INK, halo: "rgba(247,243,234,.95)", align: dx < 0 ? "right" : (dx === 0 ? "center" : "left"), lh: 14 * z });
      } else if (L.t === "mer") {
        texte(nom, xy[0], xy[1], { font: "italic 500 " + Math.round(12 * z) + "px Georgia, serif", col: "#4F6F84", halo: null, lh: 14 * z });
      } else {
        var blanc = L.c === "w";
        texte(nom.toUpperCase(), xy[0], xy[1], { font: "700 " + Math.round((L.s || 12) * z) + "px Inter, system-ui, sans-serif", col: blanc ? "#fff" : INK,
          halo: blanc ? "rgba(23,35,63,.35)" : "rgba(247,243,234,.92)", lh: 14 * z });
      }
      ctx.restore();
    });
    // anneau de lumière autour du globe en vue lointaine
    if (cam.k < 1.6) {
      var SP2 = trace("_sph", { type: "Sphere" }); ctx.lineWidth = 1.2; ctx.strokeStyle = "rgba(23,35,63,.25)"; contour(SP2);
    }
    if (i !== lastScene) majLegende(i);
    var pct = t / TOT * 100;
    plein.style.width = pct + "%";
    if (document.activeElement !== range) range.value = t;
    $(".tps").textContent = mmss(t) + " / " + mmss(TOT);
  }
  function mmss(s) { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + ("0" + s % 60).slice(-2); }
  function ecrireLeg(s) {
      legD.textContent = s.date[LANG];
      legT.textContent = s.titre[LANG];
      legX.innerHTML = (s.texte[LANG] || "").replace(/\[hors\]/g, '<span class="hors">' + UI[LANG].hors + "</span>");
      legK.innerHTML = (s.cles || []).map(function (k) {
        var c = (C.cles || {})[k];
        if (!c) return "";
        var f = c.c[0], h = c.c[1], st;
        if (f === "line") st = "background:none;border:0;border-top:3px solid " + h + ";height:0;margin-top:5px";
        else if (h) st = "background:repeating-linear-gradient(45deg," + h + " 0 2px," + (f || "#F7F3EA") + " 2px 5px)";
        else st = "background:" + f;
        return '<span class="k"><i style="' + st + '"></i>' + c[LANG] + "</span>";
      }).join("");
      chipP.textContent = s.part ? (s.part + " · ") : "";
      chipD.textContent = (C.parties && C.parties[s.part]) ? C.parties[s.part][LANG] : "";
  }
  // sur téléphone, la légende est sous la carte : on lui donne la hauteur de la plus longue,
  // pour que rien ne saute d'une date à l'autre
  function hauteurLeg() {
    leg.style.minHeight = "";
    if (!root.classList.contains("etroit")) return;
    var m = 0;
    SC.forEach(function (s) { ecrireLeg(s); m = Math.max(m, leg.offsetHeight); });
    leg.style.minHeight = m + "px";
    ecrireLeg(SC[Math.max(0, lastScene)]);
  }
  function majLegende(i) {
    var s = SC[i], fade = lastScene !== -1;
    lastScene = i;
    var ecrire = function () { ecrireLeg(s); leg.classList.remove("out"); hauteur(); };
    if (fade) { leg.classList.add("out"); clearTimeout(majLegende.t); majLegende.t = setTimeout(ecrire, 160); } else ecrire();
    var ts = ticks.children;
    for (var k = 0; k < ts.length; k++) ts[k].classList.toggle("on", k <= i);
    if (playing && voix.on) parler(i);
  }

  /* ---------- lecture ---------- */
  var arret = { on: false }, voix = { on: false, parle: false };
  function boucle(now) {
    if (!playing) return;
    var dt = Math.min(0.1, (now - last) / 1000); last = now;
    var i = sceneAt(T), fin = START[i + 1];
    var nt = T + dt;
    if (voix.on && voix.parle && nt >= fin - 0.05) nt = Math.max(T, fin - 0.05);
    if (arret.on && T < fin - 0.02 && nt >= fin - 0.02 && i < N - 1) { T = fin - 0.02; rendre(T); pause(); return; }
    T = Math.min(TOT, nt);
    var a0 = performance.now();
    rendre(T);
    // appareil lent : on baisse la définition plutôt que la fluidité
    lent = lent * 0.92 + (performance.now() - a0) * 0.08;
    if (lent > 30 && DPRMAX > 1.25) { DPRMAX = 1.25; lent = 0; taille(); }
    if (T >= TOT) { pause(); return; }
    requestAnimationFrame(boucle);
  }
  function lire() {
    if (T >= TOT - 0.05) T = 0;
    if (arret.on) { var i = sceneAt(T); if (T >= START[i + 1] - 0.05 && i < N - 1) T = START[i + 1]; }
    playing = true; last = performance.now();
    $(".go").classList.add("cache");
    $(".b-lire").textContent = "⏸"; $(".b-lire").setAttribute("aria-label", UI[LANG].pause);
    if (voix.on) parler(sceneAt(T), true);
    requestAnimationFrame(boucle);
  }
  function pause() {
    playing = false;
    if (lecteur && !lecteur.paused) lecteur.pause();
    if (window.speechSynthesis && speechSynthesis.speaking) { speechSynthesis.cancel(); voix.parle = false; }
    $(".b-lire").textContent = "▶"; $(".b-lire").setAttribute("aria-label", UI[LANG].lire);
  }
  function aller(t) {
    T = Math.max(0, Math.min(TOT, t));
    taire();
    $(".go").classList.add("cache");
    rendre(T);
  }
  // voix enregistrée (Henri en français, Ryan en anglais) ; à défaut, la voix du téléphone.
  // Un seul élément audio, réutilisé : débloqué par le premier geste, il peut ensuite enchaîner les scènes.
  var lecteur = window.Audio ? new Audio() : null, lecteurScene = -1, lecteurLang = null;
  if (lecteur) lecteur.preload = "auto";
  function taire() {
    if (lecteur) { lecteur.pause(); lecteurScene = -1; }
    if (window.speechSynthesis) speechSynthesis.cancel();
    voix.parle = false;
  }
  function parler(i, reprendre) {
    var s = SC[i], src = s.voix && s.voix[LANG];
    if (reprendre && lecteur && lecteurScene === i && lecteurLang === LANG && lecteur.src && !lecteur.ended) {
      voix.parle = true;
      lecteur.play().catch(function () { voix.parle = false; });
      return;
    }
    taire();
    if (src && lecteur) {
      lecteurScene = i; lecteurLang = LANG; voix.parle = true;
      lecteur.onended = function () { if (lecteurScene === i) voix.parle = false; };
      lecteur.onerror = function () { if (lecteurScene === i) { lecteurScene = -1; synthese(i); } };
      lecteur.src = src;
      lecteur.play().catch(function () { if (lecteurScene === i) { lecteurScene = -1; synthese(i); } });
      return;
    }
    synthese(i);
  }
  function synthese(i) {
    if (!window.speechSynthesis) { voix.parle = false; return; }
    speechSynthesis.cancel();
    var s = SC[i], txt = s.date[LANG] + ". " + s.titre[LANG] + ". " + ((s.evt && s.evt[LANG]) || s.texte[LANG] || "").replace(/\[hors\]/g, "");
    var ut = new SpeechSynthesisUtterance(txt);
    ut.lang = LANG === "fr" ? "fr-FR" : "en-GB";
    var vs = speechSynthesis.getVoices().filter(function (v) { return v.lang && v.lang.toLowerCase().indexOf(LANG) === 0; });
    if (vs.length) ut.voice = vs.filter(function (v) { return /google|natural|premium|enhanced/i.test(v.name); })[0] || vs[0];
    ut.rate = 1.02;
    voix.parle = true;
    ut.onend = ut.onerror = function () { voix.parle = false; };
    speechSynthesis.speak(ut);
  }
  $(".b-lire").addEventListener("click", function () { playing ? pause() : lire(); });
  $(".go").addEventListener("click", lire);
  $(".b-prec").addEventListener("click", function () {
    var i = sceneAt(T);
    var cible = (T - START[i] > 1.2 || i === 0) ? START[i] : START[i - 1];
    aller(cible + 0.001);
  });
  $(".b-suiv").addEventListener("click", function () { var i = sceneAt(T); aller(i < N - 1 ? START[i + 1] + 0.001 : TOT); });
  range.addEventListener("input", function () { aller(+range.value); });
  $(".o-arret").addEventListener("change", function (e) { arret.on = e.target.checked; });
  $(".o-voix").addEventListener("change", function (e) {
    if (!window.speechSynthesis && !lecteur) { e.target.checked = false; alert(UI[LANG].sansVoix); return; }
    voix.on = e.target.checked;
    if (!voix.on) taire(); else if (playing) parler(sceneAt(T));
  });
  $(".b-plein").addEventListener("click", function () {
    if (document.fullscreenElement) { document.exitFullscreen(); return; }
    if (root.requestFullscreen) root.requestFullscreen().catch(function () { window.open(location.pathname + "?lang=" + LANG, "_blank"); });
    else window.open(location.pathname + "?lang=" + LANG, "_blank");
  });
  document.addEventListener("fullscreenchange", function () { setTimeout(taille, 60); });
  document.addEventListener("keydown", function (e) {
    if (e.target.tagName === "INPUT" && e.target.type !== "range") return;
    if (e.key === " ") { e.preventDefault(); playing ? pause() : lire(); }
    else if (e.key === "ArrowRight") $(".b-suiv").click();
    else if (e.key === "ArrowLeft") $(".b-prec").click();
  });

  /* ---------- langue, intégration ---------- */
  function textes() {
    var u = UI[LANG];
    $(".go-t").textContent = u.lancer;
    $(".b-prec").setAttribute("aria-label", u.prec); $(".b-prec").title = u.prec;
    $(".b-suiv").setAttribute("aria-label", u.suiv); $(".b-suiv").title = u.suiv;
    $(".b-lire").setAttribute("aria-label", playing ? u.pause : u.lire);
    $(".b-plein").setAttribute("aria-label", u.plein); $(".b-plein").title = u.plein;
    $(".o-arret-t").textContent = u.arret; $(".o-voix-t").textContent = u.voix;
    document.documentElement.lang = LANG;
    document.title = C.titre[LANG];
    lastScene = -1; hauteurLeg(); rendre(T);
  }
  function hauteur() {
    if (!EMBED || window.parent === window) return;
    window.parent.postMessage({ type: "carte-h", code: C.code, h: Math.ceil(root.getBoundingClientRect().height) + 2 }, "*");
  }
  window.addEventListener("message", function (e) {
    var d = e.data || {};
    if (d.type === "carte-lang" && (d.lang === "fr" || d.lang === "en") && d.lang !== LANG) {
      LANG = d.lang;
      taire();
      textes();
    }
  });
  window.addEventListener("resize", function () { clearTimeout(taille.t); taille.t = setTimeout(taille, 80); });
  textes();
  taille();
  if (Q.get("t")) aller(+Q.get("t"));
  window.CARTE_API = { aller: aller, rendre: rendre, total: TOT, starts: START, lire: lire, pause: pause, t: function () { return T; },
    voix: function () { return { src: lecteur && lecteur.src, enPause: lecteur && lecteur.paused, parle: voix.parle }; } };
})();
