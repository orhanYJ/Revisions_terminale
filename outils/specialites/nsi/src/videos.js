/* Vidéos des chapitres (lecteur nsi/serie/<code>.html, généré par outils/serie-philo/generer.py depuis
   outils/serie-nsi/<module>.py). Une entrée par chapitre (clé = id du chapitre). L'onglet « vidéo » et le bandeau du
   cours n'apparaissent que si dispo est vrai : passer dispo à true (et donner min, la durée en minutes) une fois la vidéo
   publiée avec sa voix, puis relancer build.py. */
var VIDEOS = {
  ch1: { code: "nsi-ch1", dispo: true, min: 27 }
};
