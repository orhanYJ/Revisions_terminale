"""Short « Défi bac : 5 épreuves, es-tu prêt ? » : cinq formats où le spectateur joue, une matière par épreuve
(vrai ou faux en SVT, remets dans l'ordre en histoire, trouve l'intrus en philosophie, plus ou moins en géographie,
niveau 10 en physique-chimie). Habillage « jeu », musique automotivo2.

Faits : uniquement les cours de la chaîne.
1. SVT, VRAI — « mitochondries et chloroplastes descendent de bactéries phagocytées mais non digérées, devenues des
   partenaires permanents de la cellule eucaryote » ; « une phagocytose incomplète (bactérie non digérée) est à l'origine
   des mitochondries et des chloroplastes » (svt/index.html, glossaire « endosymbiose », chapitre 2 page t2b ;
   outils/serie-svt/svt_ch2.py).
2. Histoire, ordre — krach de Wall Street, octobre 1929 (24 et 29 octobre) ; Hitler nommé chancelier le 30 janvier 1933 ;
   opération Barbarossa le 22 juin 1941 ; Pearl Harbor le 7 décembre 1941 (dnl/index.html, H1, H2, H3).
3. Philosophie, intrus — pour Hobbes, Locke et Rousseau, l'État naît d'un contrat (outils/serie-philo/etat_2.py :
   « Pourquoi l'État ? Aristote, Hobbes, Locke, Rousseau », « Pour les autres, l'État est une invention : un contrat ») ;
   Descartes, le cogito (philo/index.html, « le socle du cogito »). Aristote, qui figure dans l'épisode mais pense la cité
   naturelle, n'est pas utilisé (il aurait été un second intrus possible).
4. Géographie, plus ou moins — parts de la capacité de la flotte mondiale (CNUCED, tonnes de port en lourd) :
   pétroliers 50 % en 1980, 28 % en 2024 ; vracs secs 27 % puis 43 % (dnl/index.html, G1, schéma G1Fleet et sa question
   de QCM « Quel type de navire a perdu le plus de place dans la flotte mondiale entre 1980 et 2024 ? »).
5. Physique-chimie, niveau 10 — « un photon de 11,0 eV arrivant sur un atome d'hydrogène au repos n'est pas absorbé :
   aucun écart ne vaut 11 eV (1 → 2 vaut 10,2 eV, 1 → 3 vaut 12,1 eV) » (pc/index.html, chapitre 4, fiche 2 ;
   animation pc/anim/photon.html).
Écartés : les décimales dans la voix (10,2 et 12,1 eV seulement à l'écran), la date exacte du krach (deux jours cités par
le cours), l'ADN mitochondrial transmis par la mère (glossaire seulement, pas le cœur du chapitre).
Aucune mention de la DNL, de la BFI ni d'un professeur.
"""
CODE = "defibac"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"SVT": "esse vé té", "Pearl Harbor": "Peurl Arbeur", "Wall Street": "Wol Strite",
                 "Hobbes": "Obbz", "Locke": "Lok", "cogito": "cogitô",
                 "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "10": "dix", "11": "onze", "28": "vingt-huit",
                 "1929": "mille neuf cent vingt-neuf", "1933": "mille neuf cent trente-trois", "1941": "mille neuf cent quarante et un",
                 "1980": "mille neuf cent quatre-vingts", "2024": "deux mille vingt-quatre"}
PASSAGES = [
    ("h1", "5 épreuves. 5 matières. Es-tu prêt pour le bac ?", 0.15),
    ("h2", "Compte tes points, 1 par épreuve. C'est parti !", 0.2),
    ("v0", "Épreuve 1, SVT.", 0.1),
    ("v1", "Tes mitochondries descendent d'une bactérie. Vrai… ou faux ?", 1.6),
    ("v2", "Vrai ! Une bactérie avalée, jamais digérée : c'est l'endosymbiose. 1 point.", 0.15),
    ("o0", "Épreuve 2, histoire.", 0.1),
    ("o1", "Remets ces 4 événements dans l'ordre.", 2.4),
    ("o2", "Krach en 1929, Hitler chancelier en 1933. Et le piège : Barbarossa en juin 1941, avant Pearl Harbor, en décembre.", 0.15),
    ("i0", "Épreuve 3, philosophie.", 0.1),
    ("i1", "Trois de ces penseurs fondent l'État sur un contrat. Trouve l'intrus.", 1.8),
    ("i2", "Descartes ! Hobbes, Locke et Rousseau : l'État naît d'un contrat. Lui, c'est le cogito.", 0.15),
    ("p0", "Épreuve 4, géographie.", 0.1),
    ("p1", "En 1980, les pétroliers font la moitié de la flotte mondiale. En 2024 : plus ou moins ?", 1.6),
    ("p2", "Moins ! 28 pour cent seulement. Les navires de vrac sec sont passés devant.", 0.15),
    ("n0", "Épreuve 5, niveau 10, physique-chimie.", 0.1),
    ("n1", "Un photon de 11 électronvolts frappe un atome d'hydrogène au repos. Absorbé ?", 1.8),
    ("n2", "Non ! Aucune transition ne vaut 11 électronvolts. Il faut l'énergie exacte, pas à peu près.", 0.15),
    ("e1", "Alors, prêt pour le bac ? Ton score sur 5 en commentaire.", 0.15),
    ("e2", "Toutes les matières sont sur Révisions Animées.", 0.0),
]
