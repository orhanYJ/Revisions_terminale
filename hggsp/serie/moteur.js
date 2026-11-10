/* Vidéos HGGSP « Ligne rouge » — moteur du lecteur, copie du moteur SVT (svt/serie/moteur.js, lui-même copie du moteur
   PC) aux couleurs du site HGGSP : salle de crise (noir, rouge signal, acier), bandeau « CONFIDENTIEL », tampons,
   dates au télétype, radar, fiches de renseignement.
   Ajouts propres à l'HGGSP :
   - scene : une scène d'animation du site (cartes et schémas de outils/specialites/hggsp/, extraites dans
     hggsp/serie/illu-<code>.js par outils/serie-hggsp/scenes.js) jouée par le temps de la vidéo : l'étape k au
     repère {id.k}, date au télétype, caméra qui zoome d'un cadrage à l'autre ;
   - chiffres : grands chiffres qui défilent jusqu'à leur valeur ;
   - chrono : frise de dates (télétype, tampons), l'événement k au repère {id.k} ;
   - document : une pièce du dossier (texte d'un document), passages surlignés au repère {id.k} ;
   - illustrations orbites (satellites en orbite) et kessler (collision et réaction en chaîne).
   Repris des moteurs PC et SVT : titre, chapitre, mot, question, def, note, liste, cols, cartes, cit, tableau,
   frappe, flash, carte (carte mentale finale), formule, graphe, exo (sujets de bac), pause (« À toi »)…
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py depuis outils/serie-hggsp/<module>.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  // palette du site en mode sombre (outils/specialites/hggsp/src/style.css) : encre, rouge signal, acier, kraft
  var C = { iv: "#dce3e8", iv2: "#93a3af", sa: "#ff5b49", sa2: "#b3241b", ca: "#ff8273", te: "#82b2d8", eau: "#6e9cc0", nuit: "#0a0f13",
    el: "#82b2d8", uv: "#b48cff", rouge: "#ff5b49", vert: "#6cc082", or: "#c2a878", kraft: "#c2a878" };

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
  function insec(s) {
    return String(s).replace(/ ([?!:;»])/g, "\u00a0$1").replace(/« /g, "«\u00a0")
      .replace(/(\d) (?=\d{3}(?!\d))/g, "$1\u00a0").replace(/(\d) (?=(%|km|m|milles|Md|h)(?![\wà-ÿ]))/g, "$1\u00a0")
      .replace(/(art\.|n°|≈) /g, "$1\u00a0");
  }
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
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(255,91,73," + (0.7 * (1 - f)).toFixed(2) + ")";
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

  // pictogrammes des cartes (type cartes, champ ic) : tracés qui se dessinent
  var ICONES = {
    vague: ["M6 40 C18 28 30 28 42 40 S66 52 78 40 S90 30 96 34", "M6 62 C18 50 30 50 42 62 S66 74 78 62 S90 52 96 56", "M6 84 C18 72 30 72 42 84 S66 96 78 84"],
    fusee: ["M50 6 C66 22 70 44 64 70 H36 C30 44 34 22 50 6 Z", "M36 58 L22 76 L36 72 M64 58 L78 76 L64 72", "M44 70 L42 90 M56 70 L58 90", "M50 30 a6 6 0 1 0 0.1 0"],
    satellite: ["M38 38 L62 62", "M40 36 L64 60 L60 64 L36 40 Z", "M30 30 L8 8 M24 36 L4 16 M36 24 L16 4", "M70 70 L92 92 M76 64 L96 84 M64 76 L84 96", "M62 30 a14 14 0 0 1 8 8 M66 18 a26 26 0 0 1 16 16"],
    balance: ["M50 10 V88 M30 88 H70", "M14 26 H86", "M14 26 L4 54 H24 Z M86 26 L76 54 H96 Z", "M50 10 a5 5 0 1 0 0.1 0"],
    drapeau: ["M24 94 V8", "M24 10 C40 2 56 18 76 10 V48 C56 56 40 40 24 48"],
    radar: ["M50 50 a40 40 0 1 0 0.1 0", "M50 50 a22 22 0 1 0 0.1 0", "M50 50 L82 26", "M50 10 V90 M10 50 H90"],
    globe: ["M50 50 a40 40 0 1 0 0.1 0", "M10 50 H90", "M50 10 C30 30 30 70 50 90 C70 70 70 30 50 10", "M18 30 H82 M18 70 H82"],
    tampon: ["M30 40 H70 V26 C70 14 30 14 30 26 Z", "M18 40 H82 V60 H18 Z", "M12 74 H88"],
    debris: ["M50 50 L80 20 M50 50 L86 58 M50 50 L60 90 M50 50 L18 78 M50 50 L14 34 M50 50 L40 8", "M76 16 l8 2 l-2 8 Z M84 54 l7 4 l-5 6 Z M14 30 l-6 6 l8 4 Z"]
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
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(255,91,73,.9)";
        op(mf.an, E(P(st.tl, 2, .5)));
      }
    };
  };

  TYPES.cols = function (o, v) {
    var e = o.el; e.classList.add("v-cols"); o.entree = "aucune";
    var g = h("div", "col g", e), d = h("div", "col d", e);
    h("div", "t", g, esc(v.g)); h("div", "q", g, esc(v.gq || "")); h("div", "t", d, esc(v.d)); h("div", "q", d, esc(v.dq || ""));
    var vs = h("div", "vs", e, esc(v.vs || "≠")); if (String(v.vs || "").length > 2) vs.style.fontSize = "32px";
    var rp = v.repere ? h("div", "rp", e, "<span>✻ " + esc(v.repere) + "</span>") : null;
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
        c.c.style.borderColor = actif ? "rgba(255,91,73," + (0.5 + 0.4 * pul) + ")" : "rgba(220,227,232,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(255,91,73,.25)" : "none";
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
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "HGGSP · Terminale · Ligne rouge");
    var radar = h("div", "g-radar", e, '<svg viewBox="0 0 260 260"><g fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="130" cy="130" r="40"/><circle cx="130" cy="130" r="80"/><circle cx="130" cy="130" r="120"/><path d="M130 0V260M0 130H260"/></g><g class="g-bras"><path d="M130 130L130 10A120 120 0 0 1 233 70Z" fill="currentColor" opacity=".35"/></g></svg>');
    var bras = radar.querySelector(".g-bras");
    var conf = h("div", "g-conf", e, "<span>Confidentiel</span>");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    tt.style.fontSize = Math.min(110, Math.floor(2300 / Math.max(12, String(v.serie).length))) + "px"; tt.style.textAlign = "center";
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, esc(dossierDe(EPI.code)));
    var balai = h("div", "g-balai", e);
    return function (t, st) {
      var tl = st.tl;
      op(halo, E(P(tl, 0, 1.5)) * (1 - E(P(tl, 4.6, 1)))); tr(halo, "scale(" + (0.7 + 0.4 * E(P(tl, 0, 5))) + ")");
      op(haut, E(P(tl, .3, .9))); haut.style.letterSpacing = (0.7 - 0.35 * E(P(tl, .3, 2))) + "em";
      tr(l1, "scaleX(" + EIO(P(tl, .6, 1.4)) + ")"); tr(l2, "scaleX(" + EIO(P(tl, .8, 1.4)) + ")");
      animLettres(sp, tl, 1.0, .07, .9, true);
      tr(tt, "scale(" + (1.08 - 0.08 * E(P(tl, 1, 4))) + ")");
      op(bas, E(P(tl, 2.2, .8)));
      op(radar, E(P(tl, 0, 1.2)) * .5); bras.setAttribute("transform", "rotate(" + (tl * 120 % 360).toFixed(1) + " 130 130)");
      var cq = P(tl, 1.6, .35); op(conf, E(cq)); tr(conf, "translate(-50%,0) rotate(-4deg) scale(" + (1.6 - .6 * EB(cq)).toFixed(3) + ")");
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
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(255,91,73,.35)";
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

  /* ---------- types propres aux sciences ---------- */

  // animation du site (pc/anim/<nom>.html) pilotée par le temps de la vidéo : segments [début, fin] de l'animation,
  // le segment k démarre au repère {id.k} et s'arrête sur sa dernière image jusqu'au repère suivant
  TYPES.anim = function (o, v) {
    var e = o.el; e.classList.add("v-anim");
    var hh = v.h || 600, ww = Math.round(hh * 400 / 430);
    e.style.left = (v.x != null ? v.x : 50) + "px"; e.style.top = (v.y != null ? v.y : 84) + "px";
    e.style.width = ww + "px"; e.style.height = hh + "px";
    var cad = h("div", "an-cadre", e), fr = h("iframe", "", cad);
    fr.setAttribute("title", "Animation"); fr.setAttribute("scrolling", "no"); fr.setAttribute("aria-hidden", "true"); fr.tabIndex = -1;
    var et_ = h("div", "an-et", e, "Animation");
    var pret = false;
    o.attente = new Promise(function (r) {
      fr.addEventListener("load", function () {
        var n = 0, k = setInterval(function () {
          n++;
          try { if (fr.contentWindow.ANIM && fr.contentWindow.ANIM.regler) { pret = true; clearInterval(k); r(); return; } } catch (err) { clearInterval(k); r(); return; }
          if (n > 200) { clearInterval(k); r(); }
        }, 30);
      });
    });
    fr.src = "../anim/" + v.nom + ".html?pilote=1&theme=dark";
    var seg = v.seg || [[0, 1e9]], vit = v.vit || 1, dernier = null;
    return function (t, st) {
      op(et_, E(P(st.tl, .5, .6)) * .85);
      if (!pret) return;
      var debut = v.t0, k = -1, tk = v.t0;
      for (var i = 0; i < seg.length; i++) {
        var c = v.et && v.et[String(i + 1)] != null ? v.et[String(i + 1)] : (i === 0 ? v.t0 : debut + (seg[i - 1][1] - seg[i - 1][0]) / vit);
        debut = c;
        if (t >= c) { k = i; tk = c; }
      }
      var ta = k < 0 ? seg[0][0] : Math.min(seg[k][1], seg[k][0] + (t - tk) * vit);
      ta = Math.round(ta * 60) / 60;
      if (ta !== dernier) { dernier = ta; try { fr.contentWindow.ANIM.regler(ta, v.opt || 0); } catch (err) {} }
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
    if (v.plus) h("div", "badge", c, "Hors programme");
    return function (t, st) {
      if (te) op(te, E(P(st.tl, .05, .5)));
      ls.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .25 + i * 1.1), p = E(P(t, t1, .55));
        op(x.d, p); tr(x.d, "translateY(" + (14 * (1 - p)).toFixed(1) + "px)");
        x.d.style.filter = p < 1 ? "blur(" + ((1 - p) * 5).toFixed(1) + "px)" : "none";
        if (x.l.cadre) {
          var q = P(t, t1 + .45, .9), g = Math.max(0, Math.sin((t - t1) * 2.2)) * (t > t1 + 1.3 ? .25 : 0);
          x.d.style.boxShadow = "0 0 0 2px rgba(255,91,73," + (.85 * E(q)).toFixed(2) + "),0 0 " + (34 * (1 - q) + 14 + 10 * g).toFixed(0) + "px rgba(255,91,73," + (.32 * E(q) + .1 * g).toFixed(2) + ")";
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
      grille.push(sv("line", { x1: X(x), x2: X(x), y1: m[2], y2: m[2] + ph, stroke: "rgba(220,227,232,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x), Y(y0) + 12, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("line", { x1: m[0], x2: m[0] + pw, y1: Y(y), y2: Y(y), stroke: "rgba(220,227,232,.09)", "stroke-width": 1 }, fond));
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
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col, stroke: "#040c08", "stroke-width": 1.5 }, g);
        });
        if (d.proj) {
          x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 1.6, "stroke-dasharray": "5 5", fill: "none", opacity: .8 }, g);
        }
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "rect" || d.type === "balaye") {
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: col, "fill-opacity": .22, stroke: col, "stroke-width": 2 }, g);
        x.pt = sv("circle", { r: 8, fill: col, stroke: "#040c08", "stroke-width": 1.5 }, g);
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
  var NIVEAUX = { simple: ["Exercice · pour démarrer", "#6cc082"], difficile: ["Exercice · plus difficile", "#c2a878"], bac: ["Exercice · type bac", "#ff8273"],
    dissert: ["Sujet de dissertation", "#ff5b49"], etude: ["Étude critique de document", "#82b2d8"] };
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
    var so = h("div", "pa-so", c, esc(v.sous || "Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la solution."));
    return function (t, st) {
      var tl = st.tl, a = E(P(tl, 0, .6));
      op(c, a); tr(c, "translateY(" + (24 * (1 - a)) + "px) scale(" + (0.95 + 0.05 * EB(P(tl, 0, .7))) + ")");
      tr(ic, "scale(" + (0.6 + 0.4 * EB(P(tl, .2, .6))) + ")");
      var r = (tl % 1.6) / 1.6; op(an, (1 - r) * .7); tr(an, "scale(" + (1 + r * .4) + ")");   // l'anneau ne touche plus le libellé « À toi »
      op(te, E(P(tl, .3, .5))); op(tx, E(P(tl, .5, .6))); op(so, E(P(tl, 1, .6)) * .9);
    };
  };

  /* ---------- types propres à l'HGGSP ---------- */

  // date au télétype : les caractères de txt s'écrivent un à un à partir de t0 (curseur ▌ tant que ce n'est pas fini)
  function teletype(txt, t, t0, pas) {
    var n = Math.floor((t - t0) / (pas || .045));
    if (n <= 0) return "";
    return n >= txt.length ? txt : txt.slice(0, n) + "▌";
  }

  // scène du site (carte ou schéma) jouée par le temps : window.HG_SCENES[v.anim] (hggsp/serie/illu-<code>.js).
  // Étapes : celles du site (v.pas = [indices du site, de 0] pour en garder une partie) ou v.etapes ; l'étape k
  // (de 1) commence au repère {id.k}. État cumulé comme sur le site (montre / cache), accent = pulsation.
  // v.cam = { "0": [x, y, w, h], "3": […] } : cadrage avant l'étape 1 (clé 0) et à partir de l'étape k (vol de 1,6 s).
  // v.fs : taille d'écran des étiquettes en px (20 par défaut) ; v.legende = false : pas de bande date / titre.
  TYPES.scene = function (o, v) {
    var e = o.el; e.classList.add("v-scene"); o.prof = .25;
    var S = (window.HG_SCENES || {})[v.anim];
    var x0 = v.x != null ? v.x : 60, y0 = v.y != null ? v.y : 92, ww = v.w || 1160, hh = v.h || 500;
    e.style.left = x0 + "px"; e.style.top = y0 + "px"; e.style.width = ww + "px";
    var cad = h("div", "sc-cadre", e); cad.style.height = hh + "px";
    if (!S) { h("div", "sc-manque", cad, "scène absente : " + esc(v.anim)); return function () {}; }
    var svg = sv("svg", { viewBox: (S.vb || [0, 0, S.w, S.h]).join(" "), preserveAspectRatio: "xMidYMid meet" }, cad);
    svg.innerHTML = (S.fond === "monde" && window.HG_FONDS ? HG_FONDS.monde : "") + S.svg;
    var ets = v.etapes || (v.pas ? v.pas.map(function (i) { return S.etapes[i]; }) : S.etapes);
    // états cumulés (avant l'étape 1 : rien de ce qui est animé n'est visible)
    var base = {};
    if (v.pas && v.pas[0] > 0 && !v.etapes) {           // on part au milieu des étapes du site : l'état d'avant compte
      for (var b = 0; b < v.pas[0]; b++) { (S.etapes[b].montre || []).forEach(function (x) { base[x] = 1; }); (S.etapes[b].cache || []).forEach(function (x) { delete base[x]; }); }
    }
    if (v.depart) v.depart.forEach(function (x) { base[x] = 1; });
    var etats = [base];
    ets.forEach(function (et_, i) {
      var s = {}; Object.keys(etats[i]).forEach(function (k) { s[k] = 1; });
      (et_.montre || []).forEach(function (x) { s[x] = 1; }); (et_.cache || []).forEach(function (x) { delete s[x]; });
      etats.push(s);
    });
    var els = Array.prototype.slice.call(svg.querySelectorAll("[data-k]")).map(function (el) {
      var traces = el.classList.contains("trace") ? [el] : Array.prototype.slice.call(el.querySelectorAll(".trace"));
      traces.forEach(function (p) { if (!p.getAttribute("pathLength")) p.setAttribute("pathLength", "1"); p.style.strokeDasharray = "1 1"; });
      return { el: el, k: el.getAttribute("data-k"), tr: traces };
    });
    // caméra
    var vb0 = S.vb || [0, 0, S.w, S.h], cams = [];
    for (var c = 0; c <= ets.length; c++) cams.push((v.cam && v.cam[String(c)]) || (c ? cams[c - 1] : vb0));
    var bande = v.legende === false ? null : h("div", "sc-bande", e);
    var dEl = bande ? h("span", "sc-date", bande) : null, tEl = bande ? h("span", "sc-titre", bande) : null, nEl = bande ? h("span", "sc-num", bande) : null;
    if (S.source && v.source !== false) h("div", "sc-src", e, esc(v.source || S.source));
    var fs = v.fs || 20, dernierVb = "";
    function tk(i) { return et(v, String(i), .6 + (i - 1) * 3); }
    return function (t, st) {
      var k = 0;
      for (var i = 1; i <= ets.length; i++) if (t >= tk(i)) k = i;
      var tK = k ? tk(k) : v.t0;
      // caméra : vol de cams[k-1] à cams[k]
      var a = cams[k ? k - 1 : 0], b = cams[k], u = k ? EIO(P(t, tK, v.vol || 1.6)) : 1;
      var vb = [0, 1, 2, 3].map(function (j) { return a[j] + (b[j] - a[j]) * u; });
      var key = vb.map(function (x) { return x.toFixed(1); }).join(" ");
      if (key !== dernierVb) { svg.setAttribute("viewBox", key); dernierVb = key; }
      var ech = Math.min(ww / vb[2], hh / vb[3]);
      svg.style.setProperty("--kf", (1 / ech).toFixed(4));
      svg.style.setProperty("--kfs", (fs / 20).toFixed(3));
      var acc = {}; ((ets[k - 1] || {}).accent || []).forEach(function (x) { acc[x] = 1; });
      els.forEach(function (x) {
        var on = !!etats[k][x.k], av = k ? !!etats[k - 1][x.k] : false, p;
        if (on) {
          var s0 = k; while (s0 > 0 && etats[s0 - 1][x.k]) s0--;          // étape où l'élément est apparu
          var ta = s0 ? tk(s0) : v.t0;
          p = s0 === 0 && !v.pas && !v.depart ? 1 : E(P(t, ta, .7));
          x.tr.forEach(function (pp) { pp.style.strokeDashoffset = (1 - EIO(P(t, ta, 1.4))).toFixed(4); });
          var pul = acc[x.k] ? .5 + .5 * Math.cos((t - tK) * 4.2) : 0;
          x.el.style.opacity = (p * (1 - .18 * pul)).toFixed(3);
          x.el.style.filter = acc[x.k] ? "drop-shadow(0 0 " + (2 + 5 * pul).toFixed(1) + "px rgba(255,91,73,.85))" : "none";
        } else if (av) {
          x.el.style.opacity = (1 - E(P(t, tK, .5))).toFixed(3); x.el.style.filter = "none";
        } else { x.el.style.opacity = 0; x.el.style.filter = "none"; }
      });
      if (bande) {
        var e_ = ets[k - 1];
        op(bande, k ? E(P(t, tk(1), .5)) : 0);
        if (e_) {
          var txt = teletype(e_.date || "", t, tK + .1);
          if (dEl.textContent !== txt) dEl.textContent = txt;
          dEl.style.display = e_.date ? "" : "none";
          var ti = esc(e_.titre || "");
          if (tEl._t !== ti) { tEl.innerHTML = ti; tEl._t = ti; }
          op(tEl, E(P(t, tK + .3, .5)));
          nEl.textContent = ets.length > 1 ? "ÉTAPE " + k + " / " + ets.length : "";
        }
      }
    };
  };

  // grands chiffres : items [{v: 71, dec: 0, avant: "", apres: " %", t: "légende", src: "source", jauge: 0.71}],
  // l'item k au repère {id.k} ; le nombre défile jusqu'à sa valeur, la jauge se remplit
  function nombre(x, dec) {
    var s = x.toFixed(dec || 0).replace(".", ","), p = s.split(",");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return p.join(",");
  }
  TYPES.chiffres = function (o, v) {
    var e = o.el; e.classList.add("v-chiffres"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 90) + "px"; e.style.top = (v.y != null ? v.y : 150) + "px"; e.style.width = (v.w || 1100) + "px";
    if (v.titre) h("div", "ch-ti", e, esc(v.titre));
    var rg = h("div", "ch-rang", e), n = v.items.length;
    var its = v.items.map(function (it) {
      var c = h("div", "ch-it", rg); c.style.width = (100 / n) + "%";
      var nb = h("div", "ch-nb", c); if (it.taille) nb.style.fontSize = it.taille + "px"; else if (n === 1) nb.style.fontSize = "150px";
      var tx = h("div", "ch-tx", c, esc(it.t || ""));
      var jg = it.jauge != null ? h("div", "ch-jauge", c) : null, jr = jg ? h("div", "ch-jr", jg) : null;
      var src = it.src ? h("div", "ch-src", c, esc(it.src)) : null;
      return { it: it, c: c, nb: nb, tx: tx, jr: jr, src: src };
    });
    return function (t, st) {
      its.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .2 + i * .9), p = E(P(t, t1, .6)), q = EIO(P(t, t1, 1.4));
        op(x.c, p); tr(x.c, "translateY(" + (30 * (1 - p)).toFixed(1) + "px)");
        var it = x.it, val = typeof it.v === "number" ? (it.de || 0) + (it.v - (it.de || 0)) * q : null;
        x.nb.innerHTML = '<span class="ch-av">' + esc(it.avant || "") + "</span>" + (val == null ? esc(it.v) : nombre(val, it.dec)) + '<span class="ch-ap">' + esc(it.apres || "") + "</span>";
        x.nb.style.textShadow = "0 0 " + (26 * (1 - P(t, t1 + 1.2, .8))).toFixed(1) + "px rgba(255,91,73,.55)";
        op(x.tx, E(P(t, t1 + .5, .6)));
        if (x.jr) x.jr.style.width = (100 * it.jauge * EIO(P(t, t1 + .2, 1.6))).toFixed(2) + "%";
        if (x.src) op(x.src, E(P(t, t1 + 1, .6)) * .85);
      });
    };
  };

  // frise de dates : items [{d: "1982", t: "Montego Bay", c: "mer" | "espace" | "droit" | "conflit"}], l'événement k
  // au repère {id.k} (date au télétype, tampon) ; dates à espacement régulier, en alternance au-dessus et au-dessous
  var CATS = { mer: "#6e9cc0", espace: "#b48cff", droit: "#c2a878", conflit: "#ff5b49", prive: "#6cc082" };
  TYPES.chrono = function (o, v) {
    var e = o.el; e.classList.add("v-chrono"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 60) + "px"; e.style.top = (v.y != null ? v.y : 120) + "px"; e.style.width = (v.w || 1160) + "px";
    var hh = v.h || 470; e.style.height = hh + "px";
    if (v.titre) h("div", "chr-ti", e, esc(v.titre));
    var axe = h("div", "chr-axe", e); axe.style.top = (hh / 2) + "px";
    var n = v.items.length, pas = (v.w || 1160) / n;
    var its = v.items.map(function (it, i) {
      var haut = i % 2 === 0, p = h("div", "chr-p " + (haut ? "haut" : "bas"), e);
      p.style.left = (pas * (i + .5)) + "px"; p.style.top = (hh / 2) + "px"; p.style.width = Math.min(250, pas * 1.75) + "px";
      var col = CATS[it.c] || C.sa;
      var pt = h("div", "chr-pt", p); pt.style.background = col;
      var tige = h("div", "chr-tige", p); tige.style.background = col;
      var bloc = h("div", "chr-bloc", p), d = h("div", "chr-d", bloc), tx = h("div", "chr-t", bloc, esc(it.t));
      d.style.color = col;
      return { p: p, pt: pt, tige: tige, bloc: bloc, d: d, tx: tx, it: it };
    });
    return function (t, st) {
      tr(axe, "scaleX(" + EIO(P(st.tl, 0, 1.2)) + ")");
      var dernier = -1;
      its.forEach(function (x, i) { if (t >= et(v, String(i + 1), .6 + i * .7)) dernier = i; });
      its.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .6 + i * .7), p = P(t, t1, .5);
        op(x.p, t >= t1 ? 1 : 0);
        tr(x.pt, "translate(-50%,-50%) scale(" + (EB(p) * (i === dernier ? 1.25 + .1 * Math.sin((t - t1) * 4) : 1)).toFixed(3) + ")");
        tr(x.tige, "scaleY(" + E(P(t, t1 + .1, .4)).toFixed(3) + ")");
        var q = E(P(t, t1 + .25, .5)); op(x.bloc, q * (dernier < 0 || i === dernier || !v.et ? 1 : .55));
        var txt = teletype(x.it.d, t, t1 + .15);
        if (x.d.textContent !== txt) x.d.textContent = txt;
      });
    };
  };

  // document (pièce du dossier) : v.ref (source), v.titre, v.paras [texte…] ; v.marques [extrait…] : l'extrait k est
  // surligné au repère {id.k} ; v.mode = "coin" : la pièce se range à gauche, en plus petit, pendant la correction
  TYPES.document = function (o, v) {
    var e = o.el; e.classList.add("v-document"); if (v.mode === "coin") e.classList.add("coin");
    if (v.mode !== "coin") { e.style.left = (v.x != null ? v.x : 150) + "px"; e.style.top = (v.y != null ? v.y : 86) + "px"; e.style.width = (v.w || 980) + "px"; }
    var c = h("div", "doc-feuille", e);
    h("div", "doc-tampon", c, esc(v.piece || "Pièce n° 1"));
    if (v.titre) h("div", "doc-ti", c, esc(v.titre));
    var corps = h("div", "doc-corps", c); if (v.taille) corps.style.fontSize = v.taille + "px";
    var marques = v.marques || [], spans = [];
    (v.paras || []).forEach(function (para) {
      var pe = h("p", "", corps), reste = para, html = "";
      // découpe du paragraphe autour des extraits à surligner (dans l'ordre où ils apparaissent)
      while (reste.length) {
        var best = -1, bi = -1;
        marques.forEach(function (m, i) { var j = reste.indexOf(m); if (j >= 0 && (best < 0 || j < best)) { best = j; bi = i; } });
        if (bi < 0) { html += esc(reste); break; }
        html += esc(reste.slice(0, best)) + '<span class="doc-mq" data-i="' + bi + '">' + esc(marques[bi]) + "</span>";
        reste = reste.slice(best + marques[bi].length);
      }
      pe.innerHTML = html;
      Array.prototype.forEach.call(pe.querySelectorAll(".doc-mq"), function (s) { spans.push(s); });
    });
    if (v.ref) h("div", "doc-ref", c, esc(v.ref));
    return function (t, st) {
      spans.forEach(function (s) {
        var i = +s.getAttribute("data-i"), t1 = et(v, String(i + 1), 1e9), p = EIO(P(t, t1, .7));
        s.style.backgroundSize = (100 * p).toFixed(1) + "% 100%";
        s.classList.toggle("vif", t >= t1 && t < t1 + 2.2);
      });
    };
  };

  // les orbites terrestres : {id.1} orbite basse (essaim de satellites), {id.2} orbite moyenne (positionnement),
  // {id.3} orbite géostationnaire (le satellite tourne avec la Terre et paraît immobile) ; distances non proportionnelles
  ILLU.orbites = function (s, v) {
    var W_ = v.w, H_ = v.h, cx = W_ * .3, cy = H_ * .5, g = sv("g", {}, s), R = { T: 86, b: 132, m: 196, g: 262 };
    var terre = sv("g", {}, g);
    sv("circle", { cx: cx, cy: cy, r: R.T, fill: "#2d5675" }, terre);
    var mer = sv("path", { d: "", fill: "none", stroke: "rgba(220,227,232,.3)", "stroke-width": 1.4 }, terre);
    var repere = sv("line", { x1: cx, y1: cy, x2: cx, y2: cy - R.T, stroke: C.or, "stroke-width": 3, "stroke-linecap": "round" }, terre);
    etiquette(terre, cx, cy + 9, "Terre", { fs: 24, c: C.iv, fw: 700 });
    var COL = { b: C.te, m: C.vert, g: C.sa }, orb = {}, sats = {};
    // étiquettes en colonne à droite, reliées à leur orbite par un trait
    var LAB = { g: [-48, cy - 150, "Géostationnaire : 35 786 km", v.lg || "télécoms, météo : le satellite paraît immobile"],
                m: [0, cy, "Moyenne : vers 20 000 km", v.lm || "positionnement : GPS, Galileo, Beidou"],
                b: [42, cy + 150, "Basse : 200 à 2 000 km", v.lb || "stations, observation, constellations Internet"] };
    var xl = cx + R.g + 70, lb = [], ss = [], tiges = [];
    ["b", "m", "g"].forEach(function (k) {
      var gg = sv("g", {}, g);
      orb[k] = { g: gg, c: sv("circle", { cx: cx, cy: cy, r: R[k], fill: "none", stroke: COL[k], "stroke-width": 2.6, "stroke-dasharray": k === "b" ? "0" : "8 6" }, gg) };
      var L = LAB[k], an = L[0] * Math.PI / 180, px = cx + R[k] * Math.cos(an), py = cy + R[k] * Math.sin(an);
      tiges.push(sv("path", { d: "M" + px.toFixed(1) + " " + py.toFixed(1) + " L" + (xl - 14) + " " + L[1], stroke: COL[k], "stroke-width": 1.6, fill: "none", opacity: .7 }, gg));
      sv("circle", { cx: px.toFixed(1), cy: py.toFixed(1), r: 4, fill: COL[k] }, gg);
      lb.push(etiquette(gg, xl, L[1] - 4, L[2], { fs: 27, c: COL[k], ancre: "start", fw: 700 }));
      ss.push(etiquette(gg, xl, L[1] + 26, L[3], { fs: 21, c: C.iv2, ancre: "start", fw: 500 }));
    });
    var nB = 30; sats.b = []; for (var i = 0; i < nB; i++) sats.b.push(sv("rect", { width: 7, height: 7, rx: 1.5, fill: C.te }, orb.b.g));
    sats.m = []; for (var j = 0; j < 4; j++) sats.m.push(sv("rect", { width: 11, height: 11, rx: 2, fill: C.vert }, orb.m.g));
    sats.g = sv("rect", { width: 16, height: 16, rx: 2, fill: C.sa }, orb.g.g);
    var lien = sv("line", { stroke: C.sa, "stroke-width": 1.6, "stroke-dasharray": "4 5" }, orb.g.g);
    var note = etiquette(g, cx, H_ - 4, "distances non proportionnelles", { fs: 17, c: C.iv2 });
    return function (t, st) {
      var tl = st.tl, rot = t * .25;               // rotation de la Terre (accélérée)
      op(terre, E(P(tl, 0, .6)));
      var d = ""; for (var a = 0; a < 6; a++) { var an = rot + a * Math.PI / 3, sx = Math.sin(an); if (Math.cos(an) < 0) continue; d += "M" + cx + " " + (cy - R.T) + " Q" + (cx + R.T * 1.3 * sx).toFixed(1) + " " + cy + " " + cx + " " + (cy + R.T); }
      mer.setAttribute("d", d);
      repere.setAttribute("x2", (cx + R.T * Math.cos(rot - Math.PI / 2)).toFixed(1)); repere.setAttribute("y2", (cy + R.T * Math.sin(rot - Math.PI / 2)).toFixed(1));
      ["b", "m", "g"].forEach(function (k, i) {
        var t1 = et(v, String(i + 1), .6 + i * 1.6), p = E(P(t, t1, .6));
        op(orb[k].g, p); trace(orb[k].c, EIO(P(t, t1, 1.2))); trace(tiges[i], P(t, t1 + .6, .6));
        op(lb[i], E(P(t, t1 + .8, .5))); op(ss[i], E(P(t, t1 + 1.1, .5)));
      });
      sats.b.forEach(function (r, i) {
        var an = t * 1.6 + i * 2 * Math.PI / nB + .2 * Math.sin(i * 7), rr = R.b + (alea(i) - .5) * 10;
        r.setAttribute("x", (cx + rr * Math.cos(an) - 3.5).toFixed(1)); r.setAttribute("y", (cy + rr * Math.sin(an) - 3.5).toFixed(1));
      });
      sats.m.forEach(function (r, i) {
        var an = t * .55 + i * Math.PI / 2;
        r.setAttribute("x", (cx + R.m * Math.cos(an) - 5.5).toFixed(1)); r.setAttribute("y", (cy + R.m * Math.sin(an) - 5.5).toFixed(1));
      });
      var ag = rot - Math.PI / 2, gx = cx + R.g * Math.cos(ag), gy = cy + R.g * Math.sin(ag);
      sats.g.setAttribute("x", (gx - 8).toFixed(1)); sats.g.setAttribute("y", (gy - 8).toFixed(1));
      lien.setAttribute("x1", (cx + R.T * Math.cos(ag)).toFixed(1)); lien.setAttribute("y1", (cy + R.T * Math.sin(ag)).toFixed(1));
      lien.setAttribute("x2", gx.toFixed(1)); lien.setAttribute("y2", gy.toFixed(1));
      op(note, E(P(tl, 1, .6)) * .8);
    };
  };

  // collision en orbite et réaction en chaîne (syndrome de Kessler) : des satellites sur leurs orbites ;
  // {id.1} deux satellites se percutent (débris) ; {id.2} les débris en frappent d'autres : la cascade
  ILLU.kessler = function (s, v) {
    var W_ = v.w, H_ = v.h, g = sv("g", {}, s), cx = W_ / 2, cy = H_ + 520, RT = 600;
    sv("circle", { cx: cx, cy: cy, r: RT, fill: "#16212a", stroke: "#2d5675", "stroke-width": 3 }, g);
    var ORB = [RT + 90, RT + 150, RT + 210];
    ORB.forEach(function (r) { sv("circle", { cx: cx, cy: cy, r: r, fill: "none", stroke: "rgba(220,227,232,.14)", "stroke-width": 1.4, "stroke-dasharray": "5 7" }, g); });
    function pos(r, a) { return [cx + r * Math.sin(a), cy - r * Math.cos(a)]; }
    // satellites : orbite, angle de départ, vitesse (rad/s) ; 0 et 1 se croisent au premier repère
    var k1 = et(v, "1", 2.5), k2 = et(v, "2", 6.5), D1 = v.t0, wc = .7 / Math.max(2, k1 - D1);   // les deux satellites partent à ±0,7 rad
    var SAT = [{ o: 1, w: wc, nom: v.n1 || "Iridium 33" }, { o: 1, w: -wc, nom: v.n2 || "Kosmos 2251" },
      { o: 0, w: .045 }, { o: 2, w: -.035 }, { o: 0, w: -.04 }, { o: 2, w: .04 }];
    SAT.forEach(function (st_, i) { st_.a0 = i < 2 ? -st_.w * (k1 - D1) : (alea(i * 3) - .5) * 1.4; st_.el = sv("g", {}, g);
      sv("rect", { x: -9, y: -6, width: 18, height: 12, rx: 2, fill: i < 2 ? C.te : C.iv2 }, st_.el);
      sv("path", { d: "M-22 0 H22", stroke: i < 2 ? C.te : C.iv2, "stroke-width": 4 }, st_.el);
      if (st_.nom) st_.lb = etiquette(g, 0, 0, st_.nom, { fs: 20, c: C.iv }); });
    var flash = sv("circle", { r: 10, fill: "rgba(255,210,150,.9)" }, g);
    var N = 90, deb = []; for (var d = 0; d < N; d++) deb.push({ el: sv("circle", { r: 2.2, fill: C.sa }, g), o: alea(d + 9) < .5 ? 1 : (alea(d + 3) < .5 ? 0 : 2), w: (alea(d) - .5) * .22, dr: (alea(d + 50) - .5) * 30, vague: d < 40 ? 1 : 2 });
    var t1 = etiquette(g, cx, 60, v.l1 || "10 février 2009 : première collision accidentelle", { fs: 26, c: C.sa, fw: 700 });
    var t2 = etiquette(g, cx, 100, v.l2 || "les débris en frappent d'autres : la réaction en chaîne", { fs: 22, c: C.iv });
    return function (t, st) {
      var col = t >= k1, casc = t >= k2;
      SAT.forEach(function (st_, i) {
        var a = st_.a0 + st_.w * (t - D1), p = pos(ORB[st_.o], a), detruit = (i < 2 && col) || (i >= 2 && casc && i % 2 === 0 && t > k2 + (i - 2) * .6);
        st_.el.setAttribute("transform", "translate(" + p[0].toFixed(1) + "," + p[1].toFixed(1) + ") rotate(" + (a * 57.3).toFixed(1) + ")");
        op(st_.el, detruit ? 0 : E(P(st.tl, .2, .6)));
        if (st_.lb) { st_.lb.setAttribute("x", p[0].toFixed(1)); st_.lb.setAttribute("y", (p[1] - 30).toFixed(1)); op(st_.lb, detruit ? 0 : E(P(st.tl, .5, .6)) * cl(Math.abs(a) / .22, 0, 1)); }   // les deux noms s'effacent à l'approche
      });
      var pc = pos(ORB[1], 0), fl = P(t, k1, .8);
      flash.setAttribute("cx", pc[0].toFixed(1)); flash.setAttribute("cy", pc[1].toFixed(1)); flash.setAttribute("r", (10 + 60 * fl).toFixed(1));
      op(flash, col ? (1 - fl) * .9 : 0);
      deb.forEach(function (b, i) {
        var td = b.vague === 1 ? k1 : k2 + (i % 4) * .6;
        if (t < td) { op(b.el, 0); return; }
        var u = t - td, r = ORB[b.vague === 1 ? 1 : b.o] + b.dr * Math.min(1, u / 2), a = b.w * u + (b.vague === 1 ? 0 : (alea(i) - .5) * 1.2) + (alea(i + 7) - .5) * .02;
        var p = pos(r, a); b.el.setAttribute("cx", p[0].toFixed(1)); b.el.setAttribute("cy", p[1].toFixed(1)); op(b.el, Math.min(1, u * 3));
      });
      op(t1, E(P(t, k1 + .4, .6))); op(t2, E(P(t, k2 + .3, .6)));
    };
  };

  /* ---------- scène ---------- */
  var FONDS = {
    // salle de crise (défaut), océan (bleu profond), orbite (nuit étoilée), archive (dossier kraft) ; nuit = crise
    crise: { base: "linear-gradient(160deg,#07090b 0%,#10161b 55%,#080a0c 100%)", lueurs: ["rgba(255,91,73,.16)", "rgba(130,178,216,.10)", "rgba(255,91,73,.07)"] },
    ocean: { base: "linear-gradient(170deg,#050d14 0%,#0b2232 55%,#06111a 100%)", lueurs: ["rgba(110,156,192,.22)", "rgba(130,178,216,.12)", "rgba(255,91,73,.08)"] },
    orbite: { base: "linear-gradient(160deg,#05060a 0%,#0e1220 55%,#06070c 100%)", lueurs: ["rgba(130,178,216,.16)", "rgba(180,140,255,.10)", "rgba(255,91,73,.08)"] },
    archive: { base: "linear-gradient(160deg,#0e0c09 0%,#1d1a14 55%,#0f0d0a 100%)", lueurs: ["rgba(194,168,120,.18)", "rgba(255,91,73,.10)", "rgba(130,178,216,.08)"] }
  };
  FONDS.nuit = FONDS.crise;
  // nom du dossier d'après le code de l'épisode : hggsp-t1-intro → « Thème 1 · introduction »
  var EPI = { code: "" };
  function dossierDe(code) {
    var m = /t(\d)-(intro|a1|a2|otc)/.exec(code || "");
    if (!m) return "HGGSP";
    return "Thème " + m[1] + " · " + { intro: "introduction", a1: "axe 1", a2: "axe 2", otc: "objet de travail conclusif" }[m[2]];
  }

  function Scene(EP, racine) {
    var sc = h("div", "scene", racine);
    EPI.code = EP.code;
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
    h("div", "grille", sc);
    var cv = h("canvas", "poussiere", sc); cv.width = W; cv.height = H;
    var cx = cv.getContext("2d");
    var parts = []; for (var i = 0; i < 70; i++) parts.push({ x: alea(i) * W, y: alea(i + 100) * H, vx: (alea(i + 200) - .5) * 14, vy: 6 + alea(i + 300) * 16, r: .8 + alea(i + 400) * 2, ph: alea(i + 500) * 6.28 });
    var couche = h("div", "", sc); couche.style.cssText = "position:absolute;inset:0";
    h("div", "voile", sc);
    var ent = h("div", "entete", sc), fil = h("div", "fil", sc), st = h("div", "st", sc), stS = h("span", "", st);
    // illustrations propres à la vidéo (hggsp/serie/illu-<code>.js) : SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; }
    if (window.SERIE_ILLU) Object.keys(window.SERIE_ILLU).forEach(function (k) { ILLU[k] = window.SERIE_ILLU[k]; });
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
        cx.fillStyle = "rgba(190,214,232," + a.toFixed(3) + ")";
        cx.beginPath(); cx.arc(x, y, p.r, 0, 6.283); cx.fill();
      });
      // visuels
      var plein = false;
      objs.forEach(function (o) {
        var v = o.v;
        if (t < v.t0 || t > v.t1 + (v.type === "tableau" ? 1 : .45)) { if (o.vis) { o.el.style.display = "none"; o.vis = false; } return; }
        if (!o.vis) { o.el.style.display = o.disp; o.vis = true; }
        if (v.type === "titre" || v.type === "chapitre" || v.type === "generique") plein = true;
        var a = E(P(t, v.t0, .7)), out = EIO(P(t, v.t1, v.type === "tableau" ? .6 : .35));   // sortie courte : pas de fantôme sous le visuel suivant
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
      ent.innerHTML = esc(dossierDe(EP.code)) + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
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
    document.title = EP.titre + " · " + dossierDe(EP.code) + " · HGGSP Terminale";
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
      h("span", "k", tete, "HGGSP Terminale · " + dossierDe(EP.code));
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
    bPA.title = "Arrêt automatique avant chaque solution d'exercice";
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
    var bandeau = h("div", "arret", cadre, '<span class="ic">' + ICO.pause + '</span><span><b>À toi.</b> La vidéo attend ta réponse : cherche, puis touche l\'image pour la solution.</span>');
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
        navigator.mediaSession.metadata = new MediaMetadata({ title: EP.titre, artist: "HGGSP Terminale · " + dossierDe(EP.code), album: "Terminale spécialité" });
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
  // outils du moteur, pour les illustrations écrites à part (hggsp/serie/illu-<code>.js)
  window.SERIE_OUTILS = { W: W, H: H, C: C, h: h, sv: sv, cl: cl, E: E, EIO: EIO, EB: EB, P: P, op: op, tr: tr, trace: trace, et: et, etiquette: etiquette, esc: esc, alea: alea };
})();
