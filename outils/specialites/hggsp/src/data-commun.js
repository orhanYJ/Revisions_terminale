/* ===== Conteneurs communs : chaque fichier data-*.js y ajoute ses chapitres, dossiers et animations ===== */
var CHAPS = {};      /* CHAPS["t3-a1"] = { … } : un chapitre (voir RENFORTS.md) */
var DOSSIERS = {};   /* DOSSIERS.t3 = { … } : frise, notions, acteurs, cartes, débats, sujets corrigés d'un thème */
var ANIMS = {};      /* ANIMS.nom = { … } : animation explicative pas à pas (voir RENFORTS.md) */
/* Déclare un thème rédigé : rediger("t3", { pb: "problématique", chs: ["t3-intro", "t3-a1", "t3-a2", "t3-otc"] }) */
function rediger(id, o) {
  var t = THEMES.filter(function (x) { return x.id === id; })[0];
  t.statut = "redige";
  if (o.pb) t.pb = o.pb;
  if (o.ecrit) t.ecrit = o.ecrit;
  [t.intro].concat(t.axes, [t.otc]).forEach(function (b, i) { b.ch = o.chs[i]; });
}

/* ===== Programme officiel (arrêté du 19 juillet 2019, BO spécial n° 8 du 25 juillet 2019) ===== */
var THEMES = [
  { id: "t1", n: 1, titre: "De nouveaux espaces de conquête", h: "26-28 h", statut: "redige",
    obj: "Identifier, au-delà des territoires terrestres, les possibilités d'affirmation et de développement des États liées à la conquête de l'espace et de l'océan ; comprendre les défis et rivalités qui en découlent avec l'entrée en jeu de nouveaux acteurs, notamment les entreprises privées.",
    pb: "Le droit international peut-il réguler les rivalités nées de l'affirmation de la puissance dans les espaces océaniques et extra-atmosphériques ?",
    ecrit: "Pas à l'écrit en 2027 (années impaires) : évaluable à l'écrit en 2028. Toujours utile pour le Grand oral et pour comprendre le thème 2.",
    ecrit27: false,
    intro: { t: "Océan et espace : quelles spécificités ?", j: ["Une connaissance et une maîtrise en constante évolution.", "Les dernières frontières ?"], ch: "t1-intro" },
    axes: [
      { t: "Conquêtes, affirmations de puissance et rivalités.", j: ["Les enjeux géopolitiques d'une conquête : la course à l'espace des années 1950 à l'arrivée de nouveaux acteurs (Chine, Inde, entreprises privées…).", "Affirmer sa puissance à partir des mers et des océans : la dissuasion nucléaire et les forces de projection maritimes."], ch: "t1-a1" },
      { t: "Enjeux diplomatiques et coopérations.", j: ["Coopérer pour développer la recherche : la station spatiale internationale.", "Rivalités et coopérations dans le partage, l'exploitation et la préservation des ressources des mers et des océans : de la création des zones économiques exclusives (Convention de Montego Bay) à la gestion commune de la biodiversité (conférence intergouvernementale sur la biodiversité marine, BBNJ : Biological diversity beyond national juridiction)."], ch: "t1-a2" }
    ],
    otc: { t: "La Chine : à la conquête de l'espace, des mers et des océans.", j: ["Une volonté politique d'affirmation (discours, investissements, appropriations…).", "Des enjeux économiques et géopolitiques considérables pour la Chine et le reste du monde."], ch: "t1-otc" }
  },
  { id: "t2", n: 2, titre: "Faire la guerre, faire la paix : formes de conflits et modes de résolution", h: "26-28 h", statut: "redige",
    obj: "Comprendre les logiques des affrontements armés ; étudier les modalités de construction de la paix. Le premier axe part de la définition classique de la guerre par Clausewitz pour aborder, par le terrorisme, des conflits qui sortent du schéma des guerres entre États ; le second montre, avec les traités de Westphalie et l'ONU, la complexité de la construction de la paix.",
    pb: "La guerre reste-t-elle un instrument de la politique, et comment construire une paix durable quand les conflits changent de forme ?",
    ecrit: "Évaluable à l'écrit chaque année, donc en 2027 : c'est le thème prioritaire.",
    ecrit27: true,
    intro: { t: "Formes de conflits et tentatives de paix dans le monde actuel.", j: ["Panorama des conflits armés actuels.", "Essai d'une typologie : nature des conflits, acteurs et modes de résolution."], ch: "t2-intro" },
    axes: [
      { t: "La dimension politique de la guerre : des conflits interétatiques aux enjeux transnationaux.", j: ["La guerre, « continuation de la politique par d'autres moyens » (Clausewitz) : de la guerre de 7 ans aux guerres napoléoniennes.", "Le modèle de Clausewitz à l'épreuve des « guerres irrégulières » : d'Al Qaïda à Daech."], ch: "t2-a1" },
      { t: "Le défi de la construction de la paix.", j: ["Faire la paix par les traités : les traités de Westphalie (1648).", "Faire la paix par la sécurité collective : les actions de l'ONU sous les mandats de Kofi Annan (1997-2006)."], ch: "t2-a2" }
    ],
    otc: { t: "Le Moyen-Orient : conflits régionaux et tentatives de paix impliquant des acteurs internationaux (étatiques et non étatiques).", j: ["Du conflit israélo-arabe au conflit israélo-palestinien : les tentatives de résolution, de la création de l'État d'Israël à nos jours.", "Les deux guerres du Golfe (1991 et 2003) et leurs prolongements : d'une guerre interétatique à un conflit asymétrique."], ch: "t2-otc" }
  },
  { id: "t3", n: 3, titre: "Histoire et mémoires", h: "26-28 h", statut: "bientot",
    obj: "Montrer comment les conflits et leur histoire s'inscrivent dans les mémoires des populations ; étudier le rôle de la connaissance historique et de la justice dans la reconstruction des sociétés et des États après des conflits majeurs.",
    ecrit: "Pas à l'écrit en 2027 (années impaires) : évaluable à l'écrit en 2028.", ecrit27: false,
    intro: { t: "Histoire et mémoire, histoire et justice.", j: ["La différence entre histoire et mémoire.", "Les notions de crime contre l'humanité et de génocide, et le contexte de leur élaboration."] },
    axes: [
      { t: "Histoire et mémoires des conflits.", j: ["Un débat historique et ses implications politiques : les causes de la Première Guerre mondiale.", "Mémoires et histoire d'un conflit : la guerre d'Algérie."] },
      { t: "Histoire, mémoire et justice.", j: ["La justice à l'échelle locale : les tribunaux gacaca face au génocide des Tutsis.", "La construction d'une justice pénale internationale face aux crimes de masse : le tribunal pénal international pour l'ex-Yougoslavie (TPIY)."] }
    ],
    otc: { t: "L'histoire et les mémoires du génocide des Juifs et des Tsiganes.", j: ["Lieux de mémoire du génocide des Juifs et des Tsiganes.", "Juger les crimes nazis après Nuremberg.", "Le génocide dans la littérature et le cinéma."] },
    notions: ["histoire", "mémoire(s)", "devoir de mémoire", "lois mémorielles", "crime contre l'humanité", "génocide", "crime de guerre", "justice transitionnelle", "justice pénale internationale"]
  },
  { id: "t4", n: 4, titre: "Identifier, protéger et valoriser le patrimoine : enjeux géopolitiques", h: "26-28 h", statut: "bientot",
    obj: "Connaître ce que recouvre aujourd'hui la notion de patrimoine, matériel et immatériel, dans ses dimensions historiques et géographiques, et comprendre les enjeux géopolitiques qui lui sont associés.",
    ecrit: "Évaluable à l'écrit en 2027 (années impaires).", ecrit27: true,
    intro: { t: "Introduction", j: ["La construction et l'élargissement de la notion de patrimoine : de la transmission entre individus à l'héritage au profit de l'humanité.", "Le « patrimoine mondial » de l'Unesco : une construction des États et de la communauté internationale, de plus en plus diversifiée mais spatialement concentrée."] },
    axes: [
      { t: "Usages sociaux et politiques du patrimoine", j: ["Réaménager la mémoire. Les usages de Versailles de l'empire à nos jours.", "Conflits de patrimoine. Les frises du Parthénon depuis le XIXe siècle."] },
      { t: "Patrimoine, la préservation entre tensions et concurrences", j: ["Urbanisation, développement économique et préservation du patrimoine. Paris entre protection et nouvel urbanisme…", "La destruction, la protection et la restauration du patrimoine, enjeu géopolitique. La question patrimoniale au Mali.", "Le tourisme culturel, entre valorisation et protection. Venise, entre valorisation touristique et protection du patrimoine."] }
    ],
    otc: { t: "La France et le patrimoine, des actions majeures de valorisation et de protection.", j: ["La gestion du patrimoine français : évolutions d'une politique publique.", "La patrimonialisation, entre héritage culturel et reconversion. Le bassin minier du Nord-Pas-de-Calais.", "Le patrimoine, facteur de rayonnement culturel de la France dans le monde et objet d'action diplomatique (un exemple du patrimoine immatériel : le repas gastronomique des Français)."] },
    notions: ["patrimoine matériel / immatériel", "patrimonialisation", "patrimoine mondial (Unesco, 1972)", "soft power", "mise en tourisme", "restitution"]
  },
  { id: "t5", n: 5, titre: "L'environnement, entre exploitation et protection : un enjeu planétaire", h: "26-28 h", statut: "bientot",
    obj: "Analyser l'évolution des rapports entre les sociétés et leurs milieux, et notamment les changements environnementaux non désirés qu'ils induisent ; en comprendre les enjeux géopolitiques.",
    ecrit: "Évaluable à l'écrit chaque année, donc en 2027.", ecrit27: true,
    intro: { t: "Qu'est-ce que l'environnement ?", j: ["Définitions, représentations, évolutions de la notion d'environnement : une construction historique, sociale et politique.", "Un regard sur l'histoire de l'environnement."] },
    axes: [
      { t: "Exploiter, préserver et protéger.", j: ["Exploiter et protéger une ressource « naturelle » : la forêt française depuis Colbert.", "Le rôle des individus et des sociétés dans l'évolution des milieux : « révolution néolithique » et « révolution industrielle », deux ruptures ?"] },
      { t: "Le changement climatique : approches historique et géopolitique.", j: ["Les fluctuations climatiques et leurs effets : l'évolution du climat en Europe du Moyen Âge au XIXe siècle.", "Le climat, enjeu des relations internationales : les accords internationaux (Sommets de la Terre, COP…)"] }
    ],
    otc: { t: "Les États-Unis et la question environnementale : tensions et contrastes.", j: ["L'environnement aux États-Unis : entre protection de la nature, exploitation des ressources et transformation des milieux depuis le XIXe siècle ; les rôles respectifs de l'État fédéral et des États fédérés.", "Les États-Unis et l'environnement à l'échelle internationale (État, firmes transnationales, ONG…)."] },
    notions: ["environnement", "milieu", "ressource", "anthropocène", "développement durable", "changement climatique", "transition", "gouvernance mondiale"]
  },
  { id: "t6", n: 6, titre: "L'enjeu de la connaissance", h: "26-28 h", statut: "bientot",
    obj: "Mettre en avant les conditions nationales et internationales de la construction de la connaissance, en particulier scientifique, et expliquer comment les États favorisent ou contrôlent, entre coopérations et conflits, sa production ou sa diffusion.",
    ecrit: "Évaluable à l'écrit en 2027 (années impaires).", ecrit27: true,
    intro: { t: "Introduction", j: ["La notion de « société de la connaissance » (Peter Drucker, 1969), portée et débats.", "La notion de communauté savante, communauté scientifique en histoire des sciences.", "Les acteurs et les modalités de la circulation de la connaissance."] },
    axes: [
      { t: "Produire et diffuser des connaissances", j: ["Donner accès à la connaissance : grandes étapes de l'alphabétisation des femmes du XVIe siècle à nos jours dans le monde.", "Produire de la connaissance scientifique : recherche et échanges des hommes et des femmes de science sur la question de la radioactivité de 1896 aux années 1950."] },
      { t: "La connaissance, enjeu politique et géopolitique", j: ["Le renseignement au service des États : les services secrets soviétiques et américains durant la guerre froide.", "Circulation et formation des étudiants, transferts de technologie et puissance économique : l'exemple de l'Inde."] }
    ],
    otc: { t: "Le cyberespace : conflictualité et coopération entre les acteurs.", j: ["Le cyberespace, entre réseaux et territoires (infrastructures, acteurs, liberté ou contrôle des données…)", "Cyberdéfense, entre coopération européenne et souveraineté nationale : le cas français."] },
    notions: ["société de la connaissance", "communauté savante", "alphabétisation", "renseignement", "fuite et circulation des cerveaux", "cyberespace", "souveraineté numérique"]
  }
];

/* ===== L'épreuve (note de service du 11-9-2026, NOR MENE2622655N, BO spécial n° 4 du 17 septembre 2026) ===== */
var EPREUVE = {
  format: [
    ["Durée", "4 heures."],
    ["Coefficient", "16 (épreuve terminale de spécialité). En 2027, l'écrit d'HGGSP a lieu à la mi-juin (calendrier officiel : BO spécial n° 2 du 25 août 2026)."],
    ["Structure", "Deux exercices obligatoires : une <b>dissertation</b> (au choix entre deux sujets, chacun sur un thème différent) et une <b>étude critique d'un ou deux documents</b>, sur un troisième thème, différent des deux sujets de dissertation."],
    ["Notation", "Note sur 20, appréciée avec deux échelles descriptives (une par exercice). Si tu ne traites qu'un exercice, ta copie ne peut pas dépasser 10/20. La maîtrise de la langue compte : une copie défaillante sur ce point ne peut pas avoir la moyenne."],
    ["Croquis", "Un croquis ou un schéma qui appuie la dissertation est valorisé ; il n'est jamais obligatoire."],
    ["Programme", "Rotation annuelle des thèmes. Session paire (2028…) : thèmes 1, 2, 3 et 5. Session impaire (2027…) : thèmes 2, 4, 5 et 6. Les notions de Première peuvent être mobilisées."],
    ["Oral de rattrapage", "20 min de préparation, 20 min d'épreuve : tu choisis une question problématisée parmi deux, tu réponds pendant 10 min, puis 10 min d'échange. Même programme que l'écrit."]
  ],
  dissert: [
    ["Analyser le sujet (15 min)", "Souligne chaque mot. Définis les notions (« puissance », « paix », « espace »…). Repère le cadre : dates, espaces, acteurs. Note le type de sujet : sujet-question (« … ? »), sujet à deux termes (« A et B ») ou sujet-affirmation."],
    ["Problématiser", "La problématique est une vraie question qui fait débat, pas la reformulation du sujet. Cherche une tension : coopération ou rivalité ? efficacité ou limites ? continuité ou rupture ?"],
    ["Mobiliser des exemples", "Au brouillon, liste tes exemples datés et chiffrés, puis classe-les. Le correcteur valorise la précision (une date, un nom, un chiffre) et l'articulation entre notions et exemples."],
    ["Construire un plan", "Deux ou trois parties, chacune avec deux ou trois sous-parties. Plans utiles : thématique (dimensions), dialectique (oui / mais / dépassement), chronologique pour une évolution. Chaque partie répond à une étape de la problématique."],
    ["Rédiger l'introduction", "Accroche datée → définition des termes → cadre → problématique → annonce du plan. Environ 15 lignes."],
    ["Rédiger le développement", "Un paragraphe = une idée : phrase-idée, explication, exemple précis, phrase de liaison. Saute une ligne entre les parties."],
    ["Conclure", "Réponds clairement à la problématique, puis ouvre sur une question voisine (sans poser une question vide)."],
    ["Gérer le temps", "Environ 2 h pour la dissertation, 1 h 45 pour l'étude critique, 15 min de relecture (accords, noms propres, dates)."]
  ],
  etude: [
    ["Lire le titre et la consigne", "Le titre donne le sujet ; la consigne oriente ton plan. Souvent, elle annonce deux ou trois axes : suis-les."],
    ["Présenter le document", "Nature (discours, traité, carte, article…), auteur et sa fonction, date et contexte, destinataire, intention. C'est déjà de l'esprit critique."],
    ["Problématiser", "Une question qui relie le document à l'enjeu du thème."],
    ["Analyser en paragraphes", "Pour chaque idée : cite brièvement le document (entre guillemets, avec la ligne), explique, puis apporte une connaissance extérieure qui éclaire ou contredit le passage."],
    ["Porter un regard critique", "Qui parle, pour qui, pour quoi faire ? Ce que le document montre, ce qu'il tait, ce qui a changé depuis. Ce n'est pas « critiquer » l'auteur, c'est mesurer la portée et les limites du document."],
    ["Conclure", "Réponds à la problématique et dis ce que le document apporte à la compréhension du sujet."]
  ],
  grandOral: "Grand oral (nouvelle note de service applicable dès la session 2027) : coefficient 8, 20 minutes de préparation puis 20 minutes d'épreuve. Tu présentes au jury deux questions adossées à tes deux spécialités ; il en choisit une. Premier temps (10 min, debout) : tu expliques pourquoi tu as choisi la question, puis tu la développes et tu y réponds. Second temps (10 min) : échange avec le jury, qui peut t'interroger sur tout le programme du cycle terminal de tes spécialités en lien avec ta question. Chaque thème, axe, objet de travail conclusif et jalon du programme peut servir de support : le thème 1, absent de l'écrit en 2027, reste un excellent terrain pour le Grand oral.",
  idees: ["Le droit international peut-il protéger la haute mer ? (traité BBNJ)", "L'espace va-t-il devenir un champ de bataille ?", "SpaceX : une entreprise peut-elle devenir une puissance ?", "La guerre est-elle encore la continuation de la politique par d'autres moyens ?", "L'ONU peut-elle encore faire la paix ?", "Pourquoi la paix israélo-palestinienne a-t-elle échoué depuis Oslo ?"]
};

/* ===== Ressources vérifiées (novembre 2026) ===== */
var RESSOURCES = [
  { t: "Textes officiels", l: [
    ["Programme de terminale HGGSP (annexe de l'arrêté du 19 juillet 2019)", "https://eduscol.education.fr/document/23650/download", "PDF Eduscol : la structure exacte des six thèmes et les jalons."],
    ["Note de service de l'épreuve, session 2027 et suivantes", "https://www.education.gouv.fr/bo/2026/Special4/MENE2622655N", "BO spécial n° 4 du 17 septembre 2026 : format, échelles de notation, rotation des thèmes."],
    ["Calendrier des épreuves écrites, session 2027", "https://www.education.gouv.fr/sites/default/files/document/annexe-iii-session-2027-calendrier-des-epreuves-ecrites-du-baccalaureat-general-519826.pdf", "Annexe III du BO spécial n° 2 du 25 août 2026."]
  ] },
  { t: "Ressources d'accompagnement (Eduscol, enseignement de défense)", l: [
    ["Bibliographie et ressources du thème 1", "https://eduscol.education.fr/document/44395/download", "Lectures conseillées, dossiers sur l'espace et les océans."],
    ["Bibliographie et ressources du thème 2", "https://eduscol.education.fr/document/44389/download", "Clausewitz, terrorisme, Westphalie, ONU : les ouvrages de référence."],
    ["CNES : dossiers Géoimage par programme scolaire", "https://cnes.fr/projets/geoimage/dossiers-programmes-scolaires", "Images satellites commentées, dont un dossier « océans et espace »."]
  ] },
  { t: "Sites d'enseignants et d'académies", l: [
    ["Abracadabra HG : thème 1", "https://www.abracadabrahg.com/th1-de-nouveaux-espaces-de-conquete", "Cours et documents d'un professeur, par jalon."],
    ["Géographie-histoire.info : HGGSP Terminale", "https://www.geographie-histoire.info/terminales-g-2019-geopolitique", "Fiches et ressources classées par thème."]
  ] },
  { t: "Comprendre la géopolitique", l: [
    ["Le Dessous des cartes (Arte)", "https://www.arte.tv/fr/videos/RC-014036/le-dessous-des-cartes/", "Épisodes d'environ 12 minutes, uniquement avec des cartes : idéal pour réviser et pour le croquis."],
    ["Diploweb", "https://www.diploweb.com/", "Revue de géopolitique en accès libre : articles, cartes, entretiens."],
    ["Les clés du Moyen-Orient", "https://www.lesclesdumoyenorient.com/", "Encyclopédie en ligne sur le Moyen-Orient : chronologies, portraits, analyses (objet de travail conclusif du thème 2)."],
    ["Agence spatiale européenne (ESA)", "https://www.esa.int/", "Station spatiale, Ariane, débris spatiaux : données et dossiers à jour."],
    ["Autorité internationale des fonds marins (AIFM)", "https://www.isa.org.jm/", "Contrats d'exploration, négociation du code minier."],
    ["SHOM", "https://www.shom.fr/", "Service hydrographique de la Marine : espaces maritimes français, limites, cartes."],
    ["Inventaire forestier (IGN)", "https://inventaire-forestier.ign.fr/", "Les chiffres officiels de la forêt française (surface, essences, mortalité) : thème 5."],
    ["Copernicus, service changement climatique", "https://climate.copernicus.eu/", "Températures mondiales et européennes, bilans annuels (2024 année record) : thème 5."],
    ["NOAA : courbe de Keeling", "https://gml.noaa.gov/ccgg/trends/", "La concentration de CO₂ mesurée à Mauna Loa, mise à jour chaque mois : thème 5."],
    ["CCNUCC (convention sur le climat)", "https://unfccc.int/", "Textes des accords, calendrier et décisions des COP : thème 5."]
  ] },
  { t: "Annales et révisions", l: [
    ["Spécialité HGGSP : programme et épreuve (Annabac)", "https://www.annabac.com/page/specialite-hggsp-en-tle-le-programme", "Présentation du programme ; annales sur abonnement pour une partie."],
    ["Schoolmouv : bac de spécialité HGGSP", "https://www.schoolmouv.fr/baccalaureat/hggsp", "Format de l'épreuve et conseils de révision."],
    ["Sujets et corrigés du bac HGGSP 2026 (L'Étudiant)", "https://www.letudiant.fr/bac/corriges-du-bac/article/sujets-et-corriges-bac-hggsp-2026.html", "Les sujets de juin 2026 et des corrigés de professeurs."]
  ] }
];
var MANUELS = "Manuels de spécialité HGGSP de Terminale (programme 2020) : Hachette, Hatier, Nathan, Magnard, Belin, entre autres. Ils sont payants et réservés aux établissements ; nous n'avons pas trouvé de manuel d'HGGSP de Terminale consultable gratuitement en ligne. Demande à ton professeur l'accès au manuel numérique de ton lycée.";

/* Sujets tombés en métropole (sujets officiels publiés par Eduscol, relevés par Géoconfluences) */
var SUJETS_TOMBES = [
  ["Juin 2026, jour 1", "Dissertation", "Les acteurs de la construction des mémoires", "t3"],
  ["Juin 2026, jour 1", "Dissertation", "Les évolutions des formes de la guerre du XVIIIe siècle à nos jours", "t2"],
  ["Juin 2026, jour 1", "Étude critique", "Les États-Unis et la question environnementale", "t5"],
  ["Juin 2026, jour 2", "Dissertation", "L'État, seul acteur de la protection de l'environnement ?", "t5"],
  ["Juin 2026, jour 2", "Dissertation", "Les acteurs et les modes de résolution des conflits depuis 1648", "t2"],
  ["Juin 2026, jour 2", "Étude critique", "Espace et océans, outils de la puissance des États", "t1"],
  ["Juin 2025, jour 1", "Dissertation", "Les usages du patrimoine en France", "t4"],
  ["Juin 2025, jour 1", "Dissertation", "La puissance des États dans les espaces maritimes et extra-atmosphériques", "t1"],
  ["Juin 2025, jour 1", "Étude critique", "Juger les génocides", "t3"],
  ["Juin 2025, jour 2", "Dissertation", "Le changement climatique, un enjeu géopolitique", "t5"],
  ["Juin 2025, jour 2", "Dissertation", "Construire la paix depuis le XVIIe siècle", "t2"],
  ["Juin 2025, jour 2", "Étude critique", "L'affirmation de la puissance chinoise", "t1"]
];
