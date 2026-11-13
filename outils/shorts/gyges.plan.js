// Découpage du short « L'anneau de Gygès », modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Si personne ne pouvait jamais te voir… tu resterais honnête ? »
  { a: ['s1', 0], av: .25, type: 'oeil', etat: 'ferme', t: 'SI PERSONNE|NE TE VOYAIT…', ch: 0 },
  { a: ['s1', 'tu'], type: 'mot', t: 'TU RESTERAIS|HONNÊTE ?' },
  // s2 « Il y a 2400 ans, Platon raconte cette histoire. »
  { a: ['s2', 0], type: 'mot', t: 'IL Y A|2400 ANS' },
  { a: ['s2', 'platon'], type: 'tableau', img: 'platon', z: 1.05, fx: .5, fy: .3, w: 600, h: 800, t: 'PLATON', sous: 'La République, livre II', leg: 'Raphaël, L’École d’Athènes (détail)' },
  // s3 « Tu es berger, en Lydie. Tu gardes les moutons du roi. »
  { a: ['s3', 0], type: 'berger', t: 'TOI.|BERGER, EN LYDIE', ch: 1 },
  { a: ['s3', 'gardes'], type: 'tableau', img: 'lydie', z: 1.05, fx: .24, fy: .5, w: 780, h: 760, t: 'AU SERVICE|DU ROI', leg: 'pièce de Lydie, VIᵉ s. av. J.-C.' },
  // s4 « Un orage éclate. La terre tremble. Le sol s'ouvre devant toi. »
  { a: ['s4', 0], type: 'orage', t: 'UN ORAGE|ÉCLATE' },
  { a: ['s4', 'terre'], type: 'orage', tremble: true, choc: true, t: 'LA TERRE|TREMBLE' },
  { a: ['s4', 'sol'], type: 'faille', t: 'LE SOL|S’OUVRE' },
  // s5 « Tu descends. Au fond, un cheval de bronze, creux, avec des portes. »
  { a: ['s5', 0], type: 'faille', descente: true, t: 'TU|DESCENDS' },
  { a: ['s5', 'au'], type: 'cheval', portes: ['s5', 'portes'], t: 'UN CHEVAL|DE BRONZE' },
  // s6 « Tu regardes à l'intérieur. Un mort. Plus grand qu'un homme. »
  { a: ['s6', 0], type: 'cheval', ouvre: true, t: 'À L’INTÉRIEUR…' },
  { a: ['s6', 'mort'], type: 'geant', grand: ['s6', 'plus'], t: 'UN MORT' },
  // s7 « Il ne porte qu'une chose : un anneau d'or. Tu le prends. »
  { a: ['s7', 0], type: 'anneau', t: 'UN ANNEAU|D’OR' },
  { a: ['s7', 'tu'], type: 'anneau', prend: true, t: 'TU LE|PRENDS' },
  // s8 « Plus tard, assis parmi les bergers, tu tournes le chaton de l'anneau vers ta paume. »
  { a: ['s8', 0], type: 'bergers', t: 'PARMI|LES BERGERS', ch: 2 },
  { a: ['s8', 'tournes'], type: 'chaton', sens: 1, t: 'LE CHATON|VERS TA PAUME' },
  // s9 « Et les autres parlent de toi… comme si tu étais parti. »
  { a: ['s9', 0], type: 'bergers', parle: true, t: 'ILS PARLENT|DE TOI…' },
  { a: ['s9', 'comme'], type: 'bergers', parle: true, invisible: true, t: 'COMME SI|TU ÉTAIS PARTI' },
  // s10 « Invisible. Tu le retournes : tu réapparais. Ça marche à chaque fois. »
  { a: ['s10', 0], type: 'tampon', t: 'INVISIBLE', choc: true },
  { a: ['s10', 'retournes'], type: 'essais', compte: ['s10', 'ça'], t: 'TU|RÉAPPARAIS', tbis: 'ÇA MARCHE|À CHAQUE FOIS' },
  // s11 « Alors tu files au palais. Tu séduis la reine. Avec elle, tu tues le roi. Tu prends le pouvoir. »
  { a: ['s11', 0], type: 'palais', t: 'TU FILES|AU PALAIS', ch: 3 },
  { a: ['s11', 'séduis'], type: 'cour', etape: 'reine', t: 'TU SÉDUIS|LA REINE' },
  { a: ['s11', 'avec'], type: 'cour', etape: 'roi', choc: true, t: 'TU TUES|LE ROI' },
  { a: ['s11', 'prends'], type: 'cour', etape: 'trone', t: 'TU PRENDS|LE POUVOIR' },
  // s12 « C'est l'anneau de Gygès. »
  { a: ['s12', 0], type: 'tableau', img: 'gyges', z: 2.2, fx: .12, fy: .82, w: 860, h: 900, t: 'L’ANNEAU|DE GYGÈS', leg: 'L’Anneau de Gygès, Ferrare, XVIᵉ s. (détail)' },
  // s13 « Glaucon, le frère de Platon, conclut : donne cet anneau au plus juste des hommes… il fera pareil. »
  { a: ['s13', 0], type: 'perso', t: 'GLAUCON', sous: 'le frère de Platon', ch: 4 },
  { a: ['s13', 'donne'], type: 'justes', t: 'AU PLUS JUSTE|DES HOMMES' },
  { a: ['s13', 'il'], type: 'justes', pareil: true, t: 'IL FERA|PAREIL' },
  // s14 « Personne n'est juste volontairement. On est juste par peur d'être pris. »
  { a: ['s14', 0], type: 'mot', t: 'PERSONNE N’EST JUSTE|VOLONTAIREMENT', choc: true },
  { a: ['s14', 'on'], type: 'oeil', etat: 'peur', t: 'PAR PEUR|D’ÊTRE PRIS' },
  // s15 « Platon passera toute la République à lui répondre. »
  { a: ['s15', 0], type: 'rouleau', t: 'TOUTE|LA RÉPUBLIQUE', sous: 'pour lui répondre' },
  // s16 « Ne fait-on son devoir que par peur d'être puni ? C'est un sujet type bac. La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'mot', t: 'TON DEVOIR…|PAR PEUR ?' },
  { a: ['s16', "c'est"], type: 'bac', sujet: ['Ne fait-on son devoir', 'que par peur d’être puni ?'] },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'Le devoir', fond: 'gyges' },
  // s17 « Alors toi… avec l'anneau au doigt, tu resterais honnête ? » (boucle vers « Si personne ne pouvait jamais te voir… »)
  { a: ['s17', 0], type: 'anneau', doigt: true, t: 'ALORS TOI…|TU RESTERAIS HONNÊTE ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA FAILLE', "L'ANNEAU", 'LE POUVOIR', 'LA QUESTION'];
window.IMAGES = {
  gyges: '../../philo/serie/img/dv2-gyges.jpg',     // Anonyme, L'Anneau de Gygès, Ferrare, XVIᵉ siècle, domaine public
  platon: '../../philo/serie/img/platon.jpg',       // Platon, Raphaël, L'École d'Athènes (détail), domaine public
  lydie: '../../philo/serie/img/dv1-lydie.jpg',     // pièce d'électrum de Lydie, VIᵉ s. av. J.-C., photo CNG coins, CC BY-SA 3.0
};
window.MUSIQUE = 'grec';   // musique imposée pour ce short
