/* Outils communs aux cartes de géographie DNL (G2…) : d3-geo local, simplification, dessin bilingue.
   (g1.js porte sa propre copie de ces outils, écrite avant ce module.) */
const fs = require("fs"), vm = require("vm"), path = require("path");
const ctx = {}; ctx.globalThis = ctx;
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "../../dnl/cartes/d3-geo.min.js"), "utf8"), ctx);
const d3 = ctx.d3;

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
function simplifier(d, tol = 0.4, minAire = 1.2) {
  let out = "";
  for (const ring of (d || "").split("M").filter(Boolean)) {
    const closed = /Z\s*$/.test(ring);
    const pts = ring.replace(/Z\s*$/, "").split("L").map(s => s.split(",").map(Number));
    const q = dp(pts, tol);
    let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
    for (const [x, y] of q) { minx = Math.min(minx, x); maxx = Math.max(maxx, x); miny = Math.min(miny, y); maxy = Math.max(maxy, y); }
    if (closed && (maxx - minx) * (maxy - miny) < minAire) continue;
    if (q.length < (closed ? 3 : 2)) continue;
    out += "M" + q.map(([x, y]) => (Math.round(x * 10) / 10) + "," + (Math.round(y * 10) / 10)).join("L") + (closed ? "Z" : "");
  }
  return out;
}
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");

function outils(proj, W, H, opt = {}) {
  const gp = d3.geoPath(proj).digits(1);
  const P = ll => proj(ll).map(v => Math.round(v * 10) / 10);
  const tol = opt.tol || 0.4;
  return {
    gp, P,
    fond(features, filtre) {
      const pays = features.filter(filtre || (() => true)).map(f => simplifier(gp(f), tol, opt.minAire || 1.2)).join("");
      return '<rect width="' + W + '" height="' + H + '" fill="var(--g1-mer)"/>' +
        (opt.grat ? '<path d="' + simplifier(gp(opt.grat)) + '" fill="none" stroke="var(--g1-grat)" stroke-width=".5"/>' : "") +
        '<path d="' + pays + '" fill="var(--g1-terre)" stroke="var(--g1-front)" stroke-width=".5" stroke-linejoin="round"/>';
    },
    ligne: (coords, attrs) => '<path d="' + simplifier(gp({ type: "LineString", coordinates: coords }), 0.3) + '" fill="none" ' + attrs + "/>",
    poly: (ring, attrs) => '<path d="' + gp({ type: "Polygon", coordinates: [ring] }) + '" ' + attrs + "/>",
    point: (ll, r, attrs) => { const [x, y] = P(ll); return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" ' + attrs + "/>"; },
    texte(ll, dx, dy, s, o = {}) {
      const [x, y] = P(ll);
      return '<text x="' + (x + dx) + '" y="' + (y + dy) + '" font-size="' + (o.t || 10.5) + '" font-weight="' + (o.g || 600) + '"' +
        (o.a ? ' text-anchor="' + o.a + '"' : "") + ' fill="' + (o.c || "var(--g1-encre)") + '"' + (o.i ? ' font-style="italic"' : "") +
        (o.ls ? ' letter-spacing="' + o.ls + '"' : "") +
        ' paint-order="stroke" stroke="var(--g1-halo)" stroke-width="2.6" stroke-linejoin="round">' + esc(s) + "</text>";
    },
    legende(titre, lignes, LH) {
      let s = '<g><rect x="0" y="' + H + '" width="' + W + '" height="' + LH + '" fill="var(--g1-halo)"/><path d="M0,' + H + "H" + W + '" stroke="var(--g1-front)"/>' +
        '<text x="12" y="' + (H + 17) + '" font-size="11.5" font-weight="700" fill="var(--g1-encre)">' + esc(titre) + "</text>";
      const n = Math.ceil(lignes.length / 2);
      lignes.forEach(([sym, t], i) => { const col = Math.floor(i / n), xx = 12 + col * (W / 2), yy = H + 36 + (i % n) * 17;
        s += sym(xx + 9, yy - 4) + '<text x="' + (xx + 26) + '" y="' + yy + '" font-size="10.5" fill="var(--g1-encre)">' + esc(t) + "</text>"; });
      return s + "</g>";
    }
  };
}
const sym = {
  ligne: (c, w, da) => (x, y) => '<path d="M' + (x - 9) + "," + y + "L" + (x + 9) + "," + y + '" stroke="' + c + '" stroke-width="' + w + '"' + (da ? ' stroke-dasharray="' + da + '"' : "") + "/>",
  rond: (c, r, st) => (x, y) => '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + c + '"' + (st ? ' stroke="' + st + '" stroke-width="1"' : "") + "/>",
  zone: (c, op) => (x, y) => '<rect x="' + (x - 9) + '" y="' + (y - 6) + '" width="18" height="12" rx="3" fill="' + c + '" fill-opacity="' + (op || .35) + '" stroke="' + c + '"/>',
  losange: c => (x, y) => '<path d="M' + x + "," + (y - 5) + "L" + (x + 5) + "," + y + "L" + x + "," + (y + 5) + "L" + (x - 5) + "," + y + 'Z" fill="' + c + '"/>',
  rien: () => () => ""
};
module.exports = { d3, simplifier, esc, outils, sym };
