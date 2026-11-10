/* ===================== Pages transversales : l'épreuve, les ressources ===================== */
C("ep-mystere", String.raw`
def mystere(t, i):
    if i == len(t):
        return 0
    if t[i] % 2 == 0:
        return 1 + mystere(t, i + 1)
    return mystere(t, i + 1)`, { fichier: "sujet.py", verif: "print(mystere([4, 7, 2, 9, 6], 0))", out: "3", montrer: false });

C("ep-copie-q4", String.raw`
def nb_pairs(t):
    """Renvoie le nombre d'éléments pairs de la liste d'entiers t."""
    n = 0
    for x in t:
        if x % 2 == 0:
            n = n + 1
    return n

print(nb_pairs([4, 7, 2, 9, 6]), nb_pairs([]))`, { fichier: "copie.py", out: "3 0" });

var PAGE_EPREUVE = {
  titre: "L’épreuve de NSI",
  sous: "Format officiel pour la session 2027, méthode pas à pas pour l’écrit et la partie pratique, copie commentée, Grand oral.",
  html: `
<div class="chiffres"><div><b>3 h 30</b><span>partie écrite, sur 20, coefficient 0,75</span></div><div><b>1 h</b><span>partie pratique sur ordinateur, sur 20, coefficient 0,25</span></div><div><b>16</b><span>coefficient de la spécialité dans le bac</span></div><div><b>2 / 20</b><span>maîtrise de la langue à l’écrit (nouveau en 2027)</span></div></div>

<h2>Le format officiel</h2>
<p>Texte de référence : <b>note de service du 11 septembre 2026</b> (BO spécial n° 4 du 17 septembre 2026), applicable <b>à partir de la session 2027</b>. Elle remplace la note du 4 juillet 2025 (session 2026), dont elle garde la structure. L’organisation de la partie pratique est précisée par une seconde <b>note de service du 21 septembre 2026</b> (BO n° 38 du 8 octobre 2026).</p>
<div class="tab-wrap"><table>
<tr><th></th><th>partie écrite</th><th>partie pratique</th></tr>
<tr><td>durée</td><td>3 h 30</td><td>1 h</td></tr>
<tr><td>note</td><td>sur 20, coefficient 0,75</td><td>sur 20 (au demi-point), coefficient 0,25</td></tr>
<tr><td>contenu</td><td>3 exercices indépendants, tous à traiter</td><td>« programmer sur ordinateur une application informatique à partir d’un document fourni »</td></tr>
<tr><td>matériel</td><td>calculatrice non autorisée (mention portée sur les sujets)</td><td>un ordinateur avec Python</td></tr>
<tr><td>évaluation</td><td>copie corrigée ; 2 points sur 20 pour la maîtrise de la langue</td><td>dialogue avec un professeur-examinateur, qui suit au plus 4 candidats à la fois et ne peut pas être ton professeur de l’année</td></tr>
</table></div>
<p><b>Note de l’épreuve</b> = 0,75 × écrit + 0,25 × pratique, sur 20. Exemple : 12 à l’écrit et 16 en pratique donnent 0,75 × 12 + 0,25 × 16 = <b>13</b>. Cette note compte avec un <b>coefficient 16</b> dans le baccalauréat. Les candidats individuels ou d’établissements hors contrat sont dispensés de la pratique : leur note est celle de l’écrit.</p>
<h3>Sur quoi porte l’épreuve</h3>
<p>Sur <b>tout le programme de Terminale</b>. Les notions de Première non approfondies en Terminale « doivent être connues et mobilisables », mais elles « ne peuvent cependant pas constituer un ressort essentiel du sujet ».</p>
<div class="boite ex"><div class="lab"># et les parties exclues ?</div><p>Pour les sessions 2022 et 2023, quand l’écrit avait lieu au printemps, une note de service du 12 juillet 2021 retirait certaines parties du programme de l’évaluation. Ces dispositions ont été <b>abrogées</b>, et les notes de service en vigueur (session 2026 et session 2027) n’excluent <b>aucune</b> partie : tout le programme de Terminale peut tomber à l’écrit. Les sujets récents mélangent d’ailleurs plusieurs rubriques dans un même exercice (par exemple, en 2025 : « graphes et programmation orientée objet », « algorithmique, récursivité et files »).</p></div>
<h3>La partie pratique en détail</h3>
<p>Les sujets sont tirés d’une <b>banque nationale</b> publiée au plus tard le 24 mars de chaque session (adresse officielle donnée par la note de service : <code>sujets.examens-concours.gouv.fr/delos/public/bgt/nsi</code>). L’établissement retient une liste de sujets, le jury en attribue un à chaque candidat. L’examinateur remplit une fiche individuelle : une note sur 20 au demi-point et un commentaire.</p>
<p>Depuis la session 2026, un sujet est un petit projet : un document et un fichier Python fournis, puis une série de questions (compléter une fonction, écrire des tests, trouver et corriger une erreur, expliquer un résultat), avec des moments d’échange avec l’examinateur. Pour la session 2026, la banque comptait 23 sujets, publiés le 26 mars 2026, et la grille nationale évaluait quatre compétences : <b>programmation (35 %)</b>, <b>compréhension (25 %)</b>, <b>autonomie (20 %)</b> et <b>oral (20 %)</b>, chacune notée « insuffisant, fragile, suffisant ou maîtrisé » puis convertie en note sur 20 (d’après les documents académiques de la session 2026, par exemple celui de l’IREM de Lyon, juin 2026 ; la grille de 2027 sera confirmée avec la banque).</p>
<p class="muet petit">Avant 2026, la pratique comportait deux exercices notés sur 10 : un algorithme du programme à écrire, puis un programme « à trous » à compléter. Beaucoup d’annales en ligne suivent encore ce format : elles restent un bon entraînement.</p>
<h3>Oral de contrôle (second groupe)</h3>
<p>20 minutes de préparation, 20 minutes d’oral. L’examinateur propose au moins deux questions portant sur des parties différentes du programme.</p>

<h2>Méthode pour l’écrit, pas à pas</h2>
<ol>
<li><b>Lire tout le sujet (10 min).</b> Chaque exercice commence par « Cet exercice porte sur… » : repère les thèmes, commence par celui que tu maîtrises le mieux, et numérote clairement (Exercice 2, question 3.b).</li>
<li><b>Répartir le temps.</b> Environ 1 h par exercice, proportionnellement aux points, et 20 à 30 min de relecture. Ne reste jamais bloqué plus de 5 min sur une question : les questions suivantes sont souvent faisables en admettant le résultat d’avant.</li>
<li><b>Questions « que renvoie / qu’affiche ».</b> Fais un tableau des variables à chaque tour de boucle ou dessine la pile des appels (chapitre 2). Écris le résultat <b>et</b> la justification.</li>
<li><b>Questions de code.</b> Recopie la signature (<code>def f(t, x):</code>), indente nettement (des traits verticaux aident), réutilise les fonctions déjà définies dans le sujet, respecte l’interface imposée (pile, file, classe) et n’importe pas de bibliothèque que l’énoncé n’autorise pas.</li>
<li><b>Questions de justification.</b> Une phrase complète avec le vocabulaire exact : « cas de base », « appel récursif », « LIFO », « clé primaire », « coût linéaire ». Depuis 2027, l’orthographe, la syntaxe, le lexique et l’organisation du propos valent 2 points.</li>
<li><b>Relecture.</b> Un <code>return</code> mal placé (dans la boucle), un <code>self</code> oublié, un cas vide non traité : ce sont les erreurs qui coûtent le plus de points.</li>
</ol>

<h2>Méthode pour la partie pratique</h2>
<ol>
<li><b>Lis le document</b> et <b>exécute le fichier fourni tel quel</b> avant de toucher à quoi que ce soit : tu vois ce qui marche déjà.</li>
<li><b>Avance par petits pas</b> : une fonction, puis tout de suite un essai dans la console, puis des <code>assert</code> (chapitre 4).</li>
<li><b>Pour une question « trouver l’erreur »</b> : reproduis-la sur l’entrée la plus simple, lis la dernière ligne de la trace, formule la cause avant de corriger.</li>
<li><b>Prépare-toi à expliquer</b>, c’est une partie de la note. Questions typiques d’un examinateur : quels sont les paramètres et leurs types ? que renvoie la fonction ? écris sa docstring ; la fonction est-elle récursive, quel est son cas de base ? pourquoi la boucle se termine-t-elle ? pourquoi <code>for</code> plutôt que <code>while</code> ? quelle différence entre <code>/</code> et <code>//</code>, entre <code>==</code> et <code>is</code>, entre <code>sorted(t)</code> et <code>t.sort()</code> ? que représente <code>self</code> ? quel est le coût ?</li>
<li><b>Autonomie</b> : cherche d’abord seul, mais si tu es bloqué, demande à l’examinateur plutôt que de perdre tout le temps restant.</li>
</ol>
<p>Pour t’entraîner : les exercices « type épreuve pratique » de chaque chapitre, puis la banque officielle et les sites d’exercices de la page <a href="#ressources">Ressources</a>.</p>

<h2>Copie modèle commentée</h2>
<p class="muet">Exercice inventé pour le site (4 points), suivi d’une copie rédigée et des remarques d’un correcteur.</p>
<div class="exo"><div class="tete"><span class="t">sujet · récursivité</span><span class="etiq a">4 points</span></div><div class="corps">
<p>On considère la fonction suivante, où <code>t</code> est une liste d’entiers et <code>i</code> un indice.</p>[[ep-mystere|nosortie]]
<ol><li>Que renvoie <code>mystere([4, 7, 2, 9, 6], 0)</code> ? Détailler les appels. <span class="bareme">(1 pt)</span></li>
<li>Quel est le rôle de cette fonction ? Proposer un nom plus explicite. <span class="bareme">(1 pt)</span></li>
<li>Combien d’appels sont faits pour une liste de <i>n</i> éléments ? Que se passe-t-il avec une liste de 5 000 éléments ? <span class="bareme">(1 pt)</span></li>
<li>Écrire une version itérative. <span class="bareme">(1 pt)</span></li></ol></div></div>
<div class="copie">
<div class="ligne-c"><div><p><b>1.</b> mystere(t, 0) → 4 est pair : 1 + mystere(t, 1) → 7 impair : mystere(t, 2) → 2 pair : 1 + mystere(t, 3) → 9 impair : mystere(t, 4) → 6 pair : 1 + mystere(t, 5) → i = 5 = len(t) : cas de base, renvoie 0. En remontant : 0, 1, 1, 2, 2, 3. La fonction renvoie <b>3</b>.</p></div><div class="marge ok">Descente et remontée détaillées, cas de base nommé : 1/1.</div></div>
<div class="ligne-c"><div><p><b>2.</b> Elle compte les éléments pairs de t à partir de l’indice i. Nom proposé : <code>nb_pairs_depuis</code>.</p></div><div class="marge ok">Réponse précise (« à partir de l’indice i ») et nom explicite : 1/1.</div></div>
<div class="ligne-c"><div><p><b>3.</b> Il y a un appel par indice de 0 à n, donc n + 1 appels. Avec 5 000 éléments il y aurait 5 001 appels imbriqués, ça fait trop.</p></div><div class="marge">« Ça fait trop » est insuffisant : il fallait dire que la pile d’exécution dépasse la limite de 1 000 appels de Python, qui lève une <code>RecursionError</code>. 0,5/1.</div></div>
<div class="ligne-c"><div>[[ep-copie-q4|nosortie]]</div><div class="marge ok">Version itérative juste, avec docstring ; le cas de la liste vide fonctionne (renvoie 0). 1/1.</div></div>
</div>
<p><b>Total : 3,5 / 4.</b> Ce qui fait la différence : nommer les notions (cas de base, pile d’exécution, RecursionError) et justifier chaque réponse au lieu de donner seulement le résultat.</p>

<h2>Le Grand oral</h2>
<p>Note de service du 10 septembre 2026, applicable à partir de la session 2027 : <b>20 minutes de préparation, 20 minutes d’épreuve, coefficient 8</b>.</p>
<ul><li>Tu présentes au jury <b>deux questions</b> adossées à tes deux spécialités (une par spécialité, ou transversales). Le jury en choisit une.</li>
<li><b>Premier temps (10 min)</b>, debout : tu expliques pourquoi tu as choisi cette question, puis tu la développes et tu y réponds. Tu peux préparer un support pendant les 20 minutes ; il n’est pas évalué.</li>
<li><b>Second temps (10 min)</b> : échange avec le jury (deux professeurs, dont l’un représente une de tes spécialités), qui peut t’interroger sur tout le programme de cycle terminal de tes spécialités, en lien avec ta question.</li></ul>
<p>Pistes de questions en NSI, à construire avec ton professeur : « Un programme peut-il détecter tous les bugs d’un autre programme ? » (calculabilité, problème de l’arrêt) ; « Comment un GPS trouve-t-il un itinéraire ? » (graphes, recherche de chemin) ; « Pourquoi le cadenas HTTPS protège-t-il un paiement en ligne ? » (chiffrement symétrique et asymétrique) ; « La récursivité, élégance ou danger ? » (pile d’exécution, coût) ; « Comment une base de données gère-t-elle des millions d’accès en même temps ? » (SGBD).</p>`
};

var PAGE_RESSOURCES = {
  titre: "Ressources",
  sous: "Liens vérifiés en novembre 2026. Les liens s’ouvrent dans un nouvel onglet.",
  html: `
<h2>Textes officiels</h2>
<ul class="liens">
<li><a href="https://eduscol.education.fr/document/30010/download" target="_blank" rel="noopener">Programme de NSI de Terminale (PDF, Eduscol)</a> <span class="gratuit">gratuit</span><br><span class="src">annexe de l’arrêté du 19/07/2019, BO spécial n° 8 du 25/07/2019 : les six rubriques, contenus, capacités, commentaires</span></li>
<li><a href="https://eduscol.education.fr/document/30007/download" target="_blank" rel="noopener">Programme de NSI de Première (PDF, Eduscol)</a> <span class="gratuit">gratuit</span><br><span class="src">les notions à connaître et mobiliser</span></li>
<li><a href="https://eduscol.education.gouv.fr/2068/programmes-et-ressources-en-numerique-et-sciences-informatiques-voie-g" target="_blank" rel="noopener">Eduscol : programmes et ressources en NSI</a> <span class="gratuit">gratuit</span><br><span class="src">ressources d’accompagnement officielles, sujets zéro</span></li>
<li><a href="https://www.education.gouv.fr/bo/2026/Special4/MENE2622643N" target="_blank" rel="noopener">Note de service du 11/09/2026 : épreuve de NSI à partir de 2027</a><br><span class="src">BO spécial n° 4 du 17/09/2026</span></li>
<li><a href="https://www.education.gouv.fr/bo/2026/Hebdo38/MENE2624043N" target="_blank" rel="noopener">Note de service du 21/09/2026 : partie pratique de NSI à partir de 2027</a><br><span class="src">BO n° 38 du 8/10/2026 : banque de sujets, choix des sujets, fiche d’évaluation</span></li>
<li><a href="https://www.education.gouv.fr/bo/2026/Special4/MENE2622694N" target="_blank" rel="noopener">Note de service du 10/09/2026 : le Grand oral à partir de 2027</a></li>
<li><a href="https://sujets.examens-concours.gouv.fr/delos/public/bgt/nsi" target="_blank" rel="noopener">Banque nationale des sujets de la partie pratique</a><br><span class="src">adresse donnée par la note de service ; publiée au plus tard le 24 mars de chaque session</span></li>
</ul>
<h2>Annales de l’écrit</h2>
<ul class="liens">
<li><a href="https://sti.eduscol.education.fr/print/18214" target="_blank" rel="noopener">Eduscol STI : sujets officiels 2025 (centres étrangers, jours 1 et 2)</a> <span class="gratuit">gratuit</span><br><span class="src">sujets officiels ; les corrigés y sont réservés aux enseignants pendant un an</span></li>
<li><a href="https://pixees.fr/informatiquelycee/term/" target="_blank" rel="noopener">Pixees : sujets des épreuves écrites de 2021 à 2026</a> <span class="gratuit">gratuit</span><br><span class="src">tous les sujets classés par année et par centre</span></li>
<li><a href="https://www.sujetdebac.fr/annales/specialites/spe-numerique-informatique/" target="_blank" rel="noopener">Sujetdebac : annales de NSI</a> <span class="gratuit">gratuit</span><br><span class="src">site non officiel ; vérifie l’année et le format de chaque sujet</span></li>
</ul>
<h2>S’entraîner à programmer</h2>
<ul class="liens">
<li><a href="https://codex.forge.apps.education.fr/" target="_blank" rel="noopener">CodEx : le code par les exercices</a> <span class="gratuit">gratuit</span><br><span class="src">exercices Python et SQL corrigés, écrits par des professeurs, sans inscription, exécutés dans le navigateur ; idéal pour la partie pratique</span></li>
<li><a href="https://www.france-ioi.org/" target="_blank" rel="noopener">France-IOI</a> <span class="gratuit">gratuit</span><br><span class="src">parcours progressif d’algorithmique avec correction automatique</span></li>
<li><a href="https://pythontutor.com/" target="_blank" rel="noopener">Python Tutor</a> <span class="gratuit">gratuit</span><br><span class="src">dessine les variables, les objets, les références et la pile des appels : parfait pour les chapitres 1 et 2</span></li>
</ul>
<h2>Cours en ligne de professeurs</h2>
<ul class="liens">
<li><a href="https://glassus.github.io/terminale_nsi/" target="_blank" rel="noopener">Cours de Terminale NSI d’un professeur de lycée (glassus.github.io)</a> <span class="gratuit">gratuit</span><br><span class="src">tout le programme, exercices corrigés, sujets de la banque pratique commentés</span></li>
<li><a href="https://fjunier.forge.apps.education.fr/tnsi/" target="_blank" rel="noopener">Progression de Terminale NSI d’un professeur de lycée (forge.apps.education.fr)</a> <span class="gratuit">gratuit</span><br><span class="src">progression complète, synthèses de cours</span></li>
<li><a href="https://www.zonensi.fr/NSI/Terminale/home/" target="_blank" rel="noopener">ZoneNSI : Terminale</a> <span class="gratuit">gratuit</span></li>
</ul>
<h2>Documentation de Python (en français)</h2>
<ul class="liens">
<li><a href="https://docs.python.org/fr/3/tutorial/classes.html" target="_blank" rel="noopener">Tutoriel : les classes</a> <span class="gratuit">gratuit</span></li>
<li><a href="https://docs.python.org/fr/3/tutorial/errors.html" target="_blank" rel="noopener">Tutoriel : erreurs et exceptions</a> <span class="gratuit">gratuit</span></li>
<li><a href="https://docs.python.org/fr/3/tutorial/modules.html" target="_blank" rel="noopener">Tutoriel : les modules</a> <span class="gratuit">gratuit</span></li>
<li><a href="https://docs.python.org/fr/3/library/doctest.html" target="_blank" rel="noopener">Le module doctest</a> <span class="gratuit">gratuit</span></li>
</ul>
<h2>Manuels</h2>
<p>Aucun manuel de NSI de Terminale entièrement consultable gratuitement en ligne n’a été trouvé ; ton établissement peut te donner accès à une version numérique par l’ENT.</p>
<ul class="liens">
<li><b>Spécialité NSI Terminale, 24 leçons avec exercices corrigés</b> (Ellipses), T. Balabonski, S. Conchon, J.-C. Filliâtre, K. Nguyen <span class="payant">payant</span><br><span class="src">édition 2024, ISBN 978-2-340-09653-0 ; cours complet et exigeant, écrit par des enseignants-chercheurs</span></li>
<li><b>Numérique et sciences informatiques, spécialité Terminale</b> (Hachette Éducation) <span class="payant">payant</span><br><span class="src">manuel scolaire, souvent disponible en version numérique par l’ENT de l’établissement</span></li>
</ul>
<h2>Vidéos</h2>
<ul class="liens">
<li><a href="https://www.youtube.com/watch?v=pg5YeSsOLZU" target="_blank" rel="noopener">Récursivité — NSI Terminale</a> · Les Bons Profs (7 min)</li>
<li><a href="https://www.youtube.com/watch?v=Ft2yeWCPCQY" target="_blank" rel="noopener">Récursivité, calcul de puissance, appels visualisés avec Thonny</a> · Cédric Gerland (10 min)</li>
<li><a href="https://www.youtube.com/watch?v=0r-pSf3PwVQ" target="_blank" rel="noopener">Les structures de données : pile, file et liste</a> · NovelClass (5 min)</li>
<li><a href="https://www.youtube.com/watch?v=e6HTG-mXFg8" target="_blank" rel="noopener">Le vocabulaire de la programmation orientée objet</a> · École Hexagone (6 min)</li>
</ul>`
};
