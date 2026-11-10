/* ===== Vidéos des chapitres (chaîne outils/serie-philo/generer.py, scripts outils/serie-hggsp/) =====
   VIDEOS["t1-intro"] = { code, min, dispo } : la page du chapitre affiche le bandeau « ▶ Vidéo du chapitre » quand
   dispo est vrai (vidéo publiée avec sa voix) ; avant, il reste masqué (visible pour un test avec ?video dans l'adresse).
   Le lecteur hggsp/serie/<code>.html?embed=1 est monté en iframe au premier clic (hauteur reçue par le message serie-h). */
var VIDEOS = {
  "t1-intro": { code: "hggsp-t1-intro", min: 21, dispo: false }
};
