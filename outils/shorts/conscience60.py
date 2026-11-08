"""Short « La conscience en 60 secondes » (philo, la conscience), format 3 : les cinq idées clés de la série.

Sources : uniquement la série « La conscience » de la chaîne (formules et exemples déjà vérifiés dans ses épisodes).
- Idée 1, conscience spontanée / réfléchie : conscience_1.py, scène « degres » (le joueur qui frappe le ballon voit
  le but sans penser à lui-même ; après le match, il revoit l'action : « pourquoi ai-je tiré si vite ? »).
- Idée 2, Descartes : conscience_2.py (doute des sens, du rêve, malin génie « même dans les calculs » ; « douter,
  c'est penser. Et pour penser, il faut être » ; « je pense, donc je suis » ; « la première vérité […] c'est la
  conscience que j'ai de moi-même ») et récap conscience_7.py.
- Idée 3, Freud : conscience_3.py, scène « freud » (l'oubli du nom de Signorelli, peintre des fresques d'Orvieto :
  « Il lui vient Botticelli, Boltraffio… jamais le bon » ; oublis, lapsus, rêves = trous ; « L'hypothèse de
  l'inconscient est nécessaire et légitime »).
- Idée 4, Sartre : conscience_4.py, scène « regard » (L'Être et le Néant, 1943 : l'œil au trou de la serrure,
  des pas dans le couloir, la honte : « tu existes pour toi-même… mais tel qu'un autre te voit »).
- Idée 5, la conscience morale : conscience_5.py (Rousseau : « Conscience ! conscience ! instinct divin » ;
  Raskolnikov, Crime et Châtiment, Dostoïevski, 1866 : il tue une vieille usurière, « Pas de témoin. Pas de
  preuve », « Personne ne l'accuse. Personne… sauf lui »).
Écartés (faute de place) : Nietzsche, Husserl, Locke et Hume, Leibniz, Pascal ; « conscience de quelque chose »
est de Husserl dans la série, d'où le choix de Sartre par la serrure.
"""
CODE = "conscience60"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"60": "soixante", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq",
                 "Signorelli": "Signorèlli", "Boltraffio": "Boltrafio", "Botticelli": "Botitchèlli",
                 "Raskolnikov": "Raskolnikof"}
PASSAGES = [
    ("s1", "La conscience en 60 secondes. 5 idées pour le bac.", 0.3),
    ("s2", "Idée 1 : il y a deux consciences.", 0.15),
    ("s3", "Un joueur frappe le ballon : il voit le but, pas lui-même. Conscience spontanée.", 0.2),
    ("s4", "Après le match, il revoit l'action : pourquoi j'ai tiré si vite ? Conscience réfléchie.", 0.3),
    ("s5", "Idée 2 : Descartes doute de tout. Les sens, le rêve, et même les calculs.", 0.15),
    ("s6", "Mais pour douter, il faut penser. Et pour penser, il faut être.", 0.2),
    ("s7", "Je pense, donc je suis. Ta première certitude, c'est ta conscience.", 0.3),
    ("s8", "Idée 3 : Freud. Ta conscience ne voit pas tout.", 0.15),
    ("s9", "Freud oublie le nom d'un peintre. Il lui vient Botticelli, Boltraffio… Le bon ? Signorelli.", 0.2),
    ("s10", "Un oubli, un lapsus, un rêve : des trous. Pour les expliquer, il faut un inconscient.", 0.3),
    ("s11", "Idée 4 : Sartre. Tu colles ton œil à une serrure. Tu ne penses qu'à la scène.", 0.15),
    ("s12", "Soudain, des pas. Quelqu'un te voit. La honte.", 0.2),
    ("s13", "D'un coup, tu existes pour toi… tel qu'un autre te voit.", 0.3),
    ("s14", "Idée 5 : la conscience morale, la voix qui juge. Rousseau l'appelle instinct divin.", 0.15),
    ("s15", "Raskolnikov tue une usurière. Pas de témoin, pas de preuve.", 0.2),
    ("s16", "Personne ne l'accuse. Personne… sauf lui.", 0.35),
    ("s17", "Toute la série « La conscience » est sur Révisions Animées.", 0.3),
    ("s18", "Alors : combien d'idées tu as retenues ?", 0.0),
]
