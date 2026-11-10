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
    var etiquettes = ""; /* mots de liaison : dessinés après les cases, sur un halo, pour rester lisibles */
    (a.liens || []).forEach(function (l, i) {
      var A = pos[l.de], B = pos[l.a], v = l.via; /* via : [[x1, y1], [x2, y2]] = courbe de Bézier qui contourne une case */
      var p1 = v ? bord(A, v[0][0], v[0][1]) : bord(A, B.x + B.w / 2, B.y + B.h / 2), p2 = v ? bord(B, v[1][0], v[1][1]) : bord(B, A.x + A.w / 2, A.y + A.h / 2);
      var id = l.id || ("l" + i), k = id in quand ? quand[id] : (Math.max(quand[l.de] || 0, quand[l.a] || 0));
      var mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2, c = l.courbe || 0, lx = mx + c / 2, ly = my - c / 2 - 6;
      var d = v ? "M" + p1[0] + " " + p1[1] + " C" + v[0][0] + " " + v[0][1] + " " + v[1][0] + " " + v[1][1] + " " + p2[0] + " " + p2[1]
        : c ? "M" + p1[0] + " " + p1[1] + " Q" + (mx + c) + " " + (my - c) + " " + p2[0] + " " + p2[1] : "M" + p1[0] + " " + p1[1] + " L" + p2[0] + " " + p2[1];
      if (v) { lx = (p1[0] + 3 * v[0][0] + 3 * v[1][0] + p2[0]) / 8; ly = (p1[1] + 3 * v[0][1] + 3 * v[1][1] + p2[1]) / 8 - 6; }
      if (l.lx != null) { lx = l.lx; ly = l.ly; }
      h += '<g class="a-el a-lien' + (l.s ? " " + l.s : "") + '" data-k="' + k + '"><path class="a-trait" d="' + d + '" marker-end="url(#fl-' + a.id + ')"/></g>';
      if (l.t) etiquettes += '<g class="a-el a-lien-t" data-k="' + k + '"><text class="a-lt" x="' + lx + '" y="' + ly + '" text-anchor="' + (l.la || "middle") + '">' + esc(l.t) + "</text></g>";
    });
    a.noeuds.forEach(function (n) {
      var lignes = String(n.t).split("|"), k = n.id in quand ? quand[n.id] : 0, y0 = n.y + n.h / 2 - (lignes.length - 1) * 8.5 + 5;
      h += '<g class="a-el a-noeud ' + (n.s || "arg") + '" data-k="' + k + '"><rect x="' + n.x + '" y="' + n.y + '" width="' + n.w + '" height="' + n.h + '" rx="3"/>' +
        lignes.map(function (t, j) { return '<text x="' + (n.x + n.w / 2) + '" y="' + (y0 + j * 17) + '" text-anchor="middle"' + (j === 0 && n.titre ? ' class="a-nt"' : "") + ">" + esc(t) + "</text>"; }).join("") + "</g>";
    });
    h += etiquettes + "</svg>";
    /* Version « en colonne » pour les écrans étroits : les mêmes cases, dans l'ordre de l'argument,
       reliées par leurs mots de liaison ; elle remplace le schéma qui défilait de côté. */
    var vus = [], nom = function (id) { /* nom court d'une case : avant les deux-points, sans guillemets, quatre mots au plus */
      var t = String(pos[id].t).split("|")[0].replace(/[«»]/g, "").trim(), c = t.indexOf(" :");
      if (c > 2) t = t.slice(0, c);
      var m = t.split(/\s+/); if (m.length > 4) t = m.slice(0, 4).join(" ") + "…";
      return esc(t.replace(/[\s;,.]+$/, ""));
    };
    var rang = a.noeuds.map(function (n, j) { return { n: n, k: n.id in quand ? quand[n.id] : 0, j: j }; })
      .sort(function (u, v) { return u.k - v.k || u.j - v.j; });
    var p = '<div class="a-pile" role="list" aria-label="' + esc(a.titre) + '">';
    rang.forEach(function (r, j) {
      var n = r.n, prec = j ? rang[j - 1].n.id : null, lg = [];
      /* liens entrants regroupés par mot de liaison : « donc (suite de « A » et de « B ») » */
      var grp = {}, ordreG = [];
      (a.liens || []).forEach(function (l) {
        var t = l.t ? esc(l.t) : "", cle;
        if (l.a === n.id && vus.indexOf(l.de) >= 0) {
          cle = "e:" + (t || "puis");
          if (!grp[cle]) { grp[cle] = { s: l.s, mot: t || "puis", adj: false, noms: [], sortant: false }; ordreG.push(cle); }
          if (l.de === prec) grp[cle].adj = true; else grp[cle].noms.push("« " + nom(l.de) + " »");
          if (l.s) grp[cle].s = l.s;
        } else if (l.de === n.id && vus.indexOf(l.a) >= 0) {
          cle = "s:" + (t || "vers") + l.a; grp[cle] = { s: l.s, mot: t || "vers", noms: ["« " + nom(l.a) + " »"], sortant: true }; ordreG.push(cle);
        }
      });
      lg = ordreG.map(function (c) {
        var g = grp[c], h = "<i>" + g.mot + "</i>";
        if (g.sortant) h += ' <span class="a-pl-de">→ ' + g.noms[0] + "</span>";
        else if (g.noms.length) h += ' <span class="a-pl-de">(' + (g.adj ? "et de " : "suite de ") + g.noms.join(" et de ") + ")</span>";
        return { s: g.s, h: h };
      });
      if (j) p += '<div class="a-el a-pl-lien' + (lg.some(function (x) { return x.s === "contre"; }) ? " contre" : "") + '" data-k="' + r.k + '" aria-hidden="true"><span>' + lg.map(function (x) { return x.h; }).join(" · ") + "</span></div>";
      var lignes = String(n.t).split("|");
      p += '<div class="a-el a-pc ' + (n.s || "arg") + '" data-k="' + r.k + '" role="listitem">' + (n.titre ? "<b>" + esc(lignes.shift()) + "</b><br>" : "") + lignes.map(esc).join("<br>") + "</div>";
      vus.push(n.id);
    });
    return { html: h + p + "</div>", etapes: a.etapes };
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

  /* Frises : une fois le texte mesuré, les noms de période qui débordent de leur barre passent à côté
     (là où la ligne est libre) ou se resserrent, et les étiquettes d'événements qui se chevauchent montent ou descendent. */
  function ajusterFrise(svg) {
    if (!svg || !svg.getBoundingClientRect().width) return;
    var W = svg.viewBox.baseVal.width, pers = Array.prototype.slice.call(svg.querySelectorAll(".a-per"));
    var bar = pers.map(function (g) { var r = g.querySelector("rect"); return { g: g, r: r, t: g.querySelector("text"), x: +r.getAttribute("x"), y: +r.getAttribute("y"), w: +r.getAttribute("width") }; });
    var occupe = []; /* zones déjà prises par du texte : [x1, x2, y1, y2] */
    bar.forEach(function (b) {
      var t = b.t; t.removeAttribute("font-size"); t.removeAttribute("textLength"); t.removeAttribute("lengthAdjust"); t.removeAttribute("data-hors");
      t.setAttribute("x", b.x + 7); t.setAttribute("text-anchor", "start");
      var tw = t.getBBox().width;
      if (tw + 12 > b.w) {
        var libreD = W - 6, libreG = 6;
        bar.forEach(function (o) { if (o === b || o.y !== b.y) return; if (o.x >= b.x + b.w - 1) libreD = Math.min(libreD, o.x - 4); if (o.x + o.w <= b.x + 1) libreG = Math.max(libreG, o.x + o.w + 4); });
        var place = function () {
          if (b.x + b.w + 6 + tw <= libreD) { t.setAttribute("x", b.x + b.w + 6); t.setAttribute("data-hors", "1"); return true; }
          if (b.x - 6 - tw >= libreG) { t.setAttribute("x", b.x - 6); t.setAttribute("text-anchor", "end"); t.setAttribute("data-hors", "1"); return true; }
          return false;
        };
        if (!place()) {
          t.setAttribute("font-size", "12.5"); tw = t.getBBox().width;
          if (tw + 10 > b.w && !place()) { t.setAttribute("textLength", Math.max(10, b.w - 10)); t.setAttribute("lengthAdjust", "spacingAndGlyphs"); }
        }
      }
      var bb = t.getBBox(); occupe.push([bb.x - 2, bb.x + bb.width + 2, bb.y, bb.y + bb.height]);
    });
    var basPer = bar.reduce(function (m, b) { return Math.max(m, b.y + 34); }, 0);
    var evts = Array.prototype.slice.call(svg.querySelectorAll(".a-evt")).map(function (g) {
      var ln = g.querySelector("line"), t = g.querySelector("text");
      if (!g.hasAttribute("data-y0")) g.setAttribute("data-y0", ln.getAttribute("y2"));
      var y0 = +g.getAttribute("data-y0"); ln.setAttribute("y2", y0); t.setAttribute("y", y0 + 4);
      return { ln: ln, t: t, y0: y0, x: +ln.getAttribute("x1") };
    }).sort(function (u, v) { return u.x - v.x; });
    var axe = evts.length ? +evts[0].ln.getAttribute("y1") : 0;
    evts.forEach(function (e) {
      var essais = [0], k;
      for (k = 1; k <= 8; k++) { essais.push(-15 * k); essais.push(15 * k); }
      for (k = 0; k < essais.length; k++) {
        var y = e.y0 + essais[k];
        if (y < basPer + 14 || y > axe - 14) continue;
        e.t.setAttribute("y", y + 4); var bb = e.t.getBBox(), z = [bb.x - 3, bb.x + bb.width + 3, bb.y - 1, bb.y + bb.height + 1];
        var libre = occupe.every(function (o) { return z[1] <= o[0] || z[0] >= o[1] || z[3] <= o[2] || z[2] >= o[3]; }) && z[0] >= 0 && z[1] <= W;
        if (libre) { e.ln.setAttribute("y2", y); occupe.push(z); return; }
      }
      e.t.setAttribute("y", e.y0 + 4); var b2 = e.t.getBBox(); occupe.push([b2.x - 3, b2.x + b2.width + 3, b2.y, b2.y + b2.height]);
    });
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
    if (a.type === "frise") {
      var fsvg = el.querySelector(".a-frise"); ajusterFrise(fsvg);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ajusterFrise(fsvg); });
    }
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
      var pc = el.classList.contains("a-mode-pile") && scene.querySelector(".a-pc.neuf");
      if (pc) { var rp = scene.getBoundingClientRect(), rc = pc.getBoundingClientRect(); if (rc.top < rp.top + 8 || rc.bottom > rp.bottom - 8) scene.scrollTo({ top: Math.max(0, scene.scrollTop + rc.top - rp.top - 70), behavior: reduit ? "auto" : "smooth" }); }
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
    if (a.type === "graphe") {
      var bascule = function () { var w = scene.clientWidth; if (w) el.classList.toggle("a-mode-pile", w < (a.min || 560) - 8); };
      bascule();
      if (window.ResizeObserver) new ResizeObserver(bascule).observe(scene); else window.addEventListener("resize", bascule);
    }
    appliquer();
  }
  window.HLPANIM = { monter: function (racine) { Array.prototype.forEach.call((racine || document).querySelectorAll("[data-anim]"), monterUn); } };
})();
