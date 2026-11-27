// Découpage du short « SES : trouve l'intrus » (format « le spectateur joue », plan intrus), modèle A, habillage alerte.
// a: [passage, mot] ; av : avance sur le mot. Chaque manche : un carton « manche », le plan intrus (options, chrono
// silencieux sur le dernier mot de la question, ou « Trois, deux, un » à la dernière manche, verdict), puis deux plans
// d'explication de types différents.
window.PLAN = S => S.plans([
  // h1 « SES : trouve l'intrus. 4 manches, de plus en plus dures. »
  { a: ['h1', 0], av: .25, type: 'titre', ch: 0 },
  { a: ['h1', '4'], type: 'collage', imgs: ['smith', 'lehman', 'keynes', 'petrole'], t: '4 MANCHES|DE SES' },
  // h2 « Combien tu en trouves ? »
  { a: ['h2', 0], type: 'score', etape: 0 },
  // m1a « Manche 1 : les auteurs. »
  { a: ['m1a', 0], type: 'manche', n: 1, t: 'LES|AUTEURS', img: 'smith', ch: 1 },
  // m1b « Trois sont économistes. Un seul est sociologue. » (silence : chrono) — r1 « L'intrus : Durkheim … »
  { a: ['m1b', 0], type: 'intrus', sur: '3 ÉCONOMISTES, 1 SOCIOLOGUE',
    options: [{ t: 'Smith', img: 'smith', sous: '1723 – 1790', nb: true }, { t: 'Keynes', img: 'keynes', sous: '1883 – 1946', nb: true },
      { t: 'Durkheim', img: 'durkheim', sous: '1858 – 1917', nb: true }, { t: 'Ricardo', img: 'ricardo', sous: '1772 – 1823', nb: true }],
    intrus: 2, chrono: ['m1b', -1], rep: ['r1', 0], expl: 'Un des pères de la sociologie' },
  { a: ['r1', 'un'], type: 'portrait', img: 'durkheim', t: 'DURKHEIM', sous: 'Les Règles de la méthode sociologique, 1895' },
  // e1 « Smith, Ricardo et Keynes, eux, sont économistes. Ricardo explique le commerce international par les avantages comparatifs. »
  { a: ['e1', 0], type: 'collage', imgs: ['smith', 'ricardo', 'keynes'], t: 'TROIS|ÉCONOMISTES' },
  { a: ['e1', 'explique'], type: 'ricardo' },
  // m2a « Manche 2 : la structure sociale. »
  { a: ['m2a', 0], type: 'manche', n: 2, t: 'STRUCTURE|SOCIALE', img: 'raboteurs', ch: 2 },
  // m2b « Trois sont des groupes de l'INSEE. Un seul n'en est pas un. » (silence : chrono) — r2 « Les classes moyennes ! »
  { a: ['m2b', 0], type: 'intrus', sur: 'LEQUEL N’EST PAS UN GROUPE INSEE ?',
    options: [{ t: 'Agriculteurs', img: 'labourage', sous: 'exploitants' }, { t: 'Classes moyennes', img: 'rue', sous: 'ni en haut, ni en bas' },
      { t: 'Ouvriers', img: 'raboteurs', sous: 'qualifiés ou non' }, { t: 'Artisans', img: 'boulanger', sous: 'et commerçants' }],
    intrus: 1, chrono: ['m2b', -1], rep: ['r2', 0], expl: 'Une notion débattue, pas une case de l’INSEE' },
  // r2 « … L'INSEE classe les actifs en 6 groupes socioprofessionnels. »
  { a: ['r2', "l'insee"], type: 'pcs' },
  // e2 « Les classes moyennes, elles, font débat chez les sociologues. »
  { a: ['e2', 0], type: 'mot', img: 'rue', t: 'CLASSES|MOYENNES', sous: 'un débat de sociologues' },
  // m3a « Manche 3 : les crises. »
  { a: ['m3a', 0], type: 'manche', n: 3, t: 'LES|CRISES', img: 'wallstreet', ch: 3 },
  // m3b « Trois sont des crises financières. Une seule n'en est pas une. » (silence : chrono) — r3 « Le choc pétrolier de 1973 ! »
  { a: ['m3b', 0], type: 'intrus', sur: 'LEQUEL N’EST PAS UNE CRISE FINANCIÈRE ?',
    options: [{ t: 'Subprimes', img: 'lehman', sous: '2008' }, { t: 'Krach', img: 'wallstreet', sous: '1929', nb: true },
      { t: 'Bulle internet', img: 'nasdaq', sous: '2000' }, { t: 'Choc pétrolier', img: 'petrole', sous: '1973' }],
    intrus: 3, chrono: ['m3b', -1], rep: ['r3', 0], expl: 'Une crise du pétrole, pas de la finance' },
  // r3 « … Le prix du baril est multiplié par 4. »
  { a: ['r3', 'prix'], type: 'baril' },
  // e3 « C'est un choc d'offre. En 2008, c'est la faillite d'une banque, Lehman Brothers, qui sème la panique. »
  { a: ['e3', 0], type: 'mot', t: 'UN CHOC|D’OFFRE', choc: true },
  { a: ['e3', '2008'], type: 'photo', img: 'lehman', t: 'LEHMAN|BROTHERS', sous: '15 septembre 2008 : la faillite', de: [1.05, .5, .45], vers: [1.25, .5, .3] },
  { a: ['e3', 'sème'], type: 'tampon', t: 'PANIQUE', choc: true },
  // m4 « Dernière manche, la plus dure ! Trois causes de chômage structurel, une seule de chômage conjoncturel. »
  { a: ['m4', 0], type: 'manche', n: 4, t: 'DERNIÈRE|MANCHE', icone: 'feu', choc: true, ch: 4 },
  // … c4 « Trois, deux, un. » (chrono dans la voix) — r4 « La chute de la demande ! »
  { a: ['m4', 'trois'], type: 'intrus', sur: '3 STRUCTURELS, 1 CONJONCTUREL',
    options: [{ t: 'Chute de la demande', sous: 'l’activité ralentit' }, { t: 'Frictions', sous: 'le temps de chercher' },
      { t: 'Qualifications', sous: 'inadaptées aux postes' }, { t: 'Salaire d’efficience', sous: 'asymétrie d’information' }],
    intrus: 0, chrono: ['c4', 0], rep: ['r4', 0], expl: 'Elle suit la conjoncture' },
  // r4 « … Quand l'activité ralentit, le chômage monte. »
  { a: ['r4', 'quand'], type: 'conjoncture' },
  // e4 « Frictions, qualifications inadaptées, salaire d'efficience : ces causes-là sont durables. »
  { a: ['e4', 0], type: 'fiche', sur: 'CHÔMAGE STRUCTUREL', t: 'DURABLE',
    items: [[['e4', 'frictions'], 'Frictions', 'appariement : le temps de chercher'], [['e4', 'qualifications'], 'Qualifications inadaptées', 'appariement'],
      [['e4', 'salaire'], 'Salaire d’efficience', 'asymétrie d’information']] },
  // f1 « Alors, combien d'intrus trouvés ? Dis-le en commentaire. »
  { a: ['f1', 0], type: 'score', etape: 1 },
  { a: ['f1', 'dis-le'], type: 'commentaire' },
  // f2 « Plus de défis sur Révisions Animées. »
  { a: ['f2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'keynes' },
]);
window.CHAPITRES = ['ACCROCHE', 'LES AUTEURS', 'LA STRUCTURE SOCIALE', 'LES CRISES', 'DERNIÈRE MANCHE'];
window.THEME = 'alerte';
window.MUSIQUE = 'montagem3';
window.IMAGES = {
  smith: 'img/ses-smith.jpg',            // Adam Smith, « The Muir portrait », auteur inconnu, XVIIIe siècle, domaine public (Wikimedia Commons)
  ricardo: 'img/ses-ricardo.jpg',        // David Ricardo par Thomas Phillips, vers 1821, domaine public (Wikimedia Commons)
  keynes: 'img/ses-keynes.jpg',          // John Maynard Keynes, 1929, photographe inconnu (Bettmann Archive), domaine public (Wikimedia Commons)
  durkheim: '../../philo/serie/img/durkheim.jpg',  // Émile Durkheim, photographie, domaine public
  lehman: 'img/ses-lehman.jpg',          // siège de Lehman Brothers, Times Square, photo David Shankbone, CC BY-SA 3.0 (Wikimedia Commons)
  nasdaq: 'img/ses-nasdaq.jpg',          // Nasdaq MarketSite, Times Square, photo ajay_suresh, CC BY 2.0 (Wikimedia Commons)
  petrole: 'img/ses-petrole.jpg',        // drapeaux de rationnement dans une station-service, Oregon, 1973, photo David Falconer, domaine public (NARA, Wikimedia Commons)
  wallstreet: '../../dnl/serie/img/h1-wallstreet.jpg',  // foule devant la Bourse de New York, octobre 1929, domaine public
  labourage: '../../philo/serie/img/et2-labourage.jpg', // Rosa Bonheur, Labourage nivernais, 1849 (musée d'Orsay), domaine public
  raboteurs: '../../philo/serie/img/dv3-raboteurs.jpg', // Gustave Caillebotte, Les Raboteurs de parquet, 1875 (musée d'Orsay), domaine public
  boulanger: '../../philo/serie/img/dv6-boulanger.jpg', // Jan Steen, Le Boulanger Arent Oostwaert et sa femme, vers 1658 (Rijksmuseum), domaine public
  rue: '../../philo/serie/img/t3-rue.jpg',              // Gustave Caillebotte, Rue de Paris, temps de pluie, 1877 (Art Institute of Chicago), domaine public
};
