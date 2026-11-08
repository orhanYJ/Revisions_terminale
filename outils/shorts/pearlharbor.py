"""Short « Personne ne te croit » (histoire, la Seconde Guerre mondiale) : le radar d'Opana, 7 décembre 1941.

Le cours (chapitre « La Seconde Guerre mondiale », partie I.2, idée « Décembre 1941 : la guerre devient mondiale ») :
le 7 décembre 1941, le Japon, une des puissances de l'Axe, bombarde la base américaine de Pearl Harbor, à Hawaï ;
les États-Unis déclarent aussitôt la guerre au Japon ; le 11 décembre, l'Allemagne et l'Italie déclarent la guerre
aux États-Unis ; la guerre se livre désormais sur tous les océans et tous les continents.

Faits du récit, pris hors du cours et vérifiés :
- National Park Service, « Opana Mobile Radar Site » (nps.gov/perl/learn/historyculture/opana-mobile-radar-site.htm) :
  les soldats (Privates) George Elliott et Joseph Lockard à la station radar mobile d'Opana, au nord d'Oahu ;
  à 7 h, toutes les stations s'arrêtent sauf Opana ; à 7 h 02, la première vague japonaise apparaît à 137 milles
  (≈ 220 km) au nord ; ils la suivent jusqu'à la perte du contact vers 7 h 39-7 h 45 ; le lieutenant Kermit Tyler,
  au centre d'information de Fort Shafter, à son deuxième jour de formation, leur dit de ne pas s'en faire : il croit
  à un vol de B-17 attendu de la côte ouest.
- National Park Service, « Remembering Pearl Harbor: Minute by Minute » (nps.gov/perl/learn/historyculture/timeline.htm) :
  à 7 h 02, un écho « plus gros que tout ce qu'ils avaient jamais vu » ; à 7 h 55, le message radio
  « AIR RAID PEARL HARBOR THIS IS NOT DRILL ».
- The National WWII Museum, « Remembering Pearl Harbor: A Pearl Harbor Fact Sheet » : l'attaque commence à 7 h 55 ;
  le radariste prévient son supérieur, qui pense à des B-17 américains attendus ce jour-là, « not to worry about it » ;
  2 403 Américains tués (dont 68 civils), 19 navires détruits ou endommagés dont 8 cuirassés ; le 8 décembre,
  Roosevelt obtient du Congrès la déclaration de guerre au Japon ; le 11 décembre, l'Allemagne et l'Italie
  déclarent la guerre aux États-Unis.
Écartés : le nombre d'avions vu à l'écran (« 180 » d'après Wikipédia, non confirmé ailleurs), qui des deux soldats
a téléphoné ou parlé au lieutenant (les sources divergent : on dit « vous »), le camion du petit-déjeuner en retard,
la musique hawaïenne à la radio.
Aucun nom propre de soldat dans la voix. Lien : série « La Seconde Guerre mondiale », épisode « Le Royaume-Uni seul ».
La dernière phrase relance la première (boucle).
"""
CODE = "pearlharbor"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Pearl Harbor": "Peurl Arbeur", "Hawaï": "Ha-ouaï",
                 "1941": "mille neuf cent quarante et un", "7": "sept", "7h": "sept heures",
                 "7h02": "sept heures deux", "7h40": "sept heures quarante", "7h55": "sept heures cinquante-cinq",
                 "200": "deux cents", "2400": "deux mille quatre cents", "11": "onze"}
PASSAGES = [
    ("s1", "Tu vois la guerre arriver sur ton écran… et personne ne te croit ?", 0.35),
    ("s2", "7 décembre 1941. Hawaï. Un dimanche matin.", 0.2),
    ("s3", "Tu es simple soldat. Devant toi, un radar, sur une colline.", 0.15),
    ("s4", "7h. Ton service est fini. Mais tu laisses l'écran allumé.", 0.25),
    ("s5", "7h02. Un écho apparaît. Au nord, à plus de 200 kilomètres.", 0.2),
    ("s6", "Énorme. Le plus gros que tu aies jamais vu.", 0.2),
    ("s7", "Des avions. Beaucoup d'avions. Et ils foncent droit sur l'île.", 0.3),
    ("s8", "Vous appelez. Au bout du fil, un lieutenant. C'est son deuxième jour.", 0.2),
    ("s9", "Sa réponse tient en une phrase : ne vous en faites pas.", 0.35),
    ("s10", "Pour lui, ce sont des bombardiers américains, attendus ce matin-là.", 0.25),
    ("s11", "Vous le suivez encore. Vers 7h40, il disparaît.", 0.45),
    ("s12", "7h55. Des avions plongent sur Pearl Harbor. Ils sont japonais.", 0.3),
    ("s13", "À la radio : raid aérien sur Pearl Harbor. Ceci n'est pas un exercice.", 0.35),
    ("s14", "Plus de 2400 morts américains. Et toi, tu les avais vus venir.", 0.4),
    ("s15", "Le lendemain, les États-Unis déclarent la guerre au Japon. Le 11 décembre, l'Allemagne et l'Italie la leur déclarent.", 0.2),
    ("s16", "La guerre devient mondiale.", 0.3),
    ("s17", "Pourquoi en 1941 ? C'est un sujet type bac d'histoire. La réponse est sur Révisions Animées.", 0.3),
    ("s18", "Et toi… ce point sur l'écran, tu y aurais cru ?", 0.0),
]
