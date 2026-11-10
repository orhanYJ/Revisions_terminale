/* ---------- Chapitre 10 : vecteurs, droites et plans de l'espace ---------- */
var CH10 = {
  id: "ch10", num: 10, statut: "ok", partie: "Algèbre et géométrie", titre: "Vecteurs, droites et plans de l'espace", court: "Vecteurs de l'espace",
  sous: "Le calcul vectoriel du plan, avec une dimension de plus : directions, combinaisons, bases et positions relatives.",
  resume: "Combinaisons linéaires, droites et plans, coplanarité, bases et repères, positions relatives.",
  essentiel: [
    R`Un vecteur de l'espace se définit comme dans le plan (direction, sens, longueur) ; la relation de Chasles $\vec{AB}+\vec{BC}=\vec{AC}$ reste vraie. On fabrique des vecteurs par <b>combinaisons linéaires</b> $a\vec u+b\vec v+c\vec w$.`,
    R`Une <b>droite</b> est déterminée par un point $A$ et un vecteur directeur $\vec u\neq\vec 0$ : $M\in(d)\iff\vec{AM}=t\vec u$ pour un réel $t$. Trois points sont alignés si et seulement si deux vecteurs qu'ils forment sont colinéaires.`,
    R`Un <b>plan</b> est déterminé par un point $A$ et deux vecteurs <b>non colinéaires</b> $\vec u,\vec v$ : $M\in\mathcal P\iff\vec{AM}=s\vec u+t\vec v$. Trois vecteurs sont <b>coplanaires</b> si l'un est combinaison linéaire des deux autres.`,
    R`Trois vecteurs <b>non coplanaires</b> forment une <b>base</b> : tout vecteur s'écrit de façon unique $x\vec i+y\vec j+z\vec k$. Avec une origine $O$, on obtient un repère et des coordonnées $(x;y;z)$.`,
    R`Deux droites de l'espace peuvent être <b>sécantes, parallèles ou non coplanaires</b>. Une droite et un plan : sécants ou parallèles (la droite peut être incluse). Deux plans : sécants selon une droite, ou parallèles.`
  ],
  attendus: [
    R`Représenter des combinaisons linéaires de vecteurs donnés ; exploiter une figure pour exprimer un vecteur comme combinaison linéaire d'autres vecteurs.`,
    R`Décrire la position relative de deux droites, d'une droite et d'un plan, de deux plans.`,
    R`Lire sur une figure si deux vecteurs d'un plan, trois vecteurs de l'espace, forment une base ; lire la décomposition d'un vecteur dans une base.`,
    R`Étudier géométriquement des problèmes simples de configurations dans l'espace : alignement, colinéarité, parallélisme, coplanarité.`,
    R`Supports privilégiés : le cube, le pavé, le tétraèdre. Aucune démonstration ni aucun algorithme n'est exigé dans ce chapitre.`
  ],
  premiere: R`
<ul><li><b>Vecteurs du plan</b> : $\vec{AB}=\vec{DC}\iff ABCD$ est un parallélogramme (éventuellement aplati) ; relation de Chasles ; $\vec{AB}=-\vec{BA}$.</li>
<li><b>Colinéarité dans le plan</b> : $\vec u(x;y)$ et $\vec v(x';y')$ sont colinéaires si et seulement si $xy'-x'y=0$ (déterminant nul).</li>
<li><b>Coordonnées</b> : $\vec{AB}(x_B-x_A;y_B-y_A)$ ; milieu $I$ de $[AB]$ : $\left(\frac{x_A+x_B}2;\frac{y_A+y_B}2\right)$.</li>
<li><b>Solides du collège</b> : cube, pavé droit, prisme, pyramide, tétraèdre ; volume d'une pyramide $V=\frac13\times\mathcal B\times h$.</li></ul>
[piege|Ce qui change dans l'espace]Dans le plan, deux droites non parallèles se coupent toujours. Dans l'espace, non : elles peuvent ne pas être dans un même plan. Et le critère $xy'-x'y=0$ ne suffit plus pour trois coordonnées : il faut vérifier la proportionnalité sur les trois.[/]`,
  cours: [
    { id: "vecteurs", titre: "Vecteurs de l'espace et translations", html: R`
<p>Tout ce que tu sais des vecteurs du plan reste vrai dans l'espace : on travaille simplement dans un monde à trois dimensions. Le support du chapitre : le <b>cube</b> $ABCDEFGH$, base $ABCD$ en bas, $EFGH$ au-dessus, $E$ au-dessus de $A$, $F$ au-dessus de $B$, etc.</p>
<div data-anim="cubeChasles"></div>
[def|Vecteur, translation]À tout couple de points $(A;B)$ on associe le vecteur $\vec{AB}$ : la <b>translation</b> de vecteur $\vec{AB}$ transforme $A$ en $B$. Deux vecteurs sont égaux s'ils ont même direction, même sens et même longueur : $\vec{AB}=\vec{DC}$ si et seulement si $ABCD$ est un parallélogramme (éventuellement aplati). Le vecteur nul $\vec 0=\vec{AA}$.[/]
[ex|Dans le cube]Les faces sont des carrés, donc des parallélogrammes : $\vec{AB}=\vec{DC}=\vec{EF}=\vec{HG}$, et $\vec{AE}=\vec{BF}=\vec{CG}=\vec{DH}$. Le quadrilatère $ACGE$ est un rectangle (une « tranche diagonale » du cube) : $\vec{AC}=\vec{EG}$.[/]
[prop|Relation de Chasles]Pour tous points $A$, $B$, $C$ de l'espace : $\vec{AB}+\vec{BC}=\vec{AC}$. En particulier $\vec{AB}+\vec{BA}=\vec 0$, donc $\vec{BA}=-\vec{AB}$.[/]
[ex|Un chemin le long des arêtes]$\vec{AG}=\vec{AB}+\vec{BC}+\vec{CG}$ : on va de $A$ à $G$ en suivant trois arêtes. Comme $\vec{BC}=\vec{AD}$ et $\vec{CG}=\vec{AE}$, on obtient $\vec{AG}=\vec{AB}+\vec{AD}+\vec{AE}$.[/]` },
    { id: "combinaisons", titre: "Combinaisons linéaires de vecteurs", html: R`
[def|Combinaison linéaire]Une <b>combinaison linéaire</b> des vecteurs $\vec u$, $\vec v$, $\vec w$ est un vecteur de la forme $a\vec u+b\vec v+c\vec w$, où $a$, $b$, $c$ sont des réels. Les règles de calcul sont celles du plan : $k(\vec u+\vec v)=k\vec u+k\vec v$, $(a+b)\vec u=a\vec u+b\vec u$, $a(b\vec u)=(ab)\vec u$.[/]
[ex|Le milieu d'une arête]Soit $I$ le milieu de $[FG]$. Chemin $A\to B\to F\to I$ : $\vec{AI}=\vec{AB}+\vec{BF}+\vec{FI}=\vec{AB}+\vec{AE}+\frac12\vec{FG}=\vec{AB}+\frac12\vec{AD}+\vec{AE}$.[/]
[ex|Le centre du cube]Soit $\Omega$ le milieu de la grande diagonale $[AG]$ : $\vec{A\Omega}=\frac12\vec{AG}=\frac12\vec{AB}+\frac12\vec{AD}+\frac12\vec{AE}$. On vérifie de même que $\Omega$ est le milieu de $[BH]$, $[CE]$ et $[DF]$ : les quatre grandes diagonales se coupent au centre du cube.[/]
[meth|Exprimer un vecteur en fonction d'autres]<ol><li>Relie l'origine à l'extrémité par un <b>chemin</b> de points connus (relation de Chasles).</li><li>Remplace chaque morceau par un vecteur égal parmi ceux qu'on te donne (faces parallélogrammes, milieux : $\vec{FI}=\frac12\vec{FG}$).</li><li>Regroupe les termes.</li></ol>[/]
[ex|Dans un tétraèdre]$ABCD$ est un tétraèdre, $I$ le milieu de $[BC]$ et $G$ le centre de gravité du triangle $BCD$, tel que $\vec{DG}=\frac23\vec{DI}$. Alors $\vec{AI}=\frac12\vec{AB}+\frac12\vec{AC}$, puis
$$\vec{AG}=\vec{AD}+\frac23\vec{DI}=\vec{AD}+\frac23\left(\vec{AI}-\vec{AD}\right)=\frac13\vec{AB}+\frac13\vec{AC}+\frac13\vec{AD}.$$[/]` },
    { id: "droites", titre: "Droites de l'espace, colinéarité, alignement", html: R`
[def|Vecteur directeur]Un <b>vecteur directeur</b> d'une droite $(d)$ est un vecteur non nul $\vec u=\vec{AB}$, où $A$ et $B$ sont deux points distincts de $(d)$. Deux vecteurs $\vec u$ et $\vec v$ sont <b>colinéaires</b> s'il existe un réel $k$ tel que $\vec v=k\vec u$ (ou $\vec u=k\vec v$) ; le vecteur nul est colinéaire à tout vecteur.[/]
[thm|Caractérisation d'une droite]La droite $(d)$ passant par $A$ et de vecteur directeur $\vec u$ est l'ensemble des points $M$ tels que $\vec{AM}=t\vec u$, $t$ décrivant $\R$.[/]
[prop|Alignement et parallélisme]<ul><li>$A$, $B$, $C$ sont <b>alignés</b> si et seulement si $\vec{AB}$ et $\vec{AC}$ sont colinéaires.</li><li>Deux droites sont <b>parallèles</b> si et seulement si leurs vecteurs directeurs sont colinéaires.</li></ul>[/]
[ex|Le centre du cube est sur la diagonale]Avec $\Omega$ défini par $\vec{A\Omega}=\frac12(\vec{AB}+\vec{AD}+\vec{AE})$ et $\vec{AG}=\vec{AB}+\vec{AD}+\vec{AE}$ : $\vec{AG}=2\vec{A\Omega}$. Les vecteurs sont colinéaires, donc $A$, $\Omega$, $G$ sont alignés.[/]
[ex|Alignés ou pas ?]Dans le cube, $K$ est défini par $\vec{EK}=\frac13\vec{EC}$, et $J$ est le centre de la face $ABFE$ (milieu de $[EB]$). On a $\vec{EC}=\vec{AB}+\vec{AD}-\vec{AE}$, donc $\vec{EK}=\frac13\vec{AB}+\frac13\vec{AD}-\frac13\vec{AE}$. Et $\vec{EJ}=\frac12\vec{EB}=\frac12\vec{AB}-\frac12\vec{AE}$. Les vecteurs $\vec{EK}$ et $\vec{EJ}$ ne sont pas colinéaires (la composante sur $\vec{AD}$ de $\vec{EJ}$ est nulle, pas celle de $\vec{EK}$) : $E$, $J$, $K$ ne sont pas alignés.[/]` },
    { id: "plans", titre: "Plans de l'espace, direction, coplanarité", html: R`
[def|Plan, direction d'un plan]Soit $A$ un point et $\vec u$, $\vec v$ deux vecteurs <b>non colinéaires</b>. L'ensemble des points $M$ tels que $\vec{AM}=s\vec u+t\vec v$, avec $s,t\in\R$, est un <b>plan</b> : le plan passant par $A$ et dirigé par $\vec u$ et $\vec v$. Le couple $(\vec u,\vec v)$ en est une <b>base</b> ; l'ensemble des combinaisons $s\vec u+t\vec v$ est la <b>direction</b> du plan.[/]
<p>Exemple : le plan $(ABC)$ est le plan passant par $A$ et dirigé par $\vec{AB}$ et $\vec{AC}$ (si $A$, $B$, $C$ ne sont pas alignés). Deux plans qui ont la même direction sont parallèles.</p>
[def|Vecteurs coplanaires]Trois vecteurs $\vec u$, $\vec v$, $\vec w$ sont <b>coplanaires</b> si, en les représentant à partir d'un même point $O$, les quatre points $O$, $O+\vec u$, $O+\vec v$, $O+\vec w$ sont dans un même plan. Si $\vec u$ et $\vec v$ ne sont pas colinéaires, cela revient à : il existe deux réels $a$, $b$ tels que $\vec w=a\vec u+b\vec v$.[/]
[prop|Quatre points coplanaires]$A$, $B$, $C$, $D$ (avec $A$, $B$, $C$ non alignés) sont <b>coplanaires</b> si et seulement si il existe des réels $a$, $b$ tels que $\vec{AD}=a\vec{AB}+b\vec{AC}$.[/]
[ex|Coplanaires ou non ?]Dans le cube : $\vec{AC}=\vec{AB}+\vec{AD}$, donc $\vec{AB}$, $\vec{AD}$, $\vec{AC}$ sont coplanaires (ils sont tous dans la face $ABCD$). En revanche $\vec{AB}$, $\vec{AD}$, $\vec{AE}$ ne le sont pas : $\vec{AE}$ « sort » de la face du bas.[/]
[ex|Le tétraèdre caché dans le cube]Les points $B$, $D$, $E$, $G$ sont-ils coplanaires ? $\vec{BD}=\vec{AD}-\vec{AB}$, $\vec{BE}=\vec{AE}-\vec{AB}$, $\vec{BG}=\vec{AD}+\vec{AE}$. Si $\vec{BG}=a\vec{BD}+b\vec{BE}$, alors $\vec{AD}+\vec{AE}=-(a+b)\vec{AB}+a\vec{AD}+b\vec{AE}$. Par unicité de la décomposition (partie 5) : $a=1$, $b=1$ et $a+b=0$. Impossible : les quatre points ne sont pas coplanaires. $BDEG$ est un tétraèdre (régulier : ses six arêtes sont des diagonales de faces).[/]
[ex|Six milieux dans un même plan]Soit $I$, $J$, $K$, $L$ les milieux de $[AB]$, $[BC]$, $[CG]$, $[GH]$. $\vec{IL}=\vec{AD}+\vec{AE}$ et $\vec{JK}=\frac12\vec{BG}=\frac12(\vec{AD}+\vec{AE})$. Donc $\vec{IL}=2\vec{JK}$ : les droites $(IL)$ et $(JK)$ sont parallèles, donc contenues dans un même plan : $I$, $J$, $K$, $L$ sont coplanaires. (Avec les milieux de $[HE]$ et $[EA]$, on obtient un hexagone régulier : la section du cube par le plan médiateur de la grande diagonale $[DF]$.)[/]` },
    { id: "bases", titre: "Bases, repères et coordonnées", html: R`
[def|Base, repère]Trois vecteurs $\vec i$, $\vec j$, $\vec k$ <b>non coplanaires</b> forment une <b>base</b> de l'espace. Un point $O$ et une base forment un <b>repère</b> $(O;\vec i,\vec j,\vec k)$.[/]
[thm|Décomposition dans une base]Si $(\vec i,\vec j,\vec k)$ est une base, pour tout vecteur $\vec u$ il existe un <b>unique</b> triplet $(x;y;z)$ de réels tel que $\vec u=x\vec i+y\vec j+z\vec k$ : ce sont les <b>coordonnées</b> de $\vec u$. Les coordonnées du point $M$ dans le repère $(O;\vec i,\vec j,\vec k)$ sont celles de $\vec{OM}$.[/]
[prop|Calculs en coordonnées]Avec $A(x_A;y_A;z_A)$, $B(x_B;y_B;z_B)$ :
<ul><li>$\vec{AB}(x_B-x_A;y_B-y_A;z_B-z_A)$ ; $\vec u+\vec v$ et $k\vec u$ se calculent coordonnée par coordonnée ;</li><li>milieu de $[AB]$ : $\left(\frac{x_A+x_B}2;\frac{y_A+y_B}2;\frac{z_A+z_B}2\right)$ ;</li><li>$\vec u(x;y;z)$ et $\vec v(x';y';z')$ sont colinéaires si et seulement si leurs coordonnées sont <b>proportionnelles</b> (il existe $k$ avec $x'=kx$, $y'=ky$, $z'=kz$, ou l'inverse).</li></ul>[/]
[ex|Le cube en coordonnées]Dans le repère $(A;\vec{AB},\vec{AD},\vec{AE})$ : $A(0;0;0)$, $B(1;0;0)$, $C(1;1;0)$, $D(0;1;0)$, $E(0;0;1)$, $F(1;0;1)$, $G(1;1;1)$, $H(0;1;1)$. Le centre $\Omega\left(\frac12;\frac12;\frac12\right)$, le milieu $I$ de $[FG]$ : $\left(1;\frac12;1\right)$, ce qui confirme $\vec{AI}=\vec{AB}+\frac12\vec{AD}+\vec{AE}$.[/]
[ex|Une base qui n'est pas « droite »]Dans le tétraèdre $ABCD$, $(\vec{AB},\vec{AC},\vec{AD})$ est une base (les quatre points ne sont pas coplanaires). Dans le repère $(A;\vec{AB},\vec{AC},\vec{AD})$, le centre de gravité $G$ de $BCD$ a pour coordonnées $\left(\frac13;\frac13;\frac13\right)$ (partie 2). La base n'a pas besoin d'être orthogonale : les angles et longueurs viendront au chapitre 11.[/]
[piege|Colinéarité en dimension 3]$\vec u(1;2;3)$ et $\vec v(2;4;5)$ : $1\times4-2\times2=0$, mais les vecteurs ne sont pas colinéaires ($\frac21=\frac42\neq\frac53$). Vérifie la proportionnalité sur les <b>trois</b> coordonnées.[/]
[ex|Trois vecteurs forment-ils une base ? (bac, Métropole, 8 septembre 2026)]$\vec u(1;0;2)$, $\vec v(0;1;3)$, $\vec w(2;1;0)$. Cherchons $a$, $b$ tels que $\vec w=a\vec u+b\vec v$ : la 1<sup>re</sup> coordonnée donne $a=2$, la 2<sup>e</sup> donne $b=1$, et la 3<sup>e</sup> devrait valoir $2a+3b=7$, or elle vaut $0$. Impossible ; et $\vec u$, $\vec v$ ne sont pas colinéaires. Donc $\vec u$, $\vec v$, $\vec w$ ne sont pas coplanaires : ils forment une base. L'affirmation « ils forment une base » est vraie.[/]` },
    { id: "positions", titre: "Positions relatives de droites et de plans", html: R`
<div class="tab-wrap"><table><tr><th>Objets</th><th>Positions possibles</th><th>Intersection</th></tr>
<tr><td rowspan="2">Deux droites</td><td><b>coplanaires</b> : sécantes, ou parallèles (strictement ou confondues)</td><td>un point ; vide ; la droite</td></tr>
<tr><td><b>non coplanaires</b> : ni parallèles, ni sécantes</td><td>vide</td></tr>
<tr><td>Une droite et un plan</td><td>sécants ; ou parallèles (droite strictement parallèle, ou incluse)</td><td>un point ; vide ; la droite</td></tr>
<tr><td>Deux plans</td><td>sécants ; ou parallèles (strictement ou confondus)</td><td>une droite ; vide ; le plan</td></tr></table></div>
<div data-anim="positions3d"></div>
[ex|Dans le cube]$(AB)$ et $(CG)$ ne sont ni parallèles ni sécantes : elles sont <b>non coplanaires</b>. $(EG)$ et $(AC)$ sont parallèles ($\vec{EG}=\vec{AC}$). $(AG)$ coupe le plan $(EFG)$ en $G$. Les plans $(ABC)$ et $(EFG)$ sont parallèles ; les plans $(ABC)$ et $(BCG)$ sont sécants selon la droite $(BC)$.[/]
[prop|Parallélisme d'une droite et d'un plan]Une droite est parallèle à un plan si et seulement si elle est parallèle à une droite de ce plan (son vecteur directeur est dans la direction du plan).[/]
[prop|Plans parallèles]<ul><li>Si deux droites <b>sécantes</b> d'un plan $\mathcal P$ sont parallèles à un plan $\mathcal Q$, alors $\mathcal P$ et $\mathcal Q$ sont parallèles.</li><li>Si deux plans sont parallèles, tout plan qui coupe l'un coupe l'autre, et les deux droites d'intersection sont <b>parallèles</b>.</li></ul>[/]
[thm|Théorème du toit]Si $(d_1)\subset\mathcal P_1$ et $(d_2)\subset\mathcal P_2$ sont deux droites parallèles, et si les plans $\mathcal P_1$ et $\mathcal P_2$ sont sécants selon une droite $(\Delta)$, alors $(\Delta)$ est parallèle à $(d_1)$ et à $(d_2)$.[/]
[ex|Section d'un cube par un plan]On coupe le cube par le plan $(IJK)$, où $I$, $J$, $K$ sont les milieux de $[AB]$, $[BC]$ et $[CG]$. Le segment $[IJ]$ est la trace sur la face du bas. La face du haut $EFGH$ est parallèle à celle du bas : la trace du plan sur elle est parallèle à $(IJ)$, passe par le milieu $L$ de $[GH]$ (car $\vec{IL}=2\vec{JK}$, partie 4) et aboutit au milieu $M$ de $[HE]$. On complète avec le milieu $N$ de $[EA]$ : la section est l'hexagone $IJKLMN$.[/]
<p><span class="tag hp">Pour aller plus loin</span> Le programme propose en approfondissement le <b>barycentre</b> : pour des réels $a$, $b$ de somme non nulle, il existe un unique point $G$ tel que $a\vec{GA}+b\vec{GB}=\vec 0$. Le milieu est le barycentre de $(A;1)$, $(B;1)$, le centre de gravité d'un triangle celui des trois sommets affectés du même poids. Non exigible.</p>` }
  ],
  pieges: [
    { t: "« Pas parallèles » ne veut pas dire « sécantes »", h: R`Dans l'espace, deux droites qui ne se coupent pas peuvent aussi ne pas être parallèles : elles sont <b>non coplanaires</b> (comme $(AB)$ et $(CG)$ dans le cube).` },
    { t: "Deux vecteurs ne font pas une base de l'espace", h: R`Il faut <b>trois</b> vecteurs, et non coplanaires. Deux vecteurs non colinéaires forment une base d'un <b>plan</b> seulement.` },
    { t: "Deux à deux non colinéaires ≠ non coplanaires", h: R`$\vec{AB}$, $\vec{AD}$, $\vec{AC}$ sont deux à deux non colinéaires, mais coplanaires ($\vec{AC}=\vec{AB}+\vec{AD}$). Ils ne forment pas une base.` },
    { t: "Une droite parallèle à un plan peut être dedans", h: R`« Parallèle » inclut le cas où la droite est contenue dans le plan. Pour « strictement parallèle », vérifie qu'un point de la droite n'est pas dans le plan.` },
    { t: "Colinéarité : les trois coordonnées", h: R`Le test $xy'-x'y=0$ du plan ne suffit pas : $(1;2;3)$ et $(2;4;5)$ le vérifient sur les deux premières coordonnées sans être colinéaires.` },
    { t: "Le théorème du toit demande deux plans sécants", h: R`Si les deux plans sont parallèles, il n'y a pas de droite d'intersection : le théorème ne s'applique pas.` }
  ],
  demos: [
    { bo: false, t: "Unicité de la décomposition dans une base", h: R`
<p>Soit $(\vec i,\vec j,\vec k)$ une base et supposons $\vec u=x\vec i+y\vec j+z\vec k=x'\vec i+y'\vec j+z'\vec k$. Alors $(x-x')\vec i+(y-y')\vec j+(z-z')\vec k=\vec 0$.</p>
<p>Si $z\neq z'$, on peut diviser : $\vec k=-\frac{x-x'}{z-z'}\vec i-\frac{y-y'}{z-z'}\vec j$, donc $\vec k$ serait combinaison linéaire de $\vec i$ et $\vec j$ : les trois vecteurs seraient coplanaires, ce qui est exclu. Donc $z=z'$.</p>
<p>Il reste $(x-x')\vec i+(y-y')\vec j=\vec 0$. Si $y\neq y'$, $\vec j$ serait colinéaire à $\vec i$, et les trois vecteurs seraient encore coplanaires. Donc $y=y'$, puis $(x-x')\vec i=\vec 0$ avec $\vec i\neq\vec 0$, donc $x=x'$.</p>
<p class="stylo">C'est cette unicité qui permet d'« identifier les coefficients » dans les exemples de coplanarité.</p>` },
    { bo: false, t: "Le théorème du toit", h: R`
<p>Soit $\vec u$ un vecteur directeur commun de $(d_1)$ et $(d_2)$ (elles sont parallèles). Comme $(d_1)\subset\mathcal P_1$, $\vec u$ est dans la direction de $\mathcal P_1$ ; de même, $\vec u$ est dans la direction de $\mathcal P_2$.</p>
<p>Soit $A$ un point de $(\Delta)$ et $(\delta)$ la droite passant par $A$ et dirigée par $\vec u$. Comme $A\in\mathcal P_1$ et $\vec u$ dirige $\mathcal P_1$, la droite $(\delta)$ est contenue dans $\mathcal P_1$ ; de même, elle est contenue dans $\mathcal P_2$. Donc $(\delta)\subset\mathcal P_1\cap\mathcal P_2=(\Delta)$.</p>
<p>Deux droites dont l'une est incluse dans l'autre sont égales : $(\Delta)=(\delta)$, qui est dirigée par $\vec u$. Donc $(\Delta)$ est parallèle à $(d_1)$ et à $(d_2)$.</p>` },
    { bo: false, t: "Trois points alignés : pourquoi la colinéarité suffit", h: R`
<p>Supposons $A\neq B$ et $\vec{AC}=k\vec{AB}$. La droite $(AB)$ est l'ensemble des points $M$ tels que $\vec{AM}=t\vec{AB}$ ; avec $t=k$, on obtient $M=C$. Donc $C\in(AB)$.</p>
<p>Réciproquement, si $C\in(AB)$, la caractérisation de la droite donne un réel $t$ tel que $\vec{AC}=t\vec{AB}$ : les vecteurs sont colinéaires.</p>` }
  ],
  algos: [
    { bo: false, t: "Tester la colinéarité de deux vecteurs", code: `def colineaires(u, v):
    # les trois « déterminants » 2x2 doivent être nuls
    x, y, z = u
    a, b, c = v
    return x*b - y*a == 0 and x*c - z*a == 0 and y*c - z*b == 0

print(colineaires((1, 2, 3), (2, 4, 6)))
print(colineaires((1, 2, 3), (2, 4, 5)))
print(colineaires((0, 0, 0), (5, -1, 2)))`, sortie: `True
False
True`,
      apres: R`<p>Les trois produits en croix nuls signifient que les coordonnées sont proportionnelles. Le vecteur nul est colinéaire à tout vecteur, comme le dit la définition.</p>` },
    { bo: false, t: "Quatre points sont-ils coplanaires ?", code: `from fractions import Fraction as Fr

def vec(A, B):
    return [B[i] - A[i] for i in range(3)]

def coplanaires(A, B, C, D):
    u, v, w = vec(A, B), vec(A, C), vec(A, D)
    # on cherche a, b avec w = a*u + b*v sur deux coordonnées
    for (i, j, k) in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        det = u[i]*v[j] - u[j]*v[i]
        if det != 0:
            a = Fr(w[i]*v[j] - w[j]*v[i], det)
            b = Fr(u[i]*w[j] - u[j]*w[i], det)
            # la troisième coordonnée décide
            return a*u[k] + b*v[k] == w[k], a, b
    return None   # A, B, C alignés

print(coplanaires((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)))
print(coplanaires((0, 0, 0), (1, 0, 0), (0, 1, 0), (2, 3, 0)))`, sortie: `(False, Fraction(1, 1), Fraction(-1, 1))
(True, Fraction(2, 1), Fraction(3, 1))`,
      apres: R`<p>Les coordonnées sont celles du cube dans le repère $(A;\vec{AB},\vec{AD},\vec{AE})$ : $B$, $D$, $E$, $G$ ne sont pas coplanaires (tétraèdre régulier), tandis que $A$, $B$, $D$ et le point $(2;3;0)$ sont dans le plan du bas. On résout deux équations (méthode de Cramer, <span class="tag hp">hors programme</span>), puis la troisième tranche : c'est la méthode de la partie 4, automatisée. Le module <code>fractions</code> évite les arrondis.</p>` },
    { bo: false, t: "Coordonnées d'un point défini par une combinaison", code: `def combinaison(O, coefs, vecteurs):
    P = list(O)
    for c, v in zip(coefs, vecteurs):
        for i in range(3):
            P[i] = P[i] + c * v[i]
    return P

A = (0, 0, 0)
AB, AD, AE = (1, 0, 0), (0, 1, 0), (0, 0, 1)
print(combinaison(A, [1, 0.5, 1], [AB, AD, AE]))     # I milieu de [FG]
print(combinaison(A, [0.5, 0.5, 0.5], [AB, AD, AE])) # centre du cube`, sortie: `[1.0, 0.5, 1.0]
[0.5, 0.5, 0.5]` }
  ],
  methodes: [
    { t: "Montrer que trois points sont alignés, ou deux droites parallèles", h: R`
<ol><li>Exprime $\vec{AB}$ et $\vec{AC}$ (ou les vecteurs directeurs) dans une même base, ou en coordonnées.</li><li>Trouve $k$ tel que $\vec{AC}=k\vec{AB}$ ; vérifie la relation sur <b>les trois</b> composantes.</li><li>Conclus : colinéaires ⟹ alignés (ou parallèles). Si une composante ne colle pas : pas alignés.</li></ol>` },
    { t: "Montrer que quatre points sont coplanaires", h: R`
<ol><li>Vérifie que $A$, $B$, $C$ ne sont pas alignés.</li><li>Cherche $a$, $b$ tels que $\vec{AD}=a\vec{AB}+b\vec{AC}$ : deux coordonnées (ou deux composantes) donnent $a$ et $b$, la troisième sert de <b>test</b>.</li><li>Test réussi : coplanaires. Échec : non coplanaires, et $(\vec{AB},\vec{AC},\vec{AD})$ est une base.</li></ol>
<p>Raccourci fréquent : trouver deux droites parallèles (ou sécantes) qui passent par les quatre points, comme $(IL)∥(JK)$ dans la partie 4.</p>` },
    { t: "Lire sur une figure si trois vecteurs forment une base", h: R`
<p>Représente-les à partir d'un même point. S'ils restent dans un même plan (une face, une « tranche » du solide), ils sont coplanaires : pas une base. Si l'un « sort » du plan des deux autres, c'est une base. Dans le cube : $(\vec{AB},\vec{AD},\vec{AE})$ oui ; $(\vec{AB},\vec{AC},\vec{EF})$ non ($\vec{EF}=\vec{AB}$) ; $(\vec{AC},\vec{AE},\vec{AG})$ non ($\vec{AG}=\vec{AC}+\vec{AE}$, tous dans le rectangle $ACGE$).</p>` },
    { t: "Construire la section d'un solide par un plan", h: R`
<ol><li>Deux points du plan sur une même face : on les relie (c'est un segment de la section).</li><li>Sur deux faces <b>parallèles</b>, les segments de section sont <b>parallèles</b>.</li><li>Si besoin, prolonge une droite de la section jusqu'à une arête prolongée pour obtenir un nouveau point sur une face voisine.</li></ol>` },
    { t: "Étudier la position relative de deux droites données par des points", h: R`
<p>Compare les vecteurs directeurs : colinéaires ⟹ parallèles (confondues si un point de l'une est sur l'autre). Sinon, elles sont sécantes ou non coplanaires : elles sont sécantes si et seulement si les quatre points qui les définissent sont coplanaires. Avec des représentations paramétriques, on résout un système (chapitre 12).</p>` }
  ],
  exos: [
    { niv: 1, t: "Chemins dans le cube", enonce: R`<p>$ABCDEFGH$ est un cube. $I$ est le milieu de $[EH]$, $J$ celui de $[BC]$.</p><ol><li>Exprimer $\vec{AH}$, $\vec{AF}$, $\vec{BH}$ en fonction de $\vec{AB}$, $\vec{AD}$, $\vec{AE}$.</li><li>Exprimer $\vec{AI}$ et $\vec{AJ}$ de même, puis $\vec{IJ}$.</li><li>Les droites $(IJ)$ et $(AB)$ sont-elles parallèles ?</li></ol>`,
      corrige: R`<ol><li>$\vec{AH}=\vec{AD}+\vec{AE}$ ; $\vec{AF}=\vec{AB}+\vec{AE}$ ; $\vec{BH}=\vec{BA}+\vec{AH}=-\vec{AB}+\vec{AD}+\vec{AE}$.</li><li>$\vec{AI}=\vec{AE}+\frac12\vec{EH}=\frac12\vec{AD}+\vec{AE}$ ; $\vec{AJ}=\vec{AB}+\frac12\vec{AD}$. Donc $\vec{IJ}=\vec{AJ}-\vec{AI}=\vec{AB}-\vec{AE}$.</li><li>$\vec{IJ}=\vec{AB}-\vec{AE}$ a une composante non nulle sur $\vec{AE}$ : il n'est pas colinéaire à $\vec{AB}$. Les droites ne sont pas parallèles. (En fait $\vec{IJ}=\vec{EB}$ : $(IJ)$ est parallèle à la diagonale $(EB)$ de la face avant.)</li></ol>` },
    { niv: 1, t: "Coordonnées et alignement", enonce: R`<p>Dans un repère de l'espace, $A(1;2;-1)$, $B(3;1;2)$, $C(7;-1;8)$, $D(0;4;1)$.</p><ol><li>Calculer les coordonnées de $\vec{AB}$, $\vec{AC}$ et du milieu $M$ de $[BD]$.</li><li>$A$, $B$, $C$ sont-ils alignés ?</li><li>Les vecteurs $\vec{AB}$ et $\vec{AD}$ sont-ils colinéaires ?</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(2;-1;3)$ ; $\vec{AC}(6;-3;9)$ ; $M\left(\frac32;\frac52;\frac32\right)$.</li><li>$\vec{AC}=3\vec{AB}$ (vérifié sur les trois coordonnées : $6=3\times2$, $-3=3\times(-1)$, $9=3\times3$) : alignés.</li><li>$\vec{AD}(-1;2;2)$. Si $\vec{AD}=k\vec{AB}$, la 1<sup>re</sup> coordonnée donne $k=-\frac12$, mais la 2<sup>e</sup> donnerait $k=-2$ : pas colinéaires.</li></ol>` },
    { niv: 2, t: "Coplanaires ou base ?", enonce: R`<p>Dans un repère, $A(1;0;2)$, $B(2;1;3)$, $C(0;2;1)$, $D(3;0;4)$ et $E(2;2;5)$.</p><ol><li>Montrer que $A$, $B$, $C$ ne sont pas alignés.</li><li>Les points $A$, $B$, $C$, $D$ sont-ils coplanaires ?</li><li>Et $A$, $B$, $C$, $E$ ? Que peut-on dire du triplet $(\vec{AB},\vec{AC},\vec{AE})$ ?</li></ol>`,
      corrige: R`<ol><li>$\vec{AB}(1;1;1)$, $\vec{AC}(-1;2;-1)$ : la 1<sup>re</sup> coordonnée donnerait $k=-1$, la 2<sup>e</sup> $k=2$. Non colinéaires, donc non alignés.</li><li>$\vec{AD}(2;0;2)$. On cherche $\vec{AD}=a\vec{AB}+b\vec{AC}$ : $a-b=2$ et $a+2b=0$ donnent $b=-\frac23$, $a=\frac43$. Test sur la 3<sup>e</sup> coordonnée : $a-b=\frac43+\frac23=2$. ✓ Coplanaires.</li><li>$\vec{AE}(1;2;3)$ : $a-b=1$ et $a+2b=2$ donnent $b=\frac13$, $a=\frac43$ ; 3<sup>e</sup> coordonnée : $a-b=1\neq3$. Non coplanaires : $(\vec{AB},\vec{AC},\vec{AE})$ est une base de l'espace.</li></ol>` },
    { niv: 2, t: "Positions relatives dans une pyramide", enonce: R`<p>$SABCD$ est une pyramide de sommet $S$ dont la base $ABCD$ est un parallélogramme. $I$ et $J$ sont les milieux de $[SA]$ et $[SB]$.</p><ol><li>Montrer que $(IJ)$ est parallèle à $(CD)$.</li><li>La droite $(IJ)$ est-elle parallèle au plan $(ABC)$ ?</li><li>Les plans $(SAD)$ et $(SBC)$ sont sécants (en $S$ au moins). Justifier que leur intersection est la droite passant par $S$ et parallèle à $(AD)$.</li></ol>`,
      corrige: R`<ol><li>Théorème des milieux dans $SAB$ : $\vec{IJ}=\frac12\vec{AB}$. Comme $ABCD$ est un parallélogramme, $\vec{AB}=\vec{DC}$, donc $\vec{IJ}=\frac12\vec{DC}$ : $(IJ)∥(CD)$.</li><li>$(IJ)$ est parallèle à $(AB)$, droite du plan $(ABC)$ : $(IJ)$ est parallèle au plan $(ABC)$. Elle n'est pas incluse dedans ($I$ est le milieu de $[SA]$ et $S\notin(ABC)$), donc strictement parallèle.</li><li>$(AD)\subset(SAD)$ et $(BC)\subset(SBC)$ sont parallèles ($\vec{AD}=\vec{BC}$). Les deux plans sont sécants (ils contiennent $S$ et ne sont pas confondus). Théorème du toit : leur intersection est parallèle à $(AD)$ ; elle passe par $S$.</li></ol>` },
    { niv: 3, t: "Les bimédianes du tétraèdre (type bac)", enonce: R`<p>$ABCD$ est un tétraèdre. On note $I$, $J$, $K$, $L$, $M$, $N$ les milieux respectifs de $[AB]$, $[CD]$, $[AC]$, $[BD]$, $[AD]$ et $[BC]$. On se place dans le repère $(A;\vec{AB},\vec{AC},\vec{AD})$.</p><ol><li>Justifier que ce repère est bien défini, puis donner les coordonnées des dix points.</li><li>Exprimer $\vec{KL}$ en fonction de $\vec{AB}$, $\vec{AC}$, $\vec{AD}$.</li><li>Soit $G$ le milieu de $[IJ]$. Montrer que $G$ est aussi le milieu de $[KL]$ et de $[MN]$.</li><li>En déduire que $I$, $J$, $K$, $L$ sont coplanaires et que $IKJL$ est un parallélogramme.</li><li>Montrer que la droite $(IK)$ est strictement parallèle au plan $(BCD)$.</li></ol>`,
      corrige: R`<ol><li>$ABCD$ est un tétraèdre : les quatre points ne sont pas coplanaires, donc $\vec{AB}$, $\vec{AC}$, $\vec{AD}$ ne sont pas coplanaires et forment une base. $A(0;0;0)$, $B(1;0;0)$, $C(0;1;0)$, $D(0;0;1)$ ; $I\left(\frac12;0;0\right)$, $J\left(0;\frac12;\frac12\right)$, $K\left(0;\frac12;0\right)$, $L\left(\frac12;0;\frac12\right)$, $M\left(0;0;\frac12\right)$, $N\left(\frac12;\frac12;0\right)$.</li><li>$\vec{KL}\left(\frac12;-\frac12;\frac12\right)$, soit $\vec{KL}=\frac12\vec{AB}-\frac12\vec{AC}+\frac12\vec{AD}$.</li><li>$G\left(\frac{\frac12+0}2;\frac{0+\frac12}2;\frac{0+\frac12}2\right)=\left(\frac14;\frac14;\frac14\right)$. Milieu de $[KL]$ : $\left(\frac14;\frac14;\frac14\right)$ ; milieu de $[MN]$ : $\left(\frac14;\frac14;\frac14\right)$. C'est le même point $G$ : les trois segments qui joignent les milieux d'arêtes opposées (les <b>bimédianes</b>) se coupent en leur milieu.</li><li>Les droites $(IJ)$ et $(KL)$ sont sécantes en $G$ : elles sont contenues dans un même plan, donc $I$, $J$, $K$, $L$ sont coplanaires. Le quadrilatère $IKJL$ a des diagonales $[IJ]$ et $[KL]$ de même milieu : c'est un parallélogramme.</li><li>$\vec{IK}\left(-\frac12;\frac12;0\right)$ et $\vec{BC}(-1;1;0)$ : $\vec{IK}=\frac12\vec{BC}$ (théorème des milieux dans $ABC$). $(IK)$ est parallèle à $(BC)$, droite du plan $(BCD)$, donc parallèle à ce plan. Elle n'est pas incluse : $I$ est le milieu de $[AB]$ et $A\notin(BCD)$, donc $I\notin(BCD)$ (sinon la droite $(BI)$, qui contient $A$, serait dans ce plan). Le parallélisme est strict.</li></ol>
<p class="stylo">Le point $G\left(\frac14;\frac14;\frac14\right)$ est l'isobarycentre des quatre sommets : la moyenne de leurs coordonnées.</p>` }
  ],
  annales: [
    { ref: "Bac 2026, Métropole – La Réunion, 8 septembre 2026 (sujet 1), exercice 3, affirmation 1", url: "https://www.apmep.fr/IMG/pdf/Metropole_J_spe_8osep_2026.pdf", h: R`Vrai/faux : « les vecteurs $\vec u(1;0;2)$, $\vec v(0;1;3)$ et $\vec w(2;1;0)$ forment une base de l'espace ». Vrai : ils ne sont pas coplanaires (exemple traité dans la partie 5).` },
    { ref: "Bac 2025, Amérique du Sud, 14 novembre 2025 (jour 2), exercice 2, question 3", url: "https://www.apmep.fr/IMG/pdf/Ame_du_Sud_J2_14_11_2025_DV.pdf", h: R`QCM : $A(3;2;1)$, $B(7;3;1)$, $C(-1;4;5)$, $D(-3;3;5)$ ; les points sont-ils coplanaires, alignés, $\vec{AB}$ et $\vec{CD}$ colinéaires ? Ici $\vec{AB}(4;1;0)$ et $\vec{CD}(-2;-1;0)$ ne sont pas colinéaires, $A$, $B$, $C$ ne sont pas alignés, et la recherche de $a$, $b$ avec $\vec{AD}=a\vec{AB}+b\vec{AC}$ donne $a=-\frac23$, $b=\frac56$, mais la troisième coordonnée ne colle pas ($\frac{10}3\neq4$) : les quatre points ne sont pas coplanaires (réponse a).` },
    { ref: "Bac 2024, Métropole – Antilles-Guyane, 12 septembre 2024 (jour 2), exercice 1, question 1", url: "https://www.apmep.fr/IMG/pdf/Spe_J2_12_09_2024_Metropole_DV.pdf", h: R`Le cube $ABCDEFGH$ dans le repère $(A;\vec{AB},\vec{AD},\vec{AE})$, $I$ et $J$ milieux de $[AB]$ et $[CG]$ : coordonnées de $I$, $J$, du milieu $N$ de $[IJ]$, puis des vecteurs $\vec{IJ}$ et $\vec{NF}$. La suite de l'exercice relève des chapitres 11 et 12.` }
  ],
  retenir: R`
[def|Droite et plan]Droite $(A;\vec u)$, $\vec u\neq\vec 0$ : $M\in(d)\iff\vec{AM}=t\vec u$. Plan $(A;\vec u,\vec v)$, $\vec u$, $\vec v$ non colinéaires : $M\in\mathcal P\iff\vec{AM}=s\vec u+t\vec v$.[/]
[prop|Colinéarité, coplanarité]$\vec u$, $\vec v$ colinéaires : $\vec v=k\vec u$ (coordonnées proportionnelles sur les trois). $\vec u$, $\vec v$, $\vec w$ coplanaires : $\vec w=a\vec u+b\vec v$ (si $\vec u$, $\vec v$ non colinéaires).<br>Alignés ⟺ $\vec{AB}$, $\vec{AC}$ colinéaires. Coplanaires ⟺ $\vec{AD}=a\vec{AB}+b\vec{AC}$.[/]
[thm|Base]Trois vecteurs non coplanaires forment une base : décomposition <b>unique</b> $\vec u=x\vec i+y\vec j+z\vec k$. Milieu : moyenne des coordonnées.[/]
<div class="tab-wrap"><table><tr><th>Objets</th><th>Positions</th></tr>
<tr><td>2 droites</td><td>sécantes · parallèles · <b>non coplanaires</b></td></tr>
<tr><td>droite et plan</td><td>sécants · parallèles (dont : incluse)</td></tr>
<tr><td>2 plans</td><td>sécants selon une droite · parallèles</td></tr></table></div>
[thm|Toit]Deux droites parallèles dans deux plans sécants : l'intersection des plans leur est parallèle.[/]
<p class="stylo">Cube $(A;\vec{AB},\vec{AD},\vec{AE})$ : $G(1;1;1)$, centre $\left(\frac12;\frac12;\frac12\right)$, $\vec{AG}=\vec{AB}+\vec{AD}+\vec{AE}$.</p>`,
  qcm: [
    { q: R`Dans le cube $ABCDEFGH$, $\vec{AB}+\vec{BF}+\vec{FG}=$`, c: [R`$\vec{AF}$`, R`$\vec{AG}$`, R`$\vec{AH}$`, R`$\vec{AC}$`], r: 1, e: R`Chasles : $A\to B\to F\to G$, donc $\vec{AG}$.`, ref: "vecteurs" },
    { q: R`Dans le cube, $\vec{AG}$ s'écrit :`, c: [R`$\vec{AB}+\vec{AD}$`, R`$\vec{AB}+\vec{AD}+\vec{AE}$`, R`$\vec{AB}+\vec{AE}$`, R`$2\vec{AB}+\vec{AE}$`], r: 1, e: R`$\vec{AG}=\vec{AB}+\vec{BC}+\vec{CG}$ avec $\vec{BC}=\vec{AD}$ et $\vec{CG}=\vec{AE}$.`, ref: "vecteurs" },
    { q: R`$I$ milieu de $[FG]$ dans le cube. $\vec{AI}=$`, c: [R`$\vec{AB}+\frac12\vec{AD}+\vec{AE}$`, R`$\frac12\vec{AB}+\vec{AD}+\vec{AE}$`, R`$\vec{AB}+\vec{AD}+\frac12\vec{AE}$`, R`$\frac12(\vec{AB}+\vec{AD}+\vec{AE})$`], r: 0, e: R`$\vec{AI}=\vec{AB}+\vec{BF}+\frac12\vec{FG}$.`, ref: "combinaisons" },
    { q: R`Deux droites de l'espace qui n'ont aucun point commun sont :`, c: ["forcément parallèles", "parallèles ou non coplanaires", "forcément non coplanaires", "sécantes"], r: 1, e: R`Sans point commun : strictement parallèles (coplanaires) ou non coplanaires.`, ref: "positions" },
    { q: R`Dans le cube, les droites $(AB)$ et $(CG)$ sont :`, c: ["parallèles", "sécantes", "non coplanaires", "confondues"], r: 2, e: R`Aucun plan ne les contient toutes les deux : elles ne se coupent pas et ne sont pas parallèles.`, ref: "positions" },
    { q: R`$\vec u(1;2;3)$ et $\vec v(2;4;5)$ sont :`, c: ["colinéaires", "non colinéaires", "égaux", "opposés"], r: 1, e: R`$\frac21=\frac42$ mais $\frac53\neq2$ : pas proportionnels sur la troisième coordonnée.`, ref: "bases" },
    { q: R`Trois vecteurs forment une base de l'espace si et seulement si :`, c: ["ils sont deux à deux non colinéaires", "ils sont non coplanaires", "ils sont non nuls", "ils sont orthogonaux deux à deux"], r: 1, e: R`Deux à deux non colinéaires ne suffit pas ($\vec{AB}$, $\vec{AD}$, $\vec{AC}$). Orthogonaux suffit mais n'est pas nécessaire.`, ref: "bases" },
    { q: R`Dans le cube, $(\vec{AC},\vec{AE},\vec{AG})$ :`, c: ["est une base", "n'est pas une base car $\\vec{AG}=\\vec{AC}+\\vec{AE}$", "n'est pas une base car $\\vec{AC}$ et $\\vec{AE}$ sont colinéaires", "est une base orthonormée"], r: 1, e: R`Les trois vecteurs sont dans le rectangle $ACGE$ : coplanaires.`, ref: "plans" },
    { q: R`$A(1;2;-1)$, $B(3;1;2)$. Le milieu de $[AB]$ est :`, c: [R`$(2;1{,}5;0{,}5)$`, R`$(4;3;1)$`, R`$(1;-0{,}5;1{,}5)$`, R`$(2;1;1)$`], r: 0, e: R`Moyenne des coordonnées : $\left(\frac{1+3}2;\frac{2+1}2;\frac{-1+2}2\right)$.`, ref: "bases" },
    { q: R`$A$, $B$, $C$ non alignés. $D$ est dans le plan $(ABC)$ si et seulement si :`, c: [R`$\vec{AD}=k\vec{AB}$`, R`$\vec{AD}=a\vec{AB}+b\vec{AC}$ pour des réels $a$, $b$`, R`$\vec{AD}\neq\vec 0$`, R`$\vec{AB}+\vec{AC}+\vec{AD}=\vec 0$`], r: 1, e: R`Caractérisation d'un plan par un point et deux vecteurs non colinéaires.`, ref: "plans" },
    { q: R`Une droite parallèle à une droite d'un plan $\mathcal P$ est :`, c: [R`sécante à $\mathcal P$`, R`parallèle à $\mathcal P$ (éventuellement incluse)`, R`strictement parallèle à $\mathcal P$`, R`orthogonale à $\mathcal P$`], r: 1, e: R`Elle peut être dans $\mathcal P$ : « parallèle » inclut ce cas.`, ref: "positions" },
    { q: R`Deux plans parallèles sont coupés par un troisième plan. Les deux droites d'intersection sont :`, c: ["sécantes", "parallèles", "non coplanaires", "on ne peut rien dire"], r: 1, e: R`Propriété des plans parallèles (c'est ce qui guide les sections du cube).`, ref: "positions" },
    { q: R`Théorème du toit : $(d_1)\subset\mathcal P_1$, $(d_2)\subset\mathcal P_2$, $(d_1)∥(d_2)$, $\mathcal P_1\cap\mathcal P_2=(\Delta)$. Alors :`, c: [R`$(\Delta)$ est parallèle à $(d_1)$ et $(d_2)$`, R`$(\Delta)$ coupe $(d_1)$`, R`$(\Delta)$ est orthogonale à $(d_1)$`, R`$\mathcal P_1∥\mathcal P_2$`], r: 0, e: R`L'arête du « toit » est parallèle aux deux droites.`, ref: "positions" },
    { q: R`$\vec u(1;0;2)$, $\vec v(0;1;3)$, $\vec w(2;1;7)$ :`, c: ["forment une base", "sont coplanaires", "sont colinéaires deux à deux", "sont nuls"], r: 1, e: R`$\vec w=2\vec u+\vec v$ (coordonnée par coordonnée : $2$, $1$, $4+3=7$).`, ref: "plans" }
  ],
  cartes: [
    [R`Relation de Chasles`, R`$\vec{AB}+\vec{BC}=\vec{AC}$`],
    [R`$\vec{AB}=\vec{DC}$ signifie…`, R`$ABCD$ est un parallélogramme (éventuellement aplati).`],
    [R`Caractérisation de la droite $(A;\vec u)$`, R`$M\in(d)\iff\vec{AM}=t\vec u$, $t\in\R$.`],
    [R`Caractérisation du plan $(A;\vec u,\vec v)$`, R`$M\in\mathcal P\iff\vec{AM}=s\vec u+t\vec v$, avec $\vec u$, $\vec v$ non colinéaires.`],
    [R`Vecteurs coplanaires`, R`L'un est combinaison linéaire des deux autres : $\vec w=a\vec u+b\vec v$.`],
    [R`Base de l'espace`, R`Trois vecteurs non coplanaires.`],
    [R`Décomposition dans une base`, R`Unique : $\vec u=x\vec i+y\vec j+z\vec k$.`],
    [R`Colinéarité en coordonnées`, R`Coordonnées proportionnelles sur les trois composantes.`],
    [R`Positions de deux droites de l'espace`, R`Sécantes, parallèles ou non coplanaires.`],
    [R`Positions d'une droite et d'un plan`, R`Sécants (un point) ou parallèles (vide ou droite incluse).`],
    [R`Positions de deux plans`, R`Sécants selon une droite, ou parallèles.`],
    [R`Théorème du toit`, R`Deux droites parallèles dans deux plans sécants : l'intersection des plans leur est parallèle.`],
    [R`$\vec{AG}$ dans le cube`, R`$\vec{AB}+\vec{AD}+\vec{AE}$`],
    [R`Section d'un cube : faces parallèles`, R`Les segments de section sur deux faces parallèles sont parallèles.`]
  ]
};

/* ---------- Figures de l'espace en perspective cavalière (outils partagés par les chapitres 10 à 12) ----------
   CAV.vue({ox, oy, s, k, a, repere}) renvoie une projection P(x, y, z) → [X, Y] en pixels de la scène.
   Sans « repere » : x vers la droite, y fuyant (profondeur), z vers le haut (dessin du cube ABCDEFGH).
   Avec « repere: true » : x fuyant vers l'observateur (en bas à gauche), y vers la droite, z vers le haut. */
var CAV = (function () {
  "use strict";
  function vue(o) {
    var k = o.k || 0.5, a = (o.a || 40) * Math.PI / 180, c = Math.cos(a) * k, s = Math.sin(a) * k;
    return o.repere ? function (x, y, z) { return [o.ox + o.s * (y - c * x), o.oy - o.s * (z - s * x)]; }
      : function (x, y, z) { return [o.ox + o.s * (x + c * y), o.oy - o.s * (z + s * y)]; };
  }
  function ajoute(a, b) { var r = {}, k; for (k in a) r[k] = a[k]; for (k in b || {}) r[k] = b[k]; return r; }
  var TRAIT = "stroke:var(--encre);stroke-width:1.5;fill:none", CACHE = "stroke:var(--encre2);stroke-width:1.2;stroke-dasharray:4 3;fill:none";
  function seg(S, P, A, B, cache, at) { var a = P(A[0], A[1], A[2]), b = P(B[0], B[1], B[2]); return S.px.seg(a[0], a[1], b[0], b[1], "a-branche", ajoute({ style: cache ? CACHE : TRAIT }, at)); }
  function trait(S, P, A, B, cls, at) { var a = P(A[0], A[1], A[2]), b = P(B[0], B[1], B[2]); return S.px.seg(a[0], a[1], b[0], b[1], cls, at); }
  function fleche(S, P, A, B, f, cls, at) {
    f = f === undefined ? 1 : f; if (f <= 0.01) return null;
    var Bf = [A[0] + f * (B[0] - A[0]), A[1] + f * (B[1] - A[1]), A[2] + f * (B[2] - A[2])];
    var a = P(A[0], A[1], A[2]), b = P(Bf[0], Bf[1], Bf[2]);
    return S.px.fleche(a[0], a[1], b[0], b[1], cls || "g-c", ajoute({ "stroke-width": 2.6 }, at));
  }
  function poly(S, P, pts, cls, at) { return S.px.path(pts.map(function (q, i) { var p = P(q[0], q[1], q[2]); return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("") + "Z", cls || "a-plein", at); }
  function pt(S, P, A, cls, r, at) { var p = P(A[0], A[1], A[2]); return S.px.cercle(p[0], p[1], r || 3.5, cls || "g-pt", at); }
  function txt(S, P, A, s, cls, anc, dx, dy, at) { var p = P(A[0], A[1], A[2]); return S.px.txt(p[0] + (dx || 0), p[1] + (dy || 0), s, cls, anc || "middle", at); }
  function lerp3(A, B, t) { return [A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]), A[2] + t * (B[2] - A[2])]; }
  /* angle droit en H, entre les directions u et v (unitaires, longueur r en unités de l'espace) */
  function droit(S, P, H, u, v, r) { var a = [H[0] + r * u[0], H[1] + r * u[1], H[2] + r * u[2]], b = [a[0] + r * v[0], a[1] + r * v[1], a[2] + r * v[2]], c = [H[0] + r * v[0], H[1] + r * v[1], H[2] + r * v[2]]; poly(S, P, [H, a, b, c], "a-craie", { style: "fill:none" }); }
  return { vue: vue, seg: seg, trait: trait, fleche: fleche, poly: poly, pt: pt, txt: txt, lerp3: lerp3, droit: droit };
})();

/* Animation : décomposer AG en suivant les arêtes du cube */
ANIMS.cubeChasles = {
  titre: R`Décomposer $\vec{AG}$ dans le cube`,
  vb: [360, 286],
  etapes: [
    { d: 3.5, l: R`Le cube $ABCDEFGH$ et trois vecteurs issus de $A$ : $\vec{AB}$ (bleu), $\vec{AD}$ (vert), $\vec{AE}$ (rouge). Ils ne sont pas dans un même plan : ils forment une <b>base</b>.` },
    { d: 3, l: R`Pour aller de $A$ à $G$, on suit un chemin d'arêtes. Premier pas : $\vec{AB}$.` },
    { d: 4, l: R`Deuxième pas : $\vec{BC}$. La face $ABCD$ est un carré, donc $\vec{BC}=\vec{AD}$ : c'est le vecteur vert, <b>translaté</b> de $A$ en $B$.` },
    { d: 4, l: R`Troisième pas : $\vec{CG}=\vec{AE}$, le vecteur rouge translaté de $A$ en $C$.` },
    { d: 4.5, l: R`Relation de Chasles : $\vec{AG}=\vec{AB}+\vec{BC}+\vec{CG}=\vec{AB}+\vec{AD}+\vec{AE}$. Dans le repère $(A;\vec{AB},\vec{AD},\vec{AE})$, $G$ a pour coordonnées $(1;1;1)$, et le centre du cube, milieu de $[AG]$, $\left(\frac12;\frac12;\frac12\right)$.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, P = CAV.vue({ ox: 52, oy: 212, s: 140, k: 0.5, a: 40 });
    var A = [0, 0, 0], B = [1, 0, 0], C = [1, 1, 0], D = [0, 1, 0], Ee = [0, 0, 1], F = [1, 0, 1], G = [1, 1, 1], H = [0, 1, 1];
    [[A, B], [B, C], [B, F], [Ee, F], [F, G], [G, H], [H, Ee], [A, Ee], [C, G]].forEach(function (s) { CAV.seg(S, P, s[0], s[1], false, { opacity: 0.55 }); });
    [[A, D], [D, C], [D, H]].forEach(function (s) { CAV.seg(S, P, s[0], s[1], true, { opacity: 0.55 }); });
    var lab = { A: [A, -8, 14], B: [B, 8, 14], C: [C, 12, 6], D: [D, -10, -4], E: [Ee, -10, -2], F: [F, 10, 14], G: [G, 10, -4], H: [H, -6, -8] };
    Object.keys(lab).forEach(function (n) { CAV.txt(S, P, lab[n][0], n, "", "middle", lab[n][1], lab[n][2]); });
    var f0 = k === 0 ? E(t) : 1, faible = k >= 1 ? 0.28 : 1;
    CAV.fleche(S, P, A, B, f0, "g-c", { opacity: k >= 1 ? 1 : 1 });
    CAV.fleche(S, P, A, D, f0, "g-c3", { opacity: faible });
    CAV.fleche(S, P, A, Ee, f0, "g-c2", { opacity: faible });
    if (k === 1) CAV.fleche(S, P, A, B, 1, "g-c", { "stroke-width": 4 });
    if (k >= 2) {
      var s2 = k === 2 ? E(ANIM.p(t, 0, 0.75)) : 1, o2 = CAV.lerp3(A, B, s2);
      CAV.fleche(S, P, o2, [o2[0], o2[1] + 1, o2[2]], 1, "g-c3", { "stroke-width": 3.2 });
      if (k > 2 || t > 0.8) CAV.txt(S, P, [1, 0.5, 0], "BC = AD", "b", "start", 14, 20);
    }
    if (k >= 3) {
      var s3 = k === 3 ? E(ANIM.p(t, 0, 0.75)) : 1, o3 = CAV.lerp3(A, C, s3);
      CAV.fleche(S, P, o3, [o3[0], o3[1], o3[2] + 1], 1, "g-c2", { "stroke-width": 3.2 });
      if (k > 3 || t > 0.8) CAV.txt(S, P, [1, 1, 0.5], "CG = AE", "r", "start", 10, 0);
    }
    if (k === 4) {
      CAV.fleche(S, P, A, G, E(ANIM.p(t, 0, 0.6)), "g-c", { "stroke-width": 3.6, style: "stroke:var(--encre)" });
      if (t > 0.55) {
        var M = P(0.5, 0.5, 0.5);
        S.px.cercle(M[0], M[1], 4, "g-pt2");
        S.px.txt(M[0] - 8, M[1] + 16, "Ω", "r", "middle");
        S.px.math(110, 248, 246, 36, R`$\vec{AG}=\vec{AB}+\vec{AD}+\vec{AE}$`, { opacity: E(ANIM.p(t, 0.55, 0.9)) });
      }
    }
  }
};

/* Animation : une droite qui pivote, un plan qui pivote autour d'une droite */
ANIMS.positions3d = {
  titre: "Droite et plan, plan et plan : toutes les positions",
  vb: [360, 260],
  etapes: [
    { d: 3.5, l: R`Un plan horizontal $\mathcal P$ et une droite $(d)$ qui le traverse : ils sont <b>sécants</b> en un point $I$. Sous le plan, la droite est cachée (pointillés).` },
    { d: 5, l: R`La droite pivote et devient de moins en moins inclinée : le point $I$ s'éloigne, puis sort de la partie dessinée du plan… il existe toujours tant que la droite n'est pas horizontale.` },
    { d: 3.5, l: R`Horizontale, la droite ne rencontre plus $\mathcal P$ : elle est <b>strictement parallèle</b> au plan (son vecteur directeur est dans la direction de $\mathcal P$).` },
    { d: 3.5, l: R`On la fait descendre : elle se pose dans $\mathcal P$. Elle est <b>incluse</b> dans le plan, ce qui est aussi un cas de parallélisme.` },
    { d: 5, l: R`Un second plan $\mathcal Q$ pivote autour d'une droite horizontale. Tant qu'il est incliné, il coupe $\mathcal P$ selon une <b>droite</b> $\Delta$ (en rouge), parallèle à l'axe de rotation : deux plans sécants se coupent toujours selon une droite.` },
    { d: 4.5, l: R`Quand $\mathcal Q$ devient horizontal, $\Delta$ part à l'infini : les plans sont <b>parallèles</b>. Pour deux plans, il n'y a que ces deux cas (sécants ou parallèles).` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, P = CAV.vue({ ox: 180, oy: 182, s: 58, k: 0.55, a: 38 });
    var coins = [[-2.2, -1.5, 0], [2.2, -1.5, 0], [2.2, 1.5, 0], [-2.2, 1.5, 0]];
    function dansP(X) { return Math.abs(X[0]) <= 2.2 && Math.abs(X[1]) <= 1.5; }
    var a = 0, tg = 0, z0 = 0.6, y0 = -1.5, y1 = 1.25, yD = null;
    if (k >= 4) {
      a = k === 4 ? 33 : ANIM.l(33, 0, E(t)); tg = Math.tan(a * Math.PI / 180);
      if (a > 0.5) yD = -z0 / tg;
      var Q = function (ya, yb) { return [[-1.9, ya, z0 + ya * tg], [1.9, ya, z0 + ya * tg], [1.9, yb, z0 + yb * tg], [-1.9, yb, z0 + yb * tg]]; };
      var op = k === 4 ? E(ANIM.p(t, 0, 0.3)) : 1;
      if (yD !== null && yD > y0) CAV.poly(S, P, Q(y0, yD), "a-plein2", { opacity: 0.45 * op, "stroke-dasharray": "4 3" });
    }
    CAV.poly(S, P, coins, "a-plein");
    CAV.txt(S, P, [-2.2, -1.5, 0], "𝒫", "b", "start", 6, -6, { "font-size": 16 });
    if (k <= 3) {
      var C0 = [-0.4, 0, 1.25], phi, h = 1.25;
      if (k === 0) phi = 52; else if (k === 1) phi = ANIM.l(52, 6, E(t)); else phi = 0;
      if (k === 3) h = ANIM.l(1.25, 0, E(t));
      var r = phi * Math.PI / 180, u = [Math.cos(r), 0.28, -Math.sin(r)];
      var c = [C0[0], C0[1], h];
      var A1 = [c[0] - 2 * u[0], c[1] - 2 * u[1], c[2] - 2 * u[2]];
      var A2 = [c[0] + 2.6 * u[0], c[1] + 2.6 * u[1], c[2] + 2.6 * u[2]];
      if (phi > 0) {
        var ti = h / Math.sin(r), I = [c[0] + ti * u[0], c[1] + ti * u[1], 0];
        CAV.trait(S, P, A1, ti < 2.6 ? I : A2, "g-c2", { "stroke-width": 2.6 });
        if (ti < 2.6) CAV.trait(S, P, I, A2, "g-c2", { "stroke-width": 2, "stroke-dasharray": "5 4", opacity: 0.8 });
        if (dansP(I)) { CAV.pt(S, P, I, "g-pt2", 4.5); CAV.txt(S, P, I, "I", "r", "start", 7, -6); }
        else CAV.txt(S, P, [2.2, 1.5, 0], "I est plus loin…", "r", "end", 0, -10);
        CAV.txt(S, P, A1, "(d)", "r", "end", -5, 4);
      } else {
        CAV.trait(S, P, [-2.5, 0.2, h], [2.5, 0.2, h], "g-c2", { "stroke-width": 2.6 });
        CAV.txt(S, P, [2.5, 0.2, h], k === 2 ? "(d) ∥ 𝒫" : t > 0.9 ? "(d) ⊂ 𝒫" : "(d)", "r", "end", 0, -9);
      }
    } else {
      var haut = yD !== null && yD > y0 ? yD : y0;
      CAV.poly(S, P, Q(haut, y1), "a-plein2", { opacity: k === 4 ? E(ANIM.p(t, 0, 0.3)) : 1 });
      CAV.trait(S, P, [-2.1, 0, z0], [2.1, 0, z0], "a-craie");
      CAV.txt(S, P, [1.9, y1, z0 + y1 * tg], "𝒬", "r", "start", 6, 0, { "font-size": 16 });
      if (yD !== null) {
        if (yD >= -1.5) { CAV.trait(S, P, [-2.2, yD, 0], [2.2, yD, 0], "g-c2", { "stroke-width": 3 }); CAV.txt(S, P, [2.2, yD, 0], "Δ", "r", "start", 6, 4); }
        else CAV.txt(S, P, [2.2, -1.5, 0], "Δ est plus loin…", "r", "end", 0, 16);
      } else CAV.txt(S, P, [-1.9, y1, z0], "𝒬 ∥ 𝒫", "r", "start", 0, -12);
    }
  }
};
