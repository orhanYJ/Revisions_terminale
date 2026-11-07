// Découpage du short Butler (« En 1993, elle a écrit 2024 »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « En 1993, une femme écrit un roman qui se passe en 2024. »
  { a: ['s1', 0], av: .25, type: 'date', t: '1993', de: 1960, sous: 'UNE FEMME ÉCRIT', ch: 0 },
  { a: ['s1', 'roman'], type: 'livre' },
  { a: ['s1', 'passe'], type: 'saut', de: 1993, vers: 2024, cle: ['s1', '2024'], sous: 'IL SE PASSE EN', choc: true },
  // s2 « Et ce qu'elle imagine… tu vas le reconnaître. »
  { a: ['s2', 0], type: 'mot', t: 'ET CE QU’ELLE|IMAGINE…' },
  { a: ['s2', 'tu'], type: 'mot', t: 'TU VAS LE|RECONNAÎTRE', sombre: true },
  // s3 « 20 juillet 2024. Tu t'appelles Lauren, tu as 15 ans. Tu vis en Californie, derrière un mur. »
  { a: ['s3', 0], type: 'journal', date: '20 juillet 2024', etapes: [[null, 'TON JOURNAL|INTIME']], ch: 1 },
  { a: ['s3', "t'appelles"], type: 'lauren', age: ['s3', '15'] },
  { a: ['s3', 'californie'], type: 'mur', lieu: 'CALIFORNIE', t: 'DERRIÈRE|UN MUR' },
  // s4 « Dehors, l'eau coûte plus cher que l'essence. Les incendies ne s'arrêtent plus. »
  { a: ['s4', 0], type: 'eau' },
  { a: ['s4', 'incendies'], type: 'ville' },
  // s5 « Une nouvelle drogue se répand : elle donne envie de mettre le feu. »
  { a: ['s5', 0], type: 'mot', t: 'UNE NOUVELLE|DROGUE' },
  { a: ['s5', 'elle'], type: 'yeux' },
  { a: ['s5', 'mettre'], type: 'flammes', choc: true },
  // s6 « Toi, tu caches un secret : quand quelqu'un souffre devant toi… tu ressens sa douleur. »
  { a: ['s6', 0], type: 'mot', t: 'TOI, TU CACHES|UN SECRET' },
  { a: ['s6', 'quand'], type: 'empathie', mal: ['s6', 'souffre'], toi: ['s6', 'ressens'],
    etapes: [[null, 'QUAND QUELQU’UN|SOUFFRE…'], [['s6', 'ressens'], 'TU RESSENS|SA DOULEUR']] },
  // s7 « Trois ans plus tard. Une nuit, un camion enfonce le portail. »
  { a: ['s7', 0], type: 'saut', de: 2024, vers: 2027, cle: ['s7', 'tard'], t: 'TROIS ANS|PLUS TARD', ch: 2 },
  { a: ['s7', 'une'], type: 'portail', t: 'UNE NUIT…' },
  { a: ['s7', 'enfonce'], type: 'portail', crash: true, choc: true, t: 'LE PORTAIL|CÈDE' },
  // s8 « Des visages peints. Des flammes. Ton quartier brûle. »
  { a: ['s8', 0], type: 'visages' },
  { a: ['s8', 'ton'], type: 'mur', feu: true, t: 'TON QUARTIER|BRÛLE' },
  { a: ['s8', 'brûle'], av: -.3, type: 'silence', silence: true, muet: true, t: '… puis le silence.' },
  // s9 « Tu t'enfuis vers le nord, à pied, avec ton journal. »
  { a: ['s9', 0], type: 'route' },
  // s10 « Dans ce journal, tu inventes une religion : God is Change. Dieu est changement. »
  { a: ['s9', 'avec'], type: 'journal', mot: ['EARTHSEED', ['s10', 'religion']],
    etapes: [[null, 'AVEC TON|JOURNAL'], [['s10', 'inventes'], 'TU INVENTES|UNE RELIGION']] },
  { a: ['s10', 'god'], type: 'citation', trad: ['s10', 'dieu'] },
  // s11 « Le plus fou ? Butler n'a rien deviné. Elle a regardé les problèmes qu'on néglige… et leur a laissé 30 ans. »
  { a: ['s11', 0], type: 'mot', t: 'LE PLUS FOU ?', ch: 3 },
  { a: ['s11', 'butler'], type: 'autrice', tampon: ['s11', 'rien'] },
  { a: ['s11', 'elle'], type: 'journaux' },
  { a: ['s11', 'et'], type: 'saut', ans: true, de: 0, vers: 30, cle: ['s11', '30'], sous: 'ET ELLE LEUR LAISSE', t: 'POUR DEVENIR|DES CATASTROPHES' },
  // s12 « Sécheresse, incendies, quartiers fermés : tout était déjà là. »
  { a: ['s12', 0], type: 'liste', items: [['SÉCHERESSE', ['s12', 0]], ['INCENDIES', ['s12', 'incendies']], ['QUARTIERS FERMÉS', ['s12', 'quartiers']]], fin: ['s12', 'tout'] },
  // s13 « Et son destin à elle ? Dans un carnet, elle avait écrit : je serai une autrice de best-sellers. »
  { a: ['s13', 0], type: 'mot', t: 'ET SON DESTIN|À ELLE ?', ch: 4 },
  { a: ['s13', 'dans'], type: 'note' },
  { a: ['s13', 'je'], type: 'note', zoom: true, ecrit: ['s13', 'je'] },
  // s14 « Elle meurt en 2006. Jamais dans la liste du New York Times. »
  { a: ['s14', 0], type: 'date', t: '2006', de: 1993, sous: 'ELLE MEURT' },
  { a: ['s14', 'jamais'], type: 'classement', etape: 1 },
  // s15 « En 2020, 14 ans après sa mort, son roman y entre enfin. »
  { a: ['s15', 0], type: 'classement', etape: 2, entre: ['s15', 'roman'], quatorze: ['s15', '14'], choc: true },
  // s16 « Il est au programme de l'ACL oral, en BFI. Pourquoi nous parle-t-il autant ? La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'programme' },
  { a: ['s16', 'pourquoi'], type: 'mot', t: 'POURQUOI IL NOUS|PARLE AUTANT ?' },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'Parable of the Sower', fond: 'ecriture' },
  // s17 « Et tout ça… une femme l'avait écrit. » (boucle vers « En 1993, une femme écrit un roman… »)
  { a: ['s17', 0], type: 'boucle' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE MONDE', 'LA CHUTE', 'LE RÉEL', 'LE DESTIN'];
window.IMAGES = {
  ecriture: '../../philo/serie/img/cs6-ecriture.jpg',   // Albert Anker, La Leçon d'écriture, XIXᵉ siècle (Anker † 1910), domaine public
};
