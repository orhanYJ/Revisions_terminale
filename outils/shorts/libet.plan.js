// Découpage du short « Ton cerveau décide avant toi » : un plan par changement d'image, calé sur un mot dit
// (a: [passage, mot]). Le type dit QUOI montrer ; chaque modèle (A, B, C) dit COMMENT.
window.PLAN = S => S.plans([
  // s1 « Avant même que tu décides… ton cerveau s'est déjà mis en marche. »
  { a: ['s1', 0], av: .25, type: 'mot', t: 'AVANT', sous: 'même que tu décides…', img: 'penseur', ch: 0 },
  { a: ['s1', 'cerveau'], type: 'cerveau', t: 'TON CERVEAU' },
  { a: ['s1', 'marche'], type: 'tampon', t: 'DÉJÀ EN MARCHE', choc: true },
  // s2 « En 1983, le neuroscientifique américain Benjamin Libet tente une expérience toute simple. »
  { a: ['s2', 0], type: 'date', t: '1983', de: 1900, ch: 1 },
  { a: ['s2', 'neuroscientifique'], type: 'perso', t: 'BENJAMIN LIBET', sous: 'neuroscientifique · États-Unis', img: 'neurones' },
  { a: ['s2', 'expérience'], type: 'mot', t: "L'EXPÉRIENCE", sous: 'toute simple' },
  // s3 « Plie le poignet, quand tu veux. Et sur cette horloge, note l'instant exact où l'envie te prend. »
  { a: ['s3', 0], type: 'poignet', t: 'PLIE LE POIGNET' },
  { a: ['s3', 'quand'], type: 'mot', t: 'QUAND TU VEUX', petit: true },
  { a: ['s3', 'horloge'], type: 'horloge', t: "L'HORLOGE" },
  { a: ['s3', 'instant'], type: 'horloge', t: "NOTE L'INSTANT", fige: true },
  // s4 « Pendant ce temps, des électrodes écoutent ton cerveau. »
  { a: ['s4', 0], type: 'eeg', t: 'ÉLECTRODES', img: 'vesale' },
  // s5 « Résultat ? Une activité cérébrale démarre une demi-seconde avant le geste. »
  { a: ['s5', 0], type: 'mot', t: 'RÉSULTAT ?', choc: true, ch: 2 },
  { a: ['s5', 1], type: 'frise', etape: 1 },
  // s6 « Mais l'envie de bouger, tu ne la sens que deux dixièmes de seconde avant. »
  { a: ['s6', 0], type: 'frise', etape: 2 },
  // s7 « Pendant trois dixièmes de seconde… ton cerveau travaille sans toi. »
  { a: ['s7', 0], type: 'frise', etape: 3 },
  { a: ['s7', 'ton'], type: 'mot', t: 'SANS TOI', choc: true, sombre: true },
  // s8 « Spinoza l'écrivait déjà au dix-septième siècle : une pierre qu'on lance, si elle pouvait penser,
  //      croirait qu'elle vole parce qu'elle le veut. »
  { a: ['s8', 0], type: 'portrait', t: 'SPINOZA', sous: '1632 – 1677', img: 'spinoza', ch: 3 },
  { a: ['s8', 'pierre'], type: 'pierre', etape: 1 },
  { a: ['s8', 'croirait'], type: 'pierre', etape: 2, bulle: '« Je vole parce que je le veux »' },
  // s9 « Nous sommes pareils : on se croit libre… parce qu'on ignore les causes qui nous font agir. »
  { a: ['s9', 0], type: 'mot', t: 'NOUS SOMMES PAREILS', img: 'penseur' },
  { a: ['s9', 'parce'], type: 'causes', t: 'LES CAUSES', sous: "qu'on ignore" },
  // s10 « Alors, le libre arbitre, une illusion ? Pas si vite. »
  { a: ['s10', 'libre'], type: 'mot', t: 'LIBRE ARBITRE', t2: 'ILLUSION ?', a2: ['s10', 'illusion'], ch: 4 },
  { a: ['s10', 'pas'], type: 'stop', t: 'PAS SI VITE', choc: true },
  // s11 « Libet lui-même te laisse un pouvoir : celui de dire non. Un veto, au dernier moment. »
  { a: ['s11', 0], type: 'frise', etape: 4 },
  { a: ['s11', 'non'], type: 'tampon', t: 'NON.', choc: true },
  { a: ['s11', 'veto'], type: 'frise', etape: 5 },
  // s12 « Et depuis, des chercheurs soupçonnent que ce signal n'est peut-être qu'un bruit de fond du cerveau. »
  { a: ['s12', 0], type: 'eeg', bruit: true, t: 'UN SIGNAL ?' },
  { a: ['s12', 'bruit'], type: 'mot', t: 'BRUIT DE FOND ?', bruit: true },
  // s13 « Libre ou pas ? C'est une vraie question de bac. La réponse complète est sur Révisions Animées. »
  { a: ['s13', 0], type: 'mot', t: 'LIBRE', t2: 'OU PAS ?', a2: ['s13', 'ou'], choc: true },
  { a: ['s13', 'question'], type: 'bac' },
  { a: ['s13', 'réponse'], type: 'chaine' },
  // s14 « Et toi… tu es sûr que c'est toi qui décides ? » (boucle vers le début)
  { a: ['s14', 0], type: 'mot', t: 'ET TOI…', t2: 'TU ES SÛR ?', a2: ['s14', 'sûr'], img: 'penseur', fin: true },
]);
// chapitres (barre de progression du modèle B)
window.CHAPITRES = ['ACCROCHE', "L'EXPÉRIENCE", 'RÉSULTAT', 'SPINOZA', 'VERDICT'];
window.IMAGES = {
  penseur: '../../philo/serie/img/t-penseur.jpg',      // Rodin, photo Jebulon, CC0
  neurones: '../../philo/serie/img/cs1-neurones.jpg',  // Ramón y Cajal, domaine public
  vesale: '../../philo/serie/img/t3-vesale.jpg',       // Vésale, Wellcome Collection, CC BY 4.0
  spinoza: '../../philo/serie/img/spinoza.jpg',        // portrait, domaine public
};
