"""Short « SES : plus ou moins ? » (spécialité SES de Terminale) : format « le spectateur joue », plan `plusmoins`
des formats (15/11/2026), 4 duels de chiffres. La chaîne n'a pas de cours de SES : chiffres officiels, datés et
sourcés, vérifiés le 27/11/2026. Le plan `plusmoins` arrondit à l'unité : la voix dit « environ » ou « près de ».

Sources :
1. Travail (programme : « Quelles mutations du travail et de l'emploi ? », tertiarisation) :
   - 1975 : Insee, Économie et statistique n° 462-463 (2013), V. Hecquet, « Emploi et territoires de 1975 à 2009 » :
     « La part de l'industrie a diminué de moitié, passant de 29 % à 14 % des emplois » (recensements, métropole,
     1975 → 2009) ; « tertiarisation ».
   - 2024 : Insee, « Professions et secteurs d'activité », Emploi, chômage, revenus du travail, édition 2025 (paru le
     26/06/2025) : « En 2024, l'industrie représente 12,6 % des emplois » (enquête Emploi, France).
   Les deux sources ne sont pas la même enquête (recensement contre enquête Emploi) : signalé dans la description.
2. Chômage (programme : « Comment lutter contre le chômage ? ») : Insee, « Évolution du chômage », Emploi, chômage,
   revenus du travail, édition 2026 (paru le 02/07/2026) : taux de chômage de 7,7 % en 2025 ; « À 19,8 % en 2025, le
   taux de chômage des 15-24 ans est largement supérieur à celui des autres classes d'âge. » Le taux de chômage se
   calcule sur les actifs (chômeurs / population active), définition du BIT reprise par l'Insee.
3. Inégalités (programme : « Quels sont les caractéristiques contemporaines et les facteurs de la mobilité
   sociale ? » et regards croisés « justice sociale ») : Insee Focus n° 377 (février 2026), « Écart de salaire entre
   femmes et hommes en 2024 » : secteur privé, revenu salarial moyen des femmes inférieur de 33,7 % en 1995 et de
   21,8 % en 2024 (« Depuis 1995, les inégalités de revenu salarial se sont réduites d'un tiers ») ; « même à temps de
   travail identique, le salaire moyen des femmes est inférieur à celui des hommes, de 14,0 % ».
4. Mondialisation (programme : « Quels sont les fondements du commerce international et de l'internationalisation de
   la production ? ») :
   - 1983 : OMC, International Trade Statistics 2005, tableau II.2 (« World merchandise trade by region and selected
     economy, 1948, 1953, 1963, 1973, 1983, 1993, 2003 and 2004 ») : part de la Chine dans les exportations mondiales
     de marchandises, 1,2 % en 1983.
   - 2024 : OMC, Global Trade Outlook and Statistics (avril 2025), tableau A1 : Chine, 3 577 milliards de dollars,
     14,6 % des exportations mondiales de marchandises, premier exportateur.
Écartés : la part de l'industrie en 1970 (43 % de l'emploi marchand non agricole : autre champ, pas comparable) ;
l'écart de salaire de 1995 en équivalent temps plein (22,1 %, moins parlant) ; un pourcentage de jeunes au chômage
parmi tous les jeunes (non vérifié : le schéma du short reste qualitatif) ; le PIB par habitant (comparaisons en
parité de pouvoir d'achat trop techniques pour un duel).
"""
CODE = "plusmoinsses"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"SES": "esse-eu-esse", "4": "quatre", "1": "un", "8": "huit", "13": "treize", "14": "quatorze",
                 "15": "quinze", "20": "vingt", "22": "vingt-deux", "24": "vingt-quatre", "29": "vingt-neuf",
                 "34": "trente-quatre", "1975": "mille neuf cent soixante-quinze", "1983": "mille neuf cent quatre-vingt-trois",
                 "1995": "mille neuf cent quatre-vingt-quinze", "2024": "deux mille vingt-quatre", "2025": "deux mille vingt-cinq"}
PASSAGES = [
    ("h1", "SES : plus ou moins ? 4 chiffres surprenants.", 0.15),
    ("h2", "Compte tes bonnes réponses.", 0.3),
    ("d1a", "Duel 1 : le travail.", 0.15),
    ("d1b", "En 1975, l'industrie fait 29 pour cent des emplois en France.", 0.1),
    ("d1c", "Et en 2024 : plus ou moins ?", 2.2),
    ("r1", "Moins : environ 13 pour cent ! Les emplois passent aux services : c'est la tertiarisation.", 0.3),
    ("d2a", "Duel 2 : le chômage.", 0.15),
    ("d2b", "En 2025, le taux de chômage en France est de près de 8 pour cent.", 0.1),
    ("d2c", "Et chez les 15 à 24 ans ?", 2.2),
    ("r2", "Plus : près de 20 pour cent ! Attention, c'est un taux : on divise par les jeunes actifs, pas par tous les jeunes.", 0.3),
    ("d3a", "Duel 3 : les inégalités.", 0.15),
    ("d3b", "En 1995, dans le privé, les femmes gagnent en moyenne 34 pour cent de moins que les hommes.", 0.1),
    ("d3c", "Et en 2024 ?", 0.3),
    ("c3", "Trois, deux, un.", 0.6),
    ("r3", "Moins : environ 22 pour cent. Et même à temps de travail égal, l'écart reste de 14 pour cent.", 0.3),
    ("d4a", "Dernier duel : la mondialisation.", 0.15),
    ("d4b", "En 1983, la Chine pèse à peine plus de 1 pour cent des exportations mondiales. En 2024 ?", 2.2),
    ("r4", "Plus : près de 15 pour cent ! Premier exportateur du monde.", 0.3),
    ("f1", "Alors, combien de bonnes réponses ? Dis-le en commentaire.", 0.15),
    ("f2", "Plus de défis sur Révisions Animées.", 0.0),
]
