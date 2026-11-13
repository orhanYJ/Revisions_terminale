/* Scènes de carte de la vidéo « Thème 1 · Axe 2 — Enjeux diplomatiques et coopérations » (hggsp-t1-a2).
   Reprend les outils de outils/serie-hggsp/scenes.js (lus dans ce fichier, sans le modifier : d'autres vidéos y ajoutent
   leurs cartes en parallèle) et écrit hggsp/serie/illu-hggsp-t1-a2.js (window.HG_FONDS, window.HG_SCENES), que la page
   de la vidéo charge après le moteur (type scene de hggsp/serie/moteur.js).

   Usage (depuis la racine du dépôt) :  node outils/serie-hggsp/scenes_t1_a2.js
   puis relancer generer.py hggsp_t1_a2 (l'empreinte du fichier change l'adresse chargée par la page).

   Scènes du site : iss (la station s'assemble), mer (la course aux mers), scs (mer de Chine méridionale),
   t1bbnj (le traité BBNJ). Cartes propres à la vidéo, sur le planisphère du site (Equal Earth, fond Natural Earth) :
   espace (partenaires de l'ISS, Chine exclue, deux coalitions lunaires), mers (des règles pour les mers : Islande,
   Montego Bay, Hambourg, Atalanta, La Haye), france (le domaine maritime français, ZEE approchée par des cercles
   de 200 milles), fonds (Clarion-Clipperton, Kingston, Galápagos). Tous les faits viennent du chapitre « t1-a2 » du site. */
const fs = require("fs"), path = require("path");
const RACINE = path.join(__dirname, "..", "..");

/* outils de scenes.js : tout ce qui précède son exécution (la fonction anonyme finale) */
const SRC_SC = fs.readFileSync(path.join(__dirname, "scenes.js"), "utf8");
const corps = SRC_SC.slice(0, SRC_SC.indexOf("(async function () {"));
const O = new Function("require", "__dirname", "process", corps +
  "\nreturn { donneesSite, sceneDuSite, fondSVG, chargerD3, naturalEarth, cadre, simplifier, SOURCES };")(require, __dirname, process);

/* planisphère commun (même cadrage que la carte « frontieres » de la vidéo d'introduction) */
function monde(D, d3, FEAT) {
  const WM = 1000, pm = d3.geoEqualEarth().rotate([-10, 0]);
  pm.fitWidth(WM - 8, { type: "Sphere" }); pm.translate([WM / 2, pm.translate()[1]]);
  const yN = pm([10, 80])[1];
  pm.translate([pm.translate()[0], pm.translate()[1] - yN + 6]);
  const C = O.cadre(d3, FEAT, pm, WM, D.CARTES.monde.h, 0.55, 2.5);
  /* pays (ADMIN de Natural Earth) remplis : k = data-k, fill = couleur du moteur */
  C.paysK = (k, noms, attrs) => "<path data-k='" + k + "' d='" + C.pays(f => noms.includes(f.properties.ADMIN)) + "' " + attrs + "/>";
  /* flèche au crayon gras (tracé qui se dessine) avec sa pointe */
  C.fleche = (k, a, b, courbe, coul) => {
    const [x1, y1] = C.P(a), [x2, y2] = C.P(b), mx = (x1 + x2) / 2, my = (y1 + y2) / 2 - (courbe || 0);
    const ang = Math.atan2(y2 - my, x2 - mx) * 180 / Math.PI;
    return "<g data-k='" + k + "'><path class='trace' pathLength='1' d='M" + x1 + "," + y1 + "Q" + mx + "," + my + " " + x2 + "," + y2 + "' fill='none' stroke='" + (coul || "var(--rouge)") + "' stroke-linecap='round'/>" +
      "<path d='M0,0L-13,-6.5L-13,6.5Z' fill='#b8281b' transform='translate(" + x2 + "," + y2 + ") rotate(" + ang.toFixed(1) + ")'/></g>";
  };
  /* cercles géodésiques réunis dans un seul tracé (zones de 200 milles : 200 × 1,852 km ≈ 3,33° de grand cercle) */
  C.cercles = (k, centres, rayon, attrs) => {
    const d = centres.map(c => O.simplifier(C.gp(d3.geoCircle().center(c).radius(rayon).precision(4)()), 0.3, 0)).join("");
    return "<path data-k='" + k + "' d='" + d + "' " + attrs + "/>";
  };
  C.WM = WM; C.HM = D.CARTES.monde.h;
  return C;
}
const BLEU = "fill='var(--acier)' fill-opacity='.5'", MER = "style='fill:#2d4f86;fill-opacity:.42;stroke:#2d4f86;stroke-width:1.4'", VERT = "fill='var(--ok)'", ROUGE = "class='zone'";
const R200 = 200 * 1.852 / 111.195;   // 200 milles marins en degrés de grand cercle

const CARTES_VIDEO = {
  /* l'espace : partenaires de l'ISS, la Chine exclue, deux coalitions pour la Lune */
  espace(D, d3, FEAT) {
    const C = monde(D, d3, FEAT);
    const s = [
      C.paysK("us", ["United States of America"], BLEU), C.paysK("ru", ["Russia"], BLEU),
      C.paysK("jp", ["Japan"], BLEU), C.paysK("ca", ["Canada"], BLEU),
      C.etiq("ust", [-100, 39], "États-Unis", { cl: "lbl" }),
      C.etiq("freedom", [-100, 30], "« Freedom » (1984)", { cl: "lbl-f" }),
      C.etiq("rut", [95, 62], "Russie", { cl: "lbl" }),
      C.etiq("mir", [95, 53], "Mir (1986-2001) · ralliement en 1993", { cl: "lbl-f" }),
      C.etiq("jpt", [139, 30], "Japon", { cl: "lbl", a: "start", dx: 14 }),
      C.etiq("cat", [-105, 58], "Canada", { cl: "lbl" }),
      C.etiq("esa", [10, 52], "11 États de l'ESA", { cl: "lbl" }),
      C.etiq("a15", [-25, -38], "accord du 29 janvier 1998 : 15 pays", { cl: "lbl-f" }),
      C.paysK("cn", ["China"], ROUGE),
      C.etiq("cnt", [103, 34], "Chine : exclue (2011)", { cl: "lbl-f" }),
      C.etiq("tg", [103, 25], "sa station : Tiangong", { cl: "lbl" }),
      C.fleche("sieges", [-95, 44], [60, 58], 70),
      C.etiq("siegest", [-25, 74], "échange de sièges (juillet 2022)", { cl: "lbl-f" }),
      C.paysK("art", ["United States of America"], VERT), C.paysK("artfr", ["France"], VERT),
      C.etiq("artt", [-100, 30], "accords Artemis (13 octobre 2020)", { cl: "lbl-f" }),
      C.etiq("artfrt", [2, 44], "France (juin 2022)", { cl: "lbl", a: "end", dx: -6 }),
      C.etiq("art70", [-25, -38], "plus de 70 signataires en 2026", { cl: "lbl-f" }),
      C.paysK("ilrs", ["China", "Russia"], ROUGE),
      C.etiq("ilrst", [100, 25], "ILRS : Chine et Russie (mars 2021)", { cl: "lbl-f" })
    ].join("");
    return { titre: "Coopérer dans l'espace", w: C.WM, h: C.HM, vb: [0, 0, C.WM, C.HM], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth (domaine public). L'Europe de l'ESA n'est pas détaillée." };
  },
  /* la mer : des règles pour partager, des juges pour trancher, des marines pour coopérer */
  mers(D, d3, FEAT) {
    const C = monde(D, d3, FEAT);
    const s = [
      C.paysK("isl", ["Iceland"], BLEU), C.paysK("uk", ["United Kingdom"], ROUGE),
      C.etiq("islt", [-19, 72], "Islande : 200 milles (1976)", { cl: "lbl-f" }),
      C.etiq("morue", [-19, 58], "« guerres de la morue » (1958-1976)", { cl: "lbl", a: "end", dx: -6 }),
      C.point("jam", [-77.92, 18.47], "Montego Bay (10 déc. 1982)", { a: "end", dy: 8 }),
      C.etiq("vig", [-77.9, 18.5], "en vigueur le 16 nov. 1994", { cl: "lbl-f", a: "end", dx: -10, dy: 38 }),
      C.point("hamb", [9.99, 53.55], "Hambourg : Tribunal du droit de la mer", { a: "start", dy: -14, cl: "pt-b" }),
      C.cercles("atal", [[50, 11.8], [55, 8]], 6, ROUGE),
      C.etiq("atalt", [52, 2], "Atalanta (déc. 2008)", { cl: "lbl-f", a: "start", dx: 10 }),
      C.paysK("som", ["Somalia"], BLEU),
      C.point("haye", [4.3, 52.08], "La Haye : sentence de 2016", { a: "end", dy: -14 }),
      C.cercles("scsz", [[114, 12.5]], 7, ROUGE),
      C.etiq("scst", [114, 3], "mer de Chine méridionale", { cl: "lbl-f" })
    ].join("");
    return { titre: "Partager les mers", w: C.WM, h: C.HM, vb: [0, 0, C.WM, C.HM], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth (domaine public). Positions approximatives." };
  },
  /* le domaine maritime français : environ 10 millions de km² de ZEE, plus de 90 % outre-mer */
  france(D, d3, FEAT) {
    const C = monde(D, d3, FEAT);
    const met = [[-6.5, 47], [-3.5, 44.5], [8.5, 42.5], [6, 43]];
    const om = {
      pf: [[-149.5, -17.5], [-140, -9], [-145, -16], [-135, -23], [-147.5, -23.5], [-142, -14.5]],
      nc: [[165.5, -21.5], [168, -22.5], [163, -19]], wf: [[-176.2, -13.3]], cl: [[-109.2, 10.3]],
      taaf: [[69.3, -49.3], [51.8, -46.4], [77.5, -38]], ep: [[40.4, -22.4], [42.7, -17.05], [47.3, -11.5], [54.5, -15.9]],
      re: [[55.5, -21.1], [45.15, -12.8]], am: [[-61.5, 16.2], [-61, 14.6], [-52, 6], [-56.3, 46.9]]
    };
    const tous = Object.values(om).flat();
    const s = [
      C.cercles("zmet", met, R200, MER),
      C.etiq("zmett", [2, 50], "Hexagone", { cl: "lbl", a: "end", dx: -12 }),
      C.cercles("zom", tous, R200, MER),
      C.etiq("pft", [-145, -30], "Polynésie française", { cl: "lbl" }),
      C.etiq("nct", [165, -30], "Nouvelle-Calédonie", { cl: "lbl" }),
      C.etiq("taaft", [62, -56], "Terres australes", { cl: "lbl" }),
      C.etiq("ept", [44, -27], "îles Éparses", { cl: "lbl", a: "end", dx: -8 }),
    ].join("");
    return { titre: "Le domaine maritime de la France", w: C.WM, h: C.HM, vb: [0, 0, C.WM, C.HM], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth. ZEE approchées par des cercles de 200 milles (schéma, limites réelles non tracées)." };
  },
  /* les grands fonds et la haute mer : Clarion-Clipperton, Kingston, Galápagos */
  fonds(D, d3, FEAT) {
    const C = monde(D, d3, FEAT);
    /* zone de Clarion-Clipperton : bande schématique entre Hawaï et le Mexique */
    const ccz = [[-158, 13], [-150, 19], [-118, 20], [-112, 16], [-115, 10], [-140, 2], [-157, 4], [-158, 13]];
    const s = [
      C.poly(ccz, "data-k='ccz' class='zone'"),
      C.etiq("cczt", [-150, 30], "Clarion-Clipperton : des nodules", { cl: "lbl-f" }),
      C.point("haw", [-157.8, 21.3], "Hawaï", { a: "end", dy: -4, cl: "pt-b" }),
      C.etiq("mex", [-104, 24], "MEXIQUE", { cl: "k-pays" }),
      C.etiq("ifr", [-137, -1], "contrat français (Ifremer, 2001)", { cl: "lbl" }),
      C.point("kgn", [-76.8, 18], "Kingston : l'AIFM", { a: "start", dy: -10 }),
      C.etiq("us25", [-100, 42], "États-Unis : décret du 24 avril 2025", { cl: "lbl-f" }),
      C.cercles("gal", [[-90.5, -0.6]], R200, MER),
      C.etiq("galt", [-90.5, -9], "ZEE de l'Équateur (Galápagos)", { cl: "lbl" }),
      C.etiq("hm", [-122, -10], "HAUTE MER", { cl: "lbl-f" }),
      C.etiq("calm", [-104, -14], "2020 : des centaines de navires à calmar", { cl: "lbl", a: "end" })
    ].join("");
    return { titre: "Les grands fonds et la haute mer", w: C.WM, h: C.HM, vb: [0, 0, C.WM, C.HM], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth. Zone de Clarion-Clipperton et ZEE tracées de façon schématique." };
  }
};

const SOURCES = Object.assign({}, O.SOURCES, {
  iss: "Schéma simplifié, sans échelle ; modules principaux seulement (NASA, ESA).",
  t1bbnj: "Seuil de 60 ratifications et délai de 120 jours fixés par le traité."
});

(async function () {
  const code = "hggsp-t1-a2", D = O.donneesSite(), out = {};
  for (const nom of ["iss", "mer", "scs", "t1bbnj"]) { out[nom] = O.sceneDuSite(D, nom); if (SOURCES[nom]) out[nom].source = SOURCES[nom]; }
  const d3 = O.chargerD3(), FEAT = await O.naturalEarth();
  for (const nom of Object.keys(CARTES_VIDEO)) out[nom] = CARTES_VIDEO[nom](D, d3, FEAT);
  const js = "// Généré par outils/serie-hggsp/scenes_t1_a2.js : ne pas modifier à la main.\n" +
    "// Scènes du site (outils/specialites/hggsp/src/) et cartes propres à la vidéo, jouées par le type scene du moteur.\n" +
    "window.HG_FONDS = " + JSON.stringify({ monde: O.fondSVG(D.CARTES, "monde") }) + ";\n" +
    "window.HG_SCENES = " + JSON.stringify(out) + ";\n";
  const dest = path.join(RACINE, "hggsp", "serie", "illu-" + code + ".js");
  fs.writeFileSync(dest, js);
  console.log(path.relative(RACINE, dest), Math.round(js.length / 1024) + " Ko :", Object.keys(out).map(k => k + " (" + out[k].etapes.length + " étapes)").join(", "));
})();
