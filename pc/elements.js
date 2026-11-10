/* « LIAISONS » — compléments de l'identité visuelle (voir elements.css).
   1. Accueil : trace les liaisons entre les atomes de chaque chaîne de chapitres,
      remplit les compteurs ; 2. pages de chapitre : l'atome du chapitre devant le
      thème ; 3. ordinateur : barre latérale graphite. Rien ici ne touche au contenu. */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var LOGO = '<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><path d="M9 29 L20 11 L31 29" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="20" cy="11" r="6.2" fill="#EA580C"/><circle cx="9" cy="29" r="5" fill="currentColor"/><circle cx="31" cy="29" r="5" fill="currentColor"/></svg>';

  function chaines() {
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

  function compteurs() {
    var box = document.getElementById("elStats"); if (!box) return;
    var ouverts = document.querySelectorAll("#page-accueil .chap-list li.actif").length;
    var total = document.querySelectorAll("#page-accueil .chap-list li").length;
    var videos = document.querySelectorAll('section.part[id$="-video"]').length;
    var s = '<span><b>' + ouverts + '</b>chapitres ouverts</span><span><b>' + total + '</b>au programme</span>';
    if (videos) s += '<span><b>' + videos + '</b>vidéos de cours</span>';
    box.innerHTML = s;
  }

  /* chapitre → symbole, lu sur l'accueil */
  function symboles() {
    var m = {}, liens = document.querySelectorAll("#page-accueil li.actif .chap-link");
    for (var i = 0; i < liens.length; i++) {
      var on = liens[i].getAttribute("onclick") || "", id = (on.match(/go\('([^']+)'\)/) || [])[1], sym = liens[i].querySelector(".sym");
      if (id && sym) m[id] = {sym: sym.textContent, titre: (liens[i].querySelector(".ti") || {}).textContent || ""};
    }
    return m;
  }

  function atomesChapitres(m) {
    for (var id in m) {
      var sur = document.querySelector("#page-" + id + " .chap-hero .sur");
      if (sur && !sur.querySelector(".el-at")) {
        var s = document.createElement("span"); s.className = "el-at"; s.setAttribute("aria-hidden", "true"); s.textContent = m[id].sym;
        sur.insertBefore(s, sur.firstChild);
      }
    }
  }

  function barre(m) {
    if (document.querySelector(".el-side")) return;
    var nav = document.createElement("nav"); nav.className = "el-side"; nav.setAttribute("aria-label", "Chapitres");
    var h = '<div class="el-logo" data-go="accueil">' + LOGO.replace('class="logo"', '') + '<div><b>Liai<em>sons</em></b><small>Physique-chimie · Tle</small></div></div>';
    var blocs = document.querySelectorAll("#page-accueil .theme-bloc");
    for (var i = 0; i < blocs.length; i++) {
      var t = blocs[i].querySelector("h2"), nom = t ? t.textContent.replace(/^\s*\d+\s*/, "").trim() : "";
      h += "<h6>" + nom + "</h6>";
      var lis = blocs[i].querySelectorAll(".chap-list li");
      for (var j = 0; j < lis.length; j++) {
        var lien = lis[j].querySelector(".chap-link"), ti = (lis[j].querySelector(".ti") || {}).textContent || "";
        var id = ((lien.getAttribute("onclick") || "").match(/go\('([^']+)'\)/) || [])[1];
        h += id ? '<a href="#" data-go="' + id + '"><i></i>' + ti + "</a>" : '<a class="vide" aria-disabled="true"><i></i>' + ti + "</a>";
      }
    }
    if (document.getElementById("page-tpece")) h += '<h6>Outils</h6><a href="#" data-go="tpece"><i></i>TP · ECE — gestes et montages</a>';
    h += '<svg class="el-fond" viewBox="0 0 200 170" aria-hidden="true"><g fill="none" stroke="#EA580C" stroke-width="3"><path d="M100 14L140 37V83L100 106L60 83V37Z"/><path d="M140 83L178 105M100 106V150L136 166"/></g><g fill="#EA580C"><circle cx="178" cy="105" r="8"/><circle cx="136" cy="166" r="7"/></g></svg>';
    nav.innerHTML = h;
    nav.addEventListener("click", function (e) {
      var a = e.target.closest("[data-go]"); if (!a) return;
      e.preventDefault(); if (typeof window.go === "function") window.go(a.getAttribute("data-go"));
    });
    document.body.insertBefore(nav, document.body.firstChild);
    document.body.classList.add("el-avec-side");
  }

  function actif() {
    var page = document.querySelector(".page.on"), id = page ? page.id.replace("page-", "") : "";
    var liens = document.querySelectorAll(".el-side [data-go]");
    for (var i = 0; i < liens.length; i++) liens[i].classList.toggle("on", liens[i].getAttribute("data-go") === id);
    if (id === "accueil") requestAnimationFrame(chaines);
  }

  function demarrer() {
    var brand = document.querySelector("header .brand");
    if (brand && !brand.querySelector(".logo")) brand.insertAdjacentHTML("afterbegin", LOGO);
    compteurs();
    var m = symboles();
    atomesChapitres(m);
    barre(m);
    actif();
    chaines();
    var pages = document.querySelectorAll(".page");
    if (window.MutationObserver) {
      var obs = new MutationObserver(actif);
      for (var i = 0; i < pages.length; i++) obs.observe(pages[i], {attributes: true, attributeFilter: ["class"]});
    }
    var minuteur = 0;
    window.addEventListener("resize", function () { clearTimeout(minuteur); minuteur = setTimeout(chaines, 120); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(chaines);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
