"""HGGSP, thème 1, objet de travail conclusif : « La Chine : à la conquête de l'espace, des mers et des océans » — en vidéo.

Même chaîne et même identité que les vidéos du thème 1 (hggsp_t1_intro.py, hggsp_t1_a1.py, hggsp_t1_a2.py) : la table des
cartes de l'état-major, moteur hggsp/serie/moteur.js. Contenu : le chapitre « t1-otc » du site
(outils/specialites/hggsp/src/data-t1.js), sa carte « chine » et son animation « scs » (la Chine s'avance en mer de Chine
méridionale), rien au-delà ; le sujet de dissertation et son corrigé sont ceux du chapitre (champ bac) ; les données de
l'épreuve viennent de la page « L'épreuve » du site (data-commun.js). Ce que les trois vidéos précédentes du thème
expliquent en détail (Montego Bay, traité de 1967, ISS, sentence de 2016) n'est que rappelé en une phrase.

Scènes de carte (avant la voix, à refaire si l'animation « scs » du site ou une carte de la vidéo change) :
    node outils/serie-hggsp/scenes.js hggsp-t1-otc        → hggsp/serie/illu-hggsp-t1-otc.js
(les cartes propres à la vidéo sont dans outils/serie-hggsp/cartes-hggsp-t1-otc.js).
Contrôles : python3 outils/serie-philo/verifier.py hggsp_t1_otc ;
brouillon sans voix : SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py hggsp_t1_otc ;
puis chevauchements.py hggsp-t1-otc et fermer.py hggsp_t1_otc.
"""

SITE = "hggsp"
CODE = "hggsp-t1-otc"
NOTION = "De nouveaux espaces de conquête"
NUM = 4
TITRE = "La Chine : à la conquête de l'espace, des mers et des océans"
SUIVANT = "Thème 2 · Faire la guerre, faire la paix : formes de conflits et modes de résolution"
RYTHME = "vivant"
PRONONCIATION = {"milles marins": "mil marins", "milles": "mil marins",
                 "Xi Jinping": "Si Djinne-pingue", "Hu Jintao": "Hou Djinne-tao", "Liaoning": "Liao-ningue",
                 "Shandong": "Chane-dongue", "Fujian": "Fou-djiane", "Tiangong": "Tiane-gongue", "Tianhe": "Tiane-heu",
                 "Chang'e": "Tchang-eu", "Yang Liwei": "Yangue Li-ouéï", "Shenzhou": "Chène-djo", "Zhurong": "Djou-rongue",
                 "Beidou": "Béï-dou", "Sansha": "Sane-cha", "Woody": "Woudi", "Fiery Cross": "Faïeri Crosse", "Subi": "Soubi",
                 "Mischief": "Mistchif", "Spratleys": "Spratlèïze", "Paracels": "Paracèle", "Scarborough": "Scarborô",
                 "Johnson South": "Djonsonne Saouz", "Whitsun": "Ouitseune", "Second Thomas": "Sèkeunnde Tomasse", "Jakarta": "Djakarta", "Gerald R. Ford": "Djéralde R Forde",
                 "Sierra Madre": "Siéra Madré", "COSCO": "Cosco", "Hambantota": "Hambanntota", "Gwadar": "Gouadar",
                 "Kyaukpyu": "Tchaok-piou", "Yunnan": "Iou-nane", "Senkaku": "Sènnkakou", "Diaoyu": "Diao-iou",
                 "AUKUS": "Okusse", "Quad": "Kwade", "ILRS": "I L R S", "Starlink": "Star-linque", "Qingdao": "Tchingue-dao",
                 "Sanya": "Sania", "Hainan": "Haï-nane", "Jiuquan": "Djiou-tchouane", "Wenchang": "Ouène-tchangue",
                 "Malacca": "Malaka", "Montego Bay": "Montégo Bèï", "Wolf": "Woulf", "CNES": "Cnèsse", "AIFM": "A I F M",
                 "Taïwan": "Taï-ouane", "Brunei": "Brounéï", "Manille": "Manille", "Artemis": "Artémisse",
                 "ZEE": "Z E E", "Longue Marche": "Longue Marche", "Shujianyang": "Chou-djiane-yangue"}

# ---------------------------------------------------------------- étapes des cartes propres à la vidéo
CHINE_V = [0, 0, 1000, 496]       # cadrage d'ensemble de la carte « chine »
VOIS_V = [0, 0, 1000, 636]        # cadrage d'ensemble de la carte « voisins »
MONDE_V = [0, 0, 1000, 437]       # planisphère (carte « alliances »)
CH_MARINE = [
    dict(date="Depuis 2012", titre="Qingdao : le Liaoning, premier porte-avions", montre=["qingdao"], accent=["qingdao"]),
    dict(date="2019 · 2025", titre="Sanya, sur l'île de Hainan : Shandong et Fujian", montre=["sanya"], accent=["sanya"]),
    dict(date="1er août 2017", titre="Djibouti : la première base à l'étranger", montre=["djib"], accent=["djib"]),
]
CH_ESPACE = [
    dict(date="Les vols habités", titre="Jiuquan, dans le désert de Gobi", montre=["jiuquan"], accent=["jiuquan"]),
    dict(date="Au bord de la mer", titre="Wenchang, sur l'île de Hainan", montre=["wench"], accent=["wench"]),
]
CH_ROUTES = [
    dict(date="Octobre 2013", titre="La « route de la soie maritime du XXIe siècle »", montre=["route", "shanghai"], accent=["shanghai"]),
    dict(date="2016 · 2021", titre="Le Pirée : 51 %, puis 67 % pour COSCO", montre=["piree"], accent=["piree"]),
    dict(date="Décembre 2017", titre="Hambantota, concédé pour 99 ans", montre=["hamb"], accent=["hamb"]),
]
CH_MALACCA = [
    dict(date="2003", titre="Le « dilemme de Malacca »", montre=["malacca"], accent=["malacca"]),
    dict(date="Depuis 2013", titre="Gwadar, au Pakistan", montre=["gwadar", "corridor"], accent=["gwadar"]),
    dict(date="2013 · 2017", titre="Kyaukpyu : des tubes jusqu'au Yunnan", montre=["kyauk", "tubes", "tubest"], accent=["kyauk"]),
]
VOISINS = [
    dict(date="Mer de Chine orientale", titre="Les îles Senkaku, ou Diaoyu", montre=["senkaku"], accent=["senkaku"]),
    dict(date="Taïwan", titre="De grandes manœuvres autour de l'île", montre=["tw", "manoeuvres", "manoeuvrest"], accent=["manoeuvres"]),
    dict(date="Mer de Chine méridionale", titre="La ligne en neuf traits, contestée", montre=["neuf", "scarb"], accent=["scarb"]),
    dict(date="Mars 2021", titre="Le récif de Whitsun", montre=["whitsun"], accent=["whitsun"]),
    dict(date="États-Unis", titre="Les patrouilles de « liberté de navigation »", montre=["fonop", "fonopt"], accent=["fonop"]),
]
ALLIANCES = [
    dict(date="Les ambitions chinoises", titre="Une puissance qui inquiète", montre=["cn", "cnt"], accent=["cn"]),
    dict(date="2017", titre="Le Quad : États-Unis, Japon, Inde, Australie", montre=["quad", "quadt", "quadj", "quadi", "quada", "quad17"], accent=["quad"]),
    dict(date="15 sept. 2021", titre="L'AUKUS : Australie, Royaume-Uni, États-Unis", montre=["aukus", "aukust", "ukt"], cache=["quad", "quadj", "quadi", "quad17"], accent=["aukus"]),
    dict(date="Septembre 2021", titre="Une crise diplomatique avec Paris", montre=["paris", "parist"], accent=["paris"]),
]
THOMAS = [
    dict(date="Spratleys", titre="Le récif de Second Thomas et le Sierra Madre", montre=["thomas"], accent=["thomas"]),
    dict(date="17 juin 2024", titre="Un abordage à la hache", montre=[], accent=["thomas"]),
]
POLAIRE = [
    dict(date="Janvier 2018", titre="La Chine, « État proche de l'Arctique »", montre=["cn", "cnt"], accent=["cn"]),
    dict(date="Quand la glace le permet", titre="Une « route de la soie polaire »", montre=["route", "routet", "rott"], accent=["route"]),
]
LUNE = [
    dict(date="3 janvier 2019", titre="Chang'e 4, premier atterrissage sur la face cachée", montre=["ce4", "terre", "jamais"], accent=["ce4"]),
    dict(date="Juin 2024", titre="Chang'e 6 prélève des échantillons", montre=["ce6"], accent=["ce6"]),
    dict(date="25 juin 2024", titre="Le retour sur Terre", montre=["retour", "retourt"], accent=["ce6"]),
    dict(date="Demain ?", titre="Le pôle Sud, cible des prochaines missions Chang'e", montre=["pole"], cache=["jamais"], accent=["pole"]),
]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ocean", humeur="mystere", carton=False, beats=[
        "{tab_fj}Le cinq novembre deux mille vingt-cinq, à Sanya, sur l'île de Hainan, tout au sud de la Chine. "
        "Un géant d'acier entre en service. C'est le Fujian, le troisième porte-avions chinois.",
        "Cinq mois plus tard, en avril deux mille vingt-six, une autre image fait le tour du monde. Quatre astronautes, partis de Floride, font le tour de la Lune. "
        "Mais la Chine, elle aussi, regarde la Lune. Elle s'est fixé un rendez-vous : y poser des taïkonautes avant deux mille trente.",
        ("P", 0.6),
        "{-tab_fj}{q1}Alors pourquoi la Chine se lance-t-elle, à ce rythme, à la conquête des océans… et du ciel ?",
        "{-q1}{rap}Les règles de la mer et de l'espace. La course à l'espace. La sentence de deux mille seize. "
        "Tout cela, tu le trouveras en détail dans les trois vidéos précédentes du thème. Ici, on zoome sur un seul acteur. La Chine.",
        "{-rap}{plan}Voici le dossier. {plan.1}D'abord, une volonté politique d'affirmation : des discours, des investissements, des appropriations. "
        "{plan.2}Ensuite, des enjeux économiques et géopolitiques considérables, pour la Chine et pour le reste du monde. "
        "{plan.3}Et pour finir, le bac : les pièges, puis une dissertation corrigée.",
        "{-plan}{bac0}Pour l'examen : ce thème n'est pas à l'écrit en deux mille vingt-sept. Il y revient en deux mille vingt-huit. "
        "Et l'objet conclusif est un excellent sujet de Grand oral. On y va.",
        "{-bac0}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_fj": dict(type="tableau", img="t1otc-fujian", de=[1.0, .5, .5], a=[1.12, .62, .5],
                       legende="Le porte-avions chinois Fujian, 11 septembre 2025, ministère japonais de la Défense (CC BY 4.0, Wikimedia Commons)"),
        "q1": dict(type="question", t="Pourquoi la Chine se lance-t-elle à la conquête des mers et de l'espace ?"),
        "rap": dict(type="note", titre="Déjà vu", t="Montego Bay, le traité de 1967, la course à l'espace, la sentence de 2016 : les trois vidéos précédentes du thème.", y=230),
        "plan": dict(type="liste", titre="Le dossier", items=[
            "Une volonté politique d'affirmation : discours, investissements, appropriations",
            "Des enjeux économiques et géopolitiques, pour la Chine et le reste du monde",
            "Au bac : les pièges, une dissertation corrigée"], marques=["I", "II", "✎"], x=150, y=150, w=980),
        "bac0": dict(type="note", titre="Au bac", t="Thème 1 : pas à l'écrit en 2027, à l'écrit en 2028. Et un excellent sujet de Grand oral.", y=230),
        "titre": dict(type="titre", sur="HGGSP · Thème 1 · Objet de travail conclusif", t="La Chine : à la conquête de l'espace, des mers et des océans",
                      sous="De nouveaux espaces de conquête"),
    }),

    # ================================================================ I.1 le siècle d'humiliation
    dict(id="humiliation", chap="Effacer le « siècle d'humiliation »", fond="archive", humeur="mystere",
         retenir="Pour le Parti communiste, la Chine a été dominée de la guerre de l'Opium (1839-1842) à 1949, en grande partie faute d'avoir tenu la mer. 29 novembre 2012 : Xi Jinping lance le « rêve chinois », le « grand renouveau de la nation chinoise » pour 2049.",
         beats=[
        "{m1}Pour comprendre, il faut remonter loin. Au dix-neuvième siècle.",
        "{-m1}{sh}{sh.1}De mille huit cent trente-neuf à mille huit cent quarante-deux, la Chine perd la guerre de l'Opium contre le Royaume-Uni. "
        "{sh.2}Pour le Parti communiste chinois, c'est le début d'un siècle de domination étrangère, qui ne s'achève qu'en mille neuf cent quarante-neuf, "
        "avec la victoire des communistes. On l'appelle le « siècle d'humiliation ».",
        "{-sh}{mer0}Et voici la leçon que le Parti en tire. La Chine a été dominée, en grande partie, parce qu'elle avait {!négligé la mer}négligé la mer. "
        "Les Britanniques, puis les Japonais, sont venus par les côtes.",
        "{-mer0}{reve}Fais un saut jusqu'au vingt-neuf novembre deux mille douze. Deux semaines plus tôt, Xi Jinping est devenu secrétaire général du Parti. "
        "Ce jour-là, il lance une expression qui va tout résumer : le « rêve chinois ».",
        "{-reve}{rv}{rv.1}Ce rêve, c'est le « grand renouveau de la nation chinoise ». {rv.2}Et il a une date limite : deux mille quarante-neuf. "
        "Le centenaire de la République populaire.",
        ("P", 0.5),
        "{-rv}{f1}Retiens bien ce ressort. La puissance en mer et dans l'espace doit {!effacer l'humiliation}effacer l'humiliation. "
        "Et prouver, aux Chinois comme au monde, que le régime réussit.",
    ], vis={
        "m1": dict(type="mot", t="1839", g="Le début du « siècle d'humiliation »", taille=150, y=210),
        "sh": dict(type="chrono", titre="Le « siècle d'humiliation »", items=[
            dict(d="1839-1842", t="La guerre de l'Opium, perdue contre le Royaume-Uni", c="conflit"),
            dict(d="1949", t="Victoire des communistes : la République populaire", c="conflit")], x=290, w=700, y=150, h=420),
        "mer0": dict(type="note", titre="La leçon tirée par le Parti", t="La Chine a été dominée parce qu'elle avait négligé la mer : les Britanniques, puis les Japonais, sont venus par les côtes.", y=220),
        "reve": dict(type="mot", t="29 nov. 2012", g="Xi Jinping lance le « rêve chinois »", taille=120, y=220),
        "rv": dict(type="chiffres", titre="Le « rêve chinois »", items=[
            dict(v="Renouveau", t="le « grand renouveau de la nation chinoise »", taille=72),
            dict(v="2049", t="le centenaire de la République populaire", taille=84)], y=180),
        "f1": dict(type="note", titre="À retenir", t="La puissance maritime et spatiale doit effacer l'humiliation et prouver la réussite du régime.", y=230),
    }),

    # ================================================================ I.2 des discours qui fixent des objectifs
    dict(id="discours", chap="Des discours qui fixent des objectifs", fond="crise", humeur="lumiere",
         retenir="XVIIIe congrès (novembre 2012) : faire de la Chine une « puissance maritime ». Livres blancs ; « Journée de l'espace » le 24 avril. Livre blanc du 28 janvier 2022 : une « puissance spatiale » de premier rang. 2023 : un atterrissage habité sur la Lune avant 2030.",
         beats=[
        "{q2}Un rêve, c'est bien. Mais comment le transformer en programme ?",
        "{-q2}{ob}Par des discours qui fixent des objectifs. Et des dates. "
        "{ob.1}En novembre deux mille douze, le dix-huitième congrès du Parti fixe un cap : faire de la Chine une {!puissance maritime}puissance maritime. "
        "{ob.2}Puis des livres blancs, publiés régulièrement sur l'espace et la défense, fixent les étapes.",
        "{ob.3}Le vingt-huit janvier deux mille vingt-deux, le livre blanc sur l'espace annonce l'objectif : une puissance spatiale de premier rang. "
        "{ob.4}Et en deux mille vingt-trois, l'agence des vols habités précise : un atterrissage habité sur la Lune avant deux mille trente.",
        "{-ob}{scn}Et ces succès, on les met en scène. Les lancements sont retransmis à la télévision. "
        "Et chaque vingt-quatre avril, la Chine fête sa « Journée de l'espace ». Pourquoi cette date ? "
        "En souvenir du premier satellite chinois, lancé un vingt-quatre avril.",
        "{-scn}{f2}Tu vois la logique ? Un objectif, une date, puis une célébration. La conquête sert aussi la {!propagande}propagande.",
    ], vis={
        "q2": dict(type="question", t="Comment transformer un rêve en programme ?"),
        "ob": dict(type="chrono", titre="Des objectifs et des dates", items=[
            dict(d="Nov. 2012", t="XVIIIe congrès : une « puissance maritime »", c="mer"),
            dict(d="Livres blancs", t="espace et défense : les étapes", c="droit"),
            dict(d="28 janv. 2022", t="Livre blanc : une « puissance spatiale » de premier rang", c="espace"),
            dict(d="2023", t="Objectif : un atterrissage habité sur la Lune avant 2030", c="espace")], x=100, w=1080, y=130, h=450),
        "scn": dict(type="def", terme="La « Journée de l'espace »", t="Chaque 24 avril, en souvenir du premier satellite chinois : les succès sont mis en scène, les lancements retransmis.", y=210),
        "f2": dict(type="note", titre="La logique", t="Un objectif, une date, une célébration : la conquête sert aussi la propagande du régime.", y=230),
    }),

    # ================================================================ I.3 la marine
    dict(id="marine", chap="Des investissements massifs en mer", fond="ocean", humeur="tension",
         retenir="Marine de l'Armée populaire de libération : la plus grande du monde en nombre de bâtiments (plus de 370 navires et sous-marins, Pentagone, 2024). Plus de la moitié des navires construits dans le monde. Garde-côtes et milice maritime. Liaoning (2012), Shandong (2019), Fujian (5 novembre 2025, catapultes électromagnétiques).",
         beats=[
        "{inv}Passons aux actes. Et d'abord en mer. "
        "{inv.1}La marine de l'Armée populaire de libération est devenue la plus grande du monde en nombre de bâtiments. "
        "Plus de trois cent soixante-dix navires et sous-marins, selon le Pentagone, en deux mille vingt-quatre.",
        "{inv.2}Et la Chine construit plus de la moitié des navires produits dans le monde. Premier constructeur naval de la planète !",
        "{-inv}{trio}Mais ce n'est pas tout. {trio.1}À côté de la marine de guerre, il y a deux autres flottes. "
        "{trio.2}Des garde-côtes, toujours plus nombreux. {trio.3}Et une {!milice maritime}milice maritime : des pêcheurs, encadrés par l'État. "
        "On les retrouvera tout à l'heure, en mer de Chine.",
        "{-trio}{pa}Et puis, il y a le symbole de la puissance navale : le porte-avions. La Chine en a mis trois en service en treize ans. "
        "{pa.1}Le Liaoning, en deux mille douze. Un ancien navire soviétique, racheté et remis en état. "
        "{pa.2}Le Shandong, en deux mille dix-neuf : le premier construit en Chine. "
        "{pa.3}Et le Fujian, le cinq novembre deux mille vingt-cinq. Il a des catapultes électromagnétiques, comme le plus récent porte-avions américain, le Gerald R. Ford.",
        "{-pa}{chm}Regarde où ils sont basés. {chm.1}Au nord, Qingdao, port d'attache du Liaoning. "
        "{chm.2}Au sud, Sanya, sur l'île de Hainan, face à la mer de Chine méridionale. Le Shandong et le Fujian y sont basés.",
        "{chm.3}Et loin, très loin de la Chine : Djibouti, au débouché de la mer Rouge. Depuis le premier août deux mille dix-sept, "
        "c'est la première base militaire chinoise à l'étranger.",
        "{-chm}{f3}La puissance chinoise en mer n'est donc pas seulement économique. Elle est militaire, et elle se projette loin.",
    ], vis={
        "inv": dict(type="chiffres", titre="La marine chinoise", items=[
            dict(v=370, avant="+ de ", t="navires et sous-marins : la plus grande marine en nombre", src="Pentagone, 2024", taille=84),
            dict(v=50, avant="+ de ", apres=" %", t="des navires construits dans le monde", taille=84)], y=180),
        "trio": dict(type="cartes", items=[
            dict(ic="drapeau", t="La marine de guerre", q="l'Armée populaire de libération"),
            dict(ic="radar", t="Les garde-côtes", q="une flotte toujours plus nombreuse"),
            dict(ic="vague", t="La milice maritime", q="des pêcheurs encadrés par l'État")]),
        "pa": dict(type="chrono", titre="Trois porte-avions en treize ans", items=[
            dict(d="2012", t="Liaoning : un ancien navire soviétique remis en état", c="mer"),
            dict(d="2019", t="Shandong : le premier construit en Chine", c="mer"),
            dict(d="5 nov. 2025", t="Fujian : des catapultes électromagnétiques", c="mer")], x=150, w=980, y=140, h=430),
        "chm": dict(type="scene", anim="chine", etapes=CH_MARINE, fs=23,
                    cam={"0": CHINE_V, "1": [620, 30, 330, 164], "2": [560, 170, 300, 149], "3": [20, 120, 520, 258]}),
        "f3": dict(type="note", titre="À retenir", t="La puissance chinoise en mer est militaire, pas seulement économique : elle se projette jusqu'à Djibouti.", y=230),
    }),

    # ================================================================ I.4 l'espace
    dict(id="espace", chap="Un programme spatial complet", fond="orbite", humeur="lumiere",
         retenir="Tous les segments : lanceurs Longue Marche, vols habités, station, navigation (Beidou, complet en 2020), observation, Lune et Mars. 24 avril 1970 ; Yang Liwei, 15 octobre 2003 ; Chang'e 4, 3 janvier 2019 ; Zhurong, 15 mai 2021 ; Tianhe, 29 avril 2021 ; Chang'e 6, 25 juin 2024.",
         beats=[
        "{cmp}Et dans l'espace ? La Chine a une particularité. Elle maîtrise {!tous les segments}tous les segments. "
        "{cmp.1}Ses propres lanceurs, les fusées Longue Marche. {cmp.2}Les vols habités, et une station. "
        "{cmp.3}La navigation par satellite, avec Beidou. {cmp.4}L'observation de la Terre. {cmp.5}Et l'exploration de la Lune et de Mars.",
        "{-cmp}{bd}Arrête-toi sur Beidou. Depuis deux mille vingt, ce système est complet. Il couvre toute la planète. "
        "Comme Galileo pour l'Europe, c'est un moyen de ne plus dépendre du GPS américain.",
        "{-bd}{prem}Et les premières s'accumulent. {prem.1}Le vingt-quatre avril mille neuf cent soixante-dix, le premier satellite. "
        "{prem.2}Le quinze octobre deux mille trois, Yang Liwei devient le premier taïkonaute. La Chine est alors la troisième puissance "
        "à envoyer un humain dans l'espace par ses propres moyens.",
        "{prem.3}Le vingt-neuf avril deux mille vingt et un, le module central de la station Tiangong décolle. Son nom : Tianhe. "
        "L'assemblage est achevé fin deux mille vingt-deux. {prem.4}Et le quinze mai deux mille vingt et un, la Chine se pose sur Mars, avec le robot Zhurong.",
        "{-prem}{csp}Regarde aussi d'où partent les fusées. {csp.1}Les vols habités décollent de Jiuquan, dans le désert de Gobi. "
        "{csp.2}Et Wenchang, sur l'île de Hainan, est une base au bord de la mer : les lanceurs lourds peuvent y arriver par bateau.",
    ], vis={
        "cmp": dict(type="liste", titre="Un programme spatial complet", items=[
            "Les lanceurs : les fusées Longue Marche", "Les vols habités et une station : Tiangong",
            "La navigation : Beidou", "L'observation de la Terre", "L'exploration : la Lune et Mars"], x=200, y=120, w=880),
        "bd": dict(type="def", terme="Beidou", t="Le système chinois de navigation par satellite, complet depuis 2020 : ne plus dépendre du GPS américain.", y=220),
        "prem": dict(type="chrono", titre="Les étapes de la Chine dans l'espace", items=[
            dict(d="24 avril 1970", t="Le premier satellite chinois", c="espace"),
            dict(d="15 oct. 2003", t="Yang Liwei, premier taïkonaute", c="espace"),
            dict(d="29 avril 2021", t="Tianhe, module central de Tiangong", c="espace"),
            dict(d="15 mai 2021", t="Zhurong se pose sur Mars", c="espace")], x=100, w=1080, y=130, h=450),
        "csp": dict(type="scene", anim="chine", etapes=CH_ESPACE, fs=23,
                    cam={"0": CHINE_V, "1": [470, 0, 320, 159], "2": [560, 190, 300, 149]}),
    }),

    # ================================================================ I.5 la face cachée
    dict(id="lune", chap="Premières mondiales sur la Lune", fond="orbite", humeur="mystere",
         retenir="Chang'e 4 (3 janvier 2019) : premier atterrissage sur la face cachée de la Lune. Chang'e 6 : premiers échantillons de la face cachée, rapportés le 25 juin 2024. Objectif : un atterrissage habité avant 2030.",
         beats=[
        "{q3}Et voici un exploit que personne n'avait réussi avant la Chine. Tu sais que la Lune nous montre toujours la même face ?",
        "{-q3}{ln}{ln.1}Son autre face, la face cachée, est donc invisible depuis la Terre. Le trois janvier deux mille dix-neuf, "
        "la sonde Chang'e quatre s'y pose. C'est le {!premier atterrissage}premier atterrissage sur la face cachée de la Lune.",
        "{ln.2}Cinq ans plus tard, en juin deux mille vingt-quatre, la Chine recommence avec Chang'e six. Cette fois, la sonde prélève des roches. "
        "{ln.3}Et le vingt-cinq juin, elle les rapporte sur Terre. Les tout premiers échantillons de la face cachée.",
        "{ln.4}La prochaine étape ? Des taïkonautes sur la Lune avant deux mille trente. Et peut-être, plus tard, près du pôle Sud, où l'on pense trouver de la glace d'eau.",
        "{-ln}{crs}{crs.g}Or c'est aussi la cible du programme américain Artemis. {crs.d}La Lune redevient un terrain de rivalité. "
        "Entre deux puissances, cette fois : les États-Unis… et la Chine.",
    ], vis={
        "q3": dict(type="question", t="La Lune nous montre toujours la même face. Et l'autre ?"),
        "ln": dict(type="scene", anim="lune", etapes=LUNE, depart=["disque"], fs=20,
                   cam={"0": [0, 0, 1000, 500]}),
        "crs": dict(type="cols", g="États-Unis", gq="Artemis : retour vers le pôle Sud de la Lune", d="Chine",
                    dq="un atterrissage habité visé avant 2030", vs="2030"),
    }),

    # ================================================================ I.6 la mer de Chine méridionale
    dict(id="scs", chap="S'approprier la mer de Chine méridionale", fond="crise", humeur="tension",
         retenir="Ligne en neuf traits (carte de 1947) : l'essentiel de la mer de Chine méridionale, disputée avec le Viêt Nam, les Philippines, la Malaisie, Brunei et Taïwan. 2013-2016 : îles artificielles militarisées (Fiery Cross, Subi, Mischief : pistes d'environ 3 000 m). Sansha (2012). Sentence du 12 juillet 2016 rejetée.",
         beats=[
        "{q4}Troisième levier de l'affirmation : s'approprier des espaces. Et le laboratoire, c'est la mer de Chine méridionale.",
        "{-q4}{sc}{sc.1}Tout part d'une ligne tracée sur une carte en mille neuf cent quarante-sept, puis ramenée à neuf traits. La « ligne en neuf traits ». "
        "Elle englobe presque toute la mer. Une mer que la Chine dispute au Viêt Nam, aux Philippines, à la Malaisie, à Brunei et à Taïwan.",
        "{sc.2}En janvier mille neuf cent soixante-quatorze, la Chine prend aux Sud-Vietnamiens la partie des îles Paracels qu'elle ne contrôlait pas encore. "
        "{sc.3}En mille neuf cent quatre-vingt-huit, un affrontement l'oppose au Viêt Nam dans les Spratleys, au récif Johnson South : soixante-quatre marins vietnamiens sont tués. "
        "{sc.4}En mille neuf cent quatre-vingt-quinze, elle occupe le récif de Mischief, revendiqué par les Philippines.",
        "{sc.5}En deux mille douze, elle prend le contrôle du récif de Scarborough. Et la même année, elle crée une « ville », Sansha, "
        "sur l'île Woody, dans les Paracels, pour administrer toute la zone.",
        "{-sc}{sansha}Une ville au milieu de la mer ? Oui. Car on s'approprie un espace aussi par l'{!administration}administration, et par le peuplement.",
        "{-sansha}{sc2}{sc2.1}Puis, entre deux mille treize et deux mille seize, les dragues entrent en action. Des récifs, à peine émergés, "
        "deviennent des îles artificielles. Sur Fiery Cross, Subi et Mischief, on construit des pistes d'environ trois mille mètres. "
        "Des ports. Des radars. Des récifs deviennent des bases.",
        "{-sc2}{sc3}{sc3.1}Le douze juillet deux mille seize, un tribunal arbitral donne tort à la Chine. Pékin rejette la sentence. "
        "{sc3.2}Et le cinq novembre deux mille vingt-cinq, c'est à Sanya, face à cette mer, qu'entre en service le Fujian.",
        "{-sc3}{f4}Retiens les trois gestes de l'appropriation. {f4.1}Revendiquer, avec une ligne sur une carte. "
        "{f4.2}Occuper et construire. {f4.3}Administrer, avec une ville.",
    ], vis={
        "q4": dict(type="mot", t="S'approprier", g="la mer de Chine méridionale, laboratoire de l'affirmation chinoise", taille=110, y=230),
        "sc": dict(type="scene", anim="scs", pas=[0, 1, 2, 3, 4], fs=20,
                   cam={"0": [0, 0, 760, 820], "2": [140, 80, 440, 216], "3": [200, 400, 440, 216], "5": [180, 60, 560, 274]}),
        "sansha": dict(type="def", terme="Sansha, une « ville » en mer", t="Créée en 2012 sur l'île Woody (Paracels) pour administrer les revendications chinoises : s'approprier par l'administration et le peuplement.", y=200),
        "sc2": dict(type="scene", anim="scs", pas=[5], fs=20, cam={"0": [0, 0, 760, 820], "1": [180, 400, 460, 225]}),
        "sc3": dict(type="scene", anim="scs", pas=[6, 7], fs=20, cam={"0": [0, 0, 760, 820], "1": [60, 380, 640, 314], "2": [20, 60, 440, 216]}),
        "f4": dict(type="liste", titre="Les trois gestes de l'appropriation", items=[
            "Revendiquer : la ligne en neuf traits (1947)", "Occuper et construire : les îles artificielles (2013-2016)",
            "Administrer : la « ville » de Sansha (2012)"], marques=["1", "2", "3"], x=180, y=170, w=920),
    }),

    # ================================================================ II.1 les routes de la soie
    dict(id="routes", chap="Les routes de la soie maritimes", fond="ocean", humeur="calme",
         retenir="Octobre 2013, au Parlement indonésien : Xi Jinping annonce la « route de la soie maritime du XXIe siècle ». COSCO : 51 % du Pirée (2016), 67 % (2021). Hambantota concédé pour 99 ans (décembre 2017). « Collier de perles » : une expression américaine.",
         beats=[
        "{m5}Deuxième volet du dossier : les enjeux. Économiques d'abord.",
        "{-m5}{dep}Commence par un constat. La Chine est la deuxième économie du monde. Et son commerce {!dépend de la mer}dépend de la mer.",
        "{-dep}{rt}{rt.1}En octobre deux mille treize, Xi Jinping est en visite à Jakarta, devant le Parlement indonésien. Il annonce un grand projet : "
        "la « route de la soie maritime du vingt et unième siècle ». Des ports financés ou exploités par la Chine, de la mer de Chine jusqu'à la Méditerranée.",
        "{rt.2}Exemple : le Pirée, le port d'Athènes. En deux mille seize, l'entreprise publique chinoise COSCO en prend cinquante et un pour cent. "
        "Puis soixante-sept pour cent, en deux mille vingt et un. Une porte d'entrée chinoise en Europe.",
        "{rt.3}Autre exemple : Hambantota, au Sri Lanka. En décembre deux mille dix-sept, le pays, endetté, concède son port pour quatre-vingt-dix-neuf ans à une société chinoise.",
        "{-rt}{cp}{cp.g}Les Américains ont un nom pour ces points d'appui : le « collier de perles ». "
        "{cp.d}Attention : c'est une {!expression américaine}expression américaine, une représentation. Pas un fait neutre.",
        "{-cp}{dette}Même prudence avec l'idée de « piège de la dette ». Les chercheurs la discutent. "
        "À Hambantota, la mauvaise gestion locale compte autant que les prêts chinois.",
    ], vis={
        "m5": dict(type="mot", t="Les enjeux", g="économiques et géopolitiques, pour la Chine et le reste du monde", taille=120, y=230),
        "dep": dict(type="note", titre="Le constat", t="Deuxième économie du monde, la Chine dépend de la mer pour son commerce.", y=230),
        "rt": dict(type="scene", anim="chine", etapes=CH_ROUTES, fs=23,
                   cam={"0": CHINE_V, "2": [0, 10, 380, 188], "3": [260, 230, 400, 198]}),
        "cp": dict(type="cols", g="« Collier de perles »", gq="les points d'appui chinois dans l'océan Indien", d="Mais…",
                   dq="une expression américaine : une représentation, pas un fait", vs="!"),
        "dette": dict(type="def", terme="« Piège de la dette » ?", t="Une expression discutée par les chercheurs : à Hambantota, la mauvaise gestion locale compte autant que les prêts chinois.", y=200),
    }),

    # ================================================================ II.2 le dilemme de Malacca
    dict(id="malacca", chap="Le « dilemme de Malacca »", fond="crise", humeur="tension",
         retenir="Une grande partie du pétrole importé par la Chine passe par le détroit de Malacca, que la marine américaine pourrait bloquer : le « dilemme de Malacca » (Hu Jintao, 2003). Contournements : Gwadar (Pakistan, depuis 2013), tubes de Kyaukpyu (Birmanie) au Yunnan (gazoduc 2013, oléoduc 2017).",
         beats=[
        "{q5}Mais ces routes ont un point faible. Un seul passage, très étroit. Lequel ?",
        "{-q5}{ml}{ml.1}Le détroit de Malacca, entre la Malaisie et l'île indonésienne de Sumatra. Une grande partie du pétrole importé par la Chine y passe.",
        "Et en cas de crise, la marine américaine pourrait le bloquer. En deux mille trois, le président chinois Hu Jintao a un nom pour cette angoisse : "
        "le {!« dilemme de Malacca »}« dilemme de Malacca ».",
        "{ml.2}Alors la Chine cherche à contourner le détroit. Premier exemple : Gwadar, au Pakistan, exploité par une société chinoise depuis deux mille treize. "
        "De là, la route peut remonter par la terre vers la Chine.",
        "{ml.3}Deuxième exemple : Kyaukpyu, en Birmanie. Deux tubes en partent jusqu'au Yunnan, dans le sud de la Chine. "
        "Un gazoduc, en deux mille treize. Et un oléoduc, en deux mille dix-sept.",
        "{-ml}{f5}Tu vois le lien avec la marine ? Bases, ports et tubes ont le même but : {!sécuriser les approvisionnements}sécuriser les approvisionnements.",
    ], vis={
        "q5": dict(type="question", t="Quel est le point faible des routes maritimes chinoises ?"),
        "ml": dict(type="scene", anim="chine", etapes=CH_MALACCA, depart=["route", "shanghai"], fs=23,
                   cam={"0": CHINE_V, "1": [470, 280, 300, 149], "2": [230, 30, 340, 169], "3": [470, 150, 280, 139]}),
        "f5": dict(type="note", titre="À retenir", t="Bases, ports et tubes ont un même but : sécuriser les approvisionnements en contournant Malacca.", y=230),
    }),

    # ================================================================ II.3 les ressources
    dict(id="ressources", chap="Pêche, hydrocarbures, grands fonds", fond="ocean", humeur="mystere",
         retenir="Premier pays pêcheur du monde, plus grande flotte de pêche lointaine ; hydrocarbures de la mer de Chine ; plusieurs contrats d'exploration de l'AIFM. Mars 2021 : environ 220 navires « pêcheurs » sur le récif de Whitsun, dans la ZEE des Philippines.",
         beats=[
        "{rs}Autre enjeu : les ressources. {rs.1}La Chine est le premier pays pêcheur du monde. Elle a la plus grande flotte de pêche lointaine. "
        "{rs.2}Elle convoite les hydrocarbures de la mer de Chine. "
        "{rs.3}Et elle détient plusieurs contrats d'exploration de l'Autorité internationale des fonds marins, pour les grands fonds.",
        "{-rs}{wh}Et là, les pêcheurs deviennent un instrument. En mars deux mille vingt et un, environ deux cent vingt navires chinois "
        "stationnent pendant des semaines sur le récif de Whitsun. Dans la ZEE des Philippines.",
        "Officiellement, ce sont des pêcheurs. Mais Manille les identifie comme une {!milice maritime}milice maritime.",
        "{-wh}{zg}Pourquoi c'est malin ? Parce que des bateaux de pêche, ce n'est pas une invasion. On occupe un espace… sans tirer un coup de feu. "
        "C'est ce que les spécialistes appellent une stratégie de la {!zone grise}zone grise.",
    ], vis={
        "rs": dict(type="cartes", items=[
            dict(ic="vague", t="La pêche", q="1er pays pêcheur, plus grande flotte de pêche lointaine"),
            dict(ic="globe", t="Les hydrocarbures", q="convoités en mer de Chine"),
            dict(ic="radar", t="Les grands fonds", q="plusieurs contrats d'exploration de l'AIFM")]),
        "wh": dict(type="chiffres", titre="Récif de Whitsun, mars 2021", items=[
            dict(v=220, avant="≈ ", t="navires « pêcheurs » chinois dans la ZEE des Philippines", src="Manille y voit une milice maritime")], y=190),
        "zg": dict(type="def", terme="La milice maritime", t="Des pêcheurs encadrés par l'État occupent un espace disputé sans combat : une stratégie de la zone grise.", y=210),
    }),

    # ================================================================ II.4 Arctique et espace
    dict(id="influence", chap="L'Arctique et l'espace, terrains d'influence", fond="orbite", humeur="lumiere",
         retenir="Livre blanc de janvier 2018 : la Chine « État proche de l'Arctique », une « route de la soie polaire ». Dans l'espace : exportation de satellites et de Beidou, station et missions ouvertes aux partenaires, constellations Internet face à Starlink. Chang'e 6 (2024) emporte des instruments français (CNES), européens (ESA), italiens et un satellite pakistanais.",
         beats=[
        "{arc}Et l'influence chinoise va plus loin. Jusqu'au Grand Nord. "
        "{arc.1}En janvier deux mille dix-huit, dans un livre blanc, la Chine se proclame « État proche de l'Arctique ». "
        "Proche ? La Chine n'a pourtant aucune côte sur l'océan Arctique !",
        "{arc.2}Mais l'idée est claire : proposer une « route de la soie polaire », par le nord de la Russie, vers l'Europe. Quand la glace le permet.",
        "{-arc}{inf}Dans l'espace aussi, la Chine cherche des partenaires. {inf.1}Elle exporte des satellites, et les services de Beidou. "
        "{inf.2}Elle ouvre sa station et ses missions aux pays partenaires. "
        "{inf.3}Et elle lance ses propres constellations de satellites pour Internet, pour concurrencer Starlink.",
        "{-inf}{ce6}Un exemple, tout récent. La sonde Chang'e six, en deux mille vingt-quatre, emportait des instruments venus d'ailleurs. "
        "{ce6.1}Un détecteur de radon français, du CNES. {ce6.2}Un instrument de l'Agence spatiale européenne. {ce6.3}Un autre, italien. "
        "{ce6.4}Et un petit satellite pakistanais.",
        "{-ce6}{wolf}Pourquoi c'est important ? Parce que les États-Unis, eux, ont fermé leur porte : depuis l'amendement Wolf, la NASA ne peut pas coopérer directement avec la Chine sans l'accord du Congrès. "
        "Pékin montre au monde qu'avec elle, coopérer reste possible.",
    ], vis={
        "arc": dict(type="scene", anim="polaire", etapes=POLAIRE, fs=20, cam={"0": [0, 0, 700, 700], "1": [80, 240, 620, 304]}),
        "inf": dict(type="liste", titre="L'espace, outil d'influence", items=[
            "Exporter des satellites et les services de Beidou", "Ouvrir sa station et ses missions aux partenaires",
            "Lancer ses constellations Internet, face à Starlink"], x=180, y=160, w=920),
        "ce6": dict(type="liste", titre="À bord de Chang'e 6 (2024)", items=[
            "Un détecteur de radon français (CNES)", "Un instrument de l'Agence spatiale européenne",
            "Un instrument italien", "Un petit satellite pakistanais"], x=230, y=140, w=820),
        "wolf": dict(type="def", terme="Coopérer avec la Chine", t="Les États-Unis l'excluent (amendement Wolf) ; Pékin montre qu'avec elle, coopérer reste possible.", y=210),
    }),

    # ================================================================ II.5 des voisins inquiets
    dict(id="voisins", chap="Des voisins inquiets", fond="crise", humeur="tension",
         retenir="Le Japon (Senkaku / Diaoyu), le Viêt Nam, les Philippines et l'Inde s'opposent à Pékin ; les États-Unis organisent des patrouilles de « liberté de navigation » ; grandes manœuvres chinoises autour de Taïwan.",
         beats=[
        "{q6}Tout cela, tu t'en doutes, inquiète. Qui, d'abord ? Les voisins.",
        "{-q6}{vs}{vs.1}Le Japon, en mer de Chine orientale. Il administre les îles Senkaku, que la Chine revendique sous le nom de Diaoyu.",
        "{vs.2}Taïwan, au cœur des tensions. La Chine organise de grandes manœuvres militaires autour de l'île.",
        "{vs.3}Le Viêt Nam et les Philippines, en mer de Chine méridionale. Et plus à l'ouest, l'Inde. "
        "{vs.4}Tu te souviens du récif de Whitsun ? Il est là, dans la ZEE philippine.",
        "{vs.5}Et les États-Unis, qui ne reconnaissent pas les revendications chinoises. Leur marine organise des patrouilles de « liberté de navigation ». "
        "Des navires de guerre passent volontairement dans les zones revendiquées. Le message ? Cette mer n'est pas chinoise.",
    ], vis={
        "q6": dict(type="question", t="Qui s'inquiète des ambitions chinoises ?"),
        "vs": dict(type="scene", anim="voisins", etapes=VOISINS, fs=20,
                   cam={"0": VOIS_V, "1": [330, 60, 380, 186], "2": [300, 100, 400, 196], "3": [150, 300, 480, 235], "4": [150, 410, 360, 176], "5": VOIS_V}),
    }),

    # ================================================================ II.6 Quad et AUKUS
    dict(id="alliances", chap="Le Quad et l'AUKUS", fond="crise", humeur="tension",
         retenir="Le Quad (États-Unis, Japon, Inde, Australie), relancé en 2017, coordonne ces puissances face à la Chine. AUKUS (15 septembre 2021) : des sous-marins à propulsion nucléaire pour l'Australie avec l'aide américaine et britannique ; un contrat français annulé, crise diplomatique avec Paris.",
         beats=[
        "{al}Les inquiets s'organisent. {al.1}Face à la Chine, {al.2}un premier cercle : le Quad. Les États-Unis, le Japon, l'Inde et l'Australie. "
        "Relancé en deux mille dix-sept, ce dialogue coordonne quatre puissances de l'Indo-Pacifique.",
        "{al.3}Puis, le quinze septembre deux mille vingt et un, un coup de théâtre : l'AUKUS. Australie, Royaume-Uni, États-Unis. "
        "Grâce à ce pacte, l'Australie pourra acquérir des sous-marins à propulsion nucléaire, avec l'aide américaine et britannique.",
        "{al.4}Et la France ? Elle l'apprend à ses dépens. L'Australie annule un contrat de sous-marins français. "
        "Paris parle de trahison : c'est une crise diplomatique entre alliés.",
        "{-al}{lec}La leçon ? Les ambitions chinoises redessinent les alliances. La Chine est au cœur des {!rivalités de puissance}rivalités de puissance du vingt et unième siècle.",
    ], vis={
        "al": dict(type="scene", anim="alliances", etapes=ALLIANCES, fs=20,
                   cam={"0": MONDE_V, "1": [560, 40, 340, 149], "2": MONDE_V, "4": [420, 30, 480, 210]}),
        "lec": dict(type="note", titre="La leçon", t="Les ambitions chinoises redessinent les alliances : la Chine est au cœur des rivalités de puissance du XXIe siècle.", y=230),
    }),

    # ================================================================ II.7 bilan
    dict(id="bilan", chap="Bilan : réécrire les règles ?", fond="archive", humeur="calme",
         retenir="La Chine utilise le droit quand il la sert (Montego Bay ratifiée en 1996) et le rejette quand il la contraint (sentence de 2016) ; elle propose ses propres cadres (ILRS avec la Russie). Puissance révisionniste, ou qui reprend sa place ? Second Thomas, 17 juin 2024 : abordage par des garde-côtes chinois.",
         beats=[
        "{bq}Alors, bilan. La Chine veut-elle réécrire les règles ?",
        "{-bq}{dr}Regarde son rapport au droit. {dr.g}Elle l'utilise quand il la sert : elle a ratifié la convention de Montego Bay en mille neuf cent quatre-vingt-seize. "
        "{dr.d}Et elle le rejette quand il la contraint : c'est la sentence de deux mille seize.",
        "{-dr}{ilrs}Elle propose même ses propres cadres. Par exemple, avec la Russie, un projet de station de recherche sur la Lune : l'ILRS.",
        "{-ilrs}{deux}Deux lectures s'opposent. {deux.g}Pour les uns, c'est une puissance {!révisionniste}révisionniste : elle conteste l'ordre établi par les Occidentaux. "
        "{deux.d}Pour d'autres, c'est une puissance qui reprend la place qu'elle estime lui revenir. "
        "Et ses partenaires, eux, dénoncent parfois l'endettement provoqué par certains prêts.",
        "{-deux}{st}{st.1}Un dernier exemple, pour sentir la tension sur le terrain. Le récif de Second Thomas, dans les Spratleys. "
        "Les Philippines y maintiennent un vieux navire de guerre échoué, le Sierra Madre, où vivent quelques soldats.",
        "{st.2}Le dix-sept juin deux mille vingt-quatre, des garde-côtes chinois, armés de haches et de couteaux, abordent les embarcations philippines venues le ravitailler. "
        "Un marin philippin y perd son pouce.",
        "Pas un coup de feu. Mais une violence bien réelle. C'est la rivalité de puissance au quotidien.",
    ], vis={
        "bq": dict(type="question", t="La Chine veut-elle réécrire les règles ?"),
        "dr": dict(type="cols", g="Le droit, quand il la sert", gq="Montego Bay ratifiée en 1996", d="Rejeté, quand il la contraint",
                   dq="la sentence de 2016", vs="≠"),
        "ilrs": dict(type="def", terme="L'ILRS", t="Un projet de station de recherche lunaire porté par la Chine et la Russie : proposer ses propres cadres.", y=220),
        "deux": dict(type="cols", g="Puissance révisionniste", gq="elle conteste l'ordre établi par les Occidentaux", d="Ou retour à sa place ?",
                     dq="elle reprend la place qu'elle estime lui revenir", vs="?"),
        "st": dict(type="scene", anim="voisins", etapes=THOMAS, depart=["neuf"], fs=20,
                   cam={"0": VOIS_V, "1": [150, 420, 400, 196], "2": [180, 440, 330, 162]}),
    }),

    # ================================================================ pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="crise", humeur="calme", beats=[
        "{pg}Avant le bac, les cinq pièges qui coûtent des points. "
        "{pg.1}Un : présenter la puissance chinoise comme seulement économique. Elle est aussi militaire, technologique et symbolique. "
        "{pg.2}Deux : dire que la Chine n'a pas signé la convention de Montego Bay. Elle l'a ratifiée, en mille neuf cent quatre-vingt-seize. Elle rejette la sentence de deux mille seize. "
        "{pg.3}Trois : employer « collier de perles » comme un fait. C'est une expression américaine.",
        "{pg.4}Quatre : parler de « piège de la dette » sans nuance. "
        "{pg.5}Et cinq : oublier l'échelle mondiale. Le sujet demande aussi les enjeux pour le reste du monde.",
    ], vis={
        "pg": dict(type="liste", titre="Les cinq pièges", items=[
            "Une puissance seulement économique ? Non : militaire, technologique, symbolique",
            "« La Chine n'a pas signé Montego Bay » : faux, ratifiée en 1996",
            "« Collier de perles » : une expression américaine, pas un fait",
            "« Piège de la dette » : une expression discutée",
            "Oublier l'échelle mondiale : les enjeux pour le reste du monde"], marques=["✗", "✗", "✗", "✗", "✗"], x=130, y=110, w=1020),
    }),

    # ================================================================ la dissertation
    dict(id="dissert", chap="Au bac : la dissertation", fond="archive", humeur="calme", beats=[
        "{sujet}Entraînons-nous sur un sujet de dissertation, inventé pour l'occasion. "
        "« La Chine, une puissance qui s'affirme dans les espaces maritimes et extra-atmosphériques ».",
        "{sujet.1}D'abord, les termes. « S'affirme » : c'est un processus, en cours. Il faut montrer comment, et pourquoi. "
        "{sujet.2}« Les espaces maritimes et extra-atmosphériques » : les deux, toujours ensemble. "
        "{sujet.3}Et n'oublie pas les conséquences, pour le reste du monde.",
        "{-sujet}{pz}À toi ! Mets la vidéo sur pause. Prends cinq minutes, et cherche une problématique et un plan en trois parties.{pz.stop}",
        ("P", 2.0),
        "{-pz}{pb}Voici une proposition. La problématique : comment et pourquoi la Chine fait-elle des mers et de l'espace des instruments "
        "de son affirmation de puissance, et avec quelles conséquences pour le reste du monde ?",
        "{-pb}{pl}Et le plan. {pl.1}Un : une volonté politique. Effacer le siècle d'humiliation. Le rêve chinois, en deux mille douze. "
        "Et des objectifs datés : la Lune avant deux mille trente, le renouveau pour deux mille quarante-neuf.",
        "{pl.2}Deux : des moyens considérables. Une marine de plus de trois cent soixante-dix navires, et le Fujian en deux mille vingt-cinq. "
        "Dans l'espace, Tiangong et Chang'e six. Et les routes de la soie : le Pirée, Hambantota, Gwadar.",
        "{pl.3}Trois : des tensions régionales et mondiales. En mer de Chine méridionale, la sentence de deux mille seize, puis Second Thomas en deux mille vingt-quatre. "
        "Les réponses américaines et alliées : le Quad, l'AUKUS. Et dans l'espace, deux blocs : Artemis contre l'ILRS.",
        "{-pl}{me}Le correcteur valorise la précision. Une date, un lieu, un chiffre, dans chaque paragraphe. "
        "Et ne sépare jamais la mer de l'espace : c'est leur rapprochement qui fait la force de ta copie.",
        "{-me}{go}Et au Grand oral ? Une question comme : « La Chine veut-elle réécrire les règles de la mer et de l'espace ? » "
        "Tu as maintenant tous les exemples pour y répondre, dans les deux sens.",
    ], vis={
        "sujet": dict(type="exo", niveau="dissert", titre="La Chine, une puissance qui s'affirme dans les espaces maritimes et extra-atmosphériques",
                      src="Sujet inventé pour l'entraînement (objet de travail conclusif)",
                      questions=["Analyse les termes : « s'affirme »", "Les deux espaces, toujours ensemble", "Les conséquences pour le reste du monde"]),
        "pz": dict(type="pause", t="Une problématique et un plan en trois parties pour ce sujet.",
                   sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "pb": dict(type="def", terme="Problématique", t="Comment et pourquoi la Chine fait-elle des mers et de l'espace des instruments de son affirmation de puissance, et avec quelles conséquences pour le reste du monde ?", y=170),
        "pl": dict(type="liste", titre="Un plan possible", items=[
            "Une volonté politique — siècle d'humiliation, rêve chinois (2012), la Lune avant 2030, 2049",
            "Des moyens considérables — plus de 370 navires, Fujian (2025), Tiangong, Chang'e 6, Le Pirée, Hambantota, Gwadar",
            "Des tensions régionales et mondiales — sentence de 2016, Second Thomas (2024), Quad, AUKUS, Artemis contre ILRS"],
            marques=["I", "II", "III"], x=130, y=120, w=1020),
        "me": dict(type="note", titre="Méthode", t="Une date, un lieu, un chiffre dans chaque paragraphe. Et toujours la mer et l'espace ensemble.", y=230),
        "go": dict(type="question", t="Au Grand oral : la Chine veut-elle réécrire les règles de la mer et de l'espace ?"),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap pour le bac", fond="crise", humeur="lumiere", beats=[
        "{dat}Il est temps de tout ranger. Les dates, d'abord. {dat.1}Mille neuf cent soixante-dix, le premier satellite. "
        "{dat.2}Deux mille trois, Yang Liwei. {dat.3}Deux mille douze, le rêve chinois, et le Liaoning. "
        "{dat.4}Deux mille treize, la route de la soie maritime. {dat.5}Deux mille seize, la sentence, rejetée. "
        "{dat.6}Deux mille dix-sept, Djibouti. {dat.7}Deux mille dix-neuf, la face cachée de la Lune. "
        "{dat.8}Deux mille vingt et un, l'AUKUS. {dat.9}Deux mille vingt-quatre, Chang'e six, et Second Thomas. "
        "{dat.10}Et deux mille vingt-cinq, le Fujian.",
        ("P", 1.8),
        "{-dat}{cm}Et la carte du dossier. {cm.1}Des discours, avec le rêve chinois. {cm.2}La mer : la marine et les appropriations. "
        "{cm.3}L'espace : de Tiangong à la face cachée. {cm.4}Et les réactions : le Quad, l'AUKUS, les voisins.",
        ("P", 1.2),
        "{-cm}{qd}La question qui reste ouverte : la Chine conteste-t-elle l'ordre du monde, ou y reprend-elle sa place ? À toi de trancher.",
        "{-qd}{fin}Les fiches, les QCM, la carte et l'animation de la mer de Chine t'attendent sur le site Ligne rouge : "
        "le lien est dans la description. Et ainsi se referme le thème un. Prochain dossier : faire la guerre, faire la paix. À très vite.",
        ("P", 2.5),
    ], vis={
        "dat": dict(type="chrono", titre="Les dates du dossier", items=[
            dict(d="1970", t="Premier satellite", c="espace"), dict(d="2003", t="Yang Liwei", c="espace"),
            dict(d="2012", t="Rêve chinois, Liaoning", c="mer"), dict(d="2013", t="Route de la soie maritime", c="mer"),
            dict(d="2016", t="Sentence rejetée", c="droit"), dict(d="2017", t="Base de Djibouti", c="mer"),
            dict(d="2019", t="Face cachée de la Lune", c="espace"), dict(d="2021", t="AUKUS", c="conflit"),
            dict(d="2024", t="Chang'e 6, Second Thomas", c="conflit"), dict(d="2025", t="Fujian", c="mer")],
            x=60, w=1160, y=120, h=470),
        "cm": dict(type="carte", centre="La Chine, mers et espace", branches=[
            dict(t="Des discours", items=["siècle d'humiliation", "rêve chinois (2012)", "2030, 2049"]),
            dict(t="La mer", items=["370 navires, 3 porte-avions", "îles artificielles", "routes de la soie"]),
            dict(t="L'espace", items=["Tiangong, Beidou", "face cachée (2019, 2024)", "Lune avant 2030"]),
            dict(t="Les réactions", items=["Quad (2017), AUKUS (2021)", "voisins inquiets", "sentence de 2016"])]),
        "qd": dict(type="question", t="La Chine conteste-t-elle l'ordre du monde, ou y reprend-elle sa place ?"),
        "fin": dict(type="mot", t="Ligne rouge", g="Fiches, QCM, carte et animation : le lien est dans la description.", taille=110, y=250),
    }),
]

QUIZ = [
    dict(q="Quand Xi Jinping lance-t-il l'expression de « rêve chinois » ?", r=["En 1949", "En 2003", "En novembre 2012", "En 2021"], ok=2,
         ex="Le 29 novembre 2012, deux semaines après être devenu secrétaire général du Parti.", voir="reve"),
    dict(q="Pour quelle date le « grand renouveau de la nation chinoise » est-il fixé ?", r=["2030", "2035", "2049", "2100"], ok=2,
         ex="2049, centenaire de la République populaire de Chine.", voir="rv"),
    dict(q="Quel est le troisième porte-avions chinois, mis en service le 5 novembre 2025 ?", r=["Liaoning", "Shandong", "Fujian", "Hainan"], ok=2,
         ex="Le Fujian, doté de catapultes électromagnétiques, basé à Sanya.", voir="pa"),
    dict(q="Quelle première mondiale réussit Chang'e 4 le 3 janvier 2019 ?", r=["Le premier retour d'échantillons lunaires", "Le premier atterrissage sur la face cachée de la Lune",
                                                                             "Le premier vol habité autour de la Lune", "La première station lunaire"], ok=1,
         ex="Chang'e 4 se pose sur la face cachée ; Chang'e 6 en rapporte des échantillons le 25 juin 2024.", voir="ln"),
    dict(q="Pourquoi la Chine crée-t-elle la « ville de Sansha » en 2012 ?", r=["Pour accueillir des touristes", "Pour administrer ses revendications en mer de Chine",
                                                                           "Pour lancer des fusées", "Pour y installer l'ONU"], ok=1,
         ex="S'approprier un espace, c'est aussi l'administrer et le peupler.", voir="sansha"),
    dict(q="Qu'est-ce que le « dilemme de Malacca » ?", r=["Un conflit frontalier", "La dépendance de la Chine envers un détroit que les États-Unis pourraient bloquer",
                                                         "Un traité de pêche", "Une rivalité entre deux ports"], ok=1,
         ex="Formule de Hu Jintao (2003) ; d'où Gwadar et les tubes de Kyaukpyu.", voir="ml"),
    dict(q="Quel port grec l'entreprise chinoise COSCO contrôle-t-elle ?", r=["Thessalonique", "Le Pirée", "Héraklion", "Patras"], ok=1,
         ex="51 % en 2016, 67 % en 2021 : une porte d'entrée chinoise en Europe.", voir="rt"),
    dict(q="Le « collier de perles » est…", r=["un traité signé par la Chine", "une expression américaine qui désigne les points d'appui chinois",
                                              "le nom officiel des routes de la soie", "une base chinoise"], ok=1,
         ex="C'est une représentation, pas un fait neutre.", voir="cp"),
    dict(q="Dans quel livre blanc la Chine se dit-elle « État proche de l'Arctique » ?", r=["2012", "2016", "2018", "2022"], ok=2,
         ex="Livre blanc de janvier 2018, qui propose une « route de la soie polaire ».", voir="arc"),
    dict(q="Quels pays forment l'AUKUS (15 septembre 2021) ?", r=["Australie, Royaume-Uni, États-Unis", "Inde, Japon, États-Unis, Australie",
                                                                "Australie, France, États-Unis", "Japon, Corée du Sud, États-Unis"], ok=0,
         ex="Le Quad réunit, lui, les États-Unis, le Japon, l'Inde et l'Australie.", voir="al"),
    dict(q="La Chine a-t-elle ratifié la convention de Montego Bay ?", r=["Non, jamais", "Oui, en 1996, mais elle rejette la sentence de 2016",
                                                                         "Oui, en 2016", "Elle l'a quittée en 2016"], ok=1,
         ex="Elle utilise le droit quand il la sert, et le rejette quand il la contraint.", voir="dr"),
]

CREDITS = [
    "Cartes : fond Natural Earth (domaine public), projection d3-geo (licence ISC) ; positions et tracés approximatifs ; ligne en neuf traits tracée de façon approximative.",
    "Chiffres : Pentagone (2024) ; sujet de dissertation inventé pour l'entraînement.",
    "Photographies : le porte-avions Fujian, 11 septembre 2025, ministère japonais de la Défense, état-major interarmées (CC BY 4.0), via Wikimedia Commons.",
]
