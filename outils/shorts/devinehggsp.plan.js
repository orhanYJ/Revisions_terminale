// Découpage du short « devinehggsp » (format « devine » : trois personnages du programme d'HGGSP), modèle A, habillage terminal.
// a: [passage, mot] ; av : avance sur le mot. Chaque manche : carte « MANCHE n », puis le plan `devine2` (portrait
// pixellisé qui se précise à chaque indice, chrono après « Trois, deux, un », révélation) qui revient entre des plans
// de liaison illustrant chaque indice sans montrer le visage. Seul le premier retour porte `sons: true`.
const GAGARINE = { type: 'devine2', img: 'gagarine', sur: 'DEVINE QUI C’EST · 1 / 3', indices: [
  [['d3', 'indice'], 'Pilote d’avions de chasse'], [['d4', 0], '« On y va ! » au décollage'], [['d5', 0], '1961 : 1er homme dans l’espace']],
  chrono: ['d5', 'trois'], rep: ['d6', 0], nom: 'GAGARINE', sous: 'Youri Gagarine|Vostok 1, 12 avril 1961' };
const CLAUSEWITZ = { type: 'devine2', img: 'clausewitz', sur: 'DEVINE QUI C’EST · 2 / 3', indices: [
  [['d8', 'indice'], 'Son livre paraît après sa mort'], [['d9', 0], 'Officier prussien, contre Napoléon'], [['d10', 0], '« Continuation de la politique »']],
  chrono: ['d10', 'trois'], rep: ['d11', 0], nom: 'CLAUSEWITZ', sous: 'Carl von Clausewitz|officier et penseur prussien, 1780 – 1831' };
const CURIE = { type: 'devine2', img: 'curie', sur: 'DEVINE QUI C’EST · 3 / 3', indices: [
  [['d13', 'indice'], 'Un élément au nom de son pays'], [['d14', 0], '2 prix Nobel, 2 sciences'], [['d15', 0], 'Le radium, avec Pierre']],
  chrono: ['d15', 'trois'], rep: ['d16', 0], nom: 'MARIE CURIE', sous: 'Marie Curie|Nobel de physique 1903, de chimie 1911' };
const dv = (base, a, o = {}) => Object.assign({}, base, { a }, o);
window.MUSIQUE = 'montagem2';   // musique imposée pour ce short
window.THEME = 'terminal';      // habillage imposé pour ce short
window.PLAN = S => S.plans([
  // d1 « HGGSP : devine qui c'est. 3 personnages du programme. »
  { a: ['d1', 0], av: .2, type: 'collage', imgs: ['apollo', 'borodino', 'vostok'], t: 'HGGSP|DEVINE QUI C’EST', ch: 0 },
  { a: ['d1', 'personnages'], type: 'silhouettes', t: '3 PERSONNAGES|DU PROGRAMME' },
  // d2 « 3 indices, du plus dur au plus facile. »
  { a: ['d2', 0], type: 'regles', etapes: [[['d2', 'indices'], 'INDICE 1', 'DIFFICILE'], [['d2', 'plus'], 'INDICE 2', 'MOYEN'], [['d2', 'facile'], 'INDICE 3', 'FACILE']] },
  // MANCHE 1 · d3 « Manche 1. Indice 1 : il pilotait des avions de chasse. »
  { a: ['d3', 0], type: 'manche', n: 1, matiere: 'THÈME 1 · ESPACES DE CONQUÊTE', ch: 1 },
  dv(GAGARINE, ['d3', 'indice'], { sons: true }),
  { a: ['d3', 'avions'], type: 'avion', t: 'PILOTE|DE CHASSE', sous: 'avant sa mission' },
  // d4 « Indice 2 : au décollage, il crie : on y va ! »
  dv(GAGARINE, ['d4', 0]),
  { a: ['d4', 'il'], type: 'citation', t: '« ON Y|VA ! »', an: 'AU DÉCOLLAGE' },
  // d5 « Indice 3 : en 1961, premier homme dans l'espace. Trois, deux, un. » (chrono, révélation en d6)
  dv(GAGARINE, ['d5', 0]),
  // d6 « C'est Youri Gagarine ! Un tour de la Terre en 108 minutes. »
  { a: ['d6', 'tour'], type: 'orbite', t: 'MINUTES', sous: 'un tour complet de la Terre' },
  // d7 « Thème 1 : la course à l'espace, en pleine guerre froide. »
  { a: ['d7', 0], type: 'photo', img: 'vostok', t: 'LA COURSE|À L’ESPACE', sous: 'la capsule Vostok 1 (réplique, Le Bourget)', de: [1.05, .5, .5], vers: [1.25, .55, .45] },
  { a: ['d7', 'guerre'], type: 'tampon', t: 'GUERRE FROIDE', choc: true },
  // MANCHE 2 · d8 « Manche 2. Indice 1 : son livre majeur paraît après sa mort. »
  { a: ['d8', 0], type: 'manche', n: 2, matiere: 'THÈME 2 · FAIRE LA GUERRE, FAIRE LA PAIX', ch: 2 },
  dv(CLAUSEWITZ, ['d8', 'indice'], { sons: true }),
  { a: ['d8', 'paraît'], type: 'livre', t: 'PUBLIÉ|APRÈS SA MORT', an: '1832' },
  // d9 « Indice 2 : officier prussien, il combat Napoléon. »
  dv(CLAUSEWITZ, ['d9', 0]),
  { a: ['d9', 'combat'], type: 'photo', img: 'borodino', t: 'CONTRE|NAPOLÉON', sous: 'la Moskova, 1812, peinte par Louis Lejeune', de: [1.05, .5, .5], vers: [1.2, .45, .55] },
  // d10 « Indice 3 : la guerre, continuation de la politique par d'autres moyens. Trois, deux, un. »
  dv(CLAUSEWITZ, ['d10', 0]),
  // d11 « C'est Carl von Clausewitz ! Son livre : De la guerre. »
  { a: ['d11', 'son'], type: 'photo', img: 'vomkriege', nb: true, t: 'DE LA GUERRE|VOM KRIEGE, 1832', de: [1.05, .5, .3], vers: [1.2, .5, .25] },
  // d12 « Thème 2 : faire la guerre, faire la paix. »
  { a: ['d12', 0], type: 'mot', t: 'FAIRE LA GUERRE|FAIRE LA PAIX', choc: true },
  // MANCHE 3 · d13 « Dernière manche. Indice 1 : elle donne à un élément le nom de son pays natal. »
  { a: ['d13', 0], type: 'manche', n: 3, matiere: 'THÈME 6 · L’ENJEU DE LA CONNAISSANCE', ch: 3 },
  dv(CURIE, ['d13', 'indice'], { sons: true }),
  { a: ['d13', 'élément'], type: 'element', num: 84, sym: '?', nom: '? ? ?', t: 'LE NOM|DE SON PAYS' },
  // d14 « Indice 2 : elle reçoit 2 prix Nobel, dans 2 sciences différentes. »
  dv(CURIE, ['d14', 0]),
  { a: ['d14', 'prix'], type: 'nobel', medailles: [['1903', 'PHYSIQUE'], ['1911', 'CHIMIE']], t: '2 PRIX NOBEL|2 SCIENCES' },
  // d15 « Indice 3 : avec son mari Pierre, elle découvre le radium. Trois, deux, un. »
  dv(CURIE, ['d15', 0]),
  // d16 « C'est Marie Curie ! Née à Varsovie, elle baptise le polonium pour la Pologne. »
  { a: ['d16', 'née'], type: 'mot', t: 'NÉE À|VARSOVIE' },
  { a: ['d16', 'polonium'], type: 'element', num: 84, sym: 'Po', nom: 'POLONIUM', t: 'POLONIUM|POUR LA POLOGNE', sous: 'découvert en 1898 avec Pierre Curie' },
  // d17 « Thème 6 : l'enjeu de la connaissance, avec la radioactivité. »
  { a: ['d17', 0], type: 'photo', img: 'labo1912', nb: true, t: 'LA RADIO-|ACTIVITÉ', sous: 'Marie Curie dans son laboratoire, Paris, 1912', de: [1.05, .5, .5], vers: [1.2, .6, .45] },
  // d18 « Combien tu en as trouvés ? Dis-le en commentaire. »
  { a: ['d18', 0], type: 'score', imgs: [['gagarine', 'GAGARINE'], ['clausewitz', 'CLAUSEWITZ'], ['curie', 'CURIE']], ch: 4 },
  { a: ['d18', 'dis'], type: 'mot', t: 'DIS-LE EN|COMMENTAIRE', choc: true },
  // d19 « Plus de défis sur Révisions Animées. »
  { a: ['d19', 0], type: 'chaine', serie: 'Défis du bac', fond: 'apollo' },
]);
window.CHAPITRES = ['LE JEU', 'MANCHE 1', 'MANCHE 2', 'MANCHE 3', 'TON SCORE'];
window.IMAGES = {
  gagarine: 'img/hggsp-gagarine.jpg',        // Youri Gagarine, 1961, Arto Jousi (Suomen valokuvataiteen museo / Uuden Suomen kokoelma), restauration Adam Cuerden, domaine public (Wikimedia Commons)
  clausewitz: 'img/hggsp-clausewitz.jpg',    // Carl von Clausewitz, portrait par Karl Wilhelm Wach, domaine public (Wikimedia Commons, Clausewitz.jpg)
  curie: 'img/hggsp-curie.jpg',              // Marie Curie, vers 1920, Henri Manuel, domaine public (Wikimedia Commons)
  labo1912: 'img/hggsp-curie-labo.jpg',      // Marie Curie dans son laboratoire de Paris, 1912, photographe inconnu, domaine public (Wikimedia Commons)
  vomkriege: 'img/hggsp-vomkriege.jpg',      // page de titre de Vom Kriege, Berlin, Dümmler, 1832, domaine public (Wikimedia Commons)
  vostok: 'img/hggsp-vostok.jpg',            // réplique de la capsule Vostok 1, Musée de l'air et de l'espace, Le Bourget, Alan Wilson, CC BY-SA 2.0 (Wikimedia Commons)
  borodino: 'img/hggsp-borodino.jpg',        // Louis Lejeune, La bataille de la Moskova, 7 septembre 1812, domaine public (Wikimedia Commons)
  apollo: 'img/hggsp-apollo11.jpg',          // Buzz Aldrin sur la Lune, Apollo 11, 20 juillet 1969, photo Neil Armstrong, NASA, domaine public (Wikimedia Commons)
};
