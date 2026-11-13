// Découpage du short « bacetat » (format 2, question de bac : « L'État est-il l'ennemi de la liberté ? »), modèle A.
// a: [passage, mot] ; av : avance sur le mot. Le plan `copie` revient à chaque partie : les lignes s'écrivent à leur
// repère (celles dites pendant un dessin sont déjà écrites quand on revient à la copie).
const COPIE = {
  type: 'copie', matiere: 'PHILOSOPHIE', sujet: 'L’État est-il l’ennemi|de la liberté ?', lignes: [
    [['s4', "l'état"], 'Problématique :', 'titre'],
    [['s4', 'ou'], 'ennemi de la liberté… ou sa condition ?', ''],
    [['s5', 0], 'I. Oui : l’État contraint, il peut écraser', 'partie'],
    [['s6', 'proudhon'], 'Proudhon : « être gouverné, c’est être gardé à vue… »', 'ex'],
    [['s7', 'ton'], 'Ex. : la police secrète de Ceaușescu', 'ex'],
    [['s8', 0], 'II. Mais sans État, pas de liberté', 'partie'],
    [['s9', 'montréal'], 'Ex. : Montréal, 1969 : 16 h sans police', 'ex'],
    [['s10', 'locke'], 'Locke : l’État, gardien de la vie, de la liberté, des biens', 'ex'],
    [['s11', 0], 'III. Il en est la condition, s’il est limité', 'partie'],
    [['s12', 'montesquieu'], 'Montesquieu : « le pouvoir arrête le pouvoir »', 'ex'],
    [['s13', 'le'], 'Ex. : le Watergate, 1974', 'ex'],
    [['s14', 'rousseau'], 'Rousseau : liberté naturelle ≠ liberté civile', 'ex'],
  ],
};
const copie = (a, o = {}) => Object.assign({}, COPIE, { a }, o);
window.PLAN = S => S.plans([
  // s1 « Ce sujet peut tomber au bac. Tu as 60 secondes pour le plan. »
  { a: ['s1', 0], av: .2, type: 'chrono', t: 'CE SUJET PEUT|TOMBER AU BAC', ch: 0 },
  { a: ['s1', 'tu'], type: 'chrono', run: true, t: 'TU AS 60 SECONDES|POUR LE PLAN' },
  // s2 « L'État est-il l'ennemi de la liberté ? »
  { a: ['s2', 0], type: 'bac', sujet: ['L’État est-il l’ennemi', 'de la liberté ?'] },
  // s3 « Le piège ? Le mot « ennemi ». Un obstacle gêne ; un ennemi veut ta perte. »
  { a: ['s3', 0], type: 'mot', t: 'LE PIÈGE ?', sombre: true, choc: true, ch: 1 },
  { a: ['s3', 2], type: 'loupe', cercles: [[['s3', 'ennemi'], 'l’ennemi']], t: 'UN SEUL MOT|« ENNEMI »' },
  { a: ['s3', 'obstacle'], type: 'oppose', g: ['s3', 'obstacle'], d: ['s3', 'veut'] },
  // s4 « Ta problématique : l'État est-il l'ennemi de la liberté… ou sa condition ? »
  { a: ['s4', 0], type: 'mot', t: 'TA PROBLÉMATIQUE' },
  copie(['s4', "l'état"], { souligne: [['s4', 'condition'], 1] }),
  // s5 « Première partie : oui. L'État contraint, il peut écraser. »
  copie(['s5', 0], { ch: 2 }),
  { a: ['s5', "l'état"], type: 'mot', t: 'IL CONTRAINT…|IL PEUT ÉCRASER' },
  // s6 « Proudhon : être gouverné, c'est être gardé à vue, inspecté, espionné. »
  { a: ['s6', 0], type: 'oeil', q: ['s6', 'être'], mots: [[['s6', 'gardé'], 'GARDÉ À VUE'], [['s6', 'inspecté'], 'INSPECTÉ'], [['s6', 'espionné'], 'ESPIONNÉ']] },
  // s7 « Ton exemple : la police secrète de Ceaușescu. »
  copie(['s7', 0]),
  { a: ['s7', 'police'], type: 'portrait', img: 'palais', t: 'CEAUȘESCU', sous: 'Roumanie · la police secrète' },
  // s8 « Deuxième partie : mais sans État, pas de liberté. »
  copie(['s8', 0], { ch: 3 }),
  { a: ['s8', 'sans'], type: 'mot', t: 'SANS ÉTAT…|PAS DE LIBERTÉ', sombre: true },
  // s9 « Montréal, 1969 : grève de la police. 16 heures, et la ville bascule. »
  { a: ['s9', 0], type: 'date', t: '1969', de: 1900, sous: 'MONTRÉAL' },
  { a: ['s9', 'grève'], type: 'montreal', h: ['s9', '16'], bascule: ['s9', 'bascule'] },
  // s10 « Locke : l'État est le gardien de la vie, de la liberté, des biens. »
  { a: ['s10', 0], type: 'portrait', img: 'locke', t: 'LOCKE', sous: 'Traité du gouvernement civil' },
  { a: ['s10', 'gardien'], type: 'gardien', items: [[['s10', 'vie'], 'VIE'], [['s10', 'liberté'], 'LIBERTÉ'], [['s10', 'biens'], 'BIENS']] },
  // s11 « Troisième partie : l'État, condition de la liberté… s'il est limité. »
  copie(['s11', 0], { ch: 4 }),
  { a: ['s11', "s'il"], type: 'mot', t: 'S’IL EST|LIMITÉ' },
  // s12 « Montesquieu : il faut que le pouvoir arrête le pouvoir. »
  { a: ['s12', 0], type: 'pouvoirs', q: ['s12', 'pouvoir'] },
  // s13 « Le Watergate, 1974 : la Cour suprême oblige Nixon à livrer ses enregistrements. Il démissionne. »
  { a: ['s13', 0], type: 'watergate', cour: ['s13', 'cour'] },
  { a: ['s13', 'oblige'], type: 'bandes' },
  { a: ['s13', 'il'], type: 'watergate', fin: true },
  // s14 « Rousseau distingue : liberté naturelle, limitée par tes forces ; liberté civile, garantie par la loi. »
  copie(['s14', 0]),
  { a: ['s14', 'liberté'], type: 'deuxlib', g: ['s14', 'naturelle'], d: ['s14', 'civile'] },
  // s15 « L'État retire la première… pour te donner la seconde. »
  { a: ['s15', 0], type: 'deuxlib', echange: true, r: ['s15', 'retire'], s: ['s15', 'seconde'] },
  // s16 « L'erreur à ne pas faire : réciter tes auteurs sans répondre à la question. »
  { a: ['s16', 0], type: 'mot', t: 'L’ERREUR|À NE PAS FAIRE', sombre: true, choc: true },
  { a: ['s16', 'réciter'], type: 'recite', barre: ['s16', 'question'] },
  // s17 « Un auteur est un outil pour penser. »
  { a: ['s17', 0], type: 'mot', t: 'UN AUTEUR ?|UN OUTIL POUR PENSER' },
  // s18 « Le cours complet est sur Révisions Animées. »
  { a: ['s18', 0], type: 'chaine', serie: "L'État", fond: 'liberte' },
  // s19 « Et toi… l'État, ennemi ou condition de ta liberté ? » (relance la question du début)
  { a: ['s19', 0], type: 'balance', t: 'ET TOI…|ENNEMI OU CONDITION ?' },
]);
window.CHAPITRES = ['LE SUJET', 'LE PIÈGE', 'PARTIE I', 'PARTIE II', 'PARTIE III'];
window.IMAGES = {
  proudhon: '../../philo/serie/img/proudhon.jpg',        // Gustave Courbet, Pierre-Joseph Proudhon, 1865 (détail), domaine public
  palais: '../../philo/serie/img/et4-palais.jpg',        // palais du Parlement (« Maison du peuple » de Ceaușescu), Bucarest, 1996, photo Sludge G, CC BY-SA 2.0
  gordon: '../../philo/serie/img/et2-gordon.jpg',        // John Seymour Lucas, Les Émeutes de Gordon, 1879, domaine public
  locke: '../../philo/serie/img/locke.jpg',              // Godfrey Kneller, John Locke, 1697, domaine public
  montesquieu: '../../philo/serie/img/montesquieu.jpg',  // anonyme, Montesquieu, 1728 (château de Versailles), domaine public
  nixon: '../../philo/serie/img/et3-nixon.jpg',          // Nixon quitte la Maison-Blanche, 9 août 1974, photographie officielle, domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',        // Maurice Quentin de La Tour, 1753, domaine public
  liberte: '../../philo/serie/img/t-liberte-peuple.jpg', // Eugène Delacroix, La Liberté guidant le peuple, 1830, domaine public
};
window.MUSIQUE = 'lofi';   // musique imposée pour ce short (format 2, rythme posé)
