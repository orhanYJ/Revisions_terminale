/* Cartes propres à la vidéo hggsp-t1-a1 (thème 1, axe 1 : conquêtes, affirmations de puissance et rivalités).
   Chargé par outils/serie-hggsp/scenes.js (tout fichier cartes-<code>.js du dossier) : exporte une fonction (outils)
   qui renvoie { cartes: { nom(D, d3, FEAT) → scène }, videos: { code: { site: [...], video: [...] } } }.
   Coordonnées : [longitude, latitude] ; même fond mondial Equal Earth que le site (cartes.js de HGGSP). */
module.exports = function (O) {
  const { cadre, esc } = O;

  /* « Les mers, espaces de puissance » : flottes américaines, SNLE, porte-avions, détroits, Djibouti, mer Rouge.
     Points et détroits repris de la carte « mer » du site (outils/specialites/hggsp/cartes.js) ; données du chapitre t1-a1. */
  function marine(D, d3, FEAT) {
    const WM = 1000, pm = d3.geoEqualEarth().rotate([-10, 0]);
    pm.fitWidth(WM - 8, { type: "Sphere" }); pm.translate([WM / 2, pm.translate()[1]]);
    const yN = pm([10, 80])[1];
    pm.translate([pm.translate()[0], pm.translate()[1] - yN + 6]);
    const C = cadre(d3, FEAT, pm, WM, D.CARTES.monde.h, 0.55, 2.5);
    const defs = "<defs><marker id='fl-marine' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--rouge)'/></marker>" +
      "<marker id='fl-marineb' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'><path d='M0,0L10,5L0,10z' fill='var(--acier)'/></marker></defs>";
    /* trajet au crayon par plusieurs points (courbe lissée), flèche à la fin ; bleu si o.b */
    const trajet = (k, lls, o = {}) => {
      const p = lls.map(ll => C.P(ll));
      let d = "M" + p[0].join(",");
      for (let i = 1; i < p.length; i++) {
        const [x0, y0] = p[i - 1], [x1, y1] = p[i], c = o.c === undefined ? 0.12 : o.c;
        const cx = Math.round((x0 + x1) / 2 - (y1 - y0) * c), cy = Math.round((y0 + y1) / 2 + (x1 - x0) * c);
        d += "Q" + cx + "," + cy + " " + x1 + "," + y1;
      }
      return "<path data-k='" + k + "' class='trace' pathLength='1' d='" + d + "' fill='none' stroke='" + (o.b ? "var(--acier)" : "var(--rouge)") +
        "' stroke-width='3' stroke-linecap='round' marker-end='url(#fl-marine" + (o.b ? "b" : "") + ")'/>";
    };
    const croix = (k, ll, nom, o = {}) => {
      const [x, y] = C.P(ll), a = o.a || "start", dx = a === "end" ? -9 : a === "middle" ? 0 : 9;
      return "<g data-k='" + k + "'><path d='M" + (x - 5) + "," + (y - 5) + "L" + (x + 5) + "," + (y + 5) + "M" + (x + 5) + "," + (y - 5) + "L" + (x - 5) + "," + (y + 5) +
        "' stroke='var(--rouge)' stroke-width='3' fill='none'/>" +
        "<text x='" + (x + dx) + "' y='" + (y + 4 + (o.dy || 0)) + "' text-anchor='" + a + "' class='lbl'>" + esc(nom) + "</text></g>";
    };
    const zone = (k, ring) => { if (d3.geoArea({ type: "Polygon", coordinates: [ring] }) > 2 * Math.PI) ring = ring.slice().reverse(); return "<g data-k='" + k + "'>" + C.poly(ring, "class='zone'") + "</g>"; };
    const s = [
      defs,
      C.etiq("", [-35, 30], "OCÉAN ATLANTIQUE", { cl: "k-mer" }), C.etiq("", [-150, 5], "OCÉAN PACIFIQUE", { cl: "k-mer" }), C.etiq("", [82, -34], "OCÉAN INDIEN", { cl: "k-mer" }),
      /* 1. les flottes américaines */
      C.point("us", [-76.3, 36.9], "Norfolk", { a: "start", cl: "pt-b" }),
      C.point("us2", [-117.2, 32.7], "San Diego", { a: "end", cl: "pt-b" }),
      C.point("f6", [14.3, 40.8], "6e flotte (Naples)", { a: "start", cl: "pt-b", dy: -4 }),
      C.point("f5", [50.6, 26.2], "5e flotte (Bahreïn)", { a: "end", cl: "pt-b", dy: -14 }),
      C.point("f7", [139.7, 35.3], "7e flotte (Japon)", { a: "end", cl: "pt-b", dy: -12 }),
      /* 2. les bases de SNLE */
      C.point("sn1", [-4.5, 48.3], "Île Longue", { a: "end" }),
      C.point("sn2", [-4.8, 56.1], "Faslane", { a: "end" }),
      C.point("sn3", [-81.5, 30.8], "Kings Bay", { a: "end" }),
      C.point("sn4", [-122.7, 47.7], "Bangor", { a: "start" }),
      C.point("sn5", [33.3, 69.3], "Gadjievo", { a: "start" }),
      C.point("sn6", [158.4, 52.9], "Vilioutchinsk", { a: "end" }),
      C.point("sn7", [109.6, 18.2], "Yulin", { a: "start" }),
      C.point("sn8", [83.2, 17.7], "Visakhapatnam", { a: "end" }),
      C.etiq("ilt", [-4.5, 48.3], "4 SNLE · missile M51", { cl: "lbl-f", a: "end", dx: -12, dy: 30 }),
      /* 3. le Charles-de-Gaulle : Chammal (2015), Clemenceau 25 (2024-2025) */
      C.point("toulon", [5.9, 43.1], "Toulon", { a: "end", dy: 14 }),
      trajet("chammal", [[6.5, 42.6], [20, 34.5], [32.5, 34.2]], { c: 0.1 }),
      C.etiq("chamt", [24, 31], "Chammal (2015) : Irak, Syrie", { cl: "lbl-f" }),
      trajet("clem", [[6.5, 42.4], [31.5, 32.5], [38, 20], [56, 11], [80, 2], [105, -2], [140, 5]], { c: 0.05 }),
      C.etiq("clemt", [92, -10], "Clemenceau 25 (nov. 2024 – avr. 2025)", { cl: "lbl-f" }),
      /* 4. le Fujian */
      C.point("sanya", [109.5, 18.25], "Sanya : le Fujian (2025)", { a: "end", dy: 16 }),
      /* 5. les détroits stratégiques */
      croix("ch1", [56.3, 26.6], "Ormuz", { a: "start", dy: -8 }),
      croix("ch2", [43.4, 12.6], "Bab el-Mandeb", { a: "start", dy: 14 }),
      croix("ch3", [101.5, 2.6], "Malacca", { a: "end" }),
      /* 6. Djibouti */
      C.point("djib", [43.15, 11.5], "Djibouti", { a: "end", dy: 6 }),
      C.etiq("djibt", [43.15, 11.5], "France · États-Unis · Japon · Chine (depuis 2017)", { cl: "lbl-f", a: "end", dx: -14, dy: 38 }),
      /* 7. la mer Rouge depuis novembre 2023 */
      zone("houthis", [[42.7, 13.2], [44.4, 13.3], [45.2, 15.2], [44.6, 17.4], [43.2, 17.4], [42.7, 15.6], [42.7, 13.2]]),
      C.etiq("houthist", [47.5, 16.2], "Houthis", { cl: "lbl-f", a: "start" }),
      C.point("galaxy", [41.0, 16.0], "Galaxy Leader (19 nov. 2023)", { a: "end", dy: -12 }),
      trajet("pg", [[56, 7], [48, 10.5], [41.5, 14.5]], { b: true, c: -0.15 }),
      C.etiq("pgt", [60, 6], "Prosperity Guardian (déc. 2023)", { cl: "lbl", a: "start" }),
      trajet("aspides", [[31, 33.5], [33.5, 26], [39.5, 18.5]], { b: true, c: 0.12 }),
      C.etiq("aspt", [30, 29], "Aspides, UE (févr. 2024)", { cl: "lbl", a: "end", dx: -6 })
    ].join("");
    return { titre: "Les mers, espaces de puissance", w: WM, h: D.CARTES.monde.h, vb: [0, 0, WM, D.CARTES.monde.h], fond: "monde", svg: s, etapes: [],
      source: "Fond Natural Earth (domaine public). Positions et trajets approximatifs." };
  }

  return {
    cartes: { marine },
    videos: { "hggsp-t1-a1": { site: ["espace", "t1asat"], video: ["marine"] } },
    sources: { t1asat: "Positions des tirs symboliques.",
      espace: "Fond Natural Earth. Premiers lancements orbitaux nationaux ; positions approximatives." }
  };
};
