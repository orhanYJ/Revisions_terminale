/* ===================== Diviser pour régner ===================== */
C("dpr-max", String.raw`
def maximum(t, g, d):
    """Plus grand élément de t entre les indices g et d inclus (g <= d)."""
    if g == d:                       # un seul élément : c'est lui
        return t[g]
    m = (g + d) // 2                 # 1. diviser en deux moitiés
    a = maximum(t, g, m)             # 2. régner : résoudre chaque moitié
    b = maximum(t, m + 1, d)
    if a > b:                        # 3. combiner les deux réponses
        return a
    return b

t = [3, 41, 7, 26, 15, 9]
print(maximum(t, 0, len(t) - 1))`, { out: "41" });

C("dpr-dicho", String.raw`
appels = 0

def dicho(t, x, g, d):
    """Indice de x dans le tableau trié t entre g et d inclus, ou -1."""
    global appels
    appels = appels + 1
    if g > d:                        # plus rien à chercher
        return -1
    m = (g + d) // 2                 # diviser : on regarde le milieu
    if t[m] == x:
        return m
    if t[m] < x:
        return dicho(t, x, m + 1, d) # régner : UNE seule moitié peut contenir x
    return dicho(t, x, g, m - 1)

t = list(range(0, 2000000, 2))       # un million de nombres pairs, triés
for x in [1000, 1999998, 7]:
    appels = 0
    print(x, dicho(t, x, 0, len(t) - 1), appels)`, { out: "1000 500 19\n1999998 999999 20\n7 -1 21" });

C("dpr-fusion", String.raw`
def fusion(a, b):
    """Fusionne deux listes triées a et b en une seule liste triée."""
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:             # on prend le plus petit des deux "en tête"
            res.append(a[i])
            i = i + 1
        else:
            res.append(b[j])
            j = j + 1
    return res + a[i:] + b[j:]       # l'une des deux listes est épuisée : on recopie l'autre

print(fusion([3, 27, 38, 43], [9, 10, 82]))`, { out: "[3, 9, 10, 27, 38, 43, 82]" });

C("dpr-tri", String.raw`
def tri_fusion(t):
    """Renvoie une nouvelle liste contenant les éléments de t triés."""
    if len(t) <= 1:                  # cas de base : déjà trié
        return t
    m = len(t) // 2
    gauche = tri_fusion(t[:m])       # trier la première moitié
    droite = tri_fusion(t[m:])       # trier la seconde moitié
    return fusion(gauche, droite)    # fusionner les deux moitiés triées

print(tri_fusion([38, 27, 43, 3, 9, 82, 10]))
print(tri_fusion([]), tri_fusion([5]), tri_fusion([2, 1, 2, 1]))`, { deps: ["dpr-fusion"], out: "[3, 9, 10, 27, 38, 43, 82]\n[] [5] [1, 1, 2, 2]" });

C("dpr-trace", String.raw`
def tri_fusion(t, prof=0):
    marge = "    " * prof
    print(marge + "trier", t)
    if len(t) <= 1:
        return t
    m = len(t) // 2
    r = fusion(tri_fusion(t[:m], prof + 1), tri_fusion(t[m:], prof + 1))
    print(marge + "fusion ->", r)
    return r

tri_fusion([38, 27, 43, 3])`, { deps: ["dpr-fusion"], out: String.raw`
trier [38, 27, 43, 3]
    trier [38, 27]
        trier [38]
        trier [27]
    fusion -> [27, 38]
    trier [43, 3]
        trier [43]
        trier [3]
    fusion -> [3, 43]
fusion -> [3, 27, 38, 43]` });

C("dpr-cout", String.raw`
from math import log2

comparaisons = 0

def fusion_c(a, b):
    global comparaisons
    res, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        comparaisons = comparaisons + 1
        if a[i] <= b[j]:
            res.append(a[i]); i = i + 1
        else:
            res.append(b[j]); j = j + 1
    return res + a[i:] + b[j:]

def tri_fusion_c(t):
    if len(t) <= 1:
        return t
    m = len(t) // 2
    return fusion_c(tri_fusion_c(t[:m]), tri_fusion_c(t[m:]))

for n in [8, 1024, 1048576]:
    comparaisons = 0
    tri_fusion_c(list(range(n, 0, -1)))       # liste rangée à l'envers
    print(n, comparaisons, int(n * log2(n)), n * (n - 1) // 2)`, { out: "8 12 24 28\n1024 5120 10240 523776\n1048576 10485760 20971520 549755289600" });

C("dpr-rot-copie", String.raw`
def rotation_copie(img):
    """Quart de tour dans le sens horaire, en fabriquant une NOUVELLE image."""
    n = len(img)
    return [[img[n - 1 - j][i] for j in range(n)] for i in range(n)]

img = [list("ABCD"), list("EFGH"), list("IJKL"), list("MNOP")]
for ligne in rotation_copie(img):
    print("".join(ligne))`, { out: "MIEA\nNJFB\nOKGC\nPLHD" });

C("dpr-rotation", String.raw`
def rotation(img, x, y, n):
    """Tourne d'un quart de tour (sens horaire), SUR PLACE, le carré de côté n
    dont le coin en haut à gauche est img[y][x]. n est une puissance de 2."""
    if n == 1:                                   # un pixel : rien à faire
        return
    h = n // 2
    rotation(img, x, y, h)                       # 1. tourner chacun des 4 quarts
    rotation(img, x + h, y, h)
    rotation(img, x, y + h, h)
    rotation(img, x + h, y + h, h)
    for i in range(h):                           # 2. faire tourner les quarts
        for j in range(h):                       #    pixel par pixel, 4 à la fois
            hg = img[y + i][x + j]
            img[y + i][x + j] = img[y + h + i][x + j]              # bas gauche -> haut gauche
            img[y + h + i][x + j] = img[y + h + i][x + h + j]      # bas droit -> bas gauche
            img[y + h + i][x + h + j] = img[y + i][x + h + j]      # haut droit -> bas droit
            img[y + i][x + h + j] = hg                             # haut gauche -> haut droit

img = [list("ABCD"), list("EFGH"), list("IJKL"), list("MNOP")]
rotation(img, 0, 0, 4)
for ligne in img:
    print("".join(ligne))`, { out: "MIEA\nNJFB\nOKGC\nPLHD" });

C("dpr-rot-dessin", String.raw`
dessin = ["..##....",
          "..##....",
          "..##....",
          "..##....",
          "..##....",
          "..######",
          "..######",
          "........"]
img = [list(ligne) for ligne in dessin]
rotation(img, 0, 0, 8)
for ligne in img:
    print("".join(ligne))

grande = [[64 * i + j for j in range(64)] for i in range(64)]
attendu = [[grande[63 - j][i] for j in range(64)] for i in range(64)]
rotation(grande, 0, 0, 64)
print(grande == attendu)`, { deps: ["dpr-rotation"], out: String.raw`
........
........
.#######
.#######
.##.....
.##.....
.##.....
.##.....
True` });

/* pièges */
C("dpr-p-reste", String.raw`
def fusion(a, b):
    res, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i = i + 1
        else:
            res.append(b[j]); j = j + 1
    return res                       # on a oublié ce qui reste dans a ou b

print(fusion([1, 5, 9], [2, 3]))`, { out: "[1, 2, 3]" });

C("dpr-p-base", String.raw`
def tri_fusion(t):
    m = len(t) // 2                   # pas de cas de base...
    return fusion(tri_fusion(t[:m]), tri_fusion(t[m:]))

tri_fusion([3, 1])`, { deps: ["dpr-fusion"], err: "RecursionError: maximum recursion depth exceeded" });

C("dpr-p-place", String.raw`
t = [5, 2, 4, 1]
tri_fusion(t)                         # le résultat est renvoyé... et perdu
print(t)
t = tri_fusion(t)                     # il faut le récupérer
print(t)`, { deps: ["dpr-fusion", "dpr-tri"], out: "[5, 2, 4, 1]\n[1, 2, 4, 5]" });

/* prédis la sortie */
C("dpr-x1", String.raw`
def f(t):
    if len(t) == 1:
        return t[0]
    m = len(t) // 2
    return f(t[:m]) + f(t[m:])

print(f([5, 1, 4, 2, 3]))`, { out: "15" });

C("dpr-x2", String.raw`
def mystere(t, g, d):
    if g == d:
        return (t[g], t[g])
    m = (g + d) // 2
    a, b = mystere(t, g, m)
    c, e = mystere(t, m + 1, d)
    return (min(a, c), max(b, e))

print(mystere([7, 2, 9, 4, 1, 8], 0, 5))`, { out: "(1, 9)" });

C("dpr-x3", String.raw`
appels = 0

def tri(t):
    global appels
    appels = appels + 1
    if len(t) <= 1:
        return t
    m = len(t) // 2
    return fusion(tri(t[:m]), tri(t[m:]))

print(tri([4, 1, 3, 5, 2]), appels)`, { deps: ["dpr-fusion"], out: "[1, 2, 3, 4, 5] 9" });

C("dpr-x4", String.raw`
def g(n):
    if n <= 1:
        return 0
    return 1 + g(n // 2)

print(g(8), g(1000), g(1000000))`, { out: "3 9 19" });

/* épreuve pratique 1 */
C("dpr-ep1-fourni", String.raw`
def fusion(a, b):
    """a et b sont deux listes triées dans l'ordre croissant.
    Renvoie une nouvelle liste triée contenant les éléments de a et de b."""
    res = []
    i, j = 0, 0
    while ... :
        if a[i] <= b[j]:
            res.append(a[i])
            i = i + 1
        else:
            ...
            ...
    while i < len(a):
        res.append(a[i])
        i = i + 1
    ...
    return res

def tri_fusion(t):
    """Renvoie une nouvelle liste contenant les éléments de t triés."""
    ...`, { fichier: "tri_fusion.py", run: false, trous: [6, 11, 12, 16, 21] });

C("dpr-ep1-corr", String.raw`
def fusion(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i = i + 1
        else:
            res.append(b[j])
            j = j + 1
    while i < len(a):
        res.append(a[i])
        i = i + 1
    while j < len(b):
        res.append(b[j])
        j = j + 1
    return res

def tri_fusion(t):
    if len(t) <= 1:
        return t[:]                   # une copie : on ne renvoie jamais t lui-même
    m = len(t) // 2
    return fusion(tri_fusion(t[:m]), tri_fusion(t[m:]))

def test():
    assert fusion([1, 4, 9], [2, 3, 10, 11]) == [1, 2, 3, 4, 9, 10, 11]
    assert fusion([], [1, 2]) == [1, 2]
    assert fusion([5], []) == [5]
    assert tri_fusion([]) == []
    assert tri_fusion([7]) == [7]
    assert tri_fusion([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]          # doublons
    assert tri_fusion(list(range(50, 0, -1))) == list(range(1, 51))
    t = [4, 2, 8]
    assert tri_fusion(t) == [2, 4, 8] and t == [4, 2, 8]           # t n'est pas modifiée

test()
print("tous les tests passent")`, { fichier: "tri_fusion.py", out: "tous les tests passent" });

C("dpr-ep1-bug", String.raw`
def tri_fusion_bug(t):
    if len(t) <= 1:
        return t
    m = len(t) // 2
    return fusion(tri_fusion_bug(t[:m + 1]), tri_fusion_bug(t[m + 1:]))

print(tri_fusion_bug([4, 1, 3]))`, { fichier: "version_bugguee.py", deps: ["dpr-fusion"], err: "RecursionError: maximum recursion depth exceeded" });

/* épreuve pratique 2 */
C("dpr-ep2-fourni", String.raw`
def creer_image(n):
    """Image carrée n x n dont le pixel (ligne i, colonne j) vaut n * i + j."""
    return [[n * i + j for j in range(n)] for i in range(n)]

def afficher(img):
    for ligne in img:
        print(" ".join(str(p).rjust(2) for p in ligne))

def rotation(img, x, y, n):
    """Quart de tour dans le sens horaire, sur place, du carré de côté n
    dont le coin en haut à gauche est img[y][x]."""
    if n == 1:
        return
    h = n // 2
    rotation(img, x, y, h)
    rotation(img, x + h, y, h)
    rotation(img, x, y + h, h)
    rotation(img, x + h, y + h, h)
    for i in range(h):
        for j in range(h):
            ...                       # échange circulaire de 4 pixels

img = creer_image(4)
rotation(img, 0, 0, 4)
afficher(img)`, { fichier: "rotation.py", run: false, trous: [21] });

C("dpr-ep2-corr", String.raw`
def creer_image(n):
    return [[n * i + j for j in range(n)] for i in range(n)]

def rotation(img, x, y, n):
    if n == 1:
        return
    h = n // 2
    rotation(img, x, y, h)
    rotation(img, x + h, y, h)
    rotation(img, x, y + h, h)
    rotation(img, x + h, y + h, h)
    for i in range(h):
        for j in range(h):
            hg = img[y + i][x + j]
            img[y + i][x + j] = img[y + h + i][x + j]
            img[y + h + i][x + j] = img[y + h + i][x + h + j]
            img[y + h + i][x + h + j] = img[y + i][x + h + j]
            img[y + i][x + h + j] = hg

def rotation_copie(img):
    n = len(img)
    return [[img[n - 1 - j][i] for j in range(n)] for i in range(n)]

def est_puissance_de_2(n):
    while n % 2 == 0:
        n = n // 2
    return n == 1

def test():
    for n in [1, 2, 4, 8, 32]:
        img = creer_image(n)
        attendu = rotation_copie(img)
        rotation(img, 0, 0, n)
        assert img == attendu
    img = creer_image(8)
    for _ in range(4):
        rotation(img, 0, 0, 8)          # quatre quarts de tour : retour au départ
    assert img == creer_image(8)
    assert est_puissance_de_2(64) and not est_puissance_de_2(48)

test()
print("tous les tests passent")`, { fichier: "rotation.py", out: "tous les tests passent" });

/* épreuve écrite */
C("dpr-ecrit-corr", String.raw`
def fusion_rec(a, b):
    """Version récursive de la fusion (a et b triées)."""
    if a == []:
        return b
    if b == []:
        return a
    if a[0] <= b[0]:
        return [a[0]] + fusion_rec(a[1:], b)
    return [b[0]] + fusion_rec(a, b[1:])

def tri_inv(t):
    """Renvoie (liste triée, nombre d'inversions de t)."""
    if len(t) <= 1:
        return t, 0
    m = len(t) // 2
    g, ig = tri_inv(t[:m])
    d, id_ = tri_inv(t[m:])
    res, i, j, inv = [], 0, 0, ig + id_
    while i < len(g) and j < len(d):
        if g[i] <= d[j]:
            res.append(g[i]); i = i + 1
        else:
            res.append(d[j]); j = j + 1
            inv = inv + len(g) - i      # d[j] est plus petit que TOUS les restants de g
    return res + g[i:] + d[j:], inv

print(fusion_rec([2, 7, 9], [1, 8]))
print(tri_inv([3, 1, 4, 2]))
print(tri_inv([5, 4, 3, 2, 1]))`, { out: "[1, 2, 7, 8, 9]\n([1, 2, 3, 4], 3)\n([1, 2, 3, 4, 5], 10)" });

C("dpr-retenir", String.raw`
def resoudre(probleme):
    if probleme est assez petit:              # cas de base
        return solution directe
    parties = diviser(probleme)               # 1. DIVISER
    sols = [resoudre(p) for p in parties]     # 2. RÉGNER (appels récursifs)
    return combiner(sols)                     # 3. COMBINER`, { run: false });

CH.push({
  id: "dpr", court: "diviser_regner", fichier: "diviser_regner.py",
  titre: "Diviser pour régner",
  rubrique: "Rubrique « Algorithmique » : méthode « diviser pour régner » (tri fusion, rotation d’image, recherche dichotomique)",
  accroche: "Couper un problème en sous-problèmes indépendants, les résoudre, combiner : tri fusion en n log n, dichotomie, rotation d’image sur place.",
  essentiel: [
    "<b>Diviser pour régner</b> : <b>diviser</b> le problème en sous-problèmes du même type, plus petits et <b>indépendants</b> ; les <b>résoudre</b> (récursivement) ; <b>combiner</b> leurs solutions.",
    "La <b>recherche dichotomique</b> ne garde qu’une moitié à chaque étape : environ log₂ <i>n</i> étapes (20 pour un million d’éléments).",
    "Le <b>tri fusion</b> coupe la liste en deux, trie chaque moitié, puis <b>fusionne</b> deux listes triées en un seul passage.",
    "Son coût est de l’ordre de <b><i>n</i> log₂ <i>n</i></b> comparaisons, même dans le pire des cas, contre <i>n</i>² pour les tris par insertion ou par sélection.",
    "La <b>rotation d’une image</b> d’un quart de tour se fait <b>sur place</b> : on tourne les quatre quarts, puis on les permute ; aucune copie de l’image."
  ],
  attendus: [
    "Écrire un algorithme utilisant la méthode « diviser pour régner » (c’est la seule capacité listée par le BO, mais elle se travaille sur les trois exemples ci-dessous).",
    "Connaître les exemples cités par le programme : la rotation d’une image bitmap d’un quart de tour avec un coût en mémoire constant, et le tri fusion, dont le coût en <i>n</i> log₂ <i>n</i> est à faire constater.",
    "Reconnaître la recherche dichotomique et la puissance rapide (chapitre Récursivité) comme des cas de « diviser pour régner ».",
    "Comparer le coût de deux algorithmes : <i>n</i>² contre <i>n</i> log₂ <i>n</i>, <i>n</i> contre log₂ <i>n</i>."
  ],
  idees: [
    { id: "i1", t: "Le principe : diviser, régner, combiner", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>La méthode <b>diviser pour régner</b> résout un problème en trois temps :</p><ol><li><b>diviser</b> le problème en sous-problèmes <b>du même type</b>, de taille plus petite, <b>indépendants</b> les uns des autres ;</li><li><b>régner</b> : résoudre chaque sous-problème, en général par un appel récursif (et directement quand il est assez petit) ;</li><li><b>combiner</b> les solutions des sous-problèmes pour obtenir celle du problème de départ.</li></ol></div>
<p>Exemple minimal : le maximum d’un tableau. On le coupe en deux moitiés, on cherche le maximum de chacune, et le maximum du tout est le plus grand des deux.</p>
[[dpr-max]]
<p>Ici, la méthode ne gagne rien sur un simple parcours (il faut de toute façon regarder les <i>n</i> cases), mais elle montre la structure. Le gain vient quand la combinaison est <b>bon marché</b> par rapport au travail évité, ou quand on peut <b>jeter</b> une partie du problème.</p>
<div class="boite ex"><div class="lab"># différence avec la programmation dynamique</div><p>« Indépendants » est le mot clé : les deux moitiés d’un tableau ne partagent rien. Quand les sous-problèmes <b>se chevauchent</b> (comme F(<i>n</i> − 1) et F(<i>n</i> − 2) pour Fibonacci, qui ont besoin tous les deux de F(<i>n</i> − 3)), on passe à la <b>programmation dynamique</b> (chapitre Programmation dynamique).</p></div>` },

    { id: "i2", t: "La recherche dichotomique : on ne garde qu’une moitié", h: `
<p>Pour chercher <code>x</code> dans un tableau <b>trié</b>, on regarde l’élément du milieu. S’il vaut <code>x</code>, c’est fini ; s’il est plus petit, <code>x</code> ne peut être que dans la moitié droite ; sinon, dans la moitié gauche. On <b>divise</b> (le milieu), on <b>règne</b> sur une seule moitié, et il n’y a <b>rien à combiner</b> : la réponse de la moitié est la réponse.</p>
[[dpr-dicho]]
<p>Sur un million d’éléments, au plus 21 appels (le dernier constate que la zone est vide), contre un million de comparaisons pour une recherche séquentielle. Le nombre d’appels est de l’ordre de log₂ <i>n</i> : 2²⁰ = 1 048 576. Ce coût <b>logarithmique</b> n’est possible que parce que le tableau est trié.</p>
<p>La <b>puissance rapide</b> du chapitre Récursivité suit le même schéma : a<sup>n</sup> se déduit de a<sup>n//2</sup>, un seul sous-problème deux fois plus petit.</p>` },

    { id: "i3", t: "Fusionner deux listes triées", h: `
<p>Le cœur du tri fusion est une opération simple : <b>fusionner</b> deux listes déjà triées en une seule liste triée. On compare les deux éléments « en tête », on prend le plus petit, on avance dans la liste d’où il vient, et on recommence. Quand une liste est épuisée, on recopie le reste de l’autre.</p>
[[dpr-fusion]]
<p>Chaque comparaison place un élément définitivement : fusionner deux listes de longueurs <i>p</i> et <i>q</i> demande <b>au plus <i>p</i> + <i>q</i> − 1 comparaisons</b>. La fusion est donc de coût <b>linéaire</b>. Le test <code>a[i] &lt;= b[j]</code> (et non <code>&lt;</code>) garde dans l’ordre d’origine deux éléments égaux : le tri est dit <b>stable</b>.</p>
<p>Dans l’animation, choisis « une fusion pas à pas » : les deux têtes sont comparées, la plus petite descend dans le résultat.</p>
[[w-algo-tri-fusion|fusion]]` },

    { id: "i4", t: "Le tri fusion", h: `
<p>Trier une liste revient à : la couper en deux moitiés (<b>diviser</b>), trier chaque moitié par un appel récursif (<b>régner</b>), fusionner les deux moitiés triées (<b>combiner</b>). Une liste de 0 ou 1 élément est déjà triée : c’est le cas de base.</p>
[[dpr-tri]]
<p>On voit les deux phases en affichant les appels : la <b>descente</b> découpe jusqu’aux listes d’un élément, la <b>remontée</b> fusionne.</p>
[[dpr-trace]]
[[w-algo-tri-fusion|tout]]
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1945 <b>·</b></span> John von Neumann écrit un programme de tri par fusion pour l’EDVAC, l’un des tout premiers programmes de tri pour ordinateur (d’après Donald Knuth, <i>The Art of Computer Programming</i>, vol. 3).</p></div>` },

    { id: "i5", t: "Le coût du tri fusion : n log₂ n", h: `
<p>Dessinons l’arbre des appels pour <i>n</i> = 8 : au niveau 0, une liste de 8 ; au niveau 1, deux listes de 4 ; au niveau 2, quatre listes de 2 ; au niveau 3, huit listes de 1. Il y a <b>log₂ <i>n</i></b> niveaux de fusion (ici 3).</p>
<ul><li>À chaque niveau, les fusions portent en tout sur les <i>n</i> éléments : <b>au plus <i>n</i> comparaisons par niveau</b>.</li>
<li>Avec log₂ <i>n</i> niveaux : <b>au plus <i>n</i> log₂ <i>n</i> comparaisons</b>, quel que soit l’ordre de départ.</li></ul>
<p>Mesurons sur une liste rangée à l’envers (le pire cas des tris par insertion), en comparant à <i>n</i> log₂ <i>n</i> et aux <i>n</i>(<i>n</i> − 1)/2 comparaisons du tri par insertion :</p>
[[dpr-cout]]
<div class="tab-wrap"><table><tr><th>n</th><th>tri fusion (mesuré)</th><th>n log₂ n</th><th>tri par insertion, liste à l’envers</th></tr>
<tr><td>8</td><td>12</td><td>24</td><td>28</td></tr><tr><td>1 024</td><td>5 120</td><td>10 240</td><td>523 776</td></tr><tr><td>1 048 576</td><td>10 485 760</td><td>20 971 520</td><td>environ 550 milliards</td></tr></table></div>
<p>Pour un million d’éléments, l’écart est d’un facteur 50 000 : à un milliard de comparaisons par seconde, le tri fusion prend une centième de seconde, le tri par insertion plus de 9 minutes. Le prix à payer : le tri fusion (dans cette version) <b>crée de nouvelles listes</b>, donc utilise de la mémoire supplémentaire proportionnelle à <i>n</i>.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Aucun tri par comparaisons ne peut faire mieux que de l’ordre de <i>n</i> log₂ <i>n</i> comparaisons dans le pire cas : le tri fusion est optimal de ce point de vue. Le tri de Python (<code>sorted</code>, <code>list.sort</code>), appelé Timsort (Tim Peters, 2002), est un tri fusion amélioré qui profite des morceaux déjà triés.</p></div>` },

    { id: "i6", t: "Faire tourner une image d’un quart de tour", h: `
<p>Une image bitmap est un tableau de pixels. Pour la tourner d’un quart de tour dans le sens des aiguilles d’une montre, le pixel de la ligne <i>i</i>, colonne <i>j</i> de la nouvelle image est celui de la ligne <i>n</i> − 1 − <i>j</i>, colonne <i>i</i> de l’ancienne. La méthode directe fabrique une <b>deuxième image</b> : sa mémoire est proportionnelle au nombre de pixels.</p>
[[dpr-rot-copie]]
<p>Le programme demande une rotation avec un <b>coût en mémoire constant</b> : on modifie l’image <b>sur place</b>. Pour une image carrée de côté <i>n</i> (une puissance de 2) :</p>
<ol><li><b>diviser</b> l’image en quatre quarts de côté <i>n</i>/2 ;</li><li><b>régner</b> : tourner chaque quart sur lui-même d’un quart de tour (appel récursif) ;</li><li><b>combiner</b> : déplacer les quarts d’un cran dans le sens horaire (haut gauche → haut droit → bas droit → bas gauche → haut gauche), en échangeant les pixels quatre par quatre avec une seule variable auxiliaire.</li></ol>
[[dpr-rotation]]
[[w-algo-rotation]]
<p>La vérification sur une image de 64 × 64 compare le résultat avec la formule directe :</p>
[[dpr-rot-dessin]]
<p>Mémoire : une variable <code>hg</code> pour les échanges, plus la pile d’appels, qui ne dépasse pas log₂ <i>n</i> + 1 cadres (7 pour 64 × 64). C’est négligeable devant les <i>n</i>² pixels : on parle de coût en mémoire constant (ou presque). En temps, chaque pixel est déplacé une fois par niveau : de l’ordre de <i>n</i>² log₂ <i>n</i> opérations.</p>
<div class="boite ex"><div class="lab"># avec un module d’images</div><p>Avec la bibliothèque PIL (Pillow), on lit les pixels par <code>img.getpixel((x, y))</code> et on les écrit par <code>img.putpixel((x, y), couleur)</code> : la fonction se recopie en remplaçant <code>img[y][x]</code> par ces appels. Attention, PIL désigne un pixel par (colonne, ligne).</p></div>` },

    { id: "i7", t: "Reconnaître et écrire un « diviser pour régner »", h: `
<div class="boite retenir-b"><div class="lab"># méthode</div>
<ol><li>Quel est le <b>cas de base</b> (liste vide ou d’un élément, image d’un pixel, zone vide) ?</li>
<li>Comment <b>couper</b> la donnée (milieu d’une liste, quatre quarts d’une image) ? Les morceaux doivent être <b>indépendants</b>.</li>
<li>Combien de morceaux faut-il <b>vraiment</b> traiter (un seul pour la dichotomie, deux pour le tri fusion, quatre pour l’image) ?</li>
<li>Comment <b>combiner</b> (rien, une fusion, une permutation) et combien cela coûte-t-il ?</li></ol></div>
<div class="tab-wrap"><table><tr><th>algorithme</th><th>diviser</th><th>régner</th><th>combiner</th><th>coût</th></tr>
<tr><td>dichotomie</td><td>milieu</td><td>1 moitié</td><td>rien</td><td>log₂ n</td></tr>
<tr><td>puissance rapide</td><td>n // 2</td><td>1 appel</td><td>1 ou 2 multiplications</td><td>log₂ n</td></tr>
<tr><td>tri fusion</td><td>milieu</td><td>2 moitiés</td><td>fusion (linéaire)</td><td>n log₂ n</td></tr>
<tr><td>rotation d’image</td><td>4 quarts</td><td>4 quarts</td><td>permutation des quarts</td><td>n² log₂ n, mémoire constante</td></tr></table></div>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Autres « diviser pour régner » célèbres : le <b>tri rapide</b> (<i>quicksort</i>, Tony Hoare, 1959-1961), qui partage la liste autour d’un pivot ; la multiplication rapide de grands entiers de <b>Karatsuba</b> (1960) ; la transformée de Fourier rapide (Cooley et Tukey, 1965), au cœur de la compression du son et des images.</p></div>` }
  ],
  pieges: [
    { t: "Oublier de recopier le reste dans la fusion", h: `[[dpr-p-reste]]<p>La boucle s’arrête dès qu’<b>une</b> liste est épuisée : 5 et 9 sont perdus. Il faut ajouter <code>a[i:]</code> et <code>b[j:]</code> (l’un des deux est vide).</p>` },
    { t: "Oublier le cas de base", h: `[[dpr-p-base]]<p>Sur une liste d’un élément, <code>t[:0]</code> est vide et <code>t[0:]</code> est la liste elle-même : le même appel recommence à l’infini. Le cas de base <code>len(t) &lt;= 1</code> est obligatoire.</p>` },
    { t: "Croire que tri_fusion trie la liste sur place", h: `[[dpr-p-place]]<p>Cette version <b>renvoie une nouvelle liste</b> (comme <code>sorted</code>) ; elle ne modifie pas <code>t</code> (contrairement à <code>t.sort()</code>). Il faut affecter le résultat.</p>` },
    { t: "Confondre « diviser pour régner » et « couper en deux »", h: `<p>La rotation d’image coupe en <b>quatre</b> ; la dichotomie ne traite qu’<b>une</b> moitié. Ce qui compte : des sous-problèmes du même type, plus petits, indépendants, et une combinaison des réponses. Inversement, couper en deux ne suffit pas à gagner du temps : le maximum par « diviser pour régner » coûte autant qu’un parcours.</p>` },
    { t: "Indices décalés : t[:m + 1] et t[m + 1:]", h: `<p>Avec <code>m = len(t) // 2</code>, pour une liste de 2 éléments, <code>m + 1</code> vaut 2 : la « moitié » gauche est la liste entière, et l’appel ne rétrécit pas (RecursionError). Les deux moitiés doivent être <b>strictement plus petites</b> : <code>t[:m]</code> et <code>t[m:]</code> avec <code>m ≥ 1</code>.</p>` }
  ],
  retenir: `
<h2>Le squelette</h2>
[[dpr-retenir]]
<h2>Les trois exemples du programme</h2>
<div class="tab-wrap"><table><tr><th>algorithme</th><th>diviser</th><th>régner</th><th>combiner</th><th>coût</th></tr>
<tr><td>recherche dichotomique</td><td>élément du milieu</td><td>une seule moitié</td><td>rien</td><td>≈ log₂ n</td></tr>
<tr><td>tri fusion</td><td>deux moitiés</td><td>trier chaque moitié</td><td>fusion de deux listes triées (≤ n − 1 comparaisons)</td><td>≈ n log₂ n (pire cas compris)</td></tr>
<tr><td>rotation d’image n × n</td><td>quatre quarts</td><td>tourner chaque quart</td><td>permuter les quarts, 4 pixels à la fois</td><td>mémoire constante</td></tr></table></div>
<h2>Ordres de grandeur pour n = 1 000 000</h2>
<div class="tab-wrap"><table><tr><th>coût</th><th>opérations</th></tr><tr><td>log₂ n</td><td>20</td></tr><tr><td>n</td><td>10⁶</td></tr><tr><td>n log₂ n</td><td>2 × 10⁷</td></tr><tr><td>n²</td><td>10¹²</td></tr></table></div>
<h2>Les réflexes</h2>
<ul><li>Cas de base en premier ; sous-problèmes <b>strictement plus petits</b>.</li><li>Fusion : comparer les têtes, prendre la plus petite, recopier le reste à la fin.</li><li>Rotation horaire : nouveau[i][j] = ancien[n − 1 − j][i].</li><li>Sous-problèmes qui se chevauchent → programmation dynamique, pas « diviser pour régner ».</li></ul>`,
  predis: [
    { code: "dpr-x1", niv: "facile", rep: "La fonction coupe la liste en deux et additionne les résultats des deux moitiés ; une liste d’un élément renvoie cet élément. C’est la somme : 5 + 1 + 4 + 2 + 3 = 15." },
    { code: "dpr-x2", niv: "moyen", rep: "Chaque appel renvoie le couple (minimum, maximum) de sa zone ; la combinaison prend le plus petit des minimums et le plus grand des maximums : (1, 9)." },
    { code: "dpr-x3", niv: "moyen", rep: "Liste de 5 → 2 et 3 ; 2 → 1 et 1 ; 3 → 1 et 2 ; 2 → 1 et 1. On compte 1 + 2 + 4 + 2 = 9 appels. En général, 2<i>n</i> − 1 appels pour <i>n</i> ≥ 1 (chaque appel qui n’est pas une feuille en crée deux, et il y a <i>n</i> feuilles)." },
    { code: "dpr-x4", niv: "difficile", rep: "<code>g(n)</code> compte combien de fois on peut diviser <i>n</i> par 2 avant d’atteindre 1 : c’est ⌊log₂ <i>n</i>⌋. 8 = 2³ donne 3 ; 2⁹ = 512 ≤ 1 000 &lt; 1 024 donne 9 ; 2¹⁹ = 524 288 ≤ 10⁶ &lt; 2²⁰ donne 19." }
  ],
  ep: [
    { titre: "Le tri fusion à compléter", enonce: `<p>On veut un tri fusion qui ne modifie pas la liste de départ. Le fichier fourni est incomplet.</p>[[dpr-ep1-fourni]]`,
      questions: [
        { q: "Compléter la condition de la ligne 6 et les lignes 11 et 12.", c: `<p>Ligne 6 : <code>while i &lt; len(a) and j &lt; len(b):</code>. Lignes 11-12 : <code>res.append(b[j])</code> puis <code>j = j + 1</code>.</p>` },
        { q: "La ligne 16 doit recopier ce qui reste de <code>b</code>. L’écrire. Pourquoi n’a-t-on jamais à exécuter les deux boucles de recopie avec un reste non vide ?", c: `<p>Une boucle <code>while j &lt; len(b):</code> symétrique de celle sur <code>a</code>. La première boucle ne s’arrête que lorsqu’<b>une</b> des deux listes est épuisée : au plus une des deux boucles de recopie a du travail.</p>` },
        { q: "Écrire <code>tri_fusion(t)</code> (ligne 21) et une fonction <code>test()</code> avec des cas limites : liste vide, un élément, doublons, liste à l’envers, et vérification que <code>t</code> n’est pas modifiée.", c: `[[dpr-ep1-corr]]` },
        { q: "Un camarade propose la version ci-dessous. Exécuter et expliquer l’erreur obtenue.", code: "[[dpr-ep1-bug]]", c: `<p>Pour <code>[4, 1, 3]</code>, m = 1 : les « moitiés » sont <code>[4, 1]</code> et <code>[3]</code>. Puis, pour <code>[4, 1]</code>, m = 1 et <code>t[:2]</code> est la liste <b>entière</b> : l’appel se répète à l’identique jusqu’à la <code>RecursionError</code>. Il faut couper en <code>t[:m]</code> et <code>t[m:]</code>, deux listes strictement plus courtes dès que la liste a au moins 2 éléments.</p>` },
        { q: "À l’oral : combien de comparaisons au plus pour trier 1 024 éléments ? Et avec un tri par insertion ?", c: `<p>10 niveaux de fusion (2¹⁰ = 1 024), au plus 1 024 comparaisons par niveau : au plus 10 240 (on en a mesuré 5 120 sur une liste à l’envers). Le tri par insertion en fait jusqu’à 1 024 × 1 023 / 2 = 523 776.</p>` }
      ] },
    { titre: "Rotation d’une image sur place", enonce: `<p>Une image est représentée par une liste de listes carrée de côté <i>n</i>, puissance de 2. On veut la faire tourner d’un quart de tour dans le sens horaire <b>sans créer de seconde image</b>.</p>[[dpr-ep2-fourni]]`,
      questions: [
        { q: "Quelle est la valeur attendue du pixel en haut à gauche après rotation de <code>creer_image(4)</code> ? Justifier avec la formule.", c: `<p>nouveau[0][0] = ancien[<i>n</i> − 1 − 0][0] = ancien[3][0] = 4 × 3 + 0 = <b>12</b> : c’est le coin bas gauche qui monte en haut à gauche.</p>` },
        { q: "Compléter la ligne 21 : les quatre affectations de l’échange circulaire, avec une seule variable auxiliaire.", c: `<p>On sauve le haut gauche, puis on remonte le bas gauche, on décale le bas droit vers la gauche, on descend le haut droit, et on place l’ancien haut gauche en haut à droite (voir le corrigé complet).</p>` },
        { q: "Écrire une fonction <code>rotation_copie(img)</code> qui renvoie une nouvelle image tournée, puis une fonction de test qui compare les deux méthodes pour plusieurs tailles, et vérifie que quatre quarts de tour ramènent l’image de départ.", c: `[[dpr-ep2-corr]]` },
        { q: "À l’oral : pourquoi dit-on que <code>rotation</code> a un coût en mémoire constant, alors qu’elle est récursive ?", c: `<p>Elle n’alloue aucune autre image : seulement la variable <code>hg</code> et les compteurs. La pile d’appels contient au plus log₂ <i>n</i> + 1 cadres (11 pour une image de 1 024 × 1 024 pixels), ce qui est négligeable devant le million de pixels. <code>rotation_copie</code>, elle, crée <i>n</i>² nouvelles cases.</p>` }
      ] }
  ],
  ecrit: { titre: "Fusion récursive et inversions", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Dans une liste <code>t</code>, une <b>inversion</b> est un couple d’indices (<i>i</i>, <i>j</i>) avec <i>i</i> &lt; <i>j</i> et <code>t[i] &gt; t[j]</code>. Le nombre d’inversions mesure le « désordre » d’une liste (il sert par exemple à comparer deux classements). On utilise la fonction <code>fusion</code> et le tri fusion du cours.</p>`,
    questions: [
      { q: "Donner les inversions de <code>[3, 1, 4, 2]</code>. Combien une liste de <i>n</i> éléments distincts rangés dans l’ordre décroissant en compte-t-elle ?", pts: "1 pt", c: `<p>(3, 1), (3, 2), (4, 2) : <b>3 inversions</b> (on cite les valeurs). Dans l’ordre décroissant, tous les couples sont inversés : <i>n</i>(<i>n</i> − 1)/2 (10 pour <i>n</i> = 5).</p>` },
      { q: "Écrire une version <b>récursive</b> <code>fusion_rec(a, b)</code> de la fusion de deux listes triées (sans boucle).", pts: "1,5 pt", c: `<p>Cas de base : si une liste est vide, renvoyer l’autre. Sinon, le plus petit des deux premiers éléments vient en tête, suivi de la fusion du reste : <code>[a[0]] + fusion_rec(a[1:], b)</code> ou <code>[b[0]] + fusion_rec(a, b[1:])</code>.</p>` },
      { q: "Quel inconvénient a <code>fusion_rec</code> pour des listes de 2 000 éléments chacune ?", pts: "0,5 pt", c: `<p>Chaque élément placé coûte un appel : jusqu’à 3 999 appels imbriqués, au-delà de la limite de 1 000 de Python (<code>RecursionError</code>). Les découpages <code>a[1:]</code> font en plus une copie à chaque appel. La version itérative n’a aucun de ces défauts.</p>` },
      { q: "Pendant la fusion de deux moitiés triées <code>g</code> et <code>d</code>, on prend <code>d[j]</code> alors qu’il reste <code>len(g) − i</code> éléments dans <code>g</code>. Combien d’inversions « entre les deux moitiés » cela révèle-t-il ? Pourquoi ?", pts: "1,5 pt", c: `<p><b>len(g) − i</b> : <code>d[j] &lt; g[i]</code>, et <code>g</code> est triée, donc <code>d[j]</code> est plus petit que <b>tous</b> les éléments restants de <code>g</code>, qui étaient placés avant lui dans la liste de départ.</p>` },
      { q: "En déduire une fonction <code>tri_inv(t)</code> qui renvoie le couple (liste triée, nombre d’inversions), selon la méthode diviser pour régner. Quel est son coût ?", pts: "1,5 pt", c: `<p>Inversions = inversions de la moitié gauche + inversions de la moitié droite + inversions entre les deux, comptées pendant la fusion. Même coût que le tri fusion : <i>n</i> log₂ <i>n</i>, au lieu de <i>n</i>² pour la double boucle qui teste tous les couples.</p>[[dpr-ecrit-corr]]` }
    ],
    methode: `<p>À l’écrit, « diviser pour régner » se reconnaît aux mots « couper en deux », « moitié », « sous-tableau ». On attend presque toujours : un cas de base explicite, un découpage qui rétrécit, la combinaison, et une phrase sur le coût (<i>n</i> log₂ <i>n</i> pour le tri fusion, log₂ <i>n</i> pour la dichotomie). Nomme les trois étapes dans ta copie : c’est ce que le correcteur cherche.</p>` },
  qcm: [
    { q: "Quelles sont les trois étapes de la méthode « diviser pour régner » ?", c: ["Trier, chercher, afficher", "Diviser, résoudre les sous-problèmes, combiner", "Initialiser, boucler, renvoyer", "Mémoriser, réutiliser, compléter"], a: 1, e: "Diviser en sous-problèmes indépendants, les résoudre (récursivement), combiner leurs solutions.", ref: "i1" },
    { q: "Quelle condition doivent remplir les sous-problèmes ?", c: ["Être tous de taille 1", "Être du même type, plus petits et indépendants", "Se chevaucher le plus possible", "Être résolus par une boucle while"], a: 1, e: "S’ils se chevauchent, on utilise plutôt la programmation dynamique.", ref: "i1" },
    { q: "Combien d’appels, au plus, fait la recherche dichotomique récursive dans un tableau trié d’un million d’éléments ?", c: ["Environ 20", "Environ 1 000", "500 000", "1 000 000"], a: 0, e: "On divise la zone par 2 à chaque appel : environ log₂(10⁶) ≈ 20 (21 avec l’appel qui trouve la zone vide).", ref: "i2" },
    { q: "Dans la recherche dichotomique, que fait l’étape « combiner » ?", c: ["Elle fusionne les deux moitiés", "Rien : la réponse de la moitié explorée est la réponse", "Elle additionne les indices", "Elle trie le tableau"], a: 1, e: "Une seule moitié peut contenir x ; sa réponse est directement renvoyée.", ref: "i2" },
    { q: "Que renvoie <code>fusion([2, 8], [1, 5, 9])</code> ?", c: ["[2, 8, 1, 5, 9]", "[1, 2, 5, 8, 9]", "[1, 5, 9, 2, 8]", "[1, 2, 5]"], a: 1, e: "On prend à chaque fois la plus petite des deux têtes, puis on recopie le reste.", ref: "i3" },
    { q: "Combien de comparaisons au plus pour fusionner deux listes triées de 4 et 3 éléments ?", c: ["3", "6", "7", "12"], a: 1, e: "Au plus p + q − 1 = 6 : chaque comparaison place un élément, le dernier est placé sans comparaison.", ref: "i3" },
    { q: "Quel est le cas de base du tri fusion ?", c: ["Une liste de 0 ou 1 élément, déjà triée", "Une liste de 2 éléments", "Une liste triée", "Il n’y en a pas"], a: 0, e: "Sans lui, une liste d’un élément se redécoupe indéfiniment.", ref: "i4" },
    { q: "Combien d’appels à <code>tri_fusion</code> pour une liste de 8 éléments ?", c: ["8", "15", "16", "24"], a: 1, e: "1 + 2 + 4 + 8 = 15 = 2n − 1.", ref: "i4" },
    { q: "Quel est le coût du tri fusion dans le pire des cas ?", c: ["De l’ordre de n", "De l’ordre de n log₂ n", "De l’ordre de n²", "De l’ordre de 2ⁿ"], a: 1, e: "log₂ n niveaux, au plus n comparaisons par niveau.", ref: "i5" },
    { q: "Combien de niveaux de fusion pour trier 1 024 éléments ?", c: ["2", "10", "512", "1 024"], a: 1, e: "2¹⁰ = 1 024 : on divise par deux 10 fois avant d’atteindre des listes d’un élément.", ref: "i5" },
    { q: "Quel est l’inconvénient de la version du cours du tri fusion par rapport au tri par insertion ?", c: ["Il est plus lent sur les grandes listes", "Il utilise de la mémoire supplémentaire (nouvelles listes)", "Il ne marche pas avec des doublons", "Il ne trie que des entiers"], a: 1, e: "Les découpages et les fusions créent de nouvelles listes, de taille totale proportionnelle à n.", ref: "i5" },
    { q: "Après un quart de tour horaire d’une image n × n, que vaut le pixel nouveau[i][j] ?", c: ["ancien[j][i]", "ancien[n − 1 − j][i]", "ancien[i][n − 1 − j]", "ancien[n − 1 − i][n − 1 − j]"], a: 1, e: "La colonne de gauche, lue de bas en haut, devient la ligne du haut.", ref: "i6" },
    { q: "Pourquoi la rotation d’image du cours a-t-elle un coût en mémoire (quasi) constant ?", c: ["Elle utilise une seconde image plus petite", "Elle échange les pixels sur place, avec une seule variable auxiliaire", "Elle ne traite qu’un quart de l’image", "Elle compresse l’image"], a: 1, e: "Seule la pile d’appels grandit, de log₂ n + 1 cadres au plus.", ref: "i6" },
    { q: "Lequel de ces algorithmes n’est PAS un « diviser pour régner » ?", c: ["Le tri fusion", "La recherche dichotomique", "Le tri par sélection", "La puissance rapide"], a: 2, e: "Le tri par sélection cherche le minimum et le place, n fois : aucune division en sous-problèmes indépendants.", ref: "i7" }
  ],
  cartes: [
    { r: "Diviser pour régner", v: "Diviser en sous-problèmes du même type, plus petits et indépendants ; les résoudre (récursivement) ; combiner leurs solutions." },
    { r: "Diviser pour régner ou programmation dynamique ?", v: "Sous-problèmes indépendants → diviser pour régner. Sous-problèmes qui se chevauchent → programmation dynamique." },
    { r: "Recherche dichotomique", v: "Tableau trié : on compare au milieu et on ne garde qu’une moitié. Environ log₂ n étapes (20 pour un million)." },
    { r: "Fusion de deux listes triées", v: "Comparer les têtes, prendre la plus petite, avancer ; recopier le reste à la fin. Au plus p + q − 1 comparaisons." },
    { r: "Tri fusion", v: "Liste de 0 ou 1 élément : déjà triée. Sinon : trier t[:m] et t[m:] (m = len(t) // 2), puis fusionner." },
    { r: "Coût du tri fusion", v: "n log₂ n comparaisons au plus, même dans le pire cas (log₂ n niveaux de fusion × n par niveau)." },
    { r: "Coût des tris par insertion et par sélection", v: "De l’ordre de n² (n(n − 1)/2 comparaisons pour la sélection)." },
    { r: "Nombre d’appels du tri fusion sur n éléments", v: "2n − 1 (n feuilles, n − 1 nœuds qui fusionnent)." },
    { r: "Rotation d’un quart de tour (horaire)", v: "nouveau[i][j] = ancien[n − 1 − j][i]." },
    { r: "Rotation d’image sur place", v: "Tourner les 4 quarts récursivement, puis les permuter (HG → HD → BD → BG → HG), 4 pixels à la fois. Mémoire constante." },
    { r: "Ordres de grandeur pour n = 10⁶", v: "log₂ n ≈ 20 ; n log₂ n ≈ 2 × 10⁷ ; n² = 10¹²." },
    { r: "Tri stable", v: "Deux éléments égaux restent dans leur ordre de départ. Le tri fusion l’est avec le test a[i] <= b[j]." },
    { r: "Von Neumann, 1945", v: "Écrit un programme de tri par fusion pour l’EDVAC (d’après Knuth)." }
  ]
});
