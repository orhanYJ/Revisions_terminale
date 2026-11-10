/* Vidéos de SES (« Faits & Courbes ») — moteur du lecteur, copie du moteur PC (pc/serie/moteur.js) aux couleurs du site
   (canard, corail, moutarde, ivoire sur encre) et aux typographies d'un magazine de données (IBM Plex Sans Condensed,
   Archivo, Spectral, polices locales dans fonts/).
   Repris du moteur PC : formules, graphiques, exercices, moments « À toi » où la vidéo s'arrête d'elle-même (type pause).
   Ajouts propres à la SES (mode d'emploi en tête de chaque type, plus bas) :
     donnees  graphique de données réelles du site (GRAPHES : barres par année, barres horizontales) qui se construit ;
     chaine   chaîne causale du site (CHAINES) qui se déroule étape par étape, caméra qui suit, boucle possible ;
     chiffres grands chiffres (bandeau « En chiffres ») qui comptent jusqu'à leur valeur, avec leur source ;
     sanim    animation du site (ANIMS, outils/specialites/ses/src/data-anim-*.js) rejouée et pilotée par le temps ;
     auteur   fiche d'auteur (monogramme, nom, repères, idée) comme dans le site ;
     compare  tableau comparatif à deux colonnes, ligne par ligne ;
     plan     plan de copie ou synthèse en colonnes, colonne par colonne.
   Les graphiques, chaînes et animations viennent des sources du site (outils/serie-ses/site_ses.py) : mêmes données,
   mêmes sources. Les animations sont chargées par site-ses.js (généré), avant ce moteur.
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py depuis outils/serie-ses/<module>.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  // sa = accent principal (corail), ca = canard clair, mo = moutarde, vert ; mêmes valeurs que le thème sombre du site
  var C = { iv: "#ECE6DA", iv2: "#A5B0B3", sa: "#FF7B65", sa2: "#E5533F", ca: "#5BB8C4", te: "#5BB8C4", mo: "#F0BE4F", nuit: "#0D181C",
    el: "#5BB8C4", uv: "#b48cff", rouge: "#FF7B65", vert: "#6CC18E", or: "#F0BE4F", canard: "#5BB8C4", corail: "#FF7B65", moutarde: "#F0BE4F",
    encre: "#0D181C", carte: "#14232A", carte2: "#1B2E36" };
  var CODE_Q = function (code) { var m = /-([esr])(\d+)$/.exec(code || ""); return m ? { e: "É", s: "S", r: "R" }[m[1]] + m[2] : ""; };

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
    return String(s).replace(/(\d) (?=\d{3}(?!\d))/g, "$1\u202f").replace(/ (%|€|points?\b)/g, "\u00a0$1").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
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
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(255,123,101," + (0.7 * (1 - f)).toFixed(2) + ")";
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

  // pictogrammes des cartes (type cartes, champ ic), dessinés trait par trait
  var ICONES = {
    ressource: ["M50 10 C34 36 22 52 22 64 a28 28 0 0 0 56 0 C78 52 66 36 50 10 Z", "M38 66 a12 12 0 0 0 12 12"],
    pollution: ["M12 88 V52 L32 64 V52 L52 64 V30 H66 V88 Z", "M70 26 C62 18 76 12 68 4", "M84 32 C76 22 90 16 84 6", "M8 88 H92"],
    climat: ["M44 16 a6 6 0 0 1 12 0 V62 a14 14 0 1 1 -12 0 Z", "M50 74 V36", "M66 22 H78 M66 34 H74 M66 46 H78"],
    rd: ["M40 10 H60", "M44 10 V40 L22 80 a6 6 0 0 0 6 8 H72 a6 6 0 0 0 6 -8 L56 40 V10", "M31 66 H69"],
    humain: ["M8 40 L50 22 L92 40 L50 58 Z", "M26 49 V68 C40 80 60 80 74 68 V49", "M92 40 V64"],
    infra: ["M8 82 H92", "M18 82 V54 M82 82 V54", "M8 54 C30 30 70 30 92 54", "M34 82 V44 M50 82 V40 M66 82 V44"],
    efficacite: ["M18 82 C18 42 48 18 86 16 C84 54 60 82 18 82 Z", "M18 82 L62 38"],
    substitution: ["M50 92 V46", "M50 46 L50 10", "M50 46 L82 64", "M50 46 L18 64", "M38 92 H62"],
    capter: ["M28 34 A30 30 0 0 1 78 42", "M78 42 L82 28 M78 42 L64 38", "M72 68 A30 30 0 0 1 22 58", "M22 58 L18 72 M22 58 L36 62"],
    brevet: ["M26 46 H74 V88 H26 Z", "M36 46 V32 a14 14 0 0 1 28 0 V46", "M50 62 V72"],
    usine: ["M10 88 V50 L30 62 V50 L50 62 V50 L70 62 V24 H84 V88 Z", "M6 88 H94"],
    loi: ["M50 12 V84", "M30 84 H70", "M18 30 H82", "M18 30 L8 58 H28 Z", "M82 30 L72 58 H92 Z"]
  };
  function icone(nom, parent) {
    var s = sv("svg", { viewBox: "0 0 100 100" }, parent);
    return (ICONES[nom] || []).map(function (d) {
      return sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 4.5, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    });
  }
  var ILLU = {};
  function fleche(g, d, col, ep) {
    var p = sv("path", { d: d, fill: "none", stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round" }, g);
    return { p: p, pointe: pointe(g, p, col, Math.max(15, (ep || 3) * 1.9)) };
  }

  // l'onde : sinusoïde qui avance, longueur d'onde λ, célérité c ; {id.2} : une onde de fréquence double en dessous
  // nombres à la française : 5,2 · −0,9 · 2 646,7
  function frN(n, d) {
    var s = Math.abs(n).toFixed(d == null ? 1 : d), p = s.split(".");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (n < 0 && +s !== 0 ? "−" : "") + p.join(",");
  }

  // décomposition de la croissance (exemple chiffré inventé du site, démarche de Solow) : une barre de 2,0 % qui se
  // remplit de la contribution du travail {id.1}, du capital {id.2}, puis du reste, la PGF {id.3} ; {id.4} le calcul
  ILLU.residu = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), x0 = 70, L = W_ - 140, y = H_ * .38, hb = 92, u = L / 2.0;
    var cadre = sv("rect", { x: x0, y: y, width: L, height: hb, rx: 14, fill: "none", stroke: "rgba(236,230,218,.35)", "stroke-width": 2, "stroke-dasharray": "8 7" }, g);
    var tot = etiquette(g, x0 + L, y - 26, "croissance : 2,0 % par an", { ancre: "end", fs: 30, c: C.iv, fw: 700 });
    var parts = [[0.4, C.canard, "travail", "0,4 point"], [0.6, C.moutarde, "capital", "0,6 point"], [1.0, C.corail, "PGF : le reste", "1,0 point"]];
    var cum = 0;
    var els = parts.map(function (p, i) {
      var gg = sv("g", {}, g), xa = x0 + cum * u, w = p[0] * u; cum += p[0];
      var r = sv("rect", { x: xa, y: y, width: w, height: hb, rx: i === 0 ? 14 : 0, fill: p[1], opacity: .9 }, gg);
      var t1 = etiquette(gg, xa + w / 2, y + hb / 2 + 11, p[3], { fs: 30, c: "#0D181C", fw: 700 });
      var t2 = etiquette(gg, xa + w / 2, y + hb + 44, p[2], { fs: 27, c: p[1], fw: 600 });
      return { g: gg, r: r, w: w };
    });
    var calc = etiquette(g, W_ / 2, H_ - 30, "PGF = 2,0 − 0,4 − 0,6 = 1,0 point : la moitié de la croissance", { fs: 31, c: C.iv, fw: 600 });
    var ex = etiquette(g, x0, 34, "Exemple chiffré inventé", { ancre: "start", fs: 20, c: C.iv2, fw: 500 });
    return function (t, st) {
      var tl = st.tl;
      op(cadre, E(P(tl, 0, .6))); op(tot, E(P(tl, .2, .6))); op(ex, E(P(tl, .3, .6)) * .9);
      els.forEach(function (e, i) {
        var k = et(v, String(i + 1), 1 + i * 1.4), q = EIO(P(t, k, .9));
        op(e.g, q > 0 ? 1 : 0); e.r.setAttribute("width", Math.max(0.01, e.w * q).toFixed(1));
      });
      op(calc, E(P(t, et(v, "4", 5.5), .7)));
    };
  };

  // polarisation des emplois, schéma de principe (sans données) : trois groupes d'emplois rangés par niveau de salaire ;
  // {id.1} le milieu routinier recule, {id.2} les deux extrémités résistent ou progressent
  ILLU.polarisation = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), base = H_ - 120, cw = (W_ - 160) / 3;
    var axe = sv("path", { d: "M50 " + base + " H" + (W_ - 30), stroke: C.iv, "stroke-width": 2.4, fill: "none" }, g);
    var ax2 = etiquette(g, W_ - 30, base + 96, "niveau de salaire et de qualification →", { ancre: "end", fs: 23, c: C.iv2, fw: 500 });
    var gr = [["peu qualifiés non routiniers", "aide à domicile, livraison, restauration", 150, 205, C.moutarde],
      ["intermédiaires routiniers", "saisie, guichet, travail à la chaîne", 250, 130, C.corail],
      ["très qualifiés", "conception, encadrement, analyse", 150, 225, C.canard]].map(function (d, i) {
      var x = 80 + i * (cw + 25), gg = sv("g", {}, g);
      var r = sv("rect", { x: x, y: base - d[2], width: cw, height: d[2], rx: 10, fill: d[4], opacity: .85 }, gg);
      var t1 = etiquette(gg, x + cw / 2, base + 34, d[0], { fs: 25, c: C.iv, fw: 700 });
      var t2 = etiquette(gg, x + cw / 2, base + 64, d[1], { fs: 19, c: C.iv2, fw: 500 });
      var fl = sv("text", { x: x + cw / 2, y: base - Math.max(d[2], d[3]) - 24, "text-anchor": "middle", fill: d[3] < d[2] ? C.corail : C.vert, "font-size": 56, "font-weight": 700 }, gg, d[3] < d[2] ? "↓" : "↑");
      return { g: gg, r: r, d: d, fl: fl, x: x };
    });
    var lg = etiquette(g, 50, 36, "Schéma de principe (sans données)", { ancre: "start", fs: 20, c: C.iv2, fw: 500 });
    return function (t, st) {
      var tl = st.tl;
      op(axe, E(P(tl, 0, .5))); op(ax2, E(P(tl, .3, .6))); op(lg, E(P(tl, .3, .6)) * .9);
      var k1 = et(v, "1", 2.5), k2 = et(v, "2", 5);
      gr.forEach(function (o, i) {
        op(o.g, E(P(tl, .3 + i * .3, .6)));
        var k = i === 1 ? k1 : k2, q = EIO(P(t, k, 1.2)), hh = o.d[2] + (o.d[3] - o.d[2]) * q;
        o.r.setAttribute("y", (base - hh).toFixed(1)); o.r.setAttribute("height", hh.toFixed(1));
        op(o.fl, E(P(t, k + .4, .5)));
      });
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
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(255,123,101,.9)";
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
      var pg = E(P(t, tg, .7)), pd = E(P(t, td, .7)), g0 = E(P(st.tl, .1, .6)) * .16;
      op(g, g0 + (1 - g0) * pg); tr(g, "translateX(" + (-50 * (1 - pg)) + "px)");
      op(d, g0 + (1 - g0) * pd); tr(d, "translateX(" + (50 * (1 - pd)) + "px)");
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
        var p = E(P(t, tk[i], .7)), g0 = E(P(st.tl, .1 + i * .15, .6)) * .18;
        op(c.c, g0 + (1 - g0) * p); tr(c.c, "translateY(" + (40 * (1 - p)) + "px) scale(" + (0.94 + 0.06 * p) + ")");
        c.ic.forEach(function (pa, j) { trace(pa, P(t, tk[i] + .2 + j * .15, .8)); });
        var actif = (t >= tk[i] && (i === cs.length - 1 || t < tk[i + 1]) && v.et && v.et[String(i + 1)] != null) || (hl != null && t >= hl);
        var pul = hl != null && t >= hl ? 0.5 + 0.5 * Math.sin((t - hl) * 4 + i) : 1;
        c.c.style.borderColor = actif ? "rgba(255,123,101," + (0.5 + 0.4 * pul) + ")" : "rgba(236,230,218,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(255,123,101,.25)" : "none";
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
    // SES : échelle linéaire de la première à la dernière date (de, a : bornes facultatives), graduée tous les 25 ou 50 ans
    var ds = v.items.map(function (it) { return it.d; }), a0 = v.de != null ? v.de : Math.min.apply(null, ds) - 8, a1 = v.a != null ? v.a : Math.max.apply(null, ds) + 8;
    function X(an) { return 120 + (an - a0) / (a1 - a0) * 1040; }
    var axe = h("div", "axe", e);
    var rupt = h("div", "rupt", e, ""); rupt.style.display = "none";
    var pasA = a1 - a0 > 140 ? 50 : 25, grad = [];
    for (var an_ = Math.ceil(a0 / pasA) * pasA; an_ <= a1; an_ += pasA) grad.push([an_, String(an_)]);
    var ans = grad.map(function (a) {
      var d = h("div", "an", e, a[1]); d.style.left = X(a[0]) + "px"; return d;
    });
    var RANGS = [{ top: 168, tige: [84, 120] }, { top: 420, tige: [-48, 48] }, { top: 66, tige: [84, 222] }, { top: 560, tige: [-188, 188] }];
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
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "Faits & Courbes · SES Terminale");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    tt.style.fontSize = Math.min(120, Math.floor(2300 / Math.max(12, String(v.serie).length))) + "px"; tt.style.textAlign = "center";
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, "Le cours en vidéo · " + (CODE_Q(EP_CODE) || "chapitre " + v.num));
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
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(255,123,101,.35)";
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

  // lentille convergente : axe, foyers, objet AB ; {id.1} rayon parallèle → F′, {id.2} rayon par O, {id.3} rayon par F,
  // {id.4} image A′B′ (position par la relation de conjugaison). v.oa : position de l'objet en multiples de f′ (négative)
  /* ---------- types propres à la SES ---------- */

  // graduations « rondes » entre min et max
  function graduations(min, max, n) {
    var brut = (max - min) / (n || 5), p = Math.pow(10, Math.floor(Math.log10(brut))), f = brut / p;
    var pas = (f < 1.5 ? 1 : f < 3 ? 2 : f < 7 ? 5 : 10) * p, out = [];
    for (var x = Math.ceil(min / pas - 1e-9) * pas; x <= max + 1e-9; x += pas) out.push(Math.round(x * 1e6) / 1e6);
    return out;
  }
  function cadreMag(e, v, g) {      // en-tête et pied d'un graphique du site : surtitre, titre, sous-titre, source
    var tete = h("div", "dn-tete", e);
    h("div", "dn-k", tete, esc(v.kicker || "Graphique · données réelles"));
    var ti = h("div", "dn-t", tete, esc(v.titre || g.t));
    var st = (v.sous !== false && (v.sous || g.s)) ? h("div", "dn-s", tete, esc(String(v.sous || g.s).replace(/ ?Touche une barre pour lire la valeur\.?/, ""))) : null;
    var src = (g.src || v.src) ? h("div", "dn-src", e, esc(v.src || g.src)) : null;
    return { tete: tete, ti: ti, st: st, src: src };
  }

  // donnees : un graphique du site (GRAPHES[...], recopié par le script : dict(type="donnees", g=D["graphes"]["e1-pib"], …)).
  //   g.type "barres" (une barre par année) : phases=[dict(de=1950, a=1973, l="…", moy=5.2, dur=3), …] ; la phase k se
  //     construit au repère {id.k} (barres qui montent année après année, étiquette de la dernière valeur, bande et moyenne) ;
  //     sans phases, tout monte au début. Les notes du site (1975, 2009, 2020…) s'affichent quand leur barre est là.
  //   g.type "hbarres" (barres horizontales) : la barre k pousse au repère {id.k}.
  //   x, y, w, h : cadre (défaut 80, 80, 1120, 580) ; titre, sous, src, kicker : remplacent ceux du site si besoin.
  TYPES.donnees = function (o, v) {
    var e = o.el, g = v.g; e.classList.add("v-donnees");
    var X0 = v.x != null ? v.x : 80, Y0 = v.y != null ? v.y : 80, Wd = v.w || 1120, Hd = v.h || 580;
    e.style.left = X0 + "px"; e.style.top = Y0 + "px"; e.style.width = Wd + "px"; e.style.height = Hd + "px";
    var cm = cadreMag(e, v, g);
    var top = cm.st ? 118 : 86, bas = cm.src ? 48 : 16;
    var zone = h("div", "dn-zone", e); zone.style.top = top + "px"; zone.style.bottom = bas + "px";
    var Wz = Wd - 36, Hz = Hd - top - bas;
    var s = sv("svg", { viewBox: "0 0 " + Wz + " " + Hz, width: Wz, height: Hz }, zone);
    var u = g.unite || "", dec = v.dec != null ? v.dec : 1;
    var upd;
    if (g.type === "barres") {
      var xs = g.x, ys = g.y, n = xs.length;
      var mn = g.min != null ? g.min : Math.min(0, Math.min.apply(null, ys)), mx = g.max != null ? g.max : Math.max.apply(null, ys);
      var ml = 78, mr = 20, mt = 30, mb = 46, pw = Wz - ml - mr, ph = Hz - mt - mb, bw = pw / n;
      var Y = function (y) { return mt + (1 - (y - mn) / (mx - mn)) * ph; }, XB = function (k) { return ml + k * bw; };
      var fond = sv("g", {}, s);
      graduations(mn, mx, 5).forEach(function (y) {
        sv("line", { x1: ml, x2: ml + pw, y1: Y(y), y2: Y(y), stroke: y === 0 ? "rgba(236,230,218,.75)" : "rgba(236,230,218,.12)", "stroke-width": y === 0 ? 2 : 1 }, fond);
        sv("text", { x: ml - 12, y: Y(y) + 7, "text-anchor": "end", fill: C.iv2, "font-size": 21 }, fond, (y > 0 ? "+" : "") + frN(y, 0) + u.trim().replace(/^/, " "));
      });
      var pasX = g.pasX || 10;
      xs.forEach(function (an, k) {
        if (an % pasX === 0 || (k === n - 1 && an % pasX > pasX / 2)) sv("text", { x: XB(k) + bw / 2, y: Hz - 12, "text-anchor": "middle", fill: C.iv2, "font-size": 21 }, fond, String(an));
      });
      var bandes = sv("g", {}, s), barres = sv("g", {}, s), haut = sv("g", {}, s);
      var phases = (v.phases || [{ de: xs[0], a: xs[n - 1] }]).map(function (ph_, i) {
        var k0 = xs.indexOf(ph_.de), k1 = xs.indexOf(ph_.a);
        var bd = sv("rect", { x: XB(k0), y: mt - 8, width: (k1 - k0 + 1) * bw, height: ph + 8, fill: "rgba(240,190,79,.12)", rx: 6 }, bandes);
        var xl = XB(k0) + (k1 - k0 + 1) * bw / 2, anc = "middle";
        var demi = String(ph_.l || "").length * 6.5;       // demi-largeur approchée de l'étiquette (23 px, gras)
        if (xl + demi > ml + pw) { xl = ml + pw - 4; anc = "end"; } else if (xl - demi < ml) { xl = ml + 4; anc = "start"; }
        var lb = ph_.l ? sv("text", { x: xl, y: mt + 22, "text-anchor": anc, fill: C.mo, "font-size": 23, "font-weight": 700 }, haut, ph_.l) : null;
        var moy = null, moyT = null;
        if (ph_.moy != null) {
          moy = sv("line", { x1: XB(k0), x2: XB(k1 + 1), y1: Y(ph_.moy), y2: Y(ph_.moy), stroke: C.mo, "stroke-width": 3.2, "stroke-dasharray": "10 6" }, haut);
          var lp = ph_.lp;   // place de l'étiquette [année, valeur], si la place par défaut est prise
          moyT = sv("text", { x: lp ? XB(xs.indexOf(lp[0])) : XB(k1 + 1) + 6, y: lp ? Y(lp[1]) : Y(ph_.moy) - 10, "text-anchor": lp ? "middle" : XB(k1 + 1) > ml + pw - 120 ? "end" : "start", fill: C.mo, "font-size": 22, "font-weight": 700, "paint-order": "stroke", stroke: "#0D181C", "stroke-width": 5 }, haut, "moyenne " + frN(ph_.moy, 1) + " %/an");
        }
        return { k0: k0, k1: k1, bd: bd, lb: lb, moy: moy, moyT: moyT, dur: ph_.dur || Math.min(4, .8 + (k1 - k0 + 1) * .1), i: i };
      });
      var rects = ys.map(function (y, k) { return sv("rect", { x: (XB(k) + bw * .14).toFixed(1), width: (bw * .72).toFixed(1), y: Y(0), height: 0, rx: 2, fill: y < 0 ? C.corail : C.canard }, barres); });
      var notes = (g.notes || []).map(function (nt) {
        var k = xs.indexOf(nt.x), yy = nt.y < 0 ? Math.min(Y(nt.y) + 30, mt + ph - 6) : Y(nt.y) - 12, fin_ = k > n - 6;
        return { k: k, t: sv("text", { x: fin_ ? XB(k) - 6 : XB(k) + bw / 2, y: yy, "text-anchor": fin_ ? "end" : "middle", fill: nt.y < 0 ? C.corail : C.iv, "font-size": 21, "font-weight": 700, "paint-order": "stroke", stroke: "#0D181C", "stroke-width": 5 }, haut, nt.t + " : " + (nt.y > 0 ? "+" : "") + frN(nt.y, 1) + " %") };
      });
      var bulle = sv("text", { "text-anchor": "middle", fill: C.iv, "font-size": 24, "font-weight": 700, "paint-order": "stroke", stroke: "#0D181C", "stroke-width": 6 }, haut);
      upd = function (t) {
        // instant où chaque barre est atteinte
        var tk = phases.map(function (p, i) { return et(v, String(i + 1), 1 + i * 4); });
        var dernier = -1, actif = -1, qs = [];
        rects.forEach(function (r, k) {
          var q = 0;
          phases.forEach(function (p, i) {
            if (k < p.k0 || k > p.k1) return;
            var f = (t - tk[i]) / p.dur * (p.k1 - p.k0 + 1) - (k - p.k0);
            q = Math.max(q, E(cl(f * 1.6, 0, 1)));
          });
          var y = ys[k] * q, y1 = Y(Math.max(0, y)), y2 = Y(Math.min(0, y));
          r.setAttribute("y", y1.toFixed(1)); r.setAttribute("height", Math.max(0, y2 - y1).toFixed(1));
          if (q > .5) dernier = k;
          qs[k] = q;
        });
        phases.forEach(function (p, i) {
          var q = P(t, tk[i], .4), fin = i + 1 < phases.length ? P(t, tk[i + 1], .6) : 0;
          if (t >= tk[i]) actif = i;
          op(p.bd, E(q) * (1 - E(fin)));
          if (p.lb) op(p.lb, E(q) * (1 - E(fin)));
          var qm = P(t, tk[i] + p.dur + .3, .6);
          if (p.moy) { trace(p.moy, EIO(qm)); op(p.moyT, E(P(t, tk[i] + p.dur + .7, .5))); }
        });
        notes.forEach(function (nt) { op(nt.t, E(cl(((qs[nt.k] || 0) - .6) / .4, 0, 1))); });
        // valeur de la barre qui vient de pousser, pendant la construction
        var p = actif >= 0 ? phases[actif] : null, enCours = p && t < tk[actif] + p.dur + .4;
        if (enCours && dernier >= p.k0 && !(g.notes || []).some(function (nt) { return nt.x === xs[dernier]; })) {
          var yv = ys[dernier];
          bulle.textContent = xs[dernier] + " : " + (yv > 0 ? "+" : "") + frN(yv, 1) + " %";
          bulle.setAttribute("x", cl(XB(dernier) + bw / 2, ml + 90, ml + pw - 90).toFixed(1));
          bulle.setAttribute("y", (yv >= 0 ? Y(yv) - 16 : Y(yv) + 34).toFixed(1));
          op(bulle, 1);
        } else op(bulle, 0);
      };
    } else {        // hbarres
      var cats = g.cats, vals = g.series[0].v, nc = cats.length;
      var lab = v.lab || Math.min(360, 40 + Math.max.apply(null, cats.map(function (c) { return c.length; })) * 14);
      var mn2 = Math.min(0, Math.min.apply(null, vals)), mx2 = Math.max(0, Math.max.apply(null, vals));
      var marge = (mx2 - mn2) * .06;
      if (mn2 < 0) mn2 -= marge; if (mx2 > 0) mx2 += marge;
      var pw2 = Wz - lab - 40 - 150, rh = Math.min(120, (Hz - 30) / nc), bh = rh * .6, y00 = Math.max(10, (Hz - nc * rh) / 2);
      var X = function (x) { return lab + 20 + (x - mn2) / (mx2 - mn2) * pw2; };
      var z = sv("line", { x1: X(0), x2: X(0), y1: y00 - 6, y2: y00 + nc * rh + 6, stroke: "rgba(236,230,218,.75)", "stroke-width": 2 }, s);
      var lignes = cats.map(function (c, k) {
        var yc = y00 + k * rh + rh / 2, gg = sv("g", {}, s);
        var lt = h("div", "dn-cat", zone, esc(c)); lt.style.top = (yc - 20) + "px"; lt.style.width = lab + "px";
        var r = sv("rect", { x: X(0), y: yc - bh / 2, width: 0, height: bh, rx: 6, fill: (v.couleurs || [])[k] ? C[v.couleurs[k]] || v.couleurs[k] : (vals[k] < 0 ? C.corail : C.canard) }, gg);
        var tv = sv("text", { y: yc + 11, fill: vals[k] < 0 ? C.corail : C.iv, "font-size": 32, "font-weight": 700, "text-anchor": "start" }, gg);
        return { lt: lt, r: r, tv: tv, v: vals[k], g: gg };
      });
      upd = function (t, st) {
        op(z, E(P(st.tl, .4, .5)));
        lignes.forEach(function (l, k) {
          var tk = et(v, String(k + 1), 1 + k * 1.2), q = EIO(P(t, tk, 1.1)), val = l.v * q;
          op(l.lt, E(P(t, tk - .3, .5)));
          var xa = X(0), xb = X(val);
          l.r.setAttribute("x", Math.min(xa, xb).toFixed(1)); l.r.setAttribute("width", Math.abs(xb - xa).toFixed(1));
          l.tv.textContent = q > 0 ? (l.v > 0 && v.signe !== false ? "+" : "") + frN(val, dec) + u : "";
          l.tv.setAttribute("x", ((l.v < 0 ? xa : xb) + 14).toFixed(1));   // négatif : la valeur à droite de l'axe
        });
      };
    }
    return function (t, st) {
      var tl = st.tl;
      op(cm.tete, E(P(tl, 0, .6))); tr(cm.tete, "translateY(" + (12 * (1 - E(P(tl, 0, .6)))) + "px)");
      if (cm.src) op(cm.src, E(P(tl, .8, .6)) * .9);
      upd(t, st);
    };
  };

  // chaine : une chaîne causale du site (CHAINES[...]) : dict(type="chaine", c=D["chaines"]["e1-pgf"], …).
  //   L'étape k (élément k de c.e, une case ou deux en parallèle) apparaît au repère {id.k}, la flèche se trace et le mot de
  //   liaison (« donc », « or »…) s'écrit ; la caméra suit la dernière étape. {id.tout} : vue d'ensemble (dézoom) ;
  //   {id.boucle} : flèche de retour de la dernière étape vers la première (croissance endogène), avec vue d'ensemble.
  //   x, w : colonne (défaut 190, 900) ; kicker : surtitre (défaut « Mécanisme »).
  TYPES.chaine = function (o, v) {
    var e = o.el, c = v.c; e.classList.add("v-chaine"); o.entree = "aucune";
    var X0 = v.x != null ? v.x : 190, Wc = v.w || 900;
    e.style.left = X0 + "px"; e.style.width = Wc + "px";
    var tete = h("div", "ch-tete", e);
    h("div", "ch-k", tete, esc(v.kicker || "Mécanisme"));
    h("div", "ch-t", tete, esc(v.titre || c.t));
    var vue = h("div", "ch-vue", e), piste = h("div", "ch-piste", vue);
    var svg = sv("svg", { class: "ch-fl" }, piste);
    var rangs = c.e.map(function (el, i) {
      var r = h("div", "ch-rang", piste), noeuds = el.f || [el];
      var cases = noeuds.map(function (nd) { return h("div", "ch-case k-" + (nd.k || "meca"), r, esc(nd.t)); });
      var mot = el.a && i > 0 ? h("div", "ch-mot", piste, esc(el.a)) : null;
      return { r: r, cases: cases, mot: mot, fl: [], i: i };
    });
    var boucle = null, haut = 0, pret = false, VUE_H = 720 - 166 - 26;
    if (v.boucle) piste.style.paddingRight = "96px";      // place pour la flèche de retour
    function disposer() {
      // positions réelles des cases (polices chargées), puis flèches entre étapes successives
      var top = 0;
      rangs.forEach(function (rg, i) {
        rg.top = rg.r.offsetTop; rg.bas = rg.top + rg.r.offsetHeight;
        rg.pts = rg.cases.map(function (cs) { return { cx: rg.r.offsetLeft + cs.offsetLeft + cs.offsetWidth / 2, top: rg.top, bas: rg.bas, x1: rg.r.offsetLeft + cs.offsetLeft + cs.offsetWidth }; });
      });
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      haut = piste.scrollHeight;
      svg.setAttribute("viewBox", "0 0 " + Wc + " " + (haut + 20)); svg.setAttribute("width", Wc); svg.setAttribute("height", haut + 20);
      rangs.forEach(function (rg, i) {
        rg.fl = [];
        if (!i) return;
        var prev = rangs[i - 1];
        prev.pts.forEach(function (a) {
          rg.pts.forEach(function (b) {
            var y1 = a.bas + 4, y2 = b.top - 6;
            var d = Math.abs(a.cx - b.cx) < 2 ? "M" + a.cx + " " + y1 + " V" + (y2 - 2) : "M" + a.cx + " " + y1 + " C" + a.cx + " " + (y1 + 26) + " " + b.cx + " " + (y2 - 30) + " " + b.cx + " " + (y2 - 2);
            var p = sv("path", { d: d, fill: "none", stroke: C.iv2, "stroke-width": 3, "stroke-linecap": "round" }, svg);
            var tete_ = sv("path", { d: "M" + (b.cx - 9) + " " + (y2 - 10) + " L" + (b.cx + 9) + " " + (y2 - 10) + " L" + b.cx + " " + (y2 + 3) + " Z", fill: C.iv2 }, svg);
            rg.fl.push({ p: p, t: tete_ });
          });
        });
        if (rg.mot) {
          var seul = rg.pts.length === 1 && prev.pts.length === 1;
          rg.mot.style.top = ((prev.bas + rg.top) / 2 - 17) + "px";
          if (seul) rg.mot.style.left = (rg.pts[0].cx + 20) + "px";
          else { rg.mot.style.left = "auto"; rg.mot.style.right = (v.boucle ? 96 : 0) + "px"; }   // fourche : le mot au bord droit, hors des flèches
        }
      });
      if (v.boucle && v.et && v.et.boucle != null) {
        var der = rangs[rangs.length - 1], pr = rangs[0], xd = Wc - 40;
        var a1 = der.pts[der.pts.length - 1], b1 = pr.pts[pr.pts.length - 1];
        var y1 = (der.top + der.bas) / 2, y2 = (pr.top + pr.bas) / 2;
        var d2 = "M" + (a1.x1 + 4) + " " + y1 + " C" + (xd + 30) + " " + y1 + " " + (xd + 30) + " " + y2 + " " + (b1.x1 + 14) + " " + y2;
        var bp = sv("path", { d: d2, fill: "none", stroke: C.mo, "stroke-width": 4, "stroke-linecap": "round", "stroke-dasharray": "2 0" }, svg);
        boucle = { p: bp, pointe: pointe(svg, bp, C.mo, 20) };
      }
      pret = true;
    }
    function camera(t) {
      // défilement : la dernière étape apparue reste dans la vue ; vue d'ensemble aux repères tout / boucle
      var tk = rangs.map(function (_, i) { return et(v, String(i + 1), .6 + i * 1.8); });
      var dfl = 0, prec = 0;
      rangs.forEach(function (rg, i) {
        var cible = Math.max(0, rg.bas - VUE_H), q = EIO(P(t, tk[i], .9));
        dfl += (cible - prec) * q; prec = cible;
      });
      var tTout = v.et && (v.et.tout != null ? v.et.tout : v.et.boucle);
      var k = 1;
      if (tTout != null) {
        var q2 = EIO(P(t, tTout, 1.1)), kf = Math.min(1, VUE_H / (haut + 10));
        k = 1 + (kf - 1) * q2; dfl = dfl * (1 - q2);
      }
      return { dfl: dfl, k: k, tk: tk };
    }
    return function (t, st) {
      var policesOK = !document.fonts || document.fonts.status === "loaded";
      if (!pret || (policesOK && !e._polices)) { disposer(); e._polices = policesOK; }
      var tl = st.tl, cam = camera(t);
      op(tete, E(P(tl, 0, .6))); tr(tete, "translateY(" + (10 * (1 - E(P(tl, 0, .6)))) + "px)");
      piste.style.transform = "translateY(" + (-cam.dfl).toFixed(1) + "px) scale(" + cam.k.toFixed(4) + ")";
      var dernier = -1; cam.tk.forEach(function (x, i) { if (t >= x) dernier = i; });
      rangs.forEach(function (rg, i) {
        var a = E(P(t, cam.tk[i], .6));
        op(rg.r, a * (i === dernier || cam.k < .999 ? 1 : .72)); tr(rg.r, "translateY(" + (18 * (1 - a)).toFixed(1) + "px) scale(" + (0.96 + 0.04 * a).toFixed(3) + ")");
        rg.cases.forEach(function (cs) { cs.classList.toggle("on", i === dernier && cam.k > .999); });
        rg.fl.forEach(function (f) { trace(f.p, EIO(P(t, cam.tk[i] - .35, .45))); op(f.t, E(P(t, cam.tk[i] - .05, .2))); });
        if (rg.mot) { var m = E(P(t, cam.tk[i] - .1, .45)); op(rg.mot, m); tr(rg.mot, "translateX(" + (-10 * (1 - m)).toFixed(1) + "px)"); }
      });
      if (boucle) { var qb = P(t, v.et.boucle + .4, 1.4); trace(boucle.p, EIO(qb)); op(boucle.pointe(), qb > .95 ? 1 : 0); }
    };
  };

  // chiffres : bandeau « En chiffres » ; items=[dict(n="5,2 %", l="…", s="source"), …], le chiffre k compte jusqu'à sa
  //   valeur au repère {id.k} ; titre (défaut « En chiffres ») ; x, y, w.
  TYPES.chiffres = function (o, v) {
    var e = o.el; e.classList.add("v-chiffres"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 110) + "px"; e.style.top = (v.y != null ? v.y : 150) + "px"; e.style.width = (v.w || 1060) + "px";
    var tete = h("div", "cf-tete", e, esc(v.titre || "En chiffres")), ligne = h("div", "cf-ligne", e);
    var grille = h("div", "cf-grille n" + v.items.length, e);
    var its = v.items.map(function (it) {
      var d = h("div", "cf-it", grille), nb = h("div", "cf-n", d), l = h("div", "cf-l", d, esc(it.l)), so = it.s ? h("div", "cf-s", d, esc(it.s)) : null;
      // partie numérique à faire défiler : « ×8,6 », « 5,2 % », « −34,3 % », « 61,5 milliards »
      var m = /^(.*?)([−-]?)(\d[\d  ]*(?:,\d+)?)(.*)$/.exec(it.n);
      return { d: d, nb: nb, l: l, so: so, m: m, it: it };
    });
    return function (t, st) {
      op(tete, E(P(st.tl, 0, .5))); tr(ligne, "scaleX(" + EIO(P(st.tl, .1, .8)) + ")");
      its.forEach(function (x, i) {
        var tk = et(v, String(i + 1), .5 + i * 1.5), a = E(P(t, tk, .5));
        op(x.d, a); tr(x.d, "translateY(" + (24 * (1 - a)).toFixed(1) + "px)");
        if (x.m) {
          var brut = x.m[3].replace(/[  ]/g, ""), dec = (brut.split(",")[1] || "").length, val = parseFloat(brut.replace(",", "."));
          var q = E(P(t, tk + .1, 1.3)), cur = val * q;
          x.nb.innerHTML = esc(x.m[1]) + (x.m[2] && q > 0 ? "−" : "") + frN(cur, dec) + esc(x.m[4]);
        } else x.nb.innerHTML = esc(x.it.n);
        op(x.l, E(P(t, tk + .5, .6))); if (x.so) op(x.so, E(P(t, tk + .9, .6)) * .9);
      });
    };
  };

  // sanim : une animation du site (ANIMS[nom], site-ses.js) rejouée dans la vidéo ; l'étape k démarre au repère {id.k} et
  //   dure la durée du site (× vit), puis reste sur sa dernière image ; légende du site à droite (leg="droite", défaut) ou
  //   dessous (leg="bas"), ou sans (leg=False). x, y, h : place et hauteur de la figure (largeur = 360 × h / hauteur du site).
  TYPES.sanim = function (o, v) {
    var e = o.el; e.classList.add("v-sanim");
    var an = (window.ANIMS || {})[v.nom];
    if (!an || !window.ANIM_MOTEUR) { h("div", "sa-err", e, "Animation introuvable : " + esc(v.nom)); return function () {}; }
    var A = window.ANIM_MOTEUR.A, H0 = an.h || 300, hh = v.h || 560, k = hh / H0, ww = Math.round(360 * k);
    var X0 = v.x != null ? v.x : 60, Y0 = v.y != null ? v.y : 92;
    e.style.left = X0 + "px"; e.style.top = Y0 + "px";
    var fig = h("div", "sa-fig", e); fig.style.width = (ww + 36) + "px";
    var ti = h("div", "sa-t", fig, '<span>Animation</span>' + esc(an.t));
    var svg = sv("svg", { viewBox: "0 0 360 " + H0, width: ww, height: hh }, fig);
    var src = an.src && v.src !== false ? h("div", "sa-src", fig, esc(an.src.replace(/<[^>]+>/g, ""))) : null;
    var leg = v.leg === false ? null : h("div", "sa-leg " + (v.leg || "droite"), e);
    if (leg) {
      if ((v.leg || "droite") === "droite") { leg.style.left = (ww + 36 + 40) + "px"; leg.style.width = (v.lw || Math.max(300, 1280 - X0 - ww - 36 - 40 - 60)) + "px"; }
      else { leg.style.top = (hh + 110) + "px"; leg.style.width = (ww + 36) + "px"; }
    }
    var ln = leg ? h("div", "sa-n", leg) : null, lt = leg ? h("div", "sa-l", leg) : null;
    var n = an.etapes.length, vit = v.vit || 1, dernier = "", etDern = -1;
    return function (t, st) {
      var tl = st.tl;
      op(ti, E(P(tl, 0, .6)));
      if (src) op(src, E(P(tl, 1, .6)) * .85);
      var i = 0, p = 0;
      for (var j = 0; j < n; j++) {
        var tk = et(v, String(j + 1), .8 + j * 5);
        if (t >= tk) { i = j; p = cl((t - tk) / ((an.etapes[j].d || 3.5) * vit), 0, 1); }
      }
      if (t < et(v, "1", .8)) { i = 0; p = 0; }
      var cle = i + ":" + Math.round(p * 120);
      if (cle !== dernier) { dernier = cle; try { svg.innerHTML = an.rendu(A, i, p); } catch (err) { svg.innerHTML = ""; } }
      if (leg) {
        if (i !== etDern) { etDern = i; ln.textContent = "Étape " + (i + 1) + " / " + n; lt.textContent = an.etapes[i].l; lt._t = et(v, String(i + 1), .8); }
        var a = E(P(t, Math.max(lt._t || 0, v.t0), .6));
        op(leg, E(P(tl, .4, .6))); op(lt, t < et(v, "1", .8) ? 0 : a); tr(lt, "translateY(" + (12 * (1 - a)).toFixed(1) + "px)");
        op(ln, t < et(v, "1", .8) ? 0 : 1);
      }
    };
  };

  // auteur : fiche d'auteur comme dans le site (monogramme, nom, repères, idée) ; cles = mots qui s'allument à la voix
  TYPES.auteur = function (o, v) {
    var e = o.el; e.classList.add("v-auteur");
    e.style.left = (v.x != null ? v.x : 170) + "px"; e.style.top = (v.y != null ? v.y : 170) + "px"; e.style.width = (v.w || 940) + "px";
    var c = h("div", "au-carte", e), mono = h("div", "au-mono", c, esc(v.mono || v.nom.split(" ").map(function (x) { return x[0]; }).join("").slice(0, 2)));
    var corps = h("div", "au-corps", c), nm = h("div", "au-nom", corps, esc(v.nom)), inf = v.info ? h("div", "au-info", corps, esc(v.info)) : null;
    var tx = h("div", "au-tx", corps), sp = mots(tx, v.t, "mot-l cle"), kl = cles(v, sp);
    if (v.plus) h("div", "badge", c, esc(v.plus === true ? "Hors programme" : v.plus));
    return function (t, st) {
      var tl = st.tl; allume(kl, t);
      var m = P(tl, .05, .7); tr(mono, "scale(" + (0.5 + 0.5 * EB(m)) + ") rotate(" + (-40 * (1 - E(m))) + "deg)"); op(mono, E(m));
      op(nm, E(P(tl, .3, .5))); tr(nm, "translateX(" + (-16 * (1 - E(P(tl, .3, .5)))) + "px)");
      if (inf) op(inf, E(P(tl, .5, .5)));
      sp.forEach(function (w, i) { var q = E(P(tl, .7 + i * .045, .45)); w.style.opacity = q; w.style.transform = "translateY(" + (1 - q) * 8 + "px)"; });
    };
  };

  // compare : tableau à deux colonnes ; cols=["A", "B"], lignes=[["libellé", "texte A", "texte B"], …] ; la ligne k
  //   apparaît au repère {id.k} ; titre ; x, y, w.
  TYPES.compare = function (o, v) {
    var e = o.el; e.classList.add("v-compare");
    e.style.left = (v.x != null ? v.x : 80) + "px"; e.style.top = (v.y != null ? v.y : 110) + "px"; e.style.width = (v.w || 1120) + "px";
    if (v.titre) h("div", "cp-ti", e, esc(v.titre));
    var tb = h("div", "cp-tab", e), tete = h("div", "cp-l cp-h", tb);
    h("div", "cp-c0", tete); v.cols.forEach(function (cn, j) { h("div", "cp-c cp-c" + (j + 1), tete, esc(cn)); });
    var ls = v.lignes.map(function (l) {
      var d = h("div", "cp-l", tb); h("div", "cp-c0", d, esc(l[0]));
      var cs = [h("div", "cp-c", d, esc(l[1])), h("div", "cp-c", d, esc(l[2]))];
      return { d: d, cs: cs };
    });
    return function (t, st) {
      op(tete, E(P(st.tl, .1, .6)));
      ls.forEach(function (l, i) {
        var tk = et(v, String(i + 1), .6 + i * 1.5);
        l.cs.forEach(function (c, j) { var q = E(P(t, tk + j * .5, .6)); op(c, q); tr(c, "translateY(" + (10 * (1 - q)).toFixed(1) + "px)"); });
        op(l.d.firstChild, E(P(t, tk, .5)));
        l.d.style.borderColor = t >= tk ? "rgba(236,230,218,.16)" : "transparent";
      });
    };
  };

  // plan : un plan de copie (ou une synthèse) en colonnes ; titre en tête, parties=[dict(t="I. …", items=[…]), …] ;
  //   la colonne k apparaît au repère {id.k}, ses lignes l'une après l'autre ; x, y, w.
  TYPES.plan = function (o, v) {
    var e = o.el; e.classList.add("v-plan"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 70) + "px"; e.style.top = (v.y != null ? v.y : 90) + "px"; e.style.width = (v.w || 1140) + "px";
    var ti = v.titre ? h("div", "pl-ti", e, esc(v.titre)) : null;
    var gr = h("div", "pl-gr n" + v.parties.length, e), COUL = ["#5BB8C4", "#FF7B65", "#F0BE4F", "#6CC18E"];
    var cs = v.parties.map(function (pa, i) {
      var c = h("div", "pl-col", gr); c.style.borderTopColor = COUL[i % 4];
      var t = h("div", "pl-t", c, esc(pa.t)); t.style.color = COUL[i % 4];
      return { c: c, its: pa.items.map(function (x) { return h("div", "pl-it", c, esc(x)); }) };
    });
    return function (t, st) {
      if (ti) { var a = E(P(st.tl, 0, .6)); op(ti, a); tr(ti, "scale(" + (0.92 + 0.08 * EB(P(st.tl, 0, .7))) + ")"); }
      cs.forEach(function (c, i) {
        var tk = et(v, String(i + 1), .6 + i * 1.6), p = E(P(t, tk, .6)), g0 = E(P(st.tl, .3 + i * .15, .6)) * .15;
        op(c.c, g0 + (1 - g0) * p); tr(c.c, "translateY(" + (24 * (1 - p)).toFixed(1) + "px)");
        c.its.forEach(function (it, j) { var q = E(P(t, tk + .5 + j * .45, .5)); op(it, q); tr(it, "translateX(" + (-12 * (1 - q)).toFixed(1) + "px)"); });
      });
    };
  };

  /* ---------- repris du moteur PC ---------- */

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
    if (v.plus) h("div", "badge", c, "Hors programme");
    return function (t, st) {
      if (te) op(te, E(P(st.tl, .05, .5)));
      ls.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .25 + i * 1.1), p = E(P(t, t1, .55));
        op(x.d, p); tr(x.d, "translateY(" + (14 * (1 - p)).toFixed(1) + "px)");
        x.d.style.filter = p < 1 ? "blur(" + ((1 - p) * 5).toFixed(1) + "px)" : "none";
        if (x.l.cadre) {
          var q = P(t, t1 + .45, .9), g = Math.max(0, Math.sin((t - t1) * 2.2)) * (t > t1 + 1.3 ? .25 : 0);
          x.d.style.boxShadow = "0 0 0 2px rgba(255,123,101," + (.85 * E(q)).toFixed(2) + "),0 0 " + (34 * (1 - q) + 14 + 10 * g).toFixed(0) + "px rgba(255,123,101," + (.32 * E(q) + .1 * g).toFixed(2) + ")";
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
      grille.push(sv("line", { x1: X(x), x2: X(x), y1: m[2], y2: m[2] + ph, stroke: "rgba(236,230,218,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x), Y(y0) + 12, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("line", { x1: m[0], x2: m[0] + pw, y1: Y(y), y2: Y(y), stroke: "rgba(236,230,218,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x0) - 12, Y(y), esc(String(y).replace(".", ",")), "ty"));
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
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col, stroke: "#071013", "stroke-width": 1.5 }, g);
        });
        if (d.proj) {
          x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 1.6, "stroke-dasharray": "5 5", fill: "none", opacity: .8 }, g);
        }
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "rect" || d.type === "balaye") {
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: col, "fill-opacity": .22, stroke: col, "stroke-width": 2 }, g);
        x.pt = sv("circle", { r: 8, fill: col, stroke: "#071013", "stroke-width": 1.5 }, g);
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
  // les exercices de SES suivent les épreuves du bac : partie 1, 2 ou 3 de l'épreuve composée, dissertation, savoir-faire
  var NIVEAUX = { p1: ["Partie 1 · Mobilisation des connaissances", "#6CC18E"], p2: ["Partie 2 · Étude d'un document", "#5BB8C4"],
    p3: ["Partie 3 · Raisonnement sur dossier", "#F0BE4F"], dissert: ["Dissertation", "#FF7B65"], calcul: ["Savoir-faire · calculs", "#6CC18E"] };
  TYPES.exo = function (o, v) {
    var e = o.el, coin = v.mode === "coin"; e.classList.add("v-exo", coin ? "coin" : "plein");
    if (!coin) { e.style.left = (v.x || 110) + "px"; e.style.top = (v.y || 96) + "px"; e.style.width = (v.w || 1060) + "px"; }
    var c = h("div", "ex-carte", e), nv = NIVEAUX[v.niveau] || [v.niveau || "Exercice", C.sa];
    var tag = h("div", "ex-nv", c, esc(nv[0])); tag.style.color = nv[1]; tag.style.borderColor = nv[1];
    h("div", "ex-ti", c, esc(v.titre));
    if (v.src) h("div", "ex-src", c, esc(v.src));
    var paras = (coin ? [] : v.enonce || []).map(function (p) { return h("p", "ex-p", c, esc(p)); });
    var don = v.donnees && v.donnees.length ? h("div", "ex-don", c, "<b>Données</b> " + v.donnees.map(esc).join(" &nbsp;·&nbsp; ")) : null;
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
    var te = h("div", "pa-te", c, "À toi"), tx = h("div", "pa-tx", c, esc(v.t));
    var so = h("div", "pa-so", c, esc(v.sous || "Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."));
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
    // encre : le fond du site en thème sombre ; canard, corail, moutarde : la même encre teintée d'une couleur du site
    nuit: { base: "linear-gradient(160deg,#0b1619 0%,#14232a 55%,#0c171b 100%)", lueurs: ["rgba(91,184,196,.16)", "rgba(255,123,101,.10)", "rgba(240,190,79,.08)"] },
    canard: { base: "linear-gradient(160deg,#0a181c 0%,#123039 55%,#0b1a1f 100%)", lueurs: ["rgba(91,184,196,.22)", "rgba(91,184,196,.10)", "rgba(240,190,79,.08)"] },
    corail: { base: "linear-gradient(160deg,#16141a 0%,#2a1f22 55%,#141519 100%)", lueurs: ["rgba(255,123,101,.20)", "rgba(240,190,79,.10)", "rgba(91,184,196,.08)"] },
    moutarde: { base: "linear-gradient(160deg,#121612 0%,#25261a 55%,#111612 100%)", lueurs: ["rgba(240,190,79,.18)", "rgba(255,123,101,.10)", "rgba(91,184,196,.08)"] },
    vert: { base: "linear-gradient(160deg,#0b1714 0%,#14291f 55%,#0b1613 100%)", lueurs: ["rgba(108,193,142,.18)", "rgba(91,184,196,.10)", "rgba(240,190,79,.08)"] }
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
        cx.fillStyle = "rgba(236,230,218," + (a * .7).toFixed(3) + ")";
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
      ent.innerHTML = "SES · " + CODE_Q(EP.code) + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
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

  var EP_CODE = "";
  function lancer(EP) {
    document.title = CODE_Q(EP.code) + " — " + EP.titre + " · SES Terminale, le cours en vidéo"; EP_CODE = EP.code;
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
      h("span", "k", tete, "SES · " + CODE_Q(EP.code) + " · le cours en vidéo");
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
      bCC = h("button", "btn", barre, ICO.cc), bPA = h("button", "btn on", barre, ICO.apause), bFS = h("button", "btn", barre, ICO.plein);
    bPA.title = "Arrêt automatique avant chaque correction d'exercice";
    bPlay.title = "Lecture / pause (espace)"; bM.title = "Reculer de 10 s"; bP.title = "Avancer de 10 s"; bVit.title = "Vitesse";
    bMus.title = "Musique de fond"; bCC.title = "Sous-titres"; bFS.title = "Plein écran";

    h("div", "astuce", L, "Sur téléphone, touche ⛶ : la vidéo passe en plein écran, en paysage.");
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
    h("h2", "", quiz, "As-tu bien compris ?");
    h("div", "sous", quiz, EP.quiz.length + " questions sur le chapitre. Réponds, puis lis l'explication.");
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
          if (q.voir != null) { var vo = h("button", "voir", d, "▸ Revoir ce passage de la vidéo"); vo.onclick = function () { aller(Math.max(0, q.voir - 1.5)); jouer(); (cadre.scrollIntoView || function () {}).call(cadre, { behavior: "smooth", block: "center" }); }; }
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
    // arrêts « À toi » : la vidéo s'arrête d'elle-même avant chaque correction (option, active par défaut)
    var arrets = EP.vis.filter(function (v) { return v.type === "pause"; }).map(function (v) { return v.et && v.et.stop != null ? v.et.stop : v.t0 + 2.5; });
    var autoPause = true, arretSur = null;
    var bandeau = h("div", "arret", cadre, '<span class="ic">' + ICO.pause + '</span><span><b>À toi.</b> La vidéo attend ta réponse : cherche, puis touche l\'image pour la correction.</span>');
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
    bVit.onclick = function () { vitesse = VIT[(VIT.indexOf(vitesse) + 1) % VIT.length]; audio.playbackRate = vitesse; bVit.innerHTML = '<span class="mono">' + String(vitesse).replace(".", ",") + "×</span>"; };
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
        navigator.mediaSession.metadata = new MediaMetadata({ title: CODE_Q(EP.code) + " · " + EP.titre, artist: "SES · le cours en vidéo", album: "Terminale spécialité" });
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
