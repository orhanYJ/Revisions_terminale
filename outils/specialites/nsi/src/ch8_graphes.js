/* ===================== Chapitre 8 — Graphes : structures et algorithmes ===================== */
C("c8-dict", String.raw`
#   B ─── D ─── F ─── G
#   │     │     │
#   A ─── C ─── E          (A-B, A-C, B-D, C-D, C-E, D-F, E-F, F-G)
graphe = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E", "G"],
    "G": ["F"],
}
print(graphe["C"], len(graphe["F"]))                # voisins de C, degré de F
print("E" in graphe["D"])                          # D et E sont-ils voisins ?
nb_aretes = sum(len(v) for v in graphe.values()) // 2   # chaque arête est vue deux fois
print(len(graphe), "sommets,", nb_aretes, "arêtes")`, { fichier: "graphe.py", out: "['A', 'D', 'E'] 3\nFalse\n7 sommets, 8 arêtes" });

C("c8-matrice", String.raw`
sommets = ["A", "B", "C", "D", "E", "F", "G"]
#       A  B  C  D  E  F  G
M = [[0, 1, 1, 0, 0, 0, 0],   # A
     [1, 0, 0, 1, 0, 0, 0],   # B
     [1, 0, 0, 1, 1, 0, 0],   # C
     [0, 1, 1, 0, 0, 1, 0],   # D
     [0, 0, 1, 0, 0, 1, 0],   # E
     [0, 0, 0, 1, 1, 0, 1],   # F
     [0, 0, 0, 0, 0, 1, 0]]   # G

i, j = sommets.index("C"), sommets.index("E")
print(M[i][j], M[j][i])                       # non orienté : matrice symétrique
print("degré de F :", sum(M[sommets.index("F")]))`, { fichier: "matrice.py", out: "1 1\ndegré de F : 3" });

C("c8-conversions", String.raw`
def matrice_vers_dict(M, sommets):
    g = {}
    for i in range(len(sommets)):
        g[sommets[i]] = [sommets[j] for j in range(len(sommets)) if M[i][j] != 0]
    return g

def dict_vers_matrice(g):
    sommets = list(g)
    n = len(sommets)
    M = [[0] * n for _ in range(n)]         # pas [[0] * n] * n : lignes partagées !
    for s in g:
        for v in g[s]:
            M[sommets.index(s)][sommets.index(v)] = 1
    return M, sommets

print(matrice_vers_dict(M, sommets) == graphe)
M2, s2 = dict_vers_matrice(graphe)
print(M2 == M, s2 == sommets)`, { deps: ["c8-dict", "c8-matrice"], out: "True\nTrue True" });

C("c8-oriente", String.raw`
# Graphe ORIENTÉ : qui suit qui sur un réseau social (l'arc a -> b : a suit b)
suit = {"ada": ["alan", "grace"], "alan": ["grace"], "grace": ["ada"], "linus": ["ada"]}

def predecesseurs(g, s):
    """Liste des sommets qui ont un arc vers s."""
    return [x for x in g if s in g[x]]

print(suit["alan"], predecesseurs(suit, "ada"))          # successeurs / prédécesseurs
print(len(suit["ada"]), len(predecesseurs(suit, "ada")))  # degré sortant / entrant`, { out: "['grace'] ['grace', 'linus']\n2 2" });

C("c8-pondere", String.raw`
# Graphe PONDÉRÉ (distances fictives, en km) : sommet -> {voisin: poids}
routes = {"A": {"B": 7, "C": 3}, "B": {"A": 7, "C": 2}, "C": {"A": 3, "B": 2}}
print(routes["A"]["C"] + routes["C"]["B"], "km par C, au lieu de", routes["A"]["B"])`, { out: "5 km par C, au lieu de 7" });

C("c8-classe", String.raw`
class Graphe:
    """Graphe non orienté, représenté par des listes de voisins."""
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arete(self, a, b):
        self.ajouter_sommet(a)
        self.ajouter_sommet(b)
        self.adj[a].append(b)              # dans les DEUX sens : non orienté
        self.adj[b].append(a)

    def voisins(self, s):
        return self.adj[s]

    def sommets(self):
        return list(self.adj)

g = Graphe()
for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]:
    g.ajouter_arete(a, b)
print(g.sommets(), g.voisins("D"))`, { out: "['A', 'B', 'C', 'D'] ['B', 'C']" });

C("c8-largeur", String.raw`
def parcours_largeur(g, depart):
    """Ordre de visite et distance (en nombre d'arêtes) de chaque sommet atteint."""
    distance = {depart: 0}           # sert aussi à marquer les sommets découverts
    file = [depart]
    ordre = []
    while file:
        s = file.pop(0)              # défiler
        ordre.append(s)
        for v in g[s]:
            if v not in distance:    # pas encore découvert
                distance[v] = distance[s] + 1
                file.append(v)       # enfiler
    return ordre, distance

ordre, dist = parcours_largeur(graphe, "A")
print(ordre)
print(dist)`, { deps: ["c8-dict"], out: "['A', 'B', 'C', 'D', 'E', 'F', 'G']\n{'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 3, 'G': 4}" });

C("c8-profondeur", String.raw`
def profondeur_rec(g, s, vus=None):
    """Parcours en profondeur récursif : renvoie la liste des sommets visités."""
    if vus is None:
        vus = []
    vus.append(s)                    # marquer
    for v in g[s]:
        if v not in vus:
            profondeur_rec(g, v, vus)   # aller le plus loin possible
    return vus

def profondeur_pile(g, depart):
    """Même idée avec une PILE explicite à la place de la pile d'appels."""
    vus = []
    pile = [depart]
    while pile:
        s = pile.pop()               # dépiler
        if s not in vus:
            vus.append(s)
            for v in g[s]:
                if v not in vus:
                    pile.append(v)   # empiler
    return vus

print(profondeur_rec(graphe, "A"))
print(profondeur_pile(graphe, "A"))`, { deps: ["c8-dict"], out: "['A', 'B', 'D', 'C', 'E', 'F', 'G']\n['A', 'C', 'E', 'F', 'G', 'D', 'B']" });

C("c8-chemin", String.raw`
def chemin(g, depart, arrivee):
    """Un plus court chemin (en nombre d'arêtes) de depart à arrivee, ou None."""
    parent = {depart: None}
    file = [depart]
    while file:
        s = file.pop(0)
        if s == arrivee:
            break
        for v in g[s]:
            if v not in parent:
                parent[v] = s            # on retient d'où l'on vient
                file.append(v)
    if arrivee not in parent:
        return None
    ch = []
    s = arrivee
    while s is not None:                 # on remonte les parents
        ch.append(s)
        s = parent[s]
    ch.reverse()
    return ch

print(chemin(graphe, "A", "G"))
print(chemin(graphe, "G", "C"))
print(chemin({"X": ["Y"], "Y": ["X"], "Z": []}, "X", "Z"))`, { deps: ["c8-dict"], out: "['A', 'B', 'D', 'F', 'G']\n['G', 'F', 'D', 'C']\nNone" });

C("c8-connexe", String.raw`
def est_connexe(g):
    """Non orienté : connexe si un parcours depuis un sommet atteint tous les autres."""
    if len(g) == 0:
        return True
    depart = list(g)[0]
    return len(profondeur_rec(g, depart)) == len(g)

print(est_connexe(graphe), est_connexe({"X": ["Y"], "Y": ["X"], "Z": []}))`, { deps: ["c8-dict", "c8-profondeur"], out: "True False" });

C("c8-cycle", String.raw`
def a_un_cycle(g):
    """Graphe NON orienté : un cycle existe si le parcours retombe sur un sommet
    déjà vu qui n'est pas celui d'où l'on vient (son parent)."""
    vus = set()
    def explorer(s, parent):
        vus.add(s)
        for v in g[s]:
            if v not in vus:
                if explorer(v, s):
                    return True
            elif v != parent:
                return True              # arête qui revient en arrière : cycle
        return False
    for s in g:                          # pour les graphes non connexes
        if s not in vus and explorer(s, None):
            return True
    return False

arbre = {"A": ["B", "C"], "B": ["A"], "C": ["A", "D"], "D": ["C"]}
print(a_un_cycle(graphe), a_un_cycle(arbre))`, { deps: ["c8-dict"], out: "True False" });

C("c8-cycle-oriente", String.raw`
def a_un_cycle_oriente(g):
    """Graphe ORIENTÉ : trois états. Un arc vers un sommet « en cours »
    (encore dans la pile d'appels) referme un cycle."""
    etat = {s: "blanc" for s in g}        # blanc : jamais vu ; gris : en cours ; noir : fini
    def explorer(s):
        etat[s] = "gris"
        for v in g[s]:
            if etat[v] == "gris":
                return True
            if etat[v] == "blanc" and explorer(v):
                return True
        etat[s] = "noir"
        return False
    return any(etat[s] == "blanc" and explorer(s) for s in g)

prerequis = {"bases": ["algo"], "algo": ["graphes"], "graphes": [], "web": ["bases"]}
boucle = {"a": ["b"], "b": ["c"], "c": ["a"]}
print(a_un_cycle_oriente(prerequis), a_un_cycle_oriente(boucle))`, { out: "False True" });

C("c8-p-matrice", String.raw`
M = [[0] * 3] * 3          # trois fois LA MÊME ligne
M[0][1] = 1
print(M)`, { out: "[[0, 1, 0], [0, 1, 0], [0, 1, 0]]" });

C("c8-p-marquage", String.raw`
def largeur_sans_marquage(g, depart, limite=20):
    file, ordre = [depart], []
    while file and len(ordre) < limite:      # sans limite, la boucle ne finirait pas
        s = file.pop(0)
        ordre.append(s)
        for v in g[s]:
            file.append(v)                   # on ré-enfile même les sommets déjà vus
    return ordre

print(largeur_sans_marquage({"A": ["B"], "B": ["A"]}, "A", limite=6))`, { out: "['A', 'B', 'A', 'B', 'A', 'B']" });

/* prédis la sortie */
C("c8-x1", String.raw`
M = [[0, 1, 1, 0],
     [1, 0, 1, 1],
     [1, 1, 0, 0],
     [0, 1, 0, 0]]
print([sum(ligne) for ligne in M], M[3][1] == M[1][3])`, { out: "[2, 3, 2, 1] True" });

C("c8-x2", String.raw`
g = {1: [2, 3], 2: [4], 3: [4], 4: []}
print(len(g), sum(len(v) for v in g.values()), [s for s in g if 4 in g[s]])`, { out: "4 4 [2, 3]" });

C("c8-x3", String.raw`
g = {"S": ["T", "U"], "T": ["S", "V"], "U": ["S", "V"], "V": ["T", "U", "W"], "W": ["V"]}
print(parcours_largeur(g, "W")[0])`, { deps: ["c8-largeur"], out: "['W', 'V', 'T', 'U', 'S']" });

C("c8-x4", String.raw`
g = {"S": ["T", "U"], "T": ["S", "V"], "U": ["S", "V"], "V": ["T", "U", "W"], "W": ["V"]}
print(profondeur_rec(g, "S"))`, { deps: ["c8-profondeur"], out: "['S', 'T', 'V', 'U', 'W']" });

/* épreuve pratique 1 */
C("c8-ep1-fourni", String.raw`
def ajouter_lien(reseau, a, b):
    """Ajoute l'amitié (réciproque) entre a et b dans le dictionnaire reseau."""
    for p in (a, b):
        if p not in reseau:
            reseau[p] = []
    reseau[a].append(b)

def amis_communs(reseau, a, b):
    """Liste des amis communs de a et b, dans l'ordre des amis de a."""
    ...

reseau = {}
for a, b in [("Ada", "Alan"), ("Ada", "Grace"), ("Alan", "Grace"), ("Grace", "Linus")]:
    ajouter_lien(reseau, a, b)
print(reseau["Grace"])`, { fichier: "reseau.py", run: false, trous: [10] });

C("c8-ep1-corr", String.raw`
def ajouter_lien(reseau, a, b):
    for p in (a, b):
        if p not in reseau:
            reseau[p] = []
    reseau[a].append(b)
    reseau[b].append(a)                  # l'amitié est réciproque : graphe non orienté

def amis_communs(reseau, a, b):
    return [x for x in reseau[a] if x in reseau[b]]

def suggestions(reseau, a):
    """Amis d'amis de a qui ne sont pas déjà ses amis (sommets à distance 2)."""
    res = []
    for ami in reseau[a]:
        for x in reseau[ami]:
            if x != a and x not in reseau[a] and x not in res:
                res.append(x)
    return res

reseau = {}
for a, b in [("Ada", "Alan"), ("Ada", "Grace"), ("Alan", "Grace"), ("Grace", "Linus")]:
    ajouter_lien(reseau, a, b)

def test():
    assert reseau["Grace"] == ["Ada", "Alan", "Linus"]
    assert all(x in reseau[y] for x in reseau for y in reseau[x])   # symétrie
    assert amis_communs(reseau, "Ada", "Alan") == ["Grace"]
    assert amis_communs(reseau, "Linus", "Alan") == ["Grace"]
    assert suggestions(reseau, "Ada") == ["Linus"]
    assert suggestions(reseau, "Grace") == []

test()
print("tous les tests passent")`, { fichier: "reseau.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c8-ep2-fourni", String.raw`
LABY = ["S..#",
        "##.#",
        "...E",
        ".###"]

def voisins(grille, l, c):
    """Cases libres voisines (haut, bas, gauche, droite) de la case (l, c)."""
    res = []
    for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, b = l + dl, c + dc
        if a < len(grille) and b < len(grille[0]) and grille[a][b] != "#":
            res.append((a, b))
    return res

def plus_court(grille):
    """Nombre minimal de pas de S à E (parcours en largeur), ou -1."""
    for l in range(len(grille)):
        if "S" in grille[l]:
            depart = (l, grille[l].index("S"))
    dist = {depart: 0}
    file = [depart]
    while file:
        l, c = file.pop(0)
        if grille[l][c] == "E":
            return dist[(l, c)]
        for v in voisins(grille, l, c):
            if v not in dist:
                dist[v] = dist[(l, c)] + 1
                file.append(v)
    return -1

print(plus_court(LABY))`, { fichier: "labyrinthe.py", out: "3" });

C("c8-ep2-corr", String.raw`
def voisins(grille, l, c):
    res = []
    for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, b = l + dl, c + dc
        if 0 <= a < len(grille) and 0 <= b < len(grille[0]) and grille[a][b] != "#":
            res.append((a, b))
    return res

def plus_court(grille):
    for l in range(len(grille)):
        if "S" in grille[l]:
            depart = (l, grille[l].index("S"))
    dist = {depart: 0}
    file = [depart]
    while file:
        l, c = file.pop(0)
        if grille[l][c] == "E":
            return dist[(l, c)]
        for v in voisins(grille, l, c):
            if v not in dist:
                dist[v] = dist[(l, c)] + 1
                file.append(v)
    return -1

def test():
    assert plus_court(["S..#", "##.#", "...E", ".###"]) == 5
    assert plus_court(["SE"]) == 1
    assert plus_court(["S#E"]) == -1                       # pas de chemin
    assert plus_court(["S...", "###.", "E..."]) == 8
    assert voisins(["S..#", "##.#", "...E", ".###"], 0, 0) == [(0, 1)]

test()
print("tous les tests passent")`, { fichier: "labyrinthe.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c8-ecrit-corr", String.raw`
refuges = {"Lac": ["Col", "Pic"], "Col": ["Lac", "Pic", "Gîte"], "Pic": ["Lac", "Col"],
           "Gîte": ["Col", "Source"], "Source": ["Gîte"]}

def degre_max(g):
    return max(len(g[s]) for s in g)

def accessibles(g, depart, n):
    """Sommets à au plus n étapes de depart (parcours en largeur)."""
    dist = {depart: 0}
    file = [depart]
    while file:
        s = file.pop(0)
        for v in g[s]:
            if v not in dist:
                dist[v] = dist[s] + 1
                file.append(v)
    return [s for s in dist if dist[s] <= n]

print(degre_max(refuges), accessibles(refuges, "Lac", 2))
print(parcours_largeur(refuges, "Source")[1])
print(a_un_cycle(refuges), a_un_cycle({"Gîte": ["Source"], "Source": ["Gîte"]}))`, { deps: ["c8-largeur", "c8-cycle"], out: "3 ['Lac', 'Col', 'Pic', 'Gîte']\n{'Source': 0, 'Gîte': 1, 'Col': 2, 'Lac': 3, 'Pic': 3}\nTrue False" });

C("c8-retenir", String.raw`
def parcours(g, depart):
    vus = {depart}                 # marquer dès la découverte
    a_traiter = [depart]           # FILE -> largeur ; PILE -> profondeur
    while a_traiter:
        s = a_traiter.pop(0)       # pop(0) : file ; pop() : pile
        ...                        # traiter s
        for v in g[s]:
            if v not in vus:
                vus.add(v)
                a_traiter.append(v)`, { run: false });

/* ---------- animation : parcours de graphe ---------- */
WIDGETS_EXT["parcours-graphe"] = function (z, opt, O) {
  var G = { A: ["B", "C"], B: ["A", "D"], C: ["A", "D", "E"], D: ["B", "C", "F"], E: ["C", "F"], F: ["D", "E", "G"], G: ["F"] };
  var P = { A: [40, 120], B: [130, 40], C: [130, 200], D: [225, 120], E: [255, 210], F: [335, 120], G: [420, 120] };
  var AR = [["A", "B"], ["A", "C"], ["B", "D"], ["C", "D"], ["C", "E"], ["D", "F"], ["E", "F"], ["F", "G"]];
  function cle(a, b) { return a < b ? a + b : b + a; }
  function etapes(k) {
    var E = [], et = {}, arbre = {}, dist = {}, ordre = [], chemin = {};
    function snap(msg, struct, actif) { E.push({ et: JSON.parse(JSON.stringify(et)), arbre: JSON.parse(JSON.stringify(arbre)), dist: JSON.parse(JSON.stringify(dist)), ordre: ordre.slice(), struct: struct ? struct.slice() : [], actif: actif, chemin: JSON.parse(JSON.stringify(chemin)), msg: msg }); }
    if (k === "largeur" || k === "chemin") {
      var file = ["A"], parent = { A: null }; dist.A = 0; et.A = "attente";
      snap("Départ en <b>A</b> : on le marque (distance 0) et on l’enfile. La <b>file</b> garantit qu’on traite les sommets par distance croissante.", file);
      while (file.length) {
        var s = file.shift(); et[s] = "traite"; ordre.push(s);
        var nv = [];
        G[s].forEach(function (v) { if (!(v in dist)) { dist[v] = dist[s] + 1; parent[v] = s; et[v] = "attente"; arbre[cle(s, v)] = 1; file.push(v); nv.push(v); } });
        snap("On défile <b>" + s + "</b>. " + (nv.length ? "Voisins pas encore découverts : <b>" + nv.join(", ") + "</b> → distance " + (dist[s] + 1) + ", enfilés." : "Tous ses voisins sont déjà découverts : rien à enfiler."), file, s);
        if (k === "chemin" && s === "G") break;
      }
      if (k === "chemin") {
        var x = "G", ch = [];
        while (x) { ch.unshift(x); chemin[x] = 1; if (parent[x]) chemin[cle(x, parent[x])] = 1; x = parent[x]; }
        snap("G est atteint. On remonte les <b>parents</b> mémorisés : G ← F ← D ← B ← A. Plus court chemin : <b>" + ch.join(" → ") + "</b>, " + (ch.length - 1) + " arêtes (il en existe un autre de même longueur par C et E).", [], null);
      } else snap("File vide : tous les sommets atteignables sont visités. Ordre <b>" + ordre.join(" ") + "</b> ; les traits épais forment l’arbre du parcours, les nombres sont les distances depuis A.", [], null);
      return E;
    }
    var pile = ["A"]; et.A = "attente";
    snap("Parcours en profondeur avec une <b>pile</b> : on empile A. On dépile toujours le <b>dernier</b> sommet empilé, donc on s’enfonce avant de revenir.", pile);
    var vient = {};
    while (pile.length) {
      var t = pile.pop();
      if (et[t] === "traite") { snap("On dépile <b>" + t + "</b>, déjà visité : on l’ignore.", pile, null); continue; }
      et[t] = "traite"; ordre.push(t); if (vient[t]) arbre[cle(t, vient[t])] = 1;
      var em = [];
      G[t].forEach(function (v) { if (et[v] !== "traite") { pile.push(v); vient[v] = t; et[v] = "attente"; em.push(v); } });
      snap("On dépile et on visite <b>" + t + "</b>. " + (em.length ? "On empile ses voisins non visités : " + em.join(", ") + " (le dernier empilé sera le prochain visité)." : "Aucun voisin non visité."), pile, t);
    }
    snap("Pile vide. Ordre en profondeur : <b>" + ordre.join(" ") + "</b>. La version récursive donne A B D C E F G : c’est aussi un parcours en profondeur, l’ordre dépend de l’ordre des voisins.", [], null);
    return E;
  }
  function dessine(sc, e) {
    var s = '<svg class="graphe-svg" viewBox="0 0 460 240" role="img" aria-label="Graphe de 7 sommets">';
    AR.forEach(function (a) { var k = cle(a[0], a[1]), p = P[a[0]], q = P[a[1]]; s += '<line class="ar' + (e.chemin[k] ? " ch" : e.arbre[k] ? " arb" : "") + '" x1="' + p[0] + '" y1="' + p[1] + '" x2="' + q[0] + '" y2="' + q[1] + '"/>'; });
    Object.keys(P).forEach(function (v) {
      var p = P[v], c = e.chemin[v] ? "neuf" : v === e.actif ? "actif" : e.et[v] || "";
      s += '<g class="nd-a ' + c + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="18"/><text x="' + p[0] + '" y="' + (p[1] + 5) + '" text-anchor="middle">' + v + "</text>" + (v in e.dist ? '<text class="rang" x="' + (p[0] + 16) + '" y="' + (p[1] - 15) + '">' + e.dist[v] + "</text>" : "") + "</g>";
    });
    s += "</svg>";
    sc.innerHTML = '<div class="parc">' + s + '<div class="parc-cote"><div class="titre-pile">' + (("A" in e.dist) ? "file (tête à gauche)" : "pile (sommet à droite)") + '</div><div class="mini-file">' + (e.struct.length ? e.struct.map(function (v) { return '<span class="puce">' + v + "</span>"; }).join("") : '<span class="repere">vide</span>') + '</div><div class="titre-pile">ordre de visite</div><div class="sortie-p mono">' + (e.ordre.join(" ") || "…") + "</div></div></div>";
  }
  O.lecteur(z, { titre: "parcours d’un graphe", choix: [{ k: "largeur", t: "en largeur (file)" }, { k: "profondeur", t: "en profondeur (pile)" }, { k: "chemin", t: "plus court chemin A → G" }], etapes: etapes, dessine: dessine, vitesse: 1500 });
};

/* Animation : repérer un cycle par un parcours en profondeur récursif (mêmes algorithmes que c8-cycle et c8-cycle-oriente). */
WIDGETS_EXT["cycle"] = function (z, opt, O) {
  var GR = {
    sans: { o: true, g: { A: ["B", "C"], B: ["D"], C: ["D", "E"], D: [], E: [] }, p: { A: [40, 110], B: [140, 40], C: [140, 180], D: [250, 110], E: [270, 200] } },
    avec: { o: true, g: { A: ["B", "C"], B: ["D"], C: ["D", "E"], D: [], E: ["C"] }, p: { A: [40, 110], B: [140, 40], C: [140, 180], D: [250, 110], E: [270, 200] } },
    non: { o: false, g: { A: ["B", "C"], B: ["A", "D"], C: ["A", "D"], D: ["B", "C"] }, p: { A: [40, 110], B: [150, 40], C: [150, 180], D: [260, 110] } }
  };
  function etapes(k) {
    var D = GR[k], g = D.g, E = [], etat = {}, pile = [], arc = null, cycle = null, fini = false;
    Object.keys(g).forEach(function (s) { etat[s] = "blanc"; });
    function snap(msg) { E.push({ etat: JSON.parse(JSON.stringify(etat)), pile: pile.slice(), arc: arc, cycle: cycle, msg: msg }); }
    if (D.o) {
      snap("Graphe <b>orienté</b>. Trois états : <b>blanc</b> (jamais vu), <b>gris</b> (en cours : encore dans la pile d’appels), <b>noir</b> (terminé). Un arc vers un sommet <b>gris</b> referme un cycle.");
      var explorer = function (s) {
        etat[s] = "gris"; pile.push(s); arc = null;
        snap("<code>explorer(" + s + ")</code> : " + s + " passe en <b>gris</b> et entre dans la pile d’appels.");
        for (var i = 0; i < g[s].length; i++) {
          var v = g[s][i]; arc = [s, v];
          if (etat[v] === "gris") { cycle = pile.slice(pile.indexOf(v)).concat([v]); snap("Arc " + s + " → " + v + " : " + v + " est <b>gris</b>, donc encore en cours, plus bas dans la pile. On est revenu sur un chemin déjà commencé : <b>cycle " + cycle.join(" → ") + "</b>. La fonction renvoie True."); return true; }
          if (etat[v] === "blanc") { snap("Arc " + s + " → " + v + " : " + v + " est blanc, on l’explore."); if (explorer(v)) return true; arc = null; }
          else snap("Arc " + s + " → " + v + " : " + v + " est <b>noir</b> (déjà terminé, tous ses chemins explorés sans revenir ici). <b>Pas de cycle</b> par cet arc : un simple test « déjà vu » se tromperait ici.");
        }
        etat[s] = "noir"; pile.pop(); arc = null;
        snap(s + " n’a plus de successeur à examiner : il devient <b>noir</b> et sort de la pile.");
        return false;
      };
      var trouve = false, ks = Object.keys(g);
      for (var j = 0; j < ks.length && !trouve; j++) if (etat[ks[j]] === "blanc") trouve = explorer(ks[j]);
      if (!trouve) { arc = null; snap("Tous les sommets sont noirs et aucun arc n’a mené à un sommet gris : <b>pas de cycle</b>, la fonction renvoie False. Ici, D est atteint par deux chemins (A → B → D et A → C → D) sans former de cycle."); }
    } else {
      snap("Graphe <b>non orienté</b> : on mémorise les sommets vus et, pour chacun, le sommet d’où l’on vient (son <b>parent</b>).");
      var parent = {};
      var expl = function (s, par) {
        etat[s] = "gris"; parent[s] = par; pile.push(s); arc = null;
        snap("<code>explorer(" + s + ", " + (par || "None") + ")</code> : " + s + " est marqué vu" + (par ? ", on y est arrivé depuis " + par : "") + ".");
        for (var i = 0; i < g[s].length; i++) {
          var v = g[s][i]; arc = [s, v];
          if (etat[v] === "blanc") { snap("Arête " + s + " – " + v + " : " + v + " pas encore vu, on l’explore."); if (expl(v, s)) return true; arc = null; }
          else if (v !== par) { cycle = pile.slice(pile.indexOf(v)).concat([v]); snap("Arête " + s + " – " + v + " : " + v + " est <b>déjà vu</b> et ce n’est pas le parent de " + s + " (" + par + ") : il existe deux chemins différents vers " + v + ". <b>Cycle " + cycle.join(" – ") + "</b>, la fonction renvoie True."); return true; }
          else snap("Arête " + s + " – " + v + " : " + v + " est déjà vu, mais c’est le <b>parent</b> : on revient par l’arête qu’on vient d’emprunter, ce n’est pas un cycle.");
        }
        etat[s] = "noir"; pile.pop(); arc = null;
        snap(s + " n’a plus de voisin à examiner : fin de son appel.");
        return false;
      };
      expl("A", null);
    }
    return E;
  }
  function dessine(sc, e, i, E, saut) {
    var k = sc.getAttribute("data-k"), D = GR[k], P = D.p, R = 17;
    var s = '<svg class="graphe-svg cyc" viewBox="0 0 310 225" role="img" aria-label="Graphe ' + (D.o ? "orienté" : "non orienté") + ' et parcours en profondeur">';
    var dans = function (a, b) { if (!e.cycle) return false; for (var j = 0; j + 1 < e.cycle.length; j++) if ((e.cycle[j] === a && e.cycle[j + 1] === b) || (!D.o && e.cycle[j] === b && e.cycle[j + 1] === a)) return true; return false; };
    var vus = {};
    Object.keys(D.g).forEach(function (a) {
      D.g[a].forEach(function (b) {
        if (!D.o && vus[b + a]) return; vus[a + b] = 1;
        var p = P[a], q = P[b], dx = q[0] - p[0], dy = q[1] - p[1], L = Math.sqrt(dx * dx + dy * dy), ux = dx / L, uy = dy / L;
        var dbl = D.o && D.g[b].indexOf(a) >= 0, ox = dbl ? -uy * 7 : 0, oy = dbl ? ux * 7 : 0;
        var x1 = p[0] + ux * R + ox, y1 = p[1] + uy * R + oy, x2 = q[0] - ux * (R + (D.o ? 2 : 0)) + ox, y2 = q[1] - uy * (R + (D.o ? 2 : 0)) + oy;
        var cl = dans(a, b) ? " cy" : e.arc && ((e.arc[0] === a && e.arc[1] === b) || (!D.o && e.arc[0] === b && e.arc[1] === a)) ? " ex" : "";
        s += '<line class="ar' + cl + '" x1="' + x1.toFixed(1) + '" y1="' + y1.toFixed(1) + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '"/>';
        if (D.o) s += '<path class="pointe' + cl + '" d="M' + x2.toFixed(1) + " " + y2.toFixed(1) + " L" + (x2 - ux * 10 - uy * 5).toFixed(1) + " " + (y2 - uy * 10 + ux * 5).toFixed(1) + " L" + (x2 - ux * 10 + uy * 5).toFixed(1) + " " + (y2 - uy * 10 - ux * 5).toFixed(1) + 'z"/>';
      });
    });
    Object.keys(P).forEach(function (v) {
      var p = P[v], et = e.etat[v], neuf = !saut && i > 0 && E[i - 1].etat[v] !== et;
      s += '<g class="nd-c ' + et + (neuf ? " neuf" : "") + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + R + '"/><text x="' + p[0] + '" y="' + (p[1] + 5) + '" text-anchor="middle">' + v + "</text></g>";
    });
    s += "</svg>";
    var leg = D.o ? '<span><i class="c-blanc"></i>blanc : jamais vu</span><span><i class="c-gris"></i>gris : en cours</span><span><i class="c-noir"></i>noir : terminé</span>' : '<span><i class="c-blanc"></i>pas encore vu</span><span><i class="c-gris"></i>vu, appel en cours</span><span><i class="c-noir"></i>vu, appel fini</span>';
    sc.innerHTML = '<div class="parc">' + s + '<div class="parc-cote"><div class="titre-pile">pile d’appels (le plus récent en haut)</div><div class="mini-pile cyc-pile">' + (e.pile.length ? e.pile.slice().reverse().map(function (v) { return '<span class="puce">explorer(' + v + ")</span>"; }).join("") : '<span class="repere">vide</span>') + '</div><div class="legende-c mono">' + leg + "</div></div></div>";
  }
  O.lecteur(z, {
    titre: "repérer un cycle", sous: "parcours en profondeur",
    choix: [{ k: "sans", t: "orienté, sans cycle" }, { k: "avec", t: "orienté, avec cycle" }, { k: "non", t: "non orienté" }],
    etapes: etapes, prepare: function (sc, k) { sc.setAttribute("data-k", k); }, dessine: dessine, vitesse: 1600
  });
};

CH.push({
  id: "ch8", n: 8, court: "graphes", fichier: "ch8_graphes.py",
  titre: "Graphes : structures et algorithmes",
  rubrique: "Rubriques « Structures de données » (graphes : structures relationnelles) et « Algorithmique » (algorithmes sur les graphes)",
  accroche: "Modéliser par un graphe, matrice d’adjacence et listes de voisins, parcours en largeur et en profondeur, chemins et cycles.",
  essentiel: [
    "Un <b>graphe</b> est formé de <b>sommets</b> reliés par des <b>arêtes</b> (non orienté) ou des <b>arcs</b> (orienté), éventuellement <b>pondérés</b>.",
    "Deux représentations : la <b>matrice d’adjacence</b> (tableau <i>n</i> × <i>n</i>) et les <b>listes de successeurs</b> (dictionnaire sommet → liste de voisins).",
    "Le <b>parcours en largeur</b> utilise une <b>file</b> : il visite les sommets par distance croissante et donne les plus courts chemins en nombre d’arêtes.",
    "Le <b>parcours en profondeur</b> utilise une <b>pile</b> (ou la récursivité) : il s’enfonce le plus loin possible avant de revenir ; il sert à repérer des cycles.",
    "On <b>marque</b> les sommets déjà découverts pour ne pas tourner en rond ; pour retrouver un chemin, on mémorise le <b>parent</b> de chaque sommet."
  ],
  attendus: [
    "Modéliser des situations sous forme de graphes (réseau routier, électrique, Internet, réseaux sociaux).",
    "Écrire les implémentations d’un graphe : matrice d’adjacence, liste de successeurs / de prédécesseurs ; passer d’une représentation à une autre.",
    "Parcourir un graphe en profondeur d’abord, en largeur d’abord.",
    "Repérer la présence d’un cycle dans un graphe ; chercher un chemin dans un graphe.",
    "Faire le lien avec le routage (chapitre réseaux) et utiliser les classes pour représenter un graphe."
  ],
  idees: [
    { id: "i1", t: "Modéliser par un graphe", h: `
<p>Un graphe décrit des <b>relations</b> entre des objets, sans hiérarchie (contrairement aux arbres). Exemples :</p>
<ul><li>réseau routier : sommets = villes, arêtes = routes (pondérées par la distance) ;</li>
<li>Internet : sommets = routeurs, arêtes = liaisons ; le routage cherche des chemins (chapitre réseaux) ;</li>
<li>réseau social : amitiés (non orienté) ou abonnements (orienté : je peux suivre quelqu’un qui ne me suit pas) ;</li>
<li>labyrinthe : sommets = cases libres, arêtes = passages entre cases voisines ;</li>
<li>dépendances : un cours qui en exige un autre, une tâche qui doit attendre une autre (orienté).</li></ul>
<div class="boite def"><div class="lab">"""vocabulaire"""</div><p>Deux sommets reliés sont <b>adjacents</b> (voisins). Le <b>degré</b> d’un sommet est son nombre de voisins. Un <b>chemin</b> est une suite de sommets dont chacun est adjacent au suivant ; un <b>cycle</b> est un chemin qui revient à son point de départ sans réutiliser d’arête. Un graphe non orienté est <b>connexe</b> si deux sommets quelconques sont toujours reliés par un chemin. Un arbre est un graphe connexe sans cycle.</p></div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1736 <b>·</b></span> Leonhard Euler montre qu’on ne peut pas traverser les sept ponts de Königsberg une seule fois chacun en revenant au départ : c’est l’acte de naissance de la théorie des graphes.</p></div>` },

    { id: "i2", t: "Orienté, non orienté, pondéré", h: `
<p>Dans un graphe <b>non orienté</b>, une arête relie deux sommets dans les deux sens. Dans un graphe <b>orienté</b>, un arc va d’un sommet vers un autre : on distingue les <b>successeurs</b> d’un sommet (où mènent ses arcs) et ses <b>prédécesseurs</b> (d’où viennent les arcs qui arrivent sur lui), et donc un degré sortant et un degré entrant.</p>
[[c8-oriente]]
<p>Un graphe est <b>pondéré</b> quand chaque arête porte un nombre (distance, durée, coût). Le plus court chemin n’est alors plus celui qui a le moins d’arêtes :</p>
[[c8-pondere]]` },

    { id: "i3", t: "La matrice d’adjacence", h: `
<p>On numérote les sommets de 0 à <i>n</i> − 1. La <b>matrice d’adjacence</b> est un tableau <i>n</i> × <i>n</i> : la case (<i>i</i>, <i>j</i>) vaut 1 s’il y a une arête (ou un arc) de <i>i</i> vers <i>j</i>, 0 sinon (ou le poids, pour un graphe pondéré). Pour un graphe non orienté, elle est <b>symétrique</b>. Exemple, le graphe de ce chapitre :</p>
[[c8-matrice]]
<p>Le degré d’un sommet est la somme de sa ligne. Tester si deux sommets sont voisins coûte un seul accès <code>M[i][j]</code>. Mais la matrice occupe <i>n</i>² cases, même si le graphe a peu d’arêtes : un million de sommets donnerait mille milliards de cases.</p>` },

    { id: "i4", t: "Les listes de successeurs (dictionnaire)", h: `
<p>On associe à chaque sommet la liste de ses voisins (ou successeurs), dans un dictionnaire (chapitre 5). C’est la représentation la plus utilisée en Python :</p>
[[c8-dict]]
<p>Elle n’occupe que la place nécessaire (de l’ordre de <i>n</i> + <i>m</i> pour <i>m</i> arêtes) et donne directement les voisins d’un sommet, ce dont les parcours ont besoin. Tester si deux sommets sont voisins demande en revanche de parcourir une liste.</p>
<p>Le programme demande de savoir <b>passer d’une représentation à l’autre</b> :</p>
[[c8-conversions]]` },

    { id: "i5", t: "Un graphe comme objet", h: `
<p>Le programme cite les graphes comme exemple d’utilisation des classes. Une classe <code>Graphe</code> cache la représentation (ici un dictionnaire) derrière une interface : ajouter un sommet, ajouter une arête, obtenir les voisins.</p>
[[c8-classe]]
<p>Si l’on décidait de passer à une matrice, seul le code de la classe changerait, pas celui qui l’utilise (interface et implémentation, chapitre 3).</p>` },

    { id: "i6", t: "Le parcours en largeur (avec une file)", h: `
<p>Depuis un sommet de départ, on visite d’abord ses voisins (distance 1), puis leurs voisins non encore vus (distance 2), et ainsi de suite. On utilise une <b>file</b> et on <b>marque</b> chaque sommet dès qu’il est découvert, pour ne jamais l’enfiler deux fois. C’est le parcours en largeur des arbres (chapitre 7), avec le marquage en plus, car un graphe peut contenir des cycles.</p>
[[c8-largeur]]
[[w-parcours-graphe]]
<p>Chaque sommet est enfilé et défilé une fois, chaque liste de voisins lue une fois : le coût est de l’ordre de <i>n</i> + <i>m</i> (avec une vraie file en temps constant ; ici <code>pop(0)</code> est linéaire, <code>collections.deque</code> ferait mieux).</p>` },

    { id: "i7", t: "Le parcours en profondeur (pile ou récursivité)", h: `
<p>Le parcours en <b>profondeur</b> part d’un sommet, va vers un voisin non visité, puis vers un voisin de celui-ci… le plus loin possible ; bloqué, il revient au dernier sommet qui a encore un voisin non visité. C’est la méthode du fil d’Ariane dans un labyrinthe. On l’écrit récursivement (la pile d’exécution fait le travail, chapitre 2) ou avec une <b>pile</b> explicite :</p>
[[c8-profondeur]]
<p>Les deux ordres diffèrent (la pile ressort les voisins dans l’ordre inverse), mais ce sont tous deux des parcours en profondeur. Seule la structure change entre largeur et profondeur : <b>file</b> d’un côté, <b>pile</b> de l’autre. Choisis « en profondeur » dans l’animation ci-dessus pour le voir.</p>
<p>Application immédiate : un graphe non orienté est <b>connexe</b> si un parcours depuis n’importe quel sommet les atteint tous.</p>
[[c8-connexe]]` },

    { id: "i8", t: "Chercher un chemin", h: `
<p>Pour trouver un chemin de <code>depart</code> à <code>arrivee</code>, on fait un parcours en mémorisant pour chaque sommet découvert le sommet d’où l’on vient (son <b>parent</b>). Une fois l’arrivée atteinte, on remonte les parents jusqu’au départ. Avec un parcours <b>en largeur</b>, le chemin obtenu est un <b>plus court</b> chemin en nombre d’arêtes.</p>
[[c8-chemin]]
<div class="boite hp"><div class="lab"># pour aller plus loin : graphes pondérés</div><p>Quand les arêtes ont des longueurs différentes, le parcours en largeur ne suffit plus. L’algorithme de Dijkstra (1959) généralise l’idée avec une file de priorité ; c’est le principe du protocole de routage OSPF (chapitre réseaux) et des GPS. Il n’est pas exigible en tant que tel.</p></div>` },

    { id: "i9", t: "Repérer un cycle", h: `
<p>Dans un graphe <b>non orienté</b>, un parcours en profondeur rencontre un cycle quand il trouve un voisin <b>déjà visité</b> qui n’est pas le sommet d’où il vient (son parent) : il existe alors deux chemins différents vers ce sommet.</p>
[[c8-cycle]]
<p>Dans un graphe <b>orienté</b>, on distingue trois états : jamais vu, <b>en cours</b> (encore dans la pile d’appels), terminé. Un arc vers un sommet « en cours » referme un cycle. Exemple utile : des prérequis circulaires (A exige B, qui exige A) rendent un planning impossible.</p>
[[c8-cycle-oriente]]
<p>Les deux fonctions pas à pas : regarde la couleur des sommets et la pile d’appels au moment où l’arc (ou l’arête) qui referme le cycle est examiné.</p>
[[w-cycle]]` }
  ],
  pieges: [
    { t: "Oublier de marquer les sommets visités", h: `[[c8-p-marquage]]<p>Dès qu’il y a un cycle (ici A-B-A), le parcours tourne indéfiniment. On marque un sommet <b>dès qu’on le découvre</b> (avant de l’enfiler) et on n’enfile que des sommets non marqués.</p>` },
    { t: "Créer une matrice avec [[0] * n] * n", h: `[[c8-p-matrice]]<p>Les <i>n</i> lignes sont le même objet (alias, chapitre 1). Écrire <code>[[0] * n for _ in range(n)]</code>.</p>` },
    { t: "Oublier l’arête retour d’un graphe non orienté", h: `<p>Ajouter <code>b</code> aux voisins de <code>a</code> sans ajouter <code>a</code> aux voisins de <code>b</code> crée un graphe orienté sans le vouloir : les parcours depuis <code>b</code> ne voient plus <code>a</code>.</p>` },
    { t: "Confondre file et pile", h: `<p>Largeur ↔ <b>file</b> (<code>pop(0)</code>), profondeur ↔ <b>pile</b> (<code>pop()</code>). Changer l’un pour l’autre change complètement l’ordre de visite, et seul le parcours en largeur donne des plus courts chemins.</p>` },
    { t: "Croire qu’un graphe est connexe", h: `<p>Un parcours depuis un sommet n’atteint que sa « composante ». Pour traiter tous les sommets (détection de cycle, par exemple), on relance un parcours depuis chaque sommet non encore visité.</p>` },
    { t: "Sortir des limites d’une grille", h: `<p>Pour un labyrinthe en grille, l’indice −1 est accepté par Python (il désigne la dernière ligne !) : il faut tester <code>0 &lt;= l &lt; nb_lignes</code>, pas seulement <code>l &lt; nb_lignes</code>. Voir l’exercice pratique 2.</p>` }
  ],
  retenir: `
<h2>Vocabulaire</h2>
<div class="tab-wrap"><table><tr><th>mot</th><th>sens</th></tr>
<tr><td>sommet, arête, arc</td><td>élément ; lien non orienté ; lien orienté</td></tr>
<tr><td>degré</td><td>nombre de voisins (orienté : entrant / sortant)</td></tr>
<tr><td>chemin, cycle</td><td>suite de sommets adjacents ; chemin qui revient au départ</td></tr>
<tr><td>connexe</td><td>chaque sommet est relié à chaque autre par un chemin</td></tr>
<tr><td>pondéré</td><td>chaque arête porte un poids (distance, coût)</td></tr></table></div>
<h2>Représentations</h2>
<div class="tab-wrap"><table><tr><th></th><th>matrice d’adjacence</th><th>listes de successeurs</th></tr>
<tr><td>en Python</td><td><code>M[i][j]</code> vaut 1 (ou le poids)</td><td><code>g = {"A": ["B", "C"], …}</code></td></tr>
<tr><td>place</td><td><i>n</i>²</td><td><i>n</i> + <i>m</i></td></tr>
<tr><td>voisins ?</td><td>un accès</td><td>parcourir une liste</td></tr>
<tr><td>non orienté</td><td>symétrique</td><td>chaque arête dans les deux listes</td></tr></table></div>
<h2>Le parcours générique</h2>
[[c8-retenir]]
<ul><li>Largeur (file) : distances croissantes, plus courts chemins en nombre d’arêtes.</li><li>Profondeur (pile ou récursivité) : connexité, cycles, labyrinthes.</li><li>Chemin : mémoriser le parent, remonter depuis l’arrivée.</li><li>Cycle (non orienté) : voisin déjà vu qui n’est pas le parent.</li><li>Coût d’un parcours (listes de voisins) : de l’ordre de <i>n</i> + <i>m</i>.</li></ul>`,
  predis: [
    { code: "c8-x1", niv: "facile", rep: "La somme de chaque ligne est le degré du sommet : 2, 3, 2, 1. La matrice est symétrique (graphe non orienté) : <code>M[3][1] == M[1][3]</code>." },
    { code: "c8-x2", niv: "moyen", rep: "4 sommets, 4 arcs (1→2, 1→3, 2→4, 3→4) : c’est un graphe orienté. Les prédécesseurs de 4 sont 2 et 3." },
    { code: "c8-x3", niv: "moyen", rep: "Depuis W : V (distance 1), puis les voisins de V non vus, T et U (distance 2), puis S (distance 3)." },
    { code: "c8-x4", niv: "difficile", rep: "S → T (premier voisin) → V (voisin de T non vu) → U (premier voisin non vu de V) ; U n’a plus de voisin non vu, retour à V → W." }
  ],
  ep: [
    { titre: "Un réseau d’amis", enonce: `<p>Un réseau social est un graphe non orienté représenté par un dictionnaire : chaque personne est associée à la liste de ses amis.</p>[[c8-ep1-fourni]]`,
      questions: [
        { q: "Le programme affiche <code>['Linus']</code> pour les amis de Grace, alors qu’elle est aussi amie avec Ada et Alan. Expliquer et corriger <code>ajouter_lien</code>.", c: `<p>Seul <code>b</code> est ajouté aux amis de <code>a</code> : le graphe devient orienté. L’amitié étant réciproque, il faut aussi <code>reseau[b].append(a)</code>.</p>` },
        { q: "Compléter <code>amis_communs</code>.", c: `<p><code>return [x for x in reseau[a] if x in reseau[b]]</code>.</p>` },
        { q: "Écrire <code>suggestions(reseau, a)</code> : les amis d’amis de <code>a</code> qui ne sont ni <code>a</code> ni déjà ses amis, sans doublon. Écrire des tests.", c: `[[c8-ep1-corr]]` },
        { q: "À l’oral : à quelle distance de <code>a</code> sont les sommets suggérés ? Comment trouver tous ceux à distance 3 ?", c: `<p>À distance 2 exactement. Pour une distance quelconque, on fait un parcours en largeur depuis <code>a</code> et on garde les sommets dont la distance vaut 3.</p>` }
      ] },
    { titre: "Sortir du labyrinthe", enonce: `<p>Un labyrinthe est une grille : <code>#</code> est un mur, <code>S</code> le départ, <code>E</code> la sortie. On cherche le nombre minimal de pas (haut, bas, gauche, droite) avec un parcours en largeur.</p>[[c8-ep2-fourni]]`,
      questions: [
        { q: "Compter à la main le nombre minimal de pas pour <code>LABY</code>. Le programme affiche 3 : où est l’erreur ? Corriger.", c: `<p>Il faut 5 pas : (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,3). La fonction <code>voisins</code> accepte les indices <b>négatifs</b> : depuis S, la case (−1, 0) est acceptée, et Python la lit comme la dernière ligne. Le parcours « traverse » le bord de la grille. Il faut tester <code>0 &lt;= a</code> et <code>0 &lt;= b</code> : c’est un débordement de tableau (chapitre 4).</p>` },
        { q: "Pourquoi un parcours en largeur, et pas en profondeur, pour le nombre <b>minimal</b> de pas ?", c: `<p>Le parcours en largeur découvre les cases par distance croissante : la première fois qu’il atteint E, c’est par un plus court chemin. Un parcours en profondeur trouve un chemin, pas forcément le plus court.</p>` },
        { q: "Écrire des tests : labyrinthe sans issue, sortie voisine du départ, labyrinthe « en serpent ».", c: `[[c8-ep2-corr]]` },
        { q: "À l’oral : que représentent les sommets et les arêtes du graphe ici ? Pourquoi le dictionnaire <code>dist</code> sert-il aussi de marquage ?", c: `<p>Sommets : les cases libres ; arêtes : deux cases libres voisines. Une case reçoit une distance dès qu’elle est découverte : tester <code>v not in dist</code> évite de l’enfiler deux fois.</p>` }
      ] }
  ],
  ecrit: { titre: "Un réseau de refuges de montagne", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite. Les noms de refuges sont fictifs.",
    enonce: `<p>Des sentiers relient cinq refuges : Lac–Col, Lac–Pic, Col–Pic, Col–Gîte, Gîte–Source. Les sentiers se parcourent dans les deux sens. On numérote les refuges dans l’ordre Lac (0), Col (1), Pic (2), Gîte (3), Source (4).</p>`,
    questions: [
      { q: "Ce graphe est-il orienté ? Donner sa matrice d’adjacence.", pts: "1 pt", c: `<p>Non orienté (sentiers dans les deux sens) : la matrice est symétrique.</p><pre class="mono petit">      Lac Col Pic Gîte Source
Lac  [ 0,  1,  1,  0,   0 ]
Col  [ 1,  0,  1,  1,   0 ]
Pic  [ 1,  1,  0,  0,   0 ]
Gîte [ 0,  1,  0,  0,   1 ]
Source[0,  0,  0,  1,   0 ]</pre>` },
      { q: "Donner sa représentation par un dictionnaire de listes de voisins.", pts: "0,5 pt", c: `<p class="mono petit">{"Lac": ["Col", "Pic"], "Col": ["Lac", "Pic", "Gîte"], "Pic": ["Lac", "Col"], "Gîte": ["Col", "Source"], "Source": ["Gîte"]}</p>` },
      { q: "Écrire une fonction <code>degre_max(g)</code> qui renvoie le plus grand degré du graphe <code>g</code> (dictionnaire).", pts: "0,75 pt", c: `<p><code>return max(len(g[s]) for s in g)</code> : 3, pour le Col.</p>` },
      { q: "Donner l’ordre de visite d’un parcours en largeur depuis Source, et la distance (en sentiers) de chaque refuge à Source.", pts: "1 pt", c: `<p>Source (0), Gîte (1), Col (2), puis Lac et Pic (3). Ordre : Source, Gîte, Col, Lac, Pic.</p>` },
      { q: "Écrire une fonction <code>accessibles(g, depart, n)</code> qui renvoie la liste des refuges à au plus <code>n</code> sentiers de <code>depart</code>.", pts: "1,5 pt", c: `<p>Parcours en largeur avec un dictionnaire des distances, puis on garde les sommets de distance ≤ <code>n</code>.</p>[[c8-ecrit-corr]]` },
      { q: "Le graphe contient-il un cycle ? Si l’on supprime le sentier Lac–Pic, en contient-il encore ? Justifier.", pts: "1,25 pt", c: `<p>Oui : Lac–Col–Pic–Lac. Sans le sentier Lac–Pic, il reste 4 sentiers pour 5 refuges, tous reliés : c’est un arbre, donc il n’y a plus de cycle (un graphe connexe à <i>n</i> sommets et <i>n</i> − 1 arêtes est un arbre).</p>` }
    ],
    methode: `<p>Pour un exercice de graphes : dessine le graphe, écris les deux représentations proprement (en-têtes de lignes et de colonnes pour la matrice), et pour un parcours, fais un tableau de l’état de la file (ou de la pile) et des sommets marqués à chaque étape.</p>` },
  qcm: [
    { q: "Dans un graphe non orienté, le degré d’un sommet est…", c: ["sa distance au départ", "son nombre de voisins", "son numéro", "le nombre de cycles qui le contiennent"], a: 1, e: "Nombre d’arêtes qui le touchent.", ref: "i1" },
    { q: "Un réseau d’abonnements (je suis quelqu’un qui ne me suit pas forcément) se modélise par…", c: ["un graphe non orienté", "un graphe orienté", "un arbre binaire", "une file"], a: 1, e: "La relation n’est pas symétrique : arcs orientés.", ref: "i2" },
    { q: "La matrice d’adjacence d’un graphe non orienté est toujours…", c: ["triangulaire", "symétrique", "remplie de 1", "de taille 2 × 2"], a: 1, e: "S’il y a une arête de i à j, il y en a une de j à i.", ref: "i3" },
    { q: "Combien de cases a la matrice d’adjacence d’un graphe à 100 sommets ?", c: ["100", "200", "1 000", "10 000"], a: 3, e: "n² = 100 × 100.", ref: "i3" },
    { q: "Dans <code>g = {\"A\": [\"B\", \"C\"], \"B\": [\"A\"], \"C\": [\"A\"]}</code>, quel est le degré de A ?", c: ["1", "2", "3", "0"], a: 1, e: "Longueur de la liste des voisins de A.", ref: "i4" },
    { q: "Pourquoi <code>[[0] * n] * n</code> est-il une mauvaise façon de créer une matrice ?", c: ["Elle est trop grande", "Les n lignes sont le même objet : modifier une case modifie toute la colonne", "Elle contient des None", "Elle n’est pas carrée"], a: 1, e: "Alias : utiliser une compréhension de liste.", ref: "i4" },
    { q: "Quelle structure le parcours en largeur utilise-t-il ?", c: ["Une pile", "Une file", "Un ABR", "Une matrice"], a: 1, e: "On traite les sommets dans l’ordre de leur découverte : FIFO.", ref: "i6" },
    { q: "Quel parcours donne les plus courts chemins en nombre d’arêtes ?", c: ["En profondeur", "En largeur", "Les deux", "Aucun"], a: 1, e: "Il visite les sommets par distance croissante.", ref: "i6" },
    { q: "Pourquoi marquer les sommets déjà découverts ?", c: ["Pour trier le résultat", "Pour ne pas les traiter plusieurs fois, ni boucler sur un cycle", "Pour calculer le degré", "Ce n’est utile que pour les arbres"], a: 1, e: "Sans marquage, un cycle fait tourner le parcours indéfiniment.", ref: "i6" },
    { q: "Une version récursive du parcours en profondeur utilise implicitement…", c: ["une file", "la pile d’exécution", "un dictionnaire trié", "une matrice"], a: 1, e: "Chaque appel en attente est un cadre de la pile d’appels.", ref: "i7" },
    { q: "Pour reconstruire un chemin trouvé par un parcours, on mémorise…", c: ["le degré de chaque sommet", "le parent (le sommet d’où l’on vient) de chaque sommet découvert", "la matrice", "le nombre de cycles"], a: 1, e: "On remonte ensuite les parents depuis l’arrivée.", ref: "i8" },
    { q: "Dans un graphe non orienté, un parcours en profondeur révèle un cycle quand…", c: ["un sommet a un degré pair", "il trouve un voisin déjà visité qui n’est pas son parent", "la pile est vide", "le graphe est connexe"], a: 1, e: "Il existe alors deux chemins différents vers ce voisin.", ref: "i9" },
    { q: "Un graphe connexe à 10 sommets et 9 arêtes…", c: ["contient forcément un cycle", "est un arbre (pas de cycle)", "est orienté", "n’existe pas"], a: 1, e: "Connexe avec n − 1 arêtes : c’est un arbre.", ref: "i9" }
  ],
  cartes: [
    { r: "Graphe", v: "Sommets reliés par des arêtes (non orienté) ou des arcs (orienté), éventuellement pondérés." },
    { r: "Degré", v: "Nombre de voisins d’un sommet ; orienté : degré entrant et degré sortant." },
    { r: "Chemin / cycle", v: "Suite de sommets adjacents / chemin qui revient à son départ." },
    { r: "Connexe", v: "Tout sommet est relié à tout autre par un chemin (non orienté)." },
    { r: "Matrice d’adjacence", v: "M[i][j] = 1 (ou le poids) s’il y a une arête de i vers j. Symétrique si non orienté. n² cases." },
    { r: "Listes de successeurs", v: "Dictionnaire sommet → liste de voisins. Place ≈ n + m." },
    { r: "Prédécesseurs", v: "Dans un graphe orienté, les sommets qui ont un arc vers s." },
    { r: "Parcours en largeur", v: "File ; marquer à la découverte ; distances croissantes ; plus courts chemins (en arêtes)." },
    { r: "Parcours en profondeur", v: "Pile ou récursivité ; s’enfoncer le plus loin possible puis revenir." },
    { r: "Chercher un chemin", v: "Parcours en mémorisant le parent de chaque sommet ; remonter depuis l’arrivée." },
    { r: "Cycle (non orienté)", v: "Voisin déjà visité qui n’est pas le parent." },
    { r: "Cycle (orienté)", v: "Arc vers un sommet « en cours » (encore dans la pile d’appels)." },
    { r: "Coût d’un parcours", v: "De l’ordre de n + m avec des listes de voisins et une vraie file." },
    { r: "Euler, 1736", v: "Les sept ponts de Königsberg : début de la théorie des graphes." }
  ]
});
