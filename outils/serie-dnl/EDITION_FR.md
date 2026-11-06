# Édition française des séries vidéo d'histoire (cahier des charges, 06/11/2026)

Demande de Cengiz : « une édition en français ; pareil qu'en anglais, la langue change ; tu ne mentionnes plus la DNL
mais l'histoire-géo classique ». Une série française par chapitre (H1, H2, H3), à côté de la série anglaise.

## Fichiers

- Script `outils/serie-dnl/h<chap>f_<n>.py`, traduit et adapté du script anglais `h<chap>_<n>.py` (le garder intact).
- En tête : `SITE = "dnl"`, `LANGUE = "fr"`, `CODE = "h<chap>f-<n>"`, `NOTION` en français (ex. « La Seconde Guerre
  mondiale »), `NUM`, `TITRE` en français, `SUIVANT = "Épisode <n+1> · <titre français>"` (ou rien pour le dernier).
- `PRONONCIATION` propre à la voix française : graphie phonétique française pour les mots étrangers que la voix lirait mal
  (ex. « Lebensraum » → « Lé-benss-raoum », « Einsatzgruppen » → « Aïne-zats-groupen », « Wehrmacht » → « Vèr-markt »,
  « Luftwaffe » → « Louft-vaffe », « Blitz » laisser tel quel). Les graphies anglaises du script anglais sont à jeter.
  Ne mettre que des mots réellement présents dans le texte lu ; une graphie à traits d'union est bien rendue dans les
  sous-titres (le générateur rétablit le mot écrit).
- Garder exactement la même structure : mêmes scènes, mêmes identifiants de visuels, mêmes repères `{id}`, `{-id}`,
  `{id.k}`, `{!mot}` placés au même endroit du sens, mêmes `globe` (mêmes numéros `sc` / `seg` : la carte animée
  passe d'elle-même en français), mêmes graphes et données, mêmes images (légendes traduites, crédits identiques).
  Une liste garde le même nombre de lignes (chaque ligne k a son repère `{id.k}`).
- Contrôle : `python3 outils/serie-philo/verifier.py h<chap>f_<n>` depuis la racine du dépôt doit passer sans erreur.
  Ne lancer ni `generer.py`, ni Chromium, ni Playwright (la voix et les captures sont faites ensuite, une à la fois).

## Langue et ton

- Français oral, naturel, fluide, écrit pour l'oreille : phrases courtes, pas de calque de l'anglais
  (« Here is one way to say it » → « On peut le dire ainsi »). Tutoiement du spectateur, comme le lecteur (« À toi »).
- Les nombres et dates en toutes lettres dans le texte lu quand l'anglais le faisait (« le six novembre 1941 »,
  « quatre-vingt-onze mille »), en chiffres à l'écran.
- Durée : à peu près celle de l'épisode anglais (le français est un peu plus long : resserrer plutôt qu'allonger).

## Ce qui change par rapport à l'édition anglaise

- **Plus aucune mention de la DNL, de la section BFI / ASIBA, de l'anglais comme langue d'examen**, ni du professeur,
  ni d'un élève précis : on s'adresse à un élève de Terminale qui suit l'histoire-géographie classique.
- Vocabulaire scolaire français :
  - « Key Term » → « notion clé » ; « Key Issue » → « problématique » ;
  - « Worksheet N » → « le dossier documentaire » ou « l'étude de cas » (sans numéro), « Source N » → « document N » ;
  - « the course slide / map / table » → « le document », « la carte », « le tableau » (ou « une carte du cours » si besoin) ;
  - « essay » → « réponse à une question problématisée » (ou « composition ») ; « DBQ » → « analyse de document » ;
    la structure « How useful… / largely useful » devient la démarche française de l'analyse : présenter le document,
    le situer, l'expliquer, en montrer l'intérêt et les limites ; « jugement » → « bilan critique » ;
  - « Your turn » reste la pause « À toi » (même type `pause`).
- Les citations : en français. Si l'original est français (appel du 18 juin, textes de Vichy, Pétain), reprendre le texte
  original exact. Sinon, une traduction française courante et fidèle (Churchill : « nous nous battrons sur les plages… nous
  ne nous rendrons jamais »). Ne jamais inventer : si une traduction établie n'est pas sûre, traduire au plus près et
  garder la source affichée. La phrase de Hitler du 11 décembre 1941 reste présentée « telle que le cours la cite ».
- Les faits restent ceux de l'édition anglaise corrigée (dates, chiffres) ; ne rien ajouter qui n'y soit pas.
- `QUIZ` en français (mêmes réponses justes), `CREDITS` en français, sans nom de professeur
  (« Contenu : le cours d'histoire de Terminale, chapitre … »).

## Épisode d'épreuve (H1 : 5, H2 : 8, H3 : 6)

Il ne présente plus l'essay et le DBQ de la DNL : il présente les exercices de l'histoire-géographie de Terminale,
la **réponse à une question problématisée** (introduction avec problématique, plan, paragraphes argument + exemple
précis, conclusion) et l'**analyse de document(s)** (consigne, présentation, contexte, explication, intérêt et limites),
avec les mêmes sujets et documents du chapitre que l'épisode anglais, les mêmes pauses « À toi » et des modèles rédigés en
français. Pas de barème inventé ; pas de référence à un guide d'examen étranger à l'histoire-géographie classique.
