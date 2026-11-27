"""Short « HLP : qui a dit ça ? » (format 5, quiz à trois choix) : quatre citations célèbres du programme de spécialité
HLP de Terminale (« La recherche de soi » et « L'humanité en question »), trois auteurs chaque fois.

Matière sans cours sur la chaîne : faits vérifiés le 27/11/2026 sur les sources ci-dessous ; seuls Pascal et Arendt
sont expliqués dans les séries philo de la chaîne (d'où la fin honnête).
- Montaigne, « Je suis moi-même la matière de mon livre » : Essais, « Au lecteur », daté du 1er mars 1580 (Wikisource,
  édition de 1580 : « ie suis moy-mesmes la matiere de mon liure ») ; même préface : « c'est moy que je peins ».
  Programme : la recherche de soi.
- Pascal, « Le moi est haïssable » : Pensées (publication posthume, 1670), fragment 455 éd. Brunschvicg (494 éd. Sellier ;
  article HAL halshs-01804834) ; « Le sot projet qu'il a de se peindre ! » (contre Montaigne) : fragment 644 éd. Sellier
  (article de l'université Bordeaux-Montaigne, « Usages critiques de Montaigne »). Pascal est dans la série « La
  conscience » (épisode 5).
- Rimbaud, « Je est un autre » : lettre à Georges Izambard du 13 mai 1871 et lettre à Paul Demeny du 15 mai 1871
  (« lettres du voyant »), où « le Poète se fait voyant » ; Rimbaud est né le 20 octobre 1854 : il a 16 ans.
  Programme : les métamorphoses du moi.
- Arendt, « la banalité du mal » : Eichmann à Jérusalem. Rapport sur la banalité du mal (articles du New Yorker puis livre,
  1963) ; procès d'Adolf Eichmann à Jérusalem, avril-août 1961 (NEH, « The Trial of Hannah Arendt ») ; Eichmann,
  organisateur de la déportation des Juifs d'Europe, n'est pas un monstre mais un homme qui « ne pense pas » : série
  « Le devoir », épisode 5 (« La banalité du mal, c'est obéir sans penser »). Programme : histoire et violence.
Citations : courtes ; « la banalité du mal » (œuvre sous droits) en trois mots.
Distracteurs : Rousseau et Proust (autres écritures de soi), Montaigne et Descartes, Baudelaire et Verlaine (même
génération de poètes), Kant (qui parle de « mal radical », La Religion dans les limites de la simple raison, 1793 : le piège) et Sartre. Dates de vie : dates usuelles.
Écartés : « Que sais-je ? » (pas une phrase à attribuer) ; « Longtemps, je me suis couché de bonne heure » (Proust est
dans le short devinehlp) ; le numéro de fragment dans la voix (les éditions divergent) ; « Si c'est un homme » de Primo
Levi (titre plutôt que citation, et pas de portrait libre de droits).
"""
CODE = "quidithlp"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"4": "quatre", "1": "un", "2": "deux", "3": "trois", "16": "seize", "HLP": "ache-èle-pé",
                 "1580": "quinze cent quatre-vingts", "1670": "seize cent soixante-dix",
                 "1871": "mille huit cent soixante et onze", "1963": "mille neuf cent soixante-trois",
                 "Arendt": "Arènnte", "Eichmann": "Aïkmane"}
PASSAGES = [
    ("h1", "HLP : 4 citations. Combien tu en reconnais ?", 0.3),
    ("h2", "Pour chacune, trois auteurs. Un seul l'a écrite. Attention aux pièges !", 0.35),
    ("q1", "Citation 1 : « Je suis moi-même la matière de mon livre. » Rousseau, Montaigne… ou Proust ?", 2.1),
    ("r1a", "Réponse : Montaigne !", 0.15),
    ("r1b", "Les Essais, 1580. Son projet : se peindre lui-même, tel qu'il est. Deux siècles avant les Confessions de Rousseau !", 0.4),
    ("q2", "Citation 2 : « Le moi est haïssable. » Montaigne, Pascal… ou Descartes ?", 2.1),
    ("r2a", "Réponse : Pascal !", 0.15),
    ("r2b", "Les Pensées, 1670. Et il se moque de Montaigne : quel sot projet, de se peindre !", 0.4),
    ("q3", "Citation 3 : « Je est un autre. » Baudelaire, Rimbaud… ou Verlaine ?", 2.1),
    ("r3a", "Réponse : Rimbaud !", 0.15),
    ("r3b", "Une lettre de mai 1871. Il a 16 ans, et pour lui, le poète doit se faire voyant.", 0.4),
    ("q4", "Dernière citation : « La banalité du mal. » Kant, Arendt… ou Sartre ?", 2.1),
    ("r4a", "Réponse : Hannah Arendt ! Le piège, c'était Kant et son mal radical.", 0.3),
    ("r4b", "Eichmann à Jérusalem, 1963. Au procès d'un organisateur de la Shoah, elle ne voit pas un monstre… "
            "mais un homme qui ne pense pas.", 0.4),
    ("o1", "Alors, ton score ? Dis-le en commentaire.", 0.3),
    ("o2", "Pascal et Arendt sont expliqués dans les séries philo de Révisions Animées.", 0.3),
    ("o3", "Et toi… tu en as reconnu combien ?", 0.0),
]
