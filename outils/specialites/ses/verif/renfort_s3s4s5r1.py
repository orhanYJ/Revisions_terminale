"""Recalcul des chiffres des chapitres S3, S4, S5 et R1 (site SES « Faits & Courbes »).

Sources : Insee Première n° 1739 (FQP 2014-2015, fichier ip1739.xls) ; Insee Première n° 2117 (niveaux de vie 2024) ;
Insee Première n° 2096 (marché du travail 2025) ; Insee Première n° 1929 (participation électorale 2022).
Lancer : python3 outils/specialites/ses/verif/renfort_s3s4s5r1.py  (s'arrête sur la première erreur).
"""

CAT = ["Agri", "ACCE", "Cadres", "PI", "EOQ", "EONQ"]
# Destinées des fils selon la catégorie du père, 2015, en % (lignes = père)
DEST_H = [
    [26.7, 7.9, 8.5, 20.4, 27.4, 9.1],
    [0.9, 20.6, 23.1, 23.8, 23.6, 7.9],
    [0.2, 7.9, 49.0, 25.4, 13.7, 3.8],
    [0.6, 7.8, 26.5, 31.1, 26.2, 7.7],
    [0.6, 7.2, 12.7, 26.8, 42.6, 10.1],
    [0.6, 6.5, 8.3, 18.7, 43.9, 22.1],
]
ENS_H = [2.8, 9.1, 20.4, 25.3, 32.4, 10.1]      # positions des fils
PERES = [8.3, 13.0, 13.9, 15.9, 35.6, 13.1]     # origines (pères)
FILS = [2.8, 9.1, 20.4, 25.3, 32.4, 10.1]
MERES = [7.9, 8.8, 4.8, 13.4, 30.3, 34.8]
FILLES = [1.3, 4.4, 15.2, 27.5, 30.0, 21.6]


def proche(a, b, tol, quoi):
    assert abs(a - b) <= tol, f"{quoi} : {a} au lieu de {b}"


def r1(x):
    return round(x + 1e-9, 1)


# 1. Les lignes de la table de destinée totalisent 100
for i, l in enumerate(DEST_H):
    proche(sum(l), 100, 0.15, f"ligne {CAT[i]}")

# 2. Table d'effectifs pour 1 000 fils (poids = origines des pères), puis table de recrutement
EFF = [[PERES[i] * DEST_H[i][j] / 100 * 10 for j in range(6)] for i in range(6)]
col = [sum(EFF[i][j] for i in range(6)) for j in range(6)]
for j in range(6):
    proche(col[j] / 10, ENS_H[j], 0.35, f"marge fils {CAT[j]}")
REC = [[100 * EFF[i][j] / col[j] for j in range(6)] for i in range(6)]
print("Table d'effectifs (sur 1 000 fils) :")
for i in range(6):
    print(CAT[i].ljust(6), [round(x) for x in EFF[i]], round(sum(EFF[i])))
print("Total colonnes :", [round(c) for c in col])
print("Recrutement (en % de chaque colonne) :")
for i in range(6):
    print(CAT[i].ljust(6), [r1(x) for x in REC[i]])
# Valeurs citées dans le cours
proche(r1(REC[2][2]), 33.5, 0.05, "fils cadres de père cadre (recrutement)")
proche(r1(REC[4][2] + REC[5][2]), 27.6, 0.05, "cadres fils d'employés ou ouvriers")
proche(r1(REC[0][0]), 80.6, 0.05, "agriculteurs fils d'agriculteurs")

# 3. Immobilité (diagonale pondérée) et mobilité observée
immob = sum(PERES[i] * DEST_H[i][i] / 100 for i in range(6))
print("Immobilité recalculée :", round(immob, 1), "(Insee : 34,8)")
proche(immob, 34.8, 0.3, "immobilité des hommes")

# 4. Mobilité structurelle = indice de dissimilarité
ms_h = sum(abs(a - b) for a, b in zip(PERES, FILS)) / 2
ms_f = sum(abs(a - b) for a, b in zip(MERES, FILLES)) / 2
proche(ms_h, 15.8, 0.05, "mobilité structurelle hommes")
proche(ms_f, 24.5, 0.05, "mobilité structurelle femmes")
proche(100 * 15.8 / 65.2, 24.2, 0.05, "part structurelle hommes")
proche(100 * 24.5 / 70.5, 34.8, 0.05, "part structurelle femmes")

# 5. Rapport des chances relatives (odds ratio) cadres / employés-ouvriers non qualifiés
orr = (DEST_H[2][2] / DEST_H[2][5]) / (DEST_H[5][2] / DEST_H[5][5])
print("Odds ratio recalculé sur la table arrondie :", round(orr, 1), "(Insee : 34,7)")
proche(orr, 34.7, 1.0, "odds ratio")
proche(49.0 / 8.3, 5.9, 0.05, "rapport des chances brut cadre")

# 6. Exercice « table d'effectifs » de l'animation (table fictive de 1 000 personnes)
FICT = [[60, 25, 15], [100, 150, 50], [40, 225, 335]]  # origines : haut, milieu, bas ; positions : haut, milieu, bas
orig = [sum(l) for l in FICT]
pos = [sum(FICT[i][j] for i in range(3)) for j in range(3)]
assert orig == [100, 300, 600] and pos == [200, 400, 400], (orig, pos)
diag = sum(FICT[i][i] for i in range(3))
assert diag == 545
assert sum(abs(a - b) for a, b in zip(orig, pos)) / 2 == 200
proche(100 * 60 / 100, 60, 0, "destinée haut/haut")
proche(100 * 60 / 200, 30, 0, "recrutement haut/haut")
proche(100 * 335 / 600, 55.8, 0.05, "destinée bas/bas")
proche(100 * 335 / 400, 83.75, 0.001, "recrutement bas/bas")
proche((60 / 15) / (40 / 335), 33.5, 0.05, "odds ratio fictif")

# 7. Lorenz et Gini 2024 (parts cumulées, Insee IP 2117) — Gini approché par trapèzes
pts = [(0, 0), (20, 8.4), (40, 21.9), (50, 30.1), (80, 61.2), (90, 75.1), (100, 100)]
aire = sum((x2 - x1) * (y1 + y2) / 2 for (x1, y1), (x2, y2) in zip(pts, pts[1:])) / 10000
g = 1 - 2 * aire
print("Gini approché par la courbe de Lorenz 2024 :", round(g, 3), "(Insee : 0,302, calculé sur les données individuelles)")
assert 0.26 < g < 0.31
proche((100 - 61.2) / 8.4, 4.62, 0.01, "S80/S20 2024")
proche(48580 / 13970, 3.48, 0.005, "D9/D1 2024")
proche(100 - 75.1, 24.9, 0.01, "part des 10 % les plus aisés")

# 8. Société fictive de cinq personnes de l'animation Lorenz
def gini(revenus):
    r = sorted(revenus)
    n = len(r)
    s = sum(r)
    cum, aire = 0, 0
    for x in r:
        aire += (2 * cum + x) / (2 * s * n)
        cum += x
    return 1 - 2 * aire


for revs, attendu in [([20, 20, 20, 20, 20], 0.0), ([10, 15, 20, 25, 30], 0.2), ([5, 10, 15, 20, 50], 0.4), ([2, 4, 8, 16, 70], 0.592)]:
    proche(gini(revs), attendu, 0.0005, f"Gini fictif {revs}")

# 9. S4 : marché du travail 2025 (IP 2096)
proche(5.3 + 2.1 + 0.1 + 1.8, 9.3, 0.05, "CDD + intérim (somme des arrondis)")  # Insee publie 9,4 % (arrondi des valeurs exactes)
proche(5.8 + 4.5, 10.3, 0.01, "chômage + halo")
proche(26.6 / 9.2, 2.9, 0.05, "temps partiel femmes / hommes")

# 10. S5 : écarts de vote systématique selon le diplôme (IP 1929)
proche(43.7 - 28.8, 14.9, 0.01, "écart de vote systématique 2022")
proche(30.4 - 9.5, 20.9, 0.01, "écart d'abstention systématique 2022")
proche(50.3 / 17.0, 3.0, 0.05, "abstention systématique jeunes sans diplôme / diplômés")

# 11. R1 : redistribution
proche(5.89 / 3.48, 1.69, 0.01, "D9/D1 divisé par la redistribution")
proche(0.378 - 0.302, 0.076, 0.0001, "baisse du Gini par la redistribution")
proche(716300 / 4400, 162.8, 0.1, "D9/D1 du patrimoine brut 2021")
print("Toutes les vérifications passent.")
