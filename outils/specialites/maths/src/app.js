/* ---------- CQFD — application ---------- */
(function () {
  "use strict";
  var D = document, H = D.documentElement;
  var reduit = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduit) H.classList.add("mo");
  var F = TeX.fmt;
  var $ = function (s, r) { return (r || D).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || D).querySelectorAll(s)); };
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function ic(n) { return ICONES[n] || ""; }
  var CH = window.CHAPITRES, PARCH = {};
  CH.forEach(function (c) { PARCH[c.id] = c; });
  var REDIGES = CH.filter(function (c) { return c.statut === "ok"; });

  /* ---------- Python : coloration ---------- */
  var KW = /\b(def|return|while|for|in|if|elif|else|import|from|and|or|not|True|False|None|range|print|len|append|abs|int|float|round|lambda)\b/;
  function pyHTML(code) {
    var out = "", re = /(#[^\n]*)|("[^"\n]*"|'[^'\n]*')|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_]\w*\b)|([\s\S])/g, m;
    while ((m = re.exec(code))) {
      if (m[1]) out += '<span class="c">' + esc(m[1]) + "</span>";
      else if (m[2]) out += '<span class="s">' + esc(m[2]) + "</span>";
      else if (m[3]) out += '<span class="n">' + m[3] + "</span>";
      else if (m[4]) out += KW.test(m[4]) && m[4].match(KW)[0] === m[4] ? '<span class="k">' + m[4] + "</span>" : (/^\s*\(/.test(code.slice(re.lastIndex)) ? '<span class="f">' + m[4] + "</span>" : m[4]);
      else out += esc(m[5]);
    }
    return out;
  }
  function codeHTML(a) {
    return '<div class="code"><div class="bar">Python' + (a.fichier ? " · " + esc(a.fichier) : "") +
      '<button type="button" data-copie>Copier</button></div><pre>' + pyHTML(a.code) + "</pre>" +
      (a.sortie ? '<div class="sortie">' + esc(a.sortie) + "</div>" : "") + "</div>";
  }

  /* ---------- blocs de contenu ---------- */
  function boite(type, lab, html) {
    return '<div class="boite ' + type + '"><span class="lab">' + lab + '</span><div class="corps">' + F(html) + "</div></div>";
  }
  /* Le cours est écrit en HTML enrichi : [def|Titre] … [/], [prop|…], [thm|…], [ex|…], [meth|…], [piege|…], [hist|…] */
  var LABS = { def: "Définition", prop: "Propriété", thm: "Théorème", ex: "Exemple", meth: "Méthode", piege: "Piège", hist: "Histoire" };
  function riche(html) {
    html = String(html || "").replace(/\[(def|prop|thm|ex|meth|piege|hist)(?:\|([^\]]*))?\]([\s\S]*?)\[\/\]/g, function (_, t, titre, corps) {
      return boite(t, LABS[t] + (titre ? " · " + titre : ""), corps);
    });
    html = html.replace(/\[py\]([\s\S]*?)\[\/py\]/g, function (_, c) { return codeHTML({ code: c.replace(/^\n/, "") }); });
    return F(html);
  }

  /* ---------- pages ---------- */
  var ONGLETS = [["cours", "Cours"], ["demos", "Démonstrations"], ["python", "Python"], ["methodes", "Méthodes"], ["exercices", "Exercices"], ["retenir", "À retenir"], ["qcm", "QCM"], ["cartes", "Flashcards"]];

  function enteteCh(c, onglet) {
    var h = '<div class="fil"><a href="#accueil">Accueil</a> › ' + esc(c.partie) + "</div>";
    h += '<div class="titre-ch"><span class="gros">' + c.num + '</span><div><h1>' + esc(c.titre) + "</h1><p>" + F(c.sous || "") + "</p></div></div>";
    if (c.statut === "ok") {
      h += '<nav class="onglets" aria-label="Parties du chapitre">';
      ONGLETS.forEach(function (o) { h += '<a href="#' + c.id + "/" + o[0] + '"' + (o[0] === onglet ? ' class="on" aria-current="page"' : "") + ">" + o[1] + "</a>"; });
      h += "</nav>";
    }
    return h;
  }

  function pageCours(c) {
    var h = '<div class="cinq"><h3>L\'essentiel en 5 lignes</h3><ol>' + c.essentiel.map(function (l) { return "<li>" + F(l) + "</li>"; }).join("") + "</ol></div>";
    h += '<details class="no-print"><summary><span class="st">Ce que le programme attend (BO)</span></summary><div class="dd"><ul>' + c.attendus.map(function (l) { return "<li>" + F(l) + "</li>"; }).join("") + '</ul><p style="font-size:.85rem;color:var(--encre3)">Capacités reformulées d\'après le programme officiel de spécialité (BO spécial n° 8 du 25 juillet 2019).</p></div></details>';
    if (c.premiere) h += '<details><summary><span class="st">Rappels de Première</span><span class="tag p1">1re</span></summary><div class="dd">' + riche(c.premiere) + "</div></details>";
    c.cours.forEach(function (s, i) {
      h += '<section class="bloc" id="' + c.id + "-" + s.id + '"><h2><span class="no" aria-hidden="true"><svg viewBox="0 0 30 30"><circle cx="15" cy="15" r="13" transform="rotate(' + (i * 47 % 360) + ' 15 15)"/></svg>' + (i + 1) + '</span><span class="sr">' + (i + 1) + '. </span>' + F(s.titre) + "</h2>" + riche(s.html) + "</section>";
    });
    if (c.pieges && c.pieges.length) {
      h += '<section class="bloc" id="' + c.id + '-pieges"><h2><span class="no" aria-hidden="true"><svg viewBox="0 0 30 30"><circle cx="15" cy="15" r="13"/></svg>✗</span>Les pièges du chapitre</h2>';
      c.pieges.forEach(function (p) { h += boite("piege", "Piège · " + p.t, p.h); });
      h += "</section>";
    }
    return h;
  }
  function pageDemos(c) {
    var h = "<p>Le programme liste des <b>démonstrations exigibles</b> (marquées <span class=\"tag bo\">BO</span>) : on peut te demander de les refaire au bac ou au Grand oral. Les autres sont là pour comprendre. Essaie d'abord seul, puis ouvre la rédaction.</p>";
    c.demos.forEach(function (d) {
      h += '<details class="demo"><summary><span class="st">' + F(d.t) + '</span>' + (d.bo ? '<span class="tag bo">BO</span>' : '<span class="tag inv">pour comprendre</span>') + '</summary><div class="dd">' + riche(d.h) + "</div></details>";
    });
    return h;
  }
  function pagePython(c) {
    var h = "<p>Le programme demande d'écrire et de comprendre des algorithmes en <b>Python</b> (ou en langage naturel, avec <code>←</code> pour l'affectation). Ceux marqués <span class=\"tag bo\">BO</span> sont cités par le programme. Les sorties affichées ont été obtenues en exécutant réellement le code.</p>";
    c.algos.forEach(function (a) {
      h += "<h3>" + F(a.t) + (a.bo ? ' <span class="tag bo">BO</span>' : "") + "</h3>" + riche(a.avant || "") + codeHTML(a) + riche(a.apres || "");
    });
    return h;
  }
  function pageMethodes(c) {
    var h = "";
    c.methodes.forEach(function (m) { h += "<h3>" + F(m.t) + "</h3>" + riche(m.h); });
    return h;
  }
  var NIV = { 1: ["n1", "Application"], 2: ["n2", "Approfondissement"], 3: ["n3", "Type bac"] };
  function pageExos(c) {
    var h = "<p>Trois niveaux : <span class=\"niv n1\">Application</span> <span class=\"niv n2\">Approfondissement</span> <span class=\"niv n3\">Type bac</span>. Ces exercices sont <b>inventés pour le site</b> ; chaque résultat numérique a été recalculé par un programme. Cherche au brouillon avant d'ouvrir le corrigé.</p>";
    c.exos.forEach(function (e, i) {
      h += '<div class="exo"><h4><span class="niv ' + NIV[e.niv][0] + '">' + NIV[e.niv][1] + "</span> Exercice " + (i + 1) + (e.t ? " · " + F(e.t) : "") + "</h4>" + riche(e.enonce) +
        '<details><summary><span class="st">Corrigé détaillé</span></summary><div class="dd corr">' + riche(e.corrige) + "</div></details></div>";
    });
    if (c.annales && c.annales.length) {
      h += "<h2>Dans les vrais sujets du bac</h2><p>Exercices d'annales officielles qui portent sur ce chapitre (sujets et corrigés gratuits sur le site de l'APMEP). Vérifiés sur les sujets eux-mêmes.</p>";
      c.annales.forEach(function (a) {
        h += '<div class="annale"><b>' + esc(a.ref) + "</b><br>" + F(a.h) + (a.url ? '<br><a href="' + a.url + '" target="_blank" rel="noopener">Ouvrir le sujet (PDF, APMEP)</a>' : "") + "</div>";
      });
    }
    return h;
  }
  function pageRetenir(c) {
    return '<div class="no-print" style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><button class="btn plein" type="button" data-imprime>' + ic("print") + ' Imprimer la fiche</button></div><div class="fiche"><h2 style="margin-top:.4em">À retenir — ' + esc(c.titre) + "</h2>" + riche(c.retenir) + "</div>";
  }
  function pageQCM(c) { return '<p>' + c.qcm.length + ' questions. Après chaque réponse : l\'explication, et un lien pour revoir le paragraphe du cours.</p><div data-qcm="' + c.id + '"></div>'; }
  function pageCartes(c) { return '<p>' + c.cartes.length + ' cartes. Touche la carte pour la retourner. « À revoir » la remet plus loin dans le paquet.</p><div data-cartes="' + c.id + '"></div>'; }

  function pageBientot(c) {
    var h = enteteCh(c, "");
    h += '<div class="boite hist"><span class="lab">Bientôt</span><div class="corps"><p>Ce chapitre sera rédigé au fil de l\'année. En attendant, voici <b>exactement ce que dit le programme officiel</b> : c\'est la liste de ce que tu dois savoir faire.</p></div></div>';
    h += "<h2>Contenus</h2><ul>" + c.contenus.map(function (x) { return "<li>" + F(x) + "</li>"; }).join("") + "</ul>";
    h += "<h2>Capacités attendues</h2><ul>" + c.capacites.map(function (x) { return "<li>" + F(x) + "</li>"; }).join("") + "</ul>";
    if (c.demos && c.demos.length) h += '<h2>Démonstrations exigibles <span class="tag bo">BO</span></h2><ul>' + c.demos.map(function (x) { return "<li>" + F(x) + "</li>"; }).join("") + "</ul>";
    if (c.algos && c.algos.length) h += "<h2>Algorithmes cités</h2><ul>" + c.algos.map(function (x) { return "<li>" + F(x) + "</li>"; }).join("") + "</ul>";
    if (c.note) h += riche(c.note);
    return h;
  }

  function carteCh(c) {
    var ok = c.statut === "ok";
    return '<a class="ch-carte' + (ok ? "" : " bientot") + (c.partie === "Probabilités" ? " pro" : c.partie === "Analyse" ? "" : " alg") + '" href="#' + c.id + '"><span class="num">' + c.num + '</span><span><b>' + esc(c.titre) + "</b><small>" + F(c.resume || c.sous || "") + '</small></span><span class="etat ' + (ok ? "ok" : "bt") + '">' + (ok ? "Rédigé" : "Bientôt") + "</span></a>";
  }
  function pageAccueil() {
    var h = '<div class="hero"><div class="formule" aria-hidden="true">' + TeX.math("\\lim_{n\\to+\\infty}\\left(1+\\frac{1}{n}\\right)^n=\\e") + '</div>' + COMPAS + '<h1><span>CQFD</span></h1><span class="devise">ce qu\'il fallait démontrer</span><p style="font-family:var(--serif);font-size:1.15rem;color:var(--encre);margin:.3em 0">Le carnet de maths de Terminale, spécialité.</p><p>Cours rédigés à fond, démonstrations exigibles, programmes Python, méthodes, exercices corrigés en trois niveaux, vrais sujets du bac, QCM et flashcards. Hors ligne, gratuit, sans compte.</p><div class="actions"><a class="btn plein" href="#' + REDIGES[0].id + '">Commencer : ' + esc(REDIGES[0].court) + '</a><a class="btn" href="#entrainement">' + ic("cible") + ' S\'entraîner</a><a class="btn" href="#epreuve">' + ic("copie") + " L'épreuve</a></div></div>";
    h += REDIGES.length === CH.length ? '<h2>Tout le programme</h2><p>Les ' + CH.length + " chapitres du programme officiel de Terminale sont rédigés, chacun avec son animation explicative.</p>" : '<h2>Où en est le site</h2><p>' + REDIGES.length + " chapitres sur " + CH.length + " sont rédigés. Les autres apparaissent avec le contenu exact du programme officiel, en attendant leur rédaction.</p>";
    var parties = [];
    CH.forEach(function (c) { if (parties.indexOf(c.partie) < 0) parties.push(c.partie); });
    parties.forEach(function (p) {
      h += '<div class="carte-prog"><h3>' + ic(PARTIE_IC[p] || "courbe") + " " + esc(p) + '</h3><div class="grille-ch">' + CH.filter(function (c) { return c.partie === p; }).map(carteCh).join("") + "</div></div>";
    });
    h += '<div class="boite meth"><span class="lab">Comment utiliser CQFD</span><div class="corps"><ol><li>Lis <b>L\'essentiel en 5 lignes</b>, puis le cours, crayon en main : refais les exemples.</li><li>Refais les <b>démonstrations</b> marquées BO sans regarder.</li><li>Fais les exercices dans l\'ordre des niveaux, puis le <b>vrai sujet</b> cité.</li><li>Termine par le <b>QCM</b> et les <b>flashcards</b> ; reviens-y quelques jours plus tard.</li></ol></div></div>';
    return h;
  }

  /* construction au compas : cercle, tangente en un point, rayon (décor de l'accueil) */
  var COMPAS = '<svg class="compas" viewBox="0 0 210 210" aria-hidden="true"><circle class="trace" style="--l:540" cx="105" cy="105" r="85"/><path class="trace" style="--l:240" d="M67.7 -37.3 L251.5 117.1"/><path class="r trace" style="--l:90" d="M105 105 L159.6 39.9"/><circle cx="105" cy="105" r="2.5" style="fill:var(--encre3)"/><path d="M153.2 47.6 l7.7 6.4 l6.4 -7.7" class="r"/></svg>';
  var PARTIE_IC = { "Analyse": "courbe", "Algèbre et géométrie": "cube", "Probabilités": "de" };

  function pageEntrainement(sous) {
    var h = '<div class="fil"><a href="#accueil">Accueil</a></div><h1>Entraînement</h1><p>Toutes les questions et toutes les cartes des chapitres rédigés, mélangées. Choisis un chapitre pour cibler.</p>';
    h += '<nav class="onglets"><a href="#entrainement"' + (sous !== "cartes" ? ' class="on"' : "") + '>QCM mélangé</a><a href="#entrainement/cartes"' + (sous === "cartes" ? ' class="on"' : "") + ">Flashcards</a></nav>";
    h += '<div class="filtres" data-filtre><button type="button" class="on" data-f="tout">Tous</button>' + REDIGES.map(function (c) { return '<button type="button" data-f="' + c.id + '">' + c.num + ". " + esc(c.court) + "</button>"; }).join("") + "</div>";
    h += sous === "cartes" ? '<div data-cartes="tout"></div>' : '<div data-qcm="tout"></div>';
    return h;
  }

  /* ---------- QCM ---------- */
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function questions(id) {
    if (id !== "tout") return PARCH[id].qcm.map(function (q) { q.ch = id; return q; });
    var t = [];
    REDIGES.forEach(function (c) { c.qcm.forEach(function (q) { q.ch = c.id; t.push(q); }); });
    return melange(t).slice(0, 20);
  }
  function monteQCM(el, liste) {
    var i = 0, bons = 0, rep = false;
    function rendu() {
      if (i >= liste.length) {
        el.innerHTML = '<div class="qcm"><div class="haut">Terminé</div><div class="score">' + bons + " / " + liste.length + '</div><p>' + (bons === liste.length ? "Parfait. Reviens dans quelques jours pour vérifier que c'est durable." : bons >= liste.length * 0.7 ? "Bien. Relis les paragraphes des questions manquées." : "Reprends le cours des questions manquées, puis recommence.") + '</p><div class="bas"><button class="btn plein" type="button" data-re>Recommencer</button></div></div>';
        $("[data-re]", el).onclick = function () { i = 0; bons = 0; if (el.getAttribute("data-qcm") === "tout") liste = melange(liste); rendu(); };
        return;
      }
      var q = liste[i]; rep = false;
      var h = '<div class="qcm"><div class="haut"><span>Question ' + (i + 1) + " / " + liste.length + '</span><span class="barre"><i style="width:' + (100 * i / liste.length) + '%"></i></span><span>' + bons + " ✓</span></div>";
      if (el.getAttribute("data-qcm") === "tout") h += '<div style="font-size:.78rem;color:var(--rouge);font-weight:600">' + esc(PARCH[q.ch].court) + "</div>";
      var ordre = melange(q.c.map(function (_, k) { return k; }));
      h += '<div class="q">' + F(q.q) + '</div><div class="opts">' + ordre.map(function (k, pos) { return '<button type="button" class="opt" data-k="' + k + '"><span class="l">' + "abcd"[pos] + "</span><span>" + F(q.c[k]) + "</span></button>"; }).join("") + '</div><div class="suite"></div></div>';
      el.innerHTML = h;
      $$(".opt", el).forEach(function (b) {
        b.onclick = function () {
          if (rep) return; rep = true;
          var k = +b.getAttribute("data-k"), ok = k === q.r;
          if (ok) bons++;
          $$(".opt", el).forEach(function (x) { x.disabled = true; var kk = +x.getAttribute("data-k"); if (kk === q.r) x.classList.add("ok"); else if (kk === k) x.classList.add("ko"); });
          var lien = q.ref ? '<a class="btn" href="#' + q.ch + "/cours/" + q.ref + '">' + ic("retour") + " Revoir le paragraphe</a>" : "";
          $(".suite", el).innerHTML = '<div class="expl"><span class="v ' + (ok ? "ok" : "ko") + '">' + (ok ? "Juste." : "Pas tout à fait.") + "</span> " + F(q.e) + '</div><div class="bas"><button class="btn plein" type="button" data-next>' + (i + 1 < liste.length ? "Question suivante" : "Voir le score") + "</button>" + lien + "</div>";
          $("[data-next]", el).onclick = function () { i++; rendu(); var t = el.getBoundingClientRect().top; if (t < 70) window.scrollBy(0, t - 120); };
          $("[data-next]", el).focus({ preventScroll: true });
        };
      });
    }
    rendu();
  }

  /* ---------- flashcards ---------- */
  function cartes(id) {
    if (id !== "tout") return PARCH[id].cartes.map(function (c) { return { r: c[0], v: c[1], ch: id }; });
    var t = [];
    REDIGES.forEach(function (c) { c.cartes.forEach(function (k) { t.push({ r: k[0], v: k[1], ch: c.id }); }); });
    return melange(t);
  }
  function monteCartes(el, paquet) {
    var file = paquet.slice(), su = 0, total = paquet.length;
    function rendu() {
      if (!file.length) {
        el.innerHTML = '<div class="qcm"><div class="score">' + total + " / " + total + '</div><p>Paquet terminé. Tu as su ' + su + " carte" + (su > 1 ? "s" : "") + " du premier coup.</p><button class=\"btn plein\" type=\"button\" data-re>Recommencer</button></div>";
        $("[data-re]", el).onclick = function () { file = melange(paquet); su = 0; rendu(); };
        return;
      }
      var k = file[0];
      el.innerHTML = '<div class="flash"><div style="font-size:.84rem;color:var(--encre2);margin-bottom:6px">Reste ' + file.length + " carte" + (file.length > 1 ? "s" : "") + (el.getAttribute("data-cartes") === "tout" ? " · " + esc(PARCH[k.ch].court) : "") +
        '</div><button type="button" class="carte" aria-label="Retourner la carte"><span class="face r"><small>Question</small><span>' + F(k.r) + '</span></span><span class="face v"><small>Réponse</small><span>' + F(k.v) + '</span></span></button><div class="nav"><button type="button" class="btn" data-tourne>Retourner</button><button type="button" class="btn rouge" data-rev disabled>À revoir</button><button type="button" class="btn plein" data-su disabled>Je savais</button></div></div>';
      var carte = $(".carte", el);
      function tourne() { carte.classList.toggle("tourne"); $("[data-rev]", el).disabled = false; $("[data-su]", el).disabled = false; }
      carte.onclick = tourne; $("[data-tourne]", el).onclick = tourne;
      $("[data-su]", el).onclick = function () { if (!k.vu) su++; file.shift(); rendu(); };
      $("[data-rev]", el).onclick = function () { k.vu = true; file.shift(); file.splice(Math.min(3, file.length), 0, k); rendu(); };
    }
    rendu();
  }

  /* ---------- montage après rendu ---------- */
  function monte(page) {
    $$("[data-qcm]", page).forEach(function (el) { monteQCM(el, questions(el.getAttribute("data-qcm"))); });
    $$("[data-cartes]", page).forEach(function (el) { monteCartes(el, cartes(el.getAttribute("data-cartes"))); });
    $$("[data-w]", page).forEach(function (el) { var f = WIDGETS[el.getAttribute("data-w")]; if (f) { try { f(el); } catch (e) { el.textContent = ""; } } });
    ANIM.arreter();
    $$("[data-anim]", page).forEach(function (el) { try { ANIM.monte(el, el.getAttribute("data-anim")); } catch (e) { if (window.console) console.error(e); } });
    $$("[data-copie]", page).forEach(function (b) {
      b.onclick = function () {
        var t = b.closest(".code").querySelector("pre").textContent;
        var fin = function () { b.textContent = "Copié"; setTimeout(function () { b.textContent = "Copier"; }, 1400); };
        if (navigator.clipboard) navigator.clipboard.writeText(t).then(fin, function () {}); else fin();
      };
    });
    $$("[data-imprime]", page).forEach(function (b) { b.onclick = function () { window.print(); }; });
    var f = $("[data-filtre]", page);
    if (f) $$("button", f).forEach(function (b) {
      b.onclick = function () {
        $$("button", f).forEach(function (x) { x.classList.toggle("on", x === b); });
        var id = b.getAttribute("data-f"), q = $("[data-qcm]", page), c = $("[data-cartes]", page);
        if (q) { q.setAttribute("data-qcm", id); monteQCM(q, questions(id)); }
        if (c) { c.setAttribute("data-cartes", id); monteCartes(c, cartes(id)); }
      };
    });
  }

  /* ---------- routeur ---------- */
  var main = $("#page"), menu = $("#menu");
  function route() {
    var h = decodeURIComponent(location.hash.replace(/^#/, "")) || "accueil";
    var p = h.split("/"), html = "", actif = p[0], cible = null, titre = "CQFD";
    var c = PARCH[p[0]];
    if (c && c.statut === "ok") {
      var o = p[1] || "cours";
      if (!ONGLETS.some(function (x) { return x[0] === o; })) o = "cours";
      var corps = { cours: pageCours, demos: pageDemos, python: pagePython, methodes: pageMethodes, exercices: pageExos, retenir: pageRetenir, qcm: pageQCM, cartes: pageCartes }[o](c);
      html = enteteCh(c, o) + corps;
      var i = REDIGES.indexOf(c);
      html += '<div class="suivant no-print">' + (i > 0 ? '<a class="btn" href="#' + REDIGES[i - 1].id + '">← ' + esc(REDIGES[i - 1].court) + "</a>" : "") + (i < REDIGES.length - 1 ? '<a class="btn" style="justify-content:flex-end" href="#' + REDIGES[i + 1].id + '">' + esc(REDIGES[i + 1].court) + " →</a>" : "") + "</div>";
      if (p[2]) cible = c.id + "-" + p[2];
      titre = c.court + " · CQFD";
    } else if (c) { html = pageBientot(c); titre = c.court + " · CQFD"; }
    else if (p[0] === "epreuve") { html = PAGES.epreuve(); titre = "L'épreuve · CQFD"; }
    else if (p[0] === "ressources") { html = PAGES.ressources(); titre = "Ressources · CQFD"; }
    else if (p[0] === "entrainement") { html = pageEntrainement(p[1]); titre = "Entraînement · CQFD"; }
    else { html = pageAccueil(); actif = "accueil"; }
    html += '<div class="pied">CQFD — carnet de maths de Terminale, spécialité. Contenu original rédigé d\'après le programme officiel (BO spécial n° 8 du 25 juillet 2019) et la définition de l\'épreuve (BO spécial n° 4 du 17 septembre 2026). Vérifie toujours avec ton professeur.</div>';
    main.innerHTML = html;
    main.classList.remove("entre"); void main.offsetWidth; main.classList.add("entre");
    D.title = titre;
    $$("a", menu).forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + actif); });
    fermeMenu();
    monte(main);
    if (cible) {
      var el = D.getElementById(cible);
      if (el) { setTimeout(function () { el.scrollIntoView({ behavior: reduit ? "auto" : "smooth", block: "start" }); el.classList.remove("eclaire"); void el.offsetWidth; el.classList.add("eclaire"); }, 60); return; }
    }
    window.scrollTo(0, 0);
  }

  function construireMenu() {
    var h = '<a href="#accueil">' + ic("maison") + " Accueil</a>";
    var parties = [];
    CH.forEach(function (c) { if (parties.indexOf(c.partie) < 0) parties.push(c.partie); });
    parties.forEach(function (pt) {
      h += "<h6>" + esc(pt) + "</h6>";
      CH.filter(function (c) { return c.partie === pt; }).forEach(function (c) {
        h += '<a href="#' + c.id + '"' + (c.statut === "ok" ? "" : ' class="bientot"') + '><span class="num">' + c.num + "</span>" + esc(c.court) + "</a>";
      });
    });
    h += "<h6>Préparer le bac</h6>";
    h += '<a href="#entrainement">' + ic("cible") + " Entraînement</a>";
    h += '<a href="#epreuve">' + ic("copie") + " L'épreuve</a>";
    h += '<a href="#ressources">' + ic("livres") + " Ressources</a>";
    menu.innerHTML = h;
  }
  function ouvreMenu() { menu.classList.add("ouvert"); $("#voile").classList.add("ouvert"); }
  function fermeMenu() { menu.classList.remove("ouvert"); $("#voile").classList.remove("ouvert"); }

  /* ---------- thème (bascule non mémorisée) ---------- */
  var THEMES = ["auto", "clair", "sombre"], ti = 0;
  function majTheme() {
    var t = THEMES[ti];
    if (t === "auto") H.removeAttribute("data-theme"); else H.setAttribute("data-theme", t);
    var b = $("#bTheme");
    b.innerHTML = ic(t === "auto" ? "auto" : t === "clair" ? "soleil" : "lune");
    b.setAttribute("aria-label", "Thème : " + (t === "auto" ? "automatique" : t) + " (changer)");
    b.title = b.getAttribute("aria-label");
  }

  /* ---------- recherche ---------- */
  var INDEX = null;
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function indexer() {
    INDEX = [];
    function aj(titre, lieu, texte, url) { var t = TeX.plat(texte); INDEX.push({ titre: TeX.plat(titre), lieu: lieu, texte: t, n: norm(TeX.plat(titre) + " " + t), url: url }); }
    CH.forEach(function (c) {
      var lieu = c.num + ". " + c.court;
      if (c.statut !== "ok") { aj(c.titre, lieu + " · bientôt", (c.contenus || []).concat(c.capacites || []).join(" "), "#" + c.id); return; }
      aj(c.titre, lieu, c.essentiel.join(" "), "#" + c.id);
      c.cours.forEach(function (s) { aj(s.titre, lieu + " · cours", s.html, "#" + c.id + "/cours/" + s.id); });
      (c.pieges || []).forEach(function (p) { aj("Piège : " + p.t, lieu, p.h, "#" + c.id + "/cours/pieges"); });
      c.demos.forEach(function (d) { aj(d.t, lieu + " · démonstration", d.h, "#" + c.id + "/demos"); });
      c.algos.forEach(function (a) { aj(a.t, lieu + " · Python", (a.avant || "") + " " + a.code, "#" + c.id + "/python"); });
      c.methodes.forEach(function (m) { aj(m.t, lieu + " · méthode", m.h, "#" + c.id + "/methodes"); });
      c.exos.forEach(function (e, i) { aj("Exercice " + (i + 1) + (e.t ? " : " + e.t : ""), lieu + " · exercices", e.enonce, "#" + c.id + "/exercices"); });
      c.cartes.forEach(function (k) { aj(k[0], lieu + " · flashcard", k[1], "#" + c.id + "/cartes"); });
    });
    aj("L'épreuve écrite de spécialité", "Préparer le bac", PAGES.texteEpreuve, "#epreuve");
    aj("Ressources", "Préparer le bac", PAGES.texteRessources, "#ressources");
  }
  function chercher(q) {
    var mots = norm(q).split(/\s+/).filter(function (m) { return m.length > 1; });
    if (!mots.length) return [];
    var r = [];
    INDEX.forEach(function (e) {
      var ok = mots.every(function (m) { return e.n.indexOf(m) >= 0; });
      if (!ok) return;
      var s = 0, nt = norm(e.titre);
      mots.forEach(function (m) { if (nt.indexOf(m) >= 0) s += 5; });
      if (/cours/.test(e.lieu)) s += 1;
      r.push({ e: e, s: s });
    });
    r.sort(function (a, b) { return b.s - a.s; });
    return r.slice(0, 40).map(function (x) { return x.e; });
  }
  function surligne(txt, mots) {
    var t = esc(txt), n = norm(txt);
    var pos = [];
    mots.forEach(function (m) { var i = n.indexOf(m); if (i >= 0) pos.push([i, i + m.length]); });
    if (!pos.length) return t;
    pos.sort(function (a, b) { return a[0] - b[0]; });
    var out = "", d = 0;
    pos.forEach(function (p) { if (p[0] < d) return; out += esc(txt.slice(d, p[0])) + "<mark>" + esc(txt.slice(p[0], p[1])) + "</mark>"; d = p[1]; });
    return out + esc(txt.slice(d));
  }
  function extrait(e, mots) {
    var n = norm(e.texte), i = -1;
    mots.forEach(function (m) { var k = n.indexOf(m); if (k >= 0 && (i < 0 || k < i)) i = k; });
    var d = Math.max(0, i - 50), t = e.texte.slice(d, d + 160);
    return (d > 0 ? "… " : "") + surligne(t, mots) + (d + 160 < e.texte.length ? " …" : "");
  }
  var srch = $("#srch"), sq = $("#sq"), sres = $("#sres"), enAttente = null;
  function ouvreRecherche() {
    if (!INDEX) indexer();
    if (srch.classList.contains("on")) return;
    srch.classList.add("on"); srch.setAttribute("aria-hidden", "false");
    history.pushState({ srch: 1 }, "", location.href);
    sq.value = ""; sres.innerHTML = '<div class="vide">Tape un mot : récurrence, gendarmes, asymptote, dichotomie, Pascal…</div>';
    setTimeout(function () { sq.focus(); }, 30);
  }
  function fermeRecherche() { srch.classList.remove("on"); srch.setAttribute("aria-hidden", "true"); }
  sq.addEventListener("input", function () {
    var q = sq.value, mots = norm(q).split(/\s+/).filter(function (m) { return m.length > 1; });
    var r = chercher(q);
    if (!q.trim()) { sres.innerHTML = ""; return; }
    sres.innerHTML = r.length ? r.map(function (e) { return '<a class="r" href="' + e.url + '" data-url="' + e.url + '"><small>' + esc(e.lieu) + "</small><b>" + surligne(e.titre, mots) + "</b><span>" + extrait(e, mots) + "</span></a>"; }).join("") : '<div class="vide">Aucun résultat. Essaie un autre mot.</div>';
  });
  sres.addEventListener("click", function (ev) {
    var a = ev.target.closest("a.r"); if (!a) return;
    ev.preventDefault(); enAttente = a.getAttribute("data-url");
    fermeRecherche(); history.back();
  });
  $("#sx").onclick = function () { fermeRecherche(); history.back(); };
  window.addEventListener("popstate", function () {
    if (srch.classList.contains("on")) fermeRecherche();
    if (enAttente) { var u = enAttente; enAttente = null; setTimeout(function () { if (location.hash === u) route(); else location.hash = u; }, 0); }
  });
  D.addEventListener("keydown", function (e) {
    if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && !/input|textarea|select/i.test((e.target.tagName || "")))) { e.preventDefault(); ouvreRecherche(); }
    else if (e.key === "Escape") { if (srch.classList.contains("on")) { fermeRecherche(); history.back(); } else fermeMenu(); }
  });

  /* ---------- démarrage ---------- */
  construireMenu();
  $("#bMenu").onclick = function () { menu.classList.contains("ouvert") ? fermeMenu() : ouvreMenu(); };
  $("#voile").onclick = fermeMenu;
  $("#bCherche").onclick = ouvreRecherche;
  $("#bTheme").onclick = function () { ti = (ti + 1) % 3; majTheme(); };
  majTheme();
  window.addEventListener("hashchange", route);
  route();
  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(function () {});
})();
