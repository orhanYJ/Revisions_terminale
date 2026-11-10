/* Scènes de carte et de schéma des vidéos HGGSP : extrait les animations du site (outils/specialites/hggsp/src/,
   constantes ANIMS et CARTES) et construit les cartes propres à une vidéo, puis écrit hggsp/serie/illu-<code>.js
   (window.HG_SCENES), que la page de la vidéo charge après le moteur (type scene de hggsp/serie/moteur.js).

   Usage (depuis la racine du dépôt) :  node outils/serie-hggsp/scenes.js hggsp-t1-intro
   À relancer quand une animation du site ou une carte propre à la vidéo change, puis relancer generer.py (l'empreinte
   du fichier change l'adresse chargée par la page).

   Chaque scène : { titre, w, h, vb, svg (fond + calques ; les éléments animés portent data-k), etapes, source }.
   Les étapes du site (date, titre, montre, cache, accent) servent par défaut ; le script de la vidéo peut en choisir
   une partie (pas=[…]) ou en donner d'autres (etapes=[…]).
   Fond Natural Earth 1:50m (téléchargé une fois dans ~/.cache/hggsp/, comme build.py), d3-geo local
   (dnl/cartes/d3-geo.min.js), même projection Equal Earth que le fond mondial du site (cartes.js). */
const fs = require("fs"), vm = require("vm"), path = require("path"), https = require("https");
const RACINE = path.join(__dirname, "..", "..");
const SRC = path.join(RACINE, "outils", "specialites", "hggsp", "src");
const NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson";

/* ---------- données du site ---------- */
function donneesSite() {
  const ctx = {}; vm.createContext(ctx);
  const fichiers = ["data-commun.js"].concat(fs.readdirSync(SRC).filter(f => /^data-.*\.js$/.test(f) && f !== "data-commun.js").sort());
  for (const f of fichiers) vm.runInContext(fs.readFileSync(path.join(SRC, f), "utf8"), ctx, { filename: f });
  vm.runInContext("this.__ANIMS = ANIMS", ctx);
  return { ANIMS: ctx.__ANIMS, CARTES: JSON.parse(fs.readFileSync(path.join(SRC, "cartes.json"), "utf8")) };
}
function fondSVG(CARTES, f) {
  if (f === "monde") return "<rect width='" + CARTES.monde.w + "' height='" + CARTES.monde.h + "' class='k-mer-f'/><path class='k-grat' d='" + CARTES.monde.grat + "'/><path class='k-terre' d='" + CARTES.monde.terre + "'/>";
  return f || "";
}
/* les tailles de texte sont réglées par le moteur vidéo (lisibles quel que soit le zoom) : on retire celles du site */
function sansTailles(svg) {
  return svg.replace(/font-size:\s*[\d.]+px;?/g, "").replace(/ style='\s*'/g, "").replace(/ style="\s*"/g, "");
}
function sceneDuSite(D, nom) {
  const A = D.ANIMS[nom];
  if (!A) throw new Error("animation inconnue du site : " + nom);
  const sc = typeof A.scene === "string" ? D.CARTES.anims[A.scene.slice(6)] : A.scene;
  /* le fond mondial, commun à plusieurs scènes, n'est écrit qu'une fois (HG_FONDS.monde) */
  return { titre: A.titre, w: sc.w, h: sc.h, vb: sc.vb || [0, 0, sc.w, sc.h], fond: sc.fond === "monde" ? "monde" : undefined,
    svg: sansTailles((sc.fond === "monde" ? "" : fondSVG(D.CARTES, sc.fond)) + (sc.calques || sc.svg || "")),
    etapes: A.etapes.map(e => ({ date: e.date || "", titre: e.titre || "", montre: e.montre || [], cache: e.cache || [], accent: e.accent || [] })),
    source: A.source || "" };
}

/* ---------- outils de carte (repris de outils/specialites/hggsp/cartes.js) ---------- */
function chargerD3() {
  const ctx = {}; ctx.globalThis = ctx;
  vm.runInNewContext(fs.readFileSync(path.join(RACINE, "dnl", "cartes", "d3-geo.min.js"), "utf8"), ctx);
  return ctx.d3;
}
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
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
function cadre(d3, FEAT, proj, W, H, tol, minAire) {
  proj.clipExtent([[0, 0], [W, H]]);
  const gp = d3.geoPath(proj).digits(1);
  const P = ll => proj(ll).map(v => Math.round(v));
  const pays = filtre => FEAT.filter(filtre || (() => true)).map(f => simplifier(gp(f), tol, minAire)).join("");
  const poly = (ring, attrs) => "<path d='" + simplifier(gp({ type: "Polygon", coordinates: [ring] }), 0.3, 0) + "' " + attrs + "/>";
  const point = (k, ll, nom, o = {}) => {
    const [x, y] = P(ll), a = o.a || "start", dx = a === "end" ? -10 : a === "middle" ? 0 : 10;
    return "<g data-k='" + k + "'><circle cx='" + x + "' cy='" + y + "' r='" + (o.r || 6.5) + "' class='" + (o.cl || "pt-a") + "'/>" +
      (nom ? "<text x='" + (x + dx) + "' y='" + (y + 5 + (o.dy || 0)) + "' text-anchor='" + a + "' class='" + (o.lc || "lbl") + "'>" + esc(nom) + "</text>" : "") + "</g>";
  };
  const etiq = (k, ll, s, o = {}) => { const [x, y] = P(ll); return "<text" + (k ? " data-k='" + k + "'" : "") + " x='" + (x + (o.dx || 0)) + "' y='" + (y + (o.dy || 0)) + "' text-anchor='" + (o.a || "middle") + "' class='" + (o.cl || "lbl-f") + "'>" + esc(s) + "</text>"; };
  return { gp, P, pays, poly, point, etiq };
}
function telecharger(url, dest) {
  return new Promise((ok, ko) => {
    https.get(url, r => {
      if (r.statusCode !== 200) { ko(new Error("HTTP " + r.statusCode)); return; }
      const f = fs.createWriteStream(dest); r.pipe(f); f.on("finish", () => f.close(ok));
    }).on("error", ko);
  });
}
async function naturalEarth() {
  const cache = path.join(require("os").homedir(), ".cache", "hggsp"), geo = path.join(cache, "ne50.geojson");
  if (!fs.existsSync(geo)) { fs.mkdirSync(cache, { recursive: true }); console.log("téléchargement de Natural Earth…"); await telecharger(NE, geo); }
  return JSON.parse(fs.readFileSync(geo, "utf8")).features.filter(f => f.properties.ADMIN !== "Antarctica");
}

/* ---------- cartes propres aux vidéos ---------- */
const CARTES_VIDEO = {
  /* Les « dernières frontières » sur le planisphère du site (Equal Earth, même fond mondial) : les lieux du chapitre
     d'introduction du thème 1 */
  frontieres(D, d3, FEAT) {
    const WM = 1000, pm = d3.geoEqualEarth().rotate([-10, 0]);
    pm.fitWidth(WM - 8, { type: "Sphere" }); pm.translate([WM / 2, pm.translate()[1]]);
    const yN = pm([10, 80])[1];
    pm.translate([pm.translate()[0], pm.translate()[1] - yN + 6]);
    const C = cadre(d3, FEAT, pm, WM, D.CARTES.monde.h, 0.55, 2.5);
    const s = [
      C.etiq("", [-35, 30], "OCÉAN ATLANTIQUE", { cl: "k-mer" }), C.etiq("", [-150, 5], "OCÉAN PACIFIQUE", { cl: "k-mer" }), C.etiq("", [80, -30], "OCÉAN INDIEN", { cl: "k-mer" }),
      C.point("mariannes", [142.2, 11.35], "Challenger Deep (1960)", { a: "middle", dy: 26, cl: "pt-b" }),
      C.point("jamaique", [-77.3, 18.2], "Montego Bay (1982)", { a: "start", dy: 16 }),
      C.point("houston", [-95.4, 29.8], "Houston : « la Lune » (1962)", { a: "end", dy: -8, cl: "pt-b" }),
      C.point("canaveral", [-80.6, 28.5], "Cap Canaveral : SpaceX (2015, 2020)", { a: "start", dy: -12 }),
      C.point("arctique", [40, 78], "vers le pôle Nord : drapeau russe (2007)", { a: "middle", dy: 26 }),
      C.point("scs", [114, 12.5], "mer de Chine (2016)", { a: "end", dy: -6 }),
      C.point("lux", [6.1, 49.6], "Luxembourg : loi de 2017", { a: "end", dy: -6, cl: "pt-b" }),
      C.etiq("hm", [-140, -25], "HAUTE MER", { cl: "lbl-f" })
    ].join("");
    return { titre: "Les « dernières frontières » sur la carte", w: WM, h: D.CARTES.monde.h, vb: [0, 0, WM, D.CARTES.monde.h],
      fond: "monde", svg: s, etapes: [], source: "Fond Natural Earth (domaine public). Positions approximatives." };
  },
  /* L'Arctique vu du pôle Nord : la banquise recule, un drapeau sous le pôle (tracés de banquise schématiques) */
  arctique(D, d3, FEAT) {
    const W = 700, H = 700;
    const proj = d3.geoAzimuthalEqualArea().rotate([0, -90, 0]).clipAngle(38).fitExtent([[10, 10], [W - 10, H - 10]], { type: "Sphere" });
    const C = cadre(d3, FEAT, proj, W, H, 0.35, 1.5);
    /* cercles de latitude */
    const cercle = (lat, n = 90) => { const r = []; for (let i = 0; i <= n; i++) r.push([-180 + 360 * i / n, lat]); return r; };
    const grat = [60, 70, 80].map(l => "<path class='k-grat' d='" + simplifier(C.gp({ type: "LineString", coordinates: cercle(l) }), 0.3, 0) + "'/>").join("") +
      [0, 30, 60, 90, 120, 150, 180, -150, -120, -90, -60, -30].map(lo => "<path class='k-grat' d='" + simplifier(C.gp({ type: "LineString", coordinates: [[lo, 52], [lo, 89.9]] }), 0.3, 0) + "'/>").join("");
    /* banquise d'été schématique : un anneau irrégulier autour du pôle, plus étendu autrefois (sens du tracé vérifié :
       un anneau mal orienté désignerait tout le globe sauf la banquise) */
    const banquise = (lat0, amp, graine) => {
      let r = []; for (let i = 0; i <= 72; i++) { const lo = -180 + 5 * i; r.push([lo, lat0 + amp * Math.sin(lo * Math.PI / 60 + graine) + amp * 0.6 * Math.cos(lo * Math.PI / 25 + graine * 2)]); }
      r[r.length - 1] = r[0];
      if (d3.geoArea({ type: "Polygon", coordinates: [r] }) > 2 * Math.PI) r = r.slice().reverse();
      return r;
    };
    const fond = "<rect width='" + W + "' height='" + H + "' class='k-mer-f'/>" + grat + "<path class='k-terre' d='" + C.pays() + "'/>";
    const [px, py] = C.P([0, 90]);
    const s = [
      "<g data-k='glace1'>" + C.poly(banquise(73.5, 2.2, 0.4), "class='glace' fill-opacity='.5'") + "</g>",
      "<g data-k='glace2'>" + C.poly(banquise(79.5, 1.6, 1.3), "class='glace'") + "</g>",
      C.etiq("glace1t", [-150, 73.8], "banquise d'été, autrefois", { cl: "lbl", a: "middle" }),
      C.etiq("glace2t", [30, 82.5], "banquise d'été, aujourd'hui", { cl: "lbl", a: "middle" }),
      C.etiq("", [100, 63], "RUSSIE", { cl: "k-pays" }), C.etiq("", [-105, 62], "CANADA", { cl: "k-pays" }), C.etiq("", [-40, 72], "GROENLAND", { cl: "k-pays" }),
      C.etiq("", [-152, 64], "ALASKA (É.-U.)", { cl: "k-pays" }), C.etiq("", [15, 64], "NORVÈGE", { cl: "k-pays" }),
      C.etiq("", [170, 80], "OCÉAN ARCTIQUE", { cl: "k-mer" }),
      "<g data-k='drapeau'><path d='M" + px + "," + py + "v-46' stroke='var(--encre)' stroke-width='2.5'/>" +
      "<path d='M" + px + "," + (py - 46) + "h30v8h-30z' fill='#fff'/><path d='M" + px + "," + (py - 38) + "h30v8h-30z' fill='#2D5675'/><path d='M" + px + "," + (py - 30) + "h30v8h-30z' fill='#B3241B'/>" +
      "<circle cx='" + px + "' cy='" + py + "' r='6.5' class='pt-a'/></g>",
      C.etiq("drapeaut", [0, 90], "drapeau russe · plus de 4 000 m de fond", { cl: "lbl-f", dy: 36 }),
      C.etiq("pole", [0, 90], "pôle Nord", { cl: "lbl", a: "end", dx: -14, dy: 6 })
    ].join("");
    return { titre: "L'Arctique, un front pionnier", w: W, h: H, vb: [0, 0, W, H], svg: fond + s, etapes: [],
      source: "Fond Natural Earth (domaine public). Étendues de banquise schématiques." };
  }
};

/* ---------- scènes de chaque vidéo ---------- */
/* sources affichées sous les scènes (celles du site renvoient parfois au « cours ») */
const SOURCES = {
  t1alt: "Échelle logarithmique : chaque graduation × 10.",
  mer: "Schéma sans échelle. Convention des Nations unies sur le droit de la mer (1982), traité BBNJ (ONU).",
  scs: "Fond Natural Earth ; ligne en neuf traits tracée de façon approximative."
};
const VIDEOS = {
  "hggsp-t1-intro": { site: ["t1alt", "mer", "scs"], video: ["frontieres", "arctique"] }
};

(async function () {
  const code = process.argv[2];
  if (!VIDEOS[code]) { console.error("Usage : node outils/serie-hggsp/scenes.js <code>  (codes : " + Object.keys(VIDEOS).join(", ") + ")"); process.exit(1); }
  const D = donneesSite(), out = {};
  for (const nom of VIDEOS[code].site) { out[nom] = sceneDuSite(D, nom); if (SOURCES[nom]) out[nom].source = SOURCES[nom]; }
  if (VIDEOS[code].video.length) {
    const d3 = chargerD3(), FEAT = await naturalEarth();
    for (const nom of VIDEOS[code].video) out[nom] = CARTES_VIDEO[nom](D, d3, FEAT);
  }
  const js = "// Généré par outils/serie-hggsp/scenes.js " + code + " : ne pas modifier à la main.\n" +
    "// Scènes du site (outils/specialites/hggsp/src/) et cartes propres à la vidéo, jouées par le type scene du moteur.\n" +
    "window.HG_FONDS = " + JSON.stringify({ monde: fondSVG(D.CARTES, "monde") }) + ";\n" +
    "window.HG_SCENES = " + JSON.stringify(out) + ";\n";
  const dest = path.join(RACINE, "hggsp", "serie", "illu-" + code + ".js");
  fs.writeFileSync(dest, js);
  console.log(path.relative(RACINE, dest), Math.round(js.length / 1024) + " Ko :", Object.keys(out).map(k => k + " (" + out[k].etapes.length + " étapes)").join(", "));
})();
