# Revisions_terminale — guide de passation pour Claude Code

Dépôt : `orhanYJ/Revisions_terminale` (public, GitHub Pages sur `main`).
Base publique : https://orhanyj.github.io/Revisions_terminale/

Ce fichier est écrit pour être placé à la racine du dépôt sous le nom `CLAUDE.md`.
Il résume ce que les sessions Claude.ai ont établi. En cas de doute sur l'état réel d'un site, le code du dépôt fait foi, pas ce fichier.

---

## 1. Contexte

- Cengiz (le père, qui pilote le projet, écrit en français, souvent à la voix, direct, préfère un court résumé des compromis avant d'implémenter) construit des sites de révision pour **Orhan**, son fils, en Terminale **BFI/ASIBA** à la Cité Scolaire Internationale Jacques Chirac (Martigues).
- Orhan et « le fils de Cengiz » sont **une seule personne**.
- Les sites sont des **PWA statiques**, un `index.html` autonome par dossier, installés sur l'écran d'accueil du téléphone.
- Les cours d'Orhan sont manuscrits : ils arrivent en photos. Les transcrire d'abord en fiches markdown, **signaler les passages illisibles au lieu de les combler**.

## 2. Les règles permanentes (à respecter à chaque modification)

1. **Content gate** : le contenu n'est écrit que sur ce qui a réellement été vu en cours. Ce qui n'a pas été traité reste un placeholder. Ne jamais pousser un contenu au-delà du point atteint par la classe.
2. **Un seul HTML autonome par site**, sans dépendance externe, qui fonctionne hors ligne (voir §7 pour les écarts connus).
3. **Pas de `localStorage`** pour les données utilisateur : la persistance passe par un JSON réinjecté dans un HTML téléchargé.
4. **Droit d'auteur** : pas de reproduction massive d'œuvres protégées (Friel, Atwood, Orwell, Ali). Localisateurs, descriptions, analyses. Les banques de citations relèvent de la citation courte à fin critique.
5. **Profondeur plutôt que survol** : moments textuels précis, références de page ou de chapitre.
6. **Interface simple.**
7. **Validation itérative** : un bloc livré et confirmé avant de passer au suivant.
8. **`node --check` sur tout le JS avant livraison** ; parité FR/EN vérifiée sur les sites bilingues.
9. **Lire la skill `frontend-design`** au début de toute session front, si elle est disponible.

Règles complémentaires :

- **Remplacer les fichiers au même nom.** Les URL et l'icône PWA sur le téléphone d'Orhan en dépendent. Ne jamais renommer un dossier de site.
- **Fiches mémo** : ce sont des travaux notés qu'Orhan rend à son professeur. Les sites ne fournissent **jamais** une fiche toute faite à rendre : modèle vierge, checklist de complétude, relecture de son propre brouillon. **Exception : physique-chimie** (décision de Cengiz, 13/10/2026) — chaque chapitre de `pc/` a sa fiche mémo **complète**, A4 recto-verso imprimable, limitée à l'exigible.
- **Schéma idée / exemple (DNL)** : chaque idée porte un exemple précis, voire deux. Une idée est un phénomène, un fait ou un processus ; l'exemple est le cas précis où on l'observe. Si l'exemple n'est pas dans le cours, en chercher un dans des sources valides et **signaler qu'il vient d'ailleurs**.
- **Corps du cours** : bilans, idées, explications, définitions seulement. Le détail des TP et activités va dans des panneaux repliables, fermés par défaut.
- **Hors programme** : la structure interne d'un cours est libre (du plus large au plus précis, expliquer le pourquoi et les mécanismes), mais ce qui dépasse le programme est marqué « hors programme ».
- **QCM** : majoritairement sur les idées du cours et les rappels de Première associés (avec renvoi vers la fiche) ; quelques questions de TP en série séparée.
- **Ne jamais stocker un jeton ou un identifiant** dans un fichier du dépôt, la mémoire ou un document.

**Publication (consigne de Cengiz, 12/10/2026)** : ne pas attendre qu'il demande « mets à jour le site ». Une fois une livraison validée (`node --check`, test du rendu), ouvrir la PR vers `main` et la fusionner aussitôt, pour que le site en ligne soit toujours à jour.

Préférence de travail de Cengiz : **conseiller de changer de modèle ou de niveau d'effort** quand une demande est trop triviale ou trop complexe pour le réglage actuel, et **proposer de scinder un site** quand son poids devient trop lourd.

---

## 3. Carte du dépôt

| Dossier | Contenu | Poids `index.html` | Pile |
|---|---|---|---|
| `svt/` | Spé SVT Terminale (Mme Philip) | ~544 Ko | JS natif, données en constantes |
| `pc/` | Spé Physique-Chimie | ~980 Ko (+ `anim/`) | JS natif |
| `dnl/` | DNL Histoire-Géo (M. Ros) — « Revision Atlas » | **~5,3 Mo** | React 18.2 UMD (cdnjs) |
| `philo/` | « L'Index raisonné » (M. Bellon) | ~2,3 Mo | React 18.2 UMD précompilé inline |
| `acl-ecrit/` | Hub ACL écrit : épreuve, méthode, atelier, boîte à outils, Twelfth Night | ~152 Ko | JS natif |
| `acl-lughnasa/` | *Dancing at Lughnasa* (Friel) | ~236 Ko | JS natif |
| `acl-bricklane/` | *Brick Lane* (Ali) | ~339 Ko | JS natif |
| `acl-oral/` | Hub ACL oral : cadrage + six poèmes | ~327 Ko | JS natif |
| `acl-oral-1984/` | *1984* (Orwell) | ~105 Ko | JS natif |
| `acl-oral-butler/` | *Parable of the Sower* (Butler) | ~829 Ko | JS natif |
| `italien/` | « La Grammatica » (LVB) | ~175 Ko | JS natif |
| `redpen/` | « The Red Pen » (anglais B1→C1) | ~231 Ko | JS natif |
| `cdm/` | Dossier CDM « Sensibiliser ou réguler » | ~35 Ko | JS natif |
| `medecine/` | « Protocole Santé » : initiation à la licence portail santé, test de 5 méthodes de travail | ~660 Ko | JS natif |
| `fenuareo/` | **Projet distinct** (apprentissage du reo tahiti), pas un site de révision d'Orhan | ~1,2 Mo | — |
| `test.html` | Reliquat d'un test de publication | — | à supprimer avec l'accord de Cengiz |

Chaque dossier de site contient la même structure : `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`. Certains ajoutent `motion.css` et `motion.js` (voir §5) ; tous les sites de révision (sauf `fenuareo/`) ajoutent `assistant.js`, le bouton « Demander à ChatGPT » (voir §5 bis).

Les sites ACL ont été **scindés pour le poids** : `acl-ecrit` → hub + `acl-lughnasa` + `acl-bricklane` ; `acl-oral` → hub + `acl-oral-1984` + `acl-oral-butler`. Chacun a sa propre icône dans une identité commune (ACL écrit : bleu marine et or, « reliure » ; ACL oral : orange sur anthracite) et des liens croisés.

---

## 4. Comment les sites fonctionnent

### Principe commun

Un site = un `index.html` qui contient son CSS, son JS et **ses données sous forme de constantes JavaScript**. Il n'y a ni base de données, ni build dans le dépôt : **modifier un site, c'est modifier ce fichier**. Cela rend les gros fichiers pénibles à éditer à la main. La méthode éprouvée :

- un script Python (écrit dans un fichier, pas en heredoc quand le contenu contient des apostrophes) qui insère ou remplace un bloc à une **ancre unique**, avec `assert texte.count(ancre) == 1` avant d'écrire ;
- caractères spéciaux en séquences d'échappement Unicode dans ces scripts ;
- validation immédiate (voir §8).

### SVT (`svt/`)

JS natif. Constantes principales dans `index.html` :

- `TERMINALE` : thèmes → parties → chapitres → unités, selon le **découpage de Mme Philip** (thème, chapitre, unités), pas seulement celui du BO. Tout nouveau contenu de Terminale respecte cette hiérarchie.
- `PREMIERE` : les 15 fiches de rappel de Première (complètes).
- `GLOSSAIRE` : environ 200+ termes, repérés automatiquement dans le texte (soulignés en pointillé, bulle de définition ; rubriques Définition · Où ça intervient · Attention · Voir aussi ; 2 premières occurrences par chapitre).
- `SCHEMAS` : schémas SVG interactifs (`SCHEMAS.mitose = {...}`).
- `QCM` (clés comme `t1u1`), `REDAC` (rédaction avec correction), `METHODE_PHILIP`, `SPECIMENS`, `ICONS`, `VOCAB`.

Direction artistique « végétale » : papier crème `#F7F4EC`, encre forêt `#17281E`, vert `#2F7D52`, citron `#B7D94C`. Mode sombre. Le mouvement est en deux couches : une écrite dans `index.html`, un complément dans `motion.css` / `motion.js` (voir §5).

Consigne de la prof : apprendre le vocabulaire listé et s'entraîner à rédiger seul plutôt que relire. Chaque unité est outillée en conséquence (vocabulaire, rédaction avec correction, QCM).

État : chapitre 1 « L'origine du génotype des individus » **terminé** (le chapitre 2 de Mme Philip s'ouvre sur « Nous avons vu les transferts verticaux »). Il compte deux unités seulement, d'après l'en-tête de la fiche de TP « Chap 1 – Unité 2 » : unité 1 (`t1u1`, clones), unité 2 (`t1u2`, brassages) et sa suite sur une page séparée (`t1u2b`, « Accidents génétiques lors de la méiose », ajoutée le 05/10/2026 depuis l'exposé collectif « support Eva », le TP globines et les notes d'Orhan). Il n'y a pas d'unités 3 et 4. Le diaporama des accidents a été rédigé par les élèves et contient des erreurs (corrigées dans le site, signalées en encadrés). Chapitre 2 « La complexification des génomes » : deux pages, `t2` (parties I et II, transferts horizontaux, transduction en simple mention) et `t2b` (partie III, endosymbioses, rédigée le 09/10/2026 d'après les diapositives 32 à 42, la ressource « Endosymbioses » et le TP ECE chloroplastes ; le 12/10/2026, d'après la version annotée du diaporama — « La séance en distanciel du 5 Octobre commence ici » (diapo 1), « Le cours du 12 Octobre commence ici » (diapo 16) — ajout du tableau d'arguments pour / contre corrigé par Mme Philip (diapos 28-29), de son commentaire sur la membrane interne du chloroplaste (diapo 30) et, dans `t2`, de la partie « L'étendue des transferts horizontaux dans le vivant » (documents de manuels Nathan / Bordas, activité NCBI en panneau repliable). La feuille du TP ECE chloroplastes n'est toujours pas corrigée). Chapitre 3 « L'évolution du génome au sein des populations » (page `t3`, ouverte le 14/10/2026 d'après le diaporama du chapitre et la fiche « T1C3_A1 Modélisation écarts HW ») : la classe est allée jusqu'à la diapositive 16 en distanciel (Cengiz a écrit « page 1- », lu comme 16 : sur clavier AZERTY, « - » est la touche du 6). Rédigé : partie I complète (hérédité par mélange, population et fréquences, loi de Hardy-Weinberg, conditions, causes d'écart) et l'ouverture de la partie II avec l'activité 1 en panneau repliable ; l'activité n'est pas à rendre, d'où des résultats attendus donnés comme proposition (aucune correction de la prof). **En attente** : diapositives 17 à 48 (corrections des scénarios, études de cas drosophiles de Buri, Amish et Huttérites, groupes sanguins, Culex pipiens ; bilan « évolution de la notion d'espèce » avec Doolittle et Denisova) ; VOCAB `"3"`, QCM et REDAC `t3` à compléter avec la suite. La syncytine a été mise à jour avec la correction de Mme Philip (syncytine 1 / MSRV 87 %, syncytine 2 / MSRV 20 %, arbre, conclusion) ; le TP globines du chapitre 1 avec sa correction (modèle de tableau, arbre, conclusion en quatre arguments, schéma « à recopier » en `SCHEMAS.globines`). Les grilles de notation ECE de la prof (communication : techniquement correcte, bien renseignée, pertinente ; conclusion : complète, organisée, distanciée) sont dans le panneau du TP syncytine. Points signalés dans le site : la correction globines place la myoglobine sur le chromosome 20 (les bases de données disent 22) ; la fiche ECE présente Nostoc et Chlorobium comme des plantes vertes (ce sont des bactéries). **Animations (`svt/anim/`, depuis le 09/10/2026)** : vraies animations temporelles sur le modèle de l'artefact méiose de référence (lecteur avec barre de lecture et repères d'étapes, légendes pointées, son, mode pause par étape, quiz). Un moteur commun `svt/anim/moteur.js` + `moteur.css` (appel `ANIM.lancer({END, SCENES, CALL, CUES, QUIZ, draw, bascule})`) et une page par animation, générée depuis un gabarit commun. Dans le cours, `<div data-anim="nom"></div>` monte une iframe `anim/nom.html?embed=1&theme=…` (hauteur transmise par `postMessage`, thème synchronisé) et un lien plein écran. **Depuis le 09/10/2026, tous les schémas du site sont des animations** (17 pages) : Première `mitose` (p1 et t1u1), `replication`, `expression`, `enzyme`, `globe`, `tectonique`, `ecosysteme`, `immunite`, `anticorps` ; Terminale `clonal`, `meiose` (port de l'artefact de référence, monté deux fois dans t1u2 avec `data-t0="36"` et `data-t0="22"` pour démarrer à la métaphase I ou au crossing-over), `nondisj`, `coinegal`, `globines`, `thg`, `insuline`, `endosymbiose`. L'objet `SCHEMAS` est vide (le mécanisme `data-schema` reste disponible) ; la table `ANIMS` d'index.html donne les titres. Les sources (`<nom>.js` + `meta/<nom>.json`) et le générateur de pages ne sont pas dans le dépôt : les pages `anim/<nom>.html` font foi. **Téléphone** : l'animation est intégrée bord à bord, sans cadre (iframe à fond transparent, `color-scheme` réglé par le cours), commandes sous l'image, quiz ouvert sous le lecteur dans la page (message `anim-goto`), pas de lien vers une page à part. Moteur : `?t0=` (instant de départ). Piège : le filtre `#glow` ne couvre que x de −50 à 450 en coordonnées du monde ; une animation qui panoramique dessine ce qui sort de ce cadre dans la couche `fx`. Le `sw.js` précache ces pages et les met en cache sous leur propre adresse (une iframe est une navigation : ne jamais la ranger sous la clé de la page d'accueil). Si `moteur.*` change, incrémenter `?v=N` dans les pages et dans `sw.js` (actuellement `v=5`, cache `svt-v23`). Commandes du lecteur : « précédent » / « suivant » respectent la pause (la lecture ne reprend que si elle était en cours, ou au tout premier appui) ; une seule boucle d'animation à la fois ; sur téléphone, les commandes sont juste sous l'image, en page plein écran comme dans le cours. Recherche : depuis le 09/10/2026, une **fenêtre plein écran à fond flouté** comme sur DNL (`#srch`, champ `#sq`), ouverte par le champ de l'en-tête (devenu un bouton `#q`), le bouton du bas, Ctrl+K ou « / » ; les résultats s'affichent dans la fenêtre (`trouver`, `resHTML`), la page derrière ne bouge pas pendant la frappe, et le bouton retour du téléphone ferme la fenêtre (entrée d'historique `{srch:1}`). Ne jamais re-rendre la page ni naviguer par `location.hash` pendant la frappe : sur Android avec Gboard, les lettres s'écrivaient à l'envers (bug signalé le 09/10/2026). La route `#recherche` existe encore pour les anciens liens. VOCAB accepte un champ `nomListe` quand la prof n'a pas distribué de liste (chapitre 2 : « Les définitions des diapositives de Mme Philip »). Orhan se dit très faible en géologie : ces chapitres doivent être particulièrement solides.

### DNL Histoire-Géo (`dnl/`)

React 18.2 en UMD chargé depuis cdnjs. Données dans un objet `CHAPTERS = { H1…H10, G1…G10 }`, une structure `STRUCTURE` (histoire / géographie → thèmes → chapitres) aplatie en `FLAT`, un glossaire bilingue, un index de recherche, un mode fiches, une bascule FR/EN, et des composants de cartes (`G1Map_…`, `G2ArcticMap`, etc.).

- Le **glossaire interactif** est le même mécanisme que celui de SVT.
- L'**index de recherche et le glossaire sont générés à partir du contenu des chapitres** : ils se remplissent chapitre par chapitre.
- Identité visuelle « Atlas de révision » : feuille de surcharge `atlas-skin` appliquée après le CSS d'origine, 28 icônes SVG originales (registre `ICON_PATHS`), Cormorant Garamond + Inter, bleu de Prusse / parchemin / doré. **Tout nouveau contenu DNL respecte cette identité.**
- Les 48 cartes SVG viennent de Natural Earth et ont été simplifiées (Douglas-Peucker, tolérance 0,4 px, uniquement les chemins purement M/L/Z, **courbes et flèches laissées intactes**). Résultat : 15,5 Mo → 4,4 Mo. Toute nouvelle carte doit être simplifiée à la génération, vérifiée par comparaison pixel à pixel avant/après (alerte au-delà de 3 % de différence perceptuelle).
- **Décision** : ne **pas** scinder DNL en Histoire et Géographie. Cela casserait le tirage croisé de l'oral, le glossaire partagé et la recherche. Cible : environ 3 cartes par chapitre.

Programme réel de M. Aurélien Ros (Histoire) : T1 « The fragilisation of democracy, totalitarianism and WWII (1929-1945) » ; T2 « The multiplication of actors in a bi-polar world (1945-1971) » ; T3 « Economic, political and social challenges from 1970 to 1991 » ; T4 « The world and Europe since the 1990s » (sujet d'oral). Géographie, 4 thèmes : espaces maritimes ; dynamiques territoriales (focus Grande-Bretagne) ; place de l'UE dans la mondialisation ; projet conclusif (focus France).

Épreuves : **oral coeff. 10**, 35 min (20 min de préparation + 15 min : 5 min d'exposé sur un Key Issue, 5 min de questions, 5 min de discussion sur un Key Term) ; le Key Issue et le Key Term sont tirés en croisant histoire et géographie. **Écrit coeff. 10**, 4 h, sujet A (dissertation d'histoire + étude de documents de géographie) ou sujet B (l'inverse).

Structure imposée par Cengiz pour la question a) du DBQ : jugement dès la première ligne (largely / significantly / partly / slightly useful), document présenté en une phrase, paragraphe d'atouts à plusieurs arguments, paragraphe de limites à plusieurs arguments.

État : H1 (« The Wall Street Crash and its Impact ») réécrit en entier à partir du diaporama de M. Ros ; H2 (régimes totalitaires) complet (parties I à III, version Claude.ai du 05/10/2026, partie II corrigée et complétée le même jour d'après les notes d'Orhan et les Worksheets 3 et 4) ; H3 (« World War Two ») avancé jusqu'à la fin de la partie II (introduction ; I.1 le cas français ; I.2 « The British resistance supported by the US » : stratégie de Jodl, Blitz, Worksheet 2 Churchill et de Gaulle, soutien américain, Pearl Harbor ; II.1 « German plans for Eastern Europe » : pacte germano-soviétique et annexions soviétiques de 1940, trois raisons de l'invasion ; II.2 « Operation Barbarossa: a war of annihilation (case study #2) » : trois poussées et alliés de l'Allemagne, purges et terre brûlée, discours de Staline du 7 novembre 1941, guerre d'anéantissement, Stalingrad, rapport de forces de novembre 1942 (schéma `h3forces`), Worksheet 3 Stalingrad ; cours du 12/10/2026 en distanciel, puis diaporama complet du chapitre, 43 diapositives, dont les cartes de l'Europe 1939-41 et de la France occupée) ; partie III (politique raciale, génocide) en attente ; les autres chapitres sont des placeholders. Onglet **Entraînement** (bouton de la barre latérale et de l'accueil, composant `TrainingPage`, ajouté le 06/10/2026) : volet Quiz livré (réunit `H1_QCM`, `H2_QCM`, `H3_QCM` sans les recopier + `TRAIN_QCM` : vue d'ensemble, liens entre chapitres, réflexes d'épreuve BFI, questions hors cours sourcées, rappels de Première ; chronologie générée depuis les frises) ; volets Essais et DBQ à venir (format officiel : essai « Explain » + « Assess / How far », DBQ a) « How useful » + b) ; les images des DBQ pourront être chargées en ligne, exception à la règle hors connexion décidée par Cengiz). **Fiches PDF imprimables** (ajoutées le 11/10/2026) : `dnl/fiches/H1-fr.pdf`, `H1-en.pdf`, etc., ouvertes depuis le bouton « Fiche PDF » de l'en-tête de chaque chapitre et l'onglet « Fiches PDF » de l'Entraînement (liste `FICHES_PDF`). Elles sont **générées** par `outils/fiches-dnl/` : `generer.js` lit le cours dans `dnl/index.html`, `fiches.js` porte la frise de dix dates, la légende de la carte et le schéma de synthèse de chaque chapitre, `cartes.py` produit les cartes SVG (frontières de 1930 d'aourednik/historical-basemaps, départements de gregoiredavid/france-geojson, ligne de démarcation du Département de l'Ain sur data.gouv.fr) ; `europe.py` produit les cartes d'évolution de l'Europe (changements datés de CShapes 2.0, Sarre, Bohême-Moravie et partage de la Pologne d'après Natural Earth, signalés comme approximatifs). Chaque fiche porte une grande carte légendée suivie d'une série de petites cartes datées « étape par étape » (décision de Cengiz, 13/10/2026) : H1 le monde en 1929, 1931, 1933 et 1935-37 ; H2 l'Europe en 1933, 1936, fin 1938 et septembre 1939 ; H3 l'Europe en octobre 1939, juillet 1940, mai 1941 et novembre 1942 (lignes de front simplifiées de décembre 1941 et novembre 1942, flèches de Barbarossa), plus un zoom sur la France découpée. Les éléments de carte qui ne sont pas dans le cours sont marqués « hors cours » dans la légende. **Après toute modification d'un chapitre, relancer `node outils/fiches-dnl/generer.js`** (Playwright) ; pour un nouveau chapitre, ajouter son entrée dans `fiches.js`, sa carte dans `cartes.py` et son code dans `FICHES_PDF`. Le `sw.js` sert les PDF réseau d'abord. **Renvoi vers le paragraphe** (13/10/2026) : une fois la question répondue, le QCM du chapitre et l'Entraînement affichent un lien « Revoir le paragraphe » qui ouvre le chapitre, déplie la partie, fait défiler jusqu'à l'idée et la surligne (`goIdea`, événement `goto-idea`, ancres `idee-<chapitre>-<partie>-<idée>` posées par `Idea`). Table `QCM_REFS` : empreinte de l'énoncé anglais (`qcmHash`) → `chapitre|partie|idée` ou `chapitre|ov` (synthèse → onglet L'essentiel) ; 221 questions sur 231 ont un renvoi (les 10 autres : méthode de l'épreuve, ou fait absent du cours). Les questions hors cours affichent « Le cours en parle ici ». **Toute nouvelle question de QCM doit recevoir son entrée dans `QCM_REFS`** ; toute réorganisation des parties ou des idées d'un chapitre décale les indices et oblige à refaire la table. Un script d'audit (`audit_idee_exemple.py`) vérifiait l'ancrage date/chiffre/nom propre de chaque exemple dans les deux langues : **il n'est pas dans le dépôt**.

### Philosophie (`philo/`)

React 18.2 UMD précompilé inline. Constantes : `NOTIONS` (17 notions du programme), `COURANTS`, `AUTEURS`, plus les repères et plus de 220 citations (champs `breve` et `approf`), un badge « ≈ paraphrase » sur les citations non littérales, une galerie de textes, un onglet « Mon prof ».

M. Thomas Bellon ne traite **pas** les notions une par une : il fait des chapitres par problème qui croisent plusieurs notions (chapitre 1 « la liberté » en quatre parties : métaphysique, morale, politique, peut-être esthétique). La couche « cours » prévue au-dessus de l'index par notion stocke des **distinctions** (couples de termes), chacune avec les deux termes, le contenu du cours, l'exemple de Bellon, le repère, l'auteur et une phrase de transition réutilisable en dissertation.

État : la couche « Le cours de M. Bellon » est publiée depuis le 05/10/2026 (`philo-v2`) : chapitre I « La liberté », partie 1 (liberté métaphysique) rédigée, parties 2 à 4 en attente ; page « L'explication de texte » sur le texte de Kant.

**Guide de l'explication de texte** (18/10/2026, route `m-expl`, cache `philo-v7`) : rangé dans la section « Cours » du menu, sous « Méthode » (il n'est plus sous « Le cours de M. Bellon », pour éviter le doublon signalé par Cengiz) ; l'onglet « L'explication » de la page Méthode ne fait plus que renvoyer au guide. La page est devenue un guide complet en neuf onglets — L'épreuve, Le brouillon, L'introduction, Le développement, La conclusion, Corrigés expliqués, Les erreurs, Les astuces, S'entraîner. Données dans `GUIDE_EXPL` (à côté de `METHO_EXPL`, qui garde les quatre cases de M. Bellon : onglet « L'introduction », badge « Méthode de M. Bellon »), composants `Gx*`, styles `gx-*`. Cengiz avait annoncé la méthode écrite de M. Bellon, mais elle n'est pas arrivée ; sur sa consigne, tout le reste suit la **note de service du 11/09/2026** (BO spécial n° 4 du 17/09/2026, NOR MENE2622661N, bac général à partir de la session 2027) et sa grille de notation propre à l'explication (paliers 0-5 à 16+ ; une copie défaillante sur la langue ne peut pas avoir la moyenne), les consignes de correction officielles 2024 (pluralisme : ni partie critique séparée ni schéma thème / thèse / problème / enjeux exigés) et les méthodes des sites de préparation. Méthode « simple » demandée par Cengiz, sur le modèle de son tableau citation / procédé / effet du français : le tableau **citation · geste · sens · effet**, un tableau par mouvement ; rédaction du paragraphe en cinq temps (situer, citer, expliquer, interroger, relier). **Neuf corrigés complets**, un par texte de la galerie `TEXTES`, chacun avec brouillon (six cases, tableau), copie rédigée (≈ 1 750-1 900 mots) et commentaire en marge, classés par difficulté et dotés d'un champ `lecon` (« Ce que ce texte t'apprend » : le type de texte et son geste de méthode) : Facile — Épictète (`manuel`, une distinction), Épicure (`epicure`, raisonnement déductif), Rousseau (`rousseau`, texte court et polémique), Mill (`mill`, raisonnement par alternative) ; Moyen — Platon (`platon`, allégorie), Descartes (`descartes`, récit à la première personne), Kant Lumières (`kant-lumieres`, définition) ; Difficile — Kant le gibet (`kant`, texte du cours, `cours:true`, exemples et expériences de pensée), Hegel (`hegel`, texte abstrait). Les deux premiers sont dans `GUIDE_EXPL.corriges` ; les sept autres (rédigés le 18/10/2026 par des sous-agents sur un cahier des charges commun, relus, citations vérifiées mot pour mot contre le texte du site par script) dans `GX_CORR_PLUS` ; l'ordre d'affichage est fixé juste après. Connaissances hors texte paraphrasées et signalées « hors texte » dans les commentaires. Pour un nouveau corrigé : même structure (`id`, `tid` = id du texte dans `TEXTES`, `nom`, `titre`, `niveau` Facile/Moyen/Difficile, `lecon`, `cases`, `tableau` suivant les `mouvements` du texte, `copie`, `pieges`), l'ajouter à `GX_CORR_PLUS` et à la liste d'ordre. **À reprendre quand la méthode de M. Bellon arrivera** : confronter, remplacer ce qui diffère, retirer les encadrés « À vérifier » tranchés (minutage, longueur, partie critique séparée ou non). Correctif de `philo/motion.js` (`?v=2`) : sous « réduire les animations », la pastille de la barre latérale s'affichait par-dessus l'entrée active et en masquait le libellé ; elle reste désormais cachée dans ce cas. `cdm/motion.js` porte le même code (non corrigé).

### Physique-Chimie (`pc/`)

JS natif, 21 chapitres, thème orange sur sombre. Chapitres 1 à 4 ouverts (le 3, méthodes chimiques d'analyse / titrage, ajouté le 02/10/2026 ; le 4, « La lumière, un flux de photons », ajouté le 13/10/2026, rangé dans le thème 2 « Ondes et signaux ») ; le reste est en placeholder. **Numérotation** (décision de Cengiz, 13/10/2026) : les cours étant en distanciel, le professeur ne suit plus l'ordre prévu (il privilégie les chapitres aux TP simples) ; les chapitres à venir de l'accueil n'ont donc **plus de numéro** — seul un chapitre ouvert reçoit le numéro que lui donne le professeur. Chapitre 4 : plan de travail et TP 6 (rendement d'une cellule photovoltaïque, données du tableur du professeur, pas de réponses d'Orhan) ; manuel : **édition en ligne Lelivrescolaire**, la seule qu'utilise Orhan (pas de livre papier) — chapitre 20 « Effet photoélectrique et enjeux énergétiques », cours p. 535-536, bilan p. 537, QCM p. 538, exercices p. 539 à 544 (les p. 405 / 412 / 420 citées par le plan de travail ne correspondent à rien, ne pas en tenir compte) ; simulateur de l'effet photoélectrique ; trois schémas animés (scènes du tableau `SCENES`) et trois animations explicatives. **Animations explicatives (`pc/anim/`, depuis le 13/10/2026)** : demande de Cengiz, des animations « au service de la compréhension », où l'on voit le phénomène se produire. Même moteur que SVT : `pc/anim/moteur.js` est une copie de `svt/anim/moteur.js` (seul le commentaire de tête change), `moteur.css` en reprend la feuille aux couleurs du site PC ; une page par animation (`ANIM.lancer({END, SCENES, CALL, CUES, QUIZ, draw})`), montée dans le cours par `<div data-anim="nom"></div>` (table `ANIMS` dans le script de montage de `index.html`, hauteur par `postMessage`, thème `sombre` → `dark` synchronisé, pause quand le panneau se referme). Animations du chapitre 4 (7 étapes, 74 s, quiz de 4 questions chacune) : `photon` (fiche 2 : photon de 11,0 eV non absorbé, 10,2 eV absorbé — énergie « empilée » sur le niveau de départ —, désexcitation, cascade 3 → 2 → 1 et raie rouge à 656 nm, spectres d'émission et d'absorption, ionisation à 15,0 eV) ; `photoelec` (fiche 3 : plaque de zinc, rouge intense sans effet, prévision ondulatoire démentie, UV faible puis intense puis plus énergétique, bilan pour un électron face à Φ, graphique Ec = f(ν) construit point par point) ; `cellule` (fiche 6 : couches n et p, formation du champ interne, paire électron-trou séparée, tour du circuit et ampoule, courant proportionnel à l'éclairement, photon infrarouge sans effet et photon bleu qui chauffe, bilan du rendement). Les pages `photoelec` et `cellule` ont été produites à partir de la coquille de `photon.html` (en-tête, légende, note, script) ; les scripts sources ne sont pas dans le dépôt, les pages font foi. **Correctif du 13/10/2026 sur les deux moteurs (SVT et PC)** : au premier appui sur lecture, le temps pouvait partir en négatif sur téléphone (« −22 s ») parce que l'horodatage de `requestAnimationFrame` précédait l'instant du clic ; `loop()` mesure désormais `performance.now()` et borne le pas à [0 ; 0,1 s]. Le même défaut faisait repartir l'animation au début de l'étape précédente quand on reprenait après une pause (le temps reculait de la durée de la pause). Versions : SVT `moteur.*?v=5`, cache `svt-v23` ; PC `moteur.*?v=3`, cache `pc-v32`. Les `sw.js` de SVT et PC redemandent les pages avec `cache: "no-cache"`, comme DNL, pour qu'une correction arrive sans attendre les 10 minutes de cache de GitHub Pages. **Plein écran sur place** (13/10/2026, demande de Cengiz, PC et SVT) : le bouton « Plein écran » sous chaque animation ne charge plus la page `anim/<nom>.html` ; la figure passe en `position:fixed` et s'agrandit depuis sa place (animation des dimensions, voile flouté), l'iframe n'est jamais déplacée dans la page, donc l'animation continue là où elle en était ; « ✕ Revenir au cours », Échap (relayée par le moteur, message `anim-echap`) ou le bouton retour du téléphone (entrée d'historique `{animPlein:1}`) la font revenir à sa place dans la fiche. Le moteur reçoit `anim-plein` et limite la hauteur de l'image à l'écran (`html.embed.plein`). Les pages autonomes de PC renvoient à `../#anim-<nom>`, qui rouvre le chapitre, la fiche et l'animation (avant : retour à l'accueil). Le `sw.js` précache `anim/*` et range chaque page d'animation sous sa propre adresse (corrigé le 13/10/2026 : toute navigation, iframe comprise, écrasait la clé de la page d'accueil). Nouvelle animation : l'ajouter à `ANIMS` dans `index.html` et dans `sw.js`, incrémenter le cache. Onglet final : **« Fiche mémo »** complète, comme aux chapitres 1 à 3 (exception PC à la règle des fiches mémo). L'impression ne visait que `#page-ch1` : corrigé le 13/10/2026 (`.page.on`), les fiches des chapitres 2 à 4 s'impriment. Pour chaque chapitre : plan de travail du professeur, **plus** d'autres exercices du manuel (Le Livre Scolaire) et des exercices type bac créés par Claude **signalés comme tels**, dont des exercices bilan couvrant toutes les notions exigibles. Le chapitre 1 reste à reprendre sur ce modèle. Visuels de labo complexes : prompts pour Nano Banana (anglais, fond blanc, style vectoriel plat de manuel, annotations en français, flèches `#E45C10`).

### ACL écrit (`acl-ecrit/`, `acl-lughnasa/`, `acl-bricklane/`)

Bilingue FR/EN. Le hub porte l'épreuve, la méthode du commentaire et de l'essay, l'**Atelier** (réécritures annotées des copies d'Orhan, répertoire de 45 exercices ciblant le saut KP14→KP20), la boîte à outils critique et le programme (dont *Twelfth Night*, couverture non documentée).

- **Lughnasa** : déroulé séquence par séquence avec pages du PDF, personnages, sept enjeux, banque de 21 citations avec micro-citations, et un outillage d'attaque pour l'essay (construction de la pièce, trois scènes à connaître, motifs paginés, 12 sujets classés dont 5 plans complets, 7 paires de citations contradictoires, 8 pièges). Les notes de cours du professeur restent à intégrer.
- **Brick Lane** : chapitres 1 à 10 complets, scène par scène, avec panneau « vocabulaire pour l'analyse » ; banque de 48 citations en mode révision (localisateur d'abord → l'élève écrit → réponse). Même outillage d'attaque prévu une fois les chapitres 11 à 21 rédigés.

Barème BFI (/20, paliers « Key Points ») : KP20 remarquable, KP17 très bon, KP14 satisfaisant, KP11 passable (une bonne dissertation qui ne répond pas à la question plafonne ici), KP8 élémentaire, KP5 très faible (réponse bâclée, en notes). Défaut d'Orhan à corriger : il soumet des citations à l'analyse de l'IA puis recopie les conclusions sans le cheminement. Le mode révision/rappel est le correctif structurel.

### ACL oral (`acl-oral/`, `acl-oral-1984/`, `acl-oral-butler/`)

Le hub porte les onglets de cadrage, l'onglet de thèses transversales, le diagramme SVG « Ponts entre œuvres » et les six poèmes : trois analysés (*Darkness* de Byron, *Eve to Her Daughters* de Wright, *Morning in the Burned House* d'Atwood), trois différés (*The Hollow Men*, *The Second Coming*, *The Unknown Citizen*).

- **1984** : huit parties, un onglet chacune ; peu de citations (6).
- **Butler** : chapitres 1 à 13 complets, scène par scène, bilingues, citations vérifiées contre le texte (ch. 1-6 : 110 scènes, 25 citations ; ch. 7-9 : 54 scènes, 12 citations ; ch. 10-13 ajoutés ensuite), modes détaillé / express. **Ne rien écrire au-delà du chapitre 13** tant que Cengiz n'a pas confirmé que la classe y est.

### Italien, Red Pen, CDM

- **Italien** : 3 onglets (Grammatica, Coniugazione, Lessico e funzioni), 33 chapitres A2→B2, cours en français, exemples en italien, encadrés « ⚠️ Da evitare » et « ✅ Punti chiave ».
- **Red Pen** : grammaire anglaise C1 et méthodologie de l'essay, thème « Night Study » bleu nuit et laiton avec variante jour.
- **CDM** : dossier de recherche (problématique, lectures, cas australien, partenaires, terrain, position). Oral coeff. 20 : 10 min de présentation + 10 min d'entretien. Problématique d'origine : « À l'ère du numérique, qu'est-ce qui change vraiment les comportements de santé des adolescents : la sensibilisation ou la régulation ? » ; elle a été resserrée sur le cas australien (interdiction des réseaux sociaux avant 16 ans), le Royaume-Uni servant de comparaison. **Reformulation à faire valider par le professeur avant de toucher au site et au PDF.**

### Médecine (`medecine/`, depuis le 10/10/2026)

« Protocole Santé ». But : la **licence portail santé** (première année unique qui remplace PASS et LAS à la rentrée 2027 ; textes adoptés au CNESER en juillet 2026, pas encore au Journal officiel, coefficients inconnus). Avant la médecine « pure et dure », le site teste **cinq méthodes de travail, une à la fois** (règle de Cengiz : une méthode terminée avant la suivante) : M1 relire (témoin, placé en premier exprès), M2 feuille blanche, M3 Feynman, M4 tester d'abord + séries mélangées, M5 méthode des J (cartes, boîtes de Leitner). Chaque méthode voit les **trois mêmes matières** (biologie cellulaire, biochimie, anatomie et physiologie) sur des chapitres différents (`PLAN`), pour mesurer la méthode et non l'aisance dans une matière. Calendrier identique pour toutes (`SEANCES`) : J0 mercredi, J2, J3 (apprentissage, 60 min), J4, J7, J9, J11 (consolidation, 40 min), QCM de clôture à J14, rappel tardif à J28 (questions différentes). QCM de type concours (5 propositions, barème à discordances 1 / 0,5 / 0,2 / 0), avec indice de confiance. Résultats : score J14, score J28, points par heure, fiabilité du « sûr », ressenti. Persistance : journal JSON téléchargé puis réimporté (pas de `localStorage`). Contenu : rédigé par Claude, niveau début de première année, vérifié sur ouvrages de référence et signalé comme tel. État (10/10/2026) : les **15 fiches et les 5 blocs de QCM sont en ligne** (27 QCM par méthode). Périmètre calé sur les programmes de PASS publiés (ex. Montpellier : UE1 Chimie-Biochimie, UE3 Cellules et Tissus, physiologie humaine générale) ; contenu original, aucun cours de faculté reproduit. Outils par méthode : séance guidée étape par étape avec minuteur (toutes) ; M3 `OUTILS` (3 notions + 6 questions « pourquoi ? » par chapitre, enregistreur audio non conservé) ; M4 `ENTRAIN` (6 questions de pré-test + 10 de série par chapitre, distinctes des QCM de mesure ; série mélangée de 15) ; M5 `CARTES` (25 cartes par chapitre, boîtes de Leitner dans le journal, J4/J11 toutes les boîtes, J7/J9 boîtes 1-2). Les fiches de M3 à M5, puis l'enrichissement de M1-M2, ont été rédigés par des sous-agents sur un cahier des charges commun, puis relus. **Équilibre exigé par le protocole** : toutes les fiches font 16 à 18 min de lecture (≈ 2 700 à 3 100 mots, mesure du site : mots / 170) et chaque QCM échantillonne toute sa fiche ; toute modification d'une fiche doit garder cet équilibre entre méthodes. **Décision de Cengiz (10/10/2026) : les cours sont considérés comme déjà fichés (fiches complètes) ; aucune méthode ne demande de refaire une fiche.** Conséquences : pour M5, les cartes sont fournies par le site (avec suivi des boîtes de Leitner dans le journal) ; pour M4, prévoir des banques d'entraînement distinctes des QCM de mesure ; pour M3, des questions « pourquoi ? » par chapitre.

---

## 5. Couche de mouvement

Sur les sites animés, le mouvement est maintenu **à part du contenu** dans `motion.css` et `motion.js`, chargés par un bloc repéré juste avant `</head>` :

```html
<!-- mouvement:debut — couche maintenue à part (motion.css, motion.js) ; à conserver lors des mises à jour -->
<link rel="stylesheet" href="motion.css?v=N">
<script src="motion.js?v=N" defer></script>
<!-- mouvement:fin -->
```

- Quand un `index.html` régénéré remplace l'ancien, **réinsérer ce bloc** s'il a disparu.
- Quand `motion.css` ou `motion.js` change, **incrémenter `?v=N`** et le numéro de cache du `sw.js` (les service workers servent ces fichiers cache d'abord).
- Tout ce qui bouge est rangé sous `html.mo`, classe posée seulement si l'appareil n'a pas demandé de réduire les animations. **Rien n'est jamais caché en attendant une animation.**
- SVT et PC ont deux couches : une première écrite directement dans `index.html`, qui expose des outils sur `window.MO`, et un complément dans `motion.css` / `motion.js` qui réutilise ces outils sans rien réécrire.
- **DNL** : depuis la version Claude.ai du 05/10/2026, le mouvement est écrit **dans `index.html`** (`<style id="motion-skin">` et un script « ATLAS — couche de mouvement » qui expose `window.MO`, appelé par le quiz et les flashcards). Les fichiers `dnl/motion.css` et `dnl/motion.js` d'une couche antérieure ne sont plus chargés : **ne pas réinsérer leur bloc**, les deux couches se marcheraient dessus (`window.MO`, `html.mo`).
- Les trois sites ACL écrit (`acl-ecrit`, `acl-bricklane`, `acl-lughnasa`) partagent les mêmes `motion.css` et `motion.js` : seule la ligne `var MOTIF = …` du script change d'un site à l'autre. De même pour les trois sites ACL oral (`acl-oral`, `acl-oral-1984`, `acl-oral-butler`).

Orientation décidée par Cengiz (29/09/2026) : les **animations explicatives détaillées** de SVT et de physique-chimie (50 à 100 visées) iront dans un **site à part** dédié aux animations ; pour DNL, philo, ACL, etc., seules de petites animations motivantes sont intégrées au site. Style voulu : des schémas qui **se déroulent** (chromosomes qui se rapprochent, se superposent, se séparent), légendes qui apparaissent au fil de l'animation, rendu doux et organique. Cengiz juge que des schémas qui se contentent de se dessiner « ne servent à rien » : il veut voir le phénomène se produire. L'animation méiose / crossing-over du 29/09 a été jugée « parfaite » et sert de référence.

## 5 bis. Bouton « Demander à ChatGPT » (tous les sites de révision)

Décision de Cengiz (11/10/2026) : pas d'IA hébergée par le projet (une IA gratuite hébergée a été essayée puis abandonnée, trop imprécise sur des questions pointues) ; à la place, un bouton qui ouvre **ChatGPT en discussion temporaire** avec la question d'Orhan. Conditions posées : gratuit, **aucun historique conservé**, pas de contenu de cours envoyé.

- Étendu le 11/10/2026 à **14 sites** : svt, pc, dnl, philo, acl-ecrit, acl-lughnasa, acl-bricklane, acl-oral, acl-oral-1984, acl-oral-butler, italien, redpen, cdm, medecine (pas `fenuareo/`, projet distinct). Chaque `assistant.js` est le même fichier ; seul le bloc `CONFIG` change : `NOM`, `LANGUE` ("fr" ou "en" : DNL en anglais, les autres en français), `COTE` ("gauche", ou "droite" pour la philo), `CONSIGNE` propre au site (en anglais pour la DNL, les ACL et Red Pen, avec « réponds dans la langue de ma question » ; ACL et philo : ne jamais inventer de citation ; CDM : ne jamais inventer de source ni de chiffre), `COULEURS` (variables CSS du site, donc thèmes et mode sombre suivis), `EVITER` (`nav.bottom` en SVT, `nav.bas` en médecine). Chargé par un bloc repéré `<!-- assistant:debut -->` … `<!-- assistant:fin -->` (après `<!-- mouvement:fin -->`, ou avant `</head>` en médecine) : **à réinsérer** si un `index.html` régénéré le perd. Le générateur qui a produit les 14 fichiers n'est pas dans le dépôt : pour modifier le corps commun, éditer un fichier puis recopier tout ce qui suit `fin CONFIG` dans les 13 autres, incrémenter `?v=N` (actuellement 9) et le cache de chaque `sw.js`.
- Points de vigilance signalés à Cengiz : ACL (Orhan a tendance à faire analyser ses citations par l'IA et à recopier les conclusions), CDM (dossier noté), médecine (le bouton est une variable non contrôlée du protocole des cinq méthodes).
- Bouton rond en bas à gauche (à droite : retour en haut sur PC, son sur DNL ; sur SVT il remonte au-dessus de la barre de navigation du téléphone). Le panneau ouvre `https://chatgpt.com/?temporary-chat=true&q=<consigne + question>` dans un nouvel onglet (ou dans la même fenêtre si l'onglet est bloqué). Un choix ChatGPT / Perplexity a été essayé puis retiré (11/10/2026) : Perplexity exige un compte et aucun lien ne l'ouvre en mode Incognito ; condition de Cengiz : discussion sans historique, déjà connectée.
- Rien n'est gardé côté site : pas de stockage, champ vidé après ouverture. Côté ChatGPT, `temporary-chat=true` ouvre une discussion temporaire, hors historique. Ce paramètre n'est pas documenté officiellement : s'il cesse de fonctionner, la discussion apparaîtrait dans l'historique de ChatGPT (à vérifier de temps en temps : la page doit afficher « Discussion temporaire »). Le navigateur garde l'adresse ouverte dans son propre historique.
- **Mouvement** (11/10/2026, demande de Cengiz) : écrit dans `assistant.js` même, sous `html.mo` et `prefers-reduced-motion: no-preference` ; la fonction `mouvement()` décide des délais en JS (fermeture animée, envol). Bouton : arrivée en rebond, halo qui respire, point d'interrogation qui hoche ; panneau : voile flouté, montée avec rebond (gonflement depuis le coin sur ordinateur), éléments en cascade, sortie animée ; reflet sur le bouton d'envoi quand une question est prête ; envol de la flèche à l'ouverture de l'IA ; secousse du champ vide. Sans mouvement, tout est instantané.
- Âge : ChatGPT accepte les 13-17 ans avec l'accord d'un parent (Cengiz). **Claude.ai n'est pas proposé** : ses conditions exigent 18 ans (Cengiz l'avait demandé ; à ajouter seulement si les conditions changent ou pour un usage adulte).

---

## 6. PWA et service workers

- Chaque site a un `manifest.json` (`display: standalone`, `start_url: "./"`, `scope: "./"`, icônes 192 et 512 en `any maskable`) et un `sw.js`.
- Stratégie : **réseau d'abord pour la page** (une nouvelle version est visible dès le prochain lancement, sans vider le cache), **cache d'abord pour les assets**. Sur DNL (12/10/2026), la page et les PDF sont redemandés avec `fetch(url, { cache: "no-cache" })` : sans cela, le service worker reprenait la copie que le navigateur garde 10 minutes (GitHub Pages envoie `max-age=600`), et une mise à jour du cours n'apparaissait pas tout de suite sur le téléphone.
- Chaque `sw.js` porte un nom de cache versionné en tête de fichier (`svt-v5`, `dnl-v33-h3-ii2`, `philo-v3`, `redpen-v2`, `cdm-v2`, `fenuareo-v2`, etc.). **Incrémenter ce nom à chaque livraison qui ajoute ou modifie un fichier annexe.**
- Le dépôt étant public, ne rien y mettre qu'on ne veuille pas voir en ligne.

---

## 7. Écarts connus et points à décider

1. **DNL charge React depuis cdnjs et des polices Google** : cela contredit la règle « aucune dépendance externe, fonctionne hors ligne », et le service worker ne précache pas ces ressources. Soit on les inline (React coûte de l'ordre de 140 Ko), soit on assume l'écart. À arbitrer avec Cengiz.
2. **Livré mais pas publié, d'après la mémoire de projet** (à vérifier dans le dépôt avant de refaire) :
   - (réglé le 09/10/2026) L'animation méiose / crossing-over de référence est publiée dans `svt/anim/meiose.html`.
3. **Le pipeline DNL d'origine n'est pas dans le dépôt.** Il vivait dans un conteneur éphémère (`compiled.js`, `shell_before.html`, `shell_after.html`, un dossier `geo/` avec les scripts de cartes, l'injecteur d'enrichissement, le script d'audit). Dans le dépôt, **`dnl/index.html` est la seule source** : l'éditer par injections ancrées. Si Cengiz a conservé les anciens scripts de cartes, les rapatrier.
4. **`test.html`** à la racine est un reliquat.
5. **Poids** : DNL (5,3 Mo) et Philo (2,2 Mo) sont les deux sites à surveiller. Pistes déjà évoquées : scinder SVT en `svt/` (Terminale) et `svt-premiere/` (rappels) s'il dépasse environ 2 Mo ; **ne pas** scinder DNL.

---

## 8. Procédure de modification

1. Lire la section du site concerné ci-dessus et le code réel.
2. Modifier par injection ancrée (assertion de l'unicité de l'ancre).
3. **Valider le JS** : extraire chaque `<script>` inline et le passer à `node --check` :

   ```bash
   python3 - <<'EOF'
   import re, subprocess, sys, tempfile
   html = open(sys.argv[1] if len(sys.argv) > 1 else "index.html", encoding="utf-8").read()
   ok = True
   for i, m in enumerate(re.finditer(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S)):
       with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
           f.write(m.group(1))
       r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
       print(f"script {i}: {'OK' if r.returncode == 0 else 'ERREUR'}")
       if r.returncode: print(r.stderr[:400]); ok = False
   sys.exit(0 if ok else 1)
   EOF
   ```
   (Attention : les blocs `type="text/babel"` ou JSON ne se valident pas ainsi.)
4. Pour un visuel SVG ou un changement d'interface : rendu et capture (Playwright ou `cairosvg`) avant publication. Sur de gros fichiers, `sys.setrecursionlimit` est nécessaire.
5. Incrémenter le cache du `sw.js` et les `?v=N` si des fichiers annexes ont changé.
6. Contrôler qu'aucun identifiant, jeton ou commentaire inutile ne traîne dans les fichiers.
7. Commit et push **depuis la session Claude Code Cloud avec `Revisions_terminale` attaché au démarrage** : aucune clé à créer, les identifiants sont fournis par le proxy. **Ne jamais demander ni stocker de jeton.** Le compte GitHub `orhanYJ` est celui d'Orhan, à connecter au compte Claude de Cengiz (piège : le compte lié est celui ouvert dans le navigateur au moment d'autoriser).
8. Cengiz vérifie lui-même le rendu des URL sur son téléphone.

---

## 9. Reste à faire

- **ACL écrit** : paragraphes PEEL modèles ; chapitres 11 à 21 de *Brick Lane* puis outillage d'attaque ; notes de cours du professeur pour Lughnasa.
- **ACL oral** : trois poèmes restants ; Butler à partir du chapitre 14 **seulement quand la classe y sera**.
- **DNL** : chapitres restants au fil des cours de M. Ros ; section « Oral » simulant le tirage croisé ; intégrer la liste officielle des 10 Key Issues + 10 Key Terms (distribuée vers fin avril) ; QCM et flashcards par chapitre ; rappels de Première (thème 4 d'histoire, la Première Guerre mondiale, jamais traité en classe par Orhan, à rédiger au niveau des chapitres de Terminale).
- **SVT** : chapitre 2 terminé ; intégrer la correction du TP ECE chloroplastes quand elle arrivera ; ensuite les chapitres suivants unité par unité depuis les notes et diaporamas de Mme Philip ; refonte animée par schémas motion design.
- **PC** : reprendre le chapitre 1 sur le modèle du chapitre 2 ; chapitres suivants selon la progression ; animations explicatives dans `pc/anim/` (conductimétrie et titrages des chapitres 2-3 à suivre) ; chapitre 4 : intégrer les réponses d'Orhan au TP 6 quand il l'aura fait.
- **Philo** : ouvrir les trois autres parties du chapitre I au fil du cours. Point ouvert à poser à M. Bellon : l'exemple de la chute libre illustre-t-il la liberté comme mouvement sans obstacle, ou la ruine-t-il ? Erreur à corriger dans le brouillon d'Orhan sur le Kant : il a noté « la liberté vient de la suppression de tous les désirs », le texte dit l'inverse (« tu dois, donc tu peux »).
- **Italien, Red Pen** : extension selon la progression d'Orhan.
- **CDM** : faire valider la nouvelle problématique ; envoyer en octobre les cinq questions aux quatre partenaires (Orhan relance, la date a été promise par écrit) ; terrain en collège (25 min, un vendredi après-midi) et questionnaire de suivi deux semaines après.
- **Site d'animations** SVT / physique-chimie, à créer.

## 10. Contraintes particulières

- **Partenaires CDM** (Chloe / The Sleep Charity, Dr Amanda Ferguson / Cambridge, Pr Bei Bei / Monash, Alixe Avoine / Lycée Condorcet Sydney) : échanges **écrits uniquement** (jamais d'appel ni de visio), **en anglais**, **personnel adulte seulement**, environ 200 mots, aucune question dans l'email de premier contact, engagement présenté comme environ 20 minutes sur l'année. Conserver tous les fils d'emails comme preuve de contribution.
- **Atelier de philosophie** (outil de dialogue IA) : reste un **artefact Claude.ai uniquement**, ne jamais le republier sous `/atelier/` (la version PWA exigerait une clé d'API payante).
- **Thinking Aloud** (outil de tuteur IA pour CDM, ACL oral et écrit) : artefact Claude.ai partagé, **pas un site du dépôt**.
- Absence possible d'Orhan du 14 au 18 décembre 2026 (voyage familial) : Cengiz peut avoir besoin de courriers aux professeurs concernés (notamment M. Ros et le professeur d'EPS, pour le calendrier du CCF).
