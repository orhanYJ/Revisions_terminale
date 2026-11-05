/* Dancing at Lughnasa — vidéo résumé-analyse : moteur du lecteur (copie du moteur des séries philo, v12,
   en anglais, aux couleurs du site ACL écrit : bleu marine et or ; illustration « plateau » en plus).
   Moteur d'origine :
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  var C = { iv: "#f3efe4", iv2: "#d9d2c0", sa: "#e6cb8b", sa2: "#c4a052", ca: "#c2614c", te: "#4f9a8e", eau: "#74b9d8", nuit: "#0e1525" };

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
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(230,203,139," + (0.7 * (1 - f)).toFixed(2) + ")";
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
  var RUBAN = "#b5485a";   // rouge « ruban » du site ACL écrit, éclairci pour le fond sombre

  // personnage du plateau : tête + corps, échelle selon la profondeur ; assis = plus court
  function perso(g, x, y, k, assis) {
    var gr = sv("g", { transform: "translate(" + x + "," + y + ") scale(" + k + ")" }, g);
    var corps = sv("path", { d: assis ? "M-15 -34 Q0 -40 15 -34 L19 0 Q0 4 -19 0 Z" : "M-15 -50 Q0 -56 15 -50 L21 0 Q0 4 -21 0 Z", fill: C.iv }, gr);
    var tete = sv("circle", { cx: 0, cy: assis ? -46 : -62, r: 10.5, fill: C.iv }, gr);
    return { g: gr, tete: tete, corps: corps, coul: function (c) { corps.setAttribute("fill", c); tete.setAttribute("fill", c); } };
  }

  // le plateau vu de la salle : cuisine à gauche (côté cour), jardin à droite (côté jardin), Michael devant à droite
  ILLU.plateau = function (s, v) {
    var w = v.w, hh = v.h;
    var defs = sv("defs", {}, s);
    var rg = sv("radialGradient", { id: "pl-pool", cx: "50%", cy: "50%", r: "50%" }, defs);
    sv("stop", { offset: "0%", "stop-color": "#fff4d6", "stop-opacity": .75 }, rg);
    sv("stop", { offset: "100%", "stop-color": "#fff4d6", "stop-opacity": 0 }, rg);
    var lg = sv("linearGradient", { id: "pl-cone", x1: "0", y1: "0", x2: "0", y2: "1" }, defs);
    sv("stop", { offset: "0%", "stop-color": "#fff4d6", "stop-opacity": 0 }, lg);
    sv("stop", { offset: "100%", "stop-color": "#fff4d6", "stop-opacity": .22 }, lg);
    var chaud = sv("path", { d: "M150 70 L850 70 L960 440 L40 440 Z", fill: "rgba(240,175,80,.2)", opacity: 0 }, s);
    var traits = [];
    traits.push(sv("path", { d: "M150 70 L850 70 L960 440 L40 440 Z", fill: "none", stroke: "rgba(243,239,228,.38)", "stroke-width": 2.5 }, s));
    traits.push(sv("path", { d: "M520 70 L520 205 M520 265 L520 440", fill: "none", stroke: "rgba(243,239,228,.3)", "stroke-width": 2.5, "stroke-dasharray": "8 7" }, s));
    traits.push(sv("path", { d: "M215 70 V96 H295 V70", fill: "none", stroke: "rgba(243,239,228,.4)", "stroke-width": 2.5 }, s));   // fenêtre
    traits.push(sv("path", { d: "M640 322 H780 M650 322 V336 M770 322 V336", fill: "none", stroke: "rgba(243,239,228,.4)", "stroke-width": 3 }, s)); // banc
    var lieux = [etiquette(s, 290, 412, "THE KITCHEN", { fs: 17, ls: 3, c: C.iv2 }), etiquette(s, 690, 412, "THE GARDEN", { fs: 17, ls: 3, c: C.iv2 }),
      etiquette(s, 520, 474, "▲  THE AUDIENCE  ▲", { fs: 15, ls: 3, c: "rgba(243,239,228,.55)", fw: 500 })];
    var cone = sv("path", { d: "M850 -40 L910 -40 L1000 420 L760 420 Z", fill: "url(#pl-cone)", opacity: 0 }, s);
    var pool = sv("ellipse", { cx: 880, cy: 420, rx: 130, ry: 42, fill: "url(#pl-pool)", opacity: 0 }, s);
    var K = function (y) { return 0.82 + (y - 100) / 340 * 0.38; };
    var P_ = [
      ["Kate", 85, 330, false, "off"], ["Maggie", 255, 150, false, "hen mash"], ["Chris", 520, 250, false, "irons"],
      ["Jack", 618, 318, false, "off"], ["Rose", 676, 322, true, "turf"], ["Gerry", 740, 322, true, "off"], ["Agnes", 865, 150, false, "knits"]
    ];
    var gens = P_.map(function (p) {
      var o = perso(s, p[1], p[2], K(p[2]), p[3]);
      o.nom = etiquette(s, p[1], p[2] + 24, p[0], { fs: 17, c: C.iv2 });
      o.tache = p[4] === "off" ? null : etiquette(s, p[1], p[2] + 44, p[4], { fs: 14, fw: 400, c: C.sa, cls: "ser" });
      o.part = p[4] === "off";
      return o;
    });
    var mi = perso(s, 880, 420, 1.25, false); mi.coul(C.sa);
    var miN = etiquette(s, 880, 452, "MICHAEL", { fs: 20, c: C.sa, ls: 2 });
    var miS = etiquette(s, 760, 300, "the adult narrator", { fs: 20, fw: 400, c: C.sa, cls: "ser", ancre: "end" });
    var tab = etiquette(s, 330, 30, "a frozen “formal tableau”", { fs: 24, fw: 400, c: C.iv, cls: "ser" });
    var vie = etiquette(s, 330, 30, "lights up: a warm summer afternoon", { fs: 24, fw: 400, c: C.sa, cls: "ser" });
    return function (t, st) {
      traits.forEach(function (e, i) { trace(e, P(t, v.t0 + i * .25, 1.4)); });
      lieux.forEach(function (e, i) { op(e, E(P(t, v.t0 + 1 + i * .3, .7)) * .9); });
      var e1 = et(v, "1", 1.5), e2 = et(v, "2", 4), e3 = et(v, "3", 8);
      var a1 = E(P(t, e1, 1.2)), a2 = E(P(t, e2, 1.4)), a3 = E(P(t, e3, 1.6));
      op(cone, a1 * (1 - .6 * a3)); op(pool, a1 * (1 - .5 * a3));
      op(mi.g, a1 * (1 - a3)); op(miN, a1 * (1 - a3)); op(miS, E(P(t, e1 + .8, .8)) * (1 - E(P(t, e2, .6))));
      gens.forEach(function (o, i) {
        var q = E(P(t, e2 + i * .15, .9));
        var fin = o.part ? 1 - a3 : 1;
        op(o.g, q * (.55 + .45 * a3 * (o.part ? 0 : 1)) * fin); op(o.nom, q * fin);
        if (o.tache) op(o.tache, E(P(t, e3 + .8 + i * .1, .7)));
      });
      op(tab, a2 * (1 - E(P(t, e3, .6)))); op(vie, E(P(t, e3 + .3, .8)));
      op(chaud, a3);
    };
  };

  // la « brèche » : deux lignes qui partent ensemble et s'écartent
  ILLU.breche = function (s, v) {
    var w = v.w, hh = v.h, y0 = hh / 2, x0 = 90, x1 = w - 90, d = Math.min(130, hh / 2 - 40);
    var haut = sv("path", { d: "M" + x0 + " " + y0 + " C" + (x0 + 300) + " " + y0 + " " + (x1 - 260) + " " + (y0 - d) + " " + x1 + " " + (y0 - d), fill: "none", stroke: C.sa, "stroke-width": 5, "stroke-linecap": "round" }, s);
    var bas = sv("path", { d: "M" + x0 + " " + y0 + " C" + (x0 + 300) + " " + y0 + " " + (x1 - 260) + " " + (y0 + d) + " " + x1 + " " + (y0 + d), fill: "none", stroke: C.iv2, "stroke-width": 5, "stroke-linecap": "round" }, s);
    var zone = sv("path", { d: "M" + x0 + " " + y0 + " C" + (x0 + 300) + " " + y0 + " " + (x1 - 260) + " " + (y0 - d) + " " + x1 + " " + (y0 - d) +
      " L" + x1 + " " + (y0 + d) + " C" + (x1 - 260) + " " + (y0 + d) + " " + (x0 + 300) + " " + y0 + " " + x0 + " " + y0 + " Z", fill: RUBAN, opacity: 0 }, s);
    s.insertBefore(zone, haut);
    var pt = sv("circle", { cx: x0, cy: y0, r: 8, fill: C.iv }, s);
    var lH = etiquette(s, x1, y0 - d - 22, "what seemed to be", { fs: 30, c: C.sa, cls: "ser", ancre: "end", fw: 400 });
    var lB = etiquette(s, x1, y0 + d + 44, "what was", { fs: 30, c: C.iv2, cls: "ser", ancre: "end", fw: 400 });
    var l1 = etiquette(s, x0 + 600, y0 + 8, "things changing too quickly", { fs: 22, c: C.iv, fw: 400, cls: "ser" });
    var l2 = etiquette(s, x0 + 600, y0 + 8, "becoming what they ought not to be", { fs: 22, c: C.iv, fw: 400, cls: "ser" });
    var lb = etiquette(s, x0 - 10, y0 - 26, "the summer of 1936", { fs: 18, c: C.iv2, fw: 500, ancre: "start" });
    return function (t, st) {
      var p = EIO(P(t, v.t0 + .4, 2.6));
      op(pt, E(P(t, v.t0, .5))); op(lb, E(P(t, v.t0 + .2, .6)) * (1 - E(P(t, et(v, "1", 5), .6))));
      trace(haut, p); trace(bas, p);
      op(zone, .32 * E(P(t, v.t0 + 1.2, 2.4)));
      op(lH, E(P(t, v.t0 + 2.2, .7))); op(lB, E(P(t, v.t0 + 2.5, .7)));
      var a1 = E(P(t, et(v, "1", 5), .7)), a2 = E(P(t, et(v, "2", 8), .7));
      op(l1, a1 * (1 - a2)); op(l2, a2);
      tr(l1, "translateX(" + (-20 * (1 - a1)) + "px)"); tr(l2, "translateX(" + (-20 * (1 - a2)) + "px)");
    };
  };

  // deux souvenirs liés : la radio et Jack
  ILLU.liens = function (s, v) {
    var g1 = sv("g", { transform: "translate(250,190)" }, s), g2 = sv("g", { transform: "translate(750,190)" }, s);
    // la radio
    var radio = [];
    radio.push(sv("rect", { x: -110, y: -90, width: 220, height: 170, rx: 26, fill: "none", stroke: C.sa, "stroke-width": 5 }, g1));
    radio.push(sv("path", { d: "M-110 -40 Q0 -100 110 -40", fill: "none", stroke: C.sa, "stroke-width": 4 }, g1));
    [-60, -30, 0, 30, 60].forEach(function (x) { radio.push(sv("path", { d: "M" + x + " -10 V48", fill: "none", stroke: "rgba(230,203,139,.6)", "stroke-width": 4, "stroke-linecap": "round" }, g1)); });
    var nomR = etiquette(g1, 0, 112, "MARCONI", { fs: 22, c: C.sa, ls: 5 });
    var ondes = [0, 1, 2].map(function (i) { return sv("path", { d: "M" + (130 + i * 22) + " -70 q 16 30 0 60", fill: "none", stroke: C.sa, "stroke-width": 4, "stroke-linecap": "round" }, g1); });
    // Jack
    var jk = perso(g2, 0, 70, 2.1, false); jk.coul("#b9b19c");
    var chap = sv("path", { d: "M-46 -66 H46 M-24 -66 Q0 -110 24 -66", fill: "none", stroke: "#b9b19c", "stroke-width": 7, "stroke-linecap": "round" }, g2);
    var nomJ = etiquette(g2, 0, 112, "FATHER JACK", { fs: 22, c: C.iv2, ls: 5 });
    // le lien
    var m1 = sv("ellipse", { cx: 470, cy: 190, rx: 46, ry: 26, fill: "none", stroke: C.iv, "stroke-width": 5 }, s);
    var m2 = sv("ellipse", { cx: 530, cy: 190, rx: 46, ry: 26, fill: "none", stroke: C.iv, "stroke-width": 5 }, s);
    var lien = etiquette(s, 500, 250, "always linked", { fs: 24, c: C.iv, cls: "ser", fw: 400 });
    var motsR = ["delight", "awe", "sheer magic"].map(function (m, i) { return etiquette(s, 250, 370 + i * 34, m, { fs: 25, c: C.sa, cls: "ser", fw: 400 }); });
    var motsJ = ["shock", "shrunken", "jaundiced"].map(function (m, i) { return etiquette(s, 750, 370 + i * 34, m, { fs: 25, c: C.iv2, cls: "ser", fw: 400 }); });
    return function (t, st) {
      var a = E(P(t, v.t0, .9));
      radio.forEach(function (e, i) { trace(e, P(t, v.t0 + i * .1, 1)); });
      op(nomR, a); op(g2, E(P(t, v.t0 + .5, .9))); op(nomJ, E(P(t, v.t0 + .8, .7)));
      ondes.forEach(function (o, i) { var c = ((t * .9 + i / 3) % 1); op(o, a * Math.sin(c * Math.PI) * .9); });
      var e1 = et(v, "1", 2), e2 = et(v, "2", 4), e3 = et(v, "3", 7);
      var pl = E(P(t, e1, .8)); op(m1, pl); op(m2, pl); tr(m1, "translateX(" + (-30 * (1 - pl)) + "px)"); tr(m2, "translateX(" + (30 * (1 - pl)) + "px)");
      op(lien, E(P(t, e1 + .4, .7)));
      motsJ.forEach(function (m, i) { op(m, E(P(t, e2 + i * .35, .6))); });
      motsR.forEach(function (m, i) { op(m, E(P(t, e3 + i * .35, .6))); });
      // Jack erre (« shuffling from room to room ») une fois ses mots dits
      var er = P(t, e2, 30);
      g2.setAttribute("transform", "translate(" + (750 + Math.sin(er * 40) * 14 * (er > 0 ? 1 : 0)).toFixed(1) + ",190)");
    };
  };

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
      tr(tt, "scale(" + (1 + 0.02 * Math.min(tl, 3)) + ")");   // légère avancée, bornée : un long titre ne sort pas du cadre
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
    var bg = h("div", "barre-g", c), te = h("div", "te", c, esc(note ? (v.titre || v.terme || "Note") : v.terme));
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
    h("div", "gu", e, "“");
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
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(230,203,139,.9)";
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
        c.c.style.borderColor = actif ? "rgba(230,203,139," + (0.5 + 0.4 * pul) + ")" : "rgba(243,239,228,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(230,203,139,.25)" : "none";
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
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "Brian Friel · Dancing at Lughnasa");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, "Summary & analysis · part " + v.num);
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
    h("div", "fl-te", c, "Remember");
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
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(230,203,139,.35)";
      br.forEach(function (b, i) {
        var tk = et(v, String(i + 1), .6 + i * 1.2);
        trace(b.ln, P(t, tk, .8));
        var q = P(t, tk + .5, .5); op(b.nd, E(q)); tr(b.nd, "translate(-50%,-50%) scale(" + (0.5 + 0.5 * EB(q)) + ")");
        b.its.forEach(function (it, j) { var r = E(P(t, tk + .8 + j * .25, .5)); op(it, r); tr(it, "translateY(" + (8 * (1 - r)) + "px)"); });
      });
    };
  };

  /* ---------- la pièce jouée : plateau vu de la salle, personnages qui bougent ----------
     v.etats : liste d'états ; l'état 0 vaut dès l'apparition, l'état k au repère {id.k}. Chaque état ne donne que ce qui change :
       pos  : {nom: lieu ou [x, y] ou "off"}      act : {nom: "fige" | "tricote" | "repasse" | "range" | "danse" | "danse_douce"
                                                         | "danse_lourde" | "seule" | "halete" | "assis" | "debout"}
       dit  : [nom, texte] (bulle)                 radio : true / false / "parasites"
       masque : [noms] (visage de farine)         surplis : [noms] (vêtement blanc sur la tête)
       ronde : [noms] (ils tournent en cercle)     chemin : {nom: [lieux…]} (trajet lent, ex. Kate dans le jardin)
       note : texte de didascalie affiché en bas (citation courte)
     Le rendu ne dépend que du temps : retour en arrière et export image par image donnent la même image. */
  var LIEUX = {
    fenetre: [292, 236], radio: [462, 244], buffet: [182, 300], table: [330, 368], porte: [566, 300],
    tricot_a: [404, 452], tricot_r: [238, 452], centre: [330, 420], jardin: [770, 430], banc: [840, 340],
    allee: [1110, 300], seuil: [600, 380], avant: [470, 520]
  };
  var PERSOS = {
    Kate: { c: "#8fa9d9", h: "#3b3125", femme: true }, Maggie: { c: "#e3a95c", h: "#5a3a22", femme: true, tablier: true },
    Agnes: { c: "#79c2a6", h: "#4a3420", femme: true }, Rose: { c: "#e996a6", h: "#6b4a2a", femme: true, bottes: true },
    Chris: { c: "#c3a2e6", h: "#7a5a36", femme: true }, Jack: { c: "#a9a59a", h: "#d8d4c8", chapeau: "jack" },
    Gerry: { c: "#d6c07a", h: "#4a3420", chapeau: "paille" }, Michael: { c: "#e6cb8b", h: "#4a3420" }
  };
  function coupe(txt, n) {   // texte en lignes de n caractères au plus
    var out = [], l = "";
    String(txt).split(" ").forEach(function (m) { if (l && (l + " " + m).length > n) { out.push(l); l = m; } else l = l ? l + " " + m : m; });
    if (l) out.push(l);
    return out;
  }
  function lieu(p) { return typeof p === "string" ? (LIEUX[p] || [580, 400]) : p; }
  function echelle(y) { return 1.05 * (0.74 + (y - 200) / 360 * 0.5); }
  var CAMS = { cuisine: [20, 60, 860, 445], tout: [100, 100, 980, 507], porte: [250, 90, 760, 393] };

  function figure(g, nom) {
    var PP = PERSOS[nom] || { c: C.iv, h: "#444" };
    var gr = sv("g", {}, g);
    var ombre = sv("ellipse", { cx: 0, cy: 2, rx: 22, ry: 6, fill: "rgba(0,0,0,.35)" }, gr);
    var corps = sv("g", {}, gr);
    var jg = sv("path", { d: "", stroke: PP.bottes ? "#2c2c2c" : "#d9d2c0", "stroke-width": PP.bottes ? 9 : 6, "stroke-linecap": "round", fill: "none" }, corps);
    var jd = sv("path", { d: "", stroke: PP.bottes ? "#2c2c2c" : "#d9d2c0", "stroke-width": PP.bottes ? 9 : 6, "stroke-linecap": "round", fill: "none" }, corps);
    var robe = sv("path", { d: PP.femme ? "M-14 -78 Q0 -84 14 -78 L24 -26 Q0 -20 -24 -26 Z" : "M-15 -80 Q0 -86 15 -80 L17 -36 L-17 -36 Z", fill: PP.c }, corps);
    if (PP.tablier) sv("path", { d: "M-9 -60 L9 -60 L13 -28 L-13 -28 Z", fill: "rgba(255,255,255,.75)" }, corps);
    var bg = sv("path", { d: "", stroke: PP.c, "stroke-width": 7, "stroke-linecap": "round", fill: "none" }, corps);
    var bd = sv("path", { d: "", stroke: PP.c, "stroke-width": 7, "stroke-linecap": "round", fill: "none" }, corps);
    var cheveux = sv("circle", { cx: 0, cy: -95, r: 14, fill: PP.h }, corps);
    var tete = sv("circle", { cx: 0, cy: -92, r: 11.5, fill: "#f0d6bf" }, corps);
    var masque = sv("circle", { cx: 0, cy: -92, r: 11.8, fill: "#fbfaf6", opacity: 0 }, corps);
    if (PP.chapeau === "paille") sv("path", { d: "M-20 -104 H20 M-11 -104 Q0 -122 11 -104", stroke: "#e8d79a", "stroke-width": 5, fill: "none", "stroke-linecap": "round" }, corps);
    if (PP.chapeau === "jack") sv("path", { d: "M-22 -104 H22 M-12 -104 Q0 -124 12 -104", stroke: "#2b2b2b", "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, corps);
    var surplis = sv("path", { d: "M-20 -112 Q0 -126 20 -112 L28 -30 Q0 -22 -28 -30 Z", fill: "#fbfaf6", opacity: 0 }, corps);
    var nomT = sv("text", { x: 0, y: 26, "text-anchor": "middle", fill: PP.c, "font-size": 17, "font-weight": 700 }, gr, nom);
    function bras(e, sx, ang, l) {
      var x2 = sx + Math.sin(ang) * l, y2 = -72 + Math.cos(ang) * l;
      e.setAttribute("d", "M" + sx + " -72 L" + x2.toFixed(1) + " " + y2.toFixed(1));
    }
    function jambe(e, sx, ang) {
      e.setAttribute("d", "M" + sx + " -26 L" + (sx + Math.sin(ang) * 26).toFixed(1) + " " + (-26 + Math.cos(ang) * 26).toFixed(1));
    }
    return {
      g: gr, nom: nomT, couleur: PP.c,
      pose: function (x, y, act, t, ph, extra) {
        var k = echelle(y), dy = 0, rot = 0, aG = 0.25, aD = -0.25, jG = 0.12, jD = -0.12;
        if (act === "assis" || act === "tricote") { dy = 18; jG = 1.2; jD = 1.1; aG = 2.2 + (act === "tricote" ? Math.sin(t * 9 + ph) * .15 : 0); aD = -2.2 - (act === "tricote" ? Math.sin(t * 9 + ph + 1) * .15 : 0); }
        else if (act === "repasse") { aG = 1.4 + Math.sin(t * 2.2 + ph) * .35; aD = -0.6; }
        else if (act === "range") { aG = 2.6 + Math.sin(t * 1.4 + ph) * .3; aD = -0.4; }
        else if (act === "danse" || act === "danse_lourde" || act === "seule" || act === "danse_douce") {
          var vit = act === "danse_douce" ? 5 : act === "seule" ? 7.5 : 9, s = Math.sin(t * vit + ph);
          dy = -Math.abs(s) * (act === "danse_lourde" ? 9 : act === "danse_douce" ? 4 : 7);
          rot = s * (act === "danse_douce" ? 5 : act === "seule" ? 4 : 9);
          aG = 2.6 + s * .5; aD = -2.6 + s * .5; jG = .45 * s; jD = -.45 * s;
          if (act === "danse_lourde") { jG = .7 * s; jD = -.7 * s; aG = 1.8 + s * .7; aD = -1.8 + s * .7; }
          if (act === "seule") { aG = 1.0 + s * .3; aD = -1.0 + s * .3; }
        } else if (act === "halete") { dy = Math.sin(t * 6 + ph) * 1.5; aG = .35; aD = -.35; }
        if (extra && extra.main) { aD = -1.4; }
        bras(bg, -12, aG, 30); bras(bd, 12, aD, 30); jambe(jg, -7, jG); jambe(jd, 7, jD);
        corps.setAttribute("transform", "translate(0," + dy.toFixed(1) + ") rotate(" + rot.toFixed(1) + " 0 -40)");
        gr.setAttribute("transform", "translate(" + x.toFixed(1) + "," + y.toFixed(1) + ") scale(" + k.toFixed(3) + ")");
        op(ombre, act === "assis" || act === "tricote" ? .2 : 1);
      },
      masque: function (a) { op(masque, a); }, surplis: function (a) { op(surplis, a * .95); }
    };
  }

  TYPES.jeu = function (o, v) {
    var e = o.el; e.classList.add("v-illu", "v-jeu"); o.entree = "aucune";
    e.style.left = (v.x || 0) + "px"; e.style.top = (v.y || 40) + "px"; e.style.width = (v.w || 1160) + "px"; e.style.height = (v.h || 600) + "px";
    var s = sv("svg", { viewBox: "0 0 1160 600" }, e);
    // décor : sol, mur et fenêtre de la cuisine, fourneau, table, étagère et Marconi, porte ; jardin, sycamore, banc, chemin
    var monde = sv("g", {}, s), dec = sv("g", {}, monde);
    sv("path", { d: "M120 200 L1040 200 L1150 560 L10 560 Z", fill: "rgba(243,239,228,.05)", stroke: "rgba(243,239,228,.25)", "stroke-width": 2 }, dec);
    sv("path", { d: "M566 200 L1040 200 L1150 560 L566 560 Z", fill: "rgba(120,160,95,.10)" }, dec);
    sv("rect", { x: 120, y: 40, width: 446, height: 160, fill: "rgba(243,239,228,.06)", stroke: "rgba(243,239,228,.22)", "stroke-width": 2 }, dec);
    sv("rect", { x: 245, y: 70, width: 96, height: 78, fill: "rgba(160,190,230,.18)", stroke: "rgba(243,239,228,.4)", "stroke-width": 3 }, dec);
    sv("path", { d: "M293 70 V148 M245 109 H341", stroke: "rgba(243,239,228,.35)", "stroke-width": 2 }, dec);
    sv("rect", { x: 140, y: 150, width: 70, height: 60, rx: 4, fill: "#2a2a2e", stroke: "rgba(243,239,228,.3)" }, dec);
    sv("path", { d: "M165 150 V60", stroke: "rgba(243,239,228,.25)", "stroke-width": 8 }, dec);
    sv("path", { d: "M400 160 H520", stroke: "rgba(243,239,228,.4)", "stroke-width": 4 }, dec);
    var radio = sv("rect", { x: 440, y: 126, width: 48, height: 34, rx: 7, fill: "#6b4b2e", stroke: C.sa, "stroke-width": 2 }, dec);
    sv("text", { x: 464, y: 120, "text-anchor": "middle", fill: C.sa, "font-size": 13, "letter-spacing": 2 }, dec, "MARCONI");
    sv("path", { d: "M250 350 H420 L430 380 H240 Z", fill: "rgba(160,120,80,.55)", stroke: "rgba(243,239,228,.3)" }, dec);
    sv("path", { d: "M566 205 V340", stroke: "rgba(243,239,228,.3)", "stroke-width": 3, "stroke-dasharray": "6 6" }, dec);
    sv("path", { d: "M960 200 C 940 120 990 60 1010 30 M1010 30 C 1060 60 1080 120 1060 200", stroke: "rgba(120,160,95,.5)", "stroke-width": 26, fill: "none", "stroke-linecap": "round" }, dec);
    sv("path", { d: "M790 330 H890 M800 330 V346 M880 330 V346", stroke: "rgba(243,239,228,.45)", "stroke-width": 4 }, dec);
    [["THE KITCHEN", 343, 30], ["THE GARDEN", 850, 186]].forEach(function (l) {
      sv("text", { x: l[1], y: l[2], "text-anchor": "middle", fill: "rgba(243,239,228,.4)", "font-size": 15, "letter-spacing": 4 }, dec, l[0]);
    });
    var notes = [0, 1, 2, 3].map(function () { return sv("text", { x: 0, y: 0, fill: C.sa, "font-size": 24, opacity: 0 }, monde, "♪"); });
    var statique = sv("path", { d: "M492 120 l6 -8 l5 10 l6 -12 l5 9", stroke: C.iv2, "stroke-width": 2, fill: "none", opacity: 0 }, monde);
    var calque = sv("g", {}, monde);
    var bulleG = sv("g", { opacity: 0 }, s), bulleR = sv("rect", { rx: 12, fill: "#fbfaf6" }, bulleG),
      bulleQ = sv("path", { d: "", fill: "#fbfaf6" }, bulleG), bulleT = sv("text", { "text-anchor": "middle", "font-size": 22, fill: "#1e2330", "font-weight": 600 }, bulleG);
    var noteG = sv("g", { opacity: 0 }, s), noteR = sv("rect", { x: 80, y: 6, width: 1000, height: 36, rx: 10, fill: "rgba(8,12,22,.72)" }, noteG),
      noteT = sv("text", { x: 580, y: 31, "text-anchor": "middle", "font-size": 20, fill: C.iv, "font-style": "italic", class: "ser" }, noteG);

    // états cumulés
    var noms = v.persos, ETATS = [], cur = { pos: {}, act: {}, masque: {}, surplis: {}, ronde: null, chemin: {}, radio: false, dit: null, note: null };
    (v.etats || []).forEach(function (st, k) {
      var n = { pos: Object.assign({}, cur.pos), act: Object.assign({}, cur.act), masque: Object.assign({}, cur.masque),
        surplis: Object.assign({}, cur.surplis), ronde: st.ronde !== undefined ? st.ronde : cur.ronde, chemin: {},
        radio: st.radio !== undefined ? st.radio : cur.radio, cam: st.cam || cur.cam || "cuisine", dit: st.dit || null, note: st.note !== undefined ? st.note : null };
      Object.assign(n.pos, st.pos || {}); Object.assign(n.act, st.act || {});
      (st.masque || []).forEach(function (x) { n.masque[x] = 1; }); (st.surplis || []).forEach(function (x) { n.surplis[x] = 1; });
      (st.sans_surplis || []).forEach(function (x) { n.surplis[x] = 0; });
      // un trajet continue d'un état à l'autre jusqu'à ce qu'un état redonne une position au personnage
      n.chemin = Object.assign({}, cur.chemin || {}); n.cheminDe = Object.assign({}, cur.cheminDe || {});
      Object.keys(st.chemin || {}).forEach(function (x) { n.chemin[x] = st.chemin[x]; n.cheminDe[x] = k; n.cheminDuree = n.cheminDuree || {}; });
      Object.keys(st.pos || {}).forEach(function (x) { delete n.chemin[x]; });
      n.cheminDurees = Object.assign({}, cur.cheminDurees || {});
      Object.keys(st.chemin || {}).forEach(function (x) { n.cheminDurees[x] = st.chemin_duree || 9; });
      n.duree = st.duree || 1.4; n.chemin_duree = st.chemin_duree || 9;
      ETATS.push(n); cur = n;
    });
    var figs = {}; noms.forEach(function (nm) { figs[nm] = figure(calque, nm); });
    function tEtat(k) { return k === 0 ? v.t0 : et(v, String(k), 2 + 3 * k); }
    function posA(st, nm) { var p = st.pos[nm]; return p === "off" || p == null ? null : lieu(p); }
    function posAt(k, nm, t) {
      var S = ETATS[k], tk = tEtat(k);
      var depart = function () { return k ? posAt(k - 1, nm, tk) : null; };
      if (S.ronde && S.ronde.indexOf(nm) >= 0) {
        var r = S.ronde.indexOf(nm), ang = (t - tk) * 1.1 + r * Math.PI * 2 / S.ronde.length;
        var c0 = LIEUX.centre, cx = c0[0] + Math.cos(ang) * 95, cy = c0[1] + Math.sin(ang) * 38;
        var d = depart() || [cx, cy], w = k ? EIO(P(t, tk, 1.2)) : 1;
        return [d[0] + (cx - d[0]) * w, d[1] + (cy - d[1]) * w];
      }
      if (S.chemin[nm]) {
        var pts = S.chemin[nm].map(lieu);
        return surChemin(pts, EIO(P(t, tEtat(S.cheminDe[nm]), S.cheminDurees[nm])));
      }
      var p1 = posA(S, nm);
      if (!p1) return null;
      var p0 = depart() || p1, u = k ? EIO(P(t, tk, S.duree)) : 1;
      return [p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u];
    }
    function surChemin(pts, u) {
      if (pts.length < 2) return pts[0];
      var L = [], tot = 0; for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); L.push(d); tot += d; }
      var x = u * tot;
      for (var j = 0; j < L.length; j++) { if (x <= L[j]) { var f = L[j] ? x / L[j] : 0; return [pts[j][0] + (pts[j + 1][0] - pts[j][0]) * f, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * f]; } x -= L[j]; }
      return pts[pts.length - 1];
    }
    return function (t, st) {
      var a = E(P(t, v.t0, .8)); op(dec, a);
      var k = 0; for (var i = 1; i < ETATS.length; i++) if (t >= tEtat(i)) k = i;
      var S = ETATS[k], prev = ETATS[Math.max(0, k - 1)], t0k = tEtat(k);
      var u = k ? EIO(P(t, t0k, S.duree)) : 1;
      var c1 = CAMS[S.cam] || CAMS.tout, c0 = CAMS[prev.cam] || c1, uc = k ? EIO(P(t, t0k, 2.2)) : 1;
      var cam = [0, 1, 2, 3].map(function (i) { return c0[i] + (c1[i] - c0[i]) * uc; }), sc = 1160 / cam[2];
      monde.setAttribute("transform", "scale(" + sc.toFixed(4) + ") translate(" + (-cam[0]).toFixed(2) + "," + (-cam[1]).toFixed(2) + ")");
      var ecran = function (x, y) { return [(x - cam[0]) * sc, (y - cam[1]) * sc]; };
      // radio : notes de musique ou parasites
      var on = S.radio === true;
      notes.forEach(function (n, i) {
        var c = ((t * .7 + i / 4) % 1);
        n.setAttribute("x", (470 + i * 9 + Math.sin(c * 6 + i) * 14).toFixed(1)); n.setAttribute("y", (118 - c * 70).toFixed(1));
        op(n, on ? Math.sin(c * Math.PI) * a : 0);
      });
      op(statique, S.radio === "parasites" ? (0.5 + 0.5 * Math.sin(t * 25)) * a : 0);
      radio.setAttribute("stroke-width", on ? 3 + Math.sin(t * 8) : 2);
      var ordre = [];
      noms.forEach(function (nm, idx) {
        var F = figs[nm], act = S.act[nm] || "debout";
        var q = posAt(k, nm, t), x = q ? q[0] : 0, y = q ? q[1] : 0, vis = 1;
        var la = function (X) { return posA(X, nm) || (X.ronde && X.ronde.indexOf(nm) >= 0) || X.chemin[nm] ? 1 : 0; };
        var vis1 = la(S), vis0 = k ? la(prev) : vis1;
        vis = vis0 + (vis1 - vis0) * u;
        if (!q) { var q0 = k ? posAt(k - 1, nm, t0k) : null; if (q0) { x = q0[0]; y = q0[1]; } }
        F.pose(x, y, act, t, idx * 1.7);
        op(F.g, vis * a);
        F.masque(S.masque[nm] ? (prev.masque[nm] ? 1 : u) : 0);
        F.surplis(S.surplis[nm] ? (prev.surplis[nm] ? 1 : u) : 0);
        ordre.push([y, F.g]);
        F._x = x; F._y = y;
      });
      ordre.sort(function (p, q) { return p[0] - q[0]; }).forEach(function (p) { calque.appendChild(p[1]); });
      // bulle de la réplique
      if (S.dit && figs[S.dit[0]]) {
        var F2 = figs[S.dit[0]], txt = S.dit[1];
        var lignes = coupe(txt, 40), lmax = Math.max.apply(null, lignes.map(function (l) { return l.length; }));
        var tete = ecran(F2._x, F2._y - 128 * echelle(F2._y)), fx = tete[0];
        var wv = 26 + lmax * 11.4, hb = 14 + lignes.length * 28, bx = cl(fx, wv / 2 + 10, 1150 - wv / 2), by = Math.max(hb + 6, tete[1] - 14);
        if (bulleT._txt !== txt) {
          bulleT._txt = txt; while (bulleT.firstChild) bulleT.removeChild(bulleT.firstChild);
          lignes.forEach(function (l, i) { sv("tspan", { x: 0, dy: i ? 28 : 0 }, bulleT, l); });
        }
        bulleR.setAttribute("x", bx - wv / 2); bulleR.setAttribute("y", by - hb + 12); bulleR.setAttribute("width", wv); bulleR.setAttribute("height", hb);
        bulleT.setAttribute("transform", "translate(" + bx.toFixed(1) + "," + (by - hb + 38).toFixed(1) + ")");
        bulleQ.setAttribute("d", "M" + (fx - 9) + " " + (by + 11) + " L" + fx + " " + (by + 26) + " L" + (fx + 9) + " " + (by + 11) + " Z");
        bulleR.setAttribute("stroke", F2.couleur); bulleR.setAttribute("stroke-width", 3);
        op(bulleG, E(P(t, t0k + .1, .35)) * a);
      } else op(bulleG, 0);
      if (S.note) {
        if (noteT.textContent !== S.note) { noteT.textContent = S.note; var lw = Math.min(1140, 40 + S.note.length * 9.6); noteR.setAttribute("x", 580 - lw / 2); noteR.setAttribute("width", lw); }
        op(noteG, E(P(t, t0k, .6)) * a);
      } else op(noteG, 0);
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

  /* ---------- scène ---------- */
  var FONDS = {
    nuit: { base: "linear-gradient(160deg,#0c1322 0%,#19213a 55%,#121a2b 100%)", lueurs: ["rgba(230,203,139,.20)", "rgba(79,154,142,.16)", "rgba(120,90,160,.16)"] },
    aube: { base: "linear-gradient(160deg,#1a1527 0%,#2a2036 55%,#181d31 100%)", lueurs: ["rgba(230,203,139,.24)", "rgba(194,97,76,.18)", "rgba(79,154,142,.12)"] }
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
      ent.innerHTML = esc(EP.notion) + " · Part " + EP.num + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
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
    document.title = EP.notion + " · Part " + EP.num + " — " + EP.titre;
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
      h("span", "k", tete, esc(EP.notion) + " · part " + EP.num);
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
      bCC = h("button", "btn", barre, ICO.cc), bFS = h("button", "btn", barre, ICO.plein);
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
    h("div", "sous", quiz, EP.quiz.length + " questions on this part. Answer, then read the explanation.");
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
        navigator.mediaSession.metadata = new MediaMetadata({ title: "Part " + EP.num + " · " + EP.titre, artist: "ACL · Dancing at Lughnasa", album: EP.notion });
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
