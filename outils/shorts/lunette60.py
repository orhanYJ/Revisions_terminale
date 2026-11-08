"""Short « La lunette astronomique en 60 secondes » (physique-chimie, chapitre 5) : résumé express, format 3,
musique pop.

Faits : uniquement le cours de la chaîne (pc/index.html, chapitre 5, fiches 1 à 5 ; outils/serie-pc/pc_ch5.py) :
- la lunette = deux lentilles minces convergentes de même axe : l'objectif L1 (côté objet, grande focale), l'oculaire L2
  (côté œil, petite focale) ;
- objet à l'infini → image dans le plan focal image ; l'objectif donne une image intermédiaire A1B1, réelle et
  renversée, dans son plan focal image ; taille F′B′ ≈ f′ × α : la Lune (α = 9,0 × 10⁻³ rad) au foyer d'un objectif de
  700 mm donne une image de 6,3 mm (dit « environ 6 millimètres ») ;
- lunette afocale : F′1 = F2 ; O1O2 = f′1 + f′2 (lunette du TP 7 : 50 cm + 5,0 cm = 55 cm) ;
- l'image intermédiaire est dans le plan focal objet de l'oculaire → image à l'infini, rayons émergents parallèles
  entre eux ; l'œil normal voit net à l'infini au repos, sans accommoder : on observe longtemps sans fatigue ;
- image renversée : les rayons incidents descendent, les rayons émergents montent ; « un cratère au nord de la Lune
  est donc vu en bas » ;
- G = α′/α = f′1/f′2 ; lunette 70/700 avec un oculaire de 10 mm : G = 700/10 = 70 ;
- erreur classique du QCM : écrire F1 = F′2 ou F′1 = F′2 au lieu de F′1 = F2 ;
- la démonstration de G est « à savoir rédiger » (savoir-faire C4).
Écarté : cercle oculaire, diamètre de l'objectif, Galilée et Kepler (hors programme) ; aucun fait pris hors du cours.
Schémas : rayons calculés en lentilles minces dans lunette60.types-a.js (faisceau incident parallèle → B1 dans le plan
focal → faisceau émergent parallèle à (B1O2)).
"""
CODE = "lunette60"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"60": "soixante", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six",
                 "10": "dix", "50": "cinquante", "55": "cinquante-cinq", "70": "soixante-dix", "700": "sept cents",
                 "F": "effe", "f": "effe", "G": "gé"}
PASSAGES = [
    ("s1", "La lunette astronomique en 60 secondes. C'est parti.", 0.25),
    ("s2", "Une lunette, c'est 2 lentilles convergentes. L'objectif, côté ciel. L'oculaire, côté œil.", 0.25),
    ("s3", "Idée 1 : l'objectif forme une image réelle de l'astre, dans son plan focal image.", 0.15),
    ("s4", "La Lune, avec un objectif de 700 millimètres ? Une image d'environ 6 millimètres.", 0.3),
    ("s5", "Idée 2 : réglage afocal. Le foyer image de l'objectif coïncide avec le foyer objet de l'oculaire.", 0.15),
    ("s6", "Objectif de 50 centimètres, oculaire de 5 centimètres : 55 centimètres entre les deux.", 0.3),
    ("s7", "Idée 3 : les rayons ressortent parallèles. L'image est à l'infini.", 0.15),
    ("s8", "Ton œil la voit net sans accommoder. Tu peux observer longtemps.", 0.3),
    ("s9", "Idée 4 : l'image est renversée. Les rayons entrent en descendant, ressortent en montant.", 0.15),
    ("s10", "Un cratère au nord de la Lune ? Tu le vois en bas.", 0.3),
    ("s11", "Idée 5 : le grossissement. G égale alpha prime sur alpha, le rapport des angles.", 0.15),
    ("s12", "Pour une lunette afocale, G égale f prime 1 sur f prime 2.", 0.2),
    ("s13", "700 millimètres sur 10 : elle grossit 70 fois.", 0.3),
    ("s14", "L'erreur classique : F prime 1 égale F 2. Pas F 1 égale F prime 2.", 0.3),
    ("s15", "La démonstration de G ? À savoir rédiger au bac. Elle est dans le chapitre 5, sur Révisions Animées.", 0.0),
]
