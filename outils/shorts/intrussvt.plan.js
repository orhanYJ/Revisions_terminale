// Découpage du short « SVT : trouve l'intrus » (format « le spectateur joue », plan intrus), modèle A, habillage néon.
// a: [passage, mot] ; av : avance sur le mot. Chaque manche : un carton « manche », le plan intrus (options, chrono
// silencieux ou « Trois, deux, un », verdict), puis deux plans d'explication.
window.PLAN = S => S.plans([
  // h1 « Trouve l'intrus : 4 manches de SVT. »
  { a: ['h1', 0], av: .25, type: 'titre', ch: 0 },
  { a: ['h1', '4'], type: 'collage', imgs: ['phrygane', 'culex', 'pneumo', 'pando'], couleur: true, t: '4 MANCHES|DE SVT' },
  // h2 « Combien tu en trouves ? »
  { a: ['h2', 0], type: 'score', etape: 0 },
  // m1a « Manche 1 : la méiose. »
  { a: ['m1a', 0], type: 'manche', n: 1, t: 'LA|MÉIOSE', icone: 'chromo', ch: 1 },
  // m1b « Trois créent de la diversité génétique. Un seul n'en crée aucune. » (silence : chrono) — r1 « L'intrus : la mitose ! »
  { a: ['m1b', 0], type: 'intrus', sur: 'QUI NE CRÉE AUCUNE DIVERSITÉ ?',
    options: [{ t: 'Crossing-over', sous: 'en prophase I' }, { t: 'Mitose', sous: 'une division' },
      { t: 'Fécondation', sous: 'deux gamètes' }, { t: 'Méiose', sous: 'deux divisions' }],
    intrus: 1, chrono: ['m1b', 'aucune'], rep: ['r1', 0], expl: 'Elle copie : des cellules identiques' },
  // r1 « … Elle fait des copies conformes : des clones. »
  { a: ['r1', 'copies'], type: 'photo', img: 'pando', t: 'DES|CLONES', sous: 'Pando : toute une forêt, un seul individu', de: [1.05, .5, .5], vers: [1.25, .55, .45] },
  // e1 « Le crossing-over, lui, échange des morceaux entre chromosomes homologues. »
  { a: ['e1', 0], type: 'crossing' },
  // e1b « Et chez l'humain, la méiose permet plus de 8 millions de gamètes différents. »
  { a: ['e1b', 0], type: 'mot', t: 'CHEZ L’HUMAIN', sous: '23 paires de chromosomes' },
  { a: ['e1b', 'permet'], type: 'compteur', choc: true },
  // m2a « Manche 2 : les transferts de gènes. »
  { a: ['m2a', 0], type: 'manche', n: 2, t: 'TRANSFERTS|DE GÈNES', icone: 'bacteries', ch: 2 },
  // m2b « Trois sont horizontaux. Un seul est vertical. Trouve-le. » (silence : chrono) — r2 « Les pois de Mendel ! »
  { a: ['m2b', 0], type: 'intrus', sur: '3 HORIZONTAUX, 1 VERTICAL',
    options: [{ t: 'Pneumocoques', img: 'pneumo', sous: 'Griffith, 1928' }, { t: 'Galle du collet', img: 'galle', sous: 'Agrobacterium' },
      { t: 'Placenta', img: 'placenta', sous: 'la syncytine', nb: true }, { t: 'Pois de Mendel', img: 'pois', sous: 'croisements' }],
    intrus: 3, chrono: ['m2b', 'trouve-le'], rep: ['r2', 0], expl: 'Des parents aux descendants : vertical' },
  // r2 « … Leurs gènes passent des parents aux descendants. »
  { a: ['r2', 'leurs'], type: 'vertical' },
  // e2 « Le placenta, lui, doit sa syncytine à un gène venu d'un virus. »
  { a: ['e2', 0], type: 'photo', img: 'placenta', nb: true, t: 'LA|SYNCYTINE', sous: 'elle fait fusionner les cellules du placenta', de: [1.05, .5, .5], vers: [1.2, .45, .5] },
  { a: ['e2', 'gène'], type: 'virus' },
  // m3a « Manche 3 : les forces évolutives. »
  { a: ['m3a', 0], type: 'manche', n: 3, t: 'FORCES|ÉVOLUTIVES', img: 'darwin', ch: 3 },
  // m3b « Trois exemples de sélection naturelle. Un seul est dû au hasard. » (silence : chrono) — r3 « Les drosophiles de Buri ! »
  { a: ['m3b', 0], type: 'intrus', sur: 'LEQUEL EST DÛ AU HASARD ?',
    options: [{ t: 'Phalène', img: 'phalenes', sous: 'troncs noircis' }, { t: 'Culex', img: 'culex', sous: 'insecticides' },
      { t: 'Drosophiles', img: 'drosophile', sous: 'Buri, 1956' }, { t: 'Bactéries', img: 'antibio', sous: 'antibiotique' }],
    intrus: 2, chrono: ['m3b', 'hasard'], rep: ['r3', 0], expl: 'La dérive génétique : le hasard' },
  // r3 « … C'est la dérive génétique : le pur hasard. »
  { a: ['r3', "c'est"], type: 'derive' },
  // e3 « Chez le moustique Culex, les insecticides ont trié les porteurs d'un allèle de résistance. »
  { a: ['e3', 0], type: 'portrait', img: 'culex', t: 'CULEX', sous: 'un moustique face aux insecticides' },
  { a: ['e3', 'trié'], type: 'tri' },
  // m4 « Dernière manche, la plus dure ! Trois font partie du phénotype étendu, construit hors du corps. »
  { a: ['m4', 0], type: 'manche', n: 4, t: 'DERNIÈRE|MANCHE', icone: 'feu', choc: true, ch: 4 },
  // … c4 « Trois, deux, un. » (chrono dans la voix) — r4 « Le ver de Roscoff ! »
  { a: ['m4', 'trois'], type: 'intrus', sur: 'PHÉNOTYPE ÉTENDU : L’INTRUS ?',
    options: [{ t: 'Ver de Roscoff', img: 'roscoff', sous: 'tout vert' }, { t: 'Phrygane', img: 'phrygane', sous: 'son fourreau' },
      { t: 'Jardinier satiné', img: 'jardinier', sous: 'sa tonnelle' }, { t: 'Araignée', img: 'araignee', sous: 'sa toile' }],
    intrus: 0, chrono: ['m4', 'corps'], rep: ['r4', 0], expl: 'Pas une construction : une association' },
  // r4 « … Ses algues vivent sous sa peau : c'est une symbiose. »
  { a: ['r4', 'ses'], type: 'roscoff' },
  { a: ['r4', "c'est"], type: 'mot', img: 'roscoff', t: 'C’EST UNE|SYMBIOSE', choc: true },
  // f1 « Alors, combien d'intrus trouvés ? Dis-le en commentaire. »
  { a: ['f1', 0], type: 'score', etape: 1 },
  { a: ['f1', 'dis-le'], type: 'commentaire' },
  // f2 « Tout le cours est sur Révisions Animées. »
  { a: ['f2', 0], type: 'chaine', serie: 'SVT · Génétique et évolution', fond: 'phrygane' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA MÉIOSE', 'LES TRANSFERTS', 'LES FORCES ÉVOLUTIVES', 'DERNIÈRE MANCHE'];
window.THEME = 'neon';
window.MUSIQUE = 'automotivo';
window.IMAGES = {
  pando: '../../svt/serie/img/ch1-pando.jpg',            // Pando, peupliers faux-trembles, Utah, photo Mx. Granger, CC0
  pois: '../../svt/serie/img/ch1-pois.jpg',              // fleur de pois (Pisum sativum), photo Dyorkey, CC BY-SA 3.0
  pneumo: '../../svt/serie/img/ch2-pneumo.jpg',          // pneumocoques au microscope, coloration de Gram, Arnold Kaufman, CC0
  galle: '../../svt/serie/img/ch2-galle.jpg',            // galles du collet sur un orme, Rosser1954, CC BY-SA 4.0
  placenta: '../../svt/serie/img/ch2-placenta.jpg',      // placenta humain, face fœtale, Asturnut, CC BY-SA 3.0
  antibio: '../../svt/serie/img/ch2-antibio.jpg',        // antibiogrammes de Staphylococcus aureus, HansN., CC BY-SA 4.0
  darwin: '../../svt/serie/img/ch3-darwin.jpg',          // Charles Darwin, photographie vers 1874, domaine public
  drosophile: '../../svt/serie/img/ch3-drosophile.jpg',  // Drosophila melanogaster, photo André Karwath, CC BY-SA 2.5
  phalenes: '../../svt/serie/img/ch3-phalenes.jpg',      // phalène du bouleau, forme claire et forme noire, Olaf Leillinger, CC BY-SA 2.5
  culex: '../../svt/serie/img/ch3-culex.jpg',            // Culex pipiens, photo gbohne, CC BY-SA 2.0
  roscoff: '../../svt/serie/img/ch4-roscoff.jpg',        // vers de Roscoff, Lou Wagstaffe, iNaturalist, CC BY
  phrygane: '../../svt/serie/img/ch4-phrygane.jpg',      // larve de phrygane dans son fourreau, Jonas V., iNaturalist, CC BY
  jardinier: '../../svt/serie/img/ch4-jardinier.jpg',    // tonnelle d'un jardinier satiné mâle, Sockrosma, iNaturalist, CC BY
  araignee: '../../svt/serie/img/ch4-araignee.jpg',      // épeire diadème sur sa toile, Ben G., iNaturalist, CC BY
};
