// Découpage du short Stockdale (« Ton avion est en feu »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Ton avion est en feu. Tu t'éjectes. 30 secondes avant de toucher le sol. »
  { a: ['s1', 0], av: .25, type: 'avion', t: 'TON AVION|EST EN FEU', ch: 0 },
  { a: ['s1', 'tu'], type: 'ejection', t: 'TU T’ÉJECTES', choc: true },
  { a: ['s1', '30'], type: 'chute', t: '30 SECONDES', sous: 'avant de toucher le sol', chrono: 30 },
  // s2 « Et tu penses… à un philosophe grec. »
  { a: ['s2', 0], type: 'mot', t: 'ET TU PENSES…', sombre: true },
  { a: ['s2', 'philosophe'], type: 'mot', t: 'À UN PHILOSOPHE|GREC', img: 'epictete' },
  // s3 « 1965, au-dessus du Nord-Vietnam. James Stockdale, pilote américain, descend en parachute. »
  { a: ['s3', 0], type: 'date', t: '1965', de: 1900, sous: 'NORD-VIETNAM', ch: 1 },
  { a: ['s3', 'james'], type: 'portrait', img: 'stockdale', t: 'STOCKDALE', sous: 'pilote de l’US Navy' },
  { a: ['s3', 'descend'], type: 'chute', t: 'EN PARACHUTE', village: true },
  // s4 « Il se murmure : 5 ans là-dessous, au moins. Je quitte le monde de la technologie… j'entre dans celui d'Épictète. »
  { a: ['s4', 0], type: 'mot', t: 'IL SE MURMURE…', petit: true },
  { a: ['s4', '5'], type: 'murmure', t: '5 ans là-dessous,|au moins.', duree: 1.1 },
  { a: ['s4', 'quitte'], type: 'mondes', barre: ['s4', 'technologie'] },
  { a: ['s4', "j'entre"], type: 'portrait', img: 'epictete', t: 'ÉPICTÈTE', sous: 'j’entre dans son monde' },
  // s5 « En bas, on le roue de coups. Jambe cassée. Direction Hoa Lo, le Hanoï Hilton. »
  { a: ['s5', 0], type: 'mot', t: 'EN BAS…|ROUÉ DE COUPS' },
  { a: ['s5', 'jambe'], type: 'tampon', t: 'JAMBE CASSÉE', choc: true },
  { a: ['s5', 'direction'], type: 'lieu', img: 'hoalo', t: 'HOA LO', sous: '« Hanoï Hilton »', surnom: ['s5', 'hanoï'] },
  // s6 « Torture. Fers aux pieds. Isolement. Il avait dit 5 ans… ce sera plus de 7. »
  { a: ['s6', 0], type: 'cellule', mots: [[['s6', 0], 'TORTURE'], [['s6', 'fers'], 'FERS AUX PIEDS'], [['s6', 'isolement'], 'ISOLEMENT']] },
  { a: ['s6', 'il'], type: 'jours', court: ['s6', 'ce'] },
  { a: ['s6', 'plus'], type: 'mot', t: 'PLUS DE|7 ANS', choc: true },
  // s7 « Mais dans sa tête, il a emporté un livre : le Manuel d'Épictète. »
  { a: ['s7', 0], type: 'tetelivre', t: 'DANS SA TÊTE…', livre: ['s7', 'livre'], ch: 2 },
  { a: ['s7', 'manuel'], type: 'mot', t: 'LE MANUEL|D’ÉPICTÈTE', img: 'manuel' },
  // s8 « Il y a ce qui dépend de nous… et ce qui ne dépend pas de nous. »  (s9 remplit les colonnes)
  { a: ['s8', 0], type: 'colonnes' },
  { a: ['s8', 'et'], type: 'colonnes' },
  // s9 « Son corps, la douleur : ça ne dépend pas de lui. Ce qu'il accepte, ce qu'il refuse : ça, oui. »
  { a: ['s9', 0], type: 'colonnes' },
  { a: ['s9', 'ce'], type: 'colonnes' },
  // s10 « Un jour, on lui tend un rasoir : signe qu'on va le filmer pour la propagande. »
  { a: ['s10', 0], type: 'rasoir', t: 'UN RASOIR', ch: 3 },
  { a: ['s10', 'signe'], type: 'camera', t: 'ON VA|LE FILMER', prop: ['s10', 'propagande'] },
  // s11 « Alors il se rase une bande au milieu du crâne. Et se frappe le visage avec un tabouret. Méconnaissable. »
  { a: ['s11', 0], type: 'crane', t: 'AU MILIEU|DU CRÂNE' },
  { a: ['s11', 'et'], type: 'tabouret', t: 'IL SE FRAPPE|LE VISAGE', sous: 'avec un tabouret', coup: ['s11', 'tabouret'] },
  { a: ['s11', 'méconnaissable'], type: 'flou', t: 'MÉCONNAISSABLE' },
  // s12 « Le film n'aura pas lieu. »
  { a: ['s12', 0], type: 'camera', t: 'LE FILM|N’AURA PAS LIEU', coupe: true, choc: true },
  // s13 « Libéré en 1973, il recevra la Medal of Honor. »
  { a: ['s13', 0], type: 'date', t: '1973', de: 1965, sous: 'LIBÉRÉ', ch: 4 },
  { a: ['s13', 'recevra'], type: 'medaille', t: 'MEDAL OF HONOR', sous: 'la plus haute décoration militaire américaine' },
  // s14 « On lui a tout pris. Sauf une chose : son jugement. »
  { a: ['s14', 0], type: 'mot', t: 'ON LUI A|TOUT PRIS', img: 'hoalo' },
  { a: ['s14', 'sauf'], type: 'mot', t: 'SAUF UNE CHOSE…', petit: true },
  { a: ['s14', 'son'], type: 'citadelle', t: 'SON JUGEMENT' },
  // s15 « Peut-on être libre sous la contrainte ? C'est une vraie question de bac. La réponse est sur Révisions Animées. »
  { a: ['s15', 0], type: 'mot', t: 'LIBRE|SOUS LA CONTRAINTE ?' },
  { a: ['s15', "c'est"], type: 'bac', sujet: ['Peut-on être libre', 'sous la contrainte ?'] },
  { a: ['s15', 'réponse'], type: 'chaine', serie: 'La liberté', fond: 'hoalo' },
  // s16 « Et toi… ton avion est en feu. À quoi tu penses ? » (boucle vers le début)
  { a: ['s16', 0], type: 'mot', t: 'ET TOI…', sombre: true },
  { a: ['s16', 'ton'], type: 'avion', t: 'TON AVION|EST EN FEU', bis: 'À QUOI|TU PENSES ?', abis: ['s16', 'quoi'] },
]);
window.CHAPITRES = ['ACCROCHE', 'LA CHUTE', 'LE MANUEL', 'LE REFUS', 'LA LIBERTÉ'];
window.IMAGES = {
  stockdale: '../../philo/serie/img/stockdale.jpg',      // portrait officiel, US Navy, domaine public
  epictete: '../../philo/serie/img/epictete.jpg',        // Épictète, gravure ancienne, domaine public
  manuel: '../../philo/serie/img/t4-epictete.jpg',       // frontispice du Manuel, Oxford, 1715 (gravure de M. Burghers), domaine public
  hoalo: '../../philo/serie/img/t4-hoalo.jpg',           // Hanoï, entrée de la prison de Hoa Lo (photo David McKelvey, CC BY 2.0)
};
