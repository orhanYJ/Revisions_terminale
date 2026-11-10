/* ===== Animations explicatives des thèmes 1, 2 et 5 (responsable du site) =====
   Scènes cartographiques : cartes-anims.js (scene: "carte:nom") ; scènes schématiques construites ici. */
(function () {
  /* ---------- petits outils SVG pour les scènes schématiques ---------- */
  function t(x, y, s, cl, a) { return "<text x='" + x + "' y='" + y + "' class='" + (cl || "lbl") + "' text-anchor='" + (a || "start") + "'>" + s + "</text>"; }
  /* graphique : axes, graduations et une série découpée en segments animés */
  function graphe(o) {
    var W = o.w, H = o.h, g = { x0: 60, x1: W - 30, y0: H - 40, y1: 30 };
    function X(v) { return g.x0 + (v - o.xmin) / (o.xmax - o.xmin) * (g.x1 - g.x0); }
    function Y(v) { return g.y0 - (v - o.ymin) / (o.ymax - o.ymin) * (g.y0 - g.y1); }
    var s = "<path d='M" + g.x0 + "," + g.y1 + "V" + g.y0 + "H" + g.x1 + "' fill='none' stroke='var(--encre2)' stroke-width='1.5'/>";
    o.xt.forEach(function (v) { s += "<path d='M" + X(v) + "," + g.y0 + "v5' stroke='var(--encre2)'/>" + t(X(v), g.y0 + 18, v, "sch-pt", "middle"); });
    o.yt.forEach(function (v) { s += "<path d='M" + (g.x0 - 5) + "," + Y(v) + "H" + g.x1 + "' stroke='var(--ligne)' stroke-dasharray='2 4'/>" + t(g.x0 - 8, Y(v) + 4, v, "sch-pt", "end"); });
    s += t(g.x1, g.y1 - 12, o.unite, "sch-pt", "end");
    return { s: s, X: X, Y: Y };
  }
  function segment(k, pts, G, o) {
    o = o || {};
    var d = pts.map(function (p, i) { return (i ? "L" : "M") + G.X(p[0]).toFixed(1) + "," + G.Y(p[1]).toFixed(1); }).join("");
    return "<path data-k='" + k + "' class='trace' pathLength='1' d='" + d + "' fill='none' stroke='" + (o.c || "var(--rouge)") + "' stroke-width='" + (o.w || 3.5) + "' stroke-linejoin='round' stroke-linecap='round'" + (o.pointille ? " stroke-dasharray='6 5'" : "") + "/>";
  }
  function repere(k, x, y, txt, a, G, dy) {
    var X = G.X(x), Y = G.Y(y);
    return "<g data-k='" + k + "'><circle cx='" + X.toFixed(1) + "' cy='" + Y.toFixed(1) + "' r='6' class='pt-a'/>" + t((X + (a === "end" ? -10 : 10)).toFixed(1), (Y + (dy || -8)).toFixed(1), txt, "lbl", a || "start") + "</g>";
  }

  /* ====================== THÈME 1 ====================== */
  /* Des 3 milles aux 200 milles : l'appropriation de la mer (coupe schématique) */
  (function () {
    var s = "<rect width='640' height='300' fill='var(--k-mer)'/>";
    s += "<path d='M0 60H80V300H0Z' fill='var(--k-terre2)' stroke='var(--k-front)'/>" + t(12, 50, "CÔTE", "sch-pt");
    s += "<path d='M80 150Q200 160 330 172Q420 182 470 222Q520 262 640 270V300H80Z' fill='var(--k-terre)' stroke='var(--k-front)'/>";
    s += "<g data-k='libre'><rect x='80' y='60' width='560' height='70' fill='var(--acier)' fill-opacity='.25'/>" + t(360, 100, "MER LIBRE", "lbl-f", "middle") + "</g>";
    s += "<g data-k='canon'><rect x='80' y='60' width='22' height='70' fill='var(--rouge)' fill-opacity='.55'/>" + t(108, 80, "3 milles", "lbl") + "</g>";
    s += "<g data-k='plateau'><path d='M80 150Q200 160 330 172Q420 182 470 222' fill='none' stroke='var(--kraft-f)' stroke-width='7' stroke-linecap='round'/>" + t(200, 200, "plateau continental revendiqué", "lbl") + "</g>";
    s += "<g data-k='m200'><rect x='80' y='60' width='280' height='70' fill='none' stroke='var(--rouge)' stroke-width='2.5' stroke-dasharray='7 5'/>" + t(355, 52, "200 milles revendiqués", "lbl", "end") + "</g>";
    s += "<g data-k='mt'><rect x='80' y='60' width='30' height='70' fill='#3F7FA3'/>" + t(95, 145, "12", "sch-pt", "middle") + "</g>";
    s += "<g data-k='zc'><rect x='110' y='60' width='30' height='70' fill='#5E9AB8'/>" + t(125, 145, "24", "sch-pt", "middle") + "</g>";
    s += "<g data-k='zee'><rect x='140' y='60' width='220' height='70' fill='#8DB7CC' fill-opacity='.9'/>" + t(250, 100, "ZEE (200 milles)", "lbl-f", "middle") + "</g>";
    s += "<g data-k='pc'><path d='M330 172Q420 182 470 222' fill='none' stroke='var(--kraft-f)' stroke-width='7'/>" + t(470, 205, "jusqu'à 350 milles", "lbl") + "</g>";
    s += "<g data-k='zone'>" + t(570, 262, "« LA ZONE »", "lbl-f", "middle") + t(500, 100, "HAUTE MER", "lbl-f", "middle") + "</g>";
    s += "<g data-k='amp'><circle cx='540' cy='95' r='26' fill='var(--ok)' fill-opacity='.35' stroke='var(--ok)' stroke-width='2'/>" + t(540, 140, "aire marine protégée", "lbl", "middle") + "</g>";
    s += t(320, 292, "schéma sans échelle", "sch-pt", "middle");
    ANIMS.mer = { titre: "Des 3 milles aux 200 milles : comment les États se sont approprié la mer", scene: { w: 640, h: 300, svg: s },
      etapes: [
        { date: "1609", titre: "La mer libre", texte: "Le juriste hollandais Grotius défend la liberté des mers (<em>Mare liberum</em>) : la mer n'appartient à personne, chacun peut y naviguer et commercer.", montre: ["libre"] },
        { date: "XVIIIe s.", titre: "La portée du canon", texte: "Une étroite bande côtière revient à l'État riverain : sa largeur, liée à la portée d'un canon, se fixe peu à peu à 3 milles marins (environ 5,5 km).", montre: ["canon"], accent: ["canon"] },
        { date: "28 sept. 1945", titre: "La proclamation Truman", texte: "Les États-Unis revendiquent les ressources du sol et du sous-sol de leur plateau continental : la course aux ressources de la mer commence.", montre: ["plateau"], accent: ["plateau"] },
        { date: "18 août 1952", titre: "200 milles revendiqués", texte: "Par la déclaration de Santiago, le Chili, le Pérou et l'Équateur revendiquent 200 milles pour protéger leur pêche : d'autres États suivent.", montre: ["m200"], accent: ["m200"] },
        { date: "10 déc. 1982", titre: "Montego Bay fixe les zones", texte: "La convention des Nations unies sur le droit de la mer fixe la mer territoriale (12 milles), la zone contiguë (24), la ZEE (200) et le plateau continental (jusqu'à 350 sur dossier). Au-delà : la haute mer, et « la Zone », patrimoine commun de l'humanité.", montre: ["mt", "zc", "zee", "pc", "zone"], cache: ["canon", "m200", "plateau", "libre"], accent: ["zee"] },
        { date: "17 janv. 2026", titre: "Protéger la haute mer", texte: "Le traité BBNJ entre en vigueur : il permet de créer des aires marines protégées en haute mer, là où aucun État n'est souverain.", montre: ["amp"], accent: ["amp"] }
      ], source: "Schéma du site. Dates : convention des Nations unies sur le droit de la mer (1982), ONU (BBNJ)." };
  })();

  ANIMS.espace = { titre: "La course à l'espace sur la carte : qui sait lancer un satellite ?", scene: "carte:espace",
    etapes: [
      { date: "4 oct. 1957", titre: "L'URSS ouvre la course", texte: "Spoutnik 1 part de Baïkonour, lancé par un missile intercontinental R-7. Le 12 avril 1961, Gagarine y décolle aussi.", montre: ["baik"], accent: ["baik"] },
      { date: "31 janv. 1958", titre: "La riposte américaine", texte: "Les États-Unis placent Explorer 1 en orbite depuis Cap Canaveral ; la NASA est créée la même année.", montre: ["canav"], accent: ["canav"] },
      { date: "26 nov. 1965", titre: "La France, 3e puissance spatiale", texte: "La fusée Diamant place le satellite Astérix en orbite depuis Hammaguir, dans le Sahara algérien.", montre: ["hamm"], accent: ["hamm"] },
      { date: "20 juil. 1969", titre: "Apollo 11", texte: "Les États-Unis gagnent la course à la Lune : Armstrong et Aldrin y marchent. Six missions s'y posent jusqu'en 1972.", montre: ["lune1", "lune1t"], accent: ["canav"] },
      { date: "1970-1971", titre: "Le club s'élargit", texte: "Le Japon (11 février 1970, Uchinoura) et la Chine (24 avril 1970, Jiuquan), puis le Royaume-Uni (28 octobre 1971, depuis Woomera en Australie) lancent leur premier satellite.", montre: ["uchi", "jiuq", "woom"], cache: ["lune1", "lune1t"], accent: ["jiuq"] },
      { date: "24 déc. 1979", titre: "Ariane et l'Europe", texte: "Le premier lanceur Ariane décolle de Kourou (Guyane), près de l'équateur : l'Europe gagne son accès autonome à l'espace.", montre: ["kourou"], accent: ["kourou"] },
      { date: "1980-1988", titre: "L'Inde et Israël", texte: "L'Inde (18 juillet 1980, Sriharikota) puis Israël (19 septembre 1988, Palmachim) rejoignent le club.", montre: ["srih", "palm"], accent: ["srih", "palm"] },
      { date: "2009-2012", titre: "L'Iran et la Corée du Nord", texte: "Premiers satellites iranien (2 février 2009) et nord-coréen (12 décembre 2012) : les mêmes technologies servent aux missiles balistiques.", montre: ["semn", "sohae"], accent: ["semn", "sohae"] },
      { date: "2015-2024", titre: "Le New Space", texte: "SpaceX fait revenir ses lanceurs (2015) et réalise plus de la moitié des lancements mondiaux en 2024 ; Rocket Lab lance depuis la Nouvelle-Zélande (2018). La Chine ouvre Wenchang (2016) et construit sa station.", montre: ["starb", "mahia", "wench"], accent: ["starb", "wench"] },
      { date: "1er avril 2026", titre: "Retour vers la Lune", texte: "Artemis II emmène quatre astronautes autour de la Lune : nouvelle course, avec la Chine qui vise un atterrissage habité avant 2030.", montre: ["lune2", "lune2t"], accent: ["canav", "wench"] }
    ], source: "Fond Natural Earth. Dates des premiers lancements orbitaux nationaux ; positions approximatives." };

  /* La Station spatiale internationale s'assemble (schéma) */
  (function () {
    var s = "<rect width='640' height='300' fill='#0b1620'/>";
    for (var i = 0; i < 40; i++) s += "<circle cx='" + ((i * 157) % 640) + "' cy='" + ((i * 83) % 300) + "' r='" + (i % 3 ? 0.8 : 1.4) + "' fill='#dfe8ef' opacity='.6'/>";
    s += "<path d='M0 300Q320 230 640 300Z' fill='#2D5675' opacity='.8'/>";
    function mod(k, x, y, w, h, c, lab, ly) { return "<g data-k='" + k + "'><rect x='" + x + "' y='" + y + "' width='" + w + "' height='" + h + "' rx='6' fill='" + c + "' stroke='#fff' stroke-width='1.5'/>" + "<text x='" + (x + w / 2) + "' y='" + (ly || (y - 8)) + "' text-anchor='middle' class='lbl' style='fill:#fff;stroke:#0b1620'>" + lab + "</text></g>"; }
    s += mod("zarya", 250, 120, 80, 30, "#B07A1E", "Zarya (Russie)");
    s += mod("unity", 330, 122, 36, 26, "#82B2D8", "Unity", 174);
    s += mod("zvezda", 170, 120, 80, 30, "#C0841F", "Zvezda");
    s += "<g data-k='equip'><circle cx='210' cy='135' r='5' fill='#FF5B49'/><circle cx='224' cy='135' r='5' fill='#FF5B49'/><circle cx='238' cy='135' r='5' fill='#FF5B49'/></g>";
    s += mod("destiny", 366, 120, 70, 30, "#82B2D8", "Destiny (États-Unis)");
    s += "<g data-k='panneaux'><rect x='290' y='40' width='16' height='70' fill='#4a6a8a' stroke='#fff'/><rect x='290' y='160' width='16' height='70' fill='#4a6a8a' stroke='#fff'/><rect x='470' y='40' width='16' height='70' fill='#4a6a8a' stroke='#fff'/><rect x='470' y='160' width='16' height='70' fill='#4a6a8a' stroke='#fff'/><path d='M298 110V120M298 150V160M478 110V160M436 135H478' stroke='#fff' stroke-width='3'/></g>";
    s += mod("columbus", 436, 150, 60, 26, "#2F8F9C", "Columbus (Europe)", 194);
    s += mod("kibo", 436, 94, 70, 26, "#e9e9e9", "Kibo (Japon)", 86);
    s += "<g data-k='dragon'><path d='M150 135l-24-10v20z' fill='#ddd'/><text x='120' y='160' class='lbl' style='fill:#fff;stroke:#0b1620'>Crew Dragon</text></g>";
    s += "<g data-k='fin'><path d='M320 210C380 240 430 260 470 290' class='trace' pathLength='1' fill='none' stroke='#FF5B49' stroke-width='3' stroke-dasharray='1'/><text x='480' y='250' class='lbl' style='fill:#FF5B49;stroke:#0b1620'>désorbitation prévue</text></g>";
    s += "<text x='620' y='20' text-anchor='end' class='sch-pt' style='fill:#cfdbe4'>schéma simplifié, sans échelle</text>";
    ANIMS.iss = { titre: "La Station spatiale internationale, une coopération qui s'assemble", scene: { w: 640, h: 300, svg: s },
      etapes: [
        { date: "29 janv. 1998", titre: "Un accord à 15", texte: "États-Unis, Russie, Japon, Canada et onze États de l'Agence spatiale européenne signent l'accord intergouvernemental : la fin de la guerre froide rend possible la coopération.", montre: [] },
        { date: "20 nov. 1998", titre: "Le premier module est russe", texte: "Zarya est lancé depuis Baïkonour, puis relié au module américain Unity (décembre 1998).", montre: ["zarya", "unity"], accent: ["zarya"] },
        { date: "2 nov. 2000", titre: "Occupée en permanence", texte: "Après le module de service russe Zvezda (juillet 2000), le premier équipage s'installe : depuis, la station n'a jamais été vide.", montre: ["zvezda", "equip"], accent: ["equip"] },
        { date: "7 févr. 2001", titre: "Le laboratoire américain", texte: "Destiny est amarré : les segments russe et américain dépendent l'un de l'autre (propulsion russe, électricité américaine).", montre: ["destiny", "panneaux"], accent: ["destiny"] },
        { date: "2008", titre: "L'Europe et le Japon", texte: "Le laboratoire européen Columbus (février 2008) et le module japonais Kibo (2008-2009) complètent la station : environ 420 tonnes à 400 km d'altitude.", montre: ["columbus", "kibo"], accent: ["columbus", "kibo"] },
        { date: "2011-2020", titre: "Dépendre des Soyouz, puis de SpaceX", texte: "La navette américaine s'arrête en juillet 2011 : seuls les Soyouz russes rejoignent la station, jusqu'au premier vol habité de Crew Dragon (SpaceX) en mai 2020.", montre: ["dragon"], accent: ["dragon"] },
        { date: "2030", titre: "Une fin programmée", texte: "L'ISS doit être exploitée jusqu'en 2030, puis désorbitée au-dessus du Pacifique par un véhicule commandé à SpaceX ; la Chine, exclue depuis 2011, a déjà sa station Tiangong.", montre: ["fin"], accent: ["fin"] }
      ], source: "Schéma du site d'après les données de la NASA et de l'ESA ; modules principaux seulement." };
  })();

  ANIMS.scs = { titre: "La Chine s'avance en mer de Chine méridionale", scene: "carte:scs",
    etapes: [
      { date: "1947", titre: "Une ligne sur une carte", texte: "La République de Chine publie une carte avec une ligne en onze traits, réduite à neuf traits au début des années 1950 par la République populaire : elle englobe l'essentiel de la mer.", montre: ["ligne", "lignet", "cn", "vn", "ph"], accent: ["ligne"] },
      { date: "Janv. 1974", titre: "Les Paracels", texte: "La Chine prend aux forces sud-vietnamiennes la partie des îles Paracels qu'elle ne contrôlait pas encore.", montre: ["paracel"], accent: ["paracel"] },
      { date: "14 mars 1988", titre: "Johnson South Reef", texte: "Affrontement sino-vietnamien dans les Spratleys : 64 marins vietnamiens sont tués ; la Chine occupe plusieurs récifs.", montre: ["johnson"], accent: ["johnson"] },
      { date: "1995", titre: "Mischief", texte: "La Chine occupe le récif de Mischief, dans la zone revendiquée par les Philippines.", montre: ["mischief"], accent: ["mischief"] },
      { date: "2012", titre: "Scarborough et Sansha", texte: "Après un face-à-face avec les Philippines, la Chine contrôle de fait le récif de Scarborough ; elle crée la « ville de Sansha » sur l'île Woody pour administrer ses revendications.", montre: ["scarb", "woody", "sansha"], accent: ["scarb", "woody"] },
      { date: "2013-2016", titre: "Des îles artificielles", texte: "Remblais, pistes de 3 000 m, ports et radars sur Fiery Cross, Subi et Mischief : des récifs deviennent des bases.", montre: ["fiery", "subi", "iles", "ilest"], accent: ["iles"] },
      { date: "12 juil. 2016", titre: "Le droit dit non", texte: "Le tribunal arbitral saisi par les Philippines juge les « droits historiques » chinois sans base légale. Pékin rejette la sentence.", montre: ["pca"], accent: ["ligne"] },
      { date: "5 nov. 2025", titre: "La puissance navale", texte: "Le porte-avions Fujian entre en service à Sanya, sur l'île de Hainan, face à la mer de Chine méridionale.", montre: ["sanya"], accent: ["sanya"] }
    ], source: "Fond Natural Earth ; ligne en neuf traits tracée de façon approximative. Dates : sentence arbitrale (CPA, 2016), presse." };

  /* ====================== THÈME 2 ====================== */
  ANIMS.yemen = { titre: "Yémen : comment une guerre civile s'internationalise", scene: "carte:yemen",
    etapes: [
      { date: "21 sept. 2014", titre: "Les Houthis prennent Sanaa", texte: "Un mouvement armé du nord du Yémen, les Houthis, s'empare de la capitale : c'est d'abord une guerre civile, un conflit intraétatique.", montre: ["sanaa", "houthi", "aden"], accent: ["sanaa"] },
      { date: "26 mars 2015", titre: "Une coalition intervient", texte: "L'Arabie saoudite prend la tête d'une coalition d'États arabes pour rétablir le gouvernement : le conflit devient intraétatique internationalisé.", montre: ["riyad", "coal", "coalt"], accent: ["riyad"] },
      { date: "2015-2022", titre: "Une guerre par procuration ?", texte: "L'Iran, rival de l'Arabie saoudite, soutient les Houthis (armes, missiles, drones, selon les experts de l'ONU) : deux puissances régionales s'affrontent indirectement.", montre: ["iran", "irant"], accent: ["iran"] },
      { date: "2 avril 2022", titre: "Une trêve fragile", texte: "L'ONU obtient une trêve qui fait fortement baisser les combats, sans accord de paix : le front se fige, le pays reste divisé.", montre: ["hod", "treve"], accent: ["hod"] },
      { date: "Nov. 2023", titre: "La guerre gagne la mer Rouge", texte: "Après le 7 octobre 2023, les Houthis attaquent des navires marchands près du détroit de Bab el-Mandeb : un conflit local menace une route maritime mondiale.", montre: ["mer", "mert", "bab"], accent: ["bab"] },
      { date: "12 janv. 2024", titre: "Les grandes puissances s'en mêlent", texte: "Les États-Unis et le Royaume-Uni frappent les Houthis ; l'Union européenne lance l'opération navale Aspides (février 2024).", montre: ["usuk", "usukt"], accent: ["usuk"] }
    ], source: "Fond Natural Earth ; flèches schématiques. Sources : ONU (trêve de 2022, groupe d'experts), presse internationale." };

  ANIMS.daech = { titre: "Daech : l'essor puis la chute d'un proto-État (2014-2019)", scene: "carte:daech",
    etapes: [
      { date: "Janv. 2014", titre: "Raqqa et Falloujah", texte: "Profitant de la guerre civile syrienne et de la colère des sunnites d'Irak, l'« État islamique en Irak et au Levant » prend le contrôle de Raqqa (Syrie) et de Falloujah (Irak).", montre: ["raqqa_r", "fallu_r", "bagdad", "damas", "syr", "irq", "tur"], accent: ["raqqa_r", "fallu_r"] },
      { date: "Juin 2014", titre: "Mossoul et le « califat »", texte: "Mossoul tombe le 10 juin, Tikrit le lendemain. Le 29 juin, Daech proclame un « califat » à cheval sur la frontière Irak-Syrie.", montre: ["mos_r", "tik_r", "calif"], accent: ["mos_r"] },
      { date: "Août 2014", titre: "Sinjar et la coalition", texte: "Daech prend Sinjar et massacre les Yézidis ; le 8 août, les États-Unis lancent leurs premières frappes, bientôt suivis par une coalition internationale (dont la France, opération Chammal).", montre: ["sinj_r"], accent: ["sinj_r"] },
      { date: "Janv. 2015", titre: "Kobané résiste", texte: "Après quatre mois de siège, les combattants kurdes, appuyés par les frappes de la coalition, repoussent Daech de Kobané (26 janvier 2015) : premier coup d'arrêt.", montre: ["kob_b"], cache: ["calif"], accent: ["kob_b"] },
      { date: "Mai 2015", titre: "L'apogée", texte: "Tikrit a été reprise (avril), mais Daech prend Ramadi (17 mai) et Palmyre (21 mai) : son territoire est à son maximum, peuplé de plusieurs millions d'habitants.", montre: ["tik_b", "ram_r", "palm_r"], cache: ["tik_r"], accent: ["ram_r", "palm_r"] },
      { date: "Fin 2015 - 2016", titre: "Le recul", texte: "Sinjar (13 novembre 2015), Ramadi (décembre 2015), Palmyre (27 mars 2016, reperdue en décembre puis reprise en mars 2017) et Falloujah (juin 2016) sont reprises.", montre: ["sinj_b", "ram_b", "palm_b", "fallu_b"], cache: ["sinj_r", "ram_r", "palm_r", "fallu_r"], accent: ["fallu_b"] },
      { date: "Juil.-oct. 2017", titre: "Mossoul et Raqqa", texte: "Après neuf mois de bataille urbaine, Mossoul est reprise en juillet 2017 ; Raqqa tombe en octobre face aux Forces démocratiques syriennes.", montre: ["mos_b", "raqqa_b"], cache: ["mos_r", "raqqa_r"], accent: ["mos_b", "raqqa_b"] },
      { date: "23 mars 2019", titre: "Baghouz : la fin du territoire", texte: "Le dernier réduit tombe : le « califat » territorial disparaît, mais Daech survit en réseau clandestin et dans ses branches (Afrique, Afghanistan).", montre: ["bagh_b"], accent: ["bagh_b"] }
    ], source: "Fond Natural Earth. Rouge : ville tenue par Daech ; bleu : ville reprise ou défendue. Dates : presse internationale, coalition." };

  ANIMS.annan = { titre: "L'ONU sous Kofi Annan : des échecs aux nouvelles opérations de paix", scene: "carte:annan",
    etapes: [
      { date: "1994-1995", titre: "Deux échecs fondateurs", texte: "Génocide des Tutsis au Rwanda (1994), massacre de Srebrenica (1995) : les casques bleus n'ont ni le mandat ni les moyens d'empêcher les crimes.", montre: ["rwanda", "srebr"], accent: ["rwanda", "srebr"] },
      { date: "1er janv. 1997", titre: "Kofi Annan secrétaire général", texte: "Ancien responsable des opérations de maintien de la paix, il fait publier en 1999 les rapports qui reconnaissent les fautes de l'ONU.", montre: ["ny"], accent: ["ny"] },
      { date: "1999", titre: "Des missions d'un nouveau type", texte: "Kosovo (juin), Timor oriental (octobre), Sierra Leone (octobre), RDC (novembre) : l'ONU administre des territoires, désarme, protège les civils.", montre: ["kosovo", "timor", "sleone", "rdc"], accent: ["timor"] },
      { date: "2000", titre: "Le rapport Brahimi", texte: "Mandats clairs et moyens suffisants pour les casques bleus ; une mission s'interpose entre l'Éthiopie et l'Érythrée.", montre: ["eth"], accent: ["eth"] },
      { date: "2003", titre: "L'ONU contournée", texte: "Les États-Unis et le Royaume-Uni envahissent l'Irak sans mandat ; au même moment, une mission est déployée au Liberia.", montre: ["irak", "liberia"], accent: ["irak"] },
      { date: "2004-2005", titre: "Encore plus de casques bleus", texte: "Côte d'Ivoire, Haïti, Burundi (2004), Soudan (2005) ; le Sommet mondial de 2005 adopte la responsabilité de protéger.", montre: ["civ", "haiti", "burundi", "soudan"], accent: ["soudan"] },
      { date: "11 août 2006", titre: "Le Liban", texte: "Après la guerre entre Israël et le Hezbollah, la résolution 1701 renforce la FINUL. Kofi Annan quitte ses fonctions le 31 décembre 2006.", montre: ["liban"], accent: ["liban"] }
    ], source: "Fond Natural Earth. Résolutions du Conseil de sécurité ; positions approximatives." };

  ANIMS.golfe = { titre: "Des guerres du Golfe aux conflits asymétriques", scene: "carte:golfe",
    etapes: [
      { date: "1980-1988", titre: "La guerre Iran-Irak", texte: "Huit ans de guerre entre les deux puissances du Golfe laissent l'Irak de Saddam Hussein ruiné et endetté.", montre: ["iriq", "teh", "bag"], accent: ["iriq"] },
      { date: "2 août 1990", titre: "L'invasion du Koweït", texte: "L'Irak envahit et annexe le Koweït ; le Conseil de sécurité condamne (résolution 660) puis autorise la force (résolution 678).", montre: ["inv", "kow"], cache: ["iriq"], accent: ["kow"] },
      { date: "17 janv. - 28 févr. 1991", titre: "Tempête du désert", texte: "Une coalition de 35 pays sous mandat de l'ONU libère le Koweït : une guerre interétatique classique et légale.", montre: ["coal", "coalt"], accent: ["coal"] },
      { date: "1991-2003", titre: "Un Irak sous contrôle", texte: "Saddam Hussein reste au pouvoir ; zones d'exclusion aérienne au nord et au sud, inspections, sanctions.", montre: ["nfz", "nfzt"], cache: ["inv", "coal", "coalt"], accent: ["nfz"] },
      { date: "20 mars - 9 avril 2003", titre: "L'invasion sans l'ONU", texte: "Les États-Unis et le Royaume-Uni envahissent l'Irak et prennent Bagdad le 9 avril, sans nouvelle résolution du Conseil de sécurité.", montre: ["inv03", "bag03"], cache: ["nfz", "nfzt"], accent: ["bag"] },
      { date: "2004-2007", titre: "Le conflit devient asymétrique", texte: "Insurrection, attentats, Al-Qaïda en Irak, guerre civile entre sunnites et chiites : la plus puissante armée du monde affronte des combattants irréguliers.", montre: ["civ"], cache: ["inv03"], accent: ["bag"] },
      { date: "Juin 2014", titre: "Daech", texte: "Héritier d'Al-Qaïda en Irak, Daech prend Mossoul : la guerre de 2003 a nourri le djihadisme.", montre: ["mos"], accent: ["mos"] },
      { date: "28 févr. 2026", titre: "Le Golfe toujours au cœur des tensions", texte: "Les États-Unis et Israël lancent une guerre contre l'Iran ; Téhéran riposte et ferme le détroit d'Ormuz, par où transite une grande part du pétrole mondial.", montre: ["ormuz"], accent: ["ormuz", "teh"] }
    ], source: "Fond Natural Earth ; flèches schématiques. Résolutions du Conseil de sécurité ; presse internationale (2026)." };

  /* ====================== THÈME 5 ====================== */
  (function () {
    var G = graphe({ w: 640, h: 320, xmin: 1955, xmax: 2027, ymin: 300, ymax: 440, xt: [1960, 1970, 1980, 1990, 2000, 2010, 2020], yt: [320, 360, 400, 440], unite: "CO₂ à Mauna Loa (ppm, moyenne annuelle)" });
    var D = [[1959, 316.0], [1965, 320.0], [1970, 325.7], [1975, 331.1], [1980, 338.8], [1985, 346.1], [1990, 354.5], [1995, 360.8], [2000, 369.7], [2005, 380.0], [2010, 389.9], [2015, 401.0], [2020, 414.2], [2024, 424.6]];
    function morceau(a, b) { return D.filter(function (p) { return p[0] >= a && p[0] <= b; }); }
    var s = "<rect width='640' height='320' fill='var(--papier2)'/>" + G.s;
    s += segment("c1", morceau(1959, 1970), G) + segment("c2", morceau(1970, 1990), G) + segment("c3", morceau(1990, 2015), G) + segment("c4", morceau(2015, 2024), G);
    s += repere("e1962", 1962, 318.5, "1962 : Carson", "start", G, 22) + repere("e1972", 1972, 327.5, "1972 : Stockholm", "start", G, 22) + repere("e1988", 1988, 351.5, "1988 : GIEC", "start", G, 22) + repere("e1992", 1992, 356.4, "1992 : Rio", "end", G, -12) + repere("e2015", 2015, 401.0, "2015 : Paris, 400 ppm", "end", G, -12) + repere("e2025", 2025, 430.5, "mai 2025 : 430,5", "end", G, -10);
    ANIMS.keeling = { titre: "La courbe de Keeling : le CO₂ monte, la prise de conscience suit", scene: { w: 640, h: 320, svg: s },
      etapes: [
        { date: "1958", titre: "Mesurer l'atmosphère", texte: "Le chimiste Charles David Keeling commence à mesurer le CO₂ à l'observatoire de Mauna Loa (Hawaï), loin de toute pollution locale : environ 316 ppm en 1959, contre environ 280 ppm avant l'ère industrielle.", montre: ["c1"] },
        { date: "1962-1972", titre: "Les premières alertes", texte: "Rachel Carson publie <em>Printemps silencieux</em> (1962) ; la conférence de Stockholm (1972) fait de l'environnement une question internationale. Le CO₂ continue de monter.", montre: ["e1962", "e1972", "c2"], accent: ["e1972"] },
        { date: "1988-1992", titre: "Le climat entre en diplomatie", texte: "Création du GIEC (1988), Sommet de la Terre de Rio et convention sur le climat (1992). Le CO₂ dépasse 350 ppm.", montre: ["e1988", "e1992"], accent: ["e1992"] },
        { date: "2015", titre: "L'accord de Paris", texte: "La moyenne annuelle dépasse 400 ppm ; l'accord de Paris vise à limiter le réchauffement nettement en dessous de 2 °C.", montre: ["c3", "e2015"], accent: ["e2015"] },
        { date: "2024-2025", titre: "Toujours plus haut", texte: "Moyenne annuelle d'environ 424,6 ppm en 2024 ; 430,5 ppm en moyenne mensuelle en mai 2025 (NOAA). Malgré les accords, la courbe n'a jamais baissé.", montre: ["c4", "e2025"], accent: ["e2025"] }
      ], source: "Moyennes annuelles de l'observatoire de Mauna Loa (NOAA / Scripps), arrondies au dixième ; mai 2025 : moyenne mensuelle." };
  })();

  (function () {
    var G = graphe({ w: 640, h: 320, xmin: 1650, xmax: 2030, ymin: 0, ymax: 20, xt: [1669, 1750, 1827, 1900, 1950, 2024], yt: [0, 5, 10, 15, 20], unite: "Forêt de France métropolitaine (millions d'hectares)" });
    var s = "<rect width='640' height='320' fill='var(--papier2)'/>" + G.s;
    s += segment("approx", [[1830, 9], [1985, 14.1]], G, { c: "var(--ok)", pointille: true });
    s += segment("mesure", [[1985, 14.1], [2022, 17.1], [2024, 17.5]], G, { c: "var(--ok)", w: 4.5 });
    s += repere("p1830", 1830, 9, "vers 1830 : ~9 (minimum)", "start", G, 22) + repere("p1985", 1985, 14.1, "1985 : 14,1", "end", G, -12) + repere("p2024", 2024, 17.5, "2024 : 17,5 (32 %)", "end", G, -14);
    function evt(k, an, lab, y, a) { return "<g data-k='" + k + "'><path d='M" + G.X(an) + "," + G.Y(0) + "V" + G.Y(y) + "' stroke='var(--rouge)' stroke-width='1.5' stroke-dasharray='3 3'/>" + t(G.X(an) + (a === "end" ? -4 : 4), G.Y(y) - 4, lab, "lbl", a) + "</g>"; }
    s += evt("colbert", 1669, "1669 : Colbert", 15) + evt("code", 1827, "1827 : Code forestier", 4) + evt("landes", 1857, "1857 : Landes", 13) + evt("rtm", 1882, "1860-1882 : montagnes", 15.8) + evt("ffn", 1946, "1946 : Fonds forestier", 6) + evt("crises", 1999, "1999 tempêtes, 2022 incendies", 11, "end");
    s += "<g data-k='leg'>" + t(G.X(1700), G.Y(18.5), "pointillés : estimations ; trait plein : inventaires de l'IGN", "sch-pt") + "</g>";
    ANIMS.foret = { titre: "La forêt française : défrichement, puis reconquête", scene: { w: 640, h: 320, svg: s },
      etapes: [
        { date: "1669", titre: "Préserver pour la marine", texte: "Colbert fait adopter l'ordonnance sur les eaux et forêts : on règle les coupes, on réserve de grands arbres pour les navires du roi. On ne connaît pas précisément la surface boisée de l'époque.", montre: ["colbert", "leg"], accent: ["colbert"] },
        { date: "Vers 1830", titre: "Le minimum", texte: "Besoins en bois de chauffage, en charbon de bois et en terres agricoles : la forêt ne couvre plus qu'environ 9 millions d'hectares. Le Code forestier (1827) organise la gestion des forêts publiques.", montre: ["code", "p1830"], accent: ["p1830"] },
        { date: "1857-1882", titre: "Planter et reboiser", texte: "L'État fait boiser les landes de Gascogne (1857) et reboiser les montagnes contre l'érosion et les crues (lois de 1860 et 1882).", montre: ["landes", "rtm"], accent: ["landes", "rtm"] },
        { date: "1850-1985", titre: "La reconquête", texte: "L'exode rural libère des terres qui se reboisent ; le Fonds forestier national (1946) finance des plantations. La forêt progresse lentement.", montre: ["approx", "ffn", "p1985"], accent: ["p1985"] },
        { date: "2024", titre: "Presque le double… mais fragile", texte: "17,5 millions d'hectares, 32 % du territoire (IGN). Mais tempêtes (1999), incendies (2022), sécheresses et insectes : la mortalité des arbres a doublé en dix ans.", montre: ["mesure", "p2024", "crises"], accent: ["p2024"] }
      ], source: "IGN (inventaire forestier, 1985-2024) ; vers 1830, ordre de grandeur estimé par les historiens de la forêt ; entre 1830 et 1985, tracé indicatif (la progression n'a pas été régulière)." };
  })();

  (function () {
    var G = graphe({ w: 640, h: 320, xmin: 900, xmax: 1920, ymin: -1, ymax: 1, xt: [1000, 1200, 1400, 1600, 1800, 1900], yt: [], unite: "Température en Europe : schéma qualitatif (plus chaud ↑ / plus froid ↓)" });
    var s = "<rect width='640' height='320' fill='var(--papier2)'/>" + G.s + "<path d='M" + G.X(900) + "," + G.Y(0) + "H" + G.X(1920) + "' stroke='var(--encre2)' stroke-dasharray='4 4'/>";
    s += segment("doux", [[900, 0.2], [950, 0.45], [1050, 0.55], [1150, 0.5], [1250, 0.35]], G, { c: "var(--rouge)" });
    s += segment("bascule", [[1250, 0.35], [1260, 0.0], [1300, 0.05], [1320, -0.2], [1400, -0.15]], G, { c: "var(--acier)" });
    s += segment("pag", [[1400, -0.15], [1500, -0.3], [1565, -0.45], [1650, -0.55], [1700, -0.6], [1720, -0.4], [1780, -0.35], [1816, -0.65], [1850, -0.45]], G, { c: "var(--acier)" });
    s += segment("fin", [[1850, -0.45], [1880, -0.3], [1920, -0.05]], G, { c: "var(--rouge)" });
    function evt(k, an, y, lab, a, dy) { return repere(k, an, y, lab, a, G, dy); }
    s += evt("vikings", 985, 0.5, "v. 985 : Vikings au Groenland", "start", -10) + evt("samalas", 1257, 0.1, "1257 : éruption du Samalas", "start", 18) + evt("famine", 1316, -0.18, "1315-1317 : grande famine", "start", 20);
    s += evt("bruegel", 1565, -0.45, "1565 : Bruegel", "end", 18) + evt("maunder", 1680, -0.58, "1645-1715 : soleil peu actif", "end", -14) + evt("hiver", 1709, -0.6, "1709 : grand hiver", "start", 24) + evt("tambora", 1816, -0.65, "1816 : année sans été", "end", 36) + evt("glaciers", 1850, -0.45, "v. 1850 : glaciers au maximum", "end", -70);
    ANIMS.climat = { titre: "Le climat de l'Europe du Moyen Âge au XIXe siècle", scene: { w: 640, h: 320, svg: s },
      etapes: [
        { date: "950-1250", titre: "Une période douce", texte: "Étés plus chauds en Europe : les cultures progressent vers le nord et en altitude ; des Norvégiens s'installent au Groenland vers 985.", montre: ["doux", "vikings"], accent: ["vikings"] },
        { date: "1257-1317", titre: "La bascule", texte: "Une éruption géante (Samalas, en Indonésie, 1257) refroidit le climat ; les étés pourris de 1315-1317 provoquent une grande famine en Europe du Nord.", montre: ["bascule", "samalas", "famine"], accent: ["famine"] },
        { date: "XVIe-XVIIe s.", titre: "Le petit âge glaciaire", texte: "Hivers rudes, fleuves gelés, glaciers qui avancent ; entre 1645 et 1715, le soleil est particulièrement peu actif (minimum de Maunder).", montre: ["pag", "bruegel", "maunder"], accent: ["maunder"] },
        { date: "1709-1816", titre: "Des crises de subsistance", texte: "Le grand hiver de 1709 provoque une famine meurtrière en France ; l'éruption du Tambora (1815) entraîne l'« année sans été » de 1816.", montre: ["hiver", "tambora"], accent: ["hiver", "tambora"] },
        { date: "Après 1850", titre: "La fin du petit âge glaciaire", texte: "Les glaciers alpins, au maximum vers 1850, commencent à reculer. Au XXe siècle, le réchauffement d'origine humaine prend le relais : il est plus rapide et mondial.", montre: ["fin", "glaciers"], accent: ["glaciers"] }
      ], source: "Schéma qualitatif du site (pas une courbe de mesures), d'après les synthèses d'histoire du climat (E. Le Roy Ladurie) et le GIEC." };
  })();

  ANIMS.cop = { titre: "Des Sommets de la Terre aux COP : la diplomatie du climat", scene: "carte:cop",
    etapes: [
      { date: "1972", titre: "Stockholm", texte: "Première conférence de l'ONU sur l'environnement ; création du PNUE.", montre: ["stock"], accent: ["stock"] },
      { date: "1992", titre: "Rio, le Sommet de la Terre", texte: "Convention-cadre sur les changements climatiques : responsabilités communes mais différenciées.", montre: ["rio"], accent: ["rio"] },
      { date: "1995-1997", titre: "Berlin et Kyoto", texte: "Première COP (Berlin, 1995) ; protocole de Kyoto (1997) : des objectifs pour les seuls pays industrialisés, sans les États-Unis.", montre: ["berlin", "kyoto"], accent: ["kyoto"] },
      { date: "2009", titre: "Copenhague, l'échec", texte: "La COP15 ne parvient pas à un accord contraignant pour remplacer Kyoto.", montre: ["copen"], accent: ["copen"] },
      { date: "2015", titre: "Paris", texte: "Accord universel : nettement en dessous de 2 °C, viser 1,5 °C ; chaque État fixe ses engagements.", montre: ["paris"], accent: ["paris"] },
      { date: "2021-2024", titre: "Glasgow, Dubaï, Bakou", texte: "Réduction progressive du charbon (2021), « transition hors des énergies fossiles » (2023), 300 milliards de dollars par an d'ici 2035 pour les pays en développement (2024).", montre: ["glasg", "dubai", "bakou"], accent: ["dubai"] },
      { date: "2025-2026", titre: "Belém, Washington, Antalya", texte: "À Belém (2025), pas de feuille de route sur les fossiles dans la décision finale ; les États-Unis sortent de l'accord de Paris (27 janvier 2026) ; la COP31 se tient à Antalya du 9 au 20 novembre 2026.", montre: ["belem", "wash", "antal"], accent: ["wash", "antal"] }
    ], source: "Fond Natural Earth. CCNUCC, presse spécialisée." };

  ANIMS.usa = { titre: "Les États-Unis : exploiter, protéger, se diviser", scene: "carte:usa",
    etapes: [
      { date: "1862-1889", titre: "La conquête des Plaines", texte: "Homestead Act (1862), chemins de fer, labours : les bisons, plusieurs dizaines de millions, sont presque exterminés (environ un millier en 1889).", montre: ["plaines"], accent: ["plaines"] },
      { date: "1872-1913", titre: "Préserver la nature sauvage", texte: "Yellowstone, premier parc national (1872) ; John Muir et le Sierra Club (1892) défendent Yosemite, mais la vallée de Hetch Hetchy est noyée par un barrage (1913).", montre: ["yell", "yose"], accent: ["yell"] },
      { date: "Années 1930", titre: "Le Dust Bowl", texte: "Sécheresse et labour intensif : des tempêtes de poussière ruinent les Grandes Plaines (14 avril 1935) ; le New Deal crée un service de conservation des sols.", montre: ["dust", "dustz"], accent: ["dustz"] },
      { date: "1969-1973", titre: "La révolution des lois", texte: "La rivière Cuyahoga prend feu (1969) ; Jour de la Terre et EPA (1970) ; lois sur l'air (1970), l'eau (1972), les espèces menacées (1973).", montre: ["cuya", "wash"], accent: ["wash"] },
      { date: "1989-2010", titre: "Les marées noires", texte: "Exxon Valdez en Alaska (1989), Deepwater Horizon dans le golfe du Mexique (2010) : le prix de l'exploitation pétrolière.", montre: ["valdez", "dwh"], accent: ["dwh"] },
      { date: "Depuis 2018", titre: "Premier producteur de pétrole", texte: "Le pétrole de schiste du bassin permien fait des États-Unis le premier producteur mondial de pétrole.", montre: ["perm"], accent: ["perm"] },
      { date: "2017-2026", titre: "Un pays divisé", texte: "La Californie et d'autres États résistent aux retraits fédéraux de l'accord de Paris ; en 2025-2026, l'État fédéral démantèle des règles climatiques et quitte de nouveau l'accord (27 janvier 2026).", montre: ["calif"], accent: ["calif", "wash"] }
    ], source: "Fond Natural Earth ; zone du Dust Bowl approximative. EPA, NPS, EIA, presse." };
})();
