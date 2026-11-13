"""Vérifie tous les calculs affichés ou dits dans la vidéo maths_ch3.py (relancer après toute modification des valeurs).

Usage : python3 outils/serie-maths/verif_ch3.py
"""
import math
import re
import sys
from math import cos, exp, sin, sqrt

sys.path.insert(0, "outils/serie-maths")
import maths_ch3 as M  # noqa: E402


def f1(x):
    return (2 * x + 1) / (x - 1)


# ouverture : f(1000) ≈ 2,003 ; f(10⁶) ≈ 2,000003 ; f(1,001) = 3002 ; f(0,999) = −2998
assert round(f1(1000), 3) == 2.003 and round(f1(10 ** 6), 6) == 2.000003
assert round(f1(1.001)) == 3002 and round(f1(0.999)) == -2998
assert abs(f1(1.1) - 32) < 1e-9
# bornes des branches tracées : f = −6 en 5/8, f = 10 en 11/8
assert abs(f1(0.625) + 6) < 1e-12 and abs(f1(1.375) - 10) < 1e-12
# sortie Python affichée (copiée du site) : on la recalcule
attendu = "10 2.3333333333333335\n1000 2.003003003003003\n1000000 2.000003000003\n1.1 31.999999999999975\n1.001 3002.0000000003306\n0.999 -2997.9999999999977"
obtenu = "\n".join(f"{x} {f1(x)}" for x in [10, 1000, 10 ** 6, 1.1, 1.001, 0.999])
assert obtenu == attendu, obtenu
# seuil : x²/4 ≥ 9 dès x = 6
assert 6 * 6 / 4 == 9
# 1/0,001 = 1000
assert round(1 / 0.001) == 1000
# h(x) = (x² + 3x)/(x² − 4) en 2 : numérateur 10 ; h(2,001) ≈ 2501 ; h(1,999) ≈ −2499
h = lambda x: (x * x + 3 * x) / (x * x - 4)
assert 2 * 2 + 3 * 2 == 10 and round(h(2.001)) == 2501 and round(h(1.999)) == -2499
# limite finie : 2² + 1 = 5
assert 2 ** 2 + 1 == 5
# formes indéterminées : x² − x, x − x², (x + 3) − x
assert 1e6 ** 2 - 1e6 > 1e11 and 1e6 - 1e6 ** 2 < -1e11 and (1e6 + 3) - 1e6 == 3
# (3x² + 1)/(x² − 5x) → 3 en −∞
q = lambda x: (3 * x * x + 1) / (x * x - 5 * x)
assert abs(q(-1e8) - 3) < 1e-6
# x³ et 2x en 0,01
assert abs(0.01 ** 3 - 1e-6) < 1e-15 and 2 * 0.01 == 0.02
# (x² − 1)/(x − 1) → 2 ; (eˣ − 1)/x → 1
assert abs((1.000001 ** 2 - 1) / 0.000001 - 2) < 1e-5 and abs((exp(1e-6) - 1) / 1e-6 - 1) < 1e-5
# compositions : e^(1/x) → 1, √(1 − 2x) → +∞, e^(−x²) → 0
assert abs(exp(1 / 1e9) - 1) < 1e-8 and sqrt(1 - 2 * (-1e12)) > 1e6 and exp(-(30 ** 2)) < 1e-300
# gendarmes, comparaison
assert all(-1 / x <= cos(x) / x <= 1 / x for x in [0.9 + k * 0.1 for k in range(500)])
assert all(x + cos(x) >= x - 1 for x in [k * 0.1 for k in range(500)])
# démonstration : eˣ − x a un minimum 1 en 0
assert all(exp(x) - x >= 1 - 1e-12 for x in [-20 + k * 0.01 for k in range(4000)])
# duel : 10^10, e^10 ≈ 22 026, 100^10 = 10^20, e^100 ≈ 2,7 × 10^43
assert 10 ** 10 == 10_000_000_000 and round(exp(10)) == 22026 and 100 ** 10 == 10 ** 20
assert round(exp(100) / 1e43, 1) == 2.7
# dichotomie du site : 35,7715
a, b = 11, 100
for k in range(50):
    m = (a + b) / 2
    if math.exp(m) > m ** 10:
        b = m
    else:
        a = m
assert round(b, 4) == 35.7715
# étape 1 : eˣ − x²/2 ≥ 1 sur [0 ; +∞[ ; étape 2 : identité
assert all(exp(x) - x * x / 2 >= 1 - 1e-12 for x in [k * 0.01 for k in range(3000)])
for n in (1, 2, 3, 5):
    for x in (1.0, 7.5, 20.0):
        assert abs(exp(x) / x ** n - (1 / n ** n) * (exp(x / n) / (x / n)) ** n) < 1e-9 * exp(x) / x ** n
        X = x  # x^n e^x en −x : (−X)^n e^(−X) = (−1)^n X^n e^(−X)
        assert abs((-X) ** n * exp(-X) - (-1) ** n * X ** n * exp(-X)) < 1e-15
# x² e^(−x) : maximum 4e^(−2) ≈ 0,541 en 2
assert abs(4 * exp(-2) - 0.5413) < 1e-4
# bac 2026 : (x + 1)e^(−x) → 0
assert (1e3 + 1) * exp(-1e3) < 1e-300
# exercice 1 : f(x) = (4x − 3)/(2x + 1)
g1 = lambda x: (4 * x - 3) / (2 * x + 1)
assert 4 * (-0.5) - 3 == -5 and abs(g1(1e9) - 2) < 1e-6 and g1(-0.5 + 1e-6) < -1e5 and g1(-0.5 - 1e-6) > 1e5
assert 3 - exp(-5) < 3
# exercice 2 : f(x) = (2x − 1)eˣ
fb = lambda x: (2 * x - 1) * exp(x)
d = lambda x: (fb(x + 1e-6) - fb(x - 1e-6)) / 2e-6
assert all(abs(d(x) - (2 * x + 1) * exp(x)) < 1e-5 for x in (-3, -0.5, 0, 1))
assert round(-2 * exp(-0.5), 3) == -1.213 and abs(fb(-0.5) - M.MIN_FB) < 1e-4 and fb(0.5) == 0
assert abs(fb(-60)) < 1e-20 and fb(-3) < 0 and fb(1) > 0
assert fb(1.13) < 4.2

# le texte lu : jamais « il y a » (« y » isolé est l'ordonnée pour la voix), nombres en lettres
lu = " ".join(b if isinstance(b, str) else (b[0] if isinstance(b[0], str) and b[0] not in ("P", "C") else "")
              for s in M.SCENES for b in s["beats"])
lu = re.sub(r"\{[^}]*\}", "", lu)
assert not re.search(r"\by a\b|\by avoir\b", lu), "« y a » dans le texte lu"
assert not re.search(r"\d", lu), re.findall(r".{20}\d.{20}", lu)
print("ok : tous les calculs de maths_ch3 sont justes")
