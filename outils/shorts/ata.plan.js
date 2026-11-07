// Découpage du short 'Ata (« le vrai Sa Majesté des mouches »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « 6 ados. Une île déserte. Pas d'adulte, pas de règles, pas d'État. »
  { a: ['s1', 0], av: .25, type: 'ados', t: '6 ADOS', taille: 170, ch: 0 },
  { a: ['s1', 'une'], type: 'ile', t: 'UNE ÎLE|DÉSERTE' },
  { a: ['s1', 'pas'], type: 'sans', etapes: [[['s1', "d'adulte"], 'PAS D’ADULTE'], [['s1', 'règles'], 'PAS DE RÈGLES'], [['s1', "d'État"], 'PAS D’ÉTAT']] },
  // s2 « Que va-t-il se passer ? »
  { a: ['s2', 0], type: 'mot', t: 'QUE VA-T-IL|SE PASSER ?', sombre: true },
  // s3 « Juin 1965, Tonga. 6 pensionnaires s'ennuient. Ils empruntent un bateau… sans demander. »
  { a: ['s3', 0], type: 'date', t: '1965', de: 1900, sous: 'JUIN · TONGA', ch: 1 },
  { a: ['s3', '6'], type: 'mot', t: '6 PENSIONNAIRES|QUI S’ENNUIENT' },
  { a: ['s3', 'empruntent'], type: 'bateau', t: 'ILS EMPRUNTENT|UN BATEAU', tampon: ['s3', 'sans'] },
  // s4 « Pas de carte, pas de boussole. Et la nuit, la tempête. »
  { a: ['s4', 0], type: 'sanscarte', x1: ['s4', 'carte'], x2: ['s4', 'boussole'] },
  { a: ['s4', 'et'], type: 'tempete', t: 'LA TEMPÊTE', choc: true },
  // s5 « Voile déchirée, gouvernail cassé. 8 jours à la dérive, sans manger. »
  { a: ['s5', 0], type: 'tempete', casse: true, voile: ['s5', 'déchirée'], gouv: ['s5', 'cassé'] },
  { a: ['s5', '8'], type: 'compteur', n: 8, duree: 1.7, t: 'JOURS À LA DÉRIVE', sous: 'sans manger' },
  // s6 « L'eau de pluie ? Partagée : une gorgée le matin, une le soir. »
  { a: ['s6', 0], type: 'pluie' },
  { a: ['s6', 'partagée'], type: 'gorgee', m: ['s6', 'matin'], s: ['s6', 'soir'] },
  // s7 « Puis un rocher surgit : 'Ata. Désert depuis un siècle. »
  { a: ['s7', 0], type: 'rocher', nom: ['s7', "'ata"] },
  { a: ['s7', 'désert'], type: 'mot', t: 'DÉSERT|DEPUIS UN SIÈCLE' },
  // s8 « Dans le roman Sa Majesté des mouches, des enfants seuls sombrent dans la violence. »
  { a: ['s8', 0], type: 'livre', ch: 2 },
  { a: ['s8', 'sombrent'], type: 'tampon', t: 'VIOLENCE', choc: true },
  // s9 « Eux ? Équipes de 2. Potager, cuisine, tours de garde. »
  { a: ['s9', 0], type: 'equipes' },
  { a: ['s9', 'potager'], type: 'taches', etapes: [[['s9', 'potager'], 'POTAGER'], [['s9', 'cuisine'], 'CUISINE'], [['s9', 'tours'], 'GARDE']] },
  // s10 « Une dispute ? Pause obligatoire pour se calmer. Et le feu ne s'éteint jamais. »
  { a: ['s10', 0], type: 'dispute', pause: ['s10', 'pause'] },
  { a: ['s10', 'et'], type: 'feu', t: 'LE FEU|NE S’ÉTEINT JAMAIS' },
  // s11 « Stephen tombe d'une falaise : jambe cassée. Les autres lui font une attelle… et travaillent à sa place. »
  { a: ['s11', 0], type: 'chute', t: 'STEPHEN|TOMBE DE LA FALAISE' },
  { a: ['s11', 'jambe'], type: 'jambe', attelle: ['s11', 'attelle'], choc: true },
  { a: ['s11', 'travaillent'], type: 'mot', t: 'ILS TRAVAILLENT|À SA PLACE' },
  // s12 « Septembre 1966. Un capitaine australien remarque des traces de feu sur les falaises. »
  { a: ['s12', 0], type: 'date', t: '1966', de: 1965, sous: 'SEPTEMBRE', ch: 3 },
  { a: ['s12', 'capitaine'], type: 'capitaine' },
  { a: ['s12', 'traces'], type: 'jumelles' },
  // s13 « Chez eux, on les croyait morts. On avait célébré leurs funérailles. »
  { a: ['s13', 0], type: 'mot', t: 'ON LES CROYAIT|MORTS', sombre: true },
  { a: ['s13', 'célébré'], type: 'funerailles' },
  // s14 « Ils ont tenu 15 mois. Ensemble. »
  { a: ['s14', 0], type: 'mois', ens: ['s14', 'ensemble'] },
  // s15 « Hobbes l'affirmait : sans État, c'est la guerre de tous contre tous. »
  { a: ['s15', 0], type: 'portrait', img: 'hobbes', t: 'HOBBES', sous: 'Léviathan, 1651', ch: 4 },
  { a: ['s15', 'guerre'], type: 'mot', t: 'LA GUERRE DE TOUS|CONTRE TOUS', img: 'leviathan' },
  // s16 « Alors, Hobbes avait tort ? Pas si vite : 6 garçons, ce n'est pas un pays. Et ils ont recréé des règles. »
  { a: ['s16', 0], type: 'mot', t: 'HOBBES|AVAIT TORT ?' },
  { a: ['s16', 'pas'], type: 'mot', t: 'PAS SI VITE.', choc: true },
  { a: ['s16', '6'], type: 'mot', t: '6 GARÇONS|≠ UN PAYS' },
  { a: ['s16', 'et'], type: 'regles', tampon: ['s16', 'recréé'] },
  // s17 « Peut-on se passer de l'État ? Vraie question de bac. La réponse est sur Révisions Animées. »
  { a: ['s17', 0], type: 'mot', t: 'PEUT-ON SE PASSER|DE L’ÉTAT ?' },
  { a: ['s17', 'question'], type: 'bac', sujet: ['Peut-on se passer', 'de l’État ?'] },
  { a: ['s17', 'réponse'], type: 'chaine', serie: "L'État", fond: 'leviathan' },
  // s18 « Et toi… sur cette île, tu aurais fait quoi ? » (boucle vers le début)
  { a: ['s18', 0], type: 'ados', t: 'ET TOI…|TU AURAIS FAIT QUOI ?', taille: 110 },
]);
window.CHAPITRES = ['ACCROCHE', 'LA FUGUE', "L'ÎLE", 'LE SECOURS', "L'ÉTAT"];
window.IMAGES = {
  tempete: '../../philo/serie/img/t4-tempete.jpg',       // Rembrandt, La Tempête sur la mer de Galilée, 1633, domaine public
  hobbes: '../../philo/serie/img/hobbes.jpg',            // John Michael Wright, Thomas Hobbes, vers 1669-1670, domaine public
  leviathan: '../../philo/serie/img/et2-leviathan.jpg',  // Abraham Bosse, frontispice du Léviathan, 1651 (British Library), domaine public
};
