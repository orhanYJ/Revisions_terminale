"""Le bonheur, épisode 6 : « Le bonheur à l'épreuve du bac »

Même structure que devoir_6.py : trois sujets décortiqués, une explication de texte, les pièges.
Texte expliqué : Épicure, Lettre à Ménécée, 128-132, trad. Octave Hamelin (Revue de métaphysique et de morale, 18, 1910,
p. 397-440), domaine public, vérifiée sur Wikisource (pages 549-551 du fac-similé). Descartes, Discours de la méthode, III (1637).
Méthode cohérente avec le guide de l'explication du site (six éléments de l'introduction, trois gestes,
quoi / comment / pourquoi, paragraphe en cinq temps, avocat de l'auteur, conclusion en quatre temps).
"""

CODE = "bonheur-6"
NOTION = "Le bonheur"
NUM = 6
TITRE = "Le bonheur à l'épreuve du bac"
SUIVANT = "Épisode 7 · Récap"
PRONONCIATION = {"Ménécée": "Ménéssé", "Priam": "Priame", "Stockdale": "Stokdèle", "Calliclès": "Kaliklèsse",
                 "Lorenzetti": "Lorenntsetti", "Sienne": "Sienne", "Huxley": "Euksslé", "Tocqueville": "Tokvil"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_let}{q1}Juin. Huit heures. Tu retournes la feuille. Premier sujet : le bonheur est-il affaire de chance ? "
        "Deuxième : faut-il renoncer à ses désirs pour être heureux ? Et un texte d'Épicure.",
        "{-q1}{q2}Soulagement : le bonheur, tout le monde en a une idée. C'est justement le danger.",
        "{-q2}{pie0}Car sur ce sujet, trois pièges guettent. {pie0.1}Le relativisme : « chacun son bonheur », "
        "et la réflexion s'arrête là. {pie0.2}Le catalogue : Épicure dit ceci, Kant dit cela, sans jamais répondre. "
        "{pie0.3}Et la copie de développement personnel : dix conseils pour être heureux.",
        "{-pie0}{lien}La méthode générale, on l'a vue dans les séries sur la liberté et sur le devoir, à l'épisode six. "
        "Ici, on l'applique au bonheur : trois sujets décortiqués, puis l'explication d'un texte d'Épicure.",
        ("P", 0.3),
        "{-lien}{-tab_let}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_let": dict(type="tableau", img="bh6-lettre", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .55, .5],
                        legende="Johannes Vermeer, La Lettre, vers 1670-1671 (National Gallery of Ireland, Dublin)"),
        "q1": dict(type="question", t="Le bonheur est-il affaire de chance ?"),
        "q2": dict(type="question", t="Un sujet facile ? C'est justement le danger."),
        "pie0": dict(type="liste", titre="Trois pièges du sujet sur le bonheur", items=[
            "Le relativisme : « chacun son bonheur », et c'est fini",
            "Le catalogue d'auteurs, sans réponse", "Le développement personnel : dix conseils"],
                     marques=["✗", "✗", "✗"], x=170, y=170, w=940),
        "lien": dict(type="tag", style="lien", t="La méthode générale : séries « La liberté » et « Le devoir », épisode 6",
                     x=170, y=560, w=860),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 6", t="Le bonheur à l'épreuve du bac",
                      sous="Trois sujets, une explication de texte, les pièges"),
    }),

    # ------------------------------------------------------------------ I. sujet 1
    dict(id="sujet1", chap="Sujet 1 · Affaire de chance ?", fond="aube", humeur="mystere", notions=["la liberté", "la raison"],
         retenir="La chance donne les conditions du bonheur ; la sagesse décide de ce que nous en faisons.",
         beats=[
        "{tab_for}{suj1}Premier sujet : le bonheur est-il affaire de chance ?",
        "{-suj1}{mots}D'abord, les mots. {mots.1}« Affaire de » : est-ce que le bonheur dépend de la chance, relève d'elle ? "
        "{mots.2}« La chance » : ce qui arrive sans que je l'aie voulu, le hasard, la fortune. "
        "{mots.3}Et le mot bonheur lui-même, on l'a vu dans l'épisode un, vient de « bon heur » : la bonne chance.",
        "{-mots}{prob}La problématique naît d'une tension. {prob.1}Si le bonheur dépend du hasard, je n'y peux rien : "
        "il me tombe dessus, ou pas. {prob.2}Mais alors, à quoi bon toutes les sagesses qui prétendent nous apprendre à vivre ? "
        "{prob.3}Le bonheur se reçoit-il… ou se construit-il ?",
        "{-prob}{-tab_for}{tab_pri}{plan1}{plan1.1}Première partie : oui, en partie. La santé, la naissance, les rencontres ne dépendent pas de nous. "
        "Aristote lui-même le reconnaît : Priam, le roi de Troie, a vu périr ses fils et sa cité. Nul ne dirait qu'il fut heureux.",
        "{plan1.2}Deuxième partie : mais le bonheur dépend aussi de nous. Épicure trie ses désirs ; les stoïciens distinguent "
        "ce qui dépend de nous et ce qui n'en dépend pas, vu dans l'épisode trois. L'amiral américain Stockdale a tenu "
        "sept ans dans une prison du Vietnam en se répétant le Manuel d'Épictète.",
        "{plan1.3}Troisième partie : la chance donne les conditions, la sagesse en fait quelque chose. "
        "Deux personnes peuvent recevoir la même fortune, et en faire deux vies opposées.{-plan1}",
        "{-tab_pri}{tab_bene}{dist1}La distinction qui dépasse : {dist1.g}ce qui m'arrive, {dist1.d}et ce que j'en fais. "
        "C'est là que se loge notre {#la liberté}liberté. Le bonheur n'est pas un lot qu'on gagne : c'est une manière de recevoir ce qui arrive.",
        "{-dist1}{intro}Et voilà ton introduction. {intro.1}L'accroche : le gagnant du loto, et la surprise des psychologues, "
        "épisode quatre. {intro.2}L'analyse des mots, et l'étymologie. {intro.3}La problématique : se reçoit-il, ou se construit-il ? "
        "{intro.4}L'annonce du plan.",
        "{-intro}{-tab_bene}",
    ], vis={
        "tab_for": dict(type="tableau", img="bh6-fortune", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .45],
                        legende="Edward Burne-Jones, La Roue de la Fortune, 1875-1883 (musée d'Orsay)"),
        "suj1": dict(type="mot", t="« Le bonheur est-il affaire de chance ? »", g="le grand classique", y=240, taille=64),
        "mots": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« Affaire de » : dépendre de, relever de",
            "« La chance » : ce qui arrive sans que je l'aie voulu",
            "« Bonheur » : bon heur, la bonne chance (épisode 1)"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "prob": dict(type="liste", titre="Étape 2 · Problématiser", items=[
            "Si le bonheur dépend du hasard, je n'y peux rien",
            "Mais alors, à quoi bon les sagesses ?",
            "Le bonheur se reçoit-il… ou se construit-il ?"], marques=["si", "or", "?"], x=170, y=150, w=940),
        "tab_pri": dict(type="tableau", img="bh6-priam", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .5],
                        legende="Alexandre Ivanov, Priam demande à Achille le corps d'Hector, 1824 (galerie Tretiakov, Moscou)"),
        "plan1": dict(type="liste", titre="« Le bonheur est-il affaire de chance ? »", items=[
            "I. Oui, en partie : santé, naissance, rencontres (Aristote, Priam)",
            "II. Mais il dépend aussi de nous : Épicure, les stoïciens, Stockdale",
            "III. La chance donne les conditions, la sagesse en fait quelque chose"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_bene": dict(type="tableau", img="bh6-benedicite", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                         legende="Jean Siméon Chardin, Le Bénédicité, 1740 (musée du Louvre)"),
        "dist1": dict(type="cols", g="Ce qui m'arrive", gq="la chance, la fortune", d="Ce que j'en fais",
                      dq="la sagesse, la liberté", vs="≠", repere="La distinction qui dépasse"),
        "intro": dict(type="liste", titre="L'introduction en quatre temps", items=[
            "Accroche : le gagnant du loto (épisode 4)", "Analyse : les mots, l'étymologie",
            "Problématique : se reçoit-il, ou se construit-il ?", "Annonce du plan"],
                      marques=["1", "2", "3", "4"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ II. sujet 2
    dict(id="sujet2", chap="Sujet 2 · Renoncer à ses désirs ?", fond="nuit", humeur="tension", notions=["la nature", "la religion"],
         retenir="Supprimer ses désirs, c'est cesser de vivre ; les régler, c'est la sagesse. Épicure trie, Descartes change ses désirs plutôt que l'ordre du monde.",
         beats=[
        "{tab_tan}{suj2}Deuxième sujet : faut-il renoncer à ses désirs pour être heureux ? Deux mots portent tout : "
        "{!renoncer}« renoncer »… et « ses ».",
        "{-suj2}{mots2}{mots2.1}« Renoncer » : abandonner volontairement. Ce n'est pas être privé, c'est choisir de lâcher. "
        "{mots2.2}« Ses désirs » : tous ? Ou certains ? Toute la copie se joue sur cette question.",
        "{-mots2}{plan2}{plan2.1}Première partie : oui, il le faut. Le désir est un manque sans fin : les tonneaux percés de Platon, "
        "le pendule de Schopenhauer, épisode quatre. Tantale, au milieu de l'eau et des fruits, ne peut jamais les atteindre. "
        "D'où les grandes sagesses du détachement, du bouddhisme à l'ascèse chrétienne.",
        "{-tab_tan}{tab_pie}{plan2.2}Deuxième partie : mais renoncer à tout désir, c'est renoncer à vivre. Calliclès raillait déjà Socrate : "
        "à ce compte, les pierres et les morts seraient les plus heureux. Et Rousseau : malheur à qui n'a plus rien à désirer.",
        "{plan2.3}Troisième partie : il ne s'agit pas de supprimer ses désirs, mais de les régler. Épicure les trie, "
        "vu dans l'épisode deux : les désirs {#la nature}naturels et nécessaires, oui ; les désirs vains, non. Et Descartes s'en fait une règle.{-plan2}",
        "{-tab_pie}{desc}{tab_calme}",
        ("C", "Ma troisième maxime était de tâcher toujours plutôt à me vaincre que la fortune, et à changer mes désirs "
              "que l'ordre du monde…", "c_desc"),
        "{-desc}{-c_desc}{dist2}La distinction qui dépasse : {dist2.g}supprimer ses désirs, {dist2.d}ou les régler. "
        "Le sage n'est pas celui qui ne désire plus rien. C'est celui qui désire ce qui est à sa portée.",
        "{-dist2}{-tab_calme}",
    ], vis={
        "tab_tan": dict(type="tableau", img="bh6-tantale", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .35],
                        legende="Gioacchino Assereto, Tantale, vers 1640"),
        "suj2": dict(type="mot", t="« Faut-il renoncer à ses désirs pour être heureux ? »", g="deux mots portent tout",
                     y=240, taille=58),
        "mots2": dict(type="liste", titre="Étape 1 · Peser les mots", items=[
            "« Renoncer » : abandonner volontairement, choisir de lâcher",
            "« Ses désirs » : tous ? ou certains ?"], marques=["1", "2"], x=170, y=170, w=940),
        "plan2": dict(type="liste", titre="« Faut-il renoncer à ses désirs pour être heureux ? »", items=[
            "I. Oui : le désir est un manque sans fin (Platon, Schopenhauer)",
            "II. Mais ne plus rien désirer, c'est ne plus vivre (Calliclès, Rousseau)",
            "III. Non pas supprimer, mais régler ses désirs (Épicure, Descartes)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_pie": dict(type="tableau", img="bh6-pierres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .55],
                        legende="Carl Gustav Carus, Tumulus de l'âge de pierre, vers 1820 (Galerie nationale, Oslo)"),
        "desc": dict(type="portrait", annee=1596, img="descartes", nom="René Descartes", dates="1596 – 1650",
                     legende="Discours de la méthode (1637)", x=110, y=120, w=330, h=420),
        "tab_calme": dict(type="tableau", img="bh6-calme", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .45],
                          legende="Willem van de Velde le Jeune, Navires par mer calme, vers 1665 (Rijksmuseum, Amsterdam)"),
        "c_desc": dict(type="cit", a="Descartes", o="Discours de la méthode, IIIᵉ partie (1637)", x=640, y=180, w=570),
        "dist2": dict(type="cols", g="Supprimer ses désirs", gq="cesser de vivre : les pierres seraient heureuses",
                      d="Régler ses désirs", dq="désirer ce qui est à sa portée", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ III. sujet 3
    dict(id="sujet3", chap="Sujet 3 · L'État et le bonheur", fond="aube", humeur="lumiere", notions=["l'État", "la justice", "la liberté"],
         retenir="« Faire » le bonheur des citoyens : le despotisme, même doux. En garantir les conditions : la justice.",
         beats=[
        "{tab_lor}{suj3}Troisième sujet : l'État doit-il faire le bonheur des citoyens ? Ici, le verbe décide de tout : {!faire}« faire ».",
        "{-suj3}{plan3}{plan3.1}Première partie : oui, c'est même sa raison d'être. Pour Aristote, la cité existe en vue de la vie bonne. "
        "En 1793, la Déclaration des droits l'écrit : le but de la société est le bonheur commun. Regarde cette fresque de Sienne : "
        "le bon gouvernement, c'est une ville où l'on danse, où l'on construit, où l'on commerce.",
        "{plan3.2}Deuxième partie : mais l'{#l'État}État ne peut ni ne doit faire notre bonheur à notre place. Le bonheur est indéterminé, "
        "dit Kant, et le gouvernement paternel est le pire des despotismes. Tocqueville, Huxley : un bonheur imposé fait un troupeau.",
        "{plan3.3}Troisième partie : l'État doit garantir les conditions du bonheur, non le bonheur lui-même. "
        "La sécurité, la justice, l'éducation, la santé, les libertés : de quoi chercher, chacun, sa propre vie heureuse.{-plan3}",
        "{-tab_lor}{tab_dec}{dist3}La distinction qui dépasse, vue dans l'épisode cinq : {dist3.g}faire le bonheur des citoyens, "
        "{dist3.d}ou rendre possible leur recherche du bonheur. C'est toute la différence entre un tuteur et un garant.",
        "{-dist3}{cp3}Note la méthode : dans les trois sujets, la troisième partie ne dit jamais « tout dépend ». "
        "Elle déplace la question, grâce à une distinction.",
        "{-cp3}{-tab_dec}",
    ], vis={
        "tab_lor": dict(type="tableau", img="bh6-lorenzetti", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.25, .6, .55],
                        legende="Ambrogio Lorenzetti, Les Effets du bon gouvernement dans la ville, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "suj3": dict(type="mot", t="« L'État doit-il faire le bonheur des citoyens ? »", g="le verbe décide de tout",
                     y=240, taille=60),
        "plan3": dict(type="liste", titre="« L'État doit-il faire le bonheur des citoyens ? »", items=[
            "I. Oui : sa raison d'être (Aristote, la Déclaration de 1793)",
            "II. Mais pas à notre place : Kant, Tocqueville, Huxley",
            "III. Garantir les conditions du bonheur, non le bonheur"], marques=["I", "II", "III"], x=170, y=130, w=940),
        "tab_dec": dict(type="tableau", img="bh4-declaration", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="John Trumbull, La Déclaration d'indépendance, 1819 (Capitole des États-Unis, Washington)"),
        "dist3": dict(type="cols", g="Faire le bonheur", gq="à la place des citoyens : un tuteur", d="Rendre possible sa recherche",
                      dq="garantir les conditions : un garant", vs="≠", repere="La distinction qui dépasse"),
        "cp3": dict(type="tag", style="copie", t="Copie · la partie III déplace la question, elle ne dit pas « tout dépend »",
                    x=170, y=560, w=900),
    }),

    # ------------------------------------------------------------------ IV. explication : le texte et l'introduction
    dict(id="texte", chap="L'explication · Le texte", fond="nuit", humeur="calme", notions=["la nature", "la raison"],
         retenir="Introduction : thème, question, thèse adverse, thèse, enjeu, plan. Toujours avec les lignes du texte.",
         beats=[
        "{epic}{tab_jar}Et si tu choisis l'explication de texte ? Voici un texte possible : Épicure, Lettre à Ménécée, "
        "dans la traduction d'Octave Hamelin. Écoute-le, par morceaux.",
        "{-epic}",
        ("C", "C'est pourquoi nous disons que le plaisir est le commencement et la fin de la vie heureuse.", "c_t1"),
        "{-c_t1}Puis Épicure précise : on ne recherche pas tout plaisir.",
        ("C", "Mais, précisément parce que le plaisir est le bien primitif et naturel, nous ne recherchons pas tout plaisir, "
              "et il y a des cas où nous passons par-dessus beaucoup de plaisirs, savoir lorsqu'ils doivent avoir pour suite "
              "des peines qui les surpassent…", "c_t2"),
        "{-c_t2}Et il écarte un contresens.",
        ("C", "Lors donc que nous disons que le plaisir est la fin de la vie, nous ne parlons pas des plaisirs de l'homme déréglé, "
              "ni de ceux qui consistent dans les jouissances…", "c_t3"),
        ("C", "Le plaisir dont nous parlons est celui qui consiste, pour le corps, à ne pas souffrir et, pour l'âme, "
              "à être sans trouble.", "c_t4"),
        "{-c_t4}{-tab_jar}{tab_era}{six}Au brouillon, on cherche les six éléments de l'introduction. "
        "{six.1}Le thème : le plaisir et la vie heureuse. {six.2}La question : le plaisir est-il le but de la vie heureuse ? "
        "{six.3}La thèse adverse, ce qu'on penserait spontanément : être heureux, ce serait jouir le plus possible, "
        "ou au contraire fuir les plaisirs pour être sage.",
        "{six.4}La thèse d'Épicure : le plaisir est bien le principe et la fin de la vie heureuse, car il est notre bien {#la nature}naturel ; "
        "mais c'est l'absence de douleur et de trouble, qu'on obtient en calculant, non en jouissant de tout. "
        "{six.5}L'enjeu : fonder une sagesse sur le plaisir, sans tomber dans la débauche. "
        "{six.6}Le plan : le plaisir comme principe ; le calcul des plaisirs ; le contresens écarté.",
        "{-six}{-tab_era}",
    ], vis={
        "epic": dict(type="portrait", annee=-341, img="epicure", nom="Épicure", dates="341 – 270 av. J.-C.",
                     legende="Lettre à Ménécée (vers 300 av. J.-C.)", x=110, y=120, w=330, h=420),
        "tab_jar": dict(type="tableau", img="bh6-calme", fond=True, sombre=True, de=[1.25, .6, .4], a=[1.0, .5, .5],
                        legende="Willem van de Velde le Jeune, Navires par mer calme, vers 1665 (Rijksmuseum, Amsterdam)"),
        "c_t1": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 128-129, trad. Octave Hamelin (1910)", x=170, y=200, w=940),
        "c_t2": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 129, trad. Hamelin", x=170, y=150, w=940),
        "c_t3": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 131, trad. Hamelin", x=170, y=160, w=940),
        "c_t4": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 131, trad. Hamelin", x=170, y=200, w=940),
        "tab_era": dict(type="tableau", img="bh6-erasme", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .6],
                        legende="Hans Holbein le Jeune, Érasme écrivant, 1523 (musée du Louvre)"),
        "six": dict(type="liste", titre="Les six éléments de l'introduction", items=[
            "Thème : le plaisir et la vie heureuse",
            "Question : le plaisir est-il le but de la vie heureuse ?",
            "Thèse adverse : jouir de tout… ou fuir tout plaisir",
            "Thèse : oui, mais le plaisir, c'est l'absence de douleur et de trouble",
            "Enjeu : une sagesse du plaisir, sans débauche",
            "Plan : le principe · le calcul · le contresens écarté"],
                    marques=["1", "2", "3", "4", "5", "6"], cles=["thèse adverse"], x=170, y=90, w=940),
    }),

    # ------------------------------------------------------------------ V. explication : le développement
    dict(id="developpement", chap="L'explication · Phrase par phrase", fond="aube", humeur="calme",
         notions=["la raison", "la vérité"],
         retenir="Pour chaque phrase : quoi, comment, pourquoi. Trois gestes : reformuler, définir, illustrer. Discuter en avocat de l'auteur.",
         beats=[
        "{tab_roi}{qcp}Puis, phrase par phrase, un tableau : la citation, et trois colonnes. Prenons la phrase charnière : "
        "« Lors donc que nous disons que le plaisir est la fin de la vie, nous ne parlons pas des plaisirs de l'homme déréglé. » "
        "{qcp.1}Quoi ? Épicure écarte une mauvaise lecture de sa doctrine.",
        "{qcp.2}Comment ? Par un connecteur de conclusion, « lors donc », une négation, et la désignation des adversaires : "
        "ceux qui ignorent sa doctrine, ou qui la combattent. {qcp.3}Pourquoi ? Pour défendre son école contre la calomnie, "
        "et préparer la vraie définition du plaisir.",
        "{-qcp}{-tab_roi}{tab_bene2}{ges}Pour expliquer, trois gestes. {ges.1}Reformuler : autrement dit, le plaisir du sage n'est pas l'excès. "
        "{ges.2}Définir : par « être sans trouble », il faut entendre l'ataraxie, la paix de l'âme ; et ne pas souffrir, "
        "l'aponie, la paix du corps. {ges.3}Illustrer : c'est ainsi que l'élève qui renonce à une fête la veille de l'épreuve "
        "passe par-dessus un plaisir, pour éviter une peine plus grande.",
        "{-ges}{cinq}Chaque paragraphe suit cinq temps : {cinq.1}annoncer ce que fait le texte, {cinq.2}citer, "
        "{cinq.3}expliquer, {cinq.4}interroger, {cinq.5}et relier à la thèse.",
        "{-cinq}{-tab_bene2}{tab_bou}{av}Enfin, interroge le texte, mais en avocat de l'auteur. {av.1}Objection : un bonheur qui consiste "
        "à ne pas souffrir, n'est-ce pas un bonheur bien pauvre ? Celui d'une pierre, disait Calliclès. "
        "{av.2}Réponse : Épicure ne condamne pas les plaisirs raffinés ; il dit qu'on les goûte mieux après une vie frugale. "
        "Et la paix de l'âme n'est pas un vide : c'est, dit-il, le fruit d'un entendement sobre et sain, d'une {#la raison}raison "
        "qui chasse les opinions fausses.",
        "{-av}{-tab_bou}{tab_can}{conc}Pour conclure, quatre temps. {conc.1}Le bilan : Épicure fait du plaisir le but de la vie, "
        "mais un plaisir mesuré, calculé, paisible. {conc.2}La réponse à la question : oui, le plaisir est la fin de la vie heureuse, "
        "à condition de bien l'entendre. {conc.3}L'intérêt du texte : il défait le préjugé de l'épicurien jouisseur. "
        "{conc.4}Et, si tu veux, une ouverture : Mill et la qualité des plaisirs, vue dans l'épisode deux.",
        "{-conc}{-tab_can}{tab_rb}{pie}Trois pièges à éviter. {pie.1}Réciter tout Épicure, les dieux et l'atome, en oubliant le texte. "
        "{pie.2}La paraphrase : répéter Épicure avec d'autres mots. {pie.3}Et les deux contresens : faire d'Épicure un jouisseur… "
        "ou un ascète qui condamne le plaisir. Il n'est ni l'un ni l'autre.",
        ("Le plaisir est le but. Mais le chemin passe par la raison. C'est tout le texte.", {"rate": "-5%"}),
        "{-pie}{-tab_rb}",
    ], vis={
        "tab_roi": dict(type="tableau", img="bh6-roiboit", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .4],
                        legende="Jacob Jordaens, Le Roi boit, vers 1638-1640 (musée du Louvre)"),
        "qcp": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Quoi ?", q="écarter une mauvaise lecture de la doctrine"),
            dict(ic="chemins", t="Comment ?", q="« lors donc » · négation · les adversaires nommés"),
            dict(ic="colonnes", t="Pourquoi ?", q="défendre l'école, préparer la définition")]),
        "tab_bene2": dict(type="tableau", img="bh6-benedicite", fond=True, sombre=True, de=[1.3, .4, .45], a=[1.05, .5, .5],
                          legende="Jean Siméon Chardin, Le Bénédicité, 1740 (musée du Louvre)"),
        "ges": dict(type="liste", titre="Expliquer une phrase : trois gestes", items=[
            "Reformuler · « autrement dit » : le plaisir du sage n'est pas l'excès",
            "Définir · « par… il faut entendre » : ataraxie, aponie",
            "Illustrer · « c'est ainsi que » : renoncer à la fête la veille de l'épreuve"], marques=["1", "2", "3"],
                    x=170, y=150, w=940),
        "cinq": dict(type="liste", titre="Un paragraphe en cinq temps", items=[
            "Annoncer ce que fait le texte", "Citer", "Expliquer", "Interroger", "Relier à la thèse"],
                     marques=["1", "2", "3", "4", "5"], x=170, y=110, w=940),
        "tab_bou": dict(type="tableau", img="bh6-bouddha", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.2, .5, .35],
                        legende="Bouddha assis en méditation, Gandhara, IIᵉ-IIIᵉ s., musée Georges-Labit, Toulouse (photo Didier Descouens, domaine public)"),
        "av": dict(type="liste", titre="Discuter en avocat de l'auteur", items=[
            "Objection : ne pas souffrir, un bonheur bien pauvre ?",
            "Réponse : les plaisirs raffinés ne sont pas condamnés ; la paix de l'âme vient de la raison"],
                   marques=["?", "→"], x=170, y=170, w=940),
        "tab_can": dict(type="tableau", img="bh6-canotiers", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .45],
                        legende="Pierre-Auguste Renoir, Le Déjeuner des canotiers, 1880-1881 (Phillips Collection, Washington)"),
        "conc": dict(type="liste", titre="La conclusion en quatre temps", items=[
            "Bilan : un plaisir mesuré, calculé, paisible", "Réponse : oui, le plaisir est la fin, bien entendu",
            "Intérêt : défaire le préjugé de l'épicurien jouisseur", "Ouverture : Mill et la qualité des plaisirs"],
                     marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "tab_rb": dict(type="tableau", img="bh6-roiboit", fond=True, sombre=True, de=[1.3, .6, .4], a=[1.05, .5, .5],
                       legende="Jacob Jordaens, Le Roi boit, vers 1638-1640 (musée du Louvre)"),
        "pie": dict(type="liste", titre="Trois pièges", items=[
            "Réciter tout Épicure en oubliant le texte", "Paraphraser",
            "Le double contresens : ni jouisseur, ni ascète"], marques=["✗", "✗", "✗"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : chaque sujet se joue sur un mot. Affaire de. Renoncer, et ses. Faire.",
        "{rec.2}Deux : trois distinctions qui dépassent le problème. Ce qui m'arrive, et ce que j'en fais. Supprimer ses désirs, "
        "ou les régler. Faire le bonheur des citoyens, ou en garantir les conditions.",
        "{rec.3}Trois : des exemples travaillés. Priam, Stockdale, Tantale, la fresque de Sienne, le gagnant du loto.",
        "{rec.4}Quatre : l'explication d'Épicure. Six éléments d'introduction, puis quoi, comment, pourquoi, en avocat de l'auteur.",
        "{-rec}{tab_fin}{q_fin}À toi : choisis l'un des trois sujets, et fais-en le plan en vingt minutes. "
        "Les questions t'attendent sous la vidéo.",
        "{-q_fin}{fin}",
        ("La prochaine fois : le récapitulatif de toute la série.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE BONHEUR AU BAC", branches=[
            dict(t="Lire le sujet", items=["affaire de · renoncer · faire", "un mot porte tout"]),
            dict(t="Dépasser", items=["ce qui m'arrive / ce que j'en fais", "supprimer / régler ses désirs", "faire / rendre possible"]),
            dict(t="Exemples", items=["Priam, Stockdale", "Tantale, les pierres", "la fresque de Sienne"]),
            dict(t="Expliquer Épicure", items=["six éléments", "quoi, comment, pourquoi", "ni jouisseur, ni ascète"])]),
        "tab_fin": dict(type="tableau", img="bh6-couchant", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .6, .45],
                        legende="Claude Lorrain, Port de mer au soleil couchant, 1639 (musée du Louvre)"),
        "q_fin": dict(type="question", t="Un sujet, un plan, vingt minutes."),
        "fin": dict(type="titre", sur="À suivre", t="Récap", sous="Épisode 7 · Toute la série en un épisode"),
    }),
]

QUIZ = [
    dict(q="Dans « Le bonheur est-il affaire de chance ? », quelle distinction permet de dépasser le problème ?",
         r=["Plaisir / douleur", "Ce qui m'arrive / ce que j'en fais", "Légal / légitime", "Corps / âme"], ok=1,
         voir="dist1", ex="La chance donne les conditions ; la sagesse décide de ce que nous en faisons. C'est là que se loge notre liberté."),
    dict(q="Pourquoi Priam est-il un bon exemple pour la première partie ?",
         r=["Parce qu'il est un sage stoïcien", "Parce que ses malheurs, qui ne dépendaient pas de lui, empêchent de le dire heureux",
            "Parce qu'il a gagné la guerre", "Parce qu'il a renoncé à ses désirs"], ok=1,
         voir="plan1", ex="Aristote le reconnaît : sans un minimum de biens extérieurs et de chance, on ne peut pas dire qu'une vie est heureuse."),
    dict(q="Dans « Faut-il renoncer à ses désirs pour être heureux ? », quel petit mot est décisif ?",
         r=["« pour »", "« ses » : tous les désirs, ou certains ?", "« être »", "« il »"], ok=1,
         voir="mots2", ex="Renoncer à tous ses désirs, c'est cesser de vivre ; à certains, c'est la sagesse d'Épicure."),
    dict(q="« Changer mes désirs plutôt que l'ordre du monde » : de qui est cette maxime ?",
         r=["Épicure", "Descartes", "Kant", "Rousseau"], ok=1,
         voir="c_desc", ex="Discours de la méthode, IIIᵉ partie (1637) : la troisième maxime de la morale par provision."),
    dict(q="Dans « L'État doit-il faire le bonheur des citoyens ? », sur quel verbe faut-il insister ?",
         r=["« doit »", "« faire » : à leur place, ou rendre possible ?", "« être »", "Aucun"], ok=1,
         voir="dist3", ex="Faire le bonheur à la place des citoyens, c'est le despotisme, même doux ; en garantir les conditions, c'est la justice."),
    dict(q="Pour Épicure, le plaisir qui est la fin de la vie heureuse, c'est…",
         r=["la jouissance de l'homme déréglé", "pour le corps, ne pas souffrir ; pour l'âme, être sans trouble",
            "la contemplation de Dieu", "la gloire et la richesse"], ok=1,
         voir="c_t4", ex="Lettre à Ménécée, 131 : l'aponie (pas de douleur du corps) et l'ataraxie (pas de trouble de l'âme)."),
    dict(q="Dans l'explication, quelle est la thèse adverse ?",
         r=["Le plaisir est la fin de la vie heureuse", "Être heureux, ce serait jouir de tout… ou fuir tout plaisir",
            "La prudence est le plus grand des biens", "Les dieux sont heureux"], ok=1,
         voir="six", ex="Ce qu'on penserait spontanément ; Épicure montre que le plaisir bien compris est mesuré, calculé, paisible."),
    dict(q="Quel double contresens éviter sur Épicure ?",
         r=["En faire un athée ou un croyant", "En faire un jouisseur… ou un ascète qui condamne le plaisir",
            "En faire un Grec ou un Romain", "En faire un stoïcien ou un sceptique"], ok=1,
         voir="pie", ex="Il ne cherche ni l'excès ni la privation : il calcule les plaisirs pour atteindre la paix du corps et de l'âme."),
]

CREDITS = [
    "Portraits : Épicure (buste antique, domaine public) ; Descartes (d'après Frans Hals, XVIIᵉ s.)",
    "Tableaux : Johannes Vermeer, La Lettre (vers 1670-1671) ; Edward Burne-Jones, La Roue de la Fortune (1875-1883) ; "
    "Alexandre Ivanov, Priam demande à Achille le corps d'Hector (1824) ; Jean Siméon Chardin, Le Bénédicité (1740) ; "
    "Gioacchino Assereto, Tantale (vers 1640) ; Carl Gustav Carus, Tumulus de l'âge de pierre (vers 1820) ; "
    "Willem van de Velde le Jeune, Navires par mer calme (vers 1665) ; Ambrogio Lorenzetti, Les Effets du bon gouvernement (1338-1339) ; "
    "John Trumbull, La Déclaration d'indépendance (1819) ; Hans Holbein le Jeune, Érasme écrivant (1523) ; "
    "Jacob Jordaens, Le Roi boit (vers 1638-1640) ; Pierre-Auguste Renoir, Le Déjeuner des canotiers (1880-1881) ; "
    "Claude Lorrain, Port de mer au soleil couchant (1639) : domaine public",
    "Photographie : Bouddha du Gandhara, musée Georges-Labit, Toulouse (Didier Descouens, domaine public)",
    "Texte expliqué : Épicure, Lettre à Ménécée, 128-131, trad. Octave Hamelin, Revue de métaphysique et de morale, 18 (1910), Wikisource. "
    "Descartes, Discours de la méthode, IIIᵉ partie (1637).",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
