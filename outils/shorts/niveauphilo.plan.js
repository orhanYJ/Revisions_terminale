// Découpage du short « niveauphilo » (format `niveau` : « Philo, niveau 1 → 10, à quel niveau tu t'arrêtes ? »),
// modèle A, habillage « jeu ». a: [passage, mot] ; av : avance sur le mot.
// Pour chaque palier : l'ascenseur qui monte (« Niveau N »), le plan `niveau` (question, chrono dans le silence qui suit,
// réponse et explication), puis un plan de liaison avec image sur la seconde phrase de la réponse.
const NIV = { type: 'niveau', total: 10 };
const niv = o => Object.assign({}, NIV, o);
window.PLAN = S => S.plans([
  // h1 « Philo, niveau 1 à 10. À quel niveau tu t'arrêtes ? »
  { a: ['h1', 0], av: .2, type: 'collage', ch: 0, imgs: ['platon', 'socrate', 'nietzsche'], t: 'PHILO|NIVEAU 1 → 10', couleur: true },
  { a: ['h1', 5], type: 'echelle' },   // 5 = le second « À »
  // h2 « Réponds avant la fin du chrono ! »
  { a: ['h2', 0], type: 'minuteur' },

  // n1q « Niveau 1. « Je pense, donc je suis. » Qui a dit ça ? » (chrono) ; n1r « Descartes, en 1637 ! Il doute de tout, sauf d'une chose : il pense. »
  { a: ['n1q', 0], av: .2, type: 'ascenseur', n: 1, de: 0, ch: 1 },
  niv({ a: ['n1q', 'je'], n: 1, q: '« Je pense,|donc je suis. »|Qui a dit ça ?', chrono: ['n1q', 'qui'], rep: ['n1r', 'descartes'], r: 'DESCARTES', expl: 'Discours de la méthode, 1637' }),
  { a: ['n1r', 'il'], type: 'photo', img: 'discours', t: 'IL DOUTE DE TOUT…|SAUF QU’IL PENSE', de: [1.0, .5, .25], vers: [1.25, .5, .2], legende: 'Discours de la méthode, Leyde, 1637' },

  // n3q « Niveau 3. Pour Aristote, l'homme est un animal… quoi ? » ; n3r « Politique ! Fait pour vivre en cité : lui seul a la parole. »
  { a: ['n3q', 0], av: .2, type: 'ascenseur', n: 3, de: 1 },
  niv({ a: ['n3q', 'pour'], n: 3, q: 'Pour Aristote, l’homme|est un animal…|QUOI ?', chrono: ['n3q', 'quoi'], rep: ['n3r', 'politique'], r: 'POLITIQUE', expl: 'Fait pour vivre dans une cité' }),
  { a: ['n3r', 'lui'], type: 'mot', img: 'pericles', t: 'LUI SEUL A|LA PAROLE' },

  // n5q « Niveau 5. Pour Sartre, l'existence précède… quoi ? » ; n5r « L'essence ! Pas de nature toute faite : tu n'es que ce que tu te fais. »
  { a: ['n5q', 0], av: .2, type: 'ascenseur', n: 5, de: 3, ch: 2 },
  niv({ a: ['n5q', 'pour'], n: 5, q: 'Pour Sartre,|l’existence précède…|QUOI ?', chrono: ['n5q', 'quoi'], rep: ['n5r', "l'essence"], r: 'L’ESSENCE', expl: 'Pas de nature toute faite' }),
  { a: ['n5r', 'tu'], type: 'portrait', img: 'sartre', t: 'SARTRE', sous: '« L’homme n’est rien d’autre que ce qu’il se fait »' },

  // n7q « Niveau 7. Freud : le moi est coincé entre deux instances. Lesquelles ? » ; n7r « Le ça et le surmoi ! Les pulsions d'un côté, les interdits de l'autre. »
  { a: ['n7q', 0], av: .2, type: 'ascenseur', n: 7, de: 5, ch: 3 },
  niv({ a: ['n7q', 'freud'], n: 7, q: 'Freud : le moi est coincé|entre deux instances.|LESQUELLES ?', chrono: ['n7q', 'lesquelles'], rep: ['n7r', 0], r: 'LE ÇA ET LE SURMOI', expl: 'La seconde topique, 1923' }),
  { a: ['n7r', 'pulsions'], type: 'tiraille', surmoi: ['n7r', 'interdits'] },

  // n9q « Niveau 9. Pour Kant, le bonheur est un idéal… de quoi ? » ; n9r « De l'imagination, pas de la raison ! On veut être heureux… sans savoir dire quoi. »
  { a: ['n9q', 0], av: .2, type: 'ascenseur', n: 9, de: 7, ch: 4 },
  niv({ a: ['n9q', 'pour'], n: 9, q: 'Pour Kant, le bonheur|est un idéal…|DE QUOI ?', chrono: ['n9q', 'quoi'], rep: ['n9r', 0], r: 'DE L’IMAGINATION', expl: '… pas de la raison (1785)' }),
  { a: ['n9r', 'on'], type: 'photo', img: 'jeunesse', t: 'HEUREUX…|MAIS DE QUOI ?', de: [1.0, .2, .3], vers: [1.15, .3, .35], legende: 'Thomas Cole, Le Voyage de la vie : la jeunesse, 1842' },

  // n10q « Niveau 10, boss final ! Selon Weber, l'État revendique le monopole… de quoi ? » ; n10r « De la violence physique légitime ! Arrêter, enfermer, contraindre : l'État ne partage pas ce droit. »
  { a: ['n10q', 0], av: .2, type: 'ascenseur', n: 10, de: 9, choc: true, boss: ['n10q', 'boss'] },
  niv({ a: ['n10q', 'selon'], n: 10, q: 'Selon Weber, l’État revendique|le monopole…|DE QUOI ?', chrono: ['n10q', 'quoi'], rep: ['n10r', 0], r: 'LA VIOLENCE PHYSIQUE LÉGITIME', expl: 'Weber, 1919' }),
  { a: ['n10r', 'arrêter'], type: 'verbes', mots: [['n10r', 'arrêter'], ['n10r', 'enfermer'], ['n10r', 'contraindre']] },
  { a: ['n10r', "l'état"], type: 'monopole' },

  // o1 « Dis ton niveau en commentaire ! »
  { a: ['o1', 0], type: 'commentaires', choc: true },
  // o2 « Les réponses sont dans les séries philo de Révisions Animées. »
  { a: ['o2', 0], type: 'mot', img: 'athenes', t: 'LES RÉPONSES' },
  { a: ['o2', 'séries'], type: 'chaine', serie: 'Philosophie', fond: 'penseur' },
  // o3 « Et toi… tu montes jusqu'au niveau 10 ? » (relance la question du début)
  { a: ['o3', 0], type: 'echelle', fin: true },
]);
window.CHAPITRES = ['ACCROCHE', 'FACILE', 'MOYEN', 'DIFFICILE', 'IMPOSSIBLE'];
window.IMAGES = {
  platon: '../../philo/serie/img/platon.jpg',          // Raphaël, L'École d'Athènes, détail (Platon), 1509-1511, domaine public
  socrate: '../../philo/serie/img/socrate.jpg',        // buste, copie romaine d'après Lysippe, musée du Louvre, domaine public
  nietzsche: '../../philo/serie/img/nietzsche.jpg',    // photographie de Gustav Schultze, 1882, domaine public
  discours: '../../philo/serie/img/cs2-discours.jpg',  // Descartes, Discours de la méthode, Leyde, Jan Maire, 1637, page de titre, domaine public
  pericles: '../../philo/serie/img/t-pericles.jpg',    // Philipp von Foltz, Périclès parlant aux Athéniens, 1852 (photographie, Rijksmuseum), domaine public
  sartre: '../../philo/serie/img/sartre.jpg',          // photographie de 1965, Nationaal Archief / Anefo, CC BY-SA 3.0 NL (attribution obligatoire)
  freud: '../../philo/serie/img/freud.jpg',            // photographie de Max Halberstadt, vers 1921, domaine public
  jeunesse: '../../philo/serie/img/bh1-jeunesse.jpg',  // Thomas Cole, Le Voyage de la vie : la jeunesse, 1840-1842, domaine public
  duel: '../../philo/serie/img/et1-duel.jpg',          // Jean-Léon Gérôme, Le Duel après le bal masqué, vers 1857-1859, domaine public
  athenes: '../../philo/serie/img/t-athenes.jpg',      // Raphaël, L'École d'Athènes, 1509-1511, domaine public
  penseur: '../../philo/serie/img/t-penseur.jpg',      // Auguste Rodin, Le Penseur, musée Rodin (photo Jebulon, CC0)
};
window.MUSIQUE = 'funk_agressif';   // funk brésilien agressif (choix de Cengiz, 15/11/2026)
window.THEME = 'jeu';               // plateau de jeu télé
