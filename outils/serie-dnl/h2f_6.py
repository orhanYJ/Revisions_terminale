"""Histoire · « Les régimes totalitaires » — édition française de la série vidéo, épisode 6 : « Des ambitions
hégémoniques » (partie III.1 du cours, « Les ambitions hégémoniques des régimes totalitaires »).

Traduction et adaptation de h2_6.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
histoire-géographie classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes
visuels, mêmes repères, mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 10 Lebensraum, conquérir l'Est · 18 impérialisme japonais (Mandchourie) · 25 Stresa, Wehrmacht, accord naval ·
       27 Éthiopie · 28 Rhénanie · 29 Axe Rome-Berlin, guerre d'Espagne · 32 Nankin · 33 Anschluss
Contenu : partie III.1 du chapitre dans le site (neuf idées), la carte du cours « L'expansion autoritaire dans les années
1930 », le premier sujet de documents du chapitre (« La Doctrine du fascisme ») et son corrigé résumé, la grille de
synthèse du cours (bloc « Enjeux internationaux », proposé ici à partir de la partie III.1), la grande question du
chapitre (premier argument, en paragraphe).
Hors du cours, dit comme tel : le calendrier des sanctions de la SDN (votées en octobre 1935, appliquées le 18 novembre ;
l'embargo pétrolier débattu jusqu'au printemps 1936 et jamais adopté). Corrections reprises de l'édition anglaise :
l'armée allemande franchit la frontière autrichienne le 12 mars 1938, Hitler entre à Vienne le 14 ; le chapitre
« Politique orientale » de Mein Kampf est dans le second volume (1926) ; l'Axe du 25 octobre 1936 dit comme un accord.
Adaptations : DBQ 1 a) « How useful » → analyse de document (présenter, situer, expliquer, intérêt et limites, bilan
critique) ; key issue de l'oral → la grande question du chapitre, en réponse à une question problématisée.
Citations en traduction française : Himmler (journal, 1919), Mein Kampf (« Politique orientale »), extraits de
« La Doctrine du fascisme » : traductions au plus près de la version anglaise citée par le cours.
Chaîne : outils/serie-philo/generer.py h2f_6 ; sortie dans dnl/serie/ (h2f-6.*).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-6"
NOTION = "Les régimes totalitaires"
NUM = 6
TITRE = "Des ambitions hégémoniques"
SUIVANT = "Épisode 7 · L'apaisement et la marche à la guerre"
PRONONCIATION = {"Lebensraum": "Lé-benss-raoum", "Mein Kampf": "Maïne Kammpf", "Drang nach Osten": "Drang nar Osstenn",
                 "Anschluss": "Anne-chlouss", "Ratzel": "Rat-tsel", "Himmler": "Himm-leur", "Wehrmacht": "Vèr-markt",
                 "Scipione l'africano": "Chi-pio-né la-fri-ca-no", "Gentile": "Djenn-ti-lé",
                 "Enciclopedia Italiana": "Ènn-tchi-clo-pé-dia I-ta-lia-na", "Kuomintang": "Kouo-minn-tang",
                 "Mao Zedong": "Mao Dzé-dong", "Lytton": "Li-tonne", "Moukden": "Mouk-dènn", "Friedrich": "Fri-drich",
                 "SDN": "èss-dé-ène", "SS": "èss-èss"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture6", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Le douze mars mille neuf cent trente-huit. Les troupes allemandes entrent en Autriche. "
        "Deux jours plus tard, Hitler entre à Vienne en triomphe.",
        "{-q1}{q2}C'est l'image que le cours a choisie pour ouvrir la partie trois. Parce qu'elle pose la vraie question. "
        "Cette agression était-elle un accident ? Ou était-elle inscrite dans les régimes eux-mêmes ?",
        "{-q2}{q3}L'Italie en Afrique. L'Allemagne en Europe. Le Japon en Chine. Dans les années trente, trois régimes partent à la conquête. "
        "Alors pourquoi la guerre était-elle si centrale dans ce qu'ils croyaient ?",
        "{-q3}{-g0}{plan}Voici le plan. {plan.1}D'abord, la décennie des agressions, sur la carte. {plan.2}Puis l'idée clé : la guerre comme valeur. "
        "{plan.3}Première étude de cas : l'Éthiopie. {plan.4}Puis le Lebensraum, la notion clé, et Mein Kampf. "
        "{plan.5}Puis le Japon, avec la deuxième étude de cas : Nankin. {plan.6}Et de l'entraînement : une analyse de document, et un paragraphe de question problématisée.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[33]),
        "q1": dict(type="question", t="12 mars 1938 : l'Anschluss.", bande=True),
        "q2": dict(type="question", t="Un accident… ou le programme du régime ?", bande=True),
        "q3": dict(type="question", t="Pourquoi la guerre était-elle si centrale pour ces régimes ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 6 · partie III.1 du cours", items=[
            "La décennie des agressions sur la carte : 1931 – 1938", "La guerre : une valeur centrale des régimes",
            "Étude de cas 1 : l'Éthiopie, 1935 – 1936", "Le Lebensraum et Mein Kampf : conquérir l'Est",
            "Le Japon : autarcie, race… et l'étude de cas 2, Nankin", "Entraînement : analyse de document et paragraphe"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 6", t="Des ambitions hégémoniques",
                      sous="Partie III.1 · l'Éthiopie · le Lebensraum · le Japon · Nankin"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="decennie1", chap="Une décennie d'agressions : 1931-1936", fond="nuit", humeur="tension",
         retenir="1931 : le Japon en Mandchourie · 1935 : réarmement allemand, Stresa · oct. 1935 – mai 1936 : l'Italie conquiert l'Éthiopie · 7 mars 1936 : la Rhénanie.",
         beats=[
        "{g1}Suivons d'abord l'histoire sur la carte. {g1.1}Elle commence en Asie. En mille neuf cent trente et un, le Japon occupe la Mandchourie, "
        "dans le nord-est de la Chine. Il veut ses céréales, et ses minerais. La Société des Nations proteste. "
        "Alors le Japon quitte tout simplement la SDN, en mille neuf cent trente-trois.",
        "{g1.2}Passons à l'Europe, en mille neuf cent trente-cinq. L'Allemagne réarme ouvertement, et la Wehrmacht est créée. "
        "En avril, à Stresa, le Royaume-Uni et la France tentent de garder Mussolini à leurs côtés contre Hitler. "
        "Nous reviendrons sur Stresa dans le prochain épisode.",
        "{g1.3}Octobre mille neuf cent trente-cinq. L'Italie envahit l'Éthiopie, qu'on appelle aussi l'Abyssinie. Elle attaque depuis ses colonies d'Érythrée et de Somalie. "
        "En mai mille neuf cent trente-six, ses troupes entrent dans la capitale, Addis-Abeba. La SDN débat. Elle ne fait rien qui compte.",
        "{g1.4}Et le sept mars mille neuf cent trente-six, les troupes allemandes entrent en Rhénanie. "
        "Elle était démilitarisée depuis le traité de Versailles. La France et le Royaume-Uni ne réagissent pas. Le pari de Hitler est gagné.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[18, 25, 27, 28]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="decennie2", chap="Une décennie d'agressions : 1936-1938", fond="nuit", humeur="tension",
         retenir="25 oct. 1936 : l'Axe Rome-Berlin ; l'Espagne, 1936-1939 · 1937 : le Japon attaque la Chine ; déc. 1937 : Nankin · 12 mars 1938 : l'Anschluss.",
         beats=[
        "{g2}{g2.1}Mille neuf cent trente-six. Les agresseurs se rapprochent. Le vingt-cinq octobre, l'Allemagne et l'Italie concluent un accord : "
        "l'Axe Rome-Berlin. En Espagne, la guerre civile a éclaté. Les deux dictateurs envoient de l'aide au général Franco.",
        "{g2.2}Mille neuf cent trente-sept. Le Japon attaque le reste de la Chine. En décembre, son armée prend Nankin. "
        "Pendant des semaines, elle massacre civils et prisonniers.",
        "{g2.3}Et le douze mars mille neuf cent trente-huit : notre image d'ouverture. L'armée allemande entre en Autriche, "
        "et l'Autriche disparaît. C'est l'Anschluss.",
        "{-g2}{fr1}Voici donc les dates de cet épisode. {fr1.1}Mille neuf cent trente et un : la Mandchourie. {fr1.2}Octobre mille neuf cent trente-cinq : l'Éthiopie est envahie. "
        "{fr1.3}Mars mille neuf cent trente-six : la Rhénanie. {fr1.4}Octobre mille neuf cent trente-six : l'Axe. {fr1.5}Décembre mille neuf cent trente-sept : Nankin. "
        "{fr1.6}Mars mille neuf cent trente-huit : l'Anschluss. Mets la vidéo en pause si tu as besoin de les recopier.",
        ("P", 3.0),
        "{-fr1}Le cours résume l'Europe sur une seule carte : l'expansion autoritaire dans les années trente. "
        "{exp}{exp.1}L'Allemagne prend la Rhénanie en mille neuf cent trente-six. Puis l'Anschluss, et les Sudètes, en mille neuf cent trente-huit. "
        "{exp.2}L'Italie conquiert l'Éthiopie, entre mille neuf cent trente-cinq et trente-six. "
        "{exp.3}Et l'Espagne est en guerre civile de mille neuf cent trente-six à trente-neuf, avec les deux dictateurs impliqués. "
        "Les Sudètes, ce sera pour l'épisode sept.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[29, 32, 33]),
        "fr1": dict(type="frise", items=[
            dict(nom="Mandchourie", d=1931, q="Japon"), dict(nom="Éthiopie", d=1935, q="octobre : Italie"),
            dict(nom="Rhénanie", d=1936, q="7 mars : Allemagne"), dict(nom="L'Axe", d=1936, q="25 octobre"),
            dict(nom="Nankin", d=1937, q="décembre : Japon"), dict(nom="Anschluss", d=1938, q="12 mars")]),
        "exp": dict(type="liste", titre="La carte du cours · l'expansion autoritaire dans les années 1930", items=[
            "Allemagne : Rhénanie 1936 · Anschluss 1938 · Sudètes 1938", "Italie : invasion de l'Éthiopie (Abyssinie), 1935 – 1936",
            "Espagne : guerre civile, 1936 – 1939"], x=170, y=150, w=940),
    }),

    # ================================================================ III. la guerre, valeur centrale (idée 1)
    dict(id="valeur", chap="La guerre : une valeur centrale", fond="guerre", humeur="tension",
         retenir="La guerre n'est pas un accident mais une valeur centrale : le fascisme la glorifie, le nazisme a besoin d'espace vital, le militarisme japonais voit l'expansion comme une mission. L'agression au-dehors prolonge le régime au-dedans.",
         beats=[
        "{q4}Passons au cours, idée par idée. Voici la question de cette partie. Pourquoi le recours à la guerre était-il si fondamental pour ces régimes ?",
        "{-q4}{def1}Le cours donne une réponse claire. La guerre n'était pas un accident de la politique totalitaire. "
        "C'était l'une de ses valeurs centrales. {def1.1}Et la réponse se trouve dans les idéologies elles-mêmes.",
        "{-def1}{trois}{trois.1}Le fascisme glorifie la guerre comme l'épreuve suprême d'un peuple. "
        "{trois.2}Le nazisme fait de la conquête d'un espace vital une condition de la survie de la race. "
        "{trois.3}Et le militarisme japonais présente l'expansion comme une mission.",
        "{trois.4}L'agression à l'extérieur est donc le prolongement logique des régimes construits à l'intérieur. "
        "Repense aux épisodes quatre et cinq. Un homme nouveau formé pour le combat. Une nation en armes. Des ennemis partout. "
        "Un régime bâti pour la lutte à l'intérieur cherchera la lutte à l'extérieur.",
        "{-trois}{photo1}Voilà pourquoi le cours ouvre la partie avec l'Anschluss, en mars mille neuf cent trente-huit. "
        "Hitler réalise ici, à l'extérieur, le programme qu'il avait annoncé dans Mein Kampf, dès mille neuf cent vingt-cinq : "
        "réunir tous les Allemands dans un seul Reich. Et s'étendre.{-photo1}",
    ], vis={
        "q4": dict(type="question", t="Pourquoi la guerre était-elle si fondamentale pour ces régimes ?"),
        "def1": dict(type="def", cles=["accident", "valeurs centrales"], terme="La guerre : une valeur centrale",
                     t="La guerre n'était pas un accident de la politique totalitaire, mais l'une de ses valeurs centrales.",
                     etape="La réponse se trouve dans les idéologies elles-mêmes", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="Trois idéologies, trois raisons de faire la guerre", cles=["épreuve suprême", "espace vital", "mission"], items=[
            "Le fascisme : la guerre, épreuve suprême d'un peuple", "Le nazisme : l'espace vital, condition de la survie de la race",
            "Le militarisme japonais : l'expansion comme mission", "L'agression à l'extérieur = le régime de l'intérieur, prolongé"], x=170, y=140, w=940),
        "photo1": dict(type="tableau", img="h2-anschluss", de=[1.0, .5, .5], a=[1.12, .5, .4],
                       legende="Hitler s'adresse à la foule sur la Heldenplatz, Vienne, 15 mars 1938 · Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE"),
    }),

    # ================================================================ IV. l'Éthiopie (idée 2)
    dict(id="abyssinie", chap="Étude de cas 1 · L'Éthiopie", fond="nuit", humeur="tension",
         retenir="Mussolini se sert du passé de Rome pour justifier un empire : la Libye (dès 1911-1912), puis l'Éthiopie, l'un des deux seuls États africains indépendants. Scipione l'africano (1937). Invasion en oct. 1935 ; Addis-Abeba, mai 1936.",
         beats=[
        "{photo2}{def2}Première étude de cas : l'Éthiopie. L'idéologie fasciste fait de la guerre une valeur centrale. Et cela entraîne l'Italie dans une politique étrangère agressive. "
        "{def2.1}Pour la justifier, Mussolini puise dans un passé glorieux : l'Empire romain.",
        "{-def2}{-photo2}{g4}{g4.1}{eth}{eth.1}D'abord, la Libye. L'Italie avait commencé à la coloniser pendant la guerre italo-turque de mille neuf cent onze et douze. "
        "Mussolini achève cette colonisation, brutalement. "
        "{eth.2}Puis il attaque l'Abyssinie, c'est-à-dire l'Éthiopie. C'était l'un des deux seuls États encore indépendants en Afrique. "
        "{eth.3}L'invasion commence en octobre mille neuf cent trente-cinq. {eth.4}En mai mille neuf cent trente-six, les troupes italiennes entrent dans Addis-Abeba. "
        "Et Mussolini proclame un empire, au nom de Rome.",
        "{-eth}{-g4}{film}La propagande prépare le terrain. {film.1}Mussolini finance un film historique, Scipione l'africano : Scipion l'Africain. "
        "Il sort en mille neuf cent trente-sept, et raconte la victoire de Rome sur Hannibal de Carthage. En Afrique. "
        "{film.2}Le message est clair. Rome avait conquis l'Afrique une fois. L'Italie fasciste le refera.",
        "Garde ce schéma en tête. Il revient sans cesse dans les années trente. "
        "{-film}{motif}{motif.g}D'abord, une justification idéologique. {motif.d}Ensuite, une invasion.",
    ], vis={
        "photo2": dict(type="tableau", img="h2-mussolini", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Benito Mussolini, Duce de l'Italie fasciste, années 1930 · Keystone, domaine public"),
        "def2": dict(type="def", cles=["valeur centrale", "Empire romain"], terme="Le fascisme et le passé de Rome",
                     t="La guerre comme valeur centrale → une politique étrangère agressive.",
                     etape="Mussolini se sert de l'Empire romain pour justifier ses ambitions", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H2", sc=[27]),
        "eth": dict(type="liste", titre="L'Italie en Afrique", x=740, y=80, w=500, petit=True, bande=True, items=[
            "La Libye : colonisée dès 1911 – 1912", "L'Éthiopie : l'un des deux États africains libres",
            "Octobre 1935 : l'invasion", "Mai 1936 : Addis-Abeba ; un « empire »"]),
        "film": dict(type="note", terme="Scipione l'africano · 1937", cles=["Hannibal", "Afrique"],
                     t="Un film historique financé par Mussolini : la victoire de Rome sur Hannibal.",
                     etape="Une propagande au service des ambitions fascistes en Afrique", x=170, y=200, w=940),
        "motif": dict(type="cols", g="1 · Justifier", gq="une idéologie : la gloire de Rome", d="2 · Envahir",
                      dq="l'Éthiopie, octobre 1935", vs="→", repere="Le schéma des années 1930"),
    }),

    # ================================================================ V. faiblesse italienne, impuissance de la SDN (idée 3)
    dict(id="sdn", chap="Un empire faible, une SDN impuissante", fond="nuit", humeur="calme",
         retenir="L'Italie : une puissance de second rang, un empire faible. La SDN : inefficace sans les grandes puissances ; elle gagne du temps (oct. 1935 – mai 1936) et ses sanctions excluent le pétrole.",
         beats=[
        "{cols1}L'Éthiopie révèle deux faiblesses à la fois. {cols1.g}La première est celle de l'Italie elle-même. En Europe, l'Italie reste une puissance de second rang. "
        "Son empire est faible et mal administré. Il n'a rien de comparable aux empires britannique et français. "
        "{cols1.d}La seconde faiblesse est celle de la Société des Nations. La conquête montre que la SDN est impuissante "
        "dès que les grandes puissances ne soutiennent pas ses décisions.",
        "{-cols1}{fr2}Regarde le calendrier. {fr2.1}Octobre mille neuf cent trente-cinq : l'Italie envahit. "
        "{fr2.2}D'octobre au mois de mai suivant, la SDN réfléchit à la question des sanctions. "
        "{fr2.3}Mai mille neuf cent trente-six : Addis-Abeba tombe. Sept mois. Exactement le temps qu'il a fallu à l'Italie pour conquérir le pays.",
        "{-fr2}{petrole}Et les sanctions finalement votées laissent de côté un produit : le pétrole. "
        "{petrole.1}Or c'était le seul produit qui aurait pu arrêter l'armée italienne. Ses camions et ses avions en dépendaient.",
        "{-petrole}{prec}Voici une précision hors du cours. La SDN vote rapidement des sanctions limitées, en octobre mille neuf cent trente-cinq. "
        "Elles s'appliquent à partir du dix-huit novembre. {prec.1}Ce qu'elle continue de débattre jusqu'au printemps mille neuf cent trente-six, c'est un embargo sur le pétrole. "
        "Et elle ne l'adopte jamais. Dans ta copie, écris donc : des sanctions sans le pétrole, et un embargo pétrolier débattu sans fin.",
        "{-prec}{mot1}Pour les dictateurs, la leçon est simple. L'agression paie.",
        ("P", 1.5),
    ], vis={
        "cols1": dict(type="cols", g="L'Italie", gq="une puissance de second rang ; un empire faible, mal administré", d="La Société des Nations",
                      dq="inefficace sans le soutien des grandes puissances", vs="+"),
        "fr2": dict(type="liste", titre="Sept mois : la SDN gagne du temps", cles=["sanctions", "Sept mois"], items=[
            "Octobre 1935 : l'Italie envahit l'Éthiopie", "Octobre 1935 – mai 1936 : la SDN réfléchit aux sanctions",
            "Mai 1936 : Addis-Abeba tombe · sept mois"], x=170, y=150, w=940),
        "petrole": dict(type="def", cles=["pétrole"], terme="Des sanctions… sans le pétrole",
                        t="Les sanctions finalement votées excluent le pétrole.",
                        etape="Le seul produit qui aurait pu arrêter l'armée italienne", x=170, y=200, w=940),
        "prec": dict(type="note", terme="Une précision · hors du cours", cles=["octobre", "embargo"],
                     t="Des sanctions limitées votées en octobre 1935, appliquées à partir du 18 novembre.",
                     etape="Ce qui est débattu jusqu'au printemps 1936 : l'embargo pétrolier, jamais adopté", x=170, y=200, w=940),
        "mot1": dict(type="mot", t="L'agression paie", g="La leçon de l'Éthiopie, pour tous les dictateurs", y=260, taille=90),
    }),

    # ================================================================ VI. Lebensraum (idée 4)
    dict(id="lebensraum", chap="Le Lebensraum · la notion clé", fond="guerre", humeur="mystere",
         retenir="Lebensraum (notion clé) : Ratzel (1901), une nation a besoin de son propre territoire et de ses propres ressources pour survivre (autarcie). La colonne vertébrale de la vision nazie du monde. Himmler, 1919 : « vivre ma vie à l'Est ».",
         beats=[
        "{mot2}Passons à l'Allemagne. Et à l'une des deux notions clés du chapitre : le Lebensraum. L'espace vital.",
        "{-mot2}{def4}{def4.1}C'est la théorie selon laquelle une nation a besoin de son propre territoire et de ses propres ressources pour survivre. "
        "Elle vient d'un géographe allemand, Friedrich Ratzel, en mille neuf cent un. "
        "{def4.2}Pour Ratzel, les nations doivent se suffire à elles-mêmes, en ressources et en territoire. C'est ainsi qu'elles peuvent se protéger des menaces extérieures.",
        "{-def4}{auta}Cette suffisance a un nom : l'autarcie. Une économie qui cherche à ne dépendre de personne. "
        "Souviens-toi du chapitre un. Après mille neuf cent vingt-neuf, le monde entier ferme ses marchés. "
        "L'autarcie devient le rêve de tous les régimes militaristes.",
        "{-auta}{g5}{g5.1}Les nazis font d'une théorie géographique un programme de conquête. Le Lebensraum devient la colonne vertébrale "
        "de la vision nazie du monde, et il guide leur politique étrangère. Le rêve est ancien. "
        "Dès mille neuf cent dix-neuf, Heinrich Himmler, le futur chef de la SS, écrit dans son journal qu'il voudrait un jour{-g5}",
        ("C", "vivre ma vie à l'Est et mener mes combats en Allemand, loin de la belle Allemagne", "c_him"),
        "{-c_him}{him}Himmler écrit cela en mille neuf cent dix-neuf. Il n'a pas vingt ans. {him.d}Vingt ans plus tard, à la tête de la SS, "
        "il sera l'un des hommes qui exécutent ce plan à l'Est.",
    ], vis={
        "mot2": dict(type="mot", t="Lebensraum", g="« l'espace vital » · notion clé du chapitre", y=250, taille=110),
        "def4": dict(type="def", cles=["territoire", "ressources", "survivre"], terme="Lebensraum · Friedrich Ratzel, 1901",
                     t="La théorie selon laquelle une nation a besoin de son propre territoire et de ses propres ressources pour survivre.",
                     etape="Se suffire en ressources et en territoire, contre les menaces extérieures", x=170, y=200, w=940),
        "auta": dict(type="def", cles=["personne"], terme="L'autarcie",
                     t="Une économie qui cherche à ne dépendre de personne.",
                     etape="Après 1929 : un monde qui ferme ses marchés (chapitre 1)", x=170, y=200, w=940),
        "g5": dict(type="globe", code="H2", sc=[10]),
        "c_him": dict(type="cit", a="Heinrich Himmler, futur chef de la SS", o="journal, 1919 (traduction)", x=200, y=190, w=880),
        "him": dict(type="cols", g="1919 · un rêve", gq="le journal d'un jeune homme : « vivre ma vie à l'Est »", d="1939 – 1945 · un plan",
                    dq="le chef de la SS l'exécute à l'Est (chapitre 3)", vs="→"),
    }),

    # ================================================================ VII. Mein Kampf (idée 5)
    dict(id="meinkampf", chap="Mein Kampf : conquérir l'Est", fond="guerre", humeur="tension",
         retenir="Mein Kampf (1925-1926), « Politique orientale » (vol. 2) : conquérir les terres slaves, y installer des Allemands en race de seigneurs, déporter les Russes en Sibérie, réduire les autres en esclavage. Une vieille devise : Drang nach Osten.",
         beats=[
        "{nt1}Hitler fait de l'espace vital un plan. Mein Kampf paraît en mille neuf cent vingt-cinq. "
        "Dans le second volume, tout un chapitre lui est consacré : Politique orientale. Hitler y annonce{-nt1}",
        ("C", "une politique orientale, au sens de l'acquisition du sol nécessaire à notre peuple allemand", "c_mk"),
        "{-c_mk}{plan2}Qu'est-ce que cela veut dire, concrètement ? {plan2.1}Étendre l'Allemagne aux nations slaves. "
        "{plan2.2}Y installer des Allemands, en race de seigneurs. {plan2.3}Déporter la plupart des Russes en Sibérie. "
        "{plan2.4}Et utiliser les autres comme main-d'œuvre esclave.",
        "{-plan2}{drang}L'idée elle-même n'était pas neuve. {drang.1}Au dix-neuvième siècle, la poussée vers l'Est était déjà une devise du nationalisme allemand : "
        "Drang nach Osten. La poussée vers l'Est. "
        "{drang.2}Ce qui est nouveau, c'est que Hitler en fait le centre de la politique de l'État.",
        "Garde cela en tête pour le chapitre trois. {-drang}{lien}{lien.g}Dans les années vingt, c'est un programme, écrit dans un livre. "
        "{lien.d}En juin mille neuf cent quarante et un, avec l'opération Barbarossa, il devient une guerre d'anéantissement à l'Est.",
    ], vis={
        "nt1": dict(type="note", terme="Mein Kampf · 1925 – 1926", cles=["Politique orientale"],
                    t="Volume 2 (1926) : tout un chapitre consacré à l'espace vital, « Politique orientale ».", x=170, y=470, w=940),
        "c_mk": dict(type="cit", a="Adolf Hitler", o="Mein Kampf, vol. 2 (1926), « Politique orientale » (traduction)", x=200, y=150, w=880),
        "plan2": dict(type="liste", titre="Le plan pour l'Est", cles=["slaves", "seigneurs", "Sibérie", "esclave"], items=[
            "Étendre l'Allemagne aux nations slaves", "Y installer des Allemands en race de seigneurs",
            "Déporter la plupart des Russes en Sibérie", "Utiliser les autres comme main-d'œuvre esclave"], x=170, y=140, w=940),
        "drang": dict(type="def", cles=["devise", "centre"], terme="Drang nach Osten · « la poussée vers l'Est »",
                      t="Une devise du nationalisme allemand du XIXe siècle.",
                      etape="Hitler en fait le centre de la politique de l'État", x=170, y=200, w=940),
        "lien": dict(type="cols", g="1925 – 1926 · un livre", gq="Mein Kampf annonce la conquête de l'Est", d="1941 · une guerre",
                     dq="Barbarossa : une guerre d'anéantissement (chapitre 3)", vs="→"),
    }),

    # ================================================================ VIII. le Japon : l'autarcie (idée 6)
    dict(id="japon1", chap="Le Japon (1) : la dimension économique", fond="nuit", humeur="tension",
         retenir="L'impérialisme japonais, côté économique : la crise de 1929 frappe le commerce japonais → l'autarcie ; une population qui augmente, une industrie qui manque de matières premières et d'espace. La Mandchourie dès 1931 : céréales et minerais.",
         beats=[
        "{q5}Le troisième impérialisme du cours n'est pas européen. C'est celui du Japon. Et il a deux dimensions. D'abord, l'économie.",
        "{-q5}{g6}{eco}{eco.1}La Grande Dépression de mille neuf cent vingt-neuf frappe durement le commerce japonais. "
        "Dans les années trente, elle fait naître un désir d'autarcie économique. {eco.2}L'expansion répond à deux besoins. D'abord, ceux d'une population qui augmente. "
        "{eco.3}Ensuite, ceux d'une industrie qui manque de matières premières, et d'espace. "
        "{eco.4}La conquête est donc présentée comme la solution à une crise. Une crise aggravée par la fermeture des marchés mondiaux.",
        "{-eco}{g6.1}L'exemple le plus clair, c'est la Mandchourie. À partir de mille neuf cent trente et un, le Japon occupe cette région du nord-est de la Chine. "
        "Pourquoi ? Pour ses riches terres à céréales, et ses réserves de minerais. C'est le motif économique, dans sa forme la plus simple.",
    ], vis={
        "q5": dict(type="question", t="Le Japon : pourquoi conquérir ?"),
        "g6": dict(type="globe", code="H2", sc=[18]),
        "eco": dict(type="liste", titre="La dimension économique", x=40, y=100, w=520, petit=True, bande=True, items=[
            "1929 : la Dépression frappe le commerce japonais → l'autarcie", "Une population qui augmente",
            "Une industrie qui manque de matières premières et d'espace", "La conquête vendue comme remède à la crise"]),
    }),

    # ================================================================ IX. le Japon : la race (idée 7)
    dict(id="japon2", chap="Le Japon (2) : la dimension raciale", fond="nuit", humeur="mystere",
         retenir="Le Japon, côté racial : une « race supérieure » destinée à diriger l'Asie ; le panasiatisme, un « ordre nouveau en Asie orientale ». Le ressentiment : clause d'égalité raciale rejetée en avril 1919. Hirohito en uniforme ; le soleil levant.",
         beats=[
        "{def7}La seconde dimension est raciale. L'impérialisme japonais est nourri par un fort sentiment de supériorité raciale. "
        "{def7.1}Son nom : le panasiatisme. Le Japon se voit comme une race asiatique supérieure. Il devrait donc, selon lui, libérer les territoires asiatiques "
        "de l'impérialisme occidental. Et construire un ordre nouveau en Asie orientale, sous direction japonaise.",
        "Derrière cela, il y a un ressentiment. La puissance industrielle et militaire du Japon dans le Pacifique grandit. "
        "Et pourtant le Japon se sent méprisé par les puissances occidentales. {-def7}{res}{res.g}La preuve vient de la conférence de la paix de Paris, en avril mille neuf cent dix-neuf. "
        "Les puissances occidentales rejettent la clause d'égalité raciale proposée par le Japon. "
        "{res.d}Et cela, alors même que le Japon reçoit les îles allemandes du Pacifique, sous mandat de la SDN, en mille neuf cent vingt.",
        "{-res}{symb}Le militarisme grandit donc avec un nationalisme puissant. Regarde maintenant les symboles. "
        "{symb.1}L'empereur Hirohito est représenté en uniforme militaire. "
        "{symb.2}Et le drapeau au soleil levant est le pavillon de la Marine impériale. "
        "{symb.3}Tu vois le parallèle avec l'Europe ? Comme le fascisme et le nazisme, le militarisme japonais mêle un sentiment de supériorité "
        "à l'humiliation de la paix de mille neuf cent dix-neuf.",
    ], vis={
        "def7": dict(type="def", cles=["supérieure", "libérer", "ordre nouveau"], terme="Le panasiatisme",
                     t="Le Japon, race asiatique supérieure, doit libérer l'Asie de l'impérialisme occidental.",
                     etape="… et construire un « ordre nouveau en Asie orientale » sous direction japonaise", x=170, y=200, w=940),
        "res": dict(type="cols", g="Rejeté", gq="avril 1919 : la clause d'égalité raciale refusée par l'Occident", d="Récompensé",
                    dq="1920 : les îles allemandes du Pacifique sous mandat de la SDN", vs="≠", repere="Une grande puissance pleine de ressentiment"),
        "symb": dict(type="liste", titre="Militarisme et nationalisme", cles=["uniforme", "pavillon", "humiliation"], items=[
            "L'empereur Hirohito représenté en uniforme militaire", "Le drapeau au soleil levant : pavillon de la Marine impériale",
            "Comme en Europe : supériorité + humiliation de 1919"], x=170, y=150, w=940),
    }),

    # ================================================================ X. Nankin (idée 8)
    dict(id="nankin1", chap="Étude de cas 2 · Nankin : une agression que rien n'arrête", fond="guerre", humeur="tension",
         retenir="Incident de Moukden (1931), mis en scène → la Mandchourie ; la commission Lytton ; le Japon quitte la SDN (1933) ; pas de riposte militaire américaine ; la guerre civile chinoise (Kuomintang contre Mao) → 1937 : le reste de la Chine attaqué.",
         beats=[
        "{def8}Deuxième étude de cas : Nankin. Sa leçon tient en une phrase. L'agression a grandi, parce que personne ne l'a arrêtée.",
        "{-def8}{fr3}Suis les étapes. {fr3.1}Mille neuf cent trente et un : l'incident de Moukden. Une explosion sur une voie ferrée exploitée par les Japonais. "
        "Elle a été mise en scène par l'armée japonaise elle-même, et sert de prétexte pour envahir la Mandchourie. "
        "{fr3.2}La SDN envoie une commission d'enquête : la commission Lytton. "
        "{fr3.3}La réponse du Japon ? Il quitte tout simplement la SDN, en mille neuf cent trente-trois. "
        "{fr3.4}Et en mille neuf cent trente-sept, le Japon attaque le reste de la Chine.",
        "{-fr3}{pk}Pourquoi le Japon a-t-il osé ? {pk.1}Parce que les Japonais ont compris que les États-Unis ne riposteraient pas militairement. "
        "{pk.2}Et parce que la Chine était déchirée par une guerre civile. D'un côté, les nationalistes de Tchang Kaï-chek, le Kuomintang. "
        "De l'autre, les communistes de Mao Zedong. {pk.3}Exactement comme pour l'Éthiopie : des adversaires faibles, et un monde qui regarde.",
        "{-pk}{g7}{g7.1}Décembre mille neuf cent trente-sept. L'armée japonaise prend Nankin. Pendant des semaines, jusqu'en janvier mille neuf cent trente-huit, "
        "elle tue civils et prisonniers. Un journal japonais a même raconté un concours de meurtres entre deux officiers, "
        "comme s'il s'agissait d'un sport. Le titre : Un record incroyable.",
    ], vis={
        "def8": dict(type="def", cles=["personne"], terme="Étude de cas 2 · Nankin",
                     t="L'agression a grandi parce que personne ne l'a arrêtée.", x=170, y=220, w=940),
        "fr3": dict(type="frise", items=[
            dict(nom="Incident de Moukden", d=1931, q="prétexte mis en scène"), dict(nom="Commission Lytton", d=1932, q="enquête de la SDN"),
            dict(nom="Le Japon quitte la SDN", d=1933, q=""), dict(nom="Guerre contre la Chine", d=1937, q="le reste de la Chine")]),
        "pk": dict(type="liste", titre="Pourquoi le Japon a osé", cles=["États-Unis", "guerre civile", "regarde"], items=[
            "Les États-Unis ne riposteraient pas militairement", "La Chine divisée par la guerre civile : le Kuomintang (Tchang Kaï-chek) contre les communistes de Mao",
            "Comme pour l'Éthiopie : des adversaires faibles, un monde qui regarde"], x=170, y=150, w=940),
        "g7": dict(type="globe", code="H2", sc=[32]),
    }),

    # ================================================================ XI. Nankin annonce la guerre mondiale (idée 9)
    dict(id="nankin2", chap="Nankin annonce la guerre mondiale", fond="guerre", humeur="tension",
         retenir="Nankin (déc. 1937 – janv. 1938) concentre les traits de la guerre : idéologie raciste, expansionnisme, militarisme, civils pris pour cibles. ≈ 200 000 (tribunal de Tokyo) à 300 000 (Chine) tués. Une raison de dater la guerre de 1937.",
         beats=[
        "{q6}Pourquoi Nankin est-il une étude de cas ? Parce qu'il concentre ce que deviendra la guerre mondiale.",
        "{-q6}{trait}Il montre quatre traits. {trait.1}Une idéologie violente et raciste. {trait.2}L'expansionnisme et le militarisme. "
        "{trait.3}Une forte hausse du niveau de violence. {trait.4}Et des civils comptés parmi les objectifs militaires. "
        "Garde ces quatre traits en tête. Tu les retrouveras tous en Europe après mille neuf cent trente-neuf.",
        "{-trait}{bilan}Combien de victimes ? {bilan.g}Environ deux cent mille, selon le tribunal de Tokyo pour les crimes de guerre, après la guerre. "
        "{bilan.d}Trois cent mille, selon le chiffre retenu par la Chine. {bilan.1}Le débat est un sujet en soi. "
        "Il reste politiquement sensible entre les deux pays. Dans une copie, donne la fourchette.",
        "{-bilan}{date}Et une dernière conséquence. {date.1}Nankin est l'une des raisons pour lesquelles certains historiens font commencer "
        "la Seconde Guerre mondiale en mille neuf cent trente-sept, plutôt qu'en mille neuf cent trente-neuf. {date.2}En Asie, la guerre avait déjà commencé. "
        "Ce débat ouvre le chapitre trois.",
    ], vis={
        "q6": dict(type="question", t="Pourquoi Nankin est-il une étude de cas ?"),
        "trait": dict(type="liste", titre="Nankin : les traits de la guerre à venir", cles=["raciste", "militarisme", "violence", "civils"], items=[
            "Une idéologie violente et raciste", "L'expansionnisme et le militarisme",
            "Une forte hausse du niveau de violence", "Des civils parmi les objectifs militaires"], x=170, y=140, w=940),
        "bilan": dict(type="cols", g="≈ 200 000", gq="le tribunal de Tokyo pour les crimes de guerre", d="≈ 300 000",
                      dq="le chiffre retenu par la Chine", vs="–", repere="Civils et prisonniers tués · un débat toujours sensible"),
        "date": dict(type="def", cles=["1937", "1939"], terme="Quand la guerre a-t-elle commencé ?",
                     t="Nankin est l'une des raisons de dater le début de la guerre de 1937 plutôt que de 1939.",
                     etape="En Asie, la guerre avait déjà commencé · chapitre 3", x=170, y=200, w=940),
    }),

    # ================================================================ XII. la grille de synthèse
    dict(id="grille", chap="Remplir la grille : les enjeux internationaux", fond="aube", humeur="calme",
         retenir="Expansion : Italie → l'empire de Rome, la Libye, l'Éthiopie · Allemagne → le Lebensraum à l'Est · Japon → la Mandchourie, la Chine. Sentiment de supériorité : la gloire de Rome · la race des seigneurs · la race asiatique « supérieure ».",
         beats=[
        "{gr}Tu te souviens de la grille de synthèse du cours, vue dans l'épisode trois ? Son bloc Enjeux internationaux a deux lignes, encore vides. "
        "Avec cette partie, tu peux les remplir. {gr.1}Première ligne : la volonté d'expansion. Pour l'Italie, un empire au nom de Rome : la Libye, puis l'Éthiopie. "
        "{gr.2}Pour l'Allemagne, le Lebensraum : la conquête de l'Est, annoncée dans Mein Kampf. "
        "{gr.3}Deuxième ligne : le sentiment de supériorité. L'Italie se voit en héritière de Rome. L'Allemagne, en race de seigneurs face aux Slaves.",
        "{gr.4}Et la colonne soviétique ? Cette partie du cours ne dit rien de l'expansion soviétique. Garde-la pour l'épisode sept, "
        "et le pacte d'août mille neuf cent trente-neuf. À la place, le cours ajoute un troisième agresseur : le Japon, avec son autarcie, et sa race supérieure.",
    ], vis={
        "gr": dict(type="liste", titre="La grille du cours · enjeux internationaux (proposition, d'après la partie III.1)", petit=True, items=[
            "Volonté d'expansion · Italie : l'empire de Rome ; la Libye, puis l'Éthiopie (1935 – 1936)",
            "Volonté d'expansion · Allemagne : le Lebensraum, l'Est (Mein Kampf, 1925)",
            "Sentiment de supériorité · Italie : héritière de Rome · Allemagne : une race de seigneurs face aux Slaves",
            "URSS : rien dans la partie III.1 (voir le pacte, épisode 7) · le cours ajoute le Japon"], x=150, y=140, w=980),
    }),

    # ================================================================ XIII. l'analyse de document : La Doctrine du fascisme
    dict(id="dbq1", chap="À toi · Analyse de document : La Doctrine du fascisme", fond="aube", humeur="calme",
         retenir="Analyse de document : présenter (nature, auteur, date) · situer dans le contexte · expliquer et montrer l'intérêt · limites, puis bilan critique.",
         beats=[
        "{ex1}Maintenant, le premier sujet de documents du chapitre. Le document, c'est La Doctrine du fascisme, de Benito Mussolini, "
        "rédigée avec le philosophe Giovanni Gentile. Elle est publiée en mille neuf cent trente-deux, dans l'Enciclopedia Italiana. "
        "{ex1.d}En voici quatre formules. Seule la guerre porte au maximum de tension toutes les énergies humaines. "
        "Le pacifisme est le masque d'un renoncement lâche et passif. La tendance des nations à l'expansion est une manifestation de leur vitalité. "
        "Et : pour le fascisme, l'État est un absolu.",
        "{ex1.1}La consigne. Montrez ce que ce document apprend à un historien sur le rôle de l'idéologie totalitaire "
        "parmi les causes profondes de la Seconde Guerre mondiale, puis portez un regard critique sur ce document.",
        "{-ex1}{str}La démarche, comme toujours. {str.1}D'abord, présenter le document : sa nature, son auteur, sa date. "
        "{str.2}Puis le situer dans son contexte. {str.3}Ensuite, l'expliquer et montrer son intérêt, avec plusieurs arguments. "
        "{str.4}Enfin, ses limites, avec plusieurs arguments, avant un bilan critique.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}Voici un modèle, d'après le cours. {rep1.1}Ce document est la doctrine officielle du fascisme italien, rédigée par Mussolini avec Giovanni Gentile "
        "et publiée en mille neuf cent trente-deux. La guerre, l'État absolu et l'expansion impériale y sont présentés comme la substance même du régime. "
        "{rep1.2}On peut annoncer le bilan dès le départ : ce document est très utile pour étudier l'idéologie totalitaire comme cause de la guerre. "
        "Mais il prouve l'intention bien mieux qu'il ne prouve la causalité.",
    ], vis={
        "ex1": dict(type="exo", niveau="dbq", titre="Montrez ce que le document A apprend sur le rôle de l'idéologie totalitaire parmi les causes profondes de la Seconde Guerre mondiale, puis portez un regard critique sur ce document.",
                    src="Document A : Mussolini (avec Giovanni Gentile), « La Doctrine du fascisme », Enciclopedia Italiana, 1932 (traduction)",
                    donnees=["« Seule la guerre porte au maximum de tension toutes les énergies humaines »",
                             "le pacifisme, « le masque d'un renoncement lâche et passif »",
                             "« la tendance des nations à l'expansion », une « manifestation de leur vitalité »",
                             "« pour le fascisme, l'État est un absolu »"]),
        "str": dict(type="liste", titre="L'analyse de document : la démarche", cles=["présenter", "situer", "intérêt", "limites"], items=[
            "Présenter le document : nature, auteur, date", "Le situer dans son contexte",
            "L'expliquer et montrer son intérêt : plusieurs arguments", "Ses limites : plusieurs arguments, puis un bilan critique"], x=150, y=130, w=980),
        "pa1": dict(type="pause", t="Analyse de document : que nous apprend La Doctrine du fascisme sur l'idéologie comme cause profonde de la guerre ?",
                    sous="Présentation, contexte, intérêt, limites, bilan. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "rep1": dict(type="liste", titre="Un modèle de réponse · le début", petit=True, items=[
            "Présentation : la doctrine officielle du fascisme, Mussolini et Gentile, Enciclopedia Italiana, 1932",
            "Bilan annoncé : très utile… il prouve l'intention mieux que la causalité"],
                     x=150, y=150, w=980),
    }),

    # ================================================================ XIV. l'analyse de document : intérêt et limites
    dict(id="dbq1b", chap="La Doctrine du fascisme : intérêt et limites", fond="aube", humeur="calme",
         retenir="Intérêt : la voix même du régime ; la guerre et l'expansion comme valeurs. Limites : l'intention, pas l'action (l'Italie en guerre en juin 1940) ; une date, un régime ; aucune cause économique.",
         beats=[
        "{at}Passons à l'intérêt. {at.1}D'abord, son statut. Il est écrit par le chef du régime lui-même, comme article d'encyclopédie. "
        "Ce n'est donc pas une opinion fasciste parmi d'autres. C'est la définition officielle d'une idéologie d'État par elle-même. "
        "{at.2}Ensuite, il affirme sans détour le lien entre idéologie et guerre. La guerre porte au maximum toutes les énergies humaines. Le pacifisme est une lâcheté. "
        "La guerre n'est donc pas un moyen de la politique. C'est une valeur en soi. "
        "{at.3}Troisième argument : il fait de cette valeur un programme. La tendance à l'expansion est un signe de vitalité. "
        "L'impérialisme devient un devoir de santé nationale. Et cela explique l'Éthiopie, en mille neuf cent trente-cinq. "
        "{at.4}Quatrième argument : l'État est absolu, et la démocratie rejetée. Un tel régime ne pouvait pas vivre dans l'ordre libéral de mille neuf cent dix-neuf. "
        "{at.5}Et cinquième : c'est de la propagande, mais ici ce n'est pas une faiblesse. C'est une preuve tout à fait fiable de ce que le régime voulait montrer.",
        "{-at}{li}Passons aux limites. {li.1}D'abord, une doctrine est une déclaration d'intention. Ce n'est pas le récit d'une action. "
        "L'Italie n'entre en guerre qu'en juin mille neuf cent quarante, et Mussolini hésite pendant des mois. "
        "{li.2}Ensuite, sa date. C'est un instantané de mille neuf cent trente-deux, avant la guerre d'Éthiopie, et avant l'Axe. "
        "{li.3}Puis, sa portée. Il ne concerne qu'un seul régime. Rien sur l'idéologie raciale nazie, sur le Lebensraum, ni sur le militarisme japonais. "
        "Or ce sont ces deux puissances qui ont réellement ouvert la guerre, en mille neuf cent trente-sept et en mille neuf cent trente-neuf. "
        "{li.4}Quatrième limite : il ignore les causes économiques. Le krach de mille neuf cent vingt-neuf, le nationalisme économique, l'autarcie. "
        "{li.5}Cinquième : il est écrit pour être publié. Il montre la doctrine que le régime voulait afficher, pas ce que les Italiens croyaient réellement.",
        "{-li}{ccl}{ccl.1}D'où le bilan critique. Le document est très utile : il prouve qu'un régime a inscrit la guerre dans sa doctrine officielle, bien avant mille neuf cent trente-neuf. "
        "{ccl.2}Mais il n'est qu'en partie utile pour mesurer à quel point l'idéologie a causé la guerre. Confronte-le à Mein Kampf, et à un document économique.",
    ], vis={
        "at": dict(type="liste", titre="Intérêt · plusieurs arguments", petit=True, items=[
            "Statut : la définition officielle du régime par lui-même, par le Duce en personne",
            "La guerre, une valeur en soi : « maximum de tension » ; le pacifisme, une lâcheté",
            "L'expansion comme devoir : « vitalité » → l'Éthiopie, 1935",
            "« L'État est un absolu » : incompatible avec l'ordre libéral de 1919",
            "Propagande = preuve fiable de ce que le régime professait"], x=150, y=110, w=980),
        "li": dict(type="liste", titre="Limites · plusieurs arguments", petit=True, items=[
            "L'intention, pas l'action : l'Italie en guerre seulement en juin 1940",
            "Une date : 1932, avant l'Éthiopie et l'Axe",
            "Un seul régime : ni Lebensraum, ni Japon",
            "Aucune cause économique : 1929, nationalisme économique, autarcie",
            "Écrit pour être affiché, pas ce que croyaient les Italiens"], x=150, y=110, w=980),
        "ccl": dict(type="cols", g="Très utile", gq="la guerre inscrite dans une doctrine officielle, bien avant 1939",
                    d="Utile en partie seulement", dq="pour mesurer la causalité : ajouter Mein Kampf et un document économique", vs="mais"),
    }),

    # ================================================================ XV. paragraphe de réponse à la grande question du chapitre
    dict(id="essai", chap="À toi · un paragraphe de question problématisée", fond="aube", humeur="calme",
         retenir="Argument 1 : les totalitarismes font de la guerre une valeur, de l'expansion un but — l'Éthiopie 1935 (Rome), le Lebensraum (Ratzel 1901, Mein Kampf 1925), le Japon (Mandchourie 1931, Nankin 1937). Nuance : les démocraties laissent faire.",
         beats=[
        "{ex2}Un dernier exercice. C'est la grande question du chapitre. "
        "Quel rôle les régimes totalitaires ont-ils joué dans l'effondrement de la paix mondiale à la fin des années trente ?",
        "{ex2.1}Tu répondras à toute la question dans l'épisode huit. Aujourd'hui, rédige seulement le premier argument. "
        "Un paragraphe, qui montre comment les idéologies totalitaires ont fait de la guerre une valeur et de l'expansion un but. Trois régimes, trois exemples.",
        "{-ex2}{pa2}",
        ("P", 2.0),
        "{-pa2}{mod}Voici un paragraphe modèle. {mod.1}Les idéologies totalitaires ont été une cause décisive de l'effondrement de la paix, "
        "parce qu'elles ont fait de la guerre une valeur et de l'expansion un but. "
        "{mod.2}Le fascisme glorifie la guerre comme l'épreuve suprême d'un peuple. En octobre mille neuf cent trente-cinq, l'Italie envahit l'Éthiopie, "
        "et justifie la conquête par le passé de l'Empire romain. "
        "{mod.3}Le nazisme fait de l'espace vital une condition de la survie de la race. De la théorie de Ratzel, en mille neuf cent un, "
        "Hitler tire un plan dans Mein Kampf : conquérir l'Est, et asservir les Slaves. "
        "{mod.4}Et le militarisme japonais associe l'autarcie et la supériorité raciale : la Mandchourie en mille neuf cent trente et un, puis Nankin, en décembre mille neuf cent trente-sept. "
        "{mod.5}Et la phrase de transition : pourtant, ces ambitions n'ont réussi que parce que personne ne les a arrêtées. C'est l'argument suivant. "
        "Et le prochain épisode.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Quel rôle les régimes totalitaires ont-ils joué dans l'effondrement de la paix mondiale à la fin des années 1930 ?",
                    src="Grande question du chapitre · argument 1 seulement", enonce=["Un paragraphe : les idéologies ont fait de la guerre une valeur et de l'expansion un but"]),
        "pa2": dict(type="pause", t="Rédige l'argument 1 : comment les idéologies totalitaires ont-elles fait de la guerre une valeur et de l'expansion un but ?",
                    sous="Une idée directrice, trois régimes, un exemple précis pour chacun. Mets en pause, rédige, puis relance."),
        "mod": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "Idée directrice : les idéologies ont fait de la guerre une valeur et de l'expansion un but",
            "Le fascisme → l'Éthiopie, octobre 1935, au nom de Rome",
            "Le nazisme → le Lebensraum : Ratzel (1901), Mein Kampf (1925)",
            "Le Japon → autarcie et race : Mandchourie 1931, Nankin 1937",
            "Transition : … elles ont réussi parce que personne ne les a arrêtées"], x=150, y=120, w=980),
    }),

    # ================================================================ récap
    dict(id="recap6", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}La guerre était une valeur centrale. C'était le prolongement logique, à l'extérieur, des régimes construits à l'intérieur. "
        "{carte.2}L'Éthiopie : le passé de Rome, utilisé pour justifier un empire, d'octobre mille neuf cent trente-cinq à mai mille neuf cent trente-six. "
        "Une Italie faible, une SDN impuissante, et des sanctions sans le pétrole. "
        "{carte.3}Le Lebensraum : Ratzel en mille neuf cent un. Himmler en mille neuf cent dix-neuf. Mein Kampf en mille neuf cent vingt-cinq. Le but : conquérir l'Est. "
        "{carte.4}Et le Japon : l'autarcie, et une race supérieure. La Mandchourie en mille neuf cent trente et un. Et Nankin en mille neuf cent trente-sept, qui annonce la guerre mondiale.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : l'apaisement, et la marche à la guerre. De Stresa à Munich et à Prague. "
        "Pourquoi les démocraties ont-elles cédé, jusqu'en septembre mille neuf cent trente-neuf ?",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="AMBITIONS HÉGÉMONIQUES", branches=[
            dict(t="La guerre, valeur centrale", items=["fascisme : l'épreuve suprême", "nazisme : l'espace vital", "Vienne, 12 mars 1938"]),
            dict(t="L'Éthiopie", items=["le passé de Rome · Scipion", "oct. 1935 – mai 1936", "SDN : pas de sanctions sur le pétrole"]),
            dict(t="Le Lebensraum", items=["Ratzel, 1901 · autarcie", "Mein Kampf, 1925", "Drang nach Osten"]),
            dict(t="Le Japon · Nankin", items=["autarcie · Mandchourie 1931", "panasiatisme · 1919", "Nankin, déc. 1937"])]),
        "fin": dict(type="mot", t="Ensuite : la marche à la guerre", g="Épisode 7 · l'apaisement, Munich, septembre 1939", y=270, taille=72),
    }),
]

QUIZ = [
    dict(q="D'après le cours, qu'était la guerre pour les régimes totalitaires ?",
         r=["L'une de leurs valeurs centrales, le prolongement logique du régime à l'intérieur", "Un accident imposé par les démocraties",
            "Un dernier recours après l'échec de la diplomatie", "Une nécessité purement économique"], ok=0, voir="def1",
         ex="Le fascisme glorifie la guerre, le nazisme a besoin d'espace vital, le militarisme japonais voit l'expansion comme une mission."),
    dict(q="Comment Mussolini justifie-t-il la conquête de l'Éthiopie ?",
         r=["Par le passé de l'Empire romain", "Par le besoin d'espace vital à l'Est", "Par le panasiatisme",
            "Par un mandat de la SDN"], ok=0, voir="def2",
         ex="Il finance même le film Scipione l'africano (1937), sur la victoire de Rome sur Hannibal."),
    dict(q="Quel produit les sanctions de la SDN contre l'Italie laissent-elles de côté ?",
         r=["Le pétrole", "Le blé", "Le charbon", "Les armes"], ok=0, voir="petrole",
         ex="Le pétrole aurait pu arrêter l'armée italienne ; l'embargo pétrolier a été débattu, jamais adopté."),
    dict(q="Qui a formulé la théorie du Lebensraum, et quand ?",
         r=["Le géographe Friedrich Ratzel, en 1901", "Hitler, dans Mein Kampf (1925)", "Himmler, en 1919",
            "Mussolini, en 1932"], ok=0, voir="def4",
         ex="Hitler a fait de la théorie de Ratzel un plan de conquête dans Mein Kampf, chapitre « Politique orientale »."),
    dict(q="Que prévoyait la « Politique orientale » de Hitler pour les Russes ?",
         r=["Déporter la plupart d'entre eux en Sibérie et utiliser les autres comme main-d'œuvre esclave", "En faire des alliés égaux de l'Allemagne",
            "Les laisser en paix en échange de pétrole", "En faire des citoyens allemands"], ok=0, voir="plan2",
         ex="Des Allemands devaient s'installer sur les terres slaves en race de seigneurs ; la vieille devise était Drang nach Osten."),
    dict(q="Pourquoi le Japon occupe-t-il la Mandchourie à partir de 1931, d'après le cours ?",
         r=["Pour ses terres à céréales et ses minerais", "Pour la protéger de l'Union soviétique",
            "Pour répondre à une demande de la SDN", "Pour combattre uniquement les communistes de Mao"], ok=0, voir="g6",
         ex="La dimension économique : l'autarcie, après que la crise de 1929 a frappé le commerce japonais."),
    dict(q="Qu'ont rejeté les puissances occidentales à la conférence de la paix de Paris, en avril 1919 ?",
         r=["La clause d'égalité raciale proposée par le Japon", "La revendication italienne sur l'Éthiopie", "La revendication allemande sur l'Autriche",
            "La création de la SDN"], ok=0, voir="res",
         ex="Une source de ressentiment japonais, alors même que le Japon reçoit en 1920 les îles allemandes du Pacifique sous mandat."),
    dict(q="Pourquoi Nankin est-il une raison de faire commencer la Seconde Guerre mondiale en 1937 ?",
         r=["Il montre déjà une idéologie raciste, une violence extrême et des civils pris pour cibles", "Ce fut la première victoire allemande",
            "Les États-Unis déclarèrent la guerre au Japon juste après", "Il mit fin à la SDN"], ok=0, voir="date",
         ex="≈ 200 000 (tribunal de Tokyo) à 300 000 (Chine) civils et prisonniers tués, déc. 1937 – janv. 1938."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », partie III.1 « Les ambitions hégémoniques des régimes totalitaires », avec la carte « L'expansion autoritaire dans les années 1930 », le sujet de documents sur « La Doctrine du fascisme » et son corrigé, la grille de synthèse et la grande question du chapitre, tel qu'il est rédigé sur le site ; les lignes « Enjeux internationaux » de la grille sont proposées par cette vidéo ; carte animée du chapitre 2 (site).",
    "Hors du cours : les sanctions de la SDN contre l'Italie sont votées en octobre 1935 et appliquées à partir du 18 novembre 1935 ; l'embargo pétrolier est débattu jusqu'au printemps 1936 et jamais adopté.",
    "Citations en traduction française : Heinrich Himmler (journal, 1919) ; Adolf Hitler, Mein Kampf, vol. 2 (1926) ; Benito Mussolini et Giovanni Gentile, « La Doctrine du fascisme » (1932).",
    "Photographies (via Wikimedia Commons) : Hitler sur la Heldenplatz, Vienne, 15 mars 1938 (Bundesarchiv, Bild 183-1987-0922-500, CC BY-SA 3.0 DE) ; Benito Mussolini, années 1930 (Keystone, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
