"""Short « L'anneau de Gygès » (philo, le devoir) : le mythe de Platon raconté à la deuxième personne, comme une histoire vraie.

Le cours (série « Le devoir », épisode 1 « L'anneau de Gygès » et épisode 2 « D'où vient le devoir ? ») : dans La République,
Glaucon, le frère de Platon, raconte l'histoire d'un berger de Lydie qui, après un orage, trouve au fond d'une crevasse
un anneau d'or ; en tournant la pierre de l'anneau vers l'intérieur de sa main, il devient invisible ; il se rend au palais,
séduit la reine, tue le roi et prend le pouvoir. Glaucon en tire sa conclusion : personne n'est juste volontairement ;
donne l'anneau au plus honnête des hommes, il fera comme Gygès ; nous ne respectons nos devoirs que par peur d'être pris.
« Toute La République est une réponse à Glaucon » (devoir_1.py). Sujet de la série : « Serions-nous honnêtes sans témoin ? ».

Déroulé du mythe vérifié sur la traduction de B. Jowett (Platon, République, II, 359c-360d, Project Gutenberg n° 1497) :
berger au service du roi de Lydie ; grand orage, tremblement de terre qui ouvre la terre là où il fait paître son troupeau ;
il descend dans l'ouverture ; un cheval de bronze creux, « ayant des portes » ; à l'intérieur, un mort d'une taille
« plus qu'humaine », qui ne porte rien qu'un anneau d'or ; il le prend et remonte ; à l'assemblée mensuelle des bergers
(rapport au roi sur les troupeaux), il tourne le chaton de l'anneau vers l'intérieur de sa main : il devient invisible et
les autres parlent de lui comme s'il était parti ; il le retourne vers l'extérieur : il réapparaît ; il refait l'essai,
toujours le même résultat ; il se fait choisir parmi les messagers envoyés à la cour, séduit la reine, avec son aide
conspire contre le roi, le tue et prend le royaume. Glaucon : avec deux anneaux, l'un au juste, l'autre à l'injuste,
personne ne resterait juste ; preuve qu'on n'est pas juste volontairement mais par nécessité.
Écartés : le nom exact du berger (le texte grec dit « l'ancêtre de Gygès le Lydien », Jowett corrige en « l'ancêtre de
Crésus » : on dit « l'anneau de Gygès », nom consacré de l'histoire, sans nommer le berger) ; les exemples de Glaucon
(voler au marché, tuer qui l'on veut) ; la datation précise de la République (on dit « il y a 2 400 ans », vers 375 av. J.-C.).
Aucune information personnelle. La dernière phrase relance la première (boucle).
"""
CODE = "gyges"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Gygès": "Jijèsse", "Glaucon": "Glôkon", "2400": "deux mille quatre cents"}
PASSAGES = [
    ("s1", "Si personne ne pouvait jamais te voir… tu resterais honnête ?", 0.35),
    ("s2", "Il y a 2400 ans, Platon raconte cette histoire.", 0.2),
    ("s3", "Tu es berger, en Lydie. Tu gardes les moutons du roi.", 0.15),
    ("s4", "Un orage éclate. La terre tremble. Le sol s'ouvre devant toi.", 0.25),
    ("s5", "Tu descends. Au fond, un cheval de bronze, creux, avec des portes.", 0.2),
    ("s6", "Tu regardes à l'intérieur. Un mort. Plus grand qu'un homme.", 0.25),
    ("s7", "Il ne porte qu'une chose : un anneau d'or. Tu le prends.", 0.3),
    ("s8", "Plus tard, assis parmi les bergers, tu tournes le chaton de l'anneau vers ta paume.", 0.2),
    ("s9", "Et les autres parlent de toi… comme si tu étais parti.", 0.35),
    ("s10", "Invisible. Tu le retournes : tu réapparais. Ça marche à chaque fois.", 0.3),
    ("s11", "Alors tu files au palais. Tu séduis la reine. Avec elle, tu tues le roi. Tu prends le pouvoir.", 0.35),
    ("s12", "C'est l'anneau de Gygès.", 0.3),
    ("s13", "Glaucon, le frère de Platon, conclut : donne cet anneau au plus juste des hommes… il fera pareil.", 0.25),
    ("s14", "Personne n'est juste volontairement. On est juste par peur d'être pris.", 0.35),
    ("s15", "Platon passera toute la République à lui répondre.", 0.25),
    ("s16", "Ne fait-on son devoir que par peur d'être puni ? C'est un sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Alors toi… avec l'anneau au doigt, tu resterais honnête ?", 0.0),
]
