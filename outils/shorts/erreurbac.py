"""Short « Trouve l'erreur dans ces copies de bac » (format « erreur », le spectateur joue) : trois copies de bac,
quatre lignes chacune, une seule fausse ; un chrono, puis la correction.

Sources : uniquement le cours de la chaîne (site et scripts des vidéos).
- Copie de philosophie (« Sommes-nous libres ? ») : série « La liberté ».
  · Descartes, la volonté infinie (Méditations, IV) : liberte_2.py (« Mais ma volonté est infinie »), liberte_7.py.
  · Spinoza, le libre arbitre comme illusion (on se croit libre parce qu'on ignore les causes) : liberte_3.py
    (« L'illusion du libre arbitre »), liberte_6.py.
  · L'ERREUR : « L'homme est né libre, et partout il est dans les fers » est de Rousseau, Du contrat social, I, 1
    (1762), et non de Sartre : liberte_5.py (« Son Contrat social s'ouvre sur une phrase-choc », citation c_fer,
    « Du contrat social, I, 1 (1762) »). Dans la voix : « au début de Du contrat social » (c'est la première phrase du
    chapitre 1 du livre I, après un court préambule : on ne dit pas « la toute première phrase »).
  · Sartre, « L'homme est condamné à être libre » (L'existentialisme est un humanisme, 1946) : liberte_2.py, liberte_7.py.
  · Kant, « tu dois, donc tu peux » (formule qui résume l'idée, présentée comme telle dans le cours) : liberte_4.py,
    devoir_6.py.
- Copie d'histoire (« La crise de 1929 ») : chapitre H1 du site (dnl/index.html) et série h1f_*.py.
  · Jeudi 24 octobre 1929, le jeudi noir : h1f_1.py (scène « trois »).
  · Dow Jones de 381 (septembre 1929) à 41 (juillet 1932) : h1f_1.py (retenir de la scène du krach).
  · Environ 5 000 banques en faillite avant 1932 : h1f_2.py.
  · L'ERREUR : le New Deal est lancé par Franklin Roosevelt, démocrate, élu en 1932, entré en fonctions en mars 1933,
    pas par Herbert Hoover, le président sortant (président pendant le krach) : h1f_3.py (« Mars 1933, Washington.
    Franklin Roosevelt entre en fonctions, et lance le New Deal. Secourir. Relancer. Réformer. » ; « Roosevelt, un
    démocrate, est élu en 1932 » ; « Le sortant, Herbert Hoover »).
- Copie de SVT (« La méiose ») : svt/index.html (glossaire et unité t1u2).
  · La méiose donne quatre cellules haploïdes génétiquement différentes.
  · Crossing-over (brassage intrachromosomique) en prophase I, entre chromatides non sœurs d'un bivalent.
  · L'ERREUR : les chromosomes homologues se séparent en anaphase I ; l'anaphase II sépare les chromatides (le
    glossaire du site le donne comme piège : « L'anaphase I sépare les [homologues] ; c'est l'anaphase II qui sépare
    les chromatides »).
  · 2^23 = 8 388 608 combinaisons par le seul brassage interchromosomique chez l'humain (« plus de 8 millions »).
Écartés : le Dow Jones dans la voix (déjà dans la copie), le chiffre du chômage américain (absent du cours en
français), « la toute première phrase du Contrat social » (inexact, voir plus haut).
"""
CODE = "erreurbac"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre",
                 "1762": "dix-sept cent soixante-deux", "1929": "mille neuf cent vingt-neuf",
                 "1932": "mille neuf cent trente-deux", "1933": "mille neuf cent trente-trois",
                 "SVT": "èss vé té", "Hoover": "Houveur", "Roosevelt": "Rouzvelt"}
PASSAGES = [
    ("e1", "Trois copies de bac. Une erreur cachée dans chacune.", 0.25),
    ("e2", "Toi, tu la trouves avant la fin du chrono ? On joue.", 0.3),
    ("e3", "Manche 1 : la philo. Sujet : sommes-nous libres ?", 0.2),
    ("e4", "Lis les 4 lignes. Trois, deux, un.", 1.3),
    ("e5", "Ligne 3 ! « Partout il est dans les fers » : ce n'est pas Sartre.", 0.2),
    ("e6", "C'est Rousseau, au début de Du contrat social, en 1762.", 0.2),
    ("e7", "Nuance : Sartre, lui, écrit que l'homme est condamné à être libre.", 0.3),
    ("e8", "Manche 2 : l'histoire. Sujet : la crise de 1929. Une seule ligne est fausse. Trois, deux, un.", 1.3),
    ("e9", "Ligne 4 ! Le New Deal, ce n'est pas Hoover.", 0.2),
    ("e10", "C'est Roosevelt, élu en 1932, qui le lance en 1933.", 0.15),
    ("e11", "Secourir, relancer, réformer.", 0.2),
    ("e12", "Hoover, lui, était le président du krach de 1929.", 0.3),
    ("e13", "Dernière manche, la plus dure : la SVT. Courage.", 0.2),
    ("e14", "Sujet : la méiose. 4 lignes, une seule fausse. Trois, deux, un.", 1.3),
    ("e15", "Ligne 3 ! Les homologues se séparent en anaphase 1, pas en anaphase 2.", 0.2),
    ("e16", "L'anaphase 2, elle, sépare les chromatides de chaque chromosome.", 0.2),
    ("e17", "C'est le piège classique de la méiose : retiens-le.", 0.3),
    ("e18", "Alors, combien d'erreurs repérées ? 0, 1, 2 ou 3 ? Dis-le en commentaire.", 0.25),
    ("e19", "Les cours complets sont sur Révisions Animées.", 0.0),
]
