// Découpage du short « totalitarismes60 » (format 3, résumé express : « Les totalitarismes en 60 secondes »), modèle A.
// a: [passage, mot] ; av : avance sur le mot. La fiche revient à chaque idée et se remplit (une case cochée par idée).
const FICHE = {
  type: 'fiche', sur: 'LES TOTALITARISMES EN 60 SECONDES', t: '5 IDÉES', items: [
    [['s3', 0], 'Tout contrôler', 'la nation, la race, la classe'],
    [['s6', 0], 'Le pouvoir sans coup d’État', 'Rome, 1922 · Hitler chancelier, 1933'],
    [['s9', 0], 'Un chef, un parti unique', 'le Duce, Heil Hitler, Stalingrad (1925)'],
    [['s11', 0], 'L’homme nouveau', 'Jeunesses hitlériennes, Stakhanov'],
    [['s13', 0], 'La terreur', 'Dachau, Goulag, Holodomor, Grande Purge'],
  ],
};
const fiche = (a, o = {}) => Object.assign({}, FICHE, { a }, o);
window.PLAN = S => S.plans([
  // s1 « Les totalitarismes en 60 secondes. 5 idées pour le bac. »
  { a: ['s1', 0], av: .2, type: 'chrono', t: 'LES TOTALITARISMES|EN 60 SECONDES', ch: 0 },
  { a: ['s1', '5'], type: 'mot', t: '5 IDÉES|POUR LE BAC' },
  // s2 « Mussolini, Hitler, Staline : trois régimes, une même machine. »
  { a: ['s2', 0], type: 'trio', rev: [['s2', 'mussolini'], ['s2', 'hitler'], ['s2', 'staline']], mach: ['s2', 'une'] },
  // s3 « Idée 1 : tout contrôler. Pas seulement l'État : toute la société. »
  fiche(['s3', 0]),
  { a: ['s3', 'pas'], type: 'cercles', ext: ['s3', 'toute'] },
  // s4 « Une dictature veut ton silence. Le totalitarisme veut te changer, selon une idéologie. »
  { a: ['s4', 0], type: 'duel', b2: ['s4', 'le'], ideo: ['s4', 'selon'] },
  // s5 « La nation pour Mussolini, la race pour Hitler, la classe pour Staline. »
  { a: ['s5', 0], type: 'ideo', items: [[['s5', 'nation'], 'LA NATION', 'Mussolini'], [['s5', 'race'], 'LA RACE', 'Hitler'], [['s5', 'classe'], 'LA CLASSE', 'Staline']] },
  // s6 « Idée 2 : ils prennent le pouvoir sans coup d'État. »
  fiche(['s6', 0], { ch: 1 }),
  { a: ['s6', 'sans'], type: 'mot', t: 'SANS|COUP D’ÉTAT' },
  // s7 « Octobre 1922, la marche sur Rome. La menace suffit : le roi nomme Mussolini. »
  { a: ['s7', 0], type: 'portrait', img: 'marche', t: 'LA MARCHE SUR ROME', sous: 'octobre 1922' },
  { a: ['s7', 'menace'], type: 'mot', t: 'LA MENACE|SUFFIT' },
  { a: ['s7', 'roi'], type: 'portrait', img: 'mussolini', t: 'MUSSOLINI', sous: 'nommé par le roi' },
  // s8 « Hitler, jamais majoritaire, est nommé chancelier le 30 janvier 1933. Légalement. »
  { a: ['s8', 0], type: 'vote', jamais: ['s8', 'jamais'] },
  { a: ['s8', 'chancelier'], type: 'portrait', img: 'potsdam', t: 'CHANCELIER', sous: 'Hitler, 30 janvier 1933' },
  { a: ['s8', 'légalement'], type: 'tampon', t: 'LÉGALEMENT', choc: true },
  // s9 « Idée 3 : un chef qu'on vénère, un parti unique. »
  fiche(['s9', 0], { ch: 2 }),
  { a: ['s9', 6], type: 'mot', t: 'UN CHEF|UN PARTI UNIQUE' },
  // s10 « Le Duce a toujours raison. On salue : Heil Hitler. En 1925, une ville est rebaptisée Stalingrad. »
  { a: ['s10', 0], type: 'mot', img: 'mussolini', t: 'LE DUCE A|TOUJOURS RAISON' },
  { a: ['s10', 'on'], type: 'portrait', img: 'nuremberg', t: 'HEIL HITLER', sous: 'le salut officiel' },
  { a: ['s10', 'en'], type: 'ville', nom: ['s10', 'stalingrad'] },
  // s11 « Idée 4 : fabriquer un homme nouveau, dès l'enfance. »
  fiche(['s11', 0], { ch: 3 }),
  { a: ['s11', 'un'], type: 'mot', t: 'UN HOMME NOUVEAU|DÈS L’ENFANCE' },
  // s12 « Jeunesses hitlériennes, obligatoires de 10 à 18 ans. En URSS, un modèle : le mineur Stakhanov. »
  { a: ['s12', 0], type: 'jeunesse' },
  { a: ['s12', 'en'], type: 'portrait', img: 'stakhanov', t: 'STAKHANOV', sous: 'le mineur modèle, 1935' },
  // s13 « Idée 5 : la terreur. C'est une méthode de gouvernement. »
  fiche(['s13', 0], { ch: 4 }),
  { a: ['s13', "c'est"], type: 'mot', t: 'UNE MÉTHODE|DE GOUVERNEMENT' },
  // s14 « Police politique, camps : Dachau dès 1933, le Goulag en URSS. »
  { a: ['s14', 0], type: 'camps', items: [[['s14', 'dachau'], 'DACHAU', 'Allemagne, dès 1933']] },
  { a: ['s14', 'goulag'], type: 'portrait', img: 'belomor', t: 'LE GOULAG', sous: 'des détenus au travail forcé, 1932' },
  // s15 « En 1932 et 1933, l'Holodomor, une famine provoquée, tue des millions d'Ukrainiens. »
  { a: ['s15', 0], type: 'holodomor', mil: ['s15', 'millions'], sombre: true },
  // s16 « Puis la Grande Purge de 1937 et 1938 : 680000 exécutions. »
  { a: ['s16', 0], type: 'purge', n: ['s16', '680000'], sombre: true },
  // s17 « Au bout, la guerre : le 1er septembre 1939, l'Allemagne attaque la Pologne. »
  { a: ['s17', 0], type: 'mot', t: 'AU BOUT|LA GUERRE', choc: true },
  { a: ['s17', 'le'], type: 'date', t: '1939', de: 1933, sous: '1ER SEPTEMBRE' },
  { a: ['s17', "l'allemagne"], type: 'mot', t: 'L’ALLEMAGNE ATTAQUE|LA POLOGNE' },
  // s18 « Toute la série est sur Révisions Animées. »
  { a: ['s18', 0], type: 'chaine', serie: 'Les régimes totalitaires', fond: 'nuremberg' },
  // s19 « Alors : combien d'idées tu as retenues ? »
  fiche(['s19', 0], { sur: 'TU EN AS RETENU COMBIEN ?', t: '… / 5' }),
]);
window.CHAPITRES = ['ACCROCHE · DÉFINIR', 'LE POUVOIR', 'LE CHEF', 'L’HOMME NOUVEAU', 'LA TERREUR'];
window.IMAGES = {
  mussolini: '../../dnl/serie/img/h2-mussolini.jpg',       // Benito Mussolini, vers 1937-1940, Keystone, domaine public
  potsdam: '../../dnl/serie/img/h2-potsdam.jpg',           // Hitler salue Hindenburg, Potsdam, 21 mars 1933, Bundesarchiv Bild 183-S38324, CC BY-SA 3.0 DE
  stalin: '../../dnl/serie/img/h2-stalin.jpg',             // Staline à la tribune, Moscou, 1937, photographe inconnu, domaine public
  marche: '../../dnl/serie/img/h2-march-rome.jpg',         // Mussolini et les quadrumvirs de la marche sur Rome, tableau commémoratif, photo Silvio Galimberti, CC BY-SA 4.0
  nuremberg: '../../dnl/serie/img/h2-nuremberg-1936.jpg',  // la « cathédrale de lumière », congrès de Nuremberg, septembre 1936, Bundesarchiv Bild 183-1982-1130-502, CC BY-SA 3.0 DE
  stakhanov: '../../dnl/serie/img/h2-stakhanov.jpg',       // Alexeï Stakhanov (au centre) explique sa méthode, années 1930, Eleazar Langman, domaine public
  belomor: '../../dnl/serie/img/h2-belomorkanal.jpg',      // détenus du Goulag creusant le canal de la mer Blanche à la Baltique, été 1932, photographe inconnu, domaine public
};
window.MUSIQUE = 'trap';   // musique imposée pour ce short (format 3, rythme rapide)
