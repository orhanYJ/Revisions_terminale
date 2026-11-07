"""Short « Deux sœurs disparaissent » (ACL, Dancing at Lughnasa) : la vraie histoire des tantes de Brian Friel.

La pièce (Faber, 1990) : un matin d'août 1936, Agnes et Rose Mundy partent en laissant un mot
(« We are gone for good. This is best for all. Do not try to find us. ») ; « vingt-cinq ans plus tard »,
Michael les retrouve à Londres : Agnes est morte « of exposure », Rose meurt dans « a hospice for the
destitute in Southwark » (prolepse de l'acte II, p. 63 du PDF de la classe ; résumé dans outils/serie-acl/dal_11.py).

Faits réels vérifiés :
- Friel dédie la pièce « to the memory of those five brave Glenties women » : sa mère Chris (née MacLoone, 1896)
  et quatre de ses sœurs, Kate (1882), Maggie dite Peg (1884), Rose (1889) et Agnes dite Aggie (1891).
  B. Mac Suibhne, The Irish Times, 29/03/2023, « Dancing at Lughnasa's origin story: Those five brave Glenties women ».
- Aggie et Rose partent en 1936, après la mort de leur père (fin 1935) ; installées à Pimlico au plus tard en 1939,
  « canteen ladies » ; de 1949 à la mort d'Aggie (1960), « the same decent flat, a place of their own »,
  26 Cambridge Street ; Aggie meurt le 9 mai 1960 d'une infection contractée lors d'une opération (cancer de
  l'œsophage) ; l'année suivante, Rose entre à Newington Lodge, Southwark, « a notorious dumping ground for
  destitute women and children », où elle meurt en 1962 (même article ; détails concordants dans B. Mac Suibhne,
  « A Long Way Down », Dublin Review of Books, 2020 : la famille savait qu'elles étaient à Londres, aucune trace
  de la vie de rue décrite dans la pièce avant 1960, Rose morte le 17 juin 1962).
- Friel, en sortant du National Theatre avec Thomas Kilroy, devant des sans-abri endormis sur le Strand :
  « I had two aunts who, I think, ended up something like that. » (F. Meredith, The Irish Times, 01/09/2015,
  « The dark heart of Dancing at Lughnasa »).
Écartés (incertains) : que Friel ou quelqu'un de la famille les ait « retrouvées » ; l'année 1987 de la promenade ;
la version de Kilroy (Friel partant jeune à Londres à leur recherche).
Lien avec la série « Dancing at Lughnasa » (résumé-analyse en 13 parties, partie 11 : la prolepse de Londres).
"""
CODE = "lughnasa"
TEMPO = 1.1
ACCEL = 1.1
PRONONCIATION = {"1936": "mille neuf cent trente-six", "1960": "mille neuf cent soixante",
                 "1962": "mille neuf cent soixante-deux", "25": "vingt-cinq", "10": "dix",
                 "Agnes": "Agnèsse", "Friel": "Fril", "Brian": "Braïane", "Dancing": "Dancinng",
                 "Lughnasa": "Lounassa", "Glenties": "Glèntchiz", "Southwark": "Sazeuk", "Michael": "Maïkeul",
                 "memory": "mémori", "play": "plé"}
PASSAGES = [
    ("s1", "Un matin de 1936, deux sœurs quittent la maison. Sans prévenir personne.", 0.3),
    ("s2", "Sur la table, un mot : nous partons pour de bon. Ne nous cherchez pas.", 0.3),
    ("s3", "Elles s'appellent Agnes et Rose. Elles tricotent des gants, en Irlande.", 0.15),
    ("s4", "25 ans plus tard, leur neveu Michael les retrouve. À Londres.", 0.2),
    ("s5", "Agnes est morte de froid, dehors. Rose s'éteint dans un hospice pour pauvres.", 0.35),
    ("s6", "Ça, c'est la pièce : Dancing at Lughnasa, de Brian Friel. Mais voilà…", 0.3),
    ("s7", "Agnes et Rose ont vraiment existé.", 0.4),
    ("s8", "Ce sont les tantes de l'auteur. Les sœurs de sa mère, à Glenties.", 0.15),
    ("s9", "Et elles sont vraiment parties pour Londres. En 1936. L'année même de la pièce.", 0.3),
    ("s10", "Un soir, devant des sans-abri endormis, Friel confie : j'avais deux tantes qui, je crois, ont fini comme ça.", 0.3),
    ("s11", "Je crois. Un historien a fouillé les archives.", 0.2),
    ("s12", "À Londres, elles travaillent dans des cantines. Pendant plus de 10 ans, elles ont un appartement à elles.", 0.2),
    ("s13", "Aucune trace de la rue, ni de l'alcool : la pièce a noirci leur vie.", 0.3),
    ("s14", "Mais en 1960, Agnes meurt après une opération. Rose reste seule.", 0.35),
    ("s15", "Elle meurt en 1962 dans un foyer pour femmes sans ressources. À Southwark. Comme dans la pièce.", 0.35),
    ("s16", "Alors, Michael se souvient… ou il invente ? La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Un matin de 1936, deux sœurs quittent la maison…", 0.0),
]
