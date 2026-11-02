"""L'État, épisode 1 : « Qu'est-ce que l'État ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la justice} dans le texte lu.
Citations : Rousseau, Du contrat social, I, 3 (1762), Wikisource ; Renan, « Qu'est-ce qu'une nation ? » (1882), Wikisource ;
Weber, Le Savant et le Politique (conférence de 1919), trad. J. Freund (Plon, 1959), citation courte, début coupé.
Résumés par le narrateur : Machiavel (Le Prince, I), Louis XIV (paroles rapportées, 1715), Arendt (« Qu'est-ce que
l'autorité ? », 1961), Trotski cité par Weber, saint Augustin (La Cité de Dieu, IV, 4), les trois types de domination
légitime (Weber).
"""

CODE = "etat-1"
NOTION = "L'État"
NUM = 1
TITRE = "Qu'est-ce que l'État ?"
SUIVANT = "Épisode 2 · Pourquoi l'État ? Aristote, Hobbes, Locke, Rousseau"
PRONONCIATION = {"status": "statousse", "stare": "staré", "stato": "stato", "augere": "auguéré", "Bruegel": "Breugheul",
                 "Weber": "Wébère", "Arendt": "Arènnte", "Lorenzetti": "Lorenntsetti", "Trotski": "Trotski",
                 "Locke": "Lok"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rue}{q_jour}Une journée ordinaire. Ton réveil sonne. Tu ouvres le robinet : de l'eau potable coule. "
        "Tu prends le bus, tu passes devant le commissariat, tu entres au lycée. À midi, tu achètes un sandwich.",
        ("As-tu croisé l'État, aujourd'hui ?", {"rate": "-6%"}),
        "{-q_jour}{jour}Regarde mieux. {jour.1}L'eau du robinet est contrôlée par des services publics. "
        "{jour.2}La route, les feux, le code de la route : l'État. "
        "{-tab_rue}{tab_eco}{jour.3}Ton lycée, tes professeurs, et bientôt ton bac : l'État.",
        "{-tab_eco}{tab_imp}{jour.4}Sur ton sandwich, une taxe, la TVA, qui part dans les caisses publiques. "
        "{jour.5}Et dans ton portefeuille, une carte qui dit qui tu es, délivrée, elle aussi, par l'État.",
        "{-jour}{-tab_imp}{tab_bg}{q_ou}Tu ne l'as pas vu. Tu n'as croisé aucun ministre. Et pourtant, il était partout. "
        "Alors, où est-il, l'État ? Est-ce une personne, un bâtiment… ou une idée ?",
        "{-q_ou}{noms}Cette série va chercher à le comprendre, avec {noms.1}Aristote, {noms.2}Hobbes, {noms.3}Rousseau, "
        "{noms.4}Montesquieu, {noms.5}Marx, {noms.6}Weber… et quelques autres. "
        "{-noms}{serie}Six épisodes, et un récapitulatif. Celui-ci commence par une question toute simple.",
        ("P", 0.3),
        "{-serie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rue": dict(type="tableau", img="et1-rue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                        legende="Gustave Caillebotte, Rue de Paris, temps de pluie, 1877 (Art Institute of Chicago)"),
        "q_jour": dict(type="question", t="As-tu croisé l'État, aujourd'hui ?"),
        "jour": dict(type="liste", titre="Une journée ordinaire", items=[
            "L'eau du robinet : contrôlée par des services publics",
            "La route, les feux, le code de la route",
            "Le lycée, les professeurs, le bac",
            "La TVA sur ton sandwich",
            "Ta carte d'identité"], marques=["1", "2", "3", "4", "5"], x=170, y=120, w=940),
        "tab_eco": dict(type="tableau", img="et1-ecole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Albert Anker, L'École du village en 1848, 1896 (Kunstmuseum, Bâle)"),
        "tab_imp": dict(type="tableau", img="et1-impot", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Pieter Brueghel le Jeune, Le Paiement de l'impôt (Le Collecteur d'impôts), 1620-1640 (USC Fisher Museum of Art)"),
        "tab_bg": dict(type="tableau", img="et1-bongouv", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .72, .4],
                       legende="Ambrogio Lorenzetti, Allégorie du bon gouvernement, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "q_ou": dict(type="question", t="Où est-il, l'État ? Une personne, un bâtiment, une idée ?"),
        "noms": dict(type="nuage", items=["Aristote", "Hobbes", "Rousseau", "Montesquieu", "Marx", "Weber"]),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="partout… et pourtant invisible", y=270),
        "titre": dict(type="titre", sur="L'État · Épisode 1", t="Qu'est-ce que l'État ?",
                      sous="Le mot, les distinctions, Weber, les trois légitimités"),
    }),

    # ------------------------------------------------------------------ I. le mot et la chose
    dict(id="mot", chap="Le mot et la chose", fond="aube", humeur="mystere", notions=["le temps", "le travail"],
         retenir="L'État : l'institution qui demeure quand les gouvernants passent. À distinguer du gouvernement, de la nation, de la société civile.",
         beats=[
        "{tab_pri}{etym}Commençons par le mot. État vient du latin {etym.1}status : la manière de se tenir, debout. "
        "Le verbe, c'est {etym.2}stare : se tenir, rester, demeurer. L'État, c'est ce qui tient… et ce qui reste.",
        "{etym.3}Au seizième siècle, un Florentin, Machiavel, donne au mot italien stato un sens nouveau : "
        "non plus l'état d'une chose, mais le pouvoir qui commande à des hommes sur un territoire. "
        "Son Prince s'ouvre ainsi : tous les États ont été, et sont, ou des républiques, ou des principautés. "
        "Nous le retrouverons dans l'épisode cinq.",
        "{-etym}{-tab_pri}{tab_lou}{lou}Cent cinquante ans plus tard, en France. On prête à Louis Quatorze une formule célèbre : "
        "{lou.1}l'État, c'est moi. Il ne l'a sans doute jamais prononcée. Sur son lit de mort, en 1715, "
        "il aurait dit exactement le contraire.",
        ("{lou.2}Je m'en vais… mais l'État demeurera toujours.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-lou}{def_e}Voilà la première leçon. Le roi meurt ; l'État {#le temps}demeure. "
        "{def_e.1}L'État n'est pas une personne : c'est une institution, un pouvoir qui dure au-delà de ceux qui l'exercent, "
        "et qui s'exerce sur un territoire et sur une population.",
        "{-def_e}{-tab_lou}{tab_suf}{gv}D'où une première distinction. {gv.g}Le gouvernement, ce sont ceux qui dirigent "
        "à un moment donné : ils changent après une élection. {gv.d}L'État, c'est ce qui demeure : les administrations, "
        "l'armée, la justice, l'école, les impôts.",
        ("Le gouvernement passe ; l'État reste.", {"rate": "-5%"}),
        "{-gv}{-tab_suf}{tab_fed}{nation}Deuxième distinction : l'État et la nation. La nation, c'est un peuple qui se sent uni : "
        "par une histoire, une langue, une mémoire, et surtout par la volonté de vivre ensemble. "
        "En 1882, l'historien Ernest Renan en donne une définition restée célèbre.",
        "{-nation}",
        ("C", "L'existence d'une nation est (pardonnez-moi cette métaphore) un plébiscite de tous les jours.", "c_renan"),
        "{-c_renan}{ne}Et les deux ne coïncident pas toujours. {ne.1}Il existe des nations sans État : les Kurdes, par exemple, "
        "partagés entre plusieurs pays. {ne.2}Et des États qui réunissent plusieurs peuples et plusieurs langues : "
        "la Suisse, la Belgique.",
        "{-ne}{-tab_fed}{tab_bru}{sc}Troisième distinction, enfin : l'État et la société civile. "
        "{sc.g}La société civile, c'est tout ce que les hommes font ensemble sans que l'État l'organise : "
        "les familles, les marchés, le {#le travail}travail, les associations, les fêtes. "
        "Regarde ce tableau de Bruegel : une ville entière qui vit, échange, se dispute… sans un seul soldat.",
        "{sc.d}L'État, lui, se tient au-dessus : il fixe les règles du jeu, et il les fait respecter. "
        "Jusqu'où ? Ce sera toute la question de cette série.",
        "{-sc}{-tab_bru}",
    ], vis={
        "tab_pri": dict(type="tableau", img="et1-prince", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Machiavel, Il Principe, Rome, Antonio Blado, 1532, page de titre"),
        "etym": dict(type="liste", titre="ÉTAT", items=[
            "status (latin) : la manière de se tenir, debout", "stare : se tenir, rester, demeurer",
            "Machiavel, Le Prince (1513) : lo stato, le pouvoir qui commande sur un territoire"],
                     marques=["1", "2", "→"], cles=["debout", "demeurer", "territoire"], x=170, y=170, w=940),
        "tab_lou": dict(type="tableau", img="et1-louis14", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .2],
                        legende="Hyacinthe Rigaud, Louis XIV en costume de sacre, 1701 (musée du Louvre)"),
        "lou": dict(type="dialogue", lignes=["« L'État, c'est moi. »", "« Je m'en vais, mais l'État demeurera toujours. »"],
                    src="la première : sans doute jamais prononcée · la seconde : paroles rapportées, 26 août 1715",
                    x=170, y=200, w=940),
        "def_e": dict(type="def", cles=["institution", "dure"], terme="L'État",
                      t="Une institution : un pouvoir qui dure au-delà de ceux qui l'exercent.",
                      etape="Il s'exerce sur un territoire et sur une population.", x=170, y=200, w=940),
        "tab_suf": dict(type="tableau", img="et1-suffrage", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Alfred-Henri Bramtot, Le Suffrage universel, esquisse pour la mairie des Lilas, 1891 (Petit Palais, Paris)"),
        "gv": dict(type="cols", g="Le gouvernement", gq="ceux qui dirigent, à un moment donné : ils changent",
                   d="L'État", dq="ce qui demeure : administrations, armée, justice, école, impôts", vs="≠"),
        "tab_fed": dict(type="tableau", img="et1-federation", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .6],
                        legende="Charles Thévenin, La Fête de la Fédération, 14 juillet 1790 (musée Carnavalet, Paris)"),
        "nation": dict(type="def", cles=["uni", "vivre ensemble"], terme="La nation",
                       t="Un peuple qui se sent uni : une histoire, une langue, une mémoire.",
                       etape="Et surtout : la volonté de vivre ensemble.", x=170, y=200, w=940),
        "c_renan": dict(type="cit", a="Ernest Renan", o="« Qu'est-ce qu'une nation ? », conférence à la Sorbonne (1882)",
                        x=170, y=200, w=940),
        "ne": dict(type="liste", titre="État et nation ne coïncident pas toujours", items=[
            "Des nations sans État : les Kurdes", "Des États à plusieurs peuples et plusieurs langues : la Suisse, la Belgique"],
                   marques=["1", "2"], x=170, y=190, w=940),
        "tab_bru": dict(type="tableau", img="et1-bruegel", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.45, .55, .55],
                        legende="Pieter Bruegel l'Ancien, Le Combat de Carnaval et Carême, 1559 (Kunsthistorisches Museum, Vienne)"),
        "sc": dict(type="cols", g="La société civile", gq="familles, marchés, travail, associations, fêtes",
                   d="L'État", dq="au-dessus : il fixe les règles du jeu et les fait respecter", vs="≠"),
    }),

    # ------------------------------------------------------------------ II. puissance, pouvoir, autorité
    dict(id="pouvoir", chap="Puissance, pouvoir, autorité", fond="nuit", humeur="tension", notions=["la justice", "le devoir"],
         retenir="Puissance : imposer par la force. Pouvoir : le droit de commander. Autorité : le pouvoir reconnu, obéi sans menace. La force ne fait pas le droit.",
         beats=[
        "{tab_col}{trois}Un État commande. Mais commander, qu'est-ce que c'est ? Trois mots, qu'on emploie souvent "
        "l'un pour l'autre, vont nous aider. {trois.1}La puissance, d'abord : c'est la capacité d'imposer sa volonté, "
        "par la force s'il le faut. Une armée, une tempête, un géant ont de la puissance.",
        "{-tab_col}{tab_ste}{trois.2}Le pouvoir, ensuite : c'est une puissance installée, organisée, qui a le droit de commander. "
        "Le juge, le maire, le ministre ont un pouvoir : il leur vient de leur fonction.",
        "{trois.3}L'autorité, enfin : c'est le pouvoir reconnu, celui auquel on obéit sans qu'il ait besoin de menacer. "
        "Le mot vient du latin augere, augmenter : l'autorité grandit celui qui la porte. "
        "Pense au professeur qui obtient le silence d'un seul regard… {-trois}et à celui qui doit crier, menacer, punir, "
        "comme le maître d'école de Jan Steen.",
        "{arendt}{aut}Hannah Arendt l'a souligné : l'autorité ne repose ni sur la contrainte, ni sur la persuasion, "
        "mais sur la reconnaissance. Là où l'on doit employer la force, l'autorité a déjà échoué.",
        ("Plus un pouvoir a besoin de frapper, moins il a d'autorité.", {"rate": "-5%"}),
        "{-arendt}{-aut}{-tab_ste}{tab_con}{rous}C'est exactement le problème de tout État. Rousseau l'a dit en une phrase.",
        ("C", "Le plus fort n'est jamais assez fort pour être toujours le maître, s'il ne transforme sa force en droit "
              "et l'obéissance en devoir.", "c_rous"),
        "{-rous}{-c_rous}{ll}On l'a vu dans la série sur le devoir. {ll.g}Est légal ce qui est conforme à la loi. "
        "{ll.d}Est légitime ce qui est {#la justice}juste, ce qui mérite d'être obéi. Et Rousseau tranche : "
        "la force ne fait pas le droit.",
        "{-ll}{q_leg}Un État peut-il durer par la seule force ? Non. Il lui faut être reconnu, cru, accepté. "
        "Il lui faut une {!légitimité}légitimité. Et c'est là que commence l'analyse d'un sociologue allemand : Max Weber.",
        "{-q_leg}{-tab_con}",
    ], vis={
        "tab_col": dict(type="tableau", img="et1-colosse", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .45, .3],
                        legende="Attribué à Francisco de Goya, Le Colosse, vers 1808-1812 (musée du Prado, Madrid)"),
        "trois": dict(type="cartes", items=[
            dict(ic="porte", t="Puissance", q="imposer sa volonté, par la force"),
            dict(ic="colonnes", t="Pouvoir", q="le droit de commander, attaché à une fonction"),
            dict(ic="chemins", t="Autorité", q="le pouvoir reconnu, obéi sans menace")]),
        "tab_ste": dict(type="tableau", img="et1-steen", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .4, .4],
                        legende="Jan Steen, L'École de village, vers 1665 (National Gallery of Ireland, Dublin)"),
        "arendt": dict(type="portrait", annee=1906, img="arendt", nom="Hannah Arendt", dates="1906 – 1975",
                       legende="La Crise de la culture (1961)", x=110, y=120, w=330, h=420),
        "aut": dict(type="note", titre="Arendt · l'autorité", cles=["reconnaissance", "échoué"],
                    t="Ni contrainte, ni persuasion : la reconnaissance.",
                    etape="Là où l'on doit employer la force, l'autorité a échoué (« Qu'est-ce que l'autorité ? », 1961, résumé).",
                    x=640, y=180, w=570),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .5, .5],
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "rous": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                     legende="Du contrat social, I, 3 (1762)", x=110, y=120, w=330, h=420),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 3 (1762)", x=640, y=170, w=570),
        "ll": dict(type="cols", g="Légal", gq="conforme à la loi", d="Légitime", dq="juste : ce qui mérite d'être obéi",
                   vs="≠", repere="Repère · légal / légitime (voir la série « Le devoir », épisode 1)"),
        "q_leg": dict(type="question", t="Un État peut-il durer par la seule force ?"),
    }),

    # ------------------------------------------------------------------ III. Weber : le monopole
    dict(id="weber", chap="Le monopole de la violence légitime", fond="aube", humeur="tension", notions=["la justice", "la liberté"],
         retenir="Weber : l'État revendique avec succès, sur un territoire, le monopole de la violence physique légitime. Sans légitimité, une bande de brigands.",
         beats=[
        "{tab_ber}{an}Munich, le 28 janvier 1919. L'Allemagne vient de perdre la guerre. L'empereur a abdiqué, "
        "des révolutionnaires tiennent les rues, on se bat à Berlin. Devant des étudiants, Max Weber donne une conférence : "
        "le métier et la vocation d'homme politique.",
        "{-an}{weber}{q_web}Il pose une question simple : qu'est-ce qui distingue l'État de tous les autres groupes humains ? "
        "Pas ses buts : l'État s'est occupé de tout, de la guerre, des routes, des écoles, de la religion. "
        "{-q_web}Ce qui le définit, c'est un moyen. Weber cite le révolutionnaire russe Trotski : tout État est fondé sur la force. "
        "Et il en tire la définition la plus célèbre de la science politique.",
        ("C", "… une communauté humaine qui, dans les limites d'un territoire déterminé, revendique avec succès "
              "pour son propre compte le monopole de la violence physique légitime.", "c_weber"),
        "{-weber}{-c_weber}{-tab_ber}{tab_duel}{mono}Pèse chaque mot. {mono.1}Un territoire : l'État s'arrête à ses frontières. "
        "{mono.2}La violence physique : arrêter, enfermer, contraindre, et, à la guerre, tuer. "
        "{mono.3}Le {!monopole}monopole : l'État ne partage pas ce droit. {mono.4}Légitime : cette violence est reconnue comme permise. "
        "{mono.5}Et revendique avec succès : un État qui n'arrive plus à l'imposer cesse d'en être un.",
        "{-mono}{vg}Regarde ce duel, peint par Gérôme : deux hommes ont réglé leur querelle à l'épée, à l'aube, dans la neige. "
        "{vg.g}Pendant des siècles, se faire justice soi-même allait de soi : la vengeance, le duel, la vendetta. "
        "{vg.d}L'État moderne l'interdit. C'est la police qui arrête, le juge qui condamne. "
        "Personne n'a plus le droit de se venger. En échange, chacun peut vivre en sécurité, et user de sa liberté sans craindre son voisin.",
        "{-vg}{-tab_duel}{tab_aug}{q_maf}Mais alors, quelle différence entre un État et une mafia ? Les deux prélèvent de l'argent, "
        "les deux menacent. Au cinquième siècle, saint Augustin posait déjà la question : sans la justice, "
        "que sont les royaumes, sinon de grandes bandes de brigands ?",
        "{-q_maf}{cm}{cm.1}La réponse, c'est la légitimité. Le racketteur se fait obéir par la peur ; l'État, parce qu'on reconnaît son droit. "
        "{cm.2}Attention donc au contresens : Weber ne dit pas que toute violence de l'État est légitime. "
        "Une police qui frappe sans droit perd justement ce qui la distingue d'une bande armée.",
        "{-cm}{-tab_aug}",
    ], vis={
        "tab_ber": dict(type="tableau", img="et1-berlin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .55],
                        legende="Combats de rue à Berlin, mars 1919 (photographie de presse, domaine public)"),
        "an": dict(type="mot", t="1919", g="Munich · Weber, « Le métier et la vocation d'homme politique »", y=270, taille=110),
        "weber": dict(type="portrait", annee=1864, img="weber", nom="Max Weber", dates="1864 – 1920",
                      legende="Le Savant et le Politique (1919)", x=110, y=120, w=330, h=420),
        "q_web": dict(type="note", titre="La question de Weber", cles=["distingue"],
                      t="Qu'est-ce qui distingue l'État de tous les autres groupes humains ?",
                      etape="Pas ses buts : un moyen qui lui est propre.", x=640, y=180, w=570),
        "c_weber": dict(type="cit", a="Max Weber", o="Le Savant et le Politique (1919), trad. J. Freund", x=640, y=150, w=570),
        "tab_duel": dict(type="tableau", img="et1-duel", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .6],
                         legende="Jean-Léon Gérôme, Le Duel après le bal masqué, vers 1857-1859"),
        "mono": dict(type="liste", titre="Pèse chaque mot", items=[
            "Un territoire : l'État s'arrête à ses frontières",
            "La violence physique : arrêter, enfermer, contraindre",
            "Le monopole : l'État ne partage pas ce droit",
            "Légitime : reconnue comme permise",
            "Revendique avec succès : sinon, plus d'État"], marques=["1", "2", "3", "4", "5"], x=170, y=110, w=940),
        "vg": dict(type="cols", g="Se faire justice soi-même", gq="vengeance, duel, vendetta", d="L'État moderne",
                   dq="la police arrête, le juge condamne", vs="→"),
        "tab_aug": dict(type="tableau", img="et1-augustin", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .6, .3],
                        legende="Sandro Botticelli, Saint Augustin dans son cabinet de travail, 1480, détail (église d'Ognissanti, Florence)"),
        "q_maf": dict(type="question", t="Sans la justice, que sont les royaumes, sinon de grandes bandes de brigands ?"),
        "cm": dict(type="liste", titre="État ou bande de brigands ?", items=[
            "La différence : la légitimité. On obéit parce qu'on reconnaît un droit",
            "Contresens : toute violence de l'État n'est pas légitime"], marques=["→", "!"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ IV. trois légitimités
    dict(id="legitimites", chap="Pourquoi obéit-on ?", fond="nuit", humeur="lumiere", notions=["la religion", "la raison"],
         retenir="Trois légitimités (Weber) : la tradition, le charisme, la légalité rationnelle. Des types purs, mêlés dans la réalité.",
         beats=[
        "{tab_jea}{lg}Pourquoi obéit-on ? Weber répond : il existe trois grandes sources de légitimité. "
        "Trois raisons de croire qu'un pouvoir a le droit de commander.",
        "{lg.1}La première, c'est la tradition. On obéit parce qu'on a toujours obéi : au roi, fils de roi, sacré à Reims "
        "comme ses ancêtres. Regarde Jeanne d'Arc au sacre de Charles Sept, en 1429 : la couronne, l'huile sainte, "
        "la cathédrale. Le sacre relie le pouvoir au passé, et à la {#la religion}religion.",
        "{-tab_jea}{tab_bon}{lg.2}La deuxième, c'est le charisme. On obéit à un homme, pour ses qualités extraordinaires : "
        "ses exploits, sa parole, son audace. Le prophète, le chef de guerre, le héros. Bonaparte franchissant les Alpes : "
        "c'est ainsi qu'il voulait être vu. Mais le charisme ne s'hérite pas : il doit sans cesse se prouver.",
        "{-tab_bon}{tab_bur}{lg.3}La troisième, c'est la légalité, que Weber dit {#la raison}rationnelle. On obéit à des règles écrites, "
        "impersonnelles, les mêmes pour tous. Le policier qui t'arrête, tu ne lui obéis pas parce que c'est lui, "
        "mais à cause de sa fonction.",
        "{-lg}{bur}C'est le règne de l'administration : des bureaux, des dossiers, des procédures. Rien d'héroïque. "
        "{bur.1}Mais un immense progrès : on n'obéit plus à une personne, on obéit à la règle. "
        "Et le pouvoir du fonctionnaire s'arrête là où s'arrête la loi.",
        "{-bur}{-tab_bur}{tab_syn}{mix}Attention : ce sont des types purs, des modèles. {mix.1}Dans la réalité, ils se mélangent. "
        "Un président élu exerce un pouvoir légal ; mais il lui faut un peu de charisme, et il s'entoure volontiers de traditions : "
        "le palais, les cérémonies, le défilé du 14 juillet.",
        "{mix.2}Et un pouvoir charismatique qui veut durer doit devenir tradition, ou loi. Le héros meurt ; il faut alors "
        "des règles pour désigner son successeur.",
        "{-mix}{-tab_syn}",
    ], vis={
        "tab_jea": dict(type="tableau", img="et1-jeanne", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .45, .25],
                        legende="Jean-Auguste-Dominique Ingres, Jeanne d'Arc au sacre du roi Charles VII, 1854 (musée du Louvre)"),
        "lg": dict(type="cartes", items=[
            dict(ic="colonnes", t="La tradition", q="on a toujours obéi : le roi, le sacre"),
            dict(ic="chemins", t="Le charisme", q="un être extraordinaire : le héros, le prophète"),
            dict(ic="porte", t="La légalité", q="des règles impersonnelles : la fonction")]),
        "tab_bon": dict(type="tableau", img="et1-bonaparte", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .45, .25],
                        legende="Jacques-Louis David, Bonaparte franchissant le Grand-Saint-Bernard, 1801-1805"),
        "tab_bur": dict(type="tableau", img="et1-bureau", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Edgar Degas, Le Bureau de coton à La Nouvelle-Orléans, 1873 (musée des Beaux-Arts, Pau)"),
        "bur": dict(type="def", cles=["règle", "loi"], terme="La domination légale-rationnelle",
                    t="Obéir à des règles écrites et impersonnelles, non à une personne.",
                    etape="Le pouvoir du fonctionnaire s'arrête là où s'arrête la loi.", x=170, y=200, w=940),
        "tab_syn": dict(type="tableau", img="et1-syndics", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Rembrandt, Les Syndics de la guilde des drapiers, 1662 (Rijksmuseum, Amsterdam)"),
        "mix": dict(type="liste", titre="Des types purs, mêlés dans la réalité", items=[
            "Un président élu : la loi, un peu de charisme, des traditions",
            "Le charisme qui veut durer devient tradition, ou loi"], marques=["1", "2"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ V. les grandes questions
    dict(id="questions", chap="Les grandes questions", fond="aube", humeur="mystere", notions=["la liberté", "la justice"],
         retenir="L'État nous protège… et pourrait nous écraser. D'où la série : pourquoi l'État ? Protège-t-il ou menace-t-il la liberté ? Peut-on s'en passer ? Peut-il être juste ?",
         beats=[
        "{tab_eff}{para}Résumons. {para.1}L'État est partout, et pourtant invisible : on ne voit que ses agents, ses bâtiments, ses papiers. "
        "{para.2}Il a le monopole de la force, mais il ne tient que s'il est reconnu. "
        "{para.3}Et il nous protège… mais il pourrait aussi nous écraser.",
        "{-para}{bm}Au quatorzième siècle, à Sienne, le peintre Ambrogio Lorenzetti couvre les murs de l'hôtel de ville "
        "de deux fresques qui se répondent. {bm.g}D'un côté, le bon gouvernement : une ville en paix, où l'on danse, "
        "où l'on commerce, où l'on bâtit. {bm.d}De l'autre, le mauvais : la Tyrannie, et une ville en ruine.",
        "Sept siècles plus tard, ces fresques posent encore notre question.",
        "{-bm}{qs}{qs.1}Pourquoi l'État ? Est-il naturel, ou né d'un contrat ? Épisode deux : Aristote, Hobbes, Locke, Rousseau. "
        "{qs.2}L'État protège-t-il notre {#la liberté}liberté, ou la menace-t-il ? Épisode trois : Montesquieu, Spinoza, "
        "et le totalitarisme, avec Hannah Arendt et le 1984 d'Orwell. "
        "{qs.3}Peut-on se passer de l'État ? Épisode quatre : La Boétie, Marx, les anarchistes, Nietzsche.",
        "{qs.4}L'État peut-il être juste ? Épisode cinq : Platon, Machiavel, Hegel, Rawls. {qs.5}Et l'épisode six : ta copie.",
        ("P", 0.8),
        "{-qs}{-tab_eff}",
    ], vis={
        "tab_eff": dict(type="tableau", img="et1-effets", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.0, .7, .5],
                        legende="Ambrogio Lorenzetti, Effets du bon gouvernement dans la ville, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "para": dict(type="liste", titre="Le paradoxe de l'État", items=[
            "Partout, et pourtant invisible", "Le monopole de la force… s'il est reconnu",
            "Il nous protège… et pourrait nous écraser"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "bm": dict(type="cols", g="Le bon gouvernement", gq="la paix : on danse, on commerce, on bâtit",
                   d="Le mauvais gouvernement", dq="la Tyrannie : une ville en ruine", vs="≠"),
        "qs": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · Pourquoi l'État ? Aristote, Hobbes, Locke, Rousseau",
            "Ép. 3 · L'État et la liberté : Montesquieu, Spinoza, Arendt, Orwell",
            "Ép. 4 · Contre l'État ? La Boétie, Marx, les anarchistes, Nietzsche",
            "Ép. 5 · L'État et la justice : Platon, Machiavel, Hegel, Rawls",
            "Ép. 6 · L'État à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le mot. Status, ce qui se tient debout : "
        "l'État est l'institution qui demeure quand les gouvernants passent. À distinguer du gouvernement, de la nation "
        "et de la société civile.",
        "{rec.2}Deux : puissance, pouvoir, autorité. Et une règle : la force ne fait pas le droit. "
        "Tout pouvoir cherche à devenir légitime.",
        "{rec.3}Trois : Weber. L'État revendique, sur un territoire, le monopole de la violence physique légitime.",
        "{rec.4}Quatre : on obéit par tradition, par charisme, ou par légalité.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Reste une question. Avant l'État, qu'y avait-il ? "
        "Et pourquoi des hommes nés libres ont-ils accepté d'obéir ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : pourquoi l'État ? Aristote, Hobbes, Locke, et Rousseau.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="et1-bongouv", fond=True, sombre=True, de=[1.3, .3, .45], a=[1.0, .5, .5],
                        legende="Ambrogio Lorenzetti, Allégorie du bon gouvernement, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "rec": dict(type="carte", centre="L'ÉTAT", branches=[
            dict(t="Le mot", items=["status : ce qui demeure", "≠ gouvernement, nation", "≠ société civile"]),
            dict(t="Commander", items=["puissance, pouvoir, autorité", "légal / légitime", "la force ne fait pas le droit"]),
            dict(t="Weber (1919)", items=["un territoire", "le monopole", "de la violence physique légitime"]),
            dict(t="Trois légitimités", items=["la tradition", "le charisme", "la légalité rationnelle"])]),
        "tab_fin": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .25],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651"),
        "q_suite": dict(type="question", t="Pourquoi des hommes nés libres ont-ils accepté d'obéir ?"),
        "fin": dict(type="titre", sur="À suivre", t="Pourquoi l'État ?", sous="Épisode 2 · Aristote, Hobbes, Locke, Rousseau"),
    }),
]

QUIZ = [
    dict(q="D'où vient le mot « État » ?",
         r=["Du grec polis, la cité", "Du latin status, la manière de se tenir debout", "De l'italien stella, l'étoile",
            "Du latin auctoritas, l'autorité"], ok=1,
         voir="etym", ex="Status, du verbe stare : se tenir, demeurer. L'État est ce qui demeure quand les gouvernants passent. Machiavel lui donne son sens moderne (lo stato)."),
    dict(q="Après une élection, qu'est-ce qui change ?",
         r=["L'État", "La nation", "Le gouvernement", "La société civile"], ok=2,
         voir="gv", ex="Le gouvernement, ce sont ceux qui dirigent à un moment donné ; l'État (administrations, justice, armée, école) demeure."),
    dict(q="« Un plébiscite de tous les jours » : de quoi Renan parle-t-il ?",
         r=["De l'État", "De la démocratie", "De la nation", "Du gouvernement"], ok=2,
         voir="c_renan", ex="Pour Renan (1882), la nation repose sur la volonté de vivre ensemble, sans cesse renouvelée. Nation et État ne coïncident pas toujours (les Kurdes, la Suisse)."),
    dict(q="Le professeur qui obtient le silence d'un seul regard a…",
         r=["de la puissance", "de l'autorité", "de la violence légitime", "du charisme seulement"], ok=1,
         voir="trois", ex="L'autorité est le pouvoir reconnu, obéi sans menace. Pour Arendt, là où il faut employer la force, l'autorité a échoué."),
    dict(q="Selon Weber, ce qui définit l'État, c'est…",
         r=["le bien commun", "le monopole de la violence physique légitime sur un territoire",
            "l'élection de ses dirigeants", "la défense de la religion"], ok=1,
         voir="c_weber", ex="Le Savant et le Politique (1919) : l'État se définit par un moyen, non par ses buts. Il revendique avec succès ce monopole."),
    dict(q="Qu'est-ce qui distingue l'État d'une bande de brigands ?",
         r=["Le nombre de ses membres", "La légitimité : on reconnaît son droit de commander",
            "Rien, comme le montre saint Augustin", "L'argent qu'il prélève"], ok=1,
         voir="cm", ex="Saint Augustin : sans la justice, les royaumes ne sont que de grandes bandes de brigands. Et toute violence de l'État n'est pas légitime pour autant."),
    dict(q="Un policier à qui l'on obéit « à cause de sa fonction » illustre la légitimité…",
         r=["traditionnelle", "charismatique", "légale-rationnelle", "religieuse"], ok=2,
         voir="lg", ex="On obéit à des règles impersonnelles, non à la personne. Le pouvoir du fonctionnaire s'arrête là où s'arrête la loi."),
]

CREDITS = [
    "Portraits : Max Weber (photographie, 1918) ; Jean-Jacques Rousseau (Maurice Quentin de La Tour, 1753) ; "
    "Hannah Arendt (photographie, voir les crédits de la série « Le devoir »)",
    "Tableaux et fresques : Gustave Caillebotte, Rue de Paris, temps de pluie (1877) ; Albert Anker, L'École du village en 1848 (1896) ; "
    "Pieter Brueghel le Jeune, Le Paiement de l'impôt (1620-1640) ; Ambrogio Lorenzetti, Allégorie et Effets du bon gouvernement "
    "(1338-1339) ; Hyacinthe Rigaud, Louis XIV (1701) ; Alfred-Henri Bramtot, Le Suffrage universel (1891) ; "
    "Charles Thévenin, La Fête de la Fédération (1790) ; Pieter Bruegel l'Ancien, Le Combat de Carnaval et Carême (1559) ; "
    "Goya (attribué), Le Colosse (vers 1808-1812) ; Jan Steen, L'École de village (vers 1665) ; "
    "Jean-Léon Gérôme, Le Duel après le bal masqué (vers 1857-1859) ; Sandro Botticelli, Saint Augustin (1480) ; "
    "Ingres, Jeanne d'Arc au sacre de Charles VII (1854) ; Jacques-Louis David, Bonaparte franchissant le Grand-Saint-Bernard (1801-1805) ; "
    "Edgar Degas, Le Bureau de coton à La Nouvelle-Orléans (1873) ; Rembrandt, Les Syndics des drapiers (1662) ; "
    "Abraham Bosse, frontispice du Léviathan (1651) : domaine public",
    "Documents et photographies : Machiavel, Il Principe (Blado, 1532) ; Du contrat social (1762) ; combats de rue à Berlin, mars 1919 "
    "(photographie de presse) : domaine public",
    "Citations : Rousseau, Du contrat social (1762) ; Ernest Renan, « Qu'est-ce qu'une nation ? » (1882) ; Max Weber, Le Savant et le "
    "Politique, trad. Julien Freund (Plon, 1959), citation courte. Machiavel, Louis XIV, Arendt, Trotski et saint Augustin sont résumés "
    "par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
