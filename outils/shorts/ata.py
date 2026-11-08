"""Short « Le vrai Sa Majesté des mouches » (philo, l'État) : les six garçons tongiens naufragés sur 'Ata (1965-1966).

Faits vérifiés sur R. Bregman, « The real Lord of the Flies: what happened when six boys were shipwrecked
for 15 months », The Guardian, 9 mai 2020 (extrait de Humankind, en français Humanité) :
juin 1965, six élèves (13 à 16 ans) d'un pensionnat catholique de Nuku'alofa (Tonga), qui s'ennuient,
« empruntent » le bateau d'un pêcheur ; ni carte ni boussole ; ils s'endorment, tempête, voile déchirée,
gouvernail cassé ; 8 jours à la dérive sans nourriture, eau de pluie dans des coques de noix de coco partagée
à parts égales, une gorgée le matin et une le soir ; 'Ata, rocher inhabité depuis 1863 ; équipes de deux,
tableau de service pour le potager, la cuisine et la garde ; disputes réglées par une pause imposée ; le feu
entretenu sans jamais s'éteindre pendant plus d'un an ; Stephen tombe d'une falaise, jambe cassée, attelle de
bâtons et de feuilles, les autres font son travail ; secourus le dimanche 11 septembre 1966 par le capitaine
australien Peter Warner, qui a remarqué des zones brûlées sur les falaises ; « on pense être là depuis 15 mois » ;
on les croyait morts, des funérailles avaient eu lieu. Confirmé par la nécrologie de Peter Warner
(The Independent, 22 avril 2021). Golding, Sa Majesté des mouches, 1954.
Lien : série « L'État » (etat_2.py, Hobbes : « guerre de tous contre tous » ; etat_6.py, « Peut-on se passer de l'État ? »).
La dernière phrase relance la première (boucle).
"""
CODE = "ata"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"'Ata": "Ata", "Tonga": "Tonnga", "Hobbes": "Obbse", "Stephen": "Stivène",
                 "6": "six", "8": "huit", "2": "deux", "15": "quinze",
                 "1965": "mille neuf cent soixante-cinq", "1966": "mille neuf cent soixante-six"}
PASSAGES = [
    ("s1", "6 ados. Une île déserte. Pas d'adulte, pas de règles, pas d'État.", 0.3),
    ("s2", "Que va-t-il se passer ?", 0.4),
    ("s3", "Juin 1965, Tonga. 6 pensionnaires s'ennuient. Ils empruntent un bateau… sans demander.", 0.15),
    ("s4", "Pas de carte, pas de boussole. Et la nuit, la tempête.", 0.2),
    ("s5", "Voile déchirée, gouvernail cassé. 8 jours à la dérive, sans manger.", 0.2),
    ("s6", "L'eau de pluie ? Partagée : une gorgée le matin, une le soir.", 0.3),
    ("s7", "Puis un rocher surgit : 'Ata. Désert depuis un siècle.", 0.35),
    ("s8", "Dans le roman Sa Majesté des mouches, des enfants seuls sombrent dans la violence.", 0.3),
    ("s9", "Eux ? Équipes de 2. Potager, cuisine, tours de garde.", 0.2),
    ("s10", "Une dispute ? Pause obligatoire pour se calmer. Et le feu ne s'éteint jamais.", 0.25),
    ("s11", "Stephen tombe d'une falaise : jambe cassée. Les autres lui font une attelle… et travaillent à sa place.", 0.3),
    ("s12", "Septembre 1966. Un capitaine australien remarque des traces de feu sur les falaises.", 0.2),
    ("s13", "Chez eux, on les croyait morts. On avait célébré leurs funérailles.", 0.35),
    ("s14", "Ils ont tenu 15 mois. Ensemble.", 0.45),
    ("s15", "Hobbes l'affirmait : sans État, c'est la guerre de tous contre tous.", 0.25),
    ("s16", "Alors, Hobbes avait tort ? Pas si vite : 6 garçons, ce n'est pas un pays. Et ils ont recréé des règles.", 0.3),
    ("s17", "Peut-on se passer de l'État ? Vraie question de bac. La réponse est sur Révisions Animées.", 0.3),
    ("s18", "Et toi… sur cette île, tu aurais fait quoi ?", 0.0),
]
