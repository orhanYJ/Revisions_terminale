"""Short « NSI : niveau 1 → 10, à quel niveau tu t'arrêtes ? » : format « niveau » (le spectateur joue),
habillage terminal, musique automotivo2. Six paliers de difficulté croissante, spécialité NSI de Terminale.

La chaîne n'a pas de cours de NSI : les questions suivent le programme officiel de NSI (BO spécial n° 8 du
25 juillet 2019, eduscol « Programme de numérique et sciences informatiques de terminale générale ») et chaque
résultat a été vérifié en exécutant le code Python correspondant (27/11/2026) :
- niveau 1 : 13 en binaire = 1101 (8 + 4 + 0 + 1) ; bin(13) == '0b1101' (représentation des entiers, rappel de Première) ;
- niveau 2 : pile (structure LIFO, programme de Terminale « listes, piles, files ») : on empile A, B, C, pop() rend C ;
  une file (FIFO) rend A en premier (collections.deque.popleft()) ;
- niveau 4 : SQL, requêtes d'interrogation SELECT, FROM, WHERE (programme de Terminale, bases de données) ;
  WHERE ne garde que les lignes qui vérifient la condition (vérifié avec sqlite3 : SELECT nom FROM eleves WHERE note > 14) ;
- niveau 6 : récursivité (programme de Terminale) : f(0) = 0, f(n) = n + f(n - 1) ; f(4) == 10 ;
- niveau 8 : recherche dichotomique dans une liste triée (rappel de Première, « diviser pour régner » en Terminale) :
  au pire 20 tours de boucle pour 1 000 000 éléments (mesuré : 20 ; floor(log2(10**6)) + 1 = 20 ; 2**20 = 1 048 576) ;
- niveau 10 : calculabilité, décidabilité (programme de Terminale : « montrer, sans formalisme théorique, que le problème
  de l'arrêt est indécidable ») ; Turing, « On Computable Numbers », 1936 : premiers problèmes indécidables
  (Stanford Encyclopedia of Philosophy, « Turing Machines » ; Hamkins et Nenu, arXiv 2407.00680 : l'attribution du
  problème de l'arrêt à Turing est « raisonnable avec réserve », d'où « une idée qui remonte à Turing » dans la voix).
Écartés : la hauteur d'un arbre (deux conventions selon les manuels : racine seule de hauteur 0 ou 1), le protocole
RIP (trop long à poser), la complexité en O(log n) dite comme telle (remplacée par le nombre d'étapes).
Images : outils/shorts/img/ (Wikimedia Commons, licences dans niveaunsi.plan.js et la description).
"""
CODE = "niveaunsi"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"NSI": "ène-èsse-i", "SQL": "esse-cu-elle", "WHERE": "ouère", "Turing": "Turingue",
                 "B": "bé", "C": "cé", "f": "effe",
                 "1101": "un, un, zéro, un", "1936": "mille neuf cent trente-six",
                 "0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "6": "six", "8": "huit",
                 "10": "dix", "13": "treize", "14": "quatorze", "20": "vingt"}
PASSAGES = [
    ("h1", "NSI : niveau 1 à 10.", 0.15),
    ("h2", "À quel niveau tu t'arrêtes ? Pas de triche.", 0.2),
    ("q1", "Niveau 1. Écris 13 en binaire.", 1.3),
    ("r1", "1101 ! Soit 8 plus 4 plus 1.", 0.15),
    ("q2", "Niveau 2. Une pile : tu empiles A, B, puis C. Qui sort en premier ?", 1.3),
    ("r2", "C ! Le dernier arrivé sort le premier. Une file, c'est l'inverse.", 0.15),
    ("t1", "Trop facile ? On passe aux bases de données.", 0.15),
    ("q4", "Niveau 4. En SQL, quel mot-clé filtre les lignes d'une table ?", 1.3),
    ("r4", "WHERE ! Il garde seulement les lignes qui vérifient ta condition.", 0.15),
    ("q6", "Niveau 6. Lis ce code récursif. Que renvoie f de 4 ?", 1.6),
    ("r6", "10 ! 4 plus 3 plus 2 plus 1 plus 0. La fonction s'appelle elle-même.", 0.15),
    ("t2", "Là, ça pique. Place aux algorithmes.", 0.15),
    ("q8", "Niveau 8. Recherche dichotomique dans 1 million d'éléments triés. Combien d'étapes, au pire ?", 1.3),
    ("r8", "20 ! Tu coupes en 2 à chaque étape. Et 2 puissance 20 dépasse 1 million.", 0.15),
    ("q10", "Niveau 10, boss final. Un programme peut-il prédire si n'importe quel programme s'arrête ?", 1.6),
    ("r10", "Non ! Le problème de l'arrêt est indécidable. Une idée qui remonte à Turing, en 1936.", 0.15),
    ("e1", "Alors, tu t'arrêtes où ? Dis ton niveau en commentaire.", 0.15),
    ("e2", "Plus de défis sur Révisions Animées.", 0.0),
]
