"""Maths, chapitre 1 : « Raisonnement par récurrence » — le cours en vidéo (vidéo pilote de la matière, site CQFD).

Même chaîne que les vidéos de cours PC et SVT (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les
mots) ; moteur maths/serie/moteur.js : formules en MathML ($…$, syntaxe du site), rédaction sur une page de carnet
(formule copie=True), code Python à trous, toile d'araignée (graphe, élément toile), illustrations dominos, propagation,
suite, carres, euler.
Contenu : le chapitre 1 du site (outils/specialites/maths/src/ch1.js), rien au-delà ; ce qui dépasse le programme est dit
« hors programme » ou « pour aller plus loin ». Les deux exercices sont ceux du site (formule à démontrer, abonnés
d'une chaîne). Chaque calcul affiché ou dit est vérifié par outils/serie-maths/verif_ch1.py.
Usage : PYTHONPATH=outils/serie-maths python3 outils/serie-philo/verifier.py maths_ch1
        PYTHONPATH=outils/serie-maths SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py maths_ch1   (brouillon)
        python3 outils/serie-philo/chevauchements.py maths-ch1
"""
from math import sqrt

SITE = "maths"
CODE = "maths-ch1"
NOTION = "Raisonnement par récurrence"
NUM = 1
TITRE = "Raisonnement par récurrence"
SUIVANT = "Chapitre 2 · Limites de suites"
RYTHME = "vivant"
PRONONCIATION = {"al-Karaji": "al Karadji", "As-Samaw'al": "As-Samaoual", "Fibonacci": "Fibonatchi", "Maurolico": "Maurolico",
                 "Peano": "Péano", "Bernoulli": "Bernouilli"}

# ---------------------------------------------------------------- données des graphiques (vérifiées par verif_ch1.py)
RAC = [[round(x / 20, 3), round(sqrt(x / 20 + 2), 4)] for x in range(0, 49)]          # y = √(x + 2) sur [0 ; 2,4]
U_RAC = [1.0]
for _ in range(4):
    U_RAC.append(round(sqrt(U_RAC[-1] + 2), 4))                                         # 1 ; 1,732 ; 1,932 ; 1,983 ; 1,996
F_CROIS = [[round(-0.2 + x / 10, 2), round(sqrt(-0.2 + x / 10 + 2), 4)] for x in range(0, 47)]
A_AB = [5.0]
for _ in range(7):
    A_AB.append(round(0.8 * A_AB[-1] + 3, 4))                                           # 5 ; 7 ; 8,6 ; 9,88…
BERN_P = [[n, round(1.05 ** n, 4)] for n in range(21)]                                  # 1,05^20 ≈ 2,65
BERN_A = [[n, round(1 + 0.05 * n, 4)] for n in range(21)]                               # 1 + 20 × 0,05 = 2


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ardoise", humeur="mystere", carton=False, beats=[
        "{tab_dom}{q1}{q1.1}Prends un entier n. Calcule n au carré, plus n, plus quarante et un. "
        "{q1.2}Pour n égale zéro, tu trouves quarante et un : un nombre premier. "
        "{q1.3}Pour n égale un, quarante-trois : premier. {q1.4}Pour deux, quarante-sept : encore premier.",
        "{-q1}{eul}{eul.go}Tu continues. Trois, quatre, cinq… Et ça marche à chaque fois. Dix, vingt, trente… jusqu'à trente-neuf. "
        "Quarante valeurs, quarante nombres premiers.",
        ("Alors, c'est toujours vrai ?", {"rate": "-6%"}),
        "{eul.40}Non. Pour n égale quarante, on tombe sur mille six cent quatre-vingt-un. "
        "Et mille six cent quatre-vingt-un, c'est quarante et un fois quarante et un. Pas premier du tout.",
        ("P", 0.5),
        "{-eul}{q2}Moralité : vérifier, même quarante fois, ne prouve rien. "
        "Mais alors, comment prouver qu'une propriété est vraie pour tous les entiers, une infinité de cas, sans les vérifier un par un ?",
        "{-q2}Réponse : avec des dominos. Enfin, presque. Avec le raisonnement par {!récurrence}récurrence.",
        "{-tab_dom}{plan}Voici le chemin. {plan.1}D'abord le principe : l'initialisation, l'hérédité, et pourquoi il faut les deux. "
        "{plan.2}Ensuite la rédaction modèle, celle que le correcteur attend. "
        "{plan.3}Puis les grands usages : les formules et les sommes, {plan.4}et les inégalités, avec l'inégalité de Bernoulli, une démonstration exigible. "
        "{plan.5}Et pour finir, deux exercices corrigés, dont un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_dom": dict(type="tableau", img="m1-dominos", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .5],
                        legende="Dominos qui tombent, photo Kurt:S, CC BY 2.0"),
        "q1": dict(type="formule", titre="Une expérience", x=230, y=150, w=820, lignes=[
            dict(f="$n^2+n+41$", cadre=True, taille=60),
            dict(f="$n=0$ : $41$, premier", ok=True),
            dict(f="$n=1$ : $43$, premier", ok=True),
            dict(f="$n=2$ : $47$, premier", ok=True)]),
        "eul": dict(type="illu", nom="euler", x=60, y=170, w=1160, h=520, dt=.14, titre="$n^2+n+41$ pour $n=0$, $1$, …, $39$"),
        "q2": dict(type="question", t="Comment prouver une infinité de cas sans les vérifier un par un ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Le principe : initialisation et hérédité", "La rédaction modèle, étape par étape",
            "Formules explicites et sommes", "Inégalités, et l'inégalité de Bernoulli",
            "Deux exercices corrigés, dont un type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Maths · Chapitre 1", t="Raisonnement par récurrence",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. le principe
    dict(id="principe", chap="Le principe : initialisation et hérédité", fond="ardoise", humeur="lumiere",
         retenir="Si $P(n_0)$ est vraie et si, pour tout $k\\geq n_0$, $P(k)$ entraîne $P(k+1)$, alors $P(n)$ est vraie pour tout $n\\geq n_0$.",
         beats=[
        "{q_inf}Le problème est simple à dire. On a une propriété qui dépend d'un entier n : on la note P de n. "
        "On veut la démontrer pour tous les entiers, à partir d'un certain rang, n zéro. Ça fait une infinité de cas. Impossible de tous les vérifier.",
        "{-q_inf}{tab_run}Alors, pense à une rangée de dominos. Aussi longue que tu veux. Infinie, même. "
        "Comment être sûr qu'ils vont tous tomber, sans les regarder un par un ?",
        "{-tab_run}{dom}Il suffit de deux choses. {dom.her}Première chose : les dominos sont placés de telle sorte que, si l'un d'eux tombe, "
        "n'importe lequel, il fait tomber le suivant. Si le domino k tombe, le domino k plus un tombe.",
        "{dom.init}Deuxième chose : on fait tomber le premier. Et là, regarde. Le premier fait tomber le deuxième, qui fait tomber le troisième, "
        "qui fait tomber le quatrième… Aucun n'est oublié.",
        "{dom.fin}Ils tombent tous.",
        ("P", 1.2),
        "{-dom}{def_init}En mathématiques, ces deux choses ont un nom. Faire tomber le premier domino, c'est l'{!initialisation}initialisation : "
        "on vérifie que P de n zéro est vraie.",
        "{-def_init}{def_her}Et la règle « si l'un tombe, le suivant tombe », c'est l'{!hérédité}hérédité : pour tout entier k supérieur ou égal à n zéro, "
        "si P de k est vraie, alors P de k plus un est vraie. {def_her.1}Attention : c'est une seule démonstration, mais elle vaut pour tous les k à la fois.",
        "{-def_her}{thm}{thm.1}Voici donc le principe de récurrence. Soit P de n une propriété, définie pour tout entier n supérieur ou égal à n zéro. "
        "{thm.2}Si P de n zéro est vraie, {thm.3}et si, pour tout k supérieur ou égal à n zéro, P de k entraîne P de k plus un, "
        "{thm.4}alors P de n est vraie pour tout entier n supérieur ou égal à n zéro.",
        "{-thm}{prop}Pourquoi est-ce que ça marche ? Déroulons. {prop.init}P de zéro est vraie : c'est l'initialisation. "
        "{prop.her}L'hérédité, elle, est une flèche, valable pour n'importe quel k. "
        "{prop.go}Appliquée à k égale zéro, elle donne P de un. Appliquée à k égale un, elle donne P de deux. Puis P de trois, P de quatre…",
        "{prop.fin}N'importe quel entier est atteint, en un nombre fini d'étapes. Deux démonstrations ont suffi pour une infinité de cas.",
        "{-prop}{note_ax}Une précision. Que ce raisonnement soit valable, c'est une propriété fondamentale de l'ensemble des entiers naturels. "
        "On l'admet : en mathématiques, c'est un axiome.",
        "{-note_ax}{usages}Au bac, tu rencontreras la récurrence dans trois situations. "
        "{usages.1}Établir une formule explicite : u n égale une expression de n. "
        "{usages.2}Encadrer une suite : a inférieur ou égal à u n, inférieur ou égal à b. "
        "{usages.3}Et montrer qu'une suite est monotone, par exemple u n inférieur ou égal à u n plus un.",
        "{-usages}",
    ], vis={
        "q_inf": dict(type="formule", titre="Le problème", x=200, y=170, w=880, lignes=[
            dict(f="$P(n)$ : une propriété de l'entier $n$", txt=True),
            dict(f="$P(0)$, $P(1)$, $P(2)$, …, $P(1000)$, …", taille=50),
            dict(f="une infinité de cas : impossible de tous les vérifier", txt=True)]),
        "tab_run": dict(type="tableau", img="m1-parcours", fond=True, de=[1.0, .5, .5], a=[1.25, .6, .45],
                        legende="Dominos prêts à tomber, photo Pauloleong2002, CC BY-SA 4.0"),
        "dom": dict(type="illu", nom="dominos", x=0, y=110, w=1280, h=560, n=44, k=5, y0=400,
                    bulle="si le domino $k$ tombe, il fait tomber le domino $k+1$", init="on pousse le premier",
                    fin="tous les dominos tombent"),
        "def_init": dict(type="def", terme="Initialisation", cles=["vérifie"],
                         t="On vérifie que $P(n_0)$ est vraie : le premier domino tombe.", x=170, y=210, w=940),
        "def_her": dict(type="def", terme="Hérédité", cles=["entier", "alors"],
                        t="Pour tout entier $k\\geq n_0$ : si $P(k)$ est vraie, alors $P(k+1)$ est vraie.",
                        etape="Une seule démonstration, valable pour tous les $k$ à la fois.", x=170, y=170, w=940),
        "thm": dict(type="formule", titre="Le principe de récurrence", x=150, y=130, w=980, lignes=[
            dict(f="Soit $P(n)$ une propriété définie pour tout entier $n\\geq n_0$.", txt=True),
            dict(lab="Initialisation", f="$P(n_0)$ est vraie ;"),
            dict(lab="Hérédité", f="pour tout $k\\geq n_0$, $P(k)\\Rightarrow P(k+1)$ ;"),
            dict(f="alors $P(n)$ est vraie pour tout $n\\geq n_0$.", cadre=True)]),
        "prop": dict(type="illu", nom="propagation", x=60, y=150, w=1160, h=500, n=7,
                     prop="Chaque case est un cas : $P(0)$, $P(1)$, $P(2)$…",
                     fin="Donc $P(n)$ est vraie pour tout $n\\in\\N$"),
        "note_ax": dict(type="note", titre="Un axiome", cles=["fondamentale", "admet"],
                        t="Le principe de récurrence est une propriété fondamentale de $\\N$ : on l'admet.", x=170, y=220, w=940),
        "usages": dict(type="cartes", items=[
            dict(ic="egal", t="Une formule", q="$u_n=$ une expression de $n$"),
            dict(ic="encadre", t="Un encadrement", q="$a\\leq u_n\\leq b$"),
            dict(ic="monte", t="Une monotonie", q="$u_n\\leq u_{n+1}$")]),
    }),

    # ================================================================ II. les deux étapes sont indispensables
    dict(id="deux", chap="Les deux étapes sont indispensables", fond="carnet", humeur="tension",
         retenir="Il faut les deux : sans initialisation, rien ne tombe ; sans hérédité, la chaîne s'arrête. Un exemple ne prouve rien, un contre-exemple suffit.",
         beats=[
        "{q_deux}Est-ce qu'on peut se passer d'une des deux étapes ? Faisons l'expérience.",
        "{-q_deux}{her3}{her3.1}D'abord, l'hérédité sans l'initialisation. Prenons P de n : « deux puissance n est divisible par trois ».",
        "{her3.2}Hérédité : supposons que deux puissance k soit divisible par trois, c'est-à-dire qu'il s'écrive trois fois un entier m. "
        "{her3.3}Alors deux puissance k plus un, c'est deux fois deux puissance k, donc deux fois trois m, {her3.4}c'est-à-dire trois fois deux m. "
        "Divisible par trois ! L'hérédité est vraie.",
        "{her3.5}Mais l'initialisation ? Deux puissance zéro vaut un. Et un n'est pas divisible par trois. "
        "{her3.6}En fait, deux puissance n n'est jamais divisible par trois : ce n'est qu'un produit de deux.",
        "{-her3}{dom_si}Avec les dominos, c'est limpide. {dom_si.her}La règle est en place : si l'un tombait, il ferait tomber le suivant. "
        "{dom_si.init}Mais personne ne pousse le premier. Résultat : rien ne tombe. Jamais.",
        "{-dom_si}{dom_eu}À l'inverse, l'initialisation sans l'hérédité. Tu la connais déjà : c'est notre expression du début, n au carré plus n plus quarante et un. "
        "{dom_eu.init}Elle donne un nombre premier pour n égale zéro, puis pour un, deux, trois… jusqu'à trente-neuf. "
        "Mais aucune hérédité ne relie un cas au suivant.",
        "{dom_eu.fin}En dominos : quarante dominos tombent, puis il y a un trou. Le domino numéro quarante est trop loin. "
        "La chaîne s'arrête, et mille six cent quatre-vingt-un n'est pas premier.",
        "{-dom_eu}{lecon}Retiens la leçon. {lecon.1}Sans initialisation, l'hérédité tourne à vide. "
        "{lecon.2}Sans hérédité, quarante vérifications ne font pas une preuve. "
        "{lecon.3}Et dans l'autre sens : pour montrer qu'une propriété est fausse, un seul contre-exemple suffit. Pas besoin de récurrence.",
        "{-lecon}{anc}Un mot d'histoire. Ce raisonnement est ancien : on en trouve des anticipations chez {anc.1}al-Karaji, "
        "{anc.2}As-Samaw'al, {anc.3}Fibonacci, {anc.4}ou Maurolico.",
        "{-anc}{pascal}{pascal_n}Pascal l'a formalisé.",
        "{-pascal}{-pascal_n}{peano}{peano_n}Puis surtout Peano et ses collaborateurs, à la fin du dix-neuvième siècle, "
        "qui en ont fait l'un des fondements de l'arithmétique.",
        "{-peano}{-peano_n}",
    ], vis={
        "q_deux": dict(type="question", t="Et si on oubliait une des deux étapes ?"),
        "her3": dict(type="formule", titre="L'hérédité sans l'initialisation", x=130, y=90, w=1020, lignes=[
            dict(f="$P(n)$ : « $2^n$ est divisible par $3$ »", txt=True),
            dict(f="Si $2^k=3m$ avec $m$ entier,", m="hypothèse", taille=40),
            dict(f="alors $2^{k+1}=2\\times2^k=2\\times3m$", ind=True, taille=40),
            dict(f="$2^{k+1}=3\\times(2m)$ : divisible par $3$", ind=True, ok=True, m="hérédité vraie !", taille=40),
            dict(f="Mais $2^0=1$ : pas divisible par $3$", ko=True, m="initialisation fausse", taille=40),
            dict(f="En fait, $P(n)$ n'est vraie pour aucun $n$.", txt=True)]),
        "dom_si": dict(type="illu", nom="dominos", x=0, y=120, w=1280, h=540, n=18, k=5, y0=400, mode="sans_init",
                       bulle="si l'un tombait, il ferait tomber le suivant", init="personne ne pousse : rien ne tombe"),
        "dom_eu": dict(type="illu", nom="dominos", x=0, y=120, w=1280, h=540, n=44, k=5, y0=400, mode="trou", trou=40, dt=.13,
                       bulle="", init="$n=0$ : $41$, premier", stop="$n=40$ : $1681=41^2$, pas premier",
                       fin="quarante vérifications ne font pas une preuve"),
        "lecon": dict(type="liste", titre="La leçon", items=[
            "Sans initialisation, l'hérédité tourne à vide", "Sans hérédité, des vérifications ne prouvent rien",
            "Pour réfuter, un seul contre-exemple suffit"], marques=["✗", "✗", "!"], x=170, y=170, w=940),
        "anc": dict(type="liste", titre="Des anticipations", items=["al-Karaji", "As-Samaw'al", "Fibonacci", "Maurolico"],
                    marques=["·", "·", "·", "·"], x=380, y=160, w=520),
        "pascal": dict(type="portrait", nom="Blaise Pascal", img="pascal", dates="1623 – 1662",
                       legende="formalise le raisonnement par récurrence"),
        "pascal_n": dict(type="tag", style="repere", t="Pascal : la récurrence formalisée", x=660, y=330, w=560),
        "peano": dict(type="portrait", nom="Giuseppe Peano", img="peano", dates="1858 – 1932",
                      legende="la récurrence, fondement de l'arithmétique"),
        "peano_n": dict(type="tag", style="repere", t="Fin du XIXᵉ siècle : un fondement de l'arithmétique", x=660, y=330, w=580),
    }),

    # ================================================================ III. rédiger : le modèle
    dict(id="rediger", chap="Rédiger une récurrence : le modèle", fond="ardoise", humeur="calme",
         retenir="Propriété, initialisation, hérédité, conclusion. Dans l'hérédité : on suppose $P(k)$ pour un $k$ fixé, on écrit le but $P(k+1)$, on utilise l'hypothèse.",
         beats=[
        "{suite}Passons à la pratique, avec la suite définie par u zéro égale un, et u n plus un égale deux u n plus trois. "
        "Calculons quelques termes. {suite.1}u un : deux fois un, plus trois, cinq. {suite.2}u deux : deux fois cinq, plus trois, treize. "
        "{suite.3}Puis vingt-neuf, {suite.4}soixante et un, {suite.5}cent vingt-cinq.",
        "{suite.c}Tu remarques quelque chose ? Ajoute trois à chaque terme : quatre, huit, seize, trente-deux… des puissances de deux ! "
        "{suite.ok}On conjecture que u n égale deux puissance n plus deux, moins trois.",
        "{-suite}{py}On peut le vérifier avec Python. Ce programme calcule les premiers termes, puis les valeurs de la formule. "
        "{py.s}Les deux listes coïncident.",
        "Mais attention : sept valeurs, ce n'est pas une preuve. On vient de voir ce que valent quarante vérifications ! "
        "Il faut une démonstration. Et c'est le travail de la récurrence.",
        "{-py}{copie}Voici la rédaction modèle. Le correcteur cherche quatre étapes : retiens-les, dans cet ordre. "
        "{copie.1}Un, la propriété. On l'écrit en toutes lettres : pour tout entier n, on note P de n : « u n égale deux puissance n plus deux, moins trois ».",
        "{copie.2}Deux, l'initialisation. Pour n égale zéro, on calcule séparément les deux membres. D'un côté, u zéro égale un. "
        "De l'autre, deux puissance deux, moins trois : quatre moins trois, un. Ils sont égaux : P de zéro est vraie.",
        "{copie.3}Trois, l'hérédité. On écrit : soit k un entier naturel. On suppose que P de k est vraie, "
        "c'est-à-dire u k égale deux puissance k plus deux, moins trois. {copie.m3}C'est l'hypothèse de récurrence.",
        "{copie.4}Et tout de suite, on écrit le but : montrons P de k plus un, c'est-à-dire u k plus un égale deux puissance k plus trois, moins trois. "
        "{copie.m4}Écrire le but, c'est savoir où on va.",
        "{-copie}{calc}Maintenant, le calcul. {calc.1}On part de u k plus un. Par définition de la suite, c'est deux u k plus trois. "
        "{calc.2}Et là, on utilise l'hypothèse de récurrence : on remplace u k par deux puissance k plus deux, moins trois. "
        "{calc.3}On développe : deux fois deux puissance k plus deux, c'est deux puissance k plus trois. Puis moins six, plus trois. "
        "{calc.4}Il reste deux puissance k plus trois, moins trois. C'est exactement le but. {calc.5}P de k plus un est vraie.",
        "{-calc}{concl}Quatre, la conclusion. {concl.1}P de zéro est vraie, et la propriété est héréditaire. "
        "{concl.2}Donc, par récurrence, pour tout entier naturel n, u n égale deux puissance n plus deux, moins trois.",
        "{-concl}{reflexes}Résumons en quatre réflexes. {reflexes.1}Écrire P de n en toutes lettres, entre guillemets. "
        "{reflexes.2}Pour l'initialisation, calculer séparément les deux membres. "
        "{reflexes.3}Pour l'hérédité : soit k, supposons P de k, puis écrire le but. Partir de u k plus un, utiliser la définition de la suite, puis l'hypothèse. "
        "{reflexes.4}Et conclure, en citant l'initialisation, l'hérédité et le principe de récurrence.",
        "{-reflexes}{piege_n}Un piège de rédaction, très fréquent. Tu peux écrire n au lieu de k dans l'hérédité, à condition de dire que n est fixé. "
        "Mais écrire « supposons P de n vraie pour tout n », c'est supposer exactement ce qu'on veut démontrer. "
        "On suppose P de k pour un entier k. Un seul, fixé.",
        "{-piege_n}",
    ], vis={
        "suite": dict(type="illu", nom="suite", x=50, y=120, w=1180, h=520, termes=[1, 5, 13, 29, 61, 125], op="×2 +3",
                      f="$2^{n+2}-3$", fv=["$2^2-3$", "$2^3-3$", "$2^4-3$", "$2^5-3$", "$2^6-3$", "$2^7-3$"]),
        "py": dict(type="code", titre="Python · conjecturer", x=190, y=86, w=900, taille=24, lignes=[
            "def termes(n):", "    u = 1                      # u0", "    L = [u]", "    for k in range(n):",
            "        u = 2 * u + 3          # u(k+1) = 2 u(k) + 3", "        L.append(u)", "    return L", "",
            "print(termes(6))", "print([2**(k + 2) - 3 for k in range(7)])"],
            sortie="[1, 5, 13, 29, 61, 125, 253]\n[1, 5, 13, 29, 61, 125, 253]"),
        "copie": dict(type="formule", copie=True, titre="La rédaction modèle", x=90, y=120, w=1100, lignes=[
            dict(lab="Propriété.", f="Pour tout $n\\in\\N$, on note $P(n)$ : « $u_n=2^{n+2}-3$ ».", taille=32),
            dict(lab="Initialisation.", f="$u_0=1$ et $2^{0+2}-3=4-3=1$ : $P(0)$ est vraie.", taille=32),
            dict(lab="Hérédité.", f="Soit $k\\in\\N$ tel que $u_k=2^{k+2}-3$.", m="hypothèse de récurrence", taille=32),
            dict(f="Montrons $P(k+1)$ : « $u_{k+1}=2^{k+3}-3$ ».", ind=True, hl=True, m="le but !", taille=32)]),
        "calc": dict(type="formule", copie=True, titre="Hérédité : le calcul", x=150, y=110, w=980, lignes=[
            dict(f="$u_{k+1}=2u_k+3$", m="définition de la suite", taille=40),
            dict(f="$=2\\left(2^{k+2}-3\\right)+3$", ind=True, m="hypothèse de récurrence", taille=40),
            dict(f="$=2^{k+3}-6+3$", ind=True, taille=40),
            dict(f="$=2^{k+3}-3$", ind=True, cadre=True, m="c'est le but", taille=40),
            dict(f="Donc $P(k+1)$ est vraie.", txt=True)]),
        "concl": dict(type="formule", copie=True, titre="Conclusion", x=150, y=200, w=980, lignes=[
            dict(f="$P(0)$ est vraie et la propriété est héréditaire."),
            dict(f="Par récurrence, pour tout $n\\in\\N$, $u_n=2^{n+2}-3$.", cadre=True)]),
        "reflexes": dict(type="liste", titre="Les quatre réflexes", items=[
            "Écrire $P(n)$ en toutes lettres, entre guillemets",
            "Initialisation : calculer séparément les deux membres",
            "Hérédité : « soit $k$, supposons $P(k)$ », écrire le but, utiliser l'hypothèse",
            "Conclure : initialisation, hérédité, principe de récurrence"], x=150, y=130, w=980),
        "piege_n": dict(type="note", titre="Piège de rédaction", cles=["supposer", "fixé"],
                        t="« Supposons $P(n)$ vraie pour tout $n$ » : c'est supposer ce qu'on veut démontrer. On suppose $P(k)$ pour un entier $k$ fixé.",
                        x=170, y=190, w=940),
    }),

    # ================================================================ IV. récurrence et sommes
    dict(id="sommes", chap="Récurrence et sommes", fond="carnet", humeur="lumiere",
         retenir="$1+3+5+\\cdots+(2n-1)=n^2$. Pour une somme, passer du rang $k$ au rang $k+1$, c'est ajouter le terme suivant.",
         beats=[
        "{carres}Deuxième usage : les sommes. Additionne les premiers nombres impairs. {carres.1}Un. {carres.2}Un plus trois : quatre. "
        "{carres.3}Un plus trois plus cinq : neuf. {carres.4}Plus sept : seize. {carres.5}Plus neuf : vingt-cinq.",
        "Un, quatre, neuf, seize, vingt-cinq : des carrés ! Regarde le dessin. Chaque nombre impair forme une équerre, qui complète exactement le carré suivant.",
        "{carres.g}Et voici pourquoi, en général. Autour d'un carré k fois k, l'équerre compte k carreaux, plus k carreaux, plus celui du coin : "
        "deux k plus un. {carres.f}Et k au carré, plus deux k plus un, c'est k plus un, au carré. C'est l'hérédité, en image.",
        "{-carres}{som}Rédigeons. {som.1}Pour tout entier n supérieur ou égal à un, on note P de n : « un plus trois plus cinq, "
        "et ainsi de suite jusqu'à deux n moins un, égale n au carré ».",
        "{som.2}Initialisation, pour n égale un : la somme se réduit à un, et un au carré vaut un.",
        "{som.3}Hérédité : soit k supérieur ou égal à un, tel que la somme jusqu'à deux k moins un vaut k au carré. "
        "{som.4}Au rang k plus un, on ajoute un terme, un seul : l'impair suivant, deux fois k plus un, moins un, c'est-à-dire deux k plus un. "
        "{som.5}La somme vaut donc k au carré plus deux k plus un, c'est-à-dire k plus un, au carré. C'est P de k plus un.",
        "{som.6}Conclusion : par récurrence, la formule est vraie pour tout n supérieur ou égal à un.",
        "{-som}{astuce_som}Le réflexe à retenir pour les sommes : passer du rang k au rang k plus un, c'est ajouter le terme suivant. "
        "Écris-le à part avant de calculer : c'est là que se cachent les erreurs.",
        "{-astuce_som}{sigma}{sigma.1}Cette somme s'écrit aussi avec le symbole sigma : somme, pour k allant de un à n, de deux k moins un. "
        "Le programme permet ce symbole pour abréger. Mais en cas de doute, écris la somme avec des pointillés : c'est plus sûr.",
        "{sigma.2}Une autre formule du même genre : la somme des carrés. Un au carré, plus deux au carré, jusqu'à n au carré, "
        "égale n, fois n plus un, fois deux n plus un, le tout sur six. Elle se démontre exactement de la même façon. "
        "{sigma.3}Vérifie pour n égale trois : un plus quatre plus neuf, quatorze. Et trois fois quatre fois sept, sur six : quatorze aussi.",
        "{-sigma}",
    ], vis={
        "carres": dict(type="illu", nom="carres", x=110, y=110, w=1080, h=560, c=64),
        "som": dict(type="formule", copie=True, titre="La somme des impairs", x=90, y=80, w=1100, lignes=[
            dict(lab="Propriété.", f="Pour $n\\geq1$, $P(n)$ : « $1+3+5+\\cdots+(2n-1)=n^2$ »."),
            dict(lab="Initialisation.", f="pour $n=1$, la somme vaut $1$ et $1^2=1$."),
            dict(lab="Hérédité.", f="Soit $k\\geq1$ tel que $1+3+\\cdots+(2k-1)=k^2$."),
            dict(f="Terme suivant : $2(k+1)-1=2k+1$", ind=True, m="on ajoute UN terme"),
            dict(f="$1+3+\\cdots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2$", ind=True, cadre=True, taille=31),
            dict(lab="Conclusion.", f="par récurrence, la formule est vraie pour tout $n\\geq1$.")]),
        "astuce_som": dict(type="note", titre="Le réflexe des sommes", cles=["ajouter", "suivant"],
                           t="Du rang $k$ au rang $k+1$, on ajoute le terme suivant. Écris-le à part avant de calculer.", x=170, y=200, w=940),
        "sigma": dict(type="formule", titre="D'autres écritures, d'autres sommes", x=130, y=110, w=1020, lignes=[
            dict(f="$1+3+\\cdots+(2n-1)=\\sum_{k=1}^{n}(2k-1)=n^2$", n="le symbole $\\sum$ abrège ; en cas de doute, écris les pointillés"),
            dict(f="$1^2+2^2+\\cdots+n^2=\\dfrac{n(n+1)(2n+1)}{6}$", cadre=True),
            dict(f="pour $n=3$ : $1+4+9=14$ et $\\dfrac{3\\times4\\times7}{6}=14$", ok=True)]),
    }),

    # ================================================================ V. récurrence et inégalités
    dict(id="inegalites", chap="Récurrence et inégalités", fond="ardoise", humeur="calme",
         retenir="Une fonction croissante conserve l'ordre : si $a\\leq b$, alors $f(a)\\leq f(b)$. C'est l'outil des encadrements par récurrence.",
         beats=[
        "{q5}Troisième usage, le plus fréquent au bac : les inégalités. La suite est définie par u n plus un égale f de u n, "
        "{q5.2}et on te demande de montrer, par exemple, que zéro est inférieur ou égal à u n, inférieur ou égal à u n plus un, inférieur ou égal à deux.",
        "{-q5}{gr_f}L'outil clé, c'est la croissance de f. {gr_f.1}Une fonction croissante conserve l'ordre : "
        "{gr_f.2}{gr_f.3}{gr_f.5}{gr_f.6}si a est inférieur ou égal à b, {gr_f.4}{gr_f.7}{gr_f.8}alors f de a est inférieur ou égal à f de b. "
        "On applique f à l'inégalité, sans changer son sens.",
        "{-gr_f}{ex5}{ex5.1}Exemple. u zéro égale un, et u n plus un égale racine de u n plus deux. "
        "{ex5.2}On veut montrer que, pour tout n, zéro inférieur ou égal à u n, inférieur ou égal à u n plus un, inférieur ou égal à deux. "
        "{ex5.3}On note f de x égale racine de x plus deux. Elle est croissante sur moins deux, plus l'infini : "
        "c'est la composée de deux fonctions croissantes, x donne x plus deux, puis la racine carrée.",
        "{-ex5}{toile}Avant de démontrer, regardons. {toile.1}La courbe de f, {toile.2}et la droite y égale x. "
        "{toile.3}On part de u zéro égale un. On monte jusqu'à la courbe : c'est u un. On revient sur la droite, on remonte : u deux. Puis u trois…",
        "Les termes grimpent, en escalier, et ils se tassent sous deux. {toile.4}Sans jamais le dépasser. C'est précisément ce qu'on va démontrer.",
        "{-toile}{rec5}{rec5.1}Initialisation. u zéro égale un, et u un égale racine de trois, environ un virgule soixante-treize. "
        "On a bien zéro, inférieur à un, inférieur à racine de trois, inférieur à deux.",
        "{rec5.2}Hérédité. Soit k un entier tel que zéro inférieur ou égal à u k, inférieur ou égal à u k plus un, inférieur ou égal à deux. "
        "{rec5.3}Comme f est croissante sur l'intervalle zéro, deux, on applique f à toute la chaîne, sans changer le sens.",
        "{rec5.4}Or f de u k, c'est u k plus un. Et f de u k plus un, c'est u k plus deux. "
        "{rec5.m4}Et aux deux bouts : f de zéro vaut racine de deux, et f de deux vaut racine de quatre, c'est-à-dire deux.",
        "{rec5.5}Comme zéro est inférieur à racine de deux, on obtient : zéro inférieur ou égal à u k plus un, inférieur ou égal à u k plus deux, "
        "inférieur ou égal à deux. C'est P de k plus un.",
        "{rec5.6}Conclusion : la suite est croissante, et majorée par deux. Au chapitre suivant, tu verras qu'une telle suite converge. Ici, vers deux.",
        "{-rec5}{meth5}La méthode, en trois réflexes. {meth5.1}De a inférieur ou égal à u k inférieur ou égal à b, "
        "on tire f de a inférieur ou égal à u k plus un, inférieur ou égal à f de b. {meth5.2}Puis on compare f de a avec a, et f de b avec b. "
        "{meth5.3}Et on vérifie la croissance de f sur le bon intervalle : celui où se trouvent les termes.",
        "{-meth5}{affine}Et si f n'est pas monotone ? Tu peux aussi travailler directement sur l'expression. "
        "{affine.1}Par exemple, avec u k plus un égale zéro virgule cinq u k, plus un, et l'hypothèse u k inférieur ou égal à deux. "
        "{affine.2}On multiplie par zéro virgule cinq, qui est positif : zéro virgule cinq u k, inférieur ou égal à un. "
        "{affine.3}Puis on ajoute un : u k plus un, inférieur ou égal à deux.",
        "{-affine}{piege_neg}Et attention au sens des inégalités. {piege_neg.1}Multiplier par un nombre négatif renverse l'inégalité. "
        "{piege_neg.2}Appliquer une fonction décroissante aussi. "
        "{piege_neg.3}C'est pour ça qu'avec une fonction décroissante, comme un plus un sur x, la suite n'est en général pas monotone : "
        "l'ordre s'inverse à chaque étape, et les termes oscillent.",
        "{-piege_neg}",
    ], vis={
        "q5": dict(type="formule", titre="Le cas le plus fréquent au bac", x=200, y=190, w=880, lignes=[
            dict(f="$u_{n+1}=f(u_n)$", taille=54),
            dict(f="Montrer : $0\\leq u_n\\leq u_{n+1}\\leq2$", cadre=True, taille=50)]),
        "gr_f": dict(type="graphe", titre="Une fonction croissante conserve l'ordre", x=300, y=120, w=680, h=520,
                     ax=dict(x=[-0.95, 4.4], y=[0, 2.7], gx=[], gy=[], lx="$x$", ly="$y$"),
                     el=[dict(type="courbe", pts=F_CROIS, c="te", ep=3.4),
                         dict(type="point", x=0.6, y=round(sqrt(2.6), 4), c="sa", proj=True),
                         dict(type="texte", x=0.6, y=-0.16, t="$a$", c="sa"),
                         dict(type="texte", x=-0.5, y=round(sqrt(2.6), 4), t="$f(a)$", c="sa"),
                         dict(type="point", x=3.0, y=round(sqrt(5.0), 4), c="ca", proj=True),
                         dict(type="texte", x=3.0, y=-0.16, t="$b$", c="ca"),
                         dict(type="texte", x=-0.5, y=round(sqrt(5.0), 4), t="$f(b)$", c="ca"),
                         dict(type="texte", x=2.55, y=0.75, t="$a\\leq b\\Rightarrow f(a)\\leq f(b)$", c="iv")]),
        "ex5": dict(type="formule", titre="Exemple", x=150, y=140, w=980, lignes=[
            dict(f="$u_0=1$ et $u_{n+1}=\\sqrt{u_n+2}$"),
            dict(f="Montrer : pour tout $n\\in\\N$, $0\\leq u_n\\leq u_{n+1}\\leq2$", cadre=True, taille=40),
            dict(f="$f(x)=\\sqrt{x+2}$ est croissante sur $[-2;+\\infty[$",
                 n="composée de $x\\mapsto x+2$ et de la racine carrée, toutes deux croissantes")]),
        "toile": dict(type="graphe", titre="La toile d'araignée de $u_{n+1}=\\sqrt{u_n+2}$", x=310, y=110, w=660, h=540,
                      ax=dict(x=[0, 2.4], y=[0, 2.4], gx=[0.5, 1, 1.5, 2], gy=[0.5, 1, 1.5, 2], lx="$x$", ly="$y$"),
                      el=[dict(type="courbe", pts=RAC, c="te", ep=3.4, lbl="$y=\\sqrt{x+2}$", lp=[0.55, 1.95]),
                          dict(type="droite", pts=[[0, 0], [2.4, 2.4]], c="iv2", ep=2.2, lbl="$y=x$", lp=[0.62, 0.32]),
                          dict(type="toile", u=U_RAC, c="sa", nlab=2, dur=4.5),
                          dict(type="droite", pts=[[0, 2], [2.4, 2]], c="ca", ep=2.4, tir=True, lbl="$y=2$", lp=[2.18, 2.2])]),
        "rec5": dict(type="formule", copie=True, titre="La démonstration", x=100, y=74, w=1080, lignes=[
            dict(lab="Initialisation.", f="$u_0=1$, $u_1=\\sqrt3\\approx1{,}73$ : $0\\leq1\\leq\\sqrt3\\leq2$.", taille=30),
            dict(lab="Hérédité.", f="Soit $k\\in\\N$ tel que $0\\leq u_k\\leq u_{k+1}\\leq2$.", m="hypothèse", taille=31),
            dict(f="$f$ croissante sur $[0;2]$ : $f(0)\\leq f(u_k)\\leq f(u_{k+1})\\leq f(2)$", ind=True, m="on applique $f$", taille=31),
            dict(f="soit $\\sqrt2\\leq u_{k+1}\\leq u_{k+2}\\leq2$", ind=True, m="$f(2)=\\sqrt4=2$", taille=31),
            dict(f="comme $0\\leq\\sqrt2$ : $0\\leq u_{k+1}\\leq u_{k+2}\\leq2$, c'est $P(k+1)$.", ind=True, cadre=True, taille=31),
            dict(lab="Conclusion.", f="$(u_n)$ est croissante et majorée par $2$.", taille=31)]),
        "meth5": dict(type="liste", titre="Encadrer par récurrence", items=[
            "De $a\\leq u_k\\leq b$, tirer $f(a)\\leq u_{k+1}\\leq f(b)$",
            "Comparer $f(a)$ à $a$, et $f(b)$ à $b$",
            "Vérifier la croissance de $f$ sur le bon intervalle"], x=170, y=170, w=940),
        "affine": dict(type="formule", titre="Sans la croissance de $f$ : travailler sur l'expression", x=150, y=150, w=980, lignes=[
            dict(f="$u_{k+1}=0{,}5\\,u_k+1$ et $u_k\\leq2$", txt=True),
            dict(f="$0{,}5\\,u_k\\leq0{,}5\\times2=1$", m="$0{,}5>0$ : même sens"),
            dict(f="$u_{k+1}=0{,}5\\,u_k+1\\leq2$", cadre=True, m="on ajoute $1$")]),
        "piege_neg": dict(type="liste", titre="Attention au sens", items=[
            "Multiplier par un nombre négatif renverse l'inégalité",
            "Appliquer une fonction décroissante aussi",
            "$f$ décroissante, par exemple $f(x)=1+\\dfrac1x$ : les termes oscillent"], marques=["!", "!", "!"], x=170, y=170, w=940),
    }),

    # ================================================================ VI. l'inégalité de Bernoulli (démonstration exigible)
    dict(id="bernoulli", chap="L'inégalité de Bernoulli", fond="carnet", humeur="mystere",
         retenir="Pour tout réel $a\\geq0$ et tout entier $n$ : $(1+a)^n\\geq1+na$. Le point clé : multiplier par $1+a>0$, puis $ka^2\\geq0$.",
         beats=[
        "{tag_bo}{bern}Maintenant, une démonstration que tu dois savoir refaire seul, le jour du bac : elle est exigible. L'inégalité de Bernoulli. "
        "{bern.1}Pour tout réel a positif ou nul, et pour tout entier naturel n, un plus a, puissance n, est supérieur ou égal à un plus n a.",
        "{-bern}{-tag_bo}{gr_b}Qu'est-ce qu'elle raconte ? Prends a égale zéro virgule zéro cinq : une hausse de cinq pour cent, répétée. "
        "{gr_b.1}En jaune, un virgule zéro cinq, puissance n. {gr_b.2}En bleu, un plus n fois zéro virgule zéro cinq : on ajoute toujours la même chose.",
        "{gr_b.3}{gr_b.4}Les points jaunes restent au-dessus. Pour n égale vingt, un plus vingt fois zéro virgule zéro cinq, ça fait deux. "
        "Et un virgule zéro cinq, puissance vingt ? Environ deux virgule soixante-cinq.",
        "En clair : un plus a, puissance n, grandit au moins aussi vite qu'une suite arithmétique. "
        "Au chapitre suivant, c'est la clé de la limite de q puissance n, quand q est plus grand que un.",
        "{-gr_b}{dem}Démontrons-la. {dem.1}Soit a un réel positif. Pour n entier naturel, on note P de n : "
        "« un plus a, puissance n, supérieur ou égal à un plus n a ».",
        "{dem.2}Initialisation : un plus a, puissance zéro, vaut un. Et un plus zéro fois a, vaut un aussi. "
        "Un est bien supérieur ou égal à un : P de zéro est vraie.",
        "{dem.3}Hérédité. Soit k un entier tel que un plus a, puissance k, est supérieur ou égal à un plus k a.",
        "{dem.4}Et voici le point délicat : on multiplie les deux membres par un plus a. "
        "On obtient : un plus a, puissance k plus un, supérieur ou égal à un plus k a, fois un plus a. "
        "{dem.m4}On a le droit de le faire sans changer le sens, parce que un plus a est strictement positif. "
        "C'est exactement cette justification que le correcteur attend.",
        "{dem.5}On développe le membre de droite : un, plus a, plus k a, plus k a carré. C'est-à-dire un, plus k plus un fois a, plus k a carré.",
        "{dem.6}Or k a carré est positif ou nul. Donc cette quantité est supérieure ou égale à un, plus k plus un fois a. "
        "{dem.7}Finalement, un plus a, puissance k plus un, est supérieur ou égal à un, plus k plus un fois a. C'est P de k plus un.",
        "{dem.8}Conclusion : par récurrence, pour tout entier naturel n, un plus a, puissance n, est supérieur ou égal à un plus n a.",
        "{-dem}{plus_b}Pour aller plus loin, hors programme : la même preuve marche dès que a est supérieur ou égal à moins un, "
        "car alors un plus a reste positif ou nul.",
        "{-plus_b}",
    ], vis={
        "tag_bo": dict(type="tag", style="plus", t="Démonstration exigible au bac", x=170, y=110, w=600),
        "bern": dict(type="def", terme="Inégalité de Bernoulli", cles=["réel", "entier"],
                     t="Pour tout réel $a\\geq0$ et tout entier $n\\in\\N$ : $(1+a)^n\\geq1+na$.",
                     etape="À savoir démontrer seul, par récurrence.", x=170, y=200, w=940),
        "gr_b": dict(type="graphe", titre="$a=0{,}05$ : la puissance contre la suite arithmétique", x=290, y=120, w=720, h=520,
                     ax=dict(x=[0, 21.5], y=[1, 2.85], gx=[5, 10, 15, 20], gy=[1.5, 2, 2.5], lx="$n$", ly=""),
                     el=[dict(type="points", pts=BERN_P, c="sa", pas=.09, r=6),
                         dict(type="points", pts=BERN_A, c="te", pas=.09, r=6),
                         dict(type="texte", x=14.6, y=2.62, t="$1{,}05^{20}\\approx2{,}65$", c="sa"),
                         dict(type="texte", x=15.6, y=1.68, t="$1+20\\times0{,}05=2$", c="te")]),
        "dem": dict(type="formule", copie=True, titre="Démonstration exigible : l'inégalité de Bernoulli", x=90, y=58, w=1100, lignes=[
            dict(lab="Propriété.", f="Soit $a\\geq0$. Pour $n\\in\\N$, $P(n)$ : « $(1+a)^n\\geq1+na$ ».", taille=31),
            dict(lab="Initialisation.", f="$(1+a)^0=1$ et $1+0\\times a=1$ : $1\\geq1$, $P(0)$ est vraie.", taille=31),
            dict(lab="Hérédité.", f="Soit $k\\in\\N$ tel que $(1+a)^k\\geq1+ka$.", m="hypothèse", taille=31),
            dict(f="$(1+a)^{k+1}\\geq(1+ka)(1+a)$", ind=True, hl=True, m="car $1+a>0$ !", taille=31),
            dict(f="$(1+ka)(1+a)=1+a+ka+ka^2=1+(k+1)a+ka^2$", ind=True, taille=31),
            dict(f="$ka^2\\geq0$, donc $1+(k+1)a+ka^2\\geq1+(k+1)a$", ind=True, taille=31),
            dict(f="$(1+a)^{k+1}\\geq1+(k+1)a$ : c'est $P(k+1)$.", ind=True, cadre=True, taille=31),
            dict(lab="Conclusion.", f="par récurrence, pour tout $n\\in\\N$, $(1+a)^n\\geq1+na$.", taille=31)]),
        "plus_b": dict(type="note", titre="Pour aller plus loin", cles=["moins", "positif"],
                       t="Hors programme : la même preuve marche pour $a\\geq-1$, car alors $1+a\\geq0$.", x=170, y=210, w=940),
    }),

    # ================================================================ VII. les pièges
    dict(id="pieges", chap="Les pièges classiques", fond="craie", humeur="tension",
         retenir="Initialiser au bon rang, utiliser l'hypothèse de récurrence, ne pas confondre $u_{k+1}$ et $u_k+1$.",
         beats=[
        "{pieges}Faisons le tour des pièges classiques. {pieges.1}Supposer ce qu'on veut démontrer : "
        "on l'a vu, on suppose P de k pour un k fixé, pas pour tout n.",
        "{pieges.2}Une hérédité qui n'utilise jamais l'hypothèse de récurrence. Si ton calcul de P de k plus un se passe de P de k, "
        "ce n'est pas une récurrence : soit une preuve directe était possible, soit il y a une erreur.",
        "{pieges.3}Oublier l'initialisation. Elle est souvent facile, mais elle rapporte des points. Et sans elle, on démontre des choses fausses. Écris-la toujours.",
        "{pieges.4}Confondre le terme d'indice k plus un, u k plus un, avec le terme u k auquel on ajoute un. Ce n'est pas du tout la même chose.",
        "{pieges.5}Et enfin, le mauvais rang de départ. Celui-là mérite un exemple.",
        "{-pieges}{tab2n}Compare deux puissance n et n au carré. {tab2n.1}Pour n égale zéro, un et deux, deux puissance n gagne, ou fait égalité. "
        "{tab2n.2}Pour n égale trois : huit contre neuf. Raté ! "
        "{tab2n.3}Puis, à partir de quatre : seize contre seize, trente-deux contre vingt-cinq, soixante-quatre contre trente-six. "
        "Deux puissance n repart devant, et ne se fait plus rattraper.",
        "{-tab2n}{rang}Donc on démontre : pour tout n supérieur ou égal à quatre, deux puissance n est supérieur ou égal à n au carré. "
        "{rang.1}Et on initialise à n zéro égale quatre : seize, supérieur ou égal à seize. {rang.m1}Surtout pas à zéro !",
        "{rang.2}Hérédité : si deux puissance k est supérieur ou égal à k au carré, alors deux puissance k plus un, c'est deux fois deux puissance k, "
        "donc c'est supérieur ou égal à deux k au carré. "
        "{rang.3}Il reste à montrer que deux k au carré est supérieur ou égal à k plus un, au carré. "
        "C'est-à-dire que k au carré, moins deux k, moins un, est positif.",
        "{rang.4}Or c'est k moins un, au carré, moins deux. Et pour k supérieur ou égal à quatre, k moins un, au carré, vaut au moins neuf. "
        "{rang.5}On enchaîne : deux puissance k plus un, supérieur ou égal à deux k au carré, supérieur ou égal à k plus un, au carré. "
        "Une chaîne d'inégalités : c'est le schéma standard.",
        "{-rang}",
    ], vis={
        "pieges": dict(type="liste", titre="Les pièges classiques", items=[
            "Supposer « $P(n)$ pour tout $n$ »", "Une hérédité qui n'utilise pas l'hypothèse",
            "Oublier l'initialisation", "Confondre $u_{k+1}$ et $u_k+1$", "Initialiser au mauvais rang"],
            marques=["!", "!", "!", "!", "!"], x=170, y=110, w=940),
        "tab2n": dict(type="formule", titre="Deux puissance n contre n au carré", x=130, y=150, w=1020, lignes=[
            dict(f="$2^0=1\\geq0^2$, $\\quad2^1=2\\geq1^2$, $\\quad2^2=4\\geq2^2$", ok=True, taille=40),
            dict(f="$2^3=8<9=3^2$", ko=True, taille=40),
            dict(f="$2^4=16\\geq4^2$, $\\quad2^5=32\\geq5^2$, $\\quad2^6=64\\geq6^2$", ok=True, taille=40)]),
        "rang": dict(type="formule", copie=True, titre="Pour tout $n\\geq4$ : $2^n\\geq n^2$", x=100, y=110, w=1080, lignes=[
            dict(lab="Initialisation", f="à $n_0=4$ : $2^4=16\\geq16=4^2$.", m="pas à $0$ !", taille=31),
            dict(lab="Hérédité.", f="Si $2^k\\geq k^2$ avec $k\\geq4$ : $2^{k+1}=2\\times2^k\\geq2k^2$.", taille=31),
            dict(f="Reste : $2k^2\\geq(k+1)^2\\iff k^2-2k-1\\geq0$", ind=True, taille=31),
            dict(f="$k^2-2k-1=(k-1)^2-2\\geq9-2>0$ car $k\\geq4$", ind=True, taille=31),
            dict(f="$2^{k+1}\\geq2k^2\\geq(k+1)^2$", ind=True, cadre=True, m="la chaîne d'inégalités", taille=31)]),
    }),

    # ================================================================ VIII. ce que la récurrence ne fait pas
    dict(id="limites", chap="Ce que la récurrence ne fait pas", fond="carnet", humeur="calme",
         retenir="On conjecture (premiers termes, tableur, Python), puis on prouve par récurrence. Pour réfuter, un contre-exemple suffit.",
         beats=[
        "{nefait}Trois limites à connaître. {nefait.1}La récurrence ne trouve pas la formule. Il faut la deviner, en calculant les premiers termes, "
        "avec un tableur ou Python, ou qu'elle soit donnée par l'énoncé. La récurrence sert à la prouver.",
        "{nefait.2}Elle ne s'applique qu'à des propriétés indexées par des entiers. Pour un réel x, on utilise d'autres outils, comme l'étude de fonction. "
        "{nefait.3}Et pour montrer qu'une propriété est fausse, un seul contre-exemple suffit.",
        "{-nefait}{devine}Un exemple de « deviner, puis prouver ». u zéro égale zéro, et u n plus un égale u n, plus deux n plus un. "
        "{devine.1}u un vaut zéro plus un : un. {devine.2}u deux : un plus trois, quatre. {devine.3}Puis neuf, {devine.4}seize.",
        "{devine.c}Des carrés ! {devine.ok}On conjecture que u n égale n au carré.",
        "{-devine}{prouve}Et on le prouve. {prouve.1}Initialisation : u zéro égale zéro, qui est bien zéro au carré. "
        "{prouve.2}Hérédité : si u k égale k au carré, alors u k plus un égale k au carré plus deux k plus un, c'est-à-dire k plus un, au carré. "
        "{prouve.3}Démontré.",
        "{-prouve}{fort}Pour aller plus loin, et hors programme : il existe des variantes, comme la récurrence forte, "
        "où l'on suppose toutes les propriétés de P de n zéro jusqu'à P de k pour prouver P de k plus un. Elles ne sont pas exigibles.",
        "{-fort}",
    ], vis={
        "nefait": dict(type="liste", titre="Ce que la récurrence ne fait pas", items=[
            "Elle ne trouve pas la formule : on la conjecture, puis elle la prouve",
            "Elle ne vaut que pour des propriétés d'entiers",
            "Pour réfuter, un contre-exemple suffit"], x=170, y=170, w=940),
        "devine": dict(type="illu", nom="suite", x=110, y=120, w=1060, h=520, termes=[0, 1, 4, 9, 16],
                       op=["+1", "+3", "+5", "+7"], f="$n^2$", fv=["$0^2$", "$1^2$", "$2^2$", "$3^2$", "$4^2$"]),
        "prouve": dict(type="formule", titre="Puis prouver", x=150, y=170, w=980, lignes=[
            dict(lab="Initialisation", f="$u_0=0=0^2$"),
            dict(lab="Hérédité", f="si $u_k=k^2$, alors $u_{k+1}=k^2+2k+1=(k+1)^2$", taille=38),
            dict(f="Pour tout $n\\in\\N$, $u_n=n^2$.", cadre=True)]),
        "fort": dict(type="note", titre="Pour aller plus loin", cles=["forte", "exigibles"],
                     t="Hors programme : la récurrence forte suppose $P(n_0)$, …, $P(k)$ pour prouver $P(k+1)$. Elle n'est pas exigible.",
                     x=170, y=200, w=940),
    }),

    # ================================================================ IX. exercice 1
    dict(id="exo1", chap="Exercice 1 · une formule à démontrer", fond="ardoise", humeur="tension", beats=[
        "{ex1}Place à l'entraînement. Premier exercice, pour démarrer. La suite u est définie par u zéro égale deux, "
        "et, pour tout n, u n plus un égale u n plus deux n plus trois.",
        "Trois questions. Un : calcule u un, u deux et u trois. Deux : démontre par récurrence que pour tout n, u n égale n plus un, au carré, plus un. "
        "Trois : déduis-en u dix.",
        "{-ex1}{pa1}À toi. Mets la vidéo sur pause, et rédige comme sur une copie, avec les quatre étapes.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Question un. u un égale deux, plus zéro, plus trois : cinq. "
        "{s11.2}u deux égale cinq, plus deux, plus trois : dix. {s11.3}u trois égale dix, plus quatre, plus trois : dix-sept.",
        "{-s11}{ex1c.q2}{s12}Question deux. {s12.1}On note P de n : « u n égale n plus un, au carré, plus un ». "
        "{s12.2}Initialisation : zéro plus un, au carré, plus un, ça fait deux. C'est bien u zéro.",
        "{s12.3}Hérédité : soit k tel que u k égale k plus un, au carré, plus un. "
        "{s12.4}Alors u k plus un égale u k, plus deux k plus trois. On remplace u k par l'hypothèse. "
        "{s12.5}On développe : k au carré, plus quatre k, plus cinq. "
        "{s12.6}Et k plus deux, au carré, plus un, c'est aussi k au carré plus quatre k plus cinq. C'est P de k plus un. "
        "{s12.7}Conclusion, par récurrence.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : u dix égale onze au carré, plus un. {s13.2}Cent vingt-deux. Sans calculer les dix termes !",
        "{-s13}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", etiquette="Exercice 1 · pour démarrer", titre="Une formule à démontrer",
                    enonce=["Soit $(u_n)$ définie par $u_0=2$ et, pour tout $n\\in\\N$, $u_{n+1}=u_n+2n+3$."],
                    questions=["Calculer $u_1$, $u_2$ et $u_3$.", "Démontrer par récurrence que pour tout $n\\in\\N$, $u_n=(n+1)^2+1$.",
                               "En déduire $u_{10}$."]),
        "pa1": dict(type="pause", t="Les trois premiers termes, la récurrence en quatre étapes, puis $u_{10}$."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", etiquette="Exercice 1", titre="Une formule à démontrer",
                     donnees=["$u_0=2$", "$u_{n+1}=u_n+2n+3$"],
                     questions=["$u_1$, $u_2$, $u_3$ ?", "$u_n=(n+1)^2+1$ ?", "$u_{10}$ ?"]),
        "s11": dict(type="formule", titre="1 · Les premiers termes", x=550, y=170, w=690, lignes=[
            dict(f="$u_1=2+0+3=5$", taille=42), dict(f="$u_2=5+2+3=10$", taille=42), dict(f="$u_3=10+4+3=17$", taille=42)]),
        "s12": dict(type="formule", copie=True, titre="2 · La récurrence", x=530, y=76, w=720, lignes=[
            dict(lab="Propriété.", f="$P(n)$ : « $u_n=(n+1)^2+1$ ».", taille=27),
            dict(lab="Initialisation.", f="$(0+1)^2+1=2=u_0$.", taille=27),
            dict(lab="Hérédité.", f="Soit $k\\in\\N$ tel que $u_k=(k+1)^2+1$.", taille=27),
            dict(f="$u_{k+1}=u_k+2k+3=(k+1)^2+1+2k+3$", ind=True, taille=27),
            dict(f="$u_{k+1}=k^2+4k+5$", ind=True, taille=27),
            dict(f="$(k+2)^2+1=k^2+4k+5$ : $P(k+1)$.", ind=True, cadre=True, taille=27),
            dict(lab="Conclusion.", f="par récurrence, $u_n=(n+1)^2+1$.", taille=27)]),
        "s13": dict(type="formule", titre="3 · Sans calculer dix termes", x=550, y=200, w=690, lignes=[
            dict(f="$u_{10}=(10+1)^2+1=11^2+1$", taille=40), dict(f="$u_{10}=122$", cadre=True, taille=44)]),
    }),

    # ================================================================ X. exercice 2 (type bac)
    dict(id="exo2", chap="Exercice 2 · type bac", fond="carnet", humeur="tension", beats=[
        "{ex2}Deuxième exercice, au format du bac. Une chaîne de vidéos compte cinq mille abonnés au départ. "
        "Chaque mois, elle perd vingt pour cent de ses abonnés, mais en gagne trois mille nouveaux.",
        "On note a n le nombre d'abonnés, en milliers, après n mois. Donc a zéro égale cinq, et a n plus un égale zéro virgule huit a n, plus trois.",
        "{-ex2}{ex2b}Quatre questions. {ex2b.1}Un : calcule a un et a deux. "
        "{ex2b.2}Deux : démontre par récurrence que pour tout n, cinq inférieur ou égal à a n, inférieur ou égal à a n plus un, inférieur ou égal à quinze. "
        "{ex2b.3}Trois : on pose v n égale a n moins quinze. Montre que v est géométrique, puis que a n égale quinze moins dix fois zéro virgule huit puissance n. "
        "{ex2b.4}Quatre : complète une fonction Python, pour trouver le premier mois où la chaîne dépasse quatorze mille abonnés.",
        "{-ex2b}{pa2}C'est un vrai sujet de bac. Prends le temps : mets sur pause, et rédige tout.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un. a un égale zéro virgule huit fois cinq, plus trois : sept. "
        "{s21.2}a deux égale zéro virgule huit fois sept, plus trois : huit virgule six.",
        "{-s21}{ex2c.q2}{s22}Question deux, la récurrence. {s22.1}On pose f de x égale zéro virgule huit x, plus trois. "
        "Elle est croissante sur R, car son coefficient, zéro virgule huit, est positif. "
        "{s22.2}Initialisation : a zéro égale cinq, a un égale sept, et cinq inférieur ou égal à cinq, inférieur ou égal à sept, inférieur ou égal à quinze. Vrai.",
        "{s22.3}Hérédité : supposons cinq inférieur ou égal à a k, inférieur ou égal à a k plus un, inférieur ou égal à quinze. "
        "{s22.4}f est croissante, donc on peut lui appliquer toute la chaîne. "
        "{s22.5}Or f de cinq vaut sept, et f de quinze vaut quinze. On obtient : sept inférieur ou égal à a k plus un, inférieur ou égal à a k plus deux, "
        "inférieur ou égal à quinze. {s22.6}Et comme cinq est inférieur à sept, c'est P de k plus un. Conclusion par récurrence.",
        "{-s22}{toile2}{toile2.1}{toile2.2}Regarde la toile d'araignée. {toile2.3}En escalier, les termes montent vers quinze… "
        "{toile2.4}sans jamais le dépasser. C'est exactement l'encadrement qu'on vient de démontrer.",
        "{-toile2}{ex2c.q3}{s23}Question trois : la technique de Première, la suite auxiliaire. "
        "{s23.1}v n plus un égale a n plus un, moins quinze. "
        "{s23.2}C'est-à-dire zéro virgule huit a n, plus trois, moins quinze : zéro virgule huit a n, moins douze. "
        "{s23.3}On factorise par zéro virgule huit : zéro virgule huit fois, a n moins quinze. C'est zéro virgule huit v n.",
        "{s23.4}Donc v est géométrique, de raison zéro virgule huit, et de premier terme v zéro égale cinq moins quinze, moins dix. "
        "{s23.5}Ainsi v n égale moins dix fois zéro virgule huit puissance n, et a n égale quinze, moins dix fois zéro virgule huit puissance n.",
        "{-s23}{ex2c.q4}{py2}Question quatre. Voici la fonction. {py2.l4}On veut le premier mois où a dépasse quatorze. "
        "Donc on continue tant que a est inférieur ou égal à quatorze : {py2.r1}la condition, c'est a inférieur ou égal à quatorze. "
        "{py2.l5}Et à chaque tour, on passe au mois suivant : {py2.r2}a prend la valeur zéro virgule huit fois a, plus trois.",
        "{py2.s}La fonction renvoie onze.",
        "{-py2}{s24}{s24.1}Vérifions avec la formule. a dix vaut environ treize virgule quatre-vingt-treize. "
        "{s24.2}Et a onze, environ quatorze virgule quatorze. {s24.3}La chaîne dépasse quatorze mille abonnés au bout de onze mois.",
        "{-s24}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Les abonnés d'une chaîne",
                    enonce=["Une chaîne de vidéos compte $5$ milliers d'abonnés au départ. Chaque mois, elle perd $20\\,\\%$ de ses abonnés "
                            "mais en gagne $3$ milliers.",
                            "On note $a_n$ le nombre d'abonnés, en milliers, après $n$ mois : $a_0=5$ et $a_{n+1}=0{,}8\\,a_n+3$."]),
        "ex2b": dict(type="exo", niveau="bac", etiquette="Exercice 2 · type bac", titre="Les abonnés d'une chaîne · questions",
                     questions=["Calculer $a_1$ et $a_2$.",
                                "Démontrer par récurrence que pour tout $n\\in\\N$ : $5\\leq a_n\\leq a_{n+1}\\leq15$.",
                                "On pose $v_n=a_n-15$. Montrer que $(v_n)$ est géométrique, puis que $a_n=15-10\\times0{,}8^n$.",
                                "Compléter une fonction Python qui renvoie le premier mois où $a_n>14$."]),
        "pa2": dict(type="pause", t="$a_1$ et $a_2$, l'encadrement par récurrence, la suite auxiliaire, l'algorithme de seuil."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", etiquette="Exercice 2 · type bac", titre="Les abonnés",
                     donnees=["$a_0=5$", "$a_{n+1}=0{,}8\\,a_n+3$"],
                     questions=["$a_1$, $a_2$ ?", "$5\\leq a_n\\leq a_{n+1}\\leq15$ ?", "$v_n=a_n-15$ ?", "Le seuil $14$ ?"]),
        "s21": dict(type="formule", titre="1 · Les premiers termes", x=550, y=200, w=690, lignes=[
            dict(f="$a_1=0{,}8\\times5+3=7$", taille=42), dict(f="$a_2=0{,}8\\times7+3=8{,}6$", taille=42)]),
        "s22": dict(type="formule", copie=True, titre="2 · L'encadrement", x=530, y=80, w=720, lignes=[
            dict(f="$f(x)=0{,}8x+3$ est croissante sur $\\R$ car $0{,}8>0$.", taille=27),
            dict(lab="Init.", f="$a_0=5$, $a_1=7$ : $5\\leq5\\leq7\\leq15$.", taille=27),
            dict(lab="Hérédité.", f="Si $5\\leq a_k\\leq a_{k+1}\\leq15$ :", taille=27),
            dict(f="$f(5)\\leq f(a_k)\\leq f(a_{k+1})\\leq f(15)$", ind=True, taille=27),
            dict(f="$f(5)=7$, $f(15)=15$ : $7\\leq a_{k+1}\\leq a_{k+2}\\leq15$", ind=True, taille=26),
            dict(f="donc $5\\leq a_{k+1}\\leq a_{k+2}\\leq15$ : $P(k+1)$.", ind=True, cadre=True, taille=27)]),
        "toile2": dict(type="graphe", titre="La toile d'araignée de $a_{n+1}=0{,}8\\,a_n+3$", x=570, y=120, w=650, h=520,
                       ax=dict(x=[0, 17], y=[0, 17], gx=[5, 10, 15], gy=[5, 10, 15], lx="$x$", ly="$y$"),
                       el=[dict(type="droite", pts=[[0, 3], [17, 16.6]], c="te", ep=3.2, lbl="$y=0{,}8x+3$", lp=[3.6, 8.2]),
                           dict(type="droite", pts=[[0, 0], [17, 17]], c="iv2", ep=2.2, lbl="$y=x$", lp=[12.3, 9.7]),
                           dict(type="toile", u=A_AB, c="sa", nlab=2, dur=4.5),
                           dict(type="droite", pts=[[0, 15], [17, 15]], c="ca", ep=2.4, tir=True, lbl="$y=15$", lp=[2.2, 16.0])]),
        "s23": dict(type="formule", titre="3 · La suite auxiliaire", x=550, y=110, w=690, lignes=[
            dict(f="$v_{n+1}=a_{n+1}-15$", taille=31),
            dict(f="$=0{,}8\\,a_n+3-15=0{,}8\\,a_n-12$", ind=True, taille=31),
            dict(f="$=0{,}8\\,(a_n-15)=0{,}8\\,v_n$", ind=True, taille=31),
            dict(f="géométrique de raison $0{,}8$, $v_0=5-15=-10$", txt=True),
            dict(f="$v_n=-10\\times0{,}8^n$ et $a_n=15-10\\times0{,}8^n$", cadre=True, taille=30)]),
        "py2": dict(type="code", titre="Python · l'algorithme de seuil", x=560, y=120, w=660, taille=27, lignes=[
            "def seuil():", "    n = 0", "    a = 5", "    while @1:", "        a = @2", "        n = n + 1", "    return n", "",
            "print(seuil())"], rep=["a <= 14", "0.8 * a + 3"], sortie="11"),
        "s24": dict(type="formule", titre="Vérification", x=550, y=180, w=690, lignes=[
            dict(f="$a_{10}=15-10\\times0{,}8^{10}\\approx13{,}93$", taille=36),
            dict(f="$a_{11}=15-10\\times0{,}8^{11}\\approx14{,}14>14$", taille=36),
            dict(f="au bout de $11$ mois", cadre=True, taille=38)]),
    }),

    # ================================================================ XI. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="craie", humeur="lumiere", beats=[
        "{carte}Récapitulons. Au centre, le principe : l'initialisation, et l'hérédité. "
        "{carte.1}Pour rédiger : la propriété, l'initialisation, l'hérédité avec l'hypothèse et le but, puis la conclusion. "
        "{carte.2}Pour les formules et les sommes : on remplace par l'hypothèse, on ajoute le terme suivant. "
        "{carte.3}Pour les inégalités : une fonction croissante conserve l'ordre, et l'inégalité de Bernoulli. "
        "{carte.4}Et les pièges : le rang de départ, l'hypothèse oubliée, et le terme suivant confondu avec le terme augmenté de un.",
        "{-carte}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Rédiger une récurrence complète, en quatre étapes. "
        "{bac.2}Démontrer une formule explicite. {bac.3}Démontrer une formule de somme. "
        "{bac.4}Encadrer une suite, ou montrer qu'elle est monotone, avec la croissance de f. "
        "{bac.5}Refaire seul la démonstration de l'inégalité de Bernoulli. {bac.6}Et compléter un algorithme de seuil en Python.",
        "Si tu sais faire ces six choses, ce chapitre est à toi. Les fiches, les QCM et les animations du chapitre t'attendent sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, le quiz t'attend juste après.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="RÉCURRENCE · initialisation + hérédité", branches=[
            dict(t="Rédiger", items=["la propriété $P(n)$", "l'initialisation", "l'hérédité : hypothèse et but", "la conclusion"]),
            dict(t="Formules et sommes", items=["remplacer par l'hypothèse", "ajouter le terme suivant", "$1+3+\\cdots+(2n-1)=n^2$"]),
            dict(t="Inégalités", items=["$f$ croissante conserve l'ordre", "encadrer, montrer la monotonie", "$(1+a)^n\\geq1+na$"]),
            dict(t="Pièges", items=["le bon rang $n_0$", "utiliser l'hypothèse", "$u_{k+1}\\neq u_k+1$"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Rédiger une récurrence en quatre étapes", "Démontrer une formule explicite", "Démontrer une formule de somme",
            "Encadrer une suite, montrer sa monotonie", "Refaire la démonstration de Bernoulli", "Compléter un algorithme de seuil"],
            marques=["✓"] * 6, x=170, y=96, w=940),
    }),
]

QUIZ = [
    dict(q="Dans une démonstration par récurrence, l'hérédité consiste à montrer que…",
         r=["P(n) est vraie pour tout n", "pour tout k ≥ n₀, si P(k) est vraie, alors P(k+1) est vraie", "P(n₀) et P(n₀+1) sont vraies"],
         ok=1, ex="L'hérédité est une implication : de P(k), supposée, on déduit P(k+1), pour tout k ≥ n₀.", voir="def_her"),
    dict(q="On a démontré l'hérédité de P(n) : « 2ⁿ est divisible par 3 ». On peut conclure…",
         r=["que P(n) est vraie pour tout n", "que P(n) est vraie à partir d'un certain rang", "rien : l'initialisation est fausse pour tout n"],
         ok=2, ex="2ⁿ n'est jamais divisible par 3. L'hérédité seule ne prouve rien : il faut un premier domino qui tombe.", voir="her3"),
    dict(q="n² + n + 41 est premier pour n = 0, 1, …, 39. Alors…",
         r=["il est premier pour tout n", "on ne peut rien conclure ; d'ailleurs 40² + 40 + 41 = 41²", "il suffit de vérifier n = 40 pour conclure"],
         ok=1, ex="Des vérifications ne remplacent pas une hérédité. Et 1 681 = 41 × 41 n'est pas premier.", voir="eul"),
    dict(q="Soit u₀ = 1 et uₙ₊₁ = 2uₙ + 3. Que vaut u₃ ?", r=["13", "29", "61"],
         ok=1, ex="u₁ = 5, u₂ = 13, u₃ = 29. On vérifie : 2³⁺² − 3 = 29.", voir="suite"),
    dict(q="Dans l'hérédité, on suppose que P(k) est vraie…",
         r=["pour tout entier k", "pour un entier k ≥ n₀ fixé", "pour k = n₀ uniquement"],
         ok=1, ex="On fixe un entier k ≥ n₀ quelconque ; supposer « pour tout k » reviendrait à supposer le résultat.", voir="piege_n"),
    dict(q="Pour passer de 1 + 3 + … + (2k − 1) à la somme au rang k + 1, on ajoute…",
         r=["2k − 1", "2k + 1", "2k + 3"], ok=1, ex="Le terme de rang k + 1 est 2(k + 1) − 1 = 2k + 1.", voir="som"),
    dict(q="f est croissante sur [0 ; 2] et 0 ≤ uₖ ≤ 2. On peut en déduire…",
         r=["0 ≤ f(uₖ) ≤ 2", "f(0) ≤ f(uₖ) ≤ f(2)", "f(2) ≤ f(uₖ) ≤ f(0)"],
         ok=1, ex="Une fonction croissante conserve l'ordre. Il faut ensuite comparer f(0) et f(2) aux bornes voulues.", voir="gr_f"),
    dict(q="Dans la démonstration de l'inégalité de Bernoulli, l'étape clé de l'hérédité est…",
         r=["multiplier (1 + a)ᵏ ≥ 1 + ka par 1 + a, qui est positif", "ajouter a aux deux membres", "élever au carré"],
         ok=0, ex="(1 + a)ᵏ⁺¹ ≥ (1 + ka)(1 + a) = 1 + (k + 1)a + ka² ≥ 1 + (k + 1)a. Multiplier par un positif conserve le sens.", voir="dem"),
    dict(q="2ⁿ ≥ n² est vraie pour n ≥ 4. Pour la démontrer par récurrence, on initialise à…",
         r=["n = 0", "n = 3", "n = 4"], ok=2, ex="Elle est fausse pour n = 3 (8 < 9) : on initialise au premier rang annoncé, n₀ = 4.", voir="rang"),
    dict(q="Une récurrence permet…",
         r=["de trouver une formule", "de prouver une formule conjecturée", "de prouver qu'une propriété est fausse"],
         ok=1, ex="On conjecture (calculs, Python), puis on prouve par récurrence. Pour réfuter, un contre-exemple suffit.", voir="nefait"),
]

CREDITS = [
    "Photos : dominos qui tombent, Kurt:S, CC BY 2.0 ; dominos prêts à tomber, Pauloleong2002, CC BY-SA 4.0.",
    "Portraits : Blaise Pascal, copie anonyme d'après François II Quesnel (domaine public) ; Giuseppe Peano, auteur inconnu (domaine public).",
    "Images trouvées sur Wikimedia Commons. Animations, schémas, graphiques et exercices : faits pour le site. "
    "Polices : Carnet Math (sous-ensemble de STIX Two Math), Caveat, Spectral, Archivo, JetBrains Mono, sous licence SIL OFL.",
]
