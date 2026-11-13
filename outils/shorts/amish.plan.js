// Découpage du short Amish (« Un seul couple »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Comment un seul couple peut-il marquer les gènes de toute une communauté ? »
  { a: ['s1', 0], av: .25, type: 'arbre', etape: 'hook', t: 'UN SEUL|COUPLE…', ch: 0 },
  { a: ['s1', 'les'], type: 'portrait', img: 'amish', t: 'TOUTE UNE COMMUNAUTÉ', sous: 'marquée par un seul couple ?' },
  // s2 « Pendant plus de 200 ans. Sans le savoir. »
  { a: ['s2', 0], type: 'mot', t: 'PENDANT PLUS|DE 200 ANS' },
  { a: ['s2', 'sans'], type: 'mot', t: 'SANS LE SAVOIR.', sombre: true, choc: true },
  // s3 « XVIIIe siècle. Tu es amish, en couple, et tu quittes l'Europe pour la Pennsylvanie. »
  { a: ['s3', 0], type: 'mot', t: 'XVIIIᵉ|SIÈCLE', ch: 1 },
  { a: ['s3', 'tu'], type: 'mot', img: 'amish', t: 'TU ES AMISH,|EN COUPLE' },
  { a: ['s3', 'quittes'], type: 'traversee', t: 'DE L’EUROPE|À LA PENNSYLVANIE' },
  // s4 « Quelques immigrants fondent une communauté à l'écart. On se marie au sein du groupe. »
  { a: ['s4', 0], type: 'village', mode: 'fonde', t: 'QUELQUES|IMMIGRANTS' },
  { a: ['s4', 'on'], type: 'village', mode: 'cercle', t: 'ON SE MARIE|AU SEIN DU GROUPE' },
  // s5 « Mais l'un de vous deux porte un secret : un allèle muté rare. »
  { a: ['s5', 0], type: 'village', mode: 'cercle', porteur: ['s5', 'secret'], t: 'L’UN DE VOUS DEUX|PORTE UN SECRET', ch: 2 },
  { a: ['s5', 'allèle'], type: 'chromo', copies: 1, t: 'UN ALLÈLE|MUTÉ, RARE' },
  // s6 « Un seul exemplaire : aucun symptôme. »
  { a: ['s6', 0], type: 'chromo', copies: 1, t: 'UN SEUL EXEMPLAIRE|AUCUN SYMPTÔME' },
  // s7 « Il passe à vos enfants, à vos petits-enfants… en silence. »
  { a: ['s7', 0], type: 'arbre', etape: 'transmet', t: 'DE GÉNÉRATION|EN GÉNÉRATION' },
  // s8 « Puis, dans une si petite communauté, deux porteurs ont un enfant ensemble. »
  { a: ['s8', 0], type: 'mot', t: 'UNE SI PETITE|COMMUNAUTÉ', ch: 3 },
  { a: ['s8', 'deux'], type: 'arbre', etape: 'rencontre', t: 'DEUX|PORTEURS' },
  { a: ['s8', 'enfant'], type: 'arbre', etape: 'enfant', t: 'UN ENFANT' },
  // s9 « Cet enfant reçoit l'allèle deux fois. Et là, il se révèle. »
  { a: ['s9', 0], type: 'chromo', copies: 2, t: 'L’ALLÈLE|DEUX FOIS' },
  { a: ['s9', 'et'], type: 'mot', t: 'ET LÀ,|IL SE RÉVÈLE', choc: true },
  // s10 « Le syndrome d'Ellis-van Creveld : une très petite taille, et souvent un sixième doigt. »
  { a: ['s10', 0], type: 'syndrome', etape: 'nom' },
  { a: ['s10', 'très'], type: 'syndrome', etape: 'signes', taille: ['s10', 'taille'], doigt: ['s10', 'sixième'] },
  // s11 « Ailleurs dans le monde : à peine 1 naissance sur 60 000. »
  { a: ['s11', 0], type: 'frequence', etape: 1 },
  // s12 « Chez les Amish de Pennsylvanie, l'allèle atteint 7 pour cent. »
  { a: ['s12', 0], type: 'frequence', etape: 2, choc: true },
  // s13 « Toutes les familles touchées ont la même mutation. Elles descendent du même couple. »
  { a: ['s13', 0], type: 'arbre', etape: 'meme', t: 'LA MÊME|MUTATION' },
  { a: ['s13', 'elles'], type: 'arbre', etape: 'couple', t: 'LE MÊME|COUPLE', choc: true },
  // s14 « Ce n'est pas un mystère : c'est l'effet fondateur. »
  { a: ['s14', 0], type: 'mot', t: 'CE N’EST PAS|UN MYSTÈRE', ch: 4 },
  { a: ['s14', "c'est"], type: 'tampon', t: 'EFFET FONDATEUR' },
  // s15 « Les fondateurs n'emportent qu'un échantillon des allèles, tiré au hasard. Puis la dérive génétique fait le reste. »
  { a: ['s15', 0], type: 'echantillon', t: 'UN ÉCHANTILLON|TIRÉ AU HASARD' },
  { a: ['s15', 'puis'], type: 'derive', t: 'LA DÉRIVE GÉNÉTIQUE|FAIT LE RESTE' },
  // s16 « Montrez que la dérive génétique peut modifier la diversité d'une population : sujet type bac.
  //       La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'bacsvt', sujet: ['Montrez que la dérive', 'génétique peut modifier', 'la diversité', 'd’une population.'] },
  { a: ['s16', 'sujet'], type: 'tampon', t: 'TYPE BAC' },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'SVT · chapitre 3', fond: 'amish' },
  // s17 « Le hasard ne change rien ? Un seul couple a suffi. » (boucle vers le début)
  { a: ['s17', 0], type: 'mot', t: 'LE HASARD|NE CHANGE RIEN ?' },
  { a: ['s17', 'un'], type: 'arbre', etape: 'hook', t: 'UN SEUL COUPLE|A SUFFI.' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE VOYAGE', 'LE SECRET', 'LA RÉVÉLATION', "L'EFFET FONDATEUR"];
window.IMAGES = {
  amish: '../../svt/serie/img/ch3-amish.jpg',   // buggy amish sur une route de Pennsylvanie, photo Ad Meskens, CC BY-SA 3.0 (attribution obligatoire)
};

window.MUSIQUE = 'funk_bresil';   // musique imposée pour ce short
