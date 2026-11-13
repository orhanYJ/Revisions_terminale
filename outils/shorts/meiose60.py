"""Short « La méiose en 60 secondes » (SVT, chapitre 1 « L'origine du génotype des individus », unité 2), format 3 :
les cinq idées clés de la méiose et des brassages.

Sources : uniquement le cours de la chaîne (svt/index.html, page t1u2, « B. Le cadre : méiose et fécondation »,
« D. Le premier brassage : interchromosomique », « E. Le second brassage : intrachromosomique », « À retenir » ;
définitions du vocabulaire de la professeure « Méiose », « Brassage interchromosomique », « Brassage
intrachromosomique », « Crossing-over » ; script outils/serie-svt/svt_ch1.py).
- Idée 1 : méiose = succession de deux divisions cellulaires qui, à partir d'une cellule diploïde (2n), produit quatre
  cellules haploïdes (n) génétiquement différentes, les gamètes ; chez l'humain 2n = 46 et n = 23 ; elle divise le
  nombre de chromosomes par deux.
- Idée 2 : en prophase I, les homologues s'apparient et forment un bivalent de quatre chromatides ; deux chromatides
  non sœurs se croisent en un point appelé chiasma, se cassent au même niveau et échangent leurs segments : le
  crossing-over, mécanisme du brassage intrachromosomique (nouvelles combinaisons d'allèles sur un même chromosome).
- Idée 3 : brassage interchromosomique préparé en métaphase I (les paires se placent de part et d'autre du plan
  équatorial, dans une position aléatoire) et effectué en anaphase I (les homologues se séparent) ; 2 possibilités
  par paire, 23 paires : 2 puissance 23, « environ 8 millions » de gamètes (2^23 = 8 388 608, d'où « plus de
  8 millions »).
- Idée 4 : la fécondation réunit deux gamètes au hasard et rétablit la diploïdie (n + n → 2n) ; « environ 8 millions
  multipliés par 8 millions, soit de l'ordre de 70 000 milliards de zygotes différents possibles pour un seul
  couple » ; les deux brassages et la fécondation se cumulent.
- Idée 5 : « le piège classique » du cours : intra = une seule paire, prophase I ; inter = paires différentes,
  métaphase I puis anaphase I ; « ils ne s'excluent pas, ils se cumulent à chaque méiose ».
Schémas : 2n = 4 (deux paires) pour la lisibilité, signalé à l'écran ; chromosomes à deux chromatides avant la
méiose II, à une chromatide dans les gamètes.
Écartés (faute de place) : lois de Mendel, test-cross, gènes liés et pourcentages de recombinés, Sturtevant,
accidents de la méiose (unité 2 suite).
"""
CODE = "meiose60"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"60": "soixante", "5": "cinq", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "8": "huit",
                 "46": "quarante-six", "23": "vingt-trois", "70": "soixante-dix", "000": "mille",
                 "2n": "deux n", "I": "un", "crossing-over": "crossinng-ôveur"}
PASSAGES = [
    ("s1", "La méiose en 60 secondes. 5 idées pour le bac.", 0.3),
    ("s2", "Idée 1 : une cellule à 46 chromosomes, notée 2n, se divise deux fois de suite.", 0.15),
    ("s3", "Résultat : 4 gamètes à 23 chromosomes, notés n. Le nombre est divisé par deux.", 0.3),
    ("s4", "Idée 2 : en prophase I, les chromosomes homologues s'apparient, en blocs de 4 chromatides.", 0.15),
    ("s5", "Deux chromatides non sœurs se croisent en un chiasma, se cassent et échangent leurs morceaux.", 0.2),
    ("s6", "C'est le crossing-over : le brassage intrachromosomique. De nouvelles combinaisons d'allèles sur un même chromosome.", 0.3),
    ("s7", "Idée 3 : en métaphase I, les paires se placent au hasard autour de l'équateur.", 0.15),
    ("s8", "En anaphase I, les homologues se séparent : c'est le brassage interchromosomique.", 0.2),
    ("s9", "2 possibilités par paire, 23 paires : 2 puissance 23. Plus de 8 millions de gamètes différents !", 0.3),
    ("s10", "Idée 4 : la fécondation réunit deux gamètes au hasard. 23 plus 23 : 46.", 0.15),
    ("s11", "8 millions fois 8 millions : de l'ordre de 70 000 milliards de combinaisons par couple.", 0.3),
    ("s12", "Idée 5 : le piège. Ne confonds pas les deux brassages.", 0.15),
    ("s13", "Intra : dans une même paire, en prophase I. Inter : entre paires différentes, en anaphase I.", 0.25),
    ("s14", "Et ils se cumulent, à chaque méiose.", 0.3),
    ("s15", "Toute la vidéo du chapitre 1 est sur Révisions Animées.", 0.3),
    ("s16", "Alors : combien d'idées tu connaissais déjà ?", 0.0),
]
