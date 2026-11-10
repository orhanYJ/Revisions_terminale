/* ===================== Systèmes d'exploitation — processus, ordonnancement, interblocage ===================== */
C("proc-fork", String.raw`
import os, sys

parent = os.getpid()                 # PID du processus qui exécute ce programme
print("avant fork : un seul processus")
sys.stdout.flush()                   # vider le tampon d'affichage avant la copie
pid = os.fork()                      # le système DUPLIQUE le processus courant
if pid == 0:                         # dans la copie (l'enfant), fork renvoie 0
    print("enfant : mon parent est le processus de départ :", os.getppid() == parent)
    sys.stdout.flush()
    os._exit(0)                      # l'enfant se termine
else:                                # dans le parent, fork renvoie le PID de l'enfant
    os.waitpid(pid, 0)               # le parent attend la fin de l'enfant
    print("parent : mon enfant avait un autre PID que moi :", pid != parent)`, { fichier: "fork.py", cmd: "python3 fork.py   # Linux ou macOS", out: "avant fork : un seul processus\nenfant : mon parent est le processus de départ : True\nparent : mon enfant avait un autre PID que moi : True" });

C("proc-donnees", String.raw`
# (nom, instant d'arrivée, durée d'exécution nécessaire)
PROCESSUS = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 1), ("P4", 4, 2)]

def chronogramme(gantt):
    """gantt : liste de tranches (nom, début, fin), dans l'ordre du temps.
    Renvoie une case par unité de temps ; '--' quand le processeur est libre."""
    cases = []
    for nom, debut, fin in gantt:
        cases = cases + ["--"] * (debut - len(cases)) + [nom] * (fin - debut)
    return " ".join(cases)`, { fichier: "ordonnancement.py", out: "" });

C("proc-fifo", String.raw`
def fifo(procs):
    """Premier arrivé, premier servi : chaque processus va jusqu'au bout."""
    t, gantt = 0, []
    for nom, arrivee, duree in sorted(procs, key=lambda p: p[1]):
        t = max(t, arrivee)              # le processeur attend si personne n'est prêt
        gantt.append((nom, t, t + duree))
        t = t + duree
    return gantt

print(chronogramme(fifo(PROCESSUS)))`, { deps: ["proc-donnees"], out: "P1 P1 P1 P1 P1 P2 P2 P2 P3 P4 P4" });

C("proc-rr", String.raw`
from collections import deque

def tourniquet(procs, quantum):
    """Chaque processus reçoit au plus quantum unités de temps, puis repasse en fin de file."""
    a_venir = deque(sorted(procs, key=lambda p: p[1]))
    reste = {nom: duree for nom, _, duree in procs}
    file = deque()                         # la file des processus prêts
    t, gantt = 0, []
    while a_venir or file:
        while a_venir and a_venir[0][1] <= t:
            file.append(a_venir.popleft()[0])
        if not file:                       # personne n'est prêt : on avance le temps
            t = a_venir[0][1]
            continue
        nom = file.popleft()               # l'ordonnanceur élit la tête de file
        tranche = min(quantum, reste[nom])
        gantt.append((nom, t, t + tranche))
        t = t + tranche
        reste[nom] = reste[nom] - tranche
        while a_venir and a_venir[0][1] <= t:   # arrivés pendant la tranche :
            file.append(a_venir.popleft()[0])   # ils passent AVANT le processus interrompu
        if reste[nom] > 0:
            file.append(nom)               # pas fini : retour en fin de file
    return gantt

print(chronogramme(tourniquet(PROCESSUS, 2)))
print(chronogramme(tourniquet(PROCESSUS, 1)))`, { deps: ["proc-donnees"], out: "P1 P1 P2 P2 P3 P1 P1 P4 P4 P2 P1\nP1 P2 P1 P3 P2 P1 P4 P2 P1 P4 P1" });

C("proc-prio", String.raw`
PRIORITE = {"P1": 2, "P2": 1, "P3": 3, "P4": 1}      # 1 = le plus prioritaire

def priorites(procs):
    """À chaque unité de temps, le processus prêt le plus prioritaire est élu
    (à priorité égale, le premier arrivé) : un nouveau venu plus prioritaire interrompt l'élu."""
    reste = {nom: duree for nom, _, duree in procs}
    t, gantt = 0, []
    while any(reste.values()):
        prets = [p for p in procs if p[1] <= t and reste[p[0]] > 0]
        if prets:
            nom = min(prets, key=lambda p: (PRIORITE[p[0]], p[1]))[0]
            if gantt and gantt[-1][0] == nom and gantt[-1][2] == t:
                gantt[-1] = (nom, gantt[-1][1], t + 1)      # on prolonge la tranche
            else:
                gantt.append((nom, t, t + 1))
            reste[nom] = reste[nom] - 1
        t = t + 1
    return gantt

print(chronogramme(priorites(PROCESSUS)))`, { deps: ["proc-donnees", "proc-rr"], out: "P1 P2 P2 P2 P4 P4 P1 P1 P1 P1 P3" });

C("proc-temps", String.raw`
def bilan(procs, gantt):
    fin = {}
    for nom, debut, f in gantt:
        fin[nom] = f                       # la dernière tranche donne l'instant de fin
    total = 0
    for nom, arrivee, duree in procs:
        sejour = fin[nom] - arrivee        # temps passé dans le système
        total = total + sejour
        print(nom, "séjour :", sejour, "attente :", sejour - duree)
    print("séjour moyen :", total / len(procs))

bilan(PROCESSUS, fifo(PROCESSUS))
bilan(PROCESSUS, tourniquet(PROCESSUS, 2))`, { deps: ["proc-donnees", "proc-fifo", "proc-rr"], out: "P1 séjour : 5 attente : 0\nP2 séjour : 7 attente : 4\nP3 séjour : 7 attente : 6\nP4 séjour : 7 attente : 5\nséjour moyen : 6.5\nP1 séjour : 11 attente : 6\nP2 séjour : 9 attente : 6\nP3 séjour : 3 attente : 2\nP4 séjour : 5 attente : 3\nséjour moyen : 7.0" });

C("proc-interblocage", String.raw`
import threading

imprimante, scanner = threading.Lock(), threading.Lock()   # deux ressources exclusives
rdv = threading.Barrier(2)                                 # pour synchroniser la démonstration
bilan = {}

def tache(nom, premiere, seconde):
    with premiere:                           # obtient sa première ressource
        rdv.wait()                           # ... pendant que l'autre obtient la sienne
        ok = seconde.acquire(timeout=0.5)    # attend la seconde (au plus 0,5 s ici)
        bilan[nom] = "a tout obtenu" if ok else "bloqué"
        if ok:
            seconde.release()
        rdv.wait()                           # personne ne libère avant la fin des deux attentes

p1 = threading.Thread(target=tache, args=("P1", imprimante, scanner))
p2 = threading.Thread(target=tache, args=("P2", scanner, imprimante))
p1.start(); p2.start(); p1.join(); p2.join()
print("P1", bilan["P1"], "| P2", bilan["P2"])`, { fichier: "interblocage.py", out: "P1 bloqué | P2 bloqué" });

C("proc-ordre", String.raw`
import threading

imprimante, scanner = threading.Lock(), threading.Lock()
bilan = {}

def tache(nom):
    with imprimante:                         # TOUS demandent d'abord l'imprimante...
        ok = scanner.acquire(timeout=0.5)    # ... puis le scanner
        bilan[nom] = "a tout obtenu" if ok else "bloqué"
        if ok:
            scanner.release()

p1 = threading.Thread(target=tache, args=("P1",))
p2 = threading.Thread(target=tache, args=("P2",))
p1.start(); p2.start(); p1.join(); p2.join()
print("P1", bilan["P1"], "| P2", bilan["P2"])`, { fichier: "ordre.py", out: "P1 a tout obtenu | P2 a tout obtenu" });

C("proc-cycle", String.raw`
def interblocage(attend):
    """attend : {processus: processus qui détient la ressource qu'il attend, ou None}.
    Renvoie True s'il existe un cycle d'attente (donc un interblocage)."""
    for depart in attend:
        p, vus = depart, []
        while p is not None and p not in vus:
            vus.append(p)
            p = attend[p]                  # on suit les flèches « attend »
        if p is not None:                  # on est retombé sur un processus déjà vu
            return True
    return False

print(interblocage({"P1": "P2", "P2": None}))
print(interblocage({"P1": "P2", "P2": "P3", "P3": "P1"}))
print(interblocage({"P1": "P2", "P2": "P3", "P3": None, "P4": "P1"}))`, { out: "False\nTrue\nFalse" });

C("proc-tr-rr", String.raw`
from collections import deque

file = deque([("A", 3), ("B", 2)])     # (nom, durée restante), tous prêts à t = 0
quantum = 2
t = 0
while file:
    nom, reste = file.popleft()          # l'ordonnanceur élit la tête de file
    tranche = min(quantum, reste)
    t = t + tranche
    if reste > tranche:
        file.append((nom, reste - tranche))   # pas fini : fin de file
    else:
        print(nom, "termine à", t)`, { fichier: "tourniquet_pas_a_pas.py", trace: true, titreTrace: "tourniquet, quantum 2", out: "B termine à 4\nA termine à 5" });

/* prédis la sortie */
C("proc-x1", String.raw`
print(chronogramme(fifo([("A", 0, 2), ("B", 5, 1), ("C", 1, 2)])))`, { deps: ["proc-donnees", "proc-fifo"], out: "A A C C -- B" });

C("proc-x2", String.raw`
print(chronogramme(tourniquet([("A", 0, 3), ("B", 0, 3)], 2)))`, { deps: ["proc-donnees", "proc-rr"], out: "A A B B A B" });

C("proc-x3", String.raw`
print(chronogramme(tourniquet([("A", 0, 4), ("B", 0, 1), ("C", 0, 2)], 10)))
print(chronogramme(fifo([("A", 0, 4), ("B", 0, 1), ("C", 0, 2)])))`, { deps: ["proc-donnees", "proc-fifo", "proc-rr"], out: "A A A A B C C\nA A A A B C C" });

C("proc-x4", String.raw`
print(interblocage({"P1": "P2", "P2": "P1", "P3": None}))
print(interblocage({"P1": None, "P2": "P1", "P3": "P2"}))`, { deps: ["proc-cycle"], out: "True\nFalse" });

/* épreuve pratique */
C("proc-ep-fourni", String.raw`
class Processus:
    def __init__(self, pid, duree):
        self.pid = pid
        self.reste = duree            # unités de temps encore nécessaires

class Ordonnanceur:
    """Ordonnanceur à tourniquet : file des prêts gérée comme une liste Python."""
    def __init__(self, quantum):
        self.quantum = quantum
        self.file = []                # la tête de file est self.file[0]

    def ajouter(self, p):
        self.file.append(p)

    def tranche(self):
        """Élit la tête de file, l'exécute au plus quantum unités, la remet en fin
        de file si elle n'a pas fini. Renvoie (pid, durée exécutée), ou None si la file est vide."""
        ...

    def executer(self):
        """Exécute tout ; renvoie la liste des PID dans l'ordre où ils ont fini."""
        termines = []
        while self.file != []:
            pid, d = self.tranche()
            ...
        return termines`, { fichier: "tourniquet.py", run: false, trous: [18, 25] });

C("proc-ep-corr", String.raw`
class Processus:
    def __init__(self, pid, duree):
        self.pid = pid
        self.reste = duree

class Ordonnanceur:
    def __init__(self, quantum):
        assert quantum > 0, "le quantum doit être positif"
        self.quantum = quantum
        self.file = []

    def ajouter(self, p):
        self.file.append(p)

    def tranche(self):
        if self.file == []:
            return None
        p = self.file.pop(0)                  # tête de file
        d = min(self.quantum, p.reste)
        p.reste = p.reste - d
        if p.reste > 0:
            self.file.append(p)               # pas fini : en fin de file
        return (p.pid, d)

    def executer(self):
        termines = []
        while self.file != []:
            pid, d = self.tranche()
            if pid not in [p.pid for p in self.file]:   # il n'est pas revenu dans la file : fini
                termines.append(pid)
        return termines

def test_ordonnanceur():
    o = Ordonnanceur(2)
    assert o.tranche() is None                       # file vide
    for pid, duree in [(10, 5), (11, 3), (12, 1)]:
        o.ajouter(Processus(pid, duree))
    assert o.tranche() == (10, 2)
    assert [p.pid for p in o.file] == [11, 12, 10]   # 10 repasse en fin de file
    o2 = Ordonnanceur(2)
    for pid, duree in [(10, 5), (11, 3), (12, 1)]:
        o2.ajouter(Processus(pid, duree))
    assert o2.executer() == [12, 11, 10]

test_ordonnanceur()
print("tous les tests passent")`, { fichier: "tourniquet.py", out: "tous les tests passent" });

C("proc-ep-cout", String.raw`
file = list(range(100_000))
import time
debut = time.perf_counter()
while file:
    file.pop(0)                 # chaque pop(0) décale tous les éléments suivants
lent = time.perf_counter() - debut

from collections import deque
file = deque(range(100_000))
debut = time.perf_counter()
while file:
    file.popleft()              # retrait en tête en temps constant
rapide = time.perf_counter() - debut
print(lent > rapide)`, { out: "True" });

/* épreuve écrite */
C("proc-ecrit-q", String.raw`
E = [("A", 0, 3), ("B", 1, 4), ("C", 2, 2), ("D", 3, 1)]
print(chronogramme(fifo(E)))
print(chronogramme(tourniquet(E, 2)))`, { deps: ["proc-donnees", "proc-fifo", "proc-rr"], out: "A A A B B B B C C D\nA A B B C C A D B B" });

/* ---------- animation : diagramme de Gantt ---------- */
WIDGETS_EXT["arch-gantt"] = function (z, opt, O) {
  archStyle();
  var P = [["P1", 0, 5, 2], ["P2", 1, 3, 1], ["P3", 2, 1, 3], ["P4", 4, 2, 1]];
  var COUL = { P1: "var(--bleu)", P2: "var(--vert)", P3: "var(--ambre)", P4: "var(--violet)" };
  var NOMS = { fifo: "FIFO", rr: "tourniquet, quantum 2", prio: "priorités" };
  function simule(algo) {
    var reste = {}, t = 0, cur = null, used = 0, file = [], S = [], debut = {};
    P.forEach(function (p) { reste[p[0]] = p[2]; });
    function fini() { return P.every(function (p) { return reste[p[0]] === 0; }); }
    while (!fini() && t < 40) {
      var arr = P.filter(function (p) { return p[1] === t; }).map(function (p) { return p[0]; });
      var ev = [], q = algo === "rr" ? 2 : Infinity;
      if (algo === "prio") {
        var prets = P.filter(function (p) { return p[1] <= t && reste[p[0]] > 0; });
        prets.sort(function (a, b) { return a[3] - b[3] || a[1] - b[1]; });
        var elu = prets.length ? prets[0][0] : null;
        if (cur && elu !== cur && reste[cur] > 0) ev.push("<b>" + elu + "</b> (priorité " + prets[0][3] + ") est plus prioritaire que " + cur + " : <b>" + cur + " est interrompu</b> et retourne dans les prêts.");
        cur = elu; file = prets.slice(1).map(function (p) { return p[0]; });
      } else {
        arr.forEach(function (n) { file.push(n); });
        if (cur && used === q) { file.push(cur); ev.push("Quantum épuisé : <b>" + cur + "</b> est interrompu et repasse en <b>fin de file</b>" + (arr.length ? ", après " + arr.join(", ") + " qui vient d’arriver" : "") + "."); cur = null; }
        if (!cur && file.length) { cur = file.shift(); used = 0; }
      }
      if (arr.length) ev.unshift(arr.join(", ") + " arrive" + (arr.length > 1 ? "nt" : "") + " : état <b>prêt</b>" + (algo === "prio" ? " (priorité " + arr.map(function (n) { return P.filter(function (p) { return p[0] === n; })[0][3]; }).join(", ") + ")" : ", en fin de file") + ".");
      if (cur && debut[cur] === undefined) { debut[cur] = t; ev.push("L’ordonnanceur élit <b>" + cur + "</b> pour la première fois."); }
      else if (cur && (!S.length || S[S.length - 1].cur !== cur)) ev.push("L’ordonnanceur élit <b>" + cur + "</b> (il lui reste " + reste[cur] + " unité" + (reste[cur] > 1 ? "s" : "") + ").");
      S.push({ t: t, cur: cur, file: file.slice(), ev: ev });
      if (cur) { reste[cur]--; used++; if (reste[cur] === 0) { S[S.length - 1].fin = cur; cur = null; } }
      t++;
    }
    return S;
  }
  function etapes(k) {
    var S = simule(k), E = [{ t: -1, S: S, msg: "Quatre processus arrivent à des instants différents (▼). Durées : P1 5, P2 3, P3 1, P4 2 unités" + (k === "prio" ? " ; priorités : P2 et P4 = 1 (la plus forte), P1 = 2, P3 = 3" : "") + ". Algorithme : <b>" + NOMS[k] + "</b>." + (k === "rr" ? " Règle : un processus qui arrive au moment où un autre est interrompu entre dans la file <b>avant</b> lui." : "") }];
    S.forEach(function (s, i) {
      var m = s.ev.join(" "), prev = i > 0 ? S[i - 1].cur : null;
      if (s.cur && prev === s.cur) m += (m ? " " : "") + "<b>" + s.cur + "</b> continue son exécution.";
      else if (!m) m = s.cur ? "<b>" + s.cur + "</b> s’exécute." : "Processeur inoccupé.";
      if (s.fin) m += " <b>" + s.fin + " a terminé</b> à l’instant " + (s.t + 1) + ".";
      E.push({ t: i, S: S, msg: "<span class=\"mono\">t = " + s.t + " → " + (s.t + 1) + "</span> · " + m });
    });
    var fin = {}; S.forEach(function (s) { if (s.fin) fin[s.fin] = s.t + 1; });
    var tot = 0, att = 0, det = P.map(function (p) { var sj = fin[p[0]] - p[1]; tot += sj; att += sj - p[2]; return p[0] + " " + sj + " (attente " + (sj - p[2]) + ")"; });
    E.push({ t: S.length, S: S, msg: "Bilan, temps de séjour (fin − arrivée) : " + det.join(" · ") + ". Moyenne : séjour " + String(tot / 4).replace(".", ",") + ", attente " + String(att / 4).replace(".", ",") + "." + (k === "prio" ? " P3, le moins prioritaire, a attendu le plus : avec beaucoup de processus prioritaires, il pourrait attendre indéfiniment (<b>famine</b>)." : k === "rr" ? " Le séjour moyen est plus long qu’en FIFO, mais P3, très court, a fini dès l’instant 5 : le tourniquet donne vite la main à chacun." : " P3, qui ne demandait qu’une unité, a attendu 6 unités derrière P1 et P2.") });
    return E;
  }
  function dessine(scene, e, i, E, saut) {
    var S = e.S, W = 30, X0 = 44, H = 30, Y0 = 16, n = S.length, larg = X0 + n * W + 12;
    var s = '<svg viewBox="0 0 ' + larg + " " + (Y0 + 4 * H + 104) + '" role="img" aria-label="Diagramme de Gantt de l’ordonnancement">';
    for (var u = 0; u <= n; u++) s += '<line x1="' + (X0 + u * W) + '" y1="' + (Y0 - 4) + '" x2="' + (X0 + u * W) + '" y2="' + (Y0 + 4 * H) + '" stroke="var(--ligne)" stroke-width="1"/><text class="pt" x="' + (X0 + u * W) + '" y="' + (Y0 + 4 * H + 14) + '" text-anchor="middle">' + u + "</text>";
    P.forEach(function (p, r) {
      var y = Y0 + r * H;
      s += '<text x="6" y="' + (y + 19) + '" style="font-weight:700;fill:' + COUL[p[0]] + '">' + p[0] + "</text>";
      s += '<path d="M' + (X0 + p[1] * W - 5) + " " + (y + 1) + " l10 0 l-5 7z" + '" style="fill:' + COUL[p[0]] + '"/>';
      S.forEach(function (st, k) {
        if (k > e.t || st.cur !== p[0]) return;
        var neuf = k === e.t && !saut;
        s += '<rect' + (neuf ? ' class="neuf"' : "") + ' x="' + (X0 + k * W + 1) + '" y="' + (y + 8) + '" width="' + (W - 2) + '" height="' + (H - 12) + '" rx="3" style="fill:' + COUL[p[0]] + ';opacity:.85"/>';
        if (st.fin === p[0]) s += '<text class="pt" x="' + (X0 + (k + 1) * W + 3) + '" y="' + (y + 21) + '">✓</text>';
      });
    });
    if (e.t >= 0 && e.t < n) s += '<rect x="' + (X0 + e.t * W) + '" y="' + (Y0 - 6) + '" width="' + W + '" height="' + (4 * H + 8) + '" fill="none" stroke="var(--ambre)" stroke-width="2.5" rx="3"/>';
    var y2 = Y0 + 4 * H + 34, st = e.t >= 0 && e.t < n ? S[e.t] : null;
    s += '<text class="pt" x="6" y="' + (y2 + 4) + '">processeur</text><text class="pt" x="6" y="' + (y2 + 50) + '">file des prêts</text>';
    s += '<rect x="96" y="' + (y2 - 14) + '" width="56" height="28" rx="6" style="fill:' + (st && st.cur ? COUL[st.cur] : "var(--bg2)") + ';stroke:var(--ligne2)"/><text x="124" y="' + (y2 + 5) + '" text-anchor="middle" style="font-weight:700;fill:' + (st && st.cur ? "var(--bg)" : "var(--encre3)") + '">' + (st ? st.cur || "libre" : "—") + "</text>";
    var f = st ? st.file : [];
    if (!f.length) s += '<text class="pt" x="100" y="' + (y2 + 50) + '">' + (st ? "vide" : "—") + "</text>";
    f.forEach(function (nm, j) { s += '<g' + (!saut ? ' class="neuf"' : "") + '><rect x="' + (96 + j * 50) + '" y="' + (y2 + 32) + '" width="44" height="28" rx="6" style="fill:var(--bg2);stroke:' + COUL[nm] + ';stroke-width:2"/><text x="' + (118 + j * 50) + '" y="' + (y2 + 51) + '" text-anchor="middle" style="font-weight:700;fill:' + COUL[nm] + '">' + nm + "</text></g>"; });
    if (f.length) s += '<text class="pt" x="' + (96 + f.length * 50) + '" y="' + (y2 + 51) + '">← tête à gauche</text>';
    scene.innerHTML = s + "</svg>";
  }
  O.lecteur(z, { titre: "l’ordonnanceur au travail", sous: "diagramme de Gantt", choix: [{ k: opt || "fifo", t: NOMS[opt || "fifo"] }].concat(["fifo", "rr", "prio"].filter(function (k) { return k !== (opt || "fifo"); }).map(function (k) { return { k: k, t: NOMS[k] }; })),
    etapes: etapes, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 1500 });
};

/* ---------- animation : interblocage ---------- */
WIDGETS_EXT["arch-interblocage"] = function (z, opt, O) {
  archStyle();
  var POS = { P1: [50, 112], P2: [350, 112], R1: [200, 34], R2: [200, 190] };
  var NOM = { R1: "imprimante", R2: "scanner" };
  var SC = {
    blocage: [
      { tient: [], att: [], et: { P1: "prêt", P2: "prêt" }, msg: "Deux processus doivent chacun imprimer un document scanné : il leur faut <b>les deux</b> ressources, qui ne peuvent servir qu’à un processus à la fois (accès <b>exclusif</b>). Flèche pleine : « la ressource est détenue par » ; flèche pointillée : « le processus attend »." },
      { tient: [["R1", "P1"]], att: [], et: { P1: "élu", P2: "prêt" }, msg: "P1 demande l’<b>imprimante</b> : elle est libre, le système la lui attribue." },
      { tient: [["R1", "P1"], ["R2", "P2"]], att: [], et: { P1: "prêt", P2: "élu" }, msg: "L’ordonnanceur passe la main à P2, qui demande le <b>scanner</b> : libre, il l’obtient." },
      { tient: [["R1", "P1"], ["R2", "P2"]], att: [["P1", "R2"]], et: { P1: "bloqué", P2: "prêt" }, msg: "P1 reprend et demande le scanner : <b>détenu par P2</b>. P1 passe à l’état <b>bloqué</b>, sans lâcher l’imprimante." },
      { tient: [["R1", "P1"], ["R2", "P2"]], att: [["P1", "R2"], ["P2", "R1"]], et: { P1: "bloqué", P2: "bloqué" }, cycle: true, msg: "P2 demande l’imprimante : <b>détenue par P1</b>. P2 est bloqué à son tour. P1 attend P2 qui attend P1 : c’est un <b>cycle d’attente</b>, un <b>interblocage</b> (<i>deadlock</i>). Aucun ne libérera jamais rien." },
      { tient: [["R1", "P1"], ["R2", "P2"]], att: [["P1", "R2"], ["P2", "R1"]], et: { P1: "bloqué", P2: "bloqué" }, cycle: true, msg: "Quatre conditions étaient réunies : ressources <b>exclusives</b>, processus qui <b>gardent</b> une ressource en en attendant une autre, ressources <b>non retirables</b> de force, <b>attente circulaire</b>. Il suffit d’en empêcher une : par exemple, imposer à tous le même <b>ordre</b> de demande." }
    ],
    ordre: [
      { tient: [], att: [], et: { P1: "prêt", P2: "prêt" }, msg: "Même situation, avec une règle : <b>tout le monde demande l’imprimante avant le scanner</b>." },
      { tient: [["R1", "P1"]], att: [], et: { P1: "élu", P2: "prêt" }, msg: "P1 demande l’imprimante et l’obtient." },
      { tient: [["R1", "P1"]], att: [["P2", "R1"]], et: { P1: "prêt", P2: "bloqué" }, msg: "P2 demande lui aussi l’imprimante en premier : elle est prise, P2 est bloqué… mais il <b>ne détient rien</b>." },
      { tient: [["R1", "P1"], ["R2", "P1"]], att: [["P2", "R1"]], et: { P1: "élu", P2: "bloqué" }, msg: "P1 demande le scanner : libre, il l’obtient. Il a tout ce qu’il lui faut et travaille." },
      { tient: [], att: [], et: { P1: "terminé", P2: "prêt" }, msg: "P1 termine et <b>libère</b> les deux ressources. P2, réveillé, repasse à l’état prêt." },
      { tient: [["R1", "P2"], ["R2", "P2"]], att: [], et: { P1: "terminé", P2: "élu" }, msg: "P2 obtient l’imprimante puis le scanner. Pas de cycle possible : celui qui a l’imprimante n’attend jamais un processus qui attendrait l’imprimante." }
    ]
  };
  function fleche(a, b, cl, saut) {
    var A = POS[a], B = POS[b], dx = B[0] - A[0], dy = B[1] - A[1], L = Math.sqrt(dx * dx + dy * dy), ra = a[0] === "P" ? 32 : 46, rb = b[0] === "P" ? 36 : 50;
    var x1 = A[0] + dx / L * ra, y1 = A[1] + dy / L * ra, x2 = B[0] - dx / L * rb, y2 = B[1] - dy / L * rb;
    var ux = dx / L, uy = dy / L;
    return '<path class="fil ' + cl + (saut ? "" : cl === "tient" ? " trace" : " neuf") + '" style="--l:' + Math.round(L) + '" d="M' + x1.toFixed(1) + " " + y1.toFixed(1) + " L" + x2.toFixed(1) + " " + y2.toFixed(1) + '"/><path class="tete-f ' + (cl === "tient" ? "ok" : "ko") + '" d="M' + (x2 + ux * 4).toFixed(1) + " " + (y2 + uy * 4).toFixed(1) + " L" + (x2 - ux * 9 - uy * 6).toFixed(1) + " " + (y2 - uy * 9 + ux * 6).toFixed(1) + " L" + (x2 - ux * 9 + uy * 6).toFixed(1) + " " + (y2 - uy * 9 - ux * 6).toFixed(1) + 'z"/>';
  }
  function dessine(scene, e, i, E, saut) {
    var s = '<svg viewBox="0 0 400 226" role="img" aria-label="Graphe d’allocation des ressources entre deux processus">';
    e.tient.forEach(function (f) { s += fleche(f[0], f[1], "tient", saut); });
    e.att.forEach(function (f) { s += fleche(f[0], f[1], "att", saut); });
    ["R1", "R2"].forEach(function (r) {
      var p = POS[r], libre = !e.tient.some(function (f) { return f[0] === r; });
      s += '<g class="bl' + (libre ? "" : " ok") + '"><rect x="' + (p[0] - 50) + '" y="' + (p[1] - 20) + '" width="100" height="40" rx="5"/><text x="' + p[0] + '" y="' + (p[1] - 2) + '" text-anchor="middle" class="gd">' + NOM[r] + '</text><text class="pt" x="' + p[0] + '" y="' + (p[1] + 13) + '" text-anchor="middle">' + (libre ? "libre" : "détenue") + "</text></g>";
    });
    ["P1", "P2"].forEach(function (k) {
      var p = POS[k], et = e.et[k], cl = et === "bloqué" ? " ko" : et === "élu" ? " on" : et === "terminé" ? " off" : "";
      s += '<g class="bl' + cl + '"><rect x="' + (p[0] - 34) + '" y="' + (p[1] - 30) + '" width="68" height="60" rx="30"/><text class="gd" x="' + p[0] + '" y="' + (p[1] - 2) + '" text-anchor="middle">' + k + '</text><text class="pt" x="' + p[0] + '" y="' + (p[1] + 15) + '" text-anchor="middle">' + et + "</text></g>";
    });
    if (e.cycle) s += '<text x="200" y="118" text-anchor="middle" class="gd" style="fill:var(--rouge)">cycle d’attente</text>';
    scene.innerHTML = s + "</svg>";
  }
  O.lecteur(z, { titre: "l’interblocage, pas à pas", sous: "graphe d’allocation", choix: [{ k: "blocage", t: "chacun sa première ressource" }, { k: "ordre", t: "même ordre pour tous" }],
    etapes: function (k) { return SC[k]; }, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 2400 });
};

CH.push({
  id: "proc", court: "processus", fichier: "processus.py",
  titre: "Processus et ordonnancement",
  rubrique: "Rubrique « Architectures matérielles, systèmes d’exploitation et réseaux » : gestion des processus et des ressources par un système d’exploitation",
  accroche: "Ce qu’est un processus, comment le système le crée, le fait passer d’un état à l’autre et partage le processeur entre tous (FIFO, tourniquet, priorités) ; les commandes ps, top, kill ; le risque d’interblocage.",
  essentiel: [
    "Un <b>processus</b> est un programme <b>en cours d’exécution</b>, avec sa mémoire, ses fichiers ouverts et son identifiant (<b>PID</b>) ; il est créé par un autre processus, son parent (<b>PPID</b>).",
    "Un processus passe par les états <b>prêt</b> (attend le processeur), <b>élu</b> (s’exécute), <b>bloqué</b> (attend une ressource ou une entrée-sortie), puis <b>terminé</b>.",
    "L’<b>ordonnanceur</b> du système choisit à chaque instant quel processus prêt est élu : <b>FIFO</b> (premier arrivé, premier servi), <b>tourniquet</b> (quantum de temps, retour en fin de file), <b>priorités</b>.",
    "On observe les processus avec <code>ps</code> (liste) et <code>top</code> (en direct), on en arrête un avec <code>kill PID</code>.",
    "Un <b>interblocage</b> se produit quand des processus s’attendent en cycle, chacun gardant une ressource dont l’autre a besoin : aucun ne peut plus avancer."
  ],
  attendus: [
    "Décrire la création d’un processus, l’ordonnancement de plusieurs processus par le système.",
    "Mettre en évidence le risque de l’interblocage (<i>deadlock</i>).",
    "Le programme précise : « à l’aide d’outils standard, il s’agit d’observer les processus actifs ou en attente sur une machine » ; « une présentation débranchée de l’interblocage peut être proposée »."
  ],
  intro: `<div class="boite ex"><div class="lab"># à l’écrit</div><p>Questions fréquentes : compléter un <b>diagramme de Gantt</b> pour un algorithme donné, calculer des temps d’attente, lire une sortie de <code>ps</code> (qui est le parent de qui ? quelle commande pour arrêter tel processus ?), repérer un <b>interblocage</b> dans un scénario et proposer une parade. Parfois, compléter le code Python d’un ordonnanceur.</p></div>`,
  idees: [
    { id: "i1", t: "Le système d’exploitation et la notion de processus", h: `
<p>Le <b>système d’exploitation</b> (Linux, Windows, macOS, Android…) est le logiciel qui gère la machine pour les autres programmes. Le programme de NSI lui donne pour fonctions de charger les programmes depuis la mémoire de masse et de lancer leur exécution en leur <b>créant des processus</b>, de gérer les ressources, de traiter les interruptions et les entrées-sorties, et d’assurer la sécurité du système.</p>
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>processus</b> est une instance d’un programme <b>en cours d’exécution</b>. Le <b>programme</b> est un fichier inerte sur le disque ; le <b>processus</b> est ce fichier chargé en mémoire et exécuté, avec : son code, ses données et sa pile, la valeur de ses registres (dont le compteur ordinal), ses fichiers ouverts, son état et son identifiant, le <b>PID</b> (<i>process identifier</i>).</p></div>
<p><b>Exemple</b> : ouvre deux fenêtres de terminal, et lance <code>python3</code> dans chacune. Le programme <code>python3</code> est le même fichier, mais il y a <b>deux processus</b> distincts, avec deux PID différents et des variables séparées : une variable définie dans l’un n’existe pas dans l’autre.</p>
<p>Le système range les informations de chaque processus dans un <b>bloc de contrôle</b> (PCB, <i>process control block</i>) : PID, état, registres sauvegardés, mémoire allouée, fichiers ouverts, priorité.</p>` },

    { id: "i2", t: "La création d’un processus", h: `
<p>Un processus est toujours créé par un autre processus, son <b>parent</b>. Au démarrage, le noyau lance un premier processus (sous Linux, <code>init</code> ou <code>systemd</code>, de PID 1) ; tous les autres en descendent : ils forment un <b>arbre</b>. Chaque processus connaît le PID de son parent, le <b>PPID</b>.</p>
<p>Sous Unix (Linux, macOS), la création se fait en deux temps :</p>
<ol><li><b><code>fork</code></b> : le système crée une <b>copie</b> du processus appelant (même code, copie des données), avec un nouveau PID ;</li>
<li><b><code>exec</code></b> : la copie remplace son code par celui d’un autre programme.</li></ol>
<p>C’est ce que fait le terminal quand tu tapes <code>python3 jeu.py</code> : le processus du terminal (le <i>shell</i>) se duplique, et la copie exécute <code>python3</code>. Le module <code>os</code> de Python donne accès à <code>fork</code> :</p>
[[proc-fork]]
<p>Après <code>fork</code>, il y a deux processus qui exécutent la suite du même code ; seule la valeur renvoyée par <code>fork</code> les distingue (0 dans l’enfant, le PID de l’enfant dans le parent).</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Sous Windows, il n’y a pas de <code>fork</code> : la fonction <code>CreateProcess</code> crée directement un processus qui exécute un autre programme. Un processus terminé dont le parent n’a pas encore lu le résultat reste un moment dans la table des processus : c’est un <b>zombie</b> (lettre <code>Z</code> dans <code>ps</code>).</p></div>` },

    { id: "i3", t: "Les états d’un processus", h: `
<p>Sur un processeur à un cœur, un seul processus s’exécute à un instant donné ; pourtant, des dizaines de processus semblent tourner en même temps. Le système les fait <b>alterner</b> très vite (toutes les quelques millisecondes) : c’est le <b>multitâche</b>. Chaque processus est dans l’un de ces états :</p>
<div class="tab-wrap"><table><tr><th>état</th><th>signification</th><th>exemple</th></tr>
<tr><td><b>nouveau</b></td><td>en cours de création</td><td>juste après <code>fork</code></td></tr>
<tr><td><b>prêt</b></td><td>pourrait s’exécuter, attend le processeur</td><td>un calcul interrompu à la fin de son quantum</td></tr>
<tr><td><b>élu</b> (en exécution)</td><td>s’exécute sur le processeur</td><td>un seul par cœur à la fois</td></tr>
<tr><td><b>bloqué</b> (en attente)</td><td>attend un événement : une lecture sur le disque, une touche, une ressource occupée</td><td>un programme qui attend que tu tapes au clavier</td></tr>
<tr><td><b>terminé</b></td><td>a fini, ses ressources sont libérées</td><td>après <code>exit</code></td></tr></table></div>
<p>Les transitions possibles :</p>
<ul><li><b>prêt → élu</b> : l’ordonnanceur le choisit ;</li>
<li><b>élu → prêt</b> : il est interrompu (fin de son quantum, ou arrivée d’un processus plus prioritaire) ;</li>
<li><b>élu → bloqué</b> : il demande une entrée-sortie ou une ressource indisponible ;</li>
<li><b>bloqué → prêt</b> : l’événement attendu se produit (jamais directement bloqué → élu) ;</li>
<li><b>élu → terminé</b>.</li></ul>
<p>Quand le processeur passe d’un processus à un autre, le système sauvegarde les registres du premier dans son bloc de contrôle et recharge ceux du second : c’est la <b>commutation de contexte</b>. Elle a un coût, d’où un quantum qui ne peut pas être trop court.</p>` },

    { id: "i4", t: "L’ordonnancement : trois algorithmes", h: `
<p>L’<b>ordonnanceur</b> (<i>scheduler</i>) est la partie du système qui choisit quel processus prêt devient élu. On compare les algorithmes sur un <b>diagramme de Gantt</b> : une ligne par processus, le temps en abscisse, une case colorée quand le processus s’exécute.</p>
<ul><li><b>FIFO</b> (premier arrivé, premier servi) : les processus prêts forment une file ; chacun s’exécute jusqu’au bout. Simple, mais un processus court attend derrière un long.</li>
<li><b>Tourniquet</b> (<i>round robin</i>) : chacun reçoit au plus un <b>quantum</b> de temps, puis repasse en fin de file s’il n’a pas fini. C’est la base du multitâche : chaque processus reçoit vite la main.</li>
<li><b>Priorités</b> : chaque processus a une priorité ; le plus prioritaire des prêts est élu, et l’arrivée d’un processus plus prioritaire interrompt l’élu. Risque : la <b>famine</b> d’un processus peu prioritaire qui n’est jamais élu.</li></ul>
<p>On mesure : le <b>temps de séjour</b> = instant de fin − instant d’arrivée, et le <b>temps d’attente</b> = temps de séjour − durée d’exécution. Exemple avec quatre processus : P1 (arrivée 0, durée 5), P2 (1, 3), P3 (2, 1), P4 (4, 2).</p>
[[w-arch-gantt]]
<p>En Python, la file des prêts est une <b>file</b> du chapitre « Listes, piles, files » (<code>deque</code>) :</p>
[[proc-donnees]]
[[proc-fifo]]
[[proc-rr]]
<p>La même idée réduite à l’essentiel, à exécuter pas à pas (observe la file se vider et se remplir) :</p>
[[w-trace|proc-tr-rr]]
<details class="repli"><summary>Ordonnancement par priorités (préemptif) en Python</summary><div class="corps">[[proc-prio]]<p>À l’instant 1, P2 (priorité 1) interrompt P1 (priorité 2). À l’instant 4, P4 (priorité 1) passe devant P1. P3 (priorité 3) ne s’exécute qu’à la fin.</p></div></details>
[[proc-temps]]
<div class="boite attention"><div class="lab">⚠ les conventions changent d’un sujet à l’autre</div><p>Quand un processus arrive au moment même où un autre est interrompu, qui passe d’abord dans la file ? Ici, le nouveau venu. Un sujet de bac précise toujours sa règle : <b>lis-la</b> et applique-la à la lettre.</p></div>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Les systèmes réels combinent ces idées : Linux utilise depuis la version 6.6 (2023) l’ordonnanceur EEVDF, qui répartit le temps de processeur selon une « part équitable » pondérée par la priorité de chaque processus (la valeur <code>nice</code>).</p></div>` },

    { id: "i5", t: "Observer les processus : ps, top, kill", h: `
<p>Sur Linux ou macOS, dans un terminal :</p>
<div class="code"><div class="tete"><span class="f">terminal (exemple de sortie : les numéros changent d’une machine à l’autre)</span></div><pre><code><span class="l" data-n="1">$ ps -ef</span><span class="l" data-n="2">UID    PID  PPID  C STIME TTY      TIME     CMD</span><span class="l" data-n="3">root     1     0  0 08:02 ?        00:00:03 /sbin/init</span><span class="l" data-n="4">eleve 1520     1  0 08:05 ?        00:00:01 /usr/lib/systemd/systemd --user</span><span class="l" data-n="5">eleve 2311  1520  0 08:06 pts/0    00:00:00 bash</span><span class="l" data-n="6">eleve 2675  2311 98 08:09 pts/0    00:01:12 python3 calcul.py</span><span class="l" data-n="7">eleve 2702  2311  0 08:10 pts/0    00:00:00 ps -ef</span></code></pre></div>
<ul><li><b><code>ps</code></b> (<i>process status</i>) affiche la liste des processus à un instant donné. Avec <code>-e</code> : tous les processus ; <code>-f</code> : format complet, avec le <b>PPID</b>. Ici, <code>bash</code> (PID 2311) est le parent de <code>python3 calcul.py</code> et de <code>ps -ef</code> lui-même. La colonne <code>C</code> donne l’usage du processeur (98 : le calcul l’occupe presque entièrement).</li>
<li><code>ps aux</code> ajoute <code>%CPU</code>, <code>%MEM</code> et la colonne <code>STAT</code> : <code>R</code> en exécution ou prêt, <code>S</code> endormi (bloqué, en attente d’un événement), <code>T</code> arrêté, <code>Z</code> zombie.</li>
<li><b><code>top</code></b> affiche les processus <b>en direct</b>, triés par usage du processeur, rafraîchis toutes les quelques secondes (<code>q</code> pour quitter). <code>htop</code> en est une version plus lisible.</li>
<li><b><code>kill PID</code></b> envoie un signal au processus : par défaut <code>SIGTERM</code> (« termine-toi proprement ») ; <code>kill -9 PID</code> envoie <code>SIGKILL</code>, qui le tue sans qu’il puisse réagir. Ici, <code>kill 2675</code> arrête le calcul.</li>
<li><code>pstree</code> dessine l’arbre des processus.</li></ul>
<p>Sous Windows, le <b>Gestionnaire des tâches</b> joue le rôle de <code>top</code>, et la commande <code>tasklist</code> celui de <code>ps</code>.</p>` },

    { id: "i6", t: "Ressources partagées et interblocage", h: `
<p>Les processus se partagent des <b>ressources</b> : processeur, mémoire, fichiers, imprimante, connexion à une base de données. Certaines sont à <b>accès exclusif</b> : une seule utilisation à la fois (deux processus qui écrivent en même temps dans un fichier le corrompraient). Le système les protège par des <b>verrous</b> : un processus qui demande une ressource déjà prise est <b>bloqué</b> jusqu’à sa libération.</p>
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>interblocage</b> (<i>deadlock</i>) est une situation où plusieurs processus sont bloqués <b>indéfiniment</b>, chacun attendant une ressource détenue par un autre. Exemple : P1 tient l’imprimante et attend le scanner, P2 tient le scanner et attend l’imprimante.</p></div>
[[w-arch-interblocage]]
<p>On le reproduit en Python avec deux verrous (<code>threading.Lock</code>). Pour que la démonstration s’arrête, chaque attente est limitée à 0,5 s ; dans un vrai interblocage, l’attente durerait toujours :</p>
[[proc-interblocage]]
<p>Les quatre conditions (dites de Coffman, 1971) nécessaires à un interblocage : <b>exclusion mutuelle</b> (ressources non partageables), <b>détention et attente</b> (on garde ce qu’on a en demandant autre chose), <b>pas de réquisition</b> (on ne retire pas une ressource de force), <b>attente circulaire</b>. Pour <b>prévenir</b> l’interblocage, on empêche l’une d’elles, le plus souvent l’attente circulaire : tous les processus demandent les ressources dans le <b>même ordre</b>.</p>
[[proc-ordre]]
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1965 <b>·</b></span> Edsger Dijkstra propose à ses étudiants un exercice sur des ordinateurs qui se disputent des lecteurs de bandes ; Tony Hoare le reformule en « dîner des philosophes » : cinq philosophes autour d’une table, une fourchette entre deux voisins, il en faut deux pour manger. Si chacun prend sa fourchette de gauche en même temps, tous attendent celle de droite pour toujours. C’est l’exemple classique d’interblocage.</p></div>` },

    { id: "i7", t: "Détecter un interblocage : un cycle dans un graphe", h: `
<p>On représente la situation par un <b>graphe d’attente</b> : un sommet par processus, un arc de P vers Q quand P attend une ressource détenue par Q. Il y a interblocage <b>si et seulement si</b> ce graphe contient un <b>cycle</b> (dans le cas où chaque ressource existe en un seul exemplaire). C’est un problème de graphe, comme dans la rubrique « Algorithmique » : chercher un cycle.</p>
[[proc-cycle]]
<p>Dans le troisième exemple, P4 attend P1 qui attend P2 qui attend P3, mais P3 n’attend personne : quand il aura fini, tout se débloquera. Pas de cycle, pas d’interblocage.</p>
<div class="boite hp"><div class="lab"># que fait un vrai système ?</div><p>La plupart des systèmes d’exploitation grand public ne détectent pas les interblocages entre programmes : c’est aux programmeurs de les éviter (ordre des verrous). Les systèmes de gestion de bases de données, eux, les détectent et annulent l’une des transactions en cause.</p></div>` }
  ],
  pieges: [
    { t: "Confondre programme et processus", h: `<p>Un programme est un fichier ; un processus est une exécution de ce fichier. Un même programme peut donner plusieurs processus simultanés, chacun avec son PID.</p>` },
    { t: "Faire passer un processus de bloqué à élu", h: `<p>Un processus débloqué repasse d’abord à l’état <b>prêt</b> ; c’est l’ordonnanceur qui décidera de l’élire.</p>` },
    { t: "Oublier qu’un processeur multicœur élit plusieurs processus", h: `<p>Avec 4 cœurs, jusqu’à 4 processus sont élus en même temps. Les exercices d’ordonnancement supposent en général un seul cœur : vérifie l’énoncé.</p>` },
    { t: "Temps d’attente mal calculé", h: `<p>Temps de séjour = fin − <b>arrivée</b> (pas fin − début). Temps d’attente = séjour − durée d’exécution. Vérifie sur le diagramme : l’attente compte toutes les cases où le processus est arrivé mais ne s’exécute pas.</p>` },
    { t: "Croire que kill tue toujours", h: `<p><code>kill PID</code> envoie <code>SIGTERM</code> : le processus peut l’intercepter (pour sauvegarder) ; <code>kill -9</code> (<code>SIGKILL</code>) ne peut pas être ignoré. On ne peut tuer que ses propres processus, sauf en administrateur.</p>` },
    { t: "Confondre interblocage et famine", h: `<p>Interblocage : plusieurs processus s’attendent en cycle, <b>aucun</b> n’avance. Famine : un processus n’est jamais élu parce que d’autres passent toujours devant, mais le système, lui, avance.</p>` }
  ],
  retenir: `
<h2>Processus</h2>
<ul><li>Programme <b>en cours d’exécution</b> : code, données, pile, registres, fichiers ouverts, <b>PID</b>, parent (<b>PPID</b>).</li><li>Création sous Unix : <code>fork</code> (copie du parent) puis <code>exec</code> (autre programme). Arbre des processus, racine PID 1.</li></ul>
<h2>États</h2>
<p>nouveau → <b>prêt</b> ⇄ <b>élu</b> → terminé ; élu → <b>bloqué</b> (attente d’E/S ou de ressource) → prêt.</p>
<h2>Ordonnancement</h2>
<div class="tab-wrap"><table><tr><th>algorithme</th><th>principe</th><th>défaut</th></tr><tr><td>FIFO</td><td>premier arrivé, jusqu’au bout</td><td>un court attend derrière un long</td></tr><tr><td>tourniquet</td><td>quantum, puis fin de file</td><td>commutations fréquentes</td></tr><tr><td>priorités</td><td>le plus prioritaire des prêts</td><td>famine</td></tr></table></div>
<p>Séjour = fin − arrivée · attente = séjour − durée.</p>
<h2>Commandes</h2>
<p><code>ps -ef</code> (tous, avec PPID) · <code>ps aux</code> (%CPU, %MEM, STAT) · <code>top</code> (en direct) · <code>kill PID</code> (SIGTERM) · <code>kill -9 PID</code> (SIGKILL) · <code>pstree</code>.</p>
<h2>Interblocage</h2>
<ul><li>Processus bloqués en <b>cycle d’attente</b>, chacun détenant une ressource voulue par un autre.</li><li>Conditions : exclusion mutuelle, détention et attente, pas de réquisition, attente circulaire.</li><li>Prévention : même ordre de demande pour tous. Détection : cycle dans le graphe d’attente.</li></ul>`,
  predis: [
    { code: "proc-x1", niv: "facile", rep: "A (0 à 2), puis C arrivé à 1 (2 à 4). B n’arrive qu’à 5 : le processeur est libre de 4 à 5 (<code>--</code>), puis B s’exécute. <code>fifo</code> trie par instant d’arrivée." },
    { code: "proc-x2", niv: "moyen", rep: "Quantum 2 : A s’exécute 2 unités, repasse derrière B ; B 2 unités ; A finit (1 unité) ; B finit (1 unité)." },
    { code: "proc-x3", niv: "moyen", rep: "Avec un quantum de 10, plus long que toutes les durées, aucun processus n’est jamais interrompu : le tourniquet se comporte exactement comme FIFO." },
    { code: "proc-x4", niv: "facile", rep: "Premier cas : P1 attend P2 qui attend P1, cycle, donc interblocage. Second cas : la chaîne P3 → P2 → P1 s’arrête sur P1, qui n’attend rien." }
  ],
  ep: [
    { titre: "Un ordonnanceur à tourniquet en POO", enonce: `<p>On modélise un ordonnanceur à tourniquet avec deux classes. La file des processus prêts est une liste Python dont la tête est l’élément d’indice 0.</p>[[proc-ep-fourni]]`,
      questions: [
        { q: "Compléter la méthode <code>tranche</code>.", c: `<p>Si la file est vide, renvoyer <code>None</code>. Sinon : retirer la tête (<code>self.file.pop(0)</code>), calculer <code>d = min(self.quantum, p.reste)</code>, diminuer <code>p.reste</code>, remettre <code>p</code> en fin de file s’il reste du travail, renvoyer <code>(p.pid, d)</code>.</p>` },
        { q: "Compléter <code>executer</code> : un processus est terminé quand il n’est pas revenu dans la file après sa tranche.", c: `[[proc-ep-corr]]` },
        { q: "Pour 3 processus de durées 5, 3, 1 (PID 10, 11, 12) et un quantum de 2, dans quel ordre finissent-ils ? Vérifier par un test.", c: `<p>12, puis 11, puis 10 : le chronogramme est 10 10 11 11 12 10 10 11 10. Le test <code>assert o2.executer() == [12, 11, 10]</code> le confirme.</p>` },
        { q: "À l’oral : <code>self.file.pop(0)</code> est-il efficace ? Que proposer ?", c: `<p>Non : retirer l’élément d’indice 0 d’une liste Python décale tous les autres, coût proportionnel à la longueur. Une <code>collections.deque</code> retire en tête en temps constant (<code>popleft</code>), comme la file du chapitre « Listes, piles, files ».</p>[[proc-ep-cout]]` }
      ] }
  ],
  ecrit: { titre: "Ordonnancement, commandes et interblocage", points: "≈ 8 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite (on suppose un processeur à un seul cœur).",
    enonce: `<p>Quatre processus arrivent dans le système : A (instant 0, durée 3), B (instant 1, durée 4), C (instant 2, durée 2), D (instant 3, durée 1).</p>`,
    questions: [
      { q: "Rappeler les trois états principaux d’un processus et dire dans quel état est un processus qui attend la fin d’une lecture sur le disque.", pts: "1 pt", c: `<p>Prêt, élu, bloqué. Un processus qui attend une entrée-sortie est <b>bloqué</b> ; il redeviendra prêt quand la lecture sera finie.</p>` },
      { q: "Donner le chronogramme (une case par unité de temps) avec l’algorithme FIFO, puis avec un tourniquet de quantum 2 (un processus qui arrive pendant une tranche entre dans la file avant le processus interrompu).", pts: "2 pts", code: "[[proc-ecrit-q|nosortie]]", c: `<p>FIFO : <code>A A A B B B B C C D</code>. Tourniquet : <code>A A B B C C A D B B</code> (à t = 2, B est élu et il reste C, A dans la file ; à t = 4, C est élu et il reste A, D, B).</p>[[proc-ecrit-q]]` },
      { q: "Calculer le temps de séjour moyen dans chaque cas. Quel algorithme favorise les processus courts ?", pts: "1,5 pt", c: `<p>FIFO : séjours A 3, B 6, C 7, D 7 ; moyenne 23 / 4 = 5,75. Tourniquet : A 7, B 9, C 4, D 5 ; moyenne 25 / 4 = 6,25. Le tourniquet fait finir plus tôt C et D, les plus courts (C : 4 au lieu de 7 ; D : 5 au lieu de 7), au prix d’un séjour moyen un peu plus long ici.</p>` },
      { q: "Un élève lance <code>ps -ef</code> et lit, entre autres, la ligne <code>eleve 3104 2990 99 10:12 pts/1 00:04:51 python3 boucle.py</code>. Que signifient 3104 et 2990 ? Quelle commande arrête ce programme ?", pts: "1,5 pt", c: `<p>3104 est le PID du processus, 2990 le PID de son parent (PPID), sans doute le shell <code>bash</code> du terminal. <code>kill 3104</code> lui envoie <code>SIGTERM</code> ; s’il ne s’arrête pas, <code>kill -9 3104</code>. La colonne 99 indique qu’il occupe presque tout le processeur (une boucle infinie ?).</p>` },
      { q: "Deux processus doivent écrire dans deux fichiers F1 et F2 protégés par des verrous. P1 verrouille F1 puis F2 ; P2 verrouille F2 puis F1. Décrire un déroulement qui mène à un interblocage, puis proposer une correction.", pts: "2 pts", c: `<p>P1 verrouille F1 ; P2 verrouille F2 ; P1 demande F2 (détenu par P2) : bloqué ; P2 demande F1 (détenu par P1) : bloqué. Cycle P1 → P2 → P1 : interblocage. Correction : imposer le même ordre, F1 puis F2, aux deux processus ; celui qui obtient F1 n’attend jamais un processus qui détient F1.</p>` }
    ],
    methode: `<p>Pour un tourniquet, écris la <b>file des prêts</b> à chaque fin de tranche (tête à gauche) : c’est elle qui décide du suivant. Pour un interblocage, dessine le graphe « qui attend qui » et cherche un cycle.</p>` },
  qcm: [
    { q: "Qu’est-ce qu’un processus ?", c: ["Un fichier exécutable sur le disque", "Un programme en cours d’exécution, avec sa mémoire et son PID", "Un cœur du processeur", "Une ligne de code"], a: 1, e: "Le programme est un fichier ; le processus en est une exécution.", ref: "i1" },
    { q: "Que désigne le PPID d’un processus ?", c: ["Sa priorité", "Le PID de son processus parent", "Son temps d’exécution", "Son numéro de cœur"], a: 1, e: "Parent PID : chaque processus est créé par un autre.", ref: "i2" },
    { q: "Sous Unix, que fait <code>fork</code> ?", c: ["Arrête un processus", "Crée une copie du processus appelant", "Change la priorité", "Liste les processus"], a: 1, e: "Puis <code>exec</code> remplace éventuellement le code de la copie.", ref: "i2" },
    { q: "Un processus attend la fin d’une lecture sur le disque. Il est…", c: ["élu", "prêt", "bloqué", "terminé"], a: 2, e: "Il attend un événement extérieur ; il n’a pas besoin du processeur pour l’instant.", ref: "i3" },
    { q: "Quelle transition est impossible ?", c: ["prêt → élu", "élu → bloqué", "bloqué → élu", "élu → prêt"], a: 2, e: "Un processus débloqué repasse par l’état prêt.", ref: "i3" },
    { q: "Dans l’algorithme du tourniquet, un processus dont le quantum est épuisé…", c: ["est terminé", "repasse en fin de file des prêts", "devient prioritaire", "est bloqué"], a: 1, e: "S’il n’a pas fini, il repasse en fin de file.", ref: "i4" },
    { q: "Avec FIFO, A (arrivée 0, durée 4) et B (arrivée 1, durée 1) : à quel instant B finit-il ?", c: ["1", "2", "5", "4"], a: 2, e: "A s’exécute de 0 à 4, puis B de 4 à 5.", ref: "i4" },
    { q: "Temps de séjour d’un processus arrivé à 2, terminé à 9, de durée 4 ?", c: ["4", "5", "7", "9"], a: 2, e: "Séjour = fin − arrivée = 7 ; son attente vaut 7 − 4 = 3.", ref: "i4" },
    { q: "Quel risque présente l’ordonnancement par priorités ?", c: ["L’interblocage", "La famine des processus peu prioritaires", "La perte de données", "Aucun"], a: 1, e: "S’il arrive sans cesse des processus plus prioritaires, un processus peu prioritaire n’est jamais élu.", ref: "i4" },
    { q: "Quelle commande affiche les processus en direct, triés par usage du processeur ?", c: ["ps", "top", "kill", "ls"], a: 1, e: "<code>ps</code> donne une photographie à un instant ; <code>top</code> se rafraîchit.", ref: "i5" },
    { q: "Que fait <code>kill 2675</code> ?", c: ["Affiche le processus 2675", "Envoie au processus 2675 le signal de terminaison SIGTERM", "Redémarre la machine", "Crée un processus"], a: 1, e: "<code>kill -9</code> enverrait SIGKILL, impossible à ignorer.", ref: "i5" },
    { q: "Dans <code>ps -ef</code>, quelle colonne permet de reconstituer l’arbre des processus ?", c: ["TIME", "PPID", "TTY", "C"], a: 1, e: "Chaque processus pointe vers son parent par le PPID.", ref: "i5" },
    { q: "P1 détient R1 et attend R2 ; P2 détient R2 et attend R1. C’est…", c: ["une famine", "un interblocage", "une commutation de contexte", "un fonctionnement normal"], a: 1, e: "Cycle d’attente : aucun des deux n’avancera.", ref: "i6" },
    { q: "Quelle mesure empêche cet interblocage ?", c: ["Augmenter le quantum", "Faire demander R1 puis R2 par tous les processus", "Donner plus de mémoire", "Utiliser FIFO"], a: 1, e: "Un ordre commun de demande supprime l’attente circulaire.", ref: "i6" },
    { q: "Sur un graphe d’attente (P → Q si P attend Q), un interblocage correspond à…", c: ["un sommet isolé", "un cycle", "un arbre", "un chemin de longueur 1"], a: 1, e: "Recherche de cycle dans un graphe.", ref: "i7" }
  ],
  cartes: [
    { r: "Processus", v: "Programme en cours d’exécution : code, données, pile, registres, fichiers ouverts, PID." },
    { r: "PID / PPID", v: "Identifiant du processus / identifiant de son parent." },
    { r: "fork / exec", v: "fork : copie du processus appelant. exec : remplace son code par un autre programme." },
    { r: "Les états", v: "nouveau, prêt, élu, bloqué, terminé." },
    { r: "Bloqué", v: "Attend un événement (entrée-sortie, ressource) ; redevient prêt quand il se produit." },
    { r: "Ordonnanceur", v: "Partie du système qui choisit quel processus prêt est élu." },
    { r: "FIFO", v: "Premier arrivé, premier servi, chacun jusqu’au bout." },
    { r: "Tourniquet (round robin)", v: "Quantum de temps, puis retour en fin de file s’il n’a pas fini." },
    { r: "Priorités", v: "Le plus prioritaire des prêts est élu ; risque de famine." },
    { r: "Temps de séjour / d’attente", v: "Séjour = fin − arrivée ; attente = séjour − durée d’exécution." },
    { r: "Commutation de contexte", v: "Sauvegarde des registres de l’élu, chargement de ceux du suivant." },
    { r: "ps / top", v: "ps : liste à un instant (ps -ef : avec PPID). top : en direct." },
    { r: "kill", v: "kill PID : SIGTERM ; kill -9 PID : SIGKILL (non interceptable)." },
    { r: "Interblocage (deadlock)", v: "Processus bloqués en cycle, chacun détenant une ressource voulue par un autre." },
    { r: "Prévenir l’interblocage", v: "Faire demander les ressources dans le même ordre par tous (pas d’attente circulaire)." }
  ]
});
