// Découpage du short Gammare (« Ce n'est pas lui qui décide »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Ce petit crustacé nage droit vers la mort. Et ce n'est pas lui qui décide. »
  { a: ['s1', 0], av: .25, type: 'riviere', pos: 'monte', parasite: true, oiseau: 'ombre', t: 'IL NAGE DROIT|VERS LA MORT', ch: 0 },
  { a: ['s1', 'et'], type: 'mot', t: 'CE N’EST PAS LUI|QUI DÉCIDE', choc: true },
  // s2 « Quelqu'un est aux commandes. À l'intérieur de lui. »
  { a: ['s2', 0], type: 'marionnette', t: 'QUELQU’UN EST|AUX COMMANDES' },
  { a: ['s2', "l'intérieur"], av: .3, type: 'marionnette', zoom: true, t: 'À L’INTÉRIEUR|DE LUI' },
  // s3 « Tu es un gammare. Un petit crustacé d'eau douce. »
  { a: ['s3', 0], type: 'portrait', img: 'gammare', t: 'GAMMARE', sous: 'c’est toi', ch: 1 },
  { a: ['s3', 'petit'], av: .3, type: 'riviere', pos: 'fond', t: 'UN PETIT CRUSTACÉ|D’EAU DOUCE' },
  // s4 « Ta règle de survie : rester au fond, à l'abri. Là-haut, il y a les oiseaux. »
  { a: ['s4', 0], type: 'riviere', pos: 'fond', t: 'TA RÈGLE DE SURVIE :|RESTER AU FOND' },
  { a: ['s4', 'là-haut'], type: 'riviere', pos: 'fond', oiseau: 'ombre', t: 'LÀ-HAUT…|LES OISEAUX' },
  // s5 « Un jour, un minuscule ver parasite entre dans ton corps. »
  { a: ['s5', 0], type: 'mot', t: 'UN JOUR…', sombre: true },
  { a: ['s5', 'minuscule'], type: 'ver', etape: 'entre', t: 'UN VER|PARASITE' },
  // s6 « Il s'installe. Il s'enferme dans une coque : un kyste. »
  { a: ['s6', 0], type: 'ver', etape: 'kyste', kyste: ['s6', 'kyste'], t: 'IL S’ENFERME|DANS UNE COQUE' },
  // s7 « Et là, tout change. »
  { a: ['s7', 0], type: 'mot', t: 'ET LÀ,|TOUT CHANGE.', choc: true },
  // s8 « La lumière t'attire. Tu quittes le fond. Tu remontes… jusqu'à la surface. »
  { a: ['s8', 0], type: 'riviere', pos: 'fond', parasite: true, lumiere: true, t: 'LA LUMIÈRE|T’ATTIRE', ch: 2 },
  { a: ['s8', 'tu'], type: 'riviere', pos: 'monte', parasite: true, lumiere: true, t: 'TU QUITTES LE FOND|TU REMONTES' },
  // s9 « Là-haut, tu tournoies. Frénétiquement. »
  { a: ['s9', 0], type: 'riviere', pos: 'surface', parasite: true, t: 'TU TOURNOIES|FRÉNÉTIQUEMENT' },
  // s10 « Un oiseau passe. Tu es la proie parfaite. »
  { a: ['s10', 0], type: 'riviere', pos: 'surface', parasite: true, oiseau: 'ombre', t: 'UN OISEAU|PASSE', ch: 3 },
  { a: ['s10', 'tu'], type: 'riviere', pos: 'surface', parasite: true, cible: true, t: 'LA PROIE|PARFAITE' },
  // s11 « Coup de bec. Fin de l'histoire ? Non. »
  { a: ['s11', 0], type: 'bec', t: 'COUP DE BEC', choc: true },
  { a: ['s11', 'fin'], type: 'mot', t: 'FIN DE L’HISTOIRE ?', petit: true },
  { a: ['s11', 'non'], type: 'mot', t: 'NON.', sombre: true },
  // s12 « Pour le parasite, c'est la suite du voyage. Dans l'intestin de l'oiseau, il devient adulte et se reproduit. »
  { a: ['s12', 0], type: 'cycle', etape: 1, t: 'LA SUITE|DU VOYAGE' },
  { a: ['s12', 'dans'], type: 'cycle', etape: 2, repro: ['s12', 'reproduit'], t: 'IL DEVIENT ADULTE|ET SE REPRODUIT' },
  // s13 « Toi, tu étais son habitat, sa nourriture… et son taxi. »
  { a: ['s13', 0], type: 'fiche', sur: 'POUR LE PARASITE', t: 'TOI, TU ÉTAIS…', items: [
    [['s13', 'habitat'], 'SON HABITAT'], [['s13', 'nourriture'], 'SA NOURRITURE'], [['s13', 'taxi'], 'SON TAXI', 'jusqu’à l’oiseau']] },
  // s14 « Le plus fou ? Tes gènes n'ont pas changé. C'est ton comportement qui a été piraté. »
  { a: ['s14', 0], type: 'mot', t: 'LE PLUS FOU ?', ch: 4 },
  { a: ['s14', 'tes'], type: 'genes', t: 'TES GÈNES|N’ONT PAS CHANGÉ' },
  { a: ['s14', "c'est"], type: 'genes', pirate: ['s14', 'piraté'], t: 'TON COMPORTEMENT|A ÉTÉ PIRATÉ' },
  // s15 « Pour les biologistes, ton comportement fait partie du phénotype étendu du parasite. »
  { a: ['s15', 0], type: 'mot', t: 'POUR LES|BIOLOGISTES…' },
  { a: ['s15', 'ton'], type: 'etendu', t: 'PHÉNOTYPE ÉTENDU|DU PARASITE' },
  // s16 « Montrez que le phénotype peut se diversifier sans modification du génome : sujet type bac.
  //       La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'bacsvt', sujet: ['Montrez que le phénotype', 'peut se diversifier', 'sans modification', 'du génome.'] },
  { a: ['s16', 'sujet'], type: 'tampon', t: 'TYPE BAC' },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'SVT · chapitre 4', fond: 'gammare' },
  // s17 « La prochaine fois que tu fonces vers quelque chose… es-tu sûr que c'est toi qui décides ? » (boucle vers le début)
  { a: ['s17', 0], type: 'riviere', pos: 'monte', parasite: true, t: 'LA PROCHAINE FOIS|QUE TU FONCES…' },
  { a: ['s17', 'es-tu'], type: 'marionnette', t: 'ES-TU SÛR QUE|C’EST TOI QUI DÉCIDES ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE GAMMARE', 'LA MANIPULATION', "L'OISEAU", 'LE PHÉNOTYPE ÉTENDU'];
window.IMAGES = {
  gammare: '../../svt/serie/img/ch4-gammare.jpg',   // un gammare (Gammarus pulex), photo Alexis Tinker-Tsavalas, iNaturalist, CC BY
};

window.MUSIQUE = 'phonk_sombre';   // musique imposée pour ce short
