/* ---------- Écriture des maths : syntaxe compacte (sous-ensemble de LaTeX) → MathML natif ---------- */
var TeX = (function () {
  "use strict";
  var GREC = { alpha: "α", beta: "β", gamma: "γ", delta: "δ", epsilon: "ϵ", varepsilon: "ε", theta: "θ", lambda: "λ", mu: "μ", pi: "π", sigma: "σ", phi: "φ", varphi: "φ", omega: "ω", Delta: "Δ", Omega: "Ω", Sigma: "Σ", ell: "ℓ" };
  var OPS = { leq: "⩽", le: "⩽", geq: "⩾", ge: "⩾", neq: "≠", ne: "≠", times: "×", cdot: "·", pm: "±", mp: "∓", to: "→", rightarrow: "→", Rightarrow: "⇒", Leftarrow: "⇐", iff: "⇔", Leftrightarrow: "⇔", "in": "∈", notin: "∉", subset: "⊂", cup: "∪", cap: "∩", forall: "∀", exists: "∃", approx: "≈", circ: "∘", ldots: "…", dots: "…", cdots: "⋯", mapsto: "↦", lt: "<", gt: ">", colon: ":", setminus: "∖", prime: "′", sim: "∼", "|": "‖", emptyset: "∅", ast: "∗", mid: "∣" };
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
      if ((a === "<mo>+</mo>" || a === "<mo>−</mo>") && (!out.length || /^<mo[^>]*>(?!\)|\]|\||′)/.test(out[out.length - 1]))) a = a.replace("<mo>", '<mo form="prefix" rspace="0.05em">');
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
    if (FONCS[n]) { this.blanc(); var par = this.peek() === "(" || /^\\left|^\^|^_/.test(this.s.slice(this.i)); return el("mrow", el("mi", n, 'mathvariant="normal"') + '<mo lspace="0" rspace="' + (par ? "0" : "0.17em") + '">&#x2061;</mo>'); }
    if (n === "lim") return el("mo", "lim", 'data-dessous movablelimits="false" lspace="0" rspace="0.17em"');
    if (n === "sum") return el("mo", "∑", 'data-dessous largeop="true" movablelimits="false"');
    if (n === "prod") return el("mo", "∏", 'data-dessous largeop="true" movablelimits="false"');
    if (n === "infty") return el("mi", "∞");
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
    if (r.length < 4) out = '<math' + (bloc ? ' display="block"' : "") + '>' + (r.length > 1 ? el("mrow", r.join("")) : r.join("")) + "</math>";
    else {
      /* coupures possibles avant chaque relation (et après un \quad) : la formule passe à la ligne sur téléphone */
      var REL = /^<mo>(=|⇔|⇒|⩽|⩾|&lt;|&gt;|≠|≈|∈|≡)<\/mo>$/, ESP = /^<mspace width="[12]em"><\/mspace>$/, morceaux = [[]];
      r.forEach(function (x, k) {
        if (REL.test(x) && k > 0 && morceaux[morceaux.length - 1].length) { morceaux.push([]); x = x.replace("<mo>", '<mo lspace="0.278em" rspace="0.278em">'); }
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
    return String(txt).replace(/\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g, function (_, b, i) { return b != null ? math(b, true) : math(i, false); });
  }
  /* version texte brut (recherche) */
  function plat(txt) {
    return String(txt || "").replace(/\[(def|prop|thm|ex|meth|piege|hist)(?:\|([^\]]*))?\]/g, " $2 : ").replace(/\[\/\]|\[\/?py\]/g, " ").replace(/\$\$?([^$]+)\$\$?/g, function (_, m) {
      return m.replace(/\\(frac|dfrac|sqrt|binom|text|mathbb|mathrm|abs|overline|vec|red|hl|blue|left|right|begin|end)\b/g, " ")
        .replace(/\\([a-zA-Z]+)/g, function (_, n) { return n === "infty" ? "∞" : GREC[n] || OPS[n] || ENS[n] || n; }).replace(/[{}^_\\]/g, " ");
    }).replace(/<[^>]+>/g, " ").replace(/&[a-z#0-9]+;/gi, " ").replace(/\s+/g, " ").trim();
  }
  return { math: math, fmt: fmt, plat: plat };
})();
