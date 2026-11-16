# Cahier des charges des shorts (TikTok / YouTube Shorts) — chaîne « Révisions Animées »

Vidéos verticales 1080 × 1920, **en français**, pour attirer des élèves de Terminale vers la chaîne YouTube « Révisions Animées ». Modèle validé par Cengiz : `milgram.*` (« un banger »). Lire d'abord **entièrement** : `milgram.py`, `milgram.plan.js`, `milgram.types-a.js`, `milgram.description.md`, puis `modele-a.js` (types de plans du modèle A et leurs champs), `formats-a.js` (plans `copie`, `fiche`, `vraifaux`, documentés en tête), `dessins.js` (`S.d.*`), `core.js` (API `S`), `voix.py`, `verifier.js`, et le court essai `essaiformats.plan.js`.

## Quatre formats
1. **Histoire vraie folle** (recette Milgram) : 2e personne et présent, on démarre au milieu de l'action, un personnage, suspense qui monte, révélation simple, lien avec le cours, question de bac, « La réponse est sur Révisions Animées », dernière phrase qui relance la première (boucle).
2. **Question type bac** : le sujet en accroche (« Ce sujet tombe au bac. Tu as 60 secondes. »), pourquoi il est piégeux, la problématique, le plan en deux ou trois parties avec un argument et un exemple par partie, l'erreur à ne pas faire ; le plan `copie` s'écrit au fil de la voix ; rythme posé et clair ; fin : « Le cours complet est sur Révisions Animées ».
3. **Résumé de cours express** (« X en 60 secondes ») : 5 idées clés au plus, chacune avec son exemple, en plans `fiche` et en plans dessinés ; rythme rapide ; fin vers la série ou le chapitre.
4. **Vrai ou faux** : 4 ou 5 affirmations surprenantes (plan `vraifaux` : l'affirmation, un chrono de 2 à 3 s de silence ou de suspense dans la voix — « Vrai… ou faux ? » —, puis le verdict et une explication en une phrase) ; accroche « 5 affirmations. Combien tu en as justes ? » ; fin : « Dis ton score en commentaire » puis la chaîne.

5. **Qui a dit ça ? / quiz à trois choix** (ajouté le 13/11/2026) : 4 questions (souvent une citation à attribuer, ou une question de cours), plan `quiz3` (`formats-a.js` : `sur`, `n`, `q`, `options` = 3 réponses avec `img` facultatif, `bonne`, `chrono` = repère de « A, B ou C ? », `rep` = repère du verdict, `expl`) ; accroche « 4 citations. Combien tu en reconnais ? » ; fin : score en commentaire, puis la chaîne.

## Nouveautés du 15/11/2026 (demande de Cengiz : plus de formats où le spectateur joue, plus d'images, plus de variété, musiques funk agressives)
Les formats qui marchent sont ceux qui **impliquent le spectateur** (« combien tu en as justes ? »). Six nouveaux plans dans `formats-a.js` (champs documentés en tête de chaque fonction), essai complet dans `essai2.plan.js` :
- `niveau` : échelle de difficulté « Niveau 1 → 10, à quel niveau tu t'arrêtes ? » (n, total, q, r, expl, chrono, rep, img facultatif) ;
- `ordre` : « Remets dans l'ordre » (cartes = [{t, d}] montrées mélangées, ordre = indices dans le bon ordre, chrono, rep, expl) ;
- `intrus` : « Trouve l'intrus » (options = 4 × {t, img, sous, nb}, intrus, chrono, rep, expl) ;
- `devine` : « Devine qui c'est » (img pixellisée qui se précise à chaque indice, indices = [[repère, texte]], rep, nom, sous) ;
- `plusmoins` : « Plus ou moins ? » (q, A = {t, img, v, u}, B = {t, img, v, u}, chrono, rep ; la valeur de B défile) ;
- `erreur` : « Trouve l'erreur » dans une copie (matiere, sujet, lignes, faute, correction, chrono, rep).
Plans de `modele-a.js` pour les images : `photo` (photo **en couleur** plein écran avec travelling, champs img, t, sous, de, vers, nb, legende) et `collage` (imgs = 3 ou 4 images qui tombent, t, couleur).

**Habillage** : `window.THEME = '<nom>'` dans le `.plan.js` : `archives` (noir, crème, or, rouge), `neon` (violet nuit, cyan, rose, grille rétro), `jeu` (plateau de jeu télé, violet, jaune, rayons), `alerte` (flash info, rouge, jaune, bandeau défilant), `terminal` (dossier secret, vert sur noir, code qui tombe). Chaque short a un habillage précisé par ta mission. **Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité)** dans les plans propres, jamais de code couleur en dur (sinon l'habillage ne s'applique pas). Les transitions varient seules selon l'habillage (zoom, glisse, tourne, chute, glitch, iris) ; `trans: '<type>'` sur un plan l'impose.

**Variété obligatoire** : jamais deux plans de suite du même type ; au moins 6 plans avec image (photo, collage, carte, portrait, intrus, devine…) ; des plans propres variés (pas seulement des mots).

**Musique** : funk brésilien agressif par défaut (choix de Cengiz) : `funk_agressif`, `funk_agressif2`, `funk_agressif3`, `montagem`, `montagem2`, `montagem3`, `automotivo`, `automotivo2` ; parfois `hardtekk`, `hardtekk2`, `terre`, `terre2` (`orchestre.py`). La caméra pulse sur le temps de la musique.

**Images** : celles du dépôt (`philo/serie/img/`, `dnl/serie/img/`, `svt/serie/img/`, `pc/serie/img/`, `acl-*/serie/img/`), licence retrouvée dans les `legende=` / `CREDITS` des scripts `outils/serie-*/*.py`. Une image nouvelle n'est permise que du domaine public ou sous CC BY / CC BY-SA, depuis Wikimedia Commons (vignette `upload.wikimedia.org/…/thumb/…/1280px-…`), enregistrée dans `outils/shorts/img/`, avec auteur et licence en commentaire dans `window.IMAGES` et dans la description.

## Règles communes
- **Faits** : uniquement ce que contient le cours de la chaîne (site et scripts des vidéos indiqués dans ta mission) ; tout fait pris ailleurs est vérifié sur une source sérieuse (WebSearch / WebFetch) et la source va en tête du script. Aucun fait inventé, aucune lacune comblée ; un point incertain est écarté.
- **Aucune information personnelle** : aucun nom de professeur, d'élève, d'établissement, de ville.
- **Droit d'auteur** : citations d'œuvres sous droits très courtes (une ligne), traduites dans la voix.
- **Voix** : `VOIX = "energique"`, `TEMPO = 1.0`, `CIBLE = 75` (format 2 : `CIBLE = 70`). Texte : **175 à 205 mots** lus, 14 à 20 passages. Tous les nombres écrits en chiffres dans le texte et ajoutés à `PRONONCIATION` en toutes lettres ; noms propres difficiles aussi (graphie française approchée). Une phrase = une idée, phrases courtes, langue orale, tutoiement.
- **Musique** : `window.MUSIQUE = '<style>'` dans le `.plan.js` (style imposé par ta mission). Styles : voir `musique_short.py` (`VARIANTES`), dont, depuis le 13/11/2026, `grec` (lyre et tambour antiques), `boom_bap` (hip-hop piano jazz), `chiptune` (8 bits), `ambient_mer` (nappes marines).
- **Découpage** : un plan toutes les 1,5 à 2,5 s (30 à 40 plans ; un plan `copie`, `fiche` ou `vraifaux` peut durer plus longtemps puisqu'il évolue au fil de la voix), 5 chapitres (`ch: 0` à `4` et `window.CHAPITRES`), 2 à 4 plans `choc: true` pour les formats 1 et 4 (0 à 2 pour les formats 2 et 3), un plan `chaine` (champ `serie`, `fond` = une image), pas de plan de moins de 0,5 s. Les repères `a: [passage, mot]` désignent le mot tel qu'il est écrit, apostrophe comprise (`"l'homme"`, pas `"homme"`).
- **Plans propres** dans `<code>.types-a.js` (structure de `milgram.types-a.js`) : scènes simples et lisibles, dessinées en canvas 2D, style du modèle A (noir #0d0b09, crème #efe6d2, or #d9b45a, rouge #c8372d). Sons de `mix.py` (`sfx`) : boum, drop, papier, whoosh, souffle, montee, aspire, tampon, tic, blip, pop, bip, lame, coeur, rembobine, disque, stylo, statique, glitch, gong, chapitre, valide, coupe, frappe, buzz, clic, frotte (peu de sons de coupe).
- **Images** : seulement des images déjà dans le dépôt, de licence connue (retrouver la licence dans les `legende=` des scripts `outils/serie-*/*.py`), déclarées dans `window.IMAGES` avec la licence en commentaire ; sinon, dessiner.
- **Description** `<code>.description.md` : titre YouTube Shorts, description TikTok prête à coller (avec une question pour les commentaires), hashtags, sources.

## Contrôles obligatoires
1. `node --check` sur tes fichiers JS.
2. `cd /home/user/Revisions_terminale/outils/shorts && SHORT_MUET=1 python3 voix.py <code> && cp sortie/<code>.data.js sortie/<code>.muet.data.js && node verifier.js <code>` → OK (durée muette visée : 65 à 75 s).
3. Interdit : lancer un navigateur (Chromium, Playwright, `rendu.js`) ou `voix.py` sans `SHORT_MUET=1` (une voix tourne dans le conteneur, mémoire limitée) ; modifier un fichier commun (`core.js`, `modele-a.js`, `formats-a.js`, `dessins.js`, `mix.py`, `musique_short.py`, `rendu.js`, `short.html`, `voix.py`, `verifier.js`) — décris le besoin dans ton rapport ; faire un commit.
4. Rapport final court : le texte lu complet, les faits et leur source, les points écartés, la durée muette, le résultat du vérificateur.
