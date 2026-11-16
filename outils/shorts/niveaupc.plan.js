// Découpage du short « Physique-chimie : niveau 1 → 10 », modèle A, habillage néon. a: [passage, mot] ; av : avance sur le mot.
// Chaque palier est un plan « niveau » (formats-a.js) qui va de la question à l'explication ; un plan dessiné ou une photo
// fait la liaison avec le palier suivant (jamais deux plans de suite du même type).
window.MUSIQUE = 'funk_agressif';
window.THEME = 'neon';
window.PLAN = S => S.plans([
  // h1 « Physique-chimie : niveau 1 à 10. » / h2 « À quel niveau tu t'arrêtes ? Pas de triche. »
  { a: ['h1', 0], av: .25, type: 'photo', img: 'orion', t: 'PHYSIQUE-CHIMIE|NIVEAU 1 À 10', legende: 'Nébuleuse d’Orion, Hubble, NASA, ESA, M. Robberto, domaine public', ch: 0 },
  { a: ['h2', 0], type: 'echelle' },
  { a: ['h2', 'pas'], type: 'triche', choc: true },
  // niveau 1 : le citron
  { a: ['q1', 0], type: 'niveau', n: 1, total: 10, img: 'citron', q: 'Le jus de citron :|acide ou basique ?', chrono: ['q1', 'basique'], rep: ['r1', 0],
    r: 'ACIDE', expl: 'pH vers 2,5 : sous 7, c’est acide', ch: 1 },
  { a: ['r1', 'bien'], type: 'echelleph' },
  // niveau 2 : la dilution
  { a: ['q2', 0], type: 'niveau', n: 2, total: 10, img: 'phmetre', q: 'Un acide fort dilué 10 fois :|que fait son pH ?', chrono: ['q2', 'son'], rep: ['r2', 0],
    r: '+ 1', expl: 'Il monte d’exactement une unité' },
  { a: ['r2', 'toujours'], type: 'dilution' },
  // t1 « Trop facile ? On passe aux dosages. »
  { a: ['t1', 0], type: 'collage', imgs: ['etalons', 'spectro', 'conducti'], t: 'TROP FACILE ?|LES DOSAGES', couleur: true, ch: 2 },
  // niveau 4 : Beer-Lambert
  { a: ['q4', 0], type: 'niveau', n: 4, total: 10, img: 'cuves', q: 'Concentration × 2 :|et l’absorbance ?', chrono: ['q4', 'son'], rep: ['r4', 0],
    r: 'ELLE DOUBLE', expl: 'Loi de Beer-Lambert : A = k × c' },
  { a: ['r4', "l'absorbance"], type: 'beer' },
  // niveau 6 : le titrage
  { a: ['q6', 0], type: 'niveau', n: 6, total: 10, img: 'burette', q: 'Courbe de titrage : comment|trouver l’équivalence ?', chrono: ['q6', 'trouves-tu'], rep: ['r6', 0],
    r: 'LES TANGENTES', expl: 'Le volume équivalent : au milieu du saut' },
  { a: ['r6', "l'équivalence"], type: 'tangentes' },
  // t2 « Là, ça pique. Place à la lumière. »
  { a: ['t2', 0], type: 'mot', t: 'LÀ, ÇA|PIQUE', choc: true, ch: 3 },
  { a: ['t2', 'place'], type: 'photo', img: 'soleil', t: 'PLACE À|LA LUMIÈRE', legende: 'Le Soleil, Solar Dynamics Observatory, NASA, domaine public' },
  // niveau 8 : l'effet photoélectrique
  { a: ['q8', 0], type: 'niveau', n: 8, total: 10, q: 'Une lampe rouge énorme|éclaire du zinc.|Des électrons sortent ?', chrono: ['q8', 'électrons'], rep: ['r8', 0],
    r: 'AUCUN', expl: 'Chaque photon rouge a trop peu d’énergie|Il faut de l’ultraviolet' },
  { a: ['r8', 'pas'], type: 'zinc' },
  // niveau 10 : la lunette
  { a: ['q10', 0], type: 'niveau', n: 10, total: 10, img: 'saturne', q: 'Lunette afocale|objectif : 2 dioptries, oculaire : 20|Grossissement ?', chrono: ['q10', 'oculaire'], rep: ['r10', 0],
    r: 'G = 10', expl: 'f′1 = 1/2 = 0,5 m · f′2 = 1/20 = 0,05 m|G = f′1 / f′2 = 50 / 5', ch: 4 },
  { a: ['r10', 'centimètres'], type: 'lunette' },
  // e1 « Alors, tu t'arrêtes où ? Dis ton niveau en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS, TU T’ARRÊTES|OÙ ?' },
  { a: ['e1', 'dis'], type: 'commentaire' },
  // e2 « Tous les chapitres sont sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Physique-chimie', fond: 'lune' },
]);
window.CHAPITRES = ['ACCROCHE', 'LES ACIDES', 'LES DOSAGES', 'LA LUMIÈRE', 'LA LUNETTE · TON NIVEAU'];
window.IMAGES = {
  orion: '../../pc/serie/img/c4-orion.jpg',          // nébuleuse d'Orion, télescope spatial Hubble, NASA, ESA, M. Robberto, domaine public
  citron: '../../pc/serie/img/c1-citron.jpg',        // citron entier et coupé, photo Ivar Leidus, CC BY-SA 4.0 (attribution obligatoire)
  phmetre: '../../pc/serie/img/c1-phmetre.jpg',      // pH-mètre de laboratoire, photo OER CampLev, CC BY-SA 4.0 (attribution obligatoire)
  etalons: '../../pc/serie/img/c2-etalons.jpg',      // gamme de solutions en fioles jaugées, photo Alina Popova, CC BY 4.0 (attribution obligatoire)
  spectro: '../../pc/serie/img/c2-spectro.jpg',      // spectrophotomètre de laboratoire, photo TimVickers, domaine public
  conducti: '../../pc/serie/img/c2-conductimetre.jpg', // conductimètre et sa sonde, photo Nuno Nogueira, CC BY-SA 2.5 (attribution obligatoire)
  cuves: '../../pc/serie/img/c2-cuves.jpg',          // cuves de spectrophotomètre, photo Retama, CC BY-SA 4.0 (attribution obligatoire)
  burette: '../../pc/serie/img/c3-burette.jpg',      // titrage à la burette, gravure de l'ouvrage d'Alessandri, 1895, domaine public
  soleil: '../../pc/serie/img/c4-soleil.jpg',        // le Soleil vu par le Solar Dynamics Observatory, NASA, domaine public
  saturne: '../../pc/serie/img/c5-saturne.jpg',      // Saturne vue par la sonde Cassini, 2004, NASA/JPL/Space Science Institute, domaine public
  lune: '../../pc/serie/img/c5-lune.jpg',            // la pleine Lune vue depuis l'espace, NASA, domaine public
};
