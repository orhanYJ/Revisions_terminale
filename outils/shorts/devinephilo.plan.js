// Découpage du short « devinephilo » (format `devine` : « Devine le philosophe en 3 indices »), modèle A,
// habillage « terminal » (dossier secret). a: [passage, mot] ; av : avance sur le mot (négative = après le mot).
// Chaque manche : le dossier qui s'ouvre, le plan `devine` (portrait pixellisé qui se précise à chaque indice), une image
// pendant l'un des indices, le même plan `devine` pour le dernier indice, le silence et la révélation, puis une image de liaison.
const D1 = { type: 'devine', img: 'socrate', sur: 'DOSSIER 1 · QUI EST-CE ?', rep: ['c1', "c'est"], nom: 'SOCRATE',
  sous: 'v. 470 – 399 av. J.-C.|« Une vie sans examen n’est pas une vie »',
  indices: [[['a1', 'premier'], 'Une voix intérieure lui dit « arrête »'], [['a1', 'deuxième'], 'Sa devise : « connais-toi toi-même »'],
    [['b1', 'dernier'], 'Condamné à mort à Athènes (399 av. J.-C.)']] };
const D2 = { type: 'devine', img: 'spinoza', sur: 'DOSSIER 2 · QUI EST-CE ?', rep: ['c2', "c'est"], nom: 'SPINOZA',
  sous: '1632 – 1677|On se croit libre : on ignore les causes',
  indices: [[['a2', 'premier'], 'Il polit des verres de lunettes'], [['a2', 'deuxième'], 'Chassé de sa communauté à 23 ans'],
    [['b2', 'dernier'], 'La pierre qui se croirait libre']] };
const D3 = { type: 'devine', img: 'kant', sur: 'DOSSIER 3 · QUI EST-CE ?', rep: ['c3', "c'est"], nom: 'KANT',
  sous: '1724 – 1804|Une règle qui vaut pour tous',
  indices: [[['a3', 'premier'], 'Il enseigne à Königsberg'], [['a3', 'deuxième'], 'Mentir ? Jamais, même à un assassin'],
    [['b3', 'dernier'], 'Il invente l’impératif catégorique']] };
const dv = (D, o) => Object.assign({}, D, o);
window.PLAN = S => S.plans([
  // h1 « Devine le philosophe en 3 indices. »
  { a: ['h1', 0], av: .2, type: 'dossiers', ch: 0 },
  // h2 « Le plus dur d'abord. Trouve-le le plus tôt possible ! »
  { a: ['h2', 0], type: 'photo', img: 'athenes', t: 'LE PLUS DUR|D’ABORD', de: [1.0, .5, .45], vers: [1.15, .5, .4] },
  { a: ['h2', 'trouve-le'], type: 'scanner' },

  // a1 « Dossier 1. Accès autorisé. Premier indice : … Deuxième indice : … » ; b1 « Dernier indice : … » ; c1 « C'est Socrate ! … »
  { a: ['a1', 0], type: 'dossier', n: 1, ch: 1 },
  dv(D1, { a: ['a1', 'premier'] }),
  { a: ['b1', 0], type: 'mot', img: 'acropole', t: 'ATHÈNES,|399 AV. J.-C.' },
  dv(D1, { a: ['b1', -1], av: -.4 }),
  { a: ['c1', 'sans'], type: 'photo', img: 'mortsocrate', t: 'UNE VIE SANS EXAMEN|N’EST PAS UNE VIE', de: [1.0, .6, .45], vers: [1.12, .6, .4], legende: 'Jacques-Louis David, La Mort de Socrate, 1787' },

  // a2 « Dossier 2. … » ; b2 « Dernier indice : une pierre lancée, si elle pensait, se croirait libre. » ; c2 « C'est Spinoza ! … »
  { a: ['a2', 0], type: 'dossier', n: 2, ch: 2 },
  dv(D2, { a: ['a2', 'premier'] }),
  { a: ['b2', 0], type: 'pierre', etape: 2, bulle: '« Je suis libre ! »' },
  dv(D2, { a: ['b2', -1], av: -.4 }),
  { a: ['c2', 'parce'], type: 'photo', img: 'exclu', t: 'ON SE CROIT LIBRE…|ON IGNORE LES CAUSES', de: [1.0, .4, .5], vers: [1.12, .42, .45], legende: 'Samuel Hirszenberg, Spinoza excommunié, 1907' },

  // a3 « Dossier 3, le dernier. … » ; b3 « Dernier indice : il invente l'impératif catégorique. » ; c3 « C'est Kant ! … »
  { a: ['a3', 0], type: 'dossier', n: 3, ch: 3, choc: true },
  dv(D3, { a: ['a3', 'premier'] }),
  { a: ['a3', 'deuxième'], type: 'photo', img: 'portes', t: 'UN ASSASSIN|À TA PORTE', de: [1.0, .5, .5], vers: [1.15, .55, .5], nb: true, legende: 'Vilhelm Hammershøi, Portes blanches, 1913' },
  dv(D3, { a: ['b3', 0] }),
  { a: ['c3', 'qui'], type: 'collage', imgs: ['kant', 'grundlegung', 'konigsberg'], t: 'UNE LOI|UNIVERSELLE' },

  // o1 « Combien tu en as trouvé ? Dis-le en commentaire. »
  { a: ['o1', 0], type: 'score', ch: 4, choc: true, dis: ['o1', 'dis-le'] },
  // o2 « Les 3 sont expliqués dans les séries philo de Révisions Animées. »
  { a: ['o2', 0], type: 'trio' },
  { a: ['o2', 'séries'], type: 'chaine', serie: 'Philosophie', fond: 'penseur' },
  // o3 « Et le prochain dossier… tu le trouves en combien d'indices ? » (relance le jeu du début)
  { a: ['o3', 0], type: 'dossiers', fin: true },
]);
window.CHAPITRES = ['ACCROCHE', 'DOSSIER 1', 'DOSSIER 2', 'DOSSIER 3', 'TON SCORE'];
window.IMAGES = {
  socrate: '../../philo/serie/img/socrate.jpg',             // buste, copie romaine d'après Lysippe, musée du Louvre, domaine public
  spinoza: '../../philo/serie/img/spinoza.jpg',             // portrait anonyme, vers 1665, domaine public
  kant: '../../philo/serie/img/kant.jpg',                   // portrait anonyme, XVIIIe s., domaine public
  athenes: '../../philo/serie/img/t-athenes.jpg',           // Raphaël, L'École d'Athènes, 1509-1511, domaine public
  acropole: '../../philo/serie/img/t-acropole.jpg',         // Leo von Klenze, l'Acropole et l'Aréopage d'Athènes, reconstitution, 1846, domaine public
  mortsocrate: '../../philo/serie/img/t-socrate.jpg',       // Jacques-Louis David, La Mort de Socrate, 1787 (Metropolitan Museum), domaine public
  exclu: '../../philo/serie/img/t3-spinoza-exc.jpg',        // Samuel Hirszenberg, Spinoza excommunié, 1907, domaine public
  portes: '../../philo/serie/img/dv3-portes.jpg',           // Vilhelm Hammershøi, Portes blanches, Strandgade 25, 1913, domaine public
  grundlegung: '../../philo/serie/img/dv3-grundlegung.jpg', // Kant, Grundlegung zur Metaphysik der Sitten, Riga, 1785, page de titre, domaine public
  konigsberg: '../../philo/serie/img/t4-konigsberg.jpg',    // Königsberg, ville de Kant, photochrome, vers 1900, domaine public
  penseur: '../../philo/serie/img/t-penseur.jpg',           // Auguste Rodin, Le Penseur, musée Rodin (photo Jebulon, CC0)
};
window.MUSIQUE = 'montagem2';   // funk brésilien agressif (choix de Cengiz, 15/11/2026)
window.THEME = 'terminal';      // dossier secret
