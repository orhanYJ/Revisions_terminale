(function () {
  "use strict";
  var D = window.HLP;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var main = $("#main");
  var reduit = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduit) document.documentElement.classList.add("mo");

  /* ---------- typographie française ---------- */
  function ty(h) {
    return h.replace(/(^|>)([^<]+)/g, function (m, a, t) {
      return a + t.replace(/ ([;:!?»])/g, " $1").replace(/« /g, "« ").replace(/([0-9]) (?=[0-9]{3}\b)/g, "$1 ");
    });
  }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function ico(n) { return '<svg viewBox="0 0 24 24" aria-hidden="true">' + (D.ICONES[n] || "") + "</svg>"; }
  var ORN = '<div class="orn" aria-hidden="true"><svg viewBox="0 0 46 14"><path d="M23 2a5 5 0 1 0 4 8 4 4 0 1 1-4-8z" fill="currentColor"/><circle cx="9" cy="7" r="1.3" fill="currentColor"/><circle cx="37" cy="7" r="1.3" fill="currentColor"/></svg></div>';

  function entree(id) { for (var i = 0; i < D.ENTREES.length; i++) if (D.ENTREES[i].id === id) return D.ENTREES[i]; return null; }

  /* ---------- menu ---------- */
  var menu = $("#menu"), voileM = $("#voile-menu");
  function construireMenu() {
    var h = '<div class="m-tete">' + D.LOGO + '<div><b>L’Heure bleue</b><small>HLP · Terminale</small></div></div>';
    h += '<a href="#accueil" data-r="accueil">' + ico("lune") + "Accueil</a>";
    h += "<h6>Semestre 1 · La recherche de soi</h6>";
    D.ENTREES.forEach(function (e) { h += '<a href="#' + e.id + '" data-r="' + e.id + '"><span class="num">' + e.num + "</span>" + e.titre + "</a>"; });
    h += "<h6>Semestre 2 · L’Humanité en question</h6>";
    D.S2.forEach(function (e) { h += '<a href="#s2" data-r="s2-' + e.num + '"><span class="num">' + e.num + "</span>" + e.titre + '<span class="bientot">Bientôt</span></a>'; });
    h += "<h6>Méthode & outils</h6>";
    [["epreuve", "plume", "L’épreuve"], ["atelier", "loupe", "Atelier de lecture"], ["qui", "guillemets", "Qui a écrit ?"], ["frise", "sablier", "Frise 1750-1950"],
      ["notions", "constellation", "Tableau des notions"], ["entrainement", "cible", "Entraînement"], ["ressources", "livres", "Ressources"]].forEach(function (x) {
      h += '<a href="#' + x[0] + '" data-r="' + x[0] + '">' + ico(x[1]) + x[2] + "</a>";
    });
    menu.innerHTML = h;
  }
  function ouvrirMenu(o) {
    menu.classList.toggle("ouvert", o); voileM.classList.toggle("on", o);
    $("#btn-menu").setAttribute("aria-expanded", o ? "true" : "false");
  }
  $("#btn-menu").addEventListener("click", function () { ouvrirMenu(!menu.classList.contains("ouvert")); });
  voileM.addEventListener("click", function () { ouvrirMenu(false); });
  menu.addEventListener("click", function (e) { if (e.target.closest("a")) ouvrirMenu(false); });

  /* ---------- thème (non mémorisé) ---------- */
  $("#btn-theme").addEventListener("click", function () {
    var r = document.documentElement, sombre = r.getAttribute("data-theme") ? r.getAttribute("data-theme") === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    r.setAttribute("data-theme", sombre ? "light" : "dark");
    var m = document.querySelector('meta[name="theme-color"]'); if (m) m.setAttribute("content", sombre ? "#f4eedf" : "#11172a");
  });

  /* ---------- pages ---------- */
  var PAGES = {};
  PAGES.accueil = function () {
    var h = '<section class="ciel">' + D.CIEL + '<div class="txt"><p class="sous">Humanités, littérature et philosophie · Terminale</p><h1>L’Heure bleue</h1>' +
      '<p class="acc">Le cabinet de lecture du soir, pour réviser la spécialité HLP : des textes, des idées, et la méthode pour en faire une copie.</p>' +
      '<div class="rang"><a class="btn plein" href="#e1">Commencer le semestre 1</a><a class="btn" href="#epreuve">L’épreuve</a></div></div></section>';
    h += '<div class="lecture"><p class="lettrine" style="margin-top:22px">' + D.ACCUEIL_INTRO + "</p></div>";
    h += '<section class="semestre"><h2>Semestre 1 — La recherche de soi <small>du romantisme au XX<sup>e</sup> siècle</small></h2><div class="grille g3">';
    D.ENTREES.forEach(function (e) {
      h += '<a class="entree-c" href="#' + e.id + '"><span class="chiffre">' + D.CHIFFRES[e.num] + '</span><h3>' + e.titre + "</h3><p>" + e.accroche + '</p><span class="etat tag ' + e.id + '">Rédigé</span></a>';
    });
    h += '</div></section><section class="semestre"><h2>Semestre 2 — L’Humanité en question <small>période contemporaine (XX<sup>e</sup>-XXI<sup>e</sup> siècles)</small></h2><div class="grille g3">';
    D.S2.forEach(function (e) {
      h += '<a class="entree-c bientot" href="#s2"><span class="chiffre">' + D.CHIFFRES[e.num] + '</span><h3>' + e.titre + "</h3><p>" + e.accroche + '</p><span class="etat tag">Bientôt</span></a>';
    });
    h += "</div></section>" + ORN + "<h2>Accès rapide</h2><div class='acces'>";
    [["epreuve", "plume", "L’épreuve", "Format 2027, méthode, copie commentée"], ["atelier", "loupe", "Atelier de lecture", "Surligne les procédés d’un texte"],
      ["qui", "guillemets", "Qui a écrit ?", "Une citation, quatre auteurs"], ["frise", "sablier", "La frise", "Des Lumières à 1950"],
      ["notions", "constellation", "Les notions", "Définitions et distinctions"], ["entrainement", "cible", "Entraînement", "QCM mélangé et cartes"],
      ["ressources", "livres", "Ressources", "Programme, annales, textes"], ["s2", "eclipse", "Semestre 2", "Ce qui t’attend"]].forEach(function (x) {
      h += '<a href="#' + x[0] + '">' + ico(x[1]) + "<b>" + x[2] + "</b><small>" + x[3] + "</small></a>";
    });
    h += "</div>" + D.ACCUEIL_BAS;
    return h;
  };

  var ONGLETS = [["", "Cours"], ["textes", "Textes clés"], ["sujet", "Sujet type bac"], ["qcm", "QCM"], ["cartes", "Cartes mémoire"], ["fiche", "À retenir"]];
  function pageEntree(e, sous) {
    var h = '<header class="page-entete"><p class="surtitre">Semestre 1 · La recherche de soi · Entrée ' + e.num + "</p><h1>" + e.titre + '</h1><p class="chapo">' + e.chapo + "</p></header>";
    h += '<nav class="onglets non-imp" aria-label="Parties de l’entrée">';
    ONGLETS.forEach(function (o) { h += '<a href="#' + e.id + (o[0] ? "/" + o[0] : "") + '"' + (sous === o[0] ? ' class="actif" aria-current="page"' : "") + ">" + o[1] + "</a>"; });
    h += "</nav><div class='entre'>";
    if (!sous) h += coursHTML(e);
    else if (sous === "textes") h += textesHTML(e);
    else if (sous === "sujet") h += sujetHTML(e);
    else if (sous === "qcm") h += '<p class="lecture">Douze questions sur les idées du cours. Chaque réponse est expliquée, avec un lien pour revoir le paragraphe.</p><div id="qcm-zone"></div>';
    else if (sous === "cartes") h += '<p class="lecture">Touche la carte pour la retourner. Les citations sont exactes, avec leur référence.</p><div id="fc-zone"></div>';
    else if (sous === "fiche") h += ficheHTML(e);
    h += "</div>";
    return h;
  }
  function coursHTML(e) {
    var h = '<div class="lecture"><section class="essentiel"><h2>L’essentiel en 5 lignes</h2><ol>' + e.essentiel.map(function (l) { return "<li>" + l + "</li>"; }).join("") + "</ol></section>";
    h += '<section class="cadre-prog"><h3>Ce que le programme attend</h3><ul class="puces">' + e.attendus.map(function (l) { return "<li>" + l + "</li>"; }).join("") + "</ul></section>";
    h += "<h2>Les problématiques</h2><ul class='puces'>" + e.problematiques.map(function (l) { return "<li><i>" + l + "</i></li>"; }).join("") + "</ul>";
    h += e.schema ? '<figure class="schema" data-schema>' + e.schema + "</figure>" : "";
    h += ORN + "<h2>Le cours</h2>";
    e.cours.forEach(function (c, i) {
      h += '<section class="idee" id="' + c.id + '"><h3><span class="n">' + (i + 1) + ".</span><span>" + c.titre + "</span></h3>" + c.html + "</section>";
    });
    h += ORN + "<h2>Les notions à manier</h2><dl class='defs'>" + e.notions.map(function (n) { return "<dt>" + n[0] + "</dt><dd>" + n[1] + "</dd>"; }).join("") + "</dl>";
    h += "<h2>Repères chronologiques</h2><div class='defile'><table class='t'><thead><tr><th>Date</th><th>Repère</th></tr></thead><tbody>" +
      e.reperes.map(function (r) { return "<tr><td style='white-space:nowrap'><b>" + r[0] + "</b></td><td>" + r[1] + "</td></tr>"; }).join("") + "</tbody></table></div>";
    h += "<h2>Les pièges</h2>" + e.pieges.map(function (p) { return '<div class="attention"><b class="l">Piège</b>' + p + "</div>"; }).join("");
    h += '<div class="rang non-imp"><a class="btn plein" href="#' + e.id + '/textes">Lire les textes clés</a><a class="btn" href="#' + e.id + '/qcm">Faire le QCM</a></div></div>';
    return h;
  }
  function textesHTML(e) {
    var h = '<div class="lecture"><p>' + e.textesIntro + "</p>";
    e.textes.forEach(function (t) {
      h += '<article class="texte" id="' + t.id + '"><header><h3>' + t.auteur + " — <i>" + t.oeuvre + '</i></h3><span class="ref">' + t.ref + "</span></header>" +
        (t.extrait ? '<blockquote class="extrait' + (t.vers ? " vers" : "") + '">' + t.extrait + "</blockquote>" : "") +
        '<div class="corps"><h4>Contexte</h4><p>' + t.contexte + "</p><h4>Analyse littéraire</h4>" + t.analyse + "<h4>Enjeu philosophique</h4>" + t.enjeu +
        "<h4>Liens avec d’autres œuvres</h4><p>" + t.liens + "</p></div></article>";
    });
    return h + "</div>";
  }
  function sujetHTML(e) {
    var s = e.sujet;
    var h = '<div class="lecture"><p class="mute petit">Sujet <b>inventé pour le site</b> sur le modèle officiel (session 2027) : un texte, deux questions notées chacune sur 10, à traiter sur deux copies séparées. Durée conseillée : 2 heures par question.</p>';
    h += '<div class="sujet"><div class="en-tete-bac">Baccalauréat général · Humanités, littérature et philosophie · Sujet d’entraînement</div>' +
      (s.chapeau ? '<p class="petit mute"><i>' + s.chapeau + "</i></p>" : "") +
      '<ol class="lignes">' + s.texte.map(function (l) { return "<li>" + l + "</li>"; }).join("") + '</ol><p class="ref" style="text-align:right">' + s.ref + "</p>" +
      (s.notes ? '<p class="petit mute">' + s.notes + "</p>" : "") +
      '<div class="q"><b>Première partie : ' + s.q1.type + "</b>" + s.q1.q + '</div><div class="q"><b>Deuxième partie : ' + s.q2.type + "</b>" + s.q2.q + "</div></div>";
    [["q1", "Corrigé de la première partie"], ["q2", "Corrigé de la deuxième partie"]].forEach(function (k) {
      var c = s[k[0]];
      h += "<h2>" + k[1] + " <small class='mute'>(" + c.type + ")</small></h2>";
      h += '<details class="pli"><summary>La méthode pour cette question</summary><div class="dedans">' + c.methode + "</div></details>";
      h += "<h3>Introduction rédigée</h3><div class='redige'>" + c.intro + "</div>";
      h += "<h3>Plan détaillé</h3><ol class='plan-l'>" + c.plan.map(function (p) { return "<li><b>" + p[0] + "</b>" + p[1] + "</li>"; }).join("") + "</ol>";
      h += "<h3>Conclusion rédigée</h3><div class='redige'>" + c.concl + "</div>";
    });
    return h + "</div>";
  }
  function ficheHTML(e) {
    return '<div class="lecture fiche carte"><div class="rang non-imp" style="justify-content:flex-end"><button class="btn" data-imprimer>' + ico("imprimer") + "Imprimer la fiche</button></div>" +
      "<h2>" + e.titre + "</h2><p class='mute petit'>L’Heure bleue · HLP Terminale · Semestre 1, entrée " + e.num + "</p>" + e.retenir + "</div>";
  }

  PAGES.s2 = function () {
    var h = '<header class="page-entete"><p class="surtitre">Semestre 2 · Bientôt</p><h1>L’Humanité en question</h1><p class="chapo">' + D.S2_CHAPO + "</p></header><div class='lecture entre'>";
    D.S2.forEach(function (e) {
      h += '<section class="carte"><p class="surtitre">Entrée ' + e.num + " · Bientôt</p><h2 style='margin-top:0'>" + e.titre + "</h2><p>" + e.resume + "</p><h3>Les questions du programme</h3><ul class='puces'>" +
        e.questions.map(function (q) { return "<li><i>" + q + "</i></li>"; }).join("") + "</ul><h3>Œuvres citées par la bibliographie officielle (extraits)</h3><p class='petit'>" + e.oeuvres + "</p>" +
        (e.annales ? "<h3>Déjà tombé au bac</h3><p class='petit'>" + e.annales + "</p>" : "") + "</section>";
    });
    return h + "</div>";
  };
  PAGES.epreuve = function () { return D.EPREUVE; };
  PAGES.ressources = function () { return D.RESSOURCES; };
  PAGES.frise = function () {
    var h = '<header class="page-entete"><p class="surtitre">Repères</p><h1>La frise, des Lumières à 1950</h1><p class="chapo">La période de référence du semestre 1 va « du romantisme au XX<sup>e</sup> siècle ». Ces repères permettent de situer un texte inconnu le jour de l’épreuve.</p></header>';
    h += '<div class="rang" role="group" aria-label="Filtrer"><button class="puce-f" data-ff="" aria-pressed="true">Tout</button><button class="puce-f" data-ff="e1" aria-pressed="false">Éducation</button><button class="puce-f" data-ff="e2" aria-pressed="false">Sensibilité</button><button class="puce-f" data-ff="e3" aria-pressed="false">Moi</button><button class="puce-f" data-ff="hist" aria-pressed="false">Histoire</button></div>';
    h += '<div class="frise lecture" id="frise">';
    D.FRISE.forEach(function (p) {
      h += '<div class="periode">' + p.nom + "<small>" + p.dates + " — " + p.def + "</small></div>";
      p.evts.forEach(function (ev) {
        h += '<div class="evt' + (ev[2] === "hist" ? " hist" : "") + '" data-f="' + ev[2] + '"><span class="an">' + ev[0] + "</span>" + ev[1] + "</div>";
      });
    });
    return h + "</div>";
  };
  PAGES.notions = function () {
    var h = '<header class="page-entete"><p class="surtitre">Outils</p><h1>Tableau des notions</h1><p class="chapo">Les mots qu’un correcteur attend, avec leur définition et la distinction qui les rend utiles dans une copie.</p></header>';
    h += '<div class="lecture"><label class="sr" for="filtre-n">Filtrer les notions</label><input id="filtre-n" class="champ" type="search" placeholder="Filtrer (ex. sincérité, sublime…)" autocomplete="off">' +
      '<div class="rang" role="group" aria-label="Entrée"><button class="puce-f" data-fn="" aria-pressed="true">Toutes</button><button class="puce-f" data-fn="e1" aria-pressed="false">Éducation</button><button class="puce-f" data-fn="e2" aria-pressed="false">Sensibilité</button><button class="puce-f" data-fn="e3" aria-pressed="false">Moi</button></div><div class="notion-l" id="liste-n"></div></div>';
    return h;
  };
  function remplirNotions() {
    var l = $("#liste-n"); if (!l) return;
    var q = norm($("#filtre-n").value), f = ($(".puce-f[data-fn][aria-pressed='true']") || {}).getAttribute ? $(".puce-f[data-fn][aria-pressed='true']").getAttribute("data-fn") : "";
    var h = "";
    D.NOTIONS.forEach(function (n) {
      if (f && n.e.indexOf(f) < 0) return;
      if (q && norm(n.n + " " + n.d + " " + n.dist + " " + n.a).indexOf(q) < 0) return;
      h += '<div class="notion"><h3>' + n.n + " " + n.e.map(function (x) { return '<span class="tag ' + x + '">' + (x === "e1" ? "Éducation" : x === "e2" ? "Sensibilité" : "Moi") + "</span>"; }).join("") +
        "</h3><p style='margin:.2em 0'>" + n.d + '</p><p class="dist">' + n.dist + '</p><p class="ref">' + n.a + "</p></div>";
    });
    l.innerHTML = ty(h || "<p class='mute'>Aucune notion ne correspond.</p>");
  }
  PAGES.atelier = function () {
    var h = '<header class="page-entete"><p class="surtitre">Méthode</p><h1>Atelier de lecture</h1><p class="chapo">Touche un passage surligné : la note explique le procédé et ce qu’il produit. Les couleurs marquent les mouvements du texte, le pointillé les procédés.</p></header>';
    h += '<div class="lecture"><div class="rang" role="group" aria-label="Texte">' + D.ATELIER.map(function (t, i) { return '<button class="puce-f" data-at="' + i + '" aria-pressed="' + (i === 0) + '">' + t.court + "</button>"; }).join("") + "</div>";
    h += '<div class="rang" role="group" aria-label="Calques"><span class="mute ui petit">Afficher :</span><button class="puce-f" data-cal="m" aria-pressed="true">Mouvements</button><button class="puce-f" data-cal="p" aria-pressed="true">Procédés</button></div><div id="atelier-zone"></div></div>';
    return h;
  };
  function remplirAtelier(i) {
    var t = D.ATELIER[i], z = $("#atelier-zone"); if (!z) return;
    var h = "<h2>" + t.titre + '</h2><p class="ref">' + t.ref + "</p>";
    h += '<p class="mute petit">' + t.aide + "</p>";
    h += '<div class="legende-m">' + t.mouvements.map(function (m, k) { return '<span><i style="background:var(--t-m' + (k + 1) + ')"></i>' + m + "</span>"; }).join("") + "</div>";
    h += '<div class="atelier-txt" id="at-txt">';
    t.segs.forEach(function (s, k) {
      if (typeof s === "string") { h += s; return; }
      h += '<span class="seg-a" role="button" tabindex="0" data-k="' + k + '" data-m="' + (s.m || "") + '"' + (s.p ? ' data-p="1"' : "") + ">" + s.t + "</span>";
    });
    h += '</div><div class="note-a" id="note-a" aria-live="polite" hidden></div>';
    h += "<h3>Bilan : ce que le texte fait</h3>" + t.bilan;
    z.innerHTML = ty(h);
    appliquerCalques();
  }
  function appliquerCalques() {
    var x = $("#at-txt"); if (!x) return;
    x.classList.toggle("calques-m", $(".puce-f[data-cal='m']").getAttribute("aria-pressed") === "true");
    x.classList.toggle("calques-p", $(".puce-f[data-cal='p']").getAttribute("aria-pressed") === "true");
  }
  PAGES.qui = function () {
    return '<header class="page-entete"><p class="surtitre">Jeu de mémoire</p><h1>Qui a écrit ?</h1><p class="chapo">Une citation exacte, quatre auteurs. Le jour de l’épreuve, une citation bien attribuée vaut plus qu’une longue paraphrase.</p></header><div class="lecture" id="qui-zone"></div>';
  };
  PAGES.entrainement = function () {
    return '<header class="page-entete"><p class="surtitre">Révisions</p><h1>Entraînement</h1><p class="chapo">Un QCM tiré au hasard dans les trois entrées du semestre 1, puis toutes les cartes mémoire mélangées.</p></header>' +
      '<div class="lecture"><h2>QCM mélangé</h2><div id="qcm-zone"></div>' + ORN + '<h2>Cartes mémoire</h2><div class="rang" role="group" aria-label="Type de cartes"><button class="puce-f" data-fct="" aria-pressed="true">Toutes</button><button class="puce-f" data-fct="notion" aria-pressed="false">Notions</button><button class="puce-f" data-fct="citation" aria-pressed="false">Citations</button><button class="puce-f" data-fct="date" aria-pressed="false">Dates & œuvres</button></div><div id="fc-zone"></div></div>';
  };

  /* ---------- QCM ---------- */
  function lancerQCM(zone, questions) {
    var i = 0, bons = 0, q = questions;
    function rendre() {
      if (i >= q.length) {
        zone.innerHTML = ty('<div class="qcm"><p class="surtitre">Résultat</p><p class="score">' + bons + " / " + q.length + "</p><p>" +
          (bons === q.length ? "Parfait. Passe aux cartes mémoire pour fixer les citations." : bons >= q.length * 0.7 ? "Solide. Relis les paragraphes des questions manquées." : "Reprends le cours, puis recommence : les explications te guident.") +
          '</p><div class="bas"><button class="btn plein" data-qcm-re>Recommencer</button></div></div>');
        return;
      }
      var x = q[i], ordre = melange(x.c.map(function (c, k) { return k; }));
      var h = '<div class="qcm"><div class="prog"><span>Question ' + (i + 1) + " / " + q.length + '</span><span class="barre"><i style="width:' + Math.round(i / q.length * 100) + '%"></i></span><span>' + bons + " ✓</span></div>" +
        '<p class="question">' + x.q + '</p><div class="choix">' + ordre.map(function (k) { return '<button data-k="' + k + '">' + x.c[k] + "</button>"; }).join("") + "</div><div class='zone-e'></div></div>";
      zone.innerHTML = ty(h);
    }
    zone.onclick = function (ev) {
      var b = ev.target.closest(".choix button");
      if (b && !b.disabled) {
        var x = q[i], k = +b.getAttribute("data-k"), ok = k === x.r;
        if (ok) bons++;
        $$(".choix button", zone).forEach(function (bb) { bb.disabled = true; var kk = +bb.getAttribute("data-k"); if (kk === x.r) bb.classList.add("bon"); else if (bb === b) bb.classList.add("faux"); });
        var e = x.ref ? x.ref.split("-")[0] : "";
        $(".zone-e", zone).innerHTML = ty('<div class="expl"><b>' + (ok ? "Exact." : "Non.") + "</b> " + x.e + (x.ref ? ' <br><a href="#' + e + '" data-goto="' + x.ref + '">Revoir le paragraphe →</a>' : "") +
          '</div><div class="bas"><span></span><button class="btn plein" data-suiv>' + (i + 1 < q.length ? "Question suivante" : "Voir le résultat") + "</button></div>");
        return;
      }
      if (ev.target.closest("[data-suiv]")) { i++; rendre(); zone.scrollIntoView({ block: "nearest" }); return; }
      if (ev.target.closest("[data-qcm-re]")) { i = 0; bons = 0; q = melange(questions); rendre(); }
    };
    rendre();
  }

  /* ---------- cartes mémoire ---------- */
  function lancerCartes(zone, cartes) {
    var i = 0, l = melange(cartes), su = 0, rev = 0;
    function rendre() {
      var c = l[i];
      zone.innerHTML = ty('<div class="fc-zone"><button class="fc" aria-label="Retourner la carte"><span class="face recto"><small>' + c.cat + "</small>" + c.r + '</span><span class="face verso"><small>Réponse</small>' + c.v + "</span></button></div>" +
        '<div class="fc-nav"><button class="btn" data-fc="prec" ' + (i === 0 ? "disabled" : "") + '>←</button><span class="mute ui petit">' + (i + 1) + " / " + l.length + " · " + su + " sues · " + rev + ' à revoir</span><button class="btn" data-fc="suiv">→</button></div>' +
        '<div class="rang" style="justify-content:center"><button class="btn" data-fc="rev">À revoir</button><button class="btn plein" data-fc="su">Je savais</button></div>');
    }
    zone.onclick = function (ev) {
      var f = ev.target.closest(".fc"); if (f) { f.classList.toggle("tourne"); return; }
      var b = ev.target.closest("[data-fc]"); if (!b) return;
      var a = b.getAttribute("data-fc");
      if (a === "su") su++; if (a === "rev") { rev++; l.push(l[i]); }
      if (a === "prec") i = Math.max(0, i - 1); else i = (i + 1) % l.length;
      rendre();
    };
    rendre();
  }
  function toutesCartes() {
    var t = [];
    D.ENTREES.forEach(function (e) { e.cartes.forEach(function (c) { t.push(c); }); });
    return t;
  }

  /* ---------- qui a écrit ---------- */
  function lancerQui() {
    var z = $("#qui-zone"); if (!z) return;
    var l = melange(D.QUI), i = 0, bons = 0, serie = 0;
    var auteurs = []; D.QUI.forEach(function (x) { if (auteurs.indexOf(x.a) < 0) auteurs.push(x.a); });
    function rendre() {
      var x = l[i % l.length];
      var autres = melange(auteurs.filter(function (a) { return a !== x.a; })).slice(0, 3);
      var choix = melange(autres.concat([x.a]));
      z.innerHTML = ty('<div class="qui-c"><p class="surtitre">Citation ' + (i + 1) + " · " + bons + " bonnes réponses · série " + serie + "</p><blockquote>" + x.c + '</blockquote><div class="choix">' +
        choix.map(function (a) { return "<button data-a=\"" + esc(a) + "\">" + a + "</button>"; }).join("") + '</div><div class="zone-e"></div></div>');
    }
    z.onclick = function (ev) {
      var b = ev.target.closest(".choix button");
      if (b && !b.disabled) {
        var x = l[i % l.length], ok = b.getAttribute("data-a") === x.a;
        if (ok) { bons++; serie++; } else serie = 0;
        $$(".choix button", z).forEach(function (bb) { bb.disabled = true; if (bb.getAttribute("data-a") === x.a) bb.classList.add("bon"); else if (bb === b) bb.classList.add("faux"); });
        $(".zone-e", z).innerHTML = ty('<p style="margin-top:14px"><b>' + x.a + "</b>, <i>" + x.o + "</i> (" + x.d + ").<br><span class='mute petit'>" + x.e + '</span></p><button class="btn plein" data-qs>Citation suivante</button>');
        return;
      }
      if (ev.target.closest("[data-qs]")) { i++; rendre(); }
    };
    rendre();
  }

  /* ---------- recherche ---------- */
  var INDEX = null;
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/<[^>]+>/g, " ").replace(/[’']/g, " "); }
  function brut(s) { return String(s || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim(); }
  function construireIndex() {
    INDEX = [];
    D.ENTREES.forEach(function (e) {
      INDEX.push({ t: e.titre, c: "Entrée " + e.num, h: "#" + e.id, x: brut(e.chapo + " " + e.essentiel.join(" ")) });
      e.cours.forEach(function (c) { INDEX.push({ t: c.titre, c: e.titre, h: "#" + e.id, g: c.id, x: brut(c.html) }); });
      e.textes.forEach(function (t) { INDEX.push({ t: t.auteur + ", " + brut(t.oeuvre), c: "Texte clé · " + e.titre, h: "#" + e.id + "/textes", g: t.id, x: brut(t.extrait + " " + t.contexte + " " + t.analyse) }); });
      e.notions.forEach(function (n) { INDEX.push({ t: brut(n[0]), c: "Notion · " + e.titre, h: "#" + e.id, x: brut(n[1]) }); });
      INDEX.push({ t: "Sujet type bac : " + brut(e.sujet.ref), c: e.titre, h: "#" + e.id + "/sujet", x: brut(e.sujet.q1.q + " " + e.sujet.q2.q) });
    });
    D.NOTIONS.forEach(function (n) { INDEX.push({ t: brut(n.n), c: "Tableau des notions", h: "#notions", x: brut(n.d + " " + n.dist + " " + n.a) }); });
    D.FRISE.forEach(function (p) { p.evts.forEach(function (ev) { INDEX.push({ t: ev[0] + " — " + brut(ev[1]).slice(0, 80), c: "Frise · " + brut(p.nom), h: "#frise", x: brut(ev[1]) }); }); });
    D.S2.forEach(function (e) { INDEX.push({ t: e.titre, c: "Semestre 2 · Bientôt", h: "#s2", x: brut(e.resume + " " + e.questions.join(" ")) }); });
    D.QUI.forEach(function (q) { INDEX.push({ t: "« " + brut(q.c) + " »", c: "Citation · " + q.a, h: "#qui", x: q.a + " " + q.o }); });
    D.PAGES_IDX.forEach(function (p) { INDEX.push(p); });
    INDEX.forEach(function (it) { it.n = norm(it.t + " " + it.c + " " + it.x); it.nt = norm(it.t); });
  }
  var srch = $("#srch"), sq = $("#sq"), sres = $("#sres"), srchOuvert = false;
  function ouvrirRecherche() {
    if (srchOuvert) return;
    if (!INDEX) construireIndex();
    srchOuvert = true; srch.classList.add("on");
    history.pushState({ srch: 1 }, "");
    sq.value = ""; sres.innerHTML = '<p class="mute">Tape un auteur, une œuvre, une notion, une date…</p>';
    setTimeout(function () { sq.focus(); }, 30);
  }
  function fermerRecherche(depuisPop) {
    if (!srchOuvert) return;
    srchOuvert = false; srch.classList.remove("on");
    if (!depuisPop && history.state && history.state.srch) history.back();
  }
  var minuteur = null;
  sq.addEventListener("input", function () {
    clearTimeout(minuteur);
    minuteur = setTimeout(function () {
      var q = norm(sq.value).trim();
      if (q.length < 2) { sres.innerHTML = '<p class="mute">Au moins deux lettres.</p>'; return; }
      var mots = q.split(/\s+/), r = [];
      INDEX.forEach(function (it) {
        var ok = mots.every(function (m) { return it.n.indexOf(m) >= 0; }); if (!ok) return;
        var sc = mots.reduce(function (s, m) { return s + (it.nt.indexOf(m) >= 0 ? 3 : 1); }, 0);
        r.push([sc, it]);
      });
      r.sort(function (a, b) { return b[0] - a[0]; });
      if (!r.length) { sres.innerHTML = '<p class="mute">Rien trouvé. Essaie un autre mot.</p>'; return; }
      sres.innerHTML = ty(r.slice(0, 40).map(function (x, k) {
        var it = x[1], ex = "", nx = norm(it.x), p = nx.indexOf(mots[0]);
        if (p >= 0) { var d = Math.max(0, p - 50); ex = (d ? "…" : "") + esc(it.x.slice(d, p + 110)) + "…"; }
        return '<a href="' + it.h + '" data-res="' + k + '"' + (it.g ? ' data-g="' + it.g + '"' : "") + "><span>" + esc(it.c) + "</span><b>" + esc(it.t) + "</b>" + (ex ? "<small>" + ex + "</small>" : "") + "</a>";
      }).join(""));
    }, 120);
  });
  sres.addEventListener("click", function (ev) {
    var a = ev.target.closest("a"); if (!a) return;
    ev.preventDefault();
    srchOuvert = false; srch.classList.remove("on");
    allerA = a.getAttribute("data-g");
    history.replaceState(null, "", a.getAttribute("href"));
    router();
  });
  $("#btn-cherche").addEventListener("click", ouvrirRecherche);
  $("#srch-fermer").addEventListener("click", function () { fermerRecherche(false); });
  document.addEventListener("keydown", function (e) {
    if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && !/INPUT|TEXTAREA/.test(document.activeElement.tagName))) { e.preventDefault(); ouvrirRecherche(); }
    else if (e.key === "Escape") { if (srchOuvert) fermerRecherche(false); else if (menu.classList.contains("ouvert")) ouvrirMenu(false); }
  });
  window.addEventListener("popstate", function (e) { if (srchOuvert && !(e.state && e.state.srch)) fermerRecherche(true); });

  /* ---------- routeur ---------- */
  var allerA = null;
  function router() {
    var h = (location.hash || "#accueil").slice(1), parts = h.split("/"), r = parts[0] || "accueil", sous = parts[1] || "";
    var e = entree(r), html;
    if (e) html = pageEntree(e, ONGLETS.some(function (o) { return o[0] === sous; }) ? sous : "");
    else if (PAGES[r]) html = PAGES[r]();
    else { r = "accueil"; html = PAGES.accueil(); }
    main.innerHTML = ty(html) + '<footer class="pied">' + D.PIED + "</footer>";
    $$("#menu a").forEach(function (a) { var x = a.getAttribute("data-r"); a.classList.toggle("actif", x === r && r !== "s2"); if (x === r) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current"); });
    document.title = (e ? e.titre : (D.TITRES[r] || "Accueil")) + " · L’Heure bleue — HLP Terminale";
    if (e && sous === "qcm") lancerQCM($("#qcm-zone"), melange(e.qcm));
    if (e && sous === "cartes") lancerCartes($("#fc-zone"), e.cartes);
    if (r === "entrainement") {
      var tous = []; D.ENTREES.forEach(function (x) { x.qcm.forEach(function (q) { tous.push(q); }); });
      lancerQCM($("#qcm-zone"), melange(tous).slice(0, 15));
      lancerCartes($("#fc-zone"), toutesCartes());
    }
    if (r === "qui") lancerQui();
    if (r === "atelier") remplirAtelier(0);
    if (r === "notions") remplirNotions();
    if (r === "frise") observerFrise();
    observerSchemas();
    if (allerA) {
      var cible = document.getElementById(allerA); allerA = null;
      if (cible) {
        cible.scrollIntoView({ block: "start" });
        if (cible.classList.contains("idee")) { cible.classList.add("surligne"); setTimeout(function () { cible.classList.add("fini"); }, 60); }
        return;
      }
    }
    window.scrollTo(0, 0);
  }
  window.addEventListener("hashchange", router);

  /* ---------- délégation ---------- */
  main.addEventListener("click", function (ev) {
    var g = ev.target.closest("[data-goto]");
    if (g) { ev.preventDefault(); allerA = g.getAttribute("data-goto"); var hh = g.getAttribute("href"); if (location.hash === hh) router(); else location.hash = hh; return; }
    if (ev.target.closest("[data-imprimer]")) { window.print(); return; }
    var at = ev.target.closest("[data-at]");
    if (at) { $$("[data-at]").forEach(function (b) { b.setAttribute("aria-pressed", b === at ? "true" : "false"); }); remplirAtelier(+at.getAttribute("data-at")); return; }
    var cal = ev.target.closest("[data-cal]");
    if (cal) { cal.setAttribute("aria-pressed", cal.getAttribute("aria-pressed") === "true" ? "false" : "true"); appliquerCalques(); return; }
    var seg = ev.target.closest(".seg-a");
    if (seg) { montrerNote(seg); return; }
    var ff = ev.target.closest("[data-ff]");
    if (ff) {
      $$("[data-ff]").forEach(function (b) { b.setAttribute("aria-pressed", b === ff ? "true" : "false"); });
      var f = ff.getAttribute("data-ff");
      $$(".evt").forEach(function (x) { x.style.display = !f || x.getAttribute("data-f") === f ? "" : "none"; });
      return;
    }
    var fn = ev.target.closest("[data-fn]");
    if (fn) { $$("[data-fn]").forEach(function (b) { b.setAttribute("aria-pressed", b === fn ? "true" : "false"); }); remplirNotions(); return; }
    var fct = ev.target.closest("[data-fct]");
    if (fct) {
      $$("[data-fct]").forEach(function (b) { b.setAttribute("aria-pressed", b === fct ? "true" : "false"); });
      var c = fct.getAttribute("data-fct");
      lancerCartes($("#fc-zone"), toutesCartes().filter(function (x) { return !c || x.t === c; }));
    }
  });
  main.addEventListener("keydown", function (ev) { if ((ev.key === "Enter" || ev.key === " ") && ev.target.classList.contains("seg-a")) { ev.preventDefault(); montrerNote(ev.target); } });
  main.addEventListener("input", function (ev) { if (ev.target.id === "filtre-n") remplirNotions(); });
  function montrerNote(seg) {
    var i = +$(".puce-f[data-at][aria-pressed='true']").getAttribute("data-at"), t = D.ATELIER[i], s = t.segs[+seg.getAttribute("data-k")];
    $$(".seg-a.choisi").forEach(function (x) { x.classList.remove("choisi"); }); seg.classList.add("choisi");
    var n = $("#note-a"); n.hidden = false;
    n.innerHTML = ty("<h4>" + (s.m ? "Mouvement " + s.m + " · " : "") + (s.titre || "Note") + '</h4><p style="margin:0">' + s.n + "</p>");
    n.classList.remove("neuf"); void n.offsetWidth; n.classList.add("neuf");
  }

  /* ---------- mouvement ---------- */
  var io = ("IntersectionObserver" in window) && !reduit ? new IntersectionObserver(function (l) {
    l.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add(x.target.classList.contains("evt") ? "vu" : "joue"); io.unobserve(x.target); } });
  }, { rootMargin: "0px 0px -12% 0px" }) : null;
  function observerSchemas() {
    if (!io) return;
    $$("[data-schema]").forEach(function (f) {
      $$(".trace", f).forEach(function (p) { try { p.style.setProperty("--l", Math.ceil(p.getTotalLength()) + 1); } catch (e) {} });
      var r = f.getBoundingClientRect(); if (r.top > innerHeight * 0.88) io.observe(f);
    });
  }
  function observerFrise() {
    if (!io) return;
    $$(".evt").forEach(function (x) { if (x.getBoundingClientRect().top > innerHeight) io.observe(x); });
  }

  construireMenu();
  router();
  if ("serviceWorker" in navigator && location.protocol !== "file:") navigator.serviceWorker.register("sw.js").catch(function () {});
})();
