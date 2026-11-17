/* Vidéos de cours de HLP (site « Ex libris ») — moteur du lecteur. Identité « le livre ancien enluminé » (17/11/2026) :
   toute la vidéo se joue sur la page de droite d'un livre ouvert, posé sur une table de cuir. Papier vergé (vergeures,
   chaînettes, rousseurs, ombre de la reliure), texte composé en EB Garamond qui s'écrit à l'encre, titres en
   « Exlibris Titrage » (sous-ensemble renommé d'IM Fell), rubriques et filets rouges, lettrine rouge et or qui se peint
   au début de chaque citation, manicule (☞) qui pointe les mots qui frappent et les mises en garde, notes en marge,
   fleurons et culs-de-lampe gravés, cadres à double filet des pages de titre ; entre deux parties, la page se tourne
   (elle emporte ce qui y était écrit, la partie suivante s'écrit sur la page neuve).
   Copie du moteur de maths (maths/serie/moteur.js, 11/2026) dont seule la scène change : chaque type de visuel garde
   ses champs. Ajouts propres à la HLP :
   - document : un texte de sujet aux lignes numérotées, passages soulignés en rouge au repère {id.k} (v.hl) ;
   - cit : lettrine peinte (v.sansLettrine pour l'éviter), auteur en petites capitales, œuvre (v.o) en italique,
     v.ref (livre, chapitre), v.hl (mots soulignés en rouge quand la voix les dit) ;
   - dans tous les textes : *titre d'œuvre* en italique, **mot** en gras, ^{e} en exposant (XVIII^{e}).
   Les illustrations propres à une vidéo sont dans hlp/serie/illu-<code>.js (SERIE_ILLU), chargé après ce moteur.
   L'image est une fonction pure du temps t : lecture, retour en arrière, glisser sur la barre et export vidéo
   image par image (?export=1) donnent exactement le même rendu. Les données de l'épisode (window.EPISODE)
   sont générées par outils/serie-philo/generer.py depuis outils/serie-hlp/<module>.py. */
(function () {
  "use strict";
  var W = 1280, H = 720;
  var Q = new URLSearchParams(location.search);
  var EMBED = Q.has("embed"), EXPORT = Q.has("export");
  var NS = "http://www.w3.org/2000/svg";
  // encres sur papier vergé (les noms historiques des scripts sont gardés) : iv encre noire, iv2 encre pâlie,
  // sa rubrique rouge (titres, mots clés), ca rouille (mises en garde), te encre bleue-noire, vert, or
  var C = { iv: "#2b1c11", iv2: "#6a5440", sa: "#9c2a1b", sa2: "#7d1f13", ca: "#a4521c", te: "#2f4a6b", bleu: "#2f4a6b", nuit: "#efe2c4",
    el: "#2f4a6b", rouge: "#9c2a1b", vert: "#3d6b3a", or: "#b8892e", papier: "#efe2c4" };
  var ROM = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"];
  function romain(n) { return ROM[+n] || String(n); }

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
      if (!(i % 2)) return escT(p).replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>").replace(/\*([^*]+)\*/g, "<i>$1</i>").replace(/\^\{([^}]*)\}/g, "<sup>$1</sup>");
      var j = p.lastIndexOf("$") + 1, ponct = p.slice(j), f = p.slice(0, j), d = f.slice(0, 2) === "$$";
      var m = TeX.math(d ? f.slice(2, -2) : f.slice(1, -1), false).replace(/<\/math><wbr><math>/g, "");
      if (d) m = m.replace(/<math>/g, '<math displaystyle="true">');
      return '<span class="nw">' + m + escT(ponct) + "</span>";
    }).join("");
  }
  // les espaces d'une formule ne coupent pas les mots (mots écrits un à un)
  // un titre d'œuvre en *italique* est écrit d'un bloc (ses espaces ne coupent pas les mots)
  function proteger(s) { return String(s).replace(/\$\$?[^$]+\$\$?|\*[^*\s][^*]*\*/g, function (m) { return m.replace(/[ \t\n]/g, "\u0001"); }); }
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
      // livre : les filets sont droits (souligne2 = filet anglais : un trait gras, un trait maigre), les cadres à angles vifs
      if (g === "souligne" || g === "souligne2") {
        var y = hh + (opt.dy != null ? opt.dy : 2);
        d.push([[-4, y], [w + 4, y]]);
        if (g === "souligne2") { d.push([[-4, y + 6], [w + 4, y + 6]]); }
      } else if (g === "boite") { var bx0 = -m, by0 = -m * .7, bw = w + 2 * m, bh = hh + 1.4 * m; d.push([[bx0, by0], [bx0 + bw, by0], [bx0 + bw, by0 + bh], [bx0, by0 + bh], [bx0, by0 - 1.5]]); }
      else if (g === "ellipse") {
        // texte long : l'ellipse doit contenir les coins du texte, pas seulement ses bords (sinon les lettres débordent)
        var lg = w > hh * 3;
        d.push(ptsEllipse(w / 2, hh / 2, (lg ? w * .64 : w / 2) + m * 1.6, (lg ? hh * .74 : hh / 2) + m * 1.1, R, 1.08));
      }
      else if (g === "coche") { var k = hh * .5; d.push([[w + 10, hh * .55], [w + 10 + k * .35, hh * .55 + k * .45], [w + 10 + k * 1.05, hh * .55 - k * .75]]); }
      else if (g === "barre") d.push(wob(-4, hh * .55, w + 4, hh * .47, 1.5, R));
      else if (g === "croix") { var q = hh * .32, cx = w + 12 + q, cy = hh * .5; d.push([[cx - q, cy - q], [cx + q, cy + q]]); d.push([[cx + q, cy - q], [cx - q, cy + q]]); }
      else if (g === "droite") d.push([[w + (opt.dx || 22), -4], [w + (opt.dx || 22), hh + 4]]);
      else if (g === "gauche") d.push([[-(opt.dx || 22), -4], [-(opt.dx || 22), hh + 4]]);
      var pad = 40;
      s.setAttribute("viewBox", (-pad) + " " + (-pad) + " " + (w + 2 * pad) + " " + (hh + 2 * pad));
      s.style.left = -pad + "px"; s.style.top = -pad + "px"; s.style.width = (w + 2 * pad) + "px"; s.style.height = (hh + 2 * pad) + "px";
      var tot = 0;
      d.forEach(function (pts) {
        var p = sv("path", { d: dPts(pts), fill: "none", stroke: opt.c || "currentColor", "stroke-width": (opt.ep || 3.4) * (genre === "souligne2" && ps.length ? .45 : genre === "ellipse" || genre === "coche" || genre === "croix" || genre === "barre" ? 1 : .7), "stroke-linecap": genre === "ellipse" || genre === "barre" ? "round" : "butt", "stroke-linejoin": "miter" }, s);
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

  /* ---------- le livre (textures calculées une fois, à l'échelle 1,5 : l'export est en 1920 × 1080) ---------- */
  var PAGE = { x: 70, y: 20, w: 1150, h: 680 };   // la page de droite, en coordonnées de la scène
  var TEX = {};
  // la page : papier vergé (vergeures serrées, chaînettes espacées), nuages de la pâte, rousseurs, bords jaunis,
  // ombre du pli de la reliure à gauche, grain
  function papier() {
    var k = 1.5, WW = Math.round(PAGE.w * k), HH = Math.round(PAGE.h * k), c = cvs(WW, HH), g = c.getContext("2d"), R = rng(11), i, x, y;
    g.fillStyle = "#efe2c4"; g.fillRect(0, 0, WW, HH);
    for (i = 0; i < 90; i++) {
      x = R() * WW; y = R() * HH; var r = 60 + R() * 300, gr = g.createRadialGradient(x, y, 0, x, y, r);
      gr.addColorStop(0, R() < .5 ? "rgba(255,248,228," + (.03 + R() * .04) + ")" : "rgba(196,160,104," + (.015 + R() * .025) + ")");
      gr.addColorStop(1, "rgba(0,0,0,0)"); g.fillStyle = gr; g.fillRect(x - r, y - r, 2 * r, 2 * r);
    }
    for (y = 0; y < HH; y += 6) { g.fillStyle = "rgba(110,80,40," + (.022 + R() * .018).toFixed(3) + ")"; g.fillRect(0, y, WW, 1.2); }
    for (x = 50 + R() * 30; x < WW; x += 138) { g.fillStyle = "rgba(110,80,40,.05)"; g.fillRect(x, 0, 2.6, HH); }
    for (i = 0; i < 26; i++) {
      var fx = R() * WW, fy = R() * HH, fr = 4 + R() * R() * 46, g2 = g.createRadialGradient(fx, fy, 0, fx, fy, fr);
      g2.addColorStop(0, "rgba(150,95,35," + (.07 + R() * .1) + ")"); g2.addColorStop(1, "rgba(150,95,35,0)"); g.fillStyle = g2; g.fillRect(fx - fr, fy - fr, 2 * fr, 2 * fr);
    }
    var v = g.createRadialGradient(WW * .55, HH * .5, Math.min(WW, HH) * .45, WW * .55, HH * .5, Math.max(WW, HH) * .72);
    v.addColorStop(0, "rgba(120,78,30,0)"); v.addColorStop(1, "rgba(120,78,30,.24)"); g.fillStyle = v; g.fillRect(0, 0, WW, HH);
    var gu = g.createLinearGradient(0, 0, 170, 0);
    gu.addColorStop(0, "rgba(70,40,12,.4)"); gu.addColorStop(.3, "rgba(70,40,12,.12)"); gu.addColorStop(1, "rgba(70,40,12,0)"); g.fillStyle = gu; g.fillRect(0, 0, 170, HH);
    var im = g.getImageData(0, 0, WW, HH), d = im.data;
    for (i = 0; i < d.length; i += 4) { var n = (R() - .5) * 10; d[i] += n; d[i + 1] += n * .95; d[i + 2] += n * .85; }
    g.putImageData(im, 0, 0);
    return c;
  }
  // la scène entière : la table de cuir, le bord de la page de gauche, la tranche du livre, la page de droite
  function planche() {
    var k = 1.5, WW = 1920, HH = 1080, c = cvs(WW, HH), g = c.getContext("2d"), R = rng(17), i;
    var bg = g.createRadialGradient(WW / 2, HH / 2, 80, WW / 2, HH / 2, WW * .62);
    bg.addColorStop(0, "#4a2814"); bg.addColorStop(.7, "#2c170b"); bg.addColorStop(1, "#1f1109"); g.fillStyle = bg; g.fillRect(0, 0, WW, HH);
    for (i = 0; i < 2600; i++) { g.fillStyle = "rgba(" + (R() < .5 ? "0,0,0" : "120,70,30") + "," + (.05 + R() * .08).toFixed(3) + ")"; g.fillRect(R() * WW, R() * HH, 1 + R() * 3, 1 + R() * 2); }
    g.save(); g.scale(k, k);
    g.save(); g.filter = "blur(14px)"; g.fillStyle = "rgba(0,0,0,.55)"; g.fillRect(8, 32, 1236, 684); g.restore();
    var pg = g.createLinearGradient(0, 0, 72, 0);
    pg.addColorStop(0, "#e6d6b2"); pg.addColorStop(.6, "#dcc8a0"); pg.addColorStop(.92, "#b49a6c"); pg.addColorStop(1, "#8a7048");
    g.fillStyle = pg; g.fillRect(0, 20, 72, 680);
    g.fillStyle = "#cdb88e"; g.fillRect(PAGE.x + 4, PAGE.y + 4, PAGE.w + 12, PAGE.h + 6);
    for (var x = PAGE.x + PAGE.w; x < PAGE.x + PAGE.w + 16; x += 2) { g.fillStyle = (x / 2) % 2 ? "#b8a274" : "#dccba4"; g.fillRect(x, PAGE.y + 3 + (x - PAGE.x - PAGE.w) * .25, 1, PAGE.h + 3); }
    for (var y = PAGE.y + PAGE.h; y < PAGE.y + PAGE.h + 7; y += 2) { g.fillStyle = (y / 2) % 2 ? "#b8a274" : "#dccba4"; g.fillRect(PAGE.x + 4, y, PAGE.w + 10, 1); }
    g.restore();
    g.drawImage(TEX.papier, PAGE.x * k, PAGE.y * k);
    return c;
  }
  function regle(len) {
    var k = 1.5, c = cvs(Math.round((len + 40) * k), Math.round(150 * k)), g = c.getContext("2d"), R = rng(5), i;
    g.scale(k, k); g.translate(10, 110);
    g.save(); g.filter = "blur(10px)"; g.fillStyle = "rgba(0,0,0,.5)"; g.fillRect(14, -66, len, 78); g.restore();
    g.fillStyle = "#C9A066"; g.fillRect(0, -78, len, 78);
    for (i = 0; i < 26; i++) { g.strokeStyle = "rgba(110,70,30," + (.08 + R() * .14) + ")"; g.lineWidth = 1 + R() * 2; var yy = -74 + R() * 70; g.beginPath(); g.moveTo(0, yy); g.bezierCurveTo(len * .3, yy + (R() - .5) * 8, len * .7, yy + (R() - .5) * 8, len, yy + (R() - .5) * 6); g.stroke(); }
    g.fillStyle = "rgba(255,240,210,.22)"; g.fillRect(0, -78, len, 6); g.fillStyle = "rgba(70,40,10,.35)"; g.fillRect(0, -5, len, 5);
    g.strokeStyle = "rgba(40,24,8,.85)"; g.fillStyle = "rgba(40,24,8,.85)"; g.font = "600 18px 'EB Garamond', serif";
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
    loupe: ["M44 16 a26 26 0 1 0 0.1 0", "M63 63 L88 88"],
    livre: ["M14 30 C30 22 42 22 50 30 C58 22 70 22 86 30 V80 C70 72 58 72 50 80 C42 72 30 72 14 80 Z", "M50 30 V80"],
    plume: ["M84 12 C58 18 40 40 32 74", "M84 12 C70 34 56 52 34 70", "M32 74 L24 90", "M46 50 L60 46"],
    balance: ["M50 14 V84", "M36 84 H64", "M18 30 H82", "M18 30 L8 56 H28 Z", "M82 30 L72 56 H92 Z"],
    arbre: ["M50 90 V50", "M50 62 C40 56 34 50 32 40", "M50 54 C60 50 66 42 68 32", "M50 50 C30 50 22 32 34 20 C40 8 62 8 68 20 C80 32 70 50 50 50"],
    oeil: ["M10 50 C28 24 72 24 90 50 C72 76 28 76 10 50 Z", "M50 38 a12 12 0 1 0 0.1 0"],
    ecole: ["M14 44 L50 20 L86 44", "M22 40 V82 H78 V40", "M42 82 V60 H58 V82", "M50 20 V8 H64 V14 H50"],
    chaine: ["M14 54 C14 40 34 40 40 46 L44 50", "M56 50 L60 54 C66 60 86 60 86 46 C86 32 66 32 60 38", "M46 30 L42 20 M54 30 L58 20 M50 32 V18"],
    cle: ["M30 50 a16 16 0 1 0 0.1 0", "M46 50 H88", "M76 50 V62", "M86 50 V58"],
    voix: ["M20 40 H34 L54 22 V78 L34 60 H20 Z", "M66 36 C74 44 74 56 66 64", "M76 26 C90 40 90 60 76 74"],
    sablier: ["M30 12 H70", "M30 88 H70", "M34 12 C34 40 64 42 64 50 C64 58 34 60 34 88", "M66 12 C66 40 36 42 36 50 C36 58 66 60 66 88"]
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

  /* ---------- ornements du livre ---------- */
  // fleuron gravé (celui du site), tracé à l'encre rouge ; renvoie function (u), u ∈ [0, 1]
  function fleuron(parent, cls, w) {
    var s = sv("svg", { viewBox: "0 0 86 22", class: "fleuron " + (cls || "") }, parent);
    s.style.width = (w || 150) + "px"; s.style.height = ((w || 150) * 22 / 86).toFixed(1) + "px";
    var g = sv("g", { fill: "none", stroke: "currentColor", "stroke-width": 1.1, "stroke-linecap": "round", "stroke-linejoin": "round" }, s);
    var ps = ["M43 3.5c3.2 3 3.2 12 0 15c-3.2-3-3.2-12 0-15z", "M37.5 11c-6-7.5-14.5-7.5-18.5-2c-2.8 4 1.2 8 5 6c3-1.8 1.2-5-1-4.2",
      "M48.5 11c6-7.5 14.5-7.5 18.5-2c2.8 4-1.2 8-5 6c-3-1.8-1.2-5 1-4.2", "M37.5 11c-4 4-9 6-14.5 5", "M48.5 11c4 4 9 6 14.5 5",
      "M19 9.5H5", "M67 9.5h14"].map(function (d) { return sv("path", { d: d, pathLength: 1, "stroke-dasharray": "1 1.02" }, g); });
    var c1 = sv("circle", { cx: 3, cy: 9.5, r: 1.5, fill: "currentColor" }, s), c2 = sv("circle", { cx: 83, cy: 9.5, r: 1.5, fill: "currentColor" }, s);
    return function (u) {
      ps.forEach(function (p, i) { var f = EIO(P(u, i === 0 ? 0 : .12 + (i % 3) * .06, .65)); p.style.strokeDashoffset = (1 - f).toFixed(3); p.style.visibility = f <= 0 ? "hidden" : ""; });
      ps[0].style.fill = "currentColor"; ps[0].style.fillOpacity = P(u, .55, .4).toFixed(3);
      op(c1, P(u, .8, .2)); op(c2, P(u, .8, .2));
    };
  }
  // cadre de page de titre : double filet (rouge, puis encre), tracé ; coordonnées de la scène
  function cadreTitre(e, x, y, w, hh) {
    var s = sv("svg", { class: "cadre-t", viewBox: "0 0 1280 720" }, e);
    var r1 = sv("rect", { x: x, y: y, width: w, height: hh, fill: "none", stroke: C.sa, "stroke-width": 3, pathLength: 1, "stroke-dasharray": "1 1.02" }, s);
    var r2 = sv("rect", { x: x + 14, y: y + 14, width: w - 28, height: hh - 28, fill: "none", stroke: C.iv, "stroke-width": 1.3, pathLength: 1, "stroke-dasharray": "1 1.02" }, s);
    return function (u) {
      var a = EIO(P(u, 0, .8)), b = EIO(P(u, .15, .85));
      r1.style.strokeDashoffset = (1 - a).toFixed(4); r1.style.visibility = a <= 0 ? "hidden" : "";
      r2.style.strokeDashoffset = (1 - b).toFixed(4); r2.style.visibility = b <= 0 ? "hidden" : "";
    };
  }
  // manicule (☞) : la main de lecteur qui pointe ; elle glisse de la marge et hoche une fois
  function manicule(parent, cls) { return h("span", "mani hors " + (cls || ""), parent, "☞"); }
  function pointer(m, t, t0) {
    var a = E(P(t, t0, .45)), nud = Math.sin(Math.PI * P(t, t0 + .45, .4)) * 8;
    op(m, a); tr(m, "translateX(" + (-40 * (1 - a) + nud).toFixed(1) + "px)");
  }

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
    var cad = cadreTitre(e, 202, 78, 876, 564);
    var sur = h("div", "sur", e), sus = h("span", "", sur, esc(v.sur || ""));
    var fl = fleuron(e, "fl-t", 150);
    var tt = h("div", "tt", e), tts = h("span", "tts", tt), L = String(v.t).length;
    tt.style.fontSize = (L <= 22 ? 92 : L <= 34 ? 80 : 68) + "px";
    var ls = lettres(tts, v.t); if (ls[0]) ls[0].classList.add("rub");
    var ss = h("div", "ss", e, esc(v.sous || ""));
    var cul = fleuron(e, "fl-b", 104);
    var e1 = Ecrit(sus, { v: 34 }), e2 = Ecrit(tts, { v: 22, max: 1.6 }), e3 = Ecrit(ss, { v: 34 });
    return function (t, st) {
      var tl = st.tl;
      cad(P(tl, 0, 1.3)); e1.pose(tl, .25); fl(P(tl, .45, .8)); e2.pose(tl, .6); e3.pose(tl, .9 + e2.d); cul(P(tl, 1.1 + e2.d, .7));
    };
  };

  // carton de partie : la page neuve, que la page tournée vient de découvrir ; cadre à double filet, fleuron, titre
  TYPES.chapitre = function (o, v) {
    o.entree = "aucune"; o.disp = "flex";
    var e = o.el; e.classList.add("v-chapitre");
    var cad = cadreTitre(e, 232, 138, 816, 424);
    var num = h("div", "num", e), ns = h("span", "", num, "Partie " + esc(v.num));
    var fl = fleuron(e, "fl-t", 130);
    var tt = h("div", "tt", e), tts = h("span", "tts", tt), L = String(v.t).length;
    tt.style.fontSize = (L <= 24 ? 78 : L <= 40 ? 64 : 54) + "px";
    var ls = lettres(tts, v.t); if (ls[0]) ls[0].classList.add("rub");
    var cul = fleuron(e, "fl-b", 88);
    var e1 = Ecrit(ns, { v: 30 }), e2 = Ecrit(tts, { v: 40, max: 1.15 });
    return function (t, st) {
      var tl = st.tl, t0 = .78;
      cad(P(tl, t0 - .1, 1)); e1.pose(tl, t0); fl(P(tl, t0 + .2, .6)); e2.pose(tl, t0 + .35); cul(P(tl, t0 + .5 + e2.d, .6));
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
    var mani = note ? manicule(c, "m-note") : null;
    var tx = h("div", "tx", c), sp = mots(tx, v.t, "mot-l cle"), ec = Ecrit(tx);
    var mg = Trait(c, "gauche", { c: note ? C.ca : C.sa, ep: 3, dx: 26 });
    var etp = null, eet = null, tir = null;
    if (v.etape) { etp = h("div", "et", c); var es = h("span", "", etp, esc(v.etape)); eet = Ecrit(es); tir = Trait(es, "souligne", { c: C.te, ep: 2.4, dy: 3 }); }
    var bad = v.plus ? h("div", "badge", c, "Pour aller plus loin") : null, ebad = bad ? Ecrit(bad) : null;
    var kl = cles(v, sp);
    return function (t, st) {
      var tl = st.tl;
      mg(P(tl, 0, .45)); te.maj(tl, .15); if (mani) pointer(mani, tl, .05);
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
    var ic = { repere: "❦", copie: "☞", lien: "→", plus: "+" }[v.style || "repere"] || "❦";
    var p = h("div", "pill", e); h("span", "ic", p, ic); h("span", "", p, esc(v.t));
    var ec = Ecrit(p), bx = Trait(p, "boite", { m: 4, ep: 2.6 });
    return function (t, st) { ec.pose(st.tl, .05); bx(P(st.tl, ec.d * .6, .5)); };
  };

  // citation : grand guillemet rouge dans la marge, lettrine rouge et or qui se peint (or, lettre, reflet), mots qui
  // s'allument en rouge quand la voix les dit ; v.a auteur, v.o œuvre (italique), v.ref lieu dans l'œuvre, v.hl mots
  // soulignés en rouge (texte exact d'un passage de la citation), v.para : citation approchée
  var LETTRE = /^([A-ZÀ-ÖØ-ÞŒ])/;   // une citation qui commence par une minuscule n'a pas de lettrine
  TYPES.cit = function (o, v) {
    var e = o.el; e.classList.add("v-cit"); o.entree = "aucune";
    e.style.left = (v.x || 190) + "px"; e.style.top = (v.y || 160) + "px"; e.style.width = (v.w || 900) + "px";
    var gu = h("div", "gu", e, "«");
    var tx = h("div", "tx", e), txt = String(v.t || ""), L = txt.length;
    var fs = (L <= 80 ? 52 : L <= 130 ? 46 : L <= 190 ? 40 : L <= 260 ? 36 : 32) * ((v.w || 900) < 760 ? .9 : 1);
    tx.style.fontSize = fs + "px";
    var lt = null, lor = null, llet = null, lref = null, seule = false;
    if (!v.sansLettrine && LETTRE.test(txt)) {
      lt = h("div", "lettrine hors", tx);
      var cote = Math.round(fs * 1.32 * 2 - 6);
      lt.style.width = lt.style.height = cote + "px";
      lor = h("div", "l-or", lt, '<svg viewBox="0 0 166 166"><g fill="none" stroke="rgba(255,248,225,.55)" stroke-width="2.4" stroke-linecap="round">' +
        '<path d="M18 148 C30 120 20 96 40 80 C56 68 50 46 30 40"/><path d="M148 18 C136 46 146 70 126 86 C110 98 116 120 136 126"/>' +
        '<circle cx="30" cy="40" r="5"/><circle cx="136" cy="126" r="5"/><path d="M40 80 c-10 -2 -16 6 -12 12"/><path d="M126 86 c10 2 16 -6 12 -12"/></g></svg>');
      llet = h("div", "l-lettre", lt, esc(txt[0]));
      llet.style.fontSize = Math.round(cote * .74) + "px";
      lref = h("i", "", h("div", "l-reflet", lt));
      txt = txt.slice(1);
      if (/^\s/.test(txt)) { seule = true; txt = txt.replace(/^\s+/, ""); }
    }
    var sp = mots(tx, txt, "mc");
    if (seule) sp.unshift(h("span", "mc", null, ""));   // la lettrine est un mot entier (« À ») : les indices des mots restent ceux de la voix
    var au = h("div", "au", e, "— <span class=\"sc\">" + esc(v.a || "") + "</span>" + (v.o ? ", <i>" + esc(v.o) + "</i>" : "") + (v.ref ? ", " + esc(v.ref) : "") +
      (v.para ? '<span class="ap">≈ citation approchée</span>' : ""));
    var m = v.m || [], n = sp.length, eau = Ecrit(au);
    var tm = sp.map(function (_, i) {
      if (!m.length) return v.t0 + .5 + i * .3;
      var j = m.length === n ? i : Math.min(m.length - 1, Math.round(i * (m.length - 1) / Math.max(1, n - 1)));
      return m[j][0];
    });
    var us = sp.map(function (s) { var u = unites(s); u.forEach(function (x) { x.a = 0; }); return u; });
    // mots soulignés (v.hl) : repérés dans la suite des mots de la citation
    var soul = [];
    if (v.hl) {
      var cible = String(v.hl).split(/\s+/).map(nrm), mm = sp.map(function (s) { return nrm(s.textContent); });
      for (var i = 0; i + cible.length <= mm.length; i++) {
        var okk = true;
        for (var j = 0; j < cible.length; j++) if (mm[i + j] !== cible[j]) { okk = false; break; }
        if (okk) { for (j = 0; j < cible.length; j++) soul.push({ i: i + j, tr: Trait(sp[i + j], "souligne", { c: C.sa, ep: 3.2, dy: 1 }) }); break; }
      }
    }
    return function (t, st) {
      if (lt) {
        var t0 = v.t0 + .05, po = EIO(P(t, t0, .55));
        lor.style.clipPath = "circle(" + (po * 75).toFixed(2) + "% at 50% 50%)"; lor.style.visibility = po > 0 ? "visible" : "hidden";
        var pl = P(t, t0 + .3, .5);
        llet.style.clipPath = pl < 1 ? "inset(0 0 " + (100 * (1 - pl)).toFixed(1) + "% 0)" : "";
        llet.style.visibility = pl > 0 ? "" : "hidden";
        var r = P(t, t0 + .75, .6);
        tr(lref, "translateX(" + (-80 + r * 300).toFixed(1) + "px) skewX(-18deg)"); op(lref, r > 0 && r < 1 ? 1 : 0);
      }
      op(gu, E(P(t, v.t0, .4)));
      sp.forEach(function (s, i) {
        poser(us[i], P(t, tm[i] - .1, .25) * 30);
        s.style.color = t >= tm[i] && t < tm[i] + .9 ? C.sa : "";
      });
      soul.forEach(function (x) { x.tr(P(t, tm[x.i] + .2, .35)); });
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
    h("div", "pf-cadre", pf);
    var bd = h("div", "bandeau", e);
    var nm = h("div", "bd-nom", bd), nms = h("span", "", nm, esc(v.nom));
    var inf = h("div", "bd-info", bd, esc([v.dates, v.legende].filter(Boolean).join(" · ")));
    var e1 = Ecrit(nms, { v: 22 }), e2 = Ecrit(inf, { v: 40 }), sl = Trait(nms, "souligne2", { c: C.sa, ep: 3.4, dy: 2 });
    var mf = v.annee != null ? minifrise(bd, v.annee) : null;
    return function (t, st) {
      // le tirage arrive (léger retard : un tirage précédent a le temps de partir), puis repart en glissant
      var a = E(P(st.tl, .22, .6)), q = E(P(t, v.t1, .4));
      op(pf, a * (1 - q)); tr(pf, "translate(" + (-14 * (1 - a) + 40 * q).toFixed(1) + "px,0) scale(" + (1.03 - .03 * a).toFixed(3) + ")");
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
    var vs = h("div", "vs", e), vss = h("span", "", vs, esc(v.vs || "≠")), evs = Ecrit(vss), cvs_ = function () {};   // livre : le mot de liaison en italique, sans cercle
    var rp = v.repere ? h("div", "rp", e) : null, rps = rp ? h("span", "", rp, "❦ " + esc(v.repere)) : null, erp = rp ? Ecrit(rps) : null, brp = rp ? Trait(rps, "boite", { c: C.te, m: 6, ep: 2.6 }) : null;
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
      return { c: c, ic: ic, bx: Trait(c, "boite", { m: 0, ep: 2.8, c: "rgba(43,28,17,.75)" }), en: Trait(ns, "ellipse", { c: C.sa, m: 4, ep: 2.6 }),
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
      var dessin = genre === "ok" ? '<svg viewBox="0 0 40 40"><path d="M7 21 L16 30 L34 8"/></svg>' : genre === "ko" ? '<svg viewBox="0 0 40 40"><path d="M9 9 L31 31 M31 9 L9 31"/></svg>' : null;
      var b = h("div", "mq " + genre, li), bs = h("span", "", b, dessin || esc(genre === "at" ? "☞" : genre === "num" ? mq + "." : mq));
      var tx = h("div", "tx", li), sp = mots(tx, txt, "mot-l cle");
      return { li: li, b: b, sp: sp, eb: Ecrit(bs, { d: .25 }), et_: Ecrit(tx), pa: dessin ? bs.querySelector("path") : null, cer: null };
    });
    var kl = cles(v, [].concat.apply([], lis.map(function (l) { return l.sp; })));
    return function (t, st) {
      if (ti) ti.maj(st.tl, 0);
      allume(kl, t);
      var tk = lis.map(function (_, i) { return et(v, String(i + 1), (ti ? ti.d : 0) + .3 + i * .5); });
      var dernier = -1; tk.forEach(function (x, i) { if (t >= x) dernier = i; });
      lis.forEach(function (l, i) {
        l.eb.pose(t, tk[i]); if (l.pa) trace(l.pa, P(t, tk[i], .35));
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
    var axe = sv("path", { d: "M150 372 H1150", fill: "none", stroke: C.sa, "stroke-width": 2.4, "stroke-linecap": "round" }, sa);
    var pointeA = sv("path", { d: "M1136 361 L1154 372 L1136 383", fill: "none", stroke: C.sa, "stroke-width": 3.4, "stroke-linecap": "round", "stroke-linejoin": "round" }, sa);
    var rupt = h("div", "rupt", e, "≈"); rupt.style.left = "470px";
    var ans = [[-400, "−400"], [0, "0"], [1600, "1600"], [1700, "1700"], [1800, "1800"], [1900, "1900"]].map(function (a) {
      var d = h("div", "an", e, a[1]); d.style.left = X(a[0]) + "px"; return d;
    });
    var RANGS = [{ top: 210, tige: [84, 78] }, { top: 420, tige: [-48, 48] }, { top: 66, tige: [84, 222] }, { top: 560, tige: [-188, 188] }];
    var tri = v.items.slice().sort(function (a, b) { return a.d - b.d; });
    var fin = RANGS.map(function () { return -1e9; }), serre = false;
    tri.forEach(function (it) { var x = X(it.d), r = 0; while (r < RANGS.length - 1 && x - fin[r] < 128) r++; fin[r] = x; if (r > 1) serre = true; });
    var pas = 0;
    if (serre) { rupt.style.display = "none"; ans.forEach(function (a) { a.style.display = "none"; }); pas = tri.length > 1 ? 900 / (tri.length - 1) : 0; }
    fin = RANGS.map(function () { return -1e9; });
    var its = tri.map(function (it, i) {
      var p = h("div", "p", e), x = serre ? 200 + i * pas : X(it.d), r = serre ? i % 2 : 0;
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
    if (!v.fond) h("div", "tb-marque", cadre);   // planche hors-texte : cuvette de la gravure autour de l'image
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
      if (!v.fond) tr(cadre, "translate(-50%,-50%) scale(" + (1.02 - .02 * E(P(t, v.t0, .8))).toFixed(3) + ")");
      if (lg) op(lg, E(P(st.tl, 1.2, .8)) * .9);
    };
  };

  // générique : le titre de la série s'écrit sur l'ardoise
  TYPES.generique = function (o, v) {
    var e = o.el; e.classList.add("v-generique"); o.entree = "aucune"; o.disp = "flex";
    var cad = cadreTitre(e, 202, 78, 876, 564);
    var haut = h("div", "g-haut", e), hs = h("span", "", haut, "Ex libris · HLP Terminale");
    var fl = fleuron(e, "fl-t", 170);
    var tt = h("div", "g-titre", e), tts = h("span", "", tt), ls = lettres(tts, v.serie), L = String(v.serie).length;
    if (ls[0]) ls[0].classList.add("rub");
    tt.style.fontSize = (L <= 22 ? 96 : L <= 40 ? 78 : 64) + "px";
    var bas = h("div", "g-bas", e), bs = h("span", "", bas, "Le cours en vidéo · entrée " + romain(v.num));
    var cul = fleuron(e, "fl-b", 110);
    var e1 = Ecrit(hs, { v: 30 }), e2 = Ecrit(tts, { v: 18, max: 1.8 }), e3 = Ecrit(bs, { v: 34 });
    return function (t, st) {
      var tl = st.tl;
      cad(P(tl, .05, 1.3)); e1.pose(tl, .3); fl(P(tl, .5, .8));
      e2.pose(tl, 1.0); e3.pose(tl, 1.4 + e2.d); cul(P(tl, 1.6 + e2.d, .7));
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
    var mani = manicule(m, "m-frappe");
    m.style.fontSize = Math.min(170, Math.floor(1250 / (String(v.t).length * 0.62))) + "px";
    var ec = Ecrit(ms, { d: .45 }), sl = Trait(ms, "souligne2", { c: C.sa, ep: 6, dy: 6 });
    return function (t, st) {
      var tl = st.tl, out = P(tl, 1.15, .4);
      op(fond, E(P(tl, 0, .18)) * (1 - E(out)));
      op(m, 1 - E(out));
      ec.pose(tl, .05); sl(P(tl, .5, .25)); pointer(mani, tl, .35);
    };
  };

  // « À retenir » de fin de partie : un cadre jaune tracé à la craie, sur un coin de tableau propre
  TYPES.flash = function (o, v) {
    var e = o.el; e.classList.add("v-flash"); o.entree = "aucune"; o.disp = "flex";
    var fond = h("div", "fl-fond", e), c = h("div", "fl-carte", e);
    var lab = h("div", "fl-lab", c, "❧ À retenir ❧"), elab = Ecrit(lab, { v: 30 });
    var tx = h("div", "fl-tx", c); mots(tx, v.t);
    var ec = Ecrit(tx, { v: 60, max: 1.6 }), bx = Trait(c, "boite", { c: C.sa, m: 0, ep: 4 }), bx2 = Trait(c, "boite", { c: C.sa, m: -10, ep: 1.8 });
    return function (t, st) {
      var tl = st.tl, out = o.efface ? 0 : EIO(P(t, v.t1 - .3, .6));
      op(fond, E(P(tl, 0, .4)) * (1 - out)); op(c, 1 - out);
      bx(P(tl, .15, .6)); bx2(P(tl, .25, .6)); elab.pose(tl, .3); ec.pose(tl, .4 + elab.d);
    };
  };

  // carte mentale : centre entouré, branches tracées, nœuds encadrés
  TYPES.carte = function (o, v) {
    var e = o.el; e.classList.add("v-carte"); o.entree = "aucune";
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H }, e);
    var POS = [[420, 130], [860, 130], [420, 470], [860, 470]];
    var centre = h("div", "cm-centre", e), cs = h("span", "", centre, esc(v.centre)), ece = Ecrit(cs), ent = Trait(cs, "ellipse", { c: C.sa, m: 12, ep: 3.6 });
    var br = (v.branches || []).map(function (b, i) {
      // livre : la branche part du bord de l'ellipse et rejoint le côté intérieur du nœud (elle ne barre ni le centre ni les listes)
      var p = POS[i], gch = p[0] < 640, haut = p[1] < 330, sx = gch ? 470 : 810, sy = haut ? 294 : 366, ex = gch ? 520 : 760, ey = p[1] + (haut ? 20 : -20),
        my = (sy + ey) / 2, d = "M" + sx + " " + sy + " C" + sx + " " + my + " " + ex + " " + my + " " + ex + " " + ey;
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
    // illustrations propres à une vidéo (maths/serie/illu-<code>.js, chargé après le moteur) :
    // SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; }, outils dans window.SERIE_OUTILS
    var fi = ILLU[v.nom] || (window.SERIE_ILLU || {})[v.nom];
    var f = fi ? fi(s, v) : function () {};
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
  var K_CRAIE = 1;   // la craie (Caveat) est plus étroite que l'ancienne police : même encombrement, lettres plus grandes
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
    var bx = Trait(c, "boite", { m: 0, ep: 2.8, c: "rgba(43,28,17,.55)" });
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
      grille.push(sv("path", { d: dPts(wob(X(x), m[2] + ph, X(x), m[2], 1, R)), stroke: "rgba(43,28,17,.12)", "stroke-width": 1.6, fill: "none" }, fond));
      ticks.push(txt(X(x), Y(y0) + 10, esc(String(x).replace(".", ",")), "tx"));
    });
    (ax.gy || []).forEach(function (y) {
      grille.push(sv("path", { d: dPts(wob(m[0], Y(y), m[0] + pw, Y(y), 1, R)), stroke: "rgba(43,28,17,.12)", "stroke-width": 1.6, fill: "none" }, fond));
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
  var NIVEAUX = { simple: ["Exercice · pour démarrer", C.vert], difficile: ["Exercice · plus difficile", C.sa], bac: ["Sujet type bac", C.sa] };
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
      return { d: d, en: Ecrit(ns, { d: .2 }), cer: function () {}, et_: Ecrit(tq, { v: coin ? 60 : 34 }) };
    });
    var sep = coin ? Trait(c, "droite", { c: "rgba(43,28,17,.45)", ep: 2.6, dx: 18 }) : null;
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

  // document : un texte de sujet comme au bac, lignes numérotées de cinq en cinq dans la marge ; v.lignes (une chaîne par
  // ligne, coupées comme sur le sujet), v.chapeau (présentation en italique, au-dessus), v.ref (référence, en dessous),
  // v.taille (corps, 25 par défaut). Passages au repère {id.k} : v.hl = [[l1, l2], …] (lignes l1 à l2, à partir de 1),
  // soulignés en rouge, trait de marge ; le dernier passage appelé reste net, le reste du texte pâlit.
  TYPES.document = function (o, v) {
    var e = o.el; e.classList.add("v-document"); o.entree = "aucune";
    e.style.left = (v.x || 110) + "px"; e.style.top = (v.y || 84) + "px"; e.style.width = (v.w || 1060) + "px";
    e.style.fontSize = (v.taille || 25) + "px";
    var ch = v.chapeau ? h("div", "dc-ch", e, esc(v.chapeau)) : null, ech = ch ? Ecrit(ch, { v: 60 }) : null;
    var lignes = v.lignes.map(function (l, i) {
      var d = h("div", "dc-l", e), n = h("span", "dc-n hors", d, (i + 1) % 5 === 0 || i === 0 ? String(i + 1) : ""), tx = h("span", "dc-t", d, esc(l));
      return { d: d, n: n, tx: tx, ec: Ecrit(tx, { v: 140, max: .7 }) };
    });
    var ref = v.ref ? h("div", "dc-ref", e, esc(v.ref)) : null, eref = ref ? Ecrit(ref, { v: 60 }) : null;
    var hls = (v.hl || []).map(function (r) {
      var trs = [];
      for (var i = r[0] - 1; i <= r[1] - 1; i++) if (lignes[i]) trs.push(Trait(lignes[i].tx, "souligne", { c: C.sa, ep: 2.6, dy: 0 }));
      return { a: r[0] - 1, b: r[1] - 1, trs: trs };
    });
    return function (t, st) {
      var tl = st.tl, t0 = .1;
      if (ch) { ech.pose(tl, t0); t0 += ech.d + .1; }
      lignes.forEach(function (l, i) { l.ec.pose(tl, t0 + i * .14); op(l.n, E(P(tl, t0 + i * .14, .3))); });
      if (ref) eref.pose(tl, t0 + lignes.length * .14 + .2);
      var actif = -1;
      hls.forEach(function (x, k) { var tk = v.et && v.et[String(k + 1)]; if (tk != null && t >= tk) actif = k; });
      hls.forEach(function (x, k) {
        var tk = v.et && v.et[String(k + 1)];
        x.trs.forEach(function (f, j) { f(tk == null ? 0 : P(t, tk + j * .12, .4)); });
      });
      lignes.forEach(function (l, i) {
        var dans = actif >= 0 && i >= hls[actif].a && i <= hls[actif].b;
        l.d.classList.toggle("on", dans);
        op(l.d, actif < 0 || dans ? 1 : .42);
      });
    };
  };

  // « À toi » : la vidéo s'arrête d'elle-même (si l'option est active) pour que l'élève cherche avant la correction
  TYPES.pause = function (o, v) {
    var e = o.el; e.classList.add("v-pause"); o.entree = "aucune";
    e.style.left = (v.x != null ? v.x : 200) + "px"; e.style.top = (v.y != null ? v.y : 130) + "px"; e.style.width = (v.w || 880) + "px";
    var c = h("div", "pa-carte", e);
    var ic = sv("svg", { class: "pa-ic", viewBox: "0 0 100 100" }, c), R = rng(41);
    var b1 = sv("path", { d: "M28 10 H72 M28 90 H72", fill: "none", stroke: C.iv, "stroke-width": 4, "stroke-linecap": "round" }, ic);
    var b2 = sv("path", { d: "M33 10 C33 38 62 42 62 50 C62 58 33 62 33 90 M67 10 C67 38 38 42 38 50 C38 58 67 62 67 90", fill: "none", stroke: C.iv, "stroke-width": 3, "stroke-linecap": "round" }, ic);
    var ce = sv("path", { d: "M40 30 Q50 40 60 30 Z M50 52 V66 M38 88 Q50 72 62 88 Z", fill: C.sa, stroke: C.sa, "stroke-width": 2, "stroke-linejoin": "round" }, ic);
    var te = h("div", "pa-te", c), tes = h("span", "", te, "À toi !"), ete = Ecrit(tes, { d: .45 }), ste = Trait(tes, "souligne2", { c: C.sa, ep: 4 });
    var tx = h("div", "pa-tx", c, esc(v.t)), etx = Ecrit(tx, { v: 34 });
    var so = h("div", "pa-so", c, esc(v.sous || "Mets la vidéo sur pause, prends une feuille, puis reprends pour la correction.")), eso = Ecrit(so, { v: 60 });
    var bx = Trait(c, "boite", { c: C.sa, m: 0, ep: 3.4 });
    return function (t, st) {
      var tl = st.tl;
      bx(P(tl, 0, .6)); trace(b1, P(tl, .1, .4)); trace(b2, P(tl, .3, .6)); op(ce, E(P(tl, .8, .4)));
      ete.pose(tl, .35); ste(P(tl, .85, .3)); etx.pose(tl, 1.0); eso.pose(tl, 1.1 + etx.d);
    };
  };

  /* ---------- scène : le livre ouvert ; entre deux parties, la page se tourne ---------- */
  function Scene(EP, racine) {
    var sc = h("div", "scene", racine);
    if (!TEX.regle) TEX.regle = regle(760);
    if (!TEX.papier) { TEX.papier = papier(); TEX.papierURL = TEX.papier.toDataURL("image/jpeg", .9); }
    if (!TEX.planche) { TEX.planche = planche(); TEX.plancheURL = TEX.planche.toDataURL("image/jpeg", .9); }
    sc.style.setProperty("--planche", "url(" + TEX.plancheURL + ")");
    sc.style.setProperty("--papier", "url(" + TEX.papierURL + ")");
    var ard = h("canvas", "ardoise", sc); ard.width = 1920; ard.height = 1080;
    ard.getContext("2d").drawImage(TEX.planche, 0, 0);
    var pretArd = Promise.resolve();
    var livre = h("div", "livre", sc);
    var couche = h("div", "couche", livre);
    var ombre = h("div", "pt-ombre", livre);
    // la feuille qui tourne : la texture de la page ; sa couche reprend les coordonnées de la scène
    var feuille = h("div", "feuille", livre), fc = h("div", "fe-couche", feuille), fv = h("div", "fe-voile", feuille);
    feuille.style.display = "none";
    h("div", "voile", sc);
    var ent = h("div", "entete", sc), entF = h("div", "ent-filet", sc), fil = h("div", "fil", sc), st = h("div", "st", sc), stS = h("span", "", st);
    var objs = EP.vis.map(function (v) {
      var el = h("div", "v", couche), o = { v: v, el: el, disp: "block", entree: "monte", vis: false };
      el.style.display = "none";
      o.upd = (TYPES[v.type] || function () { return function () {}; })(o, v);
      return o;
    });
    // la page se tourne au début de chaque partie (sauf la première)
    var NET = EP.scenes.slice(1).map(function (s) { return { t0: s.t0 - .12, t1: s.t0 + .8 }; });
    // ce qui est encore sur la page à la fin d'une partie y reste : la page tournée l'emporte
    objs.forEach(function (o) { NET.forEach(function (w) { if (o.v.t1 >= w.t0 - 1.5 && o.v.t1 <= w.t1 && !/^(tableau|notion|generique)$/.test(o.v.type)) o.efface = w.t1; }); });
    // passage de relais : quand un visuel commence pendant que le précédent est encore sur la page, le précédent
    // s'efface juste avant (fondu fini au début du suivant) ; le minutage du nouveau, calé sur la voix, ne bouge pas
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
    var DEG = Math.PI / 180;
    function tourne(t) {
      var w = null;
      for (var k = 0; k < NET.length; k++) if (t >= NET[k].t0 && t < NET[k].t1) { w = NET[k]; break; }
      if (!w) { if (feuille.style.display !== "none") feuille.style.display = "none"; op(ombre, 0); return null; }
      var s = EIO(P(t, w.t0, w.t1 - w.t0)), ang = -96 * s;
      if (feuille.style.display === "none") feuille.style.display = "block";
      tr(feuille, "rotateY(" + ang.toFixed(3) + "deg)");
      op(fv, Math.min(1, s * 1.4));
      var x = PAGE.x + PAGE.w * Math.max(0, Math.cos(ang * DEG));
      ombre.style.left = x.toFixed(1) + "px";
      op(ombre, Math.sin(Math.PI * Math.min(1, s * 1.05)) * .9);
      return w;
    }
    var sousOn = false, dernierSous = -1;

    function rendu(t) {
      var w = tourne(t);
      var plein = false;
      objs.forEach(function (o) {
        var v = o.v;
        if (t < v.t0 || t > (o.efface ? o.efface : o.fin < v.t1 ? o.fin + FONDU + .03 : v.t1 + (v.type === "tableau" ? 1 : .6))) { if (o.vis) { o.el.style.display = "none"; o.vis = false; } return; }
        // pendant que la page tourne, ce qu'elle porte part avec elle
        var hote = w && o.efface === w.t1 && t >= w.t0 ? fc : couche;
        if (o.el.parentNode !== hote) hote.appendChild(o.el);
        if (!o.vis) { o.el.style.display = o.disp; o.vis = true; }
        if (v.type === "titre" || v.type === "chapitre" || v.type === "generique" || v.type === "portrait" || v.type === "frappe" || v.type === "flash") plein = true;
        var a = E(P(t, v.t0, .7)), out = o.efface ? 0 : EIO(P(t, o.fin, FONDU));
        if (v.type !== "tableau") o.el.style.opacity = (o.entree === "aucune" ? 1 : a) * (1 - out);
        if (o.entree === "monte") o.el.style.transform = "translateY(" + (20 * (1 - a)).toFixed(2) + "px)";
        o.upd(t, { tl: t - v.t0, a: a, o: out });
      });
      // titre courant, en haut de la page (petites capitales), avec son filet ; caché pendant que la page tourne
      var sc_ = EP.scenes.filter(function (s) { return t >= s.t0; }).pop() || EP.scenes[0];
      var txt = "Entrée " + romain(EP.num) + (sc_.id !== EP.scenes[0].id ? " &nbsp;·&nbsp; <b>" + esc(sc_.chap) + "</b>" : "");
      if (ent._t !== txt) { ent.innerHTML = txt; ent._t = txt; }
      var autour = NET.some(function (x) { return t > x.t0 - .35 && t < x.t1 + .5; });
      var vu = plein || autour ? 0 : E(P(t, EP.scenes[0].t0 + 1, 1)) * .9;
      op(ent, vu); op(entF, vu);
      fil.style.width = (W * cl(t / EP.dur, 0, 1)).toFixed(1) + "px";
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
    m10: '<svg viewBox="0 0 24 24"><path d="M12 5V1L7 6l5 5V7a6 6 0 1 1-6 6H4a8 8 0 1 0 8-8z"/><text x="12" y="16.2" font-size="6.5" text-anchor="middle" font-family="EB Garamond" font-weight="700">10</text></svg>',
    p10: '<svg viewBox="0 0 24 24"><path d="M12 5V1l5 5-5 5V7a6 6 0 1 0 6 6h2a8 8 0 1 1-8-8z"/><text x="12" y="16.2" font-size="6.5" text-anchor="middle" font-family="EB Garamond" font-weight="700">10</text></svg>',
    plein: '<svg viewBox="0 0 24 24"><path d="M4 9V4h5v2H6v3zm11-5h5v5h-2V6h-3zM4 15h2v3h3v2H4zm14 3v-3h2v5h-5v-2z"/></svg>',
    musique: '<svg viewBox="0 0 24 24"><path d="M9 18.5a3 3 0 1 1-2-2.8V5l12-2.5v12.5a3 3 0 1 1-2-2.8V6.9L9 8.6z"/></svg>',
    apause: '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 2a8 8 0 1 1 0 16 8 8 0 0 1 0-16zM8.8 7.5h2.4v9H8.8zm4 0h2.4v9h-2.4z"/></svg>',
    cc: '<svg viewBox="0 0 24 24"><path d="M3 5h18v14H3zm2 2v10h14V7zm2.5 3.2h4v1.5h-2.5v1.6h2.5v1.5h-4zm6 0h4v1.5H15v1.6h2.5v1.5h-4z"/></svg>'
  };

  function lancer(EP) {
    document.title = "Entrée " + romain(EP.num) + " — " + EP.titre + " · HLP Terminale";
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
      h("span", "k", tete, "HLP · entrée " + romain(EP.num) + " · le cours en vidéo");
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
    h("div", "sous", quiz, EP.quiz.length + " questions sur l'entrée. Réponds, puis lis l'explication.");
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
        navigator.mediaSession.metadata = new MediaMetadata({ title: "Entrée " + romain(EP.num) + " · " + EP.titre, artist: "HLP · le cours en vidéo", album: "Terminale spécialité" });
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
    S.rendu(titre ? titre.t0 + 4.2 : 2);   // affiche : la page de titre écrite en entier
    if (tA != null) { aller(tA); affiche.classList.add("off"); }
    majUI(); setTimeout(hauteur, 300);
  }

  window.SERIE = { lancer: lancer };
  window.SERIE_OUTILS = { fleuron: fleuron, manicule: manicule, pointer: pointer, mots: mots, unites: unites, poser: poser, romain: romain, PAGE: PAGE, sv: sv, h: h, lbl: lbl, etiquette: etiquette, ptsBoite: ptsBoite, dPts: dPts, rng: rng, Trait: Trait, Ecrit: Ecrit, C: C, E: E, EIO: EIO, EB: EB, P: P, cl: cl, op: op, tr: tr, et: et, esc: esc, trace: trace, wob: wob, cvs: cvs };
})();
