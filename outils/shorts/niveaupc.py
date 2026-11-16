"""Short « Physique-chimie : niveau 1 → 10, à quel niveau tu t'arrêtes ? » : format « niveau » (le spectateur joue),
habillage néon, musique funk_agressif. Six paliers de difficulté croissante sur les cinq chapitres ouverts.

Faits : uniquement le cours de la chaîne (pc/index.html et outils/serie-pc/pc_ch1.py à pc_ch5.py) :
- niveau 1 : le jus de citron est acide, pH vers 2,5 ; sous 7 acide, 7 neutre (pc_ch1.py, l. 70-72 : « En dessous de sept,
  la solution est acide : le jus de citron, vers deux virgule cinq ») ;
- niveau 2 : « Diluer dix fois fait monter le pH d'exactement une unité » pour un acide fort (pc_ch1.py, l. 440-443 :
  10⁻² mol/L → pH 2, dilué dix fois → pH 3) ; pour un acide faible, moins (l. 671 : acide éthanoïque, + 0,6), d'où
  « pour un acide fort » dans la voix ;
- niveau 4 : loi de Beer-Lambert, « deux fois plus de molécules : A double, A ∝ c » ; A = k × c en solution diluée
  (pc_ch2.py, l. 165, 193, 223) ;
- niveau 6 : courbe pH = f(V) : montée lente, saut, palier ; V_E au milieu du saut, repéré par la méthode des tangentes
  parallèles (pc_ch3.py, l. 326, 342-346) ;
- niveau 8 : « Une lampe rouge, même énorme, même allumée des heures, ne fait sortir aucun électron d'une plaque de
  zinc » ; une lumière rouge intense envoie plus de photons, « mais chacun a exactement la même énergie » ; zinc :
  Φ = 4,3 eV, seuil vers 290 nm, « il faut de l'UV » (pc_ch4.py, l. 44, 144, 314-315, 344) ;
- niveau 10 : vergence C = 1/f′ en dioptries ; « Au TP sept, l'objectif a une vergence de deux dioptries, donc une focale
  de cinquante centimètres. L'oculaire a vingt dioptries : cinq centimètres » ; lunette afocale G = f′1/f′2
  (pc_ch5.py, l. 66-70, 297) → G = 50 / 5 = 10.
Écartés : les valeurs décimales dans la voix (pH 2,5 du citron, 4,3 eV du zinc : dites sans chiffre ou seulement à
l'écran), l'énergie d'un photon E = hν (gardée pour un autre short), le cercle oculaire (hors programme).
Images : pc/serie/img/ (licences dans les légendes de pc_ch1.py à pc_ch5.py, rappelées dans niveaupc.plan.js).
"""
CODE = "niveaupc"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Beer-Lambert": "Bère-Lambère", "pH": "pé-ache", "G": "gé",
                 "1": "un", "2": "deux", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit",
                 "10": "dix", "20": "vingt", "50": "cinquante"}
PASSAGES = [
    ("h1", "Physique-chimie : niveau 1 à 10.", 0.15),
    ("h2", "À quel niveau tu t'arrêtes ? Pas de triche.", 0.2),
    ("q1", "Niveau 1. Le jus de citron : acide ou basique ?", 1.6),
    ("r1", "Acide ! Son pH est bien en dessous de 7.", 0.15),
    ("q2", "Niveau 2. Tu dilues 10 fois un acide fort. Que fait son pH ?", 1.6),
    ("r2", "Il monte d'exactement 1. Toujours, pour un acide fort.", 0.15),
    ("t1", "Trop facile ? On passe aux dosages.", 0.15),
    ("q4", "Niveau 4. Tu doubles la concentration d'une solution colorée. Son absorbance ?", 1.6),
    ("r4", "Elle double. Loi de Beer-Lambert : l'absorbance est proportionnelle à la concentration.", 0.15),
    ("q6", "Niveau 6. Sur une courbe de titrage, comment trouves-tu l'équivalence ?", 1.6),
    ("r6", "La méthode des tangentes. L'équivalence est au milieu du saut de pH.", 0.15),
    ("t2", "Là, ça pique. Place à la lumière.", 0.15),
    ("q8", "Niveau 8. Une lampe rouge énorme éclaire une plaque de zinc. Des électrons sortent ?", 1.6),
    ("r8", "Aucun ! Un photon rouge n'a pas assez d'énergie. Il faut de l'ultraviolet.", 0.15),
    ("q10", "Niveau 10. Lunette afocale. Objectif de 2 dioptries, oculaire de 20. Grossissement ?", 1.6),
    ("r10", "10 ! Focales de 50 et 5 centimètres, et G égale 50 sur 5.", 0.2),
    ("e1", "Alors, tu t'arrêtes où ? Dis ton niveau en commentaire.", 0.15),
    ("e2", "Tous les chapitres sont sur Révisions Animées.", 0.0),
]
