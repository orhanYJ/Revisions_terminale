/* ---------- Chapitre 11 : orthogonalité et distances dans l'espace ---------- */
var CH11 = {
  id: "ch11", num: 11, statut: "ok", partie: "Algèbre et géométrie", titre: "Orthogonalité et distances dans l'espace", court: "Orthogonalité",
  sous: "Le produit scalaire passe en trois dimensions : angles, longueurs, vecteur normal, projeté orthogonal.",
  resume: "Produit scalaire, base orthonormée, droites et plans orthogonaux, vecteur normal, projeté orthogonal, distances.",
  essentiel: [
    R`Deux vecteurs de l'espace sont toujours dans un même plan : leur <b>produit scalaire</b> se définit comme en Première, $\vec u\cdot\vec v=\|\vec u\|\times\|\vec v\|\times\cos(\vec u,\vec v)$. Il est symétrique et bilinéaire.`,
    R`Dans une base <b>orthonormée</b> : $\vec u\cdot\vec v=xx'+yy'+zz'$, $\|\vec u\|=\sqrt{x^2+y^2+z^2}$, $AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}$.`,
    R`$\vec u⊥\vec v\iff\vec u\cdot\vec v=0$. Une droite est orthogonale à un plan si elle est orthogonale à <b>deux droites sécantes</b> de ce plan.`,
    R`Un <b>vecteur normal</b> $\vec n$ à un plan est un vecteur non nul orthogonal à sa direction. Le plan passant par $A$ et normal à $\vec n$ est l'ensemble des points $M$ tels que $\vec{AM}\cdot\vec n=0$.`,
    R`Le <b>projeté orthogonal</b> $H$ de $M$ sur un plan (ou une droite) est le point du plan le plus proche de $M$ : la distance de $M$ au plan est $MH$.`
  ],
  attendus: [
    R`Utiliser le produit scalaire pour démontrer une orthogonalité, pour calculer un angle, une longueur dans l'espace.`,
    R`Utiliser la projection orthogonale pour déterminer la distance d'un point à une droite ou à un plan.`,
    R`Résoudre des problèmes impliquant des grandeurs et mesures : longueur, angle, aire, volume.`,
    R`Étudier des problèmes de configuration : orthogonalité de deux droites, d'une droite et d'un plan ; lieux géométriques simples, par exemple le plan médiateur de deux points.`,
    R`Démonstration exigible : le projeté orthogonal d'un point $M$ sur un plan $\mathcal P$ est le point de $\mathcal P$ le plus proche de $M$ <span class="tag bo">BO</span>.`
  ],
  premiere: R`
<ul><li><b>Produit scalaire dans le plan</b> : $\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos(\vec u,\vec v)$ ; en repère orthonormé $\vec u\cdot\vec v=xx'+yy'$.</li>
<li><b>Projection</b> : si $H$ est le projeté orthogonal de $C$ sur $(AB)$, $\vec{AB}\cdot\vec{AC}=\vec{AB}\cdot\vec{AH}$ ($=AB\times AH$ si $\vec{AB}$ et $\vec{AH}$ ont le même sens, $-AB\times AH$ sinon).</li>
<li><b>Identités</b> : $\|\vec u+\vec v\|^2=\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2$ ; formule d'Al-Kashi $BC^2=AB^2+AC^2-2AB\times AC\cos\alpha$, où $\alpha$ est l'angle du triangle en $A$.</li>
<li><b>Trigonométrie</b> : $\cos60°=\frac12$, $\cos45°=\frac{\sqrt2}2$, $\cos90°=0$ ; $\cos$ est négatif pour un angle obtus.</li></ul>`,
  cours: [
    { id: "produit", titre: "Produit scalaire de deux vecteurs de l'espace", html: R`
<p>Représentons $\vec u=\vec{AB}$ et $\vec v=\vec{AC}$ à partir d'un même point $A$ : les trois points $A$, $B$, $C$ sont toujours dans un même plan. On calcule donc le produit scalaire <b>dans ce plan</b>, avec les outils de Première.</p>
[def|Produit scalaire]$\vec u\cdot\vec v=\|\vec u\|\times\|\vec v\|\times\cos(\vec u,\vec v)$ si les deux vecteurs sont non nuls, et $0$ sinon. En particulier $\vec u\cdot\vec u=\|\vec u\|^2$.[/]
[prop|Règles de calcul]<ul><li><b>Symétrie</b> : $\vec u\cdot\vec v=\vec v\cdot\vec u$.</li><li><b>Bilinéarité</b> : $\vec u\cdot(\vec v+\vec w)=\vec u\cdot\vec v+\vec u\cdot\vec w$ et $\vec u\cdot(k\vec v)=k(\vec u\cdot\vec v)$.</li><li>$\|\vec u+\vec v\|^2=\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2$ et $\|\vec u-\vec v\|^2=\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2$.</li></ul>[/]
[prop|Formules de polarisation]$$\vec u\cdot\vec v=\frac12\left(\|\vec u+\vec v\|^2-\|\vec u\|^2-\|\vec v\|^2\right)=\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right).$$
Le produit scalaire se calcule donc avec des longueurs seulement.[/]
[ex|Avec la projection, dans le cube d'arête $a$]La droite $(AB)$ est orthogonale à la face $BCGF$ (elle est orthogonale à $(BC)$ et à $(BF)$, sécantes en $B$), donc à la droite $(BG)$ de cette face : le projeté orthogonal de $G$ sur $(AB)$ est $B$. Par la formule de projection, $\vec{AB}\cdot\vec{AG}=\vec{AB}\cdot\vec{AB}=a^2$.[/]
<div data-anim="projCube"></div>
[ex|Avec un triangle équilatéral]Dans le cube d'arête $1$, $AC=AF=CF=\sqrt2$ (diagonales de faces) : le triangle $ACF$ est équilatéral. Donc $\vec{AC}\cdot\vec{AF}=\sqrt2\times\sqrt2\times\cos60°=1$.[/]` },
    { id: "orthonormee", titre: "Base orthonormée : produit scalaire, norme, distance", html: R`
[def|Base et repère orthonormés]Une base $(\vec i,\vec j,\vec k)$ est <b>orthonormée</b> si les trois vecteurs sont deux à deux orthogonaux et de norme $1$. Exemple : $(\vec{AB},\vec{AD},\vec{AE})$ dans un cube d'arête $1$ (mais pas dans un pavé de dimensions différentes).[/]
[thm|Expressions en base orthonormée]Si $\vec u(x;y;z)$ et $\vec v(x';y';z')$ dans une base orthonormée :
$$\vec u\cdot\vec v=xx'+yy'+zz',\qquad\|\vec u\|=\sqrt{x^2+y^2+z^2},$$
$$AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}.$$[/]
[ex|Une longueur]$A(1;2;-1)$, $B(3;0;1)$ : $\vec{AB}(2;-2;2)$, $AB=\sqrt{4+4+4}=\sqrt{12}=2\sqrt3$.[/]
[meth|Calculer un angle]$\cos(\vec u,\vec v)=\dfrac{\vec u\cdot\vec v}{\|\vec u\|\times\|\vec v\|}$, puis la calculatrice (touche $\cos^{-1}$ ou Arccos, en mode degrés).[/]
[ex|L'angle entre deux grandes diagonales du cube]Repère $(A;\vec{AB},\vec{AD},\vec{AE})$, cube d'arête $1$ : $\vec{AG}(1;1;1)$, $\vec{BH}(-1;1;1)$. $\vec{AG}\cdot\vec{BH}=-1+1+1=1$ et $AG=BH=\sqrt3$, donc $\cos\theta=\frac13$ et $\theta\approx70{,}5°$. L'angle $\beta$ entre $\vec{AB}$ et $\vec{AG}$ : $\vec{AB}\cdot\vec{AG}=1$, $\cos\beta=\frac1{\sqrt3}$, soit environ $54{,}7°$.[/]
[piege|Seulement en base orthonormée]Dans la base $(\vec{AB},\vec{AC},\vec{AD})$ d'un tétraèdre quelconque, $xx'+yy'+zz'$ ne donne <b>pas</b> le produit scalaire : les vecteurs de base ne sont ni orthogonaux ni de norme 1.[/]` },
    { id: "orthogonalite", titre: "Droites orthogonales, droite orthogonale à un plan", html: R`
[def|Vecteurs et droites orthogonaux]$\vec u$ et $\vec v$ sont <b>orthogonaux</b> si $\vec u\cdot\vec v=0$ (le vecteur nul est orthogonal à tout vecteur). Deux droites sont <b>orthogonales</b> si leurs vecteurs directeurs le sont. Elles sont <b>perpendiculaires</b> si elles sont orthogonales <b>et sécantes</b>.[/]
[ex|Orthogonales sans se couper]Dans le cube, $(AE)$ et $(BC)$ sont orthogonales ($\vec{AE}\cdot\vec{BC}=\vec{AE}\cdot\vec{AD}=0$), mais elles sont non coplanaires : elles ne sont pas perpendiculaires.[/]
[def|Droite orthogonale à un plan]Une droite est <b>orthogonale à un plan</b> si elle est orthogonale à toutes les droites de ce plan.[/]
[thm|Critère pratique]Une droite est orthogonale à un plan si et seulement si elle est orthogonale à <b>deux droites sécantes</b> de ce plan : son vecteur directeur est orthogonal à deux vecteurs non colinéaires de la direction du plan.[/]
[ex|La diagonale du cube est orthogonale à un triangle]$\vec{AG}(1;1;1)$, $\vec{BD}(-1;1;0)$, $\vec{BE}(-1;0;1)$ : $\vec{AG}\cdot\vec{BD}=0$ et $\vec{AG}\cdot\vec{BE}=0$. Les droites $(BD)$ et $(BE)$ sont sécantes en $B$ : la grande diagonale $(AG)$ est orthogonale au plan $(BDE)$.[/]
[prop|Conséquences]<ul><li>Si $(d)$ est orthogonale à $\mathcal P$, elle est orthogonale à toute droite de $\mathcal P$ : par exemple $(AG)⊥(DE)$.</li><li>Deux droites orthogonales à un même plan sont parallèles ; deux plans orthogonaux à une même droite sont parallèles.</li></ul>[/]` },
    { id: "normal", titre: "Vecteur normal à un plan, plan médiateur", html: R`
[def|Vecteur normal]Un vecteur $\vec n$ <b>non nul</b> est <b>normal</b> au plan $\mathcal P$ s'il est orthogonal à tous les vecteurs de la direction de $\mathcal P$ ; il suffit qu'il soit orthogonal à deux vecteurs non colinéaires de $\mathcal P$. Tout vecteur directeur d'une droite orthogonale à $\mathcal P$ est normal à $\mathcal P$.[/]
[thm|Plan défini par un point et un vecteur normal]Étant donnés un point $A$ et un vecteur non nul $\vec n$, l'ensemble des points $M$ tels que $\vec{AM}\cdot\vec n=0$ est le plan passant par $A$ et normal à $\vec n$.[/]
[ex|Un vecteur normal à $(ABC)$]$A(2;0;0)$, $B(0;3;0)$, $C(0;0;6)$ et $\vec n(3;2;1)$. $\vec{AB}(-2;3;0)$ : $\vec n\cdot\vec{AB}=-6+6+0=0$. $\vec{AC}(-2;0;6)$ : $\vec n\cdot\vec{AC}=-6+0+6=0$. $\vec{AB}$ et $\vec{AC}$ ne sont pas colinéaires : $\vec n$ est normal au plan $(ABC)$.[/]
[prop|Position de deux plans par leurs vecteurs normaux]Deux plans sont <b>parallèles</b> si et seulement si leurs vecteurs normaux sont colinéaires ; ils sont <b>perpendiculaires</b> si et seulement si leurs vecteurs normaux sont orthogonaux. Une droite de vecteur directeur $\vec u$ est orthogonale à un plan de vecteur normal $\vec n$ si et seulement si $\vec u$ et $\vec n$ sont colinéaires ; elle lui est parallèle si et seulement si $\vec u\cdot\vec n=0$.[/]
[def|Plan médiateur]Le <b>plan médiateur</b> du segment $[AB]$ est le plan passant par son milieu $I$ et normal à $\vec{AB}$. C'est l'ensemble des points <b>équidistants</b> de $A$ et $B$.[/]
<p><b>Pourquoi ?</b> $MA^2-MB^2=(\vec{MA}-\vec{MB})\cdot(\vec{MA}+\vec{MB})=\vec{BA}\cdot2\vec{MI}=2\,\vec{IM}\cdot\vec{AB}$. Donc $MA=MB\iff\vec{IM}\cdot\vec{AB}=0$.</p>
[ex|Le plan médiateur d'une diagonale]Dans le cube, le centre $\Omega$ est le milieu de la grande diagonale $[DF]$. Le milieu $I\left(\frac12;0;0\right)$ de $[AB]$ vérifie $ID^2=\frac14+1+0=\frac54$ et $IF^2=\frac14+0+1=\frac54$ : il est équidistant de $D$ et $F$. Il en va de même des milieux de $[BC]$, $[CG]$, $[GH]$, $[HE]$, $[EA]$ : les six sommets de l'hexagone de la partie 4 du chapitre 10 sont dans le plan médiateur de $[DF]$, qui passe par $\Omega$ et est normal à $\vec{DF}(1;-1;1)$.[/]` },
    { id: "projete", titre: "Projeté orthogonal et distances", html: R`
[def|Projeté orthogonal]Le <b>projeté orthogonal</b> d'un point $M$ sur un plan $\mathcal P$ est le point d'intersection $H$ de $\mathcal P$ et de la droite passant par $M$ orthogonale à $\mathcal P$. Sur une droite $(d)$ : c'est le point $H$ de $(d)$ tel que $(MH)⊥(d)$ (ou $H=M$ si $M\in(d)$).[/]
<div data-anim="projete3d"></div>
[thm|Le point le plus proche]Le projeté orthogonal $H$ de $M$ sur $\mathcal P$ est le point de $\mathcal P$ le plus proche de $M$ : pour tout point $A$ de $\mathcal P$, $MA\geq MH$, avec égalité seulement si $A=H$. La <b>distance de $M$ au plan</b> est $MH$. Même chose pour une droite.[/]
[meth|Calculer le projeté sur une droite $(A;\vec u)$]$H=A+t\vec u$ avec $\vec{HM}\cdot\vec u=0$, ce qui donne $t=\dfrac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}$.[/]
[ex|Distance d'un sommet à une diagonale]Cube d'arête $1$ : projeté de $B$ sur $(AG)$. $t=\frac{\vec{AB}\cdot\vec{AG}}{AG^2}=\frac13$, donc $H\left(\frac13;\frac13;\frac13\right)$ et $BH=\sqrt{\left(\frac23\right)^2+\left(\frac13\right)^2+\left(\frac13\right)^2}=\frac{\sqrt6}3\approx0{,}816$.[/]
[ex|Distance d'un point à un plan]Le projeté de $A$ sur le plan $(BDE)$ est sur la droite $(AG)$, orthogonale au plan : $H=\left(t;t;t\right)$. On cherche $t$ tel que $\vec{BH}\cdot\vec{AG}=0$ : $(t-1)+t+t=0$, d'où $t=\frac13$. Distance : $AH=\sqrt{3\times\frac19}=\frac{\sqrt3}3\approx0{,}577$.[/]` },
    { id: "mesures", titre: "Longueurs, aires, volumes", html: R`
<p>Le produit scalaire sert à trouver des longueurs, des angles droits (donc des hauteurs), et de là des aires et des volumes.</p>
[prop|Volume d'une pyramide ou d'un tétraèdre]$V=\frac13\times\mathcal B\times h$, où $\mathcal B$ est l'aire d'une base et $h$ la hauteur relative à cette base : la distance du sommet opposé au plan de la base.[/]
[ex|Un volume calculé de deux façons]Le tétraèdre $ABDE$ coupé dans le cube d'arête $1$ :
<ul><li>base $ABD$ (aire $\frac12$), hauteur $AE=1$ : $V=\frac13\times\frac12\times1=\frac16$ ;</li><li>base $BDE$, équilatéral de côté $\sqrt2$, d'aire $\frac{\sqrt3}4\times2=\frac{\sqrt3}2$, et hauteur $\frac{\sqrt3}3$ (partie 5) : $V=\frac13\times\frac{\sqrt3}2\times\frac{\sqrt3}3=\frac16$. ✓</li></ul>
Cette double écriture est une technique classique du bac : connaissant le volume, on en déduit une distance, ou l'aire d'un triangle.[/]
[meth|Aire d'un triangle $ABC$]<ul><li>Si l'on sait que le triangle est rectangle en $A$ (produit scalaire nul) : $\frac{AB\times AC}2$.</li><li>Sinon : $\frac12\times AB\times AC\times\sin\alpha$, où $\alpha$ est l'angle en $A$, avec $\cos\alpha=\frac{\vec{AB}\cdot\vec{AC}}{AB\times AC}$ et $\sin\alpha=\sqrt{1-\cos^2\alpha}$ (car $\sin\alpha\geq0$ pour un angle de triangle).</li></ul>[/]
[ex|Le triangle $ABC$ avec $A(2;0;0)$, $B(0;3;0)$, $C(0;0;6)$]$\vec{AB}\cdot\vec{AC}=4$, $AB=\sqrt{13}$, $AC=\sqrt{40}$, donc $\cos\alpha=\frac4{\sqrt{520}}$, $\sin\alpha=\sqrt{1-\frac{16}{520}}=\sqrt{\frac{504}{520}}$ et l'aire vaut $\frac12\sqrt{13}\sqrt{40}\sqrt{\frac{504}{520}}=\frac{\sqrt{504}}2=3\sqrt{14}\approx11{,}2$.[/]
<p><span class="tag hp">Pour aller plus loin</span> La <b>sphère</b> de centre $\Omega$ et de rayon $r$ est l'ensemble des points $M$ tels que $\Omega M=r$. Un plan à la distance $d$ de $\Omega$ la coupe selon un cercle de rayon $\sqrt{r^2-d^2}$ si $d<r$, lui est tangent si $d=r$, ne la rencontre pas si $d>r$ (Pythagore dans le triangle $\Omega HM$). Approfondissement non exigible.</p>` }
  ],
  pieges: [
    { t: "Orthogonales n'est pas perpendiculaires", h: R`Deux droites orthogonales peuvent ne pas se couper ($(AE)$ et $(BC)$ dans le cube). Perpendiculaires = orthogonales <b>et</b> sécantes.` },
    { t: "Orthogonale à une seule droite du plan ne suffit pas", h: R`Pour montrer qu'une droite est orthogonale à un plan, il faut <b>deux</b> droites <b>sécantes</b> du plan (deux vecteurs non colinéaires). Deux droites parallèles ne suffisent pas.` },
    { t: "La formule $xx'+yy'+zz'$", h: R`Elle n'est valable que dans une base <b>orthonormée</b>. Vérifie toujours que le repère de l'énoncé l'est.` },
    { t: "Distance à un plan : pas n'importe quel point", h: R`La distance de $M$ au plan est $MH$ avec $H$ le <b>projeté orthogonal</b>, pas $MA$ pour un point $A$ quelconque du plan (qui est plus grand).` },
    { t: "Norme et carré", h: R`$\|\vec u\|^2=x^2+y^2+z^2$, donc $\|\vec u\|=\sqrt{x^2+y^2+z^2}$ : n'oublie pas la racine, ni les signes ($(-2)^2=4$).` },
    { t: "Un angle obtus a un cosinus négatif", h: R`Si $\vec u\cdot\vec v<0$, l'angle entre les vecteurs est obtus. L'angle entre deux <b>droites</b> se prend en général aigu : on prend alors la valeur absolue du cosinus.` }
  ],
  demos: [
    { bo: true, t: "Le projeté orthogonal de $M$ sur $\\mathcal P$ est le point de $\\mathcal P$ le plus proche de $M$", h: R`
<p>Soit $H$ le projeté orthogonal de $M$ sur $\mathcal P$, et $A$ un point quelconque de $\mathcal P$.</p>
<p>La droite $(MH)$ est orthogonale au plan $\mathcal P$, et $\vec{HA}$ est un vecteur de la direction de $\mathcal P$ (car $H$ et $A$ sont dans $\mathcal P$). Donc $\vec{MH}\cdot\vec{HA}=0$.</p>
<p>Alors, par la relation de Chasles :
$$MA^2=\|\vec{MH}+\vec{HA}\|^2=MH^2+2\,\vec{MH}\cdot\vec{HA}+HA^2=MH^2+HA^2.$$</p>
<p>Comme $HA^2\geq0$, on a $MA^2\geq MH^2$, donc $MA\geq MH$ (ce sont des longueurs, positives). L'égalité a lieu si et seulement si $HA=0$, c'est-à-dire $A=H$.</p>
<p>Conclusion : $H$ est l'unique point de $\mathcal P$ qui réalise la plus petite distance à $M$. CQFD.</p>
<p class="stylo">C'est le théorème de Pythagore dans le triangle $MHA$, rectangle en $H$, écrit avec le produit scalaire.</p>` },
    { bo: false, t: "Le produit scalaire en base orthonormée", h: R`
<p>Soit $(\vec i,\vec j,\vec k)$ orthonormée : $\vec i\cdot\vec i=\vec j\cdot\vec j=\vec k\cdot\vec k=1$ et $\vec i\cdot\vec j=\vec i\cdot\vec k=\vec j\cdot\vec k=0$.</p>
<p>Par bilinéarité, $(x\vec i+y\vec j+z\vec k)\cdot(x'\vec i+y'\vec j+z'\vec k)$ se développe en neuf termes ; les six termes « croisés » sont nuls, il reste $xx'\,\vec i\cdot\vec i+yy'\,\vec j\cdot\vec j+zz'\,\vec k\cdot\vec k=xx'+yy'+zz'$.</p>
<p>Avec $\vec v=\vec u$ : $\|\vec u\|^2=x^2+y^2+z^2$.</p>` },
    { bo: false, t: "Critère : deux droites sécantes suffisent", h: R`
<p>Soit $\vec n$ orthogonal à deux vecteurs non colinéaires $\vec u$ et $\vec v$ de la direction de $\mathcal P$. Tout vecteur $\vec w$ de cette direction s'écrit $\vec w=a\vec u+b\vec v$ (chapitre 10). Par bilinéarité :
$$\vec n\cdot\vec w=a\,\vec n\cdot\vec u+b\,\vec n\cdot\vec v=a\times0+b\times0=0.$$
Donc $\vec n$ est orthogonal à toute la direction du plan : une droite dirigée par $\vec n$ est orthogonale à toute droite de $\mathcal P$.</p>` },
    { bo: false, t: "Formules de polarisation", h: R`
<p>En développant par bilinéarité et symétrie : $\|\vec u+\vec v\|^2=(\vec u+\vec v)\cdot(\vec u+\vec v)=\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2$, d'où $\vec u\cdot\vec v=\frac12\left(\|\vec u+\vec v\|^2-\|\vec u\|^2-\|\vec v\|^2\right)$.</p>
<p>De même $\|\vec u-\vec v\|^2=\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2$. En soustrayant : $\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2=4\vec u\cdot\vec v$.</p>` }
  ],
  algos: [
    { bo: false, t: "Produit scalaire, norme et angle", code: `from math import sqrt, acos, degrees

def scal(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def norme(u):
    return sqrt(scal(u, u))

def angle(u, v):
    return degrees(acos(scal(u, v) / (norme(u) * norme(v))))

AG, BH, AB = (1, 1, 1), (-1, 1, 1), (1, 0, 0)
print(scal(AG, BH), round(angle(AG, BH), 2))
print(round(angle(AB, AG), 2))`, sortie: `1 70.53
54.74`,
      apres: R`<p>Cube d'arête $1$, repère $(A;\vec{AB},\vec{AD},\vec{AE})$ orthonormé : on retrouve les angles de la partie 2.</p>` },
    { bo: false, t: "Projeté orthogonal d'un point sur une droite", code: `from fractions import Fraction as Fr

def projete_droite(M, A, u):
    AM = [M[i] - A[i] for i in range(3)]
    t = Fr(sum(AM[i]*u[i] for i in range(3)), sum(x*x for x in u))
    return [A[i] + t*u[i] for i in range(3)]

H = projete_droite((1, 0, 0), (0, 0, 0), (1, 1, 1))
print(H)`, sortie: `[Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]`,
      apres: R`<p>Projeté de $B$ sur la diagonale $(AG)$ du cube : $t=\frac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}$.</p>` },
    { bo: false, t: "Une droite est-elle orthogonale à un plan (ABC) ?", code: `def scal(u, v):
    return sum(u[i]*v[i] for i in range(3))

def vec(P, Q):
    return [Q[i] - P[i] for i in range(3)]

def orthogonale_au_plan(u, A, B, C):
    # u orthogonal à deux vecteurs non colinéaires du plan
    return scal(u, vec(A, B)) == 0 and scal(u, vec(A, C)) == 0

A, B, C = (2, 0, 0), (0, 3, 0), (0, 0, 6)
print(orthogonale_au_plan((3, 2, 1), A, B, C))
print(orthogonale_au_plan((1, 1, 1), A, B, C))`, sortie: `True
False`,
      apres: R`<p>On suppose $A$, $B$, $C$ non alignés (sinon ils ne définissent pas un plan).</p>` }
  ],
  methodes: [
    { t: "Démontrer qu'une droite est orthogonale à un plan", h: R`
<ol><li>Trouve deux vecteurs <b>non colinéaires</b> du plan (par exemple $\vec{AB}$ et $\vec{AC}$).</li><li>Calcule les deux produits scalaires avec le vecteur directeur de la droite.</li><li>S'ils sont nuls : la droite est orthogonale au plan (critère des deux droites sécantes).</li></ol>` },
    { t: "Calculer la distance d'un point $M$ à un plan", h: R`
<ol><li>Détermine un vecteur normal $\vec n$ au plan.</li><li>Écris le projeté $H=M+t\vec n$ (droite passant par $M$ orthogonale au plan).</li><li>Traduis $H\in\mathcal P$ (au chapitre 12 : on remplace dans l'équation cartésienne ; ici : $\vec{AH}\cdot\vec n=0$ pour un point $A$ du plan) et trouve $t$.</li><li>Distance : $MH=|t|\times\|\vec n\|$.</li></ol>
<p>Variante « par le volume » : si tu connais le volume $V$ d'un tétraèdre et l'aire $\mathcal B$ d'une face, la hauteur relative à cette face vaut $h=\frac{3V}{\mathcal B}$.</p>` },
    { t: "Vérifier qu'un point donné est le projeté orthogonal", h: R`
<p>Au bac, on te donne souvent $H$ : vérifie (1) que $H\in\mathcal P$ et (2) que $\vec{MH}$ est colinéaire à un vecteur normal (ou orthogonal à deux vecteurs non colinéaires du plan). Les deux conditions sont nécessaires.</p>` },
    { t: "Montrer qu'un triangle est rectangle", h: R`
<p>Calcule le produit scalaire des deux vecteurs issus du sommet supposé de l'angle droit : $\vec{HA}\cdot\vec{HB}=0$ ⟹ rectangle en $H$. Ou utilise la réciproque de Pythagore avec les trois longueurs.</p>` }
  ],
  exos: [
    { niv: 1, t: "Calculs de base", enonce: R`<p>Repère orthonormé. $\vec u(2;-1;3)$, $\vec v(1;5;1)$, $A(1;0;2)$, $B(4;-2;8)$.</p><ol><li>Calculer $\vec u\cdot\vec v$. Que peut-on en déduire ?</li><li>Calculer $\|\vec u\|$ et la distance $AB$.</li><li>Déterminer le réel $m$ pour lequel $\vec w(m;2;-2)$ est orthogonal à $\vec u$.</li></ol>`,
      corrige: R`<ol><li>$\vec u\cdot\vec v=2-5+3=0$ : $\vec u$ et $\vec v$ sont orthogonaux.</li><li>$\|\vec u\|=\sqrt{4+1+9}=\sqrt{14}$. $\vec{AB}(3;-2;6)$, $AB=\sqrt{9+4+36}=7$.</li><li>$\vec u\cdot\vec w=2m-2-6=2m-8=0\iff m=4$.</li></ol>` },
    { niv: 1, t: "Angles dans un pavé", enonce: R`<p>$ABCDEFGH$ est un pavé droit avec $AB=4$, $AD=3$, $AE=2$. On se place dans le repère orthonormé d'origine $A$ dont les axes portent $[AB]$, $[AD]$, $[AE]$ (unité : $1$).</p><ol><li>Donner les coordonnées de $C$, $F$, $G$, $H$.</li><li>Calculer la longueur de la diagonale $AG$.</li><li>Calculer $\vec{AC}\cdot\vec{AF}$ puis une mesure, au dixième de degré, de l'angle $\alpha$ du triangle $CAF$ en $A$.</li></ol>`,
      corrige: R`<ol><li>$C(4;3;0)$, $F(4;0;2)$, $G(4;3;2)$, $H(0;3;2)$.</li><li>$AG=\sqrt{16+9+4}=\sqrt{29}\approx5{,}39$.</li><li>$\vec{AC}(4;3;0)$, $\vec{AF}(4;0;2)$ : $\vec{AC}\cdot\vec{AF}=16$. $AC=5$, $AF=\sqrt{20}$. $\cos\alpha=\frac{16}{5\sqrt{20}}\approx0{,}7155$, donc $\alpha\approx44{,}3°$.</li></ol>` },
    { niv: 2, t: "Une droite orthogonale à un plan", enonce: R`<p>Repère orthonormé. $A(1;1;0)$, $B(3;0;1)$, $C(0;2;2)$, $D(4;6;-1)$.</p><ol><li>Montrer que $A$, $B$, $C$ ne sont pas alignés.</li><li>Montrer que la droite $(AD)$ est orthogonale au plan $(ABC)$.</li><li>En déduire la distance du point $D$ au plan $(ABC)$.</li><li>Calculer $\vec{AB}\cdot\vec{AC}$, puis le cosinus et le sinus de l'angle $\alpha$ du triangle $ABC$ en $A$. En déduire l'aire du triangle $ABC$.</li><li>Calculer le volume du tétraèdre $ABCD$.</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(2;-1;1)$, $\vec{AC}(-1;1;2)$ : coordonnées non proportionnelles ($\frac{-1}2\neq\frac1{-1}$). Non colinéaires, donc $A$, $B$, $C$ non alignés.</li><li>$\vec{AD}(3;5;-1)$. $\vec{AD}\cdot\vec{AB}=6-5-1=0$ et $\vec{AD}\cdot\vec{AC}=-3+5-2=0$. $(AD)$ est orthogonale à deux droites sécantes du plan, $(AB)$ et $(AC)$ : elle est orthogonale au plan $(ABC)$.</li><li>$(AD)$ est orthogonale au plan et $A$ est dans le plan : $A$ est le projeté orthogonal de $D$. Distance : $AD=\sqrt{9+25+1}=\sqrt{35}\approx5{,}92$.</li><li>$\vec{AB}\cdot\vec{AC}=-2-1+2=-1$ ; $AB=AC=\sqrt6$. $\cos\alpha=\frac{-1}{6}$ (angle obtus), $\sin\alpha=\sqrt{1-\frac1{36}}=\frac{\sqrt{35}}6$. Aire : $\frac12\times\sqrt6\times\sqrt6\times\frac{\sqrt{35}}6=\frac{\sqrt{35}}2$.</li><li>$V=\frac13\times\frac{\sqrt{35}}2\times\sqrt{35}=\frac{35}6\approx5{,}83$.</li></ol>` },
    { niv: 2, t: "Projeté orthogonal sur une droite", enonce: R`<p>Repère orthonormé. La droite $(d)$ passe par $A(1;0;-1)$ et est dirigée par $\vec u(2;1;2)$. Soit $M(5;3;6)$.</p><ol><li>Le point $M$ appartient-il à $(d)$ ?</li><li>Déterminer les coordonnées du projeté orthogonal $H$ de $M$ sur $(d)$.</li><li>En déduire la distance de $M$ à la droite $(d)$.</li></ol>`,
      corrige: R`<ol><li>$\vec{AM}(4;3;7)$ et $\vec u(2;1;2)$ : $4=2\times2$ mais $3\neq2\times1$. Non colinéaires : $M\notin(d)$.</li><li>$t=\frac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}=\frac{8+3+14}{9}=\frac{25}9$. $H=A+\frac{25}9\vec u=\left(\frac{59}9;\frac{25}9;\frac{41}9\right)$.</li><li>$\vec{HM}\left(-\frac{14}9;\frac29;\frac{13}9\right)$ (on vérifie $\vec{HM}\cdot\vec u=\frac{-28+2+26}9=0$). $MH=\frac{\sqrt{196+4+169}}9=\frac{\sqrt{369}}9=\frac{\sqrt{41}}3\approx2{,}13$.</li></ol>` },
    { niv: 3, t: "Distance et volume dans un tétraèdre (type bac)", enonce: R`<p>Repère orthonormé $(O;\vec i,\vec j,\vec k)$. On considère $A(2;0;0)$, $B(0;3;0)$, $C(0;0;6)$ et $\vec n(3;2;1)$.</p><ol><li>Montrer que $\vec n$ est normal au plan $(ABC)$.</li><li>Soit $H$ le projeté orthogonal de $O$ sur $(ABC)$. Justifier qu'il existe un réel $t$ tel que $\vec{OH}=t\vec n$, puis, en utilisant $\vec{AH}\cdot\vec n=0$, déterminer $t$ et les coordonnées de $H$.</li><li>En déduire la distance du point $O$ au plan $(ABC)$.</li><li>Calculer le volume du tétraèdre $OABC$ en prenant pour base le triangle $OAB$.</li><li>En déduire l'aire du triangle $ABC$.</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(-2;3;0)$ et $\vec{AC}(-2;0;6)$ sont non colinéaires ; $\vec n\cdot\vec{AB}=-6+6=0$ et $\vec n\cdot\vec{AC}=-6+6=0$. Donc $\vec n$ est normal à $(ABC)$.</li><li>$(OH)$ est orthogonale au plan, donc dirigée par $\vec n$ : $\vec{OH}=t\vec n$, $H(3t;2t;t)$. $\vec{AH}(3t-2;2t;t)$ et $\vec{AH}\cdot\vec n=9t-6+4t+t=14t-6=0$, d'où $t=\frac37$ et $H\left(\frac97;\frac67;\frac37\right)$.</li><li>$OH=\frac37\|\vec n\|=\frac37\sqrt{14}=\frac{3\sqrt{14}}7\approx1{,}60$.</li><li>Le triangle $OAB$ est rectangle en $O$, d'aire $\frac{2\times3}2=3$, et la hauteur relative est $OC=6$ (l'axe $(OC)$ est orthogonal au plan $(OAB)$). $V=\frac13\times3\times6=6$.</li><li>Avec la base $ABC$ et la hauteur $OH$ : $6=\frac13\times\mathcal A\times\frac{3\sqrt{14}}7$, donc $\mathcal A=\frac{42}{\sqrt{14}}=3\sqrt{14}\approx11{,}2$. On retrouve l'aire calculée dans la partie 6.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2025, Métropole, 18 juin 2025 (sujet 2), exercice 2, partie A, questions 3 et 4", url: "https://www.apmep.fr/IMG/pdf/Metropole__spe_J2_18_06_2025_DV_2.pdf", h: R`Montrer que $H(-1;0;2)$ est le projeté orthogonal de $S$ sur le plan $(ABC)$, puis « en déduire qu'il n'existe aucun point $M$ du plan $(ABC)$ tel que $SM<\frac{\sqrt{21}}2$ » : c'est exactement la démonstration exigible ($SH=\frac{\sqrt{21}}2$).` },
    { ref: "Bac 2024, Métropole, 19 juin 2024 (sujet 1), exercice 3", url: "https://www.apmep.fr/IMG/pdf/Metropole_J1_spe_19_06_2024_VTFK.pdf", h: R`Vecteur normal au plan $(CAD)$, projeté orthogonal $H$ de $B$ sur ce plan, triangle $ABH$ rectangle en $H$ (aire $\frac{25}4$), hauteur $(CO)$ et volume du tétraèdre $ABCH$, puis distance de $H$ au plan $(ABC)$ par le volume.` },
    { ref: "Bac 2024, Métropole – Antilles-Guyane, 12 septembre 2024 (jour 2), exercice 1", url: "https://www.apmep.fr/IMG/pdf/Spe_J2_12_09_2024_Metropole_DV.pdf", h: R`Dans le cube : vecteurs $\vec{IJ}$ et $\vec{NF}$ orthogonaux, aire du triangle $FIJ$ ($\frac{\sqrt{21}}8$), vecteur normal au plan $(FIJ)$, distance de $H$ au plan $(FIJ)$ ($\frac{5\sqrt{21}}{21}$), volume du tétraèdre $HFIJ$.` },
    { ref: "Bac 2026, Métropole – La Réunion, 8 septembre 2026 (sujet 1), exercice 3, affirmations 2 et 4", url: "https://www.apmep.fr/IMG/pdf/Metropole_J_spe_8osep_2026.pdf", h: R`« La droite $(CD)$ est orthogonale au plan $(ABC)$ » (deux produits scalaires à calculer) et « la distance de $N$ au plan $\mathcal P_2$ est $NH$ » (vérifier que $H$ est bien le projeté orthogonal : dans le plan, et $\vec{NH}$ normal).` }
  ],
  retenir: R`
[def|Produit scalaire]$\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos(\vec u,\vec v)=\frac12\left(\|\vec u+\vec v\|^2-\|\vec u\|^2-\|\vec v\|^2\right)$. Symétrique, bilinéaire.[/]
[thm|Base orthonormée]$\vec u\cdot\vec v=xx'+yy'+zz'$ ; $\|\vec u\|=\sqrt{x^2+y^2+z^2}$ ; $AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}$ ; $\cos(\vec u,\vec v)=\frac{\vec u\cdot\vec v}{\|\vec u\|\|\vec v\|}$.[/]
[prop|Orthogonalité]$\vec u⊥\vec v\iff\vec u\cdot\vec v=0$. Droite ⊥ plan ⟺ orthogonale à deux droites sécantes du plan. Perpendiculaires = orthogonales et sécantes.[/]
[def|Vecteur normal]$\vec n\neq\vec 0$ orthogonal à deux vecteurs non colinéaires du plan. Plan $(A;\vec n)$ : $\vec{AM}\cdot\vec n=0$. Plan médiateur de $[AB]$ : points équidistants de $A$ et $B$.[/]
[thm|Projeté orthogonal]$H$ = point du plan (de la droite) le plus proche de $M$ ; $MA^2=MH^2+HA^2$. Distance $=MH$. Sur $(A;\vec u)$ : $t=\frac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}$.[/]
<p class="stylo">Volume d'un tétraèdre : $\frac13\times$ aire de base $\times$ hauteur. Deux bases ⟹ une distance.</p>`,
  qcm: [
    { q: R`Dans un repère orthonormé, $\vec u(1;-2;2)$ et $\vec v(4;1;-1)$. $\vec u\cdot\vec v=$`, c: ["$0$", "$4$", "$-2$", "$8$"], r: 0, e: R`$4-2-2=0$ : les vecteurs sont orthogonaux.`, ref: "orthonormee" },
    { q: R`$\|\vec u\|$ pour $\vec u(1;-2;2)$ :`, c: ["$1$", "$3$", "$5$", "$9$"], r: 1, e: R`$\sqrt{1+4+4}=3$.`, ref: "orthonormee" },
    { q: R`La formule $\vec u\cdot\vec v=xx'+yy'+zz'$ est valable :`, c: ["dans toute base", "dans une base orthonormée", "seulement si les vecteurs sont orthogonaux", "seulement dans le cube"], r: 1, e: R`Elle repose sur $\vec i\cdot\vec j=0$ et $\vec i\cdot\vec i=1$, etc.`, ref: "orthonormee" },
    { q: R`Dans le cube, les droites $(AE)$ et $(BC)$ sont :`, c: ["perpendiculaires", "orthogonales mais non sécantes", "parallèles", "ni orthogonales ni parallèles"], r: 1, e: R`$\vec{AE}\cdot\vec{AD}=0$ mais elles ne sont pas coplanaires.`, ref: "orthogonalite" },
    { q: R`Pour qu'une droite soit orthogonale à un plan, il suffit qu'elle soit orthogonale à :`, c: ["une droite du plan", "deux droites parallèles du plan", "deux droites sécantes du plan", "un vecteur du plan"], r: 2, e: R`Deux vecteurs non colinéaires de la direction du plan.`, ref: "orthogonalite" },
    { q: R`Cube d'arête $1$. L'angle entre $\vec{AG}$ et $\vec{BH}$ a pour cosinus :`, c: [R`$0$`, R`$\frac13$`, R`$\frac1{\sqrt3}$`, R`$\frac12$`], r: 1, e: R`$\vec{AG}\cdot\vec{BH}=1$ et $AG=BH=\sqrt3$.`, ref: "orthonormee" },
    { q: R`$\vec n$ est normal au plan $\mathcal P$ passant par $A$. $M\in\mathcal P$ si et seulement si :`, c: [R`$\vec{AM}=k\vec n$`, R`$\vec{AM}\cdot\vec n=0$`, R`$AM=\|\vec n\|$`, R`$\vec{AM}\cdot\vec n=1$`], r: 1, e: R`Caractérisation du plan par un point et un vecteur normal.`, ref: "normal" },
    { q: R`Deux plans de vecteurs normaux $\vec n(1;2;-1)$ et $\vec n'(2;-1;0)$ sont :`, c: ["parallèles", "perpendiculaires", "confondus", "ni parallèles ni perpendiculaires"], r: 1, e: R`$\vec n\cdot\vec n'=2-2+0=0$ : normaux orthogonaux.`, ref: "normal" },
    { q: R`Le plan médiateur de $[AB]$ est l'ensemble des points $M$ tels que :`, c: [R`$MA=MB$`, R`$\vec{MA}\cdot\vec{MB}=0$`, R`$M$ est le milieu de $[AB]$`, R`$MA+MB=AB$`], r: 0, e: R`Plan passant par le milieu, normal à $\vec{AB}$ : les points équidistants. ($\vec{MA}\cdot\vec{MB}=0$ décrit une sphère.)`, ref: "normal" },
    { q: R`$H$ projeté orthogonal de $M$ sur $\mathcal P$, $A\in\mathcal P$. Alors :`, c: [R`$MA^2=MH^2+HA^2$`, R`$MA=MH+HA$`, R`$MA\leq MH$`, R`$MH^2=MA^2+AH^2$`], r: 0, e: R`Pythagore dans $MHA$ rectangle en $H$ : c'est la démonstration du BO.`, ref: "projete" },
    { q: R`Projeté de $M$ sur la droite $(A;\vec u)$ : $H=A+t\vec u$ avec $t=$`, c: [R`$\frac{\vec{AM}\cdot\vec u}{\|\vec u\|}$`, R`$\frac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}$`, R`$\vec{AM}\cdot\vec u$`, R`$\frac{AM}{\|\vec u\|}$`], r: 1, e: R`On écrit $\vec{HM}\cdot\vec u=0$ : $\vec{AM}\cdot\vec u-t\|\vec u\|^2=0$.`, ref: "projete" },
    { q: R`Un tétraèdre a pour volume $6$ ; une face a pour aire $9$. La hauteur relative à cette face vaut :`, c: ["$\\frac23$", "$2$", "$\\frac32$", "$18$"], r: 1, e: R`$V=\frac13\mathcal Bh$ donc $h=\frac{3V}{\mathcal B}=\frac{18}9=2$.`, ref: "mesures" },
    { q: R`Cube d'arête $1$ : la distance du sommet $A$ au plan $(BDE)$ vaut :`, c: [R`$1$`, R`$\frac{\sqrt3}3$`, R`$\frac{\sqrt2}2$`, R`$\sqrt3$`], r: 1, e: R`Le projeté est $\left(\frac13;\frac13;\frac13\right)$ sur la diagonale $(AG)$.`, ref: "projete" },
    { q: R`$\vec u\cdot\vec v<0$ signifie que l'angle $(\vec u,\vec v)$ est :`, c: ["droit", "aigu", "obtus", "nul"], r: 2, e: R`Le cosinus est négatif pour un angle compris entre $90°$ et $180°$.`, ref: "orthonormee" }
  ],
  cartes: [
    [R`Produit scalaire (définition)`, R`$\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos(\vec u,\vec v)$`],
    [R`Polarisation`, R`$\vec u\cdot\vec v=\frac12\left(\|\vec u+\vec v\|^2-\|\vec u\|^2-\|\vec v\|^2\right)$`],
    [R`$\vec u\cdot\vec v$ en base orthonormée`, R`$xx'+yy'+zz'$`],
    [R`Distance $AB$ en repère orthonormé`, R`$\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}$`],
    [R`$\vec u⊥\vec v$`, R`$\vec u\cdot\vec v=0$`],
    [R`Orthogonales / perpendiculaires`, R`Perpendiculaires = orthogonales et sécantes.`],
    [R`Droite orthogonale à un plan (critère)`, R`Orthogonale à deux droites sécantes du plan.`],
    [R`Vecteur normal à un plan`, R`Vecteur non nul orthogonal à deux vecteurs non colinéaires du plan.`],
    [R`Plan passant par $A$ normal à $\vec n$`, R`$\{M : \vec{AM}\cdot\vec n=0\}$`],
    [R`Plan médiateur de $[AB]$`, R`Ensemble des points équidistants de $A$ et $B$ ; passe par le milieu, normal à $\vec{AB}$.`],
    [R`Projeté orthogonal : propriété clé`, R`C'est le point le plus proche : $MA^2=MH^2+HA^2\geq MH^2$.`],
    [R`Projeté sur $(A;\vec u)$`, R`$H=A+t\vec u$, $t=\frac{\vec{AM}\cdot\vec u}{\|\vec u\|^2}$`],
    [R`Volume d'un tétraèdre`, R`$\frac13\times\mathcal B\times h$`],
    [R`Angle entre deux grandes diagonales du cube`, R`$\cos\theta=\frac13$, $\theta\approx70{,}5°$`]
  ]
};

/* Animation : le projeté orthogonal est le point le plus proche (démonstration du BO) */
ANIMS.projete3d = {
  titre: "Le projeté orthogonal, point le plus proche",
  vb: [360, 260],
  etapes: [
    { d: 3.5, l: R`Un plan $\mathcal P$, un point $M$ hors du plan et un point $A$ du plan. Quelle est la plus petite distance entre $M$ et un point de $\mathcal P$ ?` },
    { d: 4, l: R`On « laisse tomber » $M$ verticalement, c'est-à-dire orthogonalement au plan : il atteint $\mathcal P$ en $H$, le <b>projeté orthogonal</b> de $M$. Ici $MH=2$.` },
    { d: 6, l: R`Le point $A$ se déplace dans $\mathcal P$, sur un cercle de centre $H$. Le triangle $MHA$ reste rectangle en $H$ : $MA^2=MH^2+HA^2$, donc $MA>MH$ dès que $A\neq H$.` },
    { d: 4.5, l: R`$A$ se rapproche de $H$ : $HA$ diminue et $MA$ descend vers $MH$, sans jamais passer en dessous.` },
    { d: 4, l: R`$MA=MH$ seulement quand $A=H$ : $H$ est le point de $\mathcal P$ le plus proche de $M$, et la <b>distance de $M$ au plan</b> est $MH$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, P = CAV.vue({ ox: 190, oy: 200, s: 56, k: 0.55, a: 38 });
    CAV.poly(S, P, [[-2, -1.6, 0], [2.1, -1.6, 0], [2.1, 1.6, 0], [-2, 1.6, 0]], "a-plein");
    CAV.txt(S, P, [-2, -1.6, 0], "𝒫", "b", "start", 10, -6, { "font-size": 16 });
    var H = [0, 0, 0], M = [0, 0, 2], r0 = 1.5;
    var r = r0, th = -0.5;
    if (k === 2) th = -0.5 + 2 * Math.PI * E(t);
    if (k === 3) r = ANIM.l(r0, 0, E(t));
    if (k === 4) r = 0;
    var A = [r * Math.cos(th), r * Math.sin(th), 0];
    if (k >= 2) { var pts = []; for (var i = 0; i <= 48; i++) { var a = 2 * Math.PI * i / 48; pts.push(P(r0 * Math.cos(a), r0 * Math.sin(a), 0)); } S.px.path("M" + pts.map(function (p) { return p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("L"), "a-craie"); }
    var desc = k === 1 ? E(ANIM.p(t, 0, 0.7)) : k >= 2 ? 1 : 0;
    if (k >= 1) {
      var bas = CAV.lerp3(M, H, desc);
      CAV.trait(S, P, M, bas, "g-c", { "stroke-width": 2.6 });
      if (desc > 0.98) { CAV.droit(S, P, H, [1, 0, 0], [0, 0, 1], 0.22); CAV.pt(S, P, H, "g-pt", 4.5); CAV.txt(S, P, H, "H", "b", "end", -8, 14); }
      else CAV.pt(S, P, bas, "g-pt", 3);
    }
    if (r > 0.02) {
      CAV.trait(S, P, M, A, "g-c2", { "stroke-width": 2.4 });
      if (k >= 2) CAV.trait(S, P, H, A, "g-c3", { "stroke-width": 2.2 });
      CAV.pt(S, P, A, "g-pt2", 4.5); CAV.txt(S, P, A, "A", "r", "start", 8, 12);
    }
    CAV.pt(S, P, M, "g-pt2", 4.5); CAV.txt(S, P, M, "M", "r", "start", 8, -2);
    var MA = Math.sqrt(4 + r * r), nf = ANIM.nf;
    var l1 = k === 0 ? "MA = " + nf(MA, 2) : "MH = 2  ·  HA = " + nf(r, 2), l2 = k === 0 ? "" : "MA = √(MH² + HA²) = " + nf(MA, 2);
    S.px.txt(8, 24, l1, "b", "start", { "font-size": 13 });
    if (l2) S.px.txt(8, 44, l2, "r", "start", { "font-size": 13 });
    if (k >= 4) S.px.math(4, 52, 144, 34, R`$d(M;\mathcal P)=MH$`, { opacity: E(t) });
  }
};

/* Animation : le produit scalaire par projection, dans le cube */
ANIMS.projCube = {
  titre: R`Produit scalaire et projection dans le cube`,
  vb: [360, 250],
  etapes: [
    { d: 4, l: R`Cube d'arête $1$, repère orthonormé $(A;\vec{AB},\vec{AD},\vec{AE})$. On cherche $\vec{AB}\cdot\vec{AG}$.` },
    { d: 4.5, l: R`$(AB)$ est orthogonale à la face $BCGF$, donc à $(BG)$ : le projeté orthogonal de $G$ sur $(AB)$ est $B$. Ainsi $\vec{AB}\cdot\vec{AG}=\vec{AB}\cdot\vec{AB}=AB^2=1$.` },
    { d: 6, l: R`Faisons glisser $M$ sur toute la face $BCGF$ : son projeté sur $(AB)$ reste $B$. En coordonnées, $M(1;y;z)$ et $\vec{AB}\cdot\vec{AM}=1\times1+0\times y+0\times z=1$ : le produit ne change pas.` },
    { d: 5.5, l: R`Si $M$ recule vers la face $ADHE$, son projeté $H$ recule sur $[AB]$ : $\vec{AB}\cdot\vec{AM}=AB\times AH=x_M$. Sur la face $ADHE$, il vaut $0$ : $\vec{AM}$ est orthogonal à $\vec{AB}$.` },
    { d: 4, l: R`Les points $M$ qui donnent le même produit scalaire avec $\vec{AB}$ forment un plan orthogonal à $(AB)$ : ici les plans d'équation $x=c$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = ANIM.p, nf = ANIM.nf, P = CAV.vue({ ox: 30, oy: 222, s: 126, k: 0.5, a: 40 });
    var A = [0, 0, 0], B = [1, 0, 0], C = [1, 1, 0], D = [0, 1, 0], Ee = [0, 0, 1], F = [1, 0, 1], G = [1, 1, 1], H = [0, 1, 1];
    function n2(x) { return nf(x, 2).replace(",", "{,}"); }
    function tranche(x, cls, at) { CAV.poly(S, P, [[x, 0, 0], [x, 1, 0], [x, 1, 1], [x, 0, 1]], cls, at); }
    if (k >= 1 && k <= 2) tranche(1, "a-plein2", { opacity: k === 1 ? E(p(t, 0, 0.4)) : 1 });
    [[A, B], [B, C], [B, F], [Ee, F], [F, G], [G, H], [H, Ee], [A, Ee], [C, G]].forEach(function (s) { CAV.seg(S, P, s[0], s[1], false, { opacity: 0.55 }); });
    [[A, D], [D, C], [D, H]].forEach(function (s) { CAV.seg(S, P, s[0], s[1], true, { opacity: 0.55 }); });
    var lab = { A: [A, -8, 14], B: [B, 8, 14], C: [C, 12, 6], D: [D, -10, -4], E: [Ee, -10, -2], F: [F, 10, 14], G: [G, 10, -4], H: [H, -6, -8] };
    Object.keys(lab).forEach(function (n) { CAV.txt(S, P, lab[n][0], n, "", "middle", lab[n][1], lab[n][2]); });
    var X0 = 222, W0 = 136;
    if (k === 3) { var s3 = ANIM.l(1, 0, E(p(t, 0, 0.8))); tranche(s3, "a-plein"); }
    if (k === 4) [0, 0.5, 1].forEach(function (x, i) { var o = E(p(t, 0.15 * i, 0.15 * i + 0.4)); tranche(x, "a-plein", { opacity: 0.4 + 0.6 * o }); CAV.txt(S, P, [x, 0.5, 1], "= " + nf(x, 1), "b", "middle", 0, -6, { opacity: o }); });
    CAV.fleche(S, P, A, B, k === 0 ? E(p(t, 0, 0.4)) : 1, "g-c", { "stroke-width": 3.2 });
    if (k <= 1) {
      CAV.fleche(S, P, A, G, k === 0 ? E(p(t, 0.3, 0.8)) : 1, "g-c", { "stroke-width": 2.6, style: "stroke:var(--encre)" });
      S.px.math(X0, 30, W0, 34, R`$\vec{AB}\cdot\vec{AG}=\ ?$`, { opacity: k === 0 ? E(p(t, 0.6, 1)) : 1 });
      if (k === 1) {
        var o1 = E(p(t, 0.35, 0.7));
        CAV.trait(S, P, G, B, "g-as", { opacity: o1 });
        CAV.droit(S, P, B, [-1, 0, 0], [0, Math.SQRT1_2, Math.SQRT1_2], 0.09);
        S.px.math(X0, 72, W0, 34, R`$\vec{AB}\cdot\vec{AG}$`, { opacity: o1 });
        S.px.math(X0, 106, W0, 34, R`$=AB^2=1$`, { opacity: E(p(t, 0.6, 0.9)) });
      }
      return;
    }
    var M, Hh;
    if (k === 2) { var u = 2 * Math.PI * E(t); M = [1, 0.5 + 0.38 * Math.sin(u), 0.5 + 0.38 * Math.cos(u)]; Hh = B; }
    else if (k === 3) { M = [s3, 0.6, 0.7]; Hh = [s3, 0, 0]; }
    else { M = [0.5, 0.6, 0.7]; Hh = [0.5, 0, 0]; }
    if (k >= 3) CAV.trait(S, P, A, Hh, "g-c", { "stroke-width": 5, opacity: 0.45 });
    CAV.trait(S, P, M, Hh, "g-as");
    CAV.fleche(S, P, A, M, 1, "g-c3", { "stroke-width": 2.6 });
    CAV.pt(S, P, M, "g-pt2", 4.5); CAV.txt(S, P, M, "M", "r", "start", 7, -5);
    CAV.pt(S, P, Hh, "g-pt", 4); if (k >= 3) CAV.txt(S, P, Hh, "H", "b", "middle", 0, 16);
    S.px.math(X0, 30, W0, 30, "$M(" + n2(M[0]) + ";" + n2(M[1]) + ";" + n2(M[2]) + ")$");
    S.px.math(X0, 66, W0, 30, R`$\vec{AB}\cdot\vec{AM}$`);
    S.px.math(X0, 98, W0, 30, "$=" + n2(M[0]) + "$");
    if (k === 3 && t > 0.8) S.px.math(X0, 132, W0, 30, R`$\vec{AM}\perp\vec{AB}$`, { opacity: E(p(t, 0.8, 1)) });
  }
};
