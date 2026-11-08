"""Short « Pourquoi le krach de 1929 devient-il une crise mondiale ? » (histoire, chapitre 1) : format 2, question type bac.

Faits : uniquement le cours de la chaîne, chapitre 1 d'histoire (dnl/index.html, chapitre H1, frise et idées « La crise
se propage par… ») et l'épisode d'épreuve de l'édition française (outils/serie-dnl/h1f_5.py, scène « explain » :
« Pourquoi le krach de Wall Street de 1929 devient-il une crise mondiale ? », sujet écrit pour la vidéo, trois canaux) :
- le piège : on ne demande pas de raconter le krach mais d'expliquer (h1f_5, ouverture et méthode « expliquer ») ;
- canal 1, le rappel des prêts américains : plan Dawes de 1924, 800 millions de marks prêtés à l'Allemagne ; prêts
  rappelés après octobre 1929 ; la Creditanstalt, plus grande banque d'Autriche, fait faillite en mai 1931 ;
- canal 2, l'étalon-or : pour défendre le dollar, la Réserve fédérale relève ses taux et l'or quitte les autres pays ;
  le Royaume-Uni sort de l'étalon-or en septembre 1931 ;
- canal 3, le protectionnisme : le 17 juin 1930, Hoover signe le tarif Smoot-Hawley ; le Canada a riposté (mai 1930) ;
  le commerce mondial perd environ deux tiers de sa valeur entre 1929 et 1934 ;
- méthode : chaque argument s'appuie sur un exemple précis, une date, un chiffre, un nom ; la conclusion répond.
Aucune mention de la DNL, de la BFI ni du professeur. Lien : série « La crise de 1929 » (édition française H1).
Écarté faute de place : le détail du circuit des réparations et des dettes de guerre, la faillite des banques allemandes
(juillet 1931), l'Import Duties Act (1932) et les quotas français (1931).
"""
CODE = "bac1929"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 70           # format 2 (question type bac) : durée visée 70 s
PRONONCIATION = {"1929": "mille neuf cent vingt-neuf", "60": "soixante", "1924": "mille neuf cent vingt-quatre",
                 "800": "huit cents", "1931": "mille neuf cent trente et un", "17": "dix-sept",
                 "1930": "mille neuf cent trente", "1934": "mille neuf cent trente-quatre",
                 "Dawes": "Dôze", "Creditanstalt": "Crédit-anne-chtalt", "Smoot-Hawley": "Smoute-Hô-lé", "Hoover": "Houveur"}
PASSAGES = [
    ("s1", "Pourquoi le krach de 1929 devient-il une crise mondiale ? Ce genre de sujet tombe au bac. Tu as 60 secondes.", 0.35),
    ("s2", "Le piège ? Raconter le krach.", 0.25),
    ("s3", "On ne te demande pas de raconter, mais d'expliquer.", 0.3),
    ("s4", "Problématique : par quels canaux une crise américaine gagne-t-elle le monde ?", 0.3),
    ("s5", "Réponse : trois canaux. Un argument, un exemple daté.", 0.3),
    ("s6", "Un : le rappel des prêts américains. En 1924, avec le plan Dawes, l'Amérique prête 800 millions de marks à l'Allemagne.", 0.2),
    ("s7", "Après le krach, les prêts sont rappelés. En mai 1931, la Creditanstalt, la plus grande banque d'Autriche, fait faillite.", 0.35),
    ("s8", "Deux : l'étalon-or. Pour défendre le dollar, la Réserve fédérale relève ses taux. L'or quitte les autres pays.", 0.2),
    ("s9", "En septembre 1931, le Royaume-Uni sort de l'étalon-or.", 0.3),
    ("s10", "Trois : le protectionnisme. Le 17 juin 1930, Hoover signe le tarif Smoot-Hawley. Le Canada riposte.", 0.2),
    ("s11", "Résultat : entre 1929 et 1934, le commerce mondial perd environ deux tiers de sa valeur.", 0.4),
    ("s12", "L'erreur à éviter : une liste sans exemples. Chaque argument veut une date, un chiffre, un nom.", 0.3),
    ("s13", "Ta conclusion répond : la crise devient mondiale parce que les économies sont liées. Par le crédit, l'or et le commerce.", 0.3),
    ("s14", "Le cours complet est sur Révisions Animées.", 0.3),
    ("s15", "Alors, pourquoi le krach devient-il mondial ? Maintenant, tu sais.", 0.0),
]
