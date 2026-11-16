"""Short « Devine le philosophe en 3 indices » (format `devine`, le spectateur joue ; habillage « dossier secret »).

Trois manches, trois indices chacune, du plus difficile au plus facile, puis la révélation (dates et idée clé).
Faits tirés uniquement des séries philo de la chaîne (outils/serie-philo) :
- Socrate (v. 470 – 399 av. J.-C.) : conscience_5.py, scène « socrate » : « une voix qui ne se fait entendre que pour me
  détourner » (Platon, Apologie de Socrate, 31c-d), « Elle dit seulement : arrête » ; « connais-toi toi-même »,
  inscription de Delphes « que Socrate avait faite sienne » ; « Athènes, 399 avant notre ère […] comparaît devant ses
  juges », condamné à mort (etat_5.py, liberte_5.py) ; « Une vie sans examen n'est pas une vie » (Apologie, 38a).
- Spinoza (1632 – 1677) : liberte_3.py, scène « spinoza » : « À vingt-trois ans, il est chassé de sa communauté pour ses
  idées. Il vivra modestement, en polissant des verres de lunettes » ; etat_3.py : Amsterdam, 1656 ; la pierre lancée
  qui, si elle pouvait penser, se croirait libre (lettre 58 à Schuller, 1674) ; « conscients de leurs désirs et ignorants
  des causes qui les déterminent ».
- Kant (1724 – 1804) : devoir_3.py : « un professeur de Königsberg » (1785) ; scène « mensonge » : l'ami caché,
  l'assassin à la porte, Kant refuse tout droit de mentir (Sur un prétendu droit de mentir par humanité, 1797) ; scène de
  l'impératif catégorique : « Agis uniquement d'après la maxime qui fait que tu peux vouloir en même temps qu'elle devienne
  une loi universelle » (Fondements de la métaphysique des mœurs, 1785).
Écartés : « Socrate n'a rien écrit » et « la ciguë » (vrais, mais absents des séries) ; « Kant n'a jamais quitté
Königsberg » (formule courante mais approximative) ; la promenade quotidienne de Kant réglée comme une horloge
(anecdote non vérifiée dans les séries).
"""
CODE = "devinephilo"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"1": "un", "2": "deux", "3": "trois", "23": "vingt-trois",
                 "399": "trois cent quatre-vingt-dix-neuf", "Königsberg": "Keunigsberg"}
SUSPENSE = 1.2       # silence après le dernier indice : on devine avant la révélation
PASSAGES = [
    ("h1", "Devine le philosophe en 3 indices.", 0.1),
    ("h2", "Le plus dur d'abord. Trouve-le le plus tôt possible !", 0.15),
    ("a1", "Dossier 1. Accès autorisé. Premier indice : une voix intérieure lui dit seulement « arrête ». "
           "Deuxième indice : sa devise, « connais-toi toi-même ».", 0.1),
    ("b1", "Dernier indice : en 399 avant notre ère, Athènes le condamne à mort.", SUSPENSE),
    ("c1", "C'est Socrate ! Pour lui, une vie sans examen n'est pas une vie.", 0.2),
    ("a2", "Dossier 2. Accès autorisé. Premier indice : il gagne sa vie en polissant des verres de lunettes. "
           "Deuxième indice : à 23 ans, sa communauté d'Amsterdam le chasse pour ses idées.", 0.1),
    ("b2", "Dernier indice : une pierre lancée, si elle pensait, se croirait libre.", SUSPENSE),
    ("c2", "C'est Spinoza ! On se croit libre… parce qu'on ignore les causes.", 0.2),
    ("a3", "Dossier 3, le dernier. Accès autorisé. Premier indice : il enseigne à Königsberg. "
           "Deuxième indice : même face à un assassin, il interdit de mentir.", 0.1),
    ("b3", "Dernier indice : il invente l'impératif catégorique.", SUSPENSE),
    ("c3", "C'est Kant ! Agis selon une règle qui pourrait devenir une loi universelle.", 0.2),
    ("o1", "Combien tu en as trouvé ? Dis-le en commentaire.", 0.15),
    ("o2", "Les 3 sont expliqués dans les séries philo de Révisions Animées.", 0.15),
    ("o3", "Et le prochain dossier… tu le trouves en combien d'indices ?", 0.0),
]
