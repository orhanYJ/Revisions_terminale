// Découpage du short « Vrai ou faux : les océans », modèle A. a: [passage, mot] ; av : avance sur le mot.
// Les plans vraifaux (formats-a.js) durent de l'affirmation au verdict ; les plans dessinés illustrent l'explication.
window.PLAN = S => S.plans([
  // v1 « 5 affirmations sur les océans. Combien tu en as justes ? »
  { a: ['v1', 0], av: .25, type: 'mot', t: '5 AFFIRMATIONS', ch: 0 },
  { a: ['v1', 'sur'], type: 'archive', img: 'mer', t: 'SUR LES|OCÉANS', legende: 'Henry Dawson, Navires sur une mer calme au crépuscule, XIXᵉ siècle' },
  { a: ['v1', 'combien'], type: 'mot', t: 'COMBIEN TU EN|AS JUSTES ?', choc: true },
  // v2 « Top chrono. »
  { a: ['v2', 0], type: 'chrono' },
  // a1 / b1 : les marchandises voyagent par la mer (FAUX)
  { a: ['a1', 0], type: 'vraifaux', n: '1 / 5', t: 'La plupart des marchandises|voyagent en avion', chrono: ['a1', 'vrai'], rep: ['b1', 0], v: false,
    expl: 'Elles voyagent par la mer', ch: 1 },
  { a: ['b1', 'la'], type: 'part' },
  // a2 / b2 : l'Ever Given bloque le canal de Suez (VRAI)
  { a: ['a2', 0], type: 'vraifaux', n: '2 / 5', t: 'En 2021, un seul navire|a bloqué le canal de Suez', chrono: ['a2', 'vrai'], rep: ['b2', 0], v: true,
    expl: 'L’Ever Given, le 23 mars 2021' },
  { a: ['b2', "l'ever"], type: 'eiffel' },
  { a: ['b2', 'se'], type: 'suez' },
  { a: ['b2', 'commerce'], type: 'mot', t: 'COMMERCE ASIE-EUROPE|PARALYSÉ', choc: true },
  // a3 / b3 : Internet passe par des câbles sous-marins (FAUX)
  { a: ['a3', 0], type: 'vraifaux', n: '3 / 5', t: 'Internet traverse les océans|grâce aux satellites', chrono: ['a3', 'vrai'], rep: ['b3', 0], v: false,
    expl: 'Par des câbles sous-marins', ch: 2 },
  { a: ['b3', 'il'], type: 'cable' },
  { a: ['b3', "c'est"], type: 'mot', t: 'LE PLUS|RAPIDE' },
  { a: ['b3', 'et'], type: 'mot', t: 'ET LE MOINS|CHER' },
  // a4 / b4 : l'Arctique n'est pas ouvert toute l'année (FAUX)
  { a: ['a4', 0], type: 'archive', img: 'iceberg', t: 'AVEC LE|RÉCHAUFFEMENT…', legende: 'Iceberg tabulaire, photo NOAA, domaine public', ch: 3 },
  { a: ['a4', "l'arctique"], type: 'vraifaux', n: '4 / 5', t: 'L’Arctique est ouvert|aux navires toute l’année', chrono: ['a4', 'vrai'], rep: ['b4', 0], v: false,
    expl: 'Peu de temps, à la fin de l’été' },
  { a: ['b4', 'ses'], type: 'saisons' },
  { a: ['b4', 'et'], type: 'brise' },
  // a5 / b5 : la France, deuxième espace maritime du monde (VRAI)
  { a: ['a5', 0], type: 'vraifaux', n: '5 / 5', t: 'La France a le 2e plus grand|espace maritime du monde', chrono: ['a5', 'vrai'], rep: ['b5', 0], v: true,
    expl: 'Sa ZEE : la 2e du monde', ch: 4 },
  { a: ['b5', 'grâce'], type: 'zee' },
  { a: ['b5', 'dépasse'], type: 'km2', choc: true },
  // e1 « Alors, ton score ? Dis-le en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS, TON|SCORE ?' },
  { a: ['e1', 'dis-le'], type: 'commentaire' },
  // e2 « Le cours complet est sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Géographie · Espaces maritimes', fond: 'mer' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE COMMERCE', 'LES CÂBLES', 'L’ARCTIQUE', 'LA FRANCE · TON SCORE'];
window.IMAGES = {
  mer: '../../philo/serie/img/bh2-mer.jpg',          // Henry Dawson, Navires sur une mer calme au crépuscule, XIXe siècle, domaine public
  iceberg: '../../philo/serie/img/t3-iceberg.jpg',   // iceberg tabulaire, photo NOAA, domaine public
};
window.MUSIQUE = 'quiz';   // musique imposée pour ce short
