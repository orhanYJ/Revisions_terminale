"""Short « En 1993, elle a écrit 2024 » (ACL oral, BFI) : Parable of the Sower d'Octavia E. Butler, raconté à la
deuxième personne, puis le destin de l'autrice.

Faits vérifiés :
- Roman publié en 1993 ; il s'ouvre le 20 juillet 2024, jour des 15 ans de Lauren ; Californie du Sud, Robledo,
  communautés murées (NPR, « Sci-Fi Writer Octavia Butler Offer Warnings And Hope In Her Work », 24/02/2021 ;
  Grist, « Octavia Butler's 1993 Parable of the Sower predicted climate reality » ; site acl-oral-butler, ch. 1).
- L'eau coûte plusieurs fois le prix de l'essence ; incendies routiniers, Los Angeles qui brûle ; la drogue « pyro »
  rend le spectacle des flammes irrésistible ; hyperempathie (Lauren ressent la douleur qu'elle voit) ; en 2027,
  un camion volé enfonce le portail, visages peints, le quartier brûle, fuite vers le nord ; Earthseed,
  « God is Change » (texte du roman, résumé chapitre par chapitre sur le site acl-oral-butler).
- « All I did was look around at the problems we're neglecting now and give them about 30 years to grow into
  full-fledged disasters » (Butler, Essence, mai 2000, cité par Grist) : paraphrasé, pas cité.
- Note de Butler « I shall be a bestselling writer… So be it! See to it! » (archives Butler, Huntington Library ;
  HuffPost 2017, Wellcome Collection) : la date varie selon les sources (1988 ou fin des années 1970), donc non dite.
- Morte le 24 février 2006 (MacArthur Foundation) ; jamais sur la liste du New York Times de son vivant ; le roman y
  entre en septembre 2020 (n° 14, poche) (Grist ; Syfy ; Fortune).
- Première autrice de science-fiction à recevoir la bourse MacArthur, 1995 (MacArthur Foundation ; NPR) : à l'écran.
- « Make America Great Again » : dans la suite, Parable of the Talents (1998), et déjà « Let's make America great
  again » chez Reagan en 1980 : écarté (ni dans ce roman, ni une invention de Butler).
"""
CODE = "butler"
TEMPO = 1.1
ACCEL = 1.1
PRONONCIATION = {"Butler": "Beutleur", "Lauren": "Lorène", "God is Change": "Gode iz Tchéïndje",
                 "New York Times": "Niou York Taïmz", "ACL": "a cé elle", "BFI": "bé èf i",
                 "1993": "mille neuf cent quatre-vingt-treize", "2024": "deux mille vingt-quatre",
                 "2006": "deux mille six", "2020": "deux mille vingt", "20": "vingt", "15": "quinze",
                 "30": "trente", "14": "quatorze"}
PASSAGES = [
    ("s1", "En 1993, une femme écrit un roman qui se passe en 2024.", 0.35),
    ("s2", "Et ce qu'elle imagine… tu vas le reconnaître.", 0.4),
    ("s3", "20 juillet 2024. Tu t'appelles Lauren, tu as 15 ans. Tu vis en Californie, derrière un mur.", 0.2),
    ("s4", "Dehors, l'eau coûte plus cher que l'essence. Les incendies ne s'arrêtent plus.", 0.2),
    ("s5", "Une nouvelle drogue se répand : elle donne envie de mettre le feu.", 0.3),
    ("s6", "Toi, tu caches un secret : quand quelqu'un souffre devant toi… tu ressens sa douleur.", 0.3),
    ("s7", "Trois ans plus tard. Une nuit, un camion enfonce le portail.", 0.15),
    ("s8", "Des visages peints. Des flammes. Ton quartier brûle.", 0.75),
    ("s9", "Tu t'enfuis vers le nord, à pied, avec ton journal.", 0.2),
    ("s10", "Dans ce journal, tu inventes une religion : God is Change. Dieu est changement.", 0.35),
    ("s11", "Le plus fou ? Butler n'a rien deviné. Elle a regardé les problèmes qu'on néglige… et leur a laissé 30 ans.", 0.25),
    ("s12", "Sécheresse, incendies, quartiers fermés : tout était déjà là.", 0.35),
    ("s13", "Et son destin à elle ? Dans un carnet, elle avait écrit : je serai une autrice de best-sellers.", 0.3),
    ("s14", "Elle meurt en 2006. Jamais dans la liste du New York Times.", 0.35),
    ("s15", "En 2020, 14 ans après sa mort, son roman y entre enfin.", 0.4),
    ("s16", "Il est au programme de l'ACL oral, en BFI. Pourquoi nous parle-t-il autant ? La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Et tout ça… une femme l'avait écrit.", 0.0),
]
