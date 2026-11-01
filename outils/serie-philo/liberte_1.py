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
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{ico}Une question, pour commencer. Ce matin, {ico.1}qui a choisi tes habits ?",
        ("Toi, évidemment.", {"rate": "-4%"}),
        "Et la musique dans tes écouteurs ? {ico.2}Toi aussi.",
        "Et le moment où tu as ouvert ton téléphone… {ico.3}sans même y penser ?",
        ("Là, déjà… c'est moins sûr.", {"rate": "-8%", "pitch": "-2Hz"}),
        ("P", 0.6),
        "{-ico}{q1}{tab_lib}Nous passons nos journées à nous dire libres. Libres de sortir, libres de penser, libres de dire non. "
        "Et pourtant, dès qu'on essaie de dire ce que c'est, être libre… le mot nous file entre les doigts.",
        "{-q1}{noms}Cette série va prendre ce mot, que tout le monde emploie, et le regarder de très près. "
        "Avec ceux qui y ont consacré leur vie : {noms.1}Platon, {noms.2}Descartes, {noms.3}Spinoza, "
        "{noms.4}Rousseau, {noms.5}Kant, {noms.6}Sartre… et quelques autres.",
        "{-noms}{-tab_lib}{serie}Six épisodes, et un récapitulatif. Celui-ci est le premier. "
        "Car avant de savoir si nous sommes libres… {-serie}il faut savoir de quoi l'on parle.",
        ("P", 0.3),
        "{titre}",
        ("P", 3.2),
    ], vis={
        "ico": dict(type="illu", nom="icones", x=190, y=170, w=900, h=360),
        "tab_lib": dict(type="tableau", img="t-liberte-peuple", fond=True, de=[1.35, .52, .2], a=[1.0, .5, .45],
                        legende="Eugène Delacroix, La Liberté guidant le peuple, 1830"),
        "q1": dict(type="question", t="Être libre… mais de quoi parle-t-on ?"),
        "noms": dict(type="nuage", items=["Platon", "Descartes", "Spinoza", "Rousseau", "Kant", "Sartre"]),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="une notion, regardée sous tous ses angles", y=270),
        "titre": dict(type="titre", sur="La liberté · Épisode 1", t="Qu'est-ce qu'être libre ?",
                      sous="Le mot, les trois libertés, les repères"),
    }),

    # ------------------------------------------------------------------ I. le mot
    dict(id="mot", chap="Le mot", fond="aube", humeur="mystere", notions=["l'État", "le devoir"], retenir="Être libre, au sens premier : s'appartenir, n'être l'instrument de personne.", beats=[
        "{tab_acr}Remontons d'abord le temps. Athènes, cinq siècles avant notre ère. "
        "Sur l'agora, la grande place de la cité, {-tab_acr}{tab_per}{agora}deux hommes se croisent.",
        "{agora.1}L'un est citoyen : il vote, il prend la parole à l'assemblée, il décide des lois. "
        "L'autre porte la même tunique, mange le même pain… {-tab_per}{tab_esc}{agora.2}mais il appartient à quelqu'un. C'est un {!esclave}esclave.",
        ("Alors, qu'est-ce qui les sépare ?", {"pitch": "+2Hz"}),
        ("Pas la force. Pas l'intelligence. Une seule chose : {agora.3}le premier s'appartient à lui-même. "
         "Le second appartient à un autre.", {"rate": "-5%"}),
        "C'est le sens le plus ancien du mot. En grec, l'homme libre se dit {-agora}{-tab_esc}{grec}éleuthéros. "
        "En latin, {tab_for}{lat}liber.",
        "Et ces deux mots viendraient d'une même racine, très ancienne, {-grec}{-lat}{racine}qui désignait… {racine.1}le peuple. "
        "Être libre, à l'origine, c'est faire partie des siens, {racine.2}par opposition à l'étranger capturé, réduit en esclavage. "
        "On retrouve d'ailleurs cette racine dans un mot allemand, {racine.3}« Leute », qui veut dire : les gens.",
        "{-racine}{liberi}Mieux encore : en latin, liberi, au pluriel, veut dire… les enfants. "
        "Les enfants libres de la maison, par opposition aux esclaves qui y servent.",
        "{-liberi}{-tab_for}{arist}{tab_ath}Au quatrième siècle avant notre ère, Aristote en tire une définition "
        "qui va traverser toute l'histoire de la philosophie.",
        ("C", "Nous appelons homme libre celui qui est à lui-même sa fin et n'existe pas pour un autre.", "c_arist"),
        "{-arist}{-c_arist}{-tab_ath}{tab_aff}{def1}Retiens bien cette idée. Être libre, c'est ne pas être un {!instrument}instrument. "
        "L'esclave est un moyen au service des fins d'un autre ; {def1.1}l'homme libre poursuit ses propres fins.",
        "{-def1}{note}Attention, pourtant. Aristote lui-même jugeait l'esclavage naturel : il appelait l'esclave "
        "« une propriété animée ». La définition est belle, mais son époque la réservait à quelques-uns.",
        "{note.1}Toute l'histoire de la liberté sera aussi l'histoire de son extension. "
        "{-tab_aff}{kant}Deux mille ans plus tard, {#le devoir}Kant exigera que toute personne soit traitée comme une fin, "
        "et jamais simplement comme un moyen.",
        ("Tu vois le fil ?", {"pitch": "+3Hz"}),
    ], vis={
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, de=[1.0, .5, .55], a=[1.75, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 · au centre, Platon et Aristote"),
        "tab_for": dict(type="tableau", img="t-forum", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Claude Lorrain, Caprice avec les ruines du Forum romain, v. 1634"),
        "tab_aff": dict(type="tableau", img="t-affranchi", fond=True, de=[1.45, .12, .38], a=[1.6, .1, .34],
                        legende="Relief d'affranchissement, musée de Mariemont (Ad Meskens, CC BY-SA 4.0)"),
        "tab_acr": dict(type="tableau", img="t-acropole", de=[1.0, .5, .5], a=[1.35, .55, .4],
                        legende="Leo von Klenze, l'Acropole et l'Aréopage d'Athènes, reconstitution, 1846"),
        "tab_per": dict(type="tableau", img="t-pericles", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .62, .4],
                        legende="Philipp von Foltz, Périclès parlant aux Athéniens, 1852 (photographie, Rijksmuseum)"),
        "tab_esc": dict(type="tableau", img="t-esclaves", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Esclaves enchaînés par le cou, relief romain, Ashmolean Museum (photo Jun, CC BY-SA 2.0)"),
        "agora": dict(type="illu", nom="agora", x=140, y=110, w=1000, h=470),
        "grec": dict(type="mot", t="ἐλεύθερος", g="éleuthéros · grec : l'homme libre", y=150, taille=92),
        "lat": dict(type="mot", t="LIBER", g="latin : l'homme libre, qui n'est pas esclave", y=380, taille=104),
        "racine": dict(type="illu", nom="racine", x=140, y=100, w=1000, h=500, plus=True),
        "liberi": dict(type="mot", t="liberi", g="en latin : « les enfants » (nés libres)", y=250, taille=110),
        "arist": dict(type="portrait", annee=-384, legende="Métaphysique · Politique", img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      x=110, y=120, w=330, h=420),
        "c_arist": dict(type="cit", a="Aristote", o="Métaphysique, livre A, 2", x=640, y=170, w=570),
        "def1": dict(type="def", cles=["instrument", "fins"], terme="Être libre · le sens premier",
                     t="Ne pas appartenir à un autre : être à soi-même sa propre fin, et non l'instrument d'un autre.",
                     etape="Esclave → moyen pour les fins d'un autre   ·   Homme libre → poursuit ses propres fins",
                     x=170, y=190, w=940),
        "note": dict(type="note", cles=["naturel", "propriété", "extension"], titre="Attention",
                     t="Aristote juge l'esclavage naturel : l'esclave serait « une propriété animée » (Politique, I, 4).",
                     etape="L'histoire de la liberté est aussi celle de son extension à tous.",
                     x=170, y=130, w=940),
        "kant": dict(type="tag", style="lien", t="Kant (1785) : toute personne est une fin, jamais un simple moyen",
                     x=170, y=520, w=940),
    }),

    # ------------------------------------------------------------------ II. faire ce que je veux
    dict(id="faire", chap="Faire ce que je veux ?", fond="nuit", humeur="tension", notions=["le bonheur"], retenir="Faire ce que je veux ≠ vouloir librement : l'esclave de ses désirs n'est pas libre.", beats=[
        "{tab_tok}{q_quoi}Revenons à aujourd'hui. Si je te demande : être libre, c'est quoi ? "
        "Tu vas sans doute répondre : {-q_quoi}{fcqjv}c'est faire ce que je veux. Personne ne m'empêche, personne ne m'oblige.",
        "{-fcqjv}{-tab_tok}{hobbes}{tab_lev}C'est la définition du sens commun. Et elle a un défenseur de poids : Thomas Hobbes, "
        "philosophe anglais du dix-septième siècle.",
        ("C", "La liberté signifie proprement l'absence d'opposition ; par opposition, j'entends les obstacles "
              "extérieurs au mouvement.", "c_hobbes"),
        "{-hobbes}{-c_hobbes}{-tab_lev}{vase}Hobbes prend un exemple tout simple : l'eau. Retenue dans un vase, "
        "elle ne peut pas se répandre : elle n'est pas libre. {vase.1}Ôtez l'obstacle… et elle s'écoule.",
        ("Être libre, c'est cela : ne rencontrer aucun {!obstacle}obstacle.", {"rate": "-5%"}),
        "{-vase}{tab_car}{def_neg}Cette définition a un grand mérite : elle est claire, et elle se mesure. "
        "Plus il y a d'obstacles, moins je suis libre. On parle parfois de liberté négative : "
        "{def_neg.1}la liberté comme absence. Absence de murs, de chaînes, d'interdits.",
        ("Mais regarde de plus près. Elle pose deux problèmes.", {"pitch": "-2Hz"}),
        "{-def_neg}{pbs}{pbs.1}Premier problème : des obstacles extérieurs, il y en a toujours. Des murs, des lois, d'autres hommes. "
        "Hobbes, lui, précise une chose : ne pas savoir voler comme un oiseau, ce n'est pas manquer de liberté, "
        "c'est manquer de pouvoir. Reste que si être libre, c'est n'être empêché par rien du dehors… "
        "personne ne l'est jamais tout à fait. "
        "{rep_abs}Ainsi définie, la liberté est toujours relative, jamais absolue.",
        "{-tab_car}{pbs.2}Second problème, plus profond : cette définition ne regarde que ce qui se passe dehors, "
        "entre moi et le monde. Elle ne demande jamais ce qui se passe dedans.",
        ("D'où vient… ce que je veux ?", {"rate": "-10%", "pitch": "-1Hz"}),
        "{-pbs}{-rep_abs}{platon}{tab_soc}Platon a mis ce problème en scène dans un dialogue célèbre, {gorg}le Gorgias. "
        "Socrate y affronte un jeune homme brillant et arrogant : Calliclès. "
        "Pour Calliclès, l'homme vraiment libre, c'est celui qui a le courage de ses désirs.",
        "{-platon}{-gorg}{-tab_soc}{tab_cla}",
        ("C", "Pour bien vivre, il faut laisser ses passions devenir aussi grandes que possible, au lieu de les réprimer.",
         "c_call"),
        "Satisfaire tous ses désirs, sans entraves : voilà, pour lui, la liberté, et le bonheur. "
        "{-c_call}{-tab_cla}{tonneaux}Socrate lui répond par une image. Imagine deux hommes, chacun avec ses tonneaux.",
        "{tonneaux.1}Les tonneaux du premier sont sains : une fois remplis, il est tranquille. "
        "{tonneaux.2}Ceux du second sont percés. Il a beau verser, verser encore… ils se vident sans cesse. "
        "{tonneaux.3}Il passe sa vie à les remplir, sans jamais pouvoir s'arrêter.",
        ("{-tonneaux}{tab_dan}Celui qui suit tous ses désirs n'est pas libre : il est l'esclave d'un tonneau qui fuit. "
         "Car un désir satisfait en appelle aussitôt un autre.", {"rate": "-4%"}),
        "{-tab_dan}{tel}Ce tonneau, tu le connais. C'est la vidéo suivante qui se lance toute seule, "
        "{tel.1}le fil qu'on fait défiler sans fin, {tel.2}la notification à laquelle on répond sans y penser.",
        ("Je fais ce que je veux… mais est-ce bien moi qui veux ?", {"rate": "-6%", "pitch": "+1Hz"}),
        "{-tel}{rousseau}{tab_con}Vingt siècles après Platon, Jean-Jacques Rousseau résume tout cela en une phrase. "
        "Une phrase à apprendre par cœur.",
        ("C", "L'impulsion du seul appétit est esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.",
         "c_rous"),
        "{-rousseau}{-c_rous}{-tab_con}{cols1}Retiens la leçon. Faire ce que je veux, ce n'est pas forcément vouloir librement. "
        "Il y a deux questions, et non une seule. {cols1.g}Est-ce que je peux faire ce que je veux ? "
        "{cols1.d}Et est-ce que je veux librement… ce que je veux ?",
        ("P", 0.8),
    ], vis={
        "q_quoi": dict(type="question", t="Être libre, c'est quoi ?"),
        "fcqjv": dict(type="mot", t="« Faire ce que je veux »", g="la définition du sens commun", y=260, taille=78),
        "tab_lev": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.5, .5, .32],
                        legende="Abraham Bosse, frontispice du Léviathan, 1651"),
        "tab_tok": dict(type="tableau", img="t-tokyo", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Tokyo, carrefour de Shibuya (photo Benh Lieu Song, CC BY-SA 2.0)"),
        "tab_car": dict(type="tableau", img="t-carceri", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .5, .6],
                        legende="Piranèse, Prisons imaginaires, planche XVI, 1761"),
        "hobbes": dict(type="portrait", annee=1588, legende="Léviathan (1651)", img="hobbes", nom="Thomas Hobbes", dates="1588 – 1679",
                       x=110, y=120, w=330, h=420),
        "c_hobbes": dict(type="cit", a="Hobbes", o="Léviathan, chap. XXI (1651)", x=500, y=150, w=680),
        "vase": dict(type="illu", nom="vase", x=240, y=110, w=800, h=480),
        "def_neg": dict(type="def", cles=["obstacles", "mesure"], terme="La liberté « négative »",
                        t="Être libre, c'est ne rencontrer aucun obstacle extérieur.",
                        etape="Elle se mesure : plus d'obstacles → moins de liberté.", x=170, y=210, w=940),
        "pbs": dict(type="liste", cles=["obstacles", "dedans"], titre="Deux problèmes", items=[
            "Des obstacles extérieurs, il y en a toujours : murs, lois, autres hommes",
            "Elle regarde dehors, jamais dedans : d'où vient ce que je veux ?"], x=170, y=150, w=940),
        "rep_abs": dict(type="tag", style="repere", t="Repère · absolu / relatif", x=170, y=560, w=420),
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, de=[1.0, .5, .5], a=[1.45, .62, .42],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787"),
        "platon": dict(type="portrait", annee=-428, legende="Gorgias · La République", img="platon", nom="Platon", dates="v. 428 – 348 av. J.-C.",
                       x=110, y=120, w=330, h=420),
        "gorg": dict(type="mot", t="Le Gorgias", g="Socrate contre Calliclès", x=640, y=230, w=570, taille=80),
        "tab_cla": dict(type="tableau", img="t-clarke", fond=True, sombre=True, de=[1.0, 0.5, 0.3], a=[1.3, 0.5, 0.45],
                        legende="Le plus ancien manuscrit de Platon, copié en 895 (Oxford, Bodleian Library)"),
        "c_call": dict(type="cit", a="Calliclès, dans Platon", o="Gorgias, 491e – 492a", para=True, x=170, y=170, w=940),
        "tonneaux": dict(type="illu", nom="tonneaux", x=140, y=100, w=1000, h=500),
        "tab_dan": dict(type="tableau", img="t-danaides", de=[1.0, .5, .25], a=[1.25, .5, .6],
                        legende="John William Waterhouse, Les Danaïdes, 1906 · condamnées à remplir sans fin des jarres percées"),
        "tel": dict(type="illu", nom="tel", x=240, y=90, w=800, h=540),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, de=[1.0, 0.5, 0.35], a=[1.2, 0.5, 0.5], sombre=True,
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "rousseau": dict(type="portrait", annee=1712, legende="Du contrat social (1762)", img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                         x=110, y=120, w=330, h=420),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=500, y=150, w=680),
        "cols1": dict(type="cols", g="Liberté d'agir", gq="Est-ce que je peux faire ce que je veux ?",
                      d="Liberté de vouloir", dq="Est-ce que je veux librement ce que je veux ?", vs="≠"),
    }),

    # ------------------------------------------------------------------ III. trois libertés
    dict(id="trois", chap="Les trois libertés", fond="aube", humeur="lumiere", notions=["l'État", "la justice"], retenir="Trois libertés : d'agir, de vouloir, politique. Toujours se demander de laquelle on parle.", beats=[
        "{tab_pen}{trois_mot}Cette distinction, c'est la clé de toute la notion. Quand on parle de liberté, "
        "on peut en réalité parler {cartes}de trois choses différentes.",
        "{-trois_mot}{cartes.1}D'abord, la liberté d'agir : pouvoir faire ce que j'ai décidé, sans obstacle. "
        "{-tab_pen}{tab_pri}Le prisonnier ne l'a plus ; {-tab_pri}{tab_cha}l'oiseau en cage non plus. C'est la question de Hobbes : puis-je faire ?",
        "{-tab_cha}{cartes.2}Ensuite, la liberté de vouloir, qu'on appelle le libre arbitre : le pouvoir de choisir par moi-même, "
        "sans être déterminé par une cause que je ne maîtrise pas. Ici, la question n'est plus : puis-je faire ? "
        "Mais : aurais-je pu vouloir autre chose ?",
        ("C'est la question métaphysique. La plus vertigineuse.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{cartes.3}{tab_bas}Enfin, {#l'État}la liberté politique : les libertés que la société me reconnaît et me garantit. "
        "Liberté d'expression, de conscience, de circuler, de se réunir. "
        "{-tab_bas}{tab_ddhc}En 1789, la Déclaration des droits de l'homme et du citoyen la définit ainsi.{-cartes}",
        ("C", "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui.", "c_ddhc"),
        "Ces trois libertés ne vont pas forcément ensemble. Et l'histoire en offre un exemple saisissant.",
        "{-c_ddhc}{-tab_ddhc}{epic}{tab_hie}Au premier siècle de notre ère, à Rome, vit un esclave venu d'Asie Mineure : Épictète. "
        "Il n'a aucune liberté politique : il appartient à un maître.",
        "On raconte qu'un jour, ce maître lui tordit la jambe. Épictète lui dit, très calmement : "
        "{jambe}{jambe.1}« Tu vas la casser. »",
        ("La jambe se brise.", {"rate": "-8%", "pitch": "-3Hz"}),
        "Et Épictète ajoute : {jambe.2}« Je te l'avais bien dit. »",
        ("P", 0.6),
        "{-jambe}Esclave selon la loi… et pourtant maître de lui-même. Épictète deviendra l'un des plus grands "
        "philosophes stoïciens. {grille}{grille.1}Pour lui, on peut enchaîner mon corps : {grille.2}pas ma volonté. "
        "Ce n'est ni la liberté d'agir, ni exactement le libre arbitre : c'est une liberté intérieure, morale, "
        "celle du sage. Nous la retrouverons dans l'épisode quatre.",
        "{-epic}{-grille}{-tab_hie}{tab_ecr}{inverse}{inverse.1}Inversement, on peut vivre dans le pays le plus libre du monde, avoir tous les droits… "
        "{inverse.2}et rester esclave de ses habitudes, de ses peurs, de ses désirs. Le tonneau percé, encore.",
        "{-inverse}{-tab_ecr}{tab_exa}{cartes2}Retiens donc ce réflexe, pour toutes tes copies. Devant un sujet sur la liberté, "
        "demande-toi toujours : {cartes2.hl}de quelle liberté parle-t-on ? {reflexe}D'agir, de vouloir… ou politique ?",
        ("P", 0.8),
    ], vis={
        "trois_mot": dict(type="mot", t="Liberté", g="un seul mot… et trois sens", y=250, taille=110),
        "tab_pri": dict(type="tableau", img="t-prisonniers", fond=True, de=[1.0, 0.5, 0.5], a=[1.3, 0.5, 0.62],
                        legende="Vincent van Gogh, La Ronde des prisonniers, 1890"),
        "tab_pen": dict(type="tableau", img="t-penseur", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.35, .5, .25],
                        legende="Auguste Rodin, Le Penseur, détail de La Porte de l'Enfer, musée Rodin (photo Jebulon, CC0)"),
        "tab_cha": dict(type="tableau", img="t-chardonneret", fond=True, de=[1.0, 0.5, 0.5], a=[1.4, 0.5, 0.45],
                        legende="Carel Fabritius, Le Chardonneret, 1654 · un oiseau enchaîné à son perchoir"),
        "cartes": dict(type="cartes", items=[
            dict(ic="porte", t="Liberté d'agir", q="Puis-je faire ce que j'ai décidé ?"),
            dict(ic="chemins", t="Libre arbitre", q="Aurais-je pu vouloir autre chose ?"),
            dict(ic="colonnes", t="Liberté politique", q="Que me garantit la société ?")]),
        "tab_ddhc": dict(type="tableau", img="t-ddhc", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                        legende="Jean-Jacques-François Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "tab_bas": dict(type="tableau", img="t-bastille", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .45],
                        legende="Jean-Pierre Houël, La Prise de la Bastille, 1789"),
        "c_ddhc": dict(type="cit", a="Déclaration des droits de l'homme et du citoyen", o="article 4, 26 août 1789",
                       x=170, y=190, w=940),
        "tab_hie": dict(type="tableau", img="t-hierapolis", fond=True, sombre=True, de=[1.0, .25, .5], a=[1.0, .75, .5],
                        legende="Hiérapolis, en Phrygie, ville natale d'Épictète (photo Bernard Gagnon, CC BY-SA 3.0)"),
        "tab_ecr": dict(type="tableau", img="t-ecrans", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .6, .4],
                        legende="Photo Rawpixel, CC BY 2.0"),
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "epic": dict(type="portrait", annee=50, legende="Entretiens · Manuel", img="epictete", nom="Épictète", dates="v. 50 – v. 130",
                     x=110, y=120, w=330, h=420),
        "jambe": dict(type="dialogue", lignes=["« Tu vas la casser. »", "« Je te l'avais bien dit. »"],
                      src="anecdote de Celse (IIᵉ s.), citée par Origène, Contre Celse, VII, 53 · peut-être légendaire", x=640, y=180, w=570),
        "grille": dict(type="liste", titre="Épictète", items=[
            "Liberté politique : aucune (il est esclave)", "Liberté intérieure : entière"], marques=["✗", "✓"],
                       x=640, y=180, w=570),
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
    dict(id="reperes", chap="Les mots pour le dire", fond="nuit", humeur="calme", notions=["le devoir", "la nature", "la justice"], retenir="Contrainte ≠ obligation · nécessaire ≠ contingent · en droit ≠ en fait.", beats=[
        "{intro}Pour penser la liberté avec précision, le programme te donne des outils : les repères. "
        "Ce sont des couples de mots qu'on confond souvent… et que le correcteur adore voir distingués. "
        "Trois sont indispensables ici.",
        "{-intro}{murfeu}Premier couple : obligation et contrainte. Imagine deux situations. "
        "Tu marches dans la rue, et {murfeu.1}tu tombes sur un mur. Tu ne peux pas passer : c'est une contrainte. "
        "Elle agit sur toi par la force, que tu le veuilles ou non.",
        "Maintenant, {murfeu.2}tu arrives à un feu rouge. Tu pourrais passer : rien ne t'en empêche physiquement. "
        "Mais tu ne le dois pas. {murfeu.3}C'est une obligation.",
        "{-murfeu}{oc}{tab_ber}Toute la différence est là : {oc.g}la contrainte s'impose à moi ; {oc.d}l'obligation s'adresse à moi. "
        "Elle suppose que je sois libre de lui obéir… ou non.",
        ("On ne donne pas d'ordre à un caillou.", {"rate": "-6%"}),
        "{-oc}{-tab_ber}{brigand}Rousseau prend l'exemple d'un brigand qui, au coin d'un bois, te menace de son pistolet. "
        "Tu lui donnes ta bourse. Mais es-tu obligé de la lui donner ?",
        ("C", "Céder à la force est un acte de nécessité, non de volonté ; c'est tout au plus un acte de prudence.",
         "c_force"),
        "{-c_force}{-brigand}{ffd}Le brigand me contraint ; il ne m'oblige pas. {#la justice}La force ne fait pas le droit. "
        "{ffd.1}Retiens le paradoxe : l'obligation, loin de détruire la liberté, la suppose. "
        "Kant en fera le cœur de sa morale. Ce sera l'épisode quatre.",
        "{-ffd}{tab_new}{trio}Deuxième couple : {trio.1}nécessaire et contingent. "
        "Est nécessaire ce qui ne peut pas être autrement. {pierre}Une pierre lâchée tombe : {pierre.1}elle ne peut pas "
        "faire autrement.",
        "{trio.2}Est contingent ce qui est, mais aurait pu ne pas être. Tu regardes cette vidéo… "
        "mais tu aurais pu ne pas la regarder.",
        ("Enfin… c'est ce qu'on croit.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-pierre}{trio.3}Et c'est là que tout se joue. Si tout ce qui arrive est nécessaire, s'il y a une cause à chacun "
        "de mes gestes, alors le libre arbitre semble une {!illusion}illusion. Croire au libre arbitre, c'est supposer qu'il existe, "
        "quelque part, du contingent.",
        "{-trio}{-tab_new}{fd}Troisième couple : en droit, en fait. {fd.g}En droit, c'est-à-dire selon la loi, ou selon ce qui "
        "devrait être. {fd.d}En fait : ce qui se passe réellement. En droit, tu es libre de partir au bout du monde. "
        "En fait, sans argent, ce droit ne vaut pas grand-chose.",
        "{tab_dor}L'écrivain Anatole France fait dire à l'un de ses personnages cette formule cruelle.{-fd}",
        ("C", "La majestueuse égalité des lois, qui interdit au riche comme au pauvre de coucher sous les ponts, "
              "de mendier dans les rues et de voler du pain.", "c_france"),
        "{-c_france}{-tab_dor}{formel}Une liberté qui n'existe que sur le papier est-elle encore une liberté ? "
        "Dans la lignée de {tab_marx}Karl Marx, on distinguera {formel.1}les libertés formelles, et les libertés réelles. "
        "Nous y reviendrons dans l'épisode cinq.",
        ("P", 0.8),
    ], vis={
        "intro": dict(type="mot", t="Les repères", g="des couples de mots que le correcteur adore voir distingués",
                      y=250, taille=96),
        "murfeu": dict(type="illu", nom="murfeu", x=140, y=110, w=1000, h=480),
        "tab_ber": dict(type="tableau", img="t-berlin", fond=True, sombre=True, de=[1.0, 0.5, 0.5], a=[1.25, 0.5, 0.5],
                        legende="Le mur de Berlin et sa zone interdite, 1977 (photo George Garrigues, CC BY-SA 3.0)"),
        "oc": dict(type="cols", g="Contrainte", gq="s'impose à moi, par la force", d="Obligation",
                   dq="s'adresse à ma liberté : je peux désobéir", vs="≠", repere="Repère · obligation / contrainte"),
        "brigand": dict(type="portrait", img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778", legende="Du contrat social, I, 3",
                        x=110, y=120, w=330, h=420),
        "c_force": dict(type="cit", a="Rousseau", o="Du contrat social, I, 3 (1762)", x=500, y=170, w=680),
        "ffd": dict(type="def", cles=["contraint", "oblige", "suppose"], terme="La force ne fait pas le droit",
                    t="Le brigand me contraint ; il ne m'oblige pas.",
                    etape="Paradoxe : l'obligation ne détruit pas la liberté, elle la suppose.", x=170, y=210, w=940),
        "trio": dict(type="liste", titre="Repère · nécessaire / contingent", items=[
            "Nécessaire : ne peut pas être autrement",
            "Contingent : est, mais aurait pu ne pas être",
            "Si tout est nécessaire, le libre arbitre semble une illusion"], marques=["1", "2", "→"], x=560, y=150, w=640),
        "pierre": dict(type="illu", nom="chute", x=80, y=110, w=440, h=480),
        "fd": dict(type="cols", g="En droit", gq="selon la loi, ou ce qui devrait être", d="En fait",
                   dq="ce qui se passe réellement", vs="≠", repere="Repère · en droit / en fait"),
        "tab_dor": dict(type="tableau", img="t-dore", fond=True, sombre=True, de=[1.0, 0.5, 0.5], a=[1.3, 0.5, 0.45],
                        legende="Gustave Doré, Londres vu du chemin de fer, 1872"),
        "tab_new": dict(type="tableau", img="t-newton", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .55],
                        legende="William Blake, Newton, 1795-1805"),
        "c_france": dict(type="cit", a="Anatole France", o="Le Lys rouge, chap. VII (1894)", x=170, y=170, w=940),
        "tab_marx": dict(type="tableau", img="marx", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .35],
                         legende="Karl Marx, photographie de John Mayall"),
        "formel": dict(type="cols", g="Libertés formelles", gq="écrites dans la loi", d="Libertés réelles",
                       dq="que l'on a vraiment les moyens d'exercer", vs="≠", plus=True),
    }),

    # ------------------------------------------------------------------ V. le problème
    dict(id="probleme", chap="Le grand problème", fond="aube", humeur="tension", notions=["la conscience", "la nature"], retenir="Se sentir libre suffit-il à l'être ? Ou n'est-ce que l'ignorance des causes ?", beats=[
        "{q_pb}Nous voilà prêts à voir le vrai problème. D'un côté, il y a une expérience que chacun fait, à chaque instant : "
        "{-q_pb}{sens}je me sens libre. Je lève la main… ou pas. Je choisis.",
        "{-sens}{desc}Descartes dira que c'est la chose la plus évidente du monde.",
        ("C", "La liberté de notre volonté se connaît sans preuve, par la seule expérience que nous en avons.",
         "c_desc"),
        "{-desc}{-c_desc}{causes}Mais de l'autre côté, il y a tout ce que nous apprenons du monde : chaque événement a une cause. "
        "{causes.1}Mes gènes, {causes.2}mon éducation, {causes.3}mon milieu, {causes.4}mon cerveau, "
        "{causes.5}mes désirs cachés…",
        "{-causes}{spino}{tab_eth}Au dix-septième siècle, Spinoza prend une image saisissante. {lance}Imagine une pierre qu'on lance en l'air. "
        "{lance.1}Si cette pierre pouvait penser, {lance.2}elle croirait voler parce qu'elle l'a décidé.",
        ("Nous serions comme elle : conscients de nos désirs… mais ignorants des causes qui nous déterminent.",
         {"rate": "-5%"}),
        "{-spino}{-lance}{-tab_eth}{q2}Le sentiment d'être libre… ou l'{!ignorance}ignorance de ce qui nous détermine ? "
        "Voilà la grande question. Et la série va la prendre sous tous ses angles.",
        "{-q2}{plan}{tab_chr}{plan.1}Dans l'épisode deux, Descartes et Sartre défendront la liberté absolue de la volonté. "
        "{plan.2}Dans l'épisode trois, Spinoza, Freud et les sciences humaines viendront la contester. "
        "{-tab_chr}{plan.3}Dans l'épisode quatre, nous verrons qu'on peut, peut-être, devenir libre : avec les stoïciens, Spinoza encore, "
        "et Kant. {plan.4}Dans l'épisode cinq, la liberté descendra dans la rue : l'État, la loi, la société. "
        "{plan.5}Et dans l'épisode six, nous mettrons tout cela au service de ta copie.",
        ("P", 0.8),
    ], vis={
        "q_pb": dict(type="question", t="Sommes-nous vraiment libres ?"),
        "sens": dict(type="mot", t="« Je me sens libre »", g="l'expérience de chaque instant", y=260, taille=84),
        "desc": dict(type="portrait", annee=1596, legende="Méditations · Principes", img="descartes", nom="René Descartes", dates="1596 – 1650",
                     x=110, y=120, w=330, h=420),
        "c_desc": dict(type="cit", a="Descartes", o="Principes de la philosophie, I, 39 (1644 ; trad. 1647)", x=500, y=170, w=680),
        "causes": dict(type="nuage", items=["mes gènes", "mon éducation", "mon milieu", "mon cerveau", "mes désirs cachés"],
                       centre="CAUSES"),
        "tab_eth": dict(type="tableau", img="t-ethica", fond=True, de=[1.0, 0.5, 0.3], a=[1.3, 0.5, 0.45], sombre=True,
                        legende="Spinoza, Ethica, dans les Opera posthuma, 1677"),
        "tab_chr": dict(type="tableau", img="t-christine", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.4, .62, .62],
                        legende="Nils Forsberg, Descartes à la cour de la reine Christine (d'après P.-L. Dumesnil), XIXᵉ siècle"),
        "spino": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      x=110, y=120, w=330, h=420, legende="Lettre 58 à Schuller, octobre 1674"),
        "lance": dict(type="illu", nom="lance", x=545, y=140, w=730, h=480),
        "q2": dict(type="question", t="Sentiment d'être libre… ou ignorance des causes ?"),
        "plan": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · Le libre arbitre : Descartes, Sartre",
            "Ép. 3 · Une illusion ? Spinoza, Freud, les sciences humaines",
            "Ép. 4 · Se libérer : les stoïciens, Spinoza, Kant",
            "Ép. 5 · Libres ensemble : l'État, la loi, la société",
            "Ép. 6 · La liberté à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le sens premier. L'homme libre s'appartient : "
        "il n'est pas l'instrument d'un autre.",
        "{rec.2}Deux : faire ce que je veux, ce n'est pas vouloir librement. Hobbes d'un côté ; Platon et Rousseau de l'autre.",
        "{rec.3}Trois : il y a trois libertés. D'agir, de vouloir, et politique.",
        "{rec.4}Quatre : trois repères. Obligation et contrainte. Nécessaire et contingent. En droit et en fait.",
        "{-rec}{frise}Maintenant, à toi : quelques questions t'attendent sous la vidéo.",
        ("Et la prochaine fois… nous entrerons dans la tête de Descartes.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-frise}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LA LIBERTÉ", branches=[
            dict(t="Le sens premier", items=["s'appartenir", "ne pas être l'instrument d'un autre", "Aristote"]),
            dict(t="Faire ≠ vouloir", items=["Hobbes : l'absence d'obstacles", "Platon, Rousseau : l'esclave de ses désirs"]),
            dict(t="Trois libertés", items=["d'agir", "de vouloir (libre arbitre)", "politique"]),
            dict(t="Trois repères", items=["contrainte / obligation", "nécessaire / contingent", "en droit / en fait"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Platon", d=-428, img="platon"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Épictète", d=50, img="epictete"), dict(nom="Descartes", d=1596, img="descartes"),
            dict(nom="Hobbes", d=1588, img="hobbes"), dict(nom="Spinoza", d=1632, img="spinoza"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Marx", d=1818), dict(nom="Freud", d=1856), dict(nom="Sartre", d=1905)]),
        "tab_fin": dict(type="tableau", img="t-liberte-peuple", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .35], legende="Eugène Delacroix, La Liberté guidant le peuple, 1830"),
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
    "Photographies et documents : Klenze, l'Acropole (1846) ; manuscrit Clarke de Platon (895, Bodleian) ; Du contrat social (1762) ; Van Gogh, La Ronde des prisonniers (1890) ; Fabritius, Le Chardonneret (1654) ; mur de Berlin, 1977 (G. Garrigues, CC BY-SA 3.0) ; Doré, Londres (1872) ; Spinoza, Ethica (1677) ; Marx par J. Mayall ; Hiérapolis (B. Gagnon, CC BY-SA 3.0) ; relief d'affranchissement de Mariemont (Ad Meskens, CC BY-SA 4.0) ; esclaves enchaînés, Ashmolean (Jun, CC BY-SA 2.0) ; Shibuya (Benh Lieu Song, CC BY-SA 2.0) ; Rodin, Le Penseur (Jebulon, CC0) ; Foltz, Périclès (Rijksmuseum) ; salle d'examen ; foule et téléphones (Rawpixel, CC BY 2.0) : domaine public sauf mention",
    "Tableaux : Delacroix, La Liberté guidant le peuple (1830) ; Raphaël, L'École d'Athènes (1509-1511) ; Abraham Bosse, frontispice du Léviathan (1651) ; J.-L. David, La Mort de Socrate (1787) ; J. W. Waterhouse, Les Danaïdes (1906) ; J.-J.-F. Le Barbier, Déclaration des droits de l'homme et du citoyen (1789) ; Claude Lorrain, Caprice avec les ruines du Forum (v. 1634) ; Piranèse, Prisons imaginaires (1761) ; J.-P. Houël, La Prise de la Bastille (1789) ; W. Blake, Newton (1795-1805) ; N. Forsberg, Descartes et la reine Christine (XIXᵉ s.) : domaine public",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
