// Découpage du short « NSI : vrai ou faux ? », modèle A, habillage néon. a: [passage, mot] ; av : avance sur le mot.
// Les plans vraifaux (formats-a.js) durent de l'affirmation au verdict ; une image ou un plan dessiné illustre
// l'explication (jamais deux plans de suite du même type). Chrono : ['aN', -3] = le « Vrai » de « Vrai… ou faux ? ».
window.MUSIQUE = 'hardtekk2';
window.THEME = 'neon';
window.PLAN = S => S.plans([
  // v1 « 5 affirmations sur l'informatique. Combien tu en as justes ? » / v2 « Top chrono. »
  { a: ['v1', 0], av: .25, type: 'mot', t: '5 AFFIRMATIONS', ch: 0 },
  { a: ['v1', 'sur'], type: 'collage', imgs: ['eniac', 'hopper', 'lovelace', 'turing'], t: 'SUR|L’INFORMATIQUE' },
  { a: ['v1', 'combien'], type: 'mot', t: 'COMBIEN TU EN|AS JUSTES ?', choc: true },
  { a: ['v2', 0], type: 'chrono' },
  // 1 : Internet et le Web (FAUX)
  { a: ['a1', 0], type: 'vraifaux', n: '1 / 5', t: 'Internet et le Web,|c’est la même chose', chrono: ['a1', -3], rep: ['b1', 0], v: false,
    expl: 'Le Web est un service d’Internet', ch: 1 },
  { a: ['b1', 'internet'], av: -.72, type: 'reseau' },
  { a: ['b1', 'web'], av: .2, type: 'photo', img: 'serveurweb', de: [1.0, .62, .5], vers: [1.12, .64, .45], t: 'LE WEB|NÉ EN 1989', sous: 'le premier serveur web, au CERN',
    legende: 'Premier serveur web (CERN), photo Coolcaesar, CC BY-SA 3.0' },
  { a: ['b1', "n'est"], type: 'reseau', web: ['b1', "n'est"], mail: ['b1', 'comme'] },
  // 2 : IPv4 sur 32 bits (VRAI)
  { a: ['a2', 0], type: 'vraifaux', n: '2 / 5', t: 'Une adresse IPv4|tient sur 32 bits', chrono: ['a2', -3], rep: ['b2', 0], v: true,
    expl: '4 octets de 8 bits' },
  { a: ['b2', '4'], av: -.98, type: 'ip' },
  { a: ['b2', 'trop'], type: 'mot', t: 'TROP PEU|D’OÙ L’IPv6' },
  // 3 : le mot « bug » (FAUX)
  { a: ['a3', 0], type: 'vraifaux', n: '3 / 5', t: 'Le mot « bug » vient d’un|vrai insecte, trouvé en 1947', chrono: ['a3', -3], rep: ['b3', 0], v: false,
    expl: 'L’insecte est vrai, le mot est plus ancien', ch: 2 },
  { a: ['b3', "l'insecte"], av: -1.02, type: 'photo', img: 'bug', t: 'UNE VRAIE MITE|RELAIS N° 70', choc: true, de: [1.0, .2, .6], vers: [1.2, .24, .62],
    legende: 'Journal du Harvard Mark II, 9 septembre 1947, US Navy, domaine public' },
  { a: ['b3', 'mais'], type: 'date', t: '1878', de: 1947, sous: 'EDISON PARLE DÉJÀ DE BUGS' },
  // 4 : Ada Lovelace (VRAI)
  { a: ['a4', 0], type: 'vraifaux', n: '4 / 5', t: 'Le 1er programme publié|a été écrit par une femme', chrono: ['a4', -3], rep: ['b4', 0], v: true,
    expl: 'Au 19e siècle, en 1843', ch: 3 },
  { a: ['b4', 'ada'], av: -.6, type: 'portrait', img: 'lovelace', t: 'ADA LOVELACE', sous: 'Note G, 1843' },
  { a: ['b4', 'un'], type: 'photo', img: 'noteg', t: 'UN ALGORITHME|POUR UNE MACHINE', de: [1.1, .35, .4], vers: [1.35, .5, .45],
    legende: 'Ada Lovelace, Note G (nombres de Bernoulli), 1843, domaine public' },
  { a: ['b4', 'qui'], type: 'mot', img: 'babbage', t: 'JAMAIS|CONSTRUITE' },   // photo : essai partiel de la machine analytique, inachevé à la mort de Babbage
  // 5 : le problème de l'arrêt (FAUX)
  { a: ['a5', 0], type: 'vraifaux', n: '5 / 5', t: 'Avec assez de temps, un|ordinateur résout tout', chrono: ['a5', -3], rep: ['b5', 0], v: false,
    expl: 'Certains problèmes n’ont aucune solution', ch: 4 },
  { a: ['b5', 'aucun'], av: -.5, type: 'arret' },
  { a: ['b5', 'le'], type: 'mot', img: 'turing', t: 'LE PROBLÈME DE L’ARRÊT|INDÉCIDABLE', choc: true },
  // e1 « Alors, ton score ? Dis-le en commentaire. » / e2 « Plus de défis sur Révisions Animées. »
  { a: ['e1', 0], type: 'commentaire' },
  { a: ['e2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'eniac' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE RÉSEAU', 'LE BUG', 'LE PREMIER PROGRAMME', 'LES LIMITES · TON SCORE'];
window.IMAGES = {
  eniac: 'img/nsi-eniac.jpg',            // Glen Beck et Betty Snyder programment l'ENIAC, photo de l'US Army, vers 1947, domaine public
  hopper: 'img/nsi-hopper.jpg',          // Grace Hopper, photo officielle de l'US Navy par James S. Davis, 1984, domaine public
  lovelace: 'img/nsi-lovelace.jpg',      // Ada Lovelace, portrait d'Alfred Edward Chalon, vers 1840, Wikimedia Commons, domaine public
  turing: 'img/nsi-turing.jpg',          // Alan Turing en 1951, photo Elliott & Fry (recadrée), Wikimedia Commons, domaine public
  serveurweb: 'img/nsi-serveurweb.jpg',  // le premier serveur web (NeXT de Tim Berners-Lee, CERN), photo Coolcaesar, CC BY-SA 3.0 (attribution obligatoire)
  bug: 'img/nsi-bug.jpg',                // « First actual case of bug being found », journal du Harvard Mark II, 9 septembre 1947, US Navy, domaine public
  noteg: 'img/nsi-noteg.jpg',            // Ada Lovelace, « Diagram for the computation of Bernoulli numbers » (Note G), 1843, domaine public
  babbage: 'img/nsi-babbage.jpg',        // machine analytique de Babbage (modèle partiel, Science Museum), photo Marcin Wichary, CC BY 2.0 (attribution obligatoire)
};
