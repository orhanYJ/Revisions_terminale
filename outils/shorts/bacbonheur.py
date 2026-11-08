"""Short « Ce sujet peut tomber au bac » (philo, le bonheur), format 2 : le plan de « Faut-il renoncer à ses
désirs pour être heureux ? » en 60 secondes.

Sources : uniquement la série « Le bonheur » de la chaîne (citations déjà vérifiées dans ses épisodes).
- Sujet, mots du sujet, problématique et plan : bonheur_6.py, scène « sujet2 » (« Deux mots portent tout :
  renoncer… et ses » ; « Renoncer : abandonner volontairement. Ce n'est pas être privé, c'est choisir de lâcher » ;
  « Ses désirs : tous ? Ou certains ? Toute la copie se joue sur cette question » ; I. le désir est un manque sans
  fin, les tonneaux percés de Platon ; II. renoncer à tout désir, c'est renoncer à vivre, Calliclès : les pierres
  et les morts seraient les plus heureux, Rousseau : malheur à qui n'a plus rien à désirer ; III. ne pas supprimer
  ses désirs mais les régler, Descartes, troisième maxime ; on ne désire pas « avoir des ailes pour voler comme les
  oiseaux » ; « Le sage n'est pas celui qui ne désire plus rien. C'est celui qui désire ce qui est à sa portée »).
- L'erreur à ne pas faire : bonheur_6.py, scène « sujet3 » (« la troisième partie ne dit jamais « tout dépend ».
  Elle déplace la question, grâce à une distinction ») et bonheur_7.py (méthode).
- Tonneaux percés : bonheur_2.py, scène « callicles » (Gorgias : « L'insatiable a des tonneaux percés : il doit
  verser sans fin » ; « Ce tonneau percé, tu le connais : c'est notre soirée de vendredi. La vidéo suivante, le
  message suivant, la série suivante »).
- Rousseau, Julie ou la Nouvelle Héloïse (1761) : « Malheur à qui n'a plus rien à désirer ! » (bonheur_4.py).
- Descartes, Discours de la méthode, III (1637) : « … à changer mes désirs que l'ordre du monde » (bonheur_6.py) ;
  dans la voix, paraphrase (« mieux vaut changer ses désirs que l'ordre du monde »).
Écartés : Schopenhauer et Tantale (gardés pour la série, faute de temps), Épicure (même partie que Descartes).
"""
CODE = "bacbonheur"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 70           # format 2 (question de bac) : durée visée en secondes
PRONONCIATION = {"60": "soixante", "Calliclès": "Kaliklèsse"}
PASSAGES = [
    ("s1", "Ce sujet peut tomber au bac. Tu as 60 secondes pour le plan.", 0.3),
    ("s2", "Faut-il renoncer à ses désirs pour être heureux ?", 0.35),
    ("s3", "Le piège ? Il tient en deux mots.", 0.2),
    ("s4", "Renoncer : pas être privé, mais choisir de lâcher. Et ses désirs : tous ? Ou certains ?", 0.3),
    ("s5", "Voilà ta problématique : faut-il renoncer à tous ses désirs, ou seulement à certains ?", 0.35),
    ("s6", "Première partie : oui. Le désir est un manque sans fin.", 0.15),
    ("s7", "Platon parle de tonneaux percés : tu verses, tu verses, jamais pleins.", 0.2),
    ("s8", "Ton exemple : toi, ce soir. La vidéo suivante, puis la suivante.", 0.35),
    ("s9", "Deuxième partie : pourtant, sans désir, on ne vit plus.", 0.15),
    ("s10", "Sinon, disait Calliclès, les pierres seraient les plus heureuses.", 0.2),
    ("s11", "Et Rousseau : malheur à qui n'a plus rien à désirer !", 0.35),
    ("s12", "Troisième partie : ne pas supprimer ses désirs, mais les régler.", 0.15),
    ("s13", "Descartes : mieux vaut changer ses désirs que l'ordre du monde.", 0.2),
    ("s14", "Exemple : tu n'as pas d'ailes. Et ça ne te fait pas souffrir.", 0.2),
    ("s15", "Le sage désire encore : mais ce qui est à sa portée.", 0.35),
    ("s16", "L'erreur à ne pas faire : une troisième partie qui dit « ça dépend ».", 0.2),
    ("s17", "Elle doit déplacer la question : supprimer ses désirs, ou les régler.", 0.35),
    ("s18", "Le cours complet est sur Révisions Animées.", 0.3),
    ("s19", "Et toi… tu renoncerais à quoi ?", 0.0),
]
