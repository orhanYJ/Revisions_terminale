/* Animations explicatives : lecteur commun (lecture, pause, étape précédente / suivante, recommencer).
   Données : HLP.ANIMS[id] = { titre, intro, type: "texte" | "graphe" | "frise", ... } ; dans une page,
   <div data-anim="id"></div> monte l'animation. Sans lecture, la figure est affichée en entier :
   rien n'est caché tant que l'élève n'a pas lancé l'animation. */
(function () {
  "use strict";
  var D = window.HLP, NS = "http://www.w3.org/2000/svg";
  var reduit = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var IC = {
    debut: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5v14M19 5l-10 7 10 7z" fill="currentColor"/></svg>',
    prec: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5l-9 7 9 7z" fill="currentColor"/></svg>',
    lire: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5l13 7.5-13 7.5z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 4.5h4v15h-4zM13.5 4.5h4v15h-4z" fill="currentColor"/></svg>',
    suiv: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l9 7-9 7z" fill="currentColor"/></svg>'
  };
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  /* ---------- rendu des scènes ---------- */
  function sceneTexte(a) {
    var segs = a.segs || (D.ATELIER[a.atelier] || {}).segs || [], h = '<div class="anim-texte' + (a.vers ? " vers" : "") + '">', etapes = [];
    segs.forEach(function (s) {
      /* le texte non annoté se dépose avec le segment annoté qui le précède */
      if (typeof s === "string") { h += '<span class="a-seg a-plain" data-k="' + Math.max(0, etapes.length - 1) + '">' + esc(s).replace(/\n/g, "<br>") + "</span>"; return; }
      var k = etapes.length; etapes.push({ legende: "<b>" + (s.m ? "Mouvement " + s.m + " · " : "") + s.titre + "</b> " + s.n });
      h += '<span class="a-seg" data-k="' + k + '" data-m="' + (s.m || "") + '">' + esc(s.t).replace(/\n/g, "<br>") + "</span>";
    });
    return { html: h + "</div>", etapes: etapes };
  }
  function bord(n, x, y) { /* point du bord du rectangle n sur la droite qui va du centre vers (x, y) */
    var cx = n.x + n.w / 2, cy = n.y + n.h / 2, dx = x - cx, dy = y - cy;
    if (!dx && !dy) return [cx, cy];
    var t = Math.min(dx ? (n.w / 2) / Math.abs(dx) : 1e9, dy ? (n.h / 2) / Math.abs(dy) : 1e9);
    return [cx + dx * t, cy + dy * t];
  }
  function sceneGraphe(a) {
    var pos = {}; a.noeuds.forEach(function (n) { pos[n.id] = n; });
    var quand = {}; a.etapes.forEach(function (e, k) { (e.montre || []).forEach(function (id) { if (!(id in quand)) quand[id] = k; }); });
    var h = '<svg class="a-svg" viewBox="0 0 ' + a.w + " " + a.h + '" role="img" aria-label="' + esc(a.titre) + '" style="min-width:' + (a.min || 560) + 'px">' +
      '<defs><marker id="fl-' + a.id + '" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" class="a-pointe"/></marker></defs>';
    (a.liens || []).forEach(function (l, i) {
      var A = pos[l.de], B = pos[l.a], p1 = bord(A, B.x + B.w / 2, B.y + B.h / 2), p2 = bord(B, A.x + A.w / 2, A.y + A.h / 2);
      var id = l.id || ("l" + i), k = id in quand ? quand[id] : (Math.max(quand[l.de] || 0, quand[l.a] || 0));
      var mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2, c = l.courbe || 0;
      var d = c ? "M" + p1[0] + " " + p1[1] + " Q" + (mx + c) + " " + (my - c) + " " + p2[0] + " " + p2[1] : "M" + p1[0] + " " + p1[1] + " L" + p2[0] + " " + p2[1];
      h += '<g class="a-el a-lien' + (l.s ? " " + l.s : "") + '" data-k="' + k + '"><path class="a-trait" d="' + d + '" marker-end="url(#fl-' + a.id + ')"/>' +
        (l.t ? '<text class="a-lt" x="' + (mx + c / 2) + '" y="' + (my - c / 2 - 6) + '" text-anchor="middle">' + esc(l.t) + "</text>" : "") + "</g>";
    });
    a.noeuds.forEach(function (n) {
      var lignes = String(n.t).split("|"), k = n.id in quand ? quand[n.id] : 0, y0 = n.y + n.h / 2 - (lignes.length - 1) * 8.5 + 5;
      h += '<g class="a-el a-noeud ' + (n.s || "arg") + '" data-k="' + k + '"><rect x="' + n.x + '" y="' + n.y + '" width="' + n.w + '" height="' + n.h + '" rx="3"/>' +
        lignes.map(function (t, j) { return '<text x="' + (n.x + n.w / 2) + '" y="' + (y0 + j * 17) + '" text-anchor="middle"' + (j === 0 && n.titre ? ' class="a-nt"' : "") + ">" + esc(t) + "</text>"; }).join("") + "</g>";
    });
    return { html: h + "</svg>", etapes: a.etapes };
  }
  function sceneFrise(a) {
    var W = 1000, H = a.h || 270, x = function (an) { return 40 + (an - a.debut) / (a.fin - a.debut) * (W - 80); };
    var quand = {}; a.etapes.forEach(function (e, k) { (e.montre || []).forEach(function (id) { if (!(id in quand)) quand[id] = k; }); });
    var h = '<svg class="a-svg a-frise" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(a.titre) + '" style="min-width:' + (a.min || 760) + 'px">';
    h += '<line class="a-axe" x1="30" y1="' + (H - 40) + '" x2="' + (W - 30) + '" y2="' + (H - 40) + '"/>';
    for (var an = Math.ceil(a.debut / a.pas) * a.pas; an <= a.fin; an += a.pas) h += '<g class="a-grad"><line x1="' + x(an) + '" y1="' + (H - 45) + '" x2="' + x(an) + '" y2="' + (H - 35) + '"/><text x="' + x(an) + '" y="' + (H - 18) + '" text-anchor="middle">' + an + "</text></g>";
    (a.periodes || []).forEach(function (p, i) {
      var y = 24 + (p.rang || 0) * 44;
      h += '<g class="a-el a-per p' + ((p.c || i) % 4) + '" data-k="' + (quand[p.id] || 0) + '"><rect x="' + x(p.de) + '" y="' + y + '" width="' + Math.max(8, x(p.a) - x(p.de)) + '" height="34" rx="3"/>' +
        '<text x="' + (x(p.de) + 7) + '" y="' + (y + 22) + '">' + esc(p.nom) + "</text></g>";
    });
    (a.evts || []).forEach(function (e) {
      var X = x(e.an), y = H - 48 - (e.h || 30);
      h += '<g class="a-el a-evt" data-k="' + (quand[e.id] || 0) + '"><line x1="' + X + '" y1="' + (H - 40) + '" x2="' + X + '" y2="' + y + '"/><circle cx="' + X + '" cy="' + (H - 40) + '" r="4"/>' +
        '<text x="' + (X + (e.g ? -5 : 5)) + '" y="' + (y + 4) + '"' + (e.g ? ' text-anchor="end"' : "") + ">" + esc(e.t) + "</text></g>";
    });
    h += '<g class="a-curseur"><line x1="0" y1="14" x2="0" y2="' + (H - 32) + '"/><path d="M-6 8h12l-6 8z"/></g></svg>';
    return { html: h, etapes: a.etapes, x: x };
  }

  /* ---------- lecteur ---------- */
  function monterUn(el) {
    var id = el.getAttribute("data-anim"), a = D.ANIMS && D.ANIMS[id];
    if (!a || el.getAttribute("data-monte")) return;
    el.setAttribute("data-monte", "1"); a.id = id;
    var sc = a.type === "texte" ? sceneTexte(a) : a.type === "frise" ? sceneFrise(a) : sceneGraphe(a);
    var N = sc.etapes.length;
    el.className = "anim anim-" + a.type;
    el.innerHTML = '<div class="anim-tete"><span class="anim-tag">Animation</span><b>' + a.titre + "</b></div>" +
      '<div class="anim-scene">' + sc.html + "</div>" +
      '<div class="anim-legende" aria-live="polite"><span class="anim-n"></span><p></p></div>' +
      '<div class="anim-cmd" role="group" aria-label="Commandes de l’animation">' +
      '<button type="button" data-a="debut" aria-label="Recommencer">' + IC.debut + '</button><button type="button" data-a="prec" aria-label="Étape précédente">' + IC.prec + "</button>" +
      '<button type="button" class="anim-lire" data-a="lire" aria-label="Lecture">' + IC.lire + '<span>Lecture</span></button><button type="button" data-a="suiv" aria-label="Étape suivante">' + IC.suiv + '</button><span class="anim-prog"><i></i></span></div>';
    var scene = el.querySelector(".anim-scene"), leg = el.querySelector(".anim-legende p"), num = el.querySelector(".anim-n"),
      btn = el.querySelector(".anim-lire"), prog = el.querySelector(".anim-prog i"), i = -1, minuteur = null, cur = el.querySelector(".a-curseur");
    function appliquer() {
      el.classList.toggle("en-cours", i >= 0);
      Array.prototype.forEach.call(el.querySelectorAll("[data-k]"), function (x) {
        var k = +x.getAttribute("data-k");
        x.classList.toggle("vu", i < 0 || k <= i);
        x.classList.toggle("neuf", i >= 0 && k === i);
        x.classList.toggle("avenir", i >= 0 && k > i);
      });
      if (i < 0) { num.textContent = N + " étapes"; leg.innerHTML = a.intro || "Appuie sur lecture pour suivre l’explication pas à pas."; }
      else { num.textContent = "Étape " + (i + 1) + " / " + N; leg.innerHTML = sc.etapes[i].legende; }
      prog.style.width = (i < 0 ? 0 : (i + 1) / N * 100) + "%";
      if (cur && sc.x) {
        var an = i < 0 ? a.fin : sc.etapes[i].an;
        cur.setAttribute("transform", "translate(" + sc.x(an) + " 0)");
        if (i >= 0) { var r = scene.getBoundingClientRect(), svg = scene.querySelector("svg"), px = sc.x(an) / 1000 * svg.getBoundingClientRect().width; scene.scrollTo({ left: Math.max(0, px - r.width / 2), behavior: reduit ? "auto" : "smooth" }); }
      }
      var el2 = scene.querySelector(".a-el.neuf");
      if (el2 && a.type === "graphe" && scene.scrollWidth > scene.clientWidth + 4) {
        var rs2 = scene.getBoundingClientRect(), re2 = el2.getBoundingClientRect();
        scene.scrollTo({ left: Math.max(0, scene.scrollLeft + re2.left + re2.width / 2 - rs2.left - rs2.width / 2), behavior: reduit ? "auto" : "smooth" });
      }
      var actif = scene.querySelector(".a-seg.neuf:not(.a-plain)");
      if (actif && a.type === "texte") { var rs = scene.getBoundingClientRect(), ra = actif.getBoundingClientRect(); if (ra.top < rs.top || ra.bottom > rs.bottom) scene.scrollTop += ra.top - rs.top - 40; }
    }
    function arreter() { clearTimeout(minuteur); minuteur = null; btn.innerHTML = IC.lire + "<span>Lecture</span>"; btn.setAttribute("aria-label", "Lecture"); el.classList.remove("joue-anim"); }
    function planifier() {
      clearTimeout(minuteur);
      var d = (sc.etapes[i] && sc.etapes[i].d) || Math.min(9000, 2600 + String(sc.etapes[i] ? sc.etapes[i].legende : "").replace(/<[^>]+>/g, "").length * 38);
      minuteur = setTimeout(function () { if (i < N - 1) { i++; appliquer(); planifier(); } else arreter(); }, d);
    }
    el.querySelector(".anim-cmd").addEventListener("click", function (ev) {
      var b = ev.target.closest("button"); if (!b) return;
      var x = b.getAttribute("data-a");
      if (x === "lire") {
        if (minuteur) { arreter(); return; }
        if (i >= N - 1 || i < 0) i = 0; appliquer();
        btn.innerHTML = IC.pause + "<span>Pause</span>"; btn.setAttribute("aria-label", "Pause"); el.classList.add("joue-anim"); planifier(); return;
      }
      if (x === "debut") { arreter(); i = -1; appliquer(); return; }
      if (x === "prec") { i = Math.max(0, i - 1); } else if (x === "suiv") { i = Math.min(N - 1, i + 1); }
      appliquer(); if (minuteur) planifier();
    });
    appliquer();
  }
  window.HLPANIM = { monter: function (racine) { Array.prototype.forEach.call((racine || document).querySelectorAll("[data-anim]"), monterUn); } };
})();
