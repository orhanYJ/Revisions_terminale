/* Thème 6 « L'enjeu de la connaissance » : scènes des animations et cartes interactives.
   Chargé par cartes.js (fonction (ctx)) ; les étapes des animations sont dans src/data-t6.js.
   Coordonnées : [longitude, latitude]. Données d'alphabétisation : Our World in Data, d'après l'UNESCO
   (1950 : « L'analphabétisme dans le monde au milieu du XXe siècle », 1957 ; ensuite Institut de statistique
   de l'UNESCO), taux des 15 ans et plus en %, [vers 1950, 1995-2005, 2014-2024] ; ECART : alphabétisation des
   15-24 ans, [hommes, femmes, année], pays où l'écart dépasse 10 points (dernière donnée depuis 2014). */
const LIT = {"AFG":[3,null,37],"ALB":[72,99,98],"DZA":[18,70,null],"ASM":[96,null,null],"AND":[82,null,null],"AGO":[3,67,68],"ATG":[82,99,null],"ARG":[88,97,99],"ARM":[null,99,100],"ABW":[null,97,null],"AUS":[98,null,null],"AUT":[98,null,null],"AZE":[null,99,100],"BHS":[78,null,null],"BHR":[12,87,98],"BGD":[null,47,79],"BRB":[92,null,null],"BLR":[null,100,100],"BEL":[96,null,null],"BLZ":[78,77,88],"BEN":[null,35,51],"BMU":[96,null,null],"BTN":[3,53,65],"BOL":[32,87,97],"BIH":[null,97,null],"BWA":[22,81,null],"BRA":[48,89,95],"BRN":[28,93,null],"BGR":[78,98,null],"BFA":[null,24,42],"BDI":[null,59,71],"KHM":[18,74,72],"CMR":[8,68,73],"CAN":[98,null,null],"CPV":[22,null,88],"CYM":[null,null,99],"CAF":[3,51,42],"TCD":[null,28,31],"CHL":[78,96,96],"CHN":[48,91,97],"CCK":[18,null,null],"COL":[52,93,95],"COM":[22,68,76],"COG":[null,76,null],"COK":[92,null,null],"CRI":[78,95,null],"CIV":[null,49,50],"HRV":[null,98,null],"CUB":[78,100,98],"CYP":[62,97,null],"COD":[38,67,68],"DNK":[98,null,null],"DJI":[3,null,null],"DOM":[42,87,94],"WB_EAP":[null,92,97],"TLS":[3,38,69],"ECU":[58,91,93],"EGY":[22,67,79],"SLV":[38,null,90],"GNQ":[22,88,null],"ERI":[3,53,null],"EST":[null,100,null],"SWZ":[18,82,91],"ETH":[3,36,60],"WB_ECA":[null,97,99],"FLK":[92,null,null],"FRO":[98,null,null],"FJI":[68,null,null],"FIN":[98,null,null],"FRA":[96,null,null],"GUF":[68,null,null],"PYF":[32,null,null],"GAB":[null,null,89],"GMB":[8,37,52],"GEO":[null,100,100],"DEU":[98,null,null],"GHA":[22,58,76],"GIB":[68,null,null],"GRC":[72,96,null],"GRL":[98,null,null],"GRD":[68,null,null],"GLP":[68,null,null],"GUM":[88,null,null],"GTM":[28,69,82],"GIN":[null,30,40],"GNB":[3,41,64],"GUY":[78,null,86],"HTI":[12,59,68],"HND":[38,80,88],"HKG":[58,null,null],"HUN":[96,null,null],"ISL":[98,null,null],"IND":[18,61,78],"IDN":[18,90,96],"IRN":[12,82,89],"IRQ":[12,74,84],"IRL":[98,null,null],"IMN":[98,null,null],"ISR":[92,null,null],"ITA":[88,98,99],"JAM":[72,80,null],"JPN":[98,null,null],"JOR":[18,91,94],"KAZ":[null,100,null],"KEN":[22,82,null],"KIR":[92,null,99],"KWT":[18,93,96],"KGZ":[null,99,null],"LAO":[18,73,76],"WB_LAC":[null,90,95],"LVA":[null,100,null],"LBN":[48,null,92],"LSO":[52,86,90],"LBR":[8,null,null],"LBY":[8,null,null],"LIE":[98,null,null],"LTU":[null,100,null],"LUX":[96,null,null],"MAC":[58,91,97],"MDG":[32,71,75],"MWI":[8,64,70],"MYS":[38,89,96],"MDV":[72,96,98],"MLI":[null,24,36],"MLT":[58,92,null],"MHL":[null,null,96],"MTQ":[72,null,null],"MRT":[null,51,60],"MUS":[52,84,94],"MEX":[62,92,96],"MDA":[null,97,99],"MCO":[96,null,null],"MNG":[58,98,99],"MNE":[null,98,99],"MAR":[12,52,64],"MOZ":[3,48,62],"MMR":[58,90,94],"NAM":[null,85,88],"NRU":[72,null,97],"NPL":[3,49,69],"NLD":[98,null,null],"ANT":[72,null,null],"NCL":[38,96,null],"NZL":[98,null,null],"NIC":[38,78,87],"NER":[null,29,36],"NGA":[12,55,70],"NIU":[92,null,99],"NFK":[88,null,null],"WB_NA":[null,99,99],"MKD":[null,96,null],"NOR":[98,null,null],"OMN":[3,66,97],"PAK":[18,50,59],"PLW":[null,null,100],"PSE":[null,92,98],"PAN":[68,92,96],"PNG":[8,57,87],"PRY":[68,null,95],"PER":[48,88,94],"PHL":[62,93,98],"POL":[92,null,null],"PRT":[58,null,null],"PRI":[72,null,92],"QAT":[8,89,99],"REU":[38,null,null],"ROU":[78,97,99],"RUS":[null,99,100],"RWA":[8,65,79],"SHN":[98,97,null],"SPM":[92,null,null],"WSM":[88,null,98],"SMR":[88,null,100],"STP":[18,85,87],"SAU":[3,83,98],"SEN":[3,39,50],"SRB":[null,96,99],"SYC":[38,92,null],"SLE":[8,35,44],"SGP":[48,93,98],"SLB":[8,77,null],"SOM":[null,null,54],"ZAF":[42,82,91],"WB_SA":[null,62,78],"KOR":[38,null,null],"ESP":[82,98,100],"LKA":[62,91,93],"WB_SSA":[null,59,69],"SDN":[8,61,null],"SUR":[72,90,null],"SWE":[98,null,null],"CHE":[98,null,null],"SYR":[28,81,94],"TJK":[null,97,null],"TZA":[8,69,78],"THA":[52,94,91],"TGO":[8,53,73],"TKL":[96,null,100],"TON":[92,99,99],"TTO":[78,null,null],"TUN":[18,74,86],"TUR":[32,88,97],"TKM":[null,99,100],"TUV":[null,null,100],"UGA":[28,68,77],"UKR":[null,99,null],"ARE":[null,90,99],"GBR":[98,null,null],"USA":[96,null,null],"VIR":[88,null,null],"URY":[82,97,99],"UZB":[null,99,100],"VUT":[32,74,88],"VEN":[52,94,97],"VNM":[18,90,96],"WLF":[null,null,99],"YEM":[3,null,null],"ZMB":[22,69,72],"ZWE":[22,null,93]};
const ECART = {"AFG":[83,44,2022],"AGO":[88,73,2023],"CMR":[88,76,2018],"CAF":[65,37,2019],"TCD":[56,33,2019],"CIV":[76,58,2021],"COD":[88,68,2023],"DJI":[85,75,2017],"GIN":[70,43,2018],"MLI":[57,43,2024],"MOZ":[78,65,2022],"NER":[64,45,2022],"PAK":[79,67,2021],"SLE":[78,68,2019],"SOM":[76,65,2022]};

module.exports = function (ctx) {
  const { d3, cadre, M, WM, HM, OUT, FEAT, esc } = ctx;

  /* ---- outils de dessin (taille des textes : fs, en unités de la scène) ---- */
  function outils(C, nom, fs) {
    const mk = "fl6-" + nom;
    const defs = "<defs><marker id='" + mk + "' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker>" +
      "<marker id='" + mk + "b' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--acier)'/></marker></defs>";
    const st = (k) => " style='font-size:" + (fs * (k || 1)).toFixed(1) + "px'";
    const r0 = fs * 0.55;
    /* point seul (sans étiquette) */
    const pt = (k, ll, o = {}) => { const [x, y] = C.P(ll); return "<circle data-k='" + k + "' cx='" + x + "' cy='" + y + "' r='" + (o.r || r0).toFixed(1) + "' class='" + (o.cl || "pt-a") + "'/>"; };
    /* étiquette seule */
    const lb = (k, ll, s, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -fs * 0.8 : a === "middle" ? 0 : fs * 0.8;
      return "<text data-k='" + k + "' x='" + Math.round(x + dx + (o.dx || 0)) + "' y='" + Math.round(y + fs * 0.35 + (o.dy || 0)) + "' text-anchor='" + a + "' class='" + (o.cl || "lbl") + "'" + st(o.t) + ">" + esc(s) + "</text>";
    };
    /* point + étiquette dans un même groupe */
    const point = (k, ll, s, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -fs * 0.8 : a === "middle" ? 0 : fs * 0.8;
      return "<g data-k='" + k + "'><circle cx='" + x + "' cy='" + y + "' r='" + (o.r || r0).toFixed(1) + "' class='" + (o.cl || "pt-a") + "'/>" +
        (s ? "<text x='" + Math.round(x + dx + (o.dx || 0)) + "' y='" + Math.round(y + fs * 0.35 + (o.dy || 0)) + "' text-anchor='" + a + "' class='" + (o.lc || "lbl") + "'" + st(o.t) + ">" + esc(s) + "</text>" : "") + "</g>";
    };
    /* flèche courbe a → b ; o.b : bleue ; o.c : courbure ; o.tir : pointillés */
    const fleche = (k, a, b, o = {}) => {
      const [x1, y1] = C.P(a), [x2, y2] = C.P(b), mx = (x1 + x2) / 2, my = (y1 + y2) / 2, dx = x2 - x1, dy = y2 - y1, c = o.c === undefined ? 0.2 : o.c;
      const cx = Math.round(mx - dy * c), cy = Math.round(my + dx * c);
      return "<path data-k='" + k + "' class='trace' pathLength='1' d='M" + x1 + "," + y1 + "Q" + cx + "," + cy + " " + x2 + "," + y2 + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") + "' stroke-width='" + (o.w || fs * 0.2).toFixed(1) + "' stroke-linecap='round'" + (o.tir ? " stroke-dasharray='" + o.tir + "'" : "") + (o.sans ? "" : " marker-end='url(#" + mk + (o.b ? "b" : "") + ")'") + "/>";
    };
    /* encadré de texte (titre de bloc, chiffre) */
    const cartouche = (k, x, y, lignes, o = {}) => {
      const h = fs * 1.35, w = o.w || Math.max(...lignes.map(l => l.length)) * fs * 0.56 + fs;
      let s = "<g data-k='" + k + "'><rect x='" + Math.round(x) + "' y='" + Math.round(y) + "' width='" + Math.round(w) + "' height='" + Math.round(h * lignes.length + fs * 0.6) + "' rx='" + Math.round(fs * 0.3) + "' fill='var(--papier)' stroke='" + (o.rouge ? "var(--rouge)" : "var(--encre)") + "' stroke-width='" + (fs * 0.09).toFixed(1) + "' opacity='.95'/>";
      lignes.forEach((l, i) => { s += "<text x='" + Math.round(x + fs * 0.5) + "' y='" + Math.round(y + fs * 0.3 + h * (i + 0.8)) + "' class='" + (i === 0 && o.titre ? "lbl-f" : "lbl") + "'" + st(i === 0 && o.titre ? 1.05 : 0.95) + ">" + esc(l) + "</text>"; });
      return s + "</g>";
    };
    /* point (clé k) + étiquette séparée (clé k + "L"), pour n'afficher l'étiquette qu'à certaines étapes */
    const PL = (k, ll, s, o = {}) => pt(k, ll, o) + lb(k + "L", ll, s, Object.assign({}, o, { cl: o.lc }));
    return { defs, pt, lb, point, fleche, cartouche, st, PL };
  }
  /* Simplification des fonds régionaux. Correctif : quand d3 découpe un pays au bord du cadre, l'anneau se termine
     par son premier point ; la simplification de cartes.js (segment de longueur nulle) l'effaçait entièrement
     (États-Unis et Canada disparaissaient). On retire ce point en double avant de simplifier. */
  function dp(pts, tol) {
    if (pts.length < 3) return pts;
    const keep = new Uint8Array(pts.length); keep[0] = keep[pts.length - 1] = 1;
    const st = [[0, pts.length - 1]];
    while (st.length) {
      const [a, b] = st.pop(); let md = -1, mi = -1;
      const [x1, y1] = pts[a], [x2, y2] = pts[b], dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy);
      for (let i = a + 1; i < b; i++) {
        const d = L > 1e-6 ? Math.abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / L : Math.hypot(pts[i][0] - x1, pts[i][1] - y1);
        if (d > md) { md = d; mi = i; }
      }
      if (md > tol) { keep[mi] = 1; st.push([a, mi], [mi, b]); }
    }
    return pts.filter((_, i) => keep[i]);
  }
  function simplifier(d, tol, minAire) {
    let out = "";
    for (const ring of (d || "").split("M").filter(Boolean)) {
      const closed = /Z\s*$/.test(ring);
      let pts = ring.replace(/Z\s*$/, "").split("L").map(s => s.split(",").map(Number));
      if (pts.length > 2 && pts[0][0] === pts[pts.length - 1][0] && pts[0][1] === pts[pts.length - 1][1]) pts = pts.slice(0, -1);
      const q = dp(pts, tol);
      let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
      for (const [x, y] of q) { minx = Math.min(minx, x); maxx = Math.max(maxx, x); miny = Math.min(miny, y); maxy = Math.max(maxy, y); }
      if (closed && (maxx - minx) * (maxy - miny) < minAire) continue;
      if (q.length < (closed ? 3 : 2)) continue;
      out += "M" + q.map(([x, y]) => Math.round(x) + "," + Math.round(y)).join("L") + (closed ? "Z" : "");
    }
    return out;
  }
  const vbDe = (C, sw, ne, W, H) => {
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (let i = 0; i <= 20; i++) for (const [lo, la] of [[sw[0] + (ne[0] - sw[0]) * i / 20, sw[1]], [sw[0] + (ne[0] - sw[0]) * i / 20, ne[1]], [sw[0], sw[1] + (ne[1] - sw[1]) * i / 20], [ne[0], sw[1] + (ne[1] - sw[1]) * i / 20]]) {
      const [x, y] = C.P([lo, la]); x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y);
    }
    x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(W, x1); y1 = Math.min(H, y1);
    return [x0, y0, x1 - x0, y1 - y0].map(Math.round);
  };

  /* ================= 1. L'alphabétisation dans le monde (fond du monde) ================= */
  {
    const fs = 17, T = outils(M, "alpha", fs);
    const CL = [[25, "#B3241B", "< 25 %"], [50, "#E07B39", "25-50 %"], [75, "#E3BC4E", "50-75 %"], [90, "#7FB08F", "75-90 %"], [101, "#3E86A8", "≥ 90 %"]];
    /* centre du plus grand morceau de chaque pays (évite la Guyane pour la France, l'Alaska pour les États-Unis) */
    const centre = {};
    for (const f of FEAT) {
      const code = f.properties.ADM0_A3, g = f.geometry;
      let polys = g.type === "Polygon" ? [g.coordinates] : g.type === "MultiPolygon" ? g.coordinates : [];
      if (!polys.length) continue;
      let best = polys[0], ba = -1;
      for (const p of polys) { const a = d3.geoArea({ type: "Polygon", coordinates: p }); if (a > ba && a < 6) { ba = a; best = p; } }
      const c = M.gp.centroid({ type: "Polygon", coordinates: best });
      if (isFinite(c[0])) centre[code] = c.map(Math.round);
    }
    /* une couche = un trait « M x,y h0 » par pays, à bout rond : un point par pays, très léger ; halo dessous */
    const couche = (k, i) => {
      const parC = CL.map(() => ""); let halo = "";
      for (const code in LIT) {
        let v = LIT[code][i];
        if (v === null) for (let j = i - 1; j >= 0; j--) if (LIT[code][j] !== null) { v = LIT[code][j] >= 90 ? LIT[code][j] : null; break; }
        if (v === null || !centre[code]) continue;
        const m = "M" + centre[code][0] + "," + centre[code][1] + "h0";
        halo += m; parC[CL.findIndex(c => v < c[0])] += m;
      }
      return "<g data-k='" + k + "' stroke-linecap='round' fill='none'><path d='" + halo + "' stroke='var(--k-halo)' stroke-width='16'/>" +
        parC.map((d, j) => d ? "<path d='" + d + "' stroke='" + CL[j][1] + "' stroke-width='12.5'/>" : "").join("") + "</g>";
    };
    let ecart = "<g data-k='ecart'>";
    for (const code in ECART) if (centre[code]) ecart += "<circle cx='" + centre[code][0] + "' cy='" + centre[code][1] + "' r='11' fill='none' stroke='var(--rouge)' stroke-width='3'/>";
    ecart += "</g>";
    /* légende en bas à gauche, courbe mondiale en bas à droite */
    const vb = vbDe(M, [-128, -44], [150, 72], WM, HM);
    const lx = vb[0] + 6, ly = vb[1] + vb[3] - 5 * 20 - 34;
    let leg = "<g data-k='leg'><rect x='" + lx + "' y='" + ly + "' width='122' height='" + (5 * 20 + 30) + "' rx='5' fill='var(--papier)' stroke='var(--encre)' stroke-width='1.2' opacity='.95'/>" +
      "<text x='" + (lx + 8) + "' y='" + (ly + 19) + "' class='lbl-f'" + T.st(0.72) + ">Savent lire :</text>";
    CL.forEach((c, i) => { leg += "<circle cx='" + (lx + 16) + "' cy='" + (ly + 36 + i * 20) + "' r='6.5' fill='" + c[1] + "' stroke='var(--k-halo)' stroke-width='1.5'/><text x='" + (lx + 29) + "' y='" + (ly + 41 + i * 20) + "' class='lbl'" + T.st(0.78) + ">" + c[2] + "</text>"; });
    leg += "</g>";
    /* barres du taux mondial (adultes sachant lire) : 1820 12 %, 1900 21 %, 1980 68 %, 2000 81 %, 2024 88 % (Our World in Data) */
    const gx = 588, gy = 300, gw = 200, gh = 96, bw = 26;
    const PTS = [[1820, 12], [1900, 21], [1980, 68], [2000, 81], [2024, 88]];
    const bx = i => gx + 14 + i * 37, by = v => gy + gh - 16 - v / 100 * (gh - 38);
    let cour = "<g data-k='courbe0'><rect x='" + gx + "' y='" + gy + "' width='" + gw + "' height='" + gh + "' rx='5' fill='var(--papier)' stroke='var(--encre)' stroke-width='1.2' opacity='.95'/>" +
      "<text x='" + (gx + 8) + "' y='" + (gy + 15) + "' class='lbl-f'" + T.st(0.66) + ">Monde : adultes sachant lire</text>" +
      "<path d='M" + (gx + 8) + "," + by(0) + "H" + (gx + gw - 8) + "' stroke='var(--encre2)' stroke-width='1'/></g>";
    PTS.forEach(([an, v], i) => {
      cour += "<g data-k='c" + an + "'><rect x='" + bx(i) + "' y='" + by(v).toFixed(1) + "' width='" + bw + "' height='" + (by(0) - by(v)).toFixed(1) + "' fill='var(--rouge)'/>" +
        "<text x='" + (bx(i) + bw / 2) + "' y='" + (by(v) - 3).toFixed(1) + "' text-anchor='middle' class='lbl'" + T.st(0.66) + ">" + v + " %</text>" +
        "<text x='" + (bx(i) + bw / 2) + "' y='" + (gy + gh - 4) + "' text-anchor='middle' class='lbl'" + T.st(0.6) + ">" + an + "</text></g>";
    });
    const s = [
      T.PL("witt", [12.65, 51.87], "Wittenberg 1522", { a: "start", dy: -12 }),
      T.PL("bost", [-71.06, 42.36], "Massachusetts 1647", { a: "end" }),
      T.PL("stock", [18.07, 59.33], "Suède 1686", { a: "start", dy: -6 }),
      T.PL("cyr", [2.06, 48.8], "Saint-Cyr 1686", { a: "end", dy: 4 }),
      T.PL("prusse", [13.4, 52.52], "Prusse 1717", { a: "start", dy: 12 }),
      T.PL("fr1789", [2.35, 48.86], "France : 47 % / 27 %", { a: "end", dy: 8, cl: "pt-b" }),
      T.PL("fr1882", [2.35, 48.86], "France : lois Ferry", { a: "end", dy: 8, cl: "pt-b" }),
      T.PL("tokyo", [139.69, 35.69], "Japon 1872", { a: "end" }),
      T.PL("urss", [37.62, 55.75], "URSS 1919", { a: "start" }),
      T.PL("turq", [32.86, 39.93], "Turquie 1928", { a: "start", dy: 6 }),
      couche("y1950", 0), couche("y2000", 1), couche("y2020", 2),
      T.PL("cuba", [-82.37, 23.11], "Cuba 1961", { a: "end" }),
      T.PL("jomt", [100.87, 12.92], "Jomtien 1990", { a: "start" }),
      ecart,
      T.point("kabul", [69.17, 34.53], "Afghanistan 2022", { a: "end", dy: -12 }),
      T.point("swat", [72.36, 34.77], "Malala 2012", { a: "start", dy: 12 }),
      leg, cour
    ].join("");
    OUT.anims.t6alpha = { w: WM, h: HM, vb, fond: "monde", calques: T.defs + s };
  }

  /* ================= 2 et 3. Atlantique nord : la fission (1938-1939) et la radioactivité (1896-1957) =================
     Une seule scène pour les deux animations (le fond n'est stocké qu'une fois) : préfixe f_ pour la fission, r_ pour la
     radioactivité. Les points restent affichés ; les étiquettes (clé + "L") ne s'affichent qu'à l'étape qui les concerne. */
  {
    const W = 720, H = 360, sw = [-108, 31], ne = [42, 62];
    const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [sw, ne] });
    const C = cadre(proj, W, H, 0.3, 0.5);
    const terre = FEAT.map(f => simplifier(C.gp(f), 0.3, 0.5)).join("");
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/><path d='" + terre + "' class='k-terre'/>";
    const fs = 11, T = outils(C, "atl", fs);
    const L = {
      paris: [2.35, 48.86], berlin: [13.4, 52.52], stock: [18.07, 59.33], kung: [11.98, 57.87], copen: [12.57, 55.68],
      ny: [-74.0, 40.71], wash: [-77.04, 38.9], londres: [-0.13, 51.51], cambr: [0.12, 52.2], manch: [-2.24, 53.48],
      mont: [-73.57, 45.5], vienne: [16.37, 48.21], brux: [4.35, 50.85], rome: [12.5, 41.9], chic: [-87.63, 41.88],
      losal: [-106.3, 35.88], oak: [-84.27, 36.01], moscou: [37.62, 55.75], geneve: [6.14, 46.2], long: [-72.4, 41.0]
    };
    const PL = T.PL;
    /* ---- fission (préfixe f) ---- */
    const f = [
      T.fleche("f_lettre", L.berlin, L.stock, { c: -0.3 }),
      PL("f_berlin", L.berlin, "Berlin", { a: "start", dy: 4 }),
      PL("f_stock", L.stock, "Stockholm", { a: "start" }),
      PL("f_kung", L.kung, "Kungälv", { a: "end", dy: -4 }),
      PL("f_copen", L.copen, "Copenhague", { a: "end", dy: 4 }),
      T.fleche("f_bohr", L.copen, L.ny, { c: 0.16, b: true }),
      PL("f_ny", L.ny, "New York", { a: "start", dy: 2 }),
      PL("f_wash", L.wash, "Washington", { a: "end", dy: 8 }),
      T.fleche("f_w2p", L.wash, L.paris, { c: -0.1, b: true }),
      PL("f_paris", L.paris, "Paris", { a: "end", dy: 8 }),
      PL("f_lond", L.londres, "Londres (Nature)", { a: "end", dy: -4 }),
      T.fleche("f_pub1", L.londres, L.mont, { c: 0.12, b: true, tir: "0.02 0.015" }),
      T.fleche("f_pub2", L.londres, L.rome, { c: 0.25, b: true, tir: "0.02 0.015" }),
      T.fleche("f_pub3", L.londres, L.moscou, { c: -0.15, b: true, tir: "0.02 0.015" }),
      PL("f_mont", L.mont, "Montréal", { a: "end", r: 3 }),
      PL("f_rome", L.rome, "Rome", { a: "start", r: 3 }),
      PL("f_moscou", L.moscou, "Moscou", { a: "end", r: 3, dy: -8 }),
      T.fleche("f_szil", L.ny, L.paris, { c: 0.18 }),
      T.lb("f_secret", [-38, 50.5], "« Gardons le secret ! »", { a: "middle", cl: "lbl-f" }),
      PL("f_long", L.long, "Long Island", { a: "start", dy: -10 }),
      T.fleche("f_ein", L.long, L.wash, { c: -0.4 }),
      T.cartouche("f_sceau", 250, 285, ["1940 : les physiciens alliés", "cessent de publier sur la fission"], { rouge: true, titre: true })
    ];
    /* ---- radioactivité (préfixe r) ---- */
    const r = [
      T.fleche("r_pm", L.paris, L.mont, { c: 0.12, b: true, sans: true }),
      T.fleche("r_vm", L.vienne, L.manch, { c: 0.25, b: true, sans: true }),
      T.fleche("r_bb", L.berlin, L.brux, { c: 0.2, b: true, sans: true }),
      T.fleche("r_mb", L.manch, L.brux, { c: -0.2, b: true, sans: true }),
      T.fleche("r_pb", L.paris, L.brux, { c: 0.25, b: true, sans: true }),
      T.fleche("r_sb", L.stock, L.brux, { c: 0.15, b: true, sans: true }),
      PL("r_paris", L.paris, "Paris : Becquerel", { a: "end", dy: 6 }),
      T.lb("r_pl2", L.paris, "Paris : les Curie", { a: "end", dy: 6 }),
      PL("r_mont", L.mont, "Montréal : Rutherford", { a: "end", dy: -2 }),
      PL("r_stock", L.stock, "Stockholm : prix Nobel", { a: "end", dy: -4 }),
      PL("r_brux", L.brux, "Bruxelles : Solvay", { a: "start", dy: 13 }),
      PL("r_manch", L.manch, "Manchester", { a: "end", dy: -4 }),
      PL("r_vienne", L.vienne, "Vienne", { a: "start", dy: 6 }),
      PL("r_berlin", L.berlin, "Berlin : Hahn, Meitner", { a: "start", dy: -2 }),
      T.lb("r_guerre", [-30, 47], "1914-1918 : la guerre coupe le réseau", { a: "middle", cl: "lbl-f" }),
      PL("r_cambr", L.cambr, "Cambridge", { a: "end", dy: 8 }),
      PL("r_rome", L.rome, "Rome : Fermi", { a: "start" }),
      T.lb("r_p34", L.paris, "Paris : les Joliot-Curie", { a: "end", dy: 8 }),
      T.fleche("r_exil1", L.rome, L.ny, { c: 0.18, b: true }),
      T.fleche("r_exil2", L.berlin, L.stock, { c: -0.3, b: true }),
      T.fleche("r_exil3", L.berlin, L.ny, { c: 0.1, b: true }),
      T.lb("r_exil", [-38, 43.5], "exils vers l'Amérique", { a: "middle", cl: "lbl-f" }),
      T.pt("r_ny", L.ny, { r: 3 }),
      PL("r_losal", L.losal, "Los Alamos", { a: "start" }),
      PL("r_chic", L.chic, "Chicago", { a: "end", dy: -6 }),
      PL("r_oak", L.oak, "Oak Ridge", { a: "start", dy: 6 }),
      T.cartouche("r_manh", 20, 285, ["Projet Manhattan (1942-1945) :", "le secret remplace la publication"], { rouge: true, titre: true }),
      PL("r_moscou", L.moscou, "Moscou", { a: "end", dy: -8 }),
      T.fleche("r_espion", L.losal, L.moscou, { c: -0.3, tir: "0.03 0.02" }),
      T.lb("r_espt", [-45, 61], "espionnage atomique", { a: "middle", cl: "lbl-f" }),
      PL("r_geneve", L.geneve, "Genève : CERN", { a: "end", dy: 10, cl: "pt-b" }),
      T.lb("r_vienne57", L.vienne, "Vienne : AIEA", { dy: 6 })
    ];
    OUT.anims.t6atl = { w: W, h: H, fond, calques: T.defs + f.join("") + r.join("") };
  }

  /* ================= 4. Le renseignement pendant la guerre froide =================
     Points persistants ; étiquettes (clé + "L") affichées seulement aux étapes qui les concernent. */
  {
    const fs = 13, T = outils(M, "rens", fs), PL = T.PL;
    const L = {
      ottawa: [-75.7, 45.42], losal: [-106.3, 35.88], moscou: [37.62, 55.75], langley: [-77.15, 38.95],
      semip: [78.0, 50.4], londres: [-0.13, 51.51], ny: [-74.0, 40.71], berlin: [13.4, 52.52], peshawar: [71.58, 34.0],
      sverd: [60.6, 56.84], havane: [-82.37, 23.11], paris: [2.35, 48.86], helsinki: [24.94, 60.17]
    };
    const s = [
      T.fleche("espion", L.losal, L.moscou, { c: -0.25, tir: "0.03 0.02" }),
      T.fleche("cinq", L.londres, L.moscou, { c: -0.25, tir: "0.03 0.02" }),
      T.fleche("u2", L.peshawar, L.sverd, { c: 0.2, b: true }),
      T.fleche("farewell", L.moscou, L.paris, { c: 0.25, b: true }),
      T.fleche("exfil", L.moscou, L.helsinki, { c: -0.35, b: true }),
      "<path data-k='corona' class='trace' pathLength='1' d='" + M.gp({ type: "LineString", coordinates: [[-150, 14], [-100, 50], [-20, 68], [60, 64], [110, 40], [135, 14]] }) + "' fill='none' stroke='var(--acier)' stroke-width='2.4' stroke-dasharray='7 5'/>",
      T.lb("coronat", [-40, 66], "satellites Corona", { a: "middle", cl: "lbl-f", dy: -6 }),
      PL("ottawa", L.ottawa, "Ottawa : Gouzenko", { a: "end", dy: -6 }),
      PL("losal", L.losal, "Los Alamos", { a: "end", dy: 4 }),
      PL("moscou", L.moscou, "Moscou", { a: "start", dy: -10 }),
      PL("langley", L.langley, "CIA, NSA (Washington)", { a: "end", dy: 10, cl: "pt-b" }),
      T.lb("kgb", L.moscou, "KGB", { a: "start", dy: 8 }),
      PL("semip", L.semip, "Semipalatinsk", { a: "end", dy: 16 }),
      PL("londres", L.londres, "Londres : Fuchs", { a: "end", dy: -8 }),
      PL("ny", L.ny, "New York : les Rosenberg", { a: "start", dy: 10 }),
      PL("berlin", L.berlin, "Berlin : le tunnel", { a: "start", dy: 10, cl: "pt-b" }),
      PL("peshawar", L.peshawar, "Peshawar", { a: "end", dy: 8, cl: "pt-b" }),
      PL("sverd", L.sverd, "Sverdlovsk : U-2 abattu", { a: "start", dy: -8 }),
      PL("havane", L.havane, "Cuba : les missiles", { a: "start", dy: 8 }),
      T.lb("penk", L.moscou, "Penkovski arrêté", { a: "start", dy: 8 }),
      PL("paris", L.paris, "Paris : la DST", { a: "end", dy: 10, cl: "pt-b" }),
      T.lb("gordi", L.londres, "Londres : Gordievski", { a: "end", dy: -8 }),
      T.lb("exfilt", L.helsinki, "Finlande", { a: "end", dy: -10 })
    ].join("");
    OUT.anims.t6rens = { w: WM, h: HM, vb: vbDe(M, [-128, 6], [92, 74], WM, HM), fond: "monde", calques: T.defs + s };
  }

  /* ================= 5. L'Inde : cerveaux, étudiants, technologies ================= */
  {
    const fs = 10, T = outils(M, "inde", fs), PL = T.PL;
    const L = {
      bang: [77.59, 12.97], bombay: [72.88, 19.08], kharag: [87.31, 22.33], madras: [80.27, 13.08], kanpur: [80.33, 26.45], delhi: [77.21, 28.61],
      moscou: [37.62, 55.75], bonn: [7.1, 50.73], londres: [-0.13, 51.51], pokhran: [71.9, 27.1],
      kapus: [45.75, 48.57], golfe: [54.4, 24.5], vienne: [16.37, 48.21],
      /* l'Amérique du Nord est hors cadre : les flèches partent du bord gauche de la carte */
      usa: [-19, 38], ottawa: [-19, 49], sv: [-19, 30], dallas: [-19, 22]
    };
    const vb = vbDe(M, [-21, -10], [136, 64], WM, HM);
    const s = [
      T.fleche("p_urss", L.moscou, L.bombay, { c: 0.15, b: true }),
      T.fleche("p_rfa", L.bonn, L.madras, { c: 0.22, b: true }),
      T.fleche("p_usa", L.usa, L.kanpur, { c: -0.18, b: true }),
      T.fleche("p_uk", L.londres, L.delhi, { c: -0.1, b: true }),
      T.fleche("nuc", L.ottawa, L.bombay, { c: -0.22, b: true }),
      T.fleche("arya", L.kapus, L.bang, { c: 0.2, b: true, tir: "0.03 0.02" }),
      T.fleche("fuite1", L.bang, L.sv, { c: -0.2 }),
      T.fleche("fuite2", L.delhi, L.londres, { c: 0.12 }),
      T.fleche("ti", L.dallas, L.bang, { c: 0.18, b: true }),
      T.fleche("envoi1", L.golfe, L.delhi, { c: -0.3, b: true }),
      T.fleche("envoi2", L.sv, L.bang, { c: 0.25, b: true }),
      T.fleche("accord", L.usa, L.bombay, { c: -0.25, b: true }),
      T.fleche("etud", L.delhi, L.usa, { c: 0.22, w: 6 }),
      PL("iisc", L.bang, "Bangalore", { a: "end", dy: 8 }),
      PL("tifr", L.bombay, "Bombay", { a: "end" }),
      PL("iitk", L.kharag, "Kharagpur", { a: "start", dy: 4 }),
      T.lb("iitt", [62, 4], "les IIT et leurs partenaires", { a: "middle", cl: "lbl-f" }),
      T.lb("p_urssL", L.moscou, "URSS", { a: "start", dy: -8 }),
      T.lb("p_rfaL", L.bonn, "RFA", { a: "start", dy: 14 }),
      T.lb("p_usaL", L.usa, "← États-Unis", { a: "start", dy: -10 }),
      T.lb("p_ukL", L.londres, "Royaume-Uni", { a: "end", dy: -8 }),
      T.lb("nucL", L.ottawa, "← Canada : réacteur CIRUS", { a: "start", dy: -10 }),
      PL("pokhran", L.pokhran, "Pokhran 1974", { a: "end", dy: -6 }),
      T.lb("nsg", [25, 10], "embargo nucléaire (1975)", { a: "middle", cl: "lbl-f" }),
      T.lb("aryat", L.kapus, "lanceur soviétique", { a: "end", dy: -10 }),
      T.lb("fuitet", [-8, 22], "← fuite des cerveaux vers l'Amérique", { a: "start", cl: "lbl-f", dy: 34 }),
      T.lb("tit", L.dallas, "← Texas Instruments (Dallas)", { a: "start", dy: 18 }),
      T.cartouche("envois", vb[0] + 8, vb[1] + vb[3] - 52, ["2024 : 129 Md$ envoyés", "par les Indiens de l'étranger"], { titre: true }),
      PL("vienne", L.vienne, "Vienne 2008", { a: "end", dy: -8, cl: "pt-b" }),
      T.cartouche("etudt", vb[0] + 8, vb[1] + vb[3] - 72, ["2024-2025 : 363 019", "étudiants indiens", "aux États-Unis"], { titre: true, rouge: true }),
      T.lb("chandra", L.madras, "Chandrayaan-3 (2023)", { a: "middle", dy: 30, cl: "lbl-f" })
    ].join("");
    OUT.anims.t6inde = { w: WM, h: HM, vb, fond: "monde", calques: T.defs + s };
  }

  /* ================= 6. Le cyberespace : câbles et attaques ================= */
  {
    const fs = 15, T = outils(M, "cyber", fs), PL = T.PL;
    const L = {
      la: [-118.24, 34.05], geneve: [6.14, 46.2], tallinn: [24.75, 59.44], tbilissi: [44.79, 41.72], natanz: [51.9, 33.72],
      dhahran: [50.1, 26.29], hk: [114.17, 22.32], ftmeade: [-76.77, 39.11], paris: [2.35, 48.86], kiev: [30.52, 50.45],
      londres: [-0.13, 51.51], gotland: [18.5, 57.0], merrouge: [41.5, 15.0]
    };
    /* câbles : tracés schématiques, sans prétention d'exactitude (les routes réelles suivent les fonds marins) */
    const cable = (k, pts) => "<path data-k='" + k + "' class='trace' pathLength='1' d='" + M.gp({ type: "LineString", coordinates: pts }) + "' fill='none' stroke='var(--acier)' stroke-width='2.6' stroke-linecap='round'/>";
    const s = [
      cable("cab", [[-75.98, 36.85], [-45, 42], [-20, 44], [-2.93, 43.26]]),
      cable("cab2", [[-75.98, 36.85], [-45, 44], [-20, 46.5], [-2.0, 46.72]]),
      cable("cab3", [[5.37, 43.3], [12, 37], [20, 34], [32.3, 31.3], [33.5, 27], [38.5, 20], [43.3, 12.6], [55, 13], [72, 8], [80, 5.5], [95, 6], [103.82, 1.35]]),
      cable("cab4", [[-118.24, 34.05], [-150, 30], [-180, 33]]),
      cable("cab5", [[180, 33], [160, 34], [139.69, 35.69]]),
      cable("cab6", [[-2.0, 46.72], [-14, 30], [-19, 15], [-12, 4], [3.38, 6.52], [8, -10], [14, -25], [18.42, -33.92], [30, -36], [42, -25], [45, -12], [48, 5], [52, 12], [43.3, 12.6]]),
      T.fleche("snow", L.ftmeade, L.hk, { c: -0.22, b: true, tir: "0.03 0.02" }),
      T.fleche("notpetya1", L.kiev, [-75, 40], { c: 0.2, tir: "0.03 0.02" }),
      T.fleche("notpetya2", L.kiev, [105, 30], { c: -0.2, tir: "0.03 0.02" }),
      T.cartouche("cabt", 330, 380, ["Environ 570 câbles en service", "≈ 99 % des communications", "intercontinentales"], { titre: true }),
      PL("arpa", L.la, "ARPANET 1969", { a: "start", dy: 8, cl: "pt-b" }),
      PL("cern", L.geneve, "CERN : le Web", { a: "end", dy: 14, cl: "pt-b" }),
      PL("tallinn", L.tallinn, "Estonie 2007", { a: "start", dy: -8 }),
      PL("tbil", L.tbilissi, "Géorgie 2008", { a: "start", dy: 2 }),
      PL("natanz", L.natanz, "Natanz : Stuxnet", { a: "start", dy: 2 }),
      PL("dhahran", L.dhahran, "Saudi Aramco", { a: "end", dy: 10 }),
      PL("hk", L.hk, "Hong Kong : Snowden", { a: "end", dy: 14, cl: "pt-b" }),
      T.lb("ftmL", L.ftmeade, "NSA", { a: "end", dy: -8 }),
      PL("paris", L.paris, "Paris : TV5Monde", { a: "end", dy: -8 }),
      PL("kiev", L.kiev, "Ukraine", { a: "start", dy: 6 }),
      PL("londres", L.londres, "Londres : WannaCry", { a: "end", dy: -10 }),
      T.lb("notpt", [70, 52], "NotPetya se répand", { a: "middle", cl: "lbl-f" }),
      T.lb("viasat", L.kiev, "Viasat, Starlink", { a: "start", dy: 24, cl: "lbl-f" }),
      PL("balt", L.gotland, "Baltique", { a: "end", dy: -10 }),
      PL("mrouge", L.merrouge, "mer Rouge", { a: "end", dy: 14 }),
      T.lb("anssi", L.paris, "ANSSI, COMCYBER, Viginum", { a: "end", dy: 16, cl: "lbl-f" })
    ].join("");
    OUT.anims.t6cyber = { w: WM, h: HM, vb: vbDe(M, [-128, -40], [150, 72], WM, HM), fond: "monde", calques: T.defs + s };
  }

  /* ================= Cartes interactives du dossier ================= */
  const P = (c, ll, n, a, t, d) => { const [x, y] = M.P(ll); return { c, x, y, n, a, t, d }; };
  OUT.cartes.t6savoir = {
    w: WM, h: HM, fond: "monde", deco: M.txt([-100, 40], "ÉTATS-UNIS", { a: "middle" }) + M.txt([103, 33], "CHINE", { a: "middle" }) + M.txt([79, 22], "INDE", { a: "middle" }),
    pts: [
      P("sci", [2.35, 48.86], "Paris", "end", "Paris : Académie des sciences, Institut du radium, UNESCO", "Académie royale des sciences (1666), Journal des sçavans (1665), laboratoire des Curie puis Institut du radium (1914). Siège de l'UNESCO depuis 1958 (organisation créée le 16 novembre 1945)."),
      P("sci", [-0.13, 51.51], "Londres", "end", "Londres : la Royal Society", "Fondée en 1660, elle publie les Philosophical Transactions depuis 1665, la plus ancienne revue scientifique encore publiée. Nature y paraît depuis 1869."),
      P("sci", [6.14, 46.2], "Genève", "start", "Genève : le CERN", "Organisation européenne pour la recherche nucléaire, créée le 29 septembre 1954 par 12 États : un laboratoire commun pour une Europe ruinée. Tim Berners-Lee y propose le Web en mars 1989."),
      P("sci", [16.37, 48.21], "Vienne", "start", "Vienne : l'AIEA", "Agence internationale de l'énergie atomique (1957), issue du discours « Atoms for Peace » d'Eisenhower (8 décembre 1953) : diffuser le nucléaire civil, contrôler le militaire."),
      P("sci", [18.07, 59.33], "Stockholm", "start", "Stockholm : les prix Nobel", "Décernés depuis 1901, ils consacrent la communauté savante internationale : Marie Curie y est récompensée deux fois (physique 1903, chimie 1911)."),
      P("pole", [-122.1, 37.4], "Silicon Valley", "end", "La Silicon Valley (Californie)", "Universités (Stanford, Berkeley), capital-risque et géants du numérique : le modèle du pôle de la société de la connaissance. Beaucoup d'ingénieurs y viennent d'Inde et de Chine."),
      P("pole", [-71.1, 42.36], "Boston", "start", "Boston-Cambridge (Massachusetts)", "Harvard (1636) et le MIT (1861) : premier pôle mondial de recherche universitaire et de biotechnologies."),
      P("pole", [114.06, 22.54], "Shenzhen", "start", "Shenzhen (Chine)", "Zone économique spéciale créée en 1980, devenue capitale de l'électronique et du numérique chinois (Huawei, Tencent). La Chine dépense 2,69 % de son PIB en R&D en 2024 (Bureau national des statistiques)."),
      P("pole", [77.59, 12.97], "Bangalore", "start", "Bangalore (Inde)", "Indian Institute of Science (1909), premier centre de R&D d'une multinationale en Inde (Texas Instruments, 1985), Infosys, ISRO : la « Silicon Valley indienne »."),
      P("pole", [34.78, 32.08], "Tel-Aviv", "start", "Tel-Aviv (Israël)", "Israël consacre 6,3 % de son PIB à la R&D en 2023, record de l'OCDE devant la Corée du Sud (5,0 %)."),
      P("ctrl", [-106.3, 35.88], "Los Alamos", "end", "Los Alamos (Nouveau-Mexique)", "Laboratoire secret du projet Manhattan (1943), dirigé par Oppenheimer : la science devient secret d'État. Klaus Fuchs y transmet des informations à l'URSS."),
      P("ctrl", [116.4, 39.9], "Pékin", "start", "Pékin : le « grand pare-feu »", "La Chine filtre l'Internet mondial (bouclier doré, années 2000) et impose depuis la loi sur la cybersécurité (2017) le stockage des données sur son sol."),
      P("ctrl", [69.17, 34.53], "Kaboul", "start", "Kaboul (Afghanistan)", "Depuis le retour des talibans (15 août 2021), les filles sont exclues de l'enseignement secondaire (mars 2022) puis de l'université (décembre 2022) : le seul pays au monde dans ce cas."),
      P("ctrl", [37.62, 55.75], "Moscou", "start", "Moscou", "Siège du KGB (1954-1991) ; aujourd'hui, la loi sur l'« Internet souverain » (en vigueur le 1er novembre 2019) permet d'isoler le réseau russe.")
    ],
    meta: { t: "Les lieux de la connaissance : produire, partager, contrôler", c: { sci: ["Communauté savante et coopération internationale", "#2D5675"], pole: ["Pôles de la société de la connaissance", "#B07A1E"], ctrl: ["Secret, censure et contrôle du savoir", "#B3241B"] } }
  };
  OUT.cartes.t6cyber = {
    w: WM, h: HM, fond: "monde", deco: M.txt([-100, 40], "ÉTATS-UNIS", { a: "middle" }) + M.txt([95, 63], "RUSSIE", { a: "middle" }) + M.txt([103, 33], "CHINE", { a: "middle" }),
    pts: [
      P("infra", [-75.98, 36.85], "Virginia Beach", "end", "Virginia Beach (États-Unis)", "Point d'atterrissage de MAREA (Microsoft, Meta, Telxius, 2018, vers Bilbao) et de Dunant (Google, 2021, vers la Vendée) : les géants du numérique possèdent désormais leurs propres câbles."),
      P("infra", [5.37, 43.3], "Marseille", "start", "Marseille (France)", "Grand carrefour méditerranéen des câbles vers l'Afrique, le Moyen-Orient et l'Asie, et pôle de centres de données."),
      P("infra", [103.82, 1.35], "Singapour", "end", "Singapour", "Nœud majeur des câbles d'Asie du Sud-Est et de leurs centres de données."),
      P("infra", [-77.5, 39.0], "Virginie du Nord", "start", "Virginie du Nord (États-Unis)", "Plus forte concentration mondiale de centres de données (« Data Center Alley », près d'Ashburn) : le cyberespace a une géographie bien réelle."),
      P("infra", [-118.24, 34.05], "Los Angeles", "end", "Los Angeles", "Le 29 octobre 1969, l'université UCLA envoie le premier message d'ARPANET vers Stanford (SRI) : l'ancêtre d'Internet est un réseau financé par la défense américaine."),
      P("att", [24.75, 59.44], "Tallinn", "start", "Tallinn (Estonie)", "Avril-mai 2007 : cyberattaques massives après le déplacement d'un monument soviétique. L'OTAN installe à Tallinn son centre d'excellence de cyberdéfense (2008)."),
      P("att", [51.9, 33.72], "Natanz", "start", "Natanz (Iran)", "Le virus Stuxnet, découvert en juin 2010 et attribué aux États-Unis et à Israël, sabote les centrifugeuses d'enrichissement de l'uranium : première cyberarme qui détruit du matériel."),
      P("att", [30.52, 50.45], "Kiev", "start", "Kiev (Ukraine)", "23 décembre 2015 : coupure de courant pour environ 230 000 personnes ; 27 juin 2017 : NotPetya ; 24 février 2022 : attaque contre le réseau satellitaire KA-SAT de Viasat, une heure avant l'invasion."),
      P("att", [2.35, 48.86], "Paris", "end", "Paris : TV5Monde", "8-9 avril 2015 : la chaîne est coupée par une attaque attribuée au groupe russe APT28 ; elle frôle la destruction."),
      P("att", [18.5, 57.0], "Baltique", "end", "Mer Baltique", "Novembre et décembre 2024 : des câbles de télécommunications et la liaison électrique Estlink 2 sont endommagés par des ancres de navires ; l'OTAN lance la mission Baltic Sentry (janvier 2025)."),
      P("souv", [-76.77, 39.11], "Fort Meade", "end", "Fort Meade (Maryland) : la NSA", "En juin 2013, Edward Snowden révèle la surveillance mondiale des communications par la NSA (programme PRISM) : choc pour les alliés européens."),
      P("souv", [116.4, 39.9], "Pékin", "start", "Pékin", "Le « grand pare-feu » filtre Internet ; la Chine défend la « souveraineté sur le cyberespace » contre le modèle américain d'un Internet ouvert."),
      P("souv", [4.35, 50.85], "Bruxelles", "start", "Bruxelles : l'Union européenne", "RGPD (25 mai 2018), directive NIS 2 (2022), règlement sur la cyber-résilience (2024), sanctions cyber (première fois le 30 juillet 2020) : l'UE régule plus qu'elle ne combat."),
      P("souv", [2.3, 48.75], "ANSSI", "end", "L'ANSSI et le COMCYBER (France)", "Agence nationale de la sécurité des systèmes d'information (2009) pour la défense ; commandement de la cyberdéfense des armées (2017) pour l'action militaire.")
    ],
    meta: { t: "Le cyberespace : infrastructures, attaques et souveraineté", c: { infra: ["Infrastructures (câbles, données)", "#2D5675"], att: ["Cyberattaques majeures", "#B3241B"], souv: ["Surveillance, contrôle et régulation", "#B07A1E"] } }
  };
};
