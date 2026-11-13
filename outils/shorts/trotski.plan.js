// Découpage du short Trotski (« Sauf les amis »), modèle A. a: [passage, mot] ; av : avance sur le mot.
window.PLAN = S => S.plans([
  // s1 « Tu as commandé l'Armée rouge… et maintenant, tu te caches derrière des murs ? »
  { a: ['s1', 0], av: .25, type: 'etoile', t: 'TU AS COMMANDÉ|L’ARMÉE ROUGE', ch: 0 },
  { a: ['s1', 'maintenant'], type: 'maison', etat: 'forteresse', t: 'CACHÉ|DERRIÈRE DES MURS ?' },
  // s2 « Mexico, 1940. Tu es Léon Trotski. »
  { a: ['s2', 0], type: 'trotski', t: 'LÉON TROTSKI', sous: 'Mexico, 1940', ch: 1 },
  // s3 « 1917 : avec Lénine, tu fais la révolution. Puis tu commandes l'Armée rouge. »
  { a: ['s3', 0], type: 'portrait', img: 'lenine', t: '1917', sous: 'avec Lénine, la révolution' },
  { a: ['s3', 'puis'], type: 'etoile', t: 'L’ARMÉE|ROUGE' },
  // s4 « Mais Staline prend le pouvoir. Ton rival. »
  { a: ['s4', 0], type: 'portrait', img: 'staline', t: 'STALINE', sous: 'prend le pouvoir' },
  { a: ['s4', 'ton'], type: 'duel', t: 'TON RIVAL' },
  // s5 « Chassé du parti. En 1929, chassé d'URSS. »
  { a: ['s5', 0], type: 'expulse', etape: 1 },
  { a: ['s5', 'en'], type: 'expulse', etape: 2 },
  // s6 « Turquie. France. Norvège. Mexique. Staline ne t'oublie pas. »
  { a: ['s6', 0], type: 'exil', etapes: [[['s6', 0], 'TURQUIE'], [['s6', 'france'], 'FRANCE'], [['s6', 'norvège'], 'NORVÈGE'], [['s6', 'mexique'], 'MEXIQUE']] },
  { a: ['s6', 'staline'], type: 'mot', img: 'staline', t: "NE T'OUBLIE PAS" },
  // s7 « Mai 1940. Une nuit, des hommes armés mitraillent ta maison. »
  { a: ['s7', 0], type: 'maison', etat: 'nuit', t: 'MAI 1940|UNE NUIT', ch: 2 },
  { a: ['s7', 'mitraillent'], type: 'maison', etat: 'balles', choc: true, t: 'ILS|MITRAILLENT' },
  // s8 « Tu survis. On relève les murs. On ajoute des miradors. »
  { a: ['s8', 0], type: 'mot', t: 'TU|SURVIS.' },
  { a: ['s8', 'relève'], type: 'maison', etat: 'murs', t: 'ON RELÈVE|LES MURS' },
  { a: ['s8', 'ajoute'], type: 'maison', etat: 'tours', t: 'DES MIRADORS|UNE FORTERESSE' },
  // s9 « Ta maison devient une forteresse. Personne n'entre… sauf les amis. »
  { a: ['s9', 'personne'], type: 'porte', ouvre: ['s9', 'sauf'], t: "PERSONNE N'ENTRE…|SAUF LES AMIS" },
  // s10 « Un jeune homme, Jacques Mornard, sort avec une de tes militantes. »
  { a: ['s10', 0], type: 'jeune', t: 'JACQUES MORNARD', sous: 'un jeune homme' },
  { a: ['s10', 'sort'], type: 'jeune', coeur: true, t: 'JACQUES MORNARD', sous: 'il sort avec une de tes militantes' },
  // s11 « Il vient souvent. Les gardes le traitent comme un proche. »
  { a: ['s11', 0], type: 'porte', ouvre: ['s11', 0], visiteur: true, gardes: true, t: 'IL VIENT SOUVENT|COMME UN PROCHE' },
  // s12 « 20 août 1940. Il t'apporte un article à relire. Et un imperméable au bras. En plein soleil. »
  { a: ['s12', 0], type: 'date', t: '1940', de: 1937, sous: '20 AOÛT', ch: 3 },
  { a: ['s12', 'il'], type: 'article' },
  { a: ['s12', 'et'], type: 'imper', soleil: ['s12', 'plein'], t: 'UN IMPERMÉABLE|EN PLEIN SOLEIL ?' },
  // s13 « Seuls, dans ton bureau. Tu te penches sur le texte. »
  { a: ['s13', 0], type: 'bureau', t: 'SEULS' },
  { a: ['s13', 'tu'], type: 'bureau', penche: true, t: 'TU TE PENCHES|SUR LE TEXTE' },
  // s14 « Sous l'imperméable : un piolet. »
  { a: ['s14', 0], type: 'piolet', revele: ['s14', 'piolet'], t: "SOUS|L'IMPERMÉABLE…" },
  { a: ['s14', 'piolet'], type: 'piolet', revele: ['s14', 'piolet'], choc: true },
  // s15 « Tu te débats. Les gardes accourent. Tu meurs le lendemain. »
  { a: ['s15', 0], type: 'mot', t: 'TU TE|DÉBATS' },
  { a: ['s15', 'les'], type: 'porte', ouvre: ['s15', 'les'], gardes: true, t: 'LES GARDES|ACCOURENT' },
  { a: ['s15', 'meurs'], av: .35, type: 'deuil', silence: true },
  // s16 « Son vrai nom : Ramón Mercader. Agent du NKVD, la police de Staline. »
  { a: ['s16', 0], type: 'dossier' },
  { a: ['s16', 'ramón'], type: 'dossier', vrai: ['s16', 'ramón'], agent: ['s16', 'agent'], choc: true },
  // s17 « Même au bout du monde, la terreur frappe. Même les anciens chefs du régime. »
  { a: ['s17', 0], type: 'monde', t: 'MÊME AU BOUT|DU MONDE', ch: 4 },
  { a: ['s17', 'terreur'], type: 'mot', t: 'LA TERREUR|FRAPPE', sombre: true },
  { a: ['s17', 'anciens'], type: 'portrait', img: 'proces', t: 'MÊME LES CHEFS', sous: 'procès de Moscou, 1937' },
  // s18 « En quoi la terreur est-elle au cœur du régime stalinien ? Une question de bac. La réponse est sur Révisions Animées. »
  { a: ['s18', 0], type: 'mot', t: 'LA TERREUR, AU CŒUR|DU RÉGIME ?' },
  { a: ['s18', 'stalinien'], type: 'portrait', img: 'staline', t: 'STALINIEN ?', sous: 'une méthode de gouvernement' },
  { a: ['s18', 'question'], type: 'bac', matiere: 'HISTOIRE', sujet: ['En quoi la terreur est-elle', 'au cœur du régime stalinien ?'] },
  { a: ['s18', 'réponse'], type: 'chaine', serie: 'Les régimes totalitaires', fond: 'proces' },
  // s19 « Et toi… à qui tu aurais ouvert la porte ? » (boucle vers « … tu te caches derrière des murs ? »)
  { a: ['s19', 0], type: 'porte', ouvre: ['s19', 'ouvert'], visiteur: true, t: 'ET TOI…|TU AURAIS OUVERT ?' },
]);
window.CHAPITRES = ['ACCROCHE', "L'EXIL", 'LA FORTERESSE', 'LE 20 AOÛT', 'LA TERREUR'];
window.IMAGES = {
  lenine: '../../dnl/serie/img/h2-lenin-putilov.jpg',   // Isaak Brodsky, Lénine parle aux ouvriers de l'usine Poutilov (mai 1917), 1929, domaine public
  staline: '../../dnl/serie/img/h2-stalin.jpg',         // Staline à la tribune, Moscou, 1937, photographe inconnu, domaine public
  proces: '../../dnl/serie/img/h2-moscow-trial.jpg',    // les accusés du deuxième procès de Moscou, janvier 1937, photographe inconnu, domaine public
};
window.MUSIQUE = 'phonk_tension';   // musique imposée pour ce short
