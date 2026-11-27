# Cahier des charges — listes de vocabulaire anglais « Wordsmith »

## Pour qui, pour quoi
Un élève français de Terminale en section internationale (niveau B2, vise C1). Il a de vraies lacunes en vocabulaire, surtout pour **s'exprimer** (à l'écrit et à l'oral), mais aussi pour comprendre. Il veut des mots **riches mais pratiques** : utilisables dans n'importe quel contexte (conversation, essay, oral, lecture d'articles), ni techniques (pas de vocabulaire scientifique, juridique, maritime, médical…), ni farfelus ou archaïques. Quelques mots un peu plus rares sont permis s'ils restent vraiment utiles. Référence de niveau : ce qu'un anglophone cultivé emploie couramment, bande C1 (parfois C2) des Oxford 5000 / English Vocabulary Profile. Pas de mots trop simples (pas de *important, difficult, happy*).

L'application lui propose 5 mots nouveaux par jour, **dans l'ordre de la liste** : mets donc **les plus utiles en premier**.

## Format exact (JSON)
Écris un fichier JSON : un tableau de 100 objets, chacun avec exactement ces champs.

```json
{
  "id": "s-meticulous",
  "w": "meticulous",
  "pos": "adjective",
  "ipa": "/məˈtɪkjələs/",
  "reg": "courant",
  "fr": "méticuleux, minutieux",
  "def": "Showing great attention to detail; very careful and precise.",
  "col": ["meticulous attention to detail", "meticulous planning", "meticulously researched"],
  "ex": ["She keeps [[meticulous]] notes of every meeting.", "The success of the operation depended on [[meticulous]] preparation."],
  "piege": "Toujours positif ou neutre. Pour un perfectionnisme excessif, on dit plutôt <i>fussy</i> ou <i>pedantic</i>.",
  "fam": "meticulously (adv.) · meticulousness (n.)",
  "trous": [
    {"s": "He is ___ about his appearance: not a hair out of place.", "a": "meticulous", "fr": "Il est méticuleux pour son apparence : pas un cheveu qui dépasse."},
    {"s": "The report was ___ researched and full of precise figures.", "a": "meticulously", "fr": "Le rapport était minutieusement documenté et plein de chiffres précis."}
  ],
  "ecris": "une phrase sur une personne ou un travail très soigné",
  "formes": ["meticulous", "meticulously", "meticulousness"]
}
```

Règles champ par champ :
- `id` : préfixe imposé (indiqué dans ta mission) + le mot en minuscules, tirets à la place des espaces (`p-come-to-terms-with`). Unique.
- `w` : l'entrée telle qu'on l'apprend (pour un verbe, sans *to* ; pour une expression, la forme de base : `come to terms with`, `take something for granted`).
- `pos` : en anglais (`verb`, `noun`, `adjective`, `adverb`, `phrasal verb`, `expression`, `idiom`…).
- `ipa` : prononciation **britannique** standard, entre barres obliques, accent tonique marqué. Sois rigoureux (c'est vérifié). Pour une expression longue, ne donne que le ou les mots difficiles.
- `reg` : `courant`, `formel` ou `familier` (en français, minuscules).
- `fr` : le sens en français, court (2 à 6 mots, plusieurs équivalents séparés par des virgules ; deux sens numérotés « 1. … · 2. … » si vraiment nécessaire).
- `def` : définition **en anglais simple**, une phrase, qui commence par une majuscule et finit par un point. C'est elle que l'élève voit en premier, et elle sert aussi de mauvaise réponse dans des QCM : elle doit être **précise et distinctive**.
- `col` : 3 ou 4 collocations naturelles et fréquentes.
- `ex` : exactement 2 exemples **originaux** (aucune citation d'œuvre), naturels, de 8 à 20 mots. Le premier tiré de la vie courante, le second d'un registre plus argumentatif (actualité, société, histoire, débat, littérature) qu'on pourrait réutiliser à l'écrit ou à l'oral. La forme du mot apparaît **exactement** entourée de `[[ ]]` (une seule fois par exemple ; pour une expression à trou, entoure toute l'expression telle qu'elle apparaît : `[[came to terms with]]`).
- `piege` : **en français**, une ou deux phrases : faux ami, construction (préposition, transitivité), nuance avec un synonyme proche, prononciation, registre. Balises HTML permises : `<b>`, `<i>` uniquement.
- `fam` : la famille de mots utile (`"x (n.) · y (adv.)"`), ou `"—"` s'il n'y en a pas.
- `trous` : exactement 2 phrases à compléter, **différentes des exemples**, avec `___` (trois tirets bas) **exactement une fois**. `a` = ce que l'élève doit taper (la forme fléchie exacte qui manque ; pour une expression, un seul trou qui contient le mot central — ex. phrase « She finally came to ___ with her loss. », `a` = « terms »). `alt` (facultatif) = autres réponses justes acceptées. `fr` = traduction française naturelle de la phrase complète. La phrase doit rendre la réponse **déductible** sans ambiguïté avec l'indice (la définition est affichée) : évite les phrases où dix mots iraient.
- `ecris` : en français, un sujet pour que l'élève écrive sa propre phrase (« une phrase sur… »).
- `formes` : toutes les formes qui comptent comme emploi du mot dans une phrase libre (conjugaisons, pluriel, adverbe, nom dérivé ; pour une expression, les formes conjuguées de l'expression entière, ex. `["come to terms with", "comes to terms with", "came to terms with", "coming to terms with"]`).

## Interdits
- Aucune personne réelle vivante nommée dans les exemples, aucun nom d'élève, de professeur ou d'établissement, aucune référence à « ton cours », « ta prof », « en classe ».
- Pas de contenu choquant ; pas de stéréotypes.
- Pas de mot hors sujet de ta liste, pas de doublon avec la liste interdite fournie.
- Orthographe britannique (*realise, behaviour, colour*).

## Vérification avant de rendre
Écris le fichier, puis vérifie-le avec un petit script Node ou Python : JSON valide, 100 entrées, ids uniques, tous les champs présents, `___` une fois dans chaque trou, `[[` présent dans chaque exemple, `a` (ou une `alt`) cohérente avec la phrase, aucune `def` en double. Relis l'IPA de chaque mot. Rends dans ton message final : le chemin du fichier, la liste des 100 mots dans l'ordre, et tout doute (IPA, sens) que tu n'as pas pu lever.
