// Découpage du short « Maths : niveau 1 → 10 », modèle A, habillage néon. a: [passage, mot] ; av : avance sur le mot.
// Chaque palier est un plan « niveau » (formats-a.js) qui va de la question à l'explication ; un plan dessiné, une
// photo, un collage ou un portrait fait la liaison avec le palier suivant (jamais deux plans de suite du même type).
// Formules à l'écran : seulement des caractères des polices Archivo et Spectral (pas de →, ≈, ∞, ∫).
window.MUSIQUE = 'funk_agressif3';
window.THEME = 'neon';
window.PLAN = S => S.plans([
  // h1 « Maths : niveau 1 à 10. »
  { a: ['h1', 0], av: .25, type: 'photo', img: 'newton', t: 'MATHS|NIVEAU 1 À 10', de: [1.05, .5, .45], vers: [1.25, .45, .5],
    legende: 'William Blake, Newton, 1795-1805, Tate, domaine public', ch: 0 },
  // h2 « Pas de calculatrice. Tu t'arrêtes où ? »
  { a: ['h2', 0], type: 'nocalc', img: 'calculatrice', choc: true },
  { a: ['h2', 'tu'], type: 'echelle' },
  // niveau 1 : la suite qui double
  { a: ['q1', 0], type: 'niveau', n: 1, total: 10, q: 'u(0) = 3 et u(n+1) = 2 × u(n)|Combien vaut u(2) ?', chrono: ['q1', -1], rep: ['r1', 0],
    r: 'u(2) = 12', expl: '3, 6, 12 : suite géométrique de raison 2', ch: 1 },
  { a: ['r1', 'suite'], type: 'suite' },
  // niveau 2 : la convexité
  { a: ['q2', 0], type: 'niveau', n: 2, total: 10, q: 'f″ positive sur un intervalle I|f convexe ou concave ?', chrono: ['q2', 'concave'], rep: ['r2', 0],
    r: 'CONVEXE', expl: 'La courbe est au-dessus de ses tangentes' },
  { a: ['r2', 'la'], type: 'convexe' },
  // t1 « Facile ? On monte. »
  { a: ['t1', 0], type: 'collage', imgs: ['euler', 'gauss', 'bernoulli'], t: 'FACILE ?|ON MONTE', ch: 2 },
  // niveau 4 : la limite d'un quotient
  { a: ['q4', 0], type: 'niveau', n: 4, total: 10, q: '(2n + 1) / (n + 3)|Limite quand n tend vers + l’infini ?', chrono: ['q4', "l'infini"], rep: ['r4', 0],
    r: '2', expl: 'Termes de plus haut degré : 2n / n = 2' },
  { a: ['r4', 'seuls'], type: 'limite' },
  // niveau 5 : le logarithme
  { a: ['q5', 0], type: 'niveau', n: 5, total: 10, img: 'napier', q: 'ln(8) = k × ln(2)|Combien vaut k ?', chrono: ['q5', -1], rep: ['r5', 0],
    r: 'k = 3', expl: '8 = 2³, donc ln(8) = 3 ln(2)' },
  { a: ['r5', 'car'], type: 'puissance' },
  // t2 « Ça se corse. Place aux intégrales. »
  { a: ['t2', 0], type: 'mot', t: 'ÇA SE|CORSE', choc: true, ch: 3 },
  { a: ['t2', 'place'], type: 'portrait', img: 'leibniz', t: 'LEIBNIZ', sous: 'le premier signe de l’intégrale, 1675' },
  // niveau 7 : l'intégrale
  { a: ['q7', 0], type: 'niveau', n: 7, total: 10, q: 'Intégrale de 0 à 1|de 2x dx = ?', chrono: ['q7', -1], rep: ['r7', 0],
    r: '1', expl: 'Primitive de 2x : x². Donc 1² − 0² = 1' },
  { a: ['r7', 'une'], type: 'aire' },
  // niveau 8 : les poignées de main
  { a: ['q8', 0], type: 'niveau', n: 8, total: 10, q: '5 personnes se serrent toutes la main|Combien de poignées de main ?', chrono: ['q8', 'poignées'], rep: ['r8', 0],
    r: '10', expl: '2 parmi 5 = (5 × 4) / 2 = 10' },
  { a: ['r8', 'parmi'], type: 'poignees' },
  // q10 « Le boss. Niveau 10. Tu lances 2 dés. Probabilité d'avoir au moins un 6 ? »
  { a: ['q10', 0], type: 'photo', img: 'galton', t: 'LE BOSS|NIVEAU 10', de: [1.05, .5, .55], vers: [1.3, .5, .62], choc: true, ch: 4,
    legende: 'Planche de Galton, Matemateca IME-USP, photo Rodrigo Argenton, CC BY-SA 4.0' },
  { a: ['q10', 'tu'], type: 'niveau', n: 10, total: 10, q: 'Tu lances 2 dés équilibrés|P(au moins un 6) = ?', chrono: ['q10', 'moins'], rep: ['r10', 0],
    r: '11 / 36', expl: '1 − (5/6)² = 1 − 25/36 = 11/36' },
  { a: ['r10', 'par'], type: 'arbre' },
  // e1 « Alors, tu t'arrêtes où ? Dis ton niveau en commentaire. »
  { a: ['e1', 0], type: 'mot', t: 'ALORS, TU T’ARRÊTES|OÙ ?' },
  { a: ['e1', 'dis'], type: 'commentaire' },
  // e2 « Plus de défis sur Révisions Animées. »
  { a: ['e2', 0], type: 'chaine', serie: 'Défis du bac', fond: 'euler' },
]);
window.CHAPITRES = ['ACCROCHE', 'LES BASES', 'LIMITES ET LOGARITHME', 'INTÉGRALES ET DÉNOMBREMENT', 'LE BOSS · TON NIVEAU'];
window.IMAGES = {
  newton: '../../philo/serie/img/t-newton.jpg',            // William Blake, Newton, 1795-1805, Tate, domaine public
  calculatrice: '../../pc/serie/img/c4-calculatrice.jpg',  // calculatrice solaire, photo Evan-Amos, domaine public
  euler: 'img/maths-euler.jpg',          // Jakob Emanuel Handmann, Leonhard Euler, 1753, Kunstmuseum Basel, domaine public (Wikimedia Commons)
  gauss: 'img/maths-gauss.jpg',          // Christian Albrecht Jensen, Carl Friedrich Gauss, 1840, domaine public (Wikimedia Commons)
  bernoulli: 'img/maths-bernoulli.jpg',  // Niklaus Bernoulli, Jacques (Jakob) Bernoulli, 1687, domaine public (Wikimedia Commons)
  napier: 'img/maths-napier.jpg',        // John Napier, gravure de Samuel Freeman, 1835, d'après un portrait de 1616, domaine public (Wikimedia Commons)
  leibniz: '../../philo/serie/img/leibniz.jpg',            // Christoph Bernhard Francke, Leibniz, vers 1695, domaine public
  galton: 'img/maths-galton.jpg',        // planche de Galton, Matemateca IME-USP, photo Rodrigo Argenton, CC BY-SA 4.0 (attribution obligatoire)
};
