"""Le bonheur, épisode 2 : « Le plaisir rend-il heureux ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la nature} dans le texte lu.
Citations : Diogène Laërce, Vies des philosophes, II, « Aristippe » (trad. anonyme, Wikisource) ; Épicure, Lettre à
Ménécée, trad. Octave Hamelin (1910), Wikisource ; Platon, Gorgias, 494a-b, trad. Émile Chambry, Wikisource.
Mill (Utilitarisme, 1861 ; Autobiographie, 1873, chap. V) est résumé par le narrateur ; la formule « Socrate insatisfait »
a été citée dans la série « Le devoir » (épisode 4).
"""

CODE = "bonheur-2"
NOTION = "Le bonheur"
NUM = 2
TITRE = "Le plaisir rend-il heureux ?"
SUIVANT = "Épisode 3 · La sagesse des Anciens"
PRONONCIATION = {"hêdonê": "édoné", "Cyrénaïques": "Cirénaïques", "Laïs": "Laïsse", "ataraxie": "ataraxie",
                 "aponie": "aponie", "Philodème": "Filodème", "Herculanum": "Erculanome", "Bentham": "Bentame",
                 "Wordsworth": "Ouordsoueurse", "Calliclès": "Kaliklèsse"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_ste}{soir}Vendredi, minuit. Tu as passé la soirée à faire exactement ce qui te plaisait. "
        "{soir.1}Une série, trois épisodes d'affilée. {soir.2}Un paquet de chips. {soir.3}Des vidéos, encore des vidéos. "
        "Que du plaisir.",
        "{-soir}{q_vide}Et pourtant, en éteignant la lumière, un drôle de goût. Une sorte de vide. "
        "Comme si la soirée n'avait rien laissé.",
        ("Tant de plaisir… et si peu de bonheur ?", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-q_vide}{hed}C'est la question de cet épisode : le plaisir rend-il heureux ? Ceux qui répondent oui, "
        "on les appelle les hédonistes, du grec hêdonê : le plaisir.",
        "{-hed}{deux}Mais attention : il y a deux hédonismes, presque opposés. {deux.1}Celui qui court après tous les plaisirs. "
        "{deux.2}Et celui qui, pour être heureux, apprend à en refuser beaucoup.",
        ("P", 0.3),
        "{-deux}{-tab_ste}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_ste": dict(type="tableau", img="bh2-steen", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .5],
                        legende="Jan Steen, Joyeuse compagnie sur une terrasse, v. 1670 (Metropolitan Museum, New York, CC0)"),
        "soir": dict(type="liste", titre="Vendredi soir", items=[
            "Une série, trois épisodes d'affilée", "Un paquet de chips", "Des vidéos, encore des vidéos"],
                     marques=["✓", "✓", "✓"], x=170, y=170, w=940),
        "q_vide": dict(type="question", t="Tant de plaisir… et si peu de bonheur ?"),
        "hed": dict(type="mot", t="ἡδονή", g="hêdonê · le plaisir → l'hédonisme", y=250, taille=110),
        "deux": dict(type="cols", g="Tous les plaisirs", gq="courir après chaque plaisir", d="Le tri des plaisirs",
                     dq="en refuser beaucoup pour être heureux", vs="≠"),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 2", t="Le plaisir rend-il heureux ?",
                      sous="Aristippe, Épicure, Calliclès, Mill"),
    }),

    # ------------------------------------------------------------------ I. Aristippe
    dict(id="aristippe", chap="Aristippe : jouir de l'instant", fond="aube", humeur="lumiere", notions=["le temps", "la liberté"],
         retenir="Aristippe : le seul bien est le plaisir présent. Mais même le jouisseur veut rester maître : posséder sans être possédé.",
         beats=[
        "{aristippe}{tab_cyr}Commençons par le plus audacieux. Aristippe, né à Cyrène, en Afrique du Nord, "
        "vers 435 avant notre ère. Il vient à Athènes écouter Socrate… et en tire une leçon inattendue.",
        "{-aristippe}{def_ar}Pour lui, et pour l'école qu'il fonde, les Cyrénaïques, le seul bien, c'est le plaisir. "
        "{def_ar.1}Un plaisir bien précis : un mouvement doux, agréable, ressenti maintenant, dans le corps.",
        "{-def_ar}{pres}Car seul le présent nous appartient. Le passé n'est plus ; l'avenir n'est pas encore. "
        "{pres.1}Alors pourquoi se priver aujourd'hui pour un {#le temps}temps qui ne viendra peut-être jamais ?",
        "{-pres}{-tab_cyr}{tab_lai}Aristippe vit dans le luxe. Il fréquente la cour du tyran Denys de Syracuse, "
        "et une courtisane célèbre, Laïs de Corinthe. Quand on se moque de lui, il répond :",
        ("C", "Je possède Laïs ; mais je ne suis pas possédé de ses agréments, et il est beau de résister à la sensualité, "
              "sans cependant se sevrer des plaisirs.", "c_lais"),
        "{-c_lais}{maitre}Tu vois le paradoxe ? {maitre.1}Même le jouisseur veut rester maître de ses plaisirs, "
        "ne pas en devenir l'esclave. {maitre.2}Jouir, oui ; être possédé, non. "
        "Le plaisir n'est un bien que s'il laisse intacte ma {#la liberté}liberté.",
        "{-maitre}{-tab_lai}{tab_ste2}{lim_ar}Mais le problème saute aux yeux. {lim_ar.1}Un plaisir s'éteint dès qu'il est obtenu : "
        "il faut sans cesse en chercher un autre. {lim_ar.2}Et le plaisir d'aujourd'hui fait parfois la douleur de demain : "
        "la fête, puis le lendemain difficile. {lim_ar.3}Une somme d'instants agréables, est-ce une vie heureuse ?",
        ("Il faudrait un tri. Un calcul. C'est ce que va proposer Épicure.", {"rate": "-4%"}),
        "{-lim_ar}",
    ], vis={
        "aristippe": dict(type="portrait", annee=-435, img="aristippe", nom="Aristippe de Cyrène", dates="v. 435 – v. 356 av. J.-C.",
                          legende="fondateur de l'école cyrénaïque", x=110, y=120, w=330, h=420),
        "tab_cyr": dict(type="tableau", img="bh2-cyrene", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.25, .5, .45],
                        legende="Ruines de Cyrène (Shahat, Libye), ville natale d'Aristippe (photo Waseem Omar, CC BY-SA 4.0)"),
        "def_ar": dict(type="def", terme="Le plaisir selon Aristippe", cles=["mouvement", "maintenant"],
                       t="Le seul bien : un mouvement doux et agréable, ressenti maintenant.",
                       etape="Le plaisir du corps, et du moment présent.", x=170, y=200, w=940),
        "pres": dict(type="mot", t="Carpe diem", g="seul le présent nous appartient (la formule est d'Horace, bien plus tard)",
                     y=250, taille=100),
        "tab_lai": dict(type="tableau", img="bh2-lais", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Hans Holbein le Jeune, Laïs de Corinthe, 1526 (Kunstmuseum, Bâle)"),
        "c_lais": dict(type="cit", a="Aristippe, rapporté par Diogène Laërce", o="Vies des philosophes, II, « Aristippe » (trad. anonyme)",
                       x=170, y=170, w=940),
        "maitre": dict(type="liste", titre="Le paradoxe du jouisseur", items=[
            "Rester maître de ses plaisirs", "Jouir, oui ; être possédé, non"], marques=["1", "2"],
                       cles=["maître", "possédé"], x=170, y=190, w=940),
        "tab_ste2": dict(type="tableau", img="bh2-steen", fond=True, sombre=True, de=[1.4, .4, .3], a=[1.15, .5, .5],
                         legende="Jan Steen, Joyeuse compagnie sur une terrasse, v. 1670 (Metropolitan Museum, New York, CC0)"),
        "lim_ar": dict(type="liste", titre="Les limites", items=[
            "Un plaisir s'éteint : il faut en chercher un autre", "Le plaisir d'aujourd'hui, la douleur de demain",
            "Une somme d'instants fait-elle une vie heureuse ?"], marques=["✗", "✗", "?"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ II. Épicure, le tri des désirs
    dict(id="epicure", chap="Épicure : le tri des désirs", fond="nuit", humeur="calme", notions=["la nature", "la raison"],
         retenir="Épicure : le plaisir est le principe et la fin de la vie heureuse. Mais il faut trier : désirs naturels et nécessaires, naturels seulement, vains.",
         beats=[
        "{epic}{tab_acr}Un siècle plus tard, vers 306 avant notre ère, un philosophe achète un jardin aux portes d'Athènes. "
        "Il y vit avec ses amis, des hommes et des femmes, des esclaves aussi. On appelle son école le Jardin. "
        "Son maître : Épicure.",
        "Il ouvre sa Lettre à Ménécée par une phrase qui fera scandale pendant des siècles.",
        ("C", "C'est pourquoi nous disons que le plaisir est le commencement et la fin de la vie heureuse.", "c_prin"),
        "{-epic}{-c_prin}{pourc}On parlera longtemps des « pourceaux d'Épicure » ; aujourd'hui encore, un épicurien, "
        "c'est un bon vivant. {pourc.1}Contresens complet. Car Épicure ajoute aussitôt que tout plaisir n'est pas bon à prendre.",
        "{-pourc}",
        ("C", "Tout plaisir, pris en lui-même et dans sa nature propre, est donc un bien, et cependant tout plaisir "
              "n'est pas à rechercher.", "c_tri"),
        "{-c_tri}{-tab_acr}{tab_gau}{des}Il faut donc trier ses désirs. Épicure en distingue trois sortes. "
        "{des.1}Les désirs naturels et nécessaires : manger quand on a faim, boire quand on a soif, s'abriter du froid, "
        "avoir des amis. {des.2}Les désirs naturels, mais non nécessaires : des mets raffinés plutôt que du pain. "
        "{des.3}Et les désirs vains, qui ne viennent ni de la {#la nature}nature ni du besoin, mais de l'opinion : "
        "la richesse sans fin, la gloire, le pouvoir.",
        "{-des}{regle}La règle ? {regle.1}Satisfaire les premiers. {regle.2}Accueillir les seconds, sans en dépendre. "
        "{regle.3}Renoncer aux troisièmes : ils n'ont pas de limite, donc ils ne sont jamais satisfaits.",
        "{-regle}{ami}Remarque la place de l'amitié parmi les désirs nécessaires. Pour Épicure, de tous les biens que la sagesse "
        "procure, l'amitié est le plus grand : on ne philosophe pas seul, au Jardin, on vit ensemble. "
        "{ami.1}Le bonheur épicurien n'a rien d'un plaisir solitaire.",
        "{-ami}Et le plus simple peut même devenir le plus délicieux. Écoute :",
        ("C", "Du gros pain et de l'eau procurent le plus vif plaisir à celui qui les porte à sa bouche après en avoir "
              "senti la privation.", "c_pain"),
        "{-c_pain}{calc}C'est un véritable calcul, un travail de la raison. {calc.1}Je refuse un plaisir s'il entraîne "
        "une douleur plus grande. {calc.2}J'accepte une douleur si elle mène à un plaisir plus grand, comme on accepte "
        "un traitement pénible pour guérir.",
        ("Le sage épicurien n'est pas un fêtard. C'est un comptable de ses plaisirs.", {"rate": "-5%"}),
        "{-calc}",
    ], vis={
        "epic": dict(type="portrait", annee=-341, img="epicure", nom="Épicure", dates="341 – 270 av. J.-C.",
                     legende="Lettre à Ménécée", x=110, y=120, w=330, h=420),
        "tab_acr": dict(type="tableau", img="t-acropole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Leo von Klenze, l'Acropole et l'Aréopage d'Athènes, reconstitution, 1846"),
        "c_prin": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 128 (trad. O. Hamelin, 1910)", x=640, y=170, w=570),
        "pourc": dict(type="note", titre="Contresens à éviter", cles=["bon vivant", "Contresens"],
                      t="« Épicurien » ne veut pas dire « bon vivant ».",
                      etape="Épicure trie les plaisirs : beaucoup sont à refuser.", x=170, y=200, w=940),
        "c_tri": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 129 (trad. O. Hamelin, 1910)", x=170, y=170, w=940),
        "tab_gau": dict(type="tableau", img="bh2-gaufrettes", fond=True, sombre=True, de=[1.15, .5, .5], a=[1.4, .45, .5],
                        legende="Lubin Baugin, Le Dessert de gaufrettes, v. 1630-1635 (musée du Louvre ; photo Sailko, CC BY-SA 3.0)"),
        "des": dict(type="cartes", items=[
            dict(ic="porte", t="Naturels et nécessaires", q="manger, boire, s'abriter, l'amitié"),
            dict(ic="chemins", t="Naturels seulement", q="des mets raffinés plutôt que du pain"),
            dict(ic="colonnes", t="Vains", q="la richesse sans fin, la gloire, le pouvoir")]),
        "regle": dict(type="liste", titre="La règle d'Épicure", items=[
            "Naturels et nécessaires : les satisfaire", "Naturels seulement : les accueillir sans en dépendre",
            "Vains : y renoncer, ils n'ont pas de limite"], marques=["✓", "~", "✗"], x=170, y=160, w=940),
        "ami": dict(type="note", titre="L'amitié", cles=["amitié", "solitaire"],
                    t="Pour Épicure, de tous les biens que procure la sagesse, l'amitié est le plus grand.",
                    etape="Le bonheur épicurien n'a rien d'un plaisir solitaire (Maximes capitales, XXVII).", x=170, y=200, w=940),
        "c_pain": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 130-131 (trad. O. Hamelin, 1910)", x=170, y=170, w=940),
        "calc": dict(type="liste", titre="Le calcul des plaisirs", items=[
            "Refuser un plaisir qui entraîne une douleur plus grande",
            "Accepter une douleur qui mène à un plaisir plus grand"], marques=["−", "+"],
                     cles=["refuse", "accepte"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ III. l'ataraxie
    dict(id="ataraxie", chap="Le plaisir en repos", fond="aube", humeur="calme", notions=["la religion", "la science"],
         retenir="Le vrai plaisir est en repos : aponie (le corps sans douleur) et ataraxie (l'âme sans trouble). Le quadruple remède délivre des peurs.",
         beats=[
        "{tab_mer}{q_vrai}Mais alors, quel est le vrai plaisir, selon Épicure ? Pas l'excitation. Le calme.",
        "{-q_vrai}",
        ("C", "Le plaisir dont nous parlons est celui qui consiste, pour le corps, à ne pas souffrir et, pour l'âme, "
              "à être sans trouble.", "c_rep"),
        "{-c_rep}{apo}Deux mots grecs à retenir. {apo.g}L'aponie : l'absence de douleur dans le corps. "
        "{apo.d}L'ataraxie : l'absence de trouble dans l'âme. Comme une mer sans vagues.",
        "{-apo}{mvt}Épicure distingue ainsi deux plaisirs. {mvt.g}Le plaisir en mouvement, celui d'Aristippe : "
        "l'excitation, qui monte et retombe. {mvt.d}Et le plaisir en repos : l'état où plus rien ne manque. "
        "Quand on n'a plus soif, on ne cherche plus à boire.",
        "{-mvt}{-tab_mer}{tab_pap}{quad}Or, qu'est-ce qui trouble l'âme ? Nos peurs. Les disciples d'Épicure ont résumé "
        "le remède en quatre phrases, qu'on lit sur un papyrus carbonisé d'Herculanum, de la main du philosophe Philodème. "
        "{quad.1}Les dieux ne sont pas à craindre. {quad.2}La mort n'est pas à craindre. "
        "{quad.3}Le bien est facile à obtenir. {quad.4}Le mal est facile à supporter.",
        "{-quad}{dieux}Les dieux d'abord. Épicure ne les nie pas : ils existent, bienheureux, et ne s'occupent pas de nous. "
        "{dieux.1}Ce qu'il rejette, c'est la {#la religion}religion de la peur, celle des châtiments et des présages.",
        "{-dieux}{sci}Comment se délivrer de ces terreurs ? Par la connaissance de la nature. Pour Épicure, tout est fait d'atomes "
        "qui se rencontrent dans le vide. {sci.1}L'éclair n'est pas la colère de Zeus : c'est un phénomène naturel. "
        "{sci.2}Comprendre le monde, c'est cesser d'en avoir peur. Deux siècles plus tard, le poète romain Lucrèce "
        "en fera un long poème, De la nature des choses.",
        "{-sci}{-tab_pap}{epic2}Et la mort ? Écoute l'argument : il est célèbre.",
        ("C", "La mort n'est rien pour nous, puisque, tant que nous existons nous-mêmes, la mort n'est pas, "
              "et que, quand la mort existe, nous ne sommes plus.", "c_mort"),
        "{-c_mort}{morts}Tant que je suis là, la mort n'est pas là. Quand elle est là, je n'y suis plus. "
        "{morts.1}Nous ne la rencontrerons jamais : il n'y a rien à craindre.",
        "{-morts}{-epic2}{tab_mer2}{bilan}Voilà le bonheur épicurien. {bilan.1}Peu de besoins, faciles à combler. "
        "{bilan.2}Des amis. {bilan.3}Aucune peur. Une mer sans vagues.",
        "{-bilan}",
    ], vis={
        "tab_mer": dict(type="tableau", img="bh2-mer", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Henry Dawson, Navires sur une mer calme au crépuscule, XIXᵉ siècle"),
        "q_vrai": dict(type="question", t="Quel est le vrai plaisir, selon Épicure ?"),
        "c_rep": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 131 (trad. O. Hamelin, 1910)", x=170, y=170, w=940),
        "apo": dict(type="cols", g="Aponie", gq="le corps : ne pas souffrir", d="Ataraxie", dq="l'âme : être sans trouble", vs="+"),
        "mvt": dict(type="cols", g="Plaisir en mouvement", gq="l'excitation qui monte et retombe (Aristippe)",
                    d="Plaisir en repos", dq="l'état où plus rien ne manque (Épicure)", vs="≠"),
        "tab_pap": dict(type="tableau", img="bh2-papyrus", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .4],
                        legende="Papyrus d'Herculanum (rouleaux 157-152), fac-similé publié par Walter Scott, 1885"),
        "quad": dict(type="liste", titre="Le quadruple remède", items=[
            "Les dieux ne sont pas à craindre", "La mort n'est pas à craindre",
            "Le bien est facile à obtenir", "Le mal est facile à supporter"], marques=["1", "2", "3", "4"],
                     x=170, y=150, w=940),
        "dieux": dict(type="note", titre="Les dieux d'Épicure", cles=["bienheureux", "peur"],
                      t="Ils existent, bienheureux, et ne s'occupent pas de nous.",
                      etape="Ce qu'Épicure rejette : la religion de la peur.", x=170, y=200, w=940),
        "sci": dict(type="liste", titre="Connaître la nature pour ne plus avoir peur", items=[
            "L'éclair n'est pas la colère de Zeus : un phénomène naturel", "Comprendre le monde, c'est cesser d'en avoir peur"],
                    marques=["1", "2"], cles=["atomes", "peur"], x=170, y=180, w=940),
        "epic2": dict(type="portrait", img="epicure", nom="Épicure", dates="341 – 270 av. J.-C.",
                      legende="Lettre à Ménécée, 124-125", x=110, y=120, w=330, h=420),
        "c_mort": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 125 (trad. O. Hamelin, 1910)", x=640, y=150, w=570),
        "morts": dict(type="note", titre="L'argument", cles=["là", "jamais"],
                      t="Tant que je suis là, la mort n'est pas là ; quand elle est là, je n'y suis plus.",
                      etape="Nous ne la rencontrerons jamais.", x=640, y=170, w=570),
        "tab_mer2": dict(type="tableau", img="bh2-mer", fond=True, sombre=True, de=[1.3, .4, .5], a=[1.05, .5, .5],
                         legende="Henry Dawson, Navires sur une mer calme au crépuscule, XIXᵉ siècle"),
        "bilan": dict(type="liste", titre="Le bonheur épicurien", items=[
            "Peu de besoins, faciles à combler", "Des amis", "Aucune peur"], marques=["✓", "✓", "✓"],
                      x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ IV. Calliclès
    dict(id="callicles", chap="Les tonneaux percés", fond="nuit", humeur="tension", notions=["la justice", "la liberté"],
         retenir="Calliclès : le bonheur, c'est l'intensité, verser sans cesse. Socrate : c'est la vie du pluvier. Plus on veut de plaisir, plus il faut de manque.",
         beats=[
        "{tab_alc}Épicure vante le repos. Tout le monde n'est pas d'accord. Platon, déjà, avait mis le débat en scène. "
        "Ici, le peintre Regnault montre Socrate arrachant son élève Alcibiade aux bras de la Volupté.",
        "{-tab_alc}{tab_dan}{ton2}On l'a vu dans la série sur la liberté : dans le Gorgias, le jeune Calliclès veut laisser "
        "ses désirs grandir le plus possible, et Socrate lui oppose une image. {ton2.1}Le sage a des tonneaux sains : "
        "une fois remplis, il est tranquille. {ton2.2}L'insatiable a des tonneaux percés : {ton2.3}il doit verser sans fin.",
        "{-ton2}Mais la réponse de Calliclès mérite qu'on aille plus loin. Elle n'est pas bête du tout.",
        ("C", "L'homme aux tonneaux pleins n'a plus aucun plaisir, et c'est cela que j'appelais tout à l'heure "
              "vivre à la façon d'une pierre.", "c_pierre"),
        "{-c_pierre}{pierre}Retourne l'argument contre Épicure. {pierre.1}Le sage sans manque, sans désir, ne serait-il pas… "
        "une pierre ? {pierre.2}Pour Calliclès, le plaisir, c'est le flux : verser, verser encore. "
        "Mieux vaut une vie intense qu'une vie tranquille.",
        ("Avoue que l'objection est forte.", {"rate": "-6%"}),
        "{-pierre}{-tab_dan}{tab_plu}{pluv}Socrate répond par deux images, plus cruelles. {pluv.1}La vie que tu vantes, "
        "dit-il, c'est celle du pluvier : un oiseau qui, disait-on, rejette l'eau à peine l'a-t-il bue. "
        "{pluv.2}Ou celle d'un homme qui a la gale, et passe sa vie à se gratter. Il éprouve un plaisir sans fin… "
        "Est-il heureux ?",
        "{-pluv}{-tab_plu}{tab_alc2}{lec}La leçon va loin. {lec.1}Si le plaisir naît du remplissage d'un manque, "
        "alors plus je veux de plaisir, plus il me faut de manque. {lec.2}La vie de plaisirs intenses est une vie "
        "de démangeaisons. {lec.3}Le plaisir ainsi compris est toujours mêlé de douleur.",
        "{-lec}{-tab_alc2}{tab_ecr}{auj}Ce tonneau percé, tu le connais : c'est notre soirée de vendredi. {auj.1}La vidéo suivante, "
        "le message suivant, la série suivante. {auj.2}Chaque plaisir est bref, et il laisse derrière lui un petit manque, "
        "qui appelle le plaisir suivant. On n'est jamais rempli : on est occupé.",
        "{-auj}{q_deb}Le débat reste ouvert, et il fait de très bons sujets de dissertation : "
        "vaut-il mieux une vie intense, ou une vie tranquille ?",
        "{-q_deb}",
    ], vis={
        "tab_alc": dict(type="tableau", img="bh2-alcibiade", de=[1.0, .5, .5], a=[1.25, .45, .4],
                        legende="Jean-Baptiste Regnault, Socrate arrachant Alcibiade du sein de la Volupté, 1791 (musée du Louvre)"),
        "tab_dan": dict(type="tableau", img="t-danaides", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .6],
                        legende="John William Waterhouse, Les Danaïdes, 1906 · condamnées à remplir sans fin des jarres percées"),
        "ton2": dict(type="illu", nom="tonneaux", x=140, y=100, w=1000, h=500),
        "c_pierre": dict(type="cit", a="Calliclès, dans Platon", o="Gorgias, 494a-b (trad. É. Chambry)", x=170, y=170, w=940),
        "pierre": dict(type="liste", titre="L'objection de Calliclès", items=[
            "Le sage sans désir… une pierre ?", "Le plaisir, c'est le flux : mieux vaut l'intensité"],
                       marques=["?", "→"], cles=["pierre", "intensité"], x=170, y=190, w=940),
        "tab_plu": dict(type="tableau", img="bh2-pluvier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Robert Havell d'après John James Audubon, Pluvier doré, 1836 (National Gallery of Art, Washington, CC0)"),
        "pluv": dict(type="liste", titre="Les deux images de Socrate", items=[
            "Le pluvier : il rejette l'eau à peine l'a-t-il bue", "Le galeux : se gratter sans fin… est-ce être heureux ?"],
                     marques=["1", "2"], x=170, y=180, w=940),
        "tab_alc2": dict(type="tableau", img="bh2-alcibiade", fond=True, sombre=True, de=[1.4, .3, .45], a=[1.15, .5, .5],
                         legende="Jean-Baptiste Regnault, Socrate arrachant Alcibiade du sein de la Volupté, 1791 (musée du Louvre)"),
        "lec": dict(type="liste", titre="La leçon", items=[
            "Plus de plaisir exige plus de manque", "Une vie intense, une vie de démangeaisons",
            "Le plaisir est mêlé de douleur"], marques=["1", "2", "3"], x=170, y=160, w=940),
        "tab_ecr": dict(type="tableau", img="t-ecrans", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .6, .4],
                        legende="Photo Rawpixel, CC BY 2.0"),
        "auj": dict(type="liste", titre="Le tonneau percé, aujourd'hui", items=[
            "La vidéo suivante, le message suivant, la série suivante",
            "Chaque plaisir laisse un petit manque, qui appelle le suivant"], marques=["↻", "↻"], x=170, y=180, w=940),
        "q_deb": dict(type="question", t="Vaut-il mieux une vie intense, ou une vie tranquille ?"),
    }),

    # ------------------------------------------------------------------ V. Mill, pour aller plus loin
    dict(id="mill", chap="Pour aller plus loin : Mill", fond="aube", humeur="mystere", notions=["le devoir", "la conscience"],
         retenir="Mill : certains plaisirs valent mieux que d'autres. Et le paradoxe de l'hédonisme : qui vise directement le bonheur le manque.",
         beats=[
        "{mill}{tab_win}Dernier rebondissement, au dix-neuvième siècle, en Angleterre. Jeremy Bentham, le fondateur "
        "de l'utilitarisme, veut calculer les plaisirs comme on fait des comptes : leur intensité, leur durée, leur certitude. "
        "Pour lui, seule compte la quantité : un plaisir en vaut un autre. On l'a vu dans la série sur le {#le devoir}devoir.",
        "{-mill}{qual}Son disciple, John Stuart Mill, n'est pas d'accord. {qual.1}Certains plaisirs sont supérieurs : "
        "ceux de l'esprit, de l'amitié, de l'art. {qual.2}Comment le savoir ? Demande à ceux qui ont connu les deux sortes : "
        "ils ne voudraient pas échanger.",
        "{-qual}{soc}D'où sa formule, déjà rencontrée : mieux vaut être Socrate insatisfait qu'un imbécile satisfait.",
        "{-soc}{dep}Mais regarde ce que Mill vient de faire. {dep.1}Pour classer les plaisirs, il lui faut un critère "
        "qui n'est plus le plaisir : la dignité, la valeur de l'esprit. {dep.2}L'hédonisme commence à se dépasser lui-même.",
        "{-dep}{rec_mill}{crise}Et Mill a vécu, à vingt ans, une expérience troublante. {crise.1}Élevé par son père comme une machine à penser, "
        "{crise.2}il tombe dans une profonde dépression : rien ne lui fait plus plaisir. {crise.3}Il en sort peu à peu, en lisant des poèmes, "
        "ceux de Wordsworth, le poète des lacs.",
        "{-rec_mill}{-crise}{par}Il en tire une leçon, dans son Autobiographie. {par.1}Demande-toi si tu es heureux, et tu cesses de l'être. "
        "{par.2}Le bonheur ne se vise pas directement : il vient de surcroît, quand on s'occupe d'autre chose. "
        "Des autres, d'une œuvre, d'une cause.",
        ("Comme un chat qu'on poursuit : il s'enfuit. Mais il vient s'asseoir près de toi quand tu lis.", {"rate": "-5%"}),
        "{-par}",
    ], vis={
        "mill": dict(type="portrait", annee=1806, img="mill", nom="John Stuart Mill", dates="1806 – 1873",
                     legende="L'Utilitarisme (1861) · Autobiographie (1873)", x=110, y=120, w=330, h=420),
        "tab_win": dict(type="tableau", img="bh2-windermere", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .5],
                        legende="John Atkinson Grimshaw, Windermere, XIXᵉ siècle (Yale University Art Gallery)"),
        "qual": dict(type="liste", titre="La qualité des plaisirs", items=[
            "Certains plaisirs sont supérieurs : l'esprit, l'amitié, l'art",
            "Le test : ceux qui ont connu les deux ne veulent pas échanger"], marques=["1", "2"],
                     cles=["supérieurs", "échanger"], x=170, y=180, w=940),
        "soc": dict(type="mot", t="Socrate insatisfait", g="vaut mieux qu'un imbécile satisfait (Mill, L'Utilitarisme, 1861)",
                    y=250, taille=88),
        "dep": dict(type="note", titre="Pour aller plus loin", cles=["critère", "dépasser"],
                    t="Pour classer les plaisirs, Mill a besoin d'un critère qui n'est plus le plaisir.",
                    etape="L'hédonisme commence à se dépasser lui-même.", x=170, y=190, w=940),
        "crise": dict(type="liste", titre="La crise de Mill", items=[
            "Élevé par son père comme une machine à penser",
            "À vingt ans, plus rien ne lui fait plaisir",
            "Il en sort par la poésie : Wordsworth"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "rec_mill": dict(type="tag", style="plus", t="1826 · la « crise » de Mill, à vingt ans", x=170, y=560, w=620),
        "par": dict(type="def", terme="Le paradoxe de l'hédonisme", cles=["heureux", "surcroît"],
                    t="Demande-toi si tu es heureux, et tu cesses de l'être (Mill, Autobiographie, chap. V, trad. courante).",
                    etape="Le bonheur vient de surcroît, quand on s'occupe d'autre chose.", x=170, y=190, w=940, plus=True),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_mer3}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Aristippe. Le seul bien est le plaisir présent ; "
        "mais même le jouisseur veut rester maître.",
        "{rec.2}Deux : Épicure. Le plaisir est le principe de la vie heureuse, à condition de trier ses désirs : "
        "naturels et nécessaires, naturels seulement, vains.",
        "{rec.3}Trois : le vrai plaisir est en repos. Aponie, ataraxie, et le quadruple remède contre nos peurs.",
        "{rec.4}Quatre : Calliclès et Socrate. Intensité ou tranquillité ? Et Mill : le bonheur se dérobe quand on le vise.",
        "{-rec}{-tab_mer3}{tab_fin}{q_suite}Et si le bonheur n'était pas une sensation, mais une manière de vivre ? "
        "Une activité, une sagesse ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : la sagesse des Anciens. Aristote, les stoïciens, et Spinoza.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_mer3": dict(type="tableau", img="bh2-mer", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                         legende="Henry Dawson, Navires sur une mer calme au crépuscule, XIXᵉ siècle"),
        "rec": dict(type="carte", centre="LE PLAISIR", branches=[
            dict(t="Aristippe", items=["le plaisir présent", "posséder sans être possédé"]),
            dict(t="Épicure", items=["principe et fin", "trier ses désirs", "le calcul des plaisirs"]),
            dict(t="Le plaisir en repos", items=["aponie, ataraxie", "le quadruple remède"]),
            dict(t="Les objections", items=["Calliclès : l'intensité", "Socrate : le pluvier", "Mill : qualité, paradoxe"])]),
        "tab_fin": dict(type="tableau", img="bh2-alexandre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Charles Laplante, Aristote et le jeune Alexandre, gravure, 1866"),
        "q_suite": dict(type="question", t="Et si le bonheur n'était pas une sensation, mais une manière de vivre ?"),
        "fin": dict(type="titre", sur="À suivre", t="La sagesse des Anciens", sous="Épisode 3 · Aristote, les stoïciens, Spinoza"),
    }),
]

QUIZ = [
    dict(q="Pour Aristippe et les Cyrénaïques, le seul bien est…",
         r=["l'absence de trouble de l'âme", "le plaisir présent, un mouvement doux ressenti maintenant",
            "la vertu", "la contemplation"], ok=1,
         voir="def_ar", ex="Le plaisir du corps et du moment présent : le passé n'est plus, l'avenir n'est pas encore."),
    dict(q="« Je possède Laïs, mais je ne suis pas possédé » : que veut dire Aristippe ?",
         r=["Qu'il faut renoncer aux plaisirs", "Qu'on peut jouir sans devenir l'esclave de ses plaisirs",
            "Que l'amour est une illusion", "Que la richesse fait le bonheur"], ok=1,
         voir="c_lais", ex="Même le jouisseur veut rester maître : le plaisir n'est un bien que s'il laisse intacte la liberté."),
    dict(q="Selon Épicure, le désir de gloire est un désir…",
         r=["naturel et nécessaire", "naturel mais non nécessaire", "vain", "nécessaire au bonheur"], ok=2,
         voir="des", ex="Il vient de l'opinion, non de la nature ni du besoin ; il n'a pas de limite, donc il n'est jamais satisfait."),
    dict(q="Que signifie « ataraxie » ?",
         r=["L'absence de douleur dans le corps", "L'absence de trouble dans l'âme", "Le plaisir intense", "La vertu morale"], ok=1,
         voir="apo", ex="Aponie : le corps sans douleur. Ataraxie : l'âme sans trouble. Ensemble, le plaisir en repos d'Épicure."),
    dict(q="Pourquoi, selon Épicure, la mort n'est-elle « rien pour nous » ?",
         r=["Parce que l'âme est immortelle", "Parce que, tant que nous sommes, elle n'est pas ; quand elle est, nous ne sommes plus",
            "Parce que les dieux nous protègent", "Parce qu'elle est un plaisir"], ok=1,
         voir="c_mort", ex="Lettre à Ménécée, 125 : bien et mal sont dans la sensation ; la mort est la privation de toute sensation."),
    dict(q="Que reproche Calliclès à l'homme aux tonneaux pleins ?",
         r=["D'être injuste", "De vivre à la façon d'une pierre, sans plus aucun plaisir",
            "D'être trop riche", "De ne pas connaître les dieux"], ok=1,
         voir="c_pierre", ex="Pour Calliclès, le plaisir est dans le flux, dans l'intensité ; Socrate répond par le pluvier et le galeux."),
    dict(q="Qu'est-ce que le « paradoxe de l'hédonisme » tiré de l'expérience de Mill ?",
         r=["Plus on a de plaisirs, plus on est heureux", "Celui qui vise directement le bonheur le manque : il vient de surcroît",
            "Tous les plaisirs se valent", "Le plaisir est toujours mauvais"], ok=1,
         voir="par", ex="« Demande-toi si tu es heureux, et tu cesses de l'être » : le bonheur accompagne une activité tournée vers autre chose."),
]

CREDITS = [
    "Portraits : Aristippe (gravure, dans Thomas Stanley, The History of Philosophy, 1655, domaine public) ; Épicure ; John Stuart Mill : domaine public",
    "Tableaux et gravures : Jan Steen, Joyeuse compagnie sur une terrasse (v. 1670, Metropolitan Museum, CC0) ; "
    "Hans Holbein le Jeune, Laïs de Corinthe (1526) ; Leo von Klenze, l'Acropole (1846) ; "
    "Lubin Baugin, Le Dessert de gaufrettes (v. 1630-1635, photo Sailko, CC BY-SA 3.0) ; Henry Dawson, Navires sur une mer calme ; "
    "Jean-Baptiste Regnault, Socrate arrachant Alcibiade du sein de la Volupté (1791) ; John William Waterhouse, Les Danaïdes (1906) ; "
    "Robert Havell d'après Audubon, Pluvier doré (1836, NGA, CC0) ; John Atkinson Grimshaw, Windermere ; "
    "Charles Laplante, Aristote et Alexandre (1866) : domaine public sauf mention",
    "Photographies et documents : ruines de Cyrène (Waseem Omar, CC BY-SA 4.0) ; papyrus d'Herculanum, fac-similé de Walter Scott (1885, domaine public) ; foule et téléphones (Rawpixel, CC BY 2.0)",
    "Citations : Diogène Laërce, Vies des philosophes, « Aristippe » (trad. anonyme, Wikisource) ; Épicure, Lettre à Ménécée, "
    "trad. Octave Hamelin (1910), Wikisource ; Platon, Gorgias, trad. Émile Chambry, Wikisource.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
