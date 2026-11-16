# Onglet Oral DNL — format « notes à puces » (16/11/2026)

Décision de Cengiz (16/11/2026) : « plutôt qu'un discours, une liste de bullet points ; vise 4 min 30, le max c'est 5 min ».
L'élève parle **à partir de ses notes**, il ne récite pas. Chaque key issue et chaque key term reçoit donc des **notes à puces**
que l'on développe à l'oral en **4 min 30** (5 min au maximum).

## Format de chaque item (JSON)
```json
{
  "id": "h-t1-ki-1", "kind": "issue", "q": "texte officiel exact", "q_fr": "traduction",
  "chapitres": ["H1", "H2"],
  "en": {
    "sections": [
      {"t": "Introduction", "d": 40, "pts": ["…", "…"]},
      {"t": "I. …", "d": 70, "pts": ["…"]},
      {"t": "II. …", "d": 70, "pts": ["…"]},
      {"t": "III. …", "d": 60, "pts": ["…"]},
      {"t": "Conclusion", "d": 30, "pts": ["…"]}
    ],
    "jury": [["question ?", "réponse en 2-4 phrases"], ["…", "…"], ["…", "…"]]
  },
  "fr": { même structure, traduite fidèlement (mêmes sections, mêmes puces, même ordre) }
}
```
- `d` = durée conseillée de la section en secondes ; **la somme fait 270** (4 min 30). Exemples : key issue 40 + 70 + 70 + 60 + 30 ;
  key term : « Definition » 30, « Origins » 50, « Examples » 90, « Debates and limits » 60, « Links » 40.
- **Key issue** : Introduction (accroche datée, termes définis, **jugement annoncé**, plan) ; 2 ou 3 parties titrées (I., II., III.) dont
  une qui nuance (« However … ») ; Conclusion (réponse nette, preuves les plus fortes, ouverture).
- **Key term** : Definition (une phrase à savoir par cœur, gardée entière), Origins / context, Examples, Debates and limits, Links.

## Les puces
- **Plus d'idées, moins d'exemples** (Cengiz, 16/11/2026) : une puce énonce une idée (argument, cause, mécanisme, conséquence, nuance, jugement), suivie au plus d'un exemple court après un tiret (« — e.g. Rhineland, 7 March 1936 »). Pas de listes de dates ni de chiffres. 16 à 20 puces, dont au moins 12 idées. Key term : la section de 90 s s'appelle « Key features » / « Caractéristiques » (les traits de la notion, un exemple chacun).
- **14 à 20 puces par item**, 6 à 18 mots chacune ; **220 à 320 mots anglais en tout** (puces seulement) : développées à l'oral,
  elles tiennent 4 min 30.
- Des **notes**, pas des phrases rédigées : mots clés, dates, chiffres, noms, exemples précis, liens logiques
  (« → », « but », « so », « = »). Une puce = une idée ou un exemple que l'on développe en 10 à 20 secondes.
  Exemple : « Munich, 29–30 Sept. 1938: Sudetenland given away → Prague, 15 March 1939 ».
- La puce du jugement commence par « Judgement: » (« Jugement : » en français).
- Chaque idée porte un exemple précis (date, chiffre, nom, lieu).

## Règles de contenu
- Les faits viennent de la version rédigée déjà vérifiée (`h_t1_issues.json`, `h_t1_terms.json`, champ `blocs`) et du cours du site ;
  ne rien ajouter d'autre.
- **Aucune référence à un cours, une classe, un professeur, une feuille, une worksheet, un diaporama** (règle des sites du 10/11/2026) :
  pas de « the course », « as the course quotes him », « the teacher's sheet », « (added from outside the course) ». Énoncer les faits directement.
  La citation d'Hitler datée « 11 December 1941 » (source non retrouvée) n'est **pas** reprise telle quelle : garder seulement l'idée
  (« Nazi aims: eliminate the Jews, German supremacy, a "community of nations" under German leadership »).
- Pas de nom de personne réelle de l'entourage (ni élève, ni professeur, ni établissement).
- Français : traduction fidèle, typographie française (espaces insécables avant ; : ! ?, guillemets « »), les termes anglais du programme
  gardés quand c'est l'usage (key issue, appeasement, Lebensraum).
- Les questions du jury : reprendre celles de la version rédigée, réponses raccourcies à 2-4 phrases, sans référence au cours.
