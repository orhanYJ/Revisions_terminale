// Découpage du short « devinehistoire » (format « devine » : trois hommes du XXe siècle), modèle A, habillage alerte.
// a: [passage, mot] ; av : avance sur le mot. Chaque manche : carte « MANCHE n », puis le plan `devine2` (photo
// pixellisée qui se précise à chaque indice, chrono après « Trois, deux, un », révélation) qui revient entre des
// plans de liaison illustrant chaque indice. Le même objet `devine2` est repris à chaque retour (mêmes indices,
// même révélation) ; seul le premier porte `sons: true` (les sons d'indices ne sont émis qu'une fois).
const ROOSEVELT = { type: 'devine2', img: 'roosevelt', sur: 'DEVINE QUI C’EST · 1 / 3', indices: [
  [['d3', 'indice'], '1936 : « Je hais la guerre »'], [['d4', 0], 'Élu président en 1932'], [['d5', 0], 'Il lance le New Deal']],
  chrono: ['d5', 'trois'], rep: ['d6', 0], nom: 'ROOSEVELT', sous: 'Franklin D. Roosevelt|président des États-Unis dès 1933' };
const STALINE = { type: 'devine2', img: 'staline', sur: 'DEVINE QUI C’EST · 2 / 3', indices: [
  [['d8', 'indice'], '1933 : « l’abolition des classes »'], [['d9', 0], '1928 : premier plan quinquennal'], [['d10', 0], 'Dirige l’URSS de 1924 à 1953']],
  chrono: ['d10', 'trois'], rep: ['d11', 0], nom: 'STALINE', sous: 'Joseph Staline|l’URSS de 1924 à 1953' };
const CHURCHILL = { type: 'devine2', img: 'churchill', sur: 'DEVINE QUI C’EST · 3 / 3', indices: [
  [['d12', 'indice'], 'Conservateur, contre l’apaisement'], [['d13', 0], '10 mai 1940 : Premier ministre'], [['d14', 0], '« Nous ne nous rendrons jamais »']],
  chrono: ['d14', 'trois'], rep: ['d15', 0], nom: 'CHURCHILL', sous: 'Winston Churchill|Premier ministre britannique' };
const dv = (base, a, o = {}) => Object.assign({}, base, { a }, o);
window.MUSIQUE = 'hardtekk';
window.THEME = 'alerte';
window.PLAN = S => S.plans([
  // d1 « Devine qui c'est. 3 hommes qui ont fait le XXe siècle. »
  { a: ['d1', 0], av: .2, type: 'collage', imgs: ['wall', 'nuremberg', 'blitz'], t: 'DEVINE|QUI C’EST', ch: 0 },
  { a: ['d1', 'hommes'], type: 'silhouettes', t: '3 HOMMES|DU XXe SIÈCLE' },
  // d2 « 3 indices chacun, du plus dur au plus facile. Trouve avant la fin du compte ! »
  { a: ['d2', 0], type: 'regles', etapes: [[['d2', 'indices'], 'INDICE 1', 'DIFFICILE'], [['d2', 'plus'], 'INDICE 2', 'MOYEN'], [['d2', 'facile'], 'INDICE 3', 'FACILE']] },
  { a: ['d2', 'trouve'], type: 'mot', t: 'TROUVE AVANT|LA FIN DU COMPTE', choc: true },
  // MANCHE 1 · d3 « Manche 1. Indice 1 : en 1936, il déclare : je hais la guerre. »
  { a: ['d3', 0], type: 'manche', n: 1, matiere: 'LA CRISE DE 1929', ch: 1 },
  dv(ROOSEVELT, ['d3', 'indice'], { sons: true }),
  { a: ['d3', 'je'], type: 'citation', t: '« JE HAIS|LA GUERRE »', an: '1936' },
  // d4 « Indice 2 : il est élu président en 1932. »
  dv(ROOSEVELT, ['d4', 0]),
  { a: ['d4', 'élu'], type: 'date', t: '1932', de: 1900, sous: 'ÉLECTION PRÉSIDENTIELLE' },
  // d5 « Indice 3 : il lance le New Deal. Trois, deux, un. » (chrono, puis la révélation en d6)
  dv(ROOSEVELT, ['d5', 0]),
  // d6 « C'est Franklin Roosevelt ! Président des États-Unis à partir de 1933. »
  { a: ['d6', 'partir'], type: 'photo', img: 'investiture', t: '4 MARS 1933|L’INVESTITURE', sous: 'Roosevelt et Hoover, le président sortant', de: [1.05, .5, .3], vers: [1.25, .55, .25] },
  // d7 « Face à la Grande Dépression, son New Deal : secourir, relancer, réformer. »
  { a: ['d7', 0], type: 'collage', imgs: ['soupe', 'lange', 'dust'], t: 'LA GRANDE|DÉPRESSION' },
  { a: ['d7', 'secourir'], type: 'fiche', sur: 'LE NEW DEAL', t: '3 VERBES', items: [[['d7', 'secourir'], 'SECOURIR'], [['d7', 'relancer'], 'RELANCER'], [['d7', 'réformer'], 'RÉFORMER']] },
  // MANCHE 2 · d8 « Manche 2, plus dure. Indice 1 : en 1933, il promet l'abolition des classes. »
  { a: ['d8', 0], type: 'manche', n: 2, matiere: 'LES TOTALITARISMES', ch: 2 },
  dv(STALINE, ['d8', 'indice'], { sons: true }),
  { a: ['d8', "l'abolition"], type: 'affiche', t: 'L’ABOLITION|DES CLASSES', an: '1933' },
  // d9 « Indice 2 : en 1928, il lance le premier plan quinquennal. »
  dv(STALINE, ['d9', 0]),
  { a: ['d9', 'premier'], type: 'usine', t: 'PLAN|QUINQUENNAL', an: '1928' },
  // d10 « Indice 3 : il dirige l'URSS de 1924 à 1953. Trois, deux, un. »
  dv(STALINE, ['d10', 0]),
  // d11 « C'est Joseph Staline ! Sous son pouvoir : la famine en Ukraine, et le Goulag, ses camps de travail forcé. »
  { a: ['d11', 'famine'], type: 'mot', t: 'LA FAMINE|EN UKRAINE', sombre: true, choc: true },
  { a: ['d11', 'goulag'], type: 'photo', img: 'goulag', t: 'LE GOULAG', sous: 'camp de travail forcé : le canal de la mer Blanche, 1932', nb: true, de: [1.05, .3, .5], vers: [1.15, .6, .5] },
  // MANCHE 3 · d12 « Dernière manche. Indice 1 : conservateur, il s'oppose à la politique d'apaisement. »
  { a: ['d12', 0], type: 'manche', n: 3, matiere: 'LA SECONDE GUERRE MONDIALE', ch: 3 },
  dv(CHURCHILL, ['d12', 'indice'], { sons: true }),
  { a: ['d12', "s'oppose"], type: 'photo', img: 'munich', t: 'L’APAISEMENT|MUNICH, 1938', sous: 'céder à Hitler pour éviter la guerre', nb: true, de: [1.05, .5, .45], vers: [1.2, .5, .4] },
  // d13 « Indice 2 : le 10 mai 1940, il devient Premier ministre. »
  dv(CHURCHILL, ['d13', 0]),
  { a: ['d13', 'devient'], type: 'date', t: '1940', de: 1900, sous: '10 MAI' },
  // d14 « Indice 3 : devant les Communes, il lance : nous ne nous rendrons jamais. Trois, deux, un. »
  dv(CHURCHILL, ['d14', 0]),
  // d15 « C'est Winston Churchill ! En juin 1940, le Royaume-Uni se retrouve seul face à Hitler. »
  { a: ['d15', 'royaume-uni'], type: 'photo', img: 'blitz', t: 'SEUL|FACE À HITLER', sous: 'Londres sous les bombes, septembre 1940', nb: true, choc: true, de: [1.05, .5, .5], vers: [1.2, .45, .6] },
  // d16 « Combien tu en as trouvés ? Dis-le en commentaire. »
  { a: ['d16', 0], type: 'score', imgs: [['roosevelt', 'ROOSEVELT'], ['staline', 'STALINE'], ['churchill', 'CHURCHILL']], ch: 4 },
  { a: ['d16', 'dis'], type: 'mot', t: 'DIS-LE EN|COMMENTAIRE' },
  // d17 « Le cours complet est sur Révisions Animées. »
  { a: ['d17', 0], type: 'chaine', serie: 'Histoire · 1929-1945', fond: 'wall' },
]);
window.CHAPITRES = ['LE JEU', 'MANCHE 1', 'MANCHE 2', 'MANCHE 3', 'TON SCORE'];
window.IMAGES = {
  roosevelt: '../../dnl/serie/img/h1-roosevelt-1933.jpg',  // Franklin D. Roosevelt, 1933, Elias Goldensky, domaine public
  investiture: '../../dnl/serie/img/h1-hoover-fdr.jpg',    // Hoover et F. D. Roosevelt en route vers l'investiture, 4 mars 1933, Architect of the Capitol, domaine public
  staline: '../../dnl/serie/img/h2-stalin.jpg',            // Staline à la tribune, Moscou, 1937, photographe inconnu, domaine public
  churchill: '../../dnl/serie/img/h3-churchill.jpg',       // Winston Churchill, Ottawa, décembre 1941, Yousuf Karsh, Bibliothèque et Archives Canada, CC BY 2.0
  wall: '../../dnl/serie/img/h1-wallstreet.jpg',           // foule devant la Bourse de New York, octobre 1929, domaine public
  nuremberg: '../../dnl/serie/img/h2-nuremberg-1936.jpg',  // « cathédrale de lumière », congrès de Nuremberg, septembre 1936, Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE
  blitz: '../../dnl/serie/img/h3-blitz.jpg',               // enfants d'un faubourg de Londres sinistré, septembre 1940, US National Archives 306-NT-3163V, domaine public
  soupe: '../../dnl/serie/img/h1-soupkitchen.jpg',         // chômeurs devant une soupe populaire, Chicago, février 1931, US National Archives, domaine public
  lange: '../../dnl/serie/img/h1-lange-migrant.jpg',       // Dorothea Lange, Migrant Mother, mars 1936, Library of Congress, domaine public
  dust: '../../dnl/serie/img/h1-dustbowl.jpg',             // tempête de poussière, Stratford (Texas), 1935, George E. Marsh Jr., NOAA, domaine public
  goulag: '../../dnl/serie/img/h2-belomorkanal.jpg',       // détenus du Goulag creusant le canal de la mer Blanche à la Baltique, été 1932, domaine public
  munich: '../../dnl/serie/img/h2-munich.jpg',             // Chamberlain, Daladier, Hitler, Mussolini et Ciano à Munich, 29 septembre 1938, Bundesarchiv, Bild 183-R69173, CC BY-SA 3.0 DE
};
