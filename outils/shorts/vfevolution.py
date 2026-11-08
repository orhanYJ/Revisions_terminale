"""Short « 5 affirmations sur l'évolution » (SVT, thème 1.A, chapitres 2 et 3) : format 4, vrai ou faux.

Faits : uniquement le cours de SVT de la chaîne (svt/index.html, pages t2, t2b, t3b ; scripts outils/serie-svt/svt_ch2.py
et svt_ch3.py) :
1. VRAI — mitochondries et chloroplastes descendent de bactéries phagocytées par une cellule eucaryote primitive mais pas
   digérées (endosymbiose, théorie de Lynn Margulis) ; argument essentiel : la double membrane (svt_ch2.py, scènes
   « margulis », « membrane » ; ligne 39 : « des bactéries entières, avalées il y a très longtemps, qui sont devenues
   les mitochondries et les chloroplastes de nos cellules ») ;
2. FAUX — « les mutations préexistent au hasard, l'antibiotique sélectionne les bactéries déjà résistantes » ; « N'écris
   jamais qu'une bactérie s'adapte, ou mute pour survivre » (svt/index.html ; svt_ch2.py, scène « resistance ») ;
3. VRAI — la dérive génétique : expérience de Buri (1956), 107 populations de 16 drosophiles, fréquence de bw75 à 0,5 au
   départ, sans aucune sélection ; après 19 générations, beaucoup de populations ont perdu l'allèle et beaucoup d'autres
   l'ont fixé (svt/index.html, t3b ; svt_ch3.py, scène « buri ») ; l'histogramme de la vidéo est une simulation : le short
   ne donne donc aucun décompte précis ;
4. FAUX — critère phénotypique trompeur : deux fourmis des bois, Formica lugubris et F. paralugubris, longtemps confondues,
   séparées en 1996 par le critère moléculaire (svt/index.html, t3b ; svt_ch3.py, scène « espece ») ;
5. VRAI — la conjugaison : deux bactéries se relient par un pont cytoplasmique, la copie d'un plasmide passe de la donneuse
   à la receveuse, entre bactéries de la même espèce ou d'espèces différentes ; c'est souvent ainsi que passent des gènes
   de résistance aux antibiotiques (svt_ch2.py, scène « bacteries »).
Écarté : le dimorphisme sexuel de l'aurore (exemple pris hors du cours dans la vidéo), les chiffres de l'histogramme de
Buri (simulés), la syncytine (une affirmation de plus aurait dépassé la durée).
"""
CODE = "vfevolution"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"5": "cinq", "1956": "mille neuf cent cinquante-six", "107": "cent sept", "16": "seize",
                 "19": "dix-neuf", "1996": "mille neuf cent quatre-vingt-seize", "Buri": "Bouri", "ADN": "a-dé-ène"}
PASSAGES = [
    ("v1", "5 affirmations sur l'évolution. Combien tu en as justes ?", 0.35),
    ("q1", "Un. Tes mitochondries descendent d'une bactérie. Vrai… ou faux ?", 1.5),
    ("r1", "Vrai ! Une bactérie avalée par une cellule, mais jamais digérée. La preuve : ses deux membranes.", 0.3),
    ("q2", "Deux. Les bactéries mutent pour résister aux antibiotiques. Vrai… ou faux ?", 1.5),
    ("r2", "Faux ! Les mutations arrivent au hasard, avant. L'antibiotique sélectionne celles qui résistaient déjà.", 0.3),
    ("q3", "Trois. Une population peut évoluer par pur hasard. Vrai… ou faux ?", 1.5),
    ("r3", "Vrai ! C'est la dérive. En 1956, Buri suit 107 populations de 16 drosophiles, sans aucune sélection.", 0.15),
    ("r3b", "19 générations plus tard, l'allèle a disparu de beaucoup d'entre elles. Dans d'autres, il est le seul.", 0.3),
    ("q4", "Quatre. Deux animaux qui se ressemblent sont forcément de la même espèce. Vrai… ou faux ?", 1.5),
    ("r4", "Faux ! Deux fourmis des bois ont longtemps été confondues. En 1996, leur ADN a révélé deux espèces.", 0.3),
    ("q5", "Cinq. Une bactérie peut donner un gène à une bactérie d'une autre espèce. Vrai… ou faux ?", 1.5),
    ("r5", "Vrai ! Un pont se forme, une copie d'ADN passe. C'est ainsi que voyagent les résistances.", 0.35),
    ("fin", "Alors, combien tu en as justes ? Dis ton score en commentaire.", 0.3),
    ("ch", "Tout le cours est sur Révisions Animées.", 0.0),
]
