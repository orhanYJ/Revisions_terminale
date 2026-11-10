/* ===================== Chapitre 5 — Dictionnaires ===================== */
C("c5-console", String.raw`
>>> stock = {"pomme": 12, "kiwi": 30}
>>> stock["pomme"]              # lire la valeur associée à une clé
12
>>> stock["melon"] = 4          # ajouter une paire
>>> stock["kiwi"] = 28          # modifier une valeur (la clé existe déjà)
>>> stock
{'pomme': 12, 'kiwi': 28, 'melon': 4}
>>> "kiwi" in stock             # tester la présence d'une CLÉ
True
>>> 28 in stock                 # in ne cherche pas parmi les valeurs
False
>>> del stock["pomme"]          # supprimer une paire
>>> len(stock)
2`, { console: true });

C("c5-parcours", String.raw`
capitales = {"France": "Paris", "Italie": "Rome", "Japon": "Tokyo"}

for pays in capitales:                 # parcours des clés
    print(pays, end=" ")
print()
print(list(capitales.values()))        # les valeurs
for pays, ville in capitales.items():  # les couples (clé, valeur)
    if len(ville) == 5:
        print(ville, "est la capitale de", pays)`, { out: "France Italie Japon\n['Paris', 'Rome', 'Tokyo']\nParis est la capitale de France\nTokyo est la capitale de Japon" });

C("c5-get", String.raw`
ages = {"Ada": 36, "Alan": 41}
print(ages.get("Grace"))          # None : pas d'erreur
print(ages.get("Grace", 0))       # valeur par défaut choisie
print(ages["Grace"])              # accès direct à une clé absente`, { out: "None\n0", err: "KeyError: 'Grace'" });

C("c5-comprehension", String.raw`
carres = {n: n * n for n in range(1, 6)}
print(carres)
longueurs = {mot: len(mot) for mot in ["pile", "file", "arbre"]}
print(longueurs)`, { out: "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n{'pile': 4, 'file': 4, 'arbre': 5}" });

C("c5-occurrences", String.raw`
def occurrences(texte):
    """Renvoie un dictionnaire {caractère: nombre d'apparitions}."""
    compte = {}
    for c in texte:
        if c in compte:
            compte[c] = compte[c] + 1
        else:
            compte[c] = 1              # première rencontre
    return compte

def plus_frequent(compte):
    """Clé de plus grande valeur (la première rencontrée en cas d'égalité)."""
    meilleur = None
    for c in compte:
        if meilleur is None or compte[c] > compte[meilleur]:
            meilleur = c
    return meilleur

occ = occurrences("abracadabra")
print(occ)
print(plus_frequent(occ), occ[plus_frequent(occ)])`, { out: "{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}\na 5" });

C("c5-tr-occ", String.raw`
compte = {}
for c in "abba":
    if c in compte:
        compte[c] = compte[c] + 1
    else:
        compte[c] = 1
print(compte)`, { fichier: "comptage.py", trace: true, out: "{'a': 2, 'b': 2}" });

C("c5-cout", String.raw`
def recherche_liste(couples, cle):
    """couples : liste de (clé, valeur). Renvoie (valeur, nombre de comparaisons)."""
    n = 0
    for k, v in couples:
        n = n + 1
        if k == cle:
            return v, n
    return None, n

n = 1_000_000
couples = [("client" + str(i), i) for i in range(n)]
annuaire = dict(couples)                          # même contenu, en dictionnaire

print(recherche_liste(couples, "client999999"))   # le dernier : n comparaisons
print(annuaire["client999999"])                   # accès direct par la clé`, { out: "(999999, 1000000)\n999999" });

C("c5-hachage", String.raw`
def code(cle, taille):
    """Fonction de hachage SIMPLIFIÉE (pour comprendre) : somme des codes des
    caractères, modulo la taille de la table. Python en utilise une bien meilleure."""
    return sum(ord(c) for c in cle) % taille

class TableHachage:
    def __init__(self, taille=8):
        self.cases = [[] for _ in range(taille)]     # une liste de couples par case

    def ajouter(self, cle, valeur):
        case = self.cases[code(cle, len(self.cases))]
        for i in range(len(case)):
            if case[i][0] == cle:
                case[i] = (cle, valeur)              # clé déjà présente : on remplace
                return
        case.append((cle, valeur))                   # sinon on ajoute (collision possible)

    def lire(self, cle):
        for k, v in self.cases[code(cle, len(self.cases))]:   # une seule case à fouiller
            if k == cle:
                return v
        raise KeyError(cle)

t = TableHachage()
for fruit, qte in [("pomme", 12), ("kiwi", 30), ("melon", 4), ("citron", 18),
                   ("figue", 9), ("poire", 7), ("cerise", 25)]:
    t.ajouter(fruit, qte)
print(code("poire", 8), t.cases[7])
print(t.lire("poire"), t.lire("cerise"))`, { out: "7 [('citron', 18), ('poire', 7)]\n7 25" });

C("c5-cles", String.raw`
grille = {(0, 0): "X", (1, 2): "O"}     # un tuple est une clé valable
print(grille[(1, 2)], (2, 2) in grille)
cases = {[0, 0]: "X"}                   # une liste ne l'est pas`, { out: "O False", err: "TypeError: unhashable type: 'list'" });

C("c5-enregistrements", String.raw`
films = [
    {"titre": "Metropolis", "annee": 1927, "realisateur": "Fritz Lang"},
    {"titre": "Les Temps modernes", "annee": 1936, "realisateur": "Charlie Chaplin"},
    {"titre": "M le maudit", "annee": 1931, "realisateur": "Fritz Lang"},
]
par_realisateur = {}                      # dictionnaire de listes
for f in films:
    r = f["realisateur"]
    if r not in par_realisateur:
        par_realisateur[r] = []
    par_realisateur[r].append(f["titre"])
print(par_realisateur["Fritz Lang"])
print(sorted(f["annee"] for f in films))`, { out: "['Metropolis', 'M le maudit']\n[1927, 1931, 1936]" });

C("c5-ordre", String.raw`
d = {"c": 3, "a": 1, "b": 2}
print(list(d))                # l'ordre d'insertion est conservé (Python 3.7 et plus)
d["a"] = 10                   # modifier ne change pas la place de la clé
print(d)
print(d == {"a": 10, "b": 2, "c": 3})   # l'égalité ne dépend pas de l'ordre`, { out: "['c', 'a', 'b']\n{'c': 3, 'a': 10, 'b': 2}\nTrue" });

C("c5-p-modif", String.raw`
stock = {"pomme": 0, "kiwi": 30, "melon": 0}
for fruit in stock:
    if stock[fruit] == 0:
        del stock[fruit]          # on retire pendant qu'on parcourt`, { err: "RuntimeError: dictionary changed size during iteration" });

C("c5-p-modif-ok", String.raw`
stock = {"pomme": 0, "kiwi": 30, "melon": 0}
for fruit in list(stock):         # on parcourt une COPIE de la liste des clés
    if stock[fruit] == 0:
        del stock[fruit]
print(stock)`, { out: "{'kiwi': 30}" });

C("c5-p-alias", String.raw`
original = {"x": 1}
copie = original              # alias, pas une copie
copie["x"] = 99
vraie_copie = dict(original)  # nouveau dictionnaire
vraie_copie["x"] = 0
print(original, vraie_copie)`, { out: "{'x': 99} {'x': 0}" });

C("c5-p-valeur", String.raw`
notes = {"Ada": 18, "Alan": 15}
print(18 in notes, 18 in notes.values(), "Ada" in notes)`, { out: "False True True" });

/* prédis la sortie */
C("c5-x1", String.raw`
d = {"a": 1}
d["b"] = 2
d["a"] = d["a"] + 10
print(d, len(d))`, { out: "{'a': 11, 'b': 2} 2" });

C("c5-x2", String.raw`
c = {}
for x in "banane":
    c[x] = c.get(x, 0) + 1
print(c)`, { out: "{'b': 1, 'a': 2, 'n': 2, 'e': 1}" });

C("c5-x3", String.raw`
notes = {"Ada": [12, 15], "Alan": [9]}
notes["Alan"].append(14)
total = 0
for nom, liste in notes.items():
    total = total + sum(liste)
print(total, list(notes))`, { out: "50 ['Ada', 'Alan']" });

C("c5-x4", String.raw`
d = {"x": 1}
e = d
e["y"] = 2
print(d.get("y"), d.get("z", 0))
print(d["z"])`, { out: "2 0", err: "KeyError: 'z'" });

/* épreuve pratique 1 */
C("c5-ep1-fourni", String.raw`
def occurrences(mot):
    """Renvoie le dictionnaire {lettre: nombre d'apparitions dans mot}."""
    d = {}
    for lettre in mot:
        ...
    return d

def sont_anagrammes(mot1, mot2):
    """True si mot2 s'écrit avec exactement les mêmes lettres que mot1,
    chacune le même nombre de fois (ex. "chien" et "niche")."""
    return occurrences(mot1).keys() == occurrences(mot2).keys()`, { fichier: "anagrammes.py", run: false, trous: [5] });

C("c5-ep1-corr", String.raw`
def occurrences(mot):
    d = {}
    for lettre in mot:
        d[lettre] = d.get(lettre, 0) + 1
    return d

def sont_anagrammes(mot1, mot2):
    return occurrences(mot1) == occurrences(mot2)   # mêmes clés ET mêmes valeurs

def test():
    assert occurrences("") == {}
    assert occurrences("nsi") == {"n": 1, "s": 1, "i": 1}
    assert occurrences("ananas") == {"a": 3, "n": 2, "s": 1}
    assert sont_anagrammes("chien", "niche")
    assert sont_anagrammes("", "")
    assert not sont_anagrammes("aab", "abb")      # le cas qui trompait la version fournie
    assert not sont_anagrammes("pile", "piles")

test()
print("tous les tests passent")`, { fichier: "anagrammes.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c5-ep2-fourni", String.raw`
def inverser(d):
    """d associe des élèves à leur groupe, par exemple {"Ada": "A", "Alan": "B", "Grace": "A"}.
    Renvoie le dictionnaire qui associe à chaque groupe la LISTE de ses élèves
    (dans l'ordre de d) : {"A": ["Ada", "Grace"], "B": ["Alan"]}."""
    res = {}
    for eleve in d:
        res[d[eleve]] = eleve
    return res

print(inverser({"Ada": "A", "Alan": "B", "Grace": "A"}))`, { fichier: "groupes.py", out: "{'A': 'Grace', 'B': 'Alan'}" });

C("c5-ep2-corr", String.raw`
def inverser(d):
    res = {}
    for eleve, groupe in d.items():
        if groupe not in res:
            res[groupe] = []          # première fois qu'on voit ce groupe
        res[groupe].append(eleve)
    return res

def plus_grand_groupe(d):
    """Groupe qui compte le plus d'élèves (le premier rencontré en cas d'égalité)."""
    inv = inverser(d)
    meilleur = None
    for g in inv:
        if meilleur is None or len(inv[g]) > len(inv[meilleur]):
            meilleur = g
    return meilleur

def test():
    d = {"Ada": "A", "Alan": "B", "Grace": "A"}
    assert inverser(d) == {"A": ["Ada", "Grace"], "B": ["Alan"]}
    assert inverser({}) == {}
    assert inverser({"Linus": "C"}) == {"C": ["Linus"]}
    assert plus_grand_groupe(d) == "A"
    assert plus_grand_groupe({}) is None

test()
print("tous les tests passent")`, { fichier: "groupes.py", out: "tous les tests passent" });

/* épreuve écrite */
C("c5-ecrit-q1", String.raw`
resultats = {"Ada": 0, "Alan": 0, "Grace": 0}
bulletins = ["Ada", "Grace", "Ada", "blanc", "Alan", "Ada"]`, { fichier: "election.py", run: false });

C("c5-ecrit-corr", String.raw`
def depouiller(bulletins, candidats):
    """Renvoie {candidat: nombre de voix}, sans compter les bulletins invalides."""
    resultats = {c: 0 for c in candidats}
    for b in bulletins:
        if b in resultats:
            resultats[b] = resultats[b] + 1
    return resultats

def vainqueurs(resultats):
    """Liste des candidats qui ont le maximum de voix (plusieurs en cas d'égalité)."""
    maxi = max(resultats.values())
    return [c for c in resultats if resultats[c] == maxi]

bulletins = ["Ada", "Grace", "Ada", "blanc", "Alan", "Ada"]
r = depouiller(bulletins, ["Ada", "Alan", "Grace"])
print(r, vainqueurs(r))
print(vainqueurs({"Ada": 2, "Alan": 2, "Grace": 1}))`, { out: "{'Ada': 3, 'Alan': 1, 'Grace': 1} ['Ada']\n['Ada', 'Alan']" });

C("c5-retenir", String.raw`
d = {}                    # dictionnaire vide          d = {"a": 1, "b": 2}
d["k"] = v                # ajouter ou modifier         coût constant (en moyenne)
d["k"]                    # lire (KeyError si absente)  coût constant (en moyenne)
d.get("k", defaut)        # lire sans erreur
"k" in d                  # la CLÉ est-elle présente ?  coût constant (en moyenne)
del d["k"]                # supprimer
for k in d: ...           # clés     d.values()  d.items()`, { run: false });

/* ---------- animation : table de hachage ---------- */
WIDGETS_EXT["hachage"] = function (z, opt, O) {
  var PAIRES = [["pomme", 12], ["kiwi", 30], ["melon", 4], ["citron", 18], ["figue", 9], ["poire", 7], ["cerise", 25]];
  var T = 8;
  function somme(k) { var s = 0; for (var i = 0; i < k.length; i++) s += k.charCodeAt(i); return s; }
  function detail(k) { return k.split("").map(function (c) { return c + "=" + c.charCodeAt(0); }).join(" + "); }
  function vide() { var t = []; for (var i = 0; i < T; i++) t.push([]); return t; }
  function copie(t) { return t.map(function (c) { return c.slice(); }); }
  function etapes(k) {
    var E = [], t = vide();
    if (k === "inserer") {
      E.push({ t: copie(t), msg: "Une table de <b>8 cases</b>, vides. Pour ranger une paire (clé, valeur), on calcule à partir de la clé un numéro de case : c’est le <b>hachage</b>." });
      PAIRES.forEach(function (p) {
        var s = somme(p[0]), b = s % T;
        E.push({ t: copie(t), cur: p[0], calc: "h(\"" + p[0] + "\") = (" + detail(p[0]) + ") mod 8 = " + s + " mod 8 = " + b, case_: b, msg: "On hache la clé <b>" + p[0] + "</b> : somme des codes des lettres = " + s + ", reste de la division par 8 = <b>" + b + "</b>." });
        var coll = t[b].length > 0;
        t[b].push(p);
        E.push({ t: copie(t), case_: b, neuf: p[0], msg: coll ? "<b>Collision</b> : la case " + b + " contient déjà « " + t[b][0][0] + " ». On range « " + p[0] + " » à la suite, dans la même case (chaînage)." : "La case " + b + " était vide : on y range <b>" + p[0] + " → " + p[1] + "</b>. Aucune autre case n’a été regardée." });
      });
      E.push({ t: copie(t), msg: "Table remplie : 7 paires, 2 collisions (cases 3 et 7). Python utilise une fonction de hachage bien plus mélangeante et agrandit sa table quand elle se remplit, pour garder très peu de collisions." });
    } else {
      PAIRES.forEach(function (p) { t[somme(p[0]) % T].push(p); });
      var cle = k === "chercher" ? "poire" : "prune", s = somme(cle), b = s % T, n = 0;
      E.push({ t: t, cur: cle, calc: "h(\"" + cle + "\") = " + s + " mod 8 = " + b, case_: b, msg: "On cherche <b>" + cle + "</b>. On hache la clé : case <b>" + b + "</b>. On ne regardera <b>que</b> cette case." });
      if (!t[b].length) E.push({ t: t, case_: b, fouille: -1, msg: "La case " + b + " est vide : <b>" + cle + " n’est pas dans le dictionnaire</b>, après 0 comparaison. <code>\"" + cle + "\" in stock</code> vaut False." });
      t[b].forEach(function (p, j) {
        n++;
        E.push({ t: t, case_: b, fouille: j, trouve: p[0] === cle, msg: p[0] === cle ? "Comparaison n° " + n + " : « " + p[0] + " » = « " + cle + " ». <b>Trouvé : valeur " + p[1] + "</b>." : "Comparaison n° " + n + " : « " + p[0] + " » ≠ « " + cle + " », on passe au suivant de la case." });
      });
      var L = PAIRES.slice(), m = 0, trouve = false;
      E.push({ liste: L, idx: -1, msg: "Même recherche dans une <b>liste</b> de couples, sans hachage : il faut parcourir depuis le début." });
      for (var i = 0; i < L.length && !trouve; i++) { m++; trouve = L[i][0] === cle; E.push({ liste: L, idx: i, trouve: trouve, msg: "Comparaison n° " + m + " : « " + L[i][0] + " »" + (trouve ? " = « " + cle + " ». Trouvé." : " ≠ « " + cle + " ».") }); }
      E.push({ liste: L, idx: trouve ? i - 1 : L.length, trouve: trouve, fin: true, msg: "Bilan : <b>" + n + " comparaison" + (n > 1 ? "s" : "") + "</b> avec le dictionnaire, <b>" + m + "</b> avec la liste. Avec un million de paires, la liste peut demander un million de comparaisons ; le dictionnaire, une ou deux en moyenne : coût <b>constant</b>." });
    }
    return E;
  }
  function dessine(sc, e) {
    var h = "";
    if (e.calc) h += '<div class="hash-calc mono">' + O.esc(e.calc) + "</div>";
    if (e.liste) {
      h += '<div class="repere" style="text-align:left;margin-bottom:6px">couples = [ … ] (liste Python, parcourue dans l’ordre)</div><div class="hash-liste">' + e.liste.map(function (p, i) { return '<span class="puce' + (i === e.idx ? (e.trouve ? " trouve" : " vu") : i < e.idx ? " passe" : "") + '">' + p[0] + " → " + p[1] + "</span>"; }).join("") + "</div>";
    } else {
      h += '<div class="hash-table">' + e.t.map(function (c, i) {
        return '<div class="bk' + (i === e.case_ ? " vise" : "") + '"><span class="ix mono">[' + i + "]</span>" + (c.length ? c.map(function (p, j) {
          var cl = p[0] === e.neuf ? " neuf" : (i === e.case_ && j === e.fouille ? (e.trouve ? " trouve" : " vu") : "");
          return '<span class="puce' + cl + '">' + p[0] + " → " + p[1] + "</span>";
        }).join('<span class="lien-c">→</span>') : '<span class="vide mono">vide</span>') + "</div>";
      }).join("") + "</div>";
    }
    sc.innerHTML = h;
  }
  O.lecteur(z, { titre: "table de hachage d’un dictionnaire", sous: "stock = {…}", choix: [{ k: "inserer", t: "ranger 7 paires" }, { k: "chercher", t: "chercher « poire »" }, { k: "absent", t: "chercher « prune » (absente)" }], etapes: etapes, dessine: dessine, vitesse: 1600 });
};

CH.push({
  id: "ch5", n: 5, court: "dictionnaires", fichier: "ch5_dictionnaires.py",
  titre: "Dictionnaires",
  rubrique: "Rubrique « Structures de données » : dictionnaires, index et clé",
  accroche: "Associer des clés à des valeurs, compter, indexer ; pourquoi la recherche par clé est si rapide (hachage).",
  essentiel: [
    "Un <b>dictionnaire</b> associe des <b>clés</b> (uniques) à des <b>valeurs</b> : <code>d[cle]</code> donne la valeur.",
    "Lire, ajouter, modifier, tester <code>cle in d</code> : coût <b>constant en moyenne</b>, quelle que soit la taille.",
    "Chercher dans une <b>liste</b>, c’est parcourir (coût linéaire) ; un dictionnaire calcule directement où ranger la clé : c’est le <b>hachage</b>.",
    "Une clé doit être <b>hachable</b> (non modifiable) : entier, chaîne, tuple. Jamais une liste ni un dictionnaire.",
    "<code>d[k]</code> sur une clé absente lève <code>KeyError</code> ; <code>d.get(k, defaut)</code> non. On parcourt avec <code>for k in d</code>, <code>d.values()</code>, <code>d.items()</code>."
  ],
  attendus: [
    "Distinguer des structures par le jeu des méthodes qui les caractérisent (tableau, liste, pile, file, dictionnaire).",
    "Choisir une structure de données adaptée à la situation à modéliser.",
    "Distinguer la recherche d’une valeur dans une liste et dans un dictionnaire (coût linéaire ou constant).",
    "Réinvestir les dictionnaires de Première : création, accès, parcours des clés, des valeurs et des couples."
  ],
  idees: [
    { id: "i1", t: "Le dictionnaire, une structure « clé → valeur »", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>dictionnaire</b> (ou <b>tableau associatif</b>) est une structure de données qui associe à des <b>clés</b>, toutes différentes, des <b>valeurs</b>. Son interface : créer un dictionnaire vide, associer une valeur à une clé, lire la valeur d’une clé, tester la présence d’une clé, supprimer une clé.</p></div>
<p>Exemples : un répertoire (nom → numéro), l’index d’un livre (mot → pages), un stock (produit → quantité), un DNS (nom de domaine → adresse IP). Dans un tableau, on accède à un élément par sa <b>position</b> (0, 1, 2…) ; dans un dictionnaire, par sa <b>clé</b>, qui peut être un mot.</p>
[[c5-console]]
<p>Remarque : <code>in</code> teste les <b>clés</b>, pas les valeurs. Une clé apparaît une seule fois : affecter une clé qui existe déjà <b>remplace</b> sa valeur.</p>` },

    { id: "i2", t: "Parcourir : clés, valeurs, couples", h: `
<p>Trois façons de parcourir un dictionnaire : ses clés (<code>for k in d</code>, ou <code>d.keys()</code>), ses valeurs (<code>d.values()</code>), ses couples (<code>d.items()</code>, qu’on « dépaquette » en deux variables).</p>
[[c5-parcours]]
<p>Pour lire une clé qui peut être absente, <code>get</code> évite l’erreur :</p>
[[c5-get]]
<p>On peut aussi construire un dictionnaire par <b>compréhension</b>, comme une liste :</p>
[[c5-comprehension]]` },

    { id: "i3", t: "Un algorithme à connaître : compter des occurrences", h: `
<p>Compter combien de fois apparaît chaque élément d’une séquence est l’usage le plus fréquent des dictionnaires (à l’écrit comme en pratique). On parcourt une fois la séquence ; pour chaque élément, on crée la clé à la première rencontre puis on incrémente.</p>
[[c5-occurrences]]
<p>Pas à pas, sur un mot de quatre lettres : regarde le dictionnaire se remplir.</p>
[[w-trace|c5-tr-occ]]
<p>Le même schéma sert à compter des mots dans un texte, des votes, des notes, des visites par page… Un seul parcours : coût linéaire en la longueur du texte.</p>` },

    { id: "i4", t: "Chercher dans une liste ou dans un dictionnaire", h: `
<p>C’est la capacité que cite le programme. Pour trouver la valeur associée à une clé dans une <b>liste de couples</b>, il faut comparer les couples un par un : jusqu’à <i>n</i> comparaisons (coût <b>linéaire</b>). Le <b>dictionnaire</b> va directement à la bonne case : quelques comparaisons en moyenne, quel que soit <i>n</i> (coût <b>constant en moyenne</b>).</p>
[[c5-cout]]
<div class="tab-wrap"><table><tr><th>opération</th><th>liste (tableau)</th><th>dictionnaire</th></tr>
<tr><td>accès par position <code>t[i]</code></td><td>constant</td><td>sans objet (pas de position)</td></tr>
<tr><td>chercher une valeur / une clé</td><td>linéaire (<code>x in t</code> parcourt)</td><td>constant en moyenne (<code>k in d</code>)</td></tr>
<tr><td>ajouter</td><td>constant en fin (<code>append</code>)</td><td>constant en moyenne</td></tr>
<tr><td>supprimer</td><td>linéaire (décalages)</td><td>constant en moyenne</td></tr></table></div>
<p>Attention : chercher une <b>valeur</b> dans un dictionnaire (<code>v in d.values()</code>) redevient linéaire. Le dictionnaire n’accélère que la recherche <b>par clé</b>.</p>` },

    { id: "i5", t: "Comment c’est possible : le hachage", h: `
<p>Un dictionnaire est rangé dans un <b>tableau</b> de cases. Une <b>fonction de hachage</b> transforme la clé en un nombre, réduit ensuite à un numéro de case. Pour lire ou écrire une clé, on recalcule ce numéro et on va directement dans la case : pas de parcours.</p>
<p>Deux clés différentes peuvent tomber dans la même case : c’est une <b>collision</b>. On les range alors ensemble dans la case (ou dans une case voisine), et on les départage par comparaison. Si la fonction de hachage répartit bien les clés et si la table est assez grande, chaque case contient très peu de clés : d’où le coût constant <b>en moyenne</b>.</p>
[[w-hachage]]
<div class="boite hp"><div class="lab"># pour aller plus loin : une table de hachage en Python</div><p>Version simplifiée, avec la fonction de hachage du schéma (somme des codes des lettres, modulo 8). Python utilise la fonction <code>hash</code>, bien meilleure (et, pour les chaînes, différente à chaque lancement de Python, pour des raisons de sécurité), une autre gestion des collisions (adressage ouvert) et agrandit sa table quand elle se remplit. Le principe reste le même.</p>[[c5-hachage]]</div>` },

    { id: "i6", t: "Quelles clés ? Des valeurs hachables", h: `
<p>Le numéro de case dépend de la clé : si la clé pouvait changer après avoir été rangée, on ne la retrouverait plus. Python exige donc des clés <b>hachables</b>, en pratique non modifiables : <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, <code>tuple</code> (de valeurs hachables). Les listes, dictionnaires et ensembles ne peuvent pas être des clés. Les <b>valeurs</b>, elles, peuvent être n’importe quoi.</p>
[[c5-cles]]
<p>Pour repérer une case d’une grille de jeu, on utilise donc le tuple <code>(ligne, colonne)</code> comme clé.</p>` },

    { id: "i7", t: "Des dictionnaires pour structurer des données", h: `
<p>Un dictionnaire peut représenter un <b>enregistrement</b> (une fiche : champ → valeur), et une liste d’enregistrements forme une <b>table</b>, comme les fichiers CSV de Première. Un dictionnaire de listes permet de <b>regrouper</b> :</p>
[[c5-enregistrements]]
<p>Ces structures annoncent deux chapitres : les <b>bases de données</b> (chapitre 6), qui organisent des tables beaucoup plus grosses, et les <b>graphes</b> (chapitre 8), souvent représentés par un dictionnaire « sommet → liste de ses voisins ».</p>
<div class="boite hp"><div class="lab"># pour aller plus loin : JSON</div><p>Le format JSON, utilisé par la plupart des API web, s’écrit presque comme un dictionnaire Python. Le module <code>json</code> passe de l’un à l’autre (<code>json.loads</code>, <code>json.dumps</code>).</p></div>` },

    { id: "i8", t: "Ordre, égalité, modification pendant un parcours", h: `
<p>Depuis Python 3.7, un dictionnaire <b>conserve l’ordre d’insertion</b> de ses clés (c’est garanti par le langage). Mais un dictionnaire n’a pas de positions : <code>d[0]</code> cherche la <b>clé</b> 0. Deux dictionnaires sont égaux s’ils ont les mêmes paires, dans n’importe quel ordre.</p>
[[c5-ordre]]
<p>On ne doit pas ajouter ni supprimer de clés pendant qu’on parcourt le dictionnaire (voir les pièges) : on parcourt une copie de la liste des clés.</p>` },

    { id: "i9", t: "Choisir entre liste et dictionnaire", h: `
<div class="tab-wrap"><table><tr><th>besoin</th><th>structure</th></tr>
<tr><td>des éléments dans un ordre, accès par position, tri</td><td>liste (tableau)</td></tr>
<tr><td>retrouver une information à partir d’un identifiant (nom, code, mot)</td><td>dictionnaire</td></tr>
<tr><td>compter des occurrences, regrouper par catégorie</td><td>dictionnaire</td></tr>
<tr><td>mémoriser des résultats déjà calculés (mémoïsation, chapitre 2)</td><td>dictionnaire</td></tr>
<tr><td>traiter dans l’ordre d’arrivée / annuler la dernière action</td><td>file / pile</td></tr></table></div>
<div class="boite hp"><div class="lab"># pour aller plus loin : les ensembles</div><p>Le type <code>set</code> de Python est un « dictionnaire sans valeurs » : <code>x in s</code> en temps constant en moyenne, sans doublons. <code>set("banane")</code> vaut <code>{'b', 'a', 'n', 'e'}</code> (dans un ordre quelconque).</p></div>` }
  ],
  pieges: [
    { t: "Lire une clé absente avec d[cle]", h: `<p><code>KeyError</code>. Tester d’abord <code>if cle in d</code>, ou utiliser <code>d.get(cle, defaut)</code>.</p>` },
    { t: "Ajouter ou supprimer des clés pendant le parcours", h: `[[c5-p-modif]]<p>Parcourir une copie : <code>for k in list(d):</code>.</p>[[c5-p-modif-ok]]` },
    { t: "Croire que in cherche parmi les valeurs", h: `[[c5-p-valeur]]<p><code>x in d</code> teste les clés ; pour les valeurs, <code>x in d.values()</code> (et c’est alors un parcours, coût linéaire).</p>` },
    { t: "Utiliser une liste comme clé", h: `<p><code>TypeError: unhashable type: 'list'</code>. Utiliser un tuple : <code>d[(1, 2)]</code>.</p>` },
    { t: "Croire que d2 = d copie le dictionnaire", h: `[[c5-p-alias]]<p>Comme pour les listes et les objets (chapitre 1) : <code>dict(d)</code> crée une copie (superficielle).</p>` },
    { t: "Oublier de créer la clé avant d’incrémenter", h: `<p><code>compte[c] = compte[c] + 1</code> sur une clé neuve lève <code>KeyError</code>. Écrire <code>compte[c] = compte.get(c, 0) + 1</code>, ou tester <code>if c in compte</code>.</p>` }
  ],
  retenir: `
<h2>L’essentiel du dictionnaire</h2>
[[c5-retenir]]
<h2>Coûts</h2>
<div class="tab-wrap"><table><tr><th>opération</th><th>liste</th><th>dictionnaire</th></tr>
<tr><td>recherche (valeur dans une liste / clé dans un dictionnaire)</td><td>linéaire</td><td>constant en moyenne</td></tr>
<tr><td>ajout</td><td>constant en fin</td><td>constant en moyenne</td></tr>
<tr><td>accès par position</td><td>constant</td><td>impossible</td></tr></table></div>
<h2>Les réflexes</h2>
<ul><li>Clés uniques et hachables (int, str, tuple) ; valeurs quelconques.</li>
<li>Compter : <code>d[x] = d.get(x, 0) + 1</code>.</li>
<li>Regrouper : créer la liste vide à la première rencontre, puis <code>append</code>.</li>
<li><code>in</code> teste les clés. <code>d[k]</code> absente → KeyError.</li>
<li>Ne pas modifier les clés pendant un parcours : <code>for k in list(d)</code>.</li>
<li>Hachage : la clé donne directement la case ; collisions départagées par comparaison.</li></ul>`,
  predis: [
    { code: "c5-x1", niv: "facile", rep: "On ajoute la clé \"b\", puis on remplace la valeur de \"a\" (1 + 10). Le dictionnaire a deux clés." },
    { code: "c5-x2", niv: "moyen", rep: "Comptage avec <code>get</code> : b une fois, a deux fois, n deux fois, e une fois. Les clés apparaissent dans l’ordre de leur première rencontre." },
    { code: "c5-x3", niv: "moyen", rep: "La valeur de \"Alan\" est une liste, modifiée sur place par <code>append</code> : [9, 14]. Total : 12 + 15 + 9 + 14 = 50. <code>list(notes)</code> donne la liste des clés." },
    { code: "c5-x4", niv: "moyen", rep: "<code>e</code> est un alias de <code>d</code> : la clé \"y\" a bien été ajoutée à <code>d</code>, d’où 2. \"z\" est absente : <code>get</code> renvoie la valeur par défaut 0, puis <code>d[\"z\"]</code> lève KeyError." }
  ],
  ep: [
    { titre: "Anagrammes", enonce: `<p>Deux mots sont des anagrammes s’ils s’écrivent avec les mêmes lettres, chacune le même nombre de fois (« chien » et « niche »).</p>[[c5-ep1-fourni]]`,
      questions: [
        { q: "Compléter la fonction <code>occurrences</code> (ligne 5).", c: `<p><code>d[lettre] = d.get(lettre, 0) + 1</code>, ou bien <code>if lettre in d: d[lettre] += 1</code> / <code>else: d[lettre] = 1</code>.</p>` },
        { q: "La fonction <code>sont_anagrammes</code> renvoie True pour « aab » et « abb ». Expliquer pourquoi et la corriger.", c: `<p>Elle ne compare que les <b>ensembles de clés</b> ({a, b} dans les deux cas) et oublie le nombre d’occurrences. Il faut comparer les dictionnaires eux-mêmes : <code>occurrences(mot1) == occurrences(mot2)</code> (mêmes clés et mêmes valeurs, l’ordre ne compte pas).</p>` },
        { q: "Écrire un jeu de tests (cas limites compris).", c: `[[c5-ep1-corr]]` },
        { q: "À l’oral : une autre méthode consiste à comparer <code>sorted(mot1)</code> et <code>sorted(mot2)</code>. Laquelle est la plus efficace pour de longs mots ?", c: `<p>Le comptage par dictionnaire fait un seul parcours de chaque mot : coût linéaire. Le tri coûte de l’ordre de <i>n</i> log₂ <i>n</i>. Pour des mots courts, la différence est négligeable ; les deux méthodes sont justes.</p>` }
      ] },
    { titre: "Groupes de TD", enonce: `<p>Un dictionnaire associe chaque élève à son groupe. On veut la liste des élèves de chaque groupe.</p>[[c5-ep2-fourni]]`,
      questions: [
        { q: "Exécuter le programme. Le résultat est-il conforme à la documentation ? Expliquer et corriger.", c: `<p>On obtient <code>{'A': 'Grace', 'B': 'Alan'}</code> : chaque nouvel élève d’un groupe <b>remplace</b> le précédent, car une clé n’a qu’une valeur. Il faut que la valeur soit une liste, créée à la première rencontre du groupe, puis complétée par <code>append</code>.</p>` },
        { q: "Écrire <code>plus_grand_groupe(d)</code>, qui renvoie le groupe le plus nombreux (None si <code>d</code> est vide).", c: `<p>On réutilise <code>inverser</code>, puis on cherche la clé dont la liste est la plus longue.</p>` },
        { q: "Écrire des tests pour les deux fonctions.", c: `[[c5-ep2-corr]]` },
        { q: "À l’oral : pourquoi parcourir <code>d.items()</code> plutôt que <code>d</code> ?", c: `<p><code>items()</code> donne directement le couple (élève, groupe) : le code est plus lisible et évite de relire <code>d[eleve]</code>. Les deux sont justes et de même coût.</p>` }
      ] }
  ],
  ecrit: { titre: "Dépouillement d’une élection", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Lors d’une élection de délégués, chaque bulletin porte le nom d’un candidat ; un bulletin blanc ou mal écrit est invalide. On utilise un dictionnaire qui associe à chaque candidat son nombre de voix.</p>[[c5-ecrit-q1]]`,
    questions: [
      { q: "Que valent <code>len(resultats)</code>, <code>\"Ada\" in resultats</code> et <code>\"blanc\" in resultats</code> ?", pts: "0,75 pt", c: `<p>3, True, False : <code>in</code> teste les clés, et \"blanc\" n’est pas un candidat.</p>` },
      { q: "Écrire une fonction <code>depouiller(bulletins, candidats)</code> qui renvoie le dictionnaire des voix de chaque candidat (0 pour un candidat sans voix), en ignorant les bulletins invalides.", pts: "2 pts", c: `<p>On initialise toutes les clés à 0, puis on ne compte que les bulletins dont le nom est une clé du dictionnaire. Avec les bulletins donnés : Ada 3, Alan 1, Grace 1.</p>` },
      { q: "Écrire une fonction <code>vainqueurs(resultats)</code> qui renvoie la liste des candidats ayant le plus de voix (plusieurs en cas d’égalité).", pts: "1,5 pt", c: `<p>Deux parcours : un pour le maximum des valeurs, un pour garder les clés qui l’atteignent.</p>[[c5-ecrit-corr]]` },
      { q: "Un élève propose d’écrire <code>resultats[b] = resultats[b] + 1</code> sans tester <code>b in resultats</code>. Que se passe-t-il avec le bulletin \"blanc\" ?", pts: "0,75 pt", c: `<p><code>KeyError: 'blanc'</code> : la clé n’existe pas. Le programme s’arrête au premier bulletin invalide.</p>` },
      { q: "On aurait pu stocker les résultats dans une liste de couples <code>[(\"Ada\", 0), …]</code>. Comparer le coût du dépouillement de <i>n</i> bulletins pour <i>c</i> candidats dans les deux cas.", pts: "1 pt", c: `<p>Avec la liste, chaque bulletin demande de chercher le candidat dans la liste : jusqu’à <i>c</i> comparaisons, soit de l’ordre de <i>n</i> × <i>c</i> au total. Avec le dictionnaire, chaque bulletin coûte un temps constant en moyenne : de l’ordre de <i>n</i>.</p>` }
    ],
    methode: `<p>Dans un exercice de dictionnaires : distingue toujours clé et valeur, crée la clé avant de l’incrémenter, et justifie le choix du dictionnaire par la recherche par clé en temps constant.</p>` },
  qcm: [
    { q: "Que contient un dictionnaire Python ?", c: ["Des valeurs rangées par position", "Des couples clé-valeur, avec des clés toutes différentes", "Des valeurs triées", "Uniquement des chaînes"], a: 1, e: "Chaque clé est unique et donne accès à sa valeur.", ref: "i1" },
    { q: "Après <code>d = {\"a\": 1}</code> puis <code>d[\"a\"] = 5</code>, que vaut <code>d</code> ?", c: ["<code>{\"a\": 1, \"a\": 5}</code>", "<code>{\"a\": 5}</code>", "<code>{\"a\": 6}</code>", "Une erreur"], a: 1, e: "Une clé déjà présente voit sa valeur remplacée.", ref: "i1" },
    { q: "Avec <code>d = {\"x\": 3}</code>, que vaut <code>3 in d</code> ?", c: ["True", "False", "3", "Une erreur"], a: 1, e: "<code>in</code> teste les clés ; 3 est une valeur.", ref: "i1" },
    { q: "Que produit <code>d[\"z\"]</code> si \"z\" n’est pas une clé ?", c: ["None", "0", "KeyError", "IndexError"], a: 2, e: "<code>d.get(\"z\")</code> renverrait None sans erreur.", ref: "i2" },
    { q: "Quelle instruction parcourt les couples (clé, valeur) ?", c: ["<code>for k in d</code>", "<code>for v in d.values()</code>", "<code>for k, v in d.items()</code>", "<code>for i in range(len(d))</code>"], a: 2, e: "<code>items()</code> donne les couples.", ref: "i2" },
    { q: "Quelle ligne compte correctement les occurrences de <code>x</code> dans <code>c</code> ?", c: ["<code>c[x] = c[x] + 1</code>", "<code>c[x] = c.get(x, 0) + 1</code>", "<code>c.append(x)</code>", "<code>c[x] += c[x]</code>"], a: 1, e: "<code>get</code> renvoie 0 si la clé n’existe pas encore.", ref: "i3" },
    { q: "Quel est le coût moyen de <code>cle in d</code> pour un dictionnaire de <i>n</i> clés ?", c: ["Constant", "Logarithmique", "Linéaire", "Quadratique"], a: 0, e: "Le hachage donne directement la case de la clé.", ref: "i4" },
    { q: "Quel est le coût de <code>x in t</code> pour une liste <code>t</code> de <i>n</i> éléments ?", c: ["Constant", "Logarithmique", "Linéaire", "Quadratique"], a: 2, e: "La liste est parcourue élément par élément.", ref: "i4" },
    { q: "Qu’est-ce qu’une collision dans une table de hachage ?", c: ["Deux clés identiques", "Deux clés différentes qui donnent le même numéro de case", "Une clé absente", "Un dictionnaire plein"], a: 1, e: "On les range dans la même case et on les départage par comparaison.", ref: "i5" },
    { q: "Laquelle de ces valeurs ne peut pas être une clé de dictionnaire ?", c: ["<code>42</code>", "<code>\"NSI\"</code>", "<code>(1, 2)</code>", "<code>[1, 2]</code>"], a: 3, e: "Une liste est modifiable, donc non hachable : TypeError.", ref: "i6" },
    { q: "Pourquoi les clés doivent-elles être non modifiables ?", c: ["Pour économiser de la mémoire", "Parce que leur case dépend de leur valeur : modifiées, on ne les retrouverait plus", "Pour pouvoir les trier", "Ce n’est pas obligatoire"], a: 1, e: "Le numéro de case est calculé à partir de la clé.", ref: "i6" },
    { q: "Que fait une boucle <code>for k in d</code> qui exécute <code>del d[k]</code> ?", c: ["Elle vide le dictionnaire", "Elle lève RuntimeError", "Elle ne fait rien", "Elle supprime une clé sur deux"], a: 1, e: "On ne modifie pas la taille d’un dictionnaire qu’on parcourt ; parcourir <code>list(d)</code>.", ref: "i8" },
    { q: "Pour retrouver le numéro de téléphone d’un contact à partir de son nom, la meilleure structure est…", c: ["une pile", "une file", "un dictionnaire nom → numéro", "une liste triée par numéro"], a: 2, e: "Recherche par clé en temps constant en moyenne.", ref: "i9" }
  ],
  cartes: [
    { r: "Dictionnaire", v: "Structure qui associe des clés uniques à des valeurs ; accès par la clé : <code>d[cle]</code>." },
    { r: "Ajouter / modifier", v: "<code>d[cle] = valeur</code> : crée la clé si elle est absente, remplace sa valeur sinon." },
    { r: "in sur un dictionnaire", v: "Teste la présence d’une <b>clé</b> (pas d’une valeur). Coût constant en moyenne." },
    { r: "get", v: "<code>d.get(cle, defaut)</code> : la valeur, ou <code>defaut</code> (None par défaut) si la clé est absente, sans KeyError." },
    { r: "Parcours", v: "<code>for k in d</code> (clés), <code>d.values()</code>, <code>for k, v in d.items()</code>." },
    { r: "Compter des occurrences", v: "<code>c[x] = c.get(x, 0) + 1</code> pour chaque x : un seul parcours." },
    { r: "Recherche : liste ou dictionnaire ?", v: "Liste : parcours, coût linéaire. Dictionnaire (par clé) : coût constant en moyenne." },
    { r: "Hachage", v: "Une fonction transforme la clé en numéro de case : on va directement à la case." },
    { r: "Collision", v: "Deux clés différentes, même case : on les range ensemble et on les départage par comparaison." },
    { r: "Clé hachable", v: "Valeur non modifiable : int, float, str, bool, tuple. Pas list, dict, set." },
    { r: "KeyError", v: "Accès <code>d[k]</code> à une clé absente." },
    { r: "Ordre des clés", v: "Ordre d’insertion conservé depuis Python 3.7 ; mais pas d’accès par position." },
    { r: "RuntimeError: dictionary changed size during iteration", v: "On a ajouté ou supprimé une clé pendant le parcours : parcourir <code>list(d)</code>." },
    { r: "Regrouper par catégorie", v: "Dictionnaire de listes : <code>if k not in d: d[k] = []</code> puis <code>d[k].append(x)</code>." }
  ]
});
