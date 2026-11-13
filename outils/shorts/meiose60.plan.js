// Découpage du short « meiose60 » (format 3, résumé express : « La méiose en 60 secondes »), modèle A.
// a: [passage, mot] ; av : avance sur le mot. La fiche revient à chaque idée et se remplit (une case cochée par idée).
const FICHE = {
  type: 'fiche', sur: 'LA MÉIOSE EN 60 SECONDES', t: '5 IDÉES', items: [
    [['s2', 0], 'Méiose : de 2n à n', '1 cellule, 2 divisions, 4 gamètes'],
    [['s4', 0], 'Prophase I : crossing-over', 'brassage intrachromosomique'],
    [['s7', 0], 'Anaphase I : les paires se séparent', 'brassage interchromosomique · 2²³'],
    [['s10', 0], 'La fécondation', 'de l’ordre de 70 000 milliards de combinaisons'],
    [['s12', 0], 'Le piège', 'intra = prophase I · inter = anaphase I'],
  ],
};
const fiche = (a, o = {}) => Object.assign({}, FICHE, { a }, o);
window.PLAN = S => S.plans([
  // s1 « La méiose en 60 secondes. 5 idées pour le bac. »
  { a: ['s1', 0], av: .2, type: 'chrono', run: true, t: 'LA MÉIOSE|EN 60 SECONDES', ch: 0 },
  { a: ['s1', '5'], type: 'mot', t: '5 IDÉES|POUR LE BAC' },
  // s2 « Idée 1 : une cellule à 46 chromosomes, notée 2n, se divise deux fois de suite. »
  fiche(['s2', 0]),
  { a: ['s2', 'une'], type: 'divisions', etape: 0 },
  { a: ['s2', 'deux'], type: 'divisions', etape: 2, t: 'DEUX DIVISIONS|DE SUITE' },
  // s3 « Résultat : 4 gamètes à 23 chromosomes, notés n. Le nombre est divisé par deux. »
  { a: ['s3', 0], type: 'divisions', etape: 3 },
  { a: ['s3', 'le'], type: 'mot', t: 'LE NOMBRE EST|DIVISÉ PAR DEUX' },
  // s4 « Idée 2 : en prophase I, les chromosomes homologues s'apparient, en blocs de 4 chromatides. »
  fiche(['s4', 0], { ch: 1 }),
  { a: ['s4', 'les'], type: 'bivalent', etape: 'apparie', t: 'LES HOMOLOGUES|S’APPARIENT' },
  // s5 « Deux chromatides non sœurs se croisent en un chiasma, se cassent et échangent leurs morceaux. »
  { a: ['s5', 0], type: 'bivalent', etape: 'chiasma', t: 'DEUX CHROMATIDES|NON SŒURS SE CROISENT' },
  { a: ['s5', 'cassent'], av: .3, type: 'bivalent', etape: 'echange', t: 'ELLES ÉCHANGENT|LEURS MORCEAUX' },
  // s6 « C'est le crossing-over : le brassage intrachromosomique. De nouvelles combinaisons d'allèles sur un même chromosome. »
  { a: ['s6', 0], type: 'mot', t: 'CROSSING-OVER|BRASSAGE INTRA', choc: true },
  { a: ['s6', 'de'], type: 'bivalent', etape: 'resultat', t: 'DE NOUVELLES|COMBINAISONS' },
  // s7 « Idée 3 : en métaphase I, les paires se placent au hasard autour de l'équateur. »
  fiche(['s7', 0], { ch: 2 }),
  { a: ['s7', 'les'], type: 'meta', etape: 'meta' },
  // s8 « En anaphase I, les homologues se séparent : c'est le brassage interchromosomique. »
  { a: ['s8', 0], type: 'meta', etape: 'ana' },
  { a: ['s8', "c'est"], type: 'mot', t: 'BRASSAGE|INTERCHROMOSOMIQUE' },
  // s9 « 2 possibilités par paire, 23 paires : 2 puissance 23. Plus de 8 millions de gamètes différents ! »
  { a: ['s9', 0], type: 'puissance', etape: 1 },
  { a: ['s9', 'plus'], type: 'puissance', etape: 2, choc: true },
  // s10 « Idée 4 : la fécondation réunit deux gamètes au hasard. 23 plus 23 : 46. »
  fiche(['s10', 0], { ch: 3 }),
  { a: ['s10', 'la'], type: 'fecond', somme: ['s10', 9] },
  // s11 « 8 millions fois 8 millions : de l'ordre de 70 000 milliards de combinaisons par couple. »
  { a: ['s11', 0], type: 'milliards' },
  { a: ['s11', "l'ordre"], type: 'milliards', big: ['s11', "l'ordre"] },
  // s12 « Idée 5 : le piège. Ne confonds pas les deux brassages. »
  fiche(['s12', 0], { ch: 4 }),
  { a: ['s12', 'ne'], type: 'mot', t: 'NE CONFONDS PAS|LES DEUX BRASSAGES' },
  // s13 « Intra : dans une même paire, en prophase I. Inter : entre paires différentes, en anaphase I. »
  { a: ['s13', 0], type: 'piege', intra: ['s13', 0], inter: ['s13', 'inter'] },
  { a: ['s13', 'inter'], type: 'piege', inter: ['s13', 'inter'] },
  // s14 « Et ils se cumulent, à chaque méiose. »
  { a: ['s14', 0], type: 'piege', cumul: true },
  { a: ['s14', 'à'], type: 'mot', t: 'À CHAQUE|MÉIOSE' },
  // s15 « Toute la vidéo du chapitre 1 est sur Révisions Animées. »
  { a: ['s15', 0], type: 'chaine', serie: 'SVT · chapitre 1', fond: 'drosophiles' },
  // s16 « Alors : combien d'idées tu connaissais déjà ? »
  fiche(['s16', 0], { sur: 'TU EN CONNAISSAIS COMBIEN ?', t: '… / 5' }),
]);
window.CHAPITRES = ['ACCROCHE · IDÉE 1', 'LE CROSSING-OVER', "L'ANAPHASE I", 'LA FÉCONDATION', 'LE PIÈGE'];
window.IMAGES = {
  drosophiles: '../../svt/serie/img/ch1-drosophiles.jpg',   // tubes de culture de drosophiles, photo Masur, CC BY-SA 4.0 (Wikimedia Commons, attribution obligatoire)
};

window.MUSIQUE = 'house';   // musique imposée pour ce short (format 3, rythme rapide)
