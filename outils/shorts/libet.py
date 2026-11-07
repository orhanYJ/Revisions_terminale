"""Short « Ton cerveau décide avant toi » (philo, la liberté) : texte lu, passage par passage.

Chaque passage : (id, texte lu, silence après en secondes). Les faits viennent de l'épisode 3 de la série
« La liberté » (liberte_3.py) : Libet 1983, activité cérébrale ≈ −0,5 s, conscience de vouloir ≈ −0,2 s, veto,
signal peut-être simple bruit de fond ; Spinoza, lettre à Schuller (1674) et Éthique II, 35, scolie (paraphrasés).
La dernière phrase relance la première (boucle TikTok).
"""
CODE = "libet"
TEMPO = 1.1          # voix des séries, un peu plus vive
PRONONCIATION = {"Libet": "Libette"}
PASSAGES = [
    ("s1", "Avant même que tu décides… ton cerveau s'est déjà mis en marche.", 0.35),
    ("s2", "En 1983, le neuroscientifique américain Benjamin Libet tente une expérience toute simple.", 0.15),
    ("s3", "Plie le poignet, quand tu veux. Et sur cette horloge, note l'instant exact où l'envie te prend.", 0.15),
    ("s4", "Pendant ce temps, des électrodes écoutent ton cerveau.", 0.3),
    ("s5", "Résultat ? Une activité cérébrale démarre une demi-seconde avant le geste.", 0.15),
    ("s6", "Mais l'envie de bouger, tu ne la sens que deux dixièmes de seconde avant.", 0.25),
    ("s7", "Pendant trois dixièmes de seconde… ton cerveau travaille sans toi.", 0.45),
    ("s8", "Spinoza l'écrivait déjà au dix-septième siècle : une pierre qu'on lance, si elle pouvait penser, croirait qu'elle vole parce qu'elle le veut.", 0.15),
    ("s9", "Nous sommes pareils : on se croit libre… parce qu'on ignore les causes qui nous font agir.", 0.4),
    ("s10", "Alors, le libre arbitre, une illusion ? Pas si vite.", 0.2),
    ("s11", "Libet lui-même te laisse un pouvoir : celui de dire non. Un veto, au dernier moment.", 0.15),
    ("s12", "Et depuis, des chercheurs soupçonnent que ce signal n'est peut-être qu'un bruit de fond du cerveau.", 0.35),
    ("s13", "Libre ou pas ? C'est une vraie question de bac. La réponse complète est sur Révisions Animées.", 0.3),
    ("s14", "Et toi… tu es sûr que c'est toi qui décides ?", 0.0),
]
