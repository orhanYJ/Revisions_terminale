/* ---------- Chapitre 15 : concentration, loi des grands nombres ---------- */
var CH15 = {
  id: "ch15", num: 15, statut: "ok", partie: "Probabilités", titre: "Concentration, loi des grands nombres", court: "Loi des grands nombres",
  sous: "Pourquoi la moyenne d'un grand échantillon est proche de l'espérance : l'écart type mesure, Bienaymé-Tchebychev majore, la loi des grands nombres conclut.",
  resume: "Inégalité de Bienaymé-Tchebychev, inégalité de concentration, taille d'échantillon, loi des grands nombres.",
  essentiel: [
    R`<b>Inégalité de Bienaymé-Tchebychev</b> : pour toute variable $X$ d'espérance $\mu$ et de variance $V$, et tout $\delta>0$, $P(|X-\mu|\geq\delta)\leq\frac{V}{\delta^2}$.`,
    R`Avec $\delta=k\sigma$ : $P(|X-\mu|\geq k\sigma)\leq\frac1{k^2}$. Un écart de $2\sigma$ a une probabilité au plus $\frac14$, de $3\sigma$ au plus $\frac19$. L'inégalité est universelle, donc souvent grossière.`,
    R`<b>Inégalité de concentration</b> : pour la moyenne $M_n$ d'un échantillon de taille $n$, $P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}$.`,
    R`<b>Loi des grands nombres</b> : pour tout $\delta>0$, $\lim_{n\to+\infty}P(|M_n-\mu|\geq\delta)=0$. La moyenne d'un échantillon se rapproche de l'espérance ; la fréquence d'un événement, de sa probabilité.`,
    R`<b>Taille d'échantillon</b> : pour garantir $P(|M_n-\mu|\geq\delta)\leq\alpha$, il suffit que $\frac{V}{n\delta^2}\leq\alpha$, soit $n\geq\frac{V}{\alpha\delta^2}$.`
  ],
  attendus: [
    R`Appliquer l'inégalité de Bienaymé-Tchebychev pour définir une taille d'échantillon, en fonction de la précision et du risque choisis.`,
    R`Comprendre l'écart type comme unité naturelle de dispersion : des écarts de l'ordre de $\sigma$ sont normaux, des écarts de quelques $\sigma$ deviennent improbables.`,
    R`Savoir que l'inégalité est loin d'être optimale : elle donne une condition <b>suffisante</b>.`,
    R`Algorithmes : calculer $P(|S_n-pn|>\sqrt n)$ pour $S_n\sim\mathcal B(n,p)$ et comparer avec l'inégalité ; simuler une marche aléatoire ; simuler $N$ échantillons de taille $n$ et comparer l'écart type des moyennes à $\frac{\sigma}{\sqrt n}$.`,
    R`Aucune démonstration n'est exigible dans cette section ; celles qui figurent ici permettent de comprendre d'où vient la loi des grands nombres.`
  ],
  premiere: R`
<ul><li><b>Chapitre 14</b> : pour un échantillon de taille $n$, $E(M_n)=\mu$ et $V(M_n)=\frac Vn$, $\sigma(M_n)=\frac\sigma{\sqrt n}$.</li>
<li><b>Valeur absolue</b> : $|x-\mu|<\delta\iff\mu-\delta<x<\mu+\delta$ ; $|x-\mu|\geq\delta\iff x\leq\mu-\delta$ ou $x\geq\mu+\delta$.</li>
<li><b>Événement contraire</b> : $P(|X-\mu|<\delta)=1-P(|X-\mu|\geq\delta)$.</li>
<li><b>Seconde</b> : la fluctuation d'échantillonnage ; la fréquence observée sur un échantillon de taille $n$ s'écarte en général de $p$ de moins de $\frac1{\sqrt n}$.</li></ul>`,
  cours: [
    { id: "bt", titre: "L'inégalité de Bienaymé-Tchebychev", html: R`
[thm|Inégalité de Bienaymé-Tchebychev]Soit $X$ une variable aléatoire d'espérance $\mu$ et de variance $V$. Pour tout réel $\delta>0$ :
$$P(|X-\mu|\geq\delta)\leq\frac{V}{\delta^2}.$$
De façon équivalente, par passage au contraire : $P(|X-\mu|<\delta)\geq1-\frac{V}{\delta^2}$.[/]
<p><b>Ce que ça dit.</b> La variance contrôle la probabilité des grands écarts : plus $V$ est petit, moins $X$ a de chances de s'éloigner de sa moyenne. Et l'inégalité vaut pour <b>n'importe quelle</b> loi : on n'a besoin que de $\mu$ et $V$.</p>
[ex|Un dé]$\mu=3{,}5$, $V=\frac{35}{12}$. $P(|X-3{,}5|\geq2)\leq\frac{35/12}{4}=\frac{35}{48}\approx0{,}73$. En réalité, $|X-3{,}5|\geq2$ signifie $X\in\{1;6\}$ : probabilité $\frac13$. La majoration est vraie, mais large.[/]
[ex|Une loi binomiale]$X\sim\mathcal B(100;0{,}5)$ : $\mu=50$, $V=25$. $P(|X-50|\geq10)\leq\frac{25}{100}=0{,}25$, alors que le calcul exact donne environ $0{,}057$.[/]
<div data-anim="tchebychev"></div>
[ex|Un intervalle (bac, Amérique du Nord, 20 mai 2026)]Un prix $Z$ a pour espérance $9$ € et pour écart type $2$ €. « Il y a au moins $50\,\%$ de chances que le prix soit strictement compris entre $6$ et $12$ € » : $P(6<Z<12)=P(|Z-9|<3)\geq1-\frac{4}{9}=\frac59\approx0{,}56$. Affirmation justifiée.[/]
[meth|Utiliser l'inégalité]<ol><li>Identifie $\mu$ et $V$ (variance, pas écart type).</li><li>Écris l'événement sous la forme $|X-\mu|\geq\delta$ ou $|X-\mu|<\delta$ : l'intervalle doit être <b>centré</b> sur $\mu$.</li><li>Applique : $\leq\frac V{\delta^2}$, ou $\geq1-\frac V{\delta^2}$ pour le contraire.</li></ol>[/]` },
    { id: "ecarttype", titre: "L'écart type, unité naturelle de dispersion", html: R`
[prop|En nombre d'écarts types]Avec $\delta=k\sigma$ ($k>0$) : $P(|X-\mu|\geq k\sigma)\leq\frac{\sigma^2}{k^2\sigma^2}=\frac1{k^2}$.[/]
<div class="tab-wrap"><table><tr><th>Écart</th><th>Bienaymé-Tchebychev (toute loi)</th><th>$\mathcal B(100;0{,}5)$, calcul exact</th></tr>
<tr><td>$\geq\sigma$ ($\geq5$)</td><td>$\leq1$ : n'apprend rien</td><td>$\approx0{,}368$</td></tr>
<tr><td>$\geq2\sigma$ ($\geq10$)</td><td>$\leq0{,}25$</td><td>$\approx0{,}057$</td></tr>
<tr><td>$\geq3\sigma$ ($\geq15$)</td><td>$\leq0{,}111$</td><td>$\approx0{,}004$</td></tr></table></div>
<p>Le programme insiste : <b>des écarts de l'ordre de $\sigma$ sont normaux</b>, des écarts de quelques $\sigma$ deviennent improbables. L'inégalité garantit au plus $\frac14$ pour $2\sigma$, alors que pour beaucoup de lois rencontrées la probabilité réelle est de l'ordre de $0{,}05$. Le prix de l'universalité, c'est la grossièreté de la borne.</p>
[piege|Une borne au-dessus de $1$]Si $\delta\leq\sigma$, alors $\frac V{\delta^2}\geq1$ : l'inégalité est vraie mais n'apporte rien (une probabilité est toujours $\leq1$).[/]` },
    { id: "concentration", titre: "L'inégalité de concentration", html: R`
[thm|Inégalité de concentration]Soit $M_n$ la moyenne d'un échantillon de taille $n$ d'une variable aléatoire d'espérance $\mu$ et de variance $V$. Pour tout $\delta>0$ :
$$P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}.$$[/]
<p><b>D'où ça vient.</b> C'est Bienaymé-Tchebychev appliquée à $M_n$, dont l'espérance est $\mu$ et la variance $\frac Vn$ (chapitre 14). Le $n$ au dénominateur dit tout : à précision $\delta$ fixée, la borne tend vers $0$ quand $n$ grandit.</p>
<div data-anim="lgn"></div>
[ex|La moyenne de $100$ lancers de dé]$P(|M_{100}-3{,}5|\geq0{,}5)\leq\frac{35/12}{100\times0{,}25}\approx0{,}117$ : il y a au moins $88\,\%$ de chances que la moyenne de $100$ lancers soit strictement comprise entre $3$ et $4$.[/]
[ex|Fréquence d'un événement]Si $X_i$ suit la loi de Bernoulli de paramètre $p$, $M_n=F_n$ est la fréquence des succès, $\mu=p$, $V=p(1-p)\leq\frac14$. Donc $P(|F_n-p|\geq\delta)\leq\frac{p(1-p)}{n\delta^2}\leq\frac1{4n\delta^2}$, quelle que soit la valeur (inconnue) de $p$.[/]` },
    { id: "taille", titre: "Choisir une taille d'échantillon", html: R`
[meth|Taille suffisante pour une précision $\delta$ et un risque $\alpha$]On veut $P(|M_n-\mu|\geq\delta)\leq\alpha$, ou, ce qui revient au même, $P(|M_n-\mu|<\delta)\geq1-\alpha$. Il <b>suffit</b> que $\frac{V}{n\delta^2}\leq\alpha$, c'est-à-dire
$$n\geq\frac{V}{\alpha\delta^2}.$$
On prend le plus petit entier qui convient. C'est une condition suffisante : une taille plus petite peut convenir aussi, l'inégalité ne permet simplement pas de l'affirmer.[/]
<div data-w="concentration"></div>
[ex|Un sondage]Estimer une proportion à $\delta=0{,}05$ près avec un risque $\alpha=0{,}05$ : $\frac{p(1-p)}{n\times0{,}0025}\leq\frac{0{,}25}{0{,}0025\,n}\leq0{,}05$ dès que $n\geq2\,000$. Le calcul exact avec la loi binomiale (pour $p=0{,}5$) montre que $n=1\,000$ donne déjà une probabilité d'écart d'environ $0{,}002$ : la garantie de Bienaymé-Tchebychev est prudente.[/]
[ex|Bac, Métropole, 16 juin 2026]$E(M_n)=120$, $V(M_n)=\frac{1\,728}n$. On veut $P(114<M_n<126)\geq0{,}85$, c'est-à-dire $P(|M_n-120|<6)\geq0{,}85$. L'inégalité donne $P(|M_n-120|<6)\geq1-\frac{1\,728}{36n}=1-\frac{48}n$. Il suffit que $1-\frac{48}n\geq0{,}85$, soit $\frac{48}n\leq0{,}15$, $n\geq320$. Plus petit entier : $n=320$ familles.[/]
[ex|Bac, Métropole, 17 juin 2025]$E(M_N)=7{,}14$, $V(M_N)=\frac{6{,}63}N$ ; on veut $P(7<M_N<7{,}28)\geq0{,}95$, soit $P(|M_N-7{,}14|<0{,}14)\geq0{,}95$. Il suffit que $\frac{6{,}63}{N\times0{,}14^2}\leq0{,}05$, soit $N\geq\frac{6{,}63}{0{,}05\times0{,}0196}\approx6\,765{,}3$ : $N=6\,766$.[/]` },
    { id: "lgn", titre: "La loi des grands nombres", html: R`
[thm|Loi (faible) des grands nombres]Soit $M_n$ la moyenne d'un échantillon de taille $n$ d'une variable aléatoire d'espérance $\mu$. Pour tout réel $\delta>0$ :
$$\lim_{n\to+\infty}P(|M_n-\mu|\geq\delta)=0.$$[/]
<p><b>Lecture.</b> Aussi petite que soit la précision $\delta$ choisie, la probabilité que la moyenne de l'échantillon s'écarte de $\mu$ d'au moins $\delta$ tend vers $0$. Appliquée aux fréquences : la fréquence d'apparition d'un événement dans $n$ répétitions indépendantes se rapproche de sa probabilité. C'est ce qui justifie l'estimation d'une probabilité par une fréquence, les sondages, et toutes les simulations de ce site.</p>
[ex|Une pièce équilibrée]Avec $n=10\,000$ lancers, $P(|F_n-0{,}5|\geq0{,}01)\leq\frac{0{,}25}{10\,000\times0{,}0001}=0{,}25$ (calcul exact : environ $0{,}047$) ; avec $n=1\,000\,000$, la borne devient $0{,}0025$.[/]
[piege|La « loi des séries » n'existe pas]Après dix « pile », la pièce n'a pas « besoin » de faire « face » : les lancers sont indépendants, la probabilité reste $\frac12$. La loi des grands nombres ne dit pas que les écarts se <b>compensent</b> : l'écart absolu $S_n-np$ est typiquement de l'ordre de $\sqrt n$, il peut grandir ; c'est l'écart <b>relatif</b> $\frac{S_n}n-p$, de l'ordre de $\frac1{\sqrt n}$, qui tend vers $0$.[/]
[hist|Le « théorème d'or »]Jacques Bernoulli démontre la loi des grands nombres pour les fréquences dans l'<i>Ars Conjectandi</i> (1713), qu'il appelait son « théorème d'or ». Bienaymé (1853, publication en 1867) puis Tchebychev (1867) établissent l'inégalité qui porte leurs noms ; elle donne une démonstration bien plus simple de la loi des grands nombres.[/]
<p><span class="tag hp">Pour aller plus loin</span> Exemples du programme : un sondage ($n=1\,000$), le rapport de masculinité à la naissance ($n=10^6$), la demi-vie d'atomes radioactifs ($n\approx10^{23}$ atomes : la proportion désintégrée au bout d'une demi-vie est si concentrée autour de $\frac12$ que la décroissance paraît parfaitement régulière).</p>` }
  ],
  pieges: [
    { t: "Variance, pas écart type", h: R`Le numérateur est $V$ ($=\sigma^2$). Avec $\sigma=2$ et $\delta=3$ : $\frac4{9}$, pas $\frac29$.` },
    { t: "$\\delta$ au carré", h: R`$P(|X-\mu|\geq\delta)\leq\frac V{\delta^2}$ : on divise par $\delta^2$. Pour la moyenne, par $n\delta^2$.` },
    { t: "L'intervalle doit être centré sur $\\mu$", h: R`$P(114<M_n<126)$ se traite car $120$ est au milieu. Pour un intervalle non centré, on se ramène à un intervalle centré contenu dedans (ce qui donne une minoration).` },
    { t: "Strict ou large", h: R`Le contraire de $|X-\mu|\geq\delta$ est $|X-\mu|<\delta$, soit $\mu-\delta<X<\mu+\delta$ (inégalités <b>strictes</b>).` },
    { t: "Une taille suffisante, pas nécessaire", h: R`L'inégalité donne un $n$ qui <b>suffit</b>. Elle ne dit pas qu'un $n$ plus petit ne convient pas.` },
    { t: "La loi des grands nombres ne compense pas", h: R`Elle parle d'une probabilité qui tend vers $0$, pour la moyenne. Elle ne dit pas qu'après une série de « pile », « face » devient plus probable.` }
  ],
  demos: [
    { bo: false, t: "L'inégalité de Bienaymé-Tchebychev (pour une variable finie)", h: R`
<p>Soit $X$ de valeurs $x_1,\dots,x_m$, de probabilités $p_1,\dots,p_m$. Par définition, $V=\sum_i(x_i-\mu)^2p_i$. Tous les termes sont positifs ; on n'en garde que ceux pour lesquels $|x_i-\mu|\geq\delta$ :
$$V\geq\sum_{|x_i-\mu|\geq\delta}(x_i-\mu)^2p_i\geq\sum_{|x_i-\mu|\geq\delta}\delta^2p_i=\delta^2P(|X-\mu|\geq\delta).$$
En divisant par $\delta^2>0$ : $P(|X-\mu|\geq\delta)\leq\frac V{\delta^2}$. CQFD.</p>
<p class="stylo">Toute la preuve tient en une idée : les grands écarts « coûtent » au moins $\delta^2$ chacun dans la variance.</p>` },
    { bo: false, t: "De Bienaymé-Tchebychev à l'inégalité de concentration", h: R`
<p>Par le chapitre 14, $E(M_n)=\mu$ et $V(M_n)=\frac Vn$ (linéarité de l'espérance, indépendance des $X_i$). On applique Bienaymé-Tchebychev à la variable $M_n$ :
$$P(|M_n-\mu|\geq\delta)\leq\frac{V(M_n)}{\delta^2}=\frac{V}{n\delta^2}.$$</p>` },
    { bo: false, t: "De l'inégalité de concentration à la loi des grands nombres", h: R`
<p>Soit $\delta>0$ fixé. Pour tout $n\geq1$ : $0\leq P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}$. Or $\frac{V}{\delta^2}$ est une constante et $\lim_{n\to+\infty}\frac1n=0$, donc le majorant tend vers $0$. Par le théorème des gendarmes (chapitre 2), $\lim_{n\to+\infty}P(|M_n-\mu|\geq\delta)=0$. CQFD.</p>` }
  ],
  algos: [
    { bo: true, t: "$P(|S_n-pn|>\\sqrt n)$ comparée à Bienaymé-Tchebychev", code: `from math import comb, sqrt

def proba_ecart(n, p):
    # P(|S_n - pn| > sqrt(n)) pour S_n de loi B(n, p)
    return sum(comb(n, k) * p**k * (1 - p)**(n - k)
               for k in range(n + 1) if abs(k - p*n) > sqrt(n))

for n, p in [(100, 0.5), (1000, 0.5), (100, 0.2), (1000, 0.3)]:
    print(n, p, round(proba_ecart(n, p), 4), "borne :", round(p*(1 - p), 4))`, sortie: `100 0.5 0.0352 borne : 0.25
1000 0.5 0.0463 borne : 0.25
100 0.2 0.0084 borne : 0.16
1000 0.3 0.0297 borne : 0.21`,
      apres: R`<p>Avec $\delta=\sqrt n$ et $V(S_n)=np(1-p)$, l'inégalité donne $\frac{np(1-p)}n=p(1-p)$. La vraie probabilité est bien plus petite : la borne est vraie mais grossière, comme le dit le programme.</p>` },
    { bo: true, t: "Simulation d'une marche aléatoire", code: `from random import random, seed

def marche(n):
    x = 0
    positions = [0]
    for i in range(n):
        x = x + (1 if random() < 0.5 else -1)   # un pas à droite ou à gauche
        positions.append(x)
    return positions

seed(3)
P = marche(10000)
for n in [100, 1000, 10000]:
    print(n, P[n], P[n] / n)`, sortie: `100 -14 -0.14
1000 18 0.018
10000 108 0.0108`,
      apres: R`<p>La position $X_n$ (somme de $n$ pas $\pm1$) s'éloigne de $0$ de l'ordre de $\sqrt n$, mais la position moyenne par pas $\frac{X_n}n$ tend vers $0$ : c'est la loi des grands nombres. (Une autre graine donne d'autres valeurs, du même ordre de grandeur.)</p>` },
    { bo: true, t: "Simuler $N$ échantillons et comparer à $\\frac{\\sigma}{\\sqrt n}$", code: `from random import randint, seed
from math import sqrt

seed(15)
N, n = 1000, 100
moyennes = []
for j in range(N):
    moyennes.append(sum(randint(1, 6) for i in range(n)) / n)

m = sum(moyennes) / N
s = sqrt(sum((x - m)**2 for x in moyennes) / N)
print(round(m, 3), round(s, 4), round(sqrt(35 / 12) / sqrt(n), 4))
for k in [1, 2, 3]:
    dedans = sum(1 for x in moyennes if abs(x - 3.5) <= k * s)
    print(k, dedans / N)`, sortie: `3.5 0.1684 0.1708
1 0.682
2 0.948
3 0.996`,
      apres: R`<p>$1\,000$ échantillons de $100$ lancers de dé : l'écart type observé des moyennes ($\approx0{,}168$) est très proche de $\frac{\sigma}{\sqrt n}\approx0{,}171$. Environ $68\,\%$, $95\,\%$ et $99{,}6\,\%$ des moyennes sont à moins de $s$, $2s$, $3s$ de $3{,}5$ : bien mieux que les garanties $0$, $\frac34$, $\frac89$ de Bienaymé-Tchebychev.</p>` }
  ],
  methodes: [
    { t: "Majorer ou minorer une probabilité avec Bienaymé-Tchebychev", h: R`
<ol><li>Calcule (ou lis) $\mu=E(X)$ et $V=V(X)$.</li><li>Ramène l'événement à $|X-\mu|\geq\delta$ (majoration) ou à $|X-\mu|<\delta$ (minoration) ; vérifie que l'intervalle est centré sur $\mu$.</li><li>Écris l'inégalité avec les valeurs, puis conclus en une phrase dans le contexte.</li></ol>` },
    { t: "Trouver une taille d'échantillon", h: R`
<ol><li>Écris $E(M_n)=\mu$ et $V(M_n)=\frac Vn$ (souvent la question précédente).</li><li>Traduis l'énoncé : $P(a<M_n<b)\geq1-\alpha$ avec $\mu=\frac{a+b}2$ et $\delta=\frac{b-a}2$.</li><li>Inégalité de concentration : $P(|M_n-\mu|<\delta)\geq1-\frac V{n\delta^2}$. Il suffit que $1-\frac V{n\delta^2}\geq1-\alpha$, soit $n\geq\frac{V}{\alpha\delta^2}$.</li><li>Prends le plus petit entier, et interprète (« au moins … personnes »).</li></ol>` },
    { t: "Interpréter la loi des grands nombres", h: R`
<p>Phrase type : « quand la taille de l'échantillon augmente, la probabilité que la moyenne observée s'écarte de l'espérance de plus de $\delta$ tend vers $0$ ; pour un grand échantillon, la moyenne observée est donc très probablement proche de $\mu$ ».</p>` }
  ],
  exos: [
    { niv: 1, t: "Appliquer l'inégalité", enonce: R`<p>$X$ est une variable aléatoire d'espérance $20$ et de variance $4$.</p><ol><li>Majorer $P(|X-20|\geq5)$.</li><li>Minorer $P(16<X<24)$.</li><li>Pourquoi l'inégalité n'apporte-t-elle rien pour $P(|X-20|\geq1)$ ?</li></ol>`,
      corrige: R`<ol><li>$P(|X-20|\geq5)\leq\frac4{25}=0{,}16$.</li><li>$P(16<X<24)=P(|X-20|<4)\geq1-\frac4{16}=0{,}75$.</li><li>$\frac4{1^2}=4>1$ : la majoration est vraie mais inutile (ici $\delta=1<\sigma=2$).</li></ol>` },
    { niv: 1, t: "Comparer avec la valeur exacte", enonce: R`<p>$X\sim\mathcal B(40;0{,}5)$.</p><ol><li>Donner $E(X)$ et $V(X)$.</li><li>Majorer $P(|X-20|\geq6)$ par l'inégalité de Bienaymé-Tchebychev.</li><li>Calculer cette probabilité avec la calculatrice et comparer.</li></ol>`,
      corrige: R`<ol><li>$E(X)=20$, $V(X)=10$.</li><li>$P(|X-20|\geq6)\leq\frac{10}{36}\approx0{,}278$.</li><li>$P(|X-20|\geq6)=P(X\leq14)+P(X\geq26)=2P(X\leq14)\approx2\times0{,}0403=0{,}081$ (symétrie de $\mathcal B(40;0{,}5)$). La borne est environ $3{,}4$ fois trop grande.</li></ol>` },
    { niv: 2, t: "Combien de lancers ?", enonce: R`<p>On lance $n$ fois une pièce supposée équilibrée et l'on note $F_n$ la fréquence de « pile ».</p><ol><li>Donner $E(F_n)$ et $V(F_n)$.</li><li>Déterminer une taille $n$ pour laquelle l'inégalité de concentration garantit $P(0{,}45<F_n<0{,}55)\geq0{,}9$.</li><li>Même question avec l'intervalle $]0{,}49;0{,}51[$.</li></ol>`,
      corrige: R`<ol><li>$F_n$ est la moyenne de $n$ variables de Bernoulli de paramètre $0{,}5$ : $E(F_n)=0{,}5$, $V(F_n)=\frac{0{,}25}n$.</li><li>$P(|F_n-0{,}5|<0{,}05)\geq1-\frac{0{,}25}{n\times0{,}0025}=1-\frac{100}n$. Il suffit que $\frac{100}n\leq0{,}1$ : $n\geq1\,000$.</li><li>$1-\frac{0{,}25}{n\times0{,}0001}=1-\frac{2\,500}n\geq0{,}9\iff n\geq25\,000$. Diviser la précision par $5$ multiplie la taille par $25$.</li></ol>` },
    { niv: 2, t: "Un contrôle de remplissage", enonce: R`<p>Une machine remplit des bouteilles ; le volume (en mL) d'une bouteille est une variable d'espérance $500$ et d'écart type $4$. On prélève $n$ bouteilles (volumes indépendants) et l'on note $M_n$ le volume moyen.</p><ol><li>Pour $n=1$ : minorer la probabilité qu'une bouteille contienne entre $490$ et $510$ mL (bornes exclues).</li><li>Pour $n=25$ : minorer $P(498<M_{25}<502)$.</li><li>Quelle taille $n$ garantit, par l'inégalité de concentration, $P(499<M_n<501)\geq0{,}95$ ?</li></ol>`,
      corrige: R`<ol><li>$V=16$ : $P(|X-500|<10)\geq1-\frac{16}{100}=0{,}84$.</li><li>$V(M_{25})=\frac{16}{25}=0{,}64$ : $P(|M_{25}-500|<2)\geq1-\frac{0{,}64}4=0{,}84$.</li><li>$1-\frac{16}{n\times1}\geq0{,}95\iff\frac{16}n\leq0{,}05\iff n\geq320$.</li></ol>` },
    { niv: 3, t: "Erreurs détectées (type bac)", enonce: R`<p>Un logiciel contrôle des transactions ; chaque contrôle détecte une anomalie avec la probabilité $p=0{,}15$, indépendamment des autres. Une journée comporte $20$ contrôles ; $X$ est le nombre d'anomalies détectées dans la journée.</p><ol><li>Justifier que $X$ suit une loi binomiale ; donner $E(X)$ et $V(X)$.</li><li>Minorer $P(0<X<6)$ à l'aide de l'inégalité de Bienaymé-Tchebychev, puis comparer avec la valeur exacte donnée par la calculatrice.</li><li>On observe $n$ journées indépendantes, de nombres d'anomalies $X_1$, …, $X_n$, et l'on note $M_n$ leur moyenne. Donner $E(M_n)$ et $V(M_n)$.</li><li>Déterminer le plus petit $n$ pour lequel l'inégalité de concentration garantit $P(2{,}5<M_n<3{,}5)\geq0{,}99$.</li><li>Interpréter avec la loi des grands nombres.</li></ol>`,
      corrige: R`<ol><li>$20$ répétitions identiques et indépendantes d'une épreuve à deux issues, succès « anomalie » de probabilité $0{,}15$ : $X\sim\mathcal B(20;0{,}15)$, $E(X)=3$, $V(X)=20\times0{,}15\times0{,}85=2{,}55$.</li><li>$P(0<X<6)=P(|X-3|<3)\geq1-\frac{2{,}55}9\approx0{,}717$. Valeur exacte : $P(1\leq X\leq5)=P(X\leq5)-P(X=0)\approx0{,}894$ : la minoration est juste, mais prudente.</li><li>$E(M_n)=3$, $V(M_n)=\frac{2{,}55}n$.</li><li>$P(|M_n-3|<0{,}5)\geq1-\frac{2{,}55}{0{,}25n}=1-\frac{10{,}2}n$. Il suffit que $\frac{10{,}2}n\leq0{,}01$, soit $n\geq1\,020$ : $n=1\,020$ journées.</li><li>Quand $n$ augmente, la probabilité que le nombre moyen d'anomalies par jour s'écarte de $3$ d'au moins $0{,}5$ tend vers $0$ : sur un grand nombre de journées, la moyenne observée sera très probablement proche de $3$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole, 16 juin 2026 (sujet 1), exercice 1, partie B, question 3b", url: "https://www.apmep.fr/IMG/pdf/BAC_General_Specialite_Sujet_J1_metropole_FK-v2.pdf", h: R`Plus petit $n$ pour lequel l'inégalité de Bienaymé-Tchebychev permet d'affirmer $P(114<M_n<126)\geq0{,}85$ : $n=320$ (corrigé dans la partie 4).` },
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 1, question 6d", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Plus petite valeur de $N$ telle que l'inégalité garantisse $P(7<M_N<7{,}28)\geq0{,}95$ : $N=6\,766$.` },
    { ref: "Bac 2026, Amérique du Nord, 20 mai 2026 (sujet 1), exercice 1, partie C, question 5", url: "https://www.apmep.fr/IMG/pdf/Amerique_du_Nord_J1_spe_20_05_2026_FK.pdf", h: R`Espérance $9$, écart type $2$ : justifier qu'il y a au moins $50\,\%$ de chances que le prix soit strictement compris entre $6$ et $12$ (minoration $\frac59$).` },
    { ref: "Bac 2025, Centres étrangers, 12 juin 2025 (sujet 1), exercice 1, partie C", url: "https://www.apmep.fr/IMG/pdf/Etranger_spe_J1_12_06_2025_DV.pdf", h: R`Somme de trois variables binomiales indépendantes $\mathcal B(20;0{,}165)$ : $E(S)=9{,}9$, $V(S)=8{,}2665$, puis, en prenant $10$ comme valeur de $E(S)$ comme le demande l'énoncé, $P(6<S<14)\geq1-\frac{8{,}2665}{16}\approx0{,}483>0{,}48$.` }
  ],
  retenir: R`
[thm|Bienaymé-Tchebychev]$P(|X-\mu|\geq\delta)\leq\frac{V}{\delta^2}$ ; $P(|X-\mu|<\delta)\geq1-\frac V{\delta^2}$. Avec $\delta=k\sigma$ : $\leq\frac1{k^2}$.[/]
[thm|Concentration]$M_n$ moyenne d'un échantillon de taille $n$ : $P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}$.[/]
[thm|Loi des grands nombres]Pour tout $\delta>0$, $\lim_{n\to+\infty}P(|M_n-\mu|\geq\delta)=0$.[/]
[meth|Taille d'échantillon]Précision $\delta$, risque $\alpha$ : il suffit que $n\geq\frac{V}{\alpha\delta^2}$. Intervalle $]a;b[$ : $\mu=\frac{a+b}2$, $\delta=\frac{b-a}2$.[/]
<p class="stylo">Variance au numérateur, $\delta^2$ (et $n$) au dénominateur. La borne est vraie pour toute loi, donc souvent large : elle donne une taille <b>suffisante</b>.</p>`,
  qcm: [
    { q: R`$E(X)=10$, $V(X)=4$. Bienaymé-Tchebychev donne $P(|X-10|\geq4)\leq$`, c: ["$1$", "$\\frac14$", "$\\frac12$", "$\\frac1{16}$"], r: 1, e: R`$\frac{V}{\delta^2}=\frac4{16}$.`, ref: "bt" },
    { q: R`$E(X)=10$, $\sigma(X)=3$. $P(4<X<16)\geq$`, c: [R`$\frac14$`, R`$\frac34$`, R`$\frac12$`, R`$\frac23$`], r: 1, e: R`$P(|X-10|<6)\geq1-\frac9{36}=\frac34$.`, ref: "bt" },
    { q: R`Selon l'inégalité, la probabilité d'un écart d'au moins $3\sigma$ est au plus :`, c: [R`$\frac13$`, R`$\frac19$`, R`$0{,}05$`, R`$\frac1{27}$`], r: 1, e: R`$\frac1{k^2}$ avec $k=3$.`, ref: "ecarttype" },
    { q: R`Pour $\delta<\sigma$, l'inégalité de Bienaymé-Tchebychev :`, c: ["est fausse", "est vraie mais n'apprend rien", "donne une probabilité nulle", "ne s'applique pas aux lois binomiales"], r: 1, e: R`La borne $\frac V{\delta^2}$ dépasse $1$.`, ref: "ecarttype" },
    { q: R`L'inégalité de concentration s'écrit :`, c: [R`$P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}$`, R`$P(|M_n-\mu|\geq\delta)\leq\frac{V}{\delta^2}$`, R`$P(|M_n-\mu|\geq\delta)\leq\frac{nV}{\delta^2}$`, R`$P(|M_n-\mu|\geq\delta)\geq\frac{V}{n\delta^2}$`], r: 0, e: R`Bienaymé-Tchebychev appliquée à $M_n$, de variance $\frac Vn$.`, ref: "concentration" },
    { q: R`Pour une fréquence $F_n$ (paramètre $p$ inconnu), $V(F_n)$ est au plus :`, c: [R`$\frac1n$`, R`$\frac1{4n}$`, R`$\frac14$`, R`$\frac1{2n}$`], r: 1, e: R`$p(1-p)\leq\frac14$ pour tout $p\in[0;1]$.`, ref: "concentration" },
    { q: R`On veut $P(|M_n-\mu|\geq\delta)\leq\alpha$. L'inégalité de concentration dit qu'il suffit que :`, c: [R`$n\geq\frac{V}{\alpha\delta^2}$`, R`$n\leq\frac{V}{\alpha\delta^2}$`, R`$n\geq\frac{\alpha\delta^2}{V}$`, R`$n\geq\frac{V}{\delta}$`], r: 0, e: R`$\frac V{n\delta^2}\leq\alpha\iff n\geq\frac V{\alpha\delta^2}$.`, ref: "taille" },
    { q: R`$V(M_n)=\frac{1\,728}n$. Plus petit $n$ pour garantir $P(114<M_n<126)\geq0{,}85$ (moyenne $120$) :`, c: ["$48$", "$320$", "$1\\,152$", "$12$"], r: 1, e: R`$\frac{1\,728}{36n}\leq0{,}15\iff n\geq320$ (bac, juin 2026).`, ref: "taille" },
    { q: R`Diviser par $2$ la précision $\delta$ multiplie la taille garantie par :`, c: ["$2$", "$4$", "$\\sqrt2$", "$8$"], r: 1, e: R`$n\geq\frac V{\alpha\delta^2}$ : $\delta^2$ est divisé par $4$.`, ref: "taille" },
    { q: R`La loi des grands nombres affirme que, pour tout $\delta>0$ :`, c: [R`$M_n=\mu$ pour $n$ assez grand`, R`$P(|M_n-\mu|\geq\delta)$ tend vers $0$`, R`$P(|M_n-\mu|\geq\delta)=0$ pour $n\geq100$`, R`les écarts se compensent`], r: 1, e: R`C'est une affirmation sur une probabilité qui tend vers $0$.`, ref: "lgn" },
    { q: R`Après $10$ « pile » d'affilée avec une pièce équilibrée, la probabilité de « face » au lancer suivant est :`, c: ["plus grande que $\\frac12$", "$\\frac12$", "plus petite que $\\frac12$", "$1$"], r: 1, e: R`Les lancers sont indépendants : pas de « loi des séries ».`, ref: "lgn" },
    { q: R`Quand $n$ grandit, l'écart $S_n-np$ (nombre de succès moins sa moyenne) :`, c: ["tend vers $0$", "est typiquement de l'ordre de $\\sqrt n$", "est toujours nul", "est de l'ordre de $n$"], r: 1, e: R`$\sigma(S_n)=\sqrt{np(1-p)}$ ; c'est $\frac{S_n}n-p$ qui tend vers $0$.`, ref: "lgn" },
    { q: R`Dans $P(|X-\mu|\geq\delta)\leq\frac{V}{\delta^2}$, on met au numérateur :`, c: ["l'écart type", "la variance", "l'espérance", "$n$"], r: 1, e: R`La variance $V=\sigma^2$.`, ref: "pieges" },
    { q: R`Qui a appelé la loi des grands nombres son « théorème d'or » ?`, c: ["Tchebychev", "Jacques Bernoulli", "Bienaymé", "Galton"], r: 1, e: R`Dans l'<i>Ars Conjectandi</i> (1713).`, ref: "lgn" }
  ],
  cartes: [
    [R`Inégalité de Bienaymé-Tchebychev`, R`$P(|X-\mu|\geq\delta)\leq\frac{V}{\delta^2}$`],
    [R`Forme « minoration »`, R`$P(|X-\mu|<\delta)\geq1-\frac{V}{\delta^2}$`],
    [R`Écart d'au moins $k\sigma$`, R`Probabilité au plus $\frac1{k^2}$.`],
    [R`Inégalité de concentration`, R`$P(|M_n-\mu|\geq\delta)\leq\frac{V}{n\delta^2}$`],
    [R`Loi des grands nombres`, R`$\forall\delta>0$, $\lim_{n\to+\infty}P(|M_n-\mu|\geq\delta)=0$`],
    [R`Taille d'échantillon suffisante`, R`$n\geq\frac{V}{\alpha\delta^2}$`],
    [R`$P(a<M_n<b)$ : $\mu$ et $\delta$`, R`$\mu=\frac{a+b}2$, $\delta=\frac{b-a}2$`],
    [R`Variance d'une fréquence $F_n$`, R`$\frac{p(1-p)}n\leq\frac1{4n}$`],
    [R`Pourquoi la borne est-elle souvent large ?`, R`Elle vaut pour toutes les lois : c'est le prix de l'universalité.`],
    [R`Ordre de grandeur de $S_n-np$`, R`$\sqrt n$ (et $\frac{S_n}n-p$ : $\frac1{\sqrt n}$)`],
    [R`Démontrer la loi des grands nombres`, R`Inégalité de concentration + théorème des gendarmes.`],
    [R`Bienaymé, Tchebychev`, R`1853 (publié en 1867) et 1867.`],
    [R`« Théorème d'or »`, R`Jacques Bernoulli, Ars Conjectandi, 1713.`],
    [R`Sondage : précision $0{,}05$, risque $0{,}05$`, R`Bienaymé-Tchebychev garantit avec $n\geq2\,000$.`]
  ]
};

/* Interactif : borne de Bienaymé-Tchebychev contre probabilité exacte, pour une fréquence */
WIDGETS.concentration = function (el) {
  var c = WPB.cadre(el, "La borne et la vraie probabilité", "graphe");
  var n = WPB.curseur(c.ctrl, "Taille de l'échantillon n", 10, 1000, 10, 100, function (v) { return v; });
  var p = WPB.curseur(c.ctrl, "Probabilité p", 0.05, 0.95, 0.05, 0.5);
  var d = WPB.curseur(c.ctrl, "Précision δ", 0.01, 0.2, 0.01, 0.05);
  function loi(N, P) {
    var L = new Array(N + 1), lc = 0, lp = Math.log(P), lq = Math.log(1 - P);
    for (var k = 0; k <= N; k++) { L[k] = Math.exp(lc + k * lp + (N - k) * lq); lc += Math.log(N - k) - Math.log(k + 1); }
    return L;
  }
  function maj() {
    var N = +n.value, P = +p.value, D = +d.value, L = loi(N, P), hors = 0, ymax = 0;
    L.forEach(function (v, k) { if (Math.abs(k / N - P) >= D - 1e-12) hors += v; if (v > ymax) ymax = v; });
    var borne = P * (1 - P) / (N * D * D);
    var W = 360, H = 200, ml = 12, mr = 12, mt = 26, mb = 22, svg = WPB.N("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Loi de la fréquence" });
    c.scene.innerHTML = ""; c.scene.appendChild(svg);
    var X = function (f) { return ml + f * (W - ml - mr); }, Y = function (y) { return H - mb - y / (ymax * 1.1) * (H - mt - mb); };
    WPB.N("rect", { x: X(Math.max(0, P - D)), y: mt - 4, width: X(Math.min(1, P + D)) - X(Math.max(0, P - D)), height: H - mb - mt + 4, "class": "g-bande" }, svg);
    WPB.N("line", { x1: ml, x2: W - mr, y1: Y(0), y2: Y(0), "class": "g-axe" }, svg);
    [0, 0.25, 0.5, 0.75, 1].forEach(function (f) { var t = WPB.N("text", { x: X(f), y: H - mb + 15, "text-anchor": "middle", "class": "g-txt" }, svg); t.textContent = WPB.nf(f, 2); });
    var w = Math.max(1, (W - ml - mr) / (N + 1) * 0.8);
    L.forEach(function (v, k) {
      if (v < ymax * 1e-3) return;
      var dehors = Math.abs(k / N - P) >= D - 1e-12;
      WPB.N("rect", { x: X(k / N) - w / 2, y: Y(v), width: w, height: Y(0) - Y(v), style: "fill:" + (dehors ? "var(--rouge)" : "var(--bleu)") + ";fill-opacity:" + (dehors ? 0.9 : 0.5) }, svg);
    });
    var t2 = WPB.N("text", { x: ml, y: 16, "class": "g-lab b" }, svg); t2.textContent = "loi de la fréquence F (n = " + N + ")";
    var nmin = Math.ceil(P * (1 - P) / (0.05 * D * D) - 1e-9);
    c.note.innerHTML = TeX.fmt("Bande jaune : $|F-p|<\\delta$. Barres rouges : les écarts d'au moins $\\delta$. Probabilité exacte $P(|F-p|\\geq" + WPB.nf(D, 2) + ")\\approx" + WPB.nf(hors, 4) + "$ ; borne de Bienaymé-Tchebychev $\\frac{p(1-p)}{n\\delta^2}\\approx" + WPB.nf(borne, 4) + "$" + (borne >= 1 ? " (au moins $1$ : elle n'apprend rien)" : "") + ". Pour un risque de $5\\,\\%$, l'inégalité garantit le résultat dès $n\\geq" + nmin + "$.");
  }
  [n, p, d].forEach(function (i) { i.addEventListener("input", maj); });
  maj();
};

/* Animation : des fréquences qui se stabilisent (trajectoires fixées) */
ANIMS.lgn = {
  titre: "La fréquence de « pile » se stabilise",
  vb: [360, 260],
  etapes: [
    { d: 4.5, l: R`On lance une pièce équilibrée et l'on trace la fréquence $F_n$ de « pile » après $n$ lancers. Au début, elle saute beaucoup : un seul lancer la fait passer de $0$ à $1$.` },
    { d: 5, l: R`Trente séries de $500$ lancers, indépendantes : toutes les trajectoires finissent par se serrer autour de $0{,}5$.` },
    { d: 4.5, l: R`La bande $]0{,}45;0{,}55[$ : à $n=50$, beaucoup de trajectoires en sont encore dehors ; à $n=500$, presque aucune. C'est la loi des grands nombres.` },
    { d: 5, l: R`Le « goulot » $0{,}5\pm\frac{1}{\sqrt n}$ (deux écarts types de $F_n$, car $\sigma(F_n)=\frac{0{,}5}{\sqrt n}$) se resserre comme $\frac1{\sqrt n}$ et contient presque toutes les trajectoires.` },
    { d: 4.5, l: R`Bienaymé-Tchebychev garantit $P(|F_n-0{,}5|\geq0{,}05)\leq\frac{0{,}25}{n\times0{,}0025}=\frac{100}n$ : rien à $n=50$, au plus $0{,}2$ à $n=500$. La garantie est prudente, la réalité bien meilleure.` }
  ],
  _traj: null,
  rendu: function (S, k, t) {
    var A = ANIMS.lgn, NT = 30, NL = 500, E = ANIM.e;
    if (!A._traj) {
      var g = 1713 >>> 0, alea = function () { g = (g * 1664525 + 1013904223) >>> 0; return g / 4294967296; };
      A._traj = [];
      for (var j = 0; j < NT; j++) { var s = 0, f = []; for (var i = 1; i <= NL; i++) { s += alea() < 0.5 ? 1 : 0; f.push(s / i); } A._traj.push(f); }
    }
    S.rep(0, NL, 0, 1, { px: 100, py: 0.25, fy: function (v) { return ANIM.nf(v, 2); } });
    var bande = k >= 2;
    if (bande) S.rect(0, 0.45, NL, 0.55, "g-bande", { opacity: k === 2 ? E(ANIM.p(t, 0, 0.3)) : 1 });
    var nb = k === 0 ? 1 : NT, fin = k === 0 ? Math.max(2, Math.round(NL * E(t))) : k === 1 ? Math.max(2, Math.round(NL * E(t))) : NL;
    for (var j2 = 0; j2 < nb; j2++) {
      var f2 = A._traj[j2], pts = [];
      for (var i2 = 1; i2 <= fin; i2 += (i2 < 40 ? 1 : 3)) pts.push([i2, f2[i2 - 1]]);
      pts.push([fin, f2[fin - 1]]);
      S.poly(pts, j2 === 0 ? "g-c2" : "g-c", false, { "stroke-width": j2 === 0 ? 1.8 : 0.9, opacity: j2 === 0 ? 1 : 0.45, fill: "none" });
    }
    S.seg(0, 0.5, NL, 0.5, "g-as");
    if (k >= 2) {
      var o = k === 2 ? E(ANIM.p(t, 0.3, 0.7)) : 1;
      [50, 500].forEach(function (m) {
        var dehors = 0; A._traj.forEach(function (f) { if (Math.abs(f[m - 1] - 0.5) >= 0.05) dehors++; });
        S.seg(m, 0, m, 1, "a-craie", { opacity: o });
        S.txt(m + (m === 500 ? -4 : 4), 0.93, "n = " + m + " : " + dehors + "/30 dehors", "r", m === 500 ? "end" : "start", { opacity: o, "font-size": 11 });
      });
    }
    if (k >= 3) {
      var o3 = k === 3 ? E(ANIM.p(t, 0, 0.5)) : 1;
      S.courbe(function (n) { return 0.5 + 1 / Math.sqrt(n); }, 4, NL, "g-c3", 200, { "stroke-width": 2.2, opacity: o3 });
      S.courbe(function (n) { return 0.5 - 1 / Math.sqrt(n); }, 4, NL, "g-c3", 200, { "stroke-width": 2.2, opacity: o3 });
      S.txt(NL - 4, 0.62, "0,5 ± 1/√n", "", "end", { opacity: o3, "font-size": 11, style: "fill:var(--vert)" });
    }
    if (k >= 4) S.px.math(40, 180, 300, 40, R`$P(|F_n-0{,}5|\geq0{,}05)\leq\frac{100}n$`, { opacity: E(ANIM.p(t, 0, 0.4)) });
    S.txt(NL - 4, 0.04, "n", "", "end", { "font-size": 11, style: "fill:var(--encre3)" });
  }
};

/* Animation : Bienaymé-Tchebychev face au calcul exact, pour une loi binomiale */
ANIMS.tchebychev = {
  titre: R`Bienaymé-Tchebychev : une borne sûre, mais large`,
  vb: [360, 262],
  etapes: [
    { d: 4, l: R`$X\sim\mathcal B(100;0{,}5)$ : $\mu=50$, $V=25$ (écart type $5$). Voici sa loi.` },
    { d: 4.5, l: R`Pour $\delta=10$, l'événement $|X-50|\geq10$ correspond aux barres rouges, aux deux bouts. Probabilité exacte : environ $0{,}057$. L'inégalité garantit seulement $P(|X-50|\geq10)\leq\frac{25}{10^2}=0{,}25$.` },
    { d: 5, l: R`Si $\delta$ descend jusqu'à $5$ (un écart type), la borne $\frac{V}{\delta^2}$ atteint $1$ : elle est vraie, mais n'apprend plus rien (la probabilité exacte est environ $0{,}37$).` },
    { d: 5.5, l: R`Si $\delta$ monte jusqu'à $15$, les deux chutent : exacte environ $0{,}0035$, borne $\frac{25}{225}\approx0{,}11$. La borne reste toujours au-dessus.` },
    { d: 4, l: R`Bilan : la majoration est souvent large, mais elle ne demande que $\mu$ et $V$, et vaut pour n'importe quelle loi. C'est ce qui la rend utile pour <b>garantir</b> un résultat.` }
  ],
  _p: null,
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, nf = ANIM.nf, A = ANIMS.tchebychev;
    if (!A._p) { A._p = [Math.pow(2, -100)]; for (var i = 0; i < 100; i++) A._p.push(A._p[i] * (100 - i) / (i + 1)); }
    var pr = A._p;
    S.rep(29.5, 70.5, 0, 0.09, { px: 5, py: 0.02, marges: { l: 40, r: 10, t: 14, b: 84 }, fx: function (x) { return String(Math.round(x)); }, fy: function (y) { return nf(y, 2); } });
    var d = k === 0 ? null : k === 1 ? 10 : k === 2 ? Math.round(ANIM.l(10, 5, E(p(t, 0, 0.8)))) : k === 3 ? Math.round(ANIM.l(5, 15, E(p(t, 0, 0.8)))) : 15;
    var o1 = k === 1 ? E(p(t, 0, 0.4)) : 1;
    for (var j = 30; j <= 70; j++) {
      var h = pr[j] * (k === 0 ? E(p(t, Math.abs(j - 50) / 40, Math.abs(j - 50) / 40 + 0.5)) : 1), dehors = d !== null && Math.abs(j - 50) >= d;
      S.rect(j - 0.42, 0, j + 0.42, h, dehors ? "a-plein2" : "a-plein", { opacity: dehors ? 0.4 + 0.6 * o1 : 1 });
    }
    if (d === null) { S.txt(70, 0.082, "μ = 50, V = 25", "b", "end"); return; }
    [50 - d, 50 + d].forEach(function (x) { S.seg(x, 0, x, 0.088, "g-as", { opacity: o1 }); });
    S.txt(70, 0.082, "δ = " + d, "r", "end", { opacity: o1 });
    var reel = 0; for (var m = 0; m <= 100; m++) if (Math.abs(m - 50) >= d) reel += pr[m];
    var borne = Math.min(1, 25 / (d * d)), X0 = 122, LW = 200;
    function jauge(y, lab, v, cls, txt) {
      S.px.txt(X0 - 8, y + 10, lab, cls === "a-plein2" ? "r" : "", "end", { "font-size": 12, opacity: o1 });
      S.px.rect(X0, y, LW, 14, "", { style: "fill:none;stroke:var(--ligne2)", opacity: o1 });
      S.px.rect(X0, y, Math.max(1.5, LW * v), 14, cls, { opacity: o1 });
      S.px.txt(X0 + Math.max(1.5, LW * v) + 5, y + 11, txt, cls === "a-plein2" ? "r" : "b", "start", { "font-size": 12, opacity: o1 });
    }
    jauge(208, "P exacte", reel, "a-plein2", "≈ " + (reel < 0.01 ? nf(reel, 4) : nf(reel, 3)));
    jauge(234, "borne V/δ²", borne, "a-plein", (25 / (d * d) >= 1 ? "= 1" : "≈ " + nf(borne, 3)));
  }
};
