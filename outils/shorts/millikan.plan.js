// Découpage du short Millikan (« Il voulait prouver qu'Einstein avait tort »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Tu passerais 10 ans à prouver qu'Einstein a tort… pour finir par lui donner raison ? »
  { a: ['s1', 0], av: .25, type: 'annees', t: 'TU PASSERAIS|10 ANS…', ch: 0 },
  { a: ['s1', 'prouver'], type: 'tort', t: 'À PROUVER|QU’IL A TORT ?' },
  { a: ['s1', 'pour'], type: 'tort', raison: ['s1', 'raison'], t: 'POUR FINIR PAR|LUI DONNER RAISON ?' },
  // s2 « Robert Millikan, lui, l'a fait. »
  { a: ['s2', 0], type: 'perso', img: 'millikan', t: 'ROBERT MILLIKAN', sous: 'physicien américain · 1868 – 1953' },
  // s3 « 1905. Albert Einstein, jeune employé des brevets, ose une idée folle : la lumière est faite de grains. »
  { a: ['s3', 0], type: 'date', t: '1905', de: 1880, sous: 'BERNE · OFFICE DES BREVETS', ch: 1 },
  { a: ['s3', 'jeune'], type: 'perso', img: 'einstein', t: 'ALBERT EINSTEIN', sous: 'jeune employé des brevets' },
  { a: ['s3', 'idée'], type: 'mot', t: 'UNE IDÉE|FOLLE' },
  { a: ['s3', 'lumière'], type: 'grains' },
  // s4 « Pour arracher un électron à un métal, c'est la fréquence qui compte. Pas l'intensité. »
  { a: ['s4', 0], type: 'metal', mode: 'rouge' },
  { a: ['s4', 'fréquence'], type: 'metal', mode: 'uv', t: 'LA FRÉQUENCE', pas: ['s4', 'pas'] },
  // s5 « Toi, tu es Millikan. Pour toi, c'est absurde : depuis un siècle, la lumière est une onde. »
  { a: ['s5', 0], type: 'portrait', img: 'millikan', t: 'TOI', sous: 'tu es Millikan' },
  { a: ['s5', 'pour'], type: 'mot', t: 'POUR TOI :|ABSURDE', sombre: true },
  { a: ['s5', 'depuis'], type: 'onde' },
  // s6 « Tu veux la mesure parfaite. Celle qui fera tomber Einstein. »
  { a: ['s6', 0], type: 'mot', t: 'LA MESURE|PARFAITE', ch: 2 },
  { a: ['s6', 'celle'], type: 'cible' },
  // s7 « Problème : la moindre couche d'oxyde sur le métal fausse tout. »
  { a: ['s7', 0], type: 'mot', t: 'PROBLÈME', sombre: true },
  { a: ['s7', 'couche'], type: 'oxyde', faux: ['s7', 'fausse'] },
  // s8 « Alors tu construis un atelier… dans le vide. Un couteau, guidé par des aimants, rabote le sodium sous vide. »
  { a: ['s8', 0], type: 'tube', etape: 0 },
  { a: ['s8', 'couteau'], type: 'tube', etape: 1 },
  { a: ['s8', 'rabote'], type: 'tube', etape: 2 },
  // s9 « Tu éclaires. Tu mesures. Fréquence après fréquence. Pendant 10 ans. »
  { a: ['s9', 0], type: 'mesure' },
  { a: ['s9', 'pendant'], type: 'annees', t: 'PENDANT|10 ANS' },
  // s10 « 1916. Le verdict tombe. »
  { a: ['s10', 0], type: 'date', t: '1916', de: 1906, sous: 'LE VERDICT', ch: 3 },
  // s11 « Tes points s'alignent. Une droite parfaite. Exactement celle d'Einstein. »
  { a: ['s11', 0], type: 'droite', etape: 1, ligne: ['s11', 'une'] },
  { a: ['s11', 'exactement'], type: 'droite', etape: 2, choc: true },
  // s12 « Pire : sa pente te donne la constante de Planck. »
  { a: ['s12', 0], type: 'mot', t: 'PIRE…', sombre: true },
  { a: ['s12', 'pente'], type: 'droite', etape: 3, h: ['s12', 'constante'] },
  // s13 « Le plus fou ? Même là, tu n'y crois pas. Tu écris que son idée est téméraire. »
  { a: ['s13', 0], type: 'mot', t: 'LE PLUS FOU ?' },
  { a: ['s13', 'même'], type: 'portrait', img: 'millikan', t: 'TU N’Y CROIS PAS', sous: 'même après tes mesures' },
  { a: ['s13', 'écris'], type: 'article' },
  { a: ['s13', 'téméraire'], type: 'article', tampon: ['s13', 'téméraire'], choc: true },
  // s14 « Einstein reçoit le Nobel 1921 pour l'effet photoélectrique, pas pour la relativité. Toi, celui de 1923. »
  { a: ['s14', 0], type: 'nobel', img: 'einstein', an: '1921', t: 'EINSTEIN', sous: 'pour l’effet photoélectrique', asous: ['s14', "l'effet"], ch: 4 },
  { a: ['s14', 'pas'], type: 'mot', t: 'PAS POUR|LA RELATIVITÉ', choc: true },
  { a: ['s14', 'toi'], type: 'nobel', img: 'millikan', an: '1923', t: 'MILLIKAN', sous: 'en partie pour l’effet photoélectrique' },
  // s15 « C'est le chapitre 4 de physique. Établir la relation d'Einstein : vraie question de bac. »
  { a: ['s15', 0], type: 'mot', t: 'CHAPITRE 4|LA LUMIÈRE, DES PHOTONS', petit: true },
  { a: ['s15', 'établir'], type: 'sujetpc', formule: 'h × ν = Φ + Ec' },
  // s16 « La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'chaine', serie: 'Physique · chapitre 4', fond: 'einstein' },
  // s17 « Et toi… tu passerais 10 ans à prouver qu'Einstein a tort ? » (boucle vers le début)
  { a: ['s17', 0], type: 'mot', t: 'ET TOI…', sombre: true },
  { a: ['s17', 'passerais'], type: 'annees', t: 'TU PASSERAIS|10 ANS…' },
  { a: ['s17', 'prouver'], type: 'tort', t: 'À PROUVER|QU’IL A TORT ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'L’IDÉE FOLLE', 'LA TRAQUE', 'LE VERDICT', 'LE NOBEL'];
window.IMAGES = {
  millikan: '../../pc/serie/img/millikan.jpg',   // Robert Millikan, portrait de la Fondation Nobel, domaine public
  einstein: '../../pc/serie/img/einstein.jpg',   // Albert Einstein, photo Herman Mishkin, 1921, domaine public
};

window.MUSIQUE = 'trap';   // musique propre à ce short (08/11/2026 : une musique différente par short)
