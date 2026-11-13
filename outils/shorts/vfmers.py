"""Short « Vrai ou faux : les océans » (géographie, espaces maritimes), format 4 : cinq affirmations, verdicts tirés du cours.

Toutes les affirmations et explications viennent du thème « espaces maritimes » du site (dnl/index.html, CHAPTERS.G1, G2, G3,
version française des idées) :
1. FAUX — « la plupart des marchandises voyagent en avion » : le commerce maritime porte 80 % du commerce mondial en volume ;
   il domine parce qu'il n'existe aucune alternative pour transporter de grandes quantités sur de longues distances
   (G1, I.1, idée « Le commerce maritime porte 80 % du commerce mondial en volume »). Le corrigé d'un DBQ de G2 (III.2)
   dit 90 % ; le site signale que le chiffre dépend de la source et de la mesure : le short garde 80 % « en volume ».
2. VRAI — le 23 mars 2021, l'Ever Given, porte-conteneurs « plus long que la tour Eiffel n'est haute », se met en travers
   du canal de Suez et le bloque entièrement, paralysant le commerce entre l'Asie et l'Europe ; environ 12 % du commerce
   mondial passe par le canal (G1, II.2, idées « choke points » et « Les canaux »). La durée du blocage (six jours),
   ajoutée hors du cours dans le site, n'est pas dite.
3. FAUX — Internet ne traverse pas les océans par satellite : « Les câbles sous-marins sont le moyen le plus rapide et le
   moins cher de faire traverser l'océan aux données : c'est par eux que fonctionne l'Internet mondial. Ils reposent surtout
   sur le fond » (G1, I.3).
4. FAUX — l'Arctique n'est pas ouvert toute l'année : « Les routes ne sont ouvertes que peu de temps, à la fin de l'été, et
   des brise-glace coûteux doivent ouvrir la voie aux autres navires » (G2, III.1).
5. VRAI — « Grâce à ses outre-mer, la France possède une ZEE d'environ 10,7 millions de km², la deuxième du monde » ;
   (G3, V.2 ; G1, II.1). Le short dit « plus de 10 millions » ; le schéma de la ZEE donne à la Polynésie le plus grand cercle (non dit).
Écartés : les chiffres de Malacca et d'Ormuz (trop nombreux pour une phrase), le câble de 50 000 km de Meta (projet),
le nombre de brise-glace russes, la mer de Chine méridionale (trop long à poser en une affirmation).
"""
CODE = "vfmers"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Ever Given": "Éveur Guivène", "Suez": "Suèze",
                 "5": "cinq", "10": "dix", "80": "quatre-vingts",
                 "2021": "deux mille vingt et un"}
PASSAGES = [
    ("v1", "5 affirmations sur les océans. Combien tu en as justes ?", 0.3),
    ("v2", "Top chrono.", 0.3),
    ("a1", "Première. La plupart des marchandises du monde voyagent en avion. Vrai… ou faux ?", 2.0),
    ("b1", "Faux. La mer porte 80 pour cent du commerce mondial, en volume.", 0.35),
    ("a2", "Deuxième. En 2021, un seul navire a bloqué le canal de Suez. Vrai… ou faux ?", 2.0),
    ("b2", "Vrai. L'Ever Given, plus long que la tour Eiffel n'est haute, se met en travers. Commerce Asie-Europe paralysé.", 0.35),
    ("a3", "Troisième. Internet traverse les océans grâce aux satellites. Vrai… ou faux ?", 2.0),
    ("b3", "Faux. Il passe par des câbles posés au fond de la mer. C'est le moyen le plus rapide, et le moins cher.", 0.35),
    ("a4", "Quatrième. Avec le réchauffement, l'Arctique est ouvert aux navires toute l'année. Vrai… ou faux ?", 2.0),
    ("b4", "Faux. Ses routes ne s'ouvrent que peu de temps, à la fin de l'été. Et derrière des brise-glace.", 0.35),
    ("a5", "Dernière. La France a le deuxième plus grand espace maritime du monde. Vrai… ou faux ?", 2.0),
    ("b5", "Vrai. Grâce à ses outre-mer, sa zone économique exclusive dépasse 10 millions de kilomètres carrés.", 0.35),
    ("e1", "Alors, ton score ? Dis-le en commentaire.", 0.3),
    ("e2", "Le cours complet est sur Révisions Animées.", 0.0),
]
