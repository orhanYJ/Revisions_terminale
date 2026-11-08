"""Short « Ce n'est pas lui qui décide » (SVT, chapitre 4 « Mécanismes de diversité non génétique du vivant ») :
le gammare parasité, raconté à la deuxième personne.

Faits du cours (svt/index.html, page t4, « Les associations parasitaires » et « Le phénotype étendu » ; script
outils/serie-svt/svt_ch4.py, scène « Le parasitisme : le gammare ») :
- les gammares sont de petits crustacés d'eau douce, proies des oiseaux ; un gammare sain reste au fond, à l'abri ;
- certains sont infestés par des parasites qui s'enkystent dans leur corps ; ils sont alors attirés par la lumière,
  remontent à la surface, tournoient frénétiquement et deviennent des proies faciles pour les oiseaux ;
- le parasite vit sous forme de larves chez le gammare et atteint l'état adulte dans l'intestin de l'oiseau (hôte
  définitif), où il se reproduit sexuellement ; l'hôte lui offre un habitat, de la nourriture et un moyen de
  dispersion ;
- les caractéristiques de l'hôte sont modifiées sans que son génome ait changé ; la prise de contrôle d'autres
  organismes (le parasite qui modifie le comportement du gammare) élargit le phénotype de certaines espèces :
  le comportement du gammare fait partie du phénotype étendu du parasite ;
- sujet de rédaction du site (chapitre 4) : « Montrer, à l'aide d'exemples précis, que le phénotype des êtres
  vivants peut se diversifier sans modification de leur génome ».

Faits hors cours, vérifiés :
- « Ver » : le cours ne nomme pas le parasite. Le cycle qu'il décrit (multiplication asexuée chez un premier hôte
  intermédiaire, larves enkystées chez le gammare, adulte dans l'intestin d'un oiseau) est celui du trématode
  (ver plat) Microphallus papillorobustus : escargots Hydrobia, puis gammares, puis oiseaux aquatiques ; les
  métacercaires enkystées dans le cerveau du gammare provoquent phototactisme positif, géotactisme négatif et
  comportement d'évitement aberrant ; les gammares parasités vivent en surface, les sains au fond (A. Arnal et al.,
  « Activity level and aggregation behavior in the crustacean gammarid Gammarus insensibilis parasitized by the
  manipulative trematode Microphallus papillorobustus », Frontiers in Ecology and Evolution, 2015, 3:109 ;
  S. Helluy, « Relations hôtes-parasite du trématode Microphallus papillorobustus (Rankin, 1940). II.
  Modifications du comportement des Gammarus hôtes intermédiaires et localisation des métacercaires », Annales
  de Parasitologie humaine et comparée, 1983, 58, p. 1-17). Ce cas étudié vit en lagune saumâtre (étang de
  Thau) ; le cours dit « crustacés d'eau douce », vrai de la plupart des gammares : le short suit le cours. Dans l'autre cas souvent cité, un acanthocéphale (Polymorphus
  minutus, « ver à tête épineuse »), le gammare remonte aussi en surface et l'hôte définitif est aussi un oiseau
  (canards) ; dans les deux cas, le parasite est un ver : le short dit « un minuscule ver parasite », sans nom.

Écartés : le nom du parasite et le mot « acanthocéphale » (le cycle du cours, avec un premier hôte où le parasite
se multiplie, ne correspond pas aux acanthocéphales, qui n'ont qu'un hôte intermédiaire ; le cours ne nomme pas le
parasite) ; la couleur du gammare parasité (propre aux acanthocéphales, absente du cours) ; le premier hôte (non
nommé par le cours, trop long pour le short) ; la taille du gammare.
"""
CODE = "gammare"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"gammare": "gamare"}
PASSAGES = [
    ("s1", "Ce petit crustacé nage droit vers la mort. Et ce n'est pas lui qui décide.", 0.3),
    ("s2", "Quelqu'un est aux commandes. À l'intérieur de lui.", 0.45),
    ("s3", "Tu es un gammare. Un petit crustacé d'eau douce.", 0.15),
    ("s4", "Ta règle de survie : rester au fond, à l'abri. Là-haut, il y a les oiseaux.", 0.25),
    ("s5", "Un jour, un minuscule ver parasite entre dans ton corps.", 0.2),
    ("s6", "Il s'installe. Il s'enferme dans une coque : un kyste.", 0.3),
    ("s7", "Et là, tout change.", 0.4),
    ("s8", "La lumière t'attire. Tu quittes le fond. Tu remontes… jusqu'à la surface.", 0.2),
    ("s9", "Là-haut, tu tournoies. Frénétiquement.", 0.3),
    ("s10", "Un oiseau passe. Tu es la proie parfaite.", 0.3),
    ("s11", "Coup de bec. Fin de l'histoire ? Non.", 0.45),
    ("s12", "Pour le parasite, c'est la suite du voyage. Dans l'intestin de l'oiseau, il devient adulte et se reproduit.", 0.2),
    ("s13", "Toi, tu étais son habitat, sa nourriture… et son taxi.", 0.35),
    ("s14", "Le plus fou ? Tes gènes n'ont pas changé. C'est ton comportement qui a été piraté.", 0.3),
    ("s15", "Pour les biologistes, ton comportement fait partie du phénotype étendu du parasite.", 0.3),
    ("s16", "Montrez que le phénotype peut se diversifier sans modification du génome : sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s17", "La prochaine fois que tu fonces vers quelque chose… es-tu sûr que c'est toi qui décides ?", 0.0),
]
