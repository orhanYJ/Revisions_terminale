// Découpage du short « SES : plus ou moins ? » (format « le spectateur joue », plan plusmoins), modèle A, habillage jeu.
// a: [passage, mot] ; av : avance sur le mot. Chaque duel : un carton « duel », un plan qui pose la valeur A, le plan
// plusmoins (A donné, B caché, chrono silencieux ou « Trois, deux, un », B qui défile), puis un plan d'explication.
// Le plan plusmoins arrondit à l'unité (7,7 → 8 %) : la voix dit « près de » ou « environ ».
window.PLAN = S => S.plans([
  // h1 « SES : plus ou moins ? 4 chiffres surprenants. »
  { a: ['h1', 0], av: .25, type: 'titre', ch: 0 },
  { a: ['h1', '4'], type: 'collage', imgs: ['usine', 'ecrans', 'examen', 'yangshan'], couleur: true, t: '4 CHIFFRES|DE SES' },
  // h2 « Compte tes bonnes réponses. »
  { a: ['h2', 0], type: 'score', etape: 0 },
  // d1a « Duel 1 : le travail. »
  { a: ['d1a', 0], type: 'duel', n: 1, matiere: 'LE TRAVAIL', img: 'usine', ch: 1 },
  // d1b « En 1975, l'industrie fait 29 pour cent des emplois en France. »
  { a: ['d1b', 0], type: 'date', t: '1975', de: 1950, sous: 'INDUSTRIE : 29 % DES EMPLOIS' },
  // d1c « Et en 2024 : plus ou moins ? » (silence : chrono) — r1 « Moins : environ 13 pour cent ! »
  { a: ['d1b', '29'], type: 'mot', t: '29 %|DES EMPLOIS' },
  { a: ['d1c', 0], type: 'plusmoins', q: 'PART DE L’INDUSTRIE DANS L’EMPLOI',
    A: { t: 'France, 1975', img: 'usine', v: 29, u: '%' }, B: { t: 'France, 2024', img: 'ecrans', v: 12.6, u: '%' },
    chrono: ['d1c', -1], rep: ['r1', 0] },
  // r1 « … Les emplois passent aux services : c'est la tertiarisation. »
  { a: ['r1', 'les'], type: 'tertiaire' },
  // d2a « Duel 2 : le chômage. »
  { a: ['d2a', 0], type: 'duel', n: 2, matiere: 'LE CHÔMAGE', img: 'examen', ch: 2 },
  // d2b « En 2025, le taux de chômage en France est de près de 8 pour cent. »
  { a: ['d2b', 0], type: 'date', t: '2025', de: 2000, sous: 'FRANCE' },
  { a: ['d2b', 'taux'], type: 'thermo' },
  // d2c « Et chez les 15 à 24 ans ? » (silence : chrono) — r2 « Plus : près de 20 pour cent ! »
  { a: ['d2c', 0], type: 'plusmoins', q: 'TAUX DE CHÔMAGE EN 2025',
    A: { t: 'Tous les actifs', v: 7.7, u: '%' }, B: { t: 'Les 15 à 24 ans', img: 'examen', v: 19.8, u: '%' },
    chrono: ['d2c', -1], rep: ['r2', 0] },
  // r2 « … Attention, c'est un taux : on divise par les jeunes actifs, pas par tous les jeunes. »
  { a: ['r2', 'attention'], type: 'taux' },
  // d3a « Duel 3 : les inégalités. »
  { a: ['d3a', 0], type: 'duel', n: 3, matiere: 'LES INÉGALITÉS', icone: 'balance', ch: 3 },
  // d3b « En 1995, dans le privé, les femmes gagnent en moyenne 34 pour cent de moins que les hommes. »
  { a: ['d3b', 0], type: 'mot', t: 'SECTEUR|PRIVÉ' },
  { a: ['d3b', 'femmes'], type: 'balance' },
  // d3c « Et en 2024 ? » — c3 « Trois, deux, un. » (chrono dans la voix) — r3 « Moins : environ 22 pour cent. »
  { a: ['d3c', 0], type: 'plusmoins', q: 'ÉCART DE REVENU SALARIAL FEMMES-HOMMES',
    A: { t: 'Secteur privé, 1995', v: 33.7, u: '%' }, B: { t: 'Secteur privé, 2024', v: 21.8, u: '%' },
    chrono: ['c3', 0], rep: ['r3', 0] },
  // r3 « … Et même à temps de travail égal, l'écart reste de 14 pour cent. »
  { a: ['r3', 'et'], type: 'barres' },
  // d4a « Dernier duel : la mondialisation. »
  { a: ['d4a', 0], type: 'duel', n: 4, matiere: 'LA MONDIALISATION', img: 'yangshan', choc: true, ch: 4 },
  // d4b « En 1983, la Chine pèse à peine plus de 1 pour cent des exportations mondiales. En 2024 ? »
  { a: ['d4b', 0], type: 'date', t: '1983', de: 1950, sous: 'CHINE' },
  { a: ['d4b', 'pèse'], type: 'camembert' },
  { a: ['d4b', '2024'], type: 'plusmoins', q: 'PART DE LA CHINE DANS LES EXPORTATIONS MONDIALES',
    A: { t: 'Chine, 1983', v: 1.2, u: '%' }, B: { t: 'Chine, 2024', img: 'yangshan', v: 14.6, u: '%' },
    chrono: ['d4b', -1], rep: ['r4', 0] },
  // r4 « Plus : près de 15 pour cent ! Premier exportateur du monde. »
  { a: ['r4', 'premier'], type: 'photo', img: 'yangshan', t: 'N° 1|MONDIAL', sous: 'premier exportateur de marchandises (OMC, 2024)', de: [1.05, .5, .5], vers: [1.25, .55, .45], choc: true },
  // f1 « Alors, combien de bonnes réponses ? Dis-le en commentaire. »
  { a: ['f1', 0], type: 'score', etape: 1 },
  { a: ['f1', 'dis-le'], type: 'commentaire' },
  // f2 « Plus de défis sur Révisions Animées. »
  { a: ['f2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'yangshan' },
]);
window.CHAPITRES = ['ACCROCHE', 'DUEL TRAVAIL', 'DUEL CHÔMAGE', 'DUEL INÉGALITÉS', 'DUEL MONDIALISATION'];
window.THEME = 'jeu';
window.MUSIQUE = 'automotivo';
window.IMAGES = {
  usine: '../../philo/serie/img/t3-usine.jpg',     // Adolph von Menzel, La Forge (Le Laminoir), 1872-1875, domaine public
  ecrans: '../../philo/serie/img/t-ecrans.jpg',    // personnes devant des écrans, photo Rawpixel, CC BY 2.0
  examen: '../../philo/serie/img/t-examen.jpg',    // salle d'examen, domaine public
  yangshan: 'img/ses-yangshan.jpg',                // port à conteneurs de Yangshan, Shanghai, 2013, photo Bruno Corpet (Quoique), CC BY-SA 3.0 (Wikimedia Commons)
};
