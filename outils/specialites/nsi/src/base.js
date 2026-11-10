/* Données du site. Chaque extrait de code est enregistré par C(id, source, options) :
   out = sortie attendue (vérifiée en exécutant le code avec python3), err = dernière ligne d'erreur attendue,
   console = session interactive (vérifiée comme un doctest), deps = extraits à exécuter avant,
   run = false pour un code à compléter. */
var CODE = {};
function C(id, src, o) { o = o || {}; o.src = src; CODE[id] = o; return id; }
var CH = [];
/* Animations propres à un chapitre : WIDGETS_EXT["nom"] = function (zone, option, outils) { … }.
   Dans le texte du chapitre : [[w-nom]] ou [[w-nom|option]]. outils.lecteur(zone, {…}) fournit le lecteur commun
   (lecture, pause, étape précédente / suivante, légende par étape) : voir sa description dans app.js.
   Code SQL : C(id, requête, { sql: true, deps: [id du schéma], out: "col1 | col2\nval | val" }). */
var WIDGETS_EXT = {};
