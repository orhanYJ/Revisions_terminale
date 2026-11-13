// Découpage du short « Ôte-toi de mon soleil » (Diogène et Alexandre), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Alexandre le Grand te propose ce que tu veux. Tu lui réponds : pousse-toi. »
  { a: ['s1', 0], av: .25, type: 'offre', t: 'ALEXANDRE LE GRAND|TE PROPOSE TOUT', ch: 0 },
  { a: ['s1', 9], type: 'tableau', img: 'diogene', z: 3.2, fx: .66, fy: .61, w: 760, h: 820, t: 'TU LUI|RÉPONDS…' },
  { a: ['s1', 'pousse'], type: 'mot', t: 'POUSSE-TOI.', choc: true },
  // s2 « Tu t'appelles Diogène. Tu es philosophe. Et tu n'as presque rien. »
  { a: ['s2', 0], type: 'tableau', img: 'diogene', z: 1.3, fx: .72, fy: .78, w: 760, h: 820, t: 'DIOGÈNE', sous: 'philosophe, né à Sinope', leg: 'J. W. Waterhouse, Diogène, 1882 (détail)', ch: 1 },
  { a: ['s2', 'et'], type: 'mot', t: 'PRESQUE|RIEN' },
  // s3 « Un manteau, un sac, un bâton. Tu dors dans une jarre, en pleine ville. »
  { a: ['s3', 0], type: 'inventaire', items: [[['s3', 0], 'manteau', 'UN MANTEAU'], [['s3', 'sac'], 'sac', 'UN SAC'], [['s3', 'bâton'], 'baton', 'UN BÂTON']] },
  { a: ['s3', 'tu'], type: 'jarre', t: 'TU DORS|DANS UNE JARRE' },
  // s4 « Tu manges sur la place publique. On te le reproche ? C'est là que tu as eu faim. »
  { a: ['s4', 0], type: 'agora', t: 'TU MANGES|EN PUBLIC' },
  { a: ['s4', 'on'], type: 'agora', doigts: true, t: 'ON TE LE|REPROCHE ?' },
  { a: ['s4', "c'est"], type: 'mot', t: '« C’EST LÀ QUE|J’AI EU FAIM »' },
  // s5 « Tu vois un enfant boire dans ses mains. Tu jettes ton gobelet : un enfant m'a battu. »
  { a: ['s5', 0], type: 'gobelet', etape: 1, t: 'UN ENFANT|BOIT DANS SES MAINS' },
  { a: ['s5', 'jettes'], type: 'gobelet', etape: 2, t: 'TU JETTES|TON GOBELET' },
  { a: ['s5', 12], type: 'mot', t: '« UN ENFANT|M’A BATTU »' },
  // s6 « En plein jour, tu allumes une lampe : je cherche un homme. »
  { a: ['s6', 0], type: 'lampe', t: 'EN PLEIN JOUR,|UNE LAMPE' },
  { a: ['s6', 'je'], type: 'lampe', cherche: true, t: '« JE CHERCHE|UN HOMME »' },
  // s7 « On te surnomme le chien. C'est de là que vient le mot cynique. »
  { a: ['s7', 0], type: 'chien', t: 'LE CHIEN' },
  { a: ['s7', "c'est"], type: 'etymo', cyn: ['s7', 'cynique'] },
  // s8 « On raconte qu'un jour, à Corinthe, tu es allongé au soleil. »
  { a: ['s8', 0], type: 'mot', t: 'ON RACONTE|QU’UN JOUR…', ch: 2 },
  { a: ['s8', 'corinthe'], type: 'soleil', t: 'À CORINTHE,|AU SOLEIL' },
  // s9 « Une ombre s'arrête devant toi : Alexandre, que les Grecs viennent de choisir pour chef. »
  { a: ['s9', 0], type: 'soleil', ombre: true, t: 'UNE OMBRE…' },
  { a: ['s9', 'alexandre'], type: 'tableau', img: 'alexandre', z: 2.0, fx: .25, fy: .42, w: 720, h: 820, t: 'ALEXANDRE', sous: 'roi de Macédoine', leg: 'Ch. Laplante, Aristote et le jeune Alexandre, 1866 (détail)' },
  { a: ['s9', 'grecs'], type: 'armee', t: 'CHEF|DES GRECS' },
  // s10 « Il te dit : demande-moi ce que tu veux. »
  { a: ['s10', 0], type: 'parole', qui: 'ALEXANDRE', t: 'Demande-moi|ce que tu veux.', duree: 1.3, fond: 'alexandre' },
  // s11 « De l'or ? Un palais ? »
  { a: ['s11', 0], type: 'tentations', palais: ['s11', 'un'] },
  // s12 « Tu te redresses un peu. Et tu dis : ôte-toi de mon soleil. »
  { a: ['s12', 0], type: 'soleil', ombre: true, redresse: true, t: 'TU TE|REDRESSES UN PEU', ch: 3 },
  { a: ['s12', 'ôte'], type: 'parole', qui: 'DIOGÈNE', t: 'Ôte-toi|de mon soleil.', duree: .9, fond: 'diogene', choc: true, tampon: true },
  // s13 « Ses compagnons rient. Mais Alexandre dit : si je n'étais pas Alexandre, je voudrais être Diogène. »
  { a: ['s13', 0], type: 'rires', t: 'SES COMPAGNONS|RIENT' },
  { a: ['s13', 'mais'], type: 'parole', qui: 'ALEXANDRE', t: 'Si je n’étais pas|Alexandre…', duree: 1.1, fond: 'alexandre' },
  { a: ['s13', 'voudrais'], type: 'mot', t: 'JE VOUDRAIS ÊTRE|DIOGÈNE', choc: true },
  // s14 « Diogène disait : n'avoir besoin de rien, c'est divin. De peu, c'est presque divin. »
  { a: ['s14', 0], type: 'besoin', rien: ['s14', 'rien'], ch: 4 },
  { a: ['s14', 8], type: 'besoin', peu: true },
  // s15 « Le bonheur dépend-il de nous ? C'est un sujet type bac. La réponse est sur Révisions Animées. »
  { a: ['s15', 0], type: 'mot', t: 'LE BONHEUR|DÉPEND-IL DE NOUS ?' },
  { a: ['s15', "c'est"], type: 'bac', sujet: ['Le bonheur', 'dépend-il de nous ?'] },
  { a: ['s15', 'réponse'], type: 'chaine', serie: 'Le bonheur', fond: 'diogene' },
  // s16 « Et toi… Alexandre te propose ce que tu veux. Tu lui demandes quoi ? » (boucle vers « Alexandre le Grand te propose… »)
  { a: ['s16', 0], type: 'offre', t: 'ET TOI…|TU LUI DEMANDES QUOI ?' },
]);
window.CHAPITRES = ['ACCROCHE', 'LE PHILOSOPHE', 'LA RENCONTRE', 'LA RÉPONSE', 'LE BONHEUR'];
window.IMAGES = {
  diogene: '../../philo/serie/img/dv3-diogene.jpg',      // John William Waterhouse, Diogène, 1882 (Art Gallery of New South Wales), domaine public
  alexandre: '../../philo/serie/img/bh2-alexandre.jpg',  // Charles Laplante, Aristote et le jeune Alexandre, gravure, 1866, domaine public
};
window.MUSIQUE = 'boom_bap';   // musique imposée pour ce short
