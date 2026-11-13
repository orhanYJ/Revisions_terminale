"""Short « Qui a dit ça ? » (philo), format 5 : quatre citations célèbres à attribuer, trois auteurs chaque fois.

Sources : uniquement les séries philo de la chaîne (citations déjà vérifiées dans leurs épisodes), contrôlées une
seconde fois mot pour mot le 13/11/2026 :
- Sartre, « L'homme est condamné à être libre » : liberte_2.py, scène « sartre » (L'existentialisme est un humanisme,
  1946 : conférence du 29 octobre 1945, publiée en 1946) ; « Même ne pas choisir, c'est encore choisir » : même
  scène (formule du narrateur). La formule « condamné à être libre » figure aussi dans L'Être et le Néant (1943) ;
  la série et ce short citent le texte de 1946.
- Kant, « Le bonheur est un idéal, non de la raison, mais de l'imagination » : bonheur_1.py, scène « ideal »
  (Fondements de la métaphysique des mœurs, section II, 1785, trad. Delbos) ; « tout homme veut être heureux, mais
  personne ne sait dire ce qu'il veut » : même scène (« retenir »).
- Pascal, « L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant » :
  conscience_5.py, scène « pascal » (Pensées, fr. 347 éd. Brunschvicg ; publiées en 1670, après sa mort) ; « quand
  l'univers l'écraserait […] parce qu'il sait qu'il meurt » : même scène (résumé dans la voix).
- Rousseau, « L'homme est né libre, et partout il est dans les fers » : liberte_5.py, scène « rousseau » (Du contrat
  social, I, 1, 1762 ; vérifié sur Wikisource, édition de 1762 : « L'homme est né libre, & par-tout il est dans les
  fers ») ; « trouver une société qui ne soit pas une prison » : même scène (formule du narrateur).
Distracteurs : même notion ou même époque (liberté : Descartes, Spinoza ; bonheur : Épicure, Aristote ; conscience :
Descartes, Montaigne ; politique : Hobbes, Locke), tous présents dans les séries. Dates de vie affichées sous les noms :
dates usuelles.
Écartés : « L'homme est un loup pour l'homme » (formule de Plaute reprise dans la dédicace du De Cive, souvent
attribuée à tort à Hobbes : trop discutable pour un quiz) ; « Je pense, donc je suis » (trop facile).
"""
CODE = "quidit"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"4": "quatre", "1": "un", "2": "deux", "3": "trois",
                 "1946": "mille neuf cent quarante-six", "1785": "dix-sept cent quatre-vingt-cinq",
                 "1670": "seize cent soixante-dix", "1762": "dix-sept cent soixante-deux",
                 "Hobbes": "Obbse", "Locke": "Lok"}
PASSAGES = [
    ("h1", "4 citations. Combien tu en reconnais ?", 0.3),
    ("h2", "Pour chacune, trois auteurs. Un seul l'a écrite.", 0.35),
    ("q1", "Citation 1 : « L'homme est condamné à être libre. » Descartes, Spinoza… ou Sartre ?", 2.1),
    ("r1a", "Réponse : Sartre !", 0.15),
    ("r1b", "L'existentialisme est un humanisme, 1946. Même ne pas choisir, c'est encore choisir.", 0.4),
    ("q2", "Citation 2 : « Le bonheur est un idéal, non de la raison, mais de l'imagination. » Épicure, Kant… ou Aristote ?", 2.1),
    ("r2a", "Réponse : Kant !", 0.15),
    ("r2b", "Fondements de la métaphysique des mœurs, 1785. Tout le monde veut être heureux… mais personne ne sait dire ce qu'il veut.", 0.4),
    ("q3", "Citation 3 : « L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant. » Pascal, Descartes… ou Montaigne ?", 2.1),
    ("r3a", "Réponse : Pascal !", 0.15),
    ("r3b", "Les Pensées, publiées en 1670. L'univers peut l'écraser, mais l'homme, lui, sait qu'il meurt.", 0.4),
    ("q4", "Dernière citation : « L'homme est né libre, et partout il est dans les fers. » Hobbes, Rousseau… ou Locke ?", 2.1),
    ("r4a", "Réponse : Rousseau !", 0.15),
    ("r4b", "Du contrat social, 1762. Sa question : quelle société ne serait pas une prison ?", 0.4),
    ("o1", "Alors, ton score ? Dis-le en commentaire.", 0.3),
    ("o2", "Les 4 auteurs sont expliqués en détail dans les séries de Révisions Animées.", 0.3),
    ("o3", "Et toi… tu en as reconnu combien ?", 0.0),
]
