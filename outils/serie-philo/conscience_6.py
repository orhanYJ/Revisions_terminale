"""La conscience, épisode 6 : « La conscience à l'épreuve du bac »

Même structure que devoir_6.py : trois sujets décortiqués, une explication de texte pas à pas (Pascal, Pensées,
éd. Brunschvicg, fr. 347 et 348, vérifiés sur Wikisource), pièges. Méthode cohérente avec le guide de l'explication
du site (six éléments de l'introduction, trois gestes, quoi / comment / pourquoi, avocat de l'auteur, conclusion en
quatre temps). Déclaration universelle des droits de l'homme (1948), article 1 (texte officiel français).
"""

CODE = "conscience-6"
NOTION = "La conscience"
NUM = 6
TITRE = "La conscience à l'épreuve du bac"
SUIVANT = "Épisode 7 · Récap"
PRONONCIATION = {"Narcisse": "Narcisse", "Parmigianino": "Parmidjanino", "Hume": "Youme", "Leibniz": "Laïbnitz"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_mag}{q1}Tu as sûrement vécu ça. Quelqu'un t'enregistre, puis te fait écouter. Et tu sursautes : "
        "c'est ma voix, ça ? Elle sonne étrange, presque étrangère. Pourtant, tout le monde autour de toi la reconnaît.",
        ("Les autres entendent ta voix telle qu'elle est. Toi, tu ne l'avais jamais vraiment entendue.", {"rate": "-5%"}),
        "{-q1}{q2}Voilà, en trente secondes, un sujet de bac. Suis-je vraiment ce que j'ai conscience d'être ? "
        "Et voilà surtout une accroche : un fait précis, que chacun connaît, plutôt qu'une généralité.",
        "{-q2}{-tab_mag}{tab_ecr}{lien}La méthode générale, on l'a vue dans la série sur la liberté, puis appliquée au devoir. "
        "Ici, on l'applique à la conscience : trois sujets décortiqués, puis l'explication d'un texte de Pascal.",
        ("P", 0.3),
        "{-lien}{-tab_ecr}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_mag": dict(type="tableau", img="cs6-magneto", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Magnétophone, vers 1960, Wisconsin Historical Museum (photo Daderot, CC0)"),
        "q1": dict(type="question", t="C'est ma voix, ça ?"),
        "q2": dict(type="question", t="Suis-je ce que j'ai conscience d'être ?"),
        "tab_ecr": dict(type="tableau", img="cs6-ecriture", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Albert Anker, La Leçon d'écriture, XIXᵉ siècle"),
        "lien": dict(type="tag", style="lien", t="La méthode générale : série « La liberté », épisode 6", x=170, y=560, w=700),
        "titre": dict(type="titre", sur="La conscience · Épisode 6", t="La conscience à l'épreuve du bac",
                      sous="Trois sujets, une explication de texte, les pièges"),
    }),

    # ------------------------------------------------------------------ I. sujet 1
    dict(id="sujet1", chap="Sujet 1 · Suis-je ce que j'ai conscience d'être ?", fond="aube", humeur="mystere",
         notions=["l'inconscient", "la liberté"],
         retenir="Suis-je ce que j'ai conscience d'être ? La conscience me donne une image de moi, partielle ; mais je ne suis pas une chose : je me fais.",
         beats=[
        "{tab_nar}{suj1}Premier sujet : suis-je ce que j'ai conscience d'être ?",
        "{-suj1}{mots}D'abord, les mots. {mots.1}« Suis-je » : la question porte sur mon être, sur ce que je suis vraiment. "
        "{mots.2}« Ce que j'ai conscience d'être » : l'image que je me fais de moi, de l'intérieur. "
        "{mots.3}Et le sujet demande si les deux coïncident : la conscience est-elle un miroir fidèle ?",
        "{-mots}{-tab_nar}{tab_mir}{prob}La problématique naît d'une tension. {prob.1}D'un côté, personne n'est mieux placé que moi "
        "pour savoir ce que je pense : j'y ai un accès direct. {prob.2}De l'autre, ce miroir peut déformer, comme ce miroir "
        "convexe où le peintre s'est représenté. {prob.3}Alors, la conscience me révèle-t-elle ce que je suis… "
        "ou seulement ce que je crois être ?",
        "{-prob}{plan1}Le plan, en trois temps. {plan1.1}Un : oui, en un sens. Descartes : je suis une chose qui pense, "
        "et rien ne m'est plus certain. Locke : je suis la même personne aussi loin que ma conscience, ma mémoire, peut remonter.",
        "{-tab_mir}{tab_des}{plan1.2}Deux : mais la conscience ne voit pas tout. Leibniz et ses petites perceptions, Freud et "
        "l'{#l'inconscient}inconscient : une part de moi m'échappe. Et Sartre l'a montré avec la honte : autrui me révèle "
        "ce que je ne vois pas de moi. Comme ta voix enregistrée.",
        "{plan1.3}Trois : bien plus, je ne suis pas une chose qu'il suffirait de bien regarder. Je suis ce que je fais. "
        "Sartre : la conscience n'a pas de dedans, elle se projette ; Hegel : je me reconnais dans mes œuvres.{-plan1}",
        "{-tab_des}{tab_nar2}{ex1}L'exemple qui fait mouche : se dire « je suis nul en maths », comme on dirait « j'ai les yeux bleus ». "
        "{ex1.1}C'est prendre l'image qu'on a de soi pour une nature. Or cette image peut changer, si je change ce que je fais.",
        "{-ex1}{dist1}La distinction qui dépasse le problème : {dist1.g}être, à la manière d'une chose, qui est ce qu'elle est ; "
        "{dist1.d}exister, à la manière d'une conscience, qui se fait. Je ne suis jamais tout à fait ce que j'ai conscience d'être, "
        "parce que je suis toujours en train de le devenir.",
        "{-dist1}{-tab_nar2}",
    ], vis={
        "tab_nar": dict(type="tableau", img="cs6-narcisse", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .55],
                        legende="Le Caravage, Narcisse, 1597-1599 (Galerie nationale d'art ancien, Rome)"),
        "suj1": dict(type="mot", t="« Suis-je ce que j'ai conscience d'être ? »", g="un miroir fidèle ?", y=240, taille=62),
        "mots": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« Suis-je » : ce que je suis vraiment", "« Ce que j'ai conscience d'être » : l'image que je me fais de moi",
            "Le sujet : les deux coïncident-ils ?"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_mir": dict(type="tableau", img="cs6-miroir", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Parmigianino, Autoportrait au miroir convexe, vers 1524 (Kunsthistorisches Museum, Vienne)"),
        "prob": dict(type="liste", titre="Étape 2 · Problématiser", items=[
            "J'ai un accès direct à ce que je pense", "Mais le miroir peut déformer",
            "La conscience révèle-t-elle ce que je suis, ou ce que je crois être ?"], marques=["si", "or", "?"],
                     x=170, y=150, w=940),
        "plan1": dict(type="liste", titre="« Suis-je ce que j'ai conscience d'être ? »", items=[
            "I. Oui : je suis une chose qui pense (Descartes) ; la mémoire fait la personne (Locke)",
            "II. Mais la conscience ne voit pas tout : Leibniz, Freud ; autrui me révèle (Sartre)",
            "III. Je ne suis pas une chose : je me fais par mes actes (Sartre, Hegel)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_des": dict(type="tableau", img="cs6-desespere", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="Gustave Courbet, Le Désespéré (autoportrait), 1843-1845 (collection particulière)"),
        "tab_nar2": dict(type="tableau", img="cs6-narcisse", fond=True, sombre=True, de=[1.3, .4, .75], a=[1.0, .5, .5],
                         legende="Le Caravage, Narcisse, 1597-1599 (Galerie nationale d'art ancien, Rome)"),
        "ex1": dict(type="def", cles=["nature", "change"], terme="L'exemple · « je suis nul en maths »",
                    t="Prendre l'image qu'on a de soi pour une nature, comme la couleur de ses yeux.",
                    etape="Or cette image peut changer, si je change ce que je fais.", x=170, y=200, w=940),
        "dist1": dict(type="cols", g="Être", gq="comme une chose : ce qu'elle est, une fois pour toutes",
                      d="Exister", dq="comme une conscience : se faire, devenir", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ II. sujet 2
    dict(id="sujet2", chap="Sujet 2 · Peut-on se connaître soi-même ?", fond="nuit", humeur="tension",
         notions=["la vérité", "l'inconscient"],
         retenir="Se connaître : le sujet et l'objet ne font qu'un. Pas de connaissance directe et complète, mais une compréhension par détours : autrui, les œuvres, les actes.",
         beats=[
        "{tab_rem}{suj2}Deuxième sujet : peut-on se connaître soi-même ? Ici, regarde bien la difficulté cachée dans le "
        "{!soi-même}soi-même.",
        "{-suj2}{oeil}Pour connaître quelque chose, il faut d'habitude prendre du recul : l'observer du dehors. "
        "{oeil.1}Mais quand je veux me connaître, celui qui observe et celui qui est observé ne font qu'un. "
        "{oeil.2}C'est le problème de l'œil, qui voit tout… sauf lui-même.",
        "{-oeil}{plan2}{plan2.1}Première partie : oui, et mieux que quiconque. Personne ne sait mieux que moi ce que je ressens. "
        "Descartes en fait la première vérité. Et Socrate faisait de connais-toi toi-même la tâche de toute une vie.",
        "{plan2.2}Deuxième partie : non, pas directement. Quand Hume rentre en lui-même, il ne trouve jamais un moi, "
        "seulement des perceptions qui se succèdent. Freud ajoute que l'essentiel se joue dans l'inconscient. "
        "Et l'amour-propre embellit le portrait : on se juge en avocat, rarement en juge.",
        "{-tab_rem}{tab_lun}{plan2.3}Troisième partie : on peut se comprendre, mais par détours. Par autrui, qui me renvoie "
        "une image de moi, Sartre et Hegel l'ont montré. Par mes œuvres, et par mes actes : c'est en agissant que je découvre "
        "de quoi je suis capable.{-plan2}",
        "{rem}L'exemple qui fait mouche : Rembrandt. En quarante ans, il a peint près de quatre-vingts autoportraits. "
        "{rem.1}S'il se connaissait d'un seul regard, un seul aurait suffi. {rem.2}Chaque tableau est une nouvelle enquête "
        "sur lui-même, jamais achevée.",
        "{-rem}{dist2}La distinction qui dépasse : {dist2.g}connaître, comme on connaît un objet, une fois pour toutes ; "
        "{dist2.d}se comprendre, par un travail patient d'interprétation, qui ne finit jamais. Le repère utile ici : "
        "objectif et subjectif. La {#la vérité}vérité sur soi n'est pas donnée ; elle se cherche.",
        "{-dist2}{-tab_lun}",
    ], vis={
        "tab_rem": dict(type="tableau", img="cs6-rembrandt", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Rembrandt, Autoportrait à l'âge de 63 ans, 1669 (National Gallery, Londres)"),
        "suj2": dict(type="mot", t="« Peut-on se connaître soi-même ? »", g="la difficulté est dans le « soi-même »",
                     y=240, taille=68),
        "oeil": dict(type="def", cles=["recul", "lui-même"], terme="La difficulté du sujet",
                     t="Connaître, c'est prendre du recul. Mais ici, celui qui observe et celui qui est observé ne font qu'un.",
                     etape="L'œil voit tout… sauf lui-même.", x=170, y=190, w=940),
        "plan2": dict(type="liste", titre="« Peut-on se connaître soi-même ? »", items=[
            "I. Oui, mieux que quiconque : Descartes, « connais-toi toi-même » (Socrate)",
            "II. Non, pas directement : Hume, Freud, l'amour-propre",
            "III. Se comprendre par détours : autrui, les œuvres, les actes (Sartre, Hegel)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_lun": dict(type="tableau", img="cs6-lune", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .45],
                        legende="Caspar David Friedrich, Deux hommes contemplant la lune, 1819-1820 (Galerie Neue Meister, Dresde)"),
        "rem": dict(type="liste", titre="L'exemple · les autoportraits de Rembrandt", items=[
            "S'il se connaissait d'un regard, un seul aurait suffi", "Chaque tableau : une nouvelle enquête sur soi"],
                    marques=["1", "2"], x=170, y=190, w=940),
        "dist2": dict(type="cols", g="Se connaître", gq="comme un objet, une fois pour toutes",
                      d="Se comprendre", dq="par un travail d'interprétation, jamais achevé", vs="≠",
                      repere="Repère · objectif / subjectif"),
    }),

    # ------------------------------------------------------------------ III. sujet 3
    dict(id="sujet3", chap="Sujet 3 · La conscience fait-elle la dignité de l'homme ?", fond="aube", humeur="lumiere",
         notions=["le devoir", "la justice"],
         retenir="La conscience fonde la dignité (Pascal, Kant)… mais la dignité ne se mesure pas au degré de conscience : elle appartient à toute personne.",
         beats=[
        "{tab_udh}{suj3}Troisième sujet : la conscience fait-elle la dignité de l'homme ?",
        "{-suj3}{mots3}Les mots, encore. {mots3.1}« Faire » : produire, ou fonder ? La conscience est-elle la source de la dignité ? "
        "{mots3.2}« La dignité » : ce qui, dit Kant, n'a pas de prix, vu dans la série sur le {#le devoir}devoir. "
        "{mots3.3}« De l'homme » : de tout homme, par opposition à l'animal et à la chose.",
        "{-mots3}{prob3}Le piège est caché dans une conséquence. {prob3.1}Si la dignité vient de la conscience, "
        "alors celui qui en a moins, le nouveau-né, le malade plongé dans le coma, aurait-il moins de dignité ? "
        "{prob3.2}Évidemment, non. Voilà la tension à travailler.",
        "{-prob3}{plan3}{plan3.1}Première partie : oui, la conscience nous élève. Pascal : l'homme est un roseau pensant, "
        "et toute notre dignité consiste en la pensée. Kant : dire « je » élève l'homme au-dessus de tous les autres vivants.",
        "{plan3.2}Deuxième partie : mais la conscience est aussi source de misère. Seul un être conscient peut humilier, "
        "mentir, se mentir ; seul il sait qu'il va mourir. Et faire dépendre la dignité du degré de conscience "
        "menacerait les plus fragiles.",
        "{plan3.3}Troisième partie : la dignité appartient à la personne, non à ses performances. "
        "La conscience n'est pas une note qu'on obtient ; c'est le signe que nous sommes des êtres responsables, "
        "capables de répondre de nos actes. Et ce statut, on le reconnaît à tout homme.{-plan3}",
        ("C", "Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils sont doués de raison et de "
              "conscience et doivent agir les uns envers les autres dans un esprit de fraternité.", "c_dudh"),
        "{-c_dudh}{dist3}La distinction qui dépasse : {dist3.g}avoir conscience, en fait, plus ou moins, selon l'âge ou la santé ; "
        "{dist3.d}être une personne, en droit, pleinement, toujours. Le repère : en fait et en droit. "
        "C'est ce qui permet de parler de {#la justice}justice envers ceux qui ne peuvent pas la réclamer.",
        "{-dist3}{-tab_udh}",
    ], vis={
        "tab_udh": dict(type="tableau", img="cs6-udhr", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .6, .4],
                        legende="Eleanor Roosevelt et la Déclaration universelle des droits de l'homme, 1949 (FDR Library, CC BY 2.0)"),
        "suj3": dict(type="mot", t="« La conscience fait-elle la dignité de l'homme ? »", g="un sujet piégé", y=240, taille=60),
        "mots3": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« Faire » : produire, ou fonder ?", "« La dignité » : ce qui n'a pas de prix (Kant)",
            "« De l'homme » : de tout homme, face à l'animal et à la chose"], marques=["1", "2", "3"],
                      x=170, y=150, w=940),
        "prob3": dict(type="liste", titre="Étape 2 · Le piège", items=[
            "Si la dignité vient de la conscience, le nouveau-né, le malade dans le coma en auraient moins ?",
            "Évidemment, non : voilà la tension"], marques=["?", "!"], x=170, y=170, w=940),
        "plan3": dict(type="liste", titre="« La conscience fait-elle la dignité de l'homme ? »", items=[
            "I. Oui : le roseau pensant (Pascal) ; le « je » (Kant)",
            "II. Mais elle est aussi source de misère ; et le degré de conscience menacerait les fragiles",
            "III. La dignité appartient à la personne, responsable, en droit"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "c_dudh": dict(type="cit", a="Déclaration universelle des droits de l'homme", o="article 1 (10 décembre 1948)",
                       x=170, y=190, w=940),
        "dist3": dict(type="cols", g="Avoir conscience", gq="en fait : plus ou moins, selon l'âge ou la santé",
                      d="Être une personne", dq="en droit : pleinement, toujours", vs="≠", repere="Repère · en fait / en droit"),
    }),

    # ------------------------------------------------------------------ IV. explication : le texte
    dict(id="texte", chap="L'explication · Le texte", fond="nuit", humeur="calme", notions=["la nature", "la raison"],
         retenir="Introduction : thème, question, thèse adverse, thèse, enjeu, plan. Toujours avec les lignes du texte.", beats=[
        "{tab_ros}Et si tu choisis l'explication de texte ? Voici un texte court et célèbre : Pascal, Pensées, "
        "le roseau pensant, que tu as rencontré dans l'épisode cinq. Écoute-le en entier.",
        ("C", "L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant. Il ne faut pas que "
              "l'univers entier s'arme pour l'écraser : une vapeur, une goutte d'eau, suffit pour le tuer.", "c_t1"),
        "{-c_t1}",
        ("C", "Mais, quand l'univers l'écraserait, l'homme serait encore plus noble que ce qui le tue, parce qu'il sait qu'il meurt, "
              "et l'avantage que l'univers a sur lui ; l'univers n'en sait rien. Toute notre dignité consiste donc en la pensée. "
              "C'est de là qu'il faut nous relever et non de l'espace et de la durée, que nous ne saurions remplir. "
              "Travaillons donc à bien penser : voilà le principe de la morale.", "c_t2"),
        "{-c_t2}Et, dans un fragment voisin, la même idée, resserrée.",
        ("C", "Ce n'est point de l'espace que je dois chercher ma dignité, mais c'est du règlement de ma pensée. "
              "Je n'aurai pas davantage en possédant des terres : par l'espace, l'univers me comprend et m'engloutit "
              "comme un point ; par la pensée, je le comprends.", "c_t3"),
        "{-c_t3}{-tab_ros}{tab_pen}{six}Au brouillon, on cherche d'abord les six éléments de l'introduction. "
        "{six.1}Le thème : la place de l'homme dans l'univers. {six.2}La question : qu'est-ce qui fait la dignité de l'homme, "
        "si faible face à la {#la nature}nature ? {six.3}La thèse adverse, ce qu'on penserait spontanément : la grandeur se mesure "
        "à la force, à la taille, aux biens ; face à l'univers, l'homme n'est rien.",
        "{six.4}La thèse de Pascal : l'homme, le plus faible des êtres, est plus noble que l'univers qui l'écrase, "
        "car il sait qu'il meurt ; toute sa dignité consiste en la pensée. {six.5}L'enjeu : fonder la morale, "
        "car si notre dignité est de penser, notre devoir est de bien penser. "
        "{six.6}Le plan : d'abord l'image du roseau, la thèse en raccourci ; puis la démonstration par l'écrasement ; "
        "enfin la conséquence morale, que le fragment 348 confirme.",
        "{-six}{-tab_pen}",
    ], vis={
        "tab_ros": dict(type="tableau", img="cs5-roseaux", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Roseaux communs au bord d'un lac (photo Joshua Mayer, CC BY-SA 2.0)"),
        "c_t1": dict(type="cit", a="Pascal", o="Pensées, fr. 347 (éd. Brunschvicg ; 1670)", x=170, y=170, w=940),
        "c_t2": dict(type="cit", a="Pascal", o="Pensées, fr. 347 (suite)", x=170, y=100, w=940),
        "c_t3": dict(type="cit", a="Pascal", o="Pensées, fr. 348, « Roseau pensant »", x=170, y=140, w=940),
        "tab_pen": dict(type="tableau", img="cs6-pensees", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .4],
                        legende="Pascal, Pensées sur la religion, copie manuscrite, XVIIᵉ siècle (domaine public)"),
        "six": dict(type="liste", titre="Les six éléments de l'introduction", items=[
            "Thème : la place de l'homme dans l'univers",
            "Question : qu'est-ce qui fait la dignité d'un être si faible ?",
            "Thèse adverse : la grandeur se mesure à la force ; l'homme n'est rien",
            "Thèse : l'homme sait qu'il meurt ; sa dignité est la pensée",
            "Enjeu : fonder la morale sur le « bien penser »",
            "Plan : l'image · la démonstration · la conséquence morale (et fr. 348)"],
                    marques=["1", "2", "3", "4", "5", "6"], cles=["thèse adverse"], x=170, y=90, w=940),
    }),

    # ------------------------------------------------------------------ V. explication : le développement
    dict(id="developpement", chap="L'explication · Phrase par phrase", fond="aube", humeur="calme",
         notions=["la vérité", "la religion"],
         retenir="Pour chaque phrase : quoi, comment, pourquoi. Trois gestes : reformuler, définir, illustrer. Discuter en avocat de l'auteur.",
         beats=[
        "{tab_fla}{qcp}Puis, phrase par phrase, un tableau : la citation, et trois colonnes. Prenons la phrase charnière : "
        "« quand l'univers l'écraserait, l'homme serait encore plus noble que ce qui le tue ». "
        "{qcp.1}Quoi ? Même vaincu, l'homme l'emporte sur ce qui le détruit.",
        "{qcp.2}Comment ? Par une hypothèse extrême, « quand l'univers l'écraserait », un comparatif, « plus noble », "
        "et une cause, « parce qu'il sait ». {qcp.3}Pourquoi ? Pour déplacer la grandeur : de la force vers la conscience.",
        "{-qcp}{-tab_fla}{tab_hub}{ges}Pour expliquer, trois gestes. {ges.1}Reformuler : autrement dit, mourir en le sachant "
        "vaut plus que tuer sans le savoir. {ges.2}Définir : par « pensée », il faut entendre ici la conscience, le savoir de soi "
        "et du monde. {ges.3}Illustrer : c'est ainsi qu'un astronome, poussière dans une galaxie parmi des milliards, "
        "peut pourtant mesurer l'univers qui l'ignore.",
        "{-ges}{jeu}Et ne manque pas, dans le fragment 348, le jeu sur le verbe comprendre. {jeu.g}Par l'espace, l'univers "
        "me comprend : il me contient, comme un point. {jeu.d}Par la pensée, je le comprends : je le saisis par l'esprit. "
        "Un seul mot, deux sens : c'est le cœur du texte.",
        "{-jeu}{-tab_hub}{tab_mad}{av}Enfin, interroge le texte, mais en avocat de l'auteur. {av.1}Objection : savoir qu'on meurt "
        "ne sauve de rien, et rend peut-être plus malheureux que l'animal, qui l'ignore. {av.2}Réponse : Pascal ne dit pas "
        "que la pensée rend heureux, mais digne. Il l'écrit ailleurs : un arbre ne se connaît pas misérable ; "
        "c'est être grand que de connaître qu'on est misérable.",
        "{-av}{conc}Pour conclure, quatre temps. {conc.1}Le bilan : le plus faible des êtres est le plus noble, parce qu'il pense. "
        "{conc.2}La réponse à la question : la dignité de l'homme est dans la pensée, non dans la force. "
        "{conc.3}L'intérêt du texte : il fonde la morale sur un devoir de bien penser. "
        "{conc.4}Et, si tu veux, une ouverture : Kant, pour qui ce qui n'a pas de prix a une dignité.",
        "{-conc}{-tab_mad}{tab_ave}{pie}Trois pièges à éviter. {pie.1}Raconter la vie de Pascal, ou sa foi, en oubliant le texte : "
        "il écrit une apologie de la {#la religion}religion chrétienne, mais ce fragment se lit d'abord pour lui-même. "
        "{pie.2}La paraphrase : répéter l'image du roseau avec d'autres mots. {pie.3}Et le contresens : croire que Pascal "
        "méprise l'homme, ou au contraire qu'il le croit tout-puissant. Il dit les deux à la fois : misérable, et grand.",
        ("Un roseau, mais qui pense. Toute l'explication tient dans ce « mais ».", {"rate": "-5%"}),
        "{-pie}{-tab_ave}",
    ], vis={
        "tab_fla": dict(type="tableau", img="cs6-flammarion", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .45],
                        legende="Gravure dite « de Flammarion », dans L'Atmosphère de Camille Flammarion, 1888"),
        "qcp": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Quoi ?", q="même vaincu, l'homme l'emporte"),
            dict(ic="chemins", t="Comment ?", q="« quand… » · « plus noble » · « parce qu'il sait »"),
            dict(ic="colonnes", t="Pourquoi ?", q="déplacer la grandeur : de la force à la conscience")]),
        "tab_hub": dict(type="tableau", img="cs6-hubble", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.4, .5, .5],
                        legende="Le champ ultra-profond de Hubble, environ 10 000 galaxies, 2004 (NASA, ESA, domaine public)"),
        "ges": dict(type="liste", titre="Expliquer une phrase : trois gestes", items=[
            "Reformuler · « autrement dit » : mourir en le sachant vaut plus que tuer sans le savoir",
            "Définir · « par… il faut entendre » : la pensée, le savoir de soi et du monde",
            "Illustrer · « c'est ainsi que » : l'astronome qui mesure l'univers"], marques=["1", "2", "3"],
                    x=170, y=150, w=940),
        "jeu": dict(type="cols", g="L'univers me comprend", gq="par l'espace : il me contient, comme un point",
                    d="Je le comprends", dq="par la pensée : je le saisis par l'esprit", vs="↔",
                    repere="Un mot, deux sens : le cœur du texte"),
        "tab_mad": dict(type="tableau", img="cs6-madeleine", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .45, .55],
                        legende="Georges de La Tour, La Madeleine à la veilleuse, vers 1640 (LACMA, Los Angeles)"),
        "av": dict(type="liste", titre="Discuter en avocat de l'auteur", items=[
            "Objection : savoir qu'on meurt ne sauve de rien, et rend malheureux",
            "Réponse : la pensée ne rend pas heureux, mais digne (fr. 397)"], marques=["?", "→"], x=170, y=180, w=940),
        "conc": dict(type="liste", titre="La conclusion en quatre temps", items=[
            "Bilan : le plus faible est le plus noble, parce qu'il pense", "Réponse : la dignité est dans la pensée",
            "Intérêt : une morale fondée sur le « bien penser »", "Ouverture : Kant, le prix et la dignité"],
                     marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "tab_ave": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "pie": dict(type="liste", titre="Trois pièges", items=[
            "Raconter la vie et la foi de Pascal en oubliant le texte", "Paraphraser l'image du roseau",
            "Le contresens : Pascal ne méprise pas l'homme, ni ne le croit tout-puissant"], marques=["✗", "✗", "✗"],
                    x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : chaque sujet se joue sur quelques mots. Suis-je. Soi-même. "
        "Faire la dignité.",
        "{rec.2}Deux : trois distinctions qui dépassent le problème. Être et exister. Se connaître et se comprendre. "
        "Avoir conscience, en fait, et être une personne, en droit.",
        "{rec.3}Trois : des exemples travaillés. La voix enregistrée, « je suis nul en maths », les autoportraits de Rembrandt, "
        "le malade dans le coma.",
        "{rec.4}Quatre : l'explication du roseau pensant. Six éléments d'introduction, quoi, comment, pourquoi, "
        "et le double sens du verbe comprendre.",
        "{-rec}{q_fin}{tab_fin}À toi : choisis l'un des trois sujets, et fais-en le plan en vingt minutes. "
        "Les questions t'attendent sous la vidéo.",
        ("La prochaine fois : le récapitulatif de toute la série.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-q_fin}{fin}",
        ("P", 8.0),
    ], vis={
        "rec": dict(type="carte", centre="LA CONSCIENCE AU BAC", branches=[
            dict(t="Lire le sujet", items=["suis-je · soi-même", "faire la dignité", "en fait / en droit"]),
            dict(t="Dépasser", items=["être / exister", "se connaître / se comprendre", "avoir conscience / être une personne"]),
            dict(t="Exemples", items=["la voix enregistrée", "les autoportraits de Rembrandt", "Narcisse, le miroir"]),
            dict(t="Expliquer Pascal", items=["six éléments", "quoi, comment, pourquoi", "« comprendre » : deux sens"])]),
        "q_fin": dict(type="question", t="Un sujet, un plan, vingt minutes."),
        "tab_fin": dict(type="tableau", img="cs6-lune", fond=True, sombre=True, de=[1.2, .45, .5], a=[1.0, .5, .5],
                        legende="Caspar David Friedrich, Deux hommes contemplant la lune, 1819-1820 (Galerie Neue Meister, Dresde)"),
        "fin": dict(type="titre", sur="À suivre", t="Récap", sous="Épisode 7 · Toute la série en un épisode"),
    }),
]

QUIZ = [
    dict(q="Dans « Suis-je ce que j'ai conscience d'être ? », quelle distinction permet de dépasser le problème ?",
         r=["Légal / légitime", "Être (comme une chose) / exister (se faire)", "Prix / dignité", "Croire / savoir"], ok=1,
         voir="dist1", ex="Je ne suis jamais tout à fait ce que j'ai conscience d'être, parce que je suis toujours en train de le devenir (Sartre)."),
    dict(q="Pourquoi « je suis nul en maths » est-il un bon exemple pour ce sujet ?",
         r=["Parce que c'est vrai pour beaucoup d'élèves", "Parce qu'on y prend l'image qu'on a de soi pour une nature",
            "Parce que les maths ne demandent pas de conscience", "Parce que c'est une preuve de l'inconscient"], ok=1,
         voir="ex1", ex="Cette image peut changer si je change ce que je fais : c'est la mauvaise foi de celui qui se fait chose."),
    dict(q="Quelle est la difficulté propre au sujet « Peut-on se connaître soi-même ? »",
         r=["On n'a pas le temps", "Celui qui observe et celui qui est observé ne font qu'un",
            "Les autres mentent toujours", "La science l'interdit"], ok=1,
         voir="oeil", ex="Connaître suppose du recul ; or l'œil voit tout, sauf lui-même. D'où la troisième partie : se comprendre par détours."),
    dict(q="Pourquoi les quatre-vingts autoportraits de Rembrandt sont-ils un bon exemple ?",
         r=["Parce qu'il était vaniteux", "Parce que se connaître est une enquête jamais achevée",
            "Parce que la peinture est inconsciente", "Parce qu'il ne savait pas peindre autre chose"], ok=1,
         voir="rem", ex="S'il se connaissait d'un regard, un seul aurait suffi : se comprendre est un travail d'interprétation."),
    dict(q="Dans « La conscience fait-elle la dignité de l'homme ? », quel est le piège ?",
         r=["Oublier de citer Pascal", "Faire dépendre la dignité du degré de conscience, au détriment des plus fragiles",
            "Parler des animaux", "Confondre conscience et inconscient"], ok=1,
         voir="prob3", ex="Le nouveau-né ou le malade dans le coma n'ont pas moins de dignité : distinguer en fait (avoir conscience) et en droit (être une personne)."),
    dict(q="Dans le roseau pensant, pourquoi l'homme est-il plus noble que l'univers qui l'écrase ?",
         r=["Parce qu'il est plus fort", "Parce qu'il sait qu'il meurt, et l'univers n'en sait rien",
            "Parce qu'il possède des terres", "Parce qu'il est immortel"], ok=1,
         voir="qcp", ex="Pascal déplace la grandeur de la force vers la conscience : toute notre dignité consiste en la pensée."),
    dict(q="« Par l'espace, l'univers me comprend… ; par la pensée, je le comprends. » Que signifie « comprendre » ?",
         r=["Deux fois la même chose : saisir par l'esprit", "D'abord contenir, ensuite saisir par l'esprit",
            "D'abord écraser, ensuite aimer", "Rien de précis"], ok=1,
         voir="jeu", ex="Le double sens est le cœur du texte : l'univers me contient comme un point, mais je le saisis par la pensée."),
    dict(q="Quel contresens éviter sur ce texte ?",
         r=["Dire que la pensée fait la dignité", "Dire que Pascal méprise l'homme",
            "Dire que l'homme est faible", "Dire que la morale commence par bien penser"], ok=1,
         voir="pie", ex="Pascal tient les deux bouts : l'homme est misérable et grand, faible et pensant."),
]

CREDITS = [
    "Tableaux et gravures : Albert Anker, La Leçon d'écriture (XIXᵉ s.) ; Le Caravage, Narcisse (1597-1599) ; "
    "Parmigianino, Autoportrait au miroir convexe (vers 1524) ; Gustave Courbet, Le Désespéré (1843-1845) ; "
    "Rembrandt, Autoportrait à l'âge de 63 ans (1669) ; Caspar David Friedrich, Deux hommes contemplant la lune (1819-1820) ; "
    "gravure dite « de Flammarion » (1888) ; Georges de La Tour, La Madeleine à la veilleuse (vers 1640) ; "
    "Pascal, Pensées sur la religion, copie manuscrite (XVIIᵉ s.) : domaine public",
    "Photographies : magnétophone, vers 1960 (Daderot, CC0) ; Eleanor Roosevelt et la Déclaration universelle des droits de l'homme "
    "(FDR Presidential Library & Museum, CC BY 2.0) ; champ ultra-profond de Hubble (NASA, ESA, domaine public) ; "
    "roseaux (Joshua Mayer, CC BY-SA 2.0) ; salle d'examen (domaine public)",
    "Texte expliqué : Pascal, Pensées, éd. Léon Brunschvicg, fr. 347 et 348 (aussi fr. 397), Wikisource. "
    "Déclaration universelle des droits de l'homme, article 1 (1948).",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
