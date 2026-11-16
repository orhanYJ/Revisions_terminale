// Découpage du short « Seconde Guerre mondiale : niveau 1 → 10 » (format « niveau », le spectateur joue), modèle A.
// a: [passage, mot] ; av : avance sur le mot. Les plans niveau (formats-a.js) durent de la question au verdict ;
// un plan de liaison (carte schématique, radio, portrait, date…) illustre chaque réponse.
window.PLAN = S => S.plans([
  // i1 « Seconde Guerre mondiale, niveau 1 à 10. À quel niveau tu t'arrêtes ? »
  { a: ['i1', 0], av: .2, type: 'collage', imgs: ['blitz', 'reichstag', 'degaulle', 'churchill'], t: 'SECONDE GUERRE|MONDIALE', ch: 0 },
  { a: ['i1', 'niveau'], type: 'mot', t: 'NIVEAU|1 → 10' },
  { a: ['i1', 'quel'], av: .35, type: 'echelle', mode: 'stop', t: 'À QUEL NIVEAU|TU T’ARRÊTES ?', choc: true },
  // i2 « Plus tu montes, plus c'est dur. Réponds avant le chrono. »
  { a: ['i2', 0], type: 'mot', t: 'PLUS TU MONTES|PLUS C’EST DUR' },
  { a: ['i2', 'réponds'], type: 'chronometre', t: 'RÉPONDS AVANT|LE CHRONO' },
  // q1 / r1 : la Pologne
  { a: ['q1', 0], type: 'niveau', n: 1, total: 10, img: 'pacte', q: '1er septembre 1939 : quel pays|l’Allemagne envahit-elle ?',
    chrono: ['q1', 'envahit-elle'], rep: ['r1', 0], r: 'LA POLOGNE', expl: 'Juste après le pacte avec Staline', ch: 1 },
  { a: ['r1', 'son'], type: 'carto', v: 'pologne' },
  // q2 / r2 : l'appel du 18 juin
  { a: ['q2', 0], type: 'niveau', n: 2, total: 10, img: 'degaulle', q: 'De Gaulle lance son appel|depuis Londres. Quel jour ?',
    chrono: ['q2', 'jour'], rep: ['r2', 0], r: 'LE 18 JUIN 1940', expl: 'À la radio de la BBC' },
  { a: ['r2', 'à'], type: 'radio' },
  // q3 / r3 : Churchill
  { a: ['q3', 0], type: 'niveau', n: 4, total: 10, img: 'blitz', q: 'Quel Premier ministre refuse|de négocier avec Hitler, en 1940 ?',
    chrono: ['q3', '1940'], rep: ['r3', 0], r: 'CHURCHILL', expl: 'Le Royaume-Uni tient' },
  { a: ['r3', 'sous'], type: 'portrait', img: 'churchill', t: 'CHURCHILL', sous: 'Premier ministre dès le 10 mai 1940' },
  // q4 / r4 : Pearl Harbor
  { a: ['q4', 0], type: 'niveau', n: 5, total: 10, img: 'reichstag', q: 'Quelle attaque fait entrer|les États-Unis dans la guerre ?',
    chrono: ['q4', 'guerre'], rep: ['r4', 0], r: 'PEARL HARBOR', expl: 'Le 7 décembre 1941', ch: 2 },
  { a: ['r4', 'guerre'], av: .3, type: 'carto', v: 'monde' },
  // t1 « Ça se corse. »
  { a: ['t1', 0], type: 'mot', t: 'ÇA SE|CORSE', choc: true, bruit: true },
  // q5 / r5 : Barbarossa
  { a: ['q5', 0], type: 'niveau', n: 7, total: 10, img: 'staline', q: 'Comment s’appelle l’invasion|de l’URSS, le 22 juin 1941 ?',
    chrono: ['q5', '1941'], rep: ['r5', 0], r: 'BARBAROSSA', expl: 'Une guerre d’anéantissement', ch: 3 },
  { a: ['r5', 'trois'], type: 'carto', v: 'barbarossa' },
  // q6 / r6 : Paulus
  { a: ['q6', 0], type: 'niveau', n: 9, total: 10, q: 'À Stalingrad, quel général|allemand capitule ?',
    chrono: ['q6', 'capitule'], rep: ['r6', 0], r: 'PAULUS', expl: 'Le 31 janvier 1943' },
  { a: ['r6', 'tournant'], av: .3, type: 'date', t: '1943', de: 1939, sous: 'LE TOURNANT' },
  // q7 / r7 : 1937
  { a: ['q7', 0], type: 'echelle', mode: 'dernier', t: 'NIVEAU 10|LE DERNIER', choc: true },
  { a: ['q7', 'pour'], type: 'niveau', n: 10, total: 10, q: 'Pour certains historiens,|la guerre mondiale commence|en Asie. En quelle année ?',
    chrono: ['q7', 'année'], rep: ['r7', 0], r: '1937', expl: 'Le Japon attaque la Chine' },
  { a: ['r7', 'japon'], av: .3, type: 'carto', v: 'asie' },
  // e1 « Alors ? Dis ton niveau en commentaire. »
  { a: ['e1', 0], type: 'commentaire', t: 'DIS TON NIVEAU|EN COMMENTAIRE', ch: 4 },
  // e2 « Toute la guerre est sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'La Seconde Guerre mondiale', fond: 'churchill' },
]);
window.CHAPITRES = ['ACCROCHE', '1939-1940', '1940-1941', '1941-1943', 'TON NIVEAU'];
window.IMAGES = {
  blitz: '../../dnl/serie/img/h3-blitz.jpg',            // enfants d'une banlieue est de Londres, sans abri après un raid nocturne, septembre 1940, New Times Paris Bureau Collection (USIA), US National Archives 306-NT-3163V, domaine public
  churchill: '../../dnl/serie/img/h3-churchill.jpg',    // Winston Churchill, Ottawa, décembre 1941, par Yousuf Karsh (Bibliothèque et Archives Canada, Wikimedia Commons), CC BY 2.0
  reichstag: '../../dnl/serie/img/h3-reichstag.jpg',    // Hitler déclare la guerre aux États-Unis, Reichstag, 11 décembre 1941 (Wikimedia Commons), CC BY-SA 3.0
  degaulle: '../../philo/serie/img/t2-degaulle.jpg',    // le général de Gaulle au micro de la BBC, Londres, photo Keystone, domaine public
  pacte: '../../dnl/serie/img/h2-pact.jpg',             // Staline et Ribbentrop après la signature du pacte germano-soviétique, Moscou, 23 août 1939, Bundesarchiv, Bild 183-H27337 / Helmut Laux, CC BY-SA 3.0 DE
  staline: '../../dnl/serie/img/h2-stalin.jpg',         // Staline à la tribune, Moscou, 1937, photographe inconnu, domaine public
};
window.MUSIQUE = 'montagem';   // musique imposée pour ce short
window.THEME = 'alerte';       // habillage imposé pour ce short
