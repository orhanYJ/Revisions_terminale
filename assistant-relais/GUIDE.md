# Assistant de révision — mise en service du relais

Les sites SVT, PC et DNL ont un bouton « Poser une question » (en bas à gauche) qui envoie la question à une IA. Il reste invisible tant que l'adresse du relais n'est pas renseignée dans `svt/assistant.js`, `pc/assistant.js` et `dnl/assistant.js` (ligne `var RELAIS = "";`).

Le relais est un **Cloudflare Worker** (`worker.js`, dans ce dossier) qui appelle **Workers AI**, l'IA de Cloudflare. Il n'y a **aucune clé d'API** : le Worker est relié à l'IA dans le tableau de bord, rien de secret n'est stocké dans le dépôt.

- Offre gratuite : 10 000 « neurones » par jour, soit environ 130 questions par jour avec le modèle utilisé (Llama 3.3 70B). Remise à zéro à 00:00 UTC (1 h ou 2 h du matin, heure de Paris).
- Au-delà, Workers AI refuse et le site affiche « L'assistant a atteint sa limite pour aujourd'hui ». Sur l'offre gratuite, **rien ne peut être facturé**.
- Cloudflare n'utilise pas les questions pour entraîner ses modèles.

## Étapes (environ 15 minutes)

Les libellés du tableau de bord Cloudflare changent parfois légèrement ; l'ordre des étapes reste le même.

### 1. Créer le compte Cloudflare

1. Aller sur https://dash.cloudflare.com/sign-up
2. E-mail et mot de passe, puis valider l'e-mail reçu. L'offre gratuite ne demande pas de carte bancaire.

### 2. Créer le Worker

1. Dans le menu de gauche : **Compute (Workers)** → **Workers & Pages** → **Create** (ou **Create application**).
2. Choisir **Start with Hello World!**
3. Nom du Worker : `assistant-revisions` → **Deploy**.
4. Au premier Worker, Cloudflare demande de choisir un sous-domaine `*.workers.dev` : en prendre un simple (par exemple `cengiz`).

### 3. Coller le code du relais

1. Sur la page du Worker : **Edit code**.
2. Tout effacer dans l'éditeur, puis coller le contenu de `worker.js` (ce dossier du dépôt ; sur GitHub, bouton « Copy raw file »).
3. **Deploy**.

### 4. Relier l'IA (obligatoire)

1. Page du Worker → **Settings** → **Bindings** → **Add binding** (ou **+ Add**).
2. Choisir **Workers AI**.
3. Variable name : `AI` (en majuscules, exactement).
4. **Add binding** / **Deploy**.

### 5. Limite par visiteur (recommandé)

Sans cette étape, l'assistant marche, mais une seule personne pourrait épuiser le quota du jour.

1. Menu de gauche : **Storage & databases** → **Workers KV** → **Create** (ou **Create namespace**), nom : `assistant-compteurs`.
2. Page du Worker → **Settings** → **Bindings** → **Add binding** → **KV namespace**.
3. Variable name : `COMPTEURS` ; namespace : `assistant-compteurs` → **Add binding** / **Deploy**.

Effet : 30 questions par heure au plus pour un même visiteur.

### 6. Vérifier

Ouvrir l'adresse du Worker, affichée sur sa page, de la forme :

`https://assistant-revisions.<sous-domaine>.workers.dev`

Le navigateur doit afficher : **Relais de l'assistant : en service.**

### 7. Transmettre l'adresse

Envoyer cette adresse à Claude Code : elle est ajoutée dans les trois `assistant.js`, le bouton apparaît sur les sites, puis la publication suit.

## Réglages (dans `worker.js`)

| Constante | Valeur | Rôle |
|---|---|---|
| `ORIGINES` | `https://orhanyj.github.io` | seuls les sites du dépôt peuvent interroger le relais |
| `MODELE` | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | modèle de Workers AI |
| `MAX_QUESTION` | 1500 | caractères par question |
| `MAX_HISTORIQUE` | 6 | messages précédents gardés pour les questions de suite |
| `MAX_REPONSE` | 900 | longueur maximale d'une réponse (jetons) |
| `PAR_HEURE` | 30 | questions par visiteur et par heure (si `COMPTEURS` est relié) |

Après une modification de `worker.js` dans le dépôt, la recoller dans l'éditeur du Worker (étape 3) : Cloudflare ne lit pas le dépôt.

## Codes renvoyés au site

| Code | Cas | Message affiché |
|---|---|---|
| `quota` | quota gratuit du jour épuisé | limite atteinte, de nouveau disponible demain |
| `limite` | plus de `PAR_HEURE` questions dans l'heure | réessayer dans une heure |
| `occupe` | Workers AI momentanément saturé | réessayer dans quelques secondes |
| `origine`, `requete`, `configuration`, `erreur` | appel refusé ou incident | l'assistant n'a pas pu répondre |
