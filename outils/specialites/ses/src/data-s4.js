GRAPHES["s4-statut"] = {
  type: "hbarres", t: "Les formes d’emploi en 2025 : l’ensemble et les 15-24 ans",
  s: "Répartition des personnes en emploi selon le statut et le contrat, en %. Chaque série totalise 100 % (aux arrondis près).",
  src: "Source : Insee, enquête Emploi 2025 (Insee Première n° 2096, mars 2026, figure 3). Champ : France, personnes vivant dans un logement ordinaire, en emploi. CDD : toutes durées réunies.",
  unite: " %", lab: 140,
  cats: ["CDI ou fonctionnaire", "CDD", "Intérim", "Alternance, stage", "Indépendants (dont micro-entrepreneurs)", "Sans contrat ou contrat inconnu"],
  series: [{ n: "Ensemble des personnes en emploi", v: [72.8, 7.5, 1.8, 3.5, 13.5, 0.9], c: 1 }, { n: "15-24 ans en emploi", v: [39.8, 19.1, 4.6, 30.5, 3.7, 2.4], c: 2 }]
};
GRAPHES["s4-cond"] = {
  type: "hbarres", t: "Conditions de travail des salariés selon la catégorie, 2019",
  s: "Part des salariés concernés, en %.",
  src: "Source : Dares-Drees-DGAFP-Insee, enquête Conditions de travail 2019 (Insee Références, Emploi, chômage, revenus du travail, édition 2023, fiche 4.4). Contraintes de rythme : cadence d’une machine, déplacement automatique d’un produit, normes de production, demande extérieure, surveillance de la hiérarchie… Contraintes physiques : station debout prolongée, postures pénibles, charges lourdes…",
  unite: " %", dec: 0, lab: 150,
  cats: ["Au moins trois contraintes de rythme", "Travail répétitif", "Ne pas pouvoir régler soi-même les incidents", "Au moins trois contraintes physiques"],
  series: [{ n: "Cadres", v: [22, 11, 17, 7], c: 1 }, { n: "Employés", v: [29, 56, 37, 40], c: 3 }, { n: "Ouvriers", v: [54, 69, 42, 64], c: 2 }]
};
GRAPHES["s4-halo"] = {
  type: "hbarres", t: "Sans emploi et souhaitant travailler : chômeurs et halo, 2025",
  s: "Part de la population de chaque âge, en % (et non taux de chômage, qui se rapporte aux seuls actifs).",
  src: "Source : Insee, enquête Emploi 2025 (Insee Première n° 2096, figure 6). Champ : France, personnes de 15 à 64 ans vivant dans un logement ordinaire.",
  unite: " %", lab: 130,
  cats: ["15-24 ans", "25-49 ans", "50-64 ans", "Ensemble des 15-64 ans"],
  series: [{ n: "Au chômage (BIT)", v: [8.5, 6.2, 3.7, 5.8], c: 2 }, { n: "Dans le halo autour du chômage", v: [7.4, 4.4, 2.8, 4.5], c: 3 }]
};

CHAINES["s4-taylor"] = { t: "La logique de l’organisation scientifique du travail (Taylor)", e: [
  { t: "Objectif : supprimer la « flânerie » et les savoir-faire que les ouvriers de métier gardent pour eux", k: "cause" },
  { f: [{ t: "Division verticale : le bureau des méthodes conçoit et chronomètre, l’ouvrier exécute" }, { t: "Division horizontale : le travail est découpé en tâches simples et répétitives" }], a: "donc" },
  { t: "Salaire au rendement et contrôle hiérarchique strict", a: "et" },
  { t: "Forte hausse de la productivité ; des ouvriers peu qualifiés et vite remplaçables", k: "effet", a: "donc" }
] };
CHAINES["s4-ford"] = { t: "Le fordisme : produire en masse, vendre en masse", e: [
  { t: "Chaîne de montage mobile et produit standardisé (Ford T, 1913)", k: "cause" },
  { t: "Gains de productivité considérables, baisse des coûts et des prix", a: "donc" },
  { t: "Salaires plus élevés (« five dollars day », 1914) pour fixer la main-d’œuvre", a: "et" },
  { t: "Production de masse et consommation de masse se soutiennent mutuellement", k: "effet", a: "donc" },
  { t: "Mais monotonie, absentéisme, rotation du personnel, conflits, rigidité face à une demande qui se diversifie", k: "frein", a: "mais" }
] };
CHAINES["s4-post"] = { t: "Pourquoi et comment l’organisation devient post-taylorienne", e: [
  { f: [{ t: "Demande plus variée et plus exigeante en qualité", k: "cause" }, { t: "Concurrence internationale, refus du travail parcellisé", k: "cause" }] },
  { t: "Flexibilité : produire à la commande (juste-à-temps), ajuster effectifs, horaires, tâches", a: "donc" },
  { t: "Recomposition des tâches : polyvalence, rotation, équipes autonomes, contrôle de la qualité par les salariés", a: "donc" },
  { t: "Management participatif : on demande l’avis et l’implication des salariés", a: "et" },
  { f: [{ t: "Plus d’autonomie et de compétences", k: "effet" }, { t: "Intensification : rythme imposé par le client, les délais et les objectifs", k: "frein" }], a: "donc" }
] };
CHAINES["s4-polar"] = { t: "Comment le numérique polarise les emplois", e: [
  { t: "Ordinateurs, logiciels, robots puis intelligence artificielle", k: "cause" },
  { t: "Les tâches routinières (calculs, saisie, contrôle, montage répétitif) sont automatisées", a: "donc" },
  { f: [{ t: "Recul des emplois intermédiaires routiniers (secrétariat, comptabilité de base, ouvriers qualifiés de l’industrie)", k: "frein" }, { t: "Hausse des emplois très qualifiés (conception, analyse) et des emplois peu qualifiés de service difficiles à automatiser (aide à domicile, livraison)", k: "effet" }], a: "donc" },
  { t: "Polarisation des emplois et de leur qualité", k: "effet", a: "donc" }
] };
CHAINES["s4-integr"] = { t: "Pourquoi le travail intègre… et comment ce pouvoir s’affaiblit", e: [
  { f: [{ t: "Revenu et protection sociale attachés à l’emploi", k: "cause" }, { t: "Statut, identité, utilité reconnue", k: "cause" }, { t: "Relations sociales, rythme de vie", k: "cause" }] },
  { t: "Le travail rattache l’individu à la société (solidarité organique, Durkheim ; société salariale, Castel)", k: "effet", a: "donc" },
  { t: "Précarisation, chômage persistant, polarisation de la qualité des emplois", k: "frein", a: "or" },
  { t: "Intégration « incertaine » ou « disqualifiante » (Paugam), risque de désaffiliation (Castel)", k: "frein", a: "donc" }
] };

CH.s4 = {
  chapo: "Livreurs à vélo payés à la course, cadres en télétravail deux jours par semaine, intérimaires dans les entrepôts, jeunes en alternance : le travail a beaucoup changé. Ce chapitre définit précisément travail, emploi et chômage, apprend à juger de la qualité d’un emploi, retrace le passage du taylorisme au post-taylorisme, montre ce que le numérique transforme et pose une question décisive : le travail intègre-t-il encore ?",
  essentiel: [
    "Le <b>travail</b> est une activité de production de biens et de services, rémunérée ou non ; l’<b>emploi</b> est un travail rémunéré, exercé sous un <b>statut</b> (salarié ou non-salarié). Les <b>actifs</b> sont les personnes en emploi et les chômeurs ; les autres sont <b>inactifs</b>. Halo autour du chômage, sous-emploi et micro-entreprise rendent les <b>frontières</b> incertaines.",
    "La <b>qualité de l’emploi</b> se juge sur six descripteurs : conditions de travail, salaire, sécurité économique, horizon de carrière, potentiel de formation, variété des tâches. Elle est très inégale selon la catégorie, l’âge et le sexe.",
    "Le <b>taylorisme</b> divise le travail horizontalement et verticalement sous une hiérarchie stricte ; le <b>fordisme</b> y ajoute la chaîne et la consommation de masse. Le <b>post-taylorisme</b> mise sur la flexibilité, la recomposition des tâches et le management participatif : plus d’autonomie, mais un travail souvent intensifié.",
    "Le <b>numérique</b> brouille les frontières du travail (télétravail : 19,7 % des salariés en 2025 ; travail et hors travail), transforme les relations d’emploi (plateformes) et accroît le risque de <b>polarisation</b> des emplois.",
    "Le travail est source d’<b>intégration sociale</b> (Durkheim, Castel, Paugam) ; la <b>précarisation</b>, un <b>chômage</b> durablement élevé et la <b>polarisation de la qualité des emplois</b> peuvent affaiblir ce pouvoir intégrateur."
  ],
  chiffres: [
    { n: "72,8 %", l: "des personnes en emploi sont en CDI ou fonctionnaires en 2025 ; 9,4 % en CDD ou en intérim (39,8 % de CDI chez les 15-24 ans).", s: "Insee Première n° 2096 (enquête Emploi 2025)" },
    { n: "19,7 %", l: "des salariés télétravaillent au moins un jour par semaine en 2025 (51,7 % des cadres) ; 4 % en 2019.", s: "Insee Première n° 2096" },
    { n: "54 %", l: "des ouvriers subissent au moins trois contraintes de rythme en 2019, contre 34 % de l’ensemble des salariés.", s: "Enquête Conditions de travail 2019" }
  ],
  objectifs: [
    { bo: "Savoir distinguer les notions de travail, activité, statut d’emploi (salarié, non-salarié), chômage ; comprendre que les évolutions des formes d’emploi rendent plus incertaines les frontières entre emploi, chômage et inactivité.", clair: "Définir travail, emploi, activité, statut et chômage, puis montrer, chiffres à l’appui, que les frontières se brouillent (halo, sous-emploi, micro-entrepreneurs).", voir: "s4-1" },
    { bo: "Connaître les principaux descripteurs de la qualité des emplois (conditions de travail, niveau de salaire, sécurité économique, horizon de carrière, potentiel de formation, variété des tâches).", clair: "Citer et illustrer les six descripteurs de la qualité d’un emploi.", voir: "s4-2" },
    { bo: "Comprendre les principales caractéristiques des modèles d’organisation taylorien (division du travail horizontale et verticale, relation hiérarchique stricte) et post-taylorien (flexibilité, recomposition des tâches, management participatif) ; comprendre les effets positifs et négatifs de l’évolution des formes de l’organisation du travail sur les conditions de travail.", clair: "Décrire taylorisme et post-taylorisme et peser leurs effets sur les conditions de travail.", voir: "s4-3" },
    { bo: "Comprendre comment le numérique brouille les frontières du travail (télétravail, travail / hors travail), transforme les relations d’emploi et accroît les risques de polarisation des emplois.", clair: "Expliquer trois effets du numérique : frontières brouillées, nouvelles relations d’emploi (plateformes), polarisation.", voir: "s4-5" },
    { bo: "Comprendre que le travail est source d’intégration sociale et que certaines évolutions de l’emploi (précarisation, taux persistant de chômage élevé, polarisation de la qualité des emplois) peuvent affaiblir ce pouvoir intégrateur.", clair: "Montrer comment le travail intègre, puis comment trois évolutions affaiblissent cette intégration.", voir: "s4-6" }
  ],
  notions: ["travail", "emploi", "activité, population active", "inactivité", "statut d’emploi (salarié, non-salarié)", "chômage au sens du BIT", "halo autour du chômage", "sous-emploi", "formes particulières d’emploi (CDD, intérim)", "micro-entrepreneur", "qualité de l’emploi", "taylorisme", "division horizontale et verticale du travail", "fordisme", "post-taylorisme", "flexibilité", "recomposition des tâches", "management participatif", "télétravail", "plateformes numériques", "polarisation des emplois", "intégration sociale", "précarisation", "désaffiliation"],
  sections: [
    { id: "s4-1", t: "Travail, emploi, activité, chômage : des frontières qui se brouillent", h:
      '<div class="def"><b>Travail</b> — activité humaine de production de biens et de services, rémunérée ou non. Faire la cuisine chez soi, animer bénévolement un club sportif ou livrer des repas sont trois formes de travail.</div>' +
      '<div class="def"><b>Emploi</b> — travail rémunéré et socialement reconnu, exercé dans un cadre juridique : le <b>statut d’emploi</b>. Les <b>salariés</b> travaillent pour un employeur, dans un lien de <b>subordination</b>, contre un salaire (CDI, CDD, intérim, fonctionnaires, apprentis). Les <b>non-salariés</b> (indépendants) travaillent pour leur compte : agriculteurs, artisans, commerçants, professions libérales, micro-entrepreneurs.</div>' +
      '<div class="def"><b>Activité</b> — participation au marché du travail. La <b>population active</b> regroupe les personnes en emploi (actifs occupés) et les <b>chômeurs</b> ; les autres (élèves, retraités, personnes au foyer) sont <b>inactives</b>.</div>' +
      '<div class="def"><b>Chômage au sens du Bureau international du travail (BIT)</b> — situation d’une personne de 15 ans ou plus qui n’a pas travaillé, ne serait-ce qu’une heure, pendant une semaine de référence, est disponible pour travailler dans les deux semaines et a cherché activement un emploi dans le mois précédent (ou en a trouvé un qui commence dans moins de trois mois).</div>' +
      '<div data-graph="s4-statut"></div>' +
      '<p>En 2025, selon l’Insee, 69,3 % des 15-64 ans sont en emploi, 7,7 % des actifs sont au chômage, et 86,5 % des personnes en emploi sont salariées. Les 15-24 ans sont beaucoup plus souvent en contrat temporaire ou en alternance : seuls 39,8 % sont en CDI ou fonctionnaires.</p>' +
      '<h3>Trois zones grises</h3>' +
      '<ul><li><b>Entre chômage et inactivité : le halo.</b> Des personnes souhaitent travailler mais ne sont pas comptées comme chômeuses parce qu’elles ne cherchent pas activement (découragement, problème de garde d’enfant) ou ne sont pas disponibles tout de suite. En 2025, 4,5 % des 15-64 ans sont dans ce <b>halo autour du chômage</b> ; avec les chômeurs, 10,3 % sont sans emploi et souhaitent travailler (Insee).</li>' +
      '<li><b>Entre emploi et chômage : le sous-emploi.</b> Des personnes à temps partiel voudraient travailler plus et sont disponibles (ou sont en chômage partiel). En 2025, 4,4 % des personnes en emploi sont en sous-emploi, 12,3 % des employés peu qualifiés (Insee). Elles ont un emploi, mais pas assez.</li>' +
      '<li><b>Entre salariat et indépendance.</b> Le régime de micro-entrepreneur (créé en 2009 sous le nom d’auto-entrepreneur) concerne 3,7 % des personnes en emploi en 2025. Un livreur ou un chauffeur qui ne travaille que pour une plateforme, aux tarifs qu’elle fixe, est juridiquement indépendant mais économiquement dépendant (section 5).</li></ul>' +
      '<div data-graph="s4-halo"></div>' +
      '<div class="attn"><p>Ne confonds pas la <b>part</b> du chômage dans la population (5,8 % des 15-64 ans) et le <b>taux</b> de chômage, qui rapporte les chômeurs aux seuls actifs (7,7 % en 2025). Pour les 15-24 ans, l’écart est énorme : part de 8,5 % mais taux de 19,8 %, car beaucoup de jeunes sont inactifs (en études).</p></div>' },

    { id: "s4-2", t: "La qualité des emplois : six descripteurs", h:
      '<p class="lede">Deux emplois peuvent avoir le même salaire et être très différents. Le programme retient six <b>descripteurs</b> de la qualité d’un emploi.</p>' +
      '<div class="tbl"><table><thead><tr><th>Descripteur</th><th>Ce qu’il mesure</th><th>Exemple chiffré</th></tr></thead><tbody>' +
      '<tr><td><b>Conditions de travail</b></td><td>Pénibilité physique, rythme, autonomie, risques psychosociaux, horaires</td><td>64 % des ouvriers subissent au moins trois contraintes physiques, 7 % des cadres (2019)</td></tr>' +
      '<tr><td><b>Niveau de salaire</b></td><td>Rémunération, et ce qu’elle permet de vivre</td><td>Temps partiel : 26,6 % des femmes en emploi, 9,2 % des hommes (2025), d’où des salaires mensuels plus faibles</td></tr>' +
      '<tr><td><b>Sécurité économique</b></td><td>Stabilité du contrat, risque de perdre son emploi, protection sociale attachée</td><td>Un salarié sur cinq craint pour son emploi dans l’année (2019)</td></tr>' +
      '<tr><td><b>Horizon de carrière</b></td><td>Possibilités de promotion et de progression du salaire</td><td>Un CDI de cadre ouvre une carrière ; une succession de missions d’intérim, rarement</td></tr>' +
      '<tr><td><b>Potentiel de formation</b></td><td>Apprendre au travail, accéder à la formation continue</td><td>Les salariés les plus qualifiés accèdent davantage à la formation continue que les moins qualifiés</td></tr>' +
      '<tr><td><b>Variété des tâches</b></td><td>Diversité, autonomie, intérêt du travail</td><td>Travail répétitif : 69 % des ouvriers, 11 % des cadres (2019)</td></tr></tbody></table></div>' +
      '<p class="src-l">Sources : enquête Conditions de travail 2019 (Dares-Drees-DGAFP-Insee) ; Insee, enquête Emploi 2025.</p>' +
      '<div data-graph="s4-cond"></div>' +
      '<p>Lecture : en 2019, 54 % des ouvriers déclarent au moins trois contraintes de rythme, contre 22 % des cadres. Les cadres, en revanche, sont davantage interrompus par des tâches imprévues (73 % contre 66 % de l’ensemble des salariés) : leur travail est intense, mais plus autonome.</p>' +
      '<div class="cle"><p>Les descripteurs se <b>cumulent</b> : les emplois peu qualifiés combinent souvent salaire bas, temps partiel subi, contrat court, faible autonomie et peu de formation. C’est ce qu’on appelle la <b>polarisation de la qualité des emplois</b> (section 6).</p></div>' },

    { id: "s4-3", t: "Le modèle taylorien et le fordisme", h:
      '<div data-anim="s4-orga"></div>' +
      '<div class="aut"><span class="mono">FT</span><span class="an">Frederick W. Taylor<small>1856-1915</small></span><span class="ad">Ingénieur américain, auteur de <i>The Principles of Scientific Management</i> (1911). L’<b>organisation scientifique du travail</b> (OST) cherche « la seule bonne façon » (<i>one best way</i>) d’exécuter chaque tâche, mesurée au chronomètre.</span></div>' +
      '<p>Le modèle taylorien repose sur trois principes :</p><ul><li><b>Division verticale</b> : séparation entre ceux qui conçoivent (ingénieurs du bureau des méthodes) et ceux qui exécutent.</li><li><b>Division horizontale</b> : le travail est découpé en tâches élémentaires, chacune confiée à un ouvrier spécialisé qui répète les mêmes gestes.</li><li><b>Relation hiérarchique stricte</b> : contremaîtres qui contrôlent, temps imposés, salaire au rendement.</li></ul>' +
      '<div data-chain="s4-taylor"></div>' +
      '<div class="aut"><span class="mono">HF</span><span class="an">Henry Ford<small>1863-1947</small></span><span class="ad">En 1913, dans l’usine de Highland Park (Michigan), il installe la <b>chaîne de montage mobile</b> pour la Ford T : la pièce vient à l’ouvrier, le rythme est celui de la chaîne. Le 5 janvier 1914, il annonce la journée de travail payée <b>5 dollars</b>, environ le double du salaire courant, pour retenir des ouvriers qui démissionnaient en masse.</span></div>' +
      '<div data-chain="s4-ford"></div>' +
      '<div class="ex"><p>Avec la chaîne, le temps d’assemblage d’un châssis de Ford T passe, selon les chiffres de l’entreprise, de plus de douze heures à environ une heure et demie. Le prix de la voiture baisse fortement et elle devient accessible à une large clientèle, y compris aux ouvriers de Ford.</p></div>' +
      '<h3>Les limites</h3><p>Le sociologue Georges Friedmann parle du « <b>travail en miettes</b> » (1956) : le travail parcellisé est monotone, vide de sens et use les corps. Charlie Chaplin le caricature dans <i>Les Temps modernes</i> (1936). Absentéisme, rotation du personnel, malfaçons et grèves (celles des ouvriers spécialisés en France autour de 1968) en sont les symptômes. Le modèle est aussi <b>rigide</b> : il produit en grande série un produit standard (« la Ford T, de n’importe quelle couleur pourvu qu’elle soit noire », formule attribuée à Ford), alors que la demande se diversifie à partir des années 1970.</p>' },

    { id: "s4-4", t: "Le post-taylorisme : flexibilité, recomposition, participation", h:
      '<p class="lede">À partir des années 1970-1980, les entreprises cherchent une organisation plus <b>flexible</b>, capable de produire des séries variées, de bonne qualité, sans stocks. On parle de modèles <b>post-tayloriens</b>.</p>' +
      '<div data-chain="s4-post"></div>' +
      '<h3>1. La flexibilité</h3><ul><li><b>Productive</b> : produire « juste à temps », à la commande, avec des stocks minimaux (méthode <b>kanban</b> chez Toyota, théorisée par l’ingénieur Taiichi Ohno).</li><li><b>Quantitative</b> : ajuster le volume de travail, en interne (horaires variables, heures supplémentaires) ou en externe (CDD, intérim, sous-traitance).</li><li><b>Qualitative (ou fonctionnelle)</b> : des salariés polyvalents qui changent de poste selon les besoins.</li><li><b>Salariale</b> : une part du salaire liée aux résultats (primes, intéressement).</li></ul>' +
      '<h3>2. La recomposition des tâches</h3><p>On regroupe ce que le taylorisme avait séparé : <b>élargissement</b> (plusieurs tâches d’exécution), <b>enrichissement</b> (tâches de contrôle, de maintenance, de réglage), <b>rotation</b> entre postes, <b>équipes autonomes</b>. Volvo a ainsi organisé ses usines de Kalmar (1974) puis d’Uddevalla (1989) autour d’équipes qui assemblaient une grande partie de la voiture.</p>' +
      '<h3>3. Le management participatif</h3><p>Les salariés sont consultés et impliqués : cercles de qualité, groupes de résolution de problèmes, objectifs négociés, entretiens annuels. On attend d’eux initiative et engagement.</p>' +
      '<h3>Effets positifs et négatifs sur les conditions de travail</h3>' +
      '<div class="tbl"><table><thead><tr><th>Effets positifs</th><th>Effets négatifs</th></tr></thead><tbody>' +
      '<tr><td>Tâches plus variées, plus d’autonomie et de responsabilités</td><td><b>Intensification</b> : rythme fixé par le client, les délais, les objectifs</td></tr>' +
      '<tr><td>Compétences accrues, travail plus intéressant</td><td>Stress, risques psychosociaux, débordement sur la vie privée</td></tr>' +
      '<tr><td>Coopération dans l’équipe</td><td>Contrôle par les pairs et par les indicateurs ; précarité des salariés de la flexibilité externe (intérim, sous-traitance)</td></tr></tbody></table></div>' +
      '<div class="ex"><p>En 1984, 6 % des salariés déclaraient au moins trois contraintes de rythme ; ils sont environ un tiers aujourd’hui (34 % en 2019), selon les enquêtes Conditions de travail de la Dares (les définitions ont un peu évolué d’une enquête à l’autre). Le travail est moins parcellisé qu’à l’époque de Taylor, mais plus pressé.</p></div>' +
      '<div class="aut"><span class="mono">PA</span><span class="an">Philippe Askenazy<small><i>Les Désordres du travail</i>, 2004</small></span><span class="ad">Les nouvelles organisations (« productivisme réactif ») ont amélioré la productivité mais dégradé la santé au travail : troubles musculosquelettiques, accidents, stress, faute d’une prévention adaptée.</span></div>' +
      '<div class="attn"><p>Le taylorisme n’a pas disparu : on parle de <b>néo-taylorisme</b> dans les centres d’appels (scripts, temps de communication mesurés) ou dans les entrepôts de logistique (préparateurs guidés par une commande vocale ou un terminal qui fixe chaque geste). Les deux modèles coexistent.</p></div>' },

    { id: "s4-5", t: "Ce que le numérique change au travail", h:
      '<h3>1. Il brouille les frontières du travail</h3><p><b>Le lieu</b> : en 2025, 19,7 % des salariés télétravaillent au moins un jour par semaine, contre 4 % en 2019 avant la crise sanitaire ; c’est le cas de 51,7 % des cadres (Insee). <b>Le temps</b> : courriels et messageries prolongent le travail le soir et le week-end. La loi du 8 août 2016 a créé un <b>droit à la déconnexion</b>, entré en vigueur le 1<sup>er</sup> janvier 2017, que les entreprises de 50 salariés ou plus doivent organiser.</p>' +
      '<div class="ex"><p>Le télétravail apporte autonomie, moins de transports et une meilleure conciliation pour beaucoup de cadres ; mais il peut isoler, rendre le travail invisible et creuser l’écart avec les métiers qui ne peuvent pas être télétravaillés (ouvriers, soignants, caissières).</p></div>' +
      '<h3>2. Il transforme les relations d’emploi</h3><p>Les <b>plateformes</b> (VTC, livraison de repas, services à la tâche) mettent en relation clients et travailleurs indépendants. L’algorithme attribue les courses, fixe les prix, note les travailleurs : il joue une partie du rôle d’un employeur sans en avoir les obligations (cotisations, salaire minimum, congés).</p>' +
      '<div class="ex"><p>La Cour de cassation a requalifié en contrat de travail la relation d’un livreur avec Take Eat Easy (28 novembre 2018) puis celle d’un chauffeur avec Uber (4 mars 2020), en relevant un lien de subordination. La directive européenne 2024/2831 du 23 octobre 2024 sur le travail via une plateforme crée une présomption de salariat quand la plateforme contrôle le travail ; les États doivent la transposer d’ici décembre 2026.</p></div>' +
      '<h3>3. Il accroît le risque de polarisation des emplois</h3>' +
      '<div data-chain="s4-polar"></div>' +
      '<div class="def"><b>Polarisation des emplois</b> — hausse simultanée des emplois très qualifiés et des emplois peu qualifiés, au détriment des emplois intermédiaires.</div>' +
      '<p>Les économistes David Autor, Frank Levy et Richard Murnane (2003) ont montré que l’informatique remplace d’abord les <b>tâches routinières</b>, codifiables, qui sont souvent au milieu de l’échelle des salaires ; Maarten Goos et Alan Manning parlent de « <i>lousy and lovely jobs</i> » (2007). Selon l’OCDE (<i>Perspectives de l’emploi</i> 2017), entre 1995 et 2015, la part des emplois moyennement qualifiés a reculé de 9,5 points dans l’ensemble des pays de l’OCDE, quand celle des emplois très qualifiés progressait de 7,6 points et celle des emplois peu qualifiés de 1,9 point.</p>' +
      '<div class="plus"><p>En France, la hausse est surtout forte en haut de l’échelle (cadres : 23,8 % de l’emploi en 2025) ; le bas se maintient grâce aux services à la personne. L’intelligence artificielle générative pourrait toucher aussi des tâches qualifiées (rédaction, traduction, programmation) : ses effets sur l’emploi font encore débat.</p></div>' },

    { id: "s4-6", t: "Le travail, source d’intégration… fragilisée", h:
      '<div class="def"><b>Intégration sociale</b> — processus par lequel un individu est rattaché à la société : il y trouve une place, des liens et des règles partagées.</div>' +
      '<div data-chain="s4-integr"></div>' +
      '<div class="aut"><span class="mono">ÉD</span><span class="an">Émile Durkheim<small><i>De la division du travail social</i>, 1893</small></span><span class="ad">Dans les sociétés modernes, la division du travail rend les individus <b>complémentaires</b> et interdépendants : c’est la <b>solidarité organique</b>, qui remplace la solidarité mécanique fondée sur la ressemblance.</span></div>' +
      '<div class="aut"><span class="mono">RC</span><span class="an">Robert Castel<small><i>Les Métamorphoses de la question sociale</i>, 1995</small></span><span class="ad">Au XX<sup>e</sup> siècle, l’emploi salarié stable s’accompagne de droits (protection sociale, droit du travail) : c’est la <b>société salariale</b>. Quand l’emploi se précarise, les individus glissent d’une zone d’<b>intégration</b> vers une zone de <b>vulnérabilité</b>, puis de <b>désaffiliation</b> (perte d’emploi et de liens).</span></div>' +
      '<div class="aut"><span class="mono">SP</span><span class="an">Serge Paugam<small><i>Le Salarié de la précarité</i>, 2000</small></span><span class="ad">L’intégration professionnelle a deux dimensions : le rapport au <b>travail</b> (satisfaction) et le rapport à l’<b>emploi</b> (stabilité). D’où quatre types : intégration <b>assurée</b> (satisfait et stable), <b>laborieuse</b> (stable mais insatisfait), <b>incertaine</b> (satisfait mais instable), <b>disqualifiante</b> (ni l’un ni l’autre).</span></div>' +
      '<h3>Trois évolutions qui affaiblissent le pouvoir intégrateur</h3>' +
      '<ul><li><b>La précarisation</b> : contrats courts concentrés sur les jeunes (19,1 % des 15-24 ans en emploi sont en CDD en 2025) et sur les moins qualifiés ; intérim, temps partiel subi, faux indépendants des plateformes. Difficile de se projeter, de se loger, de construire une carrière.</li>' +
      '<li><b>Un chômage durablement élevé</b> : en 2025, le taux de chômage atteint 7,7 % (après un pic à 10,4 % en 2015), 19,8 % chez les 15-24 ans, et 23,1 % des chômeurs le sont depuis au moins un an (Insee). Le chômage de longue durée isole et disqualifie.</li>' +
      '<li><b>La polarisation de la qualité des emplois</b> : d’un côté des emplois stables, bien payés et autonomes ; de l’autre des emplois instables, pénibles et peu reconnus (12,3 % de sous-emploi chez les employés peu qualifiés). Le travail intègre alors très inégalement.</li></ul>' +
      '<div class="cle"><p>Le travail reste un puissant facteur d’intégration : la plupart des salariés sont en CDI (72,8 % des personnes en emploi en 2025) et 68 % estiment leur travail reconnu (2019). Mais cette intégration est devenue plus <b>inégale</b> : elle dépend de la qualité de l’emploi autant que du fait d’en avoir un.</p></div>' }
  ],
  pieges: [
    { f: "« Le travail, c’est l’emploi. »", v: "Le travail inclut des activités non rémunérées (domestiques, bénévoles). L’<b>emploi</b> est un travail rémunéré, exercé sous un statut." },
    { f: "« Un chômeur, c’est quelqu’un qui n’a pas d’emploi. »", v: "Au sens du BIT, il faut aussi être <b>disponible</b> et <b>chercher activement</b>. Sinon on est inactif, éventuellement dans le halo." },
    { f: "« Les inactifs ne veulent pas travailler. »", v: "Une partie des inactifs souhaite travailler : c’est le <b>halo autour du chômage</b> (4,5 % des 15-64 ans en 2025)." },
    { f: "« Le taux de chômage des jeunes de 19,8 % signifie qu’un jeune sur cinq est chômeur. »", v: "Le taux se rapporte aux <b>actifs</b>. La part des chômeurs parmi tous les 15-24 ans n’est que de 8,5 %." },
    { f: "« Le taylorisme a disparu. »", v: "Il coexiste avec le post-taylorisme : néo-taylorisme dans la logistique et les centres d’appels." },
    { f: "« Le post-taylorisme a amélioré les conditions de travail. »", v: "Il a apporté autonomie et polyvalence, mais aussi <b>intensification</b> du travail et stress : il faut présenter les deux effets." },
    { f: "« La polarisation, c’est la hausse des inégalités de salaires. »", v: "C’est la hausse simultanée des emplois <b>très qualifiés</b> et <b>peu qualifiés</b> au détriment des emplois intermédiaires. Elle peut accroître les inégalités, mais ce n’est pas la même notion." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Travail</b> : production de biens et services, rémunérée ou non. <b>Emploi</b> : travail rémunéré, sous un statut (salarié : subordination ; non-salarié : indépendant).</li>' +
    '<li><b>Actifs</b> = en emploi + chômeurs ; <b>inactifs</b> : les autres. <b>Chômeur BIT</b> : sans emploi, disponible, en recherche active.</li>' +
    '<li><b>Zones grises</b> : halo (4,5 % des 15-64 ans), sous-emploi (4,4 % des personnes en emploi), micro-entrepreneurs (3,7 %), plateformes.</li>' +
    '<li><b>Qualité de l’emploi</b> : conditions de travail, salaire, sécurité économique, horizon de carrière, formation, variété des tâches.</li>' +
    '<li><b>Taylor</b> (1911) : division verticale + horizontale, hiérarchie stricte, chronomètre. <b>Ford</b> (1913-1914) : chaîne mobile, standardisation, 5 dollars par jour, consommation de masse. Limites : travail en miettes (Friedmann), rigidité.</li>' +
    '<li><b>Post-taylorisme</b> : flexibilité (juste-à-temps, Ohno), recomposition des tâches (Volvo), management participatif. Effets : autonomie mais intensification (Askenazy).</li>' +
    '<li><b>Numérique</b> : télétravail et déconnexion ; plateformes et requalifications (Take Eat Easy 2018, Uber 2020, directive 2024/2831) ; polarisation (Autor ; OCDE : −9,5 points d’emplois intermédiaires, 1995-2015).</li>' +
    '<li><b>Intégration</b> : solidarité organique (Durkheim), société salariale et désaffiliation (Castel), quatre types d’intégration (Paugam). Affaiblie par précarisation, chômage persistant, polarisation de la qualité.</li></ul>' +
    '<h3>Chiffres à citer (Insee, 2025)</h3><ul><li>Taux d’emploi 15-64 ans 69,3 % ; chômage 7,7 % (15-24 ans : 19,8 %) ; CDD + intérim 9,4 % de l’emploi ; temps partiel 17,7 % (femmes 26,6 %, hommes 9,2 %).</li><li>Télétravail : 19,7 % des salariés, 51,7 % des cadres.</li></ul>',
  chainesFiche: ["s4-taylor", "s4-ford", "s4-post", "s4-polar", "s4-integr"],
  quiz: [
    { q: "Une personne qui prépare chaque soir les repas de sa famille…", c: ["travaille, mais n’occupe pas un emploi", "occupe un emploi", "est chômeuse au sens du BIT", "est dans le halo autour du chômage"], r: 0, e: "Le travail domestique est un travail non rémunéré : ce n’est pas un emploi.", s: "s4-1" },
    { q: "La population active comprend…", c: ["les personnes en emploi et les chômeurs", "seulement les salariés", "toutes les personnes de 15 à 64 ans", "les personnes en emploi et les retraités"], r: 0, e: "Actifs = actifs occupés + chômeurs. Élèves, retraités, personnes au foyer sont inactifs.", s: "s4-1" },
    { q: "Une personne sans emploi qui souhaite travailler mais n’a pas cherché d’emploi le mois dernier est…", c: ["inactive, dans le halo autour du chômage", "chômeuse au sens du BIT", "en sous-emploi", "en emploi"], r: 0, e: "Sans recherche active, elle n’est pas chômeuse au sens du BIT ; comme elle souhaite travailler, elle appartient au halo.", s: "s4-1" },
    { q: "Le sous-emploi désigne surtout…", c: ["des personnes à temps partiel qui voudraient travailler plus et sont disponibles", "des chômeurs de longue durée", "des emplois mal payés à temps plein", "des inactifs découragés"], r: 0, e: "4,4 % des personnes en emploi en 2025 (12,3 % des employés peu qualifiés).", s: "s4-1" },
    { q: "Lequel n’est PAS un descripteur de la qualité de l’emploi cité par le programme ?", c: ["La taille de l’entreprise", "L’horizon de carrière", "Le potentiel de formation", "La variété des tâches"], r: 0, e: "Les six descripteurs : conditions de travail, salaire, sécurité économique, horizon de carrière, potentiel de formation, variété des tâches.", s: "s4-2" },
    { q: "En 2019, la part des salariés qui déclarent un travail répétitif est de…", c: ["69 % chez les ouvriers et 11 % chez les cadres", "11 % chez les ouvriers et 69 % chez les cadres", "34 % dans toutes les catégories", "100 % chez les ouvriers"], r: 0, e: "Enquête Conditions de travail 2019 : la variété des tâches est très inégale selon la catégorie.", s: "s4-2" },
    { q: "La division verticale du travail chez Taylor sépare…", c: ["la conception (bureau des méthodes) et l’exécution", "les tâches d’un même atelier entre plusieurs ouvriers", "les hommes et les femmes", "le travail de jour et le travail de nuit"], r: 0, e: "La division horizontale découpe l’exécution en tâches simples ; la verticale sépare ceux qui pensent et ceux qui exécutent.", s: "s4-3" },
    { q: "Ce qu’Henry Ford ajoute au taylorisme, c’est notamment…", c: ["la chaîne de montage mobile et des salaires plus élevés permettant une consommation de masse", "les équipes autonomes", "le juste-à-temps", "le télétravail"], r: 0, e: "Chaîne mobile à Highland Park (1913), « five dollars day » (1914), standardisation : production et consommation de masse.", s: "s4-3" },
    { q: "« Le travail en miettes » (1956) est une critique du travail parcellisé formulée par…", c: ["Georges Friedmann", "Émile Durkheim", "Robert Castel", "Taiichi Ohno"], r: 0, e: "Friedmann décrit la monotonie et la perte de sens du travail taylorisé.", s: "s4-3" },
    { q: "Le juste-à-temps consiste à…", c: ["produire à la commande en limitant les stocks", "allonger les séries de production standardisées", "embaucher uniquement en CDI", "supprimer tout contrôle de la qualité"], r: 0, e: "Méthode kanban de Toyota (Taiichi Ohno) : la demande « tire » la production.", s: "s4-4" },
    { q: "Lequel est un effet NÉGATIF possible du post-taylorisme sur les conditions de travail ?", c: ["L’intensification du travail et le stress", "La polyvalence", "L’enrichissement des tâches", "La participation des salariés aux décisions"], r: 0, e: "Les contraintes de rythme se sont multipliées : 6 % des salariés en cumulaient au moins trois en 1984, 34 % en 2019.", s: "s4-4" },
    { q: "En 2025, la part des salariés qui télétravaillent au moins un jour par semaine est d’environ…", c: ["20 %", "4 %", "50 %", "80 %"], r: 0, e: "19,7 % des salariés (51,7 % des cadres), contre 4 % en 2019 (Insee).", s: "s4-5" },
    { q: "La polarisation des emplois désigne…", c: ["la hausse des emplois très qualifiés et peu qualifiés au détriment des emplois intermédiaires", "la hausse de tous les emplois qualifiés", "la disparition des emplois peu qualifiés", "la concentration des emplois dans les grandes villes"], r: 0, e: "Les tâches routinières du milieu de l’échelle sont les plus faciles à automatiser (Autor, Levy, Murnane).", s: "s4-5" },
    { q: "Pour Serge Paugam, un salarié en CDI qui n’aime pas son travail connaît une intégration…", c: ["laborieuse", "assurée", "incertaine", "disqualifiante"], r: 0, e: "Stable (emploi) mais insatisfait (travail) : intégration laborieuse.", s: "s4-6" },
    { q: "Chez Robert Castel, la « désaffiliation » désigne…", c: ["la perte conjointe de l’emploi et des liens sociaux", "le passage du salariat à l’indépendance", "la fin de l’adhésion à un syndicat", "la mobilité géographique"], r: 0, e: "On glisse de la zone d’intégration à la zone de vulnérabilité, puis de désaffiliation.", s: "s4-6" }
  ],
  cartes: [
    { r: "Travail", v: "Activité de production de biens et services, rémunérée ou non (domestique, bénévole)." },
    { r: "Emploi", v: "Travail rémunéré et socialement reconnu, exercé sous un statut (salarié ou non-salarié)." },
    { r: "Statut d’emploi", v: "Salarié (subordination à un employeur, salaire) ou non-salarié (indépendant : agriculteur, artisan, profession libérale, micro-entrepreneur)." },
    { r: "Population active", v: "Personnes en emploi + chômeurs. Les autres sont inactives." },
    { r: "Chômeur au sens du BIT", v: "15 ans ou plus, sans emploi pendant la semaine de référence, disponible sous deux semaines, en recherche active le mois précédent." },
    { r: "Halo autour du chômage", v: "Inactifs qui souhaitent travailler mais ne sont pas disponibles ou ne cherchent pas activement (4,5 % des 15-64 ans en 2025)." },
    { r: "Sous-emploi", v: "Personnes à temps partiel souhaitant travailler plus et disponibles, ou en chômage partiel (4,4 % des personnes en emploi en 2025)." },
    { r: "Les 6 descripteurs de la qualité de l’emploi", v: "Conditions de travail, salaire, sécurité économique, horizon de carrière, potentiel de formation, variété des tâches." },
    { r: "Taylorisme (OST)", v: "Division verticale (conception / exécution) et horizontale (tâches parcellisées), hiérarchie stricte, chronométrage. Taylor, 1911." },
    { r: "Fordisme", v: "Chaîne mobile (1913), standardisation, salaires élevés (5 $ par jour, 1914) : production et consommation de masse." },
    { r: "Post-taylorisme", v: "Flexibilité, recomposition des tâches (élargissement, enrichissement, rotation, équipes autonomes), management participatif." },
    { r: "Juste-à-temps (toyotisme)", v: "Produire à la commande, sans stocks (kanban), avec des salariés polyvalents. Taiichi Ohno." },
    { r: "Flexibilité quantitative / qualitative", v: "Quantitative : ajuster le volume de travail (horaires, CDD, intérim). Qualitative : polyvalence des salariés." },
    { r: "Polarisation des emplois", v: "Hausse des emplois très qualifiés et peu qualifiés, recul des emplois intermédiaires routiniers (OCDE : −9,5 points, 1995-2015)." },
    { r: "Solidarité organique (Durkheim)", v: "Cohésion fondée sur la complémentarité des individus spécialisés par la division du travail (1893)." },
    { r: "Désaffiliation (Castel)", v: "Perte de l’emploi et des liens sociaux, au terme d’un glissement par la zone de vulnérabilité (1995)." },
    { r: "Les 4 types d’intégration (Paugam)", v: "Assurée, laborieuse, incertaine, disqualifiante, selon la satisfaction au travail et la stabilité de l’emploi (2000)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice inventé pour le site, données Insee", t: "Part, taux et halo", enonce:
      '<p>En 2025, parmi les 15-24 ans, 8,5 % sont au chômage et 7,4 % dans le halo autour du chômage ; leur taux de chômage est de 19,8 % (Insee).</p><ol><li>Quelle part des 15-24 ans est sans emploi et souhaite travailler ?</li><li>Explique pourquoi le taux de chômage (19,8 %) est bien plus élevé que la part des chômeurs (8,5 %).</li><li>Déduis-en approximativement le taux d’activité des 15-24 ans, puis compare avec la donnée de l’Insee (43,0 %).</li></ol>',
      corrige: '<ol><li>8,5 + 7,4 = 15,9 % des 15-24 ans sont sans emploi et souhaitent travailler (c’est le chiffre publié par l’Insee).</li><li>La part rapporte les chômeurs à <b>toute</b> la population de l’âge ; le taux les rapporte aux seuls <b>actifs</b>. Or beaucoup de 15-24 ans sont inactifs (élèves, étudiants) : le dénominateur du taux est petit.</li><li>Taux de chômage = chômeurs ÷ actifs, donc actifs ÷ population = part des chômeurs ÷ taux de chômage = 8,5 ÷ 19,8 ≈ 0,43, soit environ 43 % : on retrouve le taux d’activité publié (43,0 %).</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Montrez que les évolutions des formes d’emploi rendent plus incertaines les frontières entre emploi, chômage et inactivité.", enonce: "<p>Sans document.</p>",
      corrige: '<div class="copie"><p>Selon le Bureau international du travail, est en emploi toute personne qui a travaillé au moins une heure pendant une semaine de référence ; est chômeuse une personne sans emploi, disponible et qui recherche activement un emploi ; les autres sont inactives. Ces frontières, nettes dans la définition, deviennent floues dans la réalité.</p><p>D’abord, entre chômage et inactivité, des personnes souhaitent travailler sans remplir tous les critères du BIT, parce qu’elles sont découragées ou ne sont pas disponibles immédiatement : c’est le halo autour du chômage, qui concerne 4,5 % des 15-64 ans en 2025 selon l’Insee. Ensuite, entre emploi et chômage, des personnes en emploi à temps partiel voudraient travailler davantage : 4,4 % des personnes en emploi sont en sous-emploi. Elles travaillent, mais restent en partie dans la situation d’un chômeur. Enfin, la multiplication des contrats courts, de l’intérim et du statut de micro-entrepreneur (3,7 % des personnes en emploi) fait alterner les périodes d’emploi et de chômage, et brouille même la frontière entre salariat et indépendance, comme le montre le cas des livreurs des plateformes.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice inventé pour le site, document Dares-Insee", t: "Conditions de travail des salariés en 2019", enonce:
      '<p>Document : le graphique « Conditions de travail des salariés selon la catégorie, 2019 » du <a href="#s4:s4-2">cours</a>.</p><ol><li>Comparez la part des ouvriers et celle des cadres qui déclarent au moins trois contraintes de rythme. (2 points)</li><li>À l’aide du document et de vos connaissances, montrez que l’organisation du travail a des effets différents selon les catégories de salariés. (4 points)</li></ol>',
      corrige: '<ol><li>Selon l’enquête Conditions de travail de 2019, 54 % des ouvriers déclarent au moins trois contraintes de rythme, contre 22 % des cadres, soit 32 points d’écart : la proportion est environ 2,5 fois plus élevée chez les ouvriers.</li><li>Les ouvriers restent proches d’une organisation <b>taylorienne</b> : 69 % ont un travail répétitif et 42 % ne peuvent pas régler eux-mêmes les incidents, signe d’une division verticale forte (la conception et la décision leur échappent). Le post-taylorisme ne les a pas épargnés : flux tendus et juste-à-temps ajoutent des contraintes de rythme liées à la demande, d’où une <b>intensification</b>. Les employés connaissent aussi un travail souvent répétitif (56 %), notamment dans le commerce et les centres d’appels (néo-taylorisme). Les cadres bénéficient au contraire des aspects positifs des organisations post-tayloriennes : autonomie (seuls 17 % ne peuvent pas régler les incidents), tâches variées (11 % de travail répétitif), management participatif. Mais leur travail est aussi intense : 73 % doivent souvent s’interrompre pour une tâche imprévue, et le numérique prolonge leur travail hors du bureau.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet inventé pour le site", t: "Montrez que certaines évolutions de l’emploi peuvent affaiblir le pouvoir intégrateur du travail.", enonce: '<p>Appuie-toi sur les graphiques « Les formes d’emploi en 2025 » et « Sans emploi et souhaitant travailler » du cours, et sur tes connaissances.</p>',
      corrige: '<p><b>Introduction.</b> Le travail intègre : il procure un revenu, des droits, une identité, des liens (Durkheim, Castel). Problème : trois évolutions fragilisent cette intégration.</p><p><b>I. La précarisation de l’emploi.</b> 9,4 % des personnes en emploi en CDD ou en intérim, mais 39,8 % seulement des 15-24 ans en CDI (Insee, 2025) ; sous-emploi (4,4 %, 12,3 % des employés peu qualifiés) ; plateformes. Intégration « incertaine » (Paugam), zone de vulnérabilité (Castel).</p><p><b>II. Un chômage persistant.</b> 7,7 % en 2025, 19,8 % chez les 15-24 ans ; 23,1 % des chômeurs depuis plus d’un an ; halo (4,5 %). Perte de revenu, de statut, de liens : risque de désaffiliation.</p><p><b>III. La polarisation de la qualité des emplois.</b> Emplois qualifiés autonomes et télétravaillables (51,7 % des cadres) contre emplois répétitifs et pénibles (69 % des ouvriers ont un travail répétitif). Intégration « laborieuse » ou « disqualifiante ».</p><p><b>Conclusion.</b> Le travail reste intégrateur pour la majorité (72,8 % en CDI ou fonctionnaires), mais de façon plus inégale.</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Les transformations de l’organisation du travail ont-elles amélioré les conditions de travail ?", enonce: "<p>Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> Depuis les années 1970, le modèle taylorien et fordiste a reculé au profit d’organisations flexibles et participatives, puis le numérique a transformé le travail. Ces changements, souvent présentés comme une libération du travail parcellisé, ont-ils réellement amélioré les conditions de travail, et pour qui ?</p><p><b>I. Des améliorations réelles</b><br>A. La fin du « travail en miettes » pour beaucoup : recomposition des tâches, autonomie, polyvalence (Volvo).<br>B. Le management participatif valorise l’initiative et les compétences.<br>C. Le numérique allège certaines tâches pénibles et permet le télétravail (19,7 % des salariés en 2025).</p><p><b>II. Mais une dégradation sur d’autres plans</b><br>A. L’intensification : 6 % des salariés avec au moins trois contraintes de rythme en 1984, 34 % en 2019 ; stress (Askenazy).<br>B. Le néo-taylorisme dans la logistique et les centres d’appels ; contrôle par les indicateurs et les algorithmes.<br>C. La flexibilité externe reporte l’insécurité sur les précaires (intérim, plateformes).</p><p><b>III. Des effets très inégaux</b><br>A. Ouvriers et employés cumulent contraintes et répétitivité (54 % et 29 % de contraintes de rythme), cadres autonomes mais interrompus.<br>B. Polarisation des emplois et de leur qualité.<br>C. Le rôle des règles : droit à la déconnexion (2016), requalification des travailleurs des plateformes (2018, 2020), directive européenne de 2024.</p>' }
  ]
};

AUTEURS.push(
  { ch: "s4", n: "Frederick W. Taylor", d: "1856-1915", th: "Organisation scientifique du travail : division verticale et horizontale", l: "<i>The Principles of Scientific Management</i> (1911) : chronométrage, « one best way », séparation de la conception et de l’exécution, tâches parcellisées, salaire au rendement." },
  { ch: "s4", n: "Henry Ford", d: "1863-1947", th: "Chaîne de montage mobile et « five dollars day »", l: "Chaîne mobile à Highland Park (1913) pour la Ford T ; journée à 5 dollars (1914) : production standardisée et consommation de masse." },
  { ch: "s4", n: "Georges Friedmann", d: "1902-1977", th: "« Le travail en miettes » : critique du travail parcellisé", l: "<i>Le Travail en miettes</i> (1956) : la parcellisation taylorienne rend le travail monotone et vide de sens." },
  { ch: "s4", n: "Taiichi Ohno", d: "1912-1990", th: "Le toyotisme : juste-à-temps et kanban", l: "Ingénieur de Toyota : production à la commande, sans stocks (kanban), qualité contrôlée par des ouvriers polyvalents." },
  { ch: "s4", n: "Philippe Askenazy", d: "<i>Les Désordres du travail</i>, 2004", th: "Les nouvelles organisations intensifient le travail et dégradent la santé", l: "Le « productivisme réactif » améliore la productivité mais multiplie troubles musculosquelettiques, accidents et stress." },
  { ch: "s4", n: "Robert Castel", d: "1933-2013", th: "Société salariale ; vulnérabilité et désaffiliation", l: "<i>Les Métamorphoses de la question sociale</i> (1995) : l’emploi stable donne des droits (société salariale) ; sa précarisation fait glisser vers la vulnérabilité puis la <b>désaffiliation</b>." },
  { ch: "s4", n: "Serge Paugam", d: "<i>Le Salarié de la précarité</i>, 2000", th: "Quatre types d’intégration professionnelle", l: "Selon la satisfaction au travail et la stabilité de l’emploi : intégration <b>assurée</b>, <b>laborieuse</b>, <b>incertaine</b>, <b>disqualifiante</b>." },
  { ch: "s4", n: "David Autor", d: "avec Levy et Murnane, 2003", th: "L’informatique remplace les tâches routinières : polarisation", l: "Les ordinateurs se substituent aux <b>tâches routinières</b>, souvent intermédiaires, et complètent les tâches abstraites : d’où la <b>polarisation des emplois</b>." }
);

ANIMS["s4-orga"] = {
  t: "De l’atelier à la chaîne, de la chaîne à l’équipe",
  h: 320,
  src: "Schéma explicatif du site (illustration, pas de données d’entreprise). Chiffres de l’étape 7 : enquête Conditions de travail 2019 (Dares-Drees-DGAFP-Insee).",
  etapes: [
    { l: "Avant Taylor, l’ouvrier de métier conçoit, découpe, assemble et contrôle lui-même la pièce, à son rythme. Il garde ses savoir-faire.", d: 4 },
    { l: "Division verticale (Taylor, 1911) : un bureau des méthodes conçoit le travail, le chronomètre et fixe « la seule bonne façon ». L’ouvrier exécute les consignes.", d: 4.5 },
    { l: "Division horizontale : le travail est découpé en tâches simples, une par poste. Chaque ouvrier répète le même geste, sous le contrôle d’un contremaître.", d: 4.5 },
    { l: "Ford (1913) : la chaîne mobile apporte la pièce à l’ouvrier ; c’est elle qui impose le rythme. La production de masse explose et les prix baissent.", d: 5 },
    { l: "Les limites : travail monotone et sans autonomie, absentéisme, départs, malfaçons, grèves ; une production rigide alors que la demande se diversifie.", d: 4.5 },
    { l: "Post-taylorisme : on produit à la commande (juste-à-temps). Une équipe polyvalente tourne sur les postes, contrôle la qualité et propose des améliorations (management participatif).", d: 5 },
    { l: "Bilan : plus d’autonomie et de tâches variées, mais un rythme imposé par le client et les délais. En 2019, 34 % des salariés et 54 % des ouvriers subissent au moins trois contraintes de rythme.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var s = "";
    function ouv(x, y, col, op, gris) {
      return A.g(op === undefined ? 1 : op, A.cercle(x, y - 22, 7, { f: gris ? "gris" : col }) + A.r(x - 8, y - 13, 16, 20, { f: gris ? "gris" : col, r: 5 }));
    }
    var taches = ["Concevoir", "Découper", "Assembler", "Contrôler"];
    if (i === 0) {
      s += ouv(180, 200, "canard", 1);
      taches.forEach(function (t, k) {
        var a = -Math.PI / 2 + k * Math.PI / 2, x = 180 + 110 * Math.cos(a), y = 170 + 80 * Math.sin(a);
        var q = A.s(p, 0.1 + k * 0.15, 0.35 + k * 0.15);
        s += A.fl(180 + 30 * Math.cos(a), 170 + 34 * Math.sin(a), 180 + 70 * Math.cos(a), 170 + 50 * Math.sin(a), { c: "canard", p: q, sw: 1.5 });
        s += A.boite(x - 46, y - 14, 92, 28, t, { k: "meca", op: q });
      });
      s += A.t(180, 300, "Un ouvrier de métier fait tout, à son rythme", { t: 12, a: "middle", c: "gris", op: A.s(p, 0.7, 1) });
      return s;
    }
    if (i === 1 || i === 2) {
      var qb = i === 1 ? A.s(p, 0, 0.35) : 1;
      s += A.boite(70, 20, 220, 40, "Bureau des méthodes : conception, chronométrage", { k: "cause", op: qb });
      s += A.t(300, 46, "⏱", { t: 20, op: qb });
      var qf = i === 1 ? A.s(p, 0.35, 0.65) : 1;
      s += A.fl(180, 62, 180, 118, { c: "canard", p: qf, sw: 2 }) + A.t(188, 96, "consignes, temps imposés", { t: 11, c: "canard", op: qf });
      if (i === 1) {
        s += ouv(180, 190, "corail", 1);
        s += A.t(180, 220, "L’ouvrier exécute", { t: 12, g: true, a: "middle", op: A.s(p, 0.6, 1) });
        s += A.t(180, 290, "Division verticale : penser / exécuter", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.75, 1) });
      } else {
        s += A.boite(130, 122, 100, 26, "Contremaître", { k: "neutre", op: A.s(p, 0, 0.3) });
        taches.slice(1).concat(["Emballer"]).forEach(function (t, k) {
          var x = 60 + k * 80, q = A.s(p, 0.2 + k * 0.12, 0.45 + k * 0.12);
          s += A.fl(180, 150, x, 168, { c: "gris", p: q, sw: 1.2 });
          s += ouv(x, 210, "corail", q);
          s += A.t(x, 236, t, { t: 11, g: true, a: "middle", op: q });
          var rep = (p * 6 + k * 0.3) % 1;
          s += A.g(q, '<path d="M' + (x - 12) + " 250 a12 12 0 1 0 24 0" + '" style="fill:none;stroke:var(--corail);stroke-width:1.5;stroke-dasharray:' + (rep * 38).toFixed(1) + ' 60"/>');
        });
        s += A.t(180, 296, "Division horizontale : une tâche simple par poste", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.7, 1) });
      }
      return s;
    }
    if (i === 3 || i === 4) {
      var yC = 170;
      s += A.r(14, yC, 332, 14, { f: "carte2", s: "ligne", r: 7 });
      for (var g = 0; g < 12; g++) { var gx = 22 + ((g * 28 + (i === 3 ? p * 140 : 0)) % 320); s += A.cercle(gx, yC + 7, 3, { f: "gris", op: 0.6 }); }
      for (var k = 0; k < 5; k++) {
        var x = 16 + ((k * 72 + (i === 3 ? p * 280 : 280)) % 330);
        s += A.r(x, yC - 16, 26, 14, { f: "moutarde", r: 3 }) + A.cercle(x + 6, yC - 2, 3, { f: "encre" }) + A.cercle(x + 20, yC - 2, 3, { f: "encre" });
      }
      ["Découper", "Assembler", "Contrôler", "Emballer"].forEach(function (t, k2) {
        var x2 = 60 + k2 * 80, malade = i === 4 && (k2 === 1 || k2 === 3);
        s += ouv(x2, 140, "corail", 1, malade && A.s(p, 0.2, 0.5) > 0.5);
        s += A.t(x2, 210, t, { t: 11, a: "middle", c: "gris" });
        if (i === 4) {
          var q4 = A.s(p, 0.1 + k2 * 0.12, 0.35 + k2 * 0.12);
          var marque = ["ennui", "absent", "malfaçon", "départ"][k2];
          s += A.r(x2 - 30, 70, 60, 20, { f: "corailc", s: "corail", r: 10, op: q4 }) + A.t(x2, 84, marque, { t: 11, g: true, a: "middle", c: "corail", op: q4 });
        }
      });
      if (i === 3) {
        s += A.t(180, 40, "La chaîne impose le rythme", { t: 14, g: true, a: "middle", c: "canard", f: true, op: A.s(p, 0, 0.3) });
        s += A.fl(40, 236, 320, 236, { c: "canard", p: A.s(p, 0.1, 0.6), sw: 2 }) + A.t(180, 256, "sens de la chaîne", { t: 11, a: "middle", c: "canard", op: A.s(p, 0.3, 0.6) });
        s += A.t(180, 292, "Produit standard, série longue, consommation de masse", { t: 12, g: true, a: "middle", op: A.s(p, 0.6, 1) });
      } else {
        s += A.t(180, 36, "Le « travail en miettes » (Friedmann)", { t: 14, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0, 0.3) });
        s += A.boite(40, 252, 280, 44, "Demande qui se diversifie : la chaîne rigide produit mal des séries variées", { k: "frein", op: A.s(p, 0.6, 0.9) });
      }
      return s;
    }
    if (i === 5) {
      var cx = 150, cy = 175, R = 62, rot = p * Math.PI * 2 / 5;
      s += A.boite(262, 40, 90, 44, "Client : commande", { k: "cause", op: A.s(p, 0, 0.25) });
      s += A.fl(300, 86, 205, 130, { c: "canard", p: A.s(p, 0.1, 0.35), sw: 2 }) + A.t(258, 118, "juste-à-temps", { t: 11, c: "canard", op: A.s(p, 0.2, 0.4) });
      s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" style="fill:none;stroke:var(--canard);stroke-width:1.5;stroke-dasharray:5 5;opacity:.6"/>';
      ["Découpe", "Montage", "Qualité", "Réglage", "Idées"].forEach(function (t, k) {
        var a = -Math.PI / 2 + k * 2 * Math.PI / 5;
        s += A.t(cx + (R + 46) * Math.cos(a), cy + (R + 24) * Math.sin(a) + 4, t, { t: 10.5, g: true, a: "middle", c: "gris", op: A.s(p, 0.2, 0.45) });
        var b = a + rot;
        s += ouv(cx + R * Math.cos(b), cy + R * Math.sin(b) + 10, "canard", A.s(p, 0.15, 0.35));
      });
      s += A.t(cx, cy + 4, "équipe", { t: 12, g: true, a: "middle", c: "canard" }) + A.t(cx, cy + 18, "polyvalente", { t: 12, g: true, a: "middle", c: "canard" });
      s += A.fl(cx + R + 20, cy + 60, 300, 270, { c: "moutarde", p: A.s(p, 0.6, 0.85), sw: 2 }) + A.t(300, 290, "produit livré", { t: 11, a: "middle", c: "moutarde", op: A.s(p, 0.7, 0.9) });
      return s;
    }
    var q6 = A.s(p, 0.1, 0.7);
    s += A.t(180, 40, "Au moins trois contraintes de rythme (2019)", { t: 13, g: true, a: "middle" });
    [["Cadres", 22], ["Ensemble des salariés", 34], ["Ouvriers", 54]].forEach(function (d, k) {
      s += A.jauge(30, 90 + k * 48, 300, d[1] * q6, 100, { c: k === 2 ? "corail" : k === 1 ? "moutarde" : "canard", l: d[0], val: Math.round(d[1] * q6) + " %" });
    });
    s += A.boite(30, 238, 140, 50, "Plus d’autonomie, de polyvalence", { k: "effet", op: A.s(p, 0.6, 0.85) });
    s += A.boite(190, 238, 140, 50, "Mais intensification et stress", { k: "frein", op: A.s(p, 0.7, 0.95) });
    return s;
  }
};
