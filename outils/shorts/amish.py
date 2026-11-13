"""Short « Un seul couple » (SVT, chapitre 3 « L'évolution du génome au sein des populations ») : l'effet fondateur
chez les Amish de Pennsylvanie et le syndrome d'Ellis-van Creveld, raconté à la deuxième personne.

Faits du cours (svt/index.html, page t3b, « C. L'effet fondateur », étude de cas 1 « les Amish et les Huttérites » ;
script outils/serie-svt/svt_ch3.py, scène « amish ») :
- définition : une petite sous-population se sépare d'une population initiale, par exemple lors d'une migration ;
  elle n'emporte qu'un échantillon non représentatif, tiré au hasard, des allèles de la population mère ; l'écart est
  d'autant plus grand que la population fondatrice est petite, et la dérive génétique s'y ajoute ensuite ;
- s'y ajoute le plus souvent une reproduction non aléatoire : les membres d'une petite communauté isolée se
  reproduisent entre eux ; les Amish sont une communauté d'origine européenne installée en Amérique du Nord, fondée
  par un petit nombre d'immigrants, qui vit isolée et se marie en son sein ;
- dans la population amish de Pennsylvanie, le syndrome d'Ellis-van Creveld (une forme de nanisme accompagnée de
  doigts surnuméraires) est relativement fréquent : fréquence de l'allèle q = 0,07, alors que la maladie est
  exceptionnelle dans le reste du monde ; dans toutes les familles amish étudiées, la mutation est la même, et il a
  pu être démontré que toutes ces familles descendaient d'un même couple d'immigrants ;
- le tableau « dérive ou sélection » du cours range l'effet fondateur avec la dérive génétique (cause : le hasard).

Faits hors cours, vérifiés :
- Comté de Lancaster (Pennsylvanie), XVIIIe siècle, couple fondateur : D. S. Weiner et al., « Orthopaedic
  manifestations of chondroectodermal dysplasia: the Ellis-van Creveld syndrome », Journal of Children's
  Orthopaedics, 2013, 7 (6), p. 465-476 (la généalogie remonte à « Samuel King et sa femme, émigrés d'Europe en
  1744 » ; la plus forte concentration de malades d'Amérique du Nord est chez les Amish de l'est de la Pennsylvanie,
  surtout le comté de Lancaster ; polydactylie postaxiale des mains) ; étude d'origine : V. A. McKusick et al.,
  « Dwarfism in the Amish. I. The Ellis-van Creveld syndrome », Bulletin of the Johns Hopkins Hospital, 1964, 115,
  p. 306-336 (le syndrome y était aussi appelé « nanisme à six doigts »).
- Hérédité autosomique récessive (il faut deux exemplaires de l'allèle muté) ; ailleurs dans le monde,
  1 naissance sur 60 000 à 200 000 (MedlinePlus Genetics, « Ellis-van Creveld syndrome », National Library of
  Medicine) : le short dit « à peine 1 naissance sur 60 000 ».

Écartés : le nom du fondateur et l'année exacte (1742, 1744 ou 1774 selon les sources : le short dit « XVIIIe
siècle ») ; lequel des deux membres du couple portait l'allèle (non établi : « l'un de vous deux ») ; la fréquence
des malades chez les Amish (« 1 sur 200 » selon certaines sources, non retrouvé dans une source primaire) et des
porteurs (12 à 13 %) ; le gène (EVC, chromosome 4) ; les Huttérites et le tableau des groupes sanguins (trop long).
Ton : respectueux, aucune « bizarrerie » ; la communauté n'est montrée que par la photo d'un buggy, sans visage.
"""
CODE = "amish"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"XVIIIe": "dix-huitième", "Amish": "Amiches", "amish": "amiche", "Lancaster": "Lannkasteur",
                 "Ellis-van": "Élisse-vane", "Creveld": "Crévelde", "200": "deux cents", "1": "une",
                 "60": "soixante", "000": "mille", "7": "sept"}
PASSAGES = [
    ("s1", "Comment un seul couple peut-il marquer les gènes de toute une communauté ?", 0.3),
    ("s2", "Pendant plus de 200 ans. Sans le savoir.", 0.4),
    ("s3", "XVIIIe siècle. Tu es amish, en couple, et tu quittes l'Europe pour la Pennsylvanie.", 0.15),
    ("s4", "Quelques immigrants fondent une communauté. On vit à l'écart, on se marie au sein du groupe.", 0.2),
    ("s5", "Mais l'un de vous deux porte un secret : un allèle muté, très rare.", 0.25),
    ("s6", "Un seul exemplaire : aucun symptôme.", 0.2),
    ("s7", "Il passe à vos enfants, à vos petits-enfants… en silence.", 0.25),
    ("s8", "Puis, dans une si petite communauté, deux porteurs ont un enfant ensemble.", 0.2),
    ("s9", "Cet enfant reçoit l'allèle deux fois. Et là, il se révèle.", 0.35),
    ("s10", "Le syndrome d'Ellis-van Creveld : une très petite taille, et souvent un sixième doigt.", 0.3),
    ("s11", "Ailleurs dans le monde : à peine 1 naissance sur 60 000.", 0.2),
    ("s12", "Chez les Amish de Pennsylvanie, l'allèle atteint 7 pour cent.", 0.2),
    ("s13", "Toutes les familles touchées ont la même mutation. Elles descendent du même couple.", 0.35),
    ("s14", "Ce n'est pas un mystère : c'est l'effet fondateur.", 0.2),
    ("s15", "Les fondateurs n'emportent qu'un échantillon des allèles, tiré au hasard. Puis la dérive génétique fait le reste.", 0.3),
    ("s16", "Montrez que la dérive génétique peut modifier la diversité d'une population : sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Le hasard ne change rien ? Un seul couple a suffi.", 0.0),
]
