"""Short « Remets dans l'ordre : de la crise de 1929 à la guerre » (histoire), format « ordre » (le spectateur joue) :
trois manches de quatre événements, montrés mélangés ; les dates sont révélées au verdict.

Sources : uniquement les chapitres « La crise de 1929 » (H1) et « Les régimes totalitaires » (H2) du site (dnl/index.html)
et leurs séries vidéo (outils/serie-dnl/h1f_1.py à h1f_6.py, édition française ; h2_1.py à h2_9.py).
Manche 1, la crise :
- le krach de Wall Street, 24-29 octobre 1929 (h1f_1.py, « Jeudi noir 24 oct. · lundi noir 28 oct. · mardi noir 29 oct. ») ;
- le Royaume-Uni quitte l'étalon-or, septembre 1931 (h1f_2.py, « Royaume-Uni sept. 1931, Japon déc. 1931, États-Unis 1933,
  France 1936 ») ;
- Roosevelt entre en fonctions en mars 1933 et lance le New Deal (h1f_3.py, « Premier New Deal (1933-1935) ») ;
- le Front populaire gagne les élections en 1936, Léon Blum président du Conseil (h1f_3.py).
- Liaison : États-Unis, 14 millions de chômeurs, 25 % des actifs (h1f_2.py) ; Hoovervilles (h1f_2.py).
Manche 2, les totalitarismes :
- la marche sur Rome, octobre 1922 (h2_2.py) ; le premier plan quinquennal, 1928 (h2_3.py) ;
- Hitler nommé chancelier le 30 janvier 1933 (h2_2.py) ; la Grande Purge, 1937-1938 (h2_5.py).
- Liaison : le totalitarisme cherche à contrôler totalement la société, pour transformer l'homme selon une
  idéologie (h2_1.py, notion clé).
Manche 3, la marche à la guerre :
- la remilitarisation de la Rhénanie, 7 mars 1936 ; l'Anschluss, 12 mars 1938 ; Munich, septembre 1938 (29-30) ;
  le pacte germano-soviétique, 23 août 1939 (h1f_4.py ; h2_7.py ; h2_1.py).
- Liaison : « chaque concession est suivie d'une exigence plus grande » (h1f_4.py, apaisement) ;
  le 1er septembre 1939, l'Allemagne envahit la Pologne, neuf jours après le pacte (h2_7.py ; h1f_4.py).
Écartés : la Mandchourie (1931) et l'Éthiopie (1935), pour garder une manche par thème ; les lois de Nuremberg
(1935) et tout événement de persécution, pour ne pas en faire une carte de jeu ; le tarif Smoot-Hawley (1930) et
le Dust Bowl (1935), faute de place ; aucun chiffre de victimes.
"""
CODE = "ordre1929"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "4": "quatre", "9": "neuf", "12": "douze", "14": "quatorze",
                 "1922": "mille neuf cent vingt-deux", "1928": "mille neuf cent vingt-huit",
                 "1929": "mille neuf cent vingt-neuf", "1931": "mille neuf cent trente et un",
                 "1933": "mille neuf cent trente-trois", "1936": "mille neuf cent trente-six",
                 "1937": "mille neuf cent trente-sept", "1938": "mille neuf cent trente-huit",
                 "1939": "mille neuf cent trente-neuf",
                 "New Deal": "Niou Dil", "Wall Street": "Wol Strite", "Anschluss": "Anne-chlouss",
                 "Hoovervilles": "Houveur-ville"}
PASSAGES = [
    ("o1", "De la crise de 1929 à la guerre : remets 12 événements dans l'ordre.", 0.25),
    ("o2", "3 manches, 4 événements chacune. Compte tes points.", 0.3),
    ("m1", "Manche 1 : la crise économique.", 0.15),
    ("m1b", "Le New Deal. Le krach de Wall Street. Le Front populaire. Le Royaume-Uni quitte l'étalon-or.", 1.6),
    ("v1", "Le krach en 1929. L'or en 1931. Le New Deal en 1933. Le Front populaire en 1936.", 0.3),
    ("x1", "Aux États-Unis : 14 millions de chômeurs, et des bidonvilles, les Hoovervilles.", 0.3),
    ("m2", "Manche 2 : les totalitarismes.", 0.15),
    ("m2b", "Hitler chancelier. La Grande Purge. La marche sur Rome. Le premier plan de Staline. Trois, deux, un.", 0.2),
    ("v2", "Rome en 1922. Le plan en 1928. Hitler en 1933. La Purge en 1937.", 0.3),
    ("x2", "Trois régimes, un seul but : tout contrôler, et transformer l'homme.", 0.3),
    ("m3", "Dernière manche : la marche à la guerre.", 0.15),
    ("m3b", "L'Anschluss. Le pacte germano-soviétique. La Rhénanie. Munich.", 1.6),
    ("v3", "La Rhénanie en 1936. L'Anschluss en mars 1938. Munich en septembre. Le pacte en août 1939.", 0.3),
    ("x3a", "Chaque recul des démocraties appelle une exigence plus grande.", 0.3),
    ("x3", "9 jours plus tard, l'Allemagne envahit la Pologne. C'est la guerre.", 0.3),
    ("e1", "Alors, combien de manches réussies ? Dis-le en commentaire.", 0.25),
    ("e2", "Toute l'histoire est sur Révisions Animées.", 0.0),
]
