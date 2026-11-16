// Découpage du short « erreurbac » (format « erreur » : trouve l'erreur dans trois copies de bac), modèle A,
// habillage archives. a: [passage, mot] ; av : avance sur le mot. Chaque manche : carte « MANCHE n », la copie
// (le spectateur lit pendant la voix, puis chrono de silence après « Trois, deux, un »), le verdict, puis des plans
// de liaison avec images.
window.MUSIQUE = 'montagem3';
window.THEME = 'archives';
window.PLAN = S => S.plans([
  // e1 « Trois copies de bac. Une erreur cachée dans chacune. »
  { a: ['e1', 0], av: .2, type: 'photo', img: 'examen', t: '3 COPIES|DE BAC', de: [1.05, .5, .5], vers: [1.25, .5, .55], nb: true, ch: 0 },
  { a: ['e1', 'une'], type: 'copies', t: '1 ERREUR|DANS CHACUNE' },
  // e2 « Toi, tu la trouves avant la fin du chrono ? On joue. »
  { a: ['e2', 0], type: 'mot', t: 'AVANT LA FIN|DU CHRONO ?' },
  { a: ['e2', 'on'], type: 'pret', t: 'ON JOUE !' },
  // e3 « Manche 1 : la philo. Sujet : sommes-nous libres ? » / e4 « Lis les 4 lignes. Trois, deux, un. »
  { a: ['e3', 0], type: 'manche', n: 1, matiere: 'PHILOSOPHIE', dessin: 'plume', ch: 1 },
  { a: ['e3', 'sujet'], type: 'erreur', matiere: 'PHILOSOPHIE', sujet: 'Sommes-nous libres ?',
    lignes: ['Descartes : ma volonté est infinie.', 'Spinoza : le libre arbitre est une illusion.',
      'Sartre : « … partout il est dans les fers ».', 'Kant : « tu dois, donc tu peux ».'],
    faute: 2, correction: 'Rousseau, Du contrat social (1762)', chrono: ['e4', 'trois'], rep: ['e5', 0] },
  // e5 « Ligne 3 ! « Partout il est dans les fers » : ce n'est pas Sartre. »
  { a: ['e5', 'ce'], type: 'barre', img: 'sartre', t: 'PAS SARTRE', choc: true },
  // e6 « C'est Rousseau, au début de Du contrat social, en 1762. »
  { a: ['e6', 0], type: 'collage', imgs: ['rousseau', 'contrat'], t: 'ROUSSEAU|DU CONTRAT SOCIAL' },
  // e7 « Nuance : Sartre, lui, écrit que l'homme est condamné à être libre. »
  { a: ['e7', 0], type: 'portrait', img: 'sartre', t: 'SARTRE', sous: 'L’existentialisme est un humanisme' },
  { a: ['e7', 'condamné'], type: 'mot', t: 'CONDAMNÉ|À ÊTRE LIBRE' },
  // e8 « Manche 2 : l'histoire. Sujet : la crise de 1929. Une seule ligne est fausse. Trois, deux, un. »
  { a: ['e8', 0], type: 'manche', n: 2, matiere: 'HISTOIRE', dessin: 'sablier', ch: 2 },
  { a: ['e8', 'sujet'], type: 'erreur', matiere: 'HISTOIRE', sujet: 'La crise de 1929',
    lignes: ['Jeudi 24 octobre 1929 : le jeudi noir.', 'Le Dow Jones tombe de 381 à 41.',
      'Environ 5 000 banques font faillite.', 'Le président Hoover lance le New Deal.'],
    faute: 3, correction: 'Roosevelt, à partir de 1933', chrono: ['e8', 'trois'], rep: ['e9', 0] },
  // e9 « Ligne 4 ! Le New Deal, ce n'est pas Hoover. »
  { a: ['e9', 'ce'], type: 'photo', img: 'hoover', t: 'PAS HOOVER…|ROOSEVELT', sous: 'en route vers l’investiture, 4 mars 1933',
    de: [1.05, .5, .3], vers: [1.25, .55, .25], choc: true },
  // e10 « C'est Roosevelt, élu en 1932, qui le lance en 1933. »
  { a: ['e10', 0], type: 'portrait', img: 'roosevelt', t: 'ROOSEVELT', sous: 'démocrate, élu en 1932' },
  { a: ['e10', '1932'], type: 'jalons', t: 'PAS HOOVER : ROOSEVELT', etapes: [[['e10', '1932'], '1929', 'LE KRACH'], [['e10', 'qui'], '1932', 'ROOSEVELT ÉLU'], [['e10', '1933'], '1933', 'LE NEW DEAL']] },
  // e11 « Secourir, relancer, réformer. »
  { a: ['e11', 0], type: 'fiche', sur: 'LE NEW DEAL', t: '3 VERBES', items: [[['e11', 'secourir'], 'SECOURIR'], [['e11', 'relancer'], 'RELANCER'], [['e11', 'réformer'], 'RÉFORMER']] },
  // e12 « Hoover, lui, était le président du krach de 1929. »
  { a: ['e12', 0], type: 'photo', img: 'wall', t: 'HOOVER|LE PRÉSIDENT DU KRACH', sous: 'Wall Street, octobre 1929', nb: true, de: [1.05, .5, .5], vers: [1.2, .45, .5] },
  // e13 « Dernière manche, la plus dure : la SVT. Courage. »
  { a: ['e13', 0], type: 'mot', t: 'LA PLUS|DURE', sombre: true, choc: true, ch: 3 },
  { a: ['e13', 'svt'], type: 'manche', n: 3, matiere: 'SVT', dessin: 'adn' },
  // e14 « Sujet : la méiose. 4 lignes, une seule fausse. Trois, deux, un. »
  { a: ['e14', 0], type: 'erreur', matiere: 'SVT', sujet: 'La méiose',
    lignes: ['La méiose donne 4 cellules haploïdes.', 'Crossing-over : en prophase I.',
      'Les homologues se séparent en anaphase II.', 'Plus de 8 millions de gamètes possibles.'],
    faute: 2, correction: 'en anaphase I (l’anaphase II : les chromatides)', chrono: ['e14', 'trois'], rep: ['e15', 0] },
  // e15 « Ligne 3 ! Les homologues se séparent en anaphase 1, pas en anaphase 2. »
  // e16 « L'anaphase 2, elle, sépare les chromatides de chaque chromosome. »
  { a: ['e15', 'pas'], type: 'anaphase', e2: ['e16', 0] },
  // e17 « C'est le piège classique de la méiose : retiens-le. »
  { a: ['e17', 0], type: 'photo', img: 'caryotype', t: 'LE PIÈGE|CLASSIQUE', sous: 'des chromosomes humains au microscope', nb: true, de: [1.1, .5, .5], vers: [1.3, .5, .45] },
  // e18 « Alors, combien d'erreurs repérées ? 0, 1, 2 ou 3 ? Dis-le en commentaire. »
  { a: ['e18', 0], type: 'score', n: [['e18', '0'], ['e18', '1'], ['e18', '2'], ['e18', '3']], ch: 4 },
  { a: ['e18', 'dis'], type: 'mot', t: 'DIS-LE EN|COMMENTAIRE' },
  // e19 « Les cours complets sont sur Révisions Animées. »
  { a: ['e19', 0], type: 'chaine', serie: 'Philosophie · Histoire · SVT', fond: 'examen' },
]);
window.CHAPITRES = ['LE DÉFI', 'PHILOSOPHIE', 'HISTOIRE', 'SVT', 'TON SCORE'];
window.IMAGES = {
  examen: '../../philo/serie/img/t-examen.jpg',          // salle d'examen, domaine public
  sartre: '../../philo/serie/img/sartre.jpg',            // Jean-Paul Sartre en 1965, Nationaal Archief / Anefo, CC BY-SA 3.0 NL
  rousseau: '../../philo/serie/img/rousseau.jpg',        // Maurice Quentin de La Tour, Jean-Jacques Rousseau, 1753, domaine public
  contrat: '../../philo/serie/img/t-contrat.jpg',        // Du contrat social, édition originale, Amsterdam, 1762, domaine public
  hoover: '../../dnl/serie/img/h1-hoover-fdr.jpg',       // Hoover et F. D. Roosevelt en route vers l'investiture, 4 mars 1933, Architect of the Capitol, domaine public
  roosevelt: '../../dnl/serie/img/h1-roosevelt-1933.jpg', // Franklin D. Roosevelt, 1933, Elias Goldensky, domaine public
  wall: '../../dnl/serie/img/h1-wallstreet.jpg',         // foule devant la Bourse de New York, octobre 1929, domaine public
  caryotype: '../../svt/serie/img/ch1-caryotype21.jpg',  // chromosomes d'une cellule humaine (47, XY, +21), Josef Reischig, CC BY-SA 3.0
};
