/* ---------- Chapitre 9 : calcul intégral ---------- */
var CH9 = {
  id: "ch9", num: 9, statut: "ok", partie: "Analyse", titre: "Calcul intégral", court: "Calcul intégral",
  sous: "Mesurer une aire sous une courbe, et découvrir que c'est l'opération inverse de la dérivation.",
  resume: "Intégrale et aire, rectangles, primitives, linéarité, Chasles, valeur moyenne, intégration par parties.",
  essentiel: [
    R`Pour $f$ continue et positive sur $[a;b]$, $\int_a^bf(x)\,dx$ est l'<b>aire</b> (en unités d'aire) du domaine entre la courbe, l'axe des abscisses et les droites $x=a$, $x=b$.`,
    R`Si $F$ est une primitive de $f$ continue : $\int_a^bf(x)\,dx=F(b)-F(a)=\left[F(x)\right]_a^b$. Et $x\mapsto\int_a^xf(t)\,dt$ est la primitive de $f$ qui s'annule en $a$.`,
    R`Linéarité, relation de Chasles $\int_a^c=\int_a^b+\int_b^c$, positivité, intégration des inégalités.`,
    R`Valeur moyenne : $\mu=\frac1{b-a}\int_a^bf(x)\,dx$. Aire entre deux courbes : $\int_a^b\left(f-g\right)$ si $f\geq g$.`,
    R`Intégration par parties : $\int_a^bu(x)v'(x)\,dx=\left[u(x)v(x)\right]_a^b-\int_a^bu'(x)v(x)\,dx$.`
  ],
  attendus: [
    R`Estimer graphiquement ou encadrer une intégrale, une valeur moyenne.`,
    R`Calculer une intégrale à l'aide d'une primitive, à l'aide d'une intégration par parties.`,
    R`Majorer (minorer) une intégrale à partir d'une majoration (minoration) d'une fonction par une autre fonction.`,
    R`Calculer l'aire entre deux courbes ; étudier une suite d'intégrales, vérifiant éventuellement une relation de récurrence ; interpréter une intégrale, une valeur moyenne dans un contexte issu d'une autre discipline.`,
    R`Démonstrations exigibles : pour $f$ positive croissante, $x\mapsto\int_a^xf(t)\,dt$ est une primitive de $f$, et $\int_a^bf=F(b)-F(a)$ ; intégration par parties.`,
    R`Algorithmes : méthodes des rectangles, des milieux, des trapèzes ; méthode de Monte-Carlo ; algorithme de Brouncker pour $\ln2$.`
  ],
  premiere: R`
<ul><li>Aires usuelles : rectangle, triangle ($\frac{\text{base}\times\text{hauteur}}2$), trapèze ($\frac{(B+b)h}2$).</li>
<li>Chapitre 8 : primitives usuelles ; toutes les primitives d'une fonction diffèrent d'une constante.</li>
<li>Chapitre 2 : somme de termes, limites de suites ; chapitre 4 : dérivée d'un produit $(uv)'=u'v+uv'$.</li></ul>`,
  cours: [
    { id: "aire", titre: "L'intégrale d'une fonction positive : une aire", html: R`
<p>Dans un repère orthogonal, l'<b>unité d'aire</b> (u.a.) est l'aire du rectangle construit sur les vecteurs unités.</p>
[def|Intégrale d'une fonction continue positive]Soit $f$ continue et positive sur $[a;b]$. L'intégrale de $a$ à $b$ de $f$, notée $\int_a^bf(x)\,dx$, est l'aire du domaine délimité par la courbe de $f$, l'axe des abscisses et les droites d'équations $x=a$ et $x=b$.[/]
[ex|Aires que l'on sait déjà calculer]$\int_0^1x\,dx=\frac12$ (triangle) ; $\int_1^43\,dx=9$ (rectangle $3\times3$) ; $\int_{-1}^1\sqrt{1-x^2}\,dx=\frac\pi2$ (demi-disque de rayon $1$).[/]
<p>La variable $x$ est « muette » : $\int_a^bf(x)\,dx=\int_a^bf(t)\,dt$. Le symbole $\int$ est un S allongé, pour « somme » : le programme met en regard $\int_a^bf(x)\,dx$ et la somme $\sum f(x_i)\,\Delta x_i$ des aires de rectangles.</p>` },
    { id: "rectangles", titre: "Encadrer une aire par des rectangles", html: R`
<p>On découpe $[a;b]$ en $n$ bandes de largeur $h=\frac{b-a}n$, et on remplace chaque bande par un rectangle. Si $f$ est croissante, les rectangles « à gauche » sont sous la courbe et ceux « à droite » au-dessus : ils encadrent l'aire.</p>
<div data-anim="rectangles"></div>
[ex|$\int_0^1x^2\,dx$]Avec $n=4$ : $0{,}21875\leq I\leq0{,}46875$ ; avec $n=16$ : $0{,}3027\leq I\leq0{,}3652$ ; avec $n=100$ : $0{,}32835\leq I\leq0{,}33835$. Les deux sommes se rapprochent de $\frac13$, la valeur exacte (partie suivante).[/]
[prop|D'autres méthodes]Méthode des <b>milieux</b> : hauteur prise au milieu de chaque bande ($n=4$ donne déjà $0{,}328$). Méthode des <b>trapèzes</b> : on relie les points par des segments ($n=4$ : $0{,}344$). Toutes sont dans l'onglet Python.[/]` },
    { id: "primitive", titre: "Intégrale et primitive", html: R`
[thm|L'aire, fonction de la borne]Si $f$ est continue et positive sur $[a;b]$, la fonction $F_a:x\mapsto\int_a^xf(t)\,dt$ est dérivable sur $[a;b]$ et $F_a'=f$ : c'est la primitive de $f$ qui s'annule en $a$. (Démonstration exigible dans le cas où $f$ est croissante.)[/]
<div data-anim="aire"></div>
[thm|Calcul par une primitive]Sous les mêmes hypothèses, si $F$ est une primitive quelconque de $f$ : $$\int_a^bf(x)\,dx=F(b)-F(a),\quad\text{noté}\quad\left[F(x)\right]_a^b.$$[/]
[ex|Calculs]$\int_0^1x^2\,dx=\left[\frac{x^3}3\right]_0^1=\frac13$ ; $\int_0^1\e^x\,dx=\e-1\approx1{,}718$ ; $\int_0^\pi\sin x\,dx=\left[-\cos x\right]_0^\pi=1+1=2$ ; $\int_1^2\frac1x\,dx=\ln2$.[/]
[thm|Existence des primitives]Toute fonction continue sur un intervalle admet des primitives. (C'est le résultat admis au chapitre 8.)[/]` },
    { id: "signe", titre: "Fonction de signe quelconque ; propriétés", html: R`
[def|Cas général]Si $f$ est continue sur un intervalle $I$ contenant $a$ et $b$, et $F$ une primitive de $f$ sur $I$, on pose $\int_a^bf(x)\,dx=F(b)-F(a)$ (le résultat ne dépend pas de la primitive choisie).[/]
<p>Interprétation : les parties sous l'axe des abscisses comptent <b>négativement</b>. Ainsi $\int_0^{2\pi}\sin x\,dx=0$ : les deux bosses s'annulent. Et $\int_b^af=-\int_a^bf$, $\int_a^af=0$.</p>
[prop|Propriétés ($f$, $g$ continues, $\lambda$ réel)]<ul><li><b>Linéarité</b> : $\int_a^b(f+g)=\int_a^bf+\int_a^bg$ et $\int_a^b\lambda f=\lambda\int_a^bf$.</li><li><b>Chasles</b> : $\int_a^cf=\int_a^bf+\int_b^cf$.</li><li><b>Positivité</b> : si $a\leq b$ et $f\geq0$ sur $[a;b]$, alors $\int_a^bf\geq0$.</li><li><b>Inégalités</b> : si $a\leq b$ et $f\leq g$ sur $[a;b]$, alors $\int_a^bf\leq\int_a^bg$.</li></ul>[/]
[ex|Majorer une intégrale]Pour $x\in[0;1]$, $0\leq\frac{x^n}{1+x}\leq x^n$, donc $0\leq\int_0^1\frac{x^n}{1+x}\,dx\leq\int_0^1x^n\,dx=\frac1{n+1}$. Par les gendarmes, cette intégrale tend vers $0$ quand $n\to+\infty$.[/]
[prop|Aire entre deux courbes]Si $f\geq g$ sur $[a;b]$ (avec $a\leq b$), l'aire entre les deux courbes est $\int_a^b\left(f(x)-g(x)\right)dx$. Entre $y=x$ et $y=x^2$ sur $[0;1]$ : $\frac12-\frac13=\frac16$ u.a.[/]
[def|Valeur moyenne]La valeur moyenne de $f$ sur $[a;b]$ ($a<b$) est $\mu=\frac1{b-a}\int_a^bf(x)\,dx$ : c'est la hauteur du rectangle de même aire. Valeur moyenne de $\sin$ sur $[0;\pi]$ : $\frac2\pi\approx0{,}637$.[/]
[ex|En physique]La température d'un café qui refroidit (chapitre 8), $T(t)=20+70\e^{-0{,}1t}$, a pour valeur moyenne sur les $10$ premières minutes $\frac1{10}\int_0^{10}T(t)\,dt=20+70\left(1-\e^{-1}\right)\approx64{,}2\,^\circ$C.[/]` },
    { id: "ipp", titre: "Intégration par parties", html: R`
[thm|Intégration par parties]Si $u$ et $v$ sont dérivables sur $[a;b]$, à dérivées continues : $$\int_a^bu(x)v'(x)\,dx=\left[u(x)v(x)\right]_a^b-\int_a^bu'(x)v(x)\,dx.$$ (Démonstration exigible.)[/]
[meth|Choisir $u$ et $v'$]On dérive ce qui se simplifie en dérivant (un polynôme, $\ln x$) et on primitive ce qui se primitive facilement ($\e^x$, $\sin$, $\cos$).[/]
[ex|Trois calculs (vérifiés numériquement)]
<ul><li>$\int_0^1x\e^x\,dx$ : $u=x$, $v'=\e^x$ ; $=\left[x\e^x\right]_0^1-\int_0^1\e^x\,dx=\e-(\e-1)=1$.</li>
<li>$\int_1^{\e}\ln x\,dx$ : $u=\ln x$, $v'=1$, $v=x$ ; $=\left[x\ln x\right]_1^{\e}-\int_1^{\e}1\,dx=\e-(\e-1)=1$.</li>
<li>$\int_0^\pi x\sin x\,dx$ : $u=x$, $v'=\sin x$, $v=-\cos x$ ; $=\left[-x\cos x\right]_0^\pi+\int_0^\pi\cos x\,dx=\pi+0=\pi$. (L'affirmation 3 du sujet de Polynésie du 16 juin 2026, qui annonçait $-\pi$, était donc fausse.)</li></ul>[/]` },
    { id: "suites", titre: "Suites d'intégrales", html: R`
[ex|Une suite classique]$I_n=\int_0^1\frac{x^n}{1+x}\,dx$ pour $n\in\N$.
<ul><li><b>Calcul de $I_0$</b> : $\int_0^1\frac1{1+x}\,dx=\left[\ln(1+x)\right]_0^1=\ln2$.</li>
<li><b>Relation</b> : $I_n+I_{n+1}=\int_0^1\frac{x^n(1+x)}{1+x}\,dx=\int_0^1x^n\,dx=\frac1{n+1}$. Donc $I_1=1-\ln2\approx0{,}307$.</li>
<li><b>Sens de variation</b> : $I_{n+1}-I_n=\int_0^1\frac{x^n(x-1)}{1+x}\,dx\leq0$ car l'intégrande est négative sur $[0;1]$ : la suite décroît.</li>
<li><b>Limite</b> : $0\leq I_n\leq\frac1{n+1}$ (partie précédente), donc $I_n\to0$.</li></ul>[/]
<p>C'est le schéma des sujets de bac : interprétation graphique, signe ou monotonie par positivité de l'intégrale, relation de récurrence (souvent par parties), limite par encadrement.</p>` }
  ],
  pieges: [
    { t: "Oublier le $dx$ ou la variable", h: R`$\int_0^1x^2$ sans $dx$ est incomplet ; et $\int_0^1t^2\,dx=t^2$ (la variable d'intégration est $x$).` },
    { t: "« Une intégrale est une aire »", h: R`Seulement si $f\geq0$ et $a\leq b$. Sinon elle peut être négative : $\int_0^{2\pi}\sin x\,dx=0$ alors que l'aire grisée vaut $4$.` },
    { t: "Le crochet", h: R`$\left[F(x)\right]_a^b=F(b)-F(a)$ : dans cet ordre. <span class="rature">$F(a)-F(b)$</span>.` },
    { t: "Le signe moins de l'intégration par parties", h: R`$\int uv'=[uv]-\int u'v$ : le terme intégral est <b>soustrait</b>.` },
    { t: "Inégalités et bornes", h: R`Intégrer $f\leq g$ donne $\int_a^bf\leq\int_a^bg$ seulement si $a\leq b$.` }
  ],
  demos: [
    { bo: true, t: "Pour $f$ positive croissante, $x\\mapsto\\int_a^xf(t)\\,dt$ est une primitive de $f$", h: R`
<p>Soit $f$ continue, positive et croissante sur $[a;b]$, et $F_a(x)=\int_a^xf(t)\,dt$. Soit $x\in[a;b[$ et $h>0$ avec $x+h\leq b$.</p>
<p>Par Chasles (vision aire), $F_a(x+h)-F_a(x)$ est l'aire sous la courbe entre $x$ et $x+h$. Comme $f$ est croissante, cette aire est comprise entre celle du rectangle de hauteur $f(x)$ et celle du rectangle de hauteur $f(x+h)$ :
$$hf(x)\leq F_a(x+h)-F_a(x)\leq hf(x+h).$$
En divisant par $h>0$ : $f(x)\leq\frac{F_a(x+h)-F_a(x)}h\leq f(x+h)$. Comme $f$ est continue, $f(x+h)\to f(x)$ quand $h\to0$ ; par les gendarmes, le taux d'accroissement tend vers $f(x)$. (Même raisonnement pour $h<0$.) Donc $F_a$ est dérivable et $F_a'(x)=f(x)$.</p>
<p><b>Conséquence.</b> Si $F$ est une primitive quelconque, $F=F_a+C$ (chapitre 8). Alors $F(b)-F(a)=F_a(b)-F_a(a)=\int_a^bf(t)\,dt-0$.</p>` },
    { bo: true, t: "Intégration par parties", h: R`
<p>$u$ et $v$ sont dérivables à dérivées continues sur $[a;b]$. Par la dérivée d'un produit, $(uv)'=u'v+uv'$, donc $uv'=(uv)'-u'v$.</p>
<p>Ces fonctions sont continues ; on intègre sur $[a;b]$ par linéarité :
$$\int_a^bu(x)v'(x)\,dx=\int_a^b(uv)'(x)\,dx-\int_a^bu'(x)v(x)\,dx.$$
Or $uv$ est une primitive de $(uv)'$, donc $\int_a^b(uv)'(x)\,dx=\left[u(x)v(x)\right]_a^b$. D'où la formule.</p>` }
  ],
  algos: [
    { bo: true, t: "Méthodes des rectangles, des milieux, des trapèzes", code: `def rectangles(f, a, b, n):
    h = (b - a) / n
    return sum(f(a + i * h) for i in range(n)) * h

def milieux(f, a, b, n):
    h = (b - a) / n
    return sum(f(a + (i + 0.5) * h) for i in range(n)) * h

def trapezes(f, a, b, n):
    h = (b - a) / n
    return sum((f(a + i * h) + f(a + (i + 1) * h)) / 2 for i in range(n)) * h

carre = lambda x: x * x
print(rectangles(carre, 0, 1, 4), milieux(carre, 0, 1, 4), trapezes(carre, 0, 1, 4))`, sortie: `0.21875 0.328125 0.34375`,
      apres: R`<p>Valeur exacte $\frac13\approx0{,}3333$ : avec seulement $4$ bandes, la méthode des milieux est la plus précise.</p>` },
    { bo: true, t: "Méthode de Monte-Carlo", avant: R`<p>On lance des points au hasard dans le carré $[0;1]^2$ ; la proportion de points sous la courbe de $x\mapsto x^2$ approche l'aire $\frac13$.</p>`, code: `from random import random

N = 100000
dessous = 0
for i in range(N):
    x, y = random(), random()
    if y <= x * x:
        dessous = dessous + 1
print(dessous / N)`, sortie: `(une valeur proche de 0,333, différente à chaque exécution)`,
      apres: R`<p>Avec $N=100\,000$ points, l'erreur est de l'ordre de quelques millièmes : la méthode converge lentement (en $\frac1{\sqrt N}$), mais marche en toute dimension.</p>` },
    { bo: true, t: "Algorithme de Brouncker pour $\\ln2$", avant: R`<p>Brouncker (XVII<sup>e</sup> siècle) a obtenu l'aire $\ln2=\int_1^2\frac1x\,dx$ comme une somme : $\ln2=\frac1{1\times2}+\frac1{3\times4}+\frac1{5\times6}+\dots$</p>`, code: `from math import log

s = 0
for k in range(1, 1001):
    s = s + 1 / ((2 * k - 1) * (2 * k))
print(s, log(2))`, sortie: `0.6928972430599386 0.6931471805599453`,
      apres: R`<p>Avec $1000$ termes, $3$ décimales exactes : la convergence est lente.</p>` }
  ],
  methodes: [
    { t: "Comment calculer une intégrale ?", h: R`
<ol><li>Chercher une primitive (tableau, formes composées), puis $F(b)-F(a)$.</li><li>Si l'intégrande est un produit « polynôme × exponentielle » ou contient $\ln x$ : intégration par parties.</li><li>Si l'on ne trouve pas de primitive : encadrer (rectangles, inégalités) ou estimer (Python).</li></ol>` },
    { t: "Comment encadrer une intégrale ?", h: R`
<p>Encadrer la fonction sur $[a;b]$ ($m\leq f(x)\leq M$, ou $g\leq f\leq h$), puis intégrer l'encadrement ($a\leq b$) : $m(b-a)\leq\int_a^bf\leq M(b-a)$.</p>` },
    { t: "Comment étudier une suite d'intégrales $I_n$ ?", h: R`
<ol><li>Interpréter graphiquement (aire si l'intégrande est positive).</li><li>Monotonie : signe de $I_{n+1}-I_n$, qui est l'intégrale d'une différence.</li><li>Encadrement pour la limite ; relation de récurrence par parties ou par linéarité.</li></ol>` }
  ],
  exos: [
    { niv: 1, t: "Calculs directs", enonce: R`<p>Calculer : $A=\int_0^2(3x^2-2x+1)\,dx$ ; $B=\int_0^1\e^{2x}\,dx$ ; $C=\int_0^{\pi/2}\cos x\,dx$ ; $D=\int_1^4\frac{1}{\sqrt x}\,dx$ ; $E=\int_0^1\frac{x}{x^2+1}\,dx$.</p>`,
      corrige: R`<p>$A=\left[x^3-x^2+x\right]_0^2=8-4+2=6$ ; $B=\left[\frac12\e^{2x}\right]_0^1=\frac{\e^2-1}2\approx3{,}195$ ; $C=\left[\sin x\right]_0^{\pi/2}=1$ ; $D=\left[2\sqrt x\right]_1^4=4-2=2$ ; $E=\left[\frac12\ln(x^2+1)\right]_0^1=\frac{\ln2}2\approx0{,}347$.</p>` },
    { niv: 1, t: "Aire et valeur moyenne", enonce: R`<ol><li>Calculer l'aire du domaine compris entre les courbes de $f(x)=x$ et $g(x)=x^2$ sur $[0;1]$.</li><li>Calculer la valeur moyenne de $\sin$ sur $[0;\pi]$.</li></ol>`,
      corrige: R`<ol><li>Sur $[0;1]$, $x\geq x^2$ : aire $=\int_0^1(x-x^2)\,dx=\frac12-\frac13=\frac16$ u.a.</li><li>$\frac1\pi\int_0^\pi\sin x\,dx=\frac2\pi\approx0{,}637$.</li></ol>` },
    { niv: 2, t: "Intégrations par parties", enonce: R`<p>Calculer : $\int_0^1x\e^{-x}\,dx$ ; $\int_1^{\e}x\ln x\,dx$.</p>`,
      corrige: R`<ul><li>$u=x$, $v'=\e^{-x}$, $v=-\e^{-x}$ : $\left[-x\e^{-x}\right]_0^1+\int_0^1\e^{-x}\,dx=-\e^{-1}+\left(1-\e^{-1}\right)=1-\frac2\e\approx0{,}264$.</li><li>$u=\ln x$, $v'=x$, $v=\frac{x^2}2$ : $\left[\frac{x^2}2\ln x\right]_1^{\e}-\int_1^{\e}\frac x2\,dx=\frac{\e^2}2-\frac{\e^2-1}4=\frac{\e^2+1}4\approx2{,}097$.</li></ul><p class="stylo">Contrôle : méthode des milieux avec $10\,000$ bandes, mêmes valeurs à $10^{-8}$ près.</p>` },
    { niv: 2, t: "Encadrer", enonce: R`<p>Montrer que pour $x\in[0;1]$, $\frac{1}{2}\leq\frac{1}{1+x^2}\leq1$, et en déduire un encadrement de $J=\int_0^1\frac1{1+x^2}\,dx$.</p>`,
      corrige: R`<p>$1\leq1+x^2\leq2$ sur $[0;1]$ ; la fonction inverse est décroissante sur $]0;+\infty[$ : $\frac12\leq\frac1{1+x^2}\leq1$. En intégrant sur $[0;1]$ : $\frac12\leq J\leq1$. <span class="tag hp">Pour aller plus loin</span> En fait $J=\frac\pi4\approx0{,}785$ (fonction arctangente, hors programme).</p>` },
    { niv: 3, t: "Aire sous $x\\e^{-x}$ (type bac)", enonce: R`<p>Soit $f(x)=x\e^{-x}$ sur $[0;+\infty[$.</p><ol><li>Montrer que $F(x)=-(x+1)\e^{-x}$ est une primitive de $f$.</li><li>Calculer l'aire $\mathcal{A}$ du domaine sous la courbe entre $x=0$ et $x=3$ (valeur exacte, puis approchée à $10^{-3}$).</li><li>En déduire la valeur moyenne de $f$ sur $[0;3]$.</li><li>Pour $t>0$, on pose $A(t)=\int_0^tf(x)\,dx$. Calculer $\lim_{t\to+\infty}A(t)$ et interpréter.</li></ol>`,
      corrige: R`<ol><li>$F'(x)=-\e^{-x}+(x+1)\e^{-x}=x\e^{-x}$. ✓</li><li>$f\geq0$ sur $[0;3]$ : $\mathcal A=F(3)-F(0)=-4\e^{-3}+1=1-4\e^{-3}\approx0{,}801$ u.a.</li><li>$\mu=\frac{1-4\e^{-3}}3\approx0{,}267$.</li><li>$A(t)=1-(t+1)\e^{-t}$ ; $t\e^{-t}\to0$ et $\e^{-t}\to0$, donc $A(t)\to1$ : l'aire sous la courbe sur $[0;+\infty[$, pourtant infiniment longue, tend vers $1$ u.a.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Centres étrangers, 10 juin 2026 (sujet 1), exercice 4, partie B", url: "https://www.apmep.fr/IMG/pdf/BAC_Specialite_Sujet_2026_J1_Centres_Etrangers_FK-v3-2.pdf", h: R`$I_n=\int_1^n\frac{\ln x}{x^2}\,dx$ : interprétation graphique, monotonie, rectangles en Python, intégration par parties $I_n=\frac{n-1-\ln n}{n}$, limite $1$ (contrôle : $I_{10}\approx0{,}6697$).` },
    { ref: "Bac 2025, Amérique du Nord, 22 mai 2025 (sujet 2), exercice 4, partie B", url: "https://www.apmep.fr/IMG/pdf/Amerique_du_Nord_J2_spe_22_05_2025_DV_FK.pdf", h: R`$I=\int_0^{\pi/2}\e^x\sin x\,dx$ et $J=\int_0^{\pi/2}\e^x\cos x\,dx$ par deux intégrations par parties (contrôle : $I=\frac{\e^{\pi/2}+1}2\approx2{,}905$).` },
    { ref: "Bac 2025, Centres étrangers, 13 juin 2025 (sujet 2), exercice 2, partie C", url: "https://www.apmep.fr/IMG/pdf/Etranger_spe_J2_13_06_2025_DV.pdf", h: R`Valeur moyenne de $\frac1{1+\e^{-0{,}2x}}$ sur $[0;40]$ grâce à une primitive (contrôle : $\approx0{,}913$).` }
  ],
  retenir: R`
[def|Intégrale]$f$ continue positive : $\int_a^bf$ = aire sous la courbe. Cas général : $\int_a^bf=F(b)-F(a)=[F]_a^b$, $F$ primitive de $f$.[/]
[thm|Le lien]$x\mapsto\int_a^xf(t)\,dt$ est la primitive de $f$ qui s'annule en $a$.[/]
[prop|Propriétés]Linéarité ; Chasles $\int_a^c=\int_a^b+\int_b^c$ ; $f\geq0$ et $a\leq b$ ⟹ $\int_a^bf\geq0$ ; $f\leq g$ et $a\leq b$ ⟹ $\int_a^bf\leq\int_a^bg$.[/]
<p><b>Aire entre deux courbes</b> ($f\geq g$) : $\int_a^b(f-g)$. <b>Valeur moyenne</b> : $\frac1{b-a}\int_a^bf$.</p>
[thm|Intégration par parties]$\int_a^buv'=[uv]_a^b-\int_a^bu'v$.[/]
<p><b>Rectangles</b> : $h\sum f(a+ih)$, $h=\frac{b-a}n$ ; encadrent l'aire si $f$ est monotone.</p>
<p class="stylo">Une intégrale n'est une aire que pour $f\geq0$ et $a\leq b$.</p>`,
  qcm: [
    { q: R`$\int_0^1x^2\,dx=$`, c: ["$\\frac12$", "$\\frac13$", "$1$", "$2$"], r: 1, e: R`$\left[\frac{x^3}3\right]_0^1=\frac13$.`, ref: "primitive" },
    { q: R`$\int_0^\pi\sin x\,dx=$`, c: ["$0$", "$1$", "$2$", "$\\pi$"], r: 2, e: R`$[-\cos x]_0^\pi=1-(-1)=2$.`, ref: "primitive" },
    { q: R`$\int_0^{2\pi}\sin x\,dx=$`, c: ["$0$", "$2$", "$4$", "$2\\pi$"], r: 0, e: R`Les parties au-dessus et au-dessous de l'axe se compensent.`, ref: "signe" },
    { q: R`Si $F$ est une primitive de $f$, $\int_a^bf(x)\,dx=$`, c: [R`$F(a)-F(b)$`, R`$F(b)-F(a)$`, R`$F(b)+F(a)$`, R`$f(b)-f(a)$`], r: 1, e: R`Le crochet $[F]_a^b=F(b)-F(a)$.`, ref: "primitive" },
    { q: R`La fonction $x\mapsto\int_1^x\frac1t\,dt$ est :`, c: [R`$\frac1x$`, R`$\ln x$`, R`$-\frac1{x^2}$`, R`$\ln x+1$`], r: 1, e: R`C'est la primitive de $\frac1x$ qui s'annule en $1$.`, ref: "primitive" },
    { q: R`La valeur moyenne de $f$ sur $[a;b]$ est :`, c: [R`$\int_a^bf$`, R`$\frac{f(a)+f(b)}2$`, R`$\frac1{b-a}\int_a^bf$`, R`$(b-a)\int_a^bf$`], r: 2, e: R`Hauteur du rectangle de base $b-a$ et de même aire.`, ref: "signe" },
    { q: R`Relation de Chasles :`, c: [R`$\int_a^bf+\int_b^cf=\int_a^cf$`, R`$\int_a^bf\times\int_b^cf=\int_a^cf$`, R`$\int_a^bf=\int_b^af$`, R`$\int_a^b(f\times g)=\int_a^bf\times\int_a^bg$`], r: 0, e: R`Les aires s'ajoutent bout à bout.`, ref: "signe" },
    { q: R`L'intégration par parties s'écrit :`, c: [R`$\int uv'=[uv]+\int u'v$`, R`$\int uv'=[uv]-\int u'v$`, R`$\int uv'=\int u\times\int v'$`, R`$\int uv'=[u'v]-\int uv$`], r: 1, e: R`Elle vient de $(uv)'=u'v+uv'$.`, ref: "ipp" },
    { q: R`$\int_0^1x\e^x\,dx=$`, c: ["$1$", "$\\e$", "$\\e-1$", "$0$"], r: 0, e: R`Par parties : $[x\e^x]_0^1-\int_0^1\e^x=\e-(\e-1)=1$.`, ref: "ipp" },
    { q: R`L'aire entre $y=x$ et $y=x^2$ sur $[0;1]$ vaut :`, c: ["$\\frac12$", "$\\frac13$", "$\\frac16$", "$1$"], r: 2, e: R`$\int_0^1(x-x^2)\,dx=\frac12-\frac13$.`, ref: "signe" },
    { q: R`Si $0\leq f(x)\leq x^n$ sur $[0;1]$, alors :`, c: [R`$\int_0^1f=\frac1{n+1}$`, R`$0\leq\int_0^1f\leq\frac1{n+1}$`, R`$\int_0^1f\geq\frac1{n+1}$`, R`on ne peut rien dire`], r: 1, e: R`Intégration des inégalités ($0\leq1$).`, ref: "signe" },
    { q: R`Pour $f$ croissante sur $[0;1]$, les rectangles « à gauche » donnent :`, c: ["une valeur par excès", "une valeur par défaut", "la valeur exacte", "on ne peut pas savoir"], r: 1, e: R`Ils sont sous la courbe : leur aire est inférieure à l'intégrale.`, ref: "rectangles" },
    { q: R`$\int_1^{\e}\ln x\,dx=$`, c: ["$0$", "$1$", "$\\e$", "$\\e-1$"], r: 1, e: R`Par parties avec $v'=1$ : $[x\ln x]_1^{\e}-(\e-1)=1$.`, ref: "ipp" }
  ],
  cartes: [
    [R`$\int_a^bf$ pour $f\geq0$ continue`, R`L'aire sous la courbe entre $x=a$ et $x=b$ (en u.a.).`],
    [R`$\int_a^bf$ avec une primitive $F$`, R`$F(b)-F(a)$`],
    [R`$x\mapsto\int_a^xf(t)\,dt$`, R`La primitive de $f$ qui s'annule en $a$.`],
    [R`Relation de Chasles`, R`$\int_a^bf+\int_b^cf=\int_a^cf$`],
    [R`Valeur moyenne sur $[a;b]$`, R`$\frac1{b-a}\int_a^bf(x)\,dx$`],
    [R`Aire entre deux courbes ($f\geq g$)`, R`$\int_a^b(f-g)$`],
    [R`Intégration par parties`, R`$\int_a^buv'=[uv]_a^b-\int_a^bu'v$`],
    [R`$\int_b^af$ en fonction de $\int_a^bf$`, R`$-\int_a^bf$`],
    [R`Positivité de l'intégrale`, R`$f\geq0$ et $a\leq b$ ⟹ $\int_a^bf\geq0$.`],
    [R`Méthode des rectangles à gauche`, R`$h\sum_{i=0}^{n-1}f(a+ih)$, $h=\frac{b-a}n$.`],
    [R`$\int_0^\pi\sin x\,dx$`, R`$2$`],
    [R`$\int_1^2\frac{dx}x$`, R`$\ln2$`]
  ]
};

/* Animation : les rectangles remplissent l'aire */
ANIMS.rectangles = {
  titre: "Des rectangles de plus en plus fins",
  vb: [360, 250],
  etapes: [
    { d: 3.5, l: R`On veut l'aire sous la courbe de $f(x)=x^2$ entre $0$ et $1$.` },
    { d: 4, l: R`$4$ rectangles à gauche (sous la courbe) : $0{,}219$. $4$ rectangles à droite (au-dessus) : $0{,}469$. L'aire est entre les deux.` },
    { d: 5, l: R`On double, puis on redouble le nombre de rectangles : $8$, puis $16$. L'escalier colle à la courbe, les deux sommes se resserrent.` },
    { d: 4.5, l: R`Avec $64$ rectangles : $0{,}326\leq I\leq0{,}341$. À la limite, les deux sommes valent $\frac13$ : c'est $\int_0^1x^2\,dx$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (x) { return x * x; };
    S.rep(-0.05, 1.08, -0.05, 1.12, { px: 0.25, py: 0.25 });
    var n = k <= 1 ? 4 : k === 2 ? (t < 0.5 ? 8 : 16) : 64, h = 1 / n;
    if (k >= 1) {
      var bas = 0, haut = 0, prog = k === 1 ? E(t) : 1;
      for (var i = 0; i < n; i++) {
        var x = i * h, yg = f(x), yd = f(x + h);
        bas += yg * h; haut += yd * h;
        S.rect(x, 0, x + h, yd, "a-plein2", { opacity: prog });
        S.rect(x, 0, x + h, yg, "a-plein");
      }
      S.txt(0.02, 1.02, n + " rectangles : " + ANIM.nf(bas, 3) + " ≤ I ≤ " + ANIM.nf(haut, 3), "b");
    }
    S.courbe(f, 0, 1.05, "g-c", 120, { "stroke-width": 2.6 });
    if (k === 0) { S.rect(0, 0, 1, 0.001, "a-plein"); S.poly([[0, 0]].concat(Array.apply(null, Array(41)).map(function (_, i) { return [i / 40, f(i / 40)]; })).concat([[1, 0]]), "a-plein", true, { opacity: E(t) }); }
    if (k === 3) S.txt(0.55, 0.12, "→ 1/3 ≈ 0,333", "r", "start", { opacity: E(t) });
  }
};

/* Animation : l'aire accumulée est une primitive */
ANIMS.aire = {
  titre: "L'aire accumulée a pour dérivée $f$",
  vb: [360, 280],
  etapes: [
    { d: 5, l: R`$f(x)=1+x\sin x$ (en haut). On fait glisser la borne $x$ : l'aire colorée $F(x)=\int_0^xf(t)\,dt$ grandit. En bas, on trace $F(x)$.` },
    { d: 4, l: R`Là où $f$ est grande, l'aire grandit vite : $F$ monte fort. Quand $f$ devient négative (après $x\approx3{,}44$), l'aire sous l'axe compte négativement : $F$ redescend.` },
    { d: 5, l: R`Un petit pas $h$ ajoute une bande d'aire $\approx f(x)\times h$. La pente de $F$ en $x$ vaut donc $f(x)$ : $F'=f$. L'aire est une primitive.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, f = function (x) { return 1 + x * Math.sin(x); };
    function F(x) { return x + Math.sin(x) - x * Math.cos(x); }
    var X = k === 0 ? 0.3 + E(t) * 2.9 : k === 1 ? 3.2 + E(t) * 0.9 : 4.1;
    var W = S.W, haut = { t: 8, b: 150 }, bas = { t: 160, b: 270 }, x0 = 0, x1 = 5, gx = function (x) { return 34 + (x - x0) / (x1 - x0) * (W - 44); };
    function Y1(y) { return haut.b - (y + 4) / 8 * (haut.b - haut.t); }
    function Y2(y) { return bas.b - (y + 1) / 9 * (bas.b - bas.t); }
    S.px.seg(34, Y1(0), W - 6, Y1(0), "g-axe"); S.px.seg(34, haut.t, 34, haut.b, "g-axe");
    S.px.seg(34, Y2(0), W - 6, Y2(0), "g-axe"); S.px.seg(34, bas.t, 34, bas.b, "g-axe");
    S.px.txt(40, haut.t + 12, "f", "b"); S.px.txt(40, bas.t + 12, "F(x) = aire de 0 à x", "r");
    var d = "M" + gx(0) + " " + Y1(0);
    for (var i = 0; i <= 80; i++) { var u = X * i / 80; d += "L" + gx(u).toFixed(1) + " " + Y1(f(u)).toFixed(1); }
    d += "L" + gx(X) + " " + Y1(0) + "Z";
    S.px.path(d, "a-plein");
    var c1 = "", c2 = "";
    for (var j = 0; j <= 120; j++) { var v = 5 * j / 120; c1 += (j ? "L" : "M") + gx(v).toFixed(1) + " " + Y1(f(v)).toFixed(1); if (v <= X) c2 += (j ? "L" : "M") + gx(v).toFixed(1) + " " + Y2(F(v)).toFixed(1); }
    S.px.path(c1, "g-c", { "stroke-width": 2.4 }); S.px.path(c2, "g-c2", { "stroke-width": 2.6 });
    S.px.seg(gx(X), Y1(f(X)), gx(X), Y2(F(X)), "a-craie");
    S.px.cercle(gx(X), Y1(f(X)), 4.5, "g-pt"); S.px.cercle(gx(X), Y2(F(X)), 4.5, "g-pt2");
    S.px.txt(W - 8, haut.t + 12, "f(x) = " + ANIM.nf(f(X), 2), "b", "end");
    S.px.txt(W - 8, bas.t + 12, "F(x) = " + ANIM.nf(F(X), 2), "r", "end");
    if (k === 2) {
      var h = 0.35 * E(t) + 0.05, s = f(X), px = (W - 44) / 5;
      S.px.rect(gx(X), Math.min(Y1(s), Y1(0)), h * px, Math.abs(Y1(s) - Y1(0)), "a-plein2");
      var dx = 0.8; S.px.seg(gx(X - dx), Y2(F(X) - s * dx), gx(X + dx), Y2(F(X) + s * dx), "g-c3", { "stroke-width": 2.2 });
      S.px.txt(gx(X) - 6, Y2(F(X)) + 22, "pente = f(x)", "c3", "end");
    }
  }
};
