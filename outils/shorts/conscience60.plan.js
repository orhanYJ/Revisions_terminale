// Découpage du short « conscience60 » (format 3, résumé express : « La conscience en 60 secondes »), modèle A.
// a: [passage, mot] ; av : avance sur le mot. La fiche revient à chaque idée et se remplit (une case cochée par idée).
const FICHE = {
  type: 'fiche', sur: 'LA CONSCIENCE EN 60 SECONDES', t: '5 IDÉES', items: [
    [['s2', 0], 'Spontanée / réfléchie', 'le joueur… puis le replay'],
    [['s5', 0], 'Descartes', 'je pense, donc je suis'],
    [['s8', 0], 'Freud', 'l’inconscient : oublis, lapsus, rêves'],
    [['s11', 0], 'Sartre', 'la honte, sous le regard d’autrui'],
    [['s14', 0], 'La conscience morale', 'Rousseau : « instinct divin »'],
  ],
};
const fiche = (a, o = {}) => Object.assign({}, FICHE, { a }, o);
window.PLAN = S => S.plans([
  // s1 « La conscience en 60 secondes. 5 idées pour le bac. »
  { a: ['s1', 0], av: .2, type: 'chrono', run: true, t: 'LA CONSCIENCE|EN 60 SECONDES', ch: 0 },
  { a: ['s1', '5'], type: 'mot', t: '5 IDÉES|POUR LE BAC' },
  // s2 « Idée 1 : il y a deux consciences. »
  fiche(['s2', 0]),
  // s3 « Un joueur frappe le ballon : il voit le but, pas lui-même. Conscience spontanée. »
  { a: ['s3', 0], type: 'portrait', img: 'football', t: 'UN JOUEUR', sous: 'frappe le ballon' },
  { a: ['s3', 'il'], type: 'foot', etapes: [[null, 'IL VOIT LE BUT…'], [['s3', 'pas'], 'PAS LUI-MÊME']] },
  { a: ['s3', 'conscience'], type: 'mot', t: 'CONSCIENCE|SPONTANÉE' },
  // s4 « Après le match, il revoit l'action : pourquoi j'ai tiré si vite ? Conscience réfléchie. »
  { a: ['s4', 0], type: 'foot', replay: true, bulle: ['s4', 'pourquoi'] },
  { a: ['s4', 'conscience'], type: 'mot', t: 'CONSCIENCE|RÉFLÉCHIE' },
  // s5 « Idée 2 : Descartes doute de tout. Les sens, le rêve, et même les calculs. »
  fiche(['s5', 0], { ch: 1 }),
  { a: ['s5', 'descartes'], type: 'portrait', img: 'descartes', t: 'DESCARTES', sous: 'je doute de tout' },
  { a: ['s5', 'les'], type: 'doute', items: [[['s5', 'sens'], 'LES SENS'], [['s5', 'rêve'], 'LE RÊVE'], [['s5', 'calculs'], 'LES CALCULS']] },
  // s6 « Mais pour douter, il faut penser. Et pour penser, il faut être. »
  { a: ['s6', 0], type: 'logique', etapes: [[null, 'DOUTER'], [['s6', 'penser'], '= PENSER'], [['s6', 'être'], '= ÊTRE']] },
  // s7 « Je pense, donc je suis. Ta première certitude, c'est ta conscience. »
  { a: ['s7', 0], type: 'mot', t: 'JE PENSE,|DONC JE SUIS', choc: true },
  { a: ['s7', 'ta'], type: 'mot', t: 'TA PREMIÈRE CERTITUDE|TA CONSCIENCE' },
  // s8 « Idée 3 : Freud. Ta conscience ne voit pas tout. »
  fiche(['s8', 0], { ch: 2 }),
  { a: ['s8', 'freud'], type: 'portrait', img: 'freud', t: 'FREUD', sous: 'ta conscience ne voit pas tout' },
  // s9 « Freud oublie le nom d'un peintre. Il lui vient Botticelli, Boltraffio… Le bon ? Signorelli. »
  { a: ['s9', 0], type: 'mot', t: 'IL OUBLIE|LE NOM D’UN PEINTRE' },
  { a: ['s9', 'il'], type: 'noms', noms: [[['s9', 'botticelli'], 'BOTTICELLI', false], [['s9', 'boltraffio'], 'BOLTRAFFIO', false], [['s9', 'signorelli'], 'SIGNORELLI', true]] },
  // s10 « Un oubli, un lapsus, un rêve : des trous. Pour les expliquer, il faut un inconscient. »
  { a: ['s10', 0], type: 'trous', trous: [[['s10', 'oubli'], 'UN OUBLI'], [['s10', 'lapsus'], 'UN LAPSUS'], [['s10', 'rêve'], 'UN RÊVE']] },
  { a: ['s10', 'pour'], type: 'trous', tous: true, insc: ['s10', 'inconscient'] },
  // s11 « Idée 4 : Sartre. Tu colles ton œil à une serrure. Tu ne penses qu'à la scène. »
  fiche(['s11', 0], { ch: 3 }),
  { a: ['s11', 'sartre'], type: 'portrait', img: 'sartre', t: 'SARTRE', sous: 'L’Être et le Néant, 1943' },
  { a: ['s11', 'colles'], type: 'serrure', etapes: [[null, 'L’ŒIL À LA SERRURE'], [['s11', 'penses'], 'RIEN QUE LA SCÈNE']] },
  // s12 « Soudain, des pas. Quelqu'un te voit. La honte. »
  { a: ['s12', 0], type: 'serrure', pas: [['s12', 'soudain'], ['s12', 'des'], ['s12', 'pas']], voit: ['s12', 'quelqu'],
    etapes: [[null, 'SOUDAIN… DES PAS'], [['s12', 'quelqu'], 'QUELQU’UN TE VOIT']] },
  { a: ['s12', 'la'], type: 'honte', choc: true },
  // s13 « D'un coup, tu existes pour toi… tel qu'un autre te voit. »
  { a: ['s13', 0], type: 'mot', img: 'ecouteuse', t: 'TU EXISTES POUR TOI…|TEL QU’UN AUTRE TE VOIT' },
  // s14 « Idée 5 : la conscience morale, la voix qui juge. Rousseau l'appelle instinct divin. »
  fiche(['s14', 0], { ch: 4 }),
  { a: ['s14', 'rousseau'], type: 'cite', img: 'rousseau', nom: 'ROUSSEAU', q: '« Conscience ! conscience !|instinct divin »',
    src: 'Émile, livre IV, 1762', aq: ['s14', 'rousseau'], duree: 1.3 },
  // s15 « Raskolnikov tue une usurière. Pas de témoin, pas de preuve. »
  { a: ['s15', 0], type: 'portrait', img: 'raskolnikov', t: 'RASKOLNIKOV', sous: 'Crime et Châtiment, 1866' },
  { a: ['s15', 'pas'], type: 'proces', lignes: [[['s15', 'pas'], 'PAS DE TÉMOIN'], [['s15', 7], 'PAS DE PREUVE']] },
  // s16 « Personne ne l'accuse. Personne… sauf lui. »
  { a: ['s16', 0], type: 'proces', mode: 'sauf', sauf: ['s16', 'sauf'] },
  // s17 « Toute la série « La conscience » est sur Révisions Animées. »
  { a: ['s17', 0], type: 'chaine', serie: 'La conscience', fond: 'ecouteuse' },
  // s18 « Alors : combien d'idées tu as retenues ? »
  fiche(['s18', 0], { sur: 'TU EN AS RETENU COMBIEN ?', t: '… / 5' }),
]);
window.CHAPITRES = ['ACCROCHE · IDÉE 1', 'DESCARTES', 'FREUD', 'SARTRE', 'LA MORALE'];
window.IMAGES = {
  football: '../../philo/serie/img/cs1-football.jpg',      // Henri Rousseau, Les Joueurs de football, 1908, domaine public
  descartes: '../../philo/serie/img/descartes.jpg',        // d'après Frans Hals, domaine public
  freud: '../../philo/serie/img/freud.jpg',                // Max Halberstadt, vers 1921, domaine public
  signorelli: '../../philo/serie/img/cs3-signorelli.jpg',  // Luca Signorelli, Les Damnés, Orvieto, 1499-1502, domaine public
  sartre: '../../philo/serie/img/sartre.jpg',              // photographie de 1965, Nationaal Archief / Anefo, CC BY-SA 3.0 NL (attribution obligatoire)
  ecouteuse: '../../philo/serie/img/cs4-ecouteuse.jpg',    // Nicolaes Maes, L'Écouteuse, 1657, domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',          // Maurice Quentin de La Tour, 1753, domaine public
  raskolnikov: '../../philo/serie/img/cs5-raskolnikov.jpg', // Mikhaïl Klodt, illustration pour Crime et Châtiment, 1874, domaine public
};
window.MUSIQUE = 'house';   // musique imposée pour ce short (format 3, rythme rapide)
