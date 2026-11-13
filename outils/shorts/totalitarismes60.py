"""Short « Les totalitarismes en 60 secondes » (histoire, les régimes totalitaires), format 3 : cinq idées clés du chapitre.

Sources : uniquement le chapitre « Totalitarian Regimes » du site (dnl/index.html, CHAPTERS.H2, version française des idées,
frise et glossaire) et sa série vidéo (outils/serie-dnl/h2_1.py à h2_9.py, surtout le récapitulatif h2_9.py).
- Trois régimes : l'Italie de Mussolini (1922-1943), l'Allemagne nazie (1933-1945), l'URSS de Staline (1924-1953) (Intro, idée 6).
- Idée 1, la définition : « un régime qui cherche à contrôler totalement la société, par la contrainte, pour transformer
  l'homme selon une idéologie » ; le contrôle atteint « le travail, les loisirs, la famille, l'école, la religion et la
  pensée » ; « Une dictature exige que l'on se taise ; un régime totalitaire exige que l'on change » (Intro, idée 3 ; II.2,
  idée 1) ; buts suprêmes : la nation (Mussolini), la race (Hitler), la classe (Staline) (II.2, idée 6 ; h2_9.py).
- Idée 2, la prise du pouvoir sans coup d'État : marche sur Rome, octobre 1922, « La menace suffit : le roi nomme
  Mussolini » (I.2, idée 2) ; les nazis premier parti, « sans jamais leur donner la majorité » (I.2, idée 5) ; le 30 janvier
  1933, Hindenburg nomme Hitler chancelier, légalement (I.2, idée 6).
- Idée 3, le chef et le parti unique : « il Duce ha sempre ragione » — Mussolini a toujours raison ; le salut officiel
  « Heil Hitler » (II.1, idée 2) ; « une ville est rebaptisée Stalingrad en 1925 » (II.1, idée 1) ; un seul parti, un symbole
  (II.1, idée 5).
- Idée 4, l'homme nouveau : Jeunesses hitlériennes « obligatoire de 10 à 18 ans » (glossaire) ; le travailleur soviétique
  « célébré dès 1935 à travers le mineur Stakhanov » (II.2, idées 1 et 5).
- Idée 5, la terreur : « pas un échec de l'ordre mais une méthode de gouvernement » (II.3, idée 1) ; Dachau ouvert en 1933,
  le Goulag (II.3, idée 4 ; frise) ; Holodomor, « famine provoquée en Ukraine », 1932-1933 (frise ; I.3) — le site donne
  « environ quatre millions de morts » comme bilan ajouté hors des notes de cours : le short dit seulement « des millions » ;
  la Grande Purge de 1937-1938, 680 000 exécutions (II.3, idée 3 ; glossaire).
- Fin : le 1er septembre 1939, l'Allemagne attaque la Pologne (III.3 ; frise).
Ton sobre : rythme rapide, mais rien de léger sur la violence (pas de choc ni de buzzer sur les victimes).
Écartés (faute de place) : la brutalisation (Mosse), Arendt et la confiance des masses, la Nuit des Longs Couteaux, les lois
de Nuremberg, le T4, les ambitions hégémoniques et l'apaisement ; aucun chiffre sur l'Holodomor (bilan hors notes de cours).
"""
CODE = "totalitarismes60"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"60": "soixante", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq",
                 "10": "dix", "18": "dix-huit", "30": "trente", "1er": "premier",
                 "1922": "mille neuf cent vingt-deux", "1925": "mille neuf cent vingt-cinq",
                 "1932": "mille neuf cent trente-deux", "1933": "mille neuf cent trente-trois",
                 "1937": "mille neuf cent trente-sept", "1938": "mille neuf cent trente-huit",
                 "1939": "mille neuf cent trente-neuf", "680000": "six cent quatre-vingt mille",
                 "Duce": "Doutché", "Heil": "Haïl", "Hindenburg": "Hinndennbourg", "Stakhanov": "Stakanof",
                 "Dachau": "Dakao", "Holodomor": "Holodomor"}
PASSAGES = [
    ("s1", "Les totalitarismes en 60 secondes. 5 idées pour le bac.", 0.3),
    ("s2", "Mussolini, Hitler, Staline : trois régimes, une même machine.", 0.3),
    ("s3", "Idée 1 : tout contrôler. Pas seulement l'État : toute la société.", 0.15),
    ("s4", "Une dictature veut ton silence. Le totalitarisme veut te changer, selon une idéologie.", 0.2),
    ("s5", "La nation pour Mussolini, la race pour Hitler, la classe pour Staline.", 0.3),
    ("s6", "Idée 2 : ils prennent le pouvoir sans coup d'État.", 0.15),
    ("s7", "Octobre 1922, la marche sur Rome. La menace suffit : le roi nomme Mussolini.", 0.2),
    ("s8", "Hitler, jamais majoritaire, est nommé chancelier le 30 janvier 1933. Légalement.", 0.3),
    ("s9", "Idée 3 : un chef qu'on vénère, un parti unique.", 0.15),
    ("s10", "Le Duce a toujours raison. On salue : Heil Hitler. En 1925, une ville est rebaptisée Stalingrad.", 0.3),
    ("s11", "Idée 4 : fabriquer un homme nouveau, dès l'enfance.", 0.15),
    ("s12", "Jeunesses hitlériennes, obligatoires de 10 à 18 ans. En URSS, un modèle : le mineur Stakhanov.", 0.3),
    ("s13", "Idée 5 : la terreur. C'est une méthode de gouvernement.", 0.15),
    ("s14", "Police politique, camps : Dachau dès 1933, le Goulag en URSS.", 0.2),
    ("s15", "En 1932 et 1933, l'Holodomor : une famine provoquée, des millions de morts en Ukraine.", 0.2),
    ("s16", "Puis la Grande Purge de 1937 et 1938 : 680000 exécutions.", 0.35),
    ("s17", "Au bout, la guerre : le 1er septembre 1939, l'Allemagne attaque la Pologne.", 0.35),
    ("s18", "Toute la série est sur Révisions Animées.", 0.3),
    ("s19", "Alors : combien d'idées tu as retenues ?", 0.0),
]
