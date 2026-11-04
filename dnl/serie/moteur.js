/* DNL History — séries vidéo des chapitres (en anglais) : moteur du lecteur.
   Copie du moteur des vidéos de cours de physique-chimie (pc/serie/moteur.js, lui-même copie du moteur des séries philo),
   textes du lecteur en anglais, couleurs « Atlas de révision » sur fond sombre (bleu de Prusse, parchemin, doré).
   Ajout propre à l'histoire : type globe, la carte animée du chapitre (dnl/cartes/<code>.html?pilote=1) pilotée par le temps
   de la vidéo ; graphe, exo et pause sont repris du moteur PC. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  var C = { iv: "#f3efe4", iv2: "#d9d2c0", sa: "#e6cb8b", sa2: "#c4a052", ca: "#d0705c", te: "#5aa596", eau: "#74b9d8", nuit: "#0e1525", el: "#8fc7e8", uv: "#b48cff", rouge: "#e0604f", vert: "#7ce08a", or: "#ffd24a" };

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
  // texte enrichi pour les sciences : x^{2} ou 10^-19 (exposant), E_c ou P_{reçue} (indice), [[num|den]] (fraction)
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/\[\[([^|\]]*)\|([^\]]*)\]\]/g, '<span class="frac"><span class="nu">$1</span><span class="de">$2</span></span>')
      .replace(/\^\{([^}]*)\}/g, "<sup>$1</sup>").replace(/\^([\u2212-]?[0-9]+)/g, function (_, x) { return "<sup>" + x.replace("-", "\u2212") + "</sup>"; })
      .replace(/_\{([^}]*)\}/g, "<sub>$1</sub>").replace(/_([^\s{<&_])/g, "<sub>$1</sub>");
  }
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
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(255,139,62," + (0.7 * (1 - f)).toFixed(2) + ")";
      c.sp.style.backgroundSize = (100 * E(p)).toFixed(0) + "% 3px";
    });
  }

  // étape k d'un visuel : instant (repère {id.k}) ou, à défaut, une valeur de repli
  function et(v, k, repli) { return v.et && v.et[k] != null ? v.et[k] : v.t0 + repli; }

  /* ---------- illustrations ---------- */
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

  var ICONES = {
    soleil: ["M50 32 a18 18 0 1 0 0.1 0", "M50 6 V18 M50 82 V94 M6 50 H18 M82 50 H94 M19 19 L27 27 M73 73 L81 81 M81 19 L73 27 M27 73 L19 81"],
    photon: ["M6 50 C14 32 22 32 28 50 S40 68 48 50 S62 32 70 50 S84 68 94 50"],
    capteur: ["M18 22 H82 V78 H18 Z", "M34 22 V78 M50 22 V78 M66 22 V78 M18 40 H82 M18 58 H82"],
    del: ["M34 60 V36 a16 16 0 0 1 32 0 V60 Z", "M26 60 H74", "M42 60 V92 M58 60 V86", "M76 26 L90 16 M78 42 L94 40"],
    laser: ["M8 38 H50 V62 H8 Z", "M50 50 H94", "M84 42 L94 50 L84 58"],
    spectro: ["M16 76 L50 22 L84 76 Z", "M4 56 L36 52", "M62 46 L96 30 M62 50 L96 50 M62 54 L96 70"],
    panneau: ["M14 70 L30 26 H86 L70 70 Z", "M22 48 H78 M50 26 L42 70", "M42 70 V90 M30 90 H54"]
  };
  function icone(nom, parent) {
    var s = sv("svg", { viewBox: "0 0 100 100" }, parent);
    return (ICONES[nom] || []).map(function (d) {
      return sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 4.5, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    });
  }
  var ILLU = {};
  // couleur d'une radiation visible (approximation) ; hors du visible : violet pâle (UV) ou rouge sombre (IR)
  function couleurLambda(l) {
    if (l < 380) return "#b48cff";
    if (l > 780) return "#8a2b1f";
    var r = 0, g = 0, b = 0;
    if (l < 440) { r = (440 - l) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; } else if (l < 510) { g = 1; b = (510 - l) / 20; }
    else if (l < 580) { r = (l - 510) / 70; g = 1; } else if (l < 645) { r = 1; g = (645 - l) / 65; } else r = 1;
    var f = l < 420 ? .3 + .7 * (l - 380) / 40 : l > 700 ? .3 + .7 * (780 - l) / 80 : 1;
    function c(x) { return Math.round(255 * Math.pow(x * f, .8)); }
    return "rgb(" + c(r) + "," + c(g) + "," + c(b) + ")";
  }
  function sinus(x0, x1, y, A, lam, ph, pas) { // tracé d'une sinusoïde de x0 à x1
    var d = "";
    for (var x = x0, i = 0; x <= x1 + .01; x += (pas || 3), i++) d += (i ? " L" : "M") + x.toFixed(1) + " " + (y - A * Math.sin(2 * Math.PI * (x - x0) / lam - ph)).toFixed(1);
    return d;
  }
  function paquet(x, y, lam, long, A, ph) { // photon dessiné comme un petit paquet d'onde
    var d = "";
    for (var s = -long / 2, i = 0; s <= long / 2; s += 1.5, i++) {
      var env = Math.pow(Math.cos(Math.PI * s / long), 2);
      d += (i ? " L" : "M") + (x + s).toFixed(1) + " " + (y - A * env * Math.sin(2 * Math.PI * s / lam - ph)).toFixed(1);
    }
    return d;
  }
  function fleche(g, d, col, ep) {
    var p = sv("path", { d: d, fill: "none", stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round" }, g);
    return { p: p, pointe: pointe(g, p, col, Math.max(15, (ep || 3) * 1.9)) };
  }

  // l'onde : sinusoïde qui avance, longueur d'onde λ, célérité c ; {id.2} : une onde de fréquence double en dessous
  ILLU.onde = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), x0 = 40, x1 = W_ - 40, lam = v.lam || 230, y1 = H_ * (v.deux ? .3 : .45);
    var o1 = sv("path", { d: "", fill: "none", stroke: v.c1 || "#ff4a3d", "stroke-width": 5, "stroke-linecap": "round" }, g);
    var br = sv("g", {}, g), yb = y1 - 92;
    var bt = sv("path", { d: "M" + (x0 + lam * .25) + " " + yb + " H" + (x0 + lam * 1.25), stroke: C.iv, "stroke-width": 2.4, fill: "none" }, br);
    sv("path", { d: "M" + (x0 + lam * .25) + " " + (yb - 12) + " v24 M" + (x0 + lam * 1.25) + " " + (yb - 12) + " v24", stroke: C.iv, "stroke-width": 2.4 }, br);
    var tl1 = etiquette(br, x0 + lam * .75, yb - 18, "λ", { fs: 40, c: C.sa, cls: "ser" });
    var cg = sv("g", {}, g), fc = fleche(cg, "M" + (x1 - 170) + " " + (y1 + 108) + " H" + (x1 - 20), C.sa, 3.5);
    etiquette(cg, x1 - 95, y1 + 150, "c = 3,00 × 10⁸ m/s", { fs: 24, c: C.iv2 });
    var o2, t2;
    if (v.deux) {
      o2 = sv("path", { d: "", fill: "none", stroke: v.c2 || "#b48cff", "stroke-width": 5, "stroke-linecap": "round" }, g);
      t2 = etiquette(g, W_ / 2, H_ * .93, v.l2 || "fréquence double : longueur d'onde deux fois plus courte", { fs: 24, c: C.iv2 });
    }
    return function (t, st) {
      var tl = st.tl, p = E(P(tl, 0, 1.4)), ph = t * 2.2;
      o1.setAttribute("d", sinus(x0, x0 + (x1 - x0) * p, y1, 46, lam, ph));
      var b = E(P(t, et(v, "1", 1.6), .7)); op(br, b);
      op(cg, E(P(t, et(v, "c", 2.6), .7))); trace(fc.p, P(t, et(v, "c", 2.6), .8)); fc.pointe();
      if (o2) {
        var k = et(v, "2", 1e9), q = E(P(t, k, 1.4));
        o2.setAttribute("d", q > 0 ? sinus(x0, x0 + (x1 - x0) * q, H_ * .7, 46, lam / 2, ph * 2) : "M0 0");
        op(t2, E(P(t, k + 1, .6)));
      }
    };
  };

  // le spectre électromagnétique : UV | visible | IR ; {id.2} énergies en eV ; {id.3} flèche « énergie du photon »
  ILLU.spectre = function (s, v) {
    var W_ = v.w, g = sv("g", {}, s), y = 70, hb = 90, xa = 30, xb = W_ - 30;
    var Lx = function (l) { return l <= 400 ? xa + (l - 100) / 300 * 230 : l <= 800 ? xa + 230 + (l - 400) / 400 * 560 : xa + 790 + (l - 800) / 1200 * (xb - xa - 790); };
    var df = sv("defs", {}, s), lg = sv("linearGradient", { id: "spv", x1: 0, x2: 1 }, df);
    for (var l = 400; l <= 800; l += 20) sv("stop", { offset: ((l - 400) / 400).toFixed(3), "stop-color": couleurLambda(l) }, lg);
    var zuv = sv("rect", { x: Lx(100), y: y, width: Lx(400) - Lx(100), height: hb, fill: "rgba(180,140,255,.22)", stroke: "rgba(180,140,255,.6)" }, g);
    var zvi = sv("rect", { x: Lx(400), y: y, width: Lx(800) - Lx(400), height: hb, fill: "url(#spv)" }, g);
    var zir = sv("rect", { x: Lx(800), y: y, width: Lx(2000) - Lx(800), height: hb, fill: "rgba(138,43,31,.35)", stroke: "rgba(255,74,61,.45)" }, g);
    var noms = [[250, "Ultraviolet"], [600, "Visible"], [1400, "Infrarouge"]].map(function (n, i) {
      return etiquette(g, Lx(n[0]), y - 22, n[1], { fs: 27, c: i === 1 ? C.iv : i ? "#ff8a7a" : "#cdb6ff" });
    });
    var gr = [100, 400, 800, 2000].map(function (l) {
      var gg = sv("g", {}, g); sv("line", { x1: Lx(l), x2: Lx(l), y1: y + hb, y2: y + hb + 12, stroke: C.iv, "stroke-width": 2 }, gg);
      etiquette(gg, Lx(l), y + hb + 40, (l === 2000 ? "…" : l + " nm"), { fs: 22, c: C.iv2 }); return gg;
    });
    var ev = sv("g", {}, g);
    [[400, "3,1 eV"], [800, "1,6 eV"]].forEach(function (a) { etiquette(ev, Lx(a[0]), y + hb + 82, a[1], { fs: 26, c: C.sa, fw: 700 }); });
    etiquette(ev, Lx(150), y + hb + 82, "plus de 3,1 eV", { fs: 22, c: "#cdb6ff" });
    etiquette(ev, Lx(1300), y + hb + 82, "moins de 1,6 eV", { fs: 22, c: "#ff8a7a" });
    var fg = sv("g", {}, g), f = fleche(fg, "M" + (xb - 40) + " " + (y + hb + 140) + " H" + (xa + 40), C.sa, 4);
    etiquette(fg, W_ / 2, y + hb + 182, "l'énergie du photon augmente quand λ diminue", { fs: 25, c: C.iv });
    return function (t, st) {
      var tl = st.tl;
      [zuv, zvi, zir].forEach(function (z, i) { op(z, E(P(tl, .2 + i * .35, .7))); });
      noms.forEach(function (n, i) { op(n, E(P(tl, .5 + i * .35, .6))); });
      gr.forEach(function (gg, i) { op(gg, E(P(tl, 1.2 + i * .15, .5))); });
      op(ev, E(P(t, et(v, "2", 1e9), .7)));
      var k = et(v, "3", 1e9); op(fg, E(P(t, k, .4))); trace(f.p, P(t, k, 1.2)); f.pointe();
    };
  };

  // intensité ≠ énergie : faisceau faible (peu de photons), intense (beaucoup, même énergie), bleu (photons plus énergétiques)
  ILLU.faisceau = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s);
    var lignes = [
      { y: H_ * .2, n: 4, lam: 22, col: "#ff4a3d", t: "rouge, faible : peu de photons", k: "1" },
      { y: H_ * .5, n: 14, lam: 22, col: "#ff4a3d", t: "rouge, intense : plus de photons, chacun la même énergie", k: "2" },
      { y: H_ * .8, n: 4, lam: 11, col: "#5a8cff", t: "bleu : chaque photon porte plus d'énergie", k: "3" }
    ];
    lignes.forEach(function (L, i) {
      L.g = sv("g", {}, g);
      L.lampe = sv("circle", { cx: 50, cy: L.y, r: 22, fill: L.col, opacity: .9 }, L.g);
      L.ph = []; for (var j = 0; j < L.n; j++) L.ph.push({ p: sv("path", { d: "", fill: "none", stroke: L.col, "stroke-width": 3.4, "stroke-linecap": "round" }, L.g), o: alea(j * 7 + i * 31), dy: (alea(j * 13 + i) - .5) * 34 });
      L.tx = etiquette(L.g, W_ / 2 + 30, L.y + 58, L.t, { fs: 24, c: C.iv2 });
    });
    return function (t, st) {
      lignes.forEach(function (L, i) {
        var k = et(v, L.k, .3 + i * 1.5), a = E(P(t, k, .6));
        op(L.g, a);
        L.ph.forEach(function (q) {
          var u = ((t - k) * .16 + q.o) % 1, x = 90 + u * (W_ - 140);
          q.p.setAttribute("d", t >= k ? paquet(x, L.y + q.dy, L.lam, 46, 9, t * 12) : "M0 0");
          q.p.style.opacity = Math.min(1, u * 8, (1 - u) * 8);
        });
      });
    };
  };

  // cellule photoélectrique : ampoule vide, cathode, anode, générateur, ampèremètre ;
  // {id.2} lumière rouge sous le seuil : plus d'électron, plus de courant ; {id.3} retour à l'UV, plus intense
  ILLU.cellpe = function (s, v) {
    var g = sv("g", {}, s), cx = 330, cy = 200;
    sv("ellipse", { cx: cx, cy: cy, rx: 190, ry: 140, fill: "rgba(127,227,255,.05)", stroke: "rgba(242,231,218,.45)", "stroke-width": 2.5 }, g);
    etiquette(g, cx, cy - 152, "ampoule vidée d'air", { fs: 20, c: C.iv2 });
    sv("path", { d: "M215 110 Q180 200 215 290", fill: "none", stroke: "#c9b79f", "stroke-width": 12, "stroke-linecap": "round" }, g);
    etiquette(g, 170, 330, "cathode (−)", { fs: 22, c: C.iv });
    sv("line", { x1: 440, y1: 150, x2: 440, y2: 250, stroke: "#c9b79f", "stroke-width": 8, "stroke-linecap": "round" }, g);
    etiquette(g, 470, 330, "anode (+)", { fs: 22, c: C.iv });
    var fil = "M200 290 V420 H330 M390 420 H560 V200 H440";
    sv("path", { d: fil + " M440 200 V150", fill: "none", stroke: "rgba(242,231,218,.6)", "stroke-width": 3 }, g);
    sv("circle", { cx: 360, cy: 420, r: 28, fill: "#24180e", stroke: C.iv, "stroke-width": 2.5 }, g);
    etiquette(g, 360, 429, "A", { fs: 26, c: C.iv, fw: 700 });
    var aig = sv("line", { x1: 360, y1: 432, x2: 360, y2: 400, stroke: C.sa, "stroke-width": 3, "stroke-linecap": "round" }, g);
    sv("rect", { x: 545, y: 290, width: 30, height: 50, fill: "#24180e", stroke: C.iv, "stroke-width": 2 }, g);
    etiquette(g, 610, 322, "générateur", { fs: 20, c: C.iv2, ancre: "start" });
    var rayons = [0, 1, 2].map(function (i) { return sv("path", { d: "", fill: "none", "stroke-width": 3.4, "stroke-linecap": "round" }, g); });
    var lum = etiquette(g, 70, 70, "", { fs: 22, c: C.iv2, ancre: "start" });
    var els = []; for (var i = 0; i < 9; i++) els.push(sv("circle", { r: 7, fill: C.el }, g));
    var cir = []; for (var j = 0; j < 12; j++) cir.push(sv("circle", { r: 5, fill: C.el, opacity: .85 }, g));
    var pc = sv("path", { d: "M440 200 H560 V420 H390 M330 420 H200 V290", fill: "none", stroke: "none" }, g), Lc = 0;
    return function (t, st) {
      var k2 = et(v, "2", 1e9), k3 = et(v, "3", 1e9), rouge = t >= k2 && t < k3, fort = t >= k3;
      var col = rouge ? "#ff4a3d" : "#b48cff", lam = rouge ? 26 : 12;
      lum.textContent = rouge ? "lumière rouge, très intense (λ > λ₀)" : fort ? "ultraviolet, plus intense" : "ultraviolet (λ < λ₀)";
      rayons.forEach(function (r, i) {
        var u = ((t * .5 + i / 3) % 1), x = 60 + u * 130, y = 90 + i * 70 + u * 30;
        r.setAttribute("d", paquet(x, y, lam, 40, 8, t * 12)); r.setAttribute("stroke", col); r.style.opacity = Math.min(1, (1 - u) * 6, u * 6);
      });
      var n = rouge ? 0 : fort ? 9 : 5;
      els.forEach(function (e, i) {
        var u = ((t * .45 + alea(i) ) % 1), y0 = 130 + alea(i + 9) * 140;
        e.setAttribute("cx", (205 + u * 230).toFixed(1)); e.setAttribute("cy", (y0 + (200 - y0) * u).toFixed(1));
        e.style.opacity = i < n ? Math.min(1, u * 10, (1 - u) * 10) : 0;
      });
      if (!Lc) Lc = pc.getTotalLength ? pc.getTotalLength() : 0;
      cir.forEach(function (c, i) {
        if (!Lc) return;
        var p = pc.getPointAtLength(((t * 60 + i * Lc / 12) % Lc));
        c.setAttribute("cx", p.x.toFixed(1)); c.setAttribute("cy", p.y.toFixed(1)); c.style.opacity = n ? (fort ? .95 : .7) : 0;
      });
      var ang = (n ? (fort ? 55 : 30) + 3 * Math.sin(t * 5) : 0) * Math.PI / 180;
      aig.setAttribute("x2", (360 + 30 * Math.sin(ang)).toFixed(1)); aig.setAttribute("y2", (432 - 30 * Math.cos(ang)).toFixed(1));
    };
  };

  // chaîne énergétique d'une cellule photovoltaïque (largeurs des flèches proportionnelles aux énergies)
  ILLU.chaine = function (s, v) {
    var g = sv("g", {}, s), W_ = v.w, yc = 150, eta = v.eta || .15;
    var fe = fleche(g, "M30 " + yc + " H300", "#ffd24a", 46);
    etiquette(g, 160, yc - 64, "énergie lumineuse reçue", { fs: 24, c: C.iv });
    var bx = sv("rect", { x: 320, y: yc - 70, width: 300, height: 140, rx: 18, fill: "#2e1c0e", stroke: C.sa, "stroke-width": 3 }, g);
    var bt = etiquette(g, 470, yc + 9, v.boite || "cellule photovoltaïque", { fs: 26, c: C.iv, fw: 700 });
    var fu = fleche(g, "M640 " + yc + " H" + (W_ - 40), C.el, 46 * eta * 1.6 + 6);
    var tu = etiquette(g, (640 + W_) / 2, yc - 44, "énergie électrique (utile)", { fs: 24, c: C.el });
    var fp = fleche(g, "M470 " + (yc + 80) + " V" + (yc + 230), "#ff6b5b", 40);
    var tp = etiquette(g, 500, yc + 200, "pertes : surtout thermique, et lumière réfléchie", { fs: 23, c: "#ff8a7a", ancre: "start" });
    var pc_ = etiquette(g, (640 + W_) / 2, yc + 56, "≈ " + Math.round(eta * 100) + " %", { fs: 30, c: C.el, fw: 700 });
    return function (t, st) {
      var tl = st.tl;
      trace(fe.p, P(tl, .1, .8)); fe.pointe();
      op(bx, E(P(tl, .6, .5))); op(bt, E(P(tl, .8, .5)));
      var k = et(v, "2", 1.6); trace(fu.p, P(t, k, .8)); fu.pointe(); op(tu, E(P(t, k + .4, .5)));
      var k3 = et(v, "3", 2.6); trace(fp.p, P(t, k3, .8)); fp.pointe(); op(tp, E(P(t, k3 + .4, .5)));
      op(pc_, E(P(t, et(v, "4", 3.4), .5)));
      [fe.pointe(), fu.pointe(), fp.pointe()].forEach(function (x, i) { op(x, [P(tl, .7, .2), P(t, k + .7, .2), P(t, k3 + .7, .2)][i]); });
    };
  };

  // dualité : photons envoyés un par un sur un écran derrière deux fentes ; les impacts dessinent des franges
  ILLU.dualite = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), xe = W_ - 120;
    sv("rect", { x: xe, y: 30, width: 70, height: H_ - 60, fill: "#0c0804", stroke: "rgba(242,231,218,.4)" }, g);
    sv("path", { d: "M220 30 V" + (H_ / 2 - 40) + " M220 " + (H_ / 2 - 20) + " V" + (H_ / 2 + 20) + " M220 " + (H_ / 2 + 40) + " V" + (H_ - 30), stroke: C.iv, "stroke-width": 8 }, g);
    etiquette(g, 220, H_ - 4, "deux fentes", { fs: 21, c: C.iv2 });
    etiquette(g, xe + 35, H_ - 4, "écran", { fs: 21, c: C.iv2 });
    var N = 700, pts = [], k = 0;
    while (pts.length < N && k < 20000) { // tirage selon l'intensité des franges (cos² sous une enveloppe)
      var y = alea(k * 3 + 1), w = Math.pow(Math.cos((y - .5) * 26), 2) * Math.exp(-Math.pow((y - .5) * 3.2, 2));
      if (alea(k * 3 + 2) < w) pts.push([xe + 6 + alea(k * 3 + 3) * 58, 34 + y * (H_ - 68)]);
      k++;
    }
    var dots = pts.map(function (p) { return sv("circle", { cx: p[0].toFixed(1), cy: p[1].toFixed(1), r: 2.6, fill: "#ffd24a", opacity: 0 }, g); });
    var vol = sv("circle", { r: 6, fill: "#ffd24a" }, g);
    etiquette(g, 110, 40, "source très faible", { fs: 20, c: C.iv2 });
    return function (t, st) {
      var tl = st.tl, d = Math.max(4, (v.t1 - v.t0) * .8), n = Math.floor(N * Math.pow(cl(tl / d, 0, 1), 1.6));
      dots.forEach(function (c, i) { c.setAttribute("opacity", i < n ? .9 : 0); });
      var u = (tl * 1.6) % 1, cible = pts[Math.min(N - 1, n)];
      vol.setAttribute("cx", (60 + u * (cible[0] - 60)).toFixed(1));
      vol.setAttribute("cy", (u < .45 ? H_ / 2 + 0 : H_ / 2 + (cible[1] - H_ / 2) * (u - .45) / .55).toFixed(1));
      op(vol, n < N ? 1 : 0);
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
    var e = o.el; e.classList.add("v-question"); if (v.bande) e.classList.add("bande");
    var tt = h("div", "tt", e);
    var sp = mots(tt, v.t);
    sp[0].innerHTML = '<span class="gu">“</span>' + sp[0].innerHTML;
    sp[sp.length - 1].innerHTML += '<span class="gu">”</span>';
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
      if (n > 6) {          // beaucoup de mots : deux colonnes, sans chevauchement
        var rangs = Math.ceil(n / 2), c = i % 2, r = Math.floor(i / 2);
        d.style.left = (c ? 920 : 360) + (alea(i) - .5) * 40 + "px";
        d.style.top = (370 + (r - (rangs - 1) / 2) * (v.centre ? 128 : 112) + (v.centre && r >= rangs / 2 ? 30 : 0) - (v.centre && r < rangs / 2 ? 30 : 0)) + "px";
        d.style.fontSize = 44 + Math.round(alea(i + 7) * 8) + "px";
      } else {
        d.style.left = (640 + Math.cos(ang) * rx) + "px"; d.style.top = (370 + Math.sin(ang) * ry) + "px";
        d.style.fontSize = (v.centre ? 46 : 58) + Math.round(alea(i + 7) * 14) + "px";
      }
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
    var bg = h("div", "barre-g", c), te = h("div", "te", c, esc(note ? (v.titre || v.terme || "Watch out") : v.terme));
    var tx = h("div", "tx serif", c), sp = mots(tx, v.t, "mot-l cle"), etp = v.etape ? h("div", "et", c, esc(v.etape)) : null;
    if (v.plus) h("div", "badge", c, "Going further");
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
    var au = h("div", "au", e, "— <b>" + esc(v.a || "") + "</b>" + (v.o ? ", " + esc(v.o) : "") + (v.para ? '<span class="ap">≈ PARAPHRASE</span>' : ""));
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
    [["1850", 1850], ["1900", 1900], ["1945", 1945], ["2000", 2000]].forEach(function (z) {
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
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(255,139,62,.9)";
        op(mf.an, E(P(st.tl, 2, .5)));
      }
    };
  };

  TYPES.cols = function (o, v) {
    var e = o.el; e.classList.add("v-cols"); o.entree = "aucune";
    var g = h("div", "col g", e), d = h("div", "col d", e);
    h("div", "t", g, esc(v.g)); h("div", "q", g, esc(v.gq || "")); h("div", "t", d, esc(v.d)); h("div", "q", d, esc(v.dq || ""));
    var vs = h("div", "vs", e, esc(v.vs || "≠")), rp = v.repere ? h("div", "rp", e, "<span>✻ " + esc(v.repere) + "</span>") : null;
    if (v.plus) h("div", "badge", e, "Going further");
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
        c.c.style.borderColor = actif ? "rgba(255,139,62," + (0.5 + 0.4 * pul) + ")" : "rgba(242,231,218,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(255,139,62,.25)" : "none";
      });
    };
  };

  TYPES.liste = function (o, v) {
    var e = o.el; e.classList.add("v-liste"); if (v.petit) e.classList.add("petit");
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
    var tri = v.items.slice().sort(function (a, b) { return a.d - b.d; });
    // dates trop serrées (plus de deux rangées nécessaires) : espacement régulier, ordre chronologique conservé
    var fin = RANGS.map(function () { return -1e9; }), serre = false;
    tri.forEach(function (it) { var x = X(it.d), r = 0; while (r < RANGS.length - 1 && x - fin[r] < 128) r++; fin[r] = x; if (r > 1) serre = true; });
    if (serre) {
      rupt.style.display = "none"; ans.forEach(function (a) { a.style.display = "none"; });
      var pas = tri.length > 1 ? 1040 / (tri.length - 1) : 0;
      X = function (an) { var k = tri.findIndex(function (it) { return it.d === an; }); return 120 + k * pas; };
    }
    fin = RANGS.map(function () { return -1e9; });
    var its = tri.map(function (it, i) {
      var p = h("div", "p", e), x = serre ? 120 + i * pas : X(it.d), r = serre ? i % 2 : 0;
      if (!serre) { while (r < RANGS.length - 1 && x - fin[r] < 128) r++; }
      fin[r] = x;
      var R = RANGS[r];
      p.style.left = x + "px"; p.style.top = R.top + "px";
      var tige = h("div", "tige", p); tige.style.top = R.tige[0] + "px"; tige.style.height = R.tige[1] + "px";
      var md = h("div", "md", p);
      if (it.img) { var im = h("img", "", md); im.src = "img/" + it.img + ".jpg"; im.alt = it.nom; } else md.textContent = it.nom[0];
      h("div", "nm", p, esc(it.nom)); h("div", "dt", p, it.d < 0 ? "−" + (-it.d) : String(it.d));
      if (it.q) h("div", "q", p, esc(it.q));
      p._k = v.items.indexOf(it) + 1;
      return p;
    });
    return function (t, st) {
      tr(axe, "scaleX(" + EIO(P(st.tl, 0, 1.4)) + ")");
      op(rupt, E(P(st.tl, 1, .5))); ans.forEach(function (a) { op(a, E(P(st.tl, 1, .6))); });
      its.forEach(function (p, i) { var q = P(t, et(v, String(p._k), .8 + i * .28), .6); op(p, E(q)); tr(p, "translateY(" + 20 * (1 - E(q)) + "px) scale(" + (0.7 + 0.3 * EB(q)) + ")"); });
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
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "DNL History · Terminale BFI");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    tt.style.fontSize = Math.min(120, Math.floor(2300 / Math.max(12, String(v.serie).length))) + "px"; tt.style.textAlign = "center";
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, "The chapter in video · episode " + v.num);
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

  // notions du programme abordées : encadré au début d'une partie, ou étiquette quand le texte touche une autre notion
  TYPES.notion = function (o, v) {
    var e = o.el; e.classList.add("v-notion"); o.entree = "aucune"; o.disp = "flex";
    if (v.titre) e.classList.add("liste");
    var tete = h("div", "nt-t", e, esc(v.titre || "Notion"));
    var pills = v.items.map(function (x, i) {
      var p = h("span", "nt-p" + (v.titre && i === 0 ? " prin" : ""), e, esc(x.charAt(0).toUpperCase() + x.slice(1)));
      return p;
    });
    return function (t, st) {
      var tl = st.tl, d = v.t1 - v.t0, a = E(P(tl, 0, .5)), out = EIO(P(tl, d - .6, .6));
      op(e, a * (1 - out));
      tr(e, "translateX(" + (40 * (1 - a) + 30 * out).toFixed(1) + "px)");
      op(tete, E(P(tl, .1, .4)));
      pills.forEach(function (p, i) {
        var q = P(tl, .25 + i * .18, .45);
        op(p, E(q)); tr(p, "translateY(" + (8 * (1 - E(q))).toFixed(1) + "px) scale(" + (0.85 + 0.15 * EB(q)).toFixed(3) + ")");
      });
    };
  };

  TYPES.frappe = function (o, v) {
    var e = o.el; e.classList.add("v-frappe"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fr-fond", e), m = h("div", "fr-mot", e, esc(v.t));
    m.style.fontSize = Math.min(150, Math.floor(1120 / (String(v.t).length * 0.8))) + "px";   // un mot long tient dans l'écran
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
    h("div", "fl-te", c, "Key point");
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
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(255,139,62,.35)";
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
    if (v.plus) h("div", "badge", e, "Going further").style.top = "-10px";
    var f = ILLU[v.nom] ? ILLU[v.nom](s, v) : function () {};
    return f;
  };

  // lentille convergente : axe, foyers, objet AB ; {id.1} rayon parallèle → F′, {id.2} rayon par O, {id.3} rayon par F,
  // {id.4} image A′B′ (position par la relation de conjugaison). v.oa : position de l'objet en multiples de f′ (négative)
  ILLU.lentille = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), y0 = H_ * .55, x0 = W_ * .5, f = v.f || 120, hA = v.ha || 70;
    var oa = (v.oa || -2.5) * f, oai = 1 / (1 / f + 1 / oa), gam = oai / oa, xa = x0 + oa, xi = x0 + oai, hi = hA * gam;
    var Y = function (hh) { return y0 - hh; };
    var axe = sv("line", { x1: 20, x2: W_ - 20, y1: y0, y2: y0, stroke: "rgba(242,231,218,.5)", "stroke-width": 1.6, "stroke-dasharray": "8 6" }, g);
    var len = sv("g", {}, g);
    sv("line", { x1: x0, x2: x0, y1: y0 - 160, y2: y0 + 160, stroke: C.el, "stroke-width": 3.4 }, len);
    sv("path", { d: "M" + (x0 - 12) + " " + (y0 - 146) + " L" + x0 + " " + (y0 - 162) + " L" + (x0 + 12) + " " + (y0 - 146) +
      "M" + (x0 - 12) + " " + (y0 + 146) + " L" + x0 + " " + (y0 + 162) + " L" + (x0 + 12) + " " + (y0 + 146), fill: "none", stroke: C.el, "stroke-width": 3.4 }, len);
    var lab = sv("g", {}, g);
    [[x0, "O"], [x0 - f, "F"], [x0 + f, "F′"]].forEach(function (p) {
      sv("circle", { cx: p[0], cy: y0, r: 4.5, fill: C.iv }, lab);
      etiquette(lab, p[0], y0 + 30, p[1], { fs: 24, c: C.iv, cls: "ser" });
    });
    var obj = sv("g", {}, g);
    sv("line", { x1: xa, x2: xa, y1: y0, y2: Y(hA) + 10, stroke: C.sa, "stroke-width": 4 }, obj);
    sv("path", { d: "M" + (xa - 9) + " " + (Y(hA) + 14) + " L" + xa + " " + Y(hA) + " L" + (xa + 9) + " " + (Y(hA) + 14) + " Z", fill: C.sa }, obj);
    etiquette(obj, xa - 18, y0 + 30, "A", { fs: 24, c: C.sa, cls: "ser" }); etiquette(obj, xa - 18, Y(hA) - 6, "B", { fs: 24, c: C.sa, cls: "ser" });
    var xe = Math.min(W_ - 20, xi + 90);
    function droite(x1, y1, x2, y2, xs) { var a = (y2 - y1) / (x2 - x1); return y1 + a * (xs - x1); }
    var r1 = sv("path", { d: "M" + xa + " " + Y(hA) + " L" + x0 + " " + Y(hA) + " L" + xe + " " + droite(x0, Y(hA), x0 + f, y0, xe).toFixed(1), fill: "none", stroke: C.or, "stroke-width": 2.6 }, g);
    var r2 = sv("path", { d: "M" + xa + " " + Y(hA) + " L" + xe + " " + droite(xa, Y(hA), x0, y0, xe).toFixed(1), fill: "none", stroke: C.vert, "stroke-width": 2.6 }, g);
    var yF = droite(xa, Y(hA), x0 - f, y0, x0);
    var r3 = sv("path", { d: "M" + xa + " " + Y(hA) + " L" + x0 + " " + yF.toFixed(1) + " L" + xe + " " + yF.toFixed(1), fill: "none", stroke: C.uv, "stroke-width": 2.6 }, g);
    var im = sv("g", {}, g);
    sv("line", { x1: xi, x2: xi, y1: y0, y2: Y(hi) - 10 * Math.sign(hi), stroke: C.vert, "stroke-width": 4 }, im);
    sv("path", { d: "M" + (xi - 9) + " " + (Y(hi) - 14 * Math.sign(hi)) + " L" + xi + " " + Y(hi) + " L" + (xi + 9) + " " + (Y(hi) - 14 * Math.sign(hi)) + " Z", fill: C.vert }, im);
    etiquette(im, xi + 22, y0 - 12, "A′", { fs: 24, c: C.vert, cls: "ser" }); etiquette(im, xi + 22, Y(hi) + 24, "B′", { fs: 24, c: C.vert, cls: "ser" });
    var lg = etiquette(g, W_ / 2, H_ - 14, v.legende || "image réelle, renversée", { fs: 23, c: C.iv2 });
    return function (t, st) {
      var tl = st.tl;
      op(axe, E(P(tl, 0, .5))); op(len, E(P(tl, .2, .6))); op(lab, E(P(tl, .5, .6))); op(obj, E(P(tl, .8, .6)));
      [r1, r2, r3].forEach(function (r, i) { var k = et(v, String(i + 1), 1.4 + i * 1.6); trace(r, EIO(P(t, k, 1.4))); });
      var k4 = et(v, "4", 6.4); op(im, E(P(t, k4, .6))); op(lg, E(P(t, k4 + .4, .6)));
    };
  };

  // l'angle sous lequel on voit un objet : œil, objet de taille h à la distance D, angle α ; {id.2} α ≈ h / D
  ILLU.angle = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), y0 = H_ * .5, xo = 90, xd = W_ - 130, hh = v.hh || 120;
    var oeil = sv("g", {}, g);
    sv("path", { d: "M" + (xo - 40) + " " + y0 + " Q" + (xo - 10) + " " + (y0 - 32) + " " + (xo + 20) + " " + y0 + " Q" + (xo - 10) + " " + (y0 + 32) + " " + (xo - 40) + " " + y0 + " Z", fill: "none", stroke: C.iv, "stroke-width": 3 }, oeil);
    sv("circle", { cx: xo - 6, cy: y0, r: 11, fill: C.el }, oeil);
    var astre = sv("circle", { cx: xd, cy: y0, r: hh, fill: "#d9d2c0", opacity: .9 }, g);
    var cra = [[-30, -40, 16], [28, 10, 22], [-10, 50, 12]].map(function (c) { return sv("circle", { cx: xd + c[0], cy: y0 + c[1], r: c[2], fill: "#b8b0a0" }, g); });
    var l1 = sv("path", { d: "M" + xo + " " + y0 + " L" + xd + " " + (y0 - hh), stroke: C.sa, "stroke-width": 2.4, fill: "none" }, g);
    var l2 = sv("path", { d: "M" + xo + " " + y0 + " L" + xd + " " + (y0 + hh), stroke: C.sa, "stroke-width": 2.4, fill: "none" }, g);
    var ax = sv("line", { x1: xo, x2: xd, y1: y0, y2: y0, stroke: "rgba(242,231,218,.4)", "stroke-dasharray": "7 6", "stroke-width": 1.5 }, g);
    var a = Math.atan(hh / (xd - xo)), R = 130;
    var arc = sv("path", { d: "M" + (xo + R * Math.cos(a)) + " " + (y0 - R * Math.sin(a)) + " A" + R + " " + R + " 0 0 1 " + (xo + R * Math.cos(a)) + " " + (y0 + R * Math.sin(a)), fill: "none", stroke: C.or, "stroke-width": 3 }, g);
    var ta = etiquette(g, xo + R + 30, y0 + 9, "α", { fs: 36, c: C.or, cls: "ser" });
    var cote = sv("g", {}, g);
    sv("line", { x1: xd + hh + 30, x2: xd + hh + 30, y1: y0 - hh, y2: y0 + hh, stroke: C.iv2, "stroke-width": 2 }, cote);
    etiquette(cote, xd + hh + 52, y0 + 9, "h", { fs: 30, c: C.iv, cls: "ser" });
    sv("line", { x1: xo, x2: xd, y1: y0 + hh + 40, y2: y0 + hh + 40, stroke: C.iv2, "stroke-width": 2 }, cote);
    etiquette(cote, (xo + xd) / 2, y0 + hh + 72, "D", { fs: 30, c: C.iv, cls: "ser" });
    var fo = etiquette(g, W_ / 2, 46, v.formule || "α ≈ h / D  (en radians, pour un petit angle)", { fs: 30, c: C.iv });
    return function (t, st) {
      var tl = st.tl;
      op(oeil, E(P(tl, 0, .6))); op(astre, E(P(tl, .3, .8))); cra.forEach(function (c) { op(c, E(P(tl, .5, .8))); });
      op(ax, E(P(tl, .8, .6))); trace(l1, P(tl, 1, 1)); trace(l2, P(tl, 1.1, 1));
      trace(arc, P(tl, 1.9, .8)); op(ta, E(P(tl, 2.3, .5)));
      var k = et(v, "2", 3.2); op(cote, E(P(t, k, .6))); op(fo, E(P(t, k + .5, .6)));
    };
  };

  /* ---------- types propres aux sciences ---------- */

  // carte animée du chapitre (dnl/cartes/<code>.html) pilotée par le temps de la vidéo. La page est rendue à une taille
  // réduite (largeur / k) puis agrandie k fois : les étiquettes de la carte restent lisibles quand la vidéo est petite.
  // seg = [[début, fin], …] en secondes de la carte, ou sc = [i, j, …] numéros de scènes de la carte (de 0) ; le segment k
  // démarre au repère {id.k} (le premier à l'apparition) et s'arrête sur sa dernière image jusqu'au repère suivant.
  TYPES.globe = function (o, v) {
    var e = o.el; e.classList.add("v-globe");
    var W = v.w || 1280, H = v.h || 720, k = v.k || 2.2;
    e.style.left = (v.x || 0) + "px"; e.style.top = (v.y || 0) + "px"; e.style.width = W + "px"; e.style.height = H + "px";
    var cad = h("div", "gl-cadre" + (v.cadre ? " encadre" : ""), e), fr = h("iframe", "", cad);
    fr.setAttribute("title", "Animated map"); fr.setAttribute("scrolling", "no"); fr.setAttribute("aria-hidden", "true"); fr.tabIndex = -1;
    fr.style.width = (W / k) + "px"; fr.style.height = (H / k) + "px"; fr.style.transform = "scale(" + k + ")";
    var api = null, seg = null;
    o.attente = new Promise(function (r) {
      fr.addEventListener("load", function () {
        var n = 0, q = setInterval(function () {
          n++;
          try { if (fr.contentWindow.CARTE_API) { api = fr.contentWindow.CARTE_API; clearInterval(q); r(); return; } } catch (err) { clearInterval(q); r(); return; }
          if (n > 300) { clearInterval(q); r(); }
        }, 30);
      });
    });
    fr.src = "../cartes/" + v.code + ".html?embed=1&pilote=1&lang=" + (v.lang || "en") + "&dpr=" + (v.dpr || 3) + "&w=" + Math.round(W / k) + "&h=" + Math.round(H / k);
    var vit = v.vit || 1, dernier = null;
    function segments() {
      if (seg) return seg;
      if (v.seg) return (seg = v.seg);
      // une scène qui suit la précédente garde le vol de caméra ; sinon on part caméra arrivée (pas de vol depuis une scène absente)
      var S = api.starts, TCs = api.transitions || [], d = v.attente_carte != null ? v.attente_carte : 0.05, sc = v.sc || [0];
      return (seg = sc.map(function (i, j) {
        var a = S[i] + (j > 0 && sc[j - 1] === i - 1 ? 0 : (TCs[i] || 0)) + (v.dt || 0);
        return [a, Math.max(a + 0.1, S[i + 1] - d)];
      }));
    }
    return function (t, st) {
      if (!api) return;
      var sg = segments(), debut = v.t0, kk = -1, tk = v.t0;
      for (var i = 0; i < sg.length; i++) {
        var c = v.et && v.et[String(i + 1)] != null ? v.et[String(i + 1)] : (i === 0 ? v.t0 : debut + (sg[i - 1][1] - sg[i - 1][0]) / vit);
        debut = c;
        if (t >= c) { kk = i; tk = c; }
      }
      var ta = kk < 0 ? sg[0][0] : Math.min(sg[kk][1], sg[kk][0] + (t - tk) * vit);
      ta = Math.round(ta * 60) / 60;
      if (ta !== dernier) { dernier = ta; try { api.rendre(ta); } catch (err) {} }
    };
  };

  // formule : lignes qui apparaissent au repère {id.k} ; cadre=True encadre la relation à retenir
  TYPES.formule = function (o, v) {
    var e = o.el; e.classList.add("v-formule");
    e.style.left = (v.x != null ? v.x : 150) + "px"; e.style.top = (v.y != null ? v.y : 150) + "px"; e.style.width = (v.w || 980) + "px";
    var c = h("div", "fo-carte" + (v.nu ? " nu" : ""), e);
    var te = v.titre ? h("div", "fo-te", c, esc(v.titre)) : null;
    var ls = v.lignes.map(function (l) {
      if (typeof l === "string") l = { f: l };
      var d = h("div", "fo-l" + (l.cadre ? " encadre" : "") + (l.txt ? " txt" : "") + (l.pt ? " pt" : "") + (l.ko ? " ko" : "") + (l.ok ? " ok" : ""), c);
      if (l.taille) d.style.fontSize = l.taille + "px";
      h("div", "fo-f", d, esc(l.f));
      var n = l.n ? h("div", "fo-n", d, esc(l.n)) : null;
      return { d: d, n: n, l: l };
    });
    if (v.plus) h("div", "badge", c, "Outside the course");
    return function (t, st) {
      if (te) op(te, E(P(st.tl, .05, .5)));
      ls.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .25 + i * 1.1), p = E(P(t, t1, .55));
        op(x.d, p); tr(x.d, "translateY(" + (14 * (1 - p)).toFixed(1) + "px)");
        x.d.style.filter = p < 1 ? "blur(" + ((1 - p) * 5).toFixed(1) + "px)" : "none";
        if (x.l.cadre) {
          var q = P(t, t1 + .45, .9), g = Math.max(0, Math.sin((t - t1) * 2.2)) * (t > t1 + 1.3 ? .25 : 0);
          x.d.style.boxShadow = "0 0 0 2px rgba(255,139,62," + (.85 * E(q)).toFixed(2) + "),0 0 " + (34 * (1 - q) + 14 + 10 * g).toFixed(0) + "px rgba(255,139,62," + (.32 * E(q) + .1 * g).toFixed(2) + ")";
        }
        if (x.n) op(x.n, E(P(t, t1 + .45, .6)));
      });
    };
  };

  // graphique : axes, puis éléments (courbe, droite, point, texte, rect, balaye) au repère {id.k}
  TYPES.graphe = function (o, v) {
    var e = o.el; e.classList.add("v-graphe");
    var Wd = v.w || 600, Hd = v.h || 480;
    e.style.left = (v.x != null ? v.x : 640) + "px"; e.style.top = (v.y != null ? v.y : 110) + "px"; e.style.width = Wd + "px"; e.style.height = Hd + "px";
    var m = v.marges || [86, 26, 44, 70], pw = Wd - m[0] - m[1], ph = Hd - m[2] - m[3], ax = v.ax;
    function X(x) { return m[0] + (x - ax.x[0]) / (ax.x[1] - ax.x[0]) * pw; }
    function Y(y) { return m[2] + (1 - (y - ax.y[0]) / (ax.y[1] - ax.y[0])) * ph; }
    var s = sv("svg", { viewBox: "0 0 " + Wd + " " + Hd, width: Wd, height: Hd }, e);
    var lab = h("div", "gr-lab", e);
    if (v.titre) h("div", "gr-ti", e, esc(v.titre));
    function txt(x, y, html, cls) { var d = h("div", "gr-t " + (cls || ""), lab, html); d.style.left = x + "px"; d.style.top = y + "px"; return d; }
    var fond = sv("g", {}, s), grille = [], ticks = [];
    var x0 = cl(0, ax.x[0], ax.x[1]), y0 = cl(0, ax.y[0], ax.y[1]);
    (ax.gx || []).forEach(function (x) {
      grille.push(sv("line", { x1: X(x), x2: X(x), y1: m[2], y2: m[2] + ph, stroke: "rgba(242,231,218,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x), Y(y0) + 12, esc(String(x)), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("line", { x1: m[0], x2: m[0] + pw, y1: Y(y), y2: Y(y), stroke: "rgba(242,231,218,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x0) - 12, Y(y), esc(String(y)), "ty"));
    });
    var axX = sv("path", { d: "M" + m[0] + " " + Y(y0) + " H" + (m[0] + pw + 14), stroke: C.iv, "stroke-width": 2.2, fill: "none" }, s);
    var axY = sv("path", { d: "M" + X(x0) + " " + (m[2] + ph) + " V" + (m[2] - 14), stroke: C.iv, "stroke-width": 2.2, fill: "none" }, s);
    var fl1 = sv("path", { d: "M" + (m[0] + pw + 16) + " " + Y(y0) + " l-12 -6 v12 z", fill: C.iv }, s);
    var fl2 = sv("path", { d: "M" + X(x0) + " " + (m[2] - 16) + " l-6 12 h12 z", fill: C.iv }, s);
    var lx = txt(m[0] + pw + 4, Y(y0) + 40, esc(ax.lx || ""), "lx"), ly = txt(X(x0) + 14, m[2] - 30, esc(ax.ly || ""), "ly");
    function chemin(pts) { return "M" + pts.map(function (p) { return X(p[0]).toFixed(1) + " " + Y(p[1]).toFixed(1); }).join(" L"); }
    function sur(pts, x) { // ordonnée d'une courbe (points triés) à l'abscisse x
      for (var i = 0; i < pts.length - 1; i++) if (x <= pts[i + 1][0]) { var u = (x - pts[i][0]) / ((pts[i + 1][0] - pts[i][0]) || 1); return pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u; }
      return pts[pts.length - 1][1];
    }
    var els = (v.el || []).map(function (d) {
      var col = C[d.c] || d.c || C.sa, g = sv("g", { opacity: 0 }, s), x = { d: d, g: g };
      if (d.type === "courbe" || d.type === "droite") {
        x.p = sv("path", { d: chemin(d.pts), stroke: col, "stroke-width": d.ep || 3.6, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
        if (d.tir) x.p.setAttribute("stroke-dasharray", "8 7");
        if (d.lbl) x.l = txt(X(d.lp[0]), Y(d.lp[1]), esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "point" || d.type === "points") {
        x.c = (d.type === "point" ? [[d.x, d.y]] : d.pts).map(function (p) {
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col, stroke: "#0c0804", "stroke-width": 1.5 }, g);
        });
        if (d.proj) {
          x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 1.6, "stroke-dasharray": "5 5", fill: "none", opacity: .8 }, g);
        }
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "rect" || d.type === "balaye") {
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: col, "fill-opacity": .22, stroke: col, "stroke-width": 2 }, g);
        x.pt = sv("circle", { r: 8, fill: col, stroke: "#0c0804", "stroke-width": 1.5 }, g);
        x.l = txt(0, 0, "", "lb"); x.l.style.color = col;
      }
      if (x.l) x.l.style.opacity = 0;
      return x;
    });
    var tAx = v.tax != null ? v.tax : 0;
    return function (t, st) {
      var pa = P(st.tl, tAx, .9);
      trace(axX, pa); trace(axY, pa); op(fl1, E(P(st.tl, tAx + .7, .3))); op(fl2, E(P(st.tl, tAx + .7, .3)));
      grille.forEach(function (gg) { op(gg, E(P(st.tl, tAx + .5, .8))); });
      ticks.forEach(function (tk) { op(tk, E(P(st.tl, tAx + .7, .6))); });
      op(lx, E(P(st.tl, tAx + .8, .6))); op(ly, E(P(st.tl, tAx + .8, .6)));
      els.forEach(function (x, i) {
        var d = x.d, t1 = et(v, String(i + 1), 1.2 + i * 1.4), dur = d.dur || (d.type === "courbe" ? 1.8 : d.type === "droite" ? 1.2 : .5);
        var a = P(t, t1, .3);
        x.g.setAttribute("opacity", (t >= t1 ? 1 : 0) * (d.fin != null && v.et && v.et[d.fin] != null ? 1 - E(P(t, v.et[d.fin], .5)) : 1));
        if (x.p) trace(x.p, EIO(P(t, t1, dur)));
        if (x.c) x.c.forEach(function (c, j) { var q = P(t, t1 + j * (d.pas || .18), .45); c.setAttribute("r", ((d.r || 6.5) * EB(q)).toFixed(2)); });
        if (x.pj) op(x.pj, E(P(t, t1 + .4, .6)) * .85);
        if (x.r) {
          var u = EIO(P(t, t1, dur)), xx = d.type === "rect" ? d.x : d.de + (d.a - d.de) * u, yy = d.type === "rect" ? d.y : sur(d.pts, xx);
          var X1 = X(x0), Y1 = Y(0), X2 = X(xx), Y2 = Y(yy);
          x.r.setAttribute("x", Math.min(X1, X2)); x.r.setAttribute("width", Math.abs(X2 - X1));
          x.r.setAttribute("y", Math.min(Y1, Y2)); x.r.setAttribute("height", Math.abs(Y2 - Y1));
          x.pt.setAttribute("cx", X2); x.pt.setAttribute("cy", Y2);
          if (d.fmt) {
            var val = xx * yy * (d.k || 1), txt_ = d.fmt.replace("{x}", (Math.round(xx * 100) / 100).toFixed(d.dx != null ? d.dx : 2).replace(".", ","))
              .replace("{y}", (Math.round(yy * 10) / 10).toFixed(d.dy != null ? d.dy : 1).replace(".", ",")).replace("{p}", Math.round(val).toString());
            x.l.innerHTML = esc(txt_);
            x.l.style.left = Math.min(X2 + 16, Wd - 140) + "px"; x.l.style.top = (Y2 - 34) + "px";
          }
        }
        if (x.l) x.l.style.opacity = E(P(t, t1 + (x.p ? dur * .6 : .2), .5));
      });
    };
  };

  // exercice : énoncé en grand (mode « plein »), ou rappel compact à gauche pendant la correction (mode « coin »)
  var NIVEAUX = { essay: ["Essay question", "#e6cb8b"], dbq: ["DBQ · document-based question", "#8fc7e8"], quiz: ["Quick check", "#7ce08a"] };
  TYPES.exo = function (o, v) {
    var e = o.el, coin = v.mode === "coin"; e.classList.add("v-exo", coin ? "coin" : "plein");
    if (!coin) { e.style.left = (v.x || 110) + "px"; e.style.top = (v.y || 96) + "px"; e.style.width = (v.w || 1060) + "px"; }
    var c = h("div", "ex-carte", e), nv = NIVEAUX[v.niveau] || [v.niveau || "Exercise", C.sa];
    var tag = h("div", "ex-nv", c, esc(nv[0])); tag.style.color = nv[1]; tag.style.borderColor = nv[1];
    h("div", "ex-ti", c, esc(v.titre));
    if (v.src) h("div", "ex-src", c, esc(v.src));
    var paras = (coin ? [] : v.enonce || []).map(function (p) { return h("p", "ex-p", c, esc(p)); });
    var don = v.donnees && v.donnees.length ? h("div", "ex-don", c, "<b>Document</b> " + v.donnees.map(esc).join(" &nbsp;·&nbsp; ")) : null;
    var qs = (v.questions || []).map(function (q, i) {
      var d = h("div", "ex-q", c); h("span", "ex-qn", d, String(i + 1)); h("span", "ex-qt", d, esc(q)); return d;
    });
    return function (t, st) {
      var tl = st.tl;
      op(tag, E(P(tl, .1, .5))); tr(tag, "translateX(" + (-20 * (1 - E(P(tl, .1, .5)))) + "px)");
      paras.forEach(function (p, i) { var q = E(P(t, et(v, "p" + (i + 1), .5 + i * .5), .6)); op(p, q); tr(p, "translateY(" + (10 * (1 - q)) + "px)"); });
      if (don) op(don, E(P(t, et(v, "d", .6 + paras.length * .5), .6)));
      var actif = -1;
      qs.forEach(function (q, i) { var k = v.et && v.et["q" + (i + 1)]; if (k != null && t >= k) actif = i; });
      qs.forEach(function (q, i) {
        var t1 = coin ? v.t0 + .3 + i * .12 : et(v, String(i + 1), .9 + paras.length * .5 + i * .4), p = E(P(t, t1, .5));
        op(q, p * (actif < 0 || actif === i ? 1 : .45)); tr(q, "translateX(" + (-16 * (1 - p)) + "px)");
        q.classList.toggle("on", actif === i);
      });
    };
  };

  // « À toi » : la vidéo s'arrête d'elle-même (si l'option est active) pour que l'élève cherche avant la correction
  TYPES.pause = function (o, v) {
    var e = o.el; e.classList.add("v-pause"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 200) + "px"; e.style.top = (v.y != null ? v.y : 130) + "px"; e.style.width = (v.w || 880) + "px";
    var c = h("div", "pa-carte", e), ic = h("div", "pa-ic", c, '<svg viewBox="0 0 24 24"><path d="M6 4h4.5v16H6zM13.5 4H18v16h-4.5z"/></svg>');
    var an = h("div", "pa-anneau", ic);
    var te = h("div", "pa-te", c, "Your turn"), tx = h("div", "pa-tx", c, esc(v.t));
    var so = h("div", "pa-so", c, esc(v.sous || "Pause the video, write your answer on a sheet, then play on for the correction."));
    return function (t, st) {
      var tl = st.tl, a = E(P(tl, 0, .6));
      op(c, a); tr(c, "translateY(" + (24 * (1 - a)) + "px) scale(" + (0.95 + 0.05 * EB(P(tl, 0, .7))) + ")");
      tr(ic, "scale(" + (0.6 + 0.4 * EB(P(tl, .2, .6))) + ")");
      var r = (tl % 1.6) / 1.6; op(an, (1 - r) * .7); tr(an, "scale(" + (1 + r * .8) + ")");
      op(te, E(P(tl, .3, .5))); op(tx, E(P(tl, .5, .6))); op(so, E(P(tl, 1, .6)) * .9);
    };
  };

  /* ---------- scène ---------- */
  var FONDS = {
    nuit: { base: "linear-gradient(160deg,#0c1322 0%,#19213a 55%,#121a2b 100%)", lueurs: ["rgba(230,203,139,.20)", "rgba(79,154,142,.16)", "rgba(120,90,160,.16)"] },
    aube: { base: "linear-gradient(160deg,#1a1527 0%,#2a2036 55%,#181d31 100%)", lueurs: ["rgba(230,203,139,.24)", "rgba(194,97,76,.18)", "rgba(79,154,142,.12)"] },
    guerre: { base: "linear-gradient(160deg,#1b0f10 0%,#2b1718 55%,#16101a 100%)", lueurs: ["rgba(194,97,76,.24)", "rgba(230,203,139,.14)", "rgba(120,90,160,.12)"] }
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
        cx.fillStyle = "rgba(255,214,170," + a.toFixed(3) + ")";
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
      ent.innerHTML = esc(EP.notion) + " · Ep. " + EP.num + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
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
    apause: '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 2a8 8 0 1 1 0 16 8 8 0 0 1 0-16zM8.8 7.5h2.4v9H8.8zm4 0h2.4v9h-2.4z"/></svg>',
    cc: '<svg viewBox="0 0 24 24"><path d="M3 5h18v14H3zm2 2v10h14V7zm2.5 3.2h4v1.5h-2.5v1.6h2.5v1.5h-4zm6 0h4v1.5H15v1.6h2.5v1.5h-4z"/></svg>'
  };

  function lancer(EP) {
    document.title = EP.notion + " · Episode " + EP.num + " — " + EP.titre;
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
      h("span", "k", tete, esc(EP.notion) + " · episode " + EP.num);
      h("h1", "", tete, esc(EP.titre));
    }
    var boite = h("div", "boite", L), cadre = h("div", "cadre", boite);
    var S = Scene(EP, cadre);
    var affiche = h("div", "affiche", cadre), gp = h("button", "gros-play", affiche, ICO.play); gp.setAttribute("aria-label", "Play");
    h("div", "charge", cadre);
    var barre = h("div", "barre", boite);
    var prog = h("div", "prog", barre), rail = h("div", "rail", prog), plein = h("div", "plein", prog);
    EP.scenes.forEach(function (s, i) { if (i) { var tc = h("div", "tic", prog); tc.style.left = (100 * s.t0 / EP.dur) + "%"; } });
    var pouce = h("div", "pouce", prog), bulle = h("div", "bulle", prog);
    var bPlay = h("button", "btn", barre, ICO.play), bM = h("button", "btn", barre, ICO.m10), bP = h("button", "btn", barre, ICO.p10);
    var temps = h("span", "temps", barre);
    h("span", "espace", barre);
    var bVit = h("button", "btn", barre, '<span class="mono">1×</span>'), bMus = h("button", "btn on", barre, ICO.musique),
      bCC = h("button", "btn", barre, ICO.cc), bPA = h("button", "btn on", barre, ICO.apause), bFS = h("button", "btn", barre, ICO.plein);
    bPA.title = "Stop automatically before each correction";
    bPlay.title = "Play / pause (space)"; bM.title = "Back 10 s"; bP.title = "Forward 10 s"; bVit.title = "Speed";
    bMus.title = "Background music"; bCC.title = "Subtitles"; bFS.title = "Full screen";

    h("div", "astuce", L, "On a phone, tap ⛶: the video goes full screen, in landscape.");
    var chaps = h("div", "chapitres", L);
    var bChap = EP.scenes.map(function (s, i) {
      var b = h("button", "chap", chaps);
      h("span", "n", b, i ? ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI"][i - 1] : "◆");
      var tx = h("span", "", b); h("div", "t", tx, esc(s.chap)); h("div", "d", tx, fmt(s.t0));
      b.onclick = function () { aller(s.t0 + (i ? .05 : 0)); if (!lecture) jouer(); bouge(b, [{ transform: "scale(.95)" }, { transform: "scale(1.03)", offset: .5 }, { transform: "none" }], { duration: 420, easing: RESSORT }); };
      return b;
    });

    // quiz
    var quiz = h("div", "quiz", L);
    h("h2", "", quiz, "Did you get it?");
    h("div", "sous", quiz, EP.quiz.length + " questions on this episode. Answer, then read the explanation.");
    var bonnes = 0, faites = 0, score = h("div", "score", null);
    EP.quiz.forEach(function (q) {
      var d = h("div", "qq", quiz); h("div", "q", d, esc(q.q));
      var bs = q.r.map(function (r, i) {
        var b = h("button", "r", d, esc(r));
        b.onclick = function () {
          bs.forEach(function (x, j) { x.disabled = true; if (j === q.ok) x.classList.add("ok"); });
          if (i !== q.ok) b.classList.add("ko"); else bonnes++;
          faites++;
          var ex = h("div", "ex", d, (i === q.ok ? "✓ Correct. " : "✗ Not quite. ") + esc(q.ex));
          if (q.voir != null) { var vo = h("button", "voir", d, "▸ Watch this passage again"); vo.onclick = function () { aller(Math.max(0, q.voir - 1.5)); jouer(); (cadre.scrollIntoView || function () {}).call(cadre, { behavior: "smooth", block: "center" }); }; }
          if (faites === EP.quiz.length) { score.textContent = "Score: " + bonnes + " / " + faites + (bonnes === faites ? " — perfect!" : ""); quiz.appendChild(score); }
          hauteur();
        };
        return b;
      });
    });
    if (EP.credits && EP.credits.length) {
      var cr = h("details", "credits", L); h("summary", "", cr, "Credits");
      EP.credits.forEach(function (c) { h("div", "", cr, esc(c)); });
      cr.addEventListener("toggle", hauteur);
    }

    // horloge : le son mène, une minuterie prend le relais sans son
    var audio = new Audio(), musique = true, src = function () { return musique ? EP.audio.mix : EP.audio.voix; };
    audio.preload = "metadata"; audio.src = src();
    // arrêts « À toi » : la vidéo s'arrête d'elle-même avant chaque correction (option, active par défaut)
    var arrets = EP.vis.filter(function (v) { return v.type === "pause"; }).map(function (v) { return v.et && v.et.stop != null ? v.et.stop : v.t0 + 2.5; });
    var autoPause = true, arretSur = null;
    var bandeau = h("div", "arret", cadre, '<span class="ic">' + ICO.pause + '</span><span><b>Your turn.</b> The video is waiting for your answer: think it through, then tap the picture for the correction.</span>');
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
      arretSur = null; cadre.classList.remove("arrete");
      lecture = true; affiche.classList.add("off");
      if (sonOK) { audio.playbackRate = vitesse; var p = audio.play(); if (p && p.catch) p.catch(function () { sonOK = false; }); }
      dernier = performance.now(); majUI(); reveil();
    }
    function pause() { lecture = false; audio.pause(); majUI(); reveil(); }
    // mouvement du site (sauf si l'appareil demande moins d'animations)
    var MQ = window.matchMedia ? matchMedia("(prefers-reduced-motion: reduce)") : null;
    function bouge(el, kf, o) { if (!el || !el.animate || (MQ && MQ.matches)) return null; try { return el.animate(kf, o); } catch (e) { return null; } }
    var DOUX = "cubic-bezier(.2,.8,.2,1)", RESSORT = "cubic-bezier(.2,.9,.3,1.15)";
    // lecture / pause : l'icône pulse au centre de l'image, comme sur YouTube
    var pulse = h("div", "pulse", cadre);
    function pulser(lit) {
      pulse.innerHTML = lit ? ICO.play : ICO.pause;
      bouge(pulse, [{ opacity: .9, transform: "translate(-50%,-50%) scale(.6)" }, { opacity: 0, transform: "translate(-50%,-50%) scale(1.5)" }], { duration: 650, easing: "ease-out" });
    }
    bChap.forEach(function (b, i) {
      bouge(b, [{ opacity: 0, transform: "translateY(18px) rotateX(-30deg)" }, { opacity: 1, transform: "none" }], { duration: 600, delay: 250 + i * 70, easing: RESSORT, fill: "backwards" });
    });
    bouge(boite, [{ opacity: 0, transform: "translateY(18px) scale(.98)" }, { opacity: 1, transform: "none" }], { duration: 700, easing: DOUX, fill: "backwards" });
    // plein écran : les commandes apparaissent quand on bouge la souris (ou touche l'écran), puis s'effacent après 2,5 s
    var tRepos = null, surBarre = false;
    function reveil() {
      L.classList.remove("repos"); clearTimeout(tRepos);
      if (estPlein() && lecture) tRepos = setTimeout(function () { if (!surBarre && !glisse && lecture) L.classList.add("repos"); }, 2500);
    }
    function bascule() { var l = lecture; l ? pause() : jouer(); if (!affiche.classList.contains("off") && !l) return; pulser(!l); }
    function boucle(now) {
      var dt = Math.min(.1, Math.max(0, (now - dernier) / 1000)); dernier = now;
      if (lecture) {
        var avant = T;
        if (sonOK && !audio.paused && audio.readyState >= 2 && !audio.seeking && enAttente == null) {
          var at = audio.currentTime;
          if (Math.abs(at - T) > .25) T = at; else T += dt * vitesse + (at - T) * .08;
        } else if (!sonOK) T += dt * vitesse;
        else if (audio.seeking || enAttente != null) { /* on attend la fin du saut */ }
        if (autoPause && T > avant) {
          var ar = arrets.filter(function (a) { return avant < a && a <= T; })[0];
          if (ar != null) { T = ar; try { audio.currentTime = ar; } catch (e) {} pause(); arretSur = ar; cadre.classList.add("arrete"); S.rendu(T); majUI(); }
        }
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
    cadre.addEventListener("click", function () {
      if (estPlein() && L.classList.contains("repos") && matchMedia("(hover: none)").matches) { reveil(); return; }   // téléphone : un toucher montre d'abord les commandes
      bascule();
    });
    ["mousemove", "pointerdown", "touchstart", "wheel"].forEach(function (n) { boite.addEventListener(n, reveil, { passive: true }); });
    barre.addEventListener("mouseenter", function () { surBarre = true; reveil(); });
    barre.addEventListener("mouseleave", function () { surBarre = false; reveil(); });
    cadre.addEventListener("dblclick", function () { pleinEcran(); });
    bM.onclick = function () { aller(T - 10); }; bP.onclick = function () { aller(T + 10); };
    var VIT = [1, 1.25, 1.5, 0.85];
    bVit.onclick = function () { vitesse = VIT[(VIT.indexOf(vitesse) + 1) % VIT.length]; audio.playbackRate = vitesse; bVit.innerHTML = '<span class="mono">' + String(vitesse) + "×</span>"; };
    bMus.onclick = function () {
      musique = !musique; bMus.classList.toggle("on", musique);
      var l = lecture; audio.pause(); audio.src = src(); sonOK = true;
      enAttente = T; audio.load(); if (l) jouer();
    };
    var cc = false;
    bCC.onclick = function () { cc = !cc; bCC.classList.toggle("on", cc); S.sous(cc); S.rendu(T); };
    bPA.onclick = function () { autoPause = !autoPause; bPA.classList.toggle("on", autoPause); };

    // plein écran (vrai si possible, sinon en couvrant la fenêtre)
    function estPlein() { return L.classList.contains("plein"); }
    function pleinEcran() {
      if (estPlein()) { sortirPlein(); return; }
      L.classList.add("plein"); ajuste(); reveil();
      bouge(cadre, [{ transform: "scale(.9)", opacity: .4, filter: "blur(4px)" }, { transform: "none", opacity: 1, filter: "blur(0)" }], { duration: 520, easing: DOUX });
      bouge(barre, [{ transform: "translateY(30px)", opacity: 0 }, { transform: "none", opacity: 1 }], { duration: 480, delay: 160, easing: DOUX, fill: "backwards" });
      if (boite.requestFullscreen) {
        boite.requestFullscreen().then(function () { try { screen.orientation.lock("landscape").catch(function () {}); } catch (e) {} }).catch(function () { pseudo(); });
      } else if (boite.webkitRequestFullscreen) { boite.webkitRequestFullscreen(); } else pseudo();
    }
    function pseudo() { document.body.classList.add("pseudo"); history.pushState({ seriePlein: 1 }, ""); }
    function sortirPlein() {
      L.classList.remove("plein", "repos"); clearTimeout(tRepos);
      bouge(boite, [{ transform: "scale(1.05)", opacity: .5 }, { transform: "none", opacity: 1 }], { duration: 480, easing: DOUX }); document.body.classList.remove("pseudo");
      if (document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(function () {});
      else if (history.state && history.state.seriePlein) history.back();
      setTimeout(ajuste, 50);
    }
    bFS.onclick = pleinEcran;
    document.addEventListener("fullscreenchange", function () { if (!document.fullscreenElement && estPlein() && !document.body.classList.contains("pseudo")) { L.classList.remove("plein", "repos"); } setTimeout(ajuste, 60); });
    addEventListener("popstate", function () { if (estPlein() && document.body.classList.contains("pseudo")) { L.classList.remove("plein"); document.body.classList.remove("pseudo"); setTimeout(ajuste, 50); } });

    document.addEventListener("keydown", function (ev) {
      if (/input|textarea/i.test(ev.target.tagName)) return;
      var k = ev.key; reveil();
      if (k === " " || k === "k") { ev.preventDefault(); bascule(); }
      else if (k === "ArrowLeft") { aller(T - 5); } else if (k === "ArrowRight") { aller(T + 5); }
      else if (k === "f") pleinEcran(); else if (k === "m") bMus.onclick(); else if (k === "c") bCC.onclick();
      else if (k === "Escape" && estPlein()) sortirPlein();
    });

    if ("mediaSession" in navigator) {
      try {
        navigator.mediaSession.metadata = new MediaMetadata({ title: "Ep. " + EP.num + " · " + EP.titre, artist: "DNL History · Revision Atlas", album: EP.notion });
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
