"""Short « Seconde Guerre mondiale : niveau 1 → 10, à quel niveau tu t'arrêtes ? » (histoire), format « niveau »
(le spectateur joue) : sept paliers de difficulté croissante (niveaux 1, 2, 4, 5, 7, 9, 10 sur 10).

Sources : uniquement le chapitre « La Seconde Guerre mondiale » du site (dnl/index.html, CHAPTERS.H3) et son édition
vidéo française (outils/serie-dnl/h3f_1.py à h3f_7.py, surtout le récapitulatif h3f_7.py) ; pour le niveau 1, le
chapitre « Les régimes totalitaires » (h2_7.py).
- Niveau 1 : le 1er septembre 1939, l'Allemagne envahit la Pologne, après son pacte avec l'Union soviétique
  (h3f_7.py, « le film de la guerre » ; pacte du 23 août 1939 qui prévoit en secret le partage de la Pologne : h2_7.py,
  h3f_4.py « sept. 1939 la Pologne partagée »).
- Niveau 2 : le 18 juin 1940, l'appel du général de Gaulle, depuis Londres, à la radio de la BBC (h3f_7.py, dix dates ;
  h3f_3.py, document A).
- Niveau 4 : Churchill, Premier ministre le 10 mai 1940, refuse de négocier ; le Blitz ne parvient pas à briser le
  Royaume-Uni (h3f_3.py, frise ; h3f_7.py).
- Niveau 5 : en décembre 1941 (le 7, frise de h3f_7.py), le Japon attaque Pearl Harbor ; la guerre devient mondiale
  (h3f_7.py).
- Niveau 7 : le 22 juin 1941, l'opération Barbarossa ; trois poussées (Leningrad, Moscou, Kiev et Rostov) ; une guerre
  d'anéantissement à l'Est (h3f_4.py, idée 2 ; h3f_7.py).
- Niveau 9 : le 31 janvier 1943, Paulus capitule à Stalingrad (derniers combats le 2 février) : le tournant de la guerre
  (h3f_4.py ; h3f_7.py).
- Niveau 10 : pour Robert Frank et Alya Aglan (« La Guerre-monde »), la guerre mondiale commence en Asie, en 1937, quand
  le Japon attaque la Chine (h3f_1.py ; h3f_7.py, quiz). Le short dit « certains historiens », sans les nommer.
Écartés : toute question sur le génocide des Juifs d'Europe (centres de mise à mort, Treblinka, ghetto de Varsovie),
pour ne pas traiter la Shoah sur le ton d'un jeu chronométré ; les chiffres de morts ; Dunkerque (338 000 évacués),
l'armistice du 22 juin 1940 et Vichy, faute de place ; Montoire (hors du cours).
Aucune image choquante : portraits, une tribune, un studio de radio, des enfants assis dans les décombres du Blitz.
"""
CODE = "niveauguerre"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "4": "quatre", "5": "cinq", "7": "sept", "9": "neuf", "10": "dix",
                 "18": "dix-huit", "22": "vingt-deux", "31": "trente et un", "1er": "premier",
                 "1937": "mille neuf cent trente-sept", "1939": "mille neuf cent trente-neuf",
                 "1940": "mille neuf cent quarante", "1941": "mille neuf cent quarante et un",
                 "1943": "mille neuf cent quarante-trois",
                 "BBC": "bé-bé-cé", "Pearl Harbor": "Peurl Arbeur", "Paulus": "Paou-louss", "Blitz": "Blits",
                 "URSS": "u-erre-èsse-èsse"}
PASSAGES = [
    ("i1", "Seconde Guerre mondiale, niveau 1 à 10. À quel niveau tu t'arrêtes ?", 0.25),
    ("i2", "Plus tu montes, plus c'est dur. Réponds avant le chrono.", 0.3),
    ("q1", "Niveau 1. 1er septembre 1939 : quel pays l'Allemagne envahit-elle ?", 1.6),
    ("r1", "La Pologne. Juste après son pacte avec Staline.", 0.3),
    ("q2", "Niveau 2. De Gaulle lance son appel depuis Londres. Quel jour ? Trois, deux, un.", 0.2),
    ("r2", "Le 18 juin 1940, à la radio de la BBC.", 0.3),
    ("q3", "Niveau 4. Quel Premier ministre refuse de négocier avec Hitler, en 1940 ?", 1.6),
    ("r3", "Churchill. Sous les bombes du Blitz, le Royaume-Uni tient.", 0.3),
    ("q4", "Niveau 5. Quelle attaque fait entrer les États-Unis dans la guerre ? Trois, deux, un.", 0.2),
    ("r4", "Pearl Harbor, le 7 décembre 1941. La guerre devient mondiale.", 0.3),
    ("t1", "Ça se corse.", 0.2),
    ("q5", "Niveau 7. Comment s'appelle l'invasion de l'URSS, le 22 juin 1941 ?", 1.6),
    ("r5", "Barbarossa : trois poussées, une guerre d'anéantissement.", 0.3),
    ("q6", "Niveau 9. À Stalingrad, quel général allemand capitule ? Trois, deux, un.", 0.2),
    ("r6", "Paulus, le 31 janvier 1943 : le tournant de la guerre.", 0.3),
    ("q7", "Niveau 10. Pour certains historiens, la guerre mondiale commence en Asie. En quelle année ?", 1.6),
    ("r7", "1937 ! Cette année-là, le Japon attaque la Chine.", 0.3),
    ("e1", "Alors ? Dis ton niveau en commentaire.", 0.25),
    ("e2", "Toute la guerre est sur Révisions Animées.", 0.0),
]
