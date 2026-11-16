// Découpage du short « Défi bac : 5 épreuves », modèle A, habillage « jeu ». a: [passage, mot] ; av : avance sur le mot.
// Une épreuve par format et par matière ; une photo ou un portrait annonce chaque épreuve, un plan dessiné l'explique.
window.MUSIQUE = 'automotivo2';
window.THEME = 'jeu';
window.PLAN = S => S.plans([
  // h1 « 5 épreuves. 5 matières. Es-tu prêt pour le bac ? » / h2 « Compte tes points, 1 par épreuve. C'est parti ! »
  { a: ['h1', 0], av: .25, type: 'epreuves', ch: 0 },
  { a: ['h1', 'es-tu'], type: 'mot', t: 'ES-TU PRÊT|POUR LE BAC ?', choc: true },
  { a: ['h2', 0], type: 'score', v: 0 },
  // épreuve 1 : SVT, vrai ou faux
  { a: ['v0', 0], type: 'photo', img: 'mito', t: 'ÉPREUVE 1|SVT', legende: 'Deux mitochondries, microscope électronique, Louisa Howard, domaine public', ch: 1 },
  { a: ['v1', 0], type: 'vraifaux', n: '1 / 5', t: 'Tes mitochondries|descendent d’une bactérie', chrono: ['v1', 'vrai'], rep: ['v2', 0], v: true,
    expl: 'Avalée, jamais digérée' },
  { a: ['v2', 'avalée'], type: 'endo' },
  { a: ['v2', '1'], type: 'score', v: 1 },
  // épreuve 2 : histoire, remets dans l'ordre
  { a: ['o0', 0], type: 'photo', img: 'wall', nb: true, t: 'ÉPREUVE 2|HISTOIRE', legende: 'Foule devant la Bourse de New York, octobre 1929, domaine public' },
  { a: ['o1', 0], type: 'ordre', cartes: [{ t: 'Pearl Harbor', d: '7 déc. 1941' }, { t: 'Krach de Wall Street', d: 'oct. 1929' },
    { t: 'Opération Barbarossa', d: '22 juin 1941' }, { t: 'Hitler chancelier', d: '30 janv. 1933' }],
    ordre: [1, 3, 2, 0], chrono: ['o1', "l'ordre"], rep: ['o2', 0], expl: 'Barbarossa (juin) avant Pearl Harbor (déc.)' },
  { a: ['o2', 'et'], type: 'piege41' },
  // épreuve 3 : philosophie, trouve l'intrus
  { a: ['i0', 0], type: 'mot', img: 'penseur', t: 'ÉPREUVE 3|PHILOSOPHIE', ch: 2 },
  { a: ['i1', 0], type: 'intrus', sur: 'L’ÉTAT, UN CONTRAT ?', options: [{ t: 'Hobbes', img: 'hobbes', nb: true }, { t: 'Locke', img: 'locke', nb: true },
    { t: 'Descartes', img: 'descartes', nb: true }, { t: 'Rousseau', img: 'rousseau', nb: true }],
    intrus: 2, chrono: ['i1', 'trouve'], rep: ['i2', 0], expl: 'Descartes : le cogito, pas le contrat' },
  { a: ['i2', "l'état"], type: 'contrat' },
  { a: ['i2', 'lui'], type: 'portrait', img: 'descartes', t: 'LE COGITO', sous: '« Je pense, donc je suis »' },
  // épreuve 4 : géographie, plus ou moins
  { a: ['p0', 0], type: 'photo', img: 'mer', t: 'ÉPREUVE 4|GÉOGRAPHIE', legende: 'Henry Dawson, Navires sur une mer calme au crépuscule, XIXᵉ siècle, domaine public', ch: 3 },
  { a: ['p1', 0], type: 'plusmoins', q: 'PART DE LA FLOTTE MONDIALE', A: { t: 'Pétroliers en 1980', v: 50, u: '%' }, B: { t: 'Pétroliers en 2024', v: 28, u: '%' },
    chrono: ['p1', 'plus'], rep: ['p2', 0] },
  { a: ['p2', 'les'], type: 'flotte' },
  // épreuve 5 : physique-chimie, niveau 10
  { a: ['n0', 0], type: 'photo', img: 'orion', t: 'ÉPREUVE 5|NIVEAU 10', legende: 'Nébuleuse d’Orion, Hubble, NASA, ESA, M. Robberto, domaine public', choc: true, ch: 4 },
  { a: ['n1', 0], type: 'niveau', n: 10, total: 10, q: 'Un photon de 11 eV|frappe un atome d’hydrogène|au repos. Absorbé ?', chrono: ['n1', 'repos'], rep: ['n2', 0],
    r: 'NON', expl: 'Aucune transition ne vaut 11 eV|niveau 1 vers 2 : 10,2 eV · vers 3 : 12,1 eV' },
  { a: ['n2', 'il'], type: 'atome' },
  // e1 « Alors, prêt pour le bac ? Ton score sur 5 en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS,|PRÊT ?' },
  { a: ['e1', 'ton'], type: 'commentaire' },
  // e2 « Toutes les matières sont sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Révisions de Terminale', fond: 'penseur' },
]);
window.CHAPITRES = ['ACCROCHE', 'SVT · HISTOIRE', 'PHILOSOPHIE', 'GÉOGRAPHIE', 'PHYSIQUE-CHIMIE · TON SCORE'];
window.IMAGES = {
  mito: '../../svt/serie/img/ch2-mito.jpg',              // deux mitochondries, poumon de mammifère, microscope électronique, Louisa Howard, domaine public
  wall: '../../dnl/serie/img/h1-wallstreet.jpg',         // foule devant la Bourse de New York, octobre 1929, Wikimedia Commons, domaine public
  penseur: '../../philo/serie/img/t-penseur.jpg',        // Rodin, Le Penseur, photo Jebulon, CC0
  hobbes: '../../philo/serie/img/hobbes.jpg',            // Thomas Hobbes, John Michael Wright, vers 1669-1670, domaine public
  locke: '../../philo/serie/img/locke.jpg',              // John Locke, Godfrey Kneller, 1697, domaine public
  descartes: '../../philo/serie/img/descartes.jpg',      // René Descartes, d'après Frans Hals, XVIIe siècle, domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',        // Jean-Jacques Rousseau, Maurice Quentin de La Tour, 1753, domaine public
  mer: '../../philo/serie/img/bh2-mer.jpg',              // Henry Dawson, Navires sur une mer calme au crépuscule, XIXe siècle, domaine public
  orion: '../../pc/serie/img/c4-orion.jpg',              // nébuleuse d'Orion, Hubble, NASA, ESA, M. Robberto, domaine public
};
