/* ---------- Chapitre 8 : primitives, équations différentielles ---------- */
var CH8 = {
  id: "ch8", num: 8, statut: "ok", partie: "Analyse", titre: "Primitives, équations différentielles", court: "Primitives, éq. diff.",
  sous: "Retrouver une fonction à partir de sa dérivée : l'inconnue est une fonction.",
  resume: "$y'=f$, primitives usuelles, $y'=ay$, $y'=ay+b$, $y'=ay+f$, méthode d'Euler.",
  essentiel: [
    R`Une <b>primitive</b> de $f$ sur $I$ est une fonction $F$ telle que $F'=f$ : c'est une solution de l'équation différentielle $y'=f$. Deux primitives diffèrent d'une constante.`,
    R`On lit le tableau des dérivées à l'envers : primitive de $x^n$ ($n\neq-1$) : $\frac{x^{n+1}}{n+1}$ ; de $\frac1x$ : $\ln x$ ; de $\e^x$ : $\e^x$ ; de $\cos$ : $\sin$ ; de $\sin$ : $-\cos$ ; et de $u'\e^u$ : $\e^u$, de $\frac{u'}u$ : $\ln u$ ($u>0$).`,
    R`Les solutions de $y'=ay$ sont les fonctions $x\mapsto C\e^{ax}$, $C$ réel.`,
    R`Pour $y'=ay+b$ ($a\neq0$) : la constante $-\frac ba$ est solution, et toutes les solutions sont $x\mapsto C\e^{ax}-\frac ba$.`,
    R`Une condition initiale $y(x_0)=y_0$ fixe la constante : il y a une seule solution qui passe par un point donné.`
  ],
  attendus: [
    R`Calculer une primitive en utilisant les primitives de référence et les fonctions de la forme $(v'\circ u)\times u'$.`,
    R`Pour $y'=ay+b$ ($a\neq0$) : déterminer une solution particulière constante, puis toutes les solutions.`,
    R`Pour $y'=ay+f$ : à partir d'une solution particulière donnée, déterminer toutes les solutions.`,
    R`Démonstrations exigibles : deux primitives d'une même fonction continue sur un intervalle diffèrent d'une constante ; résolution de $y'=ay$.`,
    R`Algorithme : méthode d'Euler pour $y'=f$ et $y'=ay+b$. Toute fonction continue sur un intervalle admet des primitives (admis ici, démontré au chapitre 9).`
  ],
  premiere: R`
<ul><li>Dérivées : $(x^n)'=nx^{n-1}$, $\left(\frac1x\right)'=-\frac1{x^2}$, $(\sqrt x)'=\frac1{2\sqrt x}$, $(\e^{ax+b})'=a\e^{ax+b}$.</li>
<li>Une fonction dont la dérivée est nulle sur un <b>intervalle</b> y est constante.</li>
<li>Chapitre 4 : $(v\circ u)'=(v'\circ u)\times u'$ ; chapitre 6 : $\ln'(x)=\frac1x$ ; chapitre 7 : $\sin'=\cos$, $\cos'=-\sin$.</li></ul>`,
  cours: [
    { id: "primitive", titre: "Équation $y'=f$ et primitives", html: R`
[def|Équation différentielle, primitive]Une <b>équation différentielle</b> est une équation dont l'inconnue est une fonction $y$, et qui fait intervenir sa dérivée $y'$. Une <b>primitive</b> de $f$ sur un intervalle $I$ est une fonction $F$ dérivable sur $I$ telle que $F'=f$ : c'est une solution de $y'=f$.[/]
[ex|Vérifier une primitive]$F(x)=x^3+x^2-5x$ est une primitive de $f(x)=3x^2+2x-5$ : on dérive $F$ et on retrouve $f$. Mais $F(x)+7$ aussi.[/]
[thm|Toutes les primitives]Si $F$ est une primitive de $f$ sur un intervalle $I$, les primitives de $f$ sur $I$ sont exactement les fonctions $x\mapsto F(x)+C$, $C$ réel. (Démonstration exigible : deux primitives diffèrent d'une constante.)[/]
[prop|Une seule primitive passe par un point]Pour $x_0\in I$ et $y_0$ réel, il existe une unique primitive $F$ de $f$ telle que $F(x_0)=y_0$.[/]
[ex|Condition initiale]Primitive de $f(x)=2x$ qui vaut $5$ en $1$ : $F(x)=x^2+C$ et $F(1)=1+C=5$, donc $F(x)=x^2+4$.[/]
<div data-anim="primitives"></div>
[thm|Existence (admise ici)]Toute fonction continue sur un intervalle admet des primitives. Mais certaines n'ont pas d'expression avec les fonctions usuelles : c'est le cas de $x\mapsto\e^{-x^2}$.[/]` },
    { id: "usuelles", titre: "Primitives usuelles et formes composées", html: R`
<div class="tab-wrap"><table><tr><th>$f(x)$</th><th>Une primitive $F(x)$</th><th>Intervalle</th></tr>
<tr><td>$k$ (constante)</td><td>$kx$</td><td>$\R$</td></tr>
<tr><td>$x^n$, $n\in\Z$, $n\neq-1$</td><td>$\frac{x^{n+1}}{n+1}$</td><td>$\R$ si $n\geq0$ ; $]0;+\infty[$ ou $]-\infty;0[$ sinon</td></tr>
<tr><td>$\frac1x$</td><td>$\ln x$</td><td>$]0;+\infty[$</td></tr>
<tr><td>$\frac1{\sqrt x}$</td><td>$2\sqrt x$</td><td>$]0;+\infty[$</td></tr>
<tr><td>$\e^x$ ; $\e^{ax+b}$ ($a\neq0$)</td><td>$\e^x$ ; $\frac1a\e^{ax+b}$</td><td>$\R$</td></tr>
<tr><td>$\cos x$ ; $\sin x$</td><td>$\sin x$ ; $-\cos x$</td><td>$\R$</td></tr></table></div>
<div class="tab-wrap"><table><tr><th>Forme reconnue</th><th>Une primitive</th><th>Condition</th></tr>
<tr><td>$u'u^n$ ($n\geq1$)</td><td>$\frac{u^{n+1}}{n+1}$</td><td></td></tr>
<tr><td>$\frac{u'}{u^2}$</td><td>$-\frac1u$</td><td>$u\neq0$</td></tr>
<tr><td>$\frac{u'}{\sqrt u}$</td><td>$2\sqrt u$</td><td>$u>0$</td></tr>
<tr><td>$\frac{u'}u$</td><td>$\ln u$</td><td>$u>0$</td></tr>
<tr><td>$u'\e^u$</td><td>$\e^u$</td><td></td></tr>
<tr><td>$(v'\circ u)\times u'$</td><td>$v\circ u$</td><td></td></tr></table></div>
[meth|Ajuster une constante multiplicative]Si on reconnaît « presque » $u'$, on multiplie et on divise : pour $x(x^2+1)^3$, $u=x^2+1$, $u'=2x$, donc $x(x^2+1)^3=\frac12u'u^3$ et une primitive est $\frac12\times\frac{u^4}4=\frac{(x^2+1)^4}8$.[/]
[ex|Six primitives (chacune vérifiée en dérivant)]
<ul><li>$2x\e^{x^2}$ : $\e^{x^2}$.</li><li>$\frac{2x}{x^2+1}$ : $\ln(x^2+1)$.</li><li>$\cos(2x)$ : $\frac12\sin(2x)$.</li><li>$\frac{1}{2x+1}$ sur $\left]-\frac12;+\infty\right[$ : $\frac12\ln(2x+1)$.</li><li>$\frac{x}{\sqrt{x^2+1}}$ : $\sqrt{x^2+1}$.</li><li>$\sin x\cos x$ : $\frac{\sin^2x}2$ (forme $u'u$ avec $u=\sin$).</li></ul>[/]
[piege|Pas de « primitive d'un produit »]Une primitive de $fg$ n'est <b>pas</b> le produit des primitives. On cherche une forme du tableau, ou (chapitre 9) une intégration par parties.[/]` },
    { id: "yay", titre: "L'équation $y'=ay$", html: R`
[thm|Solutions de $y'=ay$]Soit $a$ un réel. Les solutions sur $\R$ de $y'=ay$ sont les fonctions $x\mapsto C\e^{ax}$, où $C$ est un réel quelconque. (Démonstration exigible.)[/]
<p>Il y a une infinité de solutions, une par valeur de $C$ ; la condition $y(0)=y_0$ impose $C=y_0$ : $y(x)=y_0\e^{ax}$.</p>
[ex|Croissance d'une population de bactéries (modèle)]Si $N'=0{,}7N$ (temps en heures) et $N(0)=100$, alors $N(t)=100\e^{0{,}7t}$. Elle double quand $\e^{0{,}7t}=2$, soit $t=\frac{\ln2}{0{,}7}\approx0{,}99$ h ; après $5$ h, $N(5)=100\e^{3{,}5}\approx3\,312$.[/]
[prop|Allure des courbes]Si $a>0$ : croissance (ou décroissance) exponentielle qui s'emballe ; si $a<0$ : les solutions tendent vers $0$ en $+\infty$ ; $C=0$ donne la solution nulle. Une seule courbe passe par chaque point.[/]
<p><span class="tag hp">Pour aller plus loin</span> Le programme cite d'autres équations dont on peut vérifier des solutions sans les résoudre : $y'=y^2$ (par exemple $y=-\frac1x$), $y''+2y=0$ (par exemple $y=\cos(\sqrt2x)$), et l'équation logistique (sujet de Métropole du 17 juin 2025, posidonie).</p>` },
    { id: "yayb", titre: "L'équation $y'=ay+b$", html: R`
[thm|Solutions de $y'=ay+b$ ($a\neq0$)]La fonction constante $x\mapsto-\frac ba$ est solution. Les solutions sont les fonctions $x\mapsto C\e^{ax}-\frac ba$, $C$ réel.[/]
<p><b>Pourquoi ?</b> Une constante $k$ est solution si $0=ak+b$, soit $k=-\frac ba$. Puis $y$ est solution si et seulement si $y-k$ vérifie $(y-k)'=y'=ay+b=a(y-k)$ : $y-k$ est solution de $Y'=aY$, donc $y-k=C\e^{ax}$.</p>
<div data-anim="champ"></div>
[ex|Loi de refroidissement]Un café à $90\,^\circ$C dans une pièce à $20\,^\circ$C : $T'=-0{,}1(T-20)=-0{,}1T+2$ ($t$ en minutes). Solution constante : $20$ ; donc $T(t)=20+C\e^{-0{,}1t}$, et $T(0)=90$ donne $C=70$ : $T(t)=20+70\e^{-0{,}1t}$. $T(10)\approx45{,}8\,^\circ$C ; $T(t)<30\iff\e^{-0{,}1t}<\frac17\iff t>10\ln7\approx19{,}5$ min.[/]
[meth|Les trois étapes]1. Solution constante $k=-\frac ba$. 2. Solutions générales $C\e^{ax}+k$. 3. Condition initiale pour trouver $C$.[/]` },
    { id: "yayf", titre: "L'équation $y'=ay+f$ : avec une solution particulière", html: R`
[thm|Principe]Si $g$ est une solution particulière de $y'=ay+f$, alors les solutions sont les fonctions $g+C\e^{ax}$ ($C$ réel) : « solution particulière + solutions de l'équation sans second membre $y'=ay$ ».[/]
[ex|Au bac (Métropole, 18 juin 2025, sujet 2)]$(E)$ : $y'+0{,}6y=\e^{-0{,}6t}$, c'est-à-dire $y'=-0{,}6y+\e^{-0{,}6t}$. On vérifie que $g(t)=t\e^{-0{,}6t}$ est solution : $g'(t)=\e^{-0{,}6t}-0{,}6t\e^{-0{,}6t}=-0{,}6g(t)+\e^{-0{,}6t}$. Les solutions sont $t\mapsto t\e^{-0{,}6t}+C\e^{-0{,}6t}=(t+C)\e^{-0{,}6t}$ ; avec $v(0)=12$ : $v(t)=(12+t)\e^{-0{,}6t}$.[/]
[meth|Pourquoi ça marche]$y$ solution ⟺ $(y-g)'=a(y-g)$ ⟺ $y-g=C\e^{ax}$. C'est la même idée que pour $y'=ay+b$, avec $g$ à la place de la constante.[/]` },
    { id: "euler", titre: "La méthode d'Euler", html: R`
<p>Quand on ne sait pas résoudre, on construit une solution approchée pas à pas : à partir du point $(x_n;y_n)$, on suit la tangente donnée par l'équation sur une petite longueur $h$ :</p>
$$x_{n+1}=x_n+h,\qquad y_{n+1}=y_n+h\times y'(x_n).$$
[ex|Avec $y'=y$, $y(0)=1$]$y_{n+1}=y_n+hy_n=(1+h)y_n$. Avec $h=0{,}1$, dix pas donnent $y(1)\approx1{,}1^{10}\approx2{,}594$ ; avec $h=0{,}01$, cent pas donnent $\approx2{,}705$. La vraie valeur est $\e\approx2{,}718$ : plus le pas est petit, meilleure est l'approximation.[/]` }
  ],
  pieges: [
    { t: "Oublier la constante", h: R`« La » primitive n'existe pas : il y en a une infinité. Sans condition initiale, écris $F(x)+C$.` },
    { t: "Primitive de $\\e^{ax}$", h: R`Une primitive de $\e^{3x}$ est $\frac13\e^{3x}$, pas <span class="rature">$3\e^{3x}$</span> (ça, c'est sa dérivée).` },
    { t: "Primitive de $\\sin$", h: R`$-\cos$, avec le signe moins : $(-\cos)'=\sin$.` },
    { t: "La solution constante de $y'=ay+b$", h: R`C'est $-\frac ba$, pas <span class="rature">$\frac ba$</span>. Vérifie : $a\times\left(-\frac ba\right)+b=0$.` },
    { t: "Confondre $y'=ay+b$ et $y=ax+b$", h: R`Dans une équation différentielle, l'inconnue est une fonction : on ne « résout » pas en $x$.` }
  ],
  demos: [
    { bo: true, t: "Deux primitives d'une même fonction diffèrent d'une constante", h: R`
<p>Soient $F$ et $G$ deux primitives de $f$ sur un intervalle $I$. Posons $H=F-G$. $H$ est dérivable sur $I$ et $H'=F'-G'=f-f=0$.</p>
<p>Une fonction de dérivée nulle sur un <b>intervalle</b> est constante : il existe un réel $C$ tel que $H(x)=C$ pour tout $x\in I$, soit $F(x)=G(x)+C$.</p>
<p>Réciproquement, $G+C$ est une primitive : $(G+C)'=G'=f$.</p>
<p class="stylo">Le mot « intervalle » compte : sur $]-\infty;0[\cup]0;+\infty[$, la « constante » peut être différente de chaque côté.</p>` },
    { bo: true, t: "Résolution de $y'=ay$", h: R`
<p><b>Les fonctions $C\e^{ax}$ sont solutions</b> : $(C\e^{ax})'=aC\e^{ax}$.</p>
<p><b>Ce sont les seules.</b> Soit $y$ une solution. On pose $z(x)=y(x)\e^{-ax}$. Alors
$$z'(x)=y'(x)\e^{-ax}-ay(x)\e^{-ax}=\left(y'(x)-ay(x)\right)\e^{-ax}=0.$$
Donc $z$ est constante sur $\R$ : $z(x)=C$, et $y(x)=C\e^{ax}$.</p>
<p class="stylo">L'astuce : multiplier par $\e^{-ax}$ pour faire apparaître une dérivée nulle.</p>` }
  ],
  algos: [
    { bo: true, t: "Méthode d'Euler pour $y'=ay+b$", avant: R`<p>$y'=-0{,}5y+1$, $y(0)=0$, pas $h=0{,}5$, jusqu'à $x=4$. La solution exacte est $y(x)=2-2\e^{-0{,}5x}$.</p>`,
      code: `from math import exp

def euler(a, b, y0, h, n):
    x, y = 0, y0
    L = [y]
    for k in range(n):
        y = y + h * (a * y + b)     # on suit la tangente
        x = x + h
        L.append(round(y, 4))
    return L

print(euler(-0.5, 1, 0, 0.5, 8))
print(2 - 2 * exp(-2))`, sortie: `[0, 0.5, 0.875, 1.1562, 1.3672, 1.5254, 1.644, 1.733, 1.7998]
1.7293294335267746`,
      apres: R`<p>En $x=4$ : Euler donne $1{,}80$, la vraie valeur est $1{,}73$. Avec un pas plus petit, l'écart diminue (voir l'animation du cours).</p>` },
    { bo: true, t: "Méthode d'Euler pour $y'=y$ : une approximation de $\\e$", code: `y = 1
h = 0.01
for k in range(100):
    y = y + h * y
print(y)`, sortie: `2.704813829421526` }
  ],
  methodes: [
    { t: "Comment trouver une primitive ?", h: R`
<ol><li>Linéarité : on traite chaque terme, les constantes multiplicatives sortent.</li><li>Fonction de référence ? Lire le tableau.</li><li>Sinon, chercher une forme $u'u^n$, $\frac{u'}u$, $u'\e^u$, $\frac{u'}{\sqrt u}$… en repérant « $u$ et sa dérivée » ; ajuster la constante.</li><li><b>Vérifier en dérivant.</b></li></ol>` },
    { t: "Comment résoudre $y'=ay+b$ avec une condition initiale ?", h: R`
<p>Solution constante $-\frac ba$ ; solutions $C\e^{ax}-\frac ba$ ; puis $y(x_0)=y_0$ donne $C$. Rédaction au bac : « D'après le cours, les solutions de $(E)$ sont les fonctions … ».</p>` },
    { t: "Comment exploiter une solution particulière donnée ?", h: R`
<ol><li>Vérifier qu'elle est solution (dériver, remplacer).</li><li>Montrer que « $y$ solution ⟺ $y-g$ solution de $y'=ay$ ».</li><li>Conclure : $y=g+C\e^{ax}$.</li></ol>` }
  ],
  exos: [
    { niv: 1, t: "Primitives", enonce: R`<p>Déterminer une primitive de chaque fonction sur l'intervalle indiqué.</p><ol><li>$f(x)=4x^3-6x+1$ sur $\R$</li><li>$g(x)=\frac1{x^3}$ sur $]0;+\infty[$</li><li>$h(x)=\e^{-2x}$ sur $\R$</li><li>$k(x)=\frac{3}{3x+1}$ sur $\left]-\frac13;+\infty\right[$</li><li>$m(x)=\sin(3x)$ sur $\R$</li></ol>`,
      corrige: R`<ol><li>$x^4-3x^2+x$.</li><li>$x^{-3}$ a pour primitive $\frac{x^{-2}}{-2}=-\frac1{2x^2}$.</li><li>$-\frac12\e^{-2x}$.</li><li>Forme $\frac{u'}u$ : $\ln(3x+1)$.</li><li>$-\frac13\cos(3x)$.</li></ol>` },
    { niv: 1, t: "Équations différentielles", enonce: R`<ol><li>Résoudre $y'=3y$ avec $y(0)=2$.</li><li>Résoudre $y'=-2y+6$ avec $y(0)=1$.</li></ol>`,
      corrige: R`<ol><li>$y=C\e^{3x}$, $C=2$ : $y(x)=2\e^{3x}$.</li><li>Constante : $-\frac6{-2}=3$. $y=C\e^{-2x}+3$, et $y(0)=C+3=1$, $C=-2$ : $y(x)=3-2\e^{-2x}$ (vérifié en remplaçant dans l'équation).</li></ol>` },
    { niv: 2, t: "Formes composées", enonce: R`<p>Primitives de : $f(x)=x\e^{x^2}$ ; $g(x)=\frac{x}{x^2+4}$ ; $h(x)=\frac{\e^x}{(\e^x+1)^2}$ ; $k(x)=\cos x\sin^2x$.</p>`,
      corrige: R`<p>$f$ : $\frac12\e^{x^2}$ ; $g$ : $\frac12\ln(x^2+4)$ ; $h$ : forme $\frac{u'}{u^2}$ avec $u=\e^x+1$ : $-\frac1{\e^x+1}$ ; $k$ : forme $u'u^2$ avec $u=\sin x$ : $\frac{\sin^3x}3$.</p>` },
    { niv: 2, t: "Solution particulière donnée", enonce: R`<p>$(E)$ : $y'=2y-4x$.</p><ol><li>Montrer que $g(x)=2x+1$ est solution de $(E)$.</li><li>En déduire toutes les solutions, puis celle qui vaut $0$ en $0$.</li></ol>`,
      corrige: R`<ol><li>$g'(x)=2$ et $2g(x)-4x=4x+2-4x=2$. ✓</li><li>$y=2x+1+C\e^{2x}$ ; $y(0)=1+C=0$, $C=-1$ : $y(x)=2x+1-\e^{2x}$.</li></ol>` },
    { niv: 3, t: "Le café refroidit (type bac)", enonce: R`<p>On note $T(t)$ la température d'un café, en $^\circ$C, $t$ minutes après l'avoir servi. On admet que $T$ est solution de $(E)$ : $y'=-0{,}1y+2$ et que $T(0)=90$.</p><ol><li>Déterminer la solution constante de $(E)$ et l'interpréter.</li><li>Déterminer $T(t)$.</li><li>Calculer $T(10)$ arrondi au dixième, et la limite de $T$ en $+\infty$.</li><li>Au bout de combien de temps le café sera-t-il en dessous de $30\,^\circ$C ? Donner la durée en minutes et secondes, puis le premier nombre entier de minutes qui convient.</li><li>Écrire un programme Python appliquant la méthode d'Euler avec un pas de $0{,}1$ pour estimer $T(10)$.</li></ol>`,
      corrige: R`<ol><li>$0=-0{,}1k+2$ : $k=20$, la température de la pièce (équilibre).</li><li>$T(t)=20+C\e^{-0{,}1t}$ et $T(0)=20+C=90$ : $T(t)=20+70\e^{-0{,}1t}$.</li><li>$T(10)=20+70\e^{-1}\approx45{,}8\,^\circ$C. $\e^{-0{,}1t}\to0$ donc $T\to20$.</li><li>$70\e^{-0{,}1t}<10\iff\e^{-0{,}1t}<\frac17\iff t>10\ln7\approx19{,}46$, soit environ $19$ min $28$ s : en minutes entières, le café est sous $30\,^\circ$C au bout de $20$ minutes (à $19$ minutes, il est encore à $T(19)\approx30{,}5\,^\circ$C).</li><li><code>T = 90</code>, puis <code>for k in range(100): T = T + 0.1*(-0.1*T + 2)</code>, puis <code>print(T)</code> : on obtient environ $45{,}6$ (calcul refait en Python), proche de la valeur exacte $45{,}75$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole, 17 juin 2026 (sujet 2), exercice 2, partie B", url: "https://www.apmep.fr/IMG/pdf/BAC_generale_specialite_J2_2026-06-17_Metropole_FK-v4.pdf", h: R`$y'=-0{,}005y+6$, $v(0)=0$ : solutions, $v(t)=1200\left(1-\e^{-0{,}005t}\right)$, limite, seuil de $50$ litres (contrôle : $t\approx8{,}51$ h, soit $8$ h $31$ min).` },
    { ref: "Bac 2026, Métropole, 16 juin 2026 (sujet 1), exercice 3, partie A", url: "https://www.apmep.fr/IMG/pdf/BAC_General_Specialite_Sujet_J1_metropole_FK-v2.pdf", h: R`Chauffage : $y'=-0{,}035y+0{,}91$, $T(0)=18$, $T(t)=26-8\e^{-0{,}035t}$ ; la pièce atteint $20\,^\circ$C après environ $82$ minutes (contrôle : $1$ h $22$ min).` },
    { ref: "Bac 2025, Métropole, 18 juin 2025 (sujet 2), exercice 4, partie B, question 1", url: "https://www.apmep.fr/IMG/pdf/Metropole__spe_J2_18_06_2025_DV_2.pdf", h: R`$y'+0{,}6y=\e^{-0{,}6t}$ avec la solution particulière $t\e^{-0{,}6t}$ : traité dans le cours.` },
    { ref: "Bac 2025, Centres étrangers, 13 juin 2025 (sujet 2), exercice 2, partie C", url: "https://www.apmep.fr/IMG/pdf/Etranger_spe_J2_13_06_2025_DV.pdf", h: R`Réécrire $\frac1{1+\e^{-0{,}2x}}=\frac{\e^{0{,}2x}}{1+\e^{0{,}2x}}$, puis en trouver une primitive (forme $\frac{u'}u$ : $5\ln\left(1+\e^{0{,}2x}\right)$) pour une valeur moyenne.` }
  ],
  retenir: R`
[def|Primitive]$F'=f$ sur $I$. Toutes les primitives : $F+C$. Une seule vérifie $F(x_0)=y_0$.[/]
<div class="tab-wrap"><table><tr><th>$f$</th><th>$F$</th><th>$f$</th><th>$F$</th></tr>
<tr><td>$x^n$ ($n\neq-1$)</td><td>$\frac{x^{n+1}}{n+1}$</td><td>$u'u^n$</td><td>$\frac{u^{n+1}}{n+1}$</td></tr>
<tr><td>$\frac1x$</td><td>$\ln x$</td><td>$\frac{u'}u$ ($u>0$)</td><td>$\ln u$</td></tr>
<tr><td>$\frac1{\sqrt x}$</td><td>$2\sqrt x$</td><td>$\frac{u'}{\sqrt u}$</td><td>$2\sqrt u$</td></tr>
<tr><td>$\e^{ax+b}$</td><td>$\frac1a\e^{ax+b}$</td><td>$u'\e^u$</td><td>$\e^u$</td></tr>
<tr><td>$\cos$ ; $\sin$</td><td>$\sin$ ; $-\cos$</td><td>$\frac{u'}{u^2}$</td><td>$-\frac1u$</td></tr></table></div>
[thm|Équations différentielles]$y'=ay$ : $y=C\e^{ax}$. $y'=ay+b$ ($a\neq0$) : $y=C\e^{ax}-\frac ba$. $y'=ay+f$ : $y=g+C\e^{ax}$ ($g$ solution particulière).[/]
<p><b>Euler</b> : $y_{n+1}=y_n+h\,y'_n$.</p>
<p class="stylo">Toujours vérifier une primitive en la dérivant.</p>`,
  qcm: [
    { q: R`Une primitive de $f(x)=6x^2$ est :`, c: [R`$12x$`, R`$2x^3$`, R`$6x^3$`, R`$3x^2$`], r: 1, e: R`$(2x^3)'=6x^2$.`, ref: "usuelles" },
    { q: R`Une primitive de $\e^{2x}$ est :`, c: [R`$2\e^{2x}$`, R`$\frac12\e^{2x}$`, R`$\e^{2x}$`, R`$\e^{x^2}$`], r: 1, e: R`$\left(\frac12\e^{2x}\right)'=\e^{2x}$.`, ref: "usuelles" },
    { q: R`Une primitive de $\sin x$ est :`, c: [R`$\cos x$`, R`$-\cos x$`, R`$-\sin x$`, R`$\sin^2 x$`], r: 1, e: R`$(-\cos)'=\sin$.`, ref: "usuelles" },
    { q: R`Une primitive de $\frac{2x}{x^2+1}$ est :`, c: [R`$\ln(x^2+1)$`, R`$\frac{1}{x^2+1}$`, R`$x^2\ln x$`, R`$2\ln x$`], r: 0, e: R`Forme $\frac{u'}u$ avec $u=x^2+1>0$.`, ref: "usuelles" },
    { q: R`Si $F$ et $G$ sont deux primitives de $f$ sur un intervalle :`, c: ["$F=G$", "$F-G$ est constante", "$F\\times G=f$", "$F+G=f$"], r: 1, e: R`Démonstration exigible : $(F-G)'=0$ sur un intervalle.`, ref: "primitive" },
    { q: R`Les solutions de $y'=-2y$ sont :`, c: [R`$C\e^{2x}$`, R`$C\e^{-2x}$`, R`$-2x+C$`, R`$\e^{-2x}+C$`], r: 1, e: R`$y'=ay$ ⟹ $y=C\e^{ax}$ avec $a=-2$.`, ref: "yay" },
    { q: R`La solution constante de $y'=4y-8$ est :`, c: ["$-2$", "$2$", "$8$", "$4$"], r: 1, e: R`$0=4k-8$ ⟹ $k=2=-\frac{b}{a}$ avec $a=4$, $b=-8$.`, ref: "yayb" },
    { q: R`Les solutions de $y'=-y+3$ sont :`, c: [R`$C\e^{-x}+3$`, R`$C\e^{-x}-3$`, R`$C\e^{x}+3$`, R`$3\e^{-x}+C$`], r: 0, e: R`Constante $-\frac{3}{-1}=3$, puis $C\e^{-x}+3$.`, ref: "yayb" },
    { q: R`La solution de $y'=0{,}5y$ telle que $y(0)=4$ est :`, c: [R`$4\e^{0{,}5x}$`, R`$0{,}5\e^{4x}$`, R`$\e^{0{,}5x}+4$`, R`$4\e^{-0{,}5x}$`], r: 0, e: R`$y=C\e^{0{,}5x}$ et $C=y(0)=4$.`, ref: "yay" },
    { q: R`Si $g$ est solution de $y'=ay+f$, les solutions sont :`, c: [R`$g+C\e^{ax}$`, R`$C\,g$`, R`$g+C$`, R`$C\e^{ax}$`], r: 0, e: R`Solution particulière + solutions de $y'=ay$.`, ref: "yayf" },
    { q: R`Méthode d'Euler pour $y'=y$, $y(0)=1$, $h=0{,}1$ : $y_1=$`, c: ["$1$", "$1{,}1$", "$1{,}105$", "$\\e^{0{,}1}$"], r: 1, e: R`$y_1=y_0+h\,y_0=1+0{,}1=1{,}1$.`, ref: "euler" },
    { q: R`La démonstration de « les solutions de $y'=ay$ sont $C\e^{ax}$ » consiste à :`, c: ["dériver $y\\e^{-ax}$ et trouver $0$", "intégrer par parties", "utiliser le TVI", "utiliser la récurrence"], r: 0, e: R`$z=y\e^{-ax}$ a une dérivée nulle, donc est constante.`, ref: "yay" },
    { q: R`Une primitive de $\frac{1}{\sqrt x}$ sur $]0;+\infty[$ est :`, c: [R`$\frac{1}{2\sqrt x}$`, R`$2\sqrt x$`, R`$\sqrt x$`, R`$\ln\sqrt x$`], r: 1, e: R`$(2\sqrt x)'=2\times\frac1{2\sqrt x}$.`, ref: "usuelles" }
  ],
  cartes: [
    [R`Définition d'une primitive $F$ de $f$`, R`$F$ dérivable sur $I$ et $F'=f$.`],
    [R`Toutes les primitives de $f$ si $F$ en est une`, R`$F+C$, $C$ réel (sur un intervalle).`],
    [R`Primitive de $x^n$ ($n\neq-1$)`, R`$\frac{x^{n+1}}{n+1}$`],
    [R`Primitive de $\frac1x$ sur $]0;+\infty[$`, R`$\ln x$`],
    [R`Primitive de $\e^{ax+b}$`, R`$\frac1a\e^{ax+b}$`],
    [R`Primitive de $\cos$ ; de $\sin$`, R`$\sin$ ; $-\cos$`],
    [R`Primitive de $u'\e^u$ ; de $\frac{u'}u$`, R`$\e^u$ ; $\ln u$ ($u>0$)`],
    [R`Primitive de $u'u^n$`, R`$\frac{u^{n+1}}{n+1}$`],
    [R`Solutions de $y'=ay$`, R`$C\e^{ax}$`],
    [R`Solutions de $y'=ay+b$ ($a\neq0$)`, R`$C\e^{ax}-\frac ba$`],
    [R`Solutions de $y'=ay+f$ si $g$ est solution`, R`$g+C\e^{ax}$`],
    [R`Méthode d'Euler`, R`$y_{n+1}=y_n+h\,y'(x_n)$`]
  ]
};

/* Animation : la solution suit le champ de tangentes, Euler approche */
ANIMS.champ = {
  titre: "La solution suit les petites tangentes",
  vb: [360, 250],
  etapes: [
    { d: 4, l: R`$y'=-0{,}5y+1$. En chaque point $(x;y)$, l'équation donne la pente que doit avoir une solution qui passe par là : $-0{,}5y+1$. On dessine ces petites tangentes.` },
    { d: 5, l: R`Partons de $y(0)=0$ : la courbe suit les tangentes, monte de moins en moins vite. C'est $y=2-2\e^{-0{,}5x}$.` },
    { d: 4, l: R`Partons de $y(0)=4$ : la solution $y=2+2\e^{-0{,}5x}$ descend vers $2$.` },
    { d: 3.5, l: R`Sur la droite $y=2$, toutes les tangentes sont horizontales : la constante $2=-\frac ba$ est solution. Toutes les autres s'en approchent : $y=2+C\e^{-0{,}5x}$.` },
    { d: 6, l: R`Méthode d'Euler, pas $h=0{,}5$ : on avance de $0{,}5$ en suivant la tangente du point où l'on est. La ligne brisée colle à la vraie courbe : en $x=4$, $1{,}80$ contre $1{,}73$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (y) { return -0.5 * y + 1; };
    S.rep(0, 8, -0.5, 4.5, { px: 1, py: 1 });
    var portee = k === 0 ? E(t) : 1;
    for (var i = 0; i <= 16; i++) for (var j = 0; j <= 10; j++) {
      var x = i * 0.5, y = -0.5 + j * 0.5, s = f(y), L = 0.18, dx = L / Math.sqrt(1 + s * s * 0.64);
      if (x / 8 > portee) continue;
      S.seg(x - dx, y - s * dx, x + dx, y + s * dx, "a-champ");
    }
    function sol(C, fin, cls) { return S.courbe(function (x) { return 2 + C * Math.exp(-0.5 * x); }, 0, fin, cls, 160, { "stroke-width": 2.8 }); }
    if (k >= 1) { var f1 = k === 1 ? 8 * E(t) : 8; if (f1 > 0) sol(-2, f1, "g-c"); var yy = 2 - 2 * Math.exp(-0.5 * f1); if (k === 1) { S.pt(f1, yy, "g-pt", 5); var s1 = f(yy); S.seg(f1 - 0.6, yy - 0.6 * s1, f1 + 0.6, yy + 0.6 * s1, "g-c2", { "stroke-width": 2 }); } }
    if (k >= 2) { var f2 = k === 2 ? 8 * E(t) : 8; if (f2 > 0) sol(2, f2, "g-c"); if (k === 2) S.pt(f2, 2 + 2 * Math.exp(-0.5 * f2), "g-pt", 5); }
    if (k >= 3) S.seg(0, 2, 8 * (k === 3 ? E(t) : 1), 2, "g-c2", { "stroke-width": 2.6 });
    if (k >= 3) S.txt(7.9, 2.15, "y = 2", "r", "end");
    if (k === 4) {
      var n = Math.floor(E(t) * 8.999), pts = [[0, 0]], y = 0;
      for (var m = 0; m < n; m++) { y = y + 0.5 * f(y); pts.push([(m + 1) * 0.5, y]); }
      S.poly(pts, "g-c3", false, { "stroke-width": 2.4 });
      pts.forEach(function (q) { S.pt(q[0], q[1], "g-pt2", 3.4); });
      if (n >= 8) S.txt(4.1, 1.45, "Euler : 1,80", "r");
    }
  }
};

/* Animation : la famille des primitives, et celle qui passe par un point */
ANIMS.primitives = {
  titre: R`Toutes les primitives de $f(x)=2x$`,
  vb: [360, 250],
  etapes: [
    { d: 5, l: R`$F(x)=x^2$ est une primitive de $f(x)=2x$ : en chaque point d'abscisse $a$, la tangente à la courbe de $F$ a pour pente $F'(a)=f(a)=2a$.` },
    { d: 5.5, l: R`$x^2+C$ a la même dérivée $2x$, pour tout réel $C$ : on obtient toutes les primitives en translatant la courbe verticalement. À la même abscisse, toutes les tangentes sont parallèles (ici en $x=1$, pente $2$).` },
    { d: 4.5, l: R`Condition $F(1)=5$ : $1+C=5$, donc $C=4$. Une seule courbe passe par le point $(1;5)$ : $F(x)=x^2+4$.` },
    { d: 5, l: R`Entre deux primitives, l'écart vertical est le même partout : $(x^2+4)-x^2=4$. C'est le théorème « deux primitives d'une même fonction diffèrent d'une constante ».` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, nf = ANIM.nf;
    S.rep(-2.5, 2.5, -4, 10, { px: 1, py: 2 });
    function F(C) { return function (x) { return x * x + C; }; }
    function tangente(a, C, cls, at) { var y = a * a + C; S.seg(a - 0.55, y - 1.1 * a, a + 0.55, y + 1.1 * a, cls, at); }
    if (k === 0) {
      S.courbe(F(0), -2.5, 2.5, "g-c");
      var a = ANIM.l(-2, 2, E(t));
      tangente(a, 0, "g-c2", { "stroke-width": 2.4 });
      S.pt(a, a * a, "g-pt2", 4.5);
      S.px.txt(44, 24, "a = " + nf(a, 1) + "   pente = 2a = " + nf(2 * a, 1), "r", "start");
      return;
    }
    if (k === 1) {
      for (var C = -3; C <= 5; C++) {
        var o = C === 0 ? 1 : E(p(t, 0.08 * (C + 3), 0.08 * (C + 3) + 0.3));
        if (o < 0.01) continue;
        S.courbe(F(C), -2.5, 2.5, "g-c", 120, { opacity: C === 0 ? 1 : 0.5 * o });
        tangente(1, C, "g-c3", { opacity: o, "stroke-width": 2 });
      }
      S.px.txt(44, 24, "F(x) = x² + C", "b", "start");
      return;
    }
    if (k === 2) {
      var o2 = E(p(t, 0.2, 0.7));
      for (var C2 = -3; C2 <= 5; C2++) S.courbe(F(C2), -2.5, 2.5, "g-c", 120, { opacity: C2 === 4 ? 0.5 + 0.5 * o2 : 0.5 - 0.38 * o2, "stroke-width": C2 === 4 ? 2.2 + 1.2 * o2 : 2.2 });
      S.pt(1, 5, "g-pt2", 6, { opacity: E(p(t, 0, 0.25)) });
      S.txt(1.12, 4.3, "(1 ; 5)", "r", "start", { opacity: E(p(t, 0, 0.25)) });
      S.txt(-1.3, 9.2, "F(x) = x² + 4", "b", "start", { opacity: o2 });
      return;
    }
    S.courbe(F(0), -2.5, 2.5, "g-c", 120, { opacity: 0.6 });
    S.courbe(F(4), -2.5, 2.5, "g-c", 120, { "stroke-width": 3 });
    [-1.6, 0, 1.6].forEach(function (x, i) {
      var f = E(p(t, 0.15 * i, 0.15 * i + 0.4));
      if (f < 0.01) return;
      S.fleche(x, x * x, x, x * x + 4 * f, "g-c2", { "stroke-width": 2.2 });
      if (f > 0.9) S.txt(x + 0.08, x * x + 2.2, "4", "r", "start");
    });
    S.txt(-1.3, 8.6, "x² + 4", "b", "start");
    S.txt(1.95, 1.6, "x²", "b", "start", { opacity: 0.8 });
  }
};
