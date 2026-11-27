"""Short « HGGSP : remets dans l'ordre » (format « ordre », le spectateur joue) : trois manches de quatre événements
du programme de spécialité HGGSP de Terminale, montrés mélangés ; les dates sont révélées au verdict.

La chaîne n'a pas de cours d'HGGSP : faits tirés du programme officiel de Terminale (BO spécial n° 8 du 25 juillet 2019 ;
intitulés relus sur sherpas.com/blog/programme-hggsp-terminale-generale) et de sources sérieuses vérifiées le 27/11/2026.
Programme : thème 1 (la course à l'espace des années 1950 à l'arrivée de nouveaux acteurs ; coopérer pour développer la
recherche, l'ISS ; la Chine à la conquête de l'espace) ; thème 2 (faire la paix par les traités : les traités de
Westphalie, 1648 ; faire la paix par la sécurité collective : l'ONU ; le Moyen-Orient : du conflit israélo-arabe au
conflit israélo-palestinien) ; thème 4 (le patrimoine) ; thème 5 (le climat, enjeu des relations internationales :
les accords internationaux).
Manche 1, l'espace :
- Spoutnik 1, premier satellite artificiel, lancé par l'URSS le 4 octobre 1957 (NASA, « Sputnik and the Dawn of the
  Space Age » ; Smithsonian) ; le choc qu'il provoque aux États-Unis (NASA, idem) ;
- Apollo 11 : premiers pas sur la Lune, 20-21 juillet 1969 (NASA) ;
- Zarya, premier module de la Station spatiale internationale, lancé le 20 novembre 1998 (NASA ; ESA) ;
- Yang Liwei, Shenzhou 5, 15 octobre 2003 : la Chine, troisième pays à envoyer un homme dans l'espace par ses propres
  moyens, après l'URSS et les États-Unis (Britannica ; Futura-Sciences).
Manche 2, faire la paix :
- traités de Westphalie, 1648 (publiés le 24 octobre 1648), fin de la guerre de Trente Ans (Britannica ; Hérodote) ;
- traité de Versailles, 28 juin 1919, galerie des Glaces ;
- Charte des Nations unies signée à San Francisco le 26 juin 1945 (un.org ; Larousse) ;
- accords d'Oslo, 13 septembre 1993, Washington ; poignée de main Rabin-Arafat sur la pelouse de la Maison-Blanche
  (Britannica ; History.com).
Manche 3, patrimoine et climat :
- convention du patrimoine mondial adoptée par l'UNESCO le 16 novembre 1972 ; née du succès de la campagne de Nubie :
  les temples d'Abou Simbel découpés en blocs et remontés plus haut, réinaugurés le 22 septembre 1968 (whc.unesco.org,
  « Histoires : Abou Simbel ») ;
- Sommet de la Terre de Rio, juin 1992 (vie-publique.fr) ; protocole de Kyoto, décembre 1997, COP3 (OFEV ;
  vie-publique.fr) ; accord de Paris, 12 décembre 2015, COP21 : contenir la hausse « bien en dessous de 2 °C »
  (vie-publique.fr), adopté par la quasi-totalité des pays.
Écartés : Gagarine (sujet du short devinehggsp) ; le traité de l'espace de 1967 et la convention de Montego Bay (1982),
faute de place ; l'entrée en vigueur de Kyoto (2005) ; les chiffres de pays signataires, qui varient selon les sources.
"""
CODE = "ordrehggsp"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "11": "onze", "12": "douze",
                 "1648": "seize cent quarante-huit", "1919": "mille neuf cent dix-neuf",
                 "1945": "mille neuf cent quarante-cinq", "1957": "mille neuf cent cinquante-sept",
                 "1969": "mille neuf cent soixante-neuf", "1972": "mille neuf cent soixante-douze",
                 "1992": "mille neuf cent quatre-vingt-douze", "1993": "mille neuf cent quatre-vingt-treize",
                 "1997": "mille neuf cent quatre-vingt-dix-sept", "1998": "mille neuf cent quatre-vingt-dix-huit",
                 "2003": "deux mille trois", "2015": "deux mille quinze",
                 "HGGSP": "ache gé gé èsse pé", "ONU": "o-èn-u", "Kyoto": "Kioto", "Westphalie": "Vestfalie",
                 "Apollo": "Apolo", "Arafat": "Arafatte"}
PASSAGES = [
    ("o1", "HGGSP : remets 12 événements dans l'ordre.", 0.25),
    ("o2", "3 manches. Compte tes points.", 0.3),
    ("m1", "Manche 1 : l'espace.", 0.15),
    ("m1b", "Apollo 11. Le premier Chinois dans l'espace. Spoutnik. La Station spatiale internationale.", 1.6),
    ("v1", "Spoutnik en 1957. Apollo en 1969. La station en 1998. La Chine en 2003.", 0.3),
    ("x1", "Spoutnik, premier satellite artificiel : un choc pour les États-Unis.", 0.3),
    ("m2", "Manche 2 : faire la paix.", 0.15),
    ("m2b", "Les accords d'Oslo. La charte de l'ONU. Les traités de Westphalie. Le traité de Versailles. Trois, deux, un.", 0.6),
    ("v2", "Westphalie en 1648. Versailles en 1919. L'ONU en 1945. Oslo en 1993.", 0.3),
    ("x2", "Westphalie met fin à la guerre de Trente Ans.", 0.25),
    ("x2b", "Et en 1993, Rabin et Arafat se serrent la main à la Maison-Blanche.", 0.3),
    ("m3", "Dernière manche : le patrimoine et le climat.", 0.15),
    ("m3b", "L'accord de Paris. Le sommet de la Terre de Rio. La convention du patrimoine mondial. Le protocole de Kyoto.", 1.6),
    ("v3", "Le patrimoine en 1972. Rio en 1992. Kyoto en 1997. Paris en 2015.", 0.3),
    ("x3", "Cette convention naît d'un sauvetage : les temples d'Abou Simbel, découpés en blocs.", 0.25),
    ("x3b", "À Paris, presque tous les pays visent un réchauffement bien en dessous de 2 degrés.", 0.3),
    ("e1", "Combien de manches réussies ? Dis-le en commentaire.", 0.25),
    ("e2", "Plus de défis sur Révisions Animées.", 0.0),
]
