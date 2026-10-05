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
- **Fiches mémo** : ce sont des travaux notés qu'Orhan rend à son professeur. Les sites ne fournissent **jamais** une fiche toute faite à rendre : modèle vierge, checklist de complétude, relecture de son propre brouillon.
- **Schéma idée / exemple (DNL)** : chaque idée porte un exemple précis, voire deux. Une idée est un phénomène, un fait ou un processus ; l'exemple est le cas précis où on l'observe. Si l'exemple n'est pas dans le cours, en chercher un dans des sources valides et **signaler qu'il vient d'ailleurs**.
- **Corps du cours** : bilans, idées, explications, définitions seulement. Le détail des TP et activités va dans des panneaux repliables, fermés par défaut.
- **Hors programme** : la structure interne d'un cours est libre (du plus large au plus précis, expliquer le pourquoi et les mécanismes), mais ce qui dépasse le programme est marqué « hors programme ».
- **QCM** : majoritairement sur les idées du cours et les rappels de Première associés (avec renvoi vers la fiche) ; quelques questions de TP en série séparée.
- **Ne jamais stocker un jeton ou un identifiant** dans un fichier du dépôt, la mémoire ou un document.

Préférence de travail de Cengiz : **conseiller de changer de modèle ou de niveau d'effort** quand une demande est trop triviale ou trop complexe pour le réglage actuel, et **proposer de scinder un site** quand son poids devient trop lourd.

---

## 3. Carte du dépôt

| Dossier | Contenu | Poids `index.html` | Pile |
|---|---|---|---|
| `svt/` | Spé SVT Terminale (Mme Philip) | ~544 Ko | JS natif, données en constantes |
| `pc/` | Spé Physique-Chimie | ~817 Ko | JS natif |
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
| `fenuareo/` | **Projet distinct** (apprentissage du reo tahiti), pas un site de révision d'Orhan | ~1,2 Mo | — |
| `test.html` | Reliquat d'un test de publication | — | à supprimer avec l'accord de Cengiz |

Chaque dossier de site contient la même structure : `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`. Certains ajoutent `motion.css` et `motion.js` (voir §5).

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

État : chapitre 1 « L'origine du génotype des individus » **terminé** (le chapitre 2 de Mme Philip s'ouvre sur « Nous avons vu les transferts verticaux »). Il compte deux unités seulement, d'après l'en-tête de la fiche de TP « Chap 1 – Unité 2 » : unité 1 (`t1u1`, clones), unité 2 (`t1u2`, brassages) et sa suite sur une page séparée (`t1u2b`, « Accidents génétiques lors de la méiose », ajoutée le 05/10/2026 depuis l'exposé collectif « support Eva », le TP globines et les notes d'Orhan). Il n'y a pas d'unités 3 et 4. Le diaporama des accidents a été rédigé par les élèves et contient des erreurs (corrigées dans le site, signalées en encadrés). Chapitre 2 « Complexification des génomes » (`t2`) : traité en classe jusqu'à la syncytine au 05/10/2026 (TP type bac syncytine fait à distance, **non corrigé**) ; transduction et endosymbioses pas encore vues. Orhan se dit très faible en géologie : ces chapitres doivent être particulièrement solides.

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

État : H1 (« The Wall Street Crash and its Impact ») réécrit en entier à partir du diaporama de M. Ros ; H2 (régimes totalitaires) complet (parties I à III, version Claude.ai du 05/10/2026, partie II corrigée et complétée le même jour d'après les notes d'Orhan et les Worksheets 3 et 4) ; H3 (« World War Two ») commencé (introduction et I.1) ; les autres chapitres sont des placeholders. Un script d'audit (`audit_idee_exemple.py`) vérifiait l'ancrage date/chiffre/nom propre de chaque exemple dans les deux langues : **il n'est pas dans le dépôt**.

### Philosophie (`philo/`)

React 18.2 UMD précompilé inline. Constantes : `NOTIONS` (17 notions du programme), `COURANTS`, `AUTEURS`, plus les repères et plus de 220 citations (champs `breve` et `approf`), un badge « ≈ paraphrase » sur les citations non littérales, une galerie de textes, un onglet « Mon prof ».

M. Thomas Bellon ne traite **pas** les notions une par une : il fait des chapitres par problème qui croisent plusieurs notions (chapitre 1 « la liberté » en quatre parties : métaphysique, morale, politique, peut-être esthétique). La couche « cours » prévue au-dessus de l'index par notion stocke des **distinctions** (couples de termes), chacune avec les deux termes, le contenu du cours, l'exemple de Bellon, le repère, l'auteur et une phrase de transition réutilisable en dissertation.

État : la couche « Le cours de M. Bellon » est publiée depuis le 05/10/2026 (`philo-v2`) : chapitre I « La liberté », partie 1 (liberté métaphysique) rédigée, parties 2 à 4 en attente ; page « L'explication de texte » sur le texte de Kant.

### Physique-Chimie (`pc/`)

JS natif, 21 chapitres dans l'ordre du professeur, thème orange sur sombre. Chapitres 1 à 3 ouverts (le 3, méthodes chimiques d'analyse / titrage, ajouté le 02/10/2026) ; le reste est en placeholder. Pour chaque chapitre : plan de travail du professeur, **plus** d'autres exercices du manuel (Le Livre Scolaire) et des exercices type bac créés par Claude **signalés comme tels**, dont des exercices bilan couvrant toutes les notions exigibles. Le chapitre 1 reste à reprendre sur ce modèle. Visuels de labo complexes : prompts pour Nano Banana (anglais, fond blanc, style vectoriel plat de manuel, annotations en français, flèches `#E45C10`).

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

---

## 6. PWA et service workers

- Chaque site a un `manifest.json` (`display: standalone`, `start_url: "./"`, `scope: "./"`, icônes 192 et 512 en `any maskable`) et un `sw.js`.
- Stratégie : **réseau d'abord pour la page** (une nouvelle version est visible dès le prochain lancement, sans vider le cache), **cache d'abord pour les assets**.
- Chaque `sw.js` porte un nom de cache versionné en tête de fichier (`svt-v5`, `dnl-v18-h2-corrige`, `philo-v3`, `redpen-v2`, `cdm-v2`, `fenuareo-v2`, etc.). **Incrémenter ce nom à chaque livraison qui ajoute ou modifie un fichier annexe.**
- Le dépôt étant public, ne rien y mettre qu'on ne veuille pas voir en ligne.

---

## 7. Écarts connus et points à décider

1. **DNL charge React depuis cdnjs et des polices Google** : cela contredit la règle « aucune dépendance externe, fonctionne hors ligne », et le service worker ne précache pas ces ressources. Soit on les inline (React coûte de l'ordre de 140 Ko), soit on assume l'écart. À arbitrer avec Cengiz.
2. **Livré mais pas publié, d'après la mémoire de projet** (à vérifier dans le dépôt avant de refaire) :
   - `svt/anim/*.html` : les animations plein écran (méiose / crossing-over, ouvertes depuis un bouton sur le schéma) sont absentes du dépôt.
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
- **SVT** : chapitre 2 (complexification des génomes) jusqu'à la syncytine, puis la suite au fil du cours, puis les chapitres suivants unité par unité depuis les notes et diaporamas de Mme Philip ; refonte animée par schémas motion design.
- **PC** : reprendre le chapitre 1 sur le modèle du chapitre 2 ; chapitres suivants selon la progression ; animation de conductimétrie.
- **Philo** : ouvrir les trois autres parties du chapitre I au fil du cours. Point ouvert à poser à M. Bellon : l'exemple de la chute libre illustre-t-il la liberté comme mouvement sans obstacle, ou la ruine-t-il ? Erreur à corriger dans le brouillon d'Orhan sur le Kant : il a noté « la liberté vient de la suppression de tous les désirs », le texte dit l'inverse (« tu dois, donc tu peux »).
- **Italien, Red Pen** : extension selon la progression d'Orhan.
- **CDM** : faire valider la nouvelle problématique ; envoyer en octobre les cinq questions aux quatre partenaires (Orhan relance, la date a été promise par écrit) ; terrain en collège (25 min, un vendredi après-midi) et questionnaire de suivi deux semaines après.
- **Site d'animations** SVT / physique-chimie, à créer.

## 10. Contraintes particulières

- **Partenaires CDM** (Chloe / The Sleep Charity, Dr Amanda Ferguson / Cambridge, Pr Bei Bei / Monash, Alixe Avoine / Lycée Condorcet Sydney) : échanges **écrits uniquement** (jamais d'appel ni de visio), **en anglais**, **personnel adulte seulement**, environ 200 mots, aucune question dans l'email de premier contact, engagement présenté comme environ 20 minutes sur l'année. Conserver tous les fils d'emails comme preuve de contribution.
- **Atelier de philosophie** (outil de dialogue IA) : reste un **artefact Claude.ai uniquement**, ne jamais le republier sous `/atelier/` (la version PWA exigerait une clé d'API payante).
- **Thinking Aloud** (outil de tuteur IA pour CDM, ACL oral et écrit) : artefact Claude.ai partagé, **pas un site du dépôt**.
- Absence possible d'Orhan du 14 au 18 décembre 2026 (voyage familial) : Cengiz peut avoir besoin de courriers aux professeurs concernés (notamment M. Ros et le professeur d'EPS, pour le calendrier du CCF).
