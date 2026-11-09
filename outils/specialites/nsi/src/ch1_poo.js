/* ===================== Chapitre 1 — Programmation orientée objet ===================== */
C("c1-dict", String.raw`
# Sans objet : un dictionnaire et des fonctions séparées
compte = {"titulaire": "Ada", "solde": 100}

def deposer(compte, montant):
    compte["solde"] = compte["solde"] + montant

deposer(compte, 50)
print(compte["solde"])
compte["sold"] = 0      # faute de frappe : aucune erreur, une clé de plus !
print(compte)`, { out: String.raw`
150
{'titulaire': 'Ada', 'solde': 150, 'sold': 0}` });

C("c1-deja", String.raw`
>>> type(3)
<class 'int'>
>>> type([1, 2])
<class 'list'>
>>> mots = ["pile", "file"]
>>> mots.append("liste")     # append est une méthode de l'objet mots
>>> mots
['pile', 'file', 'liste']
>>> "nsi".upper()            # upper est une méthode des chaînes
'NSI'`, { console: true });

C("c1-compte", String.raw`
class Compte:
    """Un compte bancaire très simplifié."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire      # attribut
        self.solde = solde              # attribut

    def deposer(self, montant):         # méthode
        self.solde = self.solde + montant

    def retirer(self, montant):         # méthode qui renvoie un booléen
        if montant > self.solde:
            return False
        self.solde = self.solde - montant
        return True`, { fichier: "compte.py", out: "" });

C("c1-usage", String.raw`
c1 = Compte("Ada", 100)      # instanciation : appelle __init__
c2 = Compte("Alan")          # solde vaut 0 par défaut
c1.deposer(50)
print(c1.solde, c2.solde)
print(c1.retirer(500))       # refusé : solde insuffisant
print(c1.retirer(30), c1.solde)
print(c1.titulaire, type(c1).__name__)`, { deps: ["c1-compte"], out: String.raw`
150 0
False
True 120
Ada Compte` });

C("c1-self", String.raw`
c = Compte("Grace", 10)
c.deposer(5)              # écriture habituelle
Compte.deposer(c, 5)      # ce que Python fait réellement : self = c
print(c.solde)`, { deps: ["c1-compte"], out: "20" });

C("c1-appel-methode", String.raw`
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
        self.historique = []            # liste des opérations

    def deposer(self, montant):
        self.solde = self.solde + montant
        self.historique.append(("dépôt", montant))

    def virer_vers(self, autre, montant):
        """Retire montant de ce compte et le dépose sur le compte autre."""
        if montant > self.solde:
            return False
        self.solde = self.solde - montant
        self.historique.append(("virement", -montant))
        autre.deposer(montant)          # une méthode appelle la méthode d'un autre objet
        return True

a = Compte("Ada", 100)
b = Compte("Alan")
a.virer_vers(b, 40)
print(a.solde, b.solde)
print(a.historique, b.historique)`, { out: String.raw`
60 40
[('virement', -40)] [('dépôt', 40)]` });

C("c1-acces", String.raw`
c = Compte("Ada", 100)
print(c.solde)        # lecture d'un attribut
c.solde = -1000       # écriture directe : Python ne l'interdit pas !
print(c.solde)`, { deps: ["c1-compte"], out: "100\n-1000" });

C("c1-accesseurs", String.raw`
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde          # le _ signale : « ne touche pas directement »

    def get_solde(self):             # accesseur (getter)
        return self._solde

    def deposer(self, montant):      # seule façon prévue de modifier _solde
        assert montant > 0, "le montant doit être positif"
        self._solde = self._solde + montant

    def __str__(self):               # appelée par print() et str()
        return "Compte de " + self.titulaire + " : " + str(self._solde) + " €"

c = Compte("Ada", 100)
c.deposer(20)
print(c.get_solde())
print(c)`, { out: "120\nCompte de Ada : 120 €" });

C("c1-alias", String.raw`
a = Compte("Ada", 100)
b = a                    # b désigne LE MÊME objet que a
b.deposer(50)
print(a.solde)           # a a « changé » aussi
c = Compte("Ada", 150)   # un autre objet, mêmes valeurs
print(a is b, a is c, a == c)`, { deps: ["c1-compte"], out: "150\nTrue False False" });

C("c1-fonction-objet", String.raw`
def frais_de_tenue(compte):
    """Prélève 2 € sur le compte : la fonction modifie l'objet reçu."""
    compte.solde = compte.solde - 2

c = Compte("Alan", 10)
frais_de_tenue(c)
frais_de_tenue(c)
print(c.solde)`, { deps: ["c1-compte"], out: "6" });

C("c1-banque", String.raw`
class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []              # un attribut qui contient des objets

    def ouvrir(self, titulaire, depot=0):
        c = Compte(titulaire, depot)
        self.comptes.append(c)
        return c

    def total(self):
        s = 0
        for c in self.comptes:
            s = s + c.solde
        return s

    def plus_riche(self):
        meilleur = self.comptes[0]
        for c in self.comptes:
            if c.solde > meilleur.solde:
                meilleur = c
        return meilleur.titulaire

b = Banque("Banque du Code")
b.ouvrir("Ada", 120)
b.ouvrir("Alan", 80)
g = b.ouvrir("Grace")
g.deposer(300)
print(len(b.comptes), b.total(), b.plus_riche())`, { deps: ["c1-compte"], out: "3 500 Grace" });

C("c1-maillon", String.raw`
class Maillon:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant          # un autre Maillon, ou None

m3 = Maillon("C")
m2 = Maillon("B", m3)
m1 = Maillon("A", m2)
print(m1.valeur, m1.suivant.valeur, m1.suivant.suivant.valeur)
print(m1.suivant.suivant.suivant)`, { out: "A B C\nNone" });

C("c1-speciales", String.raw`
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):          # v + w
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __eq__(self, autre):           # v == w
        return self.x == autre.x and self.y == autre.y

    def __str__(self):                 # print(v)
        return "(" + str(self.x) + ", " + str(self.y) + ")"

u = Vecteur(1, 2)
v = Vecteur(3, 4)
print(u + v)
print(u + v == Vecteur(4, 6), u is Vecteur(1, 2))`, { out: "(4, 6)\nTrue False" });

C("c1-attr-classe", String.raw`
class Ticket:
    nb_crees = 0                       # attribut de CLASSE, partagé par tous

    def __init__(self):
        Ticket.nb_crees = Ticket.nb_crees + 1
        self.numero = Ticket.nb_crees  # attribut d'INSTANCE, propre à chaque objet

t1 = Ticket()
t2 = Ticket()
print(t1.numero, t2.numero, Ticket.nb_crees)`, { out: "1 2 2" });

C("c1-heritage", String.raw`
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "..."

class Chat(Animal):                    # Chat hérite de Animal
    def parler(self):                  # et redéfinit parler
        return self.nom + " : miaou"

print(Chat("Pixel").parler(), Animal("Bit").parler())`, { out: "Pixel : miaou ..." });

/* pièges */
C("c1-p-self", String.raw`
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(montant):             # self oublié
        self.solde = self.solde + montant

Compte(10).deposer(5)`, { err: "TypeError: Compte.deposer() takes 1 positional argument but 2 were given" });

C("c1-p-pointself", String.raw`
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        solde = solde + montant       # « self. » oublié : variable locale

Compte(10).deposer(5)`, { err: "UnboundLocalError: cannot access local variable 'solde' where it is not associated with a value" });

C("c1-p-init", String.raw`
class Compte:
    def _init_(self, solde=0):        # un seul tiret bas de chaque côté
        self.solde = solde

c = Compte(10)`, { err: "TypeError: Compte() takes no arguments" });

C("c1-p-defaut", String.raw`
class Groupe:
    def __init__(self, nom, membres=[]):    # liste créée UNE fois, partagée !
        self.nom = nom
        self.membres = membres

g1 = Groupe("T1")
g2 = Groupe("T2")
g1.membres.append("Ada")
print(g2.membres)`, { out: "['Ada']" });

C("c1-p-defaut-ok", String.raw`
class Groupe:
    def __init__(self, nom, membres=None):
        self.nom = nom
        if membres is None:
            membres = []                     # une nouvelle liste à chaque objet
        self.membres = membres

g1 = Groupe("T1")
g2 = Groupe("T2")
g1.membres.append("Ada")
print(g2.membres)`, { out: "[]" });

C("c1-p-classe", String.raw`
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

print(Compte.solde)                   # la classe n'a pas d'attribut solde`, { err: "AttributeError: type object 'Compte' has no attribute 'solde'" });

/* prédis la sortie */
C("c1-x1", String.raw`
class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrementer(self):
        self.valeur = self.valeur + 1
        return self.valeur

a = Compteur()
b = Compteur()
a.incrementer()
a.incrementer()
print(b.incrementer(), a.valeur)`, { out: "1 2" });

C("c1-x2", String.raw`
class Boite:
    def __init__(self, contenu):
        self.contenu = contenu

b1 = Boite([1, 2])
b2 = b1
b2.contenu.append(3)
b3 = Boite([1, 2, 3])
print(b1.contenu, b1 is b2, b1 == b3)`, { out: "[1, 2, 3] True False" });

C("c1-x3", String.raw`
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def doubler(self):
        self.largeur = 2 * self.largeur
        return self.aire()

r = Rectangle(3, 4)
print(r.doubler(), r.aire(), r.largeur)`, { out: "24 24 6" });

C("c1-x4", String.raw`
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplace(self, dx):
        return Point(self.x + dx, self.y)

p = Point(0, 0)
q = p.deplace(5)
p.deplace(1)
print(p.x, q.x, p is q)`, { out: "0 5 False" });

/* épreuve pratique 1 */
C("c1-ep1-fourni", String.raw`
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

class Mediatheque:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        self.livres.append(livre)

    def emprunter(self, titre):
        """Rend le livre de ce titre indisponible et renvoie True,
        ou renvoie False s'il est absent ou déjà emprunté."""
        ...

    def nombre_disponibles(self):
        n = 0
        for livre in self.livres:
            if livre.disponible:
                n = n + 1
            return n

m = Mediatheque()
m.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
m.ajouter(Livre("Notre-Dame de Paris", "Victor Hugo", 1831))
m.ajouter(Livre("Le Rouge et le Noir", "Stendhal", 1830))`, { fichier: "mediatheque.py", run: false, trous: [18] });

C("c1-ep1-corr", String.raw`
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

class Mediatheque:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        self.livres.append(livre)

    def emprunter(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                return True
        return False

    def nombre_disponibles(self):
        n = 0
        for livre in self.livres:
            if livre.disponible:
                n = n + 1
        return n                      # return sorti de la boucle

    def titres_de(self, auteur):
        return [livre.titre for livre in self.livres if livre.auteur == auteur]

m = Mediatheque()
m.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
m.ajouter(Livre("Notre-Dame de Paris", "Victor Hugo", 1831))
m.ajouter(Livre("Le Rouge et le Noir", "Stendhal", 1830))

def test_mediatheque():
    vide = Mediatheque()
    assert vide.nombre_disponibles() == 0          # cas limite : aucun livre
    assert vide.emprunter("Les Misérables") is False
    assert m.nombre_disponibles() == 3
    assert m.emprunter("Les Misérables") is True
    assert m.emprunter("Les Misérables") is False   # déjà emprunté
    assert m.emprunter("Candide") is False          # titre absent
    assert m.nombre_disponibles() == 2
    assert m.titres_de("Victor Hugo") == ["Les Misérables", "Notre-Dame de Paris"]
    assert m.titres_de("Voltaire") == []

test_mediatheque()
print("tous les tests passent")`, { fichier: "mediatheque.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c1-ep2-fourni", String.raw`
class Duree:
    """Une durée stockée en secondes (entier positif ou nul)."""

    def __init__(self, heures, minutes, secondes):
        self.total = heures * 3600 + minutes * 60 + secondes

    def en_hms(self):
        """Renvoie le tuple (heures, minutes, secondes)."""
        h = self.total // 3600
        m = ...
        s = ...
        return (h, m, s)

    def ajouter(self, autre):
        """Renvoie une NOUVELLE Duree, somme de self et de autre."""
        self.total = self.total + autre.total
        return self`, { fichier: "duree.py", run: false, trous: [10, 11] });

C("c1-ep2-corr", String.raw`
class Duree:
    """Une durée stockée en secondes (entier positif ou nul)."""

    def __init__(self, heures, minutes, secondes):
        self.total = heures * 3600 + minutes * 60 + secondes

    def en_hms(self):
        h = self.total // 3600
        m = (self.total % 3600) // 60
        s = self.total % 60
        return (h, m, s)

    def ajouter(self, autre):
        return Duree(0, 0, self.total + autre.total)   # nouvel objet, self intact

    def est_plus_longue(self, autre):
        return self.total > autre.total

def test_duree():
    assert Duree(0, 0, 0).en_hms() == (0, 0, 0)
    assert Duree(1, 2, 3).en_hms() == (1, 2, 3)
    assert Duree(0, 0, 3725).en_hms() == (1, 2, 5)     # 3725 s = 1 h 2 min 5 s
    assert Duree(0, 59, 59).ajouter(Duree(0, 0, 1)).en_hms() == (1, 0, 0)
    a = Duree(0, 30, 0)
    b = a.ajouter(Duree(0, 45, 0))
    assert a.en_hms() == (0, 30, 0)                     # a n'a pas été modifiée
    assert b.en_hms() == (1, 15, 0)
    assert b.est_plus_longue(a) and not a.est_plus_longue(a)

test_duree()
print("tous les tests passent")`, { fichier: "duree.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c1-ecrit-code", String.raw`
class Vehicule:
    def __init__(self, immat, categorie):
        self.immat = immat              # chaîne, par exemple "AB-123-CD"
        self.categorie = categorie      # "voiture" ou "moto"

class Parking:
    def __init__(self, nb_places):
        self.places = [None] * nb_places    # None : place libre

    def nb_libres(self):
        n = 0
        for p in self.places:
            if p is None:
                n = n + 1
        return n`, { fichier: "parking.py", out: "" });

C("c1-ecrit-corr", String.raw`
class Parking:
    def __init__(self, nb_places):
        self.places = [None] * nb_places

    def nb_libres(self):
        n = 0
        for p in self.places:
            if p is None:
                n = n + 1
        return n

    def est_plein(self):
        return self.nb_libres() == 0

    def garer(self, vehicule):
        for i in range(len(self.places)):
            if self.places[i] is None:
                self.places[i] = vehicule
                return i
        return -1

    def sortir(self, immat):
        for i in range(len(self.places)):
            v = self.places[i]
            if v is not None and v.immat == immat:
                self.places[i] = None
                return True
        return False

    def nb_motos(self):
        return len([v for v in self.places if v is not None and v.categorie == "moto"])

p = Parking(3)
print(p.garer(Vehicule("AB-123-CD", "voiture")), p.garer(Vehicule("EF-456-GH", "moto")))
print(p.sortir("AB-123-CD"), p.sortir("ZZ-000-ZZ"), p.nb_libres())
print(p.garer(Vehicule("IJ-789-KL", "moto")), p.nb_motos(), p.est_plein())`, { deps: ["c1-ecrit-code"], out: "0 1\nTrue False 2\n0 2 False" });

C("c1-ecrit-q1", String.raw`
p = Parking(4)
v = Vehicule("AB-123-CD", "voiture")
p.places[2] = v
print(p.nb_libres(), p.places[2].categorie, p.places[0])`, { deps: ["c1-ecrit-code"], out: "3 voiture None" });

C("c1-retenir", String.raw`
class NomDeClasse:                       # CamelCase par convention
    def __init__(self, a, b=0):          # constructeur
        self.a = a                       # attributs d'instance
        self.b = b

    def methode(self, x):                # self toujours en 1er
        self.b = self.b + x              # modifier l'objet
        return self.a * x                # ou renvoyer une valeur

obj = NomDeClasse(3)                     # instanciation
print(obj.methode(2), obj.b)             # 6 2`, { out: "6 2" });

CH.push({
  id: "ch1", n: 1, court: "poo", fichier: "ch1_poo.py",
  titre: "Programmation orientée objet",
  rubrique: "Rubriques « Structures de données » (vocabulaire de la programmation objet) et « Langages et programmation » (paradigmes)",
  accroche: "Classes, objets, attributs, méthodes, self, références et alias : écrire ses propres types.",
  essentiel: [
    "Une <b>classe</b> est un plan (un moule) ; un <b>objet</b> est une <b>instance</b> fabriquée à partir de ce plan.",
    "Les <b>attributs</b> sont les données de l’objet ; les <b>méthodes</b> sont les fonctions qui agissent sur lui.",
    "Le constructeur <code>__init__</code> initialise les attributs ; <code>self</code> désigne l’objet sur lequel on travaille.",
    "<code>obj.methode(x)</code> revient à <code>Classe.methode(obj, x)</code> : <code>self</code> reçoit <code>obj</code>.",
    "Une variable contient une <b>référence</b> vers l’objet : <code>b = a</code> ne copie rien, <code>a</code> et <code>b</code> désignent le même objet."
  ],
  attendus: [
    "Écrire la définition d’une classe (constructeur, attributs, méthodes).",
    "Accéder aux attributs et aux méthodes d’une classe, depuis l’extérieur et depuis une autre méthode.",
    "Employer le vocabulaire juste : classe, objet (instance), attribut, méthode.",
    "Utiliser des classes pour implémenter une structure de données (chapitre 3 : maillon, pile, file).",
    "Hors programme selon le BO : « tous les aspects de la programmation objet comme le polymorphisme et l’héritage »."
  ],
  idees: [
    { id: "i1", t: "Pourquoi des objets ?", h: `
<p>Jusqu’ici, tu as représenté des données avec des types construits (listes, tuples, dictionnaires) et tu les as traitées avec des fonctions séparées. Ça marche, mais rien ne relie les données à leurs traitements, et rien n’empêche une incohérence :</p>
[[c1-dict]]
<p>La <b>programmation orientée objet</b> (POO) regroupe dans un même type les <b>données</b> (attributs) et les <b>traitements</b> (méthodes) qui leur sont propres. On fabrique ainsi ses propres types, avec une interface claire : « voilà ce qu’on peut faire avec un compte ».</p>
<p>En Python, tu utilises déjà des objets sans le savoir : un entier, une chaîne, une liste sont des objets, et <code>append</code> ou <code>upper</code> sont des méthodes.</p>
[[c1-deja]]
<div class="boite histoire"><div class="lab"># git log --histoire</div>
<p><span class="commit">1967 <b>·</b></span> Ole-Johan Dahl et Kristen Nygaard (Oslo) créent <b>Simula 67</b>, premier langage à classes et objets, pour des simulations.<br>
<span class="commit">années 1970 <b>·</b></span> Alan Kay et son équipe du Xerox PARC développent <b>Smalltalk</b> et popularisent l’expression « programmation orientée objet ».<br>
<span class="commit">1991 <b>·</b></span> Guido van Rossum publie <b>Python</b>, où toute valeur est un objet.</p></div>` },

    { id: "i2", t: "Classe et objet (instance)", h: `
<div class="boite def"><div class="lab">"""définitions"""</div>
<p>Une <b>classe</b> définit un nouveau type : elle décrit les attributs et les méthodes communs à tous ses objets.<br>
Un <b>objet</b>, ou <b>instance</b>, est une valeur de ce type, créée par <b>instanciation</b> : <code>Compte("Ada", 100)</code>.<br>
Un <b>attribut</b> est une variable attachée à un objet ; une <b>méthode</b> est une fonction définie dans la classe.</p></div>
<p>Exemple fil rouge : un compte bancaire. Par convention, le nom d’une classe commence par une majuscule (<code>Compte</code>, <code>ListeChainee</code>).</p>
[[c1-compte]]
[[c1-usage]]
<p>Chaque objet possède <b>ses propres</b> attributs : déposer sur <code>c1</code> ne change pas <code>c2</code>. Le schéma suivant montre ce qui se passe en mémoire, ligne par ligne.</p>
[[w-uml]]
<div class="boite ex"><div class="lab"># diagramme de classe (UML)</div><p>À l’écrit, une classe est souvent donnée sous la forme d’un rectangle en trois cases : le <b>nom</b>, les <b>attributs</b> (avec leur type), les <b>méthodes</b> (avec leurs paramètres, sans <code>self</code>). C’est une notation de l’UML (<i>Unified Modeling Language</i>) ; il suffit de savoir la lire et la traduire en Python.</p></div>` },

    { id: "i3", t: "Le constructeur __init__ et self", h: `
<p>Quand tu écris <code>c1 = Compte("Ada", 100)</code>, Python :</p>
<ol><li>crée un objet vide de type <code>Compte</code> ;</li><li>appelle <code>__init__(objet, "Ada", 100)</code> : le paramètre <code>self</code> reçoit le nouvel objet ;</li><li>renvoie l’objet, dont la référence est rangée dans <code>c1</code>.</li></ol>
<p>La méthode <code>__init__</code> s’appelle le <b>constructeur</b> (plus exactement l’initialiseur). Son rôle est de créer les attributs avec <code>self.nom = valeur</code>. Elle ne renvoie rien.</p>
<div class="boite retenir-b"><div class="lab"># à retenir</div><p><code>self</code> est le premier paramètre de toute méthode : c’est l’objet sur lequel la méthode travaille. Dans la classe, on écrit <code>self.solde</code> ; à l’extérieur, on écrit <code>c1.solde</code>. Le mot <code>self</code> n’est qu’une convention, mais tout le monde la respecte.</p></div>
<p>Les paramètres peuvent avoir une <b>valeur par défaut</b> (<code>solde=0</code>), comme pour toute fonction. Attention aux valeurs par défaut <b>mutables</b> (une liste) : voir les pièges.</p>` },

    { id: "i4", t: "Les méthodes : agir sur l’objet", h: `
<p>Une méthode est une fonction écrite dans la classe, dont le premier paramètre est <code>self</code>. L’appel <code>c.deposer(5)</code> est un raccourci pour <code>Compte.deposer(c, 5)</code> :</p>
[[c1-self]]
<p>Une méthode peut <b>modifier</b> l’objet (<code>deposer</code>), <b>renvoyer</b> une valeur calculée à partir des attributs (<code>retirer</code> renvoie un booléen), ou les deux. Elle peut aussi appeler une autre méthode du même objet (<code>self.autre_methode()</code>) ou d’un autre objet reçu en paramètre :</p>
[[c1-appel-methode]]
<p>Ici, un attribut <code>historique</code> contient une liste : un objet peut contenir n’importe quelle valeur, y compris d’autres objets.</p>` },

    { id: "i5", t: "Accéder aux attributs, les protéger, afficher un objet", h: `
<p>On lit et on écrit un attribut avec la notation pointée <code>objet.attribut</code>. Python n’empêche pas d’écrire n’importe quoi :</p>
[[c1-acces]]
<p>Pour garder l’objet cohérent, on passe plutôt par des méthodes. Une méthode qui renvoie un attribut s’appelle un <b>accesseur</b> (<i>getter</i>) ; une méthode qui le modifie en vérifiant la valeur, un <b>mutateur</b> (<i>setter</i>). Un attribut dont le nom commence par <code>_</code> est « privé par convention » : Python ne bloque rien, c’est un avertissement entre programmeurs.</p>
[[c1-accesseurs]]
<p>Sans méthode <code>__str__</code>, <code>print(c)</code> affiche seulement quelque chose comme <code>&lt;__main__.Compte object at 0x7f…&gt;</code> (une adresse qui change à chaque exécution). Avec <code>__str__</code>, tu choisis le texte affiché ; elle doit <b>renvoyer</b> une chaîne, pas l’afficher.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>L’<b>encapsulation</b> (cacher l’implémentation derrière une interface de méthodes) est une idée centrale de la POO, mais le programme de Terminale n’exige que le vocabulaire et l’usage des accesseurs que l’énoncé te donne.</p></div>` },

    { id: "i6", t: "Références et alias : la mutation partagée", h: `
<p>Une variable ne « contient » pas un objet : elle contient une <b>référence</b> (l’adresse de l’objet en mémoire). L’affectation <code>b = a</code> copie la référence, pas l’objet. On dit que <code>b</code> est un <b>alias</b> de <code>a</code> :</p>
[[c1-alias]]
<ul><li><code>a is b</code> teste si les deux noms désignent <b>le même objet</b> ;</li>
<li><code>a == c</code> compare deux objets ; pour une classe qui ne définit pas <code>__eq__</code>, <code>==</code> se comporte comme <code>is</code>, d’où <code>False</code> alors que les attributs sont égaux.</li></ul>
<p>Même chose quand on passe un objet à une fonction : la fonction reçoit une référence vers <b>le même</b> objet et peut le modifier. C’est un <b>effet de bord</b>, voulu ici, mais source de bugs quand il ne l’est pas (chapitre 4).</p>
[[c1-fonction-objet]]
<div class="boite ex"><div class="lab"># vérifie tes réponses</div><p>Pour voir les références, colle ces programmes dans <a href="https://pythontutor.com/" target="_blank" rel="noopener">Python Tutor</a> : il dessine les variables et les flèches vers les objets.</p></div>` },

    { id: "i7", t: "Des objets qui contiennent des objets", h: `
<p>Un attribut peut contenir une liste d’objets : c’est la <b>composition</b>. Une banque possède des comptes, une médiathèque des livres, une partie des joueurs.</p>
[[c1-banque]]
<p>Un attribut peut aussi contenir <b>un</b> autre objet de la même classe. C’est l’idée du <b>maillon</b> d’une liste chaînée : chaque maillon connaît sa valeur et le maillon suivant. Tu la retrouveras au chapitre 3.</p>
[[c1-maillon]]
<p>La programmation objet sert ainsi à <b>implémenter des structures de données</b> : pile, file, arbre, graphe. C’est pour cela qu’elle est rangée dans la rubrique « Structures de données » du programme.</p>` },

    { id: "i8", t: "Méthodes spéciales et attributs de classe", h: `
<div class="boite hp"><div class="lab"># pour aller plus loin — non exigible, mais fréquent dans les sujets</div>
<p>Les méthodes dont le nom est entouré de deux tirets bas sont appelées par Python dans des situations précises : <code>__init__</code> à la création, <code>__str__</code> par <code>print</code>, <code>__eq__</code> par <code>==</code>, <code>__add__</code> par <code>+</code>, <code>__len__</code> par <code>len()</code>, <code>__lt__</code> par <code>&lt;</code>.</p></div>
[[c1-speciales]]
<p>Un attribut défini directement dans la classe (hors de toute méthode) est un <b>attribut de classe</b> : il est partagé par tous les objets. À ne pas confondre avec les attributs d’instance créés par <code>self.x = …</code>.</p>
[[c1-attr-classe]]` },

    { id: "i9", t: "Ce qui est hors programme : héritage et polymorphisme", h: `
<p>Le programme précise : « On n’aborde pas ici tous les aspects de la programmation objet comme le polymorphisme et l’héritage. » Tu peux les croiser, il faut savoir les reconnaître, pas les maîtriser.</p>
<div class="boite hp"><div class="lab"># hors programme</div>
<p>L’<b>héritage</b> permet de définir une classe à partir d’une autre (<code>class Chat(Animal)</code>) : elle récupère ses attributs et méthodes et peut en redéfinir. Le <b>polymorphisme</b> : un même appel (<code>x.parler()</code>, ou <code>len(x)</code>) produit un comportement adapté au type de <code>x</code>.</p></div>
[[c1-heritage]]
<p>La POO est l’un des trois <b>paradigmes</b> au programme, avec l’impératif et le fonctionnel (chapitre « Paradigmes de programmation », bientôt). Un même programme peut mélanger les paradigmes.</p>` }
  ],
  pieges: [
    { t: "Oublier self dans la définition d’une méthode", h: `[[c1-p-self]]<p>Python passe toujours l’objet comme premier argument : la méthode reçoit 2 arguments (l’objet et 5) alors qu’elle n’en attend qu’un.</p>` },
    { t: "Oublier « self. » devant un attribut", h: `[[c1-p-pointself]]<p>Sans <code>self.</code>, <code>solde</code> est une variable locale de la méthode, qui n’existe pas encore. Il faut écrire <code>self.solde = self.solde + montant</code>.</p>` },
    { t: "Mal écrire __init__", h: `[[c1-p-init]]<p>Deux tirets bas avant et deux après : <code>__init__</code>. Sinon, Python ne trouve pas de constructeur et refuse les arguments.</p>` },
    { t: "Une liste comme valeur par défaut", h: `[[c1-p-defaut]]<p>La valeur par défaut est évaluée <b>une seule fois</b>, à la définition : tous les objets créés sans argument partagent la même liste. La correction classique utilise <code>None</code> :</p>[[c1-p-defaut-ok]]` },
    { t: "Confondre la classe et l’objet", h: `[[c1-p-classe]]<p><code>solde</code> est un attribut d’<b>instance</b> : il n’existe qu’une fois l’objet créé. On écrit <code>c = Compte(10)</code> puis <code>c.solde</code>.</p>` },
    { t: "Croire que b = a copie l’objet", h: `<p><code>b = a</code> crée un alias : toute modification faite par <code>b</code> se voit par <code>a</code>. Pour une copie, on construit un nouvel objet : <code>b = Compte(a.titulaire, a.solde)</code>.</p>` },
    { t: "Oublier les parenthèses d’un appel de méthode", h: `<p><code>c.get_solde</code> sans parenthèses ne calcule rien : c’est la méthode elle-même (Python affiche <code>&lt;bound method …&gt;</code>). Il faut <code>c.get_solde()</code>. Une comparaison <code>c.get_solde &gt; 0</code> lève même une <code>TypeError</code>.</p>` }
  ],
  retenir: `
<h2>Vocabulaire</h2>
<div class="tab-wrap"><table><tr><th>mot</th><th>sens</th><th>en Python</th></tr>
<tr><td>classe</td><td>plan d’un nouveau type</td><td><code>class Compte:</code></td></tr>
<tr><td>objet, instance</td><td>valeur fabriquée à partir de la classe</td><td><code>c = Compte("Ada", 100)</code></td></tr>
<tr><td>attribut</td><td>donnée propre à l’objet</td><td><code>self.solde</code> / <code>c.solde</code></td></tr>
<tr><td>méthode</td><td>fonction de la classe, 1er paramètre <code>self</code></td><td><code>def deposer(self, m):</code> / <code>c.deposer(5)</code></td></tr>
<tr><td>constructeur</td><td>initialise les attributs</td><td><code>def __init__(self, …):</code></td></tr>
<tr><td>self</td><td>l’objet sur lequel la méthode travaille</td><td><code>c.deposer(5)</code> ≡ <code>Compte.deposer(c, 5)</code></td></tr>
<tr><td>accesseur / mutateur</td><td>méthode qui lit / modifie un attribut</td><td><code>get_solde()</code>, <code>deposer()</code></td></tr>
<tr><td>alias</td><td>deux noms pour le même objet</td><td><code>b = a</code> ; <code>a is b</code> → True</td></tr></table></div>
<h2>Squelette à connaître par cœur</h2>
[[c1-retenir]]
<h2>Les réflexes</h2>
<ul><li>Chaque méthode commence par <code>self</code> ; chaque attribut s’écrit <code>self.x</code> dans la classe.</li>
<li><code>__init__</code> crée les attributs, ne renvoie rien.</li>
<li>Une méthode qui doit donner un résultat le <b>renvoie</b> (<code>return</code>) ; <code>__str__</code> renvoie une chaîne.</li>
<li><code>b = a</code> : même objet. <code>is</code> teste l’identité, <code>==</code> l’égalité (qui, sans <code>__eq__</code>, est l’identité).</li>
<li>Jamais de liste comme valeur par défaut : <code>=None</code> puis <code>[]</code> dans le corps.</li>
<li>Héritage et polymorphisme : hors programme.</li></ul>`,
  predis: [
    { code: "c1-x1", niv: "facile", rep: "Chaque objet a son propre attribut <code>valeur</code>. <code>a</code> a été incrémenté deux fois (valeur 2) ; l’appel <code>b.incrementer()</code> fait passer <code>b.valeur</code> de 0 à 1 et renvoie 1." },
    { code: "c1-x2", niv: "moyen", rep: "<code>b2 = b1</code> crée un alias : on ajoute 3 à la liste du seul objet existant, donc <code>b1.contenu</code> vaut <code>[1, 2, 3]</code> et <code>b1 is b2</code> est vrai. <code>b3</code> est un autre objet ; sans <code>__eq__</code>, <code>==</code> compare les identités : False, même si les contenus sont égaux." },
    { code: "c1-x3", niv: "moyen", rep: "<code>doubler</code> modifie l’attribut (largeur 6) puis renvoie l’aire calculée avec la nouvelle largeur : 6 × 4 = 24. Le second <code>aire()</code> donne aussi 24." },
    { code: "c1-x4", niv: "moyen", rep: "<code>deplace</code> ne modifie pas <code>p</code> : elle <b>renvoie un nouvel objet</b>. <code>q</code> est ce nouvel objet (x = 5) ; le second appel crée un objet qui est perdu (non affecté). <code>p.x</code> reste 0 et <code>p is q</code> est faux." }
  ],
  ep: [
    { titre: "Médiathèque", enonce: `<p>On gère les livres d’une médiathèque. Le fichier fourni contient deux classes et une méthode à compléter. La méthode <code>nombre_disponibles</code> est déjà écrite… mais elle contient une erreur.</p>[[c1-ep1-fourni]]`,
      questions: [
        { q: "Compléter la méthode <code>emprunter</code> en respectant sa documentation.", c: `<p>On parcourt les livres ; dès qu’on trouve le bon titre <b>et</b> que le livre est disponible, on le marque emprunté et on renvoie True. Si la boucle se termine sans succès, on renvoie False (le <code>return False</code> est <b>après</b> la boucle).</p>` },
        { q: "Écrire une fonction <code>test_mediatheque()</code> qui teste <code>emprunter</code> et <code>nombre_disponibles</code>, y compris les cas limites.", c: `<p>Cas à couvrir : médiathèque vide, emprunt réussi, double emprunt du même livre, titre absent. Tests rassemblés dans le corrigé complet ci-dessous.</p>` },
        { q: "Exécuter <code>m.nombre_disponibles()</code>. Le résultat est-il correct ? Corriger.", c: `<p>La fonction renvoie 1 au lieu de 3 : le <code>return n</code> est indenté <b>dans</b> la boucle, donc la fonction s’arrête après le premier livre. Il faut le désindenter d’un niveau.</p>` },
        { q: "Ajouter une méthode <code>titres_de(auteur)</code> qui renvoie la liste des titres d’un auteur (dans l’ordre d’ajout).", c: `[[c1-ep1-corr]]` },
        { q: "À l’oral : que représente <code>self</code> dans <code>emprunter</code> ? Quel est le type de <code>livre</code> dans la boucle ?", c: `<p><code>self</code> est l’objet <code>Mediatheque</code> sur lequel on appelle la méthode (ici <code>m</code>). <code>livre</code> est un objet de la classe <code>Livre</code> : on accède à ses attributs par <code>livre.titre</code>, <code>livre.disponible</code>.</p>` }
      ] },
    { titre: "Durées", enonce: `<p>Une durée est stockée par un seul attribut : son nombre total de secondes. Deux lignes sont à compléter et la méthode <code>ajouter</code> ne respecte pas sa documentation.</p>[[c1-ep2-fourni]]`,
      questions: [
        { q: "Compléter <code>en_hms</code> (lignes 10 et 11).", c: `<p>Après avoir retiré les heures, il reste <code>self.total % 3600</code> secondes ; les minutes en sont le quotient par 60. Les secondes sont le reste de la division par 60 : <code>m = (self.total % 3600) // 60</code> et <code>s = self.total % 60</code>.</p>` },
        { q: "Pourquoi la méthode <code>ajouter</code> ne respecte-t-elle pas sa documentation ? Écrire un test qui le montre, puis corriger.", c: `<p>Elle modifie <code>self</code> (effet de bord) et renvoie <code>self</code> au lieu d’un <b>nouvel</b> objet. Test révélateur : après <code>b = a.ajouter(Duree(0, 45, 0))</code>, <code>a</code> ne doit pas avoir changé. Correction : <code>return Duree(0, 0, self.total + autre.total)</code>.</p>` },
        { q: "Écrire une méthode <code>est_plus_longue(autre)</code> et un jeu de tests complet.", c: `[[c1-ep2-corr]]` },
        { q: "À l’oral : quelle est la différence entre <code>/</code> et <code>//</code> ? Pourquoi utiliser <code>%</code> ici ?", c: `<p><code>/</code> donne un flottant (3725 / 3600 = 1.034…) ; <code>//</code> donne le quotient entier (1). <code>%</code> donne le reste de la division euclidienne : c’est ce qui « reste » une fois les heures (ou les minutes) retirées.</p>` }
      ] }
  ],
  ecrit: { titre: "Un parking (programmation objet)", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite (questions progressives, code à écrire sur la copie).",
    enonce: `<p>Un parking possède un nombre fixe de places, numérotées à partir de 0. On utilise les classes suivantes.</p>[[c1-ecrit-code]]`,
    questions: [
      { q: "On exécute le code ci-dessous. Qu’affiche-t-il ? Justifier.", pts: "0,5 pt", code: "[[c1-ecrit-q1|nosortie]]", c: `<p>Affichage : <code>3 voiture None</code>. Une place sur 4 est occupée ; <code>p.places[2]</code> est l’objet <code>v</code>, dont l’attribut <code>categorie</code> vaut <code>"voiture"</code> ; la place 0 est libre et vaut <code>None</code>.</p>` },
      { q: "Dessiner le diagramme de la classe <code>Parking</code> (nom, attributs, méthodes).", pts: "0,5 pt", c: `<p>Trois cases : <code>Parking</code> / <code>places : list</code> / <code>__init__(nb_places)</code>, <code>nb_libres() : int</code> (et les méthodes ajoutées aux questions suivantes).</p>` },
      { q: "Écrire la méthode <code>est_plein(self)</code> qui renvoie True si aucune place n’est libre. On utilisera <code>nb_libres</code>.", pts: "1 pt", c: `<p><code>return self.nb_libres() == 0</code> : appel d’une méthode du même objet par <code>self.</code>. Pas besoin de <code>if … return True else return False</code> : la comparaison est déjà un booléen.</p>` },
      { q: "Écrire la méthode <code>garer(self, vehicule)</code> qui place le véhicule sur la première place libre et renvoie son numéro, ou renvoie −1 si le parking est plein.", pts: "1,5 pt", c: `<p>Parcours par indice (on a besoin du numéro de place) ; on renvoie dès qu’on a garé. Le <code>return -1</code> est après la boucle.</p>` },
      { q: "Écrire la méthode <code>sortir(self, immat)</code> qui libère la place du véhicule dont l’immatriculation est <code>immat</code> et renvoie True, ou renvoie False s’il n’est pas dans le parking.", pts: "1,5 pt", c: `<p>Piège : une place libre vaut <code>None</code>, et <code>None.immat</code> lève une <code>AttributeError</code>. Il faut tester <code>v is not None</code> <b>avant</b> <code>v.immat</code> (le <code>and</code> s’arrête au premier faux).</p>[[c1-ecrit-corr]]` },
      { q: `On écrit <code>v = Vehicule("AB-123-CD", "voiture")</code>, puis <code>p.garer(v)</code>, puis <code>v.categorie = "moto"</code>. Le véhicule garé est-il modifié ? Expliquer.`, pts: "1 pt", c: `<p>Oui. La liste <code>p.places</code> contient une <b>référence</b> vers l’objet <code>v</code>, pas une copie : modifier l’objet par <code>v</code> modifie le véhicule garé (mutation partagée).</p>` }
    ],
    methode: `<p>À l’écrit : recopie la signature (<code>def garer(self, vehicule):</code>), indente proprement, n’oublie ni <code>self</code> ni <code>self.</code> devant les attributs, et place le <code>return</code> « échec » après la boucle. Quand une méthode existe déjà (<code>nb_libres</code>), l’énoncé attend que tu la réutilises.</p>` },
  qcm: [
    { q: "Dans <code>c = Compte(\"Ada\", 100)</code>, que désigne <code>c</code> ?", c: ["La classe Compte", "Un objet (une instance) de la classe Compte", "Une méthode", "Le constructeur"], a: 1, e: "<code>Compte(…)</code> crée une instance ; <code>c</code> contient une référence vers cet objet.", ref: "i2" },
    { q: "Quel est le rôle de la méthode <code>__init__</code> ?", c: ["Afficher l’objet", "Initialiser les attributs d’un objet qui vient d’être créé", "Supprimer l’objet", "Comparer deux objets"], a: 1, e: "Elle est appelée automatiquement à l’instanciation et crée les attributs avec <code>self.x = …</code>.", ref: "i3" },
    { q: "Dans une méthode, <code>self</code> désigne…", c: ["la classe", "le module", "l’objet sur lequel la méthode est appelée", "le premier attribut"], a: 2, e: "<code>c.deposer(5)</code> revient à <code>Compte.deposer(c, 5)</code> : <code>self</code> vaut <code>c</code>.", ref: "i4" },
    { q: "Quelle écriture est équivalente à <code>c.deposer(5)</code> ?", c: ["<code>deposer(c, 5)</code>", "<code>Compte.deposer(c, 5)</code>", "<code>Compte.deposer(5)</code>", "<code>c.deposer(c, 5)</code>"], a: 1, e: "La méthode est une fonction de la classe ; l’objet est passé comme premier argument.", ref: "i4" },
    { q: "On exécute <code>a = Compte(\"Ada\", 10)</code> puis <code>b = a</code> puis <code>b.deposer(5)</code>. Que vaut <code>a.solde</code> ?", c: ["10", "15", "5", "Une erreur est levée"], a: 1, e: "<code>b</code> est un alias : un seul objet existe, il a été modifié.", ref: "i6" },
    { q: "Pour une classe qui ne définit pas <code>__eq__</code>, <code>Compte(\"Ada\", 10) == Compte(\"Ada\", 10)</code> vaut…", c: ["True", "False", "None", "Une erreur"], a: 1, e: "Sans <code>__eq__</code>, <code>==</code> compare les identités : ce sont deux objets distincts.", ref: "i6" },
    { q: "Quelle définition de méthode est correcte ?", c: ["<code>def retirer(montant):</code>", "<code>def retirer(self, montant):</code>", "<code>def self.retirer(montant):</code>", "<code>def retirer(montant, self):</code>"], a: 1, e: "<code>self</code> est toujours le premier paramètre.", ref: "i4" },
    { q: "Dans une méthode, l’instruction <code>solde = solde + 10</code> (au lieu de <code>self.solde = …</code>) provoque…", c: ["une modification de l’attribut", "une UnboundLocalError : solde est une variable locale non définie", "rien du tout", "une SyntaxError"], a: 1, e: "Sans <code>self.</code>, Python crée une variable locale qu’on lit avant de l’avoir définie.", ref: "i3" },
    { q: "Que fait <code>print(obj)</code> si la classe définit <code>__str__</code> ?", c: ["Affiche l’adresse mémoire", "Affiche la chaîne renvoyée par <code>__str__</code>", "Lève une erreur", "Affiche tous les attributs"], a: 1, e: "<code>print</code> appelle <code>str(obj)</code>, donc <code>__str__</code>, qui doit renvoyer une chaîne.", ref: "i5" },
    { q: "Selon le programme de Terminale, quelle notion n’est pas exigible ?", c: ["Les attributs", "Les méthodes", "L’héritage", "L’instanciation"], a: 2, e: "Le BO exclut explicitement le polymorphisme et l’héritage.", ref: "i9" },
    { q: "Pourquoi éviter <code>def __init__(self, membres=[])</code> ?", c: ["C’est une erreur de syntaxe", "La même liste est partagée par tous les objets créés sans argument", "Les listes sont interdites comme attributs", "Cela rend l’objet immuable"], a: 1, e: "La valeur par défaut est créée une seule fois, à la définition de la fonction.", ref: "i3" },
    { q: "Un objet <code>Maillon</code> possède un attribut <code>suivant</code> qui contient un autre <code>Maillon</code> ou <code>None</code>. Cette idée sert à construire…", c: ["un dictionnaire", "une liste chaînée", "un tableau", "un module"], a: 1, e: "Chaque maillon référence le suivant : c’est le principe de la liste chaînée (chapitre 3).", ref: "i7" },
    { q: "Une fonction reçoit un objet en paramètre et modifie l’un de ses attributs. Après l’appel…", c: ["l’objet d’origine est modifié", "seule une copie a été modifiée", "Python lève une erreur", "l’attribut revient à sa valeur initiale"], a: 0, e: "La fonction reçoit une référence vers le même objet : c’est un effet de bord.", ref: "i6" }
  ],
  cartes: [
    { r: "Classe", v: "Plan d’un nouveau type : décrit les attributs et les méthodes communs à ses objets. <code>class Compte:</code>" },
    { r: "Objet / instance", v: "Valeur créée à partir d’une classe par instanciation : <code>c = Compte(\"Ada\", 100)</code>." },
    { r: "Attribut", v: "Donnée propre à un objet : <code>self.solde</code> dans la classe, <code>c.solde</code> à l’extérieur." },
    { r: "Méthode", v: "Fonction définie dans la classe, dont le premier paramètre est <code>self</code>." },
    { r: "__init__", v: "Constructeur (initialiseur) : appelé automatiquement à la création, il crée les attributs. Ne renvoie rien." },
    { r: "self", v: "L’objet sur lequel la méthode travaille. <code>c.f(x)</code> ≡ <code>Classe.f(c, x)</code>." },
    { r: "Accesseur / mutateur", v: "Méthode qui renvoie un attribut (<i>getter</i>) / qui le modifie en contrôlant la valeur (<i>setter</i>)." },
    { r: "Alias", v: "Deux noms pour le même objet après <code>b = a</code>. Modifier par l’un se voit par l’autre." },
    { r: "is ou == ?", v: "<code>is</code> : même objet. <code>==</code> : égalité, définie par <code>__eq__</code> (sinon identique à <code>is</code>)." },
    { r: "__str__", v: "Méthode appelée par <code>print(obj)</code> et <code>str(obj)</code> ; doit <b>renvoyer</b> une chaîne." },
    { r: "Attribut de classe", v: "Défini dans la classe hors des méthodes ; partagé par toutes les instances (ex. compteur d’objets créés)." },
    { r: "Hors programme en POO", v: "Héritage et polymorphisme (le BO le précise)." },
    { r: "Diagramme de classe UML", v: "Rectangle en 3 cases : nom de la classe / attributs (avec types) / méthodes (paramètres sans self)." },
    { r: "Simula 67", v: "Premier langage à classes et objets (Dahl et Nygaard, Norvège, 1967)." }
  ]
});
