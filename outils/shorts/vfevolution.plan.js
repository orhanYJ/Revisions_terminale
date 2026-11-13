// Découpage du short « 5 affirmations sur l'évolution » (format 4, vrai ou faux), modèle A.
// a: [passage, mot] ; av : avance sur le mot. Chaque affirmation : un plan « vraifaux » (affirmation, chrono, verdict),
// puis deux ou trois plans dessinés pour l'explication.
window.PLAN = S => S.plans([
  // v1 « 5 affirmations sur l'évolution. Combien tu en as justes ? »
  { a: ['v1', 0], av: .25, type: 'cinq', ch: 0 },
  { a: ['v1', 'sur'], type: 'helice' },
  { a: ['v1', 'combien'], type: 'score' },
  // q1 « Un. Tes mitochondries descendent d'une bactérie. Vrai… ou faux ? »
  { a: ['q1', 0], av: .15, type: 'vraifaux', n: '1 / 5', t: 'Tes mitochondries|descendent d’une bactérie', chrono: ['q1', 'vrai'], rep: ['r1', 0], v: true, expl: 'C’est l’endosymbiose', ch: 1 },
  // r1 « Vrai ! Une bactérie avalée par une cellule, mais jamais digérée. La preuve : ses deux membranes. »
  { a: ['r1', 'avalée'], type: 'phago' },
  { a: ['r1', 'mais'], type: 'phago', etape: 2 },
  { a: ['r1', 'la'], type: 'portrait', img: 'mito', t: '2 MEMBRANES', sous: 'mitochondries au microscope' },
  // q2 « Deux. Les bactéries mutent pour résister aux antibiotiques. Vrai… ou faux ? »
  { a: ['q2', 0], av: .15, type: 'vraifaux', n: '2 / 5', t: 'Les bactéries mutent|pour résister|aux antibiotiques', chrono: ['q2', 'vrai'], rep: ['r2', 0], v: false, expl: 'Le hasard d’abord, le tri ensuite', ch: 2 },
  // r2 « Faux ! Les mutations arrivent au hasard, avant. L'antibiotique sélectionne celles qui résistaient déjà. »
  { a: ['r2', 'mutations'], av: -.44, type: 'bacteries' },
  { a: ['r2', "l'antibiotique"], type: 'bacteries', etape: 2, choc: true },
  { a: ['r2', 'résistaient'], av: .15, type: 'portrait', img: 'antibio', t: 'DÉJÀ RÉSISTANTES', sous: 'pas de halo : la souche résiste' },
  // q3 « Trois. Une population peut évoluer par pur hasard. Vrai… ou faux ? »
  { a: ['q3', 0], av: .15, type: 'vraifaux', n: '3 / 5', t: 'Une population|peut évoluer|par pur hasard', chrono: ['q3', 'vrai'], rep: ['r3', 0], v: true, expl: 'C’est la dérive génétique' },
  // r3 « Vrai ! C'est la dérive. En 1956, Buri suit 107 populations de 16 drosophiles, sans aucune sélection. »
  { a: ['r3', 'en'], type: 'date', t: '1956', de: 1900, sous: 'L’EXPÉRIENCE DE BURI' },
  { a: ['r3', '107'], type: 'tubes', etape: 1 },
  { a: ['r3', 'sans'], type: 'portrait', img: 'drosophile', t: 'SANS SÉLECTION', sous: 'rien que le hasard' },
  // r3b « 19 générations plus tard, l'allèle a disparu de beaucoup d'entre elles. Dans d'autres, il est le seul. »
  { a: ['r3b', 0], type: 'tubes', etape: 2 },
  { a: ['r3b', 'disparu'], type: 'tubes', etape: 3, choc: true },
  { a: ['r3b', 'dans'], type: 'tubes', etape: 4 },
  // q4 « Quatre. Deux animaux qui se ressemblent sont forcément de la même espèce. Vrai… ou faux ? »
  { a: ['q4', 0], av: .15, type: 'vraifaux', n: '4 / 5', t: 'Deux animaux|qui se ressemblent|sont forcément|de la même espèce', chrono: ['q4', 'vrai'], rep: ['r4', 0], v: false, expl: 'La ressemblance peut tromper', ch: 3 },
  // r4 « Faux ! Deux fourmis des bois ont longtemps été confondues. En 1996, leur ADN a révélé deux espèces. »
  { a: ['r4', 'deux'], av: -.5, type: 'fourmis', etape: 0 },
  { a: ['r4', 'longtemps'], type: 'fourmis', etape: 1 },
  { a: ['r4', 'en'], type: 'date', t: '1996', de: 1950, sous: 'LE CRITÈRE MOLÉCULAIRE' },
  { a: ['r4', 'leur'], type: 'fourmis', etape: 2, choc: true },
  // q5 « Cinq. Une bactérie peut donner un gène à une bactérie d'une autre espèce. Vrai… ou faux ? »
  { a: ['q5', 0], av: .15, type: 'vraifaux', n: '5 / 5', t: 'Une bactérie peut donner|un gène à une bactérie|d’une autre espèce', chrono: ['q5', 'vrai'], rep: ['r5', 0], v: true, expl: 'C’est un transfert horizontal' },
  // r5 « Vrai ! Un pont se forme, une copie d'ADN passe. C'est ainsi que voyagent les résistances. »
  { a: ['r5', 'un'], av: -.45, type: 'conjugaison', etape: 1 },
  { a: ['r5', 'une'], type: 'conjugaison', etape: 2 },
  { a: ['r5', "c'est"], type: 'resist' },
  // fin « Alors, combien tu en as justes ? Dis ton score en commentaire. »
  { a: ['fin', 0], type: 'score', etape: 2, ch: 4 },
  { a: ['fin', 'dis'], type: 'commentaire' },
  // ch « Tout le cours est sur Révisions Animées. »
  { a: ['ch', 0], type: 'chaine', serie: 'SVT · Génétique et évolution', fond: 'drosophile' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA CELLULE', 'SÉLECTION ET HASARD', 'ESPÈCES ET GÈNES', 'TON SCORE'];
window.MUSIQUE = 'quiz';
window.IMAGES = {
  mito: '../../svt/serie/img/ch2-mito.jpg',              // deux mitochondries, poumon de mammifère, microscope électronique, Louisa Howard, domaine public
  antibio: '../../svt/serie/img/ch2-antibio.jpg',        // antibiogrammes de Staphylococcus aureus, HansN., CC BY-SA 4.0
  drosophile: '../../svt/serie/img/ch3-drosophile.jpg',  // Drosophila melanogaster, photo André Karwath, CC BY-SA 2.5
};
