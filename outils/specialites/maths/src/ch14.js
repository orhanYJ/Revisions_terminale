/* ---------- Chapitre 14 : sommes de variables aléatoires ---------- */
var CH14 = {
  id: "ch14", num: 14, statut: "ok", partie: "Probabilités", titre: "Sommes de variables aléatoires", court: "Sommes de variables",
  sous: "L'espérance d'une somme est la somme des espérances ; la variance aussi, si les variables sont indépendantes.",
  resume: "Linéarité de l'espérance, $V(aX)=a^2V(X)$, additivité de la variance, loi binomiale, échantillons, $\\frac{\\sigma}{\\sqrt n}$.",
  essentiel: [
    R`<b>Linéarité de l'espérance</b>, toujours vraie : $E(X+Y)=E(X)+E(Y)$ et $E(aX+b)=aE(X)+b$. Pas besoin de connaître la loi de $X+Y$.`,
    R`<b>Variance</b> : $V(aX+b)=a^2V(X)$, donc $\sigma(aX+b)=|a|\,\sigma(X)$. Si $X$ et $Y$ sont <b>indépendantes</b> : $V(X+Y)=V(X)+V(Y)$.`,
    R`Une variable binomiale est une somme de $n$ variables de Bernoulli indépendantes : $E(X)=np$, $V(X)=np(1-p)$, $\sigma(X)=\sqrt{np(1-p)}$.`,
    R`Un <b>échantillon</b> de taille $n$ : $n$ variables indépendantes de même loi (espérance $\mu$, variance $V$). Somme : $E(S_n)=n\mu$, $V(S_n)=nV$. Moyenne $M_n=\frac{S_n}n$ : $E(M_n)=\mu$, $V(M_n)=\frac Vn$.`,
    R`L'écart type de la moyenne est $\frac{\sigma}{\sqrt n}$ : pour diviser la dispersion par $10$, il faut un échantillon $100$ fois plus grand.`
  ],
  attendus: [
    R`Représenter une variable comme somme de variables aléatoires plus simples.`,
    R`Calculer l'espérance d'une variable aléatoire, notamment en utilisant la propriété de linéarité.`,
    R`Calculer la variance d'une variable aléatoire, notamment en l'exprimant comme somme de variables aléatoires indépendantes.`,
    R`Les variables indépendantes sont toujours envisagées dans le cadre d'une succession d'épreuves indépendantes ; justifier l'indépendance n'est pas demandé. L'additivité de la variance est admise.`,
    R`Démonstration exigible : espérance et variance de la loi binomiale <span class="tag bo">BO</span>.`
  ],
  premiere: R`
<ul><li><b>Espérance</b> : $E(X)=\sum_i x_iP(X=x_i)$, la moyenne des valeurs pondérée par leurs probabilités. C'est la moyenne qu'on obtiendrait sur un très grand nombre de répétitions.</li>
<li><b>Variance</b> : $V(X)=\sum_i(x_i-E(X))^2P(X=x_i)$, et la formule pratique $V(X)=E(X^2)-E(X)^2$ (König-Huygens). Écart type $\sigma(X)=\sqrt{V(X)}$, dans l'unité de $X$.</li>
<li><b>Exemple de référence</b> : le dé équilibré, $E=\frac{1+2+\dots+6}6=3{,}5$, $E(X^2)=\frac{91}6$, $V=\frac{91}6-\frac{49}4=\frac{35}{12}\approx2{,}92$.</li>
<li><b>Chapitre 13</b> : loi de Bernoulli ($E=p$, $V=p(1-p)$) et loi binomiale.</li></ul>`,
  cours: [
    { id: "somme", titre: "Somme de deux variables, linéarité de l'espérance", html: R`
[def|Somme de deux variables aléatoires]$X$ et $Y$ étant deux variables aléatoires définies sur le même univers, $X+Y$ est la variable qui à chaque issue $\omega$ associe $X(\omega)+Y(\omega)$.[/]
<div data-anim="sommeDes"></div>
[ex|Deux dés]$X$ et $Y$ : les faces de deux dés équilibrés, $S=X+Y$. Les $36$ couples sont équiprobables ; $S$ prend les valeurs $2$ à $12$, avec $P(S=7)=\frac6{36}=\frac16$ (la plus probable) et $P(S=2)=P(S=12)=\frac1{36}$.[/]
[thm|Linéarité de l'espérance]Pour toutes variables $X$, $Y$ et tout réel $a$ :
$$E(X+Y)=E(X)+E(Y)\qquad\text{et}\qquad E(aX)=aE(X).$$
Plus généralement $E(X_1+\dots+X_n)=E(X_1)+\dots+E(X_n)$. <b>Aucune hypothèse d'indépendance</b> n'est nécessaire.[/]
[ex|Sans calculer la loi]Pour les deux dés, $E(S)=3{,}5+3{,}5=7$. Pour $10$ dés, la somme des faces a pour espérance $35$, alors que sa loi est très longue à écrire.[/]
[ex|Même sans indépendance]On tire successivement et <b>sans remise</b> deux jetons parmi trois numérotés $1$, $2$, $3$. $X$ et $Y$ sont les deux numéros : $E(X)=E(Y)=2$ (chaque jeton a la même chance d'être tiré en premier, ou en second). Donc $E(X+Y)=4$. Contrôle sur les $6$ issues équiprobables : les sommes valent $3,4,3,5,4,5$, de moyenne $4$ ✓.[/]` },
    { id: "affine", titre: "Transformation affine : $aX+b$", html: R`
[prop|Espérance et variance de $aX+b$]Pour tous réels $a$, $b$ :
$$E(aX+b)=aE(X)+b,\qquad V(aX+b)=a^2V(X),\qquad\sigma(aX+b)=|a|\,\sigma(X).$$[/]
<p>Ajouter une constante décale toutes les valeurs : la moyenne bouge, la dispersion non. Multiplier par $a$ dilate les écarts par $|a|$, donc leurs carrés par $a^2$.</p>
[ex|Une note de QCM (bac, Asie, 5 septembre 2025)]$10$ questions à $4$ choix, réponses au hasard : le nombre $X$ de bonnes réponses suit $\mathcal B(10;0{,}25)$, $E(X)=2{,}5$. Une bonne réponse rapporte $1$ point, une mauvaise en retire $0{,}5$ : la note est $Y=X-0{,}5(10-X)=1{,}5X-5$. Donc $E(Y)=1{,}5\times2{,}5-5=-1{,}25$ : répondre au hasard fait perdre des points en moyenne. Et $V(Y)=1{,}5^2\times V(X)=2{,}25\times1{,}875\approx4{,}22$.[/]
[piege|$V(aX)$ n'est pas $aV(X)$]$V(2X)=4V(X)$ et $V(-X)=V(X)$ : une variance n'est jamais négative.[/]` },
    { id: "variance", titre: "Variables indépendantes, additivité de la variance", html: R`
<p>Dans le cadre d'une <b>succession d'épreuves indépendantes</b>, deux variables qui dépendent d'épreuves différentes (la face du premier dé, la face du second) sont <b>indépendantes</b> : $P(X=x\text{ et }Y=y)=P(X=x)\times P(Y=y)$ pour toutes valeurs $x$, $y$.</p>
[thm|Additivité de la variance (admise)]Si $X$ et $Y$ sont indépendantes : $V(X+Y)=V(X)+V(Y)$.[/]
[ex|Deux dés]$V(S)=\frac{35}{12}+\frac{35}{12}=\frac{35}6\approx5{,}83$. On peut le vérifier sur la loi de $S$ : $E(S^2)=\frac{1974}{36}$ et $\frac{1974}{36}-49=\frac{35}6$ ✓.[/]
[ex|Un panier de dépenses (bac, Métropole, 16 juin 2026)]$X$ (suppléments) : $E(X)=96$, $V(X)=3\,114$ ; $Y$ (extras), indépendante de $X$ : $E(Y)=104$, $V(Y)=1\,686$. Après une remise de $40\,\%$, le montant est $Z=0{,}6(X+Y)$. $E(Z)=0{,}6\times200=120$ et $V(Z)=0{,}6^2\times(3\,114+1\,686)=0{,}36\times4\,800=1\,728$.[/]
[piege|Sans indépendance, l'additivité tombe]Avec $Y=X$ (le même dé compté deux fois), $V(X+Y)=V(2X)=4V(X)$, et non $2V(X)$ : $X$ et $X$ ne sont évidemment pas indépendantes. Et $V(X-Y)=V(X)+V(Y)$ pour $X$, $Y$ indépendantes (car $V(-Y)=V(Y)$) : les variances s'ajoutent même pour une différence.[/]
<p><span class="tag hp">Pour aller plus loin</span> Pour $X$, $Y$ indépendantes, $E(XY)=E(X)E(Y)$ ; on en déduit l'additivité de la variance en développant $E\left((X+Y)^2\right)$. Approfondissement non exigible.</p>` },
    { id: "binomiale", titre: "Décomposer en somme : la loi binomiale", html: R`
[meth|Écrire une variable comme une somme]On associe à chaque épreuve (chaque lancer, chaque personne, chaque question…) une variable simple, souvent une variable de Bernoulli $X_i$ qui vaut $1$ si « ça arrive » et $0$ sinon. Le nombre total est $X=X_1+\dots+X_n$, et la linéarité donne $E(X)=E(X_1)+\dots+E(X_n)$.[/]
[thm|Espérance, variance, écart type de $\mathcal B(n,p)$]Si $X$ suit $\mathcal B(n,p)$ :
$$E(X)=np,\qquad V(X)=np(1-p),\qquad\sigma(X)=\sqrt{np(1-p)}.$$[/]
[ex|Donneurs universels (bac, Métropole, 17 juin 2025)]$X\sim\mathcal B(100;0{,}0714)$ : $E(X)=7{,}14$ donneurs en moyenne sur $100$ personnes ; $V(X)=100\times0{,}0714\times0{,}9286\approx6{,}63$ ; $\sigma(X)\approx2{,}57$.[/]
[ex|La linéarité marche même sans loi binomiale]On tire simultanément $2$ boules dans une urne de $3$ rouges et $2$ bleues ; $X$ est le nombre de boules rouges. Ce n'est pas un schéma de Bernoulli (pas d'indépendance). Mais $X=X_1+X_2$, où $X_i$ vaut $1$ si la $i$-ème boule (dans un ordre de tirage) est rouge ; chaque $X_i$ vaut $1$ avec la probabilité $\frac35$. Donc $E(X)=\frac65=1{,}2$. Contrôle avec la loi : $P(X=0)=0{,}1$, $P(X=1)=0{,}6$, $P(X=2)=0{,}3$, $E(X)=0{,}6+0{,}6=1{,}2$ ✓.[/]` },
    { id: "echantillon", titre: "Échantillon, somme et moyenne", html: R`
[def|Échantillon]Un <b>échantillon de taille $n$</b> d'une loi de probabilité est une liste $(X_1;\dots;X_n)$ de variables aléatoires <b>indépendantes</b> et de <b>même loi</b> (répétitions indépendantes d'une même expérience). On note $\mu$ leur espérance, $V$ leur variance, $\sigma$ leur écart type ; $S_n=X_1+\dots+X_n$ et $M_n=\frac{S_n}n$.[/]
[thm|Somme et moyenne d'un échantillon]$$E(S_n)=n\mu,\qquad V(S_n)=nV,\qquad\sigma(S_n)=\sqrt n\,\sigma,$$
$$E(M_n)=\mu,\qquad V(M_n)=\frac Vn,\qquad\sigma(M_n)=\frac{\sigma}{\sqrt n}.$$[/]
<div data-anim="moyenneResserre"></div>
[ex|La moyenne de $n$ dés]Un dé : $\mu=3{,}5$, $\sigma=\sqrt{\frac{35}{12}}\approx1{,}71$. La moyenne de $100$ lancers a la même espérance $3{,}5$, mais un écart type $\frac{1{,}71}{10}\approx0{,}17$ : elle s'écarte rarement de $3{,}5$ de plus de deux écarts types, c'est-à-dire de plus de $0{,}34$ environ.[/]
[ex|Un sondage]On interroge $n=1\,000$ personnes ; chacune répond « oui » avec la probabilité $p=0{,}5$. La proportion de « oui » $F=M_n$ (moyenne de $1\,000$ variables de Bernoulli) a pour écart type $\sqrt{\frac{0{,}5\times0{,}5}{1\,000}}\approx0{,}016$ : environ $1{,}6$ point de pourcentage. C'est le « facteur $\frac1{\sqrt n}$ » aperçu en Seconde avec la fluctuation d'échantillonnage.[/]
[piege|$S_n$ n'est pas $nX_1$]$V(S_n)=nV$ mais $V(nX_1)=n^2V$ : $n$ lancers <b>différents</b> se compensent partiellement, alors que multiplier un seul résultat par $n$ amplifie son écart.[/]` }
  ],
  pieges: [
    { t: "L'additivité de la variance exige l'indépendance", h: R`$E(X+Y)=E(X)+E(Y)$ toujours ; $V(X+Y)=V(X)+V(Y)$ seulement si $X$ et $Y$ sont indépendantes.` },
    { t: "$V(X-Y)$", h: R`Pour $X$, $Y$ indépendantes, $V(X-Y)=V(X)+V(Y)$ : on <b>ajoute</b> les variances.` },
    { t: "Le carré du coefficient", h: R`$V(aX+b)=a^2V(X)$ : la constante $b$ disparaît, le coefficient $a$ est élevé au carré.` },
    { t: "Les écarts types ne s'additionnent pas", h: R`$\sigma(X+Y)=\sqrt{V(X)+V(Y)}$, qui est plus petit que $\sigma(X)+\sigma(Y)$ en général.` },
    { t: "Espérance de la moyenne, variance de la moyenne", h: R`$E(M_n)=\mu$ (pas $\frac\mu n$) et $V(M_n)=\frac Vn$ (pas $\frac V{n^2}$, ni $nV$).` },
    { t: "$E(XY)$", h: R`En général $E(XY)\neq E(X)E(Y)$ ; l'égalité vaut pour des variables indépendantes (hors programme). La linéarité concerne les sommes, pas les produits.` }
  ],
  demos: [
    { bo: true, t: "Espérance et variance de la loi binomiale", h: R`
<p>Soit $X$ le nombre de succès dans un schéma de Bernoulli de paramètres $n$ et $p$. Pour $i$ de $1$ à $n$, notons $X_i$ la variable qui vaut $1$ si la $i$-ème épreuve est un succès et $0$ sinon.</p>
<p><b>Décomposition.</b> Compter les succès revient à additionner les $X_i$ : $X=X_1+X_2+\dots+X_n$. Chaque $X_i$ suit la loi de Bernoulli de paramètre $p$, donc $E(X_i)=p$ et $V(X_i)=p(1-p)$ (chapitre 13).</p>
<p><b>Espérance.</b> Par linéarité de l'espérance : $E(X)=E(X_1)+\dots+E(X_n)=np$.</p>
<p><b>Variance.</b> Les épreuves étant indépendantes, les variables $X_1$, …, $X_n$ sont indépendantes ; par additivité de la variance : $V(X)=V(X_1)+\dots+V(X_n)=np(1-p)$.</p>
<p><b>Écart type.</b> $\sigma(X)=\sqrt{np(1-p)}$. CQFD.</p>
<p class="stylo">Avec la formule $\sum k\binom nkp^k(1-p)^{n-k}$, le calcul direct serait bien plus long : c'est toute la force de la décomposition en somme.</p>` },
    { bo: false, t: "Linéarité de l'espérance sur un univers fini", h: R`
<p>Sur un univers fini $\Omega=\{\omega_1;\dots;\omega_N\}$, l'espérance est la moyenne des valeurs sur les issues, pondérée par leurs probabilités : $E(X)=\sum_jX(\omega_j)P(\{\omega_j\})$ (on regroupe les issues qui donnent la même valeur pour retrouver la formule usuelle).</p>
<p>Alors $E(X+Y)=\sum_j(X(\omega_j)+Y(\omega_j))P(\{\omega_j\})=\sum_jX(\omega_j)P(\{\omega_j\})+\sum_jY(\omega_j)P(\{\omega_j\})=E(X)+E(Y)$. De même $E(aX)=aE(X)$.</p>` },
    { bo: false, t: "$V(aX+b)=a^2V(X)$", h: R`
<p>$E(aX+b)=aE(X)+b$, donc $(aX+b)-E(aX+b)=a(X-E(X))$. En élevant au carré : $((aX+b)-E(aX+b))^2=a^2(X-E(X))^2$, et par linéarité de l'espérance $V(aX+b)=a^2E((X-E(X))^2)=a^2V(X)$.</p>` },
    { bo: false, t: "Espérance et variance de la moyenne d'un échantillon", h: R`
<p>$E(S_n)=E(X_1)+\dots+E(X_n)=n\mu$ (linéarité) et, les $X_i$ étant indépendantes, $V(S_n)=nV$. Puis $M_n=\frac1nS_n$ : $E(M_n)=\frac1n\times n\mu=\mu$ et $V(M_n)=\frac1{n^2}\times nV=\frac Vn$, d'où $\sigma(M_n)=\frac{\sigma}{\sqrt n}$.</p>` }
  ],
  algos: [
    { bo: false, t: "Espérance et variance d'une loi donnée par un tableau", code: `def esperance(valeurs, probas):
    return sum(x * p for x, p in zip(valeurs, probas))

def variance(valeurs, probas):
    m = esperance(valeurs, probas)
    return sum((x - m)**2 * p for x, p in zip(valeurs, probas))

X = [0, 70, 100, 170]
P = [0.19, 0.06, 0.51, 0.24]
print(round(esperance(X, P), 6), round(variance(X, P), 6))`, sortie: `96.0 3114.0`,
      apres: R`<p>La loi des suppléments du sujet de Métropole (16 juin 2026) : on retrouve $E(X)=96$ et $V(X)=3\,114$.</p>` },
    { bo: false, t: "Loi de la somme de deux variables indépendantes", code: `from fractions import Fraction as Fr

def loi_somme(loiX, loiY):
    loi = {}
    for x, px in loiX.items():
        for y, py in loiY.items():         # indépendance : on multiplie
            loi[x + y] = loi.get(x + y, 0) + px * py
    return dict(sorted(loi.items()))

de = {k: Fr(1, 6) for k in range(1, 7)}
S = loi_somme(de, de)
print(S[7], S[2], sum(k * p for k, p in S.items()))
L = {-2: Fr(1, 10), -1: Fr(4, 10), 2: Fr(3, 10), 5: Fr(2, 10)}
print(loi_somme(L, L)[4])`, sortie: `1/6 1/36 7
1/4`,
      apres: R`<p>La dernière ligne traite l'affirmation 4 du sujet d'Amérique du Sud (13 novembre 2025) : $P(Y=4)=\frac14=0{,}25$, venant des couples $(-1;5)$, $(5;-1)$ et $(2;2)$.</p>` },
    { bo: false, t: "La dispersion de la moyenne en $\\frac{\\sigma}{\\sqrt n}$", code: `from math import sqrt

sigma = sqrt(35 / 12)          # écart type d'un dé
for n in [1, 4, 25, 100, 400]:
    print(n, round(sigma / sqrt(n), 3))`, sortie: `1 1.708
4 0.854
25 0.342
100 0.171
400 0.085`,
      apres: R`<p>Multiplier la taille par $4$ divise l'écart type de la moyenne par $2$ ; par $100$, le divise par $10$. La simulation de ces moyennes est au chapitre 15.</p>` }
  ],
  methodes: [
    { t: "Calculer une espérance sans la loi", h: R`
<ol><li>Écris la variable comme une somme ou une combinaison de variables simples : $Z=aX+bY+c$, $X=X_1+\dots+X_n$.</li><li>Calcule (ou lis) l'espérance de chaque morceau.</li><li>Applique la linéarité. Aucune condition d'indépendance à vérifier.</li></ol>` },
    { t: "Calculer une variance", h: R`
<ol><li>Décompose : $Z=a(X+Y)+b$ par exemple.</li><li>Vérifie (ou cite l'énoncé) que les variables sont <b>indépendantes</b>.</li><li>$V(Z)=a^2(V(X)+V(Y))$ : les constantes additives disparaissent, les coefficients passent au carré.</li><li>Pour l'écart type, prends la racine <b>à la fin</b>.</li></ol>` },
    { t: "Étudier la moyenne d'un échantillon", h: R`
<p>Repère $n$, $\mu=E(X_1)$ et $V=V(X_1)$. Écris $E(M_n)=\mu$ et $V(M_n)=\frac Vn$ en citant la linéarité et l'indépendance. C'est presque toujours la question qui précède l'inégalité de concentration (chapitre 15).</p>` },
    { t: "Interpréter une espérance", h: R`
<p>« Sur un grand nombre de répétitions, la valeur moyenne de $X$ est proche de $E(X)$ ». Exemple : $E(Y)=-1{,}25$ : en répondant au hasard à beaucoup de QCM de ce type, on perdrait en moyenne $1{,}25$ point par QCM.</p>` }
  ],
  exos: [
    { niv: 1, t: "Règles de calcul", enonce: R`<p>$X$ et $Y$ sont deux variables aléatoires indépendantes avec $E(X)=5$, $V(X)=4$, $E(Y)=-2$, $V(Y)=9$.</p><ol><li>Calculer $E(3X-1)$ et $V(3X-1)$.</li><li>Calculer $E(X+Y)$, $V(X+Y)$ et $\sigma(X+Y)$.</li><li>Calculer $E(2X-3Y)$ et $V(2X-3Y)$.</li></ol>`,
      corrige: R`<ol><li>$E(3X-1)=15-1=14$ ; $V(3X-1)=9\times4=36$.</li><li>$E(X+Y)=3$ ; $V(X+Y)=4+9=13$ ; $\sigma(X+Y)=\sqrt{13}\approx3{,}61$ (et non $2+3=5$).</li><li>$E(2X-3Y)=10+6=16$ ; $V(2X-3Y)=4\times4+9\times9=97$.</li></ol>` },
    { niv: 1, t: "Deux dés", enonce: R`<p>On lance deux dés équilibrés, indépendamment. $S$ est la somme des faces, $D$ la différence (premier moins second).</p><ol><li>Donner $P(S=7)$, $P(S=10)$ et $P(S\leq4)$.</li><li>Calculer $E(S)$, $V(S)$ et $E(D)$, $V(D)$.</li></ol>`,
      corrige: R`<ol><li>$P(S=7)=\frac6{36}=\frac16$ ; $P(S=10)=\frac3{36}=\frac1{12}$ (couples $(4;6)$, $(5;5)$, $(6;4)$) ; $P(S\leq4)=\frac{1+2+3}{36}=\frac16$.</li><li>$E(S)=7$, $V(S)=2\times\frac{35}{12}=\frac{35}6$. $E(D)=3{,}5-3{,}5=0$ et $V(D)=\frac{35}{12}+\frac{35}{12}=\frac{35}6$ : la différence est aussi dispersée que la somme.</li></ol>` },
    { niv: 2, t: "Un jeu répété", enonce: R`<p>Un jeu coûte $2$ € ; on lance un dé : on gagne $10$ € si l'on obtient $6$, rien sinon. $G$ est le gain net d'une partie (gain moins mise).</p><ol><li>Donner la loi de $G$, puis $E(G)$ et $V(G)$.</li><li>On joue $50$ parties indépendantes ; $T$ est le gain net total. Calculer $E(T)$ et $\sigma(T)$.</li><li>Exprimer $T$ à l'aide du nombre $N$ de $6$ obtenus et retrouver $E(T)$.</li></ol>`,
      corrige: R`<ol><li>$G=8$ avec la probabilité $\frac16$, $G=-2$ avec la probabilité $\frac56$. $E(G)=\frac86-\frac{10}6=-\frac13$. $E(G^2)=\frac{64}6+\frac{4\times5}6=14$, $V(G)=14-\frac19=\frac{125}9\approx13{,}9$.</li><li>$E(T)=50\times\left(-\frac13\right)\approx-16{,}67$ € ; $V(T)=50\times\frac{125}9\approx694{,}4$, $\sigma(T)\approx26{,}35$ €.</li><li>$T=10N-2\times50=10N-100$ avec $N\sim\mathcal B\left(50;\frac16\right)$, $E(N)=\frac{50}6$ : $E(T)=\frac{500}6-100=-\frac{50}3\approx-16{,}67$ ✓. Et $V(T)=100\,V(N)=100\times50\times\frac16\times\frac56=\frac{6\,250}9\approx694{,}4$ ✓.</li></ol>` },
    { niv: 2, t: "Compter avec des variables de Bernoulli", enonce: R`<p>Un QCM a $20$ questions. Pour chaque question, un élève connaît la réponse avec la probabilité $0{,}6$, et sinon répond au hasard parmi $4$ propositions, indépendamment d'une question à l'autre.</p><ol><li>Montrer que la probabilité de répondre juste à une question est $0{,}7$.</li><li>$X$ est le nombre de bonnes réponses. Quelle est sa loi ? Donner $E(X)$ et $\sigma(X)$.</li><li>Une bonne réponse rapporte $1$ point, une mauvaise en retire $0{,}25$. Exprimer la note $N$ en fonction de $X$, puis calculer $E(N)$ et $V(N)$.</li></ol>`,
      corrige: R`<ol><li>Probabilités totales : $0{,}6\times1+0{,}4\times0{,}25=0{,}7$.</li><li>$20$ questions indépendantes, succès « juste » de probabilité $0{,}7$ : $X\sim\mathcal B(20;0{,}7)$, $E(X)=14$, $V(X)=4{,}2$, $\sigma(X)\approx2{,}05$.</li><li>$N=X-0{,}25(20-X)=1{,}25X-5$. $E(N)=17{,}5-5=12{,}5$ ; $V(N)=1{,}25^2\times4{,}2=6{,}5625$.</li></ol>` },
    { niv: 3, t: "Moyenne d'un échantillon de dépenses (type bac)", enonce: R`<p>Dans une boulangerie, la dépense $X$ (en €) d'un client suit la loi suivante :</p><div class="tab-wrap"><table><tr><td>$x_i$</td><td>$2$</td><td>$5$</td><td>$10$</td><td>$20$</td></tr><tr><td>$P(X=x_i)$</td><td>$0{,}4$</td><td>$0{,}3$</td><td>$0{,}2$</td><td>$0{,}1$</td></tr></table></div><ol><li>Calculer $E(X)$ et $V(X)$.</li><li>Le pourboire $Y$ laissé par un client, indépendant de $X$, a pour espérance $0{,}5$ et pour variance $0{,}25$. On note $T=X+Y$. Calculer $E(T)$ et $V(T)$.</li><li>Une matinée, $n$ clients passent, de dépenses totales $T_1$, …, $T_n$ indépendantes et de même loi que $T$. On note $M_n$ la moyenne. Calculer $E(M_n)$ et $V(M_n)$.</li><li>Pour quelle taille $n$ l'écart type de $M_n$ devient-il inférieur à $0{,}5$ € ?</li></ol>`,
      corrige: R`<ol><li>$E(X)=0{,}8+1{,}5+2+2=6{,}3$. $E(X^2)=1{,}6+7{,}5+20+40=69{,}1$, donc $V(X)=69{,}1-39{,}69=29{,}41$.</li><li>$E(T)=6{,}3+0{,}5=6{,}8$ ; par indépendance $V(T)=29{,}41+0{,}25=29{,}66$.</li><li>$E(M_n)=6{,}8$ et $V(M_n)=\frac{29{,}66}n$.</li><li>$\sigma(M_n)=\sqrt{\frac{29{,}66}n}<0{,}5\iff\frac{29{,}66}n<0{,}25\iff n>118{,}64$ : à partir de $n=119$ clients.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole, 16 juin 2026 (sujet 1), exercice 1, partie B, questions 1 à 3a", url: "https://www.apmep.fr/IMG/pdf/BAC_General_Specialite_Sujet_J1_metropole_FK-v2.pdf", h: R`$E(X)=96$, $V(X)=3\,114$ ; $Z=0{,}6(X+Y)$ avec $X$, $Y$ indépendantes : $E(Z)=120$, $V(Z)=1\,728$ ; moyenne d'un échantillon de $n$ familles : $E(M_n)=120$, $V(M_n)=\frac{1\,728}n$. La question 3b relève du chapitre 15.` },
    { ref: "Bac 2025, Asie, 5 septembre 2025 (sujet 1), exercice 3, question 4", url: "https://www.apmep.fr/IMG/pdf/Asie_spe_J1_05_09_2025_FK.pdf", h: R`QCM répondu au hasard, $X\sim\mathcal B(10;0{,}25)$ ; la note $Y=1{,}5X-5$ ; espérance $E(Y)=-1{,}25$ par linéarité.` },
    { ref: "Bac 2025, Amérique du Sud, 13 novembre 2025 (jour 1), exercice 2, affirmation 4", url: "https://www.apmep.fr/IMG/pdf/Ameri_du_Sud_J1__13_11_2025_DV.pdf", h: R`Somme de deux variables indépendantes de même loi : « $P(Y=4)=0{,}25$ » (vrai, voir le programme Python).` },
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 1, questions 5c et 6a à 6c", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Espérance $7{,}14$ et variance $\approx6{,}63$ d'une loi binomiale, puis moyenne $M_N$ de $N$ variables indépendantes : $E(M_N)=7{,}14$ et $V(M_N)=\frac{6{,}63}N$.` }
  ],
  retenir: R`
[thm|Linéarité (toujours)]$E(X+Y)=E(X)+E(Y)$ ; $E(aX+b)=aE(X)+b$.[/]
[thm|Variance]$V(aX+b)=a^2V(X)$, $\sigma(aX+b)=|a|\sigma(X)$. Si $X$, $Y$ indépendantes : $V(X+Y)=V(X)+V(Y)$ et $V(X-Y)=V(X)+V(Y)$.[/]
[thm|Loi binomiale]$E=np$, $V=np(1-p)$, $\sigma=\sqrt{np(1-p)}$ (somme de $n$ Bernoulli indépendantes).[/]
<div class="tab-wrap"><table><tr><th>Échantillon de taille $n$</th><th>Espérance</th><th>Variance</th><th>Écart type</th></tr>
<tr><td>$X_i$</td><td>$\mu$</td><td>$V$</td><td>$\sigma$</td></tr>
<tr><td>$S_n=X_1+\dots+X_n$</td><td>$n\mu$</td><td>$nV$</td><td>$\sqrt n\,\sigma$</td></tr>
<tr><td>$M_n=\frac{S_n}n$</td><td>$\mu$</td><td>$\frac Vn$</td><td>$\frac{\sigma}{\sqrt n}$</td></tr></table></div>
<p class="stylo">Un dé : $\mu=3{,}5$, $V=\frac{35}{12}$. Deux dés : $E(S)=7$, $V(S)=\frac{35}6$.</p>`,
  qcm: [
    { q: R`$E(X)=4$. $E(3X+2)=$`, c: ["$12$", "$14$", "$6$", "$36$"], r: 1, e: R`$3\times4+2$.`, ref: "affine" },
    { q: R`$V(X)=4$. $V(3X+2)=$`, c: ["$12$", "$14$", "$36$", "$38$"], r: 2, e: R`$3^2\times4$ ; la constante $2$ ne change pas la dispersion.`, ref: "affine" },
    { q: R`$V(-X)=$`, c: [R`$-V(X)$`, R`$V(X)$`, R`$0$`, R`$V(X)^2$`], r: 1, e: R`$(-1)^2V(X)$.`, ref: "affine" },
    { q: R`La relation $E(X+Y)=E(X)+E(Y)$ est vraie :`, c: ["seulement si $X$ et $Y$ sont indépendantes", "toujours", "seulement si $X$ et $Y$ ont la même loi", "jamais"], r: 1, e: R`La linéarité de l'espérance ne demande aucune hypothèse.`, ref: "somme" },
    { q: R`La relation $V(X+Y)=V(X)+V(Y)$ est vraie :`, c: ["toujours", "si $X$ et $Y$ sont indépendantes", "si $E(X)=E(Y)$", "jamais"], r: 1, e: R`Additivité de la variance pour des variables indépendantes.`, ref: "variance" },
    { q: R`$X$, $Y$ indépendantes, $V(X)=3$, $V(Y)=5$. $V(X-Y)=$`, c: ["$-2$", "$2$", "$8$", "$34$"], r: 2, e: R`$V(X)+V(-Y)=V(X)+V(Y)$.`, ref: "variance" },
    { q: R`On lance deux dés. $E(S)=$`, c: ["$6$", "$7$", "$3{,}5$", "$12$"], r: 1, e: R`$3{,}5+3{,}5$, sans calculer la loi de $S$.`, ref: "somme" },
    { q: R`$X\sim\mathcal B(50;0{,}2)$. $V(X)=$`, c: ["$10$", "$8$", "$2{,}83$", "$0{,}16$"], r: 1, e: R`$np(1-p)=50\times0{,}2\times0{,}8$.`, ref: "binomiale" },
    { q: R`$X\sim\mathcal B(100;0{,}5)$. $\sigma(X)=$`, c: ["$25$", "$5$", "$50$", "$0{,}5$"], r: 1, e: R`$\sqrt{100\times0{,}25}=5$.`, ref: "binomiale" },
    { q: R`La démonstration de $E(X)=np$ pour $X\sim\mathcal B(n,p)$ repose sur :`, c: ["la formule $\\binom nk$", "l'écriture $X=X_1+\\dots+X_n$ et la linéarité", "l'inégalité de Bienaymé-Tchebychev", "la symétrie de la loi"], r: 1, e: R`Somme de $n$ variables de Bernoulli d'espérance $p$.`, ref: "binomiale" },
    { q: R`Échantillon de taille $n$ d'espérance $\mu$, variance $V$. $V(M_n)=$`, c: [R`$nV$`, R`$\frac Vn$`, R`$\frac V{n^2}$`, R`$V$`], r: 1, e: R`$V\left(\frac{S_n}n\right)=\frac1{n^2}\times nV$.`, ref: "echantillon" },
    { q: R`Pour diviser par $10$ l'écart type d'une moyenne d'échantillon, il faut multiplier $n$ par :`, c: ["$10$", "$20$", "$100$", "$\\sqrt{10}$"], r: 2, e: R`$\sigma(M_n)=\frac\sigma{\sqrt n}$.`, ref: "echantillon" },
    { q: R`$E(X)=96$, $E(Y)=104$. $E(0{,}6(X+Y))=$`, c: ["$200$", "$120$", "$60$", "$124$"], r: 1, e: R`$0{,}6\times(96+104)$ (bac, Métropole, juin 2026).`, ref: "variance" },
    { q: R`$V(2X)$, comparé à la variance de la somme de deux lancers indépendants de même loi que $X$ :`, c: ["c'est pareil", "$V(2X)=4V(X)$ contre $2V(X)$", "$V(2X)=2V(X)$ contre $4V(X)$", "on ne peut pas comparer"], r: 1, e: R`Deux lancers différents se compensent en partie ; doubler un seul lancer double les écarts.`, ref: "echantillon" }
  ],
  cartes: [
    [R`Linéarité de l'espérance`, R`$E(X+Y)=E(X)+E(Y)$, $E(aX+b)=aE(X)+b$, sans condition.`],
    [R`$V(aX+b)$`, R`$a^2V(X)$`],
    [R`$\sigma(aX+b)$`, R`$|a|\,\sigma(X)$`],
    [R`Additivité de la variance`, R`$V(X+Y)=V(X)+V(Y)$ si $X$ et $Y$ sont indépendantes.`],
    [R`$V(X-Y)$, $X$ et $Y$ indépendantes`, R`$V(X)+V(Y)$`],
    [R`Espérance et variance de $\mathcal B(n,p)$`, R`$np$ et $np(1-p)$`],
    [R`Idée de la démonstration de $E=np$`, R`$X=X_1+\dots+X_n$ (Bernoulli), linéarité.`],
    [R`Échantillon de taille $n$`, R`$n$ variables indépendantes de même loi.`],
    [R`$E(S_n)$ et $V(S_n)$`, R`$n\mu$ et $nV$`],
    [R`$E(M_n)$ et $V(M_n)$`, R`$\mu$ et $\frac Vn$`],
    [R`$\sigma(M_n)$`, R`$\frac{\sigma}{\sqrt n}$`],
    [R`Variance d'un dé équilibré`, R`$\frac{35}{12}\approx2{,}92$`],
    [R`Loi de la somme de deux dés : valeur la plus probable`, R`$7$, de probabilité $\frac16$.`],
    [R`Proportion sur un échantillon de $n$ (paramètre $p$) : écart type`, R`$\sqrt{\frac{p(1-p)}n}$`]
  ]
};

/* Animation : les 36 couples de deux dés tombent dans l'histogramme de la somme */
ANIMS.sommeDes = {
  titre: "La loi de la somme de deux dés",
  vb: [360, 300],
  etapes: [
    { d: 3.5, l: R`Les $36$ couples (dé 1 ; dé 2) sont équiprobables, de probabilité $\frac1{36}$. Dans chaque case, la somme $S$.` },
    { d: 3.5, l: R`Les cases de même somme sont alignées en diagonale : une seule case pour $S=2$, six pour $S=7$.` },
    { d: 5, l: R`On range chaque case dans la colonne de sa somme : l'histogramme de $S$ se construit. $P(S=k)=\frac{\text{nombre de cases}}{36}$.` },
    { d: 4, l: R`La loi est symétrique autour de $7$ : $E(S)=7=3{,}5+3{,}5$, la somme des espérances (linéarité).` },
    { d: 4.5, l: R`Et, les deux dés étant indépendants, $V(S)=\frac{35}{12}+\frac{35}{12}=\frac{35}6$ : les variances s'ajoutent.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, c = 21, gx = 118, gy = 22, base = 284, cw = 26, ch = 13;
    var cols = ["#8E9AAF", "#5B7DB1", "#2343A8", "#23774F", "#B8860B", "#C2372B"];
    function teinte(s) { return cols[Math.min(5, 6 - Math.abs(7 - s) - 1 + 0)] || cols[0]; }
    if (k <= 2) { S.px.txt(gx + 3 * c, gy - 6, "dé 2 →", "", "middle", { "font-size": 10, style: "fill:var(--encre3)" }); S.px.txt(gx - 18, gy + 3 * c, "dé 1", "", "end", { "font-size": 10, style: "fill:var(--encre3)" }); }
    var oLab = k <= 2 ? 1 : 0;
    for (var j = 0; j < 6; j++) { S.px.txt(gx + j * c + c / 2, gy + 6 * c + 12, String(j + 1), "", "middle", { "font-size": 9, style: "fill:var(--encre3)", opacity: oLab }); S.px.txt(gx - 6, gy + j * c + c / 2 + 4, String(j + 1), "", "end", { "font-size": 9, style: "fill:var(--encre3)", opacity: oLab }); }
    var pile = {};
    for (var a = 1; a <= 6; a++) for (var b = 1; b <= 6; b++) {
      var s = a + b, rang = pile[s] = (pile[s] || 0) + 1;
      var x1 = gx + (b - 1) * c, y1 = gy + (a - 1) * c, w1 = c - 2, h1 = c - 2;
      var x2 = 22 + (s - 2) * 30, y2 = base - rang * ch, w2 = cw, h2 = ch - 1.5;
      var f = k < 2 ? 0 : k === 2 ? E(ANIM.p(t, (a + b - 2) / 14, (a + b - 2) / 14 + 0.3)) : 1;
      var col = k >= 1 ? teinte(s) : null, op = k >= 1 ? (k === 1 ? 0.25 + 0.6 * E(t) : 0.85) : 0;
      S.px.rect(ANIM.l(x1, x2, f), ANIM.l(y1, y2, f), ANIM.l(w1, w2, f), ANIM.l(h1, h2, f), "a-case", { style: col ? "fill:" + col + ";fill-opacity:" + op.toFixed(2) + ";stroke:var(--papier2)" : null });
      if (f < 0.5) S.px.txt(ANIM.l(x1, x2, f) + w1 / 2, ANIM.l(y1, y2, f) + h1 / 2 + 4, String(s), "", "middle", { "font-size": 10, style: k >= 1 ? "fill:#fff;font-weight:700" : null });
    }
    S.px.seg(16, base, 344, base, "g-axe");
    for (var s2 = 2; s2 <= 12; s2++) S.px.txt(22 + (s2 - 2) * 30 + cw / 2, base + 13, String(s2), "", "middle", { "font-size": 10 });
    if (k >= 2) {
      var o = k === 2 ? E(ANIM.p(t, 0.75, 1)) : 1;
      for (var s3 = 2; s3 <= 12; s3++) { var nb = 6 - Math.abs(7 - s3); S.px.txt(22 + (s3 - 2) * 30 + cw / 2, base - nb * ch - 5, nb + "/36", "", "middle", { "font-size": 9, opacity: o }); }
    }
    if (k >= 3) {
      var xm = 22 + 5 * 30 + cw / 2, o2 = k === 3 ? E(t) : 1;
      S.px.seg(xm, base - 6 * ch, xm, base, "g-as", { opacity: o2 });
      S.px.txt(xm, base - 6 * ch - 20, "E(S) = 7", "r", "middle", { opacity: o2 });
    }
    if (k >= 4) S.px.math(110, 70, 240, 44, R`$V(S)=\frac{35}{12}+\frac{35}{12}=\frac{35}6$`, { opacity: E(t) });
  }
};

/* Animation : la loi de la moyenne de n dés se resserre autour de 3,5 */
ANIMS.moyenneResserre = {
  titre: R`La moyenne de $n$ dés se resserre autour de $3{,}5$`,
  vb: [360, 260],
  etapes: [
    { d: 3.5, l: R`$n=1$ : la face d'un dé, loi uniforme sur $\{1;\dots;6\}$. $\mu=3{,}5$, $\sigma\approx1{,}71$.` },
    { d: 4, l: R`$n=2$ : la moyenne de deux dés. Sa loi est triangulaire (c'est la somme divisée par $2$). Même centre, $\sigma(M_2)=\frac{1{,}71}{\sqrt2}\approx1{,}21$.` },
    { d: 4, l: R`$n=4$ : la cloche apparaît, $\sigma(M_4)=\frac{1{,}71}{2}\approx0{,}85$.` },
    { d: 4, l: R`$n=16$ : $\sigma(M_{16})=\frac{1{,}71}4\approx0{,}43$. Les valeurs éloignées de $3{,}5$ deviennent très rares.` },
    { d: 4.5, l: R`$n=64$ : $\sigma(M_{64})\approx0{,}21$. L'espérance ne bouge pas ($E(M_n)=3{,}5$) ; la dispersion est divisée par $\sqrt n$. C'est le chemin vers la loi des grands nombres.` }
  ],
  _lois: null,
  rendu: function (S, k, t) {
    var A = ANIMS.moyenneResserre, ns = [1, 2, 4, 16, 64];
    if (!A._lois) {
      A._lois = {};
      var cur = [0, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6], m = 1;
      function conv(L) { var r = new Array(L.length + 6).fill(0); for (var i = 0; i < L.length; i++) if (L[i]) for (var f = 1; f <= 6; f++) r[i + f] += L[i] / 6; return r; }
      for (var n = 1; n <= 64; n++) { if (n > 1) cur = conv(cur); if (ns.indexOf(n) >= 0) A._lois[n] = cur.slice(); }
    }
    var x0 = 1, x1 = 6;
    S.rep(0.8, 6.2, 0, 2.1, { px: 1, py: 0.5 });
    function dessine(n, op) {
      var L = A._lois[n], w = 1 / n, larg = Math.max(1.1, (S.X(1 + w) - S.X(1)) * 0.8);
      for (var s = n; s <= 6 * n; s++) {
        var p = L[s] || 0, dens = p / w, x = s / n;
        if (dens < 1e-4) continue;
        var X = S.X(x), Y = S.Y(Math.min(dens, 2.1));
        S.px.rect(X - larg / 2, Y, larg, S.Y(0) - Y, "", { style: "fill:var(--bleu);fill-opacity:" + (0.55 * op).toFixed(2) });
      }
    }
    var cible = ns[k], prec = ns[Math.max(0, k - 1)], f = ANIM.e(ANIM.p(t, 0, 0.6));
    if (k > 0 && f < 1) dessine(prec, 1 - f);
    dessine(cible, k === 0 ? 1 : f);
    var sig = Math.sqrt(35 / 12) / Math.sqrt(cible), y = 1.97;
    S.seg(3.5, 0, 3.5, 2.05, "g-as");
    S.seg(3.5 - sig, y, 3.5 + sig, y, "g-c2", { "stroke-width": 2.4 });
    S.pt(3.5 - sig, y, "g-pt2", 3); S.pt(3.5 + sig, y, "g-pt2", 3);
    S.txt(3.5 + sig + 0.08, y - 0.08, "μ ± σ/√n", "r", "start");
    S.txt(0.9, 1.9, "n = " + cible, "b", "start");
    S.txt(6.15, 1.6, "densité", "", "end", { "font-size": 10, style: "fill:var(--encre3)" });
  }
};
