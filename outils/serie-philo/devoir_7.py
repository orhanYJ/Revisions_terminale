"""Le devoir, épisode 7 : « Récap »

Récapitulatif de la série (épisodes 1 à 6), même format que liberte_7.py. Formules et citations reprises des épisodes
précédents (Rousseau, Du contrat social, I, 3 ; Kant, Fondements, trad. Delbos ; Thoreau, trad. courante).
"""

CODE = "devoir-7"
NOTION = "Le devoir"
NUM = 7
TITRE = "Récap"
SUIVANT = ""
PRONONCIATION = {"Gygès": "Jijèsse", "Euthyphron": "Eutifron", "Durkheim": "Durkème", "Hume": "Hioume",
                 "Nietzsche": "Nitche", "Schuld": "Choulde", "Schulden": "Chouldenne", "Bentham": "Bentame",
                 "Thoreau": "Toro", "Eichmann": "Aïkmane", "Arendt": "Arènnte", "Régulus": "Régulusse"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="calme", carton=False, beats=[
        "{tab_vei}{q_veil}La veille de l'épreuve. Une lampe, un cahier, et une question : "
        "que faut-il vraiment retenir du devoir ?",
        "{-q_veil}{por}Souviens-toi du début. {por.1}Un portefeuille trouvé dans la rue. {por.2}Trois cents euros. "
        "{por.3}Personne ne t'a vu. Et pourtant, une petite voix : tu dois le rendre.",
        "{-por}{six}Six épisodes ont essayé de comprendre cette voix. D'où vient-elle ? Faut-il l'écouter ? "
        "Et que faire quand elle se contredit ? Une vingtaine d'auteurs, des dizaines d'exemples. "
        "Voici tout le parcours, en quelques minutes.",
        ("P", 0.3),
        "{-six}{-tab_vei}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_vei": dict(type="tableau", img="dv7-veilleuse", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.25, .5, .5],
                        legende="Georges de La Tour, La Madeleine à la veilleuse, vers 1640 (LACMA, Los Angeles)"),
        "q_veil": dict(type="question", t="Que faut-il retenir du devoir ?"),
        "por": dict(type="liste", titre="Épisode 1 · Le point de départ", items=[
            "Un portefeuille trouvé dans la rue", "Trois cents euros", "Personne ne t'a vu… « tu dois le rendre »"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "six": dict(type="mot", t="6 épisodes", g="d'où vient le devoir ? faut-il l'écouter ? quand il se contredit ?", y=270),
        "titre": dict(type="titre", sur="Le devoir · Épisode 7", t="Récap", sous="Toute la série en un épisode"),
    }),

    # ------------------------------------------------------------------ I. les fondations
    dict(id="fondations", chap="Les fondations", fond="aube", humeur="lumiere",
         notions=["la liberté", "la justice", "la religion", "la raison"],
         retenir="Une obligation, pas une contrainte. Légal ≠ légitime. Quatre voix : la société, Dieu, la conscience, la raison.",
         beats=[
        "{tab_pre}{debere}D'abord, le mot. Devoir vient du latin debere : tenir quelque chose d'un autre. "
        "Avoir un devoir, c'est être en dette.",
        "{-debere}{oc}Et une obligation n'est pas une contrainte. {oc.g}Le brigand me force. {oc.d}Le feu rouge m'oblige : "
        "il s'adresse à ma volonté. Seul un être capable de choisir peut avoir des devoirs. "
        "Le devoir suppose la {#la liberté}liberté.",
        "{-oc}{-tab_pre}{rousseau}Rousseau le résume en une phrase.",
        ("C", "Convenons donc que force ne fait pas droit, et qu'on n'est obligé d'obéir qu'aux puissances légitimes.", "c_rous"),
        "{-rousseau}{-c_rous}{tab_the}{devs}Trois sortes de devoirs, que distingue la sanction. "
        "{devs.1}Juridiques : l'État punit. {devs.2}Sociaux : le regard des autres. {devs.3}Moraux : le remords.",
        "{-devs}{ll}Et un repère capital. {ll.g}Le légal, conforme à la loi. {ll.d}Le légitime, conforme à la justice. "
        "Une loi peut être légale… sans être juste.",
        "{-ll}{-tab_the}{tab_gyg}{gyg}Puis la question de Gygès : serions-nous honnêtes si nous étions invisibles ? "
        "Glaucon répond non : nous ne serions justes que par peur d'être pris.",
        "{-gyg}{-tab_gyg}{tab_moi}{voix}Alors, d'où vient le devoir ? Quatre voix. {voix.1}La société : pour Durkheim, "
        "le devoir est un fait social, appris par l'éducation. Mais les mœurs varient : vérité en deçà des Pyrénées, erreur au-delà.",
        "{voix.2}Dieu et ses commandements. Mais le dilemme de l'Euthyphron demande : le bien est-il bien parce que Dieu "
        "l'ordonne, ou Dieu l'ordonne-t-il parce qu'il est bien ? La {#la religion}religion ne suffit pas à fonder le devoir.",
        "{voix.3}La conscience, que Rousseau appelle un « instinct divin ». Mais une conscience peut être faussée.",
        "{voix.4}La raison, enfin, la même en chacun : seule une loi que je peux vouloir pour tous fonde vraiment le devoir. "
        "Et Hume rappelle qu'on ne tire jamais un « tu dois » d'un simple « c'est ainsi ».",
        "{-voix}{-tab_moi}",
    ], vis={
        "tab_pre": dict(type="tableau", img="dv1-preteur", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .55],
                        legende="Quentin Metsys, Le Prêteur et sa femme, 1514 (musée du Louvre)"),
        "debere": dict(type="mot", t="DEBERE", g="latin : devoir · tenir quelque chose d'un autre", y=250, taille=104),
        "oc": dict(type="cols", g="Contrainte", gq="le brigand : la force agit sur moi", d="Obligation",
                   dq="le feu rouge : je peux désobéir", vs="≠", repere="Repère · obligation / contrainte"),
        "rousseau": dict(type="portrait", annee=1712, legende="Du contrat social (1762)", img="rousseau",
                         nom="Jean-Jacques Rousseau", dates="1712 – 1778", x=110, y=120, w=330, h=420),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 3 (1762)", x=640, y=170, w=570),
        "tab_the": dict(type="tableau", img="dv1-themis", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Thémis, déesse de la justice, Hong Kong (photo ChvhLR10, CC BY-SA 3.0)"),
        "devs": dict(type="liste", titre="Épisode 1 · Trois devoirs, trois sanctions", items=[
            "Juridiques : la sanction de l'État", "Sociaux : le regard des autres", "Moraux : le remords"],
                     marques=["1", "2", "3"], x=170, y=170, w=940),
        "ll": dict(type="cols", g="Légal", gq="conforme à la loi", d="Légitime", dq="conforme à la justice",
                   vs="≠", repere="Repère · légal / légitime"),
        "tab_gyg": dict(type="tableau", img="dv2-gyges", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Anonyme, L'Anneau de Gygès, Ferrare, XVIᵉ siècle"),
        "gyg": dict(type="question", t="Serions-nous honnêtes si nous étions invisibles ?"),
        "tab_moi": dict(type="tableau", img="dv2-moise", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="Rembrandt, Moïse brisant les tables de la Loi, 1659 (Gemäldegalerie, Berlin)"),
        "voix": dict(type="liste", titre="Épisode 2 · Quatre voix qui disent « tu dois »", items=[
            "La société : un fait social (Durkheim) · les mœurs varient (Pascal)",
            "Dieu : les commandements · le dilemme de l'Euthyphron",
            "La conscience : « instinct divin » (Rousseau) · mais faillible",
            "La raison : vouloir pour tous (Kant) · être ≠ devoir être (Hume)"],
                     marques=["1", "2", "3", "4"], x=170, y=130, w=940),
    }),

    # ------------------------------------------------------------------ III. Kant
    dict(id="kant", chap="Le devoir selon Kant", fond="aube", humeur="lumiere", notions=["la raison", "la vérité"],
         retenir="Kant : agir par devoir, pas seulement conformément au devoir. L'impératif catégorique : universaliser sa maxime, respecter l'humanité.",
         beats=[
        "{kant}{tab_epi}C'est la voix de la {#la raison}raison, celle de Kant. Pour lui, rien n'est bon sans restriction, "
        "sauf une bonne volonté. On juge l'intention, pas le résultat.",
        "{-kant}{dist}Souviens-toi du marchand qui rend la monnaie exacte à un enfant. {dist.g}Il agit conformément au devoir… "
        "{dist.d}mais par intérêt, non par devoir. Son action est correcte ; elle n'a pas de valeur morale. "
        "Agir par devoir, c'est agir par respect pour la loi : le seul sentiment moral, selon Kant.",
        "{-dist}{-tab_epi}{tab_hor}{imp}Le devoir commande sans condition : c'est l'impératif catégorique. "
        "Kant le formule ainsi.{-imp}",
        ("C", "Agis uniquement d'après la maxime qui fait que tu peux vouloir en même temps qu'elle devienne une loi universelle.",
         "c_ic"),
        "{-c_ic}{form}Et sa seconde formule : {form.1}traiter l'humanité, en moi et en autrui, toujours en même temps comme une fin, "
        "jamais simplement comme un moyen. {form.2}Car les choses ont un prix ; les personnes, une dignité.",
        "{-form}{con}Enfin, le mensonge. Benjamin Constant défend le droit de mentir à l'assassin ; Kant le refuse, "
        "au risque du rigorisme. « Le kantisme a les mains pures, mais il n'a pas de mains », dira Péguy.",
        "{-con}{-tab_hor}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Fondements de la métaphysique des mœurs (1785)", x=110, y=120, w=330, h=420),
        "tab_epi": dict(type="tableau", img="dv3-epicerie", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .4],
                        legende="Gerrit Dou, L'Épicière de village, 1647 (musée du Louvre)"),
        "dist": dict(type="cols", g="Conformément au devoir", gq="l'action est correcte : le marchand intéressé",
                     d="Par devoir", dq="le motif est moral : agir parce qu'on le doit", vs="≠",
                     repere="Repère · par devoir / conformément au devoir"),
        "tab_hor": dict(type="tableau", img="dv3-horaces", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .4],
                        legende="Jacques-Louis David, Le Serment des Horaces, 1784 (musée du Louvre)"),
        "imp": dict(type="mot", t="L'impératif catégorique", g="« fais », sans condition · ≠ « si tu veux…, fais… »", y=260, taille=72),
        "c_ic": dict(type="cit", a="Kant", o="Fondements de la métaphysique des mœurs, section II (1785), trad. Delbos",
                     x=170, y=170, w=940),
        "form": dict(type="liste", titre="Épisode 3 · L'humanité comme fin", items=[
            "Toujours en même temps comme une fin, jamais simplement comme un moyen",
            "Les choses ont un prix, les personnes une dignité"], marques=["1", "2"], cles=["simplement", "dignité"],
                     x=170, y=180, w=940),
        "con": dict(type="note", titre="Le droit de mentir ? (1797)", cles=["rigorisme"],
                    t="Constant : la vérité n'est due qu'à ceux qui y ont droit. Kant : aucun droit de mentir. L'objection : le rigorisme."),
    }),

    # ------------------------------------------------------------------ IV. les critiques
    dict(id="critiques", chap="Contre le devoir", fond="nuit", humeur="tension",
         notions=["l'inconscient", "le bonheur", "la conscience"],
         retenir="Nietzsche : la faute vient de la dette. Freud : le surmoi. Utilitarisme : les conséquences. Épicure, Aristote : le bonheur.",
         beats=[
        "{tab_shy}{att}Puis vinrent les attaques. {att.1}Nietzsche : en allemand, Schuld, la faute, vient de Schulden, les dettes. "
        "Et la mauvaise conscience, c'est l'agressivité retournée contre soi. Face au dragon « Tu dois », "
        "l'esprit libre, le lion, répond : « Je veux ».",
        "{-tab_shy}{tab_div}{att.2}Freud : le devoir parle par la voix du surmoi, les interdits des parents devenus "
        "{#l'inconscient}inconscients. Une garnison placée dans une ville conquise.",
        "{-tab_div}{tab_aig}{att.3}Les utilitaristes, Bentham et Mill : une action vaut par ses conséquences, le plus grand "
        "bonheur du plus grand nombre. Mill précise : mieux vaut être Socrate insatisfait qu'un imbécile satisfait. "
        "Et le dilemme du tramway en montre les limites.",
        "{-tab_aig}{tab_oli}{att.4}Et les sages grecs. Pour Épicure et Aristote, la vraie question n'est pas « que dois-je faire ? », "
        "mais « comment vivre heureux ? ».",
        ("Le devoir n'est pas mort. Mais on ne peut plus dire « tu dois » sans se demander qui parle.", {"rate": "-5%"}),
        "{-att}{-tab_oli}",
    ], vis={
        "tab_shy": dict(type="tableau", img="dv4-shylock", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Gilbert Stuart Newton, Shylock et Jessica, 1830"),
        "att": dict(type="liste", titre="Épisode 4 · Quatre attaques", items=[
            "Nietzsche : la faute vient de la dette",
            "Freud : le surmoi, une garnison intérieure",
            "Bentham, Mill : juger par les conséquences",
            "Épicure, Aristote : la question du bonheur"], marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "tab_div": dict(type="tableau", img="dv4-divan", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Le divan de Freud, Freud Museum, Londres (photo Marcelo, domaine public)"),
        "tab_aig": dict(type="tableau", img="dv4-aiguillage", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .5],
                        legende="Levier d'aiguillage (photo W. Carter, domaine public)"),
        "tab_oli": dict(type="tableau", img="dv4-oliviers", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Oliveraie à Paxos, au lever du soleil (photo Jess Stubenbord, CC0)"),
    }),

    # ------------------------------------------------------------------ V. les conflits
    dict(id="conflits", chap="Conflits de devoirs", fond="aube", humeur="tension", notions=["la justice", "l'État"],
         retenir="Antigone : le bien contre le bien. Désobéir à une loi injuste : publiquement, sans violence. Obéir n'excuse pas.",
         beats=[
        "{tab_dio}{ant}Et quand deux devoirs se contredisent ? Antigone enterre son frère malgré le décret du roi Créon, "
        "au nom des lois non écrites des dieux. Mais Créon, lui aussi, défend un devoir : l'ordre de la cité. "
        "Hegel y voit le tragique : le bien contre le bien.",
        "{-ant}{-tab_dio}{tab_par}{thoreau}Puis la désobéissance civile. Thoreau l'écrit.",
        ("C", "Je pense que nous devons être hommes d'abord, et sujets ensuite.", "c_tho"),
        "{-thoreau}{-c_tho}{dc}Rosa Parks, Martin Luther King : désobéir à une loi injuste, {dc.1}mais publiquement, sans violence, "
        "et en acceptant la sanction. Au nom de la {#la justice}justice, non de son intérêt. "
        "Mais Socrate, lui, refuse de s'évader de sa prison : on ne détruit pas les lois à la légère.",
        "{-dc}{-tab_par}{tab_nur}{ban}Et l'inverse : Eichmann, qui disait avoir fait son devoir. Hannah Arendt parle de la "
        "banalité du mal : obéir sans penser. {ban.1}Obéir n'est pas faire son devoir.",
        "{-ban}{-tab_nur}{jug}Quand aucune règle ne tranche, comme pour le jeune homme de Sartre, il faut juger. "
        "En tenant ensemble, dit Weber, la conviction et la responsabilité.",
        "{-jug}",
    ], vis={
        "tab_dio": dict(type="tableau", img="dv5-diotti", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Giuseppe Diotti, Antigone condamnée à mort par Créon, 1845"),
        "ant": dict(type="cols", g="Le décret de Créon", gq="la loi de la cité", d="Les lois non écrites",
                    dq="le devoir envers les morts", vs="↔", repere="Hegel · le bien contre le bien"),
        "tab_par": dict(type="tableau", img="dv5-parks", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Rosa Parks au bureau du shérif, Montgomery, 1956 (photo Gene Herrick, AP, domaine public)"),
        "thoreau": dict(type="portrait", annee=1817, img="thoreau", nom="Henry David Thoreau", dates="1817 – 1862",
                        legende="La Désobéissance civile (1849)", x=110, y=120, w=330, h=420),
        "c_tho": dict(type="cit", a="Thoreau", o="La Désobéissance civile (1849), trad. courante", x=640, y=170, w=570),
        "dc": dict(type="def", cles=["publiquement", "sanction"], terme="La désobéissance civile",
                   t="Désobéir à une loi injuste, au nom de la justice.",
                   etape="Publiquement, sans violence, en acceptant la sanction.", x=170, y=200, w=940),
        "tab_nur": dict(type="tableau", img="dv5-nuremberg", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Le banc des accusés au procès de Nuremberg, 1945-1946 (photo Ray D'Addario, domaine public)"),
        "ban": dict(type="def", cles=["sans penser"], terme="La banalité du mal · Arendt (1963)",
                    t="Eichmann « faisait son devoir » : il obéissait sans penser.",
                    etape="Obéir n'est pas faire son devoir.", x=170, y=200, w=940),
        "jug": dict(type="cols", g="Conviction", gq="rester fidèle à ses principes", d="Responsabilité",
                    dq="répondre des conséquences", vs="+", repere="Weber · juger quand aucune règle ne tranche"),
    }),

    # ------------------------------------------------------------------ VI. le jour J
    dict(id="jourj", chap="Le jour J", fond="nuit", humeur="lumiere",
         retenir="Définir, problématiser, distinguer pour dépasser. Une idée, un auteur, un exemple précis.", beats=[
        "{tab_med}{meth}Le jour J. {meth.1}Définir chaque mot du sujet. {meth.2}Problématiser : une tension, pas une reformulation. "
        "{meth.3}Construire trois parties, dont la dernière déplace la question grâce à une distinction. "
        "{meth.4}Et pour l'explication : six éléments d'introduction, puis quoi, comment, pourquoi.",
        "Ton introduction ? Une scène précise, l'analyse des mots, la problématique, le plan. "
        "Ta conclusion ? Un bilan, une réponse nette, et, si tu veux, une ouverture.",
        "{-meth}{suj}Des sujets qui reviennent. {suj.1}Faire son devoir, est-ce renoncer à sa liberté ? "
        "{suj.2}Le devoir peut-il s'opposer au bonheur ? {suj.3}Doit-on toujours obéir aux lois ? "
        "{suj.4}La morale est-elle affaire de sentiment ou de raison ?",
        "{-suj}{ex}Et des exemples précis : le portefeuille, Gygès, le marchand, Régulus, Antigone, Rosa Parks, Eichmann, le tramway.",
        "{-ex}{-tab_med}{piege}Le piège : réciter Kant contre Nietzsche sans répondre à la question. "
        "Un auteur est un outil pour penser, pas un argument d'autorité.",
        "{-piege}",
    ], vis={
        "tab_med": dict(type="tableau", img="dv7-meditation", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .45, .5],
                        legende="Rembrandt, Philosophe en méditation, 1632 (musée du Louvre)"),
        "meth": dict(type="liste", titre="Épisode 6 · Le jour de l'épreuve", items=[
            "Définir chaque mot du sujet", "Problématiser : une tension",
            "Trois parties : la dernière déplace la question", "Explication : six éléments, puis quoi · comment · pourquoi"],
                     marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "suj": dict(type="liste", titre="Des sujets qui reviennent", items=[
            "Faire son devoir, est-ce renoncer à sa liberté ?", "Le devoir peut-il s'opposer au bonheur ?",
            "Doit-on toujours obéir aux lois ?", "La morale est-elle affaire de sentiment ou de raison ?"],
                    marques=["?", "?", "?", "?"], x=170, y=150, w=940),
        "ex": dict(type="nuage", items=["le portefeuille", "Gygès", "le marchand", "Régulus", "Antigone", "Rosa Parks",
                                        "Eichmann", "le tramway"]),
        "piege": dict(type="note", titre="Le piège", cles=["outil"],
                      t="Réciter Kant contre Nietzsche sans répondre à la question. Un auteur est un outil pour penser."),
    }),

    # ------------------------------------------------------------------ VII. fin
    dict(id="fin", chap="Toute la notion", fond="nuit", humeur="lumiere", beats=[
        "{rec}Voici toute la notion, sur une seule carte. {rec.1}Les fondations : le mot, l'obligation, les trois devoirs. "
        "{rec.2}Les sources : la société, Dieu, la conscience, la raison. {rec.3}Kant, et ses adversaires. "
        "{rec.4}Les conflits de devoirs, et le jugement.",
        "{-rec}{frise}Et voici ceux qui t'ont accompagné, de Sophocle à Hannah Arendt : vingt-cinq siècles de pensée.",
        "{-frise}{trois}Si tu ne dois garder que trois phrases : {trois.1}Rousseau, force ne fait pas droit. "
        "{trois.2}Kant, traite l'humanité toujours comme une fin, jamais simplement comme un moyen. "
        "{trois.3}Et Martin Luther King : on a la responsabilité morale de désobéir aux lois injustes.",
        ("Un dernier mot. Le devoir n'est pas seulement un sujet de dissertation. C'est cette petite voix, devant le portefeuille, "
         "quand personne ne te voit. Tu sais maintenant l'interroger.", {"rate": "-5%"}),
        ("Demain, devant ta copie, fais ton devoir. Bonne chance.", {"rate": "-6%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-trois}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE DEVOIR", branches=[
            dict(t="Les fondations", items=["debere : la dette", "obligation ≠ contrainte", "légal / légitime"]),
            dict(t="Les sources", items=["société (Durkheim)", "Dieu (Euthyphron)", "conscience (Rousseau)", "raison (Kant)"]),
            dict(t="Kant et ses adversaires", items=["par devoir ≠ conformément", "Nietzsche, Freud", "Bentham, Mill, Épicure"]),
            dict(t="Les conflits", items=["Antigone", "désobéissance civile", "Arendt : obéir n'excuse pas"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Sophocle", d=-496, img="sophocle"), dict(nom="Platon", d=-428, img="platon"),
            dict(nom="Aristote", d=-384, img="aristote"), dict(nom="Épicure", d=-341, img="epicure"),
            dict(nom="Hume", d=1711, img="hume"), dict(nom="Rousseau", d=1712, img="rousseau"),
            dict(nom="Kant", d=1724, img="kant"), dict(nom="Bentham", d=1748, img="bentham"),
            dict(nom="Mill", d=1806, img="mill"), dict(nom="Thoreau", d=1817, img="thoreau"),
            dict(nom="Nietzsche", d=1844, img="nietzsche"), dict(nom="Freud", d=1856, img="freud"),
            dict(nom="Durkheim", d=1858, img="durkheim"), dict(nom="Sartre", d=1905, img="sartre"),
            dict(nom="Arendt", d=1906, img="arendt"), dict(nom="King", d=1929, img="king")]),
        "trois": dict(type="liste", titre="Trois phrases à garder", items=[
            "« Force ne fait pas droit » · Rousseau",
            "« Jamais simplement comme un moyen » · Kant",
            "Désobéir aux lois injustes, une responsabilité morale · Martin Luther King"], marques=["1", "2", "3"],
                      x=170, y=170, w=940),
        "tab_fin": dict(type="tableau", img="dv7-temeraire", fond=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="J. M. W. Turner, Le Dernier Voyage du Téméraire, 1839 (National Gallery, Londres)"),
        "fin": dict(type="titre", sur="Le devoir", t="Fin de la série", sous="Six épisodes et un récap · bonne épreuve !"),
    }),
]

QUIZ = [
    dict(q="De quel mot latin vient « devoir » ?",
         r=["Officium", "Debere : tenir quelque chose d'un autre", "Lex", "Virtus"], ok=1,
         voir="debere", ex="Avoir un devoir, c'est être en dette : le même verbe dit « devoir de l'argent » et « devoir faire » (épisode 1)."),
    dict(q="Une loi de ségrégation est…",
         r=["légale et légitime", "légale mais illégitime", "illégale mais légitime", "ni légale ni légitime"], ok=1,
         voir="ll", ex="Conforme à la loi de l'époque, mais contraire à la justice. Repère : légal / légitime."),
    dict(q="Que montre le dilemme de l'Euthyphron ?",
         r=["Que Dieu n'existe pas", "Que le commandement divin seul ne suffit pas à fonder le bien",
            "Que la société fonde la morale", "Que la conscience ne se trompe jamais"], ok=1,
         voir="voix", ex="Si Dieu ordonne le bien parce qu'il est bien, le bien ne dépend pas de lui ; sinon, le devoir est arbitraire (épisode 2)."),
    dict(q="Le marchand qui ne trompe pas l'enfant par intérêt agit…",
         r=["par devoir", "conformément au devoir", "contre le devoir", "par pitié"], ok=1,
         voir="dist", ex="Action correcte, motif intéressé : pas de valeur morale (Kant, Fondements, section I)."),
    dict(q="Pour Nietzsche, d'où vient l'idée de faute ?",
         r=["De la raison", "De la dette (Schuld / Schulden)", "De la pitié", "Du contrat social"], ok=1,
         voir="att", ex="Généalogie de la morale, II : la faute dérive de la dette ; la mauvaise conscience, c'est l'agressivité retournée contre soi."),
    dict(q="Un utilitariste juge une action…",
         r=["par l'intention", "par ses conséquences", "par la loi", "par la tradition"], ok=1,
         voir="att", ex="Bentham, Mill : le plus grand bonheur du plus grand nombre. Kant, lui, juge l'intention."),
    dict(q="La désobéissance civile se fait…",
         r=["en secret", "publiquement, sans violence, en acceptant la sanction", "par la force", "pour son intérêt"], ok=1,
         voir="dc", ex="Thoreau, Rosa Parks, Martin Luther King : au nom de la justice (épisode 5)."),
    dict(q="Que veut dire Arendt avec la « banalité du mal » ?",
         r=["Que le mal est rare", "Qu'on peut faire le mal en obéissant sans penser",
            "Que le mal est toujours monstrueux", "Que la loi excuse tout"], ok=1,
         voir="ban", ex="Eichmann « faisait son devoir » : obéir n'est pas faire son devoir."),
]

CREDITS = [
    "Portraits : voir les épisodes 1 à 6",
    "Tableaux : Georges de La Tour, La Madeleine à la veilleuse (vers 1640) ; Quentin Metsys, Le Prêteur et sa femme (1514) ; "
    "L'Anneau de Gygès (Ferrare, XVIᵉ s.) ; Rembrandt, Moïse brisant les tables de la Loi (1659) et Philosophe en méditation (1632) ; "
    "Gerrit Dou, L'Épicière de village (1647) ; Jacques-Louis David, Le Serment des Horaces (1784) ; "
    "Gilbert Stuart Newton, Shylock et Jessica (1830) ; Giuseppe Diotti, Antigone condamnée à mort par Créon (1845) ; "
    "J. M. W. Turner, Le Dernier Voyage du Téméraire (1839) : domaine public",
    "Photographies : Thémis, Hong Kong (ChvhLR10, CC BY-SA 3.0) ; divan de Freud (Marcelo, domaine public) ; levier d'aiguillage "
    "(W. Carter, domaine public) ; oliveraie à Paxos (Jess Stubenbord, CC0) ; Rosa Parks (Gene Herrick, AP, domaine public) ; "
    "procès de Nuremberg (Ray D'Addario, domaine public)",
    "Citations : Rousseau, Du contrat social, I, 3 (1762) ; Kant, Fondements de la métaphysique des mœurs (1785), trad. Delbos ; "
    "Thoreau, La Désobéissance civile (1849), trad. courante",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
