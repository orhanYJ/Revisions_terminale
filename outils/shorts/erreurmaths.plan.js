// Découpage du short « erreurmaths » (format « erreur » : trouve l'erreur dans trois copies de maths), modèle A,
// habillage archives. a: [passage, mot] ; av : avance sur le mot. Chaque manche : carte « MANCHE n », la copie
// (le spectateur lit pendant la voix, puis chrono de silence après « Trois, deux, un »), le verdict, puis des plans
// de liaison (portrait, schéma, formule). Formules : pas de ∞, →, ≠ (absents des polices) : en toutes lettres ou dessinés.
window.MUSIQUE = 'montagem3';
window.THEME = 'archives';
window.PLAN = S => S.plans([
  // e1 « 3 copies de maths. Une erreur cachée dans chacune. »
  { a: ['e1', 0], av: .2, type: 'photo', img: 'examen', t: '3 COPIES|DE MATHS', de: [1.05, .5, .5], vers: [1.25, .5, .55], nb: true, ch: 0 },
  { a: ['e1', 'une'], type: 'copies', t: '1 ERREUR|DANS CHACUNE' },
  // e2 « Toi, tu la trouves avant la fin du chrono ? On joue. »
  { a: ['e2', 0], type: 'collage', imgs: ['napier', 'euler', 'leibniz'], t: 'AVANT LA FIN|DU CHRONO ?' },
  { a: ['e2', 'on'], type: 'pret', t: 'ON JOUE !' },
  // e3 « Manche 1 : les logarithmes. Lis bien les 4 lignes. Trois, deux, un. »
  { a: ['e3', 0], type: 'manche', n: 1, matiere: 'LOGARITHMES', dessin: 'log', ch: 1 },
  { a: ['e3', 'lis'], type: 'erreur', matiere: 'MATHÉMATIQUES', sujet: 'Simplifier des logarithmes',
    lignes: ['ln(1) = 0', 'ln(2 × 5) = ln(2) + ln(5)', 'ln(3 + 4) = ln(3) + ln(4)', 'ln(e²) = 2'],
    faute: 2, correction: 'ln(7). Et ln(3) + ln(4) = ln(12)', chrono: ['e3', 'trois'], rep: ['e4', 0] },
  // e4 « Ligne 3 ! Le logarithme transforme un produit en somme. »
  { a: ['e4', 'le'], type: 'portrait', img: 'napier', t: 'NAPIER', sous: 'inventeur des logarithmes, 1614' },
  // e5 « Pas une somme en somme ! Logarithme de 3 plus 4, c'est logarithme de 7. »
  { a: ['e5', 0], type: 'mot', t: 'PAS UNE SOMME|EN SOMME', choc: true },
  // e6 « Et logarithme de 3, plus logarithme de 4, c'est logarithme de 12. »
  { a: ['e5', 'logarithme'], type: 'regle', e2: ['e6', 0] },
  // e7 « Manche 2 : l'exponentielle. Une seule ligne est fausse. Trois, deux, un. »
  { a: ['e7', 0], type: 'manche', n: 2, matiere: 'EXPONENTIELLE', dessin: 'exp', ch: 2 },
  { a: ['e7', 'une'], type: 'erreur', matiere: 'MATHÉMATIQUES', sujet: 'f(x) = exp(2x), pour tout réel x',
    lignes: ['exp(2x) > 0 pour tout réel x.', 'f′(x) = exp(2x).', 'Donc f′(x) > 0 : f est croissante.', 'f(0) = exp(0) = 1.'],
    faute: 1, correction: 'f′(x) = 2 exp(2x)', chrono: ['e7', 'trois'], rep: ['e8', 0] },
  // e8 « Ligne 2 ! La dérivée d'exponentielle de 2 x, ce n'est pas exponentielle de 2 x. »
  { a: ['e8', 'la'], type: 'portrait', img: 'euler', t: 'EULER', sous: 'e, le « nombre d’Euler »' },
  // e9 « Il manque un facteur 2 : la dérivée de 2 x. »
  { a: ['e9', 0], type: 'facteur' },
  // e10 « À retenir : exponentielle de u, dérivée, u prime fois exponentielle de u. »
  { a: ['e10', 0], type: 'retenir' },
  // e11 « Dernière manche, la plus dure : les limites. Courage. »
  { a: ['e11', 0], type: 'mot', t: 'LA PLUS|DURE', img: 'archimede', sombre: true, choc: true, ch: 3 },
  { a: ['e11', 'limites'], type: 'manche', n: 3, matiere: 'LIMITES', dessin: 'infini' },
  // e12 « Sujet : x carré moins x, en plus l'infini. Trois, deux, un. »
  { a: ['e12', 0], type: 'erreur', matiere: 'MATHÉMATIQUES', sujet: 'Limite de f(x) = x² − x|en + l’infini',
    lignes: ['x² tend vers + l’infini.', '− x tend vers − l’infini.', 'Donc f(x) tend vers 0.', 'Or f(x) = x(x − 1).'],
    faute: 2, correction: 'forme indéterminée !', chrono: ['e12', 'trois'], rep: ['e13', 0] },
  // e13 « Ligne 3 ! Plus l'infini moins l'infini, ça ne fait pas 0. » / e14 « C'est une forme indéterminée. On factorise par x. »
  { a: ['e13', 'plus'], type: 'fi', e2: ['e14', 0] },
  { a: ['e14', 'on'], type: 'facto' },
  // e15 « x fois x moins 1 : ça tend vers plus l'infini. »
  { a: ['e15', 'ça'], type: 'courbe' },
  // e16 « Alors, combien d'erreurs repérées ? 0, 1, 2 ou 3 ? Dis-le en commentaire. »
  { a: ['e16', 0], type: 'score', n: [['e16', '0'], ['e16', '1'], ['e16', '2'], ['e16', '3']], ch: 4 },
  { a: ['e16', 'dis'], type: 'mot', t: 'DIS-LE EN|COMMENTAIRE' },
  // e17 « Plus de défis sur Révisions Animées. »
  { a: ['e17', 0], type: 'chaine', serie: 'Défis du bac', fond: 'newton' },
]);
window.CHAPITRES = ['LE DÉFI', 'LOGARITHMES', 'EXPONENTIELLE', 'LIMITES', 'TON SCORE'];
window.IMAGES = {
  examen: '../../philo/serie/img/t-examen.jpg',          // salle d'examen, domaine public
  napier: 'img/maths-napier.jpg',        // John Napier, gravure de Samuel Freeman, 1835, d'après un portrait de 1616, domaine public (Wikimedia Commons)
  euler: 'img/maths-euler.jpg',          // Jakob Emanuel Handmann, Leonhard Euler, 1753, Kunstmuseum Basel, domaine public (Wikimedia Commons)
  leibniz: '../../philo/serie/img/leibniz.jpg',          // Christoph Bernhard Francke, Leibniz, vers 1695, domaine public
  archimede: '../../philo/serie/img/cs2-archimede.jpg',  // Archimède soulevant le monde avec un levier, gravure du Mechanics Magazine, Londres, 1824, domaine public
  newton: '../../philo/serie/img/t-newton.jpg',          // William Blake, Newton, 1795-1805, Tate, domaine public
};
