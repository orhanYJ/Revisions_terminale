# Vidéos YouTube des spécialités (maths, SES, HGGSP) — cahier des charges d'un chapitre

Une vidéo longue par chapitre du site, publiée en MP4 1920 × 1080 sur YouTube et dans le site. Les trois pilotes sont
faits et servent de modèles : `outils/serie-maths/maths_ch1.py`, `outils/serie-ses/ses_e1.py`,
`outils/serie-hggsp/hggsp_t1_intro.py`. Lis d'abord `CLAUDE.md` (§2 règles, §4 « Spécialités ouvertes au public », en
particulier « Vidéos YouTube des spécialités »), puis le pilote de ta matière en entier, avec sa vidéo en ligne :
`https://orhanyj.github.io/Revisions_terminale/<site>/serie/<code>.html`.

## Contenu

- **Le chapitre du site, rien au-delà** : la source est `outils/specialites/<site>/src/` (maths `chN.js`, SES
  `data-<chap>.js`, HGGSP `data-t<N>.js`, `CHAPS["<id>"]`). Toutes les idées et les exemples importants, les démonstrations
  ou les mécanismes, les pièges, un ou deux exercices ou sujets type bac corrigés (pause « À toi » avant la correction),
  un récap « pour le bac ». Ce qui dépasse le programme est dit « hors programme ». Chiffres, dates, citations : ceux du
  site, vérifiés.
- Durée visée : 25 à 35 min (HGGSP : 20 à 30 min). `RYTHME = "vivant"`.
- **Texte écrit pour l'oral** : phrases courtes, une idée par phrase, questions au spectateur, relances, exemples racontés,
  transitions naturelles, respirations `("P", s)`. Tutoiement. Pas d'énumération lue d'une traite.
- **Aucune personne réelle** autre que les auteurs et acteurs du programme ; jamais « ton cours », « ta prof », « le
  diaporama », « le site dit », « cette vidéo a été générée ». Fin : une phrase qui renvoie au site pour les fiches, les QCM
  et les animations (« le lien est dans la description »), sans nom.
- Script : `outils/serie-<site>/<site>_<chapitre>.py`, `SITE = "<site>"`, `CODE = "<site>-<chapitre>"` (ex. `maths-ch2`,
  `ses-e2`, `hggsp-t1-a1`), `NUM`, `TITRE`, scènes avec une `humeur` musicale (lumiere, mystere, tension, calme).

## Image : l'identité de la matière (validée par le pilote du projet)

- **Maths, le tableau noir** (`maths/serie/moteur.js`) : tout s'écrit à la craie au repère du mot, sans craie visible ;
  formules (`$…$` en MathML), `formule` (lignes `{id.k}`, `cadre`, `m` note de marge, `lab`, `ind`), `graphe` (tracé à la
  règle), `illu` (dominos, cases, suites…), `exo` (énoncé puis `mode="coin"`), `pause`, `liste`, `def`, `note`, `code`
  (Python), `carte` (carte mentale finale) ; coup d'éponge entre les parties. Commentaires en tête de chaque type.
- **SES, le magazine qu'on feuillette** (`ses/serie/moteur.js`) : une double page par partie, encadrés « Décryptage »
  (`chaine`), infographies (`graphe`, `sanim` : graphiques et animations du site rejoués, `site-ses.js`), grands chiffres,
  `rubrique` ; la **ville miniature** (`ville`, scénarios) en illustration ponctuelle quand un mécanisme s'y prête.
- **HGGSP, la table des cartes de l'état-major** (`hggsp/serie/moteur.js`) : cartes gravées sur la table (`scene` de
  carte, fiches posées, pions, flèches de manœuvre, trait au crayon gras), `chrono` en réglette, `document` en fiche.
  Scènes de carte de la vidéo dans `hggsp/serie/illu-<code>.js` (voir `illu-hggsp-t1-intro.js` et `outils/serie-hggsp/`).
- **Nouvelle illustration** : jamais dans le moteur (plusieurs sessions travaillent en même temps), mais dans
  `<site>/serie/illu-<code>.js`, chargé après le moteur : `SERIE_ILLU.nom = function (svg, v) { … return function (t, st)
  { … }; }`, outils dans `window.SERIE_OUTILS` ; puis `dict(type="illu", nom="nom", …)` dans le script. Rendu fonction
  pure du temps.
- Lisibilité sur téléphone d'abord : texte grand, rien qui sorte du cadre, pas d'écran vide, sous-titres qui ne masquent
  rien d'important.

## Ordre de fabrication

1. **Script et brouillon sans voix** :
   `SERIE_MOTEUR=muet SSL_CERT_FILE=/root/.ccr/ca-bundle.crt PYTHONPATH=outils/serie-<site> python3 outils/serie-philo/generer.py <module>`,
   puis `verifier.py <module>`, `chevauchements.py <code>`, `fermer.py <module>` (maths, HGGSP ; en SES seulement si
   aucun chevauchement n'est voulu).
2. **Relecture de l'image** (serveur `python3 outils/serie-philo/serveur.py`, port 8765) :
   `node outils/serie-philo/superpositions.js <site>/serie/<code>.html` (doit ne rien signaler d'autre que des recouvrements
   voulus) et `node outils/serie-philo/planche.js <site>/serie/<code>.html <dossier>/p` (feuilles de 4 × 4, une image toutes
   les 8 s) ; **regarde chaque feuille** et corrige : texte qui déborde ou se chevauche, étiquette mal placée, écran vide,
   visuel qui ne suit pas la voix.
3. **Contrôle indépendant du script avant toute voix**, par un sous-agent qui ne l'a pas écrit (outil Agent) : chaque
   fait, chiffre, date, définition, attribution comparé au site et à la source d'origine, chaque calcul refait en Python,
   concordance écran / voix, prononciation des nombres et des noms, langue. Corrige, refais le brouillon et la planche.
4. **Voix** (une seule voix à la fois dans le conteneur, pas de Chromium pendant qu'elle tourne) :
   `SSL_CERT_FILE=/root/.ccr/ca-bundle.crt PYTHONPATH=outils/serie-<site> python3 outils/serie-philo/generer.py <module>`,
   en tâche de fond ; une tâche s'arrête au bout de 2 h : relance-la, le cache reprend. Puis `pip install num2words` et
   `PYTHONPATH=outils/serie-<site> python3 outils/serie-philo/controle_voix.py <module> > controle.txt` : trie les
   suspects (fausses alertes connues : homophones, noms propres écrits pour la voix, « indice » entendu « un dix ») ;
   rejette les vrais défauts (`controle_voix.py <module> "début du passage" …`) et relance `generer.py`. Ne garde aucun
   nombre mal dit, aucune liaison fautive, aucune voix plate quand une meilleure prise existe.
5. `chevauchements.py <code>` une dernière fois, puis commit de **tes seuls fichiers** : script (et module annexe),
   `<site>/serie/<code>.data.js`, `<code>.html`, `voix/<code>-{v,m}-*.mp3`, `illu-<code>.js`, images. Message en
   français terminé par les deux lignes d'attribution du dépôt. Pousse sur ta branche.

## Voix : écrire pour qu'elle prononce juste

- **Nombres en lettres** dans le texte lu (« mille six cent quatre-vingt-un », « zéro virgule huit »), dates comprises.
- **Maths** : reprends tel quel le bloc `PRONONCIATION` de `maths_ch1.py` (lettres des formules en majuscules : la voix
  les dit comme des lettres, sans liaison ; « plusse » et « moin » devant une lettre ou un nombre) et `LIAISONS = "maths"`.
  Annonce les résultats (« deux fois cinq, plus trois, ça fait treize »). Écris « u indice n » plutôt que « u n ».
- **HGGSP** : « milles » marins → `"milles marins": "mil marins", "milles": "mil marins"` en tête de `PRONONCIATION` ;
  noms étrangers en graphie française dans `PRONONCIATION` (l'écran garde l'orthographe).
- Liaisons : `outils/serie-philo/liaisons.py` contrôle chaque prise (liaisons obligatoires manquantes ; en maths, liaisons
  interdites devant une lettre ou un nombre). Une prise fautive est refaite automatiquement (jusqu'à six prises).

## Ce que tu ne touches pas

Les moteurs (`<site>/serie/moteur.*`), `generer.py`, `musique.py`, `voix_qwen.py`, `liaisons.py`, `controle_voix.py`,
`kit_youtube.py`, `site_ses.py`, les sources et le `sw.js` des sites, `CLAUDE.md`. Si l'un d'eux te bloque, décris le besoin
dans ton compte rendu. Pas de MP4, pas de PR : la session coordinatrice fusionne, publie et fabrique les MP4.

## Compte rendu (send_message à la session parente, session_id "@parent")

Branche et commit, durée, plan de la vidéo (parties), visuels et illustrations ajoutés, résultat des contrôles (image,
contrôle indépendant du script avec les corrections faites, voix : passages refaits et alertes restantes), ce qui reste
imparfait.
