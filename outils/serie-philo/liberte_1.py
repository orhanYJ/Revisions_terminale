"""La liberté, épisode 1 : « Qu'est-ce qu'être libre ? »

Texte lu (beats) et visuels de chaque scène. Le générateur (generer.py) enregistre la voix,
cale chaque visuel sur le mot où il apparaît et écrit philo/serie/liberte-1.data.js.

Beats : une chaîne = la voix du narrateur ; ("C", texte, id) = citation lue par la seconde voix,
affichée par le visuel id (les mots s'allument au fil de la lecture) ; ("P", s) = silence ;
(texte, {"rate": "-6%", "pitch": "-2Hz"}) = narrateur avec une intonation particulière.
Repères dans le texte : {id} fait apparaître un visuel, {-id} le retire, {id.k} déclenche l'étape k.
"""

CODE = "liberte-1"
NOTION = "La liberté"
NUM = 1
TITRE = "Qu'est-ce qu'être libre ?"
SUIVANT = "Épisode 2 · Le libre arbitre : Descartes et Sartre"

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", carton=False, beats=[
        "{ico}Une question, pour commencer. Ce matin, {ico.1}qui a choisi tes habits ?",
        ("Toi, évidemment.", {"rate": "-4%"}),
        "Et la musique dans tes écouteurs ? {ico.2}Toi aussi.",
        "Et le moment où tu as ouvert ton téléphone… {ico.3}sans même y penser ?",
        ("Là, déjà… c'est moins sûr.", {"rate": "-8%", "pitch": "-2Hz"}),
        ("P", 0.6),
        "{-ico}{q1}Nous passons nos journées à nous dire libres. Libres de sortir, libres de penser, libres de dire non. "
        "Et pourtant, dès qu'on essaie de dire ce que c'est, être libre… le mot nous file entre les doigts.",
        "{-q1}{noms}Cette série va prendre ce mot, que tout le monde emploie, et le regarder de très près. "
        "Avec ceux qui y ont consacré leur vie : {noms.1}Platon, {noms.2}Descartes, {noms.3}Spinoza, "
        "{noms.4}Rousseau, {noms.5}Kant, {noms.6}Sartre… et quelques autres.",
        "{-noms}{serie}Six épisodes, et un récapitulatif. Celui-ci est le premier. "
        "Car avant de savoir si nous sommes libres… {-serie}il faut savoir de quoi l'on parle.",
        ("P", 0.3),
        "{titre}",
        ("P", 3.2),
    ], vis={
        "ico": dict(type="illu", nom="icones", x=190, y=170, w=900, h=360),
        "q1": dict(type="question", t="Être libre… mais de quoi parle-t-on ?"),
        "noms": dict(type="nuage", items=["Platon", "Descartes", "Spinoza", "Rousseau", "Kant", "Sartre"]),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="une notion, regardée sous tous ses angles", y=270),
        "titre": dict(type="titre", sur="La liberté · Épisode 1", t="Qu'est-ce qu'être libre ?",
                      sous="Le mot, les trois libertés, les repères"),
    }),

    # ------------------------------------------------------------------ I. le mot
    dict(id="mot", chap="Le mot", fond="aube", beats=[
        "Remontons d'abord le temps. {agora}Athènes, cinq siècles avant notre ère. "
        "Sur l'agora, la grande place de la cité, deux hommes se croisent.",
        "{agora.1}L'un est citoyen : il vote, il prend la parole à l'assemblée, il décide des lois. "
        "L'autre porte la même tunique, mange le même pain… {agora.2}mais il appartient à quelqu'un. C'est un esclave.",
        ("Alors, qu'est-ce qui les sépare ?", {"pitch": "+2Hz"}),
        ("Pas la force. Pas l'intelligence. Une seule chose : {agora.3}le premier s'appartient à lui-même. "
         "Le second appartient à un autre.", {"rate": "-5%"}),
        "C'est le sens le plus ancien du mot. En grec, l'homme libre se dit {-agora}{grec}éleuthéros. "
        "En latin, {lat}liber.",
        "Et ces deux mots viendraient d'une même racine, très ancienne, {-grec}{-lat}{racine}qui désignait… {racine.1}le peuple. "
        "Être libre, à l'origine, c'est faire partie des siens, {racine.2}par opposition à l'étranger capturé, réduit en esclavage. "
        "On retrouve d'ailleurs cette racine dans un mot allemand, {racine.3}« Loïte », qui veut dire : les gens.",
        "{-racine}{liberi}Mieux encore : en latin, libéri, au pluriel, veut dire… les enfants. "
        "Les enfants libres de la maison, par opposition aux esclaves qui y servent.",
        "{-liberi}{arist}Au quatrième siècle avant notre ère, Aristote en tire une définition "
        "qui va traverser toute l'histoire de la philosophie.",
        ("C", "Nous appelons homme libre celui qui est à lui-même sa fin et n'existe pas pour un autre.", "c_arist"),
        "{-arist}{-c_arist}{def1}Retiens bien cette idée. Être libre, c'est ne pas être un instrument. "
        "L'esclave est un moyen au service des fins d'un autre ; {def1.1}l'homme libre poursuit ses propres fins.",
        "{-def1}{note}Attention, pourtant. Aristote lui-même jugeait l'esclavage naturel : il appelait l'esclave "
        "« une propriété animée ». La définition est belle, mais son époque la réservait à quelques-uns.",
        "{note.1}Toute l'histoire de la liberté sera aussi l'histoire de son extension. "
        "{kant}Deux mille ans plus tard, Kant exigera que toute personne soit traitée comme une fin, "
        "et jamais simplement comme un moyen.",
        ("Tu vois le fil ?", {"pitch": "+3Hz"}),
    ], vis={
        "agora": dict(type="illu", nom="agora", x=140, y=110, w=1000, h=470),
        "grec": dict(type="mot", t="ἐλεύθερος", g="éleuthéros · grec : l'homme libre", y=150, taille=92),
        "lat": dict(type="mot", t="LIBER", g="latin : l'homme libre, qui n'est pas esclave", y=380, taille=104),
        "racine": dict(type="illu", nom="racine", x=140, y=100, w=1000, h=500, plus=True),
        "liberi": dict(type="mot", t="liberi", g="en latin : « les enfants » (nés libres)", y=250, taille=110),
        "arist": dict(type="portrait", img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      x=110, y=120, w=330, h=420),
        "c_arist": dict(type="cit", a="Aristote", o="Métaphysique, livre A, 2", x=500, y=170, w=680),
        "def1": dict(type="def", terme="Être libre · le sens premier",
                     t="Ne pas appartenir à un autre : être à soi-même sa propre fin, et non l'instrument d'un autre.",
                     etape="Esclave → moyen pour les fins d'un autre   ·   Homme libre → poursuit ses propres fins",
                     x=170, y=190, w=940),
        "note": dict(type="note", titre="Attention",
                     t="Aristote juge l'esclavage naturel : l'esclave serait « une propriété animée » (Politique, I, 4).",
                     etape="L'histoire de la liberté est aussi celle de son extension à tous.",
                     x=170, y=130, w=940),
        "kant": dict(type="tag", style="lien", t="Kant (1785) : toute personne est une fin, jamais un simple moyen",
                     x=170, y=520, w=940),
    }),

    # ------------------------------------------------------------------ II. faire ce que je veux
    dict(id="faire", chap="Faire ce que je veux ?", fond="nuit", beats=[
        "{q_quoi}Revenons à aujourd'hui. Si je te demande : être libre, c'est quoi ? "
        "Tu vas sans doute répondre : {-q_quoi}{fcqjv}c'est faire ce que je veux. Personne ne m'empêche, personne ne m'oblige.",
        "{-fcqjv}{hobbes}C'est la définition du sens commun. Et elle a un défenseur de poids : Thomas Hobbes, "
        "philosophe anglais du dix-septième siècle.",
        ("C", "La liberté signifie, au sens propre, l'absence d'opposition ; par opposition, j'entends les obstacles "
              "extérieurs au mouvement.", "c_hobbes"),
        "{-hobbes}{-c_hobbes}{vase}Hobbes prend un exemple tout simple : l'eau. Retenue dans un vase, "
        "elle ne peut pas se répandre : elle n'est pas libre. {vase.1}Ôtez l'obstacle… et elle s'écoule.",
        ("Être libre, c'est cela : ne rencontrer aucun obstacle.", {"rate": "-5%"}),
        "{-vase}{def_neg}Cette définition a un grand mérite : elle est claire, et elle se mesure. "
        "Plus il y a d'obstacles, moins je suis libre. On parle parfois de liberté négative : "
        "{def_neg.1}la liberté comme absence. Absence de murs, de chaînes, d'interdits.",
        ("Mais regarde de plus près. Elle pose deux problèmes.", {"pitch": "-2Hz"}),
        "{-def_neg}{pbs}{pbs.1}Premier problème : des obstacles, il y en a toujours. Je ne peux pas voler comme un oiseau, "
        "je ne peux pas être à deux endroits à la fois, je ne peux pas vivre sans manger. "
        "Si être libre, c'est n'être empêché par rien… alors personne n'est jamais libre. "
        "{rep_abs}Ainsi définie, la liberté est toujours relative, jamais absolue.",
        "{pbs.2}Second problème, plus profond : cette définition ne regarde que ce qui se passe dehors, "
        "entre moi et le monde. Elle ne demande jamais ce qui se passe dedans.",
        ("D'où vient… ce que je veux ?", {"rate": "-10%", "pitch": "-1Hz"}),
        "{-pbs}{-rep_abs}{platon}Platon a mis ce problème en scène dans un dialogue célèbre, {gorg}le Gorgias. "
        "Socrate y affronte un jeune homme brillant et arrogant : Calliclès. "
        "Pour Calliclès, l'homme vraiment libre, c'est celui qui a le courage de ses désirs.",
        "{-platon}{-gorg}",
        ("C", "Pour bien vivre, il faut laisser ses passions devenir aussi grandes que possible, au lieu de les réprimer.",
         "c_call"),
        "Satisfaire tous ses désirs, sans entraves : voilà, pour lui, la liberté, et le bonheur. "
        "{-c_call}{tonneaux}Socrate lui répond par une image. Imagine deux hommes, chacun avec ses tonneaux.",
        "{tonneaux.1}Les tonneaux du premier sont sains : une fois remplis, il est tranquille. "
        "{tonneaux.2}Ceux du second sont percés. Il a beau verser, verser encore… ils se vident sans cesse. "
        "{tonneaux.3}Il passe sa vie à les remplir, sans jamais pouvoir s'arrêter.",
        ("Celui qui suit tous ses désirs n'est pas libre : il est l'esclave d'un tonneau qui fuit. "
         "Car un désir satisfait en appelle aussitôt un autre.", {"rate": "-4%"}),
        "{-tonneaux}{tel}Ce tonneau, tu le connais. C'est la vidéo suivante qui se lance toute seule, "
        "{tel.1}le fil qu'on fait défiler sans fin, {tel.2}la notification à laquelle on répond sans y penser.",
        ("Je fais ce que je veux… mais est-ce bien moi qui veux ?", {"rate": "-6%", "pitch": "+1Hz"}),
        "{-tel}{rousseau}Vingt siècles après Platon, Jean-Jacques Rousseau résume tout cela en une phrase. "
        "Une phrase à apprendre par cœur.",
        ("C", "L'impulsion du seul appétit est esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.",
         "c_rous"),
        "{-rousseau}{-c_rous}{cols1}Retiens la leçon. Faire ce que je veux, ce n'est pas forcément vouloir librement. "
        "Il y a deux questions, et non une seule. {cols1.g}Est-ce que je peux faire ce que je veux ? "
        "{cols1.d}Et est-ce que je veux librement… ce que je veux ?",
        ("P", 0.8),
    ], vis={
        "q_quoi": dict(type="question", t="Être libre, c'est quoi ?"),
        "fcqjv": dict(type="mot", t="« Faire ce que je veux »", g="la définition du sens commun", y=260, taille=78),
        "hobbes": dict(type="portrait", img="hobbes", nom="Thomas Hobbes", dates="1588 – 1679",
                       x=110, y=120, w=330, h=420),
        "c_hobbes": dict(type="cit", a="Hobbes", o="Léviathan, chap. XXI (1651)", x=500, y=150, w=680),
        "vase": dict(type="illu", nom="vase", x=240, y=110, w=800, h=480),
        "def_neg": dict(type="def", terme="La liberté « négative »",
                        t="Être libre, c'est ne rencontrer aucun obstacle extérieur.",
                        etape="Elle se mesure : plus d'obstacles → moins de liberté.", x=170, y=210, w=940),
        "pbs": dict(type="liste", titre="Deux problèmes", items=[
            "Des obstacles, il y en a toujours : personne n'est jamais libre ?",
            "Elle regarde dehors, jamais dedans : d'où vient ce que je veux ?"], x=170, y=150, w=940),
        "rep_abs": dict(type="tag", style="repere", t="Repère · absolu / relatif", x=170, y=560, w=420),
        "platon": dict(type="portrait", img="platon", nom="Platon", dates="v. 428 – 348 av. J.-C.",
                       x=110, y=120, w=330, h=420),
        "gorg": dict(type="mot", t="Le Gorgias", g="Socrate contre Calliclès", x=500, y=230, w=680, taille=80),
        "c_call": dict(type="cit", a="Calliclès, dans Platon", o="Gorgias, 491e – 492a", para=True, x=170, y=170, w=940),
        "tonneaux": dict(type="illu", nom="tonneaux", x=140, y=100, w=1000, h=500),
        "tel": dict(type="illu", nom="tel", x=240, y=90, w=800, h=540),
        "rousseau": dict(type="portrait", img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                         x=110, y=120, w=330, h=420),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=500, y=150, w=680),
        "cols1": dict(type="cols", g="Liberté d'agir", gq="Est-ce que je peux faire ce que je veux ?",
                      d="Liberté de vouloir", dq="Est-ce que je veux librement ce que je veux ?", vs="≠"),
    }),

    # ------------------------------------------------------------------ III. trois libertés
    dict(id="trois", chap="Les trois libertés", fond="aube", beats=[
        "{trois_mot}Cette distinction, c'est la clé de toute la notion. Quand on parle de liberté, "
        "on peut en réalité parler {cartes}de trois choses différentes.",
        "{-trois_mot}{cartes.1}D'abord, la liberté d'agir : pouvoir faire ce que j'ai décidé, sans obstacle. "
        "Le prisonnier ne l'a plus ; l'oiseau en cage non plus. C'est la question de Hobbes : puis-je faire ?",
        "{cartes.2}Ensuite, la liberté de vouloir, qu'on appelle le libre arbitre : le pouvoir de choisir par moi-même, "
        "sans être déterminé par une cause que je ne maîtrise pas. Ici, la question n'est plus : puis-je faire ? "
        "Mais : aurais-je pu vouloir autre chose ?",
        ("C'est la question métaphysique. La plus vertigineuse.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{cartes.3}Enfin, la liberté politique : les libertés que la société me reconnaît et me garantit. "
        "Liberté d'expression, de conscience, de circuler, de se réunir. "
        "En 1789, la Déclaration des droits de l'homme et du citoyen la définit ainsi.{-cartes}",
        ("C", "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui.", "c_ddhc"),
        "Ces trois libertés ne vont pas forcément ensemble. Et l'histoire en offre un exemple saisissant.",
        "{-c_ddhc}{epic}Au premier siècle de notre ère, à Rome, vit un esclave venu d'Asie Mineure : Épictète. "
        "Il n'a aucune liberté politique : il appartient à un maître.",
        "On raconte qu'un jour, ce maître lui tordit la jambe. Épictète lui dit, très calmement : "
        "{jambe}{jambe.1}« Tu vas la casser. »",
        ("La jambe se brise.", {"rate": "-8%", "pitch": "-3Hz"}),
        "Et Épictète ajoute : {jambe.2}« Je te l'avais bien dit. »",
        ("P", 0.6),
        "{-jambe}Esclave selon la loi… et pourtant maître de lui-même. Épictète deviendra l'un des plus grands "
        "philosophes stoïciens. {grille}Pour lui, on peut enchaîner mon corps : {grille.1}pas ma volonté. "
        "Nous le retrouverons dans l'épisode quatre.",
        "{-epic}{-grille}{inverse}Inversement, on peut vivre dans le pays le plus libre du monde, avoir tous les droits… "
        "{inverse.1}et rester esclave de ses habitudes, de ses peurs, de ses désirs. Le tonneau percé, encore.",
        "{-inverse}{cartes2}Retiens donc ce réflexe, pour toutes tes copies. Devant un sujet sur la liberté, "
        "demande-toi toujours : {cartes2.hl}de quelle liberté parle-t-on ? {reflexe}D'agir, de vouloir… ou politique ?",
        ("P", 0.8),
    ], vis={
        "trois_mot": dict(type="mot", t="Liberté", g="un seul mot… et trois sens", y=250, taille=110),
        "cartes": dict(type="cartes", items=[
            dict(ic="porte", t="Liberté d'agir", q="Puis-je faire ce que j'ai décidé ?"),
            dict(ic="chemins", t="Libre arbitre", q="Aurais-je pu vouloir autre chose ?"),
            dict(ic="colonnes", t="Liberté politique", q="Que me garantit la société ?")]),
        "c_ddhc": dict(type="cit", a="Déclaration des droits de l'homme et du citoyen", o="article 4, 26 août 1789",
                       x=170, y=190, w=940),
        "epic": dict(type="portrait", img="epictete", nom="Épictète", dates="v. 50 – v. 130",
                     x=110, y=120, w=330, h=420),
        "jambe": dict(type="dialogue", lignes=["« Tu vas la casser. »", "« Je te l'avais bien dit. »"],
                      src="anecdote rapportée par Celse (IIᵉ siècle)", x=500, y=180, w=680),
        "grille": dict(type="liste", titre="Épictète", items=[
            "Liberté politique : aucune (il est esclave)", "Liberté intérieure : entière"], marques=["✗", "✓"],
                       x=500, y=180, w=680),
        "inverse": dict(type="liste", titre="Et à l'inverse…", items=[
            "Tous les droits, dans un pays libre", "… mais esclave de ses habitudes, de ses peurs, de ses désirs"],
                        marques=["✓", "✗"], x=170, y=190, w=940),
        "cartes2": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Agir", q="Puis-je faire ?"),
            dict(ic="chemins", t="Vouloir", q="Aurais-je pu vouloir autrement ?"),
            dict(ic="colonnes", t="Politique", q="Quels droits ?")]),
        "reflexe": dict(type="tag", style="copie", t="Réflexe copie · de quelle liberté parle le sujet ?",
                        x=340, y=590, w=600),
    }),

    # ------------------------------------------------------------------ IV. les repères
    dict(id="reperes", chap="Les mots pour le dire", fond="nuit", beats=[
        "{intro}Pour penser la liberté avec précision, le programme te donne des outils : les repères. "
        "Ce sont des couples de mots qu'on confond souvent… et que le correcteur adore voir distingués. "
        "Trois sont indispensables ici.",
        "{-intro}{murfeu}Premier couple : obligation et contrainte. Imagine deux situations. "
        "Tu marches dans la rue, et {murfeu.1}tu tombes sur un mur. Tu ne peux pas passer : c'est une contrainte. "
        "Elle agit sur toi par la force, que tu le veuilles ou non.",
        "Maintenant, {murfeu.2}tu arrives à un feu rouge. Tu pourrais passer : rien ne t'en empêche physiquement. "
        "Mais tu ne le dois pas. {murfeu.3}C'est une obligation.",
        "{-murfeu}{oc}Toute la différence est là : {oc.g}la contrainte s'impose à moi ; {oc.d}l'obligation s'adresse à moi. "
        "Elle suppose que je sois libre de lui obéir… ou non.",
        ("On ne donne pas d'ordre à un caillou.", {"rate": "-6%"}),
        "{-oc}{brigand}Rousseau prend l'exemple d'un brigand qui, au coin d'un bois, te menace de son pistolet. "
        "Tu lui donnes ta bourse. Mais es-tu obligé de la lui donner ?",
        ("C", "Céder à la force est un acte de nécessité, non de volonté ; c'est tout au plus un acte de prudence.",
         "c_force"),
        "{-c_force}{-brigand}{ffd}Le brigand me contraint ; il ne m'oblige pas. La force ne fait pas le droit. "
        "{ffd.1}Retiens le paradoxe : l'obligation, loin de détruire la liberté, la suppose. "
        "Kant en fera le cœur de sa morale. Ce sera l'épisode quatre.",
        "{-ffd}{trio}Deuxième couple, ou plutôt trio : {trio.1}nécessaire, contingent, possible. "
        "Est nécessaire ce qui ne peut pas être autrement. {pierre}Une pierre lâchée tombe : {pierre.1}elle ne peut pas "
        "faire autrement.",
        "{trio.2}Est contingent ce qui est, mais aurait pu ne pas être. Tu regardes cette vidéo… "
        "mais tu aurais pu ne pas la regarder.",
        ("Enfin… c'est ce qu'on croit.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-pierre}{trio.3}Et c'est là que tout se joue. Si tout ce qui arrive est nécessaire, s'il y a une cause à chacun "
        "de mes gestes, alors ma liberté est une illusion. Être libre suppose qu'il existe, quelque part, du contingent.",
        "{-trio}{fd}Troisième couple : en droit, en fait. {fd.g}En droit, c'est-à-dire selon la loi, ou selon ce qui "
        "devrait être. {fd.d}En fait : ce qui se passe réellement. En droit, tu es libre de partir au bout du monde. "
        "En fait, sans argent, ce droit ne vaut pas grand-chose.",
        "L'écrivain Anatole France s'en moquait, dans une formule cruelle.{-fd}",
        ("C", "La majestueuse égalité des lois, qui interdit au riche comme au pauvre de coucher sous les ponts, "
              "de mendier dans les rues et de voler du pain.", "c_france"),
        "{-c_france}{formel}Une liberté qui n'existe que sur le papier est-elle encore une liberté ? "
        "Dans la lignée de Karl Marx, on distinguera {formel.1}les libertés formelles, et les libertés réelles. "
        "Nous y reviendrons dans l'épisode cinq.",
        ("P", 0.8),
    ], vis={
        "intro": dict(type="mot", t="Les repères", g="des couples de mots que le correcteur adore voir distingués",
                      y=250, taille=96),
        "murfeu": dict(type="illu", nom="murfeu", x=140, y=110, w=1000, h=480),
        "oc": dict(type="cols", g="Contrainte", gq="s'impose à moi, par la force", d="Obligation",
                   dq="s'adresse à ma liberté : je peux désobéir", vs="≠", repere="Repère · obligation / contrainte"),
        "brigand": dict(type="portrait", img="rousseau", nom="Jean-Jacques Rousseau", dates="Du contrat social, I, 3",
                        x=110, y=120, w=330, h=420),
        "c_force": dict(type="cit", a="Rousseau", o="Du contrat social, I, 3 (1762)", x=500, y=170, w=680),
        "ffd": dict(type="def", terme="La force ne fait pas le droit",
                    t="Le brigand me contraint ; il ne m'oblige pas.",
                    etape="Paradoxe : l'obligation ne détruit pas la liberté, elle la suppose.", x=170, y=210, w=940),
        "trio": dict(type="liste", titre="Repère · nécessaire / contingent", items=[
            "Nécessaire : ne peut pas être autrement",
            "Contingent : est, mais aurait pu ne pas être",
            "Si tout est nécessaire, la liberté est une illusion"], marques=["1", "2", "→"], x=560, y=150, w=640),
        "pierre": dict(type="illu", nom="chute", x=80, y=110, w=440, h=480),
        "fd": dict(type="cols", g="En droit", gq="selon la loi, ou ce qui devrait être", d="En fait",
                   dq="ce qui se passe réellement", vs="≠", repere="Repère · en droit / en fait"),
        "c_france": dict(type="cit", a="Anatole France", o="Le Lys rouge (1894)", x=170, y=170, w=940),
        "formel": dict(type="cols", g="Libertés formelles", gq="écrites dans la loi", d="Libertés réelles",
                       dq="que l'on a vraiment les moyens d'exercer", vs="≠", plus=True),
    }),

    # ------------------------------------------------------------------ V. le problème
    dict(id="probleme", chap="Le grand problème", fond="aube", beats=[
        "{q_pb}Nous voilà prêts à voir le vrai problème. D'un côté, il y a une expérience que chacun fait, à chaque instant : "
        "{-q_pb}{sens}je me sens libre. Je lève la main… ou pas. Je choisis.",
        "{-sens}{desc}Descartes dira que c'est la chose la plus évidente du monde.",
        ("C", "La liberté de notre volonté se connaît sans preuve, par la seule expérience que nous en avons.",
         "c_desc"),
        "{-desc}{-c_desc}{causes}Mais de l'autre côté, il y a tout ce que nous apprenons du monde : chaque événement a une cause. "
        "{causes.1}Mes gènes, {causes.2}mon éducation, {causes.3}mon milieu, {causes.4}mon cerveau, "
        "{causes.5}mes désirs cachés…",
        "{-causes}{spino}Au dix-septième siècle, Spinoza prend une image saisissante. {lance}Imagine une pierre qu'on lance en l'air. "
        "{lance.1}Si cette pierre pouvait penser, {lance.2}elle croirait voler parce qu'elle l'a décidé.",
        ("Nous serions comme elle : conscients de ce que nous faisons… mais ignorants des causes qui nous font agir.",
         {"rate": "-5%"}),
        "{-spino}{-lance}{q2}Le sentiment d'être libre… ou l'ignorance de ce qui nous détermine ? "
        "Voilà la grande question. Et la série va la prendre sous tous ses angles.",
        "{-q2}{plan}{plan.1}Dans l'épisode deux, Descartes et Sartre défendront la liberté absolue de la volonté. "
        "{plan.2}Dans l'épisode trois, Spinoza, Freud et les sciences humaines viendront la contester. "
        "{plan.3}Dans l'épisode quatre, nous verrons qu'on peut, peut-être, devenir libre : avec les stoïciens, Spinoza encore, "
        "et Kant. {plan.4}Dans l'épisode cinq, la liberté descendra dans la rue : l'État, la loi, la société. "
        "{plan.5}Et dans l'épisode six, nous mettrons tout cela au service de ta copie.",
        ("P", 0.8),
    ], vis={
        "q_pb": dict(type="question", t="Sommes-nous vraiment libres ?"),
        "sens": dict(type="mot", t="« Je me sens libre »", g="l'expérience de chaque instant", y=260, taille=84),
        "desc": dict(type="portrait", img="descartes", nom="René Descartes", dates="1596 – 1650",
                     x=110, y=120, w=330, h=420),
        "c_desc": dict(type="cit", a="Descartes", o="Principes de la philosophie, I, 39 (1644)", x=500, y=170, w=680),
        "causes": dict(type="nuage", items=["mes gènes", "mon éducation", "mon milieu", "mon cerveau", "mes désirs cachés"],
                       centre="CAUSES"),
        "spino": dict(type="portrait", img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      x=110, y=120, w=330, h=420, legende="Lettre à Schuller, 1674"),
        "lance": dict(type="illu", nom="lance", x=470, y=110, w=730, h=480),
        "q2": dict(type="question", t="Sentiment d'être libre… ou ignorance des causes ?"),
        "plan": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · Le libre arbitre : Descartes, Sartre",
            "Ép. 3 · Une illusion ? Spinoza, Freud, les sciences humaines",
            "Ép. 4 · Se libérer : les stoïciens, Spinoza, Kant",
            "Ép. 5 · Libres ensemble : l'État, la loi, la société",
            "Ép. 6 · La liberté à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le sens premier. L'homme libre s'appartient : "
        "il n'est pas l'instrument d'un autre.",
        "{rec.2}Deux : faire ce que je veux, ce n'est pas vouloir librement. Hobbes d'un côté ; Platon et Rousseau de l'autre.",
        "{rec.3}Trois : il y a trois libertés. D'agir, de vouloir, et politique.",
        "{rec.4}Quatre : trois repères. Obligation et contrainte. Nécessaire et contingent. En droit et en fait.",
        "{-rec}{frise}Maintenant, à toi : quelques questions t'attendent sous la vidéo.",
        ("Et la prochaine fois… nous entrerons dans la tête de Descartes.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-frise}{fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="liste", titre="À retenir", items=[
            "Être libre, c'est s'appartenir : ne pas être l'instrument d'un autre (Aristote)",
            "Faire ce que je veux ≠ vouloir librement (Hobbes / Platon, Rousseau)",
            "Trois libertés : d'agir, de vouloir (libre arbitre), politique",
            "Repères : obligation / contrainte · nécessaire / contingent · en droit / en fait"],
                    marques=["1", "2", "3", "4"], x=150, y=120, w=980),
        "frise": dict(type="frise", items=[
            dict(nom="Platon", d=-428, img="platon"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Épictète", d=50, img="epictete"), dict(nom="Descartes", d=1596, img="descartes"),
            dict(nom="Hobbes", d=1588, img="hobbes"), dict(nom="Spinoza", d=1632, img="spinoza"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Marx", d=1818), dict(nom="Freud", d=1856), dict(nom="Sartre", d=1905)]),
        "fin": dict(type="titre", sur="À suivre", t="Le libre arbitre", sous="Épisode 2 · Descartes et Sartre"),
    }),
]

QUIZ = [
    dict(q="Selon Aristote, qui est l'homme libre ?",
         r=["Celui qui fait tout ce qu'il désire", "Celui qui est à lui-même sa propre fin et n'existe pas pour un autre",
            "Celui qui obéit aux lois de sa cité", "Celui qui ne rencontre aucun obstacle"], ok=1,
         voir="c_arist", ex="Métaphysique, A, 2 : être libre, c'est ne pas être l'instrument d'un autre. C'est le sens premier, opposé à l'esclave."),
    dict(q="Pour Hobbes, la liberté, c'est…",
         r=["l'absence d'obstacles extérieurs au mouvement", "l'obéissance à la loi qu'on s'est prescrite",
            "le pouvoir de choisir sans cause", "la connaissance des causes"], ok=0,
         voir="c_hobbes", ex="Léviathan, XXI : l'eau retenue dans un vase n'est pas libre de se répandre. C'est la liberté « négative »."),
    dict(q="Que veut montrer Socrate avec l'image des tonneaux percés ?",
         r=["Qu'il faut satisfaire tous ses désirs", "Que celui qui suit tous ses désirs n'est jamais satisfait : il en est esclave",
            "Que la liberté politique est une illusion", "Que l'eau est libre quand on ôte l'obstacle"], ok=1,
         voir="tonneaux", ex="Contre Calliclès (Gorgias) : un désir satisfait en appelle un autre. Rousseau dira : « l'impulsion du seul appétit est esclavage »."),
    dict(q="Un feu rouge relève…",
         r=["de la contrainte", "de l'obligation", "de la nécessité", "du libre arbitre"], ok=1,
         voir="murfeu", ex="Je peux physiquement passer, mais je ne le dois pas : l'obligation s'adresse à ma liberté. Le mur, lui, me contraint."),
    dict(q="« Aurais-je pu vouloir autre chose ? » De quelle liberté parle-t-on ?",
         r=["La liberté d'agir", "La liberté politique", "Le libre arbitre", "La liberté négative"], ok=2,
         voir="cartes", ex="C'est la liberté de la volonté, la question métaphysique : celle des épisodes 2 et 3."),
    dict(q="« J'ai le droit de voyager, mais je n'en ai pas les moyens. » Quel repère cela illustre-t-il ?",
         r=["Nécessaire / contingent", "Obligation / contrainte", "En droit / en fait", "Absolu / relatif"], ok=2,
         voir="fd", ex="Libre en droit, pas en fait : c'est l'écart entre libertés formelles et libertés réelles (Anatole France, Marx)."),
]

CREDITS = [
    "Aristote : buste, Rome, Palazzo Altemps (photographie Jastrow, domaine public)",
    "Platon : Raphaël, L'École d'Athènes, détail, 1509-1511",
    "Hobbes : John Michael Wright, vers 1669-1670",
    "Épictète : gravure ancienne (domaine public)",
    "Rousseau : Maurice Quentin de La Tour, 1753",
    "Descartes : d'après Frans Hals, XVIIᵉ siècle",
    "Spinoza : portrait anonyme, vers 1665",
    "Kant : portrait anonyme, XVIIIᵉ siècle",
    "Images : Wikimedia Commons. Voix de synthèse Microsoft (edge-tts). Musique originale générée pour la série.",
]
