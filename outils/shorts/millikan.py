"""Short « Il voulait prouver qu'Einstein avait tort » (physique-chimie, chapitre 4 « La lumière, un flux de photons ») :
Robert Millikan et l'effet photoélectrique, à la deuxième personne. Format 1 (histoire vraie folle), musique trap.

Faits du cours de la chaîne (pc/index.html, chapitre 4, fiches 1 à 5 et exercice 27 ; outils/serie-pc/pc_ch4.py) :
Einstein, 1905 : la lumière est faite de quanta d'énergie hν, un photon cède toute son énergie à un seul électron ;
l'énergie cinétique des électrons dépend de la fréquence, pas de l'intensité ; le modèle ondulatoire « triomphait
depuis un siècle » ; jeune employé de l'office des brevets de Berne ; prix Nobel 1921 pour ce travail, pas pour la
relativité ; Millikan, convaincu qu'Einstein avait tort, passe dix ans à mesurer l'effet ; ses mesures de 1916
confirment la relation (droites parallèles Ec = f(ν), pente h) et lui donnent une valeur précise de h ; prix Nobel
1923 ; établir la relation d'Einstein est une question de bac (« Au bac, on peut te demander d'établir cette relation »).

Faits pris ailleurs, vérifiés :
- R. A. Millikan, « A Direct Photoelectric Determination of Planck's "h" », Physical Review 7 (3), 1916, p. 355-388
  (PDF : authors.library.caltech.edu, CaltechAUTHORS:20131203-155712735) : l'hypothèse d'Einstein y est dite « bold,
  not to say the reckless » (audacieuse, pour ne pas dire téméraire) et la théorie « pretty generally abandoned »,
  alors que l'équation est vérifiée ; surfaces débarrassées de leurs couches (films) dans le vide ; « a machine shop in
  vacuo » : couteau rotatif K déplacé par des électroaimants placés hors du tube, qui rabote des cylindres de sodium
  (et de lithium) ; travaux au laboratoire Ryerson (université de Chicago ; non dit dans le short).
- Wikipédia (en), « Robert Millikan », section Photoelectric effect : convaincu que la théorie d'Einstein devait être
  fausse ; programme expérimental de dix ans ; atelier dans le vide pour obtenir une surface très propre.
- nobelprize.org : Einstein, prix Nobel de physique 1921 « for his services to Theoretical Physics, and especially for
  his discovery of the law of the photoelectric effect » (remis en 1922) ; Millikan, prix 1923 « for his work on the
  elementary charge of electricity and on the photoelectric effect ».
Écarté : les citations de l'autobiographie de 1950 et de l'hommage de 1949 (texte connu seulement de seconde main),
la précision exacte de h (0,5 % selon l'APS, non vérifiable ici), le fait que Millikan mesurait h/e et non h directement
(nuance hors programme). La dernière phrase relance la première (boucle).
"""
CODE = "millikan"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Millikan": "Milikane", "Planck": "Planque",
                 "10": "dix", "4": "quatre", "1905": "mille neuf cent cinq", "1916": "mille neuf cent seize",
                 "1921": "mille neuf cent vingt et un", "1923": "mille neuf cent vingt-trois"}
PASSAGES = [
    ("s1", "Tu passerais 10 ans à prouver qu'Einstein a tort… pour finir par lui donner raison ?", 0.3),
    ("s2", "Robert Millikan, lui, l'a fait.", 0.3),
    ("s3", "1905. Albert Einstein, jeune employé des brevets, ose une idée folle : la lumière est faite de grains.", 0.2),
    ("s4", "Pour arracher un électron à un métal, c'est la fréquence qui compte. Pas l'intensité.", 0.25),
    ("s5", "Toi, tu es Millikan. Pour toi, c'est absurde : depuis un siècle, la lumière est une onde.", 0.25),
    ("s6", "Tu veux la mesure parfaite. Celle qui fera tomber Einstein.", 0.25),
    ("s7", "Problème : la moindre couche d'oxyde sur le métal fausse tout.", 0.2),
    ("s8", "Alors tu construis un atelier… dans le vide. Un couteau, guidé par des aimants, rabote le sodium sous vide.", 0.25),
    ("s9", "Tu éclaires. Tu mesures. Fréquence après fréquence. Pendant 10 ans.", 0.3),
    ("s10", "1916. Le verdict tombe.", 0.35),
    ("s11", "Tes points s'alignent. Une droite parfaite. Exactement celle d'Einstein.", 0.25),
    ("s12", "Pire : sa pente te donne la constante de Planck.", 0.35),
    ("s13", "Le plus fou ? Même là, tu n'y crois pas. Tu écris que son idée est téméraire.", 0.35),
    ("s14", "Einstein reçoit le Nobel 1921 pour l'effet photoélectrique, pas pour la relativité. Toi, celui de 1923.", 0.3),
    ("s15", "C'est le chapitre 4 de physique. Établir la relation d'Einstein : vraie question de bac.", 0.2),
    ("s16", "La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Et toi… tu passerais 10 ans à prouver qu'Einstein a tort ?", 0.0),
]
