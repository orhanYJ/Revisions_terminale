/* Scènes cartographiques des animations ajoutées au contrôle visuel (deuxième animation de certains chapitres) :
   dilemme de Malacca (thème 1), traités de Westphalie (thème 2), procès des criminels nazis (thème 3).
   Chargé par cartes.js (fonction (ctx)) après cartes-t3.js, dont il réutilise les fonds d'Europe (ctx.EUROPEC,
   ctx.EUROPEE : même chaîne, stockée une seule fois dans la page). Étapes et textes : src/data-z-anims.js.
   Coordonnées : [longitude, latitude]. */
module.exports = function (ctx) {
  const { M, WM, HM, OUT, esc } = ctx;

  /* fenêtre (viewBox) qui contient le rectangle géographique sw-ne */
  const vbDe = (C, sw, ne, W, H) => {
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (let i = 0; i <= 20; i++) for (const [lo, la] of [[sw[0] + (ne[0] - sw[0]) * i / 20, sw[1]], [sw[0] + (ne[0] - sw[0]) * i / 20, ne[1]], [sw[0], sw[1] + (ne[1] - sw[1]) * i / 20], [ne[0], sw[1] + (ne[1] - sw[1]) * i / 20]]) {
      const [x, y] = C.P([lo, la]); x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y);
    }
    x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(W, x1); y1 = Math.min(H, y1);
    return [x0, y0, x1 - x0, y1 - y0].map(Math.round);
  };

  /* outils de dessin ; fs : taille des textes en unités de la scène (adaptée au cadrage) */
  function outils(C, nom, fs) {
    const mk = "flz-" + nom, R = v => Math.round(v * 10) / 10;
    const defs = "<defs><marker id='" + mk + "' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker>" +
      "<marker id='" + mk + "b' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--acier)'/></marker></defs>";
    const st = k => " style='font-size:" + R(fs * (k || 1)) + "px'";
    const txt = (ll, s, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -fs * 0.8 : a === "middle" ? 0 : fs * 0.8;
      return "<text x='" + R(x + dx + (o.dx || 0) * fs) + "' y='" + R(y + fs * 0.35 + (o.dy || 0) * fs) + "' text-anchor='" + a + "' class='" + (o.cl || "lbl") + "'" + st(o.t) + ">" + esc(s) + "</text>";
    };
    /* point et étiquette(s) dans un groupe data-k ; o.l2 : seconde ligne ; dy, dx en multiples de fs */
    const point = (k, ll, s, o = {}) => {
      const [x, y] = C.P(ll);
      return "<g data-k='" + k + "'><circle cx='" + x + "' cy='" + y + "' r='" + R(o.r || fs * 0.6) + "' class='" + (o.cl || "pt-a") + "'/>" + (s ? txt(ll, s, Object.assign({}, o, { cl: o.lc || "lbl" })) : "") +
        (o.l2 ? txt(ll, o.l2, Object.assign({}, o, { dy: (o.dy || 0) + 1.25, cl: "lbl", t: 0.9 })) : "") + "</g>";
    };
    const fleche = (k, a, b, o = {}) => {
      const [x1, y1] = C.P(a), [x2, y2] = C.P(b), c = o.c === undefined ? 0.2 : o.c;
      const cx = (x1 + x2) / 2 - (y2 - y1) * c, cy = (y1 + y2) / 2 + (x2 - x1) * c;
      return "<path data-k='" + k + "' class='trace' pathLength='1' d='M" + x1 + "," + y1 + "Q" + R(cx) + "," + R(cy) + " " + x2 + "," + y2 + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") + "' stroke-width='" + R(o.w || fs * 0.22) + "' stroke-linecap='round'" + (o.tir ? " stroke-dasharray='" + o.tir + "'" : "") + " marker-end='url(#" + mk + (o.b ? "b" : "") + ")'/>";
    };
    /* trajet par points de passage (ligne géodésique simplifiée, sans pointe) */
    const trajet = (k, pts, o = {}) => "<path data-k='" + k + "' class='trace' pathLength='1' d='" + C.gp({ type: "LineString", coordinates: pts }) + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") + "' stroke-width='" + R(o.w || fs * 0.3) + "' stroke-linecap='round' stroke-linejoin='round'" + (o.tir ? " stroke-dasharray='" + o.tir + "'" : "") + "/>";
    const anneau = (k, ll, r, coul) => { const [x, y] = C.P(ll); return "<circle data-k='" + k + "' cx='" + x + "' cy='" + y + "' r='" + R(r) + "' fill='none' stroke='" + (coul || "var(--rouge)") + "' stroke-width='" + R(fs * 0.25) + "'/>"; };
    const croix = (k, ll, r) => { const [x, y] = C.P(ll); return "<path data-k='" + k + "' d='M" + R(x - r) + "," + R(y - r) + "L" + R(x + r) + "," + R(y + r) + "M" + R(x + r) + "," + R(y - r) + "L" + R(x - r) + "," + R(y + r) + "' stroke='var(--rouge)' stroke-width='" + R(fs * 0.4) + "' stroke-linecap='round'/>"; };
    const etiq = (k, ll, s, o = {}) => txt(ll, s, o).replace("<text ", "<text data-k='" + k + "' ");
    return { defs, txt, point, fleche, trajet, anneau, croix, etiq };
  }

  /* ================= Thème 1 : le « dilemme de Malacca » (fond du monde) ================= */
  {
    const vb = vbDe(M, [36, -9], [124, 41], WM, HM), fs = Math.round(vb[2] / 780 * 13 * 10) / 10;
    const T = outils(M, "malacca", fs);
    const L = { ormuz: [56.3, 26.6], malacca: [100.9, 2.9], gwadar: [62.33, 25.12], kyauk: [93.55, 19.43], kunming: [102.71, 25.04], hamb: [81.12, 6.12], djib: [43.15, 11.59], canton: [113.3, 23.1] };
    const route = [[56.3, 26.6], [57.6, 25.2], [60.5, 22.6], [64, 18], [74, 7.5], [81, 5.2], [92, 6.3], [97.5, 5.4], [100.9, 2.9], [104.3, 1.3], [107.5, 6], [111.5, 15], [113.3, 21.5]];
    const s = [
      T.trajet("route", route, { w: fs * 0.42 }),
      T.etiq("routet", [70, 13.2], "pétrole et gaz du golfe vers la Chine", { a: "middle", cl: "lbl-f", t: 0.95 }),
      T.point("ormuz", L.ormuz, "Ormuz", { a: "end", dy: -0.6, cl: "pt-b" }),
      T.point("chine", L.canton, "CHINE", { a: "start", cl: "pt-b", lc: "lbl-f" }),
      T.anneau("goulot", L.malacca, fs * 1.6),
      T.croix("blocage", [99.5, 4.4], fs * 0.7),
      T.point("malacca", L.malacca, "détroit de Malacca", { a: "end", dy: 1.2, l2: "un goulet que la marine américaine pourrait bloquer" }),
      T.point("gwadar", L.gwadar, "Gwadar (Pakistan)", { a: "start", dy: -0.9, l2: "exploité par une société chinoise depuis 2013" }),
      T.trajet("tubes", [L.kyauk, [96, 21.5], [98.5, 24], L.kunming], { b: true, tir: "1.5 1", w: fs * 0.35 }),
      T.point("kyauk", L.kyauk, "Kyaukpyu (Birmanie)", { a: "end", cl: "pt-b", l2: "gazoduc 2013, oléoduc 2017" }),
      T.point("kunming", L.kunming, "Yunnan", { a: "start", cl: "pt-b", dy: -0.4 }),
      T.point("hamb", L.hamb, "Hambantota (Sri Lanka)", { a: "start", dy: 1.2, l2: "concédé pour 99 ans (déc. 2017)" }),
      T.point("djib", L.djib, "Djibouti", { a: "start", dy: -0.6, l2: "1re base militaire chinoise à l'étranger (2017)" }),
      T.etiq("inde", [79, 21], "INDE", { a: "middle", cl: "k-pays", t: 0.95 })
    ].join("");
    OUT.anims.malacca = { w: WM, h: HM, vb, mw: 760, fond: "monde", calques: T.defs + s };
  }

  /* ================= Thème 2 : la paix de Westphalie (1648), fond d'Europe centrale ================= */
  {
    const { C, fondC, WC, HC } = ctx.EUROPEC;
    const vb = vbDe(C, [-2.6, 42.6], [22.8, 55.6], WC, HC), fs = Math.round(vb[2] / 780 * 12.5 * 10) / 10;
    const T = outils(C, "westph", fs);
    const V = { prague: [14.42, 50.08], magde: [11.63, 52.13], munster: [7.63, 51.96], osna: [8.05, 52.28], amsterdam: [4.9, 52.37], suisse: [8.23, 46.82], alsace: [7.45, 48.3], metz: [6.18, 49.12], toul: [5.89, 48.68], verdun: [5.38, 49.16], stettin: [14.55, 53.43], breme: [9.0, 53.45], vienne: [16.37, 48.21], paris: [2.35, 48.86], pyr: [-1.76, 43.34] };
    const s = [
      T.point("prague", V.prague, "Prague, 23 mai 1618", { a: "start", dy: 0.2, l2: "défenestration : la guerre commence" }),
      T.point("vienne", V.vienne, "Vienne : l'empereur", { a: "end", dy: 1.1, cl: "pt-b" }),
      T.point("magde", V.magde, "Magdebourg, 20 mai 1631", { a: "start", dy: -0.5, l2: "sac : environ 20 000 morts" }),
      T.point("munster", V.munster, "Münster", { a: "end", r: fs * 0.75, cl: "pt-b", lc: "lbl-f" }),
      T.point("osna", V.osna, "Osnabrück", { a: "start", dy: -0.6, r: fs * 0.75, cl: "pt-b", lc: "lbl-f" }),
      T.etiq("congres", [4.4, 50.6], "1643-1648 : le congrès", { a: "end", cl: "lbl", t: 0.95 }),
      T.point("pu", V.amsterdam, "Provinces-Unies", { a: "end", dy: -0.5, cl: "pt-b", l2: "indépendantes (paix de Münster)" }),
      T.point("fr", V.alsace, "France : droits en Alsace,", { a: "end", dy: 2.3, l2: "Metz, Toul et Verdun confirmés" }),
      "<g data-k='eveches'>" + [V.metz, V.toul, V.verdun].map(ll => { const [x, y] = C.P(ll); return "<circle cx='" + x + "' cy='" + y + "' r='" + (fs * 0.42).toFixed(1) + "' class='pt-a'/>"; }).join("") + "</g>",
      T.point("sue", V.stettin, "Suède : Poméranie occidentale", { a: "start", dy: -0.6 }),
      T.point("breme", V.breme, "et duché de Brême", { a: "start", dy: -0.6 }),
      T.point("ch", V.suisse, "Confédération suisse", { a: "start", dy: 0.6, cl: "pt-b", l2: "indépendance reconnue" }),
      T.point("paris", V.paris, "Paris", { a: "end", r: fs * 0.45, cl: "pt-b" }),
      T.point("pyr", V.pyr, "paix des Pyrénées, 7 nov. 1659", { a: "start", dy: -0.2, cl: "pt-b" }),
      "<text x='" + (vb[0] + 8) + "' y='" + (vb[1] + vb[3] - 8) + "' class='k-note'" + " style='font-size:" + (fs * 0.8).toFixed(1) + "px'>frontières actuelles (fond de carte)</text>"
    ].join("");
    OUT.anims.westph = { w: WC, h: HC, vb, mw: 760, fond: fondC, calques: T.defs + s };
  }

  /* ================= Thème 3 : juger les criminels nazis après Nuremberg (fond d'Europe) ================= */
  {
    const { E, fondE, WE, HE } = ctx.EUROPEE;
    const vb = vbDe(E, [-9, 30.5], [37, 57], WE, HE), fs = Math.round(vb[2] / 780 * 12.5 * 10) / 10;
    const T = outils(E, "proces", fs);
    const V = { nur: [11.08, 49.45], jer: [35.21, 31.77], franc: [8.68, 50.11], lyon: [4.84, 45.76], vers: [2.13, 48.8], bdx: [-0.58, 44.84], mun: [11.58, 48.14], lun: [10.41, 53.25], itz: [9.52, 53.92] };
    const s = [
      T.point("nur", V.nur, "Nuremberg 1945-1946", { a: "start", dy: -0.3, r: fs * 0.75, l2: "+ procès des médecins (1946-1947)" }),
      T.fleche("eich", [-8.5, 34], V.jer, { c: 0.08, b: true, tir: "0.02 0.015" }),
      T.etiq("eicht", [-8.2, 35.2], "enlevé en Argentine (mai 1960)", { a: "start", t: 0.9 }),
      T.point("jer", V.jer, "Jérusalem 1961 : Eichmann", { a: "end", dy: -0.8, r: fs * 0.75 }),
      T.point("franc", V.franc, "Francfort 1963-1965", { a: "end", dy: -0.5, cl: "pt-b", l2: "procès d'Auschwitz (22 accusés)" }),
      T.etiq("impr", [-8.8, 38.2], "imprescriptibles : France 1964, RFA 1979", { a: "start", cl: "lbl-f", t: 0.95 }),
      T.point("lyon", V.lyon, "Lyon 1987 : Barbie", { a: "start", dy: 0.4 }),
      T.point("vers", V.vers, "Versailles 1994 : Touvier", { a: "end", dy: 1.1 }),
      T.point("bdx", V.bdx, "Bordeaux 1998 : Papon", { a: "end", dy: 0.4 }),
      T.point("mun", V.mun, "Munich 2011 : Demjanjuk", { a: "start", dy: 0.8, cl: "pt-b" }),
      T.point("lun", V.lun, "Lüneburg 2015 : Gröning", { a: "start", dy: 0.3, cl: "pt-b" }),
      T.point("itz", V.itz, "Itzehoe 2022 : Furchner", { a: "end", dy: -0.4, cl: "pt-b" }),
      "<text x='" + (vb[0] + 8) + "' y='" + (vb[1] + vb[3] - 8) + "' class='k-note'" + " style='font-size:" + (fs * 0.8).toFixed(1) + "px'>frontières actuelles (fond de carte)</text>"
    ].join("");
    OUT.anims.proces = { w: WE, h: HE, vb, mw: 760, fond: fondE, calques: T.defs + s };
  }
};
