// Découpage du short « ordrehggsp » (format « ordre » : HGGSP, remets dans l'ordre), modèle A, habillage archives.
// a: [passage, mot] ; av : avance sur le mot (négative : après le mot). À chaque manche : la pioche montre les quatre
// événements un par un pendant que la voix les lit (plan propre « pioche »), puis le plan ordre (formats-a.js) lance le
// chrono et révèle le bon ordre et les dates. Étapes de pioche : [repère, intitulé, image, dessin, cadrage vertical].
window.PLAN = S => S.plans([
  // o1 « HGGSP : remets 12 événements dans l'ordre. »
  { a: ['o1', 0], av: .2, type: 'collage', imgs: ['apollo', 'westphalie', 'abousimbel'], t: 'HGGSP|REMETS DANS L’ORDRE', couleur: true, ch: 0 },
  { a: ['o1', 'événements'], type: 'melange', t: '12 ÉVÉNEMENTS|DU PROGRAMME', choc: true },
  // o2 « 3 manches. Compte tes points. »
  { a: ['o2', 0], type: 'score', t: 'COMPTE|TES POINTS' },
  // m1 / m1b / v1 : l'espace
  { a: ['m1', 0], type: 'manche', n: 1, t: 'L’ESPACE', fond: 'iss', ch: 1 },
  { a: ['m1b', 0], type: 'pioche', sur: 'MANCHE 1 · L’ESPACE', etapes: [
    [['m1b', 'apollo'], 'Apollo 11', 'apollo', null, .3],
    [['m1b', 'premier'], 'Le premier Chinois|dans l’espace', 'yangliwei', null, .3],
    [['m1b', 'spoutnik'], 'Spoutnik', 'spoutnik', null, .3],
    [['m1b', 'station'], 'La Station spatiale|internationale', 'iss', null, .5]] },
  { a: ['m1b', -1], av: -.3, type: 'ordre', sur: 'MANCHE 1 · L’ESPACE', cartes: [
    { t: 'Apollo 11', d: 'juillet 1969' }, { t: 'Le premier Chinois|dans l’espace', d: 'oct. 2003' },
    { t: 'Spoutnik', d: 'oct. 1957' }, { t: 'La Station spatiale|internationale', d: 'nov. 1998, 1er module' }],
    ordre: [2, 0, 3, 1], chrono: ['m1b', -1], rep: ['v1', 0], expl: 'Des deux Grands|aux nouveaux acteurs' },
  // x1 « Spoutnik, premier satellite artificiel : un choc pour les États-Unis. »
  { a: ['x1', 0], type: 'photo', img: 'spoutnik', t: 'PREMIER SATELLITE|ARTIFICIEL', sous: 'réplique de Spoutnik 1, URSS, 4 octobre 1957', de: [1.0, .85, .2], vers: [1.12, .85, .25] },
  { a: ['x1', 'choc'], type: 'mot', t: 'UN CHOC POUR|LES ÉTATS-UNIS', choc: true },
  // m2 / m2b / v2 : faire la paix
  { a: ['m2', 0], type: 'collage', imgs: ['versailles', 'oslo', 'westphalie'], t: 'MANCHE 2|FAIRE LA PAIX', couleur: true, ch: 2 },
  { a: ['m2b', 0], type: 'pioche', sur: 'MANCHE 2 · FAIRE LA PAIX', etapes: [
    [['m2b', 'accords'], 'Les accords d’Oslo', 'oslo', null, .3],
    [['m2b', 'charte'], 'La charte|de l’ONU', null, 'onu'],
    [['m2b', 'traités'], 'Les traités|de Westphalie', 'westphalie', null, .5],
    [['m2b', 'versailles'], 'Le traité|de Versailles', 'versailles', null, .8]] },
  { a: ['m2b', 'trois'], type: 'ordre', sur: 'MANCHE 2 · FAIRE LA PAIX', cartes: [
    { t: 'Les accords d’Oslo', d: '13 sept. 1993' }, { t: 'La charte de l’ONU', d: '26 juin 1945' },
    { t: 'Les traités|de Westphalie', d: '1648' }, { t: 'Le traité|de Versailles', d: '28 juin 1919' }],
    ordre: [2, 3, 1, 0], chrono: ['m2b', 'trois'], rep: ['v2', 0], expl: 'Des traités entre États|à la sécurité collective' },
  // x2 « Westphalie met fin à la guerre de Trente Ans. »
  { a: ['x2', 0], type: 'photo', img: 'westphalie', t: 'FIN DE LA GUERRE|DE TRENTE ANS', sous: 'la paix de Münster, 1648, peinte par Gerard ter Borch', de: [1.05, .5, .5], vers: [1.2, .55, .5] },
  // x2b « Et en 1993, Rabin et Arafat se serrent la main à la Maison-Blanche. »
  { a: ['x2b', 0], type: 'date', t: '1993', de: 1945, sous: 'MAISON-BLANCHE' },
  { a: ['x2b', 'rabin'], type: 'mot', img: 'oslo', t: 'RABIN ET ARAFAT|LA POIGNÉE DE MAIN' },
  // m3 / m3b / v3 : patrimoine et climat
  { a: ['m3', 0], type: 'manche', n: 3, t: 'PATRIMOINE|ET CLIMAT', fond: 'abousimbel', ch: 3 },
  { a: ['m3b', 0], type: 'pioche', sur: 'MANCHE 3 · PATRIMOINE ET CLIMAT', etapes: [
    [['m3b', "l'accord"], 'L’accord de Paris', 'cop21', null, .5],
    [['m3b', 'sommet'], 'Le sommet de la Terre|de Rio', null, 'terre'],
    [['m3b', 'convention'], 'La convention du|patrimoine mondial', 'abousimbel', null, .5],
    [['m3b', 'protocole'], 'Le protocole|de Kyoto', 'kyoto', null, .5]] },
  { a: ['m3b', -1], av: -.3, type: 'ordre', sur: 'MANCHE 3 · PATRIMOINE ET CLIMAT', cartes: [
    { t: 'L’accord de Paris', d: 'déc. 2015' }, { t: 'Le sommet de la Terre|de Rio', d: 'juin 1992' },
    { t: 'La convention du|patrimoine mondial', d: 'nov. 1972' }, { t: 'Le protocole|de Kyoto', d: 'déc. 1997' }],
    ordre: [2, 1, 3, 0], chrono: ['m3b', -1], rep: ['v3', 0] },
  // x3 « Cette convention naît d'un sauvetage : les temples d'Abou Simbel, découpés en blocs. »
  { a: ['x3', 0], type: 'tampon', t: 'UN SAUVETAGE' },
  { a: ['x3', 'temples'], type: 'photo', img: 'chantier', nb: true, t: 'ABOU SIMBEL|SAUVÉ BLOC PAR BLOC', sous: 'les temples remontés plus haut, années 1960', de: [1.05, .5, .5], vers: [1.2, .5, .45] },
  // x3b « À Paris, presque tous les pays visent un réchauffement bien en dessous de 2 degrés. »
  { a: ['x3b', 0], type: 'thermometre', t: 'BIEN EN DESSOUS|DE 2 DEGRÉS', sous: 'l’accord de Paris, COP21, 2015', choc: true },
  // e1 « Combien de manches réussies ? Dis-le en commentaire. »
  { a: ['e1', 0], type: 'score', fin: true, t: 'COMBIEN DE|MANCHES ?', ch: 4 },
  { a: ['e1', 'dis-le'], type: 'commentaire', t: 'DIS-LE EN|COMMENTAIRE' },
  // e2 « Plus de défis sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'versailles' },
]);
window.CHAPITRES = ['ACCROCHE', 'L’ESPACE', 'FAIRE LA PAIX', 'PATRIMOINE ET CLIMAT', 'TON SCORE'];
window.IMAGES = {
  apollo: 'img/hggsp-apollo11.jpg',            // Buzz Aldrin sur la Lune, Apollo 11, 20 juillet 1969, photo Neil Armstrong, NASA, domaine public (Wikimedia Commons)
  yangliwei: 'img/hggsp-yangliwei.jpg',        // Yang Liwei à son retour, Shenzhou 5, 16 octobre 2003, China News Service, CC BY 3.0 (Wikimedia Commons)
  spoutnik: 'img/hggsp-spoutnik.jpg',          // réplique de Spoutnik 1, World Museum Liverpool, photo Rept0n1x, CC BY-SA 3.0 (Wikimedia Commons)
  iss: 'img/hggsp-iss.jpg',                    // la Station spatiale internationale vue d'Atlantis, STS-135, juillet 2011, NASA, domaine public (Wikimedia Commons)
  westphalie: 'img/hggsp-westphalie.jpg',      // Gerard ter Borch, La ratification du traité de Münster, 1648, domaine public (Wikimedia Commons)
  versailles: 'img/hggsp-versailles.jpg',      // William Orpen, La signature de la paix dans la galerie des Glaces, 28 juin 1919, domaine public (Wikimedia Commons)
  oslo: 'img/hggsp-oslo.jpg',                  // Rabin, Clinton et Arafat à la Maison-Blanche, 13 septembre 1993, Vince Musi / The White House, domaine public (Wikimedia Commons)
  abousimbel: 'img/hggsp-abousimbel.jpg',      // le grand temple de Ramsès II, Abou Simbel, 2022, Diego Delso, CC BY-SA 4.0 (Wikimedia Commons)
  chantier: 'img/hggsp-abousimbel-1966.jpg',   // chantier du déplacement des temples d'Abou Simbel, années 1960, Anefo (Nationaal Archief), CC0 (Wikimedia Commons)
  kyoto: 'img/hggsp-kyoto.jpg',                // Centre international de conférences de Kyoto, 2023, 663highland, CC BY-SA 4.0 (Wikimedia Commons)
  cop21: 'img/hggsp-cop21.jpg',                // site de la COP21, Le Bourget, 2015, Jmdigne, CC BY-SA 4.0 (Wikimedia Commons)
};
window.MUSIQUE = 'funk_agressif2';   // musique imposée pour ce short
window.THEME = 'archives';           // habillage imposé pour ce short
