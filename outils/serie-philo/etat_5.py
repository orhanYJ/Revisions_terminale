"""L'État, épisode 5 : « L'État et la justice »

Même format que les séries « La liberté », « Le devoir », « Le bonheur » et « La conscience » (voir liberte_1.py, devoir_3.py).
Citations : Platon, La République, V, 473c-d, trad. Victor Cousin, vérifiée sur Wikisource ;
Machiavel, Le Prince, XV et XVIII (1513, publié en 1532), trad. Jean-Vincent Périès, vérifiée sur Wikisource ;
Préambule de la Constitution du 27 octobre 1946, alinéa 11.
Paraphrases du narrateur : la Septième Lettre attribuée à Platon, la lettre de Machiavel à Vettori (10 décembre 1513),
Hegel (Principes de la philosophie du droit, 1820, § 257), Weber (Le Métier et la vocation d'homme politique, 1919),
Beveridge (rapport de 1942), Nozick (Anarchie, État et utopie, 1974), Rawls (Théorie de la justice, 1971 : œuvre protégée).
"""

CODE = "etat-5"
NOTION = "L'État"
NUM = 5
TITRE = "L'État et la justice"
SUIVANT = "Épisode 6 · L'État à l'épreuve du bac"
PRONONCIATION = {"Machiavel": "Makiavel", "Ramiro d'Orco": "Ramiro dOrko", "Césène": "Cézène", "Juvénal": "Juvénal",
                 "Beveridge": "Bévéridje", "Nozick": "Nozik", "Rawls": "Rôlz", "Riis": "Riisse", "Vettori": "Vèttori"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_syr}{q1}Syracuse, en Sicile, vers 367 avant notre ère. Un homme de soixante ans débarque au port. "
        "C'est le philosophe le plus célèbre de la Grèce : Platon. On l'a fait venir pour une mission insensée : "
        "faire d'un tyran un philosophe.",
        "{-q1}{sic}{sic.1}Le jeune Denys vient d'hériter du pouvoir absolu sur la plus riche cité grecque d'Occident. "
        "Son oncle, Dion, disciple de Platon, rêve d'en faire un roi sage. {sic.2}Platon hésite, puis il accepte : "
        "s'il refusait, raconte une lettre qu'on lui attribue, il craindrait de n'être qu'un beau parleur, incapable de passer aux actes.",
        "{sic.3}L'aventure tourne mal. Dion est exilé ; Platon, retenu au palais, est presque un prisonnier. "
        "Lors d'un dernier voyage, il faudra qu'un ami envoie un navire pour le tirer de là.",
        ("Le tyran n'est pas devenu philosophe.", {"rate": "-6%"}),
        "{-sic}{q2}Mais la question de Platon, elle, n'a pas vieilli. Qui doit gouverner ? Les plus sages ? Les plus habiles ? "
        "Ou tout le monde ? Et l'État peut-il être juste… ou seulement efficace ?",
        ("P", 0.3),
        "{-q2}{-tab_syr}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_syr": dict(type="tableau", img="et5-syracuse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .55],
                        legende="Le théâtre grec de Syracuse, Vᵉ siècle av. J.-C. (photo Pequod76, domaine public)"),
        "q1": dict(type="question", t="Faire d'un tyran un philosophe ?"),
        "sic": dict(type="liste", titre="Platon à Syracuse", items=[
            "Denys, jeune tyran ; Dion, son oncle, rêve d'un roi sage", "Platon accepte, pour ne pas être qu'un beau parleur",
            "Dion exilé, Platon presque prisonnier"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "q2": dict(type="question", t="Qui doit gouverner ? Et l'État peut-il être juste ?"),
        "titre": dict(type="titre", sur="L'État · Épisode 5", t="L'État et la justice",
                      sous="Platon, Machiavel, Hegel, Rawls"),
    }),

    # ------------------------------------------------------------------ I. Platon
    dict(id="platon", chap="Les philosophes rois", fond="aube", humeur="mystere",
         notions=["la justice", "la vérité", "la raison"],
         retenir="Platon : la cité juste, c'est chacun à sa place ; gouverner est un savoir, réservé aux philosophes. Objection : qui gardera les gardiens ?",
         beats=[
        "{platon}{tab_aca}Pour comprendre ce rêve, il faut revenir à Athènes. En 399, un tribunal populaire a condamné à mort "
        "Socrate, le maître de Platon : on l'a vu dans la série sur la liberté. Platon en garde une méfiance profonde envers "
        "le pouvoir de la foule. Il fonde une école, l'Académie, et écrit la République.",
        "{-platon}{-tab_aca}{tab_ath}{cite}Qu'est-ce qu'une cité juste ? Elle a trois parties. {cite.1}Ceux qui produisent : "
        "paysans, artisans, marchands. {cite.2}Ceux qui la gardent : les guerriers. {cite.3}Et ceux qui gouvernent. "
        "La {#la justice}justice, c'est que chacun fasse ce pour quoi il est fait, sans empiéter sur la tâche des autres. "
        "Comme dans une âme bien réglée, où la raison commande au courage et aux désirs.",
        "{-cite}{-tab_ath}{tab_nef}{nav}Mais qui doit gouverner ? Platon répond par une image : le navire. "
        "{nav.1}Sur un bateau, les matelots se disputent la barre. Chacun prétend savoir naviguer, sans avoir jamais appris. "
        "Ils flattent l'armateur, un peu sourd et myope, pour obtenir le gouvernail. {nav.2}Et le vrai pilote, celui qui étudie "
        "les saisons, le ciel, les astres et les vents, ils le traitent de bavard et de rêveur.",
        ("{nav.3}Gouverner, pour Platon, est un savoir. Comme la médecine, ou la navigation.", {"rate": "-5%"}),
        "{-nav}{-tab_nef}{platon2}{tab_aca2}D'où la thèse la plus célèbre de la République.",
        ("C", "Tant que les philosophes ne seront pas rois, ou que ceux qu'on appelle aujourd'hui rois et souverains ne seront "
              "pas vraiment et sérieusement philosophes, … il n'est point, ô mon cher Glaucon, de remède aux maux qui désolent "
              "les États, ni même, selon moi, à ceux du genre humain.", "c_roi"),
        "{-platon2}{-c_roi}{obj}Le philosophe-roi gouverne par la connaissance du Bien, non par intérêt. Pour qu'il ne soit pas "
        "corrompu, Platon interdit même aux gardiens la propriété privée. {obj.1}Mais l'objection est redoutable : "
        "qui contrôlera ces savants ? Qui gardera les gardiens, selon la formule du poète latin Juvénal ? "
        "{obj.2}Au vingtième siècle, Karl Popper verra dans la République l'ancêtre des régimes qui prétendent détenir "
        "la vérité, et faire le bonheur des hommes malgré eux.",
        "{-obj}{-tab_aca2}",
    ], vis={
        "platon": dict(type="portrait", annee=-428, img="platon", nom="Platon", dates="v. 428 – 348 av. J.-C.",
                       legende="La République (vers 375 av. J.-C.)", x=110, y=120, w=330, h=420),
        "tab_aca": dict(type="tableau", img="et5-academie", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .5, .45],
                        legende="L'Académie de Platon, mosaïque de Pompéi, Iᵉʳ s. av. J.-C. (Musée archéologique national, Naples)"),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.6, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 · au centre, Platon et Aristote"),
        "cite": dict(type="liste", titre="La cité juste (République, IV)", items=[
            "Ceux qui produisent : paysans, artisans, marchands", "Ceux qui gardent : les guerriers",
            "Ceux qui gouvernent : les philosophes"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_nef": dict(type="tableau", img="et5-nef", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .5, .3],
                        legende="Jérôme Bosch, La Nef des fous, vers 1500 (musée du Louvre)"),
        "nav": dict(type="liste", titre="Le navire (République, VI)", items=[
            "Les matelots se disputent la barre, sans savoir naviguer",
            "Le vrai pilote, qui étudie le ciel et les vents, passe pour un rêveur",
            "Gouverner est un savoir, comme la navigation"], marques=["1", "2", "→"], x=170, y=150, w=940),
        "platon2": dict(type="portrait", annee=-428, img="platon", nom="Platon", dates="v. 428 – 348 av. J.-C.",
                        legende="La République, livre V", x=110, y=120, w=330, h=420),
        "tab_aca2": dict(type="tableau", img="et5-academie", fond=True, sombre=True, de=[1.4, .45, .45], a=[1.1, .5, .5],
                         legende="L'Académie de Platon, mosaïque de Pompéi, Iᵉʳ s. av. J.-C. (Musée archéologique national, Naples)"),
        "c_roi": dict(type="cit", a="Platon", o="La République, V, 473c-d, trad. Victor Cousin", x=640, y=110, w=570),
        "obj": dict(type="liste", titre="Le philosophe-roi… et l'objection", items=[
            "Qui gardera les gardiens ? (Juvénal)", "Popper : l'ancêtre des régimes qui prétendent détenir la vérité"],
                    marques=["?", "!"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ II. Machiavel
    dict(id="machiavel", chap="Le lion et le renard", fond="nuit", humeur="tension",
         notions=["la vérité", "le devoir"],
         retenir="Machiavel : la politique a sa propre logique. Le prince doit être lion et renard, pour conserver l'État. Weber : conviction et responsabilité.",
         beats=[
        "{mac}{tab_flo}Florence, 1513. Niccolò Machiavel a servi pendant quatorze ans la République florentine : diplomate, "
        "il a rencontré rois, papes et chefs de guerre. Puis les Médicis reviennent au pouvoir. Accusé de complot, il est "
        "emprisonné, torturé, puis exilé dans sa petite ferme, près de Florence. On l'a croisé dans l'épisode un, avec le mot stato.",
        "Le soir, raconte-t-il dans une lettre, il quitte ses habits couverts de boue, revêt des habits de cour, et entre "
        "dans son cabinet pour converser avec les Anciens. C'est là qu'il écrit Le Prince.",
        "{-mac}{-tab_flo}{tab_bor}{rea}Ce petit livre fait l'effet d'une bombe. {rea.1}Bien des auteurs, dit-il, ont imaginé "
        "des républiques qui n'ont jamais existé : suivez son regard, vers Platon. {rea.2}Lui veut s'en tenir à la vérité "
        "effective des choses : ce que font les hommes, non ce qu'ils devraient faire.{-rea}",
        ("C", "Celui qui veut en tout et partout se montrer homme de bien ne peut manquer de périr au milieu de tant de méchants.",
         "c_mac1"),
        "{-c_mac1}{bor}Son modèle, c'est César Borgia, fils du pape. Pour pacifier la Romagne, il y envoie un homme dur, "
        "Ramiro d'Orco, qui rétablit l'ordre par la terreur. {bor.1}Puis, quand cette cruauté le rend odieux, Borgia le fait "
        "exposer un matin sur la place de Césène, coupé en morceaux. Le peuple est à la fois satisfait et terrifié.",
        ("La cruauté a servi… puis on a sacrifié le cruel.", {"rate": "-6%"}),
        "{-bor}{-tab_bor}{tab_ren}Car il y a, dit Machiavel, deux manières de combattre.",
        ("C", "On peut combattre de deux manières : ou avec les lois, ou avec la force.", "c_mac2"),
        "{-c_mac2}{rl}La première est propre à l'homme, la seconde aux bêtes. Le prince doit savoir user des deux. "
        "{rl.1}Être lion, pour épouvanter les loups. {rl.2}Être renard, pour connaître les pièges. "
        "Le lion seul tombe dans les filets ; le renard seul ne fait peur à personne.",
        "{-rl}{ctr}Attention au contresens. Machiavel n'a jamais écrit « la fin justifie les moyens ». Il constate que, "
        "chez les princes, on juge au résultat. {ctr.1}Et le résultat qu'il vise n'est pas le plaisir du tyran : "
        "c'est la conservation de l'État, la sécurité de tous. La politique a sa propre logique, qui n'est pas celle "
        "de la morale privée.",
        "{-ctr}{-tab_ren}{weber}{tab_vot}Quatre siècles plus tard, Max Weber reprend le problème, dans la conférence de 1919 "
        "dont parlait l'épisode un. On l'a vu dans la série sur le {#le devoir}devoir : il distingue deux éthiques.",
        "{-weber}{cr}{cr.g}L'éthique de conviction : rester fidèle à ses principes, quoi qu'il arrive. {cr.d}L'éthique de "
        "responsabilité : répondre des conséquences prévisibles de ses actes. L'homme d'État ne peut se passer de la seconde. "
        "Mais sans la première, il n'est plus qu'un technicien du pouvoir.",
        "{-cr}{-tab_vot}",
    ], vis={
        "mac": dict(type="portrait", annee=1469, img="machiavel", nom="Nicolas Machiavel", dates="1469 – 1527",
                    legende="Le Prince (1513, publié en 1532)", x=110, y=120, w=330, h=420),
        "tab_flo": dict(type="tableau", img="et5-florence", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="La place de la Seigneurie à Florence le 23 mai 1498, jour de l'exécution de Savonarole (attribué à Francesco Rosselli)"),
        "tab_bor": dict(type="tableau", img="et5-borgia", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .3],
                        legende="Altobello Melone, Portrait d'un gentilhomme, dit César Borgia, vers 1513 (Accademia Carrara, Bergame)"),
        "rea": dict(type="liste", titre="Le réalisme de Machiavel", items=[
            "Contre les républiques imaginaires (suivez son regard : Platon)",
            "« La vérité effective des choses » : ce que font les hommes"], marques=["✗", "✓"], x=170, y=180, w=940),
        "c_mac1": dict(type="cit", a="Machiavel", o="Le Prince, XV (1513), trad. Périès", x=170, y=190, w=940),
        "bor": dict(type="note", titre="L'exemple de César Borgia (Le Prince, VII)", cles=["terreur", "terrifié"],
                    t="Ramiro d'Orco rétablit l'ordre en Romagne par la terreur…",
                    etape="… puis Borgia le fait exposer, coupé en morceaux : le peuple est satisfait et terrifié.",
                    x=560, y=170, w=650),
        "tab_ren": dict(type="tableau", img="et5-renard", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .55],
                        legende="Pierre Quentin Chedel d'après Jean-Baptiste Oudry, Le Lion malade et le Renard, gravure pour les Fables de La Fontaine, 1755-1759"),
        "c_mac2": dict(type="cit", a="Machiavel", o="Le Prince, XVIII (1513), trad. Périès", x=170, y=200, w=940),
        "rl": dict(type="cols", g="Le lion", gq="la force : épouvanter les loups", d="Le renard", dq="la ruse : connaître les pièges",
                   vs="+", repere="Le Prince, XVIII"),
        "ctr": dict(type="note", titre="Contresens à éviter", cles=["résultat", "conservation"],
                    t="Machiavel n'a jamais écrit « la fin justifie les moyens » : chez les princes, on juge au résultat.",
                    etape="Le but : la conservation de l'État, non le plaisir du tyran.", x=170, y=180, w=940),
        "weber": dict(type="portrait", annee=1864, img="weber", nom="Max Weber", dates="1864 – 1920",
                      legende="Le Métier et la vocation d'homme politique (1919)", x=110, y=120, w=330, h=420),
        "tab_vot": dict(type="tableau", img="et5-vote1919", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Munich, élections de janvier 1919 : des religieuses votent (National Archives, États-Unis, domaine public)"),
        "cr": dict(type="cols", g="Éthique de conviction", gq="fidèle à ses principes, quoi qu'il arrive",
                   d="Éthique de responsabilité", dq="répondre des conséquences prévisibles", vs="+",
                   repere="Weber (1919) · série « Le devoir », épisode 5"),
    }),

    # ------------------------------------------------------------------ III. Hegel
    dict(id="hegel", chap="L'État, raison en acte", fond="aube", humeur="lumiere", notions=["la raison", "la liberté"],
         retenir="Hegel : famille, société civile, État. L'État réconcilie l'intérêt particulier et l'intérêt général : la liberté devenue institution.",
         beats=[
        "{hegel}{tab_heg}Pour aller plus loin, un tout autre regard. Berlin, 1820 : Hegel publie ses Principes de la philosophie "
        "du droit. Ni rêve de philosophe, ni ruse de prince. Pour lui, l'État moderne est ce que l'histoire a produit "
        "de plus rationnel.",
        "{-hegel}{mom}Il distingue trois moments. {mom.1}La famille, unie par l'amour. {mom.2}La société civile, celle de "
        "l'épisode un : le marché, le travail, où chacun poursuit son intérêt, et où naissent la richesse… et la misère. "
        "{mom.3}Et l'État, qui réconcilie l'intérêt particulier et l'intérêt général.",
        "{-mom}{hdef}L'État, écrit-il, est la réalité effective de l'idée éthique. En lui, l'individu ne perd pas sa liberté : "
        "il la trouve accomplie, dans des lois qu'il peut reconnaître comme les siennes. {hdef.1}C'est la {#la raison}raison "
        "devenue institution.",
        "{-hdef}{crit}On a reproché à Hegel d'avoir divinisé l'État, et même l'État prussien de son temps. {crit.1}Marx, "
        "qui l'a lu de près, retournera l'idée : l'État ne réconcilie rien, il masque la lutte des classes. "
        "C'était l'épisode quatre.",
        "{-crit}{-tab_heg}",
    ], vis={
        "hegel": dict(type="portrait", annee=1770, img="hegel", nom="G. W. F. Hegel", dates="1770 – 1831",
                      legende="Principes de la philosophie du droit (1820)", x=110, y=120, w=330, h=420),
        "tab_heg": dict(type="tableau", img="cs4-hegel-cours", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Franz Kugler, Hegel et ses étudiants, lithographie, 1828"),
        "mom": dict(type="liste", titre="Trois moments (Hegel)", items=[
            "La famille : l'unité par l'amour", "La société civile : le marché, les intérêts, la richesse et la misère",
            "L'État : l'intérêt particulier réconcilié avec l'intérêt général"], marques=["1", "2", "3"],
                    x=170, y=150, w=940, plus=True),
        "hdef": dict(type="def", cles=["accomplie", "institution"], terme="L'État selon Hegel", plus=True,
                     t="« La réalité effective de l'idée éthique » : la liberté accomplie dans des lois qu'on reconnaît.",
                     etape="La raison devenue institution.", x=170, y=200, w=940),
        "crit": dict(type="note", titre="L'objection", cles=["divinisé", "masque"],
                     t="Hegel aurait divinisé l'État, et l'État prussien de son temps.",
                     etape="Marx : l'État ne réconcilie rien, il masque la lutte des classes (épisode 4).", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ IV. l'État-providence
    dict(id="providence", chap="L'État-providence", fond="nuit", humeur="calme", notions=["la justice", "le travail"],
         retenir="L'État-providence redistribue : impôt selon les facultés, protection pour tous. Justice distributive. Objection : est-ce juste de prendre aux uns ?",
         beats=[
        "{tab_doc}{q_h}Revenons à aujourd'hui. Tu te casses le bras au sport. Urgences, radio, plâtre, rendez-vous de contrôle. "
        "À la sortie, tu ne paies presque rien. {-q_h}{q_qui}Qui a payé ? Tout le monde : par les cotisations et les impôts.",
        "{-q_qui}{-tab_doc}{tab_rii}{av}Cette idée est récente. {av.1}Au dix-neuvième siècle, la maladie, la vieillesse "
        "ou le chômage pouvaient jeter une famille à la rue. Regarde ces logements de New York, photographiés par Jacob Riis "
        "vers 1890.",
        "{-av}{-tab_rii}{tab_bev}{bev}En 1942, en pleine guerre, l'économiste britannique William Beveridge remet un rapport "
        "qui fera date. Il veut terrasser cinq géants : {bev.1}le besoin, {bev.2}la maladie, {bev.3}l'ignorance, "
        "{bev.4}l'insalubrité, {bev.5}et l'oisiveté forcée, le chômage.",
        "{-bev}{-tab_bev}{tab_raf}En France, la Sécurité sociale naît en 1945. Et la Constitution de 1946 inscrit cette promesse "
        "dans son préambule.",
        ("C", "Elle garantit à tous, notamment à l'enfant, à la mère et aux vieux travailleurs, la protection de la santé, "
              "la sécurité matérielle, le repos et les loisirs.", "c_pre"),
        "{-c_pre}{red}C'est l'État-providence. Il ne se contente plus de protéger les personnes et les biens : il redistribue. "
        "{red.g}D'un côté, l'impôt : la Déclaration de 1789 voulait déjà une contribution répartie entre tous les citoyens, "
        "en raison de leurs facultés. {red.d}De l'autre, les prestations : soins, retraites, allocations, école gratuite.",
        "{-red}{ari}Aristote distinguait déjà deux justices. {ari.g}La justice commutative : dans un échange, chacun reçoit "
        "l'équivalent de ce qu'il donne. {ari.d}La justice distributive : on répartit les biens communs selon ce qui revient "
        "à chacun. L'État-providence, c'est la justice distributive à grande échelle.",
        "{-ari}{obj2}Mais il a ses critiques. {obj2.1}Prendre aux uns le fruit de leur {#le travail}travail pour le donner "
        "aux autres, est-ce juste ? Le philosophe américain Robert Nozick, en 1974, ira jusqu'à comparer l'impôt sur le travail "
        "à du travail forcé. {obj2.2}Et l'assistance ne rend-elle pas dépendant ? Il faut un critère pour trancher.",
        "{-obj2}{-tab_raf}",
    ], vis={
        "tab_doc": dict(type="tableau", img="et5-docteur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .5],
                        legende="Luke Fildes, Le Docteur, 1891 (Tate Britain, Londres)"),
        "q_h": dict(type="question", t="Un bras cassé, l'hôpital… et presque rien à payer."),
        "q_qui": dict(type="question", t="Qui a payé ?"),
        "tab_rii": dict(type="tableau", img="et5-riis", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Jacob Riis, Locataires d'un logement surpeuplé, Bayard Street, New York, vers 1889"),
        "av": dict(type="note", titre="Avant l'État-providence", cles=["à la rue"],
                   t="Maladie, vieillesse, chômage…",
                   etape="… pouvaient jeter une famille à la rue.", x=170, y=200, w=940),
        "tab_bev": dict(type="tableau", img="et5-beveridge", fond=True, sombre=True, de=[1.0, .45, .4], a=[1.2, .45, .35],
                        legende="Sir William Beveridge dans son bureau, Oxford, 1943 (ministère britannique de l'Information, domaine public)"),
        "bev": dict(type="liste", titre="Le rapport Beveridge (1942) : cinq géants", items=[
            "Le besoin", "La maladie", "L'ignorance", "L'insalubrité", "L'oisiveté forcée : le chômage"],
                    marques=["1", "2", "3", "4", "5"], x=560, y=110, w=650),
        "tab_raf": dict(type="tableau", img="et5-raphael", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Raphaël, La Justice, plafond de la Chambre de la Signature, 1508-1511 (Vatican)"),
        "c_pre": dict(type="cit", a="Préambule de la Constitution du 27 octobre 1946", o="alinéa 11 (« Elle » : la Nation)",
                      x=170, y=180, w=940),
        "red": dict(type="cols", g="L'impôt", gq="selon les facultés de chacun (DDHC, art. 13)", d="Les prestations",
                    dq="soins, retraites, allocations, école", vs="→", repere="L'État-providence redistribue"),
        "ari": dict(type="cols", g="Justice commutative", gq="dans l'échange : à chacun l'équivalent", d="Justice distributive",
                    dq="répartir les biens communs selon ce qui revient à chacun", vs="≠", repere="Aristote, Éthique à Nicomaque, V"),
        "obj2": dict(type="liste", titre="Deux objections", items=[
            "Prendre le fruit du travail des uns : Nozick (1974) parle de travail forcé",
            "L'assistance rend-elle dépendant ?"], marques=["?", "?"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ V. Rawls
    dict(id="rawls", chap="Le voile d'ignorance", fond="aube", humeur="lumiere", notions=["la justice", "la liberté", "la raison"],
         retenir="Rawls : choisir les règles derrière un voile d'ignorance. 1. Les mêmes libertés pour tous. 2. Des inégalités seulement si elles profitent aux plus défavorisés.",
         beats=[
        "{tab_jus}{ga}Un jeu, pour commencer. Deux enfants doivent partager un gâteau. Comment rendre le partage juste ? "
        "C'est simple : {ga.1}celui qui coupe choisit en dernier. {ga.2}Ne sachant pas quelle part lui restera, "
        "il coupera des parts égales.",
        "{-ga}{raw}C'est, en miniature, l'idée de John Rawls, philosophe américain, dans sa Théorie de la justice, en 1971. "
        "Pour savoir ce qu'est une société juste, imagine qu'on doive en choisir les règles… derrière un voile d'ignorance.",
        "{raw.1}Tu ne sais pas qui tu seras : riche ou pauvre, homme ou femme, malade ou en bonne santé, doué ou non. "
        "Alors, quelles règles choisirais-tu, si tu pouvais être n'importe qui ?",
        "{-raw}{-tab_jus}{tab_lor5}{pri}Rawls pense que tout être raisonnable choisirait deux principes. {pri.1}Le premier : "
        "pour chacun, les mêmes {#la liberté}libertés fondamentales, les plus étendues possible : penser, s'exprimer, voter. "
        "Elles passent avant tout : on ne les sacrifie pas pour plus de richesse.",
        "{pri.2}Le second : des inégalités sont acceptables, à deux conditions. Que les places soient ouvertes à tous, "
        "avec des chances réellement égales. {pri.3}Et qu'elles profitent aux plus défavorisés. C'est le principe de différence.",
        "{-pri}{med}Un exemple. Un chirurgien gagne plus qu'un caissier. Est-ce injuste ? Pas forcément, répond Rawls, "
        "si cet écart permet des études longues dont les plus pauvres profitent aussi, en étant mieux soignés. "
        "{med.1}Mais une inégalité qui n'enrichit que les plus riches n'a aucune justification.",
        ("La justice d'un État se mesure au sort qu'il fait aux plus faibles.", {"rate": "-5%"}),
        "{-med}{-tab_lor5}",
    ], vis={
        "tab_jus": dict(type="tableau", img="et5-justitia", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.35, .45, .25],
                        legende="Hans Gieng, Justitia, fontaine de la Justice, Berne, 1543 (photo JoachimKohler-HB, CC BY-SA 4.0)"),
        "ga": dict(type="liste", titre="Partager un gâteau", items=[
            "Celui qui coupe choisit en dernier", "Ne sachant pas quelle part il aura, il coupe des parts égales"],
                   marques=["1", "→"], x=170, y=180, w=940),
        "raw": dict(type="def", cles=["voile d'ignorance", "n'importe qui"], terme="Le voile d'ignorance · Rawls (1971)", plus=True,
                    t="Choisir les règles de la société sans savoir quelle place on y occupera.",
                    etape="Riche ou pauvre, malade ou en bonne santé : et si j'étais n'importe qui ?", x=170, y=200, w=940),
        "tab_lor5": dict(type="tableau", img="et4-lorenzetti", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.3, .65, .45],
                         legende="Ambrogio Lorenzetti, Allégorie du bon gouvernement, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "pri": dict(type="liste", titre="Les deux principes de la justice", items=[
            "Les mêmes libertés fondamentales pour tous : elles passent d'abord",
            "Des inégalités, si les places sont ouvertes à tous, à chances égales",
            "… et si elles profitent aux plus défavorisés : le principe de différence"], marques=["1", "2a", "2b"],
                    x=170, y=150, w=940),
        "med": dict(type="note", titre="Le principe de différence, en pratique", cles=["plus pauvres", "aucune justification"],
                    t="Le chirurgien gagne plus : juste, si ses longues études profitent aussi aux plus pauvres.",
                    etape="Une inégalité qui n'enrichit que les riches n'a aucune justification.", x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ath3}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Platon. La cité juste, c'est chacun à sa place ; "
        "les philosophes devraient être rois. Mais qui gardera les gardiens ?",
        "{rec.2}Deux : Machiavel. La politique a sa propre logique : être lion et renard, pour conserver l'État. "
        "Et Weber : tenir ensemble conviction et responsabilité.",
        "{rec.3}Trois : Hegel, l'État comme raison devenue institution. Puis l'État-providence, qui redistribue pour protéger chacun.",
        "{rec.4}Quatre : Rawls. Une société juste est celle qu'on choisirait derrière un voile d'ignorance.",
        "{-rec}{-tab_ath3}{tab_fin}{q_suite}Tu as maintenant tous les outils. Reste à t'en servir, le jour de l'épreuve : "
        "trois sujets, et un texte de Spinoza.",
        "{-q_suite}{fin}",
        ("La prochaine fois : l'État à l'épreuve du bac.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ath3": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.6, .5, .47], a=[1.0, .5, .5],
                         legende="Raphaël, L'École d'Athènes, 1509-1511"),
        "rec": dict(type="carte", centre="L'ÉTAT ET LA JUSTICE", branches=[
            dict(t="Platon", items=["chacun à sa place", "le navire et le pilote", "les philosophes rois"]),
            dict(t="Machiavel", items=["la vérité effective", "le lion et le renard", "Weber : conviction / responsabilité"]),
            dict(t="Hegel, l'État-providence", items=["la raison devenue institution", "redistribuer", "commutative / distributive"]),
            dict(t="Rawls", items=["le voile d'ignorance", "les libertés d'abord", "le principe de différence"])]),
        "tab_fin": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "q_suite": dict(type="question", t="Trois sujets, un texte de Spinoza : prêt ?"),
        "fin": dict(type="titre", sur="À suivre", t="L'État à l'épreuve du bac", sous="Épisode 6 · Trois sujets, un texte de Spinoza"),
    }),
]

QUIZ = [
    dict(q="Pour Platon, qu'est-ce que la justice dans la cité ?",
         r=["L'égalité de tous en tout", "Que chacun fasse ce pour quoi il est fait, à sa place",
            "Le pouvoir du plus fort", "Le vote de la majorité"], ok=1,
         voir="cite", ex="Producteurs, gardiens, gouvernants : la cité juste est une harmonie, comme une âme où la raison commande."),
    dict(q="Que veut montrer Platon avec l'image du navire ?",
         r=["Que les marins sont les meilleurs gouvernants", "Que gouverner est un savoir, comme la navigation",
            "Que le pouvoir doit être tiré au sort", "Qu'il faut fuir la mer"], ok=1,
         voir="nav", ex="Les matelots se disputent la barre sans savoir naviguer ; le vrai pilote passe pour un rêveur (République, VI)."),
    dict(q="Quelle objection classique fait-on au philosophe-roi ?",
         r=["Il est trop pauvre", "Qui gardera les gardiens ?", "Il ne connaît pas la vérité", "Il est élu"], ok=1,
         voir="obj", ex="Un pouvoir qui prétend détenir la vérité échappe à tout contrôle : Popper y voit l'ancêtre des régimes totalitaires."),
    dict(q="Pour Machiavel, le prince doit être…",
         r=["toujours bon, en toute circonstance", "lion et renard : la force et la ruse",
            "un philosophe", "obéissant au pape"], ok=1,
         voir="rl", ex="Le Prince, XVIII : lion pour épouvanter les loups, renard pour connaître les pièges."),
    dict(q="« La fin justifie les moyens » : qu'en dire ?",
         r=["C'est une citation exacte du Prince", "Machiavel ne l'a jamais écrit : il dit que chez les princes on juge au résultat",
            "C'est une phrase de Platon", "C'est la devise de Rawls"], ok=1,
         voir="ctr", ex="Le but visé est la conservation de l'État, non le plaisir du tyran : la politique a sa logique propre."),
    dict(q="Selon Aristote, répartir les biens communs selon ce qui revient à chacun relève de…",
         r=["la justice commutative", "la justice distributive", "la justice divine", "la vengeance"], ok=1,
         voir="ari", ex="La justice commutative règle les échanges ; la distributive, la répartition. L'État-providence l'applique à grande échelle."),
    dict(q="Que demande l'expérience du voile d'ignorance (Rawls) ?",
         r=["Choisir les règles de la société sans savoir quelle place on y aura", "Ignorer les lois",
            "Voter à bulletin secret", "Cacher ses revenus au fisc"], ok=0,
         voir="raw", ex="Comme celui qui coupe le gâteau et choisit en dernier : on choisit des règles équitables."),
    dict(q="Selon le principe de différence, une inégalité est juste si…",
         r=["elle récompense les plus riches", "elle profite aux plus défavorisés",
            "elle est votée par la majorité", "elle est héritée"], ok=1,
         voir="pri", ex="Et à condition que les places soient ouvertes à tous, à chances égales. Les libertés fondamentales passent d'abord."),
]

CREDITS = [
    "Portraits : Platon (Raphaël, L'École d'Athènes, détail) ; Nicolas Machiavel (Santi di Tito) ; Max Weber (photographie) ; "
    "G. W. F. Hegel (Jakob Schlesinger, 1831) : domaine public",
    "Tableaux et gravures : mosaïque de l'Académie de Platon (Pompéi, Naples) ; Raphaël, L'École d'Athènes (1509-1511) et La Justice "
    "(1508-1511) ; Jérôme Bosch, La Nef des fous (vers 1500) ; Exécution de Savonarole sur la place de la Seigneurie (attribué à "
    "Francesco Rosselli) ; Altobello Melone, Portrait d'un gentilhomme, dit César Borgia (vers 1513) ; P. Q. Chedel d'après J.-B. Oudry, "
    "Le Lion malade et le Renard (1755-1759) ; Franz Kugler, Hegel et ses étudiants (1828) ; Luke Fildes, Le Docteur (1891) ; "
    "Ambrogio Lorenzetti, Allégorie du bon gouvernement (1338-1339) : domaine public",
    "Photographies : théâtre grec de Syracuse (Pequod76, domaine public) ; Munich, élections de 1919 (National Archives, domaine public) ; "
    "Jacob Riis, Bayard Street (vers 1889) ; William Beveridge, 1943 (ministère britannique de l'Information, domaine public) ; "
    "Justitia, Berne (JoachimKohler-HB, CC BY-SA 4.0) ; salle d'examen (domaine public)",
    "Citations : Platon, La République, V, trad. Victor Cousin (Wikisource) ; Machiavel, Le Prince, XV et XVIII, trad. J.-V. Périès "
    "(Wikisource) ; Préambule de la Constitution de 1946. Hegel, Weber, Beveridge, Nozick et Rawls : paraphrases.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
