(function () {
  "use strict";

  /* ---------- outils ---------- */
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function sansAccent(s) { return String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function texteDe(html) { return String(html).replace(/<span class="mono">[^<]*<\/span>/g, " ").replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim(); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function fr(n, d) {
    if (!isFinite(n)) return "—";
    var s = n.toFixed(d === undefined ? 1 : d);
    var neg = s.charAt(0) === "-"; if (neg) s = s.slice(1);
    var p = s.split("."); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (neg ? "−" : "") + p.join(",");
  }
  function mouvement() {
    return document.documentElement.classList.contains("mo") &&
      !(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  }

  var IC = {
    menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
    loupe: '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>',
    theme: '<circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 0 0 16z" fill="currentColor"/>',
    maison: '<path d="M4 11 12 4l8 7v9h-5v-6H9v6H4z"/>',
    croiss: '<path d="M4 19h16"/><path d="M5 15l4-4 3 3 6-7"/><path d="M14 7h4v4"/>',
    globe: '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.5 2.4 2.5 13.6 0 16M12 4c-2.5 2.4-2.5 13.6 0 16"/>',
    strates: '<path d="m12 4 8 4-8 4-8-4z"/><path d="m4 12 8 4 8-4"/><path d="m4 16 8 4 8-4"/>',
    ecole: '<path d="m3 9 9-4 9 4-9 4z"/><path d="M7 11v4c3 2 7 2 10 0v-4"/><path d="M21 9v5"/>',
    epreuve: '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="m10 14 2 2 4-4"/>',
    calc: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M16 11v6M8 15h2M12 15h2"/>',
    cartes: '<rect x="3" y="6" width="13" height="14" rx="2"/><path d="M8 3h11a2 2 0 0 1 2 2v12"/>',
    livre: '<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v14c-3-1-6-1-8 1-2-2-5-2-8-1z"/><path d="M12 6v14"/>',
    lien: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    gens: '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c3 .2 5.5 2.5 5.5 5.8"/>',
    imprimer: '<path d="M7 9V3h10v6"/><rect x="4" y="9" width="16" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    croix: '<path d="M6 6l12 12M18 6 6 18"/>',
    cible: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    horloge: '<circle cx="12" cy="12" r="8"/><path d="M12 7v5l3 2"/>'
  };
  function ic(n, cl) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' + (cl ? ' class="' + cl + '"' : "") + ">" + IC[n] + "</svg>"; }
  var ICQ = { e1: "croiss", e2: "globe", s1: "strates", s2: "ecole" };

  /* ---------- programme ---------- */
  var QS = {};
  PROG.forEach(function (c) { c.qs.forEach(function (q) { q.champ = c.nom; q.champId = c.id; QS[q.id] = q; }); });

  /* ---------- couches (menu, recherche) : bouton retour du téléphone ---------- */
  var couche = null, apres = null;
  function montrerCouche(nom, on) {
    if (nom === "menu") { $("#lat").classList.toggle("ouv", on); $("#voile").classList.toggle("on", on); $("#b-menu").setAttribute("aria-expanded", on ? "true" : "false"); }
    if (nom === "srch") { $("#srch").classList.toggle("on", on); document.body.style.overflow = on ? "hidden" : ""; }
  }
  function ouvrir(nom) {
    if (couche) return;
    couche = nom; montrerCouche(nom, true);
    try { history.pushState({ couche: nom }, "", location.href); } catch (e) { }
  }
  function fermer(aller) {
    if (!couche) { if (aller) location.hash = aller; return; }
    apres = aller || null;
    history.back();
  }
  window.addEventListener("popstate", function () {
    if (couche) {
      var c = couche; couche = null; montrerCouche(c, false);
      if (c === "srch") { var b = $("#q-ouvrir"); if (b) try { b.focus({ preventScroll: true }); } catch (e) { } }
      if (apres) { var g = apres; apres = null; if (location.hash === g) rendre(); else location.hash = g; }
    }
  });

  /* ---------- thème ---------- */
  function themeActuel() {
    var t = document.documentElement.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function basculerTheme() {
    var n = themeActuel() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", n);
    var m = $('meta[name="theme-color"]'); if (m) m.setAttribute("content", n === "dark" ? "#0D181C" : "#F6F3EC");
  }

  /* ---------- navigation latérale ---------- */
  function navHTML() {
    var h = '<a class="logo" href="#accueil">Faits <i>&amp;</i> Courbes</a><div class="tag">Le magazine de révision de SES · spécialité Terminale</div><nav class="nav" aria-label="Sommaire">';
    h += '<a href="#accueil" data-r="accueil">' + ic("maison") + "Accueil · le programme</a>";
    PROG.forEach(function (c) {
      h += '<div class="nav-t">' + esc(c.nom) + "</div>";
      c.qs.forEach(function (q) {
        h += '<a href="#' + q.id + '" data-r="' + q.id + '"><span class="pc">' + esc(q.code) + "</span>" + esc(q.court) + (q.statut === "bt" ? '<span class="bt">Bientôt</span>' : "") + "</a>";
      });
    });
    h += '<div class="nav-t">Boîte à outils</div>';
    h += '<a href="#epreuve" data-r="epreuve">' + ic("epreuve") + "L'épreuve et la méthode</a>";
    h += '<a href="#outils" data-r="outils">' + ic("calc") + "Savoir-faire et calculatrice</a>";
    h += '<a href="#entrainement" data-r="entrainement">' + ic("cible") + "Entraînement</a>";
    h += '<a href="#auteurs" data-r="auteurs">' + ic("gens") + "Les auteurs</a>";
    h += '<a href="#ressources" data-r="ressources">' + ic("lien") + "Ressources</a>";
    h += '</nav><div class="lat-bas">Programme officiel de 2019 (BO spécial n°&nbsp;8 du 25/07/2019) ; épreuve définie par la note de service du 11/09/2026 (session 2027).</div>';
    return h;
  }

  /* ---------- chaînes causales (SVG construit étape par étape) ---------- */
  var mesureCtx = null;
  function largeurTexte(t, police) {
    if (!mesureCtx) mesureCtx = document.createElement("canvas").getContext("2d");
    mesureCtx.font = police; return mesureCtx.measureText(t).width;
  }
  function couper(t, larg, police) {
    var mots = t.split(" "), lignes = [], cur = "";
    mots.forEach(function (m) {
      var essai = cur ? cur + " " + m : m;
      if (largeurTexte(essai, police) > larg && cur) { lignes.push(cur); cur = m; } else cur = essai;
    });
    if (cur) lignes.push(cur);
    return lignes;
  }
  function chaineSVG(spec) {
    var W = 340, P = 2, LH = 18, PADV = 9, GAP = 36;
    var famille = getComputedStyle(document.body).fontFamily;
    var police = "14px " + famille;
    var y = 4, parts = [], fleches = [];
    var prev = null;
    spec.e.forEach(function (el, i) {
      var noeuds = el.f ? el.f : [el];
      var n = noeuds.length, gapH = 10, w = (W - 2 * P - gapH * (n - 1)) / n;
      if (i > 0) y += GAP;
      var hauteurs = noeuds.map(function (nd) { return couper(nd.t, w - 20, police).length * LH + 2 * PADV; });
      var h = Math.max.apply(null, hauteurs);
      var grp = '<g class="et' + (i > 0 ? " cache" : "") + '" data-i="' + i + '" data-b="' + Math.ceil(y + h) + '">';
      var cur = [];
      noeuds.forEach(function (nd, k) {
        var x = P + k * (w + gapH);
        var lignes = couper(nd.t, w - 20, police);
        var ty = y + (h - lignes.length * LH) / 2 + LH - 5;
        grp += '<g class="nd k-' + (nd.k || "meca") + '"><rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="10"/>';
        lignes.forEach(function (l, j) { grp += '<text x="' + (x + w / 2) + '" y="' + (ty + j * LH) + '" text-anchor="middle">' + esc(l) + "</text>"; });
        grp += "</g>";
        cur.push({ cx: x + w / 2, top: y, bot: y + h });
      });
      if (prev) {
        prev.forEach(function (a) {
          cur.forEach(function (b) {
            var y1 = a.bot + 2, y2 = b.top - 3;
            var d = Math.abs(a.cx - b.cx) < 1 ? "M" + a.cx + " " + y1 + "V" + (y2 - 6) : "M" + a.cx + " " + y1 + "C" + a.cx + " " + (y1 + 18) + " " + b.cx + " " + (y2 - 22) + " " + b.cx + " " + (y2 - 6);
            grp += '<path class="fl" d="' + d + '"/><path class="tete-fl" d="M' + (b.cx - 5) + " " + (y2 - 7) + "L" + (b.cx + 5) + " " + (y2 - 7) + "L" + b.cx + " " + (y2 + 1) + 'z"/>';
          });
        });
        if (el.a) {
          var lx = cur.length === 1 && prev.length === 1 ? cur[0].cx + 10 : W / 2 + 10;
          grp += '<text class="fl-t" x="' + lx + '" y="' + (y - GAP / 2 + 4) + '">' + esc(el.a) + "</text>";
        }
      }
      grp += "</g>";
      parts.push(grp);
      prev = cur; y += h;
    });
    var H = y + 6;
    return '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(spec.t + " : " + spec.e.map(function (e) { return e.f ? e.f.map(function (x) { return x.t; }).join(" et ") : e.t; }).join(" → ")) + '">' + parts.join("") + "</svg>";
  }
  function texteChaine(spec) { return spec.e.map(function (e) { return e.f ? "[" + e.f.map(function (x) { return x.t; }).join(" + ") + "]" : e.t; }).join(" → "); }
  function monterChaines(racine) {
    $$("[data-chain]", racine).forEach(function (d) {
      var spec = CHAINES[d.getAttribute("data-chain")]; if (!spec) return;
      var n = spec.e.length;
      d.className = "chaine";
      d.innerHTML = '<div class="ct">' + esc(spec.t) + "</div>" + chaineSVG(spec) +
        '<div class="btns noprint"><button class="btn p" data-a="suiv">Étape suivante</button><button class="btn" data-a="tout">Tout voir</button><button class="btn" data-a="zero" aria-label="Recommencer">↺</button><span class="cpt" aria-live="polite">1 / ' + n + "</span></div>" +
        (spec.n ? '<p class="src-l">' + spec.n + "</p>" : "");
      var vu = 1;
      function maj(anim) {
        $$(".et", d).forEach(function (g) {
          var i = +g.getAttribute("data-i");
          var montre = i < vu;
          g.classList.toggle("cache", !montre);
          if (montre && anim && i === vu - 1 && mouvement()) {
            g.classList.remove("vient"); void g.getBBox; g.classList.add("vient");
            $$(".fl", g).forEach(function (f) { f.classList.remove("vient"); void f.getBBox; f.classList.add("vient"); });
          }
        });
        var bas = 0; $$(".et", d).forEach(function (g) { if (+g.getAttribute("data-i") < vu) bas = Math.max(bas, +g.getAttribute("data-b")); });
        $("svg", d).setAttribute("viewBox", "0 0 340 " + (bas + 6));
        $(".cpt", d).textContent = vu + " / " + n;
        $('[data-a="suiv"]', d).disabled = vu >= n;
      }
      d.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        var a = b.getAttribute("data-a");
        if (a === "suiv" && vu < n) { vu++; maj(true); }
        else if (a === "tout") { vu = n; maj(false); }
        else if (a === "zero") { vu = 1; maj(false); }
      });
      maj(false);
    });
  }

  /* ---------- graphiques ---------- */
  function echelle(min, max, n) {
    var brut = (max - min) / n, p = Math.pow(10, Math.floor(Math.log10(brut))), f = brut / p;
    var pas = (f < 1.5 ? 1 : f < 3 ? 2 : f < 7 ? 5 : 10) * p;
    var t = [], v = Math.floor(min / pas) * pas;
    while (v <= max + pas * 0.001) { t.push(+v.toFixed(6)); v += pas; }
    if (t[t.length - 1] < max) t.push(+(t[t.length - 1] + pas).toFixed(6));
    return t;
  }
  function graphe(g, W) {
    var u = g.unite || "", dec = g.dec === undefined ? 1 : g.dec;
    var H = Math.round((g.h || 300) * (W < 500 ? 0.95 : 1)), ml = 40, mr = 12, mt = 14, mb = 30, s = "";
    if (g.type === "hbarres") {
      var nc = g.cats.length, ns = g.series.length, bh = ns > 1 ? 14 : 20, gh0 = bh * ns + 16;
      var lab = Math.min(g.lab || 190, Math.round(W * 0.42)); ml = lab;
      var policeLb = "12px " + getComputedStyle(document.body).fontFamily;
      var lignesC = g.cats.map(function (c) { return couper(c, ml - 14, policeLb); });
      var hC = lignesC.map(function (l) { return Math.max(gh0, l.length * 14 + 12); });
      var yC = [], cumul = mt; hC.forEach(function (h) { yC.push(cumul); cumul += h; });
      H = cumul + 26;
      var vals = []; g.series.forEach(function (sr) { vals = vals.concat(sr.v); });
      var mn = Math.min(0, Math.min.apply(null, vals)), mx = Math.max.apply(null, vals);
      var tk = echelle(mn, mx, 4), a = tk[0], b = tk[tk.length - 1];
      var X = function (v) { return ml + (v - a) / (b - a) * (W - ml - mr - 30); };
      tk.forEach(function (t) { s += '<line class="ax' + (t === 0 ? "0" : "") + '" x1="' + X(t) + '" x2="' + X(t) + '" y1="' + mt + '" y2="' + (H - 22) + '"/><text class="lb" x="' + X(t) + '" y="' + (H - 6) + '" text-anchor="middle">' + fr(t, 0) + u + "</text>"; });
      g.cats.forEach(function (c, i) {
        var gh = hC[i], y0 = yC[i], lignes = lignesC[i], yb = y0 + (gh - bh * ns) / 2;
        lignes.forEach(function (l, j) { s += '<text class="lb" x="' + (ml - 8) + '" y="' + (y0 + gh / 2 + 4 - (lignes.length - 1) * 7 + j * 14) + '" text-anchor="end" style="font-size:12px;fill:var(--encre)">' + esc(l) + "</text>"; });
        g.series.forEach(function (sr, k) {
          var v = sr.v[i], x1 = X(Math.min(0, v)), x2 = X(Math.max(0, v)), y = yb + k * bh;
          s += '<rect class="hb c' + (sr.c || k + 1) + '" style="animation-delay:' + (i * 50) + 'ms" x="' + x1 + '" y="' + y + '" width="' + Math.max(1, x2 - x1) + '" height="' + (bh - 3) + '" rx="3" data-tip="' + esc((ns > 1 ? sr.n + " · " : "") + c) + '" data-v="' + v + '"><title>' + esc(c + " : " + fr(v, dec) + u) + "</title></rect>";
          s += '<text class="lbv" x="' + (v < 0 ? x1 - 4 : x2 + 4) + '" y="' + (y + bh - 6) + '" text-anchor="' + (v < 0 ? "end" : "start") + '">' + fr(v, dec) + u + "</text>";
        });
      });
    } else {
      var xs = g.x, n = xs.length, all = [];
      var series = g.type === "barres" ? [{ n: g.n || "", v: g.y, c: 1 }] : g.series;
      series.forEach(function (sr) { all = all.concat(sr.v.filter(function (v) { return v !== null; })); });
      var mn2 = g.min !== undefined ? g.min : Math.min(0, Math.min.apply(null, all)), mx2 = g.max !== undefined ? g.max : Math.max.apply(null, all);
      var tk2 = echelle(mn2, mx2, 5), a2 = tk2[0], b2 = tk2[tk2.length - 1];
      var step = (W - ml - mr) / n;
      var Xc = function (i) { return ml + step * (i + 0.5); };
      var Y = function (v) { return mt + (b2 - v) / (b2 - a2) * (H - mt - mb); };
      (g.bandes || []).forEach(function (bd) {
        var i1 = xs.indexOf(bd.de), i2 = xs.indexOf(bd.a);
        if (i1 < 0 || i2 < 0) return;
        s += '<rect x="' + (Xc(i1) - step / 2) + '" y="' + mt + '" width="' + (step * (i2 - i1 + 1)) + '" height="' + (H - mt - mb) + '" fill="var(--moutarde-c)" opacity=".7"/>';
        s += '<text class="lb" x="' + (Xc(i1) - step / 2 + 4) + '" y="' + (mt + 12) + '" style="font-weight:700;fill:var(--encre)">' + esc(bd.l) + "</text>";
      });
      tk2.forEach(function (t) { s += '<line class="ax' + (t === 0 ? "0" : "") + '" x1="' + ml + '" x2="' + (W - mr) + '" y1="' + Y(t) + '" y2="' + Y(t) + '"/><text class="lb" x="' + (ml - 6) + '" y="' + (Y(t) + 4) + '" text-anchor="end">' + fr(t, 0) + u + "</text>"; });
      var pas = g.pasX || Math.ceil(n / 8);
      xs.forEach(function (x, i) { if (i % pas === 0 || i === n - 1) s += '<text class="lb" x="' + Xc(i) + '" y="' + (H - 10) + '" text-anchor="middle">' + x + "</text>"; });
      if (g.type === "barres") {
        g.y.forEach(function (v, i) {
          var y1 = Y(Math.max(0, v)), y2 = Y(Math.min(0, v));
          s += '<rect class="bar' + (v < 0 ? " neg c2" : " c1") + '" style="animation-delay:' + Math.round(i * 600 / n) + 'ms" x="' + (Xc(i) - step * 0.36) + '" y="' + y1 + '" width="' + (step * 0.72) + '" height="' + Math.max(0.8, y2 - y1) + '"/>';
        });
        (g.notes || []).forEach(function (nt) {
          var i = xs.indexOf(nt.x); if (i < 0) return;
          s += '<text class="lb" x="' + Xc(i) + '" y="' + (Y(nt.y) + (nt.y < 0 ? 14 : -5)) + '" text-anchor="' + (nt.ancre || "middle") + '" style="font-weight:700;fill:var(--encre)">' + esc(nt.t) + "</text>";
        });
      } else {
        series.forEach(function (sr, k) {
          var d = "", on = false;
          sr.v.forEach(function (v, i) { if (v === null) { on = false; return; } d += (on ? "L" : "M") + Xc(i).toFixed(1) + " " + Y(v).toFixed(1); on = true; });
          s += '<g class="sr" data-k="' + k + '"><path class="ligne c' + (sr.c || k + 1) + '" d="' + d + '" fill="none" stroke-width="2.6" stroke-linejoin="round" style="fill:none"/>';
          var last = sr.v.length - 1; while (last > 0 && sr.v[last] === null) last--;
          s += '<circle class="c' + (sr.c || k + 1) + '" cx="' + Xc(last) + '" cy="' + Y(sr.v[last]) + '" r="3.5"/></g>';
        });
        s += '<line class="curseur" x1="0" x2="0" y1="' + mt + '" y2="' + (H - mb) + '" stroke="var(--encre2)" stroke-dasharray="3 3" style="display:none"/>';
      }
    }
    var leg = "";
    if (g.type === "lignes" || (g.type === "hbarres" && g.series.length > 1)) {
      leg = '<div class="leg">' + g.series.map(function (sr, k) {
        return '<button type="button" data-k="' + k + '"' + (g.type === "hbarres" ? " disabled" : "") + '><i class="c' + (sr.c || k + 1) + '" style="background:currentColor"></i>' + esc(sr.n) + "</button>";
      }).join("") + "</div>";
    }
    return '<p class="gt">' + esc(g.t) + "</p>" + (g.s ? '<p class="gs">' + esc(g.s) + "</p>" : "") + leg +
      '<div class="zone"><svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(g.t) + '">' + s + '</svg><div class="bulle"></div></div>' +
      '<p class="src-l">' + g.src + "</p>";
  }
  function monterGraphes(racine) {
    $$("[data-graph]", racine).forEach(function (d) {
      var g = GRAPHES[d.getAttribute("data-graph")]; if (!g) return;
      d.className = "graph";
      var W = Math.round(Math.max(320, Math.min(720, (d.clientWidth || 340) - 26)));
      d.innerHTML = graphe(g, W);
      $$(".leg button", d).forEach(function (b) { var c = $("i", b); c.style.color = getComputedStyle(c).fill || ""; });
      var svg = $("svg", d), bulle = $(".bulle", d), zone = $(".zone", d), u = g.unite || "", dec = g.dec === undefined ? 1 : g.dec;
      var cach = {};
      $$(".leg button", d).forEach(function (b) {
        if (b.disabled) return;
        b.addEventListener("click", function () {
          var k = b.getAttribute("data-k"); cach[k] = !cach[k]; b.classList.toggle("off", cach[k]);
          var gr = $('.sr[data-k="' + k + '"]', svg); if (gr) gr.style.display = cach[k] ? "none" : "";
        });
      });
      function point(e) {
        var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
        return pt.matrixTransform(svg.getScreenCTM().inverse());
      }
      function placer(e, html) {
        var r = zone.getBoundingClientRect();
        bulle.innerHTML = html; bulle.style.display = "block";
        var x = e.clientX - r.left + zone.scrollLeft, y = e.clientY - r.top;
        var bw = bulle.offsetWidth / 2;
        x = Math.max(bw + 2, Math.min(zone.clientWidth - bw - 2, x));
        bulle.style.left = x + "px"; bulle.style.top = Math.max(y, 50) + "px";
      }
      function cacher() { bulle.style.display = "none"; var c = $(".curseur", svg); if (c) c.style.display = "none"; }
      svg.addEventListener("pointerleave", cacher);
      svg.addEventListener("pointermove", function (e) {
        if (g.type === "hbarres") {
          var t = e.target.closest("rect.hb");
          if (!t) { cacher(); return; }
          placer(e, esc(t.getAttribute("data-tip")) + "<br><b>" + fr(+t.getAttribute("data-v"), dec) + u + "</b>");
          return;
        }
        var p = point(e), ml = 40, mr = 12, n = g.x.length, step = (W - ml - mr) / n;
        var i = Math.floor((p.x - ml) / step);
        if (i < 0 || i >= n) { cacher(); return; }
        var h = "<b>" + esc(g.x[i]) + "</b>";
        if (g.type === "barres") h += " · " + fr(g.y[i], dec) + u + (g.etiquette ? " " + esc(g.etiquette) : "");
        else g.series.forEach(function (sr, k) { if (!cach[k] && sr.v[i] !== null) h += "<br>" + esc(sr.n) + " : " + fr(sr.v[i], dec) + u; });
        var c = $(".curseur", svg);
        if (c) { var cx = ml + step * (i + 0.5); c.setAttribute("x1", cx); c.setAttribute("x2", cx); c.style.display = ""; }
        placer(e, h);
      });
    });
  }

  /* ---------- QCM ---------- */
  function lienIdee(q) { return q.s ? "#" + q.ch + ":" + q.s : "#" + q.ch; }
  function monterQuiz(el, questions, titre) {
    var liste = melange(questions), i = 0, bons = 0, rates = [];
    function etape() {
      if (i >= liste.length) {
        var pc = Math.round(100 * bons / liste.length);
        el.innerHTML = '<div class="q-carte"><span class="kick c">' + esc(titre) + '</span><div class="score">' + bons + " / " + liste.length + "</div><p>" +
          (pc >= 80 ? "Très solide. Passe aux sujets type bac." : pc >= 50 ? "Bonne base : reprends les paragraphes ci-dessous." : "Relis le cours, puis refais le quiz : c'est en se testant qu'on retient.") + "</p>" +
          (rates.length ? "<h4>À revoir</h4><ul>" + rates.map(function (q) { return '<li><a href="' + lienIdee(q) + '">' + esc(q.q) + "</a></li>"; }).join("") + "</ul>" : "") +
          '<div class="btns"><button class="btn p" data-a="re">Refaire (nouvel ordre)</button></div></div>';
        $('[data-a="re"]', el).onclick = function () { monterQuiz(el, questions, titre); };
        return;
      }
      var q = liste[i], ordre = melange(q.c.map(function (c, k) { return k; }));
      el.innerHTML = '<div class="q-carte"><span class="kick c">' + esc(titre) + " · question " + (i + 1) + " / " + liste.length + (q.chNom ? " · " + esc(q.chNom) : "") + '</span><div class="q-prog"><i style="width:' + (100 * i / liste.length) + '%"></i></div>' +
        '<p class="q-q">' + q.q + '</p><div class="q-ch">' + ordre.map(function (k) { return '<button type="button" data-k="' + k + '">' + q.c[k] + "</button>"; }).join("") + '</div><div class="q-fin"></div></div>';
      $$(".q-ch button", el).forEach(function (b) {
        b.addEventListener("click", function () {
          var k = +b.getAttribute("data-k"), ok = k === q.r;
          if (ok) bons++; else rates.push(q);
          $$(".q-ch button", el).forEach(function (x) {
            x.disabled = true;
            if (+x.getAttribute("data-k") === q.r) x.classList.add("bon");
          });
          if (!ok) b.classList.add("faux");
          $(".q-fin", el).innerHTML = '<div class="q-exp"><b class="' + (ok ? "v" : "f") + '">' + (ok ? "Exact." : "Non.") + "</b> " + q.e +
            '<div class="btns"><a class="btn" href="' + lienIdee(q) + '">Revoir le paragraphe</a><button class="btn p" data-a="n">' + (i + 1 < liste.length ? "Question suivante" : "Voir le score") + "</button></div></div>";
          $('[data-a="n"]', el).onclick = function () { i++; etape(); var t = el.getBoundingClientRect().top; if (t < 0) el.scrollIntoView(); };
        });
      });
    }
    etape();
  }

  /* ---------- flashcards ---------- */
  function monterCartes(el, cartes, titre) {
    var pile = melange(cartes), i = 0, sues = 0, revoir = [];
    function etape() {
      if (i >= pile.length) {
        el.innerHTML = '<div class="q-carte"><span class="kick c">' + esc(titre) + '</span><div class="score">' + sues + " / " + pile.length + "</div><p>cartes sues du premier coup.</p>" +
          '<div class="btns">' + (revoir.length ? '<button class="btn p" data-a="rv">Revoir les ' + revoir.length + " cartes ratées</button>" : "") + '<button class="btn" data-a="re">Tout recommencer</button></div></div>';
        var rv = $('[data-a="rv"]', el); if (rv) rv.onclick = function () { pile = melange(revoir); revoir = []; sues = 0; i = 0; etape(); };
        $('[data-a="re"]', el).onclick = function () { monterCartes(el, cartes, titre); };
        return;
      }
      var c = pile[i];
      el.innerHTML = '<span class="kick c">' + esc(titre) + " · carte " + (i + 1) + " / " + pile.length + '</span><div class="q-prog"><i style="width:' + (100 * i / pile.length) + '%"></i></div>' +
        '<div class="fc-zone"><button type="button" class="fc" aria-label="Retourner la carte"><div class="fa r"><span class="k">' + esc(c.chNom || "Recto") + '</span><span class="t">' + c.r + '</span><span class="h">Touche pour retourner</span></div><div class="fa v"><span class="k">Verso</span><span class="t">' + c.v + "</span></div></button></div>" +
        '<div class="btns"><button class="btn c" data-a="non">À revoir</button><button class="btn p" data-a="oui">Je savais</button></div>';
      var fc = $(".fc", el);
      fc.addEventListener("click", function () {
        if (mouvement()) { fc.classList.remove("tourne-anim"); void fc.offsetWidth; fc.classList.add("tourne-anim"); setTimeout(function () { fc.classList.toggle("tourne"); }, 220); }
        else fc.classList.toggle("tourne");
      });
      $('[data-a="oui"]', el).onclick = function () { sues++; i++; etape(); };
      $('[data-a="non"]', el).onclick = function () { revoir.push(c); i++; etape(); };
    }
    etape();
  }

  /* ---------- relier l'auteur à sa théorie ---------- */
  function monterRelier(el) {
    var lot = melange(AUTEURS).slice(0, 5), gauche = melange(lot), droite = melange(lot), sel = null, trouves = 0, essais = 0;
    el.innerHTML = '<p>Touche un auteur, puis l\'idée qui lui correspond. ' + '<span class="cpt"></span></p><div class="rel"><div class="col">' +
      gauche.map(function (a) { return '<button type="button" data-g="' + esc(a.n) + '"><span class="an">' + esc(a.n) + "</span></button>"; }).join("") +
      '</div><div class="col">' + droite.map(function (a) { return '<button type="button" data-d="' + esc(a.n) + '">' + esc(a.th) + "</button>"; }).join("") +
      '</div></div><div class="btns"><button class="btn p" data-a="nv">Nouvelle série</button></div><div class="rel-fin"></div>';
    $('[data-a="nv"]', el).onclick = function () { monterRelier(el); };
    el.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b || b.classList.contains("ok")) return;
      if (b.hasAttribute("data-g")) { $$("[data-g]", el).forEach(function (x) { x.classList.remove("sel"); }); b.classList.add("sel"); sel = b; return; }
      if (b.hasAttribute("data-d")) {
        if (!sel) { b.classList.add("ko"); setTimeout(function () { b.classList.remove("ko"); }, 400); return; }
        essais++;
        if (sel.getAttribute("data-g") === b.getAttribute("data-d")) {
          sel.classList.remove("sel"); sel.classList.add("ok"); b.classList.add("ok"); sel = null; trouves++;
          if (trouves === lot.length) $(".rel-fin", el).innerHTML = '<div class="q-exp"><b class="v">Bravo !</b> ' + trouves + " paires en " + essais + " essais. Revois les fiches des auteurs dans <a href=\"#auteurs\">Les auteurs</a>.</div>";
        } else { b.classList.add("ko"); setTimeout(function () { b.classList.remove("ko"); }, 400); }
      }
    });
  }

  /* ---------- calculatrice de savoir-faire ---------- */
  function nombre(v) { v = String(v).replace(/\s/g, "").replace(",", ".").replace("−", "-"); return v === "" ? NaN : +v; }
  function monterCalc(el) {
    var mode = "deux";
    function dessiner() {
      var h = '<div class="seg" role="tablist"><button data-m="deux"' + (mode === "deux" ? ' class="act"' : "") + '>Deux valeurs</button><button data-m="conv"' + (mode === "conv" ? ' class="act"' : "") + '>Convertir</button><button data-m="moy"' + (mode === "moy" ? ' class="act"' : "") + ">Taux cumulé et moyen</button></div>";
      if (mode === "deux") h += '<div class="champs"><label>Valeur de départ (V<sub>d</sub>)<input inputmode="decimal" id="c-a" value="309,1"></label><label>Valeur d\'arrivée (V<sub>a</sub>)<input inputmode="decimal" id="c-b" value="2646,7"></label></div><p class="src-l">Exemple chargé : PIB de la France en volume, 1950 et 2025 (milliards d\'euros 2020, Insee).</p>';
      if (mode === "conv") h += '<div class="champs"><label>Taux de variation (%)<input inputmode="decimal" id="c-t" value="25"></label><label>Coefficient multiplicateur<input inputmode="decimal" id="c-c" value="1,25"></label><label>Indice (base 100 au départ)<input inputmode="decimal" id="c-i" value="125"></label></div><p class="src-l">Change une case : les deux autres suivent.</p>';
      if (mode === "moy") h += '<div class="champs"><label>Taux successifs en %, séparés par « ; »<input id="c-s" value="2,7 ; 1,6 ; 1,5 ; 0,8"></label></div><p class="src-l">Exemple chargé : croissance du PIB en volume de 2022 à 2025 (Insee).</p>';
      h += '<div class="res"></div><div class="phr"></div>';
      el.innerHTML = h;
      $$(".seg button", el).forEach(function (b) { b.onclick = function () { mode = b.getAttribute("data-m"); dessiner(); }; });
      $$("input", el).forEach(function (inp) { inp.addEventListener("input", function () { calculer(inp.id); }); });
      calculer();
    }
    function res(items, phrase) {
      $(".res", el).innerHTML = items.map(function (x) { return "<div><b>" + x[1] + "</b><span>" + x[0] + "</span></div>"; }).join("");
      $(".phr", el).innerHTML = phrase;
    }
    function calculer(source) {
      if (mode === "deux") {
        var a = nombre($("#c-a", el).value), b = nombre($("#c-b", el).value);
        if (!isFinite(a) || !isFinite(b) || a === 0) { res([], "Entre deux nombres (le premier non nul)."); return; }
        var cm = b / a, t = (cm - 1) * 100;
        res([["Taux de variation = (V<sub>a</sub> − V<sub>d</sub>) / V<sub>d</sub> × 100", (t > 0 ? "+" : "") + fr(t, 1) + " %"], ["Coefficient multiplicateur = V<sub>a</sub> / V<sub>d</sub>", "× " + fr(cm, 2)], ["Indice de V<sub>a</sub>, base 100 = V<sub>d</sub>", fr(cm * 100, 1)], ["Variation absolue V<sub>a</sub> − V<sub>d</sub>", fr(b - a, 1)]],
          "Phrase type : « Entre les deux dates, la valeur a été multipliée par " + fr(cm, 2) + ", soit " + (t >= 0 ? "une hausse" : "une baisse") + " de " + fr(Math.abs(t), 1) + " %. »" + (cm >= 2 ? " Quand le coefficient dépasse 2, préfère « multipliée par » : c'est plus parlant qu'un pourcentage." : ""));
      } else if (mode === "conv") {
        var ti = $("#c-t", el), ci = $("#c-c", el), ii = $("#c-i", el), cmv;
        if (source === "c-c") cmv = nombre(ci.value); else if (source === "c-i") cmv = nombre(ii.value) / 100; else cmv = 1 + nombre(ti.value) / 100;
        if (!isFinite(cmv)) { res([], ""); return; }
        if (source !== "c-t") ti.value = fr((cmv - 1) * 100, 2).replace("−", "-");
        if (source !== "c-c") ci.value = fr(cmv, 4).replace("−", "-");
        if (source !== "c-i") ii.value = fr(cmv * 100, 2).replace("−", "-");
        res([["Coefficient multiplicateur", "× " + fr(cmv, 4)], ["Taux de variation", fr((cmv - 1) * 100, 2) + " %"], ["Indice (base 100)", fr(cmv * 100, 2)]],
          "Les trois disent la même chose : CM = 1 + t/100 et indice = CM × 100. Un indice de " + fr(cmv * 100, 1) + " signifie " + (cmv >= 1 ? "une hausse" : "une baisse") + " de " + fr(Math.abs(cmv - 1) * 100, 1) + " % par rapport à la base.");
      } else {
        var ts = $("#c-s", el).value.split(";").map(nombre).filter(isFinite);
        if (!ts.length) { res([], "Entre au moins un taux."); return; }
        var cmg = ts.reduce(function (p, x) { return p * (1 + x / 100); }, 1), n = ts.length, moy = (Math.pow(cmg, 1 / n) - 1) * 100;
        var somme = ts.reduce(function (p, x) { return p + x; }, 0);
        res([["Coefficient multiplicateur global = produit des (1 + t/100)", "× " + fr(cmg, 4)], ["Taux de variation cumulé", fr((cmg - 1) * 100, 2) + " %"], ["Taux de variation annuel moyen = CM<sup>1/n</sup> − 1", fr(moy, 2) + " % par an"], ["Somme des taux (à ne pas confondre)", fr(somme, 2) + " %"]],
          "Sur " + n + " période" + (n > 1 ? "s" : "") + ", la valeur est multipliée par " + fr(cmg, 3) + " : hausse cumulée de " + fr((cmg - 1) * 100, 1) + " %, soit " + fr(moy, 2) + " % par période en moyenne. On ne fait jamais la somme des taux : ils ne s'appliquent pas à la même base.");
      }
    }
    dessiner();
  }

  /* ---------- montage commun ---------- */
  function monter(racine) {
    monterChaines(racine); monterGraphes(racine);
    if (window.ANIM_MOTEUR) ANIM_MOTEUR.monter(racine);
    $$("[data-calc]", racine).forEach(function (d) { d.className = "calc"; monterCalc(d); });
    $$("[data-relier]", racine).forEach(function (d) { monterRelier(d); });
  }

  /* ---------- vues ---------- */
  function sparkline(id) {
    var g = GRAPHES[id]; if (!g) return "";
    var v = g.type === "barres" ? g.y : g.series[g.spark || 0].v.filter(function (x) { return x !== null; });
    var mn = Math.min.apply(null, v), mx = Math.max.apply(null, v), w = 64, h = 22;
    var d = v.map(function (y, i) { return (i ? "L" : "M") + (i * w / (v.length - 1)).toFixed(1) + " " + (h - 2 - (y - mn) / (mx - mn || 1) * (h - 4)).toFixed(1); }).join("");
    return '<svg class="spark" viewBox="0 0 64 22" aria-hidden="true"><path d="' + d + '" fill="none" stroke="var(--corail)" stroke-width="1.8"/></svg>';
  }
  function vueAccueil() {
    var h = '<div class="une"><p class="mast">Faits <i>&amp;</i> Courbes</p><div class="reg"><span>SES · spécialité Terminale</span><span>Programme 2019 · bac 2027</span></div>' +
      '<p class="chapo">Le programme de SES décrypté comme un magazine de données : des chiffres vérifiés, des mécanismes qui se construisent sous tes yeux, et tout ce qu\'il faut pour la copie.</p></div>';
    h += '<div class="chiffres">' + ACCUEIL.chiffres.map(function (c) { return '<div class="chiffre"><b>' + c.n + "</b><span>" + c.l + "</span><small>" + c.s + "</small></div>"; }).join("") + "</div>";
    h += '<div class="acces"><a href="#entrainement">' + ic("cible") + 'Entraînement<small>QCM mélangé, cartes, auteurs</small></a><a href="#epreuve">' + ic("epreuve") + 'L\'épreuve<small>Format 2027 et méthode</small></a><a href="#outils">' + ic("calc") + 'Calculatrice<small>Taux, coefficient, indice</small></a></div>';
    h += '<h2 class="sec"><span class="n">Carte</span>Le programme de Terminale</h2><p>Douze questions dans trois champs. Les chapitres rédigés sont ceux qu\'on traite en début d\'année ; les autres affichent déjà les objectifs officiels et les notions à connaître.</p>';
    PROG.forEach(function (c) {
      h += '<section class="champ"><h3>' + esc(c.nom) + "</h3><div class=\"qs\">";
      c.qs.forEach(function (q) {
        var red = q.statut === "red";
        h += '<a class="qc' + (red ? " red" : " bt") + '" href="#' + q.id + '">' + (red && q.spark ? sparkline(q.spark) : "") +
          '<span class="pastille' + (red ? " ok" : " bt") + '">' + (red ? "Rédigé" : "Bientôt") + "</span> " + (q.ecrit ? "" : '<span class="pastille non">Hors écrit</span>') +
          '<span class="qt">' + esc(q.titre) + '</span><span class="qd">' + q.objectifs.length + " objectifs d'apprentissage" + (red ? " · cours, quiz, cartes, sujets corrigés" : " · notions listées") + "</span></a>";
      });
      h += "</div></section>";
    });
    h += '<div class="def"><b>Ce qui tombe à l\'écrit en 2027.</b> La note de service du 11 septembre 2026 liste neuf questions évaluables. Trois questions du programme ne sont pas évaluées à l\'écrit : crises financières, action de l\'École et justice sociale. Elles restent au programme, éclairent les autres chapitres et peuvent nourrir ton Grand oral. <a href="#epreuve">Voir l\'épreuve</a>.</div>';
    return { titre: "Accueil", html: h };
  }

  var ONGLETS = [["", "Cours"], ["fiche", "À retenir"], ["quiz", "Quiz"], ["cartes", "Cartes"], ["bac", "Sujets bac"]];
  function enteteChap(q, ch, sous) {
    var h = '<header class="tete' + (sous ? " court" : "") + '"><span class="kick">' + esc(q.champ) + " · " + esc(q.code) + '</span><h1>' + esc(q.titre) + "</h1>" + (ch.chapo && !sous ? '<p class="chapo">' + ch.chapo + "</p>" : "") +
      (sous ? "" : '<div class="meta">' + (q.ecrit ? '<span class="pastille ok">Évaluable à l\'écrit</span>' : '<span class="pastille non">Non évalué à l\'écrit en 2027</span>') + '<span class="pastille">' + ch.quiz.length + " questions</span><span class=\"pastille\">" + ch.cartes.length + " cartes</span><span class=\"pastille\">" + ch.bac.length + " exercices corrigés</span></div>") + "</header>";
    h += '<nav class="onglets" aria-label="Parties du chapitre">' + ONGLETS.map(function (o) {
      return '<a href="#' + q.id + (o[0] ? "/" + o[0] : "") + '"' + (sous === o[0] ? ' class="act" aria-current="page"' : "") + ">" + o[1] + "</a>";
    }).join("") + "</nav>";
    return h;
  }
  function vueChapitre(q, sous) {
    var ch = CH[q.id], h = enteteChap(q, ch, sous);
    if (sous === "") {
      if (!q.ecrit) h += '<div class="attn"><p>La note de service du 11 septembre 2026 ne retient pas cette question parmi celles qui peuvent faire l\'objet d\'un sujet écrit (ni de l\'oral de contrôle). Elle reste au programme et ton professeur la traite : elle est indispensable pour comprendre la mobilité sociale (question évaluable), elle nourrit les copies sur la structure sociale et peut servir au Grand oral. Les exercices de ce chapitre entraînent la méthode du bac.</p></div>';
      h += '<section class="essentiel"><span class="kick">L\'essentiel en 5 lignes</span><ol>' + ch.essentiel.map(function (l) { return "<li><span>" + l + "</span></li>"; }).join("") + "</ol></section>";
      if (ch.chiffres) h += '<div class="chiffres">' + ch.chiffres.map(function (c) { return '<div class="chiffre"><b>' + c.n + "</b><span>" + c.l + "</span><small>" + c.s + "</small></div>"; }).join("") + "</div>";
      h += '<h2 class="sec"><span class="n">BO</span>Ce que le programme attend</h2><ol class="objs">' + ch.objectifs.map(function (o) {
        return "<li>" + o.clair + '<span class="bo">Texte officiel : « ' + esc(o.bo) + " »</span>" + (o.voir ? ' <a href="#' + q.id + ":" + o.voir + '">→ voir le cours</a>' : "") + "</li>";
      }).join("") + "</ol>";
      h += '<h4>Notions à savoir définir</h4><div class="notions">' + ch.notions.map(function (n) { return "<span>" + esc(n) + "</span>"; }).join("") + "</div>";
      ch.sections.forEach(function (s, i) {
        h += '<section class="idee" id="' + s.id + '"><h2 class="sec"><span class="n">' + (i + 1) + "</span>" + esc(s.t) + "</h2>" + s.h + "</section>";
      });
      h += '<section class="idee" id="' + q.id + '-pieges"><h2 class="sec"><span class="n">!</span>Les pièges à éviter</h2>' + ch.pieges.map(function (p) { return '<div class="piege"><span class="f">' + p.f + '</span><span class="v">' + p.v + "</span></div>"; }).join("") + "</section>";
      h += '<div class="btns"><a class="btn p" href="#' + q.id + '/quiz">Faire le quiz</a><a class="btn" href="#' + q.id + '/fiche">Fiche « À retenir »</a><a class="btn" href="#' + q.id + '/bac">Sujets corrigés</a></div>';
    } else if (sous === "fiche") {
      h += '<div class="btns noprint"><button class="btn p" data-a="imprimer">' + ic("imprimer").replace("<svg", '<svg width="18" height="18"') + "Imprimer la fiche</button></div>";
      h += '<article class="fiche"><span class="kick">Fiche · ' + esc(q.champ) + '</span><h2>' + esc(q.titre) + "</h2>" + ch.retenir +
        "<h3>Mécanismes à savoir dérouler</h3>" + ch.chainesFiche.map(function (id) { return '<div class="fchaine"><b>' + esc(CHAINES[id].t) + " :</b> " + esc(texteChaine(CHAINES[id])) + "</div>"; }).join("") + "</article>";
    } else if (sous === "quiz") {
      h += '<div id="zq"></div>';
    } else if (sous === "cartes") {
      h += '<div id="zc"></div>';
    } else if (sous === "bac") {
      h += '<p>Chaque sujet indique son origine : sujet officiel (référence exacte) ou sujet inventé pour le site. Essaie d\'abord, puis ouvre le corrigé.</p>';
      ch.bac.forEach(function (b, i) {
        h += '<article class="exo" id="' + q.id + "-bac-" + i + '"><div class="et"><span class="pastille ok">' + esc(b.type) + '</span><span class="pastille' + (b.officiel ? " bt" : "") + '">' + esc(b.origine) + "</span></div><h3>" + esc(b.t) + '</h3><div class="enon">' + b.enonce + "</div>" +
          (b.methode ? '<details class="pli"><summary>La méthode</summary><div>' + b.methode + "</div></details>" : "") +
          '<details class="corr"><summary>Voir le corrigé</summary>' + b.corrige + "</details></article>";
      });
    }
    return { titre: q.court, html: h, apres: function (r) {
      if (sous === "quiz") monterQuiz($("#zq", r), ch.quiz.map(function (x) { x.ch = q.id; return x; }), "Quiz · " + q.court);
      if (sous === "cartes") monterCartes($("#zc", r), ch.cartes, "Cartes · " + q.court);
      var bp = $('[data-a="imprimer"]', r); if (bp) bp.onclick = function () { window.print(); };
    } };
  }
  function vueBientot(q) {
    var h = '<header class="tete"><span class="kick">' + esc(q.champ) + " · " + esc(q.code) + '</span><h1>' + esc(q.titre) + '</h1><div class="meta"><span class="pastille bt">Bientôt</span>' +
      (q.ecrit ? '<span class="pastille ok">Évaluable à l\'écrit</span>' : '<span class="pastille non">Non évalué à l\'écrit (session 2027)</span>') + "</div></header>";
    h += "<p class=\"lede\">Ce chapitre sera rédigé au fil de l'année. En attendant, voici exactement ce que le programme officiel attend : c'est la liste de contrôle de tes révisions.</p>";
    if (!q.ecrit) h += '<div class="attn"><p>Cette question n\'est pas dans la liste des questions évaluables de la note de service du 11 septembre 2026 (annexe I) : elle ne peut pas faire l\'objet d\'un sujet écrit ni de l\'oral de contrôle. Elle reste au programme : ton professeur la traite, et elle peut servir au Grand oral.</p></div>';
    h += '<h2 class="sec"><span class="n">BO</span>Objectifs d\'apprentissage</h2><ol class="objs">' + q.objectifs.map(function (o) { return "<li>" + esc(o) + "</li>"; }).join("") + "</ol>";
    h += '<h2 class="sec"><span class="n">N</span>Notions à savoir définir et illustrer</h2><div class="notions">' + q.notions.map(function (n) { return "<span>" + esc(n) + "</span>"; }).join("") + "</div>";
    if (q.liens) h += '<h2 class="sec"><span class="n">↗</span>Ce que tu sais déjà</h2><p>' + q.liens + "</p>";
    return { titre: q.court, html: h };
  }
  function vueEpreuve() { return { titre: "L'épreuve", html: EPREUVE }; }
  function vueOutils() { return { titre: "Savoir-faire", html: OUTILS }; }
  function vueRessources() {
    var h = '<header class="tete"><span class="kick">Boîte à outils</span><h1>Ressources vérifiées</h1><p class="chapo">Des liens testés en novembre 2026. Les sources officielles d\'abord, puis les sites des académies, les données, les manuels et les vidéos.</p></header>';
    RESSOURCES.forEach(function (g) {
      h += '<h2 class="sec">' + esc(g.t) + '</h2><ul class="res-l">' + g.l.map(function (r) {
        return '<li><a href="' + esc(r.u) + '" target="_blank" rel="noopener">' + esc(r.n) + "</a>" + (r.b ? '<span class="badge">' + esc(r.b) + "</span>" : "") + "<p>" + r.d + "</p></li>";
      }).join("") + "</ul>";
    });
    return { titre: "Ressources", html: h };
  }
  function vueAuteurs() {
    var h = '<header class="tete"><span class="kick">Boîte à outils</span><h1>Les auteurs du programme</h1><p class="chapo">Qui a dit quoi : les attributions exactes, à citer dans tes copies. Entraîne-toi ensuite à les relier à leurs idées.</p></header>';
    h += '<div class="btns"><a class="btn p" href="#entrainement/relier">Jouer : relie l\'auteur à sa théorie</a></div>';
    ["e1", "e2", "s1", "s2"].forEach(function (id) {
      var q = QS[id];
      h += '<h2 class="sec"><span class="n">' + esc(q.code) + "</span>" + esc(q.court) + '</h2><div class="auts">' + AUTEURS.filter(function (a) { return a.ch === id; }).map(function (a) {
        var ini = a.n.split(/[\s-]+/).filter(function (x) { return /^[A-ZÉ]/.test(x); }).map(function (x) { return x.charAt(0); }).slice(-2).join("");
        return '<div class="aut"><span class="mono">' + esc(ini) + '</span><span class="an">' + esc(a.n) + "<small>" + esc(a.d) + '</small></span><span class="ad">' + a.l + "</span></div>";
      }).join("") + "</div>";
    });
    return { titre: "Auteurs", html: h };
  }
  function vueEntrainement(sous) {
    var tabs = [["", "Quiz mélangé"], ["cartes", "Toutes les cartes"], ["relier", "Relier les auteurs"]];
    var h = '<header class="tete"><span class="kick">Boîte à outils</span><h1>Entraînement</h1><p class="chapo">Se tester est la meilleure façon de retenir. Mélange les chapitres pour forcer ta mémoire à chercher.</p></header>' +
      '<nav class="onglets">' + tabs.map(function (t) { return '<a href="#entrainement' + (t[0] ? "/" + t[0] : "") + '"' + (sous === t[0] ? ' class="act"' : "") + ">" + t[1] + "</a>"; }).join("") + "</nav>";
    if (sous === "relier") h += '<div class="q-carte" data-relier></div>';
    else h += '<div class="seg" id="choix">' + ["e1", "e2", "s1", "s2"].filter(function (id) { return CH[id]; }).map(function (id) { return '<button class="act" data-c="' + id + '">' + esc(QS[id].court) + "</button>"; }).join("") + '</div><div id="ze"></div>';
    return { titre: "Entraînement", html: h, apres: function (r) {
      if (sous === "relier") return;
      var choisis = {}; Object.keys(CH).forEach(function (k) { choisis[k] = 1; });
      function lancer() {
        var ids = Object.keys(choisis).filter(function (k) { return choisis[k]; });
        if (!ids.length) { $("#ze", r).innerHTML = "<p>Choisis au moins un chapitre.</p>"; return; }
        if (sous === "cartes") {
          var cs = []; ids.forEach(function (id) { CH[id].cartes.forEach(function (c) { cs.push({ r: c.r, v: c.v, chNom: QS[id].court }); }); });
          monterCartes($("#ze", r), cs, "Cartes mélangées");
        } else {
          var qs = []; ids.forEach(function (id) { CH[id].quiz.forEach(function (x) { var y = Object.assign({}, x); y.ch = id; y.chNom = QS[id].court; qs.push(y); }); });
          monterQuiz($("#ze", r), melange(qs).slice(0, 15), "Quiz mélangé");
        }
      }
      $$("#choix button", r).forEach(function (b) { b.onclick = function () { var c = b.getAttribute("data-c"); choisis[c] = !choisis[c]; b.classList.toggle("act", !!choisis[c]); lancer(); }; });
      lancer();
    } };
  }

  /* ---------- routeur ---------- */
  function lireRoute() {
    var h = decodeURIComponent(location.hash.replace(/^#/, "")) || "accueil";
    var ancre = null, m = h.match(/^([^:]+):(.+)$/);
    if (m) { h = m[1]; ancre = m[2]; }
    var p = h.split("/");
    return { page: p[0], sous: p[1] || "", ancre: ancre };
  }
  var app;
  function rendre() {
    var r = lireRoute(), v;
    if (r.page === "recherche") { history.replaceState(null, "", "#accueil"); r = lireRoute(); setTimeout(function () { ouvrir("srch"); $("#sq").focus(); }, 0); }
    if (QS[r.page]) v = QS[r.page].statut === "red" && CH[r.page] ? vueChapitre(QS[r.page], r.sous) : vueBientot(QS[r.page]);
    else if (r.page === "epreuve") v = vueEpreuve();
    else if (r.page === "outils") v = vueOutils();
    else if (r.page === "ressources") v = vueRessources();
    else if (r.page === "auteurs") v = vueAuteurs();
    else if (r.page === "entrainement") v = vueEntrainement(r.sous);
    else { v = vueAccueil(); r.page = "accueil"; }
    app.innerHTML = '<div class="vue">' + v.html + '<footer class="pied">Faits &amp; Courbes · site de révision indépendant, contenu original rédigé d\'après le programme officiel. Les chiffres sont datés et sourcés ; vérifie toujours avec ton cours. Les sujets marqués « inventé pour le site » ne sont pas des annales.</footer></div>';
    monter(app);
    if (v.apres) v.apres(app);
    document.title = (v.titre === "Accueil" ? "" : v.titre + " · ") + "Faits & Courbes · SES Terminale";
    $$("#lat .nav a").forEach(function (a) { a.classList.toggle("act", a.getAttribute("data-r") === r.page); if (a.getAttribute("data-r") === r.page) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current"); });
    if (r.ancre) {
      var cible = document.getElementById(r.ancre);
      if (cible) {
        cible.scrollIntoView({ block: "start" });
        cible.classList.add("flash"); setTimeout(function () { cible.classList.remove("flash"); }, 2200);
        return;
      }
    }
    window.scrollTo(0, 0);
  }

  /* ---------- recherche ---------- */
  var INDEX = null;
  function construireIndex() {
    INDEX = [];
    function aj(t, ou, route, texte) { INDEX.push({ t: t, ou: ou, r: route, x: texte, nt: sansAccent(t), nx: sansAccent(texte) }); }
    Object.keys(CH).forEach(function (id) {
      var ch = CH[id], q = QS[id];
      ch.sections.forEach(function (s) {
        var tx = texteDe(s.h.replace(/<div data-chain="([^"]+)"><\/div>/g, function (m, c) { return CHAINES[c] ? " " + CHAINES[c].t + " : " + texteChaine(CHAINES[c]) + " " : ""; }));
        aj(s.t, q.court, "#" + id + ":" + s.id, tx);
      });
      ch.cartes.forEach(function (c) { aj(texteDe(c.r), q.court + " · carte", "#" + id + "/cartes", texteDe(c.v)); });
      ch.bac.forEach(function (b, i) { aj(b.t, q.court + " · sujet", "#" + id + "/bac", texteDe(b.enonce)); });
      aj("À retenir : " + q.court, q.court + " · fiche", "#" + id + "/fiche", texteDe(ch.retenir));
    });
    PROG.forEach(function (c) { c.qs.forEach(function (q) { if (q.statut !== "red") aj(q.titre, "Bientôt · " + c.nom, "#" + q.id, q.objectifs.join(" ") + " " + q.notions.join(" ")); }); });
    AUTEURS.forEach(function (a) { aj(a.n, "Auteur · " + QS[a.ch].court, "#auteurs", texteDe(a.l)); });
    var tmp = document.createElement("div");
    [["#epreuve", "L'épreuve", EPREUVE], ["#outils", "Savoir-faire", OUTILS]].forEach(function (p) {
      tmp.innerHTML = p[2];
      $$("h2", tmp).forEach(function (h2) {
        var t = h2.textContent, x = "", n = h2.nextElementSibling;
        while (n && n.tagName !== "H2") { x += " " + n.textContent; n = n.nextElementSibling; }
        aj(t.replace(/^\S{1,3}(?=[A-ZÀ-Ý])/, ""), p[1], p[0], x.replace(/\s+/g, " "));
      });
    });
  }
  function chercher(qr) {
    var zone = $("#sres");
    var mots = sansAccent(qr).split(/\s+/).filter(function (m) { return m.length > 1; });
    if (!mots.length) { zone.innerHTML = '<p class="vide">Tape un mot : « destruction créatrice », « Bourdieu », « HOS », « coefficient multiplicateur »…</p>'; return; }
    if (!INDEX) construireIndex();
    var res = [];
    INDEX.forEach(function (e) {
      var sc = 0;
      for (var i = 0; i < mots.length; i++) {
        var inT = e.nt.indexOf(mots[i]) >= 0, inX = e.nx.indexOf(mots[i]) >= 0;
        if (!inT && !inX) return;
        sc += (inT ? 10 : 0) + (inX ? 1 : 0);
      }
      res.push({ e: e, sc: sc });
    });
    res.sort(function (a, b) { return b.sc - a.sc; });
    if (!res.length) { zone.innerHTML = '<p class="vide">Rien trouvé pour « ' + esc(qr) + " ». Essaie un autre mot, sans faute de frappe.</p>"; return; }
    zone.innerHTML = res.slice(0, 30).map(function (r) {
      var e = r.e, p = e.nx.indexOf(mots[0]), ext = "";
      if (p >= 0) { var d = Math.max(0, p - 60); ext = (d ? "…" : "") + esc(e.x.substr(d, 170)) + "…"; }
      else ext = esc(e.x.substr(0, 150)) + (e.x.length > 150 ? "…" : "");
      mots.forEach(function (m) {
        if (m.length < 3) return;
        var VAR = { a: "[aàâä]", e: "[eéèêë]", i: "[iîï]", o: "[oôö]", u: "[uùûü]", c: "[cç]" };
        ext = ext.replace(new RegExp("(" + m.split("").map(function (c) { return VAR[c] || c.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }).join("") + ")", "gi"), "<mark>$1</mark>");
      });
      return '<a href="' + e.r + '"><small>' + esc(e.ou) + "</small><b>" + esc(e.t) + "</b><span>" + ext + "</span></a>";
    }).join("");
  }

  /* ---------- démarrage ---------- */
  function demarrer() {
    app = $("#app");
    $("#lat").innerHTML = navHTML();
    $("#b-menu").innerHTML = ic("menu"); $("#b-q").innerHTML = ic("loupe"); $("#b-th").innerHTML = ic("theme"); $("#b-th2").innerHTML = ic("theme");
    $("#q-ouvrir").insertAdjacentHTML("afterbegin", ic("loupe"));
    $("#s-fermer").innerHTML = ic("croix");
    $("#b-menu").onclick = function () { ouvrir("menu"); };
    $("#voile").onclick = function () { fermer(); };
    $("#lat").addEventListener("click", function (e) {
      var a = e.target.closest("a"); if (!a || couche !== "menu") return;
      e.preventDefault(); fermer(a.getAttribute("href"));
    });
    function ouvrirRech() { ouvrir("srch"); var i = $("#sq"); i.focus(); if (i.value) i.select(); chercher(i.value); }
    $("#b-q").onclick = ouvrirRech; $("#q-ouvrir").onclick = ouvrirRech;
    $("#b-th").onclick = basculerTheme; $("#b-th2").onclick = basculerTheme;
    $("#s-fermer").onclick = function () { fermer(); };
    $("#sq").addEventListener("input", function () { chercher(this.value); });
    $("#sres").addEventListener("click", function (e) { var a = e.target.closest("a"); if (!a) return; e.preventDefault(); fermer(a.getAttribute("href")); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && couche) { fermer(); return; }
      var tag = (e.target.tagName || "").toLowerCase();
      if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && tag !== "input" && tag !== "textarea")) { e.preventDefault(); if (!couche) ouvrirRech(); }
    });
    window.addEventListener("hashchange", rendre);
    rendre();
    if ("serviceWorker" in navigator && location.protocol !== "file:") {
      window.addEventListener("load", function () { navigator.serviceWorker.register("sw.js").catch(function () { }); });
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
