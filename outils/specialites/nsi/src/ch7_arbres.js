/* ===================== Chapitre 7 — Arbres binaires et arbres binaires de recherche ===================== */
C("c7-noeud", String.raw`
class Noeud:
    """Un nœud d'arbre binaire. L'arbre vide est représenté par None."""
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche      # sous-arbre gauche (un Noeud ou None)
        self.droit = droit        # sous-arbre droit  (un Noeud ou None)

#          A
#        /   \
#       B     C
#      / \     \
#     D   E     F
#        /
#       G
arbre = Noeud("A",
              Noeud("B", Noeud("D"), Noeud("E", Noeud("G"))),
              Noeud("C", None, Noeud("F")))

print(arbre.valeur, arbre.gauche.valeur, arbre.gauche.droit.gauche.valeur)
print(arbre.droit.gauche)`, { fichier: "arbre.py", out: "A B G\nNone" });

C("c7-mesures", String.raw`
def taille(a):
    """Nombre de nœuds."""
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    """Nombre de nœuds de la plus longue branche (arbre vide : 0, un seul nœud : 1)."""
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

def nb_feuilles(a):
    if a is None:
        return 0
    if a.gauche is None and a.droit is None:     # une feuille
        return 1
    return nb_feuilles(a.gauche) + nb_feuilles(a.droit)

print(taille(arbre), hauteur(arbre), nb_feuilles(arbre))`, { deps: ["c7-noeud"], out: "7 4 3" });

C("c7-parcours", String.raw`
def prefixe(a):            # racine, puis gauche, puis droit
    if a is None:
        return []
    return [a.valeur] + prefixe(a.gauche) + prefixe(a.droit)

def infixe(a):             # gauche, puis racine, puis droit
    if a is None:
        return []
    return infixe(a.gauche) + [a.valeur] + infixe(a.droit)

def suffixe(a):            # gauche, puis droit, puis racine
    if a is None:
        return []
    return suffixe(a.gauche) + suffixe(a.droit) + [a.valeur]

print("préfixe :", " ".join(prefixe(arbre)))
print("infixe  :", " ".join(infixe(arbre)))
print("suffixe :", " ".join(suffixe(arbre)))`, { deps: ["c7-noeud"], out: "préfixe : A B D E G C F\ninfixe  : D B G E A C F\nsuffixe : D G E B F C A" });

C("c7-largeur", String.raw`
def largeur(a):
    """Parcours en largeur : niveau par niveau, de gauche à droite, avec une FILE."""
    resultat = []
    file = []
    if a is not None:
        file.append(a)
    while file:                      # tant que la file n'est pas vide
        n = file.pop(0)              # défiler (coût linéaire ici ; deque serait mieux)
        resultat.append(n.valeur)
        if n.gauche is not None:
            file.append(n.gauche)    # enfiler les enfants
        if n.droit is not None:
            file.append(n.droit)
    return resultat

print(" ".join(largeur(arbre)))`, { deps: ["c7-noeud"], out: "A B C D E F G" });

C("c7-expression", String.raw`
#        *
#      /   \
#     +     -
#    / \   / \
#   3   4 6   1
expr = Noeud("*", Noeud("+", Noeud(3), Noeud(4)), Noeud("-", Noeud(6), Noeud(1)))

def evaluer(a):
    if a.gauche is None and a.droit is None:      # une feuille : un nombre
        return a.valeur
    g, d = evaluer(a.gauche), evaluer(a.droit)    # on évalue d'abord les deux côtés
    if a.valeur == "+":
        return g + d
    if a.valeur == "-":
        return g - d
    return g * d

def infixe_parenthese(a):
    if a.gauche is None and a.droit is None:
        return str(a.valeur)
    return "(" + infixe_parenthese(a.gauche) + " " + a.valeur + " " + infixe_parenthese(a.droit) + ")"

print(infixe_parenthese(expr), "=", evaluer(expr))
print(" ".join(str(v) for v in suffixe(expr)))     # la notation polonaise inverse !`, { deps: ["c7-noeud", "c7-parcours"], out: "((3 + 4) * (6 - 1)) = 35\n3 4 + 6 1 - *" });

C("c7-abr", String.raw`
def inserer(a, cle):
    """Insère cle dans l'ABR a et renvoie l'arbre obtenu (les doublons vont à droite)."""
    if a is None:
        return Noeud(cle)                     # place libre trouvée : nouvelle feuille
    if cle < a.valeur:
        a.gauche = inserer(a.gauche, cle)
    else:
        a.droit = inserer(a.droit, cle)
    return a

def rechercher(a, cle):
    """True si cle est dans l'ABR a. On ne descend que d'UN côté à chaque étape."""
    while a is not None:
        if cle == a.valeur:
            return True
        if cle < a.valeur:
            a = a.gauche
        else:
            a = a.droit
    return False

abr = None
for cle in [50, 30, 70, 20, 40, 60, 80, 35]:
    abr = inserer(abr, cle)
print(infixe(abr))                      # parcours infixe d'un ABR : les clés triées
print(rechercher(abr, 35), rechercher(abr, 65), hauteur(abr))`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours"], out: "[20, 30, 35, 40, 50, 60, 70, 80]\nTrue False 4" });

C("c7-minimum", String.raw`
def minimum(a):
    """Plus petite clé d'un ABR non vide : on descend toujours à gauche."""
    while a.gauche is not None:
        a = a.gauche
    return a.valeur

print(minimum(abr))`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours", "c7-abr"], out: "20" });

C("c7-degenere", String.raw`
peigne = None
for cle in [1, 2, 3, 4, 5, 6, 7]:          # clés insérées dans l'ordre croissant
    peigne = inserer(peigne, cle)
equilibre = None
for cle in [4, 2, 6, 1, 3, 5, 7]:          # mêmes clés, autre ordre
    equilibre = inserer(equilibre, cle)
print(hauteur(peigne), hauteur(equilibre))`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours", "c7-abr"], out: "7 3" });

C("c7-encadrement", String.raw`
from math import log2, ceil

for n in [7, 1000, 1_000_000]:
    h_min = ceil(log2(n + 1))       # arbre le plus « tassé » possible
    print(n, "nœuds : hauteur entre", h_min, "et", n)`, { out: "7 nœuds : hauteur entre 3 et 7\n1000 nœuds : hauteur entre 10 et 1000\n1000000 nœuds : hauteur entre 20 et 1000000" });

C("c7-classe", String.raw`
class ABR:
    """Un ABR vu comme un objet : l'utilisateur ne manipule pas les nœuds."""
    def __init__(self):
        self.racine = None
        self.nb = 0

    def ajouter(self, cle):
        self.racine = inserer(self.racine, cle)
        self.nb = self.nb + 1

    def contient(self, cle):
        return rechercher(self.racine, cle)

    def trie(self):
        return infixe(self.racine)

annuaire = ABR()
for nom in ["Lovelace", "Turing", "Hopper", "Knuth"]:
    annuaire.ajouter(nom)
print(annuaire.trie(), annuaire.contient("Hopper"), annuaire.nb)`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours", "c7-abr"], out: "['Hopper', 'Knuth', 'Lovelace', 'Turing'] True 4" });

/* pièges */
C("c7-p-vide", String.raw`
def taille_fausse(a):
    return 1 + taille_fausse(a.gauche) + taille_fausse(a.droit)   # cas None oublié

taille_fausse(Noeud("A"))`, { deps: ["c7-noeud"], err: "AttributeError: 'NoneType' object has no attribute 'gauche'" });

C("c7-p-insertion", String.raw`
def inserer_faux(a, cle):
    if a is None:
        return Noeud(cle)
    if cle < a.valeur:
        inserer_faux(a.gauche, cle)       # le nouveau nœud n'est rattaché à rien
    else:
        inserer_faux(a.droit, cle)
    return a

r = Noeud(50)
inserer_faux(r, 30)
print(r.gauche)`, { deps: ["c7-noeud"], out: "None" });

/* prédis la sortie */
C("c7-x1", String.raw`
t = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), Noeud(6)))
print(prefixe(t), suffixe(t))`, { deps: ["c7-noeud", "c7-parcours"], out: "[1, 2, 4, 3, 5, 6] [4, 2, 5, 6, 3, 1]" });

C("c7-x2", String.raw`
t = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), Noeud(6)))
print(taille(t), hauteur(t), nb_feuilles(t))`, { deps: ["c7-noeud", "c7-mesures"], out: "6 3 3" });

C("c7-x3", String.raw`
def mystere(a):
    if a is None:
        return 0
    return a.valeur + mystere(a.gauche) + mystere(a.droit)

t = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), Noeud(6)))
print(mystere(t), mystere(t.gauche))`, { deps: ["c7-noeud"], out: "21 6" });

C("c7-x4", String.raw`
r = None
for cle in [8, 3, 10, 1, 6, 14, 4]:
    r = inserer(r, cle)
print(infixe(r), r.gauche.droit.valeur, hauteur(r))`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours", "c7-abr"], out: "[1, 3, 4, 6, 8, 10, 14] 6 4" });

/* épreuve pratique 1 */
C("c7-ep1-fourni", String.raw`
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def taille(a):
    """Nombre de nœuds de l'arbre a (None pour l'arbre vide)."""
    ...

def hauteur(a):
    """Hauteur : 0 pour l'arbre vide, 1 pour un arbre réduit à sa racine."""
    ...

def nb_feuilles(a):
    """Nombre de feuilles (nœuds sans enfant)."""
    if a is None:
        return 0
    if a.gauche is None or a.droit is None:
        return 1
    return nb_feuilles(a.gauche) + nb_feuilles(a.droit)`, { fichier: "mesures.py", run: false, trous: [9, 13] });

C("c7-ep1-corr", String.raw`
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

def nb_feuilles(a):
    if a is None:
        return 0
    if a.gauche is None and a.droit is None:     # and, pas or
        return 1
    return nb_feuilles(a.gauche) + nb_feuilles(a.droit)

def est_parfait(a):
    """Tous les niveaux sont remplis : taille = 2**hauteur - 1."""
    return taille(a) == 2 ** hauteur(a) - 1

def test():
    peigne = Noeud(1, Noeud(2, Noeud(3)))         # 1 -> 2 -> 3 à gauche
    t = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), Noeud(6)))
    assert taille(None) == 0 and hauteur(None) == 0 and nb_feuilles(None) == 0
    assert taille(Noeud(9)) == 1 and hauteur(Noeud(9)) == 1 and nb_feuilles(Noeud(9)) == 1
    assert taille(t) == 6 and hauteur(t) == 3 and nb_feuilles(t) == 3
    assert nb_feuilles(peigne) == 1 and hauteur(peigne) == 3
    assert nb_feuilles(Noeud(1, Noeud(2, Noeud(3), Noeud(4)))) == 2   # le cas qui piégeait or
    assert not est_parfait(t) and est_parfait(Noeud(1, Noeud(2), Noeud(3)))

test()
print("tous les tests passent")`, { fichier: "mesures.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c7-ep2-fourni", String.raw`
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def inserer(a, cle):
    """Insère cle dans l'ABR a (sans doublon) et renvoie l'arbre obtenu."""
    if a is None:
        Noeud(cle)
    elif cle < a.valeur:
        a.gauche = inserer(a.gauche, cle)
    elif cle > a.valeur:
        a.droit = inserer(a.droit, cle)
    return a

def rechercher(a, cle):
    """True si cle est présente dans l'ABR a."""
    ...`, { fichier: "abr.py", run: false, trous: [19] });

C("c7-ep2-corr", String.raw`
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def inserer(a, cle):
    if a is None:
        return Noeud(cle)                 # le return manquait
    elif cle < a.valeur:
        a.gauche = inserer(a.gauche, cle)
    elif cle > a.valeur:
        a.droit = inserer(a.droit, cle)
    return a

def rechercher(a, cle):
    if a is None:
        return False
    if cle == a.valeur:
        return True
    if cle < a.valeur:
        return rechercher(a.gauche, cle)
    return rechercher(a.droit, cle)

def maximum(a):
    while a.droit is not None:
        a = a.droit
    return a.valeur

def test():
    r = None
    assert not rechercher(r, 5)                  # arbre vide
    for c in [41, 20, 65, 11, 29, 50, 91, 32]:
        r = inserer(r, c)
    assert all(rechercher(r, c) for c in [41, 20, 65, 11, 29, 50, 91, 32])
    assert not rechercher(r, 30) and not rechercher(r, 100)
    assert maximum(r) == 91
    r = inserer(r, 29)                           # doublon : rien ne change
    assert r.gauche.droit.valeur == 29 and r.gauche.droit.gauche is None

test()
print("tous les tests passent")`, { fichier: "abr.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c7-ecrit-corr", String.raw`
def evaluer(a):
    if a.gauche is None and a.droit is None:
        return a.valeur
    g = evaluer(a.gauche)
    d = evaluer(a.droit)
    if a.valeur == "+":
        return g + d
    elif a.valeur == "-":
        return g - d
    elif a.valeur == "*":
        return g * d
    return g / d

def nb_operations(a):
    if a is None or (a.gauche is None and a.droit is None):
        return 0
    return 1 + nb_operations(a.gauche) + nb_operations(a.droit)

e = Noeud("-", Noeud("*", Noeud(2), Noeud("+", Noeud(5), Noeud(3))), Noeud(4))
print(prefixe(e))
print(suffixe(e))
print(evaluer(e), nb_operations(e), hauteur(e))`, { deps: ["c7-noeud", "c7-mesures", "c7-parcours"], out: "['-', '*', 2, '+', 5, 3, 4]\n[2, 5, 3, '+', '*', 4, '-']\n12 3 4" });

C("c7-retenir", String.raw`
def f(a):                       # schéma de presque toutes les fonctions sur les arbres
    if a is None:               # cas de base : l'arbre vide
        return ...
    g = f(a.gauche)             # appel récursif à gauche
    d = f(a.droit)              # appel récursif à droite
    return ...                  # combinaison avec a.valeur`, { run: false });

/* ---------- dessin d'arbre commun aux deux animations ---------- */
function arbreSVG(racine, et, opts) {
  opts = opts || {};
  var pos = {}, i = 0, prof = 0, W = 54, H = 58;
  (function place(n, d) { if (!n) return; place(n.g, d + 1); pos[n.v] = { x: i++, y: d }; prof = Math.max(prof, d); place(n.d, d + 1); })(racine, 0);
  var larg = Math.max(i * W, 200), haut = (prof + 1) * H + 20;
  var s = '<svg class="arbre-svg" viewBox="0 0 ' + larg + " " + haut + '" style="max-width:' + Math.max(larg, 260) + 'px" role="img" aria-label="Arbre binaire">';
  (function aretes(n) {
    if (!n) return;
    [n.g, n.d].forEach(function (f) { if (f) { var a = pos[n.v], b = pos[f.v]; s += '<line class="ar" x1="' + (a.x * W + W / 2) + '" y1="' + (a.y * H + 26) + '" x2="' + (b.x * W + W / 2) + '" y2="' + (b.y * H + 26) + '"/>'; } });
    aretes(n.g); aretes(n.d);
  })(racine);
  Object.keys(pos).forEach(function (v) {
    var p = pos[v], e = et[v] || "", x = p.x * W + W / 2, y = p.y * H + 26;
    s += '<g class="nd-a ' + e + '"><circle cx="' + x + '" cy="' + y + '" r="18"/><text x="' + x + '" y="' + (y + 5) + '" text-anchor="middle">' + v + "</text>" +
      (opts.rang && opts.rang[v] ? '<text class="rang" x="' + (x + 16) + '" y="' + (y - 14) + '">' + opts.rang[v] + "</text>" : "") + "</g>";
  });
  return s + "</svg>";
}
function arbreJS(n) { return n ? { v: n[0], g: arbreJS(n[1]), d: arbreJS(n[2]) } : null; }

/* ---------- animation : les quatre parcours ---------- */
WIDGETS_EXT["parcours-arbre"] = function (z, opt, O) {
  var R = arbreJS(["A", ["B", ["D"], ["E", ["G"]]], ["C", null, ["F"]]]);
  var NOMS = { pre: "préfixe", inf: "infixe", suf: "suffixe", larg: "en largeur" };
  function etapes(k) {
    var E = [], et = {}, sortie = [], rang = {};
    function snap(msg, pile, file) { E.push({ et: JSON.parse(JSON.stringify(et)), sortie: sortie.slice(), rang: JSON.parse(JSON.stringify(rang)), pile: pile ? pile.slice() : null, file: file ? file.slice() : null, msg: msg }); }
    function traite(n) { sortie.push(n.v); rang[n.v] = sortie.length; et[n.v] = "traite"; }
    if (k === "larg") {
      var file = [R];
      snap("Parcours <b>en largeur</b> : on utilise une <b>file</b>. Au départ, elle contient la racine.", null, file.map(function (n) { return n.v; }));
      while (file.length) {
        var n = file.shift();
        traite(n);
        var enf = [n.g, n.d].filter(Boolean);
        enf.forEach(function (f) { file.push(f); et[f.v] = "attente"; });
        snap("On <b>défile</b> " + n.v + " et on le traite" + (enf.length ? " ; on <b>enfile</b> " + (enf.length > 1 ? "ses enfants " : "son enfant ") + enf.map(function (f) { return f.v; }).join(" et ") + " (à la queue)." : " ; il n’a pas d’enfant."), null, file.map(function (x) { return x.v; }));
      }
      snap("File vide : fin. Ordre <b>" + sortie.join(" ") + "</b> : niveau par niveau, de gauche à droite.", null, []);
      return E;
    }
    var pile = [];
    snap("Parcours en profondeur <b>" + NOMS[k] + "</b>, écrit récursivement : chaque appel est empilé sur la <b>pile d’exécution</b> (chapitre 2). " + (k === "pre" ? "On traite la racine <b>avant</b> ses deux sous-arbres." : k === "inf" ? "On traite la racine <b>entre</b> le sous-arbre gauche et le droit." : "On traite la racine <b>après</b> ses deux sous-arbres."), pile);
    (function dfs(n) {
      pile.push(n.v); et[n.v] = et[n.v] === "traite" ? "traite" : "actif";
      snap("Appel sur le nœud <b>" + n.v + "</b>.", pile);
      if (k === "pre") { traite(n); snap("Préfixe : on traite <b>" + n.v + "</b> tout de suite.", pile); }
      if (n.g) { if (et[n.v] !== "traite") et[n.v] = "attente"; dfs(n.g); if (et[n.v] !== "traite") et[n.v] = "actif"; }
      if (k === "inf") { traite(n); snap("Le sous-arbre gauche de " + n.v + " est fini : infixe, on traite <b>" + n.v + "</b> maintenant.", pile); }
      if (n.d) { if (et[n.v] !== "traite") et[n.v] = "attente"; dfs(n.d); if (et[n.v] !== "traite") et[n.v] = "actif"; }
      if (k === "suf") { traite(n); snap("Les deux sous-arbres de " + n.v + " sont finis : suffixe, on traite <b>" + n.v + "</b>.", pile); }
      pile.pop();
    })(R);
    snap("Pile vide : fin. Ordre " + NOMS[k] + " : <b>" + sortie.join(" ") + "</b>.", pile);
    return E;
  }
  function dessine(sc, e) {
    var h = '<div class="parc">' + arbreSVG(R, e.et, { rang: e.rang }) + '<div class="parc-cote">';
    if (e.pile) h += '<div class="titre-pile">pile d’appels (sommet en haut)</div><div class="mini-pile">' + (e.pile.length ? e.pile.slice().reverse().map(function (v, i) { return '<span class="puce' + (i === 0 ? " vu" : "") + '">parcours(' + v + ")</span>"; }).join("") : '<span class="repere">vide</span>') + "</div>";
    if (e.file) h += '<div class="titre-pile">file (tête à gauche)</div><div class="mini-file">' + (e.file.length ? e.file.map(function (v) { return '<span class="puce">' + v + "</span>"; }).join("") : '<span class="repere">vide</span>') + "</div>";
    h += '<div class="titre-pile">sortie</div><div class="sortie-p mono">' + (e.sortie.join(" ") || "…") + "</div></div></div>";
    sc.innerHTML = h;
  }
  O.lecteur(z, { titre: "parcours d’un arbre binaire", choix: [{ k: "pre", t: "préfixe" }, { k: "inf", t: "infixe" }, { k: "suf", t: "suffixe" }, { k: "larg", t: "en largeur" }], etapes: etapes, dessine: dessine, vitesse: 1300 });
};

/* ---------- animation : ABR, insertion et recherche ---------- */
WIDGETS_EXT["abr"] = function (z, opt, O) {
  function ins(r, k) { if (!r) return { v: k, g: null, d: null }; if (k < r.v) r.g = ins(r.g, k); else r.d = ins(r.d, k); return r; }
  function clone(r) { return r ? { v: r.v, g: clone(r.g), d: clone(r.d) } : null; }
  function haut(r) { return r ? 1 + Math.max(haut(r.g), haut(r.d)) : 0; }
  function etapes(k) {
    var E = [], r = null, cles;
    function snap(msg, et) { E.push({ r: clone(r), et: et || {}, msg: msg }); }
    if (k === "inserer" || k === "peigne") {
      cles = k === "inserer" ? [50, 30, 70, 20, 40, 60, 80, 35] : [1, 2, 3, 4, 5, 6, 7];
      snap("On insère, dans cet ordre : <b>" + cles.join(", ") + "</b>. Règle de l’ABR : plus petit à gauche, plus grand (ou égal) à droite.");
      cles.forEach(function (c) {
        var n = r, chemin = {};
        while (n) {
          chemin[n.v] = "vu";
          snap("Insérer <b>" + c + "</b> : on compare à " + n.v + " → " + (c < n.v ? c + " &lt; " + n.v + ", on descend à <b>gauche</b>." : c + " ≥ " + n.v + ", on descend à <b>droite</b>."), JSON.parse(JSON.stringify(chemin)));
          n = c < n.v ? n.g : n.d;
        }
        r = ins(r, c); chemin[c] = "neuf";
        snap("Place vide : <b>" + c + "</b> devient une nouvelle feuille.", chemin);
      });
      snap(k === "inserer" ? "8 clés, hauteur <b>" + haut(r) + "</b>. Le parcours infixe donne les clés triées : 20 30 35 40 50 60 70 80." : "Clés insérées dans l’ordre croissant : l’arbre est un « peigne » de hauteur <b>7</b> (autant que de clés). Rechercher 7 coûte 7 comparaisons, comme dans une liste. Avec l’ordre 4, 2, 6, 1, 3, 5, 7, la hauteur serait 3.");
      return E;
    }
    [50, 30, 70, 20, 40, 60, 80, 35].forEach(function (c) { r = ins(r, c); });
    var cle = k === "chercher" ? 35 : 65, n = r, chemin = {}, nb = 0;
    snap("On cherche <b>" + cle + "</b>. À chaque nœud, une comparaison suffit pour savoir de quel côté continuer.");
    while (n) {
      nb++;
      if (cle === n.v) { chemin[n.v] = "neuf"; snap("Comparaison " + nb + " : " + cle + " = " + n.v + ". <b>Trouvé</b> en " + nb + " comparaisons (la hauteur de l’arbre est " + haut(r) + ").", chemin); return E; }
      chemin[n.v] = "vu";
      snap("Comparaison " + nb + " : " + cle + (cle < n.v ? " &lt; " : " &gt; ") + n.v + " → à " + (cle < n.v ? "gauche" : "droite") + ". Tout l’autre sous-arbre est écarté.", chemin);
      n = cle < n.v ? n.g : n.d;
    }
    snap("On tombe sur un sous-arbre vide : <b>" + cle + " n’est pas dans l’arbre</b>, après " + nb + " comparaisons. Au plus autant de comparaisons que la hauteur.", chemin);
    return E;
  }
  function dessine(sc, e) { sc.innerHTML = e.r ? arbreSVG(e.r, e.et) : '<div class="repere" style="padding:30px">arbre vide (None)</div>'; }
  O.lecteur(z, { titre: "arbre binaire de recherche", choix: [{ k: "inserer", t: "insérer 8 clés" }, { k: "chercher", t: "chercher 35" }, { k: "absente", t: "chercher 65" }, { k: "peigne", t: "insérer 1…7 dans l’ordre" }], etapes: etapes, dessine: dessine, vitesse: 1200 });
};

CH.push({
  id: "ch7", n: 7, court: "arbres", fichier: "ch7_arbres.py",
  titre: "Arbres binaires et arbres binaires de recherche",
  rubrique: "Rubriques « Structures de données » (arbres : structures hiérarchiques) et « Algorithmique » (algorithmes sur les arbres binaires et les ABR)",
  accroche: "Vocabulaire, taille et hauteur, parcours préfixe / infixe / suffixe / en largeur, arbres binaires de recherche : recherche et insertion.",
  essentiel: [
    "Un <b>arbre</b> est une structure hiérarchique : une <b>racine</b>, des nœuds reliés à leurs <b>enfants</b>, des <b>feuilles</b> sans enfant.",
    "Un <b>arbre binaire</b> est vide, ou formé d’un nœud (sa racine) et de deux arbres binaires : ses sous-arbres <b>gauche</b> et <b>droit</b>. La définition est récursive, les algorithmes aussi.",
    "<b>Taille</b> : nombre de nœuds. <b>Hauteur</b> : nombre de nœuds de la plus longue branche (vérifie la convention de l’énoncé). Pour un arbre binaire : <i>h</i> ≤ <i>n</i> ≤ 2<sup><i>h</i></sup> − 1.",
    "Parcours en profondeur : <b>préfixe</b> (racine, G, D), <b>infixe</b> (G, racine, D), <b>suffixe</b> (G, D, racine). Parcours <b>en largeur</b> : niveau par niveau, avec une <b>file</b>.",
    "Dans un <b>ABR</b>, chaque clé est plus grande que celles de son sous-arbre gauche et plus petite que celles du droit : recherche et insertion coûtent au plus la hauteur, soit environ log₂ <i>n</i> si l’arbre est équilibré."
  ],
  attendus: [
    "Identifier des situations nécessitant une structure arborescente ; employer le vocabulaire : nœud, racine, feuille, sous-arbre gauche, sous-arbre droit.",
    "Évaluer quelques mesures des arbres binaires : taille, hauteur, encadrement de la hauteur.",
    "Calculer la taille et la hauteur d’un arbre ; parcourir un arbre de différentes façons (préfixe, infixe, suffixe ; en largeur d’abord).",
    "Rechercher une clé dans un arbre binaire de recherche, insérer une clé. Savoir que la recherche dans un ABR équilibré est de coût logarithmique.",
    "Utiliser une structure récursive adaptée et la programmation par classe (le BO cite les arbres comme exemple)."
  ],
  idees: [
    { id: "i1", t: "Des données hiérarchiques", h: `
<p>Les listes, piles et files rangent les données en ligne. Beaucoup de données sont <b>hiérarchiques</b> : un élément « contient » ou « commande » plusieurs autres.</p>
<ul><li>l’arborescence des fichiers : un dossier contient des fichiers et des sous-dossiers ;</li>
<li>une page web : la balise <code>&lt;html&gt;</code> contient <code>&lt;head&gt;</code> et <code>&lt;body&gt;</code>, qui contiennent d’autres balises (le DOM) ;</li>
<li>un tableau de tournoi (quarts, demies, finale), un arbre généalogique ;</li>
<li>une expression arithmétique : dans (3 + 4) × (6 − 1), la multiplication porte sur deux sous-expressions.</li></ul>
<div class="boite def"><div class="lab">"""vocabulaire"""</div><p>Un <b>arbre</b> est formé de <b>nœuds</b> reliés par des <b>arêtes</b>. Le nœud du haut est la <b>racine</b>. Chaque nœud (sauf la racine) a un unique <b>parent</b> ; ses <b>enfants</b> sont les nœuds qui lui sont reliés en dessous. Un nœud sans enfant est une <b>feuille</b>. Une <b>branche</b> est un chemin de la racine à une feuille.</p></div>` },

    { id: "i2", t: "L’arbre binaire, une structure récursive", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>arbre binaire</b> est soit <b>vide</b>, soit formé d’un nœud, la <b>racine</b>, qui porte une valeur, et de deux arbres binaires : le <b>sous-arbre gauche</b> et le <b>sous-arbre droit</b>. Chaque nœud a donc au plus deux enfants, et on distingue gauche et droit.</p></div>
<p>En Python, on représente un nœud par un objet (chapitre 1) dont deux attributs référencent les sous-arbres, et l’arbre vide par <code>None</code>, exactement comme le maillon d’une liste chaînée (chapitre 3), mais avec deux « suivants ».</p>
[[c7-noeud]]
<p>Cet arbre sert d’exemple dans tout le chapitre : racine A ; feuilles D, G et F ; le sous-arbre gauche de A a pour racine B.</p>` },

    { id: "i3", t: "Mesurer un arbre : taille et hauteur", h: `
<p>La <b>taille</b> est le nombre de nœuds. La <b>hauteur</b> est le nombre de nœuds de la plus longue branche. Les deux se calculent par la même idée récursive : une réponse pour l’arbre vide, puis une combinaison des réponses des deux sous-arbres.</p>
[[c7-mesures]]
<div class="boite attention"><div class="lab">⚠ deux conventions pour la hauteur</div><p>Ici : arbre vide → 0, arbre réduit à sa racine → 1 (on compte les nœuds). Certains sujets comptent les <b>arêtes</b> : racine seule → 0 et arbre vide → −1. La différence est toujours de 1. <b>Lis la définition donnée par l’énoncé</b> et applique-la.</p></div>
<p><b>Encadrement</b> (convention « nœuds ») : un arbre binaire de hauteur <i>h</i> a au moins <i>h</i> nœuds (un « peigne », une seule branche) et au plus 2<sup><i>h</i></sup> − 1 nœuds (tous les niveaux pleins : 1 + 2 + 4 + … + 2<sup><i>h</i>−1</sup>). Inversement, avec <i>n</i> nœuds, la hauteur est comprise entre ⌈log₂(<i>n</i> + 1)⌉ et <i>n</i>.</p>
[[c7-encadrement]]` },

    { id: "i4", t: "Les trois parcours en profondeur", h: `
<p>Parcourir un arbre, c’est visiter chaque nœud une fois. En profondeur, on explore entièrement un sous-arbre avant l’autre ; la seule question est de savoir <b>quand</b> on traite la racine :</p>
<div class="tab-wrap"><table><tr><th>parcours</th><th>ordre</th><th>sur l’arbre exemple</th></tr>
<tr><td>préfixe</td><td>racine, gauche, droit</td><td><code>A B D E G C F</code></td></tr>
<tr><td>infixe</td><td>gauche, racine, droit</td><td><code>D B G E A C F</code></td></tr>
<tr><td>suffixe (ou postfixe)</td><td>gauche, droit, racine</td><td><code>D G E B F C A</code></td></tr></table></div>
[[c7-parcours]]
<p>Choisis un parcours et avance pas à pas : les appels s’empilent comme au chapitre 2, et le numéro d’ordre s’affiche sur chaque nœud traité.</p>
[[w-parcours-arbre]]
<p>Astuce pour l’écrit : fais le tour de l’arbre en longeant les nœuds par la gauche ; le préfixe note un nœud quand on passe <b>à sa gauche</b>, l’infixe quand on passe <b>dessous</b>, le suffixe quand on passe <b>à sa droite</b>.</p>` },

    { id: "i5", t: "Le parcours en largeur, avec une file", h: `
<p>Le parcours <b>en largeur</b> visite les nœuds <b>niveau par niveau</b>, de gauche à droite : A, puis B et C, puis D, E et F, puis G. Il n’est pas récursif : il utilise une <b>file</b> (chapitre 3). On enfile la racine ; tant que la file n’est pas vide, on défile un nœud, on le traite et on enfile ses enfants.</p>
[[c7-largeur]]
<p>Pourquoi une file ? Les enfants d’un nœud passent <b>après</b> tous les nœuds déjà en attente, donc après le reste du niveau courant. Avec une <b>pile</b> à la place de la file, on obtiendrait un parcours en profondeur. Le même schéma servira pour les graphes (chapitre 8). Dans l’animation ci-dessus, choisis « en largeur » pour voir la file évoluer.</p>` },

    { id: "i6", t: "Un exemple d’utilisation : les arbres d’expressions", h: `
<p>Une expression arithmétique se représente par un arbre dont les feuilles sont les nombres et les nœuds internes les opérations. Pour l’évaluer, on évalue d’abord les deux sous-arbres, puis on applique l’opération : c’est un parcours <b>suffixe</b>.</p>
[[c7-expression]]
<p>Le parcours suffixe écrit l’expression en <b>notation polonaise inverse</b>, celle que l’on évalue avec une pile (chapitre 3). Le parcours infixe, avec des parenthèses, redonne l’écriture habituelle. Les compilateurs et les calculatrices utilisent ce genre d’arbre pour analyser les expressions.</p>` },

    { id: "i7", t: "L’arbre binaire de recherche (ABR)", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>arbre binaire de recherche</b> est un arbre binaire dont les nœuds portent des <b>clés</b> comparables, tel que, pour chaque nœud, toutes les clés de son sous-arbre gauche sont <b>inférieures</b> à sa clé et toutes celles de son sous-arbre droit sont <b>supérieures</b> (les doublons sont soit interdits, soit placés d’un côté choisi, ici à droite).</p></div>
<p>Conséquence : le parcours <b>infixe</b> d’un ABR donne ses clés <b>dans l’ordre croissant</b>. Pour <b>rechercher</b> une clé, on la compare à la racine : égale, trouvée ; plus petite, on continue à gauche ; plus grande, à droite. Pour <b>insérer</b>, on descend de la même façon jusqu’à une place vide, où l’on crée une feuille.</p>
[[c7-abr]]
[[w-abr]]
<p>La plus petite clé est tout en bas à gauche :</p>
[[c7-minimum]]` },

    { id: "i8", t: "Coût : tout dépend de la hauteur", h: `
<p>Recherche et insertion suivent <b>une seule branche</b> : elles font au plus <i>h</i> comparaisons, où <i>h</i> est la hauteur. Si l’arbre est <b>équilibré</b> (tous les niveaux presque pleins), <i>h</i> vaut environ log₂ <i>n</i> : une vingtaine de comparaisons pour un million de clés, comme la recherche dichotomique. Mais l’arbre dépend de l’<b>ordre d’insertion</b> : des clés insérées déjà triées donnent un « peigne » de hauteur <i>n</i>, et la recherche redevient linéaire.</p>
[[c7-degenere]]
<div class="boite hp"><div class="lab"># pour aller plus loin : les arbres équilibrés</div><p>Les arbres AVL (Adelson-Velsky et Landis, 1962) ou rouge-noir se rééquilibrent à chaque insertion par des « rotations », pour garantir une hauteur de l’ordre de log₂ <i>n</i>. Les index des bases de données (chapitre 6) utilisent des arbres équilibrés de la famille des B-arbres.</p></div>` },

    { id: "i9", t: "Programmer par classe : un ABR comme objet", h: `
<p>Le programme cite les arbres comme exemple de programmation par classe. On peut cacher les nœuds derrière une classe qui offre une interface simple (ajouter, contient, trie) : c’est la séparation interface / implémentation du chapitre 3.</p>
[[c7-classe]]
<p>Les chaînes se comparent dans l’ordre alphabétique (plus précisément, l’ordre des codes des caractères) : le parcours infixe les renvoie triées. Un ABR peut ainsi servir de dictionnaire <b>ordonné</b>, ce que le dictionnaire de Python (chapitre 5) ne fait pas.</p>` }
  ],
  pieges: [
    { t: "Oublier le cas de l’arbre vide", h: `[[c7-p-vide]]<p>Toute fonction récursive sur un arbre commence par <code>if a is None:</code>. Les sous-arbres des feuilles sont vides : sans ce cas, on finit toujours par écrire <code>None.gauche</code>.</p>` },
    { t: "Ne pas rattacher le nœud inséré", h: `[[c7-p-insertion]]<p>La fonction renvoie le sous-arbre modifié : il faut l’affecter, <code>a.gauche = inserer(a.gauche, cle)</code>, et écrire <code>abr = inserer(abr, cle)</code> à l’appel (l’arbre vide devient un nœud).</p>` },
    { t: "Se tromper de convention pour la hauteur", h: `<p>Nœuds ou arêtes ? Arbre réduit à sa racine : 1 ou 0 ? Relis la définition de l’énoncé ; l’encadrement <i>h</i> ≤ <i>n</i> ≤ 2<sup><i>h</i></sup> − 1 devient <i>h</i> + 1 ≤ <i>n</i> ≤ 2<sup><i>h</i>+1</sup> − 1 si l’on compte les arêtes.</p>` },
    { t: "Croire que l’infixe donne toujours un ordre trié", h: `<p>Seulement pour un ABR. Sur l’arbre exemple, l’infixe donne D B G E A C F, qui n’est pas trié.</p>` },
    { t: "Vérifier un ABR seulement localement", h: `<p>Comparer chaque nœud à ses deux enfants ne suffit pas : toute la partie gauche doit être inférieure à la racine. L’arbre 50 → gauche 30 → droit 60 respecte la règle localement mais 60 est à gauche de 50 : ce n’est pas un ABR.</p>` },
    { t: "Utiliser une pile pour le parcours en largeur", h: `<p>Une pile fait ressortir les derniers nœuds ajoutés : on obtient un parcours en profondeur. Le parcours en largeur exige une file (premier entré, premier sorti).</p>` }
  ],
  retenir: `
<h2>Vocabulaire et mesures</h2>
<div class="tab-wrap"><table><tr><th>mot</th><th>sens</th></tr>
<tr><td>racine, nœud, feuille</td><td>nœud sans parent ; élément de l’arbre ; nœud sans enfant</td></tr>
<tr><td>arbre binaire</td><td>vide, ou racine + sous-arbre gauche + sous-arbre droit</td></tr>
<tr><td>taille</td><td>nombre de nœuds</td></tr>
<tr><td>hauteur</td><td>nœuds de la plus longue branche (ou arêtes : lire l’énoncé)</td></tr>
<tr><td>encadrement</td><td><i>h</i> ≤ <i>n</i> ≤ 2<sup><i>h</i></sup> − 1 ; ⌈log₂(<i>n</i>+1)⌉ ≤ <i>h</i> ≤ <i>n</i></td></tr>
<tr><td>ABR</td><td>à gauche plus petit, à droite plus grand, pour <b>chaque</b> nœud</td></tr></table></div>
<h2>Le schéma récursif</h2>
[[c7-retenir]]
<h2>Parcours</h2>
<ul><li>Préfixe : R G D · Infixe : G R D · Suffixe : G D R (récursifs, une pile cachée).</li><li>En largeur : une <b>file</b> ; défiler, traiter, enfiler les enfants.</li><li>Infixe d’un ABR = clés triées. Suffixe d’un arbre d’expression = notation polonaise inverse.</li></ul>
<h2>Coûts dans un ABR</h2>
<p>Recherche, insertion : au plus <i>h</i> comparaisons. Équilibré : ≈ log₂ <i>n</i>. Dégénéré (clés insérées triées) : <i>n</i>.</p>`,
  predis: [
    { code: "c7-x1", niv: "moyen", q: "Dessine d’abord l’arbre <code>t</code>.", rep: "Racine 1 ; à gauche 2 (qui n’a qu’un enfant droit, 4) ; à droite 3 (enfants 5 et 6). Préfixe : 1, 2, 4, 3, 5, 6. Suffixe : 4, 2, 5, 6, 3, 1." },
    { code: "c7-x2", niv: "facile", rep: "6 nœuds ; la plus longue branche (1-2-4 ou 1-3-5) a 3 nœuds ; feuilles : 4, 5, 6." },
    { code: "c7-x3", niv: "facile", rep: "La fonction fait la somme des valeurs : 1 + 2 + 3 + 4 + 5 + 6 = 21 ; pour le sous-arbre gauche, 2 + 4 = 6." },
    { code: "c7-x4", niv: "difficile", rep: "Arbre : 8 ; à gauche 3 (enfants 1 et 6, et 4 sous 6 à gauche) ; à droite 10 (puis 14 à droite). L’infixe donne les clés triées ; <code>r.gauche.droit</code> est 6 ; la plus longue branche 8-3-6-4 a 4 nœuds." }
  ],
  ep: [
    { titre: "Mesures d’un arbre binaire", enonce: `[[c7-ep1-fourni]]`,
      questions: [
        { q: "Compléter <code>taille</code> et <code>hauteur</code> (lignes 9 et 13).", c: `<p>Cas de base <code>if a is None: return 0</code>, puis <code>1 + taille(a.gauche) + taille(a.droit)</code> et <code>1 + max(hauteur(a.gauche), hauteur(a.droit))</code>.</p>` },
        { q: "Calculer <code>nb_feuilles(Noeud(1, Noeud(2, Noeud(3), Noeud(4))))</code> à la main, puis avec la fonction. Le résultat est-il juste ? Corriger.", c: `<p>L’arbre a deux feuilles (3 et 4), mais la fonction renvoie 1 : la racine n’a pas d’enfant droit, et avec <code>or</code> un nœud qui a <b>un seul</b> enfant est compté comme une feuille, sans explorer son sous-arbre. Une feuille n’a <b>aucun</b> enfant : il faut <code>and</code>.</p>` },
        { q: "Écrire <code>est_parfait(a)</code>, vraie si tous les niveaux sont remplis, en utilisant l’encadrement de la taille, puis des tests.", c: `[[c7-ep1-corr]]` },
        { q: "À l’oral : quel est le coût de <code>taille</code> ? Pourquoi la récursivité est-elle naturelle ici ?", c: `<p>Chaque nœud est visité une fois : coût linéaire en la taille. La définition même de l’arbre binaire est récursive (un nœud et deux arbres binaires), donc les fonctions la suivent : cas de l’arbre vide, puis combinaison des deux sous-arbres.</p>` }
      ] },
    { titre: "Arbre binaire de recherche", enonce: `[[c7-ep2-fourni]]`,
      questions: [
        { q: "On exécute <code>r = inserer(None, 41)</code>. Que vaut <code>r</code> ? Expliquer et corriger.", c: `<p><code>r</code> vaut None : le nœud est créé mais pas renvoyé, puis la fonction atteint <code>return a</code> avec <code>a = None</code>. Correction : <code>return Noeud(cle)</code>. (À un niveau plus bas, le même oubli fait perdre le nœud à rattacher.)</p>` },
        { q: "Compléter <code>rechercher</code> (récursive ou itérative).", c: `<p>Arbre vide : False ; égalité : True ; sinon on descend d’un seul côté selon la comparaison.</p>` },
        { q: "Écrire <code>maximum(a)</code> pour un ABR non vide, puis des tests (arbre vide, clés présentes et absentes, doublon).", c: `[[c7-ep2-corr]]` },
        { q: "À l’oral : combien de comparaisons au plus pour une recherche ? Que se passe-t-il si l’on insère les clés dans l’ordre croissant ?", c: `<p>Au plus la hauteur de l’arbre. Clés insérées triées : chaque nouvelle clé va à droite de la précédente, l’arbre est un peigne de hauteur <i>n</i> et la recherche devient linéaire, comme dans une liste.</p>` }
      ] }
  ],
  ecrit: { titre: "Arbres d’expressions arithmétiques", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite. On utilise la classe <code>Noeud</code> du cours.",
    enonce: `<p>On représente une expression arithmétique par un arbre binaire : les feuilles portent des nombres, les nœuds internes un opérateur parmi <code>+ - * /</code>. On étudie l’expression <b>2 × (5 + 3) − 4</b>.</p>`,
    questions: [
      { q: "Dessiner l’arbre de cette expression. Quelle est sa racine ? Combien a-t-il de feuilles ?", pts: "1 pt", c: `<p>La dernière opération effectuée est la soustraction : c’est la racine. Sous-arbre gauche : × (feuille 2, et + avec les feuilles 5 et 3) ; sous-arbre droit : la feuille 4. Quatre feuilles : 2, 5, 3, 4.</p><pre class="mono petit">        −
      /   \\
     ×     4
    / \\
   2   +
      / \\
     5   3</pre>` },
      { q: "Donner sa taille et sa hauteur (en nombre de nœuds).", pts: "0,5 pt", c: `<p>Taille 7 ; hauteur 4 (branche − → × → + → 5).</p>` },
      { q: "Écrire le parcours préfixe et le parcours suffixe de cet arbre.", pts: "1 pt", c: `<p>Préfixe : − × 2 + 5 3 4. Suffixe : 2 5 3 + × 4 −.</p>` },
      { q: "Le parcours suffixe donne l’expression en notation polonaise inverse. Décrire son évaluation à l’aide d’une pile.", pts: "1 pt", c: `<p>On empile 2, 5, 3 ; « + » dépile 3 et 5, empile 8 ; « × » dépile 8 et 2, empile 16 ; on empile 4 ; « − » dépile 4 et 16, empile 12. Résultat : 12.</p>` },
      { q: "Écrire une fonction récursive <code>evaluer(a)</code> qui renvoie la valeur de l’expression représentée par <code>a</code>.", pts: "1,5 pt", c: `<p>Une feuille renvoie sa valeur ; sinon on évalue les deux sous-arbres puis on applique l’opérateur de la racine.</p>[[c7-ecrit-corr]]` },
      { q: "Écrire une fonction <code>nb_operations(a)</code> qui compte les opérateurs de l’expression.", pts: "1 pt", c: `<p>Les opérateurs sont exactement les nœuds internes (non feuilles) : 3 ici. Code dans le corrigé ci-dessus.</p>` }
    ],
    methode: `<p>Pour un exercice sur les arbres : dessine l’arbre, numérote les nœuds dans l’ordre du parcours demandé, écris toute fonction avec le schéma « cas de l’arbre vide (ou de la feuille), appels sur les deux sous-arbres, combinaison », et vérifie la convention de hauteur de l’énoncé.</p>` },
  qcm: [
    { q: "Qu’est-ce qu’une feuille ?", c: ["La racine de l’arbre", "Un nœud sans enfant", "Un nœud avec deux enfants", "Une arête"], a: 1, e: "Les feuilles sont les extrémités des branches.", ref: "i1" },
    { q: "Un arbre binaire est…", c: ["un arbre dont les valeurs sont 0 ou 1", "vide, ou une racine avec un sous-arbre gauche et un sous-arbre droit", "un arbre de hauteur 2", "un tableau trié"], a: 1, e: "Définition récursive ; chaque nœud a au plus deux enfants.", ref: "i2" },
    { q: "Quelle est la taille de l’arbre exemple (A, B, C, D, E, F, G) ?", c: ["3", "4", "7", "8"], a: 2, e: "La taille est le nombre de nœuds.", ref: "i3" },
    { q: "Avec la convention « nombre de nœuds », combien de nœuds au plus a un arbre binaire de hauteur 4 ?", c: ["4", "8", "15", "16"], a: 2, e: "2⁴ − 1 = 15 (1 + 2 + 4 + 8).", ref: "i3" },
    { q: "Un arbre binaire de 1 000 nœuds a une hauteur (en nœuds) au moins égale à…", c: ["1", "10", "500", "1 000"], a: 1, e: "⌈log₂ 1001⌉ = 10, car 2¹⁰ − 1 = 1 023 ≥ 1 000.", ref: "i3" },
    { q: "Quel parcours traite la racine entre ses deux sous-arbres ?", c: ["Préfixe", "Infixe", "Suffixe", "En largeur"], a: 1, e: "Infixe : gauche, racine, droit.", ref: "i4" },
    { q: "Sur l’arbre exemple, quel est le parcours préfixe ?", c: ["A B C D E F G", "A B D E G C F", "D B G E A C F", "D G E B F C A"], a: 1, e: "Racine, puis tout le sous-arbre gauche, puis le droit.", ref: "i4" },
    { q: "Quelle structure le parcours en largeur utilise-t-il ?", c: ["Une pile", "Une file", "Un dictionnaire", "Un tableau trié"], a: 1, e: "FIFO : les enfants passent après les nœuds déjà en attente.", ref: "i5" },
    { q: "Quel parcours d’un arbre d’expression donne la notation polonaise inverse ?", c: ["Préfixe", "Infixe", "Suffixe", "En largeur"], a: 2, e: "Les opérandes d’abord, l’opérateur ensuite.", ref: "i6" },
    { q: "Dans un ABR, où se trouve la plus petite clé ?", c: ["À la racine", "Au bout de la branche la plus à gauche", "Dans une feuille quelconque", "Au bout de la branche la plus à droite"], a: 1, e: "On descend à gauche tant que c’est possible.", ref: "i7" },
    { q: "Que donne le parcours infixe d’un ABR ?", c: ["Les clés dans l’ordre d’insertion", "Les clés triées par ordre croissant", "La racine en premier", "Les feuilles seulement"], a: 1, e: "Gauche (plus petits), racine, droite (plus grands), récursivement.", ref: "i7" },
    { q: "Combien de comparaisons au plus pour chercher une clé dans un ABR de hauteur h ?", c: ["1", "h", "2h", "n"], a: 1, e: "On suit une seule branche.", ref: "i8" },
    { q: "On insère 1, 2, 3, 4, 5 dans cet ordre dans un ABR vide. Quelle est sa hauteur (en nœuds) ?", c: ["3", "4", "5", "1"], a: 2, e: "Chaque clé va à droite de la précédente : un peigne de 5 nœuds.", ref: "i8" }
  ],
  cartes: [
    { r: "Racine / feuille", v: "Nœud sans parent / nœud sans enfant." },
    { r: "Arbre binaire", v: "Vide, ou une racine et deux arbres binaires : sous-arbre gauche et sous-arbre droit." },
    { r: "Taille", v: "Nombre de nœuds : 0 si vide, sinon 1 + taille(G) + taille(D)." },
    { r: "Hauteur (convention nœuds)", v: "0 si vide, sinon 1 + max(hauteur(G), hauteur(D)). Vérifier la convention de l’énoncé." },
    { r: "Encadrement de la taille", v: "h ≤ n ≤ 2ʰ − 1 (convention nœuds)." },
    { r: "Préfixe", v: "Racine, sous-arbre gauche, sous-arbre droit." },
    { r: "Infixe", v: "Sous-arbre gauche, racine, sous-arbre droit." },
    { r: "Suffixe", v: "Sous-arbre gauche, sous-arbre droit, racine." },
    { r: "Parcours en largeur", v: "Niveau par niveau avec une file : défiler un nœud, le traiter, enfiler ses enfants." },
    { r: "ABR", v: "Pour chaque nœud : clés du sous-arbre gauche < clé < clés du sous-arbre droit." },
    { r: "Recherche dans un ABR", v: "Égal : trouvé ; plus petit : à gauche ; plus grand : à droite ; arbre vide : absent." },
    { r: "Insertion dans un ABR", v: "Descendre comme pour la recherche jusqu’à une place vide ; y créer une feuille ; rattacher." },
    { r: "Coût dans un ABR", v: "Au plus la hauteur : ≈ log₂ n si équilibré, n si dégénéré (peigne)." },
    { r: "Infixe d’un ABR", v: "Les clés dans l’ordre croissant." },
    { r: "Arbre d’expression", v: "Feuilles = nombres, nœuds = opérateurs ; l’évaluation est un parcours suffixe." }
  ]
});
