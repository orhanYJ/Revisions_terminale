/* Carte mentale du thème 1.A (Génétique et évolution), d'après celle de Mme Philip.
   Module partagé : le site (svt/index.html, page du thème et haut de chaque page du 1.A) et les vidéos des
   chapitres (svt/serie/, type « mental », piloté par le temps de la vidéo).
   Couleurs et polices par variables CSS : --cm-paper, --cm-panel, --cm-ink, --cm-ink-2, --cm-leaf, --cm-water,
   --cm-clay, --cm-plum (et --cm-<couleur>-soft), --cm-etoile, --cm-coeur, --cm-coeur-txt, --cm-serif, --cm-sans.
   API : CARTE_MENTALE.creer(svg, opt) → {cadre(id, ratio), voir(box), focus(id, k), pousse(p), ...}
         CARTE_MENTALE.monter(div, opt) → carte interactive du site (puces de zoom, fil d'Ariane, liens). */
(function () {
  "use strict";

  /* ---------- Données ----------
     Carte de Mme Philip (deux pages), recopiée avec ses mots ; s:"cours" = complété d'après le cours du site ;
     et:true = « schéma à savoir refaire » (étoile de la prof) ; page = page du site qui traite la branche. */
  var CARTE = {
    id: "t1a", sur: "Thème 1 · Partie A", titre: ["Génétique", "et évolution"],
    kids: [
      { id: "c1", n: "Chapitre 1", t: "Origine du génome et évolution", note: "transferts verticaux", c: "leaf", cote: -1, page: "t1u1", kids: [
        { id: "c1a", t: "Stabilité & évolution clonale", page: "t1u1", kids: [
          { t: "Mitoses / clonage", e: "cellules de la peau, lymphocytes T, Pando…" },
          { t: "Évolutions clonales", e: "tumeur, mutations de p53 / TERT" }] },
        { id: "c1b", t: "Conséquences de la reproduction sexuée et diversité", page: "t1u2", kids: [
          { t: "Fécondation, méiose", et: true, e: "diploïde 2n, haploïde n · Mendel" },
          { t: "Brassage intra / interchromosomique", et: true, e: "crossing-over · 2²³ combinaisons · test-cross" }] },
        { id: "c1c", t: "Accidents méiotiques et évolution", page: "t1u2b", kids: [
          { t: "Anomalies chromosomiques", et: true, e: "erreur de répartition : trisomie, monosomie" },
          { t: "Échange de portions", et: true, e: "translocations, crossing-over inégaux" },
          { t: "Évolution des espèces", e: "famille multigénique ★ (opsines), remaniements, spéciation, barrières entre espèces" }] },
        { id: "c1d", t: "Cadre théorique, limites éthiques", page: "t1u3", kids: [
          { t: "Enjeux socio-éthiques du clonage, analyse génétique", e: "mucoviscidose · DPI / DPN · fichier ADN · brevets" }] }
      ] },
      { id: "c2", n: "Chapitre 2", t: "Complexification du génome", c: "water", cote: -1, page: "t2", kids: [
        { id: "c2a", t: "Transferts horizontaux de gènes", et: true, page: "t2", kids: [
          { t: "Transformation, conjugaison, transgenèse", e: "Griffith · résistance aux antibiotiques · Agrobacterium" },
          { t: "Transferts viraux", e: "rétrovirus → syncytine" },
          { t: "Transduction", e: "par un bactériophage" }] },
        { id: "c2b", t: "Endosymbioses", page: "t2b", kids: [
          { t: "Autotrophes / hétérotrophes", e: "photosynthèse, respiration" },
          { t: "Chloroplastes / mitochondries", et: true, e: "Lynn Margulis · double membrane" }] }
      ] },
      { id: "c3", n: "Chapitre 3", t: "Évolution du génome au sein des populations", c: "clay", cote: 1, page: "t3", kids: [
        { id: "c3a", t: "Équilibre de Hardy-Weinberg", page: "t3", kids: [
          { t: "Fréquences alléliques", s: "cours", e: "p + q = 1 · p² + 2pq + q² = 1 · conditions du modèle" }] },
        { id: "c3b", t: "Écarts à l'équilibre", page: "t3b", kids: [
          { t: "Dérive génétique", e: "drosophiles de Buri" },
          { t: "Effet fondateur", e: "Amish et Huttérites · groupe O des Amérindiens" },
          { t: "Sélection naturelle", e: "moustiques Culex pipiens" }] },
        { id: "c3c", t: "La notion d'espèce", s: "cours", page: "t3b", kids: [
          { t: "Critères et réseau du vivant", s: "cours", e: "arbre des molécules · Denisova · espèce en devenir" }] }
      ] },
      { id: "c4", n: "Chapitre 4", t: "Autres mécanismes évolutifs", c: "plum", cote: 1, page: "t4", kids: [
        { id: "c4a", t: "Associations entre êtres vivants", s: "cours", page: "t4", kids: [
          { t: "Mutualisme", s: "cours", e: "ver de Roscoff · microbiote intestinal" },
          { t: "Parasitisme", s: "cours", e: "gammare parasité" }] },
        { id: "c4b", t: "Phénotype étendu", s: "cours", page: "t4", kids: [
          { t: "Ce que l'animal construit hors de son corps", s: "cours", e: "phrygane · jardinier satiné · araignée" }] },
        { id: "c4c", t: "Comportements", s: "cours", page: "t4", kids: [
          { t: "Selon les ressources du milieu", s: "cours", e: "nids d'oiseaux · termitières" },
          { t: "Transmis par apprentissage", s: "cours", e: "chimpanzés et noix · chant des oiseaux · baleines à bosse" }] }
      ] }
    ]
  };
  // page du site → branche de la carte (pour le haut de chaque page)
  var PAGES = { t1u1: "c1a", t1u2: "c1b", t1u2b: "c1c", t1u3: "c1d", t2: "c2a", t2b: "c2b", t3: "c3a", t3b: "c3b", t4: "c4" };

  var NS = "http://www.w3.org/2000/svg";
  var STYLE = ".cm-g{transition:opacity .55s ease}" +
    ".cm-n{font-family:var(--cm-serif,Georgia,serif);fill:var(--cm-ink)}" +
    ".cm-k{font-family:var(--cm-sans,sans-serif);font-weight:700;letter-spacing:.09em;font-size:11px}" +
    ".cm-ft{font-family:var(--cm-serif,Georgia,serif);font-weight:600;font-size:15.5px;fill:var(--cm-ink)}" +
    ".cm-fe{font-family:var(--cm-sans,sans-serif);font-style:italic;font-size:12.5px;fill:var(--cm-ink-2)}" +
    ".cm-et{fill:var(--cm-etoile);font-family:var(--cm-sans,sans-serif);font-weight:700}" +
    ".cm-hit{cursor:pointer}" +
    "@media (prefers-reduced-motion: reduce){.cm-g{transition:none}}";
  function style() {
    if (document.getElementById("cm-style")) return;
    var s = document.createElement("style"); s.id = "cm-style"; s.textContent = STYLE; document.head.appendChild(s);
  }

  function creer(svg, opt) {
    opt = opt || {};
    style();
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var CS = getComputedStyle(svg);
    var SERIF = CS.getPropertyValue("--cm-serif") || "Georgia,serif", SANS = CS.getPropertyValue("--cm-sans") || "sans-serif";
    var cv = document.createElement("canvas").getContext("2d");
    function larg(t, font) { cv.font = font; return cv.measureText(t).width; }
    function couper(t, font, max) {
      var mots = t.split(" "), lignes = [], l = "";
      mots.forEach(function (m) { var e = l ? l + " " + m : m; if (l && larg(e, font) > max) { lignes.push(l); l = m; } else l = e; });
      if (l) lignes.push(l); return lignes;
    }

    /* ----- géométrie : chapitres 1 et 2 à gauche, 3 et 4 à droite ----- */
    var CX = 800, H = 900;
    var F_CH = "700 16px " + SERIF, F_BR = "600 14px " + SERIF, F_T = "600 15.5px " + SERIF, F_E = "italic 12.5px " + SANS;
    var X = { chap: 228, br: 430, leaf: 532 }, WCH = 188, WBR = 172, WLEAF = 252;
    var noeuds = {}, ordre = [];
    (function prep(n, parent, niveau, cote, c, k) {
      n.id = n.id || parent.id + "-" + k; n.parent = parent ? parent.id : null; n.niveau = niveau;
      n.cote = n.cote || cote; n.c = n.c || c; noeuds[n.id] = n; ordre.push(n.id);
      (n.kids || []).forEach(function (e, i) { prep(e, n, niveau + 1, n.cote, n.c, i); });
    })(CARTE, null, 0, 0, "leaf", 0);
    ordre.forEach(function (id) {
      var n = noeuds[id], s = n.cote;
      if (n.niveau === 1) { n.lt = couper(n.t, F_CH, WCH - 28); n.w = WCH; n.h = 34 + n.lt.length * 19 + 6 + (n.note ? 18 : 0); n.cx = CX + s * X.chap; }
      if (n.niveau === 2) { n.lt = couper(n.t, F_BR, WBR - 30); n.w = WBR; n.h = 22 + n.lt.length * 17; n.cx = CX + s * X.br; }
      if (n.niveau === 3) {
        n.lt = couper(n.t, F_T, WLEAF - 22);
        n.le = n.e ? couper(n.e, F_E, WLEAF - 22) : [];
        n.h = n.lt.length * 18 + (n.le.length ? 3 + n.le.length * 15.5 : 0);
        n.x = CX + s * X.leaf;
      }
    });
    function empiler(cote) {
      var slots = [];
      CARTE.kids.filter(function (c) { return c.cote === cote; }).forEach(function (ch) {
        ch.kids.forEach(function (br, bi) {
          br.kids.forEach(function (f, fi) { slots.push({ n: f, saut: !slots.length ? 0 : (fi > 0 ? 1 : (bi > 0 ? 1.9 : 3.2)) }); });
        });
      });
      var hs = slots.reduce(function (a, s) { return a + s.n.h; }, 0), u = slots.reduce(function (a, s) { return a + s.saut; }, 0);
      var g = Math.max(9, (H - 60 - hs) / u), y = 30;
      slots.forEach(function (s) { y += s.saut * g; s.n.y = y; s.n.cy = y + s.n.h / 2; s.n.ay = y + 9; y += s.n.h; });   // ay : la pastille, où arrive la tige
      return y + 30;
    }
    var hG = empiler(-1), hD = empiler(1), HT = Math.max(H, hG, hD);
    [[-1, hG], [1, hD]].forEach(function (c) {
      var d = (HT - c[1]) / 2; if (d <= 0) return;
      ordre.forEach(function (id) { var n = noeuds[id]; if (n.niveau === 3 && n.cote === c[0]) { n.y += d; n.cy += d; n.ay += d; } });
    });
    function ancre(k) { return k.niveau === 3 ? k.ay : k.cy; }
    function moy(n) { var a = n.kids[0], b = n.kids[n.kids.length - 1]; return (ancre(a) + ancre(b)) / 2; }
    ordre.forEach(function (id) { var n = noeuds[id]; if (n.niveau === 2) n.cy = moy(n); });
    ordre.forEach(function (id) { var n = noeuds[id]; if (n.niveau === 1) n.cy = moy(n); });
    var CY = HT / 2; CARTE.cy = CY; CARTE.w = 216; CARTE.h = 150; CARTE.cx = CX;
    ordre.forEach(function (id) {
      var n = noeuds[id];
      if (n.niveau < 3) n.box = [n.cx - n.w / 2, n.cy - n.h / 2, n.w, n.h];
      else {
        var lw = Math.max.apply(null, n.lt.map(function (t) { return larg(t, F_T) + 8; }).concat(n.le.map(function (t) { return larg(t, F_E); })));
        var bw = 18 + lw; n.box = n.cote > 0 ? [n.x, n.y, bw, n.h] : [n.x - bw, n.y, bw, n.h];
      }
    });

    /* ----- dessin ----- */
    function el(nom, at, parent) { var e = document.createElementNS(NS, nom); for (var k in at) e.setAttribute(k, at[k]); if (parent) parent.appendChild(e); return e; }
    function txt(parent, x, y, t, cls, at) { var e = el("text", Object.assign({ x: x, y: y, "class": cls }, at || {}), parent); e.textContent = t; return e; }
    function etoile(te) { var s = el("tspan", { "class": "cm-et", dx: 4, "font-size": "0.9em" }, te); s.textContent = "★"; }
    function col(c) { return "var(--cm-" + c + ")"; }
    function tige(x0, y0, x1, y1, w0, w1) {
      var mx = (x0 + x1) / 2;
      return "M" + x0 + "," + (y0 - w0 / 2) + " C" + mx + "," + (y0 - w0 / 2) + " " + mx + "," + (y1 - w1 / 2) + " " + x1 + "," + (y1 - w1 / 2) +
        " L" + x1 + "," + (y1 + w1 / 2) + " C" + mx + "," + (y1 + w1 / 2) + " " + mx + "," + (y0 + w0 / 2) + " " + x0 + "," + (y0 + w0 / 2) + " Z";
    }
    var Lbr = el("g", {}, svg), Lnd = el("g", {}, svg), groupes = {};
    function reg(id, e) { (groupes[id] = groupes[id] || []).push(e); e.classList.add("cm-g"); if (opt.fige) e.style.transition = "none"; return e; }
    function bouton(id, label) { var a = { "class": "cm-hit", "data-id": id }; if (opt.interactif) { a.tabindex = 0; a.role = "button"; a["aria-label"] = label; } return a; }

    ordre.forEach(function (id) {
      var n = noeuds[id]; if (!n.parent) return;
      var p = noeuds[n.parent], s = n.cote, x0, y0 = p.cy, x1, y1 = ancre(n), w0, w1;
      if (n.niveau === 1) {   // depuis le bord de la bulle centrale, à une hauteur qui reste dans la bulle
        var lim = CARTE.h / 2 - 30;
        x0 = CX + s * (CARTE.w / 2 - 3); y0 = CY + Math.max(-lim, Math.min(lim, (n.cy - CY) * 0.5)); w0 = 12; w1 = 6.5;
      }
      else { x0 = s > 0 ? p.box[0] + p.box[2] : p.box[0]; w0 = n.niveau === 2 ? 5 : 3.2; w1 = n.niveau === 2 ? 3.2 : 1.4; }
      x1 = s > 0 ? n.box[0] + (n.niveau === 3 ? 5 : 0) : n.box[0] + n.box[2] - (n.niveau === 3 ? 5 : 0);   // feuilles : jusqu'au centre de la pastille
      reg(id, el("path", { d: tige(x0, y0, x1, y1, w0, w1), fill: col(n.c), opacity: n.niveau === 3 ? .5 : .8 }, Lbr)).dataset.niv = n.niveau;
    });
    (function () {
      var b = [CX - CARTE.w / 2, CY - CARTE.h / 2, CARTE.w, CARTE.h];
      var g = reg("t1a", el("g", bouton("t1a", "Vue d'ensemble"), Lnd)); g.dataset.niv = 0;
      el("rect", { x: b[0], y: b[1], width: b[2], height: b[3], rx: 32, fill: "var(--cm-coeur)" }, g);
      el("rect", { x: b[0] + 7, y: b[1] + 7, width: b[2] - 14, height: b[3] - 14, rx: 26, fill: "none", stroke: "var(--cm-coeur-txt)", "stroke-opacity": .22 }, g);
      txt(g, CX, b[1] + 36, CARTE.sur.toUpperCase(), "cm-k", { "text-anchor": "middle", fill: "var(--cm-coeur-txt)", "fill-opacity": .75 });
      txt(g, CX, b[1] + 78, CARTE.titre[0], "cm-n", { "text-anchor": "middle", "font-size": 32, "font-weight": 600, style: "fill:var(--cm-coeur-txt)" });
      txt(g, CX, b[1] + 112, CARTE.titre[1], "cm-n", { "text-anchor": "middle", "font-size": 32, "font-weight": 600, style: "fill:var(--cm-coeur-txt)" });
    })();
    ordre.forEach(function (id) {
      var n = noeuds[id]; if (n.niveau !== 1 && n.niveau !== 2) return;
      var b = n.box, ch = n.niveau === 1, ajout = n.s === "cours";
      var g = reg(id, el("g", bouton(id, (n.n ? n.n + " : " : "") + n.t), Lnd)); g.dataset.niv = n.niveau;
      el("rect", { x: b[0], y: b[1], width: b[2], height: b[3], rx: ch ? 20 : 14, fill: ch ? col(n.c + "-soft") : "var(--cm-panel)",
        stroke: col(n.c), "stroke-width": ch ? 2 : 1.5, "stroke-dasharray": ajout ? "5 4" : "" }, g);
      var y;
      if (ch) { txt(g, n.cx, b[1] + 21, n.n.toUpperCase(), "cm-k", { "text-anchor": "middle", fill: col(n.c) }); y = b[1] + 42; }
      else y = b[1] + 24;
      n.lt.forEach(function (t, i) {
        var e = txt(g, n.cx, y + i * (ch ? 19 : 17), t, "cm-n", { "text-anchor": "middle", "font-size": ch ? 16 : 14, "font-weight": ch ? 700 : 600 });
        if (n.et && i === n.lt.length - 1) etoile(e);
      });
      if (n.note) txt(g, n.cx, y + n.lt.length * 19 + 4, n.note, "cm-fe", { "text-anchor": "middle", fill: col(n.c), style: "fill:" + col(n.c) });
    });
    ordre.forEach(function (id) {
      var n = noeuds[id]; if (n.niveau !== 3) return;
      var g = reg(id, el("g", bouton(id, n.t), Lnd)); g.dataset.niv = 3;
      var b = n.box, d = n.cote > 0, ajout = n.s === "cours";
      el("rect", { x: b[0] - 4, y: b[1] - 4, width: b[2] + 8, height: b[3] + 8, fill: "transparent" }, g);
      var px = d ? b[0] + 5 : b[0] + b[2] - 5;
      el("circle", { cx: px, cy: n.ay, r: 4.6, fill: ajout ? "var(--cm-panel)" : col(n.c), stroke: col(n.c), "stroke-width": 1.6 }, g);
      var tx = d ? b[0] + 18 : b[0] + b[2] - 18, anc = d ? "start" : "end", y = n.y + 14;
      n.lt.forEach(function (t, i) { var e = txt(g, tx, y, t, "cm-ft", { "text-anchor": anc }); if (n.et && i === n.lt.length - 1) etoile(e); y += 18; });
      y += 2;
      n.le.forEach(function (t) {
        var e = txt(g, tx, y, "", "cm-fe", { "text-anchor": anc });
        t.split("★").forEach(function (m, i) {
          if (i) { var s = el("tspan", { "class": "cm-et" }, e); s.textContent = "★"; }
          var p = el("tspan", {}, e); p.textContent = m;
        });
        y += 15.5;
      });
    });

    /* ----- caméra et mise en valeur ----- */
    function sousArbre(id) { var r = [id]; (noeuds[id].kids || []).forEach(function (k) { r = r.concat(sousArbre(k.id)); }); return r; }
    function ancetres(id) { var r = [], p = noeuds[id].parent; while (p) { r.push(p); p = noeuds[p].parent; } return r; }
    function cadre(id, ratio) {
      ratio = ratio || opt.ratio || 16 / 9;
      var ids = id === "t1a" ? ordre.slice(1) : sousArbre(id), n = noeuds[id];
      if (n.niveau === 3) ids.push(n.parent);
      var x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      ids.forEach(function (i) { var b = noeuds[i].box; x0 = Math.min(x0, b[0]); y0 = Math.min(y0, b[1]); x1 = Math.max(x1, b[0] + b[2]); y1 = Math.max(y1, b[1] + b[3]); });
      var pad = id === "t1a" ? 14 : 34; x0 -= pad; y0 -= pad; x1 += pad; y1 += pad;
      var w = x1 - x0, h = y1 - y0;
      if (w / h < ratio) { var nw = h * ratio; x0 -= (nw - w) / 2; w = nw; } else { var nh = w / ratio; y0 -= (nh - h) / 2; h = nh; }
      return [x0, y0, w, h];
    }
    function voir(v) { svg.setAttribute("viewBox", v.map(function (x) { return x.toFixed(1); }).join(" ")); }
    // trajet de caméra entre deux cadres (u de 0 à 1), avec un léger recul entre deux zooms rapprochés
    function trajet(a, b, u) {
      var e = u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2, tout = cadre("t1a");
      var r = 1 + (a[2] < tout[2] * .95 && b[2] < tout[2] * .95 ? .15 : 0) * Math.sin(Math.PI * u);
      var v = a.map(function (x, i) { return x + (b[i] - x) * e; });
      var cx = v[0] + v[2] / 2, cy = v[1] + v[3] / 2; v[2] *= r; v[3] *= r; v[0] = cx - v[2] / 2; v[1] = cy - v[3] / 2;
      return v;
    }
    // id mis en valeur (null : tout) ; k de 0 à 1 = force de l'atténuation du reste
    function focus(id, k) {
      if (k == null) k = 1;
      var garde = !id || id === "t1a" ? null : sousArbre(id).concat(ancetres(id));
      Object.keys(groupes).forEach(function (g) {
        var on = !garde || garde.indexOf(g) >= 0;
        groupes[g].forEach(function (e) { e.style.opacity = on ? "" : String(1 - .87 * k); });
      });
    }
    // la carte pousse : centre, chapitres, branches, puis feuilles (p de 0 à 1)
    function pousse(p) {
      Object.keys(groupes).forEach(function (g) {
        groupes[g].forEach(function (e) {
          var niv = +e.dataset.niv || 0, a = Math.max(0, Math.min(1, (p * 4.2 - niv) / 1.2));
          e.style.opacity = a >= 1 ? "" : String(a);
        });
      });
    }
    voir(cadre("t1a"));
    return { svg: svg, noeuds: noeuds, ordre: ordre, cadre: cadre, voir: voir, trajet: trajet, focus: focus, pousse: pousse,
      ancetres: ancetres, sousArbre: sousArbre };
  }

  /* ---------- carte interactive du site ---------- */
  function monter(div, opt) {
    opt = opt || {};
    if (div._cm) return div._cm;
    var MO = !(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);
    div.classList.add("cm");
    div.innerHTML = '<div class="cm-chips" role="toolbar" aria-label="Zoom sur la carte"></div>' +
      '<div class="cm-scene"><svg role="img" aria-label="Carte mentale du thème 1.A"></svg></div>' +
      '<div class="cm-pied"><div class="cm-fil" aria-live="polite"></div><div class="cm-act"></div></div>' +
      '<div class="cm-leg"><span><i class="cm-pt"></i>carte de Mme Philip</span><span><i class="cm-pt vide"></i>complété d\'après le cours</span>' +
      '<span><b>★</b> schéma à savoir refaire</span></div>';
    var svg = div.querySelector("svg"), api = creer(svg, { interactif: true, ratio: opt.ratio });
    var chips = div.querySelector(".cm-chips"), fil = div.querySelector(".cm-fil"), act = div.querySelector(".cm-act");
    var VB = api.cadre("t1a"), focusId = "t1a", anim = null;
    [["t1a", "Vue d'ensemble"], ["c1", "Chapitre 1"], ["c2", "Chapitre 2"], ["c3", "Chapitre 3"], ["c4", "Chapitre 4"]].forEach(function (l) {
      var b = document.createElement("button"); b.type = "button"; b.dataset.id = l[0]; b.textContent = l[1];
      b.addEventListener("click", function () { zoom(l[0]); }); chips.appendChild(b);
    });
    function libelle(id) { var n = api.noeuds[id]; return id === "t1a" ? "Thème 1.A" : (n.n ? n.n + " · " : "") + n.t; }
    function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }
    function pageDe(id) { var n = api.noeuds[id]; while (n && !n.page) n = api.noeuds[n.parent]; return n ? n.page : null; }
    function chapDe(id) { var n = api.noeuds[id]; while (n && n.niveau > 1) n = api.noeuds[n.parent]; return n && n.niveau === 1 ? n.id : null; }
    function zoom(id, sans) {
      focusId = id;
      var cible = api.cadre(id), dep = VB.slice(), t0 = performance.now(), D = MO && !sans ? 1000 : 0;
      api.focus(id === "t1a" ? null : id);
      if (anim) cancelAnimationFrame(anim);
      (function pas(now) {
        var u = D ? Math.min(1, (now - t0) / D) : 1;
        VB = api.trajet(dep, cible, u); api.voir(VB);
        anim = u < 1 ? requestAnimationFrame(pas) : null;
      })(performance.now());
      chips.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.id === id ? "true" : "false"); });
      var ch = api.ancetres(id).reverse().concat([id]);
      fil.innerHTML = ch.map(function (i, k) { return k === ch.length - 1 ? "<b>" + esc(libelle(i)) + "</b>" : esc(libelle(i)); }).join(" › ");
      act.innerHTML = "";
      var pg = id === "t1a" ? null : pageDe(id), cc = chapDe(id);
      if (pg && pg !== opt.page && opt.go) {
        var b = document.createElement("button"); b.type = "button"; b.className = "cm-btn"; b.textContent = "Ouvrir le cours →";
        b.addEventListener("click", function () { opt.go(pg); }); act.appendChild(b);
      }
      var vid = cc && opt.video ? opt.video(cc) : null;
      if (vid) {
        var v = document.createElement("button"); v.type = "button"; v.className = "cm-btn cm-vid"; v.textContent = "▶ Vidéo du chapitre";
        v.addEventListener("click", function () { opt.go(vid); }); act.appendChild(v);
      }
    }
    svg.addEventListener("click", function (ev) {
      var h = ev.target.closest(".cm-hit");
      if (!h) { zoom(focusId === "t1a" ? "t1a" : (api.noeuds[focusId].parent || "t1a")); return; }
      var id = h.getAttribute("data-id");
      zoom(id === focusId && api.noeuds[id].parent ? api.noeuds[id].parent : id);
    });
    svg.addEventListener("keydown", function (ev) {
      if (ev.key !== "Enter" && ev.key !== " ") return;
      var h = ev.target.closest(".cm-hit"); if (!h) return; ev.preventDefault(); zoom(h.getAttribute("data-id"));
    });
    zoom(opt.focus || "t1a", true);
    div._cm = { zoom: zoom, api: api };
    return div._cm;
  }

  window.CARTE_MENTALE = { CARTE: CARTE, PAGES: PAGES, creer: creer, monter: monter };
})();
