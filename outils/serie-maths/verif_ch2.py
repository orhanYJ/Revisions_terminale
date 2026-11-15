"""Vérifie tous les calculs affichés ou dits dans la vidéo maths_ch2.py (relancer après toute modification des valeurs).

Usage : python3 outils/serie-maths/verif_ch2.py
"""
from fractions import Fraction as Fr
from math import sqrt, log, ceil, isclose


def premier_rang(u, ok, nmax=100000):
    """Plus petit N tel que ok(u(n)) pour tout n de N à nmax."""
    N = None
    for n in range(nmax, -1, -1):
        if not ok(u(n)):
            return n + 1
        N = n
    return N


# I. √n ≥ A ⇔ n ≥ A² : seuils 2, 4, 6 → rangs 4, 16, 36 ; A = 100 → 10 000
for A, N in ((2, 4), (4, 16), (6, 36), (100, 10000)):
    assert premier_rang(lambda n: sqrt(n), lambda x: x >= A, 20000) == N
# premiers termes dits : 0, 1, ≈1,4, ≈1,7, 2
assert [round(sqrt(n), 1) for n in range(5)] == [0, 1, 1.4, 1.7, 2]
# suite non majorée : n si pair, 0 sinon ; une infinité de termes sous le seuil 8
assert all((n if n % 2 == 0 else 0) == 0 for n in range(1, 1001, 2))

# II. bande : u(n) = 2 + 3(−1)ⁿ/(n + 1) ; ε = 1, 0,5, 0,2 → N = 3, 6, 15
u = lambda n: 2 + 3 * (-1) ** n / (n + 1)
for e, N in ((1, 3), (0.5, 6), (0.2, 15)):
    assert premier_rang(u, lambda x: abs(x - 2) < e, 2000) == N, e
# 1 + 1/n : 2 ; 1,5 ; ≈1,33 ; bande 0,25 autour de 1 dès le rang 5
assert [round(1 + 1 / n, 2) for n in (1, 2, 3)] == [2, 1.5, 1.33]
assert premier_rang(lambda n: 1 + 1 / n if n else 99, lambda x: abs(x - 1) < 0.25, 2000) == 5

# III. terme prépondérant : (3n² − n + 1)/(2n² + 5) → 3/2 ; u(1000) ≈ 1,4995
v = lambda n: (3 * n * n - n + 1) / (2 * n * n + 5)
assert round(v(1000), 4) == 1.4995 and abs(v(10 ** 7) - 1.5) < 1e-6
# n² − 5n = n²(1 − 5/n) ; √(n+1) − √n = 1/(√(n+1) + √n)
assert all(isclose(n * n - 5 * n, n * n * (1 - 5 / n)) for n in range(1, 100))
assert all(isclose(sqrt(n + 1) - sqrt(n), 1 / (sqrt(n + 1) + sqrt(n))) for n in range(1, 1000))
# 2n/n = 2 ; n² − n → +∞ ; n − n² → −∞
assert (10 ** 6) ** 2 - 10 ** 6 > 10 ** 11 and 10 ** 6 - (10 ** 6) ** 2 < -10 ** 11

# IV. gendarmes : 2 − 1/(n+1) ≤ 2 + (−1)ⁿ/(n+1) ≤ 2 + 1/(n+1) ; n + (−1)ⁿ ≥ n − 1
assert all(2 - 1 / (n + 1) <= 2 + (-1) ** n / (n + 1) <= 2 + 1 / (n + 1) for n in range(500))
assert all(n + (-1) ** n >= n - 1 for n in range(500))

# V. qⁿ ; Bernoulli 1,02ⁿ ≥ 1 + 0,02n ; 1 + 0,02n ≥ 100 ⇔ n ≥ 4950 ; 1,02ⁿ ≥ 100 dès n = 233
assert all(1.02 ** n >= 1 + 0.02 * n for n in range(5000))
assert min(n for n in range(10000) if 1 + Fr(2, 100) * n >= 100) == 4950
assert min(n for n in range(10000) if 1.02 ** n >= 100) == 233 == ceil(log(100) / log(1.02))
# a(n) = 15 − 10 × 0,8ⁿ → 15 ; (2ⁿ + 3ⁿ)/3ⁿ = (2/3)ⁿ + 1
assert abs(15 - 10 * 0.8 ** 200 - 15) < 1e-12
assert all(Fr(2 ** n + 3 ** n, 3 ** n) == Fr(2, 3) ** n + 1 for n in range(50))
# somme géométrique et Zénon : 1/2 + … + 1/2ⁿ = 1 − 1/2ⁿ ; n = 10 : 0,9990234375 > 0,999
for q in (Fr(1, 2), Fr(-1, 3), Fr(3, 4)):
    assert all(sum(q ** k for k in range(n + 1)) == (1 - q ** (n + 1)) / (1 - q) for n in range(30))
assert all(sum(Fr(1, 2 ** k) for k in range(1, n + 1)) == 1 - Fr(1, 2 ** n) for n in range(1, 40))
assert sum(Fr(1, 2 ** k) for k in range(1, 11)) == Fr(9990234375, 10 ** 10) and 0.9990234375 > 0.999
# ouverture : 1/2, 3/4, 7/8, 15/16
assert [1 - Fr(1, 2 ** k) for k in range(1, 5)] == [Fr(1, 2), Fr(3, 4), Fr(7, 8), Fr(15, 16)]

# VI. 1 − 1/(n+1) : 0, 1/2, 2/3, 3/4, croissante, majorée par 5, limite 1
w = [1 - Fr(1, n + 1) for n in range(200)]
assert w[:4] == [0, Fr(1, 2), Fr(2, 3), Fr(3, 4)] and all(w[i] < w[i + 1] < 5 for i in range(199))

# VII. √(x + 2) : ℓ² − ℓ − 2 = (ℓ − 2)(ℓ + 1) ; la suite tend vers 2
r = [1.0]
for _ in range(60):
    r.append(sqrt(r[-1] + 2))
assert all(0 <= r[i] <= r[i + 1] <= 2 for i in range(60)) and abs(r[-1] - 2) < 1e-12
assert all(l * l - l - 2 == (l - 2) * (l + 1) for l in range(-20, 20))

# VIII. seuil 0,9ⁿ < 0,01 → 44 ; 0,9⁴³ ≈ 0,0108 ; 0,9⁴⁴ ≈ 0,0097
def seuil(e):
    n, x = 0, 1
    while x >= e:
        n, x = n + 1, 0.9 * x
    return n
assert seuil(0.01) == 44 and round(0.9 ** 43, 4) == 0.0108 and round(0.9 ** 44, 4) == 0.0097
# Héron : sortie affichée
h, sortie = 1.0, []
for k in range(5):
    h = (h + 2 / h) / 2
    sortie.append(f"{k + 1} {h}")
assert sortie == ["1 1.5", "2 1.4166666666666665", "3 1.4142156862745097", "4 1.4142135623746899", "5 1.414213562373095"], sortie
assert repr(sqrt(2)).startswith("1.414213562373095")

# Exercice 1
a = lambda n: (n ** 3 - 2 * n) / (4 * n ** 3 + n ** 2)
assert abs(a(10 ** 6) - 0.25) < 1e-5 and all(isclose(a(n), (1 - 2 / n ** 2) / (4 + 1 / n)) for n in range(1, 200))
b = lambda n: (2 * n + 1) / (n * n + 1)
assert all(isclose(b(n), (2 + 1 / n) / (n * (1 + 1 / n ** 2))) for n in range(1, 200)) and b(10 ** 6) < 1e-5
assert abs(3 * 0.7 ** 200 - 5 + 5) < 1e-12
assert all(2 ** n - 3 ** n == 3 ** n * (Fr(2, 3) ** n - 1) for n in range(40))
assert all(4 <= 5 - (-1) ** n <= 6 for n in range(1, 100))
assert all(Fr(4, n) <= Fr(5 - (-1) ** n, n) <= Fr(6, n) for n in range(1, 100))

# Exercice 2 : u0 = 0, u(n+1) = (2u + 3)/(u + 4)
f = lambda x: (2 * x + 3) / (x + 4)
u1, u2 = f(Fr(0)), f(f(Fr(0)))
assert u1 == Fr(3, 4) and 2 * u1 + 3 == Fr(9, 2) and u1 + 4 == Fr(19, 4) and u2 == Fr(18, 19) and round(float(u2), 3) == 0.947
assert f(Fr(0)) == Fr(3, 4) and f(Fr(1)) == 1
# dérivée : 2(x + 4) − (2x + 3) = 5
assert all(2 * (x + 4) - (2 * x + 3) == 5 for x in range(-10, 10))
us = [Fr(0)]
for _ in range(12):
    us.append(f(us[-1]))
assert all(0 <= us[i] <= us[i + 1] <= 1 for i in range(12))
# f(ℓ) = ℓ ⇔ ℓ² + 2ℓ − 3 = 0 ⇔ (ℓ − 1)(ℓ + 3) = 0
assert all(l * l + 2 * l - 3 == (l - 1) * (l + 3) for l in range(-20, 20))
# suite auxiliaire : v(n+1) = v(n)/5, v0 = −1/3, u = (1 + 3v)/(1 − v)
vs = [(x - 1) / (x + 3) for x in us]
assert vs[0] == Fr(-1, 3) and all(vs[i + 1] == vs[i] / 5 for i in range(12))
assert all(vs[i] == Fr(-1, 3) * Fr(1, 5) ** i for i in range(13))
assert all((1 + 3 * vs[i]) / (1 - vs[i]) == us[i] for i in range(13))
# numérateur et dénominateur après multiplication par (u + 4)
for x in us[:6]:
    assert (2 * x + 3) - (x + 4) == x - 1 and (2 * x + 3) + 3 * (x + 4) == 5 * x + 15 == 5 * (x + 3)
# seuil 1 − u < 10⁻⁶ → 9
def seuil2():
    n, x = 0, 0
    while 1 - x >= 1e-6:
        x = (2 * x + 3) / (x + 4)
        n = n + 1
    return n
assert seuil2() == 9
assert 1 - float(us[8]) > 1e-6 > 1 - float(us[9])
print("verif_ch2 : tous les calculs sont justes.")
