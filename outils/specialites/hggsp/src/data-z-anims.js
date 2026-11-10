/* ===== Deuxième animation explicative des chapitres qui n'en avaient qu'une (contrôle visuel, 10/11/2026) =====
   Chargé après tous les fichiers de chapitres (ordre alphabétique de build.py) : chaque animation est rangée dans
   la section du chapitre qu'elle illustre (fonction ranger). Scènes cartographiques : cartes-z.js (« carte:nom »).
   Tous les faits viennent du cours du chapitre concerné. */
(function () {
  function t(x, y, s, cl, a, style) { return "<text x='" + x + "' y='" + y + "' class='" + (cl || "lbl") + "'" + (a ? " text-anchor='" + a + "'" : "") + (style ? " style='" + style + "'" : "") + ">" + s + "</text>"; }
  function k(id, inner) { return "<g data-k='" + id + "'>" + inner + "</g>"; }
  function rect(x, y, w, h, fill, extra) { return "<rect x='" + x + "' y='" + y + "' width='" + w + "' height='" + h + "' fill='" + fill + "'" + (extra || "") + "/>"; }
  function ligne(x1, y1, x2, y2, coul, extra) { return "<path d='M" + x1 + "," + y1 + "L" + x2 + "," + y2 + "' stroke='" + (coul || "var(--encre2)") + "' fill='none'" + (extra || "") + "/>"; }
  function trace(id, d, coul, w, extra) { return "<path " + (id ? "data-k='" + id + "' " : "") + "class='trace' pathLength='1' d='" + d + "' fill='none' stroke='" + (coul || "var(--rouge)") + "' stroke-width='" + (w || 3) + "' stroke-linecap='round' stroke-linejoin='round'" + (extra || "") + "/>"; }
  function pt(x, y, cl, r) { return "<circle cx='" + x + "' cy='" + y + "' r='" + (r || 6) + "' class='" + (cl || "pt-a") + "'/>"; }
  function boite(x, y, w, h, titre, coul, sous) {
    return rect(x, y, w, h, "var(--papier)", " rx='6' stroke='" + (coul || "var(--encre)") + "' stroke-width='1.8'") +
      t(x + w / 2, y + (sous ? h / 2 - 2 : h / 2 + 4), titre, "lbl-f", "middle", "font-size:12px" + (coul ? ";fill:" + coul : "")) + (sous ? t(x + w / 2, y + h / 2 + 13, sous, "lbl", "middle", "font-size:10.5px") : "");
  }
  /* pointe de flèche simple en (x, y), orientée selon l'angle a (degrés) */
  function pointe(x, y, a, coul) { return "<path d='M0,0L-9,-4.5L-9,4.5Z' fill='" + (coul || "var(--rouge)") + "' transform='translate(" + x + "," + y + ") rotate(" + a + ")'/>"; }
  /* range l'animation dans la section n (de 1) du chapitre */
  function ranger(ch, n, nom) {
    var s = CHAPS[ch] && CHAPS[ch].secs[n - 1];
    if (!s) return;
    s.viz = s.viz ? (Array.isArray(s.viz) ? s.viz : [s.viz]).concat(["anim:" + nom]) : "anim:" + nom;
  }

  /* ====================== THÈME 1 ====================== */
  /* Du fond des océans à l'orbite géostationnaire (échelle logarithmique) */
  (function () {
    function yH(km) { return Math.round((194 - (Math.log(km) / Math.LN10 - 1) * 46.5) * 10) / 10; }
    function yP(m) { return Math.round((226 + (Math.log(m) / Math.LN10 - 2) * 55) * 10) / 10; }
    var s = rect(0, 0, 640, 210, "var(--papier2)") + rect(0, 210, 640, 170, "var(--k-mer)");
    s += "<path d='M0 210q20 -5 40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0' fill='none' stroke='var(--acier)' stroke-width='2'/>";
    s += ligne(70, 18, 70, 372, "var(--encre2)", " stroke-width='1.5'");
    [10, 100, 1000, 10000].forEach(function (v) { s += ligne(64, yH(v), 70, yH(v)) + t(60, yH(v) + 4, (v >= 1000 ? (v / 1000) + " 000" : v) + " km", "sch-pt", "end"); });
    [100, 1000, 10000].forEach(function (v) { s += ligne(64, yP(v), 70, yP(v)) + t(60, yP(v) + 4, (v >= 1000 ? (v / 1000) + " 000" : v) + " m", "sch-pt", "end"); });
    s += t(630, 14, "échelle logarithmique : chaque graduation × 10", "sch-pt", "end");
    s += t(630, 200, "AIR ET ESPACE ↑", "sch-pt", "end") + t(630, 226, "OCÉAN ↓", "sch-pt", "end");
    s += k("surf", t(80, 205, "niveau de la mer", "lbl"));
    s += k("lum", rect(70, yP(200), 570, 380 - yP(200), "var(--encre)", " opacity='.08'") + ligne(70, yP(200), 600, yP(200), "var(--acier)", " stroke-dasharray='5 4'") + t(80, yP(200) - 4, "200 m : presque plus de lumière", "lbl"));
    s += k("moy", ligne(70, yP(3700), 600, yP(3700), "var(--acier)", " stroke-dasharray='5 4'") + t(80, yP(3700) - 4, "≈ 3 700 m : profondeur moyenne", "lbl"));
    s += k("chal", trace("", "M330,212V" + (yP(10900) - 6), "var(--acier)", 2.5, " stroke-dasharray='1'") + pt(330, yP(10900), "pt-b", 6) + t(342, yP(10900) + 4, "≈ 10 900 m : Challenger Deep (1960)", "lbl"));
    s += k("lim", ligne(70, yH(80), 600, yH(80), "var(--rouge)", " stroke-dasharray='4 3'") + ligne(70, yH(100), 600, yH(100), "var(--rouge)", " stroke-width='2'") +
      t(80, yH(100) - 6, "100 km : ligne de Kármán (FAI)", "lbl-f", null, "font-size:12px") + t(80, yH(80) + 14, "80 km : armée de l'air américaine", "lbl") + t(600, yH(80) + 14, "aucun traité ne fixe la limite", "lbl", "end"));
    s += k("v2", trace("", "M420,210Q470," + (2 * yH(176) - 210) + " 520,210", "var(--rouge)", 2.5) + pt(470, yH(176), "pt-a", 5) + t(480, yH(176) - 6, "V2 (1944) : ≈ 176 km", "lbl"));
    s += k("leo", rect(70, yH(2000), 570, yH(200) - yH(2000), "var(--acier)", " opacity='.16'") + t(80, (yH(2000) + yH(200)) / 2 + 4, "200 à 2 000 km : orbite basse (stations, Starlink)", "lbl"));
    s += k("meo", ligne(70, yH(20000), 600, yH(20000), "var(--acier)", " stroke-width='2'") + t(80, yH(20000) + 14, "≈ 20 000 km : orbite moyenne (GPS, Galileo, Beidou)", "lbl"));
    s += k("geo", ligne(70, yH(35786), 600, yH(35786), "var(--acier)", " stroke-width='3'") + t(80, yH(35786) - 5, "35 786 km : orbite géostationnaire", "lbl-f", null, "font-size:12px"));
    ANIMS.t1alt = {
      titre: "Du fond des océans à l'orbite géostationnaire : deux milieux extrêmes",
      scene: { w: 640, h: 380, svg: s },
      etapes: [
        { date: "0 m", titre: "Partir du niveau de la mer", texte: "Vers le bas, l'océan ; vers le haut, l'air puis l'espace. L'échelle est logarithmique : sinon, l'orbite géostationnaire serait des milliers de fois plus loin que le fond des océans.", montre: ["surf"] },
        { date: "− 200 m", titre: "La nuit commence vite", texte: "La lumière disparaît presque entièrement au-delà de 200 mètres, et la pression augmente d'environ 1 bar tous les 10 mètres.", montre: ["lum"], accent: ["lum"] },
        { date: "− 3 700 m", titre: "La profondeur moyenne", texte: "Les océans font en moyenne environ 3 700 mètres de profondeur : un milieu où l'être humain ne survit qu'enfermé dans une machine.", montre: ["moy"], accent: ["moy"] },
        { date: "23 janv. 1960", titre: "Le point le plus profond", texte: "Challenger Deep, dans la fosse des Mariannes (environ 10 900 m), n'est atteint qu'en 1960 par le bathyscaphe Trieste, puis par James Cameron seul en 2012.", montre: ["chal"], accent: ["chal"] },
        { date: "80-100 km", titre: "Où commence l'espace ?", texte: "Aucun traité ne fixe la limite. La convention la plus utilisée est la ligne de Kármán (100 km, Fédération aéronautique internationale) ; l'armée de l'air américaine retient 80 km.", montre: ["lim"], accent: ["lim"] },
        { date: "20 juin 1944", titre: "Une conquête née d'une arme", texte: "Le premier objet humain à franchir les 100 km est un missile allemand V2, qui monte à environ 176 km.", montre: ["v2"], accent: ["v2"] },
        { date: "Depuis 1957", titre: "L'orbite basse", texte: "De 200 à 2 000 km : stations, satellites d'observation, constellations Internet. Starlink compte plus de 10 000 satellites en mars 2026.", montre: ["leo"], accent: ["leo"] },
        { date: "≈ 20 000 km", titre: "L'orbite moyenne", texte: "Vers 20 000 km tournent les satellites de positionnement : GPS américain, Galileo européen, Beidou chinois.", montre: ["meo"], accent: ["meo"] },
        { date: "35 786 km", titre: "L'orbite géostationnaire", texte: "Un satellite y paraît immobile au-dessus de l'équateur : télécommunications et météo. Une orbite très convoitée, dont les positions se partagent entre États.", montre: ["geo"], accent: ["geo"] }
      ],
      source: "Schéma du site (échelle logarithmique). Chiffres du cours : profondeurs, ligne de Kármán, orbites."
    };
    ranger("t1-intro", 1, "t1alt");
  })();

  /* Les tirs antisatellites : démontrer une capacité, produire des débris */
  (function () {
    var cx = 320, cy = 880, RO = 780, RT = 700;
    function sur(r, th) { var a = th * Math.PI / 180; return [Math.round((cx + r * Math.sin(a)) * 10) / 10, Math.round((cy - r * Math.cos(a)) * 10) / 10]; }
    var graine = 7;
    function alea() { graine = (graine * 9301 + 49297) % 233280; return graine / 233280; }
    function debris(th, n, ec) { var s = ""; for (var i = 0; i < n; i++) { var p = sur(RO + (alea() - 0.5) * 22, th + (alea() - 0.5) * ec); s += "<circle cx='" + p[0] + "' cy='" + p[1] + "' r='1.9' fill='var(--rouge)'/>"; } return s; }
    var s = rect(0, 0, 640, 340, "var(--papier2)");
    s += "<circle cx='" + cx + "' cy='" + cy + "' r='" + RO + "' fill='none' stroke='var(--acier)' stroke-width='1.2' stroke-dasharray='5 5'/>";
    s += "<circle cx='" + cx + "' cy='" + cy + "' r='" + RT + "' fill='var(--k-terre)' stroke='var(--k-front)' stroke-width='1.5'/>";
    s += t(320, 250, "TERRE", "k-pays", "middle") + t(620, 330, "schéma sans échelle", "sch-pt", "end");
    var tirs = [["cn", -18, "2007 · Chine", 18, 9], ["us", -6, "2008 · États-Unis", 6, 5], ["in", 6, "2019 · Inde", 10, 6], ["ru", 18, "2021 · Russie", 16, 9]];
    tirs.forEach(function (x) {
      var sat = sur(RO, x[1]), sol = sur(RT, x[1]);
      s += k(x[0] + "sat", "<rect x='" + (sat[0] - 6) + "' y='" + (sat[1] - 4) + "' width='12' height='8' fill='var(--acier)' stroke='var(--k-halo)'/><path d='M" + (sat[0] - 15) + "," + sat[1] + "H" + (sat[0] + 15) + "' stroke='var(--acier)' stroke-width='2'/>");
      s += k(x[0], trace("", "M" + sol[0] + "," + sol[1] + "L" + sat[0] + "," + (sat[1] + 6), "var(--rouge)", 2.2) + pt(sol[0], sol[1], "pt-a", 4) + debris(x[1], x[3], x[4]) + t(sat[0], sat[1] - 24, x[2], "lbl-f", "middle", "font-size:12px"));
    });
    var tout = ""; for (var i = 0; i < 46; i++) { var p = sur(RO + (alea() - 0.5) * 26, -24 + i * 48 / 45 + (alea() - 0.5)); tout += "<circle cx='" + p[0] + "' cy='" + p[1] + "' r='1.7' fill='var(--rouge)' opacity='.75'/>"; }
    s += k("kessler", tout + t(320, 40, "risque de réaction en chaîne de collisions (Kessler, 1978)", "lbl-f", "middle", "font-size:12px"));
    s += k("forces", rect(20, 262, 250, 50, "var(--papier)", " rx='6' stroke='var(--encre)'") + t(32, 282, "2019 : Space Force (États-Unis),", "lbl") + t(32, 300, "Commandement de l'espace (France)", "lbl"));
    ANIMS.t1asat = {
      titre: "Les tirs antisatellites : montrer sa force, polluer l'orbite",
      scene: { w: 640, h: 340, svg: s },
      etapes: [
        { date: "Aujourd'hui", titre: "Des armées dépendantes de l'espace", texte: "Renseignement, communications, navigation, guidage : les armées ne peuvent plus combattre sans satellites. Celui qui aveugle les satellites adverses prend l'avantage.", montre: ["cnsat", "ussat", "insat", "rusat"] },
        { date: "11 janv. 2007", titre: "La Chine détruit Fengyun-1C", texte: "Un missile tiré du sol pulvérise un vieux satellite météo chinois : plus de 3 000 débris suivis, qui menacent tous les satellites, y compris chinois.", montre: ["cn"], cache: ["cnsat"], accent: ["cn"] },
        { date: "Févr. 2008", titre: "Les États-Unis répondent", texte: "Washington abat à son tour un de ses satellites : la démonstration de capacité devient une rivalité.", montre: ["us"], cache: ["ussat"], accent: ["us"] },
        { date: "27 mars 2019", titre: "L'Inde : mission Shakti", texte: "L'Inde rejoint le club des puissances capables de détruire un satellite depuis le sol.", montre: ["in"], cache: ["insat"], accent: ["in"] },
        { date: "15 nov. 2021", titre: "La Russie et Kosmos 1408", texte: "Le nuage de débris oblige l'équipage de la Station spatiale internationale à se mettre à l'abri : le tireur menace aussi ses propres astronautes.", montre: ["ru"], cache: ["rusat"], accent: ["ru"] },
        { date: "Depuis 1978", titre: "Le syndrome de Kessler", texte: "Les débris se dispersent le long de l'orbite. Donald Kessler a décrit dès 1978 le risque d'une réaction en chaîne de collisions qui rendrait certaines orbites inutilisables.", montre: ["kessler"], accent: ["kessler"] },
        { date: "2019", titre: "L'espace, un milieu de conflictualité", texte: "Les États créent des forces spatiales : Space Force américaine (20 décembre 2019), Commandement de l'espace français (3 septembre 2019).", montre: ["forces"], accent: ["forces"] }
      ],
      source: "Schéma du site, sans échelle ; positions des tirs symboliques. Dates et chiffres du cours."
    };
    ranger("t1-a1", 3, "t1asat");
  })();

  /* Le traité BBNJ : de la négociation à l'entrée en vigueur */
  (function () {
    function X(a) { return Math.round(60 + (a - 2022.5) * 145); }
    var s = rect(0, 0, 640, 310, "var(--papier2)");
    s += ligne(60, 215, 620, 215, "var(--encre2)", " stroke-width='1.5'");
    [2023, 2024, 2025, 2026].forEach(function (a) { s += ligne(X(a), 210, X(a), 220) + t(X(a), 204, a, "sch-pt", "middle"); });
    s += t(60, 110, "ratifications : il en faut 60", "lbl");
    for (var i = 0; i < 60; i++) s += rect(60 + i * 8.4, 117, 7, 18, "none", " stroke='var(--ligne)' stroke-width='1'");
    function cases(a, b) { var r = ""; for (var i = a; i < b; i++) r += rect(60 + i * 8.4, 117, 7, 18, "var(--acier)"); return r; }
    s += k("nego", ligne(14, 232, 186, 232, "var(--encre2)", " stroke-width='3' stroke-dasharray='6 4'") + pointe(194, 232, 0, "var(--encre2)") + t(14, 252, "depuis 2004 : près de vingt ans", "lbl") + t(14, 268, "de discussions", "lbl"));
    s += k("adop", pt(X(2023.47), 215, "pt-b", 6) + t(X(2023.47) + 10, 240, "19 juin 2023 : adopté à l'ONU", "lbl"));
    s += k("sign", pt(X(2023.72), 215, "pt-b", 6) + t(X(2023.72) + 10, 258, "20 sept. 2023 : ouvert à la signature", "lbl"));
    s += k("signe", t(60, 38, "signer n'est pas ratifier : seule la ratification engage l'État", "lbl-f", null, "font-size:12px"));
    s += k("r1", cases(0, 20)) + k("r2", cases(20, 40)) + k("r3", cases(40, 60) + t(570, 131, "✓ 60", "lbl-f", null, "font-size:13px"));
    s += k("r60", pt(X(2025.72), 215, "pt-a", 7) + t(X(2025.72) - 10, 278, "sept. 2025 : 60e ratification", "lbl", "end"));
    s += k("delai", "<path d='M" + X(2025.72) + ",178Q" + Math.round((X(2025.72) + X(2026.04)) / 2) + ",160 " + X(2026.04) + ",178' fill='none' stroke='var(--rouge)' stroke-width='2'/>" + pointe(X(2026.04), 178, 60) + t(Math.round((X(2025.72) + X(2026.04)) / 2), 156, "+ 120 jours", "lbl-f", "middle", "font-size:12px"));
    s += k("vig", pt(X(2026.04), 215, "pt-a", 9) + t(X(2026.04) - 8, 298, "17 janv. 2026 : en vigueur", "lbl-f", "end", "font-size:12px"));
    s += k("fin", t(60, 64, "des aires marines protégées en haute mer deviennent possibles,", "lbl") + t(60, 82, "mais le traité n'engage que les États qui l'ont ratifié", "lbl"));
    ANIMS.t1bbnj = {
      titre: "Le traité BBNJ : comment un traité entre en vigueur",
      scene: { w: 640, h: 310, svg: s },
      etapes: [
        { date: "2004-2023", titre: "Négocier longtemps", texte: "La haute mer couvre près des deux tiers des océans, mais seule une infime partie était protégée. Il faut près de vingt ans de discussions pour aboutir à un texte.", montre: ["nego"] },
        { date: "19 juin 2023", titre: "L'adoption", texte: "L'accord sur la biodiversité marine au-delà des juridictions nationales (BBNJ) est adopté à l'ONU : aires marines protégées en haute mer, partage des ressources génétiques, études d'impact, transferts de technologies.", montre: ["adop"], accent: ["adop"] },
        { date: "20 sept. 2023", titre: "Signer n'est pas ratifier", texte: "Le traité est ouvert à la signature. Mais un État n'est lié que lorsqu'il l'a ratifié, selon ses propres règles (vote du Parlement, par exemple).", montre: ["sign", "signe"], accent: ["signe"] },
        { date: "2024-2025", titre: "Les ratifications s'accumulent", texte: "Le traité prévoit qu'il n'entrera en vigueur qu'après la 60e ratification : la jauge se remplit pays par pays.", montre: ["r1", "r2"], accent: ["r2"] },
        { date: "Sept. 2025", titre: "Le seuil est atteint", texte: "La 60e ratification déclenche le compte à rebours prévu par le traité : 120 jours.", montre: ["r3", "r60", "delai"], accent: ["r60", "delai"] },
        { date: "17 janv. 2026", titre: "L'entrée en vigueur", texte: "Le traité s'applique. Mais il n'engage que ceux qui l'ont ratifié : les grandes puissances maritimes ne le font pas toujours, et les contrôles en haute mer restent difficiles.", montre: ["vig", "fin"], accent: ["vig"] }
      ],
      source: "Schéma du site. Dates du cours ; seuil de 60 ratifications et délai de 120 jours fixés par le traité."
    };
    ranger("t1-a2", 3, "t1bbnj");
  })();

  /* Le « dilemme de Malacca » (carte : cartes-z.js) */
  ANIMS.malacca = {
    titre: "Le « dilemme de Malacca » : contourner un détroit",
    scene: "carte:malacca",
    etapes: [
      { date: "2003", titre: "Une dépendance dangereuse", texte: "Une grande partie du pétrole importé par la Chine vient du golfe Persique et passe par le détroit d'Ormuz, puis par celui de Malacca.", montre: ["route", "routet", "ormuz", "chine", "inde"] },
      { date: "2003", titre: "Le « dilemme de Malacca »", texte: "Le président Hu Jintao s'inquiète : en cas de crise, la marine américaine pourrait bloquer ce détroit étroit et paralyser l'économie chinoise.", montre: ["malacca", "goulot", "blocage"], accent: ["goulot", "blocage"] },
      { date: "Depuis 2013", titre: "Gwadar", texte: "Le port de Gwadar, au Pakistan, est exploité par une société chinoise depuis 2013 : il doit permettre d'acheminer des produits vers la Chine par voie de terre, sans passer par Malacca.", montre: ["gwadar"], accent: ["gwadar"] },
      { date: "2013-2017", titre: "Des tubes à travers la Birmanie", texte: "Un gazoduc (2013) puis un oléoduc (2017) relient le port de Kyaukpyu au Yunnan : une partie des hydrocarbures évite Malacca.", montre: ["tubes", "kyauk", "kunming"], accent: ["tubes"] },
      { date: "Déc. 2017", titre: "Hambantota", texte: "Le Sri Lanka, endetté, concède son port de Hambantota pour 99 ans à une société chinoise : un exemple du « collier de perles » dénoncé par les Américains.", montre: ["hamb"], accent: ["hamb"] },
      { date: "1er août 2017", titre: "Une base militaire à Djibouti", texte: "La Chine ouvre à Djibouti sa première base militaire à l'étranger, au débouché du détroit de Bab el-Mandeb : protéger les routes du commerce, c'est aussi projeter sa puissance.", montre: ["djib"], accent: ["djib"] }
    ],
    source: "Fond Natural Earth ; trajet schématique, positions approximatives. Faits du cours (objet de travail conclusif et carte « Les océans, espaces de puissance »)."
  };
  ranger("t1-otc", 2, "malacca");

  /* ====================== THÈME 2 ====================== */
  /* Comment finit un conflit ? */
  (function () {
    var s = rect(0, 0, 640, 360, "var(--papier2)");
    s += k("conflit", boite(14, 150, 132, 54, "CONFLIT ARMÉ", "var(--rouge)", "États, milices, groupes"));
    function branche(id, y, coul) { return "<path data-k='" + id + "' class='trace' pathLength='1' d='M146,177C200,177 196," + (y + 17) + " 248," + (y + 17) + "' fill='none' stroke='" + (coul || "var(--encre2)") + "' stroke-width='2.2'/>"; }
    s += branche("b1", 18) + k("victoire", boite(250, 18, 150, 34, "victoire militaire") + t(410, 34, "Haut-Karabakh,", "lbl") + t(410, 49, "19-20 sept. 2023", "lbl"));
    s += branche("b2", 82) + k("nego", boite(250, 82, 110, 34, "médiation"));
    s += k("cessez", ligne(360, 99, 382, 99, "var(--encre2)", " stroke-width='2'") + pointe(390, 99, 0, "var(--encre2)") + boite(392, 82, 110, 34, "cessez-le-feu") + t(447, 132, "Gaza, 10 oct. 2025", "lbl", "middle"));
    s += k("paix", ligne(502, 99, 512, 99, "var(--encre2)", " stroke-width='2'") + pointe(520, 99, 0, "var(--encre2)") + boite(522, 82, 108, 34, "accord de paix", "var(--ok)") + t(576, 132, "Colombie, 2016", "lbl", "middle"));
    s += branche("b3", 150) + k("gele", boite(250, 150, 150, 34, "conflit gelé") + ligne(400, 167, 630, 167, "var(--encre2)", " stroke-dasharray='6 4' stroke-width='2'") + t(410, 160, "ligne de cessez-le-feu = frontière de fait", "lbl") + t(410, 186, "Corée : armistice de 1953, sans traité", "lbl"));
    s += branche("b4", 218, "var(--acier)") + k("onu", boite(250, 218, 150, 34, "ONU : casques bleus", "var(--acier)") + t(410, 234, "11 opérations de maintien", "lbl") + t(410, 249, "de la paix en 2025", "lbl"));
    s += k("veto", "<path d='M190,205L214,229M214,205L190,229' stroke='var(--rouge)' stroke-width='4' stroke-linecap='round'/>" + t(14, 232, "veto : Conseil bloqué", "lbl-f", "start", "font-size:11.5px") + t(14, 248, "(Russie, 25 févr. 2022)", "lbl"));
    s += branche("b5", 290, "var(--acier)") + k("justice", boite(250, 290, 150, 34, "justice internationale", "var(--acier)") + t(410, 306, "CPI : mandat d'arrêt contre", "lbl") + t(410, 321, "Vladimir Poutine (17 mars 2023)", "lbl"));
    ANIMS.t2resol = {
      titre: "Comment finit un conflit ? Cinq issues possibles",
      scene: { w: 640, h: 360, svg: s },
      etapes: [
        { date: "Aujourd'hui", titre: "Un conflit armé", texte: "Des États, des milices ou des groupes armés s'affrontent. Plusieurs issues sont possibles, et elles se combinent souvent.", montre: ["conflit"] },
        { date: "Sept. 2023", titre: "La victoire militaire", texte: "Un camp impose ses conditions : l'Azerbaïdjan reprend par la force le Haut-Karabakh, et plus de 100 000 Arméniens fuient. Une fin rarement juste et durable.", montre: ["b1", "victoire"], accent: ["victoire"] },
        { date: "2016-2025", titre: "Négocier : du cessez-le-feu à la paix", texte: "Des médiateurs rapprochent les camps. Le cessez-le-feu arrête les combats (Gaza, 10 octobre 2025) ; seul un accord de paix règle le conflit politiquement (Colombie, 24 novembre 2016).", montre: ["b2", "nego", "cessez", "paix"], accent: ["cessez", "paix"] },
        { date: "Depuis 1953", titre: "Le conflit gelé", texte: "Les combats cessent sans règlement : la ligne de cessez-le-feu devient une frontière de fait. Corée : armistice du 27 juillet 1953, jamais suivi d'un traité.", montre: ["b3", "gele"], accent: ["gele"] },
        { date: "2025", titre: "L'ONU et la sécurité collective", texte: "Le Conseil de sécurité peut imposer des sanctions, autoriser la force ou déployer des casques bleus : 11 opérations de maintien de la paix en 2025.", montre: ["b4", "onu"], accent: ["onu"] },
        { date: "25 févr. 2022", titre: "Le blocage du veto", texte: "Un membre permanent peut tout arrêter : la Russie oppose son veto à une résolution condamnant sa propre invasion de l'Ukraine.", montre: ["veto"], accent: ["veto"] },
        { date: "17 mars 2023", titre: "Juger les responsables", texte: "La justice internationale peut faire partie de la paix : la Cour pénale internationale juge des individus, la Cour internationale de justice règle les différends entre États.", montre: ["b5", "justice"], accent: ["justice"] }
      ],
      source: "Schéma du site. Exemples et dates du cours (section « Les modes de résolution »)."
    };
    ranger("t2-intro", 3, "t2resol");
  })();

  /* De la guerre limitée à la guerre d'anéantissement (1756-1815) */
  (function () {
    function X(a) { return Math.round(40 + (a - 1750) * 8.1); }
    var s = rect(0, 0, 640, 330, "var(--papier2)");
    s += ligne(30, 200, 620, 200, "var(--encre2)", " stroke-width='1.5'");
    [1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820].forEach(function (a) { s += ligne(X(a), 196, X(a), 204) + t(X(a), 216, a, "sch-pt", "middle"); });
    function phase(id, a, b, coul, nom, y) { return k(id, rect(X(a), 172, X(b) - X(a), 22, coul, " opacity='.5'") + ligne((X(a) + X(b)) / 2, y + 5, (X(a) + X(b)) / 2, 172, coul, " stroke-dasharray='1 3' stroke-width='1.5'") + t((X(a) + X(b)) / 2, y, nom, "lbl-f", "middle", "font-size:11.5px;fill:" + coul)); }
    function ev(id, a, y, txt, anc, cl) { return k(id, ligne(X(a), y + 5, X(a), 200, "var(--encre2)", " stroke-dasharray='2 3'") + pt(X(a), 200, cl || "pt-a", 5) + t(X(a) + (anc === "end" ? -6 : 6), y, txt, "lbl", anc || "start")); }
    function evb(id, a, y, txt, anc, cl) { return k(id, ligne(X(a), 200, X(a), y - 12, "var(--encre2)", " stroke-dasharray='2 3'") + pt(X(a), 200, cl || "pt-a", 5) + t(X(a) + (anc === "end" ? -6 : 6), y, txt, "lbl", anc || "start")); }
    s += phase("p1", 1756, 1763, "var(--acier)", "guerre limitée", 22) + phase("p2", 1792, 1799, "var(--rouge)", "nation en armes", 42) + phase("p3", 1800, 1807, "var(--rouge-f)", "anéantissement", 22) + phase("p4", 1808, 1814, "var(--kraft-f)", "guérilla", 42) + phase("p5", 1815, 1820, "var(--acier)", "équilibre", 22);
    s += ev("rossbach", 1757, 150, "Rossbach (1757)", "start", "pt-b") + ev("quebec", 1759, 125, "Québec (1759)", "start", "pt-b") + ev("traites", 1763, 100, "traités de 1763", "start", "pt-b");
    s += ev("valmy", 1792, 150, "Valmy (20 sept. 1792)", "end") + ev("levee", 1793, 125, "levée en masse (23 août 1793)", "end");
    s += evb("austerlitz", 1805, 240, "Austerlitz (2 déc. 1805)", "end") + evb("iena", 1806, 265, "Iéna (14 oct. 1806)", "end") + evb("madrid", 1808, 290, "Madrid, 2 mai 1808", "end", "pt-b");
    s += evb("russie", 1812, 240, "Russie 1812", "start", "pt-b") + evb("vienne", 1815, 315, "Vienne et Waterloo (juin 1815)", "end", "pt-b");
    ANIMS.t2napo = {
      titre: "De la guerre limitée à la guerre d'anéantissement (1756-1815)",
      scene: { w: 640, h: 330, svg: s },
      etapes: [
        { date: "1756-1763", titre: "Une guerre de souverains", texte: "La guerre de Sept Ans oppose des armées de métier, coûteuses : on manœuvre plus qu'on n'anéantit. Elle est pourtant déjà mondiale (Rossbach en Europe, Québec en Amérique).", montre: ["p1", "rossbach", "quebec"], accent: ["p1"] },
        { date: "Févr. 1763", titre: "Une paix de compromis", texte: "Les traités de Paris (10 février) et d'Hubertusbourg (15 février) redistribuent des territoires sans détruire les vaincus : la guerre reste un instrument limité.", montre: ["traites"], accent: ["traites"] },
        { date: "1792-1793", titre: "La nation en armes", texte: "Valmy (20 septembre 1792), puis la levée en masse (23 août 1793) : la guerre devient l'affaire de toute la nation. Le pôle « peuple » de la trinité de Clausewitz fait irruption.", montre: ["p2", "valmy", "levee"], accent: ["p2"] },
        { date: "1805-1806", titre: "La bataille décisive", texte: "Napoléon cherche la bataille qui anéantit l'armée ennemie : Austerlitz, puis Iéna, où Clausewitz est vaincu. C'est la forme la plus proche de la « guerre absolue ».", montre: ["p3", "austerlitz", "iena"], accent: ["p3"] },
        { date: "1808-1812", titre: "Les limites de l'anéantissement", texte: "En Espagne, la guérilla refuse la bataille (soulèvement de Madrid, 2 mai 1808) ; en Russie, la retraite et l'hiver détruisent la Grande Armée, entrée avec plus de 400 000 hommes.", montre: ["p4", "madrid", "russie"], accent: ["p4"] },
        { date: "Juin 1815", titre: "Le retour de l'équilibre", texte: "Acte final du congrès de Vienne (9 juin), défaite de Waterloo (18 juin) : les grandes puissances rétablissent un équilibre qui évite une guerre générale jusqu'en 1914.", montre: ["p5", "vienne"], accent: ["p5"] }
      ],
      source: "Frise du site ; les bandes de couleur résument le type de guerre dominant. Dates du cours."
    };
    ranger("t2-a1", 2, "t2napo");
  })();

  /* La paix de Westphalie (carte : cartes-z.js) */
  ANIMS.westph = {
    titre: "La paix de Westphalie (1648) sur la carte",
    scene: "carte:westph",
    etapes: [
      { date: "23 mai 1618", titre: "La défenestration de Prague", texte: "La révolte des protestants de Bohême contre les Habsbourg ouvre la guerre de Trente Ans : conflit religieux, lutte des princes contre l'empereur, rivalités européennes.", montre: ["prague", "vienne"], accent: ["prague"] },
      { date: "20 mai 1631", titre: "Une guerre totale avant l'heure", texte: "Le sac de Magdebourg par les troupes impériales fait environ 20 000 morts. Le Saint-Empire perd entre un cinquième et un tiers de sa population.", montre: ["magde"], accent: ["magde"] },
      { date: "1643-1648", titre: "Un congrès européen", texte: "Presque toute l'Europe négocie dans deux villes de Westphalie : Münster (puissances catholiques, médiation du nonce et de Venise) et Osnabrück (l'empereur, la Suède et les protestants).", montre: ["munster", "osna", "congres"], accent: ["munster", "osna"] },
      { date: "30 janv. 1648", titre: "La paix de Münster", texte: "L'Espagne reconnaît l'indépendance des Provinces-Unies.", montre: ["pu"], accent: ["pu"] },
      { date: "24 oct. 1648", titre: "Ce que règlent les traités", texte: "La France gagne des droits en Alsace et garde Metz, Toul et Verdun ; la Suède obtient la Poméranie occidentale et Brême ; la Confédération suisse est reconnue indépendante. Le calvinisme est admis.", montre: ["fr", "eveches", "sue", "breme", "ch", "paris"], accent: ["fr", "sue"] },
      { date: "1648-1659", titre: "Une paix garantie, mais partielle", texte: "La France et la Suède sont garantes des traités. Mais la guerre entre la France et l'Espagne continue jusqu'à la paix des Pyrénées (7 novembre 1659).", montre: ["pyr"], accent: ["pyr"] }
    ],
    source: "Fond Natural Earth (frontières actuelles) ; positions approximatives. La Suède obtient les duchés de Brême et de Verden, pas la ville libre de Brême."
  };
  ranger("t2-a2", 1, "westph");

  /* Le processus de paix israélo-palestinien : deux couloirs */
  (function () {
    function X(a) { return Math.round(50 + (a - 1990) * 15.5); }
    function g(id, a, y, txt, anc, cl, haut) { var yl = haut ? 190 : 190; return k(id, ligne(X(a), y + (haut ? 5 : -12), X(a), yl, "var(--encre2)", " stroke-dasharray='2 3'") + pt(X(a), 190, cl, 5.5) + t(X(a) + (anc === "end" ? -7 : 7), y, txt, "lbl", anc || "start")); }
    var s = rect(0, 0, 640, 380, "var(--papier2)");
    s += ligne(30, 190, 620, 190, "var(--encre2)", " stroke-width='1.5'");
    [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025].forEach(function (a) { s += ligne(X(a), 186, X(a), 194) + t(X(a), 206, a, "sch-pt", "middle"); });
    s += t(30, 24, "VERS LA PAIX", "lbl-f", null, "fill:var(--acier)") + t(30, 368, "VIOLENCES ET RUPTURES", "lbl-f");
    s += g("madrid", 1991.8, 150, "Madrid (1991)", "start", "pt-b", true) + g("oslo", 1993.7, 115, "Oslo (13 sept. 1993)", "start", "pt-b", true) + g("ap", 1994.4, 80, "Autorité palestinienne (1994)", "start", "pt-b", true);
    s += g("hebron", 1994.15, 232, "Hébron (févr. 1994)", "start", "pt-a") + g("rabin", 1995.85, 262, "assassinat de Rabin (4 nov. 1995)", "start", "pt-a");
    s += g("campdavid", 2000.5, 150, "Camp David échoue (2000)", "start", "pt-b", true) + g("intifada", 2000.7, 292, "seconde Intifada (sept. 2000)", "start", "pt-a") + g("barriere", 2002, 322, "barrière en Cisjordanie (2002)", "start", "pt-a");
    s += g("hamas", 2007.45, 232, "le Hamas prend Gaza (juin 2007)", "start", "pt-a");
    s += g("abraham", 2020.7, 80, "accords d'Abraham (15 sept. 2020)", "end", "pt-b", true);
    s += g("oct7", 2023.77, 262, "7 oct. 2023 : guerre de Gaza", "end", "pt-a");
    s += g("reco", 2025.72, 115, "reconnaissances de la Palestine (sept. 2025)", "end", "pt-b", true) + g("cessez", 2025.78, 150, "cessez-le-feu à Gaza (10 oct. 2025)", "end", "pt-b", true);
    ANIMS.t2oslo = {
      titre: "Le processus de paix israélo-palestinien : espoirs et ruptures (1991-2025)",
      scene: { w: 640, h: 380, svg: s },
      etapes: [
        { date: "1991-1993", titre: "De Madrid à Oslo", texte: "Après la conférence de Madrid (30 octobre 1991), des négociations secrètes en Norvège aboutissent à la reconnaissance mutuelle d'Israël et de l'OLP et à la déclaration de principes (13 septembre 1993).", montre: ["madrid", "oslo"], accent: ["oslo"] },
        { date: "1994-1995", titre: "La paix sabotée", texte: "L'Autorité palestinienne est créée (1994), mais les extrémistes frappent : massacre de 29 Palestiniens à Hébron (février 1994), attentats du Hamas, assassinat de Yitzhak Rabin (4 novembre 1995).", montre: ["ap", "hebron", "rabin"], accent: ["rabin"] },
        { date: "2000-2002", titre: "L'échec", texte: "Le sommet de Camp David échoue (juillet 2000), la seconde Intifada éclate (septembre 2000) ; Israël commence en 2002 une barrière en Cisjordanie, jugée contraire au droit international par la CIJ (2004).", montre: ["campdavid", "intifada", "barriere"], accent: ["intifada"] },
        { date: "2005-2007", titre: "Un camp palestinien divisé", texte: "Israël évacue ses colonies de Gaza (2005) ; le Hamas gagne les élections (janvier 2006) puis prend Gaza par la force (juin 2007). Blocus et guerres successives suivent.", montre: ["hamas"], accent: ["hamas"] },
        { date: "15 sept. 2020", titre: "Une paix sans les Palestiniens", texte: "Les accords d'Abraham normalisent les relations d'Israël avec les Émirats arabes unis et Bahreïn, puis le Maroc et le Soudan : la question palestinienne paraît marginalisée.", montre: ["abraham"], accent: ["abraham"] },
        { date: "7 oct. 2023", titre: "L'attaque et la guerre", texte: "Le Hamas tue environ 1 200 personnes et enlève 251 otages ; Israël riposte par une guerre dévastatrice à Gaza.", montre: ["oct7"], accent: ["oct7"] },
        { date: "Sept.-oct. 2025", titre: "Reconnaissances et cessez-le-feu", texte: "Plusieurs États occidentaux, dont la France (22 septembre), reconnaissent l'État de Palestine ; un cessez-le-feu entre en vigueur le 10 octobre 2025. Un cessez-le-feu n'est pas encore la paix.", montre: ["reco", "cessez"], accent: ["reco", "cessez"] }
      ],
      source: "Frise du site, deux couloirs. Dates du cours."
    };
    ranger("t2-otc", 2, "t2oslo");
  })();

  /* ====================== THÈME 3 ====================== */
  ANIMS.proces = {
    titre: "Juger les criminels nazis : de Nuremberg aux procès tardifs",
    scene: "carte:proces",
    etapes: [
      { date: "1945-1947", titre: "Nuremberg", texte: "Le procès des grands criminels de guerre (1945-1946) est suivi de douze procès américains, dont le procès des médecins (1946-1947), qui énonce le code de Nuremberg sur le consentement.", montre: ["nur"], accent: ["nur"] },
      { date: "1960-1961", titre: "Le procès Eichmann", texte: "Enlevé en Argentine par le Mossad (mai 1960), Adolf Eichmann est jugé à Jérusalem en 1961 : filmé, le procès met au centre les rescapés et le génocide des Juifs.", montre: ["eich", "eicht", "jer"], accent: ["jer"] },
      { date: "1963-1965", titre: "L'Allemagne juge ses criminels", texte: "Poussée par le procureur Fritz Bauer, la justice ouest-allemande juge à Francfort 22 responsables d'Auschwitz : la société allemande découvre le fonctionnement du camp.", montre: ["franc"], accent: ["franc"] },
      { date: "1964 et 1979", titre: "Des crimes imprescriptibles", texte: "La France rend les crimes contre l'humanité imprescriptibles (1964), la RFA le meurtre (1979) : des procès deviennent possibles des décennies plus tard.", montre: ["impr"], accent: ["impr"] },
      { date: "1987-1998", titre: "La France face à Vichy", texte: "Klaus Barbie, chef de la Gestapo de Lyon (1987), Paul Touvier, de la Milice (1994), Maurice Papon, haut fonctionnaire de Vichy à Bordeaux (1998), sont condamnés.", montre: ["lyon", "vers", "bdx"], accent: ["lyon", "vers", "bdx"] },
      { date: "2011-2022", titre: "Les derniers procès", texte: "John Demjanjuk (Munich, 2011), Oskar Gröning (Lüneburg, 2015), Irmgard Furchner, secrétaire au camp du Stutthof (Itzehoe, 2022) : la justice juge encore des exécutants très âgés.", montre: ["mun", "lun", "itz"], accent: ["mun", "lun", "itz"] }
    ],
    source: "Fond Natural Earth (frontières actuelles) ; positions approximatives. Dates du cours. Le procès Touvier s'est tenu devant la cour d'assises des Yvelines, à Versailles."
  };
  ranger("t3-otc", 3, "proces");

  /* ====================== THÈME 4 ====================== */
  /* Des cercles qui s'élargissent : du patrimoine familial au patrimoine de l'humanité */
  (function () {
    var cx = 210, cy = 188;
    var anneaux = [["fam", 42, 28, "var(--encre2)"], ["nat", 82, 58, "var(--rouge)"], ["etat", 122, 88, "var(--acier)"], ["large", 162, 118, "var(--ok)"], ["hum", 200, 152, "var(--rouge-f)"]];
    var lab = [["fam", "La famille", "patrimonium : les biens du père", 52], ["nat", "La nation (1789-1794)", "Louvre 1793, « vandalisme » 1794", 102], ["etat", "L'État protège", "inspecteur 1830, loi de 1913", 152], ["large", "Un patrimoine élargi", "usines, quartiers, paysages", 202], ["hum", "L'humanité", "La Haye 1954, Nubie 1960, 1972", 252]];
    var s = rect(0, 0, 640, 370, "var(--papier2)");
    anneaux.forEach(function (a, i) {
      var l = lab[i], ex = cx + a[1] * 0.866, ey = cy - a[2] * 0.5;
      s += k(a[0], "<ellipse cx='" + cx + "' cy='" + cy + "' rx='" + a[1] + "' ry='" + a[2] + "' fill='" + a[3] + "' fill-opacity='.10' stroke='" + a[3] + "' stroke-width='2.2'/>" +
        ligne(ex, ey, 418, l[3] - 4, a[3], " stroke-width='1' stroke-dasharray='2 2'") + pt(ex, ey, "pt-b", 3.5) +
        t(424, l[3] - 2, l[1], "lbl-f", null, "font-size:12px;fill:" + a[3]) + t(424, l[3] + 13, l[2], "lbl"));
    });
    s += k("imm", "<ellipse cx='" + cx + "' cy='" + cy + "' rx='206' ry='160' fill='none' stroke='var(--acier)' stroke-width='2.5' stroke-dasharray='3 6'/>" +
      ligne(cx + 206 * 0.6, cy + 160 * 0.8, 418, 314, "var(--acier)", " stroke-width='1' stroke-dasharray='2 2'") + t(424, 316, "L'immatériel (2003)", "lbl-f", null, "font-size:12px;fill:var(--acier)") + t(424, 331, "fêtes, savoir-faire, repas", "lbl"));
    s += t(cx, cy + 4, "patrimoine", "sch-pt", "middle");
    ANIMS.t4mot = {
      titre: "Le patrimoine, des cercles qui s'élargissent",
      scene: { w: 640, h: 370, svg: s },
      etapes: [
        { date: "Antiquité", titre: "Un mot du droit familial", texte: "En latin, patrimonium désigne les biens hérités du père. Le patrimoine est d'abord privé et se transmet dans les familles.", montre: ["fam"], accent: ["fam"] },
        { date: "1789-1794", titre: "La Révolution invente le patrimoine national", texte: "Les biens du clergé sont nationalisés (2 novembre 1789), le Louvre devient un musée public (10 août 1793), l'abbé Grégoire dénonce le « vandalisme » (1794).", montre: ["nat"], accent: ["nat"] },
        { date: "1830-1913", titre: "L'État protège les monuments", texte: "Inspecteur général des monuments historiques (1830 ; Mérimée à partir de 1834), Commission (1837), loi du 31 décembre 1913 qui permet de classer même contre l'avis du propriétaire.", montre: ["etat"], accent: ["etat"] },
        { date: "XXe siècle", titre: "Un patrimoine élargi", texte: "L'habitat ordinaire, les quartiers anciens, les paysages, les sites industriels, l'architecture du XXe siècle entrent dans le patrimoine : Le Havre reconstruit, bassin minier.", montre: ["large"], accent: ["large"] },
        { date: "1954-1972", titre: "Un patrimoine de l'humanité", texte: "Convention de La Haye (1954), campagne de Nubie pour sauver Abou Simbel (1960), puis convention de l'Unesco de 1972 : un patrimoine commun qu'aucun État ne possède seul.", montre: ["hum"], accent: ["hum"] },
        { date: "17 oct. 2003", titre: "Le patrimoine immatériel", texte: "Pratiques, savoir-faire, fêtes, repas : la convention de l'Unesco de 2003 protège ce qui se transmet de génération en génération et se recrée sans cesse.", montre: ["imm"], accent: ["imm"] }
      ],
      source: "Schéma du site. Dates du cours."
    };
    ranger("t4-intro", 1, "t4mot");
  })();

  /* La politique du patrimoine en France : l'État, puis les citoyens et les financeurs */
  (function () {
    function X(a) { return Math.round(40 + (a - 1830) * 3.0); }
    function ev(id, a, y, txt, anc, cl, yb) { return k(id, ligne(X(a), y + 4, X(a), yb, "var(--encre2)", " stroke-dasharray='2 3'") + pt(X(a), yb, cl || "pt-b", 5.5) + t(X(a) + (anc === "end" ? -7 : 7), y, txt, "lbl", anc || "start")); }
    var s = rect(0, 0, 640, 360, "var(--papier2)");
    s += rect(30, 30, 590, 96, "var(--acier)", " opacity='.08'") + rect(30, 134, 590, 96, "var(--ok)", " opacity='.08'") + rect(30, 238, 590, 86, "var(--kraft)", " opacity='.25'");
    s += t(36, 46, "L'ÉTAT", "sch-pt") + t(36, 150, "CITOYENS ET COLLECTIVITÉS", "sch-pt") + t(36, 254, "FINANCER", "sch-pt");
    s += ligne(30, 334, 620, 334, "var(--encre2)", " stroke-width='1.5'");
    [1850, 1900, 1950, 2000].forEach(function (a) { s += ligne(X(a), 330, X(a), 338) + t(X(a), 352, a, "sch-pt", "middle"); });
    s += ev("i1830", 1830, 70, "1830 : inspecteur général", "start", null, 118) + ev("c1837", 1837, 95, "1837 : Commission", "start", null, 118);
    s += ev("l1913", 1913, 70, "loi du 31 décembre 1913", "start", null, 118);
    s += ev("m1959", 1959, 95, "1959 : ministère Malraux", "end", null, 118) + ev("s1962", 1962, 70, "1962 : secteurs sauvegardés", "start", null, 118);
    s += ev("j1984", 1984, 168, "1984 : 1re journée portes ouvertes", "end", "pt-a", 222) + ev("j1991", 1991, 192, "1991 : Journées européennes", "end", "pt-a", 222) + ev("r2004", 2004, 216, "2004 : Inventaire confié aux régions", "end", "pt-a", 222);
    s += ev("f1996", 1996, 268, "1996 : Fondation du patrimoine", "end", null, 316) + ev("a2003", 2003, 290, "2003 : loi Aillagon (mécénat)", "end", null, 316) + ev("k2018", 2018, 312, "2018 : Loto du patrimoine", "end", null, 316);
    s += ev("lcap", 2016, 95, "2016 : loi LCAP", "end", null, 118);
    ANIMS.t4etat = {
      titre: "Gérer le patrimoine en France : de l'État seul à tous les acteurs",
      scene: { w: 640, h: 360, svg: s },
      etapes: [
        { date: "1830-1837", titre: "Un modèle d'État", texte: "La France invente tôt une administration du patrimoine : un inspecteur général (1830), puis la Commission des monuments historiques (1837). Mérimée fait sauver Vézelay.", montre: ["i1830", "c1837"], accent: ["i1830"] },
        { date: "31 déc. 1913", titre: "Classer, même contre le propriétaire", texte: "La loi de 1913, toujours en vigueur dans ses principes, permet de classer un monument au titre des monuments historiques.", montre: ["l1913"], accent: ["l1913"] },
        { date: "1959-1964", titre: "Malraux : la culture devient un ministère", texte: "De Gaulle crée le ministère des Affaires culturelles (1959). La loi du 4 août 1962 protège des quartiers entiers (secteurs sauvegardés) ; l'Inventaire général recense tout le patrimoine (1964).", montre: ["m1959", "s1962"], accent: ["m1959", "s1962"] },
        { date: "1984-2004", titre: "Les citoyens s'approprient le patrimoine", texte: "Première « journée portes ouvertes » (septembre 1984), devenue les Journées européennes du patrimoine (1991) ; les régions reçoivent l'Inventaire (2004).", montre: ["j1984", "j1991", "r2004"], accent: ["j1984"] },
        { date: "1996-2018", titre: "Financer au-delà de l'État", texte: "Fondation du patrimoine (1996), loi Aillagon sur le mécénat (2003), Loto du patrimoine (premier tirage le 14 septembre 2018) ; 846 millions d'euros de dons pour Notre-Dame.", montre: ["f1996", "a2003", "k2018"], accent: ["a2003"] },
        { date: "7 juil. 2016", titre: "Moderniser le droit", texte: "La loi LCAP remplace les secteurs sauvegardés par les « sites patrimoniaux remarquables » et intègre le patrimoine mondial dans le droit français.", montre: ["lcap"], accent: ["lcap"] }
      ],
      source: "Frise du site en trois couloirs. Dates du cours."
    };
    ranger("t4-otc", 1, "t4etat");
  })();

  /* ====================== THÈME 5 ====================== */
  /* Une même forêt, des regards différents */
  (function () {
    var s = rect(0, 0, 640, 320, "var(--papier2)") + rect(0, 250, 640, 70, "var(--kraft)", " opacity='.45'");
    function arbre(x, y, h) { return "<path d='M" + x + "," + (y - h) + "L" + (x - h * 0.32) + "," + (y - h * 0.25) + "H" + (x + h * 0.32) + "Z' fill='var(--ok)' stroke='var(--k-halo)' stroke-width='1'/>" + rect(x - 3, y - h * 0.25, 6, h * 0.25, "var(--kraft-f)"); }
    var foret = ""; [[60, 252, 90], [105, 256, 120], [150, 250, 100], [195, 255, 130], [240, 252, 95], [285, 256, 115], [330, 250, 85]].forEach(function (a) { foret += arbre(a[0], a[1], a[2]); });
    s += foret + t(195, 296, "UNE MÊME FORÊT", "lbl-f", "middle", "font-size:12px");
    function legende(id, titre, l1, l2, dessin) { return k(id, dessin + t(380, 120, titre, "lbl-f", null, "font-size:13px") + t(380, 146, l1, "lbl") + (l2 ? t(380, 164, l2, "lbl") : "")); }
    s += legende("res", "UNE RESSOURCE", "bois de marine, combustible", "(ordonnance de Colbert, 1669)", "<path d='M372,270h90l-14,22h-62z' fill='var(--acier)'/><path d='M410,270V214M410,220l26,24h-26M410,218l-22,26h22' fill='var(--papier)' stroke='var(--acier)' stroke-width='2'/>");
    s += legende("pay", "UN PAYSAGE À ADMIRER", "Fontainebleau : « réserve artistique »", "(13 avril 1861)", rect(20, 100, 345, 175, "none", " stroke='var(--kraft-f)' stroke-width='6'"));
    s += legende("sauv", "UNE NATURE SAUVAGE", "Yellowstone, premier parc national", "(1er mars 1872)", rect(470, 226, 70, 26, "var(--papier)", " stroke='var(--encre)' stroke-width='1.5'") + ligne(505, 252, 505, 280, "var(--encre)", " stroke-width='3'") + t(505, 244, "PARC", "sch-pt", "middle"));
    s += legende("alerte", "UN MILIEU MENACÉ", "Carson, Printemps silencieux (1962)", "conférence de Stockholm (1972)", "<path d='M505,212l30,52h-60z' fill='var(--rouge)'/>" + t(505, 256, "!", "lbl-f", "middle", "fill:var(--sur-rouge);stroke:none;font-size:22px"));
    s += legende("dur", "UN BIEN À TRANSMETTRE", "développement durable", "(rapport Brundtland, 1987)", "<path d='M480,240a26,26 0 1 1 26,26' fill='none' stroke='var(--ok)' stroke-width='4'/>" + "<path d='M498,258l10,8l-10,8z' fill='var(--ok)'/>");
    s += legende("carb", "UN PUITS DE CARBONE", "la forêt absorbe du CO₂ ;", "« Anthropocène » (Crutzen, 2000)", "<path d='M120,40C120,70 160,70 160,96M200,30C200,62 196,70 196,100M280,40C280,70 250,72 250,98' fill='none' stroke='var(--acier)' stroke-width='2.5' stroke-dasharray='5 4'/>" + t(200, 24, "CO₂", "lbl-f", "middle", "fill:var(--acier)"));
    ANIMS.t5regards = {
      titre: "Une même forêt, des regards différents : l'environnement est une construction",
      scene: { w: 640, h: 320, svg: s },
      etapes: [
        { date: "1669", titre: "Une ressource", texte: "Pour l'État de Colbert, la forêt fournit le bois des navires du roi et le combustible : on règle les coupes pour préserver la ressource.", montre: ["res"], accent: ["res"] },
        { date: "13 avril 1861", titre: "Un paysage", texte: "À la demande des peintres de Barbizon, un décret crée en forêt de Fontainebleau une « réserve artistique » : l'une des premières protections d'un paysage pour sa beauté.", montre: ["pay"], cache: ["res"], accent: ["pay"] },
        { date: "1er mars 1872", titre: "La nature sauvage", texte: "Aux États-Unis, la wilderness doit être préservée de l'exploitation : Yellowstone devient le premier parc national du monde, en écartant les Amérindiens.", montre: ["sauv"], cache: ["pay"], accent: ["sauv"] },
        { date: "1962-1972", titre: "Un milieu menacé", texte: "Rachel Carson dénonce les pesticides (1962) ; la conférence de Stockholm (1972), première grande conférence mondiale sur l'environnement, crée le PNUE.", montre: ["alerte"], cache: ["sauv"], accent: ["alerte"] },
        { date: "1987", titre: "Un bien à transmettre", texte: "Le rapport Brundtland définit le développement durable : répondre aux besoins du présent sans compromettre ceux des générations futures.", montre: ["dur"], cache: ["alerte"], accent: ["dur"] },
        { date: "Depuis 2000", titre: "Un puits de carbone", texte: "Avec le changement climatique, la forêt devient aussi un stock de carbone. Paul Crutzen propose le mot « Anthropocène » (2000), terme utilisé mais discuté par les géologues.", montre: ["carb"], cache: ["dur"], accent: ["carb"] }
      ],
      source: "Schéma du site. Exemples et dates du cours (introduction et axe 1 du thème)."
    };
    ranger("t5-intro", 2, "t5regards");
  })();

  /* Deux ruptures énergétiques : capter le soleil, brûler les stocks fossiles */
  (function () {
    var s = rect(0, 0, 640, 340, "var(--papier2)") + rect(0, 250, 640, 90, "var(--kraft)", " opacity='.45'");
    s += ligne(320, 14, 320, 330, "var(--encre2)", " stroke-dasharray='4 4'");
    s += t(160, 22, "« RÉVOLUTION NÉOLITHIQUE »", "lbl-f", "middle", "font-size:12px") + t(480, 22, "« RÉVOLUTION INDUSTRIELLE »", "lbl-f", "middle", "font-size:12px");
    s += k("soleil", "<circle cx='60' cy='70' r='22' fill='#E8B43A'/>" + trace("", "M86,84L150,200", "#E8B43A", 3) + trace("", "M80,94L110,220", "#E8B43A", 3) + t(92, 58, "énergie du soleil", "lbl"));
    var ble = ""; for (var i = 0; i < 9; i++) { var x = 120 + i * 20; ble += "<path d='M" + x + ",250V" + (220 - (i % 3) * 4) + "' stroke='#B88A2E' stroke-width='2'/><ellipse cx='" + x + "' cy='" + (216 - (i % 3) * 4) + "' rx='3' ry='7' fill='#D9A63E'/>"; }
    s += k("champ", ble + t(200, 270, "plantes et animaux domestiqués", "lbl", "middle") + t(200, 286, "vers 10 000 av. J.-C., Croissant fertile", "lbl", "middle"));
    s += k("defr", "<path d='M250,250V228M262,250V232M274,250V229' stroke='var(--kraft-f)' stroke-width='5'/>" + t(262, 214, "défrichement", "lbl", "middle"));
    s += k("lent", trace("", "M40,312C120,300 200,300 290,312", "var(--ok)", 2.5) + pointe(296, 313, 10, "var(--ok)") + t(40, 330, "Grèce 6500 av. J.-C. → Atlantique : 2 500 ans", "lbl"));
    s += k("stock", "<ellipse cx='420' cy='300' rx='60' ry='14' fill='var(--encre)' opacity='.85'/><ellipse cx='545' cy='296' rx='42' ry='11' fill='var(--encre)' opacity='.85'/>" + t(480, 334, "stocks fossiles : des millions d'années", "lbl", "middle"));
    s += k("watt", rect(430, 200, 70, 50, "var(--acier)") + rect(480, 150, 14, 50, "var(--acier)") + "<circle cx='452' cy='226' r='12' fill='none' stroke='var(--papier)' stroke-width='3'/>" + trace("", "M420,286V256", "var(--rouge)", 3) + t(334, 172, "Watt, 1769", "lbl-f", null, "font-size:12px") + t(334, 188, "charbon, puis pétrole", "lbl"));
    s += k("co2", "<path d='M487,148C478,120 500,110 492,86C486,66 505,58 500,40' fill='none' stroke='var(--encre2)' stroke-width='6' stroke-linecap='round' opacity='.45'/>" +
      rect(560, 50, 22, 180, "var(--papier)", " stroke='var(--encre)' stroke-width='1.5'") + rect(560, 162, 22, 68, "var(--acier)") + rect(560, 66, 22, 96, "var(--rouge)") +
      t(554, 166, "280 ppm", "lbl", "end") + t(554, 70, "430,5 ppm", "lbl-f", "end", "font-size:12px") + t(571, 44, "CO₂", "lbl-f", "middle", "font-size:12px"));
    s += k("pop", t(330, 120, "8 milliards d'humains", "lbl-f", null, "font-size:12px") + t(330, 136, "(15 nov. 2022)", "lbl"));
    ANIMS.t5energie = {
      titre: "Deux ruptures : capter l'énergie du soleil, libérer l'énergie fossile",
      scene: { w: 640, h: 340, svg: s },
      etapes: [
        { date: "Vers 10 000 av. J.-C.", titre: "Domestiquer le vivant", texte: "Au Proche-Orient (Croissant fertile), puis dans d'autres foyers, des sociétés domestiquent plantes et animaux : l'agriculture capte l'énergie du soleil.", montre: ["soleil", "champ"], accent: ["champ"] },
        { date: "Néolithique", titre: "Une rupture dans les milieux", texte: "Pour cultiver, on défriche par le feu et la hache de pierre polie : la forêt recule durablement, la population augmente.", montre: ["defr"], accent: ["defr"] },
        { date: "6500-4000 av. J.-C.", titre: "Une « révolution » très lente", texte: "Il faut environ 2 500 ans pour que l'agriculture se diffuse de la Grèce aux rivages de l'Atlantique : une rupture par ses effets plus que par sa vitesse.", montre: ["lent"], accent: ["lent"] },
        { date: "Millions d'années", titre: "Des stocks d'énergie", texte: "Charbon et pétrole sont de l'énergie solaire accumulée pendant des millions d'années dans le sous-sol.", montre: ["stock"], accent: ["stock"] },
        { date: "1769", titre: "Puiser dans les stocks", texte: "James Watt perfectionne la machine à vapeur : l'industrie mécanisée brûle le charbon, puis le pétrole. Pour la première fois, les sociétés puisent massivement dans ces stocks.", montre: ["watt"], accent: ["watt"] },
        { date: "1950-2025", titre: "La grande accélération", texte: "Le CO₂ passe d'environ 280 ppm avant l'ère industrielle à 430,5 ppm en mai 2025 (Mauna Loa) ; la population mondiale atteint 8 milliards le 15 novembre 2022.", montre: ["co2", "pop"], accent: ["co2"] }
      ],
      source: "Schéma du site, sans échelle. Chiffres du cours (NOAA, ONU)."
    };
    ranger("t5-a1", 2, "t5energie");
  })();

  /* Le Dust Bowl : une catastrophe produite par l'exploitation (coupe schématique) */
  (function () {
    var s = rect(0, 0, 640, 330, "var(--papier2)") + rect(0, 220, 640, 110, "var(--kraft)", " opacity='.55'");
    s += ligne(0, 220, 640, 220, "var(--kraft-f)", " stroke-width='2'") + t(620, 318, "coupe schématique des Grandes Plaines", "sch-pt", "end");
    var herbe = "", racines = "";
    for (var i = 0; i < 26; i++) { var x = 20 + i * 24; herbe += "<path d='M" + x + ",220l-6,-22M" + x + ",220l0,-28M" + x + ",220l6,-20' stroke='var(--ok)' stroke-width='2.2' fill='none'/>"; racines += "<path d='M" + x + ",222c-4,20 6,34 -2,56M" + x + ",222c6,16 -2,30 8,44' stroke='var(--ok)' stroke-width='1.3' fill='none' opacity='.7'/>"; }
    s += k("prairie", herbe + racines);
    var sillons = ""; for (i = 0; i < 20; i++) sillons += "<path d='M" + (14 + i * 32) + ",220l12,-8l12,8' stroke='var(--kraft-f)' stroke-width='2.5' fill='none'/>";
    s += k("labour", sillons + "<path d='M40,190h70l14,-18h30v18h12' stroke='var(--encre)' stroke-width='3' fill='none'/><circle cx='60' cy='200' r='10' fill='none' stroke='var(--encre)' stroke-width='3'/><circle cx='150' cy='200' r='10' fill='none' stroke='var(--encre)' stroke-width='3'/>");
    var fentes = ""; for (i = 0; i < 9; i++) fentes += "<path d='M" + (60 + i * 66) + ",222l6,14l-6,10l8,16' stroke='var(--kraft-f)' stroke-width='2' fill='none'/>";
    s += k("seche", "<circle cx='560' cy='64' r='30' fill='#E8B43A'/>" + fentes);
    var nuage = ""; [[120, 170, 70, 30], [210, 150, 90, 40], [320, 130, 110, 50], [440, 110, 120, 60]].forEach(function (n) { nuage += "<ellipse cx='" + n[0] + "' cy='" + n[1] + "' rx='" + n[2] + "' ry='" + n[3] + "' fill='var(--kraft-f)' opacity='.38'/>"; });
    s += k("vent", nuage + "<path d='M20,110h70M30,140h90M20,80h60' stroke='var(--encre2)' stroke-width='2.5' stroke-linecap='round'/>" + pointe(98, 110, 0, "var(--encre2)") + pointe(128, 140, 0, "var(--encre2)") + pointe(88, 80, 0, "var(--encre2)"));
    s += k("exode", trace("", "M380,206C450,206 520,200 600,206", "var(--rouge)", 3) + pointe(608, 206, 0) + t(600, 196, "vers la Californie", "lbl", "end"));
    var repousse = ""; for (i = 0; i < 26; i += 2) { x = 20 + i * 24; repousse += "<path d='M" + x + ",220l-5,-16M" + x + ",220l0,-20M" + x + ",220l5,-15' stroke='var(--ok)' stroke-width='2.2' fill='none'/>"; }
    s += k("soins", repousse);
    function cap(id, l1, l2) { return k(id, rect(14, 12, 400, l2 ? 46 : 28, "var(--papier)", " rx='5' stroke='var(--encre)' stroke-width='1'") + t(24, 31, l1, "lbl-f", null, "font-size:12px") + (l2 ? t(24, 49, l2, "lbl") : "")); }
    s += cap("c1", "Une prairie : les racines tiennent le sol") + cap("c2", "Homestead Act (1862) : le sol est labouré à outrance") + cap("c3", "Années 1930 : la sécheresse") + cap("c4", "Tempêtes de poussière", "« dimanche noir » : 14 avril 1935") + cap("c5", "Des centaines de milliers d'exilés", "Les Raisins de la colère (Steinbeck, 1939)") + cap("c6", "1935 : un service fédéral", "de conservation des sols (New Deal)");
    ANIMS.t5dust = {
      titre: "Le Dust Bowl : comment l'exploitation fabrique une catastrophe",
      scene: { w: 640, h: 330, svg: s },
      etapes: [
        { date: "Avant 1862", titre: "La prairie", texte: "Dans les Grandes Plaines, les herbes de la prairie et leurs racines retiennent un sol sec et léger.", montre: ["prairie", "c1"], accent: ["prairie"] },
        { date: "1862-1920", titre: "Labourer à outrance", texte: "La conquête de l'Ouest et le Homestead Act (1862) mettent les Grandes Plaines en culture : la prairie est retournée, le sol reste à nu.", montre: ["labour", "c2"], cache: ["prairie", "c1"], accent: ["labour"] },
        { date: "Années 1930", titre: "La sécheresse", texte: "Une longue sécheresse dessèche les sols labourés, que plus rien ne retient.", montre: ["seche", "c3"], cache: ["c2"], accent: ["seche"] },
        { date: "14 avril 1935", titre: "Le « dimanche noir »", texte: "Le vent soulève des tempêtes de poussière géantes, qui ruinent les fermes : le 14 avril 1935, une tempête traverse toutes les Grandes Plaines.", montre: ["vent", "c4"], cache: ["c3"], accent: ["vent"] },
        { date: "Années 1930", titre: "L'exode", texte: "Des centaines de milliers de personnes partent vers la Californie ; John Steinbeck raconte cet exode dans Les Raisins de la colère (1939).", montre: ["exode", "c5"], cache: ["c4"], accent: ["exode"] },
        { date: "1935", titre: "L'État fédéral intervient", texte: "Le New Deal crée un service de conservation des sols : la catastrophe, produite par l'exploitation, conduit l'État à protéger les sols.", montre: ["soins", "c6"], cache: ["c5", "vent"], accent: ["soins"] }
      ],
      source: "Coupe schématique du site, sans échelle. Faits du cours."
    };
    ranger("t5-otc", 1, "t5dust");
  })();

  /* ====================== THÈME 6 ====================== */
  /* Le cycle de Kuhn : science normale, anomalies, crise, révolution */
  (function () {
    var N = [["n1", 320, 50, "science normale", "un paradigme partagé"], ["n2", 470, 140, "anomalies", "des résultats inexpliqués"], ["n3", 410, 270, "crise", "le paradigme vacille"], ["n4", 230, 270, "révolution", "débats entre pairs"], ["n5", 170, 140, "nouveau paradigme", "accepté par la communauté"]];
    var s = rect(0, 0, 640, 330, "var(--papier2)");
    s += "<circle cx='320' cy='170' r='118' fill='none' stroke='var(--ligne)' stroke-width='10'/>";
    N.forEach(function (n) { s += k(n[0], boite(n[1] - 78, n[2] - 20, 156, 42, n[3], n[0] === "n3" || n[0] === "n4" ? "var(--rouge)" : "var(--acier)", n[4])); });
    s += k("a1", trace("", "M400,74Q440,90 456,116", "var(--encre2)", 2.5) + pointe(458, 118, 60, "var(--encre2)"));
    s += k("a2", trace("", "M470,164Q470,220 440,246", "var(--encre2)", 2.5) + pointe(438, 248, 130, "var(--encre2)"));
    s += k("a3", trace("", "M330,290L312,290", "var(--rouge)", 3) + pointe(310, 290, 180));
    s += k("a4", trace("", "M200,246Q170,210 170,164", "var(--encre2)", 2.5) + pointe(170, 162, -90, "var(--encre2)"));
    s += k("a5", trace("", "M184,118Q210,80 240,70", "var(--encre2)", 2.5) + pointe(242, 69, -15, "var(--encre2)"));
    s += k("marques", t(548, 106, "!", "lbl-f", null, "font-size:20px") + t(560, 128, "!", "lbl-f", null, "font-size:20px") + t(552, 182, "!", "lbl-f", null, "font-size:20px"));
    s += k("ex", t(320, 160, "1900-1927 : de la physique", "lbl", "middle") + t(320, 176, "classique à la physique quantique", "lbl", "middle") + t(320, 194, "(Solvay 1927 : Einstein, Bohr)", "lbl", "middle"));
    ANIMS.t6kuhn = {
      titre: "Comment la science change de paradigme (Thomas Kuhn, 1962)",
      scene: { w: 640, h: 330, svg: s },
      etapes: [
        { date: "1962", titre: "La science normale", texte: "Selon Thomas Kuhn, une communauté scientifique partage un paradigme : des théories, des méthodes et des questions admises par tous.", montre: ["n1"], accent: ["n1"] },
        { date: "", titre: "Les anomalies s'accumulent", texte: "Des résultats ne s'expliquent pas dans le cadre admis. Au début, on les met de côté.", montre: ["a1", "n2", "marques"], accent: ["marques"] },
        { date: "", titre: "La crise", texte: "Quand les anomalies deviennent trop nombreuses, le paradigme vacille : la communauté se divise.", montre: ["a2", "n3"], accent: ["n3"] },
        { date: "", titre: "La révolution scientifique", texte: "Un nouveau cadre s'impose après des débats entre pairs : la connaissance est aussi une construction collective et sociale.", montre: ["a3", "n4"], accent: ["n4"] },
        { date: "", titre: "Un nouveau paradigme", texte: "Une fois accepté, le nouveau paradigme devient à son tour la science normale.", montre: ["a4", "n5", "a5"], cache: ["marques"], accent: ["n5"] },
        { date: "1900-1927", titre: "Un exemple : la physique quantique", texte: "Entre 1900 et la fin des années 1920, la physique classique cède la place à la physique quantique ; au conseil Solvay de 1927, Einstein et Bohr débattent de son interprétation.", montre: ["ex"], accent: ["ex"] }
      ],
      source: "Schéma du site d'après La Structure des révolutions scientifiques (Kuhn, 1962). Exemple du cours."
    };
    ranger("t6-intro", 2, "t6kuhn");
  })();

  /* La cyberdéfense française : séparer la protection et l'attaque */
  (function () {
    var s = rect(0, 0, 640, 370, "var(--papier2)");
    s += k("etat", boite(200, 12, 240, 40, "L'ÉTAT", "var(--encre)", "Livre blanc 2008 : une menace majeure"));
    function col(id, x, titre, coul) { return k(id, rect(x, 70, 186, 210, coul, " opacity='.10' rx='6'") + ligne(x + 93, 52, x + 93, 70, coul, " stroke-width='2'") + t(x + 93, 90, titre, "lbl-f", "middle", "font-size:12px;fill:" + coul)); }
    function item(id, x, y, l1, l2) { return k(id, pt(x + 12, y - 4, "pt-b", 4) + t(x + 22, y, l1, "lbl") + (l2 ? t(x + 22, y + 15, l2, "lbl") : "")); }
    s += col("protege", 14, "PROTÉGER", "var(--acier)") + col("combat", 227, "COMBATTRE", "var(--rouge)") + col("informe", 440, "INFORMER", "var(--ok)");
    s += item("anssi", 14, 118, "ANSSI (7 juillet 2009)") + item("oiv", 14, 152, "opérateurs vitaux :", "règles (2013)") + item("cybm", 14, 200, "cybermalveillance (2017)") + item("jo", 14, 238, "JO 2024 : 548", "événements traités");
    s += item("comcyber", 227, 118, "COMCYBER (2017)") + item("lio", 227, 152, "doctrine offensive", "(18 janvier 2019)") + item("lpm", 227, 200, "2024-2030 : environ", "4 milliards d'euros");
    s += item("viginum", 440, 118, "Viginum (13 juil. 2021)") + item("rrn", 440, 152, "campagne RRN dévoilée", "(juin 2023)");
    s += k("mur", rect(209, 66, 10, 218, "var(--encre)") + t(214, 300, "séparés (revue stratégique, 2018)", "lbl-f", "middle", "font-size:11.5px"));
    s += k("ue", rect(14, 316, 612, 44, "var(--acier-pale)", " rx='6' stroke='var(--acier)'") + t(320, 334, "UNION EUROPÉENNE : directives NIS (2016) et NIS 2 (2022),", "lbl", "middle") + t(320, 350, "premières sanctions cyber (30 juillet 2020)", "lbl", "middle"));
    ANIMS.t6cyberfr = {
      titre: "La cyberdéfense française : protéger, combattre, informer",
      scene: { w: 640, h: 370, svg: s },
      etapes: [
        { date: "2008", titre: "Une menace majeure", texte: "Le Livre blanc sur la défense et la sécurité nationale fait des attaques informatiques une menace majeure.", montre: ["etat"], accent: ["etat"] },
        { date: "2009-2013", titre: "Protéger les systèmes", texte: "L'ANSSI est créée par décret le 7 juillet 2009 ; la loi de programmation militaire de 2013 impose des règles aux opérateurs d'importance vitale (énergie, transports, santé…).", montre: ["protege", "anssi", "oiv"], accent: ["anssi"] },
        { date: "2017-2019", titre: "Les armées dans le cyberespace", texte: "Le COMCYBER est créé en 2017 ; la France présente sa doctrine de lutte informatique offensive le 18 janvier 2019.", montre: ["combat", "comcyber", "lio"], accent: ["comcyber"] },
        { date: "12 févr. 2018", titre: "Le modèle français : séparer", texte: "L'ANSSI ne fait ni renseignement ni attaque, pour que les victimes lui fassent confiance : la défense et l'attaque sont séparées, contrairement aux États-Unis ou au Royaume-Uni.", montre: ["mur"], accent: ["mur"] },
        { date: "2021-2023", titre: "Défendre le débat public", texte: "Viginum (13 juillet 2021) détecte les ingérences numériques étrangères ; il révèle en juin 2023 la campagne russe RRN, qui imitait de grands médias français.", montre: ["informe", "viginum", "rrn"], accent: ["viginum"] },
        { date: "2016-2022", titre: "La coopération européenne", texte: "L'UE n'a pas d'armée cyber, mais elle harmonise les règles (NIS, NIS 2) et sanctionne (premières sanctions le 30 juillet 2020, contre les auteurs de WannaCry et NotPetya).", montre: ["ue"], accent: ["ue"] },
        { date: "2017-2024", titre: "Protéger toute la société", texte: "Cybermalveillance.gouv.fr (2017) aide les particuliers ; pendant les Jeux de Paris 2024, l'ANSSI traite 548 événements ; la LPM 2024-2030 prévoit environ 4 milliards d'euros pour le cyber.", montre: ["cybm", "jo", "lpm"], accent: ["jo", "lpm"] }
      ],
      source: "Schéma du site. Dates et chiffres du cours."
    };
    ranger("t6-otc", 2, "t6cyberfr");
  })();
})();
