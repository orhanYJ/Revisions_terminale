/* ---------- Chapitre 13 : succession d'épreuves indépendantes, schéma de Bernoulli, loi binomiale ---------- */
var CH13 = {
  id: "ch13", num: 13, statut: "ok", partie: "Probabilités", titre: "Succession d'épreuves indépendantes, loi binomiale", court: "Loi binomiale",
  sous: "Répéter une expérience à deux issues et compter les succès : le modèle le plus utilisé du bac.",
  resume: "Épreuves indépendantes, arbres, loi de Bernoulli, schéma de Bernoulli, loi $\\mathcal B(n,p)$, seuils et intervalles.",
  essentiel: [
    R`Dans une <b>succession d'épreuves indépendantes</b>, la probabilité d'une issue $(x_1;\dots;x_n)$ est le <b>produit</b> des probabilités des $x_i$ : sur un arbre, on multiplie le long des branches.`,
    R`Une <b>épreuve de Bernoulli</b> a deux issues : succès (probabilité $p$) et échec ($1-p$). La variable qui vaut $1$ en cas de succès et $0$ sinon suit la loi de Bernoulli : $E=p$, $V=p(1-p)$.`,
    R`Un <b>schéma de Bernoulli</b> répète $n$ fois, de façon <b>indépendante</b>, la même épreuve de Bernoulli. Le nombre $X$ de succès suit la <b>loi binomiale</b> $\mathcal B(n,p)$.`,
    R`$P(X=k)=\binom nk p^k(1-p)^{n-k}$ : $\binom nk$ chemins de l'arbre comportent $k$ succès, et chacun a la probabilité $p^k(1-p)^{n-k}$.`,
    R`« Au moins un succès » : $P(X\geq1)=1-(1-p)^n$. Pour les autres calculs ($P(X\leq k)$, seuils, intervalles), la calculatrice ou un programme.`
  ],
  attendus: [
    R`Modéliser une situation par une succession d'épreuves indépendantes, ou une succession de deux ou trois épreuves quelconques ; la représenter par un arbre ; calculer une probabilité avec l'indépendance, les probabilités conditionnelles, la formule des probabilités totales.`,
    R`Modéliser une situation par un schéma de Bernoulli, par une loi binomiale.`,
    R`Utiliser l'expression de la loi binomiale pour résoudre un problème de seuil, de comparaison, d'optimisation relatif à des probabilités de nombre de succès.`,
    R`Calculer numériquement $P(X=k)$, $P(X\leq k)$, $P(k\leq X\leq k')$, au besoin avec un algorithme ; chercher un intervalle $I$ pour lequel $P(X\in I)$ est inférieure à $\alpha$, ou supérieure à $1-\alpha$.`,
    R`Démonstration exigible : expression de la probabilité de $k$ succès dans le schéma de Bernoulli <span class="tag bo">BO</span>. Algorithmes : planche de Galton ; surréservation ; simulation d'un échantillon.`
  ],
  premiere: R`
<ul><li><b>Probabilité conditionnelle</b> : $P_A(B)=\frac{P(A\cap B)}{P(A)}$ si $P(A)\neq0$ ; donc $P(A\cap B)=P(A)\times P_A(B)$.</li>
<li><b>Arbre pondéré</b> : la somme des probabilités issues d'un même nœud vaut $1$ ; on multiplie le long d'un chemin ; on additionne les chemins qui mènent à un même événement.</li>
<li><b>Probabilités totales</b> : si $A_1,\dots,A_m$ forment une partition de l'univers, $P(B)=P(A_1\cap B)+\dots+P(A_m\cap B)$.</li>
<li><b>Indépendance</b> : $A$ et $B$ sont indépendants si $P(A\cap B)=P(A)\times P(B)$, c'est-à-dire $P_A(B)=P(B)$.</li>
<li><b>Variable aléatoire</b> : loi, espérance $E(X)=\sum x_iP(X=x_i)$, variance $V(X)=\sum(x_i-E(X))^2P(X=x_i)=E(X^2)-E(X)^2$, écart type $\sigma=\sqrt V$.</li>
<li><b>Chapitre 5</b> : $\binom nk$ compte les mots de $n$ lettres contenant exactement $k$ lettres S.</li></ul>`,
  cours: [
    { id: "succession", titre: "Succession d'épreuves indépendantes", html: R`
[def|Le modèle]On réalise successivement $n$ épreuves (expériences aléatoires) dont les univers sont $\Omega_1$, …, $\Omega_n$. L'univers de l'expérience globale est le <b>produit cartésien</b> $\Omega_1\times\dots\times\Omega_n$ : une issue est une liste $(x_1;\dots;x_n)$. Les épreuves sont <b>indépendantes</b> lorsque
$$P((x_1;\dots;x_n))=P(x_1)\times P(x_2)\times\dots\times P(x_n).$$[/]
<p>Concrètement : le résultat d'une épreuve n'influence pas les suivantes (lancers successifs, tirages <b>avec remise</b>, personnes choisies au hasard dans une très grande population). Sur un arbre, les probabilités des branches ne dépendent pas du chemin déjà parcouru.</p>
[ex|Un dé puis une pièce]On lance un dé équilibré puis une pièce équilibrée. $\Omega=\{1;\dots;6\}\times\{P;F\}$ a $12$ issues. $P((6;P))=\frac16\times\frac12=\frac1{12}$.[/]
[ex|Trois tirages avec remise]Une urne contient $3$ boules rouges et $2$ bleues ; on tire trois fois une boule <b>avec remise</b>. $P(RRB)=\frac35\times\frac35\times\frac25=\frac{18}{125}=0{,}144$. Les issues avec exactement une bleue sont $RRB$, $RBR$, $BRR$, de même probabilité : $3\times0{,}144=0{,}432$.[/]
[piege|Sans remise, plus d'indépendance]Si l'on tire <b>sans remise</b>, la composition de l'urne change : $P(RR)=\frac35\times\frac24=\frac3{10}$ et non $\left(\frac35\right)^2$. Ce n'est plus une succession d'épreuves indépendantes : on utilise des probabilités conditionnelles.[/]` },
    { id: "arbres", titre: "Deux ou trois épreuves quelconques : arbres et probabilités totales", html: R`
<p>Quand les épreuves ne sont pas indépendantes, l'arbre reste l'outil : chaque branche porte une probabilité <b>conditionnelle</b>.</p>
[ex|Un test de dépistage (valeurs d'illustration)]Une maladie touche $2\,\%$ d'une population. Un test est positif chez $95\,\%$ des malades et chez $10\,\%$ des personnes saines. $M$ : « malade », $T$ : « test positif ».
<ul><li>$P(M\cap T)=0{,}02\times0{,}95=0{,}019$ ; $P(\overline M\cap T)=0{,}98\times0{,}10=0{,}098$.</li><li>Probabilités totales : $P(T)=0{,}019+0{,}098=0{,}117$.</li><li>Sachant que le test est positif : $P_T(M)=\frac{0{,}019}{0{,}117}\approx0{,}162$.</li></ul>
Un test positif ne donne qu'environ $16\,\%$ de chances d'être malade : la maladie est rare, les faux positifs sont nombreux. C'est un grand classique du bac (sujet de juin 2025 sur les groupes sanguins, sujet de mai 2026 sur les abonnements).[/]
[meth|Lire un énoncé de probabilités conditionnelles]« Parmi les A, 30 % … » est une probabilité <b>conditionnelle</b> $P_A(\dots)$ (deuxième niveau de l'arbre). « 12 % des abonnés ont choisi A <b>et</b> … » est une intersection $P(A\cap\dots)$ (un chemin entier).[/]` },
    { id: "bernoulli", titre: "Épreuve de Bernoulli, loi de Bernoulli", html: R`
[def|Épreuve et loi de Bernoulli]Une <b>épreuve de Bernoulli</b> est une expérience à deux issues, appelées succès ($S$, probabilité $p$) et échec ($\overline S$, probabilité $1-p$). La variable $X$ qui vaut $1$ en cas de succès et $0$ en cas d'échec suit la <b>loi de Bernoulli</b> de paramètre $p$.[/]
[prop|Espérance et variance]$E(X)=0\times(1-p)+1\times p=p$ et $V(X)=E(X^2)-E(X)^2=p-p^2=p(1-p)$.[/]
[ex|Un lancer franc]Un joueur réussit un lancer franc avec la probabilité $0{,}7$. Le nombre de paniers marqués en un lancer suit la loi de Bernoulli de paramètre $0{,}7$ : $E=0{,}7$, $V=0{,}7\times0{,}3=0{,}21$.[/]
<p>Le « succès » est ce qu'on décide de compter : obtenir un $6$, tomber sur une pièce défectueuse, une personne de groupe O négatif… ce n'est pas forcément un événement heureux.</p>` },
    { id: "schema", titre: "Schéma de Bernoulli et loi binomiale", html: R`
[def|Schéma de Bernoulli, loi binomiale]Un <b>schéma de Bernoulli</b> de paramètres $n$ et $p$ est la répétition de $n$ épreuves de Bernoulli <b>identiques</b> (même $p$) et <b>indépendantes</b>. La variable $X$ égale au <b>nombre de succès</b> suit la <b>loi binomiale</b> de paramètres $n$ et $p$, notée $\mathcal B(n,p)$. Ses valeurs sont $0$, $1$, …, $n$.[/]
<div data-anim="arbreBinomial"></div>
[thm|Probabilité de $k$ succès]Si $X$ suit $\mathcal B(n,p)$, pour tout entier $k$ de $0$ à $n$ :
$$P(X=k)=\binom nk\,p^k\,(1-p)^{n-k}.$$[/]
[ex|Cinq lancers francs]$X$ : nombre de paniers sur $5$ lancers indépendants, $X\sim\mathcal B(5;0{,}7)$. $P(X=3)=\binom53\times0{,}7^3\times0{,}3^2=10\times0{,}343\times0{,}09=0{,}3087$. $P(X\geq4)=\binom54\,0{,}7^4\times0{,}3+0{,}7^5\approx0{,}360+0{,}168=0{,}528$.[/]
[ex|Répondre au hasard à un QCM]$10$ questions, $4$ réponses dont une seule juste, réponses au hasard : $X\sim\mathcal B(10;0{,}25)$. $P(X=0)=0{,}75^{10}\approx0{,}056$ ; $P(X=5)=\binom{10}5\times0{,}25^5\times0{,}75^5\approx0{,}058$ ; $P(X\geq5)\approx0{,}078$. Avoir la moyenne au hasard arrive moins d'une fois sur dix.[/]
[meth|Rédaction attendue au bac]« On répète $n$ fois, de manière <b>identique et indépendante</b>, une épreuve à deux issues : le succès « … », de probabilité $p=\dots$, et l'échec. $X$ compte le nombre de succès, donc $X$ suit la loi binomiale $\mathcal B(n;p)$. » Pour un prélèvement dans une grande population, l'énoncé dit souvent qu'on l'<b>assimile à un tirage avec remise</b> : c'est ce qui justifie l'indépendance.[/]` },
    { id: "calculs", titre: "Calculer avec la loi binomiale : cumuls, seuils, intervalles", html: R`
<div data-w="binomiale"></div>
[prop|Les calculs usuels]<ul><li>$P(X\leq k)=P(X=0)+\dots+P(X=k)$ (fonction de répartition : <i>binomFRép</i>, <i>binomcdf</i> selon la calculatrice) ;</li><li>$P(X\geq k)=1-P(X\leq k-1)$ ; $P(X>k)=1-P(X\leq k)$ ;</li><li>$P(a\leq X\leq b)=P(X\leq b)-P(X\leq a-1)$ ;</li><li>$P(X\geq1)=1-P(X=0)=1-(1-p)^n$.</li></ul>[/]
[ex|Un problème de seuil]Chaque jour, un spot publicitaire est vu par une personne donnée avec la probabilité $0{,}1$, indépendamment des autres jours. Combien de jours faut-il pour que la probabilité de l'avoir vu au moins une fois dépasse $0{,}99$ ? On cherche le plus petit $n$ tel que $1-0{,}9^n\geq0{,}99$, soit $0{,}9^n\leq0{,}01$. Avec la calculatrice (tableau de valeurs) ou le logarithme : $n\geq\frac{\ln0{,}01}{\ln0{,}9}\approx43{,}7$. Réponse : $n=44$ jours.[/]
[ex|Un intervalle qui contient $X$ avec une probabilité d'au moins $95\,\%$]$X\sim\mathcal B(100;0{,}5)$ (nombre de « pile » sur $100$ lancers). $P(40\leq X\leq60)\approx0{,}965$ mais $P(41\leq X\leq59)\approx0{,}943$. L'intervalle $[40;60]$ est le plus petit intervalle centré sur $50$ qui contient $X$ avec une probabilité d'au moins $0{,}95$. Obtenir moins de $40$ ou plus de $60$ « pile » rend la pièce suspecte.[/]
[ex|Une probabilité conditionnelle sur une loi binomiale (bac, Amérique du Sud, novembre 2025)]$X\sim\mathcal B(20;0{,}85)$. $P_{(X\geq15)}(X\geq18)=\frac{P(X\geq18)}{P(X\geq15)}\approx0{,}434$ : l'événement $(X\geq18)$ est inclus dans $(X\geq15)$, donc leur intersection est $(X\geq18)$.[/]` },
    { id: "galton", titre: "La planche de Galton et la surréservation", html: R`
<div data-anim="galton"></div>
[ex|Pourquoi une loi binomiale ?]Sur une planche à $6$ rangées de clous, chaque clou envoie la bille à droite avec la probabilité $\frac12$, indépendamment des autres. Le numéro de la case d'arrivée est le nombre de « droite » : il suit $\mathcal B\left(6;\frac12\right)$. Il y a $\binom63=20$ chemins vers la case du milieu, contre $1$ seul vers chaque case extrême : d'où la forme en cloche, $P(X=3)=\frac{20}{64}\approx0{,}31$ et $P(X=0)=\frac1{64}\approx0{,}016$.[/]
[ex|La surréservation (exemple inventé)]Un avion a $200$ places. Chaque passager ayant acheté un billet se présente avec la probabilité $0{,}95$, indépendamment des autres. Si la compagnie vend $210$ billets, le nombre $X$ de passagers présents suit $\mathcal B(210;0{,}95)$ et $P(X>200)\approx0{,}393$ : près de $4$ fois sur $10$, des passagers resteraient à terre. L'algorithme du programme cherche le plus petit $k$ tel que $P(X>k)\leq\alpha$ : avec $\alpha=0{,}05$, on trouve $k=204$. Autrement dit, $210$ billets ne seraient raisonnables qu'avec $204$ places.[/]
[hist|Galton, Bernoulli]Jacques Bernoulli étudie la loi binomiale dans l'<i>Ars Conjectandi</i>, publié en 1713, après sa mort. La planche à clous est due au Britannique Francis Galton, qui s'intéressait à la répartition des caractères autour de la moyenne (fin du XIX<sup>e</sup> siècle).[/]
<p><span class="tag hp">Pour aller plus loin</span> <b>Loi géométrique</b> : le rang $T$ du premier succès dans une suite illimitée d'épreuves de Bernoulli vérifie $P(T=k)=(1-p)^{k-1}p$. Approfondissement non exigible.</p>` }
  ],
  pieges: [
    { t: "Vérifier les trois conditions", h: R`Deux issues, même probabilité de succès à chaque épreuve, épreuves <b>indépendantes</b>. Un tirage sans remise dans une petite urne n'est pas un schéma de Bernoulli.` },
    { t: "$P(X<k)$ n'est pas $P(X\\leq k)$", h: R`Pour une variable à valeurs entières, $P(X<5)=P(X\leq4)$. Et $P(X\geq5)=1-P(X\leq4)$, pas $1-P(X\leq5)$.` },
    { t: "« Au moins un » : l'événement contraire", h: R`$P(X\geq1)=1-P(X=0)=1-(1-p)^n$. Additionner $P(X=1)+P(X=2)+\dots$ à la main est long et risqué.` },
    { t: "Oublier le coefficient binomial", h: R`$p^k(1-p)^{n-k}$ est la probabilité d'<b>un</b> chemin. Il y en a $\binom nk$ qui comptent $k$ succès.` },
    { t: "Confondre $p$ et $1-p$", h: R`Identifie clairement le succès. Si l'on compte les échecs, $n-X$ suit $\mathcal B(n;1-p)$.` },
    { t: "Arrondir trop tôt", h: R`Garde les valeurs exactes (ou la mémoire de la calculatrice) jusqu'au bout ; arrondis seulement le résultat final, à la précision demandée.` }
  ],
  demos: [
    { bo: true, t: "Expression de la probabilité de $k$ succès dans le schéma de Bernoulli", h: R`
<p>On répète $n$ fois une épreuve de Bernoulli de paramètre $p$, de façon indépendante. Une issue est un mot de $n$ lettres, chacune $S$ (succès) ou $E$ (échec) : un chemin de l'arbre.</p>
<p><b>Probabilité d'un chemin.</b> Les épreuves étant indépendantes, la probabilité d'une issue est le produit des probabilités de ses lettres. Un mot qui contient exactement $k$ lettres $S$ et $n-k$ lettres $E$ a donc pour probabilité $p^k(1-p)^{n-k}$, quel que soit l'ordre des lettres.</p>
<p><b>Nombre de chemins.</b> Un tel mot est déterminé par les positions de ses $k$ lettres $S$ : une partie à $k$ éléments de $\{1;\dots;n\}$. Il y en a $\binom nk$ (chapitre 5).</p>
<p><b>Conclusion.</b> L'événement $(X=k)$ est la réunion de ces $\binom nk$ issues, deux à deux disjointes, de même probabilité. Donc
$$P(X=k)=\binom nk\,p^k(1-p)^{n-k}.$$
CQFD. Contrôle : la somme vaut $\sum_{k=0}^n\binom nk p^k(1-p)^{n-k}=(p+1-p)^n=1$ (formule du binôme, <span class="tag hp">hors programme</span>).</p>` },
    { bo: false, t: "Espérance et variance de la loi de Bernoulli", h: R`
<p>$X$ prend la valeur $1$ avec la probabilité $p$ et $0$ avec la probabilité $1-p$. $E(X)=1\times p+0\times(1-p)=p$. Comme $X^2=X$ (car $0^2=0$ et $1^2=1$), $E(X^2)=p$, donc $V(X)=E(X^2)-E(X)^2=p-p^2=p(1-p)$.</p>` },
    { bo: false, t: "Compter les échecs : $n-X\\sim\\mathcal B(n;1-p)$", h: R`
<p>Si l'on échange les rôles de « succès » et « échec », on obtient encore un schéma de Bernoulli, de paramètre $1-p$ ; le nombre de ses succès est le nombre d'échecs du premier, $n-X$. Donc $P(X=k)=P(n-X=n-k)$, ce qui redonne la symétrie $\binom nk=\binom n{n-k}$ lorsque $p=\frac12$.</p>` }
  ],
  algos: [
    { bo: true, t: "Simulation de la planche de Galton", code: `from random import random, seed

def bille(n):
    position = 0
    for i in range(n):            # n rangées de clous
        if random() < 0.5:        # à droite avec la probabilité 1/2
            position = position + 1
    return position

seed(2026)                        # pour retrouver la même simulation
cases = [0] * 7
for k in range(640):
    cases[bille(6)] += 1
print(cases)
print([640 * c // 64 for c in [1, 6, 15, 20, 15, 6, 1]])`, sortie: `[9, 63, 145, 176, 161, 72, 14]
[10, 60, 150, 200, 150, 60, 10]`,
      apres: R`<p>La deuxième ligne donne les effectifs théoriques $640\times\frac{\binom6k}{64}$. L'instruction <code>seed</code> fixe le point de départ du générateur pseudo-aléatoire : sans elle, chaque exécution donne d'autres effectifs, toujours proches des valeurs théoriques.</p>` },
    { bo: true, t: "Loi binomiale : $P(X=k)$ et $P(X\\leq k)$", code: `from math import comb

def binom(n, p, k):
    return comb(n, k) * p**k * (1 - p)**(n - k)

def binom_cumul(n, p, k):          # P(X <= k)
    return sum(binom(n, p, i) for i in range(k + 1))

print(round(binom(5, 0.7, 3), 4))
print(round(1 - binom_cumul(10, 0.25, 4), 4))     # P(X >= 5)`, sortie: `0.3087
0.0781` },
    { bo: true, t: "Surréservation : plus petit $k$ tel que $P(X>k)\\leq\\alpha$", code: `from math import comb

def surreservation(n, p, alpha):
    k = 0
    cumul = (1 - p)**n               # P(X <= 0)
    while 1 - cumul > alpha:         # tant que P(X > k) > alpha
        k = k + 1
        cumul = cumul + comb(n, k) * p**k * (1 - p)**(n - k)
    return k

print(surreservation(210, 0.95, 0.05))
print(surreservation(210, 0.95, 0.01))`, sortie: `204
206`,
      apres: R`<p>Avec $210$ billets vendus et $p=0{,}95$, il faudrait $204$ places pour que le risque de refuser quelqu'un soit au plus $5\,\%$, et $206$ pour $1\,\%$.</p>` },
    { bo: true, t: "Simuler un échantillon d'une variable aléatoire", code: `from random import random, seed

def bernoulli(p):
    return 1 if random() < p else 0

seed(14)
echantillon = [bernoulli(0.7) for i in range(20)]
print(echantillon)
print(sum(echantillon), "succès sur 20")`, sortie: `[1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
14 succès sur 20`,
      apres: R`<p>La somme d'un échantillon de $20$ variables de Bernoulli de paramètre $0{,}7$ est une réalisation de $\mathcal B(20;0{,}7)$, d'espérance $14$.</p>` }
  ],
  methodes: [
    { t: "Justifier qu'une variable suit une loi binomiale", h: R`
<ol><li>Décris l'épreuve élémentaire et ses deux issues ; nomme le succès et donne $p$.</li><li>Dis que l'épreuve est répétée $n$ fois de façon <b>identique et indépendante</b> (tirage avec remise, ou assimilé).</li><li>Dis que $X$ compte le nombre de succès. Conclus : $X\sim\mathcal B(n;p)$.</li></ol>` },
    { t: "Utiliser la calculatrice", h: R`
<ul><li>$P(X=k)$ : <i>binomFdp</i> (TI : binompdf ; Casio : BinomialPD ; NumWorks : application Probabilités, loi binomiale).</li><li>$P(X\leq k)$ : <i>binomFRép</i> (TI : binomcdf ; Casio : BinomialCD).</li><li>Pour $P(X\geq k)$, passe par $1-P(X\leq k-1)$ si la calculatrice n'offre que le cumul à gauche.</li></ul>
<p>Écris toujours la probabilité cherchée avant le résultat : « $P(X\geq5)=1-P(X\leq4)\approx0{,}078$ ».</p>` },
    { t: "Résoudre un problème de seuil", h: R`
<p>Traduis la condition en inéquation sur $n$ (souvent $1-(1-p)^n\geq s$, soit $(1-p)^n\leq1-s$). Résous avec le tableau de valeurs de la calculatrice, ou avec le logarithme (chapitre 6, attention au changement de sens : $\ln(1-p)<0$). Vérifie la réponse : la valeur trouvée convient, la précédente non.</p>` },
    { t: "Trouver un intervalle de probabilité au moins $1-\\alpha$", h: R`
<p>Calcule les probabilités cumulées et cherche le plus petit $a$ avec $P(X\leq a-1)\leq\frac\alpha2$… ou, plus simplement au bac, teste les intervalles proposés : $P(a\leq X\leq b)=P(X\leq b)-P(X\leq a-1)$.</p>` }
  ],
  exos: [
    { niv: 1, t: "Calculs directs", enonce: R`<p>$X$ suit la loi binomiale $\mathcal B(8;0{,}3)$. Donner les valeurs arrondies à $10^{-3}$ de :</p><ol><li>$P(X=2)$ ;</li><li>$P(X=0)$ et $P(X\geq1)$ ;</li><li>$P(X\leq3)$ et $P(2\leq X\leq4)$.</li></ol>`,
      corrige: R`<ol><li>$\binom82\times0{,}3^2\times0{,}7^6=28\times0{,}09\times0{,}117649\approx0{,}296$.</li><li>$P(X=0)=0{,}7^8\approx0{,}058$ ; $P(X\geq1)=1-0{,}7^8\approx0{,}942$.</li><li>$P(X\leq3)\approx0{,}806$ ; $P(2\leq X\leq4)=P(X\leq4)-P(X\leq1)\approx0{,}942-0{,}255=0{,}687$ (valeurs non arrondies dans le calcul : $0{,}6867$).</li></ol>` },
    { niv: 1, t: "Un arbre à trois niveaux", enonce: R`<p>On lance trois fois une pièce truquée qui tombe sur « pile » avec la probabilité $0{,}6$. $X$ est le nombre de « pile ».</p><ol><li>Représenter la situation par un arbre et donner la probabilité de l'issue $(P;F;P)$.</li><li>Justifier que $X$ suit une loi binomiale et donner sa loi complète.</li><li>Vérifier que la somme des probabilités vaut $1$.</li></ol>`,
      corrige: R`<ol><li>Lancers indépendants : $P((P;F;P))=0{,}6\times0{,}4\times0{,}6=0{,}144$.</li><li>Trois répétitions identiques et indépendantes d'une épreuve à deux issues, succès « pile » de probabilité $0{,}6$ : $X\sim\mathcal B(3;0{,}6)$. $P(X=0)=0{,}4^3=0{,}064$ ; $P(X=1)=3\times0{,}6\times0{,}4^2=0{,}288$ ; $P(X=2)=3\times0{,}6^2\times0{,}4=0{,}432$ ; $P(X=3)=0{,}6^3=0{,}216$.</li><li>$0{,}064+0{,}288+0{,}432+0{,}216=1$ ✓.</li></ol>` },
    { niv: 2, t: "Au moins une pièce défectueuse", enonce: R`<p>Une machine produit des pièces dont $3\,\%$ sont défectueuses. On prélève $n$ pièces, prélèvement assimilé à un tirage avec remise.</p><ol><li>Pour $n=20$, calculer la probabilité qu'aucune pièce ne soit défectueuse, puis qu'au moins une le soit.</li><li>Exprimer en fonction de $n$ la probabilité $q_n$ d'avoir au moins une pièce défectueuse.</li><li>Déterminer le plus petit $n$ tel que $q_n\geq0{,}9$.</li></ol>`,
      corrige: R`<ol><li>$X\sim\mathcal B(20;0{,}03)$ : $P(X=0)=0{,}97^{20}\approx0{,}544$ ; $P(X\geq1)\approx0{,}456$.</li><li>$q_n=1-0{,}97^n$.</li><li>$0{,}97^n\leq0{,}1\iff n\geq\frac{\ln0{,}1}{\ln0{,}97}\approx75{,}6$. Plus petit entier : $n=76$ (contrôle : $q_{75}\approx0{,}8982$, $q_{76}\approx0{,}9012$).</li></ol>` },
    { niv: 2, t: "Probabilités totales puis loi binomiale", enonce: R`<p>Dans un lycée, $40\,\%$ des élèves sont en Première et $60\,\%$ en Terminale. $25\,\%$ des élèves de Première et $50\,\%$ des élèves de Terminale font partie d'une association sportive.</p><ol><li>On choisit un élève au hasard. Montrer que la probabilité qu'il fasse partie de l'association est $0{,}4$.</li><li>L'élève fait partie de l'association. Quelle est la probabilité qu'il soit en Terminale ?</li><li>On interroge $15$ élèves au hasard (tirage assimilé à un tirage avec remise). Probabilité qu'exactement $6$ fassent partie de l'association ? qu'au moins $8$ en fassent partie ?</li></ol>`,
      corrige: R`<ol><li>$P(A)=0{,}4\times0{,}25+0{,}6\times0{,}5=0{,}1+0{,}3=0{,}4$.</li><li>$P_A(T)=\frac{0{,}3}{0{,}4}=0{,}75$.</li><li>$X\sim\mathcal B(15;0{,}4)$ : $P(X=6)=\binom{15}6\,0{,}4^6\,0{,}6^9\approx0{,}207$ ; $P(X\geq8)=1-P(X\leq7)\approx1-0{,}787=0{,}213$.</li></ol>` },
    { niv: 3, t: "Contrôle d'une production (type bac)", enonce: R`<p>Une usine fabrique des composants. Un composant est défectueux avec la probabilité $0{,}02$. On contrôle des lots de $50$ composants, assimilés à des tirages avec remise ; $X$ est le nombre de composants défectueux d'un lot.</p><ol><li>Justifier que $X$ suit une loi binomiale ; préciser ses paramètres.</li><li>Calculer $P(X=0)$, $P(X=1)$ puis $P(X\leq2)$, à $10^{-3}$ près.</li><li>Un lot est refusé s'il contient au moins $3$ composants défectueux. Probabilité qu'un lot soit refusé ?</li><li>On contrôle $10$ lots, indépendamment. Probabilité qu'au moins un lot soit refusé ?</li><li>Le fabricant veut que la probabilité de refuser un lot soit inférieure à $1\,\%$ ; il modifie le seuil : un lot est refusé s'il contient au moins $s$ composants défectueux. Déterminer le plus petit $s$ qui convient.</li></ol>`,
      corrige: R`<ol><li>On répète $50$ fois, de façon identique et indépendante, l'épreuve « contrôler un composant », de succès « défectueux » de probabilité $0{,}02$ ; $X$ compte les succès : $X\sim\mathcal B(50;0{,}02)$.</li><li>$P(X=0)=0{,}98^{50}\approx0{,}364$ ; $P(X=1)=50\times0{,}02\times0{,}98^{49}\approx0{,}372$ ; $P(X\leq2)\approx0{,}922$.</li><li>$P(X\geq3)=1-P(X\leq2)\approx0{,}078$.</li><li>Le nombre $Y$ de lots refusés suit $\mathcal B(10;p_r)$ avec $p_r\approx0{,}0784$ : $P(Y\geq1)=1-(1-p_r)^{10}\approx0{,}558$.</li><li>On cherche le plus petit $s$ tel que $P(X\geq s)<0{,}01$, soit $P(X\leq s-1)>0{,}99$. $P(X\leq3)\approx0{,}982$ et $P(X\leq4)\approx0{,}997$ : $s=5$.</li></ol>` }
  ],
  annales: [
    { ref: "Bac 2026, Amérique du Nord, 20 mai 2026 (sujet 1), exercice 1, parties A et B", url: "https://www.apmep.fr/IMG/pdf/Amerique_du_Nord_J1_spe_20_05_2026_FK.pdf", h: R`Arbre à trois branches puis probabilités totales ($P(H)=0{,}4125$), probabilité conditionnelle ; puis $X\sim\mathcal B(8;0{,}4125)$, $P(X=0)\approx0{,}014$, et seuil : plus petit $n$ tel que $1-0{,}5875^n\geq0{,}999$ ($n=13$).` },
    { ref: "Bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 1, questions 1 à 5", url: "https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf", h: R`Groupes sanguins : arbre, probabilités totales, $P_O(R)=0{,}83$, donneur universel ($0{,}0714$), puis $X\sim\mathcal B(100;0{,}0714)$ et $P(X\leq7)\approx0{,}577$. La suite de l'exercice relève des chapitres 14 et 15.` },
    { ref: "Bac 2025, Amérique du Sud, 13 novembre 2025 (jour 1), exercice 2, affirmation 5", url: "https://www.apmep.fr/IMG/pdf/Ameri_du_Sud_J1__13_11_2025_DV.pdf", h: R`$X\sim\mathcal B(20;0{,}85)$ : la probabilité d'avoir au moins $18$ réussites sachant qu'il y en a au moins $15$ vaut environ $0{,}434$ (vrai).` },
    { ref: "Bac 2025, Asie, 5 septembre 2025 (sujet 1), exercice 3, questions 1 à 4c", url: "https://www.apmep.fr/IMG/pdf/Asie_spe_J1_05_09_2025_FK.pdf", h: R`Le QCM répondu au hasard de la partie 4 : $X\sim\mathcal B(10;0{,}25)$, $P(X=5)\approx0{,}0584$, espérance $2{,}5$, puis une note avec points négatifs et $P(Y\leq0)=P(X\leq3)\approx0{,}78$.` },
    { ref: "Bac 2026, Asie, 9 juin 2026 (sujet 1), exercice 2, affirmation 3", url: "https://www.apmep.fr/IMG/pdf/BAC_Specialite_Sujet_2026_J1_Asie_FK.pdf", h: R`$X\sim\mathcal B(3;p)$ : « $P(X=1)=3p-6p^2+3p^3$ ». Vrai : $3p(1-p)^2$ développé.` }
  ],
  retenir: R`
[def|Succession d'épreuves indépendantes]$P((x_1;\dots;x_n))=P(x_1)\times\dots\times P(x_n)$ : on multiplie le long des branches.[/]
[def|Bernoulli]Deux issues, succès de probabilité $p$. Loi de Bernoulli : $E=p$, $V=p(1-p)$.[/]
[thm|Loi binomiale $\mathcal B(n,p)$]$n$ épreuves de Bernoulli identiques et indépendantes ; $X$ = nombre de succès.
$$P(X=k)=\binom nk p^k(1-p)^{n-k},\quad k=0,\dots,n.$$[/]
<div class="tab-wrap"><table><tr><th>Cherché</th><th>Calcul</th></tr>
<tr><td>$P(X\geq1)$</td><td>$1-(1-p)^n$</td></tr>
<tr><td>$P(X\geq k)$</td><td>$1-P(X\leq k-1)$</td></tr>
<tr><td>$P(a\leq X\leq b)$</td><td>$P(X\leq b)-P(X\leq a-1)$</td></tr>
<tr><td>seuil sur $n$</td><td>inéquation $(1-p)^n\leq\dots$, tableau de valeurs ou $\ln$</td></tr></table></div>
<p class="stylo">Rédaction : « répétition de $n$ épreuves de Bernoulli identiques et indépendantes, succès … de probabilité $p$ ; $X$ compte les succès donc $X\sim\mathcal B(n;p)$ ».</p>`,
  qcm: [
    { q: R`On lance $3$ fois un dé équilibré. La probabilité d'obtenir $(6;6;1)$ dans cet ordre est :`, c: [R`$\frac1{216}$`, R`$\frac3{216}$`, R`$\frac1{36}$`, R`$\frac12$`], r: 0, e: R`Épreuves indépendantes : $\frac16\times\frac16\times\frac16$.`, ref: "succession" },
    { q: R`On tire successivement et sans remise $2$ boules d'une urne de $3$ rouges et $2$ bleues. $P(RR)=$`, c: [R`$\frac9{25}$`, R`$\frac3{10}$`, R`$\frac35$`, R`$\frac6{25}$`], r: 1, e: R`$\frac35\times\frac24$ : sans remise, la deuxième probabilité est conditionnelle.`, ref: "succession" },
    { q: R`Une variable de Bernoulli de paramètre $0{,}3$ a pour variance :`, c: ["$0{,}3$", "$0{,}09$", "$0{,}21$", "$0{,}7$"], r: 2, e: R`$p(1-p)=0{,}3\times0{,}7$.`, ref: "bernoulli" },
    { q: R`$X\sim\mathcal B(n;p)$ compte :`, c: ["le rang du premier succès", "le nombre de succès en $n$ épreuves indépendantes", "le nombre d'épreuves", "la proportion de succès"], r: 1, e: R`Définition de la loi binomiale.`, ref: "schema" },
    { q: R`$X\sim\mathcal B(5;0{,}7)$. $P(X=3)=$`, c: [R`$0{,}7^3\times0{,}3^2$`, R`$\binom53\,0{,}7^3\times0{,}3^2$`, R`$\binom53\,0{,}7^2\times0{,}3^3$`, R`$3\times0{,}7$`], r: 1, e: R`$\binom nk p^k(1-p)^{n-k}$ avec $n=5$, $k=3$.`, ref: "schema" },
    { q: R`Le coefficient $\binom nk$ dans la loi binomiale compte :`, c: ["les succès", "les chemins de l'arbre comportant $k$ succès", "les épreuves", "les échecs"], r: 1, e: R`C'est le cœur de la démonstration exigible.`, ref: "schema" },
    { q: R`$X\sim\mathcal B(10;0{,}2)$. $P(X\geq1)=$`, c: [R`$0{,}2^{10}$`, R`$1-0{,}2^{10}$`, R`$1-0{,}8^{10}$`, R`$10\times0{,}2$`], r: 2, e: R`Contraire de « aucun succès » : $1-(1-p)^n$.`, ref: "calculs" },
    { q: R`Pour $X$ à valeurs entières, $P(X\geq4)=$`, c: [R`$1-P(X\leq4)$`, R`$1-P(X\leq3)$`, R`$P(X\leq4)$`, R`$1-P(X=4)$`], r: 1, e: R`Le contraire de $(X\geq4)$ est $(X\leq3)$.`, ref: "calculs" },
    { q: R`Plus petit $n$ tel que $1-0{,}9^n\geq0{,}99$ :`, c: ["$10$", "$43$", "$44$", "$99$"], r: 2, e: R`$0{,}9^{43}\approx0{,}0108>0{,}01$ et $0{,}9^{44}\approx0{,}0097$.`, ref: "calculs" },
    { q: R`Lequel n'est <b>pas</b> un schéma de Bernoulli ?`, c: ["$10$ lancers d'une pièce", "$5$ tirages avec remise dans une urne", "$5$ tirages sans remise dans une urne de $8$ boules", "$100$ personnes choisies dans une très grande population"], r: 2, e: R`Sans remise dans une petite urne : les épreuves ne sont pas indépendantes.`, ref: "succession" },
    { q: R`Sur la planche de Galton à $6$ rangées, la probabilité de tomber dans la case du milieu est :`, c: [R`$\frac17$`, R`$\frac{20}{64}$`, R`$\frac12$`, R`$\frac6{64}$`], r: 1, e: R`$\binom63\left(\frac12\right)^6=\frac{20}{64}$.`, ref: "galton" },
    { q: R`Une maladie touche $2\,\%$ des gens ; un test est positif chez $95\,\%$ des malades et $10\,\%$ des sains. $P(\text{test positif})=$`, c: ["$0{,}95$", "$0{,}117$", "$0{,}019$", "$0{,}162$"], r: 1, e: R`Probabilités totales : $0{,}02\times0{,}95+0{,}98\times0{,}1$.`, ref: "arbres" },
    { q: R`Dans le même exemple, $P_T(M)\approx$`, c: ["$0{,}95$", "$0{,}02$", "$0{,}16$", "$0{,}50$"], r: 2, e: R`$\frac{0{,}019}{0{,}117}\approx0{,}162$.`, ref: "arbres" },
    { q: R`$X\sim\mathcal B(n;p)$ et $Y$ le nombre d'échecs. $Y$ suit :`, c: [R`$\mathcal B(n;p)$`, R`$\mathcal B(n;1-p)$`, R`$\mathcal B(1-n;p)$`, "une loi de Bernoulli"], r: 1, e: R`Les rôles de succès et d'échec s'échangent : $Y=n-X\sim\mathcal B(n;1-p)$.`, ref: "pieges" }
  ],
  cartes: [
    [R`Succession d'épreuves indépendantes`, R`$P((x_1;\dots;x_n))=P(x_1)\times\dots\times P(x_n)$`],
    [R`Probabilités totales (partition $A$, $\overline A$)`, R`$P(B)=P(A)P_A(B)+P(\overline A)P_{\overline A}(B)$`],
    [R`Épreuve de Bernoulli`, R`Deux issues : succès ($p$), échec ($1-p$).`],
    [R`Espérance et variance de Bernoulli`, R`$E=p$, $V=p(1-p)$`],
    [R`Schéma de Bernoulli`, R`$n$ épreuves de Bernoulli identiques et indépendantes.`],
    [R`Loi binomiale : $P(X=k)$`, R`$\binom nk p^k(1-p)^{n-k}$`],
    [R`Pourquoi $\binom nk$ ?`, R`Nombre de chemins de l'arbre à $k$ succès.`],
    [R`$P(X\geq1)$ pour $\mathcal B(n,p)$`, R`$1-(1-p)^n$`],
    [R`$P(X\geq k)$`, R`$1-P(X\leq k-1)$`],
    [R`$P(a\leq X\leq b)$`, R`$P(X\leq b)-P(X\leq a-1)$`],
    [R`Calculatrice : $P(X\leq k)$`, R`binomFRép (binomcdf, BinomialCD)`],
    [R`Planche de Galton à $n$ rangées`, R`Case d'arrivée $\sim\mathcal B\left(n;\frac12\right)$.`],
    [R`Surréservation (algorithme)`, R`Plus petit $k$ tel que $P(X>k)\leq\alpha$.`],
    [R`Ars Conjectandi`, R`Jacques Bernoulli, 1713 : première étude de la loi binomiale.`]
  ]
};

/* ---------- Outils de widgets propres aux chapitres de probabilités ---------- */
var WPB = (function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function N(tag, at, par) { var e = document.createElementNS(NS, tag); for (var k in at) e.setAttribute(k, at[k]); if (par) par.appendChild(e); return e; }
  function nf(x, d) { return (+x.toFixed(d === undefined ? 4 : d)).toString().replace(".", ",").replace("-", "−"); }
  function cadre(el, titre, icone, sous) {
    el.className = "wid";
    el.innerHTML = '<div class="wt">' + (ICONES[icone] || "") + "<span>" + titre + "</span><small>" + (sous || "Interactif") + '</small></div><div class="scene"></div><div class="ctrl"></div><div class="btns"></div><div class="note" aria-live="polite"></div>';
    return { scene: el.querySelector(".scene"), ctrl: el.querySelector(".ctrl"), btns: el.querySelector(".btns"), note: el.querySelector(".note") };
  }
  function curseur(ctrl, lab, min, max, pas, val, f) {
    var l = document.createElement("label");
    l.innerHTML = "<span>" + lab + " : <b></b></span>";
    var i = document.createElement("input"); i.type = "range"; i.min = min; i.max = max; i.step = pas; i.value = val; i.setAttribute("aria-label", lab);
    l.appendChild(i); ctrl.appendChild(l);
    var b = l.querySelector("b");
    function maj() { b.textContent = f ? f(+i.value) : nf(+i.value, 2); }
    i.addEventListener("input", maj); maj();
    return i;
  }
  function liste(ctrl, lab, opts) {
    var l = document.createElement("label"); l.innerHTML = "<span>" + lab + "</span>";
    var s = document.createElement("select"); s.setAttribute("aria-label", lab);
    opts.forEach(function (o, k) { var op = document.createElement("option"); op.value = k; op.textContent = o; s.appendChild(op); });
    l.appendChild(s); ctrl.appendChild(l); return s;
  }
  function binomLoi(n, p) {
    var L = [], q = 1 - p, c = 1;
    for (var k = 0; k <= n; k++) { L.push(c * Math.pow(p, k) * Math.pow(q, n - k)); c = c * (n - k) / (k + 1); }
    return L;
  }
  /* diagramme en bâtons : valeurs v[k], k = 0..n ; marque(k) → true pour colorier en rouge */
  function batons(scene, v, marque, opt) {
    opt = opt || {};
    var W = 360, H = opt.h || 200, ml = 34, mr = 8, mt = 10, mb = 22, n = v.length - 1;
    var ymax = opt.ymax || Math.max.apply(null, v) * 1.12 || 1;
    var svg = N("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": opt.label || "Diagramme en bâtons" });
    scene.innerHTML = ""; scene.appendChild(svg);
    var X = function (k) { return ml + (k + 0.5) * (W - ml - mr) / (n + 1); }, Y = function (y) { return H - mb - y / ymax * (H - mt - mb); };
    var pasY = ymax > 0.5 ? 0.2 : ymax > 0.2 ? 0.1 : ymax > 0.1 ? 0.05 : ymax > 0.04 ? 0.02 : 0.01;
    for (var y = 0; y <= ymax + 1e-9; y += pasY) {
      N("line", { x1: ml, x2: W - mr, y1: Y(y), y2: Y(y), "class": "g-grille" }, svg);
      var t = N("text", { x: ml - 4, y: Y(y) + 4, "text-anchor": "end", "class": "g-txt" }, svg); t.textContent = nf(y, 2);
    }
    N("line", { x1: ml, x2: W - mr, y1: Y(0), y2: Y(0), "class": "g-axe" }, svg);
    var w = Math.max(1.2, Math.min(18, (W - ml - mr) / (n + 1) * 0.72)), pasX = n <= 12 ? 1 : n <= 30 ? 5 : 10;
    for (var k = 0; k <= n; k++) {
      var on = marque && marque(k);
      N("rect", { x: X(k) - w / 2, y: Y(v[k]), width: w, height: Math.max(0, Y(0) - Y(v[k])), rx: Math.min(2, w / 3), style: "fill:" + (on ? "var(--rouge)" : "var(--bleu)") + ";fill-opacity:" + (on ? 0.9 : 0.45) }, svg);
      if (k % pasX === 0) { var tx = N("text", { x: X(k), y: H - mb + 15, "text-anchor": "middle", "class": "g-txt" }, svg); tx.textContent = k; }
    }
    return { svg: svg, X: X, Y: Y, N: N };
  }
  return { N: N, nf: nf, cadre: cadre, curseur: curseur, liste: liste, binomLoi: binomLoi, batons: batons };
})();

/* Interactif : la loi binomiale, ses cumuls et ses intervalles */
WIDGETS.binomiale = function (el) {
  var c = WPB.cadre(el, "Explorer la loi binomiale", "de");
  var n = WPB.curseur(c.ctrl, "Nombre d'épreuves n", 1, 100, 1, 20, function (v) { return v; });
  var p = WPB.curseur(c.ctrl, "Probabilité de succès p", 0.01, 0.99, 0.01, 0.3);
  var mode = WPB.liste(c.ctrl, "Probabilité cherchée", ["P(X = k)", "P(X ≤ k)", "P(X ≥ k)", "P(a ≤ X ≤ b)"]);
  var a = WPB.curseur(c.ctrl, "k (ou a)", 0, 20, 1, 6, function (v) { return v; });
  var b = WPB.curseur(c.ctrl, "b", 0, 20, 1, 9, function (v) { return v; });
  var lb = b.parentNode;
  var occupe = false;
  function maj() {
    if (occupe) return;
    var N = +n.value, P = +p.value, m = +mode.value;
    a.max = N; b.max = N; if (+a.value > N) a.value = N; if (+b.value > N) b.value = N;
    occupe = true; a.dispatchEvent(new Event("input")); b.dispatchEvent(new Event("input")); occupe = false;
    lb.style.display = m === 3 ? "" : "none";
    var A = +a.value, B = Math.max(A, +b.value), L = WPB.binomLoi(N, P);
    var dans = [function (k) { return k === A; }, function (k) { return k <= A; }, function (k) { return k >= A; }, function (k) { return k >= A && k <= B; }][m];
    WPB.batons(c.scene, L, dans, { label: "Loi binomiale" });
    var s = 0; L.forEach(function (v, k) { if (dans(k)) s += v; });
    var lab = ["P(X=" + A + ")", "P(X\\leq " + A + ")", "P(X\\geq " + A + ")", "P(" + A + "\\leq X\\leq " + B + ")"][m];
    var formule = m === 0 ? " $=\\binom{" + N + "}{" + A + "}\\times" + WPB.nf(P, 2) + "^{" + A + "}\\times" + WPB.nf(1 - P, 2) + "^{" + (N - A) + "}$" : m === 2 && A > 0 ? " $=1-P(X\\leq " + (A - 1) + ")$" : m === 3 && A > 0 ? " $=P(X\\leq " + B + ")-P(X\\leq " + (A - 1) + ")$" : "";
    c.note.innerHTML = TeX.fmt("$X\\sim\\mathcal B(" + N + ";" + WPB.nf(P, 2) + ")$. $" + lab + "$" + formule + " $\\approx" + WPB.nf(s, 4) + "$. Barres rouges : valeurs comptées. Espérance $np=" + WPB.nf(N * P, 2) + "$ : le diagramme culmine près de cette valeur.");
  }
  [n, p, a, b].forEach(function (i) { i.addEventListener("input", maj); });
  mode.onchange = maj;
  maj();
};

/* Animation : l'arbre du schéma de Bernoulli se ramifie */
ANIMS.arbreBinomial = {
  titre: "L'arbre qui se ramifie : d'où vient $\\binom nk$",
  vb: [360, 300],
  etapes: [
    { d: 3, l: R`Une épreuve de Bernoulli : succès $S$ avec la probabilité $p$, échec $E$ avec $q=1-p$. Ici $p=0{,}4$.` },
    { d: 3.5, l: R`On la répète une deuxième fois, <b>indépendamment</b> : chaque branche se dédouble avec les mêmes probabilités. $4$ chemins.` },
    { d: 3.5, l: R`Troisième répétition : $8$ chemins. La probabilité d'un chemin est le produit le long des branches.` },
    { d: 5, l: R`Les chemins à <b>exactement $2$ succès</b> sont $SSE$, $SES$ et $ESS$. Il y en a $\binom32=3$, chacun de probabilité $p^2q$.` },
    { d: 5, l: R`D'où $P(X=2)=\binom32p^2q=3\times0{,}16\times0{,}6=0{,}288$. De même pour chaque $k$ : la loi $\mathcal B(3;0{,}4)$ apparaît en bas.` }
  ],
  rendu: function (S, k, t) {
    var E = ANIM.e, p = 0.4, W = 360;
    var ys = [18, 70, 122, 174], niv = k === 0 ? 1 : k === 1 ? 2 : 3, prog = k <= 2 ? E(t) : 1;
    var feuilles = []; ["S", "E"].forEach(function (a) { ["S", "E"].forEach(function (b) { ["S", "E"].forEach(function (c) { feuilles.push(a + b + c); }); }); });
    function xn(l, i) { var nb = Math.pow(2, l); return 14 + (W - 28) * (i + 0.5) / nb; }
    S.px.cercle(W / 2, ys[0], 4.5, "g-pt");
    var marque = {};
    if (k >= 3) feuilles.forEach(function (m, j) { if (m.split("S").length - 1 === 2) for (var l2 = 1; l2 <= 3; l2++) marque[l2 + "-" + Math.floor(j / Math.pow(2, 3 - l2))] = true; });
    for (var l = 1; l <= niv; l++) {
      var nb = Math.pow(2, l), f = l === niv ? prog : 1;
      for (var i = 0; i < nb; i++) {
        var px = l === 1 ? W / 2 : xn(l - 1, Math.floor(i / 2)), x = xn(l, i), succ = i % 2 === 0;
        var vert = !!marque[l + "-" + i];
        S.px.seg(px, ys[l - 1] + 5, ANIM.l(px, x, f), ANIM.l(ys[l - 1] + 5, ys[l] - 8, f), "a-branche", { style: vert ? "stroke:var(--vert);stroke-width:2.6" : null, opacity: k >= 3 && !vert ? 0.4 : 1 });
        if (f > 0.9) {
          S.px.txt(x, ys[l] + 4, succ ? "S" : "E", succ ? "b" : "r", "middle", { "font-size": 13 });
          if (l <= 2 || niv === l) S.px.txt((px + x) / 2 + (succ ? -9 : 9), (ys[l - 1] + ys[l]) / 2, succ ? "p" : "q", "", "middle", { "font-size": 10, style: "fill:var(--encre3)" });
        }
      }
    }
    if (niv === 3 && prog > 0.9) {
      for (var j = 0; j < 8; j++) {
        var m = feuilles[j], ks = m.split("S").length - 1, x3 = xn(3, j), vert2 = k >= 3 && ks === 2;
        var expr = ks === 0 ? "q³" : ks === 3 ? "p³" : ks === 1 ? "pq²" : "p²q";
        S.px.txt(x3, 198, m, vert2 ? "" : "", "middle", { "font-size": 10, style: vert2 ? "fill:var(--vert);font-weight:700" : "fill:var(--encre2)" });
        S.px.txt(x3, 212, expr, "", "middle", { "font-size": 10, style: vert2 ? "fill:var(--vert);font-weight:700" : "fill:var(--encre3)" });
      }
    }
    if (k >= 4) {
      var L = [0.216, 0.432, 0.288, 0.064], o = E(ANIM.p(t, 0, 0.6));
      S.px.seg(70, 282, 290, 282, "g-axe");
      for (var q = 0; q <= 3; q++) {
        var x0 = 98 + q * 55, h = L[q] / 0.45 * 54 * o;
        S.px.rect(x0 - 14, 282 - h, 28, h, "", { style: "fill:" + (q === 2 ? "var(--vert)" : "var(--bleu)") + ";fill-opacity:.55" });
        S.px.txt(x0, 278 - h, ANIM.nf(L[q], 3), "", "middle", { "font-size": 10, opacity: o });
        S.px.txt(x0, 295, "k = " + q, "", "middle", { "font-size": 10, style: "fill:var(--encre3)" });
      }
    } else if (k === 3) {
      S.px.math(40, 232, 280, 40, R`$P(X=2)=3\times p^2q$`, { opacity: E(t) });
    }
  }
};

/* Animation : la planche de Galton (simulation fixée : les mêmes billes à chaque lecture) */
ANIMS.galton = {
  titre: "La planche de Galton",
  vb: [360, 300],
  etapes: [
    { d: 3.5, l: R`Six rangées de clous. À chaque clou, la bille part à droite ou à gauche avec la même probabilité $\frac12$, indépendamment des autres clous.` },
    { d: 5, l: R`Une bille : son chemin est une suite de $6$ choix. Elle arrive dans la case $k$, où $k$ est le nombre de fois où elle est partie <b>à droite</b>.` },
    { d: 6, l: R`D'autres billes : les cases du milieu se remplissent plus vite, car beaucoup plus de chemins y mènent ($20$ chemins vers la case $3$, un seul vers la case $0$).` },
    { d: 7, l: R`$640$ billes : l'histogramme prend la forme d'une cloche.` },
    { d: 4.5, l: R`En pointillés, les effectifs théoriques $640\times\binom6k\left(\frac12\right)^6$ : la case d'arrivée suit la loi binomiale $\mathcal B\left(6;\frac12\right)$.` }
  ],
  _billes: null,
  rendu: function (S, k, t) {
    var A = ANIMS.galton, NB = 640, R6 = 6, W = 360;
    if (!A._billes) {
      var g = 20261110 >>> 0, alea = function () { g = (g * 1664525 + 1013904223) >>> 0; return g / 4294967296; };
      A._billes = []; for (var b = 0; b < NB; b++) { var ch = []; for (var r = 0; r < R6; r++) ch.push(alea() < 0.5 ? 1 : 0); A._billes.push(ch); }
    }
    var x0 = W / 2, dx = 22, y0 = 22, dy = 20, yBas = 160, H = 292;
    function clouX(r, i) { return x0 + (i - r / 2) * dx; }
    for (var r = 0; r < R6; r++) for (var i = 0; i <= r; i++) S.px.cercle(clouX(r, i), y0 + r * dy, 2.6, "", { style: "fill:var(--encre2)" });
    for (var c = 0; c <= 7; c++) S.px.seg(x0 + (c - 3.5) * dx, yBas - 6, x0 + (c - 3.5) * dx, H, "a-branche");
    S.px.seg(x0 - 4 * dx, H, x0 + 4 * dx, H, "g-axe");
    var nb;
    if (k === 0) { nb = 0; }
    else if (k === 1) { nb = 1; }
    else if (k === 2) { nb = 1 + Math.round(29 * E(t)); }
    else if (k === 3) { nb = 30 + Math.round((NB - 30) * ANIM.e(t)); }
    else nb = NB;
    function E(x) { return ANIM.e(x); }
    var cases = [0, 0, 0, 0, 0, 0, 0];
    var nbH = k === 1 ? (t > 0.88 ? 1 : 0) : nb;
    for (var b2 = 0; b2 < Math.min(nbH, NB); b2++) { var s = 0; A._billes[b2].forEach(function (v) { s += v; }); cases[s]++; }
    var hMax = 240, echelle = (H - yBas) / hMax;
    function caseX(j) { return x0 + (j - 3) * dx; }
    for (var j = 0; j <= 6; j++) {
      var h = cases[j] * echelle;
      if (h > 0) S.px.rect(caseX(j) - dx / 2 + 2, H - h, dx - 4, h, "", { style: "fill:var(--bleu);fill-opacity:.5" });
      S.px.txt(caseX(j), yBas - 9, String(j), "", "middle", { "font-size": 10, style: "fill:var(--encre3)" });
      if (k >= 2) S.px.txt(caseX(j), H - h - 3, String(cases[j]), "b", "middle", { "font-size": 9 });
    }
    if (k === 1) {
      var ch1 = A._billes[0], u = Math.min(1, t * 1.15) * (R6 + 1), etape = Math.floor(u), fr = u - etape;
      var pos = 0, pts = [[x0, y0 - 14]];
      for (var r2 = 0; r2 < R6; r2++) { pts.push([clouX(r2, pos) , y0 + r2 * dy - 7]); pos += ch1[r2]; }
      pts.push([caseX(pos), yBas + 4]);
      for (var q = 1; q < pts.length && q <= etape; q++) S.px.seg(pts[q - 1][0], pts[q - 1][1], pts[q][0], pts[q][1], "g-c2", { "stroke-width": 1.8 });
      var cur = etape >= pts.length - 1 ? pts[pts.length - 1] : [ANIM.l(pts[etape][0], pts[etape + 1][0], fr), ANIM.l(pts[etape][1], pts[etape + 1][1], fr)];
      S.px.cercle(cur[0], cur[1], 5, "g-pt2");
      var mots = ch1.map(function (v) { return v ? "D" : "G"; }).join(" ");
      S.px.txt(10, 22, "chemin : " + mots, "r", "start", { "font-size": 12 });
      S.px.txt(10, 40, "nombre de D = " + ch1.reduce(function (a, v) { return a + v; }, 0), "r", "start", { "font-size": 12 });
    }
    if (k >= 2) S.px.txt(10, 22, nb + (nb > 1 ? " billes" : " bille"), "b", "start", { "font-size": 13 });
    if (k >= 4) {
      var th = [1, 6, 15, 20, 15, 6, 1], o = ANIM.e(ANIM.p(t, 0, 0.5));
      for (var j2 = 0; j2 <= 6; j2++) { var ht = NB * th[j2] / 64 * echelle; S.px.rect(caseX(j2) - dx / 2 + 1, H - ht, dx - 2, ht, "", { style: "fill:none;stroke:var(--rouge);stroke-width:1.6;stroke-dasharray:4 3", opacity: o }); }
      S.px.txt(W - 10, 22, "théorie : 640 × C(6,k)/64", "r", "end", { "font-size": 11, opacity: o });
    }
  }
};
