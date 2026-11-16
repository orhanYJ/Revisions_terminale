"""Short « SVT : trouve l'intrus » (SVT, thème 1.A « Génétique et évolution ») : format « le spectateur joue »,
plan `intrus` des formats (15/11/2026), 4 manches.

Faits : uniquement le cours de SVT de la chaîne (svt/index.html et scripts outils/serie-svt/svt_ch1.py à svt_ch4.py) :
- manche 1, chapitre 1 (pages t1u1, t1u2) : la mitose « ne crée aucune diversité : elle conserve » (glossaire « mitose ») ;
  elle produit des cellules identiques, un clone (glossaire « clone » ; Pando, « un clone de 80 000 ans » : toute une
  forêt, un seul individu, troncs génétiquement identiques) ; le crossing-over échange des portions de chromatides entre
  chromosomes homologues, en prophase I ; « chez l'humain, 23 paires donnent 2^23, soit environ 8 millions de gamètes
  génétiquement différents » (8 388 608) ; « la fécondation multiplie encore » la diversité ;
- manche 2, chapitre 2 (page t2) : le transfert horizontal « s'oppose au transfert vertical, héréditaire, des parents vers
  les enfants, par la reproduction » ; transferts horizontaux : transformation (Griffith, 1928, pneumocoques), transgenèse
  naturelle d'Agrobacterium (ADN-T inséré dans une cellule végétale, galle du collet), syncytine (protéine du placenta dont
  le gène est issu d'un rétrovirus) ; les croisements de pois de Mendel (chapitre 1) relèvent du transfert vertical
  (« Tout ce chapitre décrit des transferts verticaux : des gènes transmis des parents aux enfants ») ;
- manche 3, chapitre 3 (page t3b) et rappel de Première (résistance aux antibiotiques, svt_ch2.py) : sélection naturelle
  pour la phalène du bouleau (forme noire moins chassée sur les troncs noircis), pour Culex pipiens (« l'allèle AceR
  existait par mutation, et l'insecticide a trié les porteurs ») et pour les bactéries face à un antibiotique (« Celui-ci
  ne fait que sélectionner ») ; les drosophiles de Buri (1956) illustrent la dérive génétique (le hasard) ;
- manche 4, chapitre 4 (page t4) : « Le phénotype étendu désigne tous les caractères d'un organisme qui se situent hors de
  son corps », exemples du cours : fourreau de la larve de phrygane, tonnelle (nid) du jardinier satiné, toile de
  l'araignée ; le ver de Roscoff doit sa couleur verte aux micro-algues logées sous son épiderme : association mutualiste,
  symbiose (« deux sens du mot symbiose » : le short emploie le sens de la diapositive du ver).
Écartés : le chiffre de 70 000 milliards de zygotes (trop long), la transduction (simple mention dans le cours), le port
de Marseille et les mésanges (manche déjà pleine), le gammare (son comportement fait partie du phénotype étendu du
parasite : ambigu pour un intrus).
"""
CODE = "intrussvt"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"4": "quatre", "1": "un", "2": "deux", "3": "trois", "8": "huit", "SVT": "esse-vé-té",
                 "crossing-over": "crossingue-oveur", "Buri": "Bouri", "Culex": "Culexe", "Mendel": "Mendelle",
                 "syncytine": "sincitine", "Roscoff": "Roscof"}
PASSAGES = [
    ("h1", "Trouve l'intrus : 4 manches de SVT.", 0.15),
    ("h2", "Combien tu en trouves ?", 0.3),
    ("m1a", "Manche 1 : la méiose.", 0.15),
    ("m1b", "Trois créent de la diversité génétique. Un seul n'en crée aucune.", 2.3),
    ("r1", "L'intrus : la mitose ! Elle fait des copies conformes : des clones.", 0.2),
    ("e1", "Le crossing-over, lui, échange des morceaux entre chromosomes homologues.", 0.1),
    ("e1b", "Et chez l'humain, la méiose permet plus de 8 millions de gamètes différents.", 0.3),
    ("m2a", "Manche 2 : les transferts de gènes.", 0.15),
    ("m2b", "Trois sont horizontaux. Un seul est vertical. Trouve-le.", 2.3),
    ("r2", "Les pois de Mendel ! Leurs gènes passent des parents aux descendants.", 0.2),
    ("e2", "Le placenta, lui, doit sa syncytine à un gène venu d'un virus.", 0.3),
    ("m3a", "Manche 3 : les forces évolutives.", 0.15),
    ("m3b", "Trois exemples de sélection naturelle. Un seul est dû au hasard.", 2.3),
    ("r3", "Les drosophiles de Buri ! C'est la dérive génétique : le pur hasard.", 0.2),
    ("e3", "Chez le moustique Culex, les insecticides ont trié les porteurs d'un allèle de résistance.", 0.3),
    ("m4", "Dernière manche, la plus dure ! Trois font partie du phénotype étendu, construit hors du corps.", 0.5),
    ("c4", "Trois, deux, un.", 0.6),
    ("r4", "Le ver de Roscoff ! Ses algues vivent sous sa peau : c'est une symbiose.", 0.25),
    ("f1", "Alors, combien d'intrus trouvés ? Dis-le en commentaire.", 0.15),
    ("f2", "Tout le cours est sur Révisions Animées.", 0.0),
]
