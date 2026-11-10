/* Cartes et scènes d'animation du thème 3 « Histoire et mémoires » (renfort thèmes 3 et 4).
   Chargé par cartes.js : module.exports = function (ctx) { … } ; voir RENFORTS.md. */
module.exports = function (ctx) {
  const { d3, cadre, simplifier, esc, M, WM, HM, OUT } = ctx;

  /* flèche courbe (trait qui se dessine + pointe) entre deux points projetés */
  function fleche(P, a, b, o) {
    o = o || {};
    const [x1, y1] = P(a), [x2, y2] = P(b);
    const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy) || 1, c = o.courbe === undefined ? 0.18 : o.courbe;
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

  /* ---------- fond de l'Europe (conique conforme), commun aux scènes européennes ---------- */
  const WE = 900, HE = 640;
  const pe = d3.geoConicConformal().rotate([-14, 0]).parallels([38, 58]).fitExtent([[10, 10], [WE - 10, HE - 10]], { type: "MultiPoint", coordinates: [[-9, 34], [40, 61], [36, 30]] });
  const E = cadre(pe, WE, HE, 0.8, 4);
  const fondE = '<rect width="' + WE + '" height="' + HE + '" class="k-mer-f"/><path d="' + simplifier(E.gp(d3.geoGraticule().step([10, 10])()), 0.5, 0) + '" class="k-grat"/><path d="' + E.pays() + '" class="k-terre"/>';

  /* ---------- fond de l'Europe centrale, plus serré, pour les scènes animées (réutilisé par cartes-t4.js) ---------- */
  const WC = 900, HC = 620;
  const pc = d3.geoConicConformal().rotate([-12, 0]).parallels([40, 58]).fitExtent([[0, 0], [WC, HC]], { type: "MultiPoint", coordinates: [[-6.5, 36.3], [31.5, 60.6], [-4, 58], [27, 36.5]] });
  const C = cadre(pc, WC, HC, 1.0, 8);
  const fondC = '<rect width="' + WC + '" height="' + HC + '" class="k-mer-f"/><path d="' + simplifier(C.gp(d3.geoGraticule().step([10, 10])()), 0.5, 0) + '" class="k-grat"/><path d="' + C.pays() + '" class="k-terre"/>';
  ctx.EUROPEC = { C, fondC, WC, HC, fleche, point, etiq };

  /* ===== Animation : juillet-août 1914, l'engrenage ===== */
  {
    const V = {
      sarajevo: [18.41, 43.86], vienne: [16.37, 48.21], berlin: [13.4, 52.52], belgrade: [20.46, 44.8], petersbourg: [30.32, 59.94],
      paris: [2.35, 48.86], bruxelles: [4.35, 50.85], londres: [-0.13, 51.5]
    };
    const P = C.P;
    let s = "";
    s += "<g data-k='sar'>" + point(P, V.sarajevo, "pt-a", 7) + etiq(C, V.sarajevo, "Sarajevo, 28 juin", { dx: -10, dy: 18, a: "end" }) + "</g>";
    s += "<g data-k='cheque'>" + fleche(P, V.berlin, V.vienne, { coul: "var(--acier)", courbe: 0.3 }) + etiq(C, [14.2, 50.6], "« chèque en blanc »", { a: "start", dx: 14, cl: "lbl" }) + "</g>";
    s += "<g data-k='ultim'>" + fleche(P, V.vienne, V.belgrade, { courbe: -0.25 }) + etiq(C, [19.5, 46.9], "ultimatum (23 juil.)", { a: "start", dx: 10 }) + "</g>";
    s += "<g data-k='g-serbie'>" + point(P, V.belgrade, "pt-a", 7) + etiq(C, V.belgrade, "guerre à la Serbie (28 juil.)", { a: "start", dx: 10, dy: 4 }) + "</g>";
    s += "<g data-k='mob-ru'>" + point(P, V.petersbourg, "pt-a", 8) + etiq(C, V.petersbourg, "mobilisation générale russe (30 juil.)", { a: "end", dx: -12, dy: 4 }) + fleche(P, V.petersbourg, V.belgrade, { coul: "var(--acier)", courbe: 0.2, retrait: 9 }) + "</g>";
    s += "<g data-k='g-russie'>" + fleche(P, V.berlin, V.petersbourg, { courbe: -0.15, retrait: 10 }) + etiq(C, [22.5, 57.6], "guerre à la Russie (1er août)", { a: "middle", dy: -8 }) + "</g>";
    s += "<g data-k='g-france'>" + fleche(P, V.berlin, V.paris, { courbe: 0.2 }) + point(P, V.paris, "pt-a", 7) + etiq(C, V.paris, "guerre à la France (3 août)", { a: "end", dx: -10, dy: 16 }) + "</g>";
    s += "<g data-k='belgique'>" + fleche(P, [6.9, 50.9], V.bruxelles, { courbe: 0, retrait: 8 }) + point(P, V.bruxelles, "pt-a", 6) + etiq(C, V.bruxelles, "Belgique envahie (4 août)", { a: "end", dx: -10, dy: -8 }) + "</g>";
    s += "<g data-k='g-ru'>" + fleche(P, V.londres, V.berlin, { coul: "var(--acier)", courbe: -0.2, retrait: 9 }) + point(P, V.londres, "pt-b", 7) + etiq(C, V.londres, "Royaume-Uni en guerre (4 août)", { a: "end", dx: -10, dy: -8 }) + "</g>";
    s += "<g data-k='fischer'><circle cx='" + P(V.berlin)[0] + "' cy='" + P(V.berlin)[1] + "' r='26' fill='none' stroke='var(--rouge)' stroke-width='3'/>" + etiq(C, V.berlin, "Fischer (1961) : Berlin a voulu la guerre", { cl: "lbl-f", a: "end", dx: -30, dy: -40 }) + "</g>";
    s += "<g data-k='clark'>";
    ["vienne", "berlin", "belgrade", "petersbourg", "paris", "londres"].forEach(k => { const [x, y] = P(V[k]); s += "<circle cx='" + x + "' cy='" + y + "' r='18' fill='none' stroke='var(--acier)' stroke-width='2.5' stroke-dasharray='4 3'/>"; });
    s += etiq(C, [3, 40.5], "Clark (2012) : des « somnambules »", { cl: "lbl-f", a: "middle" }) + etiq(C, [3, 39], "dans toutes les capitales", { cl: "lbl", a: "middle" }) + "</g>";
    const deco = etiq(C, [25, 52.5], "EMPIRE RUSSE", { cl: "k-pays", a: "middle" }) + "<text x='12' y='610' class='k-note'>frontières actuelles (fond de carte)</text>";
    OUT.anims.t3juillet = { w: WC, h: HC, fond: fondC, calques: deco + s };
  }

  /* ===== Animation : du génocide aux lieux de mémoire (Europe) ===== */
  {
    const P = C.P;
    const CM = { chelmno: [18.73, 52.15], belzec: [23.46, 50.38], sobibor: [23.59, 51.45], treblinka: [22.05, 52.63], auschwitz: [19.18, 50.03], majdanek: [22.6, 51.22] };
    const L = { drancy: [2.45, 48.92], mb: [-0.15, 47.13], paris: [2.356, 48.855], berlin: [13.38, 52.51], jerusalem: [35.18, 31.77], izieu: [5.64, 45.65] };
    let s = "<g data-k='centres'>";
    Object.keys(CM).forEach(k => { s += point(P, CM[k], "pt-a", 6); });
    s += etiq(C, CM.chelmno, "Chelmno", { a: "end", dx: -9 }) + etiq(C, CM.treblinka, "Treblinka", { a: "start", dx: 9, dy: -2 }) + etiq(C, CM.sobibor, "Sobibor", { a: "start", dx: 9, dy: 2 }) +
      etiq(C, CM.majdanek, "Majdanek", { a: "end", dx: -9, dy: 4 }) + etiq(C, CM.belzec, "Belzec", { a: "start", dx: 9, dy: 6 }) + etiq(C, CM.auschwitz, "Auschwitz-Birkenau", { a: "end", dx: -9, dy: 12 }) + "</g>";
    s += "<g data-k='depor'>" + fleche(P, L.drancy, CM.auschwitz, { courbe: -0.12, retrait: 8 }) + point(P, L.drancy, "pt-a", 5) + etiq(C, L.drancy, "Drancy", { a: "start", dx: 8, dy: -6 }) +
      point(P, L.mb, "pt-b", 5) + etiq(C, L.mb, "Montreuil-Bellay", { a: "end", dx: -8, dy: 4 }) + "</g>";
    s += "<g data-k='m1947'>" + "<circle cx='" + P(CM.auschwitz)[0] + "' cy='" + P(CM.auschwitz)[1] + "' r='14' fill='none' stroke='var(--ok)' stroke-width='3'/>" + etiq(C, CM.auschwitz, "musée (1947)", { a: "start", dx: 16, dy: 18, cl: "lbl" }) + "</g>";
    s += "<g data-k='m1953'><rect x='640' y='588' width='252' height='24' rx='4' fill='var(--papier)' opacity='.85'/><circle cx='654' cy='600' r='7' class='pt-b'/><text x='668' y='604' class='lbl'>Yad Vashem, Jérusalem (1953) ↘</text></g>";
    s += "<g data-k='m1956'>" + point(P, L.paris, "pt-b", 6) + etiq(C, L.paris, "Mémorial (1956 ; 2005)", { a: "end", dx: -9, dy: -6 }) + "</g>";
    s += "<g data-k='m1994'>" + point(P, L.izieu, "pt-b", 5) + etiq(C, L.izieu, "Izieu (1994)", { a: "start", dx: 8, dy: 6 }) + "</g>";
    s += "<g data-k='m2005'>" + point(P, L.berlin, "pt-b", 7) + etiq(C, L.berlin, "Berlin : mémorial (2005)", { a: "end", dx: -10, dy: -8 }) + "</g>";
    s += "<g data-k='m2012'><circle cx='" + P(L.berlin)[0] + "' cy='" + P(L.berlin)[1] + "' r='13' fill='none' stroke='var(--ok)' stroke-width='3'/>" + etiq(C, L.berlin, "Sinti et Roms (2012)", { a: "end", dx: -14, dy: 22 }) +
      "<circle cx='" + P(L.drancy)[0] + "' cy='" + P(L.drancy)[1] + "' r='11' fill='none' stroke='var(--ok)' stroke-width='3'/></g>";
    s += "<g data-k='m2016'><circle cx='" + P(L.mb)[0] + "' cy='" + P(L.mb)[1] + "' r='12' fill='none' stroke='var(--ok)' stroke-width='3'/>" + etiq(C, L.mb, "reconnaissance (2016)", { a: "end", dx: -8, dy: 20 }) + "</g>";
    OUT.anims.t3lieux = { w: WC, h: HC, fond: fondC, calques: s };
  }

  /* ===== Animation : la justice pénale internationale, 1945-2016 (monde) ===== */
  {
    const P = M.P;
    const T = {
      nuremberg: [11.08, 49.45], tokyo: [139.69, 35.69], haye: [4.3, 52.08], arusha: [36.68, -3.37], kigali: [30.06, -1.95], freetown: [-13.23, 8.48],
      phnom: [104.92, 11.56], dakar: [-17.44, 14.69], srebrenica: [19.3, 44.1], kampala: [32.58, 0.35]
    };
    const g = (k, ll, cl, r, txt, o) => "<g data-k='" + k + "'>" + point(P, ll, cl, r) + etiq(M, ll, txt, o) + "</g>";
    let s = "";
    s += g("nur", T.nuremberg, "pt-a", 6, "Nuremberg 1945", { a: "start", dx: 8, dy: 12 });
    s += g("tok", T.tokyo, "pt-a", 6, "Tokyo 1946", { a: "end", dx: -8, dy: 4 });
    s += g("tpiy", T.haye, "pt-a", 7, "TPIY, La Haye 1993", { a: "end", dx: -9, dy: -6 });
    s += "<g data-k='srebre'>" + point(P, T.srebrenica, "pt-b", 4) + etiq(M, T.srebrenica, "Srebrenica 1995", { a: "start", dx: 7, dy: 10 }) + "</g>";
    s += g("tpir", T.arusha, "pt-a", 7, "TPIR, Arusha 1994", { a: "start", dx: 9, dy: 8 });
    s += g("gacaca", T.kigali, "pt-b", 5, "gacaca 2002-2012", { a: "end", dx: -8, dy: -2 });
    s += g("tssl", T.freetown, "pt-a", 6, "Sierra Leone 2002", { a: "end", dx: -8, dy: 4 });
    s += "<g data-k='cpi'><circle cx='" + P(T.haye)[0] + "' cy='" + P(T.haye)[1] + "' r='14' fill='none' stroke='var(--rouge)' stroke-width='3'/>" + etiq(M, T.haye, "CPI 2002", { cl: "lbl-f", a: "start", dx: 16, dy: -12 }) + "</g>";
    s += g("cetc", T.phnom, "pt-a", 6, "Cambodge 2006", { a: "start", dx: 8, dy: 4 });
    s += g("cae", T.dakar, "pt-a", 6, "Dakar 2013-2016", { a: "end", dx: -8, dy: -6 });
    OUT.anims.t3tribunaux = { w: WM, h: HM, vb: [300, 10, 600, 285], fond: "monde", calques: s };
  }

  /* ===== Carte interactive : juger les crimes de masse ===== */
  {
    const pt = (c, ll, n, a, t, d) => { const [x, y] = M.P(ll); return { c, x, y, n, a, t, d }; };
    const pts = [
      pt("inter", [11.08, 49.45], "Nuremberg", "start", "Nuremberg : le Tribunal militaire international (1945-1946)", "Créé par l'accord de Londres du 8 août 1945. Procès des 20 novembre 1945 au 1er octobre 1946 : 22 accusés jugés, 12 condamnations à mort, 3 acquittements. Première définition du crime contre l'humanité (article 6 c du statut)."),
      pt("inter", [139.69, 35.69], "Tokyo", "end", "Tokyo : le Tribunal militaire international pour l'Extrême-Orient (1946-1948)", "Juge 28 dirigeants japonais ; sept sont condamnés à mort. L'empereur Hirohito n'est pas poursuivi, par décision américaine."),
      pt("inter", [4.3, 52.08], "La Haye", "end", "La Haye : TPIY (1993-2017) et Cour pénale internationale (depuis 2002)", "Le TPIY, créé par la résolution 827 du Conseil de sécurité (25 mai 1993), a mis en accusation 161 personnes. La CPI, créée par le statut de Rome (17 juillet 1998), est permanente et siège aussi à La Haye depuis le 1er juillet 2002."),
      pt("inter", [36.68, -3.37], "Arusha", "start", "Arusha (Tanzanie) : TPIR (1994-2015)", "Créé par la résolution 955 du 8 novembre 1994. Le 2 septembre 1998, le jugement Akayesu est la première condamnation pour génocide prononcée par une juridiction internationale. Fermé le 31 décembre 2015."),
      pt("inter", [-13.23, 8.48], "Freetown", "end", "Freetown : Tribunal spécial pour la Sierra Leone (2002-2013)", "Tribunal mixte (juges sierra-léonais et internationaux). Il condamne en 2012 l'ancien président libérien Charles Taylor à 50 ans de prison : premier ancien chef d'État condamné par une juridiction internationale depuis Nuremberg."),
      pt("inter", [104.92, 11.56], "Phnom Penh", "start", "Phnom Penh : Chambres extraordinaires au sein des tribunaux cambodgiens (2006-2022)", "Tribunal mixte pour juger les crimes des Khmers rouges (1975-1979, environ 1,7 million de morts). Le 16 novembre 2018, Nuon Chea et Khieu Samphan sont condamnés pour génocide envers les Vietnamiens (et les Chams pour Nuon Chea)."),
      pt("inter", [-17.44, 14.69], "Dakar", "end", "Dakar : Chambres africaines extraordinaires (2013-2017)", "Créées par le Sénégal et l'Union africaine pour juger l'ancien président tchadien Hissène Habré, condamné le 30 mai 2016 à la perpétuité pour crimes contre l'humanité : un État africain juge un ancien chef d'État africain."),
      pt("local", [30.06, -1.95], "Kigali", "start", "Rwanda : les tribunaux gacaca (2002-2012)", "Plus de 12 000 juridictions populaires installées dans les collines jugent près de deux millions d'affaires liées au génocide des Tutsis, avant leur clôture officielle le 18 juin 2012."),
      pt("local", [4.84, 45.76], "Lyon", "end", "Lyon : le procès Barbie (1987)", "Klaus Barbie, chef de la Gestapo de Lyon, extradé de Bolivie en 1983, est condamné le 4 juillet 1987 à la réclusion à perpétuité : premier procès pour crime contre l'humanité en France."),
      pt("local", [-0.58, 44.84], "Bordeaux", "end", "Bordeaux : le procès Papon (1997-1998)", "Maurice Papon, ancien secrétaire général de la préfecture de la Gironde sous l'Occupation, est condamné le 2 avril 1998 à dix ans de réclusion pour complicité de crimes contre l'humanité."),
      pt("local", [35.21, 31.77], "Jérusalem", "start", "Jérusalem : le procès Eichmann (1961)", "Adolf Eichmann, organisateur des déportations, enlevé en Argentine en mai 1960, est jugé à partir du 11 avril 1961, condamné à mort le 15 décembre 1961 et exécuté en 1962. Le procès fait entendre plus d'une centaine de témoins."),
      pt("crime", [19.3, 44.1], "Srebrenica", "start", "Srebrenica (Bosnie-Herzégovine), juillet 1995", "Environ 8 000 hommes et garçons bosniaques musulmans sont tués par les forces serbes de Bosnie. Le TPIY qualifie ces crimes de génocide (Krstić, 2001 et 2004) ; la Cour internationale de justice le confirme le 26 février 2007. Non loin, Sarajevo subit le plus long siège d'une capitale dans l'histoire contemporaine (5 avril 1992-29 février 1996)."),
      pt("crime", [29.74, -2.6], "Butare", "end", "Rwanda, avril-juillet 1994", "Le génocide des Tutsis fait environ 800 000 morts selon l'ONU (plus d'un million selon le recensement des autorités rwandaises) en une centaine de jours, à partir du 7 avril 1994."),
      pt("crime", [-3.0, 16.77], "Tombouctou", "end", "Tombouctou (Mali), 2012", "La destruction de mausolées classés au patrimoine mondial est jugée comme crime de guerre par la CPI (affaire Al Mahdi, 27 septembre 2016) : voir le thème 4.")
    ];
    const meta = { t: "Juger les crimes de masse : tribunaux et lieux", c: { inter: ["Juridictions internationales ou mixtes", "#B3241B"], local: ["Justice nationale ou locale", "#2D5675"], crime: ["Lieux de crimes de masse jugés", "#B07A1E"] } };
    const R = { "La Haye": ["end", -6], Nuremberg: ["start", -6], Lyon: ["start", 10], Bordeaux: ["end", 4], Srebrenica: ["start", 12], Butare: ["end", 8], Kigali: ["start", -6] };
    pts.forEach(p => { if (R[p.n]) { p.a = R[p.n][0]; p.dy = R[p.n][1]; } });
    OUT.cartes.justice = { w: WM, h: HM, fond: "monde", deco: "", pts, meta, vb: [340, 30, 600, 340] };
  }

  /* ===== Carte interactive : lieux de mémoire des conflits (Europe) ===== */
  {
    const pt = (c, ll, n, a, t, d) => { const [x, y] = E.P(ll); return { c, x, y, n, a, t, d }; };
    const pts = [
      pt("gm", [5.43, 49.21], "Douaumont", "start", "Ossuaire de Douaumont (Verdun)", "Inauguré en 1932, il abrite les restes d'environ 130 000 soldats inconnus. Le 22 septembre 1984, François Mitterrand et Helmut Kohl s'y tiennent la main : un geste de réconciliation franco-allemande."),
      pt("gm", [2.72, 50.4], "Lorette", "end", "Anneau de la Mémoire (Ablain-Saint-Nazaire)", "Inauguré le 11 novembre 2014 : 579 606 noms de soldats morts dans le Nord-Pas-de-Calais, classés par ordre alphabétique sans distinction de nationalité ni de grade. Inscrit au patrimoine mondial en 2023 avec 138 autres sites funéraires et mémoriels du front Ouest."),
      pt("gm", [7.15, 47.86], "Hartmannswillerkopf", "start", "Hartmannswillerkopf (Alsace)", "Le 3 août 2014, cent ans après la déclaration de guerre de l'Allemagne à la France, les présidents Hollande et Gauck y posent la première pierre d'un historial franco-allemand, inauguré par Emmanuel Macron et Frank-Walter Steinmeier le 10 novembre 2017."),
      pt("gm", [18.41, 43.86], "Sarajevo", "start", "Sarajevo", "Lieu de l'attentat du 28 juin 1914. La mémoire de Gavrilo Princip divise : héros de la libération nationale pour beaucoup de Serbes, terroriste pour d'autres."),
      pt("alg", [3.06, 36.75], "Alger", "end", "Alger : le Maqam Echahid", "Mémorial du Martyr inauguré le 5 juillet 1982, vingtième anniversaire de l'indépendance : la mémoire officielle algérienne célèbre « un million et demi de martyrs »."),
      pt("alg", [5.41, 36.19], "Sétif", "start", "Sétif et Guelma, mai 1945", "La répression des émeutes du 8 mai 1945 fait des milliers de morts algériens (bilans très discutés). Pour beaucoup d'historiens, c'est l'une des racines de la guerre d'Algérie."),
      pt("alg", [2.347, 48.853], "Paris", "end", "Paris : le pont Saint-Michel", "Une plaque y rappelle depuis 2001 la répression de la manifestation d'Algériens du 17 octobre 1961. Le 17 octobre 2012, François Hollande reconnaît « avec lucidité » une « sanglante répression »."),
      pt("alg", [2.87, 42.77], "Rivesaltes", "start", "Mémorial du camp de Rivesaltes", "Ouvert en 2015 : le camp a interné des républicains espagnols, des Juifs et des Tsiganes (1941-1942), puis des harkis et leurs familles après 1962. Un lieu de mémoires multiples."),
      pt("shoah", [19.18, 50.03], "Auschwitz", "start", "Auschwitz-Birkenau (Pologne)", "Environ 1,1 million de personnes y sont assassinées, dont environ un million de Juifs et environ 21 000 Roms et Sinti. Musée d'État depuis 1947, inscrit au patrimoine mondial en 1979. La libération du camp, le 27 janvier 1945, est devenue la Journée internationale dédiée à la mémoire des victimes de l'Holocauste (ONU, 2005)."),
      pt("shoah", [22.05, 52.63], "Treblinka", "start", "Treblinka (Pologne)", "Centre de mise à mort où environ 800 000 à 900 000 Juifs sont assassinés entre juillet 1942 et 1943. Il n'en reste presque rien : le mémorial est fait de pierres dressées."),
      pt("shoah", [2.356, 48.855], "Mémorial de la Shoah", "start", "Mémorial de la Shoah (Paris)", "Héritier du Centre de documentation juive contemporaine, créé dans la clandestinité en 1943, et du Mémorial du martyr juif inconnu (1956). Inauguré sous ce nom le 27 janvier 2005, avec le mur des Noms de 76 000 Juifs déportés de France."),
      pt("shoah", [2.45, 48.92], "Drancy", "start", "Drancy", "Camp de transit d'où partent la plupart des convois vers Auschwitz (1942-1944). Mémorial ouvert en face de la cité de la Muette le 21 septembre 2012."),
      pt("shoah", [5.64, 45.65], "Izieu", "start", "Maison d'Izieu (Ain)", "Le 6 avril 1944, 44 enfants juifs et 7 éducateurs y sont arrêtés sur ordre de Klaus Barbie. Mémorial inauguré le 24 avril 1994."),
      pt("shoah", [13.38, 52.51], "Berlin", "start", "Berlin : mémoriaux du génocide", "Mémorial aux Juifs assassinés d'Europe (2 711 stèles, inauguré le 10 mai 2005) et mémorial aux Sinti et Roms d'Europe assassinés sous le national-socialisme (24 octobre 2012), à côté du Reichstag."),
      pt("shoah", [-0.15, 47.13], "Montreuil-Bellay", "end", "Camp de Montreuil-Bellay (Maine-et-Loire)", "Le plus grand camp d'internement des « nomades » en France (1941-1945). Le 29 octobre 2016, François Hollande y reconnaît la responsabilité de la République dans l'internement des Tsiganes."),
      pt("shoah", [35.18, 31.77], "Yad Vashem", "end", "Yad Vashem (Jérusalem)", "Institut et mémorial créé par une loi israélienne du 19 août 1953. Il honore aussi les « Justes parmi les nations », non-Juifs qui ont sauvé des Juifs au péril de leur vie.")
    ];
    const R = { Drancy: ["end", -9], "Mémorial de la Shoah": ["start", 16], Lorette: ["end", -4], Paris: ["end", 6], Douaumont: ["start", -6] };
    pts.forEach(p => { if (R[p.n]) { p.a = R[p.n][0]; p.dy = R[p.n][1]; } });
    const meta = { t: "Lieux de mémoire des conflits du XXe siècle", c: { gm: ["Première Guerre mondiale", "#2D5675"], alg: ["Guerre d'Algérie", "#B07A1E"], shoah: ["Génocide des Juifs et des Tsiganes", "#B3241B"] } };
    OUT.cartes.memoire = { w: WE, h: HE, fond: fondE, deco: "", pts, meta, vb: [60, 60, 800, 560] };
  }
};
