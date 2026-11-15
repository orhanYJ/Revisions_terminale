"""Maths, chapitre 4 : « Dérivation, convexité, continuité » — le cours en vidéo (site CQFD).

Même chaîne que la vidéo pilote du chapitre 1 (outils/serie-maths/maths_ch1.py) et que celle du chapitre 3 :
outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots ; moteur maths/serie/moteur.js (tableau noir) :
formules en MathML, rédaction au tableau (formule copie=True), code Python, graphiques tracés à la règle ; illustrations
propres à la vidéo dans maths/serie/illu-maths-ch4.js (tangente qui glisse le long d'une courbe, dichotomie pas à pas).
Contenu : le chapitre 4 du site (outils/specialites/maths/src/ch4.js), rien au-delà ; ce qui dépasse le programme est dit
« hors programme » ou « pour aller plus loin ». Les deux exercices sont ceux du site (unique solution de x³ − 3x + 1 = 0 ;
étude de eˣ − x − 2, type bac). Chaque calcul affiché ou dit est vérifié par outils/serie-maths/verif_ch4.py.
Usage : PYTHONPATH=outils/serie-maths python3 outils/serie-philo/verifier.py maths_ch4
        PYTHONPATH=outils/serie-maths SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py maths_ch4   (brouillon)
        python3 outils/serie-philo/chevauchements.py maths-ch4
"""
from math import exp, sqrt

SITE = "maths"
CODE = "maths-ch4"
NOTION = "Dérivation, convexité, continuité"
NUM = 4
TITRE = "Dérivation, convexité, continuité"
SUIVANT = "Chapitre 5 · Dénombrement et combinatoire"
RYTHME = "vivant"
# 1) d'abord les produits « nombre lettre » : jamais de liaison entre un nombre et une lettre (« deux‿x »), on dit
#    « deux fois x » (le texte lu l'écrit déjà presque partout ; ces clés rattrapent un oubli) ;
# 2) puis le bloc du chapitre 1 (lettres des formules en majuscules : la voix les dit comme des lettres, sans liaison),
#    complété par les lettres de ce chapitre (g, h, k, y) ; le texte lu évite « il y a », « en a », « tout x » ;
# 3) « plusse » et « moin » devant une lettre ou un nombre qui commence par une voyelle.
PRONONCIATION = {}
for _n in ("deux", "trois", "quatre", "cinq", "six", "douze", "quinze", "seize"):
    for _l in ("x", "u", "a", "n", "f", "m"):
        PRONONCIATION[_n + " " + _l] = _n + " fois " + _l
PRONONCIATION.update({"§n": "N", "§k": "K", "§f": "F", "§x": "X", "§b": "B", "§v": "V", "§m": "M", "§q": "Q",
                      "§g": "G", "§h": "H", "§y": "Y"})
for _tok in ("un", "une", "huit", "onze", "a", "u", "N", "F", "X", "M", "R", "A", "U", "L", "H", "Y"):
    PRONONCIATION["plus " + _tok] = "plusse " + _tok
    PRONONCIATION["moins " + _tok] = "moin " + _tok
LIAISONS = "maths"


# ---------------------------------------------------------------- données des graphiques (vérifiées par verif_ch4.py)
def trace(f, a, b, n=120, y=None):
    """Points de la courbe de f sur [a ; b], arrondis ; y = (bas, haut) : on vérifie que tout reste dans le cadre."""
    pts = [[round(a + (b - a) * i / n, 4), round(f(a + (b - a) * i / n), 4)] for i in range(n + 1)]
    if y:
        assert all(y[0] - 1e-6 <= p[1] <= y[1] + 1e-6 for p in pts), (a, b)
    return pts


def CUBE(x):
    return x ** 3 + x - 1


def G3(x):
    return x ** 3 - 3 * x + 1


OUV = trace(CUBE, -0.4, 1.2, 100, (-1.6, 2.0))                       # x³ + x − 1 : −1 en 0, 1 en 1
X4 = trace(lambda x: x ** 4, -1.38, 1.38, 120, (0, 3.7))              # x⁴ : convexe, pas d'inflexion en 0
EXPM = trace(lambda x: exp(-x), -1.45, 4, 120, (0, 4.4))              # e^(−x) : convexe et décroissante
EXP = trace(exp, -3, 2, 120, (0, 7.5))                                # eˣ et sa tangente y = x + 1
RAC = trace(sqrt, 0, 9.6, 160, (0, 3.2))                              # √x et sa tangente y = (x + 1)/2
TVI3 = trace(G3, -2, 2, 160, (-1.2, 3.2))                             # x³ − 3x + 1 : trois solutions de f(x) = 0
SAUT_G = trace(lambda x: x / 2, 0, 0.98, 20, (0, 2.6))                # une fonction qui saute par-dessus k = 1,2
SAUT_D = trace(lambda x: x / 2 + 1.5, 1, 2, 20, (0, 2.6))
NEWT = trace(CUBE, 0.4, 1.1, 100, (-0.6, 1.5))                         # Newton : tangentes en 1 puis en 0,75
X1N = 0.75
X2N = round(X1N - CUBE(X1N) / (3 * X1N ** 2 + 1), 6)                  # 0,686047
FBAC = trace(lambda x: exp(x) - x - 2, 0, 2.05, 120, (-2.2, 4.4))     # eˣ − x − 2 et sa tangente en 1
E1 = round(exp(1), 4)


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ardoise", humeur="mystere", carton=False, beats=[
        "{q1}Voici une équation toute simple en apparence : x au cube, plus x, moins un, égale zéro.",
        "Essaie de la résoudre. Pas de discriminant, pas de factorisation évidente. Aucune formule du lycée ne donne la réponse.",
        "Et pourtant, regarde. {-q1}{g0}{g0.1}Pour x égale zéro, l'expression vaut moins un : c'est négatif. "
        "{g0.2}Pour x égale un, elle vaut un plus un moins un : un, c'est positif.",
        "{g0.3}Entre les deux, la courbe est passée d'en dessous de l'axe à au-dessus. Elle a donc traversé l'axe quelque part. "
        "Il existe une solution entre zéro et un !",
        ("P", 0.4),
        "Mais attention : « elle a forcément traversé », c'est une intuition. Et si la courbe faisait un saut ? "
        "Et si elle traversait trois fois ? Et combien vaut cette solution, au juste ?",
        "{-g0}{q2}Pour répondre, il faut trois outils. Savoir dériver des fonctions compliquées. "
        "Savoir lire comment une courbe tourne. Et savoir quand une courbe ne peut pas sauter.",
        "{-q2}{plan}Voici le chemin. {plan.1}D'abord la dérivée d'une fonction composée, et la dérivée seconde. "
        "{plan.2}Puis la convexité : une courbe qui tourne vers le haut ou vers le bas, et les points d'inflexion. "
        "{plan.3}Ensuite la démonstration exigible, et les inégalités qu'on en tire. "
        "{plan.4}Puis la continuité, et le théorème des valeurs intermédiaires. "
        "{plan.5}La dichotomie, pour encadrer la solution, et la méthode de Newton. "
        "{plan.6}Et pour finir, les pièges et deux exercices corrigés, dont un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q1": dict(type="formule", titre="Une équation", x=230, y=200, w=820, lignes=[
            dict(f="$x^3+x-1=0$", cadre=True, taille=64),
            dict(f="aucune formule ne donne la solution", txt=True)]),
        "g0": dict(type="graphe", titre="La courbe de $x\\mapsto x^3+x-1$", x=250, y=96, w=780, h=590,
                   ax=dict(x=[-0.4, 1.4], y=[-1.6, 2.0], gx=[0.5, 1], gy=[-1, 1], lx="$x$", ly="$y$"),
                   el=[dict(type="point", x=0, y=-1, c="ca", lbl="$-1<0$", lp=[0.3, -1.05]),
                       dict(type="point", x=1, y=1, c="vert", lbl="$1>0$", lp=[1.22, 0.9]),
                       dict(type="courbe", pts=OUV, c="iv", ep=3.4, dur=2.2)]),
        "q2": dict(type="question", t="Une solution existe-t-elle vraiment ? Combien vaut-elle ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Dérivée d'une composée, dérivée seconde", "Convexité, points d'inflexion",
            "La démonstration exigible, les inégalités", "Continuité, théorème des valeurs intermédiaires",
            "Dichotomie et méthode de Newton", "Les pièges, deux exercices corrigés"], x=150, y=110, w=980),
        "titre": dict(type="titre", sur="Maths · Chapitre 4", t="Dérivation, convexité, continuité",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. dérivée d'une composée
    dict(id="composee", chap="Dérivée d'une fonction composée", fond="ardoise", humeur="lumiere",
         retenir="$(v\\circ u)'=(v'\\circ u)\\times u'$ : on dérive l'extérieur en gardant l'intérieur, puis on multiplie par la dérivée de l'intérieur. $(\\e^u)'=u'\\,\\e^u$.",
         beats=[
        "{q_comp}Commençons par une fonction qui revient sans cesse au bac : exponentielle de, moins x au carré. "
        "Comment la dériver ? Ce n'est pas une somme, ni un produit, ni un quotient.",
        "{-q_comp}{def_c}C'est une fonction dans une fonction : une {!composée}composée. "
        "{def_c.1}On applique d'abord u, qui à x associe moins x au carré. Puis on applique v, l'exponentielle, au résultat.",
        "On note v rond u : v rond u de x, c'est v de u de x. Attention à l'ordre : on lit de droite à gauche, u d'abord, v ensuite.",
        "{-def_c}{thm_c}Voici le théorème. {thm_c.1}Si u est dérivable sur un intervalle I, et v dérivable là où u prend ses valeurs, "
        "alors v rond u est dérivable. {thm_c.2}Et sa dérivée vaut : v prime rond u, fois u prime.",
        "{thm_c.3}En clair : on dérive la fonction extérieure, en gardant l'intérieur tel quel. "
        "Puis on multiplie par la dérivée de l'intérieur. Retiens bien ce u prime : c'est lui qu'on oublie.",
        "{-thm_c}{tab_c}De ce théorème, on tire quatre formules à connaître par cœur. "
        "{tab_c.1}Exponentielle de u : sa dérivée est u prime, fois exponentielle de u. "
        "{tab_c.2}u puissance n : n fois u prime, fois u puissance n moins un. "
        "{tab_c.3}Racine de u, quand u est strictement positive : u prime sur deux racine de u. "
        "{tab_c.4}Et un sur u, quand u ne s'annule pas : moins u prime, sur u au carré.",
        "{-tab_c}{exc1}Entraînons-nous sur quatre calculs. {exc1.1}Premier : trois fois x, plus un, le tout puissance cinq. "
        "Ici, u de x vaut trois fois x plus un, et u prime vaut trois. "
        "{exc1.2}La dérivée vaut cinq, fois trois, fois trois fois x plus un, puissance quatre. Cinq fois trois, ça fait quinze.",
        "{exc1.3}Deuxième : racine carrée de, x au carré plus un. u prime vaut deux fois x. "
        "{exc1.4}La dérivée vaut deux fois x, sur deux racine de x au carré plus un. Les deux se simplifient : x sur racine de x au carré plus un.",
        "{exc1.5}Troisième : exponentielle de moins x au carré, notre fonction du début. u prime vaut moins deux fois x. "
        "{exc1.6}La dérivée vaut donc moins deux fois x, fois exponentielle de moins x au carré.",
        "{-exc1}{exc2}Et un quatrième, plus costaud : k de x égale exponentielle de deux fois x, fois x moins un, le tout au cube. "
        "{exc2.1}Quelle est la dernière opération ? Un produit. On commence donc par la formule du produit : u prime v, plus u v prime.",
        "{exc2.2}La dérivée de exponentielle de deux fois x, c'est deux fois exponentielle de deux fois x. "
        "{exc2.3}La dérivée de x moins un au cube, c'est trois fois x moins un au carré : la dérivée de x moins un vaut un.",
        "{exc2.4}On assemble. {exc2.5}Et on factorise par exponentielle de deux fois x, et par x moins un au carré. "
        "Dans la parenthèse, il reste deux fois x moins un, plus trois : deux fois x plus un.",
        "{exc2.6}Résultat : exponentielle de deux fois x, fois x moins un au carré, fois deux fois x plus un. "
        "Une forme factorisée, prête pour une étude de signe.",
        "{-exc2}{meth}D'où la méthode, en une question. {meth.1}Avant de dériver, demande-toi : quelle est la dernière opération ? "
        "Une somme, un produit, un quotient, ou une composée ? {meth.2}Puis dérive de l'extérieur vers l'intérieur. "
        "{meth.3}Et à la fin, factorise : c'est le signe de la dérivée qui t'intéresse.",
        "{-meth}{piege_u}Le piège numéro un du chapitre. {piege_u.1}La dérivée de exponentielle de trois fois x au carré, "
        "ce n'est pas exponentielle de trois fois x au carré. {piege_u.2}C'est six fois x, fois exponentielle de trois fois x au carré. "
        "La dérivée d'une composée contient toujours la dérivée de l'intérieur.",
        "{-piege_u}{pq}D'où vient cette formule ? Pour comprendre, et ce n'est pas exigible : prenons exponentielle de u. "
        "{pq.1}Le taux d'accroissement s'écrit comme un produit de deux taux. {pq.2}Le second, c'est celui de u : il tend vers u prime. "
        "{pq.3}Le premier, c'est un taux de l'exponentielle, au point u de x : il tend vers exponentielle de u de x. "
        "{pq.4}D'où u prime, fois exponentielle de u. La formule générale, elle, est admise.",
        "{-pq}",
    ], vis={
        "q_comp": dict(type="question", t="Comment dériver $x\\mapsto\\,\\e^{-x^2}$ ?"),
        "def_c": dict(type="def", terme="Fonction composée", cles=["composée"],
                      t="La composée de $u$ suivie de $v$ est la fonction $v\\circ u:x\\mapsto v\\big(u(x)\\big)$ : on applique $u$, puis $v$.",
                      etape="$\\e^{-x^2}=v\\big(u(x)\\big)$ avec $u(x)=-x^2$ et $v=\\exp$.", x=150, y=170, w=980),
        "thm_c": dict(type="formule", titre="Dérivée d'une composée", x=150, y=150, w=980, lignes=[
            dict(f="$u$ dérivable sur $I$, $v$ dérivable là où $u$ prend ses valeurs :", txt=True),
            dict(f="$(v\\circ u)'=(v'\\circ u)\\times u'$", cadre=True, taille=50),
            dict(f="$\\big(v(u(x))\\big)'=v'\\big(u(x)\\big)\\times u'(x)$", n="on dérive l'extérieur, puis on multiplie par $u'$", taille=38)]),
        "tab_c": dict(type="formule", titre="Les quatre formules", x=200, y=120, w=880, lignes=[
            dict(f="$\\left(\\e^{u}\\right)'=u'\\,\\e^{u}$", taille=44),
            dict(f="$\\left(u^n\\right)'=nu'u^{n-1}$", m="$n\\geq1$", taille=44),
            dict(f="$\\left(\\sqrt u\\right)'=\\dfrac{u'}{2\\sqrt u}$", m="$u>0$", taille=44),
            dict(f="$\\left(\\dfrac1u\\right)'=-\\dfrac{u'}{u^2}$", m="$u\\neq0$", taille=44)]),
        "exc1": dict(type="formule", copie=True, titre="Trois calculs", x=110, y=92, w=1060, lignes=[
            dict(f="$f(x)=(3x+1)^5$ : $u(x)=3x+1$, $u'(x)=3$", taille=32),
            dict(f="$f'(x)=5\\times3\\times(3x+1)^4=15(3x+1)^4$", ind=True, hl=True, taille=32),
            dict(f="$g(x)=\\sqrt{x^2+1}$ : $u'(x)=2x$", taille=32),
            dict(f="$g'(x)=\\dfrac{2x}{2\\sqrt{x^2+1}}=\\dfrac{x}{\\sqrt{x^2+1}}$", ind=True, hl=True, taille=32),
            dict(f="$h(x)=\\e^{-x^2}$ : $u'(x)=-2x$", taille=32),
            dict(f="$h'(x)=-2x\\,\\e^{-x^2}$", ind=True, hl=True, taille=32)]),
        "exc2": dict(type="formule", copie=True, titre="$k(x)=\\e^{2x}(x-1)^3$", x=110, y=96, w=1060, lignes=[
            dict(f="un produit : $(uv)'=u'v+uv'$", txt=True),
            dict(f="$\\left(\\e^{2x}\\right)'=2\\,\\e^{2x}$", ind=True, taille=34),
            dict(f="$\\left((x-1)^3\\right)'=3(x-1)^2$", ind=True, taille=34),
            dict(f="$k'(x)=2\\,\\e^{2x}(x-1)^3+\\e^{2x}\\times3(x-1)^2$", taille=34),
            dict(f="$k'(x)=\\e^{2x}(x-1)^2\\big(2(x-1)+3\\big)$", ind=True, taille=34),
            dict(f="$k'(x)=\\e^{2x}(x-1)^2(2x+1)$", ind=True, cadre=True, taille=34)]),
        "meth": dict(type="liste", titre="Dériver une fonction compliquée", items=[
            "Repérer la dernière opération : somme, produit, quotient ou composée",
            "Dériver de l'extérieur vers l'intérieur",
            "Factoriser (souvent par l'exponentielle) pour le signe"], x=150, y=170, w=980),
        "piege_u": dict(type="formule", titre="Le piège : oublier $u'$", x=170, y=190, w=940, lignes=[
            dict(f="$\\left(\\e^{3x^2}\\right)'=\\e^{3x^2}$", ko=True, taille=44),
            dict(f="$\\left(\\e^{3x^2}\\right)'=6x\\,\\e^{3x^2}$", ok=True, cadre=True, taille=44)]),
        "pq": dict(type="formule", plus=True, titre="Pour comprendre : $(\\e^u)'=u'\\,\\e^u$", x=90, y=150, w=1100, lignes=[
            dict(f="$\\dfrac{\\e^{u(x+h)}-\\e^{u(x)}}{h}=\\dfrac{\\e^{u(x+h)}-\\e^{u(x)}}{u(x+h)-u(x)}\\times\\dfrac{u(x+h)-u(x)}{h}$", taille=30),
            dict(f="$\\dfrac{u(x+h)-u(x)}{h}\\to u'(x)$", ind=True, taille=30),
            dict(f="le premier facteur $\\to\\,\\e^{u(x)}$ (taux de $\\exp$ en $u(x)$)", ind=True, taille=30),
            dict(f="d'où $(\\e^u)'=u'\\,\\e^u$ ; la formule générale est admise", cadre=True, taille=30)]),
    }),

    # ================================================================ II. dérivée seconde
    dict(id="seconde", chap="La dérivée seconde", fond="carnet", humeur="calme",
         retenir="$f''$ est la dérivée de $f'$ : elle mesure comment la pente varie. Pour une position, $x''(t)$ est l'accélération.",
         beats=[
        "{def_s}Deuxième outil, très simple. Si f prime est elle-même dérivable, on peut la dériver à son tour. "
        "{def_s.1}On obtient la {!dérivée seconde}dérivée seconde de f, notée f seconde.",
        "{-def_s}{ex_s}Un exemple, qui tombe souvent : f de x égale x fois exponentielle de x. "
        "{ex_s.1}C'est un produit. f prime de x vaut un fois exponentielle de x, plus x fois exponentielle de x. "
        "{ex_s.2}On factorise : x plus un, fois exponentielle de x.",
        "{ex_s.3}On recommence sur f prime, qui est encore un produit. La dérivée de x plus un vaut un. "
        "Donc f seconde vaut exponentielle de x, plus x plus un, fois exponentielle de x. {ex_s.4}C'est-à-dire : x plus deux, fois exponentielle de x.",
        "{-ex_s}{sens}Mais à quoi sert f seconde ? {sens.1}En physique, tu la connais déjà. Si x de t est une position, "
        "x prime de t est la vitesse, et x seconde de t, l'accélération.",
        "{sens.2}En géométrie, f prime donne la pente de la tangente. Et f seconde dit comment cette pente varie. "
        "Si f seconde est positive, la pente augmente : la courbe tourne vers le haut. {sens.3}C'est ce qu'on appelle la {!courbure}courbure. "
        "Et c'est tout l'objet de la partie suivante.",
        "{-sens}",
    ], vis={
        "def_s": dict(type="def", terme="Dérivée seconde", cles=["seconde"],
                      t="Si $f'$ est elle-même dérivable, sa dérivée est la dérivée seconde de $f$, notée $f''$.",
                      etape="$f''=(f')'$", x=150, y=200, w=980),
        "ex_s": dict(type="formule", copie=True, titre="$f(x)=x\\,\\e^x$", x=150, y=140, w=980, lignes=[
            dict(f="$f'(x)=1\\times\\,\\e^x+x\\,\\e^x$", taille=38),
            dict(f="$f'(x)=(x+1)\\,\\e^x$", ind=True, taille=38),
            dict(f="$f''(x)=1\\times\\,\\e^x+(x+1)\\,\\e^x$", taille=38),
            dict(f="$f''(x)=(x+2)\\,\\e^x$", ind=True, cadre=True, taille=38)]),
        "sens": dict(type="formule", titre="Ce que mesure $f''$", x=150, y=170, w=980, lignes=[
            dict(f="position $x(t)$, vitesse $x'(t)$, accélération $x''(t)$", taille=36),
            dict(f="$f'$ : la pente ; $f''$ : comment la pente varie", taille=36),
            dict(f="$f''$ mesure la courbure", cadre=True, taille=36)]),
    }),

    # ================================================================ III. convexité
    dict(id="convexite", chap="Fonctions convexes, concaves", fond="ardoise", humeur="lumiere",
         retenir="Pour $f$ deux fois dérivable : $f$ convexe ⇔ $f''\\geq0$ ⇔ $f'$ croissante ⇔ courbe au-dessus de ses tangentes (et sous ses cordes). Concave : tout s'inverse.",
         beats=[
        "{tg1}Regarde la courbe de l'exponentielle. Elle tourne vers le haut, comme un bol. "
        "{tg1.corde}Prends deux points A et B sur la courbe, et relie-les par un segment : une {!corde}corde.",
        "Entre A et B, la courbe passe sous la corde. Et c'est vrai quels que soient les deux points choisis.",
        "C'est exactement la définition. Une fonction est {!convexe}convexe sur un intervalle, si sa courbe est en dessous de chacune de ses cordes.",
        "{tg1.tan}Maintenant, place une tangente. {tg1.go}Et fais-la glisser le long de la courbe. Regarde deux choses. "
        "D'abord, la courbe reste toujours au-dessus de la tangente. Ensuite, la pente, affichée en haut, ne fait qu'augmenter.",
        "{tg1.fixes}La courbe est au-dessus de toutes ses tangentes, et la pente f prime est croissante. Ce n'est pas un hasard.",
        "{-tg1}{carac}Voici le théorème central, admis. {carac.1}Pour une fonction deux fois dérivable sur un intervalle, ces quatre affirmations sont équivalentes. "
        "{carac.2}f est convexe. {carac.3}Sa courbe est au-dessus de chacune de ses tangentes. "
        "{carac.4}f prime est croissante. {carac.5}Et f seconde est positive.",
        "{carac.6}Le dernier point est le plus pratique : pour savoir si une fonction est convexe, on calcule f seconde, et on étudie son signe.",
        "{-carac}{tg2}Et l'inverse ? Regarde la racine carrée. {tg2.tan}La tangente glisse, {tg2.go}et cette fois, la courbe reste en dessous. "
        "La pente diminue. La courbe tourne vers le bas, comme une voûte.",
        "{tg2.z1}On dit que f est {!concave}concave : sa courbe est au-dessus de ses cordes, en dessous de ses tangentes. "
        "Et tout s'inverse : f prime décroissante, f seconde négative.",
        "{-tg2}{refs}Les fonctions de référence, à connaître. {refs.1}x au carré et l'exponentielle sont convexes sur R : "
        "leur dérivée seconde vaut deux, et exponentielle de x. Toutes deux positives.",
        "{refs.2}La racine carrée est concave sur zéro, plus l'infini : sa dérivée seconde est négative.",
        "{refs.3}Et x au cube change de camp : concave sur moins l'infini, zéro, puis convexe sur zéro, plus l'infini. On y revient tout de suite.",
        "{-refs}{g_em}Un piège classique : ne confonds pas convexe et croissante. {g_em.1}Voici exponentielle de moins x. "
        "Elle descend : elle est décroissante. {g_em.2}Mais elle tourne vers le haut : elle est convexe. "
        "Sa dérivée seconde, c'est exponentielle de moins x, toujours positive.",
        "Le sens de variation, c'est le signe de f prime. La convexité, c'est le signe de f seconde. Deux choses différentes.",
        "{-g_em}{lect}Et au bac, on te donne souvent un graphique. Mais lequel ? {lect.1}Si on te donne la courbe de f prime, "
        "f est convexe là où f prime est croissante. {lect.2}Si on te donne la courbe de f seconde, "
        "f est convexe là où f seconde est positive. {lect.3}Avant de répondre, lis bien le nom de la courbe !",
        "{-lect}{meth_cv}La méthode complète, en trois étapes. {meth_cv.1}Calcule f seconde, et factorise-la. "
        "{meth_cv.2}Étudie son signe : positive, f est convexe ; négative, f est concave. "
        "{meth_cv.3}Et les points d'inflexion : là où f seconde s'annule en changeant de signe.",
        "{-meth_cv}{bac_p}Un exemple tiré du bac de juin deux mille vingt-six, en Polynésie. Vrai ou faux : "
        "{bac_p.1}x fois exponentielle de x est convexe sur l'intervalle moins deux, plus l'infini ?",
        "{bac_p.2}On a déjà calculé sa dérivée seconde : x plus deux, fois exponentielle de x. "
        "{bac_p.3}L'exponentielle est strictement positive. Donc le signe est celui de x plus deux, positif dès que x dépasse moins deux. "
        "{bac_p.4}C'est vrai. Et la fonction est concave avant moins deux.",
        "{-bac_p}",
    ], vis={
        "tg1": dict(type="illu", nom="tangentes", f="exp", x=150, y=90, w=980, h=600, **{
            "rx": [-2.6, 2.3], "ry": [-0.8, 8.2], "corde": [-1.6, 1.8], "lcorde": [330, 70],
            "tcorde": "entre $A$ et $B$ : la courbe sous la corde", "de": -2.2, "a": 1.95, "dur": 7,
            "fixes": [-1.5, -0.5, 0.5, 1.4], "lfixes": [330, 70], "tfixes": "toujours au-dessus des tangentes"}),
        "carac": dict(type="liste", titre="$f$ deux fois dérivable sur $I$ : équivalences", items=[
            "Les quatre affirmations suivantes sont équivalentes (admis) :",
            "$f$ est **convexe** sur $I$",
            "sa courbe est **au-dessus** de chacune de ses tangentes",
            "$f'$ est **croissante** sur $I$",
            "$f''\\geq0$ sur $I$",
            "en pratique : on étudie le **signe** de $f''$"], marques=["·", "1", "2", "3", "4", "→"], x=150, y=110, w=980),
        "tg2": dict(type="illu", nom="tangentes", f="sqrt", x=150, y=110, w=980, h=560, **{
            "rx": [-0.4, 9.6], "ry": [-0.3, 3.6], "dom": [0, 9.6], "de": 0.35, "a": 9.0, "dur": 6,
            "zones": [[690, 360, "concave : la courbe **sous** ses tangentes", "gr"]]}),
        "refs": dict(type="formule", titre="Les fonctions de référence", x=150, y=150, w=980, lignes=[
            dict(f="$x^2$ et $\\e^x$ : convexes sur $\\R$", n="$f''(x)=2$ et $f''(x)=\\e^x$, positives", taille=38),
            dict(f="$\\sqrt{x}$ : concave sur $[0;+\\infty[$", n="$f''(x)=-\\dfrac1{4x\\sqrt x}<0$", taille=38),
            dict(f="$x^3$ : concave sur $]-\\infty;0]$, convexe sur $[0;+\\infty[$", taille=38)]),
        "g_em": dict(type="graphe", titre="$\\e^{-x}$ : décroissante **et** convexe", x=250, y=110, w=780, h=560,
                     ax=dict(x=[-1.5, 4.2], y=[0, 4.6], gx=[-1, 1, 2, 3, 4], gy=[1, 2, 3, 4], lx="$x$", ly="$y$"),
                     el=[dict(type="courbe", pts=EXPM, c="iv", ep=3.4, dur=2),
                         dict(type="texte", x=2.4, y=3.2, t="$f''(x)=\\e^{-x}>0$", c="sa")]),
        "lect": dict(type="liste", titre="Lire la convexité sur un graphique", items=[
            "Courbe de $f'$ : $f$ convexe là où $f'$ **croît**",
            "Courbe de $f''$ : $f$ convexe là où $f''$ est **positive**",
            "Lire d'abord le nom de la courbe !"], marques=["1", "2", "!"], x=150, y=170, w=980),
        "meth_cv": dict(type="liste", titre="Étudier la convexité", items=[
            "Calculer $f''$ et la factoriser",
            "Signe de $f''$ : $f''\\geq0$ convexe, $f''\\leq0$ concave",
            "Inflexion : $f''$ s'annule **en** **changeant** **de** **signe**"], x=150, y=170, w=980),
        "bac_p": dict(type="formule", titre="Vrai ou faux ? (bac, Polynésie, juin 2026)", x=130, y=150, w=1020, lignes=[
            dict(f="« $g(x)=x\\,\\e^x$ est convexe sur $[-2;+\\infty[$ »", taille=38),
            dict(f="$g''(x)=(x+2)\\,\\e^x$", taille=38),
            dict(f="$\\e^x>0$ : signe de $x+2$, positif sur $[-2;+\\infty[$", taille=34),
            dict(f="Vrai (et $g$ est concave sur $]-\\infty;-2]$)", ok=True, cadre=True, taille=36)]),
    }),

    # ================================================================ IV. point d'inflexion
    dict(id="inflexion", chap="Les points d'inflexion", fond="carnet", humeur="mystere",
         retenir="Point d'inflexion : la courbe traverse sa tangente ; $f''$ s'annule **en** **changeant** **de** **signe**. $f''(a)=0$ seul ne suffit pas (contre-exemple : $x^4$ en $0$).",
         beats=[
        "{tg3}Regarde maintenant x au cube. {tg3.tan}On fait glisser la tangente, {tg3.go}depuis la gauche.",
        "{tg3.z1}Au début, la courbe est sous ses tangentes : concave. {tg3.z2}Puis, d'un coup, elle passe au-dessus : convexe. "
        "{tg3.inf}Au point de bascule, l'origine, la tangente est l'axe des abscisses. Et la courbe la traverse !",
        "Ce point a un nom : un {!point d'inflexion}point d'inflexion. C'est un point où la courbe traverse sa tangente.",
        "{-tg3}{def_i}Et avec f seconde, c'est un point où f seconde s'annule {def_i.1}en changeant de signe. "
        "Pour x au cube, f seconde vaut six fois x : négative avant zéro, positive après. Il y a bien inflexion à l'origine.",
        "{-def_i}{g_x4}Mais attention au piège. {g_x4.1}Prends x puissance quatre. "
        "Sa dérivée seconde vaut douze fois x au carré. Elle s'annule en zéro.",
        "{g_x4.2}Point d'inflexion ? Non ! Douze fois x au carré est positif des deux côtés. Elle s'annule, mais ne change pas de signe. "
        "{g_x4.3}La courbe reste au-dessus de sa tangente en zéro. x puissance quatre est convexe sur R, sans inflexion.",
        "Retiens : f seconde nulle ne suffit pas. Il faut un changement de signe.",
        "{-g_x4}{ex_i}Un exemple complet : g de x égale x au cube, moins trois fois x au carré, plus deux. "
        "{ex_i.1}g prime vaut trois fois x au carré, moins six fois x. {ex_i.2}g seconde vaut six fois x, moins six.",
        "{ex_i.3}Six fois x moins six est négatif avant un, positif après. Donc g est concave sur moins l'infini, un, et convexe sur un, plus l'infini. "
        "{ex_i.4}g seconde s'annule en changeant de signe en un. {ex_i.5}Le point d'inflexion a pour coordonnées un, et g de un, "
        "c'est-à-dire un moins trois plus deux : zéro.",
        "{-ex_i}{asie}Et un vrai ou faux du bac, en Asie, juin deux mille vingt-six. {asie.1}La fonction moins un demi x plus trois, "
        "le tout puissance cinq, est-elle convexe sur R ?",
        "{asie.2}On dérive deux fois, avec la formule de u puissance n. u prime vaut moins un demi. "
        "La dérivée seconde vaut cinq fois, moins un demi x plus trois, au cube.",
        "{asie.3}Or moins un demi x plus trois devient négatif dès que x dépasse six. Alors f seconde est négative. "
        "{asie.4}La fonction n'est pas convexe sur R : l'affirmation est fausse.",
        "{-asie}",
    ], vis={
        "tg3": dict(type="illu", nom="tangentes", f="x3", x=150, y=90, w=980, h=600, **{
            "rx": [-1.75, 1.75], "ry": [-4.6, 4.6], "de": -1.45, "a": 1.45, "dur": 7, "inf": True, "linf": [660, 350],
            "zones": [[260, 120, "concave", "gr"], [760, 120, "convexe", "pc"]]}),
        "def_i": dict(type="def", terme="Point d'inflexion", cles=["traverse", "signe"],
                      t="Un point où la courbe **traverse** sa tangente. Pour $f$ deux fois dérivable : $f''$ s'y annule en changeant de signe.",
                      etape="$x^3$ : $f''(x)=6x$, négatif puis positif : inflexion en $O$.", x=150, y=180, w=980),
        "g_x4": dict(type="graphe", titre="$x^4$ : $f''(0)=0$ mais pas d'inflexion", x=250, y=110, w=780, h=560,
                     ax=dict(x=[-1.5, 1.5], y=[-0.3, 3.8], gx=[-1, 1], gy=[1, 2, 3], lx="$x$", ly="$y$"),
                     el=[dict(type="courbe", pts=X4, c="iv", ep=3.4, dur=2),
                         dict(type="texte", x=0.62, y=1.25, t="$f''(x)=12x^2\\geq0$", c="sa"),
                         dict(type="droite", pts=[[-1.5, 0], [1.5, 0]], c="te", ep=3.2, lbl="tangente en $0$", lp=[1.0, 0.45])]),
        "ex_i": dict(type="formule", copie=True, titre="$g(x)=x^3-3x^2+2$", x=130, y=110, w=1020, lignes=[
            dict(f="$g'(x)=3x^2-6x$", taille=36),
            dict(f="$g''(x)=6x-6$", taille=36),
            dict(f="concave sur $]-\\infty;1]$, convexe sur $[1;+\\infty[$", taille=34),
            dict(f="$g''$ s'annule en changeant de signe en $1$", ind=True, taille=34),
            dict(f="point d'inflexion $(1;g(1))=(1;0)$", cadre=True, taille=36)]),
        "asie": dict(type="formule", titre="Vrai ou faux ? (bac, Asie, juin 2026)", x=130, y=150, w=1020, lignes=[
            dict(f="« $f(x)=\\left(-\\frac12x+3\\right)^5$ est convexe sur $\\R$ »", taille=38),
            dict(f="$f''(x)=5\\left(-\\frac12x+3\\right)^3$", taille=38),
            dict(f="$-\\frac12x+3<0$ pour $x>6$ : $f''<0$", taille=36),
            dict(f="Faux", ko=True, cadre=True, taille=38)]),
    }),

    # ================================================================ V. démonstration et inégalités
    dict(id="demo", chap="La démonstration exigible, les inégalités", fond="ardoise", humeur="tension",
         retenir="Si $f''\\geq0$, la courbe est au-dessus de ses tangentes : on étudie $g=f-\\text{tangente}$, minimum $0$ en $a$. Inégalités : $\\e^x\\geq x+1$ et $\\sqrt x\\leq\\frac{x+1}2$.",
         beats=[
        "{tag_bo}{dem}Place à la démonstration exigible du chapitre. Si f seconde est positive, la courbe est au-dessus de ses tangentes.",
        "{dem.1}Soit f deux fois dérivable sur I, avec f seconde positive, et soit un réel a de I. "
        "La tangente au point d'abscisse a a pour équation : y égale f prime de a, fois x moins a, plus f de a.",
        "{dem.2}L'idée : on étudie l'écart entre la courbe et la tangente. On pose g de x égale f de x, moins l'expression de la tangente.",
        "{dem.3}On dérive : f de a et f prime de a sont des constantes. Il reste g prime de x égale f prime de x, moins f prime de a.",
        "{dem.4}Or f seconde est positive, donc f prime est croissante. Si x est plus petit que a, f prime de x est plus petit que f prime de a : "
        "g prime est négative. {dem.5}Si x est plus grand que a, g prime est positive.",
        "{dem.6}Donc g décroît, puis croît : elle a un minimum au point a. Et ce minimum vaut g de a : f de a, moins f de a. Zéro.",
        "{dem.7}Conclusion : g est positive partout. La courbe est au-dessus de la tangente en a. Et ceci, pour chaque point a de I.",
        "Retiens surtout la structure : étudier la différence, la dériver, trouver son minimum. Elle sert pour toutes les inégalités.",
        "{-dem}{-tag_bo}{g_exp}Et justement, la convexité donne des inégalités presque gratuitement. {g_exp.1}L'exponentielle est convexe. "
        "{g_exp.2}Sa tangente au point d'abscisse zéro a pour équation y égale x plus un : exponentielle de zéro vaut un, et la pente aussi.",
        "{g_exp.3}La courbe est au-dessus de cette tangente. Donc, pour tout réel x, exponentielle de x est supérieure ou égale à x plus un. "
        "Une inégalité célèbre, à connaître.",
        "{-g_exp}{g_rac}Même idée avec la racine carrée, qui est concave. {g_rac.1}Elle est sous sa tangente au point d'abscisse un, "
        "{g_rac.2}d'équation y égale un demi x, plus un demi.",
        "{g_rac.3}Donc racine de x est inférieure ou égale à x plus un, sur deux, pour tout x positif. "
        "Égalité pour x égale un. {g_rac.4}Et pour x égale neuf : racine de neuf vaut trois, et neuf plus un sur deux vaut cinq. Trois est bien plus petit que cinq.",
        "{-g_rac}{meth_in}La méthode, quand on te demande de démontrer qu'une fonction est au-dessus d'une autre. "
        "{meth_in.1}Si l'autre est une tangente : par convexité. {meth_in.2}Sinon, on étudie la différence, "
        "on cherche son minimum avec la dérivée, et on montre qu'il est positif.",
        "{-meth_in}{euler}Un joli usage de exponentielle de x, supérieur ou égal à x plus un. Prends x égale un sur n, pour un entier n non nul. "
        "{euler.1}On obtient : un plus un sur n, inférieur ou égal à exponentielle de un sur n.",
        "{euler.2}Les deux membres sont positifs, et la fonction puissance n est croissante sur les positifs. On élève à la puissance n. "
        "{euler.3}Un plus un sur n, puissance n, est inférieur ou égal à exponentielle de un, ce fameux nombre e, environ deux virgule sept un huit.",
        "{-euler}",
    ], vis={
        "tag_bo": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=650, y=40, w=560),
        "dem": dict(type="formule", copie=True, titre="Si $f''\\geq0$, la courbe est au-dessus de ses tangentes", x=80, y=92, w=1120, lignes=[
            dict(lab="Soit", f="$a\\in I$ ; tangente : $y=f'(a)(x-a)+f(a)$", taille=29),
            dict(f="$g(x)=f(x)-\\left[f'(a)(x-a)+f(a)\\right]$", taille=29),
            dict(f="$g'(x)=f'(x)-f'(a)$", ind=True, taille=29),
            dict(f="$f''\\geq0$ : $f'$ croissante ; $x\\leq a\\Rightarrow g'(x)\\leq0$", ind=True, taille=29),
            dict(f="$x\\geq a\\Rightarrow g'(x)\\geq0$", ind=True, taille=29),
            dict(f="minimum en $a$ : $g(a)=f(a)-f(a)=0$", ind=True, hl=True, taille=29),
            dict(f="$g\\geq0$ : la courbe est au-dessus de la tangente en $a$", cadre=True, taille=29)]),
        "g_exp": dict(type="graphe", titre="$\\e^x\\geq x+1$", x=250, y=110, w=780, h=560,
                      ax=dict(x=[-3, 2.2], y=[-2.2, 7.6], gx=[-2, -1, 1, 2], gy=[2, 4, 6], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=EXP, c="iv", ep=3.4, dur=1.8),
                          dict(type="droite", pts=[[-3, -2], [2.2, 3.2]], c="sa", ep=3, lbl="$y=x+1$", lp=[1.2, 1.2]),
                          dict(type="texte", x=-1.4, y=5.6, t="courbe au-dessus", c="te")]),
        "g_rac": dict(type="graphe", titre="$\\sqrt x\\leq\\dfrac{x+1}2$", x=250, y=110, w=780, h=560,
                      ax=dict(x=[0, 9.8], y=[0, 5.6], gx=[1, 3, 5, 7, 9], gy=[1, 2, 3, 4, 5], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=RAC, c="iv", ep=3.4, dur=1.8),
                          dict(type="droite", pts=[[0, 0.5], [9.8, 5.15]], c="sa", ep=3, lbl="$y=\\frac12x+\\frac12$", lp=[4.1, 3.9]),
                          dict(type="point", x=1, y=1, c="te", lbl="égalité en $1$", lp=[2.2, 0.7]),
                          dict(type="points", pts=[[9, 3], [9, 5]], c="ca", lbl="$3\\leq5$", lp=[8.0, 4.0])]),
        "meth_in": dict(type="liste", titre="Démontrer $f(x)\\geq g(x)$", items=[
            "Si $g$ est une tangente de $f$ : par convexité",
            "Sinon : étudier $h=f-g$, son minimum avec $h'$, montrer qu'il est positif"], x=150, y=200, w=980),
        "euler": dict(type="formule", titre="$\\left(1+\\dfrac1n\\right)^n\\leq\\,\\e$", x=150, y=170, w=980, lignes=[
            dict(f="$x=\\dfrac1n$ : $1+\\dfrac1n\\leq\\,\\e^{\\dfrac1n}$", taille=40),
            dict(f="deux membres positifs, $t\\mapsto t^n$ croissante sur $[0;+\\infty[$", txt=True),
            dict(f="$\\left(1+\\dfrac1n\\right)^n\\leq\\left(\\e^{\\dfrac1n}\\right)^n=\\e\\approx2{,}718$", cadre=True, taille=40)]),
    }),

    # ================================================================ VI. continuité
    dict(id="continuite", chap="La continuité", fond="carnet", humeur="calme",
         retenir="$f$ continue en $a$ : $\\lim_{x\\to a}f(x)=f(a)$. Dérivable ⇒ continue (réciproque fausse : $|x|$ en $0$). $u_n\\to\\ell$ et $f$ continue en $\\ell$ ⇒ $f(u_n)\\to f(\\ell)$.",
         beats=[
        "{def_ct}Changeons de sujet. Une fonction est {!continue}continue au point a si la limite de f de x, quand x tend vers a, vaut f de a. "
        "{def_ct.1}Graphiquement : la courbe se trace sans lever le crayon.",
        "{-def_ct}{g_E}À quoi ressemble une fonction qui n'est pas continue ? {g_E.1}{g_E.4}{g_E.5}{g_E.6}{g_E.7}Voici la partie entière : "
        "E de x, c'est le plus grand entier inférieur ou égal à x. {g_E.2}Pour x entre zéro et un, exclu, elle vaut zéro. "
        "Et en un, elle vaut un. {g_E.3}La courbe saute, en chaque entier. La partie entière n'est pas continue au point un.",
        "{-g_E}{prop}Bonne nouvelle : presque toutes les fonctions que tu rencontres sont continues. {prop.1}Les polynômes, la racine, "
        "l'exponentielle, cosinus, sinus, les quotients là où ils sont définis. {prop.2}Et leurs sommes, produits et composées aussi.",
        "{prop.3}Le programme est clair : justifier la continuité n'est pas un objectif. Au bac, une phrase suffit : "
        "« f est continue, comme polynôme », ou « comme produit de fonctions continues ».",
        "{-prop}{thm_d}Un lien important avec la dérivation. {thm_d.1}Toute fonction dérivable sur un intervalle est continue sur cet intervalle.",
        "{thm_d.2}Mais la réciproque est fausse. {-thm_d}{g_abs}Le contre-exemple : la valeur absolue de x. {g_abs.1}{g_abs.2}Sa courbe est un V. "
        "Elle est continue en zéro, on la trace sans lever le crayon.",
        "{g_abs.3}Mais en zéro, il y a un coin. À gauche, la pente vaut moins un ; à droite, un. Deux demi-tangentes différentes : "
        "la valeur absolue n'est pas dérivable en zéro.",
        "{-g_abs}{suite}Dernier résultat, qui fait le lien avec les suites. {suite.1}Si u indice n converge vers L, "
        "et si f est continue au point L, alors f de u indice n converge vers f de L.",
        "{suite.2}Un exemple : u indice n tend vers deux, et f de x vaut x au carré plus un. f est continue, donc f de u indice n tend vers f de deux, "
        "c'est-à-dire cinq.",
        "{suite.3}Et la conséquence la plus utile : si u indice n plus un égale f de u indice n, et si la suite converge vers L, "
        "avec f continue, alors f de L égale L. La limite est un point fixe de f. C'est comme ça qu'on la calcule.",
        "{-suite}{conv}Enfin, une convention. {conv.1}Dans un tableau de variations, une flèche signifie que la fonction est continue "
        "et strictement monotone sur l'intervalle. Tu vas voir pourquoi c'est si important.",
        "{-conv}",
    ], vis={
        "def_ct": dict(type="def", terme="Continuité en $a$", cles=["continue", "crayon"],
                       t="$f$ est continue en $a$ si $\\lim_{x\\to a}f(x)=f(a)$. Elle est continue sur un intervalle si elle l'est en chaque point.",
                       etape="Graphiquement : la courbe se trace sans lever le crayon.", x=150, y=180, w=980),
        "g_E": dict(type="graphe", titre="La partie entière $E$ : elle saute", x=250, y=110, w=780, h=560,
                    ax=dict(x=[-2.3, 3.3], y=[-2.6, 3.2], gx=[-2, -1, 1, 2, 3], gy=[-2, -1, 1, 2], lx="$x$", ly="$y$"),
                    el=[dict(type="points", pts=[[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2]], c="sa", pas=.12),
                        dict(type="droite", pts=[[0, 0], [0.97, 0]], c="sa", ep=4, lbl="$E(x)=0$ sur $[0;1[$", lp=[0.95, -0.7]),
                        dict(type="texte", x=1.6, y=2.75, t="en $1$ : un saut", c="ca"),
                        dict(type="droite", pts=[[-2, -2], [-1.03, -2]], c="iv", ep=3.6),
                        dict(type="droite", pts=[[-1, -1], [-0.03, -1]], c="iv", ep=3.6),
                        dict(type="droite", pts=[[1, 1], [1.97, 1]], c="iv", ep=3.6),
                        dict(type="droite", pts=[[2, 2], [2.97, 2]], c="iv", ep=3.6)]),
        "prop": dict(type="formule", titre="Les fonctions continues", x=150, y=170, w=980, lignes=[
            dict(f="polynômes, racine carrée, $\\exp$, $\\cos$, $\\sin$, quotients (là où ils sont définis)", taille=34),
            dict(f="leurs sommes, produits, composées", taille=34),
            dict(f="justifier la continuité : une phrase suffit", txt=True)]),
        "thm_d": dict(type="formule", titre="Dérivable et continue", x=170, y=200, w=940, lignes=[
            dict(f="$f$ dérivable sur $I$ $\\Rightarrow$ $f$ continue sur $I$", cadre=True, taille=42),
            dict(f="la réciproque est fausse", ko=True, txt=True)]),
        "g_abs": dict(type="graphe", titre="$|x|$ : continue, pas dérivable en $0$", x=250, y=110, w=780, h=560,
                      ax=dict(x=[-3.2, 3.2], y=[-0.4, 3.4], gx=[-2, -1, 1, 2], gy=[1, 2, 3], lx="$x$", ly="$y$"),
                      el=[dict(type="droite", pts=[[-3.2, 3.2], [0, 0]], c="iv", ep=3.6, lbl="pente $-1$", lp=[-2.0, 1.2]),
                          dict(type="droite", pts=[[0, 0], [3.2, 3.2]], c="iv", ep=3.6, lbl="pente $1$", lp=[2.0, 1.2]),
                          dict(type="point", x=0, y=0, c="ca", lbl="un coin", lp=[0, 0.75])]),
        "suite": dict(type="formule", titre="Image d'une suite convergente", x=130, y=150, w=1020, lignes=[
            dict(f="$u_n\\to\\ell$ et $f$ continue en $\\ell$ $\\Rightarrow$ $f(u_n)\\to f(\\ell)$", cadre=True, taille=38),
            dict(f="$u_n\\to2$, $f(x)=x^2+1$ : $f(u_n)\\to f(2)=5$", taille=36),
            dict(f="$u_{n+1}=f(u_n)$, $u_n\\to\\ell$, $f$ continue $\\Rightarrow$ $f(\\ell)=\\ell$", n="la limite est un point fixe", taille=36)]),
        "conv": dict(type="note", titre="Convention", cles=["flèche", "monotone"],
                     t="Dans un tableau de variations, une flèche indique que la fonction est continue et strictement monotone sur l'intervalle.",
                     x=170, y=220, w=940),
    }),

    # ================================================================ VII. théorème des valeurs intermédiaires
    dict(id="tvi", chap="Le théorème des valeurs intermédiaires", fond="ardoise", humeur="tension",
         retenir="TVI : $f$ continue sur $[a;b]$, $k$ entre $f(a)$ et $f(b)$ ⇒ $f(x)=k$ a **au** **moins** **une** solution. Si de plus $f$ est strictement monotone : solution **unique**.",
         beats=[
        "{thm_tvi}Nous voilà prêts pour le théorème phare du chapitre : le {!théorème des valeurs intermédiaires}théorème des valeurs intermédiaires. "
        "On l'abrège souvent T V I.",
        "{thm_tvi.1}Si f est continue sur l'intervalle fermé a, b, {thm_tvi.2}alors, pour tout réel k compris entre f de a et f de b, "
        "{thm_tvi.3}l'équation f de x égale k admet au moins une solution dans cet intervalle.",
        "C'est l'idée de l'ouverture, rendue rigoureuse : une fonction continue ne peut pas sauter par-dessus une valeur.",
        "{-thm_tvi}{g_saut}D'ailleurs, que se passe-t-il sans la continuité ? {g_saut.1}Voici une fonction qui va de zéro à deux virgule cinq. "
        "{g_saut.2}{g_saut.3}Mais elle fait un saut, au point un. {g_saut.4}La valeur un virgule deux, comprise entre les deux, n'est jamais atteinte. "
        "Sans continuité, le théorème ne marche plus.",
        "{-g_saut}{g_trois}Et attention : « au moins une », ce n'est pas « une seule ». {g_trois.1}Voici x au cube, moins trois fois x, plus un, "
        "entre moins deux et deux. {g_trois.2}Elle vaut moins un en moins deux, et trois en deux. Zéro est entre les deux.",
        "{g_trois.3}Le théorème garantit une solution de f de x égale zéro. Et il y en a trois ! "
        "La courbe monte, redescend, puis remonte. Elle coupe l'axe trois fois.",
        "{-g_trois}{coro}Pour avoir une seule solution, il faut une hypothèse de plus. C'est le corollaire. "
        "{coro.1}Si f est continue, {coro.2}et strictement monotone sur a, b, {coro.3}alors, pour tout k compris entre f de a et f de b, "
        "l'équation f de x égale k admet une unique solution.",
        "{coro.4}Logique : une fonction strictement croissante ne repasse jamais par la même valeur. "
        "{coro.5}Et ça marche aussi sur un intervalle ouvert, ou infini, en remplaçant f de a et f de b par les limites aux bornes.",
        "{-coro}{red}Revenons à notre équation de l'ouverture, et rédigeons comme sur une copie. "
        "{red.1}Soit f de x égale x au cube, plus x, moins un. {red.2}f est continue sur zéro, un, car c'est un polynôme.",
        "{red.3}f prime de x vaut trois fois x au carré, plus un, qui est strictement positif. Donc f est strictement croissante sur zéro, un.",
        "{red.4}f de zéro vaut moins un, négatif, et f de un vaut un, positif : zéro est compris entre f de zéro et f de un.",
        "{red.5}D'après le corollaire du théorème des valeurs intermédiaires, l'équation f de x égale zéro admet une unique solution, "
        "qu'on appelle alpha, dans zéro, un.",
        "{red.6}Et alpha vaut environ zéro virgule six huit deux trois. Mais comment le sait-on ? C'est l'objet de la partie suivante.",
        "{-red}{piege_h}{piege_h.1}Au bac, chaque hypothèse rapporte des points. Continue. {piege_h.2}Strictement monotone. "
        "{piege_h.3}k compris entre les images, ou entre les limites. {piege_h.4}Puis la conclusion, avec le nom du théorème. N'en oublie aucune.",
        "{-piege_h}",
    ], vis={
        "thm_tvi": dict(type="formule", titre="Théorème des valeurs intermédiaires (TVI)", x=130, y=150, w=1020, lignes=[
            dict(f="Si $f$ est **continue** sur $[a;b]$,", taille=38),
            dict(f="pour tout réel $k$ compris entre $f(a)$ et $f(b)$,", taille=38),
            dict(f="l'équation $f(x)=k$ admet **au** **moins** **une** solution dans $[a;b]$.", cadre=True, taille=36)]),
        "g_saut": dict(type="graphe", titre="Sans continuité, $k=1{,}2$ n'est pas atteint", x=250, y=110, w=780, h=560,
                       ax=dict(x=[0, 2.2], y=[0, 2.8], gx=[0.5, 1, 1.5, 2], gy=[1, 1.2, 2, 2.5], lx="$x$", ly="$y$"),
                       el=[dict(type="courbe", pts=SAUT_G, c="iv", ep=3.6),
                           dict(type="courbe", pts=SAUT_D, c="iv", ep=3.6),
                           dict(type="point", x=1, y=2, c="iv", lbl="un saut", lp=[0.62, 2.3]),
                           dict(type="droite", pts=[[0, 1.2], [2.2, 1.2]], c="ca", ep=2.8, tir=True, lbl="$y=1{,}2$ : jamais atteint", lp=[1.55, 0.85])]),
        "g_trois": dict(type="graphe", titre="$x^3-3x+1$ : trois solutions de $f(x)=0$", x=250, y=110, w=780, h=560,
                        ax=dict(x=[-2.1, 2.1], y=[-1.3, 3.3], gx=[-2, -1, 1, 2], gy=[-1, 1, 2, 3], lx="$x$", ly="$y$"),
                        el=[dict(type="courbe", pts=TVI3, c="iv", ep=3.4, dur=2.2),
                            dict(type="points", pts=[[-2, -1], [2, 3]], c="sa", lbl="$f(-2)=-1$, $f(2)=3$", lp=[0.7, 2.85]),
                            dict(type="points", pts=[[-1.8794, 0], [0.3473, 0], [1.5321, 0]], c="ca", pas=.35)]),
        "coro": dict(type="formule", titre="Corollaire : le cas strictement monotone", x=110, y=110, w=1060, lignes=[
            dict(f="Si $f$ est **continue**", taille=36),
            dict(f="et **strictement** **monotone** sur $[a;b]$,", taille=36),
            dict(f="pour tout $k$ entre $f(a)$ et $f(b)$, $f(x)=k$ a une **unique** solution.", cadre=True, taille=34),
            dict(f="strictement croissante : jamais deux fois la même valeur", txt=True),
            dict(f="intervalle ouvert ou infini : on utilise les limites aux bornes", txt=True)]),
        "red": dict(type="formule", copie=True, titre="Rédaction type : $x^3+x-1=0$ sur $[0;1]$", x=80, y=92, w=1120, lignes=[
            dict(f="Soit $f(x)=x^3+x-1$.", taille=30),
            dict(f="$f$ est continue sur $[0;1]$ (polynôme).", ind=True, taille=30),
            dict(f="$f'(x)=3x^2+1>0$ : $f$ est strictement croissante sur $[0;1]$.", ind=True, taille=30),
            dict(f="$f(0)=-1<0$ et $f(1)=1>0$ : $0$ est compris entre $f(0)$ et $f(1)$.", ind=True, taille=30),
            dict(f="D'après le corollaire du TVI, $f(x)=0$ a une unique solution $\\alpha\\in[0;1]$.", cadre=True, taille=30),
            dict(f="$\\alpha\\approx0{,}6823$", ind=True, taille=30)]),
        "piege_h": dict(type="liste", titre="Rédaction TVI : chaque hypothèse est un point", items=[
            "$f$ est **continue** sur $I$", "$f$ est **strictement** monotone sur $I$",
            "$k$ est compris entre les images (ou les limites)", "Conclusion : « d'après le corollaire du TVI… »"],
            marques=["✓", "✓", "✓", "✓"], x=150, y=150, w=980),
    }),

    # ================================================================ VIII. dichotomie et Newton
    dict(id="dicho", chap="Encadrer la solution : dichotomie et Newton", fond="carnet", humeur="calme",
         retenir="Dichotomie : on coupe l'intervalle en deux et on garde la moitié où le signe change ; après $n$ étapes, la largeur est $\\frac{b-a}{2^n}$. Newton : $x_{n+1}=x_n-\\frac{f(x_n)}{f'(x_n)}$.",
         beats=[
        "{q_d}Le théorème dit qu'alpha existe. Il ne dit pas combien il vaut. Pour l'encadrer, on va le piéger.",
        "{-q_d}{dic}C'est la {!dichotomie}dichotomie. {dic.1}On part de zéro, un : f de zéro est négatif, f de un positif. Alpha est dedans. "
        "{dic.2}On prend le milieu, zéro virgule cinq. f de zéro virgule cinq est négatif : le changement de signe est à droite. "
        "On garde zéro virgule cinq, un.",
        "{dic.3}Nouveau milieu : zéro virgule sept cinq. f est positif : on garde la moitié gauche. "
        "{dic.4}Puis zéro virgule six deux cinq : négatif, on garde la droite.",
        "{dic.5}Puis zéro virgule six huit sept cinq : positif. {dic.6}Puis zéro virgule six cinq six deux cinq : négatif. "
        "À chaque étape, la largeur est divisée par deux.",
        "{-dic}{algo}Voici l'algorithme. {algo.1}On part de a, b, avec f de a et f de b de signes contraires. "
        "{algo.2}On calcule le milieu m. Si f de a et f de m sont de signes contraires, la solution est à gauche : b prend la valeur m. "
        "Sinon, a prend la valeur m. {algo.3}Et on recommence, tant que b moins a dépasse la précision voulue.",
        "{-algo}{ampl}Combien d'étapes ? {ampl.1}Après n étapes, la largeur vaut b moins a, sur deux puissance n. "
        "{ampl.2}Dix étapes divisent la largeur par mille vingt-quatre : à peu près un millième.",
        "{-ampl}{py_d}En Python, c'est un algorithme du programme. {py_d.l7}La ligne clé teste si f de a fois f de m est négatif ou nul : "
        "c'est la façon de dire « signes contraires ». {py_d.s}Le résultat : alpha est entre zéro virgule six huit un, et zéro virgule six huit trois. "
        "Il a fallu dix étapes.",
        "{-py_d}{g_nw}Il existe une méthode bien plus rapide, citée aussi par le programme : la méthode de {!Newton}Newton. "
        "{g_nw.1}L'idée : remplacer la courbe par sa tangente. {g_nw.2}On part de x égale un. On trace la tangente, "
        "{g_nw.3}et on regarde où elle coupe l'axe des abscisses : en zéro virgule sept cinq.",
        "{g_nw.4}On recommence depuis zéro virgule sept cinq. {g_nw.5}La nouvelle tangente coupe l'axe en zéro virgule six huit six. "
        "Déjà tout près d'alpha.",
        "{-g_nw}{py_n}{py_n.l3}La formule : x indice n plus un égale x indice n, moins f de x indice n, sur f prime de x indice n. "
        "{py_n.s}En cinq étapes seulement, on obtient une quinzaine de chiffres exacts. La dichotomie, en dix étapes, en donnait trois.",
        "{-py_n}{comp}Alors pourquoi garder la dichotomie ? {comp.1}Parce que Newton peut échouer : si la dérivée s'annule, ou si l'on part trop loin. "
        "{comp.2}La dichotomie, elle, marche toujours, dès que la fonction est continue avec des signes contraires aux bornes.",
        "{-comp}{plus_d}Et pour aller plus loin, ce n'est pas exigible : la dichotomie démontre le théorème des valeurs intermédiaires. "
        "Les bornes a et b forment deux suites, l'une croissante, l'autre décroissante, dont l'écart tend vers zéro. "
        "Elles convergent vers un même réel c. Et par continuité, f de c égale k.",
        "{-plus_d}",
    ], vis={
        "q_d": dict(type="question", t="$\\alpha$ existe. Mais combien vaut-il ?"),
        "dic": dict(type="illu", nom="dicho", x=80, y=96, w=1120, h=600, n=6),
        "algo": dict(type="liste", titre="La dichotomie", items=[
            "Départ : $[a;b]$ avec $f(a)$ et $f(b)$ de signes contraires",
            "$m=\\frac{a+b}2$ ; si $f(a)$ et $f(m)$ de signes contraires, $b\\leftarrow m$, sinon $a\\leftarrow m$",
            "On recommence tant que $b-a$ dépasse la précision"], x=130, y=170, w=1020),
        "ampl": dict(type="formule", titre="La largeur", x=170, y=200, w=940, lignes=[
            dict(f="après $n$ étapes : $\\dfrac{b-a}{2^n}$", cadre=True, taille=46),
            dict(f="$2^{10}=1024$ : dix étapes, environ $10^{-3}$", taille=40)]),
        "py_d": dict(type="code", titre="Python · la dichotomie", x=190, y=86, w=900, taille=25, lignes=[
            "def f(x):", "    return x**3 + x - 1", "", "def dichotomie(a, b, e):", "    while b - a > e:",
            "        m = (a + b) / 2", "        if f(a) * f(m) <= 0:", "            b = m", "        else:", "            a = m",
            "    return a, b", "", "print(dichotomie(0, 1, 0.001))"],
            sortie="(0.681640625, 0.6826171875)"),
        "g_nw": dict(type="graphe", titre="Newton : suivre la tangente", x=250, y=110, w=780, h=560,
                     ax=dict(x=[0.4, 1.12], y=[-0.6, 1.5], gx=[0.5, 0.75, 1], gy=[-0.5, 0.5, 1], lx="$x$", ly="$y$"),
                     el=[dict(type="courbe", pts=NEWT, c="iv", ep=3.4),
                         dict(type="point", x=1, y=1, c="sa", lbl="$x_0=1$", lp=[1.0, 1.32]),
                         dict(type="droite", pts=[[0.6, -0.6], [1.1, 1.4]], c="sa", ep=2.8, lbl="$x_1=0{,}75$", lp=[0.9, -0.3]),
                         dict(type="point", x=0.75, y=0.1719, c="te", proj=True),
                         dict(type="droite", pts=[[0.64, -0.1237], [0.85, 0.4407]], c="te", ep=2.8, lbl="$x_2\\approx0{,}686$", lp=[0.6, 0.25])]),
        "py_n": dict(type="code", titre="Python · la méthode de Newton", x=190, y=110, w=900, taille=27, lignes=[
            "x = 1.0", "for k in range(5):", "    x = x - (x**3 + x - 1) / (3 * x**2 + 1)", "    print(k + 1, x)"],
            sortie="1 0.75\n2 0.686046511627907\n3 0.6823395825973142\n4 0.6823278039465127\n5 0.6823278038280194"),
        "comp": dict(type="formule", titre="Newton ou dichotomie ?", x=150, y=200, w=980, lignes=[
            dict(f="Newton : très rapide, mais peut échouer ($f'$ nulle, départ trop loin)", taille=34),
            dict(f="dichotomie : marche toujours ($f$ continue, signes contraires)", ok=True, taille=34)]),
        "plus_d": dict(type="note", titre="Pour aller plus loin", cles=["suites", "continuité"],
                       t="Les bornes $(a_n)$ croissante et $(b_n)$ décroissante, d'écart $\\frac{b-a}{2^n}\\to0$, convergent vers un même $c$ ; par continuité, $f(c)=k$.",
                       x=170, y=200, w=940),
    }),

    # ================================================================ IX. les pièges
    dict(id="pieges", chap="Les pièges classiques", fond="craie", humeur="tension",
         retenir="Le $u'$ des composées ; convexe n'est pas croissante ; le bon graphique ; les hypothèses du TVI ; un encadrement d'amplitude $0{,}01$ aux bornes vérifiées.",
         beats=[
        "{pieges}Faisons le tour des pièges. {pieges.1}Un : oublier le u prime. La dérivée d'une composée contient toujours la dérivée de l'intérieur.",
        "{pieges.2}Deux : confondre convexe et croissante. Exponentielle de moins x est convexe, et pourtant décroissante.",
        "{pieges.3}Trois : lire la convexité sur le mauvais graphique. Sur la courbe de f prime, on regarde si elle croît. "
        "Sur la courbe de f seconde, on regarde son signe.",
        "{pieges.4}Quatre : le théorème sans ses hypothèses. Continue, strictement monotone, k entre les images. Chaque mot compte.",
        "{pieges.5}Et cinq : l'encadrement mal donné. Une valeur approchée à dix puissance moins deux près, c'est un encadrement de largeur un centième, "
        "par exemple entre zéro virgule trois quatre et zéro virgule trois cinq. Et on vérifie les signes aux deux bornes.",
        "{-pieges}",
    ], vis={
        "pieges": dict(type="liste", titre="Les pièges classiques", items=[
            "Oublier $u'$ : $\\left(\\e^{3x^2}\\right)'=6x\\,\\e^{3x^2}$", "Convexe n'est pas croissante : $\\e^{-x}$",
            "Le bon graphique : $f'$ croissante ou $f''$ positive", "TVI : continue, **strictement** monotone, $k$ entre les images",
            "Encadrement d'amplitude $0{,}01$, signes vérifiés aux bornes"],
            marques=["!", "!", "!", "!", "!"], x=130, y=110, w=1020),
    }),

    # ================================================================ X. exercice 1
    dict(id="exo1", chap="Exercice 1 · unique solution", fond="ardoise", humeur="tension", beats=[
        "{ex1}Place à l'entraînement. Premier exercice. Soit f de x égale x au cube, moins trois fois x, plus un. "
        "Un : étudier les variations de f sur l'intervalle moins un, un. "
        "Deux : montrer que l'équation f de x égale zéro a une unique solution alpha, dans zéro, un. "
        "Trois : donner un encadrement d'alpha de largeur un centième.",
        "{-ex1}{pa1}À toi. Mets la vidéo sur pause, et rédige les trois questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Question un. f prime de x vaut trois fois x au carré, moins trois. "
        "{s11.2}On factorise : trois, fois x moins un, fois x plus un.",
        "{s11.3}Sur moins un, un, x moins un est négatif et x plus un positif : f prime est négative, et ne s'annule qu'aux bornes. "
        "{s11.4}f est strictement décroissante sur moins un, un.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux. f est continue sur zéro, un, comme polynôme. {s12.2}Elle y est strictement décroissante. "
        "{s12.3}f de zéro vaut un, positif. f de un vaut un moins trois plus un : moins un, négatif. Zéro est entre les deux.",
        "{s12.4}D'après le corollaire du théorème des valeurs intermédiaires, l'équation f de x égale zéro a une unique solution alpha dans zéro, un.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois. À la calculatrice, avec un tableau de valeurs de pas un centième. "
        "{s13.2}f de zéro virgule trois quatre vaut environ zéro virgule zéro un neuf : positif. "
        "{s13.3}f de zéro virgule trois cinq vaut environ moins zéro virgule zéro zéro sept : négatif.",
        "{s13.4}Le signe change entre les deux. Donc alpha est entre zéro virgule trois quatre, et zéro virgule trois cinq.",
        "{-s13}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", etiquette="Exercice 1 · pour démarrer", titre="Unique solution",
                    enonce=["Soit $f(x)=x^3-3x+1$."],
                    questions=["Étudier les variations de $f$ sur $[-1;1]$.",
                               "Montrer que $f(x)=0$ a une unique solution $\\alpha$ dans $[0;1]$.",
                               "Donner un encadrement de $\\alpha$ d'amplitude $10^{-2}$."]),
        "pa1": dict(type="pause", t="Les variations, l'unique solution, puis l'encadrement."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", etiquette="Exercice 1", titre="Unique solution",
                     donnees=["$f(x)=x^3-3x+1$"],
                     questions=["variations sur $[-1;1]$", "unique solution dans $[0;1]$", "encadrement à $10^{-2}$"]),
        "s11": dict(type="formule", titre="1 · Variations", x=540, y=150, w=710, lignes=[
            dict(f="$f'(x)=3x^2-3$", taille=34),
            dict(f="$f'(x)=3(x-1)(x+1)$", ind=True, taille=34),
            dict(f="$f'\\leq0$ sur $[-1;1]$, nulle en $\\pm1$ seulement", taille=31),
            dict(f="$f$ strictement décroissante sur $[-1;1]$", cadre=True, taille=33)]),
        "s12": dict(type="formule", titre="2 · Unique solution", x=540, y=130, w=710, lignes=[
            dict(f="$f$ continue sur $[0;1]$ (polynôme)", taille=31),
            dict(f="strictement décroissante sur $[0;1]$", taille=31),
            dict(f="$f(0)=1>0$ et $f(1)=-1<0$", taille=31),
            dict(f="corollaire du TVI : unique $\\alpha\\in[0;1]$", cadre=True, taille=31)]),
        "s13": dict(type="formule", titre="3 · Encadrement", x=540, y=150, w=710, lignes=[
            dict(f="tableau de valeurs, pas $0{,}01$", txt=True),
            dict(f="$f(0{,}34)\\approx0{,}0193>0$", taille=34),
            dict(f="$f(0{,}35)\\approx-0{,}0071<0$", taille=34),
            dict(f="$0{,}34<\\alpha<0{,}35$", cadre=True, taille=36)]),
    }),

    # ================================================================ XI. exercice 2 (type bac)
    dict(id="exo2", chap="Exercice 2 · type bac", fond="carnet", humeur="tension", beats=[
        "{ex2}Deuxième exercice, au format du bac. f est définie sur zéro, plus l'infini, par f de x égale exponentielle de x, moins x, moins deux.",
        "Quatre questions. Un : les variations de f, et sa limite en plus l'infini. "
        "Deux : montrer que f de x égale zéro a une unique solution alpha, et qu'alpha est entre un et deux. "
        "Trois : compléter un programme Python de dichotomie, et donner un encadrement d'alpha de largeur un centième. "
        "Quatre : montrer que f est convexe, puis que f de x est supérieur ou égal à, exponentielle de un moins un, fois x, moins deux.",
        "{-ex2}{pa2}C'est un vrai sujet de bac. Prends le temps : mets sur pause, et rédige tout.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un. f prime de x vaut exponentielle de x, moins un. "
        "{s21.2}Sur zéro, plus l'infini, exponentielle de x est supérieure ou égale à un : f prime est positive, et ne s'annule qu'en zéro. "
        "f est strictement croissante, et f de zéro vaut un moins zéro moins deux : moins un.",
        "{s21.3}En plus l'infini, c'est une forme infini moins infini. On factorise par exponentielle de x : "
        "un, moins x sur exponentielle de x, moins deux sur exponentielle de x. {s21.4}Les deux fractions tendent vers zéro, "
        "la première par croissances comparées. La parenthèse tend vers un : f tend vers plus l'infini.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux. f est continue et strictement croissante sur zéro, plus l'infini. "
        "{s22.2}f de zéro vaut moins un, et f tend vers plus l'infini. Zéro est entre les deux. "
        "Par le corollaire du théorème des valeurs intermédiaires, f de x égale zéro a une unique solution alpha.",
        "{s22.3}De plus, f de un vaut exponentielle de un, moins trois : environ moins zéro virgule deux huit, négatif. "
        "{s22.4}Et f de deux vaut exponentielle de deux, moins quatre : environ trois virgule trois neuf, positif. Donc alpha est entre un et deux.",
        "{-s22}{ex2c.q3}{py3}{py3.l7}Question trois. La condition à compléter teste si f de a et f de m sont de signes contraires. "
        "{py3.r1}On écrit le produit des deux, inférieur ou égal à zéro.",
        "{py3.s}On appelle encadre de un, deux. Après sept étapes, on obtient un virgule un quatre zéro six deux cinq, et un virgule un quatre huit quatre trois sept cinq. "
        "{py3.l14}Pour donner deux décimales, on affine à la calculatrice. f de un virgule un quatre est négatif, f de un virgule un cinq positif. "
        "Donc alpha est entre un virgule un quatre, et un virgule un cinq.",
        "{-py3}{ex2c.q4}{s24}{s24.1}Question quatre. f seconde de x vaut exponentielle de x, strictement positive : f est convexe. "
        "{s24.2}Donc sa courbe est au-dessus de ses tangentes. Cherchons la tangente au point d'abscisse un.",
        "{s24.3}f prime de un vaut exponentielle de un, moins un. f de un vaut exponentielle de un, moins trois. "
        "{s24.4}La tangente : y égale exponentielle de un moins un, fois x moins un, plus exponentielle de un moins trois.",
        "{s24.5}On développe. Le terme constant vaut : moins exponentielle de un, plus un, plus exponentielle de un, moins trois. Il reste moins deux. "
        "{s24.6}La tangente a donc pour équation y égale exponentielle de un moins un, fois x, moins deux. "
        "La courbe est au-dessus : c'est l'inégalité demandée.",
        "{-s24}{g_bac}{g_bac.1}Voici la courbe, {g_bac.2}sa tangente au point d'abscisse un, toujours en dessous, "
        "{g_bac.3}et alpha, là où la courbe coupe l'axe.",
        "{-g_bac}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Étude, TVI et convexité",
                    enonce=["Soit $f$ définie sur $[0;+\\infty[$ par $f(x)=\\e^x-x-2$."],
                    questions=["Étudier les variations de $f$ et sa limite en $+\\infty$.",
                               "Montrer que $f(x)=0$ a une unique solution $\\alpha$, et que $1<\\alpha<2$.",
                               "Compléter un programme de dichotomie ; encadrer $\\alpha$ à $10^{-2}$.",
                               "Montrer que $f$ est convexe, puis que $f(x)\\geq(\\e-1)x-2$."]),
        "pa2": dict(type="pause", t="Variations et limite, unique solution, dichotomie, puis convexité."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", etiquette="Exercice 2 · type bac", titre="Étude, TVI et convexité",
                     donnees=["$f(x)=\\e^x-x-2$ sur $[0;+\\infty[$"],
                     questions=["variations, limite", "unique $\\alpha$, $1<\\alpha<2$", "dichotomie", "convexité, inégalité"]),
        "s21": dict(type="formule", titre="1 · Variations et limite", x=530, y=96, w=720, lignes=[
            dict(f="$f'(x)=\\e^x-1$", taille=31),
            dict(f="$f'\\geq0$ sur $[0;+\\infty[$, nulle en $0$ : strictement croissante, $f(0)=-1$", taille=27),
            dict(f="$f(x)=\\e^x\\left(1-\\dfrac{x}{\\e^x}-\\dfrac2{\\e^x}\\right)$", taille=31),
            dict(f="$\\lim_{x\\to+\\infty}f(x)=+\\infty$", cadre=True, taille=31)]),
        "s22": dict(type="formule", titre="2 · Unique solution", x=530, y=120, w=720, lignes=[
            dict(f="continue, strictement croissante sur $[0;+\\infty[$", taille=29),
            dict(f="$f(0)=-1<0$, $\\lim_{+\\infty}f=+\\infty$ : unique $\\alpha$", cadre=True, taille=29),
            dict(f="$f(1)=\\e-3\\approx-0{,}28<0$", taille=31),
            dict(f="$f(2)=\\e^2-4\\approx3{,}39>0$ : $1<\\alpha<2$", taille=31)]),
        "py3": dict(type="code", titre="Python · encadrer $\\alpha$", x=530, y=86, w=720, taille=23, lignes=[
            "from math import exp", "def f(x):", "    return exp(x) - x - 2", "def encadre(a, b):",
            "    while b - a > 0.01:", "        m = (a + b) / 2",
            "        if @1:", "            b = m", "        else:", "            a = m", "    return a, b", "",
            "print(encadre(1, 2))", "# 1,14 < alpha < 1,15"],
            rep=["f(a) * f(m) <= 0"], sortie="(1.140625, 1.1484375)"),
        "s24": dict(type="formule", copie=True, titre="4 · Convexité et inégalité", x=530, y=80, w=720, lignes=[
            dict(f="$f''(x)=\\e^x>0$ : $f$ convexe", taille=28),
            dict(f="courbe au-dessus de ses tangentes ; tangente en $1$ :", txt=True),
            dict(f="$f'(1)=\\e-1$, $f(1)=\\e-3$", ind=True, taille=28),
            dict(f="$y=(\\e-1)(x-1)+\\e-3$", ind=True, taille=28),
            dict(f="$y=(\\e-1)x-\\e+1+\\e-3=(\\e-1)x-2$", ind=True, taille=28),
            dict(f="$f(x)\\geq(\\e-1)x-2$ sur $[0;+\\infty[$", cadre=True, taille=28)]),
        "g_bac": dict(type="graphe", titre="$f(x)=\\e^x-x-2$ et sa tangente en $1$", x=540, y=110, w=700, h=560,
                      ax=dict(x=[0, 2.15], y=[-2.2, 4.4], gx=[0.5, 1, 1.5, 2], gy=[-2, -1, 1, 2, 3, 4], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=FBAC, c="iv", ep=3.4, dur=1.8),
                          dict(type="droite", pts=[[0, -2], [2.15, round((E1 - 1) * 2.15 - 2, 4)]], c="sa", ep=3,
                               lbl="$y=(\\e-1)x-2$", lp=[1.55, 0.6]),
                          dict(type="point", x=1.1462, y=0, c="ca", lbl="$\\alpha\\approx1{,}146$", lp=[0.72, 0.55])]),
    }),

    # ================================================================ XII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="craie", humeur="lumiere", beats=[
        "{carte}Récapitulons. {carte.1}Les composées : on dérive l'extérieur, et on multiplie par u prime. "
        "{carte.2}La convexité : f seconde positive, f prime croissante, la courbe au-dessus de ses tangentes ; "
        "et les points d'inflexion, où f seconde change de signe. "
        "{carte.3}La continuité : dérivable implique continue, et l'image d'une suite convergente. "
        "{carte.4}Et le théorème des valeurs intermédiaires, son corollaire, la dichotomie.",
        "{-carte}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Dériver une composée, et factoriser. "
        "{bac.2}Étudier la convexité avec le signe de f seconde, et trouver un point d'inflexion. "
        "{bac.3}Lire la convexité sur un graphique de f, de f prime ou de f seconde. "
        "{bac.4}Démontrer une inégalité par convexité, et refaire la démonstration exigible. "
        "{bac.5}Rédiger le corollaire du théorème des valeurs intermédiaires. {bac.6}Et encadrer une solution, par dichotomie ou à la calculatrice.",
        "Si tu sais faire ces six choses, ce chapitre est à toi. Les fiches, les QCM et les animations du chapitre t'attendent sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, un quiz sur cette vidéo t'y attend aussi.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="DÉRIVATION · CONVEXITÉ · CONTINUITÉ", branches=[
            dict(t="Composées", items=["$(v\\circ u)'=(v'\\circ u)\\times u'$", "$(\\e^u)'=u'\\,\\e^u$", "$(u^n)'=nu'u^{n-1}$"]),
            dict(t="Convexité", items=["$f''\\geq0$ ⇔ $f'$ croissante", "au-dessus des tangentes", "inflexion : signe de $f''$"]),
            dict(t="Continuité", items=["dérivable ⇒ continue", "$|x|$ : continue, pas dérivable", "$f(u_n)\\to f(\\ell)$"]),
            dict(t="TVI", items=["continue : existence", "monotone : unicité", "dichotomie : $\\frac{b-a}{2^n}$"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Dériver une composée, factoriser", "Convexité par le signe de $f''$, inflexion",
            "Lire la convexité sur $f$, $f'$ ou $f''$", "Inégalité par convexité, la démonstration",
            "Rédiger le corollaire du TVI", "Encadrer une solution"],
            marques=["✓"] * 6, x=150, y=96, w=980),
    }),
]

QUIZ = [
    dict(q="La dérivée de x ↦ e^(−3x²) est…", r=["e^(−3x²)", "−6x e^(−3x²)", "−6x"], ok=1,
         ex="(eᵘ)′ = u′eᵘ avec u(x) = −3x², u′(x) = −6x.", voir="tab_c"),
    dict(q="La dérivée de x ↦ (3x + 1)⁵ est…", r=["5(3x + 1)⁴", "15(3x + 1)⁴", "15(3x + 1)⁵"], ok=1,
         ex="(uⁿ)′ = nu′uⁿ⁻¹ : 5 × 3 × (3x + 1)⁴.", voir="exc1"),
    dict(q="f″ ≥ 0 sur I signifie que…", r=["f est croissante", "f est convexe : sa courbe est au-dessus de ses tangentes", "f est positive"],
         ok=1, ex="f″ ≥ 0 ⇔ f′ croissante ⇔ f convexe.", voir="carac"),
    dict(q="Pour f(x) = x⁴, en 0…", r=["il y a un point d'inflexion car f″(0) = 0", "il n'y a pas de point d'inflexion", "f est concave"],
         ok=1, ex="f″(x) = 12x² s'annule sans changer de signe : f est convexe sur ℝ.", voir="g_x4"),
    dict(q="L'inégalité eˣ ≥ x + 1 vient de…", r=["la convexité de exp et sa tangente en 0", "la concavité de exp", "du TVI"],
         ok=0, ex="La courbe convexe de exp est au-dessus de sa tangente en 0, d'équation y = x + 1.", voir="g_exp"),
    dict(q="Sur la courbe de f′, f est convexe là où…", r=["f′ est positive", "f′ est croissante", "f′ s'annule"], ok=1,
         ex="Convexe ⇔ f′ croissante ; le signe de f′ donne les variations de f.", voir="lect"),
    dict(q="La réciproque de « dérivable ⇒ continue »…", r=["est vraie", "est fausse : |x| est continue en 0 sans y être dérivable", "n'a pas de sens"],
         ok=1, ex="La valeur absolue a un coin en 0 : pentes −1 et 1.", voir="g_abs"),
    dict(q="f continue sur [0 ; 2], f(0) = −1, f(2) = 3. Alors f(x) = 1…", r=["a exactement une solution", "a au moins une solution", "n'a pas de solution"],
         ok=1, ex="TVI : au moins une. Pour « exactement une », il faut la stricte monotonie.", voir="thm_tvi"),
    dict(q="Par dichotomie sur [0 ; 1], combien d'étapes pour une largeur inférieure à 10⁻³ ?", r=["3", "10", "1000"], ok=1,
         ex="1/2¹⁰ = 1/1024 < 10⁻³, alors que 1/2⁹ = 1/512 > 10⁻³.", voir="ampl"),
    dict(q="uₙ → 2 et f(x) = x² + 1. Alors f(uₙ) →", r=["2", "4", "5"], ok=2,
         ex="f est continue en 2, donc f(uₙ) → f(2) = 5.", voir="suite"),
]

CREDITS = [
    "Animations, schémas, graphiques et exercices : faits pour le site. "
    "Polices : Carnet Math (sous-ensemble de STIX Two Math), Caveat, Spectral, Archivo, JetBrains Mono, sous licence SIL OFL.",
]
