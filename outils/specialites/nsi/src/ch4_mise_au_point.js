/* ===================== Chapitre 4 — Modularité et mise au point ===================== */
C("c4-geometrie", String.raw`
"""Module geometrie : quelques calculs sur les figures planes."""
from math import pi

def aire_disque(r):
    """Renvoie l'aire d'un disque de rayon r (r >= 0)."""
    assert r >= 0, "le rayon doit être positif"
    return pi * r ** 2

def perimetre_rectangle(longueur, largeur):
    """Renvoie le périmètre d'un rectangle."""
    return 2 * (longueur + largeur)

if __name__ == "__main__":       # vrai seulement si on EXÉCUTE geometrie.py
    assert perimetre_rectangle(2, 3) == 10
    assert aire_disque(0) == 0
    print("tests du module : ok")`, { fichier: "geometrie.py", cmd: "python3 geometrie.py", out: "tests du module : ok" });

C("c4-main", String.raw`
import geometrie                  # exécute geometrie.py... sans son bloc de tests

print(geometrie.perimetre_rectangle(4, 5))
print(round(geometrie.aire_disque(1), 5))`, { fichier: "main.py", cmd: "python3 main.py", files: { "geometrie.py": "c4-geometrie" }, out: "18\n3.14159" });

C("c4-imports", String.raw`
>>> import math
>>> math.sqrt(16)
4.0
>>> from math import gcd, pi
>>> gcd(84, 36)
12
>>> round(pi, 4)
3.1416
>>> import random as rd
>>> rd.randint(1, 6) in [1, 2, 3, 4, 5, 6]
True`, { console: true });

C("c4-randint", String.raw`
import random

tirages = [random.randint(1, 3) for _ in range(1000)]
print(sorted(set(tirages)))       # randint(1, 3) peut donner 3
print(list(range(1, 3)))          # range(1, 3) s'arrête AVANT 3`, { out: "[1, 2, 3]\n[1, 2]" });

C("c4-doc", String.raw`
>>> def moyenne(notes):
...     """Renvoie la moyenne de la liste notes (non vide)."""
...     return sum(notes) / len(notes)
...
>>> moyenne.__doc__
'Renvoie la moyenne de la liste notes (non vide).'
>>> import math
>>> math.gcd.__doc__.splitlines()[0]
'Greatest Common Divisor.'`, { console: true });

C("c4-pile-module", String.raw`
"""Module pile : une pile, vue uniquement à travers ces fonctions.

    p = creer_pile()      crée une pile vide
    est_vide(p)           True si p est vide
    empiler(p, x)         ajoute x au sommet de p
    depiler(p)            retire et renvoie le sommet de p (p non vide)
"""

def creer_pile():
    return []

def est_vide(p):
    return len(p) == 0

def empiler(p, x):
    p.append(x)

def depiler(p):
    assert not est_vide(p), "dépiler une pile vide"
    return p.pop()`, { fichier: "pile.py", out: "" });

C("c4-pile-usage", String.raw`
from pile import creer_pile, est_vide, empiler, depiler

def inverser(mot):
    p = creer_pile()
    for lettre in mot:
        empiler(p, lettre)
    resultat = ""
    while not est_vide(p):
        resultat = resultat + depiler(p)
    return resultat

print(inverser("module"))`, { fichier: "main.py", cmd: "python3 main.py", files: { "pile.py": "c4-pile-module" }, out: "eludom" });

C("c4-spec", String.raw`
def indice_max(t):
    """Renvoie l'indice de la première occurrence du maximum de t.

    Précondition : t est une liste de nombres non vide.
    Postcondition : le résultat i vérifie 0 <= i < len(t)
                    et t[i] >= t[j] pour tout indice j.

    >>> indice_max([3, 9, 2, 9])
    1
    """
    assert len(t) > 0, "la liste ne doit pas être vide"
    im = 0
    for i in range(1, len(t)):
        if t[i] > t[im]:
            im = i
    return im`, { fichier: "outils.py", out: "" });

C("c4-assert-ko", String.raw`
indice_max([])`, { deps: ["c4-spec"], err: "AssertionError: la liste ne doit pas être vide" });

C("c4-tests", String.raw`
def test_indice_max():
    assert indice_max([5]) == 0              # un seul élément
    assert indice_max([1, 2, 3]) == 2        # maximum à la fin
    assert indice_max([3, 2, 1]) == 0        # maximum au début
    assert indice_max([3, 9, 2, 9]) == 1     # maximum en double : le premier
    assert indice_max([-4, -2, -7]) == 1     # nombres négatifs
    assert indice_max([2.5, 2.25]) == 0      # flottants
    print("test_indice_max : ok")

test_indice_max()`, { deps: ["c4-spec"], out: "test_indice_max : ok" });

C("c4-doctest", String.raw`
import doctest
print(doctest.testmod())     # exécute les exemples >>> des docstrings du fichier`, { deps: ["c4-spec"], out: "TestResults(failed=0, attempted=1)" });

C("c4-exceptions", String.raw`
>>> [4, 8, 15][3]
Traceback (most recent call last):
  ...
IndexError: list index out of range
>>> "Score : " + 15
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
>>> int("douze")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'douze'
>>> {"Ada": 1815}["Alan"]
Traceback (most recent call last):
  ...
KeyError: 'Alan'
>>> 10 / 0
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> moyene([12, 14])
Traceback (most recent call last):
  ...
NameError: name 'moyene' is not defined
>>> None.valeur
Traceback (most recent call last):
  ...
AttributeError: 'NoneType' object has no attribute 'valeur'`, { console: true });

C("c4-trace", String.raw`
def moyenne(notes):
    return sum(notes) / len(notes)

def bilan(eleves):
    for nom in eleves:
        print(nom, moyenne(eleves[nom]))

bilan({"Ada": [15, 17], "Alan": []})`, { fichier: "notes.py", cmd: "python3 notes.py", out: "Ada 16.0", err: "ZeroDivisionError: division by zero",
  trace: String.raw`Traceback (most recent call last):
  File "notes.py", line 8, in <module>
    bilan({"Ada": [15, 17], "Alan": []})
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "notes.py", line 6, in bilan
    print(nom, moyenne(eleves[nom]))
               ~~~~~~~^^^^^^^^^^^^^
  File "notes.py", line 2, in moyenne
    return sum(notes) / len(notes)
           ~~~~~~~~~~~^~~~~~~~~~~~
ZeroDivisionError: division by zero` });

C("c4-raise", String.raw`
def moyenne(notes):
    if len(notes) == 0:
        raise ValueError("moyenne d'une liste vide")
    return sum(notes) / len(notes)

print(moyenne([12, 15]))
moyenne([])`, { out: "13.5", err: "ValueError: moyenne d'une liste vide" });

C("c4-try", String.raw`
def lire_entier(texte):
    """Convertit texte en entier ; renvoie None si c'est impossible."""
    try:
        return int(texte)
    except ValueError:            # on n'attrape QUE l'erreur prévue
        return None

print(lire_entier("42"), lire_entier(" 7 "), lire_entier("quarante-deux"))`, { out: "42 7 None" });

/* causes typiques de bugs */
C("c4-b-typage", String.raw`
reponse = "17"           # input() renvoie TOUJOURS une chaîne
print(int(reponse) + 1)  # conversion explicite : 18
print(reponse + 1)`, { out: "18", err: "TypeError: can only concatenate str (not \"int\") to str" });

C("c4-b-effet", String.raw`
def sans_le_max(t):
    t.remove(max(t))         # modifie la liste reçue... donc celle de l'appelant
    return t

notes = [12, 18, 9]
autres = sans_le_max(notes)
print(autres, notes, autres is notes)`, { out: "[12, 9] [12, 9] True" });

C("c4-b-effet-ok", String.raw`
def sans_le_max(t):
    copie = list(t)          # nouvelle liste : l'appelant n'est pas touché
    copie.remove(max(copie))
    return copie

notes = [12, 18, 9]
print(sans_le_max(notes), notes)`, { out: "[12, 9] [12, 18, 9]" });

C("c4-b-debordement", String.raw`
t = [4, 8, 15]
for i in range(len(t) + 1):     # une case de trop : les indices vont de 0 à 2
    print(t[i])`, { out: "4\n8\n15", err: "IndexError: list index out of range" });

C("c4-b-exhaustif", String.raw`
def signe(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
                    # et si x == 0 ? la fonction renvoie None
print(signe(5), signe(-2), signe(0))`, { out: "1 -1 None" });

C("c4-b-inegalite", String.raw`
def recherche(t, x):
    g, d = 0, len(t) - 1
    while g < d:                 # devrait être g <= d
        m = (g + d) // 2
        if t[m] == x:
            return m
        elif t[m] < x:
            g = m + 1
        else:
            d = m - 1
    return -1

print(recherche([7], 7), recherche([1, 3, 5], 5), recherche([1, 3, 5], 3))`, { out: "-1 -1 1" });

C("c4-b-flottants", String.raw`
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
>>> abs((0.1 + 0.2) - 0.3) < 1e-9
True
>>> import math
>>> math.isclose(0.1 + 0.2, 0.3)
True`, { console: true });

C("c4-b-nommage", String.raw`
max = 20                 # on écrase la fonction max de Python
notes = [12, 18, 9]
print(max(notes))`, { err: "TypeError: 'int' object is not callable" });

/* traces pas à pas (calculées par traces.py) */
C("c4-tr-bug", String.raw`
def recherche(t, x):
    g, d = 0, len(t) - 1
    while g < d:
        m = (g + d) // 2
        if t[m] == x:
            return m
        elif t[m] < x:
            g = m + 1
        else:
            d = m - 1
    return -1

print(recherche([1, 3, 5], 5))`, { fichier: "dicho_boguee.py", titreTrace: "while g < d (bogué)", trace: true, out: "-1" });

C("c4-tr-ok", String.raw`
def recherche(t, x):
    g, d = 0, len(t) - 1
    while g <= d:
        m = (g + d) // 2
        if t[m] == x:
            return m
        elif t[m] < x:
            g = m + 1
        else:
            d = m - 1
    return -1

print(recherche([1, 3, 5], 5))`, { fichier: "dicho_corrigee.py", titreTrace: "while g <= d (corrigé)", trace: true, out: "2" });

C("c4-tr-index", String.raw`
t = [3, 1, 4]
i = 0
while t[i] != 9:
    i = i + 1
print(i)`, { fichier: "debordement.py", titreTrace: "débordement (IndexError)", trace: true, err: "IndexError: list index out of range" });

/* pièges */
C("c4-p-assert", String.raw`
x = -5
assert (x > 0, "x doit être positif")   # un tuple non vide est toujours vrai
print("aucune erreur levée !")`, { out: "aucune erreur levée !", warn: "SyntaxWarning: assertion is always true" });

C("c4-p-except", String.raw`
def lire_note(texte):
    try:
        return float(texte)
    except:                  # attrape TOUT, y compris les vraies erreurs
        return 0

print(lire_note("15,5"))     # la virgule rend la conversion impossible... silencieusement`, { out: "0" });

/* prédis la sortie */
C("c4-x1", String.raw`
def ajoute(x, t=None):
    if t is None:
        t = []
    t.append(x)
    return t

a = [1]
b = ajoute(2, a)
c = ajoute(3)
print(a, b is a, c)`, { out: "[1, 2] True [3]" });

C("c4-x2", String.raw`
def inverse(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return None

print(inverse(4), inverse(0))`, { out: "0.25 None" });

C("c4-x3", String.raw`
total = 0
for _ in range(10):
    total = total + 0.1
print(total == 1, round(total, 2) == 1)`, { out: "False True" });

C("c4-x4", String.raw`
def f(t):
    t = t + [0]
    return t

def g(t):
    t.append(0)
    return t

a = [1]
b = f(a)
c = g(a)
print(a, b, c)`, { out: "[1, 0] [1, 0] [1, 0]" });

C("c4-x5", String.raw`
t = [3, 1, 4]
i = 0
while t[i] != 9:
    i = i + 1
print(i)`, { err: "IndexError: list index out of range" });

/* épreuve pratique 1 */
C("c4-ep1-fourni", String.raw`
def moyenne(notes):
    """Renvoie la moyenne des nombres de la liste notes (non vide)."""
    ...

def mediane(notes):
    """Renvoie la médiane de la liste notes (non vide), sans la modifier."""
    notes.sort()
    n = len(notes)
    if n % 2 == 1:
        return notes[n // 2]
    return (notes[n // 2 - 1] + notes[n // 2]) / 2

releve = [12, 8, 15, 10]
print(mediane(releve))
print(releve)`, { fichier: "stats.py", run: false, trous: [3] });

C("c4-ep1-sortie", String.raw`
def mediane(notes):
    notes.sort()
    n = len(notes)
    if n % 2 == 1:
        return notes[n // 2]
    return (notes[n // 2 - 1] + notes[n // 2]) / 2

releve = [12, 8, 15, 10]
print(mediane(releve))
print(releve)`, { fichier: "stats.py", out: "11.0\n[8, 10, 12, 15]" });

C("c4-ep1-corr", String.raw`
def moyenne(notes):
    """Renvoie la moyenne des nombres de la liste notes (non vide)."""
    assert len(notes) > 0, "liste vide"
    return sum(notes) / len(notes)

def mediane(notes):
    """Renvoie la médiane de la liste notes (non vide), sans la modifier."""
    assert len(notes) > 0, "liste vide"
    t = sorted(notes)                    # copie triée : notes n'est pas modifiée
    n = len(t)
    if n % 2 == 1:
        return t[n // 2]
    return (t[n // 2 - 1] + t[n // 2]) / 2

def test_stats():
    assert moyenne([10]) == 10
    assert moyenne([12, 8, 15, 10]) == 11.25
    assert mediane([7]) == 7                      # un seul élément
    assert mediane([3, 1, 2]) == 2                # taille impaire
    assert mediane([12, 8, 15, 10]) == 11.0       # taille paire
    releve = [12, 8, 15, 10]
    mediane(releve)
    assert releve == [12, 8, 15, 10]              # pas d'effet de bord
    try:
        moyenne([])
        assert False, "moyenne([]) aurait dû lever une erreur"
    except AssertionError as e:
        assert str(e) == "liste vide"

test_stats()
print("tous les tests passent")`, { fichier: "stats.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c4-ep2-fourni", String.raw`
def est_bissextile(annee):
    return annee % 4 == 0

def jours_dans_mois(mois, annee):
    if mois == 2:
        if est_bissextile(annee):
            return 29
        return 28
    elif mois in [4, 6, 9, 11]:
        return 30
    elif mois in [1, 3, 5, 7, 8, 10]:
        return 31

def date_valide(jour, mois, annee):
    """Renvoie True si jour/mois/annee est une date du calendrier grégorien."""
    ...`, { fichier: "dates.py", run: false, trous: [16] });

C("c4-ep2-bug", String.raw`
print(jours_dans_mois(12, 2026))
print(25 <= jours_dans_mois(12, 2026))`, { deps: ["c4-ep2-fourni"], fichier: "essai.py", out: "None", err: "TypeError: '<=' not supported between instances of 'int' and 'NoneType'" });

C("c4-ep2-corr", String.raw`
def est_bissextile(annee):
    """Divisible par 4 mais pas par 100, ou divisible par 400."""
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

def jours_dans_mois(mois, annee):
    assert 1 <= mois <= 12, "mois invalide"
    if mois == 2:
        if est_bissextile(annee):
            return 29
        return 28
    elif mois in [4, 6, 9, 11]:
        return 30
    else:                                  # tous les autres mois : 31 jours
        return 31

def date_valide(jour, mois, annee):
    return 1 <= mois <= 12 and 1 <= jour <= jours_dans_mois(mois, annee)

def test_dates():
    assert est_bissextile(2024) and est_bissextile(2000)
    assert not est_bissextile(2026) and not est_bissextile(1900)
    assert jours_dans_mois(12, 2026) == 31           # le mois oublié
    assert jours_dans_mois(2, 2028) == 29
    assert date_valide(29, 2, 2024)
    assert not date_valide(29, 2, 1900)
    assert not date_valide(31, 4, 2026)
    assert not date_valide(0, 1, 2026)
    assert not date_valide(1, 13, 2026)              # pas d'appel avec mois = 13
    assert date_valide(31, 12, 2026)

test_dates()
print("tous les tests passent")`, { fichier: "dates.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c4-ecrit-code", String.raw`
"""Module stock : un stock est un dictionnaire {nom du produit: quantité}."""

def ajouter(stock, produit, quantite):
    """Ajoute quantite unités de produit au stock."""
    if produit in stock:
        stock[produit] = stock[produit] + quantite
    else:
        stock[produit] = quantite

def retirer(stock, produit, quantite):
    """Retire quantite unités de produit. Renvoie True si c'était possible."""
    if stock[produit] < quantite:
        return False
    stock[produit] = stock[produit] - quantite
    return True

def produits_en_rupture(stock):
    """Renvoie la liste triée des produits dont la quantité est nulle."""
    return sorted([p for p in stock if stock[p] == 0])`, { fichier: "stock.py", out: "" });

C("c4-ecrit-q1", String.raw`
s = {"stylos": 10}
ajouter(s, "cahiers", 5)
r = retirer(s, "stylos", 10)
print(s, r, produits_en_rupture(s))`, { deps: ["c4-ecrit-code"], out: "{'stylos': 0, 'cahiers': 5} True ['stylos']" });

C("c4-ecrit-corr", String.raw`
def ajouter(stock, produit, quantite):
    """Ajoute quantite unités de produit au stock (modifie stock).
    Précondition : quantite est un entier strictement positif."""
    assert isinstance(quantite, int) and quantite > 0, "quantité invalide"
    if produit in stock:
        stock[produit] = stock[produit] + quantite
    else:
        stock[produit] = quantite

def retirer(stock, produit, quantite):
    """Retire quantite unités de produit (modifie stock).
    Préconditions : produit est dans stock, quantite entier > 0.
    Renvoie True si c'était possible, False sinon (stock inchangé)."""
    assert produit in stock, "produit inconnu"
    assert isinstance(quantite, int) and quantite > 0, "quantité invalide"
    if stock[produit] < quantite:
        return False
    stock[produit] = stock[produit] - quantite
    return True

def test_stock():
    s = {"stylos": 10, "gommes": 0}
    assert produits_en_rupture(s) == ["gommes"]
    assert retirer(s, "stylos", 11) is False and s["stylos"] == 10
    assert retirer(s, "stylos", 10) is True and s["stylos"] == 0
    assert produits_en_rupture(s) == ["gommes", "stylos"]     # liste triée
    assert produits_en_rupture({}) == []

test_stock()
print("tous les tests passent")`, { deps: ["c4-ecrit-code"], out: "tous les tests passent" });

C("c4-retenir", String.raw`
def ma_fonction(t):
    """Ce que fait la fonction (une phrase).

    Précondition : ce qui doit être vrai à l'entrée.
    Postcondition : ce qui est garanti à la sortie.
    """
    assert len(t) > 0, "message clair"     # vérifier la précondition
    ...

def test_ma_fonction():                    # cas normaux + cas limites
    assert ma_fonction([1]) == ...

if __name__ == "__main__":
    test_ma_fonction()`, { run: false });

/* Animation : une exception remonte la pile d'appels (notes.py, sans puis avec try … except). */
C("c4-exc-try", String.raw`
def moyenne(notes):
    return sum(notes) / len(notes)

def bilan(eleves):
    for nom in eleves:
        try:
            print(nom, moyenne(eleves[nom]))
        except ZeroDivisionError:
            print(nom, "pas de note")

bilan({"Ada": [15, 17], "Alan": []})
print("fin du programme")`, { fichier: "notes_try.py", out: "Ada 16.0\nAlan pas de note\nfin du programme" });

WIDGETS_EXT["exception"] = function (z, opt, O) {
  var PR = "programme principal", A = '"Ada"', AL = '"Alan"';
  function cadre(f, v, et) { return { f: f, v: v || "", et: et || "" }; }
  function etapes(k) {
    var E = [], t = k === "try";
    var lM = 2, lB = t ? 7 : 6, lP = t ? 11 : 8;
    function snap(l, pile, msg, o) { o = o || {}; E.push({ l: l, pile: pile, msg: msg, exc: o.exc === undefined ? -1 : o.exc, out: o.out || "", tb: o.tb || [], fin: !!o.fin, ok: !!o.ok }); }
    var p0 = cadre(PR, "", "attente");
    snap(lP, [cadre(PR, "", "actif")], "Ligne " + lP + " : le programme principal appelle <b>bilan</b>. Chaque appel empile un <b>cadre</b> (ses variables, la ligne où il en est).");
    snap(5, [p0, cadre("bilan()", "nom = " + A, "actif")], "Dans <b>bilan</b>, la boucle prend <code>nom = " + O.esc(A) + "</code>.");
    snap(lM, [p0, cadre("bilan()", "nom = " + A, "attente"), cadre("moyenne()", "notes = [15, 17]", "actif")], "Ligne " + lB + " : appel de <b>moyenne([15, 17])</b> ; bilan attend sa réponse.");
    snap(lB, [p0, cadre("bilan()", "nom = " + A, "actif")], "moyenne renvoie 32 / 2 = <b>16.0</b> ; son cadre est dépilé et <code>print</code> affiche la ligne d’Ada.", { out: "Ada 16.0" });
    snap(5, [p0, cadre("bilan()", "nom = " + AL, "actif")], "Tour suivant : <code>nom = " + O.esc(AL) + "</code>.", { out: "Ada 16.0" });
    snap(lM, [p0, cadre("bilan()", "nom = " + AL, "attente"), cadre("moyenne()", "notes = []", "actif")], "Appel de <b>moyenne([])</b> : la liste d’Alan est vide.", { out: "Ada 16.0" });
    var tb1 = ['File "' + (t ? "notes_try" : "notes") + '.py", line 2, in moyenne'];
    snap(lM, [p0, cadre("bilan()", "nom = " + AL, "attente"), cadre("moyenne()", "notes = []", "erreur")], "<code>sum([])</code> vaut 0 et <code>len([])</code> vaut 0 : la division est impossible. Python <b>lève</b> une exception <b>ZeroDivisionError</b> : l’exécution normale s’interrompt sur cette ligne.", { exc: 2, out: "Ada 16.0", tb: tb1 });
    var tb2 = ['File "' + (t ? "notes_try" : "notes") + '.py", line ' + lB + ", in bilan"].concat(tb1);
    if (!t) {
      snap(lB, [p0, cadre("bilan()", "nom = " + AL, "erreur")], "moyenne n’a pas de <code>try</code> : son cadre est <b>abandonné</b> (dépilé sans rien renvoyer) et l’exception <b>remonte</b> chez l’appelant, ligne 6 de bilan. Une ligne s’ajoute <b>au-dessus</b> de la trace.", { exc: 1, out: "Ada 16.0", tb: tb2 });
      var tb3 = ['File "notes.py", line 8, in &lt;module&gt;'].concat(tb2);
      snap(lP, [cadre(PR, "", "erreur")], "bilan ne la rattrape pas non plus : son cadre est abandonné, la boucle ne continue pas. L’exception arrive au programme principal, ligne 8.", { exc: 0, out: "Ada 16.0", tb: tb3 });
      snap(0, [], "Personne ne l’a rattrapée : le programme <b>s’arrête</b> et affiche la trace. Elle se lit comme la pile, du plus ancien appel (en haut) au plus récent (en bas), puis le type et le message. Le bug n’est pas dans moyenne : ce sont les données (liste vide).", { out: "Ada 16.0", tb: tb3, fin: true });
    } else {
      snap(lB, [p0, cadre("bilan()", "nom = " + AL, "erreur")], "moyenne n’a pas de <code>try</code> : son cadre est abandonné et l’exception remonte dans bilan, ligne 7. Or cette ligne est <b>dans un bloc try</b> dont le <code>except</code> attend justement <b>ZeroDivisionError</b>.", { exc: 1, out: "Ada 16.0", tb: tb2 });
      snap(9, [p0, cadre("bilan()", "nom = " + AL, "actif")], "L’exception est <b>rattrapée</b> : elle disparaît, et l’exécution reprend dans le bloc <code>except</code> (ligne 9).", { out: "Ada 16.0\nAlan pas de note", ok: true });
      snap(12, [cadre(PR, "", "actif")], "La boucle est finie : bilan se termine normalement et son cadre est dépilé. Le programme <b>continue</b> : rattraper une exception <b>prévue</b>, c’est éviter l’arrêt sans cacher les autres erreurs.", { out: "Ada 16.0\nAlan pas de note\nfin du programme", ok: true });
    }
    return E;
  }
  function id(k) { return k === "try" ? "c4-exc-try" : "c4-trace"; }
  O.lecteur(z, {
    titre: "une exception remonte la pile", sous: "ZeroDivisionError", vitesse: 1700,
    choix: [{ k: "sans", t: "sans try (arrêt)" }, { k: "try", t: "avec try … except" }],
    etapes: etapes,
    prepare: function (sc, k) {
      var c = CODE[id(k)];
      sc.innerHTML = '<div class="trace exc"><div class="code zebre"><div class="tete"><span class="f">' + O.esc(c.fichier) + '</span></div><pre><code>' + O.lignes(O.hlPy(c.src.replace(/^\n+|\s+$/g, ""))) + '</code></pre></div><div class="tr-cote"><div class="titre-pile">pile d’appels (le plus récent en haut)</div><div class="tr-pile"></div><div class="titre-pile">sortie</div><pre class="tr-sortie"></pre></div></div>';
    },
    dessine: function (sc, e, i, E, saut) {
      O.$$(".trace .l", sc).forEach(function (l, n) { l.classList.toggle("vise", n + 1 === e.l); l.classList.toggle("exc-l", n + 1 === e.l && e.exc >= 0); });
      var avant = i > 0 && !saut ? E[i - 1].pile.length : e.pile.length;
      O.$(".tr-pile", sc).innerHTML = e.pile.length ? e.pile.map(function (c, n) {
        var cl = c.et === "actif" ? " actif" : c.et === "erreur" ? " erreur" : "";
        return '<div class="cadre-pile' + cl + (n >= avant ? " neuf" : "") + '"><div class="nm">' + O.esc(c.f) + (n === e.exc ? ' <span class="exc-p' + (saut ? "" : " neuf") + '">ZeroDivisionError</span>' : "") + "</div>" + (c.v ? '<div class="vr">' + O.esc(c.v) + "</div>" : "") + "</div>";
      }).reverse().join("") : '<span class="repere">' + (e.fin ? "pile vide : programme arrêté" : "—") + "</span>";
      var s = O.esc(e.out);
      if (e.tb.length) s += (s ? "\n" : "") + '<span class="err-t">' + (e.fin ? "Traceback (most recent call last):\n" : "trace en construction :\n") + e.tb.map(function (x) { return "  " + x; }).join("\n") + (e.fin ? "\nZeroDivisionError: division by zero" : "") + "</span>";
      O.$(".tr-sortie", sc).innerHTML = s;
    }
  });
};

CH.push({
  id: "ch4", n: 4, court: "mise_au_point", fichier: "ch4_mise_au_point.py",
  titre: "Modularité et mise au point",
  rubrique: "Rubrique « Langages et programmation » : modularité ; mise au point des programmes, gestion des bugs",
  accroche: "Modules, API, documentation, spécification, assertions, tests, exceptions et les bugs typiques que le programme liste.",
  essentiel: [
    "Un <b>module</b> est un fichier Python réutilisable ; on l’importe avec <code>import</code> et on lit sa documentation (docstrings, <code>help()</code>).",
    "Une <b>API</b> décrit ce qu’on peut appeler (noms, paramètres, résultats) sans montrer comment c’est fait.",
    "Une <b>spécification</b> fixe préconditions et postconditions ; les <b>assertions</b> (<code>assert</code>) les vérifient à l’exécution.",
    "Un <b>jeu de tests</b> couvre les cas normaux et les cas limites (vide, un élément, bornes, doublons, négatifs).",
    "Lire une erreur commence par la <b>dernière ligne</b> de la trace : son type (<code>TypeError</code>, <code>IndexError</code>…) indique la cause, les lignes au-dessus disent où."
  ],
  attendus: [
    "Utiliser des API ou des bibliothèques ; exploiter leur documentation.",
    "Créer des modules simples et les documenter.",
    "Répondre aux causes typiques de bugs listées par le programme : typage, effets de bord non désirés, débordements dans les tableaux, instruction conditionnelle non exhaustive, choix des inégalités, comparaisons et calculs entre flottants, mauvais nommage des variables.",
    "Prolonger le travail de Première : spécification, assertions, documentation, construction de jeux de tests ; apprendre à anticiper ses erreurs."
  ],
  intro: `<div class="boite ex"><div class="lab"># pourquoi ce chapitre compte double</div><p>Il est transversal : il sert dans tous les autres chapitres, et c’est le cœur de la <b>partie pratique</b> (1 h sur machine) : écrire une fonction, la tester avec des assertions, trouver et corriger un bug, expliquer son code à l’examinateur.</p></div>`,
  idees: [
    { id: "i1", t: "Pourquoi découper un programme en modules", h: `
<p>Un programme de plusieurs milliers de lignes dans un seul fichier devient illisible. On le découpe en <b>modules</b> : des fichiers <code>.py</code> qui regroupent des fonctions (ou des classes) sur un même thème. Avantages : chaque module se comprend, se teste et se corrige seul ; on le <b>réutilise</b> dans d’autres programmes ; plusieurs personnes travaillent en parallèle.</p>
[[c4-geometrie]]
[[c4-main]]
<p>Le test <code>if __name__ == "__main__":</code> est vrai seulement quand on exécute le fichier lui-même (Python donne alors à <code>__name__</code> la valeur <code>"__main__"</code>) ; quand le fichier est importé, <code>__name__</code> vaut <code>"geometrie"</code>. On y range les tests du module : ils ne s’exécutent pas chez ceux qui l’importent.</p>` },

    { id: "i2", t: "Importer : les trois écritures", h: `
<p>Python est fourni avec une <b>bibliothèque standard</b> de modules (<code>math</code>, <code>random</code>, <code>time</code>, <code>collections</code>…). Il y a trois façons d’importer :</p>
<div class="tab-wrap"><table><tr><th>écriture</th><th>utilisation</th><th>remarque</th></tr>
<tr><td><code>import math</code></td><td><code>math.sqrt(2)</code></td><td>on voit d’où vient chaque nom</td></tr>
<tr><td><code>from math import sqrt, pi</code></td><td><code>sqrt(2)</code></td><td>plus court ; seulement les noms choisis</td></tr>
<tr><td><code>import random as rd</code></td><td><code>rd.randint(1, 6)</code></td><td>un alias plus court</td></tr></table></div>
[[c4-imports]]
<p>À éviter : <code>from module import *</code>, qui importe tous les noms d’un coup et peut écraser silencieusement les tiens (deux fonctions de même nom dans deux modules : la dernière importée gagne).</p>` },

    { id: "i3", t: "API et documentation : lire avant d’appeler", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Une <b>API</b> (<i>Application Programming Interface</i>) est l’ensemble des fonctions, classes et constantes qu’un module (ou un service) met à disposition, avec leur <b>contrat</b> : paramètres attendus, valeur renvoyée, erreurs possibles. On s’en sert sans connaître le code qui est derrière.</p></div>
<p>Lire la documentation évite des erreurs bêtes. Exemple classique : <code>random.randint(a, b)</code> peut renvoyer <code>b</code>, alors que <code>range(a, b)</code> s’arrête avant <code>b</code>.</p>
[[c4-randint]]
<p>La documentation d’une fonction Python est sa <b>docstring</b>, la chaîne placée juste sous le <code>def</code>. <code>help(fonction)</code> l’affiche dans la console ; elle est aussi rangée dans <code>fonction.__doc__</code>.</p>
[[c4-doc]]
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">23/09/1999 <b>·</b></span> La sonde <b>Mars Climate Orbiter</b> est perdue en arrivant sur Mars. Un logiciel au sol fournissait des impulsions en livres-force·seconde ; le logiciel de navigation les attendait en newtons·seconde (facteur d’environ 4,45). Chaque partie marchait ; c’est le <b>contrat</b> entre les deux (les unités) qui n’était pas respecté.</p></div>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Le mot API désigne aussi les services web qu’on interroge par Internet (météo, cartes, horaires de transport) : on envoie une requête documentée, on reçoit des données, souvent au format JSON. Même idée : un contrat, pas de code visible.</p></div>` },

    { id: "i4", t: "Créer et documenter un module", h: `
<p>Un module bien conçu a une <b>interface</b> claire et documentée : la docstring du module dit à quoi il sert et liste ses fonctions ; chaque fonction a sa docstring. C’est exactement la séparation interface / implémentation du chapitre 3.</p>
[[c4-pile-module]]
[[c4-pile-usage]]
<p>Le programme principal n’utilise que les quatre fonctions de l’interface. Si l’on réécrit <code>pile.py</code> avec des maillons, <code>main.py</code> n’a pas à changer.</p>
<div class="boite retenir-b"><div class="lab"># une bonne docstring dit</div><ul><li>ce que fait la fonction (une phrase, au présent) ;</li><li>ce que sont les paramètres (type, contraintes : la <b>précondition</b>) ;</li><li>ce qui est renvoyé ou modifié (la <b>postcondition</b>), en signalant tout effet de bord ;</li><li>éventuellement un exemple d’appel <code>&gt;&gt;&gt;</code>.</li></ul></div>` },

    { id: "i5", t: "Spécification et assertions", h: `
<div class="boite def"><div class="lab">"""définitions"""</div><p>La <b>spécification</b> d’une fonction décrit ce qu’elle doit faire, sans dire comment. La <b>précondition</b> est ce qui doit être vrai quand on l’appelle ; la <b>postcondition</b>, ce qui est garanti quand elle a fini (si la précondition était vraie).</p></div>
[[c4-spec]]
<p>L’instruction <code>assert condition, "message"</code> ne fait rien si la condition est vraie, et arrête le programme avec <code>AssertionError: message</code> sinon. Placée au début d’une fonction, elle vérifie la précondition : une erreur d’appel est détectée tout de suite, avec un message clair, au lieu de produire un résultat faux plus loin.</p>
[[c4-assert-ko]]
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Lancé avec <code>python3 -O</code>, Python ignore les <code>assert</code>. Les assertions servent donc à <b>détecter les erreurs de programmation</b>, pas à contrôler ce que tape un utilisateur : pour cela, on teste avec <code>if</code> ou on lève une exception (idée 7).</p></div>` },

    { id: "i6", t: "Tester : construire un jeu de tests", h: `
<p>Un <b>test</b> appelle une fonction sur une entrée choisie et compare le résultat à celui attendu. On les regroupe dans une fonction <code>test_…()</code> faite d’assertions. Un bon <b>jeu de tests</b> couvre :</p>
<ul><li>des cas <b>normaux</b>, dont tu connais la réponse ;</li><li>les cas <b>limites</b> : structure vide, un seul élément, premier et dernier élément, valeurs égales, nombres négatifs, zéro, flottants ;</li><li>les cas qui ont déjà provoqué un bug (pour qu’il ne revienne pas).</li></ul>
[[c4-tests]]
<p>Les tests montrent la <b>présence</b> de bugs, jamais leur absence : selon une formule célèbre de l’informaticien Edsger Dijkstra, tester peut montrer qu’il y a des erreurs, pas qu’il n’y en a pas. Une fonction qui passe tous tes tests peut encore être fausse sur un cas oublié : c’est pourquoi on choisit les cas limites avec soin.</p>
<div class="boite hp"><div class="lab"># outil pratique : doctest</div><p>Le module <code>doctest</code> exécute les exemples <code>&gt;&gt;&gt;</code> écrits dans les docstrings et vérifie que la sortie est bien celle indiquée. La documentation sert alors aussi de test.</p>[[c4-doctest]]</div>` },

    { id: "i7", t: "Les exceptions : lire une trace, lever, rattraper", h: `
<p>Quand une instruction ne peut pas s’exécuter, Python lève une <b>exception</b> : si personne ne la rattrape, le programme s’arrête et affiche une <b>trace</b> (<i>traceback</i>). Les types à reconnaître :</p>
[[c4-exceptions]]
<div class="tab-wrap"><table><tr><th>exception</th><th>cause habituelle</th></tr>
<tr><td><code>SyntaxError</code>, <code>IndentationError</code></td><td>code mal écrit (deux-points oubliés, indentation incohérente) : rien n’est exécuté</td></tr>
<tr><td><code>NameError</code></td><td>nom inconnu : faute de frappe, variable pas encore définie</td></tr>
<tr><td><code>TypeError</code></td><td>opération impossible sur ce type (<code>"a" + 1</code>, appel avec un mauvais nombre d’arguments)</td></tr>
<tr><td><code>ValueError</code></td><td>bon type mais valeur impossible (<code>int("douze")</code>)</td></tr>
<tr><td><code>IndexError</code></td><td>indice hors du tableau</td></tr>
<tr><td><code>KeyError</code></td><td>clé absente d’un dictionnaire</td></tr>
<tr><td><code>AttributeError</code></td><td>attribut ou méthode inexistant (souvent sur <code>None</code>)</td></tr>
<tr><td><code>ZeroDivisionError</code></td><td>division par zéro</td></tr>
<tr><td><code>RecursionError</code></td><td>trop d’appels récursifs imbriqués</td></tr>
<tr><td><code>AssertionError</code></td><td>une assertion est fausse</td></tr></table></div>
<p><b>Lire une trace</b> : la dernière ligne donne le type et le message ; au-dessus, les appels en cours, du plus ancien au plus récent (c’est la pile d’exécution du chapitre 2). La ligne fautive est la plus basse qui appartient à <b>ton</b> code.</p>
[[c4-trace]]
<p>Ici, le bug n’est pas dans <code>moyenne</code> mais dans les données : la liste d’Alan est vide. Une fonction peut <b>lever</b> elle-même une exception avec <code>raise</code> pour signaler un appel impossible, avec un message utile :</p>
[[c4-raise]]
<p>On peut <b>rattraper</b> une exception prévue avec <code>try … except</code> : le programme continue au lieu de s’arrêter.</p>
[[c4-try]]
<p>Ce qui se passe dans la pile d’appels quand l’exception est levée, sans puis avec <code>try … except</code> :</p>
[[w-exception]]` },

    { id: "i8", t: "Les causes typiques de bugs (liste du programme)", h: `
<p>Le programme cite précisément ces causes. Pour chacune : le symptôme et la correction.</p>
<h3>Problèmes de typage</h3>
[[c4-b-typage]]
<p><code>input()</code> renvoie toujours une chaîne ; <code>"17" + 1</code> est impossible. Convertir avec <code>int()</code> ou <code>float()</code>. Inversement, <code>"17" * 2</code> ne lève pas d’erreur… et donne <code>"1717"</code>.</p>
<h3>Effets de bord non désirés</h3>
[[c4-b-effet]]
<p>Une liste passée en paramètre n’est pas copiée (chapitre 1, alias) : la modifier dans la fonction modifie celle de l’appelant. Si ce n’est pas voulu, travailler sur une copie (<code>list(t)</code>, <code>t[:]</code>) ; si c’est voulu, l’écrire dans la docstring.</p>
[[c4-b-effet-ok]]
<h3>Débordements dans les tableaux</h3>
[[c4-b-debordement]]
<p>Les indices d’un tableau de longueur <i>n</i> vont de 0 à <i>n</i> − 1. Les erreurs « à un près » (<i>off-by-one</i>) sont les plus fréquentes : vérifier la première et la dernière itération.</p>
<h3>Instruction conditionnelle non exhaustive</h3>
[[c4-b-exhaustif]]
<p>Un <code>if … elif …</code> sans <code>else</code> laisse des cas sans réponse : la fonction renvoie <code>None</code>. Vérifier que <b>tous</b> les cas sont couverts (ici, ajouter <code>else: return 0</code>).</p>
<h3>Choix des inégalités</h3>
[[c4-b-inegalite]]
<p><code>&lt;</code> ou <code>&lt;=</code> ? Teste à la main le cas le plus petit (un seul élément) : avec <code>g &lt; d</code>, la boucle ne s’exécute pas du tout quand <code>g == d</code>.</p>
<h3>Comparaisons et calculs entre flottants</h3>
[[c4-b-flottants]]
<p>Les flottants sont stockés en binaire avec une précision limitée : 0,1 n’a pas d’écriture binaire finie. On ne teste jamais l’égalité de deux flottants avec <code>==</code> : on compare leur écart à une petite tolérance.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">04/06/1996 <b>·</b></span> Vol 501 d’<b>Ariane 5</b> : environ 40 secondes après le décollage, la fusée se détruit. Un logiciel repris d’Ariane 4 convertissait un flottant sur 64 bits en entier sur 16 bits ; la valeur, plus grande avec la nouvelle fusée, ne tenait plus dans 16 bits. Débordement non traité : un problème de typage aux conséquences très concrètes.</p></div>
<h3>Mauvais nommage des variables</h3>
[[c4-b-nommage]]
<p>Ne jamais nommer une variable comme une fonction de Python (<code>max</code>, <code>min</code>, <code>sum</code>, <code>list</code>, <code>str</code>, <code>len</code>, <code>input</code>). Éviter aussi <code>l</code>, <code>O</code>, <code>I</code> (confondus avec 1 et 0), et les noms qui mentent (<code>moyenne</code> pour une somme). Un bon nom évite un commentaire.</p>` },

    { id: "i9", t: "Une méthode pour déboguer", h: `
<ol><li><b>Lire</b> le message d’erreur en entier, en commençant par la dernière ligne.</li>
<li><b>Reproduire</b> : trouver l’entrée la plus simple qui provoque le bug, et l’écrire comme un test.</li>
<li><b>Localiser</b> : afficher les valeurs intermédiaires (<code>print</code>), ou exécuter <b>pas à pas</b> avec le débogueur de ton éditeur (Thonny, par exemple, montre la pile et les variables) ou dans <a href="https://pythontutor.com/" target="_blank" rel="noopener">Python Tutor</a>.</li>
<li><b>Comprendre</b> avant de corriger : formuler pourquoi le programme fait ce qu’il fait.</li>
<li><b>Corriger</b>, puis relancer <b>tous</b> les tests (une correction peut en casser une autre).</li></ol>
<p>Exécuter pas à pas, c’est regarder le programme ligne après ligne avec l’état de ses variables. Compare la version boguée et la version corrigée de la recherche dichotomique (idée 8, « choix des inégalités »), puis le débordement de tableau : chaque étape ci-dessous vient de la vraie exécution du code par Python.</p>
[[w-trace|c4-tr-bug,c4-tr-ok,c4-tr-index]]
<p>Expliquer son code ligne par ligne à quelqu’un, ou même à un objet posé sur le bureau, fait souvent apparaître l’erreur : c’est la méthode du « canard en plastique » (<i>rubber duck debugging</i>). C’est aussi exactement ce que demande l’examinateur pendant la partie pratique.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">09/09/1947 <b>·</b></span> Sur le calculateur Harvard Mark II, l’équipe où travaille Grace Hopper trouve un papillon de nuit coincé dans un relais et le colle dans le cahier de bord avec la mention « First actual case of bug being found ». Le mot <i>bug</i> désignait déjà un défaut technique avant cette date, mais l’anecdote l’a rendu célèbre en informatique.</p></div>` }
  ],
  pieges: [
    { t: "Mettre des parenthèses à assert", h: `[[c4-p-assert]]<p><code>assert</code> n’est pas une fonction : avec des parenthèses, on teste un tuple non vide, toujours vrai. Python avertit (<code>SyntaxWarning</code>) mais ne s’arrête pas. Écrire <code>assert x &gt; 0, "x doit être positif"</code>.</p>` },
    { t: "Rattraper toutes les exceptions", h: `[[c4-p-except]]<p>Un <code>except:</code> sans type cache aussi les vraies erreurs (faute de frappe, bug de logique). Toujours préciser le type attendu : <code>except ValueError:</code>.</p>` },
    { t: "Nommer son fichier comme un module de Python", h: `<p>Un fichier <code>random.py</code> ou <code>math.py</code> dans ton dossier est importé <b>à la place</b> du module standard : <code>import random</code> charge ton fichier, et <code>random.randint</code> provoque une <code>AttributeError</code>. Renommer le fichier.</p>` },
    { t: "Écrire un test qui ne teste rien", h: `<p><code>assert indice_max([3, 9])</code> ne compare à rien : il vérifie seulement que le résultat est « vrai » (non nul). Un test compare toujours à une valeur attendue : <code>assert indice_max([3, 9]) == 1</code>.</p>` },
    { t: "Corriger le symptôme au lieu de la cause", h: `<p>Entourer l’appel fautif d’un <code>try</code> pour « faire disparaître » l’erreur, ou ajouter un <code>if</code> pour un cas particulier, sans comprendre pourquoi il se produit, déplace le bug. Remonte la trace jusqu’à la vraie cause (souvent une donnée inattendue, comme une liste vide).</p>` },
    { t: "Comparer des flottants avec ==", h: `<p><code>0.1 + 0.2 == 0.3</code> vaut False. Utiliser <code>abs(a - b) &lt; 1e-9</code> ou <code>math.isclose(a, b)</code>.</p>` }
  ],
  retenir: `
<h2>Squelette d’une fonction propre</h2>
[[c4-retenir]]
<h2>Modules</h2>
<ul><li><code>import m</code> → <code>m.f()</code> · <code>from m import f</code> → <code>f()</code> · <code>import m as x</code> → <code>x.f()</code>. Éviter <code>import *</code>.</li>
<li><code>if __name__ == "__main__":</code> : code exécuté seulement quand on lance le fichier lui-même (tests du module).</li>
<li>API : contrat (noms, paramètres, résultats, erreurs) sans le code. Lire la doc : <code>help(f)</code>, <code>f.__doc__</code>.</li></ul>
<h2>Exceptions à reconnaître</h2>
<div class="tab-wrap"><table><tr><th>exception</th><th>cause</th></tr>
<tr><td>NameError</td><td>nom inconnu</td></tr><tr><td>TypeError</td><td>type incompatible, mauvais nombre d’arguments</td></tr><tr><td>ValueError</td><td>valeur impossible (<code>int("a")</code>)</td></tr><tr><td>IndexError</td><td>indice hors limites</td></tr><tr><td>KeyError</td><td>clé absente</td></tr><tr><td>AttributeError</td><td>attribut absent (souvent sur None)</td></tr><tr><td>ZeroDivisionError</td><td>division par zéro</td></tr><tr><td>RecursionError</td><td>trop d’appels imbriqués</td></tr><tr><td>AssertionError</td><td>assertion fausse</td></tr></table></div>
<h2>Les 7 causes de bugs du programme</h2>
<ol><li>Typage : <code>input()</code> renvoie une chaîne.</li><li>Effet de bord non désiré : une liste en paramètre n’est pas copiée.</li><li>Débordement : indices de 0 à len − 1.</li><li>Conditionnelle non exhaustive : un cas oublié renvoie None.</li><li>Inégalités : tester le plus petit cas (&lt; ou &lt;=).</li><li>Flottants : jamais de == ; une tolérance.</li><li>Nommage : pas de <code>max = …</code>, des noms qui disent la vérité.</li></ol>
<h2>Tester</h2>
<p>Cas normaux + cas limites (vide, 1 élément, bornes, doublons, négatifs, 0) + anciens bugs. Les tests montrent la présence de bugs, pas leur absence.</p>`,
  predis: [
    { code: "c4-x1", niv: "moyen", rep: "<code>ajoute(2, a)</code> modifie la liste <code>a</code> elle-même et la renvoie : <code>b</code> est <code>a</code>. <code>ajoute(3)</code> part d’une liste neuve grâce à <code>None</code> : [3]." },
    { code: "c4-x2", niv: "facile", rep: "1 / 4 = 0.25. Pour 0, la division lève <code>ZeroDivisionError</code>, rattrapée par le <code>except</code> : la fonction renvoie None." },
    { code: "c4-x3", niv: "moyen", rep: "Dix additions de 0.1 donnent 0.9999999999999999 (erreurs d’arrondi binaire) : <code>total == 1</code> est faux. Arrondi à 2 décimales, on retrouve 1.0, égal à 1." },
    { code: "c4-x4", niv: "difficile", rep: "<code>f</code> crée une <b>nouvelle</b> liste (<code>t + [0]</code>) : <code>b</code> vaut [1, 0] et <code>a</code> n’est pas touchée. Puis <code>g</code> modifie <code>a</code> sur place : <code>a</code> devient [1, 0] et <code>c</code> est <code>a</code>. Au moment du print, les trois valent [1, 0] (mais <code>b</code> est un objet différent)." },
    { code: "c4-x5", niv: "facile", rep: "9 n’est pas dans la liste : <code>i</code> atteint 3 et <code>t[3]</code> déborde. Il manquait une condition <code>i &lt; len(t)</code> <b>avant</b> <code>t[i] != 9</code>." }
  ],
  ep: [
    { titre: "Statistiques sur des notes", enonce: `<p>Le module <code>stats.py</code> doit fournir deux fonctions documentées. L’une est à écrire, l’autre ne respecte pas sa documentation.</p>[[c4-ep1-fourni]]`,
      questions: [
        { q: "Compléter <code>moyenne</code> en vérifiant la précondition par une assertion.", c: `<p><code>assert len(notes) &gt; 0, "liste vide"</code> puis <code>return sum(notes) / len(notes)</code>.</p>` },
        { q: "Exécuter le programme fourni. La médiane est-elle juste ? La documentation est-elle respectée ?", c: `[[c4-ep1-sortie]]<p>La médiane (11.0) est juste, mais <code>releve</code> a été trié : <code>notes.sort()</code> trie la liste <b>sur place</b>, donc celle de l’appelant. C’est un effet de bord non désiré, contraire à « sans la modifier ». Correction : <code>t = sorted(notes)</code>, qui renvoie une nouvelle liste triée.</p>` },
        { q: "Écrire <code>test_stats()</code> : cas normaux, tailles paire et impaire, un seul élément, absence d’effet de bord, liste vide.", c: `[[c4-ep1-corr]]` },
        { q: "À l’oral : quelle différence entre <code>sorted(t)</code> et <code>t.sort()</code> ?", c: `<p><code>t.sort()</code> est une méthode qui trie la liste <code>t</code> elle-même et renvoie <code>None</code>. <code>sorted(t)</code> est une fonction qui renvoie une <b>nouvelle</b> liste triée et laisse <code>t</code> intacte.</p>` }
      ] },
    { titre: "Dates valides", enonce: `<p>On veut vérifier qu’une date existe dans le calendrier grégorien. Une année est bissextile si elle est divisible par 4 mais pas par 100, ou si elle est divisible par 400 (2000 l’était, 1900 non).</p>[[c4-ep2-fourni]]`,
      questions: [
        { q: "Exécuter <code>jours_dans_mois(12, 2026)</code> puis <code>25 &lt;= jours_dans_mois(12, 2026)</code>. Expliquer et corriger.", code: "[[c4-ep2-bug]]", c: `<p>Décembre a été oublié : aucune branche ne s’applique, la fonction renvoie <code>None</code> (conditionnelle non exhaustive). Comparer un entier et None lève une <code>TypeError</code>. Correction : un <code>else: return 31</code> final, et une assertion sur le mois.</p>` },
        { q: "Écrire des assertions qui montrent que <code>est_bissextile</code> est fausse, puis la corriger.", c: `<p><code>assert not est_bissextile(1900)</code> échoue. Correction : <code>return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0</code>.</p>` },
        { q: "Écrire <code>date_valide(jour, mois, annee)</code> et un jeu de tests.", c: `<p>Grâce à l’évaluation paresseuse du <code>and</code>, <code>jours_dans_mois</code> n’est jamais appelée avec un mois invalide.</p>[[c4-ep2-corr]]` },
        { q: "À l’oral : comment avez-vous localisé l’erreur de décembre ?", c: `<p>Dernière ligne de la trace : <code>TypeError</code> sur <code>&lt;=</code> entre <code>int</code> et <code>NoneType</code>. Donc <code>jours_dans_mois</code> a renvoyé None ; on regarde quelles valeurs de <code>mois</code> ne passent par aucun <code>return</code>.</p>` }
      ] }
  ],
  ecrit: { titre: "Mise au point d’un module de gestion de stock", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Une boutique gère son stock avec le module suivant.</p>[[c4-ecrit-code]]`,
    questions: [
      { q: "On exécute le code ci-dessous. Qu’affiche-t-il ?", pts: "1 pt", code: "[[c4-ecrit-q1|nosortie]]", c: `<p><code>{'stylos': 0, 'cahiers': 5} True ['stylos']</code>. On ajoute un nouveau produit, on retire tous les stylos (possible : 10 ≥ 10), et les stylos sont alors en rupture.</p>` },
      { q: "Pour chacun des appels suivants (avec <code>s = {\"stylos\": 10}</code>), indiquer si une exception est levée et laquelle : a) <code>retirer(s, \"gommes\", 1)</code> ; b) <code>ajouter(s, \"stylos\", \"3\")</code> ; c) <code>retirer(s, \"stylos\", -2)</code>.", pts: "1,5 pt", c: `<p>a) <code>KeyError: 'gommes'</code> : la clé est absente. b) <code>TypeError</code> : on additionne un entier et une chaîne. c) <b>aucune exception</b>… mais la fonction renvoie True et le stock passe à 12 : une quantité négative <b>ajoute</b> au lieu de retirer. C’est le bug le plus dangereux des trois, car silencieux.</p>` },
      { q: "Écrire les préconditions de <code>ajouter</code> et <code>retirer</code> sous forme d’assertions (quantité entière strictement positive ; produit présent pour <code>retirer</code>).", pts: "1,5 pt", c: `<p><code>assert isinstance(quantite, int) and quantite &gt; 0, "quantité invalide"</code> et, pour <code>retirer</code>, <code>assert produit in stock, "produit inconnu"</code>. Le cas c) est alors arrêté avec un message clair.</p>` },
      { q: "Écrire une fonction de test d’au moins quatre assertions pour <code>retirer</code> et <code>produits_en_rupture</code>.", pts: "1 pt", c: `[[c4-ecrit-corr]]` },
      { q: "Ces fonctions modifient-elles le dictionnaire reçu ? Est-ce souhaitable ici ? Comment le signaler ?", pts: "1 pt", c: `<p>Oui, <code>ajouter</code> et <code>retirer</code> modifient le dictionnaire passé en paramètre (effet de bord) : c’est voulu, puisque leur rôle est de mettre à jour le stock. Il faut l’écrire dans la docstring (« modifie stock ») pour que l’utilisateur du module le sache. <code>produits_en_rupture</code>, elle, ne modifie rien.</p>` }
    ],
    methode: `<p>Dans une question « quelle erreur ? », nomme le <b>type exact</b> de l’exception et explique sa cause en une phrase. Pour une question de tests, varie les cas (normal, limite, erreur) et compare toujours à une valeur attendue.</p>` },
  qcm: [
    { q: "Que fait <code>from math import sqrt</code> ?", c: ["Importe tout le module math", "Rend <code>sqrt</code> utilisable directement, sans préfixe", "Crée un module sqrt", "Renomme math en sqrt"], a: 1, e: "On écrit ensuite <code>sqrt(2)</code>. Avec <code>import math</code>, il faudrait <code>math.sqrt(2)</code>.", ref: "i2" },
    { q: "Quand le bloc <code>if __name__ == \"__main__\":</code> d’un module est-il exécuté ?", c: ["À chaque import du module", "Seulement quand on exécute ce fichier directement", "Jamais", "Seulement en cas d’erreur"], a: 1, e: "Importé, le module a pour <code>__name__</code> son propre nom ; exécuté, <code>\"__main__\"</code>.", ref: "i1" },
    { q: "Qu’est-ce qu’une API ?", c: ["Un langage de programmation", "L’ensemble des fonctions offertes par un module ou un service, avec leur contrat d’utilisation", "Un type d’erreur", "Un éditeur de code"], a: 1, e: "On l’utilise grâce à sa documentation, sans voir le code.", ref: "i3" },
    { q: "<code>random.randint(1, 6)</code> peut renvoyer…", c: ["1 à 5", "1 à 6", "0 à 6", "0 à 5"], a: 1, e: "Les deux bornes sont incluses, contrairement à <code>range(1, 6)</code>.", ref: "i3" },
    { q: "Que se passe-t-il si la condition d’un <code>assert</code> est fausse ?", c: ["Rien", "Python affiche un avertissement et continue", "Le programme s’arrête avec une AssertionError", "La fonction renvoie False"], a: 2, e: "Le message éventuel suit l’erreur : <code>AssertionError: message</code>.", ref: "i5" },
    { q: "Quelle est la précondition naturelle d’une fonction <code>moyenne(t)</code> ?", c: ["t est triée", "t n’est pas vide", "t contient des entiers positifs", "t a une longueur paire"], a: 1, e: "Sinon, on divise par zéro.", ref: "i5" },
    { q: "Quel cas limite est le plus utile pour tester une fonction qui renvoie le maximum d’une liste ?", c: ["Une liste de 1 000 éléments", "Une liste d’un seul élément, ou dont le maximum est en première ou dernière position", "Une liste triée de 10 éléments", "Aucun : un seul test suffit"], a: 1, e: "Les bornes (taille 1, premier, dernier) révèlent les erreurs « à un près ».", ref: "i6" },
    { q: "<code>t = [4, 8, 15]</code> puis <code>t[3]</code> lève…", c: ["KeyError", "ValueError", "IndexError", "TypeError"], a: 2, e: "Les indices valides vont de 0 à 2.", ref: "i7" },
    { q: "<code>int(\"douze\")</code> lève…", c: ["TypeError", "ValueError", "NameError", "SyntaxError"], a: 1, e: "Le type (chaîne) est accepté par <code>int</code>, mais cette valeur-là n’est pas convertible.", ref: "i7" },
    { q: "Dans une trace d’erreur, où lire le type de l’exception ?", c: ["Sur la première ligne", "Sur la dernière ligne", "Dans le nom du fichier", "Nulle part"], a: 1, e: "Les lignes au-dessus donnent la suite des appels, du plus ancien au plus récent.", ref: "i7" },
    { q: "Une fonction modifie la liste reçue en paramètre alors que ce n’était pas prévu. C’est…", c: ["un débordement", "un effet de bord non désiré", "une erreur de typage", "une récursion infinie"], a: 1, e: "La liste n’est pas copiée à l’appel : on la modifie chez l’appelant.", ref: "i8" },
    { q: "Que vaut <code>0.1 + 0.2 == 0.3</code> en Python ?", c: ["True", "False", "Une erreur", "None"], a: 1, e: "0.1 + 0.2 vaut 0.30000000000000004 : on compare des flottants avec une tolérance.", ref: "i8" },
    { q: "La fonction <code>if x &gt; 0: return 1</code> / <code>elif x &lt; 0: return -1</code> renvoie quoi pour x = 0 ?", c: ["0", "None", "1", "Une erreur"], a: 1, e: "Aucun return n’est atteint : conditionnelle non exhaustive.", ref: "i8" },
    { q: "Pourquoi éviter d’écrire <code>max = 20</code> ?", c: ["max est un mot-clé interdit", "On masque la fonction max de Python, qui n’est plus appelable", "Les variables ne peuvent pas contenir 20", "Ce n’est pas un problème"], a: 1, e: "Ensuite <code>max([1, 2])</code> lève <code>TypeError: 'int' object is not callable</code>.", ref: "i8" }
  ],
  cartes: [
    { r: "Module", v: "Fichier .py réutilisable qui regroupe des fonctions ou des classes ; s’importe avec <code>import</code>." },
    { r: "Les 3 façons d’importer", v: "<code>import math</code> → math.sqrt ; <code>from math import sqrt</code> → sqrt ; <code>import random as rd</code> → rd.randint." },
    { r: "if __name__ == \"__main__\":", v: "Bloc exécuté seulement quand on lance le fichier lui-même, pas quand on l’importe (on y met les tests)." },
    { r: "API", v: "Fonctions et classes offertes par un module ou un service, avec leur contrat (paramètres, résultats, erreurs)." },
    { r: "Docstring", v: "Chaîne de documentation sous le <code>def</code> ; lue par <code>help()</code>, rangée dans <code>__doc__</code>." },
    { r: "Précondition / postcondition", v: "Ce qui doit être vrai à l’appel / ce qui est garanti au retour." },
    { r: "assert", v: "<code>assert condition, \"message\"</code> : AssertionError si la condition est fausse. Jamais de parenthèses autour." },
    { r: "Jeu de tests", v: "Cas normaux + cas limites (vide, un élément, bornes, doublons, négatifs) + anciens bugs." },
    { r: "Lire une trace", v: "Dernière ligne : type et message. Au-dessus : les appels, du plus ancien au plus récent." },
    { r: "raise / try-except", v: "<code>raise ValueError(\"…\")</code> signale une erreur ; <code>try: … except ValueError: …</code> la rattrape." },
    { r: "Effet de bord", v: "Modification d’une donnée extérieure à la fonction (liste reçue, variable globale). À éviter s’il n’est pas voulu et documenté." },
    { r: "Flottants", v: "0.1 + 0.2 != 0.3. Comparer avec <code>abs(a - b) &lt; 1e-9</code> ou <code>math.isclose</code>." },
    { r: "IndexError / KeyError", v: "Indice hors du tableau / clé absente du dictionnaire." },
    { r: "TypeError / ValueError", v: "Type incompatible (\"a\" + 1) / valeur impossible pour ce type (int(\"a\"))." },
    { r: "Ariane 5, vol 501 (1996)", v: "Conversion d’un flottant 64 bits en entier 16 bits qui déborde : destruction en vol." }
  ]
});
