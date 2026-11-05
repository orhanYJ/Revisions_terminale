/* Cartes du chapitre G2 (DNL) : routes arctiques (projection azimutale polaire), mer de Chine méridionale
   (Mercator), bases avancées de l'US Navy (surcouche du fond mondial de G1, même projection).
   Usage : node outils/cartes-geo/g2.js ne_50m_admin_0_countries.geojson sortie.json */
const fs = require("fs");
const { d3, outils, sym } = require("./commun.js");
const geo = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const F = geo.features;
const out = {};
const C = { nsr: "#8E2F2A", nwp: "#1c4f7c", tsr: "#5aa596", chn: "#b3402f", ev: "#6b3fa0", base: "#17233F", enc: "#17233F" };

/* ---------- 1. l'Arctique ---------- */
{
  const W = 620, H = 560, LH = 78;
  const proj = d3.geoAzimuthalEqualArea().rotate([-100, -90]).clipAngle(36).fitExtent([[10, 10], [W - 10, H - 10]], { type: "Sphere" });
  // ne garder que le disque au nord de 54° N
  const o = outils(proj, W, H, { grat: d3.geoGraticule().step([30, 10])() });
  const fond = o.fond(F, f => f.properties.ADMIN !== "Antarctica");
  const NSR = [[33, 69.6], [43, 71.5], [58, 70.6], [66, 72.2], [80, 75.8], [104, 77.8], [120, 76.5], [140, 75.5], [160, 70.8], [180, 69.6], [-172, 66.6], [-168.8, 65.8]];
  const NWP = [[-168.8, 65.8], [-166, 68.5], [-156.5, 71.6], [-140, 70.4], [-125, 71.2], [-115, 74.6], [-100, 74.4], [-85, 74.2], [-75, 73.8], [-65, 70.5], [-58, 66], [-52, 62]];
  const TSR = [[-168.8, 65.8], [-172, 72], [-175, 80], [0, 90], [5, 82], [5, 76], [8, 72]];
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += o.ligne(TSR, 'stroke="' + C.tsr + '" stroke-width="3" stroke-dasharray="6 4" stroke-linecap="round"');
    s += o.ligne(NWP, 'stroke="' + C.nwp + '" stroke-width="3.4" stroke-linecap="round"');
    s += o.ligne(NSR, 'stroke="' + C.nsr + '" stroke-width="3.4" stroke-linecap="round"');
    s += o.point([0, 90], 3.5, 'fill="#17233F"') + o.texte([0, 90], 6, -6, FR ? "pôle Nord" : "North Pole", { t: 10, g: 500 });
    const pays = [[[100, 66], FR ? "RUSSIE" : "RUSSIA"], [[-105, 63], "CANADA"], [[-41, 72], FR ? "GROENLAND (Danemark)" : "GREENLAND (Denmark)"], [[-152, 64], FR ? "ALASKA (É.-U.)" : "ALASKA (USA)"], [[16, 66], FR ? "NORVÈGE" : "NORWAY"], [[-18.5, 64.9], FR ? "ISLANDE" : "ICELAND"]];
    pays.forEach(([ll, n]) => { s += o.texte(ll, 0, 0, n, { a: "middle", t: 11, g: 700, c: "#6B6350", ls: 1 }); });
    s += o.texte([150, 76.5], 0, 0, FR ? "Route maritime du Nord" : "Northern Sea Route", { t: 11, c: C.nsr, a: "middle", g: 700 });
    s += o.texte([150, 76.5], 0, 13, FR ? "(passage du Nord-Est)" : "(Northeast Passage)", { t: 10, c: C.nsr, a: "middle", g: 500 });
    s += o.texte([-105, 77.5], 0, 0, FR ? "Passage du Nord-Ouest" : "Northwest Passage", { t: 11, c: C.nwp, a: "middle", g: 700 });
    s += o.texte([-150, 84], 0, 0, FR ? "Route transpolaire" : "Transpolar Sea Route", { t: 11, c: "#2f7a6c", a: "middle", g: 700 });
    s += o.point([33.1, 68.97], 4, 'fill="#8E2F2A" stroke="#fff"') + o.texte([33.1, 68.97], -7, 4, FR ? "Mourmansk (bases russes)" : "Murmansk (Russian bases)", { t: 10, a: "end" });
    s += o.point([-51.7, 64.2], 3.6, 'fill="#17233F" stroke="#fff"') + o.texte([-51.7, 64.2], 7, 4, "Nuuk", { t: 10 });
    s += o.texte([-169, 65.8], 6, 12, FR ? "détroit de Béring" : "Bering Strait", { t: 10, i: true });
    s += o.texte([-90, 71], 0, 0, FR ? "archipel arctique canadien" : "Canadian Arctic archipelago", { t: 9.5, i: true, a: "middle", g: 500 });
    s += o.legende(FR ? "Les routes arctiques" : "The Arctic shipping routes", [
      [sym.ligne(C.nsr, 3.4), FR ? "Route maritime du Nord, le long de la Russie" : "Northern Sea Route, along Russia"],
      [sym.ligne(C.nwp, 3.4), FR ? "Passage du Nord-Ouest (revendiqué par le Canada)" : "Northwest Passage (claimed by Canada)"],
      [sym.ligne(C.tsr, 3, "6 4"), FR ? "Route transpolaire (à venir)" : "Transpolar Sea Route (future)"],
      [sym.rond("#8E2F2A", 4, "#fff"), FR ? "Bases militaires russes" : "Russian military bases"]], LH);
    return s;
  };
  out.arctic = { vb: "0 0 " + W + " " + (H + LH), fond, en: L("en"), fr: L("fr") };
}

/* ---------- 2. la mer de Chine méridionale ---------- */
{
  const W = 560, H = 600, LH = 95;
  const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [[99, 0], [127.5, 27]] });
  proj.clipExtent([[0, 0], [W, H]]);
  const o = outils(proj, W, H, { tol: 0.3, minAire: 0.3, grat: d3.geoGraticule().step([5, 5])() });
  const fond = o.fond(F);
  const NEUF = [[108.3, 18.0], [109.2, 15.5], [109.6, 12.5], [109.8, 10.0], [109.0, 7.5], [110.6, 5.5], [112.3, 3.9], [113.9, 5.7], [115.2, 7.0], [116.3, 8.4], [117.1, 10.2], [118.4, 12.4], [119.1, 15.0], [119.7, 17.8], [120.8, 20.0], [121.8, 21.8]];
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += o.ligne(NEUF, 'stroke="' + C.chn + '" stroke-width="3" stroke-dasharray="14 9" stroke-linecap="round"');
    const iles = [[[112.0, 16.5], FR ? "îles Paracels" : "Paracel Islands", 8, -8, "start"], [[114.3, 10.0], FR ? "îles Spratleys" : "Spratly Islands", -8, -10, "end"],
      [[117.75, 15.15], FR ? "récif de Scarborough" : "Scarborough Shoal", 8, -4, "start"], [[123.5, 25.75], "Senkaku / Diaoyu", -8, -6, "end"]];
    iles.forEach(([ll, n, dx, dy, a]) => { s += o.point(ll, 5, 'fill="none" stroke="#17233F" stroke-width="1.6"') + o.point(ll, 1.8, 'fill="#17233F"') + o.texte(ll, dx, dy, n, { t: 10.5, a }); });
    s += o.point([112.9, 9.55], 4, 'fill="' + C.chn + '" stroke="#fff"') + o.texte([112.9, 9.55], -8, -7, FR ? "récif de Fiery Cross (piste chinoise)" : "Fiery Cross Reef (Chinese airstrip)", { t: 9.5, a: "end", c: C.chn });
    s += o.point([115.0, 9.9], 4.5, 'fill="' + C.ev + '" stroke="#fff"') + o.texte([115.0, 9.9], 0, 18, FR ? "220 navires chinois, mars 2021" : "220 Chinese vessels, March 2021", { t: 9.5, c: C.ev, a: "middle" });
    const pays = [[[112, 24.2], FR ? "CHINE" : "CHINA"], [[106.3, 14.5], "VIETNAM"], [[122.6, 13.6], "PHILIPPINES"], [[116.3, 3.0], FR ? "MALAISIE" : "MALAYSIA"], [[114.8, 4.4], FR ? "BRUNEI" : "BRUNEI"],
      [[121.0, 23.6], FR ? "TAÏWAN" : "TAIWAN"], [[104.9, 12.5], FR ? "CAMBODGE" : "CAMBODIA"], [[101.2, 15.3], FR ? "THAÏLANDE" : "THAILAND"], [[110.0, 1.2], FR ? "INDONÉSIE" : "INDONESIA"], [[109.7, 19.2], "Hainan"]];
    pays.forEach(([ll, n]) => { s += o.texte(ll, 0, 0, n, { a: "middle", t: n === "Hainan" ? 9.5 : 10.5, g: 700, c: "#6B6350", ls: n === "Hainan" ? 0 : .8 }); });
    s += o.texte([118.6, 10.0], 4, 0, "Palawan", { t: 9.5, g: 500, a: "middle", i: true });
    s += o.texte([114, 13.2], 0, 0, FR ? "MER DE CHINE" : "SOUTH CHINA", { t: 11, g: 700, a: "middle", c: "#4c7a93", ls: 1.5 });
    s += o.texte([114, 13.2], 0, 14, FR ? "MÉRIDIONALE" : "SEA", { t: 11, g: 700, a: "middle", c: "#4c7a93", ls: 1.5 });
    s += o.texte([125.5, 21], 0, 0, FR ? "mer de Chine orientale →" : "East China Sea →", { t: 9.5, i: true, a: "middle", g: 500, c: "#4c7a93" });
    s += o.texte([103.5, 3.2], 0, 0, FR ? "détroit de Malacca ↙" : "Strait of Malacca ↙", { t: 9.5, i: true, a: "middle", g: 500, c: "#4c7a93" });
    s += o.legende(FR ? "Les revendications en mer de Chine méridionale" : "Territorial claims in the South China Sea", [
      [sym.ligne(C.chn, 3, "9 6"), FR ? "« Ligne en neuf traits » (tracé approx.)" : "China's “nine-dash line” (approx.)"],
      [(x, y) => '<circle cx="' + x + '" cy="' + y + '" r="5" fill="none" stroke="#17233F" stroke-width="1.6"/>', FR ? "Archipels et récifs disputés" : "Disputed archipelagos and reefs"],
      [sym.rond(C.chn, 4, "#fff"), FR ? "Île artificielle militarisée (Chine)" : "Artificial island militarised by China"],
      [sym.rond(C.ev, 4.5, "#fff"), FR ? "Milice chinoise dans la ZEE philippine" : "Chinese militia in the Philippines' EEZ"],
      [sym.rien(), FR ? "Autres revendications : Vietnam, Philippines," : "Other claimants: Vietnam, the Philippines,"],
      [sym.rien(), FR ? "Malaisie, Brunei, Taïwan (Senkaku : Japon)" : "Malaysia, Brunei, Taiwan (Senkaku: Japan)"]], LH);
    return s;
  };
  out.scs = { vb: "0 0 " + W + " " + (H + LH), fond, en: L("en"), fr: L("fr") };
}

/* ---------- 3. bases avancées de l'US Navy (sur le fond mondial de G1) ---------- */
{
  const W = 900, LAT_N = 76, LAT_S = -50;
  const proj = d3.geoEqualEarth().rotate([-12, 0]).scale(W / 5.4).translate([W / 2, 0]);
  const yN = proj([12, LAT_N])[1], yS = proj([12, LAT_S])[1];
  proj.translate([W / 2, -yN + 4]);
  const H = Math.round(yS - yN + 8), LH = 78;
  const o = outils(proj, W, H);
  const B = [["Pearl Harbor", [-157.95, 21.35], 7, 4, "start"], ["Guantanamo Bay", [-75.1, 19.9], 7, 4, "start"], ["Rota", [-6.35, 36.62], -7, 4, "end"],
    ["Naples", [14.25, 40.85], -6, -6, "end"], ["Sigonella", [14.92, 37.4], -9, 13, "end"], ["Souda Bay", [24.15, 35.5], 7, -3, "start"], ["Bahrain", [50.6, 26.2], 7, -2, "start"],
    ["Djibouti", [43.15, 11.55], -7, 10, "end"], ["Diego Garcia", [72.4, -7.3], 7, 4, "start"], ["Singapore", [103.8, 1.3], 7, 10, "start"], ["Okinawa", [127.7, 26.3], -8, 10, "end"],
    ["Sasebo", [129.7, 33.2], -8, 6, "end"], ["Chinhae", [128.7, 35.1], -8, -9, "end"], ["Yokosuka", [139.7, 35.3], 7, -2, "start"], ["Guam", [144.8, 13.5], 7, 4, "start"]];
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    B.forEach(([n, ll, dx, dy, a]) => {
      const nom = FR ? ({ "Singapore": "Singapour", "Naples": "Naples", "Bahrain": "Bahreïn", "Guantanamo Bay": "Guantánamo" }[n] || n) : n;
      s += o.point(ll, 4.5, 'fill="#B8924F" stroke="#17233F" stroke-width="1.2"') + o.texte(ll, dx, dy, nom, { t: 10 });
    });
    s += o.legende(FR ? "La puissance navale américaine : les bases avancées de l'US Navy" : "American sea power: US Navy forward deployed bases", [
      [sym.rond("#B8924F", 4.5, "#17233F"), FR ? "Base avancée de l'US Navy" : "US Navy forward deployed base"],
      [sym.rien(), FR ? "Source : Council on Foreign Relations (IISS, Département de la Défense)" : "Source: Council on Foreign Relations (IISS, US Department of Defense)"]], LH);
    return s;
  };
  out.bases = { en: L("en"), fr: L("fr") };
}

fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log("arctic", out.arctic.fond.length, "scs", out.scs.fond.length, "bases", out.bases.en.length);
