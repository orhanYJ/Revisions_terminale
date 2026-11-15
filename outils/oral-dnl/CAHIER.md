# Cahier des charges — onglet « Oral » du site DNL (histoire-géographie en anglais, Terminale BFI)

## L'épreuve
Oral DNL (coefficient 10) : 20 min de préparation, puis 15 min devant le jury :
- 5 min d'exposé sur un **Key Issue** (question tirée au sort), puis 5 min de questions du jury ;
- 5 min de discussion sur un **Key Term** (notion tirée au sort).
L'élève parle **en anglais**. Le site est bilingue : chaque texte existe en anglais (`en`) et en français (`fr`) ;
le français est une vraie traduction fidèle (même contenu, même ordre), pas un résumé.

## Ce que tu produis
Pour chaque item qui t'est confié : un **texte prêt à dire en environ 5 minutes**, soit **650 à 750 mots en anglais**
(débit oral ~140 mots/min). Compte les mots de la partie « à dire » (champ `blocs`), hors plan et hors questions du jury.

### Key Issue (question)
Structure obligatoire d'un exposé de 5 min, dans `blocs`, dans cet ordre :
1. `intro` — accroche précise (une date, un fait, un chiffre du cours), définition des termes de la question,
   problématique, **jugement annoncé dès l'introduction** (ex. « I will argue that … largely / only partly … »), plan.
2. Deux ou trois `partie` — chacune : un titre court (`t`) et un paragraphe argumenté ; **chaque idée porte au moins
   un exemple précis du cours** (date, chiffre, nom, lieu). Une partie au moins nuance ou contredit (« however… »).
3. `conclusion` — réponse nette à la question (le degré : largely / partly…), rappel des 2-3 preuves les plus fortes,
   ouverture courte vers un autre chapitre ou thème.
Plus, hors temps de parole :
- `plan` : 4 à 6 lignes très courtes (le squelette à retenir en 20 min de préparation) ;
- `jury` : 3 questions que le jury pourrait poser ensuite, chacune avec une réponse de 2-4 phrases.

### Key Term (notion)
Dans `blocs`, dans cet ordre :
1. `definition` — une définition d'une ou deux phrases, à apprendre par cœur (reprendre la définition du cours si elle existe).
2. `partie` « Origins / context » — d'où vient la notion, quand, pourquoi.
3. `partie` « In the course » — 3 ou 4 exemples précis tirés du cours, avec dates et chiffres.
4. `partie` « Debates and limits » — nuances, critiques, ce que la notion ne dit pas.
5. `conclusion` « Links » — liens avec d'autres chapitres / thèmes et avec les key issues.
Plus `plan` (4-6 lignes) et `jury` (3 questions + réponses), comme pour les key issues.

## Règles de contenu (impératives)
- **Tout vient du cours du site** (fichiers `cours_*.txt` fournis) : idées, exemples, chiffres. Cite les faits tels qu'ils
  y sont. Ne contredis jamais le cours.
- Un fait **hors du cours** n'est permis que s'il est sûr, utile et courant au niveau Terminale ; il est alors suivi de
  la mention exacte « (added from outside the course) » en anglais et « (ajouté hors du cours) » en français.
  Reste très parcimonieux (2 au maximum par item).
- **Aucune information personnelle** : jamais le nom du professeur, d'un élève, de l'établissement. Écris
  « the course », « the course slide », « the worksheet ».
- Anglais naturel d'oral, niveau B2-C1, phrases nettes, connecteurs d'oral (« First of all », « This leads me to »,
  « To sum up »). Pas de listes à puces dans `blocs` : de la prose qu'on peut dire à voix haute.
- Le français : traduction fidèle, typographie française (espaces avant ; : ! ?, guillemets « »).
- Termes techniques anglais du cours conservés en français quand c'est l'usage du site (key term, choke point, EEZ → ZEE).

## Format de sortie : un fichier JSON (UTF-8, valide) — une liste d'items
```json
[
  {
    "id": "h1-ki-1",
    "kind": "issue",            // "issue" ou "term"
    "q": "texte officiel exact de la question ou du terme (anglais, tel que fourni)",
    "q_fr": "traduction française de la question / du terme",
    "chapitres": ["H1", "H2"],  // chapitres du cours mobilisés
    "en": {
      "plan": ["…", "…"],
      "blocs": [
        {"k": "intro", "p": "…"},
        {"k": "partie", "t": "…", "p": "…"},
        {"k": "conclusion", "p": "…"}
      ],
      "jury": [["question ?", "réponse"], ["…", "…"], ["…", "…"]]
    },
    "fr": { "plan": […], "blocs": [ même structure, traduite ], "jury": [ … ] }
  }
]
```
(`k` vaut `intro`, `definition`, `partie` ou `conclusion` ; `t` = titre d'une partie, présent pour `partie` et facultatif ailleurs.)
Les commentaires `//` ci-dessus sont explicatifs : le vrai fichier n'en contient pas.

## Vérification avant de rendre
- JSON valide (vérifie avec `python3 -c "import json;json.load(open('…'))"`).
- Compte les mots anglais de `blocs` de chaque item (650-750) et donne ces nombres dans ton compte rendu.
- Relis chaque chiffre et chaque date contre le fichier de cours.
