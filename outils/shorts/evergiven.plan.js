// Découpage du short Ever Given (« Un seul bateau »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Tu peux bloquer le commerce mondial… avec un seul bateau ? »
  { a: ['s1', 0], av: .25, type: 'mot', t: 'BLOQUER LE|COMMERCE MONDIAL ?', ch: 0 },
  { a: ['s1', 'avec'], type: 'canal', etat: 'travers', t: 'AVEC UN SEUL|BATEAU ?' },
  // s2 « 23 mars 2021. Canal de Suez. »
  { a: ['s2', 0], type: 'date', t: '2021', de: 1980, sous: '23 MARS · ÉGYPTE', ch: 1 },
  { a: ['s2', 'canal'], type: 'canal', etat: 'route', t: 'CANAL|DE SUEZ' },
  // s3 « Tu es à bord de l'Ever Given. Un des plus grands porte-conteneurs du monde. »
  { a: ['s3', 0], type: 'navire', t: 'À BORD DE|L’EVER GIVEN' },
  { a: ['s3', 'un'], type: 'navire', zoom: true, t: 'UN DES PLUS GRANDS|PORTE-CONTENEURS' },
  // s4 « 400 mètres. Plus long que la tour Eiffel n'est haute. »
  { a: ['s4', 0], type: 'navire', eiffel: true },
  // s5 « Tempête de sable. Le vent pousse tes conteneurs comme une voile. »
  { a: ['s5', 0], type: 'tempete', t: 'TEMPÊTE|DE SABLE' },
  { a: ['s5', 'vent'], type: 'tempete', voile: true, t: 'COMME|UNE VOILE' },
  // s6 « Le navire dérape. L'avant se plante dans une rive. L'arrière dans l'autre. »
  { a: ['s6', 0], type: 'canal', etat: 'derape', sable: true, t: 'IL|DÉRAPE', ch: 2 },
  { a: ['s6', "l'avant"], type: 'canal', etat: 'travers', avant: ['s6', 'plante'], arriere: ["s6", "l'arrière"], choc: true, t: 'PLANTÉ|DANS LES DEUX RIVES' },
  // s7 « Coincé en travers du canal. Plus rien ne passe. »
  { a: ['s7', 0], type: 'mot', t: 'COINCÉ|EN TRAVERS' },
  { a: ['s7', 'plus'], type: 'canal', etat: 'travers', bloque: ['s7', 'passe'], choc: true, t: 'PLUS RIEN|NE PASSE' },
  // s8 « Derrière toi, les navires s'arrêtent. 10. 100. Plus de 400. »
  { a: ['s8', 0], type: 'canal', etat: 'file', etapes: [[null, 0], [['s8', "s'arrêtent"], 3], [['s8', '10'], 10], [['s8', '100'], 100], [['s8', '400'], 400]] },
  // s9 « Par ce canal passe 12 pour cent du commerce mondial. Entre l'Asie et l'Europe. »
  { a: ['s9', 0], type: 'route', etape: 1 },
  { a: ['s9', 'entre'], type: 'route', etape: 2 },
  // s10 « Près de 10 milliards de dollars de marchandises bloquées. Chaque jour. »
  { a: ['s10', 0], type: 'argent' },
  { a: ['s10', 'chaque'], type: 'mot', t: 'CHAQUE|JOUR.', choc: true },
  // s11 « Sur la berge, pour te dégager… une petite pelleteuse. »
  { a: ['s11', 0], type: 'canal', etat: 'travers', t: 'POUR TE|DÉGAGER…', ch: 3 },
  { a: ['s11', 'une'], type: 'pelleteuse', t: 'UNE PETITE|PELLETEUSE' },
  // s12 « La photo fait le tour du monde. Un mème. »
  { a: ['s12', 0], type: 'pelleteuse', meme: true, tampon: ['s12', 'mème'], t: 'LE TOUR|DU MONDE' },
  // s13 « Il faut des remorqueurs, des dragues… 30 000 mètres cubes de sable. »
  { a: ['s13', 0], type: 'chantier', t: 'REMORQUEURS|ET DRAGUES' },
  { a: ['s13', '30'], type: 'chantier', m3: ['s13', '30'] },
  // s14 « Et une alliée : la Lune. Pleine lune, grande marée. »
  { a: ['s14', 0], type: 'mot', t: 'UNE ALLIÉE…', sombre: true },
  { a: ['s14', 'lune'], type: 'lune', t: 'LA LUNE', sous: 'pleine lune du 28 mars 2021' },
  { a: ['s14', 'grande'], type: 'maree', t: 'GRANDE|MARÉE' },
  // s15 « 29 mars. L'eau monte. Après 6 jours, tu flottes enfin. »
  { a: ['s15', 0], type: 'maree', monte: ["s15", "l'eau"], leve: true, t: '29 MARS|L’EAU MONTE' },
  { a: ['s15', 'après'], type: 'canal', etat: 'libre', t: 'APRÈS 6 JOURS|TU FLOTTES' },
  // s16 « Détroits et canaux : des passages étroits dont dépend le commerce mondial. En géographie, ce sont des choke points. »
  { a: ['s16', 0], type: 'choke', t: 'DES PASSAGES|ÉTROITS', ch: 4 },
  { a: ['s16', 'dont'], type: 'route', etape: 1 },
  { a: ['s16', 'en'], type: 'choke', tampon: ['s16', 'choke'], sous: 'SUEZ · MALACCA · ORMUZ' },
  // s17 « Pourquoi sont-ils stratégiques ? C'est une question type bac. La réponse est sur Révisions Animées. »
  { a: ['s17', 0], type: 'mot', t: 'POURQUOI|STRATÉGIQUES ?' },
  { a: ['s17', 'question'], type: 'bac', matiere: 'GÉOGRAPHIE', sujet: ['Pourquoi détroits et canaux', 'sont-ils stratégiques ?'] },
  { a: ['s17', 'réponse'], type: 'chaine', serie: 'Géographie · Espaces maritimes', fond: 'mer' },
  // s18 « Et toi… tu aurais cru qu'un seul bateau pouvait bloquer le monde ? » (boucle vers « Tu peux bloquer le commerce mondial… »)
  { a: ['s18', 0], type: 'mot', t: 'ET TOI…', sous: 'tu y aurais cru ?' },
  { a: ['s18', "qu'un"], type: 'canal', etat: 'travers', t: 'UN SEUL BATEAU|BLOQUE LE MONDE ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE NAVIRE', 'LE BLOCAGE', 'LE SAUVETAGE', 'LES CHOKE POINTS'];
window.IMAGES = {
  lune: '../../pc/serie/img/c5-lune.jpg',   // la pleine Lune vue depuis l'espace, NASA, domaine public
  mer: '../../philo/serie/img/bh2-mer.jpg',  // Henry Dawson, Navires sur une mer calme au crépuscule, XIXe siècle, domaine public
};
window.MUSIQUE = 'ambient_mer';   // musique imposée pour ce short
