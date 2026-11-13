"""Short « Un seul bateau » (géographie, espaces maritimes) : l'Ever Given en travers du canal de Suez, mars 2021.

Le cours (chapitre « Maritimisation and the geostrategic importance of the seas », partie II.2, idée « Les choke points
sont des passages étroits et encombrés dont dépend le commerce mondial », et Worksheet 5 « le canal de Suez ») :
les choke points sont des passages étroits très empruntés, naturels (détroits) ou artificiels (canaux) ; si l'un d'eux
ferme, le commerce mondial est durement touché ; le 23 mars 2021, l'Ever Given, porte-conteneurs plus long que la tour
Eiffel n'est haute, se met en travers du canal de Suez sous des vents violents et le bloque entièrement ; environ 12 %
du commerce mondial passe par Suez, raccourci entre l'Asie et l'Europe ; son blocage a montré la fragilité du commerce
mondial. La durée du blocage (six jours) est déjà signalée dans le cours comme ajoutée hors du cours : vérifiée ici.

Faits du récit, pris hors du cours et vérifiés :
- Port Economics, Management and Policy (Notteboom, Pallis, Rodrigue), « Blockage of the Suez Canal, March 2021 »
  (porteconomicsmanagement.org/suez-canal-blockage-2021/) : échouage le 23 mars 2021, remis à flot le 29 mars ;
  navire de 400 m de long, plus de 20 000 EVP ; vents arrière violents et tempête de sable ; tronçon sud à une seule
  voie ; dragues et pelles mécaniques retirent plus de 30 000 m³ de sable autour de la proue ; remorqueurs.
- Reuters (repris par Dawn, The Standard, etc., 3 avril 2021) : le président de l'Autorité du canal de Suez, Osama
  Rabie, parle d'une file de 422 navires, la dernière passée le 3 avril ; remise à flot le 29 mars à 15 h 05 (Boskalis).
- Associated Press / NASA (repris par KSL, ABC17, 30 mars 2021 : « Full worm moon helped break logjam in Suez Canal ») :
  la pleine Lune du 28 mars a donné une marée de vives-eaux, environ 45 cm au-dessus de la normale, le lundi 29.
- Al Jazeera, « Suez Canal blockage halts $9.6bn a day of ship traffic » (25 mars 2021), d'après Lloyd's List : environ
  9,6 milliards de dollars de marchandises par jour (estimation grossière, d'où « près de 10 milliards »).
- Al Jazeera (25 mars 2021) et The National (« Don't mock the weak », avril 2021) : la photo d'une pelleteuse seule
  creusant la berge au pied du navire, publiée par l'Autorité du canal, devient un mème mondial.
Écartés : le nombre exact de navires selon les jours (165, 213, 369, 422 selon les sources et les dates : on dit
« plus de 400 », chiffre de l'Autorité du canal à la fin) ; le coût par heure ; le nom du conducteur de la pelleteuse ;
les causes discutées après l'enquête (vitesse, erreur humaine) ; la saisie du navire par l'Égypte ; les 6 000 milles du
détour par le Cap (dans le cours, mais un chiffre de trop).
Lien : géographie, thème « Espaces maritimes », chapitre G1 (choke points). La dernière phrase relance la première.
"""
CODE = "evergiven"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Ever Given": "Èveur Guiveune", "Suez": "Su-èze", "choke points": "tchok poïntes",
                 "2021": "deux mille vingt et un", "23": "vingt-trois", "29": "vingt-neuf",
                 "400": "quatre cents", "12": "douze", "10": "dix", "100": "cent", "6": "six",
                 "30 000": "trente mille"}
PASSAGES = [
    ("s1", "Tu peux bloquer le commerce mondial… avec un seul bateau ?", 0.35),
    ("s2", "23 mars 2021. Canal de Suez.", 0.2),
    ("s3", "Tu es à bord de l'Ever Given. Un des plus grands porte-conteneurs du monde.", 0.15),
    ("s4", "400 mètres. Plus long que la tour Eiffel n'est haute.", 0.25),
    ("s5", "Tempête de sable. Le vent pousse tes conteneurs comme une voile.", 0.2),
    ("s6", "Le navire dérape. L'avant se plante dans une rive. L'arrière dans l'autre.", 0.3),
    ("s7", "Coincé en travers du canal. Plus rien ne passe.", 0.4),
    ("s8", "Derrière toi, les navires s'arrêtent. 10. 100. Plus de 400.", 0.25),
    ("s9", "Par ce canal passe 12 pour cent du commerce mondial. Entre l'Asie et l'Europe.", 0.2),
    ("s10", "Près de 10 milliards de dollars de marchandises bloquées. Chaque jour.", 0.35),
    ("s11", "Sur la berge, pour te dégager… une petite pelleteuse.", 0.3),
    ("s12", "La photo fait le tour du monde. Un mème.", 0.25),
    ("s13", "Il faut des remorqueurs, des dragues… 30 000 mètres cubes de sable.", 0.2),
    ("s14", "Et une alliée : la Lune. Pleine lune, grande marée.", 0.3),
    ("s15", "29 mars. L'eau monte. Après 6 jours, tu flottes enfin.", 0.35),
    ("s16", "Détroits et canaux : des passages étroits dont dépend le commerce mondial. En géographie, ce sont des choke points.", 0.25),
    ("s17", "Pourquoi sont-ils stratégiques ? C'est une question type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s18", "Et toi… tu aurais cru qu'un seul bateau pouvait bloquer le monde ?", 0.0),
]
