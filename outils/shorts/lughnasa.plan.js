// Découpage du short Lughnasa (« Deux sœurs disparaissent »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Un matin de 1936, deux sœurs quittent la maison. Sans prévenir personne. »
  { a: ['s1', 0], av: .25, type: 'maison', t: 'UN MATIN|DE 1936', ch: 0 },
  { a: ['s1', 'deux'], type: 'maison', partir: ['s1', 'deux'], t: 'DEUX SŒURS|S’EN VONT' },
  { a: ['s1', 'sans'], type: 'mot', t: 'SANS PRÉVENIR|PERSONNE' },
  // s2 « Sur la table, un mot : nous partons pour de bon. Ne nous cherchez pas. »
  { a: ['s2', 0], type: 'billet' },
  { a: ['s2', 'ne'], type: 'mot', t: 'NE NOUS|CHERCHEZ PAS', sombre: true },
  // s3 « Elles s'appellent Agnes et Rose. Elles tricotent des gants, en Irlande. »
  { a: ['s3', 0], type: 'soeurs', n1: ['s3', 'agnes'], n2: ['s3', 'rose'], ch: 1 },
  { a: ['s3', 'tricotent'], type: 'tricot', t: 'DES GANTS|TRICOTÉS MAIN' },
  // s4 « 25 ans plus tard, leur neveu Michael les retrouve. À Londres. »
  { a: ['s4', 0], type: 'compteur' },
  { a: ['s4', 'neveu'], type: 'mot', t: 'LEUR NEVEU|MICHAEL', sous: 'le narrateur de la pièce' },
  { a: ['s4', 'retrouve'], type: 'londres' },
  // s5 « Agnes est morte de froid, dehors. Rose s'éteint dans un hospice pour pauvres. »
  { a: ['s5', 0], type: 'froid', t: 'AGNES|MORTE DE FROID' },
  { a: ['s5', 'rose'], type: 'hospice', t: 'ROSE|À L’HOSPICE DES PAUVRES' },
  // s6 « Ça, c'est la pièce : Dancing at Lughnasa, de Brian Friel. Mais voilà… »
  { a: ['s6', 0], type: 'rideau', titre: ['s6', 'dancing'] },
  { a: ['s6', 'mais'], type: 'mot', t: 'MAIS VOILÀ…', sombre: true },
  // s7 « Agnes et Rose ont vraiment existé. »
  { a: ['s7', 0], type: 'vrai', choc: true, ch: 2 },
  // s8 « Ce sont les tantes de l'auteur. Les sœurs de sa mère, à Glenties. »
  { a: ['s8', 0], type: 'friel' },
  { a: ['s8', 'sœurs'], av: .3, type: 'arbre' },
  // s9 « Et elles sont vraiment parties pour Londres. En 1936. L'année même de la pièce. »
  { a: ['s9', 0], type: 'valises', t: 'VRAIMENT|PARTIES' },
  { a: ['s9', 'londres'], type: 'date', t: '1936', de: 1900, sous: 'DÉPART POUR LONDRES' },
  { a: ['s9', "l'année"], type: 'mot', t: 'L’ANNÉE MÊME|DE LA PIÈCE', choc: true },
  // s10 « Un soir, devant des sans-abri endormis, Friel confie : j'avais deux tantes qui, je crois, ont fini comme ça. »
  { a: ['s10', 0], type: 'nuit', t: 'UN SOIR|À LONDRES' },
  { a: ['s10', 'confie'], type: 'aveu', cercle: ['s10', 'crois'], duree: 2.4 },
  // s11 « Je crois. Un historien a fouillé les archives. »
  { a: ['s11', 0], type: 'mot', t: 'JE CROIS…', sombre: true },
  { a: ['s11', 'historien'], type: 'archives', t: 'UN HISTORIEN|FOUILLE LES ARCHIVES', ch: 3 },
  // s12 « À Londres, elles travaillent dans des cantines. Pendant plus de 10 ans, elles ont un appartement à elles. »
  { a: ['s12', 0], type: 'cantine', t: 'ELLES TRAVAILLENT|DANS DES CANTINES' },
  { a: ['s12', 'pendant'], type: 'fenetre', etat: 1, ans: true, t: 'UN APPARTEMENT|À ELLES' },
  // s13 « Aucune trace de la rue, ni de l'alcool : la pièce a noirci leur vie. »
  { a: ['s13', 0], type: 'mot', t: 'LA RUE ?|L’ALCOOL ?', t2: 'AUCUNE TRACE', a2: ['s13', "l'alcool"] },
  { a: ['s13', 'pièce'], av: .4, type: 'encre', choc: true, t: 'LA PIÈCE A|NOIRCI LEUR VIE' },
  // s14 « Mais en 1960, Agnes meurt après une opération. Rose reste seule. »
  { a: ['s14', 0], type: 'date', t: '1960', de: 1949, sous: 'LONDRES' },
  { a: ['s14', 'agnes'], type: 'fenetre', etat: 2, t: 'AGNES|MEURT', sous: 'après une opération' },
  { a: ['s14', 'rose'], type: 'fenetre', etat: 3, t: 'ROSE|RESTE SEULE' },
  // s15 « Elle meurt en 1962 dans un foyer pour femmes sans ressources. À Southwark. Comme dans la pièce. »
  { a: ['s15', 0], type: 'date', t: '1962', de: 1960, sous: 'ROSE' },
  { a: ['s15', 'dans'], type: 'foyer', t: 'UN FOYER POUR FEMMES|SANS RESSOURCES' },
  { a: ['s15', 'comme'], type: 'miroir', choc: true },
  // s16 « Alors, Michael se souvient… ou il invente ? La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'mot', t: 'MICHAEL|SE SOUVIENT…', ch: 4 },
  { a: ['s16', 'ou'], type: 'memory' },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'Dancing at Lughnasa', fond: 'glenties' },
  // s17 « Un matin de 1936, deux sœurs quittent la maison… » (boucle vers le début)
  { a: ['s17', 0], type: 'maison', partir: ['s17', 'deux'], t: 'UN MATIN|DE 1936…' },
]);
window.CHAPITRES = ['ACCROCHE', 'LA PIÈCE', 'LA VÉRITÉ', 'LES ARCHIVES', 'LA MÉMOIRE'];
window.IMAGES = {
  glenties: '../../acl-lughnasa/serie/img/dal-glenties.jpg',     // Glenties, comté de Donegal, photo Thpohl, domaine public
  donegal: '../../acl-lughnasa/serie/img/dal-donegal.jpg',       // Five Finger Strand, Donegal, photo dconvertini, CC BY-SA 4.0
  friel: '../../acl-lughnasa/serie/img/dal-friel-statue.jpg',    // Brian Friel et John B. Keane, sculpture, Dublin, photo Spleodrach, CC BY-SA 4.0
  nocturne: '../../philo/serie/img/cs1-nocturne.jpg',            // Whistler, Nocturne en bleu et or : le vieux pont de Battersea, vers 1872-1875 (Tate), domaine public
  corot: '../../philo/serie/img/cs4-souvenir.jpg',               // Corot, Souvenir de Mortefontaine, 1864 (Louvre), domaine public
};
