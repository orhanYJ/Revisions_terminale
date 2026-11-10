/* ---------- Chapitre 12 : représentations paramétriques et équations cartésiennes ---------- */
var CH12 = {
  id: "ch12", num: 12, statut: "ok", partie: "Algèbre et géométrie", titre: "Représentations paramétriques et équations cartésiennes", court: "Droites et plans repérés",
  sous: "Dans un repère orthonormé, la géométrie devient du calcul : une droite se parcourt avec un paramètre, un plan tient en une équation.",
  resume: "Représentation paramétrique d'une droite, équation cartésienne d'un plan, intersections, projetés, systèmes.",
  essentiel: [
    R`La droite passant par $A(x_A;y_A;z_A)$ et dirigée par $\vec u(a;b;c)$ a pour <b>représentation paramétrique</b> $\begin{cases}x=x_A+at\\y=y_A+bt\\z=z_A+ct\end{cases}$, $t\in\R$. Chaque valeur de $t$ donne un point.`,
    R`Un plan de vecteur normal $\vec n(a;b;c)$ a une <b>équation cartésienne</b> $ax+by+cz+d=0$. Réciproquement, une telle équation (avec $a$, $b$, $c$ non tous nuls) est celle d'un plan normal à $\vec n(a;b;c)$.`,
    R`<b>Intersection droite-plan</b> : on remplace $x$, $y$, $z$ par la représentation paramétrique dans l'équation du plan ; une solution $t$ : sécants ; aucune : parallèle strictement ; tout $t$ convient : droite incluse.`,
    R`<b>Projeté orthogonal</b> de $M$ sur le plan $ax+by+cz+d=0$ : c'est l'intersection du plan avec la droite passant par $M$ et dirigée par $\vec n(a;b;c)$.`,
    R`Alignement, coplanarité, base, intersection de deux droites : on traduit le problème par un <b>système</b> d'équations linéaires, qu'on résout par substitution.`
  ],
  attendus: [
    R`Déterminer une représentation paramétrique d'une droite ; reconnaître une droite donnée par une représentation paramétrique.`,
    R`Déterminer l'équation cartésienne d'un plan dont on connaît un vecteur normal et un point ; reconnaître un plan donné par une équation cartésienne et préciser un vecteur normal.`,
    R`Déterminer les coordonnées du projeté orthogonal d'un point sur un plan donné par une équation cartésienne, ou sur une droite donnée par un point et un vecteur directeur.`,
    R`Traduire par un système d'équations linéaires : décider si trois vecteurs forment une base, déterminer les coordonnées d'un vecteur dans une base, étudier une configuration (alignement, colinéarité, parallélisme, coplanarité, intersection et orthogonalité de droites ou de plans) ; résoudre dans les cas simples et interpréter.`,
    R`Démonstration exigible : équation cartésienne du plan normal au vecteur $\vec n$ et passant par le point $A$ <span class="tag bo">BO</span>.`
  ],
  premiere: R`
<ul><li><b>Droite du plan</b> : équation cartésienne $ax+by+c=0$, de vecteur directeur $\vec u(-b;a)$ et de vecteur normal $\vec n(a;b)$.</li>
<li><b>Systèmes de deux équations à deux inconnues</b> : substitution ou combinaison.</li>
<li><b>Chapitres 10 et 11</b> : caractérisations $\vec{AM}=t\vec u$ (droite), $\vec{AM}\cdot\vec n=0$ (plan), produit scalaire $xx'+yy'+zz'$ en repère orthonormé.</li></ul>
[piege|Une équation ne suffit plus pour une droite]Dans l'espace, $ax+by+cz+d=0$ décrit un <b>plan</b>, pas une droite. Une droite de l'espace se décrit par une représentation paramétrique (ou par deux équations : l'intersection de deux plans).[/]`,
  cours: [
    { id: "parametrique", titre: "Représentation paramétrique d'une droite", html: R`
<p>Dans tout le chapitre, l'espace est muni d'un repère orthonormé $(O;\vec i,\vec j,\vec k)$.</p>
[thm|Représentation paramétrique]Soit $(d)$ la droite passant par $A(x_A;y_A;z_A)$ et de vecteur directeur $\vec u(a;b;c)$ (non nul). $M(x;y;z)\in(d)$ si et seulement s'il existe un réel $t$ tel que
$$\begin{cases}x=x_A+at\\y=y_A+bt\\z=z_A+ct\end{cases}$$
C'est la traduction en coordonnées de $\vec{AM}=t\vec u$.[/]
[ex|Écrire une représentation paramétrique]$A(1;-2;3)$, $\vec u(2;1;-1)$ : $(d):\begin{cases}x=1+2t\\y=-2+t\\z=3-t\end{cases}$, $t\in\R$. Pour $t=0$ on retrouve $A$ ; pour $t=2$ on obtient $B(5;0;1)$.[/]
[ex|Le point appartient-il à la droite ?]$C(-3;-4;5)$ : la 1<sup>re</sup> ligne donne $1+2t=-3$, soit $t=-2$. On vérifie : $y=-2+(-2)=-4$ ✓ et $z=3-(-2)=5$ ✓. Donc $C\in(d)$. Pour $E(3;0;2)$ : $t=1$ d'après $x$, mais alors $y=-1\neq0$ : $E\notin(d)$.[/]
[prop|Lire une représentation paramétrique]Les <b>constantes</b> donnent un point (pour $t=0$), les <b>coefficients de $t$</b> donnent un vecteur directeur. Une droite a une infinité de représentations paramétriques : on peut changer de point et remplacer $\vec u$ par $k\vec u$ ($k\neq0$).[/]
[ex|Deux écritures de la même droite]$\begin{cases}x=5+4s\\y=2s\\z=1-2s\end{cases}$ représente aussi la droite $(d)$ : le point $(5;0;1)$ est $B\in(d)$ et $(4;2;-2)=2\vec u$.[/]
<p><b>Segment, demi-droite.</b> Avec $A$ et $B$, $M=A+t\vec{AB}$ décrit le segment $[AB]$ quand $t\in[0;1]$, la demi-droite $[AB)$ quand $t\geq0$.</p>` },
    { id: "cartesienne", titre: "Équation cartésienne d'un plan", html: R`
[thm|Équation cartésienne d'un plan]<ul><li>Le plan passant par $A$ et de vecteur normal $\vec n(a;b;c)$ a une équation de la forme $ax+by+cz+d=0$.</li><li>Réciproquement, si $a$, $b$, $c$ ne sont pas tous nuls, l'ensemble des points $M(x;y;z)$ tels que $ax+by+cz+d=0$ est un plan de vecteur normal $\vec n(a;b;c)$.</li></ul>[/]
[ex|Plan défini par un point et un vecteur normal]Plan passant par $A(1;2;-1)$ et normal à $\vec n(2;-1;3)$ : son équation est $2x-y+3z+d=0$. Comme $A$ est dans le plan : $2-2-3+d=0$, donc $d=3$. Équation : $2x-y+3z+3=0$.[/]
[ex|Lire un vecteur normal]Le plan $x-2z+5=0$ a pour vecteur normal $\vec n(1;0;-2)$ (le coefficient de $y$ est nul). Le plan $z=4$ est normal à $\vec k$ : il est parallèle au plan $(xOy)$, d'équation $z=0$.[/]
[meth|Équation du plan passant par trois points $A$, $B$, $C$]<ol><li>Vérifie que $A$, $B$, $C$ ne sont pas alignés.</li><li>Cherche $\vec n(a;b;c)$ tel que $\vec n\cdot\vec{AB}=0$ et $\vec n\cdot\vec{AC}=0$ : deux équations à trois inconnues, on fixe une inconnue (par exemple $c=1$, ou une valeur qui évite les fractions).</li><li>Écris $ax+by+cz+d=0$ et trouve $d$ avec $A$. Vérifie avec $B$ et $C$.</li></ol>[/]
[ex|Le plan qui coupe les trois axes]$A(1;0;0)$, $B(0;2;0)$, $C(0;0;3)$. $\vec{AB}(-1;2;0)$, $\vec{AC}(-1;0;3)$. Les conditions $-a+2b=0$ et $-a+3c=0$ donnent, avec $a=6$ : $b=3$, $c=2$. Équation $6x+3y+2z+d=0$ avec $A$ : $d=-6$. Plan : $6x+3y+2z-6=0$. Contrôle : $B$ donne $6-6=0$ ✓, $C$ donne $6-6=0$ ✓.[/]
[ex|Plan médiateur en équation]$A(1;0;2)$, $B(3;4;0)$ : milieu $I(2;2;1)$, $\vec{AB}(2;4;-2)$, que l'on peut remplacer par $(1;2;-1)$. Plan médiateur : $x+2y-z+d=0$ avec $I$ : $2+4-1+d=0$, $d=-5$. Équation : $x+2y-z-5=0$.[/]` },
    { id: "positions", titre: "Positions relatives en coordonnées", html: R`
<div class="tab-wrap"><table><tr><th>Objets</th><th>Test</th><th>Conclusion</th></tr>
<tr><td>Deux plans de normaux $\vec n$, $\vec n'$</td><td>$\vec n$, $\vec n'$ colinéaires ?</td><td>oui : parallèles (confondus si un point commun) ; non : sécants selon une droite. Perpendiculaires si $\vec n\cdot\vec n'=0$.</td></tr>
<tr><td>Droite $(A;\vec u)$, plan de normal $\vec n$</td><td>$\vec u\cdot\vec n$</td><td>$\neq0$ : sécants (en un point) ; $=0$ : parallèles, et incluse si $A$ est dans le plan. Orthogonale au plan si $\vec u$ et $\vec n$ colinéaires.</td></tr>
<tr><td>Deux droites $(A;\vec u)$, $(B;\vec v)$</td><td>$\vec u$, $\vec v$ colinéaires ?</td><td>oui : parallèles (confondues si $A$ est sur l'autre) ; non : on résout le système ⟹ sécantes (une solution) ou non coplanaires (aucune).</td></tr></table></div>
[ex|Deux plans]$\mathcal P:2x-y+z-1=0$ et $\mathcal Q:-4x+2y-2z+7=0$ : $\vec n'(-4;2;-2)=-2\vec n$, normaux colinéaires ; les plans sont parallèles. Ils ne sont pas confondus : $(0;0;1)\in\mathcal P$ mais $-2+7\neq0$. Avec $\mathcal R:x+y-z=0$ : $\vec n\cdot\vec n''=2-1-1=0$, donc $\mathcal P$ et $\mathcal R$ sont perpendiculaires.[/]
[ex|Une droite et un plan]$(d):\begin{cases}x=1+2t\\y=-2+t\\z=3-t\end{cases}$ et $\mathcal P:x-y+z-6=0$. $\vec u(2;1;-1)$, $\vec n(1;-1;1)$ : $\vec u\cdot\vec n=2-1-1=0$, donc $(d)$ est parallèle à $\mathcal P$. Le point $A(1;-2;3)$ vérifie $1+2+3-6=0$ : il est dans $\mathcal P$, donc $(d)$ est <b>incluse</b> dans $\mathcal P$.[/]` },
    { id: "intersections", titre: "Intersections : droite et plan, deux droites", html: R`
<div data-anim="droitePlan"></div>
[meth|Intersection d'une droite et d'un plan]On remplace $x$, $y$, $z$ de la représentation paramétrique dans l'équation du plan : on obtient une équation du premier degré en $t$.
<ul><li>une unique solution $t_0$ : la droite et le plan sont <b>sécants</b> au point de paramètre $t_0$ ;</li><li>une équation impossible ($0t=5$) : <b>parallèles</b>, sans point commun ;</li><li>une équation toujours vraie ($0t=0$) : la droite est <b>incluse</b> dans le plan.</li></ul>[/]
[ex|Une droite qui traverse un plan]$\mathcal P:x+y+z-3=0$ et $(d):\begin{cases}x=t\\y=2-t\\z=-1+2t\end{cases}$. On remplace : $t+(2-t)+(-1+2t)-3=0$, soit $2t-2=0$, $t=1$. Point d'intersection : $I(1;1;1)$. Contrôle : $1+1+1-3=0$ ✓.[/]
[meth|Intersection de deux droites]On écrit les deux représentations avec <b>deux paramètres différents</b> ($t$ et $s$) et on résout le système de trois équations à deux inconnues : on trouve $t$ et $s$ avec deux équations, la troisième décide.[/]
[ex|Sécantes ou non coplanaires ?]$(d_1):\begin{cases}x=1+t\\y=2t\\z=3-t\end{cases}$ et $(d_2):\begin{cases}x=2+s\\y=1-s\\z=s\end{cases}$. Vecteurs $(1;2;-1)$ et $(1;-1;1)$ non colinéaires. Système : $1+t=2+s$ et $2t=1-s$. De la première, $s=t-1$ ; dans la seconde, $2t=2-t$, donc $t=\frac23$, $s=-\frac13$. Troisième équation : $3-t=\frac73$ et $s=-\frac13$ : $\frac73\neq-\frac13$. Pas de solution : les droites ne sont <b>pas coplanaires</b>.[/]
[ex|Avec un point commun]Remplaçons $(d_2)$ par $(d_3):\begin{cases}x=2+s\\y=2-s\\z=2+s\end{cases}$. $1+t=2+s$ et $2t=2-s$ donnent $s=t-1$ puis $2t=3-t$, $t=1$, $s=0$. Troisième : $3-1=2$ et $2+0=2$ ✓. Les droites sont sécantes en $(2;2;2)$.[/]
<p><span class="tag hp">Pour aller plus loin</span> <b>Intersection de deux plans sécants</b> : on pose $z=t$ (si possible) et on exprime $x$ et $y$ en fonction de $t$ avec les deux équations : on obtient une représentation paramétrique de la droite d'intersection. Exemple : $x+y-z=0$ et $x-y+z-2=0$ ; en additionnant, $2x=2$, $x=1$, puis $y=z-1$ : la droite $x=1$, $y=-1+t$, $z=t$. Approfondissement du programme.</p>` },
    { id: "projections", titre: "Projeté orthogonal et distance en coordonnées", html: R`
[meth|Projeté orthogonal de $M$ sur le plan $\mathcal P:ax+by+cz+d=0$]<ol><li>La droite $\Delta$ passant par $M$ et orthogonale à $\mathcal P$ est dirigée par $\vec n(a;b;c)$ : $x=x_M+at$, $y=y_M+bt$, $z=z_M+ct$.</li><li>Son intersection avec $\mathcal P$ est le projeté $H$ : on remplace et on résout en $t$.</li><li>Distance de $M$ au plan : $MH=|t|\times\|\vec n\|$.</li></ol>[/]
[ex|Un projeté sur un plan]$M(4;-1;3)$ et $\mathcal P:2x-y+2z-3=0$, $\vec n(2;-1;2)$, $\|\vec n\|=3$. $\Delta:x=4+2t$, $y=-1-t$, $z=3+2t$. On remplace : $2(4+2t)-(-1-t)+2(3+2t)-3=0$, soit $12+9t=0$, $t=-\frac43$. $H\left(\frac43;\frac13;\frac13\right)$ et $MH=\frac43\times3=4$.[/]
<p><span class="tag hp">Pour aller plus loin</span> En faisant ce calcul en général, $t=-\frac{ax_M+by_M+cz_M+d}{a^2+b^2+c^2}$, d'où la formule
$$d(M;\mathcal P)=\frac{|ax_M+by_M+cz_M+d|}{\sqrt{a^2+b^2+c^2}}.$$
Elle n'est pas au programme : au bac, on attend la méthode du projeté (mais la formule permet de vérifier). Ici : $\frac{|8+1+6-3|}{3}=4$ ✓.</p>
[meth|Projeté orthogonal de $M$ sur la droite $(A;\vec u)$]$H=A+t\vec u$ avec $\vec{HM}\cdot\vec u=0$. En coordonnées : on écrit $\vec{HM}$ en fonction de $t$, on développe le produit scalaire, on résout.[/]
[ex|Un projeté sur une droite]$(d):x=1+t$, $y=1+t$, $z=t$ (point $A(1;1;0)$, $\vec u(1;1;1)$) et $M(3;1;4)$. $\vec{HM}(2-t;-t;4-t)$ ; $\vec{HM}\cdot\vec u=6-3t=0$, $t=2$. $H(3;3;2)$, $\vec{HM}(0;-2;2)$, distance $MH=2\sqrt2$.[/]` },
    { id: "systemes", titre: "Traduire un problème par un système", html: R`
<p>Le programme demande de traduire des questions géométriques en <b>systèmes linéaires</b>, puis de les résoudre dans les cas simples et d'interpréter. Le principe : on écrit la relation vectorielle cherchée, coordonnée par coordonnée.</p>
[ex|Trois vecteurs forment-ils une base ?]$\vec u(1;2;0)$, $\vec v(0;1;1)$, $\vec w(1;0;-2)$. On cherche $\alpha$, $\beta$ avec $\vec w=\alpha\vec u+\beta\vec v$ : $\begin{cases}1=\alpha\\0=2\alpha+\beta\\-2=\beta\end{cases}$. On trouve $\alpha=1$, $\beta=-2$, et la deuxième ligne est vérifiée ($2-2=0$). Donc $\vec w=\vec u-2\vec v$ : les vecteurs sont <b>coplanaires</b>, ils ne forment pas une base.[/]
[ex|Coordonnées dans une base]Avec $\vec u(1;2;0)$, $\vec v(0;1;1)$, $\vec k(0;0;1)$, qui forment une base (vérifie-le), cherchons les coordonnées de $\vec t(3;4;1)$ : $\alpha\vec u+\beta\vec v+\gamma\vec k=(\alpha;2\alpha+\beta;\beta+\gamma)=(3;4;1)$. D'où $\alpha=3$, $\beta=4-6=-2$, $\gamma=1+2=3$. Donc $\vec t=3\vec u-2\vec v+3\vec k$.[/]
[ex|Coplanarité avec un paramètre]Pour quelle valeur de $k$ le point $D_k(0;0;k)$ est-il dans le plan $x-y+4z-5=0$ ? $4k-5=0$, $k=\frac54$. Avec une équation de plan, une coplanarité se teste en une ligne.[/]
[meth|Résoudre un système de trois équations]<ol><li>Isole une inconnue dans l'équation la plus simple.</li><li>Remplace dans les deux autres : tu obtiens deux équations à deux inconnues.</li><li>Résous, remonte, puis <b>vérifie dans les trois équations</b>.</li><li>Interprète : une solution, aucune, ou une infinité (une inconnue reste libre).</li></ol>[/]
<p><span class="tag hp">Pour aller plus loin</span> <b>Sphère</b> de centre $\Omega(a;b;c)$ et de rayon $r$ : $(x-a)^2+(y-b)^2+(z-c)^2=r^2$. Pour couper une sphère par une droite, on remplace la représentation paramétrique : on obtient une équation du second degré en $t$ (0, 1 ou 2 points communs). Approfondissement non exigible.</p>` }
  ],
  pieges: [
    { t: "Normal ou directeur ?", h: R`Dans $ax+by+cz+d=0$, $(a;b;c)$ est un vecteur <b>normal</b> au plan. Dans une représentation paramétrique, les coefficients de $t$ forment un vecteur <b>directeur</b> de la droite. Ne les échange pas.` },
    { t: "Le même nom pour deux paramètres", h: R`Pour couper deux droites, appelle les paramètres $t$ et $s$. Avec la même lettre, tu imposes au point d'être atteint au « même instant » sur les deux droites, ce qui est faux en général.` },
    { t: "Une représentation paramétrique n'est pas unique", h: R`Deux représentations différentes peuvent décrire la même droite. Pour comparer, vérifie qu'un point de l'une est sur l'autre et que les vecteurs sont colinéaires.` },
    { t: "Interpréter $0t=0$ et $0t=5$", h: R`$0t=0$ : la droite est incluse dans le plan (une infinité de points communs). $0t=5$ : aucune solution, la droite est strictement parallèle au plan.` },
    { t: "Oublier la troisième équation", h: R`Avec deux paramètres et trois équations, deux équations donnent $t$ et $s$ ; la troisième doit être <b>vérifiée</b>. C'est elle qui sépare « sécantes » et « non coplanaires ».` },
    { t: "Le projeté donné par l'énoncé", h: R`Pour vérifier que $H$ est le projeté de $M$ sur $\mathcal P$ : $H\in\mathcal P$ <b>et</b> $\vec{MH}$ colinéaire à $\vec n$. Une seule des deux conditions ne suffit pas.` }
  ],
  demos: [
    { bo: true, t: "Équation cartésienne du plan normal à $\\vec n$ passant par $A$", h: R`
<p>Soit $\vec n(a;b;c)$ un vecteur non nul et $A(x_A;y_A;z_A)$. D'après le chapitre 11, le plan $\mathcal P$ passant par $A$ et normal à $\vec n$ est l'ensemble des points $M$ tels que $\vec{AM}\cdot\vec n=0$.</p>
<p><b>Sens direct.</b> Le repère étant orthonormé, avec $\vec{AM}(x-x_A;y-y_A;z-z_A)$ :
$$\vec{AM}\cdot\vec n=0\iff a(x-x_A)+b(y-y_A)+c(z-z_A)=0\iff ax+by+cz+d=0,$$
en posant $d=-ax_A-by_A-cz_A$. Le plan a donc une équation de la forme annoncée.</p>
<p><b>Réciproque.</b> Soit $a$, $b$, $c$ non tous nuls et $d$ un réel. Supposons par exemple $a\neq0$ : le point $A\left(-\frac da;0;0\right)$ vérifie l'équation. Pour tout point $M(x;y;z)$ :
$$ax+by+cz+d=a\left(x+\frac da\right)+by+cz=\vec n\cdot\vec{AM}.$$
Donc $ax+by+cz+d=0\iff\vec{AM}\cdot\vec n=0$ : l'ensemble est le plan passant par $A$ et normal à $\vec n(a;b;c)$. (Si $a=0$, on fait de même avec $b$ ou $c$.) CQFD.</p>` },
    { bo: false, t: "Représentation paramétrique : pourquoi ça marche", h: R`
<p>$M\in(d)\iff\vec{AM}$ et $\vec u$ sont colinéaires $\iff$ il existe $t\in\R$ tel que $\vec{AM}=t\vec u$ (car $\vec u\neq\vec 0$). En coordonnées, $\vec{AM}(x-x_A;y-y_A;z-z_A)=t(a;b;c)$ équivaut aux trois égalités $x=x_A+at$, $y=y_A+bt$, $z=z_A+ct$.</p>` },
    { bo: false, t: "Une droite est parallèle à un plan si et seulement si $\\vec u\\cdot\\vec n=0$", h: R`
<p>Soit $(d)$ dirigée par $\vec u$ et $\mathcal P$ normal à $\vec n$. Si $\vec u\cdot\vec n=0$, $\vec u$ est orthogonal à $\vec n$, donc dans la direction de $\mathcal P$ (la direction d'un plan est exactement l'ensemble des vecteurs orthogonaux à un vecteur normal) : $(d)$ est parallèle à $\mathcal P$.</p>
<p>Si $\vec u\cdot\vec n\neq0$, en remplaçant la représentation paramétrique dans l'équation $ax+by+cz+d=0$, on obtient $(\vec u\cdot\vec n)\,t+(ax_A+by_A+cz_A+d)=0$, qui a une unique solution : $(d)$ et $\mathcal P$ sont sécants.</p>` }
  ],
  algos: [
    { bo: false, t: "Intersection d'une droite et d'un plan", code: `from fractions import Fraction as Fr

def intersection(A, u, plan):
    a, b, c, d = plan                  # plan : ax + by + cz + d = 0
    coef = a*u[0] + b*u[1] + c*u[2]    # u . n
    cst = a*A[0] + b*A[1] + c*A[2] + d
    if coef == 0:
        return "incluse" if cst == 0 else "parallèle, aucun point commun"
    t = Fr(-cst, coef)
    return [A[i] + t*u[i] for i in range(3)]

print(intersection((0, 2, -1), (1, -1, 2), (1, 1, 1, -3)))
print(intersection((1, -2, 3), (2, 1, -1), (1, -1, 1, -6)))
print(intersection((0, 0, 0), (1, -1, 0), (1, 1, 1, -3)))`, sortie: `[Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)]
incluse
parallèle, aucun point commun`,
      apres: R`<p>Les trois cas de la partie 4 : sécants en $I(1;1;1)$, droite incluse, droite strictement parallèle.</p>` },
    { bo: false, t: "Projeté orthogonal sur un plan et distance", code: `from fractions import Fraction as Fr
from math import sqrt

def projete_plan(M, plan):
    a, b, c, d = plan
    t = Fr(-(a*M[0] + b*M[1] + c*M[2] + d), a*a + b*b + c*c)
    H = [M[0] + t*a, M[1] + t*b, M[2] + t*c]
    dist = abs(t) * sqrt(a*a + b*b + c*c)
    return H, dist

H, dist = projete_plan((4, -1, 3), (2, -1, 2, -3))
print(H, dist)`, sortie: `[Fraction(4, 3), Fraction(1, 3), Fraction(1, 3)] 4.0` },
    { bo: false, t: "Un point appartient-il à une droite ?", code: `def sur_droite(M, A, u):
    t = None
    for i in range(3):
        if u[i] != 0:
            t = (M[i] - A[i]) / u[i]   # paramètre lu sur une coordonnée
            break
    return all(abs(A[i] + t*u[i] - M[i]) < 1e-12 for i in range(3))

A, u = (1, -2, 3), (2, 1, -1)
print(sur_droite((-3, -4, 5), A, u), sur_droite((3, 0, 2), A, u))`, sortie: `True False` }
  ],
  methodes: [
    { t: "Déterminer une représentation paramétrique", h: R`
<p>Il faut un point et un vecteur directeur. Droite $(AB)$ : point $A$, vecteur $\vec{AB}$. Droite passant par $M$ et orthogonale au plan $ax+by+cz+d=0$ : point $M$, vecteur $\vec n(a;b;c)$. Droite parallèle à $(d)$ : même vecteur directeur.</p>` },
    { t: "Déterminer une équation cartésienne de plan", h: R`
<ul><li>Point $A$ + vecteur normal $\vec n$ : $ax+by+cz+d=0$, puis $d$ avec $A$.</li><li>Trois points : vecteur normal par le système $\vec n\cdot\vec{AB}=0$, $\vec n\cdot\vec{AC}=0$.</li><li>Plan parallèle à un plan donné : même vecteur normal.</li><li>Plan médiateur de $[AB]$ : normal à $\vec{AB}$, passant par le milieu.</li></ul>
<p>Si l'énoncé propose l'équation : vérifie que les points donnés la satisfont et que $\vec n$ est orthogonal à deux vecteurs non colinéaires du plan (ou simplement que trois points non alignés la vérifient).</p>` },
    { t: "Étudier la position de deux droites", h: R`
<ol><li>Vecteurs directeurs colinéaires ? Oui : parallèles (confondues ou non, tester un point).</li><li>Sinon, système en $t$ et $s$ : une solution ⟹ sécantes (calcule le point) ; aucune ⟹ non coplanaires.</li><li>Orthogonales si $\vec u\cdot\vec v=0$ (qu'elles soient sécantes ou non).</li></ol>` },
    { t: "Calculer un projeté orthogonal", h: R`
<p><b>Sur un plan</b> : droite $(M;\vec n)$, on remplace dans l'équation, on trouve $t$, puis $H$ ; distance $|t|\,\|\vec n\|$. <b>Sur une droite</b> : $H=A+t\vec u$ et $\vec{HM}\cdot\vec u=0$. Termine en vérifiant : $H$ dans le plan (sur la droite) et $\vec{MH}$ dans la bonne direction.</p>` }
  ],
  exos: [
    { niv: 1, t: "Lire et écrire une représentation paramétrique", enonce: R`<p>Repère orthonormé. $A(2;-1;0)$, $B(4;0;-3)$.</p><ol><li>Donner une représentation paramétrique de la droite $(AB)$.</li><li>Le point $C(8;2;-9)$ appartient-il à $(AB)$ ? Et $D(0;-2;4)$ ?</li><li>Donner un point et un vecteur directeur de la droite $(\delta):x=3-t$, $y=5$, $z=2t$, $t\in\R$.</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(2;1;-3)$ : $x=2+2t$, $y=-1+t$, $z=-3t$, $t\in\R$.</li><li>$C$ : $2+2t=8$ donne $t=3$ ; $y=2$ ✓, $z=-9$ ✓. $C\in(AB)$. $D$ : $t=-1$ d'après $x$ ; $y=-2$ ✓ mais $z=3\neq4$ : $D\notin(AB)$.</li><li>Point $(3;5;0)$ (pour $t=0$), vecteur directeur $(-1;0;2)$.</li></ol>` },
    { niv: 1, t: "Équations de plans", enonce: R`<p>Repère orthonormé.</p><ol><li>Équation du plan $\mathcal P$ passant par $A(3;0;-2)$ et de vecteur normal $\vec n(1;4;-1)$.</li><li>Le point $B(1;1;0)$ est-il dans $\mathcal P$ ?</li><li>Équation du plan $\mathcal Q$ parallèle à $\mathcal P$ passant par l'origine.</li><li>Un vecteur normal au plan $3y-z+1=0$ ? Ce plan est-il perpendiculaire à $\mathcal P$ ?</li></ol>`,
      corrige: R`<ol><li>$x+4y-z+d=0$ avec $A$ : $3+0+2+d=0$, $d=-5$. $\mathcal P:x+4y-z-5=0$.</li><li>$1+4-0-5=0$ : oui.</li><li>Même normal : $x+4y-z=0$.</li><li>$\vec n'(0;3;-1)$ ; $\vec n\cdot\vec n'=0+12+1=13\neq0$ : pas perpendiculaires.</li></ol>` },
    { niv: 2, t: "Droite et plan", enonce: R`<p>Repère orthonormé. $\mathcal P:2x+y-z-4=0$. Pour chaque droite, étudier sa position par rapport à $\mathcal P$ et donner l'intersection éventuelle.</p><ol><li>$(d_1):x=1+t$, $y=2-t$, $z=3t$.</li><li>$(d_2):x=t$, $y=1+t$, $z=3t$.</li><li>$(d_3):x=2+t$, $y=t$, $z=3t$.</li></ol>`,
      corrige: R`<ol><li>$2(1+t)+(2-t)-3t-4=0$ : $-2t=0$, $t=0$. Sécants en $(1;2;0)$.</li><li>$\vec u_2(1;1;3)$ et $\vec n(2;1;-1)$ : $\vec u_2\cdot\vec n=0$, parallèles. En remplaçant : $2t+1+t-3t-4=-3\neq0$ : aucun point commun, strictement parallèle.</li><li>$\vec u_3(1;1;3)$, même conclusion pour la direction. $2(2+t)+t-3t-4=0$ pour tout $t$ : $(d_3)$ est <b>incluse</b> dans $\mathcal P$.</li></ol>` },
    { niv: 2, t: "Deux droites", enonce: R`<p>Repère orthonormé. $(d):x=1+2t$, $y=-1+t$, $z=3-t$ ($t\in\R$) et $(d'):x=4+s$, $y=1-s$, $z=1+s$ ($s\in\R$). On note aussi $(d'')$ la droite $x=4+s$, $y=1-s$, $z=s$.</p><ol><li>Les droites $(d)$ et $(d')$ sont-elles parallèles ?</li><li>Montrer qu'elles sont sécantes et donner leur point d'intersection.</li><li>Sont-elles perpendiculaires ?</li><li>Montrer que $(d)$ et $(d'')$ sont non coplanaires.</li></ol>`,
      corrige: R`<ol><li>$\vec u(2;1;-1)$, $\vec v(1;-1;1)$ : $\frac12\neq\frac{-1}1$, non colinéaires, pas parallèles.</li><li>$1+2t=4+s$ et $-1+t=1-s$. De la seconde, $s=2-t$ ; dans la première : $1+2t=6-t$, $t=\frac53$, $s=\frac13$. Troisième équation : $3-\frac53=\frac43$ et $1+\frac13=\frac43$ ✓. Sécantes au point $\left(\frac{13}3;\frac23;\frac43\right)$.</li><li>$\vec u\cdot\vec v=2-1-1=0$ : orthogonales, et sécantes, donc perpendiculaires.</li><li>$(d'')$ a le même vecteur directeur que $(d')$, non colinéaire à $\vec u$. Les deux premières équations sont les mêmes qu'en 2 : $t=\frac53$, $s=\frac13$. Troisième : $\frac43\neq\frac13$. Aucune solution : ni parallèles ni sécantes, donc non coplanaires.</li></ol>
<p class="stylo">Les deux premières équations ne décident de rien : c'est la troisième qui sépare « sécantes » et « non coplanaires ».</p>` },
    { niv: 3, t: "Plan, projeté, distance, volume (type bac)", enonce: R`<p>Repère orthonormé. $A(1;1;1)$, $B(2;3;1)$, $C(0;1;2)$ et $S(5;1;6)$.</p><ol><li>Montrer que $A$, $B$, $C$ définissent un plan, puis que $\vec n(2;-1;2)$ est normal à ce plan. En déduire une équation cartésienne de $(ABC)$.</li><li>Donner une représentation paramétrique de la droite $\Delta$ passant par $S$ et orthogonale à $(ABC)$.</li><li>Déterminer les coordonnées du projeté orthogonal $H$ de $S$ sur $(ABC)$, puis la distance de $S$ au plan.</li><li>Calculer $\vec{AB}\cdot\vec{AC}$ et en déduire l'aire du triangle $ABC$, puis le volume du tétraèdre $SABC$.</li><li>Montrer que le plan $\mathcal Q:x+2y-7=0$ contient $H$ et est perpendiculaire à $(ABC)$.</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(1;2;0)$, $\vec{AC}(-1;0;1)$ non colinéaires : $A$, $B$, $C$ non alignés. $\vec n\cdot\vec{AB}=2-2+0=0$, $\vec n\cdot\vec{AC}=-2+0+2=0$ : $\vec n$ est normal. $2x-y+2z+d=0$ avec $A$ : $2-1+2+d=0$, $d=-3$. $(ABC):2x-y+2z-3=0$.</li><li>$\Delta:x=5+2t$, $y=1-t$, $z=6+2t$, $t\in\R$.</li><li>$2(5+2t)-(1-t)+2(6+2t)-3=0\iff18+9t=0\iff t=-2$. $H(1;3;2)$. Distance : $SH=|t|\times\|\vec n\|=2\times3=6$.</li><li>$\vec{AB}\cdot\vec{AC}=-1$, $AB=\sqrt5$, $AC=\sqrt2$, $\cos\alpha=\frac{-1}{\sqrt{10}}$, $\sin\alpha=\frac3{\sqrt{10}}$ ($\alpha$ : angle en $A$). Aire : $\frac12\sqrt5\sqrt2\times\frac3{\sqrt{10}}=\frac32$. Volume : $\frac13\times\frac32\times6=3$.</li><li>$H$ : $1+6-7=0$ ✓. Normaux $(1;2;0)$ et $(2;-1;2)$ : produit scalaire $2-2+0=0$, plans perpendiculaires.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole, 17 juin 2026 (jour 2), exercice 1", url: "https://www.apmep.fr/IMG/pdf/BAC_generale_specialite_J2_2026-06-17_Metropole_FK-v4.pdf", h: R`Le problème complet du chapitre : plan $(ABC)$ d'équation $x-y+4z-5=0$, droite $\Delta$ passant par $D$ orthogonale au plan, projeté $H\left(-\frac16;\frac16;\frac43\right)$, aire $3\sqrt2$, volume $1$, puis le point $D_k(0;0;k)$ : coplanaire avec $A$, $B$, $C$ pour $k=\frac54$.` },
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 3", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Vrai/faux : représentation paramétrique de $(AB)$, vecteur normal à $(OAB)$, deux droites $d$ et $d'$ non coplanaires ?, distance du point $C(2;-1;2)$ au plan $x-y+z+1=0$ égale à $2\sqrt3$ ? (vrai : le projeté est $(0;1;0)$.)` },
    { ref: "Bac 2025, Amérique du Sud, 14 novembre 2025 (jour 2), exercice 2", url: "https://www.apmep.fr/IMG/pdf/Ame_du_Sud_J2_14_11_2025_DV.pdf", h: R`QCM de positions relatives : deux droites (parallèles, orthogonales, sécantes ?), une droite et un plan (incluse, parallèle, sécante ?), coplanarité de quatre points, intersection de deux plans.` }
  ],
  retenir: R`
[thm|Droite $(A;\vec u)$, $\vec u(a;b;c)$]$\begin{cases}x=x_A+at\\y=y_A+bt\\z=z_A+ct\end{cases}$, $t\in\R$. Constantes : un point. Coefficients de $t$ : un vecteur directeur.[/]
[thm|Plan de normal $\vec n(a;b;c)$]$ax+by+cz+d=0$ ; $d$ se trouve avec un point. Réciproque : une telle équation est un plan normal à $\vec n(a;b;c)$.[/]
<div class="tab-wrap"><table><tr><th>Question</th><th>Outil</th></tr>
<tr><td>Droite ∩ plan</td><td>remplacer $x$, $y$, $z$ dans l'équation ⟹ équation en $t$</td></tr>
<tr><td>Droite ∩ droite</td><td>paramètres $t$ et $s$, 3 équations, la 3<sup>e</sup> décide</td></tr>
<tr><td>Droite ∥ plan</td><td>$\vec u\cdot\vec n=0$</td></tr>
<tr><td>Plans ∥ / ⊥</td><td>normaux colinéaires / orthogonaux</td></tr>
<tr><td>Projeté sur un plan</td><td>droite $(M;\vec n)$ ∩ plan ; distance $|t|\,\|\vec n\|$</td></tr>
<tr><td>Projeté sur une droite</td><td>$H=A+t\vec u$, $\vec{HM}\cdot\vec u=0$</td></tr></table></div>
<p class="stylo">Toujours vérifier : le point trouvé satisfait l'équation du plan, la représentation de la droite.</p>`,
  qcm: [
    { q: R`La droite $x=2-t$, $y=3t$, $z=1+2t$ a pour vecteur directeur :`, c: [R`$(2;0;1)$`, R`$(-1;3;2)$`, R`$(2;3;1)$`, R`$(1;3;2)$`], r: 1, e: R`Les coefficients de $t$.`, ref: "parametrique" },
    { q: R`Pour $t=0$, la droite $x=2-t$, $y=3t$, $z=1+2t$ passe par :`, c: [R`$(2;0;1)$`, R`$(-1;3;2)$`, R`$(0;0;0)$`, R`$(1;3;3)$`], r: 0, e: R`Les constantes donnent le point de paramètre $0$.`, ref: "parametrique" },
    { q: R`Un vecteur normal au plan $3x-z+2=0$ est :`, c: [R`$(3;-1;2)$`, R`$(3;0;-1)$`, R`$(3;-1;0)$`, R`$(0;3;-1)$`], r: 1, e: R`Coefficients de $x$, $y$, $z$ : $3$, $0$, $-1$.`, ref: "cartesienne" },
    { q: R`Le plan passant par $A(1;0;2)$ de vecteur normal $(2;1;-1)$ a pour équation :`, c: [R`$2x+y-z=0$`, R`$2x+y-z+1=0$`, R`$x+2z-5=0$`, R`$2x+y-z-2=0$`], r: 0, e: R`$2+0-2+d=0$, donc $d=0$.`, ref: "cartesienne" },
    { q: R`Une droite de vecteur directeur $\vec u$ et un plan de vecteur normal $\vec n$ avec $\vec u\cdot\vec n=0$ sont :`, c: ["sécants", "parallèles (droite éventuellement incluse)", "orthogonaux", "on ne peut rien dire"], r: 1, e: R`$\vec u$ est dans la direction du plan.`, ref: "positions" },
    { q: R`Les plans $x+y+z=1$ et $2x+2y+2z=5$ sont :`, c: ["sécants", "strictement parallèles", "confondus", "perpendiculaires"], r: 1, e: R`Normaux colinéaires ; $2x+2y+2z=2$ serait le même plan, pas $=5$.`, ref: "positions" },
    { q: R`Les plans $x+y+z=1$ et $x-y=3$ sont :`, c: ["parallèles", "perpendiculaires", "confondus", "sécants non perpendiculaires"], r: 1, e: R`$(1;1;1)\cdot(1;-1;0)=0$.`, ref: "positions" },
    { q: R`En remplaçant la représentation de $(d)$ dans l'équation de $\mathcal P$, on obtient $0t=0$. Donc :`, c: [R`$(d)$ et $\mathcal P$ sont sécants en $t=0$`, R`$(d)$ est incluse dans $\mathcal P$`, R`$(d)$ est strictement parallèle à $\mathcal P$`, R`$(d)$ est orthogonale à $\mathcal P$`], r: 1, e: R`Tout réel $t$ convient : tous les points de $(d)$ sont dans $\mathcal P$.`, ref: "intersections" },
    { q: R`La droite $x=t$, $y=2-t$, $z=-1+2t$ coupe le plan $x+y+z=3$ au point :`, c: [R`$(1;1;1)$`, R`$(0;2;-1)$`, R`$(2;0;3)$`, R`elle ne le coupe pas`], r: 0, e: R`$t+2-t-1+2t=3\iff t=1$.`, ref: "intersections" },
    { q: R`Pour étudier l'intersection de deux droites, on utilise :`, c: ["le même paramètre $t$ pour les deux", "deux paramètres différents $t$ et $s$", "les équations cartésiennes des droites", "le produit scalaire seulement"], r: 1, e: R`Le point commun n'a pas de raison d'avoir le même paramètre sur les deux droites.`, ref: "intersections" },
    { q: R`$M(4;-1;3)$, $\mathcal P:2x-y+2z-3=0$. La distance de $M$ à $\mathcal P$ vaut :`, c: ["$3$", "$4$", "$12$", "$\\frac43$"], r: 1, e: R`$t=-\frac43$ et $\|\vec n\|=3$ : $MH=4$.`, ref: "projections" },
    { q: R`Le projeté orthogonal de $M$ sur un plan $\mathcal P$ de normal $\vec n$ est l'intersection de $\mathcal P$ avec :`, c: [R`la droite passant par $M$ dirigée par $\vec n$`, R`la droite passant par $M$ parallèle à $\mathcal P$`, R`le plan passant par $M$ normal à $\vec n$`, R`la droite $(OM)$`], r: 0, e: R`La droite orthogonale au plan passant par $M$.`, ref: "projections" },
    { q: R`$\vec u(1;2;0)$, $\vec v(0;1;1)$, $\vec w(1;0;-2)$ :`, c: ["forment une base", R`sont coplanaires car $\vec w=\vec u-2\vec v$`, "sont deux à deux orthogonaux", R`sont coplanaires car $\vec w=\vec u+\vec v$`], r: 1, e: R`$\vec u-2\vec v=(1;0;-2)$.`, ref: "systemes" },
    { q: R`Le point $D_k(0;0;k)$ est dans le plan $x-y+4z-5=0$ pour $k=$`, c: ["$5$", "$\\frac54$", "$-\\frac54$", "$\\frac45$"], r: 1, e: R`$4k-5=0$ (bac Métropole, 17 juin 2026).`, ref: "systemes" }
  ],
  cartes: [
    [R`Représentation paramétrique de $(A;\vec u)$`, R`$x=x_A+at$, $y=y_A+bt$, $z=z_A+ct$, $t\in\R$`],
    [R`Dans une représentation paramétrique, les coefficients de $t$…`, R`… forment un vecteur directeur.`],
    [R`Équation d'un plan de normal $\vec n(a;b;c)$`, R`$ax+by+cz+d=0$`],
    [R`Vecteur normal au plan $ax+by+cz+d=0$`, R`$\vec n(a;b;c)$`],
    [R`Plan passant par 3 points : vecteur normal`, R`Résoudre $\vec n\cdot\vec{AB}=0$ et $\vec n\cdot\vec{AC}=0$.`],
    [R`Droite ∥ plan`, R`$\vec u\cdot\vec n=0$`],
    [R`Droite ⊥ plan`, R`$\vec u$ et $\vec n$ colinéaires`],
    [R`Plans parallèles / perpendiculaires`, R`Normaux colinéaires / orthogonaux`],
    [R`Intersection droite-plan`, R`Remplacer $x$, $y$, $z$ par la représentation paramétrique dans l'équation.`],
    [R`$0t=0$ / $0t=5$`, R`Droite incluse / strictement parallèle`],
    [R`Intersection de deux droites`, R`Paramètres $t$ et $s$ ; trois équations ; la troisième décide.`],
    [R`Projeté de $M$ sur un plan`, R`Droite $(M;\vec n)$ ∩ plan ; distance $|t|\,\|\vec n\|$.`],
    [R`Formule de la distance point-plan (hors programme)`, R`$\frac{|ax_M+by_M+cz_M+d|}{\sqrt{a^2+b^2+c^2}}$`],
    [R`Démonstration exigible du chapitre`, R`Équation cartésienne du plan normal à $\vec n$ passant par $A$ : $\vec{AM}\cdot\vec n=0$.`]
  ]
};

/* Animation : un point parcourt la droite, traverse le plan ; puis un projeté */
ANIMS.droitePlan = {
  titre: R`Le paramètre $t$ fait avancer le point jusqu'au plan`,
  vb: [360, 330],
  etapes: [
    { d: 3.5, l: R`Repère orthonormé. Le plan $\mathcal P:x+y+z-3=0$ coupe les axes en $(3;0;0)$, $(0;3;0)$, $(0;0;3)$. Son vecteur normal $\vec n(1;1;1)$ se lit sur l'équation.` },
    { d: 7, l: R`La droite $(d)$ : $x=t$, $y=2-t$, $z=-1+2t$. Quand $t$ augmente, le point $M(t)$ avance. On suit la quantité $x+y+z-3=2t-2$ : négative derrière le plan (pointillés), positive devant.` },
    { d: 3.5, l: R`Elle s'annule pour $t=1$ : $M(1)=I(1;1;1)$ est sur le plan. C'est le point d'intersection.` },
    { d: 4, l: R`Le calcul fait la même chose sans dessin : on remplace $x$, $y$, $z$ dans l'équation, $t+(2-t)+(-1+2t)-3=0$, donc $2t-2=0$ et $t=1$.` },
    { d: 6, l: R`Même méthode pour un projeté : depuis $S(2;3;2)$, on part dans la direction de $\vec n$. $S+t\vec n$ est sur $\mathcal P$ pour $3t+4=0$, $t=-\frac43$ : $H\left(\frac23;\frac53;\frac23\right)$ et $SH=\frac43\sqrt3\approx2{,}31$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, nf = ANIM.nf, P = CAV.vue({ ox: 150, oy: 196, s: 50, k: 0.5, a: 40, repere: true });
    var O = [0, 0, 0];
    [[[4, 0, 0], "x"], [[0, 4.1, 0], "y"], [[0, 0, 4.2], "z"]].forEach(function (a) { CAV.trait(S, P, O, a[0], "g-axe", {}); CAV.txt(S, P, a[0], a[1], "", "middle", 0, a[1] === "z" ? -6 : 14); });
    CAV.txt(S, P, O, "O", "", "end", -5, 12);
    var T1 = [3, 0, 0], T2 = [0, 3, 0], T3 = [0, 0, 3];
    CAV.poly(S, P, [T1, T2, T3], "a-plein");
    S.px.txt(8, 22, "𝒫 : x + y + z − 3 = 0", "b", "start", { "font-size": 13 });
    S.px.rect(0, 294, 360, 36, "", { style: "fill:var(--papier);stroke:var(--ligne)" });
    if (k <= 3) { CAV.fleche(S, P, [1, 1, 1], [1.7, 1.7, 1.7], k === 0 ? E(t) : 1, "g-c", { "stroke-width": 2.2 }); CAV.txt(S, P, [1.7, 1.7, 1.7], "n", "b", "start", 6, 0); }
    var p2 = [P(3, 0, 0), P(0, 3, 0), P(0, 0, 3)];
    function dedans(q) {
      var s = 0; for (var i = 0; i < 3; i++) { var a = p2[i], b = p2[(i + 1) % 3]; s += (b[0] - a[0]) * (q[1] - a[1]) - (b[1] - a[1]) * (q[0] - a[0]) > 0 ? 1 : -1; }
      return Math.abs(s) === 3;
    }
    function D(u) { return [u, 2 - u, -1 + 2 * u]; }
    function cache(u) { var m = D(u); return m[0] + m[1] + m[2] < 3 && dedans(P(m[0], m[1], m[2])); }
    /* la droite, en morceaux d'un seul tenant (visibles en trait plein, cachés en pointillés) */
    function droite(ta, tb) {
      var n = 80, debut = ta, etat = cache(ta);
      for (var i = 1; i <= n; i++) {
        var u = ta + (tb - ta) * i / n, e = i === n ? !etat : cache(u);
        if (e !== etat) {
          CAV.trait(S, P, D(debut), D(u), "g-c2", etat ? { "stroke-width": 2, "stroke-dasharray": "5 4", opacity: 0.75 } : { "stroke-width": 2.6 });
          debut = u; etat = e;
        }
      }
    }
    var ta = -0.4, tb = 2.2;
    if (k <= 3) {
      var tm = k === 1 ? ANIM.l(ta, tb, E(t)) : k === 2 ? ANIM.l(tb, 1, E(ANIM.p(t, 0, 0.6))) : 1;
      droite(ta, k === 1 ? tm : tb);
      CAV.txt(S, P, D(tb), "(d)", "r", "start", 6, 2);
      if (k >= 1) {
        var Mt = D(tm), v = 2 * tm - 2, ici = k >= 2 && Math.abs(tm - 1) < 0.01;
        CAV.pt(S, P, Mt, ici ? "g-pt" : "g-pt2", 5);
        CAV.txt(S, P, Mt, ici ? "I" : "M", ici ? "b" : "r", "start", 8, -6);
        if (k <= 2) {
          S.px.txt(8, 309, "t = " + nf(tm, 2) + "    M(" + nf(Mt[0], 2) + " ; " + nf(Mt[1], 2) + " ; " + nf(Mt[2], 2) + ")", "", "start", { "font-size": 12 });
          S.px.txt(8, 325, "x + y + z − 3 = 2t − 2 = " + nf(v, 2) + (Math.abs(v) < 0.01 ? "  : sur le plan" : v < 0 ? "  : derrière" : "  : devant"), Math.abs(v) < 0.01 ? "b" : "r", "start", { "font-size": 12 });
        }
      }
      if (k === 0) S.px.math(4, 296, 352, 32, R`$(d):x=t,\ y=2-t,\ z=-1+2t$`);
      if (k === 3) S.px.math(4, 296, 352, 32, R`$t+(2-t)+(-1+2t)-3=0\iff t=1$`, { opacity: E(t) });
    } else {
      droite(ta, tb);
      var Sp = [2, 3, 2], Hp = [2 / 3, 5 / 3, 2 / 3], f = E(ANIM.p(t, 0.1, 0.75)), cur = CAV.lerp3(Sp, Hp, f);
      CAV.trait(S, P, Sp, cur, "g-c", { "stroke-width": 2.6 });
      CAV.pt(S, P, Sp, "g-pt2", 4.5); CAV.txt(S, P, Sp, "S", "r", "start", 8, -4);
      CAV.pt(S, P, cur, f > 0.98 ? "g-pt" : "g-pt2", 4.5);
      S.px.txt(8, 316, "S + t·n = (2 + t ; 3 + t ; 2 + t)", "", "start", { "font-size": 12 });
      if (f > 0.98) { CAV.txt(S, P, Hp, "H", "b", "end", -8, 12); S.px.math(186, 296, 172, 32, R`$t=-\frac43$, $SH=\frac{4\sqrt3}3$`); }
    }
  }
};
