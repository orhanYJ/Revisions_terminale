"""Le bonheur, épisode 7 : « Récap »

Récapitulatif de la série (épisodes 1 à 6), même format que devoir_7.py. Formules et citations reprises des épisodes
précédents : Épicure, Lettre à Ménécée, 128, trad. Hamelin (1910) ; Saint-Just, rapport du 3 mars 1794 ;
Pascal, Pensées, fr. 172 (éd. Brunschvicg) ; Kant, Critique de la raison pratique (1788), trad. Barni.
"""

CODE = "bonheur-7"
NOTION = "Le bonheur"
NUM = 7
TITRE = "Récap"
SUIVANT = ""
PRONONCIATION = {"Aristippe": "Aristipe", "Calliclès": "Kaliklèsse", "Schopenhauer": "Chopenaouère", "Huxley": "Euksslé",
                 "Tocqueville": "Tokvil", "Nozick": "Nozik", "Karamazov": "Karamazof", "Bentham": "Bentame", "Cinéas": "Sinéasse",
                 "Pyrrhus": "Pirusse", "Ménécée": "Ménéssé"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="calme", carton=False, beats=[
        "{tab_bou}{q_veil}La veille de l'épreuve. Une bougie, un cahier, et une question : "
        "que faut-il vraiment retenir du bonheur ?",
        "{-q_veil}{lot}Souviens-toi du début. {lot.1}Un ticket de loterie, un mardi soir. {lot.2}Des millions. "
        "{lot.3}Et une certitude : cette fois, je vais être heureux.",
        "{-lot}{six}Six épisodes ont interrogé cette certitude. Le plaisir suffit-il ? La sagesse s'apprend-elle ? "
        "Le bonheur n'est-il qu'un mirage ? Et qui doit s'en charger ? Voici tout le parcours, en quelques minutes.",
        ("P", 0.3),
        "{-six}{-tab_bou}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_bou": dict(type="tableau", img="bh7-bougie", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Godfried Schalcken, Homme à la chandelle, vers 1695-1700"),
        "q_veil": dict(type="question", t="Que faut-il retenir du bonheur ?"),
        "lot": dict(type="liste", titre="Épisode 1 · Le point de départ", items=[
            "Un ticket de loterie, un mardi soir", "Des millions", "« Cette fois, je vais être heureux »"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "six": dict(type="mot", t="6 épisodes", g="le plaisir ? la sagesse ? un mirage ? l'affaire de qui ?", y=270),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 7", t="Récap", sous="Toute la série en un épisode"),
    }),

    # ------------------------------------------------------------------ I. le mot et le plaisir
    dict(id="plaisir", chap="Le mot et le plaisir", fond="aube", humeur="lumiere", notions=["le temps", "la raison"],
         retenir="Le bonheur : la fin dernière, que tous veulent, mais que personne ne sait définir. Épicure : un plaisir en repos, obtenu en triant ses désirs.",
         beats=[
        "{tab_for}{mot}D'abord, le mot. Bonheur : bon heur, la bonne chance. Les Grecs disaient eudaimonia, avoir un bon génie ; "
        "les chrétiens, béatitude. La chance, la vie réussie, la plénitude : trois visages.",
        "{-mot}{dist}Puis les distinctions. {dist.1}Le plaisir dure un instant. {dist.2}La joie, un moment. "
        "{dist.3}Le bonheur se mesure à l'échelle d'une vie : il demande du {#le temps}temps. "
        "{dist.4}Et le repère objectif, subjectif : se sentir heureux, est-ce avoir une vie heureuse ? "
        "Et Nozick le montre : presque personne n'accepterait de vivre branché sur une machine à bonheur. Nous voulons que ce soit vrai.",
        "{-dist}{-tab_for}{arist}{tab_ath}Pour Aristote, le bonheur est la fin dernière : ce qu'on veut pour lui-même, "
        "jamais pour autre chose. Pascal : tous les hommes recherchent d'être heureux. "
        "Mais Kant prévient : c'est un idéal, non de la raison, mais de l'imagination.",
        "{-arist}{-tab_ath}{tab_gau}{hed}Le plaisir rend-il heureux ? {hed.1}Aristippe jouit de l'instant, sans se laisser posséder. "
        "{hed.2}Épicure trie ses désirs : naturels et nécessaires, naturels seulement, vains. "
        "{hed.3}Et son vrai plaisir est en repos : l'aponie du corps, l'ataraxie de l'âme.{-hed}",
        ("C", "C'est pourquoi nous disons que le plaisir est le commencement et la fin de la vie heureuse.", "c_epi"),
        "{-c_epi}{-tab_gau}{tab_dan}{ton}Contre lui, Calliclès veut des désirs immenses ; Socrate lui oppose les tonneaux percés. "
        "{ton.1}Et Mill : mieux vaut être Socrate insatisfait qu'un imbécile satisfait. Le bonheur se dérobe quand on le vise.",
        "{-ton}{-tab_dan}",
    ], vis={
        "tab_for": dict(type="tableau", img="bh1-fortune", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="La roue de la Fortune, d'après l'Hortus deliciarum d'Herrade de Landsberg (XIIᵉ s.)"),
        "mot": dict(type="mot", t="BON HEUR", g="la chance · eudaimonia · beatitudo", y=250, taille=104),
        "dist": dict(type="liste", titre="Épisode 1 · Ne pas tout confondre", items=[
            "Le plaisir : un instant", "La joie : un moment", "Le bonheur : toute une vie",
            "Repère · objectif / subjectif"], marques=["1", "2", "3", "✻"], x=170, y=140, w=940),
        "arist": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      legende="Éthique à Nicomaque", x=110, y=120, w=330, h=420),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.5, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 · au centre, Platon et Aristote"),
        "tab_gau": dict(type="tableau", img="bh2-gaufrettes", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Lubin Baugin, Le Dessert de gaufrettes, v. 1630-1635 (musée du Louvre ; photo Sailko, CC BY 3.0)"),
        "hed": dict(type="liste", titre="Épisode 2 · Le plaisir", items=[
            "Aristippe : le plaisir de l'instant", "Épicure : trier ses désirs",
            "Le plaisir en repos : aponie, ataraxie"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "c_epi": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 128, trad. Hamelin (1910)", x=170, y=200, w=940),
        "tab_dan": dict(type="tableau", img="t-danaides", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.25, .5, .6],
                        legende="John William Waterhouse, Les Danaïdes, 1906 · condamnées à remplir sans fin des jarres percées"),
        "ton": dict(type="cols", g="Calliclès", gq="des désirs immenses… des tonneaux percés", d="Mill",
                    dq="Socrate insatisfait plutôt qu'un imbécile satisfait", vs="≠"),
    }),

    # ------------------------------------------------------------------ II. la sagesse des Anciens
    dict(id="sagesse", chap="La sagesse des Anciens", fond="nuit", humeur="calme", notions=["la raison", "la nature", "la liberté"],
         retenir="Aristote : le bonheur est une activité conforme à la vertu, dans une vie complète. Stoïciens : la vertu suffit. Spinoza : la joie.",
         beats=[
        "{tab_cre}{sol}Puis vint la sagesse des Anciens. Souviens-toi de Crésus sur son bûcher, appelant Solon : "
        "ne dis personne heureux avant sa mort.",
        "{-sol}{-tab_cre}{arist2}{tab_hir}Pour Aristote, le bonheur n'est pas un trésor qu'on possède, mais une activité : "
        "l'activité de l'âme conforme à la vertu, dans une vie complète. Une hirondelle ne fait pas le printemps.",
        "{-arist2}{sag}{sag.1}La vertu s'acquiert par l'habitude : c'est en pratiquant la justice qu'on devient juste. "
        "Elle vise un juste milieu, un sommet entre deux pentes. Bien vivre, c'est vivre selon la {#la raison}raison. "
        "{sag.2}Le bonheur demande des amis, et culmine dans la vie de l'esprit. "
        "{sag.3}Les stoïciens vont plus loin : la vertu suffit. Épictète conseille de ne pas demander que les choses arrivent "
        "comme on le veut, mais de les vouloir comme elles arrivent. Marc Aurèle se retire dans sa citadelle intérieure. "
        "{sag.4}Et Spinoza fait de la joie le passage à une plus grande perfection.{-sag}",
        ("C", "La béatitude n'est pas le prix de la vertu, c'est la vertu elle-même.", "c_spi"),
        "{-c_spi}{-tab_hir}{tab_rir}{deb}Reste le grand débat antique. {deb.g}Pour les stoïciens, la vertu suffit. "
        "{deb.d}Pour Aristote, il faut aussi un peu de chance : nul ne dirait heureux le vieux Priam.",
        "{-deb}{-tab_rir}",
    ], vis={
        "tab_cre": dict(type="tableau", img="bh3-cresus", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Gaspar van den Hoecke, Crésus montrant ses trésors à Solon, XVIIᵉ s. (Musée national, Varsovie)"),
        "sol": dict(type="question", t="Ne dis personne heureux avant sa mort."),
        "arist2": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                       legende="Éthique à Nicomaque, I, 7", x=110, y=120, w=330, h=420),
        "tab_hir": dict(type="tableau", img="bh3-hirondelle", fond=True, sombre=True, de=[1.0, .5, .7], a=[1.4, .5, .78],
                        legende="Hirondelles, planche de la Naturgeschichte der Vögel Deutschlands de J. A. Naumann, XIXᵉ s. (domaine public)"),
        "sag": dict(type="liste", titre="Épisode 3 · La sagesse des Anciens", items=[
            "Aristote : la vertu, une habitude, un juste milieu", "Des amis, et la vie de l'esprit",
            "Les stoïciens : la vertu suffit, la citadelle intérieure", "Spinoza : la joie"],
                    marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "c_spi": dict(type="cit", a="Spinoza", o="Éthique, V, proposition 42 (1677), trad. Saisset", x=170, y=220, w=940),
        "tab_rir": dict(type="tableau", img="bh3-rire", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Frans Hals, Garçon riant, v. 1625 (Mauritshuis, La Haye)"),
        "deb": dict(type="cols", g="Les stoïciens", gq="la vertu suffit : plus libre", d="Aristote",
                    dq="il faut aussi un peu de chance : plus humain", vs="≠"),
    }),

    # ------------------------------------------------------------------ III. une illusion ?
    dict(id="illusion", chap="Une illusion ?", fond="nuit", humeur="tension", notions=["la conscience", "l'inconscient"],
         retenir="Pascal, Schopenhauer, Rousseau, Freud : le bonheur-état est une illusion. Reste le bonheur-activité, qui se construit.",
         beats=[
        "{tab_cham}{ill}Puis vint le soupçon. Souviens-toi de Pyrrhus : Rome, la Sicile, Carthage… et ensuite, le repos. "
        "Qu'est-ce qui l'empêchait de se reposer tout de suite ? {ill.1}Pascal : nous fuyons dans le divertissement ; nous aimons la chasse, non la prise. "
        "{ill.2}Schopenhauer : la vie oscille comme un pendule, de la souffrance à l'ennui. "
        "{ill.3}Rousseau : on n'est heureux qu'avant d'être heureux. "
        "{ill.4}Freud : le bonheur n'est qu'un épisode ; il n'est pas prévu par le plan de la Création, "
        "et la souffrance nous menace par le corps, par le monde, par les autres.{-ill}",
        ("C", "Ainsi nous ne vivons jamais, mais nous espérons de vivre ; et, nous disposant toujours à être heureux, "
              "il est inévitable que nous ne le soyons jamais.", "c_pas"),
        "{-c_pas}{-tab_cham}{tab_roue}{adap}Et les psychologues ? Les gagnants du loto ne se disent pas beaucoup plus heureux "
        "que les autres. Mais l'étude est petite, et l'adaptation n'est pas totale.",
        "{-adap}{etat}La réponse : {etat.g}le bonheur comme état, complet et définitif, est sans doute une illusion. "
        "{etat.d}Le bonheur comme activité, lui, se construit. Alain le disait : le pessimisme est d'humeur ; "
        "l'optimisme est de volonté.",
        "{-etat}{-tab_roue}",
    ], vis={
        "tab_cham": dict(type="tableau", img="bh4-chambre", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .5],
                         legende="Vilhelm Hammershøi, Intérieur, Strandgade 30, 1900"),
        "ill": dict(type="liste", titre="Épisode 4 · Quatre soupçons", items=[
            "Pascal : le divertissement", "Schopenhauer : le pendule", "Rousseau : heureux avant d'être heureux",
            "Freud : un bonheur épisodique"], marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "c_pas": dict(type="cit", a="Pascal", o="Pensées, fr. 172 (éd. Brunschvicg)", x=170, y=170, w=940),
        "tab_roue": dict(type="tableau", img="bh4-roue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                         legende="Hamster dans sa roue (photo Rlicul, CC BY-SA 3.0)"),
        "adap": dict(type="note", titre="L'adaptation hédonique", cles=["petite", "totale"],
                     t="Les gagnants du loto ne se disent pas beaucoup plus heureux. Mais l'étude est petite, et l'adaptation n'est pas totale.",
                     x=170, y=200, w=940),
        "etat": dict(type="cols", g="Le bonheur-état", gq="complet, définitif : une illusion", d="Le bonheur-activité",
                     dq="il se construit, il se veut (Alain)", vs="≠"),
    }),

    # ------------------------------------------------------------------ IV. morale et politique
    dict(id="politique", chap="Morale et politique", fond="aube", humeur="lumiere", notions=["le devoir", "l'État", "la liberté"],
         retenir="Kant : se rendre digne du bonheur. L'État ne doit pas faire notre bonheur, mais en garantir les conditions.",
         beats=[
        "{kant}{tab_dec}Le bonheur peut-il fonder la morale ? Kant répond non : la morale ne nous apprend pas à nous rendre heureux, "
        "mais à nous rendre dignes du bonheur.",
        "{-kant}{pol}{pol.1}L'utilitarisme en fait pourtant le critère des lois : le plus grand bonheur du plus grand nombre. "
        "{pol.2}Mais Ivan Karamazov demande : peut-on bâtir le bonheur sur les larmes d'un seul enfant ? "
        "{pol.3}En 1776, l'Amérique proclame le droit de rechercher le bonheur ; en 1794, Saint-Just lance sa formule.{-pol}",
        ("C", "Le bonheur est une idée neuve en Europe.", "c_sj"),
        "{-c_sj}Quelques mois plus tard, en pleine Terreur, il est guillotiné. {pat}Kant, lui, refuse le gouvernement paternel. Tocqueville redoute un pouvoir immense et tutélaire, qui veut être "
        "l'unique agent de notre bonheur et nous fixe dans l'enfance ; Huxley en fait un roman, où le Sauvage réclame "
        "le droit d'être malheureux. "
        "{pat.g}Faire le bonheur des citoyens : non. {pat.d}En garantir les conditions, la sécurité, la justice, la {#la liberté}liberté : oui.",
        "{-pat}{-tab_dec}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Critique de la raison pratique (1788)", x=110, y=120, w=330, h=420),
        "tab_dec": dict(type="tableau", img="bh4-declaration", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="John Trumbull, La Déclaration d'indépendance, 1819 (Capitole des États-Unis, Washington)"),
        "pol": dict(type="liste", titre="Épisode 5 · Le bonheur des autres", items=[
            "Bentham : le plus grand bonheur du plus grand nombre",
            "Ivan Karamazov : les larmes d'un seul enfant",
            "1776 : le droit de rechercher le bonheur"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "c_sj": dict(type="cit", a="Saint-Just", o="rapport à la Convention, 3 mars 1794", x=170, y=240, w=940),
        "pat": dict(type="cols", g="Faire le bonheur des citoyens", gq="le gouvernement paternel, le despotisme doux",
                    d="En garantir les conditions", dq="sécurité, justice, libertés", vs="≠", repere="Kant, Tocqueville, Huxley"),
    }),

    # ------------------------------------------------------------------ V. le jour J
    dict(id="jourj", chap="Le jour J", fond="nuit", humeur="lumiere",
         retenir="Définir, problématiser, distinguer pour dépasser. Jamais « chacun son bonheur » comme conclusion.", beats=[
        "{tab_era}{meth}Le jour J. {meth.1}Définir chaque mot du sujet : affaire de, renoncer, faire. "
        "{meth.2}Problématiser : une tension, pas une reformulation. "
        "{meth.3}Trois parties, dont la dernière déplace la question grâce à une distinction. "
        "{meth.4}Et pour l'explication d'Épicure : six éléments d'introduction, puis quoi, comment, pourquoi.",
        "Ton introduction : une scène précise, l'analyse des mots, la problématique, le plan. "
        "Trois distinctions dépassent les problèmes : ce qui m'arrive et ce que j'en fais ; supprimer ou régler ses désirs ; "
        "faire le bonheur des citoyens, ou en garantir les conditions. Et Épicure, au plus juste : ni jouisseur, ni ascète.",
        "{-meth}{suj}Des sujets qui reviennent. {suj.1}Le bonheur est-il affaire de chance ? "
        "{suj.2}Faut-il renoncer à ses désirs pour être heureux ? {suj.3}L'État doit-il faire le bonheur des citoyens ? "
        "{suj.4}Le bonheur n'est-il qu'un idéal ?",
        "{-suj}{ex}Et des exemples précis : le ticket de loterie, les tonneaux percés, Crésus et Solon, l'hirondelle, "
        "Pyrrhus et Cinéas, le roi sans divertissement, le soma, Priam.",
        "{-ex}{-tab_era}{piege}Le piège : « chacun son bonheur ». Ce n'est pas une conclusion, c'est le refus de penser.",
        "{-piege}",
    ], vis={
        "tab_era": dict(type="tableau", img="bh6-erasme", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .6],
                        legende="Hans Holbein le Jeune, Érasme écrivant, 1523"),
        "meth": dict(type="liste", titre="Épisode 6 · Le jour de l'épreuve", items=[
            "Définir chaque mot du sujet", "Problématiser : une tension",
            "Trois parties : la dernière déplace la question", "Explication : six éléments, puis quoi · comment · pourquoi"],
                     marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "suj": dict(type="liste", titre="Des sujets qui reviennent", items=[
            "Le bonheur est-il affaire de chance ?", "Faut-il renoncer à ses désirs pour être heureux ?",
            "L'État doit-il faire le bonheur des citoyens ?", "Le bonheur n'est-il qu'un idéal ?"],
                    marques=["?", "?", "?", "?"], x=170, y=150, w=940),
        "ex": dict(type="nuage", items=["le ticket de loterie", "les tonneaux percés", "Crésus et Solon", "l'hirondelle",
                                        "Pyrrhus et Cinéas", "le roi sans divertissement", "le soma", "Priam"]),
        "piege": dict(type="note", titre="Le piège", cles=["refus"],
                      t="« Chacun son bonheur » : ce n'est pas une conclusion, c'est le refus de penser."),
    }),

    # ------------------------------------------------------------------ VI. fin
    dict(id="fin", chap="Toute la notion", fond="nuit", humeur="lumiere", beats=[
        "{rec}Voici toute la notion, sur une seule carte. {rec.1}Le mot et le plaisir. {rec.2}La sagesse des Anciens. "
        "{rec.3}Le soupçon de l'illusion. {rec.4}La morale et la cité.",
        "{-rec}{frise}Et voici ceux qui t'ont accompagné, d'Aristippe à Freud : vingt-quatre siècles à chercher la vie heureuse.",
        "{-frise}{trois}Si tu ne dois garder que trois phrases : {trois.1}Aristote, le bonheur est la fin de tous nos actes. "
        "{trois.2}Pascal, nous ne vivons jamais, mais nous espérons de vivre. "
        "{trois.3}Et Kant : la morale nous apprend à nous rendre dignes du bonheur.",
        ("Un dernier mot. Souviens-toi du ticket de loterie. Le bonheur n'est peut-être pas un lot qu'on gagne, "
         "mais une manière de vivre, qui s'apprend. Les philosophes ne t'ont pas donné de recette : ils t'ont appris à chercher.",
         {"rate": "-5%"}),
        ("Demain, devant ta copie, bonne chance. Au sens le plus ancien du mot.", {"rate": "-6%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-trois}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE BONHEUR", branches=[
            dict(t="Le mot et le plaisir", items=["bon heur, eudaimonia", "plaisir ≠ bonheur", "Épicure : trier ses désirs"]),
            dict(t="La sagesse", items=["Aristote : une activité, la vertu", "stoïciens : la vertu suffit", "Spinoza : la joie"]),
            dict(t="Une illusion ?", items=["Pascal, Schopenhauer", "Rousseau, Freud", "bonheur-état / activité"]),
            dict(t="Morale et cité", items=["Kant : digne d'être heureux", "Bentham, Saint-Just", "garantir les conditions"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Aristippe", d=-435, img="aristippe"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Épicure", d=-341, img="epicure"), dict(nom="Sénèque", d=-4, img="seneque"),
            dict(nom="Épictète", d=50, img="epictete"), dict(nom="Marc Aurèle", d=121, img="marc-aurele"),
            dict(nom="Spinoza", d=1632, img="spinoza"), dict(nom="Pascal", d=1623, img="pascal"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Bentham", d=1748, img="bentham"), dict(nom="Schopenhauer", d=1788, img="schopenhauer"),
            dict(nom="Tocqueville", d=1805, img="tocqueville"), dict(nom="Mill", d=1806, img="mill"),
            dict(nom="Freud", d=1856, img="freud")]),
        "trois": dict(type="liste", titre="Trois phrases à garder", items=[
            "Le bonheur, fin de tous nos actes · Aristote",
            "« Nous ne vivons jamais, mais nous espérons de vivre » · Pascal",
            "Se rendre digne du bonheur · Kant"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_fin": dict(type="tableau", img="bh7-soleil", fond=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Claude Monet, Impression, soleil levant, 1872 (musée Marmottan Monet, Paris)"),
        "fin": dict(type="titre", sur="Le bonheur", t="Fin de la série", sous="Six épisodes et un récap · bonne épreuve !"),
    }),
]

QUIZ = [
    dict(q="D'où vient le mot « bonheur » ?",
         r=["Du latin bonum, le bien", "De « bon heur » : la bonne chance, le bon augure", "Du grec hêdonê, le plaisir", "De l'allemand Glück"], ok=1,
         voir="mot", ex="L'heur, c'est le sort : le bonheur, à l'origine, c'est ce qui nous arrive (épisode 1)."),
    dict(q="Pour Épicure, le vrai plaisir, c'est…",
         r=["la jouissance de tous les plaisirs", "l'absence de douleur du corps et de trouble de l'âme", "la gloire", "la contemplation des dieux"], ok=1,
         voir="hed", ex="Aponie et ataraxie : un plaisir en repos, obtenu en triant ses désirs (épisode 2)."),
    dict(q="« Une hirondelle ne fait pas le printemps. » Que veut dire Aristote ?",
         r=["Que le bonheur dépend du climat", "Qu'un seul beau jour ne suffit pas : le bonheur se juge sur une vie complète",
            "Que les oiseaux sont heureux", "Que le bonheur est une illusion"], ok=1,
         voir="arist2", ex="Éthique à Nicomaque, I, 7 : le bonheur est une activité conforme à la vertu, dans une vie complète (épisode 3)."),
    dict(q="« Nous aimons la chasse, non la prise. » Qui l'explique, et avec quelle notion ?",
         r=["Rousseau : le désir", "Pascal : le divertissement", "Freud : le principe de plaisir", "Kant : le devoir"], ok=1,
         voir="ill", ex="Pensées, fr. 139 : le divertissement nous détourne de penser à notre condition (épisode 4)."),
    dict(q="Quelle distinction permet de répondre aux pessimistes ?",
         r=["Bonheur-état / bonheur-activité", "Plaisir / douleur", "Corps / âme", "Nature / culture"], ok=0,
         voir="etat", ex="Le bonheur comme état complet et définitif est sans doute une illusion ; le bonheur comme manière de vivre se construit."),
    dict(q="Selon Kant, la morale nous apprend…",
         r=["à être heureux", "à nous rendre dignes du bonheur", "à calculer nos plaisirs", "à fuir le bonheur"], ok=1,
         voir="kant", ex="Critique de la raison pratique (1788) : le bonheur ne fonde pas la morale (épisode 5)."),
    dict(q="Que doit faire l'État, selon la distinction de l'épisode 5 ?",
         r=["Faire le bonheur des citoyens à leur place", "Garantir les conditions du bonheur", "Distribuer du soma", "Ignorer le bonheur"], ok=1,
         voir="pat", ex="Faire le bonheur des citoyens, c'est le despotisme, même doux (Kant, Tocqueville, Huxley) ; en garantir les conditions, c'est la justice."),
    dict(q="Pourquoi « chacun son bonheur » est-il un piège en conclusion ?",
         r=["Parce que c'est faux", "Parce que c'est le refus de penser : la copie doit répondre au problème", "Parce que Kant l'interdit", "Parce que c'est trop long"], ok=1,
         voir="piege", ex="La troisième partie doit dépasser le problème par une distinction, pas s'arrêter au relativisme (épisode 6)."),
]

CREDITS = [
    "Portraits et images : voir les épisodes 1 à 6",
    "Tableaux : Godfried Schalcken, Homme à la chandelle (vers 1695-1700) ; Raphaël, L'École d'Athènes (1509-1511) ; "
    "Lubin Baugin, Le Dessert de gaufrettes (photo Sailko, CC BY 3.0) ; John William Waterhouse, Les Danaïdes (1906) ; "
    "Gaspar van den Hoecke, Crésus montrant ses trésors à Solon (XVIIᵉ s.) ; J. A. Naumann, Hirondelles (planche, XIXᵉ s.) ; "
    "Frans Hals, Garçon riant (v. 1625) ; "
    "Vilhelm Hammershøi, Intérieur, Strandgade 30 (1900) ; John Trumbull, La Déclaration d'indépendance (1819) ; "
    "Hans Holbein le Jeune, Érasme écrivant (1523) ; Claude Monet, Impression, soleil levant (1872) : domaine public",
    "Photographies : hamster dans sa roue (Rlicul, CC BY-SA 3.0)",
    "Citations : Épicure, Lettre à Ménécée, 128, trad. Hamelin (1910) ; Spinoza, Éthique, V, 42, trad. Saisset (1861) ; Pascal, Pensées, fr. 172 (éd. Brunschvicg) ; "
    "Saint-Just, rapport à la Convention du 3 mars 1794",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
