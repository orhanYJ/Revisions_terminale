"""SVT, chapitre 2 : « La complexification des génomes » — la vidéo du chapitre (thème 1.A).

Même chaîne que les vidéos de physique-chimie (outils/serie-pc/pc_ch5.py) : generer.py svt_ch2, sortie dans svt/serie/.
Contenu : les pages t2 (transferts horizontaux de gènes) et t2b (endosymbioses) du site, rien au-delà ; ce que le site
marque « hors programme » est dit comme tel à l'oral. Que du contenu : aucune mention scolaire ni personnelle.
Plan : la carte mentale du thème (svt/carte-mentale.js) : c2a Transferts horizontaux (★ schéma à savoir refaire),
c2b Endosymbioses (★ chloroplastes / mitochondries).
Animations du site rejouées : svt/anim/thg.html (62 s), insuline.html (50 s), endosymbiose.html (62 s).
Illustrations propres au chapitre : svt/serie/illu-svt-ch2.js (griffith, grille, barres, lignee).
"""

SITE = "svt"
CODE = "svt-ch2"
NOTION = "La complexification des génomes"
NUM = 2
TITRE = "La complexification des génomes"
RYTHME = "vivant"   # silences variables selon la fin de phrase (generer.py, _ecart_vivant)
SUIVANT = "Chapitre 3 · L'évolution du génome au sein des populations"
PRONONCIATION = {
    "ADN-T": "a-dé-ène-té", "ADN": "a-dé-ène", "ARN": "a-ère-ène", "MSRV": "ème-èsse-ère-vé", "VIH": "vé-i-ache",
    "OGM": "o-jé-ème", "ENV": "eu-ène-vé", "OMS": "o-ème-èsse", "NCBI": "ène-cé-bé-i", "pTi": "pé-té-i",
    "ENW1": "eu-ène-double-vé-un", "ERVW-1": "eu-ère-vé-double-vé-un", "16S": "seize-èsse", "18S": "dix-huit-èsse",
    "RubisCo": "Rubisco", "Griffith": "Griffite", "Avery": "Évéri", "Agrobacterium": "Agrobactériomme",
    "tumefaciens": "tuméfaciennse", "Klebsiella": "Klébsiéla", "Margulis": "Margulisse", "Geniegen2": "Génigène deux",
    "Chlorobium": "Klorobiomme", "Nostoc": "Nostok", "Futura-Sciences": "Futura Sciences", "Bordas": "Bordasse",
    "Nathan": "Natan", "R": "ère", "S": "èsse",
}


SCENES = [
    # ================================================================ ouverture : la carte du thème, puis le chapitre 2
    dict(id="ouverture", chap="Ouverture", fond="foret", humeur="mystere", carton=False, beats=[
        "{carte}Voici la carte mentale du thème un, partie A : génétique et évolution. Quatre chapitres.",
        "Le premier parlait des transferts verticaux. Les gènes passent des parents aux enfants, par la reproduction. "
        "Et à chaque génération, la méiose et la fécondation les brassent.",
        "{carte.1}Chapitre deux : la complexification des génomes. Et là, la question change de direction.",
        "Un gène peut-il passer d'un être vivant à un autre qui n'est ni son parent, ni son enfant, ni même de la même espèce ?",
        ("P", 0.8),
        "La réponse est oui. Et ça se passe partout dans le vivant !",
        "Une bactérie donne à sa voisine un gène de résistance aux antibiotiques. "
        "Un gène de virus devient, chez nous, indispensable au placenta.",
        "Et des bactéries entières, avalées il y a très longtemps, sont devenues les mitochondries et les chloroplastes de nos cellules.",
        "{-carte}{plan}{plan.1}Sur la carte, le chapitre a deux branches. La première : les transferts horizontaux de gènes.",
        ("Transformation, conjugaison, transgenèse, transferts viraux, transduction. Elle porte une étoile : un schéma à savoir refaire.", {"rate": "+5%"}),
        "{plan.2}La seconde : les endosymbioses, avec les chloroplastes et les mitochondries. Une étoile, elle aussi.",
        "{plan.3}Et à la fin, on fait le point sur ce qu'il faut savoir rédiger pour le bac.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "carte": dict(type="mental", vers=["t1a", "c2"], pousse=True),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les transferts horizontaux de gènes : bactéries, transgenèse, virus ★",
            "Les endosymbioses : chloroplastes et mitochondries ★",
            "Pour le bac : ce qu'il faut savoir rédiger et dessiner"], x=150, y=190, w=980),
        "titre": dict(type="titre", sur="SVT · Thème 1 · Chapitre 2", t="La complexification des génomes",
                      sous="Transferts horizontaux et endosymbioses, avec leurs exemples"),
    }),

    # ================================================================ A. le problème : vertical / horizontal
    dict(id="probleme", chap="Vertical ou horizontal", fond="foret", humeur="lumiere",
         retenir="Transfert horizontal : un organisme incorpore le matériel génétique d'un organisme non apparenté. Il est possible parce que l'ADN et le code génétique sont universels.",
         beats=[
        "{ma}Première branche : les transferts horizontaux de gènes. {ma.1}Repartons du chapitre un.",
        "{-ma}{univ}Les brassages créent de la diversité. Les accidents de la méiose aussi.",
        "Mais est-ce que ça suffit à expliquer toute la diversité génétique du vivant ? Non.",
        "Une propriété de l'ADN ouvre une autre voie. {univ.1}Il est universel.",
        "Même molécule chez tous les êtres vivants, lue partout avec le même code génétique. "
        "Un gène peut donc passer d'un organisme à un autre, sans lien de parenté, et continuer à s'y exprimer.",
        "{-univ}{vh}Comparons les deux transferts. {vh.1}Entre qui ?",
        "Le transfert vertical va des parents aux descendants. "
        "L'horizontal se fait entre organismes contemporains, sans lien de descendance, parfois d'espèces très éloignées.",
        "{vh.2}Par quel moyen ? Le vertical passe par la reproduction. L'horizontal, par la transformation, la conjugaison, la transgenèse ou les virus.",
        "{vh.3}Et qu'est-ce qui les rend possibles ? D'un côté, la méiose et la fécondation. De l'autre, l'universalité de l'ADN et du code génétique.",
        ("P", 0.8),
        ("{-vh}{def_th}La définition, à apprendre mot pour mot. Le transfert horizontal de gènes, aussi appelé transfert latéral, "
         "est un processus au cours duquel un organisme incorpore le matériel génétique d'un autre organisme non apparenté.", {"rate": "-4%"}),
        "{def_th.1}Il s'oppose au transfert vertical, héréditaire, des parents vers les enfants.",
        "{-def_th}{pb}D'où la question du chapitre.",
        ("P", 2.0),
    ], vis={
        "ma": dict(type="mental", vers=["c2", "c2a"]),
        "univ": dict(type="def", terme="Au-delà des transferts verticaux", cles=["universel", "code"],
                     t="Les brassages et les accidents de la méiose ne suffisent pas à expliquer toute la diversité génétique du vivant.",
                     etape="L'ADN est universel, lu partout avec le même code génétique : un gène peut passer d'un organisme à un autre et s'y exprimer.",
                     x=150, y=200, w=980),
        "vh": dict(type="illu", nom="grille", x=90, y=110, w=1100, h=540, fs=29, larg=[1, 2, 2],
                   cols=["", "Transfert vertical", "Transfert horizontal"], rows=[
                       ["Entre qui ?", "Des parents à leurs descendants", "Entre organismes contemporains, non apparentés, parfois d'espèces très éloignées"],
                       ["Par quel moyen ?", "La reproduction (sexuée ou asexuée)", "Transformation, conjugaison, transgenèse, virus"],
                       ["Ce qui le permet", "La méiose et la fécondation (ou la mitose)", "L'universalité de l'ADN et du code génétique"]]),
        "def_th": dict(type="def", terme="Transfert horizontal de gènes", cles=["incorpore", "apparenté"],
                       t="Processus au cours duquel un organisme incorpore le matériel génétique d'un autre organisme non apparenté.",
                       etape="Il s'oppose au transfert vertical, héréditaire, des parents vers les enfants.", x=150, y=190, w=980),
        "pb": dict(type="question", t="Comment des gènes passent-ils d'un organisme à un autre sans reproduction ? En quoi cela complexifie-t-il les génomes ?"),
    }),

    # ================================================================ B. Griffith
    dict(id="griffith", chap="Griffith, 1928", fond="cellule", humeur="mystere",
         retenir="Griffith : des pneumocoques R non virulents deviennent virulents au contact de S tués. Quelque chose est passé : le « facteur transformant », qui est l'ADN.",
         beats=[
        "{tab_pn}La première preuve d'un transfert horizontal ? Elle date de mille neuf cent vingt-huit.",
        "Frederick Griffith étudie le pneumocoque. Une bactérie souvent présente sans symptômes dans le nez et la gorge, "
        "mais qui peut provoquer des pneumonies ou des méningites.",
        "{-tab_pn}{souches}Il en existe deux souches. {souches.1}La souche R, pour rough, rugueuse : sans capsule, non virulente.",
        "{souches.2}La souche S, pour smooth, lisse : entourée d'une capsule, virulente.",
        "{-souches}{gr}Griffith injecte des pneumocoques à des souris, en quatre lots. {gr.1}Lot un : des S vivants. La souris meurt.",
        "{gr.2}Lot deux : des R vivants. La souris survit. {gr.3}Lot trois : des S tués par la chaleur. La souris survit.",
        "{gr.4}Et lot quatre : un mélange de S tués et de R vivants. Regarde bien. La souris meurt !",
        "{gr.5}Et dans son sang, on retrouve des pneumocoques S. Vivants.",
        "{-gr}{pa_gr}Avant l'explication, arrête-toi. Explique le lot quatre, avec les lots deux et trois comme témoins.",
        "{pa_gr.stop}{-pa_gr}{gr2}{gr2.1}{gr2.2}{gr2.3}{gr2.4}{gr2.5}Voici le raisonnement. Aucun des deux ingrédients du lot quatre n'est mortel seul : "
        "les lots deux et trois le montrent.",
        "Des S ressuscités ? Impossible. Ce sont donc des R qui ont acquis la capacité de fabriquer une capsule. "
        "Et ils la transmettent à leur descendance.",
        "{-gr2}{fact}Quelque chose est passé des S morts aux R vivants. Griffith l'appelle le facteur transformant.",
        "{fact.1}Ce facteur, c'est l'ADN. Mais Griffith ne le sait pas encore.",
        ("P", 0.8),
        "{-fact}{avery}Alors, qui l'a identifié ? C'est hors programme. En mille neuf cent quarante-quatre, Oswald Avery et ses collègues "
        "purifient une à une les molécules des pneumocoques S tués.",
        "Seul l'extrait d'ADN transforme les R en S. Et si on détruit l'ADN par une enzyme, il perd ce pouvoir. "
        "C'est l'une des premières preuves que l'ADN porte l'information génétique.",
        "{-avery}",
    ], vis={
        "tab_pn": dict(type="tableau", img="ch2-pneumo", fond=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                       legende="Pneumocoques (Streptococcus pneumoniae) au microscope, coloration de Gram · Arnold Kaufman, CC0"),
        "souches": dict(type="liste", titre="Deux souches de pneumocoque", items=[
            "R (rough, rugueuse) : sans capsule, non virulente",
            "S (smooth, lisse) : entourée d'une capsule, virulente"], marques=["R", "S"], x=150, y=210, w=980),
        "gr": dict(type="illu", nom="griffith", x=90, y=110, w=1100, h=520),
        "gr2": dict(type="illu", nom="griffith", x=90, y=110, w=1100, h=520),
        "pa_gr": dict(type="pause", t="Pourquoi la souris du lot 4 meurt-elle ? D'où viennent les S vivants ?",
                      sous="Mets sur pause, réponds en trois phrases, puis reprends."),
        "fact": dict(type="def", terme="Le facteur transformant", cles=["passe", "ADN"],
                     t="Quelque chose passe des pneumocoques S tués aux R vivants, et leur transmet le caractère « virulent ».",
                     etape="On sait aujourd'hui que c'est l'ADN : une transformation, un transfert horizontal.", x=150, y=200, w=980),
        "avery": dict(type="note", titre="Hors programme · Avery, 1944", cles=["ADN"],
                      t="Seul l'extrait d'ADN des S tués transforme les R en S ; détruit par une enzyme, il perd ce pouvoir.",
                      x=150, y=220, w=980),
    }),

    # ================================================================ C1. transformation et conjugaison
    dict(id="bacteries", chap="Transformation et conjugaison", fond="cellule", humeur="lumiere",
         retenir="Transformation : une bactérie intègre de l'ADN libre du milieu. Conjugaison : un plasmide est copié et transmis par un pont cytoplasmique, même entre espèces.",
         beats=[
        "{an1}{pt1}{pt1.1}{an1.1}Comment les bactéries échangent-elles des gènes ? Première façon, celle de Griffith : la transformation.",
        "Quand des cellules meurent, leur ADN se retrouve dans le milieu : les sols, les eaux, l'intestin. Ici, un pneumocoque S tué libère son ADN.",
        "{pt1.2}{an1.2}Dans certaines conditions, une bactérie absorbe cet ADN libre. Il entre, et s'intègre à son propre ADN.",
        "Le fragment porte le gène de la capsule. Résultat : la bactérie R fabrique une capsule. Elle devient virulente.",
        "{pt1.3}{an1.3}Deuxième mécanisme : la conjugaison. En plus de leur chromosome, beaucoup de bactéries possèdent de petites molécules d'ADN circulaire, "
        "les plasmides. Ils se répliquent indépendamment du chromosome.",
        "Deux bactéries se relient par un pont cytoplasmique. Le plasmide de la donneuse est copié, et la copie passe dans la receveuse.",
        "La donneuse garde le sien. Et ça marche entre bactéries de la même espèce, ou d'espèces différentes.",
        "C'est souvent ainsi que voyagent des gènes de virulence, ou de résistance aux antibiotiques. Un vrai avantage pour la bactérie qui en hérite.",
        "{-pt1}{pa_cj}C'est le schéma étoilé de la carte. À toi : refais-le de mémoire. Deux bactéries, leur chromosome, le plasmide, le pont, la copie.",
        "{pa_cj.stop}{-pa_cj}{-an1}{defs}Retiens les définitions. {defs.1}Transformation : une bactérie intègre de l'ADN libre du milieu.",
        ("{defs.2}Conjugaison : un plasmide est copié et transmis à une autre bactérie par un pont cytoplasmique.", {"rate": "-4%"}),
        "{defs.3}Et le plasmide : une petite molécule d'ADN circulaire, en plus du chromosome, qui se réplique de façon indépendante.",
        "{-defs}",
    ], vis={
        "an1": dict(type="anim", nom="thg", x=40, y=72, h=624, seg=[[0, 5], [5, 14.6], [15.4, 27]]),
        "pt1": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Un pneumocoque S tué libère son ADN dans le milieu",
            "Transformation : l'ADN libre entre dans la bactérie R et s'intègre à son ADN",
            "Conjugaison : par un pont cytoplasmique, la copie d'un plasmide passe dans la receveuse"]),
        "pa_cj": dict(type="pause", x=680, y=150, w=560, t="Refais le schéma de la conjugaison, légendé.",
                      sous="Chromosome, plasmide, pont cytoplasmique, copie, donneuse et receveuse. Puis compare avec l'animation."),
        "defs": dict(type="liste", titre="Trois mots", items=[
            "Transformation : une bactérie intègre de l'ADN libre du milieu",
            "Conjugaison : un plasmide est copié et transmis par un pont cytoplasmique",
            "Plasmide : petite molécule d'ADN circulaire, répliquée indépendamment du chromosome"], x=150, y=180, w=980),
    }),

    # ================================================================ C3. résistances aux antibiotiques
    dict(id="resistance", chap="La diffusion des résistances", fond="cellule", humeur="tension",
         retenir="L'antibiotique ne crée pas la résistance : il sélectionne les bactéries qui la possèdent. Le plasmide (≈ 1 sur 100, ≈ 80 % des résistances acquises) va bien plus vite que la mutation (≈ 1 sur 1 milliard).",
         beats=[
        "{tab_ab}Une conséquence majeure de la conjugaison : la diffusion des résistances aux antibiotiques.",
        "Sur ces boîtes de culture, des pastilles d'antibiotiques. Autour d'une pastille efficace, un halo clair : les bactéries ne poussent pas.",
        "Et sur la dernière boîte ? Plus aucun halo. Ces bactéries résistent.",
        "{-tab_ab}{meca}{meca.1}Comment résister ? Grâce à des gènes qui codent l'un de ces mécanismes. "
        "Une enzyme qui dégrade l'antibiotique, ou qui le rend inactif.",
        "{meca.2}Des pompes membranaires qui l'expulsent avant qu'il n'agisse. {meca.3}Ou une mutation du chromosome qui modifie sa cible.",
        "{-meca}{mp}Une résistance s'acquiert de deux façons. Et elles sont très inégales. "
        "{mp.1}Par mutation du chromosome : c'est un transfert vertical, transmis aux descendantes.",
        "{mp.2}Par acquisition d'un plasmide : c'est un transfert horizontal, reçu d'une autre bactérie.",
        "{mp.3}La mutation est rare : environ une bactérie sur un milliard. Le plasmide est fréquent : environ une sur cent.",
        "{mp.4}Résultat : environ quatre-vingts pour cent des résistances acquises le sont par plasmide.",
        ("P", 0.8),
        "{-mp}{an2}{pt2}{pt2.1}{an2.1}Et ensuite ? Un antibiotique arrive. Les bactéries qui portent le plasmide de résistance survivent. "
        "Celle qui ne l'a pas est éliminée.",
        "{pt2.2}Attention, c'est le raisonnement de Première, toujours valable. L'antibiotique ne crée pas la résistance. "
        "Il sélectionne les bactéries qui la possèdent déjà.",
        "N'écris jamais qu'une bactérie s'adapte, ou mute pour survivre.",
        "{pt2.3}Ce qui change ici, c'est la vitesse. Pas besoin d'attendre une mutation rare : la bactérie reçoit d'une voisine un gène qui marche déjà.",
        "{-pt2}{-an2}{part}Et ces échanges ont lieu partout. {part.1}En deux mille vingt, une étude l'a montré jusque dans la poussière de nos maisons : "
        "les bactéries s'y échangent leurs plasmides, et donc leurs résistances.",
        "{part.2}Des bactéries comme Klebsiella pneumoniae circulent entre l'environnement, les animaux d'élevage et les humains. "
        "Par contact, par l'alimentation, par les eaux usées.",
        "Et à chaque étape, un gène de résistance peut sauter d'une bactérie à une autre. Même d'une espèce à l'autre.",
        "{part.3}D'où l'inquiétude. L'usage massif des antibiotiques, en médecine comme en élevage, sélectionne les résistantes. "
        "Et la conjugaison les fait circuler très vite.",
        "On voit apparaître des bactéries multirésistantes, parfois résistantes à tout. "
        "L'Organisation mondiale de la santé en fait l'une des plus graves menaces pour la santé mondiale.",
        "{-part}",
    ], vis={
        "tab_ab": dict(type="tableau", img="ch2-antibio", de=[1.0, .5, .5], a=[1.45, .82, .78],
                       legende="Antibiogrammes de Staphylococcus aureus : halos d'inhibition, puis souche résistante · HansN., CC BY-SA 4.0"),
        "meca": dict(type="liste", titre="Comment une bactérie résiste", items=[
            "Une enzyme qui dégrade l'antibiotique, ou le rend inactif",
            "Des pompes membranaires qui l'expulsent",
            "Une mutation du chromosome qui modifie sa cible"], x=150, y=190, w=980),
        "mp": dict(type="illu", nom="grille", x=90, y=110, w=1100, h=540, fs=29, larg=[1.1, 1.6, 1.6],
                   cols=["", "Par mutation du chromosome", "Par acquisition d'un plasmide"], rows=[
                       ["Type de transfert", "Vertical : transmise aux descendantes", "Horizontal : reçue d'une autre bactérie"],
                       ["Mécanisme", "Mutation, au hasard", "Conjugaison (ou transformation)"],
                       ["Fréquence", "Rare : ≈ 1 bactérie sur 1 milliard", "Fréquente : ≈ 1 bactérie sur 100"],
                       ["Part des résistances acquises", "Minoritaire", "≈ 80 %"]]),
        "an2": dict(type="anim", nom="thg", x=40, y=72, h=624, seg=[[26.5, 30.4]]),
        "pt2": dict(type="liste", petit=True, titre="La sélection", x=680, y=120, w=560, items=[
            "L'antibiotique élimine les bactéries sans plasmide de résistance",
            "Il ne crée pas la résistance : il la sélectionne",
            "Le transfert horizontal accélère tout : un gène déjà fonctionnel, reçu d'une voisine"],
                    marques=["1", "2", "3"]),
        "part": dict(type="liste", titre="Partout, et vite", items=[
            "2020 : dans la poussière de nos maisons, les bactéries s'échangent leurs plasmides",
            "Klebsiella pneumoniae : environnement, élevages, humains, eaux usées",
            "Usage massif d'antibiotiques → bactéries multirésistantes (OMS : menace majeure)"], x=150, y=180, w=980),
    }),

    # ================================================================ C4. Agrobacterium
    dict(id="agro", chap="Agrobacterium, la transgenèse naturelle", fond="foret", humeur="mystere",
         retenir="Agrobacterium insère l'ADN-T de son plasmide pTi dans le génome d'une cellule végétale : galle et opines. C'est une transgenèse naturelle.",
         beats=[
        "{def_tg}Un mot nouveau : la transgenèse. {def_tg.1}C'est l'insertion d'un gène d'un organisme dans le génome d'un autre organisme. "
        "Elle peut être naturelle, ou réalisée par l'humain.",
        "{-def_tg}{tab_ga}Un exemple naturel : Agrobacterium tumefaciens, une bactérie du sol. Tu vois ces boules sur les branches de cet orme ?",
        "Ce sont des galles, des tumeurs végétales. Et c'est cette bactérie qui les provoque.",
        "{-tab_ga}{an3}{pt3}{pt3.1}{an3.1}Agrobacterium se fixe sur une cellule végétale. Et elle y injecte un fragment de son plasmide, le plasmide pTi. "
        "Ce fragment s'appelle l'ADN-T, pour ADN transféré.",
        "{pt3.2}L'ADN-T s'insère dans le génome chromosomique de la cellule végétale. "
        "Une bactérie vient donc de réaliser, naturellement, une transgenèse dans un organisme pluricellulaire.",
        "{pt3.3}Une fois intégrés, ces gènes bactériens s'expriment. Ils font produire à la plante des facteurs de croissance : "
        "les cellules prolifèrent, et forment la galle.",
        "Ils lui font aussi produire des opines, des molécules dont la bactérie se nourrit. La bactérie détourne la plante à son profit.",
        "{-pt3}{-an3}",
    ], vis={
        "def_tg": dict(type="def", terme="Transgenèse", cles=["insertion", "génome"],
                       t="L'insertion d'un gène d'un organisme dans le génome d'un autre organisme.",
                       etape="Naturelle (Agrobacterium) ou réalisée par l'humain (insuline, OGM).", x=150, y=200, w=980),
        "tab_ga": dict(type="tableau", img="ch2-galle", de=[1.0, .5, .5], a=[1.3, .55, .45],
                       legende="Galles du collet sur un orme, North Ayrshire (Écosse) · Rosser1954, CC BY-SA 4.0"),
        "an3": dict(type="anim", nom="thg", x=40, y=72, h=624, seg=[[31.4, 45.6]]),
        "pt3": dict(type="liste", petit=True, titre="Agrobacterium tumefaciens", x=680, y=120, w=560, items=[
            "Elle injecte l'ADN-T, fragment de son plasmide pTi, dans une cellule végétale",
            "L'ADN-T s'insère dans le génome chromosomique de la plante",
            "Ses gènes s'expriment : facteurs de croissance (galle) et opines (nourriture de la bactérie)"]),
    }),

    # ================================================================ C5. transgenèse dirigée : insuline
    dict(id="insuline", chap="La transgenèse dirigée : l'insuline", fond="cellule", humeur="lumiere",
         retenir="Gène d'intérêt → plasmide ouvert → plasmide recombinant (vecteur) → bactérie transformée → divisions → protéine humaine. Possible car le code génétique est universel.",
         beats=[
        "{pb2}Et l'humain, dans tout ça ? En quoi les transferts horizontaux ont-ils permis des applications biotechnologiques ?",
        "{-pb2}{an4}{pt4}{pt4.1}{an4.1}L'humain se sert des plasmides bactériens comme vecteurs d'un gène d'intérêt. Exemple : faire produire de l'insuline humaine par des bactéries. "
        "Première étape : on identifie le gène de l'insuline, l'hormone qui manque aux personnes diabétiques de type un.",
        "{pt4.2}{an4.2}Deuxième étape : on ouvre un plasmide bactérien. On coupe la boucle en un point précis.",
        "{pt4.3}{an4.3}Troisième étape : on y insère le gène humain. ADN du plasmide plus ADN humain : c'est un plasmide recombinant. "
        "Il sert de vecteur : il transporte le gène.",
        "{pt4.4}{an4.4}Quatrième étape : on transfère ce plasmide dans une bactérie, qui devient une bactérie transformée. "
        "Le code génétique est universel : elle lit le gène humain comme les siens, et fabrique la protéine humaine.",
        "{pt4.5}{an4.5}Cinquième étape : la bactérie se multiplie. À chaque division, le plasmide est copié, et transmis aux deux cellules filles.",
        "{pt4.6}{an4.6}Des milliards de bactéries transformées fabriquent alors de grandes quantités d'insuline humaine.",
        "{-pt4}{pa_in}Deuxième schéma de la branche étoilée. À toi : refais-le, avec ses cinq étapes et ses mots clés.",
        "{pa_in.stop}{-pa_in}{-an4}{mitose}Un point de vocabulaire. On lit parfois que les bactéries se multiplient par mitoses successives. C'est faux.",
        "La mitose, c'est la division du noyau des cellules eucaryotes. Une bactérie n'a pas de noyau. "
        "Elle réplique son ADN, puis se coupe en deux : c'est une division binaire. Écris « divisions », pas « mitoses ».",
        "{-mitose}{ogm}La transgenèse sert aussi à créer des OGM, des organismes génétiquement modifiés. "
        "{ogm.1}Pour les plantes, on se sert justement d'Agrobacterium.",
        "Dans l'ADN-T, on remplace les gènes de la tumeur par le gène que l'on veut introduire. Et la bactérie se charge de l'insérer.",
        ("P", 0.8),
        "{-ogm}{bil_a}Faisons le bilan des bactéries. {bil_a.1}Les gènes circulent entre organismes non apparentés. "
        "Par transformation, de l'ADN libre. Par conjugaison, des plasmides, à travers un pont cytoplasmique.",
        "{bil_a.2}Ils peuvent même passer dans un organisme pluricellulaire : c'est la transgenèse naturelle par Agrobacterium. "
        "{bil_a.3}Ces échanges expliquent la diffusion rapide des résistances aux antibiotiques.",
        "{bil_a.4}Et l'humain les a détournés. La transgenèse dirigée, avec un plasmide pour vecteur, fait produire une protéine humaine par une bactérie.",
        "{-bil_a}",
    ], vis={
        "pb2": dict(type="question", t="En quoi les transferts horizontaux ont-ils permis des applications biotechnologiques ?"),
        "an4": dict(type="anim", nom="insuline", x=40, y=72, h=624, seg=[[0, 7], [7, 14], [14, 21], [21, 28], [28, 39], [39, 50]], vit=1.4),
        "pt4": dict(type="liste", petit=True, titre="Produire de l'insuline humaine", x=680, y=100, w=560, items=[
            "Identifier le gène d'intérêt (insuline)", "Ouvrir un plasmide",
            "Insérer le gène : plasmide recombinant (vecteur)", "Le transférer : bactérie transformée",
            "Divisions : toutes les descendantes portent le gène", "Production d'insuline humaine"]),
        "pa_in": dict(type="pause", x=680, y=150, w=560, t="Refais le schéma de la production d'insuline par transgenèse.",
                      sous="Gène d'intérêt, plasmide ouvert, plasmide recombinant, bactérie transformée, divisions, insuline."),
        "mitose": dict(type="note", titre="Les bactéries ne font pas de mitose", cles=["noyau", "binaire"],
                       t="La mitose est la division du noyau des eucaryotes. Une bactérie, sans noyau, se divise par division binaire.",
                       x=150, y=210, w=980),
        "ogm": dict(type="def", terme="OGM", cles=["Agrobacterium"],
                    t="Organisme génétiquement modifié par transgenèse.",
                    etape="Plantes : on remplace dans l'ADN-T les gènes de la tumeur par le gène voulu.",
                    x=150, y=200, w=980),
        "bil_a": dict(type="liste", titre="Le bilan · les bactéries", items=[
            "Transformation (ADN libre) et conjugaison (plasmides, pont cytoplasmique)",
            "Transgenèse naturelle : Agrobacterium et la plante",
            "Diffusion rapide des résistances aux antibiotiques",
            "Transgenèse dirigée : un plasmide vecteur, une protéine humaine produite par des bactéries"], x=150, y=160, w=980),
    }),

    # ================================================================ D1. rétrovirus
    dict(id="retrovirus", chap="Les transferts viraux : le rétrovirus", fond="cellule", humeur="tension",
         retenir="Rétrovirus : ARN → transcription inverse → ADN intégré au génome de l'hôte. Environ 8 à 10 % du génome humain est d'origine virale.",
         beats=[
        "{chif}Changeons d'acteur : les virus. Le séquençage du génome humain a révélé une surprise. "
        "Environ huit à dix pour cent de sa séquence est d'origine virale !",
        "D'où viennent ces séquences ? De rétrovirus. Des virus capables de s'intégrer dans l'ADN de nos chromosomes.",
        "{-chif}{tab_vih}Le VIH, le virus du sida, est un rétrovirus. Ici, au microscope électronique : deux particules de VIH qui sortent d'une cellule.",
        "{-tab_vih}{an5}{pt5}{pt5.1}{an5.1}Le cycle, en quatre temps. Un : le rétrovirus pénètre dans la cellule hôte. "
        "Il y libère son génome, une molécule d'ARN simple brin.",
        "{pt5.2}Deux : cet ARN est copié en ADN double brin. C'est la transcription inverse, réalisée par une enzyme du virus.",
        "{pt5.3}{an5.2}Trois : l'ADN viral entre dans le noyau, et s'intègre au génome de la cellule hôte. C'est un transfert horizontal.",
        "{pt5.4}Quatre : la cellule transcrit cet ADN viral comme ses propres gènes. Elle fabrique de nouveaux virus, qui iront infecter d'autres cellules.",
        "{-pt5}{pa_rv}À toi : refais ce cycle de mémoire, avec les mots ARN, transcription inverse, ADN viral, intégration.",
        "{pa_rv.stop}{-pa_rv}{-an5}{virus}Attention : un virus n'est pas une bactérie. Ce n'est même pas une cellule. "
        "Il ne se reproduit qu'en faisant travailler une cellule hôte.",
        "Et c'est justement ce qui en fait un excellent vecteur de transfert horizontal. Pour se répliquer, le rétrovirus doit insérer ses gènes dans ceux de son hôte.",
        "{-virus}",
    ], vis={
        "chif": dict(type="mot", t="8 à 10 %", g="du génome humain est d'origine virale", taille=150, y=210),
        "tab_vih": dict(type="tableau", img="ch2-vih", de=[1.0, .48, .24], a=[1.12, .52, .74],
                        legende="Particules de VIH-1 bourgeonnant d'une cellule, microscopie électronique colorisée · NIAID, CC BY 2.0"),
        "an5": dict(type="anim", nom="thg", x=40, y=72, h=624, seg=[[46, 56], [56, 62]]),
        "pt5": dict(type="liste", petit=True, titre="Le cycle d'un rétrovirus", x=680, y=110, w=560, items=[
            "Il entre et libère son génome : un ARN simple brin",
            "Transcription inverse : l'ARN est copié en ADN double brin",
            "L'ADN viral s'intègre au génome de l'hôte, dans le noyau",
            "La cellule l'exprime et fabrique de nouveaux virus"]),
        "pa_rv": dict(type="pause", x=680, y=150, w=560, t="Refais le cycle d'un rétrovirus en quatre temps.",
                      sous="ARN viral, transcription inverse, ADN double brin, intégration au génome, nouveaux virus."),
        "virus": dict(type="note", titre="Un virus n'est pas une bactérie", cles=["cellule", "insérer"],
                      t="Ce n'est pas une cellule : il ne se reproduit qu'en faisant travailler une cellule hôte, en insérant ses gènes dans les siens.",
                      x=150, y=210, w=980),
    }),

    # ================================================================ D2. la syncytine
    dict(id="syncytine", chap="La syncytine", fond="foret", humeur="mystere",
         retenir="Syncytine 1 / protéine ENV du virus MSRV : 87 % de similitude, et même fonction (fusion des membranes). Le gène de la syncytine 1 est issu d'un transfert horizontal de gène viral.",
         beats=[
        "{tab_pl}L'exemple à connaître : la syncytine. {syn}Les syncytines sont des protéines du placenta.",
        "Elles font fusionner les membranes des cellules de l'embryon et des cellules de la mère. "
        "Ensemble, elles forment une couche continue : le syncytium.",
        "On les trouve chez les mammifères : primates, rongeurs, lapins, carnivores, grands ruminants. "
        "{syn.1}Chez l'humain, deux gènes : la syncytine un, appelée ENW1, sur le chromosome sept. Et la syncytine deux, sur le chromosome six.",
        "{-syn}{-tab_pl}{env}Or certains rétrovirus, comme le virus MSRV, savent faire fusionner leur enveloppe avec la membrane des cellules qu'ils infectent. "
        "{env.1}Ils utilisent des protéines de fusion, les protéines ENV, codées par un gène du virus.",
        "Protéines du virus, syncytines des primates : même fonction. Faire fusionner des membranes. Coïncidence ?",
        ("P", 0.8),
        "{-env}{crit}Pour trancher, un critère. Quand un gène est transmis verticalement, les mutations s'accumulent au fil du temps. "
        "Deux espèces éloignées devraient donc avoir des protéines très différentes.",
        ("{crit.1}Si les protéines de deux organismes éloignés se ressemblent à plus de quatre-vingts pour cent, cela trahit un transfert horizontal récent.", {"rate": "-4%"}),
        "{-crit}{bar}{bar.s}Les résultats de la comparaison. Le seuil : quatre-vingts pour cent. "
        "{bar.1}Syncytine un humaine contre protéine du virus MSRV : quatre-vingt-sept pour cent !",
        "Au-delà du seuil. Entre un virus et un primate. C'est un indice fort.",
        "{bar.2}Syncytine deux contre MSRV : vingt pour cent seulement. Loin sous le seuil. On y reviendra.",
        "{-bar}{args}Le raisonnement, en trois arguments. {args.1}Un argument moléculaire : quatre-vingt-sept pour cent de similitude entre la syncytine un et la protéine ENV.",
        "Un virus et un primate sont extrêmement éloignés. Par transfert vertical, leurs protéines n'auraient aucune raison de se ressembler autant. "
        "Cette ressemblance signe une parenté entre les deux gènes.",
        "{args.2}Un argument fonctionnel : les deux protéines font fusionner des membranes. On parle de similitude fonctionnelle. "
        "Un argument de plus, mais qui ne suffirait pas seul.",
        "{args.3}Un argument de parenté. On construit un arbre avec la syncytine un du gorille, du chimpanzé, de l'humain, de l'orang-outan, "
        "du gibbon et du babouin, plus la séquence du virus.",
        "Et la séquence virale se range tout près des syncytines des grands singes et de l'humain.",
        "{args.4}Conclusion : le gène de la syncytine un est issu d'un transfert horizontal de gène viral.",
        "{-args}{piege1}Deux pièges. {piege1.1}On ne parle pas d'analogie de structure, mais d'homologie de séquence. "
        "Des séquences si proches qu'elles signent une origine commune.",
        "Seule la ressemblance des séquences prouve la parenté. Deux protéines peuvent avoir la même fonction sans être apparentées.",
        "{-piege1}{piege2}Et la syncytine deux ? Vingt pour cent montrent seulement qu'elle ne vient pas de ce virus-là. "
        "Pas qu'elle vienne d'un transfert vertical.",
        "D'ailleurs, elle vient elle aussi d'un rétrovirus. Mais d'un autre. Conclure « transfert vertical » serait une erreur de raisonnement.",
        "{-piege2}",
    ], vis={
        "tab_pl": dict(type="tableau", img="ch2-placenta", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                       legende="Placenta humain, face fœtale · Asturnut, CC BY-SA 3.0"),
        "syn": dict(type="def", terme="Les syncytines", cles=["fusionner", "placenta"],
                    t="Protéines du placenta : elles font fusionner les membranes des cellules de l'embryon et de la mère, qui forment le syncytium.",
                    etape="Chez l'humain, deux gènes : syncytine 1 (ENW1, chromosome 7) et syncytine 2 (chromosome 6).",
                    x=150, y=150, w=980),
        "env": dict(type="cols", g="Syncytines des primates", gq="font fusionner les cellules de l'embryon et de la mère (placenta)",
                    d="Protéines ENV du virus MSRV", dq="font fusionner l'enveloppe du virus avec la cellule infectée", vs="="),
        "crit": dict(type="def", terme="Le critère des 80 %", cles=["80", "horizontal"],
                     t="Par transfert vertical, les mutations éloignent les protéines de deux espèces éloignées.",
                     etape="Plus de 80 % de ressemblance entre organismes éloignés : indice d'un transfert horizontal récent.", x=150, y=200, w=980),
        "bar": dict(type="illu", nom="barres", x=90, y=160, w=1100, h=400, bh=64, fs=27, max=100, seuil=80, unite=" %", lseuil="seuil : 80 %", x0=380, items=[
            dict(t="Syncytine 1 humaine / protéine MSRV", v=87, c="#2f9d62"),
            dict(t="Syncytine 2 humaine / protéine MSRV", v=20, c="#7fbecb")]),
        "args": dict(type="liste", titre="Trois arguments", items=[
            "Moléculaire : 87 % de similitude entre un virus et un primate",
            "Fonctionnel : même fonction, la fusion des membranes",
            "Parenté : sur l'arbre, la séquence virale se range près des grands singes et de l'humain",
            "Le gène de la syncytine 1 est issu d'un transfert horizontal de gène viral"], marques=["1", "2", "3", "✓"], x=150, y=150, w=980),
        "piege1": dict(type="note", titre="Analogie ou homologie ?", cles=["homologie", "séquences"],
                       t="Homologie de séquence : seule la ressemblance des séquences prouve la parenté. Même fonction ne veut pas dire apparentées.",
                       x=150, y=210, w=980),
        "piege2": dict(type="note", titre="La syncytine 2 (20 %)", cles=["virus-là", "vertical"],
                       t="Elle ne provient pas de ce virus-là. Cela ne prouve pas un transfert vertical : ne conclus rien de plus.",
                       x=150, y=210, w=980),
    }),

    # ================================================================ D2 bis. le TP syncytine façon bac
    dict(id="ece", chap="La syncytine, façon ECE", fond="foret", humeur="calme",
         retenir="Une conclusion d'ECE est complète, organisée et distanciée : une phrase sur les limites de la démarche, ou une expérience qui la compléterait.",
         beats=[
        "{etapes}{etapes.1}Cette comparaison est un sujet classique d'ECE. Reprenons-la, étape par étape. "
        "La stratégie : comparer avec Geniegen2 les séquences en acides aminés des syncytines humaines et de primates avec celles des protéines virales MSRV.",
        "On s'attend à démontrer un transfert viral si la similitude dépasse quatre-vingts pour cent.",
        "{etapes.2}Communiquer : un tableau titré, « Tableau de comparaison des protéines syncytines humaines et MSRV ». "
        "Deux lignes seulement : syncytine un, quatre-vingt-sept pour cent ; syncytine deux, vingt pour cent. L'essentiel, rien de plus.",
        "{etapes.3}Exploiter : quatre-vingt-sept pour cent, c'est au-delà de quatre-vingts. Les résultats sont compatibles avec une origine virale du gène.",
        "{etapes.4}La ressource complémentaire apporte la similitude fonctionnelle et l'arbre des primates. "
        "{etapes.5}Et la conclusion : le gène ENW1 des gorilles, chimpanzés, orangs-outans et gibbons provient d'un gène rétroviral, "
        "intégré dans le génome de leur ancêtre commun.",
        "{-etapes}{note_ece}Ce qui est évalué. {note_ece.1}La communication : techniquement correcte, bien renseignée, avec titre et unités, et pertinente. "
        "{note_ece.2}La conclusion : complète, organisée, et distanciée.",
        "{note_ece.3}Le critère le plus souvent oublié ? Le dernier. Pour être distancié, critique la démarche.",
        "Par exemple : on pourrait renforcer la preuve en insérant directement le gène ENW1 dans des cellules, pour voir s'il déclenche leur fusion. Une phrase suffit.",
        "{-note_ece}{pa_ece}À toi : rédige la conclusion complète de cette comparaison, en terminant par une phrase distanciée.",
        "{pa_ece.stop}{-pa_ece}",
    ], vis={
        "etapes": dict(type="liste", titre="L'ECE, de la stratégie à la conclusion", items=[
            "Stratégie : comparer les séquences (Geniegen2) ; transfert viral attendu si plus de 80 %",
            "Communiquer : un tableau titré, deux lignes, 87 % et 20 %",
            "Exploiter : 87 % > 80 %, compatible avec une origine virale",
            "Ressource : similitude fonctionnelle et arbre des primates",
            "Conclure : gène rétroviral intégré chez l'ancêtre commun des grands singes"], x=130, y=120, w=1020),
        "note_ece": dict(type="liste", titre="Ce qui est évalué", items=[
            "Communication : techniquement correcte, bien renseignée, pertinente",
            "Conclusion : complète, organisée, distanciée",
            "Distanciée : par exemple, insérer ENW1 dans des cellules et observer leur fusion"], marques=["1", "2", "!"], x=150, y=180, w=980),
        "pa_ece": dict(type="pause", t="Rédige la conclusion de la comparaison des syncytines, en finissant par une phrase distanciée.",
                       sous="Mets la vidéo sur pause, rédige sur une feuille, puis reprends pour comparer."),
    }),

    # ================================================================ D3. horizontal puis vertical
    dict(id="lignee", chap="Horizontal, puis vertical", fond="foret", humeur="lumiere",
         retenir="Rétrovirus intégré dans une cellule germinale → transmis à la descendance. Un transfert horizontal suivi d'une transmission verticale : une innovation, le placenta.",
         beats=[
        "{lg}Reste une énigme. Comment un gène de virus est-il devenu un gène de primate, présent chez tous ses descendants ?",
        "En général, un virus infecte des cellules somatiques. Et elles ne transmettent rien à la descendance.",
        "{lg.1}Mais si un rétrovirus infecte une cellule de la lignée germinale ? {lg.2}Alors l'ADN viral intégré se transmet à la descendance, "
        "comme n'importe quel gène.",
        "{lg.3}C'est ce qui s'est passé chez un ancêtre des primates. {lg.4}Un transfert horizontal, du virus vers une cellule germinale. "
        "Puis une transmission verticale, de génération en génération.",
        "Gibbons, orangs-outans, gorilles, chimpanzés et humains ont tous hérité du gène.",
        ("P", 0.8),
        "{-lg}{inno}{inno.1}Le génome des vertébrés est ainsi parsemé de séquences virales. Près de huit pour cent du génome humain, comme de celui de la souris.",
        "{inno.2}Et le gène de la syncytine, devenu indispensable au placenta, a été conservé. "
        "Un transfert horizontal est à l'origine d'une innovation évolutive chez les mammifères.",
        "{inno.3}Une infection virale est en général néfaste. Pourtant, des gènes viraux intégrés depuis des millions d'années remplissent des fonctions essentielles. "
        "Ils comptent dans la biologie de leur hôte, et dans l'évolution des espèces.",
        "{-inno}",
    ], vis={
        "lg": dict(type="illu", nom="lignee", x=90, y=80, w=1100, h=600),
        "inno": dict(type="liste", titre="Une innovation évolutive", items=[
            "Près de 8 % du génome humain, comme de celui de la souris, est d'origine virale",
            "Le gène de la syncytine, indispensable au placenta, a été conservé",
            "Des gènes viraux remplissent des fonctions essentielles : ils participent à l'évolution"], x=150, y=180, w=980),
    }),

    # ================================================================ D4. l'étendue des transferts, D5. transduction
    dict(id="etendue", chap="Partout dans le vivant", fond="foret", humeur="calme",
         retenir="Les transferts horizontaux touchent tous les grands groupes du vivant, donneurs ou receveurs ; les gènes reçus s'expriment et apportent de nouvelles fonctions.",
         beats=[
        "{idee}La syncytine, un cas isolé ? Pas du tout. {idee.1}Les transferts horizontaux concernent tous les grands groupes du vivant, comme donneurs ou comme receveurs.",
        "Les gènes reçus s'expriment, apportent de nouvelles fonctions, et participent à l'évolution des espèces. Trois exemples.",
        "{-idee}{docs}{docs.1}Un : l'origine des gènes reçus. Protistes, plantes, champignons, bactéries, archées et virus en donnent "
        "à l'humain, au nématode, un ver rond microscopique, et à la drosophile. Chez l'humain, ce sont les syncytines un et deux.",
        "{docs.2}Deux : on a compté les gènes d'origine étrangère qui s'expriment dans vingt-six espèces. "
        "Quarante chez les drosophiles, cent soixante-treize chez les nématodes, cent neuf chez les primates, dont l'humain.",
        "Surtout venus de bactéries et de protistes. Et sans compter les gènes viraux !",
        "{docs.3}Trois, la lignée verte. Sur un arbre du vivant, des flèches horizontales montrent les gènes reçus par les végétaux, avec leur fonction.",
        ("La genèse des chloroplastes, le métabolisme de l'amidon, la réparation de l'ADN, la résistance au stress, les vaisseaux conducteurs, la germination du pollen et des graines.", {"rate": "+5%"}),
        "{-docs}{ncbi}Ces gènes sont accessibles à tous : le génome humain est en libre accès dans la base du NCBI. "
        "On y trouve le gène de la syncytine un, sur le chromosome sept, et celui de la syncytine deux, sur le chromosome six.",
        "Dans la base, ils s'appellent ERVW-1 et ERVFRD-1. E R V, pour rétrovirus endogène.",
        "{-ncbi}{trans}Dernier mécanisme de la branche : la transduction. {trans.1}C'est un transfert d'ADN bactérien par un virus de bactérie, un bactériophage.",
        "En se multipliant dans une bactérie, le virus emporte par erreur un fragment d'ADN bactérien. Et il l'injecte dans la bactérie suivante. "
        "{trans.2}Retiens simplement que ce mécanisme existe : le mot et le principe suffisent.",
        "{-trans}",
    ], vis={
        "idee": dict(type="def", terme="L'idée", cles=["tous", "fonctions"],
                     t="Les transferts horizontaux concernent tous les grands groupes du vivant, comme donneurs ou comme receveurs.",
                     etape="Les gènes reçus s'expriment, apportent de nouvelles fonctions et participent à l'évolution.", x=150, y=200, w=980),
        "docs": dict(type="liste", titre="Trois exemples", items=[
            "Des protistes, plantes, champignons, bactéries, archées et virus vers l'humain, le nématode, la drosophile",
            "Gènes étrangers actifs, 40 chez les drosophiles, 173 chez les nématodes, 109 chez les primates",
            "La lignée verte, chloroplastes, amidon, réparation de l'ADN, stress, vaisseaux, pollen et graines"], x=130, y=150, w=1020),
        "ncbi": dict(type="note", titre="Dans la base du NCBI", cles=["syncytine"],
                     t="Syncytine 1 (chromosome 7) : ERVW-1 ; syncytine 2 (chromosome 6) : ERVFRD-1. ERV : rétrovirus endogène.",
                     x=150, y=210, w=980),
        "trans": dict(type="def", terme="Transduction", cles=["bactériophage"],
                      t="Transfert d'ADN bactérien d'une bactérie à une autre par un virus de bactérie, le bactériophage.",
                      etape="À connaître : le mot et le principe.", x=150, y=200, w=980),
    }),

    # ================================================================ E. autotrophes / hétérotrophes
    dict(id="auto", chap="Autotrophes et hétérotrophes", fond="foret", humeur="lumiere",
         retenir="Autotrophe : photosynthèse, chloroplaste. Hétérotrophe : respiration, mitochondrie. Une cellule végétale chlorophyllienne possède les deux.",
         beats=[
        "{mb}Deuxième branche : les endosymbioses. {mb.1}Les transferts horizontaux ne concernent pas que des gènes isolés. "
        "Une cellule entière peut en intégrer une autre !",
        "Les cellules eucaryotes possèdent des organites qui produisent ou convertissent l'énergie. D'où viennent-ils ? "
        "Pour le comprendre, rappel des deux grands modes de vie.",
        "{-mb}{ah}{ah.1}Les autotrophes produisent leur propre matière organique à partir de matière minérale. "
        "Les hétérotrophes en sont incapables : ils utilisent une matière organique préexistante.",
        "{ah.2}Exemples : plantes vertes et algues vertes d'un côté ; animaux et champignons de l'autre.",
        "{ah.3}Les processus. La photosynthèse : dioxyde de carbone plus eau plus lumière donnent des glucides et du dioxygène. "
        "La respiration cellulaire : matière organique plus dioxygène donnent de l'énergie, du dioxyde de carbone et de l'eau.",
        "{ah.4}Les organites : le chloroplaste pour la photosynthèse, la mitochondrie pour la respiration.",
        "{-ah}{tab_el}Et attention à un piège. Ces cellules de feuille d'élodée sont remplies de chloroplastes, les petits grains verts. "
        "Une plante est autotrophe, d'accord.",
        "Pourtant, toutes ses cellules respirent. La nuit comme le jour, pour utiliser la matière organique qu'elles ont fabriquée.",
        "{piege_mi}Une cellule végétale chlorophyllienne possède donc des chloroplastes et des mitochondries. Une cellule animale, seulement des mitochondries.",
        "{-piege_mi}{-tab_el}{q_or}D'où viennent ces deux organites ? Ils ressemblent étrangement à des bactéries.",
        ("P", 2.0),
    ], vis={
        "mb": dict(type="mental", vers=["c2", "c2b"]),
        "ah": dict(type="illu", nom="grille", x=90, y=100, w=1100, h=580, fs=26, larg=[1, 1.9, 1.9],
                   cols=["", "Autotrophes", "Hétérotrophes"], rows=[
                       ["Définition", "Produisent leur matière organique à partir de matière minérale", "Utilisent une matière organique préexistante"],
                       ["Exemples", "Plantes vertes, algues vertes", "Animaux, champignons"],
                       ["Processus", "Photosynthèse : CO₂ + eau + lumière → glucides (+ O₂)", "Respiration : matière organique + O₂ → énergie + CO₂ (+ eau)"],
                       ["Organite", "Chloroplaste", "Mitochondrie"]]),
        "tab_el": dict(type="tableau", img="ch2-elodee", fond=True, de=[1.3, .55, .5], a=[1.55, .55, .45],
                       legende="Cellules de feuille d'élodée et leurs chloroplastes, au microscope · Kelvinsong, CC BY-SA 3.0"),
        "piege_mi": dict(type="note", titre="Les plantes ont aussi des mitochondries", cles=["respirent", "mitochondries"],
                         t="Une plante est autotrophe, mais toutes ses cellules respirent : chloroplastes ET mitochondries.", x=150, y=220, w=980),
        "q_or": dict(type="question", t="Quels arguments en faveur d'une endosymbiose à l'origine des organites ?"),
    }),

    # ================================================================ F. Margulis
    dict(id="margulis", chap="Lynn Margulis et l'endosymbiose", fond="cellule", humeur="mystere",
         retenir="Symbiose : association durable à bénéfices réciproques. Endosymbiose : l'un vit à l'intérieur de l'autre. Margulis : les organites descendent de bactéries phagocytées mais non digérées.",
         beats=[
        "{defs2}Deux définitions. {defs2.1}La symbiose est une association durable, à bénéfices réciproques, entre deux êtres vivants, les symbiotes.",
        "{defs2.2}Si l'un des partenaires vit à l'intérieur des tissus ou des cellules de l'hôte, c'est une endosymbiose.",
        "{-defs2}{lm}Années mille neuf cent soixante. La biologiste américaine Lynn Margulis propose une idée audacieuse. "
        "Mitochondries et chloroplastes descendraient de bactéries !",
        "Ces bactéries auraient été phagocytées par des cellules eucaryotes primitives. Mais pas digérées.",
        "Elles seraient devenues, par endosymbiose, des composants permanents de la cellule. On parle de phagocytose incomplète.",
        "{-lm}{tab_am}Est-ce imaginable ? Oui. On l'observe encore aujourd'hui.",
        "Les amibes, comme celle-ci, sont des cellules eucaryotes qui phagocytent des bactéries. La bactérie se retrouve enfermée dans une vésicule.",
        "Et il arrive que les bactéries phagocytées ne soient pas digérées.",
        "{-tab_am}",
    ], vis={
        "defs2": dict(type="liste", titre="Deux définitions", items=[
            "Symbiose : association durable, à bénéfices réciproques, entre deux symbiotes",
            "Endosymbiose : l'un des partenaires vit à l'intérieur des tissus ou des cellules de l'hôte"], x=150, y=200, w=980),
        "lm": dict(type="portrait", img="ch2-margulis", nom="Lynn Margulis", dates="1938 – 2011", annee=1967,
                   legende="théorie endosymbiotique, années 1960 · photo Javier Pedreira, CC BY 2.0"),
        "tab_am": dict(type="tableau", img="ch2-amibe", de=[1.0, .5, .5], a=[1.3, .5, .5],
                       legende="Une amibe, Amoeba proteus, cellule eucaryote qui phagocyte ses proies · SmallRex, CC BY-SA 4.0"),
    }),

    # ================================================================ G1. la double membrane
    dict(id="membrane", chap="L'argument essentiel : la double membrane", fond="cellule", humeur="lumiere",
         retenir="Double membrane : la membrane interne est celle de la bactérie, la membrane externe celle de la vésicule de phagocytose. C'est l'argument essentiel.",
         beats=[
        "{an6}{pt6}{pt6.1}{an6.1}Rejouons l'histoire, avec l'animation du chloroplaste. Une cellule eucaryote ancestrale, avec son noyau, sans chloroplaste. "
        "À côté, une cyanobactérie libre, capable de photosynthèse, avec son ADN circulaire.",
        "{pt6.2}{an6.2}La cellule phagocyte la cyanobactérie : sa membrane l'entoure, et l'enferme dans une vésicule. Mais la bactérie n'est pas digérée. "
        "Elle est maintenant entourée de deux membranes : la sienne, et celle de la vésicule.",
        "{pt6.3}{an6.3}La bactérie vit et se divise dans la cellule, par étranglement, comme une bactérie. Chacun y gagne : c'est une endosymbiose.",
        "{-pt6}{dm}Et voici l'argument essentiel. {dm.1}Mitochondries et chloroplastes sont entourés de deux membranes. Exactement comme une bactérie phagocytée.",
        ("{dm.2}La membrane interne correspond à la membrane de la bactérie. {dm.3}La membrane externe, à la membrane de la vésicule formée par la cellule hôte.", {"rate": "-4%"}),
        "{-dm}{pa_en}C'est le schéma étoilé de cette branche. À toi : refais l'endosymbiose, avec la double membrane légendée.",
        "{pa_en.stop}{-pa_en}{-an6}{tab_ch}Au microscope électronique, un chloroplaste. Son enveloppe, et ses empilements de membranes à l'intérieur.",
        "Sa membrane interne était, à l'origine, la membrane de la cyanobactérie. D'où les ressemblances de structure entre les deux. "
        "L'endosymbiose de cyanobactéries a donné naissance à la lignée verte.",
        "{-tab_ch}{tab_mi}Et voici deux mitochondries, dans une cellule de poumon de mammifère. Même enveloppe double.",
        "{-tab_mi}{nuance}Une nuance, hors programme. Le modèle classique, une membrane bactérienne plus une membrane de vésicule, est celui qu'on attend au bac.",
        "Mais les recherches récentes le nuancent. Les cyanobactéries possèdent déjà deux membranes, "
        "et beaucoup de chercheurs pensent que les deux membranes de l'organite viennent de la bactérie.",
        "La conclusion, elle, ne change pas : la double membrane témoigne d'une bactérie englobée dans une cellule.",
        "{-nuance}",
    ], vis={
        "an6": dict(type="anim", nom="endosymbiose", x=40, y=72, h=624, seg=[[0, 7], [7, 17], [17, 24]]),
        "pt6": dict(type="liste", petit=True, titre="L'endosymbiose du chloroplaste", x=680, y=120, w=560, items=[
            "Une cellule eucaryote ancestrale et une cyanobactérie libre",
            "Phagocytose incomplète : la bactérie, enfermée dans une vésicule, n'est pas digérée",
            "Elle vit et se divise dans la cellule : une endosymbiose"]),
        "dm": dict(type="liste", petit=True, titre="La double membrane", x=680, y=140, w=560, items=[
            "Deux membranes autour des chloroplastes et des mitochondries",
            "Interne : la membrane de la bactérie",
            "Externe : la membrane de la vésicule de phagocytose"], marques=["2", "↘", "↗"]),
        "pa_en": dict(type="pause", x=680, y=150, w=560, t="Refais le schéma de l'endosymbiose, double membrane légendée.",
                      sous="Cellule hôte, noyau, cyanobactérie, vésicule, membrane interne et externe, organite."),
        "tab_ch": dict(type="tableau", img="ch2-chloro", de=[1.0, .5, .5], a=[1.25, .55, .4],
                       legende="Chloroplaste de feuille d'anémone, microscope électronique à transmission · NCI, domaine public"),
        "tab_mi": dict(type="tableau", img="ch2-mito", de=[1.0, .5, .5], a=[1.3, .4, .45],
                       legende="Deux mitochondries, poumon de mammifère, microscope électronique · Louisa Howard, domaine public"),
        "nuance": dict(type="note", titre="Hors programme · la membrane externe", cles=["bactérie"],
                       t="Les deux membranes viendraient peut-être de la bactérie. La conclusion ne change pas : une bactérie a été englobée.",
                       x=150, y=210, w=980),
    }),

    # ================================================================ G2. les autres points communs
    dict(id="points", chap="Les autres points communs", fond="cellule", humeur="calme",
         retenir="ADN circulaire, ribosomes à ARN 16S, taille du micromètre, division par étranglement, RubisCo : chloroplaste ← cyanobactérie, mitochondrie ← α-protéobactérie.",
         beats=[
        "{pc}{pc.1}Quels autres points communs entre organites et bactéries ? D'abord, les membranes. "
        "La membrane interne contient de la cardiolipine et des chaînes de transport d'électrons, avec des protéines de transport, les porines.",
        "Même composition dans la membrane bactérienne.",
        "{pc.2}Le matériel génétique : un chromosome circulaire. De trente à cent gènes dans l'organite, plusieurs milliers chez la bactérie.",
        "{pc.3}Les ribosomes : les organites ont les leurs, et leur petite sous-unité contient un ARN 16S. Comme chez les bactéries. "
        "Alors que les ribosomes de la cellule eucaryote ont un ARN 18S.",
        "{pc.4}La taille, de l'ordre du micromètre. Et la division : par étranglement médian, indépendamment de la cellule, comme une bactérie.",
        "{pc.5}La fonction : le chloroplaste fait la photosynthèse grâce à la RubisCo, comme les cyanobactéries. La mitochondrie respire, comme les alpha-protéobactéries.",
        "{-pc}{arbre}Enfin, un arbre phylogénétique construit avec les ARN ribosomiques range chloroplastes et mitochondries parmi les bactéries. "
        "{arbre.1}Le chloroplaste est apparenté aux cyanobactéries. {arbre.2}La mitochondrie, aux alpha-protéobactéries.",
        "{-arbre}{tab_cy}Question de bac : de quel type de bactérie provient le chloroplaste ? Ici, des colonies de Nostoc, une cyanobactérie.",
        ("P", 0.8),
        "{-tab_cy}{rep_cy}Réponse : d'une cyanobactérie. {rep_cy.1}Comme le chloroplaste, elle fait la photosynthèse. {rep_cy.2}Elle possède la même enzyme clé, la RubisCo.",
        "{rep_cy.3}Son ARN ribosomique seize S est le plus proche de celui du chloroplaste. {rep_cy.4}Et elle a la même taille, et se divise de la même façon.",
        "{-rep_cy}{melange}Ne mélange pas les deux organites. La cyanobactérie ne devient pas un chloroplaste qui produirait de l'énergie par des mitochondries.",
        "Il faut séparer. La cyanobactérie est l'ancêtre du chloroplaste : la photosynthèse. Une alpha-protéobactérie est l'ancêtre de la mitochondrie : la respiration. "
        "Deux endosymbioses distinctes.",
        "{-melange}",
    ], vis={
        "pc": dict(type="illu", nom="grille", x=80, y=88, w=1120, h=610, fs=23, larg=[1, 2.1, 2.1],
                   cols=["", "Organites", "Bactéries"], rows=[
                       ["Membranes", "Membrane interne à cardiolipine, chaînes de transport d'électrons, porines", "Même composition, mêmes porines"],
                       ["Matériel génétique", "Un chromosome circulaire, de 30 à 100 gènes", "Un chromosome circulaire, plusieurs milliers de gènes"],
                       ["Ribosomes", "Propres, petite sous-unité à ARN 16S", "ARN 16S (cellule eucaryote : ARN 18S)"],
                       ["Taille, division", "≈ 1 µm ; étranglement médian, indépendant de la cellule", "Même taille, même division"],
                       ["Fonction", "Chloroplaste : photosynthèse (RubisCo) ; mitochondrie : respiration", "Cyanobactéries : photosynthèse (RubisCo) ; α-protéobactéries : respiration"]]),
        "arbre": dict(type="cols", g="Chloroplaste", gq="← cyanobactérie (photosynthèse)", d="Mitochondrie", dq="← α-protéobactérie (respiration)",
                      vs="≠", repere="Arbre des ARN ribosomiques : les organites se rangent parmi les bactéries"),
        "tab_cy": dict(type="tableau", img="ch2-cyano", de=[1.0, .5, .5], a=[1.2, .55, .5],
                       legende="Colonies de Nostoc, une cyanobactérie · Christian Fischer, CC BY-SA 3.0"),
        "rep_cy": dict(type="liste", titre="Le chloroplaste vient d'une cyanobactérie", items=[
            "Même fonction : la photosynthèse", "Même enzyme clé : la RubisCo",
            "ARN ribosomique 16S le plus proche", "Même taille, même division"], marques=["1", "2", "3", "4"], x=150, y=170, w=980),
        "melange": dict(type="note", titre="Deux endosymbioses distinctes", cles=["chloroplaste", "mitochondrie"],
                        t="Cyanobactérie → chloroplaste (photosynthèse) ; α-protéobactérie → mitochondrie (respiration).", x=150, y=220, w=980),
    }),

    # ================================================================ H. les objections ; le transfert vers le noyau
    dict(id="objections", chap="Deux objections qui se retournent", fond="cellule", humeur="tension",
         retenir="Peu de gènes dans les organites (67, 87) : transfert de gènes vers le noyau, prise de relais par le noyau, protéines importées. Un transfert horizontal qui complexifie le génome de l'hôte.",
         beats=[
        "{pc2}{pc2.1}Faisons le tableau des arguments, pour et contre. En faveur : la similitude des ARN ribosomiques, la RubisCo commune, "
        "la membrane interne de type bactérien, l'ADN circulaire, la même fonction, la taille et la division, l'arbre phylogénétique.",
        "{pc2.2}Contre ? Deux membranes chez les organites, une seule chez la bactérie. "
        "Réponse : cette double membrane est justement la preuve de l'ingestion d'une bactérie.",
        "{pc2.3}Contre ? Beaucoup plus de gènes dans la bactérie ancestrale que dans les organites. Réponse : les organites ont perdu des gènes.",
        "{pc2.hl}Tu vois le retournement ? Bien expliqués, les deux arguments contre deviennent des arguments pour.",
        "{-pc2}{gn}Développons le second. {gn.1}Le plus proche parent bactérien libre de la mitochondrie a environ mille six cents gènes. {gn.2}La mitochondrie ? Soixante-sept.",
        "{gn.3}Une cyanobactérie en a de mille cinq cents à dix mille. {gn.4}Le chloroplaste ? Quatre-vingt-sept.",
        "{-gn}{an7}{pt7}{pt7.1}{an7.1}Où sont passés tous ces gènes ? Un : ils ont été transférés vers le noyau. "
        "Au cours de l'évolution, une grande partie des gènes de la bactérie ancestrale est partie dans le noyau de la cellule hôte.",
        "Pour le chloroplaste, environ mille quatre cents gènes transférés. Quatre-vingt-sept seulement restés dans l'organite.",
        "{pt7.2}{an7.2}Deux : le noyau prend le relais. Ce sont désormais ses gènes qui codent la plupart des protéines de l'organite.",
        "{pt7.3}Trois : les protéines voyagent. Fabriquées dans le cytoplasme, elles sont importées dans l'organite. "
        "Environ deux mille trois cents protéines sont importées vers le chloroplaste.",
        "{pt7.4}Un exemple : la RubisCo. Sa petite sous-unité est codée par le noyau, puis importée. Sa grande sous-unité, par le génome du chloroplaste.",
        ("P", 0.8),
        "{-pt7}{-an7}{cle}{cle.1}Et voici l'idée qui relie tout le chapitre. Ce passage de gènes du symbiote vers le noyau est un transfert horizontal, "
        "rendu possible par l'endosymbiose.",
        "{cle.2}Le génome de la cellule hôte s'enrichit de gènes bactériens. Il se complexifie. "
        "Voilà pourquoi les endosymbioses ont leur place dans ce chapitre.",
        "{-cle}",
    ], vis={
        "pc2": dict(type="illu", nom="grille", x=90, y=100, w=1100, h=580, fs=26, larg=[1.4, 1.6], hlr=[2, 3],
                    cols=["Arguments en faveur", "Arguments contre ?"], rows=[
                        ["ARN ribosomiques semblables ; RubisCo commune ; membrane interne de type bactérien ; ADN circulaire ; même fonction, taille et division ; arbre phylogénétique", "—"],
                        ["Réponse : la double membrane est la trace de l'ingestion d'une bactérie", "Deux membranes chez les organites, une seule chez la bactérie"],
                        ["Réponse : il y a eu perte de gènes dans les organites (transfert vers le noyau)", "Beaucoup plus de gènes dans la bactérie ancestrale"]]),
        "gn": dict(type="illu", nom="barres", x=90, y=120, w=1100, h=500, bh=58, fs=26, max=1600, x0=440, items=[
            dict(t="Parent bactérien libre de la mitochondrie", v=1600, lbl="1 600 gènes", c="#7fbecb"),
            dict(t="Mitochondrie", v=67, lbl="67 gènes", c="#ff6b5b"),
            dict(t="Cyanobactérie", v=1600, lbl="1 500 à 10 000 gènes", c="#2f9d62", plus=True),
            dict(t="Chloroplaste", v=87, lbl="87 gènes", c="#b7d94c")]),
        "an7": dict(type="anim", nom="endosymbiose", x=40, y=72, h=624, seg=[[24, 38], [38, 48]]),
        "pt7": dict(type="liste", petit=True, titre="Pourquoi si peu de gènes ?", x=680, y=110, w=560, items=[
            "Transfert vers le noyau : ≈ 1 400 gènes, 87 conservés dans le chloroplaste",
            "Le noyau prend le relais : il code la plupart des protéines de l'organite",
            "Les protéines sont importées : ≈ 2 300 vers le chloroplaste",
            "RubisCo : petite sous-unité codée par le noyau, grande par le chloroplaste"]),
        "cle": dict(type="liste", titre="L'idée qui relie le chapitre", items=[
            "Gènes du symbiote → noyau : un transfert horizontal, permis par l'endosymbiose",
            "Le génome de la cellule hôte s'enrichit de gènes bactériens : il se complexifie"], x=150, y=210, w=980),
    }),

    # ================================================================ I. bénéfices, bilan, TP
    dict(id="benefices", chap="Bénéfices réciproques et bilan", fond="foret", humeur="lumiere",
         retenir="L'endosymbiose est à l'origine des mitochondries et des chloroplastes, et des métabolismes des eucaryotes. Les organites se divisent par étranglement, pas par mitose.",
         beats=[
        "{an8}{pt8}{pt8.1}{an8.1}Après l'endosymbiose, qui y gagne ? Tout le monde. La cellule eucaryote devient capable de photosynthèse, grâce au chloroplaste. "
        "Ou d'une respiration efficace, grâce à la mitochondrie.",
        "{pt8.2}L'organite, lui, gagne un environnement stable. Et il dépense moins d'énergie à maintenir et exprimer un génome immense.",
        "{pt8.3}{an8.2}Le chloroplaste descend d'une cyanobactérie ; la mitochondrie, par la même histoire, d'une alpha-protéobactérie. "
        "Et en héritant de gènes bactériens, le génome de l'hôte s'est complexifié.",
        "{-pt8}{-an8}{bilan}{bilan.1}Voici le bilan à écrire. Les procaryotes sont fortement intégrés au sein de la cellule hôte, "
        "et chacun retire de cette association des bénéfices mutuels.",
        "C'est l'endosymbiose, à l'origine des métabolismes des eucaryotes. "
        "{bilan.2}Autotrophes, qui synthétisent leur matière organique à partir de matière minérale grâce à la photosynthèse.",
        "{bilan.3}Et hétérotrophes, qui produisent de l'énergie à partir de matière organique préexistante grâce à la respiration.",
        "{-bilan}{mit2}Un dernier piège. Les organites ne se divisent pas par mitose. Comme les bactéries dont ils descendent, "
        "ils se divisent par étranglement médian, indépendamment de la cellule.",
        "C'est même l'un des arguments de leur origine bactérienne.",
        "{-mit2}{tp}{tp.1}Une autre ECE classique : l'origine des chloroplastes. Sa stratégie est imposée. "
        "Comparer, avec Geniegen2, les ARN ribosomiques seize S de bactéries, de chloroplastes et de plantes vertes.",
        "{tp.2}Et comparer la séquence de la RubisCo chez des bactéries et des plantes.",
        "{tp.3}Ce qu'on attend ? Un ARN du chloroplaste plus proche de celui des bactéries, surtout d'une cyanobactérie, que de l'ARN dix-huit S du noyau de la plante. "
        "Et une RubisCo très proche de celle des cyanobactéries.",
        "{-tp}{err}{err.1}Deux précisions utiles. Nostoc et Chlorobium ne sont pas des plantes : ce sont des bactéries photosynthétiques. "
        "Nostoc est une cyanobactérie, Chlorobium une bactérie sulfureuse verte.",
        "{err.2}Et un ribosome n'est pas une protéine : c'est un assemblage d'ARN ribosomiques et de protéines.",
        "{-err}",
    ], vis={
        "an8": dict(type="anim", nom="endosymbiose", x=40, y=72, h=624, seg=[[48, 56], [56, 62]]),
        "pt8": dict(type="liste", petit=True, titre="Des bénéfices réciproques", x=680, y=120, w=560, items=[
            "La cellule : photosynthèse (chloroplaste) ou respiration efficace (mitochondrie)",
            "L'organite : un milieu stable, moins d'énergie pour son génome",
            "Le génome de l'hôte s'est complexifié"]),
        "bilan": dict(type="liste", titre="Le bilan à écrire", items=[
            "Endosymbiose : bénéfices mutuels, à l'origine des métabolismes des eucaryotes",
            "Autotrophes : matière organique à partir de matière minérale, photosynthèse",
            "Hétérotrophes : énergie à partir de matière organique préexistante, respiration"], x=150, y=180, w=980),
        "mit2": dict(type="note", titre="Les organites ne font pas de mitose", cles=["étranglement"],
                     t="Ils se divisent par étranglement médian, comme les bactéries, indépendamment de la cellule.", x=150, y=220, w=980),
        "tp": dict(type="liste", titre="ECE · l'origine des chloroplastes", items=[
            "Comparer les ARN ribosomiques 16S : bactéries, chloroplastes, plantes vertes",
            "Comparer la RubisCo : bactéries et plantes vertes",
            "Attendu : chloroplaste ≈ cyanobactérie, loin de l'ARN 18S du noyau"], x=150, y=170, w=980),
        "err": dict(type="liste", titre="Deux précisions", items=[
            "Nostoc et Chlorobium ne sont pas des plantes : ce sont des bactéries",
            "Un ribosome n'est pas une protéine : ARN ribosomiques + protéines"], marques=["!", "!"], x=150, y=170, w=980),
    }),

    # ================================================================ exercice de synthèse (type bac)
    dict(id="exo", chap="Exercice type bac", fond="aube", humeur="tension",
         retenir="Plan de synthèse : I. les bactéries (transformation, conjugaison, transgenèse) ; II. les virus (rétrovirus, syncytine) ; III. les endosymbioses (organites, gènes vers le noyau).",
         beats=[
        "{ex}Pour finir, un sujet de synthèse, au format du bac. Il est inventé pour la vidéo, mais il couvre tout le chapitre.",
        "Montrer que les transferts horizontaux de gènes contribuent à la complexification des génomes. "
        "Une introduction, un développement structuré, illustré d'exemples précis, et une conclusion. Un schéma est valorisé.",
        "{-ex}{pa_ex}À toi. Prends vingt minutes. D'abord le plan au brouillon, avec un exemple précis par idée.",
        "{pa_ex.stop}{-pa_ex}Une réponse possible. {exc}{exc.q1}{intro}L'introduction. {intro.1}Partir du transfert vertical, des parents aux descendants. "
        "Et dire que ses brassages ne suffisent pas à expliquer toute la diversité génétique.",
        "{intro.2}Définir le transfert horizontal, et ce qui le rend possible : l'universalité de l'ADN et du code génétique. "
        "{intro.3}Puis poser la question : comment ces transferts enrichissent-ils les génomes ?",
        "{-intro}{exc.q2}{plan_ex}{plan_ex.1}Le développement, en trois parties, des gènes isolés à la cellule entière. Un : chez les bactéries.",
        ("La transformation, avec Griffith. La conjugaison et les plasmides, avec les résistances aux antibiotiques. "
         "La transgenèse naturelle d'Agrobacterium, et la transgenèse dirigée de l'insuline.", {"rate": "+5%"}),
        "{plan_ex.2}Deux : par les virus. Le cycle du rétrovirus, puis la syncytine. Quatre-vingt-sept pour cent de similitude, la même fonction, "
        "et l'intégration dans une cellule germinale de l'ancêtre des primates.",
        "Un gène viral devenu un gène de mammifère, indispensable au placenta.",
        "{plan_ex.3}Trois : par endosymbiose. La double membrane et les autres arguments, puis le transfert de gènes de l'organite vers le noyau. "
        "Le génome de la cellule hôte s'enrichit de gènes bactériens.",
        "{-plan_ex}{exc.q3}{concl}La conclusion. {concl.1}Répondre à la question : par ces trois voies, des génomes reçoivent des gènes déjà fonctionnels, "
        "qui s'expriment et apportent de nouvelles fonctions.",
        "{concl.2}Et ouvrir : ces innovations vont ensuite évoluer dans les populations. C'est le chapitre trois.",
        "{-concl}{-exc}",
    ], vis={
        "ex": dict(type="exo", niveau="bac", titre="Transferts horizontaux et complexification des génomes",
                   src="Sujet inventé pour la vidéo, au format d'une question de synthèse du bac",
                   enonce=["Montrer que les transferts horizontaux de gènes contribuent à la complexification des génomes.",
                           "Réponse structurée : introduction, développement illustré d'exemples précis, conclusion. Un schéma est valorisé."],
                   questions=["Introduction : définitions et problématique", "Développement : trois parties, un exemple précis par idée",
                              "Conclusion : réponse et ouverture"]),
        "pa_ex": dict(type="pause", t="Le plan au brouillon : trois parties, un exemple précis par idée, puis rédige.",
                      sous="Mets la vidéo sur pause, rédige sur une feuille, puis reprends pour comparer."),
        "exc": dict(type="exo", mode="coin", niveau="bac", titre="La synthèse",
                    questions=["Introduction", "Développement", "Conclusion"]),
        "intro": dict(type="liste", petit=True, titre="L'introduction", x=540, y=150, w=700, items=[
            "Le transfert vertical ne suffit pas à expliquer la diversité",
            "Définition du transfert horizontal ; universalité de l'ADN et du code génétique",
            "Problématique : comment ces transferts enrichissent-ils les génomes ?"]),
        "plan_ex": dict(type="liste", petit=True, titre="Le développement", x=540, y=120, w=700, items=[
            "I. Bactéries : Griffith, conjugaison et résistances, Agrobacterium, insuline",
            "II. Virus : rétrovirus, syncytine (87 %, fusion, cellule germinale)",
            "III. Endosymbioses : double membrane, gènes de l'organite vers le noyau"], marques=["I", "II", "III"]),
        "concl": dict(type="liste", petit=True, titre="La conclusion", x=540, y=170, w=700, items=[
            "Des gènes déjà fonctionnels, qui s'expriment et apportent de nouvelles fonctions",
            "Ouverture : leur devenir dans les populations (chapitre 3)"]),
    }),

    # ================================================================ pour le bac
    dict(id="bac", chap="Pour le bac", fond="aube", humeur="calme",
         retenir="Les mots exacts : non apparenté, plasmide, pont cytoplasmique, vecteur, transcription inverse, cellule germinale, homologie de séquence, double membrane, étranglement.",
         beats=[
        "{sujets}{sujets.1}Ce qu'il faut savoir rédiger, sans aide. L'introduction du chapitre : le transfert vertical, ses limites, l'universalité de l'ADN, "
        "la définition du transfert horizontal, et la problématique.",
        "{sujets.2}L'interprétation de l'expérience de Griffith, lot par lot. "
        "{sujets.3}La diffusion des résistances aux antibiotiques : mutation rare contre plasmide fréquent, conjugaison, sélection. Et jamais de formulation finaliste.",
        "{sujets.4}La production d'insuline par transgenèse, schéma à l'appui. {sujets.5}La conclusion de la comparaison des syncytines, avec ses trois arguments et sa phrase distanciée.",
        "{sujets.6}Et l'argumentation de l'origine endosymbiotique des chloroplastes : les caractères bactériens, la cyanobactérie, le génome réduit.",
        "{-sujets}{schemas}{schemas.1}Les schémas à savoir refaire, les étoiles de la carte. La conjugaison bactérienne. {schemas.2}La transgenèse de l'insuline. "
        "{schemas.3}Le cycle du rétrovirus. {schemas.4}Et l'endosymbiose, avec la double membrane légendée.",
        "{-schemas}{reflexes}{reflexes.1}Et les réflexes qui rapportent des points. L'antibiotique sélectionne, il ne crée pas.",
        "{reflexes.2}Les bactéries se divisent, elles ne font pas de mitose. Les organites non plus. "
        "{reflexes.3}Plus de quatre-vingts pour cent entre organismes éloignés : transfert horizontal.",
        "{reflexes.4}Homologie de séquence, pas analogie. {reflexes.5}Chloroplaste, cyanobactérie. Mitochondrie, alpha-protéobactérie.",
        "{-reflexes}",
    ], vis={
        "sujets": dict(type="liste", titre="Six rédactions à maîtriser", items=[
            "L'introduction du chapitre", "Interpréter l'expérience de Griffith",
            "La diffusion des résistances aux antibiotiques", "La production d'insuline par transgenèse (schéma)",
            "La conclusion sur la syncytine", "L'origine endosymbiotique des chloroplastes"], x=150, y=110, w=980),
        "schemas": dict(type="liste", titre="★ Les schémas à refaire", items=[
            "La conjugaison bactérienne", "La transgenèse : l'insuline", "Le cycle d'un rétrovirus",
            "L'endosymbiose et la double membrane"], marques=["★", "★", "★", "★"], x=150, y=170, w=980),
        "reflexes": dict(type="liste", titre="Cinq réflexes", items=[
            "L'antibiotique sélectionne, il ne crée pas la résistance",
            "Bactéries et organites : divisions, pas mitoses",
            "Plus de 80 % entre organismes éloignés : transfert horizontal",
            "Homologie de séquence (pas analogie de structure)",
            "Chloroplaste ← cyanobactérie ; mitochondrie ← α-protéobactérie"], x=150, y=140, w=980),
    }),

    # ================================================================ fin : la carte
    dict(id="fin", chap="La carte du chapitre", fond="foret", humeur="lumiere", beats=[
        "{carte2}Revenons à la carte. {carte2.1}Les transferts horizontaux : transformation, conjugaison, transgenèse, rétrovirus et syncytine, transduction. "
        "{carte2.2}Les endosymbioses : autotrophes et hétérotrophes, chloroplastes et mitochondries.",
        "{carte2.3}Qu'est-ce qui relie tout ça ? Une seule idée. Un génome n'hérite pas seulement de ses parents.",
        "Il s'enrichit de gènes venus d'ailleurs : de bactéries, de virus, d'une cellule entière avalée. C'est la complexification des génomes.",
        "{carte2.4}Avec les transferts verticaux et horizontaux, on sait d'où viennent les variations du génome. "
        "Reste à comprendre comment elles évoluent au sein des populations. C'est le chapitre trois.",
        "Maintenant, à toi : le quiz.",
        ("P", 3.0),
    ], vis={
        "carte2": dict(type="mental", vers=["c2", "c2a", "c2b", "c2", "t1a"]),
    }),
]

QUIZ = [
    dict(q="Un transfert horizontal de gènes se fait…", r=["des parents à leurs descendants", "entre organismes non apparentés", "uniquement entre bactéries de la même espèce"], ok=1,
         ex="Un organisme incorpore le matériel génétique d'un organisme non apparenté ; c'est possible car l'ADN et le code génétique sont universels.", voir="def_th"),
    dict(q="Dans l'expérience de Griffith, les pneumocoques S vivants retrouvés dans le sang de la souris du lot 4 sont…",
         r=["des S tués qui ont repris vie", "des R qui ont acquis la capsule par transformation", "des S apportés par la souris"], ok=1,
         ex="Les S tués ne revivent pas : des R ont intégré le « facteur transformant », l'ADN des S, et fabriquent une capsule.", voir="gr"),
    dict(q="Lors de la conjugaison bactérienne…", r=["la donneuse perd son plasmide", "une copie du plasmide passe par un pont cytoplasmique", "la bactérie absorbe de l'ADN libre"], ok=1,
         ex="Le plasmide est copié : la donneuse garde le sien. L'ADN libre, c'est la transformation.", voir="defs"),
    dict(q="Pourquoi les résistances aux antibiotiques se répandent-elles si vite ?",
         r=["L'antibiotique provoque des mutations de résistance", "Les plasmides de résistance passent souvent d'une bactérie à l'autre, et l'antibiotique sélectionne leurs porteuses", "Les bactéries s'adaptent à l'antibiotique"], ok=1,
         ex="Plasmide : ≈ 1 bactérie sur 100, ≈ 80 % des résistances acquises. L'antibiotique sélectionne, il ne crée pas.", voir="pt2"),
    dict(q="Agrobacterium tumefaciens insère dans le génome d'une cellule végétale…", r=["tout son chromosome", "l'ADN-T, un fragment de son plasmide pTi", "de l'ARN viral"], ok=1,
         ex="L'ADN-T s'intègre au génome de la plante et y fait produire des facteurs de croissance (galle) et des opines.", voir="pt3"),
    dict(q="Pour faire produire de l'insuline humaine par une bactérie, le plasmide recombinant sert de…", r=["vecteur", "enzyme", "ribosome"], ok=0,
         ex="Le plasmide transporte le gène d'intérêt : c'est un vecteur. La bactérie transformée l'exprime car le code génétique est universel.", voir="pt4"),
    dict(q="Chez un rétrovirus, la transcription inverse…", r=["copie l'ADN en ARN", "copie l'ARN viral en ADN double brin", "intègre l'ARN au chromosome"], ok=1,
         ex="ARN simple brin → ADN double brin, par une enzyme du virus ; cet ADN s'intègre ensuite au génome de l'hôte.", voir="pt5"),
    dict(q="La syncytine 2 humaine ressemble à 20 % à la protéine du virus MSRV. On peut conclure que…",
         r=["elle est issue d'un transfert vertical", "elle ne provient pas de ce virus-là", "elle provient de ce virus"], ok=1,
         ex="Une faible ressemblance avec un virus donné ne dit rien de plus : ne pas conclure à un transfert vertical.", voir="piege2"),
    dict(q="L'argument essentiel de l'origine endosymbiotique des organites est…", r=["leur couleur verte", "leur double membrane", "leur présence dans toutes les cellules"], ok=1,
         ex="Membrane interne = celle de la bactérie, membrane externe = celle de la vésicule de phagocytose.", voir="dm"),
    dict(q="Le chloroplaste ne contient que 87 gènes, contre des milliers chez une cyanobactérie, parce que…",
         r=["il n'est pas d'origine bactérienne", "la plupart des gènes ont été transférés vers le noyau de la cellule hôte", "il les a perdus en se divisant par mitose"], ok=1,
         ex="≈ 1 400 gènes transférés vers le noyau, qui code désormais la plupart des protéines de l'organite (≈ 2 300 importées).", voir="pt7"),
]

CREDITS = [
    "Photos (Wikimedia Commons) : pneumocoques en coloration de Gram, Arnold Kaufman (CC0) ; antibiogrammes de Staphylococcus aureus, HansN. (CC BY-SA 4.0) ; "
    "galles du collet sur un orme, Rosser1954 (CC BY-SA 4.0) ; particules de VIH-1, NIAID (CC BY 2.0) ; placenta humain, Asturnut (CC BY-SA 3.0) ; "
    "cellules d'élodée, Kelvinsong (CC BY-SA 3.0) ; Lynn Margulis en 2005, Javier Pedreira (CC BY 2.0) ; Amoeba proteus, SmallRex (CC BY-SA 4.0) ; "
    "chloroplaste d'anémone, National Cancer Institute (domaine public) ; mitochondries, Louisa Howard (domaine public) ; Nostoc, Christian Fischer (CC BY-SA 3.0).",
    "Animations, schémas et carte mentale du thème : faits pour la vidéo. Exercice de synthèse inventé pour la vidéo.",
]
