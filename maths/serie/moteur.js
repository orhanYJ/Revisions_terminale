/* Vidéos de cours de maths (site « CQFD ») — moteur du lecteur, copie du moteur PC (pc/serie/moteur.js) aux couleurs
   du site en mode « tableau noir » (ardoise, craie, surligneur jaune, encre bleue, stylo rouge).
   Propre aux maths : les formules s'écrivent en $…$ (syntaxe compacte du site, sous-ensemble de LaTeX) et sont rendues
   en MathML natif avec la police du site (Carnet Math, sous-ensemble de STIX Two Math) ; $$…$$ = style « display ».
   Le convertisseur est une copie de outils/specialites/maths/src/mathml.js (à recopier s'il change).
   Types ajoutés ou étendus : formule (note de marge manuscrite m, étiquette lab, copie=True : la rédaction sur une page
   de carnet), code (Python, trous complétés au repère {id.r1}…, sortie au repère {id.s}), graphe (élément toile :
   toile d'araignée d'une suite u(n+1) = f(u(n))), illustrations dominos, propagation, suite, carres, euler.
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py depuis outils/serie-maths/<module>.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  // craie, surligneur jaune, encre bleue claire, stylo rouge, vert de la coche
  var C = { iv: "#ECEBE4", iv2: "#BFC4BB", sa: "#F4D35E", sa2: "#E0B53A", ca: "#FF907E", te: "#9CC3F0", bleu: "#9CC3F0", nuit: "#1b2422",
    el: "#9CC3F0", rouge: "#FF907E", vert: "#8FD6A8", or: "#F4D35E" };

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
  // les espaces d'une formule ne coupent pas les mots (mots allumés un à un, lettres une à une)
  function proteger(s) { return String(s).replace(/\$\$?[^$]+\$\$?/g, function (m) { return m.replace(/[ \t\n]/g, "\u0001"); }); }
  function rendre(s) { return s.replace(/\u0001/g, " "); }
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
    insec(proteger(txt)).split(/([ \t\n]+)/).forEach(function (m) {
      if (/^[ \t\n]+$/.test(m)) { el.appendChild(document.createTextNode(" ")); return; }
      var w = h("span", "mot-l", el);
      if (m.indexOf("$") >= 0) { out.push(h("span", "lettre", w, esc(rendre(m)))); return; }   // une formule entre d'un bloc
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
    if (sp.querySelector("math")) { sp._mot = sp; return sp; }   // une formule s'allume en bloc
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
      c.sp.style.textShadow = "0 0 " + (18 * (1 - f)).toFixed(1) + "px rgba(244,211,94," + (0.7 * (1 - f)).toFixed(2) + ")";
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
      return sv("path", { d: d, fill: "none", stroke: C.sa, "stroke-width": 4.5, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
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
    var sol = sv("line", { x1: -200, x2: x0 + n * sp + 400, y1: y0, y2: y0, stroke: "rgba(236,235,228,.35)", "stroke-width": 2 }, cam);
    var X = [], xs = x0;
    for (var i = 0; i < n; i++) { X.push(xs); xs += (mode === "trou" && i === v.trou - 1) ? Math.max(sp, hd + 40) : sp; }
    var doms = X.map(function (x, i) {
      var g = sv("g", {}, cam), r = sv("g", {}, g);
      var corps = sv("rect", { x: x, y: y0 - hd, width: wd, height: hd, rx: 4, fill: "#ECEBE4", stroke: "#0f1614", "stroke-width": 1.5 }, r);
      sv("line", { x1: x + 3, x2: x + wd - 3, y1: y0 - hd / 2, y2: y0 - hd / 2, stroke: "#5b6661", "stroke-width": 1.5 }, r);
      [.25, .75].forEach(function (f) { sv("circle", { cx: x + wd / 2, cy: y0 - hd * f, r: 2.6, fill: "#2b3632" }, r); });
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
        d.corps.setAttribute("fill", tomb ? (q < 1 ? "#F7E7A6" : "#F4D35E") : "#ECEBE4");
        d.num.setAttribute("fill", tomb ? C.sa : C.iv2);
      });
      var th_ = et(v, "her", 1e9), ph = E(P(t, th_, .6)) * (1 - E(P(t, tInit + dt * (k - 1), .5)));
      op(bh, ph); trace(arc.p, P(t, th_ + .1, .7)); arc.pointe();
      op(arc.pointe(), P(t, th_ + .7, .15) * ph);
      bul.style.opacity = ph; bul.style.left = Math.max((xa + xb) / 2 - cx, bul.offsetWidth / 2 + 16) + "px"; bul.style.top = (yb - 120) + "px";
      var ti = et(v, "init", 1e9), pi = E(P(t, ti, .5)) * (1 - E(P(t, ti + 3.2, .6)));
      op(gi, mode === "sans_init" ? 0 : pi); trace(fi.p, P(t, ti, .35)); fi.pointe();
      bi.style.opacity = mode === "sans_init" ? E(P(t, ti, .5)) : pi;
      bi.style.left = Math.max(X[0] + wd / 2 - cx + (mode === "sans_init" ? 0 : 40), bi.offsetWidth / 2 + 16) + "px"; bi.style.top = (y0 - hd - 112) + "px";
      op(croix, mode === "sans_init" ? E(P(t, ti + .3, .4)) : 0); trace(croix, P(t, ti + .3, .5));
      if (stop) {
        var ts = depart(dern) + dur + .4;
        stop.style.opacity = E(P(t, ts, .5)); stop.style.left = (X[dern + 1] + wd / 2 - cx) + "px"; stop.style.top = (y0 - hd - 112) + "px";
      }
      if (bf) bf.style.opacity = E(P(t, et(v, "fin", 1e9), .6));
    };
  };

  /* propagation : des cases P(n0), P(n0+1)… ; {id.init} la première est validée ; {id.her} la flèche générale
     « P(k) ⇒ P(k+1) » ; {id.go} les flèches s'enchaînent, chaque case validée à son tour ; {id.fin} « pour tout n ».
     v.vals : contenu des cases une fois validées (texte avec $maths$) ; v.prop : la propriété, en haut. */
  ILLU.propagation = function (s, v) {
    var W_ = v.w, H_ = v.h, n = v.n || 7, n0 = v.n0 || 0, dx = (W_ - 120) / n, cw = Math.min(118, dx - 26), ch = 96, y = H_ * .48;
    var dtp = v.dt || .75;
    var prop = v.prop ? lbl(s, W_ / 2, 8, v.prop, "titre") : null;
    var cases = [];
    for (var i = 0; i < n; i++) {
      var x = 40 + i * dx, g = sv("g", {}, s);
      var r = sv("rect", { x: x, y: y - ch / 2, width: cw, height: ch, rx: 14, fill: "rgba(236,235,228,.05)", stroke: "rgba(236,235,228,.35)", "stroke-width": 2 }, g);
      var nm = lbl(s, x + cw / 2, y - ch / 2 - 46, "$P(" + (n0 + i) + ")$", "pc");
      var va = lbl(s, x + cw / 2, y - 22, v.vals ? v.vals[i] : "", "pv");
      var ok = etiquette(g, x + cw / 2, y + ch / 2 + 42, "✓", { fs: 34, c: C.vert, fw: 700 });
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
        c.r.setAttribute("fill", on ? "rgba(143,214,168,.16)" : "rgba(236,235,228,.05)");
        c.r.setAttribute("stroke", on ? C.vert : "rgba(236,235,228,.35)");
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
      var r = sv("rect", { x: x, y: y1 - 44, width: cw, height: 88, rx: 14, fill: "rgba(156,195,240,.09)", stroke: "rgba(156,195,240,.6)", "stroke-width": 2 }, g);
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
        g2 = sv("rect", { x: x, y: y2 - 44, width: cw, height: 88, rx: 14, fill: "rgba(244,211,94,.08)", stroke: "rgba(244,211,94,.55)", "stroke-width": 2 }, s);
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
    var COUL = [["rgba(156,195,240,.30)", "#9CC3F0"], ["rgba(255,144,126,.28)", "#FF907E"]];
    var cel = [];
    for (var m = 0; m < 5; m++) {
      var lst = [], i;
      for (i = 0; i < m; i++) lst.push([m, i]);
      lst.push([m, m]);
      for (i = m - 1; i >= 0; i--) lst.push([i, m]);
      cel.push(lst.map(function (q, j) {
        return { r: sv("rect", { x: x0 + q[0] * c + 2, y: y0 - (q[1] + 1) * c + 2, width: c - 4, height: c - 4, rx: 6, fill: COUL[m % 2][0], stroke: COUL[m % 2][1], "stroke-width": 2 }, s), j: j, n: lst.length };
      }));
    }
    var SOM = ["$1=1^2$", "$1+3=4=2^2$", "$1+3+5=9=3^2$", "$1+3+5+7=16=4^2$", "$1+3+5+7+9=25=5^2$"];
    var lignes = SOM.map(function (x, i) { var d = lbl(s, 470, 40 + i * 70, x, "som"); return d; });
    // cas général
    var gg = sv("g", {}, s), K = 4;
    sv("rect", { x: x0 + 2, y: y0 - K * c + 2, width: K * c - 4, height: K * c - 4, rx: 8, fill: COUL[0][0], stroke: COUL[0][1], "stroke-width": 2 }, gg);
    var gl = [lbl(s, x0 + K * c / 2, y0 - K * c / 2 - 24, "$k\\times k$", "gk"), lbl(s, x0 + (K + 1) * c + 26, y0 - K * c / 2 - 24, "$k$", "gr"),
      lbl(s, x0 + K * c / 2, y0 - (K + 1) * c - 52, "$k$", "gr"), lbl(s, x0 + (K + 1) * c + 26, y0 - (K + 1) * c - 52, "$1$", "gr")];
    var eq = sv("g", {}, s), eqc = [];
    for (var a = 0; a < K; a++) eqc.push([K, a]);
    eqc.push([K, K]);
    for (a = K - 1; a >= 0; a--) eqc.push([a, K]);
    eqc.forEach(function (q) { sv("rect", { x: x0 + q[0] * c + 2, y: y0 - (q[1] + 1) * c + 2, width: c - 4, height: c - 4, rx: 6, fill: COUL[1][0], stroke: COUL[1][1], "stroke-width": 2 }, eq); });
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
    var W_ = v.w, H_ = v.h, cols = 10, rows = 4, cw = (W_ - 40) / cols, rh = 86, y0 = 20, dt = v.dt || .11;
    function premier(p) { if (p < 2) return false; for (var d = 2; d * d <= p; d++) if (p % d === 0) return false; return true; }
    var tuiles = [];
    for (var n = 0; n < 40; n++) {
      var x = 20 + (n % cols) * cw, y = y0 + Math.floor(n / cols) * rh, val = n * n + n + 41, g = sv("g", {}, s);
      sv("rect", { x: x + 4, y: y, width: cw - 8, height: rh - 10, rx: 10, fill: "rgba(143,214,168,.12)", stroke: premier(val) ? "rgba(143,214,168,.7)" : C.ca, "stroke-width": 1.6 }, g);
      etiquette(g, x + 16, y + 26, "n = " + n, { fs: 20, c: C.iv2, ancre: "start", cls: "ser" });
      etiquette(g, x + cw / 2, y + 62, String(val).replace(/\B(?=(\d{3})+(?!\d))/g, " "), { fs: 30, c: C.iv, fw: 600, cls: "ser" });
      etiquette(g, x + cw - 20, y + 26, "✓", { fs: 22, c: C.vert, fw: 700 });
      tuiles.push(g);
    }
    var big = sv("g", {}, s), yb = y0 + rows * rh + 22;
    sv("rect", { x: W_ / 2 - 430, y: yb, width: 860, height: 118, rx: 18, fill: "rgba(255,144,126,.14)", stroke: C.ca, "stroke-width": 3 }, big);
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
        mf.pt.style.boxShadow = "0 0 " + (6 + 8 * Math.max(0, Math.sin(t * 3))) + "px rgba(244,211,94,.9)";
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
        c.c.style.borderColor = actif ? "rgba(244,211,94," + (0.5 + 0.4 * pul) + ")" : "rgba(236,235,228,.14)";
        c.c.style.boxShadow = actif ? "0 0 " + (30 + 20 * pul) + "px rgba(244,211,94,.25)" : "none";
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
    var halo = h("div", "g-halo", e), haut = h("div", "g-haut", e, "Maths · Terminale · CQFD");
    var l1 = h("div", "g-ligne", e), tt = h("div", "g-titre", e), sp = lettres(tt, v.serie);
    tt.style.fontSize = Math.min(120, Math.floor(2300 / Math.max(12, String(v.serie).length))) + "px"; tt.style.textAlign = "center";
    var l2 = h("div", "g-ligne", e), bas = h("div", "g-bas", e, "Le cours en vidéo · chapitre " + v.num);
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
    var POS = [[360, 92], [920, 92], [360, 470], [920, 470]];
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
      centre.style.boxShadow = "0 0 " + (20 + 12 * Math.sin(t * 2)) + "px rgba(244,211,94,.35)";
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

  /* ---------- types propres aux maths ---------- */

  // formule : lignes qui apparaissent au repère {id.k} ; cadre=True encadre la relation à retenir ; lab : étiquette en
  // tête de ligne (« Hérédité. ») ; ind : ligne en retrait (suite d'un calcul) ; m : note de marge manuscrite, au stylo rouge ; hl=True : la ligne est surlignée au
  // repère {id.hk} (k = numéro de la ligne), sinon peu après son apparition ; v.copie : la rédaction sur une page de
  // carnet (papier clair, encre bleue, marge rouge) ; v.plus : badge « Hors programme »
  TYPES.formule = function (o, v) {
    var e = o.el; e.classList.add("v-formule"); if (v.copie) e.classList.add("copie");
    e.style.left = (v.x != null ? v.x : 150) + "px"; e.style.top = (v.y != null ? v.y : 150) + "px"; e.style.width = (v.w || 980) + "px";
    var c = h("div", "fo-carte" + (v.nu ? " nu" : ""), e);
    if (v.copie) h("div", "fo-marge", c);
    var te = v.titre ? h("div", "fo-te", c, esc(v.titre)) : null;
    var ls = v.lignes.map(function (l) {
      if (typeof l === "string") l = { f: l };
      var d = h("div", "fo-l" + (l.cadre ? " encadre" : "") + (l.txt ? " txt" : "") + (l.pt ? " pt" : "") + (l.ko ? " ko" : "") + (l.ok ? " ok" : "") + (l.hl ? " hl" : "") + (l.ind ? " ind" : ""), c);
      if (l.taille) d.style.fontSize = l.taille + "px";
      var col = h("div", "fo-c", d);
      var f = h("div", "fo-f", col, (l.lab ? '<b class="fo-lab">' + esc(l.lab) + "</b> " : "") + "<span class=\"fo-s\">" + esc(l.f) + "</span>");
      var n = l.n ? h("div", "fo-n", col, esc(l.n)) : null;
      var m = l.m ? h("div", "fo-m", d, esc(l.m)) : null;
      return { d: d, n: n, m: m, l: l, s: f.querySelector(".fo-s") };
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
          x.d.style.boxShadow = v.copie ? "0 0 0 2px rgba(35,67,168," + (.8 * E(q)).toFixed(2) + ")"
            : "0 0 0 2px rgba(244,211,94," + (.85 * E(q)).toFixed(2) + "),0 0 " + (34 * (1 - q) + 14 + 10 * g).toFixed(0) + "px rgba(244,211,94," + (.32 * E(q) + .1 * g).toFixed(2) + ")";
        }
        if (x.n) op(x.n, E(P(t, t1 + .45, .6)));
        if (x.m) { var pm = E(P(t, et(v, "m" + (i + 1), t1 - v.t0 + .6), .6)); op(x.m, pm); tr(x.m, "rotate(-2.5deg) translateX(" + (12 * (1 - pm)).toFixed(1) + "px)"); }
        if (x.l.hl) x.s.style.backgroundSize = (100 * EIO(P(t, et(v, "h" + (i + 1), t1 - v.t0 + .7), .7))).toFixed(1) + "% 100%";
      });
    };
  };

  // coloration minimale de Python (mots clés, nombres, chaînes, commentaires)
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
  // code Python : « @1 », « @2 »… sont des trous (« ... ») complétés par v.rep[k-1] au repère {id.rk} ; la ligne k est
  // mise en valeur à partir du repère {id.lk} ; v.sortie : ce qu'affiche le programme, au repère {id.s}
  TYPES.code = function (o, v) {
    var e = o.el; e.classList.add("v-code");
    e.style.left = (v.x != null ? v.x : 170) + "px"; e.style.top = (v.y != null ? v.y : 120) + "px"; e.style.width = (v.w || 940) + "px";
    var c = h("div", "cd-carte", e);
    var te = h("div", "cd-te", c, '<span class="cd-pt"></span><span class="cd-pt"></span><span class="cd-pt"></span>' + escT(v.titre || "Python"));
    var pre = h("div", "cd-pre", c), trous = [];
    if (v.taille) pre.style.fontSize = v.taille + "px";
    var ls = v.lignes.map(function (l, i) {
      var d = h("div", "cd-l", pre);
      h("span", "cd-n", d, String(i + 1));
      var tx = h("span", "cd-t", d);
      l.split(/(@\d)/).forEach(function (p) {
        if (/^@\d$/.test(p)) {
          var k = +p[1], tr_ = h("span", "cd-trou", tx);
          trous.push({ k: k, a: h("span", "cd-a", tr_, "..."), b: h("span", "cd-b", tr_, colore((v.rep || [])[k - 1] || "")) });
        } else tx.insertAdjacentHTML("beforeend", colore(p));
      });
      return d;
    });
    var so = v.sortie != null ? h("div", "cd-so", c, '<span class="cd-p">&gt;&gt;&gt;</span>' + escT(v.sortie).replace(/\n/g, "<br>")) : null;
    return function (t, st) {
      op(te, E(P(st.tl, 0, .4)));
      var act = -1;
      ls.forEach(function (d, i) { var k = v.et && v.et["l" + (i + 1)]; if (k != null && t >= k && (act < 0 || k >= v.et["l" + (act + 1)])) act = i; });
      ls.forEach(function (d, i) { op(d, E(P(st.tl, .15 + i * .07, .4)) * (act < 0 || act === i ? 1 : .55)); d.classList.toggle("on", act === i); });
      trous.forEach(function (x) {
        var q = P(t, et(v, "r" + x.k, 1e9), .5);
        x.a.style.display = q > 0 ? "none" : ""; x.b.style.display = q > 0 ? "" : "none";
        op(x.b, E(q)); x.b.style.backgroundSize = (100 * EIO(P(t, et(v, "r" + x.k, 1e9) + .2, .6))).toFixed(1) + "% 100%";
      });
      if (so) { var q = E(P(t, et(v, "s", 1e9), .5)); op(so, q); tr(so, "translateY(" + (10 * (1 - q)).toFixed(1) + "px)"); }
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
      grille.push(sv("line", { x1: X(x), x2: X(x), y1: m[2], y2: m[2] + ph, stroke: "rgba(236,235,228,.09)", "stroke-width": 1 }, fond));
      ticks.push(txt(X(x), Y(y0) + 12, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("line", { x1: m[0], x2: m[0] + pw, y1: Y(y), y2: Y(y), stroke: "rgba(236,235,228,.09)", "stroke-width": 1 }, fond));
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
          return sv("circle", { cx: X(p[0]), cy: Y(p[1]), r: d.r || 6.5, fill: col, stroke: "#0f1614", "stroke-width": 1.5 }, g);
        });
        if (d.proj) {
          x.pj = sv("path", { d: "M" + X(d.x) + " " + Y(d.y) + " V" + Y(y0) + " M" + X(d.x) + " " + Y(d.y) + " H" + X(x0), stroke: col, "stroke-width": 1.6, "stroke-dasharray": "5 5", fill: "none", opacity: .8 }, g);
        }
        if (d.lbl) x.l = txt(X(d.lp ? d.lp[0] : d.x), Y(d.lp ? d.lp[1] : d.y) - 26, esc(d.lbl), "lb"), x.l.style.color = col;
      } else if (d.type === "texte") {
        x.l = txt(X(d.x), Y(d.y), esc(d.t), "lb " + (d.cls || "")); x.l.style.color = col;
      } else if (d.type === "toile") {
        var u = d.u, tp = [[u[0], ax.y[0] < 0 && ax.y[1] > 0 ? 0 : ax.y[0]]];
        for (var q = 1; q < u.length; q++) { tp.push([u[q - 1], u[q]]); tp.push([u[q], u[q]]); }
        x.p = sv("path", { d: chemin(tp), stroke: col, "stroke-width": d.ep || 3, fill: "none", "stroke-linejoin": "round" }, g);
        var cum = [0];
        for (q = 1; q < tp.length; q++) cum.push(cum[q - 1] + Math.hypot(X(tp[q][0]) - X(tp[q - 1][0]), Y(tp[q][1]) - Y(tp[q - 1][1])));
        x.cum = cum.map(function (c_) { return c_ / (cum[cum.length - 1] || 1); });
        x.proj = []; x.ul = [];
        var nl = d.nlab != null ? d.nlab : 4;
        for (q = 0; q < u.length; q++) {
          if (q >= 1) x.proj.push(sv("path", { d: "M" + X(u[q]) + " " + Y(u[q]) + " V" + Y(y0), stroke: col, "stroke-width": 1.5, "stroke-dasharray": "4 5", fill: "none", opacity: 0 }, g));
          if (q <= nl) { var ul_ = txt(X(u[q]), Y(y0) + 44, esc("$" + (d.lettre || "u") + "_{" + q + "}$"), "tx ul"); ul_.style.color = col; ul_.style.opacity = 0; x.ul.push(ul_); }
        }
      } else if (d.type === "rect" || d.type === "balaye") {
        x.r = sv("rect", { x: X(x0), y: Y(0), width: 0, height: 0, fill: col, "fill-opacity": .22, stroke: col, "stroke-width": 2 }, g);
        x.pt = sv("circle", { r: 8, fill: col, stroke: "#0f1614", "stroke-width": 1.5 }, g);
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
        if (x.p && d.type === "toile") {
          var dt_ = d.dur || 1.1 * (d.u.length - 1), pr = P(t, t1, dt_);
          trace(x.p, pr);
          x.proj.forEach(function (pj, q) { pj.setAttribute("opacity", pr >= x.cum[2 * (q + 1)] - 1e-6 ? .7 : 0); });
          x.ul.forEach(function (lb, q) { lb.style.opacity = E((pr - (q ? x.cum[2 * q] : 0)) * 8); });
        } else if (x.p) trace(x.p, EIO(P(t, t1, dur)));
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
  // niveau d'un exercice ; v.etiquette remplace le libellé (« Exercice 2 · type bac »…)
  var NIVEAUX = { simple: ["Exercice 1 · pour démarrer", "#8FD6A8"], difficile: ["Exercice 2 · plus difficile", "#F4D35E"], bac: ["Exercice 3 · type bac", "#FF907E"] };
  TYPES.exo = function (o, v) {
    var e = o.el, coin = v.mode === "coin"; e.classList.add("v-exo", coin ? "coin" : "plein");
    if (!coin) { e.style.left = (v.x || 110) + "px"; e.style.top = (v.y || 96) + "px"; e.style.width = (v.w || 1060) + "px"; }
    var c = h("div", "ex-carte", e), nv = (NIVEAUX[v.niveau] || [v.niveau || "Exercice", C.sa]).slice();
    if (v.etiquette) nv[0] = v.etiquette;
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
    ardoise: { base: "linear-gradient(160deg,#18211f 0%,#212c29 55%,#161e1c 100%)", lueurs: ["rgba(244,211,94,.10)", "rgba(156,195,240,.10)", "rgba(143,214,168,.08)"] },
    carnet: { base: "linear-gradient(160deg,#141b22 0%,#1c2631 55%,#131a20 100%)", lueurs: ["rgba(156,195,240,.16)", "rgba(244,211,94,.08)", "rgba(255,144,126,.07)"] },
    craie: { base: "linear-gradient(160deg,#1d2725 0%,#283532 55%,#1b2422 100%)", lueurs: ["rgba(244,211,94,.14)", "rgba(236,235,228,.08)", "rgba(156,195,240,.10)"] }
  };
  FONDS.nuit = FONDS.ardoise;

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
    h("div", "carreaux", sc);       // quadrillage du carnet et marge rouge, sur toutes les scènes
    var cv = h("canvas", "poussiere", sc); cv.width = W; cv.height = H;
    var cx = cv.getContext("2d");
    var parts = []; for (var i = 0; i < 70; i++) parts.push({ x: alea(i) * W, y: alea(i + 100) * H, vx: (alea(i + 200) - .5) * 8, vy: 3 + alea(i + 300) * 8, r: .6 + alea(i + 400) * 1.4, ph: alea(i + 500) * 6.28 });   // poussière de craie
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
        var a = .14 + .14 * Math.sin(t * 1.3 + p.ph);
        cx.fillStyle = "rgba(236,235,228," + a.toFixed(3) + ")";
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
      ent.innerHTML = "Chapitre " + EP.num + (sc_.id !== EP.scenes[0].id ? " &nbsp;—&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
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
