/* Cartes du chapitre G1 (DNL) : fond du monde (Natural Earth 1:50m, pays actuels) en projection Equal Earth,
   simplifié (Douglas-Peucker 0,4 px, chemins M/L/Z), et deux surcouches bilingues :
   - routes : la maritimisation de l'économie mondiale (trois centres, routes, ports, choke points) ;
   - choke  : le pétrole et les choke points en 2023 (EIA), attaques et piraterie.
   Usage : node outils/cartes-geo/g1.js ne_50m_admin_0_countries.geojson sortie.json
   La sortie est injectée dans dnl/index.html (G1_FOND, G1_MAPS) par outils/cartes-geo/injecter_g1.py. */
const fs = require("fs"), vm = require("vm"), path = require("path");
const ctx = {}; ctx.globalThis = ctx;
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "../../dnl/cartes/d3-geo.min.js"), "utf8"), ctx);
const d3 = ctx.d3;

const W = 900, LAT_N = 76, LAT_S = -50, TOL = 0.4;
const proj = d3.geoEqualEarth().rotate([-12, 0]).scale(W / 5.4).translate([W / 2, 0]);
// cadrage vertical : de LAT_N à LAT_S au méridien central
const yN = proj([12, LAT_N])[1], yS = proj([12, LAT_S])[1];
proj.translate([W / 2, -yN + 4]);
const H = Math.round(yS - yN + 8);
proj.clipExtent([[0, 0], [W, H]]);
const gp = d3.geoPath(proj);
const P = ll => proj(ll).map(v => Math.round(v * 10) / 10);

// ---- simplification d'un chemin M/L/Z ----
function dp(pts, tol) {
  if (pts.length < 3) return pts;
  const keep = new Uint8Array(pts.length); keep[0] = keep[pts.length - 1] = 1;
  const st = [[0, pts.length - 1]];
  while (st.length) {
    const [a, b] = st.pop(); let md = -1, mi = -1;
    const [x1, y1] = pts[a], [x2, y2] = pts[b], dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy) || 1e-9;
    for (let i = a + 1; i < b; i++) {
      const d = Math.abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / L;
      if (d > md) { md = d; mi = i; }
    }
    if (md > tol) { keep[mi] = 1; st.push([a, mi], [mi, b]); }
  }
  return pts.filter((_, i) => keep[i]);
}
function simplifier(d) {
  let out = "";
  for (const ring of d.split("M").filter(Boolean)) {
    const closed = /Z\s*$/.test(ring);
    const pts = ring.replace(/Z\s*$/, "").split("L").map(s => s.split(",").map(Number));
    let q = dp(pts, TOL);
    let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
    for (const [x, y] of q) { minx = Math.min(minx, x); maxx = Math.max(maxx, x); miny = Math.min(miny, y); maxy = Math.max(maxy, y); }
    if (closed && (maxx - minx) * (maxy - miny) < 1.2) continue; // îlots invisibles à cette échelle
    if (q.length < (closed ? 3 : 2)) continue;
    out += "M" + q.map(([x, y]) => (Math.round(x * 10) / 10) + "," + (Math.round(y * 10) / 10)).join("L") + (closed ? "Z" : "");
  }
  return out;
}

const geo = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const pays = geo.features.filter(f => f.properties.ADMIN !== "Antarctica").map(f => simplifier(gp.digits(1)(f) || ""));
const fond = '<rect width="' + W + '" height="' + H + '" fill="var(--g1-mer)"/>' +
  '<path d="' + simplifier(gp(d3.geoGraticule().step([30, 30])()) || "") + '" fill="none" stroke="var(--g1-grat)" stroke-width=".5"/>' +
  '<path d="' + pays.join("") + '" fill="var(--g1-terre)" stroke="var(--g1-front)" stroke-width=".45" stroke-linejoin="round"/>';

// ---- outils de dessin ----
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const ligne = (coords, attrs) => '<path d="' + simplifier(gp({ type: "LineString", coordinates: coords }) || "") + '" fill="none" ' + attrs + "/>";
function ellipse(lon, lat, rx, ry, attrs) {
  const ring = []; for (let k = 0; k <= 48; k++) { const a = 2 * Math.PI * k / 48; ring.push([lon + rx * Math.cos(a), lat + ry * Math.sin(a)]); }
  return '<path d="' + gp({ type: "Polygon", coordinates: [ring.reverse()] }) + '" ' + attrs + "/>";
}
function texte(ll, dx, dy, s, o = {}) {
  const [x, y] = P(ll);
  return '<text x="' + (x + dx) + '" y="' + (y + dy) + '" font-size="' + (o.t || 10.5) + '" font-weight="' + (o.g || 600) + '"' +
    (o.a ? ' text-anchor="' + o.a + '"' : "") + ' fill="' + (o.c || "var(--g1-encre)") + '"' + (o.i ? ' font-style="italic"' : "") +
    ' paint-order="stroke" stroke="var(--g1-halo)" stroke-width="2.6" stroke-linejoin="round">' + esc(s) + "</text>";
}
const point = (ll, r, attrs) => { const [x, y] = P(ll); return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" ' + attrs + "/>"; };
const LH = 78; // hauteur de la bande de légende, sous la carte
function legende(_x, _y, _w, titre, lignes) {
  const y = H;
  let s = '<g><rect x="0" y="' + y + '" width="' + W + '" height="' + LH + '" fill="var(--g1-halo)"/>' +
    '<path d="M0,' + y + 'H' + W + '" stroke="var(--g1-front)"/>' +
    '<text x="12" y="' + (y + 17) + '" font-size="11.5" font-weight="700" fill="var(--g1-encre)">' + esc(titre) + "</text>";
  const n = Math.ceil(lignes.length / 2);
  lignes.forEach(([sym, t], i) => { const col = Math.floor(i / n), xx = 12 + col * (W / 2), yy = y + 36 + (i % n) * 17;
    s += sym(xx + 9, yy - 4) + '<text x="' + (xx + 26) + '" y="' + yy + '" font-size="10.5" fill="var(--g1-encre)">' + esc(t) + "</text>"; });
  return s + "</g>";
}
const sLigne = (c, w, da) => (x, y) => '<path d="M' + (x - 9) + "," + y + "L" + (x + 9) + "," + y + '" stroke="' + c + '" stroke-width="' + w + '"' + (da ? ' stroke-dasharray="' + da + '"' : "") + "/>";
const sRond = (c, r, st) => (x, y) => '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + c + '"' + (st ? ' stroke="' + st + '" stroke-width="1"' : "") + "/>";
const sZone = c => (x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" rx="5" fill="' + c + '" fill-opacity=".35" stroke="' + c + '"/>';
const sLos = c => (x, y) => '<path d="M' + x + "," + (y - 5) + "L" + (x + 5) + "," + y + "L" + x + "," + (y + 5) + "L" + (x - 5) + "," + y + 'Z" fill="' + c + '"/>';

const C = { route: "#1c4f7c", cap: "#8E2F2A", bri: "#b5652a", centre: "#B8924F", choke: "#8E2F2A", port: "#17233F", oil: "#2b2b2b", pir: "#6b3fa0" };

// ---- routes ----
const ASIE_EUROPE = [[121.8, 30.9], [122.6, 26], [117, 22], [111, 13], [105.5, 2.5], [101.5, 2.6], [98.2, 5.6], [94, 6.2], [81, 5.6], [64, 12.8], [50, 12.6], [43.4, 12.6], [38.8, 20.5], [33.6, 27.8], [32.5, 30.2], [32.3, 31.6], [22, 34.4], [11, 37.6], [-1, 36.4], [-5.6, 35.95], [-11, 36.8], [-11, 43.5], [-6, 48.2], [-2, 49.9], [1.4, 50.9], [3.9, 51.95]];
const CAP = [[81, 5.6], [64, -12], [42, -32], [18.5, -36.2], [5, -22], [-14, 4], [-19, 24], [-13.5, 34.5], [-11, 36.8]];
const PACIFIQUE = [[122.6, 31.2], [142, 34.5], [180, 40], [-150, 38.5], [-118.4, 33.7]];
const ATLANTIQUE = [[-6, 48.2], [-25, 46], [-50, 42], [-73.9, 40.4]];
const PANAMA = [[-73.9, 40.4], [-74.5, 31], [-72.5, 22], [-77, 14], [-79.6, 9.3], [-85, 7], [-105, 15], [-118.4, 33.7]];
const CHANCAY = [[-77.3, -11.6], [-100, -10], [-150, 2], [170, 18], [140, 26], [123, 30.2]];

function routes(L) {
  const FR = L === "fr";
  let s = "";
  s += ellipse(-88, 39.5, 20, 9.5, 'fill="' + C.centre + '" fill-opacity=".2" stroke="' + C.centre + '" stroke-width="1.2" stroke-dasharray="4 3"');
  s += ellipse(6, 49.5, 10, 6.5, 'fill="' + C.centre + '" fill-opacity=".2" stroke="' + C.centre + '" stroke-width="1.2" stroke-dasharray="4 3"');
  s += ellipse(122, 30, 15, 11, 'fill="' + C.centre + '" fill-opacity=".2" stroke="' + C.centre + '" stroke-width="1.2" stroke-dasharray="4 3"');
  s += ligne(CAP, 'stroke="' + C.cap + '" stroke-width="2" stroke-dasharray="5 4" stroke-linecap="round"');
  s += ligne(PANAMA, 'stroke="' + C.route + '" stroke-width="1.6" stroke-linecap="round"');
  s += ligne(ATLANTIQUE, 'stroke="' + C.route + '" stroke-width="2.6" stroke-linecap="round"');
  s += ligne(PACIFIQUE, 'stroke="' + C.route + '" stroke-width="3.4" stroke-linecap="round"');
  s += ligne(ASIE_EUROPE, 'stroke="' + C.route + '" stroke-width="4" stroke-linecap="round"');
  s += ligne(CHANCAY, 'stroke="' + C.bri + '" stroke-width="1.8" stroke-dasharray="2 4" stroke-linecap="round"');
  // centres
  s += texte([-88, 49.5], 0, 0, FR ? "Amérique du Nord" : "North America", { a: "middle", c: "#7a5a1e", t: 11.5, g: 700 });
  s += texte([10, 59.5], 0, 0, FR ? "Europe occidentale" : "Western Europe", { a: "middle", c: "#7a5a1e", t: 11.5, g: 700 });
  s += texte([128, 43.5], 0, 0, FR ? "Asie orientale" : "East Asia", { a: "middle", c: "#7a5a1e", t: 11.5, g: 700 });
  // ports
  const ports = [[[121.5, 31.2], 6.5], [[103.8, 1.3], 5.8], [[121.9, 29.9], 4], [[114.1, 22.4], 4], [[129, 35.1], 3.6], [[4.1, 51.95], 4], [[-118.3, 33.7], 3.4], [[-74, 40.6], 3.2], [[-77.3, -11.6], 3]];
  ports.forEach(([ll, r]) => { s += point(ll, r, 'fill="' + C.port + '" stroke="#fff" stroke-width="1.2"'); });
  s += texte([121.5, 31.2], 9, -4, FR ? "Shanghai — 50 M EVP (2024)" : "Shanghai — 50 M TEU (2024)", { t: 10 });
  s += texte([121.9, 29.9], 8, 9, "Ningbo", { t: 9.5, g: 500 });
  s += texte([129, 35.1], 6, -5, "Busan", { t: 9.5, g: 500 });
  s += texte([114.1, 22.4], -6, 13, FR ? "Shenzhen, Hong Kong, Canton" : "Shenzhen, Hong Kong, Guangzhou", { t: 9.5, g: 500, a: "end" });
  s += texte([103.8, 1.3], 8, 13, FR ? "Singapour — 39 M EVP (2023)" : "Singapore — 39 M TEU (2023)", { t: 10 });
  s += texte([4.1, 51.95], -7, 13, "Rotterdam (Northern Range)", { t: 9.5, g: 500, a: "end" });
  s += texte([-118.3, 33.7], -6, 12, "Los Angeles", { t: 9.5, g: 500, a: "end" });
  s += texte([-74, 40.6], 6, 12, "New York", { t: 9.5, g: 500 });
  s += texte([-77.3, -11.6], -6, 4, "Chancay", { t: 9.5, g: 500, a: "end" });
  // choke points
  const ck = [["Panama", [-79.6, 9.1], -6, 10, "end"], ["Gibraltar", [-5.6, 35.95], -6, 12, "end"], ["Suez", [32.5, 30.2], -6, -6, "end"],
    ["Bab el-Mandeb", [43.4, 12.6], -6, 12, "end"], [FR ? "Ormuz" : "Hormuz", [56.4, 26.6], 6, -4, "start"], ["Malacca", [100.3, 3.4], -7, -5, "end"],
    [FR ? "Cap de Bonne-Espérance" : "Cape of Good Hope", [18.5, -34.4], 6, 13, "start"]];
  ck.forEach(([n, ll, dx, dy, a]) => { s += point(ll, 3.6, 'fill="' + C.choke + '" stroke="#fff" stroke-width="1"'); s += texte(ll, dx, dy, n, { t: 9.5, c: C.choke, a }); });
  s += texte([176, 16], 0, 0, FR ? "Routes de la soie :" : "Belt and Road:", { t: 9.5, c: C.bri, i: true, a: "end" });
  s += texte([176, 16], 0, 12, "Chancay – Shanghai (2024)", { t: 9.5, c: C.bri, i: true, a: "end" });
  s += texte([20, -2], 0, 0, FR ? "détour par le Cap" : "detour round the Cape", { t: 9.5, c: C.cap, i: true, a: "middle" });
  s += texte([20, -2], 0, 12, FR ? "depuis fin 2023" : "since late 2023", { t: 9.5, c: C.cap, i: true, a: "middle" });
  s += legende(8, H - 128, 300, FR ? "La maritimisation de l'économie mondiale" : "The maritimisation of the global economy", [
    [sZone(C.centre), FR ? "Les trois centres de l'économie mondiale" : "The three centres of the global economy"],
    [sLigne(C.route, 3.4), FR ? "Grandes routes maritimes (Asie-Europe en tête)" : "Main shipping routes (Asia–Europe first)"],
    [sLigne(C.cap, 2, "5 4"), FR ? "Détour par le cap de Bonne-Espérance" : "Detour round the Cape of Good Hope"],
    [sRond(C.port, 4.5, "#fff"), FR ? "Grands ports à conteneurs" : "Major container ports"],
    [sRond(C.choke, 3.6, "#fff"), FR ? "Choke points (détroits et canaux)" : "Choke points (straits and canals)"],
    [sLigne(C.bri, 1.8, "2 4"), FR ? "Nouvelle ligne des routes de la soie" : "New Belt and Road line"]]);
  return s;
}

// ---- pétrole et choke points ----
function choke(L) {
  const FR = L === "fr";
  let s = "";
  const GOLFE = [[52, 27.2], [56.4, 26.6], [59, 23.5], [64, 18]];
  s += ligne(GOLFE.concat([[78, 7], [94, 6.2], [98.2, 5.6], [101.5, 2.6], [105.5, 2.5], [111, 13], [117, 22], [122.6, 28.5]]), 'stroke="' + C.oil + '" stroke-width="3" stroke-linecap="round" stroke-opacity=".75"');
  s += ligne([[64, 18], [52, 13.2], [43.4, 12.6], [38.8, 20.5], [33.6, 27.8], [32.5, 30.2], [32.3, 31.6], [22, 34.4], [11, 37.6], [-1, 36.4], [-5.6, 35.95], [-10.5, 38.5], [-9.8, 44], [-5.5, 48.6], [1.4, 50.6]], 'stroke="' + C.oil + '" stroke-width="2.2" stroke-linecap="round" stroke-opacity=".75"');
  s += ligne([[64, 18], [62, -10], [42, -32], [18.5, -36.2], [5, -22], [-14, 4], [-35, 18], [-74, 38]], 'stroke="' + C.oil + '" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round" stroke-opacity=".75"');
  s += ellipse(42.5, 16, 6.5, 5.5, 'fill="' + C.cap + '" fill-opacity=".18" stroke="' + C.cap + '" stroke-width="1"');
  const vols = [["Malacca", [100.3, 3.4], 23.7, -2, -14, "end"], [FR ? "Ormuz" : "Hormuz", [56.4, 26.6], 20.9, 10, -10, "start"], ["Suez", [32.5, 30.2], 8.8, -9, -6, "end"],
    ["Bab el-Mandeb", [43.4, 12.6], 8.6, -4, 17, "end"], [FR ? "Cap de Bonne-Espérance" : "Cape of Good Hope", [18.5, -34.4], 6, 12, 4, "start"],
    [FR ? "Détroits danois" : "Danish Straits", [11.5, 55.6], 4.9, 9, -4, "start"], [FR ? "Détroits turcs" : "Turkish Straits", [29, 41.1], 3.4, 7, -6, "start"], ["Panama", [-79.6, 9.1], 2.1, -7, 4, "end"]];
  vols.forEach(([n, ll, v, dx, dy, a]) => {
    const r = Math.sqrt(v) * 2.6;
    s += point(ll, r, 'fill="#e2b44a" fill-opacity=".8" stroke="#7a5a1e" stroke-width="1"');
    const off = (a === "end" ? -1 : 1) * r;
    s += texte(ll, dx + off, dy, n + " " + (FR ? String(v).replace(".", ",") : v), { t: 10, a });
  });
  const pir = [[[4, 3.5], "Nigeria 42"], [[-1, 4.2], "Ghana 16"], [[106.5, -3.5], FR ? "Indonésie 37" : "Indonesia 37"], [[104.4, 1.7], FR ? "Singapour 28" : "Singapore 28"], [[48.5, 11.6], FR ? "Yémen 18" : "Yemen 18"], [[123, 11], "Philippines 14"]];
  pir.forEach(([ll, t], i) => {
    const [x, y] = P(ll);
    s += '<path d="M' + x + "," + (y - 5) + "L" + (x + 5) + "," + y + "L" + x + "," + (y + 5) + "L" + (x - 5) + "," + y + 'Z" fill="' + C.pir + '" stroke="#fff" stroke-width=".8"/>';
    const pos = [[-7, 12, "end"], [-7, -3, "end"], [6, 14, "start"], [7, 4, "start"], [7, 13, "start"], [7, 4, "start"]][i];
    s += texte(ll, pos[0], pos[1], t, { t: 9.5, c: C.pir, a: pos[2] });
  });
  s += texte([32.5, 30.2], -9, 12, FR ? "Ever Given, mars 2021" : "Ever Given, March 2021", { t: 9.5, c: C.cap, i: true, a: "end" });
  s += texte([35.5, 16.5], 0, -2, FR ? "attaques houthies" : "Houthi attacks", { t: 9.5, c: C.cap, i: true, a: "end" });
  s += texte([35.5, 16.5], 0, 10, FR ? "depuis fin 2023" : "since late 2023", { t: 9.5, c: C.cap, i: true, a: "end" });
  s += legende(8, H - 144, 330, FR ? "Le pétrole et les choke points" : "Oil and the choke points", [
    [sRond("#e2b44a", 6, "#7a5a1e"), FR ? "Pétrole en transit, millions de barils/jour (2023)" : "Oil in transit, million barrels a day (2023)"],
    [sLigne(C.oil, 3), FR ? "Flux de pétrole du Golfe vers l'Asie et l'Europe" : "Oil flows from the Gulf to Asia and Europe"],
    [sLigne(C.oil, 1.6, "5 4"), FR ? "Route du cap de Bonne-Espérance" : "Route round the Cape of Good Hope"],
    [sZone(C.cap), FR ? "Zone d'attaques contre les navires" : "Area of attacks on ships"],
    [sLos(C.pir), FR ? "Piraterie : pays aux incidents les plus nombreux" : "Piracy: countries with the most incidents"],
    [(x, y) => "", FR ? "Sources : EIA (2023), ministère des Armées" : "Sources: EIA (2023), French Ministry of the Armed Forces"]]);
  return s;
}

const out = { vb: "0 0 " + W + " " + (H + LH), fond, maps: { routes: { en: routes("en"), fr: routes("fr") }, choke: { en: choke("en"), fr: choke("fr") } } };
fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log("fond", fond.length, "routes", out.maps.routes.en.length, "choke", out.maps.choke.en.length, "H", H);
