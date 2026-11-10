GRAPHES["s5-tend"] = {
  type: "lignes", t: "Voter à chaque tour, parfois, ou jamais : 2002-2022", spark: 1,
  s: "Comportements des inscrits sur l’ensemble des tours de la présidentielle et des législatives de chaque année, en %.",
  src: "Source : Insee, enquêtes sur la participation électorale 2002 à 2022 (Insee Première n° 1929, novembre 2022). Champ : inscrits sur les listes électorales résidant en France métropolitaine.",
  unite: " %", pasX: 1, h: 280, min: 0, max: 60,
  x: [2002, 2007, 2012, 2017, 2022],
  series: [
    { n: "Vote systématique (tous les tours)", c: 1, v: [47.6, 50.9, 47.8, 35.9, 37.0] },
    { n: "Vote intermittent", c: 3, v: [40.1, 40.5, 41.3, 50.8, 47.2] },
    { n: "Abstention systématique (aucun tour)", c: 2, v: [12.2, 8.6, 10.9, 13.4, 15.8] }
  ]
};
GRAPHES["s5-age"] = {
  type: "lignes", t: "Le vote systématique selon l’âge, 2002 et 2022",
  s: "Part des inscrits de chaque âge qui ont voté à tous les tours de la présidentielle et des législatives, en %.",
  src: "Source : Insee, enquêtes sur la participation électorale 2002 et 2022 (Insee Première n° 1929, figure 3). Champ : inscrits résidant en France métropolitaine.",
  unite: " %", pasX: 2, h: 280, min: 0, max: 70,
  x: ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90+"],
  series: [
    { n: "2002", c: 3, v: [32.5, 30.1, 35.3, 42.9, 46.5, 52.0, 54.5, 57.2, 59.4, 60.3, 60.0, 56.8, 55.8, 40.0, 23.5] },
    { n: "2022", c: 1, v: [16.7, 18.1, 19.9, 26.7, 32.7, 40.5, 42.5, 45.6, 47.6, 48.2, 53.7, 54.1, 48.8, 37.1, 21.4] }
  ]
};
GRAPHES["s5-dipl"] = {
  type: "hbarres", t: "Diplôme et participation électorale, 2022",
  s: "Inscrits non étudiants selon leur diplôme, en %.",
  src: "Source : Insee, enquête sur la participation électorale 2022 (Insee Première n° 1929, figure 5). Champ : inscrits hors étudiants, France métropolitaine.",
  unite: " %", lab: 130,
  cats: ["Aucun diplôme", "Diplôme inférieur au bac", "Baccalauréat", "Diplôme du supérieur"],
  series: [{ n: "Vote systématique", v: [28.8, 38.1, 33.3, 43.7], c: 1 }, { n: "Abstention systématique", v: [30.4, 18.0, 15.2, 9.5], c: 2 }]
};
GRAPHES["s5-pcs"] = {
  type: "hbarres", t: "Abstention systématique selon la catégorie sociale, 2022",
  s: "Part des inscrits de 25 ans ou plus qui n’ont voté à aucun tour, en %.",
  src: "Source : Insee, enquête sur la participation électorale 2022 (Insee Première n° 1929, tableau complémentaire 4). Champ : inscrits de 25 ans ou plus, France métropolitaine.",
  unite: " %", lab: 150,
  cats: ["Agriculteurs exploitants", "Artisans, commerçants, chefs d’entreprise", "Cadres", "Professions intermédiaires", "Employés", "Ouvriers", "Retraités"],
  series: [{ n: "2022", v: [8.5, 10.6, 6.8, 11.1, 15.7, 19.7, 16.4], c: 2 }]
};

CHAINES["s5-olson"] = { t: "Le paradoxe de l’action collective (Olson, 1965)", e: [
  { t: "Un bien collectif profite à tous les membres du groupe, qu’ils se mobilisent ou non", k: "cause" },
  { t: "S’engager a un coût certain (temps, argent, risque) ; ma participation change peu le résultat", a: "or" },
  { t: "L’individu rationnel a intérêt à laisser les autres agir : il devient passager clandestin", a: "donc" },
  { t: "Si chacun raisonne ainsi, personne ne se mobilise, même quand tous ont intérêt à l’action", k: "frein", a: "donc" }
] };
CHAINES["s5-depasser"] = { t: "Pourquoi les individus s’engagent malgré tout", e: [
  { t: "Paradoxe d’Olson : le calcul individuel décourage l’action", k: "frein" },
  { f: [{ t: "Incitations sélectives : avantages ou sanctions réservés aux membres (Olson)", k: "cause" }, { t: "Rétributions symboliques : reconnaissance, liens, estime de soi, compétences (Gaxie)", k: "cause" }, { t: "Structure des opportunités politiques favorable : la mobilisation peut réussir (Eisinger, Tarrow)", k: "cause" }], a: "mais" },
  { t: "Le coût de l’engagement baisse ou ses gains augmentent pour l’individu", a: "donc" },
  { t: "L’action collective devient possible", k: "effet", a: "donc" }
] };
CHAINES["s5-diplome"] = { t: "Pourquoi le diplôme favorise la participation", e: [
  { t: "Diplôme élevé : connaissances, aisance avec l’écrit et la parole, information", k: "cause" },
  { t: "Sentiment de compétence politique : on se sent légitime pour avoir un avis et le défendre (Gaxie, Le Cens caché, 1978)", a: "donc" },
  { t: "Réseaux, socialisation familiale et professionnelle tournés vers la participation", a: "et" },
  { t: "Vote plus régulier, militantisme, pétitions, engagement associatif", k: "effet", a: "donc" },
  { t: "Les moins diplômés s’abstiennent davantage : 30,4 % d’abstention systématique en 2022, contre 9,5 % des diplômés du supérieur", k: "frein", a: "à l’inverse" }
] };
CHAINES["s5-nms"] = { t: "Des conflits du travail aux nouveaux enjeux de mobilisation", e: [
  { t: "Tertiarisation, recul de la grande industrie et des ouvriers, élévation du niveau d’études", k: "cause" },
  { t: "Valeurs « post-matérialistes » : qualité de vie, autonomie, environnement, égalité (Inglehart)", a: "donc" },
  { f: [{ t: "Nouveaux enjeux : écologie, féminisme, antiracisme, droits des minorités" }, { t: "Acteurs plus diversifiés : associations, collectifs, coordinations, réseaux sociaux" }], a: "donc" },
  { t: "Les conflits du travail ne disparaissent pas, mais ne sont plus le cœur unique de l’action collective", k: "effet", a: "donc" }
] };

CH.s5 = {
  chapo: "Voter, adhérer à un parti, militer dans un syndicat, donner du temps à une association, boycotter une marque, signer une pétition en ligne : l’engagement politique prend bien des formes. Pourquoi s’engager quand on pourrait laisser les autres agir à sa place ? Qui s’engage, et comment les causes, les acteurs et les modes d’action ont-ils changé ? Ce chapitre répond avec les données de l’Insee et les grands auteurs de la science politique.",
  essentiel: [
    "L’<b>engagement politique</b> désigne toutes les formes de participation à la vie publique : <b>vote</b>, <b>militantisme</b> (partis, syndicats), <b>engagement associatif</b>, <b>consommation engagée</b> (boycott, achat responsable). Le vote devient <b>intermittent</b> : en 2022, 47,2 % des inscrits ont voté à certains tours seulement, 37,0 % à tous (Insee).",
    "Le <b>paradoxe de l’action collective</b> (Olson, 1965) : un individu rationnel a intérêt à laisser les autres se mobiliser pour un bien collectif dont il profitera de toute façon (passager clandestin).",
    "Les individus s’engagent pourtant grâce aux <b>incitations sélectives</b> (Olson), aux <b>rétributions symboliques</b> (Gaxie, 1977) et quand la <b>structure des opportunités politiques</b> est favorable (Eisinger, Tarrow).",
    "L’engagement dépend de <b>variables sociodémographiques</b> : la <b>catégorie sociale</b> et le <b>diplôme</b> (abstention systématique : 30,4 % sans diplôme, 9,5 % pour les diplômés du supérieur en 2022), l’<b>âge et la génération</b> (vote systématique : 16,7 % des 18-24 ans, 53,7 % des 70-74 ans), le <b>sexe</b>.",
    "Les <b>objets</b> de l’action collective se diversifient (conflits du travail, nouveaux enjeux, luttes minoritaires), comme les <b>acteurs</b> (partis, syndicats, associations, groupements) et les <b>répertoires d’action</b> (Tilly) : grève et manifestation, mais aussi pétition en ligne, action en justice, occupation, désobéissance civile."
  ],
  chiffres: [
    { n: "15,8 %", l: "des inscrits n’ont voté à aucun tour de la présidentielle et des législatives de 2022 (12,2 % en 2002).", s: "Insee Première n° 1929" },
    { n: "× 3,2", l: "l’abstention systématique est 3,2 fois plus fréquente chez les inscrits sans diplôme (30,4 %) que chez les diplômés du supérieur (9,5 %) en 2022.", s: "Insee Première n° 1929" },
    { n: "21 %", l: "des Français de métropole font du bénévolat dans une association en 2025, soit environ 12 millions de personnes.", s: "Baromètre France Bénévolat / Ifop 2025" }
  ],
  objectifs: [
    { bo: "Comprendre que l’engagement politique prend des formes variées (vote, militantisme, engagement associatif, consommation engagée).", clair: "Définir et illustrer les quatre formes d’engagement citées par le programme.", voir: "s5-1" },
    { bo: "Comprendre pourquoi, malgré le paradoxe de l’action collective, les individus s’engagent (incitations sélectives, rétributions symboliques, structure des opportunités politiques).", clair: "Expliquer le paradoxe d’Olson puis les trois raisons de s’engager malgré lui.", voir: "s5-2" },
    { bo: "Comprendre que l’engagement politique dépend notamment de variables sociodémographiques (catégorie socioprofessionnelle, diplôme, âge et génération, sexe).", clair: "Montrer, chiffres à l’appui, l’effet de la PCS, du diplôme, de l’âge et de la génération, du sexe.", voir: "s5-3" },
    { bo: "Comprendre la diversité et les transformations des objets de l’action collective (conflits du travail, nouveaux enjeux de mobilisation, luttes minoritaires), des acteurs (partis politiques, syndicats, associations, groupements) et de leurs répertoires.", clair: "Décrire ce qui change dans les causes, les organisations et les modes d’action collective.", voir: "s5-4" }
  ],
  notions: ["engagement politique", "participation électorale", "abstention (systématique, intermittente)", "militantisme", "engagement associatif", "consommation engagée (boycott, buycott)", "action collective", "bien collectif", "paradoxe de l’action collective", "passager clandestin", "incitations sélectives", "rétributions symboliques", "structure des opportunités politiques", "compétence politique", "effet d’âge, effet de génération", "conflits du travail", "nouveaux mouvements sociaux", "luttes minoritaires", "partis politiques", "syndicats", "associations", "groupements, groupes d’intérêt", "répertoire d’action collective"],
  sections: [
    { id: "s5-1", t: "Les formes variées de l’engagement politique", h:
      '<div class="def"><b>Engagement politique</b> — participation, individuelle ou collective, à la vie de la cité : choisir ses représentants, défendre une cause, peser sur une décision publique. Il va du geste ponctuel (voter, signer une pétition) à l’investissement durable (militer pendant des années).</div>' +
      '<h3>1. Le vote</h3><p>Forme d’engagement la plus répandue, le vote est un droit (suffrage universel masculin en 1848, étendu aux femmes par l’ordonnance du 21 avril 1944). La participation varie selon l’élection : près des trois quarts des inscrits ont voté au premier tour de la présidentielle de 2022 (73,7 %), 66,7 % au premier tour des législatives anticipées de 2024, le plus haut niveau pour un premier tour de législatives depuis 1997, et un peu plus de la moitié aux européennes de 2024.</p>' +
      '<div data-graph="s5-tend"></div>' +
      '<p>Lecture : selon l’Insee, en 2022, 37,0 % des inscrits ont voté à tous les tours de la présidentielle et des législatives, 47,2 % à certains tours seulement et 15,8 % à aucun. Depuis 2017, le <b>vote intermittent</b> dépasse le vote systématique : beaucoup votent pour l’élection qui leur paraît décisive (la présidentielle) et s’abstiennent aux autres. L’abstention n’est donc pas toujours un retrait : elle peut être un choix ponctuel.</p>' +
      '<h3>2. Le militantisme</h3><div class="def"><b>Militantisme</b> — engagement durable et actif au service d’une organisation ou d’une cause : coller des affiches, tracter, organiser des réunions, représenter ses collègues.</div><p>Il se fait dans les <b>partis politiques</b>, qui visent la conquête du pouvoir, et dans les <b>syndicats</b>, qui défendent les intérêts des salariés. Environ un salarié sur dix est syndiqué en France (10,3 % en 2019, Dares), beaucoup plus dans la fonction publique que dans le privé.</p>' +
      '<h3>3. L’engagement associatif</h3><p>Les associations (loi du 1<sup>er</sup> juillet 1901) défendent des causes (environnement, droits humains, solidarité) ou rendent des services. En 2025, 21 % des Français de métropole font du bénévolat dans une association, soit environ 12 millions de personnes (baromètre France Bénévolat / Ifop). Toutes les associations ne sont pas politiques, mais beaucoup interpellent les pouvoirs publics (Restos du cœur, Greenpeace, Ligue des droits de l’homme).</p>' +
      '<h3>4. La consommation engagée</h3><div class="def"><b>Consommation engagée</b> — usage politique de ses achats : <b>boycott</b> (refuser d’acheter les produits d’une entreprise) ou <b>buycott</b> (acheter de préférence des produits jugés responsables : commerce équitable, produits locaux).</div><div class="ex"><p>Le label de commerce équitable Max Havelaar est créé en 1988 aux Pays-Bas. En 2001, un appel au boycott des produits Danone répond à l’annonce de fermetures d’usines de biscuits LU. La sociologue Sophie Dubuisson-Quellier (<i>La Consommation engagée</i>, 2009) montre que ces gestes individuels sont souvent organisés par des collectifs.</p></div>' +
      '<div class="plus"><p>On peut ajouter d’autres formes : signer une pétition (en ligne ou non), manifester, faire grève, s’exprimer sur les réseaux sociaux, participer à une consultation publique. Les mêmes personnes cumulent souvent plusieurs formes d’engagement.</p></div>' },

    { id: "s5-2", t: "Le paradoxe de l’action collective… et comment on le dépasse", h:
      '<div data-anim="s5-olson"></div>' +
      '<div class="aut"><span class="mono">MO</span><span class="an">Mancur Olson<small><i>Logique de l’action collective</i>, 1965</small></span><span class="ad">Économiste américain. Dans un <b>grand groupe</b>, la contribution de chacun au <b>bien collectif</b> (une hausse de salaire, une loi) est négligeable, alors que son coût est individuel ; comme le bien profitera à tous, chacun a intérêt à être <b>passager clandestin</b> (<i>free rider</i>). D’où le paradoxe : des individus qui ont un intérêt commun peuvent ne pas agir ensemble.</span></div>' +
      '<div data-chain="s5-olson"></div>' +
      '<div class="def"><b>Bien collectif</b> — bien ou avantage dont personne ne peut être exclu une fois qu’il est obtenu (la hausse de salaire négociée vaut pour tous les salariés de la branche, syndiqués ou non).</div>' +
      '<h3>1. Les incitations sélectives</h3><p>Olson lui-même donne la solution : réserver des <b>avantages</b> aux seuls membres (incitations positives) ou <b>sanctionner</b> ceux qui ne participent pas (incitations négatives).</p>' +
      '<div class="ex"><p>Positives : conseil juridique, assurances, formations, informations réservées aux adhérents d’un syndicat ou d’une association. Négatives : dans certains pays, le <i>closed shop</i> imposait d’être syndiqué pour être embauché ; la pression des collègues pendant une grève joue un rôle comparable.</p></div>' +
      '<h3>2. Les rétributions symboliques</h3><div class="aut"><span class="mono">DG</span><span class="an">Daniel Gaxie<small>« Économie des partis et rétributions du militantisme », 1977</small></span><span class="ad">Les militants sont aussi « payés » autrement qu’en argent : <b>reconnaissance</b>, sentiment d’utilité, amitiés et sociabilité, estime de soi, compétences acquises (prendre la parole, organiser), parfois une carrière (élu, permanent).</span></div>' +
      '<p>L’économiste Albert Hirschman (<i>Bonheur privé, action publique</i>, 1982) ajoute que l’engagement peut être une fin en soi : on s’engage aussi pour le plaisir d’agir ensemble, et l’on alterne des phases d’engagement public et de repli sur la vie privée au gré des déceptions.</p>' +
      '<h3>3. La structure des opportunités politiques</h3><div class="def"><b>Structure des opportunités politiques</b> — ensemble des caractéristiques du contexte politique qui rendent une mobilisation plus ou moins susceptible de réussir : ouverture des institutions, alliés au pouvoir, divisions entre élites, tolérance ou répression. La notion a été proposée par Peter Eisinger (1973) et développée notamment par Sidney Tarrow.</div>' +
      '<div class="ex"><p>Les défenseurs du mariage pour les couples de même sexe se sont mobilisés pendant des années ; la loi est adoptée le 17 mai 2013, après l’élection en 2012 d’une majorité qui l’avait inscrite à son programme. À l’inverse, les opposants (la « Manif pour tous ») ont rassemblé des foules très importantes sans obtenir le retrait du texte : une majorité stable leur fermait l’opportunité.</p></div>' +
      '<div data-chain="s5-depasser"></div>' +
      '<div class="plus"><p>Albert Hirschman (<i>Exit, Voice and Loyalty</i>, 1970) propose aussi trois réactions face à un mécontentement : la <b>défection</b> (partir, changer de fournisseur), la <b>prise de parole</b> (protester) et la <b>loyauté</b> (rester fidèle). La prise de parole est d’autant plus probable que la défection est difficile.</p></div>' },

    { id: "s5-3", t: "Qui s’engage ? Les variables sociodémographiques", h:
      '<p class="lede">L’engagement n’est pas réparti au hasard. Le programme cite quatre variables.</p>' +
      '<h3>1. La catégorie socioprofessionnelle</h3><div data-graph="s5-pcs"></div><p>Lecture : en 2022, 19,7 % des ouvriers inscrits (de 25 ans ou plus) n’ont voté à aucun tour, contre 6,8 % des cadres (Insee). Les cadres et les professions intermédiaires sont aussi surreprésentés parmi les adhérents de partis et les dirigeants d’associations. Le taux de syndicalisation est plus élevé chez les salariés de la fonction publique et les catégories intermédiaires que chez les ouvriers et employés du privé, notamment dans les petites entreprises.</p>' +
      '<h3>2. Le diplôme</h3><div data-graph="s5-dipl"></div><div data-chain="s5-diplome"></div><p>Le sociologue Daniel Gaxie parle de « <b>cens caché</b> » (1978) : alors que le suffrage censitaire a disparu, le sentiment d’incompétence politique tient encore une partie des moins diplômés à l’écart. L’effet est le plus fort chez les jeunes : en 2022, 50,3 % des 18-29 ans sans diplôme et non étudiants n’ont voté à aucun tour, contre 17,0 % des jeunes diplômés du supérieur (Insee).</p>' +
      '<h3>3. L’âge et la génération</h3><div data-graph="s5-age"></div><p>Lecture : en 2022, 16,7 % des inscrits de 18 à 24 ans ont voté à tous les tours, contre 53,7 % des 70-74 ans. Deux effets se combinent :</p><ul><li><b>Effet d’âge</b> (cycle de vie) : les jeunes sont moins « installés » (études, mobilité, pas encore de logement ni d’emploi stable, parfois mal inscrits) ; la participation augmente avec l’insertion, puis baisse au grand âge (55,3 % d’abstention systématique chez les 90 ans ou plus).</li><li><b>Effet de génération</b> : à âge égal, les générations récentes votent moins régulièrement. En 2002, 32,5 % des 18-24 ans votaient à tous les tours ; en 2022, 16,7 %. Le politiste Vincent Tiberj y voit moins un désintérêt qu’une citoyenneté plus <b>distante et critique</b> : le vote n’est plus vécu comme un devoir, mais il est complété par d’autres formes d’engagement (pétitions, manifestations, causes).</li></ul>' +
      '<h3>4. Le sexe</h3><p>Depuis les années 1980, femmes et hommes votent à peu près autant. Mais les femmes restent sous-représentées dans le militantisme partisan et les fonctions électives, malgré la loi sur la <b>parité</b> du 6 juin 2000. Leur engagement prend plus souvent d’autres formes :</p>' +
      '<div class="ex src"><p>Selon le baromètre jeunesse 2019 de l’INJEP (document repris dans un sujet officiel du bac 2026), 49 % des jeunes femmes déclarent avoir signé une pétition ou défendu une cause sur internet, contre 40 % des jeunes hommes ; les jeunes hommes sont plus présents dans l’engagement bénévole (43 % contre 31 %), l’adhésion à un parti (7 % contre 3 %) et les manifestations, grèves ou occupations (22 % contre 12 %).</p></div>' +
      '<div class="cle"><p>Ces variables se cumulent : un jeune ouvrier sans diplôme s’abstient bien plus souvent qu’une cadre retraitée. Elles agissent à travers la <b>socialisation politique</b> (famille, école, travail) et le sentiment de <b>compétence</b>.</p></div>' },

    { id: "s5-4", t: "Les transformations de l’action collective : objets, acteurs, répertoires", h:
      '<div class="def"><b>Action collective</b> — action concertée d’un groupe d’individus pour défendre des intérêts communs ou une cause.</div>' +
      '<h3>1. Des objets qui se diversifient</h3><p><b>Les conflits du travail</b> (salaires, emplois, conditions de travail, retraites) ont longtemps structuré l’action collective autour du mouvement ouvrier. Ils restent importants : en 2023, l’intersyndicale a organisé plusieurs mois de grèves et de manifestations contre la réforme des retraites, adoptée après l’usage de l’article 49.3 le 16 mars 2023.</p>' +
      '<div data-chain="s5-nms"></div>' +
      '<p>Le sociologue <b>Alain Touraine</b> parle dès les années 1970 de <b>nouveaux mouvements sociaux</b> : écologistes, féministes, régionalistes, qui défendent des valeurs et des modes de vie plus que des intérêts matériels. Le politiste Ronald Inglehart (<i>The Silent Revolution</i>, 1977) explique leur essor par la diffusion de valeurs <b>post-matérialistes</b> chez des générations qui ont grandi dans l’abondance.</p>' +
      '<p><b>Les luttes minoritaires</b> sont menées par des groupes dominés ou discriminés pour obtenir l’égalité des droits et la reconnaissance : Manifeste des 343 pour le droit à l’avortement (1971), loi Veil (17 janvier 1975) ; Marche pour l’égalité et contre le racisme (1983) ; mobilisations homosexuelles, d’Act Up dans la lutte contre le sida au PaCS (1999) puis au mariage pour tous (2013) ; mouvement #MeToo (2017) contre les violences sexuelles.</p>' +
      '<h3>2. Des acteurs plus nombreux</h3><div class="tbl"><table><thead><tr><th>Acteur</th><th>Ce qu’il fait</th><th>Évolution</th></tr></thead><tbody>' +
      '<tr><td><b>Partis politiques</b></td><td>Conquérir et exercer le pouvoir, sélectionner les candidats, proposer des programmes</td><td>Adhérents en baisse, méfiance ; essor de mouvements plus souples autour d’un leader</td></tr>' +
      '<tr><td><b>Syndicats</b></td><td>Défendre les intérêts des salariés, négocier, organiser les grèves</td><td>Environ 10 % de syndiqués ; représentativité fondée depuis 2008 sur les élections professionnelles</td></tr>' +
      '<tr><td><b>Associations</b></td><td>Défendre une cause, rendre des services, alerter, agir en justice</td><td>Très nombreuses, actives sur l’environnement, la santé, les droits</td></tr>' +
      '<tr><td><b>Groupements</b> (groupes d’intérêt, collectifs, coordinations)</td><td>Peser sur une décision précise (lobbying), mobiliser sans structure permanente</td><td>Collectifs éphémères, coordinations de grévistes, mobilisations nées sur les réseaux sociaux</td></tr></tbody></table></div>' +
      '<div class="ex"><p>Le mouvement des « gilets jaunes », lancé le 17 novembre 2018 contre la hausse de la taxe sur les carburants, s’est organisé sur les réseaux sociaux et sur les ronds-points, sans parti ni syndicat à sa tête et en refusant souvent les porte-parole.</p></div>' +
      '<h3>3. Des répertoires d’action qui changent</h3><div class="aut"><span class="mono">CT</span><span class="an">Charles Tilly<small><i>La France conteste, de 1600 à nos jours</i>, 1986</small></span><span class="ad">Le <b>répertoire d’action collective</b> est l’ensemble limité des moyens d’action qu’un groupe connaît et juge légitimes à une époque. En France, vers le milieu du XIX<sup>e</sup> siècle, on passe d’un répertoire <b>local et patronné</b> (charivaris, émeutes de subsistance) à un répertoire <b>national et autonome</b> (grève, manifestation, réunion publique, pétition).</span></div>' +
      '<p>Depuis la fin du XX<sup>e</sup> siècle, ce répertoire s’enrichit :</p><ul><li><b>Médiatisation et expertise</b> : actions spectaculaires pensées pour les caméras, contre-expertises scientifiques.</li><li><b>Numérique</b> : pétitions en ligne, mots-dièses, mobilisation rapide. La pétition « L’Affaire du siècle », lancée en décembre 2018, a réuni plus de deux millions de signatures.</li><li><b>Action en justice</b> : dans la même affaire, le tribunal administratif de Paris a reconnu le 3 février 2021 la carence fautive de l’État en matière climatique.</li><li><b>Occupation et désobéissance civile</b> : la « zone à défendre » de Notre-Dame-des-Landes (projet d’aéroport abandonné le 17 janvier 2018), actions non violentes d’Extinction Rebellion.</li><li><b>Échelle européenne et mondiale</b> : marches pour le climat coordonnées dans de nombreux pays en 2019.</li></ul>' +
      '<div class="attn"><p>Les anciens moyens ne disparaissent pas : la grève et la manifestation restent centrales (mobilisations de 2023). On dit plutôt que le répertoire s’<b>élargit</b> et que les militants combinent les formes.</p></div>' }
  ],
  pieges: [
    { f: "« L’abstention montre que les Français se désintéressent de la politique. »", v: "L’abstention est souvent <b>intermittente</b> (47,2 % de votants intermittents en 2022) et coexiste avec d’autres formes d’engagement (pétitions, associations, manifestations)." },
    { f: "« Le paradoxe d’Olson dit que les gens sont égoïstes. »", v: "Il dit qu’un individu <b>rationnel</b> peut avoir intérêt à ne pas participer à une action dont il profitera de toute façon. C’est un raisonnement sur les coûts et les gains, valable surtout dans les grands groupes." },
    { f: "Confondre incitations sélectives et rétributions symboliques.", v: "Les incitations sélectives sont des <b>avantages matériels ou sanctions</b> réservés aux membres (Olson). Les rétributions symboliques sont des gains <b>non matériels</b> : reconnaissance, liens, estime de soi (Gaxie)." },
    { f: "« Les jeunes votent moins parce qu’ils sont jeunes. »", v: "Il y a un <b>effet d’âge</b> (insertion progressive), mais aussi un <b>effet de génération</b> : à âge égal, les 18-24 ans de 2022 votent moins systématiquement que ceux de 2002 (16,7 % contre 32,5 %)." },
    { f: "« Les nouveaux mouvements sociaux ont remplacé les conflits du travail. »", v: "Les conflits du travail persistent (retraites 2023) ; les objets se sont <b>diversifiés</b>, ils n’ont pas été remplacés." },
    { f: "« La structure des opportunités politiques, c’est la motivation des militants. »", v: "C’est le <b>contexte politique</b> extérieur (institutions ouvertes ou fermées, alliés, divisions des élites, répression)." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Engagement politique</b> : vote, militantisme (partis, syndicats), engagement associatif, consommation engagée (boycott, buycott).</li>' +
    '<li><b>Paradoxe de l’action collective</b> (Olson, 1965) : le bien collectif profite à tous ; le coût est individuel ; d’où le passager clandestin.</li>' +
    '<li><b>Dépassement</b> : incitations sélectives positives et négatives (Olson) ; rétributions symboliques (Gaxie, 1977) ; structure des opportunités politiques (Eisinger 1973, Tarrow) ; plaisir de l’engagement (Hirschman).</li>' +
    '<li><b>Variables</b> : PCS, diplôme (« cens caché », Gaxie 1978), âge (effet d’âge) et génération (citoyenneté distante, Tiberj), sexe (parité 2000).</li>' +
    '<li><b>Objets</b> : conflits du travail, nouveaux mouvements sociaux (Touraine, post-matérialisme d’Inglehart), luttes minoritaires (droits des femmes, antiracisme, LGBT).</li>' +
    '<li><b>Acteurs</b> : partis, syndicats, associations, groupements (lobbies, collectifs, coordinations).</li>' +
    '<li><b>Répertoires</b> (Tilly, 1986) : du local-patronné au national-autonome (grève, manifestation, pétition) ; aujourd’hui numérique, justice, occupation, désobéissance civile, échelle mondiale.</li></ul>' +
    '<h3>Chiffres à citer (Insee, participation 2022)</h3><ul><li>Vote systématique 37,0 %, intermittent 47,2 %, abstention systématique 15,8 % (12,2 % en 2002).</li><li>Abstention systématique : sans diplôme 30,4 %, diplômés du supérieur 9,5 % ; ouvriers 19,7 %, cadres 6,8 %.</li><li>Vote systématique : 18-24 ans 16,7 %, 70-74 ans 53,7 %.</li></ul>',
  chainesFiche: ["s5-olson", "s5-depasser", "s5-diplome", "s5-nms"],
  quiz: [
    { q: "Laquelle de ces actions est une forme de consommation engagée ?", c: ["Refuser d’acheter les produits d’une entreprise qui ferme des usines", "Voter aux élections européennes", "Adhérer à un syndicat", "Faire grève"], r: 0, e: "Le boycott (et le buycott) utilise ses achats comme moyen politique.", s: "s5-1" },
    { q: "En 2022, d’après l’Insee, quelle part des inscrits a voté à certains tours seulement (vote intermittent) ?", c: ["47,2 %", "15,8 %", "37,0 %", "73,7 %"], r: 0, e: "Vote intermittent 47,2 %, vote systématique 37,0 %, abstention systématique 15,8 %.", s: "s5-1" },
    { q: "Le militantisme désigne…", c: ["un engagement durable et actif au service d’une organisation ou d’une cause", "le simple fait de voter", "l’achat de produits équitables", "l’abstention volontaire"], r: 0, e: "Tracter, organiser, représenter : c’est un investissement durable dans un parti, un syndicat ou une association.", s: "s5-1" },
    { q: "Selon Olson, pourquoi un individu rationnel peut-il ne pas participer à une grève qui défend ses intérêts ?", c: ["Parce qu’il profitera du résultat même sans participer, alors que participer lui coûte", "Parce qu’il est mal informé", "Parce que la grève est interdite", "Parce qu’il n’a pas de conscience de classe"], r: 0, e: "C’est le comportement de passager clandestin face à un bien collectif.", s: "s5-2" },
    { q: "Un syndicat qui offre un conseil juridique gratuit à ses seuls adhérents utilise…", c: ["une incitation sélective positive", "une rétribution symbolique", "la structure des opportunités politiques", "une incitation sélective négative"], r: 0, e: "Avantage matériel réservé aux membres : incitation sélective positive (Olson).", s: "s5-2" },
    { q: "Pour Daniel Gaxie, les rétributions symboliques du militantisme sont par exemple…", c: ["la reconnaissance, les amitiés, l’estime de soi", "les primes versées par le parti", "les réductions d’impôt", "les sanctions contre les non-grévistes"], r: 0, e: "Gains non matériels de l’engagement (Gaxie, 1977).", s: "s5-2" },
    { q: "La structure des opportunités politiques désigne…", c: ["le contexte politique qui rend une mobilisation plus ou moins susceptible de réussir", "la liste des partis autorisés", "les motivations personnelles des militants", "les ressources financières d’une association"], r: 0, e: "Ouverture des institutions, alliés, divisions des élites, répression (Eisinger, Tarrow).", s: "s5-2" },
    { q: "En 2022, l’abstention systématique concerne…", c: ["30,4 % des inscrits sans diplôme et 9,5 % des diplômés du supérieur", "9,5 % des inscrits sans diplôme et 30,4 % des diplômés", "autant les diplômés que les non-diplômés", "50 % des cadres"], r: 0, e: "Insee Première n° 1929 : le diplôme est l’une des variables les plus discriminantes.", s: "s5-3" },
    { q: "Le « cens caché » (Gaxie, 1978) désigne…", c: ["l’exclusion de fait des moins diplômés, qui se sentent incompétents en politique", "le vote réservé aux propriétaires", "le secret du vote", "les dons cachés aux partis"], r: 0, e: "Le suffrage est universel en droit, mais le sentiment de compétence politique est inégalement réparti.", s: "s5-3" },
    { q: "En 2002, 32,5 % des 18-24 ans votaient à tous les tours ; en 2022, 16,7 %. Cette baisse illustre surtout…", c: ["un effet de génération", "un effet d’âge", "un effet du diplôme uniquement", "une erreur de mesure"], r: 0, e: "On compare des personnes du même âge à vingt ans d’écart : ce sont les générations qui diffèrent.", s: "s5-3" },
    { q: "Lequel est un exemple de lutte minoritaire ?", c: ["La mobilisation pour l’ouverture du mariage aux couples de même sexe", "Une grève pour les salaires dans une usine", "Le vote à la présidentielle", "Le lobbying d’une fédération d’entreprises"], r: 0, e: "Les luttes minoritaires visent l’égalité des droits et la reconnaissance de groupes dominés ou discriminés.", s: "s5-4" },
    { q: "Pour Alain Touraine, les « nouveaux mouvements sociaux » se distinguent par…", c: ["des enjeux culturels et de mode de vie plus que matériels (écologie, féminisme)", "la défense exclusive des salaires", "leur organisation en partis de masse", "leur refus de toute manifestation"], r: 0, e: "Ils défendent des valeurs (qualité de vie, autonomie, environnement) ; Inglehart parle de valeurs post-matérialistes.", s: "s5-4" },
    { q: "Selon Charles Tilly, le répertoire d’action collective est…", c: ["l’ensemble limité des moyens d’action connus et jugés légitimes à une époque", "la liste des adhérents d’un syndicat", "le programme d’un parti", "le calendrier des élections"], r: 0, e: "Au milieu du XIXe siècle, la France passe d’un répertoire local et patronné à un répertoire national et autonome.", s: "s5-4" },
    { q: "Laquelle est une forme récente du répertoire d’action ?", c: ["L’action en justice contre l’État pour inaction climatique", "La grève", "La manifestation", "La pétition sur papier"], r: 0, e: "« L’Affaire du siècle » : tribunal administratif de Paris, 3 février 2021. Grève, manifestation et pétition appartiennent au répertoire national-autonome du XIXe siècle.", s: "s5-4" }
  ],
  cartes: [
    { r: "Engagement politique", v: "Participation à la vie publique : vote, militantisme, engagement associatif, consommation engagée, pétition, manifestation…" },
    { r: "Vote intermittent / abstention systématique", v: "Intermittent : voter à certains tours seulement (47,2 % des inscrits en 2022). Systématique : ne voter à aucun (15,8 %)." },
    { r: "Militantisme", v: "Engagement durable et actif au service d’une organisation (parti, syndicat, association) ou d’une cause." },
    { r: "Consommation engagée", v: "Usage politique des achats : boycott (refus) ou buycott (achat responsable, commerce équitable)." },
    { r: "Bien collectif", v: "Avantage dont personne ne peut être exclu une fois qu’il est obtenu (hausse de salaire de branche, loi)." },
    { r: "Paradoxe de l’action collective", v: "Des individus ayant un intérêt commun peuvent ne pas agir ensemble, chacun préférant laisser les autres payer le coût (Olson, 1965)." },
    { r: "Passager clandestin", v: "Individu qui profite d’un bien collectif sans contribuer à son obtention." },
    { r: "Incitations sélectives", v: "Avantages (positives) ou sanctions (négatives) réservés aux membres pour les pousser à participer (Olson)." },
    { r: "Rétributions symboliques", v: "Gains non matériels de l’engagement : reconnaissance, sociabilité, estime de soi, compétences (Gaxie, 1977)." },
    { r: "Structure des opportunités politiques", v: "Contexte politique plus ou moins favorable à une mobilisation : ouverture du pouvoir, alliés, divisions des élites, répression (Eisinger, Tarrow)." },
    { r: "Cens caché", v: "Mise à l’écart de fait des moins diplômés, qui se sentent incompétents en politique (Gaxie, 1978)." },
    { r: "Effet d’âge / effet de génération", v: "Âge : comportement lié au moment du cycle de vie. Génération : comportement propre aux personnes nées à une même époque, qui persiste avec l’âge." },
    { r: "Nouveaux mouvements sociaux", v: "Mobilisations sur des enjeux culturels et de mode de vie (écologie, féminisme, minorités) depuis les années 1970 (Touraine ; post-matérialisme d’Inglehart)." },
    { r: "Luttes minoritaires", v: "Mobilisations de groupes dominés ou discriminés pour l’égalité des droits et la reconnaissance (droits des femmes, antiracisme, LGBT)." },
    { r: "Répertoire d’action collective (Tilly)", v: "Ensemble des moyens d’action disponibles à une époque. XIXe siècle : passage du local-patronné au national-autonome (grève, manifestation, pétition)." },
    { r: "Groupe d’intérêt", v: "Organisation qui cherche à influencer les décisions publiques sans viser le pouvoir (lobbying, expertise, campagnes)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice inventé pour le site, données Insee", t: "Lire et comparer des données de participation", enonce:
      '<p>En 2022, selon l’Insee, 30,4 % des inscrits sans diplôme et 9,5 % des diplômés du supérieur n’ont voté à aucun tour ; 28,8 % et 43,7 % ont voté à tous les tours. En 2002, l’abstention systématique était de 16,6 % et 5,9 %.</p><ol><li>Calcule l’écart en points et le rapport entre les deux groupes pour l’abstention systématique en 2022.</li><li>Calcule le taux de variation de l’abstention systématique des inscrits sans diplôme entre 2002 et 2022.</li><li>Rédige une phrase qui résume l’évolution.</li></ol>',
      corrige: '<ol><li>30,4 − 9,5 = 20,9 points ; 30,4 ÷ 9,5 ≈ 3,2 : l’abstention systématique est 3,2 fois plus fréquente chez les inscrits sans diplôme.</li><li>(30,4 − 16,6) ÷ 16,6 × 100 ≈ +83 % : elle a presque doublé (coefficient multiplicateur 1,83).</li><li>« Selon l’Insee, entre 2002 et 2022, l’abstention systématique a progressé dans tous les groupes, mais beaucoup plus chez les inscrits sans diplôme : l’écart avec les diplômés du supérieur passe de 10,7 à 20,9 points. »</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet officiel : bac 2026, sujet 26-SESJ2G11 (épreuve composée), partie 1 · corrigé du site", officiel: true, t: "Vous présenterez deux formes d’engagement politique.", enonce: "<p>4 points (session 2026). Sans document.</p>",
      methode: "<p>Définis l’engagement politique ; pour chaque forme : définition, exemple précis et chiffré, éventuellement une évolution. Deux paragraphes distincts suffisent.</p>",
      corrige: '<div class="copie"><p>L’engagement politique désigne l’ensemble des formes de participation des individus à la vie publique, pour choisir leurs représentants, défendre une cause ou peser sur les décisions. Il prend des formes variées, dont le vote et la consommation engagée.</p><p>Le vote est la forme d’engagement la plus répandue : il permet aux citoyens de désigner leurs représentants. Il devient plus intermittent : selon l’Insee, en 2022, 37,0 % des inscrits ont voté à tous les tours de la présidentielle et des législatives, 47,2 % à certains tours seulement et 15,8 % à aucun. Beaucoup d’électeurs choisissent donc les élections qui leur paraissent décisives.</p><p>La consommation engagée consiste à utiliser ses achats comme un moyen d’action politique : boycotter les produits d’une entreprise dont on désapprouve les pratiques, ou au contraire privilégier des produits jugés responsables (buycott), comme ceux du commerce équitable. En 2001, par exemple, un appel au boycott des produits Danone a répondu à l’annonce de fermetures d’usines. Cette forme d’engagement, individuelle en apparence, est souvent organisée par des associations.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice inventé pour le site, document Insee", t: "Le vote systématique selon l’âge en 2002 et 2022", enonce:
      '<p>Document : le graphique « Le vote systématique selon l’âge, 2002 et 2022 » du <a href="#s5:s5-3">cours</a> (Insee).</p><ol><li>Comparez le vote systématique des 18-24 ans et des 70-74 ans en 2022. (2 points)</li><li>À l’aide du document et de vos connaissances, montrez que la participation électorale dépend de l’âge et de la génération. (4 points)</li></ol>',
      corrige: '<ol><li>Selon l’Insee, en 2022, 16,7 % des inscrits de 18 à 24 ans ont voté à tous les tours de la présidentielle et des législatives, contre 53,7 % des 70-74 ans : 37 points d’écart, soit une proportion environ 3,2 fois plus élevée chez les 70-74 ans.</li><li>La participation dépend d’abord de l’<b>âge</b> : le vote systématique augmente de 18 à 79 ans puis chute au grand âge (21,4 % à 90 ans ou plus). C’est un effet de cycle de vie : les jeunes, peu installés (études, mobilité, emploi instable, inscription parfois à un ancien domicile), votent par intermittence ; l’insertion professionnelle et familiale renforce l’intégration et la participation ; la santé et l’isolement la réduisent ensuite. Elle dépend aussi de la <b>génération</b> : à âge égal, la participation régulière a reculé, surtout chez les jeunes (32,5 % des 18-24 ans votaient à tous les tours en 2002, 16,7 % en 2022). Les générations récentes vivent moins le vote comme un devoir et pratiquent un vote intermittent, tout en recourant à d’autres formes d’engagement (pétitions, manifestations, associations) : une citoyenneté plus distante et critique.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet officiel : bac 2026, sujet 26-SESJ2AG1 (épreuve composée), partie 3 · corrigé du site", officiel: true, t: "Vous montrerez que l’engagement politique dépend de variables sociodémographiques.", enonce: '<p>Le dossier officiel comprenait : un tableau de l’Insee sur les comportements de vote en 2022 selon l’âge, un extrait du baromètre jeunesse 2019 de l’INJEP sur les formes d’engagement des jeunes femmes et des jeunes hommes, un graphique de la Dares sur la syndicalisation selon le secteur et la catégorie (2013 et 2019). Utilise les données du cours.</p>',
      corrige: '<p><b>Introduction.</b> L’engagement politique regroupe vote, militantisme, engagement associatif, consommation engagée. Il n’est pas réparti au hasard : il varie selon l’âge et la génération, le sexe, le diplôme et la catégorie sociale.</p><p><b>I. L’âge et la génération.</b> Vote systématique 2022 : 17,3 % des 18-29 ans, 37,2 % des 30-64 ans, 47,7 % des 65 ans ou plus ; abstention systématique 23,7 % chez les 18-29 ans (document 1). Effet d’âge (installation) et effet de génération (citoyenneté distante, vote intermittent ; 32,5 % des 18-24 ans votaient à tous les tours en 2002).</p><p><b>II. Le sexe.</b> Vote désormais comparable ; mais formes différentes : jeunes femmes plus engagées en ligne (49 % contre 40 %), jeunes hommes plus présents dans les partis (7 % contre 3 %), le bénévolat et les manifestations (document 2) ; sous-représentation des femmes dans le militantisme partisan malgré la parité (2000).</p><p><b>III. Le diplôme et la catégorie sociale.</b> Abstention systématique 30,4 % sans diplôme, 9,5 % diplômés du supérieur ; ouvriers 19,7 %, cadres 6,8 % (Insee, 2022). Cens caché (Gaxie). Syndicalisation plus forte chez les cadres et professions intermédiaires du public que chez les ouvriers et employés du privé (document 3).</p><p><b>Conclusion.</b> Ces variables se cumulent et agissent par la socialisation et le sentiment de compétence politique.</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Comment expliquer que les individus s’engagent malgré le paradoxe de l’action collective ?", enonce: "<p>Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> Olson montre qu’un individu rationnel a intérêt à être passager clandestin. Pourtant, les grèves, les manifestations, les associations et les partis existent. Quels mécanismes rendent l’engagement rationnel, désirable ou possible ?</p><p><b>I. Un paradoxe réel</b><br>A. Bien collectif, coût individuel, contribution négligeable dans un grand groupe (Olson, 1965).<br>B. Des signes : environ 10 % de syndiqués, adhérents des partis en baisse, abstention systématique de 15,8 % en 2022.</p><p><b>II. Des gains individuels qui rendent l’engagement rationnel</b><br>A. Incitations sélectives positives (services aux adhérents) et négatives (closed shop, pression des pairs).<br>B. Rétributions symboliques (Gaxie) : reconnaissance, liens, compétences, carrière.<br>C. Le plaisir de l’action et les cycles d’engagement (Hirschman).</p><p><b>III. Un contexte et des ressources qui rendent l’engagement possible</b><br>A. Structure des opportunités politiques (mariage pour tous, 2013 ; Notre-Dame-des-Landes, 2018).<br>B. Ressources inégales : diplôme, PCS, âge (cens caché).<br>C. De nouveaux répertoires qui abaissent le coût de l’engagement (pétitions en ligne, réseaux sociaux).</p>' }
  ]
};

AUTEURS.push(
  { ch: "s5", n: "Mancur Olson", d: "1932-1998", th: "Paradoxe de l’action collective, passager clandestin, incitations sélectives", l: "<i>The Logic of Collective Action</i> (1965) : dans un grand groupe, chacun a intérêt à laisser les autres agir pour un bien collectif ; les <b>incitations sélectives</b> permettent de dépasser ce paradoxe." },
  { ch: "s5", n: "Daniel Gaxie", d: "né en 1947", th: "Rétributions symboliques du militantisme ; le « cens caché »", l: "« Économie des partis et rétributions du militantisme » (1977) : reconnaissance, sociabilité, estime de soi. <i>Le Cens caché</i> (1978) : les moins diplômés se sentent incompétents en politique." },
  { ch: "s5", n: "Albert O. Hirschman", d: "1915-2012", th: "Défection, prise de parole, loyauté ; cycles d’engagement", l: "<i>Exit, Voice and Loyalty</i> (1970) : partir, protester ou rester fidèle. <i>Bonheur privé, action publique</i> (1982) : on alterne engagement public et repli privé au gré des déceptions." },
  { ch: "s5", n: "Peter Eisinger et Sidney Tarrow", d: "1973 ; années 1980-1990", th: "Structure des opportunités politiques", l: "Le succès d’une mobilisation dépend du contexte politique : ouverture des institutions, alliés, divisions des élites, répression." },
  { ch: "s5", n: "Charles Tilly", d: "1929-2008", th: "Répertoires d’action collective", l: "<i>La France conteste, de 1600 à nos jours</i> (1986) : vers le milieu du XIXe siècle, passage d’un répertoire local et patronné à un répertoire national et autonome (grève, manifestation, pétition)." },
  { ch: "s5", n: "Alain Touraine", d: "1925-2023", th: "Nouveaux mouvements sociaux", l: "Depuis les années 1970, des mouvements (écologistes, féministes, régionalistes) portent des enjeux culturels et de mode de vie plus que des revendications matérielles." },
  { ch: "s5", n: "Ronald Inglehart", d: "1934-2021", th: "Valeurs post-matérialistes", l: "<i>The Silent Revolution</i> (1977) : les générations élevées dans l’abondance privilégient autonomie, qualité de vie et environnement." },
  { ch: "s5", n: "Vincent Tiberj", d: "politiste", th: "Citoyenneté distante et critique des nouvelles générations", l: "Les générations récentes votent moins par devoir et de façon intermittente, mais pratiquent d’autres formes d’engagement : moins de déférence, plus de critique." }
);

ANIMS["s5-olson"] = {
  t: "Le paradoxe de l’action collective, joué par douze salariés",
  h: 320,
  src: "Situation fictive construite pour le site, pour illustrer Olson (1965), Gaxie (1977) et la structure des opportunités politiques.",
  etapes: [
    { l: "Douze salariés d’une entreprise. Si au moins huit font grève, la direction accordera une hausse de salaire… à tous, grévistes ou non : c’est un bien collectif.", d: 4.5 },
    { l: "Chacun calcule : faire grève me coûte une journée de salaire ; ma présence change peu le résultat ; et si la grève réussit, j’aurai la hausse de toute façon.", d: 5 },
    { l: "Chacun a donc intérêt à laisser les autres agir : il devient passager clandestin. Personne ne bouge, et la hausse que tous souhaitaient n’est pas obtenue. C’est le paradoxe d’Olson (1965).", d: 5 },
    { l: "Incitations sélectives : le syndicat réserve à ses adhérents un conseil juridique et une caisse de grève qui compense la journée perdue. Trois salariés s’engagent.", d: 4.5 },
    { l: "Rétributions symboliques (Gaxie) : reconnaissance des collègues, amitiés, fierté, compétences acquises. Trois autres rejoignent le mouvement.", d: 4.5 },
    { l: "Structure des opportunités politiques : la direction est divisée et la presse s’intéresse au conflit ; la grève a des chances de réussir. Deux de plus : huit grévistes, la hausse est obtenue, pour les douze.", d: 5.5 }
  ],
  rendu: function (A, i, p) {
    var s = "", n = 12, seuil = 8;
    var etats = [0, 0, 0, 3, 6, 8];
    var avant = i === 0 ? 0 : etats[i - 1], apres = etats[i];
    var engages = avant + (apres - avant) * A.s(p, 0.2, 0.8);
    var couleurs = function (k) { return k < 3 ? "canard" : k < 6 ? "moutarde" : "vert"; };
    s += A.boite(20, 12, 320, 34, "Bien collectif : une hausse de salaire pour les 12, si au moins 8 font grève", { k: "neutre", t: 12 });
    for (var k = 0; k < n; k++) {
      var col = k % 6, lig = Math.floor(k / 6), x = 40 + col * 56, y = 128 + lig * 76;
      var q = Math.max(0, Math.min(1, engages - k));
      var c = q > 0.5 ? couleurs(k) : "gris";
      s += A.cercle(x, y - 26, 9, { f: c, op: q > 0.5 ? 1 : 0.55 }) + A.r(x - 10, y - 15, 20, 26, { f: c, r: 6, op: q > 0.5 ? 1 : 0.55 });
      if (q > 0.5) s += A.r(x - 16, y + 14, 32, 14, { f: "carte", s: c, r: 7 }) + A.t(x, y + 25, "grève", { t: 9.5, g: true, a: "middle", c: c });
      if (i === 5 && p > 0.85) s += A.t(x + 11, y - 34, "+", { t: 15, g: true, c: "vert" });
    }
    if (i === 1) {
      var qb = A.s(p, 0.05, 0.4);
      s += A.r(110, 52, 236, 46, { f: "carte", s: "corail", r: 10, op: qb });
      s += A.t(228, 70, "Coût certain : −1 jour de salaire", { t: 11, a: "middle", c: "corail", op: qb });
      s += A.t(228, 88, "Gain : le même, gréviste ou non", { t: 11, a: "middle", c: "corail", op: A.s(p, 0.35, 0.7) });
      s += A.fl(110, 80, 50, 98, { c: "corail", p: qb, sw: 1.5 });
    }
    var jy = 268;
    s += A.jauge(20, jy, 320, engages, n, { c: engages >= seuil ? "vert" : "corail", l: "Grévistes", val: Math.round(engages) + " / 12" });
    s += '<line x1="' + (20 + 320 * seuil / n) + '" x2="' + (20 + 320 * seuil / n) + '" y1="' + (jy - 6) + '" y2="' + (jy + 16) + '" style="stroke:var(--encre);stroke-width:2"/>';
    s += A.t(20 + 320 * seuil / n, jy + 30, "seuil : 8", { t: 10.5, a: "middle", c: "gris" });
    if (i === 2) s += A.boite(90, 56, 180, 36, "Personne ne bouge : échec", { k: "frein", g: true, op: A.s(p, 0.4, 0.8) });
    if (i === 3) s += A.t(180, 70, "Avantages réservés aux adhérents", { t: 12, g: true, a: "middle", c: "canard", op: A.s(p, 0, 0.3) });
    if (i === 4) s += A.t(180, 70, "Reconnaissance, liens, fierté", { t: 12, g: true, a: "middle", c: "moutarde", op: A.s(p, 0, 0.3) });
    if (i === 5) s += A.boite(20, 12, 320, 34, "La grève réussit : hausse de salaire pour les 12, grévistes ou non", { k: "effet", g: true, t: 12, op: A.s(p, 0.75, 0.95) }) + A.t(180, 70, "Contexte favorable : élites divisées, presse attentive", { t: 12, g: true, a: "middle", c: "vert", op: A.s(p, 0, 0.3) });
    return s;
  }
};
