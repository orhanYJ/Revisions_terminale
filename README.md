# Revisions_terminale

## Couche de mouvement

Sur les sites animés, le mouvement est maintenu à part du contenu, dans deux fichiers propres à chaque site : `motion.css` et `motion.js`. Ils sont chargés par un bloc repéré, placé juste avant `</head>` dans `index.html` :

```html
<!-- mouvement:debut — couche maintenue à part (motion.css, motion.js) ; à conserver lors des mises à jour -->
<link rel="stylesheet" href="motion.css?v=N">
<script src="motion.js?v=N" defer></script>
<!-- mouvement:fin -->
```

- Quand un `index.html` régénéré remplace l'ancien, réinsérer ce bloc s'il n'y est plus.
- Quand `motion.css` ou `motion.js` change, incrémenter `?v=N` : les service workers servent ces fichiers en cache d'abord. Incrémenter aussi le numéro de cache du `sw.js`.
- Tout ce qui bouge est rangé sous `html.mo`, classe posée seulement si l'appareil n'a pas demandé à réduire les animations. Rien n'est jamais caché en attendant une animation.
- PC et SVT portent en plus une première couche directement dans leur `index.html` ; leurs fichiers `motion.*` la complètent.
- Les trois sites ACL écrit (`acl-ecrit`, `acl-bricklane`, `acl-lughnasa`) partagent les mêmes `motion.css` et `motion.js` : seule la ligne `var MOTIF = …` du script change d'un site à l'autre.

Dernière vérification : 19/09/2026
