"""Short « SES : trouve l'intrus » (spécialité SES de Terminale) : format « le spectateur joue », plan `intrus` des
formats (15/11/2026), 4 manches. La chaîne n'a pas de cours de SES : faits tirés du programme officiel de Terminale et
de sources sérieuses, vérifiés le 27/11/2026.

Sources :
- Programme de SES de Terminale (BO spécial n° 8 du 25 juillet 2019 ; texte repris sur eduscol, « Voie générale »,
  et dans les fiches académiques, ac-nice, ac-orleans-tours) :
  « Comprendre que les problèmes d'appariements (frictions, inadéquations spatiales et de qualifications) et les
  asymétries d'information (salaire d'efficience) sont des sources de chômage structurel » ; « Comprendre les effets
  des fluctuations de l'activité économique sur le chômage conjoncturel » ; « Connaître les principales
  caractéristiques de la crise financière des années 1930 et de celle de 2008 (effondrement boursier, faillites en
  chaîne, chute du PIB et accroissement du chômage) » ; « Comprendre les phénomènes de panique bancaire et de
  faillites bancaires en chaîne » ; avantages comparatifs (dotations factorielles et technologiques) dans le chapitre
  sur le commerce international ; débat sur la pertinence d'une approche en termes de classes sociales.
- Insee, PCS 2020 (insee.fr/fr/metadonnees/pcs2020 ; « Une nomenclature socioprofessionnelle rénovée », 2020) :
  6 groupes socioprofessionnels (agriculteurs exploitants ; artisans, commerçants et chefs d'entreprise ; cadres et
  professions intellectuelles supérieures ; professions intermédiaires ; employés ; ouvriers) ; aucun ne s'appelle
  « classes moyennes ».
- Premier choc pétrolier : prix du baril multiplié par 4 entre octobre 1973 et janvier 1974 (Connaissance des
  énergies, fiche « Choc pétrolier » ; La finance pour tous, « Les chocs pétroliers ») : un choc d'offre.
- Lehman Brothers : faillite le 15 septembre 2008 (fait connu, cité par toutes les fiches du programme sur la crise
  de 2008).
- Durkheim, Les Règles de la méthode sociologique (1895), un des fondateurs de la sociologie ; Ricardo, avantages
  comparatifs (Des principes de l'économie politique et de l'impôt, 1817 : drap anglais et vin portugais) ; Smith et
  Keynes, économistes.
Écartés : le salaire minimum comme « cause » du chômage structurel (le programme parle d'effets positifs ou négatifs
des institutions : ambigu pour un intrus) ; la tulipomanie (son ampleur est discutée par les historiens) ; Marx et
Weber (à la fois économistes et sociologues : ambigu) ; les prix exacts du baril (les sources diffèrent selon le brut :
2,3 à 2,7 dollars avant, 9 à 11,65 après ; seul « multiplié par 4 » est commun).
"""
CODE = "intrusses"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"SES": "esse-eu-esse", "4": "quatre", "1": "un", "2": "deux", "3": "trois", "6": "six",
                 "1973": "mille neuf cent soixante-treize", "2008": "deux mille huit",
                 "INSEE": "Inssé", "Durkheim": "Durkème", "Keynes": "Kéïnze", "Smith": "Smisse",
                 "Ricardo": "Ricardo", "Lehman": "Lîmane", "Brothers": "Brodeurze"}
PASSAGES = [
    ("h1", "SES : trouve l'intrus. 4 manches, de plus en plus dures.", 0.15),
    ("h2", "Combien tu en trouves ?", 0.3),
    ("m1a", "Manche 1 : les auteurs.", 0.15),
    ("m1b", "Trois sont économistes. Un seul est sociologue.", 2.3),
    ("r1", "L'intrus : Durkheim, un des pères de la sociologie !", 0.2),
    ("e1", "Smith, Ricardo et Keynes, eux, sont économistes. Ricardo explique le commerce international par les avantages comparatifs.", 0.3),
    ("m2a", "Manche 2 : la structure sociale.", 0.15),
    ("m2b", "Trois sont des groupes de l'INSEE. Un seul n'en est pas un.", 2.3),
    ("r2", "Les classes moyennes ! L'INSEE classe les actifs en 6 groupes socioprofessionnels.", 0.1),
    ("e2", "Les classes moyennes, elles, font débat chez les sociologues.", 0.3),
    ("m3a", "Manche 3 : les crises.", 0.15),
    ("m3b", "Trois sont des crises financières. Une seule n'en est pas une.", 2.3),
    ("r3", "Le choc pétrolier de 1973 ! Le prix du baril est multiplié par 4.", 0.1),
    ("e3", "C'est un choc d'offre. En 2008, c'est la faillite d'une banque, Lehman Brothers, qui sème la panique.", 0.3),
    ("m4", "Dernière manche, la plus dure ! Trois causes de chômage structurel, une seule de chômage conjoncturel.", 0.5),
    ("c4", "Trois, deux, un.", 0.6),
    ("r4", "La chute de la demande ! Quand l'activité ralentit, le chômage monte.", 0.1),
    ("e4", "Frictions, qualifications inadaptées, salaire d'efficience : ces causes-là sont durables.", 0.3),
    ("f1", "Alors, combien d'intrus trouvés ? Dis-le en commentaire.", 0.15),
    ("f2", "Plus de défis sur Révisions Animées.", 0.0),
]
