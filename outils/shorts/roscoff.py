"""Short « Il a arrêté de manger » (SVT, chapitre 4 « Mécanismes de diversité non génétique du vivant ») : le ver de
Roscoff et ses micro-algues, raconté à la deuxième personne.

Faits du cours (svt/index.html, page t4, « B.1 Les associations mutualistes », exemple 1 ; script
outils/serie-svt/svt_ch4.py, scène « roscoff ») :
- Symsagittifera roscoffensis est un minuscule ver plat marin, de 1 à 5 mm, vert pomme à vert foncé : sa couleur vient
  des milliers de micro-algues vertes logées sous son épiderme ;
- jeune, le ver est translucide et ingère une seule fois des micro-algues ; adulte, il devient autotrophe : les algues
  réalisent la photosynthèse à la lumière du soleil et partagent avec lui les nutriments produits ; il n'a plus besoin
  de consommer de matière organique venue de l'extérieur ;
- les micro-algues gagnent un habitat et une stabilité de leur environnement ; le ver gagne leur capacité
  photosynthétique ; « association dont les deux partenaires tirent des bénéfices réciproques : association
  mutualiste » ; « les deux partenaires sont devenus interdépendants : on appelle cela une symbiose » ;
- bilan du chapitre : les caractéristiques de l'hôte sont modifiées sans que son génome ait changé ; la symbiose
  contribue à diversifier le phénotype (la vidéo : « son phénotype a complètement changé ; pourtant, son génome n'a
  pas bougé »).

Faits hors cours, vérifiés :
- X. Bailly et al. (Station biologique de Roscoff, CNRS - Sorbonne Université), « The chimerical and multifaceted
  marine acoel Symsagittifera roscoffensis: from photosymbiosis to brain regeneration », Frontiers in Microbiology,
  2014, 5:498 : les jeunes éclosent sans algues et avalent des algues libres du milieu dans leurs premiers jours
  (transmission strictement horizontale : les algues ne passent pas des parents aux petits) ; les vers restés sans
  algues déclinent et ne survivent pas plus de 20 jours (« l'absence du partenaire algal est invariablement létale ») ;
  adulte d'environ 4 mm, environ 40 000 cellules d'algues ; à marée basse, jusqu'à des millions d'individus se
  rassemblent et forment des tapis sur la plage ; à marée haute, ils se retirent dans le sédiment.
- L'algue est Tetraselmis convolutae ; la photosynthèse des algues est le seul apport nutritif de l'animal (article
  « Symsagittifera roscoffensis », Wikipédia en anglais, qui cite les travaux de Keeble et Gamble et de Bailly).

Écartés : la disparition du tube digestif chez l'adulte (dite par le cours, mais l'article de 2014 décrit un tissu
digestif syncytial ouvert sur la face ventrale ; le short dit seulement « tu arrêtes de manger ») ; le nom de l'algue ;
l'interprétation récente d'un « élevage » d'algues plutôt qu'un mutualisme (débat de spécialistes, hors cours) ;
la taille exacte (le short dit « quelques millimètres »).
"""
CODE = "roscoff"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Roscoff": "Roscoffe", "20": "vingt", "40": "quarante", "000": "mille"}
PASSAGES = [
    ("s1", "Cet animal a arrêté de manger. Et il ne meurt pas de faim.", 0.3),
    ("s2", "Son secret ? Il vit du soleil. Comme une plante.", 0.3),
    ("s3", "Tu es le ver de Roscoff : un ver plat marin de quelques millimètres, en Bretagne.", 0.15),
    ("s4", "Tu viens d'éclore, translucide. Ta mission : avaler des micro-algues vertes. Une seule fois.", 0.25),
    ("s5", "Si tu n'en trouves pas ? Tu ne survis pas plus de 20 jours.", 0.3),
    ("s6", "Tu les trouves. Elles s'installent sous ta peau, et se multiplient.", 0.2),
    ("s7", "Bientôt, environ 40 000 algues. Tu deviens vert.", 0.3),
    ("s8", "Et là, tu arrêtes de manger.", 0.3),
    ("s9", "Les algues font la photosynthèse, et partagent avec toi ce qu'elles fabriquent.", 0.25),
    ("s10", "À marée basse, tu remontes à la surface, au soleil. Avec des millions d'autres.", 0.2),
    ("s11", "La plage se couvre de taches vertes. À marée haute, tu t'enfonces dans le sable.", 0.3),
    ("s12", "Toi, tu gagnes la photosynthèse. Les algues, un abri stable.", 0.2),
    ("s13", "Chacun y gagne : c'est le mutualisme. Vous êtes interdépendants : une symbiose.", 0.3),
    ("s14", "Le plus fou ? Ton génome n'a pas changé. Tout vient de l'association.", 0.3),
    ("s15", "Montrez que des relations entre espèces peuvent diversifier le vivant sans modifier le génome : sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s16", "La prochaine fois que tu as faim… pense à lui. Il a arrêté de manger.", 0.0),
]
