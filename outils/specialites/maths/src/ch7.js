/* ---------- Chapitre 7 : fonctions sinus et cosinus ---------- */
var CH7 = {
  id: "ch7", num: 7, statut: "ok", partie: "Analyse", titre: "Fonctions sinus et cosinus", court: "Sinus et cosinus",
  sous: "Le point qui tourne sur le cercle, déroulé en courbe : dérivées, variations, équations.",
  resume: "Dérivées, variations, courbes ; équations et inéquations trigonométriques, optimisation.",
  essentiel: [
    R`Pour tout réel $x$, $\cos x$ et $\sin x$ sont l'abscisse et l'ordonnée du point du cercle trigonométrique associé à $x$ ; $\cos^2x+\sin^2x=1$.`,
    R`$\cos$ et $\sin$ sont $2\pi$-périodiques ; $\cos$ est paire, $\sin$ est impaire : on les étudie sur $[0;\pi]$ ou $[-\pi;\pi]$.`,
    R`$\sin'=\cos$ et $\cos'=-\sin$ ; plus généralement $(\sin u)'=u'\cos u$ et $(\cos u)'=-u'\sin u$.`,
    R`Sur $[-\pi;\pi]$, $\cos x=a$ (avec $-1<a<1$) a deux solutions opposées $\pm\alpha$ ; $\cos x\leq a$ se lit sur le cercle.`,
    R`$\lim_{x\to0}\frac{\sin x}{x}=1$ : c'est le nombre dérivé de $\sin$ en $0$.`
  ],
  attendus: [
    R`Connaître les fonctions sinus et cosinus : dérivées, variations, courbes représentatives.`,
    R`Résoudre une équation du type $\cos x=a$, une inéquation de la forme $\cos x\leq a$ sur $[-\pi;\pi]$.`,
    R`Dans le cadre de la résolution de problème, notamment géométrique, étudier une fonction simple définie à partir de fonctions trigonométriques, pour déterminer des variations, un optimum.`,
    R`Ce chapitre n'a pas de démonstration exigible ; la fonction tangente est un approfondissement possible.`
  ],
  premiere: R`
<ul><li>Le radian : sur le cercle trigonométrique (rayon $1$), un arc de longueur $x$ correspond à l'angle $x$ radians ; $\pi$ rad $=180^\circ$.</li>
<li>Valeurs remarquables :</li></ul>
<div class="tab-wrap"><table><tr><th>$x$</th><th>$0$</th><th>$\frac\pi6$</th><th>$\frac\pi4$</th><th>$\frac\pi3$</th><th>$\frac\pi2$</th><th>$\pi$</th></tr>
<tr><td>$\cos x$</td><td>$1$</td><td>$\frac{\sqrt3}2$</td><td>$\frac{\sqrt2}2$</td><td>$\frac12$</td><td>$0$</td><td>$-1$</td></tr>
<tr><td>$\sin x$</td><td>$0$</td><td>$\frac12$</td><td>$\frac{\sqrt2}2$</td><td>$\frac{\sqrt3}2$</td><td>$1$</td><td>$0$</td></tr></table></div>
<ul><li>$\cos(-x)=\cos x$, $\sin(-x)=-\sin x$, $\cos(\pi-x)=-\cos x$, $\sin(\pi-x)=\sin x$, $\cos(x+2\pi)=\cos x$.</li></ul>`,
  cours: [
    { id: "cercle", titre: "Du cercle à la courbe", html: R`
[def|Cosinus et sinus d'un réel]Sur le cercle trigonométrique, on enroule la droite des réels à partir du point $I(1;0)$, dans le sens direct. Au réel $x$ correspond un point $M$ ; ses coordonnées sont $(\cos x;\sin x)$.[/]
<p>Quand $x$ augmente, $M$ tourne : $\sin x$ (sa hauteur) et $\cos x$ (son abscisse) oscillent entre $-1$ et $1$. En reportant la hauteur en fonction de $x$, on « déroule » le cercle : c'est la sinusoïde.</p>
<div data-anim="cercle"></div>
[prop|Propriétés]Pour tout réel $x$ : $-1\leq\cos x\leq1$, $-1\leq\sin x\leq1$, $\cos^2x+\sin^2x=1$.<br>Périodicité : $\cos(x+2\pi)=\cos x$ et $\sin(x+2\pi)=\sin x$.<br>Parité : $\cos(-x)=\cos x$ ($\cos$ paire, courbe symétrique par rapport à l'axe des ordonnées), $\sin(-x)=-\sin x$ ($\sin$ impaire, courbe symétrique par rapport à l'origine).[/]
[ex|Ce qu'on en déduit]Il suffit d'étudier $\cos$ sur $[0;\pi]$ : la parité donne $[-\pi;0]$, puis la périodicité tout $\R$. Et $\cos x=\sin\left(x+\frac\pi2\right)$ : la courbe de $\cos$ est celle de $\sin$ décalée de $\frac\pi2$ vers la gauche.[/]` },
    { id: "derivees", titre: "Dérivées", html: R`
[thm|Dérivées]$\sin$ et $\cos$ sont dérivables sur $\R$, et $\sin'(x)=\cos x$, $\cos'(x)=-\sin x$.[/]
[prop|Un taux d'accroissement célèbre]Le nombre dérivé de $\sin$ en $0$ vaut $\cos0=1$, donc $\lim_{x\to0}\frac{\sin x}{x}=\lim_{x\to0}\frac{\sin x-\sin0}{x-0}=1$. Numériquement : $\frac{\sin(0{,}01)}{0{,}01}\approx0{,}99998$. (Utilisé au bac : Asie, 9 juin 2026.)[/]
[prop|Composées]Si $u$ est dérivable : $\left(\sin u\right)'=u'\cos u$ et $\left(\cos u\right)'=-u'\sin u$. En particulier $\left(\sin(ax+b)\right)'=a\cos(ax+b)$.[/]
[ex|Calculs (vérifiés numériquement)]$\left(\sin(3x+1)\right)'=3\cos(3x+1)$ ; $\left(\cos^2x\right)'=2\cos x\times(-\sin x)=-2\sin x\cos x$ ; $\left(\e^{-x}\cos x\right)'=-\e^{-x}\cos x-\e^{-x}\sin x=-\e^{-x}(\cos x+\sin x)$ ; $\left(x\sin x\right)'=\sin x+x\cos x$.[/]
[piege|Le signe de la dérivée du cosinus]$\cos'=-\sin$ (avec un moins) ; $\sin'=\cos$ (sans). Moyen mnémotechnique : en dérivant quatre fois, on revient au départ : $\sin\to\cos\to-\sin\to-\cos\to\sin$.[/]` },
    { id: "variations", titre: "Variations et courbes", html: R`
<p>Sur $[0;\pi]$, $\cos'(x)=-\sin x\leq0$ : $\cos$ est décroissante, de $1$ à $-1$. Sur $\left[-\frac\pi2;\frac\pi2\right]$, $\sin'(x)=\cos x\geq0$ : $\sin$ est croissante, de $-1$ à $1$.</p>
<div class="tab-wrap"><table><tr><th>$x$</th><th>$-\pi$</th><th>$-\frac\pi2$</th><th>$0$</th><th>$\frac\pi2$</th><th>$\pi$</th></tr>
<tr><td>$\cos x$</td><td>$-1$ ↗</td><td>$0$ ↗</td><td>$1$ (max) ↘</td><td>$0$ ↘</td><td>$-1$</td></tr>
<tr><td>$\sin x$</td><td>$0$ ↘</td><td>$-1$ (min) ↗</td><td>$0$ ↗</td><td>$1$ (max) ↘</td><td>$0$</td></tr></table></div>
[ex|Tangente en $0$]La tangente à la courbe de $\sin$ en $0$ a pour équation $y=x$ (pente $\cos0=1$). Pour $x$ proche de $0$, $\sin x\approx x$ : $\sin(0{,}1)\approx0{,}0998$.[/]
<p><span class="tag hp">Pour aller plus loin</span> La fonction tangente $\tan x=\frac{\sin x}{\cos x}$ (définie quand $\cos x\neq0$) a pour dérivée $1+\tan^2x=\frac1{\cos^2x}$. Approfondissement non exigible.</p>` },
    { id: "equations", titre: "Équations et inéquations", html: R`
[meth|Résoudre $\cos x=a$ sur $[-\pi;\pi]$]
<ol><li>Si $a>1$ ou $a<-1$ : pas de solution.</li><li>Sinon, trouver un angle $\alpha\in[0;\pi]$ tel que $\cos\alpha=a$ (valeur remarquable, ou calculatrice).</li><li>Sur $[-\pi;\pi]$, les solutions sont $\alpha$ et $-\alpha$ (une seule si $a=\pm1$).</li></ol>[/]
[ex|Exemples]$\cos x=\frac12$ : $x=\frac\pi3$ ou $x=-\frac\pi3$. $\cos x=-\frac{\sqrt3}2$ : $x=\pm\frac{5\pi}6$. $\sin x=\frac{\sqrt2}2$ sur $[-\pi;\pi]$ : $x=\frac\pi4$ ou $x=\pi-\frac\pi4=\frac{3\pi}4$ (avec $\sin(\pi-x)=\sin x$).[/]
[meth|Inéquation $\cos x\leq a$]Sur le cercle, $\cos x\leq a$ correspond aux points <b>à gauche</b> de la droite verticale d'abscisse $a$. Pour $a=\frac12$, sur $[-\pi;\pi]$ : $x\in\left[-\pi;-\frac\pi3\right]\cup\left[\frac\pi3;\pi\right]$.[/]
[ex|Avec le sinus]$2\sin x-1\geq0$ sur $[0;2\pi]$ ⟺ $\sin x\geq\frac12$ ⟺ $x\in\left[\frac\pi6;\frac{5\pi}6\right]$ (points au-dessus de la droite horizontale d'ordonnée $\frac12$).[/]
<div data-anim="trigEq"></div>` },
    { id: "optimum", titre: "Étudier une fonction : un optimum géométrique", html: R`
[ex|Le plus grand rectangle dans un demi-disque]On inscrit un rectangle dans un demi-disque de rayon $1$ : un côté sur le diamètre, deux sommets sur le demi-cercle, repérés par l'angle $\theta\in\left[0;\frac\pi2\right]$. Le rectangle a pour largeur $2\cos\theta$ et pour hauteur $\sin\theta$ : $A(\theta)=2\sin\theta\cos\theta$.
<p>$A'(\theta)=2\left(\cos\theta\cos\theta+\sin\theta\times(-\sin\theta)\right)=2\left(\cos^2\theta-\sin^2\theta\right)$.</p>
<p>Sur $\left[0;\frac\pi2\right]$, $\cos\theta$ et $\sin\theta$ sont positifs, donc $A'(\theta)\geq0\iff\cos\theta\geq\sin\theta\iff\theta\leq\frac\pi4$. L'aire est maximale pour $\theta=\frac\pi4$ : $A\left(\frac\pi4\right)=2\times\frac{\sqrt2}2\times\frac{\sqrt2}2=1$ (le rectangle mesure $\sqrt2$ sur $\frac{\sqrt2}2$).</p>[/]
[meth|Les réflexes]Restreindre l'étude grâce à la périodicité et la parité ; factoriser la dérivée ; étudier le signe de $\sin$ ou $\cos$ sur l'intervalle avec le cercle.[/]` }
  ],
  pieges: [
    { t: "Degrés et radians", h: R`En analyse, $x$ est en radians. Ta calculatrice doit être en mode radian : $\cos(60)$ en radians vaut environ $-0{,}952$, pas $\frac12$.` },
    { t: "Oublier une solution", h: R`$\cos x=\frac12$ a <b>deux</b> solutions sur $[-\pi;\pi]$ : $\frac\pi3$ et $-\frac\pi3$. Fais toujours un dessin du cercle.` },
    { t: "Signe de la dérivée", h: R`<span class="rature">$\cos'=\sin$</span> : non, $\cos'=-\sin$.` },
    { t: "$\\cos^2x$ et $\\cos(x^2)$", h: R`$\cos^2x=(\cos x)^2$ ; sa dérivée est $-2\sin x\cos x$. $\cos(x^2)$ a pour dérivée $-2x\sin(x^2)$.` }
  ],
  demos: [
    { bo: false, t: "Pourquoi $\\lim_{x\\to0}\\frac{\\sin x}{x}=1$ (idée géométrique)", h: R`
<p><span class="tag hp">Pour aller plus loin</span> Pour $0<x<\frac\pi2$, sur le cercle trigonométrique, on compare trois aires : le triangle $OIM$ (aire $\frac{\sin x}2$), le secteur angulaire (aire $\frac x2$) et le triangle $OIT$ formé avec la tangente en $I$ (aire $\frac{\tan x}2$). D'où $\sin x\leq x\leq\frac{\sin x}{\cos x}$, puis $\cos x\leq\frac{\sin x}x\leq1$. Comme $\cos x\to1$, les gendarmes donnent la limite $1$. (Au programme, on admet $\sin'=\cos$.)</p>` },
    { bo: false, t: "$\\cos'(x)=-\\sin x$ à partir de $\\sin'=\\cos$", h: R`
<p>Pour tout réel $x$, $\cos x=\sin\left(x+\frac\pi2\right)$. Par la dérivée d'une composée : $\cos'(x)=\cos\left(x+\frac\pi2\right)=-\sin x$ (car $\cos\left(x+\frac\pi2\right)=-\sin x$ sur le cercle : rotation d'un quart de tour).</p>` }
  ],
  algos: [
    { bo: false, t: "Une valeur approchée de $\\pi$ grâce au cosinus", avant: R`<p>$\cos$ s'annule une seule fois sur $[1;2]$, en $\frac\pi2$ (continue, strictement décroissante, $\cos1>0>\cos2$). Une dichotomie donne donc $\pi$ (algorithme de « recherche de valeurs approchées de $\pi$ » cité par le programme).</p>`,
      code: `from math import cos

a, b = 1.0, 2.0
for k in range(40):
    m = (a + b) / 2
    if cos(a) * cos(m) <= 0:
        b = m
    else:
        a = m
print(2 * a)`, sortie: `3.1415926535883045`,
      apres: R`<p>$\pi\approx3{,}14159265359$ : $11$ décimales exactes après $40$ étapes ($\frac1{2^{40}}\approx9\times10^{-13}$).</p>` },
    { bo: false, t: "Tabuler une fonction trigonométrique", code: `from math import sin, pi

for k in range(5):
    x = k * pi / 4
    print(round(x, 3), round(sin(x), 4))`, sortie: `0.0 0.0
0.785 0.7071
1.571 1.0
2.356 0.7071
3.142 0.0` }
  ],
  methodes: [
    { t: "Comment résoudre $\\cos x=a$ ou $\\sin x=a$ ?", h: R`
<p>Dessine le cercle et la droite verticale $x=a$ (pour $\cos$) ou horizontale $y=a$ (pour $\sin$). Les solutions sont les angles des points d'intersection : $\pm\alpha$ pour $\cos$, $\alpha$ et $\pi-\alpha$ pour $\sin$.</p>` },
    { t: "Comment étudier une fonction trigonométrique ?", h: R`
<ol><li>Réduire l'intervalle d'étude (périodicité, parité).</li><li>Dériver avec $(\sin u)'=u'\cos u$, $(\cos u)'=-u'\sin u$.</li><li>Étudier le signe de la dérivée en lisant le signe de $\sin$ ou $\cos$ sur le cercle ; tableau de variations, optimum.</li></ol>` },
    { t: "Comment utiliser $\\lim_{x\\to0}\\frac{\\sin x}x=1$ ?", h: R`
<p>Reconnaître un taux d'accroissement : $\frac{\sin x}{x}=\frac{\sin x-\sin0}{x-0}\to\sin'(0)=\cos0=1$. De même $\frac{\cos x-1}{x}\to\cos'(0)=0$.</p>` }
  ],
  exos: [
    { niv: 1, t: "Équations", enonce: R`<p>Résoudre sur $[-\pi;\pi]$ :</p><ol><li>$\cos x=\frac{\sqrt2}2$</li><li>$\cos x=-1$</li><li>$2\cos x+\sqrt3=0$</li><li>$\cos x=2$</li></ol>`,
      corrige: R`<ol><li>$x=\pm\frac\pi4$.</li><li>$x=\pi$ (et $-\pi$, qui est aussi dans l'intervalle fermé $[-\pi;\pi]$).</li><li>$\cos x=-\frac{\sqrt3}2$ : $x=\pm\frac{5\pi}6$.</li><li>Pas de solution ($\cos x\leq1$).</li></ol>` },
    { niv: 1, t: "Dérivées", enonce: R`<p>Dériver : $f(x)=\sin(2x)$ ; $g(x)=x\cos x$ ; $h(x)=\cos(x^2)$ ; $k(x)=\frac{\sin x}{x}$ sur $]0;+\infty[$.</p>`,
      corrige: R`<p>$f'(x)=2\cos(2x)$ ; $g'(x)=\cos x-x\sin x$ ; $h'(x)=-2x\sin(x^2)$ ; $k'(x)=\frac{x\cos x-\sin x}{x^2}$ (son signe est celui de $x\cos x-\sin x$, étudié au bac en Asie le 9 juin 2026).</p>` },
    { niv: 2, t: "Inéquations", enonce: R`<ol><li>Résoudre $\cos x\leq\frac12$ sur $[-\pi;\pi]$.</li><li>Résoudre $2\sin x-1\geq0$ sur $[0;2\pi]$.</li></ol>`,
      corrige: R`<ol><li>$\left[-\pi;-\frac\pi3\right]\cup\left[\frac\pi3;\pi\right]$.</li><li>$\sin x\geq\frac12$ : $\left[\frac\pi6;\frac{5\pi}6\right]$.</li></ol><p class="stylo">Contrôle : vérifié par un balayage numérique de l'intervalle.</p>` },
    { niv: 2, t: "Un rectangle optimal", enonce: R`<p>Reprendre l'exemple du cours : rectangle inscrit dans un demi-disque de rayon $R=3$. Exprimer l'aire en fonction de $\theta$ et trouver l'aire maximale.</p>`,
      corrige: R`<p>Largeur $2R\cos\theta=6\cos\theta$, hauteur $3\sin\theta$ : $A(\theta)=18\sin\theta\cos\theta$. Même étude : maximum en $\theta=\frac\pi4$, $A=18\times\frac12=9$ (soit $R^2$).</p>` },
    { niv: 3, t: "Étude de $f(x)=x+2\\cos x$ (type bac)", enonce: R`<p>Soit $f$ définie sur $[0;2\pi]$ par $f(x)=x+2\cos x$.</p><ol><li>Calculer $f'(x)$ et résoudre $f'(x)=0$ sur $[0;2\pi]$.</li><li>Étudier le signe de $f'$ et dresser le tableau de variations (valeurs exactes et approchées).</li><li>Montrer que $f(x)>0$ sur $[0;2\pi]$.</li><li>Déterminer l'équation de la tangente en $0$.</li></ol>`,
      corrige: R`<ol><li>$f'(x)=1-2\sin x$ ; $f'(x)=0\iff\sin x=\frac12\iff x=\frac\pi6$ ou $x=\frac{5\pi}6$.</li>
<li>$f'(x)\geq0\iff\sin x\leq\frac12$ : sur $\left[0;\frac\pi6\right]$ et $\left[\frac{5\pi}6;2\pi\right]$ ; $f'\leq0$ sur $\left[\frac\pi6;\frac{5\pi}6\right]$. $f(0)=2$ ; maximum local $f\left(\frac\pi6\right)=\frac\pi6+\sqrt3\approx2{,}256$ ; minimum local $f\left(\frac{5\pi}6\right)=\frac{5\pi}6-\sqrt3\approx0{,}886$ ; $f(2\pi)=2\pi+2\approx8{,}283$.</li>
<li>Le minimum de $f$ sur $[0;2\pi]$ est le plus petit de $f(0)=2$ et $f\left(\frac{5\pi}6\right)\approx0{,}886$ : il est strictement positif, donc $f>0$.</li>
<li>$f(0)=2$, $f'(0)=1$ : $y=x+2$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Asie, 9 juin 2026 (sujet 1), exercice 4", url: "https://www.apmep.fr/IMG/pdf/BAC_Specialite_Sujet_2026_J1_Asie_FK.pdf", h: R`$g(x)=x\cos x-\sin x$ sur $[0;2\pi]$ : $g'(x)=-x\sin x$, variations, signe ; puis $f(x)=\frac{\sin x}x$ : variations et limite en $0$ « en utilisant le taux d'accroissement de la fonction sinus en $0$ ».` },
    { ref: "Bac 2025, Amérique du Nord, 22 mai 2025 (sujet 2), exercice 4, partie A", url: "https://www.apmep.fr/IMG/pdf/Amerique_du_Nord_J2_spe_22_05_2025_DV_FK.pdf", h: R`$f(x)=\e^x\sin x$ sur $[0;\pi]$ : $f'(x)=\e^x(\sin x+\cos x)$, variations, inégalité $\e^x\sin x\geq x$ par convexité. La partie B calcule des intégrales par parties (chapitre 9).` }
  ],
  retenir: R`
[prop|Cercle]$M(\cos x;\sin x)$ ; $\cos^2x+\sin^2x=1$ ; $-1\leq\cos x,\sin x\leq1$ ; période $2\pi$ ; $\cos$ paire, $\sin$ impaire.[/]
[thm|Dérivées]$\sin'=\cos$ ; $\cos'=-\sin$ ; $(\sin u)'=u'\cos u$ ; $(\cos u)'=-u'\sin u$ ; $\lim_{x\to0}\frac{\sin x}x=1$.[/]
<p><b>Variations</b> : $\cos$ décroît sur $[0;\pi]$ de $1$ à $-1$ ; $\sin$ croît sur $\left[-\frac\pi2;\frac\pi2\right]$ de $-1$ à $1$.</p>
<p><b>Équations sur $[-\pi;\pi]$</b> : $\cos x=a$ ⟹ $\pm\alpha$ ; $\sin x=a$ ⟹ $\alpha$ et $\pi-\alpha$. Inéquations : lire sur le cercle.</p>
<p>Valeurs : $\cos\frac\pi3=\frac12$, $\cos\frac\pi4=\frac{\sqrt2}2$, $\cos\frac\pi6=\frac{\sqrt3}2$ (et l'inverse pour $\sin$).</p>
<p class="stylo">Calculatrice en radians. Un dessin du cercle évite d'oublier une solution.</p>`,
  qcm: [
    { q: R`$\sin'(x)=$`, c: ["$\\cos x$", "$-\\cos x$", "$-\\sin x$", "$\\sin x$"], r: 0, e: R`$\sin'=\cos$ et $\cos'=-\sin$.`, ref: "derivees" },
    { q: R`La dérivée de $x\mapsto\cos(3x)$ est :`, c: [R`$-\sin(3x)$`, R`$3\sin(3x)$`, R`$-3\sin(3x)$`, R`$3\cos(3x)$`], r: 2, e: R`$(\cos u)'=-u'\sin u$ avec $u'=3$.`, ref: "derivees" },
    { q: R`Sur $[-\pi;\pi]$, $\cos x=\frac12$ a pour solutions :`, c: [R`$\frac\pi3$ seulement`, R`$\frac\pi3$ et $-\frac\pi3$`, R`$\frac\pi6$ et $\frac{5\pi}6$`, R`$\frac\pi3$ et $\frac{2\pi}3$`], r: 1, e: R`Deux points du cercle ont pour abscisse $\frac12$ : angles $\pm\frac\pi3$.`, ref: "equations" },
    { q: R`Sur $[-\pi;\pi]$, $\sin x=\frac{\sqrt2}2$ a pour solutions :`, c: [R`$\pm\frac\pi4$`, R`$\frac\pi4$ et $\frac{3\pi}4$`, R`$\frac\pi4$ seulement`, R`$\frac\pi3$ et $\frac{2\pi}3$`], r: 1, e: R`$\sin(\pi-x)=\sin x$ : $\frac\pi4$ et $\pi-\frac\pi4$.`, ref: "equations" },
    { q: R`$\lim_{x\to0}\frac{\sin x}x=$`, c: ["$0$", "$1$", "$+\\infty$", "elle n'existe pas"], r: 1, e: R`C'est $\sin'(0)=\cos0=1$.`, ref: "derivees" },
    { q: R`$\cos$ est :`, c: ["paire et $\\pi$-périodique", "impaire et $2\\pi$-périodique", "paire et $2\\pi$-périodique", "ni paire ni impaire"], r: 2, e: R`$\cos(-x)=\cos x$ et $\cos(x+2\pi)=\cos x$.`, ref: "cercle" },
    { q: R`Sur $[0;\pi]$, la fonction $\cos$ est :`, c: ["croissante", "décroissante", "constante", "croissante puis décroissante"], r: 1, e: R`$\cos'=-\sin\leq0$ sur $[0;\pi]$.`, ref: "variations" },
    { q: R`L'ensemble des solutions de $\cos x\leq\frac12$ sur $[-\pi;\pi]$ est :`, c: [R`$\left[-\frac\pi3;\frac\pi3\right]$`, R`$\left[-\pi;-\frac\pi3\right]\cup\left[\frac\pi3;\pi\right]$`, R`$\left[\frac\pi3;\pi\right]$`, R`$\left[-\frac\pi6;\frac\pi6\right]$`], r: 1, e: R`Points du cercle à gauche de la droite $x=\frac12$.`, ref: "equations" },
    { q: R`La dérivée de $x\mapsto\cos^2x$ est :`, c: [R`$2\cos x$`, R`$-2\sin x\cos x$`, R`$2\sin x\cos x$`, R`$-\sin^2x$`], r: 1, e: R`$(u^2)'=2u'u$ avec $u=\cos$, $u'=-\sin$.`, ref: "derivees" },
    { q: R`$\cos^2x+\sin^2x=$`, c: ["$0$", "$1$", "$2$", "dépend de $x$"], r: 1, e: R`Pythagore dans le cercle de rayon $1$.`, ref: "cercle" },
    { q: R`L'aire $A(\theta)=2\sin\theta\cos\theta$ sur $\left[0;\frac\pi2\right]$ est maximale pour :`, c: [R`$\theta=0$`, R`$\theta=\frac\pi4$`, R`$\theta=\frac\pi3$`, R`$\theta=\frac\pi2$`], r: 1, e: R`$A'(\theta)=2(\cos^2\theta-\sin^2\theta)$ s'annule quand $\cos\theta=\sin\theta$.`, ref: "optimum" },
    { q: R`La tangente à la courbe de $\sin$ en $0$ a pour équation :`, c: [R`$y=0$`, R`$y=x$`, R`$y=1$`, R`$y=-x$`], r: 1, e: R`$\sin0=0$ et $\sin'(0)=\cos0=1$.`, ref: "variations" },
    { q: R`En mode radian, $\cos(\pi)=$`, c: ["$0$", "$1$", "$-1$", "$\\frac12$"], r: 2, e: R`Le point associé à $\pi$ est $(-1;0)$.`, ref: "cercle" }
  ],
  cartes: [
    [R`$\sin'$ et $\cos'$`, R`$\sin'=\cos$ ; $\cos'=-\sin$`],
    [R`$(\sin u)'$ et $(\cos u)'$`, R`$u'\cos u$ ; $-u'\sin u$`],
    [R`$\cos^2x+\sin^2x$`, R`$1$`],
    [R`Parité de $\cos$ et de $\sin$`, R`$\cos$ paire ; $\sin$ impaire.`],
    [R`Période de $\cos$ et $\sin$`, R`$2\pi$`],
    [R`$\cos\frac\pi3$, $\cos\frac\pi4$, $\cos\frac\pi6$`, R`$\frac12$ ; $\frac{\sqrt2}2$ ; $\frac{\sqrt3}2$`],
    [R`Solutions de $\cos x=a$ sur $[-\pi;\pi]$ ($|a|<1$)`, R`$\alpha$ et $-\alpha$, avec $\alpha\in]0;\pi[$, $\cos\alpha=a$.`],
    [R`Solutions de $\sin x=a$ sur $[-\pi;\pi]$`, R`$\alpha$ et $\pi-\alpha$ (si $a>0$).`],
    [R`$\lim_{x\to0}\frac{\sin x}x$`, R`$1$`],
    [R`$\sin(\pi-x)$ et $\cos(\pi-x)$`, R`$\sin x$ ; $-\cos x$`],
    [R`Variations de $\cos$ sur $[0;\pi]$`, R`Décroissante de $1$ à $-1$.`],
    [R`Tangente à $\sin$ en $0$`, R`$y=x$`]
  ]
};

/* Animation : le cercle tourne, la sinusoïde se déroule */
ANIMS.cercle = {
  titre: "Le cercle tourne, la courbe se déroule",
  vb: [360, 205],
  etapes: [
    { d: 4, l: R`Le point $M$ part de $I(1;0)$ et tourne. Sa hauteur est $\sin x$ (en rouge), son abscisse $\cos x$ (en vert). On reporte la hauteur à droite, en fonction de $x$.` },
    { d: 3.5, l: R`De $\frac\pi2$ à $\pi$ : $M$ redescend, $\sin x$ revient à $0$, $\cos x$ devient négatif.` },
    { d: 6, l: R`De $\pi$ à $2\pi$ : $\sin x$ devient négatif, atteint $-1$ en $\frac{3\pi}2$, puis revient à $0$. Un tour complet = une vague : $2\pi$ est la période.` },
    { d: 5, l: R`En reportant l'abscisse $\cos x$, on obtient la même vague, décalée de $\frac\pi2$ : $\cos x=\sin\left(x+\frac\pi2\right)$.` },
    { d: 4.5, l: R`On pose la pente de la courbe de $\sin$ à côté de $\cos$ : là où $\sin$ monte le plus vite ($x=0$), $\cos$ vaut $1$ ; au sommet de $\sin$, $\cos$ vaut $0$. C'est $\sin'=\cos$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, cx = 58, cy = 98, r = 44, gx = 118, L = 232, sc = 44, P = Math.PI;
    function GX(x) { return gx + x / (2 * P) * L; }
    function GY(y) { return cy - y * sc; }
    var x = k === 0 ? E(t) * P / 2 : k === 1 ? P / 2 + E(t) * P / 2 : k === 2 ? P + E(t) * P : 2 * P;
    S.px.cercle(cx, cy, r, "a-craie");
    S.px.seg(cx - r - 6, cy, cx + r + 6, cy, "g-axe"); S.px.seg(cx, cy - r - 6, cx, cy + r + 6, "g-axe");
    S.px.seg(gx, cy, gx + L + 4, cy, "g-axe"); S.px.seg(gx, cy - r - 8, gx, cy + r + 8, "g-axe");
    [[P / 2, "π/2"], [P, "π"], [3 * P / 2, "3π/2"], [2 * P, "2π"]].forEach(function (q) { S.px.seg(GX(q[0]), cy - 3, GX(q[0]), cy + 3, "g-axe"); S.px.txt(GX(q[0]), cy + 16, q[1], "", "middle", { "font-size": 11 }); });
    S.px.txt(gx - 4, GY(1) + 4, "1", "", "end", { "font-size": 11 }); S.px.txt(gx - 4, GY(-1) + 4, "−1", "", "end", { "font-size": 11 });
    function chemin(f, x1) { var d = ""; for (var i = 0; i <= 120; i++) { var u = x1 * i / 120; d += (i ? "L" : "M") + GX(u).toFixed(1) + " " + GY(f(u)).toFixed(1); } return d; }
    if (k >= 3) S.px.path(chemin(Math.cos, k === 3 ? E(t) * 2 * P : 2 * P), "g-c3", { "stroke-width": 2.2 });
    S.px.path(chemin(Math.sin, x), "g-c2", { "stroke-width": 2.6 });
    var a = k >= 3 ? (k === 3 ? E(t) * 2 * P : ANIM.l(0, P / 2, E(t))) : x;
    var mx = cx + r * Math.cos(a), my = cy - r * Math.sin(a);
    S.px.seg(cx, cy, mx, my, "g-c", { "stroke-width": 1.4 });
    S.px.seg(mx, cy, mx, my, "g-c2", { "stroke-width": 3 });
    S.px.seg(cx, cy, mx, cy, "g-c3", { "stroke-width": 3 });
    S.px.seg(mx, my, GX(a), GY(Math.sin(a)), "a-craie");
    S.px.cercle(mx, my, 4.5, "g-pt");
    S.px.cercle(GX(a), GY(Math.sin(a)), 4, "g-pt2");
    if (k >= 3) S.px.cercle(GX(a), GY(Math.cos(a)), 4, "g-pt", { style: "fill:var(--vert)" });
    S.px.txt(8, 20, "x = " + ANIM.nf(a, 2), "b");
    S.px.txt(8, 196, "sin x = " + ANIM.nf(Math.sin(a), 2), "r");
    S.px.txt(120, 196, "cos x = " + ANIM.nf(Math.cos(a), 2), "c3");
    if (k === 4) {
      var s = Math.cos(a), x0 = GX(a), y0 = GY(Math.sin(a)), dx = 26;
      S.px.seg(x0 - dx, y0 + s * dx * sc / (L / (2 * P)), x0 + dx, y0 - s * dx * sc / (L / (2 * P)), "g-c", { "stroke-width": 2 });
      S.px.txt(250, 196, "pente = " + ANIM.nf(s, 2), "b");
    }
  }
};

/* Animation : résoudre cos x = 1/2 et des inéquations sur le cercle */
ANIMS.trigEq = {
  titre: R`Résoudre $\cos x=\frac12$ sur le cercle`,
  vb: [370, 236],
  etapes: [
    { d: 4, l: R`Sur le cercle trigonométrique, le point $M$ associé au réel $x$ a pour abscisse $\cos x$ (en vert). Résoudre $\cos x=\frac12$, c'est chercher les points d'abscisse $\frac12$.` },
    { d: 4.5, l: R`La droite verticale d'abscisse $\frac12$ coupe le cercle en deux points : ceux de $\frac\pi3$ et de $-\frac\pi3$ (car $\cos\frac\pi3=\frac12$ et $\cos(-x)=\cos x$).` },
    { d: 5, l: R`Un tour de plus ($+2\pi$) ramène au même point. Sur $\R$, les solutions sont $\frac\pi3+2k\pi$ et $-\frac\pi3+2k\pi$, $k\in\Z$ ; sur $[-\pi;\pi]$, il n'en reste que deux.` },
    { d: 4.5, l: R`$\cos x\leq\frac12$ : les points <b>à gauche</b> de la droite. Sur $[-\pi;\pi]$ : $x\in\left[-\pi;-\frac\pi3\right]\cup\left[\frac\pi3;\pi\right]$.` },
    { d: 5, l: R`Avec le sinus, la droite est horizontale. $\sin x\geq\frac12$ : les points <b>au-dessus</b> de la droite d'ordonnée $\frac12$. Sur $[0;2\pi]$ : $x\in\left[\frac\pi6;\frac{5\pi}6\right]$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, nf = ANIM.nf, cx = 110, cy = 118, r = 88, PI = Math.PI;
    function pt(a) { return [cx + r * Math.cos(a), cy - r * Math.sin(a)]; }
    function arc(a1, a2, cls, at) { var n = Math.max(2, Math.ceil(Math.abs(a2 - a1) * 24)), d = ""; for (var i = 0; i <= n; i++) { var q = pt(a1 + (a2 - a1) * i / n); d += (i ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1); } return S.px.path(d, cls, ajoute({ fill: "none" }, at)); }
    function ajoute(a, b) { for (var c in b || {}) a[c] = b[c]; return a; }
    function lab(a, s, cls, d) { var q = [cx + (r + (d || 16)) * Math.cos(a), cy - (r + (d || 16)) * Math.sin(a) + 4]; S.px.txt(q[0], q[1], s, cls, Math.cos(a) > 0.2 ? "start" : Math.cos(a) < -0.2 ? "end" : "middle"); }
    S.px.seg(cx - r - 12, cy, cx + r + 12, cy, "g-axe");
    S.px.seg(cx, cy - r - 12, cx, cy + r + 12, "g-axe");
    S.px.cercle(cx, cy, r, "", { style: "fill:none;stroke:var(--encre2);stroke-width:1.4" });
    S.px.txt(cx + r + 4, cy + 14, "1", "", "start", { "font-size": 11 });
    S.px.txt(cx - r - 4, cy + 14, "−1", "", "end", { "font-size": 11 });
    var px0 = 210, pw = 158;
    if (k === 0) {
      var a = 2 * PI * E(t), M = pt(a);
      S.px.seg(M[0], M[1], M[0], cy, "a-craie");
      S.px.seg(cx, cy, M[0], cy, "g-c3", { "stroke-width": 4 });
      S.px.seg(cx, cy, M[0], M[1], "a-branche");
      S.px.cercle(M[0], M[1], 5, "g-pt");
      S.px.txt(M[0] + (Math.cos(a) >= 0 ? 8 : -8), M[1] - 6, "M", "b", Math.cos(a) >= 0 ? "start" : "end");
      S.px.math(px0, 50, pw, 34, "$x\\approx" + nf(a, 2).replace(",", "{,}") + "$");
      S.px.math(px0, 90, pw, 34, "$\\cos x\\approx" + nf(Math.cos(a), 2).replace(",", "{,}") + "$");
      return;
    }
    if (k <= 3) {
      var o = k === 1 ? E(p(t, 0, 0.4)) : 1, xv = cx + r / 2;
      S.px.seg(xv, cy - r - 14, xv, cy + r + 14, "g-as", { opacity: o });
      S.px.txt(xv - 5, cy + r + 12, "x = 1/2", "r", "end", { opacity: o, "font-size": 12 });
      if (k === 3) { var f3 = E(p(t, 0, 0.7)); arc(PI / 3, PI / 3 + f3 * 2 * PI / 3, "g-c2", { "stroke-width": 6, opacity: 0.75 }); arc(-PI, -PI + f3 * 2 * PI / 3, "g-c2", { "stroke-width": 6, opacity: 0.75 }); }
      var o2 = k === 1 ? E(p(t, 0.35, 0.7)) : 1;
      [PI / 3, -PI / 3].forEach(function (b) { var q = pt(b); S.px.seg(cx, cy, q[0], q[1], "a-branche", { opacity: o2 }); S.px.cercle(q[0], q[1], 5.5, "g-pt2", { opacity: o2 }); });
      if (o2 > 0.01) { lab(PI / 3, "π/3", "r"); lab(-PI / 3, "−π/3", "r"); }
      if (k === 1) {
        S.px.math(px0, 46, pw, 34, R`$\cos x=\frac12$`, { opacity: o2 });
        S.px.math(px0, 88, pw, 34, R`$x=\frac\pi3$ ou $x=-\frac\pi3$`, { opacity: o2 });
      }
      if (k === 2) {
        var b2 = PI / 3 + 2 * PI * E(p(t, 0, 0.75)), M2 = pt(b2);
        arc(PI / 3, Math.min(b2, PI / 3 + 2 * PI - 0.001), "g-c", { "stroke-width": 3, opacity: 0.55 });
        S.px.cercle(M2[0], M2[1], 5, "g-pt");
        S.px.math(px0, 40, pw, 34, "$x=\\frac\\pi3+" + nf((b2 - PI / 3) / PI, 2).replace(",", "{,}") + "\\pi$");
        if (t > 0.75) S.px.math(px0, 84, pw, 60, R`$x=\pm\frac\pi3+2k\pi$`, { opacity: E(p(t, 0.75, 0.95)) });
      }
      if (k === 3) {
        S.px.math(px0, 40, pw, 34, R`$\cos x\leq\frac12$`);
        S.px.math(px0, 82, pw, 44, R`$\left[-\pi;-\frac\pi3\right]\cup\left[\frac\pi3;\pi\right]$`, { opacity: E(p(t, 0.6, 0.9)) });
      }
      return;
    }
    var o5 = E(p(t, 0, 0.35)), yh = cy - r / 2, f5 = E(p(t, 0.35, 0.8));
    S.px.seg(cx - r - 14, yh, cx + r + 14, yh, "g-as", { opacity: o5, style: "stroke:var(--vert)" });
    arc(PI / 6, PI / 6 + f5 * 2 * PI / 3, "g-c3", { "stroke-width": 6, opacity: 0.8 });
    [PI / 6, 5 * PI / 6].forEach(function (b) { var q = pt(b); S.px.cercle(q[0], q[1], 5.5, "g-pt", { opacity: o5 }); });
    if (o5 > 0.01) { var q6 = pt(PI / 6), q56 = pt(5 * PI / 6); S.px.txt(q6[0] - 6, q6[1] + 17, "π/6", "c3", "end", { opacity: o5 }); S.px.txt(q56[0] + 6, q56[1] + 17, "5π/6", "c3", "start", { opacity: o5 }); }
    S.px.math(px0, 40, pw, 34, R`$\sin x\geq\frac12$`, { opacity: o5 });
    S.px.math(px0, 82, pw, 44, R`$\left[\frac\pi6;\frac{5\pi}6\right]$`, { opacity: E(p(t, 0.7, 0.95)) });
  }
};
