/* ---------- Chapitre 5 : combinatoire et dénombrement ---------- */
var CH5 = {
  id: "ch5", num: 5, statut: "ok", partie: "Algèbre et géométrie", titre: "Combinatoire et dénombrement", court: "Dénombrement",
  sous: "Compter sans tout écrire : listes, arrangements, permutations, combinaisons.",
  resume: "Produit cartésien, $n^k$, $n!$, arrangements, $\\binom nk$, triangle de Pascal.",
  essentiel: [
    R`<b>Principe multiplicatif</b> : $\text{card}(A\times B)=\text{card}(A)\times\text{card}(B)$. <b>Principe additif</b> : on additionne les cardinaux d'ensembles deux à deux disjoints.`,
    R`Listes de $k$ éléments d'un ensemble à $n$ éléments (ordre, répétitions permises) : $n^k$. Un ensemble à $n$ éléments a $2^n$ parties.`,
    R`Listes de $k$ éléments <b>distincts</b> (ordre compte) : $n(n-1)\dots(n-k+1)=\frac{n!}{(n-k)!}$ ; permutations de $n$ éléments : $n!$.`,
    R`Parties à $k$ éléments (combinaisons, l'ordre ne compte pas) : $\binom nk=\frac{n!}{k!(n-k)!}$.`,
    R`$\binom nk=\binom n{n-k}$ ; relation de Pascal $\binom{n-1}{k-1}+\binom{n-1}{k}=\binom nk$ ; $\sum_{k=0}^n\binom nk=2^n$.`
  ],
  attendus: [
    R`Dans un problème de dénombrement, utiliser une représentation adaptée (ensembles, arbres, tableaux, diagrammes) et reconnaître les objets à dénombrer.`,
    R`Effectuer des dénombrements simples dans des situations issues de divers domaines (informatique, génétique, théorie des jeux, probabilités…).`,
    R`Démonstrations exigibles : $\sum_{k=0}^n\binom nk=2^n$ par dénombrement ; relation de Pascal (par le calcul et par une méthode combinatoire).`,
    R`Algorithmes : coefficients $\binom nk$ par la relation de Pascal ; génération des permutations ou tirage aléatoire d'une permutation ; parties à 2 ou 3 éléments.`
  ],
  premiere: R`
<ul><li>Arbres de probabilités, issues d'une expérience à plusieurs étapes.</li><li>Notations ensemblistes : $x\in A$, $A\subset E$, $A\cup B$, $A\cap B$, complémentaire $\overline A$.</li><li>Probabilité uniforme (équiprobabilité) : $P(A)=\frac{\text{card}(A)}{\text{card}(\Omega)}$ : le dénombrement sert à calculer ces probabilités.</li></ul>`,
  cours: [
    { id: "produit", titre: "Produit cartésien et principes de base", html: R`
[def|Cardinal, $k$-uplet, produit cartésien]Le <b>cardinal</b> d'un ensemble fini $A$, noté $\text{card}(A)$, est son nombre d'éléments. Un <b>couple</b> $(a;b)$ est une liste ordonnée de deux éléments, un <b>triplet</b> en a trois, un <b>$k$-uplet</b> (ou $k$-liste) en a $k$. Le <b>produit cartésien</b> $A\times B$ est l'ensemble des couples $(a;b)$ avec $a\in A$, $b\in B$ ; $A^k$ est l'ensemble des $k$-uplets d'éléments de $A$.[/]
[prop|Principe additif]Si $A_1,\dots,A_p$ sont deux à deux disjoints : $\text{card}(A_1\cup\dots\cup A_p)=\text{card}(A_1)+\dots+\text{card}(A_p)$.[/]
[prop|Principe multiplicatif]$\text{card}(A\times B)=\text{card}(A)\times\text{card}(B)$, et plus généralement $\text{card}(A_1\times\dots\times A_k)=\text{card}(A_1)\times\dots\times\text{card}(A_k)$.[/]
[ex|Menus]$3$ entrées, $4$ plats, $2$ desserts : un menu est un triplet, il y en a $3\times4\times2=24$. Avec un arbre : $3$ branches, puis $4$ sur chacune, puis $2$ : $24$ chemins.[/]
[piege|Couple ou paire ?]$(1;2)\neq(2;1)$ : dans un couple, l'ordre compte. Dans l'ensemble $\{1;2\}$, non : $\{1;2\}=\{2;1\}$.[/]` },
    { id: "listes", titre: "Listes avec répétition : $n^k$ ; parties d'un ensemble", html: R`
[thm|Nombre de $k$-uplets]Si $\text{card}(E)=n$, le nombre de $k$-uplets d'éléments de $E$ est $\text{card}(E^k)=n^k$.[/]
[ex|Codes et mots]Code PIN à $4$ chiffres : $10^4=10\,000$. Octet (mot de $8$ bits) : $2^8=256$. Mot de passe de $8$ caractères pris parmi $62$ (lettres minuscules, majuscules, chiffres) : $62^8\approx2{,}18\times10^{14}$.[/]
[thm|Parties d'un ensemble]Un ensemble à $n$ éléments a $2^n$ parties (sous-ensembles), en comptant l'ensemble vide et l'ensemble lui-même.[/]
<p><b>Pourquoi ?</b> On numérote les éléments $x_1,\dots,x_n$. Une partie $P$ correspond à un $n$-uplet de $\{0;1\}$ : on écrit $1$ en position $i$ si $x_i\in P$, $0$ sinon. Par exemple, avec $E=\{a;b;c\}$, la partie $\{a;c\}$ correspond à $(1;0;1)$. Il y a $2^n$ tels $n$-uplets.</p>
<p>Le même objet se lit de plusieurs façons : un <b>mot</b> de longueur $n$ sur l'alphabet $\{0;1\}$, un <b>chemin</b> dans un arbre binaire à $n$ niveaux, une <b>issue</b> d'une succession de $n$ épreuves de Bernoulli (succès / échec). C'est le pont avec la loi binomiale (chapitre 13).</p>` },
    { id: "arrangements", titre: "Listes sans répétition ; permutations ; factorielle", html: R`
[def|Factorielle]Pour $n\geq1$, $n!=1\times2\times\dots\times n$, et par convention $0!=1$. $5!=120$ ; $10!=3\,628\,800$.[/]
[thm|$k$-uplets d'éléments distincts]Si $\text{card}(E)=n$ et $1\leq k\leq n$, le nombre de $k$-uplets d'éléments <b>deux à deux distincts</b> de $E$ est
$$n(n-1)(n-2)\dots(n-k+1)=\frac{n!}{(n-k)!}.$$[/]
<p>Raison : $n$ choix pour le premier élément, $n-1$ pour le deuxième (il doit être différent), … , $n-k+1$ pour le $k$-ième.</p>
[ex|Podium]$8$ coureurs, podium (or, argent, bronze) : $8\times7\times6=336$ podiums possibles.[/]
[thm|Permutations]Une <b>permutation</b> de $E$ est un $n$-uplet de ses $n$ éléments, tous distincts (un « rangement »). Il y en a $n!$.[/]
[ex|Anagrammes]Les anagrammes de MATHS (lettres toutes différentes) : $5!=120$. Pour ANANAS (3 A, 2 N, 1 S), on divise par les permutations des lettres identiques : $\frac{6!}{3!\times2!}=60$.[/]` },
    { id: "combinaisons", titre: "Combinaisons et coefficients binomiaux", html: R`
[def|Combinaison]Une <b>combinaison</b> de $k$ éléments de $E$ est une <b>partie</b> de $E$ à $k$ éléments (l'ordre ne compte pas, pas de répétition). Leur nombre se note $\binom nk$ (« $k$ parmi $n$ »).[/]
[thm|Formules]Pour $0\leq k\leq n$ :
$$\binom nk=\frac{n(n-1)\dots(n-k+1)}{k!}=\frac{n!}{k!\,(n-k)!}.$$
En particulier $\binom n0=1$, $\binom n1=n$, $\binom n2=\frac{n(n-1)}2$.[/]
<p><b>Pourquoi diviser par $k!$ ?</b> Chaque partie à $k$ éléments peut être rangée de $k!$ façons : il y a donc $k!$ fois plus de $k$-uplets d'éléments distincts que de parties.</p>
<div data-anim="arbre"></div>
[ex|Équipes et poignées de main]Choisir une équipe de $5$ joueurs parmi $12$ : $\binom{12}5=792$. Dans un groupe de $20$ personnes, chacun serre la main de chacun : $\binom{20}2=190$ poignées de main. Mains de $5$ cartes dans un jeu de $52$ : $\binom{52}5=2\,598\,960$.[/]
[prop|Symétrie et relation de Pascal]$\binom nk=\binom n{n-k}$ (choisir les $k$ éléments qu'on prend revient à choisir les $n-k$ qu'on laisse).<br>Pour $1\leq k\leq n-1$ : $\binom{n-1}{k-1}+\binom{n-1}k=\binom nk$.[/]
<div data-w="pascal"></div>
[prop|Mots et chemins]$\binom nk$ est aussi le nombre de mots de longueur $n$ formés de $k$ lettres $a$ et $n-k$ lettres $b$ (on choisit les positions des $a$), et le nombre de chemins d'un arbre binaire à $n$ niveaux qui comptent exactement $k$ succès.[/]
[ex|Chemins dans un quadrillage]Pour aller de $(0;0)$ à $(4;3)$ par des pas « droite » ou « haut », on fait $7$ pas dont $3$ vers le haut : $\binom73=35$ chemins.[/]` },
    { id: "modele", titre: "Choisir le bon modèle", html: R`
<div class="tab-wrap"><table><tr><th>L'ordre compte ?</th><th>Répétitions ?</th><th>Objet</th><th>Nombre</th></tr>
<tr><td>oui</td><td>oui</td><td>$k$-uplet (tirage successif avec remise)</td><td>$n^k$</td></tr>
<tr><td>oui</td><td>non</td><td>$k$-uplet d'éléments distincts (successif sans remise)</td><td>$\frac{n!}{(n-k)!}$</td></tr>
<tr><td>oui, tous</td><td>non</td><td>permutation</td><td>$n!$</td></tr>
<tr><td>non</td><td>non</td><td>combinaison (tirage simultané)</td><td>$\binom nk$</td></tr></table></div>
[meth|« Au moins un » : passer au complémentaire]Compter les cas où il n'y a <b>aucun</b> élément de la sorte voulue, puis soustraire du total.[/]
[ex|Au bac (Asie, 10 juin 2026)]On tire simultanément $5$ jetons parmi $32$ numérotés de $1$ à $32$. Tirages contenant au moins un multiple de $8$ ? Il y a $4$ multiples de $8$ ($8$, $16$, $24$, $32$), donc $28$ autres. Total : $\binom{32}5=201\,376$ ; sans multiple de $8$ : $\binom{28}5=98\,280$. Réponse : $201\,376-98\,280=103\,096$.[/]
[ex|Tirages avec remise (Centres étrangers, 6 juin 2024)]$3$ tirages successifs avec remise parmi $8$ jetons : $8^3=512$ tirages ; sans répétition : $8\times7\times6=336$ ; avec au moins une répétition : $512-336=176$.[/]
<p><span class="tag hp">Pour aller plus loin</span> Combinaisons avec répétition (choisir $k$ éléments parmi $n$ en autorisant les répétitions, sans ordre) : $\binom{n+k-1}k$. Approfondissement non exigible.</p>` }
  ],
  pieges: [
    { t: "Ordre ou pas ordre ?", h: R`« Tirer simultanément » ⟹ pas d'ordre : $\binom nk$. « Tirer successivement » ⟹ ordre : $n^k$ (avec remise) ou $\frac{n!}{(n-k)!}$ (sans remise).` },
    { t: "Additionner au lieu de multiplier", h: R`On multiplie pour des choix <b>successifs</b> (« et puis »), on additionne pour des cas <b>qui s'excluent</b> (« ou bien »).` },
    { t: "« Au moins un » compté directement", h: R`Compter « un multiple de 8, puis n'importe quoi » compte plusieurs fois les mêmes tirages. Passe par le complémentaire.` },
    { t: "$0!$", h: R`$0!=1$, donc $\binom n0=\binom nn=1$ : il y a une seule partie vide.` },
    { t: "Contrainte sur le premier élément", h: R`Code de 4 chiffres distincts dont le premier n'est pas $0$ : $9\times9\times8\times7=4\,536$, pas $\frac{10!}{6!}=5\,040$ (affirmation fausse du sujet de Métropole du 9 septembre 2025). Traite d'abord la case contrainte.` }
  ],
  demos: [
    { bo: true, t: "$\\sum_{k=0}^{n}\\binom nk=2^n$ par dénombrement", h: R`
<p>Soit $E$ un ensemble à $n$ éléments. On compte ses parties de deux façons.</p>
<p><b>Première façon.</b> Les parties de $E$ sont en bijection avec les $n$-uplets de $\{0;1\}$ (on écrit $1$ si l'élément est dans la partie, $0$ sinon). Il y en a $2^n$.</p>
<p><b>Deuxième façon.</b> On les range selon leur nombre d'éléments $k$, de $0$ à $n$. Il y a $\binom nk$ parties à $k$ éléments, et ces catégories sont deux à deux disjointes. Par le principe additif, le nombre de parties est $\binom n0+\binom n1+\dots+\binom nn$.</p>
<p>Les deux nombres comptent le même ensemble : $\sum_{k=0}^n\binom nk=2^n$.</p>
<p class="stylo">Le « double comptage » : un même ensemble compté de deux façons donne une égalité.</p>` },
    { bo: true, t: "Relation de Pascal, par le calcul", h: R`
<p>Pour $1\leq k\leq n-1$ :
$$\binom{n-1}{k-1}+\binom{n-1}k=\frac{(n-1)!}{(k-1)!\,(n-k)!}+\frac{(n-1)!}{k!\,(n-1-k)!}.$$
On met au même dénominateur $k!\,(n-k)!$ : on multiplie la première fraction par $\frac kk$ et la seconde par $\frac{n-k}{n-k}$ :
$$=\frac{(n-1)!\,k+(n-1)!\,(n-k)}{k!\,(n-k)!}=\frac{(n-1)!\,n}{k!\,(n-k)!}=\frac{n!}{k!\,(n-k)!}=\binom nk.$$</p>` },
    { bo: true, t: "Relation de Pascal, par une méthode combinatoire", h: R`
<p>Soit $E$ à $n$ éléments et $a$ un élément fixé de $E$. On compte les parties de $E$ à $k$ éléments en les séparant en deux groupes disjoints :</p>
<ul><li>celles qui <b>contiennent</b> $a$ : il reste à choisir $k-1$ éléments parmi les $n-1$ autres, soit $\binom{n-1}{k-1}$ ;</li><li>celles qui <b>ne contiennent pas</b> $a$ : on choisit les $k$ éléments parmi les $n-1$ autres, soit $\binom{n-1}k$.</li></ul>
<p>Par le principe additif : $\binom nk=\binom{n-1}{k-1}+\binom{n-1}k$.</p>` }
  ],
  algos: [
    { bo: true, t: "Coefficients binomiaux par la relation de Pascal", code: `def ligne_pascal(n):
    L = [1]                          # ligne 0
    for i in range(n):
        # chaque terme intérieur = somme des deux au-dessus
        L = [1] + [L[k - 1] + L[k] for k in range(1, len(L))] + [1]
    return L

print(ligne_pascal(7))
print(sum(ligne_pascal(7)), 2**7)`, sortie: `[1, 7, 21, 35, 35, 21, 7, 1]
128 128` },
    { bo: true, t: "Parties à 2 éléments d'un ensemble", code: `E = ["a", "b", "c", "d"]
parties = []
for i in range(len(E)):
    for j in range(i + 1, len(E)):   # j > i : pas de doublon
        parties.append([E[i], E[j]])
print(parties, len(parties))`, sortie: `[['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']] 6`,
      apres: R`<p>$\binom42=6$. Pour les parties à $3$ éléments, trois boucles imbriquées avec $i<j<k$.</p>` },
    { bo: true, t: "Générer toutes les permutations", code: `def permutations(L):
    if len(L) <= 1:
        return [L]
    resultat = []
    for i in range(len(L)):
        reste = L[:i] + L[i + 1:]           # on retire L[i]
        for p in permutations(reste):
            resultat.append([L[i]] + p)     # L[i] en tête
    return resultat

P = permutations([1, 2, 3])
print(P, len(P))`, sortie: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 6`,
      apres: R`<p>La fonction s'appelle elle-même (récursivité) : c'est un raisonnement par récurrence écrit en Python. $3!=6$.</p>` },
    { bo: true, t: "Tirer une permutation au hasard", code: `from random import randint

def melange(L):
    L = L[:]
    for i in range(len(L) - 1, 0, -1):
        j = randint(0, i)          # position au hasard parmi 0..i
        L[i], L[j] = L[j], L[i]    # échange
    return L

print(melange([1, 2, 3, 4, 5]))`, sortie: `(une permutation au hasard, différente à chaque exécution)`,
      apres: R`<p>C'est l'algorithme de Fisher-Yates : chacune des $n!$ permutations a la même probabilité d'être obtenue.</p>` }
  ],
  methodes: [
    { t: "Comment reconnaître le modèle ?", h: R`
<ol><li>Décris un résultat type avec un exemple concret : est-ce une liste ou un ensemble ?</li><li>Pose les deux questions : l'ordre compte-t-il ? les répétitions sont-elles possibles ?</li><li>Lis le tableau de la partie 5. En cas de doute, un petit arbre sur un cas réduit permet de vérifier.</li></ol>` },
    { t: "Comment dénombrer avec des contraintes ?", h: R`
<ul><li>Place d'abord les éléments contraints (premier chiffre non nul, lettres imposées…), puis les autres.</li><li>Découpe en cas disjoints et additionne (principe additif).</li><li>Pour « au moins un », passe par le complémentaire.</li></ul>` },
    { t: "Comment calculer $\\binom nk$ à la main ?", h: R`
<p>Utilise $\binom nk=\frac{n(n-1)\dots(n-k+1)}{k!}$ avec le plus petit des deux nombres $k$ et $n-k$ (symétrie) : $\binom{10}8=\binom{10}2=\frac{10\times9}2=45$. Les calculatrices ont une touche (souvent notée nCr ou Combinaison).</p>` }
  ],
  exos: [
    { niv: 1, t: "Codes et anagrammes", enonce: R`<ol><li>Combien de codes de $4$ chiffres (de $0$ à $9$) existe-t-il ? Combien ont leurs chiffres deux à deux distincts ?</li><li>Combien de codes de $4$ chiffres distincts dont le premier n'est pas $0$ ?</li><li>Combien d'anagrammes du mot ANANAS ?</li></ol>`,
      corrige: R`<ol><li>$10^4=10\,000$ codes ; à chiffres distincts : $10\times9\times8\times7=5\,040$.</li><li>$9$ choix pour le premier (pas $0$), puis $9$ (le $0$ revient, mais pas le premier), $8$, $7$ : $4\,536$.</li><li>$\frac{6!}{3!\,2!\,1!}=\frac{720}{12}=60$.</li></ol>` },
    { niv: 1, t: "Combinaisons", enonce: R`<ol><li>Calculer $\binom52$, $\binom63$, $\binom{10}8$.</li><li>Dans une classe de $30$ élèves, de combien de façons choisir $2$ délégués (sans distinction de rôle) ? Un délégué et un suppléant ?</li></ol>`,
      corrige: R`<ol><li>$\binom52=10$ ; $\binom63=20$ ; $\binom{10}8=\binom{10}2=45$.</li><li>Sans rôle : $\binom{30}2=\frac{30\times29}2=435$. Avec rôles (ordre) : $30\times29=870$.</li></ol>` },
    { niv: 2, t: "Au moins une femme", enonce: R`<p>Un comité de $3$ personnes est choisi parmi $6$ hommes et $4$ femmes.</p><ol><li>Combien de comités possibles ?</li><li>Combien contiennent au moins une femme ?</li><li>Combien contiennent exactement une femme ?</li></ol>`,
      corrige: R`<ol><li>$\binom{10}3=120$.</li><li>Complémentaire : comités sans femme $\binom63=20$, donc $120-20=100$.</li><li>Une femme parmi $4$ et deux hommes parmi $6$ : $4\times\binom62=4\times15=60$.</li></ol>` },
    { niv: 2, t: "Chemins", enonce: R`<p>Dans un quadrillage, on va du point $(0;0)$ au point $(6;4)$ par des pas d'une unité vers la droite ou vers le haut.</p><ol><li>Combien de pas fait-on ? Combien de chemins possibles ?</li><li>Combien de ces chemins passent par le point $(3;2)$ ?</li></ol>`,
      corrige: R`<ol><li>$10$ pas dont $4$ vers le haut : $\binom{10}4=210$ chemins.</li><li>De $(0;0)$ à $(3;2)$ : $\binom52=10$ ; de $(3;2)$ à $(6;4)$ : $\binom52=10$. Principe multiplicatif : $100$ chemins.</li></ol>` },
    { niv: 3, t: "Jetons et probabilités (type bac)", enonce: R`<p>Un sac contient $10$ jetons numérotés de $1$ à $10$.</p><p><b>Partie A.</b> On tire successivement $3$ jetons <b>avec remise</b> ; un tirage est la liste ordonnée des numéros.</p><ol><li>Combien de tirages possibles ?</li><li>Combien de tirages sans répétition de numéro ? En déduire le nombre de tirages avec au moins une répétition.</li></ol><p><b>Partie B.</b> On tire <b>simultanément</b> $3$ jetons.</p><ol start="3"><li>Combien de tirages possibles ?</li><li>Combien contiennent le jeton n° 10 ? En déduire la probabilité, les tirages étant équiprobables, d'obtenir le jeton n° 10.</li></ol>`,
      corrige: R`<ol><li>$10^3=1\,000$ ($3$-uplets avec répétition).</li><li>$10\times9\times8=720$ ; au moins une répétition : $1\,000-720=280$.</li><li>$\binom{10}3=120$.</li><li>On impose le n° 10 et on choisit les $2$ autres parmi $9$ : $\binom92=36$. Probabilité : $\frac{36}{120}=0{,}3$ (logique : chaque jeton a $3$ chances sur $10$ d'être dans la main).</li></ol>
<p class="stylo">Vérifié par énumération complète en Python (module itertools).</p>` }
  ],
  annales: [
    { ref: "Bac 2024, Centres étrangers, 6 juin 2024 (sujet 2), exercice 1, questions 1 et 2", url: "https://www.apmep.fr/IMG/pdf/Etranger_spe_J2_6_06_2024_DV.pdf", h: R`Trois tirages avec remise parmi $8$ jetons : nombre de tirages, sans répétition, avec au moins une répétition ; la question 7a fait aussi dénombrer les tirages de somme au moins $22$ (il y en a $10$).` },
    { ref: "Bac 2025, Métropole, 9 septembre 2025 (sujet 1), exercice 4, affirmation 1", url: "https://www.apmep.fr/IMG/pdf/Metropole_J1_sept_2025_DV_2.pdf", h: R`Codes de $4$ chiffres deux à deux distincts, premier chiffre non nul : « $5\,040$ » est faux, il y en a $4\,536$.` },
    { ref: "Bac 2026, Asie, 10 juin 2026 (sujet 2), exercice 4, affirmation 2", url: "https://www.apmep.fr/IMG/pdf/BAC_Spe_J2_Asie_juin_2026_FK.pdf", h: R`Tirages simultanés de $5$ jetons parmi $32$ contenant au moins un multiple de $8$ : $103\,096$ (vrai), par le complémentaire.` }
  ],
  retenir: R`
[thm|Principes]Additif (ensembles disjoints) : on additionne. Multiplicatif (produit cartésien, choix successifs) : on multiplie.[/]
<div class="tab-wrap"><table><tr><th>Objet</th><th>Ordre</th><th>Répétition</th><th>Nombre</th></tr>
<tr><td>$k$-uplets de $E$ ($\text{card }E=n$)</td><td>oui</td><td>oui</td><td>$n^k$</td></tr>
<tr><td>$k$-uplets d'éléments distincts</td><td>oui</td><td>non</td><td>$\frac{n!}{(n-k)!}$</td></tr>
<tr><td>Permutations</td><td>oui</td><td>non</td><td>$n!$</td></tr>
<tr><td>Parties à $k$ éléments</td><td>non</td><td>non</td><td>$\binom nk=\frac{n!}{k!(n-k)!}$</td></tr>
<tr><td>Toutes les parties</td><td colspan="2">—</td><td>$2^n$</td></tr></table></div>
[prop|Coefficients binomiaux]$\binom n0=\binom nn=1$ ; $\binom n1=n$ ; $\binom n2=\frac{n(n-1)}2$ ; $\binom nk=\binom n{n-k}$ ; $\binom{n-1}{k-1}+\binom{n-1}k=\binom nk$ ; $\sum_{k=0}^n\binom nk=2^n$.[/]
<p class="stylo">Simultané = combinaison. Successif = liste. « Au moins un » = complémentaire.</p>`,
  qcm: [
    { q: R`Combien de mots de $5$ lettres (avec ou sans sens) peut-on écrire avec l'alphabet de $26$ lettres ?`, c: [R`$26\times5$`, R`$26^5$`, R`$5^{26}$`, R`$\binom{26}5$`], r: 1, e: R`$5$-uplets d'un ensemble à $26$ éléments, répétitions permises : $26^5$.`, ref: "listes" },
    { q: R`Un ensemble à $6$ éléments possède combien de parties ?`, c: ["$6$", "$36$", "$64$", "$720$"], r: 2, e: R`$2^6=64$ (bijection avec les $6$-uplets de $\{0;1\}$).`, ref: "listes" },
    { q: R`$8$ coureurs, combien de podiums (or, argent, bronze) ?`, c: ["$24$", "$56$", "$336$", "$512$"], r: 2, e: R`Ordre, sans répétition : $8\times7\times6=336$.`, ref: "arrangements" },
    { q: R`Combien de façons de ranger $6$ livres différents sur une étagère ?`, c: ["$36$", "$120$", "$720$", "$46\\,656$"], r: 2, e: R`Permutations : $6!=720$.`, ref: "arrangements" },
    { q: R`$\binom{7}{2}=$`, c: ["$14$", "$21$", "$42$", "$49$"], r: 1, e: R`$\frac{7\times6}2=21$.`, ref: "combinaisons" },
    { q: R`$\binom{20}{18}=$`, c: ["$190$", "$380$", "$20$", "$18$"], r: 0, e: R`Symétrie : $\binom{20}{18}=\binom{20}2=190$.`, ref: "combinaisons" },
    { q: R`On tire simultanément $3$ boules parmi $9$. Le nombre de tirages est :`, c: [R`$9^3$`, R`$9\times8\times7$`, R`$\binom93$`, R`$3^9$`], r: 2, e: R`Simultané : pas d'ordre, pas de répétition. $\binom93=84$.`, ref: "modele" },
    { q: R`La relation de Pascal s'écrit :`, c: [R`$\binom nk=\binom{n-1}{k-1}+\binom{n-1}k$`, R`$\binom nk=\binom{n-1}k\times\binom{n-1}{k-1}$`, R`$\binom nk=\binom n{k-1}+\binom n{k+1}$`, R`$\binom nk=n\binom{n-1}k$`], r: 0, e: R`Chaque case du triangle est la somme des deux cases au-dessus.`, ref: "combinaisons" },
    { q: R`$\binom50+\binom51+\binom52+\binom53+\binom54+\binom55=$`, c: ["$25$", "$31$", "$32$", "$120$"], r: 2, e: R`$2^5=32$ : démonstration exigible par double comptage.`, ref: "combinaisons" },
    { q: R`Codes de $4$ chiffres distincts dont le premier n'est pas $0$ :`, c: ["$5\\,040$", "$4\\,536$", "$9\\,000$", "$3\\,024$"], r: 1, e: R`$9\times9\times8\times7=4\,536$ (piège du bac de septembre 2025).`, ref: "pieges" },
    { q: R`Comités de $3$ parmi $6$ hommes et $4$ femmes avec au moins une femme :`, c: ["$4$", "$60$", "$100$", "$120$"], r: 2, e: R`$\binom{10}3-\binom63=120-20=100$.`, ref: "modele" },
    { q: R`Le nombre de mots de $6$ lettres formés de $2$ « a » et $4$ « b » est :`, c: ["$12$", "$15$", "$30$", "$64$"], r: 1, e: R`On choisit les $2$ positions des « a » : $\binom62=15$.`, ref: "combinaisons" }
  ],
  cartes: [
    [R`Principe multiplicatif`, R`$\text{card}(A\times B)=\text{card}(A)\times\text{card}(B)$`],
    [R`Nombre de $k$-uplets d'un ensemble à $n$ éléments`, R`$n^k$`],
    [R`Nombre de parties d'un ensemble à $n$ éléments`, R`$2^n$`],
    [R`$k$-uplets d'éléments distincts`, R`$n(n-1)\dots(n-k+1)=\frac{n!}{(n-k)!}$`],
    [R`Nombre de permutations de $n$ éléments`, R`$n!$`],
    [R`$0!=$ ?`, R`$1$`],
    [R`$\binom nk$ (formule)`, R`$\frac{n!}{k!(n-k)!}$`],
    [R`$\binom n2=$ ?`, R`$\frac{n(n-1)}2$`],
    [R`Symétrie des coefficients binomiaux`, R`$\binom nk=\binom n{n-k}$`],
    [R`Relation de Pascal`, R`$\binom{n-1}{k-1}+\binom{n-1}k=\binom nk$`],
    [R`$\sum_{k=0}^n\binom nk=$ ?`, R`$2^n$`],
    [R`Tirage simultané de $k$ parmi $n$`, R`$\binom nk$ (combinaisons)`],
    [R`« Au moins un » : méthode`, R`Total moins les cas « aucun ».`],
    [R`Ligne $n=5$ du triangle de Pascal`, R`$1\;5\;10\;10\;5\;1$`]
  ]
};
