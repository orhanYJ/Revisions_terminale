/* Animations explicatives supplémentaires : S3 (mobilité structurelle), S4 (critères du BIT),
   S5 (répertoires d'action collective), R1 (conceptions de la justice sociale).
   Chiffres S3 et S4 recalculés par outils/specialites/ses/verif/renfort_s3s4s5r1.py. */

/* Point situé à la fraction q (0…1) de la longueur d'une ligne brisée */
function ANIM_LE_LONG(pts, q) {
  var L = 0, seg = [];
  for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(d); L += d; }
  var r = L * Math.max(0, Math.min(1, q));
  for (var j = 1; j < pts.length; j++) {
    if (seg[j - 1] >= r) { var f = seg[j - 1] ? r / seg[j - 1] : 0; return [pts[j - 1][0] + (pts[j][0] - pts[j - 1][0]) * f, pts[j - 1][1] + (pts[j][1] - pts[j - 1][1]) * f]; }
    r -= seg[j - 1];
  }
  return pts[pts.length - 1];
}

ANIMS["s3-structure"] = {
  t: "La mobilité structurelle mesurée : les hommes en 2015",
  h: 340,
  src: "Source : Insee, enquête Formation et qualification professionnelle 2014-2015 (Insee Première n° 1739, février 2019). Hommes de 35 à 59 ans, comparés à leur père. Mobilité structurelle = moitié de la somme des écarts entre les deux structures (calcul vérifié).",
  etapes: [
    { l: "Les pères d’abord : en 2015, on compare la catégorie sociale des hommes de 35 à 59 ans à celle de leur père. Parmi les pères, 8,3 % d’agriculteurs et 13,9 % de cadres.", d: 4 },
    { l: "Puis les fils : 2,8 % d’agriculteurs seulement, mais 20,4 % de cadres et 25,3 % de professions intermédiaires. En une génération, la structure des emplois s’est déplacée vers le haut.", d: 4.5 },
    { l: "Des places ont disparu (agriculteurs −5,5 points, artisans et commerçants −3,9, employés et ouvriers −6,2) ; d’autres sont apparues (cadres +6,5, professions intermédiaires +9,4).", d: 4.5 },
    { l: "Même si chacun voulait rester dans le groupe de son père, ce serait impossible : au moins 15,8 fils sur 100 doivent changer de groupe. C’est la mobilité structurelle, la moitié de la somme des écarts (31,5 ÷ 2).", d: 5 },
    { l: "Or 65,2 % des hommes ont changé de groupe (mobilité observée). La structure n’en explique qu’environ un quart (15,8 ÷ 65,2 ≈ 24 %) : le reste est la mobilité nette, ou de circulation.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var noms = ["Agriculteurs", "Artisans, commerçants", "Cadres", "Professions intermédiaires", "Employés et ouvriers qualifiés", "Employés et ouvriers non qualifiés"];
    var P = [8.3, 13.0, 13.9, 15.9, 35.6, 13.1], F = [2.8, 9.1, 20.4, 25.3, 32.4, 10.1];
    var x0 = 112, sc = 4.9, y0 = 34, rh = 37, s = "";
    s += A.r(x0 - 2, 8, 12, 9, { f: "gris", r: 2, op: 0.55 }) + A.t(x0 + 15, 16, "pères (origine)", { t: 11, c: "gris" });
    s += A.r(x0 + 112, 8, 12, 9, { f: "canard", r: 2, op: i >= 1 ? 1 : 0.3 }) + A.t(x0 + 129, 16, "fils (position)", { t: 11, c: "canard", g: true, op: i >= 1 ? 1 : 0.4 });
    var somme = 0;
    noms.forEach(function (n, k) {
      var y = y0 + k * rh, qP = i === 0 ? A.s(p, k * 0.08, 0.45 + k * 0.08) : 1, qF = i === 0 ? 0 : i === 1 ? A.s(p, k * 0.08, 0.45 + k * 0.08) : 1;
      s += A.t(x0 - 8, y + 13, n, { t: 10.5, a: "end", w: 100, v: true, c: "encre" });
      s += A.r(x0, y, P[k] * sc * qP, 11, { f: "gris", r: 2, op: 0.55 });
      s += A.t(x0 + P[k] * sc * qP + 4, y + 10, A.fr(P[k] * qP, 1), { t: 10, c: "gris", op: qP });
      if (qF > 0) {
        s += A.r(x0, y + 13, F[k] * sc * qF, 11, { f: "canard", r: 2 });
        s += A.t(x0 + F[k] * sc * qF + 4, y + 23, A.fr(F[k] * qF, 1), { t: 10.5, g: true, c: "canard", op: qF });
      }
      var d = F[k] - P[k];
      if (i >= 2) {
        var qd = i === 2 ? A.s(p, 0.1 + k * 0.1, 0.4 + k * 0.1) : 1;
        s += A.t(356, y + 18, (d > 0 ? "+" : "−") + A.fr(Math.abs(d), 1), { t: 12, g: true, a: "end", c: d > 0 ? "vert" : "corail", op: qd });
        if (i === 3) somme += Math.abs(d) * A.s(p, k * 0.1, 0.1 + k * 0.1);
      }
    });
    var yb = y0 + 6 * rh + 8;
    if (i === 2) s += A.t(180, yb + 22, "places créées : +15,9 points · places disparues : −15,6 points", { t: 11.5, g: true, a: "middle", op: A.s(p, 0.7, 1), w: 320 });
    if (i === 3) {
      s += A.t(180, yb + 14, "somme des écarts : " + A.fr(somme, 1) + " points", { t: 12, a: "middle", c: "gris" });
      s += A.t(180, yb + 40, "mobilité structurelle = " + A.fr(somme, 1) + " ÷ 2 = " + A.fr(somme / 2, 1) + " %", { t: 14.5, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.65, 1) });
    }
    if (i === 4) {
      var q = A.s(p, 0, 0.6), q2 = A.s(p, 0.45, 1);
      s += A.t(20, yb + 10, "Mobilité observée des hommes : " + A.fr(65.2 * q, 1) + " %", { t: 11.5, g: true });
      s += A.r(20, yb + 18, 320, 16, { f: "carte2", r: 5 }) + A.r(20, yb + 18, 320 * 0.652 * q, 16, { f: "canard", r: 5, op: 0.35 });
      s += A.r(20, yb + 18, 320 * 0.158 * q2, 16, { f: "corail", r: 5 });
      s += A.t(24, yb + 50, "dont structurelle : 15,8 points, soit 24 %", { t: 11.5, g: true, c: "corail", op: q2 });
      s += A.t(24, yb + 66, "le reste, mobilité nette : 49,4 points", { t: 11.5, g: true, c: "canard", op: q2 });
    }
    return s;
  }
};

ANIMS["s4-bit"] = {
  t: "Chômeur, halo ou inactif ? Les trois critères du BIT",
  h: 340,
  src: "Cas fictifs construits pour le site. Définitions : Insee (chômage au sens du BIT, halo autour du chômage). Chiffres : Insee, enquête Emploi 2025 (Insee Première n° 2096), part de la population des 15-64 ans.",
  etapes: [
    { l: "Le Bureau international du travail classe chacun avec trois critères, dans l’ordre. D’abord : avoir travaillé, ne serait-ce qu’une heure, pendant la semaine de référence.", d: 3.5 },
    { l: "Un étudiant a fait 3 heures de livraison cette semaine-là : il est en emploi. Une heure suffit. S’il souhaite travailler davantage et qu’il est disponible, il est en sous-emploi.", d: 4.5 },
    { l: "Une ancienne vendeuse n’a pas travaillé, peut commencer tout de suite et envoie des candidatures : les trois critères sont remplis, elle est chômeuse au sens du BIT.", d: 5 },
    { l: "Une mère cherche un emploi mais ne peut pas commencer avant un mois, faute de garde d’enfant : pas disponible, donc pas chômeuse. Elle souhaite travailler : elle est dans le halo autour du chômage.", d: 5 },
    { l: "Un ouvrier de 58 ans, disponible, a cessé de chercher, découragé : sans recherche active, il n’est pas chômeur au sens du BIT. Il souhaite travailler : il est lui aussi dans le halo.", d: 5 },
    { l: "Un retraité qui ne souhaite pas travailler est inactif. En 2025, 5,8 % des 15-64 ans sont au chômage et 4,5 % dans le halo : 10,3 % sont sans emploi et souhaitent travailler.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var s = "", bx = 36, bw = 190, bh = 34;
    var Q = [{ y: 30, t: "A travaillé au moins 1 heure dans la semaine ?" }, { y: 92, t: "Disponible dans les 2 semaines ?" }, { y: 154, t: "A cherché activement dans le mois ?" }, { y: 230, t: "Souhaite travailler ?" }];
    var R = { emploi: { y: 30, t: "En emploi", k: "canard" }, chomeur: { y: 154, t: "Chômeur (BIT)", k: "corail" }, halo: { y: 230, t: "Halo du chômage", k: "moutarde" }, inactif: { y: 292, t: "Inactif", k: "gris" } };
    var rx = 250, rw = 104;
    var qa = i === 0 ? p : 1;
    /* rails : « non » descend à gauche vers la question 4, « oui » descend au centre */
    var rail = '<line x1="12" x2="12" y1="' + (92 + bh / 2) + '" y2="' + (230 + bh / 2) + '" style="stroke:var(--ligne);stroke-width:2"/>';
    s += A.g(A.s(qa, 0.3, 0.7), rail +
      A.fl(bx, 92 + bh / 2, 12, 92 + bh / 2, { c: "ligne", sw: 2, tete: false }) + A.fl(bx, 154 + bh / 2, 12, 154 + bh / 2, { c: "ligne", sw: 2, tete: false }) +
      A.fl(12, 230 + bh / 2, bx - 2, 230 + bh / 2, { c: "ligne", sw: 2 }) +
      A.t(15, 92 + bh / 2 - 5, "non", { t: 10.5, c: "gris", it: true }) + A.t(15, 154 + bh / 2 - 5, "non", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw / 2, 30 + bh, bx + bw / 2, 92 - 2, { c: "ligne", sw: 2 }) + A.fl(bx + bw / 2, 92 + bh, bx + bw / 2, 154 - 2, { c: "ligne", sw: 2 }) +
      A.t(bx + bw / 2 + 6, 82, "non", { t: 10.5, c: "gris", it: true }) + A.t(bx + bw / 2 + 6, 144, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 30 + bh / 2, rx - 2, 30 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 30 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 154 + bh / 2, rx - 2, 154 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 154 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 230 + bh / 2, rx - 2, 230 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 230 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw / 2, 230 + bh, bx + bw / 2, 292 + bh / 2, { c: "ligne", sw: 2, tete: false }) + A.fl(bx + bw / 2, 292 + bh / 2, rx - 2, 292 + bh / 2, { c: "ligne", sw: 2 }) +
      A.t(bx + bw / 2 + 6, 280, "non", { t: 10.5, c: "gris", it: true }));
    /* trajets : de l'entrée jusqu'au bord de la case d'arrivée ; le tracé passe sous les cases */
    var cx = bx + bw / 2, M = function (y) { return y + bh / 2; }, fin = rx - 3;
    var T = {
      1: { pts: [[cx, 8], [cx, M(30)], [fin, M(30)]], c: "canard", lab: "3 h de livraison" },
      2: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [cx, M(154)], [fin, M(154)]], c: "corail", lab: "disponible, cherche" },
      3: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [12, M(92)], [12, M(230)], [cx, M(230)], [fin, M(230)]], c: "moutarde", lab: "pas disponible" },
      4: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [cx, M(154)], [12, M(154)], [12, M(230)], [cx, M(230)], [fin, M(230)]], c: "moutarde", lab: "ne cherche plus" },
      5: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [12, M(92)], [12, M(230)], [cx, M(230)], [cx, M(292)], [fin, M(292)]], c: "gris", lab: "ne veut pas travailler" }
    };
    var tr = T[i], qt = A.s(p, 0, 0.85);
    if (tr) s += A.pl(tr.pts, qt, { c: tr.c, sw: 3.2, op: 0.8 });
    Q.forEach(function (q, k) { s += A.boite(bx, q.y, bw, bh, q.t, { k: "meca", t: 11.5, op: i === 0 ? A.s(p, k * 0.15, 0.3 + k * 0.15) : 1 }); });
    var bilan = i === 5 && p > 0.75;
    Object.keys(R).forEach(function (k, j) {
      var r = R[k], q = i === 0 ? A.s(p, 0.5 + j * 0.1, 0.8 + j * 0.1) : 1;
      var txt = bilan && k === "chomeur" ? "Chômage : 5,8 %" : bilan && k === "halo" ? "Halo : 4,5 %" : r.t;
      s += A.boite(rx, r.y, rw, bh, txt, { k: k === "chomeur" ? "effet" : k === "halo" ? "frein" : k === "emploi" ? "cause" : "neutre", t: 11.5, g: true, op: q });
    });
    if (tr) {
      var pos = ANIM_LE_LONG(tr.pts, qt);
      s += A.cercle(pos[0], pos[1], 8, { f: tr.c, s: "carte", sw: 2.5 });
      s += A.t(rx + rw, pos[1] - 21, tr.lab, { t: 11, g: true, c: tr.c === "gris" ? "encre" : tr.c, h: true, a: "end", op: A.s(p, 0.8, 1) });
    }
    return s;
  }
};

ANIMS["s5-tilly"] = {
  t: "Comment le répertoire d’action collective change",
  h: 330,
  src: "D’après Charles Tilly, <i>La France conteste, de 1600 à nos jours</i>, 1986. Dates : abolition du délit de coalition (loi du 25 mai 1864), liberté syndicale (loi du 21 mars 1884) ; tribunal administratif de Paris, 3 février 2021 (L’Affaire du siècle).",
  etapes: [
    { l: "Charles Tilly appelle répertoire d’action collective l’ensemble limité des moyens d’action qu’un groupe connaît et juge légitimes à une époque. Il ne change que lentement.", d: 3.5 },
    { l: "Du XVIIe au milieu du XIXe siècle : un répertoire local et patronné. On agit dans sa communauté, souvent par l’intermédiaire d’un notable, directement contre l’adversaire : charivaris, émeutes de subsistance, révoltes contre l’impôt.", d: 5 },
    { l: "Au XIXe siècle, l’État national et l’industrie s’imposent : les décisions se prennent dans la capitale et les grandes entreprises. Les luttes changent d’échelle et s’adressent à l’État.", d: 4.5 },
    { l: "Vers le milieu du XIXe siècle naît un répertoire national et autonome : grève (le délit de coalition est aboli en 1864), syndicats (autorisés en 1884), manifestation, pétition, réunion publique. Des organisations permanentes agissent en leur nom propre.", d: 5.5 },
    { l: "Depuis la fin du XXe siècle, le répertoire s’enrichit : actions médiatiques, contre-expertise, pétitions en ligne, recours en justice (L’Affaire du siècle, jugée le 3 février 2021), désobéissance civile, marches pour le climat dans de nombreux pays (2019).", d: 5.5 },
    { l: "Les anciens moyens ne disparaissent pas : la grève et la manifestation restent au cœur des mobilisations de 2023 contre la réforme des retraites. Le répertoire s’élargit : les militants combinent les formes.", d: 4.5 }
  ],
  rendu: function (A, i, p) {
    var s = "", X = function (an) { return 22 + (an - 1600) * 316 / 430; }, ya = 300;
    var qa = i === 0 ? A.s(p, 0, 0.7) : 1;
    s += A.fl(X(1600), ya, X(1600) + (X(2030) - X(1600)) * qa, ya, { c: "encre", sw: 1.6 });
    [1600, 1700, 1800, 1900, 2000].forEach(function (an, k) {
      var q = i === 0 ? A.s(p, 0.1 + k * 0.12, 0.3 + k * 0.12) : 1;
      s += '<line x1="' + X(an) + '" x2="' + X(an) + '" y1="' + (ya - 4) + '" y2="' + (ya + 4) + '" style="stroke:var(--encre);stroke-width:1.5;opacity:' + q + '"/>' + A.t(X(an), ya + 18, String(an), { t: 11, a: "middle", c: "gris", op: q });
    });
    if (i === 0) s += A.boite(60, 70, 240, 74, "Répertoire : les moyens d’action connus et jugés légitimes à une époque", { k: "cause", t: 13, g: true, op: A.s(p, 0.5, 0.9) });
    /* bande 1 : local et patronné (1600-1850) */
    if (i >= 1) {
      var q1 = i === 1 ? A.s(p, 0, 0.4) : 1, op1 = i >= 3 ? 0.55 : 1;
      s += A.r(X(1600), 252, (X(1850) - X(1600)) * q1, 34, { f: "moutardec", s: "moutarde", r: 6, op: op1 });
      s += A.t(X(1600) + 8, 266, "local et patronné", { t: 12, g: true, c: "moutarde", op: q1 * op1 });
      s += A.t(X(1600) + 8, 280, "village, notable", { t: 10.5, c: "gris", op: q1 * op1 });
      if (i <= 2) ["charivari", "émeute de subsistance", "révolte contre l’impôt"].forEach(function (f, k) {
        var q = i === 1 ? A.s(p, 0.35 + k * 0.15, 0.6 + k * 0.15) : 1;
        s += A.boite(18 + k * 112, 140 + (k % 2) * 40, 104, 32, f, { k: "frein", t: 11.5, op: q * (i === 2 ? 0.5 : 1) });
      });
    }
    /* changement d'échelle : les villages convergent vers l'État */
    if (i === 2) {
      var vil = [[40, 70], [90, 34], [140, 72], [270, 50], [320, 84], [220, 28]], cE = [180, 100];
      vil.forEach(function (v, k) {
        var q = A.s(p, 0.1 + k * 0.06, 0.55 + k * 0.06);
        s += A.cercle(v[0], v[1], 7, { f: "moutarde", op: 0.8 }) + A.fl(v[0], v[1], v[0] + (cE[0] - v[0]) * 0.8 * q, v[1] + (cE[1] - v[1]) * 0.8 * q, { c: "canard", sw: 1.8, p: q > 0 ? 1 : 0 });
      });
      s += A.boite(cE[0] - 70, cE[1] - 2, 140, 30, "État national, industrie", { k: "cause", t: 12, g: true, op: A.s(p, 0.45, 0.8) });
    }
    /* bande 2 : national et autonome (1850-) */
    if (i >= 3) {
      var q2 = i === 3 ? A.s(p, 0, 0.45) : 1;
      s += A.r(X(1850), 252, (X(2026) - X(1850)) * q2, 34, { f: "canardc", s: "canard", r: 6 });
      s += A.t(X(1850) + 5, 266, "national, autonome", { t: 11.5, g: true, c: "canard", op: q2 });
      s += A.t(X(1850) + 6, 280, "syndicats, partis", { t: 10.5, c: "gris", op: q2 });
      [[1864, "1864"], [1884, "1884"]].forEach(function (d, k) {
        var q = i === 3 ? A.s(p, 0.35 + k * 0.1, 0.55 + k * 0.1) : 1;
        s += A.cercle(X(d[0]), ya, 4.5, { f: "canard", op: q });
      });
      if (i === 3) ["grève (1864)", "syndicats (1884)", "manifestation", "pétition, réunion"].forEach(function (f, k) {
        var q = A.s(p, 0.4 + k * 0.12, 0.65 + k * 0.12);
        s += A.boite(14 + (k % 2) * 170, 60 + Math.floor(k / 2) * 46, 160, 36, f, { k: "cause", t: 12.5, g: true, op: q });
      });
    }
    /* bande 3 : élargissement (fin du XXe siècle -) */
    if (i >= 4) {
      var q3 = i === 4 ? A.s(p, 0, 0.4) : 1;
      s += A.r(X(1975), 210, (X(2026) - X(1975)) * q3, 36, { f: "corailc", s: "corail", r: 6 });
      s += A.t(X(1975) - 6, 224, "élargi", { t: 12, g: true, a: "end", c: "corail", op: q3 });
      s += A.t(X(1975) - 6, 238, "médias, justice, en ligne", { t: 10.5, a: "end", c: "gris", op: q3 });
      if (i === 4) ["action médiatique", "contre-expertise", "pétition en ligne", "recours en justice (2021)", "désobéissance civile", "marches pour le climat (2019)"].forEach(function (f, k) {
        var q = A.s(p, 0.3 + k * 0.09, 0.55 + k * 0.09);
        s += A.boite(14 + (k % 2) * 170, 22 + Math.floor(k / 2) * 44, 160, 34, f, { k: "effet", t: 12, op: q });
      });
    }
    if (i === 5) {
      var q5 = A.s(p, 0.1, 0.6);
      s += A.boite(30, 40, 300, 46, "2023, retraites : grèves et manifestations, mais aussi pétitions et réseaux sociaux", { k: "cause", t: 12.5, g: true, op: q5 });
      s += A.fl(316, 92, 316, 204, { c: "canard", sw: 2, p: A.s(p, 0.4, 0.8) });
      s += A.t(306, 150, "les couches s’empilent", { t: 12, g: true, a: "end", c: "canard", op: A.s(p, 0.6, 1), h: true });
    }
    return s;
  }
};

ANIMS["r1-voile"] = {
  t: "Trois sociétés, quatre conceptions de la justice",
  h: 330,
  src: "Exemple fictif construit pour le site (revenus en milliers d’euros par an, sommes vérifiées). Ici, pour simplifier, le bien-être total est mesuré par la somme des revenus. Auteurs : J. Bentham et J. S. Mill ; J. Rawls, <i>Théorie de la justice</i>, 1971 ; R. Nozick, <i>Anarchie, État et utopie</i>, 1974.",
  etapes: [
    { l: "Trois sociétés de cinq personnes (revenus fictifs, en milliers d’euros par an). A est parfaitement égale ; B produit le plus, mais avec de fortes inégalités ; C est inégale, mais moins que B.", d: 4 },
    { l: "Utilitarisme : est juste la société où le bien-être total est le plus grand. En le mesurant par la somme des revenus, B l’emporte : 310, contre 150 pour A et 260 pour C.", d: 4.5 },
    { l: "Égalitarisme strict : est juste la société où les situations sont égales. Seule A convient, même si chacun y est moins riche qu’une partie des habitants de B et C.", d: 4 },
    { l: "Rawls : choisis sans savoir quelle place tu occuperas, derrière un « voile d’ignorance ». Prudent, tu regardes la pire place : 30 en A, 10 en B, 38 en C.", d: 5 },
    { l: "Principe de différence : les inégalités de C sont acceptables, car le plus défavorisé y vit mieux que dans la société égale (38 contre 30). Rawls choisit C, à condition que les libertés de base et l’égalité des chances soient garanties.", d: 5.5 },
    { l: "Libertarisme (Nozick) : on ne compare pas les résultats. Une répartition est juste si chacun a acquis ses revenus par le travail, l’échange libre ou le don ; prendre aux uns pour donner aux autres porte atteinte à leurs droits.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var S = [{ n: "Société A", v: [30, 30, 30, 30, 30] }, { n: "Société B", v: [10, 25, 50, 90, 135] }, { n: "Société C", v: [38, 42, 48, 58, 74] }];
    var base = 222, k = 1.18, s = "";
    var choix = i === 1 ? 1 : i === 2 ? 0 : i === 4 ? 2 : -1, qc = A.s(p, 0.35, 0.8);
    S.forEach(function (so, j) {
      var x0 = 14 + j * 116, tot = so.v.reduce(function (a, b) { return a + b; }, 0), mn = Math.min.apply(null, so.v);
      var choisi = choix === j, eteint = choix >= 0 && !choisi;
      if (choisi) s += A.r(x0 - 6, 30, 110, base - 30 + 34, { f: "moutardec", s: "moutarde", r: 10, op: qc });
      s += A.t(x0 + 49, 48, so.n, { t: 14, g: true, a: "middle", f: true, op: eteint ? 0.45 : 1 });
      so.v.forEach(function (v, m) {
        var q = i === 0 ? A.s(p, j * 0.2 + m * 0.04, j * 0.2 + m * 0.04 + 0.35) : 1;
        var pire = (i === 3 || i === 4) && v === mn && m === 0;
        var h = v * k * q;
        s += A.r(x0 + m * 20, base - h, 16, h, { f: pire ? "corail" : j === 0 ? "gris" : j === 1 ? "canard" : "vert", r: 2, op: eteint ? 0.3 : (i === 3 && !pire ? 0.35 : 1) });
        if (i === 0 || pire) s += A.t(x0 + m * 20 + 8, base - h - 4, String(Math.round(v * q)), { t: 10, a: "middle", g: pire, c: pire ? "corail" : "gris", op: i === 0 ? q : (i === 3 ? A.s(p, 0.5, 0.9) : 1) });
      });
      s += '<line x1="' + (x0 - 3) + '" x2="' + (x0 + 101) + '" y1="' + base + '" y2="' + base + '" style="stroke:var(--encre2);stroke-width:1"/>';
      if (i === 1) s += A.t(x0 + 49, base + 22, "total : " + Math.round(tot * A.s(p, 0, 0.5)), { t: 12.5, g: true, a: "middle", c: choisi ? "encre" : "gris" });
      if (i === 2) s += A.t(x0 + 49, base + 22, j === 0 ? "aucun écart" : "écart : " + (Math.max.apply(null, so.v) - mn), { t: 12.5, g: true, a: "middle", c: choisi ? "encre" : "gris", op: A.s(p, 0.1, 0.5) });
      if (i === 3 || i === 4) s += A.t(x0 + 49, base + 22, "pire place : " + mn, { t: 12.5, g: true, a: "middle", c: j === 2 && i === 4 ? "corail" : "gris" });
    });
    if (i === 3) {
      /* le voile : un rideau translucide passe sur les trois sociétés */
      var v = A.s(p, 0, 0.45) * (1 - A.s(p, 0.55, 0.85));
      s += A.r(4, 56, 352, base - 52, { f: "encre", r: 10, op: 0.55 * v });
      s += A.t(180, 140, "Quelle place auras-tu ?", { t: 16, g: true, a: "middle", c: "papier", op: v, f: true });
    }
    if (i === 4) s += A.fl(14 + 8, base - 30 * k - 10, 14 + 232 + 8, base - 38 * k - 18, { c: "corail", sw: 2, p: A.s(p, 0.1, 0.6), tir: true });
    var verdict = ["", "Utilitarisme → B", "Égalitarisme strict → A", "", "Rawls → C", ""][i];
    if (verdict) s += A.t(180, base + 56, verdict, { t: 16, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.5, 0.9) });
    if (i === 5) {
      var q5 = A.s(p, 0.2, 0.7);
      s += A.r(20, 56, 320, 112, { f: "carte", s: "canard", r: 12, op: q5 });
      s += A.t(180, 92, "Nozick ne choisit pas un tableau :", { t: 13.5, g: true, a: "middle", c: "canard", op: q5 });
      s += A.t(180, 118, "les trois peuvent être justes", { t: 13, a: "middle", op: q5 });
      s += A.t(180, 142, "si les revenus ont été acquis légitimement.", { t: 13, a: "middle", op: q5 });
      s += A.t(180, base + 56, "Libertarisme → la procédure, pas le résultat", { t: 14, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.6, 1), w: 330 });
    }
    return s;
  }
};
