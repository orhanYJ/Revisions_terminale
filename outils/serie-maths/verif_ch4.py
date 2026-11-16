"""Vérifie tous les calculs affichés ou dits dans la vidéo maths_ch4.py (relancer après toute modification des valeurs).

Recalcule les dérivées (contrôle numérique par différences centrées), les valeurs, les limites, les encadrements, les
sorties des programmes Python (code réexécuté), les données des graphiques (M.OUV, M.X2N, M.FBAC…), les étapes de la
dichotomie dessinées par maths/serie/illu-maths-ch4.js (SERIE_ILLU.dicho) et les itérés de Newton ; puis contrôle le
texte lu (nombres en lettres, pas de « y » isolé, pas de « il y a », de « tout x », de « deux x »…).
Toutes les erreurs sont listées (pas d'arrêt à la première).

Usage : python3 outils/serie-maths/verif_ch4.py
"""
import contextlib
import io
import math
import re
import sys
from math import exp, sqrt

sys.path.insert(0, "outils/serie-maths")
import maths_ch4 as M  # noqa: E402

ERR = []


def check(cond, msg):
    if not cond:
        ERR.append(msg)


def proche(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def sur_courbe(pts, F, tol=1.5e-4):
    """Points arrondis à 10⁻⁴ (abscisse et ordonnée) : on tolère l'arrondi."""
    return all(abs(p[1] - F(p[0])) <= tol * max(1.0, abs(F(p[0]))) for p in pts)


def deriv(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def deriv2(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def meme_derivee(f, fp, xs, nom, tol=1e-5, ordre=1):
    d = deriv if ordre == 1 else deriv2
    for x in xs:
        num = d(f, x)
        check(abs(num - fp(x)) <= tol * max(1.0, abs(fp(x))), f"{nom} : dérivée{'' if ordre == 1 else ' seconde'} fausse en {x} ({num} ≠ {fp(x)})")


def sortie(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, {})
    return buf.getvalue().rstrip("\n")


V = {k: v for s in M.SCENES for k, v in s["vis"].items()}
XS = [-1.7, -0.9, -0.3, 0.2, 0.8, 1.3, 2.1]
XP = [0.2, 0.7, 1.5, 3.0, 8.0]          # x > 0

# ---------------------------------------------------------------- ouverture : x³ + x − 1
check(M.CUBE(0) == -1 and M.CUBE(1) == 1 and 1 + 1 - 1 == 1, "ouverture : f(0) = −1, f(1) = 1")
check(sur_courbe(M.OUV, M.CUBE), "OUV ≠ x³ + x − 1")
check(M.OUV[0][0] == -0.4 and M.OUV[-1][0] == 1.2, "OUV : bornes")

# ---------------------------------------------------------------- I. composées
meme_derivee(lambda x: exp(-x * x), lambda x: -2 * x * exp(-x * x), XS, "e^(−x²)")
meme_derivee(lambda x: (3 * x + 1) ** 5, lambda x: 15 * (3 * x + 1) ** 4, XS, "(3x+1)^5")
check(5 * 3 == 15, "5 × 3 = 15")
meme_derivee(lambda x: sqrt(x * x + 1), lambda x: x / sqrt(x * x + 1), XS, "√(x²+1)")
meme_derivee(lambda x: sqrt(x * x + 1), lambda x: 2 * x / (2 * sqrt(x * x + 1)), XS, "√(x²+1) non simplifiée")
k = lambda x: exp(2 * x) * (x - 1) ** 3
meme_derivee(k, lambda x: 2 * exp(2 * x) * (x - 1) ** 3 + exp(2 * x) * 3 * (x - 1) ** 2, XS, "k avant factorisation")
meme_derivee(k, lambda x: exp(2 * x) * (x - 1) ** 2 * (2 * (x - 1) + 3), XS, "k factorisée (étape)")
meme_derivee(k, lambda x: exp(2 * x) * (x - 1) ** 2 * (2 * x + 1), XS, "k′ = e^(2x)(x−1)²(2x+1)")
meme_derivee(lambda x: exp(2 * x), lambda x: 2 * exp(2 * x), XS, "(e^(2x))′")
meme_derivee(lambda x: (x - 1) ** 3, lambda x: 3 * (x - 1) ** 2, XS, "((x−1)³)′")
meme_derivee(lambda x: exp(3 * x * x), lambda x: 6 * x * exp(3 * x * x), [-0.9, -0.3, 0.2, 0.8], "piège e^(3x²)")
check(not all(abs(deriv(lambda x: exp(3 * x * x), x) - exp(3 * x * x)) < 1e-3 for x in [0.2, 0.8]), "piège : e^(3x²) n'est pas sa dérivée")
# formules du tableau : (eᵘ)′, (uⁿ)′, (√u)′, (1/u)′ sur u(x) = x² + x + 2 (> 0, jamais nulle)
u, up = (lambda x: x * x + x + 2), (lambda x: 2 * x + 1)
meme_derivee(lambda x: exp(u(x)), lambda x: up(x) * exp(u(x)), XS, "(eᵘ)′")
for n in (1, 2, 3, 5):
    meme_derivee(lambda x, n=n: u(x) ** n, lambda x, n=n: n * up(x) * u(x) ** (n - 1), XS, f"(uⁿ)′ n={n}")
meme_derivee(lambda x: sqrt(u(x)), lambda x: up(x) / (2 * sqrt(u(x))), XS, "(√u)′")
meme_derivee(lambda x: 1 / u(x), lambda x: -up(x) / u(x) ** 2, XS, "(1/u)′")
# « pour comprendre » : produit de deux taux
for x in (0.3, 1.1):
    for hh in (1e-3, -1e-4):
        g = (exp(u(x + hh)) - exp(u(x))) / hh
        p = (exp(u(x + hh)) - exp(u(x))) / (u(x + hh) - u(x)) * (u(x + hh) - u(x)) / hh
        check(proche(g, p, 1e-9), "taux d'accroissement : produit de deux taux")

# ---------------------------------------------------------------- II. dérivée seconde de x eˣ
f = lambda x: x * exp(x)
meme_derivee(f, lambda x: (x + 1) * exp(x), XS, "(x eˣ)′")
meme_derivee(f, lambda x: (x + 2) * exp(x), XS, "(x eˣ)″", tol=1e-4, ordre=2)
meme_derivee(lambda x: (x + 1) * exp(x), lambda x: exp(x) + (x + 1) * exp(x), XS, "f″ avant factorisation")

# ---------------------------------------------------------------- III. convexité
meme_derivee(lambda x: x * x, lambda x: 2.0, XS, "(x²)″", tol=1e-4, ordre=2)
meme_derivee(exp, exp, XS, "(eˣ)″", tol=1e-4, ordre=2)
meme_derivee(sqrt, lambda x: -1 / (4 * x * sqrt(x)), XP, "(√x)″", tol=1e-4, ordre=2)
meme_derivee(lambda x: x ** 3, lambda x: 6 * x, XS, "(x³)″", tol=1e-4, ordre=2)
meme_derivee(lambda x: exp(-x), lambda x: exp(-x), XS, "(e^(−x))″", tol=1e-4, ordre=2)
check(all(exp(-a) > exp(-b) for a, b in [(-1, 0), (0, 2), (2, 4)]), "e^(−x) décroissante")
# convexe : courbe sous les cordes, au-dessus des tangentes ; concave pour √
for F, D, a, b in [(exp, exp, -1.6, 1.8), (lambda x: x * x, lambda x: 2 * x, -1, 2)]:
    for t in [i / 10 for i in range(1, 10)]:
        xm = a + t * (b - a)
        check(F(xm) <= F(a) + t * (F(b) - F(a)) + 1e-12, "convexe : sous la corde")
    for x0 in (-1.5, -0.5, 0.5, 1.4):
        check(all(F(x) >= F(x0) + D(x0) * (x - x0) - 1e-12 for x in [-3 + j * 0.05 for j in range(110)]), "au-dessus des tangentes")
check(all(sqrt(x) <= sqrt(x0) + (x - x0) / (2 * sqrt(x0)) + 1e-12 for x0 in (0.35, 2, 9) for x in [j * 0.05 for j in range(200)]),
      "√ concave : sous ses tangentes")
# données des graphiques
check(sur_courbe(M.EXPM, lambda x: exp(-x)) and max(p[1] for p in M.EXPM) <= 4.6, "EXPM")
check(sur_courbe(M.X4, lambda x: x ** 4) and max(p[1] for p in M.X4) <= 3.8, "X4")
check(sur_courbe(M.EXP, exp) and max(p[1] for p in M.EXP) <= 7.6, "EXP")
check(sur_courbe(M.RAC, sqrt), "RAC")
# Polynésie 16 juin 2026, affirmation 2 : x eˣ convexe sur [−2 ; +∞[, concave sur ]−∞ ; −2]
check(all((x + 2) * exp(x) >= 0 for x in [-2 + j * 0.1 for j in range(60)]), "Polynésie : g″ ≥ 0 sur [−2 ; +∞[")
check(all((x + 2) * exp(x) <= 0 for x in [-8 + j * 0.1 for j in range(61)]), "Polynésie : g″ ≤ 0 sur ]−∞ ; −2]")

# ---------------------------------------------------------------- IV. inflexion
check(deriv2(lambda x: x ** 3, -0.5) < 0 < deriv2(lambda x: x ** 3, 0.5) and abs(deriv(lambda x: x ** 3, 0)) < 1e-9, "x³ : inflexion en O, tangente y = 0")
check(all(12 * x * x >= 0 for x in XS) and 12 * 0 ** 2 == 0, "x⁴ : f″ = 12x² ≥ 0, nulle en 0")
meme_derivee(lambda x: x ** 4, lambda x: 12 * x * x, XS, "(x⁴)″", tol=1e-4, ordre=2)
g = lambda x: x ** 3 - 3 * x * x + 2
meme_derivee(g, lambda x: 3 * x * x - 6 * x, XS, "g′")
meme_derivee(g, lambda x: 6 * x - 6, XS, "g″", tol=1e-4, ordre=2)
check(g(1) == 0 and 1 - 3 + 2 == 0 and 6 * 0.9 - 6 < 0 < 6 * 1.1 - 6, "g : inflexion en (1 ; 0)")
# Asie 10 juin 2026, affirmation 1 : (−x/2 + 3)⁵, f″ = 5(−x/2 + 3)³, négative pour x > 6
fa = lambda x: (-x / 2 + 3) ** 5
meme_derivee(fa, lambda x: -2.5 * (-x / 2 + 3) ** 4, XS + [6.5, 8], "Asie f′")
meme_derivee(fa, lambda x: 5 * (-x / 2 + 3) ** 3, XS + [6.5, 8], "Asie f″", tol=1e-4, ordre=2)
check(5 * (-7 / 2 + 3) ** 3 < 0 and -6 / 2 + 3 == 0, "Asie : f″ < 0 pour x > 6, affirmation fausse")

# ---------------------------------------------------------------- V. démonstration et inégalités
for F, D, a in [(exp, exp, 0.3), (lambda x: x ** 4, lambda x: 4 * x ** 3, -0.7)]:
    gg = lambda x: F(x) - (D(a) * (x - a) + F(a))
    check(gg(a) == 0 and all(gg(x) >= -1e-12 for x in [-3 + j * 0.05 for j in range(120)]), "démo : g ≥ 0, minimum 0 en a")
check(exp(0) == 1, "tangente de exp en 0 : y = x + 1")
check(all(exp(x) >= x + 1 for x in [-30 + j * 0.05 for j in range(1000)]), "eˣ ≥ x + 1")
check(proche(1 / (2 * sqrt(1)), 0.5) and sqrt(1) == 1, "tangente de √ en 1 : y = x/2 + 1/2")
check(all(sqrt(x) <= (x + 1) / 2 + 1e-15 for x in [j * 0.01 for j in range(2000)]) and sqrt(9) == 3 and (9 + 1) / 2 == 5,
      "√x ≤ (x+1)/2 ; 3 ≤ 5")
check(all((1 + 1 / n) ** n <= math.e for n in range(1, 2000)) and round(math.e, 3) == 2.718, "(1 + 1/n)ⁿ ≤ e ≈ 2,718")
# droites des graphiques g_exp et g_rac : ce sont bien les tangentes
for nom, fd in [("g_exp", lambda x: x + 1), ("g_rac", lambda x: x / 2 + 0.5)]:
    for el in V[nom]["el"]:
        if el["type"] == "droite":
            for x, y in el["pts"]:
                check(proche(y, fd(x), 1e-6), f"{nom} : la droite tracée passe par ({x} ; {y}) au lieu de ({x} ; {fd(x)})")
check([9, 3] in V["g_rac"]["el"][3]["pts"] and [9, 5] in V["g_rac"]["el"][3]["pts"], "g_rac : points (9 ; 3) et (9 ; 5)")

# ---------------------------------------------------------------- VI. continuité
check(math.floor(0.5) == 0 and math.floor(0.999) == 0 and math.floor(1) == 1, "partie entière : E = 0 sur [0 ; 1[, E(1) = 1")
check(abs(deriv(abs, 1e-3) - 1) < 1e-6 and abs(deriv(abs, -1e-3) + 1) < 1e-6, "|x| : pentes −1 et 1")
check(2 ** 2 + 1 == 5, "f(2) = 5")

# ---------------------------------------------------------------- VII. TVI
check(sur_courbe(M.SAUT_G, lambda x: x / 2) and sur_courbe(M.SAUT_D, lambda x: x / 2 + 1.5), "SAUT")
check(M.SAUT_G[0][1] == 0 and M.SAUT_D[-1][1] == 2.5 and M.SAUT_G[-1][1] < 1.2 < M.SAUT_D[0][1] == 2.0,
      "saut : de 0 à 2,5, 1,2 jamais atteint")
check(M.G3(-2) == -1 and M.G3(2) == 3 and sur_courbe(M.TVI3, M.G3), "x³ − 3x + 1 : f(−2) = −1, f(2) = 3")
racines = sorted(2 * math.cos(math.radians(a)) for a in (40, 160, 280))      # x = 2cos θ, cos 3θ = −1/2
check(all(abs(M.G3(r)) < 1e-12 for r in racines), "racines de x³ − 3x + 1")
pts = [p for el in V["g_trois"]["el"] if el["type"] == "points" and el.get("c") == "ca" for p in el["pts"]]
check(len(pts) == 3 and all(abs(p[0] - r) < 1e-4 and p[1] == 0 for p, r in zip(sorted(pts), racines)),
      f"g_trois : racines affichées {sorted(pts)} ≠ {[round(r, 4) for r in racines]}")
check(abs(deriv(M.G3, -1)) < 1e-6 and abs(deriv(M.G3, 1)) < 1e-6 and M.G3(-1) > M.G3(1), "x³ − 3x + 1 : monte, redescend (−1), remonte (1)")
check(M.CUBE(0) < 0 < M.CUBE(1) and all(3 * x * x + 1 > 0 for x in XS), "rédaction type : f′ = 3x² + 1 > 0")
meme_derivee(M.CUBE, lambda x: 3 * x * x + 1, XS, "(x³ + x − 1)′")
a, b = 0.0, 1.0
for _ in range(60):
    m = (a + b) / 2
    a, b = (a, m) if M.CUBE(a) * M.CUBE(m) <= 0 else (m, b)
ALPHA = a
check(round(ALPHA, 4) == 0.6823, "α ≈ 0,6823")

# ---------------------------------------------------------------- VIII. dichotomie (illustration SERIE_ILLU.dicho, n = 6)
etapes, milieux = [(0.0, 1.0)], []
for _ in range(V["dic"]["n"] - 1):
    a, b = etapes[-1]
    m = (a + b) / 2
    milieux.append((m, M.CUBE(m)))
    etapes.append((a, m) if M.CUBE(a) * M.CUBE(m) <= 0 else (m, b))
check(etapes == [(0, 1), (0.5, 1), (0.5, 0.75), (0.625, 0.75), (0.625, 0.6875), (0.65625, 0.6875)], f"dichotomie : {etapes}")
check([s < 0 for _, s in milieux] == [True, False, True, False, True], "dichotomie : signes de f(m) dits (−, +, −, +, −)")
check([m for m, _ in milieux] == [0.5, 0.75, 0.625, 0.6875, 0.65625], "dichotomie : milieux dits")
check(etapes[-1][0] < ALPHA < etapes[-1][1], "α dans le dernier intervalle")
check(2 ** 10 == 1024 and 1 / 2 ** 10 < 1e-3 < 1 / 2 ** 9, "dix étapes : 1/1024 < 10⁻³")
code_d = "\n".join(V["py_d"]["lignes"])
check(sortie(code_d) == V["py_d"]["sortie"], f"py_d : sortie {sortie(code_d)!r}")
r = eval(V["py_d"]["sortie"])
check(math.floor(r[0] * 1000) == 681 and math.ceil(r[1] * 1000) == 683 and r[0] < ALPHA < r[1], "0,681 < α < 0,683")
pas = 0
a, b = 0, 1
while b - a > 0.001:
    m = (a + b) / 2
    a, b = (a, m) if M.CUBE(a) * M.CUBE(m) <= 0 else (m, b)
    pas += 1
check(pas == 10, "dix étapes")
check(V["py_d"]["lignes"][6].strip() == "if f(a) * f(m) <= 0:", "py_d.l7 : la ligne clé")

# Newton
check(M.X2N == round(0.75 - M.CUBE(0.75) / (3 * 0.75 ** 2 + 1), 6) and round(M.X2N, 3) == 0.686, "x₂ ≈ 0,686")
check(1 - M.CUBE(1) / (3 + 1) == 0.75, "x₁ = 0,75")
check(sur_courbe(M.NEWT, M.CUBE), "NEWT")
for el in V["g_nw"]["el"]:
    if el["type"] == "droite":
        x0 = 1.0 if el["c"] == "sa" else 0.75
        for x, y in el["pts"]:
            check(abs(y - (M.CUBE(x0) + (3 * x0 ** 2 + 1) * (x - x0))) < 1e-4, f"g_nw : tangente en {x0} ({x} ; {y})")
check(abs(M.CUBE(0.75) - 0.1719) < 1e-4, "point (0,75 ; 0,1719)")
code_n = "\n".join(V["py_n"]["lignes"])
check(sortie(code_n) == V["py_n"]["sortie"], f"py_n : sortie {sortie(code_n)!r}")
x5 = float(V["py_n"]["sortie"].split()[-1])
check(abs(x5 - ALPHA) < 1e-15, "Newton : une quinzaine de chiffres exacts en cinq étapes")
check(V["py_n"]["lignes"][2].strip().startswith("x = x -"), "py_n.l3 : la formule")

# ---------------------------------------------------------------- IX. pièges : 0,34 < α < 0,35 (exercice 1)
# ---------------------------------------------------------------- X. exercice 1 : x³ − 3x + 1
meme_derivee(M.G3, lambda x: 3 * x * x - 3, XS, "exo 1 : f′")
meme_derivee(M.G3, lambda x: 3 * (x - 1) * (x + 1), XS, "exo 1 : f′ factorisée")
check(M.G3(0) == 1 and M.G3(1) == -1 and 1 - 3 + 1 == -1, "exo 1 : f(0) = 1, f(1) = −1")
check(all(3 * (x - 1) * (x + 1) < 0 for x in [-0.99 + j * 0.01 for j in range(199)]), "exo 1 : f′ < 0 sur ]−1 ; 1[")
check(round(M.G3(0.34), 4) == 0.0193 and round(M.G3(0.34), 3) == 0.019, f"f(0,34) = {M.G3(0.34)}")
check(round(M.G3(0.35), 4) == -0.0071 and round(M.G3(0.35), 3) == -0.007, f"f(0,35) = {M.G3(0.35)}")
check(0.34 < racines[1] < 0.35, "0,34 < α < 0,35")

# ---------------------------------------------------------------- XI. exercice 2 : eˣ − x − 2
fb = lambda x: exp(x) - x - 2
meme_derivee(fb, lambda x: exp(x) - 1, XS, "exo 2 : f′")
meme_derivee(fb, exp, XS, "exo 2 : f″", tol=1e-4, ordre=2)
check(fb(0) == -1 and 1 - 0 - 2 == -1, "exo 2 : f(0) = −1")
check(all(exp(x) - 1 > 0 for x in [0.01 * j for j in range(1, 500)]), "exo 2 : f′ > 0 sur ]0 ; +∞[")
check(fb(50) > 1e20 and 50 / exp(50) < 1e-15 and 2 / exp(50) < 1e-15, "exo 2 : limite +∞, x/eˣ → 0")
check(proche(fb(30), exp(30) * (1 - 30 / exp(30) - 2 / exp(30)), 1e-12), "exo 2 : factorisation par eˣ")
check(round(math.e - 3, 2) == -0.28 and round(math.e ** 2 - 4, 2) == 3.39, "e − 3 ≈ −0,28 ; e² − 4 ≈ 3,39")
check(proche(fb(1), math.e - 3) and proche(fb(2), math.e ** 2 - 4), "f(1) = e − 3, f(2) = e² − 4")
code3 = "\n".join(V["py3"]["lignes"]).replace("@1", V["py3"]["rep"][0])
check(sortie(code3) == V["py3"]["sortie"], f"py3 : sortie {sortie(code3)!r}")
check(V["py3"]["sortie"] == "(1.140625, 1.1484375)", "py3 : comme le site")
a, b, pas = 1, 2, 0
while b - a > 0.01:
    m = (a + b) / 2
    a, b = (a, m) if fb(a) * fb(m) <= 0 else (m, b)
    pas += 1
check(pas == 7, "py3 : sept étapes")
check(round(fb(1.14), 3) == -0.013 and round(fb(1.15), 3) == 0.008, f"f(1,14) = {fb(1.14)}, f(1,15) = {fb(1.15)}")
a, b = 1.0, 2.0
for _ in range(60):
    m = (a + b) / 2
    a, b = (a, m) if fb(a) * fb(m) <= 0 else (m, b)
check(round(a, 4) == 1.1462 and round(a, 3) == 1.146, f"α = {a}")
check(V["g_bac"]["el"][2]["x"] == round(a, 4), "g_bac : α ≈ 1,1462")
E = math.e
check(proche((E - 1) * (0 - 1) + E - 3, -2) and proche(-E + 1 + E - 3, -2), "tangente en 1 : y = (e − 1)x − 2")
check(all(fb(x) >= (E - 1) * x - 2 - 1e-12 for x in [0.01 * j for j in range(500)]), "f(x) ≥ (e − 1)x − 2")
check(M.E1 == round(E, 4), "E1")
dr = V["g_bac"]["el"][1]["pts"]
check(dr[0] == [0, -2] and abs(dr[1][1] - ((E - 1) * dr[1][0] - 2)) < 1e-3, "g_bac : droite tracée")
check(sur_courbe(M.FBAC, fb, 4e-4) and max(p[1] for p in M.FBAC) <= 4.4, "FBAC")

# ---------------------------------------------------------------- quiz
check(proche(1 / 2 ** 10, 1 / 1024) and 1 / 1024 < 1e-3 < 1 / 512, "quiz : dichotomie")

# ---------------------------------------------------------------- le texte lu
lu = " ".join(b if isinstance(b, str) else (b[0] if isinstance(b[0], str) and b[0] not in ("P", "C") else "")
              for s in M.SCENES for b in s["beats"])
lu = re.sub(r"\{[^}]*\}", "", lu)
lu = re.sub(r"\s+", " ", lu)


def montre(pat):
    return [lu[max(0, m.start() - 30):m.end() + 12] for m in re.finditer(pat, lu)]


for nom, pat in [
    ("chiffre dans le texte lu", r"\d"),
    ("« y » isolé (hors « y égale »)", r"(?<![\w'’-])y(?![\w'’-])(?! égale)"),
    ("« il y a » / « il y en a »", r"\b[Ii]l y (en )?a\b"),
    ("« tout » + une lettre", r"\btout(e|es|s)? [a-zA-Z](?![\w'’-])"),
    ("nombre + une lettre sans « fois »",
     r"\b(un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|quatorze|quinze|seize|vingt|cent|mille) "
     r"[a-z](?![\w'’-])"),
    ("« en a » (liaison)", r"\ben a\b"),
]:
    trouve = montre(pat)
    check(not trouve, f"texte lu, {nom} : {trouve}")
for interdit in ("ton cours", "ta prof", "ton prof", "en classe", "le diaporama", "le site dit", "générée"):
    check(interdit not in lu.lower(), f"texte lu : « {interdit} »")

if ERR:
    print(f"{len(ERR)} erreur(s) :")
    for e in ERR:
        print(" -", e)
    sys.exit(1)
print("ok : tous les calculs de maths_ch4 sont justes")
