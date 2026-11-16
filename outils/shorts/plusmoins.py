"""Short « Plus ou moins ? » (toutes matières) : format « le spectateur joue », plan `plusmoins` des formats
(15/11/2026), 4 duels de chiffres tirés des cours de la chaîne.

Faits :
1. SVT (svt/index.html, page t1u2, brassage interchromosomique ; tableau « gènes hétérozygotes 1, 2, 3, 4 → gamètes
   possibles 2, 4, 8, 16 ») : avec n paires, 2^n gamètes équiprobables ; 3 paires → 8 ; chez l'humain, 23 paires
   → 2^23 = 8 388 608, « environ 8 millions » ; « la fécondation en combine deux au hasard ».
2. Histoire (dnl/index.html, chapitre H1, chiffres clés) : « De son sommet de 381 en septembre 1929, le Dow Jones tombe à
   41 en juillet 1932 — une perte de 89 % » ; le krach ouvre la Grande Dépression (titre et partie I du chapitre).
3. Physique (pc/index.html, chapitre 5 « La lunette astronomique », exercice 27 « Observation d'Olympus Mons ») : pour voir
   Mars avec la même taille apparente que la Lune à l'œil nu, G ≈ 105 ; pour Olympus Mons, « 650 km au lieu de
   6 800 km, c'est un objet dix fois plus petit, donc un grossissement dix fois plus grand, environ 1 100 » (le site
   corrige le corrigé du manuel, qui donne 110).
4. Géographie (dnl/index.html, chapitre G1, chiffres clés) : « 23.7 / 20.9 million barrels of oil a day through Malacca
   and Hormuz (2023) » : le short dit « près de 24 millions » et « environ 21 millions ».
Écartés : ZEE de la France (10,7 millions de km² : pas de chiffre comparable dans le cours), chômage américain
(3 % → 25 % : la crise de 1929 était déjà dans le duel 2), Stalingrad (pertes humaines : ton peu adapté à un jeu),
« premier détroit pétrolier du monde » pour Malacca (le cours ne compare que Malacca et Ormuz).
"""
CODE = "plusmoins"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"4": "quatre", "1": "un", "2": "deux", "3": "trois", "8": "huit", "10": "dix", "23": "vingt-trois",
                 "24": "vingt-quatre", "21": "vingt et un", "41": "quarante et un", "89": "quatre-vingt-neuf",
                 "105": "cent cinq", "1 100": "mille cent", "100": "cent", "381": "trois cent quatre-vingt-un",
                 "1929": "mille neuf cent vingt-neuf", "1932": "mille neuf cent trente-deux", "2023": "deux mille vingt-trois", "SVT": "esse-vé-té",
                 "Dow": "Dao", "Jones": "Djonze", "Olympus": "Olympusse", "Mons": "Monse", "Malacca": "Malaca",
                 "Ormuz": "Ormouz"}
PASSAGES = [
    ("h1", "Plus ou moins ? 4 chiffres fous, tirés de tes cours de Terminale.", 0.15),
    ("h2", "Compte tes bonnes réponses.", 0.3),
    ("d1a", "Duel 1 : la SVT.", 0.15),
    ("d1b", "Avec 3 paires de chromosomes, la méiose donne 8 gamètes différents. Avec tes 23 paires : plus ou moins ?", 2.2),
    ("r1", "Beaucoup plus : plus de 8 millions !", 0.15),
    ("e1", "Et la fécondation en réunit 2 au hasard.", 0.3),
    ("d2a", "Duel 2 : l'histoire.", 0.15),
    ("d2b", "Septembre 1929 : l'indice Dow Jones vaut 381 points. Juillet 1932 : plus ou moins ?", 2.2),
    ("r2", "Moins : 41 points ! Une chute de 89 pour cent.", 0.15),
    ("e2", "Le krach de 1929 ouvre la Grande Dépression, partout dans le monde.", 0.3),
    ("d3a", "Duel 3 : la physique.", 0.15),
    ("d3b", "Pour voir Mars aussi grosse que la Lune, une lunette doit grossir 105 fois. Et pour son volcan géant, Olympus Mons ?", 0.3),
    ("c3", "Trois, deux, un.", 0.6),
    ("r3", "Plus : environ 1 100 fois ! Le volcan est 10 fois plus petit que Mars.", 0.3),
    ("d4a", "Dernier duel : la géographie.", 0.15),
    ("d4b", "Chaque jour, près de 24 millions de barils de pétrole passent le détroit de Malacca. Et le détroit d'Ormuz ?", 2.2),
    ("r4", "Moins : environ 21 millions ! En 2023, Malacca fait mieux qu'Ormuz.", 0.3),
    ("f1", "Alors, combien de bonnes réponses ? Dis-le en commentaire.", 0.15),
    ("f2", "Tout est expliqué sur Révisions Animées.", 0.0),
]
