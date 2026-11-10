# HGGSP « Ligne rouge » — consignes pour les renforts

Le site `hggsp/index.html` est **généré** : ne le modifie jamais à la main.

```
python3 outils/specialites/hggsp/build.py              # régénère les cartes puis la page
python3 outils/specialites/hggsp/build.py --sans-cartes # plus rapide si tu n'as pas touché aux cartes
cd hggsp && python3 -m http.server 8834                # renfort : port 8834 (le responsable a 8833)
```

## Qui écrit quoi

| Fichier | Auteur |
|---|---|
| `src/data-t3.js`, `src/data-t4.js` (+ `cartes-t3.js`, `cartes-t4.js` si besoin) | renfort thèmes 3 et 4 |
| `src/data-t6.js` (+ `cartes-t6.js` si besoin) | renfort thème 6 |
| `src/data-t5.js`, et tout le reste (`app.js`, `style.css`, `shell.html`, `data-commun.js`, `data-t1.js`, `data-t2.js`, `data-dossiers.js`, `cartes.js`, `build.py`) | responsable |

`build.py` inclut **automatiquement** tout fichier `src/data-*.js` (après `data-commun.js`) et `cartes.js` charge
tout module `cartes-*.js` du dossier : **tu n'as aucun fichier partagé à modifier**. Si tu as besoin d'un nouveau
type de bloc dans le moteur, écris-le dans ton compte rendu au lieu de toucher à `app.js`.

## Ton fichier de données (`src/data-tN.js`)

Modèles complets à lire d'abord : `src/data-t2.js` (chapitres) et `src/data-dossiers.js` (dossier de thème).
Le programme officiel (intitulés et jalons mot pour mot) est déjà dans `THEMES` (`src/data-commun.js`).

```js
/* 1. Déclarer le thème rédigé : les 4 identifiants de chapitre, dans l'ordre intro, axe 1, axe 2, objet conclusif */
rediger("t3", { pb: "Problématique d'ensemble du thème ?", chs: ["t3-intro", "t3-a1", "t3-a2", "t3-otc"] });

/* 2. Un chapitre par identifiant */
CHAPS["t3-a1"] = {
  th: "t3", code: "T3 · AXE 1", t: "Titre du chapitre (intitulé du programme)",
  ess: ["5 phrases : l'essentiel en 5 lignes"],
  att: ["Ce que le programme attend, reformulé (3 à 5 lignes)"],
  secs: [                                   /* 2 à 4 sections */
    { t: "Titre de la section",
      idees: [                              /* chaque idée : une explication + un exemple daté et chiffré */
        { t: "Titre de l'idée", h: "Explication (HTML simple : <b>, <em>)", ex: "Exemple précis, daté, sourcé" }
      ],
      plis: [{ t: "Document ou activité (panneau replié)", h: "<p>…</p>" }],   /* facultatif */
      viz: "carte:nom" }                    /* facultatif : "carte:nom", "anim:nom", ou un tableau ["carte:x", "anim:y"] */
  ],
  pieges: ["Erreur fréquente…"],
  retenir: [["Rubrique", "Contenu de la fiche imprimable"]],
  qcm: [                                    /* 12 à 15 questions */
    { q: "Question ?", o: ["A", "B", "C", "D"], r: 1, e: "Explication de la bonne réponse.", ref: "2-3" }
  ],                                        /* r = indice de la bonne option ; ref = "section-idée" (de 1), renvoi « Revoir le paragraphe » */
  fc: [["Recto (notion, date)", "Verso (définition)"]],   /* 12 cartes environ */
  bac: { s: "Sujet de dissertation", type: "Sujet inventé pour le site (thème 3, axe 1)", h: "<p><b>Problématique possible :</b> …</p><p><b>I. …</b> …</p>" }
};

/* 3. Le dossier du thème (onglets Plan et notions, Frise, Cartes, Débats, Sujets corrigés) */
DOSSIERS.t3 = {
  cats: { histoire: ["Histoire", "#2D5675"], justice: ["Justice", "#B3241B"] },   /* catégories de la frise : libellé, couleur */
  frise: [["1945", "20 nov. 1945", "justice", "Titre court", "Une phrase d'explication."]],   /* 25 à 35 dates exactes */
  notions: [["Notion", "Définition"]],
  acteurs: [["Acteurs", "Qui, avec exemples"]],
  cartes: ["nom"],                          /* noms de cartes de CARTES (facultatif, [] sinon) */
  debats: [{ q: "Question ?", pour: ["…"], contre: ["…"], bilan: "…" }],   /* 3 débats */
  dissert: { s: "Sujet", src: "Sujet inventé pour le site. Corrigé proposé par le site.", analyse: "…", pb: "…", intro: "…",
             plan: [{ t: "I. …", sous: [["A. …", "contenu avec exemples"]] }], concl: "…", croquis: "…" },
  etude: { titre: "…", src: "Étude critique inventée pour le site.", doc: { ref: "Auteur, nature, date (domaine public ou citation courte)", txt: ["paragraphe", "…"] },
           consigne: "…", intro: "…", parts: [["1. …", "…"]], concl: "…", critique: "Regard critique : …" },
  autres: [["Autre sujet", "Piste de plan"]]
};
```

Règles d'écriture : chaînes JavaScript entre guillemets doubles, apostrophes droites `'` dans le texte, jamais de
guillemet double à l'intérieur (utilise « » avec une espace de chaque côté : la page pose elle-même les espaces
fines). Tutoiement, niveau bac, chaque idée avec un exemple **daté et chiffré, source citée**. Ce qui dépasse le
programme est marqué « (hors programme) » ou « Pour aller plus loin ». Aucun nom de professeur, d'élève,
d'établissement. Textes protégés : citation courte seulement ; les textes du domaine public peuvent être cités
plus largement avec leur référence. Tout ce qui date d'après 2024 doit être vérifié par une recherche et daté.

## Animation explicative (au moins une par chapitre) : `ANIMS.nom`

Le moteur joue une scène SVG **pas à pas** (lecture / pause / étape précédente / suivante, date en télétype,
légende qui change à chaque étape). Tu fournis la scène et les étapes ; chaque élément de la scène qui doit
apparaître, disparaître ou être mis en valeur porte un attribut `data-k="identifiant"`.

```js
ANIMS.gacaca = {
  titre: "Titre de l'animation",
  scene: { w: 640, h: 360, svg: "<g data-k='a'>…</g><path data-k='fleche' class='trace' d='M…'/>…" },
  /* ou scene: "carte:nom" pour une scène de carte générée (voir plus bas) */
  etapes: [
    { date: "1994", titre: "Titre de l'étape", texte: "Ce qui se passe, en une ou deux phrases.", montre: ["a"], cache: [], accent: ["a"] },
    { date: "2001", titre: "…", texte: "…", montre: ["fleche"], cache: ["a"] }
  ],
  source: "Sources des données (facultatif)"
};
```

- L'état de l'étape k est cumulé : sont visibles les éléments montrés aux étapes 1 à k, moins ceux cachés depuis.
  Un élément sans `data-k` est toujours visible (fond). `accent` fait pulser des éléments pendant l'étape.
- Classes utiles dans la scène : `trace` (un trait qui se dessine quand il apparaît ; ajoute `pathLength="1"`),
  `zone` (aplat rouge translucide), `fleche` (trait rouge avec pointe), `lbl` (étiquette lisible sur la carte),
  `lbl-f` (étiquette forte). Couleurs : utilise les variables `var(--rouge)`, `var(--acier)`, `var(--encre)`,
  `var(--encre2)`, `var(--ok)`, `var(--kraft-f)` pour suivre le mode sombre ; guillemets simples dans le SVG.
- Montre un **phénomène** (une évolution, un mécanisme, une chronologie spatialisée), pas un dessin qui se trace.
- Pour la placer dans un chapitre : `viz: "anim:gacaca"` dans une section.

### Scène sur un fond de carte : module `cartes-tN.js`

```js
module.exports = function (ctx) {
  /* ctx.M : outils du fond du monde (projection Equal Earth, ctx.WM × ctx.HM) ;
     ctx.cadre(projection, largeur, hauteur, tolérance, aireMin) : outils d'une carte régionale ;
     outils : P([lon, lat]) → [x, y], pays(filtre) → chemin, ligne(coords, attrs), poly(anneau, attrs), txt([lon, lat], texte, {a, dx, dy, cl}) */
  const M = ctx.M, [x, y] = M.P([2.35, 48.86]);
  ctx.OUT.anims.nom = { w: ctx.WM, h: ctx.HM, vb: [400, 40, 300, 200], fond: "monde",
    calques: "<g data-k='paris'><circle cx='" + x + "' cy='" + y + "' r='6' class='pt-a'/>" + M.txt([2.35, 48.86], "Paris", { cl: "lbl", dx: 8 }) + "</g>" };
  /* carte interactive à points (comme celles de data-dossiers.js) : ctx.OUT.cartes.nom = { w, h, fond, deco, pts, meta } — voir cartes.js */
};
```

`fond: "monde"` réutilise le fond mondial ; pour une carte régionale, construis le fond avec `ctx.cadre` comme
les cartes `chine` et `mo` de `cartes.js`. `vb` (facultatif) recadre la scène. Ensuite `scene: "carte:nom"`.

## Avant de rendre

1. `python3 outils/specialites/hggsp/build.py` sans erreur (il fait `node --check` de chaque fichier de données).
2. Ouvre tes routes (`#t3`, `#t3-intro`, `#t3:frise`…) en téléphone 390 × 844 et ordinateur, clair et sombre :
   aucune erreur console, pas de défilement horizontal ; QCM, cartes mémoire et animations testés au clic.
3. Relis tes faits. Compte rendu : fichiers, chapitres, animations, points incertains.
4. `git add` de **tes seuls fichiers** (jamais `-A`), commit en français avec les deux lignes de fin du cahier.
   Ne commite pas `hggsp/index.html` (le responsable régénère et commite la page après intégration).
