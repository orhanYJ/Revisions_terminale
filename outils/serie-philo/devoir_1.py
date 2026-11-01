"""Le devoir, épisode 1 : « Qu'est-ce que le devoir ? »

Même format que la série « La liberté » (voir liberte_1.py). Nouveauté de la série : les notions abordées
(champ notions d'une scène, repère {#la liberté} dans le texte lu).
"""

CODE = "devoir-1"
NOTION = "Le devoir"
NUM = 1
TITRE = "Qu'est-ce que le devoir ?"
SUIVANT = "Épisode 2 · D'où vient le devoir ?"

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="lumiere", carton=False, beats=[
        "{tab_wal}{q1}Imagine. Tu marches dans la rue, et tu trouves un portefeuille par terre. "
        "Dedans : trois cents euros, et une carte d'identité. Personne ne t'a vu.",
        ("Personne.", {"rate": "-8%"}),
        "{-q1}Tu pourrais le garder. Rien ne t'en empêche. Et pourtant, une petite voix murmure : "
        "tu dois le rendre.",
        ("P", 0.5),
        "{-tab_wal}{tab_exa}{mots}Ce petit mot, devoir, est partout. {mots.1}Les devoirs à la maison. "
        "{mots.2}Le devoir de mémoire. {mots.3}Le devoir civique. {mots.4}Les droits et les devoirs. "
        "{mots.5}Et ce « tu dois » que l'on entend depuis l'enfance.",
        "{-mots}{-tab_exa}{q2}Mais au fond, qu'est-ce qui m'oblige… quand rien ne me force ?",
        ("C'est toute la question de cette série.", {"rate": "-4%"}),
        "{-q2}{serie}Six épisodes, et un récapitulatif, pour regarder ce mot de très près. "
        "Avec Rousseau, Kant, Durkheim, Nietzsche, Freud… et une jeune fille de la tragédie grecque, Antigone.",
        "Et d'abord, une question simple en apparence : qu'est-ce que le devoir ?",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_wal": dict(type="tableau", img="dv1-portefeuille", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.25, .5, .6],
                        legende="Un portefeuille perdu (photo Martin Cooper, CC BY 2.0)"),
        "q1": dict(type="question", t="Personne ne t'a vu. Que fais-tu ?"),
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "mots": dict(type="nuage", items=["les devoirs à la maison", "le devoir de mémoire", "le devoir civique",
                                          "droits et devoirs", "« tu dois »"]),
        "q2": dict(type="question", t="Qu'est-ce qui m'oblige… quand rien ne me force ?"),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="Rousseau, Kant, Durkheim, Nietzsche, Freud… et Antigone", y=270),
        "titre": dict(type="titre", sur="Le devoir · Épisode 1", t="Qu'est-ce que le devoir ?",
                      sous="Le mot, l'obligation, les trois devoirs, Gygès"),
    }),

    # ------------------------------------------------------------------ I. le mot
    dict(id="mot", chap="Le mot", fond="aube", humeur="mystere", notions=["la liberté"],
         retenir="Le devoir : une obligation, pas une contrainte. Il suppose un être libre.", beats=[
        "{tab_pre}{debere}Commençons, comme toujours, par le mot. Devoir vient du latin debere. "
        "Et debere vient lui-même de de-habere : tenir quelque chose de quelqu'un d'autre.",
        "{-debere}{dette}Celui qui doit, c'est celui qui a reçu, et qui doit rendre. C'est pour cela qu'en français, "
        "le même verbe dit deux choses. {dette.g}Je dois de l'argent. {dette.d}Je dois dire la vérité.",
        ("Avoir un devoir, ce serait donc… être en {!dette}dette.", {"rate": "-5%"}),
        "{lien_n}Un philosophe fera de ce lien entre la dette et la faute une arme contre la morale : Nietzsche. "
        "Ce sera l'épisode quatre.",
        "{-dette}{-lien_n}{-tab_pre}{sens}Attention, pourtant : en français, devoir a deux sens. {sens.1}« Il doit pleuvoir demain » : "
        "c'est une probabilité. {sens.2}« Tu dois rendre ce portefeuille » : c'est une obligation. Seul le second nous intéresse.",
        "{-sens}{oc}Et une obligation n'est pas une contrainte. On l'a vu dans la série sur {#la liberté}la liberté. "
        "{oc.g}Le brigand qui pointe son pistolet sur moi me contraint : il agit par la force. "
        "{oc.d}Le feu rouge, lui, m'oblige : il s'adresse à ma volonté. Je pourrais passer… mais je ne le dois pas.",
        "Rousseau le dit à propos du brigand : céder à la force, c'est un acte de nécessité, tout au plus de prudence. "
        "Dès que le brigand s'éloigne, je n'ai plus aucune raison d'obéir. La force peut me faire plier ; elle ne peut pas m'obliger.",
        "{-oc}{rousseau}{tab_con}Rousseau le résume en une phrase, au début du Contrat social.",
        ("C", "Convenons donc que force ne fait pas droit, et qu'on n'est obligé d'obéir qu'aux puissances légitimes.",
         "c_rous"),
        "{-rousseau}{-c_rous}{-tab_con}{def1}D'où une première définition. Le devoir, c'est une obligation : "
        "ce que je dois faire, même si je ne le veux pas… mais sans y être forcé.",
        "{def1.1}Et voici la conséquence, capitale. On ne donne pas de devoirs à une pierre, ni à un chien. "
        "Seul un être capable de choisir peut avoir des devoirs.",
        "Une pierre qui tombe ne fait pas son devoir : elle suit la pesanteur, sans pouvoir faire autrement. "
        "Un chien dressé non plus : il obéit par habitude, par crainte du bâton. "
        "Le devoir ne commence que là où il y a un choix… donc la possibilité de désobéir.",
        ("Si je dois… c'est que je peux.", {"rate": "-6%", "pitch": "-1Hz"}),
    ], vis={
        "tab_pre": dict(type="tableau", img="dv1-preteur", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .55],
                        legende="Quentin Metsys, Le Prêteur et sa femme, 1514 (musée du Louvre)"),
        "debere": dict(type="mot", t="DEBERE", g="latin : devoir · de-habere, tenir quelque chose d'un autre", y=250, taille=104),
        "dette": dict(type="cols", g="Devoir de l'argent", gq="une dette envers quelqu'un", d="Devoir faire",
                      dq="une obligation morale", vs="↔"),
        "lien_n": dict(type="tag", style="lien", t="Nietzsche : la dette et la faute (épisode 4)", x=170, y=560, w=620),
        "sens": dict(type="liste", titre="Deux sens du verbe devoir", items=[
            "« Il doit pleuvoir demain » : une probabilité",
            "« Tu dois rendre ce portefeuille » : une obligation"], marques=["≈", "!"], x=170, y=170, w=940),
        "oc": dict(type="cols", g="Contrainte", gq="le brigand : la force agit sur moi", d="Obligation",
                   dq="le feu rouge : je peux désobéir", vs="≠", repere="Repère · obligation / contrainte"),
        "rousseau": dict(type="portrait", annee=1712, legende="Du contrat social (1762)", img="rousseau",
                         nom="Jean-Jacques Rousseau", dates="1712 – 1778", x=110, y=120, w=330, h=420),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.2, .5, .5],
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 3 (1762)", x=640, y=170, w=570),
        "def1": dict(type="def", cles=["obligation", "forcé"], terme="Le devoir",
                     t="Une obligation : ce que je dois faire, même si je ne le veux pas, sans y être forcé.",
                     etape="Conséquence : seul un être libre peut avoir des devoirs.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. trois sortes de devoirs
    dict(id="trois", chap="Trois sortes de devoirs", fond="nuit", humeur="lumiere", notions=["l'État", "la justice"],
         retenir="Devoirs juridiques, sociaux, moraux : la sanction les distingue. Légal ≠ légitime.", beats=[
        "{cartes}Tous les devoirs ne se ressemblent pas. On peut en distinguer trois sortes.",
        "{cartes.1}{tab_imp}D'abord, les devoirs juridiques : payer ses impôts, respecter le code de la route. "
        "Ils sont écrits dans la loi. Si je ne les respecte pas, {#l'État}l'État me sanctionne : une amende, la prison.",
        "{-tab_imp}{cartes.2}{tab_tok}Ensuite, les devoirs sociaux : dire bonjour, tenir sa parole, être poli. "
        "Personne ne t'emprisonnera si tu oublies de dire merci… mais les autres te regarderont de travers.",
        "{-tab_tok}{cartes.3}{tab_rem}Enfin, les devoirs moraux : ne pas mentir, ne pas trahir, rendre le portefeuille. "
        "Là, souvent, personne ne te voit. La seule sanction est intérieure : le remords, la mauvaise conscience.",
        "{-cartes}{-tab_rem}{sanc}Retiens ce critère, très utile en copie : ce qui distingue les devoirs, c'est la sanction. "
        "{sanc.1}Extérieure et officielle pour le droit. {sanc.2}Sociale pour les mœurs. {sanc.3}Intérieure pour la morale.",
        "Attention, ces trois cercles se recoupent. Ne pas tuer est à la fois un devoir juridique et un devoir moral. "
        "Mentir à un ami n'est pas interdit par la loi, mais c'est une faute morale. "
        "Et certaines règles n'ont rien de moral : rouler à droite plutôt qu'à gauche, c'est une simple convention.",
        "{-sanc}{dd}Un mot aussi sur les droits. On les oppose souvent aux devoirs, mais l'un ne va pas sans l'autre. "
        "{dd.g}Si j'ai le droit de m'exprimer, {dd.d}les autres ont le devoir de me laisser parler. "
        "Mon droit, c'est le devoir des autres ; et leur droit, c'est le mien.",
        "{-dd}{tab_cod}{ll}Mais le droit et la morale peuvent-ils se contredire ? Oui. Il faut ici un repère. "
        "{ll.g}Ce qui est légal, c'est ce qui est conforme à la loi. "
        "{ll.d}Ce qui est légitime, c'est ce qui est juste : ce qui mérite d'être obéi.",
        ("Une loi peut être légale… sans être légitime.", {"rate": "-5%"}),
        "{-ll}{-tab_cod}{tab_the}Pendant des décennies, dans le sud des États-Unis, des lois obligeaient les Noirs "
        "à céder leur place dans les bus. C'était légal. Était-ce {#la justice}juste ? Évidemment pas.",
        "Ceux qui ont désobéi à ces lois, comme Rosa Parks à Montgomery en 1955, ont fait quelque chose d'étrange : "
        "ils ont enfreint la loi… au nom d'un devoir plus haut. Le devoir moral ne se réduit donc pas à l'obéissance aux lois.",
        "{seg}Ce conflit entre la loi et la justice sera au cœur de l'épisode cinq, avec Antigone, "
        "Rosa Parks et Martin Luther King.",
    ], vis={
        "cartes": dict(type="cartes", items=[
            dict(ic="colonnes", t="Devoirs juridiques", q="écrits dans la loi · sanction de l'État"),
            dict(ic="chemins", t="Devoirs sociaux", q="mœurs, politesse · regard des autres"),
            dict(ic="porte", t="Devoirs moraux", q="ne pas mentir · le remords")]),
        "tab_imp": dict(type="tableau", img="dv1-impots", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="D'après Marinus van Reymerswaele, Les Collecteurs d'impôts, XVIᵉ s. (Musée national de Varsovie)"),
        "tab_tok": dict(type="tableau", img="t-tokyo", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Tokyo, carrefour de Shibuya (photo Benh Lieu Song, CC BY-SA 2.0)"),
        "tab_rem": dict(type="tableau", img="dv1-remords", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .45],
                        legende="Pierre-Paul Prud'hon, La Justice et la Vengeance divine poursuivant le Crime, 1808 (Louvre)"),
        "sanc": dict(type="liste", titre="Le critère : la sanction", cles=["sanction"], items=[
            "Droit : la sanction de l'État (amende, prison)",
            "Mœurs : le regard des autres",
            "Morale : le remords, la conscience"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "dd": dict(type="cols", g="Mon droit", gq="m'exprimer librement", d="Le devoir des autres",
                   dq="me laisser parler", vs="="),
        "tab_cod": dict(type="tableau", img="dv1-code", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .4],
                        legende="Code civil des Français, 1804"),
        "ll": dict(type="cols", g="Légal", gq="conforme à la loi", d="Légitime", dq="juste, digne d'être obéi",
                   vs="≠", repere="Repère · légal / légitime"),
        "tab_the": dict(type="tableau", img="dv1-themis", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Thémis, déesse de la justice, Hong Kong (photo ChvhLR10, CC BY-SA 3.0)"),
        "seg": dict(type="tag", style="lien", t="Épisode 5 : Antigone, Rosa Parks, Martin Luther King", x=170, y=560, w=680),
    }),

    # ------------------------------------------------------------------ III. Gygès
    dict(id="gyges", chap="L'anneau de Gygès", fond="aube", humeur="tension", notions=["la justice", "le bonheur"],
         retenir="Gygès : serions-nous honnêtes sans témoin ? Agir par devoir ≠ agir par intérêt.", beats=[
        "{q_por}Revenons à notre portefeuille. Pourquoi le rendre ? Peut-être, tout simplement… parce qu'on a peur d'être vu. "
        "{-q_por}{tab_lyd}Platon a imaginé une expérience pour tester cette idée. Elle a vingt-quatre siècles.",
        "{gyg}Dans La République, le jeune Glaucon raconte l'histoire de Gygès, un berger de Lydie. "
        "{gyg.1}Un jour, après un orage, il découvre au fond d'une crevasse un anneau d'or. "
        "{gyg.2}En tournant la pierre de l'anneau vers l'intérieur de sa main, il s'aperçoit qu'il devient invisible. "
        "{gyg.3}Que fait-il ? Il se rend au palais, séduit la reine, tue le roi… et prend le pouvoir.",
        ("Et toi ? Si tu avais cet anneau… resterais-tu honnête ?", {"pitch": "+2Hz"}),
        "{-gyg}{-tab_lyd}{platon}{tab_ath}Glaucon en tire une conclusion terrible.",
        ("C", "Ce serait là une grande preuve que personne n'est juste par choix, mais par nécessité…", "c_gla"),
        "{-platon}{-c_gla}{-tab_ath}{pg}Si Glaucon a raison, {pg.1}le devoir n'est qu'un masque : nous ne sommes honnêtes que par peur "
        "d'être punis. {pg.2}Ce que nous appelons devoir ne serait que de la prudence, de l'intérêt bien compris.",
        "Pour Glaucon, la justice est née d'un compromis. Chacun voudrait commettre l'injustice sans la subir. "
        "Comme c'est impossible, les hommes ont passé un accord : ne plus se faire de tort. "
        "La loi serait ce pacte des faibles. Celui qui serait assez fort, ou invisible, n'aurait aucune raison de le respecter.",
        "{-pg}{dist}D'où une distinction essentielle. {dist.g}Agir par intérêt : je rends le portefeuille parce que quelqu'un "
        "pourrait m'avoir vu, ou pour toucher une récompense. {dist.d}Agir par devoir : je le rends parce que je le dois, "
        "même si personne ne le saura jamais.",
        "{kant_t}Kant fera de cette distinction le cœur de sa morale. Ce sera l'épisode trois.",
        "{-dist}{-kant_t}{tab_rep}{rep}Et Platon, lui ? Toute La République est une réponse à Glaucon. "
        "{rep.1}L'injuste, même tout-puissant, n'est pas heureux : son âme est en guerre contre elle-même. "
        "{rep.2}Être juste serait la condition du {#le bonheur}bonheur.",
        ("Le devoir et le bonheur, ennemis… ou alliés ? Gardons la question.", {"rate": "-5%"}),
    ], vis={
        "q_por": dict(type="question", t="Rendrais-tu le portefeuille si tu étais sûr de ne jamais être vu ?"),
        "tab_lyd": dict(type="tableau", img="dv1-lydie", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="Pièce d'électrum de Lydie, VIᵉ s. av. J.-C. (photo CNG coins, CC BY-SA 3.0)"),
        "gyg": dict(type="liste", titre="L'anneau de Gygès · Platon, La République, II", items=[
            "Un berger trouve un anneau d'or au fond d'une crevasse",
            "En tournant la pierre, il devient invisible",
            "Il séduit la reine, tue le roi, prend le pouvoir"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "platon": dict(type="portrait", annee=-428, legende="La République, livre II", img="platon", nom="Platon",
                       dates="v. 428 – 348 av. J.-C.", x=110, y=120, w=330, h=420),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.5, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511"),
        "c_gla": dict(type="cit", a="Glaucon, dans Platon", o="La République, II, 360c (trad. V. Cousin)", x=640, y=170, w=570),
        "pg": dict(type="liste", titre="Si Glaucon a raison…", items=[
            "Le devoir n'est qu'un masque : la peur d'être puni",
            "Ce qu'on appelle devoir n'est que prudence, intérêt bien compris"], marques=["?", "?"], x=170, y=170, w=940),
        "dist": dict(type="cols", g="Agir par intérêt", gq="pour ne pas être vu, pour une récompense", d="Agir par devoir",
                     dq="parce que je le dois, même sans témoin", vs="≠"),
        "kant_t": dict(type="tag", style="lien", t="Kant : agir par devoir (épisode 3)", x=170, y=560, w=520),
        "tab_rep": dict(type="tableau", img="t-clarke", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                        legende="Le plus ancien manuscrit de Platon, copié en 895 (Oxford, Bodleian Library)"),
        "rep": dict(type="liste", titre="La réponse de Platon", items=[
            "L'injuste, même tout-puissant, n'est pas heureux : son âme est en désordre",
            "Être juste serait la condition du bonheur"], marques=["→", "→"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ IV. morale et éthique
    dict(id="ethique", chap="Morale ou éthique ?", fond="nuit", humeur="calme", notions=["le bonheur", "la raison"],
         retenir="Morale : ce que je dois (des normes). Éthique : comment bien vivre (le bonheur).", beats=[
        "{me}Un dernier outil, pour aller plus loin. On emploie souvent morale et éthique comme des synonymes. "
        "Mais on peut les distinguer.",
        "{me.g}La morale parle le langage de l'obligation : il faut, tu dois, c'est interdit. "
        "{me.d}L'éthique parle plutôt le langage du conseil : voici comment vivre bien.",
        "Le philosophe Paul Ricœur propose de réserver le mot éthique à la recherche d'une vie bonne, "
        "et le mot morale aux normes, aux règles, aux devoirs.",
        "{-me}{arist}{tab_eti}Les Grecs, Aristote en tête, pensaient surtout en termes d'éthique : comment devenir vertueux ? "
        "Comment être heureux ? Pour eux, bien agir et bien vivre, c'est la même chose.",
        "Pour Aristote, la vertu est une habitude, une disposition qu'on acquiert en agissant : "
        "on devient courageux en accomplissant des actes courageux. Et la vertu est un juste milieu : "
        "le courage se tient entre la lâcheté, qui fuit tout danger, et la témérité, qui se jette dans tous. "
        "Pas de « tu dois » ici : un art de bien vivre, qui s'apprend comme un métier.",
        "{-arist}{-tab_eti}{tab_kan}{kmod}Les modernes, avec Kant, pensent surtout en termes de morale : que dois-je faire ? "
        "Et Kant prévient : le devoir ne promet pas le bonheur. Il demande seulement d'agir selon la {#la raison}raison.",
        "{-kmod}{-tab_kan}{q3}Et si ces deux questions se contredisaient ? Si faire son devoir rendait malheureux ?",
        ("Nous retrouverons ce conflit entre devoir et bonheur dans l'épisode quatre… et au bac.", {"rate": "-4%"}),
    ], vis={
        "me": dict(type="cols", g="La morale", gq="des normes : « tu dois », le bien et le mal", d="L'éthique",
                   dq="la vie bonne : « comment bien vivre ? »", vs="≠", plus=True),
        "arist": dict(type="portrait", annee=-384, legende="Éthique à Nicomaque", img="aristote", nom="Aristote",
                      dates="384 – 322 av. J.-C.", x=110, y=120, w=330, h=420),
        "tab_eti": dict(type="tableau", img="dv1-ethique", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .4],
                        legende="Aristote, Éthique à Nicomaque, manuscrit enluminé, XVᵉ s."),
        "tab_kan": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Königsberg, ville de Kant, photochrome, vers 1900 (domaine public)"),
        "kmod": dict(type="cols", g="Les Grecs", gq="Aristote : comment être heureux ?", d="Les modernes",
                     dq="Kant : que dois-je faire ?", vs="→"),
        "q3": dict(type="question", t="Faire son devoir peut-il rendre malheureux ?"),
    }),

    # ------------------------------------------------------------------ V. les grandes questions
    dict(id="questions", chap="Les grandes questions", fond="aube", humeur="tension", notions=["la religion", "la liberté"],
         retenir="Le grand problème : le devoir est-il une contrainte déguisée, ou la marque de notre liberté ?", beats=[
        "{tab_pen}{orig}Nous avons défini le devoir. Reste la question qui fâche : d'où vient-il ? Qui a le droit de me dire : tu dois ? "
        "{orig.1}La société, qui m'a élevé ? {orig.2}{#la religion}Dieu, qui a donné des commandements ? "
        "{orig.3}Ma propre raison ? {orig.4}Ou bien n'est-ce qu'une habitude, une peur, une illusion ?",
        "Chacune de ces réponses a ses défenseurs. Pour le sociologue Durkheim, c'est la société qui parle en nous. "
        "Pour les croyants, la loi vient de Dieu. Pour Kant, c'est la raison elle-même qui se donne sa loi. "
        "Et pour Nietzsche ou Freud, le devoir pourrait bien n'être qu'un dressage : une voix intériorisée, qui nous fait souffrir.",
        "{-orig}{-tab_pen}{tab_ant}{plan}C'est le chemin de cette série. {plan.1}Épisode deux : d'où vient le devoir ? "
        "La société, Dieu, la conscience. {plan.2}Épisode trois : Kant, et le devoir fondé sur la raison. "
        "{plan.3}Épisode quatre : Nietzsche, Freud et les morales du bonheur contre le devoir. "
        "{plan.4}Épisode cinq : quand les devoirs se contredisent, avec Antigone. {plan.5}Épisode six : le devoir au bac.",
        "{-plan}{-tab_ant}{q5}Et derrière toutes ces questions, une seule. Le devoir est-il une chaîne… "
        "ou la marque même de notre liberté ?",
        ("P", 0.8),
    ], vis={
        "tab_pen": dict(type="tableau", img="t-penseur", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Auguste Rodin, Le Penseur, détail de La Porte de l'Enfer, musée Rodin (photo Jebulon, CC0)"),
        "orig": dict(type="liste", titre="D'où vient le devoir ?", items=[
            "De la société, qui m'a éduqué ?", "De Dieu, et de ses commandements ?",
            "De ma propre raison ?", "D'une habitude, d'une peur, d'une illusion ?"],
                     marques=["?", "?", "?", "?"], x=170, y=140, w=940),
        "tab_ant": dict(type="tableau", img="dv1-antigone", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .45, .3],
                        legende="Frederic Leighton, Antigone, 1882"),
        "plan": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · D'où vient le devoir ? La société, Dieu, la conscience",
            "Ép. 3 · Le devoir selon Kant",
            "Ép. 4 · Contre le devoir : Nietzsche, Freud, les morales du bonheur",
            "Ép. 5 · Conflits de devoirs : Antigone",
            "Ép. 6 · Le devoir à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
        "q5": dict(type="question", t="Le devoir : une chaîne… ou la marque de notre liberté ?"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : devoir vient de debere. Le devoir est une obligation, "
        "pas une contrainte, et il suppose un être libre.",
        "{rec.2}Deux : il y a trois sortes de devoirs, juridiques, sociaux et moraux. La sanction les distingue.",
        "{rec.3}Trois : l'anneau de Gygès. Serions-nous honnêtes sans témoin ? Agir par devoir, ce n'est pas agir par intérêt.",
        "{rec.4}Quatre : deux repères. Légal et légitime. Morale et éthique.",
        "{-rec}{frise}Maintenant, à toi : quelques questions t'attendent sous la vidéo.",
        ("Et la prochaine fois : d'où vient le devoir ?", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-frise}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE DEVOIR", branches=[
            dict(t="Le mot", items=["debere : la dette", "obligation ≠ contrainte", "suppose un être libre"]),
            dict(t="Trois devoirs", items=["juridiques, sociaux, moraux", "la sanction les distingue"]),
            dict(t="Gygès", items=["honnête sans témoin ?", "devoir ≠ intérêt"]),
            dict(t="Deux repères", items=["légal / légitime", "morale / éthique"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Platon", d=-428, img="platon"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Nietzsche", d=1844, img="nietzsche"), dict(nom="Freud", d=1856, img="freud"),
            dict(nom="Durkheim", d=1858, img="durkheim")]),
        "tab_fin": dict(type="tableau", img="dv1-moise", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .35],
                        legende="Rembrandt, Moïse brisant les Tables de la Loi, 1659 (Gemäldegalerie, Berlin)"),
        "fin": dict(type="titre", sur="À suivre", t="D'où vient le devoir ?", sous="Épisode 2 · La société, Dieu, la conscience"),
    }),
]

QUIZ = [
    dict(q="De quel mot latin vient « devoir », et que signifie-t-il d'abord ?",
         r=["Debere : tenir quelque chose d'un autre, être en dette", "Officium : la fonction",
            "Lex : la loi", "Virtus : le courage"], ok=0,
         voir="debere", ex="Debere vient de de-habere : celui qui doit tient quelque chose d'un autre. D'où le double sens : devoir de l'argent, devoir faire."),
    dict(q="Le feu rouge relève de…",
         r=["la contrainte", "l'obligation", "la nécessité", "la sanction sociale"], ok=1,
         voir="oc", ex="Je pourrais passer, rien ne m'en empêche physiquement : l'obligation s'adresse à ma volonté. Le pistolet du brigand, lui, me contraint."),
    dict(q="Pourquoi seul un être libre peut-il avoir des devoirs ?",
         r=["Parce que la loi le dit", "Parce qu'une obligation suppose qu'on puisse obéir… ou non",
            "Parce que les animaux n'ont pas de société", "Parce que le devoir est une contrainte"], ok=1,
         voir="def1", ex="On ne donne pas d'ordre à une pierre : « si je dois, c'est que je peux »."),
    dict(q="Qu'est-ce qui distingue un devoir moral d'un devoir juridique ?",
         r=["Le devoir moral est écrit dans la loi", "La sanction : intérieure (le remords) pour la morale, extérieure (l'État) pour le droit",
            "Le devoir juridique ne concerne que les adultes", "Rien : ce sont des synonymes"], ok=1,
         voir="sanc", ex="Droit : sanction de l'État ; mœurs : regard des autres ; morale : le remords, la conscience."),
    dict(q="Les lois de ségrégation dans les bus américains étaient…",
         r=["légitimes mais illégales", "légales mais illégitimes", "ni légales ni légitimes", "légales et légitimes"], ok=1,
         voir="ll", ex="Conformes à la loi de l'époque, donc légales ; injustes, donc illégitimes. Repère : légal / légitime."),
    dict(q="Que veut montrer Glaucon avec l'anneau de Gygès ?",
         r=["Que l'invisibilité est un pouvoir divin", "Que nous ne sommes justes que par peur d'être punis",
            "Que les rois sont toujours injustes", "Que la justice rend heureux"], ok=1,
         voir="c_gla", ex="« Personne n'est juste par choix, mais par nécessité » : sans témoin, chacun agirait comme Gygès. Platon lui répondra dans toute La République."),
    dict(q="Rendre le portefeuille pour toucher une récompense, c'est…",
         r=["agir par devoir", "agir par intérêt", "agir par contrainte", "agir par habitude"], ok=1,
         voir="dist", ex="L'action est conforme au devoir, mais le motif est l'intérêt. Kant fera de cette distinction le cœur de sa morale (épisode 3)."),
    dict(q="Selon la distinction proposée par Ricœur, l'éthique concerne plutôt…",
         r=["les normes et les interdits", "la recherche d'une vie bonne", "les lois de l'État", "les règles de politesse"], ok=1,
         voir="me", ex="Morale : ce que je dois (normes) ; éthique : comment bien vivre. Les Grecs pensent en termes d'éthique, Kant en termes de morale."),
]

CREDITS = [
    "Portraits : Rousseau (Maurice Quentin de La Tour, 1753) ; Platon (Raphaël, L'École d'Athènes, détail) ; Aristote (buste, Palazzo Altemps, photo Jastrow) ; Kant, Nietzsche, Freud, Durkheim (domaine public)",
    "Tableaux et gravures : Quentin Metsys, Le Prêteur et sa femme (1514) ; d'après Marinus van Reymerswaele, Les Collecteurs d'impôts (XVIᵉ s.) ; Pierre-Paul Prud'hon, La Justice et la Vengeance divine poursuivant le Crime (1808) ; Raphaël, L'École d'Athènes (1509-1511) ; Frederic Leighton, Antigone (1882) ; Rembrandt, Moïse brisant les Tables de la Loi (1659) ; Rodin, Le Penseur (photo Jebulon, CC0) : domaine public",
    "Documents et photographies : Du contrat social (1762) ; Code civil des Français (1804) ; manuscrit Clarke de Platon (895, Bodleian) ; Éthique à Nicomaque, manuscrit enluminé ; Königsberg, photochrome ; salle d'examen ; portefeuille perdu (Martin Cooper, CC BY 2.0) ; Shibuya (Benh Lieu Song, CC BY-SA 2.0) ; Thémis, Hong Kong (ChvhLR10, CC BY-SA 3.0) ; pièce de Lydie (CNG coins, CC BY-SA 3.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
