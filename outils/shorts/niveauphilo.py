"""Short « Philo : niveau 1 → 10, à quel niveau tu t'arrêtes ? » (format `niveau`, le spectateur joue).

Six paliers de difficulté croissante (1, 3, 5, 7, 9, 10), une question de cours chacun, un chrono de 2 s de silence,
la réponse et une phrase d'explication. Faits tirés uniquement des séries philo de la chaîne (outils/serie-philo) :
- Niveau 1, « Je pense, donc je suis » : Descartes, Discours de la méthode (1637), partie IV ; le doute méthodique qui
  ne peut atteindre la pensée qui doute : conscience_2.py (en-tête « Citations de Descartes : Discours de la méthode, IV
  (1637) », scène « doute », visuel « tab_dis » 1637).
- Niveau 3, l'homme « animal politique », fait pour vivre dans une cité, et la nature n'a donné qu'à l'homme la parole :
  etat_2.py, scène d'Aristote (« zôon politikon […] elle n'a donné qu'à l'homme la parole »), Politique, I.
- Niveau 5, « l'existence précède l'essence », « l'homme n'est rien d'autre que ce qu'il se fait » : liberte_2.py,
  scène IV « Sartre : l'existence précède l'essence » (L'existentialisme est un humanisme, 1946).
- Niveau 7, seconde topique de Freud (1923) : le ça (réservoir des pulsions), le surmoi (interdits des parents et de la
  société), le moi entre les deux : conscience_3.py, visuel « top2 » et « retenir » de la scène.
- Niveau 9, Kant : « Le bonheur est un idéal, non de la raison, mais de l'imagination » ; « tout homme veut être heureux,
  mais personne ne sait dire ce qu'il veut » : bonheur_1.py, scène « ideal » (Fondements de la métaphysique des mœurs,
  section II, 1785).
- Niveau 10, Weber : l'État « revendique avec succès […] le monopole de la violence physique légitime » ; « la violence
  physique : arrêter, enfermer, contraindre » ; « le monopole : l'État ne partage pas ce droit » : etat_1.py, scène
  « weber » (Le métier et la vocation d'homme politique, conférence de Munich, 28 janvier 1919).
Écartés : « L'homme est un loup pour l'homme » (formule de Plaute, attribution à Hobbes discutable) ; la date de la
conférence de Weber (1919, publiée la même année) laissée hors de la voix pour ne pas surcharger ; « la ciguë » de Socrate
(absente des séries).
"""
CODE = "niveauphilo"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "3": "trois", "5": "cinq", "6": "six", "7": "sept", "9": "neuf", "10": "dix",
                 "1637": "seize cent trente-sept", "Weber": "Wébère", "surmoi": "sur-moi"}
CHRONO = 2.0         # silence après chaque question : le chrono du plan `niveau`
PASSAGES = [
    ("h1", "Philo, niveau 1 à 10. À quel niveau tu t'arrêtes ?", 0.1),
    ("h2", "Réponds avant la fin du chrono !", 0.1),
    ("n1q", "Niveau 1. « Je pense, donc je suis. » Qui a dit ça ?", CHRONO),
    ("n1r", "Descartes, en 1637 ! Il doute de tout, sauf d'une chose : il pense.", 0.1),
    ("n3q", "Niveau 3. Pour Aristote, l'homme est un animal… quoi ?", CHRONO),
    ("n3r", "Politique ! Fait pour vivre en cité : lui seul a la parole.", 0.1),
    ("n5q", "Niveau 5. Pour Sartre, l'existence précède… quoi ?", CHRONO),
    ("n5r", "L'essence ! Pas de nature toute faite : tu n'es que ce que tu te fais.", 0.1),
    ("n7q", "Niveau 7. Freud : le moi est coincé entre deux instances. Lesquelles ?", CHRONO),
    ("n7r", "Le ça et le surmoi ! Les pulsions d'un côté, les interdits de l'autre.", 0.1),
    ("n9q", "Niveau 9. Pour Kant, le bonheur est un idéal… de quoi ?", CHRONO),
    ("n9r", "De l'imagination, pas de la raison ! On veut être heureux… sans savoir dire quoi.", 0.1),
    ("n10q", "Niveau 10, boss final ! Selon Weber, l'État revendique le monopole… de quoi ?", CHRONO),
    ("n10r", "De la violence physique légitime ! Arrêter, enfermer, contraindre : l'État ne partage pas ce droit.", 0.1),
    ("o1", "Dis ton niveau en commentaire !", 0.1),
    ("o2", "Les réponses sont dans les séries philo de Révisions Animées.", 0.1),
    ("o3", "Et toi… tu montes jusqu'au niveau 10 ?", 0.0),
]
