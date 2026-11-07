// Découpage du short Milgram (« Tu aurais appuyé ? »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Est-ce que tu enverrais 450 volts à un inconnu… juste parce qu'on te le demande ? »
  { a: ['s1', 0], av: .25, type: 'panneau', etapes: [[null, 0], [['s1', '450'], 450]], t: 'TU ENVERRAIS|450 VOLTS ?', taille: 100, ch: 0 },
  { a: ['s1', 'inconnu'], type: 'chaise', t: 'À UN|INCONNU ?' },
  { a: ['s1', 'juste'], type: 'mot', t: 'JUSTE PARCE QU’ON TE LE DEMANDE', petit: true },
  // s2 « Non ? Eux aussi, ils pensaient que non. »
  { a: ['s2', 0], type: 'mot', t: 'NON ?', sombre: true },
  { a: ['s2', 'eux'], type: 'mot', t: 'EUX AUSSI…', img: 'penseur' },
  // s3 « 1961, université Yale. Une petite annonce : quatre dollars cinquante pour une expérience sur la mémoire. »
  { a: ['s3', 0], type: 'date', t: '1961', de: 1900, sous: 'UNIVERSITÉ YALE', ch: 1 },
  { a: ['s3', 'petite'], type: 'annonce', cercle: ['s3', 'dollars'] },
  // s4 « Dans la pièce d'à côté, un homme est attaché sur une chaise. Une électrode au poignet. »
  { a: ['s4', 0], type: 'chaise', t: 'ATTACHÉ|SUR UNE CHAISE' },
  { a: ['s4', 'électrode'], type: 'chaise', zoom: true, t: 'UNE ÉLECTRODE|AU POIGNET' },
  // s5 « Toi, tu poses les questions. À chaque erreur, tu appuies. Et à chaque erreur… 15 volts de plus. »
  { a: ['s5', 0], type: 'mot', t: 'TOI.', sous: 'tu poses les questions' },
  { a: ['s5', 'appuies'], type: 'panneau', etapes: [[null, 0], [['s5', 'appuies'], 15]], t: 'À CHAQUE ERREUR|+15 VOLTS' },
  // s6 « 45 volts. 75. 150. »
  { a: ['s6', 0], type: 'panneau', etapes: [[null, 15], [['s6', 0], 45], [['s6', '75'], 75], [['s6', '150'], 150]], zoom: true },
  // s7 « À 300 volts, l'homme cogne contre le mur. »
  { a: ['s7', 0], type: 'panneau', etapes: [[null, 150], [['s7', '300'], 300]] },
  { a: ['s7', 'cogne'], type: 'mur', choc: true, t: 'IL COGNE|CONTRE LE MUR', ch: 2 },
  // s8 « Tu te retournes. Un homme en blouse grise te dit, calmement : veuillez continuer. »
  { a: ['s8', 0], type: 'blouse' },
  { a: ['s8', 'veuillez'], type: 'ordre', t: 'Veuillez continuer.', duree: .7, taille: 110 },
  // s9 « 315 volts. Il cogne encore. Puis… plus rien. Le silence. »
  { a: ['s9', 0], type: 'panneau', etapes: [[null, 300], [['s9', 0], 315]] },
  { a: ['s9', 'cogne'], type: 'mur', coups: [0], t: 'ENCORE.' },
  { a: ['s9', 'plus'], type: 'silence', silence: true, muet: true, t: '… plus rien.' },
  // s10 « L'expérience exige que vous continuiez. Vous n'avez pas le choix. »
  { a: ['s10', 0], type: 'ordre', t: "L'expérience exige|que vous continuiez.", duree: 1.1 },
  { a: ['s10', "n'avez"], av: .35, type: 'ordre', t: "Vous n'avez pas|le choix.", duree: .8, tampon: true },
  // s11 « Avant l'expérience, des étudiants de Yale l'avaient prédit : à peine une personne sur cent irait jusqu'au bout. »
  { a: ['s11', 0], type: 'sondage', etape: 1, ch: 3 },
  // s12 « Résultat : 26 sur 40. Presque deux sur trois. Jusqu'à 450 volts. »
  { a: ['s12', 0], type: 'mot', t: 'RÉSULTAT', choc: true },
  { a: ['s12', '26'], type: 'sondage', etape: 2, rouges: ['s12', '26'], pct: ['s12', 'presque'] },
  { a: ['s12', "jusqu'à"], type: 'panneau', etapes: [[null, 315], [['s12', '450'], 450]], t: 'JUSQU’À|450 VOLTS' },
  // s13 « Ils transpirent, ils tremblent, certains éclatent d'un rire nerveux… mais ils appuient. »
  { a: ['s13', 0], type: 'sueur', etapes: [[null, 'ILS TRANSPIRENT'], [['s13', 'tremblent'], 'ILS TREMBLENT']] },
  { a: ['s13', 'rire'], type: 'portrait', img: 'masques', t: 'RIRE NERVEUX', sous: '14 sur 40' },
  { a: ['s13', 'mais'], type: 'tampon', t: 'ILS APPUIENT', choc: true },
  // s14 « Le plus fou ? L'homme était un acteur. Il n'a jamais reçu la moindre décharge. Eux ne le savaient pas. »
  { a: ['s14', 0], type: 'mot', t: 'LE PLUS FOU ?' },
  { a: ['s14', "l'homme"], type: 'acteur', tampon: ['s14', 'acteur'], zero: ['s14', 'jamais'] },
  { a: ['s14', 'eux'], type: 'mot', t: 'EUX NE LE|SAVAIENT PAS' },
  // s15 « Milgram voulait comprendre une chose : comment des gens ordinaires avaient pu obéir aux nazis. »
  { a: ['s15', 0], type: 'perso', t: 'STANLEY MILGRAM', sous: 'psychologue · université Yale', ch: 4 },
  { a: ['s15', 'comment'], type: 'portrait', img: 'nuremberg', t: 'OBÉIR', sous: 'aux nazis ?' },
  // s16 « Obéir, est-ce faire son devoir ? C'est une vraie question de bac. La réponse est sur Révisions Animées. »
  { a: ['s16', 0], type: 'mot', t: 'OBÉIR, EST-CE|FAIRE SON DEVOIR\u202f?' },
  { a: ['s16', 'question'], type: 'bac', sujet: ['Obéir, est-ce', 'faire son devoir ?'] },
  { a: ['s16', 'réponse'], type: 'chaine', serie: 'Le devoir', fond: 'nuremberg' },
  // s17 « Et toi… tu aurais appuyé ? » (boucle vers le début)
  { a: ['s17', 0], type: 'doigt', t: 'ET TOI…|TU AURAIS APPUYÉ ?' },
]);
window.CHAPITRES = ['ACCROCHE', "L'EXPÉRIENCE", "L'ORDRE", 'LE RÉSULTAT', 'LE DEVOIR'];
window.IMAGES = {
  penseur: '../../philo/serie/img/t-penseur.jpg',        // Rodin, photo Jebulon, CC0
  masques: '../../philo/serie/img/t2-masques.jpg',       // photo M. Kaufman, CC BY-SA 4.0
  nuremberg: '../../philo/serie/img/dv5-nuremberg.jpg',  // procès de Nuremberg, photo Ray D'Addario, domaine public
};
