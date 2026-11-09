/* ---------- Chapitre 4 : dérivation, convexité, continuité ---------- */
var CH4 = {
  id: "ch4", num: 4, statut: "ok", partie: "Analyse", titre: "Dérivation, convexité, continuité", court: "Dérivation et continuité",
  sous: "Dériver une composée, lire la courbure, prouver qu'une équation a une solution.",
  resume: "Dérivée de $v\\circ u$, dérivée seconde, convexité, continuité, théorème des valeurs intermédiaires, dichotomie.",
  essentiel: [
    R`Dérivée d'une composée : $(v\circ u)'=(v'\circ u)\times u'$. Exemples : $\left(\e^{u}\right)'=u'\e^{u}$, $\left(\sqrt u\right)'=\frac{u'}{2\sqrt u}$, $\left(u^n\right)'=nu'u^{n-1}$.`,
    R`$f$ est <b>convexe</b> si sa courbe est sous ses cordes ; pour $f$ deux fois dérivable, cela équivaut à : $f''\geq0$, $f'$ croissante, courbe <b>au-dessus de ses tangentes</b>.`,
    R`Un <b>point d'inflexion</b> est un point où la courbe traverse sa tangente : $f''$ s'y annule <b>en changeant de signe</b>.`,
    R`Toute fonction dérivable est continue. Si $f$ est continue et $u_n\to\ell$, alors $f(u_n)\to f(\ell)$.`,
    R`<b>TVI</b> : si $f$ est continue sur $[a;b]$, elle prend toute valeur $k$ entre $f(a)$ et $f(b)$. Si en plus elle est strictement monotone, la solution de $f(x)=k$ est <b>unique</b> ; on l'encadre par dichotomie.`
  ],
  attendus: [
    R`Calculer la dérivée d'une fonction donnée par une formule simple mettant en jeu opérations algébriques et composition.`,
    R`Calculer la fonction dérivée, déterminer les limites et étudier les variations d'une fonction construite à partir des fonctions de référence.`,
    R`Démontrer des inégalités en utilisant la convexité ; lire sur un graphique de $f$, $f'$ ou $f''$ les intervalles de convexité et les points d'inflexion ; esquisser une courbe à partir de tableaux de variations de $f$, $f'$ ou $f''$.`,
    R`Étudier les solutions d'une équation $f(x)=k$ : existence, unicité, encadrement.`,
    R`Pour une fonction continue $f$ d'un intervalle dans lui-même, étudier une suite $u_{n+1}=f(u_n)$.`,
    R`Démonstration exigible : si $f''$ est positive, la courbe de $f$ est au-dessus de ses tangentes. Algorithmes : dichotomie ; méthode de Newton, de la sécante.`,
    R`La justification de la continuité ou de la dérivabilité sur un intervalle n'est pas un objectif du programme.`
  ],
  premiere: R`
<div class="tab-wrap"><table><tr><th>$f(x)$</th><th>$f'(x)$</th><th>Validité</th></tr>
<tr><td>$x^n$ ($n\in\Z$)</td><td>$nx^{n-1}$</td><td>$\R$ (ou $\R^*$ si $n<0$)</td></tr>
<tr><td>$\sqrt x$</td><td>$\frac1{2\sqrt x}$</td><td>$]0;+\infty[$</td></tr>
<tr><td>$\e^x$</td><td>$\e^x$</td><td>$\R$</td></tr>
<tr><td>$\cos x$ ; $\sin x$</td><td>$-\sin x$ ; $\cos x$</td><td>$\R$</td></tr></table></div>
<p>$(u+v)'=u'+v'$ ; $(ku)'=ku'$ ; $(uv)'=u'v+uv'$ ; $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$ ; $\left(\frac1v\right)'=-\frac{v'}{v^2}$ ; $f(ax+b)$ a pour dérivée $af'(ax+b)$.</p>
<p>Tangente en $a$ : $y=f'(a)(x-a)+f(a)$. Signe de $f'$ ⟹ variations de $f$.</p>`,
  cours: [
    { id: "composee", titre: "Dérivée d'une fonction composée", html: R`
[def|Composée]La composée de $u$ suivie de $v$ est la fonction $v\circ u:x\mapsto v(u(x))$ (on applique $u$, puis $v$). Exemple : $x\mapsto\e^{-x^2}$ est $v\circ u$ avec $u(x)=-x^2$ et $v=\exp$.[/]
[thm|Dérivée d'une composée]Si $u$ est dérivable sur $I$ et $v$ dérivable sur un intervalle contenant $u(I)$, alors $v\circ u$ est dérivable sur $I$ et
$$(v\circ u)'=(v'\circ u)\times u',\quad\text{soit}\quad\left(v(u(x))\right)'=v'(u(x))\times u'(x).$$[/]
<div class="tab-wrap"><table><tr><th>Fonction</th><th>Dérivée</th><th>Condition</th></tr>
<tr><td>$\e^{u}$</td><td>$u'\e^{u}$</td><td></td></tr>
<tr><td>$u^n$ ($n\geq1$)</td><td>$nu'u^{n-1}$</td><td></td></tr>
<tr><td>$\sqrt u$</td><td>$\frac{u'}{2\sqrt u}$</td><td>$u>0$</td></tr>
<tr><td>$\frac1u$</td><td>$-\frac{u'}{u^2}$</td><td>$u\neq0$</td></tr></table></div>
[ex|Quatre calculs]
<ul><li>$f(x)=(3x+1)^5$ : $f'(x)=5\times3\times(3x+1)^4=15(3x+1)^4$.</li>
<li>$g(x)=\sqrt{x^2+1}$ : $g'(x)=\frac{2x}{2\sqrt{x^2+1}}=\frac{x}{\sqrt{x^2+1}}$.</li>
<li>$h(x)=\e^{-x^2}$ : $h'(x)=-2x\,\e^{-x^2}$.</li>
<li>$k(x)=\e^{2x}(x-1)^3$ : produit, puis composées : $k'(x)=2\e^{2x}(x-1)^3+\e^{2x}\times3(x-1)^2=\e^{2x}(x-1)^2(2x+1)$.</li></ul>
Chaque formule a été contrôlée numériquement (taux d'accroissement).[/]
[meth|Repérer la structure]Avant de dériver, demande-toi quelle est la <b>dernière opération</b> : une somme, un produit, un quotient ou une composée ? Puis dérive de l'extérieur vers l'intérieur.[/]` },
    { id: "seconde", titre: "Dérivée seconde", html: R`
[def|Dérivée seconde]Si $f'$ est elle-même dérivable, sa dérivée est la <b>dérivée seconde</b> de $f$, notée $f''$.[/]
[ex|Calcul]$f(x)=x\e^x$ : $f'(x)=(x+1)\e^x$ ; $f''(x)=\e^x+(x+1)\e^x=(x+2)\e^x$.[/]
<p>Interprétation en physique : si $x(t)$ est une position, $x'(t)$ est la vitesse et $x''(t)$ l'accélération. En géométrie, $f''$ mesure comment la pente varie : c'est la <b>courbure</b>.</p>` },
    { id: "convexite", titre: "Fonctions convexes, concaves", html: R`
[def|Convexité]Une fonction $f$ est <b>convexe</b> sur un intervalle $I$ si, pour tous points $A$ et $B$ de sa courbe d'abscisses dans $I$, la courbe entre $A$ et $B$ est <b>en dessous de la corde</b> $[AB]$. Elle est <b>concave</b> si la courbe est au-dessus de ses cordes.[/]
[thm|Caractérisations (admises)]Pour $f$ deux fois dérivable sur $I$, il y a équivalence entre :
<ul><li>$f$ est convexe sur $I$ ;</li><li>la courbe de $f$ est au-dessus de chacune de ses tangentes ;</li><li>$f'$ est croissante sur $I$ ;</li><li>$f''\geq0$ sur $I$.</li></ul>
(Et concave ⟺ $f''\leq0$ ⟺ $f'$ décroissante ⟺ courbe en dessous des tangentes.)[/]
<p>Le sens « $f''\geq0$ ⟹ courbe au-dessus de ses tangentes » est une <b>démonstration exigible</b>.</p>
<div data-w="convexe"></div>
[def|Point d'inflexion]Un point de la courbe où la courbe <b>traverse</b> sa tangente. Si $f$ est deux fois dérivable, c'est un point où $f''$ s'annule <b>en changeant de signe</b> (la convexité change).[/]
[piege|$f''(a)=0$ ne suffit pas]$f(x)=x^4$ : $f''(x)=12x^2$ s'annule en $0$ sans changer de signe. $f$ est convexe sur $\R$ ; pas de point d'inflexion en $0$.[/]
[ex|Références]$x\mapsto x^2$ et $\exp$ sont convexes sur $\R$ ; $\sqrt{\ }$ est concave sur $[0;+\infty[$ ($f''(x)=-\frac1{4x\sqrt x}<0$) ; $x\mapsto x^3$ est concave sur $]-\infty;0]$, convexe sur $[0;+\infty[$, avec un point d'inflexion en $O$.[/]
[meth|Démontrer une inégalité par convexité]$\exp$ est convexe, donc sa courbe est au-dessus de sa tangente en $0$, d'équation $y=x+1$ : pour tout réel $x$, $\e^x\geq x+1$.<br>$\sqrt{\ }$ est concave, donc sous sa tangente en $1$, $y=\frac12x+\frac12$ : $\sqrt x\leq\frac{x+1}2$ pour tout $x\geq0$ (égalité pour $x=1$ ; pour $x=9$, $3\leq5$).[/]` },
    { id: "continuite", titre: "Continuité", html: R`
[def|Continuité]$f$ est <b>continue en $a$</b> si $\lim_{x\to a}f(x)=f(a)$. Elle est continue sur un intervalle si elle l'est en chaque point. Graphiquement : la courbe se trace « sans lever le crayon ».[/]
[prop|Fonctions continues]Les fonctions de référence (polynômes, $\sqrt{\ }$, $\exp$, $\cos$, $\sin$, quotients sur leur ensemble de définition…) et leurs sommes, produits, composées sont continues sur les intervalles où elles sont définies. Le programme précise que la justification de la continuité n'est pas un objectif : une phrase suffit.[/]
[thm|Dérivable ⟹ continue]Toute fonction dérivable sur un intervalle est continue sur cet intervalle. La réciproque est fausse : $x\mapsto|x|$ est continue en $0$ mais pas dérivable en $0$ (deux demi-tangentes de pentes $-1$ et $1$).[/]
[ex|Une fonction discontinue]La fonction partie entière $E$ (plus grand entier inférieur ou égal à $x$) « saute » en chaque entier : $E(x)=0$ pour $x\in[0;1[$ et $E(1)=1$. Elle n'est pas continue en $1$.[/]
[thm|Image d'une suite convergente]Si $(u_n)$ converge vers $\ell$ et si $f$ est continue en $\ell$, alors $(f(u_n))$ converge vers $f(\ell)$. En particulier, si $u_{n+1}=f(u_n)$ et $u_n\to\ell$, alors $f(\ell)=\ell$ (chapitre 2).[/]
<p><b>Convention</b> : dans un tableau de variations, une flèche indique que la fonction est continue et strictement monotone sur l'intervalle.</p>` },
    { id: "tvi", titre: "Théorème des valeurs intermédiaires", html: R`
[thm|Théorème des valeurs intermédiaires (TVI)]Si $f$ est <b>continue</b> sur $[a;b]$, alors pour tout réel $k$ compris entre $f(a)$ et $f(b)$, l'équation $f(x)=k$ admet <b>au moins une</b> solution dans $[a;b]$.[/]
[thm|Corollaire : cas strictement monotone]Si $f$ est <b>continue et strictement monotone</b> sur $[a;b]$, alors pour tout $k$ compris entre $f(a)$ et $f(b)$, l'équation $f(x)=k$ admet <b>une unique</b> solution dans $[a;b]$.<br>Cela s'étend aux intervalles ouverts ou infinis en remplaçant $f(a)$ et $f(b)$ par les limites.[/]
[ex|Rédaction type]Montrons que $x^3+x-1=0$ a une unique solution $\alpha$ sur $[0;1]$. Soit $f(x)=x^3+x-1$.
<ul><li>$f$ est continue sur $[0;1]$ (polynôme).</li><li>$f'(x)=3x^2+1>0$ : $f$ est strictement croissante sur $[0;1]$.</li><li>$f(0)=-1<0$ et $f(1)=1>0$ : $0$ est compris entre $f(0)$ et $f(1)$.</li></ul>
D'après le corollaire du TVI, l'équation $f(x)=0$ admet une unique solution $\alpha\in[0;1]$. Par dichotomie, $0{,}682<\alpha<0{,}683$ ($\alpha\approx0{,}6823$).[/]
[piege|Les deux hypothèses]Sans continuité, une fonction peut « sauter » par-dessus $k$. Sans stricte monotonie, il peut y avoir plusieurs solutions (le TVI garantit seulement l'existence).[/]
<div data-w="dicho"></div>` },
    { id: "dichotomie", titre: "Encadrer une solution : dichotomie et Newton", html: R`
<p>Le TVI dit qu'une solution existe, pas combien elle vaut. La <b>dichotomie</b> la piège dans un intervalle qu'on coupe en deux à chaque étape :</p>
<ol><li>On part de $[a;b]$ avec $f(a)$ et $f(b)$ de signes contraires.</li><li>On calcule $m=\frac{a+b}2$. Si $f(a)$ et $f(m)$ sont de signes contraires, la solution est dans $[a;m]$ : $b\leftarrow m$. Sinon, $a\leftarrow m$.</li><li>On recommence tant que $b-a$ dépasse la précision voulue.</li></ol>
<p>Après $n$ étapes, l'amplitude est $\frac{b-a}{2^n}$ : $10$ étapes divisent la largeur par $1024$, soit environ $10^{-3}$.</p>
<p>La <b>méthode de Newton</b> (aussi citée par le programme) remplace la courbe par sa tangente : $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$. Elle est beaucoup plus rapide quand elle converge (voir l'onglet Python).</p>` }
  ],
  pieges: [
    { t: "Oublier le $u'$", h: R`$\left(\e^{3x^2}\right)'=6x\,\e^{3x^2}$, pas $\e^{3x^2}$. La dérivée d'une composée contient toujours la dérivée de l'intérieur.` },
    { t: "Confondre convexe et croissante", h: R`$x\mapsto\e^{-x}$ est convexe et décroissante. La convexité concerne la courbure ($f''$), pas le sens de variation ($f'$).` },
    { t: "Lire la convexité sur le mauvais graphique", h: R`Sur la courbe de $f'$ : $f$ convexe là où $f'$ <b>croît</b>. Sur la courbe de $f''$ : là où $f''$ est <b>positive</b>.` },
    { t: "TVI sans continuité ou sans « strictement »", h: R`Au bac, chaque hypothèse est un point : « continue », « strictement croissante », « $k$ compris entre $f(a)$ et $f(b)$ ».` },
    { t: "Encadrement mal donné", h: R`« Valeur approchée à $10^{-2}$ près » : donne un encadrement d'amplitude $0{,}01$ (par exemple $0{,}34<\alpha<0{,}35$), en vérifiant les signes aux bornes.` }
  ],
  demos: [
    { bo: true, t: "Si $f''\\geq0$, la courbe est au-dessus de ses tangentes", h: R`
<p>Soit $f$ deux fois dérivable sur $I$ avec $f''\geq0$, et $a\in I$. La tangente en $a$ a pour équation $y=f'(a)(x-a)+f(a)$. On pose, pour $x\in I$ :
$$g(x)=f(x)-\left[f'(a)(x-a)+f(a)\right].$$</p>
<p>$g$ est dérivable et $g'(x)=f'(x)-f'(a)$.</p>
<p>Comme $f''\geq0$, $f'$ est croissante sur $I$. Donc : si $x\leq a$, $f'(x)\leq f'(a)$ et $g'(x)\leq0$ ; si $x\geq a$, $g'(x)\geq0$.</p>
<p>$g$ est donc décroissante puis croissante : elle admet un minimum en $a$, qui vaut $g(a)=f(a)-f(a)=0$. Ainsi $g(x)\geq0$ pour tout $x\in I$ : la courbe est au-dessus de la tangente en $a$. Ceci pour tout $a\in I$.</p>
<p class="stylo">La structure « étudier la différence $g$, dériver, trouver son minimum » est à connaître : elle sert pour toutes les inégalités.</p>` },
    { bo: false, t: "Une dérivée de composée sur un exemple : $(\\e^{u})'=u'\\e^{u}$", h: R`
<p>Pour $h\neq0$ : $\frac{\e^{u(x+h)}-\e^{u(x)}}{h}=\frac{\e^{u(x+h)}-\e^{u(x)}}{u(x+h)-u(x)}\times\frac{u(x+h)-u(x)}{h}$ (quand $u(x+h)\neq u(x)$). Le second facteur tend vers $u'(x)$ ; le premier est un taux d'accroissement de $\exp$ en $u(x)$, il tend vers $\e^{u(x)}$. D'où $(\e^u)'=u'\e^u$. <span class="tag hp">pour comprendre</span> : la formule générale est admise.</p>` },
    { bo: false, t: "TVI par dichotomie", h: R`
<p><span class="tag hp">Pour aller plus loin</span> (approfondissement du programme). On construit deux suites $(a_n)$ croissante et $(b_n)$ décroissante par dichotomie, avec $f(a_n)\leq k\leq f(b_n)$ et $b_n-a_n=\frac{b-a}{2^n}$. Elles convergent vers une même limite $c$ (monotones bornées, et leur écart tend vers $0$). Par continuité, $f(a_n)\to f(c)$ et $f(b_n)\to f(c)$ ; en passant à la limite dans $f(a_n)\leq k\leq f(b_n)$ : $f(c)\leq k\leq f(c)$, donc $f(c)=k$.</p>` }
  ],
  algos: [
    { bo: true, t: "Méthode de dichotomie", code: `def f(x):
    return x**3 + x - 1

def dichotomie(a, b, e):
    while b - a > e:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return a, b

print(dichotomie(0, 1, 0.001))`, sortie: `(0.681640625, 0.6826171875)`,
      apres: R`<p>La condition <code>f(a) * f(m) &lt;= 0</code> teste « $f(a)$ et $f(m)$ de signes contraires ». Il a fallu $10$ étapes. Conclusion : $0{,}681<\alpha<0{,}683$.</p>` },
    { bo: true, t: "Méthode de Newton", avant: R`<p>On suit la tangente : $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$, ici avec $f'(x)=3x^2+1$.</p>`, code: `x = 1.0
for k in range(5):
    x = x - (x**3 + x - 1) / (3 * x**2 + 1)
    print(k + 1, x)`, sortie: `1 0.75
2 0.686046511627907
3 0.6823395825973142
4 0.6823278039465127
5 0.6823278038280194`,
      apres: R`<p>En $5$ étapes, environ $15$ chiffres exacts, contre $3$ pour $10$ étapes de dichotomie. Mais Newton peut échouer si la dérivée s'annule ou si l'on part trop loin ; la dichotomie, elle, marche toujours (fonction continue, signes contraires).</p>` },
    { bo: false, t: "Balayage avec un pas", avant: R`<p>Méthode de Première, utile à la calculatrice : on avance d'un pas jusqu'au changement de signe.</p>`, code: `def balayage(a, pas):
    x = a
    while (x + pas)**3 + (x + pas) - 1 < 0:
        x = x + pas
    return x, x + pas

print(balayage(0, 0.01))`, sortie: `(0.6800000000000004, 0.6900000000000004)`,
      apres: R`<p>Les décimales parasites viennent de l'arithmétique des ordinateurs ($0{,}01$ n'est pas exactement représentable) : on lit $0{,}68<\alpha<0{,}69$.</p>` }
  ],
  methodes: [
    { t: "Comment dériver une fonction compliquée ?", h: R`
<ol><li>Repère la dernière opération (produit, quotient, composée).</li><li>Écris les fonctions intermédiaires $u$, $v$ et leurs dérivées.</li><li>Applique la formule, puis <b>factorise</b> (souvent par l'exponentielle) pour étudier le signe.</li></ol>` },
    { t: "Comment étudier la convexité ?", h: R`
<ol><li>Calcule $f''$ et factorise-la.</li><li>Étudie son signe : $f''\geq0$ ⟹ convexe ; $f''\leq0$ ⟹ concave.</li><li>Points d'inflexion : là où $f''$ s'annule <b>en changeant de signe</b>.</li></ol>
[ex|Au bac]$g(x)=x\e^x$ : $g''(x)=(x+2)\e^x$ ; convexe sur $[-2;+\infty[$, concave sur $]-\infty;-2]$, inflexion au point d'abscisse $-2$ (affirmation 2, vraie, du sujet de Polynésie du 16 juin 2026).[/]` },
    { t: "Comment démontrer qu'une équation $f(x)=k$ a une unique solution ?", h: R`
<p>Trois phrases, trois hypothèses : « $f$ est continue sur $I$ » ; « $f$ est strictement croissante (ou décroissante) sur $I$ » (tableau de variations) ; « $k$ est compris entre $f(a)$ et $f(b)$ (ou entre les limites) ». Puis : « D'après le corollaire du théorème des valeurs intermédiaires, l'équation admet une unique solution $\alpha$ dans $I$. » Encadre $\alpha$ à la calculatrice (tableau de valeurs) ou par dichotomie.</p>` },
    { t: "Comment démontrer une inégalité $f(x)\\geq g(x)$ ?", h: R`
<ul><li>Si $g$ est une tangente de $f$ : par convexité (courbe au-dessus de ses tangentes).</li><li>Sinon : étudie $h=f-g$, cherche son minimum avec $h'$, et montre qu'il est positif.</li></ul>` }
  ],
  exos: [
    { niv: 1, t: "Dérivées de composées", enonce: R`<p>Calculer la dérivée de chaque fonction.</p><ol><li>$f(x)=(2x^2-1)^4$</li><li>$g(x)=\sqrt{\e^x+1}$</li><li>$h(x)=\frac{1}{x^2+1}$</li><li>$k(x)=x\,\e^{-2x}$</li></ol>`,
      corrige: R`<ol><li>$f'(x)=4\times4x\times(2x^2-1)^3=16x(2x^2-1)^3$.</li><li>$g'(x)=\frac{\e^x}{2\sqrt{\e^x+1}}$.</li><li>$h'(x)=-\frac{2x}{(x^2+1)^2}$.</li><li>$k'(x)=\e^{-2x}+x\times(-2)\e^{-2x}=(1-2x)\e^{-2x}$.</li></ol>` },
    { niv: 1, t: "Unique solution", enonce: R`<p>Soit $f(x)=x^3-3x+1$.</p><ol><li>Étudier les variations de $f$ sur $[-1;1]$.</li><li>Montrer que l'équation $f(x)=0$ a une unique solution $\alpha$ dans $[0;1]$.</li><li>Donner un encadrement de $\alpha$ d'amplitude $10^{-2}$.</li></ol>`,
      corrige: R`<ol><li>$f'(x)=3x^2-3=3(x-1)(x+1)\leq0$ sur $[-1;1]$ (nulle seulement en $\pm1$) : $f$ est strictement décroissante sur $[-1;1]$.</li><li>$f$ est continue (polynôme), strictement décroissante sur $[0;1]$, $f(0)=1>0$ et $f(1)=-1<0$. Par le corollaire du TVI, $f(x)=0$ a une unique solution $\alpha\in[0;1]$.</li><li>$f(0{,}34)\approx0{,}0193>0$ et $f(0{,}35)\approx-0{,}0071<0$, donc $0{,}34<\alpha<0{,}35$.</li></ol>` },
    { niv: 2, t: "Convexité et inégalités", enonce: R`<ol><li>Montrer que $f(x)=\e^x$ est convexe sur $\R$, puis que pour tout réel $x$ : $\e^x\geq x+1$.</li><li>En déduire que pour tout entier $n\geq1$ : $\left(1+\frac1n\right)^n\leq\e$.</li><li>Étudier la convexité de $g(x)=x^3-3x^2+2$ et donner son point d'inflexion.</li></ol>`,
      corrige: R`<ol><li>$f''(x)=\e^x>0$ : convexe ; la tangente en $0$ est $y=x+1$ ($f(0)=f'(0)=1$), donc $\e^x\geq x+1$.</li><li>Avec $x=\frac1n$ : $1+\frac1n\leq\e^{\frac1n}$. Les deux membres sont positifs ; la fonction $t\mapsto t^n$ est croissante sur $[0;+\infty[$, donc $\left(1+\frac1n\right)^n\leq\left(\e^{\frac1n}\right)^n=\e$.</li><li>$g'(x)=3x^2-6x$, $g''(x)=6x-6$ : concave sur $]-\infty;1]$, convexe sur $[1;+\infty[$ ; $g''$ s'annule en changeant de signe en $1$ : point d'inflexion $(1;g(1))=(1;0)$.</li></ol>` },
    { niv: 2, t: "Lecture graphique", enonce: R`<p>On donne le tableau de signes de $f''$ sur $[-3;4]$ : $f''(x)<0$ sur $[-3;-1[$, $f''(-1)=0$, $f''(x)>0$ sur $]-1;2[$, $f''(2)=0$, $f''(x)>0$ sur $]2;4]$.</p><ol><li>Sur quels intervalles $f$ est-elle convexe ? concave ?</li><li>Combien la courbe a-t-elle de points d'inflexion ?</li><li>Comment varie $f'$ ?</li></ol>`,
      corrige: R`<ol><li>Concave sur $[-3;-1]$, convexe sur $[-1;4]$.</li><li>Un seul, d'abscisse $-1$ : en $2$, $f''$ s'annule sans changer de signe.</li><li>$f'$ est décroissante sur $[-3;-1]$ et croissante sur $[-1;4]$ (son signe ne se lit pas ici).</li></ol>` },
    { niv: 3, t: "Étude, TVI et convexité (type bac)", enonce: R`<p>Soit $f$ définie sur $[0;+\infty[$ par $f(x)=\e^x-x-2$.</p><ol><li>Étudier les variations de $f$ et sa limite en $+\infty$.</li><li>Montrer que l'équation $f(x)=0$ admet une unique solution $\alpha$ sur $[0;+\infty[$, et que $1<\alpha<2$.</li><li>Recopier et compléter la fonction pour obtenir un encadrement de $\alpha$ d'amplitude $10^{-2}$, et donner cet encadrement.</li><li>Montrer que $f$ est convexe, puis que pour tout $x\geq0$ : $f(x)\geq(\e-1)x-2$.</li></ol>
[py]
from math import exp
def encadre(a, b):
    while b - a > 0.01:
        m = (a + b) / 2
        if ...:
            b = m
        else:
            a = m
    return a, b
[/py]`,
      corrige: R`<ol><li>$f'(x)=\e^x-1\geq0$ sur $[0;+\infty[$, nulle seulement en $0$ : $f$ est strictement croissante, $f(0)=-1$. En $+\infty$ : $f(x)=\e^x\left(1-\frac{x}{\e^x}-\frac2{\e^x}\right)\to+\infty$.</li>
<li>$f$ est continue et strictement croissante sur $[0;+\infty[$, $f(0)=-1<0$ et $\lim_{+\infty}f=+\infty$ : par le corollaire du TVI, $f(x)=0$ a une unique solution $\alpha$. $f(1)=\e-3\approx-0{,}28<0$ et $f(2)=\e^2-4\approx3{,}39>0$, donc $1<\alpha<2$.</li>
<li>Condition : <code>(exp(a) - a - 2) * (exp(m) - m - 2) &lt;= 0</code>. Appel <code>encadre(1, 2)</code> : $(1{,}140625\,;\,1{,}1484375)$ après $7$ étapes. On peut affiner : $f(1{,}14)\approx-0{,}013$ et $f(1{,}15)\approx0{,}008$, donc $1{,}14<\alpha<1{,}15$ ($\alpha\approx1{,}1462$).</li>
<li>$f''(x)=\e^x>0$ : $f$ est convexe, donc au-dessus de ses tangentes. Tangente en $1$ : $y=f'(1)(x-1)+f(1)=(\e-1)(x-1)+\e-3=(\e-1)x-2$. D'où $f(x)\geq(\e-1)x-2$ sur $[0;+\infty[$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole – La Réunion, 8 septembre 2026, exercice 4, partie B, question 3", url: "https://www.apmep.fr/IMG/pdf/Metropole_J_spe_8osep_2026.pdf", h: R`« Démontrer que l'équation $f(t)=0{,}5$ admet une unique solution sur $[1;3]$ », avec $f(t)=4t\e^{-\frac32t}$ décroissante sur cet intervalle. (Calcul de contrôle : $f(1)\approx0{,}89$, $f(3)\approx0{,}13$, solution $\approx1{,}765$.)` },
    { ref: "Bac 2025, Métropole, 18 juin 2025 (sujet 2), exercice 4, partie B, question 2d", url: "https://www.apmep.fr/IMG/pdf/Metropole__spe_J2_18_06_2025_DV_2.pdf", h: R`« Montrer que l'équation $v(t)=1$ admet une solution unique $\alpha$, dont on donnera une valeur approchée au dixième. »` },
    { ref: "Bac 2026, Polynésie, 16 juin 2026 (sujet 1), exercice 2, affirmation 2", url: "https://www.apmep.fr/IMG/pdf/Bac_spe_Polynesie_J1_16_06_2026_DV.pdf", h: R`Vrai/faux : « $g(x)=x\e^x$ est convexe sur $[-2;+\infty[$ ». Vrai : $g''(x)=(x+2)\e^x\geq0$ sur cet intervalle.` },
    { ref: "Bac 2026, Asie, 10 juin 2026 (sujet 2), exercice 4, affirmation 1", url: "https://www.apmep.fr/IMG/pdf/BAC_Spe_J2_Asie_juin_2026_FK.pdf", h: R`« $f(x)=\left(-\frac12x+3\right)^5$ est convexe sur $\R$ » : dérivée de composée deux fois, $f''(x)=5\left(-\frac12x+3\right)^3$, négative pour $x>6$. Affirmation fausse.` }
  ],
  retenir: R`
[thm|Composée]$(v\circ u)'=(v'\circ u)\times u'$ ; $(\e^u)'=u'\e^u$ ; $(u^n)'=nu'u^{n-1}$ ; $(\sqrt u)'=\frac{u'}{2\sqrt u}$ ; $\left(\frac1u\right)'=-\frac{u'}{u^2}$.[/]
[thm|Convexité ($f$ deux fois dérivable)]$f$ convexe ⟺ $f''\geq0$ ⟺ $f'$ croissante ⟺ courbe au-dessus de ses tangentes (et sous ses cordes).<br>Point d'inflexion : $f''$ s'annule <b>et change de signe</b> ; la courbe traverse sa tangente.[/]
<p>Inégalités à connaître : $\e^x\geq x+1$ (convexité de $\exp$, tangente en $0$) ; $\sqrt x\leq\frac{x+1}2$.</p>
[thm|Continuité]Dérivable ⟹ continue. $f$ continue en $\ell$ et $u_n\to\ell$ ⟹ $f(u_n)\to f(\ell)$.[/]
[thm|TVI et corollaire]$f$ continue sur $[a;b]$, $k$ entre $f(a)$ et $f(b)$ ⟹ $f(x)=k$ a au moins une solution.<br>Si de plus $f$ strictement monotone ⟹ solution unique.[/]
<p><b>Dichotomie</b> : amplitude divisée par $2$ à chaque étape ; $n$ étapes ⟹ $\frac{b-a}{2^n}$.</p>
<p class="stylo">Rédaction TVI : continue · strictement monotone · $k$ entre les images · conclusion.</p>`,
  qcm: [
    { q: R`La dérivée de $x\mapsto\e^{-3x^2}$ est :`, c: [R`$\e^{-3x^2}$`, R`$-6x\,\e^{-3x^2}$`, R`$-3x^2\e^{-3x^2-1}$`, R`$-6x$`], r: 1, e: R`$(\e^u)'=u'\e^u$ avec $u(x)=-3x^2$, $u'(x)=-6x$.`, ref: "composee" },
    { q: R`La dérivée de $x\mapsto\sqrt{x^2+1}$ est :`, c: [R`$\frac{1}{2\sqrt{x^2+1}}$`, R`$\frac{x}{\sqrt{x^2+1}}$`, R`$\frac{2x}{\sqrt{x^2+1}}$`, R`$2x\sqrt{x^2+1}$`], r: 1, e: R`$\frac{u'}{2\sqrt u}=\frac{2x}{2\sqrt{x^2+1}}$.`, ref: "composee" },
    { q: R`La dérivée de $x\mapsto(3x+1)^5$ est :`, c: [R`$5(3x+1)^4$`, R`$15(3x+1)^4$`, R`$3(3x+1)^5$`, R`$15(3x+1)^5$`], r: 1, e: R`$(u^n)'=nu'u^{n-1}$ : $5\times3\times(3x+1)^4$.`, ref: "composee" },
    { q: R`$f''\geq0$ sur $I$ signifie que :`, c: ["$f$ est croissante", "$f$ est positive", "$f$ est convexe : sa courbe est au-dessus de ses tangentes", "$f$ est concave"], r: 2, e: R`$f''\geq0$ ⟺ $f'$ croissante ⟺ convexe.`, ref: "convexite" },
    { q: R`Pour $f(x)=x^4$, en $x=0$ :`, c: ["il y a un point d'inflexion car $f''(0)=0$", "il n'y a pas de point d'inflexion : $f''$ ne change pas de signe", "$f$ n'est pas dérivable", "$f$ est concave"], r: 1, e: R`$f''(x)=12x^2\geq0$ : $f$ est convexe sur $\R$, pas d'inflexion.`, ref: "convexite" },
    { q: R`L'inégalité $\e^x\geq x+1$ pour tout réel $x$ découle de :`, c: ["la concavité de $\\exp$", "la convexité de $\\exp$ et sa tangente en $0$", "du TVI", "de la croissance de $\\exp$ seulement"], r: 1, e: R`Courbe convexe au-dessus de sa tangente en $0$, $y=x+1$.`, ref: "convexite" },
    { q: R`Sur la courbe de $f'$, $f$ est convexe là où :`, c: ["$f'$ est positive", "$f'$ est croissante", "$f'$ s'annule", "$f'$ est négative"], r: 1, e: R`Convexe ⟺ $f'$ croissante. Le signe de $f'$ donne les variations de $f$.`, ref: "convexite" },
    { q: R`Toute fonction dérivable est continue. La réciproque :`, c: ["est vraie", "est fausse : $|x|$ est continue en $0$ sans y être dérivable", "est vraie pour les polynômes seulement", "n'a pas de sens"], r: 1, e: R`$x\mapsto|x|$ a un « coin » en $0$.`, ref: "continuite" },
    { q: R`$f$ continue sur $[0;2]$, $f(0)=-1$, $f(2)=3$. Alors :`, c: ["$f(x)=1$ a exactement une solution dans $[0;2]$", "$f(x)=1$ a au moins une solution dans $[0;2]$", "$f(x)=4$ a une solution dans $[0;2]$", "$f$ est croissante"], r: 1, e: R`TVI : au moins une. Pour « exactement une », il faut la stricte monotonie.`, ref: "tvi" },
    { q: R`Pour obtenir l'unicité dans le TVI, il faut en plus :`, c: ["que $f$ soit positive", "que $f$ soit strictement monotone", "que $f$ soit convexe", "que $f(a)=0$"], r: 1, e: R`Corollaire : continue et strictement monotone.`, ref: "tvi" },
    { q: R`Par dichotomie sur $[0;1]$, combien d'étapes pour une amplitude inférieure à $10^{-3}$ ?`, c: ["$3$", "$10$", "$100$", "$1000$"], r: 1, e: R`$\frac1{2^{10}}=\frac1{1024}<10^{-3}$, alors que $\frac1{2^9}=\frac1{512}>10^{-3}$.`, ref: "dichotomie" },
    { q: R`$u_n\to2$ et $f(x)=x^2+1$. Alors $f(u_n)\to$`, c: ["$2$", "$4$", "$5$", "on ne peut rien dire"], r: 2, e: R`$f$ est continue en $2$, donc $f(u_n)\to f(2)=5$.`, ref: "continuite" },
    { q: R`$f(x)=x\e^x$. $f''(x)=$`, c: [R`$(x+1)\e^x$`, R`$(x+2)\e^x$`, R`$x\e^x$`, R`$2\e^x$`], r: 1, e: R`$f'(x)=(x+1)\e^x$, puis $f''(x)=\e^x+(x+1)\e^x$.`, ref: "seconde" }
  ],
  cartes: [
    [R`$(v\circ u)'=$ ?`, R`$(v'\circ u)\times u'$`],
    [R`$(\e^u)'$, $(u^n)'$, $(\sqrt u)'$`, R`$u'\e^u$ ; $nu'u^{n-1}$ ; $\frac{u'}{2\sqrt u}$`],
    [R`$f$ convexe (déf.)`, R`Courbe sous ses cordes sur l'intervalle.`],
    [R`Trois caractérisations de la convexité ($f$ deux fois dérivable)`, R`$f''\geq0$ ; $f'$ croissante ; courbe au-dessus de ses tangentes.`],
    [R`Point d'inflexion`, R`La courbe traverse sa tangente ; $f''$ s'annule en changeant de signe.`],
    [R`Inégalité de convexité de l'exponentielle`, R`$\e^x\geq x+1$ pour tout réel $x$.`],
    [R`Continuité en $a$ (déf.)`, R`$\lim_{x\to a}f(x)=f(a)$`],
    [R`Dérivable ⟹ ? ; et la réciproque ?`, R`Continue. Réciproque fausse : $|x|$ en $0$.`],
    [R`Énoncé du TVI`, R`$f$ continue sur $[a;b]$, $k$ entre $f(a)$ et $f(b)$ ⟹ $\exists\,c\in[a;b]$, $f(c)=k$.`],
    [R`Corollaire du TVI`, R`Continue et strictement monotone ⟹ solution unique.`],
    [R`Dichotomie : amplitude après $n$ étapes`, R`$\frac{b-a}{2^n}$`],
    [R`Méthode de Newton`, R`$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$`],
    [R`Image d'une suite convergente`, R`$u_n\to\ell$ et $f$ continue en $\ell$ ⟹ $f(u_n)\to f(\ell)$.`]
  ]
};
