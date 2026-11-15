/* Cartes propres à la vidéo hggsp-t1-otc (thème 1, objet de travail conclusif : « La Chine : à la conquête de l'espace,
   des mers et des océans »). Chargé par outils/serie-hggsp/scenes.js (tout fichier cartes-<code>.js du dossier) :
   exporte une fonction (outils) qui renvoie { cartes: { nom(D, d3, FEAT) → scène }, videos: { code: { site, video } } }.
   Coordonnées : [longitude, latitude]. Tous les faits viennent du chapitre « t1-otc » du site (data-t1.js) et de sa carte
   « chine » (outils/specialites/hggsp/cartes.js) ; positions et tracés approximatifs.

   Cartes : chine (de la Chine au Pirée : bases, ports des routes de la soie, Malacca, tubes de contournement, bases de
   lancement), voisins (mer de Chine : Senkaku, Taïwan, Scarborough, Whitsun, Second Thomas, patrouilles américaines),
   alliances (planisphère : Quad et AUKUS), polaire (la « route de la soie polaire » vue du pôle Nord), lune (la face
   cachée de la Lune : Chang'e 4 et Chang'e 6, schéma sans échelle). */
module.exports = function (O) {
  const { cadre, simplifier, esc } = O;

  /* flèche au crayon (courbe lissée par plusieurs points), pointe à la fin ; bleu si o.b, pointillé si o.p */
  function outilsTrait(C, id, d3) {
    const defs = "<defs><marker id='fl-" + id + "' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker>" +
      "<marker id='fl-" + id + "b' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--acier)'/></marker></defs>";
    const trajet = (k, lls, o = {}) => {
      const p = lls.map(ll => C.P(ll));
      let d = "M" + p[0].join(",");
      for (let i = 1; i < p.length; i++) {
        const [x0, y0] = p[i - 1], [x1, y1] = p[i], c = o.c === undefined ? 0.1 : o.c;
        const cx = Math.round((x0 + x1) / 2 - (y1 - y0) * c), cy = Math.round((y0 + y1) / 2 + (x1 - x0) * c);
        d += "Q" + cx + "," + cy + " " + x1 + "," + y1;
      }
      return "<path data-k='" + k + "' class='trace' pathLength='1' d='" + d + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") +
        "' stroke-width='3' stroke-linecap='round'" + (o.fin === false ? "" : " marker-end='url(#fl-" + id + (o.b ? "b" : "") + ")'") + "/>";
    };
    const croix = (k, ll, nom, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -10 : a === "middle" ? 0 : 10;
      return "<g data-k='" + k + "'><path d='M" + (x - 6) + "," + (y - 6) + "L" + (x + 6) + "," + (y + 6) + "M" + (x + 6) + "," + (y - 6) + "L" + (x - 6) + "," + (y + 6) +
        "' stroke='var(--rouge)' stroke-width='3' fill='none'/>" +
        "<text x='" + (x + dx) + "' y='" + (y + 5 + (o.dy || 0)) + "' text-anchor='" + a + "' class='lbl'>" + esc(nom) + "</text></g>";
    };
    /* un anneau mal orienté désignerait tout le globe sauf la zone : on le retourne */
    const zone = (k, ring) => { if (d3.geoArea({ type: "Polygon", coordinates: [ring] }) > 2 * Math.PI) ring = ring.slice().reverse(); return "<g data-k='" + k + "'>" + C.poly(ring, "class='zone'") + "</g>"; };
    const ligne = (k, lls, attrs) => "<path" + (k ? " data-k='" + k + "'" : "") + " d='" + simplifier(C.gp({ type: "LineString", coordinates: lls }), 0.3, 0) + "' " + attrs + "/>";
    return { defs, trajet, croix, zone, ligne };
  }
  /* projection de Mercator ajustée à un rectangle de longitudes et latitudes, largeur W */
  function mercator(d3, sw, ne, W) {
    const p0 = d3.geoMercator().scale(1).translate([0, 0]);
    const a = p0([sw[0], ne[1]]), b = p0([ne[0], sw[1]]);
    const H = Math.round(W * (b[1] - a[1]) / (b[0] - a[0]));
    const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [sw, ne] });
    return { proj, H };
  }
  const NEUF = [[108.3, 18.0], [109.2, 15.5], [109.6, 12.5], [109.8, 10.0], [109.0, 7.5], [110.6, 5.5], [112.3, 3.9], [113.9, 5.7], [115.2, 7.0], [116.3, 8.4], [117.1, 10.2], [118.4, 12.4], [119.1, 15.0], [119.7, 17.8], [120.8, 20.0], [121.8, 21.8]];

  /* 1. « La Chine à la conquête des mers » : de Qingdao au Pirée */
  function chine(D, d3, FEAT) {
    const W = 1000, { proj, H } = mercator(d3, [18, -12], [150, 47], W);
    const C = cadre(d3, FEAT, proj, W, H, 0.45, 2), T = outilsTrait(C, "chine", d3);
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/><path d='" + simplifier(C.gp(d3.geoGraticule().step([10, 10])()), 0.5, 0) + "' class='k-grat'/>" +
      "<path d='" + C.pays(f => f.properties.ADMIN !== "China") + "' class='k-terre'/><path d='" + C.pays(f => f.properties.ADMIN === "China") + "' class='k-terre-cn'/>";
    const ROUTE = [[121.5, 31.2], [123, 28], [120.5, 23.5], [117, 20], [112, 13], [106, 6], [103.6, 1.3], [98.5, 5], [92, 7], [82, 5.2], [72, 10],
      [60, 13.5], [51, 13], [43.6, 12.4], [38, 20], [33.8, 27.3], [32.5, 30.5], [32.3, 31.6], [28, 34.4], [23.9, 37.6]];
    const s = [
      T.defs,
      C.etiq("", [103, 34], "CHINE", { cl: "k-pays" }), C.etiq("", [78, 22], "INDE", { cl: "k-pays" }), C.etiq("", [138, 37.5], "JAPON", { cl: "k-pays" }),
      C.etiq("", [69, 30], "PAKISTAN", { cl: "k-pays" }), C.etiq("", [118, -3], "INDONÉSIE", { cl: "k-pays" }),
      C.etiq("", [75, -6], "OCÉAN INDIEN", { cl: "k-mer" }), C.etiq("", [138, 18], "OCÉAN PACIFIQUE", { cl: "k-mer" }), C.etiq("", [28, 30.5], "Méditerranée", { cl: "k-mer", a: "end" }),
      /* étape « marine » : les grandes bases */
      C.point("qingdao", [120.4, 36.1], "Qingdao : le Liaoning (2012)", { a: "start", cl: "pt-b" }),
      C.point("sanya", [109.5, 18.25], "Sanya : Shandong (2019), Fujian (2025)", { a: "end", cl: "pt-b", dy: 14 }),
      C.point("djib", [43.15, 11.6], "Djibouti (1er août 2017)", { a: "end", cl: "pt-b", dy: 18 }),
      /* étape « espace » : les bases de lancement */
      C.point("jiuquan", [100.3, 41.0], "Jiuquan : les vols habités", { a: "end", dy: -6 }),
      C.point("wench", [111.0, 19.6], "Wenchang", { a: "start", dy: -8 }),
      /* routes de la soie maritimes */
      T.trajet("route", ROUTE, { c: 0.05 }),
      C.point("shanghai", [121.5, 31.2], "Shanghai", { a: "start" }),
      C.point("piree", [23.65, 37.95], "Le Pirée (COSCO)", { a: "start", dy: -14 }),
      C.point("hamb", [81.1, 6.12], "Hambantota (99 ans, 2017)", { a: "start", dy: 20 }),
      /* dilemme de Malacca et contournements */
      T.croix("malacca", [100.9, 2.9], "Malacca", { a: "end", dy: 16 }),
      C.point("gwadar", [62.3, 25.1], "Gwadar", { a: "end", dy: 4 }),
      T.ligne("corridor", [[62.3, 25.1], [67.0, 27.5], [71.5, 31.5], [73.5, 35.5], [75.99, 39.47]], "class='trace' pathLength='1' fill='none' stroke='var(--acier)' stroke-dasharray='8 6'"),
      C.point("kyauk", [93.55, 19.43], "Kyaukpyu", { a: "end", dy: 8 }),
      T.trajet("tubes", [[93.55, 19.43], [96.1, 21.9], [99.5, 24.0], [102.7, 25.0]], { b: true, c: 0.05 }),
      C.etiq("tubest", [103.5, 22.4], "gazoduc (2013), oléoduc (2017)", { cl: "lbl", a: "start" })
    ].join("");
    return { titre: "La Chine à la conquête des mers", w: W, h: H, vb: [0, 0, W, H], svg: fond + s, etapes: [],
      source: "Fond Natural Earth (domaine public). Positions et tracés approximatifs." };
  }

  /* 2. « Des voisins inquiets » : la mer de Chine et ses incidents */
  function voisins(D, d3, FEAT) {
    const W = 1000, { proj, H } = mercator(d3, [102, 6.5], [144, 31.5], W);
    const C = cadre(d3, FEAT, proj, W, H, 0.3, 1), T = outilsTrait(C, "vois", d3);
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/><path d='" + simplifier(C.gp(d3.geoGraticule().step([5, 5])()), 0.5, 0) + "' class='k-grat'/>" +
      "<path d='" + C.pays(f => !["China", "Taiwan"].includes(f.properties.ADMIN)) + "' class='k-terre'/><path d='" + C.pays(f => f.properties.ADMIN === "China") + "' class='k-terre-cn'/>" +
      "<path d='" + C.pays(f => f.properties.ADMIN === "Taiwan") + "' class='k-terre'/>";
    const s = [
      T.defs,
      C.etiq("", [112, 27], "CHINE", { cl: "k-pays" }), C.etiq("", [131, 33.6], "JAPON", { cl: "k-pays" }), C.etiq("", [106.2, 15.5], "VIÊT NAM", { cl: "k-pays", a: "end" }),
      C.etiq("", [124.2, 11], "PHILIPPINES", { cl: "k-pays", a: "start" }),
      C.etiq("", [114, 14.5], "mer de Chine", { cl: "k-mer" }), C.etiq("", [114, 13.3], "méridionale", { cl: "k-mer" }),
      C.etiq("", [129.5, 21], "OCÉAN PACIFIQUE", { cl: "k-mer" }),
      T.ligne("neuf", NEUF, "class='k-neuf'"),
      C.etiq("tw", [121.0, 23.7], "TAÏWAN", { cl: "lbl", a: "end", dx: -22 }),
      T.zone("manoeuvres", [[118.6, 21.0], [123.4, 21.0], [123.4, 26.4], [118.6, 26.4], [118.6, 21.0]]),
      C.etiq("manoeuvrest", [123.8, 24.3], "grandes manœuvres chinoises", { cl: "lbl-f", a: "start" }),
      C.point("senkaku", [123.5, 25.75], "Senkaku / Diaoyu (Japon)", { a: "start", dy: -14, cl: "pt-b" }),
      C.point("scarb", [117.76, 15.15], "Scarborough", { a: "start" }),
      C.point("whitsun", [114.66, 9.98], "Whitsun : ≈ 220 navires (mars 2021)", { a: "end", dy: -12 }),
      C.point("thomas", [115.87, 9.75], "Second Thomas (17 juin 2024)", { a: "start", dy: 14 }),
      T.trajet("fonop", [[108, 7.5], [111.5, 9.2], [113.8, 12.5], [116.5, 17.5], [119.5, 19.2]], { b: true, c: -0.08 }),
      C.etiq("fonopt", [117.2, 20.2], "patrouilles américaines", { cl: "lbl", a: "end" })
    ].join("");
    return { titre: "Des voisins inquiets", w: W, h: H, vb: [0, 0, W, H], svg: fond + s, etapes: [],
      source: "Fond Natural Earth (domaine public). Ligne en neuf traits, zone de manœuvres et patrouilles : tracés approximatifs." };
  }

  /* 3. « Des alliances face à la Chine » : le Quad et l'AUKUS, sur le planisphère du site */
  function alliances(D, d3, FEAT) {
    const WM = 1000, pm = d3.geoEqualEarth().rotate([-10, 0]);
    pm.fitWidth(WM - 8, { type: "Sphere" }); pm.translate([WM / 2, pm.translate()[1]]);
    const yN = pm([10, 80])[1];
    pm.translate([pm.translate()[0], pm.translate()[1] - yN + 6]);
    const C = cadre(d3, FEAT, pm, WM, D.CARTES.monde.h, 0.55, 2.5), T = outilsTrait(C, "all", d3);
    const paysK = (k, noms, attrs) => "<path data-k='" + k + "' d='" + C.pays(f => noms.includes(f.properties.ADMIN)) + "' " + attrs + "/>";
    const BLEU = "style='fill:#2d4f86;fill-opacity:.42;stroke:#2d4f86;stroke-width:1.4'", VERT = "style='fill:#3f7a3a;fill-opacity:.5;stroke:#2f5e2b;stroke-width:1.4'";
    const s = [
      T.defs,
      paysK("cn", ["China"], "class='zone'"),
      C.etiq("cnt", [103, 36], "Chine", { cl: "lbl-f" }),
      paysK("quad", ["United States of America", "Japan", "India", "Australia"], BLEU),
      C.etiq("quadt", [-100, 39], "États-Unis", { cl: "lbl" }), C.etiq("quadj", [140, 30], "Japon", { cl: "lbl", a: "start", dx: 10 }),
      C.etiq("quadi", [78, 15], "Inde", { cl: "lbl" }), C.etiq("quada", [134, -25], "Australie", { cl: "lbl" }),
      C.etiq("quad17", [-30, -38], "le Quad, relancé en 2017", { cl: "lbl-f" }),
      paysK("aukus", ["United States of America", "United Kingdom", "Australia"], VERT),
      C.etiq("aukust", [-30, -38], "AUKUS (15 septembre 2021)", { cl: "lbl-f" }),
      C.etiq("ukt", [-3, 60], "Royaume-Uni", { cl: "lbl", a: "end", dx: -8 }),
      T.trajet("paris", [[2.3, 46.5], [60, 15], [120, -10], [134, -22]], { c: 0.06 }),
      C.etiq("parist", [62, 5], "contrat de sous-marins français annulé", { cl: "lbl", a: "middle" })
    ].join("");
    return { titre: "Des alliances face à la Chine", w: WM, h: D.CARTES.monde.h, vb: [0, 0, WM, D.CARTES.monde.h], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth (domaine public)." };
  }

  /* 4. « La route de la soie polaire », vue du pôle Nord (azimutale équivalente) */
  function polaire(D, d3, FEAT) {
    const W = 700, H = 700;
    const proj = d3.geoAzimuthalEqualArea().rotate([-60, -90, 0]).clipAngle(64).fitExtent([[10, 10], [W - 10, H - 10]], { type: "Sphere" });
    const C = cadre(d3, FEAT, proj, W, H, 0.35, 1.5), T = outilsTrait(C, "pol", d3);
    const cercle = (lat, n = 90) => { const r = []; for (let i = 0; i <= n; i++) r.push([-180 + 360 * i / n, lat]); return r; };
    const grat = [30, 45, 60, 75].map(l => "<path class='k-grat' d='" + simplifier(C.gp({ type: "LineString", coordinates: cercle(l) }), 0.3, 0) + "'/>").join("") +
      [0, 30, 60, 90, 120, 150, 180, -150, -120, -90, -60, -30].map(lo => "<path class='k-grat' d='" + simplifier(C.gp({ type: "LineString", coordinates: [[lo, 27], [lo, 89.9]] }), 0.3, 0) + "'/>").join("");
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/>" + grat +
      "<path class='k-terre' d='" + C.pays(f => f.properties.ADMIN !== "China") + "'/><path class='k-terre-cn' d='" + C.pays(f => f.properties.ADMIN === "China") + "'/>";
    const ROUTE = [[122.5, 31.0], [129.5, 34.5], [137, 40], [141.8, 45.6], [150, 47], [162, 52], [172, 60], [-169.5, 65.8], [-174, 70], [170, 71.2],
      [155, 74.5], [128, 76.8], [104, 78.2], [80, 76.5], [60, 74.5], [40, 72.3], [25, 71.6], [10, 66], [4.5, 60], [4.2, 52.2]];
    const s = [
      T.defs,
      C.etiq("", [108, 31], "CHINE", { cl: "k-pays" }), C.etiq("", [95, 62], "RUSSIE", { cl: "k-pays" }), C.etiq("", [-100, 60], "CANADA", { cl: "k-pays" }),
      C.etiq("", [-40, 73], "GROENLAND", { cl: "k-pays" }), C.etiq("", [138, 37.5], "JAPON", { cl: "k-pays" }),
      C.point("cn", [116.4, 39.9], "Pékin", { a: "start", cl: "pt-b" }),
      C.etiq("cnt", [62, 51], "« État proche de l'Arctique » (2018)", { cl: "lbl-f" }),
      T.trajet("route", ROUTE, { c: 0.04 }),
      C.etiq("routet", [60, 84], "la « route de la soie polaire »", { cl: "lbl-f" }),
      C.point("rott", [4.3, 51.9], "vers les ports d'Europe", { a: "end", dy: 22 })
    ].join("");
    return { titre: "Une « route de la soie polaire »", w: W, h: H, vb: [0, 0, W, H], svg: fond + s, etapes: [], rose: [628, 628, 46],
      source: "Fond Natural Earth (domaine public). Tracé de la route maritime du Nord approximatif ; navigable surtout l'été." };
  }

  /* 5. « La face cachée de la Lune » : schéma sans échelle (projection orthographique centrée sur la face cachée) */
  function lune(D, d3) {
    const W = 1000, H = 500, R = 200, cx = 300, cy = 230;
    const pr = d3.geoOrthographic().rotate([-180, 0]).scale(R).translate([cx, cy]).clipAngle(90);
    const P = ll => pr(ll).map(v => Math.round(v));
    const pt = (k, ll, nom, o = {}) => {
      const [x, y] = P(ll), a = o.a || "start", dx = a === "end" ? -14 : 14;
      return "<g data-k='" + k + "'><circle cx='" + x + "' cy='" + y + "' r='8' class='" + (o.cl || "pt-a") + "'/>" +
        "<text x='" + (x + dx) + "' y='" + (y + 6 + (o.dy || 0)) + "' text-anchor='" + a + "' class='lbl'>" + esc(nom) + "</text></g>";
    };
    /* cratères décoratifs (positions fixes) */
    const CR = [[150, 20, 9], [210, 35, 6], [165, -10, 7], [200, 5, 11], [135, -35, 6], [225, -20, 8], [185, 55, 7], [170, -60, 9], [140, 50, 5], [215, 60, 5], [195, -40, 6]];
    const crat = CR.map(([lo, la, r]) => { const c = pr([lo, la]); return c ? "<circle cx='" + c[0].toFixed(0) + "' cy='" + c[1].toFixed(0) + "' r='" + r * 2.2 + "' fill='none' stroke='#8f8a78' stroke-width='2' opacity='.7'/>" : ""; }).join("");
    const gp = d3.geoPath(pr);
    const grille = [-60, -30, 0, 30, 60].map(la => "<path d='" + gp({ type: "LineString", coordinates: d3.range(90, 271, 5).map(lo => [lo, la]) }) + "' fill='none' stroke='#9c967f' stroke-width='1' stroke-dasharray='3 5'/>").join("");
    const [tx, ty] = [860, 230];
    const s = [
      "<defs><marker id='fl-lune' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker></defs>",
      "<g data-k='disque'><circle cx='" + cx + "' cy='" + cy + "' r='" + R + "' fill='#d9d3bf' stroke='var(--encre)' stroke-width='3'/>" + grille + crat +
      "<text x='" + cx + "' y='" + (cy - R - 16) + "' text-anchor='middle' class='lbl-f'>la face cachée de la Lune</text></g>",
      "<g data-k='terre'><circle cx='" + tx + "' cy='" + ty + "' r='46' fill='#7f9fbf' stroke='var(--encre)' stroke-width='2.5'/>" +
      "<text x='" + tx + "' y='" + (ty + 80) + "' text-anchor='middle' class='lbl'>la Terre</text></g>",
      "<g data-k='jamais'><text x='" + (tx - 10) + "' y='" + (ty - 92) + "' text-anchor='middle' class='lbl'>jamais visible</text><text x='" + (tx - 10) + "' y='" + (ty - 64) + "' text-anchor='middle' class='lbl'>depuis la Terre</text></g>",
      pt("ce4", [177.6, -45.5], "Chang'e 4 : 3 janvier 2019", { a: "end", dy: -4 }),
      pt("ce6", [-153.98, -41.6], "Chang'e 6 : juin 2024", { a: "start", dy: -20 }),
      "<path data-k='retour' class='trace' pathLength='1' d='M" + P([-153.98, -41.6]).join(",") + "Q" + 620 + "," + 440 + " " + (tx - 40) + "," + (ty + 34) + "' fill='none' stroke='var(--rouge)' stroke-width='3' stroke-linecap='round' marker-end='url(#fl-lune)'/>",
      "<text data-k='retourt' x='" + 650 + "' y='" + 478 + "' text-anchor='middle' class='lbl-f'>échantillons sur Terre : 25 juin 2024</text>",
      pt("pole", [180, -88], "pôle Sud : sans doute de la glace d'eau", { a: "end", cl: "pt-b", dy: 30 })
    ].join("");
    return { titre: "La face cachée de la Lune", w: W, h: H, vb: [0, 0, W, H], svg: s, etapes: [],
      source: "Schéma sans échelle ; positions des sites d'atterrissage approximatives." };
  }

  return {
    cartes: { chine, voisins, alliances, polaire, lune },
    videos: { "hggsp-t1-otc": { site: ["scs"], video: ["chine", "voisins", "alliances", "polaire", "lune"] } },
    sources: {}
  };
};
