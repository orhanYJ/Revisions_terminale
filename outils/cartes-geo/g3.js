/* Cartes du chapitre G3 (DNL) : la France, puissance maritime.
   - monde : surcouche du fond mondial de G1 (même projection) — outre-mer et ZEE approchées par des cercles de 200 milles,
     bases navales, prépositionnement, enjeux (Atalanta, îles Éparses, Mozambique) ;
   - metro : la France métropolitaine (conique conforme) — grands ports, bases et arsenaux, chantiers, pêche, Scandola.
   Usage : node outils/cartes-geo/g3.js ne_50m_admin_0_countries.geojson sortie.json */
const fs = require("fs");
const { d3, outils, sym } = require("./commun.js");
const geo = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const F = geo.features;
const out = {};
const C = { zee: "#2b8bc0", base: "#8E2F2A", ext: "#B8924F", port: "#17233F", peche: "#2f7a6c", chantier: "#6b3fa0", enj: "#b5652a" };

/* ---------- 1. le monde (sur G1_FOND) ---------- */
{
  const W = 900, LAT_N = 76, LAT_S = -50;
  const proj = d3.geoEqualEarth().rotate([-12, 0]).scale(W / 5.4).translate([W / 2, 0]);
  const yN = proj([12, LAT_N])[1], yS = proj([12, LAT_S])[1];
  proj.translate([W / 2, -yN + 4]);
  const H = Math.round(yS - yN + 8), LH = 96;
  const o = outils(proj, W, H);
  const R = 200 * 1.852 / 111.32; // 200 milles marins en degrés
  const ILES = [
    [-149.4, -17.6], [-151.7, -16.5], [-139.5, -9.4], [-140.1, -8.9], [-142.0, -16.0], [-145.0, -15.0], [-138.5, -19.0], [-134.9, -23.1], [-149.0, -23.4], [-147.7, -23.9], [-144.3, -27.6],
    [165.5, -21.3], [168.0, -21.5], [163.0, -19.2], [158.7, -19.9], [171.7, -22.3], [-176.2, -13.3], [-178.1, -14.3], [-109.2, 10.3],
    [55.5, -21.1], [45.15, -12.8], [40.4, -22.4], [39.7, -21.5], [42.7, -17.05], [47.3, -11.5], [54.5, -15.9], [69.5, -49.3], [51.8, -46.4], [77.55, -37.8],
    [-61.55, 16.25], [-61.0, 14.65], [-62.95, 17.95], [-52.3, 5.6], [-53.8, 6.0], [-56.3, 46.9]];
  const cercles = ILES.map(c => o.gp(d3.geoCircle().center(c).radius(R).precision(6)())).join("");
  const L = lang => {
    const FR = lang === "fr"; let s = "";
    s += '<g opacity=".38"><path d="' + cercles + '" fill="' + C.zee + '"/></g>';
    const terr = [[[-149.4, -17.6], FR ? "Polynésie française (40 % de la ZEE)" : "French Polynesia (40% of the EEZ)", -50, 42, "start"],
      [[165.5, -21.3], FR ? "Nouvelle-Calédonie" : "New Caledonia", -6, 30, "end"], [[-176.2, -13.3], FR ? "Wallis-et-Futuna" : "Wallis and Futuna", -8, -14, "end"],
      [[-109.2, 10.3], "Clipperton", 0, -14, "middle"], [[55.5, -21.1], FR ? "La Réunion" : "Réunion", 10, 4, "start"], [[45.15, -12.8], "Mayotte", 8, -6, "start"],
      [[42.7, -17.05], FR ? "îles Éparses" : "Scattered Islands", -26, 4, "end"], [[69.5, -49.3], FR ? "Terres australes (Kerguelen…)" : "French Southern Lands (Kerguelen…)", 8, -10, "start"],
      [[-61.3, 15.5], FR ? "Antilles" : "French Antilles", 14, 4, "start"], [[-53, 5.8], FR ? "Guyane" : "French Guiana", 8, 16, "start"], [[-56.3, 46.9], FR ? "Saint-Pierre-et-Miquelon" : "Saint-Pierre and Miquelon", -10, -10, "end"]];
    terr.forEach(([ll, n, dx, dy, a]) => { s += o.texte(ll, dx, dy, n, { t: 10, a, c: "#1c4f7c" }); });
    const bases = [[[5.93, 43.1], "Toulon"], [[-4.49, 48.38], "Brest"], [[-1.62, 49.65], "Cherbourg"], [[-61.07, 14.6], "Fort-de-France"], [[-52.33, 4.94], "Cayenne"],
      [[55.45, -20.88], ""], [[166.45, -22.27], "Nouméa"], [[-149.57, -17.53], "Papeete"]];
    bases.forEach(([ll, n]) => { s += o.point(ll, 3.6, 'fill="' + C.base + '" stroke="#fff" stroke-width="1"'); });
    s += o.texte([166.45, -22.27], -6, 12, "Nouméa", { t: 9.5, a: "end", c: C.base });
    s += o.texte([-149.57, -17.53], 6, -6, "Papeete", { t: 9.5, c: C.base });
    s += o.texte([0, 47], 6, -6, FR ? "Brest, Cherbourg, Toulon" : "Brest, Cherbourg, Toulon", { t: 9.5, c: C.base });
    [[[43.15, 11.6], "Djibouti", -7, 4, "end"], [[54.4, 24.5], FR ? "Abou Dhabi" : "Abu Dhabi", 7, -4, "start"]].forEach(([ll, n, dx, dy, a]) => {
      s += o.point(ll, 4.2, 'fill="' + C.ext + '" stroke="#17233F" stroke-width="1.1"') + o.texte(ll, dx, dy, n, { t: 10, a, c: "#7a5a1e" }); });
    s += o.poly(d3.range(0, 361, 15).map(a => [52 + 9 * Math.cos(a * Math.PI / 180), 9 + 5 * Math.sin(a * Math.PI / 180)]).reverse(), 'fill="none" stroke="' + C.enj + '" stroke-width="1.4" stroke-dasharray="4 3"');
    s += o.texte([60, 5], 6, 4, FR ? "opération Atalanta (piraterie)" : "Operation Atalanta (piracy)", { t: 9.5, i: true, c: C.enj });
    s += o.point([40.5, -10.5], 3.6, 'fill="' + C.enj + '"') + o.texte([40.5, -10.5], -6, -4, FR ? "gaz du Mozambique (Total)" : "Mozambique gas (Total)", { t: 9.5, c: C.enj, a: "end" });
    s += o.legende(FR ? "La France, une présence sur tous les océans" : "France, present on every ocean", [
      [sym.zone(C.zee, .45), FR ? "ZEE française, approchée (cercles de 200 milles)" : "French EEZ, approximated (200-nautical-mile circles)"],
      [sym.rien(), FR ? "10,7 millions de km², dont 62 % dans le Pacifique" : "10.7 million km², 62% of it in the Pacific"],
      [sym.rond(C.base, 3.6, "#fff"), FR ? "Bases navales (métropole et outre-mer)" : "Naval bases (mainland and overseas)"],
      [sym.rond(C.ext, 4.2, "#17233F"), FR ? "Bases à l'étranger : projection de puissance" : "Bases abroad: power projection"],
      [sym.ligne(C.enj, 1.4, "4 3"), FR ? "Enjeux : piraterie, énergie" : "Stakes: piracy, energy"]], LH);
    return s;
  };
  out.monde = { en: L("en"), fr: L("fr"), vb: "0 0 " + W + " " + (H + LH) };
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

fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log("monde", out.monde.en.length, "metro", out.metro.fond.length);
