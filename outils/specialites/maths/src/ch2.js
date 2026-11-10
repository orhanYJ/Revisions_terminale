/* ---------- Chapitre 2 : limites de suites ---------- */
var CH2 = {
  id: "ch2", num: 2, statut: "ok", partie: "Analyse", titre: "Limites de suites", court: "Limites de suites",
  sous: "Que deviennent les termes quand $n$ devient très grand ?",
  resume: "Convergence, divergence, opérations, gendarmes, $q^n$, suites monotones, $u_{n+1}=f(u_n)$.",
  essentiel: [
    R`$(u_n)$ tend vers $+\infty$ si tout intervalle $[A;+\infty[$ contient tous les termes à partir d'un certain rang ; elle converge vers $\ell$ si tout intervalle ouvert contenant $\ell$ contient tous les termes à partir d'un certain rang.`,
    R`On calcule une limite avec les limites de référence et les opérations ; face à une forme indéterminée ($\infty-\infty$, $0\times\infty$, $\frac{\infty}{\infty}$, $\frac00$), on <b>factorise le terme prépondérant</b>.`,
    R`Comparaison : si $u_n\geq v_n$ et $v_n\to+\infty$, alors $u_n\to+\infty$. Gendarmes : si $v_n\leq u_n\leq w_n$ et $v_n,w_n\to\ell$, alors $u_n\to\ell$.`,
    R`$q^n\to+\infty$ si $q>1$, $q^n\to0$ si $-1<q<1$, $q^n=1$ si $q=1$, pas de limite si $q\leq-1$.`,
    R`Toute suite croissante majorée converge (décroissante minorée aussi) ; si $u_{n+1}=f(u_n)$ avec $f$ continue, la limite vérifie $f(\ell)=\ell$.`
  ],
  attendus: [
    R`Établir la convergence d'une suite, ou sa divergence vers $+\infty$ ou $-\infty$.`,
    R`Raisonner par récurrence pour établir une propriété d'une suite.`,
    R`Étudier des phénomènes d'évolution modélisables par une suite.`,
    R`Déterminer dans des cas simples la limite d'une suite en utilisant les limites usuelles, les opérations, des majorations, minorations ou encadrements, la factorisation du terme prépondérant.`,
    R`Démonstrations exigibles : suite croissante non majorée ; limite de $(q^n)$ par l'inégalité de Bernoulli ; suite minorée par une suite qui tend vers $+\infty$.`,
    R`Algorithmes : recherche de seuils ; valeurs approchées de $\pi$, $\e$, $\sqrt2$, $\frac{1+\sqrt5}{2}$…`
  ],
  premiere: R`
<ul><li>Une suite est <b>majorée</b> par $M$ si $u_n\leq M$ pour tout $n$ ; <b>minorée</b> par $m$ si $u_n\geq m$ ; <b>bornée</b> si elle est les deux.</li>
<li>Une suite est <b>croissante</b> si $u_n\leq u_{n+1}$ pour tout $n$.</li>
<li>Suite géométrique : $u_n=u_0q^n$ ; suite arithmétique : $u_n=u_0+nr$.</li>
<li>En Première, on a vu la notion de limite sur des exemples (« les termes se rapprochent de… ») : en Terminale, on la définit précisément.</li></ul>`,
  cours: [
    { id: "infini", titre: "Tendre vers l'infini", html: R`
[def|Limite $+\infty$]La suite $(u_n)$ <b>tend vers $+\infty$</b> si tout intervalle de la forme $[A;+\infty[$ contient tous les termes $u_n$ à partir d'un certain rang. On note $\lim_{n\to+\infty}u_n=+\infty$.[/]
<p>Autrement dit : aussi grand que soit le seuil $A$, la suite finit par le dépasser <b>et ne redescend plus en dessous</b>. De même, $(u_n)$ tend vers $-\infty$ si tout intervalle $]-\infty;A]$ contient tous les termes à partir d'un certain rang.</p>
[ex|$\sqrt n$ tend vers $+\infty$]Soit $A>0$. $\sqrt n\geq A\iff n\geq A^2$. Donc dès que $n\geq A^2$, tous les termes sont dans $[A;+\infty[$. Pour $A=100$, c'est à partir du rang $10\,000$.[/]
[prop|Limites de référence]$\lim n=\lim n^2=\lim n^3=\lim\sqrt n=+\infty$ ; plus généralement $\lim n^p=+\infty$ pour tout entier $p\geq1$.[/]
[thm|Suite croissante non majorée]Toute suite croissante et non majorée tend vers $+\infty$. (Démonstration exigible.)[/]
[piege|Non majorée ne suffit pas]$u_n=n$ si $n$ est pair, $u_n=0$ si $n$ est impair : la suite n'est pas majorée mais ne tend pas vers $+\infty$ (une infinité de termes valent $0$). Il faut la croissance.[/]` },
    { id: "convergence", titre: "Converger vers un réel", html: R`
[def|Suite convergente]La suite $(u_n)$ <b>converge vers le réel $\ell$</b> si tout intervalle ouvert contenant $\ell$ contient tous les termes $u_n$ à partir d'un certain rang. On note $\lim_{n\to+\infty}u_n=\ell$. Une suite qui ne converge pas est dite <b>divergente</b>.[/]
<p>En pratique, on prend des intervalles $]\ell-\varepsilon;\ell+\varepsilon[$ : pour tout $\varepsilon>0$, il existe un rang $N$ tel que, pour $n\geq N$, $|u_n-\ell|<\varepsilon$. Joue avec la largeur de la bande :</p>
<div data-anim="bande"></div>
<div data-w="suite"></div>
[prop|Unicité et références]Si une suite converge, sa limite est unique. $\lim\frac1n=\lim\frac1{n^2}=\lim\frac1{\sqrt n}=0$ ; plus généralement $\lim\frac1{n^p}=0$ pour $p\geq1$.[/]
<p>Une suite divergente peut tendre vers $\pm\infty$… ou n'avoir <b>aucune limite</b> : $u_n=(-1)^n$ vaut $1,-1,1,-1\dots$ ; aucune bande étroite autour d'un réel ne contient tous les termes à partir d'un rang.</p>
[piege|Ce n'est pas « s'approcher »]Les termes de $u_n=1+\frac1n$ s'approchent de $0$ (ils diminuent), mais la limite est $1$. Converger vers $\ell$, c'est finir <b>aussi près qu'on veut</b> de $\ell$, pas seulement « se rapprocher ».[/]` },
    { id: "operations", titre: "Opérations sur les limites", html: R`
<p>Les règles sont admises. $\ell$ et $\ell'$ désignent des réels ; « F.I. » signifie <b>forme indéterminée</b> : on ne peut pas conclure directement, il faut transformer l'écriture.</p>
<div class="tab-wrap"><table><tr><th>$\lim u_n$</th><th>$\lim v_n$</th><th>$\lim(u_n+v_n)$</th><th>$\lim(u_nv_n)$</th></tr>
<tr><td>$\ell$</td><td>$\ell'$</td><td>$\ell+\ell'$</td><td>$\ell\ell'$</td></tr>
<tr><td>$\ell$</td><td>$+\infty$</td><td>$+\infty$</td><td>$+\infty$ si $\ell>0$ ; $-\infty$ si $\ell<0$ ; <b>F.I.</b> si $\ell=0$</td></tr>
<tr><td>$+\infty$</td><td>$+\infty$</td><td>$+\infty$</td><td>$+\infty$</td></tr>
<tr><td>$+\infty$</td><td>$-\infty$</td><td><b>F.I.</b></td><td>$-\infty$</td></tr></table></div>
<div class="tab-wrap"><table><tr><th>$\lim u_n$</th><th>$\lim v_n$</th><th>$\lim\frac{u_n}{v_n}$</th></tr>
<tr><td>$\ell$</td><td>$\ell'\neq0$</td><td>$\frac{\ell}{\ell'}$</td></tr>
<tr><td>$\ell$</td><td>$\pm\infty$</td><td>$0$</td></tr>
<tr><td>$\ell\neq0$ ou $\pm\infty$</td><td>$0$ (de signe constant)</td><td>$\pm\infty$ (règle des signes)</td></tr>
<tr><td>$\pm\infty$</td><td>$\ell'$</td><td>$\pm\infty$ (règle des signes)</td></tr>
<tr><td>$0$</td><td>$0$</td><td><b>F.I.</b></td></tr>
<tr><td>$\pm\infty$</td><td>$\pm\infty$</td><td><b>F.I.</b></td></tr></table></div>
[meth|Lever une indétermination : le terme prépondérant]$u_n=\frac{3n^2-n+1}{2n^2+5}$ est de la forme $\frac{\infty}{\infty}$. On factorise par $n^2$ en haut et en bas :
$$u_n=\frac{n^2\left(3-\frac1n+\frac1{n^2}\right)}{n^2\left(2+\frac5{n^2}\right)}=\frac{3-\frac1n+\frac1{n^2}}{2+\frac5{n^2}}\quad\text{donc}\quad\lim u_n=\frac32.$$
Python le confirme : $u_{1000}\approx1{,}4995$.[/]
[meth|$\infty-\infty$ avec des racines : la quantité conjuguée]$u_n=\sqrt{n+1}-\sqrt n$ est de la forme $\infty-\infty$. On multiplie et on divise par $\sqrt{n+1}+\sqrt n$ :
$$u_n=\frac{(n+1)-n}{\sqrt{n+1}+\sqrt n}=\frac{1}{\sqrt{n+1}+\sqrt n}\quad\text{donc}\quad\lim u_n=0.$$[/]
[ex|Un polynôme]$u_n=n^2-5n$ : forme $\infty-\infty$. $u_n=n^2\left(1-\frac5n\right)$ avec $n^2\to+\infty$ et $1-\frac5n\to1$, donc $u_n\to+\infty$. Retiens : <b>un polynôme en $n$ a la limite de son terme de plus haut degré</b>.[/]` },
    { id: "comparaison", titre: "Comparaison et théorème des gendarmes", html: R`
[thm|Comparaison]Si, à partir d'un certain rang, $u_n\geq v_n$ et si $\lim v_n=+\infty$, alors $\lim u_n=+\infty$.<br>Si, à partir d'un certain rang, $u_n\leq w_n$ et si $\lim w_n=-\infty$, alors $\lim u_n=-\infty$.[/]
<p>La première propriété est une <b>démonstration exigible</b> (onglet Démonstrations).</p>
[thm|Théorème des gendarmes]Si, à partir d'un certain rang, $v_n\leq u_n\leq w_n$, et si $(v_n)$ et $(w_n)$ convergent vers <b>la même limite</b> $\ell$, alors $(u_n)$ converge vers $\ell$.[/]
[ex|Avec $(-1)^n$]Soit $u_n=2+\frac{(-1)^n}{n+1}$. Comme $-1\leq(-1)^n\leq1$ et $n+1>0$ : $2-\frac1{n+1}\leq u_n\leq2+\frac1{n+1}$. Les deux gendarmes tendent vers $2$, donc $\lim u_n=2$.[/]
[ex|Minorer pour aller vers l'infini]$u_n=n+(-1)^n\geq n-1$ et $\lim(n-1)=+\infty$, donc $\lim u_n=+\infty$.[/]
[prop|Passage à la limite dans une inégalité]Si $u_n\leq v_n$ à partir d'un certain rang, et si les deux suites convergent, alors $\lim u_n\leq\lim v_n$.[/]
[piege|Les inégalités strictes deviennent larges]$\frac1n>0$ pour tout $n\geq1$, mais $\lim\frac1n=0$. Par passage à la limite, $<$ devient $\leq$.[/]` },
    { id: "geometrique", titre: "Suites géométriques", html: R`
[thm|Limite de $q^n$]Soit $q$ un réel.
<ul><li>Si $q>1$ : $\lim q^n=+\infty$.</li><li>Si $q=1$ : $q^n=1$ pour tout $n$, limite $1$.</li><li>Si $-1<q<1$ : $\lim q^n=0$.</li><li>Si $q\leq-1$ : $(q^n)$ n'a pas de limite.</li></ul>[/]
<p>Le cas $q>1$ est une <b>démonstration exigible</b>, qui utilise l'inégalité de Bernoulli du chapitre 1 : en écrivant $q=1+a$ avec $a>0$, on a $q^n\geq1+na$, qui tend vers $+\infty$. Exemple : $1{,}02^n\geq1+0{,}02n$, donc $1{,}02^n\geq100$ au plus tard dès $n=4950$ (en fait dès $n=233$ : Bernoulli minore beaucoup).</p>
[ex|Une suite arithmético-géométrique]$a_n=15-10\times0{,}8^n$ (chapitre 1) : $0<0{,}8<1$ donc $0{,}8^n\to0$ et $a_n\to15$.[/]
[prop|Somme des termes]Si $-1<q<1$ : $\lim\left(1+q+\dots+q^n\right)=\lim\frac{1-q^{n+1}}{1-q}=\frac1{1-q}$.[/]
[ex|Le paradoxe de Zénon]$\frac12+\frac14+\dots+\frac1{2^n}=\frac12\times\frac{1-\left(\frac12\right)^n}{1-\frac12}=1-\frac1{2^n}$, qui tend vers $1$ : une infinité de durées peut avoir une somme finie. Pour $n=10$, la somme vaut $0{,}9990234375$.[/]` },
    { id: "monotones", titre: "Suites monotones : le théorème de convergence", html: R`
[thm|Convergence monotone (admis)]Toute suite <b>croissante et majorée</b> converge. Toute suite <b>décroissante et minorée</b> converge.[/]
<p>C'est un <b>théorème d'existence</b> : il dit que la limite existe, pas ce qu'elle vaut. Si $(u_n)$ est croissante et majorée par $M$, sa limite $\ell$ vérifie $\ell\leq M$… mais $\ell$ peut être strictement plus petite que $M$ : avec $u_n=1-\frac1{n+1}$, majorée par $5$, la limite est $1$.</p>
[prop|Rappel]Une suite croissante et non majorée tend vers $+\infty$. Donc une suite croissante a toujours une limite : finie si elle est majorée, $+\infty$ sinon.[/]
[piege|Majorant n'est pas limite]« La suite est majorée par $2$ donc elle converge vers $2$ » est faux. Il faut un autre argument pour trouver la limite (partie suivante).[/]` },
    { id: "recurrentes", titre: "Suites $u_{n+1}=f(u_n)$ : la méthode complète", html: R`
<p>C'est le grand classique du bac. Schéma en trois temps :</p>
<ol><li>Par récurrence (chapitre 1) : $a\leq u_n\leq u_{n+1}\leq b$ (ou l'inverse).</li><li>La suite est croissante et majorée (ou décroissante et minorée) : elle converge vers un réel $\ell$.</li><li>Si $f$ est <b>continue</b>, en passant à la limite dans $u_{n+1}=f(u_n)$, on obtient $\ell=f(\ell)$ : on résout cette équation et on choisit la bonne solution grâce à l'encadrement.</li></ol>
[thm|Point fixe]Si $(u_n)$ converge vers $\ell$, si $u_{n+1}=f(u_n)$ et si $f$ est continue en $\ell$, alors $f(\ell)=\ell$. (Image d'une suite convergente par une fonction continue : chapitre 4.)[/]
[ex|$u_0=1$, $u_{n+1}=\sqrt{u_n+2}$]On a montré au chapitre 1 que $0\leq u_n\leq u_{n+1}\leq2$ : la suite converge vers $\ell\in[0;2]$. $f(x)=\sqrt{x+2}$ est continue, donc $\ell=\sqrt{\ell+2}$, d'où $\ell^2=\ell+2$, soit $\ell^2-\ell-2=0$, $(\ell-2)(\ell+1)=0$. Comme $\ell\geq0$, $\ell=2$.[/]
<div data-w="toile"></div>
[meth|La suite auxiliaire]Quand l'énoncé introduit $v_n=u_n-\ell$ (ou une expression plus compliquée) et montre qu'elle est géométrique de raison $q$ avec $|q|<1$, on obtient $v_n\to0$, donc $u_n\to\ell$ : c'est souvent plus rapide et cela donne aussi la <b>vitesse</b> de convergence.[/]` }
  ],
  pieges: [
    { t: "Conclure $\\infty-\\infty=0$ ou $\\frac\\infty\\infty=1$", h: R`Ce sont des formes indéterminées : $n^2-n\to+\infty$, $n-n^2\to-\infty$, $\frac{2n}{n}\to2$. Transforme l'écriture.` },
    { t: "Gendarmes avec deux limites différentes", h: R`Si $v_n\to1$ et $w_n\to3$, l'encadrement $v_n\leq u_n\leq w_n$ ne dit pas si $(u_n)$ converge.` },
    { t: "« Bornée donc convergente »", h: R`$(-1)^n$ est bornée et diverge. Il faut <b>monotone et bornée</b> (du bon côté).` },
    { t: "$q^n$ avec $q$ négatif", h: R`$(-0{,}5)^n\to0$, mais $(-2)^n$ n'a pas de limite (ni $+\infty$, ni $-\infty$) : les termes changent de signe.` },
    { t: "Oublier la continuité de $f$", h: R`Pour écrire $f(\ell)=\ell$, il faut que $f$ soit continue. Au bac, une phrase suffit : « $f$ est continue sur $I$ (fonction polynôme / racine / quotient…) ».` },
    { t: "Prendre une solution de $f(\\ell)=\\ell$ au hasard", h: R`L'équation a souvent deux solutions : élimine celle qui n'est pas dans l'intervalle donné par l'encadrement.` }
  ],
  demos: [
    { bo: true, t: "Une suite croissante non majorée tend vers $+\\infty$", h: R`
<p>Soit $(u_n)$ croissante et non majorée, et soit $A$ un réel.</p>
<p>La suite n'est pas majorée, donc $A$ n'est pas un majorant : il existe un rang $N$ tel que $u_N>A$.</p>
<p>La suite est croissante, donc pour tout $n\geq N$ : $u_n\geq u_N>A$.</p>
<p>Ainsi, tous les termes à partir du rang $N$ sont dans $[A;+\infty[$. Cela vaut pour tout $A$ : par définition, $\lim u_n=+\infty$.</p>
<p class="stylo">Les deux hypothèses servent chacune une fois : « non majorée » pour trouver $N$, « croissante » pour rester au-dessus.</p>` },
    { bo: true, t: "Limite de $(q^n)$ pour $q>1$ (avec Bernoulli)", h: R`
<p>Soit $q>1$. On pose $a=q-1>0$. D'après l'inégalité de Bernoulli (démontrée par récurrence au chapitre 1), pour tout $n\in\N$ :
$$q^n=(1+a)^n\geq1+na.$$
Or $a>0$, donc $\lim(1+na)=+\infty$. Par comparaison, $\lim q^n=+\infty$.</p>
<p><b>Cas $0<q<1$</b> (pour comprendre). On pose $Q=\frac1q>1$ : $q^n=\frac1{Q^n}$ et $Q^n\to+\infty$, donc $q^n\to0$. Pour $-1<q<0$, on utilise $|q^n|=|q|^n\to0$ et l'encadrement $-|q|^n\leq q^n\leq|q|^n$ (gendarmes).</p>` },
    { bo: true, t: "Une suite minorée par une suite qui tend vers $+\\infty$ tend vers $+\\infty$", h: R`
<p>Hypothèses : à partir d'un rang $n_1$, $u_n\geq v_n$ ; et $\lim v_n=+\infty$.</p>
<p>Soit $A$ un réel. Comme $v_n\to+\infty$, il existe un rang $n_2$ tel que pour $n\geq n_2$, $v_n\geq A$.</p>
<p>Soit $N$ le plus grand des deux rangs $n_1$ et $n_2$. Pour $n\geq N$ : $u_n\geq v_n\geq A$. Donc tous les termes $u_n$ sont dans $[A;+\infty[$ à partir du rang $N$ : $\lim u_n=+\infty$.</p>
<p class="stylo">L'astuce : prendre $N=\max(n_1,n_2)$ pour que les deux informations soient vraies en même temps.</p>` },
    { bo: false, t: "Somme géométrique : $\\lim(1+q+\\dots+q^n)=\\frac1{1-q}$ pour $|q|<1$", h: R`
<p>Pour $q\neq1$, $1+q+\dots+q^n=\frac{1-q^{n+1}}{1-q}$. Si $-1<q<1$, $q^{n+1}\to0$, donc la somme tend vers $\frac{1}{1-q}$ par opérations sur les limites.</p>` }
  ],
  algos: [
    { bo: true, t: "Recherche d'un seuil", avant: R`<p>On sait que $u_n=0{,}9^n\to0$. À partir de quel rang a-t-on $u_n<0{,}01$ ? Une boucle <code>while</code> avance tant que la condition d'arrêt n'est pas atteinte.</p>`,
      code: `def seuil(e):
    n = 0
    u = 1                 # u0 = 0,9^0
    while u >= e:
        n = n + 1
        u = 0.9 * u
    return n

print(seuil(0.01))`, sortie: `44`,
      apres: R`<p>$0{,}9^{43}\approx0{,}0108$ et $0{,}9^{44}\approx0{,}0097$. Comme la suite est décroissante, tous les termes suivants restent sous $0{,}01$. Sans la monotonie, le premier rang trouvé ne garantirait pas « à partir de ce rang ».</p>` },
    { bo: true, t: "Valeur approchée de $\\sqrt2$ (méthode de Héron)", avant: R`<p>La suite $u_0=1$, $u_{n+1}=\frac12\left(u_n+\frac2{u_n}\right)$ converge vers $\sqrt2$ très vite (le nombre de décimales exactes double environ à chaque étape). <span class="tag hp">pour aller plus loin</span> : l'étude de sa convergence est un approfondissement du programme.</p>`,
      code: `u = 1.0
for k in range(5):
    u = (u + 2 / u) / 2
    print(k + 1, u)`, sortie: `1 1.5
2 1.4166666666666665
3 1.4142156862745097
4 1.4142135623746899
5 1.414213562373095` },
    { bo: true, t: "Valeur approchée de $\\e$", avant: R`<p>Deux suites qui tendent vers $\e$ : $\left(1+\frac1n\right)^n$ (lente) et $1+\frac1{1!}+\frac1{2!}+\dots+\frac1{n!}$ (rapide).</p>`,
      code: `n = 1000
print((1 + 1/n)**n)

s = 0
t = 1                      # t = 1/k!
for k in range(11):
    s = s + t
    t = t / (k + 1)
print(s)`, sortie: `2.7169239322355936
2.7182818011463845`,
      apres: R`<p>$\e\approx2{,}718281828$ : la somme jusqu'à $\frac1{10!}$ donne déjà 7 décimales exactes, $\left(1+\frac1{1000}\right)^{1000}$ seulement 2.</p>` },
    { bo: true, t: "Valeur approchée du nombre d'or $\\frac{1+\\sqrt5}{2}$", code: `u = 1.0
for k in range(20):
    u = 1 + 1 / u
print(u, (1 + 5**0.5) / 2)`, sortie: `1.618033985017358 1.618033988749895`,
      apres: R`<p>La suite $u_{n+1}=1+\frac1{u_n}$ converge vers la solution positive de $\ell=1+\frac1\ell$, soit $\ell^2-\ell-1=0$, $\ell=\frac{1+\sqrt5}2$ (voir la toile d'araignée : elle s'enroule en spirale).</p>` }
  ],
  methodes: [
    { t: "Comment calculer une limite de suite ?", h: R`
<ol><li>Remplace mentalement $n$ par « très grand » et applique les opérations.</li><li>Si c'est une forme indéterminée : factorise le terme prépondérant (polynômes, quotients), utilise la quantité conjuguée (racines), ou réécris (puissances : $\frac{2^n+3^n}{3^n}=\left(\frac23\right)^n+1\to1$).</li><li>Si la suite contient $(-1)^n$, $\cos(n)$ ou une partie bornée : encadre, puis gendarmes ou comparaison.</li></ol>` },
    { t: "Comment montrer qu'une suite converge sans calculer sa limite ?", h: R`
<p>Montre qu'elle est <b>monotone et bornée</b> du bon côté (souvent par récurrence), puis cite le théorème : « $(u_n)$ est croissante et majorée par $2$, donc elle converge ».</p>` },
    { t: "Comment trouver la limite d'une suite $u_{n+1}=f(u_n)$ ?", h: R`
<ol><li>Justifie la convergence (monotone bornée).</li><li>Écris : « $f$ est continue sur $I$, donc la limite $\ell$ vérifie $f(\ell)=\ell$ ».</li><li>Résous et choisis la solution compatible avec les bornes.</li></ol>` },
    { t: "Comment répondre à « à partir de quel rang… » ?", h: R`
<p>Avec une formule explicite : résous l'inéquation (au chapitre 6 avec le logarithme ; pour l'instant avec la calculatrice ou un tableau de valeurs). Sinon : algorithme de seuil en Python, en vérifiant que la suite est monotone pour que le seuil soit définitif.</p>` }
  ],
  exos: [
    { niv: 1, t: "Calculs de limites", enonce: R`<p>Déterminer la limite de chaque suite.</p><ol><li>$a_n=\frac{n^3-2n}{4n^3+n^2}$</li><li>$b_n=\frac{2n+1}{n^2+1}$</li><li>$c_n=3\times0{,}7^n-5$</li><li>$d_n=2^n-3^n$</li><li>$e_n=\frac{5-(-1)^n}{n}$ ($n\geq1$)</li></ol>`,
      corrige: R`<ol><li>Forme $\frac\infty\infty$ : $a_n=\frac{1-\frac2{n^2}}{4+\frac1n}\to\frac14$ (vérification : $a_{10\,000}\approx0{,}24999$).</li>
<li>$b_n=\frac{n\left(2+\frac1n\right)}{n^2\left(1+\frac1{n^2}\right)}=\frac{2+\frac1n}{n\left(1+\frac1{n^2}\right)}$ : numérateur $\to2$, dénominateur $\to+\infty$, donc $b_n\to0$.</li>
<li>$0<0{,}7<1$ donc $0{,}7^n\to0$ et $c_n\to-5$.</li>
<li>Forme $\infty-\infty$. $d_n=3^n\left(\left(\frac23\right)^n-1\right)$ : $3^n\to+\infty$ et $\left(\frac23\right)^n-1\to-1$, donc $d_n\to-\infty$.</li>
<li>$4\leq5-(-1)^n\leq6$, donc $\frac4n\leq e_n\leq\frac6n$ ; les deux gendarmes tendent vers $0$ : $e_n\to0$.</li></ol>` },
    { niv: 1, t: "Comparaison", enonce: R`<p>Soit $u_n=n^2+(-1)^n n$ pour $n\geq1$.</p><ol><li>Montrer que $u_n\geq n^2-n$.</li><li>En déduire la limite de $(u_n)$.</li></ol>`,
      corrige: R`<ol><li>$(-1)^n\geq-1$ et $n>0$, donc $(-1)^nn\geq-n$, d'où $u_n\geq n^2-n$.</li><li>$n^2-n=n^2\left(1-\frac1n\right)\to+\infty$. Par comparaison, $u_n\to+\infty$.</li></ol>` },
    { niv: 2, t: "Géométrique et sommes", enonce: R`<p>Une balle est lâchée de $2$ m. À chaque rebond, elle remonte aux $\frac34$ de la hauteur précédente. On note $h_n$ la hauteur atteinte après le $n$-ième rebond ($h_0=2$).</p><ol><li>Exprimer $h_n$ en fonction de $n$. Limite ?</li><li>Montrer que la distance verticale totale parcourue jusqu'au $n$-ième rebond (descentes et montées) est $D_n=2+2\left(h_1+\dots+h_n\right)$.</li><li>Calculer $\lim D_n$.</li></ol>`,
      corrige: R`<ol><li>$(h_n)$ est géométrique de raison $\frac34$ : $h_n=2\times\left(\frac34\right)^n$. Comme $0<\frac34<1$, $h_n\to0$.</li>
<li>La balle descend de $2$ m, puis pour chaque rebond $k$ elle monte de $h_k$ et redescend de $h_k$ : $D_n=2+2(h_1+\dots+h_n)$.</li>
<li>$h_1+\dots+h_n=2\times\frac34\times\frac{1-\left(\frac34\right)^n}{1-\frac34}=6\left(1-\left(\frac34\right)^n\right)\to6$. Donc $D_n\to2+12=14$ m.</li></ol>` },
    { niv: 2, t: "Convergence monotone", enonce: R`<p>Soit $u_0=5$ et $u_{n+1}=\frac{u_n}{2}+\frac{1}{u_n}$.</p><ol><li>Montrer que pour $x>0$, $\frac x2+\frac1x-\sqrt2=\frac{(x-\sqrt2)^2}{2x}$. En déduire que $u_n\geq\sqrt2$ pour $n\geq1$.</li><li>Montrer que $(u_n)$ est décroissante à partir du rang $1$.</li><li>En déduire qu'elle converge et déterminer sa limite.</li></ol>`,
      corrige: R`<ol><li>$\frac{(x-\sqrt2)^2}{2x}=\frac{x^2-2\sqrt2x+2}{2x}=\frac x2-\sqrt2+\frac1x$. ✓ On voit par récurrence immédiate que $u_n>0$ ; alors $u_{n+1}-\sqrt2=\frac{(u_n-\sqrt2)^2}{2u_n}\geq0$, donc $u_n\geq\sqrt2$ pour tout $n\geq1$ (et aussi $u_0=5$).</li>
<li>$u_{n+1}-u_n=\frac1{u_n}-\frac{u_n}2=\frac{2-u_n^2}{2u_n}\leq0$ car $u_n\geq\sqrt2$. La suite est décroissante.</li>
<li>Décroissante et minorée par $\sqrt2$ : elle converge vers $\ell\geq\sqrt2$. $f(x)=\frac x2+\frac1x$ est continue sur $]0;+\infty[$, donc $\ell=\frac\ell2+\frac1\ell$, soit $\ell^2=2$, $\ell=\sqrt2$ (c'est la méthode de Héron : $\frac x2+\frac1x=\frac12\left(x+\frac2x\right)$).</li></ol>` },
    { niv: 3, t: "Une suite homographique (type bac)", enonce: R`<p>Soit $(u_n)$ définie par $u_0=0$ et $u_{n+1}=\frac{2u_n+3}{u_n+4}$. On note $f(x)=\frac{2x+3}{x+4}$ sur $[0;+\infty[$.</p>
<ol><li>Calculer $u_1$ et $u_2$.</li><li>Étudier les variations de $f$. Montrer par récurrence que $0\leq u_n\leq u_{n+1}\leq1$.</li><li>En déduire que $(u_n)$ converge et déterminer sa limite.</li><li>On pose $v_n=\frac{u_n-1}{u_n+3}$. Montrer que $(v_n)$ est géométrique de raison $\frac15$ et retrouver la limite.</li><li>Écrire un programme Python qui renvoie le plus petit $n$ tel que $1-u_n<10^{-6}$, et donner le résultat.</li></ol>`,
      corrige: R`<ol><li>$u_1=\frac34$ ; $u_2=\frac{2\times\frac34+3}{\frac34+4}=\frac{4{,}5}{4{,}75}=\frac{18}{19}\approx0{,}947$.</li>
<li>$f'(x)=\frac{2(x+4)-(2x+3)}{(x+4)^2}=\frac{5}{(x+4)^2}>0$ : $f$ est croissante. Récurrence : $0\leq0\leq\frac34\leq1$ ; si $0\leq u_k\leq u_{k+1}\leq1$, alors $f(0)\leq u_{k+1}\leq u_{k+2}\leq f(1)$, soit $\frac34\leq u_{k+1}\leq u_{k+2}\leq1$.</li>
<li>Croissante et majorée par $1$ : elle converge vers $\ell\in[0;1]$. $f$ est continue (quotient de polynômes, dénominateur non nul), donc $f(\ell)=\ell$ : $2\ell+3=\ell^2+4\ell$, $\ell^2+2\ell-3=0$, $(\ell-1)(\ell+3)=0$. Comme $\ell\geq0$ : $\ell=1$.</li>
<li>$v_{n+1}=\frac{u_{n+1}-1}{u_{n+1}+3}=\frac{(2u_n+3)-(u_n+4)}{(2u_n+3)+3(u_n+4)}=\frac{u_n-1}{5u_n+15}=\frac15v_n$. $v_0=-\frac13$, donc $v_n=-\frac13\left(\frac15\right)^n\to0$. De $v_n(u_n+3)=u_n-1$ on tire $u_n=\frac{1+3v_n}{1-v_n}\to\frac{1}{1}=1$.</li>
<li>Programme : <code>n=0 ; u=0</code> puis <code>while 1 - u &gt;= 1e-6: u = (2*u+3)/(u+4) ; n = n+1</code>, renvoyer <code>n</code>. Résultat : $n=9$ ($1-u_8\approx3{,}4\times10^{-6}$, $1-u_9\approx6{,}8\times10^{-7}$).</li></ol>
<p class="stylo">À retenir : la suite auxiliaire donne la vitesse : l'écart à $1$ est divisé par environ $5$ à chaque étape.</p>` }
  ],
  annales: [
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 4, partie A", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Posidonie : convergence d'une suite croissante majorée, limite $L=15$ par $h(L)=L$, seuil de $14$ hectares en Python. Corrigé commenté dans la page <a href="#epreuve">L'épreuve</a>.` },
    { ref: "Bac 2026, Métropole, 17 juin 2026 (sujet 2), exercice 2, partie A", url: "https://www.apmep.fr/IMG/pdf/BAC_generale_specialite_J2_2026-06-17_Metropole_FK-v4.pdf", h: R`$V_{n+1}=0{,}995V_n+6$ : récurrence, « justifier que la suite converge et calculer sa limite » ($1200$).` },
    { ref: "Bac 2026, Métropole, 16 juin 2026 (sujet 1), exercice 3, partie B", url: "https://www.apmep.fr/IMG/pdf/BAC_General_Specialite_Sujet_J1_metropole_FK-v2.pdf", h: R`Suite décroissante minorée par $10$, donc convergente ; la limite vérifie $x=0{,}965x+0{,}35$ (le terme en $\e^{-0{,}1n}$ tend vers $0$).` }
  ],
  retenir: R`
[def|Limites]$u_n\to+\infty$ : tout $[A;+\infty[$ contient tous les termes à partir d'un certain rang.<br>$u_n\to\ell$ : tout intervalle ouvert contenant $\ell$ contient tous les termes à partir d'un certain rang.[/]
<h3>Formes indéterminées</h3><p>$+\infty-\infty$ ; $0\times\infty$ ; $\frac\infty\infty$ ; $\frac00$. Outils : terme prépondérant, quantité conjuguée, réécriture.</p>
[thm|Comparaison et gendarmes]$u_n\geq v_n$ et $v_n\to+\infty$ ⟹ $u_n\to+\infty$.<br>$v_n\leq u_n\leq w_n$, $v_n\to\ell$ et $w_n\to\ell$ ⟹ $u_n\to\ell$.[/]
[thm|Géométriques]$q>1$ : $q^n\to+\infty$ ; $-1<q<1$ : $q^n\to0$ ; $q\leq-1$ : pas de limite. Si $|q|<1$ : $1+q+\dots+q^n\to\frac1{1-q}$.[/]
[thm|Suites monotones]Croissante majorée ⟹ converge. Décroissante minorée ⟹ converge. Croissante non majorée ⟹ $+\infty$.[/]
<h3>$u_{n+1}=f(u_n)$</h3><ol><li>Récurrence : $a\leq u_n\leq u_{n+1}\leq b$.</li><li>Monotone bornée ⟹ converge vers $\ell$.</li><li>$f$ continue ⟹ $f(\ell)=\ell$ ; choisir la solution dans $[a;b]$.</li></ol>
<p class="stylo">Bornée ne suffit pas. Majorant ≠ limite. Inégalité stricte → large à la limite.</p>`,
  qcm: [
    { q: R`La suite $(u_n)$ converge vers $\ell$ signifie :`, c: [R`les termes se rapprochent de $\ell$`, R`tout intervalle ouvert contenant $\ell$ contient tous les $u_n$ à partir d'un certain rang`, R`un terme vaut $\ell$`, R`tout intervalle ouvert contenant $\ell$ contient une infinité de termes`], r: 1, e: R`C'est la définition du programme. « Une infinité de termes » ne suffit pas : $(-1)^n$ a une infinité de termes égaux à $1$ sans converger.`, ref: "convergence" },
    { q: R`$\lim_{n\to+\infty}\frac{3n^2-n+1}{2n^2+5}=$`, c: ["$0$", R`$\frac32$`, "$+\\infty$", R`$\frac15$`], r: 1, e: R`On factorise par $n^2$ : $\frac{3-\frac1n+\frac1{n^2}}{2+\frac5{n^2}}\to\frac32$.`, ref: "operations" },
    { q: R`Laquelle de ces formes est indéterminée ?`, c: [R`$+\infty+\infty$`, R`$\frac{1}{+\infty}$`, R`$0\times(+\infty)$`, R`$2\times(-\infty)$`], r: 2, e: R`Les quatre F.I. : $\infty-\infty$, $0\times\infty$, $\frac\infty\infty$, $\frac00$.`, ref: "operations" },
    { q: R`$\lim\left(\sqrt{n+1}-\sqrt n\right)=$`, c: ["$0$", "$1$", "$+\\infty$", "elle n'existe pas"], r: 0, e: R`Quantité conjuguée : $\frac1{\sqrt{n+1}+\sqrt n}\to0$.`, ref: "operations" },
    { q: R`Si $2-\frac1n\leq u_n\leq2+\frac1n$ pour tout $n\geq1$, alors :`, c: [R`$u_n\to2$`, R`$u_n$ diverge`, R`on ne peut rien dire`, R`$u_n=2$ pour tout $n$`], r: 0, e: R`Théorème des gendarmes : les deux encadrements tendent vers $2$.`, ref: "comparaison" },
    { q: R`$\lim(-0{,}9)^n=$`, c: ["$0$", "$-\\infty$", "$+\\infty$", "pas de limite"], r: 0, e: R`$-1<-0{,}9<1$, donc $(-0{,}9)^n\to0$ (en oscillant autour de $0$).`, ref: "geometrique" },
    { q: R`$\lim(-1{,}5)^n=$`, c: ["$0$", "$-\\infty$", "$+\\infty$", "pas de limite"], r: 3, e: R`$q\leq-1$ : les termes alternent de signe et grandissent en valeur absolue.`, ref: "geometrique" },
    { q: R`La démonstration exigible de $\lim q^n=+\infty$ ($q>1$) utilise :`, c: ["le théorème des gendarmes", "l'inégalité de Bernoulli et la comparaison", "la quantité conjuguée", "la dérivée"], r: 1, e: R`$q^n=(1+a)^n\geq1+na\to+\infty$ avec $a=q-1>0$.`, ref: "geometrique" },
    { q: R`$\frac12+\frac14+\dots+\frac1{2^n}$ tend vers :`, c: ["$\\frac12$", "$1$", "$2$", "$+\\infty$"], r: 1, e: R`C'est $1-\frac1{2^n}$, qui tend vers $1$.`, ref: "geometrique" },
    { q: R`Une suite croissante et majorée par $5$ :`, c: ["converge vers $5$", "converge vers une limite $\\ell\\leq5$", "tend vers $+\\infty$", "peut ne pas avoir de limite"], r: 1, e: R`Théorème de convergence monotone ; la limite est inférieure ou égale au majorant, pas forcément égale.`, ref: "monotones" },
    { q: R`La suite $(-1)^n$ est bornée. Donc :`, c: ["elle converge", "elle tend vers $0$", "on ne peut pas conclure qu'elle converge : en fait elle diverge", "elle est monotone"], r: 2, e: R`Bornée ne suffit pas : il faut aussi la monotonie.`, ref: "convergence" },
    { q: R`$u_{n+1}=\sqrt{u_n+2}$ converge vers $\ell\geq0$. Alors $\ell=$`, c: ["$-1$", "$1$", "$2$", "$\\sqrt2$"], r: 2, e: R`$\ell=\sqrt{\ell+2}\Rightarrow\ell^2-\ell-2=0\Rightarrow\ell=2$ ou $\ell=-1$ ; on garde $\ell=2$.`, ref: "recurrentes" },
    { q: R`Pour écrire $f(\ell)=\ell$ à partir de $u_{n+1}=f(u_n)$, il faut que :`, c: ["$f$ soit croissante", "$f$ soit continue (en $\\ell$)", "$f$ soit positive", "$u_0=\\ell$"], r: 1, e: R`On passe à la limite dans $f(u_n)$ grâce à la continuité de $f$.`, ref: "recurrentes" },
    { q: R`$u_n\geq n-1$ pour tout $n$. Alors :`, c: [R`$u_n\to+\infty$`, R`$u_n\to-\infty$`, R`$u_n$ converge`, R`on ne sait rien`], r: 0, e: R`Comparaison : minorée par une suite qui tend vers $+\infty$ (démonstration exigible).`, ref: "comparaison" }
  ],
  cartes: [
    [R`Définition : $u_n\to+\infty$`, R`Tout intervalle $[A;+\infty[$ contient tous les termes à partir d'un certain rang.`],
    [R`Définition : $u_n\to\ell$`, R`Tout intervalle ouvert contenant $\ell$ contient tous les termes à partir d'un certain rang.`],
    [R`Les 4 formes indéterminées`, R`$\infty-\infty$ ; $0\times\infty$ ; $\frac\infty\infty$ ; $\frac00$`],
    [R`Lever $\frac\infty\infty$ pour un quotient de polynômes`, R`Factoriser en haut et en bas par le terme de plus haut degré.`],
    [R`$\sqrt{n+1}-\sqrt n$ : quelle technique ?`, R`Quantité conjuguée : multiplier et diviser par $\sqrt{n+1}+\sqrt n$.`],
    [R`Théorème des gendarmes`, R`$v_n\leq u_n\leq w_n$ et $v_n,w_n\to\ell$ ⟹ $u_n\to\ell$.`],
    [R`$\lim q^n$ selon $q$`, R`$q>1$ : $+\infty$ ; $q=1$ : $1$ ; $-1<q<1$ : $0$ ; $q\leq-1$ : pas de limite.`],
    [R`$\lim(1+q+\dots+q^n)$ pour $|q|<1$`, R`$\frac{1}{1-q}$`],
    [R`Croissante et majorée ⟹ ?`, R`Converge (vers une limite $\leq$ le majorant).`],
    [R`Croissante non majorée ⟹ ?`, R`Tend vers $+\infty$.`],
    [R`Limite de $u_{n+1}=f(u_n)$ ?`, R`Si $u_n\to\ell$ et $f$ continue : $f(\ell)=\ell$.`],
    [R`Une suite bornée converge-t-elle ?`, R`Pas forcément : $(-1)^n$.`],
    [R`Algorithme de seuil : structure`, R`<code>while</code> condition non atteinte : <code>n = n+1</code>, mettre à jour <code>u</code> ; renvoyer <code>n</code>.`]
  ]
};
