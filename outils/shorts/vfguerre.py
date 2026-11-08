"""Short « Vrai ou faux : la Seconde Guerre mondiale » (histoire) : cinq affirmations, verdicts tirés du cours.

Toutes les affirmations et explications viennent du chapitre « La Seconde Guerre mondiale » du site (dnl/index.html)
et de son édition vidéo française (outils/serie-dnl/h3f_*.py) :
1. VRAI — pacte germano-soviétique, 23 août 1939 : pacte de non-agression dont les clauses secrètes prévoient
   le partage de la Pologne ; « deux ennemis idéologiques » (cours, partie I.1 et glossaire).
2. FAUX — l'appel du 18 juin 1940 : « peu de gens entendent l'émission elle-même ; son importance grandit ensuite,
   avec la France libre » (Entraînement du site, source Fondation Charles de Gaulle / BBC) ; confirmé par le ministère
   des Armées, Chemins de mémoire, « 1940. Répondre à l'Appel » (defense.gouv.fr). De Gaulle lance la France libre
   (pas un gouvernement en exil).
3. FAUX — pas de débarquement allemand en Grande-Bretagne : la Luftwaffe n'obtient pas la maîtrise du ciel en 1940 ;
   Hitler reporte l'invasion au printemps 1941, puis sans date, parce que l'Allemagne retourne ses forces contre
   l'URSS (cours, partie I.2).
4. VRAI — le 11 décembre 1941, l'Allemagne et l'Italie déclarent la guerre aux États-Unis, quatre jours après
   Pearl Harbor (7 décembre) ; la guerre devient mondiale (cours, partie I.2).
5. FAUX — Stalingrad : l'armée allemande, encerclée en novembre 1942, capitule ; Paulus le 31 janvier 1943,
   les dernières troupes le 2 février ; environ 91 000 prisonniers (cours, partie II.2, chiffre corrigé du cours).
Écarté : une affirmation sur les centres de mise à mort (six, tous en Pologne occupée), pour ne pas traiter la Shoah
sur le ton d'un jeu (chrono, buzzer) ; aucune affirmation sur des chiffres incertains.
"""
CODE = "vfguerre"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Pearl Harbor": "Peurl Arbeur", "Paulus": "Paou-louss",
                 "5": "cinq", "4": "quatre", "11": "onze", "18": "dix-huit", "31": "trente et un",
                 "1939": "mille neuf cent trente-neuf", "1940": "mille neuf cent quarante",
                 "1941": "mille neuf cent quarante et un", "1943": "mille neuf cent quarante-trois",
                 "91000": "quatre-vingt-onze mille"}
PASSAGES = [
    ("v1", "5 affirmations sur la Seconde Guerre mondiale. Combien tu en as justes ?", 0.3),
    ("v2", "Top chrono.", 0.3),
    ("a1", "Première. En août 1939, Hitler et Staline, deux ennemis, signent un pacte. Vrai… ou faux ?", 2.0),
    ("b1", "Vrai. Le pacte germano-soviétique. En secret, il prévoit le partage de la Pologne.", 0.35),
    ("a2", "Deuxième. L'appel du 18 juin 1940 ? Presque toute la France l'entend. Vrai… ou faux ?", 2.0),
    ("b2", "Faux. Peu de gens l'entendent en direct. Son importance grandit ensuite, avec la France libre.", 0.35),
    ("a3", "Troisième. En 1940, l'armée allemande débarque en Grande-Bretagne. Vrai… ou faux ?", 2.0),
    ("b3", "Faux. Sans maîtriser le ciel, pas de débarquement. Hitler reporte l'invasion, puis se tourne vers l'URSS.", 0.35),
    ("a4", "Quatrième. En décembre 1941, c'est Hitler qui déclare la guerre aux États-Unis. Vrai… ou faux ?", 2.0),
    ("b4", "Vrai. Le 11 décembre, 4 jours après Pearl Harbor, avec l'Italie. La guerre devient mondiale.", 0.35),
    ("a5", "Dernière. À Stalingrad, l'armée allemande se bat jusqu'au bout, sans jamais se rendre. Vrai… ou faux ?", 2.0),
    ("b5", "Faux. Encerclée, elle capitule : le 31 janvier 1943, Paulus se rend. Environ 91000 Allemands sont faits prisonniers.", 0.35),
    ("e1", "Alors, ton score ? Dis-le en commentaire.", 0.3),
    ("e2", "Toute la guerre est expliquée sur Révisions Animées.", 0.0),
]
