/* Données du site. Chaque extrait de code est enregistré par C(id, source, options) :
   out = sortie attendue (vérifiée en exécutant le code avec python3), err = dernière ligne d'erreur attendue,
   console = session interactive (vérifiée comme un doctest), deps = extraits à exécuter avant,
   run = false pour un code à compléter. */
var CODE = {};
function C(id, src, o) { o = o || {}; o.src = src; CODE[id] = o; return id; }
var CH = [];
