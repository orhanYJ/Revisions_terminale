"""Le bonheur, épisode 1 : « Qu'est-ce que le bonheur ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la raison} dans le texte lu.
Citations : Aristote, Éthique à Nicomaque, trad. J.-F. Thurot (1823), Wikisource ; Pascal, Pensées, éd. Brunschvicg,
fragment 425, Wikisource ; Kant, Fondements de la métaphysique des mœurs, section II, trad. Victor Delbos (1907), Wikisource.
L'expérience de la machine à expériences (Nozick, 1974) et l'inventaire de Kant sont résumés par le narrateur.
"""

CODE = "bonheur-1"
NOTION = "Le bonheur"
NUM = 1
TITRE = "Qu'est-ce que le bonheur ?"
SUIVANT = "Épisode 2 · Le plaisir rend-il heureux ?"
PRONONCIATION = {"eudaimonia": "eudaïmonia", "daimôn": "daïmône", "augurium": "augourioum", "beatitudo": "béatitoudo",
                 "happiness": "hapinesse", "hap": "hape", "to happen": "tou hapène", "Glück": "Gluk",
                 "Nozick": "Nozik"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{tab_lot}{q_lot}Imagine. Un mardi soir, tu vérifies, sans trop y croire, les numéros d'un ticket de loterie. "
        "Un numéro… deux… trois… Tous. Tu viens de gagner des {!millions}millions.",
        ("Ta vie va changer. Tu vas être heureux. Enfin.", {"rate": "-5%"}),
        "{-q_lot}{-tab_lot}{tab_mou}{voeux}Tu fais déjà la liste. {voeux.1}Une maison. {voeux.2}Des voyages. "
        "{voeux.3}Plus jamais de réveil à six heures. {voeux.4}Des cadeaux pour ceux que tu aimes.",
        "{-voeux}{q_an}Mais un an plus tard… seras-tu vraiment plus heureux ? Des psychologues se sont posé la question. "
        "La réponse est plus surprenante qu'on ne croit : nous la verrons dans l'épisode quatre.",
        "{-q_an}{attente}Car au fond, qu'attendais-tu de cet argent ? Pas l'argent lui-même. "
        "Tu attendais ce que tout le monde attend : {attente.1}être heureux.",
        "{-attente}{q_bh}Le bonheur. Tout le monde le veut. Mais demande à dix personnes ce que c'est : "
        "tu obtiendras dix réponses.",
        "{-q_bh}{serie}Cette série va prendre ce mot au sérieux. Avec Aristote, Épicure, les stoïciens, Pascal, Kant… "
        "Six épisodes, et un récapitulatif. Celui-ci est le premier. "
        "Car avant de chercher le bonheur… {-serie}il faut savoir ce que l'on cherche.",
        ("P", 0.3),
        "{-tab_mou}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_lot": dict(type="tableau", img="bh1-loterie", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.35, .5, .25],
                        legende="Loterie nationale, affiche des résultats d'un tirage, années 1930 (Imprimerie nationale, CC0)"),
        "q_lot": dict(type="question", t="Et si tu gagnais des millions ?"),
        "tab_mou": dict(type="tableau", img="bh1-moulin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .4],
                        legende="Pierre-Auguste Renoir, Bal du moulin de la Galette, 1876 (musée d'Orsay)"),
        "voeux": dict(type="nuage", items=["une maison", "des voyages", "plus de réveil", "des cadeaux"]),
        "q_an": dict(type="question", t="Un an plus tard, seras-tu vraiment plus heureux ?"),
        "attente": dict(type="mot", t="Être heureux", g="ce que tout le monde attend… de tout le reste", y=260, taille=100),
        "q_bh": dict(type="question", t="Le bonheur : tout le monde le veut. Mais qu'est-ce que c'est ?"),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="une notion, regardée sous tous ses angles", y=270),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 1", t="Qu'est-ce que le bonheur ?",
                      sous="Le mot, les distinctions, la fin dernière"),
    }),

    # ------------------------------------------------------------------ I. le mot
    dict(id="mot", chap="Le mot", fond="aube", humeur="mystere", notions=["le langage", "la religion"],
         retenir="Bonheur : le bon heur, la bonne chance. Eudaimonia : un bon génie. Beatitudo : la plénitude.",
         beats=[
        "{tab_aug}Commençons, comme toujours, par le mot. {bh_mot}Bonheur : bon… heur. "
        "Et l'heur, en vieux français, c'est le sort, la chance.",
        "{-bh_mot}{etym}{etym.1}Le mot vient du latin augurium : le présage. À Rome, l'augure observait le vol des oiseaux, "
        "son bâton recourbé à la main, pour savoir si les dieux étaient favorables. "
        "{etym.2}Un bon augure, c'est un bon présage. {etym.3}Le bonheur, à l'origine, c'est donc… la {!chance}chance. "
        "Ce qui t'arrive. Pas ce que tu fais.",
        "{-etym}{-tab_aug}{tab_for}{ling}Et ce n'est pas propre au français. {ling.1}En anglais, happiness vient de hap : "
        "le hasard, ce qui arrive, comme dans le verbe to happen. {ling.2}En allemand, Glück veut dire à la fois "
        "le bonheur… et la chance.",
        "{-ling}{roue}Au Moyen Âge, on peignait la Fortune avec une roue. Regarde : celui qui trône en haut, couronné, "
        "sera bientôt précipité en bas. {roue.1}Le bonheur qui dépend de la chance est fragile : "
        "ce que la roue donne, la roue le reprend.",
        "{-roue}{-tab_for}{tab_vas}{grec}Les Grecs avaient un autre mot : eudaimonia. "
        "Eu, c'est bien ; daimôn, c'est une divinité, un génie protecteur. Être heureux, c'est avoir un bon génie : "
        "être bien accompagné par le destin.",
        "{-grec}{grec2}Mais les philosophes grecs vont tirer ce mot ailleurs. Pour eux, l'eudaimonia devient la vie réussie, "
        "accomplie : non plus ce qui nous arrive, mais ce que nous faisons de notre vie. Ce sera tout l'épisode trois.",
        "{-grec2}{-tab_vas}{tab_bea}{lat}Enfin, le latin : beatitudo, qui a donné notre mot béatitude. C'est le bonheur parfait, "
        "complet, celui que la {#la religion}religion chrétienne promet aux élus. "
        "Regarde ces âmes qui dansent au paradis : il ne leur manque plus rien.",
        "{-lat}{trois}Retiens ces trois visages du mot. {trois.1}La chance : le bonheur qui m'arrive. "
        "{trois.2}La vie réussie : le bonheur que je construis. {trois.3}La plénitude : un bonheur parfait, "
        "peut-être hors de ce monde.",
        ("Toute la série va hésiter entre ces trois-là.", {"rate": "-5%"}),
        "{-trois}",
    ], vis={
        "tab_aug": dict(type="tableau", img="bh1-augure", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .45, .4],
                        legende="Le lituus, bâton de l'augure, dans G. du Choul, Discours de la religion des anciens Romains, 1581"),
        "bh_mot": dict(type="mot", t="bon · heur", g="vieux français : l'heur, c'est le sort, la chance", y=250, taille=110),
        "etym": dict(type="liste", titre="D'où vient le mot ?", items=[
            "heur ← latin augurium : le présage", "bon heur : un bon présage", "le bonheur, d'abord : la chance"],
                     marques=["1", "2", "3"], cles=["augurium", "présage", "chance"], x=170, y=170, w=940),
        "tab_for": dict(type="tableau", img="bh1-fortune", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .45, .72],
                        legende="La roue de la Fortune, d'après l'Hortus deliciarum d'Herrade de Landsberg (XIIᵉ s.), copie du XIXᵉ s."),
        "ling": dict(type="liste", titre="Ailleurs aussi", items=[
            "Anglais : happiness ← hap, le hasard (to happen)", "Allemand : Glück, le bonheur et la chance"],
                     marques=["EN", "DE"], x=170, y=190, w=940),
        "roue": dict(type="note", titre="La roue de la Fortune", cles=["roue", "fragile"],
                     t="Celui qui trône en haut sera bientôt en bas : le bonheur-chance est fragile.",
                     etape="Ce que la roue donne, la roue le reprend.", x=170, y=170, w=940),
        "tab_vas": dict(type="tableau", img="bh1-vase", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.35, .5, .4],
                        legende="Lécythe attique, manière du Peintre de Meidias, Aphrodite et Éros parmi des allégories, fin du Vᵉ s. av. J.-C. (photo ArchaiOptix, CC BY-SA 4.0)"),
        "grec": dict(type="mot", t="εὐδαιμονία", g="eudaimonia · eu : bien ; daimôn : un génie, une divinité", y=240, taille=96),
        "grec2": dict(type="def", terme="L'eudaimonia des philosophes", cles=["réussie", "faisons"],
                      t="La vie réussie, accomplie : non plus ce qui nous arrive, mais ce que nous faisons de notre vie.",
                      etape="Voir l'épisode 3 : Aristote et les stoïciens.", x=170, y=200, w=940),
        "tab_bea": dict(type="tableau", img="bh1-beatitude", fond=True, sombre=True, de=[2.0, .2, .85], a=[2.2, .15, .9],
                        legende="Fra Angelico, Le Jugement dernier, détail : la ronde des élus au paradis, v. 1431 (musée San Marco, Florence)"),
        "lat": dict(type="mot", t="BEATITUDO", g="latin : la béatitude, le bonheur parfait", y=250, taille=100),
        "trois": dict(type="liste", titre="Trois visages du bonheur", items=[
            "La chance : le bonheur qui m'arrive", "La vie réussie : le bonheur que je construis",
            "La plénitude : un bonheur parfait, peut-être hors de ce monde"], marques=["1", "2", "3"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ II. plaisir, joie, satisfaction
    dict(id="distinctions", chap="Plaisir, joie, bonheur", fond="nuit", humeur="lumiere", notions=["le temps", "la conscience"],
         retenir="Le plaisir est un instant, la joie un élan, la satisfaction un désir comblé. Le bonheur : un état durable, qui porte sur toute une vie.",
         beats=[
        "{tab_esc}{q_dist}Deuxième étape : ne pas tout confondre. Le bonheur, est-ce la même chose que le plaisir ?",
        "{-q_dist}{plai}Le plaisir, d'abord. C'est une sensation agréable : un carré de chocolat, une douche chaude, "
        "une musique qu'on aime. {plai.1}Il est localisé, souvent dans le corps. Et surtout, il est bref : "
        "il naît, il monte, il s'éteint.",
        "{-plai}{-tab_esc}{tab_can}{joie}La joie, ensuite. Elle est plus large : c'est tout mon être qui est touché. "
        "Un ami retrouvé, un examen réussi, une victoire en finale. {joie.1}Mais elle aussi passe : "
        "c'est un élan, un sommet.",
        "{-joie}{-tab_can}{tab_coc}{satis}La satisfaction, enfin : c'est un désir comblé. J'avais faim, j'ai mangé. "
        "{satis.1}Regarde ces trois hommes, étendus au pays de Cocagne, le ventre plein. Satisfaits, sans aucun doute. "
        "Heureux ? On a du mal à le croire.",
        "{-satis}{-tab_coc}{tab_age}{def_bh}Le bonheur, lui, n'est pas un moment. C'est un état : "
        "{def_bh.1}une satisfaction durable, qui ne porte pas sur tel ou tel désir, mais sur l'ensemble de ma vie.",
        "{-def_bh}{tabl}Mets les quatre côte à côte. {tabl.1}Le plaisir dure un instant. {tabl.2}La joie, un moment. "
        "{tabl.3}La satisfaction, le temps qu'un nouveau désir revienne. {tabl.4}Le bonheur, lui, se mesure "
        "à l'échelle d'une vie.",
        "{-tabl}{sans}D'où deux remarques. {sans.1}On peut avoir mille plaisirs sans être heureux : "
        "pense à celui qui fait la fête tous les soirs pour oublier qu'il s'ennuie. "
        "{sans.2}Et l'on peut être heureux malgré une douleur, un deuil, une maladie.",
        "{-sans}{dur}Le bonheur entretient donc un rapport particulier avec le {#le temps}temps : il demande de la durée. "
        "C'est pourquoi on se dit souvent heureux… après coup, en regardant en arrière.",
        ("J'étais heureux, et je ne le savais pas.", {"rate": "-6%", "pitch": "-1Hz"}),
        "{-dur}",
    ], vis={
        "tab_esc": dict(type="tableau", img="bh1-escarpolette", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .55, .4],
                        legende="Jean-Honoré Fragonard, Les Hasards heureux de l'escarpolette, 1767 (Wallace Collection, Londres)"),
        "q_dist": dict(type="question", t="Le bonheur, est-ce la même chose que le plaisir ?"),
        "plai": dict(type="def", terme="Le plaisir", cles=["sensation", "bref"],
                     t="Une sensation agréable : un carré de chocolat, une douche chaude, une musique.",
                     etape="Localisé, souvent dans le corps ; et bref : il naît, il monte, il s'éteint.", x=170, y=190, w=940),
        "tab_can": dict(type="tableau", img="bh1-canotiers", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Pierre-Auguste Renoir, Le Déjeuner des canotiers, 1880-1881 (Phillips Collection, Washington)"),
        "joie": dict(type="def", terme="La joie", cles=["être", "élan"],
                     t="Une émotion qui touche tout mon être : un ami retrouvé, un examen réussi.",
                     etape="Plus large que le plaisir, mais elle passe : un élan, un sommet.", x=170, y=190, w=940),
        "tab_coc": dict(type="tableau", img="bh1-cocagne", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.35, .5, .62],
                        legende="Pieter Bruegel l'Ancien, Le Pays de Cocagne, 1567 (Alte Pinakothek, Munich)"),
        "satis": dict(type="def", terme="La satisfaction", cles=["désir", "comblé"],
                      t="Un désir comblé : j'avais faim, j'ai mangé.",
                      etape="Satisfaits… mais heureux ?", x=170, y=170, w=940),
        "tab_age": dict(type="tableau", img="bh1-ages", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Caspar David Friedrich, Les Âges de la vie, v. 1835 (Museum der bildenden Künste, Leipzig)"),
        "def_bh": dict(type="def", terme="Le bonheur", cles=["état", "durable", "ensemble"],
                       t="Un état, et non un moment.",
                       etape="Une satisfaction durable, qui porte sur l'ensemble de ma vie.", x=170, y=200, w=940),
        "tabl": dict(type="liste", titre="Combien de temps ?", items=[
            "Le plaisir : un instant", "La joie : un moment", "La satisfaction : jusqu'au désir suivant",
            "Le bonheur : l'échelle d'une vie"], marques=["·", "·", "·", "∞"], x=170, y=150, w=940),
        "sans": dict(type="liste", titre="Deux remarques", items=[
            "Des plaisirs sans bonheur : la fête pour oublier l'ennui", "Un bonheur malgré la douleur, le deuil, la maladie"],
                     marques=["✗", "✓"], x=170, y=190, w=940),
        "dur": dict(type="tag", style="repere", t="Le bonheur demande de la durée : instantané ≠ durable", x=170, y=560, w=720),
    }),

    # ------------------------------------------------------------------ III. subjectif ou objectif
    dict(id="subjectif", chap="Une affaire de goût ?", fond="aube", humeur="mystere", notions=["la vérité", "la conscience"],
         retenir="Le bonheur, est-ce ce que je ressens (subjectif) ou une vie réellement bonne (objectif) ? Le repère objectif / subjectif traverse toute la notion.",
         beats=[
        "{tab_doc}{q_quoi}Mais alors, qu'est-ce qui rend heureux ? Aristote remarquait déjà que chacun répond "
        "selon ce qui lui manque.",
        "{-q_quoi}",
        ("C", "S'il est malade, il voit le bonheur dans la santé ; s'il est pauvre, il le voit dans la richesse.", "c_mal"),
        "{-c_mal}{subj}D'où une idée tentante. {subj.g}Le bonheur serait subjectif : il dépendrait de chacun. "
        "Est heureux celui qui se sent heureux, et personne ne peut en juger à sa place.",
        "{subj.d}Pourtant, on dit aussi : il croit être heureux, mais il se trompe. C'est l'idée d'un bonheur objectif : "
        "une vie réellement bonne, que l'on peut juger de l'extérieur. La santé, des amis, une activité qui a du sens.",
        "{-subj}{-tab_doc}{tab_rev}{mach}Pour aller plus loin, une expérience de pensée, imaginée en 1974 "
        "par le philosophe américain Robert Nozick. {mach.1}Une machine se branche sur ton cerveau, "
        "et te fait vivre, jusqu'à la fin de tes jours, la vie de tes rêves. "
        "{mach.2}Succès, amour, aventures : tu croirais tout réel. {mach.3}Accepterais-tu d'y entrer ?",
        ("Réfléchis bien.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-mach}{refus}La plupart des gens refusent. Pourquoi ? Parce que nous ne voulons pas seulement nous sentir heureux. "
        "{refus.1}Nous voulons que ce soit {#la vérité}vrai : être vraiment aimés, réussir vraiment, "
        "{refus.2}et le faire nous-mêmes, au lieu de rêver qu'on le fait.",
        "{-refus}{-tab_rev}{tab_age2}{os}Le bonheur a donc deux faces. {os.g}Un sentiment, que moi seul peux éprouver. "
        "{os.d}Et une réalité, qui ne dépend pas que de moi.",
        "Retiens le repère : objectif, subjectif. Il va traverser toute la série. "
        "Le plaisir d'Épicure, la sagesse des stoïciens, le soupçon de Pascal : chacun choisira son camp.",
        "{-os}{-tab_age2}",
    ], vis={
        "tab_doc": dict(type="tableau", img="bh1-docteur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Luke Fildes, Le Docteur, 1891 (Tate Britain, Londres)"),
        "q_quoi": dict(type="question", t="Qu'est-ce qui rend heureux ?"),
        "c_mal": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, livre I, 4 (IVᵉ s. av. J.-C.), trad. Thurot", x=170, y=170, w=940),
        "subj": dict(type="cols", g="Subjectif", gq="ce que je ressens : est heureux qui se sent heureux",
                     d="Objectif", dq="une vie réellement bonne : santé, amis, activité qui a du sens", vs="≠"),
        "tab_rev": dict(type="tableau", img="bh1-reve", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .5],
                        legende="Henri Rousseau, Le Rêve, 1910 (Museum of Modern Art, New York)"),
        "mach": dict(type="liste", titre="La machine à expériences (Nozick, 1974)", items=[
            "Une machine branchée sur ton cerveau", "La vie de tes rêves : tu croirais tout réel",
            "Accepterais-tu d'y entrer ?"], marques=["1", "2", "?"], x=170, y=160, w=940, plus=True),
        "refus": dict(type="liste", titre="Pourquoi la plupart refusent", items=[
            "Nous voulons que ce soit vrai", "Et le faire nous-mêmes, pas le rêver"], marques=["✓", "✓"],
                      cles=["vrai", "nous-mêmes"], x=170, y=190, w=940),
        "tab_age2": dict(type="tableau", img="bh1-ages", fond=True, sombre=True, de=[1.3, .3, .55], a=[1.1, .5, .5],
                         legende="Caspar David Friedrich, Les Âges de la vie, v. 1835 (Museum der bildenden Künste, Leipzig)"),
        "os": dict(type="cols", g="Un sentiment", gq="que moi seul peux éprouver", d="Une réalité",
                   dq="qui ne dépend pas que de moi", vs="+", repere="Repère · objectif / subjectif"),
    }),

    # ------------------------------------------------------------------ IV. la fin dernière
    dict(id="fin", chap="Ce que tous veulent", fond="nuit", humeur="lumiere", notions=["le travail", "la raison"],
         retenir="Le bonheur est la fin dernière : on veut tout le reste pour lui, et lui pour lui-même (Aristote). Tous les hommes le recherchent (Pascal).",
         beats=[
        "{tab_exa}{chain}Fais une expérience. Demande-toi pourquoi tu fais ce que tu fais. "
        "{chain.1}Pourquoi tu révises ? Pour avoir ton bac. {chain.2}Pourquoi le bac ? Pour faire des études. "
        "{chain.3}Pourquoi des études ? Pour un {#le travail}métier qui te plaise. "
        "{chain.4}Et pourquoi un métier qui te plaise ? … Pour être heureux.",
        ("Et pourquoi veux-tu être heureux ?", {"pitch": "+2Hz"}),
        "{-chain}{-tab_exa}{arist}{tab_ath}La question n'a plus de sens. C'est ce qu'a vu Aristote, au quatrième siècle "
        "avant notre ère, au début de son Éthique à Nicomaque.",
        ("C", "Presque tout le monde, à vrai dire, est d'accord sur son nom ; car les hommes instruits, aussi bien que "
              "le vulgaire, l'appellent le bonheur.", "c_nom"),
        "{-c_nom}{moy}Nos actions s'enchaînent comme des moyens en vue de fins. Mais la chaîne ne peut pas aller à l'infini : "
        "{moy.1}il faut un point d'arrivée. Quelque chose que l'on veut pour lui-même, et jamais pour autre chose.",
        "{-moy}",
        ("C", "On peut donc dire que le bonheur est quelque chose de parfait et qui se suffit à soi-même, "
              "puisqu'il est la fin de tous nos actes.", "c_fin"),
        "{-arist}{-c_fin}{fin_def}Voilà la définition la plus solide. Le bonheur est la {!fin}fin dernière. "
        "{fin_def.1}On veut l'argent pour autre chose ; on veut le bonheur pour lui-même. "
        "Il ne sert à rien : c'est tout le reste qui lui sert.",
        "{-fin_def}{-tab_ath}{pascal}{tab_pen}Deux mille ans plus tard, au dix-septième siècle, Blaise Pascal le dit "
        "avec une force inouïe.",
        ("C", "Tous les hommes recherchent d'être heureux ; cela est sans exception ; quelques différents moyens "
              "qu'ils y emploient, ils tendent tous à ce but.", "c_pas"),
        "{-c_pas}{pas_n}Celui qui part à la guerre et celui qui reste chez lui, ajoute Pascal, cherchent la même chose, "
        "par des chemins opposés. {pas_n.1}C'est le motif de toutes nos actions, jusqu'aux plus désespérées.",
        ("Personne ne choisit d'être malheureux pour le plaisir de l'être.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-pas_n}{-pascal}{-tab_pen}",
    ], vis={
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "chain": dict(type="liste", titre="Pourquoi ?", items=[
            "Je révise → pour le bac", "Le bac → pour des études", "Des études → pour un métier qui me plaise",
            "Un métier qui me plaise → pour être heureux"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "arist": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      legende="Éthique à Nicomaque", x=110, y=120, w=330, h=420),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.6, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 · au centre, Platon et Aristote"),
        "c_nom": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, I, 4, trad. Thurot (1823)", x=640, y=150, w=570),
        "moy": dict(type="note", titre="La chaîne des fins", cles=["infini", "lui-même"],
                    t="Des moyens en vue de fins… mais pas à l'infini.",
                    etape="Il faut une fin que l'on veut pour elle-même.", x=640, y=170, w=570),
        "c_fin": dict(type="cit", a="Aristote", o="Éthique à Nicomaque, I, 7, trad. Thurot (1823)", x=640, y=150, w=570),
        "fin_def": dict(type="def", terme="Le bonheur, fin dernière", cles=["lui-même", "sert"],
                        t="Ce que l'on veut pour lui-même, et jamais en vue d'autre chose.",
                        etape="L'argent est un moyen ; le bonheur, une fin. Repère · moyen / fin", x=170, y=200, w=940),
        "pascal": dict(type="portrait", annee=1623, img="pascal", nom="Blaise Pascal", dates="1623 – 1662",
                       legende="Pensées (1670, posthume)", x=110, y=120, w=330, h=420),
        "tab_pen": dict(type="tableau", img="bh1-pensees", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .45],
                        legende="Pascal, Pensées sur la religion, manuscrit (BnF, Gallica)"),
        "c_pas": dict(type="cit", a="Pascal", o="Pensées, fragment 425 (éd. Brunschvicg)", x=640, y=150, w=570),
        "pas_n": dict(type="note", titre="Pascal", cles=["guerre", "motif"],
                      t="Celui qui part à la guerre et celui qui reste cherchent la même chose.",
                      etape="Le motif de toutes nos actions.", x=640, y=170, w=570),
    }),

    # ------------------------------------------------------------------ V. un idéal de l'imagination
    dict(id="ideal", chap="Un idéal de l'imagination", fond="aube", humeur="tension", notions=["la raison", "le devoir"],
         retenir="Kant : tout homme veut être heureux, mais personne ne sait dire ce qu'il veut. Le bonheur est un idéal de l'imagination, non de la raison.",
         beats=[
        "{kant}{tab_kon}Tout le monde veut être heureux, donc. Mais sait-on ce que l'on veut ? "
        "En 1785, Emmanuel Kant met le doigt sur le problème.",
        ("C", "Le concept du bonheur est un concept si indéterminé, que, malgré le désir qu'a tout homme d'arriver à être "
              "heureux, personne ne peut jamais dire en termes précis et cohérents ce que véritablement il désire et il veut.",
         "c_ind"),
        "{-kant}{-c_ind}{-tab_kon}{tab_amb}{inv}Kant fait l'inventaire. {inv.1}Veux-tu la richesse ? Que de soucis, "
        "que d'envie, que de pièges ! {inv.2}La connaissance ? Elle te montrera peut-être des malheurs que tu ignorais. "
        "{inv.3}Une longue vie ? Qui te dit que ce ne sera pas une longue souffrance ? "
        "{inv.4}Même la santé parfaite peut pousser à des excès qu'un peu de fragilité aurait évités.",
        "{-inv}{anam}Regarde ces deux ambassadeurs, peints par Holbein : la richesse, le savoir, les instruments de la science… "
        "{anam.1}et, au premier plan, une forme étrange, étirée. Une tête de mort, déformée. "
        "Tout ce que l'on possède peut se retourner contre nous.",
        "{-anam}{-tab_amb}{tab_jeu}",
        ("C", "Le bonheur est un idéal, non de la raison, mais de l'imagination.", "c_ideal"),
        "{-c_ideal}{ima}Ce jeune homme rame vers un château dans les nuages. Voilà le bonheur selon Kant : "
        "une image que chacun se forme à partir de son expérience, et que la {#la raison}raison ne peut pas calculer. "
        "{ima.1}Pour être heureux, il n'existe donc pas de règle sûre : seulement des conseils de prudence.",
        "{-ima}{cons}Et Kant en tire une conséquence immense. Si le bonheur est si incertain, la morale ne peut pas "
        "reposer sur lui. On l'a vu dans la série sur le devoir : {cons.1}la morale ne dit pas « sois heureux », "
        "elle dit « rends-toi digne de l'être ». Nous y reviendrons dans l'épisode cinq.",
        "{-cons}{-tab_jeu}{tab_mou2}{plan}Voilà donc les grandes questions de la série. "
        "{plan.1}Le plaisir rend-il heureux ? Aristippe, Épicure, Calliclès. "
        "{plan.2}Le bonheur est-il affaire de sagesse ? Aristote, les stoïciens, Spinoza. "
        "{plan.3}Et s'il n'était qu'une illusion ? Pascal, Schopenhauer, Freud. "
        "{plan.4}Peut-on, doit-on, rendre les autres heureux ? Kant, les utilitaristes, l'État. "
        "{plan.5}Et enfin, ta copie.",
        ("P", 0.8),
        "{-plan}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Fondements de la métaphysique des mœurs (1785)", x=110, y=120, w=330, h=420),
        "tab_kon": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Königsberg, ville de Kant, photochrome, vers 1900 (domaine public)"),
        "c_ind": dict(type="cit", a="Kant", o="Fondements de la métaphysique des mœurs, section II (1785), trad. Delbos",
                      x=640, y=130, w=570),
        "tab_amb": dict(type="tableau", img="bh1-ambassadeurs", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .7],
                        legende="Hans Holbein le Jeune, Les Ambassadeurs, 1533 (National Gallery, Londres)"),
        "inv": dict(type="liste", titre="L'inventaire de Kant", items=[
            "La richesse ? Soucis, envie, pièges", "La connaissance ? Des malheurs qu'on ignorait",
            "Une longue vie ? Peut-être une longue souffrance", "La santé ? Elle aussi peut nous perdre"],
                    marques=["?", "?", "?", "?"], x=170, y=150, w=940),
        "anam": dict(type="note", titre="Holbein, Les Ambassadeurs", cles=["richesse", "mort"],
                     t="La richesse, le savoir, les instruments de la science…",
                     etape="… et, au premier plan, une tête de mort déformée (une anamorphose).", x=170, y=130, w=940),
        "tab_jeu": dict(type="tableau", img="bh1-jeunesse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.4, .25, .35],
                        legende="Thomas Cole, Le Voyage de la vie : la jeunesse, 1840-1842"),
        "c_ideal": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=200, w=940),
        "ima": dict(type="def", terme="Un idéal de l'imagination", cles=["image", "calculer", "prudence"],
                    t="Une image que chacun se forme d'après son expérience : la raison ne peut pas la calculer.",
                    etape="Pas de règle sûre pour être heureux : des conseils de prudence.", x=170, y=190, w=940),
        "cons": dict(type="note", titre="Conséquence", cles=["morale", "digne"],
                     t="Le bonheur est trop incertain pour fonder la morale.",
                     etape="« Rends-toi digne d'être heureux » : voir l'épisode 5.", x=170, y=200, w=940),
        "tab_mou2": dict(type="tableau", img="bh1-moulin", fond=True, sombre=True, de=[1.3, .6, .45], a=[1.0, .5, .5],
                         legende="Pierre-Auguste Renoir, Bal du moulin de la Galette, 1876 (musée d'Orsay)"),
        "plan": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · Le plaisir rend-il heureux ?", "Ép. 3 · La sagesse des Anciens",
            "Ép. 4 · Le bonheur est-il une illusion ?", "Ép. 5 · Bonheur, morale et politique",
            "Ép. 6 · Le bonheur à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_can2}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le mot. Le bonheur, c'est d'abord la bonne chance ; "
        "les Grecs en ont fait la vie réussie.",
        "{rec.2}Deux : ne pas confondre. Le plaisir est un instant ; le bonheur, un état durable qui porte sur toute une vie.",
        "{rec.3}Trois : le repère objectif, subjectif. Se sentir heureux, est-ce la même chose qu'avoir une vie heureuse ?",
        "{rec.4}Quatre : le bonheur est la fin dernière, que tous recherchent, selon Aristote et Pascal ; "
        "mais, dit Kant, personne ne sait dire en quoi il consiste.",
        "{-rec}{-tab_can2}{tab_fin}{q_suite}Alors, faut-il chercher plus simple ? Et si le bonheur, c'était tout bonnement… "
        "le plaisir ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : le plaisir rend-il heureux ? Aristippe, Épicure, et les tonneaux percés.",
         {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_can2": dict(type="tableau", img="bh1-canotiers", fond=True, sombre=True, de=[1.25, .6, .4], a=[1.0, .5, .5],
                         legende="Pierre-Auguste Renoir, Le Déjeuner des canotiers, 1880-1881 (Phillips Collection, Washington)"),
        "rec": dict(type="carte", centre="LE BONHEUR", branches=[
            dict(t="Le mot", items=["bon heur : la chance", "eudaimonia : la vie réussie", "beatitudo : la plénitude"]),
            dict(t="Ne pas confondre", items=["plaisir : un instant", "joie, satisfaction", "bonheur : durable, total"]),
            dict(t="Objectif / subjectif", items=["se sentir heureux", "une vie bonne", "la machine de Nozick"]),
            dict(t="La fin dernière", items=["Aristote : voulu pour lui-même", "Pascal : tous le recherchent",
                                             "Kant : un idéal de l'imagination"])]),
        "tab_fin": dict(type="tableau", img="bh1-romains", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Thomas Couture, Les Romains de la décadence, 1847 (musée d'Orsay)"),
        "q_suite": dict(type="question", t="Et si le bonheur, c'était tout simplement le plaisir ?"),
        "fin": dict(type="titre", sur="À suivre", t="Le plaisir rend-il heureux ?",
                    sous="Épisode 2 · Aristippe, Épicure, Calliclès"),
    }),
]

QUIZ = [
    dict(q="D'où vient le mot « bonheur » ?",
         r=["Du latin bonum, le bien", "De « bon » et « heur », la chance, le sort (latin augurium)",
            "Du grec eudaimonia", "De l'anglais happiness"], ok=1,
         voir="etym", ex="L'heur, c'est le sort, le présage (augurium). Le bonheur est d'abord la bonne chance : ce qui nous arrive, pas ce que nous faisons."),
    dict(q="Qu'est-ce qui distingue le bonheur du plaisir ?",
         r=["Le bonheur est plus intense", "Le bonheur est un état durable qui porte sur l'ensemble d'une vie",
            "Le plaisir est toujours mauvais", "Il n'y a aucune différence"], ok=1,
         voir="def_bh", ex="Le plaisir est bref et localisé ; le bonheur est une satisfaction durable et totale. On peut avoir des plaisirs sans être heureux."),
    dict(q="Le fêtard qui sort tous les soirs pour oublier son ennui montre que…",
         r=["le plaisir suffit au bonheur", "l'on peut avoir des plaisirs sans être heureux",
            "le bonheur est objectif", "la joie dure plus longtemps que le plaisir"], ok=1,
         voir="sans", ex="Plaisir et bonheur ne se confondent pas : l'accumulation de plaisirs peut masquer l'absence de bonheur."),
    dict(q="Pourquoi la plupart des gens refusent-ils la « machine à expériences » de Nozick ?",
         r=["Parce qu'elle est dangereuse", "Parce que nous voulons que notre bonheur soit réel, et le vivre nous-mêmes",
            "Parce que les rêves sont désagréables", "Parce que la machine coûte trop cher"], ok=1,
         voir="refus", ex="Se sentir heureux ne suffit pas : nous voulons être vraiment aimés, réussir vraiment. Repère : objectif / subjectif."),
    dict(q="Selon Aristote, le bonheur est…",
         r=["un moyen pour obtenir la richesse", "la fin dernière, voulue pour elle-même et non en vue d'autre chose",
            "une affaire de chance seulement", "un plaisir du corps"], ok=1,
         voir="c_fin", ex="Éthique à Nicomaque, I : nos actions s'enchaînent comme moyens et fins ; le bonheur est le terme de la chaîne, ce qui se suffit à soi-même."),
    dict(q="« Tous les hommes recherchent d'être heureux ; cela est sans exception. » Qui l'a écrit ?",
         r=["Aristote", "Kant", "Pascal", "Épicure"], ok=2,
         voir="c_pas", ex="Pascal, Pensées (fr. 425 Brunschvicg) : c'est le motif de toutes les actions de tous les hommes."),
    dict(q="Pourquoi Kant dit-il que le bonheur est « un idéal de l'imagination » ?",
         r=["Parce que le bonheur n'existe pas", "Parce que personne ne peut dire avec précision ce qu'il veut pour être heureux",
            "Parce que seuls les artistes sont heureux", "Parce que la raison suffit à le définir"], ok=1,
         voir="c_ideal", ex="Le concept du bonheur est indéterminé et empirique : la raison ne peut en donner de règle sûre, seulement des conseils de prudence."),
]

CREDITS = [
    "Portraits : Aristote (buste, Rome, Palazzo Altemps, photographie Jastrow, domaine public) ; Blaise Pascal (copie d'après François II Quesnel) ; "
    "Emmanuel Kant (portrait anonyme, XVIIIᵉ s.) : domaine public",
    "Tableaux : Pierre-Auguste Renoir, Bal du moulin de la Galette (1876) et Le Déjeuner des canotiers (1880-1881) ; "
    "Fra Angelico, Le Jugement dernier (v. 1431) ; Jean-Honoré Fragonard, Les Hasards heureux de l'escarpolette (1767) ; "
    "Pieter Bruegel l'Ancien, Le Pays de Cocagne (1567) ; Caspar David Friedrich, Les Âges de la vie (v. 1835) ; "
    "Luke Fildes, Le Docteur (1891) ; Henri Rousseau, Le Rêve (1910) ; Raphaël, L'École d'Athènes (1509-1511) ; "
    "Hans Holbein le Jeune, Les Ambassadeurs (1533) ; Thomas Cole, Le Voyage de la vie : la jeunesse (1840) ; "
    "Thomas Couture, Les Romains de la décadence (1847) : domaine public",
    "Documents et photographies : Loterie nationale, affiche de résultats (années 1930, Imprimerie nationale, CC0) ; "
    "G. du Choul, Discours de la religion des anciens Romains (1581, Internet Archive Book Images, sans restriction) ; "
    "roue de la Fortune d'après l'Hortus deliciarum (domaine public) ; lécythe à la manière du Peintre de Meidias "
    "(photo ArchaiOptix, CC BY-SA 4.0) ; Pascal, Pensées, manuscrit (BnF, Gallica, domaine public) ; "
    "Königsberg, photochrome (vers 1900) ; salle d'examen : domaine public sauf mention",
    "Citations : Aristote, Éthique à Nicomaque, trad. J.-F. Thurot (1823) ; Pascal, Pensées, éd. Brunschvicg ; "
    "Kant, Fondements de la métaphysique des mœurs, trad. V. Delbos (1907) : Wikisource.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
