/* import bac — moteur du site (routeur, surligneur Python, QCM, cartes, recherche, schémas interactifs). */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var MO = function () { return document.documentElement.classList.contains("mo"); };
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function sansAccent(s) { return String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function melange(t) { t = t.slice(); for (var i = t.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = t[i]; t[i] = t[j]; t[j] = x; } return t; }
  function chap(id) { for (var i = 0; i < CH.length; i++) if (CH[i].id === id) return CH[i]; return null; }
  function toutRedige() { return PROG.every(function (r) { return r.items.every(function (it) { return !!it.ch; }); }); }
  /* Ordre des propositions des QCM : dans les données, la bonne réponse est souvent la deuxième. On les range une fois
     pour toutes, de façon déterministe (même ordre à chaque visite) : réponses numériques par ordre croissant,
     sinon permutation tirée de l'énoncé. Seul l'indice de la bonne réponse (a) est recalculé. */
  (function () {
    function nb(s) { var t = String(s).replace(/<[^>]+>/g, "").replace(/[\s  ]/g, "").replace(",", "."); return /^-?\d+(\.\d+)?$/.test(t) ? parseFloat(t) : NaN; }
    function graine(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h; }
    CH.forEach(function (c) {
      c.qcm.forEach(function (q) {
        var idx = q.c.map(function (_, i) { return i; });
        if (q.c.every(function (x) { return !isNaN(nb(x)); })) idx.sort(function (i, j) { return nb(q.c[i]) - nb(q.c[j]); });
        else { var h = graine(q.q); for (var i = idx.length - 1; i > 0; i--) { h = Math.imul(h ^ (h >>> 15), 2246822507) >>> 0; var j = h % (i + 1), x = idx[i]; idx[i] = idx[j]; idx[j] = x; } }
        q.a = idx.indexOf(q.a);
        q.c = idx.map(function (i) { return q.c[i]; });
      });
    });
  })();

  /* ---------- icônes ---------- */
  var IC = {
    menu: '<path d="M4 7h16M4 12h16M4 17h10"/>',
    cherche: '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    lune: '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
    soleil: '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    dossier: '<path d="M3 7.5V18a1.5 1.5 0 0 0 1.5 1.5h15A1.5 1.5 0 0 0 21 18V9a1.5 1.5 0 0 0-1.5-1.5H12L10 5H4.5A1.5 1.5 0 0 0 3 6.5z"/>',
    py: '<path d="M7 3.5h7l4 4V20a.5.5 0 0 1-.5.5h-10.5a.5.5 0 0 1-.5-.5V4a.5.5 0 0 1 .5-.5z"/><path d="M14 3.5V8h4"/><path d="M9 13l-1.5 1.5L9 16M12.5 13l1.5 1.5-1.5 1.5"/>',
    md: '<path d="M7 3.5h7l4 4V20a.5.5 0 0 1-.5.5h-10.5a.5.5 0 0 1-.5-.5V4a.5.5 0 0 1 .5-.5z"/><path d="M14 3.5V8h4M9 12h6M9 15h6M9 18h4"/>',
    terminal: '<rect x="3" y="4.5" width="18" height="15" rx="2"/><path d="M7 10l3 2.5L7 15M12.5 15.5H17"/>',
    carte: '<path d="M4 6.5l5-2 6 2 5-2v13l-5 2-6-2-5 2z"/><path d="M9 4.5v13M15 6.5v13"/>',
    lien: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    cible: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1.2"/>',
    maison: '<path d="M4 11l8-6.5 8 6.5V20H4z"/><path d="M10 20v-5h4v5"/>',
    impr: '<path d="M7 9V4h10v5M7 17H5a1.5 1.5 0 0 1-1.5-1.5v-5A1.5 1.5 0 0 1 5 9h14a1.5 1.5 0 0 1 1.5 1.5v5A1.5 1.5 0 0 1 19 17h-2"/><path d="M7 14h10v6H7z"/>',
    melange: '<path d="M4 7h3.5c4 0 5 10 9 10H20M4 17h3.5c1.6 0 2.7-1.6 3.6-3.5M13 10.5c.9-1.9 2-3.5 3.5-3.5H20M17.5 4.5L20 7l-2.5 2.5M17.5 14.5L20 17l-2.5 2.5"/>',
    retour: '<path d="M9 7L4 12l5 5M4.5 12H20"/>',
    suite: '<path d="M15 7l5 5-5 5M19.5 12H4"/>',
    lecture: '<path d="M8 5.5v13l10.5-6.5z"/>',
    pause: '<path d="M8 5.5v13M16 5.5v13"/>',
    debut: '<path d="M6 5.5v13M18 5.5v13L9 12z"/>',
    epreuve: '<path d="M6 3.5h12v17H6z"/><path d="M9 8h6M9 11.5h6M9 15h3.5"/>',
    cartes: '<rect x="3.5" y="6.5" width="13" height="13" rx="2"/><path d="M7.5 6.5V5a1.5 1.5 0 0 1 1.5-1.5h10A1.5 1.5 0 0 1 20.5 5v10A1.5 1.5 0 0 1 19 16.5h-2.5"/>'
  };
  function ic(n) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (IC[n] || "") + "</svg>"; }

  /* ---------- surligneur Python ---------- */
  var KW = "False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield".split(" ");
  var BI = "print len range int str float bool list dict tuple set type isinstance input abs min max sum sorted reversed enumerate zip map filter round help id open iter next any all repr hash super object chr ord divmod pow".split(" ");
  var EXC = /^[A-Z][A-Za-z]*(Error|Exception|Warning)$/;
  var RE_TOK = /(#[^\n]*)|([rRbBfFuU]{0,2}(?:"""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'))|(\b\d[\d_]*(?:\.\d+)?(?:[eE][+-]?\d+)?\b)|(@[A-Za-z_]\w*)|([A-Za-z_À-ɏ][\wÀ-ɏ]*)|(\s+)|([\s\S])/g;
  function span(cl, t) { return t.split("\n").map(function (p) { return p ? '<span class="' + cl + '">' + esc(p) + "</span>" : ""; }).join("\n"); }
  function hlPy(src) {
    var out = "", m, prev = "";
    RE_TOK.lastIndex = 0;
    while ((m = RE_TOK.exec(src))) {
      var t = m[0];
      if (m[1]) out += span("k-com", t);
      else if (m[2]) out += span("k-str", t);
      else if (m[3]) out += span("k-num", t);
      else if (m[4]) out += span("k-dec", t);
      else if (m[5]) {
        if (prev === "def") out += span("k-fn", t);
        else if (prev === "class") out += span("k-cls", t);
        else if (KW.indexOf(t) >= 0) out += span("k-kw", t);
        else if (t === "self") out += span("k-self", t);
        else if (EXC.test(t)) out += span("k-tr", t);
        else if (BI.indexOf(t) >= 0) out += span("k-bi", t);
        else out += esc(t);
        prev = t;
        continue;
      } else out += esc(t);
      if (!m[6]) prev = t;
    }
    return out;
  }
  function hlConsole(src) {
    return src.split("\n").map(function (l) {
      if (/^(>>>|\.\.\.)( |$)/.test(l)) return '<span class="k-pr">' + esc(l.slice(0, 3)) + "</span>" + hlPy(l.slice(3));
      if (/^Traceback|^\s+File |^[A-Z]\w*(Error|Exception|Warning)\b/.test(l)) return '<span class="k-tr">' + esc(l) + "</span>";
      return '<span class="muet">' + esc(l) + "</span>";
    }).join("\n");
  }
  window.hlPy = hlPy;
  var SQLKW = "SELECT FROM WHERE JOIN INNER LEFT ON AS AND OR NOT IN IS NULL INSERT INTO VALUES UPDATE SET DELETE CREATE TABLE PRIMARY KEY FOREIGN REFERENCES DISTINCT ORDER BY ASC DESC LIKE BETWEEN INTEGER TEXT REAL VARCHAR INT DATE CHAR BOOLEAN DROP UNIQUE".split(" ");
  var SQLFN = "COUNT SUM AVG MIN MAX".split(" ");
  function hlSql(src) {
    var re = /(--[^\n]*)|('(?:''|[^'])*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_À-ɏ][\wÀ-ɏ]*)|([\s\S])/g, m, out = "";
    while ((m = re.exec(src))) {
      if (m[1]) out += span("k-com", m[0]);
      else if (m[2]) out += span("k-str", m[0]);
      else if (m[3]) out += span("k-num", m[0]);
      else if (m[4]) { var u = m[0].toUpperCase(); out += SQLKW.indexOf(u) >= 0 ? span("k-kw", m[0]) : SQLFN.indexOf(u) >= 0 ? span("k-bi", m[0]) : esc(m[0]); }
      else out += esc(m[0]);
    }
    return out;
  }
  function tableSql(txt) {
    var l = txt.replace(/\s+$/, "").split("\n");
    var cel = function (x) { return x.split(" | "); };
    return '<div class="tab-wrap res-sql"><table><tr>' + cel(l[0]).map(function (x) { return "<th>" + esc(x) + "</th>"; }).join("") + "</tr>" +
      l.slice(1).map(function (r) { return "<tr>" + cel(r).map(function (x) { return "<td>" + esc(x) + "</td>"; }).join("") + "</tr>"; }).join("") + "</table></div>";
  }
  function nbLignesSql(c) { var n = c.out.replace(/\s+$/, "").split("\n").length - 1; return n + " ligne" + (n > 1 ? "s" : ""); }
  function lignes(html, opts) {
    opts = opts || {};
    var vis = opts.vise || [], trous = opts.trous || [];
    return html.split("\n").map(function (l, i) {
      var n = i + 1, cl = "l" + (vis.indexOf(n) >= 0 ? " vise" : "") + (trous.indexOf(n) >= 0 ? " trou" : "");
      return '<span class="' + cl + '" data-n="' + n + '">' + (l || " ") + "</span>";
    }).join("");
  }
  function codeHTML(id, mode) {
    var c = CODE[id];
    if (!c) return '<p class="attention">Code manquant : ' + esc(id) + "</p>";
    var src = c.src.replace(/^\n+|\s+$/g, "");
    var cons = !!c.console;
    var h = c.sql ? hlSql(src) : cons ? hlConsole(src) : hlPy(src);
    var nom = c.fichier || (c.sql ? "requête SQL" : cons ? "console Python" : "python");
    var out = "";
    var montrer = mode !== "nosortie" && ((c.out && c.out.trim()) || c.err) && c.montrer !== false;
    if (montrer) {
      if (c.sql && !c.err) out = '<div class="sortie"><div class="tete"><span class="f">' + esc(c.cmd || "sqlite> résultat : " + nbLignesSql(c)) + '</span></div>' + tableSql(c.out) + "</div>";
      else out = '<div class="sortie"><div class="tete"><span class="f">' + esc(c.cmd || (c.sql ? "sqlite>" : "python3 " + (c.fichier || "programme.py"))) + '</span></div><pre>' + sortieTexte(c) + "</pre></div>";
    }
    return '<div class="code zebre' + (cons ? " console" : "") + '" data-code="' + esc(id) + '"><div class="tete"><span class="f">' + esc(nom) + '</span><button type="button" data-copie="' + esc(id) + '">copier</button></div><pre><code>' + lignes(h, { vise: c.vise, trous: c.trous }) + "</code></pre>" + out + "</div>";
  }
  function sortieTexte(c) {
    var t = esc((c.out || "").replace(/\s+$/, ""));
    if (c.err) t = (t ? t + "\n" : "") + '<span class="err-t">' + esc(c.trace || "Traceback (most recent call last):\n  …\n" + c.err) + "</span>";
    return t;
  }
  function fill(html) {
    return String(html).replace(/\[\[([\w-]+)(?:\|([\w,-]+))?\]\]/g, function (_, id, mode) {
      if (id.indexOf("w-") === 0) return '<div data-w="' + id.slice(2) + '"' + (mode ? ' data-opt="' + mode + '"' : "") + "></div>";
      return codeHTML(id, mode);
    });
  }

  /* ---------- navigation ---------- */
  var PAGES_LAT = [
    { h: "accueil", t: "accueil.md", i: "maison" },
    { h: "programme", t: "programme.txt", i: "carte" },
    { h: "epreuve", t: "epreuve.md", i: "epreuve" },
    { h: "entrainement", t: "entrainement.py", i: "cible" },
    { h: "ressources", t: "ressources.url", i: "lien" }
  ];
  function latHTML() {
    var h = '<div class="titre-lat">Explorateur</div><div class="dossier">' + ic("dossier") + "import_bac/</div>";
    h += '<a class="ind" href="#accueil" data-r="accueil">' + ic("md") + "accueil.md</a>";
    groupes().forEach(function (g) {
      h += '<div class="dossier ind">' + ic("dossier") + g.dossier + "/</div>";
      g.ch.forEach(function (c) { h += '<a class="ind2" href="#' + c.id + '" data-r="' + c.id + '">' + ic("py") + c.fichier + "</a>"; });
    });
    PAGES_LAT.slice(1).forEach(function (p) { h += '<a class="ind" href="#' + p.h + '" data-r="' + p.h + '">' + ic(p.i) + p.t + "</a>"; });
    h += '<div class="pied-lat">NSI · spécialité Terminale<br>programme : BO spécial n° 8 du 25/07/2019<br>épreuve : session 2027</div>';
    return h;
  }
  /* Chapitres regroupés par rubrique du programme (dans l'ordre de PROG), les autres à la fin. */
  var DOSSIERS = { "01": "histoire", "02": "structures", "03": "bases_de_donnees", "04": "architecture", "05": "langages", "06": "algorithmique" };
  function groupes() {
    var vus = {}, g = [];
    PROG.forEach(function (rb) {
      var l = [];
      rb.items.forEach(function (it) { var c = it.ch && chap(it.ch); if (c && !vus[c.id]) { vus[c.id] = 1; l.push(c); } });
      if (l.length) g.push({ dossier: DOSSIERS[rb.n] || "chapitres", titre: rb.t, n: rb.n, ch: l });
    });
    var reste = CH.filter(function (c) { return !vus[c.id]; });
    if (reste.length) g.push({ dossier: "autres", titre: "Autres chapitres", n: "··", ch: reste });
    return g;
  }
  var etat = { route: "", qcm: {}, entr: null, fc: {} };
  function routeCourante() {
    var h = decodeURIComponent(location.hash.replace(/^#/, "")) || "accueil";
    var p = h.split("/");
    return { page: p[0], sous: p[1] || "", plus: p[2] || "" };
  }
  function nomFichier(r) {
    var c = chap(r.page);
    if (c) return c.fichier + (r.sous && r.sous[0] !== "i" ? " — " + r.sous : "");
    for (var i = 0; i < PAGES_LAT.length; i++) if (PAGES_LAT[i].h === r.page) return PAGES_LAT[i].t;
    return "accueil.md";
  }
  function invite(dir, cmd) {
    return '<div class="invite"><span class="u">eleve@terminale</span>:<span class="d">~/' + esc(dir) + '</span>$ <span class="c tape">' + esc(cmd) + '</span><span class="curseur"></span></div>';
  }

  var dernierOnglet = null;
  function placerIndicateur(page, c) {
    var nav = $(".onglets", page), on = nav && $(".onglets a.on", nav);
    if (!on) { dernierOnglet = null; return; }
    var ind = document.createElement("span");
    ind.className = "ind-onglet"; nav.appendChild(ind);
    var cible = { l: on.offsetLeft, w: on.offsetWidth };
    if (MO() && dernierOnglet && dernierOnglet.ch === c.id) {
      ind.style.transition = "none"; ind.style.left = dernierOnglet.l + "px"; ind.style.width = dernierOnglet.w + "px";
      void ind.offsetWidth; ind.style.transition = "";
    }
    ind.style.left = cible.l + "px"; ind.style.width = cible.w + "px";
    dernierOnglet = { ch: c.id, l: cible.l, w: cible.w };
  }
  function majLecture() {
    var h = document.documentElement, max = h.scrollHeight - innerHeight, pc = max > 0 ? Math.min(100, Math.round(100 * scrollY / max)) : 100;
    var b = $(".lecture-p i"); if (b) b.style.width = pc + "%";
    var s = $("#st-pc"); if (s) s.textContent = "lecture " + pc + " %";
  }
  /* Typographie française du texte rédigé (jamais dans le code) : espace insécable avant « : » et « » », fine insécable
     avant « ; ! ? », insécable après « « », et entre les tranches de chiffres (1 000), pour qu’aucune ligne ne commence
     par un signe isolé sur téléphone. */
  var SANS_TYPO = { CODE: 1, PRE: 1, KBD: 1, SCRIPT: 1, STYLE: 1, TEXTAREA: 1, svg: 1, SVG: 1 };
  function horsTypo(p) { return SANS_TYPO[p.nodeName] || (p.classList && (p.classList.contains("code") || p.classList.contains("invite"))); }
  function typo(racine) {
    for (var a = racine; a && a.nodeType === 1; a = a.parentNode) if (horsTypo(a)) return;
    var w =document.createTreeWalker(racine, NodeFilter.SHOW_TEXT, { acceptNode: function (n) {
      for (var p = n.parentNode; p && p !== racine; p = p.parentNode) if (horsTypo(p)) return NodeFilter.FILTER_REJECT;
      return /[ :;!?«»\d]/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    } });
    var l = [], n;
    while ((n = w.nextNode())) l.push(n);
    l.forEach(function (t) {
      var v = t.nodeValue, x = v.replace(/ ([:»])/g, " $1").replace(/ ([;!?])/g, " $1").replace(/« /g, "« ").replace(/(\d) (?=\d{3}(?!\d))/g, "$1 ");
      if (x !== v) t.nodeValue = x;
    });
  }
  /* Les schémas et le QCM réécrivent leur texte après le rendu : on applique la même typographie à ce qu’ils ajoutent. */
  var obsTypo = null;
  function suivreTypo(page) {
    if (obsTypo || typeof MutationObserver === "undefined") return;
    obsTypo = new MutationObserver(function (ms) {
      ms.forEach(function (m) {
        Array.prototype.forEach.call(m.addedNodes, function (n) {
          if (n.nodeType === 1) typo(n);
          else if (n.nodeType === 3 && n.parentNode) { var p = n.parentNode; if (p.nodeType === 1) typo(p); }
        });
      });
    });
    obsTypo.observe(page, { childList: true, subtree: true });
  }
  function render() {
    var r = routeCourante();
    var page = $("#page");
    var html = "";
    var c = chap(r.page);
    page.className = "page";
    if (c) html = pageChapitre(c, r);
    else if (r.page === "programme") html = pageProgramme(r);
    else if (r.page === "epreuve") html = pageTexte(PAGE_EPREUVE, "epreuve", "cat epreuve.md");
    else if (r.page === "ressources") html = pageTexte(PAGE_RESSOURCES, "ressources", "cat ressources.url");
    else if (r.page === "entrainement") html = pageEntrainement(r);
    else { html = pageAccueil(); page.className = "page large"; }
    page.innerHTML = html;
    typo(page);
    suivreTypo(page);
    $("#fic").textContent = nomFichier(r);
    $$(".lat a").forEach(function (a) { a.classList.toggle("actif", a.getAttribute("data-r") === r.page); });
    document.title = (c ? c.titre + " — " : r.page !== "accueil" && r.page ? nomFichier(r).replace(/\..*$/, "") + " — " : "") + "import bac · NSI Terminale";
    initPage(page, r);
    if (c) placerIndicateur(page, c); else dernierOnglet = null;
    var st = $("#st-fic"); if (st) st.textContent = nomFichier(r);
    var idee = c && /^i\d+$/.test(r.sous) ? r.sous : (c && /^i\d+$/.test(r.plus) ? r.plus : "");
    var item = r.page === "programme" && r.sous ? r.sous : "";
    if (idee) {
      var el = document.getElementById(c.id + "-" + idee);
      if (el) { el.scrollIntoView({ block: "start" }); el.classList.remove("flash"); void el.offsetWidth; el.classList.add("flash"); }
    } else if (item) {
      var d = document.getElementById("prog-" + item);
      if (d) { d.open = true; d.scrollIntoView({ block: "start" }); }
    } else window.scrollTo(0, 0);
    majLecture();
    if (MO()) { page.classList.remove("entree"); void page.offsetWidth; page.classList.add("entree"); }
  }

  /* ---------- accueil ---------- */
  function pageAccueil() {
    var nbQ = 0, nbC = 0; CH.forEach(function (c) { nbQ += c.qcm.length; nbC += c.cartes.length; });
    var term = [
      ['<span class="pr">$</span> python3', 0],
      ['<span class="pr">&gt;&gt;&gt;</span> import bac', 1],
      ['<span class="pr">&gt;&gt;&gt;</span> bac.nsi.chapitres()', 2],
      ['<span class="rep">' + esc(JSON.stringify(CH.map(function (c) { return c.court; })).replace(/"/g, "'").replace(/,/g, ", ")) + "</span>", 3],
      ['<span class="pr">&gt;&gt;&gt;</span> bac.nsi.epreuve', 4],
      ['<span class="ok">écrit 3 h 30 + pratique 1 h · coef. 16</span>', 5],
      ['<span class="pr">&gt;&gt;&gt;</span> <span class="curseur"></span>', 6]
    ].map(function (l) { return '<span class="ligne" style="animation-delay:' + (0.2 + l[1] * 0.3).toFixed(2) + 's">' + l[0] + "</span>"; }).join("\n");
    var h = '<div class="heros"><div>' + invite("", "python3 -m bac --nsi") + '<h1><span class="kw">import</span> <span class="bac">bac</span></h1>' +
      '<p class="acc">Le terminal de révision de la spécialité <b>NSI en Terminale</b> : cours rédigés à fond, code Python testé ligne à ligne, schémas qui s’animent, QCM, cartes mémoire et exercices type bac.</p>' +
      '<div class="rangee"><a class="btn prim" href="#' + CH[0].id + '">' + ic("lecture") + "Commencer le chapitre 1</a>" +
      '<a class="btn" href="#entrainement">' + ic("cible") + "S’entraîner</a></div></div>" +
      '<div class="terminal" aria-label="Exemple de session Python"><div class="tete"><i></i><i></i><i></i><span>bac — python3</span></div><pre>' + term + "</pre></div></div>";
    h += '<div class="chiffres"><div><b>' + CH.length + '</b><span>chapitres rédigés</span></div><div><b>' + nbQ + '</b><span>questions de QCM</span></div><div><b>' + nbC + '</b><span>cartes mémoire</span></div><div><b>' + Object.keys(CODE).filter(function (k) { return CODE[k].run !== false; }).length + '</b><span>extraits de code exécutés et vérifiés</span></div></div>';
    h += "<h2>Les chapitres</h2><p class=\"muet\">Rangés par rubrique du programme. Chaque chapitre se lit seul : suis l’ordre de ton professeur.</p>";
    groupes().forEach(function (g) {
      h += '<div class="dossier-acc mono"><span class="n">' + g.n + '</span> ' + g.dossier + '/ <span class="muet">— ' + esc(g.titre) + "</span></div><div class=\"grille\">";
      g.ch.forEach(function (c) {
        h += '<a class="carte-ch" href="#' + c.id + '"><span class="fic">' + c.fichier + '</span><span class="nom">' + c.n + ". " + esc(c.titre) + '</span><span class="desc">' + esc(c.accroche) + '</span><span class="pied">' + c.idees.length + " notions · " + c.qcm.length + " QCM · " + c.cartes.length + " cartes</span></a>";
      });
      h += "</div>";
    });
    h += "<h2>Carte du programme</h2><p class=\"muet\">Les six rubriques officielles du programme de Terminale" + (toutRedige() ? ", toutes rédigées sur le site." : ". Ce qui n’est pas encore rédigé est marqué « bientôt », avec ce que le programme demande.") + "</p>";
    PROG.forEach(function (r) {
      h += '<div class="rubrique"><div class="tete"><span class="n">' + r.n + "</span>" + esc(r.t) + "</div>";
      r.items.forEach(function (it) {
        var lien = it.ch ? "#" + it.ch : "#programme/" + it.id;
        h += '<div class="item-prog"><a href="' + lien + '"><span class="st ' + (it.ch ? "ok" : "bt") + '">' + (it.ch ? "rédigé" : "bientôt") + '</span><span class="ti">' + esc(it.t) + "</span></a></div>";
      });
      h += "</div>";
    });
    h += '<h2>Accès rapide</h2><div class="grille"><a class="carte-ch" href="#epreuve"><span class="fic">epreuve.md</span><span class="nom">L’épreuve</span><span class="desc">Écrit de 3 h 30, partie pratique d’1 h : format 2027, méthode, copie commentée, Grand oral.</span></a><a class="carte-ch" href="#entrainement"><span class="fic">entrainement.py</span><span class="nom">Entraînement</span><span class="desc">QCM mélangé de tous les chapitres et toutes les cartes mémoire.</span></a><a class="carte-ch" href="#ressources"><span class="fic">ressources.url</span><span class="nom">Ressources</span><span class="desc">Programme officiel, banque de l’épreuve pratique, annales, exercices en ligne, vidéos.</span></a></div>';
    h += pied();
    return h;
  }
  function pied() { return '<div class="pied"># Site indépendant, contenu original. Le programme officiel et les notes de service font foi. Exemples de code exécutés avec Python 3.</div>'; }

  /* ---------- chapitre ---------- */
  var SOUS = [["", "cours"], ["exos", "exercices"], ["qcm", "qcm"], ["cartes", "cartes"], ["retenir", "à retenir"]];
  function pageChapitre(c, r) {
    var sous = r.sous && !/^i\d+$/.test(r.sous) ? r.sous : "";
    var h = invite("chapitres", (sous === "" ? "cat " : sous === "exos" ? "python3 " : sous === "qcm" ? "python3 -m qcm " : sous === "cartes" ? "python3 -m cartes " : "lpr ") + c.fichier);
    h += "<h1>" + c.n + ". " + esc(c.titre) + '</h1><p class="soustitre">' + esc(c.rubrique) + "</p>";
    h += '<nav class="onglets" aria-label="Parties du chapitre">' + SOUS.map(function (s) {
      return '<a href="#' + c.id + (s[0] ? "/" + s[0] : "") + '" class="' + (s[0] === sous ? "on" : "") + '"><span class="x">' + (s[0] === "" ? "▸" : "·") + "</span>" + s[1] + "</a>";
    }).join("") + "</nav>";
    if (sous === "exos") h += exosHTML(c);
    else if (sous === "qcm") h += qcmHTML(c.qcm, "q-" + c.id, c);
    else if (sous === "cartes") h += '<div data-fc="' + c.id + '"></div>';
    else if (sous === "retenir") h += '<div class="rangee no-print"><button class="btn prim" type="button" data-imprimer>' + ic("impr") + 'Imprimer la fiche</button></div><div class="fiche">' + fill(c.retenir) + "</div>";
    else h += coursHTML(c);
    var i = CH.indexOf(c);
    h += '<div class="nav-ch">' + (i > 0 ? '<a class="btn" href="#' + CH[i - 1].id + '">' + ic("retour") + CH[i - 1].court + "</a>" : "<span></span>") + (i < CH.length - 1 ? '<a class="btn" href="#' + CH[i + 1].id + '">' + CH[i + 1].court + ic("suite") + "</a>" : '<a class="btn" href="#entrainement">entraînement' + ic("suite") + "</a>") + "</div>";
    return h + pied();
  }
  function coursHTML(c) {
    var h = '<div class="essentiel"><div class="t"># L’essentiel en 5 lignes</div><ol>' + c.essentiel.map(function (l) { return "<li><span>" + l + "</span></li>"; }).join("") + "</ol></div>";
    h += '<h2>Ce que le programme attend</h2><ul class="attendus">' + c.attendus.map(function (l) { return "<li><span>" + l + "</span></li>"; }).join("") + "</ul>";
    if (c.intro) h += fill(c.intro);
    h += "<h2>Le cours</h2>";
    c.idees.forEach(function (d, k) {
      h += '<section class="idee" id="' + c.id + "-" + d.id + '"><span class="num-idee">' + c.n + "." + (k + 1) + "</span><h3>" + d.t + "</h3>" + fill(d.h) + "</section>";
    });
    h += '<h2>Pièges et erreurs fréquentes</h2>';
    c.pieges.forEach(function (p) { h += '<div class="boite attention"><div class="lab">⚠ ' + p.t + "</div>" + fill(p.h) + "</div>"; });
    h += '<div class="rangee"><a class="btn prim" href="#' + c.id + '/exos">' + ic("terminal") + 'Passer aux exercices</a><a class="btn" href="#' + c.id + '/qcm">' + ic("cible") + "QCM du chapitre</a></div>";
    return h;
  }
  function exosHTML(c) {
    var h = "<h2>Prédis la sortie</h2><p class=\"muet\">Lis le programme sans l’exécuter, écris sur papier ce qu’il affiche, puis ouvre la réponse. C’est exactement ce qu’on te demande à l’écrit.</p>";
    c.predis.forEach(function (p, k) {
      h += '<div class="exo"><div class="tete"><span class="t">prédis_' + (k + 1) + ".py</span>" + (p.niv ? '<span class="etiq">' + p.niv + "</span>" : "") + '</div><div class="corps">' + (p.q ? "<p>" + p.q + "</p>" : "") + codeHTML(p.code, "nosortie") +
        '<details class="reponse"><summary>Afficher la sortie et l’explication</summary><div class="corps">' + sortieSeule(p.code) + "<p>" + p.rep + "</p></div></details></div></div>";
    });
    h += "<h2>Type épreuve pratique</h2><p class=\"muet\">Format de la partie pratique : un programme fourni, des questions où l’on programme, teste, corrige un bug et explique son code à l’examinateur. Exercices inventés pour le site, sur ce modèle.</p>";
    c.ep.forEach(function (e, k) { h += exoHTML(e, "pratique_" + (k + 1) + ".py", '<span class="etiq v">≈ 1 h · sur machine</span>'); });
    h += "<h2>Type épreuve écrite</h2>";
    h += exoHTML(c.ecrit, "ecrit.pdf", '<span class="etiq a">' + esc(c.ecrit.points || "") + "</span>");
    return h;
  }
  function sortieSeule(id) {
    var c = CODE[id]; if (!c) return "";
    if (c.sql && !c.err) return '<div class="code"><div class="sortie" style="border-top:0"><div class="tete"><span class="f">sqlite> résultat : ' + nbLignesSql(c) + '</span></div>' + tableSql(c.out) + "</div></div>";
    return '<div class="code"><div class="sortie" style="border-top:0"><div class="tete"><span class="f">python3 prédis.py</span></div><pre>' + sortieTexte(c) + "</pre></div></div>";
  }
  function exoHTML(e, fic, badge) {
    var h = '<div class="exo"><div class="tete"><span class="t">' + esc(fic) + " · " + e.titre + "</span>" + (badge || "") + '</div><div class="corps">';
    if (e.note) h += '<p class="muet petit">' + e.note + "</p>";
    h += fill(e.enonce || "");
    (e.questions || []).forEach(function (q, k) {
      h += '<p class="question"><span class="nq">Q' + (k + 1) + ".</span>" + q.q + (q.pts ? ' <span class="bareme">(' + q.pts + ")</span>" : "") + "</p>";
      if (q.code) h += fill(q.code);
      h += '<details class="reponse"><summary>Corrigé</summary><div class="corps">' + fill(q.c) + "</div></details>";
    });
    if (e.methode) h += '<div class="boite retenir-b"><div class="lab"># méthode</div>' + e.methode + "</div>";
    return h + "</div></div>";
  }

  /* ---------- QCM ---------- */
  function qcmHTML(liste, cle, c) {
    var st = etat.qcm[cle] || (etat.qcm[cle] = { rep: {} });
    var h = '<div class="qcm-score" data-score="' + cle + '"><span class="sc"></span><span class="barre-p"><i></i></span><button class="btn petit" type="button" data-raz="' + cle + '">recommencer</button></div>';
    liste.forEach(function (q, k) {
      h += '<div class="q" data-k="' + k + '"><div class="enonce"><span class="nq">' + (k + 1) + ".</span>" + q.q + "</div>" + (q.code ? fill(q.code) : "") + '<div class="choix">' +
        q.c.map(function (ch, j) { return '<button type="button" data-j="' + j + '"><span class="lt">' + "ABCDE"[j] + '</span><span>' + ch + "</span></button>"; }).join("") + '</div><div class="slot"></div></div>';
    });
    return '<div data-qcm="' + cle + '">' + h + "</div>";
  }
  function initQCM(zone, liste, cle) {
    var st = etat.qcm[cle] || (etat.qcm[cle] = { rep: {} });
    function maj() {
      var n = 0, ok = 0;
      Object.keys(st.rep).forEach(function (k) { n++; if (st.rep[k] === liste[k].a) ok++; });
      $(".sc", zone).innerHTML = '<span class="ok">' + ok + " passed</span>, " + '<span class="ko">' + (n - ok) + " failed</span>, " + (liste.length - n) + " à faire";
      $(".barre-p i", zone).style.width = (100 * n / liste.length) + "%";
    }
    function montre(qel, k, j, anim) {
      var q = liste[k], bon = j === q.a;
      $$(".choix button", qel).forEach(function (b, i) { b.disabled = true; if (i === q.a) b.classList.add("bon"); else if (i === j) b.classList.add("faux"); });
      var ref = q.ref ? q.ref.split(":") : null;
      var lien = ref ? '<a class="lien-revoir" href="#' + ref[0] + "/" + ref[1] + '">' + ic("retour") + "Revoir le paragraphe</a>" : "";
      $(".slot", qel).innerHTML = '<div class="expl"><span class="v ' + (bon ? "ok" : "ko") + '">' + (bon ? "PASSED ✔ " : "FAILED ✘ attendu : " + "ABCDE"[q.a] + " · ") + "</span>" + q.e + "<br>" + lien + "</div>";
      typo($(".slot", qel));
      qel.classList.add("repondu", bon ? "ok" : "ko");
      if (anim === false) qel.classList.remove("ok", "ko");
    }
    $$(".q", zone).forEach(function (qel) {
      var k = +qel.getAttribute("data-k");
      if (st.rep[k] !== undefined) montre(qel, k, st.rep[k], false);
      $$(".choix button", qel).forEach(function (b) {
        b.addEventListener("click", function () {
          if (st.rep[k] !== undefined) return;
          st.rep[k] = +b.getAttribute("data-j");
          montre(qel, k, st.rep[k]);
          maj();
        });
      });
    });
    var raz = $("[data-raz]", zone);
    raz.addEventListener("click", function () { st.rep = {}; if (cle === "entr") etat.entr = null; render(); });
    maj();
  }
  function tousQCM() {
    var t = [];
    CH.forEach(function (c) { c.qcm.forEach(function (q) { var x = Object.assign({}, q); x.ref = x.ref || null; if (x.ref && x.ref.indexOf(":") < 0) x.ref = c.id + ":" + x.ref; x.ch = c; t.push(x); }); });
    return t;
  }

  /* ---------- cartes mémoire ---------- */
  function initFC(el, cartes, cle) {
    var st = etat.fc[cle] || (etat.fc[cle] = { ordre: cartes.map(function (_, i) { return i; }), i: 0, su: {}, rv: {} });
    function draw() {
      var k = st.ordre[st.i], c = cartes[k];
      var nbS = Object.keys(st.su).length, nbR = Object.keys(st.rv).length;
      el.innerHTML = '<div class="fc-zone"><button class="fc" type="button" aria-label="Retourner la carte"><span class="in"><span class="face recto"><span class="lab">' + esc(c.ch || "") + " · carte " + (st.i + 1) + " / " + st.ordre.length + '</span><span class="txt">' + c.r + '</span><span class="lab">touche pour retourner</span></span><span class="face verso"><span class="lab">réponse</span><span class="txt">' + c.v + "</span></span></span></button>" +
        '<div class="fc-nav"><button class="btn petit" type="button" data-a="prec">' + ic("retour") + '</button><button class="btn petit" type="button" data-a="rv">à revoir</button><button class="btn petit prim" type="button" data-a="su">je savais</button><button class="btn petit" type="button" data-a="suiv">' + ic("suite") + "</button></div>" +
        '<div class="fc-nav"><span>✔ ' + nbS + " su · ↺ " + nbR + ' à revoir</span><button class="btn petit" type="button" data-a="mel">' + ic("melange") + "mélanger</button>" + (nbR ? '<button class="btn petit" type="button" data-a="ratees">revoir les ' + nbR + " ratées</button>" : "") + "</div></div>";
      var fc = $(".fc", el);
      fc.addEventListener("click", function () { fc.classList.toggle("tourne"); });
      $$("[data-a]", el).forEach(function (b) {
        b.addEventListener("click", function () {
          var a = b.getAttribute("data-a");
          if (a === "prec") st.i = (st.i - 1 + st.ordre.length) % st.ordre.length;
          else if (a === "suiv") st.i = (st.i + 1) % st.ordre.length;
          else if (a === "su" || a === "rv") { var kk = st.ordre[st.i]; if (a === "su") { st.su[kk] = 1; delete st.rv[kk]; } else { st.rv[kk] = 1; delete st.su[kk]; } st.i = (st.i + 1) % st.ordre.length; }
          else if (a === "mel") { st.ordre = melange(cartes.map(function (_, i) { return i; })); st.i = 0; }
          else if (a === "ratees") { st.ordre = melange(Object.keys(st.rv).map(Number)); st.i = 0; }
          draw();
        });
      });
    }
    draw();
  }

  /* ---------- programme ---------- */
  function pageProgramme(r) {
    var h = invite("", "less programme.txt") + "<h1>Carte du programme</h1><p class=\"soustitre\">Programme de Terminale (arrêté du 19/07/2019, BO spécial n° 8 du 25/07/2019), en six rubriques. Le BO précise qu’il « ne constitue pas un plan de cours » : chaque professeur choisit sa progression.</p>";
    if (toutRedige()) h += '<div class="boite def"><div class="lab"># légende</div><p><span class="etiq v">rédigé</span> chaque point du programme renvoie à son chapitre complet sur le site.</p></div>';
    else h += '<div class="boite def"><div class="lab"># légende</div><p><span class="etiq v">rédigé</span> chapitre complet sur le site · <span class="etiq">bientôt</span> pas encore rédigé : tu trouves déjà ce que le programme demande (contenus, capacités, commentaires officiels reformulés) et ce qu’il faut avoir revu avant.</p></div>';
    PROG.forEach(function (rb) {
      h += '<div class="rubrique"><div class="tete"><span class="n">' + rb.n + "</span>" + esc(rb.t) + "</div>";
      if (rb.intro) h += '<div style="padding:8px 14px" class="petit muet">' + rb.intro + "</div>";
      rb.items.forEach(function (it) {
        if (it.ch) {
          var c = chap(it.ch);
          h += '<div class="item-prog"><a href="#' + it.ch + '"><span class="st ok">rédigé</span><span class="ti">' + esc(it.t) + '</span><span class="muet petit mono">' + (c ? c.fichier : "") + "</span></a></div>";
        } else {
          h += '<details class="item-prog" id="prog-' + it.id + '"><summary><span class="st bt">bientôt</span><span class="ti">' + esc(it.t) + '</span><span class="muet">▾</span></summary><div class="corps">' +
            "<h4>Contenus</h4><p>" + it.contenus + "</p><h4>Capacités attendues</h4><ul>" + it.capacites.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ul>" +
            (it.comm ? "<h4>Précisions</h4><p>" + it.comm + "</p>" : "") + (it.avant ? "<h4>À revoir avant</h4><p>" + it.avant + "</p>" : "") + "</div></details>";
        }
      });
      h += "</div>";
    });
    return h + pied();
  }
  function pageTexte(P, dir, cmd) { return invite("", cmd) + "<h1>" + P.titre + '</h1><p class="soustitre">' + P.sous + "</p>" + fill(P.html) + pied(); }

  /* ---------- entraînement ---------- */
  function pageEntrainement(r) {
    var h = invite("", "python3 entrainement.py") + "<h1>Entraînement</h1><p class=\"soustitre\">Tout le site mélangé : un QCM de 15 questions tirées au hasard dans les " + CH.length + " chapitres, puis toutes les cartes mémoire.</p>";
    h += '<nav class="onglets"><a href="#entrainement" class="' + (r.sous !== "cartes" ? "on" : "") + '"><span class="x">▸</span>qcm mélangé</a><a href="#entrainement/cartes" class="' + (r.sous === "cartes" ? "on" : "") + '"><span class="x">·</span>toutes les cartes</a></nav>';
    if (r.sous === "cartes") h += '<div data-fc="tout"></div>';
    else {
      if (!etat.entr) etat.entr = melange(tousQCM()).slice(0, 15);
      h += '<p class="rangee"><button class="btn" type="button" data-nouvelle>' + ic("melange") + "Nouvelle série</button></p>";
      h += qcmHTML(etat.entr.map(function (q) { var x = Object.assign({}, q); x.q = '<span class="etiq">' + q.ch.court + "</span> " + q.q; return x; }), "entr");
    }
    return h + pied();
  }

  /* ---------- initialisation d'une page ---------- */
  function initPage(page, r) {
    $$("[data-qcm]", page).forEach(function (z) {
      var cle = z.getAttribute("data-qcm");
      var liste = cle === "entr" ? etat.entr : chap(cle.slice(2)).qcm.map(function (q) { var x = Object.assign({}, q); if (x.ref && x.ref.indexOf(":") < 0) x.ref = cle.slice(2) + ":" + x.ref; return x; });
      initQCM(z, liste, cle);
    });
    $$("[data-fc]", page).forEach(function (z) {
      var k = z.getAttribute("data-fc"), cartes;
      if (k === "tout") { cartes = []; CH.forEach(function (c) { c.cartes.forEach(function (x) { cartes.push(Object.assign({ ch: c.court }, x)); }); }); }
      else { var c = chap(k); cartes = c.cartes.map(function (x) { return Object.assign({ ch: c.court }, x); }); }
      initFC(z, cartes, k);
    });
    var nv = $("[data-nouvelle]", page);
    if (nv) nv.addEventListener("click", function () { etat.entr = null; delete etat.qcm.entr; render(); });
    var imp = $("[data-imprimer]", page);
    if (imp) imp.addEventListener("click", function () { window.print(); });
    $$("[data-w]", page).forEach(function (z) { var k = z.getAttribute("data-w"), f = WIDGETS[k] || (window.WIDGETS_EXT || {})[k]; if (f) f(z, z.getAttribute("data-opt"), OUTILS); });
    marquerDefilement(page);
  }
  /* Blocs de code plus larges que l'écran : un fondu à droite signale qu'on peut faire glisser le code. */
  function marquerDefilement(racine) {
    $$(".code > pre", racine).forEach(function (pre) {
      var c = pre.parentNode, f = $(":scope > .fondu-d", c);
      var deborde = pre.scrollWidth > pre.clientWidth + 2;
      if (!deborde) { if (f) c.removeChild(f); return; }
      if (!f) {
        f = document.createElement("span"); f.className = "fondu-d"; f.setAttribute("aria-hidden", "true"); c.appendChild(f);
        pre.addEventListener("scroll", function () { f.classList.toggle("fin", pre.scrollLeft + pre.clientWidth >= pre.scrollWidth - 4); }, { passive: true });
      }
      f.style.top = pre.offsetTop + "px"; f.style.height = pre.offsetHeight + "px";
    });
  }
  var attenteTaille = null;
  window.addEventListener("resize", function () { clearTimeout(attenteTaille); attenteTaille = setTimeout(function () { marquerDefilement($("#page")); }, 200); });
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-copie]");
    if (!b) return;
    var src = CODE[b.getAttribute("data-copie")].src.replace(/^\n+|\s+$/g, "");
    var fini = function () { b.textContent = "copié ✓"; setTimeout(function () { b.textContent = "copier"; }, 1400); };
    if (navigator.clipboard) navigator.clipboard.writeText(src).then(fini, function () {});
  });

  /* ---------- recherche plein écran ---------- */
  var INDEX = null;
  function texte(h) { return String(h).replace(/<div class="lab">[\s\S]*?<\/div>/g, " ").replace(/\[\[([\w-]+)(?:\|[\w,-]+)?\]\]/g, function (_, id) { return CODE[id] ? " " + CODE[id].src + " " : " "; }).replace(/<[^>]+>/g, " ").replace(/&[a-z]+;/g, " ").replace(/\s+/g, " ").replace(/\( /g, "(").replace(/ ([),.])/g, "$1").trim(); }
  function construireIndex() {
    INDEX = [];
    CH.forEach(function (c) {
      c.idees.forEach(function (d, k) { INDEX.push({ t: texte(d.t), o: c.fichier + " · " + c.n + "." + (k + 1), x: texte(d.h), h: "#" + c.id + "/" + d.id }); });
      c.pieges.forEach(function (p) { INDEX.push({ t: texte(p.t), o: c.fichier + " · piège", x: texte(p.h), h: "#" + c.id }); });
      c.cartes.forEach(function (p) { INDEX.push({ t: texte(p.r), o: c.fichier + " · carte mémoire", x: texte(p.v), h: "#" + c.id + "/cartes" }); });
      INDEX.push({ t: c.titre + " — exercices", o: c.fichier + " · exercices", x: c.ep.map(function (e) { return texte(e.titre + " " + e.enonce); }).join(" ") + " " + texte(c.ecrit.titre), h: "#" + c.id + "/exos" });
    });
    PROG.forEach(function (rb) { rb.items.forEach(function (it) { if (!it.ch) INDEX.push({ t: it.t, o: "programme.txt · bientôt · " + rb.t, x: texte(it.contenus + " " + it.capacites.join(" ")), h: "#programme/" + it.id }); }); });
    [[PAGE_EPREUVE, "#epreuve", "epreuve.md"], [PAGE_RESSOURCES, "#ressources", "ressources.url"]].forEach(function (p) {
      p[0].html.split(/<h2>/).forEach(function (s, i) {
        var t = i ? s.split("</h2>")[0] : p[0].titre;
        INDEX.push({ t: texte(t), o: p[2], x: texte(i ? s.split("</h2>").slice(1).join(" ") : s), h: p[1] });
      });
    });
    INDEX.forEach(function (e) { e.nt = sansAccent(e.t); e.nx = sansAccent(e.x); });
  }
  function chercher(q) {
    var mots = sansAccent(q).split(/\s+/).filter(function (m) { return m.length > 1; });
    if (!mots.length) return [];
    var res = [];
    INDEX.forEach(function (e) {
      var s = 0;
      for (var i = 0; i < mots.length; i++) { var a = e.nt.indexOf(mots[i]) >= 0, b = e.nx.indexOf(mots[i]) >= 0; if (!a && !b) return; s += (a ? 5 : 0) + (b ? 1 : 0); }
      res.push({ e: e, s: s });
    });
    return res.sort(function (a, b) { return b.s - a.s; }).slice(0, 30);
  }
  function extrait(e, mots) {
    var i = -1; for (var k = 0; k < mots.length && i < 0; k++) i = e.nx.indexOf(mots[k]);
    var d = Math.max(0, i - 50), t = e.x.slice(d, d + 150);
    var h = esc((d ? "…" : "") + t + (d + 150 < e.x.length ? "…" : ""));
    mots.forEach(function (m) { if (m.length < 2) return; var re = new RegExp("(" + m.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi"); h = h.replace(re, "<mark>$1</mark>"); });
    return h;
  }
  var srchOuvert = false, navApres = null;
  function ouvrirRecherche() {
    if (srchOuvert) return;
    if (!INDEX) construireIndex();
    srchOuvert = true;
    $("#srch").classList.add("on");
    history.pushState({ srch: 1 }, "");
    var i = $("#sq"); i.value = ""; $("#sres").innerHTML = '<div class="aide">Tape un mot : récursivité, self, FIFO, assert, IndexError, maillon…<br>Échap ou bouton retour pour fermer.</div>';
    i.focus();
  }
  function fermerRecherche(depuisHistorique) {
    if (!srchOuvert) return;
    srchOuvert = false;
    $("#srch").classList.remove("on");
    if (!depuisHistorique) history.back();
  }
  function afficherResultats() {
    var q = $("#sq").value, res = chercher(q), mots = sansAccent(q).split(/\s+/).filter(Boolean);
    var z = $("#sres");
    if (!q.trim()) { z.innerHTML = '<div class="aide">Tape au moins deux lettres.</div>'; return; }
    if (!res.length) { z.innerHTML = '<div class="aide">Aucun résultat pour « ' + esc(q) + " ».</div>"; return; }
    z.innerHTML = res.map(function (r) { return '<a href="' + r.e.h + '" data-h="' + r.e.h + '"><span class="o">' + esc(r.e.o) + "</span>" + esc(r.e.t) + '<span class="x">' + extrait(r.e, mots) + "</span></a>"; }).join("");
  }

  /* ---------- menu latéral (téléphone) ---------- */
  var menuOuvert = false;
  function ouvrirMenu() { if (menuOuvert) return; menuOuvert = true; $(".lat").classList.add("ouvert"); $(".voile").classList.add("on"); history.pushState({ menu: 1 }, ""); }
  function fermerMenu(depuisHistorique) { if (!menuOuvert) return; menuOuvert = false; $(".lat").classList.remove("ouvert"); $(".voile").classList.remove("on"); if (!depuisHistorique) history.back(); }

  /* ---------- démarrage ---------- */
  /* Ordre des chapitres : ch1, ch2… (numéros cités dans les textes) puis les autres dans l'ordre du programme. */
  (function () {
    var fixes = CH.filter(function (c) { return /^ch\d+$/.test(c.id); }).sort(function (a, b) { return a.n - b.n; });
    var autres = [];
    groupes().forEach(function (g) { g.ch.forEach(function (c) { if (fixes.indexOf(c) < 0 && autres.indexOf(c) < 0) autres.push(c); }); });
    CH.forEach(function (c) { if (fixes.indexOf(c) < 0 && autres.indexOf(c) < 0) autres.push(c); });
    var tous = fixes.concat(autres);
    CH.length = 0;
    tous.forEach(function (c, i) { c.n = i + 1; CH.push(c); });
  })();
  /* Les bonnes réponses sont réparties sur toutes les lettres par une rotation fixe des propositions. */
  CH.forEach(function (c) {
    c.qcm.forEach(function (q, k) {
      var n = q.c.length, t = (k * 3 + c.n) % n, r = (t - q.a + n) % n, nv = [];
      q.c.forEach(function (x, i) { nv[(i + r) % n] = x; });
      q.c = nv; q.a = t;
    });
  });
  function demarrer() {
    $(".lat").innerHTML = latHTML();
    $(".btn-menu").addEventListener("click", ouvrirMenu);
    $(".voile").addEventListener("click", function () { fermerMenu(); });
    $(".lat").addEventListener("click", function (e) {
      var a = e.target.closest("a"); if (!a || !menuOuvert) return;
      e.preventDefault(); navApres = a.getAttribute("href"); fermerMenu();
    });
    $(".btn-cherche").addEventListener("click", ouvrirRecherche);
    $("#sq").addEventListener("input", afficherResultats);
    $("#sq").addEventListener("keydown", function (e) {
      if (e.key === "Escape") { e.preventDefault(); fermerRecherche(); }
      if (e.key === "Enter") { var a = $("#sres a"); if (a) { e.preventDefault(); a.click(); } }
    });
    $("#sres").addEventListener("click", function (e) { var a = e.target.closest("a[data-h]"); if (!a) return; e.preventDefault(); navApres = a.getAttribute("data-h"); fermerRecherche(); });
    $("#sfermer").addEventListener("click", function () { fermerRecherche(); });
    $("#theme").addEventListener("click", function () {
      var d = document.documentElement, sombre = d.getAttribute("data-theme") ? d.getAttribute("data-theme") === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      d.setAttribute("data-theme", sombre ? "light" : "dark");
      $("#theme").innerHTML = ic(sombre ? "lune" : "soleil");
      var m = document.querySelector('meta[name="theme-color"]'); if (m) m.setAttribute("content", sombre ? "#F8F6EC" : "#0A1114");
    });
    var sombre0 = matchMedia("(prefers-color-scheme: dark)").matches;
    $("#theme").innerHTML = ic(sombre0 ? "soleil" : "lune");
    $(".btn-menu").innerHTML = ic("menu");
    $(".btn-cherche").innerHTML = ic("cherche") + '<span class="t">rechercher <kbd>Ctrl K</kbd></span>';
    $("#sfermer").innerHTML = ic("retour");
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); ouvrirRecherche(); }
      else if (e.key === "/" && !srchOuvert && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); ouvrirRecherche(); }
    });
    window.addEventListener("popstate", function () {
      if (srchOuvert) fermerRecherche(true);
      if (menuOuvert) fermerMenu(true);
      if (navApres) { var h = navApres; navApres = null; if (location.hash === h) render(); else location.hash = h; }
    });
    window.addEventListener("hashchange", render);
    var attente = false;
    window.addEventListener("scroll", function () { if (attente) return; attente = true; requestAnimationFrame(function () { attente = false; majLecture(); }); }, { passive: true });
    var nbv = $("#st-code"); if (nbv) nbv.textContent = "✔ " + Object.keys(CODE).filter(function (k) { return CODE[k].run !== false; }).length + " extraits vérifiés";
    render();
  }

  /* =====================================================================
     SCHÉMAS INTERACTIFS
     ===================================================================== */
  var WIDGETS = {};
  function svgEl(n, a) { var s = '<' + n; for (var k in a) s += " " + k + '="' + a[k] + '"'; return s; }

  /* ---- 1. pile d'appels pas à pas ---- */
  var PA_SRC = {
    fact: { titre: "factorielle(4)", code: "def factorielle(n):\n    if n == 0:\n        return 1\n    return n * factorielle(n - 1)\n\nfactorielle(4)" },
    fib: { titre: "fibonacci(4)", code: "def fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\n\nfibonacci(4)" },
    puis: { titre: "puissance(2, 10)", code: "def puissance(a, n):\n    if n == 0:\n        return 1\n    m = puissance(a, n // 2)\n    if n % 2 == 0:\n        return m * m\n    return a * m * m\n\npuissance(2, 10)" }
  };
  function traceAppels(type) {
    var S = [], st = [], nds = [], ndEtat = {};
    function snap(line, msg) {
      S.push({ line: line, msg: msg, st: st.map(function (f) { return { lab: f.lab, vars: f.vars.slice(), et: f.et, ret: f.ret, nd: f.nd }; }), nd: JSON.parse(JSON.stringify(ndEtat)) });
    }
    function entre(lab, vars, parent) {
      var id = nds.length; nds.push({ id: id, lab: lab, parent: parent, enf: [] }); if (parent !== null) nds[parent].enf.push(id);
      if (st.length) st[st.length - 1].et = "attente";
      var f = { lab: lab, vars: vars, et: "actif", ret: null, nd: id }; st.push(f); ndEtat[id] = { e: "actif" };
      Object.keys(ndEtat).forEach(function (k) { if (+k !== id && ndEtat[k].e === "actif") ndEtat[k].e = "attente"; });
      return f;
    }
    function sort(f, v) { f.ret = v; f.et = "renvoie"; ndEtat[f.nd] = { e: "fini", v: v }; }
    function reprend() { var p = st[st.length - 1]; if (p) { p.et = "actif"; ndEtat[p.nd].e = "actif"; } }
    if (type === "fact") {
      var fact = function (n, parent) {
        var f = entre("factorielle(" + n + ")", ["n = " + n], parent);
        snap(1, "Appel <b>factorielle(" + n + ")</b> : un nouveau cadre est <b>empilé</b>, avec sa propre variable n = " + n + ".");
        snap(2, "Test <b>n == 0</b> : " + (n === 0 ? "vrai." : "faux."));
        var r;
        if (n === 0) { r = 1; sort(f, 1); snap(3, "<b>Cas de base</b> : on renvoie 1 sans nouvel appel. La descente s’arrête, la remontée commence."); }
        else {
          snap(4, "Cas récursif : pour calculer " + n + " × factorielle(" + (n - 1) + "), il faut d’abord factorielle(" + (n - 1) + "). Ce cadre se met <b>en attente</b>.");
          var s = fact(n - 1, f.nd); reprend();
          snap(4, "factorielle(" + (n - 1) + ") a renvoyé " + s + " et son cadre a été <b>dépilé</b>. On reprend ici : " + n + " × " + s + " = " + n * s + ".");
          r = n * s; sort(f, r); snap(4, "<b>factorielle(" + n + ") renvoie " + r + "</b> à celui qui l’a appelée.");
        }
        st.pop(); return r;
      };
      var v = fact(4, null); snap(6, "La pile est vide : <b>factorielle(4) = " + v + "</b>. Il y a eu 5 appels, donc 5 cadres empilés au maximum.");
    } else if (type === "fib") {
      var fib = function (n, parent) {
        var f = entre("fibonacci(" + n + ")", ["n = " + n], parent);
        snap(1, "Appel <b>fibonacci(" + n + ")</b> : nouveau cadre empilé.");
        var r;
        if (n < 2) { r = n; sort(f, n); snap(3, "n < 2 : <b>cas de base</b>, on renvoie " + n + "."); }
        else {
          snap(4, "Il faut fibonacci(" + (n - 1) + ") <b>puis</b> fibonacci(" + (n - 2) + "). Python évalue d’abord l’appel de gauche.");
          var a = fib(n - 1, f.nd); reprend();
          f.vars = ["n = " + n, "gauche = " + a];
          snap(4, "fibonacci(" + (n - 1) + ") = " + a + ". Maintenant l’appel de droite : fibonacci(" + (n - 2) + ").");
          var b = fib(n - 2, f.nd); reprend();
          f.vars = ["n = " + n, "gauche = " + a, "droite = " + b];
          r = a + b; sort(f, r); snap(4, "fibonacci(" + n + ") renvoie " + a + " + " + b + " = <b>" + r + "</b>.");
        }
        st.pop(); return r;
      };
      var w = fib(4, null); snap(6, "Résultat : <b>fibonacci(4) = " + w + "</b> en 9 appels. Regarde l’arbre : fibonacci(2) a été calculé <b>deux fois</b>, fibonacci(1) trois fois. Pour n = 30, il faut 2 692 537 appels.");
    } else {
      var pu = function (a, n, parent) {
        var f = entre("puissance(" + a + ", " + n + ")", ["a = " + a, "n = " + n], parent);
        snap(1, "Appel <b>puissance(" + a + ", " + n + ")</b> : nouveau cadre.");
        snap(2, "Test n == 0 : " + (n === 0 ? "vrai." : "faux."));
        var r;
        if (n === 0) { r = 1; sort(f, 1); snap(3, "Cas de base : a⁰ = 1."); }
        else {
          snap(4, "On calcule m = a^(n // 2) = puissance(" + a + ", " + Math.floor(n / 2) + ") : l’exposant est <b>divisé par 2</b>.");
          var m = pu(a, Math.floor(n / 2), f.nd); reprend();
          f.vars = ["a = " + a, "n = " + n, "m = " + m];
          snap(4, "m = " + m + ". Test de parité de n = " + n + ".");
          if (n % 2 === 0) { r = m * m; snap(5, n + " est pair : a^" + n + " = m × m."); sort(f, r); snap(6, "Renvoie " + m + " × " + m + " = <b>" + r + "</b>."); }
          else { r = a * m * m; snap(5, n + " est impair : a^" + n + " = a × m × m."); sort(f, r); snap(7, "Renvoie " + a + " × " + m + " × " + m + " = <b>" + r + "</b>."); }
        }
        st.pop(); return r;
      };
      var z = pu(2, 10, null); snap(9, "Résultat : <b>2¹⁰ = " + z + "</b> en seulement 5 appels (10 → 5 → 2 → 1 → 0). Avec la méthode naïve, il en faudrait 11.");
    }
    return { S: S, nds: nds };
  }
  function layoutArbre(nds) {
    var x = 0, pos = {};
    (function place(id, d) {
      var n = nds[id];
      if (!n.enf.length) { pos[id] = { x: x++, y: d }; return; }
      n.enf.forEach(function (e) { place(e, d + 1); });
      pos[id] = { x: (pos[n.enf[0]].x + pos[n.enf[n.enf.length - 1]].x) / 2, y: d };
    })(0, 0);
    return { pos: pos, larg: x };
  }
  WIDGETS["pile-appels"] = function (z, opt) {
    var type = opt || "fact", T, i = 0, jeu = null;
    z.innerHTML = '<div class="w"><div class="tete"><span class="lab">pile d’appels pas à pas</span></div><div class="corps"><div class="choix-w">' +
      ["fact", "fib", "puis"].map(function (k) { return '<button type="button" data-t="' + k + '">' + PA_SRC[k].titre + "</button>"; }).join("") +
      '</div><div class="pa"><div class="zc"></div><div><div class="titre-pile">pile d’exécution (le sommet est en haut)</div><div class="pile"></div></div></div><div class="arbre"></div><div class="msg" aria-live="polite"></div>' +
      '<div class="cmd"><button class="btn petit" type="button" data-c="debut" aria-label="Revenir au début">' + ic("debut") + '</button><button class="btn petit" type="button" data-c="prec">' + ic("retour") + 'pas</button><button class="btn petit prim" type="button" data-c="suiv">pas' + ic("suite") + '</button><button class="btn petit" type="button" data-c="jeu">' + ic("lecture") + '<span>lecture</span></button><span class="cpt"></span></div></div></div>';
    function charger(t) {
      type = t; T = traceAppels(t); i = 0; stop();
      $$(".choix-w button", z).forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-t") === t); });
      $(".zc", z).innerHTML = '<div class="code zebre"><div class="tete"><span class="f">' + PA_SRC[t].titre.split("(")[0] + '.py</span></div><pre><code>' + lignes(hlPy(PA_SRC[t].code)) + "</code></pre></div>";
      dessine(true);
    }
    function dessine(neuf) {
      var s = T.S[i];
      $$(".zc .l", z).forEach(function (l, k) { l.classList.toggle("vise", k + 1 === s.line); });
      var p = $(".pile", z), avant = p.children.length;
      p.innerHTML = s.st.length ? s.st.map(function (f, k) {
        return '<div class="cadre-pile ' + (f.et === "actif" ? "actif" : f.et === "renvoie" ? "renvoie" : "") + (k >= avant && !neuf ? " neuf" : "") + '"><div class="nm">' + esc(f.lab) + '</div><div class="vr">' + f.vars.map(esc).join(" · ") + (f.ret !== null ? ' · <span class="rv">renvoie ' + f.ret + "</span>" : f.et === "attente" ? " · en attente…" : "") + "</div></div>";
      }).join("") : '<div class="vide">pile vide</div>';
      if (type === "fib") {
        var L = layoutArbre(T.nds), W = 74, H = 54, larg = Math.max(L.larg * W, 300);
        var svg = '<svg viewBox="0 0 ' + larg + " " + (4 * H + 40) + '" role="img" aria-label="Arbre des appels de fibonacci(4)">';
        var dx = (larg - L.larg * W) / 2;
        T.nds.forEach(function (n) { if (n.parent !== null) { var a = L.pos[n.parent], b = L.pos[n.id]; var vu = s.nd[n.id]; svg += '<line class="' + (vu ? "vu" : "") + '" x1="' + (dx + a.x * W + W / 2) + '" y1="' + (a.y * H + 20 + 26) + '" x2="' + (dx + b.x * W + W / 2) + '" y2="' + (b.y * H + 20) + '"/>'; } });
        T.nds.forEach(function (n) {
          var p0 = L.pos[n.id], e = s.nd[n.id], cl = e ? (e.e === "fini" ? "fini" : e.e === "actif" ? "actif" : "attente") : "cache";
          var x = dx + p0.x * W + 4, y = p0.y * H + 20;
          svg += '<g class="nd ' + cl + '"><rect x="' + x + '" y="' + y + '" width="' + (W - 8) + '" height="26" rx="6"/><text x="' + (x + (W - 8) / 2) + '" y="' + (y + 17) + '" text-anchor="middle">fib(' + n.lab.replace(/\D/g, "") + ")" + (e && e.e === "fini" ? "=" + e.v : "") + "</text></g>";
        });
        $(".arbre", z).innerHTML = '<div class="titre-pile" style="margin-top:10px">arbre des appels</div><div class="arbre-appels">' + svg + "</svg></div>";
      } else $(".arbre", z).innerHTML = "";
      var m = $(".msg", z); m.innerHTML = s.msg;
      if (!neuf && MO()) { m.classList.remove("neuf"); void m.offsetWidth; m.classList.add("neuf"); }
      $(".cpt", z).textContent = "étape " + (i + 1) + " / " + T.S.length;
      $('[data-c="suiv"]', z).disabled = i >= T.S.length - 1; $('[data-c="prec"]', z).disabled = i === 0; $('[data-c="debut"]', z).disabled = i === 0;
    }
    function stop() { if (jeu) { clearInterval(jeu); jeu = null; } var b = $('[data-c="jeu"]', z); if (b) b.innerHTML = ic("lecture") + "<span>lecture</span>"; }
    $$(".choix-w button", z).forEach(function (b) { b.addEventListener("click", function () { charger(b.getAttribute("data-t")); }); });
    $$("[data-c]", z).forEach(function (b) {
      b.addEventListener("click", function () {
        var c = b.getAttribute("data-c");
        if (c === "debut") { stop(); i = 0; dessine(true); }
        else if (c === "prec") { stop(); if (i > 0) { i--; dessine(true); } }
        else if (c === "suiv") { stop(); if (i < T.S.length - 1) { i++; dessine(false); } }
        else if (c === "jeu") {
          if (jeu) { stop(); return; }
          if (i >= T.S.length - 1) i = 0;
          b.innerHTML = ic("pause") + "<span>pause</span>";
          jeu = setInterval(function () { if (!document.body.contains(z)) { stop(); return; } if (i < T.S.length - 1) { i++; dessine(false); } else stop(); }, 1300);
        }
      });
    });
    charger(type);
  };

  /* ---- 2. pile et file manipulables ---- */
  WIDGETS["pile-file"] = function (z, opt) {
    var mode = opt || "pile", data = [], entree = [], sortie = [], vue2 = false, cpt = 1, journal = [];
    z.innerHTML = '<div class="w"><div class="tete"><span class="lab">pile et file à manipuler</span></div><div class="corps"><div class="choix-w"><button type="button" data-m="pile">pile (LIFO)</button><button type="button" data-m="file">file (FIFO)</button><button type="button" data-m="file2">file avec deux piles</button></div>' +
      '<div class="pf"><div><div class="scene-pf"></div></div><div><div class="titre-pile">ce que tu écrirais en Python</div><div class="journal" aria-live="polite"></div></div></div>' +
      '<div class="cmd" style="margin-top:10px"><label class="sr" for="pf-v">valeur</label><input type="text" id="pf-v" maxlength="4" autocomplete="off"><button class="btn petit prim" type="button" data-o="in"></button><button class="btn petit" type="button" data-o="out"></button><button class="btn petit" type="button" data-o="vide">est_vide()</button><button class="btn petit" type="button" data-o="raz">vider</button></div><div class="msg"></div></div></div>';
    var inp = $("input", z);
    function nom() { return mode === "pile" ? "p" : "f"; }
    function log(cmd, rep, err) { journal.push('<span class="p">&gt;&gt;&gt;</span> ' + esc(cmd)); if (rep !== undefined) journal.push('<span class="' + (err ? "e" : "r") + '">' + esc(rep) + "</span>"); var j = $(".journal", z); j.innerHTML = journal.join("\n"); j.scrollTop = j.scrollHeight; }
    function boutons() {
      $('[data-o="in"]', z).textContent = mode === "pile" ? "empiler" : "enfiler";
      $('[data-o="out"]', z).textContent = mode === "pile" ? "dépiler" : "défiler";
      $$(".choix-w button", z).forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-m") === (mode === "file" && vue2 ? "file2" : mode)); });
      inp.value = String(cpt);
    }
    function tube(t, cl, neuf, haut) {
      if (!t.length) return '<div class="tube ' + cl + '"><div class="repere" style="margin:auto">vide</div></div>';
      return '<div class="tube ' + cl + '">' + t.map(function (v, k) { return '<div class="elt' + (k === t.length - 1 && haut ? " haut" : "") + (neuf && k === t.length - 1 ? " entre" : "") + '">' + esc(v) + "</div>"; }).join("") + "</div>";
    }
    function dessine(neuf) {
      var s = $(".scene-pf", z), h;
      if (mode === "pile") h = '<div><div class="repere">↓ empiler · ↑ dépiler (sommet)</div>' + tube(data, "", neuf, true) + '<div class="repere">fond</div></div>';
      else {
        h = '<div style="width:100%"><div class="repere" style="display:flex;justify-content:space-between"><span>← défiler (tête)</span><span>enfiler (queue) ←</span></div>' + tube(data, "file", neuf, false) + "</div>";
        if (vue2) h = '<div style="width:100%">' + h + '<div style="display:flex;gap:24px;justify-content:center;margin-top:12px"><div><div class="repere">pile entree</div>' + tube(entree, "", false, true).replace('class="tube ', 'style="min-height:130px;width:90px" class="tube ') + '</div><div><div class="repere">pile sortie</div>' + tube(sortie, "", false, true).replace('class="tube ', 'style="min-height:130px;width:90px" class="tube ') + "</div></div></div>";
      }
      s.innerHTML = h;
    }
    function msg(t) { $(".msg", z).innerHTML = t; }
    function changer(m) {
      vue2 = m === "file2"; mode = m === "pile" ? "pile" : "file"; data = []; entree = []; sortie = []; cpt = 1; journal = [];
      log(mode === "pile" ? "p = Pile()" : vue2 ? "f = File()   # deux piles : entree et sortie" : "f = File()");
      msg(mode === "pile" ? "Une <b>pile</b> : on ajoute et on retire <b>du même côté</b>, le sommet. Le dernier entré est le premier sorti (LIFO)." : vue2 ? "Une file réalisée avec <b>deux piles</b> : on empile dans <code>entree</code> ; pour défiler, on dépile <code>sortie</code>, et si elle est vide on y verse d’abord toute la pile <code>entree</code>, ce qui remet les éléments dans le bon ordre." : "Une <b>file</b> : on ajoute à la queue, on retire à la tête. Le premier entré est le premier sorti (FIFO).");
      boutons(); dessine(false);
    }
    $$(".choix-w button", z).forEach(function (b) { b.addEventListener("click", function () { changer(b.getAttribute("data-m")); }); });
    $$("[data-o]", z).forEach(function (b) {
      b.addEventListener("click", function () {
        var o = b.getAttribute("data-o");
        if (o === "in") {
          var v = inp.value.trim() || String(cpt);
          if (data.length >= 7) { msg("Assez pour l’affichage : 7 éléments au plus ici (une vraie pile n’a pas cette limite)."); return; }
          data.push(v); if (vue2) entree.push(v); cpt++;
          log(nom() + (mode === "pile" ? ".empiler(" : ".enfiler(") + (isNaN(+v) ? '"' + v + '"' : v) + ")");
          msg(mode === "pile" ? "<b>" + esc(v) + "</b> est posé au sommet." : "<b>" + esc(v) + "</b> rejoint la queue de la file." + (vue2 ? " (empilé dans <code>entree</code>)" : ""));
          inp.value = String(cpt); dessine(true);
        } else if (o === "out") {
          if (!data.length) { log(nom() + (mode === "pile" ? ".depiler()" : ".defiler()"), "IndexError: " + (mode === "pile" ? "pile vide" : "file vide"), true); msg("Erreur : on ne peut pas retirer un élément d’une structure vide. Teste <code>est_vide()</code> avant."); return; }
          var r;
          if (mode === "pile") { r = data.pop(); msg("On retire le <b>sommet</b> : " + esc(r) + ", le dernier arrivé."); }
          else {
            r = data.shift();
            if (vue2) {
              var tr = "";
              if (!sortie.length) { var n = entree.length; while (entree.length) sortie.push(entree.pop()); tr = " La pile <code>sortie</code> était vide : on y a d’abord versé les " + n + " éléments de <code>entree</code> (leur ordre s’inverse)."; }
              sortie.pop(); msg("On dépile <code>sortie</code> : <b>" + esc(r) + "</b>, le premier arrivé." + tr);
            } else msg("On retire la <b>tête</b> : " + esc(r) + ", le premier arrivé.");
          }
          log(nom() + (mode === "pile" ? ".depiler()" : ".defiler()"), isNaN(+r) ? "'" + r + "'" : r); dessine(false);
        } else if (o === "vide") { log(nom() + ".est_vide()", data.length ? "False" : "True"); msg(data.length ? "La structure contient " + data.length + " élément(s)." : "Elle est vide."); }
        else changer(vue2 ? "file2" : mode);
      });
    });
    changer(mode);
  };

  /* ---- 3. liste chaînée qui se construit ---- */
  WIDGETS["liste-chainee"] = function (z) {
    var vals = [3, 5, 8], visite = -1, neuf = -1, occupe = false, cpt = 0;
    var CODES = {
      tete: "def ajouter_tete(self, v):\n    self.tete = Maillon(v, self.tete)",
      queue: "def ajouter_queue(self, v):\n    if self.tete is None:\n        self.tete = Maillon(v)\n    else:\n        m = self.tete\n        while m.suivant is not None:\n            m = m.suivant\n        m.suivant = Maillon(v)",
      suppr: "def supprimer_tete(self):\n    v = self.tete.valeur\n    self.tete = self.tete.suivant\n    return v",
      long: "def longueur(self):\n    n = 0\n    m = self.tete\n    while m is not None:\n        n = n + 1\n        m = m.suivant\n    return n"
    };
    z.innerHTML = '<div class="w"><div class="tete"><span class="lab">liste chaînée qui se construit</span></div><div class="corps"><div class="lc"></div>' +
      '<div class="cmd" style="margin-top:10px"><label class="sr" for="lc-v">valeur</label><input type="text" id="lc-v" maxlength="3" value="1" autocomplete="off"><button class="btn petit prim" type="button" data-o="tete">ajouter en tête</button><button class="btn petit" type="button" data-o="queue">ajouter en queue</button><button class="btn petit" type="button" data-o="suppr">supprimer la tête</button><button class="btn petit" type="button" data-o="long">longueur()</button><button class="btn petit" type="button" data-o="raz">recommencer</button></div>' +
      '<div class="msg" aria-live="polite"></div><div class="zc"></div></div></div>';
    function dessine() {
      var W = 104, X0 = 20, Y = 44, n = vals.length, larg = Math.max(X0 + n * W + 90, 330);
      var s = '<svg viewBox="0 0 ' + larg + ' 100" width="' + larg + '" role="img" aria-label="Liste chaînée de ' + n + ' maillons">';
      s += '<text class="tete-l" x="' + X0 + '" y="18">tete</text><path class="fl" d="M' + (X0 + 14) + " 24 L" + (X0 + 14) + " " + (Y - 4) + '"/><path class="pt" d="M' + (X0 + 9) + " " + (Y - 9) + " L" + (X0 + 14) + " " + (Y - 1) + " L" + (X0 + 19) + " " + (Y - 9) + 'z"/>';
      vals.forEach(function (v, k) {
        var x = X0 + k * W;
        s += '<g class="mai' + (k === visite ? " visite" : "") + (k === neuf ? " neuf" : "") + '"><rect x="' + x + '" y="' + Y + '" width="72" height="36" rx="6"/><line class="sep" x1="' + (x + 44) + '" y1="' + Y + '" x2="' + (x + 44) + '" y2="' + (Y + 36) + '"/><text x="' + (x + 22) + '" y="' + (Y + 23) + '" text-anchor="middle">' + esc(v) + '</text><circle class="pt" cx="' + (x + 58) + '" cy="' + (Y + 18) + '" r="4"/></g>';
        var x2 = x + W;
        s += '<path class="fl" d="M' + (x + 62) + " " + (Y + 18) + " L" + (x2 - 6) + " " + (Y + 18) + '"/><path class="pt" d="M' + (x2 - 12) + " " + (Y + 13) + " L" + (x2 - 4) + " " + (Y + 18) + " L" + (x2 - 12) + " " + (Y + 23) + 'z"/>';
      });
      s += '<text class="none" x="' + (X0 + n * W) + '" y="' + (Y + 23) + '">None</text></svg>';
      if (!n) s = s.replace("M" + (X0 + 14) + " 24 L" + (X0 + 14) + " " + (Y - 4), "M" + (X0 + 14) + " 24 L" + (X0 + 14) + " " + (Y - 4));
      $(".lc", z).innerHTML = s;
    }
    function code(k) { $(".zc", z).innerHTML = '<div class="code zebre"><div class="tete"><span class="f">méthode de ListeChainee</span></div><pre><code>' + lignes(hlPy(CODES[k])) + "</code></pre></div>"; }
    function msg(t) { $(".msg", z).innerHTML = t; }
    function parcours(jusqua, fin) {
      if (!MO() || jusqua < 0) { visite = -1; fin(); return; }
      occupe = true; var k = 0;
      (function pas() {
        visite = k; dessine();
        if (k >= jusqua) { setTimeout(function () { visite = -1; occupe = false; fin(); }, 380); return; }
        k++; setTimeout(pas, 380);
      })();
    }
    $$("[data-o]", z).forEach(function (b) {
      b.addEventListener("click", function () {
        if (occupe) return;
        var o = b.getAttribute("data-o"), inp = $("input", z), v = inp.value.trim() || String(++cpt);
        neuf = -1;
        if (o === "tete") {
          if (vals.length >= 8) { msg("8 maillons au plus pour l’affichage."); return; }
          vals.unshift(v); neuf = 0; code("tete"); dessine();
          msg("Nouveau maillon <b>" + esc(v) + "</b> dont le suivant est l’ancienne tête. <b>Aucun maillon parcouru</b> : coût constant, quelle que soit la longueur.");
        } else if (o === "queue") {
          if (vals.length >= 8) { msg("8 maillons au plus pour l’affichage."); return; }
          code("queue");
          var n = vals.length;
          parcours(n - 1, function () { vals.push(v); neuf = vals.length - 1; dessine(); msg("Pour atteindre le dernier maillon, il a fallu <b>parcourir les " + n + " maillons</b> depuis la tête : coût proportionnel à la longueur."); });
        } else if (o === "suppr") {
          code("suppr");
          if (!vals.length) { msg("<b>AttributeError</b> : la liste est vide, <code>self.tete</code> vaut None et None n’a pas d’attribut <code>valeur</code>."); return; }
          var r = vals.shift(); dessine(); msg("On renvoie <b>" + esc(r) + "</b> et la tête devient le maillon suivant. Coût constant. Le maillon retiré n’est plus référencé : Python libère sa mémoire.");
        } else if (o === "long") {
          code("long");
          var m = vals.length;
          parcours(m - 1, function () { dessine(); msg("<code>longueur()</code> renvoie <b>" + m + "</b> : on a suivi les liens maillon par maillon jusqu’à None (" + m + " pas)."); });
        } else { vals = [3, 5, 8]; cpt = 0; dessine(); msg("Liste de départ : 3 → 5 → 8 → None."); $(".zc", z).innerHTML = ""; }
        inp.value = String(isNaN(+v) ? 1 : +v + 1);
      });
    });
    dessine(); msg("Chaque maillon contient une <b>valeur</b> et une <b>référence</b> vers le maillon suivant ; le dernier pointe vers <code>None</code>. Ajoute, retire, mesure : regarde combien de maillons sont parcourus.");
  };

  /* ---- 4. diagramme de classe et objets en mémoire ---- */
  WIDGETS.uml = function (z) {
    var ETAPES = [
      { l: "class Compte: ...", m: "La <b>classe</b> est un plan : elle décrit les attributs (données) et les méthodes (actions). À ce stade, <b>aucun objet n’existe</b>." },
      { l: 'c1 = Compte("Ada", 100)', m: "<b>Instanciation</b> : Python fabrique un objet, appelle <code>__init__</code> avec <code>self</code> = ce nouvel objet, puis range dans <code>c1</code> une <b>référence</b> vers lui." },
      { l: 'c2 = Compte("Alan")', m: "Un second objet, <b>indépendant</b> du premier. Le solde n’a pas été donné : la valeur par défaut 0 s’applique." },
      { l: "c1.deposer(50)", m: "Appel de méthode : <code>self</code> reçoit l’objet désigné par <code>c1</code>. Seul cet objet est modifié." },
      { l: "c3 = c1", m: "<b>Aucun objet n’est copié</b> : <code>c3</code> est un deuxième nom pour le même objet (un <i>alias</i>). <code>c3 is c1</code> vaut True." },
      { l: "c3.retirer(30)", m: "On passe par <code>c3</code>… mais l’objet est celui de <code>c1</code> : <code>c1.solde</code> vaut désormais 120. C’est la <b>mutation partagée</b>." },
      { l: "print(c1.solde, c2.solde)", m: "Affiche <code>120 0</code>." }
    ];
    var k = 0;
    z.innerHTML = '<div class="w"><div class="tete"><span class="lab">classe, objets et références</span></div><div class="corps uml"><div class="svgz"></div><div class="code"><div class="sortie" style="border-top:0"><div class="tete"><span class="f">ligne exécutée</span></div><pre class="ligne-ex"></pre></div></div><div class="msg" aria-live="polite"></div><div class="cmd"><button class="btn petit" type="button" data-c="raz">' + ic("debut") + 'recommencer</button><button class="btn petit prim" type="button" data-c="suiv">ligne suivante' + ic("suite") + '</button><span class="cpt"></span></div></div></div>';
    function fleche(x, y, cl) { return '<path class="' + cl + '" d="M' + (x - 5) + " " + (y + 8) + " L" + x + " " + y + " L" + (x + 5) + " " + (y + 8) + 'z"/>'; }
    function dessine(nouv) {
      var et = $(".svgz", z).clientWidth < 600;
      var G = et ? { W: 400, H: 420, cx: 75, o1: [150, 200], o2: [150, 306], ow: 222, v1: [10, 230], v2: [10, 328], v3: [10, 180], leg: 408 }
                 : { W: 640, H: 380, cx: 200, o1: [190, 214], o2: [420, 214], ow: 200, v1: [18, 226], v2: [18, 276], v3: [18, 176], leg: 365 };
      var s = '<svg viewBox="0 0 ' + G.W + " " + G.H + '" role="img" aria-label="Diagramme de la classe Compte et des objets créés">';
      var X = G.cx;
      s += '<g class="cl"><rect x="' + X + '" y="8" width="250" height="150" rx="4"/><rect class="bandeau" x="' + (X + 1) + '" y="9" width="248" height="26"/><text x="' + (X + 125) + '" y="27" text-anchor="middle" font-weight="700">Compte</text><line class="sep" x1="' + X + '" y1="35" x2="' + (X + 250) + '" y2="35"/>' +
        '<text x="' + (X + 12) + '" y="54">titulaire : str</text><text x="' + (X + 12) + '" y="72">solde : int</text><line class="sep" x1="' + X + '" y1="82" x2="' + (X + 250) + '" y2="82"/>' +
        '<text x="' + (X + 12) + '" y="101">__init__(titulaire, solde=0)</text><text x="' + (X + 12) + '" y="119">deposer(montant)</text><text x="' + (X + 12) + '" y="137">retirer(montant) : bool</text></g>';
      var s1 = k >= 5 ? 120 : k >= 3 ? 150 : 100;
      function objet(o, n, tit, sol, maj, neuf) {
        return '<g class="ob' + (neuf ? " neuf" : "") + '"><rect x="' + o[0] + '" y="' + o[1] + '" width="' + G.ow + '" height="74" rx="6"/><text class="titre" x="' + (o[0] + 10) + '" y="' + (o[1] + 20) + '">objet ' + n + ' : Compte</text><text x="' + (o[0] + 10) + '" y="' + (o[1] + 42) + '">titulaire = "' + tit + '"</text><text x="' + (o[0] + 10) + '" y="' + (o[1] + 62) + '" class="' + (maj ? "maj" : "") + '">solde = ' + sol + "</text></g>";
      }
      function nomv(v, t, neuf) { return '<g class="nomvar' + (neuf ? " neuf" : "") + '"><rect x="' + v[0] + '" y="' + v[1] + '" width="58" height="30" rx="5"/><text x="' + (v[0] + 29) + '" y="' + (v[1] + 20) + '" text-anchor="middle">' + t + "</text></g>"; }
      function ref(d, len, xe, ye) { return '<path class="lien ref trace" style="--len:' + len + '" d="' + d + '"/><path class="tete-ref" d="M' + (xe - 8) + " " + (ye - 5) + " L" + xe + " " + ye + " L" + (xe - 8) + " " + (ye + 5) + 'z"/>'; }
      if (k >= 1) {
        var ix = G.o1[0] + G.ow / 2;
        s += '<path class="lien inst trace" style="--len:60" d="M' + ix + " " + G.o1[1] + " L" + ix + ' 166"/>' + fleche(ix, 160, "tete-f");
        s += objet(G.o1, 1, "Ada", s1, nouv === 3 || nouv === 5, nouv === 1);
        var y1 = G.v1[1] + 15;
        s += nomv(G.v1, "c1", nouv === 1) + ref("M" + (G.v1[0] + 58) + " " + y1 + " L" + (G.o1[0] - 8) + " " + y1, 140, G.o1[0], y1);
      }
      if (k >= 2) {
        s += objet(G.o2, 2, "Alan", 0, false, nouv === 2);
        var y2 = G.v2[1] + 15;
        if (et) {
          var xr = G.o2[0] + G.ow, yr = G.o2[1] + 20;
          s += '<path class="lien inst trace" style="--len:300" d="M' + xr + " " + yr + " L" + (xr + 16) + " " + yr + " L" + (xr + 16) + " 100 L" + (X + 258) + ' 100"/><path class="tete-f" d="M' + (X + 258) + " 95 L" + (X + 250) + " 100 L" + (X + 258) + ' 105z"/>';
          s += nomv(G.v2, "c2", nouv === 2) + ref("M" + (G.v2[0] + 58) + " " + y2 + " L" + (G.o2[0] - 8) + " " + y2, 140, G.o2[0], y2);
        } else {
          s += '<path class="lien inst trace" style="--len:110" d="M520 214 L430 166"/>' + '<path class="tete-f" d="M427 172 L426 162 L435 165z"/>';
          s += nomv(G.v2, "c2", nouv === 2) + '<path class="lien ref trace" style="--len:560" d="M76 291 L100 291 L100 340 L520 340 L520 296"/>' + '<path class="tete-ref" d="M515 304 L520 296 L525 304z"/>';
        }
      }
      if (k >= 4) {
        var y3 = G.v3[1] + 15, ye = G.o1[1] + 14, xm = G.v3[0] + 58 + 40;
        s += nomv(G.v3, "c3", nouv === 4) + ref("M" + (G.v3[0] + 58) + " " + y3 + " L" + xm + " " + y3 + " L" + xm + " " + ye + " L" + (G.o1[0] - 8) + " " + ye, 220, G.o1[0], ye);
      }
      s += '<text x="10" y="' + G.leg + '" class="legende" style="font-size:11px;fill:var(--encre3)">' + (et ? "→ référence · - - → « est une instance de »" : "noms (variables)     → référence      - - → « est une instance de »") + "</text></svg>";
      $(".svgz", z).innerHTML = s;
      $(".ligne-ex", z).innerHTML = hlPy(ETAPES[k].l) + (k === 6 ? '\n<span class="muet">120 0</span>' : "");
      $(".msg", z).innerHTML = ETAPES[k].m;
      $(".cpt", z).textContent = "ligne " + (k + 1) + " / " + ETAPES.length;
      $('[data-c="suiv"]', z).disabled = k >= ETAPES.length - 1;
    }
    $$("[data-c]", z).forEach(function (b) { b.addEventListener("click", function () { if (b.getAttribute("data-c") === "raz") { k = 0; dessine(0); } else if (k < ETAPES.length - 1) { k++; dessine(k); } }); });
    dessine(0);
  };

  /* ---- lecteur commun des animations pas à pas ----
     lecteur(zone, { titre, sous, choix: [{k, t}], etapes: function (k) -> [{msg, ...}],
                     prepare: function (scene, k, etapes), dessine: function (scene, etape, i, etapes, saut), vitesse: ms })
     Chaque étape porte sa légende (msg, en HTML). « saut » vaut true quand on recule ou qu'on recharge :
     le dessin est alors instantané ; sinon il peut s'animer (sous html.mo). */
  function lecteur(z, o) {
    var etapes = [], i = 0, jeu = null, cle = o.choix ? o.choix[0].k : null;
    z.innerHTML = '<div class="w anim"><div class="tete"><span class="lab">' + esc(o.titre) + "</span>" + (o.sous ? '<span class="sous">' + o.sous + "</span>" : "") + '</div><div class="corps">' +
      (o.choix ? '<div class="choix-w">' + o.choix.map(function (c) { return '<button type="button" data-k="' + esc(c.k) + '">' + c.t + "</button>"; }).join("") + "</div>" : "") +
      '<div class="scene"></div><div class="msg" aria-live="polite"></div><div class="cmd"><button class="btn petit" type="button" data-c="debut" aria-label="Revenir au début">' + ic("debut") + '</button><button class="btn petit" type="button" data-c="prec" aria-label="Étape précédente">' + ic("retour") + '</button><button class="btn petit prim" type="button" data-c="suiv">étape' + ic("suite") + '</button><button class="btn petit" type="button" data-c="jeu">' + ic("lecture") + '<span>lecture</span></button><span class="cpt mono"></span></div></div></div>';
    var scene = $(".scene", z);
    function stop() { if (jeu) { clearInterval(jeu); jeu = null; } var b = $('[data-c="jeu"]', z); if (b) b.innerHTML = ic("lecture") + "<span>lecture</span>"; }
    function dessine(saut) {
      var e = etapes[i], n = etapes.length, plein = Math.round(10 * (i + 1) / n);
      o.dessine(scene, e, i, etapes, saut || !MO());
      var m = $(".msg", z); m.innerHTML = e.msg || "";
      if (!saut && MO()) { m.classList.remove("neuf"); void m.offsetWidth; m.classList.add("neuf"); }
      $(".cpt", z).textContent = "[" + "#".repeat(plein) + ".".repeat(10 - plein) + "] " + (i + 1) + "/" + n;
      $('[data-c="prec"]', z).disabled = i === 0; $('[data-c="debut"]', z).disabled = i === 0;
      $('[data-c="suiv"]', z).disabled = i === n - 1;
    }
    function charger(k) {
      cle = k; stop(); etapes = o.etapes(k); i = 0;
      $$(".choix-w button", z).forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-k") === String(k)); });
      if (o.prepare) o.prepare(scene, k, etapes);
      dessine(true);
    }
    $$(".choix-w button", z).forEach(function (b) { b.addEventListener("click", function () { charger(b.getAttribute("data-k")); }); });
    $$("[data-c]", z).forEach(function (b) {
      b.addEventListener("click", function () {
        var c = b.getAttribute("data-c");
        if (c === "debut") { stop(); i = 0; dessine(true); }
        else if (c === "prec") { stop(); if (i > 0) { i--; dessine(true); } }
        else if (c === "suiv") { stop(); if (i < etapes.length - 1) { i++; dessine(false); } }
        else if (jeu) stop();
        else {
          if (i >= etapes.length - 1) { i = 0; dessine(true); }
          b.innerHTML = ic("pause") + "<span>pause</span>";
          jeu = setInterval(function () { if (!document.body.contains(z)) { stop(); return; } if (i < etapes.length - 1) { i++; dessine(false); } else stop(); }, o.vitesse || 1400);
        }
      });
    });
    charger(cle);
    return { charger: charger };
  }
  /* ---- exécution pas à pas d'un extrait (trace réelle calculée par traces.py à la construction) ----
     [[w-trace|id1,id2]] : un bouton par extrait (champ « titreTrace » de l'extrait). */
  WIDGETS.trace = function (z, opt) {
    var ids = String(opt || "").split(",").filter(function (k) { return window.TRACES && TRACES[k]; });
    if (!ids.length) return;
    function lignesSrc(id) { return CODE[id].src.replace(/^\n+|\s+$/g, "").split("\n"); }
    function etapes(id) {
      var T = TRACES[id], src = lignesSrc(id), E = [], avant = null;
      T.etapes.forEach(function (e) {
        var msg;
        if (e.r !== undefined) msg = "<b>" + esc(e.f) + "()</b> se termine et renvoie <b>" + esc(e.r) + "</b> ; son cadre est dépilé.";
        else {
          var ch = [];
          if (avant) {
            var h = e.p[e.p.length - 1], ha = avant.p[avant.p.length - 1];
            if (e.p.length > avant.p.length) ch.push("appel de <b>" + esc(h.f) + "</b> : nouveau cadre");
            else Object.keys(h.v).forEach(function (k) { if (!ha || ha.f !== h.f || ha.v[k] !== h.v[k]) ch.push("<code>" + esc(k) + "</code> vaut " + esc(h.v[k])); });
          }
          msg = "Ligne " + e.l + " : <code>" + esc(src[e.l - 1].trim()) + "</code>" + (ch.length ? " · " + ch.join(", ") : "") + ".";
        }
        E.push({ l: e.l, p: e.p, o: e.o, msg: msg });
        avant = e;
      });
      var d = E[E.length - 1] || { l: 0, p: [], o: "" };
      E.push({ l: T.err ? d.l : 0, p: T.err ? d.p : [], o: T.o, err: T.err, msg: T.err ? "Le programme s’arrête sur une erreur : <b>" + esc(T.err) + "</b>." : "Fin du programme." });
      return E;
    }
    lecteur(z, {
      titre: "exécution pas à pas", sous: "trace réelle (Python)", vitesse: 1100,
      choix: ids.length > 1 ? ids.map(function (k) { return { k: k, t: CODE[k].titreTrace || CODE[k].fichier || k }; }) : null,
      etapes: function (k) { return etapes(k || ids[0]); },
      prepare: function (sc, k) {
        var id = k || ids[0];
        sc.innerHTML = '<div class="trace"><div class="code zebre"><div class="tete"><span class="f">' + esc(CODE[id].fichier || "programme.py") + '</span></div><pre><code>' + lignes(hlPy(CODE[id].src.replace(/^\n+|\s+$/g, ""))) + '</code></pre></div><div class="tr-cote"><div class="titre-pile">variables (pile d’appels, le plus récent en haut)</div><div class="tr-pile"></div><div class="titre-pile">sortie</div><pre class="tr-sortie"></pre></div></div>';
      },
      dessine: function (sc, e) {
        $$(".trace .l", sc).forEach(function (l, i) { l.classList.toggle("vise", i + 1 === e.l); });
        var v = $(".trace .l.vise", sc); if (v && v.scrollIntoView && sc.offsetParent) { var pre = v.closest("pre"); pre.scrollTop = v.offsetTop - pre.clientHeight / 2; }
        $(".tr-pile", sc).innerHTML = e.p.length ? e.p.slice().reverse().map(function (c, i) {
          var ks = Object.keys(c.v);
          return '<div class="cadre-pile' + (i === 0 ? " actif" : "") + '"><div class="nm">' + esc(c.f) + '</div><div class="vr">' + (ks.length ? ks.map(function (k) { return esc(k) + " = " + esc(c.v[k]); }).join("<br>") : "(aucune variable)") + "</div></div>";
        }).join("") : '<span class="repere">—</span>';
        $(".tr-sortie", sc).innerHTML = esc(e.o || "") + (e.err ? '<span class="err-t">' + esc(e.err) + "</span>" : "");
      }
    });
  };

  var OUTILS = { $: $, $$: $$, esc: esc, ic: ic, MO: MO, hlPy: hlPy, hlSql: hlSql, lignes: lignes, lecteur: lecteur, codeHTML: codeHTML };
  window.NSI_OUTILS = OUTILS;

  window.NSI = { render: render, codeHTML: codeHTML, chercher: function (q) { if (!INDEX) construireIndex(); return chercher(q); } };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
