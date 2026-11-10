/* ===================== Recherche textuelle ===================== */
C("txt-naif", String.raw`
def recherche_naive(texte, motif):
    """Liste des positions où motif apparaît dans texte."""
    n, m = len(texte), len(motif)
    positions = []
    for i in range(n - m + 1):              # chaque position possible de la fenêtre
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j = j + 1                       # on compare de GAUCHE à DROITE
        if j == m:                          # tout le motif correspond
            positions.append(i)
    return positions

print(recherche_naive("LES BANANES ET LES ANANAS", "ANA"))
print(recherche_naive("LES BANANES ET LES ANANAS", "ANANAS"))
print(recherche_naive("AAAA", "AA"))`, { out: "[5, 19, 21]\n[19]\n[0, 1, 2]" });

C("txt-table", String.raw`
def table_decalage(motif):
    """Pour chaque caractère du motif SAUF le dernier : distance entre sa
    dernière occurrence et la fin du motif. Les autres caractères : len(motif)."""
    m = len(motif)
    d = {}
    for i in range(m - 1):                  # le dernier caractère est exclu
        d[motif[i]] = m - 1 - i             # une occurrence plus à droite écrase la précédente
    return d

print(table_decalage("ANANAS"))
print(table_decalage("GCAGAGAG"))`, { trace: true, titreTrace: "table_decalage", out: "{'A': 1, 'N': 2}\n{'G': 2, 'C': 6, 'A': 1}" });

C("txt-horspool", String.raw`
def horspool(texte, motif):
    n, m = len(texte), len(motif)
    d = table_decalage(motif)               # prétraitement du motif, une seule fois
    positions = []
    i = 0                                   # position de la fenêtre dans le texte
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1                       # on compare de DROITE à GAUCHE
        if j < 0:
            positions.append(i)
        i = i + d.get(texte[i + m - 1], m)  # saut lu dans la table, selon le caractère
    return positions                        # du texte sous la DERNIÈRE case du motif

print(horspool("LES BANANES ET LES ANANAS", "ANANAS"))
print(horspool("LES BANANES ET LES ANANAS", "ANA"))
print(horspool("CGTGCCTACTTACTTACTTACTTACGCGAA", "CTTACTTAC"))`, { deps: ["txt-table"], out: "[19]\n[5, 19, 21]\n[8, 12, 16]" });

C("txt-trace", String.raw`
def horspool_trace(texte, motif):
    n, m = len(texte), len(motif)
    d = table_decalage(motif)
    print(texte)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1
        c = texte[i + m - 1]
        saut = d.get(c, m)
        etat = "TROUVÉ" if j < 0 else "échec en " + str(i + j)
        print(" " * i + motif + "  " + etat + ", sous la fin : " + c + ", saut de " + str(saut))
        i = i + saut

horspool_trace("LES BANANES ET LES ANANAS", "ANANAS")`, { deps: ["txt-table"], out: String.raw`
LES BANANES ET LES ANANAS
ANANAS  échec en 5, sous la fin : A, saut de 1
 ANANAS  échec en 6, sous la fin : N, saut de 2
   ANANAS  échec en 8, sous la fin : N, saut de 2
     ANANAS  échec en 9, sous la fin : S, saut de 6
           ANANAS  échec en 16, sous la fin : E, saut de 6
                 ANANAS  échec en 22, sous la fin : N, saut de 2
                   ANANAS  TROUVÉ, sous la fin : S, saut de 6` });

C("txt-compte", String.raw`
def naive_c(texte, motif):
    n, m, c = len(texte), len(motif), 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            c = c + 1
            if texte[i + j] != motif[j]:
                break
            j = j + 1
    return c

def horspool_c(texte, motif):
    n, m, c = len(texte), len(motif), 0
    d = table_decalage(motif)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            c = c + 1
            if texte[i + j] != motif[j]:
                break
            j = j - 1
        i = i + d.get(texte[i + m - 1], m)
    return c

texte = "Le Rouge et le Noir est un roman de Stendhal paru en 1830. " * 1000
for motif in ["roman", "Stendhal paru en 1831"]:
    print(len(texte), motif, naive_c(texte, motif), horspool_c(texte, motif))`, { deps: ["txt-table"], out: "59000 roman 64996 18000\n59000 Stendhal paru en 1831 78980 4001" });

C("txt-pire", String.raw`
texte = "A" * 1000
print(naive_c(texte, "AAAB"), horspool_c(texte, "AAAB"))     # le naïf souffre
print(naive_c(texte, "BAAA"), horspool_c(texte, "BAAA"))     # Horspool souffre`, { deps: ["txt-table", "txt-compte"], out: "3988 997\n997 3988" });

C("txt-bm", String.raw`
def boyer_moore_simple(texte, motif):
    """Règle du « mauvais caractère » : on aligne le caractère du texte qui a
    provoqué l'échec avec sa dernière occurrence dans le motif."""
    n, m = len(texte), len(motif)
    derniere = {}
    for k in range(m):
        derniere[motif[k]] = k              # indice de la dernière occurrence
    positions = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1
        if j < 0:
            positions.append(i)
            i = i + 1
        else:
            i = i + max(1, j - derniere.get(texte[i + j], -1))
    return positions

print(boyer_moore_simple("LES BANANES ET LES ANANAS", "ANANAS"))
print(boyer_moore_simple("CGTGCCTACTTACTTACTTACTTACGCGAA", "CTTACTTAC"))`, { out: "[19]\n[8, 12, 16]" });

C("txt-python", String.raw`
>>> "ANANAS" in "LES BANANES ET LES ANANAS"
True
>>> "LES BANANES ET LES ANANAS".find("ANA")
5
>>> "LES BANANES ET LES ANANAS".find("KIWI")
-1
>>> "ANANAS".count("ANA")
1`, { console: true });

/* pièges */
C("txt-p-borne", String.raw`
def recherche_bug(texte, motif):
    res = []
    for i in range(len(texte) - len(motif)):      # oublie la dernière position
        if texte[i:i + len(motif)] == motif:
            res.append(i)
    return res

print(recherche_bug("BANANA", "NA"), recherche_bug("ABC", "ABC"))`, { out: "[2] []" });

C("txt-p-dernier", String.raw`
def table_fausse(motif):
    d = {}
    for i in range(len(motif)):                  # inclut le dernier caractère
        d[motif[i]] = len(motif) - 1 - i
    return d

print(table_fausse("ANANAS"))                    # 'S' -> 0 : saut nul, boucle infinie`, { out: "{'A': 1, 'N': 2, 'S': 0}" });

/* prédis la sortie */
C("txt-x1", String.raw`
d = table_decalage("ABRACADABRA")
print(sorted(d.items()))`, { deps: ["txt-table"], out: "[('A', 3), ('B', 2), ('C', 6), ('D', 4), ('R', 1)]" });

C("txt-x2", String.raw`
print(recherche_naive("ABABABA", "ABA"), "ABABABA".count("ABA"))`, { deps: ["txt-naif"], out: "[0, 2, 4] 2" });

C("txt-x3", String.raw`
texte, motif = "TTGACAGATTGACA", "GACA"
d = table_decalage(motif)
i, sauts = 0, []
while i <= len(texte) - len(motif):
    s = d.get(texte[i + len(motif) - 1], len(motif))
    sauts.append(s)
    i = i + s
print(d, sauts)`, { deps: ["txt-table"], out: "{'G': 3, 'A': 2, 'C': 1} [2, 2, 2, 4, 2]" });

C("txt-x4", String.raw`
def premiere(texte, motif):
    for i in range(len(texte) - len(motif) + 1):
        if texte[i:i + len(motif)] == motif:
            return i
    return -1

print(premiere("informatique", "ma"), premiere("informatique", "que"), premiere("NSI", "NSIS"))`, { out: "5 9 -1" });

/* épreuve pratique 1 */
C("txt-ep1-fourni", String.raw`
def est_en_position(texte, motif, i):
    """Renvoie True si motif apparaît dans texte à partir de l'indice i."""
    ...

def recherche(texte, motif):
    """Renvoie la liste des indices où motif apparaît dans texte
    (occurrences qui se chevauchent comprises)."""
    ...

print(recherche("ATGCGATGCATGCGT", "ATGC"))`, { fichier: "recherche.py", run: false, trous: [3, 8] });

C("txt-ep1-corr", String.raw`
def est_en_position(texte, motif, i):
    if i + len(motif) > len(texte):
        return False
    for j in range(len(motif)):
        if texte[i + j] != motif[j]:
            return False
    return True

def recherche(texte, motif):
    res = []
    for i in range(len(texte) - len(motif) + 1):
        if est_en_position(texte, motif, i):
            res.append(i)
    return res

def test():
    assert recherche("ATGCGATGCATGCGT", "ATGC") == [0, 5, 9]
    assert recherche("AAAA", "AA") == [0, 1, 2]                 # chevauchements
    assert recherche("ABC", "ABC") == [0]                       # motif = texte
    assert recherche("AB", "ABC") == []                         # motif trop long
    assert recherche("", "A") == []
    assert est_en_position("NSI", "SI", 1) and not est_en_position("NSI", "SI", 2)
    texte = "BLA" * 300 + "NSI" + "BLA" * 300
    assert recherche(texte, "NSI") == [900]

test()
print(recherche("ATGCGATGCATGCGT", "ATGC"))
print("tous les tests passent")`, { fichier: "recherche.py", out: "[0, 5, 9]\ntous les tests passent" });

/* épreuve pratique 2 */
C("txt-ep2-fourni", String.raw`
def table_decalage(motif):
    m = len(motif)
    d = {}
    for i in range(m):
        d[motif[i]] = m - 1 - i
    return d

def horspool(texte, motif):
    n, m = len(texte), len(motif)
    d = table_decalage(motif)
    res = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1
        if j < 0:
            res.append(i)
        i = i + d.get(texte[i + m - 1], m)
    return res

print(horspool("CACAO", "CAO"))
print(horspool("CHOCOLAT", "LAT"))`, { fichier: "horspool.py", run: false });

C("txt-ep2-corr", String.raw`
def table_decalage(motif):
    m = len(motif)
    d = {}
    for i in range(m - 1):                 # SANS le dernier caractère
        d[motif[i]] = m - 1 - i
    return d

def horspool(texte, motif):
    n, m = len(texte), len(motif)
    d = table_decalage(motif)
    res = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1
        if j < 0:
            res.append(i)
        i = i + d.get(texte[i + m - 1], m)
    return res

def naive(texte, motif):
    return [i for i in range(len(texte) - len(motif) + 1) if texte[i:i + len(motif)] == motif]

def test():
    assert table_decalage("CAO") == {"C": 2, "A": 1}
    assert horspool("CACAO", "CAO") == [2]
    assert horspool("CHOCOLAT", "LAT") == [5]
    assert horspool("AAAA", "AA") == [0, 1, 2]
    assert horspool("AB", "ABC") == []
    textes = ["ABRACADABRA", "CGTGCCTACTTACTTACTTACTTACGCGAA", "LES BANANES ET LES ANANAS"]
    motifs = ["A", "ABRA", "CTTAC", "ANA", "XYZ", "S"]
    for t in textes:
        for m in motifs:
            assert horspool(t, m) == naive(t, m), (t, m)

test()
print("tous les tests passent")`, { fichier: "horspool.py", out: "tous les tests passent" });

/* épreuve écrite */
C("txt-ecrit-corr", String.raw`
texte = "GCATCGCAGAGAGTATACAGTACG"
motif = "GCAGAGAG"
d = table_decalage(motif)
print(d)
print(horspool(texte, motif))
print(horspool_c(texte, motif), naive_c(texte, motif))`, { deps: ["txt-table", "txt-horspool", "txt-compte"], out: "{'G': 2, 'C': 6, 'A': 1}\n[5]\n21 30" });

C("txt-retenir", String.raw`
d = {}                                   # 1. PRÉTRAITEMENT du motif (une fois)
for i in range(m - 1):
    d[motif[i]] = m - 1 - i
i = 0
while i <= n - m:                        # 2. RECHERCHE
    j = m - 1
    while j >= 0 and texte[i + j] == motif[j]:
        j = j - 1                        #    de droite à gauche
    if j < 0:
        trouvé en i
    i = i + d.get(texte[i + m - 1], m)   # 3. SAUT`, { run: false });

CH.push({
  id: "texte", court: "recherche_textuelle", fichier: "recherche_textuelle.py",
  titre: "Recherche textuelle",
  rubrique: "Rubrique « Algorithmique » : recherche textuelle (algorithme de Boyer-Moore, prétraitement du motif)",
  accroche: "Trouver un motif dans un texte : algorithme naïf, Boyer-Moore-Horspool, table de décalage, et pourquoi lire le motif à l’envers fait gagner du temps.",
  essentiel: [
    "Chercher un <b>motif</b> (de longueur <i>m</i>) dans un <b>texte</b> (de longueur <i>n</i>) : on fait glisser une <b>fenêtre</b> sur le texte et on compare.",
    "L’algorithme <b>naïf</b> essaie toutes les positions et avance de 1 à chaque fois : jusqu’à <i>n</i> × <i>m</i> comparaisons.",
    "<b>Boyer-Moore</b> (dans sa version de <b>Horspool</b>) compare le motif <b>de droite à gauche</b> et, en cas d’échec, <b>saute</b> plusieurs positions d’un coup.",
    "Le saut est lu dans une <b>table de décalage</b> calculée une fois pour toutes à partir du motif : c’est le <b>prétraitement</b>. Il dépend du caractère du texte sous la dernière case du motif.",
    "Un caractère absent du motif fait sauter de <i>m</i> cases : plus le motif est long, plus la recherche est rapide (environ <i>n</i>/<i>m</i> comparaisons dans les cas favorables)."
  ],
  attendus: [
    "Étudier l’algorithme de Boyer-Moore pour la recherche d’un motif dans un texte (capacité du BO).",
    "Comprendre et mettre en avant l’intérêt du <b>prétraitement</b> du motif (commentaire du BO).",
    "Dérouler l’algorithme à la main : positions de la fenêtre, comparaisons, sauts ; construire la table de décalage.",
    "L’étude du coût est difficile et <b>ne peut pas être exigée</b> (BO) ; il faut seulement savoir comparer, sur un exemple, le nombre de comparaisons avec l’algorithme naïf."
  ],
  idees: [
    { id: "i1", t: "Le problème et son vocabulaire", h: `
<p>Chercher un mot dans une page web (Ctrl + F), un gène dans un génome, une signature de virus dans un fichier : c’est le même problème. On dispose d’un <b>texte</b> de <i>n</i> caractères et d’un <b>motif</b> de <i>m</i> caractères (en général <i>m</i> est bien plus petit que <i>n</i>), et on cherche toutes les <b>positions</b> (indices) où le motif apparaît.</p>
<div class="boite def"><div class="lab">"""définitions"""</div><ul><li><b>Occurrence</b> : position <i>i</i> telle que <code>texte[i:i+m] == motif</code>. Deux occurrences peuvent <b>se chevaucher</b> (« AA » apparaît en 0, 1 et 2 dans « AAAA »).</li><li><b>Fenêtre</b> : le morceau de texte de longueur <i>m</i> qu’on compare au motif ; on la fait glisser de gauche à droite. Il y a <i>n</i> − <i>m</i> + 1 positions possibles.</li></ul></div>
[[txt-python]]
<p>Python sait le faire (<code>in</code>, <code>find</code>, <code>count</code>), mais l’épreuve demande de comprendre <b>comment</b>. Attention : <code>count</code> ne compte pas les occurrences qui se chevauchent.</p>` },

    { id: "i2", t: "L’algorithme naïf", h: `
<p>On place la fenêtre en position 0, on compare le motif caractère par caractère <b>de gauche à droite</b> ; dès qu’un caractère diffère, on décale la fenêtre <b>d’une case</b> et on recommence.</p>
[[txt-naif]]
<p>Pour chacune des <i>n</i> − <i>m</i> + 1 positions, on fait au plus <i>m</i> comparaisons : au pire de l’ordre de <b><i>n</i> × <i>m</i></b> comparaisons, par exemple pour chercher « AAAB » dans « AAAA…A ». Sur un texte ordinaire, les échecs arrivent vite (souvent dès la première lettre) et on fait un peu plus de <i>n</i> comparaisons. Le défaut de fond : l’algorithme <b>oublie</b> ce qu’il vient de lire et n’avance que d’une case.</p>
[[w-algo-boyer-moore|naif]]` },

    { id: "i3", t: "L’idée de Boyer-Moore : lire le motif à l’envers", h: `
<p>Robert <b>Boyer</b> et J Strother <b>Moore</b> ont eu deux idées (1977) :</p>
<ol><li><b>Comparer de droite à gauche</b> : on commence par le <b>dernier</b> caractère du motif.</li>
<li><b>Utiliser le caractère du texte</b> pour sauter : si la fenêtre se termine sur un « E » et que le motif « ANANAS » ne contient aucun « E », aucune position de la fenêtre qui recouvre ce « E » ne peut convenir. On peut donc sauter <b>toute la longueur du motif</b> d’un coup.</li></ol>
<p>Si le caractère existe dans le motif, on décale juste assez pour l’aligner avec sa <b>dernière occurrence</b> dans le motif : c’est le seul décalage qui ne risque pas de manquer une occurrence.</p>
<p>R. Nigel <b>Horspool</b> a proposé en 1980 une version simplifiée, la plus enseignée : le saut ne dépend que du caractère du texte situé sous la <b>dernière case</b> du motif, quel que soit l’endroit de l’échec. C’est la version détaillée ci-dessous.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1977 <b>·</b></span> Robert S. Boyer et J Strother Moore publient « A fast string searching algorithm » dans la revue <i>Communications of the ACM</i>. La même année paraît l’algorithme de Knuth, Morris et Pratt, qui ne relit jamais un caractère du texte.<br><span class="commit">1980 <b>·</b></span> R. Nigel Horspool publie la version simplifiée qui porte son nom.</p></div>` },

    { id: "i4", t: "Le prétraitement : la table de décalage", h: `
<p>Avant toute recherche, on calcule à partir du <b>motif seul</b> une table qui dit de combien sauter selon le caractère <i>c</i> du texte lu sous la dernière case de la fenêtre :</p>
<ul><li>si <i>c</i> apparaît dans le motif <b>ailleurs qu’en dernière position</b>, saut = distance entre sa <b>dernière</b> occurrence (hors dernière case) et la fin du motif, soit <i>m</i> − 1 − <i>i</i> ;</li>
<li>sinon (caractère absent, ou présent seulement en dernière case), saut = <i>m</i>.</li></ul>
[[txt-table]]
[[w-trace|txt-table]]
<p>Pour « ANANAS » (<i>m</i> = 6) : le A d’indice 0 donne 5, puis le N d’indice 1 donne 4, le A d’indice 2 donne 3 (et <b>remplace</b> 5), le N d’indice 3 donne 2, le A d’indice 4 donne 1. Le S final n’est pas pris en compte : tous les autres caractères, S compris, donnent un saut de 6.</p>
<div class="tab-wrap"><table><tr><th>caractère</th><th>A</th><th>N</th><th>tout autre (S, E, espace…)</th></tr><tr><td>saut</td><td>1</td><td>2</td><td>6</td></tr></table></div>
<p>Le dernier caractère est exclu pour une raison précise : il donnerait un saut de 0, et la fenêtre ne bougerait plus. Ce prétraitement coûte <i>m</i> opérations et un petit dictionnaire ; il est fait <b>une seule fois</b>, puis amorti sur tout le texte. Si l’on cherche le même motif dans mille fichiers, on ne le refait pas.</p>` },

    { id: "i5", t: "La recherche, pas à pas", h: `
<p>La fenêtre commence en position <i>i</i> = 0. À chaque position : on compare de droite à gauche ; si tout correspond, on note l’occurrence ; dans tous les cas, on avance de <code>d.get(texte[i + m - 1], m)</code>.</p>
[[txt-horspool]]
<p>Le déroulement complet pour « ANANAS » : chaque ligne est une position de la fenêtre.</p>
[[txt-trace]]
<p>7 positions de fenêtre au lieu des 20 de l’algorithme naïf. Les deux sauts de 6 viennent d’un « S » puis d’un « E » sous la dernière case : aucun « E » dans le motif, et le seul « S » est en dernière position, donc exclu de la table.</p>
[[w-algo-boyer-moore|horspool]]` },

    { id: "i6", t: "Combien de comparaisons ? Un gain qui grandit avec le motif", h: `
<p>Comptons les comparaisons de caractères sur un texte de 59 000 caractères (une phrase répétée 1 000 fois), pour un motif court qui apparaît et pour un motif plus long qui n’apparaît pas :</p>
[[txt-compte]]
<div class="tab-wrap"><table><tr><th>motif</th><th>naïf</th><th>Horspool</th></tr><tr><td>« roman » (5 caractères)</td><td>64 996</td><td>18 000</td></tr><tr><td>« Stendhal paru en 1831 » (21 caractères)</td><td>78 980</td><td>4 001</td></tr></table></div>
<p>Le naïf fait toujours un peu plus de <i>n</i> comparaisons ; Horspool en fait de l’ordre de <i>n</i> / <i>m</i> quand les sauts sont grands : <b>plus le motif est long, plus il va vite</b>. C’est contre-intuitif et c’est le point à retenir. Mais il existe des cas défavorables, pour les deux algorithmes :</p>
[[txt-pire]]
<p>Le programme précise que l’étude du coût ne peut pas être exigée : on retient seulement que le pire cas reste de l’ordre de <i>n</i> × <i>m</i>, mais qu’en pratique (textes, ADN avec des motifs assez longs) Boyer-Moore est bien plus rapide.</p>` },

    { id: "i7", t: "Variante : la règle du « mauvais caractère »", h: `
<p>Certains sujets présentent Boyer-Moore avec la règle du <b>mauvais caractère</b> : en cas d’échec à l’indice <i>j</i> du motif sur le caractère <i>c</i> du texte, on décale pour aligner <i>c</i> avec sa dernière occurrence dans le motif, et d’au moins une case. Si <i>c</i> n’est pas dans le motif, on place le motif juste après lui.</p>
[[txt-bm]]
<p>Les deux versions trouvent exactement les mêmes occurrences ; seuls les sauts diffèrent. Lis bien l’énoncé : il dit toujours quelle règle appliquer et donne en général la table.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>L’algorithme complet de Boyer et Moore ajoute une seconde règle, dite du <b>bon suffixe</b> (réutiliser la partie du motif qui a déjà correspondu), et prend le plus grand des deux sauts. Il garantit un nombre de comparaisons proportionnel à <i>n</i> dans le pire cas pour la recherche de la première occurrence. Les fonctions <code>find</code> et <code>in</code> de CPython (l’interpréteur Python usuel) utilisent un mélange de Boyer-Moore et de Horspool ; depuis Python 3.10, pour les longs motifs (au moins 100 caractères) dans de longs textes, elles passent à l’algorithme « two-way » de Crochemore et Perrin (1991). Source : le code de CPython, fichier <code>Objects/stringlib/fastsearch.h</code>.</p></div>` }
  ],
  pieges: [
    { t: "Oublier la dernière position de la fenêtre", h: `[[txt-p-borne]]<p>Il y a <i>n</i> − <i>m</i> + 1 positions : la boucle est <code>range(len(texte) - len(motif) + 1)</code> (ou <code>while i &lt;= n - m</code>). Sinon, on rate une occurrence qui termine le texte, et un motif égal au texte n’est jamais trouvé.</p>` },
    { t: "Mettre le dernier caractère dans la table de Horspool", h: `[[txt-p-dernier]]<p>Le dernier caractère donnerait un saut de 0 : dès que la fenêtre se termine sur ce caractère, elle ne bouge plus et la boucle tourne indéfiniment. On boucle sur <code>range(m - 1)</code>.</p>` },
    { t: "Garder la première occurrence au lieu de la dernière", h: `<p>Pour un caractère répété (le A de « ANANAS »), il faut la <b>plus petite</b> distance à la fin, donc l’occurrence <b>la plus à droite</b> (hors dernière case). Avec la première, on sauterait trop loin et on pourrait <b>manquer</b> une occurrence. En parcourant le motif de gauche à droite, l’écrasement dans le dictionnaire donne automatiquement la bonne valeur.</p>` },
    { t: "Lire le saut sur le caractère de l’échec (dans Horspool)", h: `<p>Dans la version de Horspool, le saut dépend du caractère du texte <b>sous la dernière case</b> de la fenêtre, <code>texte[i + m - 1]</code>, même si l’échec a eu lieu plus à gauche. C’est la règle du mauvais caractère (idée 7) qui utilise le caractère de l’échec. Ne mélange pas les deux.</p>` },
    { t: "Croire que Boyer-Moore est toujours plus rapide", h: `<p>Sur « BAAA » dans « AAAA…A », Horspool compare tout le motif à chaque position et n’avance que d’une case : 3 988 comparaisons, quatre fois plus que le naïf. Et pour un motif d’un seul caractère, il n’y a rien à gagner. Le gain est réel sur les textes courants et les motifs longs.</p>` }
  ],
  retenir: `
<h2>Boyer-Moore-Horspool</h2>
[[txt-retenir]]
<h2>La table de décalage</h2>
<ul><li>Pour chaque caractère du motif <b>sauf le dernier</b> : <i>m</i> − 1 − (indice de sa dernière occurrence).</li><li>Tout autre caractère : <i>m</i>.</li><li>Exemple « ANANAS » : A → 1, N → 2, autres → 6. « GCAGAGAG » : A → 1, G → 2, C → 6, autres → 8.</li></ul>
<h2>Comparaison</h2>
<div class="tab-wrap"><table><tr><th></th><th>naïf</th><th>Boyer-Moore-Horspool</th></tr>
<tr><td>sens de comparaison</td><td>gauche → droite</td><td>droite → gauche</td></tr>
<tr><td>décalage</td><td>toujours 1</td><td>lu dans la table (1 à m)</td></tr>
<tr><td>prétraitement</td><td>aucun</td><td>table du motif, une fois</td></tr>
<tr><td>pire cas</td><td>≈ n × m</td><td>≈ n × m</td></tr>
<tr><td>cas courant</td><td>un peu plus de n</td><td>≈ n / m : plus rapide si le motif est long</td></tr></table></div>
<h2>Repères</h2><ul><li>Boyer et Moore, 1977 ; Horspool, 1980.</li><li>Le coût n’est pas exigible (BO) ; l’intérêt du <b>prétraitement</b>, si.</li></ul>`,
  predis: [
    { code: "txt-x1", niv: "facile", rep: "<i>m</i> = 11 ; on parcourt les indices 0 à 9 (le dernier A est exclu) et chaque caractère garde sa dernière occurrence : A en 7 donne 3, B en 8 donne 2, R en 9 donne 1, C en 4 donne 6, D en 6 donne 4." },
    { code: "txt-x2", niv: "moyen", rep: "La recherche naïve trouve les occurrences qui se chevauchent : 0, 2 et 4. <code>count</code>, lui, reprend sa recherche <b>après</b> chaque occurrence trouvée : seulement 2." },
    { code: "txt-x3", niv: "difficile", rep: "Table de « GACA » (<i>m</i> = 4) : G → 3, A → 2 (son occurrence d’indice 1), C → 1, autres → 4. On lit le caractère sous la dernière case : i = 0, texte[3] = A → 2 ; i = 2, texte[5] = A → 2 ; i = 4, texte[7] = A → 2 ; i = 6, texte[9] = T, absent → 4 ; i = 10, texte[13] = A → 2 ; i = 12 &gt; 14 − 4 : fin. Les fenêtres 2 et 10 sont les deux occurrences de GACA." },
    { code: "txt-x4", niv: "facile", rep: "« informatique » : i(0) n(1) f(2) o(3) r(4) m(5) a(6) : « ma » commence en 5 ; « que » commence en 9 (q(9) u(10) e(11)). Un motif plus long que le texte n’est jamais trouvé : −1." }
  ],
  ep: [
    { titre: "Recherche naïve de toutes les occurrences", enonce: `<p>On cherche un fragment d’ADN dans une séquence.</p>[[txt-ep1-fourni]]`,
      questions: [
        { q: "Compléter <code>est_en_position(texte, motif, i)</code> sans utiliser de tranche (<code>texte[i:j]</code>).", c: `<p>Vérifier d’abord que le motif tient dans le texte à partir de <i>i</i>, puis comparer caractère par caractère et renvoyer <code>False</code> au premier écart.</p>` },
        { q: "Compléter <code>recherche(texte, motif)</code>. Quel est le résultat attendu de l’appel fourni ?", c: `<p>On teste toutes les positions de 0 à <code>len(texte) - len(motif)</code> incluse : <code>[0, 5, 9]</code>.</p>` },
        { q: "Écrire un jeu de tests comprenant : occurrences qui se chevauchent, motif égal au texte, motif plus long que le texte, texte vide.", c: `[[txt-ep1-corr]]` },
        { q: "À l’oral : combien de comparaisons de caractères au plus pour un texte de 1 000 caractères et un motif de 10 ? Dans quel cas ce maximum est-il atteint ?", c: `<p>991 positions × 10 comparaisons = 9 910 au plus. C’est le cas quand presque tout le motif correspond à chaque position, par exemple « AAAAAAAAAB » dans « AAAA…A ».</p>` }
      ] },
    { titre: "Boyer-Moore-Horspool à corriger", enonce: `<p>Le programme ci-dessous ne termine pas sur le premier appel.</p>[[txt-ep2-fourni]]`,
      questions: [
        { q: "Calculer à la main <code>table_decalage(\"CAO\")</code> telle qu’elle est écrite. En déduire pourquoi <code>horspool(\"CACAO\", \"CAO\")</code> ne termine pas.", c: `<p>La boucle va jusqu’à <i>m</i> − 1 inclus : {'C': 2, 'A': 1, 'O': 0}. Quand la fenêtre se termine sur un « O » (position 2), le saut vaut 0 : <code>i</code> ne change plus, boucle infinie.</p>` },
        { q: "Corriger <code>table_decalage</code>. Que doit-elle renvoyer pour « CAO » ?", c: `<p><code>for i in range(m - 1)</code> : {'C': 2, 'A': 1}. Le « O » prend alors le saut par défaut, 3.</p>` },
        { q: "Écrire une fonction de test qui compare <code>horspool</code> à une recherche naïve sur plusieurs textes et motifs (dont des motifs absents et des chevauchements).", c: `[[txt-ep2-corr]]` },
        { q: "À l’oral : expliquer l’intérêt du prétraitement.", c: `<p>La table ne dépend que du motif : elle est calculée une seule fois, en <i>m</i> opérations, avant la recherche. Ensuite, chaque saut se lit en temps constant dans le dictionnaire. Si l’on cherche le même motif dans beaucoup de textes, ou dans un très long texte, ce petit coût initial est largement remboursé par les sauts.</p>` }
      ] }
  ],
  ecrit: { titre: "Un gène dans une séquence d’ADN", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>On cherche le motif <code>GCAGAGAG</code> dans la séquence <code>GCATCGCAGAGAGTATACAGTACG</code> (24 caractères) avec l’algorithme de Boyer-Moore dans la version de Horspool : comparaison de droite à gauche, puis décalage lu dans une table selon le caractère du texte situé sous la dernière case du motif. On utilise les fonctions <code>table_decalage</code> et <code>horspool</code> du cours.</p>`,
    questions: [
      { q: "Construire la table de décalage du motif. Que vaut le décalage pour T ?", pts: "1 pt", c: `<p><i>m</i> = 8. Indices 0 à 6 : G(0) → 7, C(1) → 6, A(2) → 5, G(3) → 4, A(4) → 3, G(5) → 2, A(6) → 1. Dernières valeurs : <b>G → 2, C → 6, A → 1</b>. T n’est pas dans le motif : décalage <b>8</b>.</p>` },
      { q: "Dérouler l’algorithme : pour chaque position de la fenêtre, indiquer le caractère sous la dernière case, le résultat de la comparaison et le décalage.", pts: "2 pts", c: `<p><i>i</i> = 0 : fenêtre GCATCGCA ; dernière case A ≠ G, échec immédiat ; sous la fin « A » → décalage 1.<br><i>i</i> = 1 : CATCGCAG ; G = G, A = A, puis C ≠ G : échec ; « G » → 2.<br><i>i</i> = 3 : TCGCAGAG ; G, A, G, A correspondent, puis C ≠ G : échec ; « G » → 2.<br><i>i</i> = 5 : GCAGAGAG ; les 8 caractères correspondent : <b>occurrence en 5</b> ; « G » → 2.<br><i>i</i> = 7 : AGAGAGTA ; A ≠ G : échec ; « A » → 1.<br><i>i</i> = 8 : GAGAGTAT ; T ≠ G : échec ; « T » → 8.<br><i>i</i> = 16 : ACAGTACG ; G = G, puis C ≠ A : échec ; « G » → 2.<br><i>i</i> = 18 &gt; 24 − 8 = 16 : fin.</p>` },
      { q: "Combien de positions de fenêtre et de comparaisons de caractères ? Comparer avec l’algorithme naïf.", pts: "1 pt", c: `<p>7 positions de fenêtre et 1 + 3 + 5 + 8 + 1 + 1 + 2 = <b>21 comparaisons</b>. L’algorithme naïf essaie les 17 positions et fait 30 comparaisons (on le vérifie en exécutant les deux fonctions du cours).</p>[[txt-ecrit-corr]]` },
      { q: "Pourquoi ne met-on pas le dernier caractère du motif dans la table ?", pts: "1 pt", c: `<p>Sa distance à la fin du motif est 0 : la fenêtre ne bougerait plus quand ce caractère se trouve sous la dernière case (boucle infinie).</p>` },
      { q: "Expliquer pourquoi l’algorithme est d’autant plus efficace que le motif est long.", pts: "1 pt", c: `<p>Quand le caractère sous la dernière case n’apparaît pas dans le motif, la fenêtre saute de <i>m</i> cases d’un coup : avec un long motif, on examine une petite fraction des caractères du texte (environ <i>n</i>/<i>m</i> dans le meilleur cas). Le naïf, lui, regarde au moins chaque caractère une fois.</p>` }
    ],
    methode: `<p>Pour dérouler Boyer-Moore à la main, fais un tableau à quatre colonnes : position <i>i</i> de la fenêtre, caractères comparés (de droite à gauche, en soulignant l’échec), caractère sous la dernière case, décalage. Écris la table de décalage en premier et vérifie à la fin que la dernière fenêtre ne dépasse pas le texte (<i>i</i> ≤ <i>n</i> − <i>m</i>).</p>` },
  qcm: [
    { q: "Combien de positions possibles a une fenêtre de longueur m dans un texte de longueur n ?", c: ["n", "n − m", "n − m + 1", "n × m"], a: 2, e: "De 0 à n − m inclus.", ref: "i1" },
    { q: "Que renvoie la recherche naïve de « AA » dans « AAAA » (toutes les occurrences) ?", c: ["[0]", "[0, 2]", "[0, 1, 2]", "[0, 1, 2, 3]"], a: 2, e: "Les occurrences peuvent se chevaucher.", ref: "i1" },
    { q: "De combien l’algorithme naïf décale-t-il la fenêtre après un échec ?", c: ["De 1", "De m", "De la valeur lue dans une table", "De n − m"], a: 0, e: "Il n’exploite pas ce qu’il a lu.", ref: "i2" },
    { q: "Quel est l’ordre de grandeur du nombre de comparaisons de l’algorithme naïf dans le pire cas ?", c: ["n", "n + m", "n × m", "n / m"], a: 2, e: "Jusqu’à m comparaisons pour chacune des n − m + 1 positions.", ref: "i2" },
    { q: "Dans Boyer-Moore, dans quel sens compare-t-on le motif et la fenêtre ?", c: ["De gauche à droite", "De droite à gauche", "Du milieu vers les bords", "Dans un ordre aléatoire"], a: 1, e: "On commence par la dernière case du motif.", ref: "i3" },
    { q: "Sous la dernière case de la fenêtre se trouve un caractère absent du motif « ANANAS ». De combien saute-t-on (Horspool) ?", c: ["1", "2", "5", "6"], a: 3, e: "Aucune position qui recouvre ce caractère ne peut convenir : on saute de m = 6.", ref: "i3" },
    { q: "Qu’appelle-t-on le prétraitement dans Boyer-Moore ?", c: ["Le tri du texte", "Le calcul, à partir du motif seul, de la table de décalage", "La conversion du texte en minuscules", "La recherche naïve faite avant"], a: 1, e: "Fait une seule fois, avant la recherche.", ref: "i4" },
    { q: "Quelle est la table de décalage de Horspool pour le motif « ANANAS » ?", c: ["A → 1, N → 2", "A → 5, N → 4, S → 0", "A → 1, N → 2, S → 0", "A → 3, N → 2"], a: 0, e: "Dernières occurrences hors dernière case : A en 4 (6 − 1 − 4 = 1), N en 3 (2). Tout le reste : 6.", ref: "i4" },
    { q: "Pourquoi exclut-on le dernier caractère du motif de la table ?", c: ["Pour gagner de la mémoire", "Il donnerait un décalage nul, donc une boucle infinie", "Il est toujours absent du texte", "Par convention, sans raison"], a: 1, e: "Sa distance à la fin du motif est 0.", ref: "i4" },
    { q: "Dans Horspool, quel caractère détermine le saut ?", c: ["Le premier caractère du motif", "Le caractère du texte où a eu lieu l’échec", "Le caractère du texte sous la dernière case de la fenêtre", "Le dernier caractère du texte"], a: 2, e: "Toujours texte[i + m − 1], même si l’échec a eu lieu plus à gauche.", ref: "i5" },
    { q: "Pour quels motifs Boyer-Moore-Horspool est-il le plus avantageux ?", c: ["Les motifs d’un seul caractère", "Les motifs longs", "Les motifs qui contiennent toutes les lettres", "Il est toujours équivalent au naïf"], a: 1, e: "Les sauts peuvent atteindre m : environ n / m comparaisons dans les cas favorables.", ref: "i6" },
    { q: "Que dit le programme sur l’étude du coût de Boyer-Moore ?", c: ["Elle est au cœur de l’épreuve", "Elle est difficile et ne peut pas être exigée", "Elle doit être démontrée", "Elle n’a aucun intérêt"], a: 1, e: "On met en avant l’intérêt du prétraitement, sans calcul de coût exigible.", ref: "i6" },
    { q: "Dans la règle du « mauvais caractère », sur quel caractère s’appuie le décalage ?", c: ["Sur le caractère du texte qui a provoqué l’échec", "Sur le dernier caractère du motif", "Sur le premier caractère du texte", "Sur aucun"], a: 0, e: "On l’aligne avec sa dernière occurrence dans le motif (au moins un cran).", ref: "i7" }
  ],
  cartes: [
    { r: "Motif, texte, occurrence", v: "On cherche les positions i telles que texte[i:i+m] == motif. Les occurrences peuvent se chevaucher." },
    { r: "Algorithme naïf", v: "Toutes les positions, comparaison de gauche à droite, décalage de 1. Pire cas ≈ n × m comparaisons." },
    { r: "Idée de Boyer-Moore", v: "Comparer de droite à gauche ; utiliser le caractère lu dans le texte pour sauter plusieurs positions d’un coup." },
    { r: "Table de décalage (Horspool)", v: "Pour chaque caractère du motif sauf le dernier : m − 1 − indice de sa dernière occurrence. Autres caractères : m." },
    { r: "Table de « ANANAS »", v: "A → 1, N → 2, tout autre caractère → 6." },
    { r: "Saut de Horspool", v: "i = i + d.get(texte[i + m − 1], m) : selon le caractère du texte sous la DERNIÈRE case de la fenêtre." },
    { r: "Prétraitement", v: "Calcul de la table à partir du motif seul, une fois, avant la recherche. Coût ≈ m, amorti sur tout le texte." },
    { r: "Pourquoi le dernier caractère est exclu", v: "Il donnerait un saut de 0 : boucle infinie." },
    { r: "Efficacité de Boyer-Moore-Horspool", v: "Environ n / m comparaisons dans les cas favorables : plus le motif est long, plus c’est rapide. Pire cas ≈ n × m." },
    { r: "Règle du mauvais caractère", v: "Échec sur le caractère c du texte : aligner c avec sa dernière occurrence dans le motif (au moins 1 case) ; s’il est absent, placer le motif après lui." },
    { r: "Coût de Boyer-Moore au bac", v: "Non exigible (BO). On retient l’intérêt du prétraitement et on compare les comparaisons sur un exemple." },
    { r: "Dates", v: "Boyer et Moore, 1977 (Communications of the ACM). Horspool, 1980. Knuth-Morris-Pratt, 1977." }
  ]
});
