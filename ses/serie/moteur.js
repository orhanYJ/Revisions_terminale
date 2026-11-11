/* Vidéos de SES (« Faits & Courbes ») — moteur du lecteur, copie du moteur PC (pc/serie/moteur.js) aux typographies d'un
   magazine de données (IBM Plex Sans Condensed, IBM Plex Sans, Spectral, polices locales dans fonts/).
   Identité (10/11/2026, piste B des maquettes) : la vidéo est un magazine qu'on feuillette sur une table — couverture,
   une double page (ou plus) par partie, page qui tourne entre deux parties, quatrième de couverture ; mode d'emploi au
   début de la section « le magazine », plus bas. Encre sur papier : C.iv est l'encre, C.iv2 le gris, C.sa le corail.
   Type ville (piste C) : la ville miniature, maquette isométrique où un scénario se joue étape par étape.
   Repris du moteur PC : formules, graphiques, exercices, moments « À toi » où la vidéo s'arrête d'elle-même (type pause).
   Ajouts propres à la SES (mode d'emploi en tête de chaque type, plus bas) :
     donnees  graphique de données réelles du site (GRAPHES : barres par année, barres horizontales) qui se construit ;
     chaine   chaîne causale du site (CHAINES) qui se déroule étape par étape, caméra qui suit, boucle possible ;
     chiffres grands chiffres (bandeau « En chiffres ») qui comptent jusqu'à leur valeur, avec leur source ;
     sanim    animation du site (ANIMS, outils/specialites/ses/src/data-anim-*.js) rejouée et pilotée par le temps ;
     auteur   fiche d'auteur (monogramme, nom, repères, idée) comme dans le site ;
     compare  tableau comparatif à deux colonnes, ligne par ligne ;
     plan     plan de copie ou synthèse en colonnes, colonne par colonne ;
     ville    la ville miniature (ménages, entreprises, banque, État, magasin, reste du monde) : un scénario par étapes.
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
  // identité magazine (10/11/2026) : encre sur papier ; iv = encre, iv2 = gris, sa = corail, mo = moutarde foncée (texte)
  var C = { iv: "#16181A", iv2: "#5A5F62", sa: "#E5533F", sa2: "#B9381F", ca: "#0B5563", te: "#0B5563", mo: "#9A6A0E", nuit: "#F5F0E6",
    el: "#0B5563", uv: "#6E5A8A", rouge: "#E5533F", vert: "#2E7D4F", or: "#C98A12", canard: "#0B5563", corail: "#E5533F", moutarde: "#D99A1E",
    encre: "#16181A", carte: "#ECE5D6", carte2: "#E3DBC9", papier: "#F5F0E6", filet: "#CFC6B4" };
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
      if (p <= 0) { c.sp.style.color = ""; c.sp.style.backgroundSize = "0% 58%"; return; }
      c.sp.style.color = f < 1 ? C.sa2 : "";
      c.sp.style.backgroundSize = (100 * E(p)).toFixed(0) + "% 58%";
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
    var cadre = sv("rect", { x: x0, y: y, width: L, height: hb, rx: 14, fill: "none", stroke: "rgba(22,24,26,.35)", "stroke-width": 2, "stroke-dasharray": "8 7" }, g);
    var tot = etiquette(g, x0 + L, y - 26, "croissance : 2,0 % par an", { ancre: "end", fs: 30, c: C.iv, fw: 700 });
    var parts = [[0.4, C.canard, "travail", "0,4 point"], [0.6, C.moutarde, "capital", "0,6 point"], [1.0, C.corail, "PGF : le reste", "1,0 point"]];
    var cum = 0;
    var els = parts.map(function (p, i) {
      var gg = sv("g", {}, g), xa = x0 + cum * u, w = p[0] * u; cum += p[0];
      var r = sv("rect", { x: xa, y: y, width: w, height: hb, rx: i === 0 ? 14 : 0, fill: p[1], opacity: .9 }, gg);
      var t1 = etiquette(gg, xa + w / 2, y + hb / 2 + 11, p[3], { fs: 30, c: p[1] === C.moutarde ? C.encre : "#fff", fw: 700 });
      var t2 = etiquette(gg, xa + w / 2, y + hb + 44, p[2], { fs: 27, c: p[1] === C.moutarde ? C.mo : p[1], fw: 600 });
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
        s.style.color = p > 0 && f < 1 ? "rgb(" + Math.round(229 - 207 * f) + "," + Math.round(83 - 59 * f) + "," + Math.round(63 - 37 * f) + ")" : (p > 0 ? C.iv : C.iv2);
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
        mf.pt.style.boxShadow = "0 0 0 " + (3 + 3 * Math.max(0, Math.sin(t * 3))).toFixed(1) + "px rgba(229,83,63,.25)";
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
        c.c.style.borderColor = actif ? "rgba(229,83,63," + (0.6 + 0.4 * pul) + ")" : "rgba(22,24,26,.16)";
        c.c.style.boxShadow = actif ? "0 0 0 " + (2 + 2 * pul).toFixed(1) + "px rgba(229,83,63,.35)" : "none";
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
      centre.style.boxShadow = "0 0 0 " + (4 + 3 * Math.sin(t * 2)).toFixed(1) + "px rgba(229,83,63,.18)";
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
        sv("line", { x1: ml, x2: ml + pw, y1: Y(y), y2: Y(y), stroke: y === 0 ? C.encre : "rgba(22,24,26,.13)", "stroke-width": y === 0 ? 2 : 1 }, fond);
        sv("text", { x: ml - 12, y: Y(y) + 7, "text-anchor": "end", fill: C.iv2, "font-size": 21 }, fond, (y > 0 ? "+" : "") + frN(y, 0) + u.trim().replace(/^/, " "));
      });
      var pasX = g.pasX || 10;
      xs.forEach(function (an, k) {
        if (an % pasX === 0 || (k === n - 1 && an % pasX > pasX / 2)) sv("text", { x: XB(k) + bw / 2, y: Hz - 12, "text-anchor": "middle", fill: C.iv2, "font-size": 21 }, fond, String(an));
      });
      var bandes = sv("g", {}, s), barres = sv("g", {}, s), haut = sv("g", {}, s);
      var phases = (v.phases || [{ de: xs[0], a: xs[n - 1] }]).map(function (ph_, i) {
        var k0 = xs.indexOf(ph_.de), k1 = xs.indexOf(ph_.a);
        var bd = sv("rect", { x: XB(k0), y: mt - 8, width: (k1 - k0 + 1) * bw, height: ph + 8, fill: "rgba(240,190,79,.26)", rx: 0 }, bandes);
        var xl = XB(k0) + (k1 - k0 + 1) * bw / 2, anc = "middle";
        var demi = String(ph_.l || "").length * 6.5;       // demi-largeur approchée de l'étiquette (23 px, gras)
        if (xl + demi > ml + pw) { xl = ml + pw - 4; anc = "end"; } else if (xl - demi < ml) { xl = ml + 4; anc = "start"; }
        var lb = ph_.l ? sv("text", { x: xl, y: mt + 22, "text-anchor": anc, fill: C.mo, "font-size": 23, "font-weight": 700 }, haut, ph_.l) : null;
        var moy = null, moyT = null;
        if (ph_.moy != null) {
          moy = sv("line", { x1: XB(k0), x2: XB(k1 + 1), y1: Y(ph_.moy), y2: Y(ph_.moy), stroke: C.mo, "stroke-width": 3.2, "stroke-dasharray": "10 6" }, haut);
          var lp = ph_.lp;   // place de l'étiquette [année, valeur], si la place par défaut est prise
          moyT = sv("text", { x: lp ? XB(xs.indexOf(lp[0])) : XB(k1 + 1) + 6, y: lp ? Y(lp[1]) : Y(ph_.moy) - 10, "text-anchor": lp ? "middle" : XB(k1 + 1) > ml + pw - 120 ? "end" : "start", fill: C.mo, "font-size": 22, "font-weight": 700, "paint-order": "stroke", stroke: C.papier, "stroke-width": 6 }, haut, "moyenne " + frN(ph_.moy, 1) + " %/an");
        }
        return { k0: k0, k1: k1, bd: bd, lb: lb, moy: moy, moyT: moyT, dur: ph_.dur || Math.min(4, .8 + (k1 - k0 + 1) * .1), i: i };
      });
      var rects = ys.map(function (y, k) { return sv("rect", { x: (XB(k) + bw * .14).toFixed(1), width: (bw * .72).toFixed(1), y: Y(0), height: 0, rx: 2, fill: y < 0 ? C.corail : C.canard }, barres); });
      var notes = (g.notes || []).map(function (nt) {
        var k = xs.indexOf(nt.x), yy = nt.y < 0 ? Math.min(Y(nt.y) + 30, mt + ph - 6) : Y(nt.y) - 12, fin_ = k > n - 6;
        return { k: k, t: sv("text", { x: fin_ ? XB(k) - 6 : XB(k) + bw / 2, y: yy, "text-anchor": fin_ ? "end" : "middle", fill: nt.y < 0 ? C.sa2 : C.iv, "font-size": 21, "font-weight": 700, "paint-order": "stroke", stroke: C.papier, "stroke-width": 6 }, haut, nt.t + " : " + (nt.y > 0 ? "+" : "") + frN(nt.y, 1) + " %") };
      });
      var bulle = sv("text", { "text-anchor": "middle", fill: C.iv, "font-size": 24, "font-weight": 700, "paint-order": "stroke", stroke: C.papier, "stroke-width": 7 }, haut);
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
      var z = sv("line", { x1: X(0), x2: X(0), y1: y00 - 6, y2: y00 + nc * rh + 6, stroke: C.encre, "stroke-width": 2 }, s);
      var lignes = cats.map(function (c, k) {
        var yc = y00 + k * rh + rh / 2, gg = sv("g", {}, s);
        var lt = h("div", "dn-cat", zone, esc(c)); lt.style.top = (yc - 20) + "px"; lt.style.width = lab + "px";
        var r = sv("rect", { x: X(0), y: yc - bh / 2, width: 0, height: bh, rx: 6, fill: (v.couleurs || [])[k] ? C[v.couleurs[k]] || v.couleurs[k] : (vals[k] < 0 ? C.corail : C.canard) }, gg);
        var tv = sv("text", { y: yc + 11, fill: vals[k] < 0 ? C.sa2 : C.iv, "font-size": 32, "font-weight": 700, "text-anchor": "start" }, gg);
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
      var policesOK = policesPretes && (!document.fonts || document.fonts.status === "loaded");
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
        l.d.style.borderColor = t >= tk ? "rgba(22,24,26,.22)" : "transparent";
      });
    };
  };

  // plan : un plan de copie (ou une synthèse) en colonnes ; titre en tête, parties=[dict(t="I. …", items=[…]), …] ;
  //   la colonne k apparaît au repère {id.k}, ses lignes l'une après l'autre ; x, y, w.
  TYPES.plan = function (o, v) {
    var e = o.el; e.classList.add("v-plan"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 70) + "px"; e.style.top = (v.y != null ? v.y : 90) + "px"; e.style.width = (v.w || 1140) + "px";
    var ti = v.titre ? h("div", "pl-ti", e, esc(v.titre)) : null;
    var gr = h("div", "pl-gr n" + v.parties.length, e), COUL = ["#0B5563", "#C2402B", "#9A6A0E", "#2E7D4F"];
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

  /* ville : la ville miniature (identité C, en illustration ponctuelle) — maquette isométrique d'une économie où un
     scénario se joue étape par étape. dict(type="ville", titre="…", scenario="productivite", …) ou un scénario écrit dans le
     script : dict(type="ville", titre="…", base=[…], flux=[…], etapes=[…]).
       Bâtiments (noms fixes, places fixes sur la maquette) : usine (l'entreprise), magasin, maisons (les ménages), banque,
         etat (l'État), monde (le reste du monde : un port), usine2 (une nouvelle entreprise). noms=dict(usine="Kodak", …)
         remplace les plaques (défaut : Entreprise, Magasin, Ménages, Banque, État, Reste du monde, Nouvelle entreprise).
       base : bâtiments déjà là au début (défaut du scénario ; sinon usine, magasin, maisons, banque) ; ils sortent de terre.
       flux : flux présents dès le début, liste de dict(de="usine", a="magasin", k="biens"|"revenus"|"achats"|"emplois",
         l="salaires" (étiquette sur le trajet, facultative), n=1 (cadence ; n=0 arrête le flux)). « biens » : caisses,
         « revenus » : pièces, « achats » : passants des ménages vers le magasin, « emplois » : travailleurs qui changent d'entreprise.
       etapes : l'étape k (de 1 à N) se joue au repère {id.k} (à défaut, toutes les 4,5 s) ; chaque étape est un dict, tous
         les champs sont facultatifs et l'état se cumule :
           montre=["usine2"]     bâtiments qui sortent de terre ;
           ferme=["usine"]       bâtiments qui ferment (grisés, panneau « Fermé », leurs flux s'arrêtent) ;
           grandit=["usine"]     l'entreprise s'agrandit (une aile sort de terre à côté) ;
           flux=[dict(…)]        flux qui commencent, changent de cadence (même de, a, k) ou s'arrêtent (n=0) ;
           etiquette=dict(h="Progrès technique", s="une nouvelle machine entre dans l'usine", sur="usine") : carte numérotée
                                 reliée au bâtiment, qui se range en pastille à l'étape suivante ;
           machine="usine"       un camion livre une machine (un engrenage reste au-dessus du bâtiment) ;
           compteur=dict(sur="usine", l="10 salariés, même équipement", de=100, a=125, u="objets par jour",
                         note="exemple chiffré inventé") : panneau qui compte, le temps de l'étape ;
           prix=dict(sur="magasin", t="PRIX ↓", c="vert") : l'étiquette de prix bascule ;
           foule=2.5             cadence des achats des ménages (demande) ;
           panneau=dict(t="PIB DE LA FRANCE EN VOLUME", n="×8,6", s="de 1950 à 2025 · Insee") : panneau planté derrière ;
           cam="usine" | "tout"  cadrage (défaut : le bâtiment de l'étiquette, sinon toute la maquette).
       Scénarios prêts à l'emploi (scenario=…) : « productivite » (des gains de productivité à la croissance, 6 étapes) et
       « destruction » (la destruction créatrice, 5 étapes) ; leurs étapes, flux et noms peuvent être remplacés champ par champ.
       titre, kicker (cartel en haut à gauche), legende=False (sans la légende biens / revenus). Rendu fonction pure du temps. */
  var VILLE_SCENARIOS = {
    productivite: {
      titre: "Des gains de productivité à la croissance",
      base: ["usine", "magasin", "maisons", "banque"],
      flux: [{ de: "usine", a: "magasin", k: "biens" }, { de: "usine", a: "maisons", k: "revenus", l: "salaires" }, { de: "maisons", a: "magasin", k: "achats" }],
      etapes: [
        { machine: "usine", etiquette: { h: "Progrès technique", s: "une nouvelle machine entre dans l'usine", sur: "usine" } },
        { compteur: { sur: "usine", l: "10 salariés, même équipement", de: 100, a: 125, u: "objets par jour", note: "exemple chiffré inventé" },
          flux: [{ de: "usine", a: "magasin", k: "biens", n: 1.5 }], etiquette: { h: "On produit plus", s: "avec autant de travail et de capital", sur: "usine" } },
        { etiquette: { h: "Coût unitaire ↓", s: "chaque objet coûte moins cher à produire", sur: "usine" } },
        { prix: { sur: "magasin", t: "PRIX ↓", c: "vert" }, flux: [{ de: "usine", a: "maisons", k: "revenus", l: "salaires", n: 1.6 }, { de: "usine", a: "banque", k: "revenus", l: "profits" }],
          etiquette: { h: "Partage des gains", s: "prix ↓ · salaires ↑ · profits ↑", sur: "magasin" } },
        { foule: 2.6, etiquette: { h: "La demande augmente", s: "les ménages achètent davantage", sur: "maisons" } },
        { grandit: ["usine"], flux: [{ de: "banque", a: "usine", k: "revenus", l: "investissement", n: 1.4 }, { de: "usine", a: "magasin", k: "biens", n: 2.1 }],
          etiquette: { h: "L'entreprise s'agrandit", s: "elle investit : la production augmente", sur: "usine" }, cam: "tout" }
      ]
    },
    destruction: {
      titre: "La destruction créatrice",
      noms: { usine: "Ancienne activité", usine2: "Innovation" },
      base: ["usine", "magasin", "maisons", "banque"],
      flux: [{ de: "usine", a: "magasin", k: "biens" }, { de: "usine", a: "maisons", k: "revenus", l: "salaires" }, { de: "maisons", a: "magasin", k: "achats" }],
      etapes: [
        { montre: ["usine2"], flux: [{ de: "banque", a: "usine2", k: "revenus", l: "crédit" }],
          etiquette: { h: "Une innovation", s: "un entrepreneur lance un produit nouveau", sur: "usine2" } },
        { flux: [{ de: "usine2", a: "magasin", k: "biens", n: 1.3 }, { de: "usine", a: "magasin", k: "biens", n: .35 }, { de: "banque", a: "usine2", k: "revenus", n: 0 }], foule: 1.8,
          etiquette: { h: "La demande se déplace", s: "les clients choisissent le produit nouveau", sur: "magasin" } },
        { ferme: ["usine"], etiquette: { h: "Destruction", s: "l'ancienne activité perd ses clients et ferme", sur: "usine" } },
        { flux: [{ de: "usine", a: "usine2", k: "emplois", l: "reconversions" }],
          etiquette: { h: "Les emplois se déplacent", s: "licenciements, reconversions : un coût social", sur: "usine2" }, cam: "tout" },
        { grandit: ["usine2"], flux: [{ de: "usine2", a: "maisons", k: "revenus", l: "salaires", n: 1.4 }, { de: "usine2", a: "magasin", k: "biens", n: 2 }],
          etiquette: { h: "Création", s: "activités et emplois nouveaux : la croissance", sur: "usine2" }, cam: "tout" }
      ]
    }
  };
  TYPES.ville = function (o, v) {
    var e = o.el; e.classList.add("v-ville"); o.entree = "aucune";
    var cv = h("canvas", "", e); cv.width = 1920; cv.height = 1080;
    var g = cv.getContext("2d"), VW = 1920, VH = 1080;
    if (document.fonts && document.fonts.load) o.attente = Promise.all([document.fonts.load('700 30px "Space Grotesk"'), document.fonts.load('500 30px "Space Grotesk"')]).catch(function () {});
    var SCN = VILLE_SCENARIOS[v.scenario] || {};
    var K = { fond: "#EAE3D4", sol: "#DCE6D2", bord: "#BFAF8F", bordF: "#A3936F", route: "#C3CBCA", trait: "#F7F4EC", canard: "#0B5563", canardC: "#5BB8C4",
      corail: "#E5533F", moutarde: "#E9B03F", piece: "#F2C14E", ivoire: "#F8F5EE", encre: "#14232B", gris: "#56636B", arbre: "#7FA66B", arbreF: "#5F8A52", vert: "#2E7D4F" };
    var NOMS = { usine: "Entreprise", magasin: "Magasin", maisons: "Ménages", banque: "Banque", etat: "État", monde: "Reste du monde", usine2: "Nouvelle entreprise" };
    [SCN.noms, v.noms].forEach(function (n) { for (var k in n || {}) NOMS[k] = n[k]; });
    var BAT = {
      usine: { i: 2, j: 1.5, w: 2.6, d: 2.5, h: 64, porte: [4.75, 2.75], r: "i", ext: { i: .2, j: 1.7, w: 1.6, d: 2.2 } },
      magasin: { i: 7, j: 1.6, w: 2.5, d: 2.4, h: 56, porte: [7.9, 4.3], r: "j" },
      monde: { i: 10.1, j: .7, w: 1.8, d: 3.6, h: 30, porte: [10.7, 4.6], r: "j" },
      maisons: { i: 1, j: 7.3, w: 3.3, d: 3.6, h: 34, porte: [4.5, 8.3], r: "i" },
      banque: { i: 7.6, j: 7.4, w: 2.2, d: 2.2, h: 72, porte: [8.4, 7.1], r: "j" },
      etat: { i: 10.3, j: 7.4, w: 1.6, d: 2.2, h: 80, porte: [11, 7.1], r: "j" },
      usine2: { i: 7.4, j: 10.0, w: 2.4, d: 1.7, h: 58, porte: [7.1, 10.8], r: "i", ext: { i: 10.2, j: 10.1, w: 1.5, d: 1.6 } }
    };
    function teinte(hex, k) {
      var n = parseInt(hex.slice(1), 16), r = n >> 16, gg = (n >> 8) & 255, b = n & 255, m = k > 0 ? 255 : 0, a = Math.abs(k);
      r = Math.round(r + (m - r) * a); gg = Math.round(gg + (m - gg) * a); b = Math.round(b + (m - b) * a);
      return "#" + [r, gg, b].map(function (x) { return x.toString(16).padStart(2, "0"); }).join("");
    }
    function gris(hex) { var n = parseInt(hex.slice(1), 16), y = Math.round(.3 * (n >> 16) + .59 * ((n >> 8) & 255) + .11 * (n & 255)); y = Math.round(y * .55 + 150 * .45); return "#" + [y, y, y].map(function (x) { return x.toString(16).padStart(2, "0"); }).join(""); }
    var IP = function (i, j, z) { return [(i - j) * 64, (i + j) * 32 - (z || 0)]; };
    function F(px, w) { g.font = w + " " + px + 'px "Space Grotesk", "IBM Plex Sans", sans-serif'; }
    function rr(x, y, w, hh, r) { g.beginPath(); if (g.roundRect) g.roundRect(x, y, w, hh, r); else g.rect(x, y, w, hh); }
    function poly(pts, col, trait) { g.beginPath(); pts.forEach(function (p, k) { if (k) g.lineTo(p[0], p[1]); else g.moveTo(p[0], p[1]); }); g.closePath(); g.fillStyle = col; g.fill(); if (trait) { g.strokeStyle = trait; g.lineWidth = 1.2; g.stroke(); } }
    var TR = "rgba(20,35,43,.25)";
    function boite(i, j, w, d, hh, z0, col, trait) {
      if (hh <= 0) return; var z1 = z0 + hh; trait = trait || TR;
      poly([IP(i + w, j, z0), IP(i + w, j + d, z0), IP(i + w, j + d, z1), IP(i + w, j, z1)], teinte(col, -.18), trait);
      poly([IP(i, j + d, z0), IP(i + w, j + d, z0), IP(i + w, j + d, z1), IP(i, j + d, z1)], teinte(col, -.32), trait);
      poly([IP(i, j, z1), IP(i + w, j, z1), IP(i + w, j + d, z1), IP(i, j + d, z1)], teinte(col, .12), trait);
    }
    function faceD(i1, j, u0, u1, v0, v1, z0, col) { poly([IP(i1, j + u0, z0 + v0), IP(i1, j + u1, z0 + v0), IP(i1, j + u1, z0 + v1), IP(i1, j + u0, z0 + v1)], col); }
    function faceG(i, j1, u0, u1, v0, v1, z0, col) { poly([IP(i + u0, j1, z0 + v0), IP(i + u1, j1, z0 + v0), IP(i + u1, j1, z0 + v1), IP(i + u0, j1, z0 + v1)], col); }
    function ombreSol(i, j, w, d, a) { poly([IP(i + .15, j + .15), IP(i + w + .35, j + .15), IP(i + w + .35, j + d + .35), IP(i + .15, j + d + .35)], "rgba(40,50,30," + a + ")"); }
    function ease(x) { return EB(x); }

    // ---------- l'état du scénario, calculé une fois (tout est daté) ----------
    var base = v.base || SCN.base || ["usine", "magasin", "maisons", "banque"];
    var etapes = v.etapes || SCN.etapes || [];
    var tk = etapes.map(function (_, k) { return et(v, String(k + 1), 1.8 + k * 4.5); });
    var T0 = v.t0, TF = v.t1 + 30;
    var bat = {};       // nom -> { t: sortie de terre, ferme: instant, grand: instant }
    base.forEach(function (n, k) { bat[n] = { t: T0 + .35 + k * .12 }; });
    var flux = [];      // { de, a, k, l, n, t0, t1 }
    function poser(f, t) {
      var avant = null;
      flux.forEach(function (x) { if (x.de === f.de && x.a === f.a && x.k === (f.k || "biens") && x.t1 > t) { x.t1 = t; avant = x; } });
      if (f.n === 0) return;
      var nf = { de: f.de, a: f.a, k: f.k || "biens", l: f.l != null ? f.l : avant ? avant.l : "", n: f.n || 1, t0: t, t1: TF, suite: !!avant, avant: avant };
      if (avant) avant.apres = nf;
      flux.push(nf);
    }
    (v.flux || SCN.flux || []).forEach(function (f) { poser(f, T0 + 1.3); });
    var cartes = [], machines = [], compteurs = [], prix = [], panneaux = [], foule = [[T0, 1]], cams = [];
    etapes.forEach(function (s, k) {
      var T = tk[k], suiv = k + 1 < tk.length ? tk[k + 1] : v.t1;
      (s.montre || []).forEach(function (n) { if (!bat[n]) bat[n] = { t: T }; });
      (s.ferme || []).forEach(function (n) { if (bat[n]) { bat[n].ferme = T; flux.forEach(function (x) { if ((x.de === n || x.a === n) && x.k !== "emplois" && x.t1 > T) x.t1 = T; }); } });
      (s.grandit || []).forEach(function (n) { if (bat[n]) bat[n].grand = T + .4; });
      (s.flux || []).forEach(function (f) { poser(f, T + .3); });
      if (s.etiquette) cartes.push({ n: cartes.length + 1, h: s.etiquette.h || "", s: s.etiquette.s || "", sur: s.etiquette.sur || "usine", t: T, k: k });
      if (s.machine) machines.push({ sur: s.machine, t: T });
      if (s.compteur) compteurs.push({ c: s.compteur, t: T + .1, fin: suiv });
      if (s.prix) prix.push({ c: s.prix, t: T + .2 });
      if (s.panneau) panneaux.push({ c: s.panneau, t: T });
      if (s.foule != null) foule.push([T, s.foule]);
      cams.push([T, s.cam || (s.etiquette && s.etiquette.sur) || "tout"]);
    });
    var nCartes = cartes.length;
    // ---------- trajets sur les routes ----------
    function trajet(de, a, dec) {
      var A = BAT[de], B = BAT[a], L = 6 + dec, pa = A.porte, pb = B.porte;
      var ra = A.r === "i" ? [L, pa[1]] : [pa[0], L], rb = B.r === "i" ? [L, pb[1]] : [pb[0], L];
      var pts = [pa, ra]; if (A.r !== B.r) pts.push([L, L]); pts.push(rb, pb);
      var Ls = [0]; for (var k = 1; k < pts.length; k++) Ls.push(Ls[k - 1] + Math.hypot(pts[k][0] - pts[k - 1][0], pts[k][1] - pts[k - 1][1]));
      return { pts: pts, L: Ls, tot: Ls[Ls.length - 1], at: function (p) {
        var s = cl(p, 0, 1) * this.tot, k = 1; while (k < this.L.length - 1 && this.L[k] < s) k++;
        var q = (s - this.L[k - 1]) / ((this.L[k] - this.L[k - 1]) || 1);
        return [this.pts[k - 1][0] + (this.pts[k][0] - this.pts[k - 1][0]) * q, this.pts[k - 1][1] + (this.pts[k][1] - this.pts[k - 1][1]) * q]; } };
    }
    var DEC = { biens: -.24, revenus: .24, achats: .02, emplois: -.06 }, PER = { biens: .72, revenus: .8, achats: .9, emplois: .55 }, VIT = { biens: 2.4, revenus: 3.2, achats: 1.7, emplois: 1.6 };
    flux.forEach(function (f, i) {
      f.ch = trajet(f.de, f.a, DEC[f.k] || 0); f.duree = f.ch.tot / (VIT[f.k] || 2.4);
      var per = (PER[f.k] || .8) / f.n, out = [], x = f.t0 - (f.suite ? per * alea(i + 3) : 0), m = 0;
      var fin = f.k === "emplois" ? Math.min(f.t1, f.t0 + 2.4) : f.t1;
      while (x < fin && m < 4000) { out.push(x); m++; x += f.k === "achats" ? per / cadenceFoule(x) : per; }
      f.departs = out;
    });
    function cadenceFoule(t) { var c = 1; foule.forEach(function (x) { if (t >= x[0]) c = x[1]; }); return c; }
    // ---------- caméra : [t, cx, cy, échelle] ----------
    function cible(n) {
      if (n === "tout" || !BAT[n]) return [0, 330, .9];
      var b = BAT[n], c = IP(b.i + b.w / 2, b.j + b.d / 2, 40); return [c[0], c[1] + 30, 1.28];
    }
    var CAMV = [[T0, 0, 380, .8], [T0 + 1.6, 0, 340, .9]];
    cams.forEach(function (c, k) {
      var cb = cible(c[1]), prev = CAMV[CAMV.length - 1];
      CAMV.push([Math.max(prev[0] + .1, c[0] - .2), prev[1], prev[2], prev[3]]);
      CAMV.push([Math.max(prev[0] + .9, c[0] + .8), cb[0], cb[1], cb[2]]);
    });
    function camera(t) {
      var i = 0; while (i < CAMV.length - 2 && t > CAMV[i + 1][0]) i++;
      var A = CAMV[i], B = CAMV[Math.min(i + 1, CAMV.length - 1)], p = EIO(P(t, A[0], Math.max(.001, B[0] - A[0])));
      return [A[1] + (B[1] - A[1]) * p, A[2] + (B[2] - A[2]) * p, Math.exp(Math.log(A[3]) + (Math.log(B[3]) - Math.log(A[3])) * p)];
    }
    var CX = 0, CY = 0, CS = 1;
    function ecran(p) { return [VW / 2 + (p[0] - CX) * CS, VH / 2 + (p[1] - CY) * CS]; }

    // ---------- objets ----------
    function pousseDe(n, t) { var b = bat[n]; return b ? ease(P(t, b.t, .5)) : 0; }
    function col(n, c) { var b = bat[n]; return b && b.ferme != null ? gris(c) : c; }
    function fumee(t, i, j, z, per, a) {
      var p = IP(i, j, z);
      for (var k = 0; k < 9; k++) {
        var age = (((t + k * per) % (per * 9)) + per * 9) % (per * 9) / (per * 9), r = 8 + age * 26;
        g.fillStyle = "rgba(250,248,242," + (.85 * (1 - age) * a).toFixed(3) + ")";
        g.beginPath(); g.arc(p[0] - age * 40 + Math.sin(k * 2.1 + t) * 4, p[1] - age * 150, r, 0, 7); g.fill();
      }
    }
    function toitScie(i, j, w, d, hh, n, c, p) {
      for (var k = 0; k < n; k++) {
        var ja = j + k * d / n, jb = ja + d / n, tz = 22 * p;
        poly([IP(i, ja, hh), IP(i + w, ja, hh), IP(i + w, jb, hh + tz), IP(i, jb, hh + tz)], teinte(c, .2));
        poly([IP(i, jb, hh), IP(i + w, jb, hh), IP(i + w, jb, hh + tz), IP(i, jb, hh + tz)], teinte(K.canardC, .15));
        poly([IP(i + w, ja, hh), IP(i + w, jb, hh), IP(i + w, jb, hh + tz)], teinte(c, -.12));
      }
    }
    function usine(n, t, p) {
      var b = BAT[n], i = b.i, j = b.j, w = b.w, d = b.d, hh = b.h * p, c = col(n, n === "usine2" ? K.vert : K.canard), ferme = bat[n].ferme != null && t >= bat[n].ferme;
      if (!ferme) c = n === "usine2" ? K.vert : K.canard;
      ombreSol(i, j, w, d, .16 * p); boite(i, j, w, d, hh, 0, c);
      if (p < .2) return;
      for (var k = 0; k < Math.floor(w / .62); k++) faceG(i, j + d, .2 + k * .6, .55 + k * .6, 22 * p, 44 * p, 0, ferme ? "#9AA1A3" : teinte(K.canardC, .3));
      faceD(i + w, j, .6, 1.6, 0, 34 * p, 0, teinte(c, -.45));
      if (n === "usine2") {      // l'entreprise nouvelle : toit plat, panneaux solaires, antenne
        for (var q = 0; q < 3; q++) poly([IP(i + .3 + q * .7, j + .3, hh + 2), IP(i + .8 + q * .7, j + .3, hh + 2), IP(i + .8 + q * .7, j + d - .3, hh + 12), IP(i + .3 + q * .7, j + d - .3, hh + 12)], "#24435A", "rgba(255,255,255,.35)");
        var an = IP(i + w - .3, j + .3, hh); g.strokeStyle = K.encre; g.lineWidth = 3; g.beginPath(); g.moveTo(an[0], an[1]); g.lineTo(an[0], an[1] - 44 * p); g.stroke();
        g.fillStyle = K.corail; g.beginPath(); g.arc(an[0], an[1] - 44 * p, 6, 0, 7); g.fill();
      } else {
        toitScie(i, j, w, d, hh, 3, c, p);
        boite(i + .3, j + .2, .45, .45, hh + 70 * p, 0, ferme ? "#7D8487" : "#3B4C54");
        if (!ferme) fumee(t, i + .52, j + .42, hh + 70 * p + 6, .34, 1);
      }
      if (ferme) {            // panneau « Fermé » cloué sur la façade
        var f = IP(i + w * .45, j + d, 30), a = E(P(t, bat[n].ferme, .5));
        g.save(); g.translate(f[0], f[1]); g.rotate(-.12); g.globalAlpha = a; g.fillStyle = "#7A5B3A"; g.fillRect(-62, -20, 124, 40);
        F(24, 700); g.fillStyle = K.ivoire; g.textAlign = "center"; g.fillText("FERMÉ", 0, 9); g.textAlign = "left"; g.restore();
      }
    }
    function aile(n, t) {
      var b = BAT[n], x = b.ext, gt = bat[n] && bat[n].grand; if (gt == null) return;
      var p = ease(P(t, gt, .7)); if (p <= 0) return;
      var c = teinte(n === "usine2" ? K.vert : K.canard, .12), hh = 52 * p;
      ombreSol(x.i, x.j, x.w, x.d, .15 * cl(p, 0, 1)); boite(x.i, x.j, x.w, x.d, hh, 0, c);
      for (var k = 0; k < 2; k++) faceG(x.i, x.j + x.d, .2 + k * .7, .6 + k * .7, 18 * p, 36 * p, 0, teinte(K.canardC, .3));
      if (n !== "usine2") toitScie(x.i, x.j, x.w, x.d, hh, 2, c, p);
    }
    function magasin(t, p) {
      var b = BAT.magasin, i = b.i, j = b.j, w = b.w, d = b.d, hh = b.h * p;
      ombreSol(i, j, w, d, .16 * p); boite(i, j, w, d, hh, 0, K.corail);
      if (p < .2) return;
      faceG(i, j + d, .3, 1.5, 0, 30 * p, 0, teinte(K.canardC, .45)); faceG(i, j + d, 1.8, 2.25, 0, 34 * p, 0, "#7A2416");
      for (var k = 0; k < 6; k++) { var u0 = .1 + k * .38, u1 = u0 + .38;
        poly([IP(i + u0, j + d, 40 * p), IP(i + u1, j + d, 40 * p), IP(i + u1, j + d + .45, 30 * p), IP(i + u0, j + d + .45, 30 * p)], k % 2 ? K.ivoire : K.corail, "rgba(20,35,43,.2)"); }
    }
    function banque(t, p) {
      var b = BAT.banque, i = b.i, j = b.j, w = b.w, d = b.d, hh = 62 * p;
      ombreSol(i, j, w, d, .16 * p); boite(i, j - .1, w, d + .1, 10 * p, 0, "#E7DCC2");
      boite(i + .15, j, w - .3, d - .15, hh, 10 * p, K.moutarde);
      if (p < .2) return;
      for (var k = 0; k < 4; k++) faceG(i + .15, j + d - .15, .25 + k * .45, .4 + k * .45, 4, hh - 6, 10 * p, K.ivoire);
      var z = hh + 10 * p;
      poly([IP(i + .15, j + d - .15, z), IP(i + w - .15, j + d - .15, z), IP(i + w / 2, j + d - .15, z + 26)], teinte(K.moutarde, .25), TR);
    }
    function etat(t, p) {
      var b = BAT.etat, i = b.i, j = b.j, w = b.w, d = b.d, hh = 58 * p;
      ombreSol(i, j, w, d, .16 * p); boite(i, j - .1, w, d + .1, 12 * p, 0, "#E7DCC2");
      boite(i + .1, j, w - .2, d - .1, hh, 12 * p, "#D9D2C3");
      if (p < .2) return;
      for (var k = 0; k < 4; k++) faceG(i + .1, j + d - .1, .18 + k * .36, .3 + k * .36, 4, hh - 4, 12 * p, K.ivoire);
      var z = hh + 12 * p, c = IP(i + w / 2, j + d / 2, z);
      g.fillStyle = teinte("#8FA3AD", -.1); g.beginPath(); g.ellipse(c[0], c[1], 34, 17, 0, Math.PI, 0); g.fill();
      g.fillStyle = "#8FA3AD"; g.beginPath(); g.arc(c[0], c[1] - 2, 34, Math.PI, 0); g.fill();
      g.strokeStyle = K.encre; g.lineWidth = 3; g.beginPath(); g.moveTo(c[0], c[1] - 36); g.lineTo(c[0], c[1] - 86 * p); g.stroke();
      var fy = c[1] - 86 * p; ["#2F4E9A", "#F8F5EE", "#D5373F"].forEach(function (cc, k) { g.fillStyle = cc; g.fillRect(c[0] + 2 + k * 12, fy, 12, 22); });
    }
    function monde(t, p) {       // le reste du monde : un quai, un porte-conteneurs
      var b = BAT.monde, i = b.i, j = b.j, w = b.w, d = b.d;
      poly([IP(i, j, 0), IP(i + w, j, 0), IP(i + w, j + d, 0), IP(i, j + d, 0)], teinte("#6FA8C8", .1 * p));
      for (var k = 0; k < 4; k++) { var y = j + .5 + k * .8, q = Math.sin(t * 2 + k) * .08;
        g.strokeStyle = "rgba(255,255,255,.55)"; g.lineWidth = 2; var a1 = IP(i + .2 + q, y), a2 = IP(i + .7 + q, y); g.beginPath(); g.moveTo(a1[0], a1[1]); g.lineTo(a2[0], a2[1]); g.stroke(); }
      if (p < .2) return;
      var oy = Math.sin(t * 1.4) * 2;
      g.save(); g.translate(0, oy);
      boite(i + .45, j + .6, .9, 2.6, 16 * p, 0, "#34444C");
      var cs = [K.corail, K.moutarde, K.canardC, K.corail, K.vert];
      for (var q2 = 0; q2 < 5; q2++) boite(i + .55, j + .75 + q2 * .45, .7, .38, 12 * p, 16 * p, cs[q2]);
      boite(i + .5, j + 2.75, .8, .4, 30 * p, 16 * p, K.ivoire);
      g.restore();
    }
    function maison(i, j, p, toit) {
      var w = 1.3, d = 1.3, hh = 34 * p; ombreSol(i, j, w, d, .14 * p);
      boite(i, j, w, d, hh, 0, K.ivoire); if (p < .3) return;
      faceG(i, j + d, .2, .5, 8, 22, 0, teinte(K.canardC, .4)); faceG(i, j + d, .75, 1.05, 0, 22, 0, teinte(toit, -.2));
      var tz = 26 * p, jm = j + d / 2;
      poly([IP(i, j, hh), IP(i + w, j, hh), IP(i + w, jm, hh + tz), IP(i, jm, hh + tz)], teinte(toit, .15), "rgba(20,35,43,.2)");
      poly([IP(i + w, j, hh), IP(i + w, j + d, hh), IP(i + w, jm, hh + tz)], teinte(K.ivoire, -.1), "rgba(20,35,43,.2)");
      poly([IP(i, jm, hh + tz), IP(i + w, jm, hh + tz), IP(i + w, j + d, hh), IP(i, j + d, hh)], toit, "rgba(20,35,43,.2)");
    }
    function arbre(i, j, p) {
      if (p <= 0) return; var q = IP(i, j);
      g.fillStyle = "rgba(40,50,30,.15)"; g.beginPath(); g.ellipse(q[0] + 6, q[1] + 3, 22 * p, 10 * p, 0, 0, 7); g.fill();
      g.strokeStyle = "#7A5B3A"; g.lineWidth = 5; g.beginPath(); g.moveTo(q[0], q[1]); g.lineTo(q[0], q[1] - 22 * p); g.stroke();
      g.fillStyle = K.arbreF; g.beginPath(); g.arc(q[0] + 4, q[1] - 36 * p, 22 * p, 0, 7); g.fill();
      g.fillStyle = K.arbre; g.beginPath(); g.arc(q[0] - 3, q[1] - 40 * p, 19 * p, 0, 7); g.fill();
    }
    function caisse(i, j) { boite(i - .17, j - .17, .34, .34, 18, 0, K.canardC, "rgba(7,62,73,.5)"); }
    function piece(i, j, z, r) { var q = IP(i, j, z);
      g.fillStyle = "#B98213"; g.beginPath(); g.ellipse(q[0], q[1] + 2, r, r * .75, 0, 0, 7); g.fill();
      g.fillStyle = K.piece; g.beginPath(); g.ellipse(q[0], q[1], r, r * .75, 0, 0, 7); g.fill(); g.strokeStyle = "#B98213"; g.lineWidth = 1.5; g.stroke(); }
    function passant(i, j, c, t, k, casque) { var q = IP(i, j), b = Math.abs(Math.sin(t * 9 + k)) * 3;
      g.fillStyle = "rgba(40,50,30,.18)"; g.beginPath(); g.ellipse(q[0], q[1], 8, 4, 0, 0, 7); g.fill();
      g.fillStyle = c; rr(q[0] - 6, q[1] - 24 - b, 12, 18, 6); g.fill(); g.fillStyle = "#E8C9A8"; g.beginPath(); g.arc(q[0], q[1] - 30 - b, 5.5, 0, 7); g.fill();
      if (casque) { g.fillStyle = K.moutarde; g.beginPath(); g.arc(q[0], q[1] - 32 - b, 6.5, Math.PI, 0); g.fill(); } }
    function engrenage(x, y, r, a, c) {
      g.save(); g.translate(x, y); g.rotate(a); g.fillStyle = c; g.beginPath();
      for (var k = 0; k < 16; k++) { var b = k * Math.PI / 8, r2 = k % 2 ? r * .72 : r; g.lineTo(Math.cos(b) * r2, Math.sin(b) * r2); g.lineTo(Math.cos(b + Math.PI / 8 - .08) * r2, Math.sin(b + Math.PI / 8 - .08) * r2); }
      g.closePath(); g.fill(); g.fillStyle = K.ivoire; g.beginPath(); g.arc(0, 0, r * .3, 0, 7); g.fill(); g.restore();
    }
    function camion(i, j) { boite(i - .55, j - .25, .8, .5, 30, 4, K.ivoire); boite(i + .25, j - .25, .35, .5, 22, 4, K.corail); var q = IP(i - .15, j, 50); engrenage(q[0], q[1], 16, 0, K.encre); }
    var ARBRES = [[.6, 5.3], [.5, 9.6], [5.0, .4], [10.8, .2], [11.5, 5.0], [9.6, 5.0], [11.4, 6.8], [2.4, 5.0], [.6, 11.4], [4.9, 11.4], [6.9, 11.5], [11.3, 11.6], [5, 6.9]];
    var MAISONS = [[1.0, 7.3, "#34444C"], [3.0, 7.3, K.corail], [1.0, 9.6, K.corail], [3.0, 9.6, "#34444C"]];
    var TEINTES = [K.corail, K.canard, K.moutarde, "#6E5A8A", K.vert, "#C0632E"];
    function dans(i, j) { for (var n in bat) { var b = BAT[n]; if (!b) continue; if (i > b.i - .5 && i < b.i + b.w + .5 && j > b.j - .5 && j < b.j + b.d + .5) return true; if (b.ext && bat[n].grand != null && i > b.ext.i - .4 && i < b.ext.i + b.ext.w + .4 && j > b.ext.j - .4 && j < b.ext.j + b.ext.d + .4) return true; } return false; }

    // ---------- la maquette ----------
    function ville(t) {
      var ps = E(P(t, T0, .6)), ep = 46;
      g.save(); g.translate(0, (1 - ps) * 160); g.globalAlpha = cl(ps * 1.4, 0, 1);
      poly([IP(.6, .9, -ep - 8), IP(12.9, .9, -ep - 8), IP(12.9, 13.1, -ep - 8), IP(.6, 13.1, -ep - 8)], "rgba(80,65,40,.16)");
      poly([IP(12, 0), IP(12, 12), IP(12, 12, -ep), IP(12, 0, -ep)], K.bord); poly([IP(0, 12), IP(12, 12), IP(12, 12, -ep), IP(0, 12, -ep)], K.bordF);
      poly([IP(0, 0), IP(12, 0), IP(12, 12), IP(0, 12)], K.sol);
      var pr = E(P(t, T0 + .35, .55));
      poly([IP(5.5, 0), IP(6.5, 0), IP(6.5, 12 * pr), IP(5.5, 12 * pr)], K.route); poly([IP(0, 5.5), IP(12 * pr, 5.5), IP(12 * pr, 6.5), IP(0, 6.5)], K.route);
      for (var k = 0; k < 12; k++) { if (k + .5 > 12 * pr || Math.abs(k + .5 - 6) < .7) continue; var q = k + .2;
        poly([IP(5.97, q), IP(6.03, q), IP(6.03, q + .5), IP(5.97, q + .5)], K.trait); poly([IP(q, 5.97), IP(q + .5, 5.97), IP(q + .5, 6.03), IP(q, 6.03)], K.trait); }
      g.restore();
      var L = [];
      function ajoute(pr_, f) { L.push([pr_, f]); }
      Object.keys(bat).forEach(function (n) {
        var b = BAT[n]; if (!b) return; var p = pousseDe(n, t); if (p <= 0) return;
        var prof = b.i + b.w / 2 + b.j + b.d / 2 + (n === "monde" ? -3 : 0);
        if (n === "usine" || n === "usine2") { ajoute(prof, function () { usine(n, t, p); }); if (b.ext) ajoute(b.ext.i + b.ext.w / 2 + b.ext.j + b.ext.d / 2, function () { aile(n, t); }); }
        else if (n === "magasin") ajoute(prof, function () { magasin(t, p); });
        else if (n === "banque") ajoute(prof, function () { banque(t, p); });
        else if (n === "etat") ajoute(prof, function () { etat(t, p); });
        else if (n === "monde") ajoute(prof, function () { monde(t, p); });
        else if (n === "maisons") MAISONS.forEach(function (m, k) { var pm = ease(P(t, bat.maisons.t + k * .07, .45)); ajoute(m[0] + m[1] + 2.6, function () { maison(m[0], m[1], pm, m[2]); }); });
      });
      ARBRES.forEach(function (a, k) { if (dans(a[0], a[1])) return; var pa = ease(P(t, T0 + .7 + k * .03, .45)); ajoute(a[0] + a[1] + .3, function () { arbre(a[0], a[1], pa); }); });
      flux.forEach(function (f, fi) {
        f.departs.forEach(function (d, k) {
          var q = (t - d) / f.duree; if (q < 0 || q > 1) return;
          var p = f.ch.at(q), pr_ = p[0] + p[1] + .3;
          if (f.k === "biens") ajoute(pr_ + .1, function () { caisse(p[0], p[1]); });
          else if (f.k === "revenus") ajoute(pr_, function () { piece(p[0], p[1], 14 + 6 * Math.sin(q * Math.PI), 8 + 2.5 * Math.min(2, f.n)); });
          else if (f.k === "achats") ajoute(pr_, function () { passant(p[0], p[1], TEINTES[(k + fi) % 6], t, k); });
          else if (f.k === "emplois") ajoute(pr_, function () { passant(p[0], p[1], K.canard, t, k, true); });
        });
      });
      machines.forEach(function (m) {
        var qc = P(t, m.t, 1.0); if (qc <= 0 || qc >= 1) return;
        var b = BAT[m.sur], ch = { pts: [[6, -0.6], [6, b.porte[1]], [b.porte[0] + .2, b.porte[1]]] };
        var tot = (b.porte[1] + .6) + Math.abs(6 - b.porte[0] - .2), s = EIO(qc) * tot, p;
        if (s < b.porte[1] + .6) p = [6, -0.6 + s]; else p = [6 - (s - b.porte[1] - .6) * Math.sign(6 - b.porte[0]), b.porte[1]];
        ajoute(p[0] + p[1] + .6, function () { camion(p[0], p[1]); });
      });
      L.sort(function (a, b) { return a[0] - b[0]; }); L.forEach(function (x) { x[1](); });
      // panneaux plantés derrière la maquette
      panneaux.forEach(function (pn) {
        var p = ease(P(t, pn.t, .65)); if (p <= 0) return;
        var q = IP(.2, .2), hp = 120 * p, bw = 660, bh = 290, top = q[1] - hp - bh;
        g.fillStyle = "#7A5B3A"; g.fillRect(q[0] - 210, q[1] - hp, 14, hp); g.fillRect(q[0] + 196, q[1] - hp, 14, hp);
        g.save(); g.translate(q[0], top + bh / 2); g.scale(1, cl(p, 0, 1.2)); g.translate(0, -bh / 2);
        g.fillStyle = "#fff"; rr(-bw / 2, 0, bw, bh, 20); g.fill(); g.strokeStyle = K.encre; g.lineWidth = 5; g.stroke();
        g.fillStyle = K.corail; rr(-bw / 2, 0, bw, 58, [20, 20, 0, 0]); g.fill();
        g.textAlign = "center"; F(30, 700); g.fillStyle = "#fff"; g.fillText(pn.c.t || "", 0, 39);
        F(150, 700); g.fillStyle = K.encre; g.fillText(pn.c.n || "", 0, 206); F(30, 500); g.fillStyle = K.gris; g.fillText(pn.c.s || "", 0, 260); g.textAlign = "left";
        g.restore();
      });
      // machines installées, prix
      machines.forEach(function (m) {
        var pm = ease(P(t, m.t + .85, .4)); if (pm <= 0) return; var b = BAT[m.sur];
        var q = IP(b.i + b.w / 2, b.j + b.d / 2, b.h + 66); g.fillStyle = "rgba(255,255,255,.92)"; g.beginPath(); g.arc(q[0], q[1], 38 * pm, 0, 7); g.fill();
        g.strokeStyle = K.encre; g.lineWidth = 3; g.stroke(); engrenage(q[0], q[1], 26 * pm, t * 2.2, K.encre);
      });
      prix.forEach(function (px) {
        var b = BAT[px.c.sur || "magasin"], q = IP(b.i + b.w * .5, b.j + b.d * .5, b.h + 56), flip = P(t, px.t, .4), sx = Math.abs(Math.cos(flip * Math.PI)), apres = flip > .5;
        if (pousseDe(px.c.sur || "magasin", t) < .9) return;
        g.save(); g.translate(q[0], q[1]); g.scale(sx, 1);
        g.strokeStyle = K.encre; g.lineWidth = 2; g.beginPath(); g.moveTo(0, 26); g.lineTo(0, 50); g.stroke();
        var cf = apres ? (K[px.c.c] || px.c.c || K.vert) : K.ivoire;
        g.fillStyle = cf; g.beginPath(); g.moveTo(-62, -26); g.lineTo(44, -26); g.lineTo(66, 0); g.lineTo(44, 26); g.lineTo(-62, 26); g.closePath(); g.fill();
        g.strokeStyle = K.encre; g.lineWidth = 2.5; g.stroke(); g.fillStyle = K.encre; g.beginPath(); g.arc(46, 0, 5, 0, 7); g.fill();
        F(28, 700); g.fillStyle = apres ? "#fff" : K.encre; g.textAlign = "center"; g.fillText(apres ? (px.c.t || "PRIX ↓") : "PRIX", -8, 10); g.textAlign = "left";
        g.restore();
      });
    }
    // plaques des bâtiments et étiquettes des flux (à l'écran)
    function plaques(t) {
      var poses = [];
      Object.keys(bat).forEach(function (n) {
        var b = BAT[n]; if (!b || !NOMS[n]) return; var p = E(P(t, bat[n].t + .4, .4)); if (p <= 0) return;
        var q = ecran(IP(b.i + b.w, b.j + b.d, 0)); F(26, 700); var tw = g.measureText(NOMS[n]).width;
        var x = q[0] - tw / 2 - 14, y = q[1] + 8, ferme = bat[n].ferme != null && t >= bat[n].ferme;
        g.save(); g.globalAlpha = p * .95; g.fillStyle = ferme ? "#8A9093" : K.encre; rr(x, y, tw + 28, 38, 8); g.fill();
        g.fillStyle = "#fff"; g.fillText(NOMS[n], x + 14, y + 28); g.restore();
      });
      flux.forEach(function (f) {
        if (!f.l || t < f.t0 || t > f.t1 + .5) return;
        var a = (f.avant && f.avant.l === f.l ? 1 : E(P(t, f.t0 + .6, .4))) * (f.apres && f.apres.l === f.l ? 1 : 1 - E(P(t, f.t1, .4))); if (a <= 0) return;
        var m = f.ch.at(.72), q = ecran(IP(m[0], m[1], 26)); F(24, 700); var tw = g.measureText(f.l).width;
        poses.forEach(function (p0) { if (Math.abs(p0[0] - q[0]) < tw / 2 + p0[2] / 2 + 20 && Math.abs(p0[1] - q[1]) < 38) q = [q[0], p0[1] + 40]; });
        poses.push([q[0], q[1], tw]);
        g.save(); g.globalAlpha = a; g.fillStyle = f.k === "revenus" ? "#FFF4D6" : "#E4F1F3"; g.strokeStyle = f.k === "revenus" ? "#B98213" : K.canard; g.lineWidth = 2;
        rr(q[0] - tw / 2 - 12, q[1] - 36, tw + 24, 33, 16); g.fill(); g.stroke();
        g.fillStyle = K.encre; g.textAlign = "center"; g.fillText(f.l, q[0], q[1] - 12); g.textAlign = "left"; g.restore();
      });
    }
    function etiquettes(t) {
      cartes.forEach(function (c, k) {
        if (t < c.t) return; var suiv = cartes[k + 1], actif = !suiv || t < suiv.t, b = BAT[c.sur] || BAT.usine;
        var hz = (bat[c.sur] && c.sur !== "maisons" ? b.h : 34) + 40;
        var an = ecran(IP(b.i + b.w / 2, b.j + b.d / 2, hz)), ax = an[0], ay = an[1];
        // plusieurs pastilles sur le même bâtiment : côte à côte, et à l'écart de l'étiquette de prix
        var rang = cartes.slice(0, k).filter(function (x) { return x.sur === c.sur; }).length;
        var dec = rang * 48 + (prix.some(function (px) { return (px.c.sur || "magasin") === c.sur; }) ? 96 : 0) + (machines.some(function (m) { return m.sur === c.sur; }) ? 58 : 0);
        if (!actif) ax += dec;
        var colN = k === nCartes - 1 ? K.vert : K.corail;
        if (actif) {
          var p = E(P(t, c.t, .35));
          F(40, 700); var wh = g.measureText(c.h).width; F(27, 500); var ws = g.measureText(c.s).width;
          var cw = Math.max(wh, ws) + 136, ch = 116, cx = ax < VW / 2 ? VW - cw - 70 : 70, cy = ax < VW / 2 ? 140 : 560;
          if (cx + cw > VW - 20) cx = VW - cw - 20;
          g.strokeStyle = K.encre; g.lineWidth = 2.5; g.setLineDash([2, 6]); g.lineCap = "round";
          var bx = ax < cx ? cx : cx + cw, by = cy + ch / 2; g.beginPath(); g.moveTo(bx, by); g.lineTo(bx + (ax - bx) * p, by + (ay - by) * p); g.stroke(); g.setLineDash([]);
          g.fillStyle = K.encre; g.beginPath(); g.arc(ax, ay, 7 * p, 0, 7); g.fill();
          g.save(); g.globalAlpha = cl(p * 1.5, 0, 1); g.translate(cx + cw / 2, cy + ch / 2); var s = .85 + .15 * EB(p); g.scale(s, s); g.translate(-cw / 2, -ch / 2);
          g.shadowColor = "rgba(20,35,43,.25)"; g.shadowBlur = 24; g.shadowOffsetY = 8; g.fillStyle = "#fff"; rr(0, 0, cw, ch, 18); g.fill(); g.shadowColor = "transparent";
          g.fillStyle = colN; g.beginPath(); g.arc(58, ch / 2, 32, 0, 7); g.fill();
          F(36, 700); g.fillStyle = "#fff"; g.textAlign = "center"; g.fillText(String(c.n), 58, ch / 2 + 13); g.textAlign = "left";
          F(40, 700); g.fillStyle = K.encre; g.fillText(c.h, 108, 52); F(27, 500); g.fillStyle = K.gris; g.fillText(c.s, 108, 90);
          g.restore();
        } else {
          g.fillStyle = colN; g.strokeStyle = "#fff"; g.lineWidth = 4; g.beginPath(); g.arc(ax, ay, 21, 0, 7); g.fill(); g.stroke();
          F(24, 700); g.fillStyle = "#fff"; g.textAlign = "center"; g.fillText(String(c.n), ax, ay + 9); g.textAlign = "left";
        }
      });
    }
    function compteur(t) {
      compteurs.forEach(function (cp) {
        var c = cp.c, p = E(P(t, cp.t, .35)) * (1 - P(t, cp.fin - .3, .3)); if (p <= 0) return;
        var val = Math.round(c.de + (c.a - c.de) * E(P(t, cp.t + .3, .8))), b = BAT[c.sur || "usine"], q = ecran(IP(b.i, b.j + b.d, 0));
        var bx = cl(q[0] - 480, 40, VW - 470), by = cl(q[1] + 20, 300, VH - 290);
        g.save(); g.globalAlpha = p; g.fillStyle = K.encre; rr(bx, by, 440, 156, 16); g.fill();
        F(25, 500); g.fillStyle = "rgba(248,245,238,.78)"; g.fillText(c.l || "", bx + 24, by + 40);
        F(56, 700); g.fillStyle = K.piece; var s = val + (c.u ? "" : ""); g.fillText(String(val), bx + 24, by + 104); var wv = g.measureText(String(val)).width;
        F(25, 500); g.fillStyle = K.ivoire; g.fillText(c.u || "", bx + 38 + wv, by + 104);
        if (c.note) { F(19, 500); g.fillStyle = "rgba(248,245,238,.6)"; g.fillText(c.note, bx + 24, by + 138); }
        g.restore();
      });
    }
    function cartel(t, tl) {
      var titre = v.titre || SCN.titre || "", kick = v.kicker || "L'économie en maquette";
      var p = E(P(tl, .2, .5)), pt = EIO(P(tl, 1.6, .6)), s = .9 - .3 * pt, x = 50, y = 100 - 6 * pt;
      F(54, 700); var tw = Math.max(560, g.measureText(titre).width + 80); var lignes = tw > 1100 ? 2 : 1;
      var mots = titre.split(" "), l1 = titre, l2 = "";
      if (lignes === 2) { var k = Math.ceil(mots.length / 2); l1 = mots.slice(0, k).join(" "); l2 = mots.slice(k).join(" "); tw = Math.max(g.measureText(l1).width, g.measureText(l2).width) + 80; }
      var hh = lignes === 2 ? 190 : 136;
      g.save(); g.globalAlpha = p; g.translate(x, y + (1 - p) * 30); g.scale(s, s);
      g.fillStyle = K.encre; rr(0, 0, tw, hh, 16); g.fill();
      F(24, 700); g.fillStyle = K.piece; g.fillText(kick.toUpperCase().split("").join(" "), 40, 50);
      F(54, 700); g.fillStyle = K.ivoire; g.fillText(l1, 40, 110); if (l2) g.fillText(l2, 40, 166);
      g.restore();
      if (v.legende === false) return;
      var pl = E(P(tl, 1.7, .4)); if (pl <= 0) return;
      var lx = 60, ly = y + hh * s + 16;
      g.save(); g.globalAlpha = pl; g.fillStyle = "rgba(255,255,255,.88)"; rr(lx, ly, 330, 58, 12); g.fill();
      g.fillStyle = K.canardC; g.fillRect(lx + 22, ly + 19, 20, 20); g.strokeStyle = K.canard; g.lineWidth = 2; g.strokeRect(lx + 22, ly + 19, 20, 20);
      F(25, 500); g.fillStyle = K.encre; g.fillText("biens", lx + 54, ly + 38);
      g.fillStyle = K.piece; g.beginPath(); g.arc(lx + 160, ly + 29, 11, 0, 7); g.fill(); g.strokeStyle = "#B98213"; g.stroke();
      g.fillStyle = K.encre; g.fillText("revenus", lx + 182, ly + 38); g.restore();
    }
    return function (t, st) {
      g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.textAlign = "left"; g.textBaseline = "alphabetic"; g.setLineDash([]);
      g.clearRect(0, 0, VW, VH);
      g.save(); g.beginPath(); g.rect(0, 72, VW, VH - 72); g.clip();       // la maquette, photographiée sur un fond uni : un cadre net dans la page
      g.fillStyle = K.fond; g.fillRect(0, 72, VW, VH - 72);
      var c = camera(t); CX = c[0]; CY = c[1]; CS = c[2];
      g.save(); g.translate(VW / 2, VH / 2); g.scale(CS, CS); g.translate(-CX, -CY); ville(t); g.restore();
      plaques(t); compteur(t); etiquettes(t); cartel(t, st.tl);
      g.restore();
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
          x.d.style.boxShadow = "0 0 0 " + (2.5 + 2 * g).toFixed(1) + "px rgba(229,83,63," + (.9 * E(q)).toFixed(2) + ")";
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
      grille.push(sv("line", { x1: X(x), x2: X(x), y1: m[2], y2: m[2] + ph, stroke: "rgba(22,24,26,.1)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x), Y(y0) + 12, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("line", { x1: m[0], x2: m[0] + pw, y1: Y(y), y2: Y(y), stroke: "rgba(22,24,26,.1)", "stroke-width": 1 }, fond));
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
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col, stroke: C.papier, "stroke-width": 2 }, g);
        });
        if (d.proj) {
          x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 1.6, "stroke-dasharray": "5 5", fill: "none", opacity: .8 }, g);
        }
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "rect" || d.type === "balaye") {
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: col, "fill-opacity": .22, stroke: col, "stroke-width": 2 }, g);
        x.pt = sv("circle", { r: 8, fill: col, stroke: C.papier, "stroke-width": 2 }, g);
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
  var NIVEAUX = { p1: ["Partie 1 · Mobilisation des connaissances", "#2E7D4F"], p2: ["Partie 2 · Étude d'un document", "#0B5563"],
    p3: ["Partie 3 · Raisonnement sur dossier", "#9A6A0E"], dissert: ["Dissertation", "#C2402B"], calcul: ["Savoir-faire · calculs", "#2E7D4F"] };
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

  /* ---------- le magazine : mise en page, caméra, pages qui tournent ---------- */
  /* Identité « Faits & Courbes » (10/11/2026) : la vidéo est un magazine qu'on feuillette sur une table. La couverture ouvre
     l'épisode (titre du chapitre, chiffre-choc : le premier type chiffres), la quatrième de couverture le ferme (dernier
     visuel titre de l'épisode : « prochain numéro »). Chaque partie (scène) a sa double page, ou sa suite de doubles pages :
     la page d'ouverture porte le surtitre (« Partie I »), le titre de la partie, le chapeau et le texte courant (la narration
     de la partie, en colonnes) ; les visuels de la scène sont mis en page comme des articles, dans des emplacements de
     1280 × 720 (la scène logique d'avant, inchangée : les x, y, w des scripts restent valables), deux par page, avec leur
     rubrique (« Définition », « Graphique », « Décryptage »…). Des visuels qui se chevauchent dans le temps partagent un
     emplacement ; un emplacement rempli reste imprimé (dans l'état de sa dernière image). La caméra va d'un emplacement à
     l'autre au début de chacun, recule sur la double page avant que la page se tourne (entre deux parties, ou quand une
     partie déborde sur une nouvelle double page). Restent posés sur l'écran, au-dessus du magazine : frappe (mot tamponné),
     flash (« À retenir », pendant que la caméra montre toute la double page), notion. Champ facultatif d'un visuel :
     rubrique (remplace l'étiquette de l'emplacement). Tout est fonction pure du temps. */
  var PW = 1360, PH = 1780, SX = 40, SL = [110, 900], ZOOM = .925;
  var SECTION = { canard: "#0B5563", corail: "#C2402B", moutarde: "#9A6A0E", vert: "#2E7D4F", nuit: "#16181A" };
  var ECRAN = { frappe: 1, flash: 1, notion: 1 };
  var RUBRIQUE = { def: "Définition", note: "Attention", cols: "Face-à-face", donnees: "Graphique", chaine: "Décryptage", chiffres: "En chiffres",
    sanim: "Animation", auteur: "Portrait", compare: "Comparaison", plan: "Le plan", formule: "Le calcul", graphe: "Graphique", exo: "Sujet",
    pause: "À toi", question: "La question", liste: "L'essentiel", cartes: "Repères", frise: "Repères", cit: "Citation", portrait: "Portrait",
    titre: "Le dossier", illu: "Schéma", ville: "La maquette", tableau: "Image", mot: "Le mot", nuage: "Les mots", carte: "Carte mentale",
    dialogue: "Dialogue", tag: "Repère" };
  // grain du papier, calculé une fois (motif déterministe), posé en fond de chaque page
  var GRAIN = (function () {
    try {
      var c = document.createElement("canvas"); c.width = c.height = 256;
      var x = c.getContext("2d"), im = x.createImageData(256, 256);
      for (var i = 0; i < 65536; i++) { var v = alea(i * 1.37) * 255; im.data[i * 4] = im.data[i * 4 + 1] = im.data[i * 4 + 2] = v; im.data[i * 4 + 3] = 22; }
      x.putImageData(im, 0, 0); return "url(" + c.toDataURL() + ")";
    } catch (e) { return "none"; }
  })();
  function phrases(txt) { return (String(txt).match(/[^.!?…]+[.!?…]+[»"]?\s*|[^.!?…]+$/g) || []).map(function (s) { return s.trim(); }).filter(Boolean); }

  // toutes les polices de la scène, chargées d'avance : la mise en page (titres ajustés, chaînes causales) se mesure
  // avec les vraies polices, et l'export n'enregistre aucune image avec une police de secours
  var POLICES = ['500 20px "IBM Plex Sans Condensed"', '700 20px "IBM Plex Sans Condensed"', '400 20px "IBM Plex Sans"', '600 20px "IBM Plex Sans"',
    '700 20px "IBM Plex Sans"', '400 20px Spectral', '600 20px Spectral', 'italic 400 20px Spectral', 'italic 500 20px Spectral', '400 20px Archivo',
    '600 20px Archivo', '700 20px Archivo', '500 20px "JetBrains Mono"', '500 20px "Space Grotesk"', '700 20px "Space Grotesk"'];
  var policesPretes = !document.fonts || !document.fonts.load;
  var chargePolices = policesPretes ? Promise.resolve() : Promise.all(POLICES.map(function (p) { return document.fonts.load(p, "Aé€−×→").catch(function () {}); }))
    .then(function () { return document.fonts.ready; }).then(function () { policesPretes = true; });
  function Scene(EP, racine) {
    var sc = h("div", "scene mag", racine);
    h("div", "table", sc);
    var monde = h("div", "monde", sc), ombreMag = h("div", "ombre-mag", monde);
    var ecran = h("div", "ecran", sc);
    var fil = h("div", "fil", sc), st = h("div", "st", sc), stS = h("span", "", st);
    var NUM = CODE_Q(EP.code) || ("n° " + (EP.num || 1));
    var NOTION = String(EP.notion || EP.titre || "").toUpperCase();

    // ----- tri des visuels : écran, en-têtes de partie, emplacements -----
    var scDe = function (v) { if (v.scene) return v.scene; var s = EP.scenes.filter(function (x) { return v.t0 >= x.t0 - .01; }).pop(); return (s || EP.scenes[0]).id; };
    var titres = EP.vis.filter(function (v) { return v.type === "titre"; });
    var derniere = EP.scenes[EP.scenes.length - 1];
    var fin = titres.length && scDe(titres[titres.length - 1]) === derniere.id &&
      !EP.vis.some(function (v) { return !ECRAN[v.type] && v.t0 > titres[titres.length - 1].t0 + .01; }) ? titres[titres.length - 1] : null;
    var chapitres = {}, flashs = {};
    EP.vis.forEach(function (v) { if (v.type === "chapitre") chapitres[scDe(v)] = v; if (v.type === "flash") flashs[scDe(v)] = v; });
    var chiffreUne = null;
    EP.vis.some(function (v) { if (v.type === "chiffres" && v.items && v.items.length) { chiffreUne = v.items[0]; return true; } return false; });

    // ----- pages -----
    var pages = [], nPage = 1;
    function page(cote, s, cls) {
      var p = h("div", "page " + cote + (cls ? " " + cls : ""), monde);
      p.style.left = (cote === "g" ? -PW : 0) + "px"; p.style.display = "none"; p.style.backgroundImage = GRAIN;
      var o = { el: p, cote: cote, s: s, groupes: [], vu: false, x0: cote === "g" ? -PW : 0, n: ++nPage };
      o.ombre = h("div", "p-ombre", p);
      if (s) {
        var col = SECTION[s.fond] || SECTION.nuit;
        p.style.setProperty("--sec", col);
        var tete = h("div", "p-tete", p);
        if (cote === "g") tete.innerHTML = "<b>" + o.n + "</b>FAITS &amp; COURBES · " + esc(NOTION);
        else tete.innerHTML = esc(String(s.chap).toUpperCase()) + "<b>" + o.n + "</b>";
        h("div", "p-pied", p, cote === "g" ? "SES · TERMINALE · " + esc(NUM) : "faits &amp; courbes");
      }
      pages.push(o);
      return o;
    }
    function emplacement(pg, k) {
      var s = h("div", "slot", pg.el); s.style.top = SL[k] + "px";
      if (k === 1) h("div", "p-filet", pg.el);
      return { pg: pg, el: s, bloc: h("div", "bloc", s), rect: [pg.x0 + SX + 640, SL[k] + 360] };
    }
    // texte courant : la narration de la partie
    function narration(s) {
      return EP.sous.filter(function (x) { return x[0] >= s.t0 - .01 && x[0] < s.t1; }).map(function (x) { return x[2]; }).join(" ").replace(/\s+/g, " ").trim();
    }
    function ouverture(pg, s, i) {
      var z = h("div", "ouv", pg.el), ch = chapitres[s.id];
      var kick = h("div", "ouv-k", z), band = h("span", "ouv-band", kick);
      h("span", "ouv-kt", kick, ch ? "Partie " + esc(ch.num) : (i === 0 ? "Le dossier · " + esc(NUM) : esc(s.chap)));
      var num = ch ? h("div", "ouv-num", z, esc(ch.num)) : null;
      if (num) num.style.fontSize = [76, 76, 72, 58, 46, 40][Math.min(5, String(ch.num).length)] + "px";
      var tt = h("div", "ouv-t", z), ts = h("span", "ouv-ts", tt, esc(ch ? (ch.t || s.chap) : (i === 0 ? EP.titre : s.chap)));
      var trait = h("div", "ouv-trait", z);
      var ph = phrases(narration(s)), chap = [], reste = [];
      ph.forEach(function (x) { if ((chap.join(" ") + x).length < 190 || !chap.length) chap.push(x); else reste.push(x); });
      var lede = h("div", "ouv-c", z, esc(chap.join(" ")));
      var cols = h("div", "ouv-cols", z);
      if (reste.length) {      // lettrine : la première lettre du texte courant (guillemets et ponctuation laissés de côté)
        var r = reste.join(" ").replace(/^[^0-9A-Za-zÀ-ÖØ-öø-ÿ]+/, ""), l0 = Array.from(r)[0] || "";
        cols.innerHTML = '<span class="lettrine">' + esc(l0) + "</span>" + esc(r.slice(l0.length));
      }
      return { z: z, band: band, num: num, tt: tt, ts: ts, trait: trait, lede: lede, cols: cols, t0: ch ? ch.t0 : s.t0, ch: ch, pg: pg };
    }
    function remplir(sl, s, k) {      // emplacement libre : citation en exergue et texte courant
      var z = h("div", "vide", sl.el), fl = flashs[s.id], ph = phrases(narration(s));
      var ex = fl ? fl.t : (ph.slice().sort(function (a, b) { return b.length - a.length; })[0] || "");
      if (ex.length > 210) ex = phrases(ex)[0] || ex;
      h("div", "vd-gu", z, "«"); h("div", "vd-ex", z, esc(ex));
      var debut = Math.min(ph.length, 3 + k * 4);
      var c = h("div", "vd-cols", z, esc(ph.slice(debut).concat(ph.slice(0, debut)).join(" ")));
      return z;
    }

    // couverture
    var une = page("d", null, "une");
    (function () {
      var p = une.el;
      var bd = h("div", "u-band", p); h("span", "", bd, "SES · Terminale"); h("span", "", bd, "N° " + esc(NUM) + " · " + esc(EP.notion || ""));
      une.mast = h("div", "u-mast", p, "FAITS &amp; COURBES");
      h("div", "u-regle", p);
      if (chiffreUne) {
        h("div", "u-k", p, "Le chiffre");
        une.chif = h("div", "u-chif", p, esc(chiffreUne.n));
        h("div", "u-l", p, esc(chiffreUne.l));
        if (chiffreUne.s) h("div", "u-s", p, "Source : " + esc(chiffreUne.s));
      }
      h("div", "u-regle b", p);
      une.titre = h("div", "u-titre", p, esc(EP.titre));
      var tz = h("div", "u-som", p);
      EP.scenes.filter(function (s, i) { return i > 0 && chapitres[s.id]; }).slice(0, 3).forEach(function (s) {
        var d = h("div", "u-it", tz); h("div", "u-in", d, "Partie " + esc(chapitres[s.id].num)); h("div", "u-it2", d, esc(s.chap));
      });
      h("div", "u-pied", p, "Le cours en vidéo · le chapitre complet, de zéro au bac");
    })();

    // groupes de visuels par partie, emplacements, doubles pages
    var planches = [{ L: null, R: une, t: 0 }];
    var groupes = [], objs = [], ouvs = [];
    function nouvelObjet(v, parent) {
      var el = h("div", "v", parent), o = { v: v, el: el, disp: "block", entree: "monte", vis: false };
      el.style.display = "none";
      o.upd = (TYPES[v.type] || function () { return function () {}; })(o, v);
      objs.push(o);
      return o;
    }
    EP.scenes.forEach(function (s, i) {
      var vs = EP.vis.filter(function (v) {
        return scDe(v) === s.id && !ECRAN[v.type] && v.type !== "generique" && v.type !== "chapitre" && v !== fin;
      }).sort(function (a, b) { return a.t0 - b.t0; });
      var gr = [];
      vs.forEach(function (v) {
        var g = gr[gr.length - 1];
        if (g && v.t0 < g.fin - .05) { g.vis.push(v); g.fin = Math.max(g.fin, v.t1); } else gr.push({ vis: [v], debut: v.t0, fin: v.t1 });
      });
      var L = page("g", s, "ouvre"), R = page("d", s), ov = ouverture(L, s, i); ouvs.push(ov);
      var pl = { L: L, R: R, t: s.t0, s: s, ouv: ov, chap: !!chapitres[s.id], groupes: [] };
      planches.push(pl);
      var libres = [emplacement(L, 1), emplacement(R, 0), emplacement(R, 1)];
      gr.forEach(function (g) {
        if (!libres.length) {
          var L2 = page("g", s), R2 = page("d", s);
          pl = { L: L2, R: R2, t: g.debut, s: s, groupes: [] }; planches.push(pl);
          libres = [emplacement(L2, 0), emplacement(L2, 1), emplacement(R2, 0), emplacement(R2, 1)];
        }
        var sl = libres.shift(), princ = g.vis.filter(function (v) { return v.type !== "tag"; })[0] || g.vis[0];
        var rub = princ.rubrique || (g.vis.some(function (v) { return v.type === "exo" && v.mode === "coin"; }) ? "Le corrigé" : RUBRIQUE[princ.type] || "");
        h("div", "rub", sl.el, esc(rub));
        g.slot = sl; g.objs = g.vis.map(function (v) { return nouvelObjet(v, sl.bloc); }); g.cle = null;
        sl.pg.groupes.push(g); pl.groupes.push(g); groupes.push(g);
      });
      libres.forEach(function (sl, k) { remplir(sl, s, k); });
    });
    var dos = null;
    if (fin) {
      dos = page("g", null, "dos");
      var p = dos.el;
      h("div", "d-mast", p, "FAITS &amp; COURBES");
      h("div", "d-k", p, "Prochain numéro");
      dos.suiv = h("div", "d-suiv", p, esc(EP.suivant || ""));
      h("div", "d-regle", p);
      dos.t = h("div", "d-t", p, esc(fin.t || ""));
      if (fin.sous) h("div", "d-s", p, esc(fin.sous));
      var cb = h("div", "d-code", p), bars = "";
      for (var k = 0; k < 46; k++) bars += '<i style="width:' + (2 + Math.floor(alea(k + 9) * 3) * 3) + 'px"></i>';
      cb.innerHTML = bars + '<span>SES · ' + esc(NUM) + "</span>";
      h("div", "d-pied", p, esc(EP.notion || "") + " · le cours en vidéo");
      planches.push({ L: dos, R: null, t: fin.t0, fin: true });
    }
    var ecrans = EP.vis.filter(function (v) { return ECRAN[v.type]; }).map(function (v) { return nouvelObjet(v, ecran); });

    // ----- pages qui tournent : du feuillet k au feuillet k + 1 -----
    var tours = planches.slice(1).map(function (pl, i) {
      var T = pl.t, avecCarton = pl.ouv && pl.chap;
      var ta = avecCarton ? T - .7 : pl.fin ? T - .5 : T - 1.1, tb = avecCarton ? T + .5 : pl.fin ? T + .8 : T + .1;
      if (i === 0) { ta = Math.min(ta, 4.9); tb = Math.max(ta + 1.1, tb); }
      return { ta: ta, tb: tb, k: i };
    });

    // ----- caméra : plans successifs [arrivée a → b, cadre c0, puis lente poussée jusqu'à c1] -----
    function vueEnsemble(k) {
      var pl = planches[k], cx = pl.L && pl.R ? 0 : pl.R ? PW / 2 : -PW / 2;
      return [cx, PH / 2, .375];
    }
    function cadre(c, f) { return [c[0], c[1], ZOOM * (f || 1)]; }
    var plans = [];
    planches.forEach(function (pl, k) {
      if (k === 0) { plans.push({ a: 0, b: 0, c0: vueEnsemble(0), c1: [PW / 2, 660, .5] }); return; }
      var tr = tours[k - 1], prec = planches[k - 1], fl = prec.s && flashs[prec.s.id];
      var aOv = fl && fl.t0 < tr.ta && fl.t0 > tr.ta - 8 ? fl.t0 : tr.ta - .8;
      plans.push({ a: aOv, b: Math.min(tr.ta, aOv + 1.1), c0: vueEnsemble(k - 1), c1: vueEnsemble(k - 1) });
      plans.push({ a: tr.ta, b: tr.tb, c0: vueEnsemble(k), c1: vueEnsemble(k) });
      if (pl.fin) { plans.push({ a: tr.tb, b: tr.tb + 1.2, c0: [-PW / 2, PH / 2, .385], c1: [-PW / 2, PH / 2 - 150, .44] }); return; }
      if (pl.ouv && pl.chap) plans.push({ a: tr.tb, b: tr.tb + .9, c0: cadre([-PW + SX + 640, SL[0] + 360]), c1: cadre([-PW + SX + 640, SL[0] + 360], 1.02) });
      pl.groupes.forEach(function (g) { plans.push({ a: g.debut - .45, b: g.debut + .45, c0: cadre(g.slot.rect), c1: cadre(g.slot.rect, 1.025) }); });
    });
    // ordre strict des clés : une arrivée ne commence pas avant la fin de la précédente
    for (var i = 1; i < plans.length; i++) {
      if (plans[i].a < plans[i - 1].b + .05) plans[i].a = plans[i - 1].b + .05;
      if (plans[i].b < plans[i].a + .35) plans[i].b = plans[i].a + .35;
    }
    var CLES = [];
    plans.forEach(function (p, i) {
      if (i) CLES.push([p.a, plans[i - 1].c1]);
      CLES.push([p.b, p.c0]);
    });
    CLES.push([EP.dur + 10, plans[plans.length - 1].c1]);
    function camera(t) {
      var i = 0; while (i < CLES.length - 2 && t > CLES[i + 1][0]) i++;
      var A = CLES[i], B = CLES[i + 1], ca = A[1], cb = B[1];
      var p = EIO(P(t, A[0], Math.max(.001, B[0] - A[0])));
      var s = Math.exp(Math.log(ca[2]) + (Math.log(cb[2]) - Math.log(ca[2])) * p);
      // grand déplacement : la caméra prend un peu de recul en chemin
      var d = Math.hypot(cb[0] - ca[0], cb[1] - ca[1]) * Math.min(ca[2], cb[2]) / 1280;
      s *= 1 - Math.min(.4, .3 * d) * Math.sin(Math.PI * p);
      return [ca[0] + (cb[0] - ca[0]) * p, ca[1] + (cb[1] - ca[1]) * p, s];
    }

    // ----- mise en page qui dépend des polices (titres ajustés à leur cadre) -----
    var misEnPage = false;
    function ajuster(el, max, min, lignes) {
      var fs = max; el.style.fontSize = fs + "px";
      var lh = parseFloat(getComputedStyle(el).lineHeight) / fs || 1.02;
      while (fs > min && el.scrollHeight > lignes * fs * lh + 6) { fs -= 3; el.style.fontSize = fs + "px"; }
    }
    function largeur(el, max, w) {
      var fs = max; el.style.fontSize = fs + "px";
      while (fs > 20 && el.scrollWidth > w) { fs -= 4; el.style.fontSize = fs + "px"; }
    }
    function mettreEnPage() {
      var vus = [];
      pages.forEach(function (p) { if (p.el.style.display === "none") { p.el.style.display = "block"; p.el.style.visibility = "hidden"; vus.push(p); } });
      largeur(une.mast, 260, 1280);
      if (une.chif) largeur(une.chif, 430, 1280);
      ajuster(une.titre, 104, 50, 3);
      ouvs.forEach(function (o) {      // titre sur deux lignes (trois s'il est long), chapeau et colonnes à la suite
        ajuster(o.tt, 124, 76, 2); if (o.tt.scrollHeight > 2 * parseFloat(o.tt.style.fontSize) * 1.06) ajuster(o.tt, 104, 60, 3);
        var y = o.tt.offsetTop + o.tt.offsetHeight + 26;
        o.lede.style.top = y + "px"; ajuster(o.lede, 36, 26, 3);
        o.cols.style.top = (y + o.lede.offsetHeight + 26) + "px";
      });
      if (dos) { ajuster(dos.suiv, 112, 50, 3); ajuster(dos.t, 64, 36, 2); }
      vus.forEach(function (p) { p.el.style.display = "none"; p.el.style.visibility = ""; });
      misEnPage = true;
    }

    // ----- rendu d'un visuel (dans un emplacement ou sur l'écran) -----
    function majObjet(o, t) {
      var v = o.v;
      if (t < v.t0 || t > v.t1 + (v.type === "tableau" ? 1 : .7)) { if (o.vis) { o.el.style.display = "none"; o.vis = false; } return; }
      if (!o.vis) { o.el.style.display = o.disp; o.vis = true; }
      var a = E(P(t, v.t0, .7)), out = EIO(P(t, v.t1, .6));
      if (v.type !== "tableau") o.el.style.opacity = (o.entree === "aucune" ? 1 : a) * (1 - out);
      var flou = (o.entree === "monte" ? (1 - a) * 6 : 0) + out * 5;
      if (v.type !== "tableau") o.el.style.filter = flou > .05 ? "blur(" + flou.toFixed(1) + "px)" : "none";
      if (o.entree === "monte") o.el.style.transform = "translateY(" + (22 * (1 - a) - 10 * out).toFixed(2) + "px) scale(" + (0.975 + 0.025 * a).toFixed(4) + ")";
      else if (v.type !== "tableau") o.el.style.transform = out > 0 ? "scale(" + (1 + .02 * out) + ")" : "";
      o.upd(t, { tl: t - v.t0, a: a, o: out });
    }
    // un emplacement rempli reste imprimé : après sa fin, il garde l'état de sa dernière image
    function majGroupe(g, t) {
      var tt = Math.min(t, g.fin - .02), cle = tt + (policesPretes ? "" : "~");
      if (t >= g.fin && g.cle === cle) return;
      g.cle = t >= g.fin ? cle : null;
      g.objs.forEach(function (o) { majObjet(o, tt); });
    }
    function majOuverture(o, t) {
      if (!o.ch) return;
      var tl = t - o.t0;
      tr(o.band, "scaleX(" + E(P(tl, .5, .6)).toFixed(3) + ")");
      o.ts.style.backgroundSize = (100 * EIO(P(tl, 1.0, 1.1))).toFixed(1) + "% 36%";   // coup de surligneur sur le titre
      if (o.num) { var q = P(tl, .6, .5); op(o.num, E(q)); tr(o.num, "scale(" + (1.35 - .35 * EB(q)).toFixed(3) + ") rotate(" + (-8 * (1 - E(q))).toFixed(2) + "deg)"); }
    }

    // ----- feuillets visibles et page qui tourne -----
    var vus = [];
    function montrer(p, role, th) {
      if (!p) return;
      vus.push(p);
      if (!p.vu) { p.el.style.display = "block"; p.vu = true; }
      var r = p.role !== role || role === "feuille-r" || role === "feuille-v" || role === "dessous-d" || role === "dessous-g";
      if (!r) return;
      p.role = role;
      if (role === "plat") { p.el.style.transform = ""; p.el.style.zIndex = 1; op(p.ombre, 0); return; }
      if (role === "feuille-r") {        // recto de la feuille qui tourne : la page de droite se soulève autour du dos
        p.el.style.transformOrigin = "0 50%"; p.el.style.zIndex = 3;
        p.el.style.transform = "perspective(5200px) rotateY(" + (-th).toFixed(4) + "rad)";
        p.ombre.style.background = "linear-gradient(90deg,rgba(20,16,10,.05),rgba(20,16,10,.4))"; op(p.ombre, (.9 * Math.sin(th)).toFixed(3));
      } else if (role === "feuille-v") { // verso : la future page de gauche se rabat
        p.el.style.transformOrigin = "100% 50%"; p.el.style.zIndex = 3;
        p.el.style.transform = "perspective(5200px) rotateY(" + (Math.PI - th).toFixed(4) + "rad)";
        p.ombre.style.background = "linear-gradient(270deg,rgba(20,16,10,.04),rgba(20,16,10,.28))"; op(p.ombre, (.8 * Math.sin(th)).toFixed(3));
      } else if (role === "dessous-d") {
        p.el.style.transform = ""; p.el.style.zIndex = 1;
        p.ombre.style.background = "linear-gradient(90deg,rgba(0,0,0,.55),rgba(0,0,0,0) 45%)"; op(p.ombre, (Math.sin(th) * (1 - th / Math.PI) * 1.3).toFixed(3));
      } else if (role === "dessous-g") {
        p.el.style.transform = ""; p.el.style.zIndex = 1;
        p.ombre.style.background = "linear-gradient(270deg,rgba(0,0,0,.5),rgba(0,0,0,0) 45%)"; op(p.ombre, (Math.sin(th) * (th / Math.PI) * 1.2).toFixed(3));
      }
    }
    function feuillets(t) {
      var k = 0, th = 0;
      tours.forEach(function (tr_, i) { if (t >= tr_.tb) k = i + 1; else if (t > tr_.ta && k === i) th = Math.PI * EIO(P(t, tr_.ta, tr_.tb - tr_.ta)); });
      var A = planches[k], B = planches[k + 1];
      vus = [];
      if (!th) { montrer(A.L, "plat"); montrer(A.R, "plat"); }
      else {
        if (A.L) montrer(A.L, th > Math.PI / 2 ? "dessous-g" : "plat", th);
        if (B && B.R) montrer(B.R, "dessous-d", th);
        if (th < Math.PI / 2) montrer(A.R, "feuille-r", th); else if (B) montrer(B.L, "feuille-v", th);
      }
      pages.forEach(function (p) { if (p.vu && vus.indexOf(p) < 0) { p.el.style.display = "none"; p.vu = false; p.role = null; } });
      // ombre du magazine sur la table
      var gauche = !!(A.L || (th > Math.PI / 2 && B && B.L)), droite = !!((B && th && B.R) || (A.R && th < Math.PI / 2));
      if (!th) { gauche = !!A.L; droite = !!A.R; }
      ombreMag.style.left = (gauche ? -PW : 0) + "px"; ombreMag.style.width = ((gauche ? PW : 0) + (droite ? PW : 0)) + "px";
      op(ombreMag, gauche || droite ? 1 : 0);
      return { k: k, th: th };
    }

    var sousOn = false, dernierSous = -1, arrivee = false;
    function rendu(t) {
      if (!misEnPage && policesPretes) mettreEnPage();
      var cam = camera(t);
      monde.style.transform = "translate(640px,360px) scale(" + cam[2].toFixed(5) + ") translate(" + (-cam[0]).toFixed(2) + "px," + (-cam[1]).toFixed(2) + "px)";
      feuillets(t);
      // le magazine arrive sur la table
      if (t < 1.2) {
        var a = E(P(t, 0, 1.1)), tf = "translate(" + (520 * (1 - a)).toFixed(1) + "px," + (1300 * (1 - a)).toFixed(1) + "px) rotate(" + (9 * (1 - a)).toFixed(2) + "deg)";
        une.el.style.transform = tf; ombreMag.style.transform = tf; une.role = "arrivee"; arrivee = true;
      } else if (arrivee) { if (une.role === "arrivee") { une.el.style.transform = ""; une.role = null; } ombreMag.style.transform = ""; arrivee = false; }
      if (une.chif && une.vu) { var q = P(t, .75, .5); op(une.chif, E(q)); tr(une.chif, "scale(" + (1.25 - .25 * EB(q)).toFixed(3) + ")"); }
      vus.forEach(function (p) { p.groupes.forEach(function (g) { majGroupe(g, t); }); });
      ouvs.forEach(function (o) { if (o.pg.vu) majOuverture(o, t); });
      ecrans.forEach(function (o) { majObjet(o, t); });
      fil.style.width = (W * cl(t / EP.dur, 0, 1)).toFixed(1) + "px";
      if (sousOn) {
        var k = -1;
        for (var i = 0; i < EP.sous.length; i++) { if (EP.sous[i][0] <= t && t < EP.sous[i][1]) { k = i; break; } }
        if (k !== dernierSous) { stS.textContent = k >= 0 ? EP.sous[k][2] : ""; st.style.display = k >= 0 ? "block" : "none"; dernierSous = k; }
      } else st.style.display = "none";
    }
    return { el: sc, rendu: rendu, sous: function (b) { sousOn = b; dernierSous = -2; },
      attentes: function () { return [chargePolices].concat(objs.filter(function (o) { return o.attente; }).map(function (o) { return o.attente; })); } };
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
      var t = tDe(ev); bulle.textContent = fmt(t) + " · " + nomChap(t);
      var lg = prog.getBoundingClientRect().width, bw = bulle.offsetWidth;   // la bulle reste entière au-dessus de la barre
      bulle.style.left = cl(lg * t / EP.dur, bw / 2, Math.max(bw / 2, lg - bw / 2)) + "px";
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
    var tA = Q.get("t") != null ? parseFloat(Q.get("t")) : null;
    S.rendu(3.4);   // affiche : la couverture du magazine
    if (tA != null) { aller(tA); affiche.classList.add("off"); }
    chargePolices.then(function () { if (!lecture) S.rendu(tA != null ? T : 3.4); });
    majUI(); setTimeout(hauteur, 300);
  }

  window.SERIE = { lancer: lancer };
})();
