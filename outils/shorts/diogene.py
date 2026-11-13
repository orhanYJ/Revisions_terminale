"""Short « Ôte-toi de mon soleil » (philo, le bonheur) : Diogène le cynique et Alexandre, raconté à la deuxième personne.

Le cours (série « Le bonheur ») : épisode 2, trier ses désirs (Épicure), les tonneaux percés (le désir sans fin) ;
épisode 3, le bonheur « se suffit à lui-même » (Aristote), ce qui dépend de nous et ce qui n'en dépend pas
(les stoïciens, Épictète) ; épisode 6, sujets de bac sur le bonheur. Les cyniques ne sont pas traités dans la série :
le short présente Diogène comme une histoire, puis renvoie honnêtement à la question de bac traitée par la série.
Le site (glossaire de philo) : « les Cyniques (Diogène) étaient une école antique ».

Anecdotes vérifiées sur Diogène Laërce, Vies et doctrines des philosophes illustres, livre VI, « Diogène »
(trad. R. D. Hicks, 1925, Wikisource) et présentées comme rapportées (« on raconte que ») :
- VI, 20 : né à Sinope ; VI, 22-23 : manteau plié (qui lui sert aussi pour dormir), besace, bâton ; il loge dans la
  jarre (le « tonneau », pithos) du Métrôon (à Athènes : on ne dit pas où est la jarre) ;
- VI, 37 : voyant un enfant boire dans ses mains, il jette le gobelet de sa besace : « un enfant m'a battu en simplicité » ;
- VI, 41 : il allume une lampe en plein jour et va disant : « je cherche un homme » ;
- VI, 58 : on lui reproche de manger sur la place publique : « c'est sur la place publique que j'ai eu faim » ;
- VI, 60 : on lui demande ce qu'il a fait pour être appelé « le chien » (kuôn, d'où « cynique ») ;
- VI, 38 : il se chauffe au soleil au Cranéion (Corinthe) ; Alexandre se tient devant lui : « demande-moi ce que tu veux » ;
  « ôte-toi de mon soleil » ; VI, 32 : Alexandre aurait dit « si je n'étais pas Alexandre, je voudrais être Diogène » ;
- VI, 105 : il disait que n'avoir besoin de rien est le propre des dieux, et avoir besoin de peu, celui des hommes
  semblables aux dieux.
Plutarque, Vie d'Alexandre, 14 (trad. Dryden, Livius.org) : après l'assemblée de l'Isthme où les Grecs choisissent
Alexandre comme chef contre la Perse, il va voir Diogène, qui vit à Corinthe, au faubourg du Cranéion, allongé au soleil ;
Diogène se redresse un peu ; Alexandre lui demande s'il désire quelque chose : « écarte-toi un peu de mon soleil » ;
ses compagnons se moquent ; Alexandre : « si je n'étais pas Alexandre, je voudrais être Diogène ».
Écartés : la jarre « à Corinthe » (Diogène Laërce la place au Métrôon d'Athènes), « l'homme le plus puissant du monde »
(en 336-335 av. J.-C., Alexandre est roi de Macédoine et chef des Grecs, pas encore conquérant de la Perse), la fausse
monnaie de Sinope et l'exil, la vente comme esclave, l'historicité de la rencontre (discutée : on dit « on raconte que »).
Aucune information personnelle. La dernière phrase relance la première (boucle).
"""
CODE = "diogene"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Diogène": "Diojène"}
PASSAGES = [
    ("s1", "Alexandre le Grand te propose ce que tu veux. Tu lui réponds : pousse-toi.", 0.4),
    ("s2", "Tu t'appelles Diogène. Tu es philosophe. Et tu n'as presque rien.", 0.2),
    ("s3", "Un manteau, un sac, un bâton. Tu dors dans une jarre, en pleine ville.", 0.25),
    ("s4", "Tu manges sur la place publique. On te le reproche ? C'est là que tu as eu faim.", 0.3),
    ("s5", "Tu vois un enfant boire dans ses mains. Tu jettes ton gobelet : un enfant m'a battu.", 0.3),
    ("s6", "En plein jour, tu allumes une lampe : je cherche un homme.", 0.3),
    ("s7", "On te surnomme le chien. C'est de là que vient le mot cynique.", 0.35),
    ("s8", "On raconte qu'un jour, à Corinthe, tu es allongé au soleil.", 0.2),
    ("s9", "Une ombre s'arrête devant toi : Alexandre, que les Grecs viennent de choisir pour chef.", 0.25),
    ("s10", "Il te dit : demande-moi ce que tu veux.", 0.3),
    ("s11", "De l'or ? Un palais ?", 0.35),
    ("s12", "Tu te redresses un peu. Et tu dis : ôte-toi de mon soleil.", 0.45),
    ("s13", "Ses compagnons rient. Mais Alexandre dit : si je n'étais pas Alexandre, je voudrais être Diogène.", 0.3),
    ("s14", "Diogène disait : n'avoir besoin de rien, c'est divin. De peu, c'est presque divin.", 0.3),
    ("s15", "Le bonheur dépend-il de nous ? C'est un sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s16", "Et toi… Alexandre te propose ce que tu veux. Tu lui demandes quoi ?", 0.0),
]
