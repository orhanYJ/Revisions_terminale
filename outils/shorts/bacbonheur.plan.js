// Découpage du short « bacbonheur » (format 2, question de bac : « Faut-il renoncer à ses désirs pour être heureux ? »),
// modèle A. a: [passage, mot] ; av : avance sur le mot. Le plan `copie` revient à chaque partie : les lignes s'écrivent
// à leur repère (celles dites pendant un dessin sont déjà écrites quand on revient à la copie).
const COPIE = {
  type: 'copie', matiere: 'PHILOSOPHIE', sujet: 'Faut-il renoncer à ses désirs|pour être heureux ?', lignes: [
    [['s5', 'faut-il'], 'Problématique :', 'titre'],
    [['s5', 'tous'], 'renoncer à tous ses désirs, ou à certains ?', ''],
    [['s6', 0], 'I. Oui : le désir est un manque sans fin', 'partie'],
    [['s7', 'platon'], 'Platon : les tonneaux percés', 'ex'],
    [['s8', 'toi'], 'Ex. : toi, ce soir, vidéo après vidéo', 'ex'],
    [['s9', 0], 'II. Mais sans désir, on ne vit plus', 'partie'],
    [['s10', 'calliclès'], 'Calliclès : la pierre serait la plus heureuse', 'ex'],
    [['s11', 'malheur'], 'Rousseau : « Malheur à qui n’a plus rien à désirer ! »', 'ex'],
    [['s12', 0], 'III. Non pas supprimer ses désirs, mais les régler', 'partie'],
    [['s13', 'descartes'], 'Descartes : changer ses désirs, pas l’ordre du monde', 'ex'],
    [['s14', 'exemple'], 'Ex. : je ne souffre pas de n’avoir pas d’ailes', 'ex'],
    [['s15', 'mais'], 'Le sage désire ce qui est à sa portée', 'ex'],
  ],
};
const copie = (a, o = {}) => Object.assign({}, COPIE, { a }, o);
window.PLAN = S => S.plans([
  // s1 « Ce sujet peut tomber au bac. Tu as 60 secondes pour le plan. »
  { a: ['s1', 0], av: .2, type: 'chrono', t: 'CE SUJET PEUT|TOMBER AU BAC', ch: 0 },
  { a: ['s1', 'tu'], type: 'chrono', run: true, t: 'TU AS 60 SECONDES|POUR LE PLAN' },
  // s2 « Faut-il renoncer à ses désirs pour être heureux ? »
  { a: ['s2', 0], type: 'bac', sujet: ['Faut-il renoncer à ses désirs', 'pour être heureux ?'] },
  // s3 « Le piège ? Il tient en deux mots. »
  { a: ['s3', 0], type: 'mot', t: 'LE PIÈGE ?', sombre: true, choc: true, ch: 1 },
  { a: ['s3', 'il'], type: 'loupe', cercles: [[['s3', 'deux'], 'renoncer'], [['s3', 'mots'], 'ses']], t: 'DEUX MOTS|PORTENT TOUT' },
  // s4 « Renoncer : pas être privé, mais choisir de lâcher. Et ses désirs : tous ? Ou certains ? »
  { a: ['s4', 0], type: 'loupe', cercles: [[['s4', 0], 'renoncer']], t: '« RENONCER »',
    lignes: [[['s4', 'pas'], 'PAS ÊTRE PRIVÉ', 'barre'], [['s4', 'choisir'], 'CHOISIR DE LÂCHER', 'or']] },
  { a: ['s4', 'ses'], av: .4, type: 'loupe', cercles: [[['s4', 'ses'], 'ses']], t: '« SES » DÉSIRS',
    lignes: [[['s4', 'tous'], 'TOUS ?', 'creme'], [['s4', 'certains'], 'OU CERTAINS ?', 'or']] },
  // s5 « Voilà ta problématique : faut-il renoncer à tous ses désirs, ou seulement à certains ? »
  { a: ['s5', 0], type: 'mot', t: 'TA PROBLÉMATIQUE' },
  copie(['s5', 'faut-il'], { souligne: [['s5', 'certains'], 1] }),
  // s6 « Première partie : oui. Le désir est un manque sans fin. »
  copie(['s6', 0], { ch: 2 }),
  { a: ['s6', 'désir'], type: 'mot', t: 'UN MANQUE|SANS FIN' },
  // s7 « Platon parle de tonneaux percés : tu verses, tu verses, jamais pleins. »
  { a: ['s7', 0], type: 'portrait', img: 'platon', t: 'PLATON', sous: 'les tonneaux percés' },
  { a: ['s7', 'tu'], type: 'tonneau', t: 'TU VERSES, TU VERSES…', t2: 'JAMAIS PLEIN', a2: ['s7', 'jamais'] },
  // s8 « Ton exemple : toi, ce soir. La vidéo suivante, puis la suivante. »
  copie(['s8', 0]),
  { a: ['s8', 'la'], type: 'phone', coups: [['s8', 'suivante'], ['s8', -1]] },
  // s9 « Deuxième partie : pourtant, sans désir, on ne vit plus. »
  copie(['s9', 0], { ch: 3 }),
  { a: ['s9', 'sans'], type: 'mot', t: 'SANS DÉSIR…|ON NE VIT PLUS', sombre: true },
  // s10 « Sinon, disait Calliclès, les pierres seraient les plus heureuses. »
  { a: ['s10', 0], type: 'pierres', couronne: ['s10', 'heureuses'], t: 'LES PIERRES|LES PLUS HEUREUSES ?' },
  // s11 « Et Rousseau : malheur à qui n'a plus rien à désirer ! »
  { a: ['s11', 0], type: 'portrait', img: 'rousseau', t: 'ROUSSEAU', sous: 'Julie ou la Nouvelle Héloïse' },
  { a: ['s11', 'malheur'], type: 'cite', img: 'rousseau', nom: 'ROUSSEAU', q: '« Malheur à qui n’a plus|rien à désirer ! »',
    src: 'Julie ou la Nouvelle Héloïse, 1761', aq: ['s11', 'malheur'], duree: 1.8 },
  // s12 « Troisième partie : ne pas supprimer ses désirs, mais les régler. »
  copie(['s12', 0], { ch: 4 }),
  { a: ['s12', 'mais'], type: 'mot', t: 'PAS SUPPRIMER…|RÉGLER' },
  // s13 « Descartes : mieux vaut changer ses désirs que l'ordre du monde. »
  { a: ['s13', 0], type: 'cite', img: 'descartes', nom: 'DESCARTES', q: '« … à changer mes désirs|que l’ordre du monde »',
    src: 'Discours de la méthode, IIIᵉ partie, 1637', aq: ['s13', 'mieux'], duree: 1.8 },
  // s14 « Exemple : tu n'as pas d'ailes. Et ça ne te fait pas souffrir. »
  { a: ['s14', 0], type: 'ailes', etapes: [[null, 'TU N’AS PAS|D’AILES…']] },
  { a: ['s14', 'et'], type: 'ailes', vole: true, etapes: [[null, 'ET ÇA NE TE FAIT|PAS SOUFFRIR']] },
  // s15 « Le sage désire encore : mais ce qui est à sa portée. »
  copie(['s15', 0], { souligne: [['s15', 'portée'], 8] }),
  // s16 « L'erreur à ne pas faire : une troisième partie qui dit « ça dépend ». »
  { a: ['s16', 0], type: 'mot', t: 'L’ERREUR|À NE PAS FAIRE', sombre: true, choc: true },
  { a: ['s16', 'une'], type: 'erreur', barre: ['s16', 'dépend'] },
  // s17 « Elle doit déplacer la question : supprimer ses désirs, ou les régler. »
  { a: ['s17', 0], type: 'reglage', sup: ['s17', 'supprimer'], reg: ['s17', 'régler'] },
  // s18 « Le cours complet est sur Révisions Animées. »
  { a: ['s18', 0], type: 'chaine', serie: 'Le bonheur', fond: 'tantale' },
  // s19 « Et toi… tu renoncerais à quoi ? » (relance la question du début)
  { a: ['s19', 0], type: 'mot', t: 'ET TOI…|TU RENONCERAIS À QUOI ?' },
]);
window.CHAPITRES = ['LE SUJET', 'LE PIÈGE', 'PARTIE I', 'PARTIE II', 'PARTIE III'];
window.IMAGES = {
  platon: '../../philo/serie/img/platon.jpg',          // Raphaël, L'École d'Athènes (détail), domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',      // Maurice Quentin de La Tour, 1753, domaine public
  descartes: '../../philo/serie/img/descartes.jpg',    // d'après Frans Hals, domaine public
  danaides: '../../philo/serie/img/t-danaides.jpg',    // John William Waterhouse, Les Danaïdes, 1906, domaine public
  pierres: '../../philo/serie/img/bh6-pierres.jpg',    // Carl Gustav Carus, Tumulus de l'âge de pierre, vers 1820, domaine public
  tantale: '../../philo/serie/img/bh6-tantale.jpg',    // Gioacchino Assereto, Tantale, vers 1640, domaine public
};
window.MUSIQUE = 'lofi';   // musique imposée pour ce short (format 2, rythme posé)
