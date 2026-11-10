window.HLP = { ENTREES: [] };
(function (H) {
  var s = ' fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"';
  H.ICONES = {
    lune: '<path d="M19 14.6A7.6 7.6 0 1 1 9.4 5a6.1 6.1 0 0 0 9.6 9.6z"' + s + '/><path d="M17.5 4.5v2M16.5 5.5h2"' + s + '/>',
    plume: '<path d="M20 3.5c-6.5.6-11 5.3-12.6 12.8L6 20.5"' + s + '/><path d="M8.2 13.4c3.8.4 7.4-1.7 9.3-5.8M10.4 9.4c2.2.2 4.2-.4 6-1.6"' + s + '/>',
    loupe: '<circle cx="10.5" cy="10.5" r="6"' + s + '/><path d="M15 15l5 5M7.6 9h5.8M7.6 11.8h4"' + s + '/>',
    guillemets: '<path d="M10 7c-3 1-4.5 3.4-4.5 6.5v3.5H10v-4H7.6M19 7c-3 1-4.5 3.4-4.5 6.5v3.5H19v-4h-2.4"' + s + '/>',
    sablier: '<path d="M6.5 3.5h11M6.5 20.5h11M8 3.5c0 5 8 5.6 8 8.5s-8 3.5-8 8.5M16 3.5c0 5-8 5.6-8 8.5s8 3.5 8 8.5"' + s + '/>',
    constellation: '<circle cx="5" cy="17" r="1.4"' + s + '/><circle cx="10" cy="7" r="1.4"' + s + '/><circle cx="15.5" cy="13" r="1.4"' + s + '/><circle cx="19.5" cy="5" r="1.4"' + s + '/><path d="M6 15.8l3.4-7.5M11.2 8l3.4 3.9M16.5 11.8l2.4-5.5"' + s + '/>',
    cible: '<circle cx="12" cy="12" r="8"' + s + '/><circle cx="12" cy="12" r="4.4"' + s + '/><circle cx="12" cy="12" r="1.2"' + s + '/>',
    livres: '<path d="M4 4.5h4v15H4zM8 4.5h4v15H8z"' + s + '/><path d="M13 5.6l3.7-1 4 14.6-3.8 1z"' + s + '/>',
    eclipse: '<circle cx="12" cy="12" r="8"' + s + '/><path d="M12 4a8 8 0 0 1 0 16a5.5 5.5 0 0 0 0-16z" fill="currentColor" opacity=".35"/>',
    imprimer: '<path d="M7 9V3.5h10V9M7 17H4.5v-7.5h15V17H17M7 14h10v6.5H7z"' + s + '/>'
  };
  H.LOGO = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="2" width="36" height="36" rx="2" fill="#f4ead3" stroke="#9c2a1b" stroke-width="1.5"/>' +
    '<rect x="5.5" y="5.5" width="29" height="29" fill="none" stroke="#9c2a1b" stroke-width=".7"/>' +
    '<path d="M9 25.5c3.8-1.9 7.4-1.9 11 0c3.6-1.9 7.2-1.9 11 0v5.5c-3.8-1.9-7.4-1.9-11 0c-3.6-1.9-7.2-1.9-11 0z" fill="none" stroke="#2b1c11" stroke-width="1.2" stroke-linejoin="round"/>' +
    '<path d="M20 25.5v5.5" stroke="#2b1c11" stroke-width="1"/><path d="M28.5 8.5c-4.2 3-6.6 8-7.2 14.5c2.3-4.2 5.6-8.4 7.2-14.5z" fill="#2b1c11"/><path d="M21.3 23l-1 2.2" stroke="#2b1c11" stroke-width="1"/>' +
    '<circle cx="12" cy="11" r="1.1" fill="#9c2a1b"/><circle cx="15" cy="15" r=".8" fill="#9c2a1b"/></svg>';
  /* Ornements gravés : fleuron (séparateur), cul-de-lampe (fin de page), coin de cadre, paraphe à la plume, emblème du frontispice. */
  var g = ' fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"';
  H.FLEURON = '<svg viewBox="0 0 86 22" aria-hidden="true"><g' + g + '><path d="M43 3.5c3.2 3 3.2 12 0 15c-3.2-3-3.2-12 0-15z" fill="currentColor"/>' +
    '<path d="M37.5 11c-6-7.5-14.5-7.5-18.5-2c-2.8 4 1.2 8 5 6c3-1.8 1.2-5-1-4.2M48.5 11c6-7.5 14.5-7.5 18.5-2c2.8 4-1.2 8-5 6c-3-1.8-1.2-5 1-4.2"/>' +
    '<path d="M37.5 11c-4 4-9 6-14.5 5M48.5 11c4 4 9 6 14.5 5M19 9.5H5M67 9.5h14"/></g><circle cx="3" cy="9.5" r="1.5" fill="currentColor"/><circle cx="83" cy="9.5" r="1.5" fill="currentColor"/></svg>';
  H.CUL = '<svg class="cul" viewBox="0 0 120 46"><g' + g + '><path d="M8 4h104M20 10h80M33 16h54"/><path d="M60 18c-10 4-12 12-6 16c4 3 9-1 6-5M60 18c10 4 12 12 6 16c-4 3-9-1-6-5"/>' +
    '<path d="M60 34v7M45 16c-6 4-12 3-14 0M75 16c6 4 12 3 14 0"/></g><circle cx="60" cy="43" r="1.8" fill="currentColor"/><path d="M57 25l3-5 3 5-3 4z" fill="currentColor"/></svg>';
  H.COIN = '<g' + g + '><path d="M2 28V2h26"/><path d="M5 25V5h20" stroke-width=".7"/><path d="M5 5c7 0 11 4 11 11c0 3-2 5-4 5s-3-2-2-3.5"/><circle cx="16" cy="16" r="1.3" fill="currentColor" stroke="none"/></g>';
  H.PARAPHE = '<svg class="paraphe" viewBox="0 0 320 34" aria-hidden="true"><path class="trait" d="M8 22 C 60 2, 90 34, 140 18 S 230 4, 270 20 S 300 26, 312 14"/>' +
    '<path class="trait" d="M128 27c10 5 26 5 36 0"/><path class="plume" d="M0 0l16-15c3-3 7-1 5 3L5 3z"/></svg>';
  H.EMBLEME = '<svg class="embleme" viewBox="0 0 150 126" aria-hidden="true"><g' + g + '>' +
    '<path class="grave" d="M18 96c19-9 38-9 57 0c19-9 38-9 57 0v18c-19-9-38-9-57 0c-19-9-38-9-57 0z"/><path class="grave" d="M75 96v18M26 100c14-5 30-5 42 0M26 106c14-5 30-5 42 0M82 100c14-5 30-5 42 0M82 106c14-5 30-5 42 0" stroke-width=".7"/>' +
    '<path class="grave" d="M98 94L127 24"/><path class="grave" d="M127 24c-14 7-22 26-25 48c11-13 20-29 25-48z"/><path d="M109 46l8-4M106 56l9-4M104 66l8-4" stroke-width=".6"/>' +
    '<path class="grave" d="M36 92V56h13v36"/><path d="M33 92h19" /><path d="M42.5 56v-4" stroke-width=".8"/>' +
    '<path d="M78 12a11 11 0 1 0 11 15a9 9 0 0 1-11-15z" fill="currentColor" stroke="none" opacity=".85"/>' +
    '<path d="M28 40l-5-4M57 40l5-4M42.5 30v-6" stroke-width=".6"/></g>' +
    '<path class="flamme" d="M42.5 34c5.5 6.5 5.5 13 0 17c-5.5-4-5.5-10.5 0-17z" fill="var(--or)"/><path class="flamme" d="M42.5 41c2.3 3 2.3 6 0 8c-2.3-2-2.3-5 0-8z" fill="var(--cuivre)"/></svg>';
  function chiffre(n) {
    return '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22.5" fill="none" stroke="currentColor" stroke-width="1"/><circle cx="24" cy="24" r="18.5" fill="none" stroke="currentColor" stroke-width=".8" stroke-dasharray="1 2.6"/>' +
      '<text x="24" y="30.5" text-anchor="middle" font-size="' + (n.length > 2 ? 15 : 18) + '" fill="currentColor" style="font-family:var(--titre)">' + n + '</text></svg>';
  }
  H.CHIFFRES = { I: chiffre("I"), II: chiffre("II"), III: chiffre("III") };
  H.ACCUEIL_INTRO = "La spécialité HLP fait travailler ensemble un professeur de lettres et un professeur de philosophie sur les mêmes questions. En Terminale, le premier semestre s’intitule « La recherche de soi » et couvre la période qui va du romantisme au XX<sup>e</sup> siècle ; le second, « L’Humanité en question », porte sur le monde contemporain. Ce site rédige à fond les trois entrées du premier semestre : pour chacune, un cours, des textes clés du domaine public analysés, un sujet type bac corrigé, un QCM, des cartes mémoire et une fiche à imprimer.";
  H.ACCUEIL_BAS = '<div class="carte lecture" style="margin-top:26px"><p class="surtitre">À savoir pour 2027</p><p style="margin:.2em 0">Une nouvelle note de service (11 septembre 2026) définit l’épreuve à partir de la session 2027 : 4 heures, un texte, une question d’<b>interprétation</b> et un <b>essai</b>, notés chacun sur 10, sur deux copies séparées. Comme depuis 2024, tout le programme de Terminale peut tomber : prépare les six entrées. <a href="#epreuve">Tout savoir sur l’épreuve →</a></p></div>';
  H.PIED = "Ex libris · HLP Terminale · Contenu original rédigé à partir du programme officiel (BO spécial n° 8 du 25 juillet 2019) et de la note de service du 11 septembre 2026. Extraits d’œuvres du domaine public d’après Wikisource ; œuvres protégées seulement résumées ou citées brièvement. Fonctionne hors connexion.";
  H.TITRES = { accueil: "Accueil", s2: "Semestre 2", epreuve: "L’épreuve", atelier: "Atelier de lecture", qui: "Qui a écrit ?", frise: "Frise", notions: "Tableau des notions", entrainement: "Entraînement", ressources: "Ressources" };
  H.PAGES_IDX = [
    { t: "Format de l’épreuve écrite (session 2027)", c: "L’épreuve", h: "#epreuve", g: "ep-format", x: "4 heures coefficient 16 deux questions interprétation essai 10 points copies séparées note de service 2026 programme limitatif" },
    { t: "Méthode de l’interprétation", c: "L’épreuve", h: "#epreuve", g: "ep-interp", x: "interprétation littéraire philosophique méthode introduction paraphrase procédés" },
    { t: "Méthode de l’essai", c: "L’épreuve", h: "#epreuve", g: "ep-essai", x: "essai littéraire philosophique problématique plan dialectique références" },
    { t: "Copie modèle commentée : Condorcet, bac 2025", c: "L’épreuve", h: "#epreuve", g: "ep-copie", x: "Condorcet pitié exercer l’âme des enfants copie commentée annale 2025 métropole" },
    { t: "Annales : sujets tombés de 2022 à 2026", c: "L’épreuve", h: "#epreuve", g: "ep-annales", x: "annales sujets bac métropole Rousseau Nietzsche Aron Mirbeau Hugo Ruy Blas Albert-Birot" },
    { t: "Le Grand oral", c: "L’épreuve", h: "#epreuve", g: "ep-go", x: "grand oral 20 minutes coefficient 8 deux questions" },
    { t: "Atelier de lecture", c: "Méthode", h: "#atelier", x: "surlignage procédés mouvements Lamartine Baudelaire Kant Rimbaud" },
    { t: "Ressources : programme, annales, textes", c: "Ressources", h: "#ressources", x: "eduscol programme wikisource gallica annales youtube manuels" }
  ];

  H.S2_CHAPO = "Le second semestre porte sur la période contemporaine (XX<sup>e</sup>-XXI<sup>e</sup> siècles). Les cours seront rédigés plus tard ; voici dès maintenant les questions que pose le programme officiel, les œuvres qu’il cite et les sujets déjà tombés.";
  H.S2 = [
    { num: "I", titre: "Création, continuités et ruptures", accroche: "Avant-gardes, manifestes, « fin de l’art » : y a-t-il des ruptures radicales ?",
      resume: "Le XX<sup>e</sup> siècle est une ère de ruptures : expressionnisme, futurisme, Dada, surréalisme multiplient les manifestes ; la philosophie parle d’une « crise de la rationalité » ; radio et cinéma transforment la culture. Mais l’ancien subsiste à côté du nouveau, en accord ou en tension.",
      questions: ["Y a-t-il des ruptures radicales en art, en littérature ou dans la pensée ?", "L’ancien ne subsiste-t-il pas, en accord ou en tension, à côté du nouveau ou à travers lui ?", "D’autres époques ont-elles connu des querelles et débats comparables ?"],
      oeuvres: "Marinetti, <i>Manifeste du futurisme</i> (1908) ; Apollinaire, <i>Alcools</i> (1913) ; Breton, <i>Manifeste du surréalisme</i> (1924) ; Césaire, <i>Cahier d’un retour au pays natal</i> (1947) ; Ionesco, <i>La Cantatrice chauve</i> (1950) ; Sarraute, <i>L’Ère du soupçon</i> (1956) ; Beckett, <i>Fin de partie</i> (1957) ; Foucault, « Qu’est-ce qu’un auteur ? » (1969)." },
    { num: "II", titre: "Histoire et violence", accroche: "Guerres, totalitarismes, témoignages : dire l’inhumain.",
      resume: "Destructions et massacres sans précédent, en particulier lors des deux guerres mondiales ; peuples dominés qui revendiquent leur dignité. La littérature témoigne, dénonce, ou tente d’exprimer la violence jusque dans son inhumanité ; la philosophie se demande si la violence est irréductible.",
      questions: ["La violence dont toutes les sociétés humaines ont fait l’expérience est-elle irréductible ?", "L’histoire universelle donne-t-elle les signes d’une marche vers des relations pacifiées ?", "Si la violence précède le droit, quel droit pourra la limiter ?", "Qu’appelle-t-on « violence » ? Toutes les violences sont-elles comparables ?"],
      oeuvres: "Kant, <i>Idée d’une histoire universelle d’un point de vue cosmopolitique</i> (1784) ; Remarque, <i>À l’Ouest, rien de nouveau</i> (1929) ; Céline, <i>Voyage au bout de la nuit</i> (1932) ; Camus, <i>La Peste</i> (1947) ; Antelme, <i>L’Espèce humaine</i> (1947) ; Arendt, <i>Les Origines du totalitarisme</i> ; Perec, <i>W ou le souvenir d’enfance</i> (1975 selon l’édition originale ; 1974 dans la bibliographie officielle) ; Semprun, <i>L’Écriture ou la vie</i> (1994).",
      annales: "2022 (métropole) : Paul Ricœur, <i>Histoire et vérité</i> ; Louis Calaferte, <i>C’est la guerre</i>. 2024 (métropole) : Aragon, <i>Le Roman inachevé</i> — « Quelles violences ce poème dit-il ? » / « Peut-on perdre son humanité ? ». 2025 (métropole) : Wisława Szymborska — « Que dit ce poème des victimes de la guerre ? » / « Peut-on conserver son humanité dans des circonstances qui risquent de nous en dépouiller ? »" },
    { num: "III", titre: "L’humain et ses limites", accroche: "Technique, écologie, humain « augmenté » : jusqu’où peut-on aller ?",
      resume: "« Jusqu’où peut-on aller ? » : la technique semble promettre un pouvoir sans limite (numérique, génétique, intelligence artificielle), mais engendre dépendances, destructions et déséquilibres écologiques. Littérature et philosophie interrogent la finitude humaine et ce que peut signifier aujourd’hui l’idée d’humanité.",
      questions: ["Quelle sorte de bonheur et quelle durée de vie pour un homme entièrement « réparé », voire « augmenté » ?", "Comment penser l’équilibre entre exploitation et conservation de la nature ?", "Le nouvel univers numérique et ses réseaux créent-ils une nouvelle sociabilité ?"],
      oeuvres: "Valéry, « Le Cimetière marin » (1920) ; Huxley, <i>Le Meilleur des mondes</i> (1932) ; Saint-Exupéry, <i>Terre des hommes</i> (1939) ; Barjavel, <i>Ravage</i> (1943) ; Orwell, <i>1984</i> (1949) ; Lévi-Strauss, <i>Tristes tropiques</i> (1955) ; Arendt, <i>Condition de l’homme moderne</i> (1958) ; Jonas, <i>Le Principe responsabilité</i> (1979).",
      annales: "2026 (métropole, jour 1) : Jean Giono, <i>Triomphe de la vie</i> (1941) — « Quel regard Jean Giono porte-t-il sur le travail de la machine ? » / « Dans quelle mesure les machines échappent-elles à l’humain ? ». Sujet zéro n° 4 (Éduscol) : Arendt, <i>Condition de l’homme moderne</i>." }
  ];

  H.FRISE = [
    { nom: "Les Lumières", dates: "vers 1715-1789", def: "la raison critique, et la découverte du sentiment", evts: [
      ["1755", "Rousseau, <i>Discours sur l’origine de l’inégalité</i> : la pitié, sentiment naturel.", "e2"],
      ["1761", "Rousseau, <i>Julie ou la Nouvelle Héloïse</i>, roman par lettres, immense succès.", "e2"],
      ["1762", "Rousseau, <i>Émile ou De l’éducation</i>, condamné et brûlé.", "e1"],
      ["1774", "Goethe, <i>Les Souffrances du jeune Werther</i>.", "e2"],
      ["1782", "Publication posthume des <i>Confessions</i> (livres I à VI) et des <i>Rêveries</i>.", "e3"],
      ["1784", "Kant, <i>Qu’est-ce que les Lumières ?</i> : « Sapere aude ».", "e1"],
      ["1789", "Prise de la Bastille (14 juillet) ; Déclaration des droits de l’homme et du citoyen (26 août).", "hist"]] },
    { nom: "Révolution, Empire, premiers romantiques", dates: "1789-1820", def: "l’histoire bouleverse les vies", evts: [
      ["1790", "Kant, <i>Critique de la faculté de juger</i> : le beau et le sublime.", "e2"],
      ["1791", "Condorcet, <i>Cinq mémoires sur l’instruction publique</i>.", "e1"],
      ["1793-1794", "La Terreur.", "hist"],
      ["1795-1796", "Goethe, <i>Les Années d’apprentissage de Wilhelm Meister</i>, modèle du roman de formation.", "e1"],
      ["1802", "Chateaubriand, <i>René</i> : le mal du siècle.", "e2"],
      ["1804-1815", "Premier Empire ; abdication de Napoléon en 1814 et 1815.", "hist"],
      ["1813", "Mme de Staël, <i>De l’Allemagne</i>, publié à Londres (l’édition de 1810 avait été détruite par la police impériale) : le romantisme allemand découvert en France.", "e2"]] },
    { nom: "Le romantisme", dates: "1820-1850", def: "le moi, la nature, l’histoire", evts: [
      ["1820", "Lamartine, <i>Méditations poétiques</i> (« Le Lac »).", "e2"],
      ["1827", "Hugo, préface de <i>Cromwell</i> : manifeste du drame romantique.", "e2"],
      ["1830", "Bataille d’<i>Hernani</i> (février) ; Stendhal, <i>Le Rouge et le Noir</i> ; révolution de Juillet.", "e1"],
      ["1833", "Loi Guizot sur l’instruction primaire.", "e1"],
      ["1834", "Musset, <i>Lorenzaccio</i>.", "e3"],
      ["1836", "Musset, <i>La Confession d’un enfant du siècle</i>.", "e2"],
      ["1848", "Révolution de février ; suffrage universel masculin ; abolition de l’esclavage.", "hist"],
      ["1849-1850", "Chateaubriand, <i>Mémoires d’outre-tombe</i> (posthumes).", "e3"]] },
    { nom: "Réalisme, Parnasse, symbolisme", dates: "1850-1900", def: "regarder le réel, déchiffrer les correspondances", evts: [
      ["1851", "Coup d’État de Louis-Napoléon Bonaparte ; Hugo part en exil.", "hist"],
      ["1854-1855", "Nerval, <i>Les Chimères</i> ; <i>Aurélia</i>.", "e3"],
      ["1856", "Hugo, <i>Les Contemplations</i> : « les Mémoires d’une âme ».", "e3"],
      ["1857", "Baudelaire, <i>Les Fleurs du mal</i> ; Flaubert, <i>Madame Bovary</i> : deux procès.", "e2"],
      ["1863", "Baudelaire, <i>Le Peintre de la vie moderne</i>.", "e2"],
      ["1869", "Flaubert, <i>L’Éducation sentimentale</i>.", "e1"],
      ["1871", "Commune de Paris (mars-mai) ; Rimbaud, lettres du voyant (13 et 15 mai).", "e3"],
      ["1878", "Vallès, <i>L’Enfant</i>.", "e1"],
      ["1881-1882", "Lois Ferry : école primaire gratuite, obligatoire, laïque.", "e1"],
      ["1882", "Nietzsche, <i>Le Gai Savoir</i>.", "e3"],
      ["1886", "Stevenson, <i>Jekyll et Hyde</i> ; Moréas, manifeste du symbolisme (<i>Le Figaro</i>, 18 septembre).", "e3"],
      ["1887", "Maupassant, <i>Le Horla</i> (version définitive).", "e3"],
      ["1889", "Bergson, <i>Essai sur les données immédiates de la conscience</i>.", "e2"]] },
    { nom: "Les modernités", dates: "1900-1950", def: "l’inconscient, le temps, le soupçon", evts: [
      ["1900", "Freud, <i>L’Interprétation du rêve</i> ; Colette, <i>Claudine à l’école</i>.", "e3"],
      ["1913", "Proust, <i>Du côté de chez Swann</i>.", "e2"],
      ["1914-1918", "Première Guerre mondiale.", "hist"],
      ["1915", "Kafka, <i>La Métamorphose</i>.", "e3"],
      ["1923", "Freud, <i>Le Moi et le Ça</i>.", "e3"],
      ["1924", "Breton, <i>Manifeste du surréalisme</i> ; lettres de Rivière à Artaud.", "e3"],
      ["1926", "Pirandello, <i>Un, personne et cent mille</i>.", "e3"],
      ["1927", "Proust, <i>Le Temps retrouvé</i> (posthume).", "e2"],
      ["1939-1945", "Seconde Guerre mondiale.", "hist"],
      ["1943-1944", "Sartre, <i>L’Être et le Néant</i> ; <i>Huis clos</i>.", "e3"],
      ["1949", "Beauvoir, <i>Le Deuxième Sexe</i>.", "e1"]] }
  ];

  H.NOTIONS = [
    { n: "Éducation / instruction", e: ["e1"], d: "L’éducation forme la personne entière ; l’instruction transmet des savoirs et leurs preuves.", dist: "Condorcet confie l’instruction à l’État et l’éducation morale et religieuse aux familles.", a: "Condorcet, Ferry, Durkheim" },
    { n: "Autorité", e: ["e1"], d: "Pouvoir reconnu comme légitime, obéi sans contrainte ni persuasion.", dist: "≠ force (contraindre) ≠ persuasion (convaincre par arguments).", a: "Arendt, Kant" },
    { n: "Tradition / transmission", e: ["e1"], d: "Ce qui est transmis d’une génération à l’autre et reçu comme ayant autorité.", dist: "Transmettre n’est pas répéter : Arendt fait de l’héritage la condition du nouveau.", a: "Arendt, Nietzsche" },
    { n: "Émancipation", e: ["e1"], d: "Sortie d’une tutelle (familiale, sociale, politique, intellectuelle).", dist: "Émancipation (acte, processus) ≠ liberté (état ou capacité).", a: "Kant, Beauvoir, Vallès" },
    { n: "Minorité / majorité", e: ["e1"], d: "Chez Kant, incapacité / capacité de penser par soi-même.", dist: "Ce n’est pas une question d’âge mais de courage.", a: "Kant (1784)" },
    { n: "Autonomie / hétéronomie", e: ["e1", "e3"], d: "Se donner sa propre loi / la recevoir d’autrui.", dist: "Autonomie ≠ indépendance : on peut obéir à une loi qu’on reconnaît comme sienne.", a: "Kant, Rousseau" },
    { n: "Nature / culture", e: ["e1"], d: "Ce qui est inné / ce qui est acquis par l’éducation et la société.", dist: "Rousseau : l’éducation doit cultiver la nature sans la défigurer.", a: "Rousseau, Kant" },
    { n: "Perfectibilité", e: ["e1"], d: "Faculté propre à l’homme de se perfectionner (et de se corrompre).", dist: "Elle rend l’éducation possible et nécessaire.", a: "Rousseau (1755)" },
    { n: "Bildungsroman", e: ["e1"], d: "Roman d’apprentissage ou de formation.", dist: "Réussi chez Goethe, ironique chez Flaubert.", a: "Goethe, Stendhal, Flaubert" },
    { n: "Sensibilité", e: ["e2"], d: "Capacité de sentir, de s’émouvoir, de juger du beau, de compatir.", dist: "Quatre sens : physique, affectif, esthétique, moral.", a: "Rousseau, Diderot, Kant" },
    { n: "Sensation / perception", e: ["e2"], d: "Impression reçue par un sens / organisation des sensations en objet.", dist: "Je sens du chaud ; je perçois un feu.", a: "Bergson, Merleau-Ponty" },
    { n: "Émotion / sentiment / passion", e: ["e2"], d: "Trouble vif et bref / état affectif durable / inclination exclusive.", dist: "La passion est « subie » (du latin <i>pati</i>).", a: "Descartes, Rousseau" },
    { n: "Pitié / sympathie / empathie", e: ["e2"], d: "Souffrir de la souffrance d’autrui / partager ses affects / se mettre à sa place.", dist: "Pour Rousseau et Condorcet, la pitié est le principe de la moralité.", a: "Rousseau, Condorcet, Scheler" },
    { n: "Lyrisme", e: ["e2", "e3"], d: "Expression des sentiments personnels d’un « je », musicalité.", dist: "Lyrisme personnel (Lamartine) / lyrisme universel (Hugo) / critique du lyrisme (Rimbaud).", a: "Lamartine, Hugo, Musset" },
    { n: "Mal du siècle / spleen", e: ["e2"], d: "Mélancolie romantique / ennui oppressant chez Baudelaire.", dist: "Le mal du siècle a des causes historiques (Musset) ; le spleen s’oppose à l’Idéal.", a: "Chateaubriand, Musset, Baudelaire" },
    { n: "Beau / sublime / agréable", e: ["e2"], d: "Harmonie de la forme / ce qui nous dépasse / ce qui plaît aux sens.", dist: "Le jugement de beau prétend à l’accord de tous, l’agréable non.", a: "Burke, Kant" },
    { n: "Synesthésie, correspondances", e: ["e2"], d: "Association de sensations de sens différents ; liens entre visible et invisible.", dist: "Correspondances horizontales (entre sens) et verticales (vers un sens caché).", a: "Baudelaire, Rimbaud" },
    { n: "Durée", e: ["e2", "e3"], d: "Temps vécu, continu et qualitatif.", dist: "≠ temps mesuré, découpé comme de l’espace.", a: "Bergson (1889)" },
    { n: "Mémoire involontaire", e: ["e2"], d: "Retour spontané du passé déclenché par une sensation.", dist: "≠ mémoire volontaire, effort de l’intelligence.", a: "Proust" },
    { n: "Moi / sujet / personne / individu", e: ["e3"], d: "Ce que je suis pour moi / celui qui pense et agit / l’être moral / l’être singulier.", dist: "<i>Persona</i> : le masque de l’acteur.", a: "Descartes, Pascal, Locke" },
    { n: "Conscience", e: ["e3"], d: "Connaissance immédiate que l’esprit a de lui-même et de ses états.", dist: "Conscience spontanée / réfléchie ; conscience morale (juger le bien et le mal).", a: "Descartes, Bergson" },
    { n: "Identité personnelle", e: ["e3"], d: "Ce qui fait que je reste le même à travers le temps.", dist: "Identité numérique (un seul) / qualitative (semblable).", a: "Locke, Hume, Ricœur" },
    { n: "Inconscient", e: ["e3"], d: "Contenus psychiques refoulés mais actifs.", dist: "Le moi « n’est pas maître dans sa propre maison ».", a: "Freud (1900, 1923)" },
    { n: "Sincérité / authenticité", e: ["e3"], d: "Dire ce qu’on pense / être ce qu’on vit.", dist: "On peut être sincère et se tromper sur soi (Rousseau).", a: "Rousseau, Sartre" },
    { n: "Mauvaise foi", e: ["e3"], d: "Mensonge à soi-même par lequel on fuit sa liberté.", dist: "≠ mensonge (on trompe un autre).", a: "Sartre (1943)" },
    { n: "Aliénation", e: ["e3"], d: "Fait de devenir étranger à soi-même.", dist: "Du latin <i>alienus</i>, « qui appartient à un autre ».", a: "Marx, Maupassant (<i>Le Horla</i>)" },
    { n: "Double", e: ["e3"], d: "Figure d’un autre soi-même.", dist: "Double fantastique (Maupassant), moral (Stevenson), poétique (Nerval).", a: "Stevenson, Maupassant, Nerval" },
    { n: "Autobiographie / mémoires / journal", e: ["e3"], d: "Récit rétrospectif d’une vie / vie mêlée à l’histoire / notes au jour le jour.", dist: "Pacte autobiographique : auteur = narrateur = personnage (Lejeune).", a: "Rousseau, Chateaubriand, Amiel" },
    { n: "Égotisme / égoïsme", e: ["e3"], d: "Analyse et culte de soi / préférence pour son intérêt.", dist: "Stendhal revendique l’égotisme, pas l’égoïsme.", a: "Stendhal" }
  ];

  H.QUI = [
    { c: "Tout est bien, sortant des mains de l’Auteur des choses : tout dégénère entre les mains de l’homme.", a: "Rousseau", o: "Émile ou De l’éducation, I", d: "1762", e: "Ouverture du traité : nature contre société." },
    { c: "Sapere aude, aie le courage de te servir de ta propre intelligence !", a: "Kant", o: "Qu’est-ce que les Lumières ?", d: "1784, trad. Barni", e: "La devise des Lumières." },
    { c: "L’homme ne peut devenir homme que par l’éducation.", a: "Kant", o: "Traité de pédagogie", d: "publié en 1803, trad. Barni", e: "L’éducation fait l’humanité de l’homme." },
    { c: "L’instruction publique est un devoir de la société à l’égard des citoyens.", a: "Condorcet", o: "Cinq mémoires sur l’instruction publique", d: "1791", e: "Première phrase du premier mémoire." },
    { c: "Je ne peins pas l’être. Je peins le passage", a: "Montaigne", o: "Essais, III, 2", d: "1588", e: "Orthographe modernisée." },
    { c: "Je n’ai pas plus fait mon livre que mon livre m’a fait", a: "Montaigne", o: "Essais, II, 18, « Du démentir »", d: "1580-1595", e: "L’écriture de soi construit le moi." },
    { c: "Je pense, donc je suis", a: "Descartes", o: "Discours de la méthode, IV", d: "1637", e: "La première certitude, après le doute." },
    { c: "Le moi est haïssable", a: "Pascal", o: "Pensées", d: "1670 (posthume)", e: "Le moi se fait centre de tout." },
    { c: "Si je ne vaux pas mieux, au moins je suis autre.", a: "Rousseau", o: "Les Confessions, I", d: "1782", e: "La singularité revendiquée." },
    { c: "De quoi jouit-on dans une pareille situation ? De rien d’extérieur à soi", a: "Rousseau", o: "Rêveries du promeneur solitaire, V", d: "1782", e: "Le sentiment de l’existence." },
    { c: "L’homme n’a point de port, le temps n’a point de rive ; / Il coule, et nous passons !", a: "Lamartine", o: "« Le Lac », Méditations poétiques", d: "1820", e: "La fuite du temps." },
    { c: "Les plus désespérés sont les chants les plus beaux", a: "Musset", o: "« La Nuit de mai »", d: "1835", e: "La douleur source de beauté." },
    { c: "Tout ce qui était n’est plus ; tout ce qui sera n’est pas encore.", a: "Musset", o: "La Confession d’un enfant du siècle", d: "1836", e: "Le mal du siècle." },
    { c: "Levez-vous vite, orages désirés qui devez emporter René dans les espaces d’une autre vie !", a: "Chateaubriand", o: "René", d: "1802", e: "Le héros du vague des passions." },
    { c: "Hélas ! quand je vous parle de moi, je vous parle de vous.", a: "Hugo", o: "Les Contemplations, préface", d: "1856", e: "Le lyrisme universel." },
    { c: "Je suis le ténébreux, — le veuf, — l’inconsolé", a: "Nerval", o: "« El Desdichado », Les Chimères", d: "1854", e: "Le moi aux mille masques." },
    { c: "Les parfums, les couleurs et les sons se répondent.", a: "Baudelaire", o: "« Correspondances », Les Fleurs du mal", d: "1857", e: "Les synesthésies." },
    { c: "Je suis la plaie et le couteau !", a: "Baudelaire", o: "« L’Héautontimorouménos », Les Fleurs du mal", d: "1857", e: "Bourreau et victime de soi." },
    { c: "Ce fut comme une apparition", a: "Flaubert", o: "L’Éducation sentimentale", d: "1869", e: "Frédéric voit Mme Arnoux." },
    { c: "Car Je est un autre.", a: "Rimbaud", o: "Lettre à Paul Demeny", d: "15 mai 1871", e: "Le moi n’est pas l’auteur de ses pensées." },
    { c: "C’est faux de dire : Je pense. On devrait dire : On me pense.", a: "Rimbaud", o: "Lettre à Georges Izambard", d: "13 mai 1871", e: "Deux jours avant la lettre à Demeny." },
    { c: "Tu dois devenir celui que tu es.", a: "Nietzsche", o: "Le Gai Savoir, § 270", d: "1882, trad. Albert", e: "Être soi est une tâche." },
    { c: "Je suis perdu ! Quelqu’un possède mon âme et la gouverne !", a: "Maupassant", o: "Le Horla", d: "1887", e: "La dépossession de soi." },
    { c: "Le vice a été pour moi un vêtement ; maintenant il est collé à ma peau.", a: "Musset", o: "Lorenzaccio, III, 3", d: "1834", e: "Le masque devenu visage." },
    { c: "cette essence n’était pas en moi, elle était moi", a: "Proust", o: "Du côté de chez Swann", d: "1913", e: "La madeleine." },
    { c: "Par l’art seulement, nous pouvons sortir de nous", a: "Proust", o: "Le Temps retrouvé", d: "1927", e: "Partager une vision du monde." },
    { c: "La durée toute pure est la forme que prend la succession de nos états de conscience quand notre moi se laisse vivre", a: "Bergson", o: "Essai sur les données immédiates de la conscience", d: "1889", e: "La durée vécue." },
    { c: "On ne naît pas femme : on le devient.", a: "Beauvoir", o: "Le Deuxième Sexe, t. II", d: "1949", e: "L’éducation façonne les rôles." },
    { c: "La modernité, c’est le transitoire, le fugitif, le contingent", a: "Baudelaire", o: "Le Peintre de la vie moderne", d: "1863", e: "Moitié de l’art." },
    { c: "Le rêve est une seconde vie.", a: "Nerval", o: "Aurélia", d: "1855", e: "Incipit du récit." }
  ];
})(window.HLP);
