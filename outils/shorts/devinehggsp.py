"""Short « HGGSP : devine qui c'est » (format « devine », le spectateur joue) : trois personnages du programme de
spécialité HGGSP de Terminale, trois indices du plus dur au plus facile, un portrait pixellisé qui se précise,
puis la révélation avec le thème du programme concerné.

La chaîne n'a pas de cours d'HGGSP : faits tirés du programme officiel de Terminale (BO spécial n° 8 du 25 juillet 2019 ;
intitulés relus sur la présentation du programme, sherpas.com/blog/programme-hggsp-terminale-generale) et de sources
sérieuses vérifiées le 27/11/2026.
Programme :
- thème 1 « De nouveaux espaces de conquête », axe 1 : « la course à l'espace des années 1950 à l'arrivée de nouveaux acteurs » ;
- thème 2 « Faire la guerre, faire la paix », axe 1 : « La guerre, “continuation de la politique par d'autres moyens”
  (Clausewitz) » et « Le modèle de Clausewitz à l'épreuve des “guerres irrégulières” : d'Al Qaïda à Daech » ;
- thème 6 « L'enjeu de la connaissance », axe 1 : recherche et échanges des scientifiques sur la radioactivité, de 1896
  aux années 1950.
Youri Gagarine (ESA, « The flight of Vostok 1 » ; Planetary Society, « Vostok 1 » ; Guinness World Records, 2015 et 2026) :
  vol de Vostok 1 le 12 avril 1961, un tour de la Terre en 108 minutes, 27 ans ; au décollage, « Poyekhali ! »
  (« On y va ! », traduction de l'ESA) ; avant sa sélection, pilote sur MiG-15 (avion de chasse) à la base de Luostari
  (Wikipédia, ESA « Yuri Gagarin »).
Carl von Clausewitz (Britannica ; Wikipédia « On War » et « Carl von Clausewitz ») : officier prussien (1780-1831),
  combat Napoléon (Iéna 1806, campagne de Russie 1812 au service du tsar, 1813-1815) ; « De la guerre » (Vom Kriege),
  inachevé, publié après sa mort, en 1832, par sa veuve Marie von Brühl.
Marie Curie (nobelprize.org, questions et réponses 1903 et 1911) : née à Varsovie ; annonce en 1898 avec Pierre Curie
  le polonium, nommé d'après la Pologne, puis le radium ; Nobel de physique 1903, de chimie 1911 : seule personne
  récompensée dans deux sciences différentes.
Écartés : Valentina Terechkova (une seule manche sur l'espace) ; « 6 300 pages » ou tout chiffre non vérifié ;
le détail des batailles de Clausewitz (Waterloo) dans la voix ; les causes de la mort de Gagarine et de Marie Curie.
"""
CODE = "devinehggsp"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "6": "six", "12": "douze",
                 "108": "cent huit", "1961": "mille neuf cent soixante et un",
                 "HGGSP": "ache gé gé èsse pé", "Clausewitz": "Klaozevitz", "Youri": "Iouri"}
PASSAGES = [
    ("d1", "HGGSP : devine qui c'est. 3 personnages du programme.", 0.25),
    ("d2", "3 indices, du plus dur au plus facile.", 0.25),
    ("d3", "Manche 1. Indice 1 : il pilotait des avions de chasse.", 0.25),
    ("d4", "Indice 2 : au décollage, il crie : on y va !", 0.25),
    ("d5", "Indice 3 : en 1961, premier homme dans l'espace. Trois, deux, un.", 1.0),
    ("d6", "C'est Youri Gagarine ! Un tour de la Terre en 108 minutes.", 0.25),
    ("d7", "Thème 1 : la course à l'espace, en pleine guerre froide.", 0.25),
    ("d8", "Manche 2. Indice 1 : son livre majeur paraît après sa mort.", 0.25),
    ("d9", "Indice 2 : officier prussien, il combat Napoléon.", 0.25),
    ("d10", "Indice 3 : la guerre, continuation de la politique par d'autres moyens. Trois, deux, un.", 1.0),
    ("d11", "C'est Carl von Clausewitz ! Son livre : De la guerre.", 0.25),
    ("d12", "Thème 2 : faire la guerre, faire la paix.", 0.25),
    ("d13", "Dernière manche. Indice 1 : elle donne à un élément le nom de son pays natal.", 0.25),
    ("d14", "Indice 2 : elle reçoit 2 prix Nobel, dans 2 sciences différentes.", 0.25),
    ("d15", "Indice 3 : avec son mari Pierre, elle découvre le radium. Trois, deux, un.", 1.0),
    ("d16", "C'est Marie Curie ! Née à Varsovie, elle baptise le polonium pour la Pologne.", 0.25),
    ("d17", "Thème 6 : l'enjeu de la connaissance, avec la radioactivité.", 0.25),
    ("d18", "Combien tu en as trouvés ? Dis-le en commentaire.", 0.25),
    ("d19", "Plus de défis sur Révisions Animées.", 0.0),
]
