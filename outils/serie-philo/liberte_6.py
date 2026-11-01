"""La liberté, épisode 6 : « La liberté à l'épreuve du bac »

Même format que liberte_1.py (voir l'en-tête de ce fichier) : beats lus, repères {id} / {-id} / {id.k} / {!mot},
citations ("C", texte, id), visuels par scène. Méthode cohérente avec la page Méthode et le guide de l'explication
de texte du site (introduction en six éléments ; plans types de la dissertation).
"""

CODE = "liberte-6"
NOTION = "La liberté"
NUM = 6
TITRE = "La liberté à l'épreuve du bac"
SUIVANT = "Épisode 7 · Récap"

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_exa}Juin. Huit heures du matin. Une salle d'examen, des rangées de tables, et sur chacune… "
        "{sujets}une feuille avec trois sujets. {sujets.1}Deux dissertations. {sujets.2}Une explication de texte. "
        "{sujets.3}Tu en choisis un seul. Tu as {!quatre heures}quatre heures.",
        "{-sujets}{-tab_exa}{tab_sab}{q_rec}Tu as vu cinq épisodes. Des dizaines d'auteurs, de citations, de distinctions. "
        "Et la tentation est immense : tout raconter. Tout ce que tu sais sur la liberté, dans l'ordre où tu l'as appris.",
        ("C'est exactement ce qu'il ne faut pas faire.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-q_rec}{reg}Le correcteur ne note pas ce que tu sais. {reg.1}Il note ce que tu en fais : "
        "{reg.2}comment tu poses un problème, {reg.3}comment tu le traites, avec des arguments, des auteurs, des exemples.",
        "{-reg}Dans cet épisode, on passe à l'atelier. Trois sujets décortiqués, une explication de texte, "
        "et les pièges à éviter.",
        ("P", 0.3),
        "{-tab_sab}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "sujets": dict(type="cartes", items=[
            dict(ic="chemins", t="Dissertation 1", q="un sujet, une question"),
            dict(ic="chemins", t="Dissertation 2", q="un autre sujet"),
            dict(ic="porte", t="Explication", q="un texte d'auteur")]),
        "tab_sab": dict(type="tableau", img="t6-sablier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .4],
                        legende="Adriaen Coorte, Vanité au sablier, fin du XVIIᵉ siècle"),
        "q_rec": dict(type="question", t="Tout raconter ?"),
        "reg": dict(type="liste", titre="Ce que note le correcteur", items=[
            "Pas ce que tu sais, mais ce que tu en fais", "Poser un problème", "Le traiter : arguments, auteurs, exemples"],
                    marques=["✎", "1", "2"], x=170, y=170, w=940),
        "titre": dict(type="titre", sur="La liberté · Épisode 6", t="La liberté à l'épreuve du bac",
                      sous="Analyser, problématiser, construire, expliquer"),
    }),

    # ------------------------------------------------------------------ I. lire le sujet
    dict(id="analyse", chap="Lire le sujet", fond="aube", humeur="calme",
         retenir="Analyser le sujet : définir chaque mot, repérer le présupposé, faire apparaître une tension.", beats=[
        "{tab_jer}{suj1}Prenons le sujet le plus classique : être libre, est-ce faire ce que l'on veut ? "
        "Avant d'écrire une ligne, on prend une demi-heure pour le lire. Vraiment le lire.",
        "{-suj1}{def_mots}Étape un : définir chaque mot. {def_mots.1}« Être libre » : de quelle liberté parle-t-on ? "
        "D'agir, de vouloir, politique ? Ici, c'est surtout la liberté d'agir… et celle de vouloir. "
        "{def_mots.2}« Faire » : agir, passer à l'acte, dans le monde. {def_mots.3}« Ce que l'on veut » : "
        "est-ce mon désir du moment, ou ma volonté réfléchie ? Ce n'est pas du tout la même chose.",
        "{-def_mots}{pres}Étape deux : repérer le présupposé, ce que la question tient pour acquis. "
        "{pres.1}Ici, elle suppose que je sais ce que je veux, et que ce vouloir vient bien de moi. "
        "C'est précisément ce qu'on peut mettre en doute.",
        "{-pres}{-tab_jer}{tab_ari}{prob}Étape trois : problématiser. Attention, {!problématiser}problématiser, "
        "ce n'est pas recopier la question en ajoutant « nous allons nous demander si ». "
        "{prob.1}C'est montrer que la réponse évidente se heurte à un fait qui la contredit.",
        "{-prob}{prob_ex}Par exemple : {prob_ex.1}si être libre, c'est n'être empêché par rien, alors celui qui suit tous ses désirs "
        "devrait être le plus libre des hommes. {prob_ex.2}Pourtant, nous disons de lui qu'il est esclave : de sa colère, "
        "de son téléphone, de ses envies. {prob_ex.3}D'où la vraie question : peut-on faire ce qu'on veut… sans être libre ?",
        ("La problématique, c'est ton fil d'Ariane. Elle te guide jusqu'à la sortie du labyrinthe.", {"rate": "-4%"}),
        "{-prob_ex}{redac}{redac.1}Côté temps, compte environ une heure et demie de brouillon, deux heures de rédaction, "
        "et un quart d'heure pour relire. {redac.2}L'introduction suit quatre temps : une accroche concrète, l'analyse des termes, "
        "la problématique, l'annonce du plan. {redac.3}La conclusion en trois : le bilan, une réponse nette à la question, "
        "et, si tu veux, une ouverture.",
        ("P", 0.5),
    ], vis={
        "redac": dict(type="liste", titre="La dissertation, en pratique", items=[
            "≈ 1 h 30 de brouillon · 2 h de rédaction · 15 min de relecture",
            "Introduction : accroche › analyse › problématique › plan",
            "Conclusion : bilan › réponse nette › ouverture"], marques=["⧗", "1", "2"], x=170, y=170, w=940),
        "tab_jer": dict(type="tableau", img="t6-jerome", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Albrecht Dürer, Saint Jérôme dans son cabinet de travail, 1514 (Met, CC0)"),
        "suj1": dict(type="mot", t="« Être libre, est-ce faire ce que l'on veut ? »", g="le sujet le plus classique",
                     y=240, taille=64),
        "def_mots": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« Être libre » : d'agir ? de vouloir ? politique ?",
            "« Faire » : agir, passer à l'acte",
            "« Ce que l'on veut » : mon désir du moment, ou ma volonté réfléchie ?"],
                         marques=["1", "2", "3"], x=170, y=150, w=940),
        "pres": dict(type="def", cles=["acquis", "doute"], terme="Étape 2 · Le présupposé",
                     t="Ce que la question tient pour acquis : que je sais ce que je veux, et que ce vouloir vient de moi.",
                     etape="C'est justement ce qu'on peut mettre en doute.", x=170, y=200, w=940),
        "tab_ari": dict(type="tableau", img="t6-ariane", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .45, .35],
                        legende="Johann Heinrich Tischbein, Ariane donnant le fil à Thésée, 1779"),
        "prob": dict(type="def", cles=["recopier", "contredit"], terme="Étape 3 · Problématiser",
                     t="Ce n'est pas recopier la question : c'est montrer que la réponse évidente se heurte à un fait qui la contredit.",
                     etape="D'un côté… mais de l'autre… : une tension, et les deux côtés semblent vrais.", x=170, y=190, w=940),
        "prob_ex": dict(type="liste", titre="Exemple de problématique", items=[
            "Si être libre, c'est n'être empêché par rien, celui qui suit tous ses désirs est le plus libre…",
            "… pourtant on le dit esclave : de sa colère, de son téléphone",
            "Peut-on faire ce qu'on veut… sans être libre ?"], marques=["si", "or", "?"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ II. sujet 1
    dict(id="sujet1", chap="Sujet 1 · Faire ce que l'on veut", fond="nuit", humeur="lumiere",
         retenir="Plan dialectique : la réponse spontanée, l'objection, puis une distinction qui dépasse les deux.", beats=[
        "{tab_ten}{plan1}Maintenant, le plan. Un plan, c'est une carte : il montre au correcteur où tu l'emmènes. Pour un sujet en « est-ce que », le plan dialectique marche presque toujours. "
        "Trois parties qui se répondent.",
        "{-tab_ten}{plan1.1}{tab_pri}Première partie : oui, être libre, c'est d'abord faire ce que l'on veut. Ne caricature pas cette réponse : "
        "prends-la au sérieux. C'est la définition de Hobbes, l'absence d'obstacles. Exemple : le prisonnier, justement, "
        "ne peut pas faire ce qu'il veut.",
        "{-tab_pri}{tab_dan}{plan1.2}Deuxième partie : mais faire ce que l'on veut peut être une servitude. Les tonneaux percés "
        "de Platon. L'impulsion du seul appétit, dit Rousseau, est esclavage. Et Spinoza ajoute : nous ignorons les causes de nos désirs. "
        "Exemple : la vidéo suivante qui se lance toute seule.",
        "{-tab_dan}{tab_uly}{plan1.3}Troisième partie : le dépassement. Pas un compromis mou, « un peu des deux ». "
        "On introduit une distinction : {-plan1}{dist}{dist.g}la liberté comme indépendance, faire ce que je veux, "
        "{dist.d}et la liberté comme autonomie, obéir à la loi que je me suis donnée. Rousseau, puis Kant.",
        "{-dist}{uly}Et voici l'exemple qui fait mouche : Ulysse et les sirènes. Il sait que leur chant va le rendre fou. "
        "{uly.1}Alors il se fait attacher au mât, {uly.2}et ordonne à ses marins de ne pas le détacher, quoi qu'il dise.",
        ("Ligoté… et pourtant plus libre que s'il avait suivi son envie. Parce que c'est lui qui a choisi sa règle.",
         {"rate": "-5%"}),
        "{rep_auto}Note la méthode : la troisième partie ne dit jamais « tout dépend ». "
        "Elle déplace la question, grâce à une distinction nouvelle.",
        ("P", 0.5),
    ], vis={
        "plan1": dict(type="liste", titre="« Être libre, est-ce faire ce que l'on veut ? »", items=[
            "I. Oui : n'être pas empêché (Hobbes · le prisonnier)",
            "II. Mais l'esclave de ses désirs n'est pas libre (Platon, Rousseau, Spinoza)",
            "III. Être libre, c'est être autonome (Rousseau, Kant · Ulysse)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_ten": dict(type="tableau", img="t6-tendre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="François Chauveau, la Carte de Tendre, 1654"),
        "tab_pri": dict(type="tableau", img="t-prisonniers", fond=True, sombre=True, de=[1.0, 0.5, 0.5], a=[1.3, 0.5, 0.62],
                        legende="Vincent van Gogh, La Ronde des prisonniers, 1890"),
        "tab_dan": dict(type="tableau", img="t-danaides", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.25, .5, .6],
                        legende="John William Waterhouse, Les Danaïdes, 1906"),
        "tab_uly": dict(type="tableau", img="t6-ulysse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .6, .4],
                        legende="John William Waterhouse, Ulysse et les sirènes, 1891"),
        "dist": dict(type="cols", g="Indépendance", gq="faire ce que je veux", d="Autonomie",
                     dq="obéir à la loi que je me suis donnée", vs="→", repere="La distinction qui dépasse"),
        "uly": dict(type="liste", titre="L'exemple · Ulysse (Odyssée, XII)", items=[
            "Il se fait attacher au mât", "« Ne me détachez pas, quoi que je dise »"], marques=["1", "2"],
                    x=170, y=200, w=940),
        "rep_auto": dict(type="tag", style="copie", t="Copie · la partie III déplace la question, elle ne dit pas « tout dépend »",
                         x=170, y=540, w=900),
    }),

    # ------------------------------------------------------------------ III. sujet 2
    dict(id="sujet2", chap="Sujet 2 · Une illusion ?", fond="aube", humeur="mystere",
         retenir="Travailler le mot du sujet : une illusion n'est pas une simple erreur, elle naît d'un désir.", beats=[
        "{tab_cav}{suj2}Deuxième sujet : la liberté est-elle une illusion ? Ici, tout se joue sur un mot : {!illusion}illusion.",
        "{-suj2}{ill}Une illusion, ce n'est pas une simple erreur. {ill.g}L'erreur se corrige quand on la voit. "
        "{ill.d}L'illusion, elle, persiste même quand on la connaît, parce qu'elle répond à un désir. "
        "Freud le dit dans L'Avenir d'une illusion : ce qui caractérise l'illusion, c'est qu'elle dérive de nos souhaits.",
        "{-ill}{plan2}D'où un plan. {plan2.1}Un : la liberté semble une évidence vécue. Descartes : elle se connaît sans preuve. "
        "Sartre : je suis condamné à être libre.",
        "{plan2.2}Deux : mais ce sentiment peut tromper. La pierre de Spinoza, l'inconscient de Freud, l'habitus de Bourdieu.",
        "{plan2.3}Trois : et si la liberté n'était ni une illusion, ni un fait donné… mais une conquête ? Les stoïciens, Spinoza "
        "encore, Kant : on n'est pas libre, on le devient.",
        "{-plan2}{-tab_cav}{fum}Et prends un exemple concret, toujours : {fum.1}le fumeur qui veut arrêter, et qui rallume pourtant "
        "une cigarette. {fum.2}Il se sent libre de fumer… mais est-ce lui qui veut, ou l'habitude ? C'est tout le sujet, en une scène.",
        "{-fum}{rep2}Ici, la distinction qui dépasse oppose deux sens : {rep2.g}le libre arbitre, pouvoir de choisir "
        "sans cause, peut-être illusoire, {rep2.d}et la libération, travail réel sur soi.",
        ("P", 0.5),
    ], vis={
        "tab_cav": dict(type="tableau", img="t6-caverne", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Jan Saenredam, d'après Cornelis van Haarlem, L'Allégorie de la caverne, 1604"),
        "suj2": dict(type="mot", t="« La liberté est-elle une illusion ? »", g="tout se joue sur un mot", y=240, taille=70),
        "ill": dict(type="cols", g="Une erreur", gq="se corrige quand on la voit", d="Une illusion",
                    dq="persiste même connue : elle répond à un désir (Freud, 1927)", vs="≠"),
        "plan2": dict(type="liste", titre="« La liberté est-elle une illusion ? »", items=[
            "I. Une évidence vécue (Descartes, Sartre)",
            "II. Un sentiment qui peut tromper (Spinoza, Freud, Bourdieu)",
            "III. Ni illusion ni fait : une conquête (stoïciens, Spinoza, Kant)"], marques=["I", "II", "III"],
                      x=170, y=150, w=940),
        "fum": dict(type="liste", titre="Un exemple qui fait penser", items=[
            "Le fumeur qui veut arrêter… et rallume une cigarette",
            "Il se sent libre de fumer : est-ce lui qui veut, ou l'habitude ?"], marques=["1", "?"], x=170, y=200, w=940),
        "rep2": dict(type="cols", g="Libre arbitre", gq="choisir sans cause : peut-être une illusion", d="Libération",
                     dq="un travail réel sur soi", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ IV. sujet 3
    dict(id="sujet3", chap="Sujet 3 · Libre sans les autres ?", fond="nuit", humeur="lumiere",
         retenir="Un exemple travaillé (Robinson) vaut mieux que dix citations. Et vérifie toujours tes citations.", beats=[
        "{tab_rob}{suj3}Troisième sujet : peut-on être libre sans les autres ? Il te faut un exemple qui fasse penser. "
        "Le voici : {!Robinson}Robinson Crusoé, seul sur son île.",
        "{-suj3}{plan3}{plan3.1}Première partie : oui, et même plus libre. Personne pour lui donner d'ordre, aucune loi, aucun regard. "
        "Les autres semblent être des limites.",
        "{plan3.2}{-tab_rob}{tab_lev}Deuxième partie : mais cette liberté est fragile, et peut-être trompeuse. Sans loi commune, dit Hobbes, "
        "chacun est menacé par chacun. Et regarde Robinson : il survit avec les outils, la langue, les savoirs… des autres, "
        "sauvés du naufrage. Locke a cette formule.{-plan3}",
        ("C", "Là où il n'y a pas de loi, il n'y a pas de liberté.", "c_locke"),
        "{-c_locke}{-tab_lev}{tab_rob2}{p3}{plan3.3}Troisième partie : la liberté se construit avec les autres. La liberté civile de Rousseau, "
        "les droits garantis par la loi, l'éducation. {p3.1}Kant le dit : l'homme ne peut devenir homme que par l'éducation.",
        "Et ta conclusion répondrait nettement : seul, on peut être indépendant. Mais on n'est libre, au sens plein, "
        "qu'avec les autres et par eux.",
        "{-p3}{-tab_rob2}{tab_ddhc}{piege}Et attention à deux pièges de citation. {piege.1}« Ma liberté s'arrête là où commence celle des autres » : "
        "aucun philosophe ne l'a écrit sous cette forme. La Déclaration de 1789 dit autre chose : pouvoir faire tout ce qui ne nuit pas à autrui. "
        "{piege.2}Et « l'enfer, c'est les autres » : Sartre a précisé qu'il parlait de rapports faussés avec autrui, "
        "pas des autres en général.",
        ("P", 0.5),
    ], vis={
        "tab_rob": dict(type="tableau", img="t6-robinson", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .3],
                        legende="Walter Paget, Robinson Crusoé, illustration, 1891"),
        "suj3": dict(type="mot", t="« Peut-on être libre sans les autres ? »", g="un exemple qui fait penser : Robinson",
                     y=240, taille=66),
        "plan3": dict(type="liste", titre="« Peut-on être libre sans les autres ? »", items=[
            "I. Oui : les autres sont des limites (Robinson seul)",
            "II. Mais sans loi commune, la liberté est précaire (Hobbes, Locke)",
            "III. La liberté se construit avec les autres (Rousseau, Kant, l'éducation)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_lev": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.5, .5, .32],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651"),
        "tab_rob2": dict(type="tableau", img="t6-robinson", fond=True, sombre=True, de=[1.3, .5, .3], a=[1.05, .5, .45],
                         legende="Walter Paget, Robinson Crusoé, illustration, 1891"),
        "tab_ddhc": dict(type="tableau", img="t-ddhc", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                         legende="J.-J.-F. Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "c_locke": dict(type="cit", a="Locke", o="Second traité du gouvernement civil, § 57 (1690 ; trad. courante)", x=170, y=200, w=940),
        "p3": dict(type="def", cles=["construit", "éducation"], terme="III. La liberté se construit avec les autres",
                   t="La liberté civile (Rousseau), les droits garantis par la loi, l'éducation.",
                   etape="Kant : « l'homme ne peut devenir homme que par l'éducation » (Réflexions sur l'éducation, 1803).",
                   x=170, y=200, w=940),
        "piege": dict(type="liste", titre="Deux pièges de citation", items=[
            "« Ma liberté s'arrête là où commence celle des autres » : formule populaire, pas une citation (DDHC, art. 4 : « ne pas nuire à autrui »)",
            "« L'enfer, c'est les autres » (Huis clos, 1944) : des rapports faussés, pas les autres en général"],
                      marques=["✗", "!"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ V. explication de texte
    dict(id="explication", chap="L'explication de texte", fond="aube", humeur="calme",
         retenir="Explication : six éléments d'introduction, puis chaque phrase : quoi ? comment ? pourquoi ?", beats=[
        "{rousseau}{tab_con}Et si tu choisis l'explication ? Prenons un texte court et célèbre : Rousseau, Du contrat social, "
        "livre un, chapitre huit. Bonne nouvelle : pas besoin de connaître toute l'œuvre. L'essentiel est dans le texte, "
        "à condition de le lire de très près.",
        ("C", "Ce que l'homme perd par le contrat social, c'est sa liberté naturelle et un droit illimité à tout ce qui le tente "
              "et qu'il peut atteindre ; ce qu'il gagne, c'est la liberté civile et la propriété de tout ce qu'il possède.", "c_r1"),
        "{-c_r1}{-rousseau}{six}Avant d'écrire, on trouve les six éléments de l'introduction. {six.1}Le thème : la liberté, "
        "quand on entre en société. {six.2}La question : perd-on sa liberté en obéissant à des lois ? "
        "{six.3}La thèse adverse : oui, toute loi est une perte de liberté. {six.4}La thèse de Rousseau : on échange une liberté "
        "naturelle, sans limite mais précaire, contre une liberté civile, garantie par la loi. "
        "{six.5}L'enjeu : fonder une obéissance qui ne soit pas une servitude. {six.6}Le plan : un bilan des pertes et des gains, "
        "puis l'ajout décisif, la liberté morale.",
        "{-six}{-tab_con}{tab_con2}Car Rousseau ajoute une phrase, la plus importante.",
        ("C", "L'impulsion du seul appétit est esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.", "c_r2"),
        "{-c_r2}{gestes}Pour l'expliquer, trois gestes. {gestes.1}Reformuler : autrement dit, suivre chacun de ses désirs, "
        "c'est être mené par eux. {gestes.2}Définir : par « appétit », il faut entendre le désir immédiat, sans réflexion. "
        "{gestes.3}Illustrer : c'est ainsi que celui qui se fixe une règle, comme Ulysse au mât, est plus libre que celui "
        "qui obéit à chaque envie.",
        "{-gestes}{para}Le piège de l'explication, c'est la paraphrase : {para.g}répéter le texte avec d'autres mots, en moins bien. "
        "{para.d}Expliquer, c'est dire pourquoi l'auteur dit ce qu'il dit, et ce que sa phrase permet de penser.",
        "{-para}{tableau}Au brouillon, fais-le phrase par phrase, dans un tableau à quatre colonnes : la citation, "
        "{tableau.1}quoi, ce que dit la phrase ; {tableau.2}comment, par quels mots, quels procédés ; {tableau.3}et pourquoi, "
        "ce que cela apporte à la thèse.",
        ("P", 0.5),
    ], vis={
        "rousseau": dict(type="portrait", annee=1712, legende="Du contrat social, I, 8 (1762)", img="rousseau",
                         nom="Jean-Jacques Rousseau", dates="1712 – 1778", x=110, y=120, w=330, h=420),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.0, 0.5, 0.35], a=[1.2, 0.5, 0.5],
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "c_r1": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=640, y=130, w=570),
        "six": dict(type="liste", titre="Les six éléments de l'introduction", items=[
            "Thème : la liberté en société",
            "Question : obéir aux lois, est-ce perdre sa liberté ?",
            "Thèse adverse : toute loi est une perte de liberté",
            "Thèse : liberté naturelle échangée contre la liberté civile",
            "Enjeu : obéir sans être esclave",
            "Plan : pertes et gains, puis la liberté morale"],
                    marques=["1", "2", "3", "4", "5", "6"], x=170, y=90, w=940),
        "tab_con2": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.2, .5, .5], a=[1.0, .5, .4],
                         legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "c_r2": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=170, y=190, w=940),
        "gestes": dict(type="liste", titre="Expliquer une phrase : trois gestes", items=[
            "Reformuler · « autrement dit » : suivre chaque désir, c'est être mené par lui",
            "Définir · « par… il faut entendre » : l'appétit, le désir immédiat",
            "Illustrer · « c'est ainsi que » : Ulysse au mât"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "para": dict(type="cols", g="Paraphraser", gq="répéter le texte, en moins bien", d="Expliquer",
                     dq="dire pourquoi l'auteur dit ce qu'il dit", vs="≠"),
        "tableau": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Quoi ?", q="ce que dit la phrase"),
            dict(ic="chemins", t="Comment ?", q="les mots, les procédés"),
            dict(ic="colonnes", t="Pourquoi ?", q="ce que cela apporte à la thèse")]),
    }),

    # ------------------------------------------------------------------ VI. pièges et atouts
    dict(id="pieges", chap="Les pièges et les atouts", fond="nuit", humeur="tension",
         retenir="Pas de récitation, pas de catalogue : chaque auteur sert un argument, chaque argument a un exemple.", beats=[
        "{tab_per}{pieges}Les pièges, maintenant. Ceux qui coûtent le plus de points. "
        "{pieges.1}Réciter : faire le perroquet du cours, sans répondre à la question posée. "
        "{pieges.2}Le catalogue : « selon Descartes… selon Spinoza… selon Sartre… », des auteurs empilés sans fil.",
        "{pieges.3}Confondre les trois libertés : passer de la liberté politique au libre arbitre sans le dire. "
        "{pieges.4}Oublier la question en route : relis-la à chaque transition. "
        "{pieges.5}Et la troisième partie molle : « tout dépend des points de vue ».",
        "Méfie-toi aussi des accroches vides : « depuis la nuit des temps, l'homme cherche la liberté ». Le correcteur l'a lue "
        "deux cents fois. Commence plutôt par une scène précise, comme celles qui ouvrent chaque épisode de cette série.",
        "{-pieges}{-tab_per}{tab_bib}{atouts}Les atouts, maintenant. {atouts.1}Des exemples précis et travaillés : "
        "le prisonnier, Épictète, Ulysse, Robinson, le feu rouge, la vidéo qui se lance seule. "
        "{atouts.2}Les repères bien employés : contrainte et obligation, nécessaire et contingent, en droit et en fait.",
        "{atouts.3}Et quelques citations courtes, sûres, que tu peux expliquer. Pas plus de cinq ou six. "
        "{-atouts}{cits}Par exemple : {cits.1}Rousseau, sur l'obéissance à la loi qu'on s'est prescrite. "
        "{cits.2}Spinoza, conscients de nos désirs et ignorants des causes. {cits.3}Sartre, condamné à être libre. "
        "{cits.4}Et l'article quatre de la Déclaration de 1789.",
        ("Une citation que tu sais expliquer vaut dix citations que tu récites.", {"rate": "-5%"}),
        "{-cits}{-tab_bib}{rep_fin}Retiens-le : chaque auteur doit servir un argument. Et chaque argument doit avoir son exemple.",
        ("P", 0.5),
    ], vis={
        "tab_per": dict(type="tableau", img="t6-perroquet", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.3, .25, .45],
                        legende="Nature morte aux artichauts et au perroquet, Italie, XVIIᵉ siècle (CC0)"),
        "pieges": dict(type="liste", titre="Les cinq pièges", items=[
            "Réciter le cours sans répondre à la question", "Le catalogue d'auteurs empilés",
            "Confondre les trois libertés", "Oublier la question en route", "La partie III molle : « tout dépend »"],
                       marques=["✗", "✗", "✗", "✗", "✗"], x=170, y=110, w=940),
        "tab_bib": dict(type="tableau", img="t6-bibliotheque", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .5, .45],
                        legende="La Long Room, bibliothèque du Trinity College, Dublin (photo Diliff, CC BY-SA 4.0)"),
        "atouts": dict(type="liste", titre="Les atouts", items=[
            "Des exemples précis : le prisonnier, Épictète, Ulysse, Robinson, le feu rouge",
            "Les repères : contrainte / obligation, nécessaire / contingent, en droit / en fait",
            "Cinq ou six citations courtes, sûres, expliquées"], marques=["✓", "✓", "✓"], x=170, y=150, w=940),
        "cits": dict(type="liste", titre="Citations sûres", items=[
            "Rousseau : « l'obéissance à la loi qu'on s'est prescrite est liberté »",
            "Spinoza : « conscients de leurs désirs et ignorants des causes qui les déterminent »",
            "Sartre : « l'homme est condamné à être libre »",
            "DDHC, art. 4 : « pouvoir faire tout ce qui ne nuit pas à autrui »"], marques=["1", "2", "3", "4"],
                     x=170, y=130, w=940),
        "rep_fin": dict(type="def", cles=["argument", "exemple"], terme="La règle d'or",
                        t="Chaque auteur sert un argument ; chaque argument a son exemple.", x=170, y=230, w=940),
    }),

    # ------------------------------------------------------------------ VII. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : lire le sujet. Définir chaque mot, repérer le présupposé.",
        "{rec.2}Deux : problématiser. Une tension, pas une reformulation.",
        "{rec.3}Trois : construire. Trois parties qui se répondent, et une troisième qui déplace la question.",
        "{rec.4}Quatre : expliquer. Six éléments d'introduction, puis chaque phrase : quoi, comment, pourquoi.",
        "{-rec}{q_fin}À toi : choisis l'un des trois sujets, et fais-en le plan en vingt minutes. Les questions t'attendent sous la vidéo.",
        ("Et la prochaine fois… tout ce qu'il faut savoir, pour la veille de l'épreuve.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-q_fin}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LA COPIE", branches=[
            dict(t="Lire le sujet", items=["définir chaque mot", "le présupposé", "de quelle liberté ?"]),
            dict(t="Problématiser", items=["une tension", "pas une reformulation", "le fil d'Ariane"]),
            dict(t="Construire", items=["I. réponse spontanée", "II. objection", "III. une distinction qui dépasse"]),
            dict(t="Expliquer", items=["six éléments", "quoi ? comment ? pourquoi ?", "reformuler, définir, illustrer"])]),
        "q_fin": dict(type="question", t="Un sujet, un plan, vingt minutes"),
        "tab_fin": dict(type="tableau", img="t6-ariane", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="Johann Heinrich Tischbein, Ariane donnant le fil à Thésée, 1779"),
        "fin": dict(type="titre", sur="À suivre", t="Récap", sous="Épisode 7 · L'essentiel, pour la veille de l'épreuve"),
    }),
]

QUIZ = [
    dict(q="Que veut dire « problématiser » un sujet ?",
         r=["Recopier la question en commençant par « nous allons nous demander si »",
            "Montrer que la réponse évidente se heurte à un fait qui la contredit",
            "Annoncer les auteurs qu'on va citer", "Donner tout de suite sa réponse"], ok=1,
         voir="prob", ex="Problématiser, c'est faire apparaître une tension : d'un côté… mais de l'autre…, et les deux semblent vrais."),
    dict(q="Qu'est-ce que le présupposé d'un sujet ?",
         r=["Ce que la question tient pour acquis", "La réponse attendue par le correcteur",
            "La citation qui l'accompagne", "Le plan conseillé"], ok=0,
         voir="pres", ex="« Être libre, est-ce faire ce que l'on veut ? » suppose que je sais ce que je veux, et que ce vouloir vient de moi."),
    dict(q="Que doit faire une bonne troisième partie de dissertation ?",
         r=["Dire que tout dépend des points de vue", "Résumer les deux premières",
            "Déplacer la question grâce à une distinction nouvelle", "Ajouter de nouveaux auteurs"], ok=2,
         voir="rep_auto", ex="Exemple : indépendance (faire ce que je veux) / autonomie (obéir à la loi que je me suis donnée)."),
    dict(q="Pourquoi l'exemple d'Ulysse et des sirènes est-il utile ?",
         r=["Il montre que la liberté, c'est suivre ses envies",
            "Il montre qu'on peut être plus libre en se donnant une règle qu'en suivant son désir",
            "Il prouve que la liberté est une illusion", "Il illustre la liberté politique"], ok=1,
         voir="uly", ex="Attaché au mât à sa demande, Ulysse obéit à une règle qu'il s'est prescrite : c'est l'autonomie (Rousseau, Kant)."),
    dict(q="Quelle est la différence entre une erreur et une illusion ?",
         r=["Aucune", "L'illusion persiste même connue, car elle répond à un désir",
            "L'erreur est volontaire", "L'illusion est toujours collective"], ok=1,
         voir="ill", ex="Freud, L'Avenir d'une illusion (1927) : l'illusion dérive de nos souhaits."),
    dict(q="« Ma liberté s'arrête là où commence celle des autres » : que faut-il en penser ?",
         r=["C'est l'article 4 de la Déclaration de 1789", "C'est une phrase de Sartre",
            "C'est une formule populaire, pas une citation d'auteur", "C'est une phrase de Kant"], ok=2,
         voir="piege", ex="La DDHC (art. 4) dit : « La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui. »"),
    dict(q="Dans le tableau du brouillon, que met-on dans la colonne « pourquoi ? »",
         r=["Ce que dit la phrase", "Les procédés et les mots employés", "Ce que la phrase apporte à la thèse",
            "La biographie de l'auteur"], ok=2,
         voir="tableau", ex="Quoi ? ce que dit la phrase · Comment ? les mots, les procédés · Pourquoi ? ce que cela apporte à la thèse."),
]

CREDITS = [
    "Rousseau : Maurice Quentin de La Tour, 1753",
    "Tableaux et gravures : A. Coorte, Vanité au sablier (fin XVIIᵉ s.) ; A. Dürer, Saint Jérôme dans son cabinet (1514, Met, CC0) ; "
    "J. H. Tischbein, Ariane et Thésée (1779) ; V. van Gogh, La Ronde des prisonniers (1890) ; J. W. Waterhouse, Les Danaïdes (1906) "
    "et Ulysse et les sirènes (1891) ; J. Saenredam, L'Allégorie de la caverne (1604) ; W. Paget, Robinson Crusoé (1891) ; "
    "Du contrat social (1762) ; A. Bosse, frontispice du Léviathan (1651) ; J.-J.-F. Le Barbier, DDHC (1789) ; nature morte au perroquet, Italie, XVIIᵉ s. (CC0) ; F. Chauveau, Carte de Tendre (1654) : domaine public",
    "Photographies : salle d'examen (domaine public) ; Long Room du Trinity College, Dublin (Diliff, CC BY-SA 4.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
