/* ===================== Chapitre 3 — Listes, piles, files ===================== */
C("c3-tad-liste", String.raw`
# Une implémentation du type abstrait Liste avec des couples (tête, queue)
def liste_vide():
    return None

def est_vide(lst):
    return lst is None

def ajoute(x, lst):          # renvoie une NOUVELLE liste : x suivi de lst
    return (x, lst)

def tete(lst):
    return lst[0]

def queue(lst):
    return lst[1]

l = ajoute(3, ajoute(5, ajoute(8, liste_vide())))
print(l)
print(tete(l), tete(queue(l)), est_vide(queue(queue(queue(l)))))`, { fichier: "liste_couples.py", out: "(3, (5, (8, None)))\n3 5 True" });

C("c3-tad-longueur", String.raw`
def longueur(lst):
    """N'utilise QUE l'interface : marche quelle que soit l'implémentation."""
    if est_vide(lst):
        return 0
    return 1 + longueur(queue(lst))

print(longueur(l), longueur(liste_vide()))`, { deps: ["c3-tad-liste"], out: "3 0" });

C("c3-maillon", String.raw`
class Maillon:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant       # Maillon suivant, ou None à la fin`, { fichier: "maillon.py", out: "" });

C("c3-maillon-fonctions", String.raw`
def longueur(m):                 # m : premier maillon, ou None
    if m is None:
        return 0
    return 1 + longueur(m.suivant)

def ieme(m, i):
    """Valeur du maillon d'indice i (0 pour le premier)."""
    while i > 0:
        m = m.suivant
        i = i - 1
    return m.valeur

def appartient(m, x):
    while m is not None:
        if m.valeur == x:
            return True
        m = m.suivant
    return False

lst = Maillon(3, Maillon(5, Maillon(8)))
print(longueur(lst), ieme(lst, 2), appartient(lst, 5), appartient(lst, 4))`, { deps: ["c3-maillon"], out: "3 8 True False" });

C("c3-liste-chainee", String.raw`
class ListeChainee:
    def __init__(self):
        self.tete = None                 # liste vide

    def est_vide(self):
        return self.tete is None

    def ajouter_tete(self, v):           # coût constant
        self.tete = Maillon(v, self.tete)

    def supprimer_tete(self):            # coût constant
        assert not self.est_vide(), "liste vide"
        v = self.tete.valeur
        self.tete = self.tete.suivant
        return v

    def ajouter_queue(self, v):          # coût linéaire : on parcourt tout
        if self.tete is None:
            self.tete = Maillon(v)
        else:
            m = self.tete
            while m.suivant is not None:
                m = m.suivant
            m.suivant = Maillon(v)

    def longueur(self):                  # coût linéaire
        n = 0
        m = self.tete
        while m is not None:
            n = n + 1
            m = m.suivant
        return n

    def __str__(self):
        morceaux = []
        m = self.tete
        while m is not None:
            morceaux.append(str(m.valeur))
            m = m.suivant
        return " -> ".join(morceaux + ["None"])

l = ListeChainee()
for v in [8, 5, 3]:
    l.ajouter_tete(v)
l.ajouter_queue(13)
print(l, "| longueur :", l.longueur())
print(l.supprimer_tete(), "|", l)`, { deps: ["c3-maillon"], fichier: "liste_chainee.py", out: "3 -> 5 -> 8 -> 13 -> None | longueur : 4\n3 | 5 -> 8 -> 13 -> None" });

C("c3-pile-liste", String.raw`
class Pile:
    """Pile implémentée avec une liste Python : le sommet est la FIN de la liste."""

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return len(self.contenu) == 0

    def empiler(self, x):
        self.contenu.append(x)           # coût constant

    def depiler(self):
        if self.est_vide():
            raise IndexError("dépiler une pile vide")
        return self.contenu.pop()        # coût constant

    def sommet(self):
        if self.est_vide():
            raise IndexError("pile vide")
        return self.contenu[-1]

    def taille(self):
        return len(self.contenu)

p = Pile()
for x in [1, 2, 3]:
    p.empiler(x)
print(p.depiler(), p.sommet(), p.taille())`, { fichier: "pile.py", out: "3 2 2" });

C("c3-pile-chainee", String.raw`
class Pile:
    """Même interface, implémentée avec des maillons : le sommet est la tête."""

    def __init__(self):
        self.haut = None

    def est_vide(self):
        return self.haut is None

    def empiler(self, x):
        self.haut = Maillon(x, self.haut)

    def depiler(self):
        if self.est_vide():
            raise IndexError("dépiler une pile vide")
        x = self.haut.valeur
        self.haut = self.haut.suivant
        return x

p = Pile()
for x in [1, 2, 3]:
    p.empiler(x)
print(p.depiler(), p.depiler(), p.est_vide())`, { deps: ["c3-maillon"], fichier: "pile_chainee.py", out: "3 2 False" });

C("c3-pile-vide", String.raw`
p = Pile()
p.empiler("a")
p.depiler()
p.depiler()`, { deps: ["c3-pile-liste"], err: "IndexError: dépiler une pile vide" });

C("c3-npi", String.raw`
def evaluer_npi(expression):
    """Évalue une expression en notation polonaise inverse (NPI),
    par exemple "3 4 + 2 *", qui vaut (3 + 4) * 2."""
    p = Pile()
    for jeton in expression.split():
        if jeton in ["+", "-", "*", "/"]:
            b = p.depiler()              # le 2e opérande est au sommet
            a = p.depiler()
            if jeton == "+":
                p.empiler(a + b)
            elif jeton == "-":
                p.empiler(a - b)
            elif jeton == "*":
                p.empiler(a * b)
            else:
                p.empiler(a / b)
        else:
            p.empiler(int(jeton))
    return p.depiler()

print(evaluer_npi("3 4 + 2 *"))          # (3 + 4) * 2
print(evaluer_npi("10 2 8 * + 3 -"))     # 10 + 2 * 8 - 3`, { deps: ["c3-pile-liste"], out: "14\n23" });

C("c3-file-liste", String.raw`
class FileListe:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def enfiler(self, x):
        self.contenu.append(x)           # à la queue : coût constant

    def defiler(self):
        return self.contenu.pop(0)       # à la tête : TOUS les éléments sont décalés`, { verif: "f = FileListe()\nfor x in 'abc':\n    f.enfiler(x)\nprint(f.defiler(), f.defiler(), f.est_vide())", out: "a b False", montrer: false });

C("c3-file-chainee", String.raw`
class File:
    def __init__(self):
        self.tete = None       # on défile ici
        self.queue = None      # on enfile ici

    def est_vide(self):
        return self.tete is None

    def enfiler(self, x):                # coût constant
        m = Maillon(x)
        if self.est_vide():
            self.tete = m
        else:
            self.queue.suivant = m
        self.queue = m

    def defiler(self):                   # coût constant
        if self.est_vide():
            raise IndexError("défiler une file vide")
        x = self.tete.valeur
        self.tete = self.tete.suivant
        if self.tete is None:            # la file est devenue vide
            self.queue = None
        return x

f = File()
for client in ["Ada", "Alan", "Grace"]:
    f.enfiler(client)
print(f.defiler(), f.defiler())
f.enfiler("Linus")
print(f.defiler(), f.defiler(), f.est_vide())`, { deps: ["c3-maillon"], fichier: "file_chainee.py", out: "Ada Alan\nGrace Linus True" });

C("c3-file-2piles", String.raw`
class File2P:
    """File réalisée avec deux piles (deux listes Python utilisées en piles)."""

    def __init__(self):
        self.entree = []        # on empile ici à chaque enfiler
        self.sortie = []        # on dépile ici à chaque défiler

    def est_vide(self):
        return self.entree == [] and self.sortie == []

    def enfiler(self, x):
        self.entree.append(x)

    def defiler(self):
        if self.sortie == []:
            while self.entree != []:                  # on renverse entree
                self.sortie.append(self.entree.pop()) # dans sortie
        if self.sortie == []:
            raise IndexError("défiler une file vide")
        return self.sortie.pop()

f = File2P()
for x in [1, 2, 3]:
    f.enfiler(x)
print(f.defiler(), f.entree, f.sortie)
f.enfiler(4)
print(f.defiler(), f.defiler(), f.defiler(), f.est_vide())`, { fichier: "file_deux_piles.py", out: "1 [] [3, 2]\n2 3 4 True" });

C("c3-deque", String.raw`
from collections import deque     # « double-ended queue »

f = deque()
f.append("Ada")                   # enfiler à droite
f.append("Alan")
print(f.popleft(), len(f))        # défiler à gauche, en temps constant`, { out: "Ada 1" });

/* pièges */
C("c3-p-tete", String.raw`
def afficher(lst):               # lst : un objet ListeChainee
    while lst.tete is not None:
        print(lst.tete.valeur, end=" ")
        lst.tete = lst.tete.suivant    # on avance... en déplaçant la tête !

l = ListeChainee()
for v in [8, 5, 3]:
    l.ajouter_tete(v)
afficher(l)
print("| vide ?", l.est_vide())`, { deps: ["c3-maillon", "c3-liste-chainee"], out: "3 5 8 | vide ? True" });

C("c3-p-ordre", String.raw`
p = Pile()
p.empiler(10)
p.empiler(4)
b = p.depiler()        # 4 : le DERNIER empilé
a = p.depiler()        # 10
print(a - b, b - a)`, { deps: ["c3-pile-liste"], out: "6 -6" });

/* prédis la sortie */
C("c3-x1", String.raw`
p = []
for x in [4, 7, 1]:
    p.append(x)
p.pop()
p.append(9)
print(p.pop(), p.pop(), p)`, { out: "9 7 [4]" });

C("c3-x2", String.raw`
f = []
for lettre in "NSI":
    f.append(lettre)
print(f.pop(0) + f.pop(0), f)`, { out: "NS ['I']" });

C("c3-x3", String.raw`
class Maillon:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

m = Maillon(1, Maillon(2, Maillon(3)))
m.suivant.suivant = Maillon(4)
m = Maillon(0, m)
c = m
while c is not None:
    print(c.valeur, end=" ")
    c = c.suivant`, { out: "0 1 2 4" });

C("c3-x4", String.raw`
def mystere(mot):
    pile = []
    for lettre in mot:
        pile.append(lettre)
    resultat = ""
    while pile:                      # tant que la pile n'est pas vide
        resultat = resultat + pile.pop()
    return resultat

print(mystere("radar"), mystere("pile"))`, { out: "radar elip" });

/* épreuve pratique 1 */
C("c3-ep1-fourni", String.raw`
def bien_parenthesee(expr):
    """Renvoie True si les parenthèses ( et ) de expr sont bien équilibrées."""
    p = []                          # pile des parenthèses ouvrantes
    for c in expr:
        if c == "(":
            ...
        elif c == ")":
            if ...:
                return False
            p.pop()
    return True`, { fichier: "parentheses.py", run: false, trous: [6, 8] });

C("c3-ep1-corr", String.raw`
def bien_parenthesee(expr):
    p = []
    for c in expr:
        if c == "(":
            p.append(c)
        elif c == ")":
            if len(p) == 0:          # fermante sans ouvrante
                return False
            p.pop()
    return len(p) == 0               # il ne doit rester aucune ouvrante

def bien_parenthesee_multi(expr):
    """Même chose avec (), [] et {}."""
    ouvrante = {")": "(", "]": "[", "}": "{"}
    p = []
    for c in expr:
        if c in "([{":
            p.append(c)
        elif c in ")]}":
            if len(p) == 0 or p.pop() != ouvrante[c]:
                return False
    return len(p) == 0

def test():
    assert bien_parenthesee("(a+b)*(c-d)")
    assert bien_parenthesee("")                      # chaîne vide
    assert not bien_parenthesee("((a)")              # le bug de la version fournie
    assert not bien_parenthesee(")(")
    assert bien_parenthesee_multi("f(x[2]) + {y}")
    assert not bien_parenthesee_multi("(a]")
    assert not bien_parenthesee_multi("([)]")        # croisées : un compteur ne verrait rien
    assert not bien_parenthesee_multi("[")

test()
print("tous les tests passent")`, { fichier: "parentheses.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c3-ep2-fourni", String.raw`
class File:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return self.elements == []

    def enfiler(self, x):
        self.elements.append(x)

    def defiler(self):
        return self.elements.pop()

    def taille(self):
        ...

def josephe(n, k):
    """n personnes numérotées de 1 à n sont en cercle. On compte k personnes ;
    la k-ième sort du cercle ; on recommence à compter avec la suivante.
    Renvoie la liste des numéros dans l'ordre de sortie."""
    ...`, { fichier: "josephe.py", run: false, trous: [14, 20] });

C("c3-ep2-corr", String.raw`
class File:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return self.elements == []

    def enfiler(self, x):
        self.elements.append(x)

    def defiler(self):
        assert not self.est_vide(), "file vide"
        return self.elements.pop(0)          # la TÊTE, pas la fin

    def taille(self):
        return len(self.elements)

def josephe(n, k):
    f = File()
    for i in range(1, n + 1):
        f.enfiler(i)
    ordre = []
    while not f.est_vide():
        for _ in range(k - 1):               # les k-1 premiers passent derrière
            f.enfiler(f.defiler())
        ordre.append(f.defiler())            # le k-ième sort
    return ordre

def test():
    f = File()
    for x in [1, 2, 3]:
        f.enfiler(x)
    assert f.defiler() == 1 and f.taille() == 2      # FIFO
    assert josephe(7, 3) == [3, 6, 2, 7, 5, 1, 4]
    assert josephe(1, 5) == [1]
    assert josephe(5, 1) == [1, 2, 3, 4, 5]
    assert josephe(41, 3)[-1] == 31

test()
print("tous les tests passent")`, { fichier: "josephe.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c3-ecrit-corr", String.raw`
class Navigateur:
    def __init__(self, accueil):
        self.courante = accueil
        self.precedentes = Pile()
        self.suivantes = Pile()

    def visiter(self, url):
        self.precedentes.empiler(self.courante)
        self.courante = url
        self.suivantes = Pile()                 # on oublie les pages « suivantes »

    def retour(self):
        if not self.precedentes.est_vide():
            self.suivantes.empiler(self.courante)
            self.courante = self.precedentes.depiler()

    def avancer(self):
        if not self.suivantes.est_vide():
            self.precedentes.empiler(self.courante)
            self.courante = self.suivantes.depiler()

n = Navigateur("accueil")
for page in ["a", "b", "c"]:
    n.visiter(page)
n.retour()
n.retour()
n.visiter("d")
n.retour()
print(n.courante, n.precedentes.contenu, n.suivantes.contenu)
n.avancer()
n.avancer()                                     # sans effet : plus de page suivante
print(n.courante)`, { deps: ["c3-pile-liste"], out: "a ['accueil'] ['d']\nd" });

C("c3-retenir", String.raw`
p = []            # pile avec une liste Python
p.append(x)       # empiler : coût constant
p.pop()           # dépiler (le sommet = la fin) : coût constant

f = []            # file avec une liste Python (simple mais lente)
f.append(x)       # enfiler à la queue
f.pop(0)          # défiler la tête : coût LINÉAIRE (tout est décalé)`, { run: false });

CH.push({
  id: "ch3", n: 3, court: "lineaires", fichier: "ch3_lineaires.py",
  titre: "Listes, piles, files",
  rubrique: "Rubrique « Structures de données » : interface et implémentation, structures linéaires",
  accroche: "Type abstrait, interface et implémentation ; listes chaînées, piles (LIFO), files (FIFO), et leurs coûts.",
  essentiel: [
    "Un <b>type abstrait</b> est décrit par son <b>interface</b> (ce qu’on peut faire) ; une <b>implémentation</b> dit comment c’est fait.",
    "Une <b>pile</b> est LIFO (dernier entré, premier sorti) : empiler, dépiler, est_vide.",
    "Une <b>file</b> est FIFO (premier entré, premier sorti) : enfiler, défiler, est_vide.",
    "Une <b>liste chaînée</b> est une suite de maillons (valeur + référence vers le suivant) : ajout en tête en temps constant, accès au <i>i</i>-ème en temps linéaire.",
    "Le type <code>list</code> de Python est un <b>tableau dynamique</b> : <code>append</code> et <code>pop()</code> sont rapides en fin, mais <code>pop(0)</code> et <code>insert(0, x)</code> décalent tout."
  ],
  attendus: [
    "Spécifier une structure de données par son interface ; distinguer interface et implémentation.",
    "Écrire plusieurs implémentations d’une même structure (le BO cite la file avec un tableau ou avec deux piles).",
    "Distinguer listes, piles et files par le jeu des méthodes qui les caractérisent ; distinguer les modes LIFO et FIFO.",
    "Choisir une structure de données adaptée à la situation à modéliser.",
    "Utiliser la programmation objet pour implémenter ces structures (lien avec le chapitre 1) et la récursivité pour les parcourir (chapitre 2)."
  ],
  idees: [
    { id: "i1", t: "Interface et implémentation : le type abstrait", h: `
<div class="boite def"><div class="lab">"""définitions"""</div>
<p>Un <b>type abstrait de données</b> est défini par son <b>interface</b> : la liste des opérations possibles, avec ce qu’elles prennent et ce qu’elles renvoient (et éventuellement leur coût).<br>
Une <b>implémentation</b> est une façon concrète de réaliser cette interface en Python (avec une liste, des maillons, deux piles…).</p></div>
<p>Comme une télécommande : tu sais ce que fait chaque bouton (interface) sans savoir comment le circuit est câblé (implémentation). On peut changer le circuit sans changer la façon de s’en servir.</p>
<div class="tab-wrap"><table><tr><th>opération</th><th>rôle</th><th>pile</th><th>file</th></tr>
<tr><td>créer</td><td>structure vide</td><td><code>Pile()</code></td><td><code>File()</code></td></tr>
<tr><td>tester</td><td>est-elle vide ?</td><td><code>est_vide()</code></td><td><code>est_vide()</code></td></tr>
<tr><td>ajouter</td><td>insérer un élément</td><td><code>empiler(x)</code> au sommet</td><td><code>enfiler(x)</code> à la queue</td></tr>
<tr><td>retirer</td><td>enlever et renvoyer</td><td><code>depiler()</code> le sommet</td><td><code>defiler()</code> la tête</td></tr>
<tr><td>consulter (option)</td><td>lire sans retirer</td><td><code>sommet()</code></td><td><code>tete()</code></td></tr></table></div>
<p>Le code qui <b>utilise</b> une pile ne doit appeler que ces opérations : il marchera avec n’importe quelle implémentation. C’est ce qui permet de travailler à plusieurs et de remplacer une implémentation lente par une rapide (lien avec la modularité, chapitre 4). Les noms exacts varient d’un sujet à l’autre : l’énoncé donne toujours l’interface à utiliser.</p>` },

    { id: "i2", t: "Le type abstrait Liste", h: `
<p>Une <b>liste</b> (au sens des structures de données) est soit <b>vide</b>, soit formée d’une <b>tête</b> (son premier élément) et d’une <b>queue</b> (la liste des éléments suivants). C’est une définition <b>récursive</b>. Interface minimale : créer une liste vide, tester si elle est vide, ajouter un élément en tête, lire la tête, obtenir la queue.</p>
[[c3-tad-liste]]
<p>Une fonction qui n’utilise que l’interface est indépendante de l’implémentation, et elle se programme naturellement en récursif :</p>
[[c3-tad-longueur]]
<div class="boite attention"><div class="lab">⚠ ne pas confondre</div><p>Le type <code>list</code> de Python n’est <b>pas</b> une liste chaînée : c’est un <b>tableau dynamique</b> (cases contiguës en mémoire, qu’on agrandit au besoin). Le mot « liste » désigne donc deux choses différentes : lis bien l’énoncé.</p></div>` },

    { id: "i3", t: "La liste chaînée : des maillons reliés", h: `
<p>Une <b>liste chaînée</b> est une implémentation de la liste : chaque <b>maillon</b> (ou cellule) contient une <b>valeur</b> et une <b>référence</b> vers le maillon suivant ; le dernier maillon pointe vers <code>None</code>. On ne garde que la référence du premier maillon : la <b>tête</b>.</p>
[[c3-maillon]]
[[w-liste-chainee]]
<p>Pour atteindre un maillon, il faut suivre les liens depuis la tête : on ne peut pas sauter directement à la case <i>i</i> comme dans un tableau.</p>
[[c3-maillon-fonctions]]
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1955-1956 <b>·</b></span> Allen Newell, Cliff Shaw et Herbert Simon inventent les listes chaînées pour leur langage IPL, consacré à l’intelligence artificielle.</p></div>` },

    { id: "i4", t: "Une classe ListeChainee", h: `
<p>On regroupe la tête et les opérations dans une classe. Remarque le coût de chaque méthode : il dépend du nombre de maillons à parcourir.</p>
[[c3-liste-chainee]]
<ul><li><code>ajouter_tete</code> et <code>supprimer_tete</code> ne touchent qu’au premier maillon : <b>coût constant</b>, quelle que soit la longueur.</li>
<li><code>ajouter_queue</code> et <code>longueur</code> parcourent toute la liste : <b>coût linéaire</b>. On peut rendre <code>ajouter_queue</code> constant en gardant aussi une référence vers le dernier maillon (c’est ce que fait la file de l’idée 8).</li></ul>` },

    { id: "i5", t: "Tableau ou liste chaînée : comparer les coûts", h: `
<div class="tab-wrap"><table><tr><th>opération</th><th>tableau dynamique (<code>list</code> de Python)</th><th>liste chaînée</th></tr>
<tr><td>lire ou modifier l’élément d’indice <i>i</i></td><td>constant : <code>t[i]</code></td><td>linéaire (suivre <i>i</i> liens)</td></tr>
<tr><td>ajouter / retirer à la fin</td><td>constant (en moyenne) : <code>append</code>, <code>pop()</code></td><td>linéaire, ou constant avec une référence vers la queue</td></tr>
<tr><td>ajouter / retirer au début</td><td>linéaire : <code>insert(0, x)</code>, <code>pop(0)</code> décalent tout</td><td>constant</td></tr>
<tr><td>longueur</td><td>constant : <code>len(t)</code></td><td>linéaire (ou constant si on tient un compteur)</td></tr></table></div>
<p>Aucune structure n’est meilleure partout : on choisit selon les opérations les plus fréquentes. Pour une file d’attente de 100 000 clients, défiler avec <code>pop(0)</code> décale 99 999 éléments à chaque client servi ; avec une liste chaînée, rien n’est décalé.</p>` },

    { id: "i6", t: "La pile (LIFO) et ses implémentations", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Une <b>pile</b> (<i>stack</i>) est une structure où l’on ajoute et retire <b>du même côté</b>, le <b>sommet</b> : le dernier élément entré est le premier sorti, en anglais <b>LIFO</b> (<i>Last In, First Out</i>).</p></div>
<p>Exemples : la pile d’assiettes, le bouton « Retour » du navigateur, l’annulation <kbd>Ctrl</kbd>+<kbd>Z</kbd> (on annule la dernière action), la pile d’exécution des appels de fonction (chapitre 2).</p>
[[w-pile-file|pile]]
<p><b>Implémentation 1</b>, avec une liste Python dont la fin est le sommet :</p>
[[c3-pile-liste]]
<p><b>Implémentation 2</b>, avec des maillons dont la tête est le sommet. L’interface est identique : un programme qui utilise la pile ne voit pas la différence.</p>
[[c3-pile-chainee]]
<p>Dépiler une pile vide est une erreur : l’implémentation lève une exception, et le programme qui l’utilise doit tester <code>est_vide()</code> avant.</p>
[[c3-pile-vide]]` },

    { id: "i7", t: "Une pile pour calculer : la notation polonaise inverse", h: `
<p>En <b>notation polonaise inverse</b> (NPI), l’opérateur s’écrit <b>après</b> ses deux opérandes : <code>3 4 +</code> signifie 3 + 4, et <code>3 4 + 2 *</code> signifie (3 + 4) × 2. Plus besoin de parenthèses. L’évaluation se fait avec une pile : un nombre est empilé ; un opérateur dépile deux nombres et empile le résultat.</p>
[[c3-npi]]
<p>Attention à l’ordre : le premier nombre dépilé est le <b>second</b> opérande (pour <code>10 3 -</code>, on dépile 3 puis 10 et on calcule 10 − 3).</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1955 <b>·</b></span> Friedrich L. Bauer et Klaus Samelson (Munich) décrivent l’évaluation des expressions à l’aide d’une pile, le « principe de la cave » (<i>Kellerprinzip</i>).<br><span class="commit">1972 <b>·</b></span> La calculatrice de poche HP-35 de Hewlett-Packard fonctionne en NPI.</p></div>` },

    { id: "i8", t: "La file (FIFO) et ses implémentations", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Une <b>file</b> (<i>queue</i>) est une structure où l’on ajoute d’un côté (la <b>queue</b>) et retire de l’autre (la <b>tête</b>) : le premier entré est le premier sorti, <b>FIFO</b> (<i>First In, First Out</i>).</p></div>
<p>Exemples : la file d’attente d’un guichet, la file d’impression, les touches tapées au clavier en attente de traitement, l’ordonnancement de processus, le parcours en largeur d’un arbre ou d’un graphe (chapitres à venir).</p>
[[w-pile-file|file]]
<p><b>Implémentation 1</b>, avec une liste Python : simple, mais <code>pop(0)</code> a un coût linéaire.</p>
[[c3-file-liste]]
<p><b>Implémentation 2</b>, avec des maillons et <b>deux références</b>, tête et queue : enfiler et défiler en temps constant.</p>
[[c3-file-chainee]]
<p><b>Implémentation 3</b>, avec <b>deux piles</b> (exemple cité par le programme) : on empile dans <code>entree</code> ; pour défiler, on dépile <code>sortie</code>, et si elle est vide on y verse d’abord toute la pile <code>entree</code>, ce qui inverse l’ordre et remet le plus ancien au sommet. Choisis « file avec deux piles » dans le schéma ci-dessus pour le voir.</p>
[[c3-file-2piles]]
<p>Un transfert coûte cher, mais chaque élément n’est transféré <b>qu’une fois</b> : sur une longue suite d’opérations, le coût moyen par opération reste constant (on parle de coût <b>amorti</b>).</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Le module standard <code>collections</code> fournit <code>deque</code>, une file à deux bouts efficace.</p>[[c3-deque]]</div>` },

    { id: "i9", t: "Choisir la bonne structure", h: `
<div class="tab-wrap"><table><tr><th>situation</th><th>structure</th><th>pourquoi</th></tr>
<tr><td>annuler les dernières actions d’un éditeur</td><td>pile</td><td>on annule la plus récente d’abord</td></tr>
<tr><td>vérifier des parenthèses, évaluer une expression</td><td>pile</td><td>la dernière ouvrante doit être fermée en premier</td></tr>
<tr><td>servir des clients, des impressions, des requêtes dans l’ordre d’arrivée</td><td>file</td><td>premier arrivé, premier servi</td></tr>
<tr><td>accéder souvent à l’élément n° <i>i</i></td><td>tableau (<code>list</code>)</td><td>accès en temps constant</td></tr>
<tr><td>insérer et supprimer souvent en tête</td><td>liste chaînée</td><td>pas de décalage</td></tr>
<tr><td>retrouver une valeur à partir d’une clé (nom → numéro)</td><td>dictionnaire</td><td>recherche par clé (chapitre à venir)</td></tr></table></div>
<p>À l’écrit, une question classique : « Pourquoi utiliser une pile plutôt qu’une file ici ? » La réponse se justifie toujours par l’ordre de sortie voulu (LIFO ou FIFO).</p>` }
  ],
  pieges: [
    { t: "Confondre la pile et la file", h: `<p>Pile : on retire le <b>dernier</b> ajouté (LIFO). File : on retire le <b>premier</b> ajouté (FIFO). Avec une liste Python : pile = <code>append</code> + <code>pop()</code> ; file = <code>append</code> + <code>pop(0)</code>.</p>` },
    { t: "Dépiler (ou défiler) une structure vide", h: `<p>Toujours tester <code>est_vide()</code> avant <code>depiler()</code> : <code>while not p.est_vide(): x = p.depiler()</code>. Sur une liste Python vide, <code>pop()</code> lève <code>IndexError: pop from empty list</code>.</p>` },
    { t: "Perdre la tête de la liste en la parcourant", h: `[[c3-p-tete]]<p>En déplaçant <code>lst.tete</code> pour avancer, on détruit la liste. Il faut une variable de parcours : <code>m = lst.tete</code> puis <code>m = m.suivant</code>.</p>` },
    { t: "Inverser les opérandes en dépilant", h: `[[c3-p-ordre]]<p>Le premier dépilé est le dernier empilé : pour <code>a - b</code>, on dépile d’abord <code>b</code>.</p>` },
    { t: "Oublier de mettre à jour la queue d’une file chaînée", h: `<p>Dans <code>enfiler</code>, il faut relier l’ancien dernier maillon au nouveau (<code>self.queue.suivant = m</code>) <b>et</b> déplacer la référence <code>self.queue</code>. Quand la file devient vide, la tête et la queue doivent toutes deux valoir <code>None</code>.</p>` },
    { t: "Utiliser les opérations d’une implémentation au lieu de l’interface", h: `<p>Si l’énoncé donne une interface (<code>empiler</code>, <code>depiler</code>, <code>est_vide</code>), n’écris pas <code>p.contenu[-1]</code> ou <code>len(p.contenu)</code> : tu supposerais une implémentation particulière, et la réponse est comptée fausse.</p>` }
  ],
  retenir: `
<h2>Les trois structures</h2>
<div class="tab-wrap"><table><tr><th>structure</th><th>principe</th><th>opérations</th><th>exemples</th></tr>
<tr><td>liste</td><td>vide, ou tête + queue</td><td>est_vide, ajouter en tête, tête, queue</td><td>chaîne de maillons</td></tr>
<tr><td>pile</td><td>LIFO : dernier entré, premier sorti</td><td>empiler, dépiler, est_vide, (sommet)</td><td>Ctrl+Z, retour arrière, appels de fonctions, parenthèses</td></tr>
<tr><td>file</td><td>FIFO : premier entré, premier sorti</td><td>enfiler, défiler, est_vide</td><td>file d’attente, impressions, parcours en largeur</td></tr></table></div>
<h2>Implémentations et coûts</h2>
<div class="tab-wrap"><table><tr><th>implémentation</th><th>ajouter</th><th>retirer</th></tr>
<tr><td>pile avec <code>list</code> (sommet = fin)</td><td>constant</td><td>constant</td></tr>
<tr><td>pile avec maillons (sommet = tête)</td><td>constant</td><td>constant</td></tr>
<tr><td>file avec <code>list</code> et <code>pop(0)</code></td><td>constant</td><td><b>linéaire</b></td></tr>
<tr><td>file avec maillons, tête + queue</td><td>constant</td><td>constant</td></tr>
<tr><td>file avec deux piles</td><td>constant</td><td>constant en moyenne (amorti)</td></tr></table></div>
[[c3-retenir]]
<h2>Les réflexes</h2>
<ul><li>Interface = <b>quoi</b> ; implémentation = <b>comment</b>. N’utilise que l’interface donnée.</li><li>Tester <code>est_vide()</code> avant de retirer.</li><li>Parcourir une liste chaînée avec une variable <code>m</code>, jamais en déplaçant la tête.</li><li>La <code>list</code> de Python est un tableau dynamique, pas une liste chaînée.</li><li>File avec deux piles : on ne transfère <code>entree</code> vers <code>sortie</code> que si <code>sortie</code> est vide.</li></ul>`,
  predis: [
    { code: "c3-x1", niv: "facile", rep: "Après la boucle : [4, 7, 1] ; <code>pop()</code> retire 1 ; on empile 9 : [4, 7, 9]. Les deux <code>pop()</code> renvoient 9 puis 7 ; il reste [4]. Les arguments de <code>print</code> sont évalués de gauche à droite." },
    { code: "c3-x2", niv: "facile", rep: "La liste est utilisée en file : <code>pop(0)</code> retire le premier élément. On obtient \"N\" puis \"S\", concaténés en \"NS\" ; il reste ['I']." },
    { code: "c3-x3", niv: "moyen", rep: "Chaîne de départ 1 → 2 → 3. On remplace le suivant du maillon 2 : 1 → 2 → 4 (le maillon 3 n’est plus accessible). Puis on ajoute 0 en tête : 0 → 1 → 2 → 4." },
    { code: "c3-x4", niv: "moyen", rep: "Une pile renverse l’ordre : on empile toutes les lettres, on les dépile de la dernière à la première. « radar » est un palindrome, « pile » devient « elip »." }
  ],
  ep: [
    { titre: "Expression bien parenthésée", enonce: `<p>On veut vérifier qu’une expression est bien parenthésée : chaque parenthèse fermante correspond à une ouvrante qui la précède, et il n’en reste aucune ouverte à la fin. On utilise une liste Python comme pile.</p>[[c3-ep1-fourni]]`,
      questions: [
        { q: "Compléter les lignes 6 et 8.", c: `<p>Ligne 6 : <code>p.append(c)</code> (on empile l’ouvrante). Ligne 8 : <code>len(p) == 0</code> (une fermante arrive alors qu’aucune ouvrante n’attend).</p>` },
        { q: "Tester la fonction avec <code>\"((a)\"</code>. Le résultat est-il correct ? Corriger la dernière ligne.", c: `<p>Elle renvoie True alors qu’une parenthèse reste ouverte. Il faut vérifier que la pile est vide à la fin : <code>return len(p) == 0</code>.</p>` },
        { q: "Écrire <code>bien_parenthesee_multi(expr)</code> qui gère (), [] et {}. On pourra utiliser un dictionnaire qui associe à chaque fermante son ouvrante.", c: `<p>À chaque fermante, on dépile et on vérifie que l’ouvrante dépilée est la bonne. Grâce au <code>or</code>, <code>p.pop()</code> n’est exécuté que si la pile n’est pas vide.</p>` },
        { q: "Écrire un jeu de tests pour les deux fonctions.", c: `[[c3-ep1-corr]]` },
        { q: "À l’oral : pour une seule sorte de parenthèses, un simple compteur suffirait. Pourquoi faut-il une pile avec plusieurs sortes ?", c: `<p>Un compteur par sorte accepterait <code>([)]</code> : autant d’ouvrantes que de fermantes de chaque sorte, mais elles se croisent. La pile mémorise l’<b>ordre</b> : la dernière ouverte doit être la première fermée (LIFO).</p>` }
      ] },
    { titre: "La file et le problème de Josèphe", enonce: `<p>On dispose d’une classe <code>File</code>… dont une méthode est fausse et une autre à écrire.</p>[[c3-ep2-fourni]]`,
      questions: [
        { q: "Enfiler 1, 2, 3 puis défiler une fois. Quel élément obtient-on ? Est-ce le comportement d’une file ? Corriger.", c: `<p>On obtient 3 : <code>pop()</code> retire le dernier élément, c’est le comportement d’une <b>pile</b>. Pour une file, il faut retirer le premier : <code>self.elements.pop(0)</code>.</p>` },
        { q: "Compléter la méthode <code>taille</code>.", c: `<p><code>return len(self.elements)</code>.</p>` },
        { q: "Écrire <code>josephe(n, k)</code> en utilisant <b>uniquement</b> l’interface de la classe File (pas d’accès à <code>elements</code>).", c: `<p>On enfile 1 à <i>n</i>. Tant que la file n’est pas vide : on fait passer <i>k</i> − 1 personnes de la tête à la queue (<code>f.enfiler(f.defiler())</code>), puis la suivante sort.</p>` },
        { q: "Écrire des tests. On donne : <code>josephe(7, 3)</code> vaut <code>[3, 6, 2, 7, 5, 1, 4]</code> et le dernier sorti pour <i>n</i> = 41, <i>k</i> = 3 est 31.", c: `[[c3-ep2-corr]]` },
        { q: "À l’oral : quel est le coût de <code>defiler</code> ici ? Proposer une meilleure implémentation.", c: `<p><code>pop(0)</code> décale tous les éléments : coût linéaire. Une file chaînée avec références vers la tête et la queue, ou une file à deux piles, défile en temps constant (amorti pour les deux piles). L’interface ne change pas, donc <code>josephe</code> n’a pas à être modifiée.</p>` }
      ] }
  ],
  ecrit: { titre: "L’historique d’un navigateur (piles)", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Un navigateur web mémorise la page <b>courante</b> et deux piles : <code>precedentes</code> (les pages visitées avant) et <code>suivantes</code> (les pages quittées avec le bouton Retour). On dispose d’une classe <code>Pile</code> d’interface : <code>Pile()</code>, <code>est_vide()</code>, <code>empiler(x)</code>, <code>depiler()</code>.</p>
<ul><li><code>visiter(url)</code> : la page courante est empilée dans <code>precedentes</code>, <code>url</code> devient la page courante et la pile <code>suivantes</code> est vidée ;</li>
<li><code>retour()</code> : s’il y a une page précédente, la page courante est empilée dans <code>suivantes</code> et la page précédente devient la page courante ;</li>
<li><code>avancer()</code> : l’inverse de <code>retour()</code>.</li></ul>`,
    questions: [
      { q: "Pourquoi une pile, et non une file, convient-elle pour les pages précédentes ?", pts: "0,5 pt", c: `<p>Le bouton Retour ramène à la page visitée <b>le plus récemment</b> : la dernière empilée doit sortir la première (LIFO).</p>` },
      { q: "La page courante est « accueil » et les piles sont vides. On exécute : visiter(\"a\"), visiter(\"b\"), visiter(\"c\"), retour(), retour(), visiter(\"d\"), retour(). Donner la page courante et le contenu des deux piles après chaque instruction.", pts: "1,5 pt", c: `<div class="tab-wrap"><table><tr><th>instruction</th><th>courante</th><th>precedentes (sommet à droite)</th><th>suivantes</th></tr>
<tr><td>visiter("a")</td><td>a</td><td>accueil</td><td>vide</td></tr><tr><td>visiter("b")</td><td>b</td><td>accueil, a</td><td>vide</td></tr><tr><td>visiter("c")</td><td>c</td><td>accueil, a, b</td><td>vide</td></tr>
<tr><td>retour()</td><td>b</td><td>accueil, a</td><td>c</td></tr><tr><td>retour()</td><td>a</td><td>accueil</td><td>c, b</td></tr><tr><td>visiter("d")</td><td>d</td><td>accueil, a</td><td>vide</td></tr><tr><td>retour()</td><td>a</td><td>accueil</td><td>d</td></tr></table></div>` },
      { q: "Écrire les méthodes <code>visiter</code> et <code>retour</code> de la classe <code>Navigateur</code>, dont le constructeur est <code>__init__(self, accueil)</code>.", pts: "2 pts", c: `<p>On n’utilise que l’interface de <code>Pile</code>. Pour vider <code>suivantes</code>, le plus simple est de créer une pile neuve.</p>` },
      { q: "Écrire la méthode <code>avancer</code>.", pts: "1 pt", c: `[[c3-ecrit-corr]]` },
      { q: "Pourquoi <code>visiter</code> doit-elle vider la pile <code>suivantes</code> ?", pts: "0,5 pt", c: `<p>Après une nouvelle visite, les anciennes pages « suivantes » appartiennent à un autre chemin de navigation : les proposer avec Avancer n’aurait pas de sens (c’est le comportement des navigateurs réels).</p>` },
      { q: "Quel est le coût de chaque méthode si la pile est implémentée avec une liste Python ?", pts: "0,5 pt", c: `<p>Constant : chaque méthode fait au plus un empilement et un dépilement, qui se font en fin de liste (<code>append</code>, <code>pop()</code>).</p>` }
    ],
    methode: `<p>Pour un exercice sur les piles et les files : dessine l’état des structures après chaque instruction (sommet bien repéré), respecte l’interface donnée, et justifie le choix pile/file par l’ordre de sortie.</p>` },
  qcm: [
    { q: "Que signifie LIFO ?", c: ["Le premier entré est le premier sorti", "Le dernier entré est le premier sorti", "Les éléments sortent dans l’ordre croissant", "Les éléments sortent au hasard"], a: 1, e: "Last In, First Out : c’est le mode de la pile.", ref: "i6" },
    { q: "Quelle structure est FIFO ?", c: ["La pile", "La file", "Le dictionnaire", "La liste chaînée"], a: 1, e: "First In, First Out : premier arrivé, premier servi.", ref: "i8" },
    { q: "On empile 1, 2, 3 puis on dépile deux fois. Que contient la pile ?", c: ["[1]", "[3]", "[1, 2]", "[2, 3]"], a: 0, e: "On dépile 3 puis 2 ; il reste 1.", ref: "i6" },
    { q: "On enfile 1, 2, 3 puis on défile deux fois. Que contient la file ?", c: ["[1]", "[3]", "[1, 2]", "[2, 3]"], a: 1, e: "On défile 1 puis 2 ; il reste 3.", ref: "i8" },
    { q: "Qu’est-ce qui distingue une interface d’une implémentation ?", c: ["Rien, ce sont des synonymes", "L’interface dit ce qu’on peut faire, l’implémentation comment c’est fait", "L’interface est en Python, l’implémentation en anglais", "L’implémentation est toujours plus rapide"], a: 1, e: "Une même interface peut avoir plusieurs implémentations.", ref: "i1" },
    { q: "Dans une liste chaînée, quel est le coût de l’ajout en tête ?", c: ["Constant", "Logarithmique", "Linéaire", "Quadratique"], a: 0, e: "On crée un maillon qui pointe vers l’ancienne tête : aucun parcours.", ref: "i4" },
    { q: "Dans une liste chaînée de n maillons, quel est le coût de l’accès au dernier élément (sans référence vers la queue) ?", c: ["Constant", "Logarithmique", "Linéaire", "Exponentiel"], a: 2, e: "Il faut suivre les n − 1 liens depuis la tête.", ref: "i5" },
    { q: "Pourquoi <code>pop(0)</code> sur une liste Python est-il coûteux ?", c: ["Il trie la liste", "Il décale tous les éléments restants d’une case", "Il copie la liste", "Il parcourt la liste deux fois"], a: 1, e: "La list de Python est un tableau : retirer la première case oblige à décaler les autres.", ref: "i5" },
    { q: "Pour implémenter une pile avec une liste Python <code>p</code>, on utilise…", c: ["<code>p.append(x)</code> et <code>p.pop(0)</code>", "<code>p.insert(0, x)</code> et <code>p.pop()</code>", "<code>p.append(x)</code> et <code>p.pop()</code>", "<code>p.append(x)</code> et <code>p.remove(x)</code>"], a: 2, e: "Le sommet est la fin de la liste : ajout et retrait en temps constant.", ref: "i6" },
    { q: "Dans une file réalisée avec deux piles <code>entree</code> et <code>sortie</code>, quand transfère-t-on les éléments ?", c: ["À chaque enfiler", "À chaque défiler", "Quand on défile et que <code>sortie</code> est vide", "Jamais"], a: 2, e: "On verse <code>entree</code> dans <code>sortie</code> seulement si <code>sortie</code> est vide : l’ordre s’inverse et le plus ancien arrive au sommet.", ref: "i8" },
    { q: "Quelle est la valeur de l’expression NPI <code>2 3 4 * +</code> ?", c: ["20", "14", "24", "9"], a: 1, e: "On empile 2, 3, 4 ; * dépile 4 et 3 et empile 12 ; + dépile 12 et 2 et empile 14.", ref: "i7" },
    { q: "Quelle structure choisir pour la fonction « annuler » (Ctrl+Z) d’un éditeur ?", c: ["Une file", "Une pile", "Un dictionnaire", "Un tableau trié"], a: 1, e: "On annule d’abord la dernière action : LIFO.", ref: "i9" },
    { q: "Le type <code>list</code> de Python est…", c: ["une liste chaînée", "un tableau dynamique", "une pile", "un dictionnaire"], a: 1, e: "Ses éléments sont rangés dans des cases contiguës : accès par indice en temps constant.", ref: "i2" }
  ],
  cartes: [
    { r: "Type abstrait de données", v: "Structure définie par son interface (opérations possibles), indépendamment de son implémentation." },
    { r: "Interface / implémentation", v: "Interface : ce qu’on peut faire. Implémentation : comment c’est réalisé en Python." },
    { r: "Pile", v: "LIFO : dernier entré, premier sorti. empiler, dépiler, est_vide, sommet." },
    { r: "File", v: "FIFO : premier entré, premier sorti. enfiler (à la queue), défiler (la tête), est_vide." },
    { r: "Liste (type abstrait)", v: "Vide, ou une tête suivie d’une queue (qui est une liste). Définition récursive." },
    { r: "Maillon", v: "Objet qui contient une valeur et une référence vers le maillon suivant (None à la fin)." },
    { r: "Coûts de la liste chaînée", v: "Ajout/suppression en tête : constant. Accès au i-ème, longueur, ajout en queue : linéaire." },
    { r: "Coûts de la list Python", v: "t[i], append, pop() : constant. insert(0, x), pop(0) : linéaire (décalages)." },
    { r: "Pile avec une list Python", v: "Sommet = fin : <code>append</code> pour empiler, <code>pop()</code> pour dépiler." },
    { r: "File avec deux piles", v: "Enfiler : empiler dans entree. Défiler : si sortie est vide, y verser entree ; puis dépiler sortie. Coût amorti constant." },
    { r: "File chaînée", v: "Deux références : tête (on défile) et queue (on enfile). Les deux opérations en temps constant." },
    { r: "Notation polonaise inverse", v: "Opérateur après les opérandes : <code>3 4 + 2 *</code> = (3 + 4) × 2. S’évalue avec une pile." },
    { r: "Exemples de piles", v: "Ctrl+Z, bouton Retour, pile d’appels, vérification de parenthèses." },
    { r: "Exemples de files", v: "File d’attente, impressions, ordonnancement des processus, parcours en largeur." }
  ]
});
