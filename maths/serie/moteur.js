/* Vidéos de cours de maths (site « CQFD ») — moteur du lecteur. Identité « le tableau noir » (10/11/2026) : une ardoise
   vert-noir avec ses traces d'effacement, tout s'écrit à la craie, trait par trait, sans bâton de craie visible ; titres
   soulignés deux fois, notes et pièges en craie de couleur, résultats entourés à la craie jaune, règle en bois pour tracer
   les axes, coup d'éponge entre les parties, poussière de craie.
   Les formules s'écrivent en $…$ (syntaxe compacte du site, sous-ensemble de LaTeX) et sont rendues en MathML natif :
   la composition (fractions, exposants, indices, racines, sommes, parenthèses extensibles) est celle de la police du site
   (Carnet Math, sous-ensemble de STIX Two Math), les lettres et les chiffres sont écrits à la craie (Caveat) ; $$…$$ = style
   « display ». Le convertisseur est une copie de outils/specialites/maths/src/mathml.js (à recopier s'il change).
   Écriture progressive : chaque visuel découpe son texte en unités (mots, formules) que la craie révèle de gauche à
   droite (fonction Ecrit) ; les traits (soulignés, cadres, coches, axes) se tracent (fonction Trait).
   Types propres aux maths : formule (note de marge m, étiquette lab, ok / ko, hl : souligné jaune, cadre : entouré en
   jaune, copie=True : la rédaction au tableau, avec sa marge), code (Python, trous complétés au repère {id.r1}…, sortie
   au repère {id.s}), graphe (axes tracés à la règle ; élément toile : toile d'araignée d'une suite u(n+1) = f(u(n))),
   illustrations dominos, propagation, suite, carres, euler.
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py depuis outils/serie-maths/<module>.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  // craies : blanche, jaune, bleue, rose, verte (les noms historiques des scripts sont gardés : iv, sa, ca, te…)
  var C = { iv: "#EEF0E6", iv2: "#BFC7BE", sa: "#F4D85E", sa2: "#E6C64C", ca: "#F6A9A2", te: "#A9D3F3", bleu: "#A9D3F3", nuit: "#1b2723",
    el: "#A9D3F3", rouge: "#F6A9A2", vert: "#B9E3A6", or: "#F4D85E" };

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
  /* ---------- convertisseur des maths : copie de outils/specialites/maths/src/mathml.js ---------- */
  /* ---------- Écriture des maths : syntaxe compacte (sous-ensemble de LaTeX) → MathML natif ---------- */
  var TeX = (function () {
    "use strict";
    var GREC = { alpha: "α", beta: "β", gamma: "γ", delta: "δ", epsilon: "ϵ", varepsilon: "ε", theta: "θ", lambda: "λ", mu: "μ", pi: "π", sigma: "σ", phi: "φ", varphi: "φ", omega: "ω", Delta: "Δ", Omega: "Ω", Sigma: "Σ", ell: "ℓ" };
    var OPS = { leq: "⩽", le: "⩽", geq: "⩾", ge: "⩾", neq: "≠", ne: "≠", times: "×", cdot: "·", pm: "±", mp: "∓", to: "→", rightarrow: "→", Rightarrow: "⇒", Leftarrow: "⇐", iff: "⇔", Leftrightarrow: "⇔", "in": "∈", notin: "∉", subset: "⊂", cup: "∪", cap: "∩", forall: "∀", exists: "∃", approx: "≈", circ: "∘", ldots: "…", dots: "…", cdots: "⋯", mapsto: "↦", lt: "<", gt: ">", colon: ":", setminus: "∖", prime: "′", sim: "∼", "|": "‖", equiv: "≡", leftarrow: "←", perp: "⊥", parallel: "∥", emptyset: "∅", ast: "∗", mid: "∣" };
    var ENS = { R: "ℝ", N: "ℕ", Z: "ℤ", Q: "ℚ", C: "ℂ" };
    var FONCS = { ln: 1, exp: 1, cos: 1, sin: 1, tan: 1, max: 1, min: 1, log: 1 };

    function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
    function el(tag, inner, attrs) { return "<" + tag + (attrs ? " " + attrs : "") + ">" + inner + "</" + tag + ">"; }
    function mo(c, attrs) { return el("mo", esc(c), attrs); }
    function mrow(a) { return a.length === 1 ? a[0] : el("mrow", a.join("")); }

    function Parser(src) { this.s = src; this.i = 0; }
    Parser.prototype.peek = function () { return this.s[this.i]; };
    Parser.prototype.blanc = function () { while (this.i < this.s.length && /\s/.test(this.s[this.i])) this.i++; };
    Parser.prototype.cmd = function () {
      var m = /^\\([A-Za-z]+|.)/.exec(this.s.slice(this.i));
      this.i += m[0].length; return m[1];
    };
    Parser.prototype.groupe = function () {
      this.blanc();
      if (this.peek() === "{") { this.i++; var r = this.liste("}"); this.i++; return mrow(r.length ? r : ["<mrow></mrow>"]); }
      if (/[0-9]/.test(this.peek())) return el("mn", this.s[this.i++]);
      return this.atome();
    };
    Parser.prototype.brut = function () {
      this.blanc();
      if (this.peek() !== "{") return this.s[this.i++] || "";
      var d = 0, j = this.i;
      for (; j < this.s.length; j++) { if (this.s[j] === "{") d++; else if (this.s[j] === "}") { d--; if (!d) break; } }
      var t = this.s.slice(this.i + 1, j); this.i = j + 1; return t;
    };
    Parser.prototype.liste = function (fin) {
      var out = [];
      for (;;) {
        this.blanc();
        if (this.i >= this.s.length) break;
        var c = this.peek();
        if (fin && c === fin) break;
        if (c === "&" || (c === "\\" && this.s[this.i + 1] === "\\")) break;
        if (c === "\\" && /^\\(right|end)\b/.test(this.s.slice(this.i))) break;
        var a = this.atome();
        if (a === null) continue;
        if (out.length && /^<mrow><mi mathvariant="normal">(ln|exp|cos|sin|tan|max|min|log)</.test(a) && !/^<mo/.test(out[out.length - 1])) out.push('<mspace width="0.17em"></mspace>');
        if ((a === "<mo>+</mo>" || a === "<mo>−</mo>") && (!out.length || /^<mo(?:\s[^>]*)?>(?!\)|\]|\||′)/.test(out[out.length - 1]))) a = a.replace("<mo>", '<mo form="prefix" rspace="0.05em">');
        out.push(this.scripts(a));
      }
      return out;
    };
    Parser.prototype.scripts = function (base) {
      var sub = null, sup = null, prime = "";
      for (;;) {
        this.blanc();
        var c = this.peek();
        if (c === "_") { this.i++; sub = this.groupe(); }
        else if (c === "^") { this.i++; sup = this.groupe(); }
        else if (c === "'") { this.i++; prime += "′"; }
        else break;
      }
      if (prime) base = el("mrow", base + mo(prime, 'lspace="0" rspace="0"'));
      var dessous = /^<mo[^>]*data-dessous/.test(base);
      if (dessous) {
        base = base.replace(" data-dessous", "");
        if (sub && sup) return el("munderover", base + sub + sup);
        if (sub) return el("munder", base + sub);
        if (sup) return el("mover", base + sup);
        return base;
      }
      if (sub && sup) return el("msubsup", base + sub + sup);
      if (sub) return el("msub", base + sub);
      if (sup) return el("msup", base + sup);
      return base;
    };
    Parser.prototype.cas = function () {
      var lignes = [], ligne = [], cell;
      for (;;) {
        cell = this.liste(null);
        ligne.push(el("mtd", mrow(cell.length ? cell : ["<mrow></mrow>"]), 'style="text-align:left;padding:0 .4em .15em 0"'));
        this.blanc();
        if (this.peek() === "&") { this.i++; continue; }
        if (this.peek() === "\\" && this.s[this.i + 1] === "\\") { this.i += 2; lignes.push(el("mtr", ligne.join(""))); ligne = []; continue; }
        break;
      }
      lignes.push(el("mtr", ligne.join("")));
      if (/^\\end\{[a-z]+\}/.test(this.s.slice(this.i))) this.i += /^\\end\{[a-z]+\}/.exec(this.s.slice(this.i))[0].length;
      return lignes;
    };
    Parser.prototype.atome = function () {
      var c = this.peek();
      if (c === "{") return this.groupe();
      if (c === "}") { this.i++; return null; }
      if (c === "\\") return this.commande();
      if (/[0-9]/.test(c)) {
        var m = /^[0-9]+(?:[.,][0-9]+)*/.exec(this.s.slice(this.i));
        this.i += m[0].length; return el("mn", m[0]);
      }
      if (/[A-Za-zÀ-ÿ]/.test(c)) { this.i++; return el("mi", c); }
      this.i++;
      if (c === "-") return mo("−");
      if (c === "*") return mo("×");
      if (c === "~") return '<mspace width="0.3em"></mspace>';
      if (c === "|") return mo("|", 'stretchy="false"');
      if (c === "(" || c === ")" || c === "[" || c === "]") return mo(c, 'stretchy="false"');
      if (c === "<" || c === ">" || c === "=") return mo(c);
      return mo(c);
    };
    Parser.prototype.commande = function () {
      var n = this.cmd(), a, b;
      if (n === "\\") return null;
      if (n === "frac" || n === "dfrac" || n === "tfrac") {
        a = this.groupe(); b = this.groupe();
        var f = el("mfrac", a + b);
        return n === "dfrac" ? el("mstyle", f, 'displaystyle="true"') : f;
      }
      if (n === "sqrt") {
        this.blanc();
        if (this.peek() === "[") { var j = this.s.indexOf("]", this.i); var idx = new Parser(this.s.slice(this.i + 1, j)); this.i = j + 1; return el("mroot", this.groupe() + mrow(idx.liste(null))); }
        return el("msqrt", this.groupe());
      }
      if (n === "binom") { a = this.groupe(); b = this.groupe(); return el("mrow", mo("(", 'stretchy="true"') + el("mfrac", a + b, 'linethickness="0"') + mo(")", 'stretchy="true"')); }
      if (n === "text") return el("mtext", esc(this.brut()).replace(/ /g, "&#160;"));
      if (n === "mathbb") { var l = this.brut(); return el("mi", ENS[l] || l, 'mathvariant="normal"'); }
      if (ENS[n]) return el("mi", ENS[n], 'mathvariant="normal"');
      if (n === "mathcal") { var lc = this.brut(); return el("mi", { P: "𝒫", C: "𝒞", B: "ℬ", D: "𝒟", E: "ℰ", F: "ℱ" }[lc] || lc, 'mathvariant="normal"'); }
      if (n === "mathrm" || n === "operatorname") return el("mi", esc(this.brut()), 'mathvariant="normal"');
      if (n === "e") return el("mi", "e", 'mathvariant="normal"');
      if (n === "i") return el("mi", "i", 'mathvariant="normal"');
      if (GREC[n]) return el("mi", GREC[n], /^[A-Z]/.test(n) ? 'mathvariant="normal"' : "");
      if (FONCS[n]) { this.blanc(); var par = this.peek() === "(" || this.peek() === "'" || /^(?:\\left|\\right|\^|_|[.,;:)\]}]|$)/.test(this.s.slice(this.i)); return el("mrow", el("mi", n, 'mathvariant="normal"') + '<mo lspace="0" rspace="' + (par ? "0" : "0.17em") + '">&#x2061;</mo>'); }
      if (n === "lim") return el("mo", "lim", 'data-dessous movablelimits="false" lspace="0" rspace="0.17em"');
      if (n === "sum") return el("mo", "∑", 'data-dessous largeop="true" movablelimits="false"');
      if (n === "prod") return el("mo", "∏", 'data-dessous largeop="true" movablelimits="false"');
      if (n === "infty") return el("mi", "∞");
      if (n === "widehat" || n === "hat") return el("mover", this.groupe() + mo("^", 'stretchy="' + (n === "widehat") + '"'), 'accent="true"');
      if (/^(big|Big|bigg|Bigg)[lr]?$/.test(n)) return null;
      if (n === "int") return el("mo", "∫", 'largeop="true" movablelimits="false" rspace="0.1em"');
      if (OPS[n]) return mo(OPS[n]);
      if (n === "quad") return '<mspace width="1em"></mspace>';
      if (n === "qquad") return '<mspace width="2em"></mspace>';
      if (n === ",") return '<mspace width="0.17em"></mspace>';
      if (n === ";") return '<mspace width="0.28em"></mspace>';
      if (n === "!") return "";
      if (n === "{" || n === "}" || n === "%" || n === "$" || n === "#" || n === "&") return mo(n, 'stretchy="false"');
      if (n === "abs") return el("mrow", mo("|", 'stretchy="true"') + this.groupe() + mo("|", 'stretchy="true"'));
      if (n === "overline") return el("mover", this.groupe() + mo("‾", 'stretchy="true"'), 'accent="true"');
      if (n === "vec") return el("mover", this.groupe() + mo("→", 'stretchy="true"'), 'accent="true"');
      if (n === "displaystyle") return null;
      if (n === "red" || n === "hl" || n === "blue") return el("mrow", this.groupe(), 'class="m-' + n + '"');
      if (n === "left") {
        this.blanc(); var o = this.s[this.i] === "\\" ? this.cmd() : this.s[this.i++];
        o = o === "." ? "" : o === "{" ? "{" : o;
        var inner = this.liste(null);
        var fermant = "";
        if (/^\\right/.test(this.s.slice(this.i))) { this.i += 6; this.blanc(); fermant = this.s[this.i] === "\\" ? this.cmd() : this.s[this.i++]; fermant = fermant === "." ? "" : fermant; }
        return el("mrow", (o ? mo(o, 'stretchy="true" fence="true"') : "") + inner.join("") + (fermant ? mo(fermant, 'stretchy="true" fence="true"') : ""));
      }
      if (n === "begin") {
        var env = this.brut();
        var t = el("mtable", this.cas().join(""), 'columnalign="left"');
        if (env === "cases") return el("mrow", mo("{", 'stretchy="true" fence="true"') + t);
        return t;
      }
      return el("mi", esc(n));
    };

    var cache = {};
    function math(src, bloc) {
      var k = (bloc ? "B" : "I") + src;
      if (cache[k]) return cache[k];
      var p = new Parser(src.replace(/\{,\}/g, ",")), r = [];
      try { r = p.liste(null); } catch (e) { r = [el("mtext", esc(src))]; }
      var out;
      if (r.length === 1 && /^<mo>[^<]*<\/mo>$/.test(r[0])) r[0] = r[0].replace("<mo>", '<mo lspace="0" rspace="0">');
      if (r.length < 4) out = '<math' + (bloc ? ' display="block"' : "") + '>' + (r.length > 1 ? el("mrow", r.join("")) : r.join("")) + "</math>";
      else {
        /* coupures possibles avant chaque relation (et après un \quad) : la formule passe à la ligne sur téléphone */
        var REL = /^<mo>(=|⇔|⇒|⩽|⩾|&lt;|&gt;|≠|≈|∈|≡)<\/mo>$/, ESP = /^<mspace width="[12]em"><\/mspace>$/, morceaux = [[]];
        var prof = 0;
        r.forEach(function (x, k) {
          if (/^<mo[^>]*>\(<\/mo>$/.test(x)) prof++; else if (/^(?:<msup>|<msub>|<msubsup>)?<mo[^>]*>\)<\/mo>/.test(x)) prof--;
          if (REL.test(x) && prof <= 0 && k > 0 && morceaux[morceaux.length - 1].length) { morceaux.push([]); x = x.replace("<mo>", '<mo lspace="0.278em" rspace="0.278em">'); }
          morceaux[morceaux.length - 1].push(x);
          if (bloc && ESP.test(x) && k < r.length - 1) morceaux.push([]);
        });
        var att = bloc ? ' displaystyle="true"' : "";
        out = morceaux.filter(function (m) { return m.length; }).map(function (m) { return "<math" + att + ">" + (m.length > 1 ? el("mrow", m.join("")) : m.join("")) + "</math>"; }).join("<wbr>");
        if (bloc) out = '<span class="mb">' + out + "</span>";
      }
      cache[k] = out;
      return out;
    }
    /* texte riche : $$…$$ (bloc), $…$ (en ligne) ; le reste est du HTML laissé tel quel */
    function fmt(txt) {
      if (txt == null) return "";
      /* Typographie : espace insécable avant « : ; ! ? » et après « (le texte seulement, jamais le code ni les balises),
         et une formule en ligne reste collée à la ponctuation qui la suit (pas de virgule en début de ligne). */
      var t = String(txt).split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>|<math[\s\S]*?<\/math>|\$\$[\s\S]+?\$\$|\$[^$]+?\$|<[^>]*>)/), out = "";
      for (var k = 0; k < t.length; k++) {
        var s = t[k];
        if (k % 2 === 0) { out += s.replace(/ ([;!?])/g, " $1").replace(/ ([:»])/g, " $1").replace(/« /g, "« "); continue; }
        if (s.slice(0, 2) === "$$") { out += math(s.slice(2, -2), true); continue; }
        if (s[0] !== "$") { out += s; continue; }
        var suite = k + 1 < t.length ? t[k + 1].replace(/ ([;!?])/g, " $1").replace(/ ([:»])/g, " $1") : "", m = /^[  ]?[,.;:!?)»…]+/.exec(suite);
        var av = /[(\[«]\u00A0?$/.exec(out), ap = m ? m[0] : "", bouts = math(s.slice(1, -1), false).split("<wbr>");
        if (m) t[k + 1] = suite.slice(ap.length);
        if (av) out = out.slice(0, out.length - av[0].length);
        if (av || ap) {
          if (bouts.length === 1) bouts[0] = '<span class="nw">' + (av ? av[0] : "") + bouts[0] + ap + "</span>";
          else {
            if (av) bouts[0] = '<span class="nw">' + av[0] + bouts[0] + "</span>";
            if (ap) bouts[bouts.length - 1] = '<span class="nw">' + bouts[bouts.length - 1] + ap + "</span>";
          }
        }
        out += bouts.join("<wbr>");
      }
      return out;
    }
    /* version texte brut (recherche) */
    function plat(txt) {
      return String(txt || "").replace(/\[(def|prop|thm|ex|meth|piege|hist)(?:\|([^\]]*))?\]/g, " $2 : ").replace(/\[\/\]|\[\/?py\]/g, " ").replace(/\$\$?([^$]+)\$\$?/g, function (_, m) {
        return m.replace(/\\[,;:!]|\\q?quad/g, " ").replace(/\\(int|sum|prod|lim)(?![a-zA-Z])/g, function (_, n) { return { int: " ∫", sum: " Σ", prod: " Π", lim: " lim" }[n]; }).replace(/\\(frac|dfrac|sqrt|binom|text|mathbb|mathrm|abs|overline|vec|red|hl|blue|left|right|begin|end)\b/g, " ")
          .replace(/\\([a-zA-Z]+)/g, function (_, n) { return n === "infty" ? "∞" : GREC[n] || OPS[n] || ENS[n] || n; }).replace(/[{}^_\\]/g, " ");
      }).replace(/<[^>]+>/g, " ").replace(/&[a-z#0-9]+;/gi, " ").replace(/\s+/g, " ").trim();
    }
    return { math: math, fmt: fmt, plat: plat };
  })();

  function escT(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  // texte avec maths : $…$ (en ligne) et $$…$$ (fractions en grand) → MathML ; **mot** → gras ; le reste est échappé
  function esc(s) {
    return String(s).split(/(\$\$[^$]+\$\$[.,;:!?)»]*|\$[^$]+\$[.,;:!?)»]*)/).map(function (p, i) {
      if (!(i % 2)) return escT(p).replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
      var j = p.lastIndexOf("$") + 1, ponct = p.slice(j), f = p.slice(0, j), d = f.slice(0, 2) === "$$";
      var m = TeX.math(d ? f.slice(2, -2) : f.slice(1, -1), false).replace(/<\/math><wbr><math>/g, "");
      if (d) m = m.replace(/<math>/g, '<math displaystyle="true">');
      return '<span class="nw">' + m + escT(ponct) + "</span>";
    }).join("");
  }
  // les espaces d'une formule ne coupent pas les mots (mots écrits un à un)
  function proteger(s) { return String(s).replace(/\$\$?[^$]+\$\$?/g, function (m) { return m.replace(/[ \t\n]/g, "\u0001"); }); }
  function rendre(s) { return s.replace(/\u0001/g, " "); }
  function fmt(t) { t = Math.max(0, Math.floor(t)); return Math.floor(t / 60) + ":" + ("0" + t % 60).slice(-2); }
  function alea(n) { var x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }
  function op(e, v) { e.style.opacity = v; }
  function tr(e, v) { e.style.transform = v; }
  function trace(e, p) { // dessine un tracé SVG de 0 à p
    if (!e._L) { e._L = e.getTotalLength ? e.getTotalLength() || 1 : 1; e.style.strokeDasharray = e._L + " " + (e._L + 2); }
    e.style.strokeDashoffset = e._L * (1 - cl(p, 0, 1));
    e.style.visibility = p <= 0 ? "hidden" : "";
  }
  function insec(s) { return String(s).replace(/ ([?!:;»])/g, " $1").replace(/« /g, "« "); }
  // lettres une à une (les mots restent insécables)
  function lettres(el, txt) {
    var out = [];
    insec(proteger(txt)).split(/([ \t\n]+)/).forEach(function (m) {
      if (/^[ \t\n]+$/.test(m)) { el.appendChild(document.createTextNode(" ")); return; }
      var w = h("span", "mot-l", el);
      if (m.indexOf("$") >= 0) { out.push(h("span", "lettre", w, esc(rendre(m)))); return; }   // une formule s'écrit d'un bloc
      Array.from(m).forEach(function (c) { out.push(h("span", "lettre", w, esc(c))); });
    });
    return out;
  }
  function mots(el, txt, cls) {
    var out = [];
    insec(proteger(txt)).split(/[ \t\n]+/).forEach(function (m, i) {
      if (i) el.appendChild(document.createTextNode(" "));
      out.push(h("span", cls || "mot-l", el, esc(rendre(m))));
    });
    return out;
  }
  // mots clés d'un visuel : chaque span dont le mot commence comme une clé s'allume quand la voix la prononce
  function nrm(x) { return String(x).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z]/g, ""); }
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
    if (sp.querySelector("math")) { sp._mot = sp; return sp; }   // une formule s'allume en bloc
    var m = sp.textContent.match(/^([«"'(\s  ]*)(.*?)([\s  ]*[.,;:!?»")…]*)$/);
    if (!m || (!m[1] && !m[3])) { sp._mot = sp; return sp; }
    sp.textContent = "";
    if (m[1]) sp.appendChild(document.createTextNode(m[1]));
    var in_ = h("span", "cle", sp, esc(m[2]));
    if (m[3]) sp.appendChild(document.createTextNode(m[3]));
    sp._mot = in_;
    return in_;
  }
  // le mot dit par la voix passe à la craie jaune et se souligne
  function allume(lst, t) {
    lst.forEach(function (c) {
      var p = P(t, c.t, .35);
      if (p <= 0) { if (c.on) { c.sp.style.color = ""; c.sp.style.backgroundSize = "0% 4px"; c.on = false; } return; }
      c.on = true;
      c.sp.style.color = C.sa;
      c.sp.style.backgroundSize = (100 * E(p)).toFixed(0) + "% 4px";
    });
  }

  // étape k d'un visuel : instant (repère {id.k}) ou, à défaut, une valeur de repli
  function et(v, k, repli) { return v.et && v.et[k] != null ? v.et[k] : v.t0 + repli; }

  /* =====================================================================================================
     LA CRAIE
     ===================================================================================================== */
  function rng(s) { return function () { s |= 0; s = s + 0x6D2B79F5 | 0; var t = Math.imul(s ^ s >>> 15, 1 | s); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function cvs(w, hh) { var c = document.createElement("canvas"); c.width = w; c.height = hh; return c; }
  function rrect(g, x, y, w, hh, r, suite) {
    if (!suite) g.beginPath();
    g.moveTo(x + r, y); g.lineTo(x + w - r, y); g.quadraticCurveTo(x + w, y, x + w, y + r);
    g.lineTo(x + w, y + hh - r); g.quadraticCurveTo(x + w, y + hh, x + w - r, y + hh); g.lineTo(x + r, y + hh);
    g.quadraticCurveTo(x, y + hh, x, y + hh - r); g.lineTo(x, y + r); g.quadraticCurveTo(x, y, x + r, y); g.closePath();
  }
  // segment tremblé (main levée) : points avec un léger bruit perpendiculaire
  function wob(x0, y0, x1, y1, amp, R, n) {
    n = n || Math.max(3, Math.round(Math.hypot(x1 - x0, y1 - y0) / 28));
    var dx = x1 - x0, dy = y1 - y0, l = Math.hypot(dx, dy) || 1, nx = -dy / l, ny = dx / l, pts = [], ph = R() * 6, bend = (R() - .5) * amp * 1.6;
    for (var i = 0; i <= n; i++) {
      var u = i / n, e = (i === 0 || i === n) ? 0 : (Math.sin(u * 5 + ph) * .5 + (R() - .5) * .6) * amp + Math.sin(u * Math.PI) * bend;
      pts.push([x0 + dx * u + nx * e, y0 + dy * u + ny * e]);
    }
    return pts;
  }
  function dPts(pts) { return "M" + pts.map(function (p) { return p[0].toFixed(1) + " " + p[1].toFixed(1); }).join(" L"); }
  // ellipse à main levée, qui dépasse un peu son départ
  function ptsEllipse(cx, cy, rx, ry, R, tours) {
    var pts = [], n = 72, a0 = -2.4 + R() * .3; tours = tours || 1.1;
    for (var i = 0; i <= n; i++) {
      var u = i / n, a = a0 + u * Math.PI * 2 * tours, k = 1 + .045 * Math.sin(u * 7 + 1) + .05 * u;
      pts.push([cx + Math.cos(a) * rx * k, cy + Math.sin(a) * ry * k + (u - .5) * ry * .1]);
    }
    return pts;
  }
  // cadre à main levée (coins légèrement arrondis, le trait déborde à la fermeture)
  function ptsBoite(x, y, w, hh, R) {
    var r = Math.min(16, hh * .3), a = 2.2, p = [];
    function seg(x0, y0, x1, y1) { var s = wob(x0, y0, x1, y1, a, R); if (p.length) s.shift(); p = p.concat(s); }
    seg(x + r, y + R() * 3, x + w - r, y + (R() - .5) * 4);
    seg(x + w - r, p[p.length - 1][1], x + w + (R() - .5) * 3, y + r);
    seg(p[p.length - 1][0], y + r, x + w + (R() - .5) * 4, y + hh - r);
    seg(p[p.length - 1][0], y + hh - r, x + w - r, y + hh + (R() - .5) * 3);
    seg(x + w - r, p[p.length - 1][1], x + r, y + hh + (R() - .5) * 4);
    seg(x + r, p[p.length - 1][1], x + (R() - .5) * 3, y + hh - r);
    seg(p[p.length - 1][0], y + hh - r, x + (R() - .5) * 4, y + r);
    seg(p[p.length - 1][0], y + r, x + r + 26, y - 3 + R() * 3);
    return p;
  }

  // génération : relève les mesures (les polices chargées changent la taille des textes)
  var GEN = 0;
  if (document.fonts) {
    document.fonts.addEventListener && document.fonts.addEventListener("loadingdone", function () { GEN++; });
    document.fonts.ready.then(function () { GEN++; });
  }

  /* trait de craie posé sur un hôte (en position relative) : mesuré une fois (et après chargement des polices), puis
     tracé de u = 0 à 1. genres : souligne, souligne2 (double), boite, ellipse, entoure (ellipse si l'hôte est compact,
     cadre sinon), coche, croix, barre (rature), gauche / droite (trait vertical en marge). opt : c (couleur), ep, m (marge), dy. */
  function Trait(hote, genre, opt) {
    opt = opt || {};
    if (getComputedStyle(hote).position === "static") hote.style.position = "relative";
    if (/^(SPAN|B)$/.test(hote.tagName)) hote.style.display = "inline-block";
    var s = sv("svg", { class: "tr-c", "aria-hidden": "true" }, hote), ps = [], gen = -1, vu = -1;
    s.style.display = "none";
    function construit() {
      var w = hote.offsetWidth, hh = hote.offsetHeight;
      if (!w || !hh) return false;
      gen = GEN; s.innerHTML = ""; ps = [];
      var R = rng(opt.graine || (Math.round(w * 7 + hh * 13) + genre.length)), m = opt.m != null ? opt.m : 10, d = [], g = genre;
      if (g === "entoure") g = w < hh * 3.2 ? "ellipse" : "boite";
      if (g === "souligne" || g === "souligne2") {
        var y = hh + (opt.dy != null ? opt.dy : 2);
        d.push(wob(-6, y + R() * 2, w + 8, y - 1 - R() * 2, 1.6, R));
        if (g === "souligne2") d.push(wob(6, y + 9, w - 2, y + 8 + (R() - .5) * 2, 1.6, R));
      } else if (g === "boite") d.push(ptsBoite(-m, -m * .7, w + 2 * m, hh + 1.4 * m, R));
      else if (g === "ellipse") {
        // texte long : l'ellipse doit contenir les coins du texte, pas seulement ses bords (sinon les lettres débordent)
        var lg = w > hh * 3;
        d.push(ptsEllipse(w / 2, hh / 2, (lg ? w * .64 : w / 2) + m * 1.6, (lg ? hh * .74 : hh / 2) + m * 1.1, R, 1.08));
      }
      else if (g === "coche") { var k = hh * .5; d.push([[w + 10, hh * .55], [w + 10 + k * .35, hh * .55 + k * .45], [w + 10 + k * 1.05, hh * .55 - k * .75]]); }
      else if (g === "barre") d.push(wob(-4, hh * .55, w + 4, hh * .47, 1.5, R));
      else if (g === "croix") { var q = hh * .32, cx = w + 12 + q, cy = hh * .5; d.push([[cx - q, cy - q], [cx + q, cy + q]]); d.push([[cx + q, cy - q], [cx - q, cy + q]]); }
      else if (g === "droite") d.push(wob(w + (opt.dx || 22), -4, w + (opt.dx || 22) + (R() - .5) * 4, hh + 4, 1.4, R));
      else if (g === "gauche") d.push(wob(-(opt.dx || 22), -4, -(opt.dx || 22) + (R() - .5) * 4, hh + 4, 1.4, R));
      var pad = 40;
      s.setAttribute("viewBox", (-pad) + " " + (-pad) + " " + (w + 2 * pad) + " " + (hh + 2 * pad));
      s.style.left = -pad + "px"; s.style.top = -pad + "px"; s.style.width = (w + 2 * pad) + "px"; s.style.height = (hh + 2 * pad) + "px";
      var tot = 0;
      d.forEach(function (pts) {
        var p = sv("path", { d: dPts(pts), fill: "none", stroke: opt.c || "currentColor", "stroke-width": opt.ep || 3.4, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
        var L = p.getTotalLength() || 1;
        p.style.strokeDasharray = L + " " + (L + 2);
        ps.push({ p: p, a: tot, L: L }); tot += L;
      });
      ps.forEach(function (x) { x.a /= tot; x.b = x.a + x.L / tot; });
      vu = -1;
      return true;
    }
    return function (u) {
      if (u <= 0) { if (s.style.display !== "none") s.style.display = "none"; return; }
      if (s.style.display === "none") s.style.display = "";
      if (gen !== GEN && !construit()) return;
      if (u === vu) return;
      vu = u;
      ps.forEach(function (x) {
        var f = cl((u - x.a) / (x.b - x.a), 0, 1);
        x.p.style.strokeDashoffset = x.L * (1 - f);
        x.p.style.visibility = f <= 0 ? "hidden" : "";
      });
    };
  }

  /* écriture : les unités d'un élément (mots, formules) dans l'ordre de lecture */
  function unites(el) {
    var out = [];
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          if (!/\S/.test(c.textContent)) return;
          var fr = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (p) {
            if (!p) return;
            if (!/\S/.test(p)) { fr.appendChild(document.createTextNode(p)); return; }
            var s = document.createElement("span"); s.className = "ec"; s.textContent = p; fr.appendChild(s);
            out.push({ e: s, n: p.length });
          });
          node.replaceChild(fr, c);
        } else if (c.nodeType === 1) {
          var tg = c.tagName.toLowerCase();
          if (tg === "svg" || c.classList.contains("hors")) return;
          if (tg === "math" || c.classList.contains("nw") || c.classList.contains("ec") || c.classList.contains("lettre") || (c.classList.contains("mot-l") && !c.querySelector(".lettre"))) {
            if (tg !== "math") c.classList.add("ec");
            out.push({ e: c, n: Math.max(1, c.textContent.replace(/\s/g, "").length) });
          } else if (tg !== "br" && tg !== "wbr") walk(c);
        }
      });
    })(el);
    return out;
  }
  // c : nombre de caractères déjà écrits ; la craie révèle chaque unité de gauche à droite
  function poser(us, c) {
    for (var i = 0; i < us.length; i++) {
      var x = us[i], f = cl((c - x.a) / x.n, 0, 1);
      if (f === x.f) continue;
      x.f = f;
      x.e.style.visibility = f <= 0 ? "hidden" : "";
      x.e.style.clipPath = f > 0 && f < 1 ? "inset(-45% " + (100 * (1 - f)).toFixed(1) + "% -55% -40%)" : "";
    }
  }
  var VITESSE = 26;   // caractères écrits par seconde
  function Ecrit(el, opt) {
    opt = opt || {};
    var us = unites(el), tot = 0;
    us.forEach(function (x) { x.a = tot; tot += x.n + 1; });
    var d = opt.d || cl(tot / (opt.v || VITESSE), opt.min || .3, opt.max || 2.6);
    poser(us, 0);
    return { d: d, n: tot, us: us, el: el,
      pose: function (t, t0) { poser(us, t0 == null ? tot : (t - t0) / d * tot); },
      u: function (u) { poser(us, u * tot); } };
  }

  /* ---------- textures (calculées une fois) ---------- */
  var TEX = {};
  // l'ardoise : fond vert-noir, nuages, traces d'effacement, anciens coups d'éponge, fantômes d'anciennes leçons, grain
  function planche(fantomes) {
    var WW = 1920, HH = 1080, c = cvs(WW, HH), g = c.getContext("2d"), R = rng(7), i;
    g.fillStyle = "#1b2723"; g.fillRect(0, 0, WW, HH);
    for (i = 0; i < 170; i++) {
      var x = R() * WW, y = R() * HH, r = 80 + R() * 420, dark = R() < .45;
      var gr = g.createRadialGradient(x, y, 0, x, y, r);
      gr.addColorStop(0, dark ? "rgba(4,10,8," + (.06 + R() * .1) + ")" : "rgba(80,104,94," + (.03 + R() * .06) + ")");
      gr.addColorStop(1, "rgba(0,0,0,0)"); g.fillStyle = gr; g.fillRect(x - r, y - r, 2 * r, 2 * r);
    }
    g.lineCap = "round";
    for (i = 0; i < 50; i++) {
      var x0 = R() * WW, y0 = R() * HH;
      g.strokeStyle = "rgba(200,218,208," + (.012 + R() * .022) + ")"; g.lineWidth = 50 + R() * 160;
      g.beginPath(); g.moveTo(x0, y0);
      g.bezierCurveTo(x0 + (R() - .5) * 900, y0 + (R() - .5) * 500, x0 + (R() - .5) * 900, y0 + (R() - .5) * 500, x0 + (R() - .5) * 1200, y0 + (R() - .5) * 600); g.stroke();
    }
    for (i = 0; i < 8; i++) {
      var zx = R() * WW, zy = R() * HH * .3; g.strokeStyle = "rgba(205,220,212," + (.012 + R() * .015) + ")"; g.lineWidth = 140 + R() * 80;
      g.beginPath(); g.moveTo(zx, zy); for (var k = 1; k < 6; k++) g.lineTo(zx + k * 110 + R() * 40, k % 2 ? zy + 500 + R() * 200 : zy + R() * 80); g.stroke();
    }
    if (fantomes) {
      var gh = [["f(x) = x² − 3x + 2", 1180, 1000, 64], ["Δ = b² − 4ac", 1480, 250, 78], ["(a + b)² = a² + 2ab + b²", 90, 960, 60],
        ["lim", 800, 150, 86], ["√2", 560, 880, 78], ["x ↦ eˣ", 1640, 660, 66], ["u₀ = 1", 300, 330, 70]];
      g.filter = "blur(2.5px)";
      gh.forEach(function (q) { g.font = "700 " + q[3] + "px Caveat"; g.fillStyle = "rgba(220,230,224," + (.05 + R() * .03) + ")"; g.save(); g.translate(q[1], q[2]); g.rotate((R() - .5) * .08); g.fillText(q[0], 0, 0); g.restore(); });
      g.filter = "none";
    }
    var im = g.getImageData(0, 0, WW, HH), d = im.data;
    for (i = 0; i < d.length; i += 4) { var n = (R() - .5) * 9; d[i] += n; d[i + 1] += n; d[i + 2] += n; }
    g.putImageData(im, 0, 0);
    var gb = g.createLinearGradient(0, HH - 70, 0, HH); gb.addColorStop(0, "rgba(220,225,220,0)"); gb.addColorStop(1, "rgba(220,225,220,.06)"); g.fillStyle = gb; g.fillRect(0, HH - 70, WW, 70);
    return c;
  }
  // grain de la craie : masque (opaque = la craie a pris, trous = le tableau transparaît)
  function grain() {
    var N = 300, c = cvs(N, N), g = c.getContext("2d"), R = rng(3), im = g.createImageData(N, N), d = im.data;
    for (var y = 0; y < N; y++) for (var x = 0; x < N; x++) {
      var i = (y * N + x) * 4, v = R(), bl = .5 + .5 * Math.sin(x * .07 + Math.sin(y * .05) * 2) * Math.sin(y * .09 + x * .02);
      var a = v < .07 + .1 * bl ? 0 : v < .16 + .1 * bl ? 130 : 255;
      d[i] = d[i + 1] = d[i + 2] = 255; d[i + 3] = a;
    }
    g.putImageData(im, 0, 0); return c.toDataURL("image/png");
  }
  // l'éponge (vue de dessus) et la règle en bois, à l'échelle 1,5 (l'export est en 1920 × 1080)
  function eponge() {
    var c = cvs(560, 260), g = c.getContext("2d"), R = rng(9), i;
    g.translate(280, 130);
    g.save(); g.filter = "blur(14px)"; g.fillStyle = "rgba(0,0,0,.55)"; rrect(g, -230, -84, 500, 210, 36); g.fill(); g.restore();
    g.fillStyle = "#3d4249"; rrect(g, -250, -100, 500, 200, 36); g.fill();
    g.fillStyle = "#B88954"; rrect(g, -232, -84, 464, 168, 26); g.fill();
    for (i = 0; i < 22; i++) { g.strokeStyle = "rgba(90,55,20," + (.12 + R() * .18) + ")"; g.lineWidth = 1 + R() * 2.5; var yy = -80 + R() * 160; g.beginPath(); g.moveTo(-228, yy); g.bezierCurveTo(-80, yy + (R() - .5) * 18, 80, yy + (R() - .5) * 18, 228, yy + (R() - .5) * 12); g.stroke(); }
    g.fillStyle = "rgba(60,35,12,.35)"; rrect(g, -150, -26, 300, 52, 26); g.fill();
    g.fillStyle = "rgba(255,235,200,.18)"; rrect(g, -232, -84, 464, 10, 6); g.fill();
    return c;
  }
  function regle(len) {
    var k = 1.5, c = cvs(Math.round((len + 40) * k), Math.round(150 * k)), g = c.getContext("2d"), R = rng(5), i;
    g.scale(k, k); g.translate(10, 110);
    g.save(); g.filter = "blur(10px)"; g.fillStyle = "rgba(0,0,0,.5)"; g.fillRect(14, -66, len, 78); g.restore();
    g.fillStyle = "#C9A066"; g.fillRect(0, -78, len, 78);
    for (i = 0; i < 26; i++) { g.strokeStyle = "rgba(110,70,30," + (.08 + R() * .14) + ")"; g.lineWidth = 1 + R() * 2; var yy = -74 + R() * 70; g.beginPath(); g.moveTo(0, yy); g.bezierCurveTo(len * .3, yy + (R() - .5) * 8, len * .7, yy + (R() - .5) * 8, len, yy + (R() - .5) * 6); g.stroke(); }
    g.fillStyle = "rgba(255,240,210,.22)"; g.fillRect(0, -78, len, 6); g.fillStyle = "rgba(70,40,10,.35)"; g.fillRect(0, -5, len, 5);
    g.strokeStyle = "rgba(40,24,8,.85)"; g.fillStyle = "rgba(40,24,8,.85)"; g.font = "600 18px Archivo, sans-serif";
    for (var x = 20, n = 0; x < len - 10; x += 18, n++) {
      var hh = n % 10 === 0 ? 30 : n % 5 === 0 ? 20 : 11; g.lineWidth = n % 10 === 0 ? 2.2 : 1.4;
      g.beginPath(); g.moveTo(x, -4); g.lineTo(x, -4 - hh); g.stroke();
      if (n % 10 === 0) g.fillText(String(n), x + 4, -40);
    }
    return c.toDataURL("image/png");
  }
  // hachures de craie (remplissage des cases, des aires)
  function hachures(defs, id, col, pas, ep) {
    var p = sv("pattern", { id: id, patternUnits: "userSpaceOnUse", width: pas || 12, height: pas || 12, patternTransform: "rotate(-45)" }, defs);
    sv("line", { x1: 0, y1: 0, x2: 0, y2: pas || 12, stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round", opacity: .75 }, p);
    return "url(#" + id + ")";
  }
  /* ---------- illustrations ---------- */
  function etiquette(g, x, y, txt, opt) {
    opt = opt || {};
    return sv("text", { x: x, y: y, "text-anchor": opt.ancre || "middle", fill: opt.c || C.iv, "font-size": Math.round((opt.fs || 26) * 1.22),
      "font-weight": 700, "letter-spacing": opt.ls || 0, class: "cr-t " + (opt.cls || "") }, g, txt);
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

  function fleche(g, d, col, ep) {
    var p = sv("path", { d: d, fill: "none", stroke: col, "stroke-width": ep || 3, "stroke-linecap": "round" }, g);
    return { p: p, pointe: pointe(g, p, col, Math.max(15, (ep || 3) * 1.9)) };
  }
  // pictogrammes des cartes (tracés qui se dessinent)
  var ICONES = {
    egal: ["M22 40 H78", "M22 60 H78"],
    encadre: ["M30 18 Q16 50 30 82", "M70 18 Q84 50 70 82", "M40 50 H60"],
    monte: ["M14 84 H34 V64 H54 V44 H74 V24 H90", "M14 92 H92"],
    domino: ["M30 14 H58 V86 H30 Z", "M30 50 H58", "M44 30 v.1 M44 68 v.1", "M66 30 L86 86"],
    somme: ["M76 18 H26 L54 50 L26 82 H76"],
    loupe: ["M44 16 a26 26 0 1 0 0.1 0", "M63 63 L88 88"]
  };
  function icone(nom, parent) {
    var s = sv("svg", { viewBox: "0 0 100 100" }, parent);
    return (ICONES[nom] || []).map(function (d) {
      return sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 5, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    });
  }
  // étiquette HTML posée sur une illustration (texte avec $maths$), coordonnées de la boîte de l'illustration
  function lbl(s, x, y, html, cls) {
    var d = h("div", "il-lab " + (cls || ""), s.parentNode, esc(html));
    d.style.left = x + "px"; d.style.top = y + "px";
    return d;
  }
  var ILLU = {};

  /* dominos : la récurrence en image. Une rangée de dominos numérotés ; repères nommés :
     {id.her} bulle « si le domino k tombe, il fait tomber k+1 » ; {id.init} on pousse le premier, la chaîne part,
     la caméra suit la vague ; {id.fin} bandeau v.fin.
     v.mode : "chaine" (défaut) | "sans_init" (rien ne tombe : le premier n'est pas poussé, croix rouge)
            | "trou" (au domino v.trou l'écart est trop grand : la chaîne s'arrête). v.n0 : premier numéro. */
  ILLU.dominos = function (s, v) {
    var W_ = v.w, H_ = v.h, n = v.n || 40, sp = v.sp || 66, hd = v.hd || 158, wd = v.wd || 22, y0 = v.y0 || H_ * .66;
    var x0 = v.x0 || 70, dt = v.dt || .2, dur = v.dur || .34, n0 = v.n0 || 0, k = v.k != null ? v.k : 3, mode = v.mode || "chaine";
    var thC = Math.acos(wd / sp) * 180 / Math.PI;
    var def = sv("defs", {}, s), mid = "dm" + Math.round(alea(v.t0) * 1e6);
    var lg = sv("linearGradient", { id: mid + "g", x1: 0, x2: 1 }, def);
    sv("stop", { offset: 0, "stop-color": "#fff", "stop-opacity": 1 }, lg);
    sv("stop", { offset: .86, "stop-color": "#fff", "stop-opacity": 1 }, lg);
    sv("stop", { offset: 1, "stop-color": "#fff", "stop-opacity": 0 }, lg);
    var mk = sv("mask", { id: mid + "m" }, def); sv("rect", { x: 0, y: -50, width: W_, height: H_ + 100, fill: "url(#" + mid + "g)" }, mk);
    var monde = sv("g", { mask: "url(#" + mid + "m)" }, s), cam = sv("g", {}, monde);
    var hj = hachures(def, mid + "h", C.sa, 10, 2.6);
    var sol = sv("path", { d: dPts(wob(-200, y0 + 2, x0 + n * sp + 400, y0, 2, rng(4), Math.round((x0 + n * sp + 600) / 40))), fill: "none", stroke: "rgba(238,240,230,.55)", "stroke-width": 3, "stroke-linecap": "round" }, cam);
    var X = [], xs = x0;
    for (var i = 0; i < n; i++) { X.push(xs); xs += (mode === "trou" && i === v.trou - 1) ? Math.max(sp, hd + 40) : sp; }
    var doms = X.map(function (x, i) {
      var g = sv("g", {}, cam), r = sv("g", {}, g);
      var corps = sv("rect", { x: x, y: y0 - hd, width: wd, height: hd, rx: 4, fill: "rgba(238,240,230,.10)", stroke: C.iv, "stroke-width": 3 }, r);
      sv("line", { x1: x + 3, x2: x + wd - 3, y1: y0 - hd / 2, y2: y0 - hd / 2, stroke: C.iv, "stroke-width": 2.2 }, r);
      [.25, .75].forEach(function (f) { sv("circle", { cx: x + wd / 2, cy: y0 - hd * f, r: 3, fill: C.iv }, r); });
      var num = i + n0, t = etiquette(g, x + wd / 2, y0 + 38, String(num), { fs: num >= 100 ? 20 : 25, c: C.iv2, cls: "ser" });
      return { g: g, r: r, corps: corps, x: x, num: t };
    });
    var dern = n - 1;
    if (mode === "trou") dern = v.trou - 1;
    // départ de la chute du domino i
    var tInit = et(v, "init", 1e9) + .35;
    function depart(i) { return mode === "sans_init" ? 1e9 : tInit + i * dt; }
    function angle(i, t) {
      var u = cl((t - depart(i)) / dur, 0, 1);
      if (i > dern) return 0;
      var fin = (i === dern && mode === "trou") ? 90 : thC;
      return fin * u * u;
    }
    // bulle de l'hérédité au-dessus des dominos k et k+1
    var bh = sv("g", {}, cam), xa = X[k] + wd / 2, xb = X[k + 1] + wd / 2, yb = y0 - hd - 26;
    var arc = fleche(bh, "M" + xa + " " + yb + " Q" + (xa + xb) / 2 + " " + (yb - 54) + " " + xb + " " + (yb - 4), C.sa, 3.4);
    var lk = etiquette(bh, xa, y0 + 76, "k", { fs: 30, c: C.sa, cls: "ser", fw: 700 });
    var lk1 = etiquette(bh, xb + 14, y0 + 76, "k + 1", { fs: 30, c: C.sa, cls: "ser", fw: 700 });
    var bul = lbl(s, 0, 0, v.bulle || "si le domino $k$ tombe, il fait tomber le domino $k+1$", "bulle");
    // initialisation : la main qui pousse (une flèche) et l'étiquette
    var gi = sv("g", {}, cam), fi = fleche(gi, "M" + (X[0] - 70) + " " + (y0 - hd * .8) + " H" + (X[0] - 8), C.ca, 4.5);
    var bi = lbl(s, 0, 0, v.init || "le premier tombe", "bulle r");
    var croix = sv("path", { d: "M" + (X[0] - 18) + " " + (y0 - hd - 30) + " l" + (wd + 36) + " " + (hd * .55) + " M" + (X[0] + wd + 18) + " " + (y0 - hd - 30) + " l" + (-wd - 36) + " " + (hd * .55),
      stroke: C.ca, "stroke-width": 7, "stroke-linecap": "round", fill: "none" }, cam);
    var stop = mode === "trou" ? lbl(s, 0, 0, v.stop || "la chaîne s'arrête", "bulle r") : null;
    var bf = v.fin ? lbl(s, W_ / 2, 22, v.fin, "ban") : null;
    var xFin = X[n - 1] + wd + 60 - W_;
    return function (t, st) {
      var tl = st.tl;
      // caméra : suit la vague, le front aux trois cinquièmes de l'image
      var front = mode === "sans_init" ? 0 : (t - tInit) / dt;
      var fx = front <= 0 ? 0 : X[Math.min(dern, Math.floor(front))] + (front % 1) * sp;
      var cx = cl(fx - W_ * .6, 0, Math.max(0, (mode === "trou" ? X[dern] + hd + 260 - W_ : xFin)));
      cam.setAttribute("transform", "translate(" + (-cx).toFixed(1) + ",0)");
      op(sol, E(P(tl, 0, .6)));
      doms.forEach(function (d, i) {
        var a = E(P(tl, .1 + Math.min(i, 24) * .035, .45));
        op(d.g, a);
        var th = angle(i, t);
        d.r.setAttribute("transform", "rotate(" + th.toFixed(2) + " " + (d.x + wd) + " " + y0 + ")");
        var tomb = th > 1 ? 1 : 0, q = P(t, depart(i) + dur * .7, .5);
        d.corps.setAttribute("fill", tomb ? hj : "rgba(238,240,230,.10)"); d.corps.setAttribute("stroke", tomb ? C.sa : C.iv);
        d.corps.style.opacity = tomb ? .75 + .25 * (1 - q) : 1;
        d.num.setAttribute("fill", tomb ? C.sa : C.iv2);
      });
      var th_ = et(v, "her", 1e9), ph = E(P(t, th_, .6)) * (1 - E(P(t, tInit + dt * (k - 1), .5)));
      op(bh, ph); trace(arc.p, P(t, th_ + .1, .7)); arc.pointe();
      op(arc.pointe(), P(t, th_ + .7, .15) * ph);
      bul.style.opacity = ph; bul.style.left = Math.max((xa + xb) / 2 - cx, bul.offsetWidth / 2 + 16) + "px"; bul.style.top = (yb - 120) + "px";
      var ti = et(v, "init", 1e9), pi = E(P(t, ti, .5)) * (1 - E(P(t, ti + 3.2, .6)));
      op(gi, mode === "sans_init" ? 0 : pi); trace(fi.p, P(t, ti, .35)); fi.pointe();
      bi.style.opacity = mode === "sans_init" ? E(P(t, ti, .5)) : pi;
      bi.style.left = Math.max(X[0] + wd / 2 - cx + (mode === "sans_init" ? 0 : 40), bi.offsetWidth / 2 + 16) + "px"; bi.style.top = (mode === "sans_init" ? y0 - hd - 200 : y0 - hd - 112) + "px";
      op(croix, mode === "sans_init" ? E(P(t, ti + .3, .4)) : 0); trace(croix, P(t, ti + .3, .5));
      if (stop) {
        var ts = depart(dern) + dur + .4;
        stop.style.opacity = E(P(t, ts, .5)); stop.style.left = Math.min(X[dern + 1] + wd / 2 - cx, W_ - stop.offsetWidth / 2 - 16) + "px"; stop.style.top = (y0 - hd - 112) + "px";
      }
      if (bf) bf.style.opacity = E(P(t, et(v, "fin", 1e9), .6));
    };
  };

  /* propagation : des cases P(n0), P(n0+1)… ; {id.init} la première est validée ; {id.her} la flèche générale
     « P(k) ⇒ P(k+1) » ; {id.go} les flèches s'enchaînent, chaque case validée à son tour ; {id.fin} « pour tout n ».
     v.vals : contenu des cases une fois validées (texte avec $maths$) ; v.prop : la propriété, en haut. */
  ILLU.propagation = function (s, v) {
    var W_ = v.w, H_ = v.h, n = v.n || 7, n0 = v.n0 || 0, dx = (W_ - 120) / n, cw = Math.min(118, dx - 26), ch = 96, y = H_ * .48;
    var hv = hachures(sv("defs", {}, s), "pg" + Math.round(alea(v.t0) * 1e6), C.vert, 13, 2.2);
    var dtp = v.dt || .75;
    var prop = v.prop ? lbl(s, W_ / 2, 8, v.prop, "titre") : null;
    var cases = [];
    for (var i = 0; i < n; i++) {
      var x = 40 + i * dx, g = sv("g", {}, s);
      var r = sv("path", { d: dPts(ptsBoite(x, y - ch / 2, cw, ch, rng(30 + i))), fill: "none", stroke: "rgba(238,240,230,.5)", "stroke-width": 2.6, "stroke-linejoin": "round" }, g);
      var nm = lbl(s, x + cw / 2, y - ch / 2 - 46, "$P(" + (n0 + i) + ")$", "pc");
      var va = lbl(s, x + cw / 2, y - 22, v.vals ? v.vals[i] : "", "pv");
      var ok = sv("path", { d: "M" + (x + cw / 2 - 14) + " " + (y + ch / 2 + 26) + " l10 12 l20 -26", fill: "none", stroke: C.vert, "stroke-width": 4.5, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      var fl = null;
      if (i < n - 1) {
        var xa = x + cw - 4, xb = x + dx + 4, ya = y - ch / 2 - 8;
        fl = fleche(g, "M" + xa + " " + ya + " Q" + (xa + xb) / 2 + " " + (ya - 40) + " " + xb + " " + (ya - 2), C.sa, 3);
        fl.k = lbl(s, (xa + xb) / 2, y + ch / 2 + 14, "$k=" + (n0 + i) + "$", "pk");
      }
      cases.push({ g: g, r: r, nm: nm, va: va, ok: ok, fl: fl, x: x });
    }
    var etc = lbl(s, 40 + n * dx - 10, y - 30, "…", "etc");
    var her = lbl(s, W_ / 2, H_ - 120, v.her || "Hérédité : pour tout $k$, $P(k)\\Rightarrow P(k+1)$", "bulle");
    var fin = lbl(s, W_ / 2, H_ - 120, v.fin || "Donc $P(n)$ est vraie pour tout $n\\geq " + n0 + "$", "ban");
    return function (t, st) {
      var tl = st.tl;
      if (prop) prop.style.opacity = E(P(tl, 0, .6));
      var ti = et(v, "init", 1e9), tg = et(v, "go", 1e9), th = et(v, "her", 1e9), tf = et(v, "fin", 1e9);
      cases.forEach(function (c, i) {
        var a = E(P(tl, .2 + i * .08, .5));
        op(c.g, a); c.nm.style.opacity = a;
        var tv = i === 0 ? ti : tg + (i - 1) * dtp + dtp * .7, q = P(t, tv, .45), on = t >= tv;
        c.r.setAttribute("fill", on ? hv : "none");
        c.r.setAttribute("stroke", on ? C.vert : "rgba(238,240,230,.5)");
        var sc = on ? 1 + .1 * Math.sin(Math.PI * q) : 1;
        c.r.setAttribute("transform", "translate(" + (c.x + cw / 2) + " " + y + ") scale(" + sc.toFixed(3) + ") translate(" + (-(c.x + cw / 2)) + " " + (-y) + ")");
        op(c.ok, E(q)); c.va.style.opacity = v.vals ? E(q) : 0;
        if (c.fl) {
          var tfl = tg + i * dtp;
          trace(c.fl.p, P(t, tfl, dtp * .7)); var pf = c.fl.pointe(); op(pf, P(t, tfl + dtp * .6, .1));
          c.fl.k.style.opacity = E(P(t, tfl + .1, .4)) * .9;
        }
      });
      etc.style.opacity = E(P(t, tg + (n - 1) * dtp, .5));
      her.style.opacity = E(P(t, th, .5)) * (1 - E(P(t, tf - .3, .4)));
      fin.style.opacity = E(P(t, tf, .5));
    };
  };

  /* la suite qui se calcule : cases u0, u1… remplies une à une (flèche « v.op » entre deux termes), puis, au repère
     {id.c}, la ligne de la formule conjecturée v.f (valeurs v.fv) et, au repère {id.ok}, les coches.
     Le terme k (k ≥ 1) apparaît au repère {id.k} (sinon toutes les 0,9 s). */
  ILLU.suite = function (s, v) {
    var W_ = v.w, H_ = v.h, n = v.termes.length, dx = Math.min(176, (W_ - 190) / n), cw = dx - 36, y1 = v.fv ? H_ * .36 : H_ * .5, y2 = H_ * .74;
    var x0 = Math.max((W_ - n * dx) / 2 + 18, 160);
    var L1 = lbl(s, 20, y1 - 26, v.l1 || "$u_n$", "lg"), L2 = v.fv ? lbl(s, 20, y2 - 26, v.f, "lg f") : null;
    var cs = v.termes.map(function (val, i) {
      var x = x0 + i * dx, g = sv("g", {}, s);
      var r = sv("path", { d: dPts(ptsBoite(x, y1 - 44, cw, 88, rng(50 + i))), fill: "none", stroke: C.te, "stroke-width": 2.6, "stroke-linejoin": "round", opacity: .8 }, g);
      var ix = lbl(s, x + cw / 2, y1 - 92, "$" + (v.lettre || "u") + "_{" + (i + (v.i0 || 0)) + "}$", "pi");
      var va = lbl(s, x + cw / 2, y1 - 25, String(val), "pv");
      var fl = null, fo = null;
      if (i < n - 1) {
        var xa = x + cw / 2 + 6, xb = x + dx + cw / 2 - 6, ya = y1 + 52;
        fl = fleche(g, "M" + xa + " " + ya + " Q" + (xa + xb) / 2 + " " + (ya + 44) + " " + xb + " " + (ya + 2), C.sa, 2.6);
        fo = lbl(s, (xa + xb) / 2, ya + 34, Array.isArray(v.op) ? v.op[i] : v.op || "", "po");
      }
      var g2 = null, v2 = null, ok = null;
      if (v.fv) {
        g2 = sv("path", { d: dPts(ptsBoite(x, y2 - 44, cw, 88, rng(70 + i))), fill: "none", stroke: C.sa, "stroke-width": 2.6, "stroke-linejoin": "round", opacity: .8 }, s);
        v2 = lbl(s, x + cw / 2, y2 - 25, String(v.fv[i]), "pv");
        ok = etiquette(s, x + cw / 2, (y1 + y2) / 2 + 22, "=", { fs: 40, c: C.vert, fw: 700 });
      }
      return { g: g, ix: ix, va: va, fl: fl, fo: fo, g2: g2, v2: v2, ok: ok };
    });
    return function (t, st) {
      var tl = st.tl;
      L1.style.opacity = E(P(tl, 0, .5));
      var tk = cs.map(function (_, i) { return i === 0 ? v.t0 + .3 : et(v, String(i), .3 + i * .9); });
      cs.forEach(function (c, i) {
        var a = E(P(t, tk[i], .5));
        op(c.g, Math.max(a, .18 * E(P(tl, 0, .5)))); c.ix.style.opacity = Math.max(a, .35 * E(P(tl, 0, .5)));
        c.va.style.opacity = a; c.va.style.transform = "translate(-50%,0) scale(" + (0.6 + 0.4 * EB(P(t, tk[i], .5))).toFixed(3) + ")";
        if (c.fl) {
          var tf = i + 1 < tk.length ? tk[i + 1] - .55 : 1e9;
          trace(c.fl.p, P(t, tf, .5)); op(c.fl.pointe(), P(t, tf + .45, .1)); c.fo.style.opacity = E(P(t, tf + .1, .4));
        }
        if (c.g2) {
          var tc = et(v, "c", 1e9) + .25 * i, q = E(P(t, tc, .5));
          op(c.g2, q); c.v2.style.opacity = q;
          op(c.ok, E(P(t, et(v, "ok", 1e9) + .15 * i, .4)));
        }
      });
      if (L2) L2.style.opacity = E(P(t, et(v, "c", 1e9), .5));
    };
  };

  /* les nombres impairs construisent des carrés : {id.k} (k = 1…5) ajoute l'équerre de 2k − 1 carreaux ;
     {id.g} le cas général : carré k × k, équerre k + k + 1. */
  ILLU.carres = function (s, v) {
    var W_ = v.w, H_ = v.h, c = v.c || 62, x0 = 70, y0 = H_ - 50;
    var dfs = sv("defs", {}, s), gid = "ca" + Math.round(alea(v.t0) * 1e6);
    var COUL = [[hachures(dfs, gid + "b", C.te, 11, 2.4), C.iv], [hachures(dfs, gid + "r", C.ca, 11, 2.4), C.iv]];
    var cel = [];
    for (var m = 0; m < 5; m++) {
      var lst = [], i;
      for (i = 0; i < m; i++) lst.push([m, i]);
      lst.push([m, m]);
      for (i = m - 1; i >= 0; i--) lst.push([i, m]);
      cel.push(lst.map(function (q, j) {
        return { r: sv("rect", { x: x0 + q[0] * c + 3, y: y0 - (q[1] + 1) * c + 3, width: c - 6, height: c - 6, rx: 3, fill: COUL[m % 2][0], stroke: COUL[m % 2][1], "stroke-width": 2.6 }, s), j: j, n: lst.length };
      }));
    }
    var SOM = ["$1=1^2$", "$1+3=4=2^2$", "$1+3+5=9=3^2$", "$1+3+5+7=16=4^2$", "$1+3+5+7+9=25=5^2$"];
    var lignes = SOM.map(function (x, i) { var d = lbl(s, 470, 40 + i * 70, x, "som"); return d; });
    // cas général
    var gg = sv("g", {}, s), K = 4;
    sv("path", { d: dPts(ptsBoite(x0 + 3, y0 - K * c + 3, K * c - 6, K * c - 6, rng(91))), fill: COUL[0][0], stroke: COUL[0][1], "stroke-width": 3, "stroke-linejoin": "round" }, gg);
    var gl = [lbl(s, x0 + K * c / 2, y0 - K * c / 2 - 24, "$k\\times k$", "gk"), lbl(s, x0 + (K + 1) * c + 26, y0 - K * c / 2 - 24, "$k$", "gr"),
      lbl(s, x0 + K * c / 2, y0 - (K + 1) * c - 52, "$k$", "gr"), lbl(s, x0 + (K + 1) * c + 26, y0 - (K + 1) * c - 52, "$1$", "gr")];
    var eq = sv("g", {}, s), eqc = [];
    for (var a = 0; a < K; a++) eqc.push([K, a]);
    eqc.push([K, K]);
    for (a = K - 1; a >= 0; a--) eqc.push([a, K]);
    eqc.forEach(function (q) { sv("rect", { x: x0 + q[0] * c + 3, y: y0 - (q[1] + 1) * c + 3, width: c - 6, height: c - 6, rx: 3, fill: COUL[1][0], stroke: COUL[1][1], "stroke-width": 2.6 }, eq); });
    var gf = [lbl(s, 470, 120, "équerre : $k+k+1=2k+1$ carreaux", "som"), lbl(s, 470, 200, "$k^2+(2k+1)=(k+1)^2$", "som gros")];
    return function (t, st) {
      var tg = et(v, "g", 1e9), avant = 1 - E(P(t, tg - .2, .5));
      cel.forEach(function (lst, m) {
        var tm = m === 0 ? et(v, "1", .3) : et(v, String(m + 1), .3 + m * 2.4);
        lst.forEach(function (q) {
          var a = q.j / q.n * .7, o = E(P(t, tm + a, .35));
          op(q.r, o * avant);
        });
        var dernier = m === 4 || t < (m + 1 < 5 ? et(v, String(m + 2), 1e9) : 1e9);
        lignes[m].style.opacity = E(P(t, tm + .6, .4)) * avant * (dernier ? 1 : .5);
      });
      var pg = E(P(t, tg, .6));
      op(gg, pg); gl.forEach(function (d, i) { d.style.opacity = E(P(t, tg + .3 + i * .2, .4)); });
      eqc.forEach(function () {});
      op(eq, E(P(t, tg + 1, .6)));
      gf[0].style.opacity = E(P(t, tg + 1.4, .5)); gf[1].style.opacity = E(P(t, et(v, "f", tg - v.t0 + 3), .5));
    };
  };

  /* le piège d'Euler : n² + n + 41 est premier pour n = 0…39 (cases cochées une à une), puis {id.40} : 1681 = 41². */
  ILLU.euler = function (s, v) {
    var W_ = v.w, H_ = v.h, cols = 10, rows = 4, cw = (W_ - 40) / cols, rh = 80, y0 = 14, dt = v.dt || .11;
    function premier(p) { if (p < 2) return false; for (var d = 2; d * d <= p; d++) if (p % d === 0) return false; return true; }
    var tuiles = [];
    for (var n = 0; n < 40; n++) {
      var x = 20 + (n % cols) * cw, y = y0 + Math.floor(n / cols) * rh, val = n * n + n + 41, g = sv("g", {}, s);
      sv("path", { d: dPts(ptsBoite(x + 6, y + 2, cw - 12, rh - 14, rng(200 + n))), fill: "none", stroke: premier(val) ? "rgba(185,227,166,.7)" : C.ca, "stroke-width": 2.2, "stroke-linejoin": "round" }, g);
      etiquette(g, x + 18, y + 26, "n = " + n, { fs: 19, c: C.iv2, ancre: "start", cls: "ser" });
      etiquette(g, x + cw / 2, y + 62, String(val).replace(/\B(?=(\d{3})+(?!\d))/g, " "), { fs: 30, c: C.iv, fw: 600, cls: "ser" });
      sv("path", { d: "M" + (x + cw - 34) + " " + (y + 18) + " l6 8 l13 -16", fill: "none", stroke: C.vert, "stroke-width": 3.4, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      tuiles.push(g);
    }
    var big = sv("g", {}, s), yb = y0 + rows * rh + 22;
    sv("path", { d: dPts(ptsBoite(W_ / 2 - 430, yb, 860, 118, rng(77))), fill: "none", stroke: C.ca, "stroke-width": 3.6, "stroke-linejoin": "round" }, big);
    if (v.titre) lbl(s, W_ / 2, -64, v.titre, "titre").style.opacity = 1;
    var tb = lbl(s, W_ / 2, yb + 14, v.t40 || "$n=40$ : $40^2+40+41=1681=41\\times41$", "eul");
    var nb = lbl(s, W_ / 2, yb + 64, "pas premier !", "eul2");
    return function (t, st) {
      var tg = et(v, "go", .4);
      tuiles.forEach(function (g, i) { var q = P(t, tg + i * dt, .3); op(g, E(q)); g.setAttribute("transform", "translate(0," + (10 * (1 - E(q))).toFixed(1) + ")"); });
      var t4 = et(v, "40", 1e9), q4 = P(t, t4, .5);
      op(big, E(q4)); big.setAttribute("transform", "translate(" + (Math.sin(Math.min(1, P(t, t4 + .5, .5)) * 22) * 6 * (1 - P(t, t4 + .5, .5))).toFixed(1) + ",0)");
      tb.style.opacity = E(q4); nb.style.opacity = E(P(t, t4 + .6, .4));
    };
  };

  /* ---------- types de visuels (tout s'écrit à la craie) ---------- */
  var TYPES = {};
  // titre de bloc : écrit à la craie jaune, souligné deux fois ; renvoie function (t, t0)
  function entete(parent, txt, cls, opt) {
    opt = opt || {};
    var d = h("div", "cr-h " + (cls || ""), parent), s = h("span", "cr-hs", d, esc(txt));
    var ec = Ecrit(s, { v: opt.v || 30 }), sl = Trait(s, opt.simple ? "souligne" : "souligne2", { ep: opt.ep || 3.4, dy: opt.dy });
    return { el: d, d: ec.d + .3, maj: function (t, t0) { ec.pose(t, t0); sl(P(t, t0 + ec.d, .3)); } };
  }

  TYPES.titre = function (o, v) {
    o.disp = "flex"; o.entree = "aucune";
    var e = o.el; e.classList.add("v-titre");
    var sur = h("div", "sur", e), sus = h("span", "", sur, esc(v.sur || ""));
    var tt = h("div", "tt", e), tts = h("span", "tts", tt);
    lettres(tts, v.t);
    var ss = h("div", "ss", e, esc(v.sous || ""));
    var e1 = Ecrit(sus, { v: 34 }), e2 = Ecrit(tts, { v: 22, max: 1.6 }), e3 = Ecrit(ss, { v: 34 });
    var sl = Trait(tts, "souligne2", { c: C.sa, ep: 5, dy: 6 });
    return function (t, st) {
      var tl = st.tl;
      e1.pose(tl, .05); e2.pose(tl, .35); sl(P(tl, .4 + e2.d, .35)); e3.pose(tl, .85 + e2.d);
    };
  };

  // carton de partie : il s'écrit sur le tableau que l'éponge vient de nettoyer
  TYPES.chapitre = function (o, v) {
    o.entree = "aucune"; o.disp = "flex";
    var e = o.el; e.classList.add("v-chapitre");
    var num = h("div", "num", e), ns = h("span", "", num, "Partie " + esc(v.num));
    var tt = h("div", "tt", e), tts = h("span", "tts", tt);
    lettres(tts, v.t);
    var e1 = Ecrit(ns, { v: 30 }), e2 = Ecrit(tts, { v: 40, max: 1.15 }), sl = Trait(tts, "souligne2", { c: C.sa, ep: 4.5, dy: 4 });
    var ent = Trait(ns, "entoure", { c: C.sa, ep: 3.2, m: 8 });
    return function (t, st) {
      var tl = st.tl, t0 = .78;
      e1.pose(tl, t0); ent(P(tl, t0 + e1.d, .3)); e2.pose(tl, t0 + .35); sl(P(tl, t0 + .4 + e2.d, .3));
    };
  };

  TYPES.mot = function (o, v) {
    var e = o.el; e.classList.add("v-mot");
    e.style.left = (v.x != null ? v.x : 140) + "px"; e.style.width = (v.w || 1000) + "px"; e.style.top = (v.y != null ? v.y : 260) + "px";
    var tt = h("div", "tt", e), tts = h("span", "", tt); tt.style.fontSize = Math.round((v.taille || 96) * 1.15) + "px";
    lettres(tts, v.t);
    var gl = v.g ? h("div", "gl", e, esc(v.g)) : null;
    var e1 = Ecrit(tts, { v: 18 }), e2 = gl ? Ecrit(gl) : null, sl = Trait(tts, "souligne2", { c: C.sa, ep: 4 });
    o.entree = "aucune";
    return function (t, st) { e1.pose(st.tl, 0); sl(P(st.tl, e1.d, .3)); if (e2) e2.pose(st.tl, e1.d + .4); };
  };

  TYPES.question = function (o, v) {
    o.disp = "flex"; o.entree = "aucune";
    var e = o.el; e.classList.add("v-question");
    var tt = h("div", "tt", e);
    var sp = mots(tt, v.t);
    sp[0].innerHTML = '<span class="gu">« </span>' + sp[0].innerHTML;
    sp[sp.length - 1].innerHTML += '<span class="gu"> »</span>';
    var ec = Ecrit(tt, { v: 20, max: 3 });
    return function (t, st) { ec.pose(st.tl, .1); };
  };

  TYPES.nuage = function (o, v) {
    o.entree = "aucune";
    var e = o.el; e.classList.add("v-nuage");
    var n = v.items.length, its = [];
    var ce = v.centre ? h("div", "ce", e, esc(v.centre)) : null, ece = ce ? Ecrit(ce) : null, ent = ce ? Trait(ce, "ellipse", { c: C.sa, m: 10 }) : null;
    v.items.forEach(function (txt, i) {
      var ang = (-90 + i * 360 / n + (alea(i) - .5) * 18) * Math.PI / 180;
      var rx = v.centre ? 400 : 360, ry = v.centre ? 220 : 190;
      var d = h("div", "it", e, esc(txt));
      if (n > 6) {
        var rangs = Math.ceil(n / 2), c = i % 2, r = Math.floor(i / 2);
        d.style.left = (c ? 920 : 360) + (alea(i) - .5) * 40 + "px";
        d.style.top = (370 + (r - (rangs - 1) / 2) * (v.centre ? 128 : 112) + (v.centre && r >= rangs / 2 ? 30 : 0) - (v.centre && r < rangs / 2 ? 30 : 0)) + "px";
        d.style.fontSize = 52 + Math.round(alea(i + 7) * 8) + "px";
      } else {
        d.style.left = (640 + Math.cos(ang) * rx) + "px"; d.style.top = (370 + Math.sin(ang) * ry) + "px";
        d.style.fontSize = (v.centre ? 54 : 66) + Math.round(alea(i + 7) * 14) + "px";
      }
      its.push({ d: d, ec: Ecrit(d) });
    });
    return function (t, st) {
      if (ce) { ece.pose(st.tl, 0); ent(P(st.tl, ece.d, .4)); }
      its.forEach(function (x, i) {
        var t0 = et(v, String(i + 1), .3 + i * .45);
        x.ec.pose(t, t0);
        x.d.style.color = t >= t0 && t < t0 + 1.4 ? C.sa : "";
      });
    };
  };

  // définition, note : titre souligné (jaune, ou rose pour une note), texte à la craie blanche, trait de marge
  function carte(o, v, note) {
    var e = o.el; o.entree = "aucune";
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 200) + "px"; e.style.width = (v.w || 940) + "px";
    var c = h("div", "carte" + (note ? " note" : ""), e);
    var te = entete(c, note ? (v.titre || "Attention") : v.terme, "te", { simple: note });
    var tx = h("div", "tx", c), sp = mots(tx, v.t, "mot-l cle"), ec = Ecrit(tx);
    var mg = Trait(c, "gauche", { c: note ? C.ca : C.sa, ep: 3, dx: 26 });
    var etp = null, eet = null, tir = null;
    if (v.etape) { etp = h("div", "et", c); var es = h("span", "", etp, esc(v.etape)); eet = Ecrit(es); tir = Trait(es, "souligne", { c: C.te, ep: 2.4, dy: 3 }); }
    var bad = v.plus ? h("div", "badge", c, "Pour aller plus loin") : null, ebad = bad ? Ecrit(bad) : null;
    var kl = cles(v, sp);
    return function (t, st) {
      var tl = st.tl;
      mg(P(tl, 0, .45)); te.maj(tl, .15);
      ec.pose(tl, .2 + te.d);
      allume(kl, t);
      if (etp) { var t1 = et(v, "1", 1.6 + ec.d) - v.t0; eet.pose(tl, t1); tir(P(tl, t1 + eet.d, .3)); }
      if (bad) ebad.pose(tl, .5);
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
    var ec = Ecrit(p), bx = Trait(p, "boite", { m: 4, ep: 2.6 });
    return function (t, st) { ec.pose(st.tl, .05); bx(P(st.tl, ec.d * .6, .5)); };
  };

  TYPES.cit = function (o, v) {
    var e = o.el; e.classList.add("v-cit"); o.entree = "aucune";
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 170) + "px"; e.style.width = (v.w || 940) + "px";
    h("div", "gu", e, "«");
    var tx = h("div", "tx", e), L = (v.t || "").length;
    tx.style.fontSize = (L <= 90 ? 54 : L <= 140 ? 48 : L <= 200 ? 42 : 38) * ((v.w || 940) < 800 ? .9 : 1) + "px";
    var sp = mots(tx, v.t, "mc");
    var au = h("div", "au", e, "— <b>" + esc(v.a || "") + "</b>" + (v.o ? ", " + esc(v.o) : "") + (v.para ? '<span class="ap">≈ citation approchée</span>' : ""));
    var m = v.m || [], n = sp.length, eau = Ecrit(au);
    var tm = sp.map(function (_, i) {
      if (!m.length) return v.t0 + .5 + i * .3;
      var j = m.length === n ? i : Math.min(m.length - 1, Math.round(i * (m.length - 1) / Math.max(1, n - 1)));
      return m[j][0];
    });
    var us = sp.map(function (s) { var u = unites(s); u.forEach(function (x) { x.a = 0; }); return u; });
    return function (t, st) {
      sp.forEach(function (s, i) {
        poser(us[i], P(t, tm[i] - .1, .25) * 30);
        s.style.color = t >= tm[i] && t < tm[i] + .9 ? C.sa : "";
      });
      eau.pose(st.tl, .7);
    };
  };

  // repère dans le temps : petite frise de -600 à 2000, point à l'année de l'auteur
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

  // portrait : un tirage photo punaisé au tableau (ruban adhésif), le nom écrit à la craie dessous
  TYPES.portrait = function (o, v) {
    var e = o.el; e.classList.add("v-portrait", "grand"); o.entree = "aucune";
    var pf = h("div", "pf", e), img;
    if (v.img) { img = h("img", "", pf); img.src = "img/" + v.img + ".jpg"; img.alt = v.nom; img.decoding = "sync"; }
    else img = h("div", "mono", pf, esc((v.nom || "?").split(" ").map(function (x) { return x[0]; }).join("")));
    h("div", "scotch a", pf); h("div", "scotch b", pf);
    var bd = h("div", "bandeau", e);
    var nm = h("div", "bd-nom", bd), nms = h("span", "", nm, esc(v.nom));
    var inf = h("div", "bd-info", bd, esc([v.dates, v.legende].filter(Boolean).join(" · ")));
    var e1 = Ecrit(nms, { v: 22 }), e2 = Ecrit(inf, { v: 40 }), sl = Trait(nms, "souligne2", { c: C.sa, ep: 3.4, dy: 2 });
    var mf = v.annee != null ? minifrise(bd, v.annee) : null;
    return function (t, st) {
      // le tirage arrive (léger retard : un tirage précédent a le temps de partir), puis repart en glissant
      var a = E(P(st.tl, .22, .6)), q = E(P(t, v.t1, .4));
      op(pf, a * (1 - q)); tr(pf, "translate(" + (-30 * (1 - a) + 90 * q).toFixed(1) + "px," + (-20 * (1 - a) + 40 * q).toFixed(1) + "px) rotate(" + (-2.2 - 3 * (1 - a) + 5 * q).toFixed(2) + "deg) scale(" + (1.04 - .04 * a).toFixed(3) + ")");
      e1.pose(st.tl, .55); sl(P(st.tl, .6 + e1.d, .3)); e2.pose(st.tl, .9 + e1.d);
      if (mf) { op(mf.f, E(P(st.tl, 1.6, .7))); op(mf.an, E(P(st.tl, 2, .5))); }
    };
  };

  TYPES.cols = function (o, v) {
    var e = o.el; e.classList.add("v-cols"); o.entree = "aucune";
    var g = h("div", "col g", e), d = h("div", "col d", e);
    var gt = h("div", "t", g, esc(v.g)), gq = h("div", "q", g, esc(v.gq || "")), dt = h("div", "t", d, esc(v.d)), dq = h("div", "q", d, esc(v.dq || ""));
    var eg = [Ecrit(gt, { v: 22 }), Ecrit(gq)], ed = [Ecrit(dt, { v: 22 }), Ecrit(dq)];
    var sg = Trait(gt, "souligne2", { c: C.sa }), sd = Trait(dt, "souligne2", { c: C.te });
    var vs = h("div", "vs", e), vss = h("span", "", vs, esc(v.vs || "≠")), evs = Ecrit(vss), cvs_ = Trait(vss, "ellipse", { c: C.ca, m: 12 });
    var rp = v.repere ? h("div", "rp", e) : null, rps = rp ? h("span", "", rp, "✻ " + esc(v.repere)) : null, erp = rp ? Ecrit(rps) : null, brp = rp ? Trait(rps, "boite", { c: C.te, m: 6, ep: 2.6 }) : null;
    var bad = v.plus ? h("div", "badge", e, "Pour aller plus loin") : null, ebad = bad ? Ecrit(bad) : null;
    return function (t, st) {
      var tg = et(v, "g", .1), td = et(v, "d", v.et && v.et["1"] ? v.et["1"] - v.t0 : .9);
      eg[0].pose(t, tg); sg(P(t, tg + eg[0].d, .3)); eg[1].pose(t, tg + eg[0].d + .3);
      ed[0].pose(t, td); sd(P(t, td + ed[0].d, .3)); ed[1].pose(t, td + ed[0].d + .3);
      var tv = Math.max(tg, td) + .5;
      evs.pose(t, tv); cvs_(P(t, tv + .2, .5));
      if (rp) { erp.pose(t, tv + .6); brp(P(t, tv + .6 + erp.d, .5)); }
      if (bad) ebad.pose(st.tl, .3);
    };
  };

  TYPES.cartes = function (o, v) {
    var e = o.el; e.classList.add("v-cartes"); if (v.petit) e.classList.add("petit"); o.entree = "aucune";
    var cs = v.items.map(function (it, i) {
      var c = h("div", "ca", e); c.style.left = (i * 380) + "px";
      var n = h("div", "n", c), ns = h("span", "", n, String(i + 1));
      var ic = icone(it.ic, c);
      var tt = h("div", "t", c, esc(it.t)), q = h("div", "q", c, esc(it.q));
      return { c: c, ic: ic, bx: Trait(c, "boite", { m: 0, ep: 2.8, c: "rgba(238,240,230,.75)" }), en: Trait(ns, "ellipse", { c: C.sa, m: 4, ep: 2.6 }),
        en_: Ecrit(ns), et_: Ecrit(tt, { v: 24 }), eq: Ecrit(q), st: Trait(tt, "souligne", { c: C.sa, ep: 3 }) };
    });
    return function (t, st) {
      var tk = cs.map(function (_, i) { return et(v, String(i + 1), .2 + i * .4); });
      var hl = v.et && v.et.hl != null ? v.et.hl : null;
      cs.forEach(function (c, i) {
        var t0 = tk[i];
        c.bx(P(t, t0, .55));
        c.en_.pose(t, t0 + .2); c.en(P(t, t0 + .3, .35));
        c.ic.forEach(function (pa, j) { trace(pa, P(t, t0 + .35 + j * .15, .6)); });
        c.et_.pose(t, t0 + .6); c.st(P(t, t0 + .6 + c.et_.d, .3)); c.eq.pose(t, t0 + .9 + c.et_.d);
        var actif = (t >= tk[i] && (i === cs.length - 1 || t < tk[i + 1]) && v.et && v.et[String(i + 1)] != null) || (hl != null && t >= hl);
        c.c.classList.toggle("actif", !!actif);
      });
    };
  };

  // liste : titre souligné deux fois, numéros entourés à la craie, coches vertes, croix roses
  TYPES.liste = function (o, v) {
    var e = o.el; e.classList.add("v-liste"); if (v.petit) e.classList.add("petit"); o.entree = "aucune";
    e.style.left = (v.x || 170) + "px"; e.style.top = (v.y || 150) + "px"; e.style.width = (v.w || 940) + "px";
    var ti = v.titre ? entete(e, v.titre, "ti") : null;
    var lis = v.items.map(function (txt, i) {
      var li = h("div", "li", e), mq = (v.marques || [])[i] || String(i + 1);
      var genre = mq === "✓" ? "ok" : mq === "✗" ? "ko" : mq === "!" ? "at" : mq === "·" ? "pt" : /^\d+$/.test(mq) ? "num" : "autre";
      var b = h("div", "mq " + genre, li), bs = h("span", "", b, esc(mq));
      var tx = h("div", "tx", li), sp = mots(tx, txt, "mot-l cle");
      return { li: li, b: b, sp: sp, eb: Ecrit(bs, { d: .25 }), et_: Ecrit(tx), cer: genre === "num" ? Trait(bs, "ellipse", { c: C.sa, m: 7, ep: 2.8 }) : null };
    });
    var kl = cles(v, [].concat.apply([], lis.map(function (l) { return l.sp; })));
    return function (t, st) {
      if (ti) ti.maj(st.tl, 0);
      allume(kl, t);
      var tk = lis.map(function (_, i) { return et(v, String(i + 1), (ti ? ti.d : 0) + .3 + i * .5); });
      var dernier = -1; tk.forEach(function (x, i) { if (t >= x) dernier = i; });
      lis.forEach(function (l, i) {
        l.eb.pose(t, tk[i]); if (l.cer) l.cer(P(t, tk[i] + .15, .35));
        l.et_.pose(t, tk[i] + .3);
        op(l.li, i === dernier || !v.et || t < tk[i] ? 1 : .72);
      });
    };
  };

  TYPES.dialogue = function (o, v) {
    var e = o.el; e.classList.add("v-dialogue"); o.entree = "aucune";
    e.style.left = (v.x || 500) + "px"; e.style.top = (v.y || 180) + "px"; e.style.width = (v.w || 680) + "px";
    var ls = v.lignes.map(function (l) { var d = h("div", "l", e, esc(l)); return Ecrit(d); });
    var src = v.src ? h("div", "src", e, esc(v.src)) : null, es = src ? Ecrit(src) : null;
    return function (t, st) {
      ls.forEach(function (l, i) { l.pose(t, et(v, String(i + 1), i * 2)); });
      if (es) es.pose(st.tl, 1);
    };
  };

  TYPES.frise = function (o, v) {
    var e = o.el; e.classList.add("v-frise"); o.entree = "aucune";
    function X(an) { return an < 500 ? 120 + (an + 500) / 1000 * 300 : 520 + (an - 1500) / 450 * 640; }
    var sa = sv("svg", { class: "fr-axe", viewBox: "0 0 1280 720" }, e);
    var axe = sv("path", { d: dPts(wob(80, 374, 1200, 371, 1.6, rng(12), 40)), fill: "none", stroke: C.sa, "stroke-width": 3.4, "stroke-linecap": "round" }, sa);
    var pointeA = sv("path", { d: "M1186 360 L1204 371 L1186 384", fill: "none", stroke: C.sa, "stroke-width": 3.4, "stroke-linecap": "round", "stroke-linejoin": "round" }, sa);
    var rupt = h("div", "rupt", e, "≈"); rupt.style.left = "470px";
    var ans = [[-400, "−400"], [0, "0"], [1600, "1600"], [1700, "1700"], [1800, "1800"], [1900, "1900"]].map(function (a) {
      var d = h("div", "an", e, a[1]); d.style.left = X(a[0]) + "px"; return d;
    });
    var RANGS = [{ top: 210, tige: [84, 78] }, { top: 420, tige: [-48, 48] }, { top: 66, tige: [84, 222] }, { top: 560, tige: [-188, 188] }];
    var tri = v.items.slice().sort(function (a, b) { return a.d - b.d; });
    var fin = RANGS.map(function () { return -1e9; }), serre = false;
    tri.forEach(function (it) { var x = X(it.d), r = 0; while (r < RANGS.length - 1 && x - fin[r] < 128) r++; fin[r] = x; if (r > 1) serre = true; });
    var pas = 0;
    if (serre) { rupt.style.display = "none"; ans.forEach(function (a) { a.style.display = "none"; }); pas = tri.length > 1 ? 1040 / (tri.length - 1) : 0; }
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
      var nm = h("div", "nm", p, esc(it.nom)), dt = h("div", "dt", p, it.d < 0 ? "−" + (-it.d) : String(it.d));
      var q = it.q ? h("div", "q", p, esc(it.q)) : null;
      return { p: p, k: v.items.indexOf(it) + 1, md: md, e: [Ecrit(dt), Ecrit(nm), q ? Ecrit(q) : null] };
    });
    return function (t, st) {
      trace(axe, EIO(P(st.tl, 0, 1.2))); trace(pointeA, P(st.tl, 1.15, .2));
      op(rupt, E(P(st.tl, 1, .5))); ans.forEach(function (a) { op(a, E(P(st.tl, 1, .6))); });
      its.forEach(function (x, i) {
        var t0 = et(v, String(x.k), .8 + i * .28);
        op(x.p, t >= t0 ? 1 : 0); op(x.md, E(P(t, t0, .4)));
        x.e[0].pose(t, t0 + .1); x.e[1].pose(t, t0 + .25); if (x.e[2]) x.e[2].pose(t, t0 + .5);
      });
    };
  };

  // tableau (photo, œuvre) : en fond, une image projetée, très pâle, sur l'ardoise ; sinon un tirage punaisé au tableau
  TYPES.tableau = function (o, v) {
    var e = o.el; e.classList.add("v-tableau"); if (v.fond) e.classList.add("fond-t"); if (v.sombre) e.classList.add("sombre"); o.entree = "aucune";
    var cadre = h("div", "tb-cadre", e), img = h("img", "", cadre); img.alt = v.legende || ""; img.decoding = "sync";
    var pret = false, enCours = false;
    function charge() {
      if (enCours) return; enCours = true;
      img.style.width = img.naturalWidth + "px"; img.style.height = img.naturalHeight + "px";
      var fin = function () { pret = true; };
      if (img.decode) img.decode().then(fin, fin); else fin();
    }
    o.attente = new Promise(function (r) { var k = setInterval(function () { if (pret) { clearInterval(k); r(); } }, 30); });
    img.addEventListener("load", charge);
    img.src = "img/" + v.img + ".jpg";
    if (!v.fond) { h("div", "scotch a", cadre); h("div", "scotch b", cadre); }
    var lg = v.legende ? h("div", "lg", e, esc(v.legende)) : null;
    var de = v.de || [1.15, .5, .4], a_ = v.a || [1, .5, .5];
    // tirage : 900 × 506 au centre (cadre de 16/9), légèrement de travers
    var CW = v.fond ? W : 900, CH = v.fond ? H : 506;
    return function (t, st) {
      if (!pret && img.complete && img.naturalWidth) charge();
      var iw = img.naturalWidth || 1600, ih = img.naturalHeight || 900;
      var u = EIO(P(t, v.t0, Math.max(4, v.t1 - v.t0 + .6)));
      var z = de[0] + (a_[0] - de[0]) * u, fx = de[1] + (a_[1] - de[1]) * u, fy = de[2] + (a_[2] - de[2]) * u;
      var sc = Math.max(CW / iw, CH / ih) * z, w = iw * sc, hh = ih * sc;
      var x = cl(CW / 2 - fx * w, CW - w, 0), y = cl(CH / 2 - fy * hh, CH - hh, 0);
      img.style.transform = "translate3d(" + x.toFixed(2) + "px," + y.toFixed(2) + "px,0) scale(" + sc.toFixed(5) + ")";
      var a = pret ? E(P(t, v.t0, v.fond ? 1.2 : .7)) * (1 - EIO(P(t, v.t1, .9))) : 0;
      op(e, a);
      if (!v.fond) tr(cadre, "translate(-50%,-50%) rotate(" + (1.4 - 2.5 * (1 - E(P(t, v.t0, .8)))).toFixed(2) + "deg) scale(" + (1.03 - .03 * E(P(t, v.t0, .8))).toFixed(3) + ")");
      if (lg) op(lg, E(P(st.tl, 1.2, .8)) * .9);
    };
  };

  // générique : le titre de la série s'écrit sur l'ardoise
  TYPES.generique = function (o, v) {
    var e = o.el; e.classList.add("v-generique"); o.entree = "aucune"; o.disp = "flex";
    var haut = h("div", "g-haut", e), hs = h("span", "", haut, "CQFD · Maths Terminale");
    var tt = h("div", "g-titre", e), tts = h("span", "", tt); lettres(tts, v.serie);
    tt.style.fontSize = Math.min(132, Math.floor(2700 / Math.max(12, String(v.serie).length))) + "px";
    var bas = h("div", "g-bas", e), bs = h("span", "", bas, "Le cours en vidéo · chapitre " + v.num);
    var e1 = Ecrit(hs, { v: 30 }), e2 = Ecrit(tts, { v: 18, max: 1.8 }), e3 = Ecrit(bs, { v: 34 });
    var en = Trait(hs, "entoure", { c: C.sa, m: 9, ep: 3 }), sl = Trait(tts, "souligne2", { c: C.sa, ep: 5.5, dy: 8 });
    return function (t, st) {
      var tl = st.tl;
      e1.pose(tl, .3); en(P(tl, .3 + e1.d, .4));
      e2.pose(tl, 1.0); sl(P(tl, 1.05 + e2.d, .4)); e3.pose(tl, 1.6 + e2.d);
      op(e, 1 - EIO(P(t, v.t1 - .5, .6)));
    };
  };

  // notions du programme abordées : petite note en haut à droite
  TYPES.notion = function (o, v) {
    var e = o.el; e.classList.add("v-notion"); o.entree = "aucune"; o.disp = "flex";
    if (v.titre) e.classList.add("liste");
    var tete = h("div", "nt-t", e, esc(v.titre || "Notion"));
    var pills = v.items.map(function (x, i) { return h("span", "nt-p" + (v.titre && i === 0 ? " prin" : ""), e, esc(x.charAt(0).toUpperCase() + x.slice(1))); });
    var ec = Ecrit(e, { v: 40 }), bx = Trait(e, "boite", { m: 2, ep: 2.4, c: C.sa });
    return function (t, st) {
      var tl = st.tl, d = v.t1 - v.t0;
      ec.pose(tl, .05); bx(P(tl, ec.d * .5, .5)); op(e, 1 - EIO(P(tl, d - .6, .6)));
    };
  };

  // mot qui frappe : un coin de tableau propre, le mot écrit en grand, à la craie jaune, souligné deux fois
  TYPES.frappe = function (o, v) {
    var e = o.el; e.classList.add("v-frappe"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fr-fond", e), m = h("div", "fr-mot", e), ms = h("span", "", m);
    lettres(ms, v.t);
    m.style.fontSize = Math.min(170, Math.floor(1250 / (String(v.t).length * 0.62))) + "px";
    var ec = Ecrit(ms, { d: .45 }), sl = Trait(ms, "souligne2", { c: C.sa, ep: 6, dy: 6 });
    return function (t, st) {
      var tl = st.tl, out = P(tl, 1.15, .4);
      op(fond, E(P(tl, 0, .18)) * (1 - E(out)));
      op(m, 1 - E(out));
      ec.pose(tl, .05); sl(P(tl, .5, .25));
    };
  };

  // « À retenir » de fin de partie : un cadre jaune tracé à la craie, sur un coin de tableau propre
  TYPES.flash = function (o, v) {
    var e = o.el; e.classList.add("v-flash"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fl-fond", e), c = h("div", "fl-carte", e);
    var te = entete(c, "À retenir", "fl-te", {});
    var tx = h("div", "fl-tx", c); mots(tx, v.t);
    var ec = Ecrit(tx, { v: 60, max: 1.6 }), bx = Trait(c, "boite", { c: C.sa, m: 0, ep: 4 });
    return function (t, st) {
      var tl = st.tl, out = o.efface ? 0 : EIO(P(t, v.t1 - .3, .6));
      op(fond, E(P(tl, 0, .4)) * (1 - out)); op(c, 1 - out);
      bx(P(tl, .15, .6)); te.maj(tl, .3); ec.pose(tl, .4 + te.d);
    };
  };

  // carte mentale : centre entouré, branches tracées, nœuds encadrés
  TYPES.carte = function (o, v) {
    var e = o.el; e.classList.add("v-carte"); o.entree = "aucune";
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H }, e);
    var POS = [[360, 92], [920, 92], [360, 470], [920, 470]];
    var centre = h("div", "cm-centre", e), cs = h("span", "", centre, esc(v.centre)), ece = Ecrit(cs), ent = Trait(cs, "ellipse", { c: C.sa, m: 12, ep: 3.6 });
    var br = (v.branches || []).map(function (b, i) {
      var p = POS[i], ex = p[0] + (p[0] < 640 ? 80 : -80), d = "M640 330 C" + (640 + (ex - 640) * .5) + " 330 " + ex + " " + (330 + (p[1] - 330) * .5) + " " + ex + " " + (p[1] + (p[1] < 330 ? 18 : -18));
      var ln = sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 3.4, "stroke-linecap": "round", opacity: .85 }, svg);
      var nd = h("div", "cm-noeud", e), nds = h("span", "", nd, esc(b.t)); nd.style.left = p[0] + "px"; nd.style.top = p[1] + "px";
      var gauche = p[0] < 640, col = h("div", "cm-items" + (gauche ? " g" : " d"), e);
      col.style.left = (gauche ? p[0] - 300 : p[0] - 40) + "px"; col.style.top = (p[1] + 40) + "px";
      var its = b.items.map(function (x) { return Ecrit(h("div", "cm-it", col, esc(x))); });
      return { ln: ln, end: Ecrit(nds), bx: Trait(nds, "boite", { m: 7, ep: 2.6 }), its: its };
    });
    return function (t, st) {
      ece.pose(st.tl, 0); ent(P(st.tl, ece.d, .5));
      br.forEach(function (b, i) {
        var tk = et(v, String(i + 1), .6 + i * 1.2);
        trace(b.ln, P(t, tk, .7));
        b.end.pose(t, tk + .55); b.bx(P(t, tk + .55 + b.end.d, .4));
        b.its.forEach(function (it, j) { it.pose(t, tk + .9 + j * .35); });
      });
    };
  };

  TYPES.illu = function (o, v) {
    var e = o.el; e.classList.add("v-illu"); o.entree = "aucune";
    e.style.left = v.x + "px"; e.style.top = v.y + "px"; e.style.width = v.w + "px"; e.style.height = v.h + "px";
    var s = sv("svg", { viewBox: "0 0 " + v.w + " " + v.h }, e);
    var bad = v.plus ? h("div", "badge", e, "Pour aller plus loin") : null;
    if (bad) bad.style.top = "-10px";
    var f = ILLU[v.nom] ? ILLU[v.nom](s, v) : function () {};
    // les étiquettes posées sur l'illustration s'écrivent à la craie dès qu'elles apparaissent
    // (fonction pure du temps : la part écrite suit l'opacité que l'illustration donne à l'étiquette)
    var labs = Array.prototype.slice.call(e.querySelectorAll(".il-lab")).map(function (d) { return { d: d, ec: Ecrit(d, { v: 34 }) }; });
    return function (t, st) {
      f(t, st);
      labs.forEach(function (x) { x.ec.u(cl(parseFloat(x.d.style.opacity || "0") / .45, 0, 1)); });
    };
  };

  /* ---------- types propres aux maths ---------- */

  // formule : lignes écrites au repère {id.k} ; cadre=True : la relation à retenir, entourée à la craie jaune ; lab :
  // étiquette en tête de ligne (« Hérédité. ») ; ind : ligne en retrait (suite d'un calcul) ; m : note de marge à la craie
  // rose ; hl=True : la ligne est soulignée en jaune au repère {id.hk} (k = numéro de la ligne), sinon après son écriture ;
  // ok / ko : craie verte (coche) / rose (croix) ; n : précision sous la ligne ; v.copie : la rédaction au tableau
  // (trait de marge, étiquettes en bleu soulignées) ; v.plus : badge « Hors programme » ; taille : corps de la ligne.
  var K_CRAIE = 1.12;   // la craie (Caveat) est plus étroite que l'ancienne police : même encombrement, lettres plus grandes
  TYPES.formule = function (o, v) {
    var e = o.el; e.classList.add("v-formule"); if (v.copie) e.classList.add("copie"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 150) + "px"; e.style.top = (v.y != null ? v.y : 150) + "px"; e.style.width = (v.w || 980) + "px";
    var c = h("div", "fo-carte" + (v.nu ? " nu" : ""), e);
    var marge = null;   // (la rédaction au tableau n'a pas de trait de marge : il doublerait le trait qui sépare l'énoncé de la correction)
    var te = v.titre ? entete(c, v.titre, "fo-te") : null;
    var ls = v.lignes.map(function (l) {
      if (typeof l === "string") l = { f: l };
      var d = h("div", "fo-l" + (l.cadre ? " encadre" : "") + (l.txt ? " txt" : "") + (l.pt ? " pt" : "") + (l.ko ? " ko" : "") + (l.ok ? " ok" : "") + (l.hl ? " hl" : "") + (l.ind ? " ind" : ""), c);
      if (l.taille) d.style.fontSize = Math.round(l.taille * K_CRAIE) + "px";
      var col = h("div", "fo-c", d);
      var f = h("div", "fo-f", col, (l.lab ? '<b class="fo-lab">' + esc(l.lab) + "</b> " : "") + "<span class=\"fo-s\">" + esc(l.f) + "</span>");
      var n = l.n ? h("div", "fo-n", col, esc(l.n)) : null;
      var m = l.m ? h("div", "fo-m", d, esc(l.m)) : null;
      var s = f.querySelector(".fo-s"), lab = f.querySelector(".fo-lab");
      return { d: d, l: l, ef: Ecrit(f), en: n ? Ecrit(n, { v: 40 }) : null, em: m ? Ecrit(m, { v: 30 }) : null,
        cad: l.cadre ? Trait(f, "entoure", { c: C.sa, ep: 3.8, m: 13 }) : null,
        sl: l.hl ? Trait(s, "souligne", { c: C.sa, ep: 5, dy: 1 }) : null,
        lb: lab ? Trait(lab, "souligne", { c: C.te, ep: 2.6, dy: 0 }) : null,
        mq: l.ok ? Trait(f, "coche", { c: C.vert, ep: 4.4 }) : l.ko ? Trait(f, "croix", { c: C.ca, ep: 4 }) : null };
    });
    var bad = v.plus ? h("div", "badge", c, "Hors programme") : null, ebad = bad ? Ecrit(bad) : null;
    return function (t, st) {
      var tl = st.tl;
      if (marge) marge(P(tl, 0, .5));
      if (te) te.maj(tl, .05);
      if (bad) ebad.pose(tl, .3);
      ls.forEach(function (x, i) {
        var t1 = et(v, String(i + 1), .25 + i * 1.1), fin = t1 + x.ef.d;
        x.ef.pose(t, t1);
        if (x.lb) x.lb(P(t, t1 + x.ef.d * .25, .25));
        if (x.en) x.en.pose(t, fin + .1);
        if (x.mq) x.mq(P(t, fin + .05, .3));
        if (x.cad) x.cad(P(t, fin + .15, .55));
        if (x.em) x.em.pose(t, Math.max(et(v, "m" + (i + 1), t1 - v.t0 + .6), t1 + .3));
        if (x.sl) x.sl(P(t, Math.max(et(v, "h" + (i + 1), t1 - v.t0 + .7), fin), .45));
      });
    };
  };

  // coloration minimale de Python (mots clés, nombres, chaînes, commentaires), en craies de couleur
  var MOTS_PY = /^(def|return|while|for|in|if|else|elif|and|or|not|range|print|True|False|None|import|from)$/;
  function colore(src) {
    return String(src).split(/(#.*$|"[^"]*"|'[^']*'|[A-Za-z_]\w*|\d+(?:\.\d+)?)/).map(function (p, i) {
      if (!(i % 2)) return escT(p);
      if (p[0] === "#") return '<span class="py-com">' + escT(p) + "</span>";
      if (p[0] === '"' || p[0] === "'") return '<span class="py-str">' + escT(p) + "</span>";
      if (/^\d/.test(p)) return '<span class="py-num">' + p + "</span>";
      return MOTS_PY.test(p) ? '<span class="py-kw">' + p + "</span>" : p;
    }).join("");
  }
  // code Python écrit au tableau : « @1 », « @2 »… sont des trous (« ... ») complétés par v.rep[k-1] au repère {id.rk} ;
  // la ligne k est montrée (flèche jaune) à partir du repère {id.lk} ; v.sortie : ce qu'affiche le programme, au repère {id.s}
  TYPES.code = function (o, v) {
    var e = o.el; e.classList.add("v-code"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 170) + "px"; e.style.top = (v.y != null ? v.y : 120) + "px"; e.style.width = (v.w || 940) + "px";
    var c = h("div", "cd-carte", e);
    var te = entete(c, v.titre || "Python", "cd-te", { simple: true });
    var pre = h("div", "cd-pre", c), trous = [];
    if (v.taille) pre.style.fontSize = v.taille + "px";
    var ls = v.lignes.map(function (l, i) {
      var d = h("div", "cd-l", pre);
      h("span", "cd-n", d, String(i + 1));
      var tx = h("span", "cd-t", d), mes = [];
      l.split(/(@\d)/).forEach(function (p) {
        if (/^@\d$/.test(p)) {
          var k = +p[1], tr_ = h("span", "cd-trou", tx);
          var a = h("span", "cd-a", tr_, "..."), b = h("span", "cd-b", tr_, colore((v.rep || [])[k - 1] || ""));
          trous.push({ k: k, a: a, b: b, eb: null });
        } else tx.insertAdjacentHTML("beforeend", colore(p));
      });
      return { d: d, tx: tx };
    });
    // écriture ligne à ligne (les trous gardent leurs points de suspension, leur réponse s'écrit plus tard)
    trous.forEach(function (x) { x.b.classList.add("hors"); });
    var tl0 = .25 + te.d;
    ls.forEach(function (l) { l.ec = Ecrit(l.tx, { v: 70, max: .9 }); l.t0 = tl0; tl0 += l.ec.d * .8 + .02; });
    trous.forEach(function (x) { x.b.classList.remove("hors"); x.eb = Ecrit(x.b, { v: 20 }); });
    var bx = Trait(c, "boite", { m: 0, ep: 2.8, c: "rgba(238,240,230,.55)" });
    var so = v.sortie != null ? h("div", "cd-so", c, '<span class="cd-p">&gt;&gt;&gt;</span>' + escT(v.sortie).replace(/\n/g, "<br>")) : null;
    var eso = so ? Ecrit(so, { v: 50 }) : null;
    return function (t, st) {
      var tl = st.tl;
      bx(P(tl, 0, .6)); te.maj(tl, .1);
      var act = -1;
      ls.forEach(function (d, i) { var k = v.et && v.et["l" + (i + 1)]; if (k != null && t >= k && (act < 0 || k >= v.et["l" + (act + 1)])) act = i; });
      ls.forEach(function (l, i) { l.ec.pose(tl, l.t0); op(l.d, act < 0 || act === i ? 1 : .55); l.d.classList.toggle("on", act === i); });
      trous.forEach(function (x) {
        var tr0 = et(v, "r" + x.k, 1e9), q = t >= tr0;
        x.a.style.display = q ? "none" : ""; x.b.style.display = q ? "" : "none";
        x.eb.pose(t, tr0);
      });
      if (so) eso.pose(t, et(v, "s", 1e9));
    };
  };

  // graphique : les axes sont tracés à la règle (elle glisse sous l'axe des abscisses, puis le long de l'axe des
  // ordonnées, puis s'en va), puis les éléments (courbe, droite, point(s), texte, rect, balaye, toile) au repère {id.k}
  TYPES.graphe = function (o, v) {
    var e = o.el; e.classList.add("v-graphe"); o.entree = "aucune";
    var Wd = v.w || 600, Hd = v.h || 480;
    e.style.left = (v.x != null ? v.x : 640) + "px"; e.style.top = (v.y != null ? v.y : 110) + "px"; e.style.width = Wd + "px"; e.style.height = Hd + "px";
    var m = v.marges || [86, 26, 44, 70], pw = Wd - m[0] - m[1], ph = Hd - m[2] - m[3], ax = v.ax;
    function X(x) { return m[0] + (x - ax.x[0]) / (ax.x[1] - ax.x[0]) * pw; }
    function Y(y) { return m[2] + (1 - (y - ax.y[0]) / (ax.y[1] - ax.y[0])) * ph; }
    var s = sv("svg", { viewBox: "0 0 " + Wd + " " + Hd, width: Wd, height: Hd }, e);
    var lab = h("div", "gr-lab", e);
    var ti = v.titre ? h("div", "gr-ti", e, esc(v.titre)) : null, eti = ti ? Ecrit(ti, { v: 40 }) : null;
    function txt(x, y, html, cls) { var d = h("div", "gr-t " + (cls || ""), lab, html); d.style.left = x + "px"; d.style.top = y + "px"; return d; }
    var fond = sv("g", {}, s), grille = [], ticks = [], R = rng(Math.round(Wd + Hd + (v.t0 || 0)));
    var x0 = cl(0, ax.x[0], ax.x[1]), y0 = cl(0, ax.y[0], ax.y[1]);
    (ax.gx || []).forEach(function (x) {
      grille.push(sv("path", { d: dPts(wob(X(x), m[2] + ph, X(x), m[2], 1, R)), stroke: "rgba(238,240,230,.12)", "stroke-width": 1.6, fill: "none" }, fond));
      ticks.push(txt(X(x), Y(y0) + 10, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("path", { d: dPts(wob(m[0], Y(y), m[0] + pw, Y(y), 1, R)), stroke: "rgba(238,240,230,.12)", "stroke-width": 1.6, fill: "none" }, fond));
      ticks.push(txt(X(x0) - 12, Y(y), esc(String(y).replace(".", ",")), "ty"));
    });
    var axX = sv("path", { d: dPts(wob(m[0] - 4, Y(y0), m[0] + pw + 14, Y(y0) - 1, .8, R)), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, s);
    var axY = sv("path", { d: dPts(wob(X(x0), m[2] + ph + 4, X(x0) + 1, m[2] - 14, .8, R)), stroke: C.iv, "stroke-width": 3, fill: "none", "stroke-linecap": "round" }, s);
    var fl1 = sv("path", { d: "M" + (m[0] + pw + 4) + " " + (Y(y0) - 9) + " L" + (m[0] + pw + 17) + " " + Y(y0) + " L" + (m[0] + pw + 4) + " " + (Y(y0) + 9), fill: "none", stroke: C.iv, "stroke-width": 3, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    var fl2 = sv("path", { d: "M" + (X(x0) - 9) + " " + (m[2] - 4) + " L" + X(x0) + " " + (m[2] - 17) + " L" + (X(x0) + 9) + " " + (m[2] - 4), fill: "none", stroke: C.iv, "stroke-width": 3, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    var lx = txt(m[0] + pw + 4, Y(y0) + 34, esc(ax.lx || ""), "lx"), ly = txt(X(x0) + 14, m[2] - 34, esc(ax.ly || ""), "ly");
    // la règle en bois
    var rg = h("img", "regle", e); rg.src = TEX.regle || ""; rg.alt = "";
    var LR = 760;
    rg.style.width = (LR + 40) + "px"; rg.style.height = "150px";
    var poseA = { x: m[0] - 30, y: Y(y0) + 1, a: 0 }, poseB = { x: X(x0) - 1, y: m[2] + ph + 34, a: -90 }, poseO = { x: Wd + 700, y: Y(y0) - 120, a: -6 };
    var poseI = { x: Wd + 600, y: Y(y0) + 40, a: 4 };
    function pose(p) { rg.style.transform = "translate(" + (p.x - 10).toFixed(1) + "px," + (p.y - 110).toFixed(1) + "px) rotate(" + p.a.toFixed(2) + "deg)"; }
    function mel(p, q, u) { return { x: p.x + (q.x - p.x) * u, y: p.y + (q.y - p.y) * u, a: p.a + (q.a - p.a) * u }; }
    function chemin(pts) { return "M" + pts.map(function (p) { return X(p[0]).toFixed(1) + " " + Y(p[1]).toFixed(1); }).join(" L"); }
    function sur(pts, x) {
      for (var i = 0; i < pts.length - 1; i++) if (x <= pts[i + 1][0]) { var u = (x - pts[i][0]) / ((pts[i + 1][0] - pts[i][0]) || 1); return pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u; }
      return pts[pts.length - 1][1];
    }
    var els = (v.el || []).map(function (d) {
      var col = C[d.c] || d.c || C.sa, g = sv("g", { opacity: 0 }, s), x = { d: d, g: g };
      if (d.type === "courbe" || d.type === "droite") {
        x.p = sv("path", { d: chemin(d.pts), stroke: col, "stroke-width": (d.ep || 3.6) * 1.1, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
        if (d.tir) { x.p.setAttribute("stroke-dasharray", "10 9"); x.tir = true; }
        if (d.lbl) x.l = txt(X(d.lp[0]), Y(d.lp[1]), esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "point" || d.type === "points") {
        x.c = (d.type === "point" ? [[d.x, d.y]] : d.pts).map(function (p) {
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col }, g);
        });
        if (d.proj) x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 2.2, "stroke-dasharray": "6 7", "stroke-linecap": "round", fill: "none", opacity: .85 }, g);
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "toile") {
        var u = d.u, tp = [[u[0], ax.y[0] < 0 && ax.y[1] > 0 ? 0 : ax.y[0]]];
        for (var q = 1; q < u.length; q++) { tp.push([u[q - 1], u[q]]); tp.push([u[q], u[q]]); }
        x.p = sv("path", { d: chemin(tp), stroke: col, "stroke-width": (d.ep || 3) * 1.1, fill: "none", "stroke-linejoin": "round", "stroke-linecap": "round" }, g);
        var cum = [0];
        for (q = 1; q < tp.length; q++) cum.push(cum[q - 1] + Math.hypot(X(tp[q][0]) - X(tp[q - 1][0]), Y(tp[q][1]) - Y(tp[q - 1][1])));
        x.cum = cum.map(function (c_) { return c_ / (cum[cum.length - 1] || 1); });
        x.proj = []; x.ul = [];
        var nl = d.nlab != null ? d.nlab : 4;
        for (q = 0; q < u.length; q++) {
          if (q >= 1) x.proj.push(sv("path", { d: "M" + X(u[q]) + " " + Y(u[q]) + " V" + Y(y0), stroke: col, "stroke-width": 2, "stroke-dasharray": "5 7", "stroke-linecap": "round", fill: "none", opacity: 0 }, g));
          if (q <= nl) { var ul_ = txt(X(u[q]), Y(y0) + 40, esc("$" + (d.lettre || "u") + "_{" + q + "}$"), "tx ul"); ul_.style.color = col; ul_.style.opacity = 0; x.ul.push(ul_); }
        }
      } else if (d.type === "rect" || d.type === "balaye") {
        x.hid = "gh" + Math.round(alea((v.t0 || 0) + (v.el || []).indexOf(d)) * 1e6);
        var hf = hachures(sv("defs", {}, g), x.hid, col, 12, 2.4);
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: hf, stroke: col, "stroke-width": 2.6 }, g);
        x.pt = sv("circle", { r: 8, fill: col }, g);
        x.l = txt(0, 0, "", "lb"); x.l.style.color = col;
      }
      if (x.l) { x.l.style.opacity = 0; if (d.type !== "rect" && d.type !== "balaye") x.el_ = Ecrit(x.l, { v: 34 }); }
      return x;
    });
    var tAx = v.tax != null ? v.tax : 0;
    return function (t, st) {
      var tl = st.tl - tAx;
      if (ti) eti.pose(st.tl, 0);
      // la règle : arrivée, axe des x, bascule, axe des y, départ
      var p = tl < 0 ? mel(poseI, poseA, EIO(P(tl, -.45, .45))) : tl < .55 ? poseA : tl < .9 ? mel(poseA, poseB, EIO(P(tl, .55, .35))) : tl < 1.35 ? poseB : mel(poseB, poseO, EIO(P(tl, 1.35, .5)));
      var vu = tl > -.45 && tl < 1.85;
      rg.style.display = vu ? "" : "none";
      if (vu) pose(p);
      trace(axX, P(tl, .05, .45)); trace(axY, P(tl, .92, .4));
      trace(fl1, P(tl, .5, .12)); trace(fl2, P(tl, 1.3, .12));
      grille.forEach(function (gg, i) { trace(gg, P(tl, 1.3 + i * .05, .35)); });
      ticks.forEach(function (tk) { op(tk, E(P(tl, 1.4, .5))); });
      op(lx, E(P(tl, .55, .4))); op(ly, E(P(tl, 1.35, .4)));
      els.forEach(function (x, i) {
        var d = x.d, t1 = et(v, String(i + 1), 1.2 + i * 1.4), dur = d.dur || (d.type === "courbe" ? 1.8 : d.type === "droite" ? 1.2 : .5);
        x.g.setAttribute("opacity", (t >= t1 ? 1 : 0) * (d.fin != null && v.et && v.et[d.fin] != null ? 1 - E(P(t, v.et[d.fin], .5)) : 1));
        if (x.p && d.type === "toile") {
          var dt_ = d.dur || 1.1 * (d.u.length - 1), pr = P(t, t1, dt_);
          trace(x.p, pr);
          x.proj.forEach(function (pj, q) { pj.setAttribute("opacity", pr >= x.cum[2 * (q + 1)] - 1e-6 ? .75 : 0); });
          x.ul.forEach(function (lb, q) { lb.style.opacity = E((pr - (q ? x.cum[2 * q] : 0)) * 8); });
        } else if (x.p) {
          if (x.tir) { var pt_ = EIO(P(t, t1, dur)); x.p.style.clipPath = pt_ < 1 ? "inset(0 " + (100 * (1 - pt_)).toFixed(1) + "% 0 0)" : ""; }
          else trace(x.p, EIO(P(t, t1, dur)));
        }
        if (x.c) x.c.forEach(function (c, j) { var q = P(t, t1 + j * (d.pas || .18), .3); c.setAttribute("r", ((d.r || 6.5) * E(q)).toFixed(2)); });
        if (x.pj) { op(x.pj, t >= t1 + .3 ? .85 : 0); x.pj.style.clipPath = ""; }
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
        if (x.l) {
          var tl_ = t1 + (x.p ? dur * .6 : .2);
          if (x.el_) { x.l.style.opacity = t >= tl_ ? 1 : 0; x.el_.pose(t, tl_); }
          else x.l.style.opacity = E(P(t, tl_, .5));
        }
      });
    };
  };

  // exercice : énoncé au tableau (mode « plein »), ou rappel compact à gauche, séparé par un trait, pendant la correction
  // (mode « coin ») ; niveau d'un exercice ; v.etiquette remplace le libellé (« Exercice 2 · type bac »…)
  var NIVEAUX = { simple: ["Exercice 1 · pour démarrer", C.vert], difficile: ["Exercice 2 · plus difficile", C.sa], bac: ["Exercice 3 · type bac", C.ca] };
  TYPES.exo = function (o, v) {
    var e = o.el, coin = v.mode === "coin"; e.classList.add("v-exo", coin ? "coin" : "plein"); o.entree = "aucune";
    if (!coin) { e.style.left = (v.x || 110) + "px"; e.style.top = (v.y || 96) + "px"; e.style.width = (v.w || 1060) + "px"; }
    var c = h("div", "ex-carte", e), nv = (NIVEAUX[v.niveau] || [v.niveau || "Exercice", C.sa]).slice();
    if (v.etiquette) nv[0] = v.etiquette;
    var tag = h("div", "ex-nv", c), tgs = h("span", "", tag, esc(nv[0])); tag.style.color = nv[1];
    var etag = Ecrit(tgs, { v: 40 }), stag = Trait(tgs, "souligne", { c: nv[1], ep: 2.8 });
    var ti = h("div", "ex-ti", c), tis = h("span", "", ti, esc(v.titre)), eti = Ecrit(tis, { v: 30 }), sti = Trait(tis, "souligne2", { c: C.sa, ep: 3.2 });
    var src = v.src ? h("div", "ex-src", c, esc(v.src)) : null, esrc = src ? Ecrit(src, { v: 50 }) : null;
    var paras = (coin ? [] : v.enonce || []).map(function (p) { return Ecrit(h("p", "ex-p", c, esc(p)), { v: 34, max: 2.4 }); });
    var don = v.donnees && v.donnees.length ? h("div", "ex-don", c, "<b>Données</b> " + v.donnees.map(esc).join(" &nbsp;·&nbsp; ")) : null;
    var edon = don ? Ecrit(don, { v: 40 }) : null;
    var qs = (v.questions || []).map(function (q, i) {
      var d = h("div", "ex-q", c), n = h("span", "ex-qn", d), ns = h("span", "", n, String(i + 1)), tq = h("span", "ex-qt", d, esc(q));
      return { d: d, en: Ecrit(ns, { d: .2 }), cer: Trait(ns, "ellipse", { c: C.sa, m: coin ? 2 : 5, ep: coin ? 2.2 : 2.6 }), et_: Ecrit(tq, { v: coin ? 60 : 34 }) };
    });
    var sep = coin ? Trait(c, "droite", { c: "rgba(238,240,230,.45)", ep: 2.6, dx: 18 }) : null;
    var vit = coin ? .55 : 1;
    return function (t, st) {
      var tl = st.tl;
      if (sep) sep(P(tl, 0, .6));
      etag.pose(tl, .1); stag(P(tl, .1 + etag.d, .25));
      var tt = .35 + etag.d * vit;
      eti.pose(tl, tt); sti(P(tl, tt + eti.d, .3)); tt += eti.d + .2;
      if (src) { esrc.pose(tl, tt); tt += esrc.d * vit; }
      paras.forEach(function (p, i) { p.pose(t, et(v, "p" + (i + 1), tt + i * .5)); });
      if (don) edon.pose(t, et(v, "d", tt + paras.length * .5 + .2));
      var actif = -1;
      qs.forEach(function (q, i) { var k = v.et && v.et["q" + (i + 1)]; if (k != null && t >= k) actif = i; });
      qs.forEach(function (q, i) {
        var t1 = coin ? v.t0 + tt + .2 + i * .45 : et(v, String(i + 1), tt + .5 + paras.length * .5 + i * .4);
        q.en.pose(t, t1); q.cer(P(t, t1 + .1, .3)); q.et_.pose(t, t1 + .25);
        op(q.d, actif < 0 || actif === i ? 1 : .5);
        q.d.classList.toggle("on", actif === i);
      });
    };
  };

  // « À toi » : la vidéo s'arrête d'elle-même (si l'option est active) pour que l'élève cherche avant la correction
  TYPES.pause = function (o, v) {
    var e = o.el; e.classList.add("v-pause"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 200) + "px"; e.style.top = (v.y != null ? v.y : 130) + "px"; e.style.width = (v.w || 880) + "px";
    var c = h("div", "pa-carte", e);
    var ic = sv("svg", { class: "pa-ic", viewBox: "0 0 100 100" }, c), R = rng(41);
    var b1 = sv("path", { d: dPts(wob(38, 26, 37, 74, 1.2, R, 4)), fill: "none", stroke: C.sa, "stroke-width": 9, "stroke-linecap": "round" }, ic);
    var b2 = sv("path", { d: dPts(wob(62, 26, 63, 74, 1.2, R, 4)), fill: "none", stroke: C.sa, "stroke-width": 9, "stroke-linecap": "round" }, ic);
    var ce = sv("path", { d: dPts(ptsEllipse(50, 50, 40, 40, R, 1.08)), fill: "none", stroke: C.sa, "stroke-width": 4, "stroke-linecap": "round" }, ic);
    var te = h("div", "pa-te", c), tes = h("span", "", te, "À toi !"), ete = Ecrit(tes, { d: .45 }), ste = Trait(tes, "souligne2", { c: C.sa, ep: 4 });
    var tx = h("div", "pa-tx", c, esc(v.t)), etx = Ecrit(tx, { v: 34 });
    var so = h("div", "pa-so", c, esc(v.sous || "Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction.")), eso = Ecrit(so, { v: 60 });
    var bx = Trait(c, "boite", { c: C.sa, m: 0, ep: 3.4 });
    return function (t, st) {
      var tl = st.tl;
      bx(P(tl, 0, .6)); trace(ce, P(tl, .1, .5)); trace(b1, P(tl, .45, .15)); trace(b2, P(tl, .6, .15));
      ete.pose(tl, .35); ste(P(tl, .85, .3)); etx.pose(tl, 1.0); eso.pose(tl, 1.1 + etx.d);
    };
  };

  /* ---------- scène : l'ardoise, la couche de craie, l'éponge entre les parties ---------- */
  var NE = 240;   // empreintes de l'éponge par passage
  function epongeEn(s) {   // position de l'éponge (coordonnées 1920 × 1080) à l'avancement s ∈ [0, 1] du nettoyage
    var y = 470 - 640 * Math.cos(Math.PI * 4 * s), x = 70 + s * 1640;
    return { x: x, y: y, a: .1 * Math.sin(Math.PI * 4 * s) };
  }
  function empreinte(g, p) { g.save(); g.translate(p.x, p.y); g.rotate(p.a); rrect(g, -235, -95, 470, 190, 34); g.restore(); }

  function Scene(EP, racine) {
    var sc = h("div", "scene", racine);
    if (!TEX.grain) TEX.grain = grain();
    if (!TEX.regle) TEX.regle = regle(760);
    if (!TEX.eponge) TEX.eponge = eponge();
    sc.style.setProperty("--grain", "url(" + TEX.grain + ")");
    var ard = h("canvas", "ardoise", sc); ard.width = 1920; ard.height = 1080;
    // l'ardoise attend la police de la craie (fantômes d'anciennes leçons)
    var pretArd = (document.fonts && document.fonts.load ? document.fonts.load("700 60px Caveat", "Δab√") : Promise.resolve()).catch(function () {}).then(function () {
      if (!TEX.planche) { TEX.planche = planche(true); TEX.plancheURL = TEX.planche.toDataURL("image/jpeg", .9); }
      ard.getContext("2d").drawImage(TEX.planche, 0, 0);
      sc.style.setProperty("--planche", "url(" + TEX.plancheURL + ")");
    });
    var resid = h("canvas", "eponge-r", sc); resid.width = 1920; resid.height = 1080;
    var rx = resid.getContext("2d");
    var pc = h("canvas", "poussiere", sc); pc.width = W; pc.height = H;
    var cx = pc.getContext("2d");
    var parts = []; for (var i = 0; i < 46; i++) parts.push({ x: alea(i) * W, y: alea(i + 100) * H, vx: (alea(i + 200) - .5) * 6, vy: 2 + alea(i + 300) * 6, r: .6 + alea(i + 400) * 1.3, ph: alea(i + 500) * 6.28 });   // poussière de craie
    var couche = h("div", "couche", sc);
    var dessus = h("canvas", "eponge-d", sc); dessus.width = 1920; dessus.height = 1080;
    var dx_ = dessus.getContext("2d");
    h("div", "voile", sc);
    var ent = h("div", "entete", sc), fil = h("div", "fil", sc), st = h("div", "st", sc), stS = h("span", "", st);
    var objs = EP.vis.map(function (v) {
      var el = h("div", "v", couche), o = { v: v, el: el, disp: "block", entree: "monte", vis: false };
      el.style.display = "none";
      o.upd = (TYPES[v.type] || function () { return function () {}; })(o, v);
      if (!/^(tableau|portrait|graphe|frappe|flash)$/.test(v.type)) el.classList.add("craie");
      return o;
    });
    // un coup d'éponge au début de chaque partie (sauf la première)
    var NET = EP.scenes.slice(1).map(function (s) { return { t0: s.t0 - .12, t1: s.t0 + .8 }; });
    // ce qui est encore au tableau à la fin d'une partie y reste jusqu'au passage de l'éponge
    objs.forEach(function (o) { NET.forEach(function (w) { if (o.v.t1 >= w.t0 - 1.5 && o.v.t1 <= w.t1 && !/^(tableau|notion|generique)$/.test(o.v.type)) o.efface = w.t1; }); });
    // passage de relais (11/11/2026, pilote : « gros problèmes de chevauchements ») : quand un visuel commence pendant
    // que le précédent est encore au tableau, le précédent s'efface juste avant (fondu fini au début du suivant), sinon
    // la craie écrit le nouveau texte par-dessus l'ancien ; le minutage du nouveau, calé sur la voix, ne bouge pas
    var SANS_RELAIS = /^(tableau|notion|generique|frappe|flash)$/;
    var FONDU = .42;
    objs.forEach(function (w) {
      w.fin = w.v.t1;
      if (SANS_RELAIS.test(w.v.type) || w.efface) return;
      objs.forEach(function (o) {
        if (o === w || SANS_RELAIS.test(o.v.type)) return;
        if (w.v.t0 < o.v.t0 - 1 && w.v.t1 > o.v.t0 - FONDU && w.v.t1 < o.v.t0 + 3) w.fin = Math.min(w.fin, o.v.t0 - FONDU - .04);
      });
    });
    var MOUILLE = null;   // trace humide de tout le passage (calculée une fois)
    function mouille() {
      if (MOUILLE) return MOUILLE;
      MOUILLE = cvs(1920, 1080); var g = MOUILLE.getContext("2d");
      g.filter = "blur(12px)"; g.fillStyle = "#000";
      for (var k = 0; k <= NE; k += 2) { empreinte(g, epongeEn(k / NE)); g.fill(); }
      g.filter = "none";
      return MOUILLE;
    }
    function chemin(g, s) { g.beginPath(); for (var k = 0; k <= NE; k++) { var q = k / NE; if (q > s) break; var p = epongeEn(q); g.save(); g.translate(p.x, p.y); g.rotate(p.a); rrect(g, -235, -95, 470, 190, 34, true); g.restore(); } }
    var resSale = true, dessusSale = true;
    function eponger(t) {
      var w = null;
      for (var k = 0; k < NET.length; k++) if (t > NET[k].t0 - .3 && t < NET[k].t1 + 2.6) { w = NET[k]; break; }
      if (!w) {
        if (resSale) { rx.clearRect(0, 0, 1920, 1080); resSale = false; }
        if (dessusSale) { dx_.clearRect(0, 0, 1920, 1080); dessusSale = false; }
        return;
      }
      var d = w.t1 - w.t0, s = EIO(P(t, w.t0, d));
      // trace humide sur l'ardoise (sous la craie), qui sèche en deux secondes
      rx.clearRect(0, 0, 1920, 1080); resSale = true;
      var wet = .28 * (1 - EIO(P(t, w.t1 - .2, 2.4)));
      if (wet > .003 && t >= w.t1) { rx.globalAlpha = wet; rx.drawImage(mouille(), 0, 0); rx.globalAlpha = 1; }
      // le tableau propre recouvre la craie là où l'éponge est passée ; l'éponge, la poussière qu'elle soulève
      dx_.clearRect(0, 0, 1920, 1080); dessusSale = true;
      if (t > w.t0 && t < w.t1 + .03 && TEX.planche) {
        dx_.save(); chemin(dx_, s); dx_.clip(); dx_.drawImage(TEX.planche, 0, 0);
        dx_.globalAlpha = wet; dx_.drawImage(mouille(), 0, 0); dx_.restore();
      }
      var p;
      if (t < w.t0) { var p0 = epongeEn(0), u = E(P(t, w.t0 - .28, .28)); p = { x: p0.x - 520 * (1 - u), y: p0.y + 640 * (1 - u), a: p0.a }; }
      else if (t > w.t1) { var p1 = epongeEn(1), u2 = Math.pow(P(t, w.t1, .32), 2); p = { x: p1.x + 620 * u2, y: p1.y + 720 * u2, a: p1.a }; }
      else p = epongeEn(s);
      if (t > w.t0 - .3 && t < w.t1 + .33) { dx_.save(); dx_.translate(p.x, p.y); dx_.rotate(p.a); dx_.drawImage(TEX.eponge, -280, -130); dx_.restore(); }
      var n = 70;
      for (k = 0; k < n; k++) {
        var q = (k + alea(k)) / n, tk = w.t0 + q * d, age = t - tk;
        if (age < 0 || age > 1.1) continue;
        var pk = epongeEn(q), ox = (alea(k + 9) - .5) * 420, oy = (alea(k + 19) - .5) * 160;
        dx_.globalAlpha = .55 * (1 - age / 1.1); dx_.fillStyle = "#E8ECE2";
        dx_.beginPath(); dx_.arc(pk.x + ox + (alea(k + 29) - .5) * 60 * age, pk.y + oy + 260 * age * age, 1.5 + alea(k + 39) * 2.5, 0, 6.283); dx_.fill();
      }
      dx_.globalAlpha = 1;
    }
    var sousOn = false, dernierSous = -1;

    function rendu(t) {
      eponger(t);
      // poussière de craie qui flotte dans la lumière
      cx.clearRect(0, 0, W, H);
      parts.forEach(function (p) {
        var x = ((p.x + p.vx * t) % W + W) % W, y = ((p.y + p.vy * t) % H + H) % H;
        var a = .08 + .08 * Math.sin(t * 1.3 + p.ph);
        cx.fillStyle = "rgba(232,238,228," + a.toFixed(3) + ")";
        cx.beginPath(); cx.arc(x, y, p.r, 0, 6.283); cx.fill();
      });
      // visuels
      var plein = false;
      objs.forEach(function (o) {
        var v = o.v;
        if (t < v.t0 || t > (o.efface ? o.efface + .03 : o.fin < v.t1 ? o.fin + FONDU + .03 : v.t1 + (v.type === "tableau" ? 1 : .6))) { if (o.vis) { o.el.style.display = "none"; o.vis = false; } return; }
        if (!o.vis) { o.el.style.display = o.disp; o.vis = true; }
        if (v.type === "titre" || v.type === "chapitre" || v.type === "generique" || v.type === "portrait") plein = true;   // le portrait monte jusqu'en haut : pas d'en-tête dessus
        var a = E(P(t, v.t0, .7)), out = o.efface ? 0 : EIO(P(t, o.fin, FONDU));
        if (v.type !== "tableau") o.el.style.opacity = (o.entree === "aucune" ? 1 : a) * (1 - out);
        if (o.entree === "monte") o.el.style.transform = "translateY(" + (20 * (1 - a)).toFixed(2) + "px)";
        o.upd(t, { tl: t - v.t0, a: a, o: out });
      });
      // en-tête : chapitre, partie (écrit en petit, en haut à gauche du tableau)
      var sc_ = EP.scenes.filter(function (s) { return t >= s.t0; }).pop() || EP.scenes[0];
      var txt = "Chapitre " + EP.num + (sc_.id !== EP.scenes[0].id ? " &nbsp;·&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
      if (ent._t !== txt) { ent.innerHTML = txt; ent._t = txt; }
      op(ent, plein ? 0 : E(P(t, EP.scenes[0].t0 + 1, 1)) * .85);
      fil.style.width = (W * cl(t / EP.dur, 0, 1)).toFixed(1) + "px";
      // sous-titres
      if (sousOn) {
        var k = -1;
        for (var i = 0; i < EP.sous.length; i++) { if (EP.sous[i][0] <= t && t < EP.sous[i][1]) { k = i; break; } }
        if (k !== dernierSous) { stS.textContent = k >= 0 ? EP.sous[k][2] : ""; st.style.display = k >= 0 ? "block" : "none"; dernierSous = k; }
      } else st.style.display = "none";
    }
    return { el: sc, rendu: rendu, sous: function (b) { sousOn = b; dernierSous = -2; },
      attentes: function () { return [pretArd].concat(objs.filter(function (o) { return o.attente; }).map(function (o) { return o.attente; })); } };
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
    document.title = "Chapitre " + EP.num + " — " + EP.titre + " · Maths Terminale";
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
      h("span", "k", tete, "Maths · chapitre " + EP.num + " · le cours en vidéo");
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
        navigator.mediaSession.metadata = new MediaMetadata({ title: "Ch. " + EP.num + " · " + EP.titre, artist: "Maths · le cours en vidéo", album: "Terminale spécialité" });
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
