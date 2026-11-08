"""Short « Ton avion est en feu » (philo, la liberté) : James Stockdale et le Manuel d'Épictète, à la deuxième personne.

Faits vérifiés :
- J. B. Stockdale, « Courage Under Fire: Testing Epictetus's Doctrines in a Laboratory of Human Behavior », Hoover
  Institution, 1993 (discours au King's College de Londres) : abattu le 9 septembre 1965 au-dessus du Nord-Vietnam
  (A-4 en feu, commandes coupées) ; après l'éjection, « environ trente secondes » avant de toucher la rue principale
  d'un village ; il se murmure « Five years down there, at least. I'm leaving the world of technology and entering
  the world of Epictetus. » ; rossé à l'arrivée, jambe gravement cassée ; le Manuel (ce qui dépend de nous / ce qui
  n'en dépend pas) ; quatrième de couverture : torturé quinze fois, deux ans aux fers, quatre ans à l'isolement.
- Rasoir tendu = signe qu'on le préparait pour un film de propagande ; il se rase une bande au milieu du crâne, puis
  se frappe le visage avec un tabouret : Washington Monthly, 29/12/2005 ; DVIDS (département de la Défense), récit
  de son fils (« until he was unrecognizable ») ; la citation de la Medal of Honor parle de ses « efforts de
  self-disfiguration » pour ne pas servir à la propagande ; US Naval Academy : printemps 1969.
- Libéré le 12 février 1973 (Operation Homecoming), soit 7 ans et 5 mois ; Medal of Honor remise par le président
  Ford le 4 mars 1976.
- Épictète, Manuel, I : « Il y a ce qui dépend de nous, il y a ce qui ne dépend pas de nous » (traduction reprise
  de l'épisode 4 de la série « La liberté », liberte_4.py).
Écarté : la tentative de suicide de 1969 (poignets), les détails des tortures, le nombre exact de jours prononcé.
La dernière phrase relance la première (boucle).
"""
CODE = "stockdale"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Stockdale": "Stokdèle", "Épictète": "Épiktète",
                 "Hoa Lo": "Hoa Lô", "Hanoï": "Anoï", "Hilton": "Hiltonne", "Medal of Honor": "Médeul ov Onneur",
                 "30": "trente", "1965": "mille neuf cent soixante-cinq", "1973": "mille neuf cent soixante-treize",
                 "5": "cinq", "7": "sept"}
PASSAGES = [
    ("s1", "Ton avion est en feu. Tu t'éjectes. 30 secondes avant de toucher le sol.", 0.25),
    ("s2", "Et tu penses… à un philosophe grec.", 0.45),
    ("s3", "1965, au-dessus du Nord-Vietnam. James Stockdale, pilote américain, descend en parachute.", 0.15),
    ("s4", "Il se murmure : 5 ans là-dessous, au moins. Je quitte le monde de la technologie… j'entre dans celui d'Épictète.", 0.35),
    ("s5", "En bas, on le roue de coups. Jambe cassée. Direction Hoa Lo, le Hanoï Hilton.", 0.2),
    ("s6", "Torture. Fers aux pieds. Isolement. Il avait dit 5 ans… ce sera plus de 7.", 0.4),
    ("s7", "Mais dans sa tête, il a emporté un livre : le Manuel d'Épictète.", 0.2),
    ("s8", "Il y a ce qui dépend de nous… et ce qui ne dépend pas de nous.", 0.3),
    ("s9", "Son corps, la douleur : ça ne dépend pas de lui. Ce qu'il accepte, ce qu'il refuse : ça, oui.", 0.35),
    ("s10", "Un jour, on lui tend un rasoir : signe qu'on va le filmer pour la propagande.", 0.2),
    ("s11", "Alors il se rase une bande au milieu du crâne. Et se frappe le visage avec un tabouret. Méconnaissable.", 0.3),
    ("s12", "Le film n'aura pas lieu.", 0.45),
    ("s13", "Libéré en 1973, il recevra la Medal of Honor.", 0.2),
    ("s14", "On lui a tout pris. Sauf une chose : son jugement.", 0.35),
    ("s15", "Peut-on être libre sous la contrainte ? C'est une vraie question de bac. La réponse est sur Révisions Animées.", 0.3),
    ("s16", "Et toi… ton avion est en feu. À quoi tu penses ?", 0.0),
]
