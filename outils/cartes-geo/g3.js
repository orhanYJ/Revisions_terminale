/* Cartes du chapitre G3 (DNL) : la France, puissance maritime.
   - monde : d'après la carte du cours « La France, une grande puissance maritime » (diapositive 76), fond propre (même projection
     que G1, jusqu'à 56° S) — contrôler (France, puissances concurrentes, bases), sécuriser (route mondiale, axes entre les territoires,
     zones d'approvisionnement), s'approprier (ZEE approchée par des cercles de 200 milles, demandes EXTRAPLAC) ;
   - metro : la France métropolitaine (conique conforme) — grands ports, bases et arsenaux, chantiers, pêche, Scandola ;
   - synth : la carte de synthèse du thème, « Les espaces maritimes dans la mondialisation » (diapositive 81), sur G1_FOND.
   Usage : node outils/cartes-geo/g3.js ne_50m_admin_0_countries.geojson sortie.json */
const fs = require("fs");
const { d3, outils, sym, simplifier, esc } = require("./commun.js");
const geo = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const F = geo.features;
const out = {};
const C = { zee: "#2b8bc0", base: "#8E2F2A", ext: "#B8924F", port: "#17233F", peche: "#2f7a6c", chantier: "#6b3fa0", enj: "#b5652a" };

/* ---------- 1. le monde : d'après la carte « La France, une grande puissance maritime » du cours (diapositive 76) ---------- */
{
  // fond propre (jusqu'à 56° S pour garder Kerguelen et Crozet), même projection que G1
  const W = 900, LAT_N = 75, LAT_S = -56;
  const proj = d3.geoEqualEarth().rotate([-12, 0]).scale(W / 5.4).translate([W / 2, 0]);
  const yN = proj([12, LAT_N])[1], yS = proj([12, LAT_S])[1];
  proj.translate([W / 2, -yN + 4]);
  const H = Math.round(yS - yN + 8), LH = 150;
  proj.clipExtent([[0, 0], [W, H]]);
  const o = outils(proj, W, H);
  const pays = F.filter(f => f.properties.ADMIN !== "Antarctica");
  const fondBase = o.fond(pays);
  // puissances maritimes concurrentes (vert) et France métropolitaine (rouge)
  const RIV = ["United States of America", "United Kingdom", "Russia", "China"];
  const riv = pays.filter(f => RIV.includes(f.properties.ADMIN)).map(f => simplifier(o.gp(f), 0.4, 1.2)).join("");
  const fr = F.find(f => f.properties.ADMIN === "France");
  const metro = { type: "MultiPolygon", coordinates: fr.geometry.coordinates.filter(pl => { const [x, y] = pl[0][0]; return x > -6 && x < 10 && y > 41 && y < 52; }) };
  const fond = fondBase +
    '<path d="' + riv + '" fill="' + "#c4d67d" + '" stroke="#9fb35a" stroke-width=".5" stroke-linejoin="round"/>' +
    '<path d="' + simplifier(o.gp(metro), 0.3, 0.2) + '" fill="#c8372d" stroke="#8E2F2A" stroke-width=".6"/>';
  const R = 200 * 1.852 / 111.32; // 200 milles marins en degrés
  const ILES = [
    [-149.4, -17.6], [-151.7, -16.5], [-139.5, -9.4], [-140.1, -8.9], [-142.0, -16.0], [-145.0, -15.0], [-138.5, -19.0], [-134.9, -23.1], [-149.0, -23.4], [-147.7, -23.9], [-144.3, -27.6],
    [165.5, -21.3], [168.0, -21.5], [163.0, -19.2], [158.7, -19.9], [171.7, -22.3], [-176.2, -13.3], [-178.1, -14.3], [-109.2, 10.3],
    [55.5, -21.1], [45.15, -12.8], [40.4, -22.4], [39.7, -21.5], [42.7, -17.05], [47.3, -11.5], [54.5, -15.9], [69.5, -49.3], [51.8, -46.4], [77.55, -37.8],
    [-61.55, 16.25], [-61.0, 14.65], [-62.95, 17.95], [-52.3, 5.6], [-53.8, 6.0], [-56.3, 46.9]];
  const cercles = ILES.map(c => o.gp(d3.geoCircle().center(c).radius(R).precision(6)())).join("");
  // flèche en coordonnées écran : départ au point ll, direction ang (degrés, 0 = est, 90 = sud), longueur l
  const fleche = (ll, ang, l, c) => {
    const [x, y] = o.P(ll), a = ang * Math.PI / 180, x0 = x + 7 * Math.cos(a), y0 = y + 7 * Math.sin(a), x1 = x + (7 + l) * Math.cos(a), y1 = y + (7 + l) * Math.sin(a);
    const h = 5, b = 3.2, hx = x1 - h * Math.cos(a), hy = y1 - h * Math.sin(a);
    const r = v => Math.round(v * 10) / 10;
    return '<path d="M' + r(x0) + "," + r(y0) + "L" + r(hx) + "," + r(hy) + '" stroke="' + c + '" stroke-width="1.6"/>' +
      '<path d="M' + r(x1) + "," + r(y1) + "L" + r(hx - b * Math.sin(a)) + "," + r(hy + b * Math.cos(a)) + "L" + r(hx + b * Math.sin(a)) + "," + r(hy - b * Math.cos(a)) + 'Z" fill="' + c + '"/>';
  };
  const ROUGE = "#c8372d", ROUTE = "#2b7fb8", AXE = "#7fb6dc";
  // route maritime mondiale (Amérique du Nord – Europe – Suez – Malacca – Asie orientale, et le détour par le Cap)
  const route = [[-74, 39.5], [-60, 41.5], [-40, 42], [-20, 40], [-9, 36.6], [-5.6, 35.95], [0, 37], [10, 37.6], [20, 34.5], [29, 32.6], [32.4, 31.3], [32.6, 29.9], [34.5, 26.5], [38.5, 20.5], [42, 14.5], [43.4, 12.6], [50, 12.4], [60, 11], [72, 7.5], [80, 5.4], [88, 5.8], [95, 6.2], [99, 3.6], [103.6, 1.2], [106, 3], [110, 8], [113, 14], [116, 19], [119.5, 23], [122, 28], [123.5, 31.5]];
  const cap = [[-9, 36.6], [-14, 28], [-18.5, 18], [-19, 8], [-10, -5], [2, -18], [10, -30], [18.5, -36], [28, -35.5], [37, -30], [45, -24], [53, -12], [58, -2], [62, 6], [66, 8.8]];
  const axes = [
    [[-5, 47.3], [-20, 38], [-40, 26], [-55, 18.5], [-60.6, 15.6]],                         // métropole → Antilles
    [[-60.6, 15.6], [-56, 10], [-52.6, 6.3]],                                                  // Antilles → Guyane
    [[-61.2, 14.2], [-72, 12], [-79.6, 9.2], [-90, 3], [-110, -6], [-130, -13], [-146, -17]],  // Antilles → Panama → Polynésie
    [[44, 10.5], [50, 2], [53.5, -9], [55.2, -19.6]],                                          // Djibouti → La Réunion
    [[43.4, 11.4], [44.8, 2], [45, -11.3]],                                                    // Djibouti → Mayotte
    [[50, 11.5], [66, 2], [85, -6], [105, -12], [125, -13], [145, -14], [162, -19.8]],         // Djibouti → Nouvelle-Calédonie
    [[56.5, -22.2], [62, -34], [68.8, -47.6]]];                                                // La Réunion → Kerguelen
  const hach = (id, c) => '<pattern id="' + id + '" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="' + c + '" fill-opacity=".12"/><path d="M0,0V7" stroke="' + c + '" stroke-width="2.4" stroke-opacity=".7"/></pattern>';
  const APPRO = [
    [[-17, 21], [-5, 25], [4, 22.5], [12, 21.5], [15.5, 15], [10, 11], [0, 11.5], [-12, 12.5], [-17, 14.5], [-17, 21]],   // Afrique de l'Ouest et Sahel
    [[37, 28], [44, 31], [48, 29.5], [51, 25], [56, 23.5], [55, 18], [49, 15], [43, 14], [39.5, 20], [37, 28]]];         // péninsule Arabique
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += "<defs>" + hach("g3h-appro-" + lang, ROUGE) + "</defs>";
    APPRO.forEach(r => { s += o.poly(r, 'fill="url(#g3h-appro-' + lang + ')" stroke="' + ROUGE + '" stroke-opacity=".5" stroke-width=".8"'); });
    s += '<g opacity=".55"><path d="' + cercles + '" fill="#f0a93b" stroke="#d98a1c" stroke-width=".6"/></g>';
    axes.forEach(a => { s += o.ligne(a, 'stroke="' + AXE + '" stroke-width="1.5" stroke-linecap="round"'); });
    s += o.ligne(route, 'stroke="' + ROUTE + '" stroke-width="5" stroke-opacity=".9" stroke-linejoin="round"') + o.ligne(route, 'stroke="#fff" stroke-width="2" stroke-linejoin="round"');
    s += o.ligne(cap, 'stroke="' + ROUTE + '" stroke-width="3.2" stroke-opacity=".75" stroke-linejoin="round"') + o.ligne(cap, 'stroke="#fff" stroke-width="1.1" stroke-opacity=".9"');
    // demandes d'extension de la ZEE (programme EXTRAPLAC), d'après la carte du cours
    const EXT = [[[-145, -16], 200, 16], [[-142, -15.5], -30, 16], [[-142, -19], 60, 16], [[-52.6, 5.8], -60, 14], [[-60.8, 16], -80, 13],
      [[165.6, -21], -60, 14], [[166, -22.5], 110, 15], [[167.5, -21.6], 40, 13], [[-176.6, -13.6], -70, 12], [[55.6, -21.3], 10, 14], [[55.4, -21.3], 120, 12],
      [[40.3, -21.8], 130, 13], [[69.6, -49.3], -110, 13], [[69.6, -49.3], 60, 12], [[51.8, -46.4], 190, 13], [[51.9, -46.4], -60, 12], [[77.5, -37.8], -70, 12]];
    EXT.forEach(([ll, a, l]) => { s += fleche(ll, a, l, ROUGE); });
    const terr = [[[-150, -24], FR ? "Polynésie française (40 % de la ZEE)" : "French Polynesia (40% of the EEZ)", -48, 26, "start"],
      [[167, -21.3], FR ? "Nouvelle-Calédonie" : "New Caledonia", 4, 34, "middle"], [[-177, -13.3], FR ? "Wallis-et-Futuna" : "Wallis and Futuna", -10, -4, "end"],
      [[-109.2, 10.3], "Clipperton", 0, -14, "middle"], [[55.5, -21.1], FR ? "La Réunion" : "Réunion", 14, 4, "start"], [[45.15, -12.8], "Mayotte", -8, -2, "end"],
      [[54.5, -15.9], "Tromelin", 10, -4, "start"], [[40.3, -21.6], FR ? "îles Éparses" : "Scattered Islands", -12, 6, "end"],
      [[69.5, -49.3], "Kerguelen", 14, 4, "start"], [[51.8, -46.4], "Crozet", -14, 10, "end"], [[77.55, -37.8], FR ? "Amsterdam, Saint-Paul" : "Amsterdam, Saint-Paul", 12, 4, "start"],
      [[-61.3, 15.5], FR ? "Guadeloupe, Martinique" : "Guadeloupe, Martinique", 12, -6, "start"], [[-63, 18], FR ? "St-Martin, St-Barthélemy" : "St Martin, St Barthélemy", -10, -6, "end"],
      [[-53, 5.8], FR ? "Guyane" : "French Guiana", 10, 16, "start"], [[-56.3, 46.9], FR ? "Saint-Pierre-et-Miquelon" : "Saint-Pierre and Miquelon", -14, -6, "end"]];
    terr.forEach(([ll, n, dx, dy, a]) => { s += o.texte(ll, dx, dy, n, { t: 9.5, a, c: "#8a4b07" }); });
    const bases = [[5.93, 43.1], [-4.49, 48.38], [-1.62, 49.65], [-56.17, 46.78], [-61.07, 14.6], [-52.33, 4.94], [55.45, -20.88], [45.26, -12.78], [166.45, -22.27], [-149.57, -17.53]];
    bases.forEach(ll => { s += o.point(ll, 3.4, 'fill="#17233F" stroke="#fff" stroke-width="1"'); });
    s += o.texte([-1.5, 48.6], -10, -9, "Brest, Cherbourg", { t: 9.5, a: "end", c: "#17233F" }) + o.texte([5.93, 43.1], 8, 10, "Toulon", { t: 9.5, c: "#17233F" });
    [[[43.15, 11.6], "Djibouti", -8, 12, "end"], [[54.4, 24.5], FR ? "Abou Dhabi" : "Abu Dhabi", 8, -5, "start"]].forEach(([ll, n, dx, dy, a]) => {
      s += o.point(ll, 4.4, 'fill="#B8924F" stroke="#17233F" stroke-width="1.2"') + o.texte(ll, dx, dy, n, { t: 10, a, c: "#6d5016" }); });
    [[[-100, 40], FR ? "ÉTATS-UNIS" : "UNITED STATES"], [[95, 62], FR ? "RUSSIE" : "RUSSIA"], [[103, 34], FR ? "CHINE" : "CHINA"]].forEach(([ll, n]) => { s += o.texte(ll, 0, 0, n, { t: 10, a: "middle", c: "#4f5f1c", ls: 1 }); });
    s += o.texte([-3, 56.5], -6, -10, FR ? "ROYAUME-UNI" : "UNITED KINGDOM", { t: 9, a: "end", c: "#4f5f1c", ls: .6 });
    s += o.poly(d3.range(0, 361, 15).map(a => [52 + 9 * Math.cos(a * Math.PI / 180), 9 + 5 * Math.sin(a * Math.PI / 180)]).reverse(), 'fill="none" stroke="#b5652a" stroke-width="1.4" stroke-dasharray="4 3"');
    s += o.texte([60, 4], 6, 6, FR ? "opération Atalanta (piraterie)" : "Operation Atalanta (piracy)", { t: 9.5, i: true, c: "#b5652a" });
    s += o.point([40.5, -10.5], 3.4, 'fill="#b5652a" stroke="#fff"') + o.texte([40.5, -10.5], -7, -3, FR ? "gaz du Mozambique (Total)" : "Mozambique gas (Total)", { t: 9.5, c: "#b5652a", a: "end" });
    s += o.texte([-28, -28], 0, 0, FR ? "OCÉAN ATLANTIQUE" : "ATLANTIC OCEAN", { t: 9.5, a: "middle", c: "#5c8db0", i: true, ls: 1 });
    s += o.texte([88, -28], 0, 0, FR ? "OCÉAN INDIEN" : "INDIAN OCEAN", { t: 9.5, a: "middle", c: "#5c8db0", i: true, ls: 1 });
    s += o.texte([-128, 22], 0, 0, FR ? "OCÉAN PACIFIQUE" : "PACIFIC OCEAN", { t: 9.5, a: "middle", c: "#5c8db0", i: true, ls: 1 });
    // légende en trois colonnes, dans l'ordre de la carte du cours
    const cols = [
      [FR ? "1. Contrôler l'espace maritime mondial" : "1. Controlling the world's maritime space", [
        [(x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" rx="2" fill="#c8372d"/>', FR ? "Territoire français (métropole)" : "French territory (mainland)"],
        [(x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" rx="2" fill="#c4d67d" stroke="#9fb35a"/>', FR ? "Puissances maritimes concurrentes (grande" : "Rival maritime powers (large EEZ"],
        [sym.rien(), FR ? "ZEE et force navale importante)" : "and a strong navy)"],
        [sym.rond("#17233F", 3.4, "#fff"), FR ? "Bases navales de la Marine nationale" : "Naval bases of the French Navy"],
        [sym.rond("#B8924F", 4.4, "#17233F"), FR ? "Bases à l'étranger (projection de puissance)" : "Bases abroad (power projection)"],
        [sym.rien(), FR ? "Océan mondial : zone de patrouille des SNLE" : "World ocean: patrol zone of the SSBNs"]]],
      [FR ? "2. Sécuriser l'espace maritime mondial" : "2. Securing the world's maritime space", [
        [(x, y) => '<path d="M' + (x - 9) + "," + y + "H" + (x + 9) + '" stroke="' + ROUTE + '" stroke-width="5"/><path d="M' + (x - 9) + "," + y + "H" + (x + 9) + '" stroke="#fff" stroke-width="2"/>', FR ? "Route maritime mondiale (et détour par le Cap)" : "World shipping route (and the Cape detour)"],
        [sym.ligne(AXE, 1.6), FR ? "Axes entre les territoires français" : "Routes between French territories"],
        [(x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" fill="url(#g3h-appro-' + lang + ')" stroke="' + ROUGE + '" stroke-opacity=".5"/>', FR ? "Zones d'approvisionnement en matières premières" : "Main raw material supply areas"],
        [sym.ligne("#b5652a", 1.4, "4 3"), FR ? "Autres enjeux : piraterie, gaz" : "Other stakes: piracy, gas"]]],
      [FR ? "3. S'approprier les mers et les océans" : "3. Appropriating the seas and oceans", [
        [sym.zone("#f0a93b", .55), FR ? "ZEE française (cercles de 200 milles)" : "French EEZ (200-nautical-mile circles)"],
        [sym.rien(), FR ? "10,7 millions de km², 62 % dans le Pacifique" : "10.7 million km², 62% in the Pacific"],
        [(x, y) => '<path d="M' + (x - 9) + "," + y + "H" + (x + 4) + '" stroke="' + ROUGE + '" stroke-width="1.6"/><path d="M' + (x + 9) + "," + y + "L" + (x + 3) + "," + (y - 3.4) + "L" + (x + 3) + "," + (y + 3.4) + 'Z" fill="' + ROUGE + '"/>', FR ? "Demandes d'extension (programme EXTRAPLAC)" : "Extension claims (EXTRAPLAC programme)"]]]];
    let lg = '<g><rect x="0" y="' + H + '" width="' + W + '" height="' + LH + '" fill="var(--g1-halo)"/><path d="M0,' + H + "H" + W + '" stroke="var(--g1-front)"/>';
    cols.forEach(([t, lignes], c) => {
      const x0 = 12 + c * 300;
      lg += '<text x="' + x0 + '" y="' + (H + 18) + '" font-size="11" font-weight="700" fill="var(--g1-encre)">' + esc(t) + "</text>";
      lignes.forEach(([sy, tx], i) => { const yy = H + 37 + i * 18; lg += sy(x0 + 9, yy - 4) + '<text x="' + (x0 + 26) + '" y="' + yy + '" font-size="10" fill="var(--g1-encre)">' + esc(tx) + "</text>"; });
    });
    s += lg + "</g>";
    return s;
  };
  out.monde = { vb: "0 0 " + W + " " + (H + LH), fond, en: L("en"), fr: L("fr") };
}

/* ---------- 2. la France métropolitaine ---------- */
{
  const W = 560, H = 560, LH = 96;
  const proj = d3.geoConicConformal().parallels([44, 49]).rotate([-3, 0]).fitExtent([[10, 10], [W - 10, H - 10]], { type: "MultiPoint", coordinates: [[-5.4, 41.1], [10.0, 41.1], [-5.4, 51.3], [10.0, 51.3], [2.3, 51.3], [2.3, 41.1]] });
  proj.clipExtent([[0, 0], [W, H]]);
  const o = outils(proj, W, H, { tol: 0.3, minAire: 0.4, grat: d3.geoGraticule().step([2, 2])() });
  const fond = o.fond(F);
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += o.ligne([[2.4, 51.1], [3.5, 51.4], [4.3, 51.8]], 'stroke="#1c4f7c" stroke-width="2.5" stroke-dasharray="6 4"');
    s += o.texte([4.4, 51.9], 4, -2, FR ? "Northern Range (Anvers, Rotterdam)" : "Northern Range (Antwerp, Rotterdam)", { t: 9.5, i: true, c: "#1c4f7c" });
    const ports = [[[4.9, 43.4], FR ? "Marseille-Fos (53e mondial ; Fos 4XL)" : "Marseille-Fos (53rd in the world; Fos 4XL)", -10, -8, "end", 7], [[0.15, 49.48], FR ? "Le Havre (68e mondial)" : "Le Havre (68th in the world)", 2, 19, "middle", 6],
      [[2.3, 51.04], "Dunkerque", 7, 12, "start", 4.5], [[-2.2, 47.27], "Nantes-Saint-Nazaire", 8, 4, "start", 4.5], [[-0.6, 44.86], "Bordeaux", -8, 4, "end", 3.5], [[1.1, 49.44], "Rouen", 7, 4, "start", 3.5]];
    ports.forEach(([ll, n, dx, dy, a, r]) => { s += o.point(ll, r, 'fill="' + C.port + '" stroke="#fff" stroke-width="1.2"') + o.texte(ll, dx, dy, n, { t: 10, a }); });
    [[[5.93, 43.1], "Toulon", 6, 15, "start"], [[-4.49, 48.38], "Brest", -8, 4, "end"], [[-1.62, 49.65], "Cherbourg", -8, -4, "end"]].forEach(([ll, n, dx, dy, a]) => {
      s += '<g>' + o.point(ll, 6, 'fill="none" stroke="' + C.base + '" stroke-width="2.4"') + o.point(ll, 2.2, 'fill="' + C.base + '"') + "</g>" + o.texte(ll, dx, dy, n, { t: 10.5, a, c: C.base }); });
    s += o.texte([5.93, 43.1], 6, 27, FR ? "porte-avions, SNA" : "aircraft carrier, SSNs", { t: 9, c: C.base, i: true });
    s += o.texte([-2.2, 47.27], 8, 16, FR ? "Chantiers de l'Atlantique (paquebots)" : "Chantiers de l'Atlantique (cruise ships)", { t: 9, c: C.chantier, i: true });
    [[[1.6, 50.73], "Boulogne-sur-Mer", -7, 4, "end"], [[-3.37, 47.75], "Lorient", 6, -4, "start"]].forEach(([ll, n, dx, dy, a]) => { s += o.point(ll, 3.6, 'fill="' + C.peche + '"') + o.texte(ll, dx, dy, n, { t: 9.5, c: C.peche, a }); });
    s += o.point([8.6, 42.37], 4, 'fill="#5aa596" stroke="#fff"') + o.texte([8.6, 42.37], -4, 17, FR ? "réserve de Scandola" : "Scandola reserve", { t: 9.5, a: "end", c: "#2f7a6c" });
    s += o.legende(FR ? "Ports, arsenaux et chantiers de la France métropolitaine" : "Ports, naval bases and shipyards of mainland France", [
      [sym.rond(C.port, 4.5, "#fff"), FR ? "Grands ports de commerce (66 ports en tout)" : "Major commercial ports (66 ports in all)"],
      [(x, y) => '<circle cx="' + x + '" cy="' + y + '" r="5.5" fill="none" stroke="' + C.base + '" stroke-width="2.2"/>', FR ? "Arsenaux et bases navales" : "Naval bases and arsenals"],
      [sym.rond(C.peche, 3.6), FR ? "Grands ports de pêche" : "Leading fishing ports"],
      [sym.rond("#5aa596", 4, "#fff"), FR ? "Espace protégé" : "Protected area"],
      [sym.ligne("#1c4f7c", 2.5, "6 4"), FR ? "Vers la Northern Range, au nord" : "Towards the Northern Range"]], LH);
    return s;
  };
  out.metro = { vb: "0 0 " + W + " " + (H + LH), fond, en: L("en"), fr: L("fr") };
}

/* ---------- 3. synthèse du thème : « Les espaces maritimes dans la mondialisation » (diapositive 81), sur G1_FOND ---------- */
{
  const W = 900, LAT_N = 76, LAT_S = -50;
  const proj = d3.geoEqualEarth().rotate([-12, 0]).scale(W / 5.4).translate([W / 2, 0]);
  const yN = proj([12, LAT_N])[1], yS = proj([12, LAT_S])[1];
  proj.translate([W / 2, -yN + 4]);
  const H = Math.round(yS - yN + 8), LH = 128;
  proj.clipExtent([[0, 0], [W, H]]);
  const o = outils(proj, W, H);
  const AUTO = "#2b7fb8", PECHE = "#7fb59c", ORANGE = "#ef9d2e", PASS = "#d6336c", HYD = "#8a4fb0", PIR = "#5b4636";
  // pays en orange : les cinq premiers États pour le volume de la pêche, d'après la carte du cours
  const TOP5 = ["United States of America", "Peru", "China", "Indonesia", "Russia"];
  const top5 = F.filter(f => TOP5.includes(f.properties.ADMIN)).map(f => simplifier(o.gp(f), 0.4, 1.2)).join("");
  const ell = (c, rx, ry) => d3.range(0, 361, 12).map(a => [c[0] + rx * Math.cos(a * Math.PI / 180), c[1] + ry * Math.sin(a * Math.PI / 180)]).reverse();
  const PECHES = [[[-35, 58], 16, 8], [[0, 62], 10, 5], [[-58, 45], 9, 5], [[-172, 57], 12, 5], [[150, 46], 12, 9], [[-80, -15], 6, 14], [[-60, -46], 7, 6],
    [[-20, 16], 5, 8], [[112, -2], 13, 7], [[64, 14], 8, 6], [[16, -33], 7, 5]];
  const AUTOS = [
    [[-74, 40], [-55, 43], [-30, 47], [-10, 49], [1.5, 50.6], [4, 51.9]],                                                      // Atlantique nord
    [[-6, 36], [0, 37], [10, 37.6], [20, 34.5], [29, 32.6], [32.4, 31.3], [32.6, 29.9], [34.5, 26.5], [38.5, 20.5], [42, 14.5], [43.4, 12.6], [50, 12.4], [60, 11], [72, 7.5], [80, 5.4], [88, 5.8], [95, 6.2], [99, 3.6], [103.6, 1.2], [106, 3], [110, 8], [113, 14], [116, 19], [119.5, 23], [122, 29], [125, 33], [129, 35]],
    [[1.5, 50.6], [-5, 48.5], [-10, 43], [-9.5, 37.5], [-6, 36]],                                                               // Manche – Gibraltar
    [[142, 36], [165, 40], [-170, 43], [-145, 41], [-125, 36], [-118.2, 33.7]],                                               // Pacifique nord
    [[-79.6, 9.2], [-77, 14], [-76, 22], [-77, 30], [-74, 40]]];                                                                 // Panama – côte est
  const ROUTES = [
    [[-6, 36], [-14, 28], [-18.5, 18], [-19, 8], [-10, -5], [2, -18], [10, -30], [18.5, -36], [28, -35.5], [37, -30], [45, -24], [53, -12], [58, -2], [65, 8.5]],
    [[-74, 39], [-60, 25], [-40, 5], [-34, -8], [-40, -25], [-55, -40], [-66, -55]],
    [[-79.6, 9.2], [-82, 0], [-80, -12], [-75, -30], [-75, -48], [-68, -56]],
    [[-118.2, 33.7], [-110, 22], [-95, 14], [-79.6, 9.2]],
    [[104, 1], [110, -6], [118, -9], [125, -12], [135, -15], [150, -25]],
    [[60, 11], [57, 20], [56.3, 26.3], [55, 25]]];
  const ARCT = [
    [[25, 71.5], [45, 73.5], [60, 74.5], [80, 75.4], [100, 75.6], [125, 74.6], [145, 73.5], [165, 70.8], [-172, 67.5], [-169, 65.8], [-170, 60], [-175, 52], [170, 45], [150, 40], [142, 36]],
    [[-58, 70], [-75, 74.2], [-95, 74.6], [-115, 73.5], [-130, 71.5], [-150, 71.6], [-162, 70.5], [-169, 65.8]]];
  const PORTS = [[[4.1, 51.95], "Rotterdam", 6, -4, "start"], [[55.03, 25.0], FR => FR ? "Dubaï" : "Dubai", 6, -4, "start"], [[103.8, 1.27], FR => FR ? "Singapour" : "Singapore", -6, 11, "end"],
    [[121.8, 31.0], FR => FR ? "Shanghai" : "Shanghai", 7, 3, "start"], [[121.9, 29.9], "Ningbo", 7, 11, "start"], [[120.3, 36.07], "Qingdao", 6, 0, "start"], [[129.04, 35.1], FR => FR ? "Pusan" : "Busan", 6, 3, "start"],
    [[117.7, 39.0], "Tianjin", -6, -2, "end"], [[119.6, 39.93], "Qinhuangdao", -6, -7, "end"], [[113.6, 22.8], FR => FR ? "Canton" : "Guangzhou", -6, -2, "end"], [[114.17, 22.3], "Hong Kong", 6, 2, "start"], [[113.9, 22.5], "Shenzhen", -6, 9, "end"]];
  const PASSAGES = [[-79.6, 9.2], [-169, 65.8], [-5.6, 35.95], [32.4, 30.6], [56.3, 26.5], [43.4, 12.6], [100.5, 3], [-66, -56.5], [19, -35.5], [1.5, 51], [40.5, -16]];
  const HYDROS = [[-91, 27.5], [-150, 70.4], [3, 57.5], [40, 71.5], [72, 71], [51, 41], [51, 27], [5.5, 4], [11.5, -7.5], [-40, -24], [143.5, 52.5], [113, 9], [113, 5], [34, 33], [-60, -51], [-52, 47]];
  const PIRATES = [[[5, 3], 7, 5], [[52, 10], 10, 7], [[103, 3], 5, 4], [[-75, 15], 6, 4], [[89, 20], 4, 3]];
  const ETOILES = [[-138, 71.5], [15, 74.5], [114, 13]];
  const etoileXY = (x, y, r) => { let d = "";
    for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * 0.45 : r; d += (i ? "L" : "M") + (Math.round((x + rr * Math.cos(a)) * 10) / 10) + "," + (Math.round((y + rr * Math.sin(a)) * 10) / 10); }
    return '<path d="' + d + 'Z" fill="#d23a24" stroke="#7a1d10" stroke-width=".7"/>'; };
  const etoile = (ll, r) => etoileXY(...o.P(ll), r);
  const triXY = (x, y, c) => '<path d="M' + x + "," + (y - 4.2) + "L" + (x + 4) + "," + (y + 3) + "L" + (x - 4) + "," + (y + 3) + 'Z" fill="' + c + '" stroke="#fff" stroke-width=".7"/>';
  const tri = (ll, c) => triXY(...o.P(ll), c);
  const facade = (pts) => o.ligne(pts, 'stroke="' + AUTO + '" stroke-width="6" stroke-opacity=".35" stroke-linecap="round"') + o.ligne(pts, 'stroke="' + AUTO + '" stroke-width="1.6" stroke-dasharray="2 3"');
  const FACADES = [[[-1.5, 49.6], [2, 51.1], [4.3, 52], [8, 53.6], [10, 54]], [[-77, 35], [-74, 40.5], [-70.5, 42], [-70, 43.5]], [[113, 22.3], [118, 24.5], [121.5, 30.5], [121, 36.5], [119, 39], [126.5, 34.5], [129.5, 35.5], [135, 34.5], [140, 35.5]]];
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += '<path d="' + top5 + '" fill="' + ORANGE + '" fill-opacity=".72" stroke="#c77a12" stroke-width=".5" stroke-linejoin="round"/>';
    PECHES.forEach(([c, rx, ry]) => { s += o.poly(ell(c, rx, ry), 'fill="' + PECHE + '" fill-opacity=".55"'); });
    ROUTES.forEach(r => { s += o.ligne(r, 'stroke="' + AUTO + '" stroke-width="1.8" stroke-opacity=".85" stroke-linejoin="round"'); });
    AUTOS.forEach(r => { s += o.ligne(r, 'stroke="' + AUTO + '" stroke-width="4.6" stroke-opacity=".9" stroke-linejoin="round" stroke-linecap="round"'); });
    ARCT.forEach(r => { s += o.ligne(r, 'stroke="' + AUTO + '" stroke-width="1.8" stroke-dasharray="6 4" stroke-linejoin="round"'); });
    FACADES.forEach(f => { s += facade(f); });
    HYDROS.forEach(ll => { s += o.point(ll, 3.4, 'fill="' + HYD + '" stroke="#fff" stroke-width=".8"'); });
    PIRATES.forEach(([c, rx, ry]) => { s += o.poly(ell(c, rx, ry), 'fill="none" stroke="' + PIR + '" stroke-width="2" stroke-dasharray="1.5 2.5" stroke-linecap="round"'); });
    PASSAGES.forEach(ll => { const [x, y] = o.P(ll); s += '<rect x="' + (x - 4.5) + '" y="' + (y - 2) + '" width="9" height="4" rx="1" fill="' + PASS + '" transform="rotate(-35 ' + x + " " + y + ')"/>'; });
    ETOILES.forEach(ll => { s += etoile(ll, 7); });
    PORTS.forEach(([ll]) => { s += tri(ll, "#17233F"); });
    PORTS.forEach(([ll, n, dx, dy, a]) => { if (["Rotterdam", "Singapore", "Shanghai", "Dubai", "Hong Kong", "Busan"].includes(typeof n === "function" ? n(false) : n)) s += o.texte(ll, dx, dy, typeof n === "function" ? n(FR) : n, { t: 9, a, c: "#17233F" }); });
    s += o.texte([118, 34], -10, -16, FR ? "ports chinois" : "Chinese ports", { t: 8.5, a: "end", c: "#17233F", i: true });
    const boite = (ll, t) => { const [x, y] = o.P(ll), w = t.length * 6.1 + 10;
      return '<rect x="' + (x - w / 2) + '" y="' + (y - 8) + '" width="' + w + '" height="15" fill="#fffdf7" stroke="#17233F" stroke-width="1"/>' + o.texte(ll, 0, 3.6, t, { t: 9, a: "middle", c: "#17233F", ls: .5 }); };
    s += boite([-100, 39], FR ? "ÉTATS-UNIS" : "UNITED STATES") + boite([-12, 57.5], FR ? "ROYAUME-UNI" : "UNITED KINGDOM") + boite([2.4, 46.4], "FRANCE");
    [[[-75, -9], FR ? "PÉROU" : "PERU", "end", -12], [[104, 35], FR ? "CHINE" : "CHINA", "middle", 0], [[118, -3], FR ? "INDONÉSIE" : "INDONESIA", "middle", 18], [[100, 63], FR ? "RUSSIE" : "RUSSIA", "middle", 0]].forEach(([ll, n, a, dx]) => { s += o.texte(ll, dx, 0, n, { t: 9, a, c: "#8a4b07", ls: .5 }); });
    s += o.texte([-35, 72], 0, 0, FR ? "routes arctiques" : "Arctic routes", { t: 9, a: "middle", c: AUTO, i: true });
    // légende en trois colonnes, dans l'ordre de la carte du cours
    const cols = [
      [FR ? "1. Un espace de circulation" : "1. A space of circulation", [
        [sym.ligne(AUTO, 4.6), FR ? "Autoroutes maritimes" : "Maritime highways"],
        [sym.ligne(AUTO, 1.8), FR ? "Routes maritimes" : "Shipping routes"],
        [sym.ligne(AUTO, 1.8, "6 4"), FR ? "Route alternative lors du dégel de la banquise" : "Alternative route as the pack ice melts"],
        [(x, y) => '<path d="M' + (x - 9) + "," + y + "H" + (x + 9) + '" stroke="' + AUTO + '" stroke-width="6" stroke-opacity=".35"/><path d="M' + (x - 9) + "," + y + "H" + (x + 9) + '" stroke="' + AUTO + '" stroke-width="1.6" stroke-dasharray="2 3"/>', FR ? "Façades maritimes" : "Maritime façades"]]],
      [FR ? "2. Des enjeux économiques" : "2. Economic stakes", [
        [sym.zone(PECHE, .55), FR ? "Grandes zones de pêche" : "Major fishing grounds"],
        [sym.zone(ORANGE, .72), FR ? "Les 5 premiers États pour le volume de la pêche" : "The top 5 states by fishing volume"],
        [(x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" fill="#fffdf7" stroke="#17233F"/>', FR ? "Les 3 premiers États par leur domaine maritime" : "The top 3 states by maritime domain"],
        [(x, y) => triXY(x, y, "#17233F"), FR ? "Ports majeurs" : "Major ports"],
        [sym.rond(HYD, 3.4, "#fff"), FR ? "Gisements d'hydrocarbures offshore" : "Offshore oil and gas fields"]]],
      [FR ? "3. Des enjeux stratégiques" : "3. Strategic stakes", [
        [(x, y) => '<rect x="' + (x - 6) + '" y="' + (y - 2) + '" width="12" height="4" rx="1" fill="' + PASS + '"/>', FR ? "Passages maritimes stratégiques" : "Strategic passages (choke points)"],
        [(x, y) => etoileXY(x, y, 6), FR ? "Rivalités entre riverains pour les ressources" : "Coastal state rivalries over resources"],
        [(x, y) => '<ellipse cx="' + x + '" cy="' + y + '" rx="8" ry="5.5" fill="none" stroke="' + PIR + '" stroke-width="2" stroke-dasharray="1.5 2.5" stroke-linecap="round"/>', FR ? "Zones de piraterie" : "Piracy zones"]]]];
    let lg = '<g><rect x="0" y="' + H + '" width="' + W + '" height="' + LH + '" fill="var(--g1-halo)"/><path d="M0,' + H + "H" + W + '" stroke="var(--g1-front)"/>';
    cols.forEach(([t, lignes], c) => {
      const x0 = 12 + c * 300;
      lg += '<text x="' + x0 + '" y="' + (H + 18) + '" font-size="11" font-weight="700" fill="var(--g1-encre)">' + esc(t) + "</text>";
      lignes.forEach(([sy, tx], i) => { const yy = H + 37 + i * 18; lg += sy(x0 + 9, yy - 4) + '<text x="' + (x0 + 26) + '" y="' + yy + '" font-size="10" fill="var(--g1-encre)">' + esc(tx) + "</text>"; });
    });
    s += lg + "</g>";
    return s;
  };
  out.synth = { vb: "0 0 " + W + " " + (H + LH), en: L("en"), fr: L("fr"), h: H };
}

fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log("monde", out.monde.fond.length, out.monde.en.length, "metro", out.metro.fond.length, "synth", out.synth.en.length, "h", out.synth.h);
