// Découpage du short « cerveau » (« Ta main gauche choisit une pelle »), modèle A. a: [passage, mot] ; av : avance sur le mot.
// Code couleur : cerveau gauche (qui parle) = or ; cerveau droit (muet) = rouge.
window.PLAN = S => S.plans([
  // s1 « Ta main gauche choisit une pelle. Tu ne sais pas pourquoi. »
  { a: ['s1', 0], av: .2, type: 'mains', etape: 'prend', t: 'TA MAIN GAUCHE|CHOISIT UNE PELLE', ch: 0 },
  { a: ['s1', 'tu'], type: 'mot', t: 'TU NE SAIS PAS|POURQUOI', sombre: true },
  // s2 « Et pourtant… tu vas l'expliquer. »
  { a: ['s2', 0], type: 'mot', t: 'ET POURTANT…' },
  { a: ['s2', 'tu'], type: 'mot', t: 'TU VAS|L’EXPLIQUER', choc: true },
  // s3 « Années 1970. Tu es le patient P.S. Pour stopper ton épilepsie, on t'opère. »
  { a: ['s3', 0], type: 'date', t: '1970', de: 1900, ch: 1 },
  { a: ['s3', 'patient'], type: 'perso', t: 'PATIENT « P.S. »', sous: 'on ne connaît que ses initiales' },
  { a: ['s3', 'pour'], type: 'crise', t: 'ÉPILEPSIE|TRÈS GRAVE' },
  // s4 « On coupe ton corps calleux : le pont entre les deux moitiés du cerveau. »
  { a: ['s4', 0], type: 'dessus', coupe: ['s4', 'calleux'] },
  { a: ['s4', 'pont'], type: 'dessus', mode: 'pont', t: 'LE PONT ENTRE|LES DEUX MOITIÉS' },
  // s5 « 200 millions de fibres. Tes deux moitiés ne se parlent plus. »
  { a: ['s5', 0], type: 'fibres', choc: true },
  { a: ['s5', 'tes'], type: 'separe', t: 'ELLES NE SE|PARLENT PLUS' },
  // s6 « Au quotidien ? Presque rien ne change. »
  { a: ['s6', 0], type: 'mot', t: 'AU QUOTIDIEN ?' },
  { a: ['s6', 'presque'], type: 'mot', t: 'PRESQUE RIEN|NE CHANGE' },
  // s7 « Michael Gazzaniga, élève du futur Nobel Roger Sperry, te fait passer un test. »
  { a: ['s7', 0], type: 'nom', t: 'MICHAEL GAZZANIGA', sous: 'neuroscientifique', ch: 2 },
  { a: ['s7', 'roger'], type: 'nom', t: 'ROGER SPERRY', sous: 'son directeur de thèse · Nobel 1981' },
  { a: ['s7', 'passer'], type: 'ecran', t: 'LE TEST', puis: 'FIXE LE POINT', aPuis: ['s8', 'point'] },
  // s8 « Tu fixes un point sur un écran. Deux images, en un éclair. »
  { a: ['s8', 'deux'], type: 'ecran', flash: ['s8', 'deux'], t: 'DEUX IMAGES', puis: 'EN UN ÉCLAIR', aPuis: ['s8', 'éclair'] },
  // s9 « Le secret : l'image de gauche ne va que dans ton cerveau droit. »
  { a: ['s9', 0], type: 'croise', t: 'LE SECRET' },
  { a: ['s9', 'gauche'], av: .35, type: 'croise', t: 'L’IMAGE DE GAUCHE…', fl: ['s9', 'gauche'] },
  // s10 « Ton cerveau gauche voit une patte de poulet. Le droit, un paysage de neige. »
  { a: ['s10', 0], type: 'voit', mode: 'g', bg: ['s10', 'patte'], t: 'TON CERVEAU GAUCHE|VOIT UNE PATTE DE POULET' },
  { a: ['s10', 'le'], type: 'voit', mode: 'gd', bd: ['s10', 'paysage'], t: 'LE DROIT|UN PAYSAGE DE NEIGE' },
  // s11 « Devant toi, des images. Ta main droite montre le poulet. Ta main gauche… la pelle. »
  { a: ['s11', 0], type: 'cartes' },
  { a: ['s11', 'droite'], av: .45, type: 'cartes', main: 'd', t: 'LA MAIN DROITE|LE POULET' },
  { a: ['s11', 'gauche'], av: .45, type: 'cartes', main: 'g', t: 'LA MAIN GAUCHE|LA PELLE', choc: true },
  // s12 « Logique. Sauf que ton cerveau droit ne parle pas. »
  { a: ['s12', 'sauf'], type: 'muet', t: 'TON CERVEAU DROIT|NE PARLE PAS', ch: 3 },
  // s13 « On te demande pourquoi. Ton cerveau gauche répond. Lui n'a jamais vu la neige. »
  { a: ['s13', 0], type: 'mot', t: 'POURQUOI|LA PELLE ?' },
  { a: ['s13', 'ton'], type: 'voit', mode: 'parle', t: 'LE GAUCHE|RÉPOND' },
  { a: ['s13', 'lui'], type: 'mot', t: 'IL N’A JAMAIS|VU LA NEIGE', sombre: true },
  // s14 « Oh, c'est simple. La patte va avec le poulet, et il faut une pelle pour nettoyer le poulailler. »
  { a: ['s14', 0], type: 'reponse', t: 'Oh, c’est simple.', debut: true, duree: .6, taille: 110 },
  { a: ['s14', 'la'], type: 'reponse', t: 'La patte va|avec le poulet…', icones: ['patte', 'poulet'], duree: 1.2 },
  { a: ['s14', 'il'], av: .4, type: 'reponse', t: '… et il faut une pelle|pour nettoyer|le poulailler.', icones: ['pelle', 'poulailler'], duree: 2.4, fin: true },
  // s15 « Il invente. Aussitôt. Gazzaniga appelle ça : l'interprète. »
  { a: ['s15', 0], type: 'tampon', t: 'IL INVENTE', choc: true },
  { a: ['s15', 'gazzaniga'], type: 'interprete', titre: ['s15', 'linterprete'] },
  // s16 « Et si, toi aussi, tu expliquais tes choix après coup ? »
  { a: ['s16', 0], type: 'mot', t: 'ET SI|TOI AUSSI ?', ch: 4 },
  { a: ['s16', 'tu'], type: 'mot', t: 'TU EXPLIQUES TES CHOIX|APRÈS COUP ?', img: 'penseur' },
  // s17 « Suis-je ce que j'ai conscience d'être ? Question de bac. Descartes, Freud et Nietzsche y répondent sur Révisions Animées. »
  { a: ['s17', 0], type: 'bac', sujet: ['Suis-je ce que', 'j’ai conscience d’être ?'] },
  { a: ['s17', 'descartes'], type: 'trio', noms: [['s17', 'descartes'], ['s17', 'freud'], ['s17', 'nietzsche']] },
  { a: ['s17', 'sur'], type: 'chaine', serie: 'La conscience', fond: 'neurones' },
  // s18 « Alors… ta main gauche. Pourquoi la pelle ? » (boucle vers le début)
  { a: ['s18', 0], type: 'mains', etape: 'hesite', t: 'TA MAIN GAUCHE…|POURQUOI LA PELLE ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE PATIENT', 'LE TEST', "L'INTERPRÈTE", 'LA CONSCIENCE'];
window.IMAGES = {
  penseur: '../../philo/serie/img/t-penseur.jpg',        // Rodin, photo Jebulon, CC0
  neurones: '../../philo/serie/img/cs1-neurones.jpg',    // Ramón y Cajal, neurones du cervelet, vers 1894, domaine public
  descartes: '../../philo/serie/img/descartes.jpg',      // d'après Frans Hals, domaine public
  freud: '../../philo/serie/img/freud.jpg',              // Max Halberstadt, vers 1921, domaine public
  nietzsche: '../../philo/serie/img/nietzsche.jpg',      // Gustav Schultze, 1882, domaine public
};
