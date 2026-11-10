"""Vérifie tous les calculs affichés ou dits dans la vidéo maths_ch1.py (relancer après toute modification des valeurs).

Usage : python3 outils/serie-maths/verif_ch1.py
"""
from fractions import Fraction as Fr
from math import sqrt, isqrt


def premier(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


# modèle de rédaction : u0 = 1, u(n+1) = 2 u(n) + 3, u(n) = 2^(n+2) - 3
u = [1]
for _ in range(7):
    u.append(2 * u[-1] + 3)
assert u == [2 ** (n + 2) - 3 for n in range(8)] == [1, 5, 13, 29, 61, 125, 253, 509]
# l'hérédité, calcul symbolique sur quelques k : 2(2^(k+2) - 3) + 3 = 2^(k+3) - 3
assert all(2 * (2 ** (k + 2) - 3) + 3 == 2 ** (k + 3) - 3 for k in range(50))
# 2^n n'est jamais divisible par 3 ; l'hérédité est vraie (2^k = 3m => 2^(k+1) = 3 × 2m)
assert all(2 ** n % 3 for n in range(200))
# Euler : n² + n + 41 premier pour n = 0…39, pas pour n = 40
assert all(premier(n * n + n + 41) for n in range(40))
assert 40 ** 2 + 40 + 41 == 1681 == 41 * 41 and not premier(1681)
assert [n * n + n + 41 for n in (0, 1, 2, 39)] == [41, 43, 47, 1601]
# somme des impairs
assert all(sum(2 * k - 1 for k in range(1, n + 1)) == n * n for n in range(1, 200))
assert [sum(range(1, 2 * n, 2)) for n in range(1, 6)] == [1, 4, 9, 16, 25]
assert all(k * k + 2 * k + 1 == (k + 1) ** 2 for k in range(100))
# somme des carrés (énoncé) et des entiers
assert all(sum(k * k for k in range(1, n + 1)) == n * (n + 1) * (2 * n + 1) // 6 for n in range(1, 100))
assert 1 + 4 + 9 == 14 == 3 * 4 * 7 // 6
# u0 = 1, u(n+1) = √(u(n) + 2) : croissante, entre 0 et 2
v = [1.0]
for _ in range(8):
    v.append(sqrt(v[-1] + 2))
assert all(0 <= v[i] <= v[i + 1] <= 2 for i in range(8))
assert round(v[1], 2) == 1.73 and round(sqrt(2), 2) == 1.41 and sqrt(4) == 2
print("toile √(x+2) :", [round(x, 3) for x in v[:6]])
# Bernoulli : 1,05^20 ≈ 2,65 ≥ 1 + 20 × 0,05 = 2
assert round(1.05 ** 20, 2) == 2.65 and abs(1 + 20 * 0.05 - 2) < 1e-12
assert all((1 + a) ** n >= 1 + n * a - 1e-12 for a in (0, .05, .3, 1, 2.5) for n in range(30))
# (1 + ka)(1 + a) = 1 + (k+1)a + ka²
for k in range(10):
    for a in (Fr(1, 3), Fr(2), Fr(5, 7)):
        assert (1 + k * a) * (1 + a) == 1 + (k + 1) * a + k * a * a
print("Bernoulli a = 0,05 :", [(n, round(1.05 ** n, 3), round(1 + .05 * n, 2)) for n in (0, 5, 10, 15, 20)])
# 2^n et n² : faux pour n = 3, vrai pour n ≥ 4
tab = [(n, 2 ** n, n * n) for n in range(7)]
assert [x[1] >= x[2] for x in tab] == [True, True, True, False, True, True, True]
assert all(2 ** n >= n * n for n in range(4, 300))
assert all(2 * k * k >= (k + 1) ** 2 for k in range(3, 300)) and 2 * 2 * 2 < 3 ** 2
assert all(k * k - 2 * k - 1 == (k - 1) ** 2 - 2 for k in range(100))
# encadrer sans croissance de f : u(k+1) = 0,5 u(k) + 1, u(k) ≤ 2 => u(k+1) ≤ 2
assert 0.5 * 2 + 1 == 2
# deviner puis prouver : u0 = 0, u(n+1) = u(n) + 2n + 1 => u(n) = n²
w = [0]
for n in range(10):
    w.append(w[-1] + 2 * n + 1)
assert w == [n * n for n in range(11)]
# exercice 1 : u0 = 2, u(n+1) = u(n) + 2n + 3 ; u(n) = (n+1)² + 1 ; u10 = 122
e = [2]
for n in range(12):
    e.append(e[-1] + 2 * n + 3)
assert e[:4] == [2, 5, 10, 17] and e == [(n + 1) ** 2 + 1 for n in range(13)] and e[10] == 122
assert all((k + 1) ** 2 + 1 + 2 * k + 3 == k * k + 4 * k + 5 == (k + 2) ** 2 + 1 for k in range(100))
# exercice 2 (type bac) : a0 = 5, a(n+1) = 0,8 a(n) + 3 ; a(n) = 15 − 10 × 0,8^n ; seuil 14 au mois 11
a = [Fr(5)]
for n in range(15):
    a.append(Fr(4, 5) * a[-1] + 3)
assert a[1] == 7 and a[2] == Fr(43, 5)
assert all(a[n] == 15 - 10 * Fr(4, 5) ** n for n in range(16))
assert all(5 <= a[n] <= a[n + 1] <= 15 for n in range(15))
assert Fr(4, 5) * 5 + 3 == 7 and Fr(4, 5) * 15 + 3 == 15
# v(n+1) = a(n+1) − 15 = 0,8 a(n) − 12 = 0,8 (a(n) − 15)
assert all(a[n + 1] - 15 == Fr(4, 5) * (a[n] - 15) for n in range(15))
assert round(float(a[10]), 2) == 13.93 and round(float(a[11]), 2) == 14.14
assert round(0.8 ** 10, 3) == 0.107 and round(0.8 ** 11, 3) == 0.086
n, x = 0, 5
while x <= 14:
    x = 0.8 * x + 3
    n += 1
assert n == 11
print("abonnés :", [round(float(z), 2) for z in a[:12]])
print("tous les calculs sont justes")
