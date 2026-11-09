/* Cartes des fiches de géographie (G1, G2, G3) : les cartes du site, telles qu'elles sont injectées dans dnl/index.html
   (G1_FOND, G1_MAPS, G2_MAPS, G3_MAPS, produites par outils/cartes-geo/), écrites en SVG autonomes dans cartes/,
   avec les couleurs du site à la place des variables CSS.
   Usage, depuis la racine du dépôt :  node outils/fiches-dnl/cartes-geo.js   (avant generer.js G1 G2 G3) */
const fs = require("fs");
const path = require("path");
const ICI = __dirname;
const html = fs.readFileSync(path.join(ICI, "..", "..", "dnl", "index.html"), "utf8");
const lire = nom => { const m = html.match(new RegExp("^const " + nom + " = (.*);$", "m")); if (!m) throw new Error(nom); return JSON.parse(m[1]); };
const VARS = { "--g1-mer": "#dfeaee", "--g1-grat": "#c9dbe2", "--g1-terre": "#f1ead8", "--g1-front": "#cdbf9f", "--g1-encre": "#17233F", "--g1-halo": "#fffdf7" };
const FOND = lire("G1_FOND"), VB = lire("G1_VB");
const M = { G1: lire("G1_MAPS"), G2: lire("G2_MAPS"), G3: lire("G3_MAPS") };
/* fichier de la fiche → [chapitre, clé de la carte] ; « <code> » seul = carte principale */
const SORTIES = {
  "G1": ["G1", "routes"], "G1-choke": ["G1", "choke"],
  "G2": ["G2", "arctic"], "G2-scs": ["G2", "scs"], "G2-bases": ["G2", "bases"],
  "G3": ["G3", "monde"], "G3-metro": ["G3", "metro"], "G3-synth": ["G3", "synth"]
};
const remplacer = s => s.replace(/var\((--g1-[a-z]+)\)/g, (_, v) => VARS[v]);
for (const [fichier, [ch, cle]] of Object.entries(SORTIES)) {
  const m = M[ch][cle];
  for (const lang of ["en", "fr"]) {
    const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + (m.vb || VB) + '" width="100%" font-family="Inter, Arial, sans-serif">' +
      remplacer((m.fond || FOND) + m[lang]).replace(/g3h-appro-(en|fr)/g, "g3h-appro-fiche") + "</svg>";
    fs.writeFileSync(path.join(ICI, "cartes", fichier + "-" + lang + ".svg"), svg);
  }
  console.log(fichier, Math.round(fs.statSync(path.join(ICI, "cartes", fichier + "-en.svg")).size / 1024) + " Ko");
}
