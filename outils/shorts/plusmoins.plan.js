// Découpage du short « Plus ou moins ? » (format « le spectateur joue », plan plusmoins), modèle A, habillage jeu.
// a: [passage, mot] ; av : avance sur le mot. Chaque duel : un carton « duel », le plan plusmoins (A donné, B caché,
// chrono silencieux ou « Trois, deux, un », B qui défile), puis un plan d'explication.
window.PLAN = S => S.plans([
  // h1 « Plus ou moins ? 4 chiffres fous, tirés de tes cours de Terminale. »
  { a: ['h1', 0], av: .25, type: 'titre', ch: 0 },
  { a: ['h1', '4'], type: 'collage', imgs: ['drosophiles', 'wallstreet', 'lune', 'mer'], couleur: true, t: '4 CHIFFRES|FOUS' },
  // h2 « Compte tes bonnes réponses. »
  { a: ['h2', 0], type: 'score', etape: 0 },
  // d1a « Duel 1 : la SVT. »
  { a: ['d1a', 0], type: 'duel', n: 1, matiere: 'SVT', icone: 'chromo', ch: 1 },
  // d1b « Avec 3 paires de chromosomes, la méiose donne 8 gamètes différents. Avec tes 23 paires : plus ou moins ? » — r1 « Beaucoup plus »
  { a: ['d1b', 0], type: 'plusmoins', q: 'GAMÈTES DIFFÉRENTS POSSIBLES',
    A: { t: '3 paires de chromosomes', v: 8, u: 'gamètes' }, B: { t: 'Tes 23 paires', v: 8388608, u: 'gamètes' },
    chrono: ['d1b', 'plus'], rep: ['r1', 0] },
  // e1 « Et la fécondation en réunit 2 au hasard. »
  { a: ['e1', 0], type: 'fecondation' },
  // d2a « Duel 2 : l'histoire. »
  { a: ['d2a', 0], type: 'duel', n: 2, matiere: 'HISTOIRE', img: 'wallstreet', ch: 2 },
  // d2b « Septembre 1929 : l'indice Dow Jones vaut 381 points. Juillet 1932 : plus ou moins ? » — r2 « Moins : 41 points ! »
  { a: ['d2b', 0], type: 'plusmoins', q: 'L’INDICE DOW JONES',
    A: { t: 'Septembre 1929', img: 'wallstreet', v: 381, u: 'points' }, B: { t: 'Juillet 1932', img: 'hooverville', v: 41, u: 'points' },
    chrono: ['d2b', 'plus'], rep: ['r2', 0] },
  // r2 « … Une chute de 89 pour cent. »
  { a: ['r2', 'chute'], type: 'chute', choc: true },
  // e2 « Le krach de 1929 ouvre la Grande Dépression, partout dans le monde. »
  { a: ['e2', 0], type: 'photo', img: 'soupe', t: 'LA GRANDE|DÉPRESSION', sous: 'Chicago, 1931 : la file des chômeurs', de: [1.05, .5, .45], vers: [1.25, .45, .4] },
  // d3a « Duel 3 : la physique. »
  { a: ['d3a', 0], type: 'duel', n: 3, matiere: 'PHYSIQUE', icone: 'lunette', ch: 3 },
  // d3b « Pour voir Mars aussi grosse que la Lune, une lunette doit grossir 105 fois. Et pour son volcan géant, Olympus Mons ? »
  { a: ['d3b', 0], type: 'angle' },
  { a: ['d3b', 'et'], type: 'plusmoins', q: 'GROSSISSEMENT NÉCESSAIRE',
    A: { t: 'Mars, grosse comme la Lune', img: 'lune', v: 105, u: 'fois' }, B: { t: 'Olympus Mons, son volcan', img: 'yerkes', v: 1100, u: 'fois' },
    chrono: ['d3b', 'mons'], rep: ['r3', 0] },
  // c3 « Trois, deux, un. » — r3 « Plus : environ 1 100 fois ! Le volcan est 10 fois plus petit que Mars. »
  { a: ['r3', 'le'], type: 'volcan' },
  // d4a « Dernier duel : la géographie. »
  { a: ['d4a', 0], type: 'duel', n: 4, matiere: 'GÉOGRAPHIE', img: 'mer', choc: true, ch: 4 },
  // d4b « Chaque jour, près de 24 millions de barils de pétrole passent le détroit de Malacca. Et le détroit d'Ormuz ? »
  { a: ['d4b', 0], type: 'detroits' },
  { a: ['d4b', 'et'], type: 'plusmoins', q: 'BARILS DE PÉTROLE PAR JOUR',
    A: { t: 'Détroit de Malacca', img: 'mer', v: 23700000, u: '' }, B: { t: 'Détroit d’Ormuz', v: 20900000, u: '' },
    chrono: ['d4b', "d'ormuz"], rep: ['r4', 0] },
  // r4 « Moins : environ 21 millions ! En 2023, Malacca fait mieux qu'Ormuz. »
  { a: ['r4', '2023'], type: 'podium' },
  // f1 « Alors, combien de bonnes réponses ? Dis-le en commentaire. »
  { a: ['f1', 0], type: 'score', etape: 1 },
  { a: ['f1', 'dis-le'], type: 'commentaire' },
  // f2 « Tout est expliqué sur Révisions Animées. »
  { a: ['f2', 0], type: 'chaine', serie: 'Révisions de Terminale', fond: 'lune' },
]);
window.CHAPITRES = ['ACCROCHE', 'DUEL SVT', 'DUEL HISTOIRE', 'DUEL PHYSIQUE', 'DUEL GÉOGRAPHIE'];
window.THEME = 'jeu';
window.MUSIQUE = 'funk_agressif3';
window.IMAGES = {
  drosophiles: '../../svt/serie/img/ch1-drosophiles.jpg',  // tubes de culture de drosophiles, photo Masur, CC BY-SA 4.0
  wallstreet: '../../dnl/serie/img/h1-wallstreet.jpg',     // foule devant la Bourse de New York, octobre 1929, domaine public
  hooverville: '../../dnl/serie/img/h1-hooverville.jpg',   // Hooverville à Seattle, 1933, Seattle Municipal Archives, CC BY 2.0
  soupe: '../../dnl/serie/img/h1-soupkitchen.jpg',         // chômeurs devant une soupe populaire, Chicago, février 1931, US National Archives, domaine public
  lune: '../../pc/serie/img/c5-lune.jpg',                  // la pleine Lune vue depuis l'espace, NASA, domaine public
  yerkes: '../../pc/serie/img/c5-yerkes.jpg',              // la lunette de 40 pouces de l'observatoire Yerkes, 1897, domaine public
  mer: '../../philo/serie/img/bh2-mer.jpg',                // Henry Dawson, Navires sur une mer calme au crépuscule, XIXe siècle, domaine public
};
