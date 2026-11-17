"""NSI, chapitre 1 : « Programmation orientée objet » — le cours en vidéo (site « import bac »), vidéo pilote de la NSI.

Chaîne des vidéos des spécialités : outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots ; moteur
nsi/serie/moteur.js (identité « flux de données » : nuit lumineuse, grille en perspective, panneaux de verre) ; type code
(éditeur et terminal : lignes tapées aux repères {id.k}, ligne active {id.lk}, sortie {id.s} ou {id.sk}, erreur {id.e}) ;
illustrations propres à la vidéo dans nsi/serie/illu-nsi-ch1.js (memoire : variables, objets et références ; moule : la
classe et ses instances ; uml : le diagramme de classe).
Contenu : le chapitre 1 du site (outils/specialites/nsi/src/ch1_poo.js), rien au-delà ; ce qui dépasse le programme est
dit « pour aller plus loin » ou « hors programme ». Les programmes affichés sont ceux du site, parfois abrégés (commentaires
raccourcis, méthodes inutiles au propos retirées, une ligne trop longue coupée entre parenthèses) ; chaque sortie annoncée
est vérifiée en exécutant le programme : outils/serie-nsi/verif_ch1.py.
Le texte lu ne contient pas de code : il le dit avec des mots (« self point solde ») ; l'écran montre le code.
Usage : python3 outils/serie-philo/verifier.py nsi_ch1
        python3 outils/serie-nsi/verif_ch1.py
        SERIE_MOTEUR=muet PYTHONPATH=outils/serie-nsi python3 outils/serie-philo/generer.py nsi_ch1   (brouillon sans voix)
        python3 outils/serie-philo/chevauchements.py nsi-ch1

POINTS À FAIRE VÉRIFIER (contrôle indépendant avant la voix) :
- prononciation des mots anglais et des noms de code (dictionnaire PRONONCIATION ci-dessous : self, print, append, None,
  True, False, getter, setter, TypeError…) : à écouter sur un premier essai de voix ; « self » est laissé tel quel ;
- l'histoire : Smalltalk est daté « années soixante-dix » comme sur le site (pas d'année précise) ; Simula 67 (1967,
  Dahl et Nygaard, Oslo) et Python (1991, Guido van Rossum) comme sur le site ;
- le diagramme UML du Compte (types « str », « int », « bool ») est une proposition de la vidéo : le site décrit la
  notation sans donner ce diagramme ;
- l'exercice 2 reprend l'exercice d'écrit du site (le parking) sans sa question 2 (le diagramme de classe), et la
  question 6 du site devient la question 5 ;
- les messages d'erreur affichés sont ceux de Python 3.11 et suivants (UnboundLocalError en particulier) ;
- la valeur d'une liste dans un attribut est dessinée dans la case de l'objet (simplification : en mémoire, la liste est
  elle-même un objet référencé), exercice 1.
"""

SITE = "nsi"
CODE = "nsi-ch1"
NOTION = "Programmation orientée objet"
NUM = 1
TITRE = "Programmation orientée objet"
SUIVANT = "Chapitre 2 · Récursivité"
RYTHME = "vivant"
# graphies données à la voix seulement (sous-titres et écran gardent l'orthographe normale) : mots anglais du code et
# noms des exemples ; « c1 », « c2 »… sont dits « c un », « c deux »
PRONONCIATION = {
    "print": "printe", "append": "appennde", "upper": "eupeur", "None": "nonne", "True": "trou", "False": "folse",
    "getter": "guétteur", "setter": "sétteur", "get solde": "guette solde", "TypeError": "taïpe érreur",
    "UnboundLocalError": "eunbaounde lôcal érreur", "AttributeError": "attribioute érreur", "is": "iz",
    "Alan": "Alanne", "Grace": "Gréïce", "Smalltalk": "smôltôk", "Xerox": "Zirox", "PARC": "parc",
    "Guido van Rossum": "Guido vanne Rossoum", "Ole-Johan Dahl": "Olé Yohanne Dal", "Kristen Nygaard": "Kristène Nugor",
    "Simula": "Simula", "UML": "U M L", "POO": "P O O", "c1": "c un", "c2": "c deux", "m1": "m un", "m2": "m deux",
    "m3": "m trois", "b1": "b un", "b2": "b deux", "b3": "b trois", "t1": "t un", "t2": "t deux",
    "init": "inite", "str": "esse té erre", "eq": "é cu", "add": "adde", "len": "lène", "lt": "elle té",
    "less than": "lesse zanne",
    "Init": "Inite", "Str": "Esse té erre", "Eq": "É cu", "Add": "Adde", "Len": "Lène", "Print": "Printe", "Append": "Appennde",
    "Get solde": "Guette solde", "Nb créés": "Nombre créés", "nb créés": "nombre créés", "assert": "assèrte", "Pixel": "Pixèle",
}
LIAISONS = "maths"   # jamais de liaison devant une lettre ou un nombre (« deux‿a », « les‿objets c un »…)


def L(s):
    """Lignes d'un programme écrit dans une chaîne (la première ligne vide est ignorée)."""
    return s.strip("\n").split("\n")


# ------------------------------------------------------------------ les programmes affichés (vérifiés par verif_ch1.py)
O_DICT = L('''
compte = {"titulaire": "Ada", "solde": 100}

def deposer(compte, montant):
    compte["solde"] = compte["solde"] + montant

deposer(compte, 50)
print(compte["solde"])
compte["sold"] = 0      # faute de frappe : aucune erreur !
print(compte)
''')
DEJA = L('''
>>> type(3)
<class 'int'>
>>> type([1, 2])
<class 'list'>
>>> mots = ["pile", "file"]
>>> mots.append("liste")
>>> mots
['pile', 'file', 'liste']
>>> "nsi".upper()
'NSI'
''')
COMPTE = L('''
class Compte:
    """Un compte bancaire très simplifié."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if montant > self.solde:
            return False
        self.solde = self.solde - montant
        return True
''')
INI = L('''
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

c1 = Compte("Ada", 100)
''')
USAGE = L('''
c1 = Compte("Ada", 100)
c2 = Compte("Alan")
c1.deposer(50)
print(c1.solde, c2.solde)
print(c1.retirer(500))
print(c1.retirer(30), c1.solde)
print(c1.titulaire, type(c1).__name__)
''')
SELF = L('''
c = Compte("Grace", 10)
c.deposer(5)            # l'écriture habituelle
Compte.deposer(c, 5)    # ce que fait Python : self = c
print(c.solde)
''')
TRACE = L('''
class Compte:
    ...
    def deposer(self, montant):
        self.solde = self.solde + montant

a = Compte("Ada", 100)
b = Compte("Alan")
a.deposer(50)
b.deposer(20)
''')
VIR = L('''
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
        self.historique = []

    def deposer(self, montant):
        self.solde = self.solde + montant
        self.historique.append(("dépôt", montant))

    def virer_vers(self, autre, montant):
        if montant > self.solde:
            return False
        self.solde = self.solde - montant
        self.historique.append(("virement", -montant))
        autre.deposer(montant)
        return True
''')
VIR_U = L('''
a = Compte("Ada", 100)
b = Compte("Alan")
a.virer_vers(b, 40)
print(a.solde, b.solde)
print(a.historique, b.historique)
''')
ACCES = L('''
c = Compte("Ada", 100)
print(c.solde)
c.solde = -1000       # Python ne l'interdit pas !
print(c.solde)
''')
GS = L('''
class Compte:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde

    def get_solde(self):
        return self._solde

    def deposer(self, montant):
        assert montant > 0, "le montant doit être positif"
        self._solde = self._solde + montant

    def __str__(self):
        return ("Compte de " + self.titulaire
                + " : " + str(self._solde) + " €")
''')
GS_U = L('''
c = Compte("Ada", 100)
c.deposer(20)
print(c.get_solde())
print(c)
''')
ALIAS = L('''
a = Compte("Ada", 100)
b = a
b.deposer(50)
print(a.solde)
c = Compte("Ada", 150)
print(a is b, a is c, a == c)
''')
FONC = L('''
def frais_de_tenue(compte):
    """Prélève 2 € sur le compte reçu."""
    compte.solde = compte.solde - 2

c = Compte("Alan", 10)
frais_de_tenue(c)
frais_de_tenue(c)
print(c.solde)
''')
BANQUE = L('''
class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ouvrir(self, titulaire, depot=0):
        c = Compte(titulaire, depot)
        self.comptes.append(c)
        return c

    def total(self):
        s = 0
        for c in self.comptes:
            s = s + c.solde
        return s
''')
BANQUE_U = L('''
b = Banque("Banque du Code")
b.ouvrir("Ada", 120)
b.ouvrir("Alan", 80)
g = b.ouvrir("Grace")
g.deposer(300)
print(len(b.comptes), b.total())
''')
MAILLON = L('''
class Maillon:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

m3 = Maillon("C")
m2 = Maillon("B", m3)
m1 = Maillon("A", m2)
print(m1.valeur, m1.suivant.valeur, m1.suivant.suivant.valeur)
print(m1.suivant.suivant.suivant)
''')
VECTEUR = L('''
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

u = Vecteur(1, 2)
v = Vecteur(3, 4)
print(u + v)
print(u + v == Vecteur(4, 6), u is Vecteur(1, 2))
''')
TICKET = L('''
class Ticket:
    nb_crees = 0                       # attribut de CLASSE

    def __init__(self):
        Ticket.nb_crees = Ticket.nb_crees + 1
        self.numero = Ticket.nb_crees  # attribut d'INSTANCE

t1 = Ticket()
t2 = Ticket()
print(t1.numero, t2.numero, Ticket.nb_crees)
''')
HERITAGE = L('''
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "..."

class Chat(Animal):                    # Chat hérite de Animal
    def parler(self):                  # et redéfinit parler
        return self.nom + " : miaou"

print(Chat("Pixel").parler(), Animal("Bit").parler())
''')
P_SELF = L('''
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(montant):             # self oublié
        self.solde = self.solde + montant

Compte(10).deposer(5)
''')
P_POINT = L('''
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        solde = solde + montant       # « self. » oublié

Compte(10).deposer(5)
''')
P_INIT = L('''
class Compte:
    def _init_(self, solde=0):        # un seul tiret bas de chaque côté
        self.solde = solde

c = Compte(10)
''')
P_DEFAUT = L('''
class Groupe:
    def __init__(self, nom, membres=[]):    # liste créée UNE fois !
        self.nom = nom
        self.membres = membres

g1 = Groupe("T1")
g2 = Groupe("T2")
g1.membres.append("Ada")
print(g2.membres)
''')
P_DEFAUT_OK = L('''
class Groupe:
    def __init__(self, nom, membres=None):
        self.nom = nom
        if membres is None:
            membres = []        # une nouvelle liste à chaque objet
        self.membres = membres

g1 = Groupe("T1")
g2 = Groupe("T2")
g1.membres.append("Ada")
print(g2.membres)
''')
BOITE = L('''
class Boite:
    def __init__(self, contenu):
        self.contenu = contenu

b1 = Boite([1, 2])
b2 = b1
b2.contenu.append(3)
b3 = Boite([1, 2, 3])
print(b1.contenu, b1 is b2, b1 == b3)
''')
POINT = L('''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplace(self, dx):
        return Point(self.x + dx, self.y)

p = Point(0, 0)
q = p.deplace(5)
p.deplace(1)
print(p.x, q.x, p is q)
''')
MEDIA = L('''
class Mediatheque:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        self.livres.append(livre)

    def emprunter(self, titre):
        """Rend indisponible le livre de ce titre et renvoie True,
        ou renvoie False s'il est absent ou déjà emprunté."""
        ...

    def nombre_disponibles(self):
        n = 0
        for livre in self.livres:
            if livre.disponible:
                n = n + 1
            return n
''')
LIVRE = L('''
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
''')
MD_EMPR = L('''
def emprunter(self, titre):
    for livre in self.livres:
        if livre.titre == titre and livre.disponible:
            livre.disponible = False
            return True
    return False
''')
MD_NB = L('''
def nombre_disponibles(self):
    n = 0
    for livre in self.livres:
        if livre.disponible:
            n = n + 1
    return n            # return sorti de la boucle
''')
MD_TESTS = L('''
vide = Mediatheque()
assert vide.nombre_disponibles() == 0       # cas limite
m = Mediatheque()
m.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
m.ajouter(Livre("Notre-Dame de Paris", "Victor Hugo", 1831))
m.ajouter(Livre("Le Rouge et le Noir", "Stendhal", 1830))
assert m.nombre_disponibles() == 3
assert m.emprunter("Les Misérables") is True
assert m.emprunter("Les Misérables") is False
assert m.emprunter("Candide") is False
assert m.nombre_disponibles() == 2
print("tous les tests passent")
''')
PARKING = L('''
class Vehicule:
    def __init__(self, immat, categorie):
        self.immat = immat              # "AB-123-CD"
        self.categorie = categorie      # "voiture" ou "moto"

class Parking:
    def __init__(self, nb_places):
        self.places = [None] * nb_places    # None : place libre

    def nb_libres(self):
        n = 0
        for p in self.places:
            if p is None:
                n = n + 1
        return n
''')
PK_Q1 = L('''
p = Parking(4)
v = Vehicule("AB-123-CD", "voiture")
p.places[2] = v
print(p.nb_libres(), p.places[2].categorie, p.places[0])
''')
PK_PLEIN = L('''
def est_plein(self):
    return self.nb_libres() == 0
''')
PK_GARER = L('''
def garer(self, vehicule):
    for i in range(len(self.places)):
        if self.places[i] is None:
            self.places[i] = vehicule
            return i
    return -1
''')
PK_SORTIR = L('''
def sortir(self, immat):
    for i in range(len(self.places)):
        v = self.places[i]
        if v is not None and v.immat == immat:
            self.places[i] = None
            return True
    return False
''')
SQUELETTE = L('''
class NomDeClasse:                       # CamelCase par convention
    def __init__(self, a, b=0):          # constructeur
        self.a = a                       # attributs d'instance
        self.b = b

    def methode(self, x):                # self toujours en 1er
        self.b = self.b + x              # modifier l'objet
        return self.a * x                # ou renvoyer une valeur

obj = NomDeClasse(3)                     # instanciation
print(obj.methode(2), obj.b)
''')


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", humeur="mystere", carton=False, beats=[
        "{o_code}{o_code.1}Imagine que tu programmes une banque. Un compte, c'est un titulaire et un solde. "
        "Tu le ranges dans un dictionnaire : titulaire, Ada ; solde, cent.",
        "{o_code.3}Pour déposer de l'argent, tu écris une fonction à part, déposer, qui reçoit le compte et un montant. "
        "{o_code.6}On dépose cinquante. {o_code.7}On affiche le solde : {o_code.s1}cent cinquante. Tout va bien.",
        "Mais regarde la ligne suivante. {o_code.8}{o_code.x8}Une faute de frappe : sold, sans le e. "
        "{o_code.9}Python ne dit rien. {o_code.s2}Il ajoute simplement une nouvelle clé au dictionnaire. "
        "Le vrai solde n'a pas bougé, et personne n'est prévenu.",
        ("P", 0.4),
        "{-o_code}{o_q}Rien ne relie les données d'un compte aux opérations qu'on fait dessus. "
        "Et rien n'empêche d'écrire n'importe quoi. Alors, comment faire mieux ?",
        "{-o_q}{plan}La réponse s'appelle la programmation orientée objet. Voici le chemin. "
        "{plan.1}D'abord, les classes et les objets. {plan.2}Puis le constructeur, et le fameux self. "
        "{plan.3}Les méthodes, et l'accès aux attributs. {plan.4}Les références et les alias : le piège préféré des sujets. "
        "{plan.5}Des objets qui contiennent des objets. "
        "{plan.6}Et pour finir, les pièges classiques, et trois exercices corrigés : prédire une sortie, une épreuve pratique, et un sujet type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "o_code": dict(type="code", fichier="banque.py", x=170, y=78, w=940, taille=23, lignes=O_DICT,
                       sortie="150\n{'titulaire': 'Ada', 'solde': 150, 'sold': 0}"),
        "o_q": dict(type="question", t="Comment relier les données et les traitements ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Classes et objets", "Le constructeur et `self`", "Les méthodes, l'accès aux attributs",
            "Références et alias", "Des objets dans des objets", "Les pièges, trois exercices corrigés"], x=200, y=96, w=880),
        "titre": dict(type="titre", sur="NSI · Chapitre 1", t="Programmation orientée objet",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. pourquoi des objets
    dict(id="pourquoi", chap="Pourquoi des objets ?", humeur="lumiere",
         retenir="La POO regroupe dans un même type les **données** (attributs) et les **traitements** (méthodes). En Python, toute valeur est déjà un objet.",
         beats=[
        "{def_poo}La programmation orientée objet part d'une idée simple : regrouper, dans un même type, "
        "les données et les traitements qui vont avec. Les données, on les appelle les attributs. Les traitements, ce sont les méthodes.",
        "{def_poo.1}On fabrique ainsi ses propres types, avec un mode d'emploi clair : voilà ce qu'on peut faire avec un compte. Et rien d'autre.",
        "{-def_poo}{deja}{deja.1}Et tu sais quoi ? Tu utilises déjà des objets, sans le savoir. "
        "Demande à Python le type de trois : il répond, classe int. "
        "{deja.3}Le type d'une liste : classe list. En Python, toute valeur est un objet, et son type est une classe.",
        "{deja.5}Prenons une liste de mots : pile, et file. "
        "{deja.6}On écrit : mots, point, append, de liste. Ce point, c'est l'appel d'une méthode. Append est une méthode de l'objet mots. "
        "{deja.7}Et la liste a bien grandi.",
        "{deja.9}Même chose avec une chaîne : upper est une méthode des chaînes, qui renvoie la chaîne en majuscules.",
        "{-deja}{hist}Cette idée a une histoire. "
        "{hist.1}En mille neuf cent soixante-sept, deux chercheurs d'Oslo, Ole-Johan Dahl et Kristen Nygaard, créent Simula, "
        "le premier langage à classes et objets, pour faire des simulations. "
        "{hist.2}Dans les années soixante-dix, Alan Kay et son équipe du Xerox PARC développent Smalltalk, "
        "et popularisent l'expression : programmation orientée objet. "
        "{hist.3}Et en mille neuf cent quatre-vingt-onze, Guido van Rossum publie Python, où toute valeur est un objet.",
        "{-hist}",
    ], vis={
        "def_poo": dict(type="def", terme="Programmation orientée objet", cles=["attributs", "méthodes"],
                        t="Regrouper dans un même type les **données** (les attributs) et les **traitements** (les méthodes) qui leur sont propres.",
                        etape="On fabrique ses propres types, avec une interface claire : « voilà ce qu'on peut faire avec un compte ».",
                        x=150, y=170, w=980),
        "deja": dict(type="code", console=True, x=250, y=84, w=780, taille=25, lignes=DEJA),
        "hist": dict(type="liste", titre="L'histoire", css="dates", items=[
            "**Simula 67** · premier langage à classes et objets (Dahl et Nygaard, Oslo)",
            "**Smalltalk** · l'expression « programmation orientée objet » (Kay, Xerox PARC)",
            "**Python** · toute valeur est un objet (van Rossum)"],
            marques=["1967", "années 70", "1991"], x=120, y=170, w=1040),
    }),

    # ================================================================ II. classe et objet
    dict(id="classe", chap="Classe et objet", humeur="lumiere",
         retenir="Une **classe** est un plan ; un **objet** (une instance) est fabriqué à partir de ce plan. Attributs : les données de l'objet. Méthodes : les fonctions de la classe.",
         beats=[
        "{moule}Deux mots à bien distinguer. Une classe, c'est un plan, un moule. Elle décrit ce que tous les objets auront en commun. "
        "{moule.a}Pour un compte : un titulaire, et un solde. Ce sont les attributs. "
        "{moule.m}Et deux actions, déposer et retirer : ce sont les méthodes.",
        "{moule.1}À partir du plan, on fabrique des objets. Voici un premier compte : celui d'Ada, avec cent euros. "
        "{moule.2}Et un second : celui d'Alan, avec zéro euro. Même plan, mais chaque objet a ses propres valeurs.",
        "On dit qu'un objet est une instance de la classe. Et fabriquer un objet, c'est l'instancier.",
        "{-moule}{voc}Faisons le point sur le vocabulaire. {voc.1}Une classe définit un nouveau type : c'est le plan. "
        "{voc.2}Un objet, ou instance, est une valeur de ce type. {voc.3}Un attribut, c'est une variable attachée à un objet. "
        "{voc.4}Et une méthode, une fonction définie dans la classe.",
        "{-voc}{cl_code}{cl_code.1}Voyons maintenant la classe Compte, écrite en Python. {cl_code.l1}On commence par le mot clé class, "
        "suivi du nom de la classe. Par convention, il commence par une majuscule. "
        "{cl_code.2}Juste dessous, une phrase entre triples guillemets : la documentation de la classe.",
        "{cl_code.4}{cl_code.l4}Ensuite, une méthode très spéciale : init, entourée de deux tirets bas de chaque côté. C'est le constructeur. "
        "Nous y reviendrons dans un instant. {cl_code.5}{cl_code.l5-6}Il crée les deux attributs : self point titulaire, et self point solde.",
        "{cl_code.8}{cl_code.l8-9}Puis la méthode déposer : elle ajoute le montant au solde. "
        "{cl_code.11}{cl_code.l11-15}Et la méthode retirer. {cl_code.12}Si le montant dépasse le solde, {cl_code.13}elle refuse, et renvoie False. "
        "{cl_code.14}Sinon, elle retire le montant, {cl_code.15}et renvoie True.",
        "{cl_code.l0}Remarque : chaque méthode commence par le même paramètre, self. Garde cette question pour la partie suivante.",
        "{-cl_code}{uml}À l'écrit du bac, une classe est souvent donnée sous une autre forme : un diagramme de classe, en trois cases. "
        "{uml.1}En haut, le nom de la classe. {uml.2}Au milieu, les attributs, avec leur type. "
        "{uml.3}En bas, les méthodes, avec leurs paramètres, mais sans self.",
        "C'est une notation de l'UML, un langage de modélisation. Il suffit de savoir la lire, et la traduire en Python.",
        "{-uml}",
    ], vis={
        "moule": dict(type="illu", nom="moule", x=50, y=110, w=1180, h=560,
                      classe=dict(nom="Compte", attrs=["titulaire", "solde"], meths=["deposer(montant)", "retirer(montant)"]),
                      objets=[dict(nom="c1", vals=['"Ada"', "100"]), dict(nom="c2", vals=['"Alan"', "0"])]),
        "voc": dict(type="liste", titre="Le vocabulaire", items=[
            "**Classe** : le plan d'un nouveau type", "**Objet**, ou **instance** : une valeur de ce type",
            "**Attribut** : une variable attachée à un objet", "**Méthode** : une fonction définie dans la classe"],
            x=170, y=150, w=940),
        "cl_code": dict(type="code", fichier="compte.py", x=250, y=82, w=780, taille=22, lignes=COMPTE),
        "uml": dict(type="illu", nom="uml", x=60, y=120, w=1160, h=500, classe_nom="Compte",
                    attrs=["titulaire : str", "solde : int"],
                    meths=["deposer(montant)", "retirer(montant) : bool"], bw=480),
    }),

    # ================================================================ III. le constructeur et self
    dict(id="init", chap="Le constructeur et self", humeur="calme",
         retenir="`c1 = Compte(\"Ada\", 100)` : Python crée un objet vide, appelle `__init__` avec `self` = ce nouvel objet, puis range sa référence dans `c1`. `__init__` crée les attributs et ne renvoie rien.",
         beats=[
        "{q_inst}Que se passe-t-il exactement quand on écrit : c1 égale Compte, de Ada, cent ?",
        "{-q_inst}{ini}{mem1}Trois étapes. {ini.l6}{mem1.1}Un : Python crée un objet vide, de type Compte.",
        "{ini.l2}{mem1.2}Deux : il appelle le constructeur init, en lui passant ce nouvel objet. "
        "Le paramètre self reçoit l'objet. Titulaire reçoit Ada, et solde reçoit cent.",
        "{ini.l3}{mem1.3}Le constructeur exécute : self point titulaire égale titulaire. L'objet reçoit son premier attribut. "
        "{ini.l4}{mem1.4}Puis self point solde égale solde.",
        "{ini.l6b}{mem1.5}Trois : l'objet est renvoyé, et sa référence est rangée dans la variable c1. "
        "Self, lui, disparaît : ce n'était qu'un paramètre, le temps de l'appel.",
        "{-ini}{-mem1}{def_init}Retiens bien. Le constructeur init est appelé automatiquement à la création de l'objet. "
        "Son rôle : créer les attributs, avec self point nom, égale valeur. Il ne renvoie rien. "
        "{def_init.1}Pour être précis, on devrait dire l'initialiseur : quand il est appelé, l'objet existe déjà.",
        "{-def_init}{def_self}Et self ? C'est le premier paramètre de toute méthode : l'objet sur lequel la méthode travaille. "
        "Dans la classe, on écrit self point solde. À l'extérieur, on écrit c1 point solde. "
        "{def_self.1}Le mot self n'est qu'une convention. Mais tout le monde la respecte : fais de même.",
        "{-def_self}{usage}{mem2}Testons notre classe. {usage.1}{mem2.1}On crée c1, le compte d'Ada, avec cent euros. "
        "{usage.2}{mem2.2}Et c2, le compte d'Alan, sans préciser de solde. {usage.l2}Le paramètre solde a une valeur par défaut, zéro : "
        "c'est elle qui est utilisée.",
        "{usage.3}{mem2.3}On dépose cinquante euros sur c1. {usage.4}On affiche les deux soldes : {usage.s1}cent cinquante, et zéro. "
        "Déposer sur c1 n'a rien changé à c2 : chaque objet possède ses propres attributs.",
        "{usage.5}Ensuite, c1 point retirer, de cinq cents. Le solde ne suffit pas : {usage.s2}la méthode renvoie False, et le solde ne bouge pas. "
        "{usage.6}{mem2.4}Retirer trente, en revanche, ça marche : {usage.s3}True, et il reste cent vingt euros.",
        "{usage.7}Dernière ligne : le titulaire de c1, et le nom de son type. {usage.s4}Ada, et Compte. Notre classe est bien un nouveau type.",
        "{-usage}{-mem2}",
    ], vis={
        "q_inst": dict(type="question", t="Que fait Python quand on écrit `c1 = Compte(\"Ada\", 100)` ?"),
        "ini": dict(type="code", fichier="compte.py", instant=True, x=30, y=96, w=640, taille=21, lignes=INI),
        "mem1": dict(type="illu", nom="memoire", x=680, y=110, w=575, h=560, vw=240, ow=290, ordre=["self", "titulaire", "solde", "c1"], etats=[
            dict(),
            dict(o=dict(o1=dict(c="Compte", a=[], p=[266, 330])), note="1 · un objet vide"),
            dict(v=dict(self="o1", titulaire='="Ada"', solde="=100"), note="2 · __init__(self, \"Ada\", 100)"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"']])), note="self.titulaire = titulaire"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"'], ["solde", "100"]])), note="self.solde = solde"),
            dict(v=dict(self="-", titulaire="-", solde="-", c1="o1"), note="3 · la référence va dans c1"),
        ]),
        "def_init": dict(type="def", terme="Le constructeur `__init__`", cles=["attributs"],
                         t="Appelé automatiquement à la création, il **crée les attributs** avec `self.nom = valeur`. Il ne renvoie rien.",
                         etape="Plus exactement : l'initialiseur. L'objet existe déjà quand il est appelé.", x=150, y=170, w=980),
        "def_self": dict(type="def", terme="self",
                         t="Le premier paramètre de **toute** méthode : l'objet sur lequel elle travaille. Dans la classe : `self.solde` ; à l'extérieur : `c1.solde`.",
                         etape="« self » n'est qu'une convention… que tout le monde respecte.", x=150, y=170, w=980),
        "usage": dict(type="code", fichier="essai.py", x=30, y=84, w=640, taille=22, lignes=USAGE,
                      sortie="150 0\nFalse\nTrue 120\nAda Compte"),
        "mem2": dict(type="illu", nom="memoire", x=700, y=110, w=550, h=560, vw=150, ow=330, etats=[
            dict(),
            dict(v=dict(c1="o1"), o=dict(o1=dict(c="Compte", a=[["titulaire", '"Ada"'], ["solde", "100"]], p=[200, 40]))),
            dict(v=dict(c2="o2"), o=dict(o2=dict(c="Compte", a=[["titulaire", '"Alan"'], ["solde", "0"]], p=[200, 280]))),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"'], ["solde", "150"]])), note="c1.deposer(50)"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"'], ["solde", "120"]])), note="c1.retirer(30)"),
        ]),
    }),

    # ================================================================ IV. les méthodes
    dict(id="methodes", chap="Les méthodes", humeur="lumiere",
         retenir="`c.deposer(5)` revient à `Compte.deposer(c, 5)` : self reçoit l'objet placé devant le point. Une méthode modifie l'objet, renvoie une valeur, ou les deux.",
         beats=[
        "{q_self}Une méthode, c'est une fonction écrite dans la classe, dont le premier paramètre est self. "
        "Mais alors, quand on écrit c point déposer, de cinq, où est passé self ?",
        "{-q_self}{self_code}{self_code.1}Prenons le compte de Grace, avec dix euros. {self_code.2}L'écriture habituelle : c point déposer, de cinq. "
        "{self_code.3}Et voici ce que Python fait réellement : il appelle la fonction déposer de la classe Compte, en lui donnant c comme premier argument. "
        "Self reçoit c. {self_code.4}On a déposé deux fois cinq euros : {self_code.s}le solde vaut vingt.",
        "{-self_code}{tr_code}{mem3}Regardons self travailler. {tr_code.l8}{mem3.1}On appelle a point déposer, de cinquante. "
        "Pendant l'appel, self désigne l'objet de a. {tr_code.l4}{mem3.2}Self point solde augmente de cinquante : c'est le solde d'Ada qui passe à cent cinquante.",
        "{tr_code.l9}{mem3.3}Maintenant, b point déposer, de vingt. Cette fois, self désigne l'objet de b. "
        "{tr_code.l4b}{mem3.4}Et c'est le solde d'Alan qui passe à vingt. "
        "{tr_code.l0}{mem3.5}Le même code, deux objets différents : c'est tout l'intérêt de self.",
        "{-tr_code}{-mem3}{trois}Une méthode peut faire trois choses. {trois.1}Modifier l'objet, comme déposer. "
        "{trois.2}Renvoyer une valeur calculée à partir des attributs, comme retirer, qui renvoie un booléen. {trois.3}Ou les deux à la fois. "
        "{trois.4}Elle peut aussi appeler une autre méthode : du même objet, avec self point, ou d'un autre objet, reçu en paramètre.",
        "{-trois}{vir}{vir.1}Exemple : un virement d'un compte vers un autre. {vir.l5}On ajoute d'abord un attribut historique, une liste vide au départ. "
        "Un attribut peut contenir n'importe quelle valeur, même une liste. "
        "{vir.7}{vir.l7-9}Déposer ajoute le montant au solde, et note l'opération dans l'historique.",
        "{vir.11}{vir.l11}Et voici virer vers. Elle reçoit deux choses : un autre compte, et le montant. "
        "{vir.12}{vir.l12-13}Si le solde ne suffit pas, elle refuse. {vir.14}{vir.l14-15}Sinon, elle retire le montant, et le note. "
        "{vir.16}{vir.l16}Puis elle appelle autre point déposer : une méthode qui appelle la méthode d'un autre objet. {vir.17}{vir.l17}Et elle renvoie True.",
        "{vir.l0}{vir_u}{vir_u.1}Ada a cent euros, {vir_u.2}Alan zéro. {vir_u.3}Ada vire quarante euros à Alan. "
        "{vir_u.4}Résultat : {vir_u.s1}soixante, et quarante. {vir_u.5}Et chacun a son historique : {vir_u.s2}"
        "un virement de moins quarante chez Ada, un dépôt de quarante chez Alan.",
        "{-vir}{-vir_u}",
    ], vis={
        "q_self": dict(type="question", t="`c.deposer(5)` : où est passé `self` ?"),
        "self_code": dict(type="code", fichier="self.py", x=140, y=110, w=1000, taille=26, lignes=SELF, sortie="20"),
        "tr_code": dict(type="code", fichier="self.py", instant=True, x=24, y=96, w=650, taille=21, lignes=TRACE),
        "mem3": dict(type="illu", nom="memoire", x=700, y=110, w=556, h=560, vw=170, ow=320, ordre=["a", "b", "self", "montant"], etats=[
            dict(v=dict(a="o1", b="o2"), o=dict(o1=dict(c="Compte", a=[["titulaire", '"Ada"'], ["solde", "100"]], p=[205, 40]),
                                                o2=dict(c="Compte", a=[["titulaire", '"Alan"'], ["solde", "0"]], p=[205, 290]))),
            dict(v=dict(self="o1", montant="=50"), note="a.deposer(50) : self = a"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"'], ["solde", "150"]]))),
            dict(v=dict(self="o2", montant="=20"), note="b.deposer(20) : self = b"),
            dict(o=dict(o2=dict(a=[["titulaire", '"Alan"'], ["solde", "20"]]))),
            dict(v=dict(self="-", montant="-"), note="même code, deux objets"),
        ]),
        "trois": dict(type="liste", titre="Ce que fait une méthode", items=[
            "**Modifier** l'objet : `deposer`", "**Renvoyer** une valeur : `retirer` renvoie un booléen",
            "Ou **les deux**", "**Appeler** une autre méthode : `self.autre()`, `autre_objet.methode()`"],
            x=150, y=150, w=980),
        "vir": dict(type="code", fichier="virement.py", x=20, y=80, w=730, taille=20, lignes=VIR),
        "vir_u": dict(type="code", fichier="virement.py", x=768, y=96, w=492, taille=19, lignes=VIR_U,
                      sortie="60 40\n[('virement', -40)] [('dépôt', 40)]"),
    }),

    # ================================================================ V. accès, accesseurs, affichage
    dict(id="acces", chap="Accéder aux attributs, afficher un objet", humeur="calme",
         retenir="On lit et on écrit un attribut par `objet.attribut`, mais mieux vaut passer par des méthodes : accesseur (getter), mutateur (setter). `_solde` : privé par convention. `__str__` **renvoie** le texte affiché par `print`.",
         beats=[
        "{acc}{acc.1}On lit et on écrit un attribut avec la notation pointée : objet, point, attribut. "
        "{acc.2}Lire c point solde : {acc.s1}cent. {acc.3}{acc.x3}Mais Python laisse aussi écrire n'importe quoi : c point solde égale moins mille. "
        "{acc.4}On affiche le solde : {acc.s2}moins mille. Aucune erreur ! Le compte est à découvert, sans le moindre contrôle.",
        "{-acc}{gs}Pour garder un objet cohérent, on passe plutôt par des méthodes. "
        "{gs.1}Une méthode qui renvoie un attribut s'appelle un accesseur, en anglais un getter. "
        "{gs.2}Une méthode qui le modifie, en vérifiant la valeur, s'appelle un mutateur : un setter. "
        "{gs.3}Et un attribut dont le nom commence par un tiret bas est privé, par convention. Python ne bloque rien : "
        "c'est un avertissement entre programmeurs. Ne touche pas directement.",
        "{-gs}{gcode}Voici la classe réécrite. {gcode.4}{gcode.l4}L'attribut s'appelle maintenant : tiret bas solde. "
        "{gcode.6}{gcode.l6-7}Get solde est l'accesseur : il renvoie tiret bas solde. "
        "{gcode.9}{gcode.l9-11}Déposer est la seule façon prévue de modifier le solde. "
        "{gcode.l10}Avec assert, elle vérifie d'abord que le montant est positif. Sinon, le programme s'arrête, avec une erreur.",
        "{gcode.13}{gcode.l13-15}Enfin, une méthode spéciale : str, entourée de deux tirets bas. Elle doit renvoyer une chaîne : le texte qu'affichera print. "
        "{gcode.l0}{gu}{gu.1}On crée le compte, {gu.2}on dépose vingt, {gu.3}on lit le solde avec l'accesseur : {gu.s1}cent vingt. "
        "{gu.4}Et print de c affiche {gu.s2}la phrase renvoyée par str : Compte de Ada, cent vingt euros.",
        "{-gcode}{-gu}{nostr}Et sans str, que ferait print ? Il afficherait seulement quelque chose comme : main, Compte object at, "
        "suivi d'une adresse en mémoire. Illisible, et différent à chaque exécution. "
        "{nostr.1}Attention : str doit renvoyer la chaîne, avec return. Pas l'afficher avec print.",
        "{-nostr}{enc}Pour aller plus loin : cacher l'intérieur d'un objet derrière une interface de méthodes, c'est l'encapsulation. "
        "C'est une idée centrale de la programmation objet. "
        "{enc.1}Mais le programme de Terminale n'exige que le vocabulaire, et l'usage des accesseurs que l'énoncé te donne.",
        "{-enc}",
    ], vis={
        "acc": dict(type="code", fichier="acces.py", x=170, y=100, w=940, taille=26, lignes=ACCES, sortie="100\n-1000"),
        "gs": dict(type="liste", titre="Protéger les attributs", items=[
            "**Accesseur** (getter) : une méthode qui renvoie un attribut",
            "**Mutateur** (setter) : une méthode qui le modifie, en contrôlant la valeur",
            "`_solde` : privé **par convention** (Python ne bloque rien)"], x=140, y=160, w=1000),
        "gcode": dict(type="code", fichier="compte.py", x=24, y=84, w=790, taille=19, lignes=GS),
        "gu": dict(type="code", fichier="compte.py", x=838, y=96, w=418, taille=19, lignes=GS_U,
                   sortie="120\nCompte de Ada : 120 €"),
        "nostr": dict(type="note", titre="Sans `__str__`",
                      t="`print(c)` affiche seulement `<__main__.Compte object at 0x7f…>` : une adresse, qui change à chaque exécution.",
                      etape="`__str__` doit **renvoyer** une chaîne (`return`), pas l'afficher.", x=140, y=180, w=1000),
        "enc": dict(type="def", terme="Encapsulation", plus=True,
                    t="Cacher l'implémentation d'un objet derrière une interface de méthodes : une idée centrale de la POO.",
                    etape="Exigible en Terminale : le vocabulaire, et l'usage des accesseurs que l'énoncé fournit.", x=150, y=190, w=980),
    }),

    # ================================================================ VI. références et alias
    dict(id="alias", chap="Références et alias", humeur="tension",
         retenir="Une variable contient une **référence** vers l'objet. `b = a` copie la référence : un seul objet, deux noms. `is` teste l'identité ; sans `__eq__`, `==` aussi. Une fonction qui reçoit un objet peut le modifier.",
         beats=[
        "{ref}Voici sans doute le point le plus important du chapitre, et le piège préféré des sujets de bac. "
        "Une variable ne contient pas un objet. Elle contient une référence : l'adresse de l'objet en mémoire.",
        "{-ref}{alc}{mem4}{alc.1}{mem4.1}On crée a, un compte de cent euros. {alc.2}{mem4.2}Puis on écrit : b égale a. "
        "{alc.l2}Cette ligne ne copie pas l'objet. Elle copie la référence. a et b désignent le même objet : on dit que b est un alias de a.",
        "{alc.l0}{alc.3}{mem4.3}On dépose cinquante, en passant par b. {alc.4}Et on affiche le solde de a : {alc.s1}cent cinquante ! "
        "a a changé aussi, puisque c'est le même objet.",
        "{alc.5}{mem4.4}Maintenant, c : un autre compte, avec les mêmes valeurs. {alc.6}Et trois tests. "
        "{alc.s2}a is b : True, c'est le même objet. a is c : False, ce sont deux objets distincts. "
        "Et a, double égal, c : False aussi ! Pour une classe qui ne définit pas la méthode eq, le double égal compare les identités, exactement comme is.",
        "{-alc}{-mem4}{isq}Retiens la différence. {isq.1}is teste si deux noms désignent le même objet. "
        "{isq.2}Le double égal teste l'égalité. Mais sans méthode eq dans la classe, il se comporte comme is. "
        "{isq.3}Et pour copier vraiment un objet, il faut en construire un nouveau : b égale Compte, de a point titulaire, et a point solde.",
        "{-isq}{fo}{mem5}{fo.1}Même chose quand on passe un objet à une fonction. {fo.l1-3}La fonction frais de tenue reçoit un compte, "
        "et lui retire deux euros. {fo.5}{fo.l5}{mem5.1}On crée c, avec dix euros. "
        "{fo.6}{fo.l6}{mem5.2}On appelle la fonction : son paramètre, compte, reçoit une référence vers le même objet. {mem5.3}Le solde passe à huit.",
        "{fo.7}{fo.l7}{mem5.4}Deuxième appel : six. {mem5.5}{fo.8}{fo.l8}Print affiche {fo.s}six : la fonction a modifié l'objet d'origine. "
        "C'est un effet de bord. Ici, il est voulu. Mais quand il ne l'est pas, c'est une source de bugs : "
        "tu le verras dans le chapitre Modularité et mise au point.",
        "{-fo}{-mem5}",
    ], vis={
        "ref": dict(type="def", terme="Référence", cles=["référence"],
                    t="Une variable ne « contient » pas l'objet : elle contient une **référence** vers lui, son adresse en mémoire.",
                    x=150, y=200, w=980),
        "alc": dict(type="code", fichier="alias.py", x=30, y=84, w=620, taille=23, lignes=ALIAS, sortie="150\nTrue False False"),
        "mem4": dict(type="illu", nom="memoire", x=690, y=110, w=560, h=560, vw=150, ow=330, ordre=["a", "b", "c"], etats=[
            dict(),
            dict(v=dict(a="o1"), o=dict(o1=dict(c="Compte", a=[["titulaire", '"Ada"'], ["solde", "100"]], p=[200, 40]))),
            dict(v=dict(b="o1"), note="b = a : la référence est copiée"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Ada"'], ["solde", "150"]])), note="b.deposer(50)"),
            dict(v=dict(c="o2"), o=dict(o2=dict(c="Compte", a=[["titulaire", '"Ada"'], ["solde", "150"]], p=[200, 290])),
                 note="c : un autre objet"),
        ]),
        "isq": dict(type="liste", titre="is ou == ?", items=[
            "`a is b` : est-ce **le même objet** ?",
            "`a == b` : l'égalité, définie par `__eq__` ; sans elle, comme `is`",
            "Copier vraiment : `b = Compte(a.titulaire, a.solde)`"], x=140, y=160, w=1000),
        "fo": dict(type="code", fichier="frais.py", x=30, y=84, w=620, taille=22, lignes=FONC, sortie="6"),
        "mem5": dict(type="illu", nom="memoire", x=690, y=110, w=560, h=560, vw=190, ow=310, ordre=["c", "compte"], etats=[
            dict(),
            dict(v=dict(c="o1"), o=dict(o1=dict(c="Compte", a=[["titulaire", '"Alan"'], ["solde", "10"]], p=[230, 110]))),
            dict(v=dict(compte="o1"), note="frais_de_tenue(c) : compte = c"),
            dict(o=dict(o1=dict(a=[["titulaire", '"Alan"'], ["solde", "8"]]))),
            dict(o=dict(o1=dict(a=[["titulaire", '"Alan"'], ["solde", "6"]])), note="deuxième appel"),
            dict(v=dict(compte="-"), note="l'objet d'origine a changé"),
        ]),
    }),

    # ================================================================ VII. composition
    dict(id="compo", chap="Des objets qui contiennent des objets", humeur="lumiere",
         retenir="Un attribut peut contenir d'autres objets : c'est la **composition** (une banque et ses comptes). Un maillon qui référence le maillon suivant : c'est la liste chaînée.",
         beats=[
        "{bq}{bq.1}Un attribut peut contenir une liste d'objets. C'est la composition : une banque possède des comptes, une médiathèque des livres. "
        "{bq.l1}Voici la classe Banque. {bq.4}{bq.l4}Son attribut comptes est une liste, vide au départ.",
        "{bq.6}{bq.l6-9}La méthode ouvrir crée un nouveau Compte, {bq.8}l'ajoute à la liste, {bq.9}et le renvoie. "
        "{bq.11}{bq.l11-15}Total parcourt les comptes, et additionne leurs soldes : self point comptes, puis c point solde.",
        "{bq.l0}{bqu}{bqu.1}On crée la banque. {bqu.2}On ouvre deux comptes, {bqu.4}puis un troisième, celui de Grace, qu'on garde dans g. "
        "{bqu.5}On dépose trois cents euros sur g. {bqu.6}On affiche : {bqu.s}trois comptes, et cinq cents euros en tout : cent vingt, plus quatre-vingts, plus trois cents. "
        "Le dépôt fait par g se retrouve dans la banque : g et la liste désignent le même objet.",
        "{-bq}{-bqu}{mai}{mai.1}Un attribut peut aussi contenir un autre objet, de la même classe. C'est l'idée du maillon. "
        "{mai.l1-4}La classe Maillon a deux attributs : {mai.l3}la valeur, {mai.l4}et suivant, qui désigne un autre maillon, ou None, par défaut.",
        "{mai.l0}{mai.6}On crée trois maillons, en partant de la fin : m3 contient C. {mai.7}m2 contient B, et pointe vers m3. "
        "{mai.8}m1 contient A, et pointe vers m2. {mai.9}En suivant les références : {mai.s1}m1 point suivant point valeur donne B, "
        "et deux fois suivant donne C. {mai.10}Trois fois suivant : {mai.s2}None, la fin de la chaîne.",
        "{-mai}{mem6}Voici la chaîne en mémoire. {mem6.1}m3, {mem6.2}m2 qui pointe vers m3, {mem6.3}m1 qui pointe vers m2. "
        "C'est le principe de la liste chaînée, que tu retrouveras dans le chapitre Listes, piles, files.",
        "{mem6.4}Et c'est pour cela que la programmation objet est rangée dans la rubrique Structures de données du programme : "
        "elle sert à implémenter des piles, des files, des arbres, des graphes.",
        "{-mem6}",
    ], vis={
        "bq": dict(type="code", fichier="banque.py", x=24, y=84, w=650, taille=20, lignes=BANQUE),
        "bqu": dict(type="code", fichier="banque.py", x=700, y=96, w=556, taille=20, lignes=BANQUE_U, sortie="3 500"),
        "mai": dict(type="code", fichier="maillon.py", x=24, y=84, w=860, taille=21, lignes=MAILLON, term="droite", tw=330,
                    sortie="A B C\nNone"),
        "mem6": dict(type="illu", nom="memoire", x=40, y=120, w=1200, h=540, vw=150, ow=280, ordre=["m3", "m2", "m1"], etats=[
            dict(),
            dict(v=dict(m3="o3"), o=dict(o3=dict(c="Maillon", a=[["valeur", '"C"'], ["suivant", "None"]], p=[920, 30]))),
            dict(v=dict(m2="o2"), o=dict(o2=dict(c="Maillon", a=[["valeur", '"B"'], ["suivant", "@o3"]], p=[590, 180]))),
            dict(v=dict(m1="o1"), o=dict(o1=dict(c="Maillon", a=[["valeur", '"A"'], ["suivant", "@o2"]], p=[200, 330]))),
            dict(note="pile, file, arbre, graphe : des objets reliés"),
        ]),
    }),

    # ================================================================ VIII. pour aller plus loin
    dict(id="plus", chap="Pour aller plus loin", humeur="mystere",
         retenir="Méthodes spéciales : `__str__` (print), `__eq__` (==), `__add__` (+)… Un attribut de classe est partagé par tous les objets. Héritage et polymorphisme : hors programme.",
         beats=[
        "{spec}Les méthodes dont le nom est entouré de deux tirets bas sont appelées par Python dans des situations précises. "
        "{spec.1}Init, à la création. {spec.2}Str, par print. {spec.3}Eq, par le double égal. {spec.4}Add, par le signe plus. "
        "{spec.5}Len, par la fonction len. {spec.6}Et lt, pour less than, par le signe inférieur. "
        "Ce n'est pas exigible, mais on en croise souvent dans les sujets.",
        "{-spec}{vec}Exemple : des vecteurs. {vec.6}{vec.l6-7}Add renvoie un nouveau vecteur, somme des deux. "
        "{vec.9}{vec.l9-10}Eq compare les coordonnées. {vec.12}{vec.l12-13}Et str fabrique le texte à afficher.",
        "{vec.15}{vec.l15-17}u vaut un, deux. v vaut trois, quatre. Print de u plus v : {vec.s1}quatre, six. "
        "{vec.18}{vec.l18}Ensuite : u plus v, double égal, Vecteur quatre, six. {vec.s2}True, grâce à eq. "
        "Mais u is Vecteur un, deux : False. Mêmes coordonnées, mais deux objets distincts.",
        "{-vec}{tick}Autre outil : l'attribut de classe. {tick.2}{tick.l2}Nb créés est défini directement dans la classe, hors de toute méthode. "
        "Il est partagé par tous les objets. {tick.4}{tick.l5}À chaque création, le constructeur l'augmente de un, "
        "{tick.l6}et donne ce numéro au ticket, dans un attribut d'instance, propre à chaque objet.",
        "{tick.l0}{tick.8}On crée deux tickets. {tick.10}Résultat : {tick.s}numéros un et deux. Et deux tickets créés en tout.",
        "{-tick}{her}Enfin, ce qui est hors programme. {her.8}{her.l8}L'héritage permet de définir une classe à partir d'une autre : "
        "Chat hérite d'Animal. Il récupère ses attributs et ses méthodes, {her.9}{her.l9-10}et peut en redéfinir, comme parler.",
        "{her.12}{her.l12}Résultat : {her.s}un chat dit miaou ; un animal quelconque dit trois petits points. Un même appel, parler, "
        "qui s'adapte au type de l'objet : c'est le polymorphisme.",
        "{her.l0}Le programme le précise : héritage et polymorphisme ne sont pas exigibles. Il faut savoir les reconnaître, pas les maîtriser.",
        "{-her}{para}Retiens aussi ceci : la programmation objet est l'un des trois paradigmes au programme, avec l'impératif et le fonctionnel. "
        "Et un même programme peut les mélanger.",
        "{-para}",
    ], vis={
        "spec": dict(type="liste", titre="Les méthodes spéciales", plus=True, items=[
            "`__init__` : à la création", "`__str__` : par `print` et `str()`", "`__eq__` : par `==`",
            "`__add__` : par `+`", "`__len__` : par `len()`", "`__lt__` : par `<`"], x=200, y=96, w=880),
        "vec": dict(type="code", fichier="vecteur.py", instant=True, x=24, y=84, w=780, taille=19, lignes=VECTEUR,
                    term="droite", tw=420, sortie="(4, 6)\nTrue False"),
        "tick": dict(type="code", fichier="ticket.py", x=120, y=100, w=1040, taille=24, lignes=TICKET, sortie="1 2 2"),
        "her": dict(type="code", titre="Hors programme · l'héritage", fichier="animaux.py", x=30, y=84, w=860, taille=20,
                    lignes=HERITAGE, term="droite", tw=340, sortie="Pixel : miaou ..."),
        "para": dict(type="note", titre="Trois paradigmes",
                     t="La programmation **objet**, la programmation **impérative**, la programmation **fonctionnelle** : un même programme peut les mélanger.",
                     x=150, y=210, w=980),
    }),

    # ================================================================ IX. les pièges
    dict(id="pieges", chap="Les pièges classiques", humeur="tension",
         retenir="`self` en premier paramètre ; `self.` devant chaque attribut ; `__init__` avec deux tirets bas ; jamais de liste par défaut ; la classe n'est pas l'objet ; `b = a` ne copie rien ; des parenthèses pour appeler.",
         beats=[
        "{p1}Faisons le tour des pièges. Premier piège : oublier self dans la définition d'une méthode. "
        "{p1.5}{p1.x5}Ici, déposer n'a qu'un paramètre : montant. {p1.8}{p1.l8}On appelle Compte de dix, point déposer, de cinq. "
        "{p1.e}Erreur ! Python passe toujours l'objet en premier argument : la méthode reçoit deux arguments, l'objet et cinq, "
        "alors qu'elle n'en attend qu'un.",
        "{-p1}{p2}Deuxième piège, plus sournois : oublier self point devant un attribut. "
        "{p2.6}{p2.x6}Ici : solde égale solde plus montant, sans self. Pour Python, solde est alors une variable locale de la méthode, "
        "{p2.8}qu'on lit avant de l'avoir définie. {p2.e}UnboundLocalError. Il faut écrire : self point solde, égale self point solde plus montant.",
        "{-p2}{p3}Troisième piège : mal écrire init. {p3.2}{p3.x2}Un seul tiret bas de chaque côté. "
        "{p3.5}{p3.l5}Python ne trouve pas de constructeur, {p3.e}et refuse les arguments : Compte ne prend pas d'argument. "
        "Il faut deux tirets bas, avant et après.",
        "{-p3}{p4}Quatrième piège, célèbre : une liste comme valeur par défaut. {p4.2}{p4.x2}Membres égale crochets vides. "
        "{p4.6}{p4.l6-7}On crée deux groupes, sans préciser les membres. {p4.8}{p4.l8}On ajoute Ada au premier. {p4.9}{p4.l9}Et on affiche les membres du second.",
        "{p4.s}Surprise : Ada est aussi dans le second groupe ! La valeur par défaut est créée une seule fois, à la définition de la méthode. "
        "Tous les objets créés sans argument partagent la même liste.",
        "{-p4}{p4b}La correction classique : None par défaut. {p4b.l4-5}Si membres vaut None, on crée une nouvelle liste, dans le corps de la méthode. "
        "Une liste neuve pour chaque objet. {p4b.l0}{p4b.s}Cette fois, le second groupe est vide.",
        "{-p4b}{p5}Encore trois pièges, plus courts. {p5.1}Confondre la classe et l'objet : Compte point solde n'existe pas. "
        "Solde est un attribut d'instance : il n'existe qu'une fois l'objet créé. "
        "{p5.2}Croire que b égale a copie l'objet : c'est un alias. "
        "{p5.3}Et oublier les parenthèses d'un appel : c point get solde, sans parenthèses, ne calcule rien. C'est la méthode elle-même, pas son résultat.",
        "{-p5}",
    ], vis={
        "p1": dict(type="code", fichier="piege1.py", x=110, y=86, w=1060, taille=24, lignes=P_SELF,
                   erreur="TypeError: Compte.deposer() takes 1 positional argument but 2 were given"),
        "p2": dict(type="code", fichier="piege2.py", x=60, y=86, w=1160, taille=21, lignes=P_POINT,
                   erreur="UnboundLocalError: cannot access local variable 'solde' where it is not associated with a value"),
        "p3": dict(type="code", fichier="piege3.py", x=110, y=110, w=1060, taille=22, lignes=P_INIT,
                   erreur="TypeError: Compte() takes no arguments"),
        "p4": dict(type="code", fichier="piege4.py", x=110, y=86, w=1060, taille=23, lignes=P_DEFAUT, sortie="['Ada']"),
        "p4b": dict(type="code", fichier="piege4.py", instant=True, x=110, y=86, w=1060, taille=21, lignes=P_DEFAUT_OK, sortie="[]"),
        "p5": dict(type="liste", titre="Trois autres pièges", items=[
            "La classe n'est pas l'objet : `Compte.solde` → AttributeError",
            "`b = a` ne copie pas l'objet : c'est un **alias**",
            "Des parenthèses pour appeler : `c.get_solde()`, pas `c.get_solde`"],
            marques=["!", "!", "!"], x=120, y=160, w=1040),
    }),

    # ================================================================ X. exercice 1 : prédis la sortie
    dict(id="exo1", chap="Exercice 1 · prédis la sortie", humeur="tension", beats=[
        "{ex1}Place à l'entraînement. Premier exercice : prédis la sortie. Lis ce programme sans l'exécuter, "
        "et écris sur une feuille ce qu'il affiche. C'est exactement ce qu'on te demande à l'écrit.",
        "{-ex1}{pa1}À toi. Mets la vidéo sur pause, et écris la sortie.",
        "{pa1.stop}{-pa1}{ex1c}{mem7}Correction. {ex1c.l5}{mem7.1}b1 est une boîte qui contient la liste un, deux. "
        "{ex1c.l6}{mem7.2}b2 égale b1 : un alias. Une seule boîte, deux noms.",
        "{ex1c.l7}{mem7.3}On ajoute trois à la liste, en passant par b2. C'est la liste de l'unique boîte qui grandit. "
        "{ex1c.l8}{mem7.4}b3 est une autre boîte, qui contient une autre liste : un, deux, trois.",
        "{ex1c.l9}Que vaut l'affichage ? {ex1c.s}D'abord b1 point contenu : un, deux, trois. Ensuite b1 is b2 : True, même objet. "
        "Enfin b1, double égal, b3 : False. Les contenus sont égaux, mais la classe n'a pas de méthode eq : le double égal compare les identités.",
        "{-ex1c}{-mem7}{ex1b}Une deuxième, plus rapide. {ex1b.l6-7}La méthode déplace renvoie un nouveau point. "
        "{ex1b.l9-11}On crée p, à l'origine. q égale p point déplace, de cinq. Puis on appelle p point déplace, de un, sans garder le résultat. "
        "{ex1b.l12}Que valent p point x, q point x, et p is q ?",
        "{-ex1b}{pa1b}À toi : trois valeurs à prédire.",
        "{pa1b.stop}{-pa1b}{ex1bc}{ex1bc.s}Zéro, cinq, False. {ex1bc.l7}Déplace ne modifie pas p : elle renvoie un nouvel objet. "
        "{ex1bc.l10}q est ce nouveau point, d'abscisse cinq. {ex1bc.l11}Le second appel crée un point qui est aussitôt perdu : on ne le range nulle part. "
        "{ex1bc.l12}Et p n'a pas bougé : p point x vaut toujours zéro. Deux objets distincts, donc p is q est faux.",
        "{-ex1bc}",
    ], vis={
        "ex1": dict(type="code", titre="Exercice 1 · prédis la sortie", fichier="boite.py", instant=True, x=200, y=96, w=880, taille=26,
                    lignes=BOITE),
        "pa1": dict(type="pause", t="Écris ce qu'affiche la dernière ligne."),
        "ex1c": dict(type="code", fichier="boite.py", instant=True, x=30, y=90, w=640, taille=22, lignes=BOITE,
                     sortie="[1, 2, 3] True False"),
        "mem7": dict(type="illu", nom="memoire", x=700, y=110, w=550, h=560, vw=150, ow=330, ordre=["b1", "b2", "b3"], etats=[
            dict(),
            dict(v=dict(b1="o1"), o=dict(o1=dict(c="Boite", a=[["contenu", "[1, 2]"]], p=[200, 40]))),
            dict(v=dict(b2="o1"), note="b2 = b1 : un alias"),
            dict(o=dict(o1=dict(a=[["contenu", "[1, 2, 3]"]])), note="b2.contenu.append(3)"),
            dict(v=dict(b3="o2"), o=dict(o2=dict(c="Boite", a=[["contenu", "[1, 2, 3]"]], p=[200, 290])), note="b3 : un autre objet"),
        ]),
        "ex1b": dict(type="code", titre="Exercice 1 · deuxième programme", fichier="point.py", instant=True, x=200, y=96, w=880, taille=24,
                     lignes=POINT),
        "pa1b": dict(type="pause", t="Que valent `p.x`, `q.x` et `p is q` ?"),
        "ex1bc": dict(type="code", fichier="point.py", instant=True, x=200, y=84, w=880, taille=20, lignes=POINT, sortie="0 5 False"),
    }),

    # ================================================================ XI. exercice 2 : épreuve pratique
    dict(id="exo2", chap="Exercice 2 · épreuve pratique : la médiathèque", humeur="tension", beats=[
        "{epq}Deuxième exercice, au format de l'épreuve pratique : sur machine, avec un programme fourni. "
        "On gère les livres d'une médiathèque. Un livre a un titre, un auteur, une année, et un attribut disponible, qui vaut True au départ.",
        "{epq.1}Trois questions. Un : compléter la méthode emprunter. {epq.2}Deux : la méthode nombre disponibles est déjà écrite, mais elle contient une erreur. "
        "Avec trois livres disponibles, elle renvoie un. Trouve l'erreur, et corrige-la. {epq.3}Trois : écrire des tests, y compris les cas limites.",
        "{-epq}{ep}Voici le programme fourni. {ep.l3}La médiathèque range ses livres dans une liste. {ep.l8-11}La méthode emprunter est à compléter : "
        "sa documentation dit ce qu'elle doit faire. {ep.l13-18}Et voici nombre disponibles, qui se trompe.",
        "{-ep}{pa_ep}À toi. Mets sur pause, et cherche les trois questions. Si tu as un ordinateur, tape le programme et teste-le.",
        "{pa_ep.stop}{-pa_ep}{epc}{epc.q1}{md1}Correction. Question un : emprunter. {md1.1}{md1.2}On parcourt les livres. "
        "{md1.3}Dès qu'on trouve le bon titre, et que le livre est disponible, {md1.4}on le marque emprunté, {md1.5}et on renvoie True. "
        "{md1.6}{md1.l6}Si la boucle se termine sans succès, on renvoie False. Ce return est après la boucle, pas dedans.",
        "{-md1}{epc.q2}{md2}Question deux : le bug. {md2.1}{md2.2}Dans la version fournie, le return n était indenté dans la boucle. "
        "La méthode s'arrêtait donc dès le premier livre, et renvoyait un. {md2.6}{md2.l6}Il suffit de désindenter le return d'un niveau : "
        "on ne renvoie le compte qu'une fois tous les livres parcourus.",
        "{-md2}{epc.q3}{md3}Question trois : les tests. {md3.1}{md3.2}D'abord un cas limite : une médiathèque vide a zéro livre disponible. "
        "{md3.3}Puis une médiathèque de trois livres. {md3.7}Trois disponibles. {md3.8}Un premier emprunt réussit. "
        "{md3.9}Le même livre, une seconde fois : refusé, il est déjà emprunté. {md3.10}Un titre absent : refusé aussi. "
        "{md3.11}Et il reste deux livres disponibles. {md3.12}Si une assertion est fausse, le programme s'arrête avec une erreur. {md3.s}Ici, tous les tests passent.",
        "{-md3}{-epc}{oral}À l'épreuve pratique, l'examinateur te pose aussi des questions à l'oral. Par exemple : "
        "{oral.1}que représente self dans emprunter ? L'objet Médiathèque sur lequel on appelle la méthode. "
        "{oral.2}Et quel est le type de livre, dans la boucle ? Un objet de la classe Livre : on accède à ses attributs par livre point titre, livre point disponible.",
        "{-oral}",
    ], vis={
        "epq": dict(type="exo", niveau="difficile", etiquette="Exercice 2 · épreuve pratique", titre="La médiathèque",
                    enonce=["Un livre (classe `Livre`) a un titre, un auteur, une année et un attribut `disponible`, True au départ."],
                    questions=["Compléter la méthode `emprunter` (voir sa documentation).",
                               "`nombre_disponibles` renvoie 1 au lieu de 3 : trouver l'erreur et la corriger.",
                               "Écrire des tests, y compris les cas limites."]),
        "ep": dict(type="code", fichier="mediatheque.py", instant=True, x=120, y=84, w=1040, taille=19, lignes=MEDIA),
        "pa_ep": dict(type="pause", t="Compléter, corriger, tester."),
        "epc": dict(type="exo", mode="coin", niveau="difficile", etiquette="Exercice 2 · épreuve pratique", titre="La médiathèque",
                    donnees=["`livres` : liste de `Livre`"], questions=["`emprunter`", "le bug", "les tests"]),
        "md1": dict(type="code", fichier="mediatheque.py", x=530, y=140, w=726, taille=19, lignes=MD_EMPR),
        "md2": dict(type="code", fichier="mediatheque.py", x=530, y=140, w=726, taille=19, lignes=MD_NB),
        "md3": dict(type="code", fichier="tests.py", x=530, y=84, w=726, taille=17, lignes=MD_TESTS, sortie="tous les tests passent"),
        "oral": dict(type="liste", titre="À l'oral", items=[
            "`self` dans `emprunter` : l'objet `Mediatheque` sur lequel on appelle la méthode",
            "`livre` dans la boucle : un objet de la classe `Livre` (`livre.titre`, `livre.disponible`)"],
            marques=["?", "?"], x=140, y=170, w=1000),
    }),

    # ================================================================ XII. exercice 3 : type bac (écrit)
    dict(id="exo3", chap="Exercice 3 · type bac : un parking", humeur="tension", beats=[
        "{ex2}Troisième exercice, au format de l'épreuve écrite. Un parking possède un nombre fixe de places, numérotées à partir de zéro. "
        "Une place libre vaut None.",
        "Cinq questions. {ex2.1}Un : prédire l'affichage d'un petit programme. {ex2.2}Deux : écrire la méthode est plein. "
        "{ex2.3}Trois : écrire garer, qui place un véhicule sur la première place libre. {ex2.4}Quatre : écrire sortir, qui libère la place d'un véhicule. "
        "{ex2.5}Cinq : une question sur les références.",
        "{-ex2}{pk}Voici les deux classes fournies. {pk.l1-4}Un véhicule a une immatriculation, et une catégorie, voiture ou moto. "
        "{pk.l6-8}Un parking a un attribut places : une liste de None, de la taille voulue. "
        "{pk.l10-15}Et une méthode nb libres, qui compte les places qui valent None.",
        "{-pk}{pa2}C'est un exercice au format du bac. Prends le temps : mets sur pause, et rédige tout sur une feuille.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}{k1}Correction. Question un. {k1.1}On crée un parking de quatre places, {k1.2}un véhicule, "
        "{k1.3}et on range ce véhicule à la place numéro deux. {k1.4}Que vaut l'affichage ? {k1.s}Trois places libres. "
        "La catégorie du véhicule de la place deux : voiture. Et la place zéro est libre : None.",
        "{-k1}{ex2c.q2}{k2}{k2.1}Question deux : est plein. {k2.2}Une seule ligne suffit : on renvoie self point nb libres, "
        "double égal zéro. On réutilise la méthode existante, avec self point, comme l'énoncé le demande. "
        "Pas besoin de if, return True, else, return False : la comparaison est déjà un booléen.",
        "{-k2}{ex2c.q3}{k3}{k3.1}Question trois : garer. {k3.2}On parcourt les places par indice, car on a besoin du numéro de la place. "
        "{k3.3}Dès qu'une place vaut None, {k3.4}on y range le véhicule, {k3.5}et on renvoie son numéro. "
        "{k3.6}{k3.l6}Si la boucle se termine sans succès, le parking est plein : on renvoie moins un. Attention : ce return est après la boucle, pas dedans.",
        "{-k3}{ex2c.q4}{k4}{k4.1}Question quatre : sortir. {k4.2}On parcourt encore les places par indice. {k4.3}On note v la place courante.",
        "{k4.4}{k4.l4}Voici le piège : une place libre vaut None, et None point immat provoque une erreur. "
        "Il faut donc tester v is not None avant de regarder v point immat. Le and s'arrête au premier test faux.",
        "{k4.5}Si c'est le bon véhicule, on libère la place, {k4.6}et on renvoie True. {k4.7}{k4.l7}Sinon, après la boucle, False.",
        "{-k4}{ex2c.q5}{k5}Question cinq. On écrit v égale un véhicule, catégorie voiture, on le gare, puis on change v point catégorie en moto. "
        "Le véhicule garé est-il modifié ? {k5.1}Oui ! La liste des places contient une référence vers l'objet v, pas une copie. "
        "Modifier l'objet par v modifie le véhicule garé. C'est la mutation partagée.",
        "{-k5}{-ex2c}{meth}Pour finir, la méthode de l'écrit. {meth.1}Recopie la signature, avec self. {meth.2}Écris self point devant chaque attribut. "
        "{meth.3}Place le return d'échec après la boucle. {meth.4}Et quand une méthode existe déjà, réutilise-la : c'est souvent ce que l'énoncé attend.",
        "{-meth}",
    ], vis={
        "ex2": dict(type="exo", niveau="bac", etiquette="Exercice 3 · type bac", titre="Un parking",
                    enonce=["Un parking possède un nombre fixe de places, numérotées à partir de 0. Une place libre vaut `None`."],
                    questions=["Prédire l'affichage d'un programme.", "Écrire la méthode `est_plein(self)`.",
                               "Écrire `garer(self, vehicule)` : première place libre, renvoie son numéro, ou −1.",
                               "Écrire `sortir(self, immat)` : libère la place, renvoie True, ou False.",
                               "Le véhicule garé est-il modifié si l'on modifie `v` ensuite ?"]),
        "pk": dict(type="code", fichier="parking.py", instant=True, x=140, y=84, w=1000, taille=21, lignes=PARKING),
        "pa2": dict(type="pause", t="Les cinq questions, rédigées comme sur une copie."),
        "ex2c": dict(type="exo", mode="coin", niveau="bac", etiquette="Exercice 3 · type bac", titre="Un parking",
                     donnees=["`places` : liste, `None` = libre"],
                     questions=["prédire l'affichage", "`est_plein`", "`garer`", "`sortir`", "références"]),
        "k1": dict(type="code", fichier="question1.py", x=530, y=110, w=726, taille=18, lignes=PK_Q1, sortie="3 voiture None"),
        "k2": dict(type="code", fichier="parking.py", x=530, y=150, w=726, taille=23, lignes=PK_PLEIN),
        "k3": dict(type="code", fichier="parking.py", x=530, y=130, w=726, taille=22, lignes=PK_GARER),
        "k4": dict(type="code", fichier="parking.py", x=530, y=120, w=726, taille=21, lignes=PK_SORTIR),
        "k5": dict(type="def", terme="Mutation partagée", x=540, y=170, w=700,
                   t="Oui : `p.places` contient une **référence** vers l'objet `v`, pas une copie. Modifier l'objet par `v` modifie le véhicule garé."),
        "meth": dict(type="liste", titre="À l'écrit", items=[
            "Recopier la signature : `def garer(self, vehicule):`", "`self.` devant chaque attribut",
            "Le `return` d'échec **après** la boucle", "Réutiliser les méthodes existantes (`self.nb_libres()`)"],
            marques=["✓"] * 4, x=150, y=150, w=980),
    }),

    # ================================================================ XIII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", humeur="lumiere", beats=[
        "{carte}Récapitulons. {carte.1}Une classe est un plan ; un objet, une instance fabriquée à partir de ce plan. "
        "{carte.2}Le constructeur init crée les attributs, et self désigne l'objet sur lequel on travaille. "
        "{carte.3}Les méthodes modifient l'objet ou renvoient une valeur ; on protège les attributs avec des accesseurs. "
        "{carte.4}Et une variable contient une référence : b égale a crée un alias.",
        "{-carte}{sq}Voici le squelette à connaître par cœur. {sq.l1}Le nom de la classe, avec une majuscule. "
        "{sq.l2-4}Le constructeur, qui crée les attributs d'instance. {sq.l6-8}Une méthode, avec self en premier, "
        "qui modifie l'objet, ou renvoie une valeur. {sq.l10}Puis l'instanciation, {sq.l11}et l'appel. {sq.l0}{sq.s}Six, et deux.",
        "{-sq}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Écrire une classe : constructeur, attributs, méthodes. "
        "{bac.2}Accéder aux attributs et aux méthodes, depuis l'extérieur et depuis une autre méthode. "
        "{bac.3}Employer le vocabulaire juste : classe, objet, instance, attribut, méthode. "
        "{bac.4}Prédire l'effet des références et des alias. {bac.5}Et utiliser des classes pour construire une structure de données.",
        "Si tu sais faire ces cinq choses, ce chapitre est à toi. Les fiches, le QCM et les exercices du chapitre sont sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, un quiz sur cette vidéo t'y attend aussi.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="PROGRAMMATION OBJET", branches=[
            dict(t="Classe et objet", items=["classe = le plan", "objet = une instance", "`c = Compte(\"Ada\", 100)`"]),
            dict(t="Constructeur, self", items=["`__init__` crée les attributs", "self = l'objet", "`c.f(x)` ≡ `Compte.f(c, x)`"]),
            dict(t="Méthodes, accès", items=["modifier, renvoyer", "accesseur, mutateur", "`__str__` renvoie une chaîne"]),
            dict(t="Références", items=["`b = a` : un alias", "`is` : même objet", "effet de bord"])]),
        "sq": dict(type="code", titre="Le squelette à connaître", fichier="squelette.py", instant=True, x=120, y=110, w=1040, taille=21,
                   lignes=SQUELETTE, sortie="6 2"),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Écrire une classe : constructeur, attributs, méthodes", "Accéder aux attributs et aux méthodes",
            "Le vocabulaire : classe, objet, instance, attribut, méthode", "Prédire l'effet des références et des alias",
            "Construire une structure de données avec des classes"],
            marques=["✓"] * 5, x=140, y=110, w=1000),
    }),
]

QUIZ = [
    dict(q="Dans c = Compte(\"Ada\", 100), que désigne c ?", r=["La classe Compte", "Un objet (une instance) de la classe Compte", "Le constructeur"],
         ok=1, ex="Compte(…) crée une instance ; c contient une référence vers cet objet.", voir="mem1"),
    dict(q="Quel est le rôle de la méthode __init__ ?", r=["Afficher l'objet", "Initialiser les attributs de l'objet qui vient d'être créé", "Comparer deux objets"],
         ok=1, ex="Elle est appelée automatiquement à l'instanciation et crée les attributs avec self.x = …", voir="def_init"),
    dict(q="Quelle écriture est équivalente à c.deposer(5) ?", r=["deposer(c, 5)", "Compte.deposer(c, 5)", "c.deposer(c, 5)"],
         ok=1, ex="L'objet placé devant le point est passé comme premier argument : self reçoit c.", voir="self_code"),
    dict(q="Quelle définition de méthode est correcte ?", r=["def retirer(montant):", "def retirer(self, montant):", "def retirer(montant, self):"],
         ok=1, ex="self est toujours le premier paramètre d'une méthode.", voir="p1"),
    dict(q="a = Compte(\"Ada\", 10), puis b = a, puis b.deposer(5). Que vaut a.solde ?", r=["10", "15", "5"],
         ok=1, ex="b est un alias de a : un seul objet existe, il a été modifié.", voir="alc"),
    dict(q="Sans méthode __eq__, Compte(\"Ada\", 10) == Compte(\"Ada\", 10) vaut…", r=["True", "False", "une erreur"],
         ok=1, ex="Sans __eq__, == compare les identités : ce sont deux objets distincts.", voir="isq"),
    dict(q="Dans une méthode, solde = solde + 10 (sans self.) provoque…", r=["la modification de l'attribut", "une UnboundLocalError", "rien du tout"],
         ok=1, ex="Sans self., solde est une variable locale, lue avant d'avoir été définie.", voir="p2"),
    dict(q="Pourquoi éviter def __init__(self, membres=[]) ?", r=["C'est une erreur de syntaxe", "La même liste est partagée par tous les objets créés sans argument", "Les listes sont interdites comme attributs"],
         ok=1, ex="La valeur par défaut est créée une seule fois, à la définition de la méthode. On écrit membres=None, puis une nouvelle liste dans le corps.", voir="p4"),
    dict(q="Une fonction reçoit un objet et modifie l'un de ses attributs. Après l'appel…", r=["l'objet d'origine est modifié", "seule une copie a été modifiée", "l'attribut reprend sa valeur"],
         ok=0, ex="La fonction reçoit une référence vers le même objet : c'est un effet de bord.", voir="fo"),
    dict(q="Selon le programme de Terminale, quelle notion n'est pas exigible ?", r=["Les attributs", "L'héritage", "L'instanciation"],
         ok=1, ex="Le programme exclut explicitement l'héritage et le polymorphisme.", voir="her"),
]

CREDITS = [
    "Animations, schémas et programmes : faits pour le site (programmes exécutés avec Python 3). "
    "Polices : Space Grotesk, JetBrains Mono, Carnet Math (sous-ensemble de STIX Two Math), sous licence SIL OFL.",
]
