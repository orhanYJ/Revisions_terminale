// Découpage du short « devinehlp » (format « devine » : « HLP : devine l'auteur en 3 indices »), modèle A, habillage
// « alerte ». a: [passage, mot] ; av : avance sur le mot. Chaque manche (une partie du programme) : carte « MANCHE n »,
// puis le plan `devine2` (portrait pixellisé qui se précise à chaque indice, chrono après « Trois, deux, un »,
// révélation) qui revient entre des plans de liaison illustrant les indices. Le même objet `devine2` est repris à chaque
// retour ; seul le premier porte `sons: true` (les sons des indices ne sont émis qu'une fois).
const ROUSSEAU = { type: 'devine2', img: 'rousseau', sur: 'DEVINE L’AUTEUR · 1 / 3', indices: [
  [['a1', 'indice'], 'Il abandonne ses 5 enfants'], [['a2', 0], 'Il écrit un traité d’éducation'], [['a3', 0], '« L’homme est né libre… »']],
  chrono: ['a3', 'trois'], rep: ['c1', 0], nom: 'ROUSSEAU', sous: '1712 – 1778|Émile ou De l’éducation, 1762' };
const PROUST = { type: 'devine2', img: 'proust', sur: 'DEVINE L’AUTEUR · 2 / 3', indices: [
  [['b1', 'indice'], 'Il écrit la nuit, dans le liège'], [['b2', 0], 'Prix Goncourt en 1919'], [['b3', 0], 'Une madeleine dans le thé']],
  chrono: ['b3', 'trois'], rep: ['c2', 0], nom: 'PROUST', sous: '1871 – 1922|À la recherche du temps perdu' };
const FREUD = { type: 'devine2', img: 'freud', sur: 'DEVINE L’AUTEUR · 3 / 3', indices: [
  [['e1', 'indice'], '1938 : il fuit les nazis'], [['e2', 0], 'Le rêve, voie royale'], [['e3', 0], 'Il invente la psychanalyse']],
  chrono: ['e3', 'trois'], rep: ['c3', 0], nom: 'FREUD', sous: '1856 – 1939|L’Interprétation du rêve, 1900' };
const dv = (base, a, o = {}) => Object.assign({}, base, { a }, o);
window.MUSIQUE = 'terre2';
window.THEME = 'alerte';
window.PLAN = S => S.plans([
  // d1 « HLP : devine l'auteur en 3 indices. »
  { a: ['d1', 0], av: .2, type: 'mosaique', ch: 0 },
  // d2 « Du plus dur au plus facile. Trouve avant la fin du compte ! »
  { a: ['d2', 0], type: 'regles', etapes: [[['d2', 'du'], 'INDICE 1', 'DIFFICILE'], [['d2', 'au'], 'INDICE 2', 'MOYEN'], [['d2', 'facile'], 'INDICE 3', 'FACILE']] },
  { a: ['d2', 'trouve'], type: 'mot', t: 'TROUVE AVANT|LA FIN DU COMPTE', choc: true },
  // MANCHE 1 · a1 « Manche 1 : l'éducation. Indice 1 : il abandonne ses 5 enfants. »
  { a: ['a1', 0], type: 'manche', n: 1, matiere: 'ÉDUCATION, TRANSMISSION|ET ÉMANCIPATION', ch: 1 },
  dv(ROUSSEAU, ['a1', 'indice'], { sons: true }),
  { a: ['a1', 'abandonne'], type: 'mot', t: '5 ENFANTS|ABANDONNÉS', sombre: true, choc: true },
  // a2 « Indice 2 : il écrit pourtant un traité d'éducation. »
  dv(ROUSSEAU, ['a2', 0]),
  { a: ['a2', 'traité'], type: 'photo', img: 'emile', t: 'UN TRAITÉ|D’ÉDUCATION', de: [1.0, .5, .3], vers: [1.15, .5, .25], nb: true, legende: 'Émile ou De l’éducation, page de titre, 1762 (domaine public)' },
  // a3 « Indice 3 : « L'homme est né libre, et partout il est dans les fers. » Trois, deux, un. » ; c1 « C'est Rousseau ! … »
  dv(ROUSSEAU, ['a3', 0]),
  // c1 « … L'Émile, 1762. Et dans ses Confessions, il avoue tout. »
  { a: ['c1', 'et'], type: 'aveu', avoue: ['c1', 'avoue'] },
  // MANCHE 2 · b1 « Manche 2 : la sensibilité. Indice 1 : il écrit la nuit, dans une chambre tapissée de liège. »
  { a: ['b1', 0], type: 'manche', n: 2, matiere: 'LES EXPRESSIONS|DE LA SENSIBILITÉ', ch: 2 },
  dv(PROUST, ['b1', 'indice'], { sons: true }),
  { a: ['b1', 'chambre'], type: 'chambre' },
  // b2 « Indice 2 : prix Goncourt en 1919. »
  dv(PROUST, ['b2', 0]),
  { a: ['b2', 'goncourt'], type: 'date', t: '1919', de: 1900, sous: 'PRIX GONCOURT' },
  // b3 « Indice 3 : une madeleine trempée dans le thé. Trois, deux, un. » ; c2 « C'est Marcel Proust ! … »
  dv(PROUST, ['b3', 0]),
  // c2 « … Un goût, et tout le passé revient : la mémoire involontaire. »
  { a: ['c2', 'un'], type: 'madeleine', revient: ['c2', 'revient'] },
  { a: ['c2', 'mémoire'], type: 'collage', imgs: ['proust', 'epreuves'], t: 'LA MÉMOIRE|INVOLONTAIRE' },
  // MANCHE 3 · e1 « Dernière manche : les métamorphoses du moi. Indice 1 : en 1938, il fuit les nazis pour Londres. »
  { a: ['e1', 0], type: 'manche', n: 3, matiere: 'LES MÉTAMORPHOSES|DU MOI', ch: 3 },
  dv(FREUD, ['e1', 'indice'], { sons: true }),
  { a: ['e1', 'fuit'], type: 'photo', img: 'berggasse', t: 'VIENNE|1938', sous: 'il fuit les nazis pour Londres', de: [1.05, .5, .45], vers: [1.2, .5, .4], legende: 'Plaque au 19, Berggasse, Vienne, où Freud vécut de 1891 à 1938 (photo GuentherZ, CC BY 3.0)' },
  // e2 « Indice 2 : pour lui, le rêve est la voie royale vers l'inconscient. »
  dv(FREUD, ['e2', 0]),
  { a: ['e2', 'rêve'], type: 'mot', img: 'traumdeutung', t: 'LE RÊVE|VOIE ROYALE' },
  // e3 « Indice 3 : il invente la psychanalyse. Trois, deux, un. » ; c3 « C'est Sigmund Freud ! … »
  dv(FREUD, ['e3', 0]),
  // c3 « … Le moi n'est pas maître dans sa propre maison. »
  { a: ['c3', 'pas'], av: .5, type: 'maison', choc: true },
  // o1 « Combien tu en as trouvé ? Dis-le en commentaire. »
  { a: ['o1', 0], type: 'score', imgs: [['rousseau', 'ROUSSEAU'], ['proust', 'PROUST'], ['freud', 'FREUD']], dis: ['o1', 'dis-le'], ch: 4 },
  // o2 « Rousseau et Freud sont expliqués dans les séries philo de Révisions Animées. »
  { a: ['o2', 0], type: 'collage', imgs: ['rousseau', 'freud'], t: 'EXPLIQUÉS|EN VIDÉO' },
  { a: ['o2', 'séries'], type: 'chaine', serie: 'Philosophie', fond: 'emile' },
  // o3 « Et le prochain auteur… tu le trouves en combien d'indices ? » (relance le jeu du début)
  { a: ['o3', 0], type: 'mosaique', fin: true },
]);
window.CHAPITRES = ['LE JEU', 'MANCHE 1', 'MANCHE 2', 'MANCHE 3', 'TON SCORE'];
window.IMAGES = {
  rousseau: '../../philo/serie/img/rousseau.jpg',              // Maurice Quentin de La Tour, 1753, domaine public
  freud: '../../philo/serie/img/freud.jpg',                    // Max Halberstadt, vers 1921, domaine public
  emile: '../../philo/serie/img/dv2-emile.jpg',                // Rousseau, Émile ou De l'éducation, page de titre, 1762, domaine public
  traumdeutung: '../../philo/serie/img/cs3-traumdeutung.jpg',  // Freud, Die Traumdeutung, Vienne, 1900, page de titre, domaine public
  berggasse: '../../philo/serie/img/bh4-berggasse.jpg',        // plaque au 19, Berggasse, Vienne, photo GuentherZ, CC BY 3.0 (attribution obligatoire)
  // Wikimedia Commons, enregistrées dans outils/shorts/img/ le 27/11/2026 :
  proust: 'img/hlp-proust.jpg',                // Otto Wegener, Marcel Proust vers 1895, domaine public (File:Marcel_Proust_vers_1895.jpg)
  epreuves: 'img/hlp-proust-epreuves.jpg',     // épreuves corrigées de À la recherche du temps perdu, domaine public (File:MS_A_la_recherche_du_temps_perdu.jpg)
};
