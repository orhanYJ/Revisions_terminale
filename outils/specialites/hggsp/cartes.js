/* Cartes du site HGGSP (hggsp/) : fonds Natural Earth 1:50m (pays actuels), d3-geo local
   (dnl/cartes/d3-geo.min.js), simplification Douglas-Peucker, chemins M/L/Z.
   Usage : appelé par build.py (node cartes.js ne_50m_admin_0_countries.geojson src/cartes.json).
   La sortie (fonds + cartes + calques d'animation) est collée dans hggsp/index.html (constante CARTES).
   Chaque carte : { w, h, fond (« monde » ou chemin propre), deco (SVG fixe), pts : points cliquables
   { c : couche, x, y, n : étiquette courte, a : ancre de l'étiquette, t : titre, d : texte } }. */
const fs = require("fs"), vm = require("vm"), path = require("path");
const ctx = {}; ctx.globalThis = ctx;
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "../../../dnl/cartes/d3-geo.min.js"), "utf8"), ctx);
const d3 = ctx.d3;

function dp(pts, tol) {
  if (pts.length < 3) return pts;
  const keep = new Uint8Array(pts.length); keep[0] = keep[pts.length - 1] = 1;
  const st = [[0, pts.length - 1]];
  while (st.length) {
    const [a, b] = st.pop(); let md = -1, mi = -1;
    const [x1, y1] = pts[a], [x2, y2] = pts[b], dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy);
    for (let i = a + 1; i < b; i++) {
      /* extrémités confondues (anneau refermé sur son premier point) : distance au point, sinon tout l'anneau disparaîtrait */
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
const geo = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const FEAT = geo.features.filter(f => f.properties.ADMIN !== "Antarctica");

function cadre(proj, W, H, tol, minAire) {
  proj.clipExtent([[0, 0], [W, H]]);
  const gp = d3.geoPath(proj).digits(1);
  const P = ll => proj(ll).map(v => Math.round(v));
  const pays = (filtre) => FEAT.filter(filtre || (() => true)).map(f => simplifier(gp(f), tol, minAire)).join("");
  const ligne = (coords, attrs) => '<path d="' + simplifier(gp({ type: "LineString", coordinates: coords }), 0.3, 0) + '" fill="none" ' + attrs + "/>";
  const poly = (ring, attrs) => '<path d="' + simplifier(gp({ type: "Polygon", coordinates: [ring] }), 0.3, 0) + '" ' + attrs + "/>";
  const txt = (ll, s, o = {}) => { const [x, y] = P(ll); return '<text x="' + (x + (o.dx || 0)) + '" y="' + (y + (o.dy || 0)) + '" class="' + (o.cl || "k-pays") + '"' + (o.a ? ' text-anchor="' + o.a + '"' : "") + ">" + esc(s) + "</text>"; };
  return { gp, P, pays, ligne, poly, txt };
}

const OUT = { cartes: {} };

/* ---------------- fond du monde (Equal Earth, sans l'Antarctique) ---------------- */
const WM = 1000;
const pm = d3.geoEqualEarth().rotate([-10, 0]);
pm.fitWidth(WM - 8, { type: "Sphere" }); pm.translate([WM / 2, pm.translate()[1]]);
const yN = pm([10, 80])[1], yS = pm([10, -56])[1];
pm.translate([pm.translate()[0], pm.translate()[1] - yN + 6]);
const HM = Math.round(yS - yN + 12);
const M = cadre(pm, WM, HM, 0.55, 2.5);
OUT.monde = { w: WM, h: HM, terre: M.pays(), grat: simplifier(M.gp(d3.geoGraticule().step([30, 30])()), 0.6, 0) };
const pt = (c, ll, n, a, t, d) => { const [x, y] = M.P(ll); return { c, x, y, n, a, t, d }; };

/* ---------------- 1. Les océans, espaces de puissance ---------------- */
{
  const chokes = [[[56.3, 26.6], "Ormuz"], [[43.4, 12.6], "Bab el-Mandeb"], [[32.4, 30.5], "Suez"], [[101.5, 2.6], "Malacca"], [[-79.7, 9.1], "Panama"], [[-5.6, 35.95], "Gibraltar"]];
  let deco = "";
  chokes.forEach(([ll, n]) => { const [x, y] = M.P(ll); deco += '<g class="k-choke"><path d="M' + (x - 4) + "," + (y - 4) + "L" + (x + 4) + "," + (y + 4) + "M" + (x + 4) + "," + (y - 4) + "L" + (x - 4) + "," + (y + 4) + '"/></g>'; });
  deco += M.txt([-100, 40], "ÉTATS-UNIS", { a: "middle" }) + M.txt([100, 62], "RUSSIE", { a: "middle" }) + M.txt([103, 33], "CHINE", { a: "middle" }) + M.txt([77, 26], "INDE", { a: "middle" }) +
    M.txt([-35, 30], "OCÉAN ATLANTIQUE", { cl: "k-mer", a: "middle" }) + M.txt([-150, 5], "OCÉAN PACIFIQUE", { cl: "k-mer", a: "middle" }) + M.txt([78, -25], "OCÉAN INDIEN", { cl: "k-mer", a: "middle" });
  const pts = [
    pt("snle", [-4.5, 48.3], "Île Longue", "end", "Île Longue (France)", "Base des 4 sous-marins nucléaires lanceurs d'engins (SNLE) français, en rade de Brest. Au moins un SNLE est en patrouille en permanence depuis 1972."),
    pt("snle", [-4.8, 56.1], "Faslane", "end", "Faslane (Royaume-Uni)", "Base écossaise des 4 SNLE britanniques de la classe Vanguard, armés de missiles Trident d'origine américaine."),
    pt("snle", [-81.5, 30.8], "Kings Bay", "end", "Kings Bay (États-Unis)", "Base des SNLE de la classe Ohio sur l'Atlantique (Géorgie). La marine américaine en compte 14 au total."),
    pt("snle", [-122.7, 47.7], "Bangor", "end", "Bangor (États-Unis)", "Base des SNLE de la classe Ohio sur le Pacifique (État de Washington)."),
    pt("snle", [33.3, 69.3], "Gadjievo", "start", "Gadjievo (Russie)", "Base des SNLE de la flotte du Nord, près de Mourmansk, avec un accès direct à l'Arctique et à l'Atlantique."),
    pt("snle", [158.4, 52.9], "Vilioutchinsk", "end", "Vilioutchinsk (Russie)", "Base des SNLE de la flotte du Pacifique, au Kamtchatka."),
    pt("snle", [109.6, 18.2], "Yulin (Hainan)", "start", "Yulin, île de Hainan (Chine)", "Base des SNLE chinois (type 094), avec des abris souterrains. Elle ouvre sur la mer de Chine méridionale, que Pékin cherche à contrôler pour y faire patrouiller ses sous-marins à l'abri."),
    pt("snle", [83.2, 17.7], "Visakhapatnam", "end", "Visakhapatnam (Inde)", "Port d'attache de la flotte de l'Est indienne ; l'Inde arme des SNLE depuis l'INS Arihant (en service en 2016)."),
    pt("us", [-76.3, 36.9], "Norfolk", "start", "Norfolk (États-Unis)", "Plus grande base navale du monde, sur l'Atlantique."),
    pt("us", [-117.2, 32.7], "San Diego", "end", "San Diego (États-Unis)", "Grande base de la flotte du Pacifique."),
    pt("us", [50.6, 26.2], "Bahreïn", "start", "Manama, Bahreïn", "Quartier général de la 5e flotte américaine, face à l'Iran et au détroit d'Ormuz."),
    pt("us", [14.3, 40.8], "Naples", "start", "Naples (Italie)", "Quartier général de la 6e flotte américaine (Méditerranée)."),
    pt("us", [139.7, 35.3], "Yokosuka", "start", "Yokosuka (Japon)", "Quartier général de la 7e flotte, la plus grande flotte américaine déployée hors des États-Unis, avec un porte-avions basé en permanence au Japon."),
    pt("us", [144.7, 13.4], "Guam", "start", "Guam (États-Unis)", "Île américaine du Pacifique occidental : base de sous-marins et de bombardiers, à environ 3 000 km de la Chine."),
    pt("us", [72.4, -7.3], "Diego Garcia", "start", "Diego Garcia (archipel des Chagos)", "Base américano-britannique au cœur de l'océan Indien. Un traité signé en mai 2025 prévoit de rendre l'archipel à Maurice tout en louant la base au Royaume-Uni pour 99 ans."),
    pt("fr", [5.9, 43.1], "Toulon", "start", "Toulon (France)", "Premier port militaire français, port d'attache du porte-avions Charles-de-Gaulle (en service depuis 2001)."),
    pt("fr", [43.15, 11.5], "Djibouti", "end", "Djibouti", "Base française (la plus importante hors de France) et, depuis le 1er août 2017, première base militaire chinoise à l'étranger, à quelques kilomètres l'une de l'autre, au débouché du détroit de Bab el-Mandeb."),
    pt("fr", [54.4, 24.5], "Abu Dhabi", "end", "Abu Dhabi (Émirats arabes unis)", "Base interarmées française ouverte en 2009, face au détroit d'Ormuz."),
    pt("fr", [55.5, -20.9], "La Réunion", "start", "La Réunion (France)", "Point d'appui français dans l'océan Indien, qui surveille aussi les îles Éparses et leur ZEE."),
    pt("fr", [166.4, -22.3], "Nouméa", "end", "Nouméa (France)", "Point d'appui français dans le Pacifique Sud (Nouvelle-Calédonie)."),
    pt("fr", [-149.6, -17.5], "Papeete", "start", "Papeete (France)", "Point d'appui français en Polynésie : il surveille la plus vaste ZEE française.")
  ];
  OUT.cartes.mer = { w: WM, h: HM, fond: "monde", deco, pts };
}

/* ---------------- 2. Les bases de lancement ---------------- */
{
  let deco = M.txt([-100, 40], "ÉTATS-UNIS", { a: "middle" }) + M.txt([95, 63], "RUSSIE", { a: "middle" }) + M.txt([103, 33], "CHINE", { a: "middle" }) + M.txt([-60, -10], "BRÉSIL", { a: "middle" });
  const pts = [
    pt("ru", [63.3, 45.9], "Baïkonour", "end", "Baïkonour (Kazakhstan)", "Cosmodrome soviétique d'où partent Spoutnik (4 octobre 1957) et Gagarine (12 avril 1961). Loué par la Russie au Kazakhstan depuis 1994 ; encore utilisé pour les vols habités Soyouz vers l'ISS."),
    pt("ru", [40.6, 62.9], "Plessetsk", "end", "Plessetsk (Russie)", "Cosmodrome militaire du Nord de la Russie."),
    pt("ru", [128.3, 51.9], "Vostotchny", "start", "Vostotchny (Russie)", "Cosmodrome inauguré en 2016 pour ne plus dépendre du Kazakhstan."),
    pt("us", [-80.6, 28.5], "Cap Canaveral", "end", "Cap Canaveral et Kennedy Space Center (Floride)", "Site des missions Apollo, de la navette, de Falcon 9 (SpaceX) et d'Artemis II (1er avril 2026). Proche de l'équateur, il profite de la rotation de la Terre."),
    pt("us", [-120.6, 34.7], "Vandenberg", "end", "Vandenberg (Californie)", "Base de la Space Force pour les orbites polaires (satellites d'observation)."),
    pt("us", [-97.2, 26.0], "Starbase", "end", "Starbase (Texas)", "Site privé de SpaceX, où est essayée la fusée géante Starship, retenue par la NASA pour poser des astronautes sur la Lune."),
    pt("eu", [-52.8, 5.2], "Kourou", "start", "Kourou, Centre spatial guyanais (France)", "Port spatial de l'Europe depuis 1968, à 5° de l'équateur : Ariane 5 (1996-2023), Ariane 6 (premier vol le 9 juillet 2024), Vega."),
    pt("cn", [100.3, 41.0], "Jiuquan", "end", "Jiuquan (Chine)", "Base des vols habités chinois : Yang Liwei y décolle le 15 octobre 2003 (Shenzhou 5)."),
    pt("cn", [111.6, 38.8], "Taiyuan", "start", "Taiyuan (Chine)", "Base de lancement de satellites en orbite polaire."),
    pt("cn", [102.0, 28.2], "Xichang", "end", "Xichang (Chine)", "Base des satellites géostationnaires et de Beidou, le GPS chinois."),
    pt("cn", [111.0, 19.6], "Wenchang", "start", "Wenchang, île de Hainan (Chine)", "Base la plus proche de l'équateur, pour les lanceurs lourds Longue Marche 5 : station Tiangong, sondes lunaires Chang'e 5 et 6, sonde martienne Tianwen-1."),
    pt("in", [80.2, 13.7], "Sriharikota", "start", "Sriharikota, centre Satish-Dhawan (Inde)", "Base de l'ISRO : Chandrayaan-3, premier atterrissage près du pôle Sud lunaire (23 août 2023)."),
    pt("jp", [131.0, 30.4], "Tanegashima", "start", "Tanegashima (Japon)", "Principale base de l'agence spatiale japonaise JAXA (lanceurs H-IIA puis H3)."),
    pt("autres", [127.5, 34.4], "Naro", "end", "Naro (Corée du Sud)", "Base sud-coréenne : premier satellite mis en orbite par un lanceur entièrement national (Nuri) le 21 juin 2022."),
    pt("autres", [124.7, 39.7], "Sohae", "end", "Sohae (Corée du Nord)", "Base nord-coréenne : premier satellite placé en orbite en décembre 2012 ; les mêmes technologies servent aux missiles balistiques."),
    pt("autres", [53.9, 35.2], "Semnan", "start", "Semnan (Iran)", "Base iranienne : premier satellite iranien (Omid) en orbite en février 2009."),
    pt("autres", [34.7, 31.9], "Palmachim", "end", "Palmachim (Israël)", "Base israélienne : lancements vers l'ouest, au-dessus de la Méditerranée, pour ne pas survoler les pays voisins."),
    pt("autres", [177.9, -39.3], "Mahia", "end", "Mahia (Nouvelle-Zélande)", "Base privée de l'entreprise américaine Rocket Lab (petits lanceurs Electron).")
  ];
  OUT.cartes.espace = { w: WM, h: HM, fond: "monde", deco, pts };
}

/* ---------------- 3. Terrorisme transnational ---------------- */
{
  const calif = [[38.0, 36.4], [40.2, 36.7], [42.6, 36.6], [43.6, 36.3], [44.0, 35.3], [43.7, 34.1], [44.1, 33.2], [43.3, 32.9], [42.0, 33.6], [40.8, 34.3], [39.2, 34.5], [37.6, 34.8], [37.4, 35.6], [38.0, 36.4]];
  let deco = M.poly(calif, 'class="k-zone-ei"') + M.txt([64.5, 33.2], "AFGH.", { a: "middle" }) + M.txt([47.5, 17.2], "YÉMEN", { a: "middle" });
  const pts = [
    pt("aq", [-74.0, 40.7], "New York", "start", "11 septembre 2001 : New York et Washington", "19 terroristes d'Al-Qaïda détournent quatre avions : 2 977 morts (World Trade Center, Pentagone, Pennsylvanie). Les États-Unis répondent par la « guerre contre le terrorisme » et attaquent l'Afghanistan le 7 octobre 2001."),
    pt("aq", [36.8, -1.3], "Nairobi", "start", "7 août 1998 : Nairobi et Dar es Salaam", "Attentats contre les ambassades américaines au Kenya et en Tanzanie : 224 morts. Al-Qaïda se révèle comme organisation terroriste transnationale."),
    pt("aq", [45.0, 12.8], "Aden", "start", "12 octobre 2000 : Aden (Yémen)", "Attaque d'Al-Qaïda contre le destroyer américain USS Cole (17 marins tués)."),
    pt("aq", [115.2, -8.7], "Bali", "start", "12 octobre 2002 : Bali (Indonésie)", "Attentats de la Jemaah Islamiyah, liée à Al-Qaïda, contre des boîtes de nuit : 202 morts."),
    pt("aq", [-3.7, 40.4], "Madrid", "end", "11 mars 2004 : Madrid", "Bombes dans des trains de banlieue : 191 morts. Cellule inspirée par Al-Qaïda."),
    pt("aq", [-0.1, 51.5], "Londres", "end", "7 juillet 2005 : Londres", "Quatre kamikazes dans le métro et un bus : 52 morts."),
    pt("aq", [73.2, 34.2], "Abbottabad", "start", "2 mai 2011 : Abbottabad (Pakistan)", "Oussama ben Laden, fondateur d'Al-Qaïda, est tué par un commando américain."),
    pt("ei", [43.1, 36.3], "Mossoul", "start", "Mossoul (Irak)", "Prise par Daech le 10 juin 2014. Le « califat » est proclamé le 29 juin ; le 4 juillet, Abou Bakr al-Baghdadi apparaît en « calife » dans la grande mosquée al-Nouri. Reprise par l'armée irakienne et la coalition en juillet 2017."),
    pt("ei", [39.0, 35.95], "Raqqa", "end", "Raqqa (Syrie)", "« Capitale » syrienne de Daech, reprise par les Forces démocratiques syriennes, soutenues par la coalition, en octobre 2017."),
    pt("ei", [40.9, 34.5], "Baghouz", "end", "Baghouz (Syrie)", "Dernier réduit territorial de Daech, tombé le 23 mars 2019 : fin du « califat » territorial, pas de l'organisation."),
    pt("ei", [2.35, 48.86], "Paris", "start", "13 novembre 2015 : Paris et Saint-Denis", "Attentats coordonnés de Daech (Stade de France, terrasses, Bataclan) : 130 morts. Commando préparé en Syrie et en Belgique."),
    pt("ei", [4.35, 50.85], "Bruxelles", "start", "22 mars 2016 : Bruxelles", "Attentats de l'aéroport et du métro, par la même cellule que celle du 13 novembre : 32 morts."),
    pt("ei", [7.26, 43.7], "Nice", "start", "14 juillet 2016 : Nice", "Un camion fonce dans la foule sur la promenade des Anglais : 86 morts. Attentat revendiqué par Daech."),
    pt("ei", [37.4, 55.8], "Moscou", "start", "22 mars 2024 : Crocus City Hall, Moscou", "Attaque d'une salle de concert revendiquée par l'État islamique au Khorassan (branche afghane de Daech) : plus de 140 morts. Daech a perdu son territoire, pas sa capacité de frapper.")
  ];
  OUT.cartes.terro = { w: WM, h: HM, fond: "monde", deco, pts };
}

/* ---------------- 4. Les opérations de l'ONU sous Kofi Annan ---------------- */
{
  let deco = "";
  const pts = [
    pt("omp", [125.6, -8.6], "Timor oriental", "start", "Timor oriental : ATNUTO (1999-2002)", "Après le référendum d'autodétermination du 30 août 1999 et les violences des milices pro-indonésiennes, le Conseil autorise une force multinationale (INTERFET, menée par l'Australie), puis crée une administration transitoire de l'ONU (résolution 1272, 25 octobre 1999). Indépendance le 20 mai 2002."),
    pt("omp", [21.0, 42.6], "Kosovo", "start", "Kosovo : MINUK (1999)", "Après 78 jours de frappes de l'OTAN menées sans autorisation du Conseil de sécurité, la résolution 1244 (10 juin 1999) place le Kosovo sous administration provisoire de l'ONU, protégé par la KFOR de l'OTAN."),
    pt("omp", [-11.8, 8.5], "Sierra Leone", "end", "Sierra Leone : MINUSIL (1999-2005)", "Créée par la résolution 1270 (22 octobre 1999). En mai 2000, des centaines de casques bleus sont pris en otage par les rebelles du RUF ; l'intervention britannique (opération Palliser) sauve la mission, qui réussit ensuite le désarmement."),
    pt("omp", [23.6, -2.9], "RDC", "start", "République démocratique du Congo : MONUC (1999)", "Créée par la résolution 1279 (30 novembre 1999) pour surveiller le cessez-le-feu de Lusaka ; elle devient l'une des plus grandes opérations de l'ONU."),
    pt("omp", [38.9, 15.2], "Éthiopie-Érythrée", "start", "Éthiopie-Érythrée : MINUEE (2000-2008)", "Mission d'interposition le long de la frontière après la guerre de 1998-2000 (accord d'Alger, décembre 2000)."),
    pt("omp", [-9.4, 6.4], "Liberia", "end", "Liberia : MINUL (2003-2018)", "Déployée après le départ de Charles Taylor (2003) ; elle accompagne la reconstruction et l'élection d'Ellen Johnson Sirleaf (2005)."),
    pt("omp", [-5.5, 7.5], "Côte d'Ivoire", "start", "Côte d'Ivoire : ONUCI (2004-2017)", "Mission déployée avec l'appui de la force française Licorne après la guerre civile de 2002."),
    pt("omp", [-72.3, 18.9], "Haïti", "start", "Haïti : MINUSTAH (2004-2017)", "Mission de stabilisation dirigée par le Brésil après le départ du président Aristide."),
    pt("omp", [29.9, -3.4], "Burundi", "start", "Burundi : ONUB (2004-2006)", "Accompagne la fin de la guerre civile et les élections de 2005."),
    pt("omp", [31.6, 9.5], "Soudan", "end", "Soudan : MINUS (2005-2011)", "Surveille l'accord de paix de 2005 entre Khartoum et les rebelles du Sud. Pour le Darfour, la mission conjointe avec l'Union africaine (MINUAD) n'est créée qu'en 2007, après le départ de Kofi Annan."),
    pt("omp", [35.5, 33.3], "Liban", "end", "Liban : FINUL renforcée (2006)", "Après la guerre entre Israël et le Hezbollah (juillet-août 2006), la résolution 1701 (11 août 2006) porte la FINUL jusqu'à 15 000 soldats autorisés. Son mandat a été prolongé une dernière fois jusqu'au 31 décembre 2026."),
    pt("crise", [44.4, 33.3], "Irak 2003", "start", "Irak : la guerre sans l'ONU (2003)", "Les États-Unis et le Royaume-Uni attaquent l'Irak le 20 mars 2003 sans nouvelle résolution du Conseil de sécurité. Kofi Annan juge cette guerre « illégale » au regard de la Charte (septembre 2004)."),
    pt("crise", [30.1, -1.9], "Rwanda", "end", "Rwanda (1994) : l'échec qui hante l'ONU", "Pendant le génocide des Tutsis (avril-juillet 1994), la MINUAR est réduite au lieu d'être renforcée. Kofi Annan dirigeait alors le département des opérations de maintien de la paix ; le rapport Carlsson (décembre 1999) reconnaît l'échec de l'ONU."),
    pt("crise", [19.3, 44.1], "Srebrenica", "end", "Srebrenica (1995)", "Environ 8 000 hommes et garçons bosniaques sont massacrés dans une « zone de sécurité » de l'ONU. Le rapport de Kofi Annan (novembre 1999) admet les erreurs de l'organisation.")
  ];
  OUT.cartes.onu = { w: WM, h: HM, fond: "monde", deco, pts };
}

/* ---------------- 5. La Chine et les espaces maritimes (Indo-Pacifique) ---------------- */
{
  const W = 900, H = 640;
  const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [[41, -10], [146, 44]] });
  const C = cadre(proj, W, H, 0.45, 2);
  const fond = '<rect width="' + W + '" height="' + H + '" class="k-mer-f"/><path d="' + simplifier(C.gp(d3.geoGraticule().step([10, 10])()), 0.5, 0) + '" class="k-grat"/>' +
    '<path d="' + C.pays(f => f.properties.ADMIN !== "China") + '" class="k-terre"/><path d="' + C.pays(f => f.properties.ADMIN === "China") + '" class="k-terre-cn"/>';
  const NEUF = [[108.3, 18.0], [109.2, 15.5], [109.6, 12.5], [109.8, 10.0], [109.0, 7.5], [110.6, 5.5], [112.3, 3.9], [113.9, 5.7], [115.2, 7.0], [116.3, 8.4], [117.1, 10.2], [118.4, 12.4], [119.1, 15.0], [119.7, 17.8], [120.8, 20.0], [121.8, 21.8]];
  const CHAINE = [[131, 33], [128.5, 29], [125, 25], [122.2, 22.5], [121, 19], [119.5, 13], [117.5, 8], [116, 5.5]];
  const ROUTE = [[121.5, 31.2], [123, 28], [120.5, 23.5], [118, 21.5], [113, 15], [106, 6], [103.6, 1.3], [98.5, 5], [92, 8], [81.1, 5.8], [72, 10], [62.3, 24.5], [58, 18], [51, 13], [43.4, 12.3], [38, 20], [33, 29]];
  let deco = C.ligne(ROUTE, 'class="k-route"') + C.ligne(NEUF, 'class="k-neuf"') + C.ligne(CHAINE, 'class="k-chaine"') +
    C.txt([104, 35], "CHINE", { a: "middle", cl: "k-pays k-gros" }) + C.txt([79, 22], "INDE", { a: "middle" }) + C.txt([138, 36.5], "JAPON", { a: "middle" }) + C.txt([121, 23.7], "TAÏWAN", { a: "start", dx: 10 }) +
    C.txt([123.5, 12.3], "PHILIPPINES", { a: "start" }) + C.txt([116, 0], "INDONÉSIE", { a: "middle" }) + C.txt([106.5, 15.5], "VIÊT NAM", { a: "end", dx: -4 }) + C.txt([69, 29], "PAKISTAN", { a: "middle" }) +
    C.txt([113.8, 13.9], "mer de Chine", { a: "middle", cl: "k-mer k-petit" }) + C.txt([113.8, 12.7], "méridionale", { a: "middle", cl: "k-mer k-petit" }) + C.txt([75, -3], "OCÉAN INDIEN", { a: "middle", cl: "k-mer" }) + C.txt([138, 20], "OCÉAN PACIFIQUE", { a: "middle", cl: "k-mer" }) +
    C.txt([128.6, 27.5], "« première chaîne d'îles »", { a: "start", cl: "k-note", dx: 6 });
  const P = (c, ll, n, a, t, d) => { const [x, y] = C.P(ll); return { c, x, y, n, a, t, d }; };
  const pts = [
    P("ilots", [112.9, 9.55], "Fiery Cross", "end", "Récif de Fiery Cross (Spratleys)", "Récif transformé en île artificielle par la Chine (2014-2015), avec une piste de 3 000 m, des hangars et un port. Les Spratleys sont aussi revendiquées par le Viêt Nam, les Philippines, la Malaisie, Brunei et Taïwan."),
    P("ilots", [115.5, 9.9], "Mischief", "start", "Récif de Mischief (Spratleys)", "Occupé par la Chine depuis 1995, militarisé après 2015, dans la ZEE des Philippines. Le tribunal arbitral de 2016 l'a jugé incapable de générer des droits maritimes propres."),
    P("ilots", [112.3, 16.8], "Paracels", "start", "Îles Paracels", "Prises par la Chine au Sud-Viêt Nam en janvier 1974 ; l'île Woody (Yongxing) abrite le siège administratif chinois de la « ville de Sansha » (2012)."),
    P("ilots", [117.8, 15.15], "Scarborough", "start", "Récif de Scarborough", "Contrôlé de fait par la Chine depuis l'affrontement de 2012 avec les Philippines, à environ 220 km des côtes philippines."),
    P("bases", [109.6, 18.2], "Sanya-Yulin", "end", "Sanya et Yulin (Hainan)", "Grande base navale du Sud : SNLE, et porte-avions Shandong et Fujian (mis en service à Sanya le 5 novembre 2025)."),
    P("bases", [120.4, 36.1], "Qingdao", "start", "Qingdao", "Quartier général de la flotte du Nord ; port d'attache du porte-avions Liaoning (premier porte-avions chinois, 2012)."),
    P("bases", [43.15, 11.6], "Djibouti", "start", "Djibouti", "Première base militaire chinoise à l'étranger, ouverte le 1er août 2017, officiellement pour soutenir la lutte contre la piraterie et évacuer des ressortissants."),
    P("ports", [62.3, 25.1], "Gwadar", "end", "Gwadar (Pakistan)", "Port exploité par une société chinoise depuis 2013, débouché du corridor économique Chine-Pakistan : il permettrait de contourner le détroit de Malacca."),
    P("ports", [81.1, 6.1], "Hambantota", "start", "Hambantota (Sri Lanka)", "Faute de pouvoir rembourser ses emprunts, le Sri Lanka concède le port pour 99 ans à China Merchants Port en décembre 2017 : un exemple cité du « piège de la dette », expression discutée par les chercheurs."),
    P("ports", [93.5, 19.4], "Kyaukpyu", "start", "Kyaukpyu (Birmanie)", "Port en eau profonde et terminal d'oléoduc et de gazoduc vers le Yunnan (gazoduc en service en 2013, oléoduc en 2017) : un autre moyen d'éviter Malacca."),
    P("ports", [121.5, 31.2], "Shanghai", "start", "Shanghai", "Premier port à conteneurs du monde depuis 2010. Les grands ports chinois occupent l'essentiel du haut du classement mondial."),
    P("espace", [111.0, 19.6], "Wenchang", "start", "Wenchang (Hainan)", "Base de lancement côtière de la Chine : les lanceurs lourds peuvent y être acheminés par la mer. Départ de la station Tiangong et des sondes Chang'e 5 et 6."),
    P("espace", [100.3, 41.0], "Jiuquan", "end", "Jiuquan", "Base des vols habités Shenzhou vers la station Tiangong.")
  ];
  OUT.cartes.chine = { w: W, h: H, fond, deco, pts };
}

/* ---------------- 6. Le Moyen-Orient ---------------- */
{
  const W = 900, H = 640;
  const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [[26, 12], [63, 41]] });
  const C = cadre(proj, W, H, 0.35, 0.8);
  const fond = '<rect width="' + W + '" height="' + H + '" class="k-mer-f"/><path d="' + simplifier(C.gp(d3.geoGraticule().step([5, 5])()), 0.5, 0) + '" class="k-grat"/>' +
    '<path d="' + C.pays(f => !["Israel", "Palestine"].includes(f.properties.ADMIN)) + '" class="k-terre"/>' +
    '<path d="' + C.pays(f => f.properties.ADMIN === "Israel") + '" class="k-terre-il"/><path d="' + C.pays(f => f.properties.ADMIN === "Palestine") + '" class="k-terre-ps"/>';
  const NFZN = [[36.3, 36], [44.5, 36]], NFZS = [[38.8, 32], [47.5, 32]], NFZS2 = [[38.8, 33], [47.5, 33]];
  let deco = C.ligne([[38.9, 36], [44.4, 36]], 'class="k-nfz"') + C.ligne([[39.0, 32], [47.6, 32]], 'class="k-nfz"') + C.ligne([[38.9, 33], [47.0, 33]], 'class="k-nfz k-nfz2"') +
    C.txt([42, 36.2], "36e parallèle", { a: "middle", cl: "k-note", dy: -4 }) + C.txt([44, 31.7], "32e puis 33e parallèle", { a: "middle", cl: "k-note", dy: 12 }) +
    C.txt([43.5, 33.8], "IRAK", { a: "middle", cl: "k-pays", dy: -6 }) + C.txt([53.5, 32.5], "IRAN", { a: "middle" }) + C.txt([45, 24], "ARABIE SAOUDITE", { a: "middle" }) + C.txt([38.5, 35.0], "SYRIE", { a: "middle" }) +
    C.txt([30.5, 26.5], "ÉGYPTE", { a: "middle" }) + C.txt([36.8, 31.0], "JORDANIE", { a: "start", dx: 2, dy: 10 }) + C.txt([35.5, 39], "TURQUIE", { a: "middle" }) +
    C.txt([48, 15.6], "YÉMEN", { a: "middle" }) + C.txt([57, 21], "OMAN", { a: "middle" }) + C.txt([51, 27.4], "golfe Persique", { a: "middle", cl: "k-mer" }) + C.txt([33, 33.6], "Méditerranée", { a: "end", cl: "k-mer" }) + C.txt([38.5, 21], "mer Rouge", { a: "middle", cl: "k-mer" });
  const P = (c, ll, n, a, t, d) => { const [x, y] = C.P(ll); return { c, x, y, n, a, t, d }; };
  const pts = [
    P("ip", [35.22, 31.78], "Jérusalem", "end", "Jérusalem", "Ville sainte des trois monothéismes. Le plan de partage de 1947 prévoyait un statut international ; Israël occupe Jérusalem-Est depuis 1967 et proclame Jérusalem « entière et réunifiée » capitale (loi fondamentale de 1980), ce que l'ONU ne reconnaît pas. Les États-Unis y transfèrent leur ambassade le 14 mai 2018."),
    P("ip", [34.45, 31.45], "Gaza", "end", "Bande de Gaza", "Occupée par l'Égypte (1948-1967) puis par Israël ; colonies évacuées en 2005 ; contrôlée par le Hamas depuis juin 2007 et soumise à un blocus. Attaque du Hamas en Israël le 7 octobre 2023, puis guerre dévastatrice ; cessez-le-feu le 10 octobre 2025."),
    P("ip", [35.75, 33.0], "Golan", "start", "Plateau du Golan", "Syrien, conquis par Israël en 1967, annexé en 1981 ; cette annexion n'est pas reconnue par l'ONU (résolution 497), mais l'a été par les États-Unis en 2019."),
    P("ip", [33.4, 28.5], "Sinaï", "end", "Sinaï", "Conquis par Israël en 1967 et rendu à l'Égypte en 1982, en application du traité de paix israélo-égyptien du 26 mars 1979 (après les accords de Camp David de septembre 1978)."),
    P("golfe", [47.98, 29.37], "Koweït", "start", "Koweït : invasion du 2 août 1990", "L'Irak de Saddam Hussein envahit et annexe le Koweït. Le Conseil de sécurité exige le retrait (résolution 660) puis autorise « tous les moyens nécessaires » (résolution 678). La coalition de 35 pays le libère : offensive aérienne le 17 janvier 1991, cessez-le-feu le 28 février."),
    P("golfe", [44.4, 33.3], "Bagdad", "start", "Bagdad : 9 avril 2003", "La coalition américano-britannique, entrée en Irak le 20 mars 2003 sans mandat de l'ONU, prend Bagdad. Le régime tombe vite, mais l'occupation déclenche une insurrection, puis une guerre civile entre sunnites et chiites (2006-2007)."),
    P("golfe", [43.1, 36.3], "Mossoul", "start", "Mossoul : 2014-2017", "Prise par Daech en juin 2014, issu de la branche irakienne d'Al-Qaïda née de l'insurrection contre l'occupation américaine. Reprise en juillet 2017."),
    P("golfe", [56.3, 26.6], "Ormuz", "start", "Détroit d'Ormuz", "Passage du pétrole du Golfe. Fermé par l'Iran après le début, le 28 février 2026, de la guerre lancée par les États-Unis et Israël contre l'Iran : un prolongement de la conflictualité régionale (voir le cours)."),
    P("golfe", [51.4, 35.7], "Téhéran", "end", "Téhéran", "Capitale de la République islamique d'Iran, adversaire d'Israël et des États-Unis. Frappes israéliennes et américaines en juin 2025 (« guerre des douze jours », du 13 au 24 juin), puis guerre à partir du 28 février 2026, au cours de laquelle le Guide suprême Ali Khamenei est tué.")
  ];
  OUT.cartes.mo = { w: W, h: H, fond, deco, pts };
}

/* ajustements d'étiquettes (ancre, décalage vertical) pour éviter les chevauchements */
const RETOUCHES = {
  mer: { Toulon: ["start", -6], Naples: ["start", 7], "Bahreïn": ["end", -7], "Abu Dhabi": ["end", 10], Djibouti: ["end", 9] },
  espace: { "Cap Canaveral": ["start", 2], Starbase: ["end", 4], Naro: ["start", 4], Taiyuan: ["start", 0, ""], Sohae: ["start", -6] },
  terro: { Londres: ["end", -4], Bruxelles: ["start", -5], Paris: ["start", 6], Nice: ["start", 7], Raqqa: ["end", -6], Baghouz: ["end", 8], Mossoul: ["start", -3] },
  onu: { "Sierra Leone": ["end", -5], Liberia: ["end", 7], Rwanda: ["end", -5], Burundi: ["start", 6], RDC: ["end", 4], "Timor oriental": ["end", 0], Srebrenica: ["end", -2], Kosovo: ["start", 2] },
  chine: { Paracels: ["start", 4], Wenchang: ["start", -5] },
  mo: { "Jérusalem": ["end", -5], Gaza: ["end", 9] }
};
for (const [c, t] of Object.entries(RETOUCHES)) for (const p of OUT.cartes[c].pts) if (t[p.n]) { p.a = t[p.n][0]; p.dy = t[p.n][1]; if (t[p.n].length > 2) p.n = t[p.n][2]; }
/* recadrage des cartes mondiales sur leurs points (même fond, autre fenêtre) */
for (const c of ["terro", "onu"]) {
  const P = OUT.cartes[c].pts, mx = 70, my = 50;
  let x0 = Math.min(...P.map(p => p.x)) - mx, x1 = Math.max(...P.map(p => p.x)) + mx, y0 = Math.min(...P.map(p => p.y)) - my, y1 = Math.max(...P.map(p => p.y)) + my;
  x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(WM, x1); y1 = Math.min(HM, y1);
  OUT.cartes[c].vb = [x0, y0, x1 - x0, y1 - y0].map(Math.round);
}
/* légendes des cartes (couleur et libellé de chaque couche de points, symboles fixes) */
const META = {
  mer: { t: "Les océans, espaces de puissance : dissuasion et projection", c: { snle: ["Bases de sous-marins nucléaires lanceurs d'engins (SNLE)", "#B3241B"], us: ["Grandes bases et flottes américaines", "#2D5675"], fr: ["Points d'appui français", "#B07A1E"] }, leg: [["choke", "Détroits stratégiques (Ormuz, Bab el-Mandeb, Suez, Malacca, Panama, Gibraltar)"]] },
  espace: { t: "Les puissances spatiales et leurs bases de lancement", c: { us: ["États-Unis", "#2D5675"], ru: ["Russie", "var(--encre2)"], eu: ["Europe (Kourou)", "#2F7F8C"], cn: ["Chine", "#B3241B"], in: ["Inde", "#B07A1E"], jp: ["Japon", "#7A4A8C"], autres: ["Autres États et entreprises", "#2F6B3B"] } },
  terro: { t: "Le terrorisme transnational, d'Al-Qaïda à Daech", c: { aq: ["Al-Qaïda et groupes liés : attentats, lieux clés", "#2D5675"], ei: ["Daech : territoire, attentats", "#B3241B"] }, leg: [["zone", "Territoire du « califat » à son apogée (2014-2015), tracé approximatif"]] },
  onu: { t: "L'ONU sous Kofi Annan (1997-2006) : opérations et échecs", c: { omp: ["Opérations de paix créées ou renforcées sous Annan", "#2D5675"], crise: ["Échecs hérités et contournements de l'ONU", "#B3241B"] } },
  chine: { t: "La Chine à la conquête des mers (et de l'espace)", c: { ilots: ["Îlots et récifs disputés, occupés par la Chine", "#B3241B"], bases: ["Bases navales chinoises", "var(--encre)"], ports: ["Ports des routes de la soie maritimes", "#B07A1E"], espace: ["Bases de lancement", "#2D5675"] }, leg: [["neuf", "« Ligne en neuf traits » (revendications chinoises, tracé approximatif)"], ["chaine", "« Première chaîne d'îles » (représentation stratégique chinoise)"], ["route", "Route maritime vers l'Europe"]] },
  mo: { t: "Le Moyen-Orient : conflits et tentatives de paix", c: { ip: ["Conflit israélo-arabe et israélo-palestinien", "#B3241B"], golfe: ["Guerres du Golfe et prolongements", "#2D5675"] }, leg: [["il", "Israël (frontières de Natural Earth)"], ["ps", "Territoires palestiniens (Cisjordanie, Gaza)"], ["nfz", "Zones d'exclusion aérienne en Irak (1991-2003)"]] }
};
for (const k in META) OUT.cartes[k].meta = META[k];

/* modules complémentaires : chaque fichier cartes-*.js du dossier exporte une fonction (ctx) qui ajoute
   ses cartes (ctx.OUT.cartes.nom = { w, h, fond, deco, pts, meta }) et ses calques d'animation
   (ctx.OUT.anims.nom = { w, h, fond, calques: { id: svg } }) ; voir RENFORTS.md */
OUT.anims = OUT.anims || {};
const CTX = { d3, cadre, simplifier, esc, M, WM, HM, OUT, FEAT };
for (const f of fs.readdirSync(__dirname).filter(f => /^cartes-.+\.js$/.test(f)).sort()) require(path.join(__dirname, f))(CTX);
fs.writeFileSync(process.argv[3], JSON.stringify(OUT));
const taille = s => Math.round(JSON.stringify(s).length / 1024) + " Ko";
console.log("monde", taille(OUT.monde), Object.keys(OUT.cartes).map(k => k + " " + taille(OUT.cartes[k])).join(", "));
