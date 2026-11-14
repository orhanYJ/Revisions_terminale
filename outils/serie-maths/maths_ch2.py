"""Maths, chapitre 2 : « Limites de suites » — le cours en vidéo (site CQFD).

Même chaîne que la vidéo pilote maths_ch1.py (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les
mots) ; moteur maths/serie/moteur.js ; illustrations propres à la vidéo dans maths/serie/illu-maths-ch2.js : nuage
(suite de points, bande epsilon ou seuil A qui se règle, rang N) et zenon (la pièce à traverser).
Contenu : le chapitre 2 du site (outils/specialites/maths/src/ch2.js), rien au-delà ; ce qui dépasse le programme est dit
« pour aller plus loin ». Les deux exercices sont ceux du site (calculs de limites ; suite homographique, type bac).
Chaque calcul affiché ou dit est vérifié par outils/serie-maths/verif_ch2.py.
Usage : PYTHONPATH=outils/serie-maths python3 outils/serie-philo/verifier.py maths_ch2
        PYTHONPATH=outils/serie-maths SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py maths_ch2   (brouillon)
        python3 outils/serie-philo/chevauchements.py maths-ch2
"""
from math import sqrt

SITE = "maths"
CODE = "maths-ch2"
NOTION = "Limites de suites"
NUM = 2
TITRE = "Limites de suites"
SUIVANT = "Chapitre 3 · Limites de fonctions"
RYTHME = "vivant"
# bloc repris du pilote maths_ch1.py (lettres des formules en majuscules : la voix les dit comme des lettres, sans liaison)
PRONONCIATION = {"Bernoulli": "Bernouli", "Zénon": "Zénon", "Héron": "Héron",
                 "§n": "N", "§k": "K", "§f": "F", "§x": "X", "§b": "B", "§v": "V", "§m": "M", "§q": "Q",
                 # lettres propres au chapitre : ℓ (dite « l »), w, p, c, d, e (suites de l'exercice 1)
                 "§l": "L", "§w": "W", "§p": "P", "§c": "C", "§d": "D", "§e": "E"}
# devant une lettre ou un nombre qui commence par une voyelle, « plus » se dit [plys] et « moins » [mwɛ̃], sans
# liaison : la graphie donnée à la voix l'impose (« plusse un », « moin A ») ; liaisons.py contrôle chaque prise
for _tok in ("un", "une", "huit", "onze", "a", "u", "N", "F", "X", "M", "R", "A", "U", "L", "E", "epsilon"):
    PRONONCIATION["plus " + _tok] = "plusse " + _tok
    PRONONCIATION["moins " + _tok] = "moin " + _tok
PRONONCIATION["Moins un"] = "Moin un"
# « y » isolé : la lettre, dite « i grec » (pas le pronom de « il y a »)
PRONONCIATION["droite y égale"] = "droite i grec égale"
LIAISONS = "maths"

# ---------------------------------------------------------------- données des graphiques (vérifiées par verif_ch2.py)
RACN = [[n, round(sqrt(n), 4)] for n in range(41)]                                     # √n : seuils 2, 4, 6 → rangs 4, 16, 36
NONMAJ = [[n, n if n % 2 == 0 else 0] for n in range(21)]                              # n si n pair, 0 sinon
BANDE = [[n, round(2 + 3 * (-1) ** n / (n + 1), 4)] for n in range(31)]                # 2 + 3(−1)ⁿ/(n + 1)
ALT = [[n, (-1) ** n] for n in range(17)]                                              # (−1)ⁿ
UNSURN = [[n, round(1 + 1 / n, 4)] for n in range(1, 21)]                              # 1 + 1/n
GEND_U = [[n, round(2 + (-1) ** n / (n + 1), 4)] for n in range(26)]                   # 2 + (−1)ⁿ/(n + 1)
GEND_V = [[n, round(2 - 1 / (n + 1), 4)] for n in range(26)]
GEND_W = [[n, round(2 + 1 / (n + 1), 4)] for n in range(26)]
GEO = {q: [[n, round(q ** n, 4)] for n in range(16 if abs(q) < 1 else 11)] for q in (1.2, 0.8, -0.8, -1.2)}  # qⁿ (|q| > 1 : n ≤ 10, dans le cadre)
MONTE = [[n, round(1 - 1 / (n + 1), 4)] for n in range(21)]                            # 1 − 1/(n + 1), majorée par 5
RAC = [[round(x / 20, 3), round(sqrt(x / 20 + 2), 4)] for x in range(0, 49)]          # y = √(x + 2) sur [0 ; 2,4]
U_RAC = [1.0]
for _ in range(4):
    U_RAC.append(round(sqrt(U_RAC[-1] + 2), 4))                                         # 1 ; 1,732 ; 1,932 ; 1,983 ; 1,996


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ardoise", humeur="mystere", carton=False, beats=[
        "{zen}Tu es au bord d'une pièce, et tu veux atteindre le mur d'en face. {zen.1}D'abord, tu parcours la moitié du chemin. "
        "{zen.2}Puis la moitié de ce qui reste : un quart. {zen.3}Puis la moitié du reste : un huitième. {zen.4}Puis un seizième…",
        "{zen.go}Et ainsi de suite, sans fin. Ça fait une infinité d'étapes.",
        ("Alors, est-ce que tu arrives au mur ?", {"rate": "-6%"}),
        ("P", 0.5),
        "C'est un très vieux paradoxe, attribué au philosophe grec Zénon. Additionne les distances : un demi, puis trois quarts, "
        "puis sept huitièmes, puis quinze seizièmes. Après n étapes, il reste un, sur deux puissance n. "
        "Le total parcouru vaut un, moins un sur deux puissance n.",
        "{zen.fin}Et ce reste devient aussi petit qu'on veut. Le total, lui, finit aussi près qu'on veut de un. "
        "Une infinité d'étapes… et pourtant, une longueur finie.",
        ("P", 0.4),
        "{-zen}{q1}Toute la question du chapitre est là. Quand n devient très grand, que deviennent les termes d'une suite ? "
        "Est-ce qu'ils explosent ? Est-ce qu'ils s'installent près d'un nombre ? Ou est-ce qu'ils ne se décident jamais ?",
        "{-q1}{plan}Voici le chemin. {plan.1}D'abord, les deux définitions : tendre vers l'infini, et converger vers un réel. "
        "{plan.2}Ensuite, les outils de calcul : les opérations, les formes indéterminées, la comparaison et les gendarmes. "
        "{plan.3}Puis les suites géométriques, avec une démonstration exigible. "
        "{plan.4}Le théorème des suites monotones, et la méthode complète pour les suites définies par récurrence. "
        "{plan.5}Et pour finir, deux exercices corrigés, dont un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "zen": dict(type="illu", nom="zenon", x=40, y=110, w=1200, h=560,
                    fin="une infinité d'étapes, une longueur totale de $1$"),
        "q1": dict(type="question", t="Quand $n$ devient très grand, que deviennent les termes $u_n$ ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Tendre vers l'infini, converger vers un réel", "Opérations, formes indéterminées, comparaison, gendarmes",
            "Les suites géométriques $q^n$", "Suites monotones, suites $u_{n+1}=f(u_n)$",
            "Deux exercices corrigés, dont un type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Maths · Chapitre 2", t="Limites de suites",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. tendre vers +∞
    dict(id="infini", chap="Tendre vers plus l'infini", fond="ardoise", humeur="lumiere",
         retenir="$\\lim u_n=+\\infty$ : tout intervalle $[A;+\\infty[$ contient tous les termes à partir d'un certain rang. "
                 "Une suite croissante non majorée tend vers $+\\infty$.",
         beats=[
        "{rac}Commençons par une suite simple : racine de n. {rac.s1}Zéro, un, environ un virgule quatre, un virgule sept, puis deux… "
        "Les termes grandissent. Lentement, mais sans jamais s'arrêter.",
        "Que veut dire, précisément, « tendre vers plus l'infini » ? On se fixe un seuil, A. "
        "{rac.b1}Par exemple, A égale deux. À partir du rang quatre, tous les termes valent au moins deux. Tous, et pour toujours.",
        "{rac.b2}On monte le seuil : A égale quatre. Il faut aller plus loin, jusqu'au rang seize. Mais à partir de là, encore une fois, "
        "plus aucun terme ne passe en dessous. {rac.b3}A égale six : rang trente-six.",
        "Aussi haut que soit le seuil, il existe un rang à partir duquel la suite le dépasse, et ne redescend plus jamais en dessous. "
        "C'est ça, tendre vers plus l'infini.",
        "{-rac}{def_inf}Voici la définition. La suite u tend vers plus l'infini si tout intervalle de la forme A, plus l'infini, "
        "contient tous les termes u indice n, à partir d'un certain rang. "
        "{def_inf.1}On écrit : la limite de u indice n, quand n tend vers plus l'infini, égale plus l'infini.",
        "{-def_inf}{calc_rac}Vérifions-le pour racine de n. {calc_rac.1}Soit A un réel strictement positif. "
        "La racine de n est supérieure ou égale à A, si et seulement si n est supérieur ou égal à A au carré. "
        "{calc_rac.2}Donc, dès que n dépasse A au carré, tous les termes sont dans l'intervalle. "
        "{calc_rac.3}Pour A égale cent, c'est à partir du rang dix mille. Loin… mais ce rang existe.",
        "{-calc_rac}{ref}Les limites de référence. {ref.1}n, n au carré, n au cube, et racine de n tendent vers plus l'infini. "
        "{ref.2}Plus généralement, n puissance p, pour tout entier p supérieur ou égal à un. "
        "{ref.3}Et dans l'autre sens : une suite tend vers moins l'infini si tout intervalle de moins l'infini à A contient tous ses termes, "
        "à partir d'un certain rang.",
        "{-ref}{tag_bo}{thm_cnm}Premier théorème, et première démonstration exigible. "
        "{thm_cnm.1}Toute suite croissante et non majorée tend vers plus l'infini.",
        "{-thm_cnm}{-tag_bo}{dem_cnm}Démontrons-le. {dem_cnm.1}Soit u une suite croissante et non majorée. Et soit A un réel, n'importe lequel.",
        "{dem_cnm.2}La suite n'est pas majorée : donc A n'est pas un majorant. Il existe donc un rang, appelons-le grand N, "
        "tel que u indice grand N est strictement plus grand que A.",
        "{dem_cnm.3}Et la suite est croissante : pour tout n supérieur ou égal à grand N, u indice n est supérieur ou égal à u indice grand N. "
        "Donc il est plus grand que A.",
        "{dem_cnm.4}Ainsi, tous les termes à partir du rang grand N sont dans l'intervalle A, plus l'infini. Et ça marche pour n'importe quel A. "
        "Par définition, la suite tend vers plus l'infini.",
        "{dem_cnm.5}Regarde : chaque hypothèse sert une fois. « Non majorée », pour trouver le rang. « Croissante », pour rester au-dessus.",
        "{-dem_cnm}{nm}Et la croissance est indispensable. Regarde cette suite. {nm.s1}u indice n vaut n quand n est pair, et zéro quand n est impair. "
        "Elle n'est pas majorée : ses termes pairs grandissent sans fin.",
        "{nm.b1}Mais fixe un seuil, huit par exemple. Une infinité de termes valent zéro, en dessous. Aucun rang ne convient. "
        "Non majorée, mais elle ne tend pas vers plus l'infini.",
        "{-nm}",
    ], vis={
        "rac": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                    ax=dict(x=[0, 41], y=[0, 7.2], gx=[10, 20, 30, 40], gy=[2, 4, 6], lx="$n$"),
                    series=[dict(pts=RACN, c="te", r=5.5, pas=.06, lab="$u_n=\\sqrt n$", lp=[3.2, 6.6])],
                    etapes=[dict(type="seuil", A=2, N=4, lab="$A=2$ : dès le rang $4$", lp=[28, 1.2]),
                            dict(type="seuil", A=4, N=16, lab="$A=4$ : dès le rang $16$", lp=[28, 1.2]),
                            dict(type="seuil", A=6, N=36, lab="$A=6$ : dès le rang $36$", lp=[28, 1.2])]),
        "def_inf": dict(type="def", terme="Tendre vers $+\\infty$", cles=["tout", "tous"],
                        t="La suite $(u_n)$ tend vers $+\\infty$ si tout intervalle $[A;+\\infty[$ contient tous les termes $u_n$ à partir d'un certain rang.",
                        etape="On note $\\lim_{n\\to+\\infty}u_n=+\\infty$.", x=170, y=180, w=940),
        "calc_rac": dict(type="formule", titre="Exemple : $\\sqrt n$", x=150, y=150, w=980, lignes=[
            dict(f="Soit $A>0$ : $\\sqrt n\\geq A\\iff n\\geq A^2$"),
            dict(f="dès que $n\\geq A^2$, tous les termes sont dans $[A;+\\infty[$", txt=True),
            dict(f="$A=100$ : à partir du rang $10\\,000$", cadre=True)]),
        "ref": dict(type="formule", titre="Limites de référence", x=150, y=150, w=980, lignes=[
            dict(f="$\\lim n=\\lim n^2=\\lim n^3=\\lim\\sqrt n=+\\infty$", taille=44),
            dict(f="$\\lim n^p=+\\infty$ pour tout entier $p\\geq1$", cadre=True),
            dict(f="$\\lim u_n=-\\infty$ : tout $]-\\infty;A]$ contient tous les termes à partir d'un certain rang", txt=True)]),
        "tag_bo": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=170, y=130, w=600),
        "thm_cnm": dict(type="def", terme="Théorème", cles=["croissante", "majorée"],
                        t="Toute suite croissante et non majorée tend vers $+\\infty$.", x=170, y=240, w=940),
        "dem_cnm": dict(type="formule", copie=True, titre="Démonstration exigible : croissante et non majorée", x=90, y=90, w=1100, lignes=[
            dict(f="Soit $(u_n)$ croissante et non majorée, et soit $A$ un réel.", taille=32),
            dict(lab="Non majorée :", f="$A$ n'est pas un majorant, donc il existe $N$ tel que $u_N>A$.", taille=32),
            dict(lab="Croissante :", f="pour tout $n\\geq N$, $u_n\\geq u_N>A$.", taille=32),
            dict(f="Dès le rang $N$, tous les termes sont dans $[A;+\\infty[$, et ce pour tout $A$ : $\\lim u_n=+\\infty$.", cadre=True, taille=32),
            dict(f="« non majorée » donne le rang ; « croissante » garde au-dessus", txt=True)]),
        "nm": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                   ax=dict(x=[0, 21], y=[0, 21.5], gx=[5, 10, 15, 20], gy=[5, 10, 15, 20], lx="$n$"),
                   series=[dict(pts=NONMAJ, c="te", r=6, pas=.1, lab="$n$ si $n$ pair, $0$ sinon", lp=[5.5, 19.8])],
                   etapes=[dict(type="seuil", A=8, N=None, lab="seuil $8$ : aucun rang ne convient", lp=[13.5, 5.6])]),
    }),

    # ================================================================ II. converger vers un réel
    dict(id="converge", chap="Converger vers un réel", fond="carnet", humeur="mystere",
         retenir="$\\lim u_n=\\ell$ : tout intervalle ouvert contenant $\\ell$ contient tous les termes à partir d'un certain rang. "
                 "Une suite qui ne converge pas est divergente.",
         beats=[
        "{bande}Maintenant, une suite qui ne part pas à l'infini. {bande.s1}u indice n égale deux, plus trois fois moins un puissance n, sur n plus un. "
        "Ses termes oscillent : au-dessus de deux, en dessous, au-dessus… en se rapprochant. {bande.l}On trace la droite y égale deux.",
        "Comment dire, précisément, que la suite « s'installe » près de deux ? {bande.b1}On trace une bande autour de deux, de demi-largeur epsilon. "
        "Avec epsilon égale un : à partir du rang trois, tous les termes sont dans la bande.",
        "{bande.b2}On resserre : epsilon égale zéro virgule cinq. Il faut aller plus loin, jusqu'au rang six. "
        "{bande.b3}Epsilon égale zéro virgule deux : rang quinze. La bande rétrécit, le rang recule… mais il existe toujours.",
        "Aussi étroite que soit la bande, il existe un rang à partir duquel tous les termes sont dedans. C'est ça, converger vers deux.",
        "{-bande}{def_cv}La définition. La suite u converge vers le réel l si tout intervalle ouvert contenant l contient tous les termes "
        "u indice n, à partir d'un certain rang. On écrit : la limite de u indice n égale l. "
        "{def_cv.1}Et une suite qui ne converge pas est dite divergente.",
        "{-def_cv}{eps}En pratique, on prend des intervalles centrés en l. {eps.1}Pour tout epsilon strictement positif, il existe un rang grand N "
        "tel que, {eps.2}pour tout n supérieur ou égal à grand N, la distance entre u indice n et l est plus petite qu'epsilon. "
        "{eps.3}Autrement dit, à partir de ce rang, u indice n reste coincé entre l moins epsilon et l plus epsilon.",
        "{-eps}{uni}Deux propriétés. {uni.1}Si une suite converge, sa limite est unique. "
        "{uni.2}Et les limites de référence : un sur n, un sur n au carré, et un sur racine de n tendent vers zéro. "
        "{uni.3}Plus généralement, un sur n puissance p tend vers zéro, pour tout entier p supérieur ou égal à un.",
        "{-uni}{alt}Une suite divergente peut tendre vers plus ou moins l'infini. Mais elle peut aussi n'avoir aucune limite. "
        "{alt.s1}Exemple : moins un puissance n. Un, moins un, un, moins un…",
        "{alt.b1}Prends une bande étroite autour de un : les termes de rang impair, qui valent moins un, en sortent toujours. "
        "Et autour de moins un, ce sont les termes de rang pair. Aucune bande étroite ne contient tous les termes à partir d'un rang. Pas de limite.",
        "{-alt}{app}Et maintenant, un piège de vocabulaire. {app.s1}Regarde u indice n égale un plus un sur n. Deux, un virgule cinq, "
        "environ un virgule trente-trois… Les termes diminuent : chacun est plus près de zéro que le précédent. Ils « se rapprochent » de zéro.",
        "{app.b1}Mais la limite, c'est un. Les termes finissent aussi près qu'on veut de un, et ils y restent. De zéro, jamais.",
        "{-app}{piege_app}Retiens-le. Converger vers l, ce n'est pas seulement « se rapprocher » de l. "
        "C'est finir aussi près qu'on veut de l, à partir d'un certain rang.",
        "{-piege_app}",
    ], vis={
        "bande": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                      ax=dict(x=[0, 31], y=[-1.2, 5.4], gx=[5, 10, 15, 20, 25, 30], gy=[1, 2, 3, 4, 5], lx="$n$"),
                      series=[dict(pts=BANDE, c="te", r=6, pas=.07, lab="$u_n=2+\\frac{3(-1)^n}{n+1}$", lp=[22.5, 5.2])],
                      ligne=dict(y=2, lab="$\\ell=2$"),
                      etapes=[dict(type="bande", l=2, e=1, N=3, lab="$\\varepsilon=1$ : dès le rang $3$", lp=[22.5, 3.75]),
                              dict(type="bande", l=2, e=0.5, N=6, lab="$\\varepsilon=0{,}5$ : dès le rang $6$", lp=[22.5, 3.75]),
                              dict(type="bande", l=2, e=0.2, N=15, lab="$\\varepsilon=0{,}2$ : dès le rang $15$", lp=[22.5, 3.75])]),
        "def_cv": dict(type="def", terme="Converger vers un réel $\\ell$", cles=["ouvert", "tous"],
                       t="La suite $(u_n)$ converge vers $\\ell$ si tout intervalle ouvert contenant $\\ell$ contient tous les termes $u_n$ "
                         "à partir d'un certain rang. On note $\\lim_{n\\to+\\infty}u_n=\\ell$.",
                       etape="Une suite qui ne converge pas est divergente.", x=170, y=170, w=940),
        "eps": dict(type="formule", titre="Avec $\\varepsilon$", x=150, y=150, w=980, lignes=[
            dict(f="pour tout $\\varepsilon>0$, il existe un rang $N$ tel que :", txt=True),
            dict(f="$n\\geq N\\Rightarrow|u_n-\\ell|<\\varepsilon$", cadre=True, taille=50),
            dict(f="c'est-à-dire $\\ell-\\varepsilon<u_n<\\ell+\\varepsilon$", taille=40)]),
        "uni": dict(type="formule", titre="À connaître", x=150, y=150, w=980, lignes=[
            dict(f="Si une suite converge, sa limite est unique.", txt=True),
            dict(f="$\\lim\\dfrac1n=\\lim\\dfrac1{n^2}=\\lim\\dfrac1{\\sqrt n}=0$", taille=44),
            dict(f="$\\lim\\dfrac1{n^p}=0$ pour tout entier $p\\geq1$", cadre=True)]),
        "alt": dict(type="illu", nom="nuage", x=170, y=110, w=940, h=560,
                    ax=dict(x=[0, 17], y=[-1.6, 1.8], gx=[4, 8, 12, 16], gy=[-1, 1], lx="$n$"),
                    series=[dict(pts=ALT, c="te", r=7, pas=.12, trait="pale", lab="$(-1)^n$", lp=[0.6, 1.72])],
                    etapes=[dict(type="bande", l=1, e=0.4, N=None, lab="autour de $1$ : jamais tous dedans", lp=[9.5, 0.35])]),
        "app": dict(type="illu", nom="nuage", x=170, y=110, w=940, h=560,
                    ax=dict(x=[0, 21], y=[0, 2.3], gx=[5, 10, 15, 20], gy=[1, 2], lx="$n$"),
                    series=[dict(pts=UNSURN, c="te", r=6, pas=.1, lab="$u_n=1+\\frac1n$", lp=[14, 2.15])],
                    ligne=dict(y=1, lab="$\\ell=1$"),
                    etapes=[dict(type="bande", l=1, e=0.25, N=5, lab="les termes finissent près de $1$, pas de $0$", lp=[11, 0.42])]),
        "piege_app": dict(type="note", titre="Piège", cles=["rapprocher", "aussi"],
                          t="Converger vers $\\ell$, ce n'est pas « se rapprocher » de $\\ell$ : c'est finir aussi près qu'on veut de $\\ell$, à partir d'un certain rang.",
                          x=170, y=210, w=940),
    }),

    # ================================================================ III. opérations, formes indéterminées
    dict(id="operations", chap="Opérations et formes indéterminées", fond="ardoise", humeur="calme",
         retenir="Quatre formes indéterminées : $\\infty-\\infty$, $0\\times\\infty$, $\\frac\\infty\\infty$, $\\frac00$. "
                 "Pour les lever : factoriser le terme prépondérant, ou multiplier par la quantité conjuguée.",
         beats=[
        "{ops}Pour calculer une limite, on n'utilise presque jamais la définition. On utilise des règles d'opérations, qui sont admises. "
        "Voici les principales, en raccourci. {ops.1}Si u tend vers l et v vers l prime, la somme tend vers l plus l prime. "
        "{ops.2}Un nombre plus une suite qui tend vers plus l'infini : la somme tend vers plus l'infini. {ops.3}Et plus l'infini, ajouté à plus l'infini, donne plus l'infini.",
        "{ops.4}Pour un produit : l fois plus l'infini, ça donne plus l'infini si l est strictement positif, moins l'infini s'il est strictement négatif. "
        "{ops.5}Pour un quotient : un nombre divisé par une suite qui tend vers l'infini, ça tend vers zéro. "
        "{ops.6}Et un nombre non nul divisé par une suite qui tend vers zéro, en gardant un signe constant : ça tend vers l'infini, avec la règle des signes.",
        "{-ops}{q_fi}Mais dans quatre cas, les règles ne concluent pas. {-q_fi}Ce sont les {!formes indéterminées}formes indéterminées. "
        "{fi}{fi.1}L'infini moins l'infini. {fi.2}Zéro fois l'infini. {fi.3}L'infini sur l'infini. {fi.4}Et zéro sur zéro.",
        "Attention : ça ne veut pas dire que la limite n'existe pas. Ça veut dire qu'il faut transformer l'écriture avant de conclure.",
        "{-fi}{fi_ex}La preuve que rien n'est décidé d'avance. {fi_ex.1}n au carré, moins n : forme infini moins infini, et ça tend vers plus l'infini. "
        "{fi_ex.2}n moins n au carré : même forme, et ça tend vers moins l'infini. "
        "{fi_ex.3}Et deux n sur n : forme infini sur infini, et ça vaut deux. "
        "Donc jamais « infini moins infini égale zéro », ni « infini sur infini égale un ».",
        "{-fi_ex}{prep}La méthode reine : factoriser par le {!terme prépondérant}terme prépondérant, celui qui grandit le plus vite. "
        "{prep.1}Exemple : trois n au carré, moins n, plus un, le tout sur deux n au carré, plus cinq. En haut comme en bas, ça tend vers plus l'infini : forme indéterminée.",
        "{prep.2}On factorise par n au carré, en haut et en bas. {prep.3}Les n au carré se simplifient. "
        "Il reste : trois, moins un sur n, plus un sur n au carré ; sur deux, plus cinq sur n au carré.",
        "{prep.4}Or un sur n, un sur n au carré, et cinq sur n au carré tendent vers zéro. La limite vaut trois demis. "
        "{prep.5}Python le confirme : u indice mille vaut environ un virgule quatre mille neuf cent quatre-vingt-quinze.",
        "{-prep}{poly}Même idée pour un polynôme. {poly.1}n au carré, moins cinq n : forme infini moins infini. "
        "{poly.2}On factorise par n au carré : n au carré, fois un moins cinq sur n. "
        "{poly.3}n au carré tend vers plus l'infini, un moins cinq sur n tend vers un : le produit tend vers plus l'infini. "
        "{poly.4}Retiens : un polynôme en n a la limite de son terme de plus haut degré.",
        "{-poly}{q_rac}Et avec des racines ? Là, factoriser ne suffit pas. {-q_rac}L'astuce, c'est la {!quantité conjuguée}quantité conjuguée. "
        "{conj}{conj.1}La racine de la somme n plus un, moins la racine de n : forme infini moins infini. {conj.2}On multiplie et on divise par la racine de n plus un, plus la racine de n.",
        "{conj.3}En haut, on reconnaît une identité remarquable : la différence des carrés. Il reste n plus un, moins n : c'est-à-dire un. "
        "{conj.4}On obtient un, sur une somme qui tend vers plus l'infini. La limite vaut zéro.",
        "{-conj}",
    ], vis={
        "ops": dict(type="formule", titre="Les règles, en raccourci", x=150, y=74, w=980, lignes=[
            dict(f="$\\ell+\\ell'$", taille=34, m="somme"),
            dict(f="$\\ell+(+\\infty)=+\\infty$", taille=34),
            dict(f="$(+\\infty)+(+\\infty)=+\\infty$", taille=34),
            dict(f="$\\ell\\times(+\\infty)=+\\infty$ si $\\ell>0$, $-\\infty$ si $\\ell<0$", taille=34, m="produit"),
            dict(f="$\\dfrac{\\ell}{\\pm\\infty}=0$", taille=34, m="quotient"),
            dict(f="$\\dfrac{\\ell}{0}=\\pm\\infty$ si $\\ell\\neq0$, dénominateur de signe constant", taille=34)]),
        "q_fi": dict(type="question", t="Et quand les règles ne concluent pas ?"),
        "q_rac": dict(type="question", t="Et avec des racines, comme $\\sqrt{n+1}-\\sqrt n$ ?"),
        "fi": dict(type="liste", titre="Les quatre formes indéterminées", items=[
            "$+\\infty-(+\\infty)$", "$0\\times\\infty$", "$\\dfrac{\\infty}{\\infty}$", "$\\dfrac00$"],
            marques=["?", "?", "?", "?"], x=330, y=120, w=620),
        "fi_ex": dict(type="formule", titre="Rien n'est décidé d'avance", x=150, y=150, w=980, lignes=[
            dict(f="$n^2-n\\to+\\infty$", n="forme $\\infty-\\infty$"),
            dict(f="$n-n^2\\to-\\infty$", n="même forme, autre limite"),
            dict(f="$\\dfrac{2n}{n}=2$", n="forme $\\frac\\infty\\infty$, et la limite vaut $2$")]),
        "prep": dict(type="formule", titre="Le terme prépondérant", x=120, y=74, w=1040, lignes=[
            dict(f="$u_n=\\dfrac{3n^2-n+1}{2n^2+5}$ : forme $\\frac\\infty\\infty$", taille=34),
            dict(f="$u_n=\\dfrac{n^2\\left(3-\\frac1n+\\frac1{n^2}\\right)}{n^2\\left(2+\\frac5{n^2}\\right)}$", ind=True, taille=34, m="on factorise par $n^2$"),
            dict(f="$u_n=\\dfrac{3-\\frac1n+\\frac1{n^2}}{2+\\frac5{n^2}}$", ind=True, taille=34),
            dict(f="$\\lim u_n=\\dfrac32$", cadre=True, taille=38),
            dict(f="Python : $u_{1000}\\approx1{,}4995$", ok=True, taille=32)]),
        "poly": dict(type="formule", titre="Un polynôme", x=150, y=150, w=980, lignes=[
            dict(f="$u_n=n^2-5n$ : forme $\\infty-\\infty$"),
            dict(f="$u_n=n^2\\left(1-\\frac5n\\right)$", ind=True),
            dict(f="$n^2\\to+\\infty$ et $1-\\frac5n\\to1$, donc $u_n\\to+\\infty$", ind=True),
            dict(f="un polynôme a la limite de son terme de plus haut degré", cadre=True, taille=34)]),
        "conj": dict(type="formule", titre="La quantité conjuguée", x=120, y=110, w=1040, lignes=[
            dict(f="$u_n=\\sqrt{n+1}-\\sqrt n$ : forme $\\infty-\\infty$", taille=36),
            dict(f="$u_n=\\dfrac{\\left(\\sqrt{n+1}-\\sqrt n\\right)\\left(\\sqrt{n+1}+\\sqrt n\\right)}{\\sqrt{n+1}+\\sqrt n}$", ind=True, taille=34),
            dict(f="$u_n=\\dfrac{(n+1)-n}{\\sqrt{n+1}+\\sqrt n}=\\dfrac{1}{\\sqrt{n+1}+\\sqrt n}$", ind=True, taille=34, m="$(a-b)(a+b)=a^2-b^2$"),
            dict(f="$\\lim u_n=0$", cadre=True, taille=38)]),
    }),

    # ================================================================ IV. comparaison et gendarmes
    dict(id="comparaison", chap="Comparaison et théorème des gendarmes", fond="carnet", humeur="tension",
         retenir="Si $u_n\\geq v_n$ et $v_n\\to+\\infty$, alors $u_n\\to+\\infty$. Si $v_n\\leq u_n\\leq w_n$ et si $v_n$ et $w_n$ "
                 "tendent vers la même limite $\\ell$, alors $u_n\\to\\ell$.",
         beats=[
        "{q_cmp}Que faire quand une suite contient un morceau qui ne se calme jamais, comme moins un puissance n ? "
        "Les opérations ne suffisent plus. On compare.",
        "{-q_cmp}{cmp}{cmp.1}Le théorème de comparaison. Si, à partir d'un certain rang, u indice n est supérieur ou égal à v indice n, "
        "et si v indice n tend vers plus l'infini, alors u indice n tend vers plus l'infini. "
        "{cmp.2}C'est logique : u est poussée vers le haut par v. "
        "{cmp.3}Et de même vers le bas : si u indice n est inférieur ou égal à w indice n, et si w indice n tend vers moins l'infini, "
        "alors u indice n tend vers moins l'infini.",
        "{-cmp}{tag_bo2}{dem_cmp}La première propriété est une démonstration exigible. "
        "{dem_cmp.1}Les hypothèses : à partir d'un rang n un, u indice n est supérieur ou égal à v indice n. Et v indice n tend vers plus l'infini.",
        "{dem_cmp.2}Soit A un réel. Comme v indice n tend vers plus l'infini, il existe un rang n deux, à partir duquel v indice n est supérieur ou égal à A.",
        "{dem_cmp.3}On prend grand N, le plus grand des deux rangs, n un et n deux. "
        "{dem_cmp.4}Pour n supérieur ou égal à grand N, les deux informations sont vraies en même temps : "
        "u indice n est supérieur ou égal à v indice n, qui est supérieur ou égal à A.",
        "{dem_cmp.5}Donc, à partir du rang grand N, tous les termes u indice n sont dans l'intervalle A, plus l'infini. "
        "Par définition, u indice n tend vers plus l'infini. L'astuce à retenir : prendre le plus grand des deux rangs.",
        "{-dem_cmp}{-tag_bo2}{min_ex}Un exemple. {min_ex.1}u indice n égale n, plus moins un puissance n. "
        "Moins un puissance n vaut un ou moins un : il est toujours supérieur ou égal à moins un. "
        "{min_ex.2}Donc u indice n est supérieur ou égal à n moins un. "
        "{min_ex.3}Et n moins un tend vers plus l'infini. Par comparaison, u indice n tend vers plus l'infini.",
        "{-min_ex}Pour une limite finie, il y a le {!théorème des gendarmes}théorème des gendarmes. "
        "{gend}{gend.s1}Prends u indice n égale deux, plus moins un puissance n, sur n plus un. Les termes sautillent autour de deux.",
        "{gend.s2}On les coince entre deux suites. En dessous, deux moins un sur n plus un. {gend.s3}Au-dessus, deux plus un sur n plus un. "
        "{gend.l}Et ces deux gendarmes tendent tous les deux vers deux. "
        "Le prisonnier, coincé entre eux, n'a pas le choix : il tend vers deux, lui aussi.",
        "{-gend}{thm_g}Le théorème. {thm_g.1}Si, à partir d'un certain rang, v indice n est inférieur ou égal à u indice n, inférieur ou égal à w indice n, "
        "{thm_g.2}et si v et w convergent vers la même limite l, {thm_g.3}alors u converge vers l.",
        "{-thm_g}{red_g}La rédaction, sur notre exemple. {red_g.1}Pour tout n, moins un puissance n est compris entre moins un et un. "
        "{red_g.2}On divise par n plus un, qui est strictement positif : le sens ne change pas. "
        "{red_g.3}Puis on ajoute deux : deux moins un sur n plus un, inférieur ou égal à u indice n, inférieur ou égal à deux plus un sur n plus un. "
        "{red_g.4}Les deux gendarmes tendent vers deux. Donc, d'après le théorème des gendarmes, u indice n tend vers deux.",
        "{-red_g}{p_g}Deux pièges. {p_g.1}Les gendarmes doivent avoir la même limite. Si v tend vers un et w vers trois, "
        "l'encadrement ne dit pas si u converge.",
        "{p_g.2}Le passage à la limite dans une inégalité : si u indice n est inférieur ou égal à v indice n, et si les deux suites convergent, "
        "alors la limite de u est inférieure ou égale à celle de v. "
        "{p_g.3}Mais attention : les inégalités strictes deviennent larges. Un sur n est strictement positif pour tout n supérieur ou égal à un, et pourtant sa limite vaut zéro.",
        "{-p_g}",
    ], vis={
        "q_cmp": dict(type="question", t="Et si la suite contient un morceau qui ne se calme jamais, comme $(-1)^n$ ?"),
        "cmp": dict(type="formule", titre="Le théorème de comparaison", x=120, y=130, w=1040, lignes=[
            dict(f="Si $u_n\\geq v_n$ à partir d'un certain rang et $\\lim v_n=+\\infty$, alors $\\lim u_n=+\\infty$.", cadre=True, taille=34),
            dict(f="$u_n$ est poussée vers le haut par $v_n$", txt=True),
            dict(f="Si $u_n\\leq w_n$ à partir d'un certain rang et $\\lim w_n=-\\infty$, alors $\\lim u_n=-\\infty$.", taille=34)]),
        "tag_bo2": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=660, y=34, w=560),
        "dem_cmp": dict(type="formule", copie=True, titre="Démonstration exigible : la comparaison", x=90, y=124, w=1100, lignes=[
            dict(lab="Hypothèses.", f="$u_n\\geq v_n$ pour $n\\geq n_1$, et $\\lim v_n=+\\infty$.", taille=32),
            dict(f="Soit $A$ réel : il existe $n_2$ tel que $n\\geq n_2\\Rightarrow v_n\\geq A$.", taille=32),
            dict(f="On pose $N$ = le plus grand des rangs $n_1$ et $n_2$.", hl=True, m="l'astuce !", taille=32),
            dict(f="Pour $n\\geq N$ : $u_n\\geq v_n\\geq A$.", ind=True, taille=32),
            dict(f="Dès le rang $N$, tous les $u_n$ sont dans $[A;+\\infty[$ : $\\lim u_n=+\\infty$.", cadre=True, taille=32)]),
        "min_ex": dict(type="formule", titre="Minorer pour aller vers l'infini", x=150, y=150, w=980, lignes=[
            dict(f="$u_n=n+(-1)^n$ et $(-1)^n\\geq-1$"),
            dict(f="donc $u_n\\geq n-1$", ind=True),
            dict(f="$\\lim(n-1)=+\\infty$, donc par comparaison $\\lim u_n=+\\infty$", cadre=True, taille=36)]),
        "gend": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                     ax=dict(x=[0, 26], y=[0.9, 3.1], gx=[5, 10, 15, 20, 25], gy=[1.5, 2, 2.5, 3], lx="$n$"),
                     series=[dict(pts=GEND_U, c="sa", r=6.5, pas=.08, lab="$u_n$", lp=[13, 2.45]),
                             dict(pts=GEND_V, c="te", trait=True, points=False, ep=3, lab="$v_n=2-\\frac1{n+1}$", lp=[4.5, 1.3]),
                             dict(pts=GEND_W, c="ca", trait=True, points=False, ep=3, lab="$w_n=2+\\frac1{n+1}$", lp=[4.5, 2.95])],
                     ligne=dict(y=2, lab="$2$")),
        "thm_g": dict(type="formule", titre="Le théorème des gendarmes", x=150, y=150, w=980, lignes=[
            dict(f="Si, à partir d'un certain rang, $v_n\\leq u_n\\leq w_n$,", taille=38),
            dict(f="et si $(v_n)$ et $(w_n)$ convergent vers la même limite $\\ell$,", taille=38),
            dict(f="alors $(u_n)$ converge vers $\\ell$.", cadre=True, taille=40)]),
        "red_g": dict(type="formule", copie=True, titre="Rédaction : $u_n=2+\\frac{(-1)^n}{n+1}$", x=100, y=110, w=1080, lignes=[
            dict(f="$-1\\leq(-1)^n\\leq1$", taille=34),
            dict(f="$-\\dfrac1{n+1}\\leq\\dfrac{(-1)^n}{n+1}\\leq\\dfrac1{n+1}$", ind=True, m="$n+1>0$", taille=34),
            dict(f="$2-\\dfrac1{n+1}\\leq u_n\\leq2+\\dfrac1{n+1}$", ind=True, m="on ajoute $2$", taille=34),
            dict(f="les deux gendarmes tendent vers $2$, donc $\\lim u_n=2$", cadre=True, taille=34)]),
        "p_g": dict(type="liste", titre="Deux pièges", items=[
            "Les gendarmes doivent avoir la même limite",
            "Si $u_n\\leq v_n$ et si les deux convergent : $\\lim u_n\\leq\\lim v_n$",
            "$\\frac1n>0$ mais $\\lim\\frac1n=0$ : à la limite, $<$ devient $\\leq$"], marques=["!", "·", "!"], x=150, y=170, w=980),
    }),

    # ================================================================ V. suites géométriques
    dict(id="geometrique", chap="Les suites géométriques", fond="ardoise", humeur="lumiere",
         retenir="$q>1$ : $q^n\\to+\\infty$ ; $q=1$ : $q^n=1$ ; $-1<q<1$ : $q^n\\to0$ ; $q\\leq-1$ : pas de limite. "
                 "Si $-1<q<1$ : $1+q+\\cdots+q^n\\to\\frac1{1-q}$.",
         beats=[
        "{geo}Passons aux suites géométriques : q puissance n. Tout dépend de q. "
        "{geo.q1}Avec q égale un virgule deux, chaque terme est vingt pour cent plus grand que le précédent. Les termes dépassent tout seuil.",
        "{geo.q2}Avec q égale zéro virgule huit, chaque terme perd vingt pour cent. Les termes fondent vers zéro, sans jamais l'atteindre.",
        "{geo.q3}Avec q égale moins zéro virgule huit, le signe change à chaque pas, mais la taille fond : les termes zigzaguent vers zéro.",
        "{geo.q4}Et avec q égale moins un virgule deux, le signe change, et la taille grandit. Les termes sautent de plus en plus loin, "
        "d'un côté puis de l'autre. Ni plus l'infini, ni moins l'infini : pas de limite.",
        "{geo.tous}Quatre raisons, quatre destins.",
        "{-geo}{thm_q}Le théorème. Soit q un réel. {thm_q.1}Si q est strictement plus grand que un, q puissance n tend vers plus l'infini. "
        "{thm_q.2}Si q égale un, q puissance n vaut un, toujours. "
        "{thm_q.3}Si q est strictement compris entre moins un et un, q puissance n tend vers zéro. "
        "{thm_q.4}Et si q est inférieur ou égal à moins un, q puissance n n'a pas de limite.",
        "{-thm_q}{tag_bo3}{dem_q}Le cas q plus grand que un est une démonstration exigible. "
        "Elle utilise l'inégalité de Bernoulli, démontrée par récurrence au chapitre précédent. "
        "{dem_q.1}Soit q strictement plus grand que un. On pose a égale q moins un : a est strictement positif.",
        "{dem_q.2}D'après l'inégalité de Bernoulli, pour tout entier naturel n, q puissance n, c'est-à-dire un plus a, le tout à la puissance n, "
        "est supérieur ou égal à un, plus n fois a.",
        "{dem_q.3}Or a est strictement positif, donc un, plus n fois a, tend vers plus l'infini. "
        "{dem_q.4}Par comparaison, q puissance n tend vers plus l'infini. Deux résultats déjà démontrés, et c'est fini.",
        "{-dem_q}{-tag_bo3}{bern_ex}Un ordre de grandeur. {bern_ex.1}Un virgule zéro deux, puissance n, est supérieur ou égal à "
        "un, plus zéro virgule zéro deux fois n. {bern_ex.2}Donc il dépasse cent au plus tard à partir de n égale quatre mille neuf cent cinquante. "
        "{bern_ex.3}En réalité, c'est dès n égale deux cent trente-trois : Bernoulli minore beaucoup. "
        "Mais pour prouver une limite infinie, une minoration grossière suffit.",
        "{-bern_ex}{q01}Et quand q est entre zéro et un ? Pour comprendre : {q01.1}on pose grand Q égale un sur petit q, qui est plus grand que un. "
        "{q01.2}Alors petit q puissance n égale un, sur grand Q puissance n. Le dénominateur tend vers plus l'infini : q puissance n tend vers zéro. "
        "{q01.3}Et pour q entre moins un et zéro, on encadre q puissance n entre moins valeur absolue de q puissance n, "
        "et valeur absolue de q puissance n. Les gendarmes font le reste.",
        "{-q01}{app_q}Deux applications. {app_q.1}Au chapitre précédent, on a trouvé a indice n égale quinze, moins dix fois zéro virgule huit puissance n. "
        "Zéro virgule huit est entre zéro et un : zéro virgule huit puissance n tend vers zéro, et a indice n tend vers quinze.",
        "{app_q.2}Autre exemple : deux puissance n, plus trois puissance n, le tout sur trois puissance n. "
        "{app_q.3}On réécrit : deux tiers, puissance n, plus un. Deux tiers puissance n tend vers zéro : la limite vaut un.",
        "{-app_q}{somg}Et les sommes ? {somg.1}Pour q différent de un, un plus q, plus q au carré, jusqu'à q puissance n, "
        "égale un moins q puissance n plus un, sur un moins q. "
        "{somg.2}Si q est strictement compris entre moins un et un, q puissance n plus un tend vers zéro. "
        "{somg.3}La somme tend donc vers un, sur un moins q.",
        "{-somg}{zen2}Retour au paradoxe de Zénon. {zen2.1}Un demi, plus un quart, jusqu'à un sur deux puissance n : "
        "on factorise par un demi, et on reconnaît une somme géométrique de raison un demi. {zen2.2}Elle vaut un, moins un sur deux puissance n.",
        "{zen2.3}Et un sur deux puissance n tend vers zéro : la somme tend vers un. "
        "{zen2.4}Pour n égale dix, elle dépasse déjà zéro virgule neuf cent quatre-vingt-dix-neuf. "
        "Une infinité d'étapes, une longueur totale de un : c'est la réponse des mathématiques au paradoxe.",
        "{-zen2}",
    ], vis={
        "geo": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                    ax=dict(x=[0, 15.5], y=[-6.6, 6.6], gx=[5, 10, 15], gy=[-4, -2, 2, 4], lx="$n$"),
                    series=[dict(pts=GEO[1.2], c="ca", r=6, pas=.1, trait="pale", lab="$q=1{,}2$", lp=[12.6, 6.3],
                                 o=[["q1", 1], ["q2", .22], ["tous", 1]]),
                            dict(pts=GEO[0.8], c="vert", r=6, pas=.1, trait="pale", lab="$q=0{,}8$", lp=[2.6, 1.4],
                                 o=[["q2", 1], ["q3", .22], ["tous", 1]]),
                            dict(pts=GEO[-0.8], c="te", r=6, pas=.1, trait="pale", lab="$q=-0{,}8$", lp=[2.6, -1.3],
                                 o=[["q3", 1], ["q4", .22], ["tous", 1]]),
                            dict(pts=GEO[-1.2], c="sa", r=6, pas=.1, trait="pale", lab="$q=-1{,}2$", lp=[12.6, -5.6],
                                 o=[["q4", 1], ["tous", 1]])]),
        "thm_q": dict(type="formule", titre="Limite de $q^n$", x=150, y=120, w=980, lignes=[
            dict(f="$q>1$ : $\\lim q^n=+\\infty$", taille=42),
            dict(f="$q=1$ : $q^n=1$ pour tout $n$", taille=42),
            dict(f="$-1<q<1$ : $\\lim q^n=0$", taille=42),
            dict(f="$q\\leq-1$ : $(q^n)$ n'a pas de limite", taille=42)]),
        "tag_bo3": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=660, y=34, w=560),
        "dem_q": dict(type="formule", copie=True, titre="Démonstration exigible : $q>1$", x=90, y=110, w=1100, lignes=[
            dict(f="Soit $q>1$. On pose $a=q-1>0$.", taille=34),
            dict(f="Bernoulli : pour tout $n\\in\\N$, $q^n=(1+a)^n\\geq1+na$.", m="chapitre 1", taille=34),
            dict(f="$a>0$, donc $\\lim(1+na)=+\\infty$.", taille=34),
            dict(f="Par comparaison, $\\lim q^n=+\\infty$.", cadre=True, taille=34)]),
        "bern_ex": dict(type="formule", titre="Un ordre de grandeur", x=150, y=150, w=980, lignes=[
            dict(f="$1{,}02^n\\geq1+0{,}02\\,n$"),
            dict(f="$1+0{,}02\\,n\\geq100\\iff n\\geq4950$", n="donc $1{,}02^n\\geq100$ au plus tard dès $n=4950$"),
            dict(f="en fait dès $n=233$ : Bernoulli minore beaucoup", txt=True)]),
        "q01": dict(type="formule", titre="Pour comprendre : $-1<q<1$", x=150, y=140, w=980, lignes=[
            dict(f="$0<q<1$ : $Q=\\dfrac1q>1$"),
            dict(f="$q^n=\\dfrac1{Q^n}\\to0$ car $Q^n\\to+\\infty$", ind=True),
            dict(f="$-1<q<0$ : $-|q|^n\\leq q^n\\leq|q|^n$, gendarmes", taille=38)]),
        "app_q": dict(type="formule", titre="Deux applications", x=150, y=140, w=980, lignes=[
            dict(f="$a_n=15-10\\times0{,}8^n$ : $0{,}8^n\\to0$ donc $a_n\\to15$", taille=38),
            dict(f="$\\dfrac{2^n+3^n}{3^n}$", taille=38),
            dict(f="$=\\left(\\dfrac23\\right)^n+1\\to1$", ind=True, cadre=True, taille=38)]),
        "somg": dict(type="formule", titre="Somme des termes", x=150, y=150, w=980, lignes=[
            dict(f="$q\\neq1$ : $1+q+\\cdots+q^n=\\dfrac{1-q^{n+1}}{1-q}$", taille=40),
            dict(f="si $-1<q<1$ : $q^{n+1}\\to0$", ind=True),
            dict(f="$\\lim\\left(1+q+\\cdots+q^n\\right)=\\dfrac1{1-q}$", cadre=True, taille=40)]),
        "zen2": dict(type="formule", titre="Le paradoxe de Zénon", x=120, y=120, w=1040, lignes=[
            dict(f="$\\frac12+\\frac14+\\cdots+\\frac1{2^n}=\\frac12\\times\\dfrac{1-\\left(\\frac12\\right)^n}{1-\\frac12}$", taille=36),
            dict(f="$=1-\\dfrac1{2^n}$", ind=True, taille=36),
            dict(f="$\\lim\\left(\\frac12+\\cdots+\\frac1{2^n}\\right)=1$", cadre=True, taille=38),
            dict(f="$n=10$ : $0{,}9990234375$", ok=True, taille=34)]),
    }),

    # ================================================================ VI. suites monotones
    dict(id="monotones", chap="Suites monotones : le théorème de convergence", fond="carnet", humeur="calme",
         retenir="Croissante et majorée : converge. Décroissante et minorée : converge. Croissante non majorée : $+\\infty$. "
                 "Un majorant n'est pas la limite.",
         beats=[
        "{q6}Parfois, on ne sait pas calculer la limite. Peut-on quand même savoir qu'elle existe ?",
        "{-q6}{thm_m}Oui : c'est le {!théorème de convergence monotone}théorème de convergence monotone. Il est admis. "
        "{thm_m.1}Toute suite croissante et majorée converge. {thm_m.2}Et toute suite décroissante et minorée converge.",
        "{-thm_m}{monte}{monte.s1}Prends u indice n égale un, moins un sur n plus un. Zéro, un demi, deux tiers, trois quarts… "
        "Elle est croissante. {monte.s2}Et elle est majorée : par cinq, par exemple. Aucun terme ne dépasse cinq. "
        "D'après le théorème, elle converge.",
        "{monte.l}Mais vers quoi ? Vers un. Pas vers cinq.",
        "{-monte}{exist}C'est un {!théorème d'existence}théorème d'existence. {exist.1}Il dit que la limite existe, pas ce qu'elle vaut. "
        "{exist.2}Si la suite est croissante et majorée par M, sa limite l est inférieure ou égale à M. "
        "{exist.3}Mais elle peut être strictement plus petite. Un majorant n'est pas la limite !",
        "{-exist}{bilan_m}Avec le théorème du début du chapitre, on a un bilan complet pour une suite croissante. "
        "{bilan_m.1}Majorée : elle converge, vers une limite finie. {bilan_m.2}Non majorée : elle tend vers plus l'infini. "
        "{bilan_m.3}Dans tous les cas, une suite croissante a une limite.",
        "{-bilan_m}{p_born}Et un piège classique. {p_born.1}« La suite est bornée, donc elle converge. » C'est faux. "
        "{p_born.2}Moins un puissance n est bornée, entre moins un et un. Et elle diverge. "
        "{p_born.3}Il faut la monotonie, et la borne du bon côté : majorée si elle croît, minorée si elle décroît.",
        "{-p_born}",
    ], vis={
        "q6": dict(type="question", t="Peut-on savoir qu'une limite existe, sans la calculer ?"),
        "thm_m": dict(type="formule", titre="Théorème de convergence monotone (admis)", x=150, y=170, w=980, lignes=[
            dict(f="Toute suite croissante et majorée converge.", cadre=True, taille=42),
            dict(f="Toute suite décroissante et minorée converge.", cadre=True, taille=42)]),
        "monte": dict(type="illu", nom="nuage", x=170, y=96, w=940, h=590,
                      ax=dict(x=[0, 21], y=[0, 5.6], gx=[5, 10, 15, 20], gy=[1, 2, 3, 4, 5], lx="$n$"),
                      series=[dict(pts=MONTE, c="te", r=6, pas=.09, lab="$u_n=1-\\frac1{n+1}$", lp=[14.5, 1.55]),
                              dict(pts=[[0, 5], [21, 5]], c="ca", trait=True, points=False, ep=3.2, lab="majorant $5$", lp=[16.5, 5.45],
                                   o=[["s2", 1]])],
                      ligne=dict(y=1, lab="$\\ell=1$")),
        "exist": dict(type="liste", titre="Un théorème d'existence", items=[
            "Il dit que la limite existe, pas ce qu'elle vaut",
            "Croissante et majorée par $M$ : $\\ell\\leq M$",
            "$\\ell$ peut être strictement plus petite que $M$ : majorant $\\neq$ limite"], marques=["·", "·", "!"], x=150, y=170, w=980),
        "bilan_m": dict(type="formule", titre="Une suite croissante…", x=150, y=170, w=980, lignes=[
            dict(f="majorée : elle converge", ok=True, taille=42),
            dict(f="non majorée : elle tend vers $+\\infty$", ok=True, taille=42),
            dict(f="dans tous les cas, elle a une limite", cadre=True, taille=42)]),
        "p_born": dict(type="liste", titre="Piège : « bornée donc convergente »", items=[
            "« Bornée, donc convergente » : faux", "$(-1)^n$ est bornée et diverge",
            "Il faut monotone, et bornée du bon côté"], marques=["✗", "✗", "!"], x=150, y=170, w=980),
    }),

    # ================================================================ VII. u(n+1) = f(u(n))
    dict(id="recurrentes", chap="Suites définies par récurrence : la méthode complète", fond="ardoise", humeur="mystere",
         retenir="1. Par récurrence : $a\\leq u_n\\leq u_{n+1}\\leq b$. 2. Monotone et bornée : elle converge vers $\\ell$. "
                 "3. $f$ continue : $f(\\ell)=\\ell$, et on garde la solution compatible avec l'encadrement.",
         beats=[
        "{meth}Voici le grand classique du bac : une suite définie par u indice n plus un égale f de u indice n. La méthode tient en trois temps. "
        "{meth.1}Un : par récurrence, on encadre. Par exemple, a inférieur ou égal à u indice n, inférieur ou égal à u indice n plus un, inférieur ou égal à b.",
        "{meth.2}Deux : la suite est croissante et majorée, donc elle converge vers un réel l. "
        "{meth.3}Trois : si f est continue, on passe à la limite dans la relation de récurrence. On obtient f de l égale l. "
        "On résout, et on garde la solution compatible avec l'encadrement.",
        "{-meth}{pf}Pourquoi f de l égale l ? {pf.1}Quand n tend vers plus l'infini, u indice n plus un tend vers l : c'est la même suite, décalée d'un rang. "
        "{pf.2}Et si f est continue en l, f de u indice n tend vers f de l. "
        "{pf.3}Or u indice n plus un et f de u indice n, c'est la même suite. Sa limite est unique : donc f de l égale l. "
        "{pf.4}Le lien entre continuité et suites sera étudié au chapitre quatre.",
        "{-pf}{ex7}L'exemple du chapitre précédent. {ex7.1}u zéro égale un, et u indice n plus un égale la racine de la somme, u indice n plus deux. "
        "On a démontré, par récurrence, que zéro est inférieur ou égal à u indice n, inférieur ou égal à u indice n plus un, inférieur ou égal à deux. "
        "{ex7.2}La suite est croissante, et majorée par deux : elle converge vers un réel l, compris entre zéro et deux.",
        "{-ex7}{toile}{toile.1}{toile.2}La toile d'araignée le montre. {toile.3}Les termes montent en escalier, et se tassent vers le point "
        "où la courbe croise la droite y égale x. {toile.4}C'est là que f de l égale l.",
        "{-toile}{res7}Calculons. {res7.1}La fonction f, racine carrée de la somme x plus deux, est continue sur l'intervalle de moins deux à plus l'infini. "
        "Donc l égale la racine de la somme, l plus deux. {res7.2}On élève au carré : l au carré égale l plus deux.",
        "{res7.3}Soit l au carré, moins l, moins deux, égale zéro. On factorise : l moins deux, fois l plus un, égale zéro. "
        "{res7.4}Deux solutions : deux, et moins un. Or l est compris entre zéro et deux : on élimine moins un. La limite vaut deux.",
        "{-res7}{p7}Trois réflexes. {p7.1}Écrire la phrase sur la continuité : « f est continue sur cet intervalle, car c'est une fonction racine, "
        "un polynôme, ou un quotient ». Sans elle, f de l égale l n'est pas justifié.",
        "{p7.2}Ne pas prendre une solution au hasard : l'équation en a souvent deux, et c'est l'encadrement qui choisit.",
        "{p7.3}Et quand l'énoncé introduit une suite auxiliaire, par exemple v indice n égale u indice n moins l, et qu'elle est géométrique de raison q, "
        "avec q strictement compris entre moins un et un, alors v tend vers zéro, et u tend vers l. "
        "C'est souvent plus rapide, et ça donne en plus la vitesse de convergence.",
        "{-p7}",
    ], vis={
        "meth": dict(type="formule", titre="La méthode en trois temps", x=110, y=120, w=1060, lignes=[
            dict(lab="1.", f="par récurrence : $a\\leq u_n\\leq u_{n+1}\\leq b$", taille=38),
            dict(lab="2.", f="croissante et majorée : $(u_n)$ converge vers un réel $\\ell$", taille=38),
            dict(lab="3.", f="$f$ continue : $f(\\ell)=\\ell$ ; on résout, on garde la bonne solution", cadre=True, taille=36)]),
        "pf": dict(type="formule", titre="Pourquoi $f(\\ell)=\\ell$ ?", x=150, y=130, w=980, lignes=[
            dict(f="$u_{n+1}\\to\\ell$ : la même suite, décalée d'un rang"),
            dict(f="$f$ continue en $\\ell$ : $f(u_n)\\to f(\\ell)$"),
            dict(f="$u_{n+1}=f(u_n)$ et la limite est unique : $f(\\ell)=\\ell$", cadre=True, taille=38),
            dict(f="continuité et suites : au chapitre 4", txt=True)]),
        "ex7": dict(type="formule", titre="Exemple", x=150, y=150, w=980, lignes=[
            dict(f="$u_0=1$ et $u_{n+1}=\\sqrt{u_n+2}$ : $0\\leq u_n\\leq u_{n+1}\\leq2$", taille=38, n="démontré par récurrence au chapitre 1"),
            dict(f="croissante et majorée par $2$ : elle converge vers $\\ell\\in[0;2]$", cadre=True, taille=36)]),
        "toile": dict(type="graphe", titre="La toile d'araignée de $u_{n+1}=\\sqrt{u_n+2}$", x=310, y=110, w=660, h=540,
                      ax=dict(x=[0, 2.4], y=[0, 2.4], gx=[0.5, 1, 1.5, 2], gy=[0.5, 1, 1.5, 2], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=RAC, c="te", ep=3.4, lbl="$y=\\sqrt{x+2}$", lp=[0.55, 1.95]),
                          dict(type="droite", pts=[[0, 0], [2.4, 2.4]], c="iv2", ep=2.2, lbl="$y=x$", lp=[0.62, 0.32]),
                          dict(type="toile", u=U_RAC, c="sa", nlab=2, dur=4.5),
                          dict(type="point", x=2, y=2, c="ca", r=9, lbl="$\\ell=2$", lp=[2.12, 1.86])]),
        "res7": dict(type="formule", copie=True, titre="Calcul de la limite", x=100, y=110, w=1080, lignes=[
            dict(f="$f(x)=\\sqrt{x+2}$ est continue sur $[-2;+\\infty[$, donc $\\ell=\\sqrt{\\ell+2}$", taille=34),
            dict(f="$\\ell^2=\\ell+2$", ind=True, taille=34),
            dict(f="$\\ell^2-\\ell-2=0$, soit $(\\ell-2)(\\ell+1)=0$", ind=True, taille=34),
            dict(f="$\\ell=2$ ou $\\ell=-1$ ; or $\\ell\\in[0;2]$ : $\\ell=2$", ind=True, cadre=True, taille=34)]),
        "p7": dict(type="liste", titre="Trois réflexes", items=[
            "Écrire la phrase : « $f$ est continue sur $I$ »",
            "Choisir la solution grâce à l'encadrement",
            "Suite auxiliaire $v_n=u_n-\\ell$ géométrique, $|q|<1$ : $u_n\\to\\ell$"], x=150, y=170, w=980),
    }),

    # ================================================================ VIII. algorithmes
    dict(id="algos", chap="Algorithmes : seuils et valeurs approchées", fond="carnet", humeur="calme",
         retenir="Algorithme de seuil : tant que la condition d'arrêt n'est pas atteinte, on passe au rang suivant. "
                 "La suite doit être monotone pour que le seuil soit définitif.",
         beats=[
        "{seuil}Une question classique : à partir de quel rang ? Prends u indice n égale zéro virgule neuf, puissance n. Elle tend vers zéro. "
        "À partir de quel rang devient-elle plus petite que zéro virgule zéro un ?",
        "{seuil.l2}On part de n égale zéro, et u égale un. {seuil.l4}{seuil.r1}Tant que u est supérieur ou égal à e, la précision visée, "
        "{seuil.l5}on passe au rang suivant, {seuil.l6}{seuil.r2}et on multiplie u par zéro virgule neuf. "
        "{seuil.l7}Quand la boucle s'arrête, on renvoie n. {seuil.s}Résultat : quarante-quatre.",
        "{-seuil}{v_seuil}Vérifions. {v_seuil.1}Zéro virgule neuf puissance quarante-trois vaut environ zéro virgule zéro cent huit : encore au-dessus. "
        "{v_seuil.2}Puissance quarante-quatre : environ zéro virgule zéro zéro quatre-vingt-dix-sept. En dessous.",
        "{v_seuil.3}Et la suite est décroissante : tous les termes suivants restent en dessous. "
        "Sans la monotonie, le premier rang trouvé ne garantirait pas « à partir de ce rang ».",
        "{-v_seuil}{heron}Les suites servent aussi à calculer des valeurs approchées. La méthode de Héron : u zéro égale un, "
        "et u indice n plus un égale la moitié de la somme : u indice n, plus deux sur u indice n. Elle converge vers racine de deux. Et à toute vitesse : "
        "le nombre de décimales exactes double environ à chaque étape.",
        "{heron.s}Dès la cinquième étape, Python affiche racine de deux à la précision de la machine : quinze décimales exactes. "
        "L'étude de cette convergence, elle, est un approfondissement : pour aller plus loin.",
        "Le même principe donne des valeurs approchées du nombre e, ou du nombre d'or.",
        "{-heron}",
    ], vis={
        "seuil": dict(type="code", titre="Python · l'algorithme de seuil", x=190, y=96, w=900, taille=30, lignes=[
            "def seuil(e):", "    n = 0", "    u = 1                 # u0 = 0,9^0", "    while @1:", "        n = n + 1",
            "        u = @2", "    return n", "", "print(seuil(0.01))"], rep=["u >= e", "0.9 * u"], sortie="44"),
        "v_seuil": dict(type="formule", titre="Vérification", x=150, y=150, w=980, lignes=[
            dict(f="$0{,}9^{43}\\approx0{,}0108>0{,}01$", taille=42),
            dict(f="$0{,}9^{44}\\approx0{,}0097<0{,}01$", taille=42, ok=True),
            dict(f="suite décroissante : le seuil est définitif", cadre=True, taille=38)]),
        "heron": dict(type="code", titre="Python · la méthode de Héron", x=190, y=96, w=900, taille=28, lignes=[
            "u = 1.0", "for k in range(5):", "    u = (u + 2 / u) / 2", "    print(k + 1, u)"],
            sortie="1 1.5\n2 1.4166666666666665\n3 1.4142156862745097\n4 1.4142135623746899\n5 1.414213562373095"),
    }),

    # ================================================================ IX. pièges
    dict(id="pieges", chap="Les pièges classiques", fond="craie", humeur="tension",
         retenir="Forme indéterminée : transformer. Gendarmes : même limite. Bornée ne suffit pas. $q\\leq-1$ : pas de limite. "
                 "Écrire la continuité de $f$, et choisir la bonne solution.",
         beats=[
        "{pieges}Faisons le tour des pièges. {pieges.1}Écrire « infini moins infini égale zéro ». C'est une forme indéterminée : "
        "n au carré moins n tend vers plus l'infini. On transforme l'écriture.",
        "{pieges.2}Des gendarmes qui n'ont pas la même limite. Alors le théorème ne dit rien.",
        "{pieges.3}« Bornée, donc convergente. » Moins un puissance n est bornée, et diverge. Il faut aussi la monotonie.",
        "{pieges.4}q puissance n avec q négatif. Moins zéro virgule cinq, puissance n, tend vers zéro. "
        "Mais moins deux, puissance n, n'a pas de limite : ni plus l'infini, ni moins l'infini. Les termes changent de signe.",
        "{pieges.5}Oublier la continuité de f. Pour écrire f de l égale l, il faut que f soit continue. Une phrase suffit, mais elle est attendue.",
        "{pieges.6}Et prendre une solution de f de l égale l au hasard. L'équation en a souvent deux : on élimine celle qui sort de l'encadrement.",
        "{-pieges}",
    ], vis={
        "pieges": dict(type="liste", titre="Les pièges classiques", items=[
            "« $\\infty-\\infty=0$ », « $\\frac\\infty\\infty=1$ »", "Des gendarmes de limites différentes",
            "« Bornée, donc convergente »", "$(-2)^n$ : pas de limite (mais $(-0{,}5)^n\\to0$)",
            "Oublier la continuité de $f$", "Une solution de $f(\\ell)=\\ell$ au hasard"],
            marques=["!"] * 6, x=150, y=96, w=980),
    }),

    # ================================================================ X. exercice 1
    dict(id="exo1", chap="Exercice 1 · cinq limites à calculer", fond="ardoise", humeur="tension", beats=[
        "{ex1}Place à l'entraînement. Premier exercice : détermine la limite de chacune de ces cinq suites. "
        "a indice n égale n au cube, moins deux n, sur quatre n au cube, plus n au carré. b indice n égale deux n plus un, sur n au carré plus un. "
        "c indice n égale trois fois zéro virgule sept puissance n, moins cinq. d indice n égale deux puissance n, moins trois puissance n. "
        "Et e indice n égale cinq, moins moins un puissance n, le tout sur n, pour n supérieur ou égal à un.",
        "{-ex1}{pa1}À toi. Mets la vidéo sur pause. Pour chacune : repère la forme, puis choisis l'outil.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}a indice n : forme infini sur infini. On factorise par n au cube, en haut et en bas. "
        "{s11.2}Il reste un, moins deux sur n au carré ; sur quatre, plus un sur n. {s11.3}La limite vaut un quart.",
        "{-s11}{ex1c.q2}{s12}{s12.1}b indice n : forme infini sur infini. En haut, on factorise par n, en bas par n au carré. "
        "{s12.2}Après simplification, il reste deux plus un sur n, sur n fois un plus un sur n au carré. "
        "{s12.3}Le numérateur tend vers deux, le dénominateur vers plus l'infini : la limite vaut zéro.",
        "{-s12}{ex1c.q3}{s13}{s13.1}c indice n : zéro virgule sept est entre zéro et un, donc zéro virgule sept puissance n tend vers zéro. "
        "{s13.2}La limite vaut moins cinq.",
        "{-s13}{ex1c.q4}{s14}{s14.1}d indice n : forme infini moins infini. On factorise par le terme prépondérant, trois puissance n. "
        "{s14.2}Il reste trois puissance n, fois deux tiers puissance n, moins un. "
        "{s14.3}Trois puissance n tend vers plus l'infini, et la parenthèse vers moins un. La limite vaut moins l'infini.",
        "{-s14}{ex1c.q5}{s15}{s15.1}e indice n : moins un puissance n vaut un ou moins un, donc le numérateur est compris entre quatre et six. "
        "{s15.2}On divise par n, strictement positif : quatre sur n, inférieur ou égal à e indice n, inférieur ou égal à six sur n. "
        "{s15.3}Les deux gendarmes tendent vers zéro : la limite vaut zéro.",
        "{-s15}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", etiquette="Exercice 1 · pour démarrer", titre="Cinq limites à calculer",
                    enonce=["Déterminer la limite de chaque suite."],
                    questions=["$a_n=\\dfrac{n^3-2n}{4n^3+n^2}$", "$b_n=\\dfrac{2n+1}{n^2+1}$", "$c_n=3\\times0{,}7^n-5$",
                               "$d_n=2^n-3^n$", "$e_n=\\dfrac{5-(-1)^n}{n}$ pour $n\\geq1$"]),
        "pa1": dict(type="pause", t="Pour chaque suite : la forme, puis l'outil (terme prépondérant, $q^n$, gendarmes)."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", etiquette="Exercice 1", titre="Cinq limites",
                     questions=["$a_n=\\frac{n^3-2n}{4n^3+n^2}$", "$b_n=\\frac{2n+1}{n^2+1}$", "$c_n=3\\times0{,}7^n-5$",
                                "$d_n=2^n-3^n$", "$e_n=\\frac{5-(-1)^n}{n}$"]),
        "s11": dict(type="formule", titre="$a_n$", x=550, y=150, w=690, lignes=[
            dict(f="forme $\\frac\\infty\\infty$ : on factorise par $n^3$", txt=True),
            dict(f="$a_n=\\dfrac{1-\\frac2{n^2}}{4+\\frac1n}$", taille=42),
            dict(f="$\\lim a_n=\\dfrac14$", cadre=True, taille=42)]),
        "s12": dict(type="formule", titre="$b_n$", x=550, y=130, w=690, lignes=[
            dict(f="$b_n=\\dfrac{n\\left(2+\\frac1n\\right)}{n^2\\left(1+\\frac1{n^2}\\right)}$", taille=36),
            dict(f="$b_n=\\dfrac{2+\\frac1n}{n\\left(1+\\frac1{n^2}\\right)}$", taille=36),
            dict(f="numérateur $\\to2$, dénominateur $\\to+\\infty$ : $\\lim b_n=0$", cadre=True, taille=30)]),
        "s13": dict(type="formule", titre="$c_n$", x=550, y=190, w=690, lignes=[
            dict(f="$0<0{,}7<1$ donc $0{,}7^n\\to0$", taille=40),
            dict(f="$\\lim c_n=-5$", cadre=True, taille=42)]),
        "s14": dict(type="formule", titre="$d_n$", x=550, y=150, w=690, lignes=[
            dict(f="forme $\\infty-\\infty$ : on factorise par $3^n$", txt=True),
            dict(f="$d_n=3^n\\left(\\left(\\frac23\\right)^n-1\\right)$", taille=40),
            dict(f="$3^n\\to+\\infty$, parenthèse $\\to-1$ : $\\lim d_n=-\\infty$", cadre=True, taille=32)]),
        "s15": dict(type="formule", titre="$e_n$", x=550, y=150, w=690, lignes=[
            dict(f="$4\\leq5-(-1)^n\\leq6$", taille=40),
            dict(f="$\\dfrac4n\\leq e_n\\leq\\dfrac6n$", taille=40, m="$n>0$"),
            dict(f="gendarmes : $\\lim e_n=0$", cadre=True, taille=40)]),
    }),

    # ================================================================ XI. exercice 2 (type bac)
    dict(id="exo2", chap="Exercice 2 · type bac", fond="carnet", humeur="tension", beats=[
        "{ex2}Deuxième exercice, au format du bac. La suite u est définie par u zéro égale zéro, et u indice n plus un égale "
        "deux u indice n, plus trois, sur u indice n plus quatre. On note f de x égale deux x plus trois, sur x plus quatre, définie sur l'intervalle de zéro à plus l'infini.",
        "{-ex2}{ex2b}Cinq questions. {ex2b.1}Un : calcule u indice un et u indice deux. "
        "{ex2b.2}Deux : étudie les variations de f, puis démontre par récurrence que zéro est inférieur ou égal à u indice n, inférieur ou égal à u indice n plus un, inférieur ou égal à un. "
        "{ex2b.3}Trois : déduis-en que la suite converge, et détermine sa limite. "
        "{ex2b.4}Quatre : on pose v indice n égale u indice n moins un, sur u indice n plus trois. Montre que v est géométrique de raison un cinquième, et retrouve la limite. "
        "{ex2b.5}Cinq : écris un programme Python qui renvoie le plus petit n tel que un moins u indice n est plus petit que dix puissance moins six.",
        "{-ex2b}{pa2}C'est un vrai sujet de bac. Prends le temps : mets sur pause, et rédige tout.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un. u indice un égale trois sur quatre : trois quarts. "
        "{s21.2}u indice deux : deux fois trois quarts, plus trois, ça fait quatre virgule cinq. Divisé par trois quarts plus quatre, quatre virgule soixante-quinze. "
        "{s21.3}C'est dix-huit dix-neuvièmes, environ zéro virgule neuf cent quarante-sept.",
        "{-s21}{ex2c.q2}{s22}Question deux. {s22.1}On dérive le quotient. f prime de x égale deux fois la parenthèse x plus quatre, moins la parenthèse deux x plus trois, "
        "le tout sur x plus quatre, au carré. Il reste cinq, sur x plus quatre, au carré. C'est strictement positif : f est croissante.",
        "{s22.2}Initialisation : u zéro égale zéro, u indice un égale trois quarts, et zéro, inférieur ou égal à zéro, inférieur ou égal à trois quarts, inférieur ou égal à un. Vrai.",
        "{s22.3}Hérédité : soit k un entier naturel tel que zéro inférieur ou égal à u indice k, inférieur ou égal à u indice k plus un, inférieur ou égal à un. "
        "{s22.4}f est croissante sur l'intervalle de zéro à plus l'infini : on lui applique toute la chaîne. "
        "{s22.5}Or f de zéro vaut trois quarts, et f de un vaut cinq cinquièmes, c'est-à-dire un. "
        "On obtient : trois quarts, inférieur ou égal à u indice k plus un, inférieur ou égal à u indice k plus deux, inférieur ou égal à un.",
        "{s22.6}Et comme zéro est inférieur à trois quarts, c'est la propriété au rang k plus un. "
        "{s22.7}Conclusion : par récurrence, l'encadrement est vrai pour tout entier naturel n.",
        "{-s22}{ex2c.q3}{s23}Question trois. {s23.1}La suite est croissante et majorée par un : elle converge vers un réel l, compris entre zéro et un. "
        "{s23.2}f est continue sur l'intervalle de zéro à plus l'infini : c'est un quotient de polynômes, dont le dénominateur ne s'annule pas. Donc f de l égale l.",
        "{s23.3}Deux l plus trois égale l au carré plus quatre l. Soit l au carré, plus deux l, moins trois, égale zéro. "
        "{s23.4}On factorise : l moins un, fois l plus trois. Les solutions : un, et moins trois. "
        "{s23.5}Comme l est positif, la limite vaut un.",
        "{-s23}{ex2c.q4}{s24}Question quatre. {s24.1}v indice n plus un égale u indice n plus un, moins un, sur u indice n plus un, plus trois. "
        "On remplace u indice n plus un par son expression, et on multiplie en haut et en bas par u indice n plus quatre.",
        "{s24.2}En haut : deux u indice n plus trois, moins u indice n moins quatre : il reste u indice n moins un. "
        "En bas : deux u indice n plus trois, plus trois u indice n plus douze : cinq u indice n plus quinze. "
        "{s24.3}C'est cinq fois u indice n plus trois. Donc v indice n plus un égale un cinquième de v indice n.",
        "{s24.4}La suite v est géométrique, de raison un cinquième, et de premier terme v zéro égale moins un tiers. "
        "Donc v indice n égale moins un tiers, fois un cinquième puissance n. {s24.5}Un cinquième est entre zéro et un : v tend vers zéro. "
        "{s24.6}Enfin, on exprime u en fonction de v : u indice n égale un plus trois v indice n, sur un moins v indice n. Ça tend vers un sur un : on retrouve un.",
        "{-s24}{ex2c.q5}{py2}Question cinq. Voici le programme. {py2.l4}On veut le premier rang où un moins u devient plus petit que dix puissance moins six. "
        "Donc on continue tant que un moins u est supérieur ou égal à dix puissance moins six : {py2.r1}c'est la condition. "
        "{py2.l5}Et à chaque tour, {py2.r2}u prend la valeur f de u, {py2.l6}et n augmente de un.",
        "{py2.s}Le programme renvoie neuf. L'écart à un est divisé par environ cinq à chaque étape : c'est la vitesse que donne la suite auxiliaire.",
        "{-py2}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Une suite homographique",
                    enonce=["Soit $(u_n)$ définie par $u_0=0$ et, pour tout $n\\in\\N$, $u_{n+1}=\\dfrac{2u_n+3}{u_n+4}$.",
                            "On note $f(x)=\\dfrac{2x+3}{x+4}$ sur $[0;+\\infty[$."]),
        "ex2b": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Une suite homographique · questions",
                     questions=["Calculer $u_1$ et $u_2$.",
                                "Étudier les variations de $f$. Montrer par récurrence que $0\\leq u_n\\leq u_{n+1}\\leq1$.",
                                "En déduire que $(u_n)$ converge et déterminer sa limite.",
                                "On pose $v_n=\\dfrac{u_n-1}{u_n+3}$. Montrer que $(v_n)$ est géométrique de raison $\\frac15$ ; retrouver la limite.",
                                "Écrire un programme qui renvoie le plus petit $n$ tel que $1-u_n<10^{-6}$."]),
        "pa2": dict(type="pause", t="$u_1$, $u_2$, la récurrence, la limite par $f(\\ell)=\\ell$, la suite auxiliaire, le seuil."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", etiquette="Exercice 2 · type bac", titre="Suite homographique",
                     donnees=["$u_0=0$", "$u_{n+1}=\\frac{2u_n+3}{u_n+4}$"],
                     questions=["$u_1$, $u_2$ ?", "$0\\leq u_n\\leq u_{n+1}\\leq1$ ?", "La limite ?", "$v_n=\\frac{u_n-1}{u_n+3}$ ?", "Le seuil $10^{-6}$ ?"]),
        "s21": dict(type="formule", titre="1 · Les premiers termes", x=550, y=150, w=690, lignes=[
            dict(f="$u_1=\\dfrac{3}{4}$", taille=40),
            dict(f="$u_2=\\dfrac{2\\times\\frac34+3}{\\frac34+4}=\\dfrac{4{,}5}{4{,}75}$", taille=38),
            dict(f="$u_2=\\dfrac{18}{19}\\approx0{,}947$", cadre=True, taille=40)]),
        "s22": dict(type="formule", copie=True, titre="2 · Variations et récurrence", x=530, y=76, w=720, lignes=[
            dict(f="$f'(x)=\\dfrac{2(x+4)-(2x+3)}{(x+4)^2}=\\dfrac{5}{(x+4)^2}>0$", taille=26),
            dict(lab="Initialisation.", f="$0\\leq0\\leq\\frac34\\leq1$.", taille=27),
            dict(lab="Hérédité.", f="Soit $k$ tel que $0\\leq u_k\\leq u_{k+1}\\leq1$.", taille=27),
            dict(f="$f$ croissante : $f(0)\\leq f(u_k)\\leq f(u_{k+1})\\leq f(1)$", ind=True, taille=26),
            dict(f="$\\frac34\\leq u_{k+1}\\leq u_{k+2}\\leq1$", ind=True, m="$f(1)=\\frac55=1$", taille=27),
            dict(f="et $0\\leq\\frac34$ : c'est $P(k+1)$.", ind=True, cadre=True, taille=27),
            dict(lab="Conclusion.", f="pour tout $n$, $0\\leq u_n\\leq u_{n+1}\\leq1$.", taille=27)]),
        "s23": dict(type="formule", titre="3 · La limite", x=550, y=110, w=690, lignes=[
            dict(f="croissante, majorée par $1$ : converge vers $\\ell\\in[0;1]$", taille=28),
            dict(f="$f$ continue sur $[0;+\\infty[$ : $f(\\ell)=\\ell$", taille=30),
            dict(f="$2\\ell+3=\\ell^2+4\\ell\\iff\\ell^2+2\\ell-3=0$", taille=30),
            dict(f="$(\\ell-1)(\\ell+3)=0$", ind=True, taille=32),
            dict(f="$\\ell\\geq0$ : $\\ell=1$", cadre=True, taille=34)]),
        "s24": dict(type="formule", titre="4 · La suite auxiliaire", x=540, y=80, w=710, lignes=[
            dict(f="$v_{n+1}=\\dfrac{u_{n+1}-1}{u_{n+1}+3}=\\dfrac{(2u_n+3)-(u_n+4)}{(2u_n+3)+3(u_n+4)}$", taille=25),
            dict(f="$v_{n+1}=\\dfrac{u_n-1}{5u_n+15}$", ind=True, taille=28),
            dict(f="$v_{n+1}=\\dfrac15\\,v_n$", ind=True, cadre=True, taille=30),
            dict(f="$v_0=-\\frac13$, donc $v_n=-\\frac13\\left(\\frac15\\right)^n$", taille=28),
            dict(f="$0<\\frac15<1$ : $v_n\\to0$", taille=28),
            dict(f="$u_n=\\dfrac{1+3v_n}{1-v_n}\\to1$", cadre=True, taille=30)]),
        "py2": dict(type="code", titre="Python · le seuil", x=560, y=120, w=660, taille=27, lignes=[
            "def seuil():", "    n = 0", "    u = 0", "    while @1:", "        u = @2", "        n = n + 1", "    return n", "",
            "print(seuil())"], rep=["1 - u >= 1e-6", "(2*u + 3) / (u + 4)"], sortie="9"),
    }),

    # ================================================================ XII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="craie", humeur="lumiere", beats=[
        "{carte}Récapitulons. Au centre, la limite d'une suite. "
        "{carte.1}Les définitions : tendre vers plus l'infini, avec un seuil A ; converger vers l, avec une bande autour de l. "
        "{carte.2}Pour calculer : les opérations, les quatre formes indéterminées, le terme prépondérant et la quantité conjuguée. "
        "{carte.3}Pour comparer : la comparaison, et les gendarmes. "
        "{carte.4}Et les grands théorèmes : la limite de q puissance n, la convergence monotone, et f de l égale l.",
        "{-carte}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Calculer une limite, en levant une forme indéterminée. "
        "{bac.2}Utiliser la comparaison ou les gendarmes. {bac.3}Donner la limite de q puissance n, et refaire la démonstration avec Bernoulli. "
        "{bac.4}Refaire les deux autres démonstrations exigibles : croissante non majorée, et comparaison. "
        "{bac.5}Mener l'étude complète d'une suite définie par u indice n plus un égale f de u indice n. {bac.6}Et écrire un algorithme de seuil.",
        "Si tu sais faire ces six choses, ce chapitre est à toi. Les fiches, les QCM et les animations du chapitre t'attendent sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, un quiz sur cette vidéo est là aussi.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="LIMITE D'UNE SUITE · $n\\to+\\infty$", branches=[
            dict(t="Définitions", items=["$+\\infty$ : un seuil $A$", "$\\ell$ : une bande autour de $\\ell$", "divergente : pas de limite finie"]),
            dict(t="Calculer", items=["opérations", "4 formes indéterminées", "terme prépondérant, conjuguée"]),
            dict(t="Comparer", items=["$u_n\\geq v_n\\to+\\infty$", "gendarmes : même limite", "$<$ devient $\\leq$"]),
            dict(t="Théorèmes", items=["$q^n$ selon $q$", "monotone et bornée", "$f(\\ell)=\\ell$, $f$ continue"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Lever une forme indéterminée", "Comparaison, gendarmes", "$q^n$, et la démonstration par Bernoulli",
            "Les deux autres démonstrations exigibles", "Étudier $u_{n+1}=f(u_n)$ de bout en bout", "Écrire un algorithme de seuil"],
            marques=["✓"] * 6, x=170, y=96, w=940),
    }),
]

QUIZ = [
    dict(q="La suite (uₙ) converge vers ℓ signifie…",
         r=["les termes se rapprochent de ℓ", "tout intervalle ouvert contenant ℓ contient tous les termes à partir d'un certain rang",
            "tout intervalle ouvert contenant ℓ contient une infinité de termes"],
         ok=1, ex="C'est la définition. « Se rapprocher » ne suffit pas (1 + 1/n se rapproche de 0, sa limite est 1), ni « une infinité de termes » ((−1)ⁿ).",
         voir="def_cv"),
    dict(q="Laquelle de ces formes est indéterminée ?", r=["+∞ + (+∞)", "0 × ∞", "2 × (−∞)"],
         ok=1, ex="Les quatre formes indéterminées : ∞ − ∞, 0 × ∞, ∞/∞, 0/0.", voir="fi"),
    dict(q="lim (3n² − n + 1)/(2n² + 5) = …", r=["0", "3/2", "+∞"],
         ok=1, ex="On factorise par n² en haut et en bas : (3 − 1/n + 1/n²)/(2 + 5/n²) → 3/2.", voir="prep"),
    dict(q="lim (√(n + 1) − √n) = …", r=["0", "1", "+∞"],
         ok=0, ex="Quantité conjuguée : 1/(√(n + 1) + √n) → 0.", voir="conj"),
    dict(q="Si 2 − 1/n ≤ uₙ ≤ 2 + 1/n pour tout n ≥ 1, alors…", r=["uₙ → 2", "on ne peut rien dire", "uₙ = 2 pour tout n"],
         ok=0, ex="Théorème des gendarmes : les deux encadrements tendent vers 2.", voir="thm_g"),
    dict(q="lim (−1,5)ⁿ = …", r=["0", "−∞", "pas de limite"],
         ok=2, ex="q ≤ −1 : les termes changent de signe et grandissent en valeur absolue.", voir="thm_q"),
    dict(q="La démonstration de lim qⁿ = +∞ pour q > 1 utilise…",
         r=["le théorème des gendarmes", "l'inégalité de Bernoulli et la comparaison", "la quantité conjuguée"],
         ok=1, ex="qⁿ = (1 + a)ⁿ ≥ 1 + na → +∞, avec a = q − 1 > 0.", voir="dem_q"),
    dict(q="Une suite croissante et majorée par 5…", r=["converge vers 5", "converge vers une limite ℓ ≤ 5", "tend vers +∞"],
         ok=1, ex="Convergence monotone : la limite est inférieure ou égale au majorant, pas forcément égale (1 − 1/(n + 1) → 1).", voir="exist"),
    dict(q="uₙ₊₁ = √(uₙ + 2) converge vers ℓ ≥ 0. Alors ℓ = …", r=["−1", "2", "√2"],
         ok=1, ex="ℓ = √(ℓ + 2) donne ℓ² − ℓ − 2 = 0, soit ℓ = 2 ou ℓ = −1 ; on garde ℓ = 2.", voir="res7"),
    dict(q="Pour écrire f(ℓ) = ℓ à partir de uₙ₊₁ = f(uₙ), il faut que…", r=["f soit croissante", "f soit continue", "u₀ = ℓ"],
         ok=1, ex="On passe à la limite dans f(uₙ) grâce à la continuité de f.", voir="pf"),
]

CREDITS = [
    "Animations, schémas, graphiques et exercices : faits pour le site. "
    "Polices : Carnet Math (sous-ensemble de STIX Two Math), Caveat, Spectral, Archivo, JetBrains Mono, sous licence SIL OFL.",
]
