# Onglet Oral DNL — discours rédigé dépliable (17/11/2026)

Demande de Cengiz (17/11/2026) : sous les notes à puces de chaque key issue et de chaque key term, un **discours rédigé**,
dépliable (fermé par défaut), qui montre comment les notes se développent à l'oral. « Assure-toi que le discours est cohérent ;
ce n'est pas une thèse à défendre, mais une explication objective. »

## Format
Dans chaque item, à côté de `sections` et `jury`, pour `en` et pour `fr` :
```json
"discours": [
  {"t": "Introduction", "p": "Paragraphe…"},
  {"t": "I. …", "p": "Paragraphe…"},
  …
  {"t": "Conclusion", "p": "Paragraphe…"}
]
```
- **Une entrée par section des notes, dans le même ordre, avec exactement le même titre `t`** que la section correspondante.
- `p` = un paragraphe (deux au plus, séparés par `\n\n`).

## Longueur
- 4 min 30 à l'oral, 140 mots par minute : **600 à 680 mots anglais** au total (jamais plus de 700 = 5 min).
- Chaque section reçoit à peu près la part de mots de sa durée `d` (d / 270 × total).

## Cohérence avec les notes
- Le discours **développe les puces de sa section, dans l'ordre**, toutes, sans en ajouter d'autres : chaque puce devient une ou deux
  phrases (l'idée, puis l'exemple qui l'illustre). Quelqu'un qui lit les notes puis le discours doit retrouver la même chose.
- Des transitions entre les parties (« This leads to… », « Yet… », « Finally… ») ; une introduction qui pose la question et annonce le plan,
  une conclusion qui répond.
- Aucun fait qui ne soit pas dans les notes ou dans la version rédigée vérifiée (`<thème>_*_redige.json`).

## Ton : expliquer, pas plaider
- **Explication objective** : on expose les faits, les mécanismes, les causes ; quand il y a débat entre historiens, on présente
  les positions et on les attribue (« Taylor argued… ; most historians stress… »), sans prendre parti avec emphase.
- Pas de rhétorique d'avocat (« clearly », « undeniably », « it is obvious that », « we must reject »), pas d'exclamations.
- Une question « How far do you agree… » ou « Assess the role… » attend une réponse : elle est donnée comme une **conclusion pesée**
  (ce que montrent les faits, et ses limites), pas comme une thèse à défendre.
- Une question « Assess the aims… » attend une **explication des buts et leur évaluation** (lesquels, comment ils se traduisent,
  lesquels étaient centraux ou secondaires, dans quelle mesure ils ont été réalisés), pas un réquisitoire.

## Évaluer tout au long (key issues, retour du professeur du 19/11/2026)
- Chaque paragraphe de partie **se termine par une phrase d'évaluation** qui développe la puce « Assessment: » de la partie
  (« So, in assessing these aims, … », « This shows that … was the central / a secondary … », « To a large extent, …, but … »).
- L'introduction énonce le jugement d'ensemble ; la conclusion le reprend en s'appuyant sur les bilans des parties.
- Toujours mesuré : peser et hiérarchiser, pas plaider.
- Longueur : 620 à 690 mots anglais (5 min au maximum).

## Règles communes (comme les notes)
- Aucune référence à un cours, une classe, un professeur, une feuille, une worksheet, un diaporama ; aucun nom d'élève ni de professeur.
- La citation d'Hitler datée « 11 December 1941 » n'apparaît pas (idée seulement).
- Français : traduction fidèle du discours anglais, même découpage ; typographie française (espaces insécables avant : ; ? ! %, « »).
  Éviter les mots « cours », « discours », « concours », « recours » (un contrôle automatique cherche « cours »).
