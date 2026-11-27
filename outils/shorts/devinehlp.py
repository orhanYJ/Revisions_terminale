"""Short « HLP : devine l'auteur en 3 indices » (format `devine`, le spectateur joue ; habillage « alerte »).

Trois manches, une par partie du premier semestre de la spécialité HLP de Terminale (« La recherche de soi » :
éducation, transmission et émancipation ; les expressions de la sensibilité ; les métamorphoses du moi). Trois indices
du plus dur au plus facile, un portrait pixellisé qui se précise, puis la révélation.
Matière sans cours sur la chaîne : faits vérifiés le 27/11/2026. Rousseau et Freud sont expliqués dans les séries philo
de la chaîne (« La liberté », épisode 5 ; « La conscience », épisode 3) : la fin le dit, sans plus.
- Rousseau (1712 – 1778) : ses cinq enfants (avec Thérèse Levasseur) déposés aux Enfants-Trouvés, ce qu'il avoue dans les
  Confessions (livres VIII et IX) ; Émile ou De l'éducation, 1762 (Stanford Encyclopedia of Philosophy, « Jean Jacques
  Rousseau ») ; « L'homme est né libre, et partout il est dans les fers » : Du contrat social, I, 1, 1762 (série « La
  liberté », épisode 5, vérifié sur Wikisource).
- Proust (1871 – 1922) : chambre tapissée de liège au 102, boulevard Haussmann (1910), où il écrit la nuit (Open Culture,
  « The Cork-Lined Bedroom » ; Wikipedia, boulevard Haussmann) ; prix Goncourt le 10 décembre 1919 pour À l'ombre des
  jeunes filles en fleurs (ministère de la Culture ; OpenEdition, « Proust et le prix Goncourt ») ; la madeleine trempée
  dans le thé et le souvenir qui revient : Du côté de chez Swann (1913), « Combray » : la mémoire involontaire.
- Freud (1856 – 1939) : quitte Vienne le 4 juin 1938, après l'Anschluss, pour Londres, où il meurt le 23 septembre 1939
  (Freud Museum London) ; le rêve, « voie royale » vers l'inconscient, L'Interprétation du rêve (1900) ; « le moi n'est
  pas maître dans sa propre maison » (Une difficulté de la psychanalyse, 1917) : série « La conscience », épisode 3.
Écartés : « Je forme une entreprise qui n'eut jamais d'exemple » (Confessions : trop long pour un indice) ; le nombre
exact de volumes de la Recherche et leurs dates (sept, de 1913 à 1927, en partie posthumes : trop de détails) ; les
causes de la mort de Freud (sources divergentes) ; Primo Levi (aucun portrait libre de droits sûr).
"""
CODE = "devinehlp"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "5": "cinq", "HLP": "ache-èle-pé",
                 "1762": "dix-sept cent soixante-deux", "1919": "mille neuf cent dix-neuf",
                 "1938": "mille neuf cent trente-huit", "Goncourt": "Gonnecour"}
PASSAGES = [
    ("d1", "HLP : devine l'auteur en 3 indices.", 0.2),
    ("d2", "Du plus dur au plus facile. Trouve avant la fin du compte !", 0.25),
    ("a1", "Manche 1 : l'éducation. Indice 1 : il abandonne ses 5 enfants.", 0.25),
    ("a2", "Indice 2 : il écrit pourtant un traité d'éducation.", 0.25),
    ("a3", "Indice 3 : « L'homme est né libre, et partout il est dans les fers. » Trois, deux, un.", 1.15),
    ("c1", "C'est Rousseau ! L'Émile, 1762. Et dans ses Confessions, il avoue tout.", 0.3),
    ("b1", "Manche 2 : la sensibilité. Indice 1 : il écrit la nuit, dans une chambre tapissée de liège.", 0.25),
    ("b2", "Indice 2 : prix Goncourt en 1919.", 0.25),
    ("b3", "Indice 3 : une madeleine trempée dans le thé. Trois, deux, un.", 1.15),
    ("c2", "C'est Marcel Proust ! À la recherche du temps perdu. Un goût, et tout le passé revient : "
           "la mémoire involontaire.", 0.3),
    ("e1", "Dernière manche : les métamorphoses du moi. Indice 1 : en 1938, il fuit les nazis pour Londres.", 0.25),
    ("e2", "Indice 2 : pour lui, le rêve est la voie royale vers l'inconscient.", 0.25),
    ("e3", "Indice 3 : il invente la psychanalyse. Trois, deux, un.", 1.15),
    ("c3", "C'est Sigmund Freud ! Le moi n'est pas maître dans sa propre maison.", 0.3),
    ("o1", "Combien tu en as trouvé ? Dis-le en commentaire.", 0.2),
    ("o2", "Rousseau et Freud sont expliqués dans les séries philo de Révisions Animées.", 0.2),
    ("o3", "Et le prochain auteur… tu le trouves en combien d'indices ?", 0.0),
]
