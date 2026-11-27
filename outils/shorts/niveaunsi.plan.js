// Découpage du short « NSI : niveau 1 → 10 », modèle A, habillage terminal. a: [passage, mot] ; av : avance sur le mot.
// Chaque palier est un plan « niveau » (formats-a.js) qui va de la question à l'explication, sauf le niveau 6 (plan propre
// « niveaucode » : le code reste à l'écran pendant le chrono) ; un plan dessiné ou une image fait la liaison avec le palier
// suivant (jamais deux plans de suite du même type).
window.MUSIQUE = 'automotivo2';
window.THEME = 'terminal';
window.PLAN = S => S.plans([
  // h1 « NSI : niveau 1 à 10. » / h2 « À quel niveau tu t'arrêtes ? Pas de triche. »
  { a: ['h1', 0], av: .25, type: 'collage', imgs: ['turing', 'lovelace', 'hopper'], t: 'NSI|NIVEAU 1 À 10', ch: 0 },
  { a: ['h2', 0], type: 'echelle' },
  { a: ['h2', 'pas'], type: 'triche', choc: true },
  // niveau 1 : 13 en binaire
  { a: ['q1', 0], type: 'niveau', n: 1, total: 10, img: 'eniac', q: 'Écris 13|en binaire', chrono: ['q1', 'binaire'], rep: ['r1', 0],
    r: '1101', expl: '8 + 4 + 0 + 1 = 13', ch: 1 },
  { a: ['r1', 'soit'], type: 'bits' },
  // niveau 2 : la pile
  { a: ['q2', 0], type: 'niveau', n: 2, total: 10, q: 'Une pile : tu empiles|A, B, puis C.|Qui sort en premier ?', chrono: ['q2', 'qui'], rep: ['r2', 0],
    r: 'C', expl: 'Dernier entré, premier sorti' },
  { a: ['r2', 'le'], type: 'pile', file: ['r2', 'une'] },
  // t1 « Trop facile ? On passe aux bases de données. »
  { a: ['t1', 0], type: 'photo', img: 'datacenter', t: 'TROP FACILE ?|LES BASES DE DONNÉES', legende: 'Centre de données, photo BalticServers.com, CC BY-SA 3.0', ch: 2 },
  // niveau 4 : SQL
  { a: ['q4', 0], type: 'niveau', n: 4, total: 10, q: 'En SQL, quel mot-clé|filtre les lignes|d’une table ?', chrono: ['q4', 'filtre'], rep: ['r4', 0],
    r: 'WHERE', expl: 'SELECT … FROM … WHERE condition' },
  { a: ['r4', 'il'], type: 'sql' },
  // niveau 6 : la fonction récursive (le code reste affiché)
  { a: ['q6', 0], type: 'niveaucode', n: 6, chrono: ['q6', 'que'], rep: ['r6', 0], r: 'f(4) = 10', expl: '4 + 3 + 2 + 1 + 0' },
  { a: ['r6', 2], av: .15, type: 'appels' },   // 2 = le premier « plus » : les appels suivent « 4 plus 3 plus 2 plus 1 plus 0 »
  // t2 « Là, ça pique. Place aux algorithmes. »
  { a: ['t2', 0], type: 'mot', t: 'LÀ, ÇA|PIQUE', choc: true, ch: 3 },
  { a: ['t2', 'place'], type: 'photo', img: 'noteg', t: 'PLACE AUX|ALGORITHMES', de: [1.15, .3, .4], vers: [1.4, .45, .45],
    legende: 'Ada Lovelace, Note G, 1843 : le premier algorithme publié, domaine public' },
  // niveau 8 : la dichotomie
  { a: ['q8', 0], type: 'niveau', n: 8, total: 10, q: 'Recherche dichotomique|1 million d’éléments triés|Combien d’étapes au pire ?', chrono: ['q8', 'combien'], rep: ['r8', 0],
    r: '20 ÉTAPES', expl: 'On coupe en 2 à chaque fois|2 puissance 20 = 1 048 576' },
  { a: ['r8', 'tu'], type: 'dicho' },
  // niveau 10 : le problème de l'arrêt
  { a: ['q10', 0], type: 'mot', t: 'NIVEAU 10|BOSS FINAL', choc: true, ch: 4 },
  { a: ['q10', 'un'], type: 'niveau', n: 10, total: 10, q: 'Un programme peut-il prédire|si n’importe quel programme|s’arrête ?', chrono: ['q10', "s'arrête"], rep: ['r10', 0],
    r: 'NON', expl: 'Le problème de l’arrêt|est indécidable' },
  { a: ['r10', 'une'], type: 'portrait', img: 'turing', t: 'TURING', sous: 'On Computable Numbers, 1936' },
  // e1 « Alors, tu t'arrêtes où ? Dis ton niveau en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS, TU T’ARRÊTES|OÙ ?' },
  { a: ['e1', 'dis'], type: 'commentaire' },
  // e2 « Plus de défis sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'eniac' },
]);
window.CHAPITRES = ['ACCROCHE', 'LES BASES', 'LES DONNÉES', 'LES ALGOS', 'BOSS FINAL · TON NIVEAU'];
window.IMAGES = {
  turing: 'img/nsi-turing.jpg',          // Alan Turing en 1951, photo Elliott & Fry (recadrée), Wikimedia Commons, domaine public
  lovelace: 'img/nsi-lovelace.jpg',      // Ada Lovelace, portrait d'Alfred Edward Chalon, vers 1840, Wikimedia Commons, domaine public
  hopper: 'img/nsi-hopper.jpg',          // Grace Hopper, photo officielle de l'US Navy par James S. Davis, 1984, domaine public
  eniac: 'img/nsi-eniac.jpg',            // Glen Beck et Betty Snyder programment l'ENIAC, photo de l'US Army, vers 1947, domaine public
  datacenter: 'img/nsi-datacenter.jpg',  // centre de données, photo BalticServers.com, CC BY-SA 3.0 (attribution obligatoire)
  noteg: 'img/nsi-noteg.jpg',            // Ada Lovelace, « Diagram for the computation of Bernoulli numbers » (Note G), 1843, domaine public
};
