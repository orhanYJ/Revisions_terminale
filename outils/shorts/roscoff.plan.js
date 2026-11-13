// Découpage du short Roscoff (« Il a arrêté de manger »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Cet animal a arrêté de manger. Et il ne meurt pas de faim. »
  { a: ['s1', 0], av: .25, type: 'ver', mode: 'vert', t: 'IL A ARRÊTÉ|DE MANGER', ch: 0 },
  { a: ['s1', 'et'], type: 'mot', t: 'ET IL NE MEURT PAS|DE FAIM', choc: true },
  // s2 « Son secret ? Il vit du soleil. Comme une plante. »
  { a: ['s2', 0], type: 'mot', t: 'SON SECRET ?', sombre: true },
  { a: ['s2', 'il'], type: 'soleil', t: 'IL VIT|DU SOLEIL' },
  { a: ['s2', 'comme'], type: 'mot', t: 'COMME UNE|PLANTE' },
  // s3 « Tu es le ver de Roscoff : un ver plat marin de quelques millimètres, en Bretagne. »
  { a: ['s3', 0], type: 'vrai', img: 'roscoff', t: 'LE VER DE ROSCOFF', sous: 'Symsagittifera roscoffensis', ch: 1 },
  { a: ['s3', 'un'], type: 'ver', mode: 'vert', regle: true, t: 'UN VER PLAT MARIN|EN BRETAGNE' },
  // s4 « Tu viens d'éclore, translucide. Ta mission : avaler des micro-algues vertes. Une seule fois. »
  { a: ['s4', 0], type: 'ver', mode: 'oeuf', t: 'TU VIENS|D’ÉCLORE' },
  { a: ['s4', 'ta'], type: 'avale', t: 'TA MISSION :|AVALER DES ALGUES' },
  { a: ['s4', 'une'], type: 'mot', t: 'UNE SEULE|FOIS' },
  // s5 « Si tu n'en trouves pas ? Tu ne survis pas plus de 20 jours. »
  { a: ['s5', 0], type: 'ver', mode: 'jeune', t: 'SI TU N’EN|TROUVES PAS ?' },
  { a: ['s5', 'survis'], type: 'compte', choc: true },
  // s6 « Tu les trouves. Elles s'installent sous ta peau, et se multiplient. »
  { a: ['s6', 0], type: 'ver', mode: 'algues', mult: ['s6', 'multiplient'], t: 'ELLES S’INSTALLENT|SOUS TA PEAU', ch: 2 },
  // s7 « Bientôt, environ 40 000 algues. Tu deviens vert. »
  { a: ['s7', 0], type: 'compteur' },
  { a: ['s7', 'tu'], type: 'ver', mode: 'vert', t: 'TU DEVIENS|VERT' },
  // s8 « Et là, tu arrêtes de manger. »
  { a: ['s8', 0], type: 'mot', t: 'TU ARRÊTES|DE MANGER', choc: true },
  // s9 « Les algues font la photosynthèse, et partagent avec toi ce qu'elles fabriquent. »
  { a: ['s9', 0], type: 'photo', t: 'LES ALGUES FONT|LA PHOTOSYNTHÈSE' },
  { a: ['s9', 'partagent'], type: 'photo', partage: ['s9', 'partagent'], t: 'ELLES PARTAGENT|AVEC TOI' },
  // s10 « À marée basse, tu remontes à la surface, au soleil. Avec des millions d'autres. »
  { a: ['s10', 0], type: 'plage', maree: 'basse', t: 'À MARÉE BASSE…', ch: 3 },
  { a: ['s10', 'tu'], type: 'plage', maree: 'basse', monte: true, t: 'TU REMONTES|AU SOLEIL' },
  { a: ['s10', 'avec'], type: 'plage', maree: 'basse', foule: true, t: 'AVEC DES MILLIONS|D’AUTRES' },
  // s11 « La plage se couvre de taches vertes. À marée haute, tu t'enfonces dans le sable. »
  { a: ['s11', 0], type: 'vrai', img: 'roscoff', t: 'DES TACHES VERTES', sous: 'sur le sable, à marée basse' },
  { a: ['s11', 'haute'], av: .4, type: 'plage', maree: 'haute', t: 'MARÉE HAUTE :|TU T’ENFONCES' },
  // s12 « Toi, tu gagnes la photosynthèse. Les algues, un abri stable. »
  { a: ['s12', 0], type: 'echange', toi: ['s12', 'photosynthèse'], alg: ['s12', 'abri'], ch: 4 },
  // s13 « Chacun y gagne : c'est le mutualisme. Vous êtes interdépendants : une symbiose. »
  { a: ['s13', 0], type: 'mot', t: 'CHACUN Y GAGNE :|LE MUTUALISME' },
  { a: ['s13', 'vous'], type: 'echange', lien: true, t: 'INTERDÉPENDANTS :|UNE SYMBIOSE' },
  // s14 « Le plus fou ? Ton génome n'a pas changé. Tout vient de l'association. »
  { a: ['s14', 0], type: 'mot', t: 'LE PLUS FOU ?' },
  { a: ['s14', 'ton'], type: 'genome', t: 'TON GÉNOME|N’A PAS CHANGÉ' },
  { a: ['s14', 'tout'], type: 'genome', asso: true },
  // s15 « Montrez que des relations entre espèces peuvent diversifier le vivant sans modifier le génome : sujet type bac.
  //       La réponse est sur Révisions Animées. »
  { a: ['s15', 0], type: 'bacsvt', sujet: ['Montrez que des relations', 'entre espèces peuvent', 'diversifier le vivant', 'sans modifier le génome.'] },
  { a: ['s15', 'sujet'], type: 'tampon', t: 'TYPE BAC' },
  { a: ['s15', 'réponse'], type: 'chaine', serie: 'SVT · chapitre 4', fond: 'roscoff' },
  // s16 « La prochaine fois que tu as faim… pense à lui. Il a arrêté de manger. » (boucle vers le début)
  { a: ['s16', 0], type: 'mot', t: 'LA PROCHAINE FOIS|QUE TU AS FAIM…' },
  { a: ['s16', 'il'], type: 'ver', mode: 'vert', t: 'IL A ARRÊTÉ|DE MANGER' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA NAISSANCE', 'LES ALGUES', 'LA PLAGE', 'LE MUTUALISME'];
window.IMAGES = {
  roscoff: '../../svt/serie/img/ch4-roscoff.jpg',   // vers de Roscoff (Symsagittifera roscoffensis), photo Lou Wagstaffe, iNaturalist, CC BY (attribution obligatoire)
};

window.MUSIQUE = 'docu';   // musique imposée pour ce short
