/* ===================== Réseaux — protocoles de routage (RIP, OSPF) ===================== */
/* Réseau d'exemple commun au cours, au code Python et aux deux animations (débits en Mbit/s) */
var ROUT_RES = {
  pos: { A: [40, 120], B: [200, 34], C: [130, 206], D: [282, 206], E: [228, 128], F: [382, 120] },
  liens: [["A", "B", 10], ["B", "F", 10], ["A", "C", 100], ["C", "D", 100], ["D", "F", 50], ["C", "E", 20], ["E", "F", 100]]
};

C("rout-table", String.raw`
import ipaddress

# Table de routage du routeur R1 : (réseau de destination, passerelle, interface)
TABLE_R1 = [
    ("192.168.1.0/24", "direct",   "eth0"),   # réseau local de R1
    ("10.0.0.0/30",    "direct",   "eth1"),   # liaison vers R2 (R2 = 10.0.0.2)
    ("10.0.1.0/30",    "direct",   "eth2"),   # liaison vers R3 (R3 = 10.0.1.2)
    ("192.168.2.0/24", "10.0.0.2", "eth1"),   # réseau local de R2
    ("192.168.3.0/24", "10.0.1.2", "eth2"),   # réseau local de R3
    ("0.0.0.0/0",      "10.0.1.2", "eth2"),   # route par défaut : tout le reste
]

def prochain_saut(table, ip):
    """Renvoie (passerelle, interface) de la route la plus précise qui contient ip."""
    adresse = ipaddress.ip_address(ip)
    meilleure = None
    for reseau, passerelle, interface in table:
        r = ipaddress.ip_network(reseau)
        if adresse in r and (meilleure is None or r.prefixlen > meilleure[0].prefixlen):
            meilleure = (r, passerelle, interface)
    return meilleure[1], meilleure[2]

print(prochain_saut(TABLE_R1, "192.168.2.17"))
print(prochain_saut(TABLE_R1, "192.168.1.5"))
print(prochain_saut(TABLE_R1, "8.8.8.8"))`, { fichier: "table_routage.py", out: "('10.0.0.2', 'eth1')\n('direct', 'eth0')\n('10.0.1.2', 'eth2')" });

C("rout-reseau", String.raw`
# Le réseau de l'animation : liaisons et débits (Mbit/s)
LIENS = {("A", "B"): 10, ("B", "F"): 10, ("A", "C"): 100, ("C", "D"): 100,
         ("D", "F"): 50, ("C", "E"): 20, ("E", "F"): 100}

def voisins(liens):
    """Dictionnaire {routeur: liste triée de ses voisins directs}."""
    v = {}
    for a, b in liens:
        v.setdefault(a, []).append(b)
        v.setdefault(b, []).append(a)
    return {r: sorted(v[r]) for r in sorted(v)}

print(voisins(LIENS))`, { fichier: "reseau.py", out: "{'A': ['B', 'C'], 'B': ['A', 'F'], 'C': ['A', 'D', 'E'], 'D': ['C', 'F'], 'E': ['C', 'F'], 'F': ['B', 'D', 'E']}" });

C("rout-rip", String.raw`
INFINI = 16          # pour RIP, 16 sauts veut dire « inaccessible »

def tour_rip(tables, vois):
    """Un tour : chaque routeur reçoit les tables de ses voisins (telles qu'au début du tour).
    tables[r] = {destination: (distance en sauts, passerelle)}. Renvoie True si une table a changé."""
    annonces = {r: dict(tables[r]) for r in tables}
    change = False
    for r in sorted(tables):
        for v in vois[r]:
            for dest, (d, passerelle) in annonces[v].items():
                if passerelle == r:              # v ne renvoie pas à r une route apprise de r
                    continue
                nd = min(d + 1, INFINI)          # un saut de plus pour passer par v
                if dest not in tables[r]:
                    if nd < INFINI:
                        tables[r][dest] = (nd, v)
                        change = True
                elif tables[r][dest][1] == v:    # v est déjà ma passerelle : je crois sa nouvelle distance
                    if tables[r][dest][0] != nd:
                        tables[r][dest] = (nd, v)
                        change = True
                elif nd < tables[r][dest][0]:    # route strictement plus courte : on l'adopte
                    tables[r][dest] = (nd, v)
                    change = True
    return change

vois = voisins(LIENS)
tables = {r: {r: (0, None)} for r in vois}      # au départ, chacun ne connaît que lui-même
tour = 0
while tour_rip(tables, vois):
    tour = tour + 1
    print("après le tour", tour, ":", tables["A"])
print("table de A :", sorted(tables["A"].items()))`, { deps: ["rout-reseau"], fichier: "rip.py", out: "après le tour 1 : {'A': (0, None), 'B': (1, 'B'), 'C': (1, 'C')}\naprès le tour 2 : {'A': (0, None), 'B': (1, 'B'), 'C': (1, 'C'), 'F': (2, 'B'), 'D': (2, 'C'), 'E': (2, 'C')}\ntable de A : [('A', (0, None)), ('B', (1, 'B')), ('C', (1, 'C')), ('D', (2, 'C')), ('E', (2, 'C')), ('F', (2, 'B'))]" });

C("rout-route", String.raw`
def route(tables, depart, arrivee):
    """Suit les passerelles de proche en proche, comme le paquet lui-même."""
    chemin = [depart]
    r = depart
    while r != arrivee:
        d, passerelle = tables[r][arrivee]
        assert d < INFINI, "destination inaccessible"
        r = passerelle
        chemin.append(r)
    return chemin

print(route(tables, "A", "F"), route(tables, "E", "B"))`, { deps: ["rout-reseau", "rout-rip"], out: "['A', 'B', 'F'] ['E', 'F', 'B']" });

C("rout-panne", String.raw`
del LIENS[("B", "F")]                          # la liaison B-F tombe
vois = voisins(LIENS)
for r, perdu in (("B", "F"), ("F", "B")):      # B et F marquent inaccessibles les routes
    for dest, (d, passerelle) in tables[r].items():   # qui passaient par la liaison
        if passerelle == perdu:
            tables[r][dest] = (INFINI, perdu)
tour = 0
while tour_rip(tables, vois):
    tour = tour + 1
print("stable après", tour, "tours ;", route(tables, "A", "F"), route(tables, "B", "F"))`, { deps: ["rout-reseau", "rout-rip", "rout-route"], out: "stable après 3 tours ; ['A', 'C', 'D', 'F'] ['B', 'A', 'C', 'D', 'F']" });

C("rout-cout", String.raw`
def cout_ospf(debit):
    """Coût d'une liaison : 10**8 / débit (débit en bit/s)."""
    return 10 ** 8 / debit

for nom, debit in [("10 Mbit/s", 10e6), ("100 Mbit/s", 100e6), ("1 Gbit/s", 1e9)]:
    print(nom, "->", cout_ospf(debit))`, { out: "10 Mbit/s -> 10.0\n100 Mbit/s -> 1.0\n1 Gbit/s -> 0.1" });

C("rout-dijkstra", String.raw`
def graphe_ospf(liens):
    """{routeur: {voisin: coût}}, avec coût = 100 / débit en Mbit/s (soit 10**8 / débit en bit/s)."""
    g = {}
    for (a, b), debit in liens.items():
        c = 100 // debit
        g.setdefault(a, {})[b] = c
        g.setdefault(b, {})[a] = c
    return {s: g[s] for s in sorted(g)}      # routeurs rangés par ordre alphabétique

def dijkstra(g, depart):
    dist = {s: float("inf") for s in g}
    prec = {s: None for s in g}
    dist[depart] = 0
    a_traiter = sorted(g)                      # sommets dont la distance n'est pas définitive
    while a_traiter:
        s = min(a_traiter, key=lambda x: dist[x])   # le plus proche (à égalité : ordre alphabétique)
        a_traiter.remove(s)                    # sa distance est maintenant définitive
        for v, c in g[s].items():
            if dist[s] + c < dist[v]:          # passer par s est plus court
                dist[v] = dist[s] + c
                prec[v] = s
    return dist, prec

def chemin(prec, arrivee):
    ch = [arrivee]
    while prec[ch[0]] is not None:
        ch.insert(0, prec[ch[0]])
    return ch

LIENS_OSPF = {("A", "B"): 10, ("B", "F"): 10, ("A", "C"): 100, ("C", "D"): 100,
              ("D", "F"): 50, ("C", "E"): 20, ("E", "F"): 100}
g = graphe_ospf(LIENS_OSPF)
dist, prec = dijkstra(g, "A")
print(dist)
print(chemin(prec, "F"), chemin(prec, "E"), chemin(prec, "B"))`, { fichier: "ospf.py", out: "{'A': 0, 'B': 10, 'C': 1, 'D': 2, 'E': 5, 'F': 4}\n['A', 'C', 'D', 'F'] ['A', 'C', 'D', 'F', 'E'] ['A', 'B']" });

C("rout-tr-route", String.raw`
TABLES = {"A": {"F": "B"}, "B": {"F": "F"}, "F": {"F": None}}   # passerelle vers F

def route(depart, arrivee):
    chemin = [depart]
    r = depart
    while r != arrivee:
        r = TABLES[r][arrivee]       # le routeur r transmet à sa passerelle
        chemin.append(r)
    return chemin

print(route("A", "F"))`, { fichier: "route_pas_a_pas.py", trace: true, titreTrace: "route(\"A\", \"F\")", out: "['A', 'B', 'F']" });

/* prédis la sortie */
C("rout-x1", String.raw`
print(prochain_saut(TABLE_R1, "192.168.3.200"))
print(prochain_saut(TABLE_R1, "10.0.0.2"))
print(prochain_saut(TABLE_R1, "192.168.4.1"))`, { deps: ["rout-table"], out: "('10.0.1.2', 'eth2')\n('direct', 'eth1')\n('10.0.1.2', 'eth2')" });

C("rout-x2", String.raw`
g = {"X": {"Y": 4, "Z": 1}, "Y": {"X": 4, "Z": 2, "T": 1}, "Z": {"X": 1, "Y": 2, "T": 6}, "T": {"Y": 1, "Z": 6}}
dist, prec = dijkstra(g, "X")
print(dist["T"], chemin(prec, "T"))`, { deps: ["rout-dijkstra"], out: "4 ['X', 'Z', 'Y', 'T']" });

C("rout-x3", String.raw`
ligne = {("R1", "R2"): 1, ("R2", "R3"): 1, ("R3", "R4"): 1, ("R4", "R5"): 1}
vois = voisins(ligne)
tables = {r: {r: (0, None)} for r in vois}
tour = 0
while tour_rip(tables, vois):
    tour = tour + 1
print(tour, tables["R1"]["R5"])`, { deps: ["rout-reseau", "rout-rip"], out: "4 (4, 'R2')" });

C("rout-x4", String.raw`
print(graphe_ospf({("P", "Q"): 10, ("Q", "R"): 100, ("P", "R"): 20}))`, { deps: ["rout-dijkstra"], out: "{'P': {'Q': 10, 'R': 5}, 'Q': {'P': 10, 'R': 1}, 'R': {'Q': 1, 'P': 5}}" });

/* épreuve pratique */
C("rout-ep-fourni", String.raw`
# Tables de routage déjà calculées : TABLES[routeur][destination] = passerelle
TABLES = {
    "R1": {"R2": "R2", "R3": "R3", "R4": "R2"},
    "R2": {"R1": "R1", "R3": "R1", "R4": "R4"},
    "R3": {"R1": "R1", "R2": "R1", "R4": "R1"},
    "R4": {"R1": "R2", "R2": "R2", "R3": "R2"},
}

def route(tables, depart, arrivee):
    """Renvoie la liste des routeurs traversés par un paquet de depart à arrivee."""
    ...`, { fichier: "chemin.py", run: false, trous: [10] });

C("rout-ep-corr", String.raw`
TABLES = {
    "R1": {"R2": "R2", "R3": "R3", "R4": "R2"},
    "R2": {"R1": "R1", "R3": "R1", "R4": "R4"},
    "R3": {"R1": "R1", "R2": "R1", "R4": "R1"},
    "R4": {"R1": "R2", "R2": "R2", "R3": "R2"},
}

def route(tables, depart, arrivee):
    """Renvoie la liste des routeurs traversés ; lève une erreur en cas de boucle."""
    chemin = [depart]
    r = depart
    while r != arrivee:
        assert arrivee in tables[r], "pas de route de " + r + " vers " + arrivee
        r = tables[r][arrivee]
        assert r not in chemin, "boucle de routage : " + " -> ".join(chemin + [r])
        chemin.append(r)
    return chemin

def test_route():
    assert route(TABLES, "R1", "R1") == ["R1"]
    assert route(TABLES, "R3", "R4") == ["R3", "R1", "R2", "R4"]
    assert route(TABLES, "R4", "R3") == ["R4", "R2", "R1", "R3"]
    faux = {"R1": {"R4": "R2"}, "R2": {"R4": "R1"}}
    try:
        route(faux, "R1", "R4")
        assert False, "la boucle aurait dû être détectée"
    except AssertionError as e:
        assert str(e).startswith("boucle")

test_route()
print(route(TABLES, "R3", "R4"))`, { fichier: "chemin.py", out: "['R3', 'R1', 'R2', 'R4']" });

C("rout-ep-boucle", String.raw`
def route_naive(tables, depart, arrivee):
    chemin = [depart]
    r = depart
    while r != arrivee and len(chemin) < 10:     # garde-fou pour la démonstration
        r = tables[r][arrivee]
        chemin.append(r)
    return chemin

faux = {"R1": {"R4": "R2"}, "R2": {"R4": "R1"}}
print(route_naive(faux, "R1", "R4"))`, { out: "['R1', 'R2', 'R1', 'R2', 'R1', 'R2', 'R1', 'R2', 'R1', 'R2']" });

/* épreuve écrite : vérification des réponses */
C("rout-ecrit-verif", String.raw`
LIENS_E = {("R1", "R2"): 10, ("R2", "R6"): 10, ("R1", "R3"): 100, ("R3", "R4"): 100,
           ("R4", "R5"): 50, ("R5", "R6"): 100, ("R2", "R4"): 20}
vois = voisins(LIENS_E)
tables = {r: {r: (0, None)} for r in vois}
while tour_rip(tables, vois):
    pass
print("RIP :", {d: tables["R1"][d][0] for d in sorted(tables["R1"])}, route(tables, "R1", "R6"))
dist, prec = dijkstra(graphe_ospf(LIENS_E), "R1")
print("OSPF :", dist["R6"], chemin(prec, "R6"))
del LIENS_E[("R4", "R5")]
dist, prec = dijkstra(graphe_ospf(LIENS_E), "R1")
print("OSPF sans R4-R5 :", dist["R6"], chemin(prec, "R6"))`, { deps: ["rout-reseau", "rout-rip", "rout-route", "rout-dijkstra"], out: "RIP : {'R1': 0, 'R2': 1, 'R3': 1, 'R4': 2, 'R5': 3, 'R6': 2} ['R1', 'R2', 'R6']\nOSPF : 5 ['R1', 'R3', 'R4', 'R5', 'R6']\nOSPF sans R4-R5 : 17 ['R1', 'R3', 'R4', 'R2', 'R6']" });

/* ---------- dessin commun du réseau ---------- */
function routSVG(o) {
  /* o : { etiq(a, b, debit) -> texte, lien(a, b) -> classe, noeud(r) -> classe, jetons: [[a, b, cl]], h } */
  var P = ROUT_RES.pos, s = '<svg viewBox="0 0 422 ' + (o.h || 240) + '" role="img" aria-label="' + (o.aria || "Réseau de six routeurs") + '">';
  ROUT_RES.liens.forEach(function (l) {
    var a = P[l[0]], b = P[l[1]], cl = o.lien ? o.lien(l[0], l[1]) : "";
    s += '<line class="fil ' + cl + '" x1="' + a[0] + '" y1="' + a[1] + '" x2="' + b[0] + '" y2="' + b[1] + '"/>';
  });
  ROUT_RES.liens.forEach(function (l) {
    var a = P[l[0]], b = P[l[1]], t = o.etiq ? o.etiq(l[0], l[1], l[2]) : "";
    if (!t) return;
    var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, w = t.length * 6.6 + 8;
    s += '<rect class="cout-f" x="' + (mx - w / 2) + '" y="' + (my - 9) + '" width="' + w + '" height="17" rx="4"/><text class="cout" x="' + mx + '" y="' + (my + 4) + '" text-anchor="middle">' + t + "</text>";
  });
  (o.jetons || []).forEach(function (j, k) { var a = P[j[0]], b = P[j[1]]; s += archJeton("M" + a[0] + " " + a[1] + " L" + b[0] + " " + b[1], j[2] || "b", 1, 0); });
  Object.keys(P).forEach(function (r) {
    var p = P[r], cl = o.noeud ? o.noeud(r) : "";
    s += '<g class="nd ' + cl + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="17"/><text x="' + p[0] + '" y="' + (p[1] + 5) + '" text-anchor="middle">' + r + "</text></g>";
  });
  return s + (o.fin || "") + "</svg>";
}

/* ---------- animation : convergence de RIP ---------- */
WIDGETS_EXT["arch-rip"] = function (z, opt, O) {
  archStyle();
  var R = ["A", "B", "C", "D", "E", "F"], INF = 16;
  function vois(liens) { var v = {}; R.forEach(function (r) { v[r] = []; }); liens.forEach(function (l) { v[l[0]].push(l[1]); v[l[1]].push(l[0]); }); R.forEach(function (r) { v[r].sort(); }); return v; }
  function copie(T) { var c = {}; R.forEach(function (r) { c[r] = {}; Object.keys(T[r]).forEach(function (d) { c[r][d] = T[r][d].slice(); }); }); return c; }
  function tour(T, V) {
    var ann = copie(T), chg = [];
    R.forEach(function (r) {
      V[r].forEach(function (v) {
        Object.keys(ann[v]).sort().forEach(function (dest) {
          var d = ann[v][dest][0], nh = ann[v][dest][1];
          if (nh === r) return;
          var nd = Math.min(d + 1, INF), cur = T[r][dest];
          if (!cur) { if (nd < INF) { T[r][dest] = [nd, v]; chg.push(r + dest); } }
          else if (cur[1] === v) { if (cur[0] !== nd) { T[r][dest] = [nd, v]; chg.push(r + dest); } }
          else if (nd < cur[0]) { T[r][dest] = [nd, v]; chg.push(r + dest); }
        });
      });
    });
    return chg;
  }
  function chemin(T, a, b) { var c = [a], r = a; while (r !== b && c.length < 8) { r = T[r][b][1]; c.push(r); } return c; }
  function etapes(k) {
    var liens = ROUT_RES.liens.map(function (l) { return l; }), V = vois(liens), T = {}, E = [], n = 0, chg;
    R.forEach(function (r) { T[r] = {}; T[r][r] = [0, null]; });
    if (k === "rip") E.push({ T: copie(T), chg: [], liens: liens, msg: "Au départ, chaque routeur ne connaît que <b>lui-même</b> (distance 0). Les débits sont indiqués sur les liaisons : RIP ne s’en sert <b>pas</b>, il ne compte que les <b>sauts</b>. Ligne de A dans le tableau : la table de routage de A." });
    while ((chg = tour(T, V)).length) {
      n++;
      if (k === "rip") E.push({ T: copie(T), chg: chg, liens: liens, jetons: true, msg: "<b>Tour " + n + "</b> : chaque routeur envoie sa table à ses voisins (jetons). Il garde une route annoncée par un voisin si elle est <b>nouvelle</b> ou <b>plus courte</b>, en ajoutant 1 saut et en notant ce voisin comme passerelle. " + chg.length + " entrées changent (en orange)." + (n === 1 ? " Chacun apprend ses voisins directs." : n === 2 ? " Les routes à 2 sauts apparaissent : par exemple A apprend F par B." : "") });
    }
    if (k === "rip") {
      E.push({ T: copie(T), chg: [], liens: liens, jetons: true, msg: "<b>Tour " + (n + 1) + "</b> : les annonces n’apportent plus rien. Les tables ont <b>convergé</b> en " + n + " tours. (Un vrai routeur RIP envoie sa table toutes les 30 secondes.)" });
      var c = chemin(T, "A", "F");
      E.push({ T: copie(T), chg: [], liens: liens, route: c, msg: "Un paquet de A vers F suit les passerelles : A l’envoie à B (table de A : « F, 2 sauts, par B »), B l’envoie à F. Route <b>" + c.join(" → ") + "</b> : 2 sauts, mais par deux liaisons lentes à 10 Mbit/s. RIP ne voit pas les débits." });
      return E;
    }
    /* panne de la liaison B-F, à partir des tables convergées */
    E.push({ T: copie(T), chg: [], liens: liens, route: chemin(T, "A", "F"), msg: "Les tables ont convergé (animation précédente) : un paquet de A vers F passe par <b>A → B → F</b>." });
    liens = liens.filter(function (l) { return !(l[0] === "B" && l[1] === "F"); }); V = vois(liens);
    var perte = [];
    [["B", "F"], ["F", "B"]].forEach(function (x) { Object.keys(T[x[0]]).forEach(function (d) { if (T[x[0]][d][1] === x[1]) { T[x[0]][d] = [INF, x[1]]; perte.push(x[0] + d); } }); });
    E.push({ T: copie(T), chg: perte, liens: liens, panne: true, msg: "<b>Panne</b> : la liaison B–F est coupée. B et F le détectent et marquent <b>inaccessibles</b> (distance 16, notée ∞) les routes qui l’empruntaient. Les autres routeurs ne savent encore rien : la table de A indique toujours « F par B »." });
    n = 0;
    while ((chg = tour(T, V)).length) {
      n++;
      E.push({ T: copie(T), chg: chg, liens: liens, panne: true, jetons: true, msg: "<b>Tour " + n + " après la panne</b> : " + (n === 1 ? "A reçoit de B « F : ∞ » ; comme B est sa passerelle pour F, il le croit… mais C lui annonce « F à 2 sauts » : A adopte F à 3 sauts par C. B apprend D et E par A." : n === 2 ? "B apprend F à 4 sauts par A ; D et E retrouvent B par C." : "F retrouve B (4 sauts, par D).") + " " + chg.length + (chg.length > 1 ? " entrées changent." : " entrée change.") });
    }
    var c2 = chemin(T, "A", "F");
    E.push({ T: copie(T), chg: [], liens: liens, panne: true, route: c2, msg: "Stable après " + n + " tours. Le paquet de A vers F passe maintenant par <b>" + c2.join(" → ") + "</b> (3 sauts). Pendant la reconvergence, certains paquets ont pu être perdus : avec RIP, elle prend plusieurs échanges de 30 s." });
    return E;
  }
  function dessine(scene, e, i, E, saut) {
    var enRoute = function (a, b) { if (!e.route) return false; for (var k = 0; k < e.route.length - 1; k++) if ((e.route[k] === a && e.route[k + 1] === b) || (e.route[k] === b && e.route[k + 1] === a)) return true; return false; };
    var present = function (a, b) { return e.liens.some(function (l) { return l[0] === a && l[1] === b; }); };
    var jetons = [];
    if (e.jetons && !saut) e.liens.forEach(function (l) { jetons.push([l[0], l[1], "b"]); jetons.push([l[1], l[0], "v"]); });
    var svg = routSVG({ aria: "Réseau de six routeurs échangeant leurs tables RIP", etiq: function (a, b, d) { return present(a, b) ? d + " Mb/s" : "coupée"; },
      lien: function (a, b) { return !present(a, b) ? "ko" : enRoute(a, b) ? "on" : ""; },
      noeud: function (r) { return e.route && e.route.indexOf(r) >= 0 ? "on" : ""; }, jetons: jetons });
    var t = '<div class="ar-tab"><table><caption>tables de routage : distance en sauts · passerelle</caption><tr><th>routeur</th>' + R.map(function (d) { return "<th>→ " + d + "</th>"; }).join("") + "</tr>";
    R.forEach(function (r) {
      t += "<tr><th>" + r + "</th>" + R.map(function (d) {
        var x = e.T[r][d], cl = e.chg.indexOf(r + d) >= 0 && !saut ? "chg" : (e.chg.indexOf(r + d) >= 0 ? "chg" : "");
        var txt = !x ? "·" : x[0] === 0 ? "0" : x[0] >= INF ? "∞" : x[0] + "·" + x[1];
        return '<td class="' + cl + '">' + txt + "</td>";
      }).join("") + "</tr>";
    });
    scene.innerHTML = svg + t + "</table></div>";
  }
  O.lecteur(z, { titre: "RIP : les tables convergent tour par tour", sous: "vecteur de distance", choix: [{ k: "rip", t: "construction des tables" }, { k: "panne", t: "panne de la liaison B–F" }],
    etapes: etapes, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 3000 });
};

/* ---------- animation : Dijkstra pour OSPF ---------- */
WIDGETS_EXT["arch-dijkstra"] = function (z, opt, O) {
  archStyle();
  var R = ["A", "B", "C", "D", "E", "F"];
  function cout(d) { return 100 / d; }
  function etapes() {
    var g = {}; R.forEach(function (r) { g[r] = {}; });
    ROUT_RES.liens.forEach(function (l) { g[l[0]][l[1]] = cout(l[2]); g[l[1]][l[0]] = cout(l[2]); });
    var dist = {}, prec = {}, fait = [], E = [];
    R.forEach(function (r) { dist[r] = Infinity; prec[r] = null; }); dist.A = 0;
    function snap(o) { o.dist = Object.assign({}, dist); o.prec = Object.assign({}, prec); o.fait = fait.slice(); return o; }
    E.push(snap({ msg: "OSPF : chaque routeur connaît <b>toute la carte</b> du réseau et le <b>coût</b> de chaque liaison : coût = 10⁸ / débit en bit/s (10 Mbit/s → 10, 20 → 5, 50 → 2, 100 → 1). A calcule ses meilleures routes avec l’algorithme de <b>Dijkstra</b>. Au départ : A à 0, les autres à ∞." }));
    var rest = R.slice();
    while (rest.length) {
      var s = rest.reduce(function (m, x) { return dist[x] < dist[m] ? x : m; }, rest[0]);
      rest.splice(rest.indexOf(s), 1); fait.push(s);
      var maj = [], ignore = [];
      Object.keys(g[s]).sort().forEach(function (v) {
        if (fait.indexOf(v) >= 0) return;
        var nd = dist[s] + g[s][v];
        if (nd < dist[v]) { maj.push(v + " : " + dist[s] + " + " + g[s][v] + " = " + nd + (dist[v] === Infinity ? "" : " &lt; " + dist[v]) + " → <b>" + v + " = " + nd + "</b> par " + s); dist[v] = nd; prec[v] = s; }
        else ignore.push(v + " : " + dist[s] + " + " + g[s][v] + " = " + nd + " ≥ " + dist[v] + ", inchangé");
      });
      E.push(snap({ s: s, maj: maj.map(function (m) { return m.charAt(0); }), msg: "On choisit le routeur non traité <b>le plus proche</b> : <b>" + s + "</b> (" + dist[s] + "). Sa distance est définitive. " + (maj.length || ignore.length ? "On examine ses voisins non traités : " + maj.concat(ignore).join(" ; ") + "." : "Tous ses voisins sont déjà traités.") }));
    }
    function ch(b) { var c = [b]; while (prec[c[0]]) c.unshift(prec[c[0]]); return c; }
    E.push(snap({ arbre: true, route: ch("F"), msg: "Terminé. Les liaisons vertes forment l’<b>arbre des plus courts chemins</b> depuis A. Vers F : <b>" + ch("F").join(" → ") + "</b>, coût " + dist.F + " (1 + 1 + 2), alors que RIP choisissait A → B → F (coût 20, deux liaisons à 10 Mbit/s). Vers E : " + ch("E").join(" → ") + " (5), moins cher que A → C → E (6)." }));
    return E;
  }
  function dessine(scene, e, i, E, saut) {
    var arbre = function (a, b) { return (e.prec[b] === a && e.fait.indexOf(b) >= 0) || (e.prec[a] === b && e.fait.indexOf(a) >= 0); };
    var surRoute = function (a, b) { if (!e.route) return false; for (var k = 0; k < e.route.length - 1; k++) if ((e.route[k] === a && e.route[k + 1] === b) || (e.route[k] === b && e.route[k + 1] === a)) return true; return false; };
    var svg = routSVG({ aria: "Réseau OSPF et algorithme de Dijkstra depuis A", etiq: function (a, b, d) { return String(100 / d); },
      lien: function (a, b) { return surRoute(a, b) ? "on" : arbre(a, b) ? "ok" : (e.s && (a === e.s || b === e.s) ? "on" : ""); },
      noeud: function (r) { return r === e.s ? "on" : e.fait.indexOf(r) >= 0 ? "ok" : ""; },
      fin: R.map(function (r) { var p = ROUT_RES.pos[r], d = e.dist[r]; return '<text class="pt" x="' + (p[0] + (r === "F" ? -2 : 0)) + '" y="' + (p[1] + (p[1] > 150 ? 32 : -24)) + '" text-anchor="middle">' + (d === Infinity ? "∞" : d) + "</text>"; }).join("") });
    var t = '<div class="ar-tab"><table><caption>distance depuis A · prédécesseur (vert : définitif)</caption><tr>' + R.map(function (r) { return "<th>" + r + "</th>"; }).join("") + "</tr><tr>" + R.map(function (r) {
      var d = e.dist[r], cl = e.fait.indexOf(r) >= 0 ? "fixe" : (e.maj && e.maj.indexOf(r) >= 0 ? "chg" : "");
      return '<td class="' + cl + '">' + (d === Infinity ? "∞" : d) + (e.prec[r] ? " · " + e.prec[r] : "") + "</td>";
    }).join("") + "</tr></table></div>";
    scene.innerHTML = svg + t;
  }
  O.lecteur(z, { titre: "OSPF : Dijkstra s’étend depuis A", sous: "état de liens", etapes: etapes, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 3200 });
};

CH.push({
  id: "rout", court: "routage", fichier: "routage.py",
  titre: "Protocoles de routage",
  rubrique: "Rubrique « Architectures matérielles, systèmes d’exploitation et réseaux » : protocoles de routage",
  accroche: "Comment un paquet traverse Internet de routeur en routeur : tables de routage, RIP (nombre de sauts, Bellman-Ford) et OSPF (coût selon le débit, Dijkstra), et ce qui se passe quand une liaison tombe.",
  essentiel: [
    "Un <b>routeur</b> relie plusieurs réseaux ; pour chaque paquet, il consulte sa <b>table de routage</b> : réseau de destination → <b>passerelle</b> (prochain routeur) et interface de sortie.",
    "Les tables sont remplies automatiquement par un <b>protocole de routage</b> : les routeurs échangent des informations et calculent les meilleures routes.",
    "<b>RIP</b> : chaque routeur envoie sa table à ses voisins ; la métrique est le <b>nombre de sauts</b> (au plus 15 ; 16 = inaccessible). Algorithme de Bellman-Ford distribué.",
    "<b>OSPF</b> : chaque routeur connaît toute la carte du réseau ; la métrique est un <b>coût</b> lié au débit (coût = 10⁸ / débit en bit/s) ; chaque routeur calcule ses routes avec l’algorithme de <b>Dijkstra</b>.",
    "Les deux protocoles peuvent choisir des routes <b>différentes</b> : RIP ignore les débits, OSPF préfère plusieurs liaisons rapides à une liaison lente."
  ],
  attendus: [
    "Identifier, suivant le protocole de routage utilisé, la route empruntée par un paquet.",
    "Le programme précise : « en mode débranché, les tables de routage étant données, on se réfère au nombre de sauts (protocole RIP) ou au coût des routes (protocole OSPF) » ; « le lien avec les algorithmes de recherche de chemin sur un graphe est mis en évidence »."
  ],
  intro: `<div class="boite ex"><div class="lab"># un grand classique de l’écrit</div><p>Presque chaque session propose un exercice de routage : un schéma de réseau, des tables à compléter pour RIP, des coûts à calculer pour OSPF, la route d’un paquet, puis « la liaison X tombe : que devient la route ? ». Méthode et modèle dans l’onglet exercices.</p></div>`,
  idees: [
    { id: "i1", t: "Rappels : paquets, adresses, routeurs", h: `
<p>En Première, tu as vu qu’un message est découpé en <b>paquets</b> ; chaque paquet IP porte l’adresse IP de son expéditeur et celle de son destinataire. Une adresse comme <code>192.168.2.17/24</code> se lit en deux parties : les 24 premiers bits désignent le <b>réseau</b> (<code>192.168.2.0/24</code>), le reste désigne la <b>machine</b> dans ce réseau.</p>
<p>À l’intérieur d’un réseau local, les machines communiquent directement (par le commutateur). Pour sortir du réseau, un paquet passe par un <b>routeur</b> : un équipement relié à plusieurs réseaux, qui décide vers quel voisin faire suivre chaque paquet. Sur Internet, un paquet traverse en général une dizaine de routeurs ou plus ; chacun ne connaît que le <b>prochain saut</b>, pas le trajet complet.</p>
<div class="code"><div class="tete"><span class="f">terminal (exemple de sortie, adresses anonymisées)</span></div><pre><code><span class="l" data-n="1">$ traceroute exemple.org</span><span class="l" data-n="2"> 1  box.maison (192.168.1.254)   2.1 ms</span><span class="l" data-n="3"> 2  10.75.12.1                   8.4 ms</span><span class="l" data-n="4"> 3  …                           11.0 ms</span><span class="l" data-n="5"> …</span></code></pre></div>
<p>La commande <code>traceroute</code> (<code>tracert</code> sous Windows) affiche les routeurs successifs traversés vers une destination, avec le temps d’aller-retour : chaque ligne est un <b>saut</b>.</p>` },

    { id: "i2", t: "La table de routage", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>La <b>table de routage</b> d’un routeur associe à chaque <b>réseau de destination</b> : la <b>passerelle</b> (adresse du prochain routeur, ou « direct » si le réseau est relié au routeur), l’<b>interface</b> de sortie, et souvent une <b>métrique</b> (distance ou coût de la route).</p></div>
<p>Exemple : le routeur R1 est relié à son réseau local <code>192.168.1.0/24</code> (interface <code>eth0</code>), à R2 par <code>eth1</code> et à R3 par <code>eth2</code>. Une <b>route par défaut</b> (<code>0.0.0.0/0</code>) dit où envoyer tout ce qui ne correspond à aucune autre ligne (vers Internet).</p>
[[rout-table]]
<p>Quand plusieurs lignes conviennent (la route par défaut convient toujours), le routeur prend la plus <b>précise</b> : celle dont le masque est le plus long. Les tables peuvent être écrites à la main par l’administrateur (<b>routage statique</b>), ce qui ne s’adapte pas aux pannes ; sur un grand réseau, elles sont calculées par un <b>protocole de routage</b> (<b>routage dynamique</b>).</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>La règle de la route la plus précise (« plus long préfixe ») n’est pas exigible. À l’écrit, les tables données ont une ligne par réseau de destination ; il suffit de lire la passerelle.</p></div>` },

    { id: "i3", t: "RIP : compter les sauts", h: `
<p><b>RIP</b> (<i>Routing Information Protocol</i>) est un protocole à <b>vecteur de distance</b> :</p>
<ul><li>la <b>métrique</b> est le <b>nombre de sauts</b> : le nombre de routeurs à traverser (un réseau directement relié est à distance 1 dans les tables RIP réelles ; dans les exercices, on compte souvent les liaisons entre routeurs : <b>lis la convention de l’énoncé</b>) ;</li>
<li>chaque routeur envoie régulièrement (toutes les 30 secondes) sa table à ses <b>voisins directs</b>, et seulement à eux ;</li>
<li>à la réception, il ajoute 1 à chaque distance annoncée ; il adopte la route si la destination est <b>nouvelle</b> ou si la distance est <b>strictement plus petite</b>, avec ce voisin comme passerelle ;</li>
<li>une distance de <b>16</b> signifie « inaccessible » : RIP est limité aux réseaux de diamètre 15 au plus.</li></ul>
<p>Chaque routeur applique ainsi, de proche en proche, l’<b>algorithme de Bellman-Ford</b> : après k tours, il connaît les meilleures routes de k sauts au plus. Sur le réseau ci-dessous, les tables convergent en 2 tours.</p>
[[w-arch-rip]]
<p>En Python, avec une table <code>{destination: (distance, passerelle)}</code> par routeur :</p>
[[rout-reseau]]
[[rout-rip]]
<p>Un paquet suit ensuite les passerelles, routeur après routeur :</p>
[[rout-route]]
[[w-trace|rout-tr-route]]
<div class="boite hp"><div class="lab"># pour aller plus loin : le comptage à l’infini</div><p>Le code n’annonce pas une route au voisin qui en est la passerelle (« horizon partagé », <i>split horizon</i>). Sans cette règle, après une panne, deux routeurs peuvent se renvoyer une route morte en augmentant sa distance d’un saut à chaque échange, jusqu’à 16 : c’est le « comptage à l’infini », qui explique le choix d’une limite aussi basse que 16.</p></div>` },

    { id: "i4", t: "RIP face à une panne", h: `
<p>Quand une liaison tombe, les deux routeurs qui la bordent marquent inaccessibles (distance 16) les routes qui l’empruntaient et l’annoncent. Les voisins qui utilisaient ces routes les abandonnent et adoptent la meilleure alternative annoncée par un autre voisin. Au bout de quelques tours, les tables ont <b>reconvergé</b>. Rejoue l’animation ci-dessus avec « panne de la liaison B–F ».</p>
[[rout-panne]]
<p>Avec des échanges toutes les 30 secondes, la reconvergence de RIP peut prendre plusieurs minutes sur un grand réseau, pendant lesquelles des paquets sont perdus ou tournent en boucle. C’est une des raisons pour lesquelles les opérateurs lui préfèrent OSPF.</p>` },

    { id: "i5", t: "OSPF : le coût des liaisons et Dijkstra", h: `
<p><b>OSPF</b> (<i>Open Shortest Path First</i>) est un protocole à <b>état de liens</b> :</p>
<ul><li>chaque routeur décrit ses liaisons (voisins et état) dans de petits messages diffusés à <b>tous</b> les routeurs de la zone ; chacun reconstitue ainsi la <b>carte complète</b> du réseau, un <b>graphe pondéré</b> ;</li>
<li>le <b>poids</b> d’une liaison est son <b>coût</b>, d’autant plus faible que le débit est grand ; la formule la plus courante dans les sujets est <b>coût = 10⁸ / débit</b> (débit en bit/s) ; l’énoncé la rappelle toujours, et certains prennent une autre référence (10⁹ par exemple) ;</li>
<li>chaque routeur calcule lui-même les plus courts chemins vers toutes les destinations avec l’<b>algorithme de Dijkstra</b>, et en déduit sa table.</li></ul>
[[rout-cout]]
<div class="tab-wrap"><table><tr><th>débit</th><th>10 Mbit/s</th><th>20 Mbit/s</th><th>50 Mbit/s</th><th>100 Mbit/s</th><th>1 Gbit/s</th></tr><tr><td>coût</td><td>10</td><td>5</td><td>2</td><td>1</td><td>0,1</td></tr></table></div>
<p>Le <b>coût d’une route</b> est la somme des coûts de ses liaisons. <b>Dijkstra</b> part du routeur source (distance 0), et répète : choisir le routeur non traité de plus petite distance (elle est alors définitive), puis mettre à jour ses voisins si passer par lui est moins cher.</p>
[[w-arch-dijkstra]]
[[rout-dijkstra]]
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Dans les routeurs réels, le débit de référence (10⁸ bit/s par défaut chez la plupart des constructeurs) se règle, et un coût ne descend pas sous 1 : sans réglage, une liaison à 1 Gbit/s et une à 100 Mbit/s auraient le même coût. Les grands réseaux OSPF sont découpés en <b>zones</b>.</p></div>` },

    { id: "i6", t: "Comparer RIP et OSPF", h: `
<p>Sur le même réseau, pour aller de A à F :</p>
<ul><li><b>RIP</b> choisit <b>A → B → F</b> : 2 sauts, le minimum. Mais ces deux liaisons sont à 10 Mbit/s.</li>
<li><b>OSPF</b> choisit <b>A → C → D → F</b> : 3 sauts, mais un coût de 1 + 1 + 2 = 4, contre 10 + 10 = 20 par B.</li></ul>
<div class="tab-wrap"><table><tr><th></th><th>RIP</th><th>OSPF</th></tr>
<tr><td>type</td><td>vecteur de distance</td><td>état de liens</td></tr>
<tr><td>ce que sait un routeur</td><td>les distances annoncées par ses voisins</td><td>la carte complète du réseau</td></tr>
<tr><td>métrique</td><td>nombre de sauts (max 15)</td><td>coût = 10⁸ / débit, additionné</td></tr>
<tr><td>algorithme</td><td>Bellman-Ford, distribué</td><td>Dijkstra, sur chaque routeur</td></tr>
<tr><td>après une panne</td><td>reconvergence lente (échanges toutes les 30 s)</td><td>rapide : l’état de la liaison est diffusé, chacun recalcule</td></tr>
<tr><td>usage</td><td>petits réseaux</td><td>réseaux d’entreprise et d’opérateurs</td></tr></table></div>
<p>Dans les deux cas, le routage revient à chercher un <b>plus court chemin dans un graphe</b> : routeurs = sommets, liaisons = arêtes, pondérées par 1 (RIP) ou par le coût (OSPF). C’est le lien avec la rubrique « Algorithmique » que demande le programme.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1956-1959 <b>·</b></span> Lester Ford (1956) et Richard Bellman (1958) publient l’algorithme qui porte leurs noms ; Edsger Dijkstra publie le sien en 1959. <span class="commit">1969 <b>·</b></span> ARPANET, l’ancêtre d’Internet, relie ses premiers nœuds. <span class="commit">1988 <b>·</b></span> RIP est décrit dans la RFC 1058. <span class="commit">1989 <b>·</b></span> première spécification d’OSPF (RFC 1131) ; la version 2, utilisée aujourd’hui pour IPv4, est décrite dans la RFC 2328 (1998).</p></div>
<div class="boite hp"><div class="lab"># et entre opérateurs ?</div><p>RIP et OSPF fonctionnent à l’intérieur d’un même domaine (le réseau d’une entreprise ou d’un opérateur). Entre domaines, Internet utilise un autre protocole, BGP, qui choisit les routes selon des accords entre opérateurs. Hors programme.</p></div>` }
  ],
  pieges: [
    { t: "Compter les routeurs au lieu des liaisons (ou l’inverse)", h: `<p>Selon les sujets, la distance RIP vers un réseau directement relié vaut 0 ou 1. Lis la convention et applique-la à <b>toutes</b> les lignes ; la route choisie, elle, ne change pas.</p>` },
    { t: "Additionner des débits", h: `<p>On n’additionne pas les débits : on additionne les <b>coûts</b> (10⁸ / débit). Une route de deux liaisons à 100 Mbit/s coûte 1 + 1 = 2, moins qu’une liaison à 10 Mbit/s (coût 10).</p>` },
    { t: "Oublier qu’une table ne donne que le prochain saut", h: `<p>Pour trouver la route complète d’un paquet, on lit la table du routeur de départ, puis celle de la passerelle, et ainsi de suite jusqu’à la destination.</p>` },
    { t: "Dans Dijkstra, figer une distance trop tôt", h: `<p>Une distance n’est définitive que lorsque le routeur est choisi comme le plus proche des non traités. Avant, elle peut encore baisser (E passe de 6 à 5 dans l’exemple).</p>` },
    { t: "Croire que RIP connaît les débits", h: `<p>RIP ne regarde que le nombre de sauts. S’il existe deux routes de même nombre de sauts, il garde la première apprise, même si l’autre est bien plus rapide.</p>` }
  ],
  retenir: `
<h2>Table de routage</h2>
<p>Destination (réseau) → passerelle (prochain routeur ou « direct »), interface, métrique. Route par défaut <code>0.0.0.0/0</code>. Un routeur ne connaît que le <b>prochain saut</b>.</p>
<h2>RIP</h2>
<ul><li>Vecteur de distance : chacun envoie sa table à ses <b>voisins</b> (toutes les 30 s).</li><li>Métrique : <b>nombre de sauts</b> ; 16 = inaccessible (max 15).</li><li>On garde une route nouvelle ou <b>strictement</b> plus courte (distance annoncée + 1, passerelle = le voisin).</li><li>Bellman-Ford distribué ; reconvergence lente après une panne.</li></ul>
<h2>OSPF</h2>
<ul><li>État de liens : chacun connaît la <b>carte complète</b>.</li><li>Coût d’une liaison = <b>10⁸ / débit</b> (bit/s) : 10 Mbit/s → 10 ; 100 Mbit/s → 1 ; 1 Gbit/s → 0,1. Coût d’une route = somme.</li><li>Plus courts chemins par <b>Dijkstra</b> : choisir le non-traité le plus proche, mettre à jour ses voisins.</li></ul>
<h2>Méthode d’exercice</h2>
<ol><li>Dessine le graphe (routeurs, liaisons, débits ou coûts).</li><li>RIP : compte les sauts de chaque route possible, garde la plus courte.</li><li>OSPF : calcule les coûts, fais Dijkstra (ou compare toutes les routes si le réseau est petit).</li><li>Panne : retire la liaison et recommence.</li></ol>`,
  predis: [
    { code: "rout-x1", niv: "facile", rep: "<code>192.168.3.200</code> est dans <code>192.168.3.0/24</code> : passerelle R3. <code>10.0.0.2</code> est dans le réseau de liaison <code>10.0.0.0/30</code>, directement relié par eth1. <code>192.168.4.1</code> ne correspond qu’à la route par défaut : R3, par eth2." },
    { code: "rout-x2", niv: "moyen", rep: "Dijkstra depuis X : Z (1), puis Y par Z (1 + 2 = 3 &lt; 4), puis T par Y (3 + 1 = 4 &lt; 1 + 6 = 7). Le chemin direct X–Y (4) n’est pas le meilleur." },
    { code: "rout-x3", niv: "moyen", rep: "Sur une ligne de 5 routeurs, R1 apprend R2 au tour 1, R3 au tour 2… R5 au tour 4. Un tour de plus ne change rien : la boucle s’arrête avec <code>tour</code> = 4. R5 est à 4 sauts, par R2." },
    { code: "rout-x4", niv: "facile", rep: "Coûts 100 / débit en Mbit/s : 10 → 10, 100 → 1, 20 → 5. Le dictionnaire de R est rempli dans l’ordre où ses liaisons apparaissent : d’abord Q, puis P." }
  ],
  ep: [
    { titre: "Suivre un paquet de table en table", enonce: `<p>On connaît les tables de routage de quatre routeurs (destination → passerelle). On veut la liste des routeurs traversés par un paquet.</p>[[rout-ep-fourni]]`,
      questions: [
        { q: "Écrire <code>route(tables, depart, arrivee)</code>.", c: `<p>Partir de <code>depart</code> et, tant qu’on n’est pas arrivé, lire <code>tables[r][arrivee]</code> pour passer au routeur suivant, en l’ajoutant à la liste.</p>` },
        { q: "Des tables mal configurées peuvent créer une <b>boucle de routage</b>. Que fait une version naïve sur l’exemple ci-dessous ?", code: "[[rout-ep-boucle|nosortie]]", c: `[[rout-ep-boucle]]<p>R1 envoie à R2, qui renvoie à R1 : le paquet tourne indéfiniment (la version naïve ne s’arrête que grâce au garde-fou). Dans un vrai réseau, le champ <b>TTL</b> du paquet IP, diminué de 1 à chaque routeur, finit par le détruire.</p>` },
        { q: "Ajouter deux assertions : pas de route connue, et boucle détectée (un routeur déjà visité). Écrire un jeu de tests.", c: `[[rout-ep-corr]]` },
        { q: "À l’oral : ces tables sont-elles celles de RIP ? Comment le vérifier ?", c: `<p>R3 → R4 passe par R1 et R2 : 3 sauts. Il faudrait connaître les liaisons. Si R3 était relié directement à R4, RIP choisirait la route directe (1 saut) : les tables ne seraient pas celles de RIP.</p>` }
      ] }
  ],
  ecrit: { titre: "Routage dans un réseau de six routeurs", points: "≈ 8 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite. On compte la distance RIP en nombre de liaisons entre routeurs.",
    enonce: `<p>Six routeurs R1 à R6 sont reliés par les liaisons suivantes : R1–R2 (10 Mbit/s), R2–R6 (10 Mbit/s), R1–R3 (100 Mbit/s), R3–R4 (100 Mbit/s), R4–R5 (50 Mbit/s), R5–R6 (100 Mbit/s), R2–R4 (20 Mbit/s). Un ordinateur du réseau de R1 envoie un paquet à un serveur du réseau de R6.</p>`,
    questions: [
      { q: "Dessiner le graphe du réseau.", pts: "0,5 pt", c: `<p>Six sommets ; sept arêtes étiquetées par les débits. Repère la « diagonale » R2–R4 qui relie les deux chemins.</p>` },
      { q: "Le réseau utilise RIP. Donner la distance de R1 à chacun des autres routeurs, puis la route du paquet.", pts: "2 pts", c: `<p>R2 : 1 ; R3 : 1 ; R4 : 2 (par R3 ou par R2, égalité) ; R5 : 3 ; R6 : 2 (par R2). Route : <b>R1 → R2 → R6</b>, 2 sauts.</p>` },
      { q: "Le réseau utilise OSPF, avec coût = 10⁸ / débit (bit/s). Calculer le coût de chaque liaison.", pts: "1 pt", c: `<p>10 Mbit/s → 10 ; 20 Mbit/s → 5 ; 50 Mbit/s → 2 ; 100 Mbit/s → 1. Donc R1–R2 : 10, R2–R6 : 10, R1–R3 : 1, R3–R4 : 1, R4–R5 : 2, R5–R6 : 1, R2–R4 : 5.</p>` },
      { q: "Déterminer la route choisie par OSPF et son coût.", pts: "2 pts", c: `<p>R1 → R2 → R6 coûte 20 ; R1 → R3 → R4 → R5 → R6 coûte 1 + 1 + 2 + 1 = <b>5</b> ; R1 → R3 → R4 → R2 → R6 : 17 ; R1 → R2 → R4 → R5 → R6 : 18. OSPF choisit <b>R1 → R3 → R4 → R5 → R6</b>, coût 5.</p>` },
      { q: "La liaison R4–R5 tombe en panne. Quelle route OSPF prend-il ? Et RIP ?", pts: "1,5 pt", c: `<p>OSPF : R1 → R3 → R4 → R2 → R6 coûte 17, R1 → R2 → R6 coûte 20 : <b>R1 → R3 → R4 → R2 → R6</b>. RIP : la route R1 → R2 → R6 ne passait pas par R4–R5, elle ne change pas.</p>[[rout-ecrit-verif]]` },
      { q: "Pourquoi OSPF réagit-il plus vite à cette panne que RIP en général ?", pts: "1 pt", c: `<p>Avec OSPF, R4 et R5 diffusent aussitôt le nouvel état de leurs liaisons à tous les routeurs, qui recalculent leurs routes avec Dijkstra. Avec RIP, l’information ne progresse que de voisin en voisin, au rythme des échanges périodiques (30 s).</p>` }
    ],
    methode: `<p>Écris toujours le <b>détail des sommes</b> de coûts pour chaque route candidate : le correcteur note le raisonnement. Pour un réseau de plus de cinq ou six routeurs, applique Dijkstra en tableau (une ligne par étape) plutôt que d’énumérer les routes.</p>` },
  qcm: [
    { q: "Que contient une ligne de table de routage ?", c: ["L’adresse MAC de chaque machine", "Un réseau de destination et la passerelle (prochain saut) pour l’atteindre", "Le trajet complet jusqu’à la destination", "Le contenu des paquets"], a: 1, e: "Le routeur ne connaît que le prochain saut, avec l’interface et la métrique.", ref: "i2" },
    { q: "À quoi sert la route <code>0.0.0.0/0</code> ?", c: ["À bloquer les paquets", "C’est la route par défaut, pour toutes les destinations non listées", "À joindre le routeur lui-même", "À rien"], a: 1, e: "Elle convient à toute adresse ; on la prend quand aucune route plus précise ne convient.", ref: "i2" },
    { q: "Quelle est la métrique de RIP ?", c: ["Le débit", "Le nombre de sauts", "Le temps de réponse", "Le coût 10⁸ / débit"], a: 1, e: "RIP compte les routeurs traversés et ignore les débits.", ref: "i3" },
    { q: "Pour RIP, une distance de 16 signifie…", c: ["16 routeurs traversés", "destination inaccessible", "liaison à 16 Mbit/s", "priorité maximale"], a: 1, e: "La distance maximale utilisable est 15.", ref: "i3" },
    { q: "Un routeur RIP envoie sa table…", c: ["à tous les routeurs du réseau", "à ses voisins directs", "à un serveur central", "seulement en cas de panne"], a: 1, e: "Vecteur de distance : échanges de voisin à voisin, toutes les 30 secondes.", ref: "i3" },
    { q: "Le routeur X a une route vers N à 4 sauts. Son voisin Y lui annonce N à 2 sauts. X adopte…", c: ["N à 2 sauts par Y", "N à 3 sauts par Y", "N à 5 sauts", "rien : il garde 4"], a: 1, e: "2 + 1 = 3 &lt; 4 : nouvelle route, passerelle Y.", ref: "i3" },
    { q: "Quel algorithme RIP met-il en œuvre de façon distribuée ?", c: ["Dijkstra", "Bellman-Ford", "Boyer-Moore", "Le tri fusion"], a: 1, e: "Chaque échange améliore les distances d’un saut de plus.", ref: "i3" },
    { q: "Après une panne, pourquoi RIP met-il du temps à reconverger ?", c: ["Il recalcule tout avec Dijkstra", "L’information ne circule que de voisin en voisin, au rythme des échanges périodiques", "Il attend l’administrateur", "Il ne reconverge jamais"], a: 1, e: "Chaque tour d’échange fait progresser l’information d’un saut.", ref: "i4" },
    { q: "Avec la formule coût = 10⁸ / débit, quel est le coût d’une liaison à 100 Mbit/s ?", c: ["100", "10", "1", "0,1"], a: 2, e: "10⁸ / 10⁸ = 1.", ref: "i5" },
    { q: "Deux liaisons à 100 Mbit/s en série coûtent, pour OSPF…", c: ["2, moins qu’une liaison à 10 Mbit/s (10)", "200", "50", "autant qu’une liaison à 10 Mbit/s"], a: 0, e: "On additionne les coûts : 1 + 1 = 2.", ref: "i5" },
    { q: "Quel algorithme chaque routeur OSPF exécute-t-il ?", c: ["Bellman-Ford", "Dijkstra", "Le tri par insertion", "Aucun : il recopie la table de ses voisins"], a: 1, e: "Plus courts chemins sur la carte complète du réseau.", ref: "i5" },
    { q: "Dans Dijkstra, quand la distance d’un sommet devient-elle définitive ?", c: ["Dès qu’elle est calculée une première fois", "Quand il est choisi comme le non-traité le plus proche", "À la fin seulement", "Jamais"], a: 1, e: "Avant, elle peut encore diminuer.", ref: "i5" },
    { q: "Route A–B–F (deux liaisons à 10 Mbit/s) ou A–C–D–F (100, 100, 50 Mbit/s) : que choisissent RIP et OSPF ?", c: ["Tous deux A–B–F", "RIP : A–B–F ; OSPF : A–C–D–F", "RIP : A–C–D–F ; OSPF : A–B–F", "Tous deux A–C–D–F"], a: 1, e: "RIP minimise les sauts (2 contre 3) ; OSPF les coûts (4 contre 20).", ref: "i6" },
    { q: "Quel type de protocole est OSPF ?", c: ["À vecteur de distance", "À état de liens", "De chiffrement", "De transport"], a: 1, e: "Chaque routeur diffuse l’état de ses liaisons et reconstitue la carte complète.", ref: "i6" }
  ],
  cartes: [
    { r: "Routeur", v: "Équipement relié à plusieurs réseaux, qui transmet chaque paquet vers le prochain saut." },
    { r: "Table de routage", v: "Destination (réseau) → passerelle, interface, métrique." },
    { r: "Passerelle", v: "Adresse du prochain routeur vers la destination (ou « direct »)." },
    { r: "Route par défaut", v: "0.0.0.0/0 : pour toutes les destinations non listées." },
    { r: "Routage statique / dynamique", v: "Tables écrites à la main / calculées par un protocole de routage." },
    { r: "RIP", v: "Vecteur de distance ; métrique = nombre de sauts ; tables envoyées aux voisins toutes les 30 s." },
    { r: "Règle de mise à jour RIP", v: "Distance annoncée + 1 ; on adopte si destination nouvelle ou distance strictement plus petite." },
    { r: "16 pour RIP", v: "Distance « infinie » : destination inaccessible (max 15 sauts)." },
    { r: "Bellman-Ford", v: "Algorithme de plus courts chemins par améliorations successives ; distribué dans RIP." },
    { r: "OSPF", v: "État de liens ; chaque routeur connaît la carte ; métrique = coût ; Dijkstra." },
    { r: "Coût OSPF", v: "10⁸ / débit (bit/s) : 10 Mbit/s → 10, 100 Mbit/s → 1, 1 Gbit/s → 0,1." },
    { r: "Dijkstra", v: "Choisir le non-traité le plus proche (définitif), mettre à jour ses voisins, recommencer." },
    { r: "RIP ou OSPF après une panne", v: "RIP : lent, de voisin en voisin. OSPF : diffusion de l’état de la liaison, recalcul immédiat." },
    { r: "traceroute", v: "Commande qui affiche les routeurs successifs traversés vers une destination." },
    { r: "Repères", v: "Bellman-Ford (1956-1958), Dijkstra (1959), ARPANET (1969), RIP (RFC 1058, 1988), OSPF (RFC 1131, 1989)." }
  ]
});
