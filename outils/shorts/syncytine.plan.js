// Découpage du short Syncytine (« Sans un virus, tu ne serais pas né »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Sans un virus, tu ne serais pas né. »
  { a: ['s1', 0], av: .25, type: 'virus', t: 'SANS|UN VIRUS…', ch: 0 },
  { a: ['s1', 'tu'], type: 'mot', t: 'TU NE SERAIS|PAS NÉ', choc: true },
  // s2 « Pas malgré lui. Grâce à lui. »
  { a: ['s2', 0], type: 'mot', t: 'PAS MALGRÉ LUI…', sombre: true },
  { a: ['s2', 'grâce'], type: 'virus', t: 'GRÂCE|À LUI', taille: 130 },
  // s3 « Il y a des millions d'années, un virus infecte un singe. Ton ancêtre. »
  { a: ['s3', 0], type: 'mot', t: 'IL Y A DES|MILLIONS D’ANNÉES', ch: 1 },
  { a: ['s3', 'un'], type: 'infection', t: 'UN VIRUS|INFECTE UN SINGE' },
  { a: ['s3', 'ton'], type: 'perso', t: 'TON ANCÊTRE', sous: 'un singe, il y a des millions d’années' },
  // s4 « Un rétrovirus : il glisse ses gènes dans l'ADN de la cellule. »
  { a: ['s4', 0], type: 'portrait', img: 'vih', t: 'UN RÉTROVIRUS', sous: 'ici le VIH, un rétrovirus d’aujourd’hui' },
  { a: ['s4', 'glisse'], type: 'adn', insere: true, t: 'IL GLISSE SES GÈNES|DANS L’ADN' },
  // s5 « Mais cette fois, il touche une cellule qui va donner un ovule… ou un spermatozoïde. »
  { a: ['s5', 0], type: 'mot', t: 'MAIS CETTE FOIS…', petit: true },
  { a: ['s5', 'touche'], type: 'germinale', ovule: ['s5', 'ovule'], spz: ['s5', 'spermatozoïde'] },
  // s6 « Le gène du virus passe aux enfants. Génération après génération. »
  { a: ['s6', 0], type: 'generations', marques: [['s6', 'enfants'], ['s6', 'génération'], ['s6', 'après']] },
  // s7 « Ce gène fabrique une protéine qui fusionne les membranes. L'arme du virus pour entrer. »
  { a: ['s7', 0], type: 'proteine', t: 'IL FABRIQUE|UNE PROTÉINE', ch: 2 },
  { a: ['s7', 'fusionne'], type: 'fusion', mode: 'virus', t: 'ELLE FUSIONNE|LES MEMBRANES' },
  { a: ['s7', "l'arme"], type: 'virus', t: 'L’ARME DU VIRUS|POUR ENTRER' },
  // s8 « Aujourd'hui, ce gène est toujours là. Dans ton ADN. Chromosome 7. »
  { a: ['s8', 0], type: 'mot', t: 'AUJOURD’HUI…', petit: true },
  { a: ['s8', 'toujours'], type: 'adn', sur: 'TON ADN', t: 'TOUJOURS LÀ|DANS TON ADN' },
  { a: ['s8', 'chromosome'], type: 'chromosome' },
  // s9 « Son nom : la syncytine. »
  { a: ['s9', 0], type: 'nom', t: 'SYNCYTINE', sous: 'un gène venu d’un virus' },
  // s10 « Quand tu étais embryon, elle a fusionné des cellules pour construire… ton placenta. »
  { a: ['s10', 0], type: 'embryon', t: 'QUAND TU ÉTAIS|EMBRYON', ch: 3 },
  { a: ['s10', 'fusionné'], type: 'fusion', mode: 'cellules', t: 'ELLE FUSIONNE|DES CELLULES' },
  { a: ['s10', 'ton'], type: 'portrait', img: 'placenta', t: 'TON PLACENTA', sous: 'construit grâce au gène du virus', choc: true },
  // s11 « L'organe qui t'a relié à ta mère. »
  { a: ['s11', 0], type: 'lien', t: 'L’ORGANE QUI T’A RELIÉ|À TA MÈRE' },
  // s12 « Des souris privées d'une syncytine ? Leurs embryons meurent avant de naître. »
  { a: ['s12', 0], type: 'souris', t: 'DES SOURIS|PRIVÉES DE SYNCYTINE ?' },
  { a: ['s12', 'leurs'], type: 'souris', mort: true, t: 'ELLES MEURENT|AVANT DE NAÎTRE', choc: true },
  // s13 « La preuve ? On compare ta syncytine 1 à une protéine du virus MSRV. »
  { a: ['s13', 0], type: 'mot', t: 'LA PREUVE ?', ch: 4 },
  { a: ['s13', 'compare'], type: 'compare', etape: 1 },
  // s14 « 87 pour cent de ressemblance. Entre un virus et toi ! »
  { a: ['s14', 0], av: .15, type: 'compare', etape: 2, pct: ['s14', '87'], choc: true },
  { a: ['s14', 'entre'], type: 'mot', t: 'ENTRE UN VIRUS|ET TOI !' },
  // s15 « Ça s'appelle un transfert horizontal de gènes. Près de 8 pour cent de ton ADN vient de virus. »
  { a: ['s15', 0], type: 'horizontal', t: 'TRANSFERT|HORIZONTAL' },
  { a: ['s15', 'près'], type: 'genome' },
  // s16 « Montrez que des transferts horizontaux ont contribué à la diversification des génomes : sujet type bac.
  //       La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'bacsvt', sujet: ['Montrez que des transferts', 'horizontaux ont contribué', 'à la diversification', 'des génomes.'] },
  { a: ['s16', 'sujet'], type: 'tampon', t: 'TYPE BAC' },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'SVT · chapitre 2', fond: 'placenta' },
  // s17 « La prochaine fois que tu maudis un virus… sans un virus, tu ne serais pas né. » (boucle vers le début)
  { a: ['s17', 0], type: 'mot', t: 'LA PROCHAINE FOIS|QUE TU MAUDIS UN VIRUS…' },
  { a: ['s17', 'sans'], type: 'virus', t: 'SANS UN VIRUS…|TU NE SERAIS PAS NÉ', taille: 96 },
]);
window.CHAPITRES = ['ACCROCHE', "L'INFECTION", 'LE GÈNE', 'LE PLACENTA', 'LA PREUVE'];
window.IMAGES = {
  vih: '../../svt/serie/img/ch2-vih.jpg',            // particules de VIH-1, microscopie électronique colorisée, NIAID, CC BY 2.0
  placenta: '../../svt/serie/img/ch2-placenta.jpg',  // placenta humain, face fœtale, photo Asturnut, CC BY-SA 3.0
};

window.MUSIQUE = 'suspense_phonk';   // musique imposée pour ce short
