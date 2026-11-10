/* ---------- Animations explicatives : moteur commun ----------
   Une animation se déclare ainsi (dans n'importe quel fichier de src/, après anims.js) :

   ANIMS.nom = {
     titre: "Titre affiché",
     vb: [360, 240],                       // taille de la scène SVG (unités de la viewBox)
     etapes: [                             // une légende par étape (texte riche : $math$ permis)
       { d: 3, l: "Ce qui se passe à l'étape 1." },
       { d: 4, l: "…" }
     ],
     rendu: function (S, k, t) { … }       // dessine l'état : étape k (0, 1, …), avancement t de 0 à 1
   };

   Le rendu est une fonction pure de (k, t) : on redessine tout à chaque image.
   Dans le cours : <div data-anim="nom"></div>.
   Outils de S : S.rep(x0, x1, y0, y1, {px, py}) pose un repère gradué ; S.X(x), S.Y(y) ;
   S.courbe(f, a, b, cls, n) ; S.seg(xa, ya, xb, yb, cls) ; S.fleche(...) ; S.pt(x, y, cls, r) ;
   S.txt(x, y, texte, cls, ancre) ; S.rect(xa, ya, xb, yb, cls) ; S.poly(points, cls, ferme) ;
   les mêmes en pixels : S.px.seg, S.px.fleche, S.px.txt, S.px.rect, S.px.cercle, S.px.path ;
   S.px.math(x, y, w, h, "texte avec $math$") : étiquette en vraie notation (MathML dans un foreignObject).
   Le dernier argument facultatif de chaque outil est un objet d'attributs SVG ({opacity: .5}…).
   Aides : ANIM.e(t) (adoucissement), ANIM.l(a, b, t) (interpolation), ANIM.p(t, t0, t1) (sous-avancement).
   Classes utiles : g-c (bleu), g-c2 (rouge), g-c3 (vert), g-as (pointillés rouges), g-pt, g-pt2, g-bande,
   g-lab (étiquette), g-lab r / b, a-plein (aplat bleu léger), a-plein2 (aplat rouge léger), a-craie.
   Sans mouvement (prefers-reduced-motion), la lecture passe d'étape en étape sans interpolation. Au repos,
   la figure finale et toutes les légendes sont visibles : rien n'est caché en attendant l'animation. */
var R = String.raw;
var ANIMS = {};
var ANIM = (function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg", F = TeX.fmt;
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function e(t) { t = clamp(t); return t * t * (3 - 2 * t); }
  function l(a, b, t) { return a + (b - a) * t; }
  function p(t, t0, t1) { return clamp((t - t0) / (t1 - t0)); }
  function nf(x, d) { if (!isFinite(x)) return x > 0 ? "+∞" : "−∞"; return (+x.toFixed(d === undefined ? 3 : d)).toString().replace(".", ",").replace("-", "−"); }
  function N(tag, at, par) { var el = document.createElementNS(NS, tag); for (var k in at) if (at[k] !== undefined && at[k] !== null) el.setAttribute(k, at[k]); if (par) par.appendChild(el); return el; }
  function ajoute(at, x) { if (x) for (var k in x) at[k] = x[k]; return at; }

  function Scene(svg, W, H) {
    var S = { W: W, H: H, nf: nf }, g, plot, clipId = "ac" + Math.random().toString(36).slice(2, 8);
    var defs = N("defs", {}, svg), cp = N("clipPath", { id: clipId }, defs), cr = N("rect", { x: 0, y: 0, width: W, height: H }, cp);
    var mk = N("marker", { id: clipId + "f", viewBox: "0 0 10 10", refX: 8, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" }, defs);
    N("path", { d: "M0 0L10 5L0 10z", fill: "context-stroke" }, mk);
    var m = { l: 34, r: 10, t: 10, b: 22 }, x0 = 0, x1 = 1, y0 = 0, y1 = 1;
    S.vider = function () { if (g) svg.removeChild(g); g = N("g", {}, svg); plot = g; S.g = g; x0 = 0; x1 = 1; y0 = 0; y1 = 1; m = { l: 34, r: 10, t: 10, b: 22 }; cr.setAttribute("width", W); cr.setAttribute("height", H); cr.setAttribute("x", 0); cr.setAttribute("y", 0); };
    S.X = function (x) { return m.l + (x - x0) / (x1 - x0) * (W - m.l - m.r); };
    S.Y = function (y) { var v = H - m.b - (y - y0) / (y1 - y0) * (H - m.t - m.b); return v > 4000 ? 4000 : v < -4000 ? -4000 : v; };
    S.rep = function (a, b, c, d, opt) {
      opt = opt || {}; x0 = a; x1 = b; y0 = c; y1 = d;
      if (opt.marges) m = opt.marges;
      var gg = N("g", { opacity: opt.opacite === undefined ? 1 : opt.opacite }, g), k, px = opt.px || 1, py = opt.py || 1;
      if (!opt.sansGrille) {
        for (k = Math.ceil(a / px - 1e-9) * px; k <= b + 1e-9; k += px) {
          N("line", { x1: S.X(k), x2: S.X(k), y1: m.t, y2: H - m.b, "class": "g-grille" }, gg);
          if (!opt.sansNombres) { var t = N("text", { x: S.X(k), y: H - m.b + 15, "text-anchor": "middle", "class": "g-txt" }, gg); t.textContent = opt.fx ? opt.fx(k) : nf(k, 2); }
        }
        for (k = Math.ceil(c / py - 1e-9) * py; k <= d + 1e-9; k += py) {
          N("line", { x1: m.l, x2: W - m.r, y1: S.Y(k), y2: S.Y(k), "class": "g-grille" }, gg);
          if (!opt.sansNombres) { var t2 = N("text", { x: m.l - 5, y: S.Y(k) + 4, "text-anchor": "end", "class": "g-txt" }, gg); t2.textContent = opt.fy ? opt.fy(k) : nf(k, 2); }
        }
      }
      if (c <= 0 && d >= 0) N("line", { x1: m.l, x2: W - m.r, y1: S.Y(0), y2: S.Y(0), "class": "g-axe" }, gg);
      if (a <= 0 && b >= 0) N("line", { x1: S.X(0), x2: S.X(0), y1: m.t, y2: H - m.b, "class": "g-axe" }, gg);
      cr.setAttribute("x", m.l - 6); cr.setAttribute("y", m.t - 6); cr.setAttribute("width", W - m.l - m.r + 12); cr.setAttribute("height", H - m.t - m.b + 12);
      plot = N("g", { "clip-path": "url(#" + clipId + ")" }, g);
      return S;
    };
    S.libre = function () { plot = g; return S; };
    S.courbe = function (f, a, b, cls, n, x) {
      n = n || 200; var d = "", lev = true, haut = (y1 - y0) * 6;
      for (var i = 0; i <= n; i++) {
        var xx = a + (b - a) * i / n, y = f(xx);
        if (!isFinite(y) || y > y1 + haut || y < y0 - haut) { lev = true; continue; }
        d += (lev ? "M" : "L") + S.X(xx).toFixed(1) + " " + S.Y(y).toFixed(1); lev = false;
      }
      return N("path", ajoute({ d: d, "class": cls || "g-c" }, x), plot);
    };
    S.seg = function (xa, ya, xb, yb, cls, x) { return N("line", ajoute({ x1: S.X(xa), y1: S.Y(ya), x2: S.X(xb), y2: S.Y(yb), "class": cls || "g-c2" }, x), plot); };
    S.fleche = function (xa, ya, xb, yb, cls, x) { return N("line", ajoute({ x1: S.X(xa), y1: S.Y(ya), x2: S.X(xb), y2: S.Y(yb), "class": cls || "g-c2", "marker-end": "url(#" + clipId + "f)" }, x), plot); };
    S.pt = function (x, y, cls, r, at) { return N("circle", ajoute({ cx: S.X(x), cy: S.Y(y), r: r || 4, "class": cls || "g-pt" }, at), plot); };
    S.txt = function (x, y, s, cls, anc, at) { var t = N("text", ajoute({ x: S.X(x), y: S.Y(y), "class": "g-lab " + (cls || ""), "text-anchor": anc || "start" }, at), g); t.textContent = s; return t; };
    S.rect = function (xa, ya, xb, yb, cls, at) { var X1 = S.X(xa), X2 = S.X(xb), Y1 = S.Y(ya), Y2 = S.Y(yb); return N("rect", ajoute({ x: Math.min(X1, X2), y: Math.min(Y1, Y2), width: Math.abs(X2 - X1), height: Math.abs(Y2 - Y1), "class": cls || "g-bande" }, at), plot); };
    S.poly = function (pts, cls, ferme, at) { return N(ferme ? "polygon" : "polyline", ajoute({ points: pts.map(function (q) { return S.X(q[0]).toFixed(1) + "," + S.Y(q[1]).toFixed(1); }).join(" "), "class": cls || "g-c" }, at), plot); };
    S.px = {
      seg: function (xa, ya, xb, yb, cls, at) { return N("line", ajoute({ x1: xa, y1: ya, x2: xb, y2: yb, "class": cls || "g-c2" }, at), g); },
      fleche: function (xa, ya, xb, yb, cls, at) { return N("line", ajoute({ x1: xa, y1: ya, x2: xb, y2: yb, "class": cls || "g-c2", "marker-end": "url(#" + clipId + "f)" }, at), g); },
      txt: function (x, y, s, cls, anc, at) { var t = N("text", ajoute({ x: x, y: y, "class": "g-lab " + (cls || ""), "text-anchor": anc || "start" }, at), g); t.textContent = s; return t; },
      rect: function (x, y, w, h, cls, at) { return N("rect", ajoute({ x: x, y: y, width: w, height: h, "class": cls || "g-bande" }, at), g); },
      cercle: function (x, y, r, cls, at) { return N("circle", ajoute({ cx: x, cy: y, r: r, "class": cls || "g-pt" }, at), g); },
      path: function (d, cls, at) { return N("path", ajoute({ d: d, "class": cls || "g-c" }, at), g); },
      math: function (x, y, w, h, html, at) { var fo = N("foreignObject", ajoute({ x: x, y: y, width: w, height: h }, at), g); var d = document.createElement("div"); d.className = "a-math"; d.innerHTML = "<span>" + TeX.fmt(html) + "</span>"; fo.appendChild(d); return fo; }
    };
    S.vider();
    return S;
  }

  var enCours = null;
  function monte(el, nom) {
    var A = ANIMS[nom];
    if (!A) return;
    var reduit = !document.documentElement.classList.contains("mo");
    var n = A.etapes.length, debuts = [], total = 0;
    A.etapes.forEach(function (s) { debuts.push(total); total += s.d; });
    el.className = "anim";
    el.innerHTML = '<div class="at"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l6-3.5z" fill="currentColor"/></svg><span>' + F(A.titre) + '</span><small>Animation · ' + n + ' étapes</small></div>' +
      '<div class="scene"></div><div class="cap" aria-live="polite"></div>' +
      '<div class="ctl"><button type="button" class="ab" data-a="prev" aria-label="Étape précédente">' + ICO.prev + '</button><button type="button" class="ab jouer" data-a="play" aria-label="Lecture">' + ICO.play + '</button><button type="button" class="ab" data-a="next" aria-label="Étape suivante">' + ICO.next + '</button><div class="barre" role="group" aria-label="Étapes"></div></div>' +
      '<details class="deroule"><summary><span class="st">Le déroulé en ' + n + ' étapes</span></summary><ol>' + A.etapes.map(function (s) { return "<li>" + F(s.l) + "</li>"; }).join("") + "</ol></details>";
    var svg = N("svg", { viewBox: "0 0 " + A.vb[0] + " " + A.vb[1], role: "img", "aria-label": A.titre.replace(/\$/g, "") }, el.querySelector(".scene"));
    var S = Scene(svg, A.vb[0], A.vb[1]);
    var cap = el.querySelector(".cap"), barre = el.querySelector(".barre"), bplay = el.querySelector('[data-a="play"]');
    var segs = A.etapes.map(function (s, i) {
      var b = document.createElement("button"); b.type = "button"; b.className = "sg"; b.style.flexGrow = s.d; b.setAttribute("aria-label", "Étape " + (i + 1));
      b.innerHTML = "<i></i>"; b.onclick = function () { aller(debuts[i] + (reduit ? s.d - 1e-6 : 0)); if (!joue) dessiner(); }; barre.appendChild(b); return b;
    });
    var T = total, joue = false, raf = 0, dernier = 0, kc = -1, attente = 0;
    function etat(T) { var k = n - 1; for (var i = 0; i < n; i++) if (T < debuts[i] + A.etapes[i].d) { k = i; break; } return { k: k, t: clamp((T - debuts[k]) / A.etapes[k].d) }; }
    function dessiner() {
      var st = etat(T);
      S.vider();
      try { A.rendu(S, st.k, st.t); } catch (err) { if (window.console) console.error(err); }
      segs.forEach(function (b, i) { var f = i < st.k ? 1 : i > st.k ? 0 : st.t; b.firstChild.style.width = (f * 100) + "%"; b.classList.toggle("on", i === st.k); });
      if (st.k !== kc || !cap.innerHTML) {
        kc = st.k;
        cap.innerHTML = '<b>' + (st.k + 1) + "/" + n + "</b> " + F(A.etapes[st.k].l);
        if (!reduit) { cap.classList.remove("neuf"); void cap.offsetWidth; cap.classList.add("neuf"); }
      }
    }
    function aller(t) { T = Math.max(0, Math.min(total, t)); kc = -1; }
    function boucle(ts) {
      if (!joue) return;
      var dt = Math.min(0.1, Math.max(0, (performance.now() - dernier) / 1000)); dernier = performance.now();
      if (reduit) {
        attente += dt;
        var st = etat(T);
        if (attente > Math.max(2.5, A.etapes[st.k].d)) { attente = 0; if (st.k >= n - 1) { pause(); return; } aller(debuts[st.k + 1] + A.etapes[st.k + 1].d - 1e-6); dessiner(); }
      } else {
        T += dt;
        if (T >= total) { T = total; dessiner(); pause(); return; }
        dessiner();
      }
      raf = requestAnimationFrame(boucle);
    }
    function jouer() {
      if (enCours && enCours !== pause) enCours();
      enCours = pause;
      if (T >= total - 1e-5) aller(reduit ? A.etapes[0].d - 1e-6 : 0);
      joue = true; attente = 0; dernier = performance.now(); el.classList.add("joue");
      bplay.innerHTML = ICO.pause; bplay.setAttribute("aria-label", "Pause");
      dessiner(); raf = requestAnimationFrame(boucle);
    }
    function pause() {
      joue = false; cancelAnimationFrame(raf); el.classList.remove("joue");
      bplay.innerHTML = ICO.play; bplay.setAttribute("aria-label", "Lecture");
      if (enCours === pause) enCours = null;
    }
    bplay.onclick = function () { joue ? pause() : jouer(); };
    function finEtape(i) { return debuts[i] + A.etapes[i].d - 1e-6; }
    el.querySelector('[data-a="next"]').onclick = function () {
      var st = etat(T);
      if (joue && !reduit) { if (st.k < n - 1) aller(debuts[st.k + 1]); }
      else if (st.t < 0.999 && !reduit) aller(finEtape(st.k));
      else if (st.k < n - 1) aller(finEtape(st.k + 1));
      attente = 0; dessiner();
    };
    el.querySelector('[data-a="prev"]').onclick = function () {
      var st = etat(T);
      if (joue && !reduit) aller(st.t > 0.25 ? debuts[st.k] : debuts[Math.max(0, st.k - 1)]);
      else if (st.k > 0) aller(finEtape(st.k - 1));
      else aller(reduit ? finEtape(0) : 0);
      attente = 0; dessiner();
    };
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { es.forEach(function (x) { if (!x.isIntersecting && joue) pause(); }); }).observe(el);
    dessiner();
    el.classList.add("repos");
    bplay.addEventListener("click", function () { el.classList.remove("repos"); }, { once: true });
  }
  var ICO = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z" fill="currentColor"/></svg>',
    prev: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM19 5.5v13L9.5 12z" fill="currentColor"/></svg>',
    next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM5 5.5v13L14.5 12z" fill="currentColor"/></svg>'
  };
  return { monte: monte, e: e, l: l, p: p, nf: nf, arreter: function () { if (enCours) enCours(); } };
})();

/* ---------- Animations des chapitres 1 à 5 ---------- */

/* Chapitre 1 : la récurrence se propage */
ANIMS.propagation = {
  titre: "La propriété se propage d'un rang au suivant",
  vb: [360, 230],
  etapes: [
    { d: 3.5, l: R`On veut prouver $P(n)$ : « $u_n=2^{n+2}-3$ » pour la suite $u_0=1$, $u_{n+1}=2u_n+3$. Chaque case est un rang $n$.` },
    { d: 3.5, l: R`<b>Initialisation</b> : $u_0=1$ et $2^2-3=1$. La case $0$ est validée.` },
    { d: 4.5, l: R`<b>Hérédité</b>, une fois pour toutes : si $u_k=2^{k+2}-3$, alors $u_{k+1}=2(2^{k+2}-3)+3=2^{k+3}-3$. C'est une flèche « $k\Rightarrow k+1$ » valable pour <b>tout</b> $k$.` },
    { d: 7, l: R`On enchaîne : la case $0$ valide la $1$, qui valide la $2$, puis la $3$… Chaque flèche est la même hérédité, appliquée à un $k$ différent.` },
    { d: 3.5, l: R`Aucun rang n'échappe à la chaîne : $P(n)$ est vraie pour tout $n\in\N$. Deux preuves ont suffi pour une infinité de cas.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, n = 8, x0 = 14, dx = 42, y = 120, w = 34, h = 40;
    var vals = [1, 5, 13, 29, 61, 125, 253, 509];
    var valide = k < 1 ? -1 : k === 1 ? (t > 0.4 ? 0 : -1) : k === 2 ? 0 : k === 3 ? Math.floor(E(t) * 7.99) : 7;
    S.px.math(40, 8, 280, 34, R`$P(n)$ : « $u_n=2^{n+2}-3$ »`);
    for (var i = 0; i < n; i++) {
      var x = x0 + i * dx, on = i <= valide, frais = i === valide && (k === 1 || k === 3);
      S.px.rect(x, y - h / 2, w, h, on ? "a-case on" : "a-case", { rx: 6, transform: frais ? "translate(" + (x + w / 2) + " " + y + ") scale(" + (1 + 0.12 * Math.sin(Math.PI * p(k === 1 ? t : (E(t) * 7.99) % 1, 0, 1))) + ") translate(" + (-(x + w / 2)) + " " + (-y) + ")" : null });
      S.px.txt(x + w / 2, y - 26, "n=" + i, "", "middle", { "font-size": 11 });
      S.px.txt(x + w / 2, y + 5, on ? String(vals[i]) : "?", on ? "b" : "", "middle", { "font-size": vals[i] > 99 ? 11 : 13 });
      if (on) S.px.txt(x + w / 2, y + 36, "✓", "c3", "middle", { "font-size": 15 });
      if (i < n - 1 && (k >= 3 ? i < valide : false)) {
        var xa = x + w / 2 + 3, xb = x + dx + w / 2 - 3, ya = y - 40, cy = y - 58;
        S.px.path("M" + xa + " " + ya + "Q" + (xa + xb) / 2 + " " + cy + " " + xb + " " + ya, "g-c3", { fill: "none", "stroke-width": 1.8 });
        S.px.path("M" + xb + " " + ya + "l-6.5 -4.2l1.2 5.6z", "g-c3", { fill: "currentColor", style: "fill:var(--vert)" });
      }
    }
    S.px.txt(x0 + n * dx - 6, y + 5, "…", "", "start", { "font-size": 18 });
    if (k === 2) {
      var a = E(p(t, 0, 0.5));
      S.px.rect(60, 172, 240, 46, "a-bulle", { rx: 10, opacity: a });
      S.px.txt(180, 191, "si P(k) est vraie,", "", "middle", { opacity: a });
      S.px.txt(180, 208, "alors P(k+1) est vraie", "r", "middle", { opacity: a });
    }
    if (k === 4) { S.px.txt(180, 196, "pour tout n ∈ ℕ", "r", "middle", { "font-size": 17, opacity: E(t * 2) }); }
  }
};

/* Chapitre 2 : la bande ε se resserre */
ANIMS.bande = {
  titre: "La bande $\\varepsilon$ se resserre, le rang $N$ recule",
  vb: [360, 240],
  etapes: [
    { d: 4, l: R`On place les termes de $u_n=2+\frac{3(-1)^n}{n+1}$ : ils oscillent autour de $2$ en s'en rapprochant.` },
    { d: 3.5, l: R`On trace une bande de demi-largeur $\varepsilon=1$ autour de $\ell=2$. À partir du rang $N=3$, tous les termes sont dedans.` },
    { d: 4, l: R`On resserre : $\varepsilon=0{,}5$. Il faut aller plus loin : $N=6$.` },
    { d: 4, l: R`$\varepsilon=0{,}2$ : $N=15$. La bande est plus étroite, le rang recule… mais il existe toujours.` },
    { d: 4, l: R`Pour <b>toute</b> largeur $\varepsilon>0$, un tel rang existe : c'est exactement $\lim_{n\to+\infty}u_n=2$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, u = function (n) { return 2 + 3 * Math.pow(-1, n) / (n + 1); };
    S.rep(0, 30, -1.2, 5.2, { px: 5, py: 1 });
    function N0(eps) { for (var m = 200; m >= 0; m--) if (Math.abs(u(m) - 2) >= eps) return m + 1; return 0; }
    var eps = k < 1 ? null : k === 1 ? 1 : k === 2 ? ANIM.l(1, 0.5, E(t)) : k === 3 ? ANIM.l(0.5, 0.2, E(t)) : ANIM.l(0.2, 0.08, E(t));
    if (eps) eps = Math.round(eps * 1000) / 1000;
    if (eps) { S.rect(0, 2 - eps, 30, 2 + eps, "g-bande", { opacity: k === 1 ? E(t * 2) : 1 }); S.txt(29.5, 2 + Math.max(eps, 0.5) + 0.15, "2 ± " + ANIM.nf(eps, 2), "r", "end"); }
    S.seg(0, 2, 30, 2, "g-as");
    var nb = k === 0 ? Math.floor(E(t) * 30.99) : 30, Nn = eps ? N0(eps) : null;
    for (var i = 0; i <= nb; i++) S.pt(i, u(i), eps && i >= Nn ? "g-pt" : (eps ? "g-pt2" : "g-pt"), 3.3);
    if (Nn !== null && Nn <= 30) { S.seg(Nn, -1.2, Nn, 5.2, "g-c2", { "stroke-dasharray": "4 3" }); S.txt(Nn + 0.4, 4.6, "N = " + Nn, "r"); }
  }
};

/* Chapitre 3 : l'asymptote, vue de près puis de loin */
ANIMS.asymptote = {
  titre: "La courbe colle à son asymptote",
  vb: [360, 250],
  etapes: [
    { d: 4, l: R`$f(x)=\frac{2x+1}{x-1}=2+\frac{3}{x-1}$. Le point $M$ part vers la droite : l'écart entre $f(x)$ et $2$ (en rouge) vaut $\frac{3}{x-1}$.` },
    { d: 4.5, l: R`On recule la caméra : sur $[0;100]$, la courbe se confond avec la droite $y=2$. L'écart tend vers $0$ : $\lim_{x\to+\infty}f(x)=2$, asymptote horizontale.` },
    { d: 4, l: R`Retour près de $x=1$. Quand $x\to1^+$, $x-1$ est un petit nombre <b>positif</b> : $\frac{3}{x-1}$ explose, $f(x)\to+\infty$.` },
    { d: 4, l: R`Quand $x\to1^-$, $x-1$ est petit et <b>négatif</b> : $f(x)\to-\infty$. La droite $x=1$ est asymptote verticale.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (x) { return 2 + 3 / (x - 1); }, xm, X1 = 10;
    if (k === 1) X1 = Math.exp(ANIM.l(Math.log(10), Math.log(100), E(t)));
    if (k >= 2) X1 = 6;
    var bas = k >= 2 ? -10 : -2, haut = k >= 2 ? 12 : 8;
    S.rep(k >= 2 ? -4 : 0, X1, bas, haut, { px: X1 > 40 ? 20 : X1 > 12 ? 5 : 1, py: 2 });
    S.seg(-10, 2, 200, 2, "g-as");
    if (k >= 2 || X1 < 12) S.seg(1, -40, 1, 40, "g-as");
    S.courbe(f, 1.0005, X1, "g-c", 500);
    if (k >= 2) S.courbe(f, -4, 0.9995, "g-c", 300);
    if (k === 0) xm = ANIM.l(2, 9.5, E(t));
    else if (k === 1) xm = X1 * 0.92;
    else if (k === 2) xm = ANIM.l(3, 1.18, E(t));
    else xm = ANIM.l(-1, 0.82, E(t));
    var ym = f(xm);
    if (k <= 1) { S.seg(xm, 2, xm, ym, "g-c2", { "stroke-width": 3 }); S.txt(xm, ym + (k === 1 ? 0.5 : 0.35), "écart " + ANIM.nf(3 / (xm - 1), 3), "r", "end"); }
    S.pt(xm, Math.max(bas - 1, Math.min(haut + 1, ym)), "g-pt2", 5);
    if (k >= 2) S.txt(xm + (k === 2 ? 0.25 : -0.25), Math.max(bas + 0.5, Math.min(haut - 0.6, ym)), "f(" + ANIM.nf(xm, 2) + ") ≈ " + ANIM.nf(ym, 1), "r", k === 2 ? "start" : "end");
  }
};

/* Chapitre 4 : le théorème des valeurs intermédiaires, puis la dichotomie */
ANIMS.tvi = {
  titre: "Pourquoi la courbe doit couper la droite $y=k$",
  vb: [360, 240],
  etapes: [
    { d: 3.5, l: R`$f(x)=x^3+x-1$ sur $[0;1]$ : $f(0)=-1<0$ et $f(1)=1>0$. La valeur $k=0$ est entre les deux.` },
    { d: 4, l: R`$f$ est continue : on trace sa courbe sans lever le crayon, du point sous l'axe au point au-dessus. Impossible de passer sans <b>couper</b> la droite $y=0$ : c'est le TVI.` },
    { d: 3.5, l: R`$f$ est strictement croissante ($f'(x)=3x^2+1>0$) : la courbe ne coupe l'axe qu'<b>une</b> fois. Solution unique $\alpha$.` },
    { d: 6, l: R`Dichotomie : on coupe $[0;1]$ en deux, on garde la moitié où le signe change. $[0{,}5;1]$, puis $[0{,}5;0{,}75]$, puis $[0{,}625;0{,}75]$…` },
    { d: 3.5, l: R`Après $10$ coupes, l'intervalle mesure $\frac1{1024}$ : $0{,}681<\alpha<0{,}683$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (x) { return x * x * x + x - 1; };
    S.rep(-0.1, 1.1, -1.5, 1.5, { px: 0.25, py: 0.5 });
    var fin = k === 0 ? 0 : k === 1 ? E(t) : 1;
    S.seg(-0.1, 0, 1.1, 0, "g-c2", { "stroke-width": 2 });
    S.txt(1.08, 0.08, "y = 0", "r", "end");
    if (k >= 3) {
      var a = 0, b = 1, nb = k === 3 ? Math.floor(E(t) * 5.99) : 10;
      for (var i = 0; i < nb; i++) { var m = (a + b) / 2; if (f(a) * f(m) <= 0) b = m; else a = m; }
      S.rect(a, -1.5, b, 1.5);
      S.seg(a, -1.5, a, 1.5, "g-as"); S.seg(b, -1.5, b, 1.5, "g-as");
      S.txt(0.02, 1.3, "[" + ANIM.nf(a, 4) + " ; " + ANIM.nf(b, 4) + "]", "b");
    }
    if (fin > 0) S.courbe(f, 0, fin, "g-c", 120, { "stroke-width": 3 });
    S.pt(0, -1, "g-pt2", 5); S.pt(1, 1, "g-pt", 5);
    if (k >= 1 && fin > 0.682) S.pt(0.6823, 0, "g-pt2", 6);
    if (k === 2) S.txt(0.69, -0.25, "α unique", "r");
  }
};

/* Chapitre 4 : la tangente roule sur la courbe */
ANIMS.tangente = {
  titre: "La tangente roule : convexe, concave, inflexion",
  vb: [360, 240],
  etapes: [
    { d: 5, l: R`$f(x)=x^3-3x$. Le point de contact glisse de $x=-2$ vers $x=0$ : la tangente est <b>au-dessus</b> de la courbe, sa pente diminue ($f'$ décroît) : $f$ est concave, $f''(x)=6x<0$.` },
    { d: 3, l: R`En $x=0$, $f''(0)=0$ et $f''$ change de signe : la tangente <b>traverse</b> la courbe. C'est le point d'inflexion.` },
    { d: 5, l: R`De $0$ à $2$, la tangente passe <b>en dessous</b> de la courbe et sa pente augmente ($f'$ croît) : $f$ est convexe, $f''>0$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (x) { return x * x * x - 3 * x; }, d = function (x) { return 3 * x * x - 3; };
    S.rep(-2.5, 2.5, -4, 4, { px: 1, py: 2 });
    S.courbe(f, -2.5, 2.5, "g-c");
    var a = k === 0 ? ANIM.l(-2, -0.05, E(t)) : k === 1 ? ANIM.l(-0.05, 0.05, t) : ANIM.l(0.05, 2, E(t));
    var cls = a < -0.02 ? "g-c2" : a > 0.02 ? "g-c3" : "g-c2";
    S.seg(-2.5, f(a) + d(a) * (-2.5 - a), 2.5, f(a) + d(a) * (2.5 - a), cls, { "stroke-width": 2.4 });
    S.pt(a, f(a), "g-pt2", 5.5);
    S.txt(-2.4, 3.4, "f''(" + ANIM.nf(a, 2) + ") = " + ANIM.nf(6 * a, 2), a < -0.02 ? "r" : "b");
    S.txt(-2.4, 2.7, a < -0.02 ? "concave" : a > 0.02 ? "convexe" : "inflexion", a < -0.02 ? "r" : "b");
  }
};

/* Chapitre 5 : de l'arbre aux combinaisons */
ANIMS.arbre = {
  titre: "Pourquoi on divise par $k!$",
  vb: [360, 260],
  etapes: [
    { d: 3, l: R`On choisit $3$ coureurs parmi $4$ (A, B, C, D) <b>dans l'ordre</b> : $4$ choix pour l'or…` },
    { d: 3, l: R`… puis $3$ pour l'argent : $4\times3=12$ branches…` },
    { d: 3, l: R`… puis $2$ pour le bronze : $4\times3\times2=24$ podiums ordonnés.` },
    { d: 4.5, l: R`On colorie chaque podium selon l'<b>ensemble</b> de ses coureurs : ABC, ABD, ACD, BCD. Chaque couleur revient $3!=6$ fois (les $6$ ordres d'un même trio).` },
    { d: 3.5, l: R`Donc le nombre de trios (sans ordre) est $\frac{24}{6}=4=\binom43$. C'est la formule $\binom nk=\frac{n(n-1)\dots(n-k+1)}{k!}$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, L = ["A", "B", "C", "D"], cols = { ABC: "var(--bleu)", ABD: "var(--rouge)", ACD: "var(--vert)", BCD: "#B07F0A" };
    var feuilles = [];
    L.forEach(function (a) { L.forEach(function (b) { if (b === a) return; L.forEach(function (c) { if (c === a || c === b) return; feuilles.push(a + b + c); }); }); });
    var y = [22, 70, 130, 200], W = 360;
    S.px.cercle(180, y[0], 5, "g-pt");
    var niv = k === 0 ? 1 : k === 1 ? 2 : 3, prog = k <= 2 ? E(t) : 1;
    function xn(lvl, idx, nb) { return 12 + (W - 24) * (idx + 0.5) / nb; }
    for (var lvl = 1; lvl <= niv; lvl++) {
      var nb = lvl === 1 ? 4 : lvl === 2 ? 12 : 24, a = lvl === niv ? prog : 1;
      for (var i = 0; i < nb; i++) {
        var par = lvl === 1 ? 180 : xn(lvl - 1, Math.floor(i / (lvl === 2 ? 3 : 2)), lvl === 2 ? 4 : 12);
        var x = xn(lvl, i, nb), mot = lvl === 3 ? feuilles[i] : null;
        var col = k >= 3 && mot ? cols[mot.split("").sort().join("")] : null;
        S.px.seg(par, y[lvl - 1] + 4, ANIM.l(par, x, a), ANIM.l(y[lvl - 1] + 4, y[lvl] - 8, a), "a-branche", { opacity: lvl === 3 && k >= 3 ? 0.35 : 1 });
        if (a > 0.95) {
          var lab = lvl === 3 ? mot : (lvl === 1 ? L[i] : feuilles[i * 2].slice(0, 2));
          if (lvl < 3) S.px.txt(x, y[lvl] + 4, lab.slice(-1), "", "middle", { "font-size": 12 });
          else {
            var ty = y[3] + 2 + (k >= 3 ? 0 : 0);
            S.px.txt(x, ty, lab[0], col ? "" : "", "middle", { "font-size": 9, style: col ? "fill:" + col + ";font-weight:700" : null });
            S.px.txt(x, ty + 11.5, lab[1], "", "middle", { "font-size": 9, style: col ? "fill:" + col + ";font-weight:700" : null });
            S.px.txt(x, ty + 23, lab[2], "", "middle", { "font-size": 9, style: col ? "fill:" + col + ";font-weight:700" : null });
          }
        }
      }
    }
    var tot = niv === 1 ? 4 : niv === 2 ? 12 : 24;
    S.px.txt(8, 250, k === 4 ? "24 ÷ 3! = 4 trios" : tot + " branches", k === 4 ? "r" : "b", "start", k === 4 ? { "font-size": 14 } : null);
    if (k >= 3) {
      var a2 = k === 3 ? E(t) : 1;
      Object.keys(cols).forEach(function (c, i) { S.px.txt(196 + i * 41, 250, c, "", "middle", { style: "fill:" + cols[c] + ";font-weight:700", opacity: a2, "font-size": 12 }); });
    }
  }
};

/* Chapitre 2 : les quatre comportements de q^n */
ANIMS.geometrique = {
  titre: "Quatre raisons, quatre destins pour $q^n$",
  vb: [360, 250],
  etapes: [
    { d: 4, l: R`$q=1{,}2$ : chaque terme est $20\,\%$ plus grand que le précédent. Les termes dépassent tout seuil : $1{,}2^n\to+\infty$.` },
    { d: 4, l: R`$q=0{,}8$ : chaque terme perd $20\,\%$. Les termes fondent vers $0$ sans jamais l'atteindre : $0{,}8^n\to0$.` },
    { d: 4, l: R`$q=-0{,}8$ : le signe alterne à chaque pas, mais la taille fond : les termes zigzaguent vers $0$. $(-0{,}8)^n\to0$.` },
    { d: 4, l: R`$q=-1{,}2$ : le signe alterne et la taille grandit : les termes sautent de plus en plus loin, d'un côté puis de l'autre. Pas de limite.` },
    { d: 3.5, l: R`Bilan : seule la <b>taille</b> $|q|$ compte pour la convergence vers $0$ ($|q|<1$) ; si $q>1$, limite $+\infty$ ; si $q\leq-1$, pas de limite.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, Q = [1.2, 0.8, -0.8, -1.2], cols = ["g-pt2", "g-pt", "g-pt", "g-pt2"];
    S.rep(0, 15, -6, 6, { px: 5, py: 2 });
    S.seg(0, 0, 15, 0, "g-axe");
    var lst = k < 4 ? [k] : [0, 1, 2, 3];
    lst.forEach(function (i) {
      var q = Q[i], nb = k < 4 ? Math.floor(E(t) * 15.99) : 15, pts = [];
      for (var n = 0; n <= nb; n++) { var v = Math.pow(q, n); pts.push([n, Math.max(-7, Math.min(7, v))]); }
      S.poly(pts, k < 4 ? "a-craie" : "a-craie", false, { opacity: k < 4 ? 1 : 0.5 });
      pts.forEach(function (p) { S.pt(p[0], p[1], cols[i], 3.4, { opacity: k < 4 ? 1 : 0.7 }); });
      if (k === 4) { var last = pts[pts.length - 1]; S.txt(14.8, Math.max(-5.6, Math.min(5.6, last[1])) + [0.3, 0.5, -1.1, 0.3][i], "q = " + ANIM.nf(q, 1), cols[i] === "g-pt2" ? "r" : "b", "end"); }
    });
    if (k < 4) S.txt(0.3, 5.3, "q = " + ANIM.nf(Q[k], 1) + " : les termes qⁿ, n de 0 à 15", k === 0 || k === 3 ? "r" : "b");
  }
};

/* Chapitre 5 : le triangle de Pascal se construit */
ANIMS.pascalAnim = {
  titre: "Chaque case est la somme des deux cases au-dessus",
  vb: [360, 230],
  etapes: [
    { d: 3, l: R`Ligne $0$ : $\binom00=1$. Chaque ligne commence et finit par $1$ : $\binom n0=\binom nn=1$.` },
    { d: 6, l: R`Pour remplir une case intérieure, on additionne les deux cases juste au-dessus : $\binom{n-1}{k-1}+\binom{n-1}{k}=\binom nk$. On descend ligne par ligne.` },
    { d: 4, l: R`Pourquoi ? Pour choisir $k$ éléments parmi $n$, soit on prend un élément fixé $a$ (il reste $k-1$ à choisir parmi $n-1$), soit on ne le prend pas ($k$ parmi $n-1$).` },
    { d: 4, l: R`La somme d'une ligne double à chaque fois : $1, 2, 4, 8, 16\dots$ C'est $\sum_{k=0}^n\binom nk=2^n$, le nombre de parties d'un ensemble à $n$ éléments.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, L = 7, W = 360, dx = 36, dy = 28;
    function C(n, j) { var r = 1; for (var i = 1; i <= j; i++) r = r * (n - j + i) / i; return Math.round(r); }
    var total = (L + 1) * (L + 2) / 2, vis = k === 0 ? 1 : k === 1 ? Math.max(1, Math.floor(E(t) * total)) : total, c = 0, cible = null;
    for (var n = 0; n <= L; n++) for (var j = 0; j <= n; j++) {
      c++; if (c > vis) continue;
      var x = W / 2 + (j - n / 2) * dx - 24, y = 20 + n * dy, frais = c === vis && k === 1;
      if (frais && j > 0 && j < n) cible = [n, j];
      S.px.rect(x - 16, y - 11, 32, 22, frais ? "a-case on" : "a-case", { rx: 6 });
      S.px.txt(x, y + 5, String(C(n, j)), frais ? "r" : "", "middle", { "font-size": C(n, j) > 9 ? 12 : 13 });
    }
    if (cible) {
      var n2 = cible[0], j2 = cible[1];
      [j2 - 1, j2].forEach(function (jj) { var x = W / 2 + (jj - (n2 - 1) / 2) * dx - 24, y = 20 + (n2 - 1) * dy; S.px.fleche(x, y + 11, W / 2 + (j2 - n2 / 2) * dx - 24 + (jj < j2 ? -6 : 6), 20 + n2 * dy - 12, "g-c2", { "stroke-width": 1.6 }); });
    }
    if (k === 2) {
      S.px.txt(W - 8, 30, "avec a : C(n−1, k−1)", "r", "end", { opacity: E(t * 2) });
      S.px.txt(W - 8, 50, "sans a : C(n−1, k)", "b", "end", { opacity: E(t * 2 - 0.3) });
    }
    if (k === 3) for (var m = 0; m <= L; m++) S.px.txt(W - 6, 25 + m * dy, "= " + Math.pow(2, m), "r", "end", { opacity: E(t * 3 - m * 0.25) });
  }
};
