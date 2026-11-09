/* ===================== Chapitre 2 — Récursivité ===================== */
C("c2-somme", String.raw`
def somme(n):
    """Renvoie 0 + 1 + 2 + ... + n, pour n entier positif ou nul."""
    if n == 0:                  # cas de base : on connaît la réponse
        return 0
    return n + somme(n - 1)     # cas récursif : un problème plus petit

print(somme(4), somme(100))`, { out: "10 5050" });

C("c2-fact", String.raw`
def factorielle(n):
    """Renvoie n! = 1 x 2 x ... x n, avec 0! = 1."""
    if n == 0:
        return 1
    return n * factorielle(n - 1)

for k in range(6):
    print(k, factorielle(k))`, { out: "0 1\n1 1\n2 2\n3 6\n4 24\n5 120" });

C("c2-trace", String.raw`
def factorielle(n, prof=0):
    marge = "    " * prof
    print(marge + "appel factorielle(" + str(n) + ")")
    if n == 0:
        resultat = 1
    else:
        resultat = n * factorielle(n - 1, prof + 1)
    print(marge + "factorielle(" + str(n) + ") renvoie " + str(resultat))
    return resultat

factorielle(3)`, { out: String.raw`
appel factorielle(3)
    appel factorielle(2)
        appel factorielle(1)
            appel factorielle(0)
            factorielle(0) renvoie 1
        factorielle(1) renvoie 1
    factorielle(2) renvoie 2
factorielle(3) renvoie 6` });

C("c2-limite", String.raw`
import sys
print(sys.getrecursionlimit())     # 1000 par défaut

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

factorielle(5000)                  # 5001 appels imbriqués : trop !`, { out: "1000", err: "RecursionError: maximum recursion depth exceeded" });

C("c2-negatif", String.raw`
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

factorielle(-1)     # -1, -2, -3... n n'atteint jamais 0`, { err: "RecursionError: maximum recursion depth exceeded" });

C("c2-precondition", String.raw`
def factorielle(n):
    assert n >= 0, "n doit être un entier positif ou nul"
    if n == 0:
        return 1
    return n * factorielle(n - 1)

factorielle(-1)`, { err: "AssertionError: n doit être un entier positif ou nul" });

C("c2-iter", String.raw`
def factorielle_iter(n):
    resultat = 1
    for k in range(2, n + 1):
        resultat = resultat * k
    return resultat

print(factorielle_iter(5))
print(factorielle_iter(5000) > 10 ** 16000)   # aucun souci de pile`, { out: "120\nTrue" });

C("c2-fib", String.raw`
appels = 0

def fibonacci(n):
    global appels
    appels = appels + 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for n in [4, 10, 20, 30]:
    appels = 0
    print(n, fibonacci(n), appels)`, { out: "4 3 9\n10 55 177\n20 6765 21891\n30 832040 2692537" });

C("c2-memo", String.raw`
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:                     # chaque valeur n'est calculée qu'une fois
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(30), fibonacci_memo(100))`, { out: "832040 354224848179261915075" });

C("c2-puissance", String.raw`
def puissance(a, n):                 # a^n = a x a^(n-1) : n + 1 appels
    if n == 0:
        return 1
    return a * puissance(a, n - 1)

def puissance_rapide(a, n):          # l'exposant est divisé par 2 à chaque appel
    if n == 0:
        return 1
    m = puissance_rapide(a, n // 2)
    if n % 2 == 0:
        return m * m                 # a^n = (a^(n//2))^2 si n est pair
    return a * m * m                 # a^n = a x (a^(n//2))^2 si n est impair

print(puissance(2, 10), puissance_rapide(2, 10))
print(puissance_rapide(3, 13) == 3 ** 13)
print(puissance_rapide(2, 1000000).bit_length())   # 22 appels seulement`, { out: "1024 1024\nTrue\n1000001" });

C("c2-puissance-naive-ko", String.raw`
def puissance(a, n):
    if n == 0:
        return 1
    return a * puissance(a, n - 1)

puissance(2, 1000000)`, { err: "RecursionError: maximum recursion depth exceeded" });

C("c2-chaines", String.raw`
def longueur(ch):
    if ch == "":
        return 0
    return 1 + longueur(ch[1:])          # ch[1:] : la chaîne sans son 1er caractère

def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    if mot[0] != mot[-1]:
        return False
    return est_palindrome(mot[1:-1])     # on retire le premier et le dernier

def somme_liste(t, i=0):
    """Somme des éléments de t à partir de l'indice i."""
    if i == len(t):
        return 0
    return t[i] + somme_liste(t, i + 1)

print(longueur("récursif"), est_palindrome("kayak"), est_palindrome("nsi"))
print(somme_liste([4, 8, 15, 16, 23, 42]))`, { out: "8 True False\n108" });

C("c2-dicho", String.raw`
def recherche(t, x, g, d):
    """Indice de x dans le tableau trié t, entre les indices g et d inclus, ou -1."""
    if g > d:                            # zone de recherche vide
        return -1
    m = (g + d) // 2
    if t[m] == x:
        return m
    if t[m] < x:
        return recherche(t, x, m + 1, d)  # x ne peut être qu'à droite
    return recherche(t, x, g, m - 1)      # ou qu'à gauche

t = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(recherche(t, 13, 0, len(t) - 1), recherche(t, 4, 0, len(t) - 1))`, { out: "5 -1" });

C("c2-hanoi", String.raw`
def hanoi(n, depart, arrivee, intermediaire):
    """Affiche les déplacements pour amener n disques de depart vers arrivee."""
    if n == 0:
        return
    hanoi(n - 1, depart, intermediaire, arrivee)    # libérer le grand disque
    print("disque", n, ":", depart, "->", arrivee)  # le déplacer
    hanoi(n - 1, intermediaire, arrivee, depart)    # reposer les n-1 dessus

hanoi(3, "A", "C", "B")`, { out: String.raw`
disque 1 : A -> C
disque 2 : A -> B
disque 1 : C -> B
disque 3 : A -> C
disque 1 : B -> A
disque 2 : B -> C
disque 1 : A -> C` });

C("c2-sierpinski", String.raw`
def sierpinski(n):
    """Renvoie la liste des lignes d'un triangle de Sierpinski d'ordre n."""
    if n == 0:
        return ["*"]
    t = sierpinski(n - 1)
    marge = " " * 2 ** (n - 1)
    haut = [marge + ligne + marge for ligne in t]       # un triangle centré
    bas = [ligne + " " + ligne for ligne in t]          # deux triangles côte à côte
    return haut + bas

for ligne in sierpinski(3):
    print(ligne)`, { out: String.raw`
       *
      * *
     *   *
    * * * *
   *       *
  * *     * *
 *   *   *   *
* * * * * * * *` });

/* pièges */
C("c2-p-return", String.raw`
def somme(n):
    if n == 0:
        return 0
    n + somme(n - 1)          # le résultat est calculé... puis perdu

print(somme(3))`, { err: "TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'" });

C("c2-p-pair", String.raw`
def est_pair(n):
    if n == 0:
        return True
    return est_pair(n - 2)    # 3, 1, -1, -3... on saute par-dessus 0

est_pair(3)`, { err: "RecursionError: maximum recursion depth exceeded" });

C("c2-p-print", String.raw`
def double(n):
    if n == 0:
        print(0)              # affiche au lieu de renvoyer
    else:
        print(2 + double(n - 1))

double(2)`, { out: "0", err: "TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'" });

/* prédis la sortie */
C("c2-x1", String.raw`
def mystere(n):
    if n == 0:
        return 0
    return n % 10 + mystere(n // 10)

print(mystere(2026))`, { out: "10" });

C("c2-x2", String.raw`
def f(n):
    if n > 0:
        print(n, end=" ")
        f(n - 1)
        print(n, end=" ")

f(3)`, { out: "3 2 1 1 2 3" });

C("c2-x3", String.raw`
def g(t):
    if len(t) == 1:
        return t[0]
    m = g(t[1:])
    if t[0] > m:
        return t[0]
    return m

print(g([3, 9, 2, 7]))`, { out: "9" });

C("c2-x4", String.raw`
appels = 0

def fibo(n):
    global appels
    appels = appels + 1
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(5), appels)`, { out: "5 15" });

/* épreuve pratique 1 */
C("c2-ep1-fourni", String.raw`
def recherche_dicho(t, x, g, d):
    """t est un tableau trié dans l'ordre croissant.
    Renvoie un indice de x dans t entre g et d inclus, ou -1 s'il n'y est pas."""
    if ...:
        return -1
    m = (g + d) // 2
    if t[m] == x:
        return m
    elif t[m] < x:
        return recherche_dicho(t, x, ..., ...)
    else:
        return recherche_dicho(t, x, ..., ...)

def cherche(t, x):
    """Renvoie un indice de x dans le tableau trié t, ou -1."""
    ...`, { fichier: "dichotomie.py", run: false, trous: [4, 10, 12, 16] });

C("c2-ep1-bug", String.raw`
def recherche_bug(t, x, g, d):
    if g > d:
        return -1
    m = (g + d) // 2
    if t[m] == x:
        return m
    elif t[m] < x:
        return recherche_bug(t, x, m, d)      # m au lieu de m + 1
    else:
        return recherche_bug(t, x, g, m - 1)

print(recherche_bug([1, 3], 3, 0, 1))`, { fichier: "version_bugguee.py", err: "RecursionError: maximum recursion depth exceeded" });

C("c2-ep1-corr", String.raw`
def recherche_dicho(t, x, g, d):
    if g > d:
        return -1
    m = (g + d) // 2
    if t[m] == x:
        return m
    elif t[m] < x:
        return recherche_dicho(t, x, m + 1, d)
    else:
        return recherche_dicho(t, x, g, m - 1)

def cherche(t, x):
    return recherche_dicho(t, x, 0, len(t) - 1)

def test_cherche():
    t = [1, 4, 9, 16, 25, 36, 49]
    assert cherche(t, 16) == 3
    assert cherche(t, 1) == 0            # première case
    assert cherche(t, 49) == 6           # dernière case
    assert cherche(t, 10) == -1          # absent, entre deux valeurs
    assert cherche(t, 100) == -1         # absent, trop grand
    assert cherche([], 5) == -1          # tableau vide
    assert cherche([7], 7) == 0          # un seul élément
    assert cherche([1, 3], 3) == 1       # le cas qui piégeait la version bugguée
    grand = list(range(0, 2000000, 2))   # un million de nombres pairs
    assert cherche(grand, 1999998) == 999999

test_cherche()
print("tous les tests passent")`, { fichier: "dichotomie.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c2-ep2-fourni", String.raw`
def aplatir(liste):
    """Renvoie la liste des éléments de liste, dans l'ordre, en ouvrant
    les sous-listes à toutes les profondeurs.
    aplatir([1, [2, [3, 4]], 5]) doit renvoyer [1, 2, 3, 4, 5]."""
    resultat = []
    for x in liste:
        if isinstance(x, list):
            resultat.append(aplatir(x))
        else:
            resultat.append(x)
    return resultat

print(aplatir([1, [2, [3, 4]], 5]))`, { fichier: "aplatir.py", out: "[1, [2, [3, 4]], 5]" });

C("c2-ep2-corr", String.raw`
def aplatir(liste):
    resultat = []
    for x in liste:
        if isinstance(x, list):
            resultat.extend(aplatir(x))   # ou : resultat = resultat + aplatir(x)
        else:
            resultat.append(x)
    return resultat

def profondeur(liste):
    """1 pour une liste sans sous-liste, 1 + la plus grande profondeur
    de ses sous-listes sinon."""
    p = 0
    for x in liste:
        if isinstance(x, list):
            p = max(p, profondeur(x))
    return 1 + p

def somme_imbriquee(liste):
    s = 0
    for x in liste:
        if isinstance(x, list):
            s = s + somme_imbriquee(x)
        else:
            s = s + x
    return s

def test():
    assert aplatir([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert aplatir([]) == []
    assert aplatir([[[]]]) == []
    assert aplatir([[1], [2, [3]], [[[4]]]]) == [1, 2, 3, 4]
    assert profondeur([]) == 1
    assert profondeur([1, 2]) == 1
    assert profondeur([1, [2, [3, 4]], 5]) == 3
    assert somme_imbriquee([1, [2, [3, 4]], 5]) == 15

test()
print("tous les tests passent")`, { fichier: "aplatir.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c2-ecrit-corr", String.raw`
def vol(n):
    """Temps de vol de n : nombre d'étapes pour atteindre 1."""
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + vol(n // 2)
    return 1 + vol(3 * n + 1)

def altitude(n):
    """Plus grande valeur atteinte par la suite qui part de n."""
    if n == 1:
        return 1
    if n % 2 == 0:
        suivant = n // 2
    else:
        suivant = 3 * n + 1
    return max(n, altitude(suivant))

def vol_iter(n):
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes = etapes + 1
    return etapes

print(vol(6), vol(27), altitude(27), vol_iter(97))`, { out: "8 111 9232 118" });

C("c2-retenir", String.raw`
def f(n):
    if n == 0:            # 1. cas de base : réponse directe, sans appel
        return 1
    return n * f(n - 1)   # 2. cas récursif : appel sur un problème PLUS PETIT
                          # 3. on combine (n * ...) et on RENVOIE`, { run: false });

CH.push({
  id: "ch2", n: 2, court: "recursivite", fichier: "ch2_recursivite.py",
  titre: "Récursivité",
  rubrique: "Rubrique « Langages et programmation » : récursivité (lien avec « Algorithmique » : diviser pour régner, arbres, graphes)",
  accroche: "Une fonction qui s’appelle elle-même : cas de base, pile d’appels, RecursionError, coût, puissance rapide.",
  essentiel: [
    "Une fonction <b>récursive</b> s’appelle elle-même sur un problème <b>plus petit</b>.",
    "Elle a toujours au moins un <b>cas de base</b> (réponse directe, sans appel) et un <b>cas récursif</b> qui se rapproche du cas de base.",
    "Chaque appel est <b>empilé</b> sur la pile d’exécution avec ses propres variables, puis <b>dépilé</b> quand il renvoie son résultat.",
    "Trop d’appels imbriqués saturent la pile : Python lève <code>RecursionError</code> (limite par défaut : 1 000 niveaux).",
    "Le coût se compte en appels : <i>n</i> pour la factorielle, exponentiel pour Fibonacci naïf, environ log₂ <i>n</i> pour la puissance rapide."
  ],
  attendus: [
    "Écrire un programme récursif (le BO conseille des exemples de domaines variés).",
    "Analyser le fonctionnement d’un programme récursif : suivre les appels, prévoir la sortie, justifier qu’il se termine.",
    "Faire le lien avec la pile d’exécution, avec les structures récursives (listes, arbres) et avec la méthode « diviser pour régner ».",
    "Comparer le coût de deux algorithmes (passage de <i>n</i> à log₂ <i>n</i>, ou d’un coût exponentiel à un coût raisonnable)."
  ],
  idees: [
    { id: "i1", t: "Le principe : se ramener à un problème plus petit", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Une fonction est <b>récursive</b> lorsqu’elle s’appelle elle-même. Elle résout un problème en le ramenant au <b>même problème</b> sur une donnée plus petite, jusqu’à un cas assez simple pour être résolu directement.</p></div>
<p>Pour calculer 0 + 1 + … + <i>n</i>, il suffit de savoir calculer 0 + 1 + … + (<i>n</i> − 1) et d’ajouter <i>n</i>. Et pour <i>n</i> = 0, la réponse est 0, sans calcul.</p>
[[c2-somme]]
<p>Comme des poupées russes : pour ouvrir la plus grande, on ouvre celle qu’elle contient, et ainsi de suite jusqu’à la plus petite, qui ne s’ouvre pas. L’appel <code>somme(4)</code> attend <code>somme(3)</code>, qui attend <code>somme(2)</code>… jusqu’à <code>somme(0)</code> qui répond 0 ; les réponses remontent alors : 0, 1, 3, 6, 10.</p>` },

    { id: "i2", t: "Cas de base et cas récursif : la méthode en trois questions", h: `
<p>Beaucoup de définitions mathématiques sont déjà récursives. La factorielle : 0! = 1 et, pour <i>n</i> ≥ 1, <i>n</i>! = <i>n</i> × (<i>n</i> − 1)!. Le code la recopie presque mot pour mot :</p>
[[c2-fact]]
<div class="boite retenir-b"><div class="lab"># méthode pour écrire une fonction récursive</div>
<ol><li><b>Le cas de base</b> : quelle est la plus petite donnée possible, et sa réponse ? (<i>n</i> = 0, liste vide, chaîne vide, un seul élément…)</li>
<li><b>La réduction</b> : comment se ramener à une donnée plus petite ? (<i>n</i> − 1, <i>n</i> // 2, la liste sans son premier élément…)</li>
<li><b>La combinaison</b> : en <b>supposant</b> que l’appel récursif renvoie la bonne réponse pour la donnée plus petite, comment obtenir la réponse pour la donnée entière ?</li></ol>
<p>Ce « supposer que l’appel marche » est le cœur de la récursivité : c’est le même raisonnement qu’une démonstration par récurrence en mathématiques.</p></div>` },

    { id: "i3", t: "La pile d’exécution", h: `
<p>Quand une fonction en appelle une autre (ou s’appelle elle-même), l’appel en cours est <b>mis en attente</b>. Python range dans une zone de mémoire appelée <b>pile d’exécution</b> (ou pile d’appels) un <b>cadre</b> par appel en cours : ses paramètres, ses variables locales et l’endroit où reprendre.</p>
<ul><li><b>Descente</b> : chaque nouvel appel <b>empile</b> un cadre. Les variables <code>n</code> de chaque appel sont <b>différentes</b>.</li>
<li><b>Remontée</b> : quand un appel renvoie son résultat, son cadre est <b>dépilé</b> et l’appel du dessous reprend là où il s’était arrêté.</li></ul>
<p>Avance pas à pas pour voir les cadres s’empiler puis se dépiler :</p>
[[w-pile-appels|fact]]
<p>On peut aussi « voir » la pile en affichant les appels avec une marge proportionnelle à la profondeur :</p>
[[c2-trace]]
<p>La pile est exactement la structure du chapitre 3 : le dernier appel commencé est le premier terminé (LIFO).</p>` },

    { id: "i4", t: "Terminaison et RecursionError", h: `
<p>Une fonction récursive <b>se termine</b> si chaque chaîne d’appels finit par atteindre un cas de base. Pour le justifier, on exhibe une quantité entière positive qui <b>diminue strictement</b> à chaque appel (on parle de <b>variant</b>) : ici <code>n</code>, qui passe à <code>n − 1</code> et s’arrête à 0.</p>
<p>La pile d’exécution a une taille limitée. Python refuse plus de 1 000 niveaux d’appels imbriqués par défaut et lève <code>RecursionError</code>, même si la fonction est juste :</p>
[[c2-limite]]
<p>Si le cas de base n’est jamais atteint, on obtient la même erreur : c’est l’équivalent récursif d’une boucle infinie.</p>
[[c2-negatif]]
<p>Pour s’en protéger, on écrit la <b>précondition</b> avec une assertion (chapitre 4) :</p>
[[c2-precondition]]
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p><code>sys.setrecursionlimit(10000)</code> relève la limite, mais la pile réelle du système peut alors déborder et faire planter Python : c’est une rustine, pas une solution. Contrairement à d’autres langages, Python n’optimise pas les appels récursifs terminaux.</p></div>` },

    { id: "i5", t: "Récursif ou itératif ?", h: `
<p>Tout algorithme récursif peut s’écrire avec des boucles (au besoin en gérant soi-même une pile), et inversement. La version itérative de la factorielle n’empile aucun cadre :</p>
[[c2-iter]]
<div class="tab-wrap"><table><tr><th></th><th>récursif</th><th>itératif</th></tr>
<tr><td>lisibilité</td><td>très proche d’une définition mathématique ou d’une structure récursive (arbre, liste chaînée)</td><td>naturel pour un parcours simple</td></tr>
<tr><td>mémoire</td><td>un cadre de pile par appel en cours</td><td>quelques variables</td></tr>
<tr><td>limite en Python</td><td>environ 1 000 appels imbriqués</td><td>aucune</td></tr></table></div>
<p>À l’écrit, on te demande souvent l’un <b>puis</b> l’autre : sache passer de <code>return n * f(n - 1)</code> à une boucle qui accumule le résultat.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1958 <b>·</b></span> John McCarthy conçoit <b>LISP</b>, un langage où la récursivité est l’outil central.<br><span class="commit">1960 <b>·</b></span> <b>ALGOL 60</b> autorise les procédures récursives, qui s’appuient sur une pile d’exécution.</p></div>` },

    { id: "i6", t: "Plusieurs appels : Fibonacci et l’arbre d’appels", h: `
<p>La suite de Fibonacci est définie par F(0) = 0, F(1) = 1 et F(<i>n</i>) = F(<i>n</i> − 1) + F(<i>n</i> − 2). La traduction directe fait <b>deux</b> appels récursifs : les appels forment un <b>arbre</b>.</p>
[[c2-fib]]
<p>Le nombre d’appels explose : 2 692 537 appels pour F(30), parce que les mêmes valeurs sont recalculées encore et encore (F(28) est calculé 2 fois, F(27) 3 fois, F(26) 5 fois…). Le coût est <b>exponentiel</b>. Dans le schéma, choisis <code>fibonacci(4)</code> : l’arbre se construit pendant que la pile monte et descend.</p>
[[w-pile-appels|fib]]
<p>La profondeur de la pile, elle, ne dépasse pas <i>n</i> : l’arbre est large, pas profond.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin : mémoïsation</div><p>On mémorise chaque résultat dans un dictionnaire pour ne le calculer qu’une fois. C’est le point de départ de la <b>programmation dynamique</b> (au programme, chapitre à venir).</p>[[c2-memo]]</div>` },

    { id: "i7", t: "Diviser l’exposant par 2 : la puissance rapide", h: `
<p>Pour calculer a<sup>n</sup>, la méthode naïve (a<sup>n</sup> = a × a<sup>n−1</sup>) fait <i>n</i> + 1 appels. Or a<sup>10</sup> = (a<sup>5</sup>)², a<sup>5</sup> = a × (a<sup>2</sup>)², a<sup>2</sup> = (a<sup>1</sup>)², a<sup>1</sup> = a × (a<sup>0</sup>)² : en <b>divisant l’exposant par 2</b> à chaque appel, on n’en fait que 5.</p>
[[c2-puissance]]
<div class="tab-wrap"><table><tr><th>exposant n</th><th>appels (naïf)</th><th>appels (rapide)</th></tr>
<tr><td>10</td><td>11</td><td>5</td></tr><tr><td>1 000</td><td>1 001</td><td>11</td></tr><tr><td>1 000 000</td><td>RecursionError</td><td>21</td></tr></table></div>
<p>Le nombre d’appels de la version rapide vaut ⌊log₂ <i>n</i>⌋ + 2 pour <i>n</i> ≥ 1 : c’est un coût <b>logarithmique</b>. Le programme insiste sur ce passage de <i>n</i> à log₂ <i>n</i>. C’est aussi un premier exemple de <b>diviser pour régner</b>. (Le dernier calcul ci-dessus, 2<sup>1 000 000</sup>, demande 21 appels.)</p>
[[c2-puissance-naive-ko]]` },

    { id: "i8", t: "Récursivité sur les chaînes et les tableaux", h: `
<p>Une chaîne ou une liste peut se voir récursivement : « vide », ou « un premier élément suivi du reste ». D’où des fonctions très courtes :</p>
[[c2-chaines]]
<p>Le découpage <code>ch[1:]</code> crée une <b>copie</b> à chaque appel, ce qui coûte du temps. Pour les tableaux, on préfère passer un <b>indice</b> en paramètre (comme <code>somme_liste</code>), ce qui évite toute copie. C’est ainsi qu’on écrit la <b>recherche dichotomique</b> de Première en version récursive :</p>
[[c2-dicho]]
<p>Le variant est la taille de la zone <code>d − g + 1</code>, divisée par deux environ à chaque appel : environ 20 appels suffisent pour un tableau d’un million d’éléments.</p>` },

    { id: "i9", t: "Des exemples de domaines variés : Hanoï et fractales", h: `
<p>Les <b>tours de Hanoï</b> : déplacer une pile de <i>n</i> disques d’un piquet à un autre, un disque à la fois, sans jamais poser un disque sur un plus petit. La solution récursive tient en trois lignes : déplacer les <i>n</i> − 1 disques du dessus sur le piquet intermédiaire, déplacer le grand, reposer les <i>n</i> − 1 dessus.</p>
[[c2-hanoi]]
<p>Il faut 2<sup>n</sup> − 1 déplacements (7 pour 3 disques, 1 023 pour 10). Le casse-tête a été publié en 1883 par le mathématicien français Édouard Lucas.</p>
<p>Les <b>fractales</b> sont des figures qui contiennent des copies réduites d’elles-mêmes : la récursivité les dessine naturellement. Version texte du triangle de Sierpinski :</p>
[[c2-sierpinski]]
<p>Le module <code>turtle</code> permet de dessiner de la même façon le flocon de von Koch ou un arbre fractal : chaque branche porte deux branches plus petites. Plus tard, tu retrouveras la récursivité partout : arbres, parcours de graphes, tri fusion.</p>` }
  ],
  pieges: [
    { t: "Oublier le return devant l’appel récursif", h: `[[c2-p-return]]<p>Sans <code>return</code>, la fonction renvoie <code>None</code>. L’appel du dessus essaie alors de calculer <code>2 + None</code>. Le cas récursif doit <b>renvoyer</b> la combinaison : <code>return n + somme(n - 1)</code>.</p>` },
    { t: "Un cas de base jamais atteint", h: `[[c2-p-pair]]<p>Avec un pas de 2, un nombre impair saute par-dessus 0. Il faut un cas de base pour 1 (<code>if n == 1: return False</code>) ou un test <code>n &lt;= 1</code>. Vérifie toujours que <b>toutes</b> les valeurs atteignent un cas de base.</p>` },
    { t: "Afficher au lieu de renvoyer", h: `[[c2-p-print]]<p><code>print</code> montre une valeur à l’écran mais la fonction renvoie <code>None</code>. Une fonction récursive qui calcule doit <b>renvoyer</b> ; on affiche seulement le résultat final.</p>` },
    { t: "Croire que les variables sont partagées entre les appels", h: `<p>Chaque appel a ses propres variables locales : modifier <code>n</code> dans un appel ne change pas le <code>n</code> de l’appel qui attend. En revanche, une <b>liste</b> passée en paramètre est le même objet pour tous les appels : la modifier (avec <code>append</code>, <code>pop</code>) se voit partout.</p>` },
    { t: "Écrire Fibonacci naïf pour de grands n", h: `<p>Le résultat est juste, mais le temps est exponentiel : F(40) demande plus de 300 millions d’appels. À l’écrit, si on te demande « que peut-on reprocher à cette fonction ? », la réponse attendue est : des calculs redondants, un coût exponentiel, et la solution est la mémoïsation.</p>` }
  ],
  retenir: `
<h2>Le squelette</h2>
[[c2-retenir]]
<h2>Vocabulaire</h2>
<div class="tab-wrap"><table><tr><th>mot</th><th>sens</th></tr>
<tr><td>fonction récursive</td><td>fonction qui s’appelle elle-même</td></tr>
<tr><td>cas de base</td><td>donnée pour laquelle la réponse est directe, sans appel récursif</td></tr>
<tr><td>cas récursif</td><td>appel sur une donnée plus petite, puis combinaison</td></tr>
<tr><td>pile d’exécution</td><td>mémoire des appels en cours : un cadre par appel (paramètres, variables locales)</td></tr>
<tr><td>variant</td><td>entier positif qui diminue strictement à chaque appel : prouve la terminaison</td></tr>
<tr><td>RecursionError</td><td>trop d’appels imbriqués (limite 1 000 par défaut) ou cas de base jamais atteint</td></tr></table></div>
<h2>Coûts à connaître</h2>
<div class="tab-wrap"><table><tr><th>fonction</th><th>nombre d’appels</th><th>coût</th></tr>
<tr><td>factorielle(n), somme(n)</td><td>n + 1</td><td>linéaire</td></tr>
<tr><td>fibonacci(n) naïf</td><td>2 F(n+1) − 1 (2 692 537 pour n = 30)</td><td>exponentiel</td></tr>
<tr><td>puissance rapide</td><td>⌊log₂ n⌋ + 2</td><td>logarithmique</td></tr>
<tr><td>dichotomie sur n éléments</td><td>environ log₂ n</td><td>logarithmique</td></tr>
<tr><td>hanoï(n)</td><td>2ⁿ − 1 déplacements</td><td>exponentiel</td></tr></table></div>
<h2>Les réflexes</h2>
<ul><li>Écrire le cas de base <b>en premier</b>.</li><li>Vérifier que <b>chaque</b> appel se rapproche du cas de base (variant).</li><li><code>return</code> devant la combinaison.</li><li>Pour suivre un programme récursif : dessiner la pile (ou l’arbre) des appels, la descente puis la remontée.</li><li>Deux appels récursifs = un arbre d’appels : attention aux calculs répétés.</li></ul>`,
  predis: [
    { code: "c2-x1", niv: "facile", rep: "La fonction additionne le dernier chiffre (<code>n % 10</code>) et la somme des chiffres du reste (<code>n // 10</code>) : 6 + 2 + 0 + 2 + 0 = 10. C’est la somme des chiffres." },
    { code: "c2-x2", niv: "moyen", rep: "Chaque appel affiche <code>n</code> à la <b>descente</b> (avant l’appel) et à la <b>remontée</b> (après). Descente : 3 2 1 ; l’appel f(0) n’affiche rien ; remontée : 1 2 3." },
    { code: "c2-x3", niv: "moyen", rep: "<code>g</code> renvoie le maximum : celui du premier élément et du maximum du reste. g([7]) = 7, g([2, 7]) = 7, g([9, 2, 7]) = 9, g([3, 9, 2, 7]) = 9." },
    { code: "c2-x4", niv: "difficile", rep: "F(5) = 5. Nombre d’appels C(n) = C(n−1) + C(n−2) + 1 avec C(0) = C(1) = 1 : C(2) = 3, C(3) = 5, C(4) = 9, C(5) = 15." }
  ],
  ep: [
    { titre: "Recherche dichotomique récursive", enonce: `<p>La recherche dichotomique fait partie des algorithmes « à savoir écrire ». On la veut ici en version récursive.</p>[[c2-ep1-fourni]]`,
      questions: [
        { q: "Compléter <code>recherche_dicho</code> (lignes 4, 10 et 12).", c: `<p>Ligne 4 : <code>g &gt; d</code> (zone vide). Ligne 10 : <code>m + 1, d</code>. Ligne 12 : <code>g, m - 1</code>. On <b>exclut</b> <code>m</code>, déjà testé : c’est ce qui garantit que la zone rétrécit.</p>` },
        { q: "Compléter la fonction <code>cherche(t, x)</code>, qui appelle <code>recherche_dicho</code> sur tout le tableau.", c: `<p><code>return recherche_dicho(t, x, 0, len(t) - 1)</code>. Une telle fonction « enveloppe » cache les paramètres techniques <code>g</code> et <code>d</code> à l’utilisateur.</p>` },
        { q: "Un camarade a écrit la version ci-dessous. Exécuter l’appel proposé, expliquer l’erreur obtenue et la corriger.", code: "[[c2-ep1-bug]]", c: `<p>Avec <code>[1, 3]</code>, g = 0, d = 1, m = 0 et t[0] = 1 &lt; 3 : l’appel suivant est <code>recherche_bug(t, 3, 0, 1)</code>, <b>identique</b> au premier. La zone ne rétrécit pas, le cas de base n’est jamais atteint : <code>RecursionError</code>. Il faut <code>m + 1</code>.</p>` },
        { q: "Écrire une fonction <code>test_cherche()</code> avec au moins six assertions, dont des cas limites.", c: `[[c2-ep1-corr]]` },
        { q: "À l’oral : pourquoi cette fonction se termine-t-elle ? Combien d’appels au maximum pour un tableau d’un million d’éléments ?", c: `<p>La taille <code>d − g + 1</code> de la zone est un entier positif qui diminue strictement (elle est au moins divisée par deux) ; quand elle devient nulle, <code>g &gt; d</code> et on s’arrête. Un million ≈ 2²⁰ : une vingtaine d’appels au plus (log₂ <i>n</i>), contre un million de comparaisons pour une recherche séquentielle.</p>` }
      ] },
    { titre: "Aplatir des listes imbriquées", enonce: `<p>Une liste peut contenir des listes, qui contiennent des listes… La fonction fournie doit « aplatir » une telle liste. <code>isinstance(x, list)</code> vaut True si <code>x</code> est une liste.</p>[[c2-ep2-fourni]]`,
      questions: [
        { q: "Exécuter le programme. Le résultat est-il conforme à la documentation ? Corriger la fonction.", c: `<p>On obtient <code>[1, [2, [3, 4]], 5]</code> : <code>append</code> ajoute la liste renvoyée <b>comme un seul élément</b>. Il faut ajouter ses éléments un par un : <code>resultat.extend(aplatir(x))</code> ou <code>resultat = resultat + aplatir(x)</code>.</p>` },
        { q: "Où est le cas de base de cette fonction récursive ?", c: `<p>Il est implicite : une liste qui ne contient <b>aucune sous-liste</b> (ou la liste vide) ne déclenche aucun appel récursif ; la boucle se termine et la fonction renvoie. Les appels portent sur des listes strictement moins imbriquées.</p>` },
        { q: "Écrire une fonction récursive <code>profondeur(liste)</code> : 1 pour une liste sans sous-liste (y compris la liste vide), sinon 1 + la plus grande profondeur de ses sous-listes.", c: `<p>On garde le maximum des profondeurs des sous-listes rencontrées, puis on ajoute 1.</p>` },
        { q: "Écrire <code>somme_imbriquee(liste)</code> qui additionne tous les nombres d’une liste imbriquée, puis un jeu de tests pour les trois fonctions.", c: `[[c2-ep2-corr]]` }
      ] }
  ],
  ecrit: { titre: "La suite de Syracuse", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>On part d’un entier <i>n</i> ≥ 1. S’il est pair, on le divise par 2 ; s’il est impair, on le multiplie par 3 et on ajoute 1. On recommence avec le nombre obtenu. La <b>conjecture de Syracuse</b> affirme qu’on finit toujours par atteindre 1. Le <b>temps de vol</b> de <i>n</i> est le nombre d’étapes nécessaires pour atteindre 1 ; l’<b>altitude</b> est la plus grande valeur rencontrée.</p>`,
    questions: [
      { q: "Écrire la suite des valeurs obtenues en partant de 6. Donner son temps de vol et son altitude.", pts: "0,5 pt", c: `<p>6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 : <b>8 étapes</b>, altitude <b>16</b>.</p>` },
      { q: "Écrire une fonction <b>récursive</b> <code>vol(n)</code> qui renvoie le temps de vol de <code>n</code>.", pts: "1,5 pt", c: `<p>Cas de base : <code>vol(1) = 0</code>. Sinon, une étape de plus que le temps de vol du nombre suivant : <code>return 1 + vol(n // 2)</code> si <code>n</code> est pair, <code>return 1 + vol(3 * n + 1)</code> sinon. Utiliser <code>//</code> pour garder un entier.</p>` },
      { q: "Identifier le cas de base et le cas récursif. Peut-on prouver que <code>vol(n)</code> se termine pour tout <i>n</i> ? Expliquer.", pts: "1 pt", c: `<p>Contrairement à la factorielle, on ne connaît <b>aucun variant</b> : le nombre suivant peut être plus grand (3n + 1). Prouver que <code>vol</code> termine pour tout <i>n</i> reviendrait à démontrer la conjecture de Syracuse, qui reste un problème ouvert. On sait seulement, par des calculs sur ordinateur, qu’elle est vraie pour un très grand nombre d’entiers.</p>` },
      { q: "On sait que <code>vol(27)</code> vaut 111. Combien de cadres la pile d’exécution contient-elle au maximum pendant ce calcul ? Python peut-il faire ce calcul ?", pts: "1 pt", c: `<p>Les appels vol(27), vol(82), …, vol(1) sont tous en attente en même temps : 111 + 1 = <b>112 cadres</b>. C’est bien en dessous de la limite par défaut de 1 000 : aucun problème.</p>` },
      { q: "Écrire une fonction récursive <code>altitude(n)</code>. On pourra utiliser <code>max(a, b)</code>.", pts: "1 pt", c: `<p>Cas de base : altitude(1) = 1. Sinon, le maximum entre <code>n</code> et l’altitude du nombre suivant. On trouve altitude(27) = 9 232.</p>` },
      { q: "Écrire une version itérative <code>vol_iter(n)</code>.", pts: "1 pt", c: `<p>Une boucle <code>while n != 1</code> qui remplace <code>n</code> par le suivant et compte les étapes.</p>[[c2-ecrit-corr]]` }
    ],
    methode: `<p>À l’écrit, la récursivité tombe souvent sous la forme : écrire la fonction, identifier le cas de base, justifier la terminaison, dessiner la pile ou l’arbre d’appels pour une petite valeur, puis réécrire en itératif. Soigne le vocabulaire (« cas de base », « appel récursif », « pile d’exécution ») : la maîtrise de la langue compte pour 2 points sur 20 à partir de la session 2027.</p>` },
  qcm: [
    { q: "Qu’est-ce qu’une fonction récursive ?", c: ["Une fonction qui contient une boucle", "Une fonction qui s’appelle elle-même", "Une fonction sans paramètre", "Une fonction qui renvoie une liste"], a: 1, e: "Elle résout un problème en s’appelant sur une donnée plus petite.", ref: "i1" },
    { q: "Que manque-t-il le plus souvent à une fonction récursive qui ne s’arrête pas ?", c: ["Un print", "Un cas de base atteignable", "Une boucle for", "Une variable globale"], a: 1, e: "Sans cas de base atteint, les appels s’enchaînent jusqu’à la RecursionError.", ref: "i2" },
    { q: "Que vaut <code>factorielle(4)</code> avec la définition du cours ?", c: ["4", "10", "24", "120"], a: 2, e: "4 × 3 × 2 × 1 = 24.", ref: "i2" },
    { q: "Lors de l’appel <code>factorielle(3)</code>, combien de cadres la pile contient-elle au maximum ?", c: ["1", "3", "4", "6"], a: 2, e: "factorielle(3), (2), (1) et (0) sont en attente en même temps : 4 cadres.", ref: "i3" },
    { q: "Que contient un cadre de la pile d’exécution ?", c: ["Le code source du programme", "Les paramètres et variables locales d’un appel en cours", "Toutes les variables globales", "Le résultat final"], a: 1, e: "Chaque appel a son propre cadre ; les variables de deux appels sont distinctes.", ref: "i3" },
    { q: "Quelle est la limite par défaut du nombre d’appels imbriqués en Python ?", c: ["100", "1 000", "65 536", "Il n’y en a pas"], a: 1, e: "<code>sys.getrecursionlimit()</code> renvoie 1000 ; au-delà : RecursionError.", ref: "i4" },
    { q: "Comment justifier qu’une fonction récursive se termine ?", c: ["Elle contient un return", "On trouve un entier positif qui diminue strictement à chaque appel", "On l’exécute une fois", "Elle a moins de 10 lignes"], a: 1, e: "Un variant entier positif strictement décroissant ne peut pas décroître indéfiniment.", ref: "i4" },
    { q: "Combien d’appels fait <code>fibonacci(4)</code> (version naïve à deux appels) ?", c: ["4", "5", "9", "16"], a: 2, e: "C(4) = C(3) + C(2) + 1 = 5 + 3 + 1 = 9.", ref: "i6" },
    { q: "Pourquoi la version naïve de Fibonacci est-elle lente ?", c: ["Elle utilise des flottants", "Elle recalcule de nombreuses fois les mêmes valeurs", "Elle dépasse toujours la limite de pile", "Python ne gère pas l’addition récursive"], a: 1, e: "L’arbre d’appels contient des sous-arbres identiques : coût exponentiel.", ref: "i6" },
    { q: "Combien d’appels fait <code>puissance_rapide(2, 10)</code> ?", c: ["3", "5", "10", "11"], a: 1, e: "Exposants 10 → 5 → 2 → 1 → 0 : 5 appels.", ref: "i7" },
    { q: "Quel est l’ordre de grandeur du nombre d’appels de la puissance rapide pour un exposant n ?", c: ["n", "n²", "log₂ n", "2ⁿ"], a: 2, e: "L’exposant est divisé par 2 à chaque appel : environ log₂ n appels.", ref: "i7" },
    { q: "Sans <code>return</code> devant le cas récursif (<code>n + somme(n - 1)</code>), on obtient…", c: ["le bon résultat", "une TypeError (on ajoute un entier et None)", "une boucle infinie", "une SyntaxError"], a: 1, e: "La fonction renvoie None ; l’appel du dessus calcule <code>n + None</code>.", ref: "i2" },
    { q: "Combien de déplacements pour résoudre les tours de Hanoï à 4 disques ?", c: ["8", "15", "16", "31"], a: 1, e: "2⁴ − 1 = 15.", ref: "i9" }
  ],
  cartes: [
    { r: "Fonction récursive", v: "Fonction qui s’appelle elle-même sur une donnée plus petite." },
    { r: "Cas de base", v: "Donnée pour laquelle la fonction répond directement, sans appel récursif (n = 0, liste vide…)." },
    { r: "Les 3 questions pour écrire une fonction récursive", v: "1. Cas de base ? 2. Comment réduire la donnée ? 3. Comment combiner le résultat de l’appel ?" },
    { r: "Pile d’exécution", v: "Mémoire des appels en cours : un cadre par appel (paramètres, variables locales, point de reprise). Empilé à l’appel, dépilé au return." },
    { r: "RecursionError", v: "Trop d’appels imbriqués (limite par défaut 1 000) ou cas de base jamais atteint." },
    { r: "Variant", v: "Entier positif qui diminue strictement à chaque appel : il prouve que la fonction se termine." },
    { r: "Factorielle récursive", v: "<code>return 1</code> si n == 0, sinon <code>return n * factorielle(n - 1)</code>." },
    { r: "Nombre d’appels de fibonacci(n) naïf", v: "2 F(n+1) − 1 : 9 pour n = 4, 2 692 537 pour n = 30. Coût exponentiel." },
    { r: "Puissance rapide", v: "m = a^(n//2) ; renvoyer m×m si n pair, a×m×m sinon. Environ log₂ n appels." },
    { r: "Mémoïsation", v: "Mémoriser les résultats déjà calculés (dictionnaire) pour ne pas les recalculer. Base de la programmation dynamique." },
    { r: "Tours de Hanoï", v: "Déplacer n−1 disques, le grand, puis n−1 disques : 2ⁿ − 1 déplacements. Édouard Lucas, 1883." },
    { r: "Récursif → itératif", v: "Toujours possible (au besoin avec une pile explicite). L’itératif évite la limite de pile." },
    { r: "LISP", v: "Langage de John McCarthy (1958), fondé sur la récursivité." }
  ]
});
