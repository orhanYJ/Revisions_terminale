// Découpage du short « Remets dans l'ordre : de la crise de 1929 à la guerre » (format « ordre », le spectateur joue), modèle A.
// a: [passage, mot] ; av : avance sur le mot (négative : après le mot). À chaque manche : la pioche montre les quatre
// événements un par un pendant que la voix les lit (plan propre « pioche »), puis le plan ordre (formats-a.js) lance le
// chrono et révèle le bon ordre et les dates.
window.PLAN = S => S.plans([
  // o1 « De la crise de 1929 à la guerre : remets 12 événements dans l'ordre. »
  { a: ['o1', 0], av: .2, type: 'photo', img: 'lange', nb: true, t: 'DE LA CRISE|DE 1929…', de: [1.05, .5, .3], vers: [1.2, .5, .25], ch: 0 },
  { a: ['o1', 'guerre'], av: .3, type: 'date', t: '1939', de: 1929, sous: '… À LA GUERRE' },
  { a: ['o1', 'remets'], type: 'melange', t: 'REMETS DANS|L’ORDRE', choc: true },
  // o2 « 3 manches, 4 événements chacune. Compte tes points. »
  { a: ['o2', 0], type: 'score', t: 'COMPTE|TES POINTS' },
  // m1 / m1b / v1 : la crise
  { a: ['m1', 0], type: 'manche', n: 1, t: 'LA CRISE|ÉCONOMIQUE', fond: 'dust', ch: 1 },
  { a: ['m1b', 0], type: 'pioche', sur: 'MANCHE 1 · LA CRISE', etapes: [
    [['m1b', 'new'], 'Le New Deal', 'roosevelt'],
    [['m1b', 'krach'], 'Le krach|de Wall Street', 'wall'],
    [['m1b', 'front'], 'Le Front populaire', 'blum'],
    [['m1b', 'royaume-uni'], 'Le Royaume-Uni|quitte l’étalon-or', null, 'or']] },
  { a: ['m1b', -1], av: -.3, type: 'ordre', sur: 'MANCHE 1 · LA CRISE', cartes: [
    { t: 'Le New Deal', d: 'mars 1933' }, { t: 'Le krach de|Wall Street', d: 'oct. 1929' },
    { t: 'Le Front populaire', d: '1936' }, { t: 'Le Royaume-Uni|quitte l’étalon-or', d: 'sept. 1931' }],
    ordre: [1, 3, 0, 2], chrono: ['m1b', -1], rep: ['v1', 0], expl: 'Plus tôt on quitte l’or,|plus tôt on se redresse' },
  // x1 « Aux États-Unis : 14 millions de chômeurs, et des bidonvilles, les Hoovervilles. »
  { a: ['x1', 0], type: 'photo', img: 'soupe', nb: true, t: '14 MILLIONS|DE CHÔMEURS', sous: 'Chicago, 1931' },
  { a: ['x1', 'bidonvilles'], type: 'mot', img: 'hooverville', t: 'LES|HOOVERVILLES' },
  // m2 / m2b / v2 : les totalitarismes
  { a: ['m2', 0], type: 'collage', imgs: ['mussolini', 'staline', 'nuremberg'], t: 'MANCHE 2|LES TOTALITARISMES', ch: 2 },
  { a: ['m2b', 0], type: 'pioche', sur: 'MANCHE 2 · LES TOTALITARISMES', etapes: [
    [['m2b', 'hitler'], 'Hitler chancelier', 'potsdam'],
    [['m2b', 'grande'], 'La Grande Purge', 'proces'],
    [['m2b', 'marche'], 'La marche sur Rome', 'marche'],
    [['m2b', 'premier'], 'Le premier plan|de Staline', 'plan']] },
  { a: ['m2b', 'trois'], type: 'ordre', sur: 'MANCHE 2 · LES TOTALITARISMES', cartes: [
    { t: 'Hitler chancelier', d: '30 janv. 1933' }, { t: 'La Grande Purge', d: '1937-1938' },
    { t: 'La marche sur Rome', d: 'oct. 1922' }, { t: 'Le premier plan|de Staline', d: '1928' }],
    ordre: [2, 3, 0, 1], chrono: ['m2b', 'trois'], rep: ['v2', 0], expl: 'Italie, URSS, Allemagne' },
  // x2 « Trois régimes, un seul but : tout contrôler, et transformer l'homme. »
  { a: ['x2', 0], type: 'photo', img: 'nuremberg', nb: true, t: 'TROIS RÉGIMES|UN SEUL BUT', sous: 'Nuremberg, 1936' },
  { a: ['x2', 'tout'], type: 'tampon', t: 'TOUT CONTRÔLER', choc: true },
  // m3 / m3b / v3 : la marche à la guerre
  { a: ['m3', 0], type: 'manche', n: 3, t: 'LA MARCHE|À LA GUERRE', ch: 3 },
  { a: ['m3b', 0], type: 'pioche', sur: 'MANCHE 3 · VERS LA GUERRE', etapes: [
    [['m3b', "l'anschluss"], 'L’Anschluss', 'anschluss'],
    [['m3b', 'pacte'], 'Le pacte|germano-soviétique', 'pacte'],
    [['m3b', 'rhénanie'], 'La Rhénanie|remilitarisée', null, 'rhin'],
    [['m3b', 'munich'], 'Les accords|de Munich', 'munich']] },
  { a: ['m3b', -1], av: -.3, type: 'ordre', sur: 'MANCHE 3 · VERS LA GUERRE', cartes: [
    { t: 'L’Anschluss', d: '12 mars 1938' }, { t: 'Le pacte|germano-soviétique', d: '23 août 1939' },
    { t: 'La Rhénanie|remilitarisée', d: '7 mars 1936' }, { t: 'Les accords|de Munich', d: 'sept. 1938' }],
    ordre: [2, 0, 3, 1], chrono: ['m3b', -1], rep: ['v3', 0] },
  // x3a « Chaque recul des démocraties appelle une exigence plus grande. »
  { a: ['x3a', 0], type: 'portrait', img: 'heston', t: 'L’APAISEMENT', sous: 'Chamberlain de retour de Munich, 1938' },
  // x3 « 9 jours plus tard, l'Allemagne envahit la Pologne. C'est la guerre. »
  { a: ['x3', 0], type: 'date', t: '1939', de: 1936, sous: '1ER SEPTEMBRE' },
  { a: ['x3', "l'allemagne"], type: 'mot', t: 'L’ALLEMAGNE ENVAHIT|LA POLOGNE' },
  { a: ['x3', "c'est"], type: 'tampon', t: 'LA GUERRE', choc: true },
  // e1 « Alors, combien de manches réussies ? Dis-le en commentaire. »
  { a: ['e1', 0], type: 'score', fin: true, t: 'COMBIEN DE|MANCHES ?', ch: 4 },
  { a: ['e1', 'dis-le'], type: 'commentaire', t: 'DIS-LE EN|COMMENTAIRE' },
  // e2 « Toute l'histoire est sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Histoire · de 1929 à 1939', fond: 'wall' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA CRISE', 'LES TOTALITARISMES', 'VERS LA GUERRE', 'TON SCORE'];
window.IMAGES = {
  lange: '../../dnl/serie/img/h1-lange-migrant.jpg',          // Dorothea Lange, Migrant Mother, Nipomo, Californie, mars 1936 (Library of Congress), domaine public
  wall: '../../dnl/serie/img/h1-wallstreet.jpg',              // foule devant la Bourse de New York, octobre 1929 (Wikimedia Commons), domaine public
  dust: '../../dnl/serie/img/h1-dustbowl.jpg',                // tempête de poussière à l'approche de Stratford, Texas, 1935, George E. Marsh Jr. (NOAA, Wikimedia Commons), domaine public
  roosevelt: '../../dnl/serie/img/h1-roosevelt-1933.jpg',     // Franklin D. Roosevelt, 1933, par Elias Goldensky (Wikimedia Commons), domaine public
  blum: '../../dnl/serie/img/h1-blum-1936.jpg',               // Léon Blum à son bureau, devant un micro, 1936, Agence Meurisse, domaine public
  soupe: '../../dnl/serie/img/h1-soupkitchen.jpg',            // chômeurs devant une soupe populaire, Chicago, février 1931 (US National Archives), domaine public
  hooverville: '../../dnl/serie/img/h1-hooverville.jpg',      // Hooverville sur les vasières de Seattle, 7 février 1933, Seattle Municipal Archives (Wikimedia Commons), CC BY 2.0
  mussolini: '../../dnl/serie/img/h2-mussolini.jpg',          // Benito Mussolini, vers 1937-1940, Keystone, domaine public
  staline: '../../dnl/serie/img/h2-stalin.jpg',               // Staline à la tribune, Moscou, 1937, photographe inconnu, domaine public
  nuremberg: '../../dnl/serie/img/h2-nuremberg-1936.jpg',     // la « cathédrale de lumière », congrès de Nuremberg, septembre 1936, Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE
  potsdam: '../../dnl/serie/img/h2-potsdam.jpg',              // Hitler salue Hindenburg, Potsdam, 21 mars 1933, Bundesarchiv, Bild 183-S38324, CC BY-SA 3.0 DE
  proces: '../../dnl/serie/img/h2-moscow-trial.jpg',          // les accusés du deuxième procès de Moscou, janvier 1937, photographe inconnu, domaine public
  marche: '../../dnl/serie/img/h2-march-rome.jpg',            // Mussolini et les quadrumvirs de la marche sur Rome, tableau commémoratif, photo Silvio Galimberti, CC BY-SA 4.0
  plan: '../../dnl/serie/img/h2-fyp-poster.jpg',              // affiche du plan quinquennal « 2 + 2 plus l'enthousiasme des travailleurs = 5 », 1931, Iakov Guminer, domaine public
  anschluss: '../../dnl/serie/img/h2-anschluss.jpg',          // Hitler devant la foule de la Heldenplatz, Vienne, 15 mars 1938, Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE
  pacte: '../../dnl/serie/img/h2-pact.jpg',                   // Staline et Ribbentrop après la signature du pacte germano-soviétique, Moscou, 23 août 1939, Bundesarchiv, Bild 183-H27337 / Helmut Laux, CC BY-SA 3.0 DE
  munich: '../../dnl/serie/img/h2-munich.jpg',                // Chamberlain, Daladier, Hitler, Mussolini et Ciano avant la signature des accords de Munich, 29 septembre 1938, Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE
  heston: '../../dnl/serie/img/h2-heston.jpg',                // Chamberlain brandit la déclaration anglo-allemande à l'aéroport de Heston, 30 septembre 1938, Imperial War Museums, D 2239, domaine public
};
window.MUSIQUE = 'funk_agressif2';   // musique imposée pour ce short
window.THEME = 'archives';           // habillage imposé pour ce short
