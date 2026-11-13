"""Short « Ce sujet peut tomber au bac » (philo, l'État), format 2 : le plan de « L'État est-il l'ennemi de la
liberté ? » en 60 secondes.

Sources : uniquement la série « L'État » de la chaîne (citations déjà vérifiées dans ses épisodes).
- Sujet, mots du sujet, problématique et plan : etat_6.py, scène « sujet1 » (« Ennemi : le mot est fort. Un obstacle
  gêne ; un ennemi veut ma perte » ; « Est-il son ennemi… ou sa condition ? » ; I. oui, l'État contraint, et il peut
  écraser, Proudhon ; II. mais sans État, il n'y a pas de liberté du tout, Montréal 1969, seize heures sans police,
  Locke, l'État gardien de la vie, de la liberté, des biens ; III. il en est la condition, à condition qu'il soit
  limité, Montesquieu, « le pouvoir arrête le pouvoir » ; la distinction qui dépasse (Rousseau) : liberté naturelle,
  limitée par mes seules forces / liberté civile, garantie par la loi ; « L'État retire la première… pour donner la
  seconde »).
- Proudhon, Idée générale de la Révolution au XIXe siècle, Épilogue (1851) : « Être gouverné, c'est être gardé à vue,
  inspecté, espionné… » (etat_4.py, vérifié sur Wikisource par la série ; début de la phrase seulement).
- Exemple de la partie I : la Roumanie de Ceaușescu, « police secrète, pénuries, culte de sa personne » (etat_4.py,
  ouverture ; etat_6.py le cite dans le « nuage » du sujet).
- Montréal, 7 octobre 1969, grève de la police, seize heures (etat_2.py, ouverture ; etat_6.py et etat_7.py).
- Locke, l'État gardien de la vie, de la liberté et des biens (etat_2.py, etat_6.py, etat_7.py ; résumé, pas une
  citation).
- Montesquieu, De l'esprit des lois, XI, 4 (1748) : « il faut que, par la disposition des choses, le pouvoir arrête le
  pouvoir » (etat_3.py) ; dans la voix, abrégé comme dans etat_6.py, l'incise « par la disposition des choses » omise.
- Watergate (etat_3.py et etat_7.py) : le 24 juillet 1974, la Cour suprême, à l'unanimité, ordonne à Nixon de livrer
  ses enregistrements ; il démissionne le 9 août 1974 (United States v. Nixon, 418 U.S. 683).
- Rousseau, Du contrat social, I, 8 (1762) : la liberté naturelle « qui n'a pour bornes que les forces de
  l'individu » ; la liberté civile, que le texte dit « limitée par la volonté générale », est résumée comme dans la
  série (« garantie par la loi ») : paraphrase.
- L'erreur à ne pas faire : etat_7.py, scène « jourj » (« Le piège : réciter Hobbes contre Marx sans répondre à la
  question. Un auteur est un outil pour penser, pas un argument d'autorité »).
Écartés : Nietzsche (« le plus froid des monstres froids », même partie que Proudhon, faute de place), Weber
(définition de l'État), Hobbes.
"""
CODE = "bacetat"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 70           # format 2 (question de bac) : durée visée en secondes
PRONONCIATION = {"60": "soixante", "1969": "mille neuf cent soixante-neuf", "16": "seize",
                 "1974": "mille neuf cent soixante-quatorze", "Ceaușescu": "Tchaouchesscou", "Proudhon": "Proudon",
                 "Locke": "Lok", "Watergate": "Ouatergueït", "Nixon": "Nixone"}
PASSAGES = [
    ("s1", "Ce sujet peut tomber au bac. Tu as 60 secondes pour le plan.", 0.3),
    ("s2", "L'État est-il l'ennemi de la liberté ?", 0.35),
    ("s3", "Le piège ? Le mot « ennemi ». Un obstacle gêne ; un ennemi veut ta perte.", 0.3),
    ("s4", "Ta problématique : l'État est-il l'ennemi de la liberté… ou sa condition ?", 0.35),
    ("s5", "Première partie : oui. L'État contraint, il peut écraser.", 0.15),
    ("s6", "Proudhon : être gouverné, c'est être gardé à vue, inspecté, espionné.", 0.2),
    ("s7", "Ton exemple : la police secrète de Ceaușescu.", 0.35),
    ("s8", "Deuxième partie : mais sans État, pas de liberté.", 0.15),
    ("s9", "Montréal, 1969 : grève de la police. 16 heures, et la ville bascule.", 0.2),
    ("s10", "Locke : l'État est le gardien de la vie, de la liberté, des biens.", 0.35),
    ("s11", "Troisième partie : l'État, condition de la liberté… s'il est limité.", 0.15),
    ("s12", "Montesquieu : il faut que le pouvoir arrête le pouvoir.", 0.2),
    ("s13", "Le Watergate, 1974 : la Cour suprême oblige Nixon à livrer ses enregistrements. Il démissionne.", 0.3),
    ("s14", "Rousseau distingue : liberté naturelle, limitée par tes forces ; liberté civile, garantie par la loi.", 0.2),
    ("s15", "L'État retire la première… pour te donner la seconde.", 0.35),
    ("s16", "L'erreur à ne pas faire : réciter tes auteurs sans répondre à la question.", 0.2),
    ("s17", "Un auteur est un outil pour penser.", 0.35),
    ("s18", "Le cours complet est sur Révisions Animées.", 0.3),
    ("s19", "Et toi… l'État, ennemi ou condition de ta liberté ?", 0.0),
]
