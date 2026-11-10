/* ===================== Histoire de l'informatique ===================== */
C("hist-euclide", String.raw`
def pgcd(a, b):
    """Algorithme d'Euclide (Éléments, livre VII, vers 300 av. J.-C.), version par divisions."""
    while b != 0:
        a, b = b, a % b              # pgcd(a, b) = pgcd(b, reste de a par b)
    return a

print(pgcd(1071, 462), pgcd(2026, 1936))`, { out: "21 2" });

C("hist-heron", String.raw`
def racine(a, etapes):
    """Méthode de Héron d'Alexandrie (Ier siècle) : x devient la moyenne de x et a / x."""
    x = a
    for _ in range(etapes):
        x = (x + a / x) / 2
    return x

for k in [1, 2, 3, 4, 5]:
    print(k, racine(2, k))`, { out: "1 1.5\n2 1.4166666666666665\n3 1.4142156862745097\n4 1.4142135623746899\n5 1.414213562373095" });

C("hist-binaire", String.raw`
def en_binaire(n):
    """Écriture binaire de l'entier n >= 1, par divisions successives par 2."""
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n = n // 2
    return chiffres

for annee in [1703, 1936, 1969]:
    print(annee, en_binaire(annee), bin(annee))`, { out: "1703 11010100111 0b11010100111\n1936 11110010000 0b11110010000\n1969 11110110001 0b11110110001" });

C("hist-bernoulli", String.raw`
from fractions import Fraction
from math import comb

def bernoulli(n):
    """Nombres de Bernoulli B0..Bn (convention moderne, B1 = -1/2),
    par la relation : somme des comb(m + 1, k) * B_k pour k de 0 à m = 0."""
    B = [Fraction(1)]
    for m in range(1, n + 1):
        s = sum(comb(m + 1, k) * B[k] for k in range(m))
        B.append(-s / (m + 1))
    return B

B = bernoulli(8)
print([str(b) for b in B])
print("B8 =", B[8])`, { out: "['1', '-1/2', '1/6', '0', '-1/30', '0', '1/42', '0', '-1/30']\nB8 = -1/30" });

C("hist-moore", String.raw`
transistors, annee = 2300, 1971          # Intel 4004
while annee < 2021:
    transistors = transistors * 2        # loi de Moore (1975) : doublement tous les 2 ans
    annee = annee + 2
print(annee, transistors)
print(round(transistors / 2300), "fois plus qu'en 1971")`, { out: "2021 77175193600\n33554432 fois plus qu'en 1971" });

C("hist-frise", String.raw`
REPERES = {
    1642: "Pascaline (Blaise Pascal)",
    1843: "notes d'Ada Lovelace sur la machine analytique",
    1936: "machine de Turing",
    1948: "premier programme enregistré (Manchester)",
    1969: "ARPANET",
    1991: "premier site web (CERN)",
}

def avant(annee):
    return [a for a in sorted(REPERES) if a < annee]

print(avant(1900))
print(max(REPERES) - min(REPERES), "ans entre", REPERES[min(REPERES)], "et", REPERES[max(REPERES)])`, { out: "[1642, 1843]\n349 ans entre Pascaline (Blaise Pascal) et premier site web (CERN)" });

/* prédis la sortie */
C("hist-x1", String.raw`
a, b, etapes = 252, 105, 0
while b != 0:
    a, b = b, a % b
    etapes = etapes + 1
print(a, etapes)`, { out: "21 3" });

C("hist-x2", String.raw`
print(int("101010", 2), bin(1948)[2:].count("1"))`, { out: "42 7" });

C("hist-x3", String.raw`
def crible(n):
    """Crible d'Ératosthène (IIIe siècle av. J.-C.) : nombres premiers jusqu'à n."""
    premier = [True] * (n + 1)
    premier[0] = premier[1] = False
    for i in range(2, n + 1):
        if premier[i]:
            for multiple in range(i * i, n + 1, i):
                premier[multiple] = False
    return [i for i in range(n + 1) if premier[i]]

print(crible(30))`, { out: "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]" });

C("hist-x4", String.raw`
evenements = [("Web", 1989), ("ARPANET", 1969), ("Turing", 1936), ("Linux", 1991)]
evenements.sort(key=lambda e: e[1])
print([nom for nom, annee in evenements if annee >= 1950])`, { out: "['ARPANET', 'Web', 'Linux']" });

/* épreuve pratique 1 */
C("hist-ep1-fourni", String.raw`
def pgcd_iter(a, b):
    """PGCD de deux entiers positifs, par l'algorithme d'Euclide (version itérative)."""
    ...

def pgcd_rec(a, b):
    """Même calcul, version récursive."""
    ...

def nb_divisions(a, b):
    """Nombre de divisions effectuées par l'algorithme d'Euclide."""
    ...`, { fichier: "euclide.py", run: false });

C("hist-ep1-corr", String.raw`
from math import gcd

def pgcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pgcd_rec(a, b):
    if b == 0:
        return a
    return pgcd_rec(b, a % b)

def nb_divisions(a, b):
    n = 0
    while b != 0:
        a, b = b, a % b
        n = n + 1
    return n

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def test():
    assert pgcd_iter(1071, 462) == pgcd_rec(1071, 462) == 21
    assert pgcd_iter(17, 5) == 1                     # premiers entre eux
    assert pgcd_iter(12, 0) == 12 and pgcd_rec(0, 12) == 12
    for a in range(1, 60):
        for b in range(1, 60):
            assert pgcd_iter(a, b) == pgcd_rec(a, b) == gcd(a, b)
    assert nb_divisions(1071, 462) == 3
    assert nb_divisions(fib(21), fib(20)) == 19      # deux Fibonacci consécutifs : le pire cas (Lamé, 1844)

test()
print(fib(21), fib(20), nb_divisions(fib(21), fib(20)))
print("tous les tests passent")`, { fichier: "euclide.py", out: "10946 6765 19\ntous les tests passent" });

/* épreuve pratique 2 */
C("hist-ep2-fourni", String.raw`
FRISE = [
    ("ENIAC présenté au public", 1946, "matériel"),
    ("langage Fortran", 1957, "logiciel"),
    ("transistor", 1947, "matériel"),
    ("premier microprocesseur, Intel 4004", 1971, "matériel"),
    ("système Unix", 1969, "logiciel"),
    ("langage Python", 1991, "logiciel"),
    ("protocole TCP/IP adopté sur ARPANET", 1983, "réseau"),
]

def trier(frise):
    """Renvoie une NOUVELLE liste des événements triés par date."""
    ...

def par_decennie(frise):
    """Dictionnaire {décennie: [noms des événements]} ; 1957 est dans la décennie 1950."""
    ...`, { fichier: "frise.py", run: false });

C("hist-ep2-corr", String.raw`
FRISE = [
    ("ENIAC présenté au public", 1946, "matériel"),
    ("langage Fortran", 1957, "logiciel"),
    ("transistor", 1947, "matériel"),
    ("premier microprocesseur, Intel 4004", 1971, "matériel"),
    ("système Unix", 1969, "logiciel"),
    ("langage Python", 1991, "logiciel"),
    ("protocole TCP/IP adopté sur ARPANET", 1983, "réseau"),
]

def trier(frise):
    return sorted(frise, key=lambda e: e[1])

def par_decennie(frise):
    d = {}
    for nom, annee, categorie in frise:
        dec = annee // 10 * 10
        if dec not in d:
            d[dec] = []
        d[dec].append(nom)
    return d

def premier_de(frise, categorie):
    candidats = [e for e in frise if e[2] == categorie]
    if candidats == []:
        return None
    return min(candidats, key=lambda e: e[1])[0]

def test():
    t = trier(FRISE)
    assert [e[1] for e in t] == [1946, 1947, 1957, 1969, 1971, 1983, 1991]
    assert FRISE[0][1] == 1946 and FRISE[1][1] == 1957          # FRISE n'est pas modifiée
    d = par_decennie(FRISE)
    assert sorted(d) == [1940, 1950, 1960, 1970, 1980, 1990]
    assert len(d[1940]) == 2
    assert premier_de(FRISE, "logiciel") == "langage Fortran"
    assert premier_de(FRISE, "jeu") is None

test()
for dec, noms in sorted(par_decennie(FRISE).items()):
    print(dec, noms)
print("tous les tests passent")`, { fichier: "frise.py", out: String.raw`
1940 ['ENIAC présenté au public', 'transistor']
1950 ['langage Fortran']
1960 ['système Unix']
1970 ['premier microprocesseur, Intel 4004']
1980 ['protocole TCP/IP adopté sur ARPANET']
1990 ['langage Python']
tous les tests passent` });

C("hist-retenir", String.raw`
-300   Euclide (PGCD)            1936  Turing, Church        1969  ARPANET, Unix
 825   al-Khwarizmi              1945  von Neumann (EDVAC)   1971  Intel 4004
1642   Pascaline                 1947  transistor            1973  Micral N
1801   métier Jacquard           1948  Manchester Baby       1983  TCP/IP
1843   Ada Lovelace              1957  Fortran               1989  Web (proposition)
1854   Boole                     1958  circuit intégré       1991  Linux, Python, 1er site web`, { run: false });

CH.push({
  id: "hist", court: "histoire", fichier: "histoire.md",
  titre: "Histoire de l’informatique",
  rubrique: "Rubrique « Histoire de l’informatique » : événements clés, protagonistes, évolution des rôles du logiciel et du matériel",
  accroche: "De l’algorithme d’Euclide au smartphone : les dates, les personnes et les idées à situer, et comment le logiciel a pris le pas sur le matériel.",
  essentiel: [
    "Les <b>algorithmes</b> existent depuis l’Antiquité (Euclide, vers −300 ; al-Khwarizmi, IXe siècle, qui a donné son nom au mot) ; les <b>machines à calculer</b> datent du XVIIe siècle (Pascaline, 1642).",
    "Au XIXe siècle : cartes perforées (Jacquard, 1801), machine analytique de <b>Babbage</b> et premier programme publié par <b>Ada Lovelace</b> (1843), algèbre de <b>Boole</b> (1854).",
    "<b>1936</b> : Turing (et Church) définissent ce qu’est un calcul et la machine universelle. <b>1945</b> : architecture de von Neumann. <b>1948</b> : premier programme enregistré exécuté (Manchester).",
    "Le matériel se miniaturise : transistor (1947), circuit intégré (1958), microprocesseur (1971), micro-ordinateur (1973), smartphone (2007). Le logiciel suit : Fortran (1957), Unix (1969), Python (1991).",
    "Les réseaux : <b>ARPANET</b> (1969), TCP/IP (1974, adopté en 1983), le <b>Web</b> (1989-1991). Le logiciel est devenu l’essentiel de la valeur et du coût d’un système."
  ],
  attendus: [
    "Situer dans le temps les principaux événements de l’histoire de l’informatique et leurs protagonistes (BO).",
    "Identifier l’évolution des rôles relatifs des logiciels et des matériels (BO).",
    "Ces repères complètent ceux de Première et se construisent avec les autres chapitres : sur ce site, ils sont aussi dans les encadrés <code># git log --histoire</code> de chaque chapitre.",
    "À l’écrit, l’histoire apparaît surtout en introduction d’un exercice ou en question de culture ; au Grand oral, elle donne du relief à une question."
  ],
  idees: [
    { id: "i1", t: "Des algorithmes avant les machines", h: `
<p>Un <b>algorithme</b> est une suite finie d’instructions qui résout un problème. On en écrit depuis bien avant les ordinateurs :</p>
<ul><li>vers <b>−1800</b>, des tablettes babyloniennes décrivent des méthodes de calcul pas à pas (approximations de racines carrées) ;</li>
<li>vers <b>−300</b>, <b>Euclide</b> décrit dans ses <i>Éléments</i> l’algorithme du plus grand commun diviseur, toujours utilisé (il sert dans le chiffrement RSA) ;</li>
<li>vers <b>825</b>, le savant persan <b>al-Khwarizmi</b>, à Bagdad, écrit des traités de calcul et d’algèbre ; son nom latinisé a donné le mot « algorithme », et le titre d’un de ses livres le mot « algèbre ».</li></ul>
[[hist-euclide]]
<p>La méthode de Héron d’Alexandrie (Ier siècle) pour approcher √2 double à peu près le nombre de décimales justes à chaque étape :</p>
[[hist-heron]]
[[w-algo-frise]]` },

    { id: "i2", t: "Machines à calculer et cartes perforées (XVIIe-XIXe siècle)", h: `
<ul><li><b>1642</b> : <b>Blaise Pascal</b>, 19 ans, conçoit la <b>Pascaline</b>, machine à additionner et soustraire à roues dentées, pour aider son père, commissaire aux impôts.</li>
<li><b>1673</b> : <b>Leibniz</b> présente une machine qui multiplie ; en <b>1703</b>, il expose l’<b>arithmétique binaire</b> (avec seulement 0 et 1), la base de tous les ordinateurs actuels.</li>
<li><b>1801</b> : le métier à tisser de <b>Joseph-Marie Jacquard</b> est piloté par des <b>cartes perforées</b> : changer de motif, c’est changer de cartes, sans toucher à la machine. C’est déjà l’idée d’un programme séparé du matériel.</li>
<li><b>1834-1843</b> : <b>Charles Babbage</b> conçoit la <b>machine analytique</b>, programmable par cartes perforées, avec une unité de calcul (le « moulin ») et une mémoire (le « magasin ») ; elle ne sera jamais construite. En <b>1843</b>, <b>Ada Lovelace</b> publie des notes où elle détaille un programme pour calculer les nombres de Bernoulli : on la considère comme la première personne à avoir publié un programme. Elle pressent aussi que la machine pourrait manipuler autre chose que des nombres (de la musique, par exemple).</li>
<li><b>1854</b> : <b>George Boole</b> formalise la logique avec une algèbre à deux valeurs (vrai, faux) : l’algèbre de Boole des circuits logiques.</li>
<li><b>1890</b> : <b>Herman Hollerith</b> traite le recensement des États-Unis avec des machines à cartes perforées ; son entreprise deviendra IBM en 1924.</li></ul>
[[hist-binaire]]
<div class="boite hp"><div class="lab"># pour aller plus loin : le programme d’Ada Lovelace en Python</div><p>Sa note G calcule le nombre de Bernoulli qu’on note aujourd’hui B<sub>8</sub> (B<sub>7</sub> dans sa numérotation). Avec des fractions exactes :</p>[[hist-bernoulli]]</div>` },

    { id: "i3", t: "1936 et après : les fondements théoriques", h: `
<p>En <b>1936</b>, <b>Alan Turing</b> (britannique, 1912-1954) publie « On Computable Numbers, with an Application to the Entscheidungsproblem ». Il y définit la <b>machine de Turing</b>, montre qu’une <b>machine universelle</b> peut simuler toutes les autres, et qu’il existe des problèmes <b>indécidables</b> (chapitre Calculabilité). La même année, <b>Alonzo Church</b> arrive au même résultat avec le lambda-calcul. Le programme de NSI retient 1936 comme l’année du « concept de machine universelle ».</p>
<ul><li><b>1937</b> : <b>Claude Shannon</b> montre, dans son mémoire de master, que l’algèbre de Boole permet de concevoir des circuits à relais : c’est la naissance des circuits logiques.</li>
<li><b>1939-1945</b> : à Bletchley Park, Turing et ses collègues cassent les messages chiffrés par la machine allemande Enigma, en s’aidant de machines électromécaniques (les « bombes »).</li>
<li><b>1948</b> : Shannon fonde la <b>théorie de l’information</b> et popularise le mot <b>bit</b> (<i>binary digit</i>).</li>
<li><b>1950</b> : Turing propose son « jeu de l’imitation » (le test de Turing) pour se demander si une machine peut penser.</li></ul>
<div class="boite ex"><div class="lab"># le prix Turing</div><p>Depuis 1966, l’association ACM décerne chaque année le <b>prix Turing</b>, souvent présenté comme le « Nobel de l’informatique ». Des lauréats que tu croises dans ce site : Dijkstra (1972), Knuth (1974), Codd (1981, bases de données), Cerf et Kahn (2004, TCP/IP), Barbara Liskov (2008), Berners-Lee (2016, le Web).</p></div>` },

    { id: "i4", t: "Les premiers ordinateurs (1941-1949)", h: `
<ul><li><b>1941</b> : <b>Konrad Zuse</b> fait fonctionner à Berlin le <b>Z3</b>, calculateur électromécanique (à relais) programmable, piloté par un film perforé.</li>
<li><b>1943-1944</b> : <b>Colossus</b>, machine électronique (à tubes) construite à Bletchley Park par Tommy Flowers pour déchiffrer les messages Lorenz du haut commandement allemand ; elle reste secrète jusque dans les années 1970.</li>
<li><b>1945-1946</b> : l’<b>ENIAC</b> (États-Unis) : 18 000 tubes, environ 30 tonnes, environ 5 000 additions par seconde. Il est « programmé » en <b>recâblant</b> des panneaux et en réglant des interrupteurs, travail réalisé en grande partie par six programmeuses (dont Jean Jennings et Betty Holberton).</li>
<li><b>1945</b> : <b>John von Neumann</b> décrit, dans le rapport sur l’EDVAC, une machine où le <b>programme est enregistré dans la mémoire</b>, comme les données : unité de calcul, unité de contrôle, mémoire, entrées-sorties. C’est l’<b>architecture de von Neumann</b>, vue en Première.</li>
<li><b>21 juin 1948</b> : à l’université de Manchester, la « <b>Baby</b> » (Williams, Kilburn, Tootill) exécute le premier programme <b>enregistré en mémoire</b> : 17 instructions, qui cherchent le plus grand diviseur d’un nombre. Le programme de NSI date de <b>1948</b> les premiers ordinateurs.</li>
<li><b>1949</b> : l’<b>EDSAC</b> (Cambridge), premier ordinateur à programme enregistré utilisé pour des calculs au quotidien.</li></ul>
<p>Qu’est-ce qui change en 1948 ? Avant, changer de calcul voulait dire <b>modifier la machine</b> (recâbler l’ENIAC). Après, il suffit de <b>charger un autre programme</b> en mémoire : la machine devient universelle, au sens de Turing. Le logiciel est né.</p>` },

    { id: "i5", t: "Le matériel : la miniaturisation", h: `
<ul><li><b>1947</b> : invention du <b>transistor</b> aux laboratoires Bell (Bardeen, Brattain, Shockley ; prix Nobel de physique 1956). Il remplace les tubes : plus petit, plus fiable, moins gourmand.</li>
<li><b>1958</b> : <b>Jack Kilby</b> (Texas Instruments) réalise le premier <b>circuit intégré</b> (plusieurs composants sur une seule puce) ; Robert Noyce en propose une version au silicium en 1959.</li>
<li><b>1965</b> : <b>Gordon Moore</b> observe que le nombre de transistors par puce double à intervalle régulier (il fixe ce rythme à environ deux ans en 1975) : la « loi de Moore », une observation, pas une loi physique.</li>
<li><b>1971</b> : <b>Intel 4004</b>, premier <b>microprocesseur</b> commercialisé : tout le processeur sur une puce, 2 300 transistors.</li>
<li><b>1973</b> : en France, le <b>Micral N</b> (société R2E, conçu par François Gernelle), est le premier micro-ordinateur commercial à microprocesseur. Puis l’Apple II (1977), l’IBM PC (1981), le Macintosh (1984) mettent l’ordinateur sur les bureaux et dans les foyers.</li>
<li><b>2007</b> : l’iPhone popularise le <b>smartphone</b> ; ses composants sont réunis sur un <b>système sur puce</b> (SoC : processeur, mémoire, radio, graphisme), au programme de Terminale.</li></ul>
[[hist-moore]]
<p>Le calcul donne environ 77 milliards de transistors en 2021 : c’est l’ordre de grandeur des plus grosses puces grand public de cette année-là (57 milliards pour l’Apple M1 Max, 2021). La loi de Moore a tenu un demi-siècle ; elle ralentit depuis les années 2010, la gravure approchant des limites physiques.</p>` },

    { id: "i6", t: "Le logiciel : langages et systèmes", h: `
<ul><li><b>1947</b> : <b>Grace Hopper</b> et son équipe trouvent un papillon de nuit coincé dans un relais du Harvard Mark II et le collent dans le cahier de bord, « premier cas réel de bug trouvé » (le mot « bug » existait déjà). En <b>1952</b>, elle écrit l’un des premiers <b>compilateurs</b> (A-0) ; elle inspire ensuite COBOL (1959), langage de gestion.</li>
<li><b>1957</b> : <b>Fortran</b> (John Backus, IBM), premier langage de haut niveau largement diffusé, pour le calcul scientifique. <b>1958</b> : <b>LISP</b> (John McCarthy), fondé sur la récursivité.</li>
<li><b>1962</b> : Philippe Dreyfus crée le mot <b>informatique</b> (information + automatique).</li>
<li><b>1969</b> : <b>Margaret Hamilton</b> dirige l’équipe qui écrit le logiciel de vol embarqué des missions <b>Apollo</b> ; elle popularise l’expression « ingénierie logicielle ». La même année, Ken Thompson et Dennis Ritchie créent <b>Unix</b> aux laboratoires Bell ; Ritchie crée le <b>langage C</b> en 1972 pour le réécrire.</li>
<li><b>1970</b> : Edgar F. <b>Codd</b> invente le <b>modèle relationnel</b> ; le langage SQL naît chez IBM au milieu des années 1970 (chapitre Bases de données).</li>
<li><b>1991</b> : <b>Linus Torvalds</b> publie le noyau <b>Linux</b>, logiciel libre ; la même année, <b>Guido van Rossum</b> publie la première version de <b>Python</b>. Richard Stallman avait lancé le projet GNU et le mouvement du logiciel libre en 1983-1985.</li></ul>` },

    { id: "i7", t: "Les réseaux : d’ARPANET au Web", h: `
<ul><li><b>1969</b> : <b>ARPANET</b>, réseau financé par l’agence de recherche du ministère américain de la Défense, relie quatre sites universitaires et de recherche (UCLA, le SRI, l’université de Californie à Santa Barbara et l’université de l’Utah). Le premier message, le <b>29 octobre 1969</b>, devait être « login » : la machine réceptrice plante après « lo ». Le programme de NSI retient 1969 comme le début du développement d’Internet.</li>
<li><b>1974</b> : <b>Vint Cerf</b> et <b>Bob Kahn</b> décrivent le protocole <b>TCP</b>, qui permet de relier des réseaux différents ; ARPANET passe à <b>TCP/IP</b> le 1er janvier <b>1983</b>. Le Français Louis Pouzin avait conçu dès 1971-1973 le réseau Cyclades, fondé sur les datagrammes, une idée reprise par TCP/IP.</li>
<li><b>1976-1977</b> : Diffie et Hellman inventent l’échange de clés, puis Rivest, Shamir et Adleman le chiffrement <b>RSA</b> : le chiffrement asymétrique au programme de Terminale.</li>
<li><b>1982</b> : en France, le <b>Minitel</b> se diffuse dans les foyers (annuaire, services en ligne), dix ans avant le Web.</li>
<li><b>1989</b> : au CERN, <b>Tim Berners-Lee</b> propose le <b>World Wide Web</b> (HTTP, HTML, URL) ; le premier site est mis en ligne en 1991, et le CERN place la technologie du Web dans le domaine public en avril 1993.</li></ul>
<p>Internet et le Web ne sont pas la même chose : Internet est le réseau de réseaux (1969-1983), le Web est un service qui l’utilise (1989-1991), comme le courrier électronique.</p>` },

    { id: "i8", t: "Logiciel et matériel : des rôles qui s’inversent", h: `
<p>Le BO demande d’<b>identifier l’évolution des rôles relatifs des logiciels et des matériels</b>. Quatre étapes :</p>
<ol><li><b>Le matériel est tout</b> (années 1940) : la machine est construite pour un calcul ; la « programmer », c’est la recâbler (ENIAC). Le matériel coûte une fortune, le temps de calcul est précieux.</li>
<li><b>Le logiciel se sépare du matériel</b> (1948-1960) : programme enregistré, puis langages de haut niveau et compilateurs. Un même programme Fortran tourne sur plusieurs machines. En 1969, IBM commence à facturer ses logiciels séparément de ses ordinateurs : le logiciel devient un produit.</li>
<li><b>Le logiciel devient l’essentiel</b> (années 1970-2000) : le matériel, produit en masse, devient bon marché ; la valeur, le coût et les bugs sont dans le logiciel (systèmes d’exploitation, bureautique, Web). On parle de « crise du logiciel » dès 1968.</li>
<li><b>Le matériel se dématérialise et se spécialise</b> (depuis 2000) : virtualisation et informatique en nuage (une « machine » est souvent un logiciel qui en simule une), logiciels embarqués partout (voitures, objets connectés) ; et retour de matériels spécialisés pour accélérer certains logiciels (processeurs graphiques pour l’intelligence artificielle, SoC des téléphones).</li></ol>
<div class="tab-wrap"><table><tr><th>époque</th><th>exemple</th><th>changer de tâche, c’est…</th></tr>
<tr><td>1801</td><td>métier Jacquard</td><td>changer les cartes perforées</td></tr>
<tr><td>1946</td><td>ENIAC</td><td>recâbler la machine (des jours)</td></tr>
<tr><td>1948</td><td>Manchester Baby</td><td>charger un autre programme en mémoire</td></tr>
<tr><td>aujourd’hui</td><td>smartphone</td><td>installer une application (des secondes)</td></tr></table></div>
[[hist-frise]]` }
  ],
  pieges: [
    { t: "Confondre Internet et le Web", h: `<p>Internet (ARPANET, 1969 ; TCP/IP, 1983) est l’infrastructure, le réseau de réseaux. Le Web (Berners-Lee, 1989-1991) est un service qui fonctionne sur Internet, avec HTTP, HTML et les URL. Le courrier électronique est un autre service, plus ancien que le Web.</p>` },
    { t: "Dire que Turing a construit le premier ordinateur", h: `<p>En 1936, Turing décrit une machine <b>théorique</b>. Il travaille ensuite sur des machines réelles (les bombes de Bletchley Park, le projet ACE, le Manchester Mark 1), mais le premier programme enregistré exécuté l’est sur la Baby de Williams, Kilburn et Tootill (1948).</p>` },
    { t: "Croire que l’ENIAC est le premier ordinateur au sens moderne", h: `<p>L’ENIAC (1945-1946) est électronique et très rapide pour son époque, mais il se programme en le recâblant. L’ordinateur au sens actuel, avec programme <b>enregistré en mémoire</b> (architecture de von Neumann), date de 1948-1949.</p>` },
    { t: "Prendre la loi de Moore pour une loi physique", h: `<p>C’est une <b>observation</b> économique et technique (doublement du nombre de transistors par puce environ tous les deux ans), qui s’est vérifiée pendant un demi-siècle et ralentit aujourd’hui.</p>` },
    { t: "Inventer une date quand on hésite", h: `<p>À l’écrit et au Grand oral, mieux vaut un ordre de grandeur juste (« au milieu des années 1970 ») qu’une date fausse. Les repères à connaître sûrement sont ceux du programme : 1936, 1948, 1969, et ceux de la fiche « À retenir ».</p>` }
  ],
  retenir: `
<h2>La frise à connaître</h2>
[[hist-retenir]]
<h2>Les personnes</h2>
<div class="tab-wrap"><table><tr><th>qui</th><th>quand</th><th>quoi</th></tr>
<tr><td>Euclide</td><td>vers −300</td><td>algorithme du PGCD</td></tr>
<tr><td>al-Khwarizmi</td><td>IXe siècle</td><td>traités de calcul ; le mot « algorithme »</td></tr>
<tr><td>Blaise Pascal</td><td>1642</td><td>Pascaline</td></tr>
<tr><td>Leibniz</td><td>1673, 1703</td><td>machine à multiplier ; arithmétique binaire</td></tr>
<tr><td>Babbage, Ada Lovelace</td><td>1834-1843</td><td>machine analytique ; premier programme publié</td></tr>
<tr><td>George Boole</td><td>1854</td><td>algèbre de Boole</td></tr>
<tr><td>Alan Turing, Alonzo Church</td><td>1936</td><td>machine universelle, calculabilité</td></tr>
<tr><td>John von Neumann</td><td>1945</td><td>programme enregistré en mémoire</td></tr>
<tr><td>Claude Shannon</td><td>1937, 1948</td><td>circuits logiques, théorie de l’information</td></tr>
<tr><td>Grace Hopper</td><td>1952</td><td>compilateur A-0, COBOL</td></tr>
<tr><td>Margaret Hamilton</td><td>1969</td><td>logiciel de vol d’Apollo</td></tr>
<tr><td>Thompson et Ritchie</td><td>1969, 1972</td><td>Unix, langage C</td></tr>
<tr><td>Cerf et Kahn</td><td>1974</td><td>TCP/IP</td></tr>
<tr><td>Tim Berners-Lee</td><td>1989-1991</td><td>le Web</td></tr></table></div>
<h2>Logiciel et matériel</h2>
<p>Recâbler (1946) → charger un programme (1948) → langages et compilateurs (1957) → le logiciel devient un produit (1969) et l’essentiel de la valeur → virtualisation, nuage, matériels spécialisés (aujourd’hui).</p>`,
  predis: [
    { code: "hist-x1", niv: "facile", rep: "252 = 2 × 105 + 42, puis 105 = 2 × 42 + 21, puis 42 = 2 × 21 + 0 : trois divisions, PGCD 21." },
    { code: "hist-x2", niv: "moyen", rep: "101010 en binaire vaut 32 + 8 + 2 = 42. 1948 s’écrit 11110011100 en binaire : sept chiffres 1." },
    { code: "hist-x3", niv: "moyen", rep: "Le crible barre les multiples de 2, 3, 5 (à partir de leur carré) ; restent les nombres premiers jusqu’à 30." },
    { code: "hist-x4", niv: "facile", rep: "Après le tri par date : Turing (1936), ARPANET (1969), Web (1989), Linux (1991). On garde ceux de 1950 ou après, dans cet ordre." }
  ],
  ep: [
    { titre: "L’algorithme d’Euclide", enonce: `<p>L’algorithme d’Euclide repose sur la propriété : pgcd(<i>a</i>, <i>b</i>) = pgcd(<i>b</i>, <i>r</i>), où <i>r</i> est le reste de la division de <i>a</i> par <i>b</i>, et pgcd(<i>a</i>, 0) = <i>a</i>.</p>[[hist-ep1-fourni]]`,
      questions: [
        { q: "Écrire <code>pgcd_iter(a, b)</code> et <code>pgcd_rec(a, b)</code>.", c: `<p>Itératif : tant que <code>b != 0</code>, remplacer (<code>a</code>, <code>b</code>) par (<code>b</code>, <code>a % b</code>). Récursif : cas de base <code>b == 0</code> ; sinon <code>return pgcd_rec(b, a % b)</code>.</p>` },
        { q: "Écrire <code>nb_divisions(a, b)</code>, puis des tests qui comparent les deux versions entre elles et avec <code>math.gcd</code>.", c: `[[hist-ep1-corr]]` },
        { q: "Calculer <code>nb_divisions</code> pour deux nombres de Fibonacci consécutifs. Que constate-t-on ?", c: `<p>Pour F(21) = 10 946 et F(20) = 6 765, il faut 19 divisions : chaque reste est le nombre de Fibonacci précédent. Gabriel Lamé a montré en 1844 que c’est le pire cas : le nombre de divisions est au plus environ cinq fois le nombre de chiffres du plus petit nombre. L’algorithme est donc très rapide, même pour des nombres de centaines de chiffres (comme dans RSA).</p>` }
      ] },
    { titre: "Une frise chronologique", enonce: `<p>On représente des événements par des triplets (nom, année, catégorie).</p>[[hist-ep2-fourni]]`,
      questions: [
        { q: "Écrire <code>trier(frise)</code> sans modifier la liste reçue.", c: `<p><code>return sorted(frise, key=lambda e: e[1])</code> : <code>sorted</code> renvoie une nouvelle liste, contrairement à <code>frise.sort()</code>.</p>` },
        { q: "Écrire <code>par_decennie(frise)</code>, puis <code>premier_de(frise, categorie)</code> qui renvoie le nom de l’événement le plus ancien d’une catégorie (ou <code>None</code>). Écrire des tests.", c: `[[hist-ep2-corr]]` },
        { q: "À l’oral : situer chacun des événements de la frise dans l’évolution des rôles du matériel et du logiciel.", c: `<p>Le transistor et le microprocesseur rendent le matériel petit et bon marché ; Fortran puis Unix et Python montrent que l’effort se déplace vers le logiciel, portable d’une machine à l’autre ; TCP/IP relie des machines différentes par un protocole, c’est-à-dire du logiciel.</p>` }
      ] }
  ],
  ecrit: { titre: "Du recâblage au programme enregistré", points: "≈ 5 points · 35 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>« L’ENIAC (1946) pouvait calculer des milliers d’additions par seconde, mais changer de calcul demandait des jours. Avec la machine de Manchester (1948), il suffisait de charger un autre programme. » On s’intéresse à ce tournant.</p>`,
    questions: [
      { q: "Placer dans l’ordre chronologique, avec leur date : l’article de Turing sur les nombres calculables, le rapport de von Neumann sur l’EDVAC, le premier programme enregistré exécuté, l’invention du transistor.", pts: "1 pt", c: `<p>Turing (1936), von Neumann (1945), transistor (décembre 1947), Manchester Baby (juin 1948).</p>` },
      { q: "Qu’est-ce qu’une machine « à programme enregistré » ? Quels en sont les quatre éléments selon von Neumann ?", pts: "1,5 pt", c: `<p>Le programme est stocké dans la <b>mémoire</b>, au même titre que les données, au lieu d’être câblé. Éléments : unité arithmétique et logique (calcul), unité de contrôle (lit et décode les instructions une à une), mémoire (programme et données), entrées-sorties.</p>` },
      { q: "Expliquer le lien entre cette architecture et l’idée qu’« un programme est aussi une donnée ».", pts: "1 pt", c: `<p>Comme le programme est rangé en mémoire comme les données, un programme peut lire, écrire ou modifier un autre programme : c’est ce que font les compilateurs, les interpréteurs et les systèmes d’exploitation. C’est aussi l’idée de la machine universelle de Turing (1936), qui lit la description d’une autre machine sur son ruban.</p>` },
      { q: "Décrire en quelques lignes l’évolution des rôles relatifs du matériel et du logiciel depuis 1946, avec deux exemples datés.", pts: "1,5 pt", c: `<p>D’abord le matériel domine (ENIAC recâblé, 1946). Le programme enregistré (1948) puis les langages de haut niveau (Fortran, 1957) séparent le logiciel du matériel ; en 1969, IBM vend ses logiciels séparément. Avec le microprocesseur (1971) le matériel devient bon marché et le logiciel concentre la valeur ; aujourd’hui une machine peut même être un logiciel (virtualisation), tandis que des puces spécialisées (GPU, SoC) accélèrent certains logiciels.</p>` }
    ],
    methode: `<p>Une question d’histoire se traite comme une mini-argumentation : une date juste, un acteur, et surtout <b>ce que cela change</b>. « En 1948, la Baby de Manchester exécute le premier programme enregistré en mémoire : changer de calcul ne demande plus de modifier la machine. » vaut mieux qu’une liste de dates.</p>` },
  qcm: [
    { q: "D’où vient le mot « algorithme » ?", c: ["Du grec « algos » (douleur)", "Du nom du savant al-Khwarizmi (IXe siècle)", "D’un sigle anglais", "Du nom d’Ada Lovelace"], a: 1, e: "Son nom latinisé (Algoritmi) a donné le mot.", ref: "i1" },
    { q: "Qui a conçu une machine à calculer en 1642 ?", c: ["Leibniz", "Blaise Pascal", "Charles Babbage", "Alan Turing"], a: 1, e: "La Pascaline, à roues dentées, additionne et soustrait.", ref: "i2" },
    { q: "Qui a exposé l’arithmétique binaire en 1703 ?", c: ["Boole", "Leibniz", "Pascal", "Shannon"], a: 1, e: "Gottfried Wilhelm Leibniz.", ref: "i2" },
    { q: "Qui est considérée comme la première personne à avoir publié un programme (1843) ?", c: ["Grace Hopper", "Ada Lovelace", "Margaret Hamilton", "Marie Curie"], a: 1, e: "Ses notes sur la machine analytique de Babbage calculent les nombres de Bernoulli.", ref: "i2" },
    { q: "Que se passe-t-il en 1936 ?", c: ["Le premier ordinateur est construit", "Turing décrit la machine universelle", "Internet est créé", "Le transistor est inventé"], a: 1, e: "Article « On Computable Numbers… ».", ref: "i3" },
    { q: "Qui a fondé la théorie de l’information (1948) ?", c: ["Claude Shannon", "John von Neumann", "Alonzo Church", "Tim Berners-Lee"], a: 0, e: "Il popularise aussi le mot « bit ».", ref: "i3" },
    { q: "Comment programmait-on l’ENIAC ?", c: ["Avec un clavier et un écran", "En recâblant des panneaux et en réglant des interrupteurs", "Avec le langage Python", "En chargeant un programme en mémoire"], a: 1, e: "Changer de calcul pouvait prendre des jours.", ref: "i4" },
    { q: "Quelle machine exécute le premier programme enregistré en mémoire, le 21 juin 1948 ?", c: ["L’ENIAC", "La Baby de Manchester", "Le Z3", "L’IBM PC"], a: 1, e: "Small-Scale Experimental Machine de Williams, Kilburn et Tootill.", ref: "i4" },
    { q: "Que décrit l’architecture de von Neumann (1945) ?", c: ["Un réseau de machines", "Une machine dont le programme est enregistré en mémoire avec les données", "Un langage de programmation", "Une machine à cartes perforées"], a: 1, e: "Unité de calcul, unité de contrôle, mémoire, entrées-sorties.", ref: "i4" },
    { q: "Quel est le premier microprocesseur commercialisé (1971) ?", c: ["Intel 4004", "Micral N", "Apple II", "Z3"], a: 0, e: "2 300 transistors sur une puce.", ref: "i5" },
    { q: "Qui a dirigé l’écriture du logiciel de vol des missions Apollo ?", c: ["Grace Hopper", "Margaret Hamilton", "Ada Lovelace", "Barbara Liskov"], a: 1, e: "Margaret Hamilton, au MIT.", ref: "i6" },
    { q: "En quelle année Python est-il publié pour la première fois ?", c: ["1972", "1983", "1991", "2007"], a: 2, e: "Par Guido van Rossum, la même année que le noyau Linux.", ref: "i6" },
    { q: "Quel réseau, à l’origine d’Internet, relie ses premiers sites en 1969 ?", c: ["Le Web", "ARPANET", "Minitel", "Cyclades"], a: 1, e: "Premier message le 29 octobre 1969, entre UCLA et le SRI.", ref: "i7" },
    { q: "Qui a inventé le World Wide Web, et où ?", c: ["Vint Cerf, à l’UCLA", "Tim Berners-Lee, au CERN", "Bill Gates, chez Microsoft", "Louis Pouzin, à l’IRIA"], a: 1, e: "Proposition en 1989, premier site en 1991.", ref: "i7" },
    { q: "Que signifie la décision d’IBM, en 1969, de facturer ses logiciels à part ?", c: ["Que le matériel devient gratuit", "Que le logiciel devient un produit à part entière, distinct du matériel", "Que les logiciels deviennent libres", "Que les ordinateurs n’ont plus besoin de logiciels"], a: 1, e: "Une étape de l’évolution des rôles relatifs du logiciel et du matériel.", ref: "i8" }
  ],
  cartes: [
    { r: "Euclide, vers −300", v: "Algorithme du PGCD dans les Éléments : pgcd(a, b) = pgcd(b, a mod b)." },
    { r: "al-Khwarizmi", v: "Savant persan, Bagdad, IXe siècle (vers 825). Son nom a donné « algorithme »." },
    { r: "1642", v: "Pascaline de Blaise Pascal : machine à additionner à roues dentées." },
    { r: "Leibniz", v: "Machine à multiplier (1673) ; arithmétique binaire (1703)." },
    { r: "1801", v: "Métier à tisser de Jacquard, piloté par des cartes perforées." },
    { r: "Babbage et Ada Lovelace", v: "Machine analytique (conçue à partir de 1834, jamais construite) ; notes de Lovelace, premier programme publié (1843)." },
    { r: "George Boole, 1854", v: "Algèbre de la logique à deux valeurs : base des circuits logiques." },
    { r: "1936", v: "Turing (machine universelle, indécidabilité) et Church (lambda-calcul)." },
    { r: "1945", v: "Rapport de von Neumann sur l’EDVAC : programme enregistré en mémoire avec les données." },
    { r: "21 juin 1948", v: "La Baby de Manchester exécute le premier programme enregistré en mémoire." },
    { r: "1947 / 1958 / 1971", v: "Transistor (Bell) / circuit intégré (Kilby) / microprocesseur Intel 4004." },
    { r: "Grace Hopper", v: "Compilateur A-0 (1952), inspiratrice de COBOL ; le « bug » du Mark II (1947)." },
    { r: "1969", v: "ARPANET (premier message le 29 octobre), Unix, logiciel d’Apollo (Margaret Hamilton)." },
    { r: "TCP/IP", v: "Décrit par Cerf et Kahn (1974), adopté par ARPANET le 1er janvier 1983." },
    { r: "Le Web", v: "Tim Berners-Lee, CERN : proposition 1989, premier site 1991, domaine public 1993." },
    { r: "Rôles du logiciel et du matériel", v: "Recâbler (ENIAC) → programme enregistré (1948) → langages, logiciel vendu à part (1969) → le logiciel concentre la valeur → virtualisation et matériels spécialisés." }
  ]
});
