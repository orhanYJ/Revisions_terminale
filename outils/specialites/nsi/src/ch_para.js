/* ===================== Paradigmes de programmation ===================== */
C("para-imp", String.raw`
def somme_carres_pairs(t):
    s = 0                            # un ÉTAT, modifié pas à pas
    for x in t:
        if x % 2 == 0:
            s = s + x * x            # affectation : la valeur de s change
    return s

print(somme_carres_pairs([1, 2, 3, 4, 5, 6]))`, { out: "56" });

C("para-fonc", String.raw`
def carre(x):
    return x * x

def est_pair(x):
    return x % 2 == 0

def somme_carres_pairs_f(t):
    return sum(map(carre, filter(est_pair, t)))      # une composition de fonctions

def somme_carres_pairs_rec(t):
    if t == []:
        return 0
    reste = somme_carres_pairs_rec(t[1:])
    return carre(t[0]) + reste if est_pair(t[0]) else reste

print(somme_carres_pairs_f([1, 2, 3, 4, 5, 6]), somme_carres_pairs_rec([1, 2, 3, 4, 5, 6]))
print(sum(x * x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0))`, { out: "56 56\n56" });

C("para-obj", String.raw`
class Serie:
    """Une série de mesures."""
    def __init__(self):
        self.valeurs = []            # l'état est rangé DANS l'objet

    def ajouter(self, x):
        self.valeurs.append(x)

    def somme_carres_pairs(self):
        return sum(x * x for x in self.valeurs if x % 2 == 0)

s = Serie()
for x in [1, 2, 3, 4, 5, 6]:
    s.ajouter(x)
print(s.somme_carres_pairs(), len(s.valeurs))`, { out: "56 6" });

C("para-tri-imp", String.raw`
def tri_selection(t):
    """Trie t SUR PLACE : la liste elle-même est modifiée, rien n'est renvoyé."""
    for i in range(len(t)):
        imin = i
        for j in range(i + 1, len(t)):
            if t[j] < t[imin]:
                imin = j
        t[i], t[imin] = t[imin], t[i]

notes = [14, 9, 17, 11]
tri_selection(notes)
print(notes)`, { out: "[9, 11, 14, 17]" });

C("para-pure", String.raw`
total = 0

def ajoute(x):                       # IMPURE : lit et modifie une variable globale
    global total
    total = total + x
    return total

def somme(a, b):                     # PURE : le résultat ne dépend que des paramètres
    return a + b

print(ajoute(5), ajoute(5), ajoute(5))   # même appel, résultats différents
print(somme(5, 5), somme(5, 5))          # même appel, même résultat`, { out: "5 10 15\n10 10" });

C("para-effet", String.raw`
def ajoute_bonus(notes):             # effet de bord : modifie la liste reçue
    for i in range(len(notes)):
        notes[i] = notes[i] + 1
    return notes

def avec_bonus(notes):               # sans effet de bord : renvoie une nouvelle liste
    return [n + 1 for n in notes]

notes = [12, 15]
nouvelles = avec_bonus(notes)
print(notes, nouvelles)
nouvelles = ajoute_bonus(notes)
print(notes, nouvelles, nouvelles is notes)`, { out: "[12, 15] [13, 16]\n[13, 16] [13, 16] True" });

C("para-ordre-sup", String.raw`
def appliquer_n_fois(f, n, x):
    """f est une FONCTION passée en paramètre."""
    for _ in range(n):
        x = f(x)
    return x

def multiplicateur(k):
    """Renvoie une FONCTION : x -> k * x."""
    def mult(x):
        return k * x
    return mult

triple = multiplicateur(3)
print(triple(14), appliquer_n_fois(triple, 4, 1))
print(list(map(len, ["NSI", "Turing", "Python"])))
print(sorted(["pomme", "kiwi", "banane"], key=len))
print(list(filter(lambda mot: "a" in mot, ["pomme", "kiwi", "banane"])))`, { out: "42 81\n[3, 6, 6]\n['kiwi', 'pomme', 'banane']\n['banane']" });

C("para-reduce", String.raw`
from functools import reduce

print(reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5], 1))      # 1*1*2*3*4*5
print(reduce(lambda acc, mot: acc + len(mot), ["un", "deux", "trois"], 0))`, { out: "120\n11" });

C("para-immuable", String.raw`
point = (3, 4)                       # un tuple : on ne peut pas le modifier
deplace = (point[0] + 1, point[1])   # on en fabrique un nouveau
print(point, deplace)
point[0] = 10`, { out: "(3, 4) (4, 4)", err: "TypeError: 'tuple' object does not support item assignment" });

C("para-compte-imp", String.raw`
solde = 100                          # état global

def deposer(montant):
    global solde
    solde = solde + montant

def retirer(montant):
    global solde
    if montant <= solde:
        solde = solde - montant

deposer(50)
retirer(30)
retirer(500)                         # refusé
print(solde)`, { out: "120" });

C("para-compte-fonc", String.raw`
from functools import reduce

def appliquer(solde, operation):
    """Renvoie le NOUVEAU solde ; ne modifie rien."""
    nature, montant = operation
    if nature == "depot":
        return solde + montant
    if nature == "retrait" and montant <= solde:
        return solde - montant
    return solde

operations = (("depot", 50), ("retrait", 30), ("retrait", 500))
print(reduce(appliquer, operations, 100))
print(reduce(appliquer, operations[:1], 100))     # rejouer l'historique jusqu'à un moment donné`, { out: "120\n150" });

C("para-compte-obj", String.raw`
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde = self.solde - montant
            return True
        return False

a = Compte("Ada", 100)
b = Compte("Alan")
a.deposer(50)
print(a.retirer(30), a.retirer(500), b.retirer(1))
print(a.titulaire, a.solde, "|", b.titulaire, b.solde)`, { out: "True False False\nAda 120 | Alan 0" });

/* pièges */
C("para-p-defaut", String.raw`
def ajouter(element, liste=[]):      # la liste par défaut est créée une seule fois
    liste.append(element)
    return liste

print(ajouter("a"))
print(ajouter("b"))                  # surprise : la liste se souvient de "a"`, { out: "['a']\n['a', 'b']" });

C("para-p-map", String.raw`
r = map(lambda x: x * 10, [1, 2, 3])
print(r)
print(list(r))
print(list(r))                       # un map ne se parcourt qu'une fois`, { out: "<map object at 0x...>\n[10, 20, 30]\n[]", run: false });

C("para-p-sort", String.raw`
t = [3, 1, 2]
u = t.sort()                         # méthode impérative : trie t, renvoie None
print(t, u)
v = sorted([3, 1, 2])                # fonction : renvoie une nouvelle liste
print(v)`, { out: "[1, 2, 3] None\n[1, 2, 3]" });

/* prédis la sortie */
C("para-x1", String.raw`
print(list(map(lambda x: x + 1, filter(lambda x: x > 2, [1, 5, 2, 8]))))`, { out: "[6, 9]" });

C("para-x2", String.raw`
def f(t):
    t.append(0)
    return len(t)

a = [1, 2]
b = a
print(f(b), a, f(a[:]), a)`, { out: "3 [1, 2, 0] 4 [1, 2, 0]" });

C("para-x3", String.raw`
def puissance(n):
    return lambda x: x ** n

carre, cube = puissance(2), puissance(3)
print(carre(5), cube(2), puissance(0)(99))`, { out: "25 8 1" });

C("para-x4", String.raw`
fonctions = [lambda x: x + i for i in range(3)]
print([f(10) for f in fonctions])`, { out: "[12, 12, 12]" });

/* épreuve pratique 1 */
C("para-ep1-fourni", String.raw`
def moyennes_admis(eleves):
    """eleves : liste de couples (nom, liste de notes).
    Renvoie la liste des couples (nom, moyenne) des élèves dont la moyenne
    est au moins 10, dans l'ordre de départ. Moyenne arrondie à 2 décimales."""
    res = []
    for i in range(len(eleves)):
        nom = eleves[i][0]
        notes = eleves[i][1]
        s = 0
        for n in notes:
            s = s + n
        m = round(s / len(notes), 2)
        if m >= 10:
            res.append((nom, m))
    return res

classe = [("Ada", [12, 15, 9]), ("Alan", [8, 9, 11]), ("Grace", [16, 14])]
print(moyennes_admis(classe))`, { fichier: "paradigmes.py", out: "[('Ada', 12.0), ('Grace', 15.0)]" });

C("para-ep1-corr", String.raw`
def moyenne(notes):
    return round(sum(notes) / len(notes), 2)

def moyennes_admis_f(eleves):
    """Style fonctionnel : aucune variable modifiée, aucune boucle explicite."""
    avec_moy = map(lambda e: (e[0], moyenne(e[1])), eleves)
    return list(filter(lambda c: c[1] >= 10, avec_moy))

def moyennes_admis_c(eleves):
    return [(nom, moyenne(notes)) for nom, notes in eleves if moyenne(notes) >= 10]

def moyennes_admis_rec(eleves):
    if eleves == []:
        return []
    nom, notes = eleves[0]
    suite = moyennes_admis_rec(eleves[1:])
    return [(nom, moyenne(notes))] + suite if moyenne(notes) >= 10 else suite

def test():
    classe = [("Ada", [12, 15, 9]), ("Alan", [8, 9, 11]), ("Grace", [16, 14])]
    copie = [(n, list(t)) for n, t in classe]
    attendu = [("Ada", 12.0), ("Grace", 15.0)]
    for f in [moyennes_admis_f, moyennes_admis_c, moyennes_admis_rec]:
        assert f(classe) == attendu
        assert f([]) == []
        assert f([("Linus", [10])]) == [("Linus", 10.0)]       # 10 compte
    assert classe == copie                                     # aucune donnée modifiée

test()
print("tous les tests passent")`, { fichier: "paradigmes.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("para-ep2-fourni", String.raw`
class Pile:
    def __init__(self):
        self.contenu = []
    def empiler(self, x):
        self.contenu.append(x)
    def depiler(self):
        return self.contenu.pop()
    def est_vide(self):
        return self.contenu == []

# Version fonctionnelle : une pile est un tuple, () est la pile vide,
# (sommet, reste) une pile non vide. Rien n'est jamais modifié.
def empiler_f(p, x):
    ...
def sommet_f(p):
    ...
def depiler_f(p):
    """Renvoie la pile sans son sommet."""
    ...`, { fichier: "piles.py", run: false, trous: [14, 16, 19] });

C("para-ep2-corr", String.raw`
class Pile:
    def __init__(self):
        self.contenu = []
    def empiler(self, x):
        self.contenu.append(x)
    def depiler(self):
        return self.contenu.pop()
    def est_vide(self):
        return self.contenu == []

def empiler_f(p, x):
    return (x, p)

def sommet_f(p):
    return p[0]

def depiler_f(p):
    return p[1]

def parentheses_ok_objet(texte):
    p = Pile()
    for c in texte:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            p.depiler()
    return p.est_vide()

def parentheses_ok_fonc(texte, p=()):
    if texte == "":
        return p == ()
    if texte[0] == "(":
        return parentheses_ok_fonc(texte[1:], empiler_f(p, "("))
    if texte[0] == ")":
        return p != () and parentheses_ok_fonc(texte[1:], depiler_f(p))
    return parentheses_ok_fonc(texte[1:], p)

def test():
    p0 = ()
    p1 = empiler_f(p0, 1)
    p2 = empiler_f(p1, 2)
    assert sommet_f(p2) == 2 and depiler_f(p2) == p1
    assert p1 == (1, ())                       # p1 n'a pas été modifiée par l'ajout de 2
    for t, ok in [("(a(b)c)", True), ("(()", False), (")(", False), ("", True), ("f(x) * (y + 1)", True)]:
        assert parentheses_ok_objet(t) == ok == parentheses_ok_fonc(t)

test()
print("tous les tests passent")`, { fichier: "piles.py", out: "tous les tests passent" });

/* épreuve écrite */
C("para-ecrit-corr", String.raw`
def compte_occurrences_imp(t, v):
    n = 0
    for x in t:
        if x == v:
            n = n + 1
    return n

def compte_occurrences_rec(t, v):
    if t == []:
        return 0
    return (1 if t[0] == v else 0) + compte_occurrences_rec(t[1:], v)

def compte_occurrences_f(t, v):
    return len(list(filter(lambda x: x == v, t)))

t = [3, 1, 3, 2, 3]
print(compte_occurrences_imp(t, 3), compte_occurrences_rec(t, 3), compte_occurrences_f(t, 3))`, { out: "3 3 3" });

C("para-retenir", String.raw`
# impératif : un état modifié par des instructions
s = 0
for x in t:
    s = s + x
# fonctionnel : des fonctions pures, composées, sans modification
s = reduce(lambda acc, x: acc + x, t, 0)        # ou sum(t), ou une fonction récursive
# objet : l'état et les traitements regroupés dans des objets
compteur = Compteur()
for x in t:
    compteur.ajouter(x)`, { run: false });

CH.push({
  id: "para", n: 17, court: "paradigmes", fichier: "paradigmes.py",
  titre: "Paradigmes de programmation",
  rubrique: "Rubrique « Langages et programmation » : paradigmes impératif, fonctionnel et objet",
  accroche: "Impératif, fonctionnel, objet : trois façons de penser un programme, souvent mélangées en Python. Effets de bord, fonctions pures, fonctions d’ordre supérieur, et comment choisir.",
  essentiel: [
    "Un <b>paradigme</b> est une façon de structurer un programme et de penser le calcul. Un même problème s’écrit dans plusieurs paradigmes ; Python les permet tous les trois.",
    "<b>Impératif</b> : une suite d’instructions qui <b>modifient un état</b> (affectations, boucles). C’est le plus proche du fonctionnement de la machine.",
    "<b>Fonctionnel</b> : le programme est une composition de <b>fonctions pures</b> (même entrée → même sortie, aucun <b>effet de bord</b>), sans modifier de variables ; les fonctions sont des valeurs (map, filter, lambda).",
    "<b>Objet</b> : les données et les traitements sont regroupés dans des <b>objets</b> (attributs + méthodes), instances de classes, qui communiquent par appels de méthodes.",
    "On <b>choisit</b> le paradigme selon le champ d’application, et on les <b>mélange</b> souvent dans un même programme."
  ],
  attendus: [
    "Distinguer sur des exemples les paradigmes impératif, fonctionnel et objet (BO).",
    "Choisir le paradigme de programmation selon le champ d’application d’un programme (BO).",
    "Savoir qu’avec un même langage on peut utiliser des paradigmes différents, et que dans un même programme on peut en mêler plusieurs (commentaire du BO).",
    "Repérer un effet de bord, écrire une fonction pure, utiliser une fonction comme paramètre ou comme résultat."
  ],
  idees: [
    { id: "i1", t: "Un même problème, trois façons de l’écrire", h: `
<p>Calculons la somme des carrés des nombres pairs d’une liste. En <b>impératif</b>, on décrit <b>comment</b> faire, pas à pas, avec une variable qui change :</p>
[[para-imp]]
<p>En <b>fonctionnel</b>, on décrit <b>ce qu’on calcule</b> comme une composition de fonctions : garder les pairs, élever au carré, additionner. Aucune variable n’est modifiée.</p>
[[para-fonc]]
<p>En <b>objet</b>, on modélise une entité (ici une série de mesures) qui <b>contient</b> ses données et <b>sait</b> faire les calculs qui la concernent :</p>
[[para-obj]]
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>paradigme de programmation</b> est un style, une manière de concevoir et d’organiser un programme, avec ses concepts propres : instructions et état (impératif), fonctions et valeurs (fonctionnel), objets et messages (objet).</p></div>
[[w-algo-paradigmes]]` },

    { id: "i2", t: "Le paradigme impératif : un état qui change", h: `
<p>Un programme impératif est une <b>séquence d’instructions</b> exécutées dans l’ordre, qui modifient l’<b>état</b> du programme (la valeur des variables, le contenu de la mémoire). Ses outils : l’<b>affectation</b>, la séquence, les tests, les <b>boucles</b>.</p>
[[para-tri-imp]]
<p>Le tri par sélection est typiquement impératif : il échange des cases de la liste <b>sur place</b>. C’est économe en mémoire et proche du processeur, qui exécute lui-même des instructions modifiant des registres et des cases mémoire (modèle de von Neumann). Fortran (1957) et C (1972) sont des langages d’abord impératifs.</p>
<p>La difficulté : pour comprendre ce que fait une ligne, il faut savoir <b>l’état</b> à ce moment-là, donc tout ce qui s’est passé avant. Plus l’état est partagé (variables globales), plus les bugs sont difficiles à trouver.</p>` },

    { id: "i3", t: "Fonctions pures et effets de bord", h: `
<div class="boite def"><div class="lab">"""définitions"""</div><ul><li>Une fonction a un <b>effet de bord</b> si elle modifie quelque chose en dehors de ses variables locales : une variable globale, une liste reçue en paramètre, un fichier, l’écran.</li><li>Une fonction est <b>pure</b> si son résultat ne dépend <b>que de ses paramètres</b> et si elle n’a <b>aucun effet de bord</b>. Appelée deux fois avec les mêmes arguments, elle donne deux fois le même résultat.</li></ul></div>
[[para-pure]]
<p>L’effet de bord le plus piégeux en Python : modifier une liste reçue en paramètre. L’appelant voit sa liste changer, souvent sans s’y attendre.</p>
[[para-effet]]
<p>Une fonction pure se teste facilement (aucun contexte à préparer), se comprend seule, et peut être exécutée en parallèle sans risque. Le chapitre Mise au point classe les « effets de bord non désirés » parmi les causes typiques de bugs.</p>` },

    { id: "i4", t: "Le paradigme fonctionnel", h: `
<p>En programmation fonctionnelle, un programme est une <b>expression</b> à évaluer, construite à partir de <b>fonctions pures</b>. Ses principes :</p>
<ul><li><b>pas de modification</b> : on ne change pas une valeur, on en fabrique une nouvelle (données <b>immuables</b>) ;</li>
<li><b>récursivité</b> plutôt que boucles (une boucle a besoin d’un compteur qui change) ;</li>
<li>les fonctions sont des <b>valeurs comme les autres</b> : on peut les passer en paramètre, les renvoyer, les ranger dans une liste. Une fonction qui prend ou renvoie une fonction est dite <b>d’ordre supérieur</b>.</li></ul>
[[para-ordre-sup]]
<p><code>map(f, t)</code> applique <code>f</code> à chaque élément, <code>filter(p, t)</code> garde ceux qui vérifient <code>p</code>, <code>lambda x: …</code> écrit une petite fonction sans nom. <code>reduce</code> (module <code>functools</code>) combine les éléments un à un dans un accumulateur :</p>
[[para-reduce]]
<p>En Python, les tuples et les chaînes sont immuables ; les listes ne le sont pas.</p>
[[para-immuable]]
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1936 <b>·</b></span> Le lambda-calcul d’Alonzo Church, un modèle de calcul fait uniquement de fonctions, est l’ancêtre de la programmation fonctionnelle (le mot-clé <code>lambda</code> de Python en vient).<br><span class="commit">1958 <b>·</b></span> LISP (John McCarthy). <span class="commit">1990 <b>·</b></span> Haskell, langage fonctionnel pur. <span class="commit">1996 <b>·</b></span> OCaml, développé en France à l’Inria.</p></div>` },

    { id: "i5", t: "Le paradigme objet", h: `
<p>Le paradigme objet (chapitre Programmation objet) organise le programme autour d’<b>objets</b> qui regroupent un <b>état</b> (les attributs) et des <b>comportements</b> (les méthodes). Chaque objet est une <b>instance</b> d’une <b>classe</b>. L’état n’est plus global : chaque objet garde le sien, et on y accède par ses méthodes (<b>encapsulation</b>).</p>
[[para-compte-obj]]
<p>Les deux comptes sont indépendants : impossible de les confondre, ce qui serait facile avec des variables globales. C’est pour cela que l’objet domine dans les grands logiciels, les interfaces graphiques (chaque bouton, chaque fenêtre est un objet) et les jeux (chaque personnage).</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1967 <b>·</b></span> Simula 67 (Ole-Johan Dahl et Kristen Nygaard, Norvège) introduit classes et objets.<br><span class="commit">1972 <b>·</b></span> Smalltalk (Alan Kay et son équipe, Xerox PARC) popularise le terme « programmation orientée objet ».<br><span class="commit">1995 <b>·</b></span> Java, langage objet devenu l’un des plus utilisés au monde.</p></div>` },

    { id: "i6", t: "Comparer : le même compte bancaire dans les trois paradigmes", h: `
<p>Version impérative : un état global modifié par des procédures.</p>
[[para-compte-imp]]
<p>Version fonctionnelle : une fonction pure calcule le nouveau solde à partir de l’ancien et d’une opération ; l’historique est un tuple qu’on ne modifie jamais. Bonus : on peut <b>rejouer</b> l’historique jusqu’à n’importe quel moment.</p>
[[para-compte-fonc]]
<p>Version objet : voir l’idée précédente.</p>
<div class="tab-wrap"><table><tr><th></th><th>impératif</th><th>fonctionnel</th><th>objet</th></tr>
<tr><td>unité de base</td><td>instruction</td><td>fonction (pure)</td><td>objet (classe)</td></tr>
<tr><td>état</td><td>variables modifiées</td><td>pas de modification : nouvelles valeurs</td><td>attributs, propres à chaque objet</td></tr>
<tr><td>répétition</td><td>boucles</td><td>récursivité, map, filter, reduce</td><td>boucles ou récursion dans les méthodes</td></tr>
<tr><td>point fort</td><td>proche de la machine, efficace</td><td>fiable, testable, parallélisable</td><td>modélise des entités, organise les grands programmes</td></tr>
<tr><td>risque</td><td>effets de bord, état difficile à suivre</td><td>copies, récursion profonde (en Python)</td><td>surconception, état caché dans les objets</td></tr>
<tr><td>langages typiques</td><td>C, Fortran</td><td>Haskell, OCaml, LISP</td><td>Java, Smalltalk, C++</td></tr></table></div>` },

    { id: "i7", t: "Mélanger et choisir les paradigmes", h: `
<p>Python, JavaScript, OCaml, Scala sont <b>multi-paradigmes</b> : on choisit le style à chaque endroit du programme. Une classe (objet) peut avoir des méthodes écrites avec des boucles (impératif) et utiliser <code>sorted(…, key=lambda …)</code> (fonctionnel). Le programme de NSI le dit : avec un même langage, et dans un même programme, on mêle les paradigmes.</p>
<p>On choisit selon le <b>champ d’application</b> :</p>
<ul><li><b>impératif</b> : programmes proches du matériel (systèmes d’exploitation, pilotes, objets embarqués), calcul intensif où l’on veut maîtriser la mémoire (Linux est écrit en C) ;</li>
<li><b>objet</b> : logiciels de grande taille, interfaces graphiques, jeux vidéo, simulations, où l’on modélise beaucoup d’entités qui ont un état ;</li>
<li><b>fonctionnel</b> : traitement de données (transformer, filtrer, agréger), calcul parallèle et distribué (le modèle MapReduce de Google, 2004, doit son nom à <code>map</code> et <code>reduce</code>), compilateurs, finance, et partout où la fiabilité prime.</li></ul>
<div class="boite hp"><div class="lab"># pour aller plus loin : le paradigme déclaratif</div><p>On décrit le <b>résultat voulu</b>, pas la manière de l’obtenir. SQL en est l’exemple au programme : <code>SELECT nom FROM eleve WHERE note &gt;= 10</code> ne dit rien de l’algorithme ; le SGBD choisit. Prolog (1972, Alain Colmerauer et Philippe Roussel, Marseille) est un langage de programmation <b>logique</b>, une autre forme de déclaratif. Les compréhensions de liste de Python ont un air déclaratif.</p></div>` }
  ],
  pieges: [
    { t: "Une liste comme valeur par défaut", h: `[[para-p-defaut]]<p>La valeur par défaut est évaluée <b>une fois</b>, à la définition de la fonction : la même liste est réutilisée et modifiée à chaque appel. C’est un effet de bord caché. Écrire <code>liste=None</code> puis <code>if liste is None: liste = []</code>.</p>` },
    { t: "Confondre t.sort() et sorted(t)", h: `[[para-p-sort]]<p><code>t.sort()</code> est impératif : il modifie <code>t</code> et renvoie <code>None</code>. <code>sorted(t)</code> est fonctionnel : il renvoie une nouvelle liste et ne touche pas à <code>t</code>. Même distinction pour <code>t.reverse()</code> et <code>reversed(t)</code>.</p>` },
    { t: "Oublier que map et filter sont paresseux", h: `[[para-p-map]]<p><code>map(…)</code> et <code>filter(…)</code> renvoient un objet qui calcule les valeurs <b>à la demande</b>, pas une liste : <code>print(map(f, t))</code> affiche <code>&lt;map object at 0x…&gt;</code>. On écrit <code>list(map(f, t))</code>. Et cet objet ne se parcourt qu’<b>une seule fois</b> : un second <code>list(r)</code> donne <code>[]</code>.</p>` },
    { t: "Croire qu’une fonction qui renvoie une liste n’a pas d’effet de bord", h: `<p>Dans l’idée 3, <code>ajoute_bonus</code> renvoie bien une liste… mais c’est la liste reçue, modifiée. Pour savoir si une fonction est pure, regarde si elle <b>modifie</b> quelque chose, pas ce qu’elle renvoie.</p>` },
    { t: "Penser qu’un paradigme est « meilleur » dans l’absolu", h: `<p>À l’écrit, la question « quel paradigme choisir ? » attend une <b>justification liée à l’application</b> (entités avec un état → objet ; transformation de données sans effet de bord, parallélisme → fonctionnel ; contrôle fin de la machine → impératif), pas une préférence.</p>` }
  ],
  retenir: `
<h2>Les trois paradigmes au programme</h2>
<div class="tab-wrap"><table><tr><th>paradigme</th><th>idée</th><th>outils</th><th>applications typiques</th></tr>
<tr><td>impératif</td><td>instructions qui modifient un état</td><td>affectation, boucles, tests</td><td>systèmes, embarqué, calcul intensif</td></tr>
<tr><td>fonctionnel</td><td>composition de fonctions pures, pas de modification</td><td>récursivité, map, filter, reduce, lambda, données immuables</td><td>traitement de données, parallélisme, fiabilité</td></tr>
<tr><td>objet</td><td>objets = attributs + méthodes, instances de classes</td><td>classes, encapsulation</td><td>grands logiciels, interfaces, jeux, simulations</td></tr></table></div>
[[para-retenir]]
<h2>Vocabulaire</h2>
<ul><li><b>Effet de bord</b> : modification de quelque chose hors des variables locales (global, liste reçue, fichier, affichage).</li><li><b>Fonction pure</b> : résultat dépendant seulement des paramètres, sans effet de bord.</li><li><b>Fonction d’ordre supérieur</b> : prend ou renvoie une fonction (map, filter, sorted avec key).</li><li><b>Immuable</b> : non modifiable (tuple, chaîne).</li><li><b>Multi-paradigme</b> : langage qui permet plusieurs paradigmes (Python).</li></ul>
<h2>Repères</h2><ul><li>1957 Fortran, 1972 C (impératif) ; 1958 LISP, 1990 Haskell, 1996 OCaml (fonctionnel) ; 1967 Simula, 1972 Smalltalk, 1995 Java (objet) ; 1972 Prolog (logique).</li></ul>`,
  predis: [
    { code: "para-x1", niv: "facile", rep: "<code>filter</code> garde 5 et 8 (strictement plus grands que 2), puis <code>map</code> ajoute 1 : [6, 9]." },
    { code: "para-x2", niv: "moyen", rep: "<code>b</code> et <code>a</code> désignent la même liste : <code>f(b)</code> lui ajoute 0 (effet de bord) et renvoie 3. <code>a[:]</code> est une <b>copie</b> : <code>f</code> la modifie (longueur 4) mais <code>a</code> ne change plus. Les arguments sont évalués de gauche à droite ; quand on affiche <code>a</code>, il vaut [1, 2, 0] les deux fois." },
    { code: "para-x3", niv: "moyen", rep: "<code>puissance(n)</code> renvoie une fonction qui élève à la puissance <i>n</i> : 5² = 25, 2³ = 8, 99⁰ = 1." },
    { code: "para-x4", niv: "difficile", rep: "Piège classique : chaque <code>lambda</code> utilise la variable <code>i</code> <b>au moment de l’appel</b>, pas sa valeur au moment de la création. Quand on appelle les fonctions, la boucle est finie et <code>i</code> vaut 2 : 10 + 2 = 12 trois fois. (Pour figer la valeur : <code>lambda x, i=i: x + i</code>.)" }
  ],
  ep: [
    { titre: "Réécrire en style fonctionnel", enonce: `<p>La fonction ci-dessous est écrite en style impératif.</p>[[para-ep1-fourni]]`,
      questions: [
        { q: "Repérer dans <code>moyennes_admis</code> toutes les variables dont la valeur change. Cette fonction a-t-elle un effet de bord sur <code>eleves</code> ?", c: `<p><code>res</code> (liste modifiée par <code>append</code>), <code>i</code>, <code>nom</code>, <code>notes</code>, <code>s</code>, <code>n</code>, <code>m</code>. Aucun effet de bord sur <code>eleves</code> : elle le lit sans le modifier. Les modifications sont locales : la fonction est pure vue de l’extérieur, mais écrite de façon impérative.</p>` },
        { q: "Écrire une fonction <code>moyenne(notes)</code> sans boucle, puis <code>moyennes_admis_f</code> avec <code>map</code> et <code>filter</code>, sans aucune affectation de variable modifiée.", c: `<p><code>sum(notes) / len(notes)</code> arrondi ; puis <code>map</code> pour fabriquer les couples (nom, moyenne) et <code>filter</code> pour garder ceux dont la moyenne est au moins 10.</p>` },
        { q: "Écrire deux autres versions : par compréhension de liste et récursive. Écrire des tests qui vérifient que les trois versions donnent le même résultat et que la liste de départ n’est pas modifiée.", c: `[[para-ep1-corr]]` },
        { q: "À l’oral : quelle version préférez-vous, et pourquoi ?", c: `<p>Toute réponse argumentée convient. Par exemple : la compréhension est la plus lisible en Python ; la version <code>map/filter</code> montre la composition ; la version récursive est la plus « fonctionnelle » mais risque la <code>RecursionError</code> au-delà d’environ 1 000 élèves et copie la liste à chaque appel.</p>` }
      ] },
    { titre: "Une pile en objet et en fonctionnel", enonce: `<p>On compare deux façons de réaliser une pile : une classe dont l’état change, et des tuples imbriqués qu’on ne modifie jamais.</p>[[para-ep2-fourni]]`,
      questions: [
        { q: "Compléter <code>empiler_f</code>, <code>sommet_f</code> et <code>depiler_f</code> (lignes 14, 16 et 19). Que vaut la pile obtenue en empilant 1 puis 2 sur la pile vide ?", c: `<p><code>return (x, p)</code>, <code>return p[0]</code>, <code>return p[1]</code>. On obtient <code>(2, (1, ()))</code>. La pile <code>(1, ())</code> existe toujours, inchangée : empiler fabrique une nouvelle pile qui <b>partage</b> l’ancienne.</p>` },
        { q: "Écrire <code>parentheses_ok_objet(texte)</code> avec la classe, puis <code>parentheses_ok_fonc(texte)</code>, récursive, avec les fonctions sur les tuples. Tester les deux.", c: `[[para-ep2-corr]]` },
        { q: "À l’oral : laquelle de ces deux piles peut-on partager sans risque entre deux parties d’un programme ?", c: `<p>La pile fonctionnelle : personne ne peut la modifier, chacun fabrique ses propres versions. Avec la classe, si deux parties du programme ont une référence vers le même objet, un <code>depiler</code> de l’une change ce que voit l’autre.</p>` }
      ] }
  ],
  ecrit: { titre: "Reconnaître et choisir un paradigme", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>On veut compter le nombre d’occurrences d’une valeur <code>v</code> dans une liste <code>t</code>.</p>`,
    questions: [
      { q: "Écrire une fonction impérative <code>compte_occurrences_imp(t, v)</code>.", pts: "1 pt", c: `<p>Un compteur initialisé à 0 et une boucle <code>for</code> qui l’incrémente quand l’élément vaut <code>v</code>.</p>` },
      { q: "Écrire une version récursive, puis une version utilisant <code>filter</code>. À quel paradigme se rattachent-elles ? Justifier.", pts: "1,5 pt", c: `<p>Au paradigme fonctionnel : aucune variable n’est modifiée, le résultat est une expression composée de fonctions ; la répétition vient de la récursivité ou de <code>filter</code>.</p>[[para-ecrit-corr]]` },
      { q: "Voici une fonction : <code>def ajoute(t, x): t.append(x); return len(t)</code>. Est-elle pure ? Justifier, puis écrire une version pure.", pts: "1 pt", c: `<p>Non : elle modifie la liste reçue (effet de bord), et deux appels identiques <code>ajoute(t, 5)</code> renvoient des longueurs différentes. Version pure : <code>def ajoute(t, x): return t + [x]</code>, qui renvoie une nouvelle liste (dont on prendra la longueur si besoin).</p>` },
      { q: "Pour chacune des applications suivantes, proposer un paradigme et justifier en une phrase : (a) un jeu vidéo avec de nombreux personnages ; (b) le calcul de statistiques sur des millions de lignes réparties sur plusieurs serveurs ; (c) le pilote d’une carte réseau.", pts: "1,5 pt", c: `<p>(a) <b>Objet</b> : chaque personnage est une entité avec un état (position, vie) et des comportements ; une classe par type de personnage. (b) <b>Fonctionnel</b> : des transformations sans effet de bord (map, filter, reduce) peuvent s’exécuter en parallèle sur chaque serveur sans conflit. (c) <b>Impératif</b> : il faut contrôler précisément la mémoire et les registres du matériel, au plus près de la machine.</p>` },
      { q: "Python est dit « multi-paradigme ». Expliquer, avec un exemple de programme qui mélange deux paradigmes.", pts: "1 pt", c: `<p>Python permet d’écrire des instructions et des boucles (impératif), des classes (objet) et des fonctions d’ordre supérieur, lambda, map, filter (fonctionnel). Exemple : une méthode de classe qui trie ses données avec <code>sorted(self.eleves, key=lambda e: e.moyenne)</code> mélange objet et fonctionnel.</p>` }
    ],
    methode: `<p>Pour reconnaître le paradigme d’un code : des <b>affectations qui modifient</b> et des boucles → impératif ; <code>class</code>, <code>self</code>, des méthodes → objet ; des fonctions passées en paramètre, <code>lambda</code>, <code>map</code>, de la récursion sans modification → fonctionnel. Pour « choisir un paradigme », la réponse attendue est toujours une <b>justification par l’application</b>.</p>` },
  qcm: [
    { q: "Qu’est-ce qu’un paradigme de programmation ?", c: ["Un langage de programmation", "Une façon de concevoir et de structurer un programme", "Un type de bug", "Un compilateur"], a: 1, e: "Un style, avec ses concepts : instructions et état, fonctions, objets.", ref: "i1" },
    { q: "Quel paradigme repose sur des instructions qui modifient un état ?", c: ["Impératif", "Fonctionnel", "Logique", "Déclaratif"], a: 0, e: "Affectations, boucles, tests : on décrit comment faire.", ref: "i2" },
    { q: "Une fonction pure…", c: ["n’a pas de paramètre", "renvoie un résultat qui ne dépend que de ses paramètres et n’a aucun effet de bord", "ne contient pas de boucle", "est écrite en une ligne"], a: 1, e: "Même appel, même résultat, rien de modifié à l’extérieur.", ref: "i3" },
    { q: "Laquelle de ces fonctions a un effet de bord ?", c: ["<code>def f(t): return len(t)</code>", "<code>def f(t): return t + [0]</code>", "<code>def f(t): t.append(0)</code>", "<code>def f(x): return x * x</code>"], a: 2, e: "append modifie la liste reçue en paramètre.", ref: "i3" },
    { q: "Que renvoie <code>list(map(lambda x: 2 * x, [1, 2, 3]))</code> ?", c: ["[1, 2, 3]", "[2, 4, 6]", "12", "[1, 4, 9]"], a: 1, e: "map applique la fonction à chaque élément.", ref: "i4" },
    { q: "Que renvoie <code>list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]))</code> ?", c: ["[2, 4]", "[1, 3, 5]", "[True, False, True, False, True]", "3"], a: 1, e: "filter garde les éléments pour lesquels la fonction renvoie True.", ref: "i4" },
    { q: "Qu’est-ce qu’une fonction d’ordre supérieur ?", c: ["Une fonction très rapide", "Une fonction qui prend une fonction en paramètre ou en renvoie une", "Une fonction récursive", "Une méthode de classe"], a: 1, e: "Exemples : map, filter, sorted avec key.", ref: "i4" },
    { q: "Quel type Python est immuable ?", c: ["list", "dict", "tuple", "set"], a: 2, e: "On ne peut pas modifier un tuple ; on en fabrique un nouveau.", ref: "i4" },
    { q: "Dans le paradigme objet, où se trouve l’état ?", c: ["Dans des variables globales", "Dans les attributs de chaque objet", "Il n’y a pas d’état", "Dans les paramètres des fonctions"], a: 1, e: "Chaque instance a ses propres attributs, manipulés par ses méthodes.", ref: "i5" },
    { q: "Quel langage a introduit les classes et les objets, en 1967 ?", c: ["C", "Simula", "LISP", "Python"], a: 1, e: "Simula 67, de Dahl et Nygaard.", ref: "i5" },
    { q: "Quel avantage a la version fonctionnelle du compte bancaire ?", c: ["Elle est plus courte", "On peut rejouer l’historique, rien n’étant modifié", "Elle utilise moins de mémoire", "Elle n’a pas besoin de fonctions"], a: 1, e: "Les opérations sont des données ; le solde à tout moment se recalcule.", ref: "i6" },
    { q: "Quel paradigme choisir pour une interface graphique avec de nombreuses fenêtres et boutons ?", c: ["Objet", "Uniquement impératif", "Logique", "Aucun"], a: 0, e: "Chaque élément est une entité avec un état et des comportements.", ref: "i7" },
    { q: "Que signifie « Python est multi-paradigme » ?", c: ["Il a plusieurs versions", "On peut y programmer en impératif, en objet et en fonctionnel, et les mélanger", "Il est compilé et interprété", "Il fonctionne sur plusieurs systèmes"], a: 1, e: "Le BO insiste : un même langage, un même programme peuvent mêler les paradigmes.", ref: "i7" },
    { q: "Que renvoie <code>t.sort()</code> ?", c: ["La liste triée", "None, car elle trie t sur place", "Une copie triée", "Un booléen"], a: 1, e: "Méthode impérative ; sorted(t) est sa version fonctionnelle.", ref: "i2" }
  ],
  cartes: [
    { r: "Paradigme de programmation", v: "Façon de concevoir et structurer un programme : impératif, fonctionnel, objet (et déclaratif / logique, hors programme)." },
    { r: "Paradigme impératif", v: "Séquence d’instructions qui modifient un état : affectations, boucles, tests. Proche de la machine. C, Fortran." },
    { r: "Paradigme fonctionnel", v: "Composition de fonctions pures, données immuables, récursivité, fonctions comme valeurs. Haskell, OCaml, LISP." },
    { r: "Paradigme objet", v: "Objets regroupant attributs (état) et méthodes, instances de classes ; encapsulation. Simula, Smalltalk, Java." },
    { r: "Effet de bord", v: "Modification de quelque chose hors des variables locales : variable globale, liste reçue, fichier, affichage." },
    { r: "Fonction pure", v: "Son résultat ne dépend que de ses paramètres et elle n’a aucun effet de bord." },
    { r: "Fonction d’ordre supérieur", v: "Fonction qui prend une fonction en paramètre ou en renvoie une : map, filter, sorted(…, key=…)." },
    { r: "map / filter / reduce", v: "map(f, t) : f appliquée à chaque élément ; filter(p, t) : éléments qui vérifient p ; reduce(f, t, init) : combine les éléments dans un accumulateur." },
    { r: "lambda", v: "Petite fonction anonyme : lambda x: x * x. Le mot vient du lambda-calcul de Church (1936)." },
    { r: "t.sort() / sorted(t)", v: "t.sort() trie sur place et renvoie None (impératif) ; sorted(t) renvoie une nouvelle liste (fonctionnel)." },
    { r: "Choisir un paradigme", v: "Matériel, performance → impératif ; entités avec état (interfaces, jeux) → objet ; transformation de données, parallélisme → fonctionnel." },
    { r: "Multi-paradigme", v: "Langage qui permet plusieurs paradigmes, mélangeables dans un même programme : Python, JavaScript, OCaml." },
    { r: "Dates des paradigmes", v: "Fortran 1957, LISP 1958, Simula 1967, C 1972, Smalltalk 1972, Prolog 1972, Haskell 1990, Java 1995, OCaml 1996." }
  ]
});
