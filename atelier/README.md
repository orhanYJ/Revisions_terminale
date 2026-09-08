# Atelier de philosophie

Entraînement au dialogue philosophique pour la terminale.
Quatre exercices : creuser une notion, défendre une thèse contre objections,
problématiser un sujet de dissertation, expliquer un texte.

Les réponses sont générées en direct par un modèle Claude. L'application
n'écrit jamais de plan ni de paragraphe à la place de l'élève.

En ligne : https://orhanyj.github.io/Revisions_terminale/atelier/

À ne pas confondre avec `philo/` (L'Index raisonné), qui est un autre site du
dépôt. Les deux cohabitent : dossiers distincts, cache distinct
(`atelier-v1`), clés de stockage préfixées `atelier.`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | l'application entière (interface + logique + appels au modèle) |
| `manifest.json` | déclaration PWA : nom, icônes, mode plein écran |
| `sw.js` | service worker : ouverture hors ligne de la coquille |
| `icon-192.png`, `icon-512.png`, `icon-512-maskable.png` | icônes de l'écran d'accueil |

## Clé API

Aucune clé n'est écrite dans ce dépôt. L'élève saisit la sienne au premier
lancement ; elle est conservée dans le `localStorage` de son appareil sous
`atelier.cle` et n'est transmise qu'à `api.anthropic.com`, via l'en-tête
`anthropic-dangerous-direct-browser-access`.

Modèles proposés : `claude-sonnet-5` (par défaut) et `claude-haiku-4-5-20251001`.

## Mise à jour

Remplacer les fichiers sous le même nom pour garder l'URL et l'icône stables.
Après modification de `index.html`, incrémenter `CACHE` dans `sw.js`
(`atelier-v1` → `atelier-v2`) pour que les appareils déjà installés reçoivent
la nouvelle version.
