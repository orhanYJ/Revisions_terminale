/* ===================== Programmation dynamique ===================== */
C("dyn-fib-naif", String.raw`
calculs = {}                         # combien de fois chaque fib(k) est calculé

def fib(n):
    calculs[n] = calculs.get(n, 0) + 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
for k in range(10, -1, -1):
    print("fib(" + str(k) + ") calculé", calculs[k], "fois")`, { out: String.raw`
55
fib(10) calculé 1 fois
fib(9) calculé 1 fois
fib(8) calculé 2 fois
fib(7) calculé 3 fois
fib(6) calculé 5 fois
fib(5) calculé 8 fois
fib(4) calculé 13 fois
fib(3) calculé 21 fois
fib(2) calculé 34 fois
fib(1) calculé 55 fois
fib(0) calculé 34 fois` });

C("dyn-memo", String.raw`
appels = 0

def fib_memo(n, memo):
    """memo est un dictionnaire {k: fib(k)} des valeurs déjà calculées."""
    global appels
    appels = appels + 1
    if n in memo:                    # déjà calculé : on le relit
        return memo[n]
    if n < 2:
        resultat = n
    else:
        resultat = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = resultat               # on le note avant de le renvoyer
    return resultat

for n in [10, 30, 90]:
    appels = 0
    print(n, fib_memo(n, {}), appels)`, { out: "10 55 19\n30 832040 59\n90 2880067194370816120 179" });

C("dyn-asc", String.raw`
def fib_table(n):
    """Méthode ascendante : on remplit le tableau f du plus petit au plus grand."""
    f = [0] * (n + 1)
    if n >= 1:
        f[1] = 1
    for k in range(2, n + 1):
        f[k] = f[k - 1] + f[k - 2]   # les deux valeurs sont déjà dans le tableau
    return f

print(fib_table(10))
print(fib_table(100)[100])`, { out: "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]\n354224848179261915075" });

C("dyn-asc2", String.raw`
def fib_deux(n):
    a, b = 0, 1                      # a = fib(k), b = fib(k + 1)
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_deux(10), fib_deux(100) == 354224848179261915075)`, { out: "55 True" });

C("dyn-glouton", String.raw`
def rendu_glouton(s, pieces):
    """pieces est triée dans l'ordre DÉCROISSANT. Prend toujours la plus grosse pièce possible."""
    res = []
    for p in pieces:
        while s >= p:
            res.append(p)
            s = s - p
    return res

euros = [200, 100, 50, 20, 10, 5, 2, 1]          # en centimes... ou en euros
print(rendu_glouton(289, euros))
print(rendu_glouton(6, [4, 3, 1]))               # 3 pièces, alors que 3 + 3 suffit`, { out: "[200, 50, 20, 10, 5, 2, 2]\n[4, 1, 1]" });

C("dyn-monnaie-rec", String.raw`
appels = 0

def rendu_rec(s, pieces):
    """Nombre minimal de pièces pour rendre s (une pièce de 1 est disponible)."""
    global appels
    appels = appels + 1
    if s == 0:
        return 0
    meilleur = s                                  # au pire : s pièces de 1
    for p in pieces:
        if p <= s:
            meilleur = min(meilleur, 1 + rendu_rec(s - p, pieces))
    return meilleur

for s in [6, 20, 30]:
    appels = 0
    print(s, rendu_rec(s, [1, 3, 4]), appels)`, { out: "6 2 24\n20 5 20736\n30 8 2550408" });

C("dyn-monnaie-memo", String.raw`
def rendu_memo(s, pieces, memo):
    if s == 0:
        return 0
    if s not in memo:
        meilleur = s
        for p in pieces:
            if p <= s:
                meilleur = min(meilleur, 1 + rendu_memo(s - p, pieces, memo))
        memo[s] = meilleur
    return memo[s]

print(rendu_memo(30, [1, 3, 4], {}), rendu_memo(900, [1, 3, 4], {}))`, { out: "8 225" });

C("dyn-monnaie", String.raw`
def rendu_dyn(S, pieces):
    """nb[s] = nombre minimal de pièces pour rendre s ; choix[s] = une pièce à donner en premier."""
    nb = [0] + [S + 1] * S           # S + 1 joue le rôle de « l'infini »
    choix = [0] * (S + 1)
    for s in range(1, S + 1):        # du plus petit montant au plus grand
        for p in pieces:
            if p <= s and nb[s - p] + 1 < nb[s]:
                nb[s] = nb[s - p] + 1
                choix[s] = p
    return nb, choix

def pieces_rendues(S, choix):
    res = []
    while S > 0:
        res.append(choix[S])
        S = S - choix[S]
    return res

nb, choix = rendu_dyn(10, [1, 3, 4])
print(nb)
print(choix)
print(pieces_rendues(6, choix), pieces_rendues(10, choix))`, { out: "[0, 1, 2, 1, 1, 2, 2, 2, 2, 3, 3]\n[0, 1, 1, 3, 4, 1, 3, 3, 4, 1, 3]\n[3, 3] [3, 3, 4]" });

C("dyn-lcs", String.raw`
def plssc(a, b):
    """Table L : L[i][j] = longueur de la plus longue sous-séquence commune
    à a[:i] (les i premiers caractères de a) et b[:j]."""
    n, m = len(a), len(b)
    L = [[0] * (m + 1) for _ in range(n + 1)]   # ligne 0 et colonne 0 : mot vide
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:                 # même dernier caractère
                L[i][j] = L[i - 1][j - 1] + 1
            else:                                    # on renonce à l'un des deux
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L

def reconstruire(a, b, L):
    """Remonte la table depuis la case en bas à droite."""
    i, j, res = len(a), len(b), []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            res.append(a[i - 1])
            i, j = i - 1, j - 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
    return "".join(reversed(res))

L = plssc("PYTHON", "PHOTON")
for ligne in L:
    print(ligne)
print(L[6][6], reconstruire("PYTHON", "PHOTON", L))`, { out: String.raw`
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 2, 2, 2]
[0, 1, 2, 2, 2, 2, 2]
[0, 1, 2, 3, 3, 3, 3]
[0, 1, 2, 3, 3, 3, 4]
4 PTON` });

C("dyn-adn", String.raw`
a = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
b = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
L = plssc(a, b)
s = reconstruire(a, b, L)
print(len(a), len(b), L[len(a)][len(b)], s)`, { deps: ["dyn-lcs"], out: "29 28 20 GTCGTCGGAAGCCGGCCGAA" });

C("dyn-align", String.raw`
def alignement(a, b, ident=1, diff=-1, trou=-1):
    """Score maximal d'un alignement de a et b, et un alignement qui l'atteint."""
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = i * trou                       # a[:i] aligné face à des trous
    for j in range(1, m + 1):
        S[0][j] = j * trou
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = S[i - 1][j - 1] + (ident if a[i - 1] == b[j - 1] else diff)
            S[i][j] = max(diag, S[i - 1][j] + trou, S[i][j - 1] + trou)
    i, j, ha, hb = n, m, "", ""                  # reconstruction depuis la fin
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i][j] == S[i - 1][j - 1] + (ident if a[i - 1] == b[j - 1] else diff):
            ha, hb = a[i - 1] + ha, b[j - 1] + hb
            i, j = i - 1, j - 1
        elif i > 0 and S[i][j] == S[i - 1][j] + trou:
            ha, hb = a[i - 1] + ha, "-" + hb
            i = i - 1
        else:
            ha, hb = "-" + ha, b[j - 1] + hb
            j = j - 1
    return S[n][m], ha, hb

score, ha, hb = alignement("GATTACA", "GCATGCA")
print(score)
print(ha)
print(hb)`, { out: "2\nG-ATTACA\nGCA-TGCA" });

/* pièges */
C("dyn-p-defaut", String.raw`
def fib_memo(n, memo={}):            # dictionnaire par défaut : créé UNE SEULE fois
    if n not in memo:
        memo[n] = n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print(fib_memo(5))
print(len(fib_memo.__defaults__[0]))   # le dictionnaire a survécu à l'appel`, { out: "5\n6" });

C("dyn-p-ordre", String.raw`
def fib_table_faux(n):
    f = [0] * (n + 1)
    f[1] = 1
    for k in range(n, 1, -1):        # du plus grand au plus petit : mauvais sens
        f[k] = f[k - 1] + f[k - 2]
    return f[n]

print(fib_table_faux(10))`, { out: "0" });

C("dyn-p-copie", String.raw`
L = [[0] * 3] * 2                    # deux fois LA MÊME ligne
L[0][0] = 7
print(L)
L = [[0] * 3 for _ in range(2)]      # deux lignes distinctes
L[0][0] = 7
print(L)`, { out: "[[7, 0, 0], [7, 0, 0]]\n[[7, 0, 0], [0, 0, 0]]" });

/* prédis la sortie */
C("dyn-x1", String.raw`
memo = {}

def f(n):
    if n <= 2:
        return 1
    if n not in memo:
        memo[n] = f(n - 1) + f(n - 3)
    return memo[n]

print(f(7), sorted(memo.keys()))`, { out: "9 [3, 4, 5, 6, 7]" });

C("dyn-x2", String.raw`
t = [1] * 6
for k in range(2, 6):
    t[k] = t[k - 1] + 2 * t[k - 2]
print(t)`, { out: "[1, 1, 3, 5, 11, 21]" });

C("dyn-x3", String.raw`
def chemins(n, m):
    c = [[1] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c[i][j] = c[i - 1][j] + c[i][j - 1]
    return c[n][m]

print(chemins(2, 2), chemins(3, 3))`, { out: "6 20" });

C("dyn-x4", String.raw`
print(rendu_glouton(8, [6, 4, 1]), rendu_dyn(8, [1, 4, 6])[0][8])`, { deps: ["dyn-glouton", "dyn-monnaie"], out: "[6, 1, 1] 2" });

/* épreuve pratique 1 */
C("dyn-ep1-fourni", String.raw`
def rendu_dyn(S, pieces):
    """Renvoie la liste nb où nb[s] est le nombre minimal de pièces
    pour rendre la somme s, pour s de 0 à S. La pièce 1 est dans pieces."""
    nb = [0] * (S + 1)
    for s in range(1, S + 1):
        nb[s] = ...
        for p in pieces:
            if ...:
                nb[s] = ...
    return nb

print(rendu_dyn(12, [1, 5, 6, 9]))`, { fichier: "monnaie.py", run: false, trous: [6, 8, 9] });

C("dyn-ep1-corr", String.raw`
def rendu_dyn(S, pieces):
    nb = [0] * (S + 1)
    for s in range(1, S + 1):
        nb[s] = s                                   # au pire, s pièces de 1
        for p in pieces:
            if p <= s and nb[s - p] + 1 < nb[s]:
                nb[s] = nb[s - p] + 1
    return nb

def rendu_glouton(s, pieces):
    res = []
    for p in sorted(pieces, reverse=True):
        while s >= p:
            res.append(p)
            s = s - p
    return res

def premier_contre_exemple(pieces, maxi):
    """Plus petite somme où le glouton n'est pas optimal, ou None."""
    nb = rendu_dyn(maxi, pieces)
    for s in range(1, maxi + 1):
        if len(rendu_glouton(s, pieces)) > nb[s]:
            return s
    return None

def test():
    nb = rendu_dyn(12, [1, 5, 6, 9])
    assert nb[0] == 0 and nb[1] == 1 and nb[5] == 1
    assert nb[10] == 2                              # 5 + 5 (le glouton donne 9 + 1 : 2 aussi)
    assert nb[11] == 2                              # 5 + 6
    assert nb[12] == 2                              # 6 + 6 (le glouton : 9 + 1 + 1 + 1)
    assert premier_contre_exemple([1, 5, 6, 9], 50) == 11
    assert premier_contre_exemple([1, 2, 5, 10, 20, 50, 100, 200], 500) is None
    assert premier_contre_exemple([1, 3, 4], 20) == 6

test()
print(rendu_dyn(12, [1, 5, 6, 9]))
print("tous les tests passent")`, { fichier: "monnaie.py", out: "[0, 1, 2, 3, 4, 1, 1, 2, 3, 1, 2, 2, 2]\ntous les tests passent" });

/* épreuve pratique 2 */
C("dyn-ep2-fourni", String.raw`
def plssc_rec(a, b):
    """Longueur de la plus longue sous-séquence commune à a et b."""
    if a == "" or b == "":
        return 0
    if a[-1] == b[-1]:
        return 1 + plssc_rec(a[:-1], b[:-1])
    return max(plssc_rec(a[:-1], b), plssc_rec(a, b[:-1]))

print(plssc_rec("CHIEN", "NICHE"))
print(plssc_rec("ABCDEFGHIJKLMNOP", "PONMLKJIHGFEDCBA"))   # très long...`, { fichier: "sous_sequence.py", run: false });

C("dyn-ep2-corr", String.raw`
def plssc_memo(a, b, memo=None):
    if memo is None:
        memo = {}
    if a == "" or b == "":
        return 0
    if (a, b) not in memo:
        if a[-1] == b[-1]:
            memo[(a, b)] = 1 + plssc_memo(a[:-1], b[:-1], memo)
        else:
            memo[(a, b)] = max(plssc_memo(a[:-1], b, memo), plssc_memo(a, b[:-1], memo))
    return memo[(a, b)]

def table(a, b):
    L = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L

def sous_sequence(a, b):
    L = table(a, b)
    i, j, res = len(a), len(b), ""
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            res = a[i - 1] + res
            i, j = i - 1, j - 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
    return res

def est_sous_sequence(s, mot):
    k = 0
    for c in mot:
        if k < len(s) and c == s[k]:
            k = k + 1
    return k == len(s)

def test():
    assert plssc_memo("CHIEN", "NICHE") == 3
    assert plssc_memo("ABCDEFGHIJKLMNOP", "PONMLKJIHGFEDCBA") == 1
    assert plssc_memo("", "ABC") == 0
    for a, b in [("CHIEN", "NICHE"), ("PYTHON", "PHOTON"), ("ACGTTGCA", "TGCATGCA")]:
        s = sous_sequence(a, b)
        assert len(s) == plssc_memo(a, b) == table(a, b)[len(a)][len(b)]
        assert est_sous_sequence(s, a) and est_sous_sequence(s, b)

test()
print(sous_sequence("CHIEN", "NICHE"), sous_sequence("ACGTTGCA", "TGCATGCA"))
print("tous les tests passent")`, { fichier: "sous_sequence.py", out: "CHE ATGCA\ntous les tests passent" });

/* épreuve écrite */
C("dyn-ecrit-corr", String.raw`
pyramide = [[3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]]

def somme_max_rec(p, i, j):
    """Meilleure somme d'un chemin qui part de la case (i, j) et descend jusqu'en bas."""
    if i == len(p) - 1:
        return p[i][j]
    return p[i][j] + max(somme_max_rec(p, i + 1, j), somme_max_rec(p, i + 1, j + 1))

def somme_max(p):
    """Version ascendante : on remonte la pyramide depuis la dernière ligne."""
    meilleur = p[-1][:]                         # copie de la dernière ligne
    for i in range(len(p) - 2, -1, -1):
        meilleur = [p[i][j] + max(meilleur[j], meilleur[j + 1]) for j in range(i + 1)]
    return meilleur[0]

print(somme_max_rec(pyramide, 0, 0), somme_max(pyramide))`, { out: "23 23" });

C("dyn-retenir", String.raw`
# descendante (mémoïsation)              # ascendante (tableau)
def f(n, memo):                          def f(n):
    if n in memo:                            t = [0] * (n + 1)
        return memo[n]                       t[0] = ...      # cas de base
    if cas de base:                          for k in range(1, n + 1):
        return ...                               t[k] = ...  # à partir de t[k-1], t[k-2]...
    memo[n] = ... f(...) ...                 return t[n]
    return memo[n]`, { run: false });

CH.push({
  id: "dyn", n: 14, court: "prog_dynamique", fichier: "prog_dynamique.py",
  titre: "Programmation dynamique",
  rubrique: "Rubrique « Algorithmique » : programmation dynamique (rendu de monnaie, alignement de séquences)",
  accroche: "Ne jamais calculer deux fois la même chose : mémoïsation, tableau rempli du plus petit au plus grand, rendu de monnaie, plus longue sous-séquence commune, alignement.",
  essentiel: [
    "La <b>programmation dynamique</b> s’applique quand un problème se ramène à des sous-problèmes qui <b>se chevauchent</b> : on <b>mémorise</b> chaque résultat pour ne jamais le recalculer.",
    "Deux façons de faire : <b>descendante</b> (récursion + mémoïsation dans un dictionnaire) ou <b>ascendante</b> (remplir un tableau du plus petit sous-problème au plus grand).",
    "La clé est la <b>relation de récurrence</b> : exprimer la solution d’un problème avec celles de problèmes plus petits.",
    "<b>Rendu de monnaie</b> : nb[s] = 1 + min(nb[s − p]) sur les pièces p ≤ s ; l’algorithme glouton, lui, n’est pas toujours optimal (6 avec 1, 3, 4).",
    "<b>Plus longue sous-séquence commune</b> et <b>alignement de séquences</b> : une table (n + 1) × (m + 1) remplie ligne par ligne, puis une remontée pour retrouver la solution. On échange du <b>temps</b> contre de la <b>mémoire</b>."
  ],
  attendus: [
    "Utiliser la programmation dynamique pour écrire un algorithme (capacité du BO).",
    "Les exemples du programme : <b>alignement de séquences</b> et <b>rendu de monnaie</b>.",
    "Le programme invite à <b>discuter le coût en mémoire</b> : un tableau ou un dictionnaire de résultats, parfois réductible à quelques variables.",
    "Savoir distinguer programmation dynamique, « diviser pour régner » (sous-problèmes indépendants) et algorithme glouton (choix local jamais remis en cause, vu en Première)."
  ],
  idees: [
    { id: "i1", t: "Le problème : des calculs répétés", h: `
<p>La définition de Fibonacci (F(0) = 0, F(1) = 1, F(<i>n</i>) = F(<i>n</i> − 1) + F(<i>n</i> − 2)) se traduit directement en une fonction récursive. Comptons combien de fois chaque valeur est recalculée pour F(10) :</p>
[[dyn-fib-naif]]
<p>F(1) est calculé 55 fois, F(2) 34 fois : ce sont… les nombres de Fibonacci eux-mêmes, qui croissent de façon <b>exponentielle</b> (environ × 1,618 à chaque rang). Le problème n’est pas la récursivité, c’est que les sous-problèmes F(<i>n</i> − 1) et F(<i>n</i> − 2) <b>se chevauchent</b> : tous deux ont besoin de F(<i>n</i> − 3), et ainsi de suite.</p>
<div class="boite def"><div class="lab">"""définition"""</div><p>La <b>programmation dynamique</b> résout un problème en le décomposant en sous-problèmes qui <b>se chevauchent</b>, en résolvant chaque sous-problème <b>une seule fois</b> et en <b>mémorisant</b> sa solution pour la réutiliser.</p></div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">années 1950 <b>·</b></span> Le mathématicien américain Richard <b>Bellman</b> invente la méthode et son nom ; son livre <i>Dynamic Programming</i> paraît en 1957. « Programmation » y a le sens de « planification », pas d’écriture de code.</p></div>` },

    { id: "i2", t: "Méthode descendante : la mémoïsation", h: `
<p>On garde la fonction récursive, mais on <b>note</b> chaque résultat dans un dictionnaire <code>memo</code>. Avant de calculer, on regarde si la réponse y est déjà.</p>
[[dyn-memo]]
<p>Pour <i>n</i> = 30 : 59 appels au lieu de 2 692 537. Chaque valeur F(<i>k</i>) n’est calculée qu’une fois, les autres appels la relisent : le coût devient <b>linéaire</b>. En contrepartie, le dictionnaire occupe une case par valeur calculée (mémoire proportionnelle à <i>n</i>), et la pile d’appels monte jusqu’à <i>n</i> niveaux (attention à la limite de 1 000).</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Le module standard <code>functools</code> fournit le décorateur <code>@functools.cache</code> (Python 3.9 et suivants) qui mémoïse automatiquement une fonction. Pratique, mais à l’écrit on attend que tu saches écrire le dictionnaire toi-même.</p></div>` },

    { id: "i3", t: "Méthode ascendante : remplir un tableau", h: `
<p>On peut aussi partir des plus petits sous-problèmes et remonter : on remplit un tableau <code>f</code> de la case 0 à la case <i>n</i>. Quand on calcule <code>f[k]</code>, les cases dont il dépend sont <b>déjà remplies</b>.</p>
[[dyn-asc]]
<p>Plus de récursion, donc plus de limite de pile. Et en regardant les dépendances, on s’aperçoit que seules les <b>deux dernières</b> valeurs servent : on peut réduire la mémoire à deux variables.</p>
[[dyn-asc2]]
<div class="tab-wrap"><table><tr><th>version</th><th>temps</th><th>mémoire</th></tr>
<tr><td>récursive naïve</td><td>exponentiel (2 692 537 appels pour n = 30)</td><td>pile de n cadres</td></tr>
<tr><td>mémoïsation (descendante)</td><td>linéaire</td><td>dictionnaire de n valeurs + pile de n cadres</td></tr>
<tr><td>tableau (ascendante)</td><td>linéaire</td><td>tableau de n + 1 cases</td></tr>
<tr><td>deux variables</td><td>linéaire</td><td>constante</td></tr></table></div>` },

    { id: "i4", t: "Rendu de monnaie : quand le glouton échoue", h: `
<p>Problème : rendre une somme <i>s</i> avec le <b>moins de pièces possible</b>, les valeurs des pièces étant données (et en quantité illimitée). En Première, tu as vu l’algorithme <b>glouton</b> : prendre à chaque fois la plus grosse pièce possible.</p>
[[dyn-glouton]]
<p>Avec les euros, le glouton est toujours optimal (on dit que le système est <b>canonique</b>). Mais avec des pièces de 1, 3 et 4, il rend 6 avec trois pièces (4 + 1 + 1) alors que deux suffisent (3 + 3) : le premier choix, « le plus gros possible », était mauvais, et le glouton ne revient jamais sur un choix.</p>
<p>Il faut donc <b>essayer toutes les premières pièces</b>. Si l’on donne d’abord une pièce <i>p</i>, il reste à rendre <i>s</i> − <i>p</i> de façon optimale. D’où la relation de récurrence :</p>
<div class="boite retenir-b"><div class="lab"># relation de récurrence</div><p>nb(0) = 0 et, pour <i>s</i> &gt; 0 : <b>nb(<i>s</i>) = 1 + min { nb(<i>s</i> − <i>p</i>) : <i>p</i> pièce, <i>p</i> ≤ <i>s</i> }</b>.</p></div>
[[dyn-monnaie-rec]]
<p>La traduction récursive directe est juste mais explose : plus de deux millions d’appels pour 30, parce que nb(26), nb(25)… sont recalculés sans cesse. Avec mémoïsation, chaque montant de 0 à <i>s</i> n’est calculé qu’une fois :</p>
[[dyn-monnaie-memo]]` },

    { id: "i5", t: "Rendu de monnaie : le tableau et la reconstruction", h: `
<p>Version ascendante : on remplit <code>nb[0]</code>, <code>nb[1]</code>, …, <code>nb[S]</code> dans cet ordre. On garde aussi, dans <code>choix[s]</code>, la pièce qui a donné le minimum : cela permet de <b>reconstruire</b> la liste des pièces, et pas seulement leur nombre.</p>
[[dyn-monnaie]]
[[w-algo-table-dyn|monnaie]]
<p>Pour rendre 10 : <code>choix[10]</code> = 3, il reste 7 ; <code>choix[7]</code> = 3, il reste 4 ; <code>choix[4]</code> = 4, il reste 0. Coût : pour chacun des <i>S</i> montants, on essaie les <i>k</i> pièces, soit de l’ordre de <i>S</i> × <i>k</i> opérations ; mémoire : deux tableaux de <i>S</i> + 1 cases.</p>` },

    { id: "i6", t: "La plus longue sous-séquence commune", h: `
<p>Une <b>sous-séquence</b> d’un mot s’obtient en effaçant certaines lettres, sans changer l’ordre des autres : « PHON » est une sous-séquence de « PYTHON » (on efface Y et T). La <b>plus longue sous-séquence commune</b> (PLSC) à deux mots mesure leur ressemblance : on l’utilise pour comparer deux versions d’un fichier (la commande <code>diff</code>) ou deux brins d’ADN.</p>
<p>On note L[<i>i</i>][<i>j</i>] la longueur de la PLSC des <i>i</i> premières lettres de <i>a</i> et des <i>j</i> premières lettres de <i>b</i>. On regarde les <b>dernières</b> lettres :</p>
<ul><li>si elles sont <b>égales</b>, elles font partie d’une PLSC : L[<i>i</i>][<i>j</i>] = L[<i>i</i> − 1][<i>j</i> − 1] + 1 ;</li>
<li>sinon, l’une des deux ne sert pas : L[<i>i</i>][<i>j</i>] = max(L[<i>i</i> − 1][<i>j</i>], L[<i>i</i>][<i>j</i> − 1]) ;</li>
<li>et L[0][<i>j</i>] = L[<i>i</i>][0] = 0 (avec un mot vide, rien en commun).</li></ul>
[[dyn-lcs]]
[[w-algo-table-dyn|lcs]]
<p>On remplit la table ligne par ligne : chaque case dépend de celle du dessus, de celle de gauche et de la diagonale, déjà calculées. Pour <b>retrouver</b> la sous-séquence, on part de la case en bas à droite et on remonte : diagonale quand les lettres sont égales (on note la lettre), sinon vers la plus grande des deux voisines. Coût : <i>n</i> × <i>m</i> cases, chacune en temps constant.</p>
[[dyn-adn]]
<div class="boite ex"><div class="lab"># pourquoi pas la force brute ?</div><p>Un mot de 29 lettres a 2²⁹ (plus de 500 millions) sous-séquences. La table, elle, n’a que 30 × 29 = 870 cases.</p></div>` },

    { id: "i7", t: "L’alignement de séquences", h: `
<p>En biologie, on compare deux séquences d’ADN en les <b>alignant</b> : on les écrit l’une sous l’autre en insérant des <b>trous</b> (notés « - ») pour faire correspondre le plus de lettres possible. On donne un <b>score</b> à chaque colonne, par exemple +1 si les lettres sont identiques, −1 si elles diffèrent, −1 pour un trou ; on cherche l’alignement de <b>score maximal</b>.</p>
<p>Même raisonnement que pour la PLSC, sur la dernière colonne de l’alignement : soit elle aligne les deux dernières lettres, soit la dernière lettre de <i>a</i> face à un trou, soit un trou face à la dernière lettre de <i>b</i>. D’où :</p>
<div class="boite retenir-b"><div class="lab"># relation de récurrence</div><p>S[<i>i</i>][<i>j</i>] = max( S[<i>i</i> − 1][<i>j</i> − 1] + (1 ou −1), S[<i>i</i> − 1][<i>j</i>] − 1, S[<i>i</i>][<i>j</i> − 1] − 1 ), avec S[<i>i</i>][0] = −<i>i</i> et S[0][<i>j</i>] = −<i>j</i>.</p></div>
[[dyn-align]]
<p>Lecture de l’alignement obtenu, colonne par colonne : G/G, -/C, A/A, T/-, T/T, A/G, C/C, A/A. Cinq colonnes identiques (+5), une différence A/G (−1), deux trous (−2) : score <b>2</b>. Plusieurs alignements peuvent avoir le même score maximal ; la remontée en donne un.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1970 <b>·</b></span> Saul <b>Needleman</b> et Christian <b>Wunsch</b> publient cet algorithme d’alignement de séquences de protéines : c’est l’un des fondements de la bio-informatique.</p></div>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Avec un score de 1 pour une égalité et 0 pour une différence ou un trou, le score maximal est exactement la longueur de la PLSC. Et la <b>distance d’édition</b> (de Levenshtein, 1965), qui compte le nombre minimal d’insertions, suppressions et substitutions pour passer d’un mot à l’autre, se calcule avec la même table : c’est ce qu’utilisent les correcteurs orthographiques.</p></div>` },

    { id: "i8", t: "Reconnaître un problème de programmation dynamique", h: `
<div class="boite retenir-b"><div class="lab"># méthode en quatre étapes</div>
<ol><li><b>Définir le sous-problème</b> par quelques paramètres : nb[<i>s</i>] pour un montant, L[<i>i</i>][<i>j</i>] pour deux préfixes.</li>
<li><b>Écrire la relation de récurrence</b> (avec les cas de base) en raisonnant sur un « dernier choix » : la dernière pièce, la dernière lettre, la dernière colonne.</li>
<li><b>Choisir l’ordre de calcul</b> pour que chaque case ne dépende que de cases déjà remplies (montants croissants, lignes du haut vers le bas).</li>
<li><b>Reconstruire</b> la solution si on la demande (garder le choix fait, ou remonter la table).</li></ol></div>
<div class="tab-wrap"><table><tr><th>méthode</th><th>sous-problèmes</th><th>exemple</th></tr>
<tr><td>diviser pour régner</td><td>indépendants</td><td>tri fusion</td></tr>
<tr><td>programmation dynamique</td><td>qui se chevauchent, chacun résolu une fois</td><td>rendu de monnaie optimal, PLSC</td></tr>
<tr><td>glouton</td><td>un seul choix local à chaque étape, jamais remis en cause</td><td>rendu de monnaie en euros</td></tr></table></div>
<p>Signes qui doivent t’alerter à l’écrit : « nombre minimal / maximal », « meilleur », « nombre de façons », une fonction récursive à <b>plusieurs appels</b> dont les arguments se recoupent, une question « que peut-on reprocher à cette fonction ? ».</p>` }
  ],
  pieges: [
    { t: "Un dictionnaire comme valeur par défaut", h: `[[dyn-p-defaut]]<p>La valeur par défaut <code>memo={}</code> est créée <b>une seule fois</b>, à la définition de la fonction : elle est partagée par tous les appels suivants. Ici c’est sans danger (les valeurs de Fibonacci ne changent pas), mais si la fonction a d’autres paramètres (les pièces !), les résultats d’un appel pollueront le suivant. Écris <code>memo=None</code> puis <code>if memo is None: memo = {}</code>, ou passe le dictionnaire explicitement.</p>` },
    { t: "Remplir le tableau dans le mauvais ordre", h: `[[dyn-p-ordre]]<p>En partant de <code>k = n</code>, on utilise <code>f[k − 1]</code> et <code>f[k − 2]</code> qui valent encore 0. Dans la méthode ascendante, l’ordre de remplissage est <b>imposé</b> par les dépendances.</p>` },
    { t: "Créer une table avec [[0] * m] * n", h: `[[dyn-p-copie]]<p>Le <code>* 2</code> recopie la <b>référence</b> à la même liste : modifier une case modifie toute la colonne. Pour une table, utilise toujours une liste en compréhension.</p>` },
    { t: "Oublier le décalage d’indice entre la table et le mot", h: `<p>La table L a <i>n</i> + 1 lignes : la ligne <i>i</i> correspond aux <i>i</i> premières lettres, dont la dernière est <code>a[i - 1]</code>. Comparer <code>a[i]</code> et <code>b[j]</code> décale tout (et provoque un <code>IndexError</code> à la dernière ligne).</p>` },
    { t: "Croire que le glouton est toujours optimal", h: `<p>Il l’est pour les euros, pas pour n’importe quel système. Pour prouver qu’un algorithme glouton n’est pas optimal, <b>un seul contre-exemple suffit</b> : 6 avec {1, 3, 4}, 8 avec {1, 4, 6} (6 + 1 + 1 contre 4 + 4).</p>` }
  ],
  retenir: `
<h2>Les deux squelettes</h2>
[[dyn-retenir]]
<h2>Les relations à connaître</h2>
<div class="tab-wrap"><table><tr><th>problème</th><th>sous-problème</th><th>récurrence</th><th>coût</th></tr>
<tr><td>Fibonacci</td><td>F(k)</td><td>F(k) = F(k − 1) + F(k − 2), F(0) = 0, F(1) = 1</td><td>n</td></tr>
<tr><td>rendu de monnaie</td><td>nb[s]</td><td>nb[0] = 0 ; nb[s] = 1 + min nb[s − p] (p ≤ s)</td><td>S × nombre de pièces</td></tr>
<tr><td>PLSC</td><td>L[i][j]</td><td>lettres égales : L[i−1][j−1] + 1 ; sinon max(L[i−1][j], L[i][j−1])</td><td>n × m</td></tr>
<tr><td>alignement</td><td>S[i][j]</td><td>max(diagonale + identité ou différence, haut + trou, gauche + trou)</td><td>n × m</td></tr></table></div>
<h2>Vocabulaire</h2>
<ul><li><b>Sous-problèmes qui se chevauchent</b> : le même sous-problème sert plusieurs fois.</li><li><b>Mémoïsation</b> : mémoriser les résultats déjà calculés (dictionnaire) ; méthode descendante.</li><li><b>Méthode ascendante</b> : remplir un tableau du plus petit sous-problème au plus grand.</li><li><b>Reconstruction</b> : retrouver la solution elle-même (pièces, lettres) en gardant les choix ou en remontant la table.</li><li><b>Glouton</b> : choix local jamais remis en cause ; rapide, pas toujours optimal (6 avec {1, 3, 4}).</li></ul>`,
  predis: [
    { code: "dyn-x1", niv: "facile", rep: "Attention, la relation est f(n − 1) + f(n − 3), et f(n) = 1 pour n ≤ 2 (y compris f(0)). f(3) = f(2) + f(0) = 2 ; f(4) = f(3) + f(1) = 3 ; f(5) = f(4) + f(2) = 4 ; f(6) = f(5) + f(3) = 6 ; f(7) = f(6) + f(4) = 9. Les clés mémorisées sont 3 à 7 : les cas n ≤ 2 renvoient 1 sans être stockés." },
    { code: "dyn-x2", niv: "facile", rep: "t[2] = 1 + 2 × 1 = 3, t[3] = 3 + 2 × 1 = 5, t[4] = 5 + 2 × 3 = 11, t[5] = 11 + 2 × 5 = 21. Chaque case est calculée à partir des deux précédentes, déjà remplies." },
    { code: "dyn-x3", niv: "moyen", rep: "c[i][j] compte les chemins de (0, 0) à (i, j) en n’allant que vers le bas ou la droite : on arrive par le haut ou par la gauche. chemins(2, 2) = 6 et chemins(3, 3) = 20 (ce sont les coefficients binomiaux C(4, 2) et C(6, 3))." },
    { code: "dyn-x4", niv: "moyen", rep: "Le glouton prend 6, puis 1 et 1 : trois pièces. La programmation dynamique trouve 4 + 4 : deux pièces. nb[8] vaut 2." }
  ],
  ep: [
    { titre: "Rendu de monnaie optimal", enonce: `<p>On dispose de pièces de 1, 5, 6 et 9 unités, en quantité illimitée.</p>[[dyn-ep1-fourni]]`,
      questions: [
        { q: "Combien de pièces l’algorithme glouton rend-il pour 12 ? Est-ce optimal ?", c: `<p>Glouton : 9, puis 1, 1, 1 : <b>4 pièces</b>. Or 6 + 6 en fait 2 : le glouton n’est pas optimal pour ce système.</p>` },
        { q: "Compléter les lignes 6, 8 et 9 de <code>rendu_dyn</code>.", c: `<p>Ligne 6 : <code>nb[s] = s</code> (au pire <i>s</i> pièces de 1). Ligne 8 : <code>p &lt;= s and nb[s - p] + 1 &lt; nb[s]</code>. Ligne 9 : <code>nb[s - p] + 1</code>.</p>` },
        { q: "Écrire <code>rendu_glouton(s, pieces)</code> puis <code>premier_contre_exemple(pieces, maxi)</code> qui renvoie la plus petite somme pour laquelle le glouton n’est pas optimal (ou <code>None</code>). Tester sur trois systèmes, dont les euros.", c: `[[dyn-ep1-corr]]<p>Pour {1, 5, 6, 9}, la première somme mal rendue est 11 : le glouton donne 9 + 1 + 1, alors que 5 + 6 suffit.</p>` },
        { q: "À l’oral : quel est le coût en temps et en mémoire de <code>rendu_dyn(S, pieces)</code> ? Pourquoi est-ce de la programmation dynamique ?", c: `<p>Temps : <i>S</i> × <i>k</i> (pour <i>k</i> pièces). Mémoire : un tableau de <i>S</i> + 1 cases. C’est de la programmation dynamique car nb[<i>s</i>] se déduit de sous-problèmes nb[<i>s</i> − <i>p</i>] qui se chevauchent (nb[3] sert pour nb[4], nb[8], nb[9]…), chacun calculé une seule fois.</p>` }
      ] },
    { titre: "Plus longue sous-séquence commune", enonce: `<p>On fournit une fonction récursive qui calcule la longueur de la plus longue sous-séquence commune (PLSC) à deux mots.</p>[[dyn-ep2-fourni]]`,
      questions: [
        { q: "Exécuter le programme. Que constate-t-on pour le second appel ? Pourquoi ?", c: `<p>Le premier appel renvoie 3 (« CHE ») presque immédiatement ; le second ne se termine pas en un temps raisonnable. Quand les dernières lettres diffèrent, la fonction fait <b>deux</b> appels, qui recalculent les mêmes couples de préfixes : le nombre d’appels est exponentiel. Ici toutes les dernières lettres diffèrent jusqu’au bout, c’est le pire cas.</p>` },
        { q: "Écrire <code>plssc_memo(a, b, memo=None)</code> qui mémorise les résultats dans un dictionnaire indexé par le couple <code>(a, b)</code>.", c: `<p>Même code, avec un test <code>if (a, b) not in memo</code> avant le calcul et un stockage dans <code>memo[(a, b)]</code>. Il y a au plus (<i>n</i> + 1)(<i>m</i> + 1) couples de préfixes : 289 pour deux mots de 16 lettres.</p>` },
        { q: "Écrire une version ascendante <code>table(a, b)</code> et une fonction <code>sous_sequence(a, b)</code> qui renvoie une PLSC. Écrire <code>est_sous_sequence(s, mot)</code> et l’utiliser dans les tests.", c: `[[dyn-ep2-corr]]` },
        { q: "À l’oral : pourquoi ne peut-on pas énumérer toutes les sous-séquences de <code>a</code> et tester si elles sont dans <code>b</code> ?", c: `<p>Un mot de <i>n</i> lettres a 2<sup>n</sup> sous-séquences (chaque lettre est gardée ou effacée) : plus d’un million pour 20 lettres, plus d’un milliard pour 30. La table, elle, a (<i>n</i> + 1)(<i>m</i> + 1) cases.</p>` }
      ] }
  ],
  ecrit: { titre: "La pyramide de nombres", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Une pyramide de nombres est représentée par une liste de listes : la ligne <i>i</i> (numérotée à partir de 0) contient <i>i</i> + 1 nombres. On part du sommet et on descend jusqu’à la dernière ligne ; depuis la case (<i>i</i>, <i>j</i>), on peut aller en (<i>i</i> + 1, <i>j</i>) ou en (<i>i</i> + 1, <i>j</i> + 1). On cherche la plus grande somme possible des nombres rencontrés.</p>
<pre class="petit">        3
      7   4
    2   4   6
  8   5   9   3</pre>
<p>Cette pyramide s’écrit <code>pyramide = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]</code>.</p>`,
    questions: [
      { q: "Combien de chemins différents y a-t-il dans une pyramide de 4 lignes ? De <i>n</i> lignes ?", pts: "0,5 pt", c: `<p>À chacune des 3 descentes, 2 choix : 2³ = <b>8 chemins</b> ; pour <i>n</i> lignes, 2<sup>n−1</sup>. Pour 100 lignes, 2⁹⁹ ≈ 6 × 10²⁹ chemins : impossible de tous les essayer.</p>` },
      { q: "Un élève propose de descendre toujours vers le plus grand des deux voisins. Quelle somme obtient-il ? Est-ce la meilleure ?", pts: "1 pt", c: `<p>3 → 7 → 4 → 9 : somme <b>23</b>. Ici c’est optimal, mais ce n’est pas garanti : avec <code>[[1], [2, 1], [1, 1, 50]]</code>, le glouton fait 1 → 2 → 1 = 4, alors que 1 → 1 → 50 = 52. C’est un algorithme glouton.</p>` },
      { q: "On note M(<i>i</i>, <i>j</i>) la meilleure somme d’un chemin qui part de la case (<i>i</i>, <i>j</i>). Donner M sur la dernière ligne, puis une relation entre M(<i>i</i>, <i>j</i>), M(<i>i</i> + 1, <i>j</i>) et M(<i>i</i> + 1, <i>j</i> + 1).", pts: "1,5 pt", c: `<p>Sur la dernière ligne : M(<i>i</i>, <i>j</i>) = p[<i>i</i>][<i>j</i>]. Sinon : <b>M(<i>i</i>, <i>j</i>) = p[<i>i</i>][<i>j</i>] + max(M(<i>i</i> + 1, <i>j</i>), M(<i>i</i> + 1, <i>j</i> + 1))</b>. La réponse est M(0, 0).</p>` },
      { q: "Écrire une fonction récursive <code>somme_max_rec(p, i, j)</code>. Expliquer pourquoi elle est inefficace.", pts: "1 pt", c: `<p>Elle traduit la relation. Mais la case (2, 1) est atteinte depuis (1, 0) et depuis (1, 1) : M(2, 1) est calculé deux fois, et les recalculs se multiplient en descendant (sous-problèmes qui se chevauchent). Le nombre d’appels est 2<sup>n</sup> − 1.</p>` },
      { q: "Écrire une fonction <code>somme_max(p)</code> en programmation dynamique, sans récursion, qui remonte la pyramide depuis la dernière ligne. Donner son coût et sa mémoire.", pts: "2 pts", c: `<p>On garde une liste <code>meilleur</code> des valeurs M de la ligne en dessous et on calcule celle de la ligne courante. Coût : une opération par case, soit <i>n</i>(<i>n</i> + 1)/2 ; mémoire : une ligne de <i>n</i> valeurs. On trouve 23.</p>[[dyn-ecrit-corr]]` }
    ],
    methode: `<p>Dans un sujet, la programmation dynamique arrive souvent en trois temps : une version récursive à analyser (« pourquoi est-elle lente ? » → sous-problèmes qui se chevauchent, coût exponentiel), une relation de récurrence à écrire, une version avec mémoïsation ou tableau. Écris toujours les <b>cas de base</b> et précise l’<b>ordre de remplissage</b>.</p>` },
  qcm: [
    { q: "Quand utilise-t-on la programmation dynamique ?", c: ["Quand les sous-problèmes sont indépendants", "Quand les sous-problèmes se chevauchent", "Quand il n’y a qu’un seul sous-problème", "Uniquement pour trier"], a: 1, e: "On mémorise alors chaque sous-problème pour ne le résoudre qu’une fois.", ref: "i1" },
    { q: "Dans le calcul naïf de fib(10), combien de fois fib(1) est-il calculé ?", c: ["1", "10", "55", "89"], a: 2, e: "Le nombre de calculs de fib(1) vaut fib(10) = 55.", ref: "i1" },
    { q: "Qu’est-ce que la mémoïsation ?", c: ["Apprendre un algorithme par cœur", "Mémoriser les résultats déjà calculés pour ne pas les recalculer", "Vider la mémoire après chaque appel", "Écrire les résultats dans un fichier"], a: 1, e: "Typiquement dans un dictionnaire, consulté avant chaque calcul.", ref: "i2" },
    { q: "Quel est le coût de fib_memo(n) ?", c: ["Exponentiel", "Linéaire", "Constant", "Quadratique"], a: 1, e: "Chaque valeur de 0 à n n’est calculée qu’une fois.", ref: "i2" },
    { q: "Dans la méthode ascendante, dans quel ordre remplit-on le tableau ?", c: ["Du plus grand sous-problème au plus petit", "Du plus petit au plus grand, pour que les cases utilisées soient déjà remplies", "Au hasard", "En commençant par le milieu"], a: 1, e: "L’ordre est imposé par les dépendances de la relation de récurrence.", ref: "i3" },
    { q: "Avec des pièces de 1, 3 et 4, combien de pièces l’algorithme glouton rend-il pour 6 ?", c: ["2", "3", "4", "6"], a: 1, e: "4 + 1 + 1 : 3 pièces, alors que 3 + 3 en demande 2.", ref: "i4" },
    { q: "Quelle relation donne le nombre minimal de pièces nb(s) ?", c: ["nb(s) = nb(s − 1) + 1", "nb(s) = 1 + min nb(s − p) sur les pièces p ≤ s", "nb(s) = s // plus grande pièce", "nb(s) = max nb(s − p)"], a: 1, e: "On essaie toutes les premières pièces possibles et on garde la meilleure.", ref: "i4" },
    { q: "À quoi sert le tableau <code>choix</code> dans rendu_dyn ?", c: ["À accélérer le calcul", "À reconstruire les pièces à rendre, pas seulement leur nombre", "À trier les pièces", "À éviter la récursion"], a: 1, e: "choix[s] est une pièce optimale à donner en premier ; on recommence avec s − choix[s].", ref: "i5" },
    { q: "Quel est le coût de rendu_dyn(S, pieces) avec k pièces ?", c: ["De l’ordre de S × k", "De l’ordre de kˢ", "De l’ordre de k", "De l’ordre de log S"], a: 0, e: "Pour chacun des S montants, on essaie chacune des k pièces.", ref: "i5" },
    { q: "Quelle est la longueur de la plus longue sous-séquence commune à « PYTHON » et « PHOTON » ?", c: ["2", "3", "4", "6"], a: 2, e: "Par exemple « PTON » (celle que trouve la remontée) ou « PHON ».", ref: "i6" },
    { q: "Si a[i − 1] == b[j − 1], que vaut L[i][j] ?", c: ["L[i − 1][j − 1] + 1", "max(L[i − 1][j], L[i][j − 1])", "L[i − 1][j] + L[i][j − 1]", "0"], a: 0, e: "Les deux dernières lettres égales prolongent une PLSC des préfixes plus courts.", ref: "i6" },
    { q: "Combien de cases a la table de la PLSC pour deux mots de 10 et 20 lettres ?", c: ["30", "200", "231", "2³⁰"], a: 2, e: "(10 + 1) × (20 + 1) = 231, en comptant la ligne et la colonne du mot vide.", ref: "i6" },
    { q: "Dans l’alignement de séquences, que représente le symbole « - » ?", c: ["Une lettre différente", "Un trou (insertion ou suppression)", "La fin de la séquence", "Une lettre inconnue"], a: 1, e: "Un trou face à une lettre de l’autre séquence ; il est pénalisé dans le score.", ref: "i7" },
    { q: "Quelle méthode ne remet jamais en cause un choix fait ?", c: ["La programmation dynamique", "L’algorithme glouton", "La mémoïsation", "La reconstruction"], a: 1, e: "C’est ce qui le rend rapide… et parfois non optimal.", ref: "i8" }
  ],
  cartes: [
    { r: "Programmation dynamique", v: "Résoudre chaque sous-problème une seule fois et mémoriser sa solution. Pour des sous-problèmes qui se chevauchent." },
    { r: "Mémoïsation (méthode descendante)", v: "Fonction récursive + dictionnaire des résultats déjà calculés, consulté avant tout calcul." },
    { r: "Méthode ascendante", v: "Remplir un tableau du plus petit sous-problème au plus grand ; pas de récursion." },
    { r: "Fibonacci : naïf / mémoïsé / ascendant", v: "Exponentiel (2 692 537 appels pour n = 30) / linéaire (59 appels) / linéaire, et mémoire constante avec deux variables." },
    { r: "Rendu de monnaie : récurrence", v: "nb(0) = 0 ; nb(s) = 1 + min nb(s − p) pour les pièces p ≤ s." },
    { r: "Contre-exemple au glouton", v: "Pièces {1, 3, 4}, somme 6 : glouton 4 + 1 + 1 (3 pièces), optimal 3 + 3 (2 pièces)." },
    { r: "Système canonique", v: "Système de pièces pour lequel le glouton est toujours optimal (les euros)." },
    { r: "Sous-séquence", v: "Mot obtenu en effaçant des lettres sans changer l’ordre des autres. « PHON » est une sous-séquence de « PYTHON »." },
    { r: "PLSC : récurrence", v: "L[i][0] = L[0][j] = 0 ; lettres a[i−1] et b[j−1] égales : L[i−1][j−1] + 1 ; sinon max(L[i−1][j], L[i][j−1])." },
    { r: "Coût de la PLSC ou de l’alignement", v: "n × m cases (table (n + 1) × (m + 1)), chacune en temps constant." },
    { r: "Alignement de séquences", v: "Insérer des trous « - » pour maximiser un score (ex. +1 identique, −1 différent, −1 trou). Needleman et Wunsch, 1970." },
    { r: "Reconstruction", v: "Retrouver la solution : garder le choix fait (choix[s]) ou remonter la table depuis la dernière case." },
    { r: "Richard Bellman", v: "Invente la programmation dynamique dans les années 1950 (livre de 1957)." },
    { r: "Piège : [[0] * m] * n", v: "Les n lignes sont la même liste. Écrire [[0] * m for _ in range(n)]." }
  ]
});
