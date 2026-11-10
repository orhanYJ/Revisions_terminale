GRAPHES["r2-ges"] = {
  type: "hbarres", t: "Qui émet le CO₂ fossile dans le monde ? (2024)",
  s: "Part des émissions mondiales de CO₂ d’origine fossile, en %.",
  src: "Source : Global Carbon Project, Global Carbon Budget 2025 (émissions de 2024).",
  unite: " %", lab: 120,
  cats: ["Chine", "États-Unis", "Inde", "Union européenne"],
  series: [{ n: "Part des émissions mondiales", v: [32, 13, 8, 6], c: 2 }]
};

CHAINES["r2-agenda"] = { t: "Comment une question environnementale devient un problème public", e: [
  { t: "Un fait est constaté par des scientifiques et des experts (réchauffement, pollution, disparition d’espèces)", k: "cause" },
  { t: "Des acteurs le dénoncent et le rendent visible : ONG, mouvements citoyens, médias, partis", a: "puis" },
  { t: "Il est défini comme un problème qui appelle une action des pouvoirs publics", a: "donc" },
  { t: "Il entre sur l’agenda politique : débats, lois, négociations ; d’autres acteurs s’y opposent (intérêts économiques)", k: "effet", a: "donc" }
] };
CHAINES["r2-externalite"] = { t: "Pourquoi le marché seul produit trop de pollution", e: [
  { t: "Une entreprise émet des gaz à effet de serre en produisant", k: "cause" },
  { t: "Elle ne paie pas les dommages que subissent les autres : c’est une externalité négative", a: "or" },
  { t: "Son coût privé est inférieur au coût pour la société", a: "donc" },
  { t: "Elle produit et pollue plus que ce qui serait souhaitable pour la société", k: "effet", a: "donc" },
  { t: "D’où l’intervention publique : obliger, taxer, plafonner ou subventionner", k: "cause", a: "d’où" }
] };
CHAINES["r2-taxe"] = { t: "L’effet attendu d’une taxe carbone", e: [
  { t: "L’État fixe un prix par tonne de CO₂ émise (taxe pigouvienne)", k: "cause" },
  { t: "Les produits et activités polluants deviennent plus chers", a: "donc" },
  { f: [{ t: "Ménages : moins de consommation d’énergies fossiles" }, { t: "Entreprises : investissements pour émettre moins" }], a: "donc" },
  { t: "Les émissions baissent là où c’est le moins coûteux ; la taxe rapporte des recettes à redistribuer", k: "effet", a: "donc" }
] };
CHAINES["r2-passager"] = { t: "Le passager clandestin dans les négociations climatiques", e: [
  { t: "Le climat est un bien commun mondial : non excluable, mais chacun peut le dégrader", k: "cause" },
  { t: "Réduire ses émissions coûte au pays qui le fait ; le bénéfice profite à tous", a: "or" },
  { t: "Chaque pays a intérêt à laisser les autres faire l’effort", a: "donc" },
  { t: "Si tous raisonnent ainsi, les réductions sont insuffisantes : le réchauffement continue", k: "frein", a: "donc" },
  { t: "Il faut des accords, des financements et des incitations (ajustement carbone aux frontières)", k: "effet", a: "d’où" }
] };

ANIMS["r2-quotas"] = {
  t: "Le marché de quotas : moins cher pour le même résultat",
  h: 330,
  src: "Exemple simplifié (coûts de réduction constants par tonne, chiffres illustratifs). Réalité : système d’échange de quotas d’émission de l’Union européenne (SEQE), depuis 2005 ; prix qui dépasse pour la première fois 100 € la tonne le 21 février 2023.",
  etapes: [
    { l: "Deux usines émettent chacune 60 tonnes de CO₂. Le régulateur fixe un plafond de 100 tonnes et distribue 50 quotas (droits d’émettre une tonne) à chacune.", d: 4 },
    { l: "Sans échange, chacune doit réduire de 10 tonnes. Réduire une tonne coûte 20 € à A et 60 € à B : A paie 200 €, B paie 600 €. Coût total : 800 €.", d: 4.5 },
    { l: "Avec un marché : comme réduire est bon marché pour A, elle réduit de 20 tonnes et n’utilise que 40 de ses quotas.", d: 3.5 },
    { l: "A vend ses 10 quotas inutilisés à B, par exemple 40 € l’un (entre 20 et 60 €). B n’a plus rien à réduire.", d: 3.5 },
    { l: "Bilan : toujours 100 tonnes émises, mais un coût total de 400 € au lieu de 800 €. A et B gagnent chacune 200 € par rapport à la situation sans échange.", d: 4 },
    { l: "Le prix du quota pousse à réduire les émissions là où c’est le moins cher. Le plafond garantit la quantité ; c’est le prix qui varie.", d: 3.5 }
  ],
  rendu: function (A, i, p) {
    var s = "", us = [{ n: "Usine A", x: 20, cout: 20 }, { n: "Usine B", x: 190, cout: 60 }];
    var red = i === 0 ? [0, 0] : i === 1 ? [10 * A.s(p, 0.1, 0.7), 10 * A.s(p, 0.1, 0.7)] : i === 2 ? [A.l(10, 20, A.s(p, 0.1, 0.8)), 10] : i === 3 ? [20, A.l(10, 0, A.s(p, 0.2, 0.9))] : [20, 0];
    var sc = 2.6, base = 230;
    us.forEach(function (u, j) {
      s += A.t(u.x + 75, 22, u.n, { t: 15, g: true, a: "middle", f: true });
      s += A.t(u.x + 75, 38, "réduire 1 t coûte " + u.cout + " €", { t: 11, a: "middle", c: "gris" });
      var em = 60 - red[j], hEm = em * sc, hRed = red[j] * sc;
      s += A.r(u.x + 40, base - hEm, 70, hEm, { f: "gris", r: 3, op: 0.75 });
      if (hRed > 0.5) s += A.r(u.x + 40, base - 60 * sc, 70, hRed, { f: "none", s: "vert", sw: 2, r: 3 }) + (red[j] > 3 ? A.t(u.x + 75, base - 60 * sc + hRed / 2 + 4, "−" + A.fr(red[j], 0) + " t", { t: 11.5, g: true, a: "middle", c: "vert" }) : "");
      s += A.t(u.x + 75, base - hEm / 2 + 4, A.fr(em, 0) + " t émises", { t: 11.5, g: true, a: "middle", c: "carte" });
      var quotas = j === 0 ? (i >= 3 ? A.l(50, 40, i === 3 ? A.s(p, 0.2, 0.9) : 1) : 50) : (i >= 3 ? A.l(50, 60, i === 3 ? A.s(p, 0.2, 0.9) : 1) : 50);
      s += '<line x1="' + (u.x + 30) + '" x2="' + (u.x + 120) + '" y1="' + (base - quotas * sc) + '" y2="' + (base - quotas * sc) + '" style="stroke:var(--corail);stroke-width:2.5;stroke-dasharray:5 3"/>';
      s += A.t(u.x + 124, base - quotas * sc + 4, A.fr(quotas, 0) + " quotas", { t: 10.5, g: true, c: "corail" });
      var cout = i === 0 ? 0 : i === 1 ? red[j] * u.cout : (j === 0 ? red[0] * 20 - (i >= 3 ? 400 * (i === 3 ? A.s(p, 0.2, 0.9) : 1) : 0) : red[1] * 60 + (i >= 3 ? 400 * (i === 3 ? A.s(p, 0.2, 0.9) : 1) : 0));
      if (i >= 1) s += A.t(u.x + 75, base + 22, "coût net : " + A.fr(cout, 0) + " €", { t: 12.5, g: true, a: "middle", c: "encre" });
    });
    s += '<line x1="10" x2="350" y1="' + base + '" y2="' + base + '" style="stroke:var(--encre2);stroke-width:1"/>';
    if (i === 0) s += A.t(180, 290, "plafond total : 100 tonnes (50 + 50 quotas)", { t: 12.5, g: true, a: "middle", c: "corail", op: A.s(p, 0.4, 0.9) });
    if (i === 1) s += A.t(180, 290, "coût total sans échange : 800 €", { t: 13, g: true, a: "middle", op: A.s(p, 0.6, 1) });
    if (i >= 3) {
      var q = i === 3 ? A.s(p, 0, 0.7) : 1;
      s += A.fl(150, 72, 210, 72, { c: "corail", sw: 2.5, p: q }) + A.t(180, 64, "10 quotas × 40 €", { t: 11.5, g: true, a: "middle", c: "corail", op: q, h: true });
    }
    if (i >= 4) s += A.t(180, 290, "toujours 100 t émises, coût total : 400 €", { t: 13, g: true, a: "middle", c: "vert", op: i === 4 ? A.s(p, 0.3, 0.8) : 1 });
    if (i === 5) s += A.t(180, 312, "le plafond fixe la quantité, le marché fixe le prix", { t: 12, a: "middle", c: "gris", op: A.s(p, 0.3, 0.8) });
    return s;
  }
};

ANIMS["r2-passager"] = {
  t: "Pourquoi les accords climatiques sont si difficiles",
  h: 320,
  src: "Schéma de principe. Repères : Convention-cadre des Nations unies sur les changements climatiques (Rio, 1992) ; accord de Paris (2015) ; objectif de financement de 300 milliards de dollars par an d’ici 2035 (COP29, Bakou, 2024) ; mécanisme d’ajustement carbone aux frontières de l’UE (phase définitive depuis 2026).",
  etapes: [
    { l: "Le climat est un bien commun mondial : tous en profitent, personne ne peut en être exclu, et chacun peut le dégrader par ses émissions.", d: 3.5 },
    { l: "Réduire ses émissions coûte au pays qui le fait. Le bénéfice, un réchauffement moins fort, profite à tous les pays.", d: 3.5 },
    { l: "Chaque pays est donc tenté de laisser les autres faire l’effort tout en profitant du résultat : c’est la stratégie du passager clandestin.", d: 3.5 },
    { l: "Si tous raisonnent ainsi, personne ne réduit assez et le réchauffement continue : c’est la « tragédie des biens communs » (Hardin, 1968).", d: 3.5 },
    { l: "S’y ajoutent les inégalités de développement : les pays pauvres, qui ont peu émis dans l’histoire, refusent de freiner leur croissance sans aide des pays riches.", d: 4 },
    { l: "D’où des accords fondés sur des engagements nationaux (Paris, 2015), des financements pour les pays en développement et des incitations commerciales (ajustement carbone aux frontières).", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", P = [{ n: "Pays riche 1", x: 14, y: 30 }, { n: "Pays riche 2", x: 246, y: 30 }, { n: "Pays émergent", x: 14, y: 196 }, { n: "Pays pauvre", x: 246, y: 196 }];
    var temp = i <= 2 ? 0.5 : i === 3 ? A.l(0.5, 0.9, A.s(p, 0, 1)) : i === 4 ? 0.9 : A.l(0.9, 0.62, A.s(p, 0, 1));
    s += A.r(166, 70, 28, 170, { f: "carte2", r: 14, s: "ligne" }) + A.r(170, 74 + 162 * (1 - temp), 20, 162 * temp, { f: "corail", r: 10 }) + A.cercle(180, 248, 18, { f: "corail" });
    s += A.t(180, 60, "climat", { t: 13, g: true, a: "middle", f: true }) + A.t(180, 288, "réchauffement", { t: 11, a: "middle", c: "gris" });
    P.forEach(function (c, k) {
      var reduit = i === 1 ? k === 0 : i >= 2 && i <= 4 ? false : i === 5;
      var tente = i === 2 || i === 3 || i === 4;
      var em = reduit ? 0.35 : (k === 3 ? 0.25 : 0.8);
      if (i === 1 && k === 0) em = A.l(0.8, 0.35, A.s(p, 0, 0.8));
      if (i === 5) em = k === 3 ? 0.25 : A.l(0.8, 0.45, A.s(p, 0, 0.9));
      s += A.boite(c.x, c.y, 100, 34, c.n, { k: tente && k < 3 ? "frein" : "neutre", t: 12, g: true });
      s += A.jauge(c.x, c.y + 54, 100, em, 1, { c: "gris", l: "émissions" });
      var dx = c.x < 100 ? c.x + 100 : c.x, dy = c.y + 20;
      s += A.fl(dx, dy, dx < 180 ? 164 : 196, 150, { c: "gris", sw: 1.4, op: 0.5, tete: false, tir: true });
      if (i === 1 && k === 0) s += A.t(c.x + 50, c.y + 86, "coût : pour lui seul", { t: 10.5, g: true, a: "middle", c: "corail", op: A.s(p, 0.4, 0.9) });
      if (tente && k < 3) s += A.t(c.x + 50, c.y + 86, "« après vous ! »", { t: 10.5, g: true, a: "middle", c: "moutarde", op: i === 2 ? A.s(p, 0.2 + k * 0.15, 0.6 + k * 0.15) : 1, it: true });
      if (i === 4 && k === 3) s += A.t(c.x + 50, c.y + 86, "« aidez-nous d’abord »", { t: 10.5, g: true, a: "middle", c: "canard", op: A.s(p, 0.3, 0.8), it: true });
    });
    if (i === 1) s += A.t(180, 312, "le bénéfice : pour tous", { t: 12, g: true, a: "middle", c: "vert", op: A.s(p, 0.5, 1) });
    if (i === 5) {
      s += A.fl(296, 126, 296, 192, { c: "vert", sw: 2.6, p: A.s(p, 0.2, 0.7) }) + A.t(292, 160, "financements", { t: 11, g: true, a: "end", c: "vert", op: A.s(p, 0.5, 1), h: true });
    }
    return s;
  }
};

CH.r2 = {
  chapo: "Le climat se réchauffe, des espèces disparaissent, l’air de certaines villes est irrespirable : ces faits ne deviennent des priorités politiques qu’au terme de luttes entre acteurs. Ce chapitre explique comment l’environnement devient un problème public, à quelles échelles on agit, avec quels instruments, et pourquoi les accords mondiaux sont si difficiles.",
  essentiel: [
    "Une question environnementale devient un <b>problème public</b> quand des <b>acteurs</b> (scientifiques, ONG, mouvements citoyens, partis, entreprises, pouvoirs publics) la font reconnaître et l’inscrivent à l’<b>agenda politique</b>, entre <b>coopération et conflit</b>.",
    "L’action publique pour l’environnement articule plusieurs <b>échelles</b> : locale, nationale, européenne et mondiale.",
    "La pollution est une <b>externalité négative</b>. Quatre instruments : la <b>réglementation</b>, la <b>taxation</b>, les <b>marchés de quotas d’émission</b>, les <b>subventions à l’innovation verte</b> ; chacun a ses avantages et ses limites, et leur mise en œuvre peut échouer (acceptabilité, lobbying, fuites de carbone).",
    "Le climat est un <b>bien commun</b> mondial : chaque pays est tenté de jouer le <b>passager clandestin</b>, ce qui freine les accords internationaux.",
    "Les <b>inégalités de développement</b> compliquent encore les négociations : responsabilités historiques des pays riches, besoin de croissance des pays pauvres, financements Nord-Sud."
  ],
  chiffres: [
    { n: "−34,3 %", l: "d’émissions de gaz à effet de serre en France entre 1990 et 2025 ; l’objectif est −50 % en 2030.", s: "Citepa, Secten 2026" },
    { n: "32 %", l: "des émissions mondiales de CO₂ fossile viennent de Chine en 2024, 13 % des États-Unis, 8 % de l’Inde, 6 % de l’Union européenne.", s: "Global Carbon Budget 2025" },
    { n: "300 Md$", l: "par an d’ici 2035 : l’objectif de financement climatique en faveur des pays en développement fixé à la COP29 (Bakou, 2024).", s: "Nations unies, COP29" }
  ],
  objectifs: [
    { bo: "Savoir identifier les différents acteurs (pouvoirs publics, ONG, entreprises, experts, partis, mouvements citoyens) qui participent à la construction des questions environnementales comme problème public et à leur mise à l’agenda politique ; comprendre que ces acteurs entretiennent des relations de coopération et de conflit.", clair: "Nommer les acteurs, dire ce que chacun fait pour (ou contre) la mise à l’agenda, avec un exemple, et montrer qu’ils coopèrent et s’opposent.", voir: "r2-1" },
    { bo: "Comprendre que l’action publique pour l’environnement articule différentes échelles (locale, nationale, européenne, mondiale).", clair: "Donner un exemple d’action à chaque échelle et montrer comment elles s’emboîtent.", voir: "r2-2" },
    { bo: "En prenant l’exemple du changement climatique : connaître les principaux instruments dont disposent les pouvoirs publics pour faire face aux externalités négatives sur l’environnement : réglementation, marchés de quotas d’émission, taxation, subvention à l’innovation verte ; comprendre que ces différents instruments présentent des avantages et des limites, et que leur mise en œuvre peut se heurter à des dysfonctionnements de l’action publique.", clair: "Expliquer les quatre instruments, leurs avantages, leurs limites et les échecs possibles de leur mise en œuvre.", voir: "r2-3" },
    { bo: "En prenant l’exemple du changement climatique : comprendre qu’en présence de bien commun les négociations et accords internationaux liés à la préservation de l’environnement sont contraints par des stratégies de passager clandestin et les inégalités de développement entre pays.", clair: "Expliquer pourquoi les accords climatiques sont difficiles : bien commun, passager clandestin, inégalités de développement.", voir: "r2-4" }
  ],
  notions: ["problème public", "mise à l’agenda politique", "acteurs de l’action publique", "coopération et conflit", "échelles de l’action publique", "externalité négative", "réglementation", "taxation (taxe pigouvienne)", "marché de quotas d’émission", "subvention à l’innovation verte", "dysfonctionnements de l’action publique", "bien commun", "passager clandestin", "inégalités de développement", "responsabilités communes mais différenciées"],
  sections: [
    { id: "r2-1", t: "Comment l’environnement devient un problème public", h:
      '<div class="def"><b>Problème public</b> — situation que des acteurs ont réussi à faire reconnaître comme problématique et comme relevant de l’action des pouvoirs publics. Un problème n’est pas « public » par nature : il le devient par un travail de mobilisation et de définition.</div>' +
      '<div class="def"><b>Mise à l’agenda politique</b> — processus par lequel un problème entre dans la liste des sujets que les pouvoirs publics examinent et sur lesquels ils décident.</div>' +
      '<div data-chain="r2-agenda"></div>' +
      '<div class="tbl"><table><thead><tr><th>Acteur</th><th>Rôle</th><th>Exemple</th></tr></thead><tbody>' +
      '<tr><td><b>Experts, scientifiques</b></td><td>Établir les faits, alerter</td><td>Le GIEC, créé en 1988, synthétise l’état des connaissances sur le climat dans des rapports réguliers.</td></tr>' +
      '<tr><td><b>ONG</b></td><td>Alerter, mobiliser, plaider, poursuivre en justice</td><td>« L’Affaire du siècle » : quatre associations attaquent l’État ; le tribunal administratif de Paris reconnaît sa faute le 3 février 2021.</td></tr>' +
      '<tr><td><b>Mouvements citoyens</b></td><td>Rendre le problème visible, faire pression</td><td>Grève scolaire de Greta Thunberg (août 2018), puis marches pour le climat de 2019 dans de nombreux pays.</td></tr>' +
      '<tr><td><b>Partis</b></td><td>Porter le problème dans la compétition électorale</td><td>Partis écologistes ; reprise du thème par les autres partis.</td></tr>' +
      '<tr><td><b>Entreprises</b></td><td>Innover, mais aussi défendre leurs intérêts (lobbying)</td><td>Secteurs émetteurs qui freinent certaines normes ; entreprises qui investissent dans les technologies propres.</td></tr>' +
      '<tr><td><b>Pouvoirs publics</b></td><td>Décider, légiférer, négocier</td><td>Convention citoyenne pour le climat (150 citoyens tirés au sort, 2019-2020), suivie de la loi Climat et résilience du 22 août 2021.</td></tr>' +
      '</tbody></table></div>' +
      '<p>Ces acteurs <b>coopèrent</b> (scientifiques et ONG qui s’appuient les uns sur les autres, entreprises associées à des politiques publiques) et <b>s’opposent</b> (ONG contre l’État en justice, lobbies contre réglementations, mouvements sociaux contre une taxe jugée injuste).</p>' +
      '<div class="ex src"><p>Le livre de la biologiste Rachel Carson, <i>Silent Spring</i> (1962), sur les effets des pesticides, a joué un grand rôle dans la mise à l’agenda des questions environnementales aux États-Unis ; le DDT y est interdit pour l’agriculture en 1972. Exemple historique, hors des documents du programme.</p></div>' +
      '<div class="ex"><p>Le sujet de dissertation du bac 2026 (jour 1) : « Comment les questions environnementales peuvent-elles devenir un problème public ? ». Plan corrigé dans l’onglet <a href="#r2/bac">Sujets bac</a>.</p></div>' },

    { id: "r2-2", t: "Une action publique à plusieurs échelles", h:
      '<div class="tbl"><table><thead><tr><th>Échelle</th><th>Exemples d’action</th></tr></thead><tbody>' +
      '<tr><td><b>Mondiale</b></td><td>Convention-cadre des Nations unies sur les changements climatiques (Rio, 1992) ; protocole de Kyoto (1997) ; accord de Paris (2015) : limiter le réchauffement « nettement en dessous de 2 °C » et poursuivre les efforts pour 1,5 °C ; conférences annuelles (COP).</td></tr>' +
      '<tr><td><b>Européenne</b></td><td>Système d’échange de quotas d’émission (SEQE, 2005) ; loi européenne sur le climat (2021) : −55 % d’émissions nettes en 2030 par rapport à 1990 et neutralité climatique en 2050 ; mécanisme d’ajustement carbone aux frontières.</td></tr>' +
      '<tr><td><b>Nationale</b></td><td>Stratégie nationale bas-carbone ; Haut Conseil pour le climat ; taxe carbone ; MaPrimeRénov’ ; loi Climat et résilience (2021).</td></tr>' +
      '<tr><td><b>Locale</b></td><td>Plans climat-air-énergie territoriaux des intercommunalités ; transports en commun, pistes cyclables, rénovation des bâtiments publics.</td></tr>' +
      '</tbody></table></div>' +
      '<p>Ces échelles <b>s’emboîtent</b> : l’accord de Paris fixe un objectif mondial, l’Union le traduit en objectifs pour ses États, la France en budgets carbone par secteur, et les collectivités les mettent en œuvre sur le terrain. Elles peuvent aussi entrer en <b>tension</b> : les engagements nationaux sont volontaires, une commune peut aller plus loin que l’État, une règle européenne peut être contestée localement.</p>' +
      '<div class="ex"><p>La France vise −50 % d’émissions brutes en 2030 par rapport à 1990 ; selon le Citepa, ses émissions ont baissé de 34,3 % entre 1990 et 2025 (359,4 millions de tonnes équivalent CO₂ en 2025). Le rythme de baisse doit s’accélérer pour atteindre l’objectif.</p></div>' },

    { id: "r2-3", t: "Les instruments face aux externalités négatives", h:
      '<div class="def"><b>Externalité négative</b> — effet défavorable de l’activité d’un agent sur d’autres agents, sans compensation monétaire. Les émissions de gaz à effet de serre en sont l’exemple type : celui qui émet ne paie pas les dommages du réchauffement.</div>' +
      '<div data-chain="r2-externalite"></div>' +
      '<h3>1. La réglementation</h3><p>Interdire ou imposer des normes : normes d’émission des véhicules, interdiction d’installer des chaudières neuves au fioul ou au charbon en France depuis le 1er juillet 2022, normes de performance énergétique des bâtiments.<br><b>Avantage</b> : efficace et simple à comprendre quand le danger est grave. <b>Limites</b> : coûts de contrôle ; même effort exigé de tous, même de ceux pour qui réduire coûte très cher ; pas d’incitation à faire mieux que la norme.</p>' +
      '<h3>2. La taxation</h3><div class="aut"><span class="mono">AP</span><span class="an">Arthur Cecil Pigou<small>1877-1959</small></span><span class="ad"><i>The Economics of Welfare</i> (1920) : une taxe égale au dommage causé fait « internaliser » l’externalité : le pollueur paie le coût social de son activité. C’est la <b>taxe pigouvienne</b>, à l’origine du principe pollueur-payeur.</span></div>' +
      '<div data-chain="r2-taxe"></div>' +
      '<p><b>Avantage</b> : chacun réduit ses émissions là où c’est le moins coûteux pour lui ; recettes publiques. <b>Limites</b> : on ne sait pas à l’avance de combien les émissions baisseront ; la taxe pèse davantage sur les ménages modestes et ruraux ; elle doit être acceptée.</p>' +
      '<div class="ex"><p>En France, la composante carbone des taxes sur l’énergie est créée en 2014 ; elle atteint 44,6 € par tonne de CO₂ en 2018. La hausse prévue pour 2019 est abandonnée après le mouvement des Gilets jaunes, parti le 17 novembre 2018 d’une contestation de la hausse des prix des carburants.</p></div>' +
      '<h3>3. Le marché de quotas d’émission</h3><p>L’autorité fixe un <b>plafond</b> total d’émissions et distribue ou vend des <b>quotas</b> (droits d’émettre une tonne). Les entreprises qui réduisent facilement leurs émissions revendent leurs quotas à celles pour qui c’est plus coûteux. L’idée vient de John H. Dales (1968), dans le prolongement de Ronald Coase (1960).</p>' +
      '<div data-anim="r2-quotas"></div>' +
      '<p><b>Avantage</b> : la quantité totale d’émissions est garantie ; la réduction se fait au moindre coût. <b>Limites</b> : le prix peut être trop bas si trop de quotas sont distribués (le prix du SEQE est resté longtemps très faible avant les réformes de la fin des années 2010) ; prix instable ; risque de <b>fuites de carbone</b> (production déplacée vers des pays sans contrainte), d’où le mécanisme d’ajustement carbone aux frontières de l’Union, dans sa phase définitive depuis le 1er janvier 2026.</p>' +
      '<h3>4. La subvention à l’innovation verte</h3><p>Financer la recherche et la diffusion de technologies propres (énergies renouvelables, rénovation thermique, véhicules électriques) : MaPrimeRénov’ depuis 2020 en France. <b>Avantage</b> : corrige une autre défaillance, le sous-investissement privé dans l’innovation (les connaissances se diffusent, <a href="#e1:e1-3">É1</a>) ; politiquement plus facile qu’une taxe. <b>Limites</b> : coût pour les finances publiques ; effets d’aubaine ; risque d’effet rebond (<a href="#e1:e1-6">É1</a>).</p>' +
      '<h3>Les dysfonctionnements de l’action publique</h3><ul><li><b>Problèmes d’acceptabilité</b> : l’écotaxe poids lourds, votée en 2009, est abandonnée en 2014 après la mobilisation des « Bonnets rouges » en Bretagne.</li><li><b>Influence des groupes d’intérêt</b> (lobbying) qui obtiennent exemptions ou délais.</li><li><b>Horizon court</b> des responsables politiques face à un problème de long terme.</li><li><b>Inefficacité ou injustice</b> : des mesures mal ciblées pèsent sur les plus modestes sans réduire fortement les émissions.</li></ul>' },

    { id: "r2-4", t: "Bien commun, passager clandestin et inégalités de développement", h:
      '<div class="def"><b>Bien commun</b> — bien <b>non excluable</b> (on ne peut empêcher personne d’en profiter) mais <b>rival</b> (l’usage par les uns réduit ce qui reste pour les autres). Le climat, les océans, la biodiversité en sont des exemples.</div>' +
      '<div class="aut"><span class="mono">GH</span><span class="an">Garrett Hardin<small>1915-2003</small></span><span class="ad">« La tragédie des biens communs » (<i>Science</i>, 1968) : chaque utilisateur d’un pâturage commun a intérêt à y mettre une bête de plus ; si tous le font, le pâturage est détruit. Sans règles, un bien commun est surexploité.</span></div>' +
      '<div class="aut"><span class="mono">EO</span><span class="an">Elinor Ostrom<small>1933-2012 · Nobel 2009</small></span><span class="ad"><i>Governing the Commons</i> (1990) : des communautés savent gérer durablement des biens communs (pêcheries, irrigation) grâce à des règles collectives, sans passer ni par l’État ni par le marché.</span></div>' +
      '<div class="def"><b>Passager clandestin</b> — agent qui profite d’un bien collectif sans contribuer à son coût. Dans les négociations climatiques, un pays profite des efforts des autres sans réduire lui-même ses émissions.</div>' +
      '<div data-anim="r2-passager"></div>' +
      '<div data-chain="r2-passager"></div>' +
      '<div class="ex"><p>Les États-Unis n’ont jamais ratifié le protocole de Kyoto. Ils ont quitté l’accord de Paris une première fois (retrait effectif en 2020), l’ont réintégré en 2021, puis s’en sont retirés de nouveau en janvier 2025, sur décision du président Trump, avec effet un an plus tard.</p></div>' +
      '<h3>Les inégalités de développement</h3>' +
      '<div data-graph="r2-ges"></div>' +
      '<p>Les pays riches ont émis l’essentiel des gaz accumulés depuis la révolution industrielle ; les pays émergents émettent aujourd’hui beaucoup (la Chine représente 32 % des émissions mondiales de CO₂ fossile en 2024) mais moins par habitant que les États-Unis ; les pays pauvres émettent peu et subissent fortement les effets du réchauffement. D’où le principe des « <b>responsabilités communes mais différenciées</b> » (Rio, 1992) et les demandes de financements :</p>' +
      '<ul><li>en 2009, les pays riches promettent 100 milliards de dollars par an de financements climatiques d’ici 2020 (objectif atteint en 2022 selon l’OCDE) ;</li><li>en 2024, la COP29 de Bakou fixe un objectif d’au moins 300 milliards de dollars par an d’ici 2035 ;</li><li>la COP28 (Dubaï, 2023) rend opérationnel un fonds pour les « pertes et dommages » subis par les pays vulnérables.</li></ul>' +
      '<div class="cle"><p><b>Pourquoi l’accord de Paris (2015) est différent :</b> au lieu d’objectifs imposés, chaque pays présente ses propres engagements (contributions déterminées au niveau national), révisés tous les cinq ans. Plus de pays participent, mais les engagements additionnés restent insuffisants pour tenir l’objectif de température : le problème du passager clandestin n’a pas disparu.</p></div>' +
      '<div class="ex"><p>Un succès souvent cité : le protocole de Montréal (1987) sur les gaz détruisant la couche d’ozone (CFC). Peu de producteurs, des substituts disponibles, un danger clairement identifié : la couche d’ozone est aujourd’hui en voie de reconstitution.</p></div>' }
  ],
  pieges: [
    { f: "« Un problème environnemental devient public parce qu’il est grave. »", v: "Il le devient parce que des acteurs le font reconnaître et l’inscrivent à l’agenda ; des problèmes graves peuvent rester longtemps ignorés." },
    { f: "Confondre taxe carbone et marché de quotas.", v: "La taxe fixe le <b>prix</b> et laisse la quantité s’ajuster ; le marché de quotas fixe la <b>quantité</b> (plafond) et laisse le prix s’ajuster." },
    { f: "« Un marché de quotas, c’est un droit à polluer sans limite. »", v: "Le plafond limite le total ; acheter un quota oblige quelqu’un d’autre à émettre moins." },
    { f: "« Bien commun = bien public. »", v: "Un bien public est non excluable et non rival (éclairage public) ; un bien commun est non excluable mais <b>rival</b> (stocks de poissons, capacité de l’atmosphère à absorber le CO₂)." },
    { f: "« Le passager clandestin, c’est un pays qui triche. »", v: "C’est un comportement rationnel : profiter de l’effort des autres sans payer ; il ne suppose pas de tricherie." },
    { f: "Citer seulement l’échelle mondiale.", v: "Le programme demande d’articuler local, national, européen et mondial." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Problème public</b> et <b>mise à l’agenda</b> ; acteurs : experts (GIEC, 1988), ONG (Affaire du siècle, 2021), mouvements citoyens (2018-2019), partis, entreprises (lobbying), pouvoirs publics (Convention citoyenne, loi Climat et résilience 2021) ; coopération et conflit.</li>' +
    '<li><b>Échelles</b> : mondiale (Rio 1992, Kyoto 1997, Paris 2015), européenne (SEQE 2005, −55 % en 2030), nationale (SNBC, taxe carbone), locale (plans climat).</li>' +
    '<li><b>Externalité négative</b> ; instruments : <b>réglementation</b> (normes) ; <b>taxe</b> pigouvienne (Pigou, 1920) ; <b>marché de quotas</b> (plafond + échange ; Dales, 1968) ; <b>subvention à l’innovation verte</b>. Dysfonctionnements : acceptabilité (Gilets jaunes 2018, Bonnets rouges 2013-2014), lobbying, fuites de carbone.</li>' +
    '<li><b>Bien commun</b> (non excluable, rival) ; tragédie des communs (Hardin, 1968) ; Ostrom (1990) ; <b>passager clandestin</b> ; <b>responsabilités communes mais différenciées</b>.</li></ul>' +
    '<h3>Chiffres</h3><ul><li>France : GES −34,3 % de 1990 à 2025 (Citepa) ; taxe carbone 44,6 €/t depuis 2018.</li><li>Parts des émissions de CO₂ fossile 2024 : Chine 32 %, États-Unis 13 %, Inde 8 %, UE 6 % (Global Carbon Budget 2025).</li><li>Finance climat : 100 Md$/an promis en 2009 ; 300 Md$/an d’ici 2035 (COP29).</li></ul>',
  chainesFiche: ["r2-agenda", "r2-externalite", "r2-taxe", "r2-passager"],
  quiz: [
    { q: "Un problème devient « public » lorsque…", c: ["des acteurs le font reconnaître comme relevant de l’action des pouvoirs publics", "il touche plus de la moitié de la population", "les scientifiques le mesurent", "il est mentionné une fois dans la presse"], r: 0, e: "C’est un processus de construction et de mobilisation, pas une propriété naturelle du problème.", s: "r2-1" },
    { q: "Le GIEC, créé en 1988, est un exemple d’acteur de type…", c: ["expert scientifique", "ONG militante", "parti politique", "entreprise"], r: 0, e: "Il synthétise l’état des connaissances scientifiques sur le climat.", s: "r2-1" },
    { q: "« L’Affaire du siècle » est…", c: ["une action en justice d’associations contre l’État pour inaction climatique", "un accord international", "une taxe carbone", "un rapport du GIEC"], r: 0, e: "Le tribunal administratif de Paris a reconnu la faute de l’État le 3 février 2021.", s: "r2-1" },
    { q: "L’accord de Paris sur le climat date de…", c: ["2015", "1992", "1997", "2009"], r: 0, e: "1992 : Convention de Rio ; 1997 : protocole de Kyoto ; 2009 : conférence de Copenhague.", s: "r2-2" },
    { q: "L’objectif européen pour 2030 est une baisse des émissions nettes de…", c: ["55 % par rapport à 1990", "100 % par rapport à 2005", "20 % par rapport à 2020", "34 % par rapport à 1990"], r: 0, e: "Loi européenne sur le climat (2021) ; neutralité climatique en 2050.", s: "r2-2" },
    { q: "Une externalité négative est…", c: ["un effet défavorable d’une activité sur d’autres, sans compensation", "une taxe sur la pollution", "un bénéfice pour l’entreprise", "une importation de biens polluants"], r: 0, e: "Exemple : les émissions de CO₂, dont l’émetteur ne paie pas les dommages.", s: "r2-3" },
    { q: "La taxe pigouvienne vise à…", c: ["faire payer au pollueur le coût social de sa pollution", "interdire toute pollution", "subventionner les pollueurs", "fixer un plafond d’émissions"], r: 0, e: "Arthur Pigou (1920) : internaliser l’externalité.", s: "r2-3" },
    { q: "Dans un marché de quotas d’émission, ce qui est fixé à l’avance est…", c: ["la quantité totale d’émissions autorisées", "le prix de la tonne de CO₂", "le nombre d’entreprises", "le montant de la taxe"], r: 0, e: "Le plafond fixe la quantité ; le prix résulte des échanges.", s: "r2-3" },
    { q: "L’avantage principal d’un marché de quotas par rapport à une norme identique pour tous est…", c: ["les réductions se font là où elles coûtent le moins", "il ne coûte rien à personne", "il supprime toute pollution", "il rapporte toujours plus qu’une taxe"], r: 0, e: "Celui qui réduit à bas coût vend ses quotas à celui pour qui c’est cher.", s: "r2-3" },
    { q: "Le mouvement des Gilets jaunes (2018) illustre…", c: ["un problème d’acceptabilité d’une taxe environnementale", "le succès du marché de quotas", "la création du GIEC", "une subvention à l’innovation verte"], r: 0, e: "La hausse prévue de la taxe carbone a été abandonnée.", s: "r2-3" },
    { q: "Un bien commun est…", c: ["non excluable et rival", "excluable et non rival", "non excluable et non rival", "excluable et rival"], r: 0, e: "Ex. : les stocks de poissons, la capacité de l’atmosphère à absorber le CO₂.", s: "r2-4" },
    { q: "Un pays qui profite des réductions d’émissions des autres sans réduire les siennes adopte une stratégie de…", c: ["passager clandestin", "protectionnisme", "soutenabilité forte", "taxe pigouvienne"], r: 0, e: "C’est ce qui rend les accords climatiques fragiles.", s: "r2-4" },
    { q: "Le principe des « responsabilités communes mais différenciées » signifie que…", c: ["tous les pays doivent agir, mais les pays riches davantage", "seuls les pays pauvres doivent agir", "chaque pays réduit ses émissions du même pourcentage", "les pays émergents sont exemptés"], r: 0, e: "Adopté à Rio en 1992, il tient compte des responsabilités historiques et des inégalités de développement.", s: "r2-4" },
    { q: "Pour Elinor Ostrom, les biens communs…", c: ["peuvent être bien gérés par des règles collectives des communautés", "sont toujours détruits", "doivent être privatisés", "doivent être gérés uniquement par l’État"], r: 0, e: "Prix Nobel 2009, <i>Governing the Commons</i> (1990).", s: "r2-4" }
  ],
  cartes: [
    { r: "Problème public", v: "Situation que des acteurs ont fait reconnaître comme relevant de l’action des pouvoirs publics." },
    { r: "Mise à l’agenda politique", v: "Entrée d’un problème dans la liste des sujets que les pouvoirs publics examinent et traitent." },
    { r: "Les six types d’acteurs", v: "Pouvoirs publics, ONG, entreprises, experts, partis, mouvements citoyens ; coopération et conflit." },
    { r: "Échelles de l’action publique", v: "Locale, nationale, européenne, mondiale ; elles s’emboîtent et peuvent entrer en tension." },
    { r: "Externalité négative", v: "Effet défavorable d’une activité sur d’autres agents, sans compensation monétaire (ex. : émissions de CO₂)." },
    { r: "Réglementation", v: "Normes et interdictions (ex. : interdiction des chaudières neuves au fioul en France depuis juillet 2022)." },
    { r: "Taxe pigouvienne", v: "Taxe égale au dommage causé, qui fait internaliser l’externalité (Pigou, 1920)." },
    { r: "Marché de quotas d’émission", v: "Plafond d’émissions + quotas échangeables ; la quantité est fixée, le prix varie (SEQE de l’UE, 2005)." },
    { r: "Subvention à l’innovation verte", v: "Financement public des technologies propres (ex. : MaPrimeRénov’, 2020)." },
    { r: "Fuite de carbone", v: "Déplacement de la production polluante vers des pays aux règles moins strictes." },
    { r: "Bien commun", v: "Bien non excluable mais rival (climat, océans, ressources halieutiques)." },
    { r: "Tragédie des biens communs", v: "Sans règles, un bien commun est surexploité, chacun ayant intérêt à en prendre plus (Hardin, 1968)." },
    { r: "Passager clandestin", v: "Agent qui profite d’un bien collectif sans contribuer à son coût." },
    { r: "Responsabilités communes mais différenciées", v: "Principe de Rio (1992) : tous agissent, les pays riches davantage, du fait de leurs émissions passées et de leurs moyens." },
    { r: "Accord de Paris", v: "2015 : limiter le réchauffement nettement sous 2 °C ; engagements nationaux révisés tous les cinq ans." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site (exemple simplifié)", t: "Taxe ou quotas : calculer le coût d’une réduction", enonce: '<p>Deux usines émettent 60 tonnes chacune ; le plafond est de 100 tonnes. Réduire une tonne coûte 20 € à A et 60 € à B (coûts constants).</p><ol><li>Coût total si chacune réduit de 10 tonnes ?</li><li>Coût total si A réduit de 20 tonnes et B de 0 ?</li><li>À quel prix A et B ont-elles toutes deux intérêt à échanger 10 quotas ?</li></ol>',
      corrige: '<ol><li>10 × 20 + 10 × 60 = 200 + 600 = 800 €.</li><li>20 × 20 = 400 € : moitié moins cher pour le même résultat (100 tonnes).</li><li>Entre 20 et 60 € le quota : au-dessus de 20 €, A gagne à réduire plus pour vendre ; en dessous de 60 €, B gagne à acheter plutôt qu’à réduire. À 40 €, chacune gagne 200 € par rapport à la situation sans échange.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que la mise en œuvre des instruments de l’action publique pour l’environnement peut se heurter à des dysfonctionnements.", enonce: "<p>3,5 points, sans document.</p>",
      corrige: '<div class="copie"><p>Les pouvoirs publics disposent de plusieurs instruments pour réduire les externalités négatives sur l’environnement : réglementation, taxation, marchés de quotas et subventions. Leur mise en œuvre peut toutefois échouer.</p><p>D’abord, un problème d’acceptabilité sociale : une taxe carbone renchérit l’énergie et pèse davantage sur les ménages modestes et ruraux, qui dépendent de la voiture. En France, la hausse prévue de la taxe carbone pour 2019 a été abandonnée après le mouvement des Gilets jaunes, parti en novembre 2018 d’une contestation du prix des carburants ; de même, l’écotaxe poids lourds a été abandonnée en 2014 après la mobilisation des Bonnets rouges.</p><p>Ensuite, l’influence des groupes d’intérêt : des secteurs émetteurs obtiennent des exemptions, des délais ou une distribution généreuse de quotas gratuits. Sur le marché européen de quotas, l’excès de quotas a longtemps maintenu un prix très bas, qui n’incitait guère à réduire les émissions, jusqu’aux réformes de la fin des années 2010. Ces dysfonctionnements réduisent l’efficacité des instruments.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, données Global Carbon Budget", t: "Qui émet le CO₂ fossile ?", enonce: '<p>Document : le graphique « Qui émet le CO₂ fossile dans le monde ? (2024) » dans <a href="#r2:r2-4">le cours</a>.</p><ol><li>Quelle part des émissions mondiales représentent ensemble les quatre émetteurs du document ?</li><li>À l’aide du document et de vos connaissances, montrez que les inégalités de développement compliquent les négociations climatiques.</li></ol>',
      corrige: '<ol><li>Selon le Global Carbon Budget 2025, en 2024, la Chine (32 %), les États-Unis (13 %), l’Inde (8 %) et l’Union européenne (6 %) représentent ensemble 59 % des émissions mondiales de CO₂ d’origine fossile.</li><li>Le document montre que les grands émetteurs actuels comprennent des pays émergents (Chine, Inde) et des pays riches (États-Unis, Union européenne). Les pays riches ont émis l’essentiel des gaz accumulés depuis la révolution industrielle : les émergents leur demandent donc de faire davantage d’efforts et refusent de freiner une croissance dont ils ont besoin pour réduire la pauvreté. Les pays pauvres, qui émettent peu, réclament des financements pour s’adapter. D’où le principe des responsabilités communes mais différenciées (Rio, 1992) et les négociations sur les financements (300 milliards de dollars par an d’ici 2035, COP29). Ces désaccords s’ajoutent à la tentation du passager clandestin : chaque pays attend que les autres agissent.</li></ol>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet officiel : bac 2026, jour 1 (France), dissertation · plan du site", officiel: true, t: "Comment les questions environnementales peuvent-elles devenir un problème public ?", enonce: "<p>Les documents du sujet officiel ne sont pas reproduits ici. « Comment » : plan explicatif.</p>",
      corrige: '<p><b>Problématique.</b> Une dégradation de l’environnement n’entre pas d’elle-même dans le débat politique. Par quels processus et grâce à quels acteurs une question environnementale est-elle reconnue comme un problème appelant l’action des pouvoirs publics ?</p><p><b>I. Des acteurs qui construisent le problème</b><br>A. Les experts établissent et diffusent les faits (GIEC depuis 1988 ; rapports, alertes).<br>B. Les ONG et les mouvements citoyens le rendent visible et mobilisent (marches pour le climat 2019, Affaire du siècle 2021).<br>C. Les médias et les partis le portent dans l’espace public et la compétition électorale.</p><p><b>II. Une mise à l’agenda qui passe par des conflits et des coopérations</b><br>A. Des intérêts opposés : entreprises et lobbies, contestations sociales (Gilets jaunes, 2018).<br>B. Des coopérations : experts et ONG, entreprises qui innovent, citoyens associés (Convention citoyenne 2019-2020).<br>C. Des fenêtres d’opportunité : catastrophes, COP, élections.</p><p><b>III. À plusieurs échelles, de la mise à l’agenda à l’action publique</b><br>A. Mondiale : Rio 1992, Paris 2015.<br>B. Européenne et nationale : SEQE, loi Climat et résilience 2021, taxe carbone.<br>C. Locale : plans climat des collectivités ; tensions entre échelles.</p>' }
  ]
};

AUTEURS.push(
  { ch: "r2", n: "Arthur Cecil Pigou", d: "1877-1959", th: "Taxer le pollueur à hauteur du dommage causé", l: "<i>The Economics of Welfare</i> (1920) : une <b>taxe</b> égale au dommage fait internaliser l’externalité négative (principe pollueur-payeur)." },
  { ch: "r2", n: "Ronald Coase", d: "1910-2013 · Nobel 1991", th: "Des droits de propriété négociables pour régler les externalités", l: "« The Problem of Social Cost » (1960) : avec des <b>droits de propriété</b> bien définis, les parties peuvent négocier pour corriger une externalité ; inspiration des marchés de droits à polluer." },
  { ch: "r2", n: "Garrett Hardin", d: "1915-2003", th: "La tragédie des biens communs", l: "« The Tragedy of the Commons » (1968) : sans règles, chacun surexploite le <b>bien commun</b>, qui finit détruit." },
  { ch: "r2", n: "Elinor Ostrom", d: "1933-2012 · Nobel 2009", th: "Les communautés peuvent gérer durablement les communs", l: "<i>Governing the Commons</i> (1990) : des <b>règles collectives</b> locales permettent de gérer durablement des biens communs, sans État ni marché." }
);
