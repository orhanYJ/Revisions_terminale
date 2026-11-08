// Découpage du short Pearl Harbor (« Personne ne te croit »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Tu vois la guerre arriver sur ton écran… et personne ne te croit ? »
  { a: ['s1', 0], av: .25, type: 'ascope', etat: 'echo', pic: ['s1', 'arriver'], t: 'TU VOIS LA GUERRE|ARRIVER', ch: 0 },
  { a: ['s1', 'personne'], type: 'mot', t: 'ET PERSONNE|NE TE CROIT ?', sombre: true },
  // s2 « 7 décembre 1941. Hawaï. Un dimanche matin. »
  { a: ['s2', 0], type: 'date', t: '1941', de: 1900, sous: '7 DÉCEMBRE', ch: 1 },
  { a: ['s2', 'hawaï'], type: 'ile', t: 'HAWAÏ', sous: 'un dimanche matin' },
  // s3 « Tu es simple soldat. Devant toi, un radar, sur une colline. »
  { a: ['s3', 0], type: 'mot', t: 'TOI.', sous: 'simple soldat' },
  { a: ['s3', 'devant'], type: 'colline' },
  // s4 « 7h. Ton service est fini. Mais tu laisses l'écran allumé. »
  { a: ['s4', 0], type: 'heure', h: 7, m: 0, t: 'SERVICE FINI' },
  { a: ['s4', 'mais'], type: 'ascope', etat: 'veille', t: 'TU LAISSES|L’ÉCRAN ALLUMÉ' },
  // s5 « 7h02. Un écho apparaît. Au nord, à plus de 200 kilomètres. »
  { a: ['s5', 0], type: 'heure', h: 7, m: 2 },
  { a: ['s5', 'écho'], type: 'ascope', etat: 'echo', pic: ['s5', 'apparaît'], t: 'UN ÉCHO' },
  { a: ['s5', 'au'], type: 'ile', fleche: true, km: ['s5', '200'], t: 'AU NORD' },
  // s6 « Énorme. Le plus gros que tu aies jamais vu. »
  { a: ['s6', 0], type: 'ascope', etat: 'gros', t: 'ÉNORME' },
  { a: ['s6', 'gros'], type: 'mot', t: 'LE PLUS GROS|JAMAIS VU' },
  // s7 « Des avions. Beaucoup d'avions. Et ils foncent droit sur l'île. »
  { a: ['s7', 0], type: 'vol', n: ['s7', 'beaucoup'] },
  { a: ['s7', 'et'], type: 'ile', fleche: true, approche: true, t: 'DROIT|SUR L’ÎLE' },
  // s8 « Vous appelez. Au bout du fil, un lieutenant. C'est son deuxième jour. »
  { a: ['s8', 0], type: 'telephone', t: 'VOUS|APPELEZ', ch: 2 },
  { a: ['s8', 'au'], type: 'perso', t: 'UN LIEUTENANT', sous: 'son deuxième jour de formation' },
  // s9 « Sa réponse tient en une phrase : ne vous en faites pas. »
  { a: ['s9', 0], type: 'telephone', bulle: true, t: 'SA RÉPONSE' },
  { a: ['s9', 'ne'], type: 'reponse', t: 'Ne vous en faites pas.', duree: .8 },
  // s10 « Pour lui, ce sont des bombardiers américains, attendus ce matin-là. »
  { a: ['s10', 0], type: 'b17' },
  { a: ['s10', 'attendus'], type: 'mot', t: 'ATTENDUS|CE MATIN-LÀ' },
  // s11 « Vous le suivez encore. Vers 7h40, il disparaît. »
  { a: ['s11', 0], type: 'ascope', etat: 'suit', t: 'VOUS LE|SUIVEZ' },
  { a: ['s11', 'vers'], type: 'heure', h: 7, m: 40 },
  { a: ['s11', 'disparaît'], av: .1, type: 'ascope', etat: 'perdu', silence: true, muet: true, t: '… IL DISPARAÎT' },
  // s12 « 7h55. Des avions plongent sur Pearl Harbor. Ils sont japonais. »
  { a: ['s12', 0], type: 'heure', h: 7, m: 55, ch: 3 },
  { a: ['s12', 'avions'], type: 'attaque' },
  { a: ['s12', 'ils'], type: 'japonais', choc: true },
  // s13 « À la radio : raid aérien sur Pearl Harbor. Ceci n'est pas un exercice. »
  { a: ['s13', 0], type: 'radio', fr1: ['s13', 'raid'], l2: ['s13', 'ceci'], choc: true },
  // s14 « Plus de 2400 morts américains. Et toi, tu les avais vus venir. »
  { a: ['s14', 0], type: 'bilan', n: ['s14', '2400'] },
  { a: ['s14', 'et'], type: 'ascope', etat: 'fin', t: 'TU LES AVAIS|VUS VENIR' },
  // s15 « Le lendemain, les États-Unis déclarent la guerre au Japon. Le 11 décembre, l'Allemagne et l'Italie la leur déclarent. »
  { a: ['s15', 0], type: 'declare', etape: 1, ch: 4 },
  { a: ['s15', '11'], type: 'declare', etape: 2 },
  // s16 « La guerre devient mondiale. »
  { a: ['s16', 0], type: 'globe', choc: true },
  // s17 « Pourquoi en 1941 ? C'est un sujet type bac d'histoire. La réponse est sur Révisions Animées. »
  { a: ['s17', 0], type: 'mot', t: 'POURQUOI|EN 1941 ?' },
  { a: ['s17', 'sujet'], type: 'bach', sujet: ['Pourquoi la guerre devient-elle', 'mondiale en 1941 ?'] },
  { a: ['s17', 'réponse'], type: 'chaine', serie: 'La Seconde Guerre mondiale', fond: 'churchill' },
  // s18 « Et toi… ce point sur l'écran, tu y aurais cru ? » (boucle vers « Tu vois la guerre arriver sur ton écran… »)
  { a: ['s18', 0], type: 'ascope', etat: 'fin', t: 'ET TOI…|TU Y AURAIS CRU ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE RADAR', "L'APPEL", "L'ATTAQUE", 'LA GUERRE MONDIALE'];
window.IMAGES = {
  churchill: '../../dnl/serie/img/h3-churchill.jpg',   // Winston Churchill, Ottawa, décembre 1941, photo Yousuf Karsh (Library and Archives Canada), CC BY 2.0
  reichstag: '../../dnl/serie/img/h3-reichstag.jpg',   // Hitler déclare la guerre aux États-Unis, Reichstag, 11 décembre 1941 (Wikimedia Commons), CC BY-SA 3.0
};
window.MUSIQUE = 'suspense';   // musique imposée pour ce short
