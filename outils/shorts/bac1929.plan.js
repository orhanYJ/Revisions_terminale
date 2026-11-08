// Découpage du short « Pourquoi le krach de 1929 devient-il une crise mondiale ? » (format 2, question de bac), modèle A.
// a: [passage, mot] ; av : avance sur le mot. La copie s'écrit au fil de la voix : premier plan « copie », puis « copie2 ».
window.PLAN = S => {
const COPIE = {
  matiere: 'HISTOIRE', sujet: 'Pourquoi le krach de 1929|devient-il une crise mondiale ?',
  lignes: [
    [['s4', 0], 'Problématique :', 'titre'],
    [['s4', 'par'], 'par quels canaux gagne-t-elle le monde ?', ''],
    [['s6', 'le'], 'I. Le rappel des prêts américains', 'partie'],
    [['s7', 'en'], 'plan Dawes (1924) → Creditanstalt (mai 1931)', 'ex'],
    [['s8', 0], 'II. L’étalon-or transmet la crise', 'partie'],
    [['s9', 'le'], 'le Royaume-Uni en sort (sept. 1931)', 'ex'],
    [['s10', 'le'], 'III. Le protectionnisme', 'partie'],
    [['s11', 'entre'], 'Smoot-Hawley (1930) → commerce : −2/3', 'ex'],
    [['s13', 'crise'], 'Conclusion : des économies liées', 'titre'],
  ],
  souligne: [['s13', 'répond'], 1],
};
return S.plans([
  // s1 « Pourquoi le krach de 1929 devient-il une crise mondiale ? Ce genre de sujet tombe au bac. Tu as 60 secondes. »
  { a: ['s1', 0], av: .25, type: 'krach', t: 'POURQUOI LE KRACH|DE 1929…', ch: 0 },
  { a: ['s1', 'devient-il'], type: 'monde', t: 'DEVIENT-IL|MONDIAL ?' },
  { a: ['s1', 'ce'], type: 'copie', ...COPIE },
  { a: ['s1', 'tu'], type: 'chrono', t: 'TU AS|60 SECONDES' },
  // s2 « Le piège ? Raconter le krach. »
  { a: ['s2', 0], type: 'mot', t: 'LE PIÈGE', sombre: true, ch: 1 },
  { a: ['s2', 'raconter'], type: 'portrait', img: 'wallstreet', t: 'RACONTER', sous: 'le krach…' },
  // s3 « On ne te demande pas de raconter, mais d'expliquer. »
  { a: ['s3', 0], type: 'mot', t: 'RACONTER', t2: 'EXPLIQUER', a2: ['s3', "d'expliquer"] },
  // s4 « Problématique : par quels canaux une crise américaine gagne-t-elle le monde ? »
  { a: ['s4', 0], type: 'copie2', ...COPIE },
  // s5 « Réponse : trois canaux. Un argument, un exemple daté. »
  { a: ['s5', 0], type: 'canaux', ch: 2 },
  { a: ['s5', 'un'], type: 'mot', t: 'UN ARGUMENT|UN EXEMPLE DATÉ' },
  // s6 « Un : le rappel des prêts américains. En 1924, avec le plan Dawes, l'Amérique prête 800 millions de marks à l'Allemagne. »
  { a: ['s6', 0], type: 'copie2', ...COPIE },
  { a: ['s6', 'en'], type: 'date', t: '1924', de: 1900, sous: 'PLAN DAWES' },
  { a: ['s6', "l'Amérique"], type: 'circuit', etape: 1 },
  // s7 « Après le krach, les prêts sont rappelés. En mai 1931, la Creditanstalt, la plus grande banque d'Autriche, fait faillite. »
  { a: ['s7', 0], type: 'circuit', etape: 2 },
  { a: ['s7', 'en'], type: 'copie2', ...COPIE },
  { a: ['s7', 'Creditanstalt'], type: 'banque' },
  { a: ['s7', 'faillite'], type: 'banque', faillite: true, choc: true },
  // s8 « Deux : l'étalon-or. Pour défendre le dollar, la Réserve fédérale relève ses taux. L'or quitte les autres pays. »
  { a: ['s8', 0], type: 'copie2', ...COPIE, ch: 3 },
  { a: ['s8', 'défendre'], type: 'taux', monte: ['s8', 'relève'] },
  { a: ['s8', "l'or"], type: 'lingots' },
  // s9 « En septembre 1931, le Royaume-Uni sort de l'étalon-or. »
  { a: ['s9', 0], type: 'date', t: '1931', de: 1924, sous: 'SEPTEMBRE · ROYAUME-UNI' },
  // s10 « Trois : le protectionnisme. Le 17 juin 1930, Hoover signe le tarif Smoot-Hawley. Le Canada riposte. »
  { a: ['s9', 'le'], type: 'copie2', ...COPIE },
  { a: ['s10', '17'], av: .35, type: 'tarif', etape: 1 },
  { a: ['s10', 'Canada'], av: .3, type: 'tarif', etape: 2 },
  // s11 « Résultat : entre 1929 et 1934, le commerce mondial perd environ deux tiers de sa valeur. »
  { a: ['s11', 'entre'], type: 'copie2', ...COPIE },
  { a: ['s11', 'perd'], type: 'commerce', choc: true },
  // s12 « L'erreur à éviter : une liste sans exemples. Chaque argument veut une date, un chiffre, un nom. »
  { a: ['s12', 0], type: 'mot', t: 'L’ERREUR|À ÉVITER', sombre: true, ch: 4 },
  { a: ['s12', 'une'], type: 'nue', x: ['s12', 'sans'] },
  { a: ['s12', 'chaque'], type: 'preuves', r: [['s12', 'date'], ['s12', 'chiffre'], ['s12', 'nom']] },
  // s13 « Ta conclusion répond : la crise devient mondiale parce que les économies sont liées. Par le crédit, l'or et le commerce. »
  { a: ['s13', 0], type: 'copie2', ...COPIE },
  { a: ['s13', 'liées'], type: 'canaux', t: 'DES ÉCONOMIES|LIÉES', r: [['s13', 'crédit'], ['s13', "l'or"], ['s13', 'commerce']] },
  // s14 « Le cours complet est sur Révisions Animées. »
  { a: ['s14', 0], type: 'chaine', serie: 'La crise de 1929', fond: 'wallstreet' },
  // s15 « Alors, pourquoi le krach devient-il mondial ? Maintenant, tu sais. » (boucle vers le début)
  { a: ['s15', 0], type: 'monde', t: 'POURQUOI LE KRACH|DEVIENT-IL MONDIAL ?' },
  { a: ['s15', 'maintenant'], type: 'mot', t: 'MAINTENANT,|TU SAIS.' },
]);
};
window.CHAPITRES = ['LE SUJET', 'LE PIÈGE', 'LE CRÉDIT', 'L’OR ET LA DOUANE', 'LA MÉTHODE'];
window.MUSIQUE = 'lofi2';
window.IMAGES = {
  wallstreet: '../../dnl/serie/img/h1-wallstreet.jpg',   // foule devant la Bourse de New York, octobre 1929, domaine public
};
