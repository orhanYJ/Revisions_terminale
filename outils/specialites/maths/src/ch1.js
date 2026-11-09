/* ---------- Chapitre 1 : raisonnement par récurrence ---------- */
var R = String.raw;
var CH1 = {
  id: "ch1", num: 1, statut: "ok", partie: "Analyse", titre: "Raisonnement par récurrence", court: "Récurrence",
  sous: "Démontrer qu'une propriété est vraie pour une infinité d'entiers, en deux étapes.",
  resume: "Initialisation, hérédité, rédaction ; formules, inégalités, suites bornées et monotones.",
  essentiel: [
    R`Pour prouver qu'une propriété $P(n)$ est vraie <b>pour tout entier</b> $n\geq n_0$, on prouve deux choses : $P(n_0)$ est vraie (<b>initialisation</b>) et, pour tout $k\geq n_0$, si $P(k)$ est vraie alors $P(k+1)$ l'est aussi (<b>hérédité</b>).`,
    R`C'est l'image des dominos : le premier tombe, et chacun fait tomber le suivant, donc tous tombent.`,
    R`Dans l'hérédité, on <b>suppose</b> $P(k)$ pour un entier $k$ fixé et on doit <b>utiliser</b> cette hypothèse pour obtenir $P(k+1)$.`,
    R`Trois usages au bac : établir une formule explicite $u_n=\dots$, encadrer une suite ($a\leq u_n\leq b$), montrer qu'elle est monotone ($u_n\leq u_{n+1}$).`,
    R`Vérifier la propriété pour beaucoup de valeurs de $n$ ne prouve rien : $n^2+n+41$ est premier pour $n=0,\dots,39$, mais pas pour $n=40$.`
  ],
  attendus: [
    R`Démontrer une propriété par récurrence (programme : vocabulaire ensembliste et logique).`,
    R`Raisonner par récurrence pour établir une propriété d'une suite (programme : suites).`,
    R`Démontrer par récurrence l'inégalité de Bernoulli, utilisée ensuite pour la limite de $(q^n)$ <span class="tag bo">démonstration exigible</span>.`,
    R`Étudier des phénomènes d'évolution modélisables par une suite.`
  ],
  premiere: R`
<h3>Suites arithmétiques et géométriques</h3>
<div class="tab-wrap"><table><tr><th></th><th>Arithmétique de raison $r$</th><th>Géométrique de raison $q$</th></tr>
<tr><td>Récurrence</td><td>$u_{n+1}=u_n+r$</td><td>$u_{n+1}=q\,u_n$</td></tr>
<tr><td>Terme général</td><td>$u_n=u_0+nr$<br>$u_n=u_p+(n-p)r$</td><td>$u_n=u_0\,q^n$<br>$u_n=u_p\,q^{n-p}$</td></tr>
<tr><td>Somme</td><td>$1+2+\dots+n=\frac{n(n+1)}{2}$</td><td>$1+q+\dots+q^n=\frac{1-q^{n+1}}{1-q}$ si $q\neq1$</td></tr></table></div>
<p>Somme de termes consécutifs d'une suite arithmétique : $\text{(nombre de termes)}\times\frac{\text{premier}+\text{dernier}}{2}$. D'une suite géométrique : $\text{premier}\times\frac{1-q^{\text{nombre de termes}}}{1-q}$.</p>
<h3>Sens de variation</h3>
<ul><li>On étudie le signe de $u_{n+1}-u_n$ : positif pour tout $n$ ⟹ suite croissante.</li>
<li>Si tous les termes sont strictement positifs, on peut comparer $\frac{u_{n+1}}{u_n}$ à $1$.</li>
<li>Si $u_n=f(n)$ avec $f$ croissante sur $[0;+\infty[$, alors $(u_n)$ est croissante.</li>
<li>Une suite géométrique $u_n=u_0q^n$ avec $u_0>0$ est croissante si $q>1$, décroissante si $0<q<1$.</li></ul>
[piege|Ne pas confondre]Si $u_{n+1}=f(u_n)$, le sens de variation de $f$ <b>ne donne pas</b> directement celui de $(u_n)$. Exemple : $f(x)=0{,}5x+2$ est croissante, mais avec $u_0=10$ la suite décroît ($10$ ; $7$ ; $5{,}5$…). C'est justement là que la récurrence sert (partie 4).[/]`,
  cours: [
    { id: "principe", titre: "Le principe : initialisation et hérédité", html: R`
<p>On veut démontrer qu'une propriété dépendant d'un entier $n$ est vraie pour <b>tous</b> les entiers à partir d'un rang $n_0$ : une infinité de cas. Impossible de tous les vérifier. L'idée de la récurrence : montrer qu'on peut passer de n'importe quel cas au suivant.</p>
[thm|Principe de récurrence]Soit $P(n)$ une propriété définie pour tout entier $n\geq n_0$. Si :
<ul><li><b>Initialisation</b> : $P(n_0)$ est vraie ;</li><li><b>Hérédité</b> : pour tout entier $k\geq n_0$, si $P(k)$ est vraie, alors $P(k+1)$ est vraie ;</li></ul>
alors $P(n)$ est vraie pour tout entier $n\geq n_0$.[/]
<div data-w="dominos"></div>
<p><b>Pourquoi ça marche ?</b> $P(n_0)$ est vraie ; l'hérédité appliquée à $k=n_0$ donne $P(n_0+1)$ ; appliquée à $k=n_0+1$, elle donne $P(n_0+2)$… On atteint ainsi n'importe quel entier en un nombre fini d'étapes. C'est une propriété fondamentale de l'ensemble $\N$ : on l'admet (en mathématiques, c'est un axiome).</p>
[ex|Les deux étapes sont indispensables]
<ul><li><b>Hérédité sans initialisation</b>. $P(n)$ : « $2^n$ est divisible par $3$ ». Si $2^k=3m$, alors $2^{k+1}=2\times3m=3\times(2m)$ : l'hérédité est vraie ! Mais $P(0)$ est fausse ($2^0=1$), et en fait $P(n)$ n'est jamais vraie.</li>
<li><b>Initialisation sans hérédité</b>. $n^2+n+41$ est un nombre premier pour $n=0,1,\dots,39$. Mais pour $n=40$ : $40^2+40+41=1681=41^2$, qui n'est pas premier. Quarante vérifications ne font pas une preuve.</li></ul>[/]
[hist|Une idée ancienne]Le programme le rappelle : le raisonnement par récurrence a été formalisé par Pascal, puis surtout par Peano et ses collaborateurs à la fin du XIX<sup>e</sup> siècle ; on en trouve des anticipations chez al-Karaji, As-Samaw'al, Fibonacci et Maurolico.[/]` },
    { id: "rediger", titre: "Rédiger une récurrence : le modèle", html: R`
<p>Au bac, la rédaction compte : le correcteur cherche les quatre étapes. Voici un modèle à reproduire.</p>
[ex|Une formule explicite]Soit $(u_n)$ définie par $u_0=1$ et $u_{n+1}=2u_n+3$. Montrons que pour tout $n\in\N$, $u_n=2^{n+2}-3$.
<p><b>Propriété.</b> Pour tout $n\in\N$, on note $P(n)$ : « $u_n=2^{n+2}-3$ ».</p>
<p><b>Initialisation.</b> Pour $n=0$ : $u_0=1$ et $2^{0+2}-3=4-3=1$. Donc $P(0)$ est vraie.</p>
<p><b>Hérédité.</b> Soit $k\in\N$. On suppose que $P(k)$ est vraie, c'est-à-dire $u_k=2^{k+2}-3$ (<span class="stylo">hypothèse de récurrence</span>). Montrons $P(k+1)$ : « $u_{k+1}=2^{k+3}-3$ ».
$$u_{k+1}=2u_k+3=2\left(2^{k+2}-3\right)+3=2^{k+3}-6+3=2^{k+3}-3.$$
Donc $P(k+1)$ est vraie.</p>
<p><b>Conclusion.</b> $P(0)$ est vraie et la propriété est héréditaire ; par récurrence, pour tout $n\in\N$, $u_n=2^{n+2}-3$.</p>[/]
[meth|Les quatre réflexes]
<ol><li>Écrire $P(n)$ en toutes lettres, avec des guillemets.</li>
<li>Initialisation : calculer <b>séparément</b> les deux membres au rang $n_0$.</li>
<li>Hérédité : « Soit $k\geq n_0$ ; supposons $P(k)$ » puis écrire <b>le but</b> $P(k+1)$. Partir de $u_{k+1}$, utiliser la définition de la suite, puis l'hypothèse de récurrence.</li>
<li>Conclure en citant initialisation, hérédité et le principe de récurrence.</li></ol>[/]
<p>On peut écrire $n$ au lieu de $k$ dans l'hérédité (« soit $n$ un entier tel que $P(n)$ est vraie »), à condition de bien dire que $n$ est <b>fixé</b>. Écrire « supposons $P(n)$ vraie pour tout $n$ » serait supposer ce qu'on veut démontrer.</p>` },
    { id: "sommes", titre: "Récurrence et sommes", html: R`
<p>Les formules de sommes sont des cas d'école : passer du rang $k$ au rang $k+1$, c'est <b>ajouter un terme</b>.</p>
[ex|La somme des premiers nombres impairs]Montrons que pour tout $n\geq1$ : $1+3+5+\dots+(2n-1)=n^2$.
<p><b>Initialisation.</b> Pour $n=1$, la somme vaut $1$ et $1^2=1$.</p>
<p><b>Hérédité.</b> Soit $k\geq1$ tel que $1+3+\dots+(2k-1)=k^2$. Au rang $k+1$, on ajoute le terme suivant $2(k+1)-1=2k+1$ :
$$1+3+\dots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2.$$</p>
<p><b>Conclusion.</b> Par récurrence, la formule est vraie pour tout $n\geq1$.</p>[/]
<p>Avec le symbole somme, on écrit $\sum_{k=1}^{n}(2k-1)=n^2$. Le programme permet d'utiliser ce symbole pour abréger, mais sa manipulation pour démontrer des égalités n'est pas un objectif : en cas de doute, écris la somme avec des pointillés.</p>
[prop|Somme des carrés]Pour tout $n\geq1$ : $1^2+2^2+\dots+n^2=\frac{n(n+1)(2n+1)}{6}$. (Démonstration dans l'onglet Démonstrations.)[/]` },
    { id: "inegalites", titre: "Récurrence et inégalités : encadrer, montrer la monotonie", html: R`
<p>C'est l'usage le plus fréquent au bac : la suite est définie par $u_{n+1}=f(u_n)$ et on demande de montrer, par exemple, $0\leq u_n\leq u_{n+1}\leq2$. L'outil clé est la <b>croissance de $f$</b> : une fonction croissante conserve l'ordre.</p>
[prop|Fonction croissante et inégalités]Si $f$ est croissante sur un intervalle $I$ et si $a\leq b$ sont dans $I$, alors $f(a)\leq f(b)$. On « applique $f$ » à une inégalité sans changer son sens.[/]
[ex|Une suite bornée et croissante]Soit $u_0=1$ et $u_{n+1}=\sqrt{u_n+2}$. Montrons que pour tout $n\in\N$ : $0\leq u_n\leq u_{n+1}\leq2$.
<p>On note $f(x)=\sqrt{x+2}$, définie et croissante sur $[-2;+\infty[$ (composée de $x\mapsto x+2$ et de la racine, toutes deux croissantes).</p>
<p><b>Initialisation.</b> $u_0=1$, $u_1=\sqrt3\approx1{,}73$ : on a bien $0\leq1\leq\sqrt3\leq2$.</p>
<p><b>Hérédité.</b> Soit $k\in\N$ tel que $0\leq u_k\leq u_{k+1}\leq2$. Comme $f$ est croissante sur $[0;2]$ :
$$f(0)\leq f(u_k)\leq f(u_{k+1})\leq f(2),$$ soit $$\sqrt2\leq u_{k+1}\leq u_{k+2}\leq2.$$
Comme $0\leq\sqrt2$, on obtient $0\leq u_{k+1}\leq u_{k+2}\leq2$ : c'est $P(k+1)$.</p>
<p><b>Conclusion.</b> Pour tout $n$, $0\leq u_n\leq u_{n+1}\leq2$ : la suite est croissante et majorée par $2$ (on verra au chapitre 2 qu'elle converge, ici vers $2$).</p>[/]
<div data-w="toile"></div>
[thm|Inégalité de Bernoulli]Pour tout réel $a\geq0$ et tout entier $n\in\N$ : $$(1+a)^n\geq1+na.$$[/]
<p>Elle est démontrée par récurrence dans l'onglet <b>Démonstrations</b> (démonstration exigible). Elle dit que $(1+a)^n$ grandit au moins comme une suite arithmétique : par exemple $1{,}05^{20}\geq1+20\times0{,}05=2$ (en réalité $1{,}05^{20}\approx2{,}65$). C'est la clé de la limite de $q^n$ quand $q>1$ (chapitre 2).</p>
[meth|Encadrer sans croissance de $f$]Si $f$ n'est pas monotone, on travaille directement sur l'expression : par exemple pour $u_{k+1}=0{,}5u_k+1$ et l'hypothèse $u_k\leq2$, on multiplie par $0{,}5>0$ puis on ajoute $1$ : $u_{k+1}\leq0{,}5\times2+1=2$.[/]` },
    { id: "limites", titre: "Ce que la récurrence ne fait pas", html: R`
<ul><li>Elle ne <b>trouve</b> pas la formule : il faut la deviner (calcul des premiers termes, tableur, Python) ou qu'elle soit donnée par l'énoncé. Elle sert à la <b>prouver</b>.</li>
<li>Elle ne s'applique qu'à des propriétés indexées par des <b>entiers</b>. Pour un réel $x$, on utilise d'autres outils (étude de fonction, convexité au chapitre 4).</li>
<li>Pour montrer qu'une propriété est fausse, un seul <b>contre-exemple</b> suffit : pas besoin de récurrence.</li></ul>
[ex|Deviner, puis prouver]Avec $u_0=0$ et $u_{n+1}=u_n+2n+1$, les premiers termes sont $0, 1, 4, 9, 16$ : on conjecture $u_n=n^2$. Hérédité : si $u_k=k^2$, alors $u_{k+1}=k^2+2k+1=(k+1)^2$.[/]
<p><span class="tag hp">Pour aller plus loin</span> Il existe des variantes (récurrence « forte », où l'on suppose $P(n_0),\dots,P(k)$ pour prouver $P(k+1)$ ; récurrence à deux pas pour les suites $u_{n+2}=au_{n+1}+bu_n$). Elles ne sont pas exigibles.</p>` }
  ],
  pieges: [
    { t: "Supposer ce qu'on veut démontrer", h: R`Écrire dans l'hérédité « supposons que $P(n)$ est vraie pour tout $n$ ». On suppose $P(k)$ pour <b>un</b> entier $k$ fixé.` },
    { t: "L'hérédité qui n'utilise pas l'hypothèse", h: R`Si ton calcul de $P(k+1)$ n'utilise jamais $P(k)$, ce n'est pas une récurrence (soit une preuve directe était possible, soit il y a une erreur).` },
    { t: "Oublier l'initialisation", h: R`Sans elle, on peut « démontrer » des choses fausses (voir « $2^n$ divisible par $3$ »). Elle rapporte des points même si elle est facile : écris-la.` },
    { t: "Le mauvais rang de départ", h: R`$2^n\geq n^2$ est faux pour $n=3$ ($8<9$) et vrai pour $n\geq4$ : on initialise à $n_0=4$, pas à $0$.` },
    { t: "Inégalité multipliée par un négatif", h: R`Dans l'hérédité, multiplier par un nombre négatif <b>renverse</b> l'inégalité ; appliquer une fonction <b>décroissante</b> aussi.` },
    { t: "Confondre $u_{k+1}$ et $u_k+1$", h: R`$u_{k+1}$ est le terme de rang $k+1$ ; $u_k+1$ est le terme de rang $k$ augmenté de $1$.` }
  ],
  demos: [
    { bo: true, t: R`Inégalité de Bernoulli : $(1+a)^n\geq1+na$ pour $a\geq0$`, h: R`
<p>Soit $a$ un réel positif. Pour $n\in\N$, on note $P(n)$ : « $(1+a)^n\geq1+na$ ».</p>
<p><b>Initialisation.</b> $(1+a)^0=1$ et $1+0\times a=1$ : $1\geq1$, donc $P(0)$ est vraie.</p>
<p><b>Hérédité.</b> Soit $k\in\N$ tel que $(1+a)^k\geq1+ka$. Comme $1+a>0$, on peut multiplier les deux membres par $1+a$ sans changer le sens :
$$(1+a)^{k+1}\geq(1+ka)(1+a)=1+a+ka+ka^2=1+(k+1)a+ka^2.$$
Or $ka^2\geq0$, donc $1+(k+1)a+ka^2\geq1+(k+1)a$. Finalement $(1+a)^{k+1}\geq1+(k+1)a$ : $P(k+1)$ est vraie.</p>
<p><b>Conclusion.</b> Par récurrence, pour tout $n\in\N$, $(1+a)^n\geq1+na$.</p>
<p class="stylo">Le point délicat : justifier qu'on multiplie par un nombre positif ($1+a>0$).</p>
<p><span class="tag hp">Pour aller plus loin</span> La même preuve marche pour $a\geq-1$ (car alors $1+a\geq0$).</p>` },
    { bo: false, t: R`Somme des entiers : $1+2+\dots+n=\frac{n(n+1)}{2}$`, h: R`
<p>$P(n)$ : « $1+2+\dots+n=\frac{n(n+1)}{2}$ », pour $n\geq1$. Initialisation : $1=\frac{1\times2}{2}$.</p>
<p>Hérédité : si $1+\dots+k=\frac{k(k+1)}{2}$, alors
$$1+\dots+k+(k+1)=\frac{k(k+1)}{2}+(k+1)=\frac{(k+1)(k+2)}{2}.$$
C'est $P(k+1)$. Conclusion par récurrence.</p>
<p><i>Autre preuve (Gauss)</i> : on écrit la somme à l'endroit et à l'envers, et on additionne : $2S=n(n+1)$.</p>` },
    { bo: false, t: R`Somme des carrés : $1^2+\dots+n^2=\frac{n(n+1)(2n+1)}{6}$`, h: R`
<p>Initialisation ($n=1$) : $1=\frac{1\times2\times3}{6}$.</p>
<p>Hérédité : si $1^2+\dots+k^2=\frac{k(k+1)(2k+1)}{6}$, alors
$$1^2+\dots+k^2+(k+1)^2=\frac{k(k+1)(2k+1)}{6}+(k+1)^2=\frac{(k+1)\left[k(2k+1)+6(k+1)\right]}{6}=\frac{(k+1)(2k^2+7k+6)}{6}.$$
Or $(k+2)(2k+3)=2k^2+7k+6$, donc la somme vaut $\frac{(k+1)(k+2)(2k+3)}{6}$, c'est-à-dire la formule au rang $k+1$ (car $2(k+1)+1=2k+3$).</p>
<p class="stylo">Astuce : factoriser par $(k+1)$ tout de suite, au lieu de tout développer.</p>` },
    { bo: false, t: R`$4^n-1$ est divisible par $3$ pour tout $n\in\N$`, h: R`
<p>Initialisation : $4^0-1=0=3\times0$.</p>
<p>Hérédité : si $4^k-1=3m$ avec $m$ entier, alors $4^{k+1}-1=4\times4^k-1=4(3m+1)-1=12m+3=3(4m+1)$, multiple de $3$.</p>
<p>Conclusion par récurrence. (On peut aussi remarquer que $4\equiv1$ modulo $3$, notion de l'option maths expertes.)</p>` }
  ],
  algos: [
    { t: "Calculer les termes et tester une conjecture", avant: R`<p>Python calcule vite les premiers termes : utile pour <b>conjecturer</b> une formule. Mais un test sur 30 valeurs n'est pas une preuve.</p>`,
      code: `def termes(n):
    u = 1                      # u0
    L = [u]
    for k in range(n):
        u = 2 * u + 3          # u(k+1) = 2 u(k) + 3
        L.append(u)
    return L

L = termes(6)
print(L)
print([2**(k + 2) - 3 for k in range(7)])`,
      sortie: `[1, 5, 13, 29, 61, 125, 253]
[1, 5, 13, 29, 61, 125, 253]`,
      apres: R`<p>Les deux listes coïncident : on conjecture $u_n=2^{n+2}-3$, puis on le <b>démontre</b> par récurrence (partie 2 du cours).</p>` },
    { t: "Le piège d'Euler : vrai 40 fois, puis faux", avant: R`<p>On cherche le premier entier $n$ pour lequel $n^2+n+41$ n'est pas premier.</p>`,
      code: `def est_premier(p):
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d = d + 1
    return True

n = 0
while est_premier(n**2 + n + 41):
    n = n + 1
print(n, n**2 + n + 41)`,
      sortie: `40 1681`,
      apres: R`<p>$1681=41\times41$. Une boucle <code>while</code> qui « cherche le premier rang où… » est exactement la structure des algorithmes de <b>seuil</b> du chapitre 2.</p>` },
    { t: "Vérifier une somme", code: `n = 10
S = 0
for k in range(1, n + 1):
    S = S + (2 * k - 1)       # on ajoute le k-ième impair
print(S, n**2)`, sortie: `100 100` }
  ],
  methodes: [
    { t: "Comment montrer que $u_n=$ (une formule) ?", h: R`
<ol><li>Initialisation : calcule $u_{n_0}$ avec la définition et avec la formule.</li><li>Hérédité : écris $u_{k+1}$ avec la relation de récurrence, <b>remplace</b> $u_k$ par la formule (hypothèse), simplifie jusqu'à la formule au rang $k+1$.</li><li>Écris le but au rang $k+1$ avant de calculer : tu sais où aller.</li></ol>` },
    { t: "Comment montrer que $a\\leq u_n\\leq b$ ?", h: R`
<ol><li>Si $u_{n+1}=f(u_n)$ avec $f$ croissante sur $[a;b]$ : de $a\leq u_k\leq b$ on tire $f(a)\leq u_{k+1}\leq f(b)$, puis on compare $f(a)$ à $a$ et $f(b)$ à $b$.</li><li>Si $f$ est affine $f(x)=mx+p$ avec $m>0$ : on multiplie par $m$, puis on ajoute $p$, étape par étape.</li><li>Vérifie l'hypothèse de croissance <b>sur le bon intervalle</b> : celui où se trouvent les termes.</li></ol>` },
    { t: "Comment montrer que $(u_n)$ est monotone par récurrence ?", h: R`
<p>Montre $P(n)$ : « $u_n\leq u_{n+1}$ » (croissante) ou « $u_{n+1}\leq u_n$ » (décroissante). Si $f$ est croissante, l'inégalité se « propage » : $u_k\leq u_{k+1}\Rightarrow f(u_k)\leq f(u_{k+1})$, soit $u_{k+1}\leq u_{k+2}$. On combine souvent : « $a\leq u_n\leq u_{n+1}\leq b$ » en une seule récurrence.</p>
[piege|Ne pas mélanger]Si $f$ est décroissante, l'ordre s'inverse à chaque étape : la suite n'est en général pas monotone (elle « oscille »). Exemple : $f(x)=1+\frac1x$ (essaie le nombre d'or dans la toile d'araignée).[/]` },
    { t: "Comment écrire une inégalité de puissances ($2^n\\geq n^2$…) ?", h: R`
<p>Dans l'hérédité, on part de $2^{k+1}=2\times2^k\geq2k^2$ (hypothèse) puis on montre $2k^2\geq(k+1)^2$, ce qui revient à $k^2-2k-1\geq0$, vrai pour $k\geq3$. On combine : $2^{k+1}\geq2k^2\geq(k+1)^2$. Chaîne d'inégalités : c'est le schéma standard.</p>` }
  ],
  exos: [
    { niv: 1, t: "Une formule à démontrer", enonce: R`<p>Soit $(u_n)$ définie par $u_0=2$ et, pour tout $n\in\N$, $u_{n+1}=u_n+2n+3$.</p><ol><li>Calculer $u_1$, $u_2$, $u_3$.</li><li>Démontrer par récurrence que pour tout $n\in\N$, $u_n=(n+1)^2+1$.</li><li>En déduire $u_{10}$.</li></ol>`,
      corrige: R`<ol><li>$u_1=2+0+3=5$ ; $u_2=5+2+3=10$ ; $u_3=10+4+3=17$.</li>
<li>$P(n)$ : « $u_n=(n+1)^2+1$ ». <b>Initialisation</b> : $(0+1)^2+1=2=u_0$. <b>Hérédité</b> : soit $k\in\N$ tel que $u_k=(k+1)^2+1$. Alors
$$u_{k+1}=u_k+2k+3=(k+1)^2+1+2k+3=k^2+4k+5=(k+2)^2+1,$$ c'est $P(k+1)$. <b>Conclusion</b> : par récurrence, $u_n=(n+1)^2+1$ pour tout $n$.</li>
<li>$u_{10}=11^2+1=122$.</li></ol>` },
    { niv: 1, t: "Une somme", enonce: R`<p>Démontrer que pour tout entier $n\geq1$ : $1\times2+2\times3+\dots+n(n+1)=\frac{n(n+1)(n+2)}{3}$.</p>`,
      corrige: R`<p><b>Initialisation</b> ($n=1$) : $1\times2=2$ et $\frac{1\times2\times3}{3}=2$.</p>
<p><b>Hérédité</b> : soit $k\geq1$ tel que $1\times2+\dots+k(k+1)=\frac{k(k+1)(k+2)}{3}$. On ajoute le terme $(k+1)(k+2)$ :
$$\frac{k(k+1)(k+2)}{3}+(k+1)(k+2)=(k+1)(k+2)\left(\frac{k}{3}+1\right)=\frac{(k+1)(k+2)(k+3)}{3}.$$
C'est la formule au rang $k+1$. <b>Conclusion</b> par récurrence. Vérification : pour $n=3$, $2+6+12=20=\frac{3\times4\times5}{3}$.</p>` },
    { niv: 2, t: "Encadrement et monotonie", enonce: R`<p>Soit $u_0=0$ et $u_{n+1}=\sqrt{3u_n+4}$ pour tout $n\in\N$.</p><ol><li>Soit $f(x)=\sqrt{3x+4}$ sur $\left[-\frac43;+\infty\right[$. Justifier que $f$ est croissante.</li><li>Démontrer par récurrence que pour tout $n$ : $0\leq u_n\leq u_{n+1}\leq4$.</li><li>Que peut-on en dire de la suite ?</li></ol>`,
      corrige: R`<ol><li>$x\mapsto3x+4$ est croissante et positive sur l'intervalle, la racine carrée est croissante sur $[0;+\infty[$ : par composition, $f$ est croissante. (On peut aussi dériver : $f'(x)=\frac{3}{2\sqrt{3x+4}}>0$ pour $x>-\frac43$.)</li>
<li><b>Initialisation</b> : $u_0=0$, $u_1=\sqrt4=2$ et $0\leq0\leq2\leq4$. <b>Hérédité</b> : si $0\leq u_k\leq u_{k+1}\leq4$, la croissance de $f$ sur $[0;4]$ donne $f(0)\leq f(u_k)\leq f(u_{k+1})\leq f(4)$, soit $2\leq u_{k+1}\leq u_{k+2}\leq4$ (car $f(4)=\sqrt{16}=4$), donc $0\leq u_{k+1}\leq u_{k+2}\leq4$. <b>Conclusion</b> par récurrence.</li>
<li>Elle est croissante et majorée par $4$. Au chapitre 2 : elle converge, vers la solution positive de $\ell=\sqrt{3\ell+4}$, soit $\ell^2-3\ell-4=0$, $\ell=4$. Valeurs : $u_2\approx3{,}162$, $u_5\approx3{,}953$, $u_{10}\approx3{,}9996$.</li></ol>` },
    { niv: 2, t: "Puissances contre carrés", enonce: R`<ol><li>Comparer $2^n$ et $n^2$ pour $n=0,1,\dots,6$.</li><li>Démontrer que pour tout entier $n\geq4$, $2^n\geq n^2$.</li></ol>`,
      corrige: R`<ol><li>$n=0$ : $1>0$ ; $n=1$ : $2>1$ ; $n=2$ : $4=4$ ; $n=3$ : $8<9$ ; $n=4$ : $16=16$ ; $n=5$ : $32>25$ ; $n=6$ : $64>36$. La propriété est fausse pour $n=3$.</li>
<li><b>Initialisation</b> à $n_0=4$ : $16\geq16$. <b>Hérédité</b> : soit $k\geq4$ tel que $2^k\geq k^2$. Alors $2^{k+1}=2\times2^k\geq2k^2$. Il reste à montrer $2k^2\geq(k+1)^2$, c'est-à-dire $k^2-2k-1\geq0$. Or $k^2-2k-1=(k-1)^2-2$ et pour $k\geq4$, $(k-1)^2\geq9>2$. Donc $2^{k+1}\geq2k^2\geq(k+1)^2$. <b>Conclusion</b> : pour tout $n\geq4$, $2^n\geq n^2$.</li></ol>` },
    { niv: 3, t: "Abonnés d'une chaîne (type bac)", enonce: R`<p>Une chaîne de vidéos compte $5$ milliers d'abonnés au départ. Chaque mois, elle perd $20\,\%$ de ses abonnés mais en gagne $3$ milliers. On note $a_n$ le nombre d'abonnés, en milliers, après $n$ mois : $a_0=5$ et $a_{n+1}=0{,}8a_n+3$.</p>
<ol><li>Calculer $a_1$ et $a_2$.</li><li>Démontrer par récurrence que pour tout $n\in\N$ : $5\leq a_n\leq a_{n+1}\leq15$.</li><li>On pose $v_n=a_n-15$. Montrer que $(v_n)$ est géométrique, puis que $a_n=15-10\times0{,}8^n$.</li><li>Recopier et compléter la fonction Python pour qu'elle renvoie le premier mois où la chaîne dépasse $14$ milliers d'abonnés, puis donner ce mois.</li></ol>
[py]
def seuil():
    n = 0
    a = 5
    while ...:
        a = ...
        n = n + 1
    return n
[/py]`,
      corrige: R`<ol><li>$a_1=0{,}8\times5+3=7$ ; $a_2=0{,}8\times7+3=8{,}6$.</li>
<li>Soit $f(x)=0{,}8x+3$, croissante sur $\R$ (coefficient $0{,}8>0$). <b>Initialisation</b> : $a_0=5$, $a_1=7$, et $5\leq5\leq7\leq15$. <b>Hérédité</b> : si $5\leq a_k\leq a_{k+1}\leq15$, alors $f(5)\leq f(a_k)\leq f(a_{k+1})\leq f(15)$, soit $7\leq a_{k+1}\leq a_{k+2}\leq15$, d'où $5\leq a_{k+1}\leq a_{k+2}\leq15$. <b>Conclusion</b> par récurrence.</li>
<li>$v_{n+1}=a_{n+1}-15=0{,}8a_n-12=0{,}8(a_n-15)=0{,}8v_n$ : géométrique de raison $0{,}8$, de premier terme $v_0=-10$. Donc $v_n=-10\times0{,}8^n$ et $a_n=15-10\times0{,}8^n$.</li>
<li>Condition de boucle : <code>a &lt;= 14</code> ; mise à jour : <code>a = 0.8 * a + 3</code>. La fonction renvoie $11$ : $a_{10}\approx13{,}93$ et $a_{11}\approx14{,}14$ (car $0{,}8^{10}\approx0{,}107$ et $0{,}8^{11}\approx0{,}086$). La chaîne dépasse $14$ milliers au bout de $11$ mois.</li></ol>
<p class="stylo">Méthode bac : la question 2 se rédige comme le modèle du cours ; la question 3 est la technique de Première « suite auxiliaire ».</p>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole, 17 juin 2026 (sujet 2), exercice 2, partie A", url: "https://www.apmep.fr/IMG/pdf/BAC_generale_specialite_J2_2026-06-17_Metropole_FK-v4.pdf", h: R`Pollution d'un bassin : $V_{n+1}=0{,}995V_n+6$, $V_0=0$. Programme Python à compléter, puis « montrer par récurrence que $V_n\leq V_{n+1}\leq1200$ », puis convergence et limite.` },
    { ref: "Bac 2026, Métropole, 16 juin 2026 (sujet 1), exercice 3, partie B", url: "https://www.apmep.fr/IMG/pdf/BAC_General_Specialite_Sujet_J1_metropole_FK-v2.pdf", h: R`Refroidissement d'une pièce : $u_{n+1}=0{,}965u_n+0{,}35+0{,}07\,\e^{-0{,}1n}$. Montrer par récurrence que $u_n>10$, puis la convergence.` },
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 4, partie A", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Posidonie : $u_{n+1}=-0{,}02u_n^2+1{,}3u_n$, $u_0=1$. Démontrer que $1\leq u_n\leq u_{n+1}\leq20$ (avec $h$ croissante), puis convergence, limite $15$ et algorithme de seuil. Cette suite est dans la toile d'araignée du cours.` }
  ],
  retenir: R`
[thm|Principe de récurrence]Si $P(n_0)$ est vraie et si, pour tout $k\geq n_0$, $P(k)\Rightarrow P(k+1)$, alors $P(n)$ est vraie pour tout $n\geq n_0$.[/]
<h3>Rédaction type</h3>
<ol><li><b>Propriété</b> : « Pour $n\geq n_0$, on note $P(n)$ : … »</li><li><b>Initialisation</b> : vérifier $P(n_0)$ (calculer les deux membres).</li><li><b>Hérédité</b> : « Soit $k\geq n_0$ tel que $P(k)$ est vraie. Montrons $P(k+1)$. » Utiliser la définition de la suite <b>et</b> l'hypothèse.</li><li><b>Conclusion</b> : « Par récurrence, $P(n)$ est vraie pour tout $n\geq n_0$. »</li></ol>
<h3>Outils</h3>
<ul><li>Si $f$ est croissante sur $I$ : $a\leq b\Rightarrow f(a)\leq f(b)$ (on « passe » l'inégalité de $u_k$ à $u_{k+1}$).</li><li>Multiplier par un négatif ou appliquer une fonction décroissante renverse l'inégalité.</li><li>Bernoulli : $(1+a)^n\geq1+na$ pour $a\geq0$ (démonstration exigible).</li></ul>
<h3>Formules utiles</h3>
<ul><li>$1+2+\dots+n=\frac{n(n+1)}{2}$ ; $1+3+\dots+(2n-1)=n^2$ ; $1^2+\dots+n^2=\frac{n(n+1)(2n+1)}{6}$.</li><li>Arithmétique : $u_n=u_0+nr$. Géométrique : $u_n=u_0q^n$ ; $1+q+\dots+q^n=\frac{1-q^{n+1}}{1-q}$ ($q\neq1$).</li></ul>
<p class="stylo">Un exemple ne prouve rien ; un contre-exemple suffit à réfuter.</p>`,
  qcm: [
    { q: R`Dans une démonstration par récurrence, l'hérédité consiste à montrer que :`, c: [R`$P(n)$ est vraie pour tout $n$`, R`pour tout $k\geq n_0$, si $P(k)$ est vraie, alors $P(k+1)$ est vraie`, R`$P(n_0)$ et $P(n_0+1)$ sont vraies`, R`$P(k+1)$ entraîne $P(k)$`], r: 1, e: R`L'hérédité est une implication : de $P(k)$ (supposée) on déduit $P(k+1)$, pour tout $k\geq n_0$.`, ref: "principe" },
    { q: R`On a démontré l'hérédité de $P(n)$ : « $2^n$ est divisible par $3$ ». On peut conclure :`, c: [R`$P(n)$ est vraie pour tout $n$`, R`$P(n)$ est vraie à partir d'un certain rang`, R`rien, car l'initialisation est fausse pour tout $n$`, R`$P(n)$ est vraie pour $n$ pair`], r: 2, e: R`$2^n$ n'est jamais divisible par $3$. L'hérédité seule ne prouve rien : il faut un premier domino qui tombe.`, ref: "principe" },
    { q: R`$n^2+n+41$ est premier pour $n=0,1,\dots,39$. Alors :`, c: [R`il est premier pour tout $n$`, R`on ne peut rien conclure pour $n\geq40$ ; d'ailleurs $40^2+40+41=41^2$`, R`il est premier pour tout $n$ impair`, R`il suffit de vérifier $n=40$ pour conclure`], r: 1, e: R`Des vérifications ne remplacent pas une hérédité. Et $1681=41\times41$ n'est pas premier.`, ref: "principe" },
    { q: R`Soit $u_0=1$ et $u_{n+1}=2u_n+3$. Que vaut $u_3$ ?`, c: ["13", "29", "31", "61"], r: 1, e: R`$u_1=5$, $u_2=13$, $u_3=29$. On vérifie : $2^{3+2}-3=29$.`, ref: "rediger" },
    { q: R`Dans l'hérédité, on suppose que $P(k)$ est vraie :`, c: [R`pour tout entier $k$`, R`pour un entier $k\geq n_0$ fixé`, R`pour $k=n_0$ uniquement`, R`pour $k=0$`], r: 1, e: R`On fixe un entier $k\geq n_0$ quelconque ; supposer « pour tout $k$ » reviendrait à supposer le résultat.`, ref: "rediger" },
    { q: R`Pour passer de $1+3+\dots+(2k-1)$ à la somme au rang $k+1$, on ajoute :`, c: [R`$2k-1$`, R`$2k+1$`, R`$2k+3$`, R`$k+1$`], r: 1, e: R`Le terme de rang $k+1$ est $2(k+1)-1=2k+1$.`, ref: "sommes" },
    { q: R`$f$ est croissante sur $[0;2]$ et $0\leq u_k\leq2$. On peut en déduire :`, c: [R`$0\leq f(u_k)\leq2$`, R`$f(0)\leq f(u_k)\leq f(2)$`, R`$f(2)\leq f(u_k)\leq f(0)$`, R`$u_k\leq f(u_k)$`], r: 1, e: R`Une fonction croissante conserve l'ordre. Il faut ensuite comparer $f(0)$ et $f(2)$ aux bornes voulues.`, ref: "inegalites" },
    { q: R`L'inégalité de Bernoulli affirme que pour $a\geq0$ et $n\in\N$ :`, c: [R`$(1+a)^n\leq1+na$`, R`$(1+a)^n\geq1+na$`, R`$(1+a)^n\geq1+a^n$`, R`$(1+a)^n=1+na$`], r: 1, e: R`Exemple : $1{,}05^{20}\approx2{,}65\geq2$. Démonstration exigible, par récurrence.`, ref: "inegalites" },
    { q: R`Dans la démonstration de Bernoulli, l'étape clé de l'hérédité est :`, c: [R`multiplier $(1+a)^k\geq1+ka$ par $1+a$, qui est positif`, R`ajouter $a$ aux deux membres`, R`utiliser la dérivée de $x\mapsto(1+x)^n$`, R`élever au carré`], r: 0, e: R`$(1+a)^{k+1}\geq(1+ka)(1+a)=1+(k+1)a+ka^2\geq1+(k+1)a$. Multiplier par un positif conserve le sens.`, ref: "inegalites" },
    { q: R`$2^n\geq n^2$ est vraie pour $n\geq4$. Pour la démontrer par récurrence, on initialise à :`, c: ["$n=0$", "$n=3$", "$n=4$", "$n=5$"], r: 2, e: R`Elle est fausse pour $n=3$ ($8<9$) : on initialise au premier rang de la propriété annoncée, $n_0=4$.`, ref: "pieges" },
    { q: R`Soit $f(x)=1+\frac1x$, décroissante sur $]0;+\infty[$, et $u_{n+1}=f(u_n)$. En général, la suite $(u_n)$ :`, c: ["est croissante", "est décroissante", "n'est pas monotone : ses termes oscillent", "est constante"], r: 2, e: R`Une fonction décroissante inverse l'ordre à chaque étape : les termes sont alternativement au-dessus et en dessous de la limite (nombre d'or).`, ref: "inegalites" },
    { q: R`Une récurrence permet :`, c: ["de trouver une formule", "de prouver une formule conjecturée", "de prouver une propriété pour tout réel $x$", "de prouver qu'une propriété est fausse"], r: 1, e: R`On conjecture (calculs, Python), puis on prouve par récurrence. Pour réfuter, un contre-exemple suffit.`, ref: "limites" }
  ],
  cartes: [
    [R`Les deux étapes d'une récurrence ?`, R`<b>Initialisation</b> : $P(n_0)$ vraie. <b>Hérédité</b> : pour tout $k\geq n_0$, $P(k)\Rightarrow P(k+1)$.`],
    [R`Que suppose-t-on dans l'hérédité ?`, R`$P(k)$ pour <b>un</b> entier $k\geq n_0$ fixé (hypothèse de récurrence).`],
    [R`Inégalité de Bernoulli`, R`Pour $a\geq0$ et $n\in\N$ : $(1+a)^n\geq1+na$.`],
    [R`$1+2+\dots+n=$ ?`, R`$\frac{n(n+1)}{2}$`],
    [R`$1+3+5+\dots+(2n-1)=$ ?`, R`$n^2$`],
    [R`$1^2+2^2+\dots+n^2=$ ?`, R`$\frac{n(n+1)(2n+1)}{6}$`],
    [R`$1+q+q^2+\dots+q^n=$ ? ($q\neq1$)`, R`$\frac{1-q^{n+1}}{1-q}$`],
    [R`Terme général d'une suite géométrique`, R`$u_n=u_0q^n=u_pq^{n-p}$`],
    [R`$f$ croissante sur $I$, $a\leq b$ dans $I$ : ?`, R`$f(a)\leq f(b)$ : l'inégalité garde son sens.`],
    [R`Multiplier une inégalité par un négatif`, R`Renverse le sens.`],
    [R`Contre-exemple d'Euler`, R`$n^2+n+41$ premier pour $n\leq39$, mais $40^2+40+41=1681=41^2$.`],
    [R`Hérédité vraie mais initialisation fausse : exemple`, R`« $2^n$ est divisible par $3$ » : héréditaire, jamais vraie.`],
    [R`Pourquoi écrire le but $P(k+1)$ dans l'hérédité ?`, R`Pour savoir vers quoi orienter le calcul (et que le correcteur le voie).`]
  ]
};
