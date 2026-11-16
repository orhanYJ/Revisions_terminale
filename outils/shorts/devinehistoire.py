"""Short « Devine qui c'est : les hommes qui ont fait le XXe siècle » (format « devine », le spectateur joue) :
trois manches, trois indices du plus dur au plus facile, une photo pixellisée qui se précise, puis la révélation.

Sources : uniquement le cours d'histoire de la chaîne (dnl/index.html, chapitres H1 à H3, et les scripts des
vidéos outils/serie-dnl/h1f_*.py, h2_*.py, h3f_*.py).
- Franklin Roosevelt :
  · 1936, « Je hais la guerre » (discours « I hate war ») : h1f_4.py (« En 1936, Franklin Roosevelt déclare »).
  · démocrate, élu en 1932 : h1f_3.py (« Roosevelt, un démocrate, est élu en 1932 »).
  · le New Deal ; entre en fonctions en mars 1933 ; « Secourir. Relancer. Réformer. » : h1f_3.py.
  · photo Hoover et Roosevelt en route vers l'investiture, 4 mars 1933 : h1f_3.py.
- Joseph Staline :
  · discours du 7 janvier 1933 : le plan quinquennal présenté comme la voie vers « l'abolition des classes » en URSS :
    h2_1.py, h2_3.py (Worksheet 2).
  · premier plan quinquennal lancé en 1928 : h2_3.py (« In 1928, he launches the first Five-Year Plan »).
  · l'URSS de Staline de 1924 à sa mort en 1953 : h2_1.py (« Stalin's USSR (1924–1953) »).
  · la famine en Ukraine de 1932-1933 (Holodomor) et le Goulag, ses camps de travail forcé : h2_1.py, h2_3.py, h2_5.py.
- Winston Churchill :
  · conservateur hostile à l'apaisement ; Premier ministre le 10 mai 1940 ; le 4 juin 1940, aux Communes, « nous ne
    nous rendrons jamais » ; après l'armistice du 22 juin 1940, le Royaume-Uni est seul : h3f_3.py.
Écartés : de Gaulle et Mussolini (trois manches seulement) ; « président jusqu'en 1945 » pour Roosevelt (pas dans le
cours) ; le chiffre des morts du Holodomor (non repris).
"""
CODE = "devinehistoire"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "10": "dix", "XXe": "vingtième",
                 "1924": "mille neuf cent vingt-quatre", "1928": "mille neuf cent vingt-huit",
                 "1932": "mille neuf cent trente-deux", "1933": "mille neuf cent trente-trois",
                 "1936": "mille neuf cent trente-six", "1940": "mille neuf cent quarante",
                 "1953": "mille neuf cent cinquante-trois", "Roosevelt": "Rouzvelt", "Churchill": "Tcheur-tchil",
                 "URSS": "u-erre-èsse-èsse", "Goulag": "Goulague"}
PASSAGES = [
    ("d1", "Devine qui c'est. 3 hommes qui ont fait le XXe siècle.", 0.25),
    ("d2", "3 indices chacun, du plus dur au plus facile. Trouve avant la fin du compte !", 0.25),
    ("d3", "Manche 1. Indice 1 : en 1936, il déclare : je hais la guerre.", 0.25),
    ("d4", "Indice 2 : il est élu président en 1932.", 0.25),
    ("d5", "Indice 3 : il lance le New Deal. Trois, deux, un.", 1.15),
    ("d6", "C'est Franklin Roosevelt ! Président des États-Unis à partir de 1933.", 0.2),
    ("d7", "Face à la Grande Dépression, son New Deal : secourir, relancer, réformer.", 0.25),
    ("d8", "Manche 2, plus dure. Indice 1 : en 1933, il promet l'abolition des classes.", 0.25),
    ("d9", "Indice 2 : en 1928, il lance le premier plan quinquennal.", 0.25),
    ("d10", "Indice 3 : il dirige l'URSS de 1924 à 1953. Trois, deux, un.", 1.15),
    ("d11", "C'est Joseph Staline ! Sous son pouvoir : la famine en Ukraine, et le Goulag, ses camps de travail forcé.", 0.25),
    ("d12", "Dernière manche. Indice 1 : conservateur, il s'oppose à la politique d'apaisement.", 0.25),
    ("d13", "Indice 2 : le 10 mai 1940, il devient Premier ministre.", 0.25),
    ("d14", "Indice 3 : devant les Communes, il lance : nous ne nous rendrons jamais. Trois, deux, un.", 1.15),
    ("d15", "C'est Winston Churchill ! En juin 1940, le Royaume-Uni se retrouve seul face à Hitler.", 0.25),
    ("d16", "Combien tu en as trouvés ? Dis-le en commentaire.", 0.25),
    ("d17", "Le cours complet est sur Révisions Animées.", 0.0),
]
