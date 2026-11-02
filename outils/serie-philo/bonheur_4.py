"""Le bonheur, épisode 4 : « Le bonheur est-il une illusion ? »

Même format que les séries « La liberté » et « Le devoir » (voir liberte_1.py, devoir_3.py).
Citations vérifiées sur Wikisource : Pascal, Pensées, éd. Brunschvicg (fr. 139, 142, 172) ; Schopenhauer, Le Monde comme
volonté et comme représentation, IV, § 57, trad. Burdeau ; Rousseau, Julie ou la Nouvelle Héloïse, VI, lettre 8 (1761).
Freud, Malaise dans la civilisation, II (1930) : citation approchée. Alain, Propos sur le bonheur (1928), propos « Il faut jurer ».
Étude citée : Brickman, Coates et Janoff-Bulman, « Lottery winners and accident victims », 1978 ; nuancée par
Lindqvist, Östling et Cesarini (gagnants suédois, 2020).
"""

CODE = "bonheur-4"
NOTION = "Le bonheur"
NUM = 4
TITRE = "Le bonheur est-il une illusion ?"
SUIVANT = "Épisode 5 · Bonheur, morale et politique"
PRONONCIATION = {"Pyrrhus": "Pirusse", "Cinéas": "Sinéasse", "Schopenhauer": "Chopenaouère",
                 "Brickman": "Brikmane", "Illinois": "Ilinoï"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_pyr}{q1}Trois siècles avant notre ère, le roi Pyrrhus prépare une immense campagne. "
        "Son conseiller, Cinéas, lui pose une question toute simple.",
        "{-q1}{dia}{dia.1}Et quand tu auras vaincu les Romains ? {dia.2}Je prendrai la Sicile, répond le roi. "
        "Puis Carthage, puis la Grèce entière. {dia.3}Et après tout cela ? "
        "{dia.4}Alors, nous nous reposerons. Nous passerons nos journées à boire et à converser, heureux.",
        ("Cinéas sourit. Et qu'est-ce qui nous empêche… de le faire dès maintenant ?", {"rate": "-6%"}),
        ("P", 0.5),
        "{-dia}{q2}Pyrrhus n'a pas répondu. Il est parti en guerre. Plutarque raconte la scène ; "
        "Pascal, vingt siècles plus tard, la relève dans ses Pensées. Car elle pose une question troublante.",
        "{-q2}{q3}Et si le bonheur n'était qu'un mirage, qui recule à mesure qu'on avance ?",
        "{-q3}{quatre}Quatre penseurs vont répondre : oui, le bonheur est une illusion. "
        "Écoutons-les… avant de leur répondre.",
        ("P", 0.3),
        "{-quatre}{-tab_pyr}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_pyr": dict(type="tableau", img="bh4-pyrrhus", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .45, .32],
                        legende="Pyrrhus, roi d'Épire, buste romain, musée archéologique de Naples (photo Marie-Lan Nguyen, domaine public)"),
        "q1": dict(type="question", t="Et après la victoire ?"),
        "dia": dict(type="dialogue", lignes=["« Et quand tu auras vaincu les Romains ? »", "« La Sicile. Puis Carthage, puis la Grèce. »",
                                             "« Et après tout cela ? »", "« Nous nous reposerons, heureux. »"],
                    src="d'après Plutarque, Vie de Pyrrhus, 14", x=500, y=170, w=700),
        "q2": dict(type="question", t="Qu'est-ce qui nous empêche d'être heureux dès maintenant ?"),
        "q3": dict(type="question", t="Et si le bonheur n'était qu'un mirage ?"),
        "quatre": dict(type="nuage", items=["Pascal", "Schopenhauer", "Rousseau", "Freud"]),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 4", t="Le bonheur est-il une illusion ?",
                      sous="Pascal, Schopenhauer, Rousseau, Freud"),
    }),

    # ------------------------------------------------------------------ I. Pascal
    dict(id="pascal", chap="Le divertissement", fond="aube", humeur="tension", notions=["la conscience", "le temps", "la religion"],
         retenir="Pascal : nous fuyons la pensée de notre condition dans le divertissement. Nous aimons la chasse, non la prise.",
         beats=[
        "{pascal}{tab_cham}Blaise Pascal, au dix-septième siècle. Savant de génie et croyant ardent, il meurt à trente-neuf ans ; "
        "ses notes deviendront les Pensées. L'une d'elles part d'une observation : à force de regarder les hommes s'agiter…",
        ("C", "… j'ai découvert que tout le malheur des hommes vient d'une seule chose, qui est de ne savoir pas demeurer "
              "en repos, dans une chambre.", "c_ch"),
        "{-pascal}{-c_ch}{q_ch}Essaie. Une heure seul dans une chambre, sans téléphone, sans musique, sans rien. "
        "Pourquoi est-ce si difficile ?",
        "{-q_ch}{seul}Parce que, seul et immobile, je me mets à penser à moi. {seul.1}À ce que je suis : fragile, mortel, "
        "ignorant de presque tout. {seul.2}Alors je fuis.",
        "{-seul}{-tab_cham}{tab_chasse}{div}Pascal appelle cela le {!divertissement}divertissement : au sens premier, ce qui nous détourne. "
        "{div.1}Le jeu, la conversation, la guerre même. Prends le chasseur. Si on lui offrait le lièvre au départ, "
        "il n'en voudrait pas.{-div}",
        ("C", "Ce lièvre ne nous garantirait pas de la vue de la mort et des misères, mais la chasse — qui nous en détourne — "
              "nous en garantit.", "c_lie"),
        "{-c_lie}{prise}Voilà le secret. {prise.g}Nous croyons chercher la prise : le résultat, le repos. "
        "{prise.d}En réalité, ce que nous aimons, c'est la chasse : le mouvement qui nous empêche de penser.",
        "{-prise}{-tab_chasse}{tab_roi}{q_roi}Même le roi n'y échappe pas. Il a tout. Mais laissez-le seul, sans compagnie, "
        "penser à lui tout à loisir : il sera plus malheureux que le dernier de ses sujets qui joue et qui danse.{-q_roi}",
        ("C", "… un roi sans divertissement est un homme plein de misères.", "c_roi"),
        "{-c_roi}{-tab_roi}{tel}Et nous ? {tel.1}Le fil qu'on fait défiler sans fin, {tel.2}la notification qui tombe à point nommé. "
        "Pascal n'avait pas de téléphone ; il en avait déjà compris l'usage.",
        "{-tel}{tab_van}{temps}Il va plus loin. Le divertissement a une forme intérieure : vivre ailleurs que dans le présent. "
        "Nous regrettons le passé, nous attendons l'avenir. {temps.1}Le {#le temps}présent ne nous suffit jamais.{-temps}",
        ("C", "Ainsi nous ne vivons jamais, mais nous espérons de vivre ; et, nous disposant toujours à être heureux, "
              "il est inévitable que nous ne le soyons jamais.", "c_viv"),
        "{-c_viv}{note_p}Attention au contresens : Pascal ne méprise pas ceux qui se divertissent. Ils ont raison de fuir. "
        "Mais le divertissement, dit-il, est aussi la plus grande de nos misères : il nous empêche de chercher le vrai remède. "
        "{note_p.1}Et ce remède, pour l'apologiste chrétien, c'est Dieu seul.",
        "{-note_p}{-tab_van}",
    ], vis={
        "pascal": dict(type="portrait", annee=1623, img="pascal", nom="Blaise Pascal", dates="1623 – 1662",
                       legende="Pensées (1670)", x=110, y=120, w=330, h=420),
        "tab_cham": dict(type="tableau", img="bh4-chambre", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .5],
                         legende="Vilhelm Hammershøi, Intérieur, Strandgade 30, 1900"),
        "c_ch": dict(type="cit", a="Pascal", o="Pensées, fr. 139 (éd. Brunschvicg ; 1670)", x=640, y=170, w=570),
        "q_ch": dict(type="question", t="Une heure seul dans une chambre, sans rien. Pourquoi est-ce si difficile ?"),
        "seul": dict(type="liste", titre="Seul dans la chambre", items=[
            "Je pense à moi : fragile, mortel, ignorant", "Alors je fuis"], marques=["1", "→"], x=170, y=190, w=940),
        "tab_chasse": dict(type="tableau", img="bh4-chasse", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.15, .7, .5],
                           legende="Paolo Uccello, La Chasse nocturne, vers 1470 (Ashmolean Museum, Oxford)"),
        "div": dict(type="def", cles=["détourne"], terme="Le divertissement",
                    t="Ce qui nous détourne de penser à notre condition.",
                    etape="Le jeu, la conversation, la chasse, la guerre même.", x=170, y=190, w=940),
        "c_lie": dict(type="cit", a="Pascal", o="Pensées, fr. 139 (éd. Brunschvicg)", x=170, y=180, w=940),
        "prise": dict(type="cols", g="La prise", gq="ce que nous croyons chercher : le résultat, le repos",
                      d="La chasse", dq="ce que nous aimons : le mouvement qui empêche de penser", vs="≠"),
        "tab_roi": dict(type="tableau", img="bh4-roi", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.3, .5, .2],
                        legende="Hyacinthe Rigaud, Louis XIV en costume de sacre, 1701 (musée du Louvre)"),
        "q_roi": dict(type="question", t="Un roi qui a tout, seul, sans divertissement ?"),
        "c_roi": dict(type="cit", a="Pascal", o="Pensées, fr. 142 (éd. Brunschvicg)", x=170, y=230, w=940),
        "tel": dict(type="illu", nom="tel", x=240, y=90, w=800, h=540),
        "tab_van": dict(type="tableau", img="bh4-vanite", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .5],
                        legende="Philippe de Champaigne, Vanité (la tulipe, le crâne, le sablier), vers 1671 (musée de Tessé, Le Mans)"),
        "temps": dict(type="liste", titre="Vivre ailleurs que dans le présent", items=[
            "Le présent ne nous suffit jamais"], marques=["⧗"], x=170, y=200, w=940),
        "c_viv": dict(type="cit", a="Pascal", o="Pensées, fr. 172 (éd. Brunschvicg)", x=170, y=170, w=940),
        "note_p": dict(type="note", titre="Contresens à éviter", cles=["misères", "remède"],
                       t="Pascal ne méprise pas le divertissement : il console de nos misères… et il est la plus grande de nos misères.",
                       etape="Le vrai remède, pour l'apologiste chrétien : Dieu seul.", x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ II. Schopenhauer
    dict(id="schopenhauer", chap="Le pendule", fond="nuit", humeur="mystere", notions=["la nature", "l'art"],
         retenir="Schopenhauer : désirer, c'est manquer, donc souffrir ; être satisfait, c'est s'ennuyer. La vie oscille entre les deux.",
         beats=[
        "{schop}{tab_voy0}Deux siècles plus tard, en Allemagne, un philosophe pousse le pessimisme jusqu'au bout : Arthur Schopenhauer.",
        "{vv}Son idée : au fond de toute chose, il y a une force aveugle, qui veut sans savoir pourquoi. "
        "Il l'appelle la volonté, ou le vouloir-vivre. Elle fait pousser la plante, chasser le loup… et désirer l'homme.",
        "{-schop}{-vv}{-tab_voy0}{tab_cri}{meca}Regarde ce qu'elle fait de nous. {meca.1}Je désire. Mais désirer, c'est manquer de quelque chose : "
        "tout vouloir naît d'un besoin, d'un manque, donc d'une {!souffrance}souffrance.",
        "{meca.2}Je finis par obtenir ce que je voulais. Le plaisir est vif… et bref. "
        "Car la satisfaction n'a rien de positif : elle n'est que la fin d'une douleur. "
        "{meca.3}Et quand il n'y a plus rien à désirer ?",
        "{-meca}{-tab_cri}{tab_ennui}Alors vient l'ennui. Schopenhauer le décrit avec une précision cruelle.",
        ("C", "… et les voilà tombés dans un vide épouvantable, dans l'ennui : leur nature, leur existence leur pèse "
              "d'un poids intolérable.", "c_vide"),
        "{-c_vide}{-tab_ennui}{tab_pend}D'où son image la plus célèbre.",
        ("C", "La vie donc oscille, comme un pendule, de droite à gauche, de la souffrance à l'ennui : ce sont là les deux "
              "éléments dont elle est faite, en somme.", "c_pend"),
        "{-c_pend}{pend}{pend.g}D'un côté, la souffrance du manque. {pend.d}De l'autre, l'ennui de la satisfaction. "
        "Et le bonheur ? Il n'est que le point le plus bas du pendule : on le traverse, on ne s'y arrête jamais.",
        "Tu reconnais le tonneau percé de Calliclès, vu dans la série sur la liberté. Mais pour Schopenhauer, "
        "ce n'est pas seulement le débauché qui a des tonneaux percés : c'est la nature même du désir.",
        "{-pend}{-tab_pend}{tab_voy}{issue}Y a-t-il une issue ? Pour aller plus loin : Schopenhauer en voit deux. "
        "{issue.1}L'{#l'art}art, d'abord : devant un tableau, dans une musique, j'oublie un instant de vouloir ; je contemple. "
        "C'est une trêve.",
        "{issue.2}Et, plus radicalement, l'ascèse : éteindre en soi le vouloir-vivre, comme les sages de l'Inde qu'il admirait. "
        "Un remède… qui ressemble beaucoup à un renoncement au bonheur.",
        "{-issue}{-tab_voy}",
    ], vis={
        "schop": dict(type="portrait", annee=1788, img="schopenhauer", nom="Arthur Schopenhauer", dates="1788 – 1860",
                      legende="Le Monde comme volonté et comme représentation (1818)", x=110, y=120, w=330, h=420),
        "tab_voy0": dict(type="tableau", img="bh4-tigre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                         legende="Henri Rousseau, Surpris ! (Tigre dans une tempête tropicale), 1891 (National Gallery, Londres)"),
        "vv": dict(type="def", cles=["aveugle"], terme="Le vouloir-vivre",
                   t="Une force aveugle, au fond de toute chose, qui veut sans savoir pourquoi.",
                   etape="Elle fait pousser la plante, chasser le loup… et désirer l'homme.", x=640, y=200, w=570),
        "tab_cri": dict(type="tableau", img="t2-cri", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .35],
                        legende="Edvard Munch, Le Cri, 1893 (Galerie nationale, Oslo)"),
        "meca": dict(type="liste", titre="La mécanique du désir", items=[
            "Désirer, c'est manquer : une souffrance", "Obtenir : un plaisir bref, la fin d'une douleur",
            "Plus rien à désirer : l'ennui"], marques=["1", "2", "3"], cles=["manquer", "ennui"], x=170, y=150, w=940),
        "tab_ennui": dict(type="tableau", img="bh4-ennui", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .5],
                          legende="Walter Sickert, Ennui, vers 1914 (Tate, Londres)"),
        "c_vide": dict(type="cit", a="Schopenhauer", o="Le Monde comme volonté et comme représentation, IV, § 57 (1818), trad. Burdeau",
                       x=170, y=180, w=940),
        "tab_pend": dict(type="tableau", img="bh4-pendule", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                         legende="Le pendule de Foucault au Panthéon, Paris (photo Rsk6400, CC BY-SA 3.0)"),
        "c_pend": dict(type="cit", a="Schopenhauer", o="Le Monde comme volonté et comme représentation, IV, § 57, trad. Burdeau",
                       x=170, y=170, w=940),
        "pend": dict(type="cols", g="La souffrance", gq="le désir : un manque", d="L'ennui", dq="la satisfaction : un vide",
                     vs="⟷", repere="Le bonheur : un point de passage"),
        "tab_voy": dict(type="tableau", img="bh4-voyageur", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.2, .5, .3],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, vers 1818 (Kunsthalle, Hambourg)"),
        "issue": dict(type="liste", titre="Pour aller plus loin · deux issues", items=[
            "L'art : contempler, oublier un instant de vouloir", "L'ascèse : éteindre le vouloir-vivre"],
                      marques=["1", "2"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ III. Rousseau
    dict(id="rousseau", chap="Heureux avant d'être heureux", fond="aube", humeur="lumiere", notions=["le temps", "la religion"],
         retenir="Rousseau : on jouit moins de ce qu'on obtient que de ce qu'on espère. « On n'est heureux qu'avant d'être heureux. »",
         beats=[
        "{rousseau}{tab_hel}Rousseau, lui, renverse le tableau. Dans son roman Julie ou la Nouvelle Héloïse, en 1761, "
        "son héroïne écrit une lettre étrange. Elle a tout : un mari estimable, des enfants, une maison paisible au bord du lac Léman. "
        "Et pourtant, elle avoue un mal secret : elle s'ennuie d'être heureuse.",
        ("C", "Malheur à qui n'a plus rien à désirer ! il perd pour ainsi dire tout ce qu'il possède.", "c_mal"),
        "{-c_mal}{-rousseau}{-tab_hel}{tab_cyt}{imag}Pourquoi ? Parce que le désir n'est pas seulement un manque. {imag.1}Tant que je désire, j'imagine. "
        "{imag.2}Mon imagination embellit ce que j'attends, le pare de toutes les couleurs. "
        "{imag.3}Puis l'objet arrive… et il n'est que ce qu'il est.{-imag}",
        ("C", "On jouit moins de ce qu'on obtient que de ce qu'on espère et l'on n'est heureux qu'avant d'être heureux.", "c_av"),
        "{-c_av}{av_ap}{av_ap.g}Avant : le désir, l'attente, l'imagination qui travaille. "
        "{av_ap.d}Après : la possession… et la déception. Pense au voyage qu'on prépare pendant des mois : "
        "souvent, les préparatifs étaient le meilleur moment.",
        "{-av_ap}{-tab_cyt}{tab_hel2}Julie en tire une formule superbe.",
        ("C", "Le pays des chimères est en ce monde le seul digne d'être habité, et tel est le néant des choses humaines, "
              "qu'hors l'Être existant par lui-même il n'y a rien de beau que ce qui n'est pas.", "c_chim"),
        "{-c_chim}{etre}L'Être existant par lui-même, c'est Dieu : comme chez Pascal, seule la {#la religion}religion promet "
        "un bonheur qui ne déçoive pas.",
        "{-etre}{cmp}Mais remarque la différence avec Schopenhauer. {cmp.g}Pour lui, désirer, c'est souffrir. "
        "{cmp.d}Pour Rousseau, désirer, c'est déjà être heureux : peut-être même la seule façon de l'être.",
        ("Le bonheur serait une illusion… mais une illusion qui fait vivre. À condition de ne jamais l'atteindre.", {"rate": "-5%"}),
        "{-cmp}{-tab_hel2}",
    ], vis={
        "rousseau": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                         legende="Julie ou la Nouvelle Héloïse (1761)", x=110, y=120, w=330, h=420),
        "tab_hel": dict(type="tableau", img="bh4-heloise", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .55],
                        legende="Jean-Michel Moreau le Jeune, illustration pour Julie ou la Nouvelle Héloïse, gravure, XVIIIᵉ s. (BnF)"),
        "c_mal": dict(type="cit", a="Rousseau", o="Julie ou la Nouvelle Héloïse, VI, lettre 8 (1761)", x=640, y=190, w=570),
        "tab_cyt": dict(type="tableau", img="bh4-cythere", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.25, .45, .45],
                        legende="Antoine Watteau, Pèlerinage à l'île de Cythère, 1717 (musée du Louvre)"),
        "imag": dict(type="liste", titre="Le désir et l'imagination", items=[
            "Tant que je désire, j'imagine", "L'imagination embellit ce que j'attends", "L'objet arrive… et n'est que ce qu'il est"],
                     marques=["1", "2", "3"], x=170, y=160, w=940),
        "c_av": dict(type="cit", a="Rousseau", o="Julie ou la Nouvelle Héloïse, VI, lettre 8 (1761)", x=170, y=200, w=940),
        "av_ap": dict(type="cols", g="Avant", gq="le désir, l'attente, l'imagination", d="Après",
                      dq="la possession… et la déception", vs="→"),
        "tab_hel2": dict(type="tableau", img="bh4-heloise", fond=True, sombre=True, de=[1.25, .5, .3], a=[1.0, .5, .5],
                         legende="Jean-Michel Moreau le Jeune, illustration pour Julie ou la Nouvelle Héloïse, gravure, XVIIIᵉ s. (BnF)"),
        "c_chim": dict(type="cit", a="Rousseau", o="Julie ou la Nouvelle Héloïse, VI, lettre 8 (1761)", x=170, y=170, w=940),
        "etre": dict(type="def", cles=["Dieu", "encore"], terme="« L'Être existant par lui-même »",
                     t="Dieu : le seul bonheur qui ne déçoive pas.",
                     etape="Sur cette terre, rien n'est beau que ce qui n'existe pas encore.", x=170, y=200, w=940),
        "cmp": dict(type="cols", g="Schopenhauer", gq="désirer, c'est souffrir", d="Rousseau",
                    dq="désirer, c'est déjà être heureux", vs="≠"),
    }),

    # ------------------------------------------------------------------ IV. Freud
    dict(id="freud", chap="Pas prévu par la Création", fond="nuit", humeur="tension",
         notions=["l'inconscient", "la nature", "la technique"],
         retenir="Freud : le bonheur n'est qu'épisodique ; la souffrance vient du corps, du monde et des autres. Chacun doit chercher sa voie.",
         beats=[
        "{freud}{tab_berg}Vienne, 1930. Sigmund Freud, le fondateur de la psychanalyse, "
        "publie Malaise dans la civilisation. "
        "Il y pose la question franchement : que veulent les hommes ? Être heureux. Et ils y parviennent mal.",
        "{pp}Car nous sommes gouvernés, dit-il, par le principe de plaisir : rechercher le plaisir, éviter le déplaisir. "
        "{pp.1}Ce programme est inscrit au plus profond de nous, dans notre {#l'inconscient}inconscient. "
        "Mais il est en conflit avec le monde entier. D'où ce constat, que l'on cite souvent ainsi.{-pp}",
        ("C", "On serait tenté de dire que le dessein que l'homme soit « heureux » n'est pas inclus dans le plan de la « Création ».",
         "c_freud"),
        "{-c_freud}{-freud}{-tab_berg}{tab_bain}{epi}Pourquoi ? D'abord parce que le bonheur, au sens fort, est par nature épisodique. "
        "Il naît de la satisfaction soudaine d'un besoin longtemps retenu. Prolongé, il s'émousse. "
        "{epi.1}Nous sommes ainsi faits que seul le contraste nous procure une jouissance intense. "
        "Un bain chaud est délicieux… les cinq premières minutes.",
        "{-epi}{-tab_bain}{tab_mal}{trois}Ensuite, parce que la souffrance, elle, nous menace de trois côtés. "
        "{trois.1}Notre propre corps, voué à la maladie et à la mort. "
        "{-tab_mal}{tab_vag}{trois.2}Le monde extérieur, la nature, qui peut se déchaîner contre nous. "
        "{trois.3}Et nos relations avec les autres hommes : la souffrance, dit Freud, que nous ressentons peut-être "
        "le plus douloureusement.",
        "{-trois}{-tab_vag}{tab_cyt2}{tech}Contre cela, les hommes inventent des stratégies. {tech.1}S'étourdir, par l'ivresse. "
        "{tech.2}S'isoler des autres. {tech.3}Maîtriser la nature, par la science et la {#la technique}technique. "
        "{tech.4}Sublimer ses désirs, dans le travail ou dans l'art. {tech.5}Aimer, et être aimé.",
        "Aucune n'est sûre. Il n'y a pas de recette valable pour tous : chacun, dit Freud, doit chercher par lui-même "
        "de quelle façon il peut trouver le bonheur.",
        "{-tech}{-tab_cyt2}",
    ], vis={
        "freud": dict(type="portrait", annee=1856, img="freud", nom="Sigmund Freud", dates="1856 – 1939",
                      legende="Malaise dans la civilisation (1930)", x=110, y=120, w=330, h=420),
        "tab_berg": dict(type="tableau", img="bh4-berggasse", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.2, .5, .35],
                         legende="Plaque au 19, Berggasse, Vienne, où Freud vécut de 1891 à 1938 (photo GuentherZ, CC BY 3.0)"),
        "pp": dict(type="def", cles=["plaisir", "conflit"], terme="Le principe de plaisir",
                   t="Rechercher le plaisir, éviter le déplaisir : le programme de notre vie psychique.",
                   etape="Un programme inconscient… en conflit avec le monde entier.", x=640, y=170, w=570),
        "c_freud": dict(type="cit", a="Freud", o="Malaise dans la civilisation, chap. II (1930)", para=True, x=640, y=180, w=570),
        "tab_bain": dict(type="tableau", img="bh4-tub", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                         legende="Edgar Degas, Le Tub, 1886, pastel (musée d'Orsay)"),
        "epi": dict(type="def", cles=["épisodique", "contraste"], terme="Le bonheur selon Freud",
                    t="La satisfaction soudaine d'un besoin retenu : un épisode, non un état.",
                    etape="Seul le contraste nous procure une jouissance intense.", x=170, y=190, w=940),
        "tab_mal": dict(type="tableau", img="bh4-malade", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .45, .4],
                        legende="Edvard Munch, L'Enfant malade, 1885-1886 (Galerie nationale, Oslo)"),
        "trois": dict(type="liste", titre="Trois sources de souffrance", items=[
            "Le corps : la maladie, la mort", "Le monde extérieur : la nature qui se déchaîne",
            "Les autres hommes : la plus douloureuse"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_vag": dict(type="tableau", img="bh4-vague", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .5],
                        legende="Katsushika Hokusai, La Grande Vague de Kanagawa, vers 1831 (estampe)"),
        "tab_cyt2": dict(type="tableau", img="bh4-cythere", fond=True, sombre=True, de=[1.3, .75, .5], a=[1.0, .5, .5],
                         legende="Antoine Watteau, Pèlerinage à l'île de Cythère, 1717 (musée du Louvre)"),
        "tech": dict(type="liste", titre="Les stratégies du bonheur, selon Freud", items=[
            "S'étourdir : l'ivresse", "S'isoler des autres", "Maîtriser la nature : la science, la technique",
            "Sublimer : le travail, l'art", "Aimer, et être aimé"], marques=["1", "2", "3", "4", "5"], x=170, y=110, w=940),
    }),

    # ------------------------------------------------------------------ V. alors, une illusion ?
    dict(id="reponse", chap="Alors, une illusion ?", fond="aube", humeur="mystere",
         notions=["la science", "la raison", "la liberté"],
         retenir="On s'habitue au meilleur comme au pire, mais pas totalement. Illusoire : le bonheur-état. Reste le bonheur-activité, qui se construit.",
         beats=[
        "{tab_loto}{q_loto}Pour aller plus loin, quittons un instant les philosophes. En 1978, trois psychologues américains, "
        "Philip Brickman et ses collègues, publient une enquête devenue célèbre.",
        "{-q_loto}{etu}Ils interrogent des gagnants de la loterie de l'Illinois, des personnes restées paralysées après un accident, "
        "et des gens ordinaires.",
        "{etu.1}Résultat surprenant : les gagnants ne se disent pas beaucoup plus heureux que les gens ordinaires. "
        "{etu.2}Pire : ils trouvent moins de plaisir aux petites joies de tous les jours, une conversation, un compliment, "
        "un bon petit déjeuner. {etu.3}Et les accidentés se disent moins heureux, certes, mais bien moins malheureux "
        "qu'on ne l'aurait cru.",
        "{-etu}{-tab_loto}{tab_roue}{adapt}Les psychologues parlent d'adaptation hédonique, ou de tapis roulant hédonique. "
        "Comme un hamster dans sa roue, nous courons vers le bonheur… et le décor revient sans cesse au même point. "
        "{adapt.1}On s'habitue au meilleur comme au pire.",
        "C'est Schopenhauer, vérifié en laboratoire ?",
        ("Pas si vite.", {"rate": "-8%"}),
        "{-adapt}{prud}{prud.1}L'étude portait sur vingt-deux gagnants seulement : c'est très peu. "
        "{prud.2}Le bonheur y était une simple note, de zéro à cinq. "
        "{prud.3}Et des études plus récentes, sur des milliers de joueurs suédois, trouvent qu'après un gros gain, "
        "la satisfaction à l'égard de la vie reste durablement plus élevée. "
        "{prud.4}L'adaptation existe, mais elle n'est pas totale. Et la {#la science}science mesure ce que les gens disent "
        "de leur bonheur, non ce qu'il est : dans une copie, un exemple, jamais une preuve.",
        "{-prud}{-tab_roue}{tab_mat}{dist}Alors, le bonheur est-il une illusion ? Regarde ce que nos quatre penseurs critiquent. "
        "{dist.g}Un bonheur conçu comme un état : complet, définitif, la satisfaction de tous nos désirs, pour toujours. "
        "Celui-là, oui, est sans doute une illusion. "
        "Kant dira même que c'est un idéal, non de la raison, mais de l'imagination : ce sera l'épisode suivant.",
        "{dist.d}Mais le bonheur peut se penser autrement : comme une activité, une manière de vivre. "
        "C'est la leçon d'Aristote et des stoïciens, vue dans l'épisode trois.",
        "{-dist}{-tab_mat}{tab_mat2}{alain}Au vingtième siècle, le philosophe Alain en fait toute une sagesse, "
        "dans ses Propos sur le bonheur. Pour lui, le bonheur ne tombe pas du ciel comme la pluie : "
        "il se fait, il se veut, comme on apprend un métier.{-alain}",
        ("C", "Le pessimisme est d'humeur ; l'optimisme est de volonté.", "c_al"),
        "{-c_al}{rep}Voilà peut-être la vraie réponse à nos pessimistes. "
        "{rep.1}Ils décrivent très bien ce qui nous arrive quand nous attendons le bonheur passivement, comme un cadeau. "
        "{rep.2}Ils ne prouvent pas qu'on ne puisse pas le construire, librement, par l'action.",
        ("Le bonheur n'est peut-être pas un état qu'on atteint. Plutôt une manière de marcher.", {"rate": "-5%"}),
        "{-rep}{-tab_mat2}",
    ], vis={
        "tab_loto": dict(type="tableau", img="bh4-loto", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .4],
                         legende="Grille de loterie (photo Santeri Viinamäki, CC BY-SA 4.0)"),
        "q_loto": dict(type="question", t="Gagner à la loterie rend-il heureux ?"),
        "etu": dict(type="liste", titre="Brickman, Coates et Janoff-Bulman (1978)", items=[
            "Les gagnants : pas beaucoup plus heureux que les autres",
            "Moins de plaisir aux petites joies du quotidien",
            "Les accidentés : moins heureux, mais moins qu'on ne l'aurait cru"],
                    marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_roue": dict(type="tableau", img="bh4-roue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                         legende="Hamster dans sa roue (photo Rlicul, CC BY-SA 3.0)"),
        "adapt": dict(type="def", cles=["habitue"], terme="L'adaptation hédonique",
                      t="Après un grand bonheur ou un grand malheur, on revient peu à peu à son niveau habituel.",
                      etape="On s'habitue au meilleur comme au pire.", x=170, y=200, w=940, plus=True),
        "prud": dict(type="liste", titre="Avec prudence", items=[
            "Vingt-deux gagnants seulement", "Une note de 0 à 5 : ce que les gens disent",
            "Gagnants suédois : satisfaction durablement plus haute", "L'adaptation existe, mais n'est pas totale"],
                     marques=["✗", "✗", "→", "="], x=170, y=130, w=940),
        "tab_mat": dict(type="tableau", img="bh4-matisse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Henri Matisse, Le Bonheur de vivre, 1905-1906 (Barnes Foundation, Philadelphie)"),
        "dist": dict(type="cols", g="Le bonheur-état", gq="complet, définitif : sans doute une illusion",
                     d="Le bonheur-activité", dq="une manière de vivre, qui se construit", vs="≠",
                     repere="La distinction qui dépasse"),
        "tab_mat2": dict(type="tableau", img="bh4-matisse", fond=True, sombre=True, de=[1.4, .75, .4], a=[1.2, .6, .5],
                         legende="Henri Matisse, Le Bonheur de vivre, 1905-1906 (Barnes Foundation, Philadelphie)"),
        "alain": dict(type="mot", t="Alain", g="Propos sur le bonheur (1928) : le bonheur se fait, il se veut", y=240, taille=104),
        "c_al": dict(type="cit", a="Alain", o="Propos sur le bonheur, « Il faut jurer » (1923)", x=170, y=220, w=940),
        "rep": dict(type="liste", titre="Une réponse aux pessimistes", items=[
            "Ils décrivent le bonheur attendu passivement, comme un cadeau",
            "Ils ne prouvent pas qu'on ne puisse pas le construire"], marques=["✓", "→"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Pascal. Le divertissement nous détourne de penser à notre condition ; "
        "nous aimons la chasse, non la prise.",
        "{rec.2}Deux : Schopenhauer. Désirer, c'est souffrir ; être satisfait, c'est s'ennuyer. La vie oscille comme un pendule.",
        "{rec.3}Trois : Rousseau et Freud. On n'est heureux qu'avant d'être heureux ; et le bonheur n'est qu'un épisode.",
        "{rec.4}Quatre : l'adaptation hédonique, avec prudence. Et une distinction pour ta copie : le bonheur comme état, "
        "peut-être illusoire ; le bonheur comme activité, à construire.",
        "{-rec}{tab_fin}{q_suite}Reste une question. La morale doit-elle viser le bonheur ? "
        "Et l'État doit-il nous le promettre ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : bonheur, morale et politique. Kant, les utilitaristes, et l'État.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE BONHEUR, UNE ILLUSION ?", branches=[
            dict(t="Pascal", items=["le divertissement", "la chasse, non la prise", "le roi sans divertissement"]),
            dict(t="Schopenhauer", items=["désirer = manquer = souffrir", "le pendule : souffrance / ennui"]),
            dict(t="Rousseau, Freud", items=["heureux avant d'être heureux", "un bonheur épisodique", "trois sources de souffrance"]),
            dict(t="Répondre", items=["l'adaptation hédonique (prudence)", "bonheur-état / bonheur-activité", "Alain : vouloir son bonheur"])]),
        "tab_fin": dict(type="tableau", img="bh4-declaration", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="John Trumbull, La Déclaration d'indépendance, 1819 (Capitole des États-Unis, Washington)"),
        "q_suite": dict(type="question", t="L'État doit-il promettre le bonheur ?"),
        "fin": dict(type="titre", sur="À suivre", t="Bonheur, morale et politique", sous="Épisode 5 · Kant, l'utilitarisme, l'État"),
    }),
]

QUIZ = [
    dict(q="Selon Pascal, d'où vient tout le malheur des hommes ?",
         r=["De la pauvreté", "De ne savoir pas demeurer en repos, dans une chambre", "De l'injustice des rois", "De l'ignorance des sciences"],
         ok=1, voir="c_ch", ex="Pensées, fr. 139 : seuls et immobiles, nous pensons à notre condition, fragile et mortelle ; alors nous fuyons dans le divertissement."),
    dict(q="« Ce n'est que la chasse, et non pas la prise, qu'ils recherchent. » Que veut dire Pascal ?",
         r=["Qu'il faut chasser pour se nourrir", "Que nous aimons l'agitation qui nous détourne de penser, plus que le résultat",
            "Que le lièvre rend heureux", "Que la chasse est un péché"], ok=1,
         voir="prise", ex="Le lièvre offert ne nous divertirait pas : c'est la poursuite qui nous empêche de voir la mort et nos misères."),
    dict(q="Pour Schopenhauer, la vie oscille comme un pendule entre…",
         r=["le plaisir et la joie", "la souffrance et l'ennui", "le travail et le repos", "la raison et la passion"], ok=1,
         voir="c_pend", ex="Désirer, c'est manquer, donc souffrir ; être satisfait, c'est tomber dans l'ennui (Le Monde…, IV, § 57)."),
    dict(q="Selon Schopenhauer, qu'est-ce que la satisfaction ?",
         r=["Un bien positif et durable", "Seulement la fin d'une douleur", "La récompense de la vertu", "Une illusion des sens"], ok=1,
         voir="meca", ex="Le plaisir n'a rien de positif : il supprime un manque, puis l'ennui arrive."),
    dict(q="« On n'est heureux qu'avant d'être heureux. » Qui l'écrit, et que veut-il dire ?",
         r=["Pascal : il faut se divertir", "Rousseau : on jouit plus de ce qu'on espère que de ce qu'on obtient",
            "Freud : le bonheur est inconscient", "Schopenhauer : le désir est une souffrance"], ok=1,
         voir="c_av", ex="Julie ou la Nouvelle Héloïse, VI, 8 : l'imagination embellit l'objet désiré ; la possession déçoit."),
    dict(q="Pourquoi, selon Freud, le bonheur ne peut-il être qu'épisodique ?",
         r=["Parce que Dieu l'interdit", "Parce que seul le contraste nous procure une jouissance intense",
            "Parce que la société le défend", "Parce que la raison le refuse"], ok=1,
         voir="epi", ex="Malaise dans la civilisation, II : un plaisir prolongé s'émousse ; le bonheur naît d'une satisfaction soudaine."),
    dict(q="Que faut-il retenir de l'étude de 1978 sur les gagnants de la loterie ?",
         r=["Que l'argent ne fait jamais le bonheur", "Qu'on s'adapte en partie au meilleur comme au pire, mais l'étude est petite et discutée",
            "Que les accidentés sont plus heureux que les gagnants", "Qu'elle prouve la thèse de Pascal"], ok=1,
         voir="prud", ex="22 gagnants seulement, une note de 0 à 5 ; des études suédoises plus récentes nuancent : l'adaptation n'est pas totale."),
    dict(q="Quelle distinction permet de répondre aux pessimistes ?",
         r=["Plaisir / douleur", "Bonheur-état / bonheur-activité", "Corps / esprit", "Nature / culture"], ok=1,
         voir="dist", ex="Le bonheur comme état complet et définitif est sans doute illusoire ; le bonheur comme manière de vivre se construit (Aristote, Alain)."),
]

CREDITS = [
    "Portraits : Pascal (copie d'après François II Quesnel) ; Arthur Schopenhauer (photographie de Johann Schäfer, 1859) ; "
    "Rousseau (Maurice Quentin de La Tour, 1753) ; Freud (photographie, domaine public)",
    "Tableaux et gravures : Henri Rousseau, Surpris ! (1891) ; Vilhelm Hammershøi, Intérieur, Strandgade 30 (1900) ; Paolo Uccello, La Chasse nocturne (vers 1470) ; "
    "Hyacinthe Rigaud, Louis XIV en costume de sacre (1701) ; Philippe de Champaigne, Vanité (vers 1671) ; "
    "Katsushika Hokusai, La Grande Vague de Kanagawa (vers 1831) ; Edvard Munch, Le Cri (1893) et L'Enfant malade (1885-1886) ; "
    "Walter Sickert, Ennui (vers 1914) ; Caspar David Friedrich, Le Voyageur contemplant une mer de nuages (vers 1818) ; "
    "Jean-Michel Moreau le Jeune, illustration pour Julie ou la Nouvelle Héloïse (gravure, BnF) ; "
    "Antoine Watteau, Pèlerinage à l'île de Cythère (1717) ; Edgar Degas, Le Tub (1886) ; Henri Matisse, Le Bonheur de vivre (1905-1906) ; "
    "John Trumbull, La Déclaration d'indépendance (1819) : domaine public",
    "Photographies : buste de Pyrrhus, Naples (Marie-Lan Nguyen, domaine public) ; pendule de Foucault au Panthéon (Rsk6400, CC BY-SA 3.0) ; "
    "plaque de la Berggasse, Vienne (GuentherZ, CC BY 3.0) ; grille de loterie (Santeri Viinamäki, CC BY-SA 4.0) ; "
    "hamster dans sa roue (Rlicul, CC BY-SA 3.0)",
    "Citations : Pascal, Pensées, éd. Brunschvicg, fr. 139, 142, 172 ; Schopenhauer, Le Monde comme volonté et comme représentation, "
    "IV, § 57, trad. Auguste Burdeau ; Rousseau, Julie ou la Nouvelle Héloïse, VI, 8 (1761) ; Freud, Malaise dans la civilisation, II (1930), "
    "citation approchée ; Alain, Propos sur le bonheur (1928). Étude : P. Brickman, D. Coates, R. Janoff-Bulman, Journal of Personality "
    "and Social Psychology, 1978 ; E. Lindqvist, R. Östling, D. Cesarini, Review of Economic Studies, 2020.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
