/* Scènes cartographiques des animations du responsable (thèmes 1, 2 et 5) et carte des États-Unis.
   Chaque scène : ctx.OUT.anims.nom = { w, h, vb, fond, calques } ; les éléments animés portent data-k.
   Les étapes (dates, textes) sont dans src/data-anims.js. Coordonnées : [longitude, latitude]. */
module.exports = function (ctx) {
  const { d3, cadre, M, WM, HM, OUT } = ctx;
  const esc = ctx.esc;

  /* ---- outils de dessin ---- */
  function outils(C, nom) {
    const mk = "fl-" + nom;
    const defs = "<defs><marker id='" + mk + "' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker>" +
      "<marker id='" + mk + "b' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--acier)'/></marker></defs>";
    /* point avec étiquette ; o.cl : classe du point (pt-a rouge, pt-b bleu) ; o.a : ancre ; o.dy */
    const point = (k, ll, nomLieu, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -9 : a === "middle" ? 0 : 9;
      return "<g data-k='" + k + "'><circle cx='" + x + "' cy='" + y + "' r='" + (o.r || 6.5) + "' class='" + (o.cl || "pt-a") + "'/>" +
        (nomLieu ? "<text x='" + (x + dx) + "' y='" + (y + 4 + (o.dy || 0)) + "' text-anchor='" + a + "' class='" + (o.lc || "lbl") + "'>" + esc(nomLieu) + "</text>" : "") + "</g>";
    };
    /* flèche courbe de a vers b (courbure c) ; bleu si o.b */
    const fleche = (k, a, b, o = {}) => {
      const [x1, y1] = C.P(a), [x2, y2] = C.P(b), mx = (x1 + x2) / 2, my = (y1 + y2) / 2, dx = x2 - x1, dy = y2 - y1, c = o.c === undefined ? 0.2 : o.c;
      const cx = Math.round(mx - dy * c), cy = Math.round(my + dx * c);
      return "<path data-k='" + k + "' class='trace' pathLength='1' d='M" + x1 + "," + y1 + "Q" + cx + "," + cy + " " + x2 + "," + y2 + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") + "' stroke-width='" + (o.w || 3) + "' stroke-linecap='round' marker-end='url(#" + mk + (o.b ? "b" : "") + ")'/>";
    };
    /* un anneau mal orienté désignerait tout le globe sauf la zone : on le retourne si besoin */
    const zone = (k, ring, cl) => { if (d3.geoArea({ type: "Polygon", coordinates: [ring] }) > 2 * Math.PI) ring = ring.slice().reverse(); return "<g data-k='" + k + "'>" + C.poly(ring, "class='" + (cl || "zone") + "'") + "</g>"; };
    const etiq = (k, ll, s, o = {}) => { const [x, y] = C.P(ll); return "<text data-k='" + k + "' x='" + (x + (o.dx || 0)) + "' y='" + (y + (o.dy || 0)) + "' text-anchor='" + (o.a || "middle") + "' class='" + (o.cl || "lbl-f") + "'>" + esc(s) + "</text>"; };
    return { defs, point, fleche, zone, etiq };
  }
  /* fenêtre (viewBox) qui contient le rectangle géographique sw-ne : on échantillonne ses bords */
  const vbDe = (C, sw, ne, W, H) => {
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (let i = 0; i <= 20; i++) for (const [lo, la] of [[sw[0] + (ne[0] - sw[0]) * i / 20, sw[1]], [sw[0] + (ne[0] - sw[0]) * i / 20, ne[1]], [sw[0], sw[1] + (ne[1] - sw[1]) * i / 20], [ne[0], sw[1] + (ne[1] - sw[1]) * i / 20]]) {
      const [x, y] = C.P([lo, la]); x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y);
    }
    x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(W, x1); y1 = Math.min(H, y1);
    return [x0, y0, x1 - x0, y1 - y0];
  };
  const regional = (sw, ne, W, H, tol) => {
    const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [sw, ne] });
    const C = cadre(proj, W, H, tol || 0.35, 0.6);
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/><path d='" + C.pays() + "' class='k-terre'/>";
    return { C, fond };
  };

  /* ================= 1. La course à l'espace (monde) ================= */
  {
    const T = outils(M, "espace");
    const s = [
      T.point("baik", [63.3, 45.9], "Baïkonour (URSS)", { a: "start" }),
      T.point("canav", [-80.6, 28.5], "Cap Canaveral (États-Unis)", { a: "start", cl: "pt-b" }),
      T.point("hamm", [-3.1, 30.9], "Hammaguir (France, Algérie)", { a: "end" }),
      T.point("uchi", [131.1, 31.3], "Uchinoura (Japon)", { a: "start" }),
      T.point("jiuq", [100.3, 41.0], "Jiuquan (Chine)", { a: "end" }),
      T.point("woom", [136.5, -31.1], "Woomera (R.-U., Australie)", { a: "end" }),
      T.point("kourou", [-52.8, 5.2], "Kourou (Europe)", { a: "start" }),
      T.point("srih", [80.2, 13.7], "Sriharikota (Inde)", { a: "end" }),
      T.point("palm", [34.7, 31.9], "Palmachim (Israël)", { a: "end", dy: 6 }),
      T.point("semn", [53.9, 35.2], "Semnan (Iran)", { a: "start", dy: -4 }),
      T.point("sohae", [124.7, 39.7], "Sohae (Corée du Nord)", { a: "start", dy: -6 }),
      T.point("starb", [-97.2, 26.0], "Starbase (SpaceX)", { a: "end", cl: "pt-b" }),
      T.point("mahia", [177.9, -39.3], "Mahia (Rocket Lab)", { a: "end", cl: "pt-b" }),
      T.point("wench", [111.0, 19.6], "Wenchang (Chine)", { a: "start" }),
      T.fleche("lune1", [-80.6, 28.5], [-40, 60], { b: true, c: -0.25 }),
      T.etiq("lune1t", [-40, 64], "Apollo 11 → la Lune", { cl: "lbl-f" }),
      T.fleche("lune2", [-80.6, 28.5], [-45, 58], { c: -0.3 }),
      T.etiq("lune2t", [-45, 62], "Artemis II autour de la Lune", { cl: "lbl-f" })
    ].join("");
    OUT.anims.espace = { w: WM, h: HM, vb: vbDe(M, [-125, -46], [180, 66], WM, HM), fond: "monde", calques: T.defs + s };
  }

  /* ================= 2. ONU sous Kofi Annan (monde) ================= */
  {
    const T = outils(M, "onu");
    const P = (k, ll, n, a, cl, dy) => T.point(k, ll, n, { a, cl: cl || "pt-b", dy });
    const s = [
      P("rwanda", [30.1, -1.9], "Rwanda 1994", "start", "pt-a", 2),
      P("srebr", [19.3, 44.1], "Srebrenica 1995", "end", "pt-a", -4),
      P("kosovo", [21.0, 42.6], "Kosovo 1999", "start", null, 4),
      P("timor", [125.6, -8.6], "Timor oriental 1999", "end"),
      P("sleone", [-11.8, 8.5], "Sierra Leone 1999", "end", null, -4),
      P("rdc", [23.6, -2.9], "RDC 1999", "end", null, 6),
      P("eth", [38.9, 15.2], "Éthiopie-Érythrée 2000", "start"),
      P("liberia", [-9.4, 6.4], "Liberia 2003", "end", null, 8),
      P("irak", [44.4, 33.3], "Irak 2003 (sans l'ONU)", "start", "pt-a"),
      P("civ", [-5.5, 7.5], "Côte d'Ivoire 2004", "start", null, 4),
      P("haiti", [-72.3, 18.9], "Haïti 2004", "start"),
      P("burundi", [29.9, -3.4], "Burundi 2004", "start", null, 8),
      P("soudan", [31.6, 9.5], "Soudan 2005", "end"),
      P("liban", [35.5, 33.3], "Liban 2006", "end", null, -2),
      P("ny", [-74.0, 40.7], "Siège de l'ONU (New York)", "start", "pt-a")
    ].join("");
    OUT.anims.annan = { w: WM, h: HM, vb: [209, 37, 678, 287], fond: "monde", calques: T.defs + s };
  }

  /* ================= 3. COP et sommets (monde) ================= */
  {
    const T = outils(M, "cop");
    const P = (k, ll, n, a, dy, cl) => T.point(k, ll, n, { a, dy, cl: cl || "pt-b" });
    const s = [
      P("stock", [18.07, 59.33], "Stockholm 1972", "start", -6, "pt-a"),
      P("rio", [-43.2, -22.9], "Rio 1992", "start", 0, "pt-a"),
      P("berlin", [13.4, 52.5], "Berlin 1995 (COP1)", "start", 12),
      P("kyoto", [135.77, 35.0], "Kyoto 1997", "start"),
      P("copen", [12.57, 55.68], "Copenhague 2009", "start", 2),
      P("paris", [2.35, 48.86], "Paris 2015", "end", 10, "pt-a"),
      P("glasg", [-4.25, 55.86], "Glasgow 2021", "end", -4),
      P("dubai", [55.3, 25.2], "Dubaï 2023", "start", 6),
      P("bakou", [49.87, 40.41], "Bakou 2024", "start", -2),
      P("belem", [-48.5, -1.46], "Belém 2025", "start", 0),
      P("antal", [30.7, 36.9], "Antalya 2026", "start", 6, "pt-a"),
      P("wash", [-77.0, 38.9], "Washington : retraits 2020 et 2026", "start", 0, "pt-a")
    ].join("");
    OUT.anims.cop = { w: WM, h: HM, vb: vbDe(M, [-95, -32], [150, 64], WM, HM), fond: "monde", calques: T.defs + s };
  }

  /* ================= 4. Mer de Chine méridionale ================= */
  {
    const { C, fond } = regional([103, 1], [124, 24], 760, 820, 0.3);
    const T = outils(C, "scs");
    const NEUF = [[108.3, 18.0], [109.2, 15.5], [109.6, 12.5], [109.8, 10.0], [109.0, 7.5], [110.6, 5.5], [112.3, 3.9], [113.9, 5.7], [115.2, 7.0], [116.3, 8.4], [117.1, 10.2], [118.4, 12.4], [119.1, 15.0], [119.7, 17.8], [120.8, 20.0], [121.8, 21.8]];
    const s = [
      "<g data-k='ligne'>" + C.ligne(NEUF, "class='k-neuf'") + "</g>",
      T.etiq("lignet", [117.6, 20.6], "ligne en neuf traits", { cl: "lbl", a: "end" }),
      T.point("paracel", [112.3, 16.8], "Paracels", { a: "start" }),
      T.point("johnson", [114.28, 9.72], "Johnson South", { a: "start", dy: 10 }),
      T.point("mischief", [115.53, 9.9], "Mischief", { a: "start", dy: -6 }),
      T.point("scarb", [117.76, 15.15], "Scarborough", { a: "start" }),
      T.point("fiery", [112.89, 9.55], "Fiery Cross", { a: "end" }),
      T.point("subi", [114.08, 10.92], "Subi", { a: "start", dy: -4 }),
      T.point("sanya", [109.6, 18.2], "Sanya", { a: "end", cl: "pt-b" }),
      T.point("woody", [112.33, 16.83], "", { r: 9, cl: "pt-b" }),
      T.etiq("sansha", [112.0, 17.8], "« ville de Sansha » (2012)", { cl: "lbl", a: "end" }),
      T.zone("iles", [[112.5, 9.2], [116.0, 9.2], [116.0, 11.3], [112.5, 11.3], [112.5, 9.2]], "zone"),
      T.etiq("ilest", [114.3, 8.6], "îles artificielles", { cl: "lbl-f" }),
      T.etiq("pca", [120.8, 11.0], "sentence de 2016 : « droits historiques » rejetés", { cl: "lbl", a: "start" }),
      T.etiq("vn", [106.5, 14.5], "VIÊT NAM", { cl: "lbl", a: "middle" }),
      T.etiq("ph", [122.5, 13.3], "PHILIPPINES", { cl: "lbl", a: "middle" }),
      T.etiq("cn", [112.0, 22.8], "CHINE", { cl: "lbl", a: "middle" })
    ].join("");
    OUT.anims.scs = { w: 760, h: 820, fond, calques: T.defs + s };
  }

  /* ================= 5. Daech : essor et recul (Irak-Syrie) ================= */
  {
    const { C, fond } = regional([35.5, 31.6], [48.2, 38.0], 900, 520, 0.3);
    const T = outils(C, "daech");
    const V = [["raqqa", [39.01, 35.95], "Raqqa", "end"], ["fallu", [43.78, 33.35], "Falloujah", "start"], ["mos", [43.13, 36.34], "Mossoul", "start"], ["tik", [43.68, 34.6], "Tikrit", "start"],
      ["sinj", [41.87, 36.32], "Sinjar", "end"], ["ram", [43.3, 33.42], "Ramadi", "end"], ["palm", [38.27, 34.56], "Palmyre", "end"]];
    let s = "";
    V.forEach(([k, ll, n, a]) => { s += T.point(k + "_r", ll, n, { a, cl: "pt-a", r: 8 }) + T.point(k + "_b", ll, n, { a, cl: "pt-b", r: 8 }); });
    s += T.point("kob_b", [38.36, 36.89], "Kobané", { a: "end", cl: "pt-b", r: 8 }) + T.point("bagh_b", [40.94, 34.47], "Baghouz", { a: "start", cl: "pt-b", r: 8, dy: 4 });
    s += T.point("bagdad", [44.36, 33.31], "Bagdad", { a: "start", cl: "pt-b", r: 5, lc: "lbl" }) + T.point("damas", [36.29, 33.51], "Damas", { a: "start", cl: "pt-b", r: 5 });
    s += T.etiq("syr", [38.6, 35.1], "SYRIE", { cl: "lbl" }) + T.etiq("irq", [42.2, 32.6], "IRAK", { cl: "lbl" }) + T.etiq("tur", [40.5, 37.6], "TURQUIE", { cl: "lbl" });
    s += T.etiq("calif", [42.0, 35.15], "« califat » proclamé le 29 juin 2014", { cl: "lbl-f" });
    OUT.anims.daech = { w: 900, h: 520, fond, calques: T.defs + s };
  }

  /* ================= 6. Les guerres du Golfe (Moyen-Orient) ================= */
  {
    const { C, fond } = regional([36, 23], [60, 38.5], 900, 640, 0.35);
    const T = outils(C, "golfe");
    const s = [
      T.etiq("iriq", [48.5, 33.3], "guerre Iran-Irak 1980-1988", { cl: "lbl-f" }),
      T.fleche("inv", [44.4, 33.3], [47.8, 29.6], { c: 0.15 }),
      T.point("kow", [47.98, 29.37], "Koweït", { a: "start", dy: 6 }),
      T.fleche("coal", [45.0, 25.0], [47.2, 29.0], { b: true, c: -0.2 }),
      T.etiq("coalt", [45.0, 24.3], "coalition de 35 pays (ONU)", { cl: "lbl", a: "middle" }),
      "<g data-k='nfz'>" + C.ligne([[38.9, 36], [44.4, 36]], "class='k-nfz'") + C.ligne([[39.0, 33], [47.0, 33]], "class='k-nfz'") + "</g>",
      T.etiq("nfzt", [41.6, 36.6], "zones d'exclusion aérienne", { cl: "lbl", a: "middle" }),
      T.fleche("inv03", [47.6, 29.3], [44.6, 33.0], { c: -0.2, w: 4 }),
      T.point("bag", [44.36, 33.31], "Bagdad", { a: "end", cl: "pt-b" }),
      T.etiq("bag03", [43.9, 32.4], "prise le 9 avril 2003", { cl: "lbl-f", a: "end" }),
      T.etiq("civ", [43.6, 34.4], "insurrection, guerre civile 2006-2007", { cl: "lbl", a: "end" }),
      T.point("mos", [43.13, 36.34], "Mossoul (Daech, 2014)", { a: "start" }),
      T.point("ormuz", [56.3, 26.6], "Ormuz fermé (2026)", { a: "end", dy: -8 }),
      T.point("teh", [51.4, 35.7], "Téhéran", { a: "start", cl: "pt-b" })
    ].join("");
    OUT.anims.golfe = { w: 900, h: 640, fond, calques: T.defs + s };
  }

  /* ================= 7. Yémen : une guerre civile internationalisée ================= */
  {
    const { C, fond } = regional([34, 11.2], [58, 27], 900, 600, 0.35);
    const T = outils(C, "yemen");
    const s = [
      T.point("sanaa", [44.19, 15.37], "Sanaa", { a: "end" }),
      T.etiq("houthi", [44.2, 17.2], "Houthis", { cl: "lbl-f" }),
      T.point("aden", [45.03, 12.8], "Aden (gouvernement)", { a: "start", cl: "pt-b" }),
      T.point("riyad", [46.68, 24.71], "Riyad", { a: "start", cl: "pt-b" }),
      T.fleche("coal", [46.68, 24.4], [44.6, 15.9], { b: true, c: 0.15 }),
      T.etiq("coalt", [48.6, 20.5], "coalition menée par l'Arabie saoudite", { cl: "lbl", a: "middle" }),
      T.fleche("iran", [57.5, 26.5], [45.2, 16.3], { c: 0.25 }),
      T.etiq("irant", [55.0, 24.2], "soutien de l'Iran", { cl: "lbl-f" }),
      T.point("hod", [42.95, 14.8], "Hodeïda", { a: "end" }),
      T.etiq("treve", [44.2, 14.0], "trêve de l'ONU (avril 2022)", { cl: "lbl", a: "middle" }),
      T.fleche("mer", [43.2, 15.6], [38.6, 19.5], { c: 0.2 }),
      T.etiq("mert", [38.3, 20.4], "attaques en mer Rouge", { cl: "lbl-f" }),
      T.point("bab", [43.4, 12.6], "Bab el-Mandeb", { a: "end", r: 5 }),
      T.fleche("usuk", [36.8, 21.5], [42.6, 15.5], { b: true, c: -0.25 }),
      T.etiq("usukt", [36.4, 22.4], "frappes américano-britanniques", { cl: "lbl", a: "middle" })
    ].join("");
    OUT.anims.yemen = { w: 900, h: 600, fond, calques: T.defs + s };
  }

  /* ================= 8. États-Unis : carte interactive et animation ================= */
  {
    const W = 900, H = 560;
    const proj = d3.geoConicEqualArea().parallels([29.5, 45.5]).rotate([108, 0]).fitExtent([[10, 10], [W - 10, H - 10]], { type: "MultiPoint", coordinates: [[-125, 24], [-67, 49], [-150, 62], [-120, 49], [-80, 25]] });
    const C = cadre(proj, W, H, 0.35, 0.6);
    const fondUS = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/><path d='" + C.pays(f => f.properties.ADMIN !== "United States of America") + "' class='k-terre'/><path d='" + C.pays(f => f.properties.ADMIN === "United States of America") + "' class='k-terre-cn'/>";
    const T = outils(C, "usa");
    const L = {
      yell: [[-110.6, 44.6], "Yellowstone"], yose: [[-119.6, 37.8], "Yosemite / Hetch Hetchy"], dust: [[-101.5, 36.6], "Dust Bowl"],
      cuya: [[-81.7, 41.5], "Cuyahoga (Cleveland)"], wash: [[-77.0, 38.9], "Washington (EPA)"], valdez: [[-146.4, 60.8], "Exxon Valdez"],
      dwh: [[-88.4, 28.7], "Deepwater Horizon"], perm: [[-102.5, 31.8], "Bassin permien (Texas)"], calif: [[-121.5, 38.6], "Californie"],
      plaines: [[-99.0, 40.5], "Grandes Plaines"]
    };
    const ord = [["plaines", "pt-a", "end"], ["yell", "pt-b", "start"], ["yose", "pt-b", "end"], ["dust", "pt-a", "start"], ["cuya", "pt-a", "start"], ["wash", "pt-b", "start"], ["valdez", "pt-a", "start"], ["dwh", "pt-a", "start"], ["perm", "pt-a", "end"], ["calif", "pt-b", "end"]];
    const s = ord.map(([k, cl, a]) => T.point(k, L[k][0], L[k][1], { cl, a, dy: k === "calif" ? 14 : k === "yose" ? -6 : k === "perm" ? 6 : 0 })).join("") +
      T.zone("dustz", [[-104, 35], [-98.5, 35], [-98.5, 38.5], [-104, 38.5], [-104, 35]]);
    OUT.anims.usa = { w: W, h: H, fond: fondUS, calques: T.defs + s };
    /* carte interactive à points */
    const pt = (c, ll, n, a, t, d) => { const [x, y] = C.P(ll); return { c, x, y, n, a, t, d }; };
    OUT.cartes.usa = { w: W, h: H, fond: fondUS, deco: C.txt([-98, 39], "ÉTATS-UNIS", { a: "middle" }) + C.txt([-105, 54], "CANADA", { a: "middle" }) + C.txt([-102, 26], "MEXIQUE", { a: "middle" }) + C.txt([-150, 64.5], "ALASKA", { a: "middle" }),
      meta: { t: "Les États-Unis : protéger et exploiter", c: { prot: ["Protection de la nature et lois", "#2D5675"], expl: ["Exploitation et catastrophes", "#B3241B"] } },
      pts: [
        pt("prot", [-110.6, 44.6], "Yellowstone", "start", "Yellowstone (Wyoming)", "Premier parc national du monde, créé le 1er mars 1872 ; les Amérindiens qui fréquentaient ces terres en sont écartés."),
        pt("prot", [-119.6, 37.8], "Yosemite", "end", "Yosemite et Hetch Hetchy (Californie)", "John Muir défend la Sierra Nevada (Sierra Club, 1892) ; la vallée de Hetch Hetchy est noyée par un barrage autorisé en 1913 pour San Francisco."),
        pt("expl", [-101.5, 36.6], "Dust Bowl", "start", "Le Dust Bowl (Grandes Plaines)", "Années 1930 : sécheresse et labour intensif provoquent des tempêtes de poussière ; « dimanche noir » le 14 avril 1935 ; service de conservation des sols créé en 1935."),
        pt("expl", [-81.7, 41.5], "Cuyahoga", "start", "La Cuyahoga à Cleveland (Ohio)", "Le 22 juin 1969, la rivière polluée prend feu : un symbole qui pousse aux grandes lois des années 1970."),
        pt("prot", [-77.0, 38.9], "Washington", "start", "Washington : l'État fédéral", "EPA créée le 2 décembre 1970 ; Clean Air Act (1970), Clean Water Act (1972), Endangered Species Act (1973) ; retraits de l'accord de Paris (2020, 2026) ; abrogation du constat de danger du CO₂ (février 2026)."),
        pt("expl", [-146.4, 60.8], "Exxon Valdez", "start", "Exxon Valdez (Alaska)", "Le 24 mars 1989, le pétrolier s'échoue dans le détroit du Prince-William et pollue des centaines de kilomètres de côtes."),
        pt("expl", [-88.4, 28.7], "Deepwater Horizon", "start", "Deepwater Horizon (golfe du Mexique)", "Le 20 avril 2010, l'explosion de la plateforme tue 11 personnes ; environ 4,9 millions de barils se répandent selon les estimations fédérales."),
        pt("expl", [-102.5, 31.8], "Bassin permien", "end", "Le bassin permien (Texas, Nouveau-Mexique)", "Cœur du pétrole de schiste, exploité par fracturation hydraulique : les États-Unis sont le premier producteur mondial de pétrole depuis 2018."),
        pt("prot", [-121.5, 38.6], "Californie", "end", "La Californie", "État pionnier, longtemps autorisé à fixer des normes automobiles plus strictes ; cofondateur de l'Alliance des États-Unis pour le climat (2017) ; autorisation annulée par le Congrès en juin 2025, contestée en justice.")
      ] };
    OUT.cartes.usa.pts.forEach(p => { if (p.n === "Californie") p.dy = 12; if (p.n === "Yosemite") p.dy = -4; });
  }
};
