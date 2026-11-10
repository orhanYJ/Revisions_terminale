/* Identité visuelle du site de physique-chimie : deux thèmes au choix.
   « Liaisons » (elements.css, par défaut) : la molécule, orange sur graphite.
   « Pleine lumière » (lumiere.css, chargé à la demande) : l'observatoire de nuit, le spectre.
   Le choix du thème et du mode clair / sombre est retenu sur l'appareil seulement
   (localStorage, préférence d'affichage, aucune donnée de révision) ; un petit script du
   <head> l'applique avant l'affichage. Rien ici ne touche au contenu. */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var CLE_ID = "pc-identite", CLE_MODE = "pc-mode";
  var ID = {
    liaisons: {
      nom: "Liaisons", marque: 'Liai<b>sons</b>', side: 'Liai<em>sons</em>', mode: "clair",
      titre: 'Tout le programme, <em>liaison</em> par liaison.',
      lead: "Chaque chapitre est un atome de la chaîne : il s'allume quand il est en ligne. Cours, TP corrigés, exercices, schémas interactifs, vidéo et fiche mémo. L'objectif n'est pas de réciter : c'est de comprendre pourquoi chaque formule dit ce qu'elle dit.",
      logo: '<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><path d="M9 29 L20 11 L31 29" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="20" cy="11" r="6.2" fill="#EA580C"/><circle cx="9" cy="29" r="5" fill="currentColor"/><circle cx="31" cy="29" r="5" fill="currentColor"/></svg>',
      apercu: "radial-gradient(circle at 30% 35%,#FFA066 0 9%,#EA580C 10% 15%,transparent 16%),radial-gradient(circle at 70% 65%,#F4F1F7 0 8%,transparent 9%),#1B1A1E",
      desc: "La molécule · orange sur graphite"
    },
    lumiere: {
      nom: "Pleine lumière", marque: 'Pleine <b>lumière</b>', side: 'Pleine <em>lumière</em>', mode: "sombre",
      titre: 'La physique-chimie, <em>en pleine lumière.</em>',
      lead: "Chaque chapitre est une raie du spectre : elle s'allume quand le chapitre est en ligne. Cours, TP corrigés, exercices, schémas interactifs, vidéo et fiche mémo, pour comprendre pourquoi chaque formule dit ce qu'elle dit.",
      logo: '<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><path d="M2 21 L15 20" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M20 7 L30 31 L10 31 Z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M24 19 L39 13" stroke="#7C5CFF" stroke-width="2.2" stroke-linecap="round"/><path d="M25 21 L39 20" stroke="#3AD16B" stroke-width="2.2" stroke-linecap="round"/><path d="M26 23 L39 27" stroke="#FF8A3D" stroke-width="2.2" stroke-linecap="round"/></svg>',
      apercu: "linear-gradient(90deg,transparent 0 18%,#7C5CFF 18% 21%,transparent 21% 36%,#2F8BFF 36% 39%,transparent 39% 54%,#3AD16B 54% 57%,transparent 57% 72%,#FF8A3D 72% 75%,transparent 75%),#07080F",
      desc: "L'observatoire · le spectre de la lumière"
    }
  };
  function lire(k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } }
  function ecrire(k, v) { try { window.localStorage.setItem(k, v); } catch (e) {} }
  function identite() { return document.documentElement.getAttribute("data-identite") === "lumiere" ? "lumiere" : "liaisons"; }

  /* couleur d'une longueur d'onde (nm) */
  function couleur(l) {
    var s = [[400,[124,92,255]],[440,[59,108,255]],[480,[34,170,220]],[520,[58,209,107]],[565,[255,211,77]],[600,[255,138,61]],[650,[255,61,90]],[700,[210,30,50]]];
    if (l <= s[0][0]) return "rgb(124,92,255)";
    for (var i = 0; i < s.length - 1; i++) if (l <= s[i + 1][0]) {
      var u = (l - s[i][0]) / (s[i + 1][0] - s[i][0]), a = s[i][1], b = s[i + 1][1];
      return "rgb(" + a.map(function (v, j) { return Math.round(v + (b[j] - v) * u); }).join(",") + ")";
    }
    return "rgb(210,30,50)";
  }

  /* ---------- liaisons de l'accueil (thème « Liaisons ») ---------- */
  function chaines() {
    if (identite() !== "liaisons") return;
    var listes = document.querySelectorAll("#page-accueil .chap-list");
    for (var k = 0; k < listes.length; k++) {
      var ul = listes[k], lis = ul.querySelectorAll(":scope > li");
      if (!ul.offsetParent || lis.length < 2) continue;
      var r0 = ul.getBoundingClientRect(), pts = [];
      for (var i = 0; i < lis.length; i++) {
        var at = lis[i].querySelector(".sym");
        if (!at) return;
        var r = at.getBoundingClientRect();
        pts.push({x: r.left - r0.left + r.width / 2, y: r.top - r0.top + r.height / 2, on: lis[i].classList.contains("actif")});
      }
      var svg = ul.querySelector(":scope > .el-liaisons"), neuf = !svg;
      if (neuf) { svg = document.createElementNS(NS, "svg"); svg.setAttribute("class", "el-liaisons"); svg.setAttribute("aria-hidden", "true"); ul.insertBefore(svg, ul.firstChild); }
      svg.innerHTML = "";
      for (var j = 0; j < pts.length - 1; j++) {
        var a = pts[j], b = pts[j + 1], p = document.createElementNS(NS, "path");
        p.setAttribute("d", "M" + a.x.toFixed(1) + " " + a.y.toFixed(1) + " L" + b.x.toFixed(1) + " " + b.y.toFixed(1));
        if (!(a.on && b.on)) p.setAttribute("class", "vide");
        else if (neuf) { var l = Math.hypot(b.x - a.x, b.y - a.y); p.setAttribute("class", "trace"); p.style.setProperty("--l", l.toFixed(1)); p.style.animationDelay = (0.15 + j * 0.12) + "s"; }
        svg.appendChild(p);
      }
    }
  }

  /* ---------- chaque chapitre : une raie du spectre (couleur, longueur d'onde) ---------- */
  var RAIES = {};
  function raies() {
    var lis = document.querySelectorAll("#page-accueil .chap-list li"), n = lis.length;
    for (var i = 0; i < n; i++) {
      var lambda = Math.round(405 + (n < 2 ? 0 : i / (n - 1)) * 290), c = couleur(lambda);
      lis[i].style.setProperty("--c", c);
      lis[i].setAttribute("data-lambda", lambda + " nm");
      var lien = lis[i].querySelector(".chap-link"), id = ((lien.getAttribute("onclick") || "").match(/go\('([^']+)'\)/) || [])[1];
      if (id) RAIES[id] = c;
    }
  }

  function compteurs() {
    var box = document.getElementById("elStats"); if (!box) return;
    var ouverts = document.querySelectorAll("#page-accueil .chap-list li.actif").length;
    var total = document.querySelectorAll("#page-accueil .chap-list li").length;
    var videos = document.querySelectorAll('section.part[id$="-video"]').length;
    var s = '<span><b>' + ouverts + '</b>chapitres ouverts</span><span><b>' + total + '</b>au programme</span>';
    if (videos) s += '<span><b>' + videos + '</b>vidéos de cours</span>';
    box.innerHTML = s;
  }

  function symboles() {
    var m = {}, liens = document.querySelectorAll("#page-accueil li.actif .chap-link");
    for (var i = 0; i < liens.length; i++) {
      var id = ((liens[i].getAttribute("onclick") || "").match(/go\('([^']+)'\)/) || [])[1], sym = liens[i].querySelector(".sym");
      if (id && sym) m[id] = sym.textContent;
    }
    return m;
  }

  function atomesChapitres(m) {
    for (var id in m) {
      var hero = document.querySelector("#page-" + id + " .chap-hero"), sur = hero && hero.querySelector(".sur");
      if (!sur) continue;
      if (RAIES[id]) hero.style.setProperty("--c", RAIES[id]);
      if (!sur.querySelector(".el-at")) {
        var s = document.createElement("span"); s.className = "el-at"; s.setAttribute("aria-hidden", "true"); s.textContent = m[id];
        sur.insertBefore(s, sur.firstChild);
      }
    }
  }

  function barre() {
    if (document.querySelector(".el-side")) return;
    var nav = document.createElement("nav"); nav.className = "el-side"; nav.setAttribute("aria-label", "Chapitres");
    var h = '<div class="el-logo" data-go="accueil"><span class="el-logo-svg"></span><div><b></b><small>Physique-chimie · Tle</small></div></div>';
    var blocs = document.querySelectorAll("#page-accueil .theme-bloc");
    for (var i = 0; i < blocs.length; i++) {
      var t = blocs[i].querySelector("h2"), nom = t ? t.textContent.replace(/^\s*\d+\s*/, "").trim() : "";
      h += "<h6>" + nom + "</h6>";
      var lis = blocs[i].querySelectorAll(".chap-list li");
      for (var j = 0; j < lis.length; j++) {
        var lien = lis[j].querySelector(".chap-link"), ti = (lis[j].querySelector(".ti") || {}).textContent || "";
        var id = ((lien.getAttribute("onclick") || "").match(/go\('([^']+)'\)/) || [])[1], c = lis[j].style.getPropertyValue("--c");
        var st = c ? ' style="--c:' + c + '"' : "";
        h += id ? '<a href="#" data-go="' + id + '"' + st + '><i></i>' + ti + "</a>" : '<a class="vide" aria-disabled="true"' + st + '><i></i>' + ti + "</a>";
      }
    }
    if (document.getElementById("page-tpece")) h += '<h6>Outils</h6><a href="#" data-go="tpece"><i></i>TP · ECE — gestes et montages</a>';
    h += '<svg class="el-fond" viewBox="0 0 200 170" aria-hidden="true"><g fill="none" stroke="var(--orange)" stroke-width="3"><path d="M100 14L140 37V83L100 106L60 83V37Z"/><path d="M140 83L178 105M100 106V150L136 166"/></g><g fill="var(--orange)"><circle cx="178" cy="105" r="8"/><circle cx="136" cy="166" r="7"/></g></svg>';
    nav.innerHTML = h;
    nav.addEventListener("click", function (e) {
      var a = e.target.closest("[data-go]"); if (!a) return;
      e.preventDefault(); if (typeof window.go === "function") window.go(a.getAttribute("data-go"));
    });
    document.body.insertBefore(nav, document.body.firstChild);
    document.body.classList.add("el-avec-side");
  }

  /* ---------- textes et logos propres au thème ---------- */
  function habiller() {
    var I = ID[identite()];
    var brand = document.querySelector("header .brand");
    if (brand) {
      var ancien = brand.querySelector(".logo"); if (ancien) ancien.remove();
      brand.insertAdjacentHTML("afterbegin", I.logo);
      var nom = brand.querySelector("span:not(.brand-s)"); if (nom) nom.innerHTML = I.marque;
    }
    var side = document.querySelector(".el-side");
    if (side) { side.querySelector(".el-logo-svg").innerHTML = I.logo; side.querySelector(".el-logo b").innerHTML = I.side; }
    var h1 = document.querySelector("#page-accueil .hero h1"); if (h1) h1.innerHTML = I.titre;
    var lead = document.querySelector("#page-accueil .hero .lead"); if (lead) lead.textContent = I.lead;
    document.title = I.nom + " — Physique-Chimie Terminale";
    var meta = document.querySelector('meta[name="theme-color"]'); if (meta) meta.setAttribute("content", identite() === "lumiere" ? "#07080F" : "#1B1A1E");
    var b = document.getElementById("btnIdent"); if (b) b.setAttribute("aria-label", "Changer de thème (actuel : " + I.nom + ")");
  }

  function libelleMode() {
    var bt = document.getElementById("btnTheme");
    if (bt) bt.textContent = document.documentElement.getAttribute("data-theme") === "sombre" ? "Clair" : "Sombre";
  }

  function chargerLumiere(fait) {
    var l = document.getElementById("css-lumiere");
    if (l) { if (fait) fait(); return; }
    l = document.createElement("link"); l.rel = "stylesheet"; l.href = "lumiere.css?v=1"; l.id = "css-lumiere";
    l.onload = function () { if (fait) fait(); };
    document.head.appendChild(l);
  }

  function choisir(nom) {
    var d = document.documentElement;
    ecrire(CLE_ID, nom);
    ecrire(CLE_MODE, ID[nom].mode);
    function poser() {
      if (nom === "lumiere") d.setAttribute("data-identite", "lumiere"); else d.removeAttribute("data-identite");
      d.setAttribute("data-theme", ID[nom].mode);
      libelleMode(); habiller(); fermerMenu();
      var svg = document.querySelectorAll(".el-liaisons"); for (var i = 0; i < svg.length; i++) svg[i].remove();
      requestAnimationFrame(function () { chaines(); caler(); });
    }
    if (nom === "lumiere") chargerLumiere(poser); else poser();
  }

  /* hauteur de l'en-tête pour les onglets collants (calerBarres de la page) */
  function caler() { if (typeof window.calerBarres === "function") window.calerBarres(); }

  /* ---------- menu des thèmes ---------- */
  var menu = null;
  function fermerMenu() { if (menu) { menu.hidden = true; var b = document.getElementById("btnIdent"); if (b) b.setAttribute("aria-expanded", "false"); } }
  function ouvrirMenu() {
    if (!menu) {
      menu = document.createElement("div"); menu.className = "el-menu"; menu.setAttribute("role", "menu");
      var h = '<div class="el-menu-t">Thème du site</div>';
      for (var k in ID) h += '<button type="button" role="menuitemradio" data-id="' + k + '"><span class="el-ap" style="background:' + ID[k].apercu + '"></span><span><b>' + ID[k].nom + "</b><small>" + ID[k].desc + "</small></span></button>";
      h += '<p class="el-menu-n">Retenu sur cet appareil seulement.</p>';
      menu.innerHTML = h;
      menu.addEventListener("click", function (e) { var b = e.target.closest("[data-id]"); if (b) choisir(b.getAttribute("data-id")); });
      document.body.appendChild(menu);
      document.addEventListener("click", function (e) { if (menu && !menu.hidden && !menu.contains(e.target) && !e.target.closest("#btnIdent")) fermerMenu(); });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape") fermerMenu(); });
    }
    var cur = identite(), bs = menu.querySelectorAll("[data-id]");
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute("aria-checked", bs[i].getAttribute("data-id") === cur ? "true" : "false");
    menu.hidden = false;
    document.getElementById("btnIdent").setAttribute("aria-expanded", "true");
    var f = menu.querySelector('[aria-checked="true"]'); if (f) f.focus();
  }
  function boutonTheme() {
    var bt = document.getElementById("btnTheme"); if (!bt || document.getElementById("btnIdent")) return;
    var b = document.createElement("button"); b.type = "button"; b.id = "btnIdent"; b.className = "btn-ident";
    b.setAttribute("aria-haspopup", "true"); b.setAttribute("aria-expanded", "false"); b.title = "Changer de thème";
    b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="12" r="6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="15" cy="12" r="6" fill="currentColor" opacity=".55"/></svg><span>Thème</span>';
    b.addEventListener("click", function (e) { e.stopPropagation(); if (menu && !menu.hidden) fermerMenu(); else ouvrirMenu(); });
    bt.parentNode.insertBefore(b, bt);
  }

  /* le bouton clair / sombre d'origine : on retient le mode choisi */
  function retenirMode() {
    var orig = window.basculeTheme;
    if (typeof orig !== "function" || orig._retenu) return;
    var f = function () { var r = orig.apply(this, arguments); ecrire(CLE_MODE, document.documentElement.getAttribute("data-theme")); return r; };
    f._retenu = true; window.basculeTheme = f;
    var bt = document.getElementById("btnTheme");
    if (bt) bt.setAttribute("onclick", "basculeTheme()");
  }

  function actif() {
    var page = document.querySelector(".page.on"), id = page ? page.id.replace("page-", "") : "";
    var liens = document.querySelectorAll(".el-side [data-go]");
    for (var i = 0; i < liens.length; i++) liens[i].classList.toggle("on", liens[i].getAttribute("data-go") === id);
    if (id === "accueil") requestAnimationFrame(chaines);
  }

  function demarrer() {
    raies();
    compteurs();
    atomesChapitres(symboles());
    barre();
    boutonTheme();
    retenirMode();
    libelleMode();
    habiller();
    actif();
    chaines();
    var pages = document.querySelectorAll(".page");
    if (window.MutationObserver) {
      var obs = new MutationObserver(actif);
      for (var i = 0; i < pages.length; i++) obs.observe(pages[i], {attributes: true, attributeFilter: ["class"]});
    }
    var minuteur = 0;
    window.addEventListener("resize", function () { clearTimeout(minuteur); minuteur = setTimeout(chaines, 120); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { chaines(); caler(); });
    caler();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
