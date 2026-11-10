/* ===================== Calculabilité, décidabilité ===================== */
C("calc-exec", String.raw`
programme = "def carre(x):\n    return x * x\n\nprint(carre(7))"
print(type(programme), len(programme))     # un programme... est une chaîne de caractères
print(programme.count("x"))                # qu'on peut analyser comme n'importe quel texte
exec(programme)                            # et qu'on peut faire exécuter`, { out: "<class 'str'> 47\n3\n49" });

C("calc-genere", String.raw`
lignes = []
for k in range(1, 4):
    lignes.append("print(" + str(k) + ", 'x 7 =', " + str(k) + " * 7)")
code = "\n".join(lignes)                   # un programme fabriqué par un programme
print(code)
print("--- exécution ---")
exec(code)`, { out: String.raw`
print(1, 'x 7 =', 1 * 7)
print(2, 'x 7 =', 2 * 7)
print(3, 'x 7 =', 3 * 7)
--- exécution ---
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21` });

C("calc-fichier", String.raw`
import subprocess, sys

source = 'nom = "Turing"\nprint("Bonjour", nom, len(nom))\n'
with open("bonjour.py", "w", encoding="utf-8") as f:     # écrire un programme dans un fichier
    f.write(source)

resultat = subprocess.run([sys.executable, "bonjour.py"], capture_output=True, text=True)
print("l'interpréteur a reçu le fichier bonjour.py et a affiché :", resultat.stdout.strip())`, { out: "l'interpréteur a reçu le fichier bonjour.py et a affiché : Bonjour Turing 6" });

C("calc-analyse", String.raw`
source = '''def syracuse(n):
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return n

def boucle():
    while True:
        pass
'''
fonctions = [l[4:l.index("(")] for l in source.splitlines() if l.startswith("def ")]
print(fonctions)
print([l.strip() for l in source.splitlines() if "while" in l])`, { out: "['syracuse', 'boucle']\n['while n != 1:', 'while True:']" });

C("calc-fonction", String.raw`
def appliquer(f, x):
    return f(x)                      # f est une donnée : une fonction reçue en paramètre

def double(n):
    return 2 * n

print(appliquer(double, 21), appliquer(len, "Turing"), appliquer(str.upper, "nsi"))`, { out: "42 6 NSI" });

C("calc-quine", String.raw`
s = 's = %r\nprint(s %% s)'
print(s % s)`, { out: String.raw`
s = 's = %r\nprint(s %% s)'
print(s % s)` });

C("calc-turing", String.raw`
def executer(machine, mot, etat="debut", trace=False):
    """Simule une machine de Turing. machine : dictionnaire
    (état, symbole lu) -> (symbole à écrire, déplacement G/D/-, nouvel état).
    Le ruban est infini : une case jamais écrite contient le blanc "_"."""
    ruban = dict(enumerate(mot))
    pos, pas = 0, 0
    while etat != "fin":
        if trace:
            vue = "".join(ruban.get(k, "_") for k in range(-1, len(mot) + 1))
            print(vue, " " * 2, etat, "tête en", pos)
        lu = ruban.get(pos, "_")
        ecrit, dep, etat = machine[(etat, lu)]
        ruban[pos] = ecrit
        pos = pos + {"G": -1, "D": 1, "-": 0}[dep]
        pas = pas + 1
    cases = range(min(ruban), max(ruban) + 1)
    return "".join(ruban.get(k, "_") for k in cases).strip("_"), pas

PLUS_UN = {                                  # ajoute 1 à un nombre écrit en binaire
    ("debut", "0"): ("0", "D", "debut"),     # aller tout à droite...
    ("debut", "1"): ("1", "D", "debut"),
    ("debut", "_"): ("_", "G", "retenue"),   # ... puis revenir sur le dernier chiffre
    ("retenue", "1"): ("0", "G", "retenue"), # 1 + 1 = 10 : on pose 0, on retient 1
    ("retenue", "0"): ("1", "-", "fin"),     # 0 + 1 = 1 : terminé
    ("retenue", "_"): ("1", "-", "fin"),     # on déborde à gauche : nouveau chiffre 1
}

for mot in ["1011", "111", "0"]:
    print(mot, "->", executer(PLUS_UN, mot))`, { out: "1011 -> ('1100', 8)\n111 -> ('1000', 8)\n0 -> ('1', 3)" });

C("calc-turing-trace", String.raw`
executer(PLUS_UN, "1011", trace=True)`, { deps: ["calc-turing"], out: String.raw`
_1011_    debut tête en 0
_1011_    debut tête en 1
_1011_    debut tête en 2
_1011_    debut tête en 3
_1011_    debut tête en 4
_1011_    retenue tête en 3
_1010_    retenue tête en 2
_1000_    retenue tête en 1` });

C("calc-syracuse", String.raw`
def s_arrete_avant(n, limite):
    """Calcule la suite de Syracuse de n pendant au plus limite étapes."""
    for etape in range(limite):
        if n == 1:
            return "s'arrête après " + str(etape) + " étapes"
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return "je ne sais pas (limite atteinte)"

print(s_arrete_avant(6, 100))
print(s_arrete_avant(27, 100))       # pourtant elle s'arrête... après 111 étapes
print(s_arrete_avant(27, 1000))`, { out: "s'arrête après 8 étapes\nje ne sais pas (limite atteinte)\ns'arrête après 111 étapes" });

C("calc-arret", String.raw`
def arret(programme, donnee):
    """SUPPOSONS que cette fonction existe : elle renvoie True si
    programme(donnee) s'arrête, False s'il tourne indéfiniment,
    et elle répond toujours, en un temps fini."""
    ...

def paradoxe(programme):
    if arret(programme, programme):  # si programme(programme) s'arrête...
        while True:                  # ... alors je boucle indéfiniment
            pass
    else:                            # s'il ne s'arrête pas...
        return "fini"                # ... alors je m'arrête

paradoxe(paradoxe)                   # s'arrête-t-il ?`, { run: false });

C("calc-candidats", String.raw`
def construire_paradoxe(arret):
    """Fabrique le programme « paradoxe » associé à un candidat arret.
    Au lieu de boucler vraiment, il annonce ce qu'il ferait."""
    def paradoxe(programme):
        if arret(programme, programme):
            return "boucle indéfiniment"
        return "s'arrête"
    return paradoxe

candidats = {
    "toujours oui": lambda p, d: True,
    "toujours non": lambda p, d: False,
    "nom court":    lambda p, d: len(p.__name__) < 10,
}
for nom, arret in candidats.items():
    paradoxe = construire_paradoxe(arret)
    prediction = "s'arrête" if arret(paradoxe, paradoxe) else "boucle indéfiniment"
    print(nom, ": arret prédit", prediction, "/ en réalité,", paradoxe(paradoxe))`, { out: String.raw`
toujours oui : arret prédit s'arrête / en réalité, boucle indéfiniment
toujours non : arret prédit boucle indéfiniment / en réalité, s'arrête
nom court : arret prédit s'arrête / en réalité, boucle indéfiniment` });

/* pièges */
C("calc-p-exec", String.raw`
programme = "print(10 / 0)"
print("le texte du programme est correct :", programme)
exec(programme)`, { out: "le texte du programme est correct : print(10 / 0)", err: "ZeroDivisionError: division by zero" });

/* prédis la sortie */
C("calc-x1", String.raw`
code = "x = 5\nx = x * 2\nprint(x)"
print(len(code.split("\n")))
exec(code)
exec(code.replace("2", "3"))`, { out: "3\n10\n15" });

C("calc-x2", String.raw`
def compose(f, g):
    def h(x):
        return f(g(x))
    return h

plus_un = lambda x: x + 1
carre = lambda x: x * x
print(compose(carre, plus_un)(3), compose(plus_un, carre)(3))`, { out: "16 10" });

C("calc-x3", String.raw`
EFFACE = {
    ("debut", "1"): ("0", "D", "debut"),
    ("debut", "0"): ("0", "D", "debut"),
    ("debut", "_"): ("_", "-", "fin"),
}
print(executer(EFFACE, "1101"))`, { deps: ["calc-turing"], out: "('0000', 5)" });

C("calc-x4", String.raw`
def f(n):
    while n != 0:
        n = n - 2
    return "fini"

print(f(10))
print(f(7) if False else "f(7) : jamais affiché ?")`, { out: "fini\nf(7) : jamais affiché ?" });

/* épreuve pratique 1 */
C("calc-ep1-fourni", String.raw`
def executer(machine, mot, max_pas=1000):
    """Simule la machine sur le mot. Renvoie (contenu du ruban, nombre de pas),
    ou None si la machine n'a pas atteint l'état "fin" en max_pas pas."""
    ruban = dict(enumerate(mot))
    etat, pos, pas = "debut", 0, 0
    while etat != "fin":
        if pas == max_pas:
            ...
        lu = ruban.get(pos, "_")
        ecrit, dep, etat = ...
        ruban[pos] = ecrit
        pos = ...
        pas = pas + 1
    cases = range(min(ruban), max(ruban) + 1)
    return "".join(ruban.get(k, "_") for k in cases).strip("_"), pas

INVERSE = {}       # à écrire : remplace chaque 0 par 1 et chaque 1 par 0`, { fichier: "turing.py", run: false, trous: [8, 10, 12, 17] });

C("calc-ep1-corr", String.raw`
def executer(machine, mot, max_pas=1000):
    ruban = dict(enumerate(mot))
    etat, pos, pas = "debut", 0, 0
    while etat != "fin":
        if pas == max_pas:
            return None
        lu = ruban.get(pos, "_")
        ecrit, dep, etat = machine[(etat, lu)]
        ruban[pos] = ecrit
        pos = pos + {"G": -1, "D": 1, "-": 0}[dep]
        pas = pas + 1
    cases = range(min(ruban), max(ruban) + 1)
    return "".join(ruban.get(k, "_") for k in cases).strip("_"), pas

INVERSE = {
    ("debut", "0"): ("1", "D", "debut"),
    ("debut", "1"): ("0", "D", "debut"),
    ("debut", "_"): ("_", "-", "fin"),
}

PAIR = {                                     # écrit V si le nombre binaire est pair, F sinon
    ("debut", "0"): ("0", "D", "debut"),
    ("debut", "1"): ("1", "D", "debut"),
    ("debut", "_"): ("_", "G", "test"),
    ("test", "0"): ("V", "-", "fin"),
    ("test", "1"): ("F", "-", "fin"),
}

FOU = {("debut", "_"): ("_", "D", "debut")}  # avance vers la droite sans jamais s'arrêter

def test():
    assert executer(INVERSE, "1100") == ("0011", 5)
    assert executer(INVERSE, "") == ("", 1)
    assert executer(PAIR, "110")[0] == "11V"
    assert executer(PAIR, "111")[0] == "11F"
    assert executer(FOU, "") is None
    assert executer(FOU, "", max_pas=10**5) is None

test()
print("tous les tests passent")`, { fichier: "turing.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("calc-ep2-fourni", String.raw`
def fonctions_definies(source):
    """Liste des noms des fonctions définies (lignes commençant par def) dans source."""
    ...

def appels(source, nom):
    """Nombre de fois où nom( apparaît dans source, en dehors de la ligne def."""
    ...

def est_recursive(source, nom):
    """True si la fonction nom s'appelle elle-même (on suppose qu'elle est la seule
    fonction du texte source)."""
    ...`, { fichier: "analyse.py", run: false });

C("calc-ep2-corr", String.raw`
def fonctions_definies(source):
    noms = []
    for ligne in source.split("\n"):
        if ligne.startswith("def "):
            noms.append(ligne[4:ligne.index("(")])
    return noms

def appels(source, nom):
    n = 0
    for ligne in source.split("\n"):
        if not ligne.strip().startswith("def "):
            n = n + ligne.count(nom + "(")
    return n

def est_recursive(source, nom):
    return appels(source, nom) > 0

FACT = "def fact(n):\n    if n == 0:\n        return 1\n    return n * fact(n - 1)\n"
FIB = "def fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\n"
CARRE = "def carre(x):\n    return x * x\n"

def test():
    assert fonctions_definies(FACT + CARRE) == ["fact", "carre"]
    assert appels(FIB, "fib") == 2
    assert est_recursive(FACT, "fact") and not est_recursive(CARRE, "carre")
    with open(__file__, encoding="utf-8") as f:     # le programme s'analyse lui-même
        moi = f.read()
    assert "test" in fonctions_definies(moi)

test()
print("tous les tests passent")`, { fichier: "analyse.py", out: "tous les tests passent" });

/* épreuve écrite */
C("calc-ecrit-corr", String.raw`
MACHINE = {
    ("debut", "a"): ("a", "D", "debut"),
    ("debut", "b"): ("a", "D", "vu_b"),
    ("debut", "_"): ("a", "-", "fin"),
    ("vu_b", "a"): ("b", "D", "debut"),
    ("vu_b", "b"): ("b", "D", "vu_b"),
    ("vu_b", "_"): ("b", "-", "fin"),
}
for mot in ["ab", "bab", "abba"]:
    print(mot, executer(MACHINE, mot))`, { deps: ["calc-turing"], out: "ab ('aab', 3)\nbab ('abab', 4)\nabba ('aabba', 5)" });

C("calc-retenir", String.raw`
# Démonstration par l'absurde : supposons que arret(p, d) existe.
def paradoxe(p):
    if arret(p, p):
        while True:
            pass
    return "fini"
# paradoxe(paradoxe) s'arrête   ⇒ arret répond True  ⇒ paradoxe boucle : contradiction
# paradoxe(paradoxe) boucle     ⇒ arret répond False ⇒ paradoxe s'arrête : contradiction
# Donc arret ne peut pas exister : le problème de l'arrêt est indécidable.`, { run: false });

/* Animation : la preuve par l'absurde de l'indécidabilité de l'arrêt, un cas après l'autre. */
WIDGETS_EXT["arret"] = function (z, opt, O) {
  var SRC = 'def paradoxe(prog):\n    if arret(prog, prog):\n        while True:\n            pass\n    else:\n        return "fini"\n\nparadoxe(paradoxe)';
  function etapes(k) {
    var s = k === "arrete", H = s ? "s’arrête" : "ne s’arrête pas (boucle)";
    var E = [];
    function snap(l, o, msg) { E.push({ l: l, hyp: o.hyp ? H : "", rep: o.rep || "", reel: o.reel || "", boucle: !!o.boucle, contra: !!o.contra, msg: msg }); }
    snap(8, {}, "On lance <code>paradoxe(paradoxe)</code> : le programme reçoit <b>son propre texte</b> comme donnée. C’est permis : un programme est une donnée.");
    snap(8, { hyp: 1 }, "Raisonnement par cas. <b>Cas " + (s ? 1 : 2) + "</b> : supposons que <code>paradoxe(paradoxe)</code> " + H + ".");
    snap(2, { hyp: 1, rep: s ? "True" : "False" }, "Ligne 2 : il interroge <code>arret(paradoxe, paradoxe)</code>. Par hypothèse, <code>arret</code> ne se trompe jamais : elle répond <b>" + (s ? "True" : "False") + "</b> (« " + (s ? "il s’arrête" : "il ne s’arrête pas") + " »).");
    if (s) snap(3, { hyp: 1, rep: "True", reel: "boucle indéfiniment", boucle: true }, "La condition est vraie : <code>paradoxe</code> entre dans <code>while True</code> et <b>tourne indéfiniment</b>.");
    else snap(6, { hyp: 1, rep: "False", reel: "s’arrête (renvoie \"fini\")" }, "La condition est fausse : on passe dans le <code>else</code>, <code>paradoxe</code> renvoie \"fini\" et <b>s’arrête</b>.");
    snap(s ? 3 : 6, { hyp: 1, rep: s ? "True" : "False", reel: s ? "boucle indéfiniment" : "s’arrête (renvoie \"fini\")", boucle: s, contra: true }, "On avait supposé qu’il " + H + ", et il fait <b>le contraire</b> : <b>contradiction</b>, ce cas est impossible. " + (s ? "Passe au cas 2." : "Les deux cas sont impossibles : l’hypothèse de départ est fausse. Aucune fonction <code>arret</code> correcte ne peut exister : le problème de l’arrêt est <b>indécidable</b>."));
    return E;
  }
  O.lecteur(z, {
    titre: "preuve par l’absurde", sous: "paradoxe(paradoxe)", vitesse: 2200,
    choix: [{ k: "arrete", t: "cas 1 : il s’arrête" }, { k: "boucle", t: "cas 2 : il boucle" }],
    etapes: etapes,
    prepare: function (sc) {
      sc.innerHTML = '<div class="trace arret-p"><div class="code zebre"><div class="tete"><span class="f">paradoxe.py</span></div><pre><code>' + O.lignes(O.hlPy(SRC)) + '</code></pre></div><div class="tr-cote"><div class="titre-pile">hypothèse</div><div class="ap-v" data-v="hyp"></div><div class="titre-pile">arret(paradoxe, paradoxe) répond</div><div class="ap-v" data-v="rep"></div><div class="titre-pile">ce que fait vraiment paradoxe(paradoxe)</div><div class="ap-v" data-v="reel"></div><div class="ap-contra" aria-hidden="true">✘ contradiction</div></div></div>';
    },
    dessine: function (sc, e, i, E, saut) {
      O.$$(".l", sc).forEach(function (l, n) { l.classList.toggle("vise", n + 1 === e.l); });
      ["hyp", "rep", "reel"].forEach(function (k) {
        var el = O.$('[data-v="' + k + '"]', sc), v = e[k], nv = v && (saut || !i || E[i - 1][k] !== v);
        el.innerHTML = v ? '<span class="' + (nv && !saut ? "neuf" : "") + '">' + O.esc(v) + (k === "reel" && e.boucle ? ' <span class="ap-tour" aria-hidden="true">↻</span>' : "") + "</span>" : '<span class="repere">…</span>';
      });
      O.$(".ap-contra", sc).classList.toggle("on", e.contra);
    }
  });
};

CH.push({
  id: "calc", court: "calculabilite", fichier: "calculabilite.py",
  titre: "Calculabilité, décidabilité",
  rubrique: "Rubrique « Langages et programmation » : notion de programme en tant que donnée, calculabilité, décidabilité",
  accroche: "Un programme est aussi une donnée ; machine de Turing ; ce qu’un ordinateur peut calculer ne dépend pas du langage ; le problème de l’arrêt est indécidable.",
  essentiel: [
    "Un <b>programme est aussi une donnée</b> : un texte que d’autres programmes lisent, analysent, transforment ou exécutent (interpréteur, compilateur, système d’exploitation, téléchargement).",
    "Une <b>machine de Turing</b> (1936) : un ruban infini, une tête de lecture, un nombre fini d’états et une table de transitions. Elle modélise tout ce qu’un algorithme peut faire.",
    "La <b>calculabilité ne dépend pas du langage</b> : Python, C, JavaScript ou une machine de Turing calculent exactement les mêmes fonctions (thèse de Church-Turing).",
    "Un problème de décision est <b>décidable</b> s’il existe un algorithme qui répond oui ou non, correctement et en temps fini, pour <b>chaque</b> entrée.",
    "Le <b>problème de l’arrêt</b> (savoir si un programme s’arrête sur une donnée) est <b>indécidable</b> : on le montre par l’absurde avec un programme qui contredit toute prédiction sur lui-même."
  ],
  attendus: [
    "Comprendre que tout programme est aussi une donnée (BO) ; le programme cite les interpréteurs, les compilateurs, le téléchargement de logiciels et les systèmes d’exploitation.",
    "Comprendre que la calculabilité ne dépend pas du langage de programmation utilisé.",
    "Montrer, <b>sans formalisme théorique</b>, que le problème de l’arrêt est indécidable.",
    "Le programme ne demande <b>pas</b> d’étudier les machines de Turing en détail : elles servent ici à comprendre ce qu’est « calculer ». Les dérouler sur un exemple est un bon exercice."
  ],
  idees: [
    { id: "i1", t: "Un programme est aussi une donnée", h: `
<p>Un fichier <code>.py</code> n’est qu’un <b>texte</b>. Ce texte est une donnée pour un autre programme, l’<b>interpréteur</b> Python, qui le lit et l’exécute. En Python même, on peut manipuler un programme comme une chaîne de caractères, l’analyser, puis le faire exécuter par <code>exec</code> :</p>
[[calc-exec]]
<p>On peut aussi écrire un programme dans un fichier et le confier à l’interpréteur, exactement comme quand tu cliques sur « Exécuter » :</p>
[[calc-fichier]]
<div class="tab-wrap"><table><tr><th>programme</th><th>sa donnée</th><th>ce qu’il en fait</th></tr>
<tr><td>interpréteur (Python)</td><td>un programme source</td><td>l’exécute instruction par instruction</td></tr>
<tr><td>compilateur (C, Java)</td><td>un programme source</td><td>le traduit en un autre programme (code machine, bytecode)</td></tr>
<tr><td>système d’exploitation</td><td>un fichier exécutable</td><td>le charge en mémoire et lance un processus</td></tr>
<tr><td>magasin d’applications, navigateur</td><td>un logiciel, un script JavaScript</td><td>le télécharge comme n’importe quel fichier, puis l’installe ou l’exécute</td></tr>
<tr><td>antivirus, correcteur, éditeur</td><td>un programme</td><td>le lit, le colore, y cherche des erreurs ou des signatures</td></tr></table></div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1945 <b>·</b></span> Dans le rapport sur l’EDVAC, John von Neumann décrit une machine où <b>le programme est rangé dans la même mémoire que les données</b> : c’est l’architecture de presque tous les ordinateurs depuis.<br><span class="commit">1952 <b>·</b></span> Grace Hopper écrit l’un des premiers compilateurs (A-0) : un programme qui fabrique des programmes.</p></div>` },

    { id: "i2", t: "Des programmes qui fabriquent et analysent des programmes", h: `
<p>Puisqu’un programme est un texte, un programme peut en <b>écrire</b> un autre :</p>
[[calc-genere]]
<p>Ou en <b>analyser</b> un autre sans l’exécuter, comme le fait un éditeur qui signale les erreurs :</p>
[[calc-analyse]]
<p>Plus simplement encore, en Python une <b>fonction</b> est une valeur comme une autre : on peut la passer en paramètre, la ranger dans une liste, la renvoyer.</p>
[[calc-fonction]]
<div class="boite hp"><div class="lab"># pour aller plus loin : un programme qui s’écrit lui-même</div><p>Un <b>quine</b> est un programme qui affiche son propre code source. Celui-ci tient en deux lignes : <code>%r</code> insère la représentation de la chaîne, guillemets compris, et <code>%%</code> donne un <code>%</code>.</p>[[calc-quine]]</div>` },

    { id: "i3", t: "La machine de Turing", h: `
<p>En 1936, pour définir précisément ce qu’est « un calcul », le mathématicien britannique Alan <b>Turing</b> imagine une machine très simple :</p>
<ul><li>un <b>ruban</b> infini découpé en cases, chacune contenant un symbole (ou un blanc, noté _) ;</li>
<li>une <b>tête</b> de lecture et d’écriture, placée sur une case ;</li>
<li>un <b>état</b> courant, pris dans une liste finie ;</li>
<li>une <b>table de transitions</b> : selon l’état et le symbole lu, la machine écrit un symbole, déplace la tête d’une case (à gauche, à droite ou pas) et change d’état. Elle s’arrête dans l’état final.</li></ul>
<p>Voici une machine qui ajoute 1 à un nombre écrit en binaire, et un simulateur de quelques lignes : la table de transitions est un dictionnaire.</p>
[[calc-turing]]
[[w-algo-turing]]
<p>Le simulateur affiche le ruban à chaque pas pour 1011 (11 en décimal) : la tête va tout à droite, puis revient en propageant la retenue. Résultat 1100 (12).</p>
[[calc-turing-trace]]
<div class="boite ex"><div class="lab"># la machine universelle</div><p>Turing montre surtout qu’on peut construire une machine <b>universelle</b> : elle lit sur son ruban la <b>description</b> (la table) d’une autre machine et sa donnée, puis la simule. C’est exactement ce que fait notre fonction <code>executer</code>, et ce que fait un ordinateur avec un programme : le programme est une donnée de la machine universelle.</p></div>` },

    { id: "i4", t: "La calculabilité ne dépend pas du langage", h: `
<p>Une fonction est <b>calculable</b> s’il existe un algorithme (une machine de Turing, un programme) qui, pour chaque entrée, s’arrête en donnant le résultat.</p>
<p>En 1936 aussi, l’Américain Alonzo <b>Church</b> propose une autre définition, avec son <b>lambda-calcul</b>, un langage fait uniquement de fonctions. Turing montre que les deux définitions donnent <b>exactement les mêmes</b> fonctions calculables. Depuis, tous les modèles raisonnables (langages de programmation, circuits, automates cellulaires…) se sont révélés équivalents.</p>
<div class="boite def"><div class="lab">"""thèse de Church-Turing"""</div><p>Tout ce qui est calculable par un algorithme est calculable par une machine de Turing. Ce n’est pas un théorème (« algorithme » n’a pas de définition mathématique indépendante) mais une thèse, jamais mise en défaut.</p></div>
<p>Conséquence pour toi : <b>ce qu’on peut calculer ne dépend pas du langage</b>. Un programme Python peut simuler une machine de Turing (nous venons de le faire) ; une machine de Turing peut simuler l’interpréteur Python. Un langage capable de cela est dit <b>Turing-complet</b> : Python, C, Java, JavaScript le sont. Les langages diffèrent par leur commodité, leur vitesse, leur sûreté, <b>pas</b> par ce qu’ils peuvent calculer. SQL sans récursion, ou HTML, ne sont pas des langages Turing-complets.</p>` },

    { id: "i5", t: "Problèmes décidables et indécidables", h: `
<div class="boite def"><div class="lab">"""définitions"""</div><p>Un <b>problème de décision</b> est une question dont la réponse est oui ou non, posée pour une infinité d’entrées possibles : « l’entier <i>n</i> est-il premier ? ». Il est <b>décidable</b> s’il existe un algorithme qui, pour <b>toute</b> entrée, s’arrête et donne la bonne réponse. Sinon, il est <b>indécidable</b>.</p></div>
<ul><li>« <i>n</i> est-il premier ? » : décidable (essayer les diviseurs jusqu’à √<i>n</i>).</li>
<li>« Ce mot est-il dans le dictionnaire ? », « ce graphe a-t-il un cycle ? » : décidables.</li>
<li>« Ce programme s’arrête-t-il sur cette donnée ? » : <b>indécidable</b> (idée suivante).</li></ul>
<p>Attention : indécidable ne veut pas dire « difficile » ni « long à calculer », mais « <b>aucun</b> algorithme ne peut répondre correctement dans tous les cas », quelle que soit la puissance de la machine. Pour un cas particulier, on peut souvent répondre ; c’est la méthode générale qui n’existe pas.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1928 <b>·</b></span> David <b>Hilbert</b> et Wilhelm Ackermann posent l’<i>Entscheidungsproblem</i> (« problème de la décision ») : existe-t-il une méthode mécanique pour décider si un énoncé logique est démontrable ?<br><span class="commit">1931 <b>·</b></span> Kurt <b>Gödel</b> publie ses théorèmes d’incomplétude.<br><span class="commit">1936 <b>·</b></span> Church, puis Turing (« On Computable Numbers, with an Application to the Entscheidungsproblem ») répondent <b>non</b>.</p></div>` },

    { id: "i6", t: "Le problème de l’arrêt est indécidable", h: `
<p>Peut-on écrire une fonction <code>arret(programme, donnee)</code> qui dit, <b>sans se tromper et toujours en temps fini</b>, si <code>programme(donnee)</code> s’arrête ? Exécuter le programme ne suffit pas : s’il ne s’est pas arrêté au bout d’une heure, s’arrêtera-t-il dans deux ?</p>
[[calc-syracuse]]
<p>Turing a prouvé qu’une telle fonction ne peut pas exister. Raisonnons <b>par l’absurde</b> : supposons qu’elle existe, et écrivons ce programme :</p>
[[calc-arret]]
<p>Que se passe-t-il pour <code>paradoxe(paradoxe)</code> ? (Un programme est une donnée : on peut le donner à lui-même.)</p>
<ul><li>Si <code>paradoxe(paradoxe)</code> <b>s’arrête</b>, alors <code>arret(paradoxe, paradoxe)</code> renvoie <code>True</code>… donc <code>paradoxe</code> entre dans la boucle infinie et <b>ne s’arrête pas</b>. Contradiction.</li>
<li>Si <code>paradoxe(paradoxe)</code> <b>ne s’arrête pas</b>, alors <code>arret</code> renvoie <code>False</code>… donc <code>paradoxe</code> renvoie « fini » et <b>s’arrête</b>. Contradiction.</li></ul>
[[w-arret]]
<p>Les deux cas sont impossibles : l’hypothèse était fausse. <b>Aucune fonction <code>arret</code> correcte ne peut exister</b>, dans aucun langage. On peut le constater sur des candidats : chacun se trompe sur le <code>paradoxe</code> construit contre lui.</p>
[[calc-candidats]]
<div class="boite retenir-b"><div class="lab"># les trois ingrédients de la preuve</div><ol><li>un programme est une donnée (on peut le passer à <code>arret</code>, et à lui-même) ;</li><li>on suppose qu’<code>arret</code> existe et répond toujours ;</li><li><code>paradoxe</code> fait <b>le contraire</b> de ce qu’<code>arret</code> prédit sur lui.</li></ol></div>` },

    { id: "i7", t: "Ce que cela change en pratique", h: `
<p>L’indécidabilité de l’arrêt a des conséquences très concrètes :</p>
<ul><li>aucun outil ne peut détecter <b>toutes</b> les boucles infinies de <b>tous</b> les programmes ;</li>
<li>aucun antivirus ne peut décider, pour <b>tout</b> programme, s’il finira par faire une action malveillante : les antivirus utilisent des signatures et des heuristiques, qui se trompent parfois ;</li>
<li>on ne peut pas écrire un correcteur automatique qui décide si n’importe quel programme respecte sa spécification.</li></ul>
<p>Les outils réels contournent la difficulté : ils répondent « oui », « non » ou « je ne sais pas », ou se limitent à des programmes particuliers, ou fixent une limite de temps. C’est aussi pour cela qu’on <b>teste</b> et qu’on écrit des <b>variants de boucle</b> (chapitre Mise au point) : on prouve la terminaison de <b>nos</b> programmes, au cas par cas.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>Le <b>théorème de Rice</b> (1953) généralise : toute propriété non triviale du <b>comportement</b> d’un programme est indécidable. Autre problème célèbre : en 1970, Iouri Matiiassevitch prouve qu’aucun algorithme ne peut décider si une équation polynomiale à coefficients entiers a des solutions entières (dixième problème de Hilbert, posé en 1900). Quant à la conjecture de Syracuse, elle n’est pas « indécidable » : c’est un problème ouvert, que personne n’a encore résolu.</p></div>` }
  ],
  pieges: [
    { t: "Confondre « indécidable » et « très long à calculer »", h: `<p>Un problème difficile (comme trouver le meilleur trajet entre 50 villes) est décidable : un algorithme répond, même s’il prend des années. Indécidable signifie qu’<b>aucun</b> algorithme ne répond juste pour <b>toutes</b> les entrées, quel que soit le temps accordé.</p>` },
    { t: "Croire qu’on ne peut jamais savoir si un programme s’arrête", h: `<p>Pour beaucoup de programmes, on le sait très bien (une boucle <code>for</code> sur une liste finie, une fonction récursive avec un variant). L’indécidabilité dit seulement qu’il n’existe pas de <b>méthode générale</b> qui marche pour tous.</p>` },
    { t: "Mal conclure la démonstration", h: `<p>La démonstration ne prouve pas que <code>paradoxe</code> boucle, ni qu’il s’arrête : elle prouve que la fonction <code>arret</code> <b>ne peut pas exister</b>. Il faut écrire les deux cas, constater une contradiction dans chacun, et conclure sur l’<b>hypothèse</b>.</p>` },
    { t: "Penser que le texte d’un programme correct s’exécute sans erreur", h: `[[calc-p-exec]]<p>Le texte est une donnée valide (une chaîne bien formée, même syntaxiquement correcte) ; son exécution peut quand même échouer. Analyser un programme et l’exécuter sont deux choses différentes.</p>` },
    { t: "Croire qu’un langage plus récent calcule plus de choses", h: `<p>Python, C et une machine de Turing calculent les mêmes fonctions. Un langage récent est plus commode, plus sûr ou plus expressif, pas plus « puissant » au sens de la calculabilité.</p>` }
  ],
  retenir: `
<h2>Un programme est une donnée</h2>
<ul><li>Interpréteur : exécute un programme source. Compilateur : le traduit. Système d’exploitation : charge un exécutable. Téléchargement : un logiciel est un fichier.</li><li>En Python : <code>exec(chaine)</code>, une fonction passée en paramètre.</li></ul>
<h2>Machine de Turing (1936)</h2>
<p>Ruban infini, tête, états en nombre fini, table (état, symbole lu) → (symbole écrit, déplacement, nouvel état). Une machine <b>universelle</b> simule toute autre machine dont on lui donne la description.</p>
<h2>Calculabilité</h2>
<ul><li>Thèse de Church-Turing : tout ce qui est calculable par un algorithme l’est par une machine de Turing.</li><li>Tous les langages Turing-complets calculent les mêmes fonctions.</li></ul>
<h2>Le problème de l’arrêt</h2>
[[calc-retenir]]
<h2>Repères</h2>
<ul><li>1928 : Hilbert et Ackermann, <i>Entscheidungsproblem</i>. 1931 : Gödel. 1936 : Church (lambda-calcul) et Turing (machine, indécidabilité).</li><li>1945 : programme enregistré dans la mémoire (von Neumann).</li></ul>`,
  predis: [
    { code: "calc-x1", niv: "facile", rep: "La chaîne contient deux \\n, donc 3 lignes. Exécutée, elle affiche 5 × 2 = 10. Après remplacement du caractère 2 par 3, le programme devient x = 5, x = x * 3 : 15. On a modifié un programme comme un texte." },
    { code: "calc-x2", niv: "moyen", rep: "<code>compose(f, g)</code> renvoie la fonction x ↦ f(g(x)). carre(plus_un(3)) = 4² = 16 ; plus_un(carre(3)) = 9 + 1 = 10. Des fonctions reçues et renvoyées comme des données." },
    { code: "calc-x3", niv: "moyen", rep: "La machine avance vers la droite en écrivant 0 sur chaque case, puis s’arrête sur le premier blanc : 4 pas pour les chiffres + 1 pas sur le blanc = 5 pas, ruban 0000." },
    { code: "calc-x4", niv: "difficile", rep: "f(10) : 10, 8, …, 0, la boucle s’arrête. Mais f(7) passerait par 1, −1, −3… sans jamais valoir 0 : boucle infinie. Ici l’appel f(7) n’est jamais évalué, car l’expression conditionnelle choisit l’autre branche (la condition vaut False). Repérer qu’un programme <b>pourrait</b> ne pas s’arrêter demande de raisonner, pas d’exécuter." }
  ],
  ep: [
    { titre: "Un simulateur de machine de Turing", enonce: `<p>On représente une machine de Turing par un dictionnaire : à chaque couple (état, symbole lu) on associe le triplet (symbole à écrire, déplacement « G », « D » ou « - », nouvel état). L’état initial est « debut », l’état final « fin », le blanc « _ ».</p>[[calc-ep1-fourni]]`,
      questions: [
        { q: "Compléter les lignes 8, 10 et 12. Pourquoi a-t-on besoin du paramètre <code>max_pas</code> ?", c: `<p>Ligne 8 : <code>return None</code>. Ligne 10 : <code>machine[(etat, lu)]</code>. Ligne 12 : <code>pos + {"G": -1, "D": 1, "-": 0}[dep]</code>. Sans limite, une machine qui ne s’arrête pas ferait tourner le simulateur indéfiniment ; et on ne peut pas savoir à l’avance si elle s’arrêtera (problème de l’arrêt). La limite permet de répondre « je ne sais pas » (<code>None</code>).</p>` },
        { q: "Écrire la machine <code>INVERSE</code> (ligne 17) qui remplace chaque 0 par 1 et chaque 1 par 0, puis s’arrête.", c: `<p>Trois transitions depuis l’état « debut » : 0 → écrire 1, D ; 1 → écrire 0, D ; _ → rien, s’arrêter.</p>` },
        { q: "Écrire une machine <code>PAIR</code> qui remplace le dernier chiffre d’un nombre binaire par V s’il est pair, F sinon. Écrire des tests, dont un pour une machine qui ne s’arrête jamais.", c: `[[calc-ep1-corr]]` },
        { q: "À l’oral : si <code>executer</code> renvoie <code>None</code>, peut-on conclure que la machine ne s’arrête pas ?", c: `<p>Non : on sait seulement qu’elle ne s’est pas arrêtée en <code>max_pas</code> pas. Elle pourrait s’arrêter plus tard (comme la suite de Syracuse de 27, qui demande 111 étapes). Aucun choix de limite ne permet de conclure dans tous les cas.</p>` }
      ] },
    { titre: "Un programme qui analyse des programmes", enonce: `<p>On veut écrire quelques outils d’analyse de code Python, qui reçoivent le texte d’un programme sous forme de chaîne.</p>[[calc-ep2-fourni]]`,
      questions: [
        { q: "Écrire <code>fonctions_definies(source)</code>.", c: `<p>Parcourir les lignes ; pour celles qui commencent par <code>def </code>, garder ce qui est entre <code>def </code> et la parenthèse ouvrante.</p>` },
        { q: "Écrire <code>appels(source, nom)</code> et <code>est_recursive(source, nom)</code>, puis des tests sur la factorielle, Fibonacci et une fonction non récursive. Faire analyser au programme son propre fichier.", c: `[[calc-ep2-corr]]` },
        { q: "Un camarade propose d’ajouter <code>boucle_infinie(source)</code> qui renverrait <code>True</code> si et seulement si le programme peut tourner indéfiniment. Est-ce possible en général ? Que peut-on faire à la place ?", c: `<p>Non : ce serait résoudre le problème de l’arrêt, indécidable. On peut seulement signaler des cas suspects (un <code>while True</code> sans <code>break</code> ni <code>return</code>), avec des faux positifs et des oublis, ou exécuter avec une limite de temps et répondre « je ne sais pas ».</p>` },
        { q: "À l’oral : en quoi cet exercice illustre-t-il qu’un programme est une donnée ?", c: `<p>Le programme analysé est une simple chaîne de caractères, lue et découpée par un autre programme, sans être exécutée. C’est ce que font les éditeurs de code, les correcteurs de style (comme Pylint) et les compilateurs.</p>` }
      ] }
  ],
  ecrit: { titre: "Machine de Turing et problème de l’arrêt", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>On considère la machine de Turing suivante, sur l’alphabet {a, b} avec le blanc « _ ». Elle démarre dans l’état « debut », la tête sur la première lettre du mot.</p>
<div class="tab-wrap"><table><tr><th>état</th><th>lu</th><th>écrit</th><th>déplacement</th><th>nouvel état</th></tr>
<tr><td>debut</td><td>a</td><td>a</td><td>D</td><td>debut</td></tr><tr><td>debut</td><td>b</td><td>a</td><td>D</td><td>vu_b</td></tr><tr><td>debut</td><td>_</td><td>a</td><td>-</td><td>fin</td></tr>
<tr><td>vu_b</td><td>a</td><td>b</td><td>D</td><td>debut</td></tr><tr><td>vu_b</td><td>b</td><td>b</td><td>D</td><td>vu_b</td></tr><tr><td>vu_b</td><td>_</td><td>b</td><td>-</td><td>fin</td></tr></table></div>`,
    questions: [
      { q: "Dérouler la machine sur le mot « ab » : donner le ruban, la position de la tête et l’état à chaque pas.", pts: "1,5 pt", c: `<p>Pas 1 : debut lit a, écrit a, va à droite. Pas 2 : debut lit b, écrit a, va à droite, état vu_b. Pas 3 : vu_b lit _, écrit b, s’arrête. Ruban final <b>aab</b>, en 3 pas.</p>` },
      { q: "Que devient « bab » ? « abba » ? Décrire en une phrase ce que fait la machine.", pts: "1,5 pt", c: `<p>« bab » → « abab » ; « abba » → « aabba ». La machine <b>insère un a au début du mot</b> en décalant tout le mot d’une case vers la droite. Son état sert de mémoire d’une lettre : dans « debut », la lettre qu’elle vient d’effacer était un a (ou elle n’a encore rien lu) ; dans « vu_b », c’était un b. À chaque case, elle écrit la lettre mémorisée et retient celle qu’elle lit.</p>[[calc-ecrit-corr]]` },
      { q: "Cette machine s’arrête-t-elle sur tout mot ? Justifier.", pts: "1 pt", c: `<p>Oui : la tête avance d’une case vers la droite à chaque pas, sauf au dernier. Le mot étant fini, elle atteint un blanc après (longueur du mot) pas, et toute transition sur un blanc mène à l’état fin : longueur + 1 pas en tout. Ici on sait prouver la terminaison, car cette machine est particulière.</p>` },
      { q: "Rappeler l’énoncé du problème de l’arrêt et démontrer qu’il est indécidable, en écrivant le programme utilisé en Python.", pts: "2 pts", c: `<p>Énoncé : il n’existe pas de programme <code>arret(p, d)</code> qui, pour tout programme <code>p</code> et toute donnée <code>d</code>, s’arrête et renvoie <code>True</code> si <code>p(d)</code> s’arrête, <code>False</code> sinon. Preuve : voir l’idée 6 (supposer qu’il existe, construire <code>paradoxe</code>, étudier les deux cas pour <code>paradoxe(paradoxe)</code>, conclure par l’absurde).</p>` }
    ],
    methode: `<p>La démonstration de l’indécidabilité de l’arrêt est un « classique à savoir refaire ». Elle tient en dix lignes : l’hypothèse (« supposons qu’il existe… »), le programme <code>paradoxe</code>, les <b>deux</b> cas, la conclusion sur l’hypothèse. Le vocabulaire est noté : « décidable », « indécidable », « par l’absurde », « un programme est une donnée ».</p>` },
  qcm: [
    { q: "Pourquoi dit-on qu’un programme est aussi une donnée ?", c: ["Parce qu’il contient des variables", "Parce que son texte peut être lu, transformé ou exécuté par un autre programme", "Parce qu’il est stocké dans un tableur", "Parce qu’il renvoie toujours une valeur"], a: 1, e: "Interpréteurs, compilateurs, systèmes d’exploitation traitent des programmes comme données.", ref: "i1" },
    { q: "Que fait un compilateur ?", c: ["Il exécute un programme ligne par ligne", "Il traduit un programme source en un autre programme (code machine, bytecode)", "Il supprime les bugs", "Il télécharge des bibliothèques"], a: 1, e: "Il prend un programme en donnée et produit un programme.", ref: "i1" },
    { q: "Que fait <code>exec(\"print(2 + 3)\")</code> ?", c: ["Affiche print(2 + 3)", "Affiche 5", "Renvoie la chaîne \"5\"", "Provoque une erreur"], a: 1, e: "exec exécute le texte reçu comme un programme Python.", ref: "i2" },
    { q: "Quels éléments composent une machine de Turing ?", c: ["Un processeur, une mémoire vive et un disque", "Un ruban infini, une tête de lecture/écriture, un ensemble fini d’états, une table de transitions", "Un clavier et un écran", "Une pile et une file"], a: 1, e: "Modèle théorique décrit par Turing en 1936.", ref: "i3" },
    { q: "Qu’est-ce qu’une machine de Turing universelle ?", c: ["Une machine qui résout tous les problèmes", "Une machine qui simule n’importe quelle autre machine dont on lui donne la description", "Une machine sans état final", "Une machine qui ne s’arrête jamais"], a: 1, e: "C’est l’idée de l’ordinateur à programme enregistré.", ref: "i3" },
    { q: "En quelle année Turing décrit-il sa machine ?", c: ["1843", "1936", "1948", "1969"], a: 1, e: "Article « On Computable Numbers, with an Application to the Entscheidungsproblem ».", ref: "i3" },
    { q: "Que signifie « la calculabilité ne dépend pas du langage » ?", c: ["Tous les langages ont la même vitesse", "Les langages Turing-complets calculent exactement les mêmes fonctions", "On peut écrire un programme dans n’importe quelle langue", "Les compilateurs sont inutiles"], a: 1, e: "Ils diffèrent par leur commodité, pas par ce qu’ils peuvent calculer.", ref: "i4" },
    { q: "Que dit la thèse de Church-Turing ?", c: ["Tout problème est décidable", "Tout ce qui est calculable par un algorithme est calculable par une machine de Turing", "Les machines de Turing sont plus rapides que les ordinateurs", "Le lambda-calcul est plus puissant que les machines de Turing"], a: 1, e: "C’est une thèse (non démontrable), jamais mise en défaut.", ref: "i4" },
    { q: "Un problème de décision est décidable si…", c: ["on connaît la réponse pour un cas", "il existe un algorithme qui répond correctement, en temps fini, pour toute entrée", "il se résout en moins d’une seconde", "il a une réponse unique"], a: 1, e: "Pour toute entrée, et toujours en temps fini.", ref: "i5" },
    { q: "Lequel de ces problèmes est indécidable ?", c: ["Savoir si un entier est premier", "Savoir si un programme quelconque s’arrête sur une donnée quelconque", "Trier une liste", "Savoir si un mot est un palindrome"], a: 1, e: "C’est le problème de l’arrêt.", ref: "i6" },
    { q: "Dans la démonstration, que fait <code>paradoxe(p)</code> quand <code>arret(p, p)</code> vaut True ?", c: ["Il s’arrête", "Il entre dans une boucle infinie", "Il appelle arret encore", "Il renvoie True"], a: 1, e: "Il fait le contraire de ce que prédit arret.", ref: "i6" },
    { q: "Que prouve exactement la démonstration par l’absurde ?", c: ["Que paradoxe boucle", "Que paradoxe s’arrête", "Qu’aucune fonction arret correcte et toujours terminante ne peut exister", "Que Python ne peut pas exécuter paradoxe"], a: 2, e: "Les deux cas mènent à une contradiction : c’est l’hypothèse qui est fausse.", ref: "i6" },
    { q: "Pourquoi un antivirus ne peut-il pas être parfait ?", c: ["Faute de puissance de calcul", "Parce que décider le comportement futur de tout programme est indécidable", "Parce que les virus sont chiffrés", "Parce qu’il est écrit en Python"], a: 1, e: "Conséquence de l’indécidabilité (théorème de Rice, hors programme).", ref: "i7" }
  ],
  cartes: [
    { r: "Un programme est une donnée", v: "Son texte peut être lu, analysé, transformé, téléchargé ou exécuté par un autre programme (interpréteur, compilateur, OS)." },
    { r: "Interpréteur / compilateur", v: "Interpréteur : exécute le programme source. Compilateur : le traduit en un autre programme (code machine, bytecode)." },
    { r: "exec en Python", v: "exec(chaine) exécute le texte d’un programme Python contenu dans une chaîne." },
    { r: "Machine de Turing", v: "Ruban infini, tête de lecture/écriture, états en nombre fini, table (état, symbole lu) → (symbole écrit, déplacement, nouvel état). Turing, 1936." },
    { r: "Machine universelle", v: "Machine qui simule toute autre machine dont la description est écrite sur son ruban : l’idée du programme enregistré." },
    { r: "Fonction calculable", v: "Il existe un algorithme (une machine de Turing) qui la calcule en s’arrêtant pour chaque entrée." },
    { r: "Thèse de Church-Turing", v: "Tout ce qui est calculable par un algorithme est calculable par une machine de Turing. Lambda-calcul (Church) et machines (Turing) : mêmes fonctions." },
    { r: "Turing-complet", v: "Langage capable de simuler une machine de Turing : Python, C, Java, JavaScript. Ils calculent tous les mêmes fonctions." },
    { r: "Problème décidable", v: "Problème oui/non pour lequel un algorithme répond correctement et en temps fini pour toute entrée." },
    { r: "Problème de l’arrêt", v: "Décider si un programme quelconque s’arrête sur une donnée quelconque. Indécidable (Turing, 1936)." },
    { r: "Preuve de l’indécidabilité de l’arrêt", v: "Supposer arret(p, d) ; paradoxe(p) boucle si arret(p, p), s’arrête sinon ; paradoxe(paradoxe) contredit les deux cas." },
    { r: "Repères 1928-1936", v: "1928 Entscheidungsproblem (Hilbert, Ackermann) ; 1931 Gödel ; 1936 Church et Turing." },
    { r: "Indécidable ≠ difficile", v: "Indécidable : aucun algorithme ne répond juste pour toutes les entrées, quel que soit le temps donné." }
  ]
});
