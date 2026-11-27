"""Short « Trouve l'erreur dans ces copies de maths » (format « erreur », le spectateur joue) : trois copies de
spécialité mathématiques de Terminale, quatre lignes chacune, une seule fausse ; un chrono, puis la correction.
Habillage archives, musique montagem3. La chaîne n'a pas de cours de maths : fin « Plus de défis ».

Sources : programme de spécialité mathématiques de Terminale générale, BO spécial n° 8 du 25 juillet 2019
(eduscol) : fonction logarithme (« ln(ab) = ln a + ln b »), dérivée de la composée « exp(u) » (« (e^u)′ = u′ e^u »),
limites de fonctions et formes indéterminées. Chaque ligne est vérifiée ici :
- copie 1 (logarithmes) : ln(1) = 0 (vrai) ; ln(2 × 5) = ln 2 + ln 5 (vrai, propriété du produit) ;
  L'ERREUR : ln(3 + 4) = ln 3 + ln 4. En fait ln(3 + 4) = ln 7 (environ 1,95) et ln 3 + ln 4 = ln 12 (environ 2,48) :
  le logarithme transforme un produit en somme, pas une somme en somme ; ln(e²) = 2 (vrai).
- copie 2 (exponentielle, f(x) = exp(2x)) : exp(2x) > 0 pour tout réel x (vrai) ; L'ERREUR : f′(x) = exp(2x).
  En fait, avec u(x) = 2x, u′(x) = 2 : f′(x) = 2 exp(2x) ; « donc f′(x) > 0 : f est croissante » (vrai, aussi avec la
  bonne dérivée) ; f(0) = exp(0) = 1 (vrai).
- copie 3 (limites, f(x) = x² − x en + l'infini) : x² tend vers + l'infini (vrai) ; − x tend vers − l'infini (vrai) ;
  L'ERREUR : « donc f(x) tend vers 0 » : + l'infini − l'infini est une forme indéterminée, pas 0 ;
  f(x) = x(x − 1) (vrai) ; x et x − 1 tendent vers + l'infini, donc f(x) tend vers + l'infini (produit).
Plans de liaison (à l'écran seulement) : Napier publie les logarithmes en 1614 (Mirifici logarithmorum canonis
descriptio), pour remplacer les multiplications par des additions ; le nombre e est appelé « nombre d'Euler » ;
gravure d'Archimède soulevant le monde (Mechanics Magazine, 1824) pour « la plus dure ».
Écartés : l'inégalité multipliée par un négatif (plutôt du niveau de Seconde, et quatre manches dépasseraient la
durée), la probabilité conditionnelle inversée (trop longue à lire en quatre lignes), les valeurs décimales de ln 7
et ln 12 dans la voix, les symboles absents des polices (∞, →, ≠ : écrits en toutes lettres). Le compte à rebours
« Trois, deux, un » reste en lettres, comme dans erreurbac.
Images : outils/shorts/img/maths-*.jpg (Wikimedia Commons), philo/serie/img/ (licences dans les CREDITS des séries).
"""
CODE = "erreurmaths"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "7": "sept", "12": "douze",
                 "x": "ixe"}
PASSAGES = [
    ("e1", "3 copies de maths. Une erreur cachée dans chacune.", 0.25),
    ("e2", "Toi, tu la trouves avant la fin du chrono ? On joue.", 0.3),
    ("e3", "Manche 1 : les logarithmes. Lis bien les 4 lignes. Trois, deux, un.", 1.3),
    ("e4", "Ligne 3 ! Le logarithme transforme un produit en somme.", 0.15),
    ("e5", "Pas une somme en somme ! Logarithme de 3 plus 4, c'est logarithme de 7.", 0.15),
    ("e6", "Et logarithme de 3, plus logarithme de 4, c'est logarithme de 12.", 0.3),
    ("e7", "Manche 2 : l'exponentielle. Une seule ligne est fausse. Trois, deux, un.", 1.3),
    ("e8", "Ligne 2 ! La dérivée d'exponentielle de 2 x, ce n'est pas exponentielle de 2 x.", 0.15),
    ("e9", "Il manque un facteur 2 : la dérivée de 2 x.", 0.15),
    ("e10", "À retenir : exponentielle de u, dérivée, u prime fois exponentielle de u.", 0.3),
    ("e11", "Dernière manche, la plus dure : les limites. Courage.", 0.2),
    ("e12", "Sujet : x carré moins x, en plus l'infini. Trois, deux, un.", 1.3),
    ("e13", "Ligne 3 ! Plus l'infini moins l'infini, ça ne fait pas 0.", 0.15),
    ("e14", "C'est une forme indéterminée. On factorise par x.", 0.15),
    ("e15", "x fois x moins 1 : ça tend vers plus l'infini.", 0.3),
    ("e16", "Alors, combien d'erreurs repérées ? 0, 1, 2 ou 3 ? Dis-le en commentaire.", 0.25),
    ("e17", "Plus de défis sur Révisions Animées.", 0.0),
]
