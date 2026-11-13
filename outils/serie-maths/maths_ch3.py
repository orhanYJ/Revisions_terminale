"""Maths, chapitre 3 : « Limites de fonctions » — le cours en vidéo (site CQFD).

Même chaîne que la vidéo pilote du chapitre 1 (outils/serie-maths/maths_ch1.py) : outils/serie-philo/generer.py, voix
clonée, calage des visuels sur les mots ; moteur maths/serie/moteur.js (tableau noir) : formules en MathML, rédaction au
tableau (formule copie=True), code Python, graphiques tracés à la règle (graphe : courbes, asymptotes en pointillés).
Contenu : le chapitre 3 du site (outils/specialites/maths/src/ch3.js), rien au-delà ; ce qui dépasse le programme est dit
« hors programme » ou « pour aller plus loin ». Les deux exercices sont ceux du site (limites et asymptotes ; étude de
(2x − 1)eˣ, type bac). Chaque calcul affiché ou dit est vérifié par outils/serie-maths/verif_ch3.py.
Usage : PYTHONPATH=outils/serie-maths python3 outils/serie-philo/verifier.py maths_ch3
        PYTHONPATH=outils/serie-maths SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py maths_ch3   (brouillon)
        python3 outils/serie-philo/chevauchements.py maths-ch3
"""
from math import cos, exp, sin, sqrt

SITE = "maths"
CODE = "maths-ch3"
NOTION = "Limites de fonctions"
NUM = 3
TITRE = "Limites de fonctions"
SUIVANT = "Chapitre 4 · Dérivation, convexité, continuité"
RYTHME = "vivant"
# bloc repris du chapitre 1 (lettres des formules en majuscules, sans liaison ; « plusse » et « moin » devant une lettre
# ou un nombre), complété par les lettres de ce chapitre (g, h, y) ; le texte lu évite « il y a » pour que « y » isolé
# soit toujours l'ordonnée
PRONONCIATION = {"§n": "N", "§k": "K", "§f": "F", "§x": "X", "§b": "B", "§v": "V", "§m": "M", "§q": "Q",
                 "§g": "G", "§h": "H", "§y": "Y"}
for _tok in ("un", "une", "huit", "onze", "a", "u", "N", "F", "X", "M", "R", "A", "U", "L", "H", "Y"):
    PRONONCIATION["plus " + _tok] = "plusse " + _tok
    PRONONCIATION["moins " + _tok] = "moin " + _tok
LIAISONS = "maths"


# ---------------------------------------------------------------- données des graphiques (vérifiées par verif_ch3.py)
def trace(f, a, b, n=120, y=None):
    """Points de la courbe de f sur [a ; b], arrondis ; y = (bas, haut) : on vérifie que tout reste dans le cadre."""
    pts = [[round(a + (b - a) * i / n, 4), round(f(a + (b - a) * i / n), 4)] for i in range(n + 1)]
    if y:
        assert all(y[0] - 1e-6 <= p[1] <= y[1] + 1e-6 for p in pts), (a, b)
    return pts


def F1(x):
    return (2 * x + 1) / (x - 1)


# f(x) = (2x + 1)/(x − 1) sur [−4 ; 6] × [−6 ; 10] : branche gauche jusqu'à f = −6 (x = 5/8), droite depuis f = 10 (x = 11/8)
F1_G = trace(F1, -4, 0.625, 90, (-6, 10))
F1_D = trace(F1, 1.375, 6, 90, (-6, 10))
SEUIL = trace(lambda x: x * x / 4, 0, 8, 80, (0, 16))                       # y = x²/4, seuil A = 9 dépassé dès x = 6
INV2 = trace(lambda x: 2 + 1 / x, 0.25, 10, 120, (0, 6))                    # y = 2 + 1/x
COS = trace(cos, 0, 20, 240, (-1.6, 1.6))
SINC = trace(lambda x: sin(x) / x, 0.05, 30, 300, (-0.3, 1.1))
INV_D = trace(lambda x: 1 / x, 1 / 6, 4, 90, (-6, 6))
INV_G = trace(lambda x: 1 / x, -4, -1 / 6, 90, (-6, 6))
INV2_D = trace(lambda x: 1 / (x * x), 0.41, 4, 90, (0, 6))
INV2_G = trace(lambda x: 1 / (x * x), -4, -0.41, 90, (0, 6))
EXP = trace(exp, -5, 2.55, 120, (0, 13))
GAUSS = trace(lambda x: exp(-x * x), -3, 3, 120, (0, 1.2))
COSX = trace(lambda x: cos(x) / x, 0.9, 20, 240, (-1.2, 1.2))
GEND_H = trace(lambda x: 1 / x, 0.84, 20, 120, (-1.2, 1.2))
GEND_B = trace(lambda x: -1 / x, 0.84, 20, 120, (-1.2, 1.2))
XCOS = trace(lambda x: x + cos(x), 0, 12, 160, (-2, 13))
X2E = trace(lambda x: x * x * exp(-x), 0, 14, 140, (0, 0.7))
FB = trace(lambda x: (2 * x - 1) * exp(x), -7, 1.13, 160, (-1.6, 4.2))   # f(1,13) ≈ 3,91
MIN_FB = round(-2 * exp(-0.5), 4)                                           # −2e^(−1/2) ≈ −1,2131


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ardoise", humeur="mystere", carton=False, beats=[
        "{q1}{q1.1}Voici une fonction : f de x égale deux x plus un, sur x moins un. "
        "Elle a un défaut : en un, le dénominateur vaut zéro. Elle n'est pas définie en ce point.",
        "Alors posons deux questions. Que devient f de x quand x devient très grand ? Et que se passe-t-il quand x s'approche de un ?",
        "{q1.2}Calculons. f de mille : environ deux virgule zéro zéro trois. "
        "{q1.3}f d'un million : deux virgule zéro zéro zéro zéro zéro trois. On dirait que ça se rapproche de deux.",
        "{q1.4}Et près de un ? f de un virgule zéro zéro un : trois mille deux. "
        "{q1.5}f de zéro virgule neuf neuf neuf : moins deux mille neuf cent quatre-vingt-dix-huit. Ça explose ! "
        "D'un côté vers le haut, de l'autre vers le bas.",
        "{-q1}{g0}Regarde la courbe. {g0.1}{g0.2}Deux morceaux, séparés par la valeur interdite. "
        "{g0.3}À droite comme à gauche, loin du centre, la courbe se colle à une droite horizontale, à la hauteur deux. "
        "{g0.4}Et près de un, elle file le long d'une droite verticale, vers le haut ou vers le bas.",
        "Ces deux droites ont un nom : des {!asymptotes}asymptotes. Les trouver, c'est étudier les limites de la fonction. "
        "Le comportement aux bords.",
        ("P", 0.5),
        "{-g0}{plan}Voici le chemin. {plan.1}D'abord les limites en l'infini, et les asymptotes horizontales. "
        "{plan.2}Puis les limites en un réel, et les asymptotes verticales. "
        "{plan.3}Ensuite les fonctions de référence, dont l'exponentielle. "
        "{plan.4}Les opérations, les formes indéterminées, et la composition. "
        "{plan.5}Puis la comparaison, les gendarmes, et les croissances comparées, avec deux démonstrations exigibles. "
        "{plan.6}Et pour finir, les pièges, et deux exercices corrigés, dont un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q1": dict(type="formule", titre="Une expérience", x=230, y=110, w=820, lignes=[
            dict(f="$f(x)=\\dfrac{2x+1}{x-1}$", cadre=True, taille=54),
            dict(f="$f(1000)\\approx2{,}003$", taille=40),
            dict(f="$f(1\\,000\\,000)\\approx2{,}000\\,003$", taille=40),
            dict(f="$f(1{,}001)=3002$", taille=40),
            dict(f="$f(0{,}999)=-2998$", taille=40)]),
        "g0": dict(type="graphe", titre="La courbe de $f(x)=\\dfrac{2x+1}{x-1}$", x=190, y=96, w=900, h=590,
                   ax=dict(x=[-4, 6], y=[-6, 10], gx=[-2, 2, 4], gy=[-4, 4, 8], lx="$x$", ly="$y$"),
                   el=[dict(type="courbe", pts=F1_G, c="iv", ep=3.4),
                       dict(type="courbe", pts=F1_D, c="iv", ep=3.4),
                       dict(type="droite", pts=[[-4, 2], [6, 2]], c="sa", ep=2.6, tir=True, lbl="$y=2$", lp=[-3, 2.8]),
                       dict(type="droite", pts=[[1, -6], [1, 10]], c="ca", ep=2.6, tir=True, lbl="$x=1$", lp=[2.1, 8.9])]),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Limites en l'infini, asymptotes horizontales", "Limites en un réel, asymptotes verticales",
            "Les fonctions de référence, l'exponentielle", "Opérations, formes indéterminées, composition",
            "Comparaison, gendarmes, croissances comparées", "Les pièges, deux exercices corrigés"], x=150, y=110, w=980),
        "titre": dict(type="titre", sur="Maths · Chapitre 3", t="Limites de fonctions",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. limites en l'infini
    dict(id="infini", chap="Limites en plus ou moins l'infini", fond="ardoise", humeur="lumiere",
         retenir="Si $\\lim_{x\\to\\pm\\infty}f(x)=\\ell$ (un réel), la droite d'équation $y=\\ell$ est asymptote horizontale ; la position relative vient du signe de $f(x)-\\ell$.",
         beats=[
        "{q_inf}Commençons par le plus naturel. Que fait f de x quand x devient de plus en plus grand ? "
        "Tu connais déjà l'idée, avec les suites. La seule différence : au lieu d'un entier n, c'est un réel x qui grandit.",
        "{-q_inf}{def_pinf}Première situation : f de x tend vers plus l'infini quand x tend vers plus l'infini. "
        "Ça veut dire que tout intervalle de la forme A, plus l'infini, contient toutes les valeurs f de x, dès que x est assez grand.",
        "{-def_pinf}{g_seuil}En image. {g_seuil.1}Voici une courbe qui monte. {g_seuil.2}Choisis un seuil A, aussi haut que tu veux. Ici, neuf. "
        "{g_seuil.3}À partir d'un certain x, ici six, la courbe passe au-dessus du seuil, {g_seuil.4}et elle n'en redescend plus. "
        "Si c'est vrai pour n'importe quel seuil, même un milliard, alors la limite est plus l'infini.",
        "{-g_seuil}{def_lim}Deuxième situation : une limite finie. f de x tend vers un réel L si tout intervalle ouvert contenant L "
        "contient toutes les valeurs f de x, pour x assez grand. Aussi étroit que soit l'intervalle, la courbe finit par entrer dans l'intervalle, et n'en sort plus.",
        "{def_lim.1}Et dans ce cas, la droite d'équation y égale L est {!asymptote horizontale}asymptote horizontale à la courbe, en plus l'infini.",
        "{-def_lim}{moins}Et en moins l'infini ? Mêmes définitions. On remplace « x assez grand » par « x assez petit », "
        "c'est-à-dire x inférieur ou égal à un certain nombre B.",
        "{-moins}{g_inv}Un exemple. {g_inv.1}f de x égale deux, plus un sur x. Quand x tend vers plus l'infini, un sur x tend vers zéro. "
        "Donc f de x tend vers deux. {g_inv.2}La droite d'équation y égale deux est asymptote horizontale en plus l'infini.",
        "{g_inv.3}Et une question qu'on te pose souvent : la courbe est-elle au-dessus, ou en dessous ? "
        "Pour x positif, un sur x est positif, donc f de x est plus grand que deux. La courbe est au-dessus de son asymptote.",
        "{-g_inv}{meth_pos}La méthode générale : pour la position relative, on étudie le signe de f de x, moins L. "
        "{meth_pos.1}Positif : la courbe est au-dessus. Négatif : en dessous.",
        "{-meth_pos}{g_cos}Attention : une fonction n'a pas toujours de limite. {g_cos.1}Regarde cosinus de x. "
        "Il oscille entre moins un et un, indéfiniment. Il ne se rapproche d'aucune valeur, et il ne part pas à l'infini. "
        "{g_cos.2}Cosinus n'a pas de limite en plus l'infini.",
        "{-g_cos}{g_sinc}Autre surprise. {g_sinc.1}Voici sinus de x, sur x. Elle tend vers zéro en plus l'infini, on le prouvera avec les gendarmes. "
        "{g_sinc.2}Donc l'axe des abscisses est asymptote. Et pourtant, la courbe le traverse ! Une infinité de fois.",
        "Une courbe peut couper son asymptote. L'asymptote décrit le comportement à l'infini. Ce n'est pas une barrière.",
        "{-g_sinc}",
    ], vis={
        "q_inf": dict(type="question", t="Que devient $f(x)$ quand $x$ devient de plus en plus grand ?"),
        "def_pinf": dict(type="def", terme="Limite infinie en $+\\infty$", cles=["intervalle", "grand"],
                         t="$\\lim_{x\\to+\\infty}f(x)=+\\infty$ si tout intervalle $[A;+\\infty[$ contient toutes les valeurs $f(x)$ pour $x$ assez grand.",
                         x=150, y=200, w=980),
        "g_seuil": dict(type="graphe", titre="Passer au-dessus de n'importe quel seuil", x=270, y=110, w=740, h=560,
                        ax=dict(x=[0, 8.6], y=[0, 16.5], gx=[2, 4, 6, 8], gy=[4, 9, 12, 16], lx="$x$", ly="$y$"),
                        el=[dict(type="courbe", pts=SEUIL, c="iv", ep=3.4),
                            dict(type="droite", pts=[[0, 9], [8.6, 9]], c="sa", ep=2.6, tir=True, lbl="seuil $A=9$", lp=[1.6, 10.3]),
                            dict(type="point", x=6, y=9, c="ca", proj=True),
                            dict(type="texte", x=3.4, y=14.6, t="pour $x\\geq6$ : $f(x)\\geq A$", c="ca")]),
        "def_lim": dict(type="def", terme="Limite finie en $+\\infty$", cles=["intervalle", "ouvert"],
                        t="$\\lim_{x\\to+\\infty}f(x)=\\ell$ si tout intervalle ouvert contenant $\\ell$ contient toutes les valeurs $f(x)$ pour $x$ assez grand.",
                        etape="La droite d'équation $y=\\ell$ est alors asymptote horizontale en $+\\infty$.", x=150, y=170, w=980),
        "moins": dict(type="note", titre="En $-\\infty$", cles=["petit"],
                      t="Mêmes définitions, « pour $x$ assez petit » : $x\\leq B$ pour un certain réel $B$.", x=170, y=220, w=940),
        "g_inv": dict(type="graphe", titre="$f(x)=2+\\dfrac1x$ en $+\\infty$", x=290, y=110, w=700, h=560,
                      ax=dict(x=[0, 10.5], y=[0, 6.2], gx=[2, 4, 6, 8, 10], gy=[2, 4, 6], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=INV2, c="iv", ep=3.4),
                          dict(type="droite", pts=[[0, 2], [10.5, 2]], c="sa", ep=2.6, tir=True, lbl="$y=2$", lp=[9.4, 1.3]),
                          dict(type="texte", x=6.6, y=4.2, t="$f(x)-2=\\dfrac1x>0$ : au-dessus", c="te")]),
        "meth_pos": dict(type="formule", titre="Position relative", x=170, y=170, w=940, lignes=[
            dict(f="On étudie le signe de $f(x)-\\ell$.", txt=True),
            dict(f="$f(x)-\\ell>0$ : courbe au-dessus ; $f(x)-\\ell<0$ : en dessous.", taille=36)]),
        "g_cos": dict(type="graphe", titre="$\\cos x$ : pas de limite en $+\\infty$", x=150, y=150, w=980, h=460,
                      ax=dict(x=[0, 20.5], y=[-1.6, 1.6], gx=[5, 10, 15, 20], gy=[-1, 1], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=COS, c="iv", ep=3.2, dur=3),
                          dict(type="texte", x=15.5, y=1.38, t="elle oscille sans fin", c="ca")]),
        "g_sinc": dict(type="graphe", titre="$\\dfrac{\\sin x}{x}$ coupe son asymptote $y=0$", x=150, y=130, w=980, h=500,
                       ax=dict(x=[0, 31], y=[-0.3, 1.1], gx=[10, 20, 30], gy=[0.5, 1], lx="$x$", ly="$y$"),
                       el=[dict(type="courbe", pts=SINC, c="iv", ep=3.2, dur=3),
                           dict(type="droite", pts=[[0, 0], [31, 0]], c="sa", ep=3, lbl="asymptote $y=0$", lp=[24, 0.32])]),
    }),

    # ================================================================ II. limites en un réel
    dict(id="point", chap="Limites en un réel, asymptotes verticales", fond="carnet", humeur="tension",
         retenir="Si $\\lim_{x\\to a}f(x)=\\pm\\infty$ (d'un côté au moins), la droite d'équation $x=a$ est asymptote verticale. On étudie souvent la limite à gauche et à droite.",
         beats=[
        "{def_a}Deuxième bord : une valeur interdite, un réel a. On dit que f de x tend vers plus l'infini quand x tend vers a, "
        "si tout intervalle A, plus l'infini, contient toutes les valeurs f de x, dès que x est assez proche de a.",
        "{def_a.1}Et la droite d'équation x égale a est alors {!asymptote verticale}asymptote verticale.",
        "{-def_a}{cotes}Souvent, le comportement n'est pas le même des deux côtés. {cotes.1}On note x tend vers a plus, "
        "quand x s'approche de a en restant plus grand que a : c'est la limite à droite. {cotes.2}Et x tend vers a moins, "
        "quand x reste plus petit : la limite à gauche.",
        "{-cotes}{g_1x}Premier exemple : un sur x, près de zéro. {g_1x.1}Si x est positif et se rapproche de zéro, un sur x devient énorme. "
        "Un sur zéro virgule zéro zéro un, ça fait mille. La limite à droite est plus l'infini. "
        "{g_1x.2}Si x est négatif, un sur x est négatif, et de plus en plus grand en valeur absolue : la limite à gauche est moins l'infini.",
        "{g_1x.3}Deux côtés, deux limites différentes. Mais dans les deux cas, l'axe des ordonnées, la droite x égale zéro, est asymptote verticale.",
        "{-g_1x}{g_1x2}{g_1x2.1}{g_1x2.2}Comparons avec un sur x au carré. Là, le carré est toujours positif : "
        "la limite est plus l'infini des deux côtés. On écrit simplement : la limite en zéro de un sur x au carré vaut plus l'infini.",
        "{-g_1x2}{ex_f}Revenons à notre fonction du début, deux x plus un, sur x moins un, quand x tend vers un. "
        "{ex_f.1}Le numérateur tend vers deux fois un, plus un : trois. {ex_f.2}Le dénominateur, x moins un, tend vers zéro.",
        "{ex_f.3}Tout se joue sur le signe du dénominateur. x moins un est positif si x est plus grand que un, négatif sinon. "
        "{ex_f.4}À droite de un : trois, divisé par un nombre positif qui tend vers zéro. Ça donne plus l'infini. "
        "{ex_f.5}À gauche de un : trois, divisé par un nombre négatif qui tend vers zéro. Moins l'infini.",
        "{ex_f.6}Conclusion : la droite d'équation x égale un est asymptote verticale. Exactement ce qu'on avait vu sur la courbe.",
        "{-ex_f}{py}Et Python confirme. Ce programme calcule f de x pour des x de plus en plus grands, puis pour des x proches de un. "
        "{py.s}On lit : environ deux en plus l'infini, des valeurs énormes et positives à droite de un, énormes et négatives à gauche.",
        "Un détail amusant : f de un virgule un devrait valoir trente-deux, et Python affiche trente et un virgule neuf neuf neuf, et ainsi de suite. "
        "Les nombres à virgule sont arrondis en machine.",
        "Mais retiens bien : Python sert à conjecturer, ou à vérifier un calcul. Il ne justifie jamais une limite.",
        "{-py}{meth_vi}Voici donc la méthode, en trois étapes, pour une limite en une valeur interdite. "
        "{meth_vi.1}Un : la limite du numérateur, souvent un réel non nul, et celle du dénominateur, zéro. "
        "{meth_vi.2}Deux : un tableau de signes du dénominateur, pour savoir s'il tend vers zéro par valeurs positives ou négatives, selon le côté. "
        "{meth_vi.3}Trois : la règle des signes. Et si le numérateur tend aussi vers zéro, c'est une autre histoire : on la verra avec les formes indéterminées.",
        "{-meth_vi}{ex_h}Entraînons-nous. h de x égale x au carré plus trois x, sur x au carré moins quatre, en deux. "
        "{ex_h.1}Le numérateur tend vers quatre plus six : dix. {ex_h.2}Le dénominateur s'écrit x moins deux, fois x plus deux. "
        "Il tend vers zéro. Près de deux, x plus deux est positif, donc le signe est celui de x moins deux.",
        "{ex_h.3}À droite de deux, il est positif : h tend vers plus l'infini. À gauche, il est négatif : moins l'infini. "
        "{ex_h.4}Vérification numérique : h de deux virgule zéro zéro un vaut environ deux mille cinq cent un, "
        "et h de un virgule neuf neuf neuf, environ moins deux mille quatre cent quatre-vingt-dix-neuf.",
        "{-ex_h}{piege0}Et un réflexe de rédaction. {piege0.1}N'écris jamais « trois sur zéro égale l'infini ». On ne divise pas par zéro. "
        "On étudie la limite d'un quotient dont le dénominateur tend vers zéro, avec son signe.",
        "{-piege0}{fini}Dernière chose : une limite en un point peut aussi être finie. {fini.1}La limite en deux de x au carré plus un, c'est cinq. "
        "{fini.2}Pour une fonction usuelle définie en a, on remplace simplement x par a. C'est la continuité : tu la verras au chapitre suivant.",
        "{-fini}",
    ], vis={
        "def_a": dict(type="def", terme="Limite infinie en un réel $a$", cles=["intervalle", "proche"],
                      t="$\\lim_{x\\to a}f(x)=+\\infty$ si tout intervalle $[A;+\\infty[$ contient toutes les valeurs $f(x)$ pour $x$ assez proche de $a$.",
                      etape="La droite d'équation $x=a$ est alors asymptote verticale.", x=150, y=170, w=980),
        "cotes": dict(type="formule", titre="À droite, à gauche", x=170, y=190, w=940, lignes=[
            dict(f="$x\\to a^+$ : $x$ tend vers $a$ avec $x>a$", n="la limite à droite"),
            dict(f="$x\\to a^-$ : $x$ tend vers $a$ avec $x<a$", n="la limite à gauche")]),
        "g_1x": dict(type="graphe", titre="$\\dfrac1x$ près de $0$", x=270, y=96, w=740, h=590,
                     ax=dict(x=[-4, 4], y=[-6, 6], gx=[-2, 2], gy=[-4, 4], lx="$x$", ly="$y$"),
                     el=[dict(type="courbe", pts=INV_D, c="iv", ep=3.4),
                         dict(type="courbe", pts=INV_G, c="iv", ep=3.4),
                         dict(type="texte", x=2.25, y=4.8, t="$\\lim_{x\\to0^+}\\dfrac1x=+\\infty$", c="sa"),
                         dict(type="texte", x=-2.25, y=-4.8, t="$\\lim_{x\\to0^-}\\dfrac1x=-\\infty$", c="ca")]),
        "g_1x2": dict(type="graphe", titre="$\\dfrac1{x^2}$ près de $0$", x=270, y=110, w=740, h=560,
                      ax=dict(x=[-4, 4], y=[0, 6.3], gx=[-2, 2], gy=[2, 4, 6], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=INV2_D, c="iv", ep=3.4),
                          dict(type="courbe", pts=INV2_G, c="iv", ep=3.4),
                          dict(type="texte", x=2.0, y=4.6, t="$+\\infty$ des deux côtés", c="sa")]),
        "ex_f": dict(type="formule", copie=True, titre="$f(x)=\\dfrac{2x+1}{x-1}$ quand $x\\to1$", x=110, y=86, w=1060, lignes=[
            dict(f="$\\lim_{x\\to1}(2x+1)=3$", m="numérateur", taille=34),
            dict(f="$\\lim_{x\\to1}(x-1)=0$", m="dénominateur", taille=34),
            dict(f="$x-1>0$ si $x>1$ ; $x-1<0$ si $x<1$", m="signe", taille=34),
            dict(f="$\\lim_{x\\to1^+}f(x)=+\\infty$", ind=True, m="$\\frac{3}{0^+}$", taille=34),
            dict(f="$\\lim_{x\\to1^-}f(x)=-\\infty$", ind=True, m="$\\frac{3}{0^-}$", taille=34),
            dict(f="la droite d'équation $x=1$ est asymptote verticale.", cadre=True, taille=32)]),
        "py": dict(type="code", titre="Python · conjecturer une limite", x=190, y=86, w=900, taille=25, lignes=[
            "def f(x):", "    return (2 * x + 1) / (x - 1)", "", "for x in [10, 1000, 10**6]:", "    print(x, f(x))",
            "for x in [1.1, 1.001, 0.999]:", "    print(x, f(x))"],
            sortie="10 2.3333333333333335\n1000 2.003003003003003\n1000000 2.000003000003\n1.1 31.999999999999975\n1.001 3002.0000000003306\n0.999 -2997.9999999999977"),
        "meth_vi": dict(type="liste", titre="Limite en une valeur interdite", items=[
            "Limites du numérateur (souvent un réel non nul) et du dénominateur ($0$)",
            "Tableau de signes du dénominateur : $0^+$ ou $0^-$ selon le côté",
            "Règle des signes ; si c'est $\\frac00$, autre méthode"], x=150, y=170, w=980),
        "ex_h": dict(type="formule", copie=True, titre="$h(x)=\\dfrac{x^2+3x}{x^2-4}$ en $2$", x=110, y=96, w=1060, lignes=[
            dict(f="$\\lim_{x\\to2}(x^2+3x)=4+6=10$", m="numérateur", taille=33),
            dict(f="$x^2-4=(x-2)(x+2)\\to0$ ; près de $2$, $x+2>0$", m="signe de $x-2$", taille=33),
            dict(f="$\\lim_{x\\to2^+}h(x)=+\\infty$ et $\\lim_{x\\to2^-}h(x)=-\\infty$", cadre=True, taille=33),
            dict(f="$h(2{,}001)\\approx2501$ et $h(1{,}999)\\approx-2499$", n="vérification numérique", taille=31)]),
        "piege0": dict(type="note", titre="Jamais « $\\frac30=\\infty$ »", cles=["divise", "signe"],
                       t="On ne divise pas par zéro : on étudie la limite d'un quotient dont le dénominateur tend vers $0$, avec son signe ($0^+$ ou $0^-$).",
                       x=170, y=200, w=940),
        "fini": dict(type="formule", titre="Une limite finie en un point", x=170, y=200, w=940, lignes=[
            dict(f="$\\lim_{x\\to2}(x^2+1)=2^2+1=5$", taille=44),
            dict(f="fonction usuelle définie en $a$ : on remplace $x$ par $a$", n="c'est la continuité, au chapitre 4", txt=True)]),
    }),

    # ================================================================ III. fonctions de référence
    dict(id="reference", chap="Les fonctions de référence", fond="ardoise", humeur="lumiere",
         retenir="$\\lim_{x\\to+\\infty}\\e^x=+\\infty$ et $\\lim_{x\\to-\\infty}\\e^x=0$ : l'axe des abscisses est asymptote à la courbe de $\\exp$ en $-\\infty$.",
         beats=[
        "{ref}Pour calculer des limites, on part toujours des mêmes briques : les fonctions de référence. Passons-les en revue.",
        "{ref.1}Les puissances, x puissance n, avec n supérieur ou égal à un. En plus l'infini, elles tendent toutes vers plus l'infini. "
        "{ref.2}En moins l'infini, ça dépend de la parité : plus l'infini si n est pair, comme x au carré, moins l'infini si n est impair, comme x au cube.",
        "{ref.3}Leurs inverses, un sur x puissance n, tendent vers zéro en plus l'infini comme en moins l'infini. "
        "{ref.4}Et en zéro, on vient de le voir : plus l'infini si n est pair ; si n est impair, plus l'infini à droite et moins l'infini à gauche.",
        "{ref.5}La racine carrée de x tend vers zéro en zéro, et vers plus l'infini en plus l'infini.",
        "{-ref}{thm_exp}Et la star du chapitre : l'exponentielle. {thm_exp.1}En plus l'infini, exponentielle de x tend vers plus l'infini. "
        "{thm_exp.2}En moins l'infini, elle tend vers zéro.",
        "{-thm_exp}{g_exp}Regarde sa courbe. {g_exp.1}Elle passe par le point zéro, un. {g_exp.2}À droite, elle monte en flèche. "
        "{g_exp.3}À gauche, elle s'écrase sur l'axe des abscisses, sans jamais le toucher : l'exponentielle est strictement positive. "
        "L'axe des abscisses est donc asymptote horizontale à la courbe, en moins l'infini.",
        "Ces deux limites sont une démonstration exigible. Pour la faire, il nous manque un outil, le théorème de comparaison. "
        "On la fera un peu plus loin.",
        "{-g_exp}",
    ], vis={
        "ref": dict(type="formule", titre="Les fonctions de référence", x=110, y=100, w=1060, lignes=[
            dict(f="$x^n$ ($n\\geq1$) : $\\to+\\infty$ en $+\\infty$", taille=33),
            dict(f="en $-\\infty$ : $+\\infty$ si $n$ pair, $-\\infty$ si $n$ impair", ind=True, taille=33),
            dict(f="$\\dfrac1{x^n}$ : $\\to0$ en $+\\infty$ et en $-\\infty$", taille=33),
            dict(f="en $0$ : $+\\infty$ si $n$ pair ; $n$ impair : $-\\infty$ en $0^-$, $+\\infty$ en $0^+$", ind=True, taille=31),
            dict(f="$\\sqrt x$ : $\\to0$ en $0$, $\\to+\\infty$ en $+\\infty$", taille=33)]),
        "thm_exp": dict(type="formule", titre="Limites de l'exponentielle", x=200, y=200, w=880, lignes=[
            dict(f="$\\lim_{x\\to+\\infty}\\e^x=+\\infty$", taille=50),
            dict(f="$\\lim_{x\\to-\\infty}\\e^x=0$", cadre=True, taille=50)]),
        "g_exp": dict(type="graphe", titre="La courbe de l'exponentielle", x=270, y=110, w=740, h=560,
                      ax=dict(x=[-5, 2.8], y=[0, 13.3], gx=[-4, -2, 1, 2], gy=[1, 5, 10], lx="$x$", ly="$y$"),
                      el=[dict(type="point", x=0, y=1, c="sa", lbl="$(0;1)$", lp=[-1.3, 2.6]),
                          dict(type="courbe", pts=EXP, c="iv", ep=3.4),
                          dict(type="droite", pts=[[-5, 0], [0, 0]], c="ca", ep=3.4, lbl="asymptote en $-\\infty$", lp=[-2.6, 2.4])]),
    }),

    # ================================================================ IV. opérations et formes indéterminées
    dict(id="operations", chap="Opérations et formes indéterminées", fond="carnet", humeur="tension",
         retenir="Formes indéterminées : $\\infty-\\infty$, $0\\times\\infty$, $\\frac\\infty\\infty$, $\\frac00$. En $\\pm\\infty$, un polynôme se comporte comme son terme de plus haut degré ; en $0$, c'est le plus bas degré qui domine.",
         beats=[
        "{ops}Maintenant, comment calculer la limite d'une somme, d'un produit, d'un quotient ? Bonne nouvelle : "
        "les règles sont exactement les mêmes que pour les suites. Elles sont admises.",
        "{ops.1}Plus l'infini, plus plus l'infini : plus l'infini. {ops.2}Un réel non nul, fois l'infini : l'infini, avec la règle des signes. "
        "{ops.3}Un réel, divisé par quelque chose qui tend vers l'infini : zéro.",
        "{-ops}{fi}Mais quatre situations résistent. On les appelle les {!formes indéterminées}formes indéterminées. "
        "{fi.1}L'infini moins l'infini. {fi.2}Zéro fois l'infini. {fi.3}L'infini sur l'infini. {fi.4}Et zéro sur zéro.",
        "{-fi}{fi_ex}Pourquoi « indéterminées » ? Parce que le résultat dépend de la situation. Trois exemples, tous de la forme infini moins infini, en plus l'infini. "
        "{fi_ex.1}x au carré, moins x : ça tend vers plus l'infini. {fi_ex.2}x, moins x au carré : moins l'infini. "
        "{fi_ex.3}Et x plus trois, moins x : ça vaut trois, tout le temps.",
        "{fi_ex.4}Même forme au départ, trois résultats différents. Une forme indéterminée ne veut pas dire « pas de limite ». "
        "Elle veut dire : les règles ne suffisent pas. Il faut transformer l'écriture.",
        "{-fi_ex}{poly}Le premier outil : factoriser par le terme prépondérant. Exemple : la limite en moins l'infini de trois x au carré plus un, "
        "sur x au carré moins cinq x. {poly.1}C'est de la forme infini sur infini.",
        "{poly.2}On factorise en haut et en bas par x au carré. En haut, il reste trois, plus un sur x au carré. En bas, un, moins cinq sur x. "
        "{poly.3}Les x au carré se simplifient. Un sur x au carré et cinq sur x tendent vers zéro : la limite vaut trois sur un, c'est-à-dire trois.",
        "{poly.4}Et le raccourci à retenir : en plus ou moins l'infini, un polynôme se comporte comme son terme de plus haut degré. "
        "Un quotient, comme le quotient des termes de plus haut degré. Ici, trois x au carré sur x au carré : trois.",
        "{-poly}{retour}Appliquons-le à notre fonction du début. {retour.1}En plus l'infini, deux x plus un, sur x moins un, "
        "se comporte comme deux x sur x : deux. {retour.2}Pareil en moins l'infini. "
        "{retour.3}La droite d'équation y égale deux est donc asymptote horizontale, des deux côtés. Python l'avait deviné ; maintenant, c'est démontré.",
        "{-retour}{p0}Attention, un piège classique. {p0.1}En zéro, c'est l'inverse : c'est le terme de plus bas degré qui domine. "
        "{p0.2}Près de zéro, x au cube plus deux x se comporte comme deux x. Quand x vaut zéro virgule zéro un, x au cube vaut un millionième, "
        "deux x vaut deux centièmes. Ne factorise surtout pas par x au cube !",
        "{-p0}{zz}Deuxième outil, pour zéro sur zéro en un réel a : factoriser par x moins a. "
        "{zz.1}La limite en un de x au carré moins un, sur x moins un. En un, le numérateur et le dénominateur valent zéro. "
        "{zz.2}Mais x au carré moins un, c'est x moins un, fois x plus un. {zz.3}Pour x différent de un, on simplifie : il reste x plus un. "
        "{zz.4}Qui tend vers deux.",
        "{-zz}{taux}Et un dernier zéro sur zéro, qui tombe souvent : exponentielle de x, moins un, le tout sur x, en zéro. "
        "{taux.1}Pas de factorisation ici. Mais reconnais un taux d'accroissement : exponentielle de x moins exponentielle de zéro, sur x moins zéro. "
        "{taux.2}Sa limite, c'est le nombre dérivé de l'exponentielle en zéro : exponentielle de zéro, c'est-à-dire un.",
        "{-taux}",
    ], vis={
        "ops": dict(type="formule", titre="Les règles, comme pour les suites", x=170, y=150, w=940, lignes=[
            dict(f="$(+\\infty)+(+\\infty)=+\\infty$", taille=40),
            dict(f="réel non nul $\\times\\infty=\\infty$", m="règle des signes", taille=40),
            dict(f="$\\dfrac{\\text{réel}}{\\infty}=0$", taille=40)]),
        "fi": dict(type="formule", titre="Les quatre formes indéterminées", x=230, y=170, w=820, lignes=[
            dict(f="$\\infty-\\infty$", taille=48), dict(f="$0\\times\\infty$", taille=48),
            dict(f="$\\dfrac{\\infty}{\\infty}$", taille=48), dict(f="$\\dfrac00$", taille=48)]),
        "fi_ex": dict(type="formule", titre="$\\infty-\\infty$ en $+\\infty$ : trois résultats", x=170, y=150, w=940, lignes=[
            dict(f="$x^2-x\\to+\\infty$", taille=40),
            dict(f="$x-x^2\\to-\\infty$", taille=40),
            dict(f="$(x+3)-x=3\\to3$", taille=40),
            dict(f="la forme ne suffit pas : il faut transformer l'écriture", txt=True, ko=True)]),
        "poly": dict(type="formule", copie=True, titre="Factoriser par le terme prépondérant", x=110, y=100, w=1060, lignes=[
            dict(f="$\\lim_{x\\to-\\infty}\\dfrac{3x^2+1}{x^2-5x}$", m="forme $\\frac\\infty\\infty$", taille=34),
            dict(f="$\\dfrac{3x^2+1}{x^2-5x}=\\dfrac{x^2\\left(3+\\frac1{x^2}\\right)}{x^2\\left(1-\\frac5x\\right)}$", ind=True, taille=34),
            dict(f="$=\\dfrac{3+\\frac1{x^2}}{1-\\frac5x}\\to\\dfrac31=3$", ind=True, cadre=True, taille=34),
            dict(f="raccourci : quotient des termes de plus haut degré, $\\dfrac{3x^2}{x^2}=3$", txt=True)]),
        "retour": dict(type="formule", titre="Retour au début", x=170, y=170, w=940, lignes=[
            dict(f="en $+\\infty$ : $\\dfrac{2x+1}{x-1}$ se comporte comme $\\dfrac{2x}{x}=2$", taille=36),
            dict(f="de même en $-\\infty$", ind=True, taille=36),
            dict(f="$y=2$ : asymptote horizontale en $+\\infty$ et en $-\\infty$", cadre=True, taille=36)]),
        "p0": dict(type="formule", titre="En $0$, c'est l'inverse", x=170, y=170, w=940, lignes=[
            dict(f="en $0$, le terme de plus bas degré domine", txt=True),
            dict(f="$x^3+2x\\approx2x$ près de $0$", taille=40, n="pour $x=0{,}01$ : $x^3=0{,}000\\,001$ et $2x=0{,}02$")]),
        "zz": dict(type="formule", copie=True, titre="$\\frac00$ en $a$ : factoriser par $(x-a)$", x=130, y=140, w=1020, lignes=[
            dict(f="$\\lim_{x\\to1}\\dfrac{x^2-1}{x-1}$", m="forme $\\frac00$", taille=36),
            dict(f="$x^2-1=(x-1)(x+1)$", ind=True, taille=36),
            dict(f="pour $x\\neq1$ : $\\dfrac{(x-1)(x+1)}{x-1}=x+1$", ind=True, taille=36),
            dict(f="$x+1\\to2$ : la limite vaut $2$", ind=True, cadre=True, taille=36)]),
        "taux": dict(type="formule", titre="Un taux d'accroissement", x=170, y=170, w=940, lignes=[
            dict(f="$\\dfrac{\\e^x-1}{x}=\\dfrac{\\e^x-\\e^0}{x-0}$", m="forme $\\frac00$", taille=40),
            dict(f="$\\lim_{x\\to0}\\dfrac{\\e^x-1}{x}=\\exp'(0)=\\e^0=1$", cadre=True, taille=40)]),
    }),

    # ================================================================ V. composition
    dict(id="composition", chap="La composition", fond="ardoise", humeur="calme",
         retenir="Si $\\lim_{x\\to a}u(x)=b$ et $\\lim_{X\\to b}v(X)=c$, alors $\\lim_{x\\to a}v(u(x))=c$. Rédaction : « on pose $X=u(x)$ ».",
         beats=[
        "{q_comp}Comment trouver la limite d'exponentielle de moins x au carré, en plus l'infini ? "
        "Ce n'est ni une somme, ni un produit, ni un quotient : c'est une fonction dans une fonction. Une composée.",
        "{-q_comp}{thm_c}Le théorème de composition dit ceci. {thm_c.1}Si u de x tend vers b quand x tend vers a, "
        "{thm_c.2}et si v de grand X tend vers c quand grand X tend vers b, {thm_c.3}alors v de u de x tend vers c quand x tend vers a.",
        "{thm_c.4}Et a, b, c peuvent être des réels, ou plus ou moins l'infini. L'idée est simple : on suit la valeur, étage par étage.",
        "{-thm_c}{red_c}Rédigeons notre exemple, comme sur une copie. {red_c.1}On pose grand X égale moins x au carré. "
        "{red_c.2}Quand x tend vers plus l'infini, grand X tend vers moins l'infini. "
        "{red_c.3}Or la limite d'exponentielle de grand X, quand grand X tend vers moins l'infini, vaut zéro. "
        "{red_c.4}Donc, par composition, exponentielle de moins x au carré tend vers zéro en plus l'infini.",
        "{-red_c}{g_gauss}Voici sa courbe : une cloche. {g_gauss.1}Elle culmine à un, en zéro, {g_gauss.2}et s'aplatit sur l'axe des abscisses des deux côtés. "
        "En moins l'infini aussi, la limite vaut zéro : moins x au carré tend encore vers moins l'infini.",
        "{-g_gauss}{autres}Deux autres exemples, pour prendre le réflexe. {autres.1}Exponentielle de, un sur x, en plus l'infini : "
        "un sur x tend vers zéro, et exponentielle de zéro vaut un. La limite est un. "
        "{autres.2}Racine carrée de, un moins deux x, en moins l'infini : un moins deux x tend vers plus l'infini, "
        "et la racine carrée aussi. La limite est plus l'infini.",
        "{-autres}{phrase}Retiens la phrase type, mot pour mot. {phrase.1}On pose grand X égale u de x. Quand x tend vers a, grand X tend vers b. "
        "Or la limite de v en b vaut c. Par composition, la limite de v de u de x vaut c. Quatre phrases, et tous les points.",
        "{-phrase}",
    ], vis={
        "q_comp": dict(type="question", t="$\\lim_{x\\to+\\infty}\\e^{-x^2}$ : une fonction dans une fonction ?"),
        "thm_c": dict(type="formule", titre="Théorème de composition", x=150, y=150, w=980, lignes=[
            dict(f="Si $\\lim_{x\\to a}u(x)=b$", taille=40),
            dict(f="et $\\lim_{X\\to b}v(X)=c$,", taille=40),
            dict(f="alors $\\lim_{x\\to a}v\\big(u(x)\\big)=c$.", cadre=True, taille=40),
            dict(f="$a$, $b$, $c$ : des réels ou $\\pm\\infty$", txt=True)]),
        "red_c": dict(type="formule", copie=True, titre="Rédiger une composition", x=130, y=140, w=1020, lignes=[
            dict(f="On pose $X=-x^2$.", taille=36),
            dict(f="Quand $x\\to+\\infty$, $X\\to-\\infty$.", taille=36),
            dict(f="Or $\\lim_{X\\to-\\infty}\\e^X=0$.", taille=36),
            dict(f="Par composition, $\\lim_{x\\to+\\infty}\\e^{-x^2}=0$.", cadre=True, taille=36)]),
        "g_gauss": dict(type="graphe", titre="La courbe de $x\\mapsto\\e^{-x^2}$", x=190, y=140, w=900, h=480,
                        ax=dict(x=[-3.2, 3.2], y=[0, 1.25], gx=[-2, -1, 1, 2], gy=[0.5, 1], lx="$x$", ly="$y$"),
                        el=[dict(type="point", x=0, y=1, c="sa", lbl="$(0;1)$", lp=[0.65, 1.12]),
                            dict(type="courbe", pts=GAUSS, c="iv", ep=3.4, dur=2.4)]),
        "autres": dict(type="formule", titre="Deux autres compositions", x=130, y=170, w=1020, lignes=[
            dict(f="$\\lim_{x\\to+\\infty}\\e^{\\frac1x}=\\e^0=1$", n="car $\\frac1x\\to0$", taille=40),
            dict(f="$\\lim_{x\\to-\\infty}\\sqrt{1-2x}=+\\infty$", n="car $1-2x\\to+\\infty$", taille=40)]),
        "phrase": dict(type="note", titre="La phrase type", cles=["pose", "composition"],
                       t="« On pose $X=u(x)$. Quand $x\\to a$, $X\\to b$. Or $\\lim_{X\\to b}v(X)=c$. Par composition, $\\lim_{x\\to a}v(u(x))=c$. »",
                       x=150, y=200, w=980),
    }),

    # ================================================================ VI. comparaison et gendarmes
    dict(id="comparaison", chap="Comparaison et gendarmes", fond="carnet", humeur="lumiere",
         retenir="Comparaison : si $f(x)\\geq g(x)$ et $g(x)\\to+\\infty$, alors $f(x)\\to+\\infty$. Gendarmes : $g\\leq f\\leq h$ et $g$, $h$ de même limite finie $\\ell$ donnent $f\\to\\ell$.",
         beats=[
        "{q_cmp}Que faire quand la fonction contient un cosinus ou un sinus, qui oscille sans limite ? On l'encadre.",
        "{-q_cmp}{thm_cmp}Premier théorème, la {!comparaison}comparaison. {thm_cmp.1}Si f de x est supérieur ou égal à g de x pour x assez grand, "
        "et si g de x tend vers plus l'infini, alors f de x tend aussi vers plus l'infini. "
        "Celle qui est au-dessus est poussée vers le haut. {thm_cmp.2}Et vers le bas, c'est pareil : sous une fonction qui tend vers moins l'infini, on est entraîné vers moins l'infini.",
        "{-thm_cmp}{thm_g}Deuxième théorème, les {!gendarmes}gendarmes. {thm_g.1}Si g de x est inférieur ou égal à f de x, lui-même inférieur ou égal à h de x, "
        "pour x assez grand, {thm_g.2}et si g et h ont la même limite finie L, alors f de x tend aussi vers L. Coincée entre les deux, elle n'a pas le choix.",
        "{-thm_g}{g_gend}Exemple : f de x égale cosinus de x, sur x, pour x positif. {g_gend.1}La courbe oscille, de moins en moins fort. "
        "{g_gend.2}{g_gend.3}Comme cosinus est compris entre moins un et un, on divise par x, qui est positif : f de x est compris entre moins un sur x et un sur x. "
        "{g_gend.4}Les deux gendarmes tendent vers zéro. Donc, par le théorème des gendarmes, f de x tend vers zéro.",
        "C'est exactement le même argument pour sinus de x sur x : il tend vers zéro, comme annoncé.",
        "{-g_gend}{g_xcos}Et pour la comparaison : g de x égale x plus cosinus de x. "
        "{g_xcos.1}Comme cosinus de x est supérieur ou égal à moins un, g de x est supérieur ou égal à x moins un. "
        "{g_xcos.2}La courbe reste au-dessus d'une droite qui monte sans fin. {g_xcos.3}x moins un tend vers plus l'infini, donc, par comparaison, g aussi.",
        "{-g_xcos}{tag_bo}{dem_e}Nous avons maintenant l'outil pour la première démonstration exigible : les limites de l'exponentielle. "
        "{dem_e.1}En plus l'infini. On étudie g de x égale exponentielle de x, moins x. "
        "{dem_e.2}Sa dérivée vaut exponentielle de x, moins un. Elle est négative pour x négatif, positive pour x positif. "
        "{dem_e.3}Donc g admet un minimum en zéro. Et g de zéro vaut exponentielle de zéro, moins zéro : un. Qui est strictement positif.",
        "{dem_e.4}Donc, pour tout réel x, exponentielle de x est strictement plus grand que x. "
        "{dem_e.5}Comme x tend vers plus l'infini, par comparaison, exponentielle de x tend vers plus l'infini.",
        "{dem_e.6}En moins l'infini, maintenant. Exponentielle de x égale un, sur exponentielle de moins x. On pose grand X égale moins x. "
        "{dem_e.7}Quand x tend vers moins l'infini, grand X tend vers plus l'infini, donc exponentielle de grand X aussi, "
        "{dem_e.8}et un sur exponentielle de grand X tend vers zéro. Conclusion : exponentielle de x tend vers zéro en moins l'infini.",
        "{-dem_e}{-tag_bo}",
    ], vis={
        "q_cmp": dict(type="question", t="Et quand la fonction contient un $\\cos$ ou un $\\sin$ ?"),
        "thm_cmp": dict(type="def", terme="Théorème de comparaison", cles=["grand", "tend"],
                        t="Si $f(x)\\geq g(x)$ pour $x$ assez grand et $\\lim_{x\\to+\\infty}g(x)=+\\infty$, alors $\\lim_{x\\to+\\infty}f(x)=+\\infty$.",
                        etape="De même vers $-\\infty$ (avec $f\\leq g$), en $-\\infty$ ou en un réel $a$.", x=150, y=170, w=980),
        "thm_g": dict(type="def", terme="Théorème des gendarmes", cles=["finie", "limite"],
                      t="Si $g(x)\\leq f(x)\\leq h(x)$ pour $x$ assez grand, et si $g$ et $h$ ont la même limite finie $\\ell$ en $+\\infty$, alors $\\lim_{x\\to+\\infty}f(x)=\\ell$.",
                      x=150, y=190, w=980),
        "g_gend": dict(type="graphe", titre="$f(x)=\\dfrac{\\cos x}{x}$ entre deux gendarmes", x=150, y=120, w=980, h=530,
                       ax=dict(x=[0, 20.5], y=[-1.2, 1.2], gx=[5, 10, 15, 20], gy=[-1, 1], lx="$x$", ly="$y$"),
                       el=[dict(type="courbe", pts=COSX, c="iv", ep=3.2, dur=2.6),
                           dict(type="courbe", pts=GEND_H, c="te", ep=2.6, lbl="$y=\\frac1x$", lp=[3.6, 0.62]),
                           dict(type="courbe", pts=GEND_B, c="te", ep=2.6, lbl="$y=-\\frac1x$", lp=[3.6, -0.62]),
                           dict(type="texte", x=14.5, y=0.75, t="les gendarmes tendent vers $0$", c="sa")]),
        "g_xcos": dict(type="graphe", titre="$g(x)=x+\\cos x\\geq x-1$", x=290, y=110, w=700, h=560,
                       ax=dict(x=[0, 12.5], y=[-2, 13], gx=[4, 8, 12], gy=[4, 8, 12], lx="$x$", ly="$y$"),
                       el=[dict(type="courbe", pts=XCOS, c="iv", ep=3.2, dur=2.4),
                           dict(type="droite", pts=[[0, -1], [12.5, 11.5]], c="te", ep=2.6, lbl="$y=x-1$", lp=[10.4, 6.6]),
                           dict(type="texte", x=3.3, y=10.5, t="$x-1\\to+\\infty$ : $g\\to+\\infty$", c="sa")]),
        "tag_bo": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=650, y=40, w=560),
        "dem_e": dict(type="formule", copie=True, titre="Démonstration : les limites de l'exponentielle", x=90, y=92, w=1100, lignes=[
            dict(lab="En $+\\infty$.", f="$g(x)=\\e^x-x$, $g'(x)=\\e^x-1$", taille=30),
            dict(f="$g'(x)\\leq0$ sur $]-\\infty;0]$, $g'(x)\\geq0$ sur $[0;+\\infty[$", ind=True, taille=30),
            dict(f="minimum en $0$ : $g(0)=\\e^0-0=1>0$", ind=True, taille=30),
            dict(f="donc $\\e^x>x$ pour tout réel $x$", ind=True, hl=True, taille=30),
            dict(f="$x\\to+\\infty$ : par comparaison, $\\lim_{x\\to+\\infty}\\e^x=+\\infty$", ind=True, cadre=True, taille=30),
            dict(lab="En $-\\infty$.", f="$\\e^x=\\dfrac1{\\e^{-x}}$ ; on pose $X=-x$", taille=30),
            dict(f="$x\\to-\\infty$ : $X\\to+\\infty$ et $\\e^X\\to+\\infty$", ind=True, taille=30),
            dict(f="$\\dfrac1{\\e^X}\\to0$ : $\\lim_{x\\to-\\infty}\\e^x=0$", ind=True, cadre=True, taille=30)]),
    }),

    # ================================================================ VII. croissances comparées
    dict(id="croissances", chap="Les croissances comparées", fond="ardoise", humeur="mystere",
         retenir="Pour tout entier $n\\geq1$ : $\\frac{\\e^x}{x^n}\\to+\\infty$ et $x^n\\e^{-x}\\to0$ en $+\\infty$ ; $x^n\\e^x\\to0$ en $-\\infty$. L'exponentielle l'emporte sur toute puissance.",
         beats=[
        "{q_cc}Exponentielle de x, sur x, en plus l'infini. Le haut tend vers plus l'infini, le bas aussi : forme infini sur infini. Qui gagne ?",
        "{-q_cc}{duel}Faisons un duel plus serré : exponentielle de x contre x puissance dix. {duel.1}En x égale dix, x puissance dix vaut dix milliards. "
        "Exponentielle de dix, environ vingt-deux mille. La puissance écrase l'exponentielle.",
        "{duel.2}Mais en x égale cent ? Cent puissance dix, c'est un suivi de vingt zéros. "
        "Exponentielle de cent, environ deux virgule sept fois dix puissance quarante-trois. L'exponentielle a pris l'avantage. Et elle ne le rendra plus.",
        "{-duel}{py_d}Où se fait le dépassement ? Ce programme le cherche par dichotomie, une méthode que tu verras au chapitre suivant. "
        "{py_d.s}Réponse : vers trente-cinq virgule soixante-dix-sept. Au-delà, l'exponentielle est devant, pour toujours.",
        "{-py_d}{thm_cc}C'est le théorème des {!croissances comparées}croissances comparées. Pour tout entier n supérieur ou égal à un : "
        "{thm_cc.1}en plus l'infini, exponentielle de x, divisée par x puissance n, tend vers plus l'infini. "
        "{thm_cc.2}En plus l'infini, x puissance n fois exponentielle de moins x tend vers zéro. "
        "{thm_cc.3}Et en moins l'infini, x puissance n fois exponentielle de x tend vers zéro.",
        "{thm_cc.4}Une seule phrase pour tout retenir : l'exponentielle l'emporte sur toute puissance.",
        "{-thm_cc}{tag_bo2}{dem_cc}La première de ces limites est une démonstration exigible. Allons-y. "
        "{dem_cc.1}Étape un, avec n égale un. On étudie h de x égale exponentielle de x, moins x au carré sur deux, pour x positif. "
        "{dem_cc.2}Sa dérivée vaut exponentielle de x, moins x : on vient de montrer que c'est strictement positif. "
        "{dem_cc.3}Donc h est croissante, et h de x est supérieur ou égal à h de zéro, qui vaut un.",
        "{dem_cc.4}Ainsi exponentielle de x est plus grand que x au carré sur deux. On divise par x, positif : "
        "exponentielle de x sur x est plus grand que x sur deux. {dem_cc.5}Et x sur deux tend vers plus l'infini. Par comparaison, exponentielle de x sur x aussi.",
        "{-dem_cc}{dem_n}{dem_n.1}Étape deux, pour n quelconque. L'astuce : écrire exponentielle de x comme : exponentielle de, x sur n, le tout à la puissance n. "
        "{dem_n.2}On obtient : un sur n puissance n, fois, exponentielle de x sur n, sur x sur n, le tout à la puissance n.",
        "{dem_n.3}On pose grand X égale x sur n, qui tend vers plus l'infini. D'après l'étape un, exponentielle de grand X sur grand X tend vers plus l'infini. "
        "{dem_n.4}Sa puissance n-ième aussi, et le produit par la constante positive un sur n puissance n aussi. C'est démontré.",
        "{-dem_n}{-tag_bo2}{csq}Les deux autres limites s'en déduisent. {csq.1}x puissance n fois exponentielle de moins x, "
        "c'est l'inverse du quotient : exponentielle de x, divisée par x puissance n. L'inverse de quelque chose qui tend vers plus l'infini tend vers zéro.",
        "{csq.2}Et en moins l'infini, on pose grand X égale moins x : x puissance n fois exponentielle de x devient, au signe près, "
        "grand X puissance n fois exponentielle de moins grand X. Qui tend vers zéro.",
        "{-csq}{g_x2e}Regarde la courbe de x au carré, fois exponentielle de moins x. {g_x2e.1}Au début, la puissance domine : la courbe monte. "
        "{g_x2e.2}Puis l'exponentielle reprend le dessus, et écrase tout vers zéro. L'axe des abscisses est asymptote en plus l'infini.",
        "{-g_x2e}{fact}La méthode, quand une forme indéterminée mélange exponentielle et puissances : on factorise par le terme qui domine. "
        "{fact.1}Exemple : exponentielle de x, moins x au cube, en plus l'infini. Forme infini moins infini. "
        "{fact.2}On factorise par exponentielle de x : il reste un, moins x au cube sur exponentielle de x. "
        "{fact.3}Par croissances comparées, x au cube sur exponentielle de x tend vers zéro. La parenthèse tend vers un, et le tout vers plus l'infini.",
        "{-fact}{bac26}Au bac, ça tombe sous forme de vrai ou faux. En juin deux mille vingt-six, un sujet affirmait : "
        "{bac26.1}la limite en plus l'infini de x plus un, fois exponentielle de moins x, vaut plus l'infini. Vrai ou faux ?",
        "{bac26.2}Faux ! On développe : x fois exponentielle de moins x, plus exponentielle de moins x. "
        "{bac26.3}Le premier tend vers zéro par croissances comparées, le second vers zéro. La limite vaut zéro.",
        "{-bac26}{obl}Pour aller plus loin, et ce n'est pas exigible : les asymptotes obliques. "
        "Si l'écart entre f de x et a x plus b tend vers zéro en plus l'infini, la droite d'équation y égale a x plus b est asymptote oblique.",
        "{-obl}",
    ], vis={
        "q_cc": dict(type="question", t="$\\dfrac{\\e^x}{x}$ en $+\\infty$ : forme $\\frac\\infty\\infty$. Qui gagne ?"),
        "duel": dict(type="formule", titre="Le duel : $\\e^x$ contre $x^{10}$", x=150, y=170, w=980, lignes=[
            dict(f="$x=10$ : $x^{10}=10^{10}$ et $\\e^{10}\\approx22\\,026$", m="la puissance mène", taille=38),
            dict(f="$x=100$ : $x^{10}=10^{20}$ et $\\e^{100}\\approx2{,}7\\times10^{43}$", m="l'exponentielle gagne", taille=38)]),
        "py_d": dict(type="code", titre="Python · quand l'exponentielle dépasse $x^{10}$", x=190, y=110, w=900, taille=26, lignes=[
            "import math", "", "a, b = 11, 100     # e^x < x^10 en 11, > en 100", "for k in range(50):",
            "    m = (a + b) / 2", "    if math.exp(m) > m**10:", "        b = m", "    else:", "        a = m", "print(round(b, 4))"],
            sortie="35.7715"),
        "thm_cc": dict(type="formule", titre="Croissances comparées ($n\\geq1$)", x=170, y=140, w=940, lignes=[
            dict(f="$\\lim_{x\\to+\\infty}\\dfrac{\\e^x}{x^n}=+\\infty$", taille=42),
            dict(f="$\\lim_{x\\to+\\infty}x^n\\e^{-x}=0$", taille=42),
            dict(f="$\\lim_{x\\to-\\infty}x^n\\e^x=0$", taille=42),
            dict(f="l'exponentielle l'emporte sur toute puissance", txt=True, cadre=True)]),
        "tag_bo2": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=650, y=40, w=560),
        "dem_cc": dict(type="formule", copie=True, titre="Démonstration : $\\dfrac{\\e^x}{x}\\to+\\infty$", x=100, y=100, w=1080, lignes=[
            dict(lab="Étape 1.", f="$h(x)=\\e^x-\\dfrac{x^2}2$ sur $[0;+\\infty[$", taille=32),
            dict(f="$h'(x)=\\e^x-x>0$", ind=True, m="démonstration précédente", taille=32),
            dict(f="$h$ croissante : $h(x)\\geq h(0)=1>0$", ind=True, taille=32),
            dict(f="$\\e^x>\\dfrac{x^2}2$, donc pour $x>0$ : $\\dfrac{\\e^x}x>\\dfrac x2$", ind=True, taille=32),
            dict(f="$\\dfrac x2\\to+\\infty$ : par comparaison, $\\dfrac{\\e^x}x\\to+\\infty$", ind=True, cadre=True, taille=32)]),
        "dem_n": dict(type="formule", copie=True, titre="Étape 2 : $n$ quelconque", x=100, y=130, w=1080, lignes=[
            dict(f="$\\e^x=\\left(\\e^{x/n}\\right)^n$", taille=38),
            dict(f="$\\dfrac{\\e^x}{x^n}=\\dfrac1{n^n}\\left(\\dfrac{\\e^{x/n}}{x/n}\\right)^n$", ind=True, taille=38),
            dict(f="$X=\\dfrac xn\\to+\\infty$ et $\\dfrac{\\e^X}X\\to+\\infty$", ind=True, m="étape 1", taille=34),
            dict(f="puissance $n$-ième, constante $\\dfrac1{n^n}>0$ : $\\dfrac{\\e^x}{x^n}\\to+\\infty$", ind=True, cadre=True, taille=32)]),
        "csq": dict(type="formule", titre="Les conséquences", x=130, y=170, w=1020, lignes=[
            dict(f="$x^n\\e^{-x}=\\dfrac1{\\e^x/x^n}\\to0$", m="en $+\\infty$", taille=38),
            dict(f="$X=-x$ : $x^n\\e^x=(-1)^nX^n\\e^{-X}\\to0$", m="en $-\\infty$", taille=38)]),
        "g_x2e": dict(type="graphe", titre="$x^2\\e^{-x}$ : la puissance, puis l'exponentielle", x=190, y=140, w=900, h=480,
                      ax=dict(x=[0, 14.5], y=[0, 0.7], gx=[2, 4, 8, 12], gy=[0.2, 0.4, 0.6], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=X2E[:21], c="iv", ep=3.4, dur=1.2),
                          dict(type="courbe", pts=X2E[20:], c="iv", ep=3.4, dur=2.2),
                          dict(type="texte", x=10.4, y=0.36, t="$\\to0$ en $+\\infty$", c="sa")]),
        "fact": dict(type="formule", copie=True, titre="Factoriser par l'exponentielle", x=130, y=150, w=1020, lignes=[
            dict(f="$\\lim_{x\\to+\\infty}\\left(\\e^x-x^3\\right)$", m="forme $\\infty-\\infty$", taille=36),
            dict(f="$\\e^x-x^3=\\e^x\\left(1-\\dfrac{x^3}{\\e^x}\\right)$", ind=True, taille=36),
            dict(f="$\\dfrac{x^3}{\\e^x}\\to0$, la parenthèse $\\to1$ : limite $+\\infty$", ind=True, cadre=True, taille=34)]),
        "bac26": dict(type="formule", titre="Vrai ou faux ? (bac, juin 2026)", x=130, y=170, w=1020, lignes=[
            dict(f="« $\\lim_{x\\to+\\infty}(x+1)\\e^{-x}=+\\infty$ »", taille=38),
            dict(f="$(x+1)\\e^{-x}=x\\e^{-x}+\\e^{-x}\\to0+0=0$", taille=38),
            dict(f="Faux : la limite vaut $0$", ko=True, cadre=True, taille=38)]),
        "obl": dict(type="note", titre="Pour aller plus loin", cles=["oblique", "exigible"],
                    t="Hors programme : si $f(x)-(ax+b)\\to0$ en $+\\infty$, la droite $y=ax+b$ est asymptote oblique. Ce n'est pas exigible.",
                    x=170, y=200, w=940),
    }),

    # ================================================================ VIII. les pièges
    dict(id="pieges", chap="Les pièges classiques", fond="craie", humeur="tension",
         retenir="Le côté en une valeur interdite ; jamais « $\\frac30$ » ; une courbe peut couper son asymptote ; en $0$, le plus bas degré ; l'exponentielle gagne toujours.",
         beats=[
        "{pieges}Faisons le tour des pièges. {pieges.1}Un : oublier le côté. La limite en un de un sur, x moins un, n'existe pas : "
        "plus l'infini à droite, moins l'infini à gauche. Fais toujours le tableau de signes du dénominateur.",
        "{pieges.2}Deux : écrire « trois sur zéro ». On ne divise pas par zéro, on étudie un dénominateur qui tend vers zéro, avec son signe.",
        "{pieges.3}Trois : croire qu'une courbe ne coupe jamais son asymptote. Sinus de x sur x la traverse une infinité de fois.",
        "{pieges.4}Quatre : factoriser par le mauvais terme. En plus ou moins l'infini, le plus haut degré domine ; en zéro, le plus bas.",
        "{pieges.5}Et cinq : les croissances comparées à l'envers. x puissance cent sur exponentielle de x tend vers zéro, "
        "même si, en dix, x puissance cent est gigantesque. Et en moins l'infini, x puissance n fois exponentielle de x tend vers zéro, pas vers l'infini.",
        "{-pieges}{asym}Et pour finir, la fiche réflexe des asymptotes. {asym.1}Une limite finie L en plus ou moins l'infini : asymptote horizontale, y égale L. "
        "{asym.2}Une limite infinie en un réel a, d'un côté au moins : asymptote verticale, x égale a. On cherche a parmi les valeurs interdites. "
        "{asym.3}Et la position relative : le signe de f de x, moins L.",
        "{-asym}",
    ], vis={
        "pieges": dict(type="liste", titre="Les pièges classiques", items=[
            "Oublier le côté : $\\lim_{x\\to1}\\frac1{x-1}$ n'existe pas", "Écrire « $\\frac30=\\infty$ »",
            "Une courbe peut couper son asymptote", "En $0$, le plus bas degré domine",
            "$\\frac{x^{100}}{\\e^x}\\to0$ ; $x^n\\e^x\\to0$ en $-\\infty$"],
            marques=["!", "!", "!", "!", "!"], x=150, y=110, w=980),
        "asym": dict(type="liste", titre="Trouver une asymptote", items=[
            "$\\lim_{x\\to\\pm\\infty}f(x)=\\ell$ : asymptote horizontale $y=\\ell$",
            "$\\lim_{x\\to a}f(x)=\\pm\\infty$ : asymptote verticale $x=a$",
            "Position relative : signe de $f(x)-\\ell$"], marques=["→", "→", "→"], x=150, y=170, w=980),
    }),

    # ================================================================ IX. exercice 1
    dict(id="exo1", chap="Exercice 1 · limites et asymptotes", fond="ardoise", humeur="tension", beats=[
        "{ex1}Place à l'entraînement. Premier exercice : déterminer des limites, et en déduire les asymptotes. "
        "Un : f de x égale quatre x moins trois, sur deux x plus un, en plus et moins l'infini, et en moins un demi. "
        "Deux : g de x égale x au cube, moins cinq x au carré, plus un, en moins l'infini et en plus l'infini. "
        "Trois : k de x égale trois, moins exponentielle de moins x, en plus l'infini.",
        "{-ex1}{pa1}À toi. Mets la vidéo sur pause, et cherche les trois.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Question un. En plus ou moins l'infini, on prend le quotient des termes de plus haut degré : "
        "quatre x sur deux x, c'est deux. f tend vers deux, et la droite d'équation y égale deux est asymptote horizontale.",
        "{s11.2}En moins un demi, le numérateur tend vers quatre fois moins un demi, moins trois : moins deux moins trois, moins cinq. "
        "{s11.3}Le dénominateur tend vers zéro, et il est positif quand x est plus grand que moins un demi.",
        "{s11.4}Donc, à droite de moins un demi : moins cinq sur un petit nombre positif, f tend vers moins l'infini. "
        "{s11.5}À gauche : moins cinq sur un petit nombre négatif, plus l'infini. {s11.6}La droite d'équation x égale moins un demi est asymptote verticale.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux. Un polynôme se comporte comme son terme de plus haut degré : x au cube. "
        "{s12.2}Donc g tend vers moins l'infini en moins l'infini, et vers plus l'infini en plus l'infini. "
        "{s12.3}Pas de limite finie, pas d'asymptote.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois. Exponentielle de moins x tend vers zéro en plus l'infini, par composition : moins x tend vers moins l'infini. "
        "{s13.2}Donc k tend vers trois moins zéro, c'est-à-dire trois. Asymptote horizontale : y égale trois. "
        "{s13.3}Et comme exponentielle de moins x est strictement positive, k de x est plus petit que trois : la courbe est en dessous de son asymptote.",
        "{-s13}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", etiquette="Exercice 1 · pour démarrer", titre="Limites et asymptotes",
                    enonce=["Déterminer les limites demandées et en déduire les asymptotes éventuelles."],
                    questions=["$f(x)=\\dfrac{4x-3}{2x+1}$ en $\\pm\\infty$ et en $-\\frac12$.",
                               "$g(x)=x^3-5x^2+1$ en $-\\infty$ et en $+\\infty$.",
                               "$k(x)=3-\\e^{-x}$ en $+\\infty$."]),
        "pa1": dict(type="pause", t="Les limites de $f$, $g$ et $k$, puis les asymptotes."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", etiquette="Exercice 1", titre="Limites et asymptotes",
                     donnees=["$f(x)=\\frac{4x-3}{2x+1}$", "$g(x)=x^3-5x^2+1$", "$k(x)=3-\\e^{-x}$"],
                     questions=["$f$ en $\\pm\\infty$, en $-\\frac12$", "$g$ en $\\pm\\infty$", "$k$ en $+\\infty$"]),
        "s11": dict(type="formule", titre="1 · La fonction $f$", x=530, y=80, w=720, lignes=[
            dict(f="en $\\pm\\infty$ : $\\dfrac{4x}{2x}=2$ ; asymptote $y=2$", taille=29),
            dict(f="en $-\\frac12$ : $4x-3\\to-5$", taille=29),
            dict(f="$2x+1\\to0$, positif si $x>-\\frac12$", taille=29),
            dict(f="$\\lim_{x\\to(-\\frac12)^+}f(x)=-\\infty$", ind=True, taille=29),
            dict(f="$\\lim_{x\\to(-\\frac12)^-}f(x)=+\\infty$", ind=True, taille=29),
            dict(f="asymptote verticale $x=-\\frac12$", cadre=True, taille=29)]),
        "s12": dict(type="formule", titre="2 · La fonction $g$", x=550, y=170, w=690, lignes=[
            dict(f="comme $x^3$ en $\\pm\\infty$", taille=36),
            dict(f="$\\lim_{-\\infty}g=-\\infty$, $\\lim_{+\\infty}g=+\\infty$", taille=36),
            dict(f="pas d'asymptote", txt=True)]),
        "s13": dict(type="formule", titre="3 · La fonction $k$", x=550, y=150, w=690, lignes=[
            dict(f="$-x\\to-\\infty$ donc $\\e^{-x}\\to0$", m="composition", taille=33),
            dict(f="$\\lim_{x\\to+\\infty}k(x)=3$ : asymptote $y=3$", cadre=True, taille=33),
            dict(f="$\\e^{-x}>0$ : $k(x)<3$, courbe en dessous", taille=33)]),
    }),

    # ================================================================ X. exercice 2 (type bac)
    dict(id="exo2", chap="Exercice 2 · type bac", fond="carnet", humeur="tension", beats=[
        "{ex2}Deuxième exercice, au format du bac : une étude complète. f est définie sur R par f de x égale deux x moins un, "
        "fois exponentielle de x. On note C sa courbe.",
        "Quatre questions. Un : la limite de f en plus l'infini. Deux : la limite en moins l'infini, et son interprétation graphique. "
        "Trois : montrer que f prime de x égale deux x plus un, fois exponentielle de x, et dresser le tableau de variations complet. "
        "Quatre : résoudre f de x égale zéro, et étudier le signe de f.",
        "{-ex2}{pa2}C'est un vrai sujet de bac. Prends le temps : mets sur pause, et rédige tout.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un. En plus l'infini, deux x moins un tend vers plus l'infini, "
        "et exponentielle de x aussi. {s21.2}Par produit, f tend vers plus l'infini. Pas de piège ici.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux. En moins l'infini, deux x moins un tend vers moins l'infini, mais exponentielle de x tend vers zéro. "
        "Forme zéro fois l'infini : indéterminée.",
        "{s22.2}On développe : f de x égale deux fois x exponentielle de x, moins exponentielle de x. "
        "{s22.3}Par croissances comparées, x exponentielle de x tend vers zéro en moins l'infini. Et exponentielle de x aussi. "
        "{s22.4}Donc f tend vers zéro. {s22.5}Interprétation : l'axe des abscisses, la droite d'équation y égale zéro, est asymptote horizontale à C en moins l'infini.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois. f est un produit : u fois v, avec u de x égale deux x moins un, et v de x égale exponentielle de x. "
        "{s23.2}f prime égale u prime v plus u v prime : deux exponentielle de x, plus deux x moins un, fois exponentielle de x. "
        "{s23.3}On factorise par exponentielle de x : deux, plus deux x moins un, ça fait deux x plus un. C'est bien la formule.",
        "{s23.4}Comme exponentielle de x est strictement positive, f prime a le signe de deux x plus un : "
        "négatif avant moins un demi, positif après.",
        "{s23.5}Donc f décroît, depuis la limite zéro en moins l'infini, jusqu'à son minimum en moins un demi. "
        "{s23.6}Le minimum vaut deux fois moins un demi, moins un, c'est-à-dire moins deux, fois exponentielle de moins un demi. "
        "Environ moins un virgule deux cent treize. {s23.7}Puis f croît vers plus l'infini.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre. Exponentielle de x n'est jamais nulle. Donc f de x égale zéro équivaut à deux x moins un égale zéro, "
        "c'est-à-dire x égale un demi. {s24.2}Le signe de f est celui de deux x moins un : f est négative avant un demi, positive après.",
        "{-s24}{g_bac}{g_bac.1}{g_bac.2}Et voici la courbe, qui résume tout. {g_bac.3}En moins l'infini, elle se colle à l'axe des abscisses, "
        "par en dessous, puisque f est négative de ce côté. {g_bac.4}Elle descend jusqu'au minimum, en moins un demi, "
        "{g_bac.5}remonte, coupe l'axe en un demi, et file vers plus l'infini.",
        "{-g_bac}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Une étude complète",
                    enonce=["Soit $f$ définie sur $\\R$ par $f(x)=(2x-1)\\e^x$, de courbe $\\mathcal C$."],
                    questions=["Déterminer la limite de $f$ en $+\\infty$.",
                               "Déterminer la limite de $f$ en $-\\infty$. Interpréter graphiquement.",
                               "Montrer que $f'(x)=(2x+1)\\e^x$ et dresser le tableau de variations complet de $f$.",
                               "Résoudre $f(x)=0$ et étudier le signe de $f$."]),
        "pa2": dict(type="pause", t="Les deux limites, la dérivée et les variations, puis le signe de $f$."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", etiquette="Exercice 2 · type bac", titre="Une étude complète",
                     donnees=["$f(x)=(2x-1)\\e^x$"],
                     questions=["limite en $+\\infty$", "limite en $-\\infty$", "$f'$ et variations", "$f(x)=0$, signe"]),
        "s21": dict(type="formule", titre="1 · En $+\\infty$", x=550, y=200, w=690, lignes=[
            dict(f="$2x-1\\to+\\infty$ et $\\e^x\\to+\\infty$", taille=36),
            dict(f="par produit, $\\lim_{x\\to+\\infty}f(x)=+\\infty$", cadre=True, taille=36)]),
        "s22": dict(type="formule", titre="2 · En $-\\infty$", x=540, y=100, w=710, lignes=[
            dict(f="forme $(-\\infty)\\times0$ : indéterminée", ko=True, taille=31),
            dict(f="$f(x)=2x\\e^x-\\e^x$", taille=33),
            dict(f="$x\\e^x\\to0$ (croissances comparées), $\\e^x\\to0$", taille=31),
            dict(f="$\\lim_{x\\to-\\infty}f(x)=0$", cadre=True, taille=33),
            dict(f="$y=0$ : asymptote horizontale à $\\mathcal C$ en $-\\infty$", taille=31)]),
        "s23": dict(type="formule", copie=True, titre="3 · Dérivée et variations", x=530, y=76, w=720, lignes=[
            dict(f="$u(x)=2x-1$, $v(x)=\\e^x$ : $f'=u'v+uv'$", taille=27),
            dict(f="$f'(x)=2\\e^x+(2x-1)\\e^x$", taille=27),
            dict(f="$f'(x)=(2x+1)\\e^x$", cadre=True, taille=27),
            dict(f="$\\e^x>0$ : signe de $2x+1$, nul en $-\\frac12$", taille=27),
            dict(f="$f$ décroît de $0$ (limite) jusqu'à $f\\left(-\\frac12\\right)$", taille=27),
            dict(f="$f\\left(-\\frac12\\right)=-2\\e^{-\\frac12}\\approx-1{,}213$", ind=True, taille=27),
            dict(f="puis $f$ croît vers $+\\infty$", taille=27)]),
        "s24": dict(type="formule", titre="4 · Signe de $f$", x=550, y=170, w=690, lignes=[
            dict(f="$\\e^x\\neq0$ : $f(x)=0\\iff2x-1=0\\iff x=\\frac12$", taille=31),
            dict(f="$f(x)<0$ sur $\\left]-\\infty;\\frac12\\right[$", taille=33),
            dict(f="$f(x)>0$ sur $\\left]\\frac12;+\\infty\\right[$", taille=33)]),
        "g_bac": dict(type="graphe", titre="La courbe $\\mathcal C$", x=560, y=110, w=680, h=560,
                      ax=dict(x=[-7, 1.8], y=[-1.6, 4.2], gx=[-6, -4, -2, 1], gy=[-1, 1, 2, 3, 4], lx="$x$", ly="$y$"),
                      el=[dict(type="droite", pts=[[-7, 0], [0, 0]], c="ca", ep=3.4, lbl="asymptote $y=0$", lp=[-4.6, 0.55]),
                          dict(type="courbe", pts=FB[:110], c="iv", ep=3.4, dur=2.2),
                          dict(type="point", x=-0.5, y=MIN_FB, c="sa", lbl="minimum", lp=[-3.0, -1.25]),
                          dict(type="courbe", pts=FB[109:], c="iv", ep=3.4, dur=1.4),
                          dict(type="point", x=0.5, y=0, c="te")]),
    }),

    # ================================================================ XI. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="craie", humeur="lumiere", beats=[
        "{carte}Récapitulons. Au centre : les limites, le comportement aux bords. "
        "{carte.1}Les asymptotes : horizontale pour une limite finie en l'infini, verticale pour une limite infinie en un réel. "
        "{carte.2}Les références : les puissances, leurs inverses, et l'exponentielle, qui tend vers zéro en moins l'infini. "
        "{carte.3}Les outils : les opérations, la factorisation du terme prépondérant, la composition, la comparaison et les gendarmes. "
        "{carte.4}Et les croissances comparées : l'exponentielle l'emporte sur toute puissance.",
        "{-carte}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Lire ou justifier une asymptote, horizontale ou verticale. "
        "{bac.2}Étudier une limite en une valeur interdite, à gauche et à droite. "
        "{bac.3}Lever une forme indéterminée, en factorisant. {bac.4}Rédiger une composition. "
        "{bac.5}Utiliser les croissances comparées, et refaire les deux démonstrations exigibles. "
        "{bac.6}Et encadrer avec un cosinus, pour les gendarmes ou la comparaison.",
        "Si tu sais faire ces six choses, ce chapitre est à toi. Les fiches, les QCM et les animations du chapitre t'attendent sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, un quiz sur cette vidéo t'y attend aussi.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="LIMITES · le comportement aux bords", branches=[
            dict(t="Asymptotes", items=["limite finie en $\\pm\\infty$ : $y=\\ell$", "limite infinie en $a$ : $x=a$", "position : signe de $f(x)-\\ell$"]),
            dict(t="Références", items=["$x^n$, $\\frac1{x^n}$, $\\sqrt x$", "$\\e^x\\to+\\infty$ en $+\\infty$", "$\\e^x\\to0$ en $-\\infty$"]),
            dict(t="Outils", items=["terme prépondérant", "composition : $X=u(x)$", "comparaison, gendarmes"]),
            dict(t="Croissances comparées", items=["$\\frac{\\e^x}{x^n}\\to+\\infty$", "$x^n\\e^{-x}\\to0$", "$x^n\\e^x\\to0$ en $-\\infty$"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Lire ou justifier une asymptote", "Une limite en une valeur interdite, des deux côtés",
            "Lever une forme indéterminée", "Rédiger une composition",
            "Croissances comparées et les deux démonstrations", "Encadrer avec $\\cos$ ou $\\sin$"],
            marques=["✓"] * 6, x=150, y=96, w=980),
    }),
]

QUIZ = [
    dict(q="lim (4x² − 1)/(2x² + x) quand x → +∞ vaut…", r=["0", "2", "+∞"], ok=1,
         ex="Quotient des termes de plus haut degré : 4x²/2x² = 2.", voir="poly"),
    dict(q="Si lim f(x) = 3 quand x → +∞, alors…",
         r=["la droite x = 3 est asymptote verticale", "la droite y = 3 est asymptote horizontale en +∞", "f(x) < 3 pour tout x"],
         ok=1, ex="Limite finie en l'infini : asymptote horizontale. La position relative demande l'étude du signe de f(x) − 3.", voir="def_lim"),
    dict(q="lim 1/(x − 2) quand x → 2 avec x < 2 vaut…", r=["+∞", "−∞", "0"], ok=1,
         ex="Pour x < 2, x − 2 est négatif et tend vers 0 : le quotient tend vers −∞.", voir="cotes"),
    dict(q="lim eˣ quand x → −∞ vaut…", r=["−∞", "0", "1"], ok=1,
         ex="L'axe des abscisses est asymptote à la courbe de l'exponentielle en −∞.", voir="g_exp"),
    dict(q="lim x⁵e⁻ˣ quand x → +∞ vaut…", r=["+∞", "0", "on ne peut pas savoir"], ok=1,
         ex="Croissances comparées : l'exponentielle l'emporte sur toute puissance.", voir="thm_cc"),
    dict(q="lim e^(−x²) quand x → +∞ vaut…", r=["0", "1", "+∞"], ok=0,
         ex="Composition : X = −x² tend vers −∞, et eˣ tend vers 0 en −∞.", voir="red_c"),
    dict(q="lim (x² − 1)/(x − 1) quand x → 1 vaut…", r=["0", "2", "n'existe pas"], ok=1,
         ex="Forme 0/0 : on simplifie par x − 1, il reste x + 1, qui tend vers 2.", voir="zz"),
    dict(q="lim cos(x)/x quand x → +∞ vaut…", r=["0", "1", "n'existe pas"], ok=0,
         ex="Gendarmes : −1/x ≤ cos(x)/x ≤ 1/x pour x > 0, et ±1/x tendent vers 0.", voir="g_gend"),
    dict(q="Près de 0, x³ + 2x se comporte comme…", r=["x³", "2x", "3x"], ok=1,
         ex="En 0, c'est le terme de plus bas degré qui domine.", voir="p0"),
    dict(q="La démonstration de lim eˣ/x = +∞ s'appuie sur…",
         r=["eˣ > x²/2 pour x ≥ 0, puis la comparaison", "le théorème des gendarmes avec cos", "la quantité conjuguée"],
         ok=0, ex="h(x) = eˣ − x²/2 est croissante et h(0) = 1, donc eˣ/x > x/2 pour x > 0.", voir="dem_cc"),
]

CREDITS = [
    "Animations, schémas, graphiques et exercices : faits pour le site. "
    "Polices : Carnet Math (sous-ensemble de STIX Two Math), Caveat, Spectral, Archivo, JetBrains Mono, sous licence SIL OFL.",
]
