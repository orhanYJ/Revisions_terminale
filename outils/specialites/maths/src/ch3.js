/* ---------- Chapitre 3 : limites de fonctions ---------- */
var CH3 = {
  id: "ch3", num: 3, statut: "ok", partie: "Analyse", titre: "Limites de fonctions", court: "Limites de fonctions",
  sous: "Comportement aux bords : en $\\pm\\infty$, près d'une valeur interdite ; asymptotes.",
  resume: "Limites en $\\pm\\infty$ et en un point, asymptotes, opérations, composition, croissances comparées.",
  essentiel: [
    R`$\lim_{x\to+\infty}f(x)=\ell$ : $f(x)$ finit aussi près qu'on veut de $\ell$ ; la droite $y=\ell$ est alors <b>asymptote horizontale</b>.`,
    R`$\lim_{x\to a}f(x)=\pm\infty$ : la droite $x=a$ est <b>asymptote verticale</b> ; on étudie souvent la limite à gauche ($x\to a^-$) et à droite ($x\to a^+$).`,
    R`Les opérations se font comme pour les suites, avec les mêmes formes indéterminées ; on lève l'indétermination en factorisant le terme prépondérant.`,
    R`Composition : si $u(x)\to b$ et $v(X)\to c$ quand $X\to b$, alors $v(u(x))\to c$. Exemple : $\e^{-x^2}\to0$ en $+\infty$.`,
    R`Croissances comparées : en $+\infty$, $\frac{\e^x}{x^n}\to+\infty$ et $x^n\e^{-x}\to0$ ; en $-\infty$, $x^n\e^x\to0$. <b>L'exponentielle l'emporte sur toute puissance.</b>`
  ],
  attendus: [
    R`Déterminer dans des cas simples la limite d'une fonction en un point, en $\pm\infty$, avec les limites usuelles, les croissances comparées, les opérations, des majorations, minorations ou encadrements, la factorisation du terme prépondérant.`,
    R`Faire le lien entre l'existence d'une asymptote parallèle à un axe et celle de la limite correspondante.`,
    R`Démonstration exigible : croissance comparée de $x\mapsto x^n$ et de l'exponentielle en $+\infty$ ; limites de l'exponentielle en $\pm\infty$ (listée dans la partie « Suites » du programme).`,
    R`Les opérations sur les limites sont admises ; la composition s'utilise « en contexte ».`
  ],
  premiere: R`
<ul><li>Fonction exponentielle : $\exp'=\exp$, $\e^x>0$, $\e^{a+b}=\e^a\e^b$, $\e^{-a}=\frac1{\e^a}$, $(\e^a)^n=\e^{na}$, $\e^0=1$, strictement croissante sur $\R$.</li>
<li>Dérivées usuelles : $(x^n)'=nx^{n-1}$, $\left(\frac1x\right)'=-\frac1{x^2}$, $(\sqrt x)'=\frac1{2\sqrt x}$ ; $(uv)'=u'v+uv'$, $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$, $(\e^{ax+b})'=a\e^{ax+b}$.</li>
<li>Nombre dérivé : $f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$. Par exemple $\lim_{h\to0}\frac{\e^h-1}{h}=\exp'(0)=1$.</li>
<li>$-1\leq\cos x\leq1$ et $-1\leq\sin x\leq1$ pour tout réel $x$.</li></ul>`,
  cours: [
    { id: "infini", titre: "Limite en $+\\infty$ ou en $-\\infty$", html: R`
[def|Limite infinie en $+\infty$]$\lim_{x\to+\infty}f(x)=+\infty$ si tout intervalle $[A;+\infty[$ contient toutes les valeurs $f(x)$ pour $x$ assez grand.[/]
[def|Limite finie en $+\infty$]$\lim_{x\to+\infty}f(x)=\ell$ si tout intervalle ouvert contenant $\ell$ contient toutes les valeurs $f(x)$ pour $x$ assez grand. La droite d'équation $y=\ell$ est alors <b>asymptote horizontale</b> à la courbe en $+\infty$.[/]
<p>Mêmes définitions en $-\infty$ (« pour $x$ assez petit », c'est-à-dire $x\leq B$ pour un certain $B$). C'est exactement l'idée des suites, avec un réel $x$ à la place de l'entier $n$.</p>
[ex|$f(x)=2+\frac1x$]Quand $x\to+\infty$, $\frac1x\to0$ donc $f(x)\to2$ : asymptote horizontale $y=2$. Et $f(x)>2$ pour $x>0$ : la courbe est <b>au-dessus</b> de l'asymptote.[/]
[piege|Pas de limite]$\cos x$ oscille entre $-1$ et $1$ : il n'a pas de limite en $+\infty$.[/]` },
    { id: "point", titre: "Limite en un réel $a$ ; asymptote verticale", html: R`
[def|Limite infinie en $a$]$\lim_{x\to a}f(x)=+\infty$ si tout intervalle $[A;+\infty[$ contient toutes les valeurs $f(x)$ pour $x$ assez proche de $a$. La droite d'équation $x=a$ est alors <b>asymptote verticale</b>.[/]
<p>Souvent, le comportement diffère selon le côté : on note $x\to a^+$ (ou $x\to a$, $x>a$) et $x\to a^-$ (ou $x\to a$, $x<a$).</p>
[ex|$\frac1x$ en $0$]$\lim_{x\to0^+}\frac1x=+\infty$ et $\lim_{x\to0^-}\frac1x=-\infty$ ; asymptote verticale $x=0$. En revanche $\lim_{x\to0}\frac1{x^2}=+\infty$ des deux côtés.[/]
[ex|$f(x)=\frac{2x+1}{x-1}$]Quand $x\to1$, le numérateur tend vers $3$ et le dénominateur vers $0$. Signe du dénominateur : $x-1>0$ si $x>1$. Donc $\lim_{x\to1^+}f(x)=+\infty$ et $\lim_{x\to1^-}f(x)=-\infty$. Numériquement, $f(1{,}001)=3002$ et $f(0{,}999)=-2998$.[/]
<div data-w="asymptotes"></div>
<p>Il existe aussi des limites <b>finies</b> en un point : $\lim_{x\to2}(x^2+1)=5$. Pour une fonction usuelle définie en $a$, on remplace simplement $x$ par $a$ (c'est la continuité, chapitre 4).</p>` },
    { id: "reference", titre: "Fonctions de référence", html: R`
<div class="tab-wrap"><table><tr><th>Fonction</th><th>en $-\infty$</th><th>en $0$</th><th>en $+\infty$</th></tr>
<tr><td>$x^n$, $n$ pair $\geq2$</td><td>$+\infty$</td><td>$0$</td><td>$+\infty$</td></tr>
<tr><td>$x^n$, $n$ impair</td><td>$-\infty$</td><td>$0$</td><td>$+\infty$</td></tr>
<tr><td>$\frac1{x^n}$, $n$ pair</td><td>$0$</td><td>$+\infty$</td><td>$0$</td></tr>
<tr><td>$\frac1{x^n}$, $n$ impair</td><td>$0$</td><td>$0^-$ : $-\infty$ ; $0^+$ : $+\infty$</td><td>$0$</td></tr>
<tr><td>$\sqrt x$</td><td>—</td><td>$0$</td><td>$+\infty$</td></tr>
<tr><td>$\e^x$</td><td>$0$</td><td>$1$</td><td>$+\infty$</td></tr></table></div>
[thm|Limites de l'exponentielle]$\lim_{x\to+\infty}\e^x=+\infty$ et $\lim_{x\to-\infty}\e^x=0$. L'axe des abscisses est asymptote à la courbe de $\exp$ en $-\infty$. (Démonstration exigible.)[/]` },
    { id: "operations", titre: "Opérations et composition", html: R`
<p>Les règles d'addition, de multiplication et de quotient sont <b>les mêmes que pour les suites</b> (voir le tableau du chapitre 2), avec les mêmes formes indéterminées : $\infty-\infty$, $0\times\infty$, $\frac\infty\infty$, $\frac00$. Elles sont admises.</p>
[meth|Quotient de polynômes en $\pm\infty$]$\lim_{x\to-\infty}\frac{3x^2+1}{x^2-5x}=\lim_{x\to-\infty}\frac{x^2\left(3+\frac1{x^2}\right)}{x^2\left(1-\frac5x\right)}=3$. Plus vite : <b>en $\pm\infty$, un polynôme se comporte comme son terme de plus haut degré</b>, et un quotient comme le quotient des termes de plus haut degré (ici $\frac{3x^2}{x^2}=3$).[/]
[meth|Forme $\frac00$ en un point : factoriser par $(x-a)$]$\lim_{x\to1}\frac{x^2-1}{x-1}$ : forme $\frac00$. Pour $x\neq1$, $\frac{(x-1)(x+1)}{x-1}=x+1\to2$.[/]
[thm|Composition]Si $\lim_{x\to a}u(x)=b$ et $\lim_{X\to b}v(X)=c$, alors $\lim_{x\to a}v(u(x))=c$ ($a$, $b$, $c$ réels ou $\pm\infty$).[/]
[ex|Rédiger une composition]$\lim_{x\to+\infty}\e^{-x^2}$ : on pose $X=-x^2$. Quand $x\to+\infty$, $X\to-\infty$, et $\lim_{X\to-\infty}\e^X=0$. Par composition, $\lim_{x\to+\infty}\e^{-x^2}=0$.<br>De même $\lim_{x\to+\infty}\e^{\frac1x}=\e^0=1$ et $\lim_{x\to-\infty}\sqrt{1-2x}=+\infty$.[/]` },
    { id: "comparaison", titre: "Comparaison et gendarmes", html: R`
[thm|Comparaison]Si $f(x)\geq g(x)$ pour $x$ assez grand et $\lim_{x\to+\infty}g(x)=+\infty$, alors $\lim_{x\to+\infty}f(x)=+\infty$. (Énoncés analogues en $-\infty$, en $a$, et pour $-\infty$.)[/]
[thm|Gendarmes]Si $g(x)\leq f(x)\leq h(x)$ pour $x$ assez grand, et si $g$ et $h$ ont la même limite finie $\ell$ en $+\infty$, alors $\lim_{x\to+\infty}f(x)=\ell$.[/]
[ex|Avec un cosinus]$f(x)=\frac{\cos x}{x}$ pour $x>0$ : $-\frac1x\leq f(x)\leq\frac1x$, et $\pm\frac1x\to0$ : par les gendarmes, $\lim_{x\to+\infty}f(x)=0$.<br>$g(x)=x+\cos x\geq x-1\to+\infty$ : par comparaison, $\lim_{x\to+\infty}g(x)=+\infty$.[/]` },
    { id: "croissances", titre: "Croissances comparées", html: R`
<p>Face à $\frac{\e^x}{x}$ en $+\infty$, on a une forme $\frac\infty\infty$. Qui gagne ? Toujours l'exponentielle.</p>
[thm|Croissances comparées]Pour tout entier $n\geq1$ :
$$\lim_{x\to+\infty}\frac{\e^x}{x^n}=+\infty,\qquad\lim_{x\to+\infty}x^n\e^{-x}=0,\qquad\lim_{x\to-\infty}x^n\e^x=0.$$[/]
<p>La première est une <b>démonstration exigible</b>. Les deux autres s'en déduisent : $x^n\e^{-x}=\frac{1}{\e^x/x^n}$ ; et en posant $X=-x$, $x^n\e^x=(-1)^nX^n\e^{-X}$.</p>
<div data-w="croissances"></div>
[meth|Factoriser par l'exponentielle]$\lim_{x\to+\infty}(\e^x-x^3)$ : forme $\infty-\infty$. $\e^x-x^3=\e^x\left(1-\frac{x^3}{\e^x}\right)$ ; $\frac{x^3}{\e^x}\to0$ donc la parenthèse tend vers $1$, et le tout vers $+\infty$.[/]
[ex|Au bac]$\lim_{x\to+\infty}(x+1)\e^{-x}=\lim\left(x\e^{-x}+\e^{-x}\right)=0+0=0$. C'était l'affirmation 1 (fausse : elle annonçait $+\infty$) de l'exercice 2 du sujet de Polynésie du 16 juin 2026.[/]
<p><span class="tag hp">Pour aller plus loin</span> Asymptotes obliques : si $\lim_{x\to+\infty}\left[f(x)-(ax+b)\right]=0$, la droite $y=ax+b$ est asymptote oblique. Exemple : $\sqrt{x^2+x}-x\to\frac12$ (quantité conjuguée), donc $y=x+\frac12$ est asymptote à $x\mapsto\sqrt{x^2+x}$ en $+\infty$. Ce n'est pas exigible.</p>` }
  ],
  pieges: [
    { t: "Oublier le côté", h: R`$\lim_{x\to1}\frac1{x-1}$ n'existe pas : $+\infty$ à droite, $-\infty$ à gauche. Fais un tableau de signes du dénominateur.` },
    { t: "« $\\frac{3}{0}=\\infty$ »", h: R`On ne divise pas par zéro : on étudie la limite d'un quotient dont le dénominateur <b>tend</b> vers $0$, avec son signe ($0^+$ ou $0^-$).` },
    { t: "Asymptote et courbe", h: R`Une courbe peut couper son asymptote horizontale (exemple : $\frac{\sin x}{x}$ coupe $y=0$ une infinité de fois). L'asymptote décrit le comportement <b>à l'infini</b>.` },
    { t: "Terme prépondérant en $0$", h: R`En $0$, c'est le terme de <b>plus bas</b> degré qui domine : $x^3+2x\approx2x$ près de $0$. Ne factorise pas par $x^3$.` },
    { t: "Croissances comparées à l'envers", h: R`$\frac{x^{100}}{\e^x}\to0$ en $+\infty$, même si $x^{100}$ est énorme pour $x=10$. Mais en $-\infty$, $\e^x\to0$ et c'est $x^n\e^x\to0$.` }
  ],
  demos: [
    { bo: true, t: "Limites de l'exponentielle en $+\\infty$ et en $-\\infty$", h: R`
<p><b>En $+\infty$.</b> Soit $g(x)=\e^x-x$. $g'(x)=\e^x-1$, négatif sur $]-\infty;0]$, positif sur $[0;+\infty[$ : $g$ a un minimum en $0$, $g(0)=1>0$. Donc $\e^x>x$ pour tout réel $x$. Comme $\lim_{x\to+\infty}x=+\infty$, par comparaison $\lim_{x\to+\infty}\e^x=+\infty$.</p>
<p><b>En $-\infty$.</b> Pour tout $x$, $\e^x=\frac{1}{\e^{-x}}$. On pose $X=-x$ : quand $x\to-\infty$, $X\to+\infty$ et $\e^X\to+\infty$, donc $\frac1{\e^X}\to0$. Ainsi $\lim_{x\to-\infty}\e^x=0$.</p>
<p class="stylo">Variante par les suites : $\e^n=(\e)^n$ avec $\e>1$, donc $\e^n\to+\infty$ (suite géométrique), et $\exp$ est croissante.</p>` },
    { bo: true, t: "Croissance comparée : $\\lim_{x\\to+\\infty}\\frac{\\e^x}{x^n}=+\\infty$", h: R`
<p><b>Étape 1 : $n=1$.</b> Soit $h(x)=\e^x-\frac{x^2}2$ sur $[0;+\infty[$. $h'(x)=\e^x-x>0$ (vu ci-dessus), donc $h$ est croissante et $h(x)\geq h(0)=1>0$. Ainsi $\e^x>\frac{x^2}{2}$, et pour $x>0$ : $\frac{\e^x}x>\frac x2$. Comme $\frac x2\to+\infty$, par comparaison $\frac{\e^x}{x}\to+\infty$.</p>
<p><b>Étape 2 : $n$ quelconque.</b> Pour $x>0$ :
$$\frac{\e^x}{x^n}=\frac{\left(\e^{\frac xn}\right)^n}{x^n}=\frac1{n^n}\left(\frac{\e^{\frac xn}}{\frac xn}\right)^n.$$
On pose $X=\frac xn\to+\infty$ : $\frac{\e^X}{X}\to+\infty$ (étape 1), donc sa puissance $n$-ième aussi, et le produit par la constante $\frac1{n^n}>0$ aussi.</p>
<p><b>Conséquence.</b> $x^n\e^{-x}=\frac{x^n}{\e^x}=\frac{1}{\e^x/x^n}\to0$.</p>` },
    { bo: false, t: "$\\lim_{x\\to-\\infty}x\\e^x=0$", h: R`
<p>On pose $X=-x\to+\infty$ : $x\e^x=-X\e^{-X}=-\frac{X}{\e^X}$. Or $\frac{X}{\e^X}\to0$ (croissance comparée), donc $x\e^x\to0$.</p>` }
  ],
  algos: [
    { bo: false, t: "Conjecturer une limite avec Python", avant: R`<p>On calcule $f(x)$ pour des $x$ de plus en plus grands. Utile pour vérifier un calcul, jamais suffisant pour le justifier.</p>`,
      code: `def f(x):
    return (2 * x + 1) / (x - 1)

for x in [10, 1000, 10**6]:
    print(x, f(x))
for x in [1.1, 1.001, 0.999]:
    print(x, f(x))`, sortie: `10 2.3333333333333335
1000 2.003003003003003
1000000 2.000003000003
1.1 31.999999999999975
1.001 3002.0000000003306
0.999 -2997.9999999999977`,
      apres: R`<p>On lit : limite $2$ en $+\infty$, $+\infty$ en $1^+$, $-\infty$ en $1^-$. Remarque : <code>f(1.1)</code> affiche <code>31.999999999999975</code> au lieu de $32$ : les nombres à virgule sont arrondis en machine.</p>` },
    { bo: false, t: "Quand l'exponentielle dépasse $x^{10}$", code: `import math

a, b = 11, 100               # e^x < x^10 en 11, > en 100
for k in range(50):
    m = (a + b) / 2
    if math.exp(m) > m**10:
        b = m
    else:
        a = m
print(round(b, 4))`, sortie: `35.7715`,
      apres: R`<p>C'est une dichotomie (chapitre 4). Au-delà de $x\approx35{,}77$, $\e^x>x^{10}$ pour toujours.</p>` }
  ],
  methodes: [
    { t: "Comment trouver une asymptote ?", h: R`
<ul><li>Limite <b>finie</b> $\ell$ en $\pm\infty$ ⟹ asymptote <b>horizontale</b> $y=\ell$.</li><li>Limite <b>infinie</b> en un réel $a$ (à gauche ou à droite) ⟹ asymptote <b>verticale</b> $x=a$. On cherche $a$ parmi les valeurs interdites.</li><li>Position relative : étudie le signe de $f(x)-\ell$.</li></ul>` },
    { t: "Comment étudier une limite en une valeur interdite ?", h: R`
<ol><li>Limite du numérateur (souvent un réel non nul) et du dénominateur ($0$).</li><li>Tableau de signes du dénominateur : $0^+$ ou $0^-$ selon le côté.</li><li>Règle des signes. Si c'est $\frac00$ : factorise par $(x-a)$ et simplifie.</li></ol>
[ex|$h(x)=\frac{x^2+3x}{x^2-4}$ en $2$]Numérateur $\to10$, dénominateur $(x-2)(x+2)\to0$ : positif si $x>2$, négatif si $1<x<2$. Donc $+\infty$ en $2^+$ et $-\infty$ en $2^-$ (Python : $h(2{,}001)\approx2501$, $h(1{,}999)\approx-2499$).[/]` },
    { t: "Comment lever une forme indéterminée avec l'exponentielle ?", h: R`
<p>Repère le terme qui domine ($\e^x$ en $+\infty$, souvent la puissance en $-\infty$ car $\e^x\to0$) et factorise par lui, puis applique les croissances comparées. Réécris $x^n\e^{-x}$ et $x^n\e^x$ sous les formes du cours.</p>` },
    { t: "Comment rédiger une composition ?", h: R`
<p>« On pose $X=u(x)$. Quand $x\to a$, $X\to b$. Or $\lim_{X\to b}v(X)=c$. Par composition, $\lim_{x\to a}v(u(x))=c$. »</p>` }
  ],
  exos: [
    { niv: 1, t: "Limites et asymptotes", enonce: R`<p>Déterminer les limites demandées et en déduire les asymptotes éventuelles.</p><ol><li>$f(x)=\frac{4x-3}{2x+1}$ en $\pm\infty$ et en $-\frac12$.</li><li>$g(x)=x^3-5x^2+1$ en $-\infty$ et $+\infty$.</li><li>$k(x)=3-\e^{-x}$ en $+\infty$.</li></ol>`,
      corrige: R`<ol><li>En $\pm\infty$ : $\frac{4x}{2x}=2$, donc $f\to2$ ; asymptote horizontale $y=2$. En $-\frac12$ : numérateur $\to-5$, dénominateur $\to0$, positif si $x>-\frac12$. Donc $f\to-\infty$ en $\left(-\frac12\right)^+$ et $+\infty$ en $\left(-\frac12\right)^-$ ; asymptote verticale $x=-\frac12$.</li>
<li>Terme de plus haut degré $x^3$ : $-\infty$ en $-\infty$, $+\infty$ en $+\infty$. Pas d'asymptote.</li>
<li>$\e^{-x}\to0$ (composition) donc $k\to3$ : asymptote $y=3$ en $+\infty$, et $k(x)<3$ : courbe en dessous.</li></ol>` },
    { niv: 1, t: "Formes indéterminées", enonce: R`<ol><li>$\lim_{x\to3}\frac{x^2-9}{x-3}$</li><li>$\lim_{x\to+\infty}\frac{\e^x+x}{\e^x}$</li><li>$\lim_{x\to-\infty}(x^2+x)\e^x$</li><li>$\lim_{x\to0}\frac{\e^x-1}{x}$</li></ol>`,
      corrige: R`<ol><li>$\frac{(x-3)(x+3)}{x-3}=x+3\to6$.</li><li>$1+\frac{x}{\e^x}\to1+0=1$.</li><li>$x^2\e^x+x\e^x\to0+0=0$ (croissances comparées en $-\infty$).</li><li>C'est le taux d'accroissement de $\exp$ en $0$ : il tend vers $\exp'(0)=\e^0=1$ (Python : $1{,}0000005$ pour $x=10^{-6}$).</li></ol>` },
    { niv: 2, t: "Gendarmes et comparaison", enonce: R`<ol><li>Montrer que pour $x>0$ : $\frac{2x-1}{x}\leq\frac{2x+\cos x}{x}\leq\frac{2x+1}{x}$. En déduire $\lim_{x\to+\infty}\frac{2x+\cos x}{x}$.</li><li>Déterminer $\lim_{x\to+\infty}\left(x^2-3x\sin x\right)$ en minorant.</li></ol>`,
      corrige: R`<ol><li>$-1\leq\cos x\leq1$, on ajoute $2x$ puis on divise par $x>0$. Les deux gendarmes valent $2\mp\frac1x\to2$ : la limite est $2$.</li><li>$-3x\sin x\geq-3x$ pour $x>0$ (car $\sin x\leq1$ et $-3x<0$). Donc $x^2-3x\sin x\geq x^2-3x=x(x-3)\to+\infty$. Par comparaison, la limite est $+\infty$.</li></ol>` },
    { niv: 2, t: "Croissances comparées", enonce: R`<p>Déterminer :</p><ol><li>$\lim_{x\to+\infty}\frac{\e^{2x}}{x^3}$</li><li>$\lim_{x\to+\infty}\frac{x^2+1}{\e^x}$</li><li>$\lim_{x\to+\infty}\left(\e^x-x^3\right)$</li><li>$\lim_{x\to+\infty}\frac{\e^x-x}{\e^x+x}$</li></ol>`,
      corrige: R`<ol><li>On pose $X=2x$ : $\frac{\e^{2x}}{x^3}=\frac{\e^X}{(X/2)^3}=8\frac{\e^X}{X^3}\to+\infty$.</li><li>$\frac{x^2}{\e^x}+\frac1{\e^x}\to0$.</li><li>$\e^x\left(1-\frac{x^3}{\e^x}\right)\to+\infty$.</li><li>On divise en haut et en bas par $\e^x$ : $\frac{1-\frac x{\e^x}}{1+\frac x{\e^x}}\to\frac{1}{1}=1$.</li></ol>` },
    { niv: 3, t: "Étude complète (type bac)", enonce: R`<p>Soit $f$ définie sur $\R$ par $f(x)=(2x-1)\e^x$, de courbe $\mathcal{C}$.</p><ol><li>Déterminer la limite de $f$ en $+\infty$.</li><li>Déterminer la limite de $f$ en $-\infty$. Interpréter graphiquement.</li><li>Montrer que $f'(x)=(2x+1)\e^x$ et dresser le tableau de variations complet de $f$.</li><li>Résoudre $f(x)=0$ et étudier le signe de $f$.</li></ol>`,
      corrige: R`<ol><li>$2x-1\to+\infty$ et $\e^x\to+\infty$ : par produit, $f\to+\infty$.</li>
<li>Forme $\infty\times0$. $f(x)=2x\e^x-\e^x$ ; $x\e^x\to0$ (croissance comparée) et $\e^x\to0$, donc $f\to0$. L'axe des abscisses ($y=0$) est asymptote horizontale à $\mathcal C$ en $-\infty$.</li>
<li>$f'(x)=2\e^x+(2x-1)\e^x=(2x+1)\e^x$. Comme $\e^x>0$, $f'$ a le signe de $2x+1$ : négative sur $\left]-\infty;-\frac12\right]$, positive ensuite. $f$ décroît de $0$ (limite) jusqu'au minimum $f\left(-\frac12\right)=-2\e^{-\frac12}\approx-1{,}213$, puis croît vers $+\infty$.</li>
<li>$\e^x\neq0$, donc $f(x)=0\iff2x-1=0\iff x=\frac12$. $f(x)<0$ sur $\left]-\infty;\frac12\right[$, $f(x)>0$ sur $\left]\frac12;+\infty\right[$.</li></ol>
<p class="stylo">Remarque : sur $\left]-\infty;-\frac12\right]$, $f$ est négative ; la courbe est donc sous son asymptote $y=0$ en $-\infty$.</p>` }
  ],
  annales: [
    { ref: "Bac 2026, Polynésie, 16 juin 2026 (sujet 1), exercice 2, affirmation 1", url: "https://www.apmep.fr/IMG/pdf/Bac_spe_Polynesie_J1_16_06_2026_DV.pdf", h: R`Vrai/faux : « La limite de $f(x)=(x+1)\e^{-x}$ en $+\infty$ est $+\infty$ ». Faux, par croissances comparées (la limite est $0$).` },
    { ref: "Bac 2025, Métropole, 18 juin 2025 (sujet 2), exercice 4, partie B, question 2b", url: "https://www.apmep.fr/IMG/pdf/Metropole__spe_J2_18_06_2025_DV_2.pdf", h: R`Vitesse d'un chariot $v(t)=(12+t)\e^{-0{,}6t}$ : déterminer sa limite en $+\infty$ en utilisant une écriture donnée qui fait apparaître $\frac{0{,}6t}{\e^{0{,}6t}}$. La partie A fait lire une asymptote sur un graphique.` },
    { ref: "Bac 2026, Métropole – La Réunion, 8 septembre 2026, exercice 4, partie B, question 1", url: "https://www.apmep.fr/IMG/pdf/Metropole_J_spe_8osep_2026.pdf", h: R`Quantité de médicament $f(t)=4t\e^{-\frac32t}$ : limite en $+\infty$ et interprétation.` }
  ],
  retenir: R`
[def|Asymptotes]$\lim_{x\to\pm\infty}f(x)=\ell$ ⟹ asymptote horizontale $y=\ell$.<br>$\lim_{x\to a}f(x)=\pm\infty$ (d'un côté au moins) ⟹ asymptote verticale $x=a$.[/]
<h3>Références</h3><ul><li>$\e^x\to+\infty$ en $+\infty$ ; $\e^x\to0$ en $-\infty$.</li><li>$\frac1{x^n}\to0$ en $\pm\infty$ ; $\frac1x\to\pm\infty$ en $0^\pm$.</li><li>Polynôme en $\pm\infty$ : comme son terme de plus haut degré ; quotient : quotient des termes de plus haut degré.</li></ul>
[thm|Croissances comparées]$\frac{\e^x}{x^n}\to+\infty$ et $x^n\e^{-x}\to0$ en $+\infty$ ; $x^n\e^x\to0$ en $-\infty$.[/]
<h3>Outils</h3><ul><li>F.I. : $\infty-\infty$, $0\times\infty$, $\frac\infty\infty$, $\frac00$.</li><li>Composition : poser $X=u(x)$.</li><li>Comparaison, gendarmes (avec $-1\leq\cos x\leq1$).</li><li>Valeur interdite : tableau de signes du dénominateur, limites à gauche et à droite.</li></ul>
<p class="stylo">En $0$, c'est le plus bas degré qui domine ; en $\pm\infty$, le plus haut.</p>`,
  qcm: [
    { q: R`$\lim_{x\to+\infty}\frac{4x^2-1}{2x^2+x}=$`, c: ["$0$", "$2$", "$4$", "$+\\infty$"], r: 1, e: R`Quotient des termes de plus haut degré : $\frac{4x^2}{2x^2}=2$.`, ref: "operations" },
    { q: R`Si $\lim_{x\to+\infty}f(x)=3$, alors :`, c: [R`$x=3$ est asymptote verticale`, R`$y=3$ est asymptote horizontale en $+\infty$`, R`$f(x)<3$ pour tout $x$`, R`$f$ est croissante`], r: 1, e: R`Limite finie en l'infini ⟹ asymptote horizontale. La position relative demande une étude de signe.`, ref: "infini" },
    { q: R`$\lim_{x\to2^-}\frac{1}{x-2}=$`, c: ["$+\\infty$", "$-\\infty$", "$0$", "$\\frac12$"], r: 1, e: R`Pour $x<2$, $x-2<0$ et tend vers $0$ : le quotient tend vers $-\infty$.`, ref: "point" },
    { q: R`$\lim_{x\to-\infty}\e^x=$`, c: ["$-\\infty$", "$0$", "$1$", "$+\\infty$"], r: 1, e: R`L'axe des abscisses est asymptote à la courbe de l'exponentielle en $-\infty$.`, ref: "reference" },
    { q: R`$\lim_{x\to+\infty}x^5\e^{-x}=$`, c: ["$+\\infty$", "$0$", "$1$", "forme indéterminée sans limite"], r: 1, e: R`Croissance comparée : l'exponentielle l'emporte sur toute puissance.`, ref: "croissances" },
    { q: R`$\lim_{x\to-\infty}x\e^x=$`, c: ["$-\\infty$", "$0$", "$1$", "$+\\infty$"], r: 1, e: R`Croissance comparée en $-\infty$ : $x^n\e^x\to0$.`, ref: "croissances" },
    { q: R`$\lim_{x\to+\infty}\e^{-x^2}=$`, c: ["$0$", "$1$", "$+\\infty$", "$-\\infty$"], r: 0, e: R`Composition : $X=-x^2\to-\infty$ et $\e^X\to0$.`, ref: "operations" },
    { q: R`$\lim_{x\to1}\frac{x^2-1}{x-1}=$`, c: ["$0$", "$1$", "$2$", "n'existe pas"], r: 2, e: R`Forme $\frac00$ ; on simplifie par $x-1$ : $x+1\to2$.`, ref: "operations" },
    { q: R`$\lim_{x\to+\infty}\frac{\cos x}{x}=$`, c: ["$0$", "$1$", "n'existe pas", "$+\\infty$"], r: 0, e: R`Gendarmes : $-\frac1x\leq\frac{\cos x}x\leq\frac1x$ pour $x>0$.`, ref: "comparaison" },
    { q: R`La démonstration de $\lim\frac{\e^x}{x}=+\infty$ s'appuie sur :`, c: [R`$\e^x\geq\frac{x^2}2$ pour $x\geq0$, puis comparaison`, R`le théorème des gendarmes avec $\cos$`, R`la quantité conjuguée`, R`l'inégalité de Bernoulli`], r: 0, e: R`On étudie $h(x)=\e^x-\frac{x^2}2$, croissante et positive sur $[0;+\infty[$ ; alors $\frac{\e^x}x\geq\frac x2$.`, ref: "croissances" },
    { q: R`$\lim_{x\to+\infty}(\e^x-x^3)=$`, c: ["$0$", "$-\\infty$", "$+\\infty$", "F.I. sans limite"], r: 2, e: R`$\e^x\left(1-\frac{x^3}{\e^x}\right)$ ; la parenthèse tend vers $1$.`, ref: "croissances" },
    { q: R`Près de $0$, $x^3+2x$ se comporte comme :`, c: ["$x^3$", "$2x$", "$3x$", "$x^3+2x$ n'a pas de terme dominant"], r: 1, e: R`En $0$, c'est le terme de plus bas degré qui domine.`, ref: "pieges" },
    { q: R`$f(x)=\frac{2x+1}{x-1}$. Ses asymptotes sont :`, c: [R`$x=1$ et $y=2$`, R`$x=2$ et $y=1$`, R`$x=-\frac12$ et $y=2$`, R`seulement $y=2$`], r: 0, e: R`Limite $2$ en $\pm\infty$ ; limites infinies en $1^\pm$.`, ref: "point" }
  ],
  cartes: [
    [R`Asymptote horizontale : condition`, R`$\lim_{x\to\pm\infty}f(x)=\ell$ (réel) ⟹ $y=\ell$.`],
    [R`Asymptote verticale : condition`, R`$\lim_{x\to a}f(x)=\pm\infty$ ⟹ $x=a$.`],
    [R`$\lim_{x\to-\infty}\e^x$ et $\lim_{x\to+\infty}\e^x$`, R`$0$ et $+\infty$.`],
    [R`$\lim_{x\to+\infty}\frac{\e^x}{x^n}$`, R`$+\infty$`],
    [R`$\lim_{x\to+\infty}x^n\e^{-x}$`, R`$0$`],
    [R`$\lim_{x\to-\infty}x^n\e^x$`, R`$0$`],
    [R`$\lim_{x\to0}\frac{\e^x-1}{x}$`, R`$1$ (nombre dérivé de $\exp$ en $0$).`],
    [R`Limite d'un quotient de polynômes en $\pm\infty$`, R`Celle du quotient des termes de plus haut degré.`],
    [R`Théorème de composition`, R`$u(x)\to b$ et $v(X)\to c$ quand $X\to b$ ⟹ $v(u(x))\to c$.`],
    [R`$\lim_{x\to0^-}\frac1x$ ?`, R`$-\infty$`],
    [R`Forme $\frac00$ en $a$ : réflexe`, R`Factoriser numérateur et dénominateur par $(x-a)$.`],
    [R`Encadrer $\cos x$`, R`$-1\leq\cos x\leq1$`]
  ]
};
