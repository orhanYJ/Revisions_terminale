/* ===== Ligne rouge — moteur du site (navigation par adresse #…, rendu, QCM, cartes mémoire, frises, cartes, recherche) ===== */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var APP = $("#app");
  var ORDRE = [];
  THEMES.forEach(function (t) { if (t.statut === "redige") [t.intro].concat(t.axes, [t.otc]).forEach(function (b) { if (b.ch && CHAPS[b.ch]) ORDRE.push(b.ch); }); });
  var TH_RED = THEMES.filter(function (t) { return t.statut === "redige"; }).map(function (t) { return t.id; });
  var LETTRES = "ABCDEFGH";
  var COUL = { espace: "var(--acier)", mer: "#2F8F9C", chine: "var(--rouge)", guerre: "var(--encre)", paix: "var(--ok)", terro: "var(--rouge)", mo: "#C0841F" };

  /* typographie française : espaces fines avant ; : ! ? » et après « */
  function typo(s) {
    return String(s).replace(/ ([;:!?»])/g, " $1").replace(/« /g, "« ");
  }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function sans(s) { return String(s).replace(/<[^>]+>/g, ""); }
  function norm(s) { return sans(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[’']/g, " "); }
  function theme(id) { for (var i = 0; i < THEMES.length; i++) if (THEMES[i].id === id) return THEMES[i]; return null; }
  function ic(n, cl) { return '<svg class="ic ' + (cl || "") + '" aria-hidden="true"><use href="#i-' + n + '"/></svg>'; }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  var MO = function () { return document.documentElement.classList.contains("mo"); };
  /* relance l'animation d'arrivée d'un bloc dont le contenu change (légende d'animation, fiche d'un lieu, d'une date) */
  function rejouer(el) { if (!el || !MO()) return; el.classList.remove("maj"); void el.offsetWidth; el.classList.add("maj"); }

  /* ---------------- navigation latérale ---------------- */
  function construireNav() {
    var h = '<div class="nav-tete"><b>Ligne rouge</b><button class="btn-ic" id="nav-fermer" aria-label="Fermer le menu" style="width:44px;height:44px;border:0;background:none;cursor:pointer">' + ic("croix") + '</button></div>';
    h += '<h2>Salle de crise</h2><a href="#accueil" data-r="accueil">' + ic("radar") + 'Accueil et programme</a>';
    THEMES.forEach(function (t) {
      if (t.statut === "redige") {
        h += '<h2>Thème ' + t.n + '</h2><a href="#' + t.id + '" data-r="' + t.id + '">' + ic("th" + t.n) + '<span>' + typo(t.titre.split(" :")[0]) + '</span></a>';
        [t.intro].concat(t.axes, [t.otc]).forEach(function (b, k) {
          var lib = k === 0 ? "Introduction" : (k === 3 ? "Objet conclusif" : "Axe " + k);
          h += '<a class="sous" href="#' + b.ch + '" data-r="' + b.ch + '"><span class="num">' + (k === 0 ? "IN" : k === 3 ? "OC" : "A" + k) + '</span>' + lib + '</a>';
        });
      }
    });
    h += '<h2>À venir</h2>';
    THEMES.forEach(function (t) { if (t.statut !== "redige") h += '<a href="#' + t.id + '" data-r="' + t.id + '">' + ic("th" + t.n) + '<span>Thème ' + t.n + '</span><span class="bt">BIENTÔT</span></a>'; });
    h += '<h2>Préparer le bac</h2><a href="#epreuve" data-r="epreuve">' + ic("stylo") + 'L\'épreuve</a><a href="#entrainement" data-r="entrainement">' + ic("cible") + 'Entraînement</a><a href="#ressources" data-r="ressources">' + ic("livre") + 'Ressources</a>';
    $("#nav").innerHTML = h;
    $("#nav-fermer").addEventListener("click", fermerNav);
  }
  function ouvrirNav() { $("#nav").classList.add("ouvert"); $("#voile-nav").classList.add("on"); }
  function fermerNav() { $("#nav").classList.remove("ouvert"); $("#voile-nav").classList.remove("on"); }

  /* ---------------- vidéo du chapitre (hggsp/serie/<code>.html) ---------------- */
  function activerVideo() {
    var b = $(".video-btn"); if (!b) return;
    var boite = $(".video-c");
    b.addEventListener("click", function () {
      var ouvre = b.getAttribute("aria-expanded") !== "true";
      b.setAttribute("aria-expanded", ouvre ? "true" : "false");
      boite.hidden = !ouvre;
      if (ouvre && !boite.firstChild) boite.innerHTML = '<iframe src="serie/' + b.getAttribute("data-code") + '.html?embed=1" title="Vidéo du chapitre" allow="fullscreen; autoplay" allowfullscreen data-serie="' + b.getAttribute("data-code") + '"></iframe>';
      else if (!ouvre) { var fr = $("iframe", boite); try { fr.contentWindow.postMessage({ type: "serie-pause" }, "*"); } catch (e) {} }
    });
  }
  window.addEventListener("message", function (e) {
    var d = e.data || {};
    if (d.type === "serie-h" && d.h) $$("iframe[data-serie]").forEach(function (fr) { if (fr.contentWindow === e.source) fr.style.height = Math.ceil(d.h) + "px"; });
  });
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) $$("iframe[data-serie]").forEach(function (fr) { try { fr.contentWindow.postMessage({ type: "serie-pause" }, "*"); } catch (e) {} });
  });

  /* ---------------- routeur ---------------- */
  function route() {
    var h = decodeURIComponent(location.hash.slice(1)) || "accueil";
    var cible = null, onglet = null;
    if (h.indexOf("@") > 0) { cible = h.split("@")[1]; h = h.split("@")[0]; }
    if (h.indexOf(":") > 0) { onglet = h.split(":")[1]; h = h.split(":")[0]; }
    fermerNav();
    var base = h;
    if (cible && PAGE === h + ":" + (onglet || "")) { allerA(h, cible); return; }
    PAGE = h + ":" + (onglet || "");
    if (CHAPS[h]) pageChapitre(h);
    else if (theme(h)) { if (theme(h).statut === "redige") pageTheme(h, onglet); else pageBientot(h); }
    else if (h === "epreuve") pageEpreuve();
    else if (h === "ressources") pageRessources();
    else if (h === "entrainement") pageEntrainement();
    else { base = "accueil"; pageAccueil(); }
    $$("#nav a").forEach(function (a) { a.classList.toggle("actif", a.getAttribute("data-r") === base); });
    habiller(base);
    document.title = (base === "accueil" ? "" : (document.querySelector("h1") ? sans(document.querySelector("h1").textContent) + " · " : "")) + "Ligne rouge · HGGSP Terminale";
    if (cible) allerA(base, cible);
    else if (!onglet) window.scrollTo(0, 0);
  }
  var PAGE = "";
  /* habillage « salle de crise » : bandeau confidentiel, fil d'Ariane tapé au télétype */
  function habiller(base) {
    var p = $(".page", APP);
    if (!p) return;
    var code = base === "accueil" ? "INDEX" : base.toUpperCase().replace("-", " · ");
    var b = document.createElement("div");
    b.className = "conf";
    b.setAttribute("aria-hidden", "true");
    var txt = "CONFIDENTIEL ◆ DOSSIER " + code + " ◆ DIFFUSION RESTREINTE : CANDIDATS AU BAC ◆ HGGSP TERMINALE ◆ ";
    b.innerHTML = "<span>" + txt + txt + txt + "</span>";
    APP.insertBefore(b, p);
    var fil = $(".fil", p);
    if (fil && MO()) {
      var html = fil.innerHTML, plein = fil.textContent, i = 0;
      fil.textContent = "";
      var tic = setInterval(function () { i += 2; fil.textContent = plein.slice(0, i) + "▌"; if (i >= plein.length) { clearInterval(tic); fil.innerHTML = html; } }, 18);
    }
  }
  function allerA(base, cible) {
    var el = document.getElementById(base + "-" + cible);
    if (el) { setTimeout(function () { el.scrollIntoView({ behavior: MO() ? "smooth" : "auto", block: "start" }); if (el.classList.contains("idee")) { el.classList.remove("surligne"); void el.offsetWidth; el.classList.add("surligne"); } }, 60); }
  }

  /* ---------------- accueil ---------------- */
  function pageAccueil() {
    var h = '<div class="page large">';
    h += '<section class="une"><svg class="radar" viewBox="0 0 260 260" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="130" cy="130" r="40"/><circle cx="130" cy="130" r="80"/><circle cx="130" cy="130" r="120"/><path d="M130 0V260M0 130H260"/></g><g class="balai"><path d="M130 130L130 10A120 120 0 0 1 233 70Z" fill="currentColor" opacity=".35"/></g>' + [[178, 88], [92, 70], [206, 168], [64, 150], [150, 214], [110, 116]].map(function (p, i) { return '<circle class="blip" style="animation-delay:' + (i * 1) + 's" cx="' + p[0] + '" cy="' + p[1] + '" r="5" fill="#FF5B49"/>'; }).join("") + '</svg>';
    h += '<span class="classif">DOSSIER CLASSÉ · HGGSP · TERMINALE</span><h1>Ligne <i>rouge</i></h1>';
    h += '<p>' + typo("Histoire-géographie, géopolitique et sciences politiques : le programme de spécialité de Terminale, thème par thème, avec des cours rédigés, des frises et des cartes interactives, des sujets corrigés et de quoi t'entraîner.") + '</p></section>';
    h += '<div class="raccourcis"><a href="#t2">' + ic("th2") + 'Thème 2 (écrit chaque année)</a><a href="#t5">' + ic("th5") + 'Thème 5 (écrit chaque année)</a><a href="#epreuve">' + ic("stylo") + 'L\'épreuve</a><a href="#entrainement">' + ic("cible") + 'S\'entraîner</a><a href="#ressources">' + ic("livre") + 'Ressources</a></div>';
    h += '<div class="alerte"><b>Bac 2027 :</b> ' + typo("l'écrit porte sur les thèmes 2, 4, 5 et 6 (rotation fixée par la note de service du 11 septembre 2026). Les thèmes 1 et 3 ne sont pas à l'écrit en 2027, mais ils restent au programme, au Grand oral, et reviennent à l'écrit en 2028.") + '</div>';
    h += '<h2 class="sec"><span class="n">00</span>La carte du programme</h2><div class="programme">';
    THEMES.forEach(function (t) {
      var red = t.statut === "redige";
      h += '<div class="carte-p onglet dossier" data-onglet="Thème ' + t.n + ' · ' + t.h + '">';
      h += '<span class="tampon ' + (red ? "" : "gris") + '">' + (red ? "Rédigé" : "Bientôt") + '</span>';
      h += '<a class="tete" href="#' + t.id + '" style="text-decoration:none;color:inherit">' + ic("th" + t.n, "th") + '<div><h3>' + typo(t.titre) + '</h3><div class="ecr">Écrit 2027 : <b class="' + (t.ecrit27 ? "oui" : "non") + '">' + (t.ecrit27 ? "oui" : "non") + '</b></div></div></a>';
      h += '<div class="puces">';
      [t.intro].concat(t.axes, [t.otc]).forEach(function (b, k) {
        var lib = k === 0 ? "Introduction" : (k === 3 ? "Objet conclusif" : "Axe " + k);
        h += red ? '<a href="#' + b.ch + '">' + lib + '</a>' : '<span>' + lib + '</span>';
      });
      h += red ? '<a href="#' + t.id + '" style="border-color:var(--rouge)">Dossier : frise, cartes, sujets</a>' : '<a href="#' + t.id + '">Voir les jalons</a>';
      h += '</div></div>';
    });
    h += '</div>';
    h += '<h2 class="sec"><span class="n">01</span>Comment utiliser ce site</h2><div class="carte-p"><ol class="etapes">';
    h += '<li><b>Lis l\'essentiel, puis le cours</b>' + typo("Chaque idée porte un exemple daté et chiffré : c'est lui qui fera la différence dans ta copie.") + '</li>';
    h += '<li><b>Teste-toi tout de suite</b>' + typo("QCM et cartes mémoire en bas de chaque chapitre ; une erreur renvoie au paragraphe à revoir.") + '</li>';
    h += '<li><b>Entraîne-toi sur des sujets</b>' + typo("Chaque dossier de thème contient une dissertation et une étude critique corrigées, avec la méthode.") + '</li>';
    h += '<li><b>Imprime les fiches « À retenir »</b>' + typo("Une page par chapitre, pour réviser sans écran.") + '</li></ol></div>';
    h += '</div>';
    APP.innerHTML = h;
  }

  /* ---------------- page « bientôt » ---------------- */
  function structureHTML(t, liens) {
    var h = '<div class="structure">';
    var blocs = [["Introduction", t.intro]].concat(t.axes.map(function (a, i) { return ["Axe " + (i + 1), a]; }), [["Objet de travail conclusif", t.otc]]);
    blocs.forEach(function (b) {
      h += '<div class="bloc"><h4><span class="etiq">' + b[0] + '</span>' + (liens && b[1].ch ? '<a href="#' + b[1].ch + '">' + typo(b[1].t) + '</a>' : typo(b[1].t)) + '</h4><ul>';
      b[1].j.forEach(function (j) { h += '<li>' + typo(j) + '</li>'; });
      h += '</ul></div>';
    });
    return h + '</div>';
  }
  function pageBientot(id) {
    var t = theme(id);
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · Thème ' + t.n + '</div>';
    h += '<h1 class="titre">' + typo(t.titre) + '<span class="ligne-rouge"></span></h1>';
    h += '<div class="rangee" style="margin:6px 0 14px"><span class="tampon gris">Bientôt</span><span class="tampon ' + (t.ecrit27 ? "" : "gris") + '">' + (t.ecrit27 ? "Écrit 2027" : "Hors écrit 2027") + '</span></div>';
    h += '<div class="alerte acier">' + typo("Le cours de ce thème sera rédigé au fil de l'année. En attendant, voici ce que dit le programme officiel : ce sont les jalons que ton professeur doit traiter, et les mots exacts à connaître.") + '</div>';
    h += '<div class="carte-p onglet" data-onglet="Objectif du thème"><p>' + typo(t.obj) + '</p><p style="font:600 14px var(--sans);margin:0">' + typo(t.ecrit) + '</p></div>';
    h += '<h2 class="sec"><span class="n">01</span>Structure officielle (' + t.h + ')</h2>' + structureHTML(t, false);
    h += '<h2 class="sec"><span class="n">02</span>Notions à maîtriser</h2><div class="puces">' + t.notions.map(function (n) { return '<span>' + typo(n) + '</span>'; }).join("") + '</div>';
    h += '<p style="font:13px var(--sans);color:var(--encre2);margin-top:8px">Notions liées aux jalons du programme, à définir avec précision dans tes copies.</p></div>';
    APP.innerHTML = h;
  }

  /* ---------------- chapitre ---------------- */
  function pageChapitre(id) {
    var c = CHAPS[id], t = theme(c.th);
    var i = ORDRE.indexOf(id);
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · <a href="#' + t.id + '">Thème ' + t.n + '</a> · ' + c.code.split("· ")[1] + '</div>';
    h += '<h1 class="titre">' + typo(c.t) + '<span class="ligne-rouge"></span></h1>';
    h += '<div class="rangee no-print" style="margin:4px 0 10px"><span class="tampon">Rédigé</span><span class="tampon ' + (t.ecrit27 ? "" : "gris") + '">' + (t.ecrit27 ? "Écrit 2027" : "Hors écrit 2027") + '</span></div>';
    h += '<div class="carte-p onglet essentiel note-s" data-onglet="Note de synthèse"><dl class="memo"><dt>Objet</dt><dd>' + typo(c.t) + '</dd><dt>Réf.</dt><dd>' + c.code + '</dd><dt>Classement</dt><dd><b>L\'essentiel en 5 lignes</b></dd></dl><ol>' + c.ess.map(function (e) { return '<li>' + typo(e) + '</li>'; }).join("") + '</ol></div>';
    var vid = typeof VIDEOS !== "undefined" && VIDEOS[id];
    if (vid && (vid.dispo || /[?&]video\b/.test(location.search))) {
      h += '<div class="video-b no-print"><button class="video-btn" aria-expanded="false" data-code="' + vid.code + '"><span class="vb-ic">' + ic("lire") + '</span><span class="vb-t"><b>Vidéo du chapitre</b><small>Le chapitre en ' + vid.min + ' min · cartes animées, dissertation et étude critique corrigées</small></span></button><div class="video-c" hidden></div></div>';
    }
    h += '<details class="pli attendu no-print"><summary>Ce que le programme attend</summary><div class="corps"><ul>' + c.att.map(function (e) { return '<li>' + typo(e) + '</li>'; }).join("") + '</ul></div></details>';
    h += '<nav class="sommaire no-print" aria-label="Sommaire">' + c.secs.map(function (s, k) { return '<a href="#' + id + '@s' + (k + 1) + '">' + (k + 1) + '. ' + typo(s.t) + '</a>'; }).join("") + '<a href="#' + id + '@qcm">QCM</a><a href="#' + id + '@fiche">À retenir</a></nav>';
    c.secs.forEach(function (s, k) {
      h += '<h2 class="sec" id="' + id + '-s' + (k + 1) + '"><span class="n">' + String(k + 1).padStart(2, "0") + '</span>' + typo(s.t) + '</h2>';
      h += '<div class="carte-p">';
      s.idees.forEach(function (d, j) {
        h += '<div class="idee" id="' + id + '-' + (k + 1) + '-' + (j + 1) + '"><span class="num">§ ' + (k + 1) + '.' + (j + 1) + '</span><h3>' + typo(d.t) + '</h3><div>' + typo(d.h) + '</div>' + (d.ex ? '<div class="ex">' + typo(d.ex) + '</div>' : "") + '</div>';
      });
      (s.plis || []).forEach(function (p) { h += '<details class="pli"><summary>' + typo(p.t) + '</summary><div class="corps">' + typo(p.h) + '</div></details>'; });
      h += '</div>';
      if (s.viz) h += viz(s.viz, id + "-v" + k);
    });
    h += '<h2 class="sec"><span class="n">!!</span>Pièges et erreurs fréquentes</h2><div class="carte-p pieges"><ul>' + c.pieges.map(function (p) { return '<li>' + typo(p) + '</li>'; }).join("") + '</ul></div>';
    h += '<div class="retenir-bloc" id="' + id + '-fiche"><h2 class="sec"><span class="n">★</span>À retenir</h2><div class="carte-p onglet retenir" data-onglet="Fiche · ' + c.code + '"><p style="font:700 15px var(--sans);margin:0 0 6px">' + typo(c.t) + '</p><table>' + c.retenir.map(function (r) { return '<tr><th>' + typo(r[0]) + '</th><td>' + typo(r[1]) + '</td></tr>'; }).join("") + '</table></div>';
    h += '<div class="rangee no-print"><button class="btn" id="imprimer">' + ic("print") + 'Imprimer la fiche</button><button class="btn" id="caviarder" aria-pressed="false">' + ic("oeil") + '<span>Caviarder pour réviser</span></button></div></div>';
    h += '<h2 class="sec" id="' + id + '-qcm"><span class="n">?</span>S\'entraîner</h2><div class="onglets no-print" role="tablist"><button role="tab" aria-selected="true" data-o="qcm">QCM (' + c.qcm.length + ' questions)</button><button role="tab" aria-selected="false" data-o="fc">Cartes mémoire (' + c.fc.length + ')</button><button role="tab" aria-selected="false" data-o="bac">Sujet type bac</button></div><div class="carte-p no-print" id="zone-ex"></div>';
    h += '<div class="suite no-print">' + (i > 0 ? '<a href="#' + ORDRE[i - 1] + '"><small>← Précédent</small>' + typo(CHAPS[ORDRE[i - 1]].t) + '</a>' : '<a href="#' + t.id + '"><small>← Dossier</small>Thème ' + t.n + '</a>') + (i < ORDRE.length - 1 ? '<a class="d" href="#' + ORDRE[i + 1] + '"><small>Suivant →</small>' + typo(CHAPS[ORDRE[i + 1]].t) + '</a>' : '<a class="d" href="#entrainement"><small>Suivant →</small>Entraînement</a>') + '</div>';
    h += '</div>';
    APP.innerHTML = h;
    activerViz();
    activerVideo();
    $("#imprimer").addEventListener("click", function () { document.documentElement.classList.add("impr"); window.print(); });
    var bc = $("#caviarder"), tab = $(".retenir table");
    bc.addEventListener("click", function () {
      var on = bc.getAttribute("aria-pressed") !== "true";
      bc.setAttribute("aria-pressed", on ? "true" : "false");
      $("span", bc).textContent = on ? "Tout dévoiler" : "Caviarder pour réviser";
      tab.classList.toggle("caviarde", on);
      $$("td", tab).forEach(function (td) { td.classList.remove("vu"); if (on) td.setAttribute("tabindex", "0"); else td.removeAttribute("tabindex"); });
    });
    $$("td", tab).forEach(function (td) {
      function voir() { if (tab.classList.contains("caviarde")) td.classList.add("vu"); }
      td.addEventListener("click", voir);
      td.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); voir(); } });
    });
    var zone = $("#zone-ex");
    var qs = c.qcm.map(function (q) { var o = Object.assign({}, q); o.ch = id; return o; });
    function montre(o) {
      $$(".onglets button").forEach(function (b) { b.setAttribute("aria-selected", b.getAttribute("data-o") === o ? "true" : "false"); });
      if (o === "qcm") qcm(zone, qs, false);
      else if (o === "fc") cartesMemoire(zone, c.fc);
      else zone.innerHTML = '<span class="etiq">' + typo(c.bac.type) + '</span><h3 style="margin-top:6px">« ' + typo(c.bac.s) + ' »</h3><div class="copie">' + typo(c.bac.h) + '</div><p style="font:14px var(--sans);margin:10px 0 0"><a href="#' + t.id + ':sujets">Voir les sujets entièrement corrigés du thème ' + t.n + ' →</a></p>';
    }
    $$(".onglets button").forEach(function (b) { b.addEventListener("click", function () { montre(b.getAttribute("data-o")); }); });
    montre("qcm");
  }

  /* ---------------- QCM ---------------- */
  function qcm(zone, liste, melanger) {
    var qs = melanger ? melange(liste) : liste.slice();
    var k = 0, score = 0;
    function rendu() {
      if (k >= qs.length) {
        zone.innerHTML = '<div class="qcm"><div class="fin"><div class="etiq">Résultat</div><div class="score">' + score + ' / ' + qs.length + '</div><p style="font:15px var(--sans)">' + (score === qs.length ? "Sans faute. Passe aux cartes mémoire ou à un sujet." : score >= qs.length * .7 ? "Bien. Revois les paragraphes des questions manquées." : "Relis le cours, puis recommence : c'est en se trompant qu'on retient.") + '</p><button class="btn plein" id="q-re">Recommencer (ordre mélangé)</button></div></div>';
        $("#q-re", zone).addEventListener("click", function () { qs = melange(liste); k = 0; score = 0; rendu(); });
        return;
      }
      var q = qs[k], ordre = melange(q.o.map(function (_, i) { return i; }));
      var h = '<div class="qcm"><div class="prog"><span>Question ' + (k + 1) + ' / ' + qs.length + '</span><span>Score ' + score + '</span></div><div class="barre"><i style="width:' + (k / qs.length * 100) + '%"></i></div>';
      h += '<p class="q">' + (q.ch && melanger ? '<small>' + CHAPS[q.ch].code + '</small>' : "") + typo(q.q) + '</p><div class="opts">';
      ordre.forEach(function (oi, n) { h += '<button class="opt" data-i="' + oi + '" data-l="' + LETTRES[n] + '">' + typo(q.o[oi]) + '</button>'; });
      h += '</div><div class="expl-z" aria-live="polite"></div></div>';
      zone.innerHTML = h;
      $$(".opt", zone).forEach(function (b) {
        b.addEventListener("click", function () {
          var choix = +b.getAttribute("data-i"), juste = choix === q.r;
          if (juste) score++;
          $$(".opt", zone).forEach(function (x) { x.disabled = true; var xi = +x.getAttribute("data-i"); if (xi === q.r) x.classList.add("bon"); else if (x === b) x.classList.add("faux"); });
          var lien = q.ref ? '<a href="#' + q.ch + '@' + q.ref + '">Revoir le paragraphe →</a>' : "";
          $(".expl-z", zone).innerHTML = '<div class="expl"><b class="' + (juste ? "ok" : "ko") + '">' + (juste ? "Juste." : "Faux.") + '</b> ' + typo(q.e) + '<div class="rangee" style="margin-top:10px;justify-content:space-between">' + lien + '<button class="btn plein petit" id="q-suiv">' + (k === qs.length - 1 ? "Voir le score" : "Question suivante") + '</button></div></div>';
          $("#q-suiv", zone).addEventListener("click", function () { k++; rendu(); });
          $("#q-suiv", zone).focus({ preventScroll: true });
        });
      });
    }
    rendu();
  }

  /* ---------------- cartes mémoire ---------------- */
  function cartesMemoire(zone, liste) {
    var pile = melange(liste), su = 0, revoir = 0, total = liste.length;
    function rendu() {
      if (!pile.length) {
        zone.innerHTML = '<div class="fc"><div class="qcm"><div class="fin"><div class="etiq">Paquet terminé</div><div class="score">' + su + ' / ' + total + '</div><p style="font:15px var(--sans)">sues du premier coup · ' + revoir + ' passage(s) à revoir</p><button class="btn plein" id="fc-re">Rejouer le paquet</button></div></div></div>';
        $("#fc-re", zone).addEventListener("click", function () { pile = melange(liste); su = 0; revoir = 0; rendu(); });
        return;
      }
      var c = pile[0];
      zone.innerHTML = '<div class="fc"><div class="qcm"><div class="prog"><span>Reste ' + pile.length + ' carte(s)</span><span>Sues ' + su + '</span></div></div><div class="scene"><button class="carte" aria-label="Retourner la carte"><span class="face recto"><span class="etiq">Recto</span><span class="txt">' + typo(c[0]) + '</span><span class="aide">TOUCHE POUR RETOURNER</span></span><span class="face verso"><span class="etiq">Verso</span><span class="txt">' + typo(c[1]) + '</span></span></button></div><div class="rangee" style="justify-content:center"><button class="btn" id="fc-non" disabled>À revoir</button><button class="btn plein" id="fc-oui" disabled>Je savais</button></div></div>';
      var carte = $(".carte", zone), hRecto = $(".recto", zone).scrollHeight, hVerso = $(".verso", zone).scrollHeight;
      carte.style.minHeight = Math.max(210, hRecto, hVerso) + "px";
      carte.addEventListener("click", function () { carte.classList.toggle("retournee"); $("#fc-non", zone).disabled = false; $("#fc-oui", zone).disabled = false; });
      $("#fc-oui", zone).addEventListener("click", function () { if (!c.vu) su++; pile.shift(); rendu(); });
      $("#fc-non", zone).addEventListener("click", function () { revoir++; c = pile.shift(); var copie = c.slice(); copie.vu = true; pile.push(copie); rendu(); });
    }
    rendu();
  }

  /* ---------------- visuels : schémas et cartes ---------------- */
  function viz(v, uid) {
    if (Array.isArray(v)) return v.map(function (x, i) { return viz(x, uid + "-" + i); }).join("");
    if (v.indexOf("anim:") === 0) return animHTML(v.slice(5), uid);
    if (v.indexOf("carte:") === 0) return carteHTML(v.slice(6), uid);
    if (v === "zones") return schemaZones(uid);
    if (v === "orbites") return schemaOrbites(uid);
    if (v === "trinite") return schemaTrinite(uid);
    return "";
  }
  var ZONES = [
    ["ei", "Eaux intérieures", "#2D5675", "En deçà de la ligne de base (ports, baies, estuaires) : souveraineté totale, comme sur le territoire terrestre."],
    ["mt", "Mer territoriale · 12 milles", "#3F7FA3", "Jusqu'à 12 milles marins (22 km) : l'État est souverain (police, douane, pêche, sol et sous-sol, espace aérien), mais les navires étrangers ont un droit de passage inoffensif."],
    ["zc", "Zone contiguë · 24 milles", "#5E9AB8", "De 12 à 24 milles : l'État peut contrôler pour prévenir ou punir les infractions douanières, fiscales, sanitaires et d'immigration."],
    ["zee", "ZEE · 200 milles", "#8DB7CC", "Jusqu'à 200 milles (370 km) : droits souverains sur l'exploration et l'exploitation des ressources (pêche, hydrocarbures, énergie). Navigation, survol et pose de câbles restent libres pour tous."],
    ["pc", "Plateau continental · jusqu'à 350 milles", "#B07A1E", "Le sol et le sous-sol peuvent être revendiqués au-delà de 200 milles, jusqu'à 350, si le plateau géologique se prolonge : dossier examiné par la Commission des limites du plateau continental (CLPC)."],
    ["hm", "Haute mer et « la Zone »", "#B3241B", "Au-delà : la haute mer, libre pour tous (près des deux tiers des océans), où le traité BBNJ (en vigueur depuis le 17 janvier 2026) permet de créer des aires marines protégées. Ses fonds, « la Zone », sont un patrimoine commun de l'humanité géré par l'AIFM."]
  ];
  function schemaZones(uid) {
    var x = [70, 110, 160, 215, 400, 520, 640], y0 = 70;
    var s = '<svg viewBox="0 0 640 250" role="img" aria-label="Les espaces maritimes selon la convention de Montego Bay">';
    s += '<rect x="0" y="0" width="640" height="250" fill="none"/>';
    s += '<path d="M0 70 L70 70 L70 250 L0 250Z" fill="var(--k-terre2)" stroke="var(--k-front)"/><text x="10" y="58" class="sch-pt">TERRE</text>';
    for (var i = 0; i < 6; i++) {
      var z = ZONES[i];
      s += '<g class="sch-zone" data-z="' + z[0] + '"><rect x="' + x[i] + '" y="' + y0 + '" width="' + (x[i + 1] - x[i]) + '" height="60" fill="' + z[2] + '" fill-opacity=".85"/></g>';
    }
    s += '<path d="M70 130 L70 160 Q 160 165 300 175 Q 380 182 420 205 Q 470 232 520 238 L640 240 L640 250 L70 250Z" fill="var(--k-terre2)" stroke="var(--k-front)"/>';
    s += '<text x="200" y="195" class="sch-pt">PLATEAU CONTINENTAL</text><text x="530" y="232" class="sch-pt">« LA ZONE »</text><text x="520" y="160" class="sch-pt">GRANDS FONDS</text>';
    s += '<path d="M70 62 V40 M110 62 V40 M160 62 V40 M215 62 V40 M400 62 V40 M520 62 V40" stroke="var(--encre)" stroke-width="1"/>';
    s += '<text x="66" y="34" class="sch-pt" text-anchor="middle">0</text><text x="110" y="34" class="sch-pt" text-anchor="middle">12</text><text x="160" y="34" class="sch-pt" text-anchor="middle">24</text><text x="215" y="34" class="sch-pt" text-anchor="middle">200</text><text x="400" y="34" class="sch-pt" text-anchor="middle">350 (max.)</text>';
    s += '<text x="600" y="34" class="sch-pt" text-anchor="middle">milles</text><text x="72" y="16" class="sch-pt">ligne de base ↓</text>';
    s += '<text x="300" y="104" class="sch-txt" text-anchor="middle" fill="#fff" style="fill:#fff">ZEE</text><text x="580" y="104" class="sch-txt" text-anchor="middle" style="fill:#fff">HAUTE MER</text>';
    s += '<text x="320" y="245" class="sch-pt" text-anchor="middle">schéma sans échelle</text></svg>';
    var b = ZONES.map(function (z) { return '<button aria-pressed="false" data-z="' + z[0] + '">' + z[1] + '</button>'; }).join("");
    return '<figure class="schema" data-schema="zones" id="' + uid + '"><figcaption class="etiq">Schéma interactif · les espaces maritimes (convention de Montego Bay, 1982)</figcaption><div class="cadre">' + s + '</div><div class="choix">' + b + '</div><div class="lecture" aria-live="polite">' + typo("Touche une zone (ou un bouton) pour lire ce que l'État côtier peut y faire. Plus on s'éloigne de la côte, moins ses droits sont étendus.") + '</div></figure>';
  }
  var ORB = [
    ["b", "Orbite basse · 200 à 2 000 km", "La Station spatiale internationale (environ 400 km), la station chinoise Tiangong, les satellites d'observation et les constellations Internet comme Starlink (vers 550 km). Un tour de Terre en 90 minutes environ. C'est l'orbite la plus encombrée et la plus menacée par les débris."],
    ["m", "Orbite moyenne · vers 20 000 km", "Les systèmes de navigation : GPS (États-Unis), Galileo (Union européenne), Glonass (Russie), Beidou (Chine). Avoir son propre système, c'est ne pas dépendre d'une autre puissance en cas de crise."],
    ["g", "Orbite géostationnaire · 35 786 km", "Au-dessus de l'équateur, un satellite fait un tour en 24 heures : il paraît immobile. Télécommunications, météo, alerte antimissile. Les positions sur cette orbite sont une ressource rare, attribuée par l'Union internationale des télécommunications."]
  ];
  function schemaOrbites(uid) {
    var s = '<svg viewBox="0 0 560 320" role="img" aria-label="Les orbites terrestres">';
    s += '<circle cx="280" cy="160" r="34" fill="var(--acier)"/><path d="M256 146q12-8 20 2t22-4M252 170q16 6 28-2t20 6" stroke="var(--papier)" stroke-width="2" fill="none" opacity=".6"/>';
    var R = { b: 56, m: 100, g: 148 };
    ["b", "m", "g"].forEach(function (k) {
      s += '<g class="sch-zone" data-z="' + k + '"><circle cx="280" cy="160" r="' + R[k] + '" fill="none" stroke="' + (k === "g" ? "var(--rouge)" : k === "m" ? "var(--ok)" : "var(--encre)") + '" stroke-width="2" stroke-dasharray="' + (k === "b" ? "0" : "5 4") + '"/>';
      s += '<g class="orbite-sat ' + k + '"><rect x="' + (276) + '" y="' + (160 - R[k] - 4) + '" width="8" height="8" rx="1" fill="' + (k === "g" ? "var(--rouge)" : k === "m" ? "var(--ok)" : "var(--encre)") + '"/></g></g>';
    });
    s += '<text x="342" y="112" class="sch-pt">BASSE</text><text x="382" y="86" class="sch-pt">MOYENNE</text><text x="430" y="40" class="sch-pt">GÉOSTATIONNAIRE</text>';
    s += '<text x="280" y="164" class="sch-txt" text-anchor="middle" style="fill:#fff">Terre</text><text x="280" y="312" class="sch-pt" text-anchor="middle">distances non proportionnelles</text></svg>';
    var b = ORB.map(function (z) { return '<button aria-pressed="false" data-z="' + z[0] + '">' + z[1].split(" · ")[0] + '</button>'; }).join("");
    return '<figure class="schema" data-schema="orbites" id="' + uid + '"><figcaption class="etiq">Schéma interactif · les orbites, une ressource disputée</figcaption><div class="cadre">' + s + '</div><div class="choix">' + b + '</div><div class="lecture" aria-live="polite">' + typo("Touche une orbite pour savoir ce qui s'y trouve et pourquoi elle compte pour la puissance.") + '</div></figure>';
  }
  var TRI = [
    ["p", "Le peuple · la violence originelle", "Haine, hostilité, passions : la force qui pousse à la guerre. La levée en masse de 1793 la fait entrer dans les guerres modernes ; le terrorisme cherche à la manipuler (terroriser, mobiliser des partisans)."],
    ["a", "Le chef et l'armée · hasard et talent", "La guerre est un jeu de probabilités : frictions, incertitude, courage, génie du chef. Napoléon à Austerlitz en est le modèle ; une guérilla en joue en refusant la bataille."],
    ["g", "Le gouvernement · la raison politique", "La guerre est un instrument : le gouvernement fixe le but et décide de la paix. C'est le pôle qui fait de la guerre « la continuation de la politique par d'autres moyens »."]
  ];
  function schemaTrinite(uid) {
    var P = { g: [280, 34], p: [90, 270], a: [470, 270] };
    var s = '<svg viewBox="0 0 560 310" role="img" aria-label="La trinité de Clausewitz">';
    s += '<path class="trace" d="M280 34 L90 270 L470 270 Z" fill="none" stroke="var(--rouge)" stroke-width="2.5"/>';
    s += '<text x="280" y="196" class="sch-txt" text-anchor="middle" style="font-size:15px;font-weight:800">GUERRE</text><text x="280" y="214" class="sch-pt" text-anchor="middle">« un caméléon »</text>';
    TRI.forEach(function (t) {
      var p = P[t[0]];
      s += '<g class="sch-zone" data-z="' + t[0] + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="26" fill="var(--papier)" stroke="var(--encre)" stroke-width="2"/><text x="' + p[0] + '" y="' + (p[1] + 5) + '" class="sch-txt" text-anchor="middle" style="font-size:13px;font-weight:800">' + (t[0] === "g" ? "GOUV." : t[0] === "p" ? "PEUPLE" : "ARMÉE") + '</text></g>';
    });
    s += '<text x="280" y="300" class="sch-pt" text-anchor="middle">Clausewitz, De la guerre, livre I, chapitre 1</text></svg>';
    var b = TRI.map(function (z) { return '<button aria-pressed="false" data-z="' + z[0] + '">' + z[1].split(" · ")[0] + '</button>'; }).join("");
    return '<figure class="schema" data-schema="trinite" id="' + uid + '"><figcaption class="etiq">Schéma interactif · la « trinité » de Clausewitz</figcaption><div class="cadre">' + s + '</div><div class="choix">' + b + '</div><div class="lecture" aria-live="polite">' + typo("Touche un pôle du triangle. Si l'un des trois fait défaut, la guerre change de nature ou s'arrête.") + '</div></figure>';
  }
  function activerViz() {
    $$(".schema").forEach(function (f) {
      var type = f.getAttribute("data-schema"), data = type === "zones" ? ZONES : type === "orbites" ? ORB : TRI;
      function choisir(z) {
        var d = data.filter(function (x) { return x[0] === z; })[0];
        $$(".sch-zone", f).forEach(function (g) { g.classList.toggle("off", g.getAttribute("data-z") !== z); g.classList.toggle("on", g.getAttribute("data-z") === z); });
        $$(".choix button", f).forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-z") === z ? "true" : "false"); });
        $(".lecture", f).innerHTML = '<b>' + typo(d[1]) + '</b>' + typo(d[3] || d[2]);
      }
      $$(".choix button", f).forEach(function (b) { b.addEventListener("click", function () { choisir(b.getAttribute("data-z")); }); });
      $$(".sch-zone", f).forEach(function (g) { g.addEventListener("click", function () { choisir(g.getAttribute("data-z")); }); });
    });
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("joue"); io.unobserve(e.target); } }); }, { threshold: .35 });
      $$(".schema .cadre").forEach(function (c) { io.observe(c); });
    }
    $$(".carto").forEach(activerCarte);
    $$(".anim").forEach(activerAnim);
  }

  /* fond d'une carte ou d'une scène : « monde » (fond mondial commun), « @n » (fond régional partagé, CARTES.fonds[n],
     dédoublonné par build.py) ou le SVG du fond lui-même */
  function fondSVG(f) {
    if (f === "monde") return '<rect width="' + CARTES.monde.w + '" height="' + CARTES.monde.h + '" class="k-mer-f"/><path class="k-grat" d="' + CARTES.monde.grat + '"/><path class="k-terre" d="' + CARTES.monde.terre + '"/>';
    if (f && f.charAt(0) === "@") return CARTES.fonds[+f.slice(1)];
    return f || "";
  }

  /* ---------------- animations explicatives pas à pas (ANIMS) ---------------- */
  function animHTML(nom, uid) {
    var A = ANIMS[nom];
    if (!A) return "";
    var sc = typeof A.scene === "string" ? CARTES.anims[A.scene.slice(6)] : A.scene;
    var vb = sc.vb || [0, 0, sc.w, sc.h], fond = "";
    fond = fondSVG(sc.fond);
    /* la date de l'étape est tamponnée dans une bande au-dessus de la scène : elle ne masque plus le dessin */
    var dates = A.etapes.some(function (e) { return e.date; });
    var pts = A.etapes.map(function (e, i) { return '<button class="a-pt" data-i="' + i + '" aria-label="Étape ' + (i + 1) + ' : ' + esc(sans(e.titre)) + '"><span>' + (i + 1) + '</span></button>'; }).join("");
    return '<figure class="anim" data-anim="' + nom + '" id="' + uid + '"><div class="a-tete"><span class="etiq">Animation · ' + A.etapes.length + ' étapes</span><h3>' + typo(A.titre) + '</h3></div>' +
      (dates ? '<div class="a-bande" aria-hidden="true"><span class="a-date"></span></div>' : "") +
      '<div class="a-cadre"><svg viewBox="' + vb.join(" ") + '" role="img" aria-label="' + esc(sans(A.titre)) + '" style="--mw:' + (sc.mw || Math.min(900, Math.max(560, Math.round(vb[2] * 0.86)))) + 'px">' + fond + (sc.calques || sc.svg || "") + '</svg></div>' +
      '<div class="a-cmd"><button class="a-b" data-a="prec" aria-label="Étape précédente"><svg class="ic"><use href="#i-prec"/></svg></button><button class="a-b a-lire" data-a="lire" aria-label="Lecture"><svg class="ic"><use href="#i-lire"/></svg></button><button class="a-b" data-a="suiv" aria-label="Étape suivante"><svg class="ic"><use href="#i-suiv"/></svg></button><div class="a-pts">' + pts + '</div></div>' +
      '<div class="a-legende" aria-live="polite"></div>' + (A.source ? '<div class="src">' + typo(A.source) + '</div>' : "") + '</figure>';
  }
  function activerAnim(f) {
    var A = ANIMS[f.getAttribute("data-anim")], k = -1, minuteur = null, lecture = false;
    var els = $$("[data-k]", f), leg = $(".a-legende", f), dateEl = $(".a-date", f) || document.createElement("span"), bLire = $('[data-a="lire"]', f);
    function etat(n) {
      var vis = {};
      for (var i = 0; i <= n; i++) { (A.etapes[i].montre || []).forEach(function (x) { vis[x] = 1; }); (A.etapes[i].cache || []).forEach(function (x) { delete vis[x]; }); }
      return vis;
    }
    function teletype(el, txt) {
      if (el._t) clearInterval(el._t);
      if (!MO()) { el.textContent = txt; return; }
      var i = 0; el.textContent = "";
      el._t = setInterval(function () { i++; el.textContent = txt.slice(0, i) + (i < txt.length ? "▌" : ""); if (i >= txt.length) clearInterval(el._t); }, 45);
    }
    function aller(n, auto) {
      n = Math.max(0, Math.min(A.etapes.length - 1, n));
      var avant = k >= 0 ? etat(k) : {}, vis = etat(n), e = A.etapes[n], acc = {};
      (e.accent || []).forEach(function (x) { acc[x] = 1; });
      els.forEach(function (el) {
        var id = el.getAttribute("data-k"), on = !!vis[id];
        el.classList.toggle("anim-off", !on);
        el.classList.toggle("anim-acc", !!acc[id]);
        if (on && !avant[id]) { el.classList.remove("anim-in"); void el.getBoundingClientRect(); el.classList.add("anim-in"); }
      });
      k = n;
      /* sur téléphone, le cadre défile : on le recentre sur le premier élément mis en valeur de l'étape */
      var cible = (e.accent || [])[0] || (e.montre || [])[0], cadreA = $(".a-cadre", f), el = cible && $('[data-k="' + cible + '"]', f);
      if (el && cadreA.scrollWidth > cadreA.clientWidth + 2) {
        var r = el.getBoundingClientRect(), rc = cadreA.getBoundingClientRect();
        cadreA.scrollTo({ left: Math.max(0, cadreA.scrollLeft + r.left + r.width / 2 - rc.left - rc.width / 2), behavior: MO() && k >= 0 && auto !== undefined ? "smooth" : "auto" });
      }
      teletype(dateEl, e.date || "");
      rejouer(leg);
      leg.innerHTML = '<div class="a-num">ÉTAPE ' + (n + 1) + ' / ' + A.etapes.length + (e.date ? ' · ' + esc(e.date) : "") + '</div><b>' + typo(e.titre) + '</b>' + typo(e.texte || "");
      $$(".a-pt", f).forEach(function (b, i) { b.classList.toggle("fait", i < n); b.setAttribute("aria-current", i === n ? "step" : "false"); });
      $('[data-a="prec"]', f).disabled = n === 0;
      $('[data-a="suiv"]', f).disabled = n === A.etapes.length - 1;
      if (!auto) stop();
    }
    function stop() { lecture = false; clearTimeout(minuteur); bLire.innerHTML = '<svg class="ic"><use href="#i-lire"/></svg>'; bLire.setAttribute("aria-label", "Lecture"); f.classList.remove("en-lecture"); }
    function tic() {
      if (!lecture) return;
      minuteur = setTimeout(function () { if (k >= A.etapes.length - 1) { stop(); return; } aller(k + 1, true); tic(); }, (A.etapes[k].duree || 5.5) * 1000);
    }
    function lire() {
      if (lecture) { stop(); return; }
      if (k >= A.etapes.length - 1) aller(0, true);
      lecture = true; f.classList.add("en-lecture");
      bLire.innerHTML = '<svg class="ic"><use href="#i-pause"/></svg>'; bLire.setAttribute("aria-label", "Pause");
      tic();
    }
    $('[data-a="prec"]', f).addEventListener("click", function () { aller(k - 1); });
    $('[data-a="suiv"]', f).addEventListener("click", function () { aller(k + 1); });
    bLire.addEventListener("click", lire);
    $$(".a-pt", f).forEach(function (b) { b.addEventListener("click", function () { aller(+b.getAttribute("data-i")); }); });
    aller(0);
  }
  function carteHTML(nom, uid) {
    var m = CARTES.cartes[nom], meta = m.meta, W = m.w, H = m.h, vb = m.vb || [0, 0, W, H];
    /* sur téléphone, largeur minimale proportionnelle au cadrage : les étiquettes gardent environ 9,5 px à l'écran */
    var s = '<svg viewBox="' + vb.join(" ") + '" role="img" aria-label="' + esc(meta.t) + '" style="--mw:' + Math.min(1000, Math.max(680, Math.round(vb[2] * 0.9))) + 'px">';
    s += fondSVG(m.fond);
    s += m.deco;
    m.pts.forEach(function (p, i) {
      var col = meta.c[p.c][1], dx = p.a === "end" ? -8 : 8;
      s += '<g class="pt" data-c="' + p.c + '" data-i="' + i + '" tabindex="0" role="button" aria-label="' + esc(p.t) + '"><circle cx="' + p.x + '" cy="' + p.y + '" r="5.5" fill="' + col + '" style="animation-delay:' + (0.25 + i * 0.04).toFixed(2) + 's"/><text x="' + (p.x + dx) + '" y="' + (p.y + 4 + (p.dy || 0)) + '" text-anchor="' + (p.a || "start") + '">' + esc(p.n) + '</text></g>';
    });
    s += '</svg>';
    var leg = Object.keys(meta.c).map(function (k) { return '<button aria-pressed="true" data-c="' + k + '"><span class="sym" style="background:' + meta.c[k][1] + '"></span>' + typo(meta.c[k][0]) + '</button>'; }).join("");
    (meta.leg || []).forEach(function (l) {
      var sym = l[0] === "choke" ? '<span class="sym" style="background:none;box-shadow:none;border:0;color:var(--rouge);font:800 14px/12px var(--sans);width:auto">✕</span>' : l[0] === "zone" ? '<span class="sym zone" style="background:rgba(179,36,27,.35);border-color:var(--rouge)"></span>' : l[0] === "il" ? '<span class="sym zone" style="background:#8FAFC7"></span>' : l[0] === "ps" ? '<span class="sym zone" style="background:#D9A86B"></span>' : '<span class="sym ligne" style="background:' + (l[0] === "neuf" ? "var(--rouge)" : l[0] === "nfz" || l[0] === "route" ? "var(--acier)" : "var(--encre2)") + '"></span>';
      leg += '<span class="statique">' + sym + typo(l[1]) + '</span>';
    });
    var liste = m.pts.map(function (p, i) { return '<li><button class="btn-lien" data-i="' + i + '" style="background:none;border:0;padding:6px 0;min-height:36px;cursor:pointer;text-align:left;font:600 14px var(--sans);color:var(--acier)">' + esc(p.t) + '</button></li>'; }).join("");
    return '<figure class="carto" data-carte="' + nom + '" id="' + uid + '"><figcaption><span class="etiq">Carte interactive</span><h3>' + typo(meta.t) + '</h3></figcaption><div class="leg">' + leg + '</div><div class="carto-cadre">' + s + '</div><div class="carto-info" aria-live="polite">' + typo("Touche un point pour afficher la fiche du lieu ; touche une catégorie de la légende pour l'afficher ou la masquer.") + '</div><details class="pli"><summary>Tous les lieux de la carte</summary><div class="corps"><ul style="margin:0;padding-left:16px">' + liste + '</ul></div></details><div class="src">Fond : Natural Earth 1:50m (domaine public), pays actuels ; positions approximatives à cette échelle. Carte réalisée pour le site.</div></figure>';
  }
  function activerCarte(f) {
    var m = CARTES.cartes[f.getAttribute("data-carte")], cadreC = $(".carto-cadre", f);
    /* sur téléphone, la carte défile de côté : la centrer sur les points au départ, puis sur le point choisi */
    function centrer(x, doux) {
      if (cadreC.scrollWidth <= cadreC.clientWidth + 2) return;
      var vb = m.vb || [0, 0, m.w, m.h], k = cadreC.scrollWidth / vb[2];
      cadreC.scrollTo({ left: Math.max(0, (x - vb[0]) * k - cadreC.clientWidth / 2), behavior: doux && MO() ? "smooth" : "auto" });
    }
    var xs = m.pts.map(function (p) { return p.x; }).sort(function (a, b) { return a - b; });
    if (xs.length) centrer((xs[0] + xs[xs.length - 1]) / 2);
    function choisir(i) {
      var p = m.pts[i];
      centrer(p.x, true);
      $$(".pt", f).forEach(function (g) { g.classList.toggle("sel", +g.getAttribute("data-i") === i); });
      rejouer($(".carto-info", f));
      $(".carto-info", f).innerHTML = '<b>' + typo(esc(p.t)) + '</b>' + typo(p.d);
    }
    $$(".pt", f).forEach(function (g) {
      g.addEventListener("click", function () { choisir(+g.getAttribute("data-i")); });
      g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); choisir(+g.getAttribute("data-i")); } });
    });
    $$(".btn-lien", f).forEach(function (b) { b.addEventListener("click", function () { choisir(+b.getAttribute("data-i")); $(".carto-info", f).scrollIntoView({ block: "nearest", behavior: MO() ? "smooth" : "auto" }); }); });
    $$(".leg button", f).forEach(function (b) {
      b.addEventListener("click", function () {
        var on = b.getAttribute("aria-pressed") !== "true", c = b.getAttribute("data-c");
        b.setAttribute("aria-pressed", on ? "true" : "false");
        $$('.pt[data-c="' + c + '"]', f).forEach(function (g) { g.classList.toggle("cache-couche", !on); });
      });
    });
  }

  /* ---------------- frise ---------------- */
  function couleur(D, k) { return Array.isArray(D.cats[k]) ? D.cats[k][1] : COUL[k] || "var(--rouge)"; }
  function friseHTML(id) {
    var D = DOSSIERS[id];
    var h = '<div class="frise-bloc"><div class="frise-filtres" role="group" aria-label="Filtrer la frise">';
    Object.keys(D.cats).forEach(function (k) { h += '<button aria-pressed="true" data-c="' + k + '"><i style="background:' + couleur(D, k) + '"></i>' + (Array.isArray(D.cats[k]) ? D.cats[k][0] : D.cats[k]) + '</button>'; });
    h += '<button aria-pressed="false" data-mode="lire" style="margin-left:auto">' + ic("lire") + '<span>Dérouler la frise</span></button><button aria-pressed="false" data-mode="cache">' + ic("oeil") + 'Masquer les dates</button></div>';
    h += '<div class="frise-cadre"><div class="frise">';
    D.frise.forEach(function (e, i) { h += '<button class="ev" data-c="' + e[2] + '" data-i="' + i + '" aria-pressed="false" style="--c:' + couleur(D, e[2]) + '"><span class="an">' + e[0] + '</span><span class="dt">' + typo(e[1]) + '</span><b>' + typo(e[3]) + '</b></button>'; });
    h += '</div></div><div class="frise-info" aria-live="polite">' + typo("Touche un événement pour lire son explication. Mode révision : masque les dates et essaie de les retrouver avant de toucher.") + '</div></div>';
    return h;
  }
  function activerFrise(id) {
    var D = DOSSIERS[id], f = $(".frise"), info = $(".frise-info");
    $$(".ev").forEach(function (b) {
      b.addEventListener("click", function () {
        var e = D.frise[+b.getAttribute("data-i")];
        $$(".ev").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        b.classList.add("vu");
        rejouer(info);
        info.innerHTML = '<b class="tt" style="--c:' + couleur(D, e[2]) + '"></b><br><b>' + typo(e[3]) + '</b> — ' + typo(e[4]);
        var tt = $(".tt", info), d = sans(e[1]), n = 0;
        if (!MO()) tt.textContent = d;
        else { tt.textContent = ""; clearInterval(info._t); info._t = setInterval(function () { n++; tt.textContent = d.slice(0, n) + (n < d.length ? "▌" : ""); if (n >= d.length) clearInterval(info._t); }, 40); }
      });
    });
    $$(".frise-filtres button[data-c]").forEach(function (b) {
      b.addEventListener("click", function () {
        var on = b.getAttribute("aria-pressed") !== "true"; b.setAttribute("aria-pressed", on ? "true" : "false");
        $$('.ev[data-c="' + b.getAttribute("data-c") + '"]').forEach(function (x) { x.style.display = on ? "" : "none"; });
      });
    });
    /* lecture automatique : la frise se déroule d'événement en événement */
    var bl = $('.frise-filtres button[data-mode="lire"]'), cadreF = $(".frise-cadre"), minut = null;
    function arreter() { clearInterval(minut); minut = null; bl.setAttribute("aria-pressed", "false"); $("span", bl).textContent = "Dérouler la frise"; }
    function montrer(b) {
      b.click();
      var x = b.offsetLeft - cadreF.clientWidth / 2 + b.offsetWidth / 2;
      cadreF.scrollTo({ left: Math.max(0, x), behavior: MO() ? "smooth" : "auto" });
    }
    bl.addEventListener("click", function () {
      if (minut) { arreter(); return; }
      var evs = $$(".ev").filter(function (x) { return x.style.display !== "none"; });
      if (!evs.length) return;
      var cur = evs.map(function (x) { return x.getAttribute("aria-pressed"); }).indexOf("true"), k = cur >= 0 && cur < evs.length - 1 ? cur + 1 : 0;
      bl.setAttribute("aria-pressed", "true"); $("span", bl).textContent = "Pause";
      montrer(evs[k]);
      minut = setInterval(function () { if (!document.body.contains(bl)) { clearInterval(minut); return; } k++; if (k >= evs.length) { arreter(); return; } montrer(evs[k]); }, 3200);
    });
    $$(".ev").forEach(function (b) { b.addEventListener("pointerdown", function () { if (minut) arreter(); }); });
    window.addEventListener("hashchange", arreter, { once: true });
    var bm = $('.frise-filtres button[data-mode="cache"]');
    bm.addEventListener("click", function () { var on = bm.getAttribute("aria-pressed") !== "true"; bm.setAttribute("aria-pressed", on ? "true" : "false"); f.classList.toggle("cache", on); $$(".ev").forEach(function (x) { x.classList.remove("vu"); }); });
  }

  /* fiche de renseignement (notions, acteurs) */
  function ficheR(type, i, titre, txt) {
    return '<article class="fiche-r"><header><span>FICHE ' + type.toUpperCase() + ' N° ' + String(i + 1).padStart(2, "0") + '</span><span class="classe">IDENTIFIÉ</span></header><h4>' + typo(titre) + '</h4><p>' + typo(txt) + '</p></article>';
  }

  /* ---------------- dossier d'un thème ---------------- */
  var ONGLETS_T = [["plan", "Plan et notions"], ["frise", "Frise"], ["cartes", "Cartes"], ["anims", "Animations"], ["debats", "Débats"], ["sujets", "Sujets corrigés"]];
  /* animations des chapitres d'un thème, dans l'ordre du programme */
  function animsDuTheme(t) {
    var l = [];
    [t.intro].concat(t.axes, [t.otc]).forEach(function (b) {
      var c = CHAPS[b.ch];
      if (c) c.secs.forEach(function (s) { [].concat(s.viz || []).forEach(function (v) { if (v.indexOf("anim:") === 0 && ANIMS[v.slice(5)]) l.push([b.ch, v.slice(5)]); }); });
    });
    return l;
  }
  function pageTheme(id, onglet) {
    var t = theme(id), D = DOSSIERS[id] || { cats: {}, frise: [], notions: [], acteurs: [], cartes: [], debats: [], autres: [] };
    onglet = onglet || "plan";
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · Dossier du thème ' + t.n + '</div>';
    h += '<h1 class="titre">' + typo(t.titre) + '<span class="ligne-rouge"></span></h1>';
    h += '<div class="rangee" style="margin:4px 0 12px"><span class="tampon">Rédigé</span><span class="tampon ' + (t.ecrit27 ? "" : "gris") + '">' + (t.ecrit27 ? "Écrit 2027" : "Hors écrit 2027") + '</span></div>';
    h += '<div class="carte-p onglet" data-onglet="Problématique du thème · ' + t.h + '"><p style="font:700 17px/1.45 var(--sans)">' + typo(t.pb) + '</p><p style="margin:0;font:15px/1.5 var(--sans)">' + typo(t.ecrit) + '</p></div>';
    h += '<div class="onglets" role="tablist">' + ONGLETS_T.map(function (o) { return '<button role="tab" data-o="' + o[0] + '" aria-selected="' + (o[0] === onglet) + '">' + o[1] + '</button>'; }).join("") + '</div><div id="zone-t"></div></div>';
    APP.innerHTML = h;
    function montre(o) {
      $$(".onglets button").forEach(function (b) { b.setAttribute("aria-selected", b.getAttribute("data-o") === o ? "true" : "false"); });
      var z = $("#zone-t"), x = "";
      if (o === "plan") {
        x += '<h2 class="sec"><span class="n">01</span>Les chapitres du dossier</h2>' + structureHTML(t, true);
        x += '<p style="font:14px var(--sans);color:var(--encre2)">Intitulés et jalons recopiés du programme officiel (BO spécial n° 8 du 25 juillet 2019).</p>';
        x += '<h2 class="sec"><span class="n">02</span>Notions clés</h2><div class="fiches-r">' + D.notions.map(function (n, i) { return ficheR("Notion", i, n[0], n[1]); }).join("") + '</div>';
        x += '<h2 class="sec"><span class="n">03</span>Les acteurs</h2><div class="fiches-r">' + D.acteurs.map(function (n, i) { return ficheR("Acteurs", i, n[0], n[1]); }).join("") + '</div>';
      } else if (o === "frise") {
        x += '<h2 class="sec"><span class="n">⟶</span>Frise chronologique</h2>' + friseHTML(id);
      } else if (o === "cartes") {
        x += '<h2 class="sec"><span class="n">◎</span>Cartes du thème</h2>' + D.cartes.map(function (c, k) { return carteHTML(c, id + "-c" + k); }).join("");
      } else if (o === "anims") {
        var la = animsDuTheme(t);
        x += '<h2 class="sec"><span class="n">▶</span>Animations du thème</h2><p style="font:15px var(--sans)">' + typo("Chaque animation se joue étape par étape : lecture, pause, étape précédente ou suivante. Les dates s'affichent au télétype, la légende explique ce qui se passe.") + '</p>';
        x += la.length ? la.map(function (a, k) { return '<p class="etiq" style="margin:22px 0 -8px"><a href="#' + a[0] + '">' + CHAPS[a[0]].code + ' →</a></p>' + animHTML(a[1], id + "-an" + k); }).join("") : '<p>Aucune animation pour ce thème.</p>';
      } else if (o === "debats") {
        x += '<h2 class="sec"><span class="n">⇄</span>Repères de débat</h2><p style="font:15px var(--sans)">' + typo("Des arguments contradictoires, utiles pour une partie dialectique de dissertation ou pour l'échange du Grand oral.") + '</p>';
        D.debats.forEach(function (d) { x += '<div class="carte-p"><h3 style="margin-top:0">' + typo(d.q) + '</h3><div class="debat"><div class="col pour"><h4>Oui, car…</h4><ul>' + d.pour.map(function (a) { return '<li>' + typo(a) + '</li>'; }).join("") + '</ul></div><div class="col contre"><h4>Non, car…</h4><ul>' + d.contre.map(function (a) { return '<li>' + typo(a) + '</li>'; }).join("") + '</ul></div></div><div class="bilan"><b>Pour trancher :</b> ' + typo(d.bilan) + '</div></div>'; });
      } else {
        var S = D.dissert, E = D.etude;
        x += '<h2 class="sec"><span class="n">A</span>Dissertation corrigée</h2><div class="carte-p onglet copie" data-onglet="Sujet de dissertation"><h3 style="margin-top:0;font:800 21px/1.2 var(--titre);text-transform:uppercase">« ' + typo(S.s) + ' »</h3><p class="etiq" style="margin-bottom:12px">' + typo(S.src) + '</p>';
        x += '<details class="pli" open><summary>1. Analyser le sujet</summary><div class="corps">' + typo(S.analyse) + '</div></details>';
        x += '<details class="pli"><summary>2. Problématique</summary><div class="corps"><b>' + typo(S.pb) + '</b></div></details>';
        x += '<details class="pli"><summary>3. Introduction rédigée</summary><div class="corps">' + typo(S.intro) + '</div></details>';
        x += '<details class="pli"><summary>4. Plan détaillé avec exemples</summary><div class="corps">' + S.plan.map(function (p) { return '<div class="plan-p"><h4>' + typo(p.t) + '</h4>' + p.sous.map(function (s) { return '<p class="sp"><b>' + typo(s[0]) + '.</b> ' + typo(s[1]) + '</p>'; }).join("") + '</div>'; }).join("") + '</div></details>';
        x += '<details class="pli"><summary>5. Conclusion rédigée</summary><div class="corps">' + typo(S.concl) + '</div></details>';
        x += '<details class="pli"><summary>Bonus : un croquis</summary><div class="corps">' + typo(S.croquis) + '</div></details></div>';
        x += '<h2 class="sec"><span class="n">B</span>Étude critique de document corrigée</h2><div class="carte-p onglet copie" data-onglet="Étude critique"><h3 style="margin-top:0;font:800 21px/1.2 var(--titre);text-transform:uppercase">' + typo(E.titre) + '</h3><p class="etiq" style="margin-bottom:12px">' + typo(E.src) + '</p><div class="doc">' + E.doc.txt.map(function (p) { return '<p>' + typo(p) + '</p>'; }).join("") + '<div class="ref">' + typo(E.doc.ref) + '</div></div><p style="margin-top:12px;font:700 15.5px/1.5 var(--sans)">Consigne : ' + typo(E.consigne) + '</p>';
        x += '<details class="pli"><summary>Introduction rédigée</summary><div class="corps">' + typo(E.intro) + '</div></details>';
        E.parts.forEach(function (p) { x += '<details class="pli"><summary>' + typo(p[0]) + '</summary><div class="corps">' + typo(p[1]) + '</div></details>'; });
        x += '<details class="pli"><summary>Conclusion rédigée</summary><div class="corps">' + typo(E.concl) + '</div></details><div class="bilan">' + typo(E.critique) + '</div></div>';
        x += '<h2 class="sec"><span class="n">C</span>Autres sujets pour t\'entraîner</h2><div class="carte-p">' + D.autres.map(function (a) { return '<h3 style="margin-top:6px">« ' + typo(a[0]) + ' »</h3><p style="font:15px/1.5 var(--sans)">' + typo(a[1]) + '</p>'; }).join("") + '</div>';
      }
      z.innerHTML = x;
      if (o === "frise") activerFrise(id);
      if (o === "cartes") $$(".carto").forEach(activerCarte);
      if (o === "anims") $$(".anim").forEach(activerAnim);
    }
    $$(".onglets button").forEach(function (b) { b.addEventListener("click", function () { history.replaceState(null, "", "#" + id + ":" + b.getAttribute("data-o")); montre(b.getAttribute("data-o")); }); });
    montre(onglet);
  }

  /* ---------------- l'épreuve ---------------- */
  function pageEpreuve() {
    var E = EPREUVE, S = DOSSIERS.t2.dissert;
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · Bac</div><h1 class="titre">L\'épreuve écrite d\'HGGSP<span class="ligne-rouge"></span></h1>';
    h += '<div class="alerte acier">' + typo("Source : note de service du 11 septembre 2026 (BO spécial n° 4 du 17 septembre 2026), applicable à partir de la session 2027.") + '</div>';
    h += '<div class="carte-p onglet retenir" data-onglet="Le format officiel"><table>' + E.format.map(function (r) { return '<tr><th>' + r[0] + '</th><td>' + typo(r[1]) + '</td></tr>'; }).join("") + '</table></div>';
    h += '<h2 class="sec"><span class="n">01</span>Quels thèmes à l\'écrit ?</h2><div class="tab-cadre"><table class="tab-ecrit"><thead><tr><th>Thème</th><th>2027</th><th>2028</th></tr></thead><tbody>';
    var pair = { t1: 1, t2: 1, t3: 1, t5: 1 }, imp = { t2: 1, t4: 1, t5: 1, t6: 1 };
    THEMES.forEach(function (t) { h += '<tr><td><a href="#' + t.id + '">' + t.n + '. ' + typo(t.titre) + '</a></td><td class="' + (imp[t.id] ? "oui" : "non") + '">' + (imp[t.id] ? "oui" : "—") + '</td><td class="' + (pair[t.id] ? "oui" : "non") + '">' + (pair[t.id] ? "oui" : "—") + '</td></tr>'; });
    h += '</tbody></table></div><p style="font:14px var(--sans);color:var(--encre2)">' + typo("Les thèmes 2 et 5 tombent chaque année. Tous les thèmes restent au programme de l'année et peuvent servir au Grand oral.") + '</p>';
    h += '<h2 class="sec"><span class="n">02</span>La dissertation, pas à pas</h2><div class="carte-p"><ol class="etapes">' + E.dissert.map(function (e) { return '<li><b>' + e[0] + '</b>' + typo(e[1]) + '</li>'; }).join("") + '</ol></div>';
    h += '<h2 class="sec"><span class="n">03</span>Une introduction modèle, commentée</h2><p style="font:15px var(--sans)">Sujet : « ' + typo(S.s) + ' » (bac 2025). Chaque bloc est commenté.</p><div class="annot">';
    var segs = [["Accroche", "Le 24 octobre 1648, à Münster et à Osnabrück, les diplomates de presque toute l'Europe signent les traités qui mettent fin à la guerre de Trente Ans. Près de quatre siècles plus tard, le 10 octobre 2025, un cessez-le-feu est conclu à Gaza après deux ans de guerre, sans qu'aucun accord de paix ne soit signé. Entre ces deux dates, la manière de faire la paix a profondément changé.", "Deux faits datés qui encadrent la période et posent déjà un contraste : traité contre simple cessez-le-feu."],
      ["Définitions", "La paix peut se définir a minima comme l'absence de guerre, mais une paix durable suppose un règlement politique accepté, des garanties et la justice. La « construire », c'est mobiliser des acteurs (États, diplomates, organisations internationales, médiateurs) et des outils (traités, sécurité collective, opérations de paix, justice).", "Chaque mot du sujet est défini, y compris le verbe « construire », souvent oublié."],
      ["Problématique", "Comment, depuis le XVIIe siècle, les États et la communauté internationale ont-ils cherché à construire une paix durable, et pourquoi cette construction reste-t-elle inachevée ?", "Une vraie question, avec une tension (chercher / inachevée), qui annonce le fil rouge."],
      ["Annonce du plan", "Nous verrons d'abord la paix par les traités entre États souverains, puis la paix par la sécurité collective, enfin les limites de cette construction face aux conflits contemporains.", "Trois parties claires, chronologiques puis critiques."]];
    segs.forEach(function (s) { h += '<div class="seg"><span class="etiq">' + s[0] + '</span>' + typo(s[1]) + '<span class="com">→ ' + typo(s[2]) + '</span></div>'; });
    h += '</div><p style="font:15px var(--sans);margin-top:10px"><a href="#t2:sujets">Lire le corrigé complet (plan détaillé, conclusion) →</a></p>';
    h += '<h2 class="sec"><span class="n">04</span>L\'étude critique de document(s)</h2><div class="carte-p"><ol class="etapes">' + E.etude.map(function (e) { return '<li><b>' + e[0] + '</b>' + typo(e[1]) + '</li>'; }).join("") + '</ol><p style="font:15px var(--sans);margin:0">Une étude corrigée par thème : ' + THEMES.filter(function (t) { return DOSSIERS[t.id] && DOSSIERS[t.id].etude; }).map(function (t) { return '<a href="#' + t.id + ':sujets">' + typo(DOSSIERS[t.id].etude.titre) + ' (thème ' + t.n + ')</a>'; }).join(" ; ") + '.</p></div>';
    h += '<h2 class="sec"><span class="n">05</span>Le Grand oral</h2><div class="carte-p"><p style="font:15.5px/1.55 var(--sans)">' + typo(E.grandOral) + '</p><h3>Des idées de questions</h3><ul style="font:15px/1.5 var(--sans);padding-left:18px">' + E.idees.map(function (i) { return '<li>' + typo(i) + '</li>'; }).join("") + '</ul></div>';
    h += '<h2 class="sec"><span class="n">06</span>Sujets tombés récemment</h2><div class="carte-p"><ul class="liens" style="padding-left:18px">' + SUJETS_TOMBES.map(function (s) { return '<li><b>' + typo(s[2]) + '</b><small>' + s[0] + ' · ' + s[1] + ' · <a href="#' + s[3] + '">thème ' + s[3].slice(1) + '</a></small></li>'; }).join("") + '</ul><p style="font:13px var(--sans);color:var(--encre2);margin:0">Sujets de métropole (Eduscol, Géoconfluences). En 2025, la liste des thèmes évaluables n\'était pas celle qui s\'applique à partir de 2027 ; pour les énoncés complets, voir les annales dans la page Ressources.</p></div>';
    h += '</div>';
    APP.innerHTML = h;
  }

  /* ---------------- ressources ---------------- */
  function pageRessources() {
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · Ressources</div><h1 class="titre">Ressources vérifiées<span class="ligne-rouge"></span></h1>';
    h += '<p style="font:15px var(--sans)">' + typo("Chaque lien a été vérifié en novembre 2026. Les sites officiels d'abord, puis les ressources de professeurs et de géopolitique.") + '</p>';
    RESSOURCES.forEach(function (g, k) {
      h += '<h2 class="sec"><span class="n">' + String(k + 1).padStart(2, "0") + '</span>' + typo(g.t) + '</h2><div class="carte-p"><ul class="liens" style="padding-left:18px;margin:0">';
      g.l.forEach(function (l) { h += '<li><a href="' + esc(l[1]) + '" target="_blank" rel="noopener">' + typo(l[0]) + '</a><small>' + typo(l[2]) + '</small></li>'; });
      h += '</ul></div>';
    });
    h += '<h2 class="sec"><span class="n">' + String(RESSOURCES.length + 1).padStart(2, "0") + '</span>Manuels</h2><div class="carte-p"><p style="font:15px/1.5 var(--sans);margin:0">' + typo(MANUELS) + '</p></div></div>';
    APP.innerHTML = h;
  }

  /* ---------------- entraînement ---------------- */
  function pageEntrainement() {
    var portees = [["tout", "Tout"]].concat(TH_RED.map(function (t) { return [t, "Thème " + t.slice(1)]; }), ORDRE.map(function (c) { return [c, CHAPS[c].code.replace(" · ", " ").replace("OBJET CONCLUSIF", "OBJET CONCL.")]; }));
    var h = '<div class="page"><div class="fil"><a href="#accueil">Programme</a> · Entraînement</div><h1 class="titre">Entraînement<span class="ligne-rouge"></span></h1>';
    h += '<p style="font:15px var(--sans)">' + typo("Choisis ce que tu veux réviser, puis le mode. Chaque série de QCM tire 15 questions au hasard ; chaque erreur te renvoie au paragraphe du cours.") + '</p>';
    h += '<div class="carte-p onglet" data-onglet="1. Ce que tu révises"><div class="puces" id="portee">' + portees.map(function (p, i) { return '<button class="btn petit" data-p="' + p[0] + '" aria-pressed="' + (i === 0) + '" style="border-radius:999px;' + (i === 0 ? "background:var(--encre);color:var(--papier)" : "") + '">' + p[1] + '</button>'; }).join("") + '</div></div>';
    h += '<div class="onglets" role="tablist" style="margin-top:20px"><button role="tab" data-o="qcm" aria-selected="true">QCM mélangé</button><button role="tab" data-o="fc" aria-selected="false">Cartes mémoire</button></div><div class="carte-p" id="zone-e"></div></div>';
    APP.innerHTML = h;
    var portee = "tout", mode = "qcm";
    function chaps() { return ORDRE.filter(function (c) { return portee === "tout" || c === portee || CHAPS[c].th === portee; }); }
    function lance() {
      var z = $("#zone-e");
      if (mode === "qcm") {
        var qs = []; chaps().forEach(function (c) { CHAPS[c].qcm.forEach(function (q) { var o = Object.assign({}, q); o.ch = c; qs.push(o); }); });
        qcm(z, melange(qs).slice(0, 15), true);
      } else {
        var fc = []; chaps().forEach(function (c) { fc = fc.concat(CHAPS[c].fc); });
        (portee === "tout" ? Object.keys(DOSSIERS) : DOSSIERS[portee] ? [portee] : []).forEach(function (t) { (DOSSIERS[t].frise || []).forEach(function (e) { fc.push(["Date : " + sans(e[3]), e[1] + " — " + e[4]]); }); });
        cartesMemoire(z, fc);
      }
    }
    $$("#portee button").forEach(function (b) {
      b.addEventListener("click", function () {
        portee = b.getAttribute("data-p");
        $$("#portee button").forEach(function (x) { var on = x === b; x.setAttribute("aria-pressed", on); x.style.background = on ? "var(--encre)" : ""; x.style.color = on ? "var(--papier)" : ""; });
        lance();
      });
    });
    $$(".onglets button").forEach(function (b) { b.addEventListener("click", function () { mode = b.getAttribute("data-o"); $$(".onglets button").forEach(function (x) { x.setAttribute("aria-selected", x === b); }); lance(); }); });
    lance();
  }

  /* ---------------- recherche plein écran ---------------- */
  var INDEX = null;
  function construireIndex() {
    INDEX = [];
    ORDRE.forEach(function (id) {
      var c = CHAPS[id];
      INDEX.push({ t: c.t, s: c.code, x: c.ess.join(" "), h: "#" + id });
      c.secs.forEach(function (s, k) { s.idees.forEach(function (d, j) { INDEX.push({ t: d.t, s: c.code + " · § " + (k + 1) + "." + (j + 1), x: d.h + " " + (d.ex || ""), h: "#" + id + "@" + (k + 1) + "-" + (j + 1) }); }); });
      c.fc.forEach(function (f) { INDEX.push({ t: f[0], s: "Carte mémoire · " + c.code, x: f[1], h: "#" + id + "@fiche" }); });
    });
    Object.keys(DOSSIERS).forEach(function (t) {
      DOSSIERS[t].notions.forEach(function (n) { INDEX.push({ t: n[0], s: "Notion · thème " + t.slice(1), x: n[1], h: "#" + t + ":plan" }); });
      DOSSIERS[t].frise.forEach(function (e) { INDEX.push({ t: e[3] + " (" + e[1] + ")", s: "Frise · thème " + t.slice(1), x: e[4], h: "#" + t + ":frise" }); });
    });
    THEMES.forEach(function (t) { INDEX.push({ t: "Thème " + t.n + " · " + t.titre, s: t.statut === "redige" ? "Dossier" : "Bientôt", x: t.obj + " " + [t.intro].concat(t.axes, [t.otc]).map(function (b) { return b.t + " " + b.j.join(" "); }).join(" "), h: "#" + t.id }); });
    INDEX.push({ t: "L'épreuve écrite", s: "Bac", x: "durée 4 heures coefficient 16 dissertation étude critique grand oral thèmes évaluables 2027", h: "#epreuve" });
    INDEX.forEach(function (e) { e.n = norm(e.t + " " + e.x); e.nt = norm(e.t); });
  }
  function chercher(q) {
    var res = $("#srch-res"), mots = norm(q).split(/\s+/).filter(function (m) { return m.length > 1; });
    if (!mots.length) { res.innerHTML = '<p class="vide">' + typo("Tape un mot : « ZEE », « Westphalie », « Daech », « 1967 »…") + '</p>'; return; }
    if (!INDEX) construireIndex();
    var trouv = INDEX.filter(function (e) { return mots.every(function (m) { return e.n.indexOf(m) >= 0; }); });
    trouv.sort(function (a, b) { var sa = mots.filter(function (m) { return a.nt.indexOf(m) >= 0; }).length, sb = mots.filter(function (m) { return b.nt.indexOf(m) >= 0; }).length; return sb - sa; });
    if (!trouv.length) { res.innerHTML = '<p class="vide">Aucun résultat.</p>'; return; }
    res.innerHTML = trouv.slice(0, 40).map(function (e) {
      var txt = sans(e.x), nt = norm(txt), p = nt.indexOf(mots[0]), d = Math.max(0, p - 50), ext = (d > 0 ? "…" : "") + txt.slice(d, d + 150) + (txt.length > d + 150 ? "…" : "");
      return '<a href="' + e.h + '" data-h="' + e.h + '"><small>' + esc(e.s) + '</small><b>' + marque(sans(e.t), mots) + '</b><span>' + marque(ext, mots) + '</span></a>';
    }).join("");
  }
  function marque(s, mots) {
    var out = esc(s), n = norm(s);
    var plages = [];
    mots.forEach(function (m) { var i = n.indexOf(m); if (i >= 0) plages.push([i, i + m.length]); });
    if (!plages.length) return out;
    plages.sort(function (a, b) { return b[0] - a[0]; });
    var r = s;
    plages.forEach(function (p) { r = r.slice(0, p[0]) + "\u0001" + r.slice(p[0], p[1]) + "\u0002" + r.slice(p[1]); });
    return esc(r).replace(/\u0001/g, "<mark>").replace(/\u0002/g, "</mark>");
  }
  var srchOuvert = false, cibleApres = null;
  function ouvrirRecherche() {
    if (srchOuvert) return;
    srchOuvert = true;
    $("#srch").classList.add("on");
    history.pushState({ srch: 1 }, "");
    var i = $("#sq"); i.value = ""; chercher(""); i.focus();
  }
  function fermerRecherche() { if (srchOuvert) history.back(); }
  window.addEventListener("popstate", function () {
    if (!srchOuvert) return;
    srchOuvert = false;
    $("#srch").classList.remove("on");
    if (cibleApres) { var c = cibleApres; cibleApres = null; setTimeout(function () { if (location.hash === c) route(); else location.hash = c; }, 0); }
  });

  /* ---------------- démarrage ---------------- */
  function demarrer() {
    construireNav();
    $("#menu-btn").addEventListener("click", ouvrirNav);
    $("#voile-nav").addEventListener("click", fermerNav);
    $("#q").addEventListener("click", ouvrirRecherche);
    $("#srch-fermer").addEventListener("click", function () { fermerRecherche(); });
    $("#sq").addEventListener("input", function () { chercher(this.value); });
    $("#srch").addEventListener("click", function (e) {
      var a = e.target.closest("a[data-h]");
      if (a) { e.preventDefault(); cibleApres = a.getAttribute("data-h"); fermerRecherche(); return; }
      if (e.target === this) fermerRecherche();
    });
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); ouvrirRecherche(); }
      else if (e.key === "/" && !srchOuvert && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); ouvrirRecherche(); }
      else if (e.key === "Escape") { if (srchOuvert) fermerRecherche(); else fermerNav(); }
    });
    $("#theme-btn").addEventListener("click", function () {
      var r = document.documentElement, sombre = r.getAttribute("data-theme") ? r.getAttribute("data-theme") === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      r.setAttribute("data-theme", sombre ? "light" : "dark");
      $("#theme-btn").setAttribute("aria-label", sombre ? "Passer en mode sombre" : "Passer en mode clair");
    });
    window.addEventListener("afterprint", function () { document.documentElement.classList.remove("impr"); });
    window.addEventListener("hashchange", route);
    route();
    if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(function () {});
  }
  demarrer();
})();
