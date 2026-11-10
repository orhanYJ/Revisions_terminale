/* Moteur des animations explicatives.
   Une animation se déclare dans un fichier de données :
     ANIMS["id"] = {
       t: "Titre",                       // affiché au-dessus de la scène
       h: 300,                           // hauteur de la scène (largeur fixe : 360)
       src: "Source : …",                // facultatif, sous la scène
       etapes: [{ l: "légende de l'étape", d: 4 }, …],   // d = durée en secondes (3,5 par défaut)
       rendu: function (A, i, p) { return "<svg…>" }      // i = étape (0…n−1), p = avancement 0…1 de l'étape
     };
   et se place dans le cours par <div data-anim="id"></div>.
   rendu est une fonction pure : elle dessine tout l'état à l'instant (i, p). Les étapes antérieures sont
   considérées comme terminées (p = 1). Outils A : voir plus bas (A.s, A.t, A.boite, A.fl, A.pl, A.axes…).
   Sans mouvement (prefers-reduced-motion), chaque étape s'affiche directement terminée. */
var ANIM_MOTEUR = (function () {
  "use strict";
  var W = 360;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fr(n, d) {
    if (!isFinite(n)) return "—";
    var s = Math.abs(n).toFixed(d === undefined ? 1 : d), p = s.split(".");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (n < 0 && +s !== 0 ? "−" : "") + p.join(",");
  }
  var ctx = null, famille = "";
  function larg(t, taille, gras) {
    if (!ctx) { ctx = document.createElement("canvas").getContext("2d"); famille = getComputedStyle(document.body).fontFamily; }
    ctx.font = (gras ? "700 " : "") + taille + "px " + famille; return ctx.measureText(t).width;
  }
  function couper(t, w, taille, gras) {
    var out = [], cur = "";
    String(t).split(" ").forEach(function (m) {
      var e = cur ? cur + " " + m : m;
      if (larg(e, taille, gras) > w && cur) { out.push(cur); cur = m; } else cur = e;
    });
    if (cur) out.push(cur);
    return out;
  }
  function borne(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function ease(p) { p = borne(p); return p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; }
  var COUL = { canard: "var(--canard)", corail: "var(--corail)", moutarde: "var(--moutarde)", encre: "var(--encre)", gris: "var(--encre2)", vert: "var(--vert)", ligne: "var(--ligne)", carte: "var(--carte)", papier: "var(--papier)", canardc: "var(--canard-c)", corailc: "var(--corail-c)", moutardec: "var(--moutarde-c)", carte2: "var(--carte2)" };
  function c(n) { return COUL[n] || n; }

  var A = {
    W: W, fr: fr, esc: esc,
    /* avancement d'un sous-intervalle [a, b] de p, adouci */
    s: function (p, a, b) { return ease((p - a) / ((b === undefined ? 1 : b) - a)); },
    l: function (a, b, t) { return a + (b - a) * t; },
    /* texte : o = { t: taille, g: gras, c: couleur, a: "start|middle|end", op: opacité, it: italique, w: largeur max (retour à la ligne) } */
    t: function (x, y, txt, o) {
      o = o || {}; var t = o.t || 13, lignes = o.w ? couper(txt, o.w, t, o.g) : [String(txt)];
      var dy = o.v ? -(lignes.length - 1) * t * 0.6 : 0;
      return '<text x="' + x + '" y="' + (y + dy) + '" text-anchor="' + (o.a || "start") + '" style="font-size:' + t + "px;" + (o.g ? "font-weight:700;" : "") + (o.it ? "font-style:italic;" : "") + "fill:" + c(o.c || "encre") + ";opacity:" + (o.op === undefined ? 1 : o.op) + (o.f ? ";font-family:var(--titre);font-stretch:condensed" : "") + (o.h ? ";paint-order:stroke;stroke:var(--carte);stroke-width:4px;stroke-linejoin:round" : "") + '">' +
        lignes.map(function (l, k) { return '<tspan x="' + x + '" dy="' + (k ? t * 1.2 : 0) + '">' + esc(l) + "</tspan>"; }).join("") + "</text>";
    },
    /* rectangle : o = { f: remplissage, s: trait, r: arrondi, op, sw } */
    r: function (x, y, w, h, o) {
      o = o || {};
      return '<rect x="' + x + '" y="' + y + '" width="' + Math.max(0, w) + '" height="' + Math.max(0, h) + '" rx="' + (o.r === undefined ? 4 : o.r) + '" style="fill:' + c(o.f || "carte") + ";stroke:" + (o.s ? c(o.s) : "none") + ";stroke-width:" + (o.sw || 1.5) + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
    },
    cercle: function (x, y, r, o) {
      o = o || {};
      return '<circle cx="' + x + '" cy="' + y + '" r="' + Math.max(0, r) + '" style="fill:' + c(o.f || "canard") + ";stroke:" + (o.s ? c(o.s) : "none") + ";stroke-width:" + (o.sw || 1.5) + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
    },
    /* boîte avec texte centré : o = { k: "cause|meca|effet|frein|neutre", t: taille, op } */
    boite: function (x, y, w, h, txt, o) {
      o = o || {};
      var k = o.k || "meca", t = o.t || 12.5;
      var st = { cause: ["canard", "canard", "carte"], meca: ["carte", "canard", "encre"], effet: ["corailc", "corail", "encre"], frein: ["moutardec", "moutarde", "encre"], neutre: ["carte2", "ligne", "encre"] }[k];
      var lignes = couper(txt, w - 12, t, o.g), lh = t * 1.22, y0 = y + h / 2 - (lignes.length - 1) * lh / 2 + t * 0.36;
      return '<g style="opacity:' + (o.op === undefined ? 1 : o.op) + '">' + A.r(x, y, w, h, { f: st[0], s: st[1], r: 8 }) +
        lignes.map(function (l, j) { return '<text x="' + (x + w / 2) + '" y="' + (y0 + j * lh) + '" text-anchor="middle" style="font-size:' + t + "px;fill:" + c(st[2]) + (o.g ? ";font-weight:700" : "") + '">' + esc(l) + "</text>"; }).join("") + "</g>";
    },
    /* flèche de (x1, y1) à (x2, y2), tracée jusqu'à la fraction o.p ; o = { c, sw, p, op, tete } */
    fl: function (x1, y1, x2, y2, o) {
      o = o || {}; var p = o.p === undefined ? 1 : borne(o.p);
      if (p <= 0) return "";
      var x = x1 + (x2 - x1) * p, y = y1 + (y2 - y1) * p, a = Math.atan2(y2 - y1, x2 - x1), L = 7;
      var col = c(o.c || "gris");
      var s = '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x + '" y2="' + y + '" style="stroke:' + col + ";stroke-width:" + (o.sw || 1.8) + ";opacity:" + (o.op === undefined ? 1 : o.op) + (o.tir ? ";stroke-dasharray:4 3" : "") + '"/>';
      if (o.tete !== false) s += '<path d="M' + x + " " + y + "L" + (x - L * Math.cos(a - 0.45)) + " " + (y - L * Math.sin(a - 0.45)) + "L" + (x - L * Math.cos(a + 0.45)) + " " + (y - L * Math.sin(a + 0.45)) + 'z" style="fill:' + col + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
      return s;
    },
    /* ligne brisée tracée jusqu'à la fraction p de sa longueur ; o = { c, sw, op, aire: y du bas pour remplir } */
    pl: function (pts, p, o) {
      o = o || {}; p = p === undefined ? 1 : borne(p);
      if (pts.length < 2 || p <= 0) return "";
      var long = 0, seg = [];
      for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(d); long += d; }
      var reste = long * p, out = [pts[0]];
      for (var j = 1; j < pts.length && reste > 0; j++) {
        if (seg[j - 1] <= reste) { out.push(pts[j]); reste -= seg[j - 1]; }
        else { var f = reste / seg[j - 1]; out.push([pts[j - 1][0] + (pts[j][0] - pts[j - 1][0]) * f, pts[j - 1][1] + (pts[j][1] - pts[j - 1][1]) * f]); reste = 0; }
      }
      var d2 = out.map(function (q, k) { return (k ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1); }).join("");
      var s = "";
      if (o.aire !== undefined) s += '<path d="' + d2 + "L" + out[out.length - 1][0].toFixed(1) + " " + o.aire + "L" + out[0][0].toFixed(1) + " " + o.aire + 'z" style="fill:' + c(o.c || "canard") + ';opacity:.13"/>';
      s += '<path d="' + d2 + '" style="fill:none;stroke:' + c(o.c || "canard") + ";stroke-width:" + (o.sw || 2.6) + ";stroke-linejoin:round;stroke-linecap:round;opacity:" + (o.op === undefined ? 1 : o.op) + (o.tir ? ";stroke-dasharray:5 4" : "") + '"/>';
      return s;
    },
    /* axes : origine (x0, y0), largeur w, hauteur h ; o = { lx, ly : libellés } */
    axes: function (x0, y0, w, h, o) {
      o = o || {};
      var s = A.fl(x0, y0, x0 + w, y0, { c: "gris", sw: 1.3 }) + A.fl(x0, y0, x0, y0 - h, { c: "gris", sw: 1.3 });
      if (o.lx) s += A.t(x0 + w, y0 + 16, o.lx, { t: 11, a: "end", c: "gris" });
      if (o.ly) s += A.t(x0 + 6, y0 - h + 4, o.ly, { t: 11, c: "gris" });
      return s;
    },
    g: function (op, contenu, tr) { return '<g style="opacity:' + borne(op) + '"' + (tr ? ' transform="' + tr + '"' : "") + ">" + contenu + "</g>"; },
    /* pastille numérotée */
    puce: function (x, y, n, o) { o = o || {}; return A.cercle(x, y, 10, { f: o.f || "corail", op: o.op }) + A.t(x, y + 4, n, { t: 11, g: true, a: "middle", c: "carte", op: o.op }); },
    /* jauge horizontale de valeur v entre 0 et max */
    jauge: function (x, y, w, v, max, o) {
      o = o || {};
      return A.r(x, y, w, 10, { f: "carte2", r: 5 }) + A.r(x, y, w * borne(v / max), 10, { f: o.c || "corail", r: 5 }) +
        (o.l ? A.t(x, y - 5, o.l, { t: 11, c: "gris" }) : "") + (o.val ? A.t(x + w, y - 5, o.val, { t: 11, g: true, a: "end" }) : "");
    }
  };

  function mouvement() {
    return document.documentElement.classList.contains("mo") && !(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  }
  var IC_LECT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>';
  var IC_PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z" fill="currentColor"/></svg>';
  var IC_PREC = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM20 5v14L9 12z" fill="currentColor"/></svg>';
  var IC_SUIV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM4 5v14l11-7z" fill="currentColor"/></svg>';
  var IC_ZERO = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4v4h4"/></svg>';

  var actives = [];
  function monterUne(d) {
    var id = d.getAttribute("data-anim"), an = ANIMS[id];
    if (!an) return;
    var n = an.etapes.length, H = an.h || 300;
    d.className = "anim";
    d.innerHTML = '<div class="an-tete"><span class="an-k">Animation</span><span class="an-t">' + esc(an.t) + "</span></div>" +
      '<div class="an-scene"><svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(an.t) + '"></svg></div>' +
      '<div class="an-leg" aria-live="polite"><span class="an-n"></span><span class="an-l"></span></div>' +
      '<div class="an-barre" role="group" aria-label="Étapes">' + an.etapes.map(function (e, k) { return '<button type="button" data-k="' + k + '" aria-label="Étape ' + (k + 1) + '"><i></i></button>'; }).join("") + "</div>" +
      '<div class="an-cmd"><button type="button" class="an-b" data-a="prec" aria-label="Étape précédente">' + IC_PREC + '</button><button type="button" class="an-b an-jouer" data-a="jouer" aria-label="Lecture">' + IC_LECT + '</button><button type="button" class="an-b" data-a="suiv" aria-label="Étape suivante">' + IC_SUIV + '</button><button type="button" class="an-b" data-a="zero" aria-label="Recommencer">' + IC_ZERO + "</button></div>" +
      '<details class="an-txt"><summary>Le déroulé en texte</summary><ol>' + an.etapes.map(function (e) { return "<li>" + esc(e.l) + "</li>"; }).join("") + "</ol></details>" +
      (an.src ? '<p class="src-l">' + an.src + "</p>" : "");
    var svg = d.querySelector("svg"), leg = d.querySelector(".an-l"), num = d.querySelector(".an-n"), bJ = d.querySelector(".an-jouer");
    var segs = Array.prototype.slice.call(d.querySelectorAll(".an-barre button"));
    var etat = { i: 0, p: mouvement() ? 0 : 1, joue: false, attente: 0, dernier: 0, vu: false };
    function duree(k) { return (an.etapes[k].d || 3.5) * 1000; }
    function dessiner() {
      var s;
      try { s = an.rendu(A, etat.i, etat.p); } catch (e) { s = ""; }
      svg.innerHTML = s;
      segs.forEach(function (b, k) { b.querySelector("i").style.width = (k < etat.i ? 100 : k === etat.i ? etat.p * 100 : 0) + "%"; b.classList.toggle("act", k === etat.i); });
    }
    function legende(anim) {
      num.textContent = "Étape " + (etat.i + 1) + " / " + n;
      leg.textContent = an.etapes[etat.i].l;
      if (anim && mouvement()) { leg.classList.remove("vient"); void leg.offsetWidth; leg.classList.add("vient"); }
    }
    function majBouton() { bJ.innerHTML = etat.joue ? IC_PAUSE : IC_LECT; bJ.setAttribute("aria-label", etat.joue ? "Pause" : "Lecture"); d.classList.toggle("joue", etat.joue); }
    function aller(k, depart) {
      etat.i = Math.max(0, Math.min(n - 1, k));
      etat.p = depart && mouvement() ? 0 : 1; etat.attente = 0;
      legende(true); dessiner();
    }
    function boucle(t) {
      if (!etat.joue) return;
      var dt = Math.min(100, Math.max(0, t - (etat.dernier || t))); etat.dernier = t;
      if (etat.p < 1) { etat.p = Math.min(1, etat.p + dt / duree(etat.i)); dessiner(); }
      else {
        etat.attente += dt;
        if (etat.attente > 1500) {
          if (etat.i < n - 1) { aller(etat.i + 1, true); }
          else { etat.joue = false; majBouton(); return; }
        }
      }
      requestAnimationFrame(boucle);
    }
    function jouer() {
      if (!mouvement()) { if (etat.i < n - 1) aller(etat.i + 1, false); return; }
      if (etat.i === n - 1 && etat.p >= 1) aller(0, true);
      etat.joue = true; etat.dernier = 0; majBouton(); requestAnimationFrame(boucle);
    }
    function pause() { etat.joue = false; majBouton(); }
    d.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var a = b.getAttribute("data-a");
      if (b.hasAttribute("data-k")) { pause(); aller(+b.getAttribute("data-k"), false); return; }
      if (a === "jouer") { if (etat.joue) pause(); else jouer(); }
      else if (a === "suiv") { aller(etat.i + 1, etat.joue); }
      else if (a === "prec") { pause(); aller(etat.i - 1, false); }
      else if (a === "zero") { pause(); aller(0, true); if (mouvement()) jouer(); }
    });
    legende(false); dessiner(); majBouton();
    var obj = { d: d, demarrer: function () { if (!etat.vu && mouvement()) { etat.vu = true; jouer(); } }, pause: pause, joue: function () { return etat.joue; } };
    actives.push(obj);
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting && x.intersectionRatio > 0.45) obj.demarrer();
          else if (!x.isIntersecting && etat.joue) pause();
        });
      }, { threshold: [0, 0.45, 0.8] });
      io.observe(d);
    }
  }
  return {
    A: A,
    monter: function (racine) {
      actives.forEach(function (o) { o.pause(); });
      actives = [];
      Array.prototype.slice.call((racine || document).querySelectorAll("[data-anim]")).forEach(monterUne);
    }
  };
})();
