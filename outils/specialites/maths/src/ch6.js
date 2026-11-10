/* ---------- Chapitre 6 : fonction logarithme népérien ---------- */
var CH6 = {
  id: "ch6", num: 6, statut: "ok", partie: "Analyse", titre: "Fonction logarithme népérien", court: "Logarithme",
  sous: "La fonction qui défait l'exponentielle : elle transforme les produits en sommes.",
  resume: "Réciproque de l'exponentielle, propriétés algébriques, équations, dérivée, limites, croissances comparées.",
  essentiel: [
    R`Pour tout réel $a>0$, l'équation $\e^x=a$ a une unique solution, notée $\ln(a)$. Ainsi $\e^{\ln a}=a$ pour $a>0$ et $\ln(\e^x)=x$ pour tout réel $x$ ; $\ln1=0$, $\ln\e=1$.`,
    R`$\ln$ transforme les produits en sommes : $\ln(ab)=\ln a+\ln b$ ; d'où $\ln\frac1a=-\ln a$, $\ln\frac ab=\ln a-\ln b$, $\ln(a^n)=n\ln a$, $\ln\sqrt a=\frac12\ln a$.`,
    R`$\ln$ est définie, dérivable et strictement croissante sur $]0;+\infty[$, avec $\ln'(x)=\frac1x$ ; $(\ln u)'=\frac{u'}{u}$.`,
    R`$\lim_{x\to0^+}\ln x=-\infty$, $\lim_{x\to+\infty}\ln x=+\infty$ ; croissances comparées : $\frac{\ln x}{x}\to0$ en $+\infty$, $x\ln x\to0$ en $0$.`,
    R`Le logarithme résout les équations « en exposant » : $q^n<s\iff n\ln q<\ln s$ ; attention, on divise par $\ln q$, négatif si $0<q<1$.`
  ],
  attendus: [
    R`Connaître la fonction $\ln$, construite comme réciproque de la fonction exponentielle, ses propriétés algébriques, sa dérivée, ses variations, ses limites et sa courbe.`,
    R`Utiliser l'équation fonctionnelle de l'exponentielle ou du logarithme pour transformer une écriture, résoudre une équation, une inéquation.`,
    R`Dans le cadre d'une résolution de problème, utiliser les propriétés des fonctions exponentielle et logarithme.`,
    R`Démonstrations exigibles : calcul de la dérivée de $\ln$ (la dérivabilité étant admise) ; limite en $0$ de $x\mapsto x\ln x$.`,
    R`Algorithme : algorithme de Briggs pour le calcul du logarithme.`
  ],
  premiere: R`
<ul><li>$\exp$ est définie, dérivable, strictement croissante sur $\R$, $\e^x>0$ ; $\e^{a+b}=\e^a\e^b$, $\e^{a-b}=\frac{\e^a}{\e^b}$, $(\e^a)^n=\e^{na}$.</li>
<li>$\e^a=\e^b\iff a=b$ et $\e^a<\e^b\iff a<b$ (stricte croissance).</li>
<li>Chapitre 4 : une fonction continue et strictement monotone sur un intervalle prend une fois et une seule chaque valeur intermédiaire.</li></ul>`,
  cours: [
    { id: "definition", titre: "Définition : la réciproque de l'exponentielle", html: R`
<p>La fonction $\exp$ est continue et strictement croissante sur $\R$, avec $\lim_{-\infty}\exp=0$ et $\lim_{+\infty}\exp=+\infty$. D'après le corollaire du théorème des valeurs intermédiaires, chaque réel $a>0$ est atteint <b>une et une seule fois</b>.</p>
[def|Logarithme népérien]Pour tout réel $a>0$, l'unique réel $x$ tel que $\e^x=a$ est noté $\ln(a)$. La fonction $\ln:x\mapsto\ln(x)$ est définie sur $]0;+\infty[$.[/]
[prop|Les deux sens]Pour tout $a>0$ : $\e^{\ln a}=a$. Pour tout réel $x$ : $\ln(\e^x)=x$. Pour $a>0$ et $x$ réel : $\e^x=a\iff x=\ln a$. En particulier $\ln1=0$ et $\ln\e=1$.[/]
[ex|Lire la définition]$\ln(\e^{3})=3$ ; $\e^{\ln 7}=7$ ; $\e^x=5\iff x=\ln5\approx1{,}609$. Et $\ln(-2)$ n'existe pas : aucune puissance de $\e$ n'est négative.[/]
<p>Dans un repère orthonormé, les courbes de $\exp$ et de $\ln$ sont <b>symétriques par rapport à la droite $y=x$</b> : le point $(a;\e^a)$ de l'une correspond au point $(\e^a;a)$ de l'autre.</p>
<div data-anim="reciproque"></div>
[hist|Napier et Briggs]Les premières tables de logarithmes (Napier en 1614, puis Briggs quelques années plus tard) ont servi à transformer les multiplications longues des astronomes et des navigateurs en additions. « Népérien » vient de Neper, l'autre graphie du nom de Napier. Le programme cite la méthode de Briggs, qui est dans l'onglet Python.[/]` },
    { id: "algebre", titre: "Propriétés algébriques", html: R`
[thm|Relation fonctionnelle]Pour tous réels $a>0$ et $b>0$ : $\ln(ab)=\ln a+\ln b$.[/]
<p><b>Preuve.</b> $\e^{\ln a+\ln b}=\e^{\ln a}\times\e^{\ln b}=ab=\e^{\ln(ab)}$. L'exponentielle étant strictement croissante, deux réels qui ont la même exponentielle sont égaux : $\ln a+\ln b=\ln(ab)$.</p>
<div data-anim="regle"></div>
[prop|Conséquences]Pour $a>0$, $b>0$ et $n\in\Z$ : $$\ln\frac1a=-\ln a,\qquad\ln\frac ab=\ln a-\ln b,\qquad\ln(a^n)=n\ln a,\qquad\ln\sqrt a=\frac12\ln a.$$[/]
[ex|Calculs]$\ln8=\ln(2^3)=3\ln2\approx2{,}079$ ; $\ln\frac{1}{\e^2}=-2$ ; $\ln\sqrt\e=\frac12$ ; $\e^{2\ln3}=\left(\e^{\ln3}\right)^2=9$ ; $\ln12-\ln3=\ln4=2\ln2$.[/]
[piege|Il n'y a pas de formule pour une somme]<span class="rature">$\ln(a+b)=\ln a+\ln b$</span> est faux : $\ln(1+1)=\ln2\approx0{,}69$ alors que $\ln1+\ln1=0$. Et <span class="rature">$\ln(a)\times\ln(b)=\ln(ab)$</span> aussi.[/]` },
    { id: "equations", titre: "Équations, inéquations, seuils", html: R`
[prop|Comparer]Pour $a>0$ et $b>0$ : $\ln a=\ln b\iff a=b$ et $\ln a<\ln b\iff a<b$. Le signe : $\ln x<0$ sur $]0;1[$, $\ln1=0$, $\ln x>0$ sur $]1;+\infty[$.[/]
[meth|Résoudre une équation avec ln]
<ol><li>Chercher le <b>domaine</b> : tout ce qui est sous un $\ln$ doit être strictement positif.</li><li>Regrouper avec les propriétés algébriques, puis passer à l'exponentielle (ou comparer les arguments).</li><li>Garder seulement les solutions du domaine.</li></ol>[/]
[ex|Avec un domaine]$\ln x+\ln(x-1)=\ln6$. Domaine : $x>1$. L'équation devient $\ln(x(x-1))=\ln6$, soit $x^2-x-6=0$, $(x-3)(x+2)=0$. Seule $x=3$ est dans le domaine.[/]
[ex|Inéquation]$\ln(2x-1)\leq\ln(x+3)$. Domaine : $x>\frac12$ (et alors $x+3>0$). $\ln$ est croissante : $2x-1\leq x+3\iff x\leq4$. Solution : $\left]\frac12;4\right]$.[/]
[meth|Les seuils sans tâtonner]Pour $0{,}8^n<0{,}01$ : la fonction $\ln$ est strictement croissante, donc $n\ln0{,}8<\ln0{,}01$. Or $\ln0{,}8<0$ : on divise et l'inégalité <b>change de sens</b> : $n>\frac{\ln0{,}01}{\ln0{,}8}\approx20{,}64$. Le premier entier est $n=21$.[/]
[ex|Doubler un capital]Placé à $3\,\%$ par an, un capital double quand $1{,}03^n\geq2\iff n\geq\frac{\ln2}{\ln1{,}03}\approx23{,}45$, soit au bout de $24$ ans.[/]` },
    { id: "derivee", titre: "Dérivée et variations", html: R`
[thm|Dérivée]$\ln$ est dérivable sur $]0;+\infty[$ et $\ln'(x)=\frac1x$. (Démonstration exigible, la dérivabilité étant admise.)[/]
<p>Comme $\frac1x>0$ sur $]0;+\infty[$, $\ln$ est <b>strictement croissante</b>. Et $\ln''(x)=-\frac1{x^2}<0$ : $\ln$ est <b>concave</b>.</p>
[prop|Composée]Si $u$ est dérivable et strictement positive sur $I$, alors $\ln(u)$ est dérivable sur $I$ et $\left(\ln u\right)'=\frac{u'}{u}$.[/]
[ex|Dérivées]$f(x)=\ln(x^2+1)$ : $f'(x)=\frac{2x}{x^2+1}$. $g(x)=x\ln x$ : $g'(x)=\ln x+x\times\frac1x=\ln x+1$. $h(x)=\ln(3x-2)$ sur $\left]\frac23;+\infty\right[$ : $h'(x)=\frac{3}{3x-2}$.[/]
[meth|Une inégalité par concavité]La tangente à la courbe de $\ln$ en $1$ a pour équation $y=x-1$. $\ln$ étant concave, sa courbe est sous ses tangentes : $\ln x\leq x-1$ pour tout $x>0$ (c'était l'affirmation 4, vraie, du sujet de Métropole du 18 juin 2025).[/]` },
    { id: "limites", titre: "Limites, courbe, croissances comparées", html: R`
[prop|Limites aux bornes]$\lim_{x\to+\infty}\ln x=+\infty$ et $\lim_{x\to0^+}\ln x=-\infty$ : l'axe des ordonnées est asymptote verticale.[/]
<p>La courbe passe par $(1;0)$ et $(\e;1)$ ; sa tangente en $1$ est $y=x-1$. Elle monte de plus en plus lentement : il faut atteindre $x=\e^{10}\approx22\,026$ pour que $\ln x$ dépasse $10$.</p>
[thm|Croissances comparées]Pour tout entier $n\geq1$ :
$$\lim_{x\to+\infty}\frac{\ln x}{x}=0,\qquad\lim_{x\to+\infty}\frac{\ln x}{x^n}=0,\qquad\lim_{x\to0^+}x\ln x=0,\qquad\lim_{x\to0^+}x^n\ln x=0.$$
<b>Toute puissance de $x$ l'emporte sur le logarithme.</b>[/]
[prop|Un taux d'accroissement]$\lim_{x\to0}\frac{\ln(1+x)}{x}=1$ : c'est le nombre dérivé de $\ln$ en $1$, $\ln'(1)=1$.[/]
[ex|Au bac (Centres étrangers, 10 juin 2026)]$f(x)=\frac{\ln x}{x^2}$ : en $0^+$, $\ln x\to-\infty$ et $\frac1{x^2}\to+\infty$, donc $f\to-\infty$ ; en $+\infty$, $\frac{\ln x}{x^2}\to0$ par croissance comparée : asymptotes $x=0$ et $y=0$.[/]
<p><span class="tag hp">Pour aller plus loin</span> Le logarithme décimal $\log(x)=\frac{\ln x}{\ln10}$ (utilisé en chimie pour le pH, en acoustique pour les décibels) n'est pas au programme de spécialité.</p>` }
  ],
  pieges: [
    { t: "Oublier le domaine", h: R`$\ln(x-3)$ n'existe que pour $x>3$. Une « solution » hors du domaine doit être rejetée.` },
    { t: "Inventer une formule pour une somme", h: R`<span class="rature">$\ln(a+b)=\ln a\times\ln b$</span>, <span class="rature">$\ln(a+b)=\ln a+\ln b$</span> : aucune formule n'existe.` },
    { t: "Diviser par un logarithme négatif", h: R`$\ln q<0$ quand $0<q<1$ : diviser par $\ln q$ change le sens de l'inégalité.` },
    { t: "$\\ln(a^n)$ et $(\\ln a)^n$", h: R`$\ln(a^2)=2\ln a$, mais $(\ln a)^2$ est autre chose : pour $a=\e$, $\ln(\e^2)=2$ et $(\ln\e)^2=1$.` },
    { t: "La dérivée de $\\ln u$", h: R`$\left(\ln(x^2+1)\right)'=\frac{2x}{x^2+1}$, pas <span class="rature">$\frac{1}{x^2+1}$</span> : il faut la dérivée de l'intérieur.` }
  ],
  demos: [
    { bo: true, t: "Dérivée de $\\ln$ (la dérivabilité étant admise)", h: R`
<p>Pour tout $x>0$, $\e^{\ln x}=x$. On dérive les deux membres. À gauche, c'est une composée $\e^{u}$ avec $u=\ln$ : sa dérivée est $u'\e^{u}=\ln'(x)\,\e^{\ln x}=\ln'(x)\times x$. À droite, la dérivée vaut $1$.</p>
<p>Donc $x\ln'(x)=1$, et comme $x\neq0$ : $\ln'(x)=\frac1x$.</p>
<p class="stylo">L'idée : dériver l'égalité $\e^{\ln x}=x$, qui définit $\ln$.</p>` },
    { bo: true, t: "Limite en $0$ de $x\\mapsto x\\ln x$", h: R`
<p>Pour $x>0$, on pose $X=-\ln x$, c'est-à-dire $x=\e^{-X}$. Quand $x\to0^+$, $\ln x\to-\infty$, donc $X\to+\infty$.</p>
<p>Alors $x\ln x=\e^{-X}\times(-X)=-\frac{X}{\e^X}$. Par croissance comparée (chapitre 3), $\frac{X}{\e^X}\to0$ quand $X\to+\infty$. Donc $\lim_{x\to0^+}x\ln x=0$.</p>
<p class="stylo">Le changement de variable ramène au résultat connu sur l'exponentielle.</p>` },
    { bo: false, t: "$\\lim_{x\\to+\\infty}\\frac{\\ln x}{x}=0$", h: R`
<p>On pose $X=\ln x$, donc $x=\e^X$, et $X\to+\infty$ quand $x\to+\infty$. Alors $\frac{\ln x}{x}=\frac{X}{\e^X}\to0$ (croissance comparée).</p>` },
    { bo: false, t: "Limites de $\\ln$ en $+\\infty$ et en $0$", h: R`
<p><b>En $+\infty$.</b> Soit $A$ un réel. Pour $x>\e^A$, la croissance de $\ln$ donne $\ln x>\ln(\e^A)=A$ : tout intervalle $[A;+\infty[$ contient $\ln x$ pour $x$ assez grand.</p>
<p><b>En $0$.</b> Pour $x>0$, $\ln x=-\ln\frac1x$ ; quand $x\to0^+$, $\frac1x\to+\infty$, donc $\ln\frac1x\to+\infty$ et $\ln x\to-\infty$.</p>` }
  ],
  algos: [
    { bo: true, t: "Algorithme de Briggs", avant: R`<p>Idée de Briggs : prendre plusieurs fois la racine carrée de $a$ ramène près de $1$, et près de $1$, $\ln(1+h)\approx h$. Comme $\ln\left(a^{1/2^k}\right)=\frac{\ln a}{2^k}$, on obtient $\ln a\approx2^k\left(a^{1/2^k}-1\right)$.</p>`,
      code: `from math import sqrt

def briggs(a, k):
    for i in range(k):
        a = sqrt(a)            # a devient a^(1/2^k)
    return 2**k * (a - 1)

print(briggs(2, 10))
print(briggs(2, 20))`, sortie: `0.6933818297000016
0.6931474097073078`,
      apres: R`<p>$\ln2\approx0{,}693147$ : avec $k=20$, six décimales exactes. (Au-delà, les arrondis de la machine dégradent le résultat : $a-1$ devient trop petit.)</p>` },
    { bo: false, t: "Seuil : boucle ou logarithme ?", code: `from math import log

n = 0
while 0.8**n >= 0.01:
    n = n + 1
print(n)
print(log(0.01) / log(0.8))`, sortie: `21
20.637702317032343`,
      apres: R`<p>Les deux méthodes concordent : la boucle trouve $21$, le calcul donne $n>20{,}64$.</p>` }
  ],
  methodes: [
    { t: "Comment résoudre une équation ou une inéquation avec $\\ln$ ou $\\exp$ ?", h: R`
<ol><li>Domaine.</li><li>Isoler l'exponentielle ($\e^{u}=a$) ou le logarithme ($\ln u=b$).</li><li>Appliquer la fonction réciproque : $\e^u=a\iff u=\ln a$ ($a>0$) ; $\ln u=b\iff u=\e^b$.</li><li>Pour une inéquation, utiliser la croissance de $\ln$ ou de $\exp$ (le sens est conservé).</li></ol>` },
    { t: "Comment étudier une fonction avec $\\ln$ ?", h: R`
<ol><li>Domaine (argument du $\ln$ strictement positif).</li><li>Limites aux bornes : croissances comparées, factorisation du terme qui domine.</li><li>Dérivée avec $(\ln u)'=\frac{u'}u$, signe (souvent celui d'un numérateur), tableau de variations.</li></ol>` },
    { t: "Comment trouver un seuil avec le logarithme ?", h: R`
<p>$q^n<s$ (avec $q>0$, $s>0$) ⟺ $n\ln q<\ln s$. Si $q>1$ : $n<\frac{\ln s}{\ln q}$. Si $0<q<1$ : $n>\frac{\ln s}{\ln q}$ (le sens change). Conclure par le premier entier qui convient.</p>` }
  ],
  exos: [
    { niv: 1, t: "Calculs et équations", enonce: R`<ol><li>Simplifier : $A=\ln(\e^3)$, $B=\e^{2\ln3}$, $C=\ln\frac1{\e^2}$, $D=\ln\sqrt\e$, $E=\ln12-\ln3-\ln4$.</li><li>Résoudre : $\e^{2x}=7$ ; $\ln(x)=-1$ ; $\ln x+\ln(x-1)=\ln6$.</li></ol>`,
      corrige: R`<ol><li>$A=3$ ; $B=9$ ; $C=-2$ ; $D=\frac12$ ; $E=\ln\frac{12}{3\times4}=\ln1=0$.</li><li>$2x=\ln7$, $x=\frac{\ln7}2\approx0{,}973$ ; $x=\e^{-1}=\frac1\e$ ; $x=3$ (voir le cours : $x=-2$ est hors du domaine $x>1$).</li></ol>` },
    { niv: 1, t: "Seuils", enonce: R`<ol><li>Plus petit entier $n$ tel que $2^n>1000$.</li><li>Plus petit entier $n$ tel que $\left(\frac12\right)^n<10^{-3}$.</li><li>Une substance a une concentration $c(t)=5\e^{-0{,}2t}$ (mg/L, $t$ en heures). À partir de quand $c(t)<1$ ?</li></ol>`,
      corrige: R`<ol><li>$n\ln2>\ln1000$, $n>\frac{\ln1000}{\ln2}\approx9{,}97$ : $n=10$ ($2^{10}=1024$).</li><li>$n\ln\frac12<\ln10^{-3}$ ; $\ln\frac12<0$ donc $n>\frac{\ln10^{-3}}{\ln0{,}5}\approx9{,}97$ : $n=10$.</li><li>$\e^{-0{,}2t}<\frac15\iff-0{,}2t<\ln\frac15=-\ln5\iff t>5\ln5\approx8{,}05$ h, soit environ $8$ h $03$ min.</li></ol>` },
    { niv: 2, t: "Une inégalité", enonce: R`<p>Soit $f(x)=x-\ln x$ sur $]0;+\infty[$.</p><ol><li>Étudier les variations de $f$.</li><li>En déduire que $\ln x\leq x-1$ pour tout $x>0$. Retrouver ce résultat par la concavité.</li></ol>`,
      corrige: R`<ol><li>$f'(x)=1-\frac1x=\frac{x-1}x$ : négative sur $]0;1]$, positive sur $[1;+\infty[$. Minimum $f(1)=1$.</li><li>Donc $x-\ln x\geq1$, soit $\ln x\leq x-1$. Par concavité : $\ln''(x)=-\frac1{x^2}<0$, la courbe est sous sa tangente en $1$, $y=x-1$.</li></ol>` },
    { niv: 2, t: "Limites", enonce: R`<p>Déterminer : $\lim_{x\to+\infty}(x-\ln x)$ ; $\lim_{x\to0^+}x^2\ln x$ ; $\lim_{x\to+\infty}\frac{\ln x+x}{x}$ ; $\lim_{x\to0^+}\frac{\ln x}{x}$.</p>`,
      corrige: R`<ul><li>$x-\ln x=x\left(1-\frac{\ln x}x\right)\to+\infty$.</li><li>$x^2\ln x=x\times(x\ln x)\to0\times0=0$.</li><li>$\frac{\ln x}x+1\to1$.</li><li>$\ln x\to-\infty$ et $\frac1x\to+\infty$ : le produit tend vers $-\infty$ (pas de forme indéterminée).</li></ul>` },
    { niv: 3, t: "Étude de $g(x)=x\\ln x-x$ (type bac)", enonce: R`<p>Soit $g$ définie sur $]0;+\infty[$ par $g(x)=x\ln x-x$.</p><ol><li>Déterminer les limites de $g$ en $0$ et en $+\infty$.</li><li>Montrer que $g'(x)=\ln x$ et dresser le tableau de variations.</li><li>Résoudre $g(x)=0$.</li><li>Étudier la convexité de $g$ et donner l'équation de sa tangente au point d'abscisse $\e$.</li><li>Que représente $g$ pour la fonction $\ln$ ? (lien avec le chapitre 8)</li></ol>`,
      corrige: R`<ol><li>En $0$ : $x\ln x\to0$ (démonstration exigible) et $x\to0$, donc $g\to0$. En $+\infty$ : $g(x)=x(\ln x-1)\to+\infty$.</li>
<li>$g'(x)=\ln x+x\times\frac1x-1=\ln x$ : négative sur $]0;1]$, positive ensuite. Minimum $g(1)=-1$.</li>
<li>$x(\ln x-1)=0$ avec $x>0$ : $\ln x=1$, $x=\e$.</li>
<li>$g''(x)=\frac1x>0$ : $g$ est convexe. Tangente en $\e$ : $g(\e)=0$, $g'(\e)=1$, donc $y=x-\e$.</li>
<li>$g'=\ln$ : $g$ est une <b>primitive</b> de $\ln$ sur $]0;+\infty[$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Centres étrangers, 10 juin 2026 (sujet 1), exercice 4, partie A", url: "https://www.apmep.fr/IMG/pdf/BAC_Specialite_Sujet_2026_J1_Centres_Etrangers_FK-v3-2.pdf", h: R`$f(x)=\frac{\ln x}{x^2}$ : limites et asymptotes, $f'(x)=\frac{1-2\ln x}{x^3}$, tableau de variations (maximum $\frac1{2\e}$ en $\sqrt\e$), tangente, convexité ($f''(x)=\frac{-5+6\ln x}{x^4}$, inflexion en $\e^{5/6}$).` },
    { ref: "Bac 2024, Métropole, 20 juin 2024 (sujet 2), exercice 3, partie B", url: "https://www.apmep.fr/IMG/pdf/Me_tropole_J2_spe_20_06_2024_VTFK.pdf", h: R`$f(x)=x^2+2x-1+\ln(x+2)$ sur $]-2;+\infty[$ : limite en $-2$, dérivée, unique solution $\alpha$ de $f(x)=0$ (contrôle : $\alpha\approx0{,}12$), point d'inflexion.` },
    { ref: "Bac 2025, Métropole, 18 juin 2025 (sujet 2), exercice 3, affirmation 4", url: "https://www.apmep.fr/IMG/pdf/Metropole__spe_J2_18_06_2025_DV_2.pdf", h: R`« Pour tout réel $x>0$, $\ln(x)-x+1\leq0$ » : vrai, par concavité ou étude de fonction (exercice 3 ci-dessus).` }
  ],
  retenir: R`
[def|Définition]Pour $a>0$ : $\ln a$ est l'unique réel $x$ tel que $\e^x=a$. $\e^{\ln a}=a$ ($a>0$) ; $\ln(\e^x)=x$ ($x\in\R$) ; $\ln1=0$ ; $\ln\e=1$.[/]
[prop|Algèbre ($a,b>0$, $n\in\Z$)]$\ln(ab)=\ln a+\ln b$ ; $\ln\frac ab=\ln a-\ln b$ ; $\ln\frac1a=-\ln a$ ; $\ln(a^n)=n\ln a$ ; $\ln\sqrt a=\frac12\ln a$.[/]
[thm|Analyse]$\ln'(x)=\frac1x$ ; $(\ln u)'=\frac{u'}u$ ; $\ln$ strictement croissante, concave ; $\ln x<0$ sur $]0;1[$, $>0$ sur $]1;+\infty[$.<br>$\lim_{0^+}\ln=-\infty$ ; $\lim_{+\infty}\ln=+\infty$ ; $\frac{\ln x}{x}\to0$ en $+\infty$ ; $x\ln x\to0$ en $0^+$ ; $\frac{\ln(1+x)}x\to1$ en $0$.[/]
<p>Inégalité : $\ln x\leq x-1$. Seuil : $q^n<s\iff n\ln q<\ln s$ (diviser par $\ln q<0$ change le sens).</p>
<p class="stylo">Domaine d'abord. Pas de formule pour $\ln(a+b)$.</p>`,
  qcm: [
    { q: R`$\ln(\e^5)=$`, c: ["$5$", "$\\e^5$", "$\\ln5$", "$5\\e$"], r: 0, e: R`$\ln(\e^x)=x$ pour tout réel $x$.`, ref: "definition" },
    { q: R`L'équation $\e^x=-3$ :`, c: ["a pour solution $\\ln3$", "a pour solution $-\\ln3$", "n'a pas de solution", "a pour solution $\\ln(-3)$"], r: 2, e: R`$\e^x>0$ pour tout $x$ : aucune solution. $\ln(-3)$ n'existe pas.`, ref: "definition" },
    { q: R`$\ln12-\ln3=$`, c: ["$\\ln9$", "$2\\ln2$", "$4$", "$\\frac{\\ln12}{\\ln3}$"], r: 1, e: R`$\ln\frac{12}3=\ln4=\ln(2^2)=2\ln2$.`, ref: "algebre" },
    { q: R`Pour $a,b>0$, laquelle est vraie ?`, c: [R`$\ln(a+b)=\ln a+\ln b$`, R`$\ln(ab)=\ln a\times\ln b$`, R`$\ln(ab)=\ln a+\ln b$`, R`$\ln\frac ab=\frac{\ln a}{\ln b}$`], r: 2, e: R`C'est la relation fonctionnelle : $\ln$ transforme les produits en sommes.`, ref: "algebre" },
    { q: R`L'ensemble des solutions de $\ln(x)<0$ est :`, c: ["$]-\\infty;0[$", "$]0;1[$", "$]1;+\\infty[$", "$]0;\\e[$"], r: 1, e: R`$\ln x<\ln1\iff x<1$, et $x>0$ (domaine).`, ref: "equations" },
    { q: R`Plus petit entier $n$ tel que $0{,}8^n<0{,}01$ :`, c: ["$20$", "$21$", "$11$", "$100$"], r: 1, e: R`$n>\frac{\ln0{,}01}{\ln0{,}8}\approx20{,}64$ ; attention au changement de sens car $\ln0{,}8<0$.`, ref: "equations" },
    { q: R`L'équation $\ln x+\ln(x-1)=\ln6$ a pour solution(s) :`, c: ["$3$ et $-2$", "$3$", "$-2$", "$6$"], r: 1, e: R`On obtient $x^2-x-6=0$, mais le domaine impose $x>1$ : seule $x=3$ convient.`, ref: "equations" },
    { q: R`La dérivée de $x\mapsto\ln(x^2+1)$ est :`, c: [R`$\frac1{x^2+1}$`, R`$\frac{2x}{x^2+1}$`, R`$2x\ln(x^2+1)$`, R`$\frac{2x}{\ln(x^2+1)}$`], r: 1, e: R`$(\ln u)'=\frac{u'}u$ avec $u=x^2+1$.`, ref: "derivee" },
    { q: R`La démonstration exigible de $\ln'(x)=\frac1x$ consiste à :`, c: ["dériver l'égalité $\\e^{\\ln x}=x$", "utiliser le taux d'accroissement de $\\ln$ en $0$", "utiliser la convexité", "calculer une primitive"], r: 0, e: R`$\ln'(x)\e^{\ln x}=1$, soit $x\ln'(x)=1$.`, ref: "derivee" },
    { q: R`$\lim_{x\to0^+}x\ln x=$`, c: ["$-\\infty$", "$0$", "$1$", "$+\\infty$"], r: 1, e: R`Démonstration exigible : avec $X=-\ln x$, $x\ln x=-\frac X{\e^X}\to0$.`, ref: "limites" },
    { q: R`$\lim_{x\to+\infty}\frac{\ln x}{x}=$`, c: ["$0$", "$1$", "$+\\infty$", "elle n'existe pas"], r: 0, e: R`Croissance comparée : $x$ l'emporte sur $\ln x$.`, ref: "limites" },
    { q: R`Pour tout $x>0$ :`, c: [R`$\ln x\geq x-1$`, R`$\ln x\leq x-1$`, R`$\ln x\leq x-2$`, R`$\ln x=x-1$`], r: 1, e: R`$\ln$ est concave : sa courbe est sous sa tangente en $1$, $y=x-1$.`, ref: "derivee" },
    { q: R`Dans un repère orthonormé, les courbes de $\exp$ et $\ln$ sont symétriques par rapport :`, c: ["à l'axe des abscisses", "à l'origine", "à la droite $y=x$", "à la droite $x=1$"], r: 2, e: R`$(a;\e^a)$ sur l'une ⟷ $(\e^a;a)$ sur l'autre : on échange abscisse et ordonnée.`, ref: "definition" }
  ],
  cartes: [
    [R`Définition de $\ln a$ ($a>0$)`, R`L'unique réel $x$ tel que $\e^x=a$.`],
    [R`$\e^{\ln a}$ et $\ln(\e^x)$`, R`$a$ (pour $a>0$) et $x$ (pour tout réel $x$).`],
    [R`$\ln1$ et $\ln\e$`, R`$0$ et $1$`],
    [R`$\ln(ab)=$ ?`, R`$\ln a+\ln b$`],
    [R`$\ln(a^n)=$ ? et $\ln\sqrt a=$ ?`, R`$n\ln a$ ; $\frac12\ln a$`],
    [R`$\ln'(x)$ et $(\ln u)'$`, R`$\frac1x$ ; $\frac{u'}u$`],
    [R`Signe de $\ln x$`, R`Négatif sur $]0;1[$, nul en $1$, positif sur $]1;+\infty[$.`],
    [R`$\lim_{x\to0^+}\ln x$ et $\lim_{x\to+\infty}\ln x$`, R`$-\infty$ et $+\infty$`],
    [R`$\lim_{x\to+\infty}\frac{\ln x}x$`, R`$0$`],
    [R`$\lim_{x\to0^+}x\ln x$`, R`$0$`],
    [R`$\lim_{x\to0}\frac{\ln(1+x)}x$`, R`$1$`],
    [R`Inégalité de concavité du logarithme`, R`$\ln x\leq x-1$ pour tout $x>0$.`],
    [R`Résoudre $q^n<s$ avec $0<q<1$`, R`$n>\frac{\ln s}{\ln q}$ (le sens change).`]
  ]
};

/* Animation : ln, reflet de exp dans le miroir y = x */
ANIMS.reciproque = {
  titre: "$\\ln$ : l'exponentielle vue dans le miroir $y=x$",
  vb: [340, 340],
  etapes: [
    { d: 3, l: R`La courbe de $\exp$ et la droite $y=x$, dans un repère orthonormé.` },
    { d: 6, l: R`Chaque point $M(a;\e^a)$ a un reflet $M'(\e^a;a)$ de l'autre côté de la droite $y=x$. Les reflets dessinent la courbe de $\ln$ : on a échangé « l'entrée » et « la sortie ».` },
    { d: 4, l: R`Lecture : $(0;1)$ se reflète en $(1;0)$, donc $\ln1=0$ ; $(1;\e)$ se reflète en $(\e;1)$, donc $\ln\e=1$.` },
    { d: 5, l: R`La tangente en $M$ a pour pente $\e^a$ ; son reflet a pour pente $\frac1{\e^a}=\frac1x$ au point d'abscisse $x=\e^a$. C'est $\ln'(x)=\frac1x$.` },
    { d: 4, l: R`L'asymptote $y=0$ de $\exp$ en $-\infty$ se reflète en l'asymptote $x=0$ de $\ln$ : $\lim_{x\to0^+}\ln x=-\infty$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, ex = Math.exp, ln = Math.log;
    S.rep(-3, 5, -3, 5, { px: 1, py: 1, marges: { l: 26, r: 8, t: 8, b: 22 } });
    S.seg(-3, -3, 5, 5, "g-as");
    S.txt(4.6, 4.95, "y = x", "r", "end");
    S.courbe(ex, -3, ln(5), "g-c", 160);
    S.txt(1.22, 4.6, "exp", "b", "end");
    var aMax = k === 0 ? -3 : k === 1 ? ANIM.l(-3, ln(5) - 0.01, E(t)) : ln(5) - 0.01;
    if (aMax > -3) S.courbe(ln, ex(-3), ex(aMax), "g-c2", 160, { "stroke-width": 3 });
    if (k >= 2 || (k === 1 && t > 0.6)) S.txt(3.9, 0.95, "ln", "r", "start");
    function paire(a, lab) {
      var M = [a, ex(a)], P = [ex(a), a];
      S.seg(M[0], M[1], P[0], P[1], "a-craie");
      S.pt(M[0], M[1], "g-pt", 4.5); S.pt(P[0], P[1], "g-pt2", 4.5);
      if (lab) {
        S.txt(M[0] - 0.15, Math.min(M[1] + 0.25, 4.65), lab[0], "b", "end");
        if (P[0] > 4) S.txt(P[0] - 0.1, P[1] + 0.35, lab[1], "r", "end"); else S.txt(P[0] + 0.12, P[1] - 0.4, lab[1], "r", "start");
      }
    }
    if (k === 1) paire(aMax, ["M", "M'"]);
    if (k === 2) { paire(0, ["(0;1)", "(1;0)"]); if (t > 0.45) paire(1, ["(1;e)", "(e;1)"]); }
    if (k === 3) {
      var a = ANIM.l(-1.2, 1.2, E(t)), m = ex(a);
      paire(a, ["M", "M'"]);
      S.seg(a - 2, m - 2 * m, a + 2, m + 2 * m, "g-c3");
      S.seg(m - 2 * m, a - 2, m + 2 * m, a + 2, "g-c3");
      S.txt(4.9, -2.05, "pente en M : " + ANIM.nf(m, 2), "b", "end");
      S.txt(4.9, -2.65, "pente en M' : " + ANIM.nf(1 / m, 2) + " = 1/" + ANIM.nf(m, 2), "r", "end");
    }
    if (k === 4) {
      var o = E(t);
      S.seg(-3, 0, 5, 0, "g-c", { "stroke-width": 3, opacity: 0.25 + 0.5 * o });
      S.seg(0, -3, 0, 5, "g-c2", { "stroke-width": 3, opacity: 0.25 + 0.5 * o });
      S.txt(-2.9, 0.42, "asymptote y = 0", "b", "start");
      S.txt(0.12, -2.7, "asymptote x = 0", "r");
    }
  }
};

/* Animation : la règle à calcul, ou ln(ab) = ln a + ln b */
ANIMS.regle = {
  titre: R`La règle à calcul : multiplier en ajoutant des $\ln$`,
  vb: [360, 220],
  etapes: [
    { d: 4, l: R`Une règle graduée « en logarithmes » : chaque nombre $x$ est placé à une distance proportionnelle à $\ln x$ du bord. Le $1$ est au bord, car $\ln1=0$ ; les graduations se serrent vers la droite.` },
    { d: 4, l: R`La longueur de $1$ à $2$ représente $\ln2\approx0{,}69$ ; celle de $1$ à $3$ représente $\ln3\approx1{,}10$.` },
    { d: 5, l: R`On met les deux longueurs bout à bout : on arrive exactement sur la graduation $6$. $\ln2+\ln3=\ln6$ : c'est $\ln(ab)=\ln a+\ln b$.` },
    { d: 6, l: R`Une seconde règle glisse : son $1$ vient sous le $2$. Au-dessus de chaque nombre $b$ de la règle mobile, on lit $2b$ sur la règle fixe : $2\times1{,}5=3$, $2\times2=4$, $2\times3=6$, $2\times4=8$, $2\times5=10$.` },
    { d: 4, l: R`Multiplier, c'est additionner des longueurs de logarithmes. Les règles à calcul, utilisées du XVII<sup>e</sup> siècle jusqu'à l'arrivée des calculatrices électroniques dans les années 1970, reposent sur cette propriété.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, x0 = 30, L = 300, pos = function (v) { return x0 + L * Math.log(v) / Math.LN10; };
    var REG = "fill:var(--papier);stroke:var(--encre2);stroke-width:1.2";
    /* règle fixe : graduations sur le bord bas */
    S.px.rect(x0 - 8, 66, L + 16, 32, "", { rx: 4, style: REG });
    for (var v = 1; v <= 10; v += 0.5) {
      var o = k === 0 ? E(p(t, (v - 1) / 12, (v - 1) / 12 + 0.25)) : 1, ent = v % 1 === 0;
      S.px.seg(pos(v), 98, pos(v), ent ? 84 : 90, "a-branche", { opacity: o, style: "stroke:var(--encre)" });
      if (ent) S.px.txt(pos(v), 80, String(v), "", "middle", { opacity: o, "font-size": 12 });
    }
    function crochet(a, b, y, cls, lab, op) {
      S.px.seg(a, y, b, y, cls, { opacity: op, "stroke-width": 3 });
      S.px.seg(a, y - 5, a, y + 5, cls, { opacity: op });
      S.px.seg(b, y - 5, b, y + 5, cls, { opacity: op });
      S.px.txt((a + b) / 2, y - 8, lab, cls === "g-c2" ? "r" : "b", "middle", { opacity: op });
    }
    if (k === 1 || k === 2) {
      var o1 = k === 1 ? E(p(t, 0, 0.4)) : 1, o2 = k === 1 ? E(p(t, 0.4, 0.8)) : 1;
      crochet(pos(1), pos(2), 52, "g-c", "ln 2", o1);
      var dx = k === 2 ? E(p(t, 0, 0.6)) * (pos(2) - pos(1)) : 0, yy = k === 2 ? ANIM.l(28, 52, E(p(t, 0, 0.6))) : 28;
      crochet(pos(1) + dx, pos(3) + dx, yy, "g-c2", "ln 3", o2);
      if (k === 2 && t > 0.6) {
        var o3 = E(p(t, 0.6, 0.85));
        S.px.seg(pos(6), 52, pos(6), 98, "g-c3", { opacity: o3, "stroke-dasharray": "4 3" });
        S.px.cercle(pos(6), 80, 11, "", { opacity: o3, style: "fill:none;stroke:var(--vert);stroke-width:2" });
        S.px.math(20, 150, 320, 40, R`$\ln2+\ln3=\ln6$`, { opacity: o3 });
      }
    }
    if (k >= 3) {
      var dec = (k === 3 ? E(p(t, 0, 0.4)) : 1) * (pos(2) - pos(1)), lim = x0 + L + 8;
      S.px.rect(x0 - 8 + dec, 102, lim - (x0 - 8 + dec), 32, "", { style: REG + ";fill:var(--bleu-p)" });
      for (var w = 1; w <= 10; w += 0.5) {
        var X = pos(w) + dec; if (X > lim - 2) break;
        var en = w % 1 === 0;
        S.px.seg(X, 102, X, en ? 116 : 110, "a-branche", { style: "stroke:var(--bleu)" });
        if (en) S.px.txt(X, 128, String(w), "b", "middle", { "font-size": 12 });
      }
      var o4 = k === 3 ? E(p(t, 0.45, 0.7)) : 1;
      [1.5, 2, 3, 4, 5].forEach(function (b, i) {
        var oi = k === 3 ? E(p(t, 0.45 + i * 0.09, 0.6 + i * 0.09)) : 1;
        S.px.seg(pos(2 * b), 84, pos(2 * b), 116, "g-c3", { opacity: oi, "stroke-width": 2.6 });
      });
      S.px.math(20, 148, 320, 34, R`$2\times b$ se lit au-dessus de $b$`, { opacity: o4 });
      if (k === 4) S.px.math(20, 182, 320, 36, R`$\ln(ab)=\ln a+\ln b$`, { opacity: E(p(t, 0, 0.5)) });
    }
  }
};
