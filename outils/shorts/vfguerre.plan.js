// Découpage du short « Vrai ou faux : la Seconde Guerre mondiale », modèle A. a: [passage, mot] ; av : avance sur le mot.
// Les plans vraifaux (formats-a.js) durent de l'affirmation au verdict et à son explication ; les plans dessinés illustrent la suite.
window.PLAN = S => S.plans([
  // v1 « 5 affirmations sur la Seconde Guerre mondiale. Combien tu en as justes ? »
  { a: ['v1', 0], av: .25, type: 'mot', t: '5 AFFIRMATIONS', ch: 0 },
  { a: ['v1', 'seconde'], type: 'archive', img: 'blitz', t: 'LA SECONDE|GUERRE MONDIALE', legende: 'Londres, septembre 1940' },
  { a: ['v1', 'combien'], type: 'mot', t: 'COMBIEN TU EN|AS JUSTES ?', choc: true },
  // v2 « Top chrono. »
  { a: ['v2', 0], type: 'chrono' },
  // a1 / b1 : le pacte germano-soviétique (VRAI)
  { a: ['a1', 0], type: 'vraifaux', n: '1 / 5', t: 'Août 1939 : Hitler et Staline,|deux ennemis, signent un pacte', chrono: ['a1', 'vrai'], rep: ['b1', 0], v: true,
    expl: 'Le pacte germano-soviétique', ch: 1 },
  { a: ['b1', 'secret'], type: 'pologne' },
  // a2 / b2 : l'appel du 18 juin (FAUX)
  { a: ['a2', 0], type: 'vraifaux', n: '2 / 5', t: 'Presque toute la France entend|l’appel du 18 juin 1940', chrono: ['a2', 'vrai'], rep: ['b2', 0], v: false,
    expl: 'Peu de gens l’entendent en direct' },
  { a: ['b2', 'son'], type: 'portrait', img: 'degaulle', t: 'LA FRANCE LIBRE', sous: 'de Gaulle à la BBC, à Londres' },
  // a3 / b3 : pas de débarquement en Grande-Bretagne (FAUX)
  { a: ['a3', 0], type: 'vraifaux', n: '3 / 5', t: '1940 : l’armée allemande|débarque en Grande-Bretagne', chrono: ['a3', 'vrai'], rep: ['b3', 0], v: false,
    expl: 'Elle n’a pas la maîtrise du ciel', ch: 2 },
  { a: ['b3', 'hitler'], type: 'urss' },
  // a4 / b4 : Hitler déclare la guerre aux États-Unis (VRAI)
  { a: ['a4', 0], type: 'vraifaux', n: '4 / 5', t: 'Décembre 1941 : Hitler déclare|la guerre aux États-Unis', chrono: ['a4', 'vrai'], rep: ['b4', 0], v: true,
    expl: 'Le 11 décembre, avec l’Italie' },
  { a: ['b4', '4'], type: 'portrait', img: 'reichstag', t: '11 DÉC. 1941', sous: '4 jours après Pearl Harbor' },
  { a: ['b4', 'la'], type: 'globe', choc: true },
  // a5 / b5 : Stalingrad, la capitulation (FAUX)
  { a: ['a5', 0], type: 'vraifaux', n: '5 / 5', t: 'Stalingrad : l’armée allemande|ne se rend jamais', chrono: ['a5', 'vrai'], rep: ['b5', 0], v: false,
    expl: 'Encerclée, elle capitule', ch: 3 },
  { a: ['b5', 'le'], type: 'stalingrad' },
  { a: ['b5', 'environ'], type: 'prisonniers', n: ['b5', '91000'], choc: true },
  // e1 « Alors, ton score ? Dis-le en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS, TON|SCORE ?', ch: 4 },
  { a: ['e1', 'dis-le'], type: 'commentaire' },
  // e2 « Toute la guerre est expliquée sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'La Seconde Guerre mondiale', fond: 'blitz' },
]);
window.CHAPITRES = ['ACCROCHE', '1939-1940', '1940-1941', '1943', 'TON SCORE'];
window.IMAGES = {
  blitz: '../../dnl/serie/img/h3-blitz.jpg',         // enfants d'un faubourg de Londres sinistré, septembre 1940, US National Archives 306-NT-3163V, domaine public
  degaulle: '../../philo/serie/img/t2-degaulle.jpg',  // le général de Gaulle au micro de la BBC, Londres, photo Keystone, domaine public
  reichstag: '../../dnl/serie/img/h3-reichstag.jpg',  // Hitler déclare la guerre aux États-Unis, Reichstag, 11 décembre 1941 (Wikimedia Commons), CC BY-SA 3.0
};
window.MUSIQUE = 'quiz2';   // musique imposée pour ce short
