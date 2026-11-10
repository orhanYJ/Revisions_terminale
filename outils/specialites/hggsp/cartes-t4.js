/* Cartes et scènes d'animation du thème 4 « Identifier, protéger et valoriser le patrimoine » (renfort thèmes 3 et 4).
   Chargé par cartes.js après cartes-t3.js (ordre alphabétique) : réutilise ctx.EUROPEC défini par cartes-t3.js. */
module.exports = function (ctx) {
  const { d3, cadre, simplifier, M, WM, HM, OUT } = ctx;

  function fleche(P, a, b, o) {
    o = o || {};
    const [x1, y1] = P(a), [x2, y2] = P(b);
    const dx = x2 - x1, dy = y2 - y1, c = o.courbe === undefined ? 0.18 : o.courbe;
    const cx = (x1 + x2) / 2 - dy * c, cy = (y1 + y2) / 2 + dx * c;
    let ux = x2 - cx, uy = y2 - cy; const n = Math.hypot(ux, uy) || 1; ux /= n; uy /= n;
    const r = o.retrait === undefined ? 7 : o.retrait, tx = x2 - ux * r, ty = y2 - uy * r;
    const coul = o.coul || "var(--rouge)";
    const R = v => Math.round(v * 10) / 10;
    return "<path class='fleche trace' pathLength='1' style='stroke:" + coul + "' d='M" + R(x1) + "," + R(y1) + "Q" + R(cx) + "," + R(cy) + " " + R(tx) + "," + R(ty) + "'/>" +
      "<path style='fill:" + coul + "' d='M" + R(tx + ux * 2) + "," + R(ty + uy * 2) + "L" + R(tx - ux * 10 - uy * 5) + "," + R(ty - uy * 10 + ux * 5) + "L" + R(tx - ux * 10 + uy * 5) + "," + R(ty - uy * 10 - ux * 5) + "Z'/>";
  }
  const point = (P, ll, cl, r) => { const [x, y] = P(ll); return "<circle cx='" + x + "' cy='" + y + "' r='" + (r || 6) + "' class='" + (cl || "pt-a") + "'/>"; };
  const etiq = (C, ll, s, o) => C.txt(ll, s, Object.assign({ cl: "lbl" }, o || {})).replace(/"/g, "'");
  /* étiquette déportée, reliée au point par un trait fin (amas européen de la carte du monde) */
  const lead = (ll, lx, ly, txt, a, cl) => { const [x, y] = M.P(ll); return "<path d='M" + x + "," + y + " L" + (lx + (a === "end" ? 3 : -3)) + "," + (ly - 4) + "' stroke='var(--encre2)' stroke-width='1'/><text x='" + lx + "' y='" + ly + "' text-anchor='" + a + "' class='" + (cl || "lbl") + "'>" + txt + "</text>"; };
  const anneau = (P, ll, r, coul) => { const [x, y] = P(ll); return "<circle cx='" + x + "' cy='" + y + "' r='" + r + "' fill='none' stroke='" + coul + "' stroke-width='3'/>"; };

  /* ===== Animation : les frises du Parthénon dispersées (Europe centrale) ===== */
  {
    const WC = 800, HC = 640;
    const pp = d3.geoConicConformal().rotate([-11, 0]).parallels([38, 55]).fitExtent([[0, 0], [WC, HC]], { type: "MultiPoint", coordinates: [[-5.5, 35.0], [27.5, 57.3], [-3.5, 55.5], [27.5, 35.4]] });
    const C = cadre(pp, WC, HC, 1.0, 8);
    const fondC = '<rect width="' + WC + '" height="' + HC + '" class="k-mer-f"/><path d="' + simplifier(C.gp(d3.geoGraticule().step([10, 10])()), 0.5, 0) + '" class="k-grat"/><path d="' + C.pays() + '" class="k-terre"/>';
    const P = C.P;
    const V = { athenes: [23.73, 37.97], londres: [-0.13, 51.5], paris: [2.34, 48.86], copenhague: [12.57, 55.68], vatican: [12.45, 41.9], palerme: [13.36, 38.12], vienne: [16.37, 48.21], munich: [11.58, 48.14], wurzburg: [9.93, 49.79] };
    let s = "";
    s += "<g data-k='parth'>" + point(P, V.athenes, "pt-a", 9) + etiq(C, V.athenes, "Athènes, Acropole", { a: "end", dx: -12, dy: -6, cl: "lbl-f" }) + "</g>";
    s += "<g data-k='y1687'>" + anneau(P, V.athenes, 18, "var(--rouge)") + anneau(P, V.athenes, 28, "var(--rouge)") + etiq(C, V.athenes, "1687 : explosion", { a: "end", dx: -12, dy: 12 }) + "</g>";
    s += "<g data-k='louvre'>" + fleche(P, V.athenes, V.paris, { courbe: -0.12, coul: "var(--acier)" }) + point(P, V.paris, "pt-b", 6) + etiq(C, V.paris, "Louvre (fin du XVIIIe s.)", { a: "end", dx: -10, dy: 4 }) + "</g>";
    s += "<g data-k='elgin'>" + fleche(P, V.athenes, V.londres, { courbe: -0.2, coul: "var(--rouge)" }) + point(P, V.londres, "pt-a", 9) + etiq(C, V.londres, "British Museum (1816)", { a: "end", dx: -12, dy: -8, cl: "lbl-f" }) + "</g>";
    s += "<g data-k='frag'>" + point(P, V.copenhague, "pt-b", 4) + etiq(C, V.copenhague, "Copenhague", { a: "start", dx: 7, dy: 4 }) +
      point(P, V.vienne, "pt-b", 4) + etiq(C, V.vienne, "Vienne", { a: "start", dx: 7, dy: 4 }) + point(P, V.munich, "pt-b", 4) + etiq(C, V.munich, "Munich", { a: "start", dx: 7, dy: 10 }) +
      point(P, V.wurzburg, "pt-b", 4) + etiq(C, V.wurzburg, "Wurtzbourg", { a: "end", dx: -7, dy: 0 }) + point(P, V.vatican, "pt-b", 5) + etiq(C, V.vatican, "Vatican", { a: "end", dx: -8, dy: 4 }) +
      point(P, V.palerme, "pt-b", 5) + etiq(C, V.palerme, "Palerme", { a: "end", dx: -8, dy: 4 }) + "</g>";
    s += "<g data-k='grece'><text x='" + (P(V.athenes)[0] - 12) + "' y='" + (P(V.athenes)[1] + 40) + "' text-anchor='end' class='lbl'>Grèce indépendante (1830)</text></g>";
    s += "<g data-k='mercouri'>" + fleche(P, V.athenes, V.londres, { courbe: 0.25, coul: "var(--ok)", retrait: 12 }) + etiq(C, [18.2, 47.6], "demande de retour (1983)", { a: "start", cl: "lbl" }) + "</g>";
    s += "<g data-k='musee'>" + anneau(P, V.athenes, 16, "var(--ok)") + etiq(C, V.athenes, "musée de l'Acropole (2009)", { a: "end", dx: -20, dy: 22 }) + "</g>";
    s += "<g data-k='retours'>" + fleche(P, V.palerme, V.athenes, { courbe: 0.25, coul: "var(--ok)" }) + fleche(P, V.vatican, V.athenes, { courbe: -0.2, coul: "var(--ok)" }) + etiq(C, [17.5, 39.6], "retours 2022-2023", { a: "middle", cl: "lbl" }) + "</g>";
    s += "<g data-k='litige'>" + anneau(P, V.londres, 16, "var(--rouge)") + etiq(C, V.londres, "litige non réglé (2026)", { a: "start", dx: 18, dy: 22, cl: "lbl-f" }) + "</g>";
    OUT.anims.t4parthenon = { w: WC, h: HC, fond: fondC, calques: s };
  }

  /* ===== Animation : une liste qui grandit et se diversifie (monde) ===== */
  {
    const P = M.P;
    const prem = [[-90.5, -0.6], [-110.5, 44.6], [-108.46, 37.18], [-125.6, 61.5], [-55.53, 51.6], [-78.51, -0.22], [-17.4, 14.67], [39.04, 12.03], [38.2, 13.2], [6.08, 50.77], [19.94, 50.06], [20.05, 49.98]];
    let s = "<g data-k='y1978'>";
    prem.forEach(ll => { s += point(P, ll, "pt-b", 4.5); });
    s += etiq(M, [-110.5, 44.6], "Yellowstone", { a: "end", dx: -8 }) + etiq(M, [-90.5, -0.6], "Galápagos", { a: "end", dx: -8 }) + etiq(M, [-17.4, 14.67], "Gorée", { a: "end", dx: -8 }) + etiq(M, [39.04, 12.03], "Lalibela", { a: "start", dx: 8, dy: 6 }) + lead([19.94, 50.06], 600, 24, "Cracovie 1978", "start") + "</g>";
    const g = (k, ll, cl, txt, o) => "<g data-k='" + k + "'>" + point(P, ll, cl, 5.5) + etiq(M, ll, txt, o) + "</g>";
    s += "<g data-k='y1979'>" + point(P, [2.12, 48.8], "pt-a", 5.5) + lead([2.12, 48.8], 455, 66, "Versailles 1979", "end") + "</g><g data-k='y1979b'>" + point(P, [19.18, 50.03], "pt-a", 5.5) + lead([19.18, 50.03], 600, 42, "Auschwitz 1979", "start") + "</g>";
    s += "<g data-k='y1987'>" + point(P, [12.33, 45.44], "pt-a", 5.5) + lead([12.33, 45.44], 455, 100, "Venise 1987", "end") + point(P, [-3.0, 16.77], "pt-a", 5.5) + etiq(M, [-3.0, 16.77], "Tombouctou 1988", { a: "start", dx: 8, dy: 4 }) + "</g>";
    s += "<g data-k='y2001'>" + anneau(P, [67.83, 34.83], 11, "var(--rouge)") + point(P, [67.83, 34.83], "pt-a", 5) + etiq(M, [67.83, 34.83], "Bamiyan 2001", { a: "start", dx: 12, dy: 4 }) + "</g>";
    s += "<g data-k='radies'>";
    [[57.0, 20.0], [13.74, 51.05], [-2.99, 53.41]].forEach(ll => { const [x, y] = P(ll); s += "<path d='M" + (x - 6) + "," + (y - 6) + "L" + (x + 6) + "," + (y + 6) + "M" + (x + 6) + "," + (y - 6) + "L" + (x - 6) + "," + (y + 6) + "' stroke='var(--rouge)' stroke-width='3'/>"; });
    s += lead([-2.99, 53.41], 455, 30, "Liverpool 2021", "end") + lead([13.74, 51.05], 600, 60, "Dresde 2009", "start") + etiq(M, [57.0, 20.0], "Oman 2007", { a: "start", dx: 9, dy: 6 }) + "</g>";
    s += "<g data-k='y2014'>" + point(P, [22.6, -19.3], "pt-b", 6) + etiq(M, [22.6, -19.3], "Okavango : 1 000e bien (2014)", { a: "start", dx: 9, dy: 4 }) + "</g>";
    s += "<g data-k='y2015'>" + anneau(P, [38.27, 34.55], 10, "var(--rouge)") + anneau(P, [43.13, 36.34], 10, "var(--rouge)") + etiq(M, [38.27, 34.55], "Palmyre 2015", { a: "end", dx: -10, dy: 12 }) + etiq(M, [43.13, 36.34], "Mossoul 2017", { a: "start", dx: 10, dy: -4 }) + "</g>";
    s += "<g data-k='y2023'>" + point(P, [30.06, -1.95], "pt-b", 5.5) + etiq(M, [30.06, -1.95], "mémoriaux du génocide (Rwanda)", { a: "end", dx: -9, dy: 4 }) + point(P, [2.72, 50.4], "pt-b", 5) + anneau(P, [30.73, 46.48], 10, "var(--rouge)") + lead([30.73, 46.48], 600, 82, "Odessa (en péril, 2023)", "start") + "</g>";
    s += "<g data-k='y2026'>" + anneau(P, [-0.8, 49.35], 12, "var(--ok)") + lead([-0.8, 49.35], 455, 48, "Débarquement 2026", "end", "lbl-f") + "</g>";
    s += "<g data-k='bilan'><rect x='130' y='300' width='252' height='58' rx='6' fill='var(--papier)' opacity='.92' stroke='var(--rouge)'/><text x='142' y='322' class='lbl-f'>1 273 biens (juillet 2026)</text><text x='142' y='342' class='lbl'>près de la moitié en Europe et Amérique du Nord</text></g>";
    OUT.anims.t4monde = { w: WM, h: HM, vb: [120, 10, 720, 370], fond: "monde", calques: s };
  }

  /* ===== Animation : la question patrimoniale au Mali ===== */
  {
    const W = 800, H = 620;
    const proj = d3.geoMercator().fitExtent([[10, 10], [W - 10, H - 10]], { type: "MultiPoint", coordinates: [[-12.6, 10.0], [4.5, 25.2]] });
    const C = cadre(proj, W, H, 0.5, 2);
    const mali = C.pays(f => f.properties.ADMIN === "Mali");
    const [, yZone] = C.P([0, 15.6]);
    const fond = '<rect width="' + W + '" height="' + H + '" class="k-mer-f"/><path d="' + C.pays(f => f.properties.ADMIN !== "Mali") + '" class="k-terre"/><path d="' + mali + '" class="k-terre-cn"/>' +
      '<clipPath id="clip-mali-anim"><path d="' + mali + '"/></clipPath>';
    const P = C.P;
    const S = { tomb: [-3.0, 16.77], djenne: [-4.55, 13.9], band: [-3.45, 14.4], gao: [-0.04, 16.27], bamako: [-8.0, 12.64], konna: [-3.88, 14.95], kidal: [1.41, 18.44] };
    let s = "<g data-k='zone'><rect x='0' y='0' width='" + W + "' height='" + yZone + "' clip-path='url(#clip-mali-anim)' class='zone'/>" + etiq(C, [-1.5, 20.5], "nord contrôlé par des groupes armés", { a: "middle", cl: "lbl-f" }) + etiq(C, [-1.5, 19.7], "(avril 2012-janvier 2013, tracé approximatif)", { a: "middle", cl: "lbl" }) + "</g>";
    s += "<g data-k='sites'>" + point(P, S.tomb, "pt-b", 7) + etiq(C, S.tomb, "Tombouctou (1988)", { a: "end", dx: -16, dy: -10 }) + point(P, S.djenne, "pt-b", 7) + etiq(C, S.djenne, "Djenné (1988)", { a: "end", dx: -18, dy: 0 }) +
      point(P, S.band, "pt-b", 7) + etiq(C, S.band, "Falaise de Bandiagara (1989)", { a: "start", dx: 18, dy: 4 }) + point(P, S.gao, "pt-b", 7) + etiq(C, S.gao, "Tombeau des Askia, Gao (2004)", { a: "start", dx: 18, dy: 4 }) +
      point(P, S.bamako, "pt-a", 5) + etiq(C, S.bamako, "Bamako", { a: "end", dx: -9, dy: 4 }) + "</g>";
    s += "<g data-k='peril12'>" + anneau(P, S.tomb, 14, "var(--rouge)") + anneau(P, S.gao, 14, "var(--rouge)") + "</g>";
    s += "<g data-k='destr'><text x='" + (P(S.tomb)[0] + 18) + "' y='" + (P(S.tomb)[1] - 18) + "' class='lbl-f'>mausolées détruits</text></g>";
    s += "<g data-k='manus'>" + fleche(P, S.tomb, S.bamako, { courbe: 0.15, coul: "var(--acier)" }) + etiq(C, [-6.5, 15.4], "≈ 370 000 manuscrits évacués", { a: "end", dx: 0 }) + "</g>";
    s += "<g data-k='serval'>" + fleche(P, S.bamako, S.konna, { courbe: -0.1, coul: "var(--acier)" }) + fleche(P, S.konna, S.tomb, { courbe: -0.15, coul: "var(--acier)" }) + point(P, S.konna, "pt-a", 5) + etiq(C, S.konna, "Konna (janv. 2013)", { a: "end", dx: -9, dy: -6 }) + "</g>";
    s += "<g data-k='recon'>" + anneau(P, S.tomb, 22, "var(--ok)") + etiq(C, S.tomb, "reconstruits (2014-2015)", { a: "start", dx: 26, dy: -16 }) + "</g>";
    s += "<g data-k='peril16'>" + anneau(P, S.djenne, 14, "var(--rouge)") + etiq(C, S.djenne, "en péril (2016)", { a: "end", dx: -18, dy: 16 }) + "</g>";
    s += "<g data-k='peril23'>" + anneau(P, S.band, 14, "var(--rouge)") + etiq(C, S.band, "en péril (2023)", { a: "start", dx: 18, dy: 20 }) + "</g>";
    s += "<g data-k='retour'>" + fleche(P, S.bamako, S.tomb, { courbe: 0.3, coul: "var(--ok)" }) + etiq(C, S.bamako, "retour des manuscrits (août 2025)", { a: "start", dx: -20, dy: 24 }) + "</g>";
    const deco = etiq(C, [-5.5, 21.5], "MALI", { cl: "k-pays", a: "middle" }) + etiq(C, [-10.5, 21.5], "MAURITANIE", { cl: "k-pays", a: "middle" }) + etiq(C, [3.5, 21.4], "ALGÉRIE", { cl: "k-pays", a: "middle" }) +
      etiq(C, [2.8, 13.6], "NIGER", { cl: "k-pays", a: "middle" }) + etiq(C, [-1.6, 12.2], "BURKINA FASO", { cl: "k-pays", a: "middle" });
    OUT.anims.t4mali = { w: W, h: H, vb: [40, 120, 720, 470], fond, calques: deco + s };
  }

  /* ===== Carte interactive : le patrimoine mondial, entre valorisation et menaces ===== */
  {
    const pt = (c, ll, n, a, t, d) => { const [x, y] = M.P(ll); return { c, x, y, n, a, t, d }; };
    const pts = [
      pt("etud", [2.35, 48.86], "France", "end", "France : 56 biens (septembre 2026)", "Versailles (1979), Paris, rives de la Seine (1991), bassin minier (2012), plages du Débarquement (2026)… : voir la carte de la France ci-dessous et l'objet de travail conclusif."),
      pt("etud", [23.73, 37.97], "Athènes", "start", "Acropole d'Athènes (Grèce, 1987)", "Les frises du Parthénon sont dispersées entre Athènes, Londres et d'autres musées ; la Grèce réclame les marbres du British Museum depuis 1983."),
      pt("etud", [-3.0, 16.77], "Tombouctou", "start", "Tombouctou (Mali, 1988, en péril depuis 2012)", "Mosquées et mausolées de saints, manuscrits : des mausolées détruits par des djihadistes en 2012, reconstruits avec l'UNESCO ; premier procès de la CPI pour destruction du patrimoine (2016)."),
      pt("etud", [12.33, 45.44], "Venise", "start", "Venise et sa lagune (Italie, 1987)", "Moins de 50 000 habitants dans le centre historique depuis 2022, des millions de visiteurs : grands navires interdits en 2021, droit d'accès payant certains jours depuis 2024."),
      pt("menace", [67.83, 34.83], "Bamiyan", "start", "Bamiyan (Afghanistan)", "Les deux bouddhas géants (VIe siècle) sont dynamités par les talibans en mars 2001. Le site est inscrit au patrimoine mondial et sur la liste en péril en 2003."),
      pt("menace", [38.27, 34.55], "Palmyre", "end", "Palmyre (Syrie, 1980)", "Daech détruit le temple de Baalshamin et le temple de Bel en 2015 et assassine l'archéologue Khaled al-Asaad, ancien directeur des antiquités du site (18 août 2015)."),
      pt("menace", [43.13, 36.34], "Mossoul", "start", "Mossoul (Irak)", "La mosquée al-Nouri et son minaret penché (XIIe siècle) sont détruits par Daech en juin 2017. L'UNESCO lance en 2018 l'initiative « Faire revivre l'esprit de Mossoul » pour les reconstruire."),
      pt("menace", [30.73, 46.48], "Odessa", "start", "Centre historique d'Odessa (Ukraine)", "Inscrit au patrimoine mondial et sur la liste en péril en procédure d'urgence le 25 janvier 2023, en pleine guerre."),
      pt("menace", [-2.99, 53.41], "Liverpool", "end", "Liverpool (Royaume-Uni), radiée en 2021", "Le port marchand, inscrit en 2004, est retiré de la liste le 21 juillet 2021 à cause de projets immobiliers qui ont altéré son paysage : troisième radiation de l'histoire après l'Oman (2007) et Dresde (2009)."),
      pt("menace", [13.74, 51.05], "Dresde", "start", "Vallée de l'Elbe à Dresde (Allemagne), radiée en 2009", "Un pont routier construit en plein paysage protégé conduit l'UNESCO à retirer le bien de la liste."),
      pt("memoire", [19.18, 50.03], "Auschwitz", "start", "Auschwitz-Birkenau (Pologne, 1979)", "Un des premiers lieux de mémoire inscrits : un patrimoine de l'horreur, à transmettre (voir le thème 3)."),
      pt("memoire", [30.06, -1.95], "Rwanda", "start", "Sites mémoriaux du génocide (Rwanda, 2023)", "Nyamata, Murambi, Gisozi et Bisesero, inscrits le 20 septembre 2023, après des années de débat sur les lieux liés à des conflits récents."),
      pt("memoire", [132.45, 34.39], "Hiroshima", "end", "Mémorial de la paix d'Hiroshima (Japon, 1996)", "Le dôme de Genbaku, seul bâtiment resté debout près de l'hypocentre du 6 août 1945, inscrit malgré les réserves des États-Unis et de la Chine."),
      pt("valor", [-17.4, 14.67], "Gorée", "end", "Île de Gorée (Sénégal, 1978)", "Parmi les douze premiers biens inscrits : un lieu de mémoire de la traite atlantique, devenu un symbole visité par les chefs d'État."),
      pt("valor", [22.6, -19.3], "Okavango", "start", "Delta de l'Okavango (Botswana, 2014)", "Le 1 000e bien inscrit sur la liste du patrimoine mondial."),
      pt("valor", [32.59, 22.34], "Abou Simbel", "start", "Monuments de Nubie (Égypte, 1979)", "Sauvés de la montée des eaux du barrage d'Assouan par une campagne internationale de l'UNESCO lancée en 1960 : les temples d'Abou Simbel sont démontés et remontés (1964-1968)."),
      pt("valor", [104.0, 30.9], "Chine", "end", "La Chine, 61 biens", "Deuxième pays le plus doté après l'Italie (62 biens) en septembre 2026 : l'inscription est aussi un instrument de soft power et de tourisme.")
    ];
    const R = { France: ["end", 10], Liverpool: ["end", -4], Dresde: ["start", -10], Auschwitz: ["start", 6], Venise: ["end", 10], "Athènes": ["end", 12], Odessa: ["start", 12] };
    pts.forEach(p => { if (R[p.n]) { p.a = R[p.n][0]; p.dy = R[p.n][1]; } });
    const meta = { t: "Le patrimoine mondial : lieux étudiés, menaces, mémoire", c: { etud: ["Lieux étudiés dans le thème", "#B3241B"], menace: ["Destructions, menaces, radiations", "#2D5675"], memoire: ["Lieux de mémoire inscrits", "#B07A1E"], valor: ["Repères de la liste", "#2F6B3B"] } };
    OUT.cartes.patrimoine = { w: WM, h: HM, fond: "monde", deco: "", pts, meta, vb: [300, 20, 640, 330] };
  }

  /* ===== Carte interactive : la France et son patrimoine ===== */
  {
    const W = 760, H = 720;
    const proj = d3.geoConicConformal().rotate([-2.5, 0]).parallels([44, 49]).fitExtent([[20, 20], [W - 20, H - 20]], { type: "MultiPoint", coordinates: [[-4.8, 42.3], [8.3, 51.1]] });
    const C = cadre(proj, W, H, 0.6, 3);
    const fond = '<rect width="' + W + '" height="' + H + '" class="k-mer-f"/><path d="' + C.pays(f => f.properties.ADMIN !== "France") + '" class="k-terre"/><path d="' + C.pays(f => f.properties.ADMIN === "France") + '" class="k-terre-cn"/>';
    const pt = (c, ll, n, a, t, d) => { const [x, y] = C.P(ll); return { c, x, y, n, a, t, d }; };
    const pts = [
      pt("etud", [2.12, 48.8], "Versailles", "end", "Versailles (patrimoine mondial 1979)", "Château royal, musée (1837), lieu de mémoire franco-allemand (1871, 1919) et de la République (Congrès)."),
      pt("etud", [2.35, 48.86], "Paris", "start", "Paris, rives de la Seine (1991)", "Notre-Dame (incendie 2019, réouverture 2024), tours et PLU bioclimatique (2024)."),
      pt("etud", [2.83, 50.43], "Lens", "start", "Bassin minier (2012) et Louvre-Lens (2012)", "Inscription le 30 juin 2012 ; Louvre-Lens ouvert le 4 décembre 2012 sur l'ancien carreau de la fosse 9."),
      pt("etud", [3.17, 50.34], "Lewarde", "start", "Centre historique minier de Lewarde", "Ouvert en 1984 sur la fosse Delloye : le plus grand musée de la mine en France."),
      pt("etud", [5.04, 47.32], "Dijon", "start", "Cité internationale de la gastronomie et du vin (Dijon)", "Ouverte en mai 2022 : l'un des équipements prévus pour faire vivre l'inscription du repas gastronomique des Français (2010)."),
      pt("unesco", [-1.51, 48.64], "Mont-Saint-Michel", "end", "Mont-Saint-Michel et sa baie (1979)", "Parmi les premiers biens français inscrits ; plus de deux millions de visiteurs par an, d'où un aménagement pour limiter les voitures sur le site."),
      pt("unesco", [-0.57, 44.84], "Bordeaux", "end", "Bordeaux, port de la Lune (2007)", "Un ensemble urbain du XVIIIe siècle : l'inscription a accompagné la reconquête des quais."),
      pt("unesco", [0.11, 49.49], "Le Havre", "start", "Le Havre, la ville reconstruite par Auguste Perret (2005)", "Un patrimoine du XXe siècle, en béton : la reconnaissance d'une ville détruite en 1944 et reconstruite."),
      pt("unesco", [4.83, 45.76], "Lyon", "start", "Site historique de Lyon (1998)", "Du Vieux-Lyon à la Croix-Rousse : un centre ancien sauvé de la démolition par le premier secteur sauvegardé (1964)."),
      pt("unesco", [2.35, 43.21], "Carcassonne", "start", "Cité de Carcassonne (1997)", "Restaurée par Viollet-le-Duc au XIXe siècle : un exemple de restauration discutée."),
      pt("unesco", [-3.08, 47.58], "Carnac", "end", "Mégalithes de Carnac et des rives du Morbihan (2025)", "Plus de 3 000 menhirs alignés : inscription obtenue en 2025."),
      pt("memoire", [-0.8, 49.35], "Débarquement", "start", "Plages du Débarquement (2026)", "Inscrites le 26 juillet 2026 : un patrimoine de mémoire, inscrit le même jour que les forteresses royales du Languedoc : la France compte 56 biens."),
      pt("memoire", [2.72, 50.4], "Lorette", "end", "Sites funéraires et mémoriels de la Première Guerre mondiale (2023)", "139 sites en France et en Belgique, inscrits le 20 septembre 2023, dont l'Anneau de la Mémoire de Notre-Dame-de-Lorette."),
      pt("memoire", [5.43, 49.21], "Verdun", "start", "Verdun (ossuaire de Douaumont)", "Un des sites du bien de 2023 ; lieu de la réconciliation franco-allemande (1984).")
    ];
    const R = { Paris: ["start", -6], Versailles: ["end", 8], Lewarde: ["start", 10], Lens: ["start", -6], Lorette: ["end", -4], "Le Havre": ["start", -6], "Débarquement": ["end", 6] };
    pts.forEach(p => { if (R[p.n]) { p.a = R[p.n][0]; p.dy = R[p.n][1]; } });
    const meta = { t: "La France et son patrimoine : des lieux, des politiques, des mémoires", c: { etud: ["Lieux étudiés dans le thème", "#B3241B"], unesco: ["Autres biens du patrimoine mondial", "#2D5675"], memoire: ["Patrimoine et mémoire des guerres", "#B07A1E"] } };
    OUT.cartes.patrifr = { w: W, h: H, fond, deco: "", pts, meta };
  }
};
