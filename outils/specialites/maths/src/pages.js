/* ---------- Pages transversales : l'épreuve, les ressources ---------- */
var PAGES = (function () {
  var F = TeX.fmt;
  function riche(h) {
    return F(String(h).replace(/\[(def|prop|thm|ex|meth|piege|hist)(?:\|([^\]]*))?\]([\s\S]*?)\[\/\]/g, function (_, t, titre, corps) {
      var L = { def: "Définition", prop: "Propriété", thm: "Théorème", ex: "Exemple", meth: "Méthode", piege: "Piège", hist: "Histoire" };
      return '<div class="boite ' + t + '"><span class="lab">' + L[t] + (titre ? " · " + titre : "") + '</span><div class="corps">' + corps + "</div></div>";
    }).replace(/\[py\]([\s\S]*?)\[\/py\]/g, function (_, c) { return '<div class="code"><div class="bar">Python</div><pre>' + c.replace(/^\n/, "").replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</pre></div>"; }));
  }
  var EPREUVE = String.raw`
<div class="fil"><a href="#accueil">Accueil</a> › Préparer le bac</div>
<h1>L'épreuve de spécialité</h1>
<p>Ce qui suit est tiré du texte officiel qui définit l'épreuve : note de service du 11 septembre 2026, publiée au <b>Bulletin officiel spécial n° 4 du 17 septembre 2026</b> (même numéro que les autres épreuves de spécialité, qui s'appliquent à compter de la session 2027).</p>
<div class="tab-wrap"><table>
<tr><th>Durée</th><td>4 heures, épreuve écrite.</td></tr>
<tr><th>Coefficient</th><td>16 (sur un total de 100 au baccalauréat général), comme chaque épreuve de spécialité.</td></tr>
<tr><th>Programme</th><td>Le programme de spécialité de <b>Terminale</b> en vigueur ; les notions de <b>Première</b> peuvent être mobilisées. Le texte de 2026 ne prévoit <b>aucune partie exclue</b> : tout le programme peut tomber.</td></tr>
<tr><th>Structure</th><td><b>Quatre exercices indépendants</b>, chacun noté sur 4 à 8 points ; le sujet aborde une grande variété des contenus du programme.</td></tr>
<tr><th>Notation</th><td>Sur 20 points, dont <b>2 points de maîtrise de la langue</b> : orthographe, syntaxe, capacité à formuler un raisonnement, vocabulaire juste et adapté.</td></tr>
<tr><th>Calculatrice</th><td>Le sujet précise si elle est autorisée, « dans les conditions précisées par les textes en vigueur » : en pratique, calculatrice avec <b>mode examen</b> activé, ou calculatrice « type collège » sans mémoire.</td></tr>
<tr><th>Oral de contrôle</th><td>Au second groupe : 20 minutes de préparation, 20 minutes d'entretien sur au moins deux questions de parties différentes du programme ; calculatrice autorisée.</td></tr>
</table></div>
<div class="boite piege"><span class="lab">À ne pas confondre</span><div class="corps"><p>La partie « automatismes » sans calculatrice, sous forme de QCM, appartient à l'<b>épreuve anticipée de mathématiques</b> passée en fin de Première, pas à l'épreuve de spécialité de Terminale. Les automatismes restent indispensables : ils font gagner du temps partout.</p><p>Nouveau programme : un programme de Terminale rénové a été publié au BO du 2 avril 2026, mais il n'entre en application qu'à la rentrée 2027. <b>Pour le bac 2027, c'est le programme de 2019 qui s'applique</b> : celui de ce site.</p></div></div>

<h2>Ce que l'on trouve dans les sujets</h2>
<p>Sur les sujets de 2024 à 2026 publiés par l'APMEP, presque chaque sujet contient : un exercice de <b>probabilités</b> (arbre, loi binomiale), un exercice de <b>géométrie dans l'espace</b>, un exercice sur les <b>suites</b> (récurrence, limite, algorithme de seuil en Python), un exercice sur les <b>fonctions</b> (limites, dérivée, convexité, logarithme, équation différentielle). Les questions de type <b>vrai/faux à justifier</b> sont fréquentes : une réponse non justifiée ne rapporte rien.</p>

<h2>La méthode, pas à pas</h2>
<ol>
<li><b>Lire tout le sujet (10 minutes).</b> Repère les quatre thèmes et les questions que tu sais faire. Commence par l'exercice où tu es le plus à l'aise.</li>
<li><b>Gérer le temps.</b> Compte environ 50 minutes par exercice, et garde 15 minutes pour relire. Un exercice sur 4 points mérite moins de temps qu'un exercice sur 8.</li>
<li><b>Ne pas rester bloqué.</b> Les questions s'enchaînent, mais le sujet donne souvent le résultat à démontrer : tu peux l'<b>admettre</b> pour la suite (écris-le : « D'après la question 2, admise… »).</li>
<li><b>Justifier.</b> Cite le théorème et vérifie ses hypothèses : « $f$ est continue et strictement croissante sur $[1;2]$… d'après le corollaire du théorème des valeurs intermédiaires… ».</li>
<li><b>Rédiger en phrases.</b> Deux points sur vingt portent sur la langue : des phrases complètes, des connecteurs (« donc », « or », « par conséquent »), un vocabulaire exact (« croissante », pas « qui monte »).</li>
<li><b>Utiliser la calculatrice pour vérifier</b> : tableau de valeurs pour un seuil, valeur approchée d'une limite, signe d'une dérivée. Mais la justification reste à écrire.</li>
<li><b>Conclure dans le contexte</b> : « La superficie dépassera 14 hectares en 2042 », pas seulement « $n=18$ ».</li>
</ol>

<h2>Un corrigé commenté</h2>
<p><b>Sujet : bac 2025, Métropole, 17 juin 2025 (sujet 1), exercice 4, partie A</b> (<a href="https://www.apmep.fr/IMG/pdf/Metro_J1_17_06_2025_DV.pdf" target="_blank" rel="noopener">sujet sur le site de l'APMEP</a>). Résumé de l'énoncé : la superficie (en hectares) recouverte par la posidonie au 1er juillet de l'année $2024+n$ est $u_n$, avec $u_0=1$ et $u_{n+1}=-0{,}02u_n^2+1{,}3u_n$. On note $h(x)=-0{,}02x^2+1{,}3x$, admise croissante sur $[0;20]$.</p>
<div class="boite ex"><span class="lab">Question 1 · Calculer $u_1$</span><div class="corps"><p>$u_1=h(u_0)=-0{,}02\times1^2+1{,}3\times1=1{,}28$. Au 1er juillet 2025, la posidonie recouvrirait $1{,}28$ ha.</p><p class="stylo">Commentaire : on conclut dans le contexte, avec l'unité.</p></div></div>
<div class="boite ex"><span class="lab">Question 2a · Montrer que $1\leq u_n\leq u_{n+1}\leq20$</span><div class="corps"><p>Pour $n\in\N$, $P(n)$ : « $1\leq u_n\leq u_{n+1}\leq20$ ».</p><p><b>Initialisation</b> : $u_0=1$ et $u_1=1{,}28$, donc $1\leq1\leq1{,}28\leq20$.</p><p><b>Hérédité</b> : soit $k\in\N$ tel que $1\leq u_k\leq u_{k+1}\leq20$. La fonction $h$ est croissante sur $[0;20]$, donc $h(1)\leq h(u_k)\leq h(u_{k+1})\leq h(20)$, c'est-à-dire $1{,}28\leq u_{k+1}\leq u_{k+2}\leq18$, d'où $1\leq u_{k+1}\leq u_{k+2}\leq20$.</p><p><b>Conclusion</b> : par récurrence, $P(n)$ est vraie pour tout $n\in\N$.</p><p class="stylo">Commentaire : c'est la question la plus rentable. Le correcteur attend le mot « croissante » et le calcul de $h(1)$ et $h(20)$.</p></div></div>
<div class="boite ex"><span class="lab">Question 2b · En déduire que $(u_n)$ converge</span><div class="corps"><p>D'après 2a, la suite est croissante ($u_n\leq u_{n+1}$) et majorée par $20$. Toute suite croissante et majorée converge : $(u_n)$ converge vers une limite $L$, et $1\leq L\leq20$.</p></div></div>
<div class="boite ex"><span class="lab">Question 2c · Justifier que $L=15$</span><div class="corps"><p>$h$ est continue sur $[0;20]$ (fonction polynôme) et $u_{n+1}=h(u_n)$ : la limite vérifie $h(L)=L$. Or $h(x)=x\iff-0{,}02x^2+0{,}3x=0\iff-0{,}02x(x-15)=0\iff x=0$ ou $x=15$. Comme $L\geq1$, $L=15$.</p><p class="stylo">Commentaire : l'argument « $h$ continue » est indispensable (chapitre 4) ; l'exclusion de $0$ grâce à $L\geq1$ aussi.</p></div></div>
<div class="boite ex"><span class="lab">Question 3 · Seuil de 14 hectares</span><div class="corps"><p>a. La suite converge vers $15>14$ : l'intervalle ouvert $]14;16[$ contient $15$, donc il contient tous les termes à partir d'un certain rang. La superficie finira par dépasser $14$ ha.</p><p>b. Algorithme complété :</p>
[py]
def seuil():
    n = 0
    u = 1
    while u <= 14:
        n = n + 1
        u = -0.02 * u**2 + 1.3 * u
    return n
[/py]
<p>Il renvoie $18$ (calcul refait en Python : $u_{17}\approx13{,}79$ et $u_{18}\approx14{,}12$) : la superficie dépassera $14$ ha au 1er juillet 2042.</p></div></div>

<h2>Le Grand oral (session 2027)</h2>
<p>D'après la note de service du 10 septembre 2026 (même BO spécial n° 4), applicable à compter de la session 2027 :</p>
<ul><li><b>Coefficient 8</b> ; 20 minutes de préparation, 20 minutes d'épreuve ; aucun matériel hormis de quoi écrire (un tableau peut être disponible).</li>
<li>Tu présentes au jury <b>deux questions</b> adossées à tes deux spécialités (une par spécialité, ou transversales) ; le jury en choisit une.</li>
<li><b>Premier temps (10 min)</b>, debout : tu expliques pourquoi tu as choisi la question, tu la développes et tu y réponds. <b>Second temps (10 min)</b> : échange avec le jury, qui peut t'interroger sur tout le programme du cycle terminal de tes spécialités, en lien avec ta question.</li></ul>
<div class="boite meth"><span class="lab">Des idées de questions en maths</span><div class="corps"><ul><li>Peut-on démontrer une infinité de résultats en deux lignes ? (la récurrence)</li><li>Comment une calculatrice trouve-t-elle $\sqrt2$ ? (dichotomie, méthode de Héron)</li><li>Pourquoi l'exponentielle finit-elle toujours par dépasser les puissances ? (croissances comparées)</li><li>Combien de mots de passe faut-il essayer pour en casser un ? (dénombrement)</li><li>Une suite peut-elle modéliser une population ou une épidémie ? (suites $u_{n+1}=f(u_n)$)</li></ul><p>Choisis une question qui t'intéresse vraiment, et prépare un exemple chiffré que tu sais refaire au tableau.</p></div></div>`;

  var RESS = [
    ["Textes officiels", [
      ["Programme de spécialité de Terminale (PDF, Eduscol)", "https://eduscol.education.fr/document/24568/download", "Le texte qui fait foi : contenus, capacités, démonstrations et algorithmes de chaque chapitre (BO spécial n° 8 du 25 juillet 2019)."],
      ["Programmes et ressources en mathématiques, voie générale et technologique (Eduscol)", "https://eduscol.education.gouv.fr/5817/programmes-et-ressources-en-mathematiques-voie-gt", "Page officielle qui rassemble programmes, ressources d'accompagnement et informations sur les nouveaux programmes."],
      ["BO spécial n° 4 du 17 septembre 2026 (PDF)", "https://www.education.gouv.fr/sites/default/files/document/20260917boenjsspe4pdf-520753.pdf", "Définition des épreuves à compter de la session 2027 : épreuve de spécialité mathématiques (4 h, quatre exercices), Grand oral, maîtrise de la langue."]
    ]],
    ["Annales officielles et corrigés", [
      ["APMEP : annales de Terminale générale", "https://www.apmep.fr/Annales-Terminale-Generale", "Tous les sujets du bac depuis des décennies, avec corrigés gratuits rédigés par des professeurs. La référence."],
      ["APMEP : sujets 2026", "https://www.apmep.fr/Annee-2026", "Métropole, centres étrangers, Asie, Polynésie, Amérique du Nord, Antilles-Guyane…"],
      ["APMEP : sujets 2025", "https://www.apmep.fr/Annee-2025", "Les sujets 2025 avec leurs corrigés."],
      ["APMEP : exercices regroupés par type", "https://www.apmep.fr/Les-exercices-regroupes-par-type", "Pour travailler un thème précis d'annales en annales."]
    ]],
    ["Manuels", [
      ["Lelivrescolaire.fr : Mathématiques Terminale spécialité", "https://www.lelivrescolaire.fr/manuels/mathematiques-specialite-terminale-2020", "Manuel consultable en ligne sur le site de l'éditeur (certaines fonctions demandent un compte). Ordre : combinatoire, espace, suites, limites, continuité, dérivation…"],
      ["Sésamath : livret Première / Terminale spécialité", "https://manuel.sesamath.net/numerique/?ouvrage=cah1ere_tle_spe_2022", "Ressource libre et gratuite de l'association Sésamath, consultable en ligne."]
    ]],
    ["Cours et vidéos", [
      ["Yvan Monka, maths et tiques : cours de Terminale", "https://www.maths-et-tiques.fr/index.php/cours-maths/niveau-terminale", "Cours en PDF et vidéos courtes pour chaque chapitre, gratuits."],
      ["Yvan Monka sur YouTube", "https://www.youtube.com/@YMONKA", "Des centaines de vidéos de méthode, une notion par vidéo."],
      ["Hedacademy sur YouTube", "https://www.youtube.com/@hedacademy", "Exercices corrigés au tableau, du calcul de base au bac."]
    ]],
    ["S'exercer et programmer", [
      ["MathALÉA (CoopMaths)", "https://coopmaths.fr/alea/", "Exercices générés aléatoirement, avec correction : idéal pour les automatismes."],
      ["Basthon : Python dans le navigateur", "https://basthon.fr/", "Pour tester les programmes Python du site sans rien installer."],
      ["GeoGebra Calculatrice", "https://www.geogebra.org/calculator", "Tracer une courbe, une suite, une tangente, pour vérifier une conjecture."],
      ["Site de mathématiques de l'académie de Nancy-Metz", "https://sites.ac-nancy-metz.fr/mathematiques/", "Actualités officielles du bac, textes, ressources des professeurs."]
    ]]
  ];
  function ressources() {
    var h = '<div class="fil"><a href="#accueil">Accueil</a> › Préparer le bac</div><h1>Ressources</h1><p>Chaque lien a été vérifié. Les manuels payants (Hachette, Nathan, Hatier, Bordas…) ne sont pas listés : ton lycée t\'en prête souvent un.</p>';
    RESS.forEach(function (g) {
      h += "<h2>" + g[0] + "</h2>";
      g[1].forEach(function (r) { h += '<div class="annale"><b><a href="' + r[1] + '" target="_blank" rel="noopener">' + r[0] + "</a></b><br>" + r[2] + "</div>"; });
    });
    h += '<h2>À propos de ce site</h2><p>Contenu original, rédigé d\'après le programme officiel ; les exercices sont inventés pour le site (signalé à chaque fois) et leurs résultats recalculés par programme ; les références d\'annales renvoient aux sujets officiels publiés par l\'APMEP. Les formules sont affichées en MathML, avec une police mathématique réduite tirée de STIX Two Math (licence SIL Open Font License 1.1, fichier <code>OFL-STIX.txt</code>).</p>';
    return h;
  }
  return {
    epreuve: function () { return riche(EPREUVE); },
    ressources: ressources,
    texteEpreuve: EPREUVE,
    texteRessources: RESS.map(function (g) { return g[0] + " " + g[1].map(function (r) { return r[0] + " " + r[2]; }).join(" "); }).join(" ")
  };
})();
