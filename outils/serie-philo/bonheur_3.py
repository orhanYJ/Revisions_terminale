"""Le bonheur, épisode 3 : « La sagesse des Anciens »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la raison} dans le texte lu.
Citations : Aristote, Éthique à Nicomaque, trad. J.-F. Thurot (1823), Wikisource ; Épictète, Manuel, VIII, trad. J.-M. Guyau
(1875), Wikisource ; Sénèque, De la vie heureuse, I, trad. J. Baillard, Wikisource ; Marc Aurèle, Pensées, IV, 3,
trad. A. Couat (1904), Wikisource ; Spinoza, Éthique, trad. É. Saisset (1861), Wikisource.
Crésus et Solon : Hérodote, Histoires, I, 30-33 et 86, résumé par le narrateur.
"""

CODE = "bonheur-3"
NOTION = "Le bonheur"
NUM = 3
TITRE = "La sagesse des Anciens"
SUIVANT = "Épisode 4 · Le bonheur est-il une illusion ?"
PRONONCIATION = {"Tellos": "Tèlosse", "Cyrus": "Cirusse", "Priam": "Priame", "Gallion": "Galion", "Myson": "Mison",
                 "Zénon": "Zénon", "Stoa": "Stoa"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_cre}{q_cre}Sardes, en Lydie, au sixième siècle avant notre ère. Le roi Crésus est l'homme le plus riche du monde. "
        "Il reçoit un sage venu d'Athènes, Solon, lui fait visiter ses trésors, puis lui demande : "
        "qui est l'homme le plus heureux que tu aies rencontré ?",
        "{-q_cre}{tellos}Crésus attend son propre nom. Solon répond : Tellos, un Athénien. "
        "{tellos.1}Il a vécu dans une cité prospère. {tellos.2}Il a vu grandir ses enfants, et naître ses petits-enfants. "
        "{tellos.3}Et il est mort en défendant sa patrie, honoré de tous.",
        "{-tellos}{sol}Crésus s'agace : et moi ? La réponse de Solon, en substance : "
        "ne dis personne heureux avant sa mort. Tant que la vie n'est pas finie, la roue peut tourner.",
        "{-sol}{-tab_cre}{tab_buc}{an}Quelques années plus tard, Crésus est vaincu par le roi perse Cyrus. "
        "On le place sur un bûcher. Et là, raconte Hérodote, il appelle trois fois : Solon ! Solon ! Solon !",
        ("Il venait de comprendre.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-an}{q_sag}Le bonheur ne serait donc pas ce que l'on possède, mais la manière dont on mène toute sa vie ? "
        "C'est la grande idée des sages de l'Antiquité.",
        ("P", 0.3),
        "{-q_sag}{-tab_buc}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_cre": dict(type="tableau", img="bh3-cresus", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Gaspar van den Hoecke, Crésus montrant ses trésors à Solon, XVIIᵉ s. (Musée national, Varsovie)"),
        "q_cre": dict(type="question", t="Qui est l'homme le plus heureux que tu aies rencontré ?"),
        "tellos": dict(type="liste", titre="Tellos d'Athènes, selon Solon", items=[
            "Une cité prospère", "Des enfants, des petits-enfants", "Une mort glorieuse, honoré de tous"],
                       marques=["1", "2", "3"], x=170, y=170, w=940),
        "sol": dict(type="mot", t="Avant sa mort ?", g="« Ne dis personne heureux avant sa mort » · Hérodote, Histoires, I, 32",
                    y=250, taille=96),
        "tab_buc": dict(type="tableau", img="bh3-bucher", fond=True, sombre=True, de=[1.0, .45, .5], a=[1.3, .4, .4],
                        legende="Myson, Crésus sur son bûcher, amphore attique, v. 500-490 av. J.-C. (musée du Louvre, G 197)"),
        "an": dict(type="tag", style="repere", t="Hérodote, Histoires, I, 86 · « Solon ! Solon ! Solon ! »", x=170, y=560, w=720),
        "q_sag": dict(type="question", t="Le bonheur : ce que l'on possède, ou la manière de mener sa vie ?"),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 3", t="La sagesse des Anciens",
                      sous="Aristote, les stoïciens, Spinoza"),
    }),

    # ------------------------------------------------------------------ I. Aristote
    dict(id="aristote", chap="Aristote : bien vivre, c'est bien agir", fond="aube", humeur="lumiere", notions=["la raison", "la nature"],
         retenir="Aristote : le bonheur est l'activité de l'âme conforme à la vertu, dans une vie complète. Il ne se possède pas : il se fait.",
         beats=[
        "{arist}{tab_lyc}Aristote connaît l'histoire de Solon : il la discute dans l'Éthique à Nicomaque. "
        "On l'a vu dans l'épisode un : pour lui, le bonheur est la fin dernière. Mais en quoi consiste-t-il ?",
        "{-arist}{fonc}Sa méthode est simple. {fonc.1}Un bon joueur de flûte, c'est celui qui joue bien de la flûte. "
        "{fonc.2}Un bon sculpteur, celui qui sculpte bien. {fonc.3}Chaque être est bon quand il accomplit bien "
        "sa fonction propre. Alors, quelle est la fonction propre de l'homme ?",
        "{-fonc}{rai}Se nourrir, grandir ? Les plantes le font aussi. Sentir ? Les animaux aussi. "
        "Ce qui n'appartient qu'à l'homme, c'est la {#la raison}raison. "
        "{rai.1}L'homme heureux sera donc celui qui vit selon la raison, et qui le fait excellemment.",
        "{-rai}{-tab_lyc}{arist2}{tab_hir}D'où sa définition.",
        ("C", "Le bien de l'homme est l'activité de l'âme dirigée par la vertu ; et, s'il y a plusieurs vertus, "
              "par celle qui est la plus parfaite, et de plus dans une vie parfaite.", "c_act"),
        "{-c_act}Et il ajoute un proverbe.",
        ("C", "Une hirondelle ne fait pas le printemps, ni aussi un seul jour ; de même un seul jour, ou un temps très-court, "
              "ne suffit pas pour rendre un homme complètement heureux.", "c_hir"),
        "{-arist2}{-c_hir}{-tab_hir}{tab_cou}{mots}Trois mots à peser. {mots.1}Activité : le bonheur n'est pas un état "
        "qu'on possède, comme un trésor ; c'est quelque chose qu'on fait. Aux jeux Olympiques, dit Aristote, "
        "ce ne sont pas les plus beaux ni les plus forts qui reçoivent la couronne, mais ceux qui combattent.",
        "{mots.2}Vertu, au sens grec : l'excellence, comme on parle de l'excellence d'un athlète. "
        "{mots.3}Une vie complète : Solon avait raison, le bonheur se juge sur la durée.",
        "{-mots}{-tab_cou}{tab_cre2}{ext}Mais Aristote est réaliste. {ext.1}Pour bien agir, il faut aussi quelques biens "
        "extérieurs : la santé, un peu de richesse, des amis, une cité. {ext.2}Celui qui tombe dans les malheurs de Priam, "
        "le vieux roi de Troie qui perd tout, on ne peut pas le dire heureux. "
        "{ext.3}Le bonheur dépend surtout de nous… mais pas entièrement.",
        "{-ext}",
    ], vis={
        "arist": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      legende="Éthique à Nicomaque", x=110, y=120, w=330, h=420),
        "tab_lyc": dict(type="tableau", img="bh3-lycee", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .55],
                        legende="Athènes, vestiges du Lycée, l'école d'Aristote (photo George E. Koronaios, CC0)"),
        "fonc": dict(type="liste", titre="La fonction propre", items=[
            "Le bon joueur de flûte : il joue bien", "Le bon sculpteur : il sculpte bien",
            "Et l'homme ? Quelle est sa fonction propre ?"], marques=["1", "2", "?"], x=170, y=170, w=940),
        "rai": dict(type="def", terme="Le propre de l'homme", cles=["raison", "excellemment"],
                    t="Ni se nourrir (les plantes), ni sentir (les animaux) : la raison.",
                    etape="L'homme heureux vit selon la raison, et le fait excellemment.", x=170, y=200, w=940),
        "arist2": dict(type="portrait", img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                       legende="Éthique à Nicomaque, livre I", x=110, y=120, w=330, h=420),
        "tab_hir": dict(type="tableau", img="bh3-hirondelle", fond=True, sombre=True, de=[1.0, .5, .7], a=[1.4, .5, .78],
                        legende="Hirondelles, planche de la Naturgeschichte der Vögel Deutschlands de J. A. Naumann, XIXᵉ s. (domaine public)"),
        "c_act": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, I, 7, trad. Thurot (1823)", x=640, y=150, w=570),
        "c_hir": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, I, 7, trad. Thurot (1823)", x=640, y=150, w=570),
        "tab_cou": dict(type="tableau", img="bh3-coureurs", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Coureurs sur une amphore panathénaïque, v. 530 av. J.-C. (Metropolitan Museum ; photo Ismoon, CC BY-SA 4.0)"),
        "mots": dict(type="liste", titre="Trois mots à peser", items=[
            "Activité : le bonheur se fait, il ne se possède pas", "Vertu : l'excellence (arétè)",
            "Une vie complète : il se juge sur la durée"], marques=["1", "2", "3"],
                     cles=["Activité", "Vertu", "complète"], x=170, y=160, w=940),
        "tab_cre2": dict(type="tableau", img="bh3-cresus", fond=True, sombre=True, de=[1.4, .3, .4], a=[1.15, .5, .5],
                         legende="Gaspar van den Hoecke, Crésus montrant ses trésors à Solon, XVIIᵉ s. (Musée national, Varsovie)"),
        "ext": dict(type="liste", titre="Le réalisme d'Aristote", items=[
            "Il faut aussi des biens extérieurs : santé, un peu de richesse, des amis, une cité",
            "Les malheurs de Priam : on ne peut pas le dire heureux",
            "Le bonheur dépend surtout de nous… pas entièrement"], marques=["+", "✗", "→"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ II. devenir vertueux
    dict(id="vertu", chap="Devenir vertueux", fond="nuit", humeur="calme", notions=["la justice", "la technique"],
         retenir="On devient juste en pratiquant la justice : la vertu est une habitude. Le juste milieu entre deux excès est un sommet, pas une moyenne.",
         beats=[
        "{tab_cou2}{q_dev}Comment devient-on vertueux ? Pas en lisant des livres de morale. En s'exerçant.",
        "{-q_dev}",
        ("C", "En bâtissant on devient maçon, en jouant de la lyre, on devient musicien ; et de même en pratiquant "
              "la justice, on devient juste.", "c_hab"),
        "{-c_hab}{hab}{hab.1}La vertu n'est ni un don, ni un savoir : c'est une habitude, une disposition qu'on acquiert. "
        "{hab.2}Au début, être courageux ou généreux coûte un effort. Puis cela devient une seconde nature, "
        "et même un plaisir : l'homme vertueux aime bien agir.",
        "{-hab}{-tab_cou2}{tab_blo}{mil}Et que vise cette habitude ? Le juste milieu. {mil.1}Le courage est le milieu entre "
        "la lâcheté, qui manque d'audace, {mil.2}et la témérité, qui en a trop. "
        "{mil.3}La générosité, entre l'avarice et la prodigalité.",
        "{-mil}",
        ("C", "La vertu est un certain milieu entre deux vices, l'un par excès, l'autre par défaut.", "c_mil"),
        "{-c_mil}{som}Attention au contresens : le juste milieu n'est pas la moyenne, ni la tiédeur. "
        "{som.1}C'est un sommet entre deux pentes. Comme ce funambule au-dessus du Niagara : un pas de trop, d'un côté "
        "ou de l'autre, et c'est la chute.",
        "{som.2}Et ce milieu se trouve en situation, chaque fois. Ce qui est courageux pour un soldat ne l'est pas "
        "pour un médecin. La {#la justice}justice elle-même, dit Aristote, est une affaire de juste mesure : "
        "ne prendre ni trop, ni trop peu.",
        ("Tenir le juste milieu, avoue-t-il, est une tâche difficile.", {"rate": "-5%"}),
        "{-som}",
    ], vis={
        "tab_cou2": dict(type="tableau", img="bh3-coureurs", fond=True, sombre=True, de=[1.35, .4, .45], a=[1.1, .55, .5],
                         legende="Coureurs sur une amphore panathénaïque, v. 530 av. J.-C. (Metropolitan Museum ; photo Ismoon, CC BY-SA 4.0)"),
        "q_dev": dict(type="question", t="Comment devient-on vertueux ?"),
        "c_hab": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, II, 1, trad. Thurot (1823)", x=170, y=170, w=940),
        "hab": dict(type="def", terme="La vertu, une habitude", cles=["habitude", "seconde nature"],
                    t="Ni un don, ni un savoir : une disposition acquise par l'exercice.",
                    etape="D'abord un effort, puis une seconde nature, et même un plaisir.", x=170, y=200, w=940),
        "tab_blo": dict(type="tableau", img="bh3-blondin", fond=True, sombre=True, de=[1.0, .45, .65], a=[1.3, .4, .7],
                        legende="William England, Blondin traversant le Niagara sur une corde, 1859 (domaine public)"),
        "mil": dict(type="liste", titre="Le juste milieu", items=[
            "Défaut : la lâcheté", "Excès : la témérité → milieu : le courage",
            "Avarice / prodigalité → milieu : la générosité"], marques=["−", "+", "="], x=170, y=170, w=940),
        "c_mil": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, II, 9, trad. Thurot (1823)", x=170, y=190, w=940),
        "som": dict(type="note", titre="Contresens à éviter", cles=["sommet", "situation"],
                    t="Le juste milieu n'est pas la moyenne : c'est un sommet entre deux pentes.",
                    etape="Il se trouve en situation : le courage du soldat n'est pas celui du médecin.", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ III. amitié, contemplation
    dict(id="amis", chap="Des amis, et la vie de l'esprit", fond="aube", humeur="lumiere", notions=["la vérité", "l'État"],
         retenir="Pas de bonheur sans amis : l'homme est un être fait pour vivre avec d'autres. Le bonheur le plus haut : la contemplation, la vie de l'intelligence.",
         beats=[
        "{tab_kyl}{suff}Le bonheur se suffit à lui-même, disait Aristote. Mais attention : se suffire, ce n'est pas vivre seul. "
        "{suff.1}L'homme est un animal politique, fait pour vivre dans une cité, avec d'autres. "
        "D'où cette phrase, au début du livre huit.",
        "{-suff}",
        ("C", "Il n'est personne qui consentît à vivre privé d'amis, dût-il posséder tous les autres biens.", "c_ami"),
        "{-c_ami}{ami3}Aristote distingue trois amitiés. {ami3.1}L'amitié utile : on se fréquente parce qu'on se rend service. "
        "{ami3.2}L'amitié agréable : parce qu'on s'amuse ensemble. {ami3.3}Et l'amitié vertueuse : "
        "on aime l'autre pour ce qu'il est. Les deux premières se défont quand l'utilité ou le plaisir disparaissent ; "
        "la troisième dure.",
        "{-ami3}{achi}Regarde Achille qui panse la blessure de son ami Patrocle, sur cette coupe vieille de vingt-cinq siècles. "
        "{achi.1}L'ami véritable, dit Aristote, est un autre soi-même.",
        "{-achi}{-tab_kyl}{tab_geo}{cont}Reste une dernière surprise, à la fin du livre. Quelle est la vie la plus heureuse ? "
        "{cont.1}Ni la vie de plaisirs, qui est celle des bêtes. {cont.2}Ni même la vie politique, pleine d'honneurs, "
        "mais agitée. {cont.3}C'est la vie contemplative : celle de l'intelligence qui cherche à connaître la "
        "{#la vérité}vérité, pour le seul plaisir de comprendre.",
        "{-cont}{div}C'est l'activité la plus continue, la plus libre, celle qui se suffit le plus à elle-même. "
        "{div.1}Aristote la dit presque divine : le savant, le chercheur, le philosophe approchent un bonheur "
        "que seuls les dieux possèdent pleinement. {div.2}Une vie au-dessus de la condition humaine, reconnaît-il… "
        "mais vers laquelle il faut tendre autant qu'on le peut.",
        "{-div}",
    ], vis={
        "tab_kyl": dict(type="tableau", img="bh3-kylix", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .5],
                        legende="Peintre de Sosias, Achille pansant Patrocle, coupe attique, v. 500 av. J.-C. (Altes Museum, Berlin ; photo Dosseman, CC BY-SA 4.0)"),
        "suff": dict(type="note", titre="Se suffire à soi-même", cles=["seul", "politique"],
                     t="Se suffire, ce n'est pas vivre seul.",
                     etape="L'homme est un animal politique, fait pour vivre avec d'autres.", x=170, y=200, w=940),
        "c_ami": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, VIII, 1, trad. Thurot (1823)", x=170, y=190, w=940),
        "ami3": dict(type="cartes", items=[
            dict(ic="porte", t="L'amitié utile", q="on se rend service"),
            dict(ic="chemins", t="L'amitié agréable", q="on s'amuse ensemble"),
            dict(ic="colonnes", t="L'amitié vertueuse", q="on aime l'autre pour ce qu'il est")]),
        "achi": dict(type="mot", t="Un autre soi-même", g="Aristote, Éthique à Nicomaque, IX · l'ami véritable", y=250, taille=96),
        "tab_geo": dict(type="tableau", img="bh3-geographe", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .45, .4],
                        legende="Johannes Vermeer, Le Géographe, 1669 (Städel Museum, Francfort)"),
        "cont": dict(type="liste", titre="Quelle vie est la plus heureuse ?", items=[
            "La vie de plaisirs : celle des bêtes", "La vie politique : des honneurs, mais l'agitation",
            "La vie contemplative : comprendre, pour comprendre"], marques=["✗", "~", "✓"], x=170, y=160, w=940),
        "div": dict(type="def", terme="La vie contemplative", cles=["continue", "divine", "tendre"],
                    t="L'activité la plus continue, la plus libre, qui se suffit le plus à elle-même.",
                    etape="Presque divine : au-dessus de la condition humaine, mais il faut y tendre.", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ IV. les stoïciens
    dict(id="stoiciens", chap="Les stoïciens : la vertu suffit", fond="nuit", humeur="calme", notions=["la nature", "la liberté"],
         retenir="Les stoïciens : vivre en accord avec la nature ; la vertu suffit au bonheur. Vouloir ce qui arrive, et se retirer dans sa citadelle intérieure.",
         beats=[
        "{tab_sto}{zen}Athènes, vers 300 avant notre ère. Sous un portique couvert de peintures, la Stoa, le philosophe Zénon "
        "enseigne. Ses disciples prendront le nom du lieu : les stoïciens.",
        "{-zen}{sto_def}Pour eux, être heureux, c'est vivre en accord avec la {#la nature}nature, c'est-à-dire avec la raison "
        "qui ordonne le monde. {sto_def.1}Et ils vont plus loin qu'Aristote : la vertu suffit au bonheur. "
        "La santé, la richesse, la réputation ne sont ni des biens ni des maux. Elles sont indifférentes.",
        "{-sto_def}{-tab_sto}{epic}{tab_hie}On l'a vu dans la série sur la liberté avec Épictète : il y a ce qui dépend de nous, "
        "nos jugements, et ce qui n'en dépend pas. Le stoïcien en tire une recette du bonheur, la plus exigeante qui soit.",
        ("C", "Ne demande pas que ce qui arrive arrive comme tu le veux, mais veux ce qui arrive comme il arrive, "
              "et tu couleras une vie heureuse.", "c_epi"),
        "{-c_epi}{-epic}{vou}Tu ne peux pas empêcher la pluie le jour de ta fête. Mais tu peux cesser d'exiger qu'il fasse beau. "
        "{vou.1}Le malheur, c'est l'écart entre ce que je veux et ce qui arrive. Le stoïcien le supprime… "
        "en changeant ce qu'il veut.",
        "{-vou}{-tab_hie}{sen}{tab_sen}Sénèque, conseiller de l'empereur Néron, consacre un traité entier à la question : "
        "De la vie heureuse. Il commence ainsi.",
        ("C", "Vivre heureux, mon frère Gallion, voilà ce que veulent tous les hommes : quant à bien voir ce qui fait "
              "le bonheur, quel nuage sur leurs yeux !", "c_sen"),
        "{-c_sen}{sen_n}Sénèque, d'ailleurs, est immensément riche, et on le lui reproche. Il répond, comme Aristippe "
        "avant lui : {sen_n.1}le sage peut avoir des richesses, à condition qu'elles ne l'aient pas.",
        "{-sen_n}{-sen}{-tab_sen}{marc}{tab_col}Un siècle plus tard, l'empereur Marc Aurèle, en campagne sur les bords du Danube, "
        "écrit le soir, pour lui seul.",
        ("C", "Nulle part l'homme ne trouve une retraite plus calme et plus de repos que dans son âme.", "c_marc"),
        "{-c_marc}{citd}C'est la citadelle intérieure : un lieu en soi où rien n'entre sans notre accord. "
        "{citd.1}Mais pour aller plus loin, écoute l'objection d'Aristote, qui vise cette sagesse-là.",
        "{-citd}{-marc}",
        ("C", "Quant à ceux qui prétendent qu'un homme étendu sur la roue, et plongé dans la plus cruelle infortune, "
              "est encore heureux, s'il est vertueux, … ce qu'ils disent n'a aucun sens.", "c_roue"),
        "{-c_roue}{deb}Voilà le grand débat antique. {deb.g}Pour les stoïciens, la vertu suffit. "
        "{deb.d}Pour Aristote, il faut aussi un peu de chance. Le stoïcien est plus {#la liberté}libre ; "
        "l'aristotélicien, plus humain.",
        "{-deb}{-tab_col}",
    ], vis={
        "tab_sto": dict(type="tableau", img="bh3-stoa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .5],
                        legende="Athènes, la stoa d'Attale, portique reconstruit au XXᵉ siècle (photo Julian Lupyan, CC0)"),
        "zen": dict(type="mot", t="ἡ στοά", g="la Stoa, le portique · d'où le nom des stoïciens", y=250, taille=100),
        "sto_def": dict(type="def", terme="Le bonheur stoïcien", cles=["nature", "suffit", "indifférentes"],
                        t="Vivre en accord avec la nature, c'est-à-dire avec la raison qui ordonne le monde.",
                        etape="La vertu suffit au bonheur ; santé, richesse, réputation sont indifférentes.", x=170, y=190, w=940),
        "epic": dict(type="portrait", annee=50, img="epictete", nom="Épictète", dates="v. 50 – v. 130",
                     legende="Manuel · Entretiens", x=110, y=120, w=330, h=420),
        "tab_hie": dict(type="tableau", img="t-hierapolis", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.15, .7, .5],
                        legende="Hiérapolis, en Phrygie, ville natale d'Épictète (photo Bernard Gagnon, CC BY-SA 3.0)"),
        "c_epi": dict(type="cit", a="Épictète", o="Manuel, VIII (trad. J.-M. Guyau, 1875)", x=640, y=170, w=570),
        "vou": dict(type="note", titre="La recette stoïcienne", cles=["écart", "veut"],
                    t="Le malheur, c'est l'écart entre ce que je veux et ce qui arrive.",
                    etape="Le stoïcien le supprime… en changeant ce qu'il veut.", x=170, y=200, w=940),
        "sen": dict(type="portrait", annee=-4, img="seneque", nom="Sénèque", dates="v. 4 av. – 65 apr. J.-C.",
                    legende="De la vie heureuse (v. 58)", x=110, y=120, w=330, h=420),
        "tab_sen": dict(type="tableau", img="t4-seneque", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Pierre Paul Rubens, La Mort de Sénèque, v. 1615 (Alte Pinakothek, Munich)"),
        "c_sen": dict(type="cit", a="Sénèque", o="De la vie heureuse, I (trad. J. Baillard)", x=640, y=150, w=570),
        "sen_n": dict(type="note", titre="Sénèque, le riche", cles=["richesses"],
                      t="On lui reproche sa fortune.",
                      etape="Le sage peut avoir des richesses, à condition qu'elles ne l'aient pas.", x=640, y=180, w=570),
        "marc": dict(type="portrait", annee=121, img="marc-aurele", nom="Marc Aurèle", dates="121 – 180",
                     legende="Pensées pour moi-même", x=110, y=120, w=330, h=420),
        "tab_col": dict(type="tableau", img="bh3-colonne", fond=True, sombre=True, de=[1.7, .27, .5], a=[1.9, .25, .45],
                        legende="Colonne de Marc Aurèle, Rome, les campagnes du Danube (planche d'E. Petersen, 1896, domaine public)"),
        "c_marc": dict(type="cit", a="Marc Aurèle", o="Pensées, IV, 3 (trad. A. Couat, 1904)", x=640, y=170, w=570),
        "citd": dict(type="note", titre="La citadelle intérieure", cles=["citadelle", "accord"],
                     t="Un lieu en soi où rien n'entre sans notre accord.",
                     etape="Mais Aristote objecte…", x=640, y=190, w=570),
        "c_roue": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, VII, 13, trad. Thurot (1823)", x=170, y=170, w=940),
        "deb": dict(type="cols", g="Les stoïciens", gq="la vertu suffit au bonheur : plus libre",
                    d="Aristote", dq="il faut aussi un peu de chance : plus humain", vs="≠"),
    }),

    # ------------------------------------------------------------------ V. Spinoza
    dict(id="spinoza", chap="Pour aller plus loin : Spinoza et la joie", fond="aube", humeur="lumiere",
         notions=["la raison", "la conscience"],
         retenir="Spinoza : la joie est le passage à une plus grande perfection. La béatitude n'est pas la récompense de la vertu, c'est la vertu elle-même.",
         beats=[
        "{spino}{tab_rij}Dernier sage, et non le moindre. Au dix-septième siècle, Baruch Spinoza retrouve les Anciens… "
        "mais il met au centre un mot qu'ils avaient laissé de côté : la joie.",
        ("C", "La joie est le passage d'une moindre perfection à une perfection plus grande.", "c_joie"),
        "{-c_joie}{-spino}{-tab_rij}{tab_rir}{jt}Pour Spinoza, chaque être s'efforce d'exister le plus pleinement possible. "
        "{jt.g}La joie, c'est quand ma puissance d'agir augmente : je comprends un problème, je réussis un geste, "
        "je retrouve un ami. {jt.d}La tristesse, quand elle diminue : la honte, la peur, l'envie, qui me rapetissent.",
        "{-jt}{cons_sp}D'où une morale étonnante. {cons_sp.1}Il ne faut pas se méfier de la joie, mais de la tristesse. "
        "{cons_sp.2}Ceux qui nous font peur ou nous culpabilisent pour mieux nous gouverner nous affaiblissent. "
        "{cons_sp.3}Et la joie la plus solide vient de la connaissance : plus je comprends le monde et moi-même, "
        "moins je subis.",
        "{-cons_sp}{-tab_rir}{tab_rij2}{spino2}D'où la dernière proposition de l'Éthique, qui résume tout l'épisode.",
        ("C", "La béatitude n'est pas le prix de la vertu, c'est la vertu elle-même.", "c_beat"),
        "{-c_beat}{-spino2}{fin_sp}Retiens-la bien. {fin_sp.1}Le bonheur n'est pas une récompense qui viendrait après l'effort. "
        "{fin_sp.2}Il est dans l'activité même : bien agir, comprendre, aimer. "
        "Aristote, les stoïciens et Spinoza sont au moins d'accord sur ce point.",
        "{-fin_sp}",
    ], vis={
        "spino": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      legende="Éthique (1677, posthume)", x=110, y=120, w=330, h=420),
        "tab_rij": dict(type="tableau", img="t4-rijnsburg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="Rijnsburg, la maison où vécut Spinoza, photographie ancienne (Elias Canneman, RCE, CC BY-SA 4.0)"),
        "c_joie": dict(type="cit", a="Spinoza", o="Éthique, III, définitions des affects, II (trad. É. Saisset, 1861)",
                       x=640, y=170, w=570),
        "tab_rir": dict(type="tableau", img="bh3-rire", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Frans Hals, Garçon riant, v. 1625 (Mauritshuis, La Haye)"),
        "jt": dict(type="cols", g="La joie", gq="ma puissance d'agir augmente : comprendre, réussir, retrouver un ami",
                   d="La tristesse", dq="elle diminue : la honte, la peur, l'envie", vs="≠"),
        "cons_sp": dict(type="liste", titre="Une morale de la joie", items=[
            "Se méfier de la tristesse, non de la joie", "Ceux qui nous font peur nous affaiblissent",
            "La joie la plus solide : comprendre"], marques=["1", "2", "3"], x=170, y=160, w=940),
        "tab_rij2": dict(type="tableau", img="t4-rijnsburg", fond=True, sombre=True, de=[1.25, .55, .45], a=[1.0, .5, .5],
                         legende="Rijnsburg, la maison où vécut Spinoza, photographie ancienne (Elias Canneman, RCE, CC BY-SA 4.0)"),
        "spino2": dict(type="portrait", img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                       legende="Éthique, V, proposition 42", x=110, y=120, w=330, h=420),
        "c_beat": dict(type="cit", a="Spinoza", o="Éthique, V, proposition 42 (trad. É. Saisset, 1861)", x=640, y=180, w=570),
        "fin_sp": dict(type="liste", titre="Ce que les sages ont en commun", items=[
            "Le bonheur n'est pas une récompense", "Il est dans l'activité même : agir, comprendre, aimer"],
                       marques=["✗", "✓"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_lyc2}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Aristote. Le bonheur est l'activité de l'âme "
        "conforme à la vertu, dans une vie complète. Une hirondelle ne fait pas le printemps.",
        "{rec.2}Deux : la vertu est une habitude et un juste milieu ; et le bonheur demande des amis, "
        "et culmine dans la vie de l'esprit.",
        "{rec.3}Trois : les stoïciens. La vertu suffit ; vouloir ce qui arrive ; la citadelle intérieure.",
        "{rec.4}Quatre : Spinoza. La joie augmente notre puissance d'agir, et la béatitude est la vertu elle-même.",
        "{-rec}{-tab_lyc2}{tab_fin}{q_suite}Mais si tout cela n'était qu'une belle histoire ? Et si nous courions après "
        "le bonheur comme un chasseur court après un lièvre… qu'il ne voudrait pas qu'on lui donne ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : le bonheur est-il une illusion ? Pascal, Schopenhauer, et Freud.",
         {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_lyc2": dict(type="tableau", img="bh3-stoa", fond=True, sombre=True, de=[1.2, .45, .5], a=[1.0, .5, .5],
                         legende="Athènes, la stoa d'Attale, portique reconstruit au XXᵉ siècle (photo Julian Lupyan, CC0)"),
        "rec": dict(type="carte", centre="LA SAGESSE DES ANCIENS", branches=[
            dict(t="Aristote", items=["activité conforme à la vertu", "une vie complète", "l'hirondelle"]),
            dict(t="Bien vivre", items=["la vertu, une habitude", "le juste milieu", "l'amitié, la contemplation"]),
            dict(t="Les stoïciens", items=["la vertu suffit", "vouloir ce qui arrive", "la citadelle intérieure"]),
            dict(t="Spinoza", items=["la joie", "la puissance d'agir", "béatitude = vertu"])]),
        "tab_fin": dict(type="tableau", img="bh3-chasse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Johann Georg Pforr, Chasse au lièvre avec un fauconnier, XVIIIᵉ siècle (domaine public)"),
        "q_suite": dict(type="question", t="Et si le bonheur n'était qu'une illusion ?"),
        "fin": dict(type="titre", sur="À suivre", t="Le bonheur est-il une illusion ?",
                    sous="Épisode 4 · Pascal, Schopenhauer, Freud"),
    }),
]

QUIZ = [
    dict(q="Que répond Solon à Crésus, qui se croit le plus heureux des hommes ?",
         r=["Qu'il a raison, puisqu'il est le plus riche", "Qu'on ne peut dire personne heureux avant sa mort",
            "Que le bonheur est un plaisir du corps", "Que seuls les dieux sont heureux"], ok=1,
         voir="sol", ex="Hérodote, I, 32 : tant que la vie n'est pas finie, la fortune peut tourner. Aristote discute cette idée au livre I de l'Éthique à Nicomaque."),
    dict(q="Selon Aristote, le bonheur est…",
         r=["un état que l'on possède", "l'activité de l'âme conforme à la vertu, dans une vie complète",
            "l'absence de trouble", "la somme des plaisirs"], ok=1,
         voir="c_act", ex="Éthique à Nicomaque, I, 7 : le bonheur est une activité (on le fait), selon l'excellence propre à l'homme, la raison."),
    dict(q="« Une hirondelle ne fait pas le printemps » signifie, chez Aristote, que…",
         r=["le bonheur est une affaire de saison", "un seul jour ou un temps très court ne suffit pas à rendre heureux",
            "les animaux ne sont pas heureux", "le bonheur est une illusion"], ok=1,
         voir="c_hir", ex="Le bonheur se juge sur une vie complète : c'est une manière durable de vivre, non un instant."),
    dict(q="Comment devient-on juste, selon Aristote ?",
         r=["En naissant juste", "En apprenant la définition de la justice", "En pratiquant des actions justes", "En obéissant aux dieux"], ok=2,
         voir="c_hab", ex="La vertu est une habitude : en bâtissant on devient maçon, en pratiquant la justice on devient juste."),
    dict(q="Le juste milieu d'Aristote, c'est…",
         r=["la moyenne, la tiédeur", "un sommet entre deux vices, l'un par excès, l'autre par défaut",
            "un compromis politique", "l'indifférence"], ok=1,
         voir="som", ex="Le courage, entre la lâcheté et la témérité, est un sommet, difficile à tenir, qui se trouve en situation."),
    dict(q="« Veux ce qui arrive comme il arrive, et tu couleras une vie heureuse. » Qui l'a écrit ?",
         r=["Aristote", "Épictète", "Épicure", "Spinoza"], ok=1,
         voir="c_epi", ex="Manuel, VIII : le malheur est l'écart entre ce que je veux et ce qui arrive ; le stoïcien change ce qu'il veut."),
    dict(q="Que reproche Aristote à ceux qui disent l'homme vertueux heureux même « sur la roue » ?",
         r=["De mépriser la vertu", "De dire une chose qui n'a aucun sens : le bonheur demande aussi des biens extérieurs",
            "D'être trop religieux", "De confondre plaisir et joie"], ok=1,
         voir="c_roue", ex="Éthique à Nicomaque, VII, 13 : contre la thèse stoïcienne que la vertu suffit, Aristote rappelle la part de la fortune."),
    dict(q="Pour Spinoza, la joie est…",
         r=["une passion à combattre", "le passage d'une moindre perfection à une perfection plus grande",
            "la récompense de la vertu", "l'absence de désir"], ok=1,
         voir="c_joie", ex="Éthique, III : la joie augmente notre puissance d'agir. Et la béatitude n'est pas le prix de la vertu, c'est la vertu même (V, 42)."),
]

CREDITS = [
    "Portraits : Aristote (buste, Rome, Palazzo Altemps, photographie Jastrow) ; Épictète (gravure ancienne) ; Sénèque ; "
    "Marc Aurèle (statue équestre, Capitole, photo Jebulon, CC0) ; Baruch Spinoza (portrait anonyme, vers 1665) : domaine public",
    "Tableaux et gravures : Gaspar van den Hoecke, Crésus montrant ses trésors à Solon (XVIIᵉ s.) ; Johannes Vermeer, Le Géographe (1669) ; "
    "Pierre Paul Rubens, La Mort de Sénèque (v. 1615) ; Frans Hals, Garçon riant (v. 1625) ; "
    "Johann Georg Pforr, Chasse au lièvre avec un fauconnier ; J. A. Naumann, planche d'hirondelles : domaine public",
    "Antiquités et photographies : Myson, Crésus sur son bûcher (Louvre G 197, domaine public) ; amphore panathénaïque, "
    "Metropolitan Museum (photo Ismoon, CC BY-SA 4.0) ; Peintre de Sosias, Achille et Patrocle, Altes Museum (photo Dosseman, CC BY-SA 4.0) ; "
    "vestiges du Lycée (George E. Koronaios, CC0) ; stoa d'Attale (Julian Lupyan, CC0) ; Hiérapolis (Bernard Gagnon, CC BY-SA 3.0) ; "
    "William England, Blondin au-dessus du Niagara (1859) ; colonne de Marc Aurèle, planche d'E. Petersen (1896) ; "
    "maison de Spinoza à Rijnsburg (Elias Canneman, RCE, CC BY-SA 4.0) : domaine public sauf mention",
    "Citations : Aristote, Éthique à Nicomaque, trad. J.-F. Thurot (1823) ; Épictète, Manuel, trad. J.-M. Guyau (1875) ; "
    "Sénèque, De la vie heureuse, trad. J. Baillard ; Marc Aurèle, Pensées, trad. A. Couat (1904) ; "
    "Spinoza, Éthique, trad. É. Saisset (1861) : Wikisource. Hérodote, Histoires, I, résumé.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
