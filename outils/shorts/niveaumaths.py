"""Short « Maths : niveau 1 → 10, à quel niveau tu t'arrêtes ? » : format « niveau » (le spectateur joue),
habillage néon, musique funk_agressif3. Sept paliers de difficulté croissante, de tête, sur le programme de
spécialité mathématiques de Terminale (la chaîne n'a pas de cours de maths : fin « Plus de défis »).

Sources : programme de spécialité mathématiques de Terminale générale, BO spécial n° 8 du 25 juillet 2019
(eduscol, « Mathématiques, enseignement de spécialité, classe terminale ») : suites et limites de suites,
convexité (« f convexe si et seulement si f″ ≥ 0 ; courbe au-dessus de ses tangentes »), fonction logarithme
(« ln(ab) = ln a + ln b, ln(a^n) = n ln a »), primitives et calcul intégral, combinatoire (« nombre de parties à k
éléments d'un ensemble à n éléments »), succession d'épreuves indépendantes et loi binomiale. Chaque résultat est
recalculé ici :
- niveau 1 : u(0) = 3 et u(n+1) = 2 u(n) : u(1) = 6, u(2) = 12 (suite géométrique de raison 2, rappel de Première) ;
- niveau 2 : f″ positive sur un intervalle → f convexe sur cet intervalle ; la courbe est au-dessus de ses tangentes ;
- niveau 4 : (2n + 1) / (n + 3) = (2 + 1/n) / (1 + 3/n) → 2 quand n tend vers + l'infini ;
- niveau 5 : ln 8 = ln(2³) = 3 ln 2, donc k = 3 ;
- niveau 7 : une primitive de 2x est x² ; intégrale de 0 à 1 de 2x dx = 1² − 0² = 1 (aire d'un triangle de base 1 et de
  hauteur 2 : 1, vérification) ;
- niveau 8 : 5 personnes, chaque paire se serre la main une fois : « 2 parmi 5 » = 5 × 4 / 2 = 10 ;
- niveau 10 : deux dés équilibrés indépendants ; P(aucun 6) = (5/6)² = 25/36 ; P(au moins un 6) = 1 − 25/36 = 11/36
  (environ 0,306) : on passe par l'événement contraire.
Plans de liaison (à l'écran seulement) : Napier publie les logarithmes en 1614 (Mirifici logarithmorum canonis
descriptio) ; Leibniz écrit pour la première fois le signe de l'intégrale dans un manuscrit de 1675 ; la planche de
Galton montre la loi binomiale (les billes rebondissent à gauche ou à droite à chaque rangée de clous).
Écartés : l'espérance d'une loi binomiale (trop facile pour le niveau 10), le vecteur normal à un plan (géométrie
dans l'espace : la question tient mal en trois secondes à l'oral), « 3 secondes par question » (le chrono réel
dépend de la voix : on dit seulement « pas de calculatrice »), toute formule lue avec un symbole absent des polices
(→, ≈, ∞, ∫ : écrits en toutes lettres ou dessinés).
Images : outils/shorts/img/maths-*.jpg (Wikimedia Commons, licences dans niveaumaths.plan.js et la description),
philo/serie/img/ et pc/serie/img/ (licences dans les CREDITS des scripts des séries).
"""
CODE = "niveaumaths"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six",
                 "7": "sept", "8": "huit", "10": "dix", "11": "onze", "12": "douze", "36": "trente-six",
                 "f": "effe", "n": "enne", "k": "ka", "x": "ixe"}
PASSAGES = [
    ("h1", "Maths : niveau 1 à 10.", 0.15),
    ("h2", "Pas de calculatrice. Tu t'arrêtes où ?", 0.2),
    ("q1", "Niveau 1. u 0 vaut 3, chaque terme double. u 2 ?", 1.4),
    ("r1", "12 ! Suite géométrique de raison 2.", 0.15),
    ("q2", "Niveau 2. f seconde positive : f convexe ou concave ?", 1.4),
    ("r2", "Convexe ! La courbe est au-dessus de ses tangentes.", 0.15),
    ("t1", "Facile ? On monte.", 0.15),
    ("q4", "Niveau 4. 2 n plus 1, sur n plus 3. Limite en plus l'infini ?", 1.4),
    ("r4", "2 ! Seuls comptent les termes forts : 2 n sur n.", 0.15),
    ("q5", "Niveau 5. Logarithme de 8 égale k fois logarithme de 2. k ?", 1.4),
    ("r5", "3 ! Car 8, c'est 2 puissance 3.", 0.15),
    ("t2", "Ça se corse. Place aux intégrales.", 0.15),
    ("q7", "Niveau 7. L'intégrale de 0 à 1 de 2 x ?", 1.4),
    ("r7", "1 ! Une primitive de 2 x, c'est x carré.", 0.15),
    ("q8", "Niveau 8. 5 personnes se serrent toutes la main. Combien de poignées ?", 1.4),
    ("r8", "10 ! 2 parmi 5 : 5 fois 4, divisé par 2.", 0.2),
    ("q10", "Le boss. Niveau 10. Tu lances 2 dés. Probabilité d'avoir au moins un 6 ?", 1.6),
    ("r10", "11 sur 36 ! Par le contraire : 1 moins 5 sixièmes au carré.", 0.2),
    ("e1", "Alors, tu t'arrêtes où ? Dis ton niveau en commentaire.", 0.15),
    ("e2", "Plus de défis sur Révisions Animées.", 0.0),
]
