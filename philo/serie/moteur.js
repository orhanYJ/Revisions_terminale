/* Série philo — moteur du lecteur.
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  var C = { iv: "#f3efe4", iv2: "#d9d2c0", sa: "#e8b25a", sa2: "#c8811f", ca: "#c2614c", te: "#4f9a8e", eau: "#74b9d8", nuit: "#0e1525" };

  /* ---------- outils ---------- */
  function h(tag, cls, parent, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    if (parent) parent.appendChild(e);
    return e;
  }
  function sv(tag, at, parent, txt) {
    var e = document.createElementNS(NS, tag);
    for (var k in at) e.setAttribute(k, at[k]);
    if (txt != null) e.textContent = txt;
    if (parent) parent.appendChild(e);
    return e;
  }
  function cl(x, a, b) { return x < a ? a : x > b ? b : x; }
  function E(x) { x = cl(x, 0, 1); return 1 - Math.pow(1 - x, 3); }
  function EIO(x) { x = cl(x, 0, 1); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }
  function EB(x) { x = cl(x, 0, 1); var c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); }
  function P(t, t0, d) { return cl((t - t0) / d, 0, 1); }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function fmt(t) { t = Math.max(0, Math.floor(t)); return Math.floor(t / 60) + ":" + ("0" + t % 60).slice(-2); }
  function alea(n) { var x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }
  function op(e, v) { e.style.opacity = v; }
  function tr(e, v) { e.style.transform = v; }
  function trace(e, p) { // dessine un tracé SVG de 0 à p
    if (!e._L) { e._L = e.getTotalLength ? e.getTotalLength() || 1 : 1; e.style.strokeDasharray = e._L; }
    e.style.strokeDashoffset = e._L * (1 - cl(p, 0, 1));
  }
  // lettres une à une (les mots restent insécables)
  function insec(s) { return String(s).replace(/ ([?!:;»])/g, "\u00a0$1").replace(/« /g, "«\u00a0"); }
  function lettres(el, txt) {
    var out = [];
    insec(txt).split(/([ \t\n]+)/).forEach(function (m) {
      if (/^[ \t\n]+$/.test(m)) { el.appendChild(document.createTextNode(" ")); return; }
      var w = h("span", "mot-l", el);
      Array.from(m).forEach(function (c) { out.push(h("span", "lettre", w, esc(c))); });
    });
    return out;
  }
  function mots(el, txt, cls) {
    var out = [];
    insec(txt).split(/[ \t\n]+/).forEach(function (m, i) {
      if (i) el.appendChild(document.createTextNode(" "));
      out.push(h("span", cls || "mot-l", el, esc(m)));
    });
    return out;
  }
  function animLettres(sp, tl, debut, pas, duree, flou) {
    for (var i = 0; i < sp.length; i++) {
      var p = E(P(tl, debut + i * pas, duree));
      sp[i].style.opacity = p;
      sp[i].style.transform = "translateY(" + ((1 - p) * 0.45).toFixed(3) + "em)";
      if (flou) sp[i].style.filter = p < 1 ? "blur(" + ((1 - p) * 6).toFixed(1) + "px)" : "none";
    }
  }
  // mots clés d'un visuel : chaque span dont le mot commence comme une clé s'allume quand la voix la prononce
  function nrm(x) { return String(x).toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z]/g, ""); }
  function cles(v, spans) {
    if (!v.kt) return [];
    var out = [];
    spans.forEach(function (sp) {
      var w = nrm(sp.textContent);
      Object.keys(v.kt).forEach(function (k) {
        var nk = nrm(k);
        if (w && nk && w.indexOf(nk.slice(0, Math.max(4, nk.length - 2))) === 0) out.push({ sp: motSeul(sp), t: v.kt[k] });
      });
    });
    return out;
  }
  // n'allume que le mot, pas la ponctuation collée (« naturel : » → « naturel » souligné, « : » normal)
  function motSeul(sp) {
    if (sp._mot) return sp._mot;
    var m = sp.textContent.match(/^([«"'(\s\u00a0\u202f]*)(.*?)([\s\u00a0\u202f]*[.,;:!?»")…]*)$/);
    if (!m || (!m[1] && !m[3])) { sp._mot = sp; return sp; }
    sp.textContent = "";
    if (m[1]) sp.appendChild(document.createTextNode(m[1]));
    var in_ = h("span", "cle", sp, esc(m[2]));
    if (m[3]) sp.appendChild(document.createTextNode(m[3]));
    sp._mot = in_;
    return in_;
  }
  function allume(lst, t) {
    lst.forEach(function (c) {
      var p = P(t, c.t, .35), f = P(t, c.t + .35, 1.4);
      if (p <= 0) { c.sp.style.color = ""; c.sp.style.textShadow = ""; c.sp.style.backgroundSize = "0% 3px"; return; }
      c.sp.style.color = C.sa;
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(232,178,90," + (0.7 * (1 - f)).toFixed(2) + ")";
      c.sp.style.backgroundSize = (100 * E(p)).toFixed(0) + "% 3px";
    });
  }

  // étape k d'un visuel : instant (repère {id.k}) ou, à défaut, une valeur de repli
  function et(v, k, repli) { return v.et && v.et[k] != null ? v.et[k] : v.t0 + repli; }

  /* ---------- icônes et illustrations ---------- */
  var ICONES = {
    porte: ["M30 88 V16 H70 V88", "M30 16 L58 24 V94 L30 88", "M50 56 h0.5", "M78 52 H96 M88 44 L96 52 L88 60"],
    chemins: ["M50 94 V58", "M50 58 C50 40 30 36 22 12", "M50 58 C50 40 70 36 78 12", "M16 20 L22 10 L30 18", "M70 18 L78 10 L84 20"],
    colonnes: ["M10 34 L50 12 L90 34 Z", "M14 40 H86", "M22 44 V82 M40 44 V82 M60 44 V82 M78 44 V82", "M10 88 H90 M14 82 H86"]
  };
  function icone(nom, parent) {
    var s = sv("svg", { viewBox: "0 0 100 100" }, parent);
    return (ICONES[nom] || []).map(function (d) {
      return sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 4.5, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    });
  }
  function silhouette(g, x, y, k) { // personnage stylisé (tête + toge)
    k = k || 1;
    var gr = sv("g", { transform: "translate(" + x + "," + y + ") scale(" + k + ")" }, g);
    var tete = sv("circle", { cx: 0, cy: -150, r: 26, fill: C.iv }, gr);
    var corps = sv("path", { d: "M-42 -112 Q0 -128 42 -112 L58 40 Q0 52 -58 40 Z", fill: C.iv }, gr);
    return { g: gr, tete: tete, corps: corps };
  }
  function pieton(g) { // pictogramme qui marche
    var gr = sv("g", {}, g);
    var at = { stroke: C.iv, "stroke-width": 11, "stroke-linecap": "round", fill: "none" };
    var tete = sv("circle", { cx: 0, cy: -122, r: 17, fill: C.iv }, gr);
    var tronc = sv("path", Object.assign({ d: "M0 -98 L0 -50" }, at), gr);
    var j1 = sv("path", Object.assign({ d: "" }, at), gr), j2 = sv("path", Object.assign({ d: "" }, at), gr);
    var b1 = sv("path", Object.assign({ d: "" }, at), gr), b2 = sv("path", Object.assign({ d: "" }, at), gr);
    return {
      g: gr, pose: function (x, y, phase, ampl) {
        gr.setAttribute("transform", "translate(" + x + "," + y + ")");
        var a = ampl ? Math.sin(phase) * ampl : 0.2, b = -a;
        function m(ang, l, y0) { return "M0 " + y0 + " L" + (Math.sin(ang) * l).toFixed(1) + " " + (y0 + Math.cos(ang) * l).toFixed(1); }
        j1.setAttribute("d", m(a, 50, -48)); j2.setAttribute("d", m(b, 50, -48));
        b1.setAttribute("d", m(b * 0.8, 40, -92)); b2.setAttribute("d", m(a * 0.8, 40, -92));
      }
    };
  }
  function etiquette(g, x, y, txt, opt) {
    opt = opt || {};
    return sv("text", { x: x, y: y, "text-anchor": opt.ancre || "middle", fill: opt.c || C.iv, "font-size": opt.fs || 26,
      "font-weight": opt.fw || 600, "letter-spacing": opt.ls || 0, class: opt.cls || "" }, g, txt);
  }

  function pointe(g, chemin, couleur, taille) {
    taille = taille || 18;
    var tri = sv("path", { d: "", fill: couleur }, g), fait = false;
    return function () {
      if (fait) return tri;
      var L = chemin.getTotalLength();
      if (!L) return tri;
      var a = chemin.getPointAtLength(L), b = chemin.getPointAtLength(Math.max(0, L - 4));
      var ux = a.x - b.x, uy = a.y - b.y, n = Math.hypot(ux, uy) || 1;
      ux /= n; uy /= n;
      var px = -uy, py = ux, k = taille, l = taille * 0.55;
      var tip = [a.x + ux * k * 0.35, a.y + uy * k * 0.35];
      tri.setAttribute("d", "M" + tip[0].toFixed(1) + " " + tip[1].toFixed(1) +
        " L" + (tip[0] - ux * k + px * l).toFixed(1) + " " + (tip[1] - uy * k + py * l).toFixed(1) +
        " L" + (tip[0] - ux * k * 0.72).toFixed(1) + " " + (tip[1] - uy * k * 0.72).toFixed(1) +
        " L" + (tip[0] - ux * k - px * l).toFixed(1) + " " + (tip[1] - uy * k - py * l).toFixed(1) + " Z");
      fait = true;
      return tri;
    };
  }

  var ILLU = {};

  ILLU.icones = function (s, v) {
    var xs = [150, 450, 750], lab = ["tes habits", "ta musique", "ton téléphone"], items = [];
    var dessins = [
      ["M-60 -40 L-30 -60 Q0 -44 30 -60 L60 -40 L47 -12 L32 -20 L32 60 L-32 60 L-32 -20 L-47 -12 Z"],
      ["M-9 40 V-44 L51 -58 V26", "M-9 -44 L51 -58", "M-25 40 a16 13 0 1 0 32 0 a16 13 0 1 0 -32 0", "M35 26 a16 13 0 1 0 32 0 a16 13 0 1 0 -32 0"],
      ["M-38 -56 Q-38 -68 -26 -68 H26 Q38 -68 38 -56 V56 Q38 68 26 68 H-26 Q-38 68 -38 56 Z", "M-28 -52 H28 V44 H-28 Z", "M-6 56 H6"]
    ];
    xs.forEach(function (x, i) {
      var g = sv("g", { transform: "translate(" + x + ",150)" }, s);
      var cer = sv("circle", { r: 112, fill: "rgba(255,255,255,.04)", stroke: "rgba(243,239,228,.25)", "stroke-width": 2 }, g);
      var tr_ = dessins[i].map(function (d) { return sv("path", { d: d, fill: "none", stroke: C.iv, "stroke-width": 5, "stroke-linejoin": "round", "stroke-linecap": "round" }, g); });
      var marque = i < 2
        ? sv("path", { d: "M66 -96 l16 16 l30 -34", fill: "none", stroke: C.sa, "stroke-width": 9, "stroke-linecap": "round", "stroke-linejoin": "round" }, g)
        : sv("text", { x: 92, y: -62, "text-anchor": "middle", fill: C.ca, "font-size": 96, "font-weight": 700, class: "ser" }, g, "?");
      var t = etiquette(s, x, 312, lab[i], { fs: 28, fw: 500, c: C.iv2 });
      items.push({ g: g, cer: cer, tr: tr_, marque: marque, t: t });
    });
    return function (t, st) {
      items.forEach(function (it, i) {
        var t0 = et(v, String(i + 1), 0.4 + i * 1.5);
        var p = P(t, t0, 1.1);
        it.tr.forEach(function (e) { trace(e, p); });
        op(it.t, E(P(t, t0 + .2, .6)));
        it.cer.setAttribute("stroke", p > 0 ? "rgba(232,178,90," + (0.25 + 0.5 * E(p)) + ")" : "rgba(243,239,228,.25)");
        var m = E(P(t, t0 + .7, .5));
        if (i < 2) trace(it.marque, m);
        else {
          op(it.marque, m);
          tr(it.marque, "rotate(" + (Math.sin(t * 3.2) * 9).toFixed(2) + "deg) scale(" + (0.6 + 0.4 * EB(m)) + ")");
          it.marque.style.transformOrigin = "92px -90px";
        }
      });
    };
  };

  ILLU.agora = function (s, v) {
    var fond = sv("g", { opacity: .55 }, s), traits = [];
    traits.push(sv("path", { d: "M80 420 H920", stroke: "rgba(243,239,228,.4)", "stroke-width": 3, fill: "none" }, fond));
    traits.push(sv("path", { d: "M150 120 L500 40 L850 120 Z", stroke: "rgba(232,178,90,.6)", "stroke-width": 3, fill: "none" }, fond));
    [190, 300, 410, 590, 700, 810].forEach(function (x) {
      traits.push(sv("path", { d: "M" + (x - 18) + " 140 H" + (x + 18) + " M" + (x - 12) + " 140 V400 M" + (x + 12) + " 140 V400 M" + (x - 20) + " 400 H" + (x + 20),
        stroke: "rgba(243,239,228,.32)", "stroke-width": 3, fill: "none" }, fond));
    });
    var A = silhouette(s, 360, 380, 1), B = silhouette(s, 640, 380, 1);
    var lA = etiquette(s, 360, 150, "CITOYEN", { c: C.sa, ls: 4, fs: 24 });
    var sA = etiquette(s, 360, 180, "vote · parle · décide", { c: C.iv2, fs: 20, fw: 400 });
    var lB = etiquette(s, 640, 150, "ESCLAVE", { c: C.ca, ls: 4, fs: 24 });
    var chaine = sv("g", {}, s), maillons = [];
    for (var i = 0; i < 9; i++) {
      maillons.push(sv("ellipse", { cx: 690 + i * 22, cy: 330 + i * 9, rx: 12, ry: 7, fill: "none", stroke: C.ca, "stroke-width": 4,
        transform: "rotate(" + (i % 2 ? 60 : 20) + " " + (690 + i * 22) + " " + (330 + i * 9) + ")" }, chaine));
    }
    var pieu = sv("path", { d: "M893 418 V395", stroke: C.ca, "stroke-width": 8, "stroke-linecap": "round" }, chaine);
    // la boucle fait le tour de la tête du citoyen et revient vers lui : il s'appartient
    var boucle = sv("path", { d: "M318 262 A48 48 0 1 1 398 258", fill: "none", stroke: C.sa, "stroke-width": 5, "stroke-linecap": "round" }, s);
    var pA = pointe(s, boucle, C.sa, 20);
    var tA = etiquette(s, 360, 158, "s'appartient", { c: C.sa, fs: 32, cls: "ser" });
    var fl = sv("path", { d: "M682 196 C740 120 830 110 922 136", fill: "none", stroke: C.ca, "stroke-width": 5, "stroke-linecap": "round" }, s);
    var pB = pointe(s, fl, C.ca, 20);
    var tB = etiquette(s, 800, 92, "appartient à un autre", { c: C.ca, fs: 28, cls: "ser" });
    return function (t, st) {
      traits.forEach(function (e, i) { trace(e, P(t, v.t0 + i * .12, 1.4)); });
      var a = E(P(t, v.t0 + .5, .8));
      [A, B].forEach(function (S, i) { op(S.g, a); S.g.setAttribute("transform", "translate(" + (i ? 640 : 360) + "," + (380 + (1 - a) * 30) + ")"); });
      var e1 = et(v, "1", 3), e2 = et(v, "2", 6), e3 = et(v, "3", 9);
      var p1 = E(P(t, e1, .7));

      A.tete.setAttribute("fill", p1 > 0 ? C.sa : C.iv); A.corps.setAttribute("fill", p1 > 0 ? C.sa : C.iv);
      A.corps.style.opacity = A.tete.style.opacity = 0.75 + 0.25 * p1;
      var p2 = P(t, e2, 1.6);
      maillons.forEach(function (m, i) { op(m, E(P(p2, i / 11, .2))); });
      op(pieu, E(P(p2, .85, .15)));
      B.corps.setAttribute("fill", p2 > 0 ? "#9a9688" : C.iv); B.tete.setAttribute("fill", p2 > 0 ? "#9a9688" : C.iv);
      var p3 = P(t, e3, 1.2);
      op(fond, .55 - .35 * E(P(t, e3, .8))); op(lA, p1 * (1 - E(P(t, e3, .5)))); op(sA, E(P(t, e1 + .4, .7)) * (1 - E(P(t, e3, .5)))); op(lB, E(P(t, e2, .6)) * (1 - E(P(t, e3, .5))));
      trace(boucle, p3); op(boucle, p3 > 0 ? 1 : 0); op(pA(), E(P(p3, .9, .1))); op(tA, E(P(t, e3 + .6, .6)));
      var p4 = P(t, e3 + 1.2, 1.0);
      trace(fl, p4); op(fl, p4 > 0 ? 1 : 0); op(pB(), E(P(p4, .9, .1))); op(tB, E(P(t, e3 + 1.6, .6)));
    };
  };

  ILLU.racine = function (s, v) {
    var racine = sv("g", {}, s);
    sv("rect", { x: 390, y: 290, width: 220, height: 62, rx: 31, fill: "rgba(232,178,90,.12)", stroke: C.sa, "stroke-width": 2 }, racine);
    var rx = etiquette(racine, 500, 331, null, { c: C.sa, fs: 32, cls: "ser" });
    [["*h", 0, 32], ["1", 7, 19], ["leud", -7, 32], ["h", -13, 19], ["-", 13, 32]].forEach(function (m) {
      sv("tspan", { dy: m[1], "font-size": m[2] }, rx, m[0]);
    });
    etiquette(racine, 630, 328, "racine indo-européenne", { c: C.iv2, fs: 19, fw: 400, ancre: "start" });
    var sens = etiquette(s, 500, 400, "« le peuple »", { c: C.iv, fs: 38, cls: "ser" });
    var exp = etiquette(s, 500, 458, "libre = être des nôtres  ≠  l'étranger capturé", { c: C.iv2, fs: 26, fw: 400 });
    var br = [
      sv("path", { d: "M470 290 C440 200 280 220 200 150", fill: "none", stroke: C.sa, "stroke-width": 3 }, s),
      sv("path", { d: "M500 290 C500 230 500 180 500 140", fill: "none", stroke: C.sa, "stroke-width": 3 }, s),
      sv("path", { d: "M530 290 C560 200 720 220 800 150", fill: "none", stroke: C.sa, "stroke-width": 3 }, s)];
    var fe = [
      [etiquette(s, 200, 110, "ἐλεύθερος", { fs: 44, cls: "ser" }), etiquette(s, 200, 140, "grec", { fs: 20, fw: 400, c: C.iv2 })],
      [etiquette(s, 500, 100, "liber", { fs: 48, cls: "ser" }), etiquette(s, 500, 128, "latin", { fs: 20, fw: 400, c: C.iv2 })],
      [etiquette(s, 800, 110, "Leute", { fs: 44, cls: "ser" }), etiquette(s, 800, 140, "allemand · « les gens »", { fs: 20, fw: 400, c: C.iv2 })]];
    return function (t, st) {
      op(racine, E(P(t, v.t0 + .1, .6)));
      [0, 1].forEach(function (i) { trace(br[i], P(t, v.t0 + .5 + i * .3, 1.2)); fe[i].forEach(function (e) { op(e, E(P(t, v.t0 + 1.4 + i * .3, .6))); }); });
      var e1 = et(v, "1", 3), e2 = et(v, "2", 6), e3 = et(v, "3", 9);
      op(sens, E(P(t, e1, .7)));
      sens.setAttribute("fill", t > e1 ? "rgb(" + [243, 239 - 20 * Math.max(0, Math.sin((t - e1) * 2)), 228 - 80 * Math.max(0, Math.sin((t - e1) * 2))].map(Math.round) + ")" : C.iv);
      op(exp, E(P(t, e2, .8)));
      trace(br[2], P(t, e3, 1.0)); fe[2].forEach(function (e) { op(e, E(P(t, e3 + .8, .6))); });
    };
  };

  // eau : un même polygone passe du vase à la flaque
  ILLU.vase = function (s, v) {
    var cx = 400, prof = [[38, 40], [40, 92], [100, 140], [128, 200], [124, 270], [96, 336], [56, 382], [60, 400]];
    function bord(y) { // demi-largeur intérieure du vase à la hauteur y
      for (var i = 0; i < prof.length - 1; i++) {
        var a = prof[i], b = prof[i + 1];
        if (y >= a[1] && y <= b[1]) return a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) - 11;
      }
      return 30;
    }
    var N = 24, haut = 158, bas = 382;
    function formeVase(t) {
      var pts = [];
      for (var i = 0; i <= N; i++) { var x = -bord(haut) + 2 * bord(haut) * i / N; pts.push([cx + x, haut + 4 * Math.sin(t * 2.4 + i * 0.7)]); }
      for (i = 1; i <= N; i++) { var y = haut + (bas - haut) * i / N; pts.push([cx + bord(y), y]); }
      for (i = 1; i < N; i++) { pts.push([cx + bord(bas) - 2 * bord(bas) * i / N, bas]); }
      for (i = N; i >= 1; i--) { y = haut + (bas - haut) * i / N; pts.push([cx - bord(y), y]); }
      return pts;
    }
    function formeFlaque(t, k) {
      var pts = [], L = 340 * k + 30;
      for (var i = 0; i <= N; i++) { var x = -L + 2 * L * i / N; pts.push([cx + x, 404 - 10 * Math.cos(Math.PI * (x / L) / 2) + 2 * Math.sin(t * 3 + i)]); }
      for (i = 1; i <= N; i++) pts.push([cx + L + 6 * Math.sin(Math.PI * i / N), 404 + 14 * i / N]);
      for (i = 1; i < N; i++) pts.push([cx + L - 2 * L * i / N, 420]);
      for (i = N; i >= 1; i--) pts.push([cx - L - 6 * Math.sin(Math.PI * i / N), 404 + 14 * i / N]);
      return pts;
    }
    var sol = sv("path", { d: "M20 422 H780", stroke: "rgba(243,239,228,.35)", "stroke-width": 3 }, s);
    var defs = sv("defs", {}, s), gid = "eau" + v.id;
    var lg = sv("linearGradient", { id: gid, x1: 0, y1: 0, x2: 0, y2: 1 }, defs);
    sv("stop", { offset: 0, "stop-color": "#9fd3ea" }, lg); sv("stop", { offset: 1, "stop-color": "#2f6f93" }, lg);
    var eau = sv("path", { d: "", fill: "url(#" + gid + ")", opacity: .92 }, s);
    var d = "M" + (cx - 38) + " 40 L" + (cx - 40) + " 92 ";
    var dr = prof.map(function (p) { return (cx + p[0]) + " " + p[1]; });
    var dl = prof.slice().reverse().map(function (p) { return (cx - p[0]) + " " + p[1]; });
    var vase = sv("g", {}, s);
    var cont = sv("path", { d: "M" + dl.join(" L") + " M" + dr.join(" L"), fill: "none", stroke: C.sa, "stroke-width": 7, "stroke-linejoin": "round", "stroke-linecap": "round" }, vase);
    sv("path", { d: "M" + (cx - 128) + " 400 H" + (cx + 128), stroke: C.sa, "stroke-width": 7, "stroke-linecap": "round" }, vase);
    sv("path", { d: "M" + (cx - 56) + " 30 H" + (cx + 56), stroke: C.sa, "stroke-width": 7, "stroke-linecap": "round" }, vase);
    var lo = etiquette(s, 640, 210, "obstacle", { c: C.sa, fs: 30, cls: "ser" });
    var flo = sv("path", { d: "M600 220 C580 230 560 240 540 246", fill: "none", stroke: C.sa, "stroke-width": 3 }, s);
    var lib = etiquette(s, 400, 120, "liberté = absence d'obstacle", { c: C.iv, fs: 38, cls: "ser" });
    var gouttes = [];
    for (var i = 0; i < 14; i++) gouttes.push(sv("circle", { r: 5 + alea(i) * 5, fill: "#9fd3ea" }, s));
    return function (t, st) {
      var e1 = et(v, "1", 5), p = EIO(P(t, e1, 2.4));
      trace(cont, P(t, v.t0, 1.4)); op(sol, E(P(t, v.t0, .8)));
      var A = formeVase(t), B = formeFlaque(t, p);
      var pts = A.map(function (a, i) { var b = B[i]; return [a[0] + (b[0] - a[0]) * p, a[1] + (b[1] - a[1]) * p]; });
      eau.setAttribute("d", "M" + pts.map(function (q) { return q[0].toFixed(1) + " " + q[1].toFixed(1); }).join(" L") + " Z");
      op(eau, E(P(t, v.t0 + .8, .8)) * .92);
      op(vase, 1 - E(P(t, e1, 1.2)));
      tr(vase, "translateY(" + (-240 * EIO(P(t, e1, 1.4))) + "px)");
      op(lo, E(P(t, v.t0 + 1.4, .6)) * (1 - E(P(t, e1, .5)))); op(flo, lo.style.opacity);
      op(lib, E(P(t, e1 + 1.8, .8)));
      gouttes.forEach(function (g, i) {
        var tt = t - e1 - 0.3 - alea(i + 20) * 0.6;
        var vis = tt > 0 && tt < 1.4;
        op(g, vis ? 1 - tt / 1.4 : 0);
        if (vis) {
          var dir = i % 2 ? 1 : -1, vx = dir * (90 + alea(i + 3) * 160);
          g.setAttribute("cx", cx + vx * tt); g.setAttribute("cy", 300 - 140 * tt + 330 * tt * tt);
        }
      });
    };
  };

  ILLU.tonneaux = function (s, v) {
    var defs = sv("defs", {}, s);
    function tonneau(x, id) {
      var g = sv("g", { transform: "translate(" + x + ",0)" }, s);
      var forme = "M-92 180 Q-112 300 -92 420 L92 420 Q112 300 92 180 Z";
      var cp = sv("clipPath", { id: id }, defs); sv("path", { d: forme }, cp);
      var eau = sv("rect", { x: -120, y: 420, width: 240, height: 0, fill: C.eau, "clip-path": "url(#" + id + ")", opacity: .9 }, g);
      sv("path", { d: forme, fill: "none", stroke: "#b07a3c", "stroke-width": 7, "stroke-linejoin": "round" }, g);
      [210, 300, 390].forEach(function (y) { sv("path", { d: "M-100 " + y + " Q0 " + (y + 10) + " 100 " + y, fill: "none", stroke: "#8a5a2b", "stroke-width": 6 }, g); });
      sv("ellipse", { cx: 0, cy: 180, rx: 92, ry: 16, fill: "rgba(14,21,37,.6)", stroke: "#b07a3c", "stroke-width": 5 }, g);
      return { g: g, eau: eau };
    }
    function cruche(x) {
      var g = sv("g", {}, s);
      sv("path", { d: "M-30 -30 Q-38 10 -22 34 H22 Q38 10 30 -30 Z M30 -24 L52 -40", fill: "#3a4560", stroke: C.iv2, "stroke-width": 4, "stroke-linejoin": "round" }, g);
      var jet = sv("path", { d: "", fill: "none", stroke: C.eau, "stroke-width": 9, "stroke-linecap": "round" }, s);
      return { g: g, jet: jet, x: x };
    }
    var A = tonneau(260, "tA" + v.id), B = tonneau(740, "tB" + v.id);
    var cA = cruche(260), cB = cruche(740);
    var lA = etiquette(s, 260, 470, "tonneaux sains", { fs: 28, cls: "ser" }), lB = etiquette(s, 740, 470, "tonneaux percés", { fs: 28, cls: "ser", c: C.ca });
    var sA = etiquette(s, 260, 500, "le tempérant : rempli, tranquille", { fs: 19, fw: 400, c: C.iv2 });
    var sB = etiquette(s, 740, 500, "l'insatiable : jamais rempli", { fs: 19, fw: 400, c: C.iv2 });
    var trous = [[-60, 380], [10, 400], [70, 370]].map(function (q) { return sv("ellipse", { cx: 740 + q[0], cy: q[1], rx: 7, ry: 5, fill: "#0b0f19" }, s); });
    var fuites = [[-60, 380, -1], [10, 400, 1], [70, 370, 1]].map(function (q) { return sv("path", { d: "", fill: "none", stroke: C.eau, "stroke-width": 5, "stroke-linecap": "round", "stroke-dasharray": "10 12" }, s); });
    var flaque = sv("ellipse", { cx: 740, cy: 432, rx: 0, ry: 9, fill: C.eau, opacity: .6 }, s);
    var inf = etiquette(s, 900, 250, "∞", { fs: 92, c: C.sa, cls: "ser" });
    function verse(c, t, actif, cible) {
      var a = E(actif);
      op(c.g, a); c.g.setAttribute("transform", "translate(" + (c.x - 70) + "," + (110 - 30 * (1 - a)) + ") rotate(" + (35 * a) + ")");
      if (a > 0.6) {
        var ex = c.x - 70 + 46, ey = 116, w = Math.sin(t * 9) * 3;
        c.jet.setAttribute("d", "M" + ex + " " + ey + " Q" + (ex + 8 + w) + " " + (ey + 60) + " " + (c.x - 4) + " " + cible);
        op(c.jet, (a - .6) / .4);
      } else op(c.jet, 0);
    }
    return function (t, st) {
      var a = E(P(t, v.t0, .8));
      op(A.g, a); op(B.g, a); op(lA, a); op(lB, a);
      var e1 = et(v, "1", 2), e2 = et(v, "2", 6), e3 = et(v, "3", 10);
      var nA = 0.88 * EIO(P(t, e1 + .4, 3));
      A.eau.setAttribute("y", 420 - 240 * nA); A.eau.setAttribute("height", 240 * nA);
      verse(cA, t, P(t, e1, .5) * (1 - P(t, e1 + 3.6, .6)), 420 - 240 * nA);
      op(sA, E(P(t, e1 + 1, .8)));
      var actifB = P(t, e2, .5);
      var nB = actifB > 0 ? 0.16 + 0.08 * Math.sin((t - e2) * 1.3) + 0.12 * E(P(t, e2, 1.5)) : 0;
      B.eau.setAttribute("y", 420 - 240 * nB); B.eau.setAttribute("height", 240 * nB);
      verse(cB, t, actifB, 420 - 240 * nB);
      op(sB, E(P(t, e2 + 1, .8)));
      trous.forEach(function (o) { op(o, E(P(t, e2, .6))); });
      fuites.forEach(function (f, i) {
        var q = [[-60, 380, -1], [10, 400, 1], [70, 370, 1]][i], x0 = 740 + q[0], y0 = q[1];
        f.setAttribute("d", "M" + x0 + " " + y0 + " Q" + (x0 + q[2] * 26) + " " + (y0 + 8) + " " + (x0 + q[2] * 34) + " 430");
        f.style.strokeDashoffset = -((t * 60) % 22);
        op(f, E(P(t, e2 + .8 + i * .3, .5)));
      });
      flaque.setAttribute("rx", 130 * E(P(t, e2 + 1, 4)));
      op(inf, E(P(t, e3, .8))); tr(inf, "scale(" + (1 + 0.06 * Math.sin(t * 2.5)) + ")"); inf.style.transformOrigin = "900px 220px";
    };
  };

  ILLU.tel = function (s, v) {
    var defs = sv("defs", {}, s), id = "ecr" + v.id;
    var cp = sv("clipPath", { id: id }, defs); sv("rect", { x: 282, y: 52, width: 236, height: 436, rx: 18 }, cp);
    sv("rect", { x: 262, y: 20, width: 276, height: 500, rx: 40, fill: "#0b0f19", stroke: C.iv2, "stroke-width": 5 }, s);
    var ecran = sv("g", { "clip-path": "url(#" + id + ")" }, s);
    sv("rect", { x: 282, y: 52, width: 236, height: 436, fill: "#141b2c" }, ecran);
    var fil = sv("g", {}, ecran), cartes = [];
    var teintes = ["#c8811f", "#4f9a8e", "#c2614c", "#6c7bb8", "#b5925a", "#5e8f6a"];
    for (var i = 0; i < 6; i++) {
      var g = sv("g", {}, fil);
      sv("rect", { x: 296, y: 0, width: 208, height: 150, rx: 12, fill: teintes[i], opacity: .75 }, g);
      sv("path", { d: "M386 55 l30 20 l-30 20 Z", fill: "rgba(255,255,255,.85)" }, g);
      sv("rect", { x: 296, y: 162, width: 150, height: 10, rx: 5, fill: "rgba(243,239,228,.45)" }, g);
      sv("rect", { x: 296, y: 180, width: 100, height: 10, rx: 5, fill: "rgba(243,239,228,.25)" }, g);
      cartes.push(g);
    }
    var auto = sv("g", {}, ecran);
    sv("rect", { x: 282, y: 52, width: 236, height: 436, fill: "rgba(5,8,15,.82)" }, auto);
    etiquette(auto, 400, 196, "Vidéo suivante dans", { fs: 20, fw: 400, c: C.iv2 });
    var cpt = etiquette(auto, 400, 300, "3", { fs: 72, c: C.sa, cls: "ser" });
    var anneau = sv("circle", { cx: 400, cy: 278, r: 52, fill: "none", stroke: C.sa, "stroke-width": 5, transform: "rotate(-90 400 278)" }, auto);
    var notif = sv("g", {}, ecran);
    sv("rect", { x: 292, y: 62, width: 216, height: 64, rx: 14, fill: "#f3efe4" }, notif);
    sv("path", { d: "M318 104 h22 q-5 -5 -5 -14 q0 -12 -6 -14 q0 -5 -5 -5 q-5 0 -5 5 q-6 2 -6 14 q0 9 -5 14 z", fill: C.sa2 }, notif);
    etiquette(notif, 352, 90, "Nouveau message", { fs: 17, c: "#1c2438", ancre: "start" });
    etiquette(notif, 352, 112, "Réponds vite !", { fs: 15, fw: 400, c: "#4a5270", ancre: "start" });
    var pastille = sv("circle", { cx: 530, cy: 30, r: 16, fill: C.ca }, s);
    var nb = etiquette(s, 530, 37, "3", { fs: 18, c: "#fff" });
    var fleches = sv("path", { d: "M600 200 A120 120 0 1 1 600 340", fill: "none", stroke: "rgba(232,178,90,.5)", "stroke-width": 4, "stroke-dasharray": "2 12", "stroke-linecap": "round" }, s);
    var fleches2 = sv("path", { d: "M200 340 A120 120 0 1 1 200 200", fill: "none", stroke: "rgba(232,178,90,.5)", "stroke-width": 4, "stroke-dasharray": "2 12", "stroke-linecap": "round" }, s);
    return function (t, st) {
      var tl = t - v.t0, e1 = et(v, "1", 4), e2 = et(v, "2", 6);
      var fin = P(tl, 3.2, .4);
      op(auto, 1 - fin);
      var n = Math.max(1, 3 - Math.floor(tl / 1.05));
      cpt.textContent = n;
      trace(anneau, 1 - ((tl % 1.05) / 1.05));
      // défilement : la vitesse s'emballe après l'étape 1
      var d = 30 * Math.max(0, tl - 3.2) + 170 * Math.max(0, t - e1) + 90 * Math.pow(Math.max(0, t - e1), 1.5);
      cartes.forEach(function (c, i) { var y = ((i * 214 - d) % (6 * 214) + 6 * 214) % (6 * 214) - 120; c.setAttribute("transform", "translate(0," + y.toFixed(1) + ")"); });
      var pn = P(t, e2, .7);
      notif.setAttribute("transform", "translate(0," + (-90 * (1 - EB(pn))).toFixed(1) + ")");
      op(notif, pn > 0 ? 1 : 0);
      op(pastille, E(P(t, e2 + .3, .4))); op(nb, E(P(t, e2 + .3, .4)));
      pastille.setAttribute("r", 16 + 3 * Math.max(0, Math.sin((t - e2) * 6)) * (t > e2 ? 1 : 0));
      fleches.style.strokeDashoffset = -t * 40; fleches2.style.strokeDashoffset = -t * 40;
      op(fleches, E(P(t, e1, .8))); op(fleches2, E(P(t, e1, .8)));
    };
  };

  ILLU.murfeu = function (s, v) {
    sv("path", { d: "M500 30 V450", stroke: "rgba(243,239,228,.18)", "stroke-width": 2, "stroke-dasharray": "8 10" }, s);
    var sol = sv("path", { d: "M20 420 H980", stroke: "rgba(243,239,228,.35)", "stroke-width": 3 }, s);
    var mur = sv("g", {}, s);
    for (var r = 0; r < 9; r++) for (var c = 0; c < 2; c++) {
      sv("rect", { x: 330 + (r % 2 ? 0 : -10) + c * 40, y: 420 - (r + 1) * 30, width: 38, height: 27, rx: 3, fill: "#8f4a3a", stroke: "#6b3428", "stroke-width": 2 }, mur);
    }
    var feu = sv("g", {}, s);
    sv("path", { d: "M860 420 V170", stroke: "#5b6478", "stroke-width": 10 }, feu);
    sv("rect", { x: 830, y: 60, width: 60, height: 130, rx: 14, fill: "#1a2030", stroke: "#5b6478", "stroke-width": 4 }, feu);
    var rouge = sv("circle", { cx: 860, cy: 95, r: 20, fill: "#3a1d1d" }, feu);
    var vert = sv("circle", { cx: 860, cy: 155, r: 20, fill: "#1d3a2a" }, feu);
    var halo = sv("circle", { cx: 860, cy: 95, r: 46, fill: "rgba(230,70,60,.25)" }, feu);
    var pA = pieton(s), pB = pieton(s);
    var tC = etiquette(s, 250, 90, "CONTRAINTE", { c: C.ca, ls: 4, fs: 30 }), sC = etiquette(s, 250, 130, "je ne peux pas passer", { c: C.iv2, fs: 24, fw: 400 });
    var tO = etiquette(s, 680, 90, "OBLIGATION", { c: C.sa, ls: 4, fs: 30 }), sO = etiquette(s, 680, 130, "je ne dois pas passer", { c: C.iv2, fs: 24, fw: 400 });
    var poss = sv("path", { d: "M800 300 H960", stroke: "rgba(232,178,90,.7)", "stroke-width": 3, "stroke-dasharray": "6 8", fill: "none" }, s);
    var possP = sv("path", { d: "M960 300 l-12 -8 M960 300 l-12 8", stroke: "rgba(232,178,90,.7)", "stroke-width": 3 }, s);
    var possT = etiquette(s, 880, 280, "je pourrais…", { c: C.sa, fs: 20, fw: 400 });
    return function (t, st) {
      var e1 = et(v, "1", 3), e2 = et(v, "2", 8), e3 = et(v, "3", 12);
      op(sol, E(P(t, v.t0, .6)));
      // A marche vers le mur et s'arrête net
      var xa = 90 + Math.min(1, P(t, v.t0, Math.max(.5, e1 - v.t0 + .3))) * 200;
      var marcheA = t < e1 + .3;
      var choc = t > e1 + .3 ? Math.sin((t - e1 - .3) * 30) * 6 * Math.exp(-(t - e1 - .3) * 6) : 0;
      pA.pose(xa - choc, 418, t * 8, marcheA ? .5 : 0);
      op(mur, E(P(t, e1 - .6, .5))); tr(mur, "translateY(" + (20 * (1 - E(P(t, e1 - .6, .5)))) + "px)");
      op(tC, E(P(t, e1 + .4, .6))); op(sC, E(P(t, e1 + .8, .6)));
      // B arrive au feu, qui passe au rouge : il s'arrête de lui-même
      var arrB = e2 + .9;
      var xb = 560 + 200 * E(P(t, e2 - 1.2, 2.1));
      pB.pose(xb, 418, t * 8, t < arrB ? .5 : 0);
      op(pB.g, E(P(t, e2 - 1.4, .5)));
      op(feu, E(P(t, e2 - 1.4, .6)));
      var rougeOn = t > e2 + .2;
      rouge.setAttribute("fill", rougeOn ? "#e8463c" : "#3a1d1d"); vert.setAttribute("fill", rougeOn ? "#1d3a2a" : "#3fcf86");
      op(halo, rougeOn ? .6 + .4 * Math.sin(t * 4) : 0);
      var p3 = E(P(t, e3, .6));
      op(tO, p3); op(sO, E(P(t, e3 + .4, .6)));
      trace(poss, P(t, e2 + 1.6, 1)); op(possP, E(P(t, e2 + 2.5, .3))); op(possT, E(P(t, e2 + 2, .6)));
    };
  };

  ILLU.chute = function (s, v) {
    sv("path", { d: "M120 70 H320", stroke: "rgba(243,239,228,.4)", "stroke-width": 4 }, s);
    var sol = sv("path", { d: "M40 420 H400", stroke: "rgba(243,239,228,.35)", "stroke-width": 3 }, s);
    var traj = sv("path", { d: "M220 120 V400", stroke: "rgba(232,178,90,.5)", "stroke-width": 3, "stroke-dasharray": "6 10" }, s);
    var pierre = sv("path", { d: "M-30 -8 L-14 -28 L18 -26 L32 -4 L22 22 L-10 26 L-30 12 Z", fill: "#8c8a83", stroke: "#cfcabd", "stroke-width": 3 }, s);
    var poud = [0, 1, 2, 3].map(function (i) { return sv("circle", { r: 6, fill: "rgba(243,239,228,.5)" }, s); });
    var lab = etiquette(s, 220, 470, "NÉCESSAIRE", { c: C.sa, ls: 4, fs: 26 });
    return function (t, st) {
      var e1 = et(v, "1", 1);
      var tt = Math.max(0, t - e1), cyc = 2.4, k = tt % cyc;
      var y = 100;
      if (t > e1) { y = Math.min(392, 100 + 0.5 * 1500 * k * k); if (k > 0.62) y = 392 - 18 * Math.max(0, Math.sin((k - .62) * 12)) * Math.exp(-(k - .62) * 6); }
      pierre.setAttribute("transform", "translate(220," + y.toFixed(1) + ") rotate(" + (t > e1 ? k * 120 : 0).toFixed(1) + ")");
      op(traj, t > e1 ? 0.3 : E(P(t, v.t0, .6)));
      var kk = k - .62;
      poud.forEach(function (c, i) {
        var on = t > e1 && kk > 0 && kk < .8;
        op(c, on ? .8 * (1 - kk / .8) : 0);
        if (on) { c.setAttribute("cx", 220 + (i - 1.5) * 30 * (1 + kk * 3)); c.setAttribute("cy", 412 - 20 * kk); }
      });
      op(lab, E(P(t, e1 + .5, .6)));
    };
  };

  ILLU.lance = function (s, v) {
    var x0 = 70, y0 = 400, x1 = 680, y1 = 420, top = 90;
    function pt(u) { var x = x0 + (x1 - x0) * u, y = y0 + (y1 - y0) * u - 4 * (y0 - top) * u * (1 - u); return [x, y]; }
    var dpath = "M" + [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1].map(function (u) { var p = pt(u); return p[0].toFixed(0) + " " + p[1].toFixed(0); }).join(" L");
    var traj = sv("path", { d: dpath, fill: "none", stroke: "rgba(232,178,90,.55)", "stroke-width": 3, "stroke-dasharray": "4 12", "stroke-linecap": "round" }, s);
    var main = sv("path", { d: "M20 450 Q50 410 74 404 Q86 402 84 414 Q78 430 60 450", fill: "#b9a68c", stroke: "#e2d4bd", "stroke-width": 3 }, s);
    var pierre = sv("g", {}, s);
    sv("path", { d: "M-26 -6 L-12 -24 L16 -22 L28 -2 L20 20 L-8 22 L-26 10 Z", fill: "#8c8a83", stroke: "#cfcabd", "stroke-width": 3 }, pierre);
    var yeux = sv("g", {}, pierre);
    sv("circle", { cx: -6, cy: -4, r: 4, fill: "#fff" }, yeux); sv("circle", { cx: 9, cy: -4, r: 4, fill: "#fff" }, yeux);
    sv("circle", { cx: -5, cy: -4, r: 2, fill: "#111" }, yeux); sv("circle", { cx: 10, cy: -4, r: 2, fill: "#111" }, yeux);
    var bulle = sv("g", {}, s);
    sv("rect", { x: 330, y: 10, width: 390, height: 92, rx: 46, fill: "#f3efe4" }, bulle);
    etiquette(bulle, 525, 50, "« Je vole parce que", { fs: 25, c: "#1c2438", cls: "ser" });
    etiquette(bulle, 525, 82, "je l'ai décidé ! »", { fs: 25, c: "#1c2438", cls: "ser" });
    var b1 = sv("circle", { r: 9, fill: "#f3efe4" }, s), b2 = sv("circle", { r: 6, fill: "#f3efe4" }, s);
    var cap = etiquette(s, 380, 470, "Spinoza : la pierre qui croit choisir de voler", { fs: 21, fw: 400, c: C.iv2 });
    return function (t, st) {
      op(traj, E(P(t, v.t0, .8))); op(main, E(P(t, v.t0, .6)));
      var per = 3.4, u = ((t - v.t0) % per) / per, p = pt(EIO(u) * .25 + u * .75);
      pierre.setAttribute("transform", "translate(" + p[0].toFixed(1) + "," + p[1].toFixed(1) + ")");
      op(pierre, t > v.t0 + .3 ? 1 : 0);
      var e1 = et(v, "1", 2), e2 = et(v, "2", 4);
      op(yeux, E(P(t, e1, .5)));
      var pb = E(P(t, e2, .6));
      op(bulle, pb); tr(bulle, "scale(" + (0.8 + 0.2 * EB(P(t, e2, .6))) + ")"); bulle.style.transformOrigin = "525px 100px";
      var c1 = [p[0] + (420 - p[0]) * .35, p[1] + (110 - p[1]) * .35], c2 = [p[0] + (420 - p[0]) * .65, p[1] + (110 - p[1]) * .65];
      b1.setAttribute("cx", c2[0]); b1.setAttribute("cy", c2[1]); b2.setAttribute("cx", c1[0]); b2.setAttribute("cy", c1[1]);
      op(b1, pb); op(b2, pb);
      op(cap, E(P(t, v.t0 + 1, .8)));
    };
  };

  /* ---------- types de visuels ---------- */
  var TYPES = {};

  TYPES.titre = function (o, v) {
    o.disp = "flex"; o.entree = "aucune";
    var e = o.el; e.classList.add("v-titre");
    var halo = h("div", "halo", e), sur = h("div", "sur", e, esc(v.sur || "")), tt = h("div", "tt serif", e);
    var sp = lettres(tt, v.t), regle = h("div", "regle", e), ss = h("div", "ss", e, esc(v.sous || ""));
    return function (t, st) {
      var tl = st.tl;
      op(halo, E(P(tl, 0, 1.2)) * (0.75 + 0.25 * Math.sin(t * 1.3))); tr(halo, "scale(" + (0.85 + 0.15 * E(P(tl, 0, 2))) + ")");
      op(sur, E(P(tl, .1, .7))); sur.style.letterSpacing = (0.6 - 0.28 * E(P(tl, .1, 1.2))) + "em";
      animLettres(sp, tl, .3, .035, .7, true);
      tr(regle, "scaleX(" + E(P(tl, .8, 1)) + ")");
      op(ss, E(P(tl, 1.2, .8))); tr(ss, "translateY(" + (14 * (1 - E(P(tl, 1.2, .8)))) + "px)");
      tr(tt, "scale(" + (1 + 0.02 * tl) + ")");
    };
  };

  TYPES.chapitre = function (o, v) {
    o.entree = "aucune";
    var e = o.el; e.classList.add("v-chapitre");
    var num = h("div", "num", e, esc(v.num)), tt = h("div", "tt", e), sp = lettres(tt, v.t), trait = h("div", "trait", e);
    return function (t, st) {
      var tl = st.tl;
      op(num, E(P(tl, 0, .8)) * .9); tr(num, "scale(" + (1.25 - 0.25 * E(P(tl, 0, 1.2)) + 0.02 * tl) + ")");
      animLettres(sp, tl, .35, .03, .6, true);
      tr(trait, "scaleX(" + E(P(tl, .7, .9)) + ")");
    };
  };

  TYPES.mot = function (o, v) {
    var e = o.el; e.classList.add("v-mot");
    e.style.left = (v.x != null ? v.x : 140) + "px"; e.style.width = (v.w || 1000) + "px"; e.style.top = (v.y != null ? v.y : 260) + "px";
    var tt = h("div", "tt", e); tt.style.fontSize = (v.taille || 96) + "px";
    var sp = lettres(tt, v.t), gl = v.g ? h("div", "gl", e, esc(v.g)) : null;
    o.entree = "aucune";
    return function (t, st) {
      animLettres(sp, st.tl, 0, Math.min(.05, 1 / sp.length), .6, true);
      if (gl) { op(gl, E(P(st.tl, .6, .7))); tr(gl, "translateY(" + 12 * (1 - E(P(st.tl, .6, .7))) + "px)"); }
    };
  };

  TYPES.question = function (o, v) {
    o.disp = "flex"; o.entree = "aucune";
    var e = o.el; e.classList.add("v-question");
    var tt = h("div", "tt", e);
    var sp = mots(tt, v.t);
    sp[0].innerHTML = '<span class="gu">«\u00a0</span>' + sp[0].innerHTML;
    sp[sp.length - 1].innerHTML += '<span class="gu">\u00a0»</span>';
    return function (t, st) {
      sp.forEach(function (m, i) {
        var p = E(P(st.tl, .1 + i * .12, .7));
        m.style.opacity = p; m.style.filter = p < 1 ? "blur(" + ((1 - p) * 8).toFixed(1) + "px)" : "none";
      });
      tr(tt, "scale(" + (1 + 0.012 * st.tl) + ")");
    };
  };

  TYPES.nuage = function (o, v) {
    o.entree = "aucune";
    var e = o.el; e.classList.add("v-nuage");
    var n = v.items.length, its = [];
    var ce = v.centre ? h("div", "ce", e, esc(v.centre)) : null;
    v.items.forEach(function (txt, i) {
      var ang = (-90 + i * 360 / n + (alea(i) - .5) * 18) * Math.PI / 180;
      var rx = v.centre ? 400 : 360, ry = v.centre ? 220 : 190;
      var d = h("div", "it", e, esc(txt));
      d.style.left = (640 + Math.cos(ang) * rx) + "px"; d.style.top = (370 + Math.sin(ang) * ry) + "px";
      d.style.fontSize = (v.centre ? 46 : 58) + Math.round(alea(i + 7) * 14) + "px";
      its.push(d);
    });
    return function (t, st) {
      if (ce) { op(ce, E(P(st.tl, 0, .6))); tr(ce, "translate(-50%,-50%) scale(" + (0.9 + 0.1 * EB(P(st.tl, 0, .6))) + ")"); }
      its.forEach(function (d, i) {
        var t0 = et(v, String(i + 1), .3 + i * .45), p = E(P(t, t0, .6));
        d.style.opacity = p;
        d.style.color = t >= t0 && t < t0 + 1.2 ? C.sa : C.iv;
        d.style.transform = "translate(-50%,-50%) translate(" + (Math.sin(t * .6 + i * 2) * 8).toFixed(1) + "px," + (Math.cos(t * .5 + i) * 6 + (1 - p) * 20).toFixed(1) + "px) scale(" + (0.85 + 0.15 * EB(P(t, t0, .6))) + ")";
      });
    };
  };

  function carte(o, v, note) {
    var e = o.el;
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 200) + "px"; e.style.width = (v.w || 940) + "px";
    var c = h("div", "carte" + (note ? " note" : ""), e);
    var bg = h("div", "barre-g", c), te = h("div", "te", c, esc(note ? (v.titre || "Attention") : v.terme));
    var tx = h("div", "tx serif", c), sp = mots(tx, v.t, "mot-l cle"), etp = v.etape ? h("div", "et", c, esc(v.etape)) : null;
    if (v.plus) h("div", "badge", c, "Pour aller plus loin");
    var kl = cles(v, sp);
    return function (t, st) {
      allume(kl, t);
      tr(bg, "scaleY(" + E(P(st.tl, .1, .7)) + ")");
      op(te, E(P(st.tl, .2, .6)));
      sp.forEach(function (m, i) { var p = E(P(st.tl, .4 + i * .06, .5)); m.style.opacity = p; m.style.transform = "translateY(" + (1 - p) * 10 + "px)"; });
      if (etp) { var t1 = et(v, "1", 1.6 + sp.length * .06); op(etp, E(P(t, t1, .7))); tr(etp, "translateY(" + 10 * (1 - E(P(t, t1, .7))) + "px)"); }
    };
  }
  TYPES.def = function (o, v) { return carte(o, v, false); };
  TYPES.note = function (o, v) { return carte(o, v, true); };

  TYPES.tag = function (o, v) {
    o.disp = "flex"; o.entree = "aucune";
    var e = o.el; e.classList.add("v-tag", v.style || "repere");
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 560) + "px"; e.style.width = (v.w || 600) + "px";
    var ic = { repere: "✻", copie: "✎", lien: "↔", plus: "+" }[v.style || "repere"] || "✻";
    var p = h("div", "pill", e); h("span", "ic", p, ic); h("span", "", p, esc(v.t));
    return function (t, st) { tr(p, "translateX(" + (-40 * (1 - E(P(st.tl, 0, .7)))) + "px)"); };
  };

  TYPES.cit = function (o, v) {
    var e = o.el; e.classList.add("v-cit");
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 170) + "px"; e.style.width = (v.w || 940) + "px";
    h("div", "gu", e, "«");
    var tx = h("div", "tx", e), L = (v.t || "").length;
    tx.style.fontSize = (L <= 90 ? 46 : L <= 140 ? 41 : L <= 200 ? 36 : 32) * ((v.w || 940) < 800 ? .9 : 1) + "px";
    var sp = mots(tx, v.t, "mc");
    var au = h("div", "au", e, "— <b>" + esc(v.a || "") + "</b>" + (v.o ? ", " + esc(v.o) : "") + (v.para ? '<span class="ap">≈ CITATION APPROCHÉE</span>' : ""));
    var m = v.m || [], n = sp.length;
    var tm = sp.map(function (_, i) {
      if (!m.length) return v.t0 + .5 + i * .3;
      var j = m.length === n ? i : Math.min(m.length - 1, Math.round(i * (m.length - 1) / Math.max(1, n - 1)));
      return m[j][0];
    });
    return function (t, st) {
      sp.forEach(function (s, i) {
        var p = E(P(t, tm[i] - .05, .3)), f = P(t, tm[i] + .35, .8);
        s.style.opacity = 0.2 + 0.8 * p;
        s.style.color = p > 0 && f < 1 ? "rgb(" + Math.round(232 + 11 * f) + "," + Math.round(178 + 61 * f) + "," + Math.round(90 + 138 * f) + ")" : (p > 0 ? C.iv : C.iv2);
        s.style.transform = "translateY(" + (-3 * p * (1 - f)).toFixed(2) + "px)";
      });
      op(au, E(P(st.tl, .7, .7)));
    };
  };

  // repère dans le temps : petite frise de -600 à 2000, point lumineux à l'année de l'auteur
  function minifrise(parent, annee) {
    var f = h("div", "mf", parent);
    var X = function (an) { return an < 500 ? (an + 600) / 1100 * 30 : an < 1500 ? 30 + (an - 500) / 1000 * 22 : 52 + (an - 1500) / 500 * 48; };
    h("div", "mf-axe", f);
    [["Antiquité", -600], ["Moyen Âge", 500], ["Modernes", 1500], ["Contemp.", 1800]].forEach(function (z) {
      var l = h("div", "mf-z", f, z[0]); l.style.left = X(z[1]) + "%";
    });
    var pt = h("div", "mf-pt", f); pt.style.left = X(annee) + "%";
    var an = h("div", "mf-an", f, annee < 0 ? (-annee) + " av. J.-C." : String(annee)); an.style.left = X(annee) + "%";
    return { f: f, pt: pt, an: an };
  }

  TYPES.portrait = function (o, v) {
    var e = o.el; e.classList.add("v-portrait", "grand"); o.entree = "aucune"; o.prof = -0.6;
    var pf = h("div", "pf", e), img;
    if (v.img) { img = h("img", "", pf); img.src = "img/" + v.img + ".jpg"; img.alt = v.nom; img.decoding = "sync"; }
    else img = h("div", "mono", pf, esc((v.nom || "?").split(" ").map(function (x) { return x[0]; }).join("")));
    var bd = h("div", "bandeau", e);
    var trait = h("div", "bd-trait", bd);
    var nm = h("div", "bd-nom", bd, esc(v.nom));
    var inf = h("div", "bd-info", bd, esc([v.dates, v.legende].filter(Boolean).join(" · ")));
    var mf = v.annee != null ? minifrise(bd, v.annee) : null;
    return function (t, st) {
      var a = E(P(st.tl, 0, 1.1)), vie = P(t, v.t0, Math.max(6, v.t1 - v.t0));
      op(pf, a); tr(pf, "translateX(" + (-40 * (1 - a)) + "px)");
      tr(img, "scale(" + (1.06 + 0.1 * vie) + ") translate(" + (1.5 * vie) + "%," + (-2.5 * vie) + "%)");
      tr(trait, "scaleX(" + E(P(st.tl, .5, .8)) + ")");
      var b = E(P(st.tl, .6, .7)); op(nm, b); tr(nm, "translateX(" + (-24 * (1 - b)) + "px)");
      var c = E(P(st.tl, .9, .7)); op(inf, c);
      if (mf) {
        op(mf.f, E(P(st.tl, 1.3, .7)) * (1 - E(P(st.tl, 5.5, .8)) * .55));
        var q = P(st.tl, 1.7, .6); tr(mf.pt, "translate(-50%,-50%) scale(" + (0.3 + 0.7 * EB(q)) + ")");
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(232,178,90,.9)";
        op(mf.an, E(P(st.tl, 2, .5)));
      }
    };
  };

  TYPES.cols = function (o, v) {
    var e = o.el; e.classList.add("v-cols"); o.entree = "aucune";
    var g = h("div", "col g", e), d = h("div", "col d", e);
    h("div", "t", g, esc(v.g)); h("div", "q", g, esc(v.gq || "")); h("div", "t", d, esc(v.d)); h("div", "q", d, esc(v.dq || ""));
    var vs = h("div", "vs", e, esc(v.vs || "≠")), rp = v.repere ? h("div", "rp", e, "<span>✻ " + esc(v.repere) + "</span>") : null;
    if (v.plus) h("div", "badge", e, "Pour aller plus loin");
    return function (t, st) {
      var tg = et(v, "g", .1), td = et(v, "d", v.et && v.et["1"] ? v.et["1"] - v.t0 : .9);
      var pg = E(P(t, tg, .7)), pd = E(P(t, td, .7));
      op(g, pg); tr(g, "translateX(" + (-50 * (1 - pg)) + "px)");
      op(d, pd); tr(d, "translateX(" + (50 * (1 - pd)) + "px)");
      var tv = Math.max(tg, td) + .5, pv = P(t, tv, .6);
      op(vs, E(pv)); tr(vs, "translate(-50%,-50%) scale(" + (0.4 + 0.6 * EB(pv)) + ") rotate(" + (-90 * (1 - E(pv))) + "deg)");
      if (rp) op(rp, E(P(t, tv + .5, .6)));
    };
  };

  TYPES.cartes = function (o, v) {
    var e = o.el; e.classList.add("v-cartes"); if (v.petit) e.classList.add("petit"); o.entree = "aucune";
    var cs = v.items.map(function (it, i) {
      var c = h("div", "ca", e); c.style.left = (i * 380) + "px";
      h("div", "n", c, "0" + (i + 1));
      var ic = icone(it.ic, c);
      h("div", "t", c, esc(it.t)); h("div", "q", c, esc(it.q));
      return { c: c, ic: ic };
    });
    return function (t, st) {
      var tk = cs.map(function (_, i) { return et(v, String(i + 1), .2 + i * .4); });
      var hl = v.et && v.et.hl != null ? v.et.hl : null;
      cs.forEach(function (c, i) {
        var p = E(P(t, tk[i], .7));
        op(c.c, p); tr(c.c, "translateY(" + (40 * (1 - p)) + "px) scale(" + (0.94 + 0.06 * p) + ")");
        c.ic.forEach(function (pa, j) { trace(pa, P(t, tk[i] + .2 + j * .15, .8)); });
        var actif = (t >= tk[i] && (i === cs.length - 1 || t < tk[i + 1]) && v.et && v.et[String(i + 1)] != null) || (hl != null && t >= hl);
        var pul = hl != null && t >= hl ? 0.5 + 0.5 * Math.sin((t - hl) * 4 + i) : 1;
        c.c.style.borderColor = actif ? "rgba(232,178,90," + (0.5 + 0.4 * pul) + ")" : "rgba(243,239,228,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(232,178,90,.25)" : "none";
      });
    };
  };

  TYPES.liste = function (o, v) {
    var e = o.el; e.classList.add("v-liste");
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 150) + "px"; e.style.width = (v.w || 940) + "px";
    if (v.titre) h("div", "ti", e, esc(v.titre));
    var lis = v.items.map(function (txt, i) {
      var li = h("div", "li", e), mq = (v.marques || [])[i] || String(i + 1);
      var b = h("div", "mq" + (mq === "✓" ? " ok" : mq === "✗" ? " ko" : ""), li, esc(mq));
      var tx = h("div", "tx", li), sp = mots(tx, txt, "mot-l cle");
      return { li: li, b: b, tx: tx, sp: sp };
    });
    var kl = cles(v, [].concat.apply([], lis.map(function (l) { return l.sp; })));
    return function (t, st) {
      allume(kl, t);
      var tk = lis.map(function (_, i) { return et(v, String(i + 1), .3 + i * .5); });
      var dernier = -1; tk.forEach(function (x, i) { if (t >= x) dernier = i; });
      lis.forEach(function (l, i) {
        var p = E(P(t, tk[i], .6));
        op(l.li, p * (i === dernier || !v.et ? 1 : .62)); tr(l.li, "translateX(" + (-30 * (1 - p)) + "px)");
        tr(l.b, "scale(" + (0.5 + 0.5 * EB(P(t, tk[i], .5))) + ")");
      });
    };
  };

  TYPES.dialogue = function (o, v) {
    var e = o.el; e.classList.add("v-dialogue");
    e.style.left = (v.x || 500) + "px"; e.style.top = (v.y || 180) + "px"; e.style.width = (v.w || 680) + "px";
    var ls = v.lignes.map(function (l) { return h("div", "l", e, esc(l)); });
    var src = v.src ? h("div", "src", e, esc(v.src)) : null;
    return function (t, st) {
      ls.forEach(function (l, i) { var p = E(P(t, et(v, String(i + 1), i * 2), .6)); op(l, p); tr(l, "translateY(" + 16 * (1 - p) + "px)"); });
      if (src) op(src, E(P(st.tl, 1, .8)) * .9);
    };
  };

  TYPES.frise = function (o, v) {
    var e = o.el; e.classList.add("v-frise"); o.entree = "aucune";
    function X(an) { return an < 500 ? 120 + (an + 500) / 1000 * 300 : 520 + (an - 1500) / 450 * 640; }
    var axe = h("div", "axe", e);
    var rupt = h("div", "rupt", e, "≈"); rupt.style.left = "470px";
    var ans = [[-400, "−400"], [0, "0"], [1600, "1600"], [1700, "1700"], [1800, "1800"], [1900, "1900"]].map(function (a) {
      var d = h("div", "an", e, a[1]); d.style.left = X(a[0]) + "px"; return d;
    });
    var RANGS = [{ top: 210, tige: [84, 78] }, { top: 420, tige: [-48, 48] }, { top: 66, tige: [84, 222] }, { top: 560, tige: [-188, 188] }];
    var fin = RANGS.map(function () { return -1e9; });
    var its = v.items.slice().sort(function (a, b) { return a.d - b.d; }).map(function (it, i) {
      var p = h("div", "p", e), x = X(it.d), r = 0;
      while (r < RANGS.length - 1 && x - fin[r] < 128) r++;
      fin[r] = x;
      var R = RANGS[r];
      p.style.left = x + "px"; p.style.top = R.top + "px";
      var tige = h("div", "tige", p); tige.style.top = R.tige[0] + "px"; tige.style.height = R.tige[1] + "px";
      var md = h("div", "md", p);
      if (it.img) { var im = h("img", "", md); im.src = "img/" + it.img + ".jpg"; im.alt = it.nom; } else md.textContent = it.nom[0];
      h("div", "nm", p, esc(it.nom)); h("div", "dt", p, it.d < 0 ? "−" + (-it.d) : String(it.d));
      return p;
    });
    return function (t, st) {
      tr(axe, "scaleX(" + EIO(P(st.tl, 0, 1.4)) + ")");
      op(rupt, E(P(st.tl, 1, .5))); ans.forEach(function (a) { op(a, E(P(st.tl, 1, .6))); });
      its.forEach(function (p, i) { var q = P(st.tl, .8 + i * .28, .6); op(p, E(q)); tr(p, "translateY(" + 20 * (1 - E(q)) + "px) scale(" + (0.7 + 0.3 * EB(q)) + ")"); });
    };
  };

  // tableau : œuvre plein cadre, travelling lent (Ken Burns) d'un cadrage à l'autre ; en fond, assombri sous les autres visuels
  TYPES.tableau = function (o, v) {
    var e = o.el; e.classList.add("v-tableau"); if (v.fond) e.classList.add("fond-t"); if (v.sombre) e.classList.add("sombre"); o.entree = "aucune";
    var img = h("img", "", e); img.alt = v.legende || ""; img.decoding = "sync";
    var pret = false, enCours = false;
    // l'image n'apparaît qu'une fois décodée : pas de cadre vide ni de flash au premier affichage
    function charge() {
      if (enCours) return; enCours = true;
      img.style.width = img.naturalWidth + "px"; img.style.height = img.naturalHeight + "px";
      var fin = function () { pret = true; };
      if (img.decode) img.decode().then(fin, fin); else fin();
    }
    o.attente = new Promise(function (r) { var k = setInterval(function () { if (pret) { clearInterval(k); r(); } }, 30); });
    img.addEventListener("load", charge);
    img.src = "img/" + v.img + ".jpg";
    h("div", "ombre", e);
    var lg = v.legende ? h("div", "lg", e, esc(v.legende)) : null;
    var de = v.de || [1.15, .5, .4], a_ = v.a || [1, .5, .5];
    return function (t, st) {
      if (!pret && img.complete && img.naturalWidth) charge();
      // l'image garde sa taille réelle ; seul le transform (translation + échelle) change : pas de redimensionnement
      // ni de nouveau décodage à chaque image, donc pas de clignotement
      var iw = img.naturalWidth || 1600, ih = img.naturalHeight || 900;
      var u = EIO(P(t, v.t0, Math.max(4, v.t1 - v.t0 + .6)));
      var z = de[0] + (a_[0] - de[0]) * u, fx = de[1] + (a_[1] - de[1]) * u, fy = de[2] + (a_[2] - de[2]) * u;
      var sc = Math.max(W / iw, H / ih) * z, w = iw * sc, hh = ih * sc;
      var x = cl(W / 2 - fx * w, W - w, 0), y = cl(H / 2 - fy * hh, H - hh, 0);
      img.style.transform = "translate3d(" + x.toFixed(2) + "px," + y.toFixed(2) + "px,0) scale(" + sc.toFixed(5) + ")";
      op(e, pret ? E(P(t, v.t0, 1.2)) * (1 - EIO(P(t, v.t1, .9))) : 0);
      if (lg) op(lg, E(P(st.tl, 1.2, .8)) * .9);
    };
  };

  TYPES.generique = function (o, v) {
    var e = o.el; e.classList.add("v-generique"); o.entree = "aucune"; o.disp = "flex";
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "L'Index raisonné · Philosophie");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, "Série vidéo · épisode " + v.num);
    var balai = h("div", "g-balai", e);
    return function (t, st) {
      var tl = st.tl;
      op(halo, E(P(tl, 0, 1.5)) * (1 - E(P(tl, 4.6, 1)))); tr(halo, "scale(" + (0.7 + 0.4 * E(P(tl, 0, 5))) + ")");
      op(haut, E(P(tl, .3, .9))); haut.style.letterSpacing = (0.7 - 0.35 * E(P(tl, .3, 2))) + "em";
      tr(l1, "scaleX(" + EIO(P(tl, .6, 1.4)) + ")"); tr(l2, "scaleX(" + EIO(P(tl, .8, 1.4)) + ")");
      animLettres(sp, tl, 1.0, .07, .9, true);
      tr(tt, "scale(" + (1.08 - 0.08 * E(P(tl, 1, 4))) + ")");
      op(bas, E(P(tl, 2.2, .8)));
      tr(balai, "translateX(" + (-400 + 2100 * EIO(P(tl, 2.4, 1.6))) + "px) skewX(-20deg)");
      op(balai, P(tl, 2.4, .2) * (1 - P(tl, 3.8, .2)));
      op(e, 1 - EIO(P(t, v.t1 - .6, .8)));
    };
  };

  TYPES.frappe = function (o, v) {
    var e = o.el; e.classList.add("v-frappe"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fr-fond", e), m = h("div", "fr-mot", e, esc(v.t));
    return function (t, st) {
      var tl = st.tl, a = P(tl, 0, .35), out = P(tl, 1.05, .45);
      op(fond, E(a) * (1 - E(out)));
      op(m, E(P(tl, 0, .2)) * (1 - E(out)));
      var sc = 1.35 - 0.35 * EB(a) + 0.04 * tl;
      var sh = tl < .45 ? Math.sin(tl * 70) * 5 * (1 - tl / .45) : 0;
      tr(m, "translateX(" + sh.toFixed(1) + "px) scale(" + sc.toFixed(3) + ")");
      m.style.letterSpacing = (0.12 - 0.08 * E(a)) + "em";
      m.style.filter = out > 0 ? "blur(" + (8 * out).toFixed(1) + "px)" : "none";
    };
  };

  TYPES.flash = function (o, v) {
    var e = o.el; e.classList.add("v-flash"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fl-fond", e), c = h("div", "fl-carte", e);
    h("div", "fl-te", c, "À retenir");
    var tx = h("div", "fl-tx", c), sp = mots(tx, v.t);
    return function (t, st) {
      var tl = st.tl, a = E(P(tl, 0, .6)), out = EIO(P(t, v.t1 - .3, .6));
      op(fond, a * (1 - out));
      op(c, a * (1 - out)); tr(c, "translateY(" + (24 * (1 - a)) + "px) scale(" + (0.96 + 0.04 * a) + ")");
      sp.forEach(function (m, i) { var p = E(P(tl, .35 + i * .05, .4)); m.style.opacity = p; });
    };
  };

  TYPES.carte = function (o, v) {
    var e = o.el; e.classList.add("v-carte"); o.entree = "aucune";
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H }, e);
    var POS = [[360, 130], [920, 130], [360, 460], [920, 460]];
    var centre = h("div", "cm-centre", e, esc(v.centre));
    var br = (v.branches || []).map(function (b, i) {
      var p = POS[i], ex = p[0] + (p[0] < 640 ? 80 : -80), d = "M640 330 C" + (640 + (ex - 640) * .5) + " 330 " + ex + " " + (330 + (p[1] - 330) * .5) + " " + ex + " " + (p[1] + (p[1] < 330 ? 18 : -18));
      var ln = sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 3, "stroke-linecap": "round", opacity: .8 }, svg);
      var nd = h("div", "cm-noeud", e, esc(b.t)); nd.style.left = p[0] + "px"; nd.style.top = p[1] + "px";
      var gauche = p[0] < 640, col = h("div", "cm-items" + (gauche ? " g" : " d"), e);
      col.style.left = (gauche ? p[0] - 300 : p[0] - 40) + "px"; col.style.top = (p[1] + 36) + "px";
      var its = b.items.map(function (x) { return h("div", "cm-it", col, esc(x)); });
      return { ln: ln, nd: nd, its: its };
    });
    return function (t, st) {
      var a = E(P(st.tl, 0, .7));
      op(centre, a); tr(centre, "translate(-50%,-50%) scale(" + (0.6 + 0.4 * EB(P(st.tl, 0, .7))) + ")");
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(232,178,90,.35)";
      br.forEach(function (b, i) {
        var tk = et(v, String(i + 1), .6 + i * 1.2);
        trace(b.ln, P(t, tk, .8));
        var q = P(t, tk + .5, .5); op(b.nd, E(q)); tr(b.nd, "translate(-50%,-50%) scale(" + (0.5 + 0.5 * EB(q)) + ")");
        b.its.forEach(function (it, j) { var r = E(P(t, tk + .8 + j * .25, .5)); op(it, r); tr(it, "translateY(" + (8 * (1 - r)) + "px)"); });
      });
    };
  };

  TYPES.illu = function (o, v) {
    var e = o.el; e.classList.add("v-illu"); o.entree = "aucune";
    e.style.left = v.x + "px"; e.style.top = v.y + "px"; e.style.width = v.w + "px"; e.style.height = v.h + "px";
    var s = sv("svg", { viewBox: "0 0 " + v.w + " " + v.h }, e);
    if (v.plus) h("div", "badge", e, "Pour aller plus loin").style.top = "-10px";
    var f = ILLU[v.nom] ? ILLU[v.nom](s, v) : function () {};
    return f;
  };

  /* ---------- scène ---------- */
  var FONDS = {
    nuit: { base: "linear-gradient(160deg,#0c1322 0%,#19213a 55%,#121a2b 100%)", lueurs: ["rgba(232,178,90,.20)", "rgba(79,154,142,.16)", "rgba(120,90,160,.16)"] },
    aube: { base: "linear-gradient(160deg,#1a1527 0%,#2a2036 55%,#181d31 100%)", lueurs: ["rgba(232,178,90,.24)", "rgba(194,97,76,.18)", "rgba(79,154,142,.12)"] }
  };

  function Scene(EP, racine) {
    var sc = h("div", "scene", racine);
    var fonds = EP.scenes.map(function (s, i) {
      var f = h("div", "fond", sc), def = FONDS[s.fond] || FONDS.nuit;
      f.style.background = def.base;
      var lu = def.lueurs.map(function (c, j) {
        var l = h("div", "lueur", f); var r = 520 + j * 140;
        l.style.width = l.style.height = r + "px"; l.style.background = "radial-gradient(circle," + c + ",transparent 65%)";
        l.style.left = (j === 0 ? 700 : j === 1 ? -100 : 300) + "px"; l.style.top = (j === 0 ? -150 : j === 1 ? 300 : 380) + "px";
        return l;
      });
      return { el: f, lu: lu, s: s, i: i };
    });
    var cv = h("canvas", "poussiere", sc); cv.width = W; cv.height = H;
    var cx = cv.getContext("2d");
    var parts = []; for (var i = 0; i < 70; i++) parts.push({ x: alea(i) * W, y: alea(i + 100) * H, vx: (alea(i + 200) - .5) * 14, vy: 6 + alea(i + 300) * 16, r: .8 + alea(i + 400) * 2, ph: alea(i + 500) * 6.28 });
    var couche = h("div", "", sc); couche.style.cssText = "position:absolute;inset:0";
    h("div", "voile", sc);
    var ent = h("div", "entete", sc), fil = h("div", "fil", sc), st = h("div", "st", sc), stS = h("span", "", st);
    var objs = EP.vis.map(function (v) {
      var el = h("div", "v", couche), o = { v: v, el: el, disp: "block", entree: "monte", vis: false };
      el.style.display = "none";
      o.upd = (TYPES[v.type] || function () { return function () {}; })(o, v);
      return o;
    });
    var sousOn = false, dernierSous = -1;

    function rendu(t) {
      // fonds
      fonds.forEach(function (f, i) {
        var s = f.s, a = i === 0 ? 1 : E(P(t, s.t0 - .6, 1.2)), b = i === fonds.length - 1 ? 0 : E(P(t, s.t1 - .6, 1.2));
        var w = a * (1 - b);
        if (w <= 0.001) { if (f.on) { f.el.style.display = "none"; f.on = false; } return; }
        if (!f.on) { f.el.style.display = "block"; f.on = true; }
        f.el.style.opacity = w;
        f.lu.forEach(function (l, j) {
          l.style.transform = "translate(" + (Math.sin(t * .07 + j * 2.1) * 120).toFixed(1) + "px," + (Math.cos(t * .05 + j * 1.3) * 80).toFixed(1) + "px) scale(" + (1 + .12 * Math.sin(t * .09 + j)).toFixed(3) + ")";
        });
      });
      // poussière lumineuse
      cx.clearRect(0, 0, W, H);
      parts.forEach(function (p) {
        var x = ((p.x + p.vx * t) % W + W) % W, y = ((p.y - p.vy * t) % H + H) % H;
        var a = .25 + .25 * Math.sin(t * 1.3 + p.ph);
        cx.fillStyle = "rgba(243,224,180," + a.toFixed(3) + ")";
        cx.beginPath(); cx.arc(x, y, p.r, 0, 6.283); cx.fill();
      });
      // visuels
      var plein = false;
      objs.forEach(function (o) {
        var v = o.v;
        if (t < v.t0 || t > v.t1 + (v.type === "tableau" ? 1 : .7)) { if (o.vis) { o.el.style.display = "none"; o.vis = false; } return; }
        if (!o.vis) { o.el.style.display = o.disp; o.vis = true; }
        if (v.type === "titre" || v.type === "chapitre" || v.type === "generique") plein = true;
        var a = E(P(t, v.t0, .7)), out = EIO(P(t, v.t1, .6));
        if (v.type !== "tableau") o.el.style.opacity = (o.entree === "aucune" ? 1 : a) * (1 - out);
        // profondeur : le texte et les images dérivent doucement, à des vitesses différentes
        var pr = o.prof != null ? o.prof : (v.type === "tableau" ? 0 : 1);
        var dx = (Math.sin(t * .071 + 1) * 7 * pr).toFixed(2), dy = (Math.cos(t * .053) * 5 * pr).toFixed(2);
        var flou = (o.entree === "monte" ? (1 - a) * 7 : 0) + out * 6;
        if (v.type !== "tableau") o.el.style.filter = flou > .05 ? "blur(" + flou.toFixed(1) + "px)" : "none";
        if (o.entree === "monte") o.el.style.transform = "translate(" + dx + "px," + (26 * (1 - a) - 14 * out + +dy).toFixed(2) + "px) scale(" + (0.97 + 0.03 * a + 0.02 * out).toFixed(4) + ")";
        else if (v.type !== "tableau") o.el.style.transform = "translate(" + dx + "px," + dy + "px)" + (out > 0 ? " scale(" + (1 + .025 * out) + ")" : "");
        o.upd(t, { tl: t - v.t0, a: a, o: out });
      });
      // en-tête : notion, épisode, chapitre
      var sc_ = EP.scenes.filter(function (s) { return t >= s.t0; }).pop() || EP.scenes[0];
      ent.innerHTML = esc(EP.notion) + " · Ép. " + EP.num + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
      op(ent, plein ? 0 : E(P(t, EP.scenes[0].t0 + 1, 1)) * .9);
      fil.style.width = (W * cl(t / EP.dur, 0, 1)).toFixed(1) + "px";
      // sous-titres
      if (sousOn) {
        var k = -1;
        for (var i = 0; i < EP.sous.length; i++) { if (EP.sous[i][0] <= t && t < EP.sous[i][1]) { k = i; break; } }
        if (k !== dernierSous) { stS.textContent = k >= 0 ? EP.sous[k][2] : ""; st.style.display = k >= 0 ? "block" : "none"; dernierSous = k; }
      } else st.style.display = "none";
    }
    return { el: sc, rendu: rendu, sous: function (b) { sousOn = b; dernierSous = -2; },
      attentes: function () { return objs.filter(function (o) { return o.attente; }).map(function (o) { return o.attente; }); } };
  }

  /* ---------- lecteur ---------- */
  var ICO = {
    play: '<svg viewBox="0 0 24 24"><path d="M7 4.5v15l12.5-7.5z"/></svg>',
    pause: '<svg viewBox="0 0 24 24"><path d="M6 4h4.5v16H6zM13.5 4H18v16h-4.5z"/></svg>',
    m10: '<svg viewBox="0 0 24 24"><path d="M12 5V1L7 6l5 5V7a6 6 0 1 1-6 6H4a8 8 0 1 0 8-8z"/><text x="12" y="16.2" font-size="6.5" text-anchor="middle" font-family="Archivo" font-weight="700">10</text></svg>',
    p10: '<svg viewBox="0 0 24 24"><path d="M12 5V1l5 5-5 5V7a6 6 0 1 0 6 6h2a8 8 0 1 1-8-8z"/><text x="12" y="16.2" font-size="6.5" text-anchor="middle" font-family="Archivo" font-weight="700">10</text></svg>',
    plein: '<svg viewBox="0 0 24 24"><path d="M4 9V4h5v2H6v3zm11-5h5v5h-2V6h-3zM4 15h2v3h3v2H4zm14 3v-3h2v5h-5v-2z"/></svg>',
    musique: '<svg viewBox="0 0 24 24"><path d="M9 18.5a3 3 0 1 1-2-2.8V5l12-2.5v12.5a3 3 0 1 1-2-2.8V6.9L9 8.6z"/></svg>',
    cc: '<svg viewBox="0 0 24 24"><path d="M3 5h18v14H3zm2 2v10h14V7zm2.5 3.2h4v1.5h-2.5v1.6h2.5v1.5h-4zm6 0h4v1.5H15v1.6h2.5v1.5h-4z"/></svg>'
  };

  function lancer(EP) {
    document.title = EP.notion + " · Épisode " + EP.num + " — " + EP.titre;
    if (EMBED) document.body.classList.add("embed");
    var racine = document.getElementById("serie");

    if (EXPORT) { // rendu seul, pour fabriquer la vidéo image par image
      document.body.style.margin = 0;
      racine.style.cssText = "position:fixed;inset:0;overflow:hidden;background:#000";
      var S0 = Scene(EP, racine);
      var k0 = Math.min(innerWidth / W, innerHeight / H);
      S0.el.style.transform = "scale(" + k0 + ")";
      if (Q.has("sous")) S0.sous(true);
      window.RENDU = function (t) { S0.rendu(t); };
      window.DUREE = EP.dur;
      var imgs = Array.from(document.images);
      window.PRET = Promise.all([document.fonts.ready].concat(S0.attentes(), imgs.map(function (im) { return im.complete ? 1 : new Promise(function (r) { im.addEventListener("load", r); im.addEventListener("error", r); }); })));
      S0.rendu(0);
      return;
    }

    var L = h("div", "lecteur", racine);
    if (!EMBED) {
      var tete = h("div", "l-tete", L);
      h("span", "k", tete, esc(EP.notion) + " · épisode " + EP.num);
      h("h1", "", tete, esc(EP.titre));
    }
    var boite = h("div", "boite", L), cadre = h("div", "cadre", boite);
    var S = Scene(EP, cadre);
    var affiche = h("div", "affiche", cadre), gp = h("button", "gros-play", affiche, ICO.play); gp.setAttribute("aria-label", "Lecture");
    h("div", "charge", cadre);
    var barre = h("div", "barre", boite);
    var prog = h("div", "prog", barre), rail = h("div", "rail", prog), plein = h("div", "plein", prog);
    EP.scenes.forEach(function (s, i) { if (i) { var tc = h("div", "tic", prog); tc.style.left = (100 * s.t0 / EP.dur) + "%"; } });
    var pouce = h("div", "pouce", prog), bulle = h("div", "bulle", prog);
    var bPlay = h("button", "btn", barre, ICO.play), bM = h("button", "btn", barre, ICO.m10), bP = h("button", "btn", barre, ICO.p10);
    var temps = h("span", "temps", barre);
    h("span", "espace", barre);
    var bVit = h("button", "btn", barre, '<span class="mono">1×</span>'), bMus = h("button", "btn on", barre, ICO.musique),
      bCC = h("button", "btn", barre, ICO.cc), bFS = h("button", "btn", barre, ICO.plein);
    bPlay.title = "Lecture / pause (espace)"; bM.title = "Reculer de 10 s"; bP.title = "Avancer de 10 s"; bVit.title = "Vitesse";
    bMus.title = "Musique de fond"; bCC.title = "Sous-titres"; bFS.title = "Plein écran";

    h("div", "astuce", L, "Sur téléphone, touche ⛶ : la vidéo passe en plein écran, en paysage.");
    var chaps = h("div", "chapitres", L);
    var bChap = EP.scenes.map(function (s, i) {
      var b = h("button", "chap", chaps);
      h("span", "n", b, i ? ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"][i - 1] : "◆");
      var tx = h("span", "", b); h("div", "t", tx, esc(s.chap)); h("div", "d", tx, fmt(s.t0));
      b.onclick = function () { aller(s.t0 + (i ? .05 : 0)); if (!lecture) jouer(); };
      return b;
    });

    // quiz
    var quiz = h("div", "quiz", L);
    h("h2", "", quiz, "As-tu bien compris ?");
    h("div", "sous", quiz, EP.quiz.length + " questions sur l'épisode. Réponds, puis lis l'explication.");
    var bonnes = 0, faites = 0, score = h("div", "score", null);
    EP.quiz.forEach(function (q) {
      var d = h("div", "qq", quiz); h("div", "q", d, esc(q.q));
      var bs = q.r.map(function (r, i) {
        var b = h("button", "r", d, esc(r));
        b.onclick = function () {
          bs.forEach(function (x, j) { x.disabled = true; if (j === q.ok) x.classList.add("ok"); });
          if (i !== q.ok) b.classList.add("ko"); else bonnes++;
          faites++;
          var ex = h("div", "ex", d, (i === q.ok ? "✓ Exact. " : "✗ Pas tout à fait. ") + esc(q.ex));
          if (q.voir != null) { var vo = h("button", "voir", d, "▸ Revoir ce passage de l'épisode"); vo.onclick = function () { aller(Math.max(0, q.voir - 1.5)); jouer(); (cadre.scrollIntoView || function () {}).call(cadre, { behavior: "smooth", block: "center" }); }; }
          if (faites === EP.quiz.length) { score.textContent = "Score : " + bonnes + " / " + faites + (bonnes === faites ? " — parfait !" : ""); quiz.appendChild(score); }
          hauteur();
        };
        return b;
      });
    });
    if (EP.credits && EP.credits.length) {
      var cr = h("details", "credits", L); h("summary", "", cr, "Crédits");
      EP.credits.forEach(function (c) { h("div", "", cr, esc(c)); });
      cr.addEventListener("toggle", hauteur);
    }

    // horloge : le son mène, une minuterie prend le relais sans son
    var audio = new Audio(), musique = true, src = function () { return musique ? EP.audio.mix : EP.audio.voix; };
    audio.preload = "metadata"; audio.src = src();
    var T = 0, lecture = false, vitesse = 1, sonOK = true, dernier = 0, fini = false, enAttente = null;
    audio.addEventListener("loadedmetadata", function () { if (enAttente != null) { try { audio.currentTime = enAttente; } catch (e) {} enAttente = null; } });
    audio.addEventListener("error", function () { sonOK = false; });
    audio.addEventListener("waiting", function () { cadre.classList.add("attente"); });
    audio.addEventListener("playing", function () { cadre.classList.remove("attente"); });
    audio.addEventListener("canplay", function () { cadre.classList.remove("attente"); });

    function majUI() {
      bPlay.innerHTML = lecture ? ICO.pause : ICO.play;
      temps.textContent = fmt(T) + " / " + fmt(EP.dur);
      var f = 100 * T / EP.dur; plein.style.width = f + "%"; pouce.style.left = f + "%";
      var actif = 0; EP.scenes.forEach(function (s, i) { if (T >= s.t0 - .01) actif = i; });
      bChap.forEach(function (b, i) { b.classList.toggle("on", i === actif); });
    }
    function aller(t) {
      T = cl(t, 0, EP.dur); fini = false;
      if (sonOK) { if (audio.readyState >= 1) { try { audio.currentTime = T; } catch (e) {} } else { enAttente = T; audio.load(); } }
      S.rendu(T); majUI();
    }
    function jouer() {
      if (T >= EP.dur - .05) aller(0);
      lecture = true; affiche.classList.add("off");
      if (sonOK) { audio.playbackRate = vitesse; var p = audio.play(); if (p && p.catch) p.catch(function () { sonOK = false; }); }
      dernier = performance.now(); majUI();
    }
    function pause() { lecture = false; audio.pause(); majUI(); }
    function bascule() { lecture ? pause() : jouer(); }
    function boucle(now) {
      var dt = Math.min(.1, Math.max(0, (now - dernier) / 1000)); dernier = now;
      if (lecture) {
        if (sonOK && !audio.paused && audio.readyState >= 2 && !audio.seeking && enAttente == null) {
          var at = audio.currentTime;
          if (Math.abs(at - T) > .25) T = at; else T += dt * vitesse + (at - T) * .08;
        } else if (!sonOK) T += dt * vitesse;
        else if (audio.seeking || enAttente != null) { /* on attend la fin du saut */ }
        if (T >= EP.dur) { T = EP.dur; pause(); fini = true; quiz.scrollIntoView && setTimeout(function () { quiz.scrollIntoView({ behavior: "smooth", block: "start" }); }, 600); }
        S.rendu(T); majUI();
      }
      requestAnimationFrame(boucle);
    }
    requestAnimationFrame(boucle);

    // barre de progression
    function tDe(ev) { var r = prog.getBoundingClientRect(); return cl((ev.clientX - r.left) / r.width, 0, 1) * EP.dur; }
    function nomChap(t) { var n = EP.scenes[0].chap; EP.scenes.forEach(function (s) { if (t >= s.t0) n = s.chap; }); return n; }
    var glisse = false, reprise = false;
    prog.addEventListener("pointerdown", function (ev) { glisse = true; reprise = lecture; if (lecture) pause(); prog.setPointerCapture(ev.pointerId); prog.classList.add("glisse"); aller(tDe(ev)); });
    prog.addEventListener("pointermove", function (ev) {
      var t = tDe(ev); bulle.style.left = (100 * t / EP.dur) + "%"; bulle.textContent = fmt(t) + " · " + nomChap(t);
      if (glisse) aller(t);
    });
    prog.addEventListener("pointerup", function () { glisse = false; prog.classList.remove("glisse"); affiche.classList.add("off"); if (reprise) jouer(); });

    bPlay.onclick = bascule; gp.onclick = function (ev) { ev.stopPropagation(); jouer(); };
    cadre.addEventListener("click", function () { bascule(); });
    cadre.addEventListener("dblclick", function () { pleinEcran(); });
    bM.onclick = function () { aller(T - 10); }; bP.onclick = function () { aller(T + 10); };
    var VIT = [1, 1.25, 1.5, 0.85];
    bVit.onclick = function () { vitesse = VIT[(VIT.indexOf(vitesse) + 1) % VIT.length]; audio.playbackRate = vitesse; bVit.innerHTML = '<span class="mono">' + String(vitesse).replace(".", ",") + "×</span>"; };
    bMus.onclick = function () {
      musique = !musique; bMus.classList.toggle("on", musique);
      var l = lecture; audio.pause(); audio.src = src(); sonOK = true;
      enAttente = T; audio.load(); if (l) jouer();
    };
    var cc = false;
    bCC.onclick = function () { cc = !cc; bCC.classList.toggle("on", cc); S.sous(cc); S.rendu(T); };

    // plein écran (vrai si possible, sinon en couvrant la fenêtre)
    function estPlein() { return L.classList.contains("plein"); }
    function pleinEcran() {
      if (estPlein()) { sortirPlein(); return; }
      L.classList.add("plein"); ajuste();
      if (boite.requestFullscreen) {
        boite.requestFullscreen().then(function () { try { screen.orientation.lock("landscape").catch(function () {}); } catch (e) {} }).catch(function () { pseudo(); });
      } else if (boite.webkitRequestFullscreen) { boite.webkitRequestFullscreen(); } else pseudo();
    }
    function pseudo() { document.body.classList.add("pseudo"); history.pushState({ seriePlein: 1 }, ""); }
    function sortirPlein() {
      L.classList.remove("plein"); document.body.classList.remove("pseudo");
      if (document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(function () {});
      else if (history.state && history.state.seriePlein) history.back();
      setTimeout(ajuste, 50);
    }
    bFS.onclick = pleinEcran;
    document.addEventListener("fullscreenchange", function () { if (!document.fullscreenElement && estPlein() && !document.body.classList.contains("pseudo")) { L.classList.remove("plein"); } setTimeout(ajuste, 60); });
    addEventListener("popstate", function () { if (estPlein() && document.body.classList.contains("pseudo")) { L.classList.remove("plein"); document.body.classList.remove("pseudo"); setTimeout(ajuste, 50); } });

    document.addEventListener("keydown", function (ev) {
      if (/input|textarea/i.test(ev.target.tagName)) return;
      var k = ev.key;
      if (k === " " || k === "k") { ev.preventDefault(); bascule(); }
      else if (k === "ArrowLeft") { aller(T - 5); } else if (k === "ArrowRight") { aller(T + 5); }
      else if (k === "f") pleinEcran(); else if (k === "m") bMus.onclick(); else if (k === "c") bCC.onclick();
      else if (k === "Escape" && estPlein()) sortirPlein();
    });

    if ("mediaSession" in navigator) {
      try {
        navigator.mediaSession.metadata = new MediaMetadata({ title: "Ép. " + EP.num + " · " + EP.titre, artist: "Philo · L'Index raisonné", album: EP.notion });
        navigator.mediaSession.setActionHandler("play", jouer); navigator.mediaSession.setActionHandler("pause", pause);
        navigator.mediaSession.setActionHandler("seekbackward", function () { aller(T - 10); });
        navigator.mediaSession.setActionHandler("seekforward", function () { aller(T + 10); });
      } catch (e) {}
    }

    // mise à l'échelle de la scène
    function ajuste() {
      var w = cadre.clientWidth, hh = cadre.clientHeight, k = Math.min(w / W, hh / H);
      S.el.style.transform = "translate(" + ((w - W * k) / 2).toFixed(1) + "px," + ((hh - H * k) / 2).toFixed(1) + "px) scale(" + k.toFixed(5) + ")";
      hauteur();
    }
    function hauteur() { if (EMBED && parent !== window) parent.postMessage({ type: "serie-h", code: EP.code, h: document.documentElement.scrollHeight }, "*"); }
    if (window.ResizeObserver) new ResizeObserver(ajuste).observe(cadre); else addEventListener("resize", ajuste);
    addEventListener("message", function (ev) { if (ev.data && ev.data.type === "serie-pause") pause(); });
    ajuste();
    // affiche : le carton de titre
    var titre = EP.vis.filter(function (v) { return v.type === "titre"; })[0];
    var tA = Q.get("t") != null ? parseFloat(Q.get("t")) : null;
    S.rendu(titre ? titre.t0 + 2.6 : 2);
    if (tA != null) { aller(tA); affiche.classList.add("off"); }
    majUI(); setTimeout(hauteur, 300);
  }

  window.SERIE = { lancer: lancer };
})();
