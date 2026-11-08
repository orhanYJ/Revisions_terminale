// Découpage du short « La lunette astronomique en 60 secondes », modèle A. a: [passage, mot] ; av : avance sur le mot.
// Les cinq idées du résumé (plan « fiche » repris à chaque idée : les items s'allument à leur repère).
const IDEES = [
  [['s3', 'idée'], 'L’objectif → image intermédiaire', 'réelle, renversée, dans son plan focal image'],
  [['s5', 'idée'], 'Réglage afocal : F′₁ = F₂', 'O₁O₂ = f′₁ + f′₂'],
  [['s7', 'idée'], 'Les rayons ressortent parallèles', 'image à l’infini : l’œil n’accommode pas'],
  [['s9', 'idée'], 'L’image est renversée', 'les rayons descendent, puis remontent'],
  [['s11', 'idée'], 'G = α′ / α = f′₁ / f′₂', 'le rapport des angles'],
];
const FICHE = { type: 'fiche', sur: 'RÉSUMÉ EXPRESS', t: 'LA LUNETTE EN 5 IDÉES', items: IDEES };
window.PLAN = S => S.plans([
  // s1 « La lunette astronomique en 60 secondes. C'est parti. »
  { a: ['s1', 0], av: .25, type: 'chrono60', ch: 0 },
  { a: ['s1', "c'est"], type: 'mot', t: 'C’EST PARTI' },
  // s2 « Une lunette, c'est 2 lentilles convergentes. L'objectif, côté ciel. L'oculaire, côté œil. »
  { a: ['s2', 0], type: 'lunette', t: '2 LENTILLES|CONVERGENTES' },
  { a: ['s2', "l'objectif"], type: 'lunette', hl: 'l1', t: 'L’OBJECTIF|CÔTÉ CIEL' },
  { a: ['s2', "l'oculaire"], type: 'lunette', hl: 'l2', t: 'L’OCULAIRE|CÔTÉ ŒIL' },
  // s3 « Idée 1 : l'objectif forme une image réelle de l'astre, dans son plan focal image. »
  Object.assign({ a: ['s3', 0], ch: 1 }, FICHE),
  { a: ['s3', 'image'], type: 'lunette', l2: false, hl: 'l1', rayons: 1, image: true, t: 'UNE IMAGE RÉELLE|ET RENVERSÉE' },
  { a: ['s3', 'plan'], type: 'lunette', l2: false, rayons: 1, trace: .25, image: true, plan: ['s3', 'plan'], t: 'DANS SON PLAN|FOCAL IMAGE' },
  // s4 « La Lune, avec un objectif de 700 millimètres ? Une image d'environ 6 millimètres. »
  { a: ['s4', 0], type: 'photo', img: 'lune', z: 4.2, fx: .508, fy: .52, t: 'LA LUNE', sous: 'objectif de 700 mm' },
  { a: ['s4', 'une'], type: 'lune', etape: 'taille' },
  // s5 « Idée 2 : réglage afocal. Le foyer image de l'objectif coïncide avec le foyer objet de l'oculaire. »
  Object.assign({ a: ['s5', 0], ch: 2 }, FICHE),
  { a: ['s5', 'le'], type: 'lunette', f1: ['s5', 'foyer'], t: 'FOYER IMAGE|DE L’OBJECTIF' },
  { a: ['s5', 'coïncide'], type: 'lunette', f1: ['s5', 'foyer'], f2: ['s5', 'objet'], egal: ['s5', 'objet'], t: 'FOYER OBJET|DE L’OCULAIRE', at: ['s5', 'objet'] },
  // s6 « Objectif de 50 centimètres, oculaire de 5 centimètres : 55 centimètres entre les deux. »
  { a: ['s6', 0], type: 'regle', e50: ['s6', '50'], e5: ['s6', 6], e55: ['s6', '55'] },
  // s7 « Idée 3 : les rayons ressortent parallèles. L'image est à l'infini. »
  Object.assign({ a: ['s7', 0] }, FICHE),
  { a: ['s7', 'rayons'], type: 'lunette', rayons: 2, t: 'ILS RESSORTENT|PARALLÈLES', sous: 'l’image est à l’infini', asous: ['s7', "l'image"] },
  // s8 « Ton œil la voit net sans accommoder. Tu peux observer longtemps. »
  { a: ['s8', 0], type: 'oeil' },
  { a: ['s8', 'tu'], type: 'photo', img: 'saturne', z: 1.5, fx: .5, fy: .5, t: 'TU OBSERVES|LONGTEMPS', sous: 'sans fatigue' },
  // s9 « Idée 4 : l'image est renversée. Les rayons entrent en descendant, ressortent en montant. »
  Object.assign({ a: ['s9', 0], ch: 3 }, FICHE),
  { a: ['s9', 'les'], type: 'lunette', rayons: 2, fleches: ['s9', 'ressortent'], t: 'L’IMAGE EST|RENVERSÉE' },
  // s10 « Un cratère au nord de la Lune ? Tu le vois en bas. »
  { a: ['s10', 0], type: 'lune', flip: ['s10', 'tu'] },
  // s11 « Idée 5 : le grossissement. G égale alpha prime sur alpha, le rapport des angles. »
  Object.assign({ a: ['s11', 0], ch: 4 }, FICHE),
  { a: ['s11', 4], type: 'formule', sur: 'LE GROSSISSEMENT', lignes: [[null, 'G = α′ / α', 'cadre'], [['s11', 'rapport'], 'angle dans la lunette ÷ angle à l’œil nu', 'petit']] },
  { a: ['s11', 'rapport'], type: 'lunette', rayons: 2, trace: .3, angles: true, t: 'α : À L’ŒIL NU|α′ : DANS LA LUNETTE' },
  // s12 « Pour une lunette afocale, G égale f prime 1 sur f prime 2. »
  { a: ['s12', 0], type: 'lunette', focales: true, t: 'LUNETTE|AFOCALE' },
  { a: ['s12', 'f'], type: 'formule', sur: 'LUNETTE AFOCALE', lignes: [[null, 'G = α′ / α', ''], [null, 'G = f′₁ / f′₂', 'cadre']] },
  // s13 « 700 millimètres sur 10 : elle grossit 70 fois. »
  { a: ['s13', 0], type: 'formule', sur: 'OBJECTIF 700 mm · OCULAIRE 10 mm', lignes: [[null, 'G = 700 / 10', ''], [['s13', 6], 'G = 70', 'cadre']], t: 'ELLE GROSSIT|70 FOIS' },
  // s14 « L'erreur classique : F prime 1 égale F 2. Pas F 1 égale F prime 2. »
  { a: ['s14', 0], type: 'erreur', bon: ['s14', 'f'] },
  { a: ['s14', 'pas'], type: 'erreur', faux: ['s14', 'pas'], choc: true },
  // s15 « La démonstration de G ? À savoir rédiger au bac. Elle est dans le chapitre 5, sur Révisions Animées. »
  { a: ['s15', 0], type: 'mot', t: 'LA DÉMONSTRATION|DE G ?' },
  { a: ['s15', 'à'], type: 'sujetpc', formule: 'G = α′ / α = f′₁ / f′₂' },
  { a: ['s15', 'elle'], type: 'chaine', serie: 'Physique · chapitre 5', fond: 'yerkes' },
]);
window.CHAPITRES = ['EN 60 SECONDES', 'L’OBJECTIF', 'LE RÉGLAGE AFOCAL', 'L’IMAGE RENVERSÉE', 'LE GROSSISSEMENT'];
window.IMAGES = {
  lune: '../../pc/serie/img/c5-lune.jpg',         // la pleine Lune vue depuis l'espace, NASA, domaine public
  saturne: '../../pc/serie/img/c5-saturne.jpg',   // Saturne vue par Cassini, 2004, NASA/JPL/Space Science Institute, domaine public
  yerkes: '../../pc/serie/img/c5-yerkes.jpg',     // la lunette de 40 pouces de l'observatoire Yerkes, 1897, domaine public
};

window.MUSIQUE = 'pop';   // musique propre à ce short (08/11/2026 : une musique différente par short)
