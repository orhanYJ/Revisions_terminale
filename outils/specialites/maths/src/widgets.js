/* ---------- Icônes (SVG originaux, trait « stylo ») ---------- */
var ICONES = (function () {
  function s(p, extra) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' + (extra || "") + ">" + p + "</svg>"; }
  return {
    maison: s('<path d="M3.5 11 12 4l8.5 7"/><path d="M6 9.5V20h12V9.5"/><path d="M10 20v-5h4v5"/>'),
    cible: s('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>'),
    copie: s('<path d="M6 3h9l3 3v15H6z"/><path d="M9 9h6M9 12.5h6M9 16h4"/><path d="m14.5 15.5 2 2 3.5-4" stroke="var(--rouge)"/>'),
    livres: s('<path d="M4 5h4v15H4zM8 6h4v14H8z"/><path d="m13 6.5 3.8-1 3.7 13.6-3.8 1z"/>'),
    courbe: s('<path d="M3 20V4M3 20h18"/><path d="M5 17c3-1 4-9 7-9s4 5 8 5" stroke="var(--bleu)"/>'),
    cube: s('<path d="M12 3 4 7.5v9L12 21l8-4.5v-9z"/><path d="M4 7.5 12 12l8-4.5M12 12v9"/>'),
    de: s('<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="8.5" cy="8.5" r="1.2" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1.2" fill="currentColor"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/>'),
    retour: s('<path d="M9 14 4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/>'),
    print: s('<path d="M7 9V3h10v6"/><rect x="3.5" y="9" width="17" height="8" rx="2"/><path d="M7 14h10v7H7z"/>'),
    soleil: s('<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/>'),
    lune: s('<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>'),
    auto: s('<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17a8.5 8.5 0 0 0 0-17z" fill="currentColor"/>'),
    loupe: s('<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/>'),
    menu: s('<path d="M4 7h16M4 12h16M4 17h11"/>'),
    croix: s('<path d="M6 6l12 12M18 6 6 18"/>'),
    domino: s('<rect x="3" y="7" width="5" height="13" rx="1"/><rect x="10" y="7" width="5" height="13" rx="1" transform="rotate(14 12.5 20)"/><path d="M18 20 21 9"/>'),
    toile: s('<path d="M3 21 21 3" stroke-dasharray="2 3"/><path d="M4 20c4-9 9-13 17-14"/><path d="M6 21v-9h6v-4h4" stroke="var(--rouge)"/>'),
    asym: s('<path d="M3 8h18" stroke-dasharray="3 3"/><path d="M9 3v18" stroke-dasharray="3 3"/><path d="M11 21c0-8 2-11 10-12M3 7c5 0 5-1 5-4" stroke="var(--bleu)"/>'),
    expo: s('<path d="M3 21h18M3 21V3"/><path d="M4 20c6-1 10-3 14-16" stroke="var(--rouge)"/><path d="M4 20c6-2 11-5 16-10" stroke="var(--bleu)"/>'),
    dicho: s('<path d="M3 12h18"/><path d="M4 9v6M20 9v6M12 9v6" /><path d="M16 10v4" stroke="var(--rouge)"/><path d="M5 18c4-1 9-6 14-13" stroke="var(--bleu)"/>'),
    tangente: s('<path d="M3 18c4-14 9-14 18-2" stroke="var(--bleu)"/><path d="M3 7l18 3" stroke="var(--rouge)"/>'),
    triangle: s('<circle cx="12" cy="5" r="1.6"/><circle cx="9" cy="10" r="1.6"/><circle cx="15" cy="10" r="1.6"/><circle cx="6" cy="15" r="1.6"/><circle cx="12" cy="15" r="1.6" fill="currentColor"/><circle cx="18" cy="15" r="1.6"/><path d="M4 20h16"/>'),
    graphe: s('<path d="M3 21V3M3 21h18"/><circle cx="7" cy="8" r="1.3" fill="currentColor"/><circle cx="11" cy="14" r="1.3" fill="currentColor"/><circle cx="15" cy="10" r="1.3" fill="currentColor"/><circle cx="19" cy="12" r="1.3" fill="currentColor"/><path d="M4 12h17" stroke="var(--rouge)" stroke-dasharray="2 3"/>')
  };
})();

/* ---------- Interactifs : graphes SVG, curseurs ---------- */
var WIDGETS = (function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var F = TeX.fmt;
  function mo() { return document.documentElement.classList.contains("mo"); }
  function nf(x, d) { if (!isFinite(x)) return x > 0 ? "+∞" : "−∞"; var s = (+x.toFixed(d === undefined ? 3 : d)).toString().replace(".", ","); return s.replace("-", "−"); }
  function cadre(el, titre, icone, sous) {
    el.className = "wid";
    el.innerHTML = '<div class="wt">' + (ICONES[icone] || "") + "<span>" + titre + "</span><small>" + (sous || "Interactif") + '</small></div><div class="scene"></div><div class="ctrl"></div><div class="btns"></div><div class="note" aria-live="polite"></div>';
    return { scene: el.querySelector(".scene"), ctrl: el.querySelector(".ctrl"), btns: el.querySelector(".btns"), note: el.querySelector(".note") };
  }
  function curseur(ctrl, lab, min, max, pas, val, f) {
    var l = document.createElement("label");
    l.innerHTML = '<span>' + lab + " : <b></b></span>";
    var i = document.createElement("input"); i.type = "range"; i.min = min; i.max = max; i.step = pas; i.value = val;
    l.appendChild(i); ctrl.appendChild(l);
    var b = l.querySelector("b");
    function maj() { b.textContent = f ? f(+i.value) : nf(+i.value); }
    i.addEventListener("input", maj); maj();
    return i;
  }
  function liste(ctrl, lab, opts, f) {
    var l = document.createElement("label");
    l.innerHTML = "<span>" + lab + "</span>";
    var s = document.createElement("select");
    opts.forEach(function (o, k) { var op = document.createElement("option"); op.value = k; op.textContent = o; s.appendChild(op); });
    l.appendChild(s); ctrl.appendChild(l);
    return s;
  }
  function bouton(btns, txt, plein) { var b = document.createElement("button"); b.type = "button"; b.className = "btn" + (plein ? " plein" : ""); b.textContent = txt; btns.appendChild(b); return b; }
  function N(tag, at, par) { var e = document.createElementNS(NS, tag); for (var k in at) e.setAttribute(k, at[k]); if (par) par.appendChild(e); return e; }

  /* repère : x ∈ [x0,x1], y ∈ [y0,y1] dans un rectangle W×H */
  function Repere(scene, W, H, x0, x1, y0, y1, opt) {
    opt = opt || {};
    var m = { l: 34, r: 12, t: 12, b: 24 };
    var svg = N("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": opt.label || "Graphique" });
    scene.innerHTML = ""; scene.appendChild(svg);
    var R = { svg: svg, W: W, H: H };
    R.X = function (x) { return m.l + (x - x0) / (x1 - x0) * (W - m.l - m.r); };
    R.Y = function (y) { return H - m.b - (y - y0) / (y1 - y0) * (H - m.t - m.b); };
    R.clipY = function (y) { return Math.max(-3000, Math.min(3000, R.Y(y))); };
    var g = N("g", {}, svg);
    var px = opt.px || 1, py = opt.py || 1, k;
    /* grandes graduations en puissances de 10 (« 3·10⁵ ») : elles tiennent dans la marge */
    function grand(v) {
      if (Math.abs(v) < 1e4) return nf(v, 2);
      var e = Math.floor(Math.log10(Math.abs(v)) + 1e-9), q = Math.round(v / Math.pow(10, e) * 10) / 10, SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹";
      return (q === 1 ? "" : nf(q, 1) + "·") + "10" + String(e).split("").map(function (c) { return SUP[+c]; }).join("");
    }
    for (k = Math.ceil(x0 / px) * px; k <= x1 + 1e-9; k += px) {
      N("line", { x1: R.X(k), x2: R.X(k), y1: m.t, y2: H - m.b, "class": "g-grille" }, g);
      if (Math.abs(k) > 1e-9 || !opt.sansZeroX) { var t = N("text", { x: R.X(k), y: H - m.b + 15, "text-anchor": "middle", "class": "g-txt" }, g); t.textContent = nf(k, 2); }
    }
    for (k = Math.ceil(y0 / py) * py; k <= y1 + 1e-9; k += py) {
      N("line", { x1: m.l, x2: W - m.r, y1: R.Y(k), y2: R.Y(k), "class": "g-grille" }, g);
      var t2 = N("text", { x: m.l - 5, y: R.Y(k) + 4, "text-anchor": "end", "class": "g-txt" }, g); t2.textContent = grand(k);
    }
    if (y0 <= 0 && y1 >= 0) N("line", { x1: m.l, x2: W - m.r, y1: R.Y(0), y2: R.Y(0), "class": "g-axe" }, g);
    if (x0 <= 0 && x1 >= 0) N("line", { x1: R.X(0), x2: R.X(0), y1: m.t, y2: H - m.b, "class": "g-axe" }, g);
    var cid = "clip" + Math.random().toString(36).slice(2, 8);
    var cp = N("clipPath", { id: cid }, N("defs", {}, svg));
    N("rect", { x: m.l - 7, y: m.t - 7, width: W - m.l - m.r + 14, height: H - m.t - m.b + 14 }, cp);
    R.calque = N("g", { "clip-path": "url(#" + cid + ")" }, svg);
    R.vider = function () { while (R.calque.firstChild) R.calque.removeChild(R.calque.firstChild); };
    R.courbe = function (f, a, b, cls, n) {
      n = n || 240; var d = "", lev = true;
      for (var i = 0; i <= n; i++) {
        var x = a + (b - a) * i / n, y = f(x);
        if (!isFinite(y) || Math.abs(y - (y0 + y1) / 2) > 8 * (y1 - y0)) { lev = true; continue; }
        d += (lev ? "M" : "L") + R.X(x).toFixed(1) + " " + R.clipY(y).toFixed(1) + " "; lev = false;
      }
      return N("path", { d: d, "class": cls || "g-c" }, R.calque);
    };
    R.seg = function (xa, ya, xb, yb, cls) { return N("line", { x1: R.X(xa), y1: R.clipY(ya), x2: R.X(xb), y2: R.clipY(yb), "class": cls || "g-c2" }, R.calque); };
    R.pt = function (x, y, cls, r) { return N("circle", { cx: R.X(x), cy: R.clipY(y), r: r || 4, "class": cls || "g-pt" }, R.calque); };
    R.txt = function (x, y, s, cls, anc) { var t = N("text", { x: R.X(x), y: R.clipY(y), "class": "g-lab " + (cls || ""), "text-anchor": anc || "start" }, R.calque); t.textContent = s; return t; };
    R.rect = function (xa, ya, xb, yb, cls) { var X1 = R.X(xa), X2 = R.X(xb), Y1 = R.clipY(ya), Y2 = R.clipY(yb); return N("rect", { x: Math.min(X1, X2), y: Math.min(Y1, Y2), width: Math.abs(X2 - X1), height: Math.abs(Y2 - Y1), "class": cls || "g-bande" }, R.calque); };
    R.anime = function (path) { if (!mo() || !path.getTotalLength) return; var l = path.getTotalLength(); path.style.setProperty("--l", l); path.classList.add("trace"); };
    return R;
  }

  var W = {};

  /* 1. Récurrence : les dominos */
  W.dominos = function (el) {
    var c = cadre(el, "Les dominos de la récurrence", "domino", "Animation");
    var cas = liste(c.ctrl, "Situation", ["Initialisation + hérédité : tout tombe", "Hérédité seule, personne ne pousse le premier", "Initialisation seule : un écart casse la chaîne"]);
    var nb = 11, Wd = 360, Hd = 150, svg = N("svg", { viewBox: "0 40 " + Wd + " 104", role: "img", "aria-label": "Rangée de dominos" });
    c.scene.appendChild(svg);
    N("line", { x1: 4, x2: Wd - 4, y1: 118, y2: 118, "class": "g-axe" }, svg);
    var doms = [], timers = [];
    function pos(i, ecart) { return 12 + i * 29 + (ecart && i > 4 ? 32 : 0); }
    function dessine() {
      timers.forEach(clearTimeout); timers = [];
      doms.forEach(function (d) { d.g.remove(); if (d.t !== d.g) d.t.remove(); }); doms = [];
      var ecart = +cas.value === 2;
      for (var i = 0; i < nb; i++) {
        var x = pos(i, ecart);
        var g = N("g", {}, svg);
        g.style.transformBox = "view-box"; g.style.transformOrigin = (x + 9) + "px 118px";
        N("rect", { x: x, y: 70, width: 9, height: 48, rx: 1.5, fill: "var(--papier)", stroke: "var(--encre)", "stroke-width": 1.6 }, g);
        N("line", { x1: x + 1.5, x2: x + 7.5, y1: 94, y2: 94, stroke: "var(--encre)", "stroke-width": 1 }, g);
        N("circle", { cx: x + 4.5, cy: 82, r: 1.3, fill: "var(--encre)" }, g);
        N("circle", { cx: x + 4.5, cy: 106, r: 1.3, fill: "var(--encre)" }, g);
        var t = N("text", { x: x + 4.5, y: 134, "text-anchor": "middle", "class": "g-txt" }, svg); t.textContent = i;
        doms.push({ g: g, t: t });
      }
      if (ecart) { var tx = N("text", { x: pos(5, true) - 12, y: 60, "text-anchor": "middle", "class": "g-lab r" }, svg); tx.textContent = "écart"; doms.push({ g: tx, t: tx }); }
      c.note.innerHTML = F(["Chaque domino $n$ fait tomber le suivant $n+1$ : c'est l'<b>hérédité</b>. Pousse le domino $0$ : c'est l'<b>initialisation</b>.",
        "L'hérédité est vraie (chaque domino ferait tomber le suivant)… mais si personne ne pousse le domino $0$, rien ne tombe. <b>Sans initialisation, on ne prouve rien.</b>",
        "On pousse le domino $0$, mais entre le domino $4$ et le domino $5$ l'écart est trop grand : « si $n$ tombe alors $n+1$ tombe » est faux pour $n=4$. <b>Sans hérédité pour tout $n$, la chaîne casse.</b>"][+cas.value]);
      pousse.disabled = false;
    }
    function tombe(i, d) {
      var g = doms[i].g;
      if (mo()) { g.style.transition = "transform .32s cubic-bezier(.5,0,.75,.4)"; timers.push(setTimeout(function () { g.style.transform = "rotate(" + d + "deg)"; }, 10)); }
      else g.style.transform = "rotate(" + d + "deg)";
    }
    function lance() {
      pousse.disabled = true;
      var k = +cas.value;
      if (k === 1) { c.note.innerHTML = F("On attend… rien ne se passe : l'hérédité seule ne fait jamais tomber le premier domino. Il manque $P(0)$."); return; }
      var stop = k === 2 ? 5 : nb, pas = mo() ? 230 : 0;
      for (var i = 0; i < stop; i++) (function (i) {
        timers.push(setTimeout(function () { tombe(i, i === stop - 1 && stop < nb ? 88 : (i === nb - 1 ? 66 : 34)); }, i * pas));
      })(i);
      timers.push(setTimeout(function () {
        c.note.innerHTML = F(k === 0 ? "Tous les dominos sont tombés : $P(n)$ est vraie <b>pour tout entier</b> $n\\geq 0$. Même s'il y en avait une infinité !" : "Les dominos $0$ à $4$ sont tombés, puis tout s'arrête : $P(5)$, $P(6)$… ne sont pas démontrées. Vérifier quelques cas ne prouve rien.");
      }, stop * pas + 200));
    }
    var pousse = bouton(c.btns, "Pousser le domino 0", true);
    var re = bouton(c.btns, "Relever");
    pousse.onclick = lance; re.onclick = dessine; cas.onchange = dessine;
    dessine();
  };

  /* 2. Convergence d'une suite et bande ]ℓ−ε ; ℓ+ε[ */
  W.suite = function (el) {
    var c = cadre(el, "Toutes les valeurs à partir d'un certain rang", "graphe");
    var S = [
      { n: "u_n=2+\\frac{3(-1)^n}{n+1}", f: function (n) { return 2 + 3 * Math.pow(-1, n) / (n + 1); }, l: 2, y: [-1.5, 5.5] },
      { n: "u_n=3-\\frac{4}{n+1}", f: function (n) { return 3 - 4 / (n + 1); }, l: 3, y: [-1.5, 4.5] },
      { n: "u_n=2-1{,}5\\times 0{,}8^n", f: function (n) { return 2 - 1.5 * Math.pow(0.8, n); }, l: 2, y: [0, 3] },
      { n: "u_n=\\sqrt{n}", f: function (n) { return Math.sqrt(n); }, l: Infinity, y: [0, 7] },
      { n: "u_n=(-1)^n", f: function (n) { return Math.pow(-1, n); }, l: NaN, y: [-2, 2] }
    ];
    var choix = liste(c.ctrl, "Suite", ["2 + 3(−1)ⁿ/(n+1) → 2", "3 − 4/(n+1) → 3", "2 − 1,5 × 0,8ⁿ → 2", "√n → +∞", "(−1)ⁿ : pas de limite"]);
    var eps = curseur(c.ctrl, "Largeur ε (ou seuil A)", 0.05, 1, 0.05, 0.5);
    var nmax = 40;
    function maj() {
      var s = S[+choix.value], e = +eps.value, R = Repere(c.scene, 360, 220, 0, nmax, s.y[0], s.y[1], { px: 5, py: s.y[1] - s.y[0] > 4 ? 1 : 0.5, label: "Termes de la suite" });
      var lab = eps.parentNode.querySelector("span");
      var dans, N0 = null, info;
      if (s.l === Infinity) {
        var A = 1 + e * 5; lab.firstChild.nodeValue = "Seuil A : ";
        lab.querySelector("b").textContent = nf(A, 2);
        R.rect(0, A, nmax, s.y[1] + 5);
        R.seg(0, A, nmax, A, "g-as");
        dans = function (n) { return s.f(n) >= A; };
        N0 = Math.ceil(A * A);
        info = "Tous les termes sont dans $[A;+\\infty[$ dès le rang $N=" + N0 + "$ (car $\\sqrt{n}\\geq A \\iff n\\geq A^2$). Monte le seuil : le rang recule, mais il existe toujours.";
      } else {
        lab.firstChild.nodeValue = "Largeur ε : ";
        var l = isNaN(s.l) ? 1 : s.l;
        R.rect(0, l - e, nmax, l + e);
        R.seg(0, l, nmax, l, "g-as");
        R.txt(nmax - 0.5, l + e + 0.12, isNaN(s.l) ? "1 ± ε" : "ℓ ± ε", "r", "end");
        dans = function (n) { return Math.abs(s.f(n) - l) < e; };
        for (var k = 200; k >= 0; k--) if (!dans(k)) { N0 = k + 1; break; }
        if (N0 === null) N0 = 0;
        info = isNaN(s.l) ? "Les termes valent $1$ puis $-1$ en alternance : quelle que soit la bande autour de $1$ (ou de $-1$), une infinité de termes en sortent. <b>La suite n'a pas de limite.</b>" :
          "Avec $\\varepsilon=" + nf(e, 2) + "$, tous les termes sont dans la bande à partir du rang $N=" + N0 + "$. Réduis $\\varepsilon$ : $N$ grandit, mais il existe toujours. C'est la définition de $\\lim u_n=" + s.l + "$.";
        if (isNaN(s.l)) N0 = null;
      }
      for (var n = 0; n <= nmax; n++) R.pt(n, s.f(n), dans(n) && N0 !== null && n >= N0 ? "g-pt" : "g-pt2", 3.4);
      if (N0 !== null && N0 <= nmax) { R.seg(N0, s.y[0], N0, s.y[1], "g-as"); R.txt(N0 + 0.4, s.y[0] + (s.y[1] - s.y[0]) * 0.06, "N = " + N0, "b"); }
      c.note.innerHTML = F("$" + s.n + "$. " + info + " Points <span style=\"color:var(--rouge)\">rouges</span> : hors de la bande.");
    }
    choix.onchange = maj; eps.addEventListener("input", maj); maj();
  };

  /* 3. Toile d'araignée u_{n+1} = f(u_n) */
  W.toile = function (el) {
    var c = cadre(el, "Le diagramme en toile d'araignée", "toile");
    var FS = [
      { n: "f(x)=0{,}5x+2", f: function (x) { return 0.5 * x + 2; }, d: [0, 8], u0: [0, 8, 1], l: "4" },
      { n: "f(x)=\\sqrt{2x+3}", f: function (x) { return Math.sqrt(2 * x + 3); }, d: [0, 8], u0: [0, 8, 0.5], l: "3" },
      { n: "f(x)=1+\\frac{1}{x}", f: function (x) { return 1 + 1 / x; }, d: [0, 3], u0: [0.3, 3, 2.5], l: "\\frac{1+\\sqrt5}{2}\\approx1{,}618" },
      { n: "h(x)=-0{,}02x^2+1{,}3x", f: function (x) { return -0.02 * x * x + 1.3 * x; }, d: [0, 20], u0: [0.5, 20, 1], l: "15" }
    ];
    var choix = liste(c.ctrl, "Fonction f", ["0,5x + 2 (limite 4)", "√(2x+3) (limite 3)", "1 + 1/x (nombre d'or)", "−0,02x² + 1,3x (bac 2025)"]);
    var u0 = curseur(c.ctrl, "Premier terme u₀", 0, 8, 0.1, 1);
    var etapes = 0, R, s;
    var suiv = bouton(c.btns, "Étape suivante", true), tout = bouton(c.btns, "Tracer 12 étapes"), raz = bouton(c.btns, "Effacer");
    function base() {
      s = FS[+choix.value]; etapes = 0;
      R = Repere(c.scene, 360, 300, s.d[0], s.d[1], s.d[0], s.d[1], { px: s.d[1] > 10 ? 5 : s.d[1] > 4 ? 1 : 0.5, py: s.d[1] > 10 ? 5 : s.d[1] > 4 ? 1 : 0.5, label: "Diagramme en toile" });
      R.courbe(function (x) { return x; }, s.d[0], s.d[1], "g-as");
      R.anime(R.courbe(s.f, Math.max(s.d[0], 0.05), s.d[1], "g-c"));
      R.txt(s.d[1] * 0.97, s.d[1] * 0.9, "y = x", "r", "end");
      R.pt(+u0.value, 0, "g-pt2", 4.5);
      c.note.innerHTML = F("$u_{n+1}=" + s.n.replace(/^[fh]\(x\)=/, "").replace(/x/g, "u_n") + "$, $u_0=" + nf(+u0.value, 2) + "$. On monte jusqu'à la courbe (on calcule $f(u_n)$), puis on rejoint la droite $y=x$ (on reporte $u_{n+1}$ sur l'axe).");
    }
    function etape() {
      var u = +u0.value;
      for (var i = 0; i < etapes; i++) u = s.f(u);
      var v = s.f(u);
      if (!isFinite(v)) return;
      var a = R.seg(u, etapes === 0 ? 0 : u, u, v, "g-c2"), b = R.seg(u, v, v, v, "g-c2");
      if (mo() && a.getTotalLength) { [a, b].forEach(function (p, k) { var l = Math.hypot(p.x2.baseVal.value - p.x1.baseVal.value, p.y2.baseVal.value - p.y1.baseVal.value) || 1; p.style.setProperty("--l", l); p.style.animationDelay = (k * 0.18) + "s"; p.style.animationDuration = ".35s"; p.classList.add("trace"); }); }
      R.pt(v, 0, "g-pt", 3);
      etapes++;
      var termes = [], w = +u0.value; for (var j = 0; j <= etapes; j++) { termes.push(nf(w, 3)); w = s.f(w); }
      c.note.innerHTML = F("Termes : $" + termes.map(function (t, k) { return "u_{" + k + "}\\approx" + t; }).join(",\\ ") + "$. Ils s'approchent de $\\ell=" + s.l + "$, abscisse du point où la courbe coupe $y=x$ : c'est la solution de $f(\\ell)=\\ell$.");
    }
    suiv.onclick = function () { if (etapes < 30) etape(); };
    tout.onclick = function () { for (var k = 0; k < 12; k++) etape(); };
    raz.onclick = base;
    choix.onchange = function () { var r = FS[+choix.value].u0; u0.min = r[0]; u0.max = r[1]; u0.step = r[1] > 10 ? 0.5 : 0.1; u0.value = r[2]; u0.dispatchEvent(new Event("input")); };
    u0.addEventListener("input", base);
    base();
  };

  /* 4. Asymptotes */
  W.asymptotes = function (el) {
    var c = cadre(el, "Lire une asymptote sur la courbe", "asym");
    var FS = [
      { n: "f(x)=\\frac{2x+1}{x-1}", f: function (x) { return (2 * x + 1) / (x - 1); }, x: [-8, 10], y: [-6, 10], av: 1, ah: 2, txt: "Quand $x\\to\\pm\\infty$, $f(x)\\to2$ : la droite $y=2$ est asymptote horizontale. Quand $x\\to1^+$, $f(x)\\to+\\infty$ et quand $x\\to1^-$, $f(x)\\to-\\infty$ : la droite $x=1$ est asymptote verticale." },
      { n: "g(x)=x\\e^{-x}", f: function (x) { return x * Math.exp(-x); }, x: [-1, 10], y: [-1, 1], ah: 0, txt: "Croissances comparées : $\\lim_{x\\to+\\infty}x\\e^{-x}=0$, donc l'axe des abscisses ($y=0$) est asymptote en $+\\infty$. Pas d'asymptote en $-\\infty$ : $g(x)\\to-\\infty$." },
      { n: "k(x)=3+\\frac{1}{x^2}", f: function (x) { return 3 + 1 / (x * x); }, x: [-6, 6], y: [0, 10], av: 0, ah: 3, txt: "$\\lim_{x\\to0}\\frac{1}{x^2}=+\\infty$ des deux côtés : la droite $x=0$ est asymptote verticale. En $\\pm\\infty$, $k(x)\\to3$ : asymptote $y=3$, et la courbe reste au-dessus car $\\frac{1}{x^2}>0$." }
    ];
    var choix = liste(c.ctrl, "Fonction", ["(2x+1)/(x−1)", "x e⁻ˣ", "3 + 1/x²"]);
    var xs = curseur(c.ctrl, "Abscisse x du point", 0, 1, 0.001, 0.8);
    function maj() {
      var s = FS[+choix.value];
      var R = Repere(c.scene, 360, 260, s.x[0], s.x[1], s.y[0], s.y[1], { px: 2, py: s.y[1] - s.y[0] > 4 ? 2 : 0.5, label: "Courbe et asymptotes" });
      if (s.av !== undefined) R.seg(s.av, s.y[0], s.av, s.y[1], "g-as");
      if (s.ah !== undefined) R.seg(s.x[0], s.ah, s.x[1], s.ah, "g-as");
      R.courbe(s.f, s.x[0], s.x[1], "g-c", 600);
      var x = s.x[0] + (+xs.value) * (s.x[1] - s.x[0]);
      if (s.av !== undefined && Math.abs(x - s.av) < 0.02) x = s.av + 0.02;
      var y = s.f(x);
      xs.parentNode.querySelector("b").textContent = nf(x, 2);
      R.pt(x, y, "g-pt2", 5);
      var droite = x > s.x[0] + 0.6 * (s.x[1] - s.x[0]);
      R.txt(x + (droite ? -0.2 : 0.2), Math.min(y, s.y[1] - 0.3) + 0.3, "f(" + nf(x, 2) + ") ≈ " + nf(y, 3), "r", droite ? "end" : "start");
      c.note.innerHTML = F("$" + s.n + "$. " + s.txt + (s.ah !== undefined ? " Écart avec l'asymptote horizontale : $" + nf(Math.abs(y - s.ah), 4) + "$." : ""));
    }
    choix.onchange = maj; xs.addEventListener("input", maj); maj();
  };

  /* 5. Croissances comparées : xⁿ contre eˣ */
  W.croissances = function (el) {
    var c = cadre(el, "L'exponentielle gagne toujours", "expo");
    var n = curseur(c.ctrl, "Puissance n", 1, 10, 1, 3, function (v) { return v; });
    function dernierCroisement(k) { var a = k + 0.01, b = 200; for (var i = 0; i < 200; i++) { var m = (a + b) / 2; if (Math.exp(m) - Math.pow(m, k) > 0) b = m; else a = m; } return b; }
    function maj() {
      var k = +n.value, X = Math.max(8, Math.ceil(dernierCroisement(k) * 1.25)), M = Math.pow(k / Math.E, k);
      var R = Repere(c.scene, 360, 230, 0, X, 0, M * 1.35, { px: X > 30 ? 10 : 2, py: M * 1.35 > 50 ? Math.pow(10, Math.floor(Math.log10(M * 1.35))) : (M > 2 ? 1 : 0.2), label: "Quotient xⁿ / eˣ" });
      R.anime(R.courbe(function (x) { return Math.pow(x, k) / Math.exp(x); }, 0, X, "g-c", 400));
      R.pt(k, M, "g-pt2", 4.5);
      R.txt(k + X * 0.02, M * 1.12, "max en x = " + k, "r");
      var x1 = dernierCroisement(k);
      c.note.innerHTML = F("Courbe de $x\\mapsto\\frac{x^{" + k + "}}{\\e^x}$ : elle monte jusqu'à $x=" + k + "$ (maximum $\\left(\\frac{" + k + "}{\\e}\\right)^{" + k + "}\\approx" + nf(M, M > 1000 ? 0 : 3) + "$), puis retombe vers $0$. Donc $\\lim_{x\\to+\\infty}\\frac{x^{" + k + "}}{\\e^x}=0$. " + (k > 2 ? "Et $\\e^x$ dépasse définitivement $x^{" + k + "}$ dès $x\\approx" + nf(x1, 2) + "$." : "Et ici $\\e^x>x^{" + k + "}$ pour tout $x\\geq0$ ; plus la puissance est grande, plus l'exponentielle met de temps à gagner : essaie $n=10$."));
    }
    n.addEventListener("input", maj); maj();
  };

  /* 6. Dichotomie pas à pas */
  W.dicho = function (el) {
    var c = cadre(el, "Dichotomie pas à pas", "dicho", "Algorithme");
    var FS = [
      { n: "f(x)=x^3+x-1", f: function (x) { return x * x * x + x - 1; }, a: 0, b: 1, y: [-1.5, 1.5] },
      { n: "g(x)=x^2-2", f: function (x) { return x * x - 2; }, a: 1, b: 2, y: [-1.5, 2.5] }
    ];
    var choix = liste(c.ctrl, "Équation", ["x³ + x − 1 = 0 sur [0 ; 1]", "x² − 2 = 0 sur [1 ; 2] (√2)"]);
    var a, b, k, R, s, lignes;
    var suiv = bouton(c.btns, "Couper en deux", true), raz = bouton(c.btns, "Recommencer");
    var tab = document.createElement("div"); tab.className = "tab-wrap"; tab.style.margin = "4px 14px 0"; el.insertBefore(tab, c.note);
    function base() {
      s = FS[+choix.value]; a = s.a; b = s.b; k = 0; lignes = [];
      R = Repere(c.scene, 360, 220, s.a - 0.1, s.b + 0.1, s.y[0], s.y[1], { px: 0.25, py: 0.5, label: "Dichotomie" });
      dessine();
    }
    function dessine() {
      R.vider();
      R.rect(a, s.y[0], b, s.y[1]);
      R.courbe(s.f, s.a - 0.1, s.b + 0.1, "g-c");
      R.seg(a, s.y[0], a, s.y[1], "g-as"); R.seg(b, s.y[0], b, s.y[1], "g-as");
      R.pt(a, s.f(a), "g-pt2"); R.pt(b, s.f(b), "g-pt");
      tab.innerHTML = '<table><tr><th>Étape</th><th>a</th><th>b</th><th>m</th><th>signe de f(m)</th></tr>' + lignes.join("") + "</table>";
      c.note.innerHTML = F("$" + s.n + "$ est continue et change de signe sur $[" + nf(a, 6) + ";" + nf(b, 6) + "]$ : une solution $\\alpha$ s'y trouve (TVI). Amplitude : $" + nf(b - a, 6) + "=\\frac{1}{2^{" + k + "}}$." + (k >= 7 ? " Il faut $n$ étapes pour une amplitude $\\frac{1}{2^n}$ : $10$ étapes donnent environ $10^{-3}$." : ""));
    }
    suiv.onclick = function () {
      if (k >= 20) return;
      var m = (a + b) / 2, fm = s.f(m);
      lignes.push("<tr><td>" + (k + 1) + "</td><td>" + nf(a, 6) + "</td><td>" + nf(b, 6) + "</td><td>" + nf(m, 6) + "</td><td>" + (fm < 0 ? "−  → a ← m" : "+  → b ← m") + "</td></tr>");
      if (s.f(a) * fm <= 0) b = m; else a = m;
      k++; dessine();
    };
    raz.onclick = base; choix.onchange = base;
    base();
  };

  /* 7. Convexité : la tangente qui glisse */
  W.convexe = function (el) {
    var c = cadre(el, "Convexe, concave, point d'inflexion", "tangente");
    var FS = [
      { n: "f(x)=x^3-3x", f: function (x) { return x * x * x - 3 * x; }, d: function (x) { return 3 * x * x - 3; }, d2: function (x) { return 6 * x; }, x: [-2.5, 2.5], y: [-4, 4], i: 0, txt: "$f''(x)=6x$ : $f$ est concave sur $]-\\infty;0]$, convexe sur $[0;+\\infty[$, et $O(0;0)$ est un point d'inflexion : la tangente y traverse la courbe." },
      { n: "f(x)=\\e^x", f: Math.exp, d: Math.exp, d2: Math.exp, x: [-3, 2.5], y: [-1, 7], txt: "$f''(x)=\\e^x>0$ : $f$ est convexe sur $\\R$, la courbe est au-dessus de toutes ses tangentes. Avec la tangente en $0$ : $\\e^x\\geq x+1$ pour tout $x$." },
      { n: "g(x)=x\\e^x", f: function (x) { return x * Math.exp(x); }, d: function (x) { return (x + 1) * Math.exp(x); }, d2: function (x) { return (x + 2) * Math.exp(x); }, x: [-5, 1.2], y: [-1, 3], i: -2, txt: "$g''(x)=(x+2)\\e^x$ est du signe de $x+2$ : $g$ est concave sur $]-\\infty;-2]$ et convexe sur $[-2;+\\infty[$ (sujet du bac Polynésie, juin 2026). Point d'inflexion d'abscisse $-2$." }
    ];
    var choix = liste(c.ctrl, "Fonction", ["x³ − 3x", "eˣ", "x eˣ"]);
    var xs = curseur(c.ctrl, "Point de contact a", 0, 1, 0.002, 0.75);
    function maj() {
      var s = FS[+choix.value], a = s.x[0] + (+xs.value) * (s.x[1] - s.x[0]);
      xs.parentNode.querySelector("b").textContent = nf(a, 2);
      var R = Repere(c.scene, 360, 240, s.x[0], s.x[1], s.y[0], s.y[1], { px: 1, py: s.y[1] - s.y[0] > 6 ? 2 : 1, label: "Courbe et tangente" });
      R.courbe(s.f, s.x[0], s.x[1], "g-c");
      var T = function (x) { return s.f(a) + s.d(a) * (x - a); };
      R.seg(s.x[0], T(s.x[0]), s.x[1], T(s.x[1]), s.d2(a) >= 0 ? "g-c3" : "g-c2");
      if (s.i !== undefined) R.pt(s.i, s.f(s.i), "g-pt", 4);
      R.pt(a, s.f(a), "g-pt2", 5);
      var sg = s.d2(a), mot = Math.abs(sg) < 0.05 ? "$f''(a)\\approx0$ : point d'inflexion" : sg > 0 ? "$f''(a)>0$ : convexe ici, la courbe est au-dessus de la tangente (verte)" : "$f''(a)<0$ : concave ici, la courbe est en dessous de la tangente (rouge)";
      c.note.innerHTML = F("$" + s.n + "$. En $a=" + nf(a, 2) + "$, " + mot + ". " + s.txt);
    }
    choix.onchange = maj; xs.addEventListener("input", maj); maj();
  };

  /* 8. Triangle de Pascal */
  W.pascal = function (el) {
    var c = cadre(el, "Le triangle de Pascal", "triangle");
    var nn = curseur(c.ctrl, "Nombre de lignes", 4, 11, 1, 7, function (v) { return "n = 0 à " + v; });
    var sel = { n: 4, k: 2 };
    function C(n, k) { var r = 1; for (var i = 1; i <= k; i++) r = r * (n - k + i) / i; return Math.round(r); }
    function maj() {
      var L = +nn.value; if (sel.n > L) sel = { n: L, k: Math.min(sel.k, L) };
      var Wd = 360, dx = Wd / (L + 2), dy = 26, Hd = (L + 1) * dy + 16;
      var svg = N("svg", { viewBox: "0 0 " + Wd + " " + Hd, role: "img", "aria-label": "Triangle de Pascal" });
      c.scene.innerHTML = ""; c.scene.appendChild(svg);
      for (var n = 0; n <= L; n++) for (var k = 0; k <= n; k++) {
        var x = Wd / 2 + (k - n / 2) * dx, y = 16 + n * dy;
        var g = N("g", { tabindex: 0, role: "button", "aria-label": "C(" + n + "," + k + ")" }, svg); g.style.cursor = "pointer";
        var on = n === sel.n && k === sel.k, pere = n === sel.n - 1 && (k === sel.k || k === sel.k - 1);
        N("rect", { x: x - dx / 2 + 2, y: y - 11, width: dx - 4, height: 22, rx: 6, fill: on ? "var(--surligne2)" : pere ? "var(--surligne)" : "var(--papier)", stroke: on || pere ? "var(--rouge)" : "var(--ligne2)" }, g);
        var t = N("text", { x: x, y: y + 4.5, "text-anchor": "middle", "class": "g-lab", style: "font-size:" + (C(n, k) > 99 ? 10.5 : 12.5) + "px" + (on ? ";fill:#1B2A5E" : "") }, g); t.textContent = C(n, k);
        (function (n, k) { var f = function () { sel = { n: n, k: k }; maj(); }; g.addEventListener("click", f); g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); f(); } }); })(n, k);
      }
      var n0 = sel.n, k0 = sel.k, txt = "$\\binom{" + n0 + "}{" + k0 + "}=" + C(n0, k0) + "$ : nombre de parties à $" + k0 + "$ éléments d'un ensemble à $" + n0 + "$ éléments.";
      if (k0 > 0 && k0 < n0) txt += " Relation de Pascal : $\\binom{" + (n0 - 1) + "}{" + (k0 - 1) + "}+\\binom{" + (n0 - 1) + "}{" + k0 + "}=" + C(n0 - 1, k0 - 1) + "+" + C(n0 - 1, k0) + "=" + C(n0, k0) + "$.";
      txt += " Somme de la ligne $" + n0 + "$ : $2^{" + n0 + "}=" + Math.pow(2, n0) + "$. Symétrie : $\\binom{" + n0 + "}{" + k0 + "}=\\binom{" + n0 + "}{" + (n0 - k0) + "}$.";
      c.note.innerHTML = F(txt + " <i>Touche une case.</i>");
    }
    nn.addEventListener("input", maj); maj();
  };

  return W;
})();
