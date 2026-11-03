"""L'État, épisode 4 : « Contre l'État ? »

Même format que les séries « La liberté », « Le devoir », « Le bonheur » et « La conscience » (voir liberte_1.py, devoir_3.py).
Citations : La Boétie, Discours de la servitude volontaire (vers 1548, publié en 1576), orthographe modernisée
(texte vérifié sur Wikisource, édition Bonnefon) ; Marx et Engels, Manifeste du parti communiste, I (1848), trad. courante ;
Proudhon, Idée générale de la Révolution au XIXᵉ siècle, Épilogue (1851), vérifié sur Wikisource ;
Nietzsche, Ainsi parlait Zarathoustra, I, « De la nouvelle idole » (1883), trad. Henri Albert, vérifié sur Wikisource.
Engels (Anti-Dühring, L'Origine de la famille), Bakounine (Étatisme et anarchie) et Clastres (La Société contre l'État,
1974, œuvre protégée) : paraphrasés par le narrateur.
"""

CODE = "etat-4"
NOTION = "L'État"
NUM = 4
TITRE = "Contre l'État ?"
SUIVANT = "Épisode 5 · L'État et la justice"
PRONONCIATION = {"Ceaușescu": "Tchaouchesscou", "Bucarest": "Bucaresste", "Sarlat": "Sarla", "Engels": "Ènguèlss",
                 "Guayaki": "Gouayaki", "Nietzsche": "Nitche", "an-arkhè": "ann-arkè",
                 "Besançon": "Bezanson", "Clastres": "Klastre"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_fou}{q1}Bucarest, le vingt et un décembre 1989. Sur une grande place, cent mille personnes ont été rassemblées "
        "par le régime. Au balcon du Comité central, le dictateur Nicolae Ceaușescu prend la parole. Depuis vingt-quatre ans, "
        "il gouverne la Roumanie d'une main de fer : police secrète, pénuries, culte de sa personne.",
        "{-q1}{-tab_fou}{tab_bal}{r89}{r89.1}Comme d'habitude, la télévision retransmet en direct. Comme d'habitude, "
        "on attend les applaudissements. {r89.2}Mais au fond de la place, quelques sifflets. Puis des cris. "
        "{r89.3}Puis la foule entière qui hue.",
        ("Ceaușescu s'arrête, la main levée. Il ne comprend pas.", {"rate": "-6%"}),
        "{r89.4}La télévision coupe l'image. Le lendemain, il s'enfuit en hélicoptère, depuis le toit du même bâtiment. "
        "Le régime s'effondre.",
        "{-r89}{q2}Il avait l'armée, la police, les prisons. Il ne lui manquait qu'une chose : que les gens continuent d'obéir.",
        "{-q2}{ann}Et si la force de l'État n'était que la nôtre, prêtée ? Aujourd'hui, on donne la parole à ceux qui "
        "se méfient de l'État… ou qui voudraient s'en passer.",
        ("P", 0.3),
        "{-ann}{-tab_bal}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_fou": dict(type="tableau", img="et4-foule", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .55],
                        legende="Bucarest, décembre 1989 (Musée national d'histoire de la Roumanie, collection « Le communisme en Roumanie », attribution)"),
        "q1": dict(type="question", t="Bucarest, 21 décembre 1989. Cent mille personnes sur une place."),
        "tab_bal": dict(type="tableau", img="et4-balcon", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .3],
                        legende="Le balcon du dernier discours de Ceaușescu, envahi par la foule, décembre 1989 (Musée national d'histoire de la Roumanie, attribution)"),
        "r89": dict(type="liste", titre="21 décembre 1989", items=[
            "La télévision retransmet en direct", "Quelques sifflets, puis des cris", "La foule entière hue le dictateur",
            "L'image coupée, la fuite, la chute"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "q2": dict(type="question", t="Que reste-t-il au tyran quand plus personne n'obéit ?"),
        "ann": dict(type="mot", t="Contre l'État ?", g="ceux qui s'en méfient… ou voudraient s'en passer", y=260, taille=96),
        "titre": dict(type="titre", sur="L'État · Épisode 4", t="Contre l'État ?",
                      sous="La Boétie, Marx, les anarchistes, Nietzsche"),
    }),

    # ------------------------------------------------------------------ I. La Boétie
    dict(id="boetie", chap="La servitude volontaire", fond="aube", humeur="mystere", notions=["la liberté", "la nature"],
         retenir="La Boétie : le tyran n'a que la force qu'on lui donne. On sert par coutume, par divertissement, par intérêt.",
         beats=[
        "{boetie}{tab_sar}Ce mystère, un jeune homme l'a formulé quatre siècles plus tôt. {n_boe}Étienne de La Boétie naît en 1530 "
        "à Sarlat, dans le Périgord. Avant ses dix-huit ans, dit Montaigne, il écrit un court texte : le Discours de la "
        "servitude volontaire. Montaigne deviendra son meilleur ami, et dira de leur amitié : parce que c'était lui, "
        "parce que c'était moi.",
        "{-n_boe}{-tab_sar}{tab_man}Sa question tient en une phrase.",
        ("C", "Je ne voudrais sinon entendre comment il se peut faire que tant d'hommes, tant de bourgs, tant de villes, "
              "tant de nations endurent quelquefois un tyran seul…", "c_tyr"),
        "{-boetie}{-c_tyr}{un}Un tyran, remarque La Boétie, n'a que deux yeux, deux mains, un seul corps. Ce n'est pas sa force "
        "qui tient des millions d'hommes. {un.1}Alors, quoi ? Sa réponse fait scandale : ce sont les hommes eux-mêmes qui se donnent. "
        "La servitude n'est pas seulement subie. Elle est {!volontaire}volontaire.",
        "{-un}{-tab_man}{tab_col}D'où un appel d'une simplicité désarmante.",
        ("C", "Soyez résolus de ne servir plus, et vous voilà libres.", "c_res"),
        "{-c_res}{col}Pas besoin de le renverser, précise-t-il. Il suffit de ne plus le soutenir, {col.1}et vous le verrez, "
        "comme un grand colosse à qui l'on a dérobé sa base, de son poids même fondre en bas et se rompre.",
        ("C'est exactement ce qui s'est passé à Bucarest.", {"rate": "-5%"}),
        "{-col}{-tab_col}{tab_pol}{cau}Mais alors, pourquoi obéit-on ? La Boétie donne trois raisons. {cau.1}D'abord, la coutume. "
        "Ceux qui naissent sous le joug ne connaissent rien d'autre : ils prennent pour leur {#la nature}nature ce qui n'est "
        "qu'une habitude. Ils ont oublié leur liberté naturelle.",
        "{cau.2}Ensuite, les divertissements. Les tyrans offraient au peuple des théâtres, des jeux, des gladiateurs : "
        "La Boétie les appelle les appâts de la servitude. {-tab_pol}{tab_ecr}Tu peux te demander quels sont les nôtres.",
        "{-tab_ecr}{tab_bal2}{cau.3}Enfin, et surtout, la chaîne des complices. Autour du tyran, cinq ou six favoris. "
        "Sous eux, six cents qui profitent. Sous ces six cents, six mille, à qui l'on donne des places et des privilèges. "
        "Et ainsi de suite, jusqu'à des millions.",
        "{-cau}{pyr}Le tyran ne tient pas par la force contre tous. Il tient parce qu'il a acheté un peu de chacun.",
        ("Le pouvoir ne se prend pas seulement. Il se donne.", {"rate": "-5%"}),
        "{-pyr}{lec}Retiens la leçon pour ta copie. Même l'État le plus brutal repose sur une forme de consentement, "
        "fait d'habitude, de distraction et d'intérêt. {lec.1}Ce n'est donc pas d'abord une critique de l'État : c'est une "
        "critique de notre obéissance. Et un appel à notre responsabilité.",
        "{-lec}{-tab_bal2}",
    ], vis={
        "n_boe": dict(type="note", titre="Étienne de La Boétie (1530-1563)", cles=["dix-huit", "lui"],
                     t="Avant ses dix-huit ans : le Discours de la servitude volontaire.",
                     etape="Montaigne, son ami : « parce que c'était lui, parce que c'était moi ».", x=640, y=150, w=570),
        "boetie": dict(type="portrait", annee=1530, img="boetie", nom="Étienne de La Boétie", dates="1530 – 1563",
                       legende="Discours de la servitude volontaire (vers 1548)", x=110, y=120, w=330, h=420),
        "tab_sar": dict(type="tableau", img="et4-sarlat", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .25],
                        legende="Maison natale de La Boétie, Sarlat (photo Thesupermat, CC BY-SA 3.0)"),
        "tab_man": dict(type="tableau", img="et4-manuscrit", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .35],
                        legende="« Contre la tirannie et tirans, La Servitude volontaire », copie manuscrite, XVIᵉ s. (Bibliothèques virtuelles humanistes, CC BY-SA 4.0)"),
        "c_tyr": dict(type="cit", a="La Boétie", o="Discours de la servitude volontaire (vers 1548), orthographe modernisée",
                      x=640, y=150, w=570),
        "un": dict(type="def", cles=["volontaire"], terme="La servitude volontaire",
                   t="Un tyran n'a que deux yeux, deux mains, un seul corps : sa force, c'est nous qui la lui donnons.",
                   etape="La servitude n'est pas seulement subie : elle est consentie.", x=170, y=200, w=940),
        "tab_col": dict(type="tableau", img="et4-colosse", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Maarten van Heemskerck et Philip Galle, Le Colosse de Rhodes, gravure, 1572"),
        "c_res": dict(type="cit", a="La Boétie", o="Discours de la servitude volontaire, orthographe modernisée", x=170, y=200, w=940),
        "col": dict(type="note", titre="Le colosse sans base", cles=["soutenir", "colosse"],
                    t="Inutile de renverser le tyran : il suffit de ne plus le soutenir.",
                    etape="Comme un colosse privé de sa base, il s'effondre de son propre poids.", x=170, y=180, w=940),
        "tab_pol": dict(type="tableau", img="et4-pollice", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .55],
                        legende="Jean-Léon Gérôme, Pollice verso, 1872 (Phoenix Art Museum)"),
        "tab_ecr": dict(type="tableau", img="t-ecrans", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .6, .4],
                        legende="Photo Rawpixel, CC BY 2.0"),
        "tab_bal2": dict(type="tableau", img="et4-balcon", fond=True, sombre=True, de=[1.3, .5, .3], a=[1.0, .5, .5],
                         legende="Bucarest, décembre 1989 : le siège du Comité central (Musée national d'histoire de la Roumanie, attribution)"),
        "cau": dict(type="liste", titre="Pourquoi obéit-on ? Trois raisons", items=[
            "La coutume : on prend l'habitude pour la nature", "Les divertissements : « les appâts de la servitude »",
            "La chaîne des complices : 6, puis 600, puis 6 000…"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "pyr": dict(type="mot", t="6 → 600 → 6 000 → …", g="la pyramide des complices : chacun est un peu acheté", y=250, taille=96),
        "lec": dict(type="def", cles=["consentement", "obéissance"], terme="La leçon de La Boétie",
                    t="Même l'État le plus brutal repose sur une forme de consentement.",
                    etape="Une critique de notre obéissance, plus que de l'État : un appel à la responsabilité.",
                    x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. Marx et Engels
    dict(id="marx", chap="L'État d'une classe", fond="nuit", humeur="tension", notions=["le travail", "la justice"],
         retenir="Marx et Engels : l'État n'est pas neutre, c'est l'instrument de la classe dominante. Sans classes, il devrait dépérir.",
         beats=[
        "{marx}{tab_men}Trois siècles plus tard, la critique change de cible. Pour Karl Marx et son ami Friedrich Engels, "
        "le problème n'est pas un tyran. {n_mx}C'est l'État lui-même, même quand il est élu. On a croisé Marx dans la série sur la "
        "liberté, avec les libertés formelles. Allons plus loin.",
        "{-n_mx}{-tab_men}{tab_mfs}{lc}En 1848, ils publient le Manifeste du parti communiste. L'histoire de toute société, disent-ils, "
        "est l'histoire de luttes de classes : maîtres et esclaves, seigneurs et serfs, et aujourd'hui bourgeois et prolétaires. "
        "Et l'État, dans tout cela ?",
        "{-lc}",
        ("C", "Le gouvernement moderne n'est qu'un comité qui gère les affaires communes de la classe bourgeoise tout entière.",
         "c_man"),
        "{-marx}{-c_man}{-tab_mfs}{tab_pyr}{inst}Voilà la thèse. {inst.1}L'État se présente comme neutre, au-dessus des intérêts, "
        "au service de tous. {inst.2}En réalité, c'est un {!instrument}instrument : celui de la classe qui possède les usines, "
        "la terre, le capital. {inst.3}Ses lois protègent d'abord la propriété ; sa police et son armée, l'ordre qui la garantit.",
        "{-inst}{aff}Regarde cette affiche syndicaliste américaine, de 1911. {aff.1}Tout en haut, le sac d'argent : le capital. "
        "{aff.2}Juste en dessous, les rois et les présidents : nous vous gouvernons. {aff.3}Puis le clergé, l'armée, "
        "les bourgeois attablés… {aff.4}et tout en bas, ceux qui portent tout le monde : les travailleurs.",
        "{-aff}{-tab_pyr}{tab_men2}{ex_m}Un exemple du dix-neuvième siècle. L'ouvrier travaille parfois quatorze heures par jour. "
        "S'il se met en grève avec d'autres, la loi le punit : en France, il faut attendre 1864 pour que la grève ne soit plus "
        "un délit. {ex_m.1}Le {#le travail}travail est libre, en droit. Mais celui qui n'a que ses bras doit accepter les "
        "conditions de celui qui possède l'usine.",
        "{-ex_m}{-tab_men2}{engels}{tab_com}Engels ajoute une hypothèse sur l'origine. {n_en}{n_en.1}L'État serait né le jour où la société "
        "s'est divisée en classes, pour empêcher que leur lutte ne la détruise. {n_en.2}Il se pose en arbitre… {n_en.3}mais il reste l'État "
        "de la classe la plus puissante.",
        "{-engels}{-n_en}{dep}D'où une conséquence étonnante. Si l'État n'existe que parce qu'il y a des classes, une société sans classes "
        "n'en aura plus besoin. {dep.1}Après la révolution, une période de transition, la dictature du prolétariat. "
        "Marx croit en voir l'esquisse en 1871, dans la Commune de Paris. {dep.2}Puis l'État doit dépérir. "
        "{dep.3}On ne l'abolira pas, écrit Engels : il s'éteindra de lui-même, et sa machine ira au musée des antiquités, "
        "à côté du rouet et de la hache de bronze.",
        "{-dep}{-tab_com}{tab_pal}{iro}Seulement voilà. Au vingtième siècle, les régimes qui se réclament de Marx bâtissent "
        "les États les plus puissants de l'histoire : parti unique, police politique, économie tout entière planifiée. "
        "Celui de Ceaușescu en faisait partie. {iro.1}Regarde ce palais : pour le construire, il a fait raser un quartier entier "
        "de Bucarest. C'est l'un des plus grands bâtiments administratifs du monde.",
        ("L'État devait s'éteindre. Il est devenu énorme.", {"rate": "-6%"}),
        "{-iro}{-tab_pal}{q_pq}Pourquoi ? Un anarchiste l'avait prédit, dès 1873.",
        "{-q_pq}",
    ], vis={
        "n_mx": dict(type="note", titre="Marx et Engels", cles=["l'État lui-même", "élu"],
                    t="Le problème n'est pas un tyran : c'est l'État lui-même, même quand il est élu.", x=640, y=150, w=570),
        "lc": dict(type="note", titre="Manifeste du parti communiste (1848)", cles=["luttes de classes"],
                  t="L'histoire de toute société est l'histoire de luttes de classes.",
                  etape="Maîtres et esclaves, seigneurs et serfs, bourgeois et prolétaires.", x=640, y=150, w=570),
        "marx": dict(type="portrait", annee=1818, img="marx", nom="Karl Marx", dates="1818 – 1883",
                     legende="Manifeste du parti communiste (1848, avec Engels)", x=110, y=120, w=330, h=420),
        "tab_men": dict(type="tableau", img="et4-menzel", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .5],
                        legende="Adolph Menzel, Le Laminoir, 1872-1875 (Alte Nationalgalerie, Berlin)"),
        "tab_mfs": dict(type="tableau", img="et4-manifeste", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .35],
                        legende="Manifest der Kommunistischen Partei, première édition, Londres, février 1848"),
        "c_man": dict(type="cit", a="Marx et Engels", o="Manifeste du parti communiste, I (1848), trad. courante",
                      x=640, y=170, w=570),
        "tab_pyr": dict(type="tableau", img="et4-pyramide", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.35, .5, .3],
                        legende="Pyramid of Capitalist System, affiche des Industrial Workers of the World, 1911 (domaine public)"),
        "inst": dict(type="liste", titre="L'État selon Marx", items=[
            "Il se dit neutre, au service de tous", "En réalité : l'instrument de la classe dominante",
            "Ses lois protègent la propriété ; sa force, l'ordre établi"], marques=["1", "2", "3"], cles=["instrument"],
                     x=170, y=150, w=940),
        "aff": dict(type="liste", titre="L'affiche de 1911, de haut en bas", items=[
            "Le capital", "« Nous vous gouvernons » : rois et présidents", "« Nous vous trompons », « nous vous tirons dessus »…",
            "Tout en bas : « nous travaillons pour tous »"], marques=["1", "2", "3", "4"], x=560, y=150, w=650),
        "tab_men2": dict(type="tableau", img="et4-menzel", fond=True, sombre=True, de=[1.3, .3, .5], a=[1.1, .45, .5],
                         legende="Adolph Menzel, Le Laminoir, 1872-1875 (Alte Nationalgalerie, Berlin)"),
        "ex_m": dict(type="def", cles=["en droit"], terme="Libre en droit, pas en fait",
                     t="L'ouvrier est libre de signer son contrat… mais il n'a que ses bras pour vivre.",
                     etape="Repère · en droit / en fait : les libertés formelles (série « La liberté », épisode 1).",
                     x=170, y=200, w=940),
        "n_en": dict(type="liste", titre="L'origine de l'État (Engels)", items=[
            "Né quand la société se divise en classes",
            "Il se pose en arbitre…",
            "… mais reste l'État de la classe la plus puissante"], marques=["1", "2", "3"], x=640, y=150, w=570),
        "engels": dict(type="portrait", annee=1820, img="engels", nom="Friedrich Engels", dates="1820 – 1895",
                       legende="L'Origine de la famille, de la propriété privée et de l'État (1884)", x=110, y=120, w=330, h=420),
        "tab_com": dict(type="tableau", img="et4-commune", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Barricade de la Commune, rue de Castiglione, Paris, 1871 (attribuée à Bruno Braquehais, Paris Musées, CC0)"),
        "dep": dict(type="liste", titre="Le dépérissement de l'État", items=[
            "La révolution, puis la dictature du prolétariat", "Une société sans classes : l'État devient inutile",
            "Il « s'éteint » : au musée, à côté du rouet (Engels)"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_pal": dict(type="tableau", img="et4-palais", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .35],
                        legende="Le palais du Parlement (ancienne « Maison du peuple » de Ceaușescu), Bucarest, 1996 (photo Sludge G, CC BY-SA 2.0)"),
        "iro": dict(type="note", titre="L'ironie de l'histoire", cles=["énorme"],
                    t="Les régimes qui se réclament de Marx bâtissent les États les plus puissants : parti unique, police politique.",
                    etape="Bucarest : un quartier entier rasé pour un palais du pouvoir.", x=170, y=170, w=940),
        "q_pq": dict(type="question", t="Pourquoi l'État ne s'est-il pas éteint ?"),
    }),

    # ------------------------------------------------------------------ III. l'anarchisme
    dict(id="anarchie", chap="L'ordre sans maître", fond="aube", humeur="lumiere", notions=["la liberté", "la justice"],
         retenir="Anarchie : non le désordre, mais l'absence de commandement. Proudhon : contrats libres, mutuellisme, fédéralisme. Bakounine : tout État crée une minorité qui gouverne.",
         beats=[
        "{tab_cou}{an}D'abord, un mot à laver de son sens courant : anarchie. En grec, an-arkhè, c'est l'absence de commandement, "
        "de chef. {an.1}Pas le désordre.",
        "{-an}{proudhon}Le premier à s'en réclamer fièrement est un Français, fils d'un tonnelier de Besançon : "
        "Pierre-Joseph Proudhon. {n_pr}En 1840, il lance une formule qui fait scandale, la propriété, c'est le vol, "
        "et déclare, dans le même livre : je suis anarchiste. Onze ans plus tard, il écrit une page restée célèbre.",
        "{-n_pr}",
        ("C", "Être gouverné, c'est être gardé à vue, inspecté, espionné, dirigé, légiféré, réglementé, parqué, endoctriné, "
              "prêché, contrôlé, estimé, apprécié, censuré, commandé, par des êtres qui n'ont ni le titre, ni la science, "
              "ni la vertu…", "c_pro"),
        "{-proudhon}{-c_pro}{ana}Que propose-t-il à la place ? {ana.1}Pas le chaos : des contrats libres, passés entre égaux. "
        "{ana.2}Des associations de travailleurs, des banques d'entraide, qui prêtent sans intérêt : c'est le mutuellisme. "
        "{ana.3}Et le fédéralisme : des communes qui s'unissent de bas en haut, au lieu d'un pouvoir qui descend d'en haut.",
        ("L'ordre ne viendrait plus du commandement. Il viendrait de l'accord.", {"rate": "-5%"}),
        "{-ana}{-tab_cou}{bak}{tab_bale}Pour aller plus loin : Michel Bakounine. {n_bk}Un aristocrate russe devenu révolutionnaire, "
        "de toutes les barricades d'Europe, emprisonné, déporté en Sibérie, évadé. Pour lui, la {#la liberté}liberté des autres, "
        "loin de limiter la mienne, l'agrandit : on n'est libre qu'entre égaux.",
        "{-bak}{-n_bk}{mb}Dans l'Association internationale des travailleurs, il affronte Marx. {mb.g}Marx veut conquérir l'État, "
        "pour qu'il dépérisse ensuite. {mb.d}Bakounine répond : jamais. Un État gouverné au nom des ouvriers sera gouverné "
        "par une minorité, d'anciens ouvriers devenus chefs, qui ne représenteront bientôt plus qu'eux-mêmes.",
        "{-mb}{pred}Dans Étatisme et anarchie, en 1873, il annonce une nouvelle classe dirigeante, de savants et de bureaucrates, "
        "qui opprimera au nom du peuple. {pred.1}Le vingtième siècle lui a largement donné raison.",
        "{-pred}{-tab_bale}{tab_lev0}{obj}Reste une objection sérieuse. {obj.1}Sans aucun État, qui protège le faible contre le fort ? "
        "C'est l'objection de Hobbes, qu'on a vue dans la série sur la liberté : sans pouvoir commun, la guerre de chacun "
        "contre chacun. {obj.2}Les anarchistes répondent que l'homme n'est pas un loup : l'entraide est aussi naturelle "
        "que la lutte. Le débat reste ouvert.",
        "{-obj}{-tab_lev0}",
    ], vis={
        "tab_cou": dict(type="tableau", img="et4-courbet", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .35],
                        legende="Gustave Courbet, Pierre-Joseph Proudhon et ses enfants en 1853, 1865 (Petit Palais, Paris)"),
        "an": dict(type="mot", t="an-arkhè", g="grec : l'absence de commandement, de chef · pas le désordre", y=250, taille=104),
        "n_pr": dict(type="note", titre="Pierre-Joseph Proudhon (1809-1865)", cles=["vol", "anarchiste"],
                    t="1840 : « la propriété, c'est le vol ».",
                    etape="Et dans le même livre : « je suis anarchiste ».", x=640, y=150, w=570),
        "proudhon": dict(type="portrait", annee=1809, img="proudhon", nom="Pierre-Joseph Proudhon", dates="1809 – 1865",
                         legende="Idée générale de la Révolution au XIXᵉ siècle (1851)", x=110, y=120, w=330, h=420),
        "c_pro": dict(type="cit", a="Proudhon", o="Idée générale de la Révolution au XIXᵉ siècle, Épilogue (1851)",
                      x=640, y=110, w=570),
        "ana": dict(type="liste", titre="L'anarchie selon Proudhon", items=[
            "Des contrats libres, entre égaux", "Le mutuellisme : associations et banques d'entraide",
            "Le fédéralisme : des communes unies de bas en haut"], marques=["1", "2", "3"], x=170, y=160, w=940),
        "n_bk": dict(type="note", titre="Michel Bakounine (1814-1876)", cles=["Sibérie", "égaux"],
                    t="Aristocrate russe, révolutionnaire, déporté en Sibérie, évadé.",
                    etape="On n'est libre qu'entre égaux.", x=640, y=150, w=570),
        "bak": dict(type="portrait", annee=1814, img="bakounine", nom="Michel Bakounine", dates="1814 – 1876",
                    legende="Étatisme et anarchie (1873)", x=110, y=120, w=330, h=420),
        "tab_bale": dict(type="tableau", img="et4-bale", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .55],
                         legende="Le congrès de l'Association internationale des travailleurs à Bâle, 1869 (gravure, domaine public)"),
        "mb": dict(type="cols", g="Marx", gq="conquérir l'État, pour qu'il dépérisse ensuite", d="Bakounine",
                   dq="tout État crée une minorité qui gouverne : l'abolir", vs="≠", plus=True),
        "pred": dict(type="note", titre="Pour aller plus loin · une prédiction (1873)", cles=["nouvelle classe"],
                     t="Un État « ouvrier » produira une nouvelle classe dirigeante, de savants et de bureaucrates.",
                     etape="Le XXᵉ siècle lui a largement donné raison.", x=170, y=180, w=940),
        "tab_lev0": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .3],
                         legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651"),
        "obj": dict(type="liste", titre="L'objection et la réponse", items=[
            "Sans État, qui protège le faible ? La guerre de chacun contre chacun (Hobbes)",
            "L'homme n'est pas un loup : l'entraide est aussi naturelle que la lutte"], marques=["?", "→"],
                    x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ IV. Nietzsche, Clastres
    dict(id="nietzsche", chap="Le plus froid des monstres froids", fond="nuit", humeur="mystere",
         notions=["la religion", "le langage"],
         retenir="Nietzsche : l'État, « le plus froid des monstres froids », ment en se disant le peuple. Clastres : des sociétés contre l'État.",
         beats=[
        "{nietz}{tab_zar}Dernière attaque, d'un tout autre ordre. {n_nz}Nietzsche, qu'on a vu dans la série sur le devoir dénoncer "
        "la morale du troupeau, s'en prend aussi à l'État. Dans Ainsi parlait Zarathoustra, en 1883, un chapitre s'intitule : "
        "de la nouvelle idole.",
        "{-n_nz}",
        ("C", "L'État, c'est le plus froid de tous les monstres froids : il ment froidement et voici le mensonge qui rampe "
              "de sa bouche : « Moi, l'État, je suis le Peuple. »", "c_nie"),
        "{-nietz}{-c_nie}{-tab_zar}{tab_dor}{men}Quel est ce mensonge ? {men.1}Les peuples, dit Nietzsche, sont nés d'une foi, "
        "d'une manière de vivre, de valeurs inventées par des créateurs. {men.2}L'État, lui, est une machine froide : "
        "il dit « peuple » pour se faire aimer, mais il ne connaît que des administrés, des contribuables, des numéros.",
        "{men.3}Et il se fait adorer. Là où l'on servait les dieux, on sert désormais l'État : on lui sacrifie sa vie, "
        "on meurt pour lui. La {#la religion}religion a changé d'autel : c'est la nouvelle idole.",
        "{-men}{-tab_dor}{tab_voy}Pire : l'État fabrique des hommes moyens, interchangeables. Il y a beaucoup trop d'hommes, "
        "dit Zarathoustra, et l'État a été inventé pour les {!superflus}superflus. L'homme créateur commence ailleurs.",
        ("C", "Là où finit l'État, là seulement commence l'homme qui n'est pas superflu…", "c_fin"),
        "{-c_fin}{nn}Attention au contresens : Nietzsche n'est pas anarchiste. Il ne rêve ni de contrats libres, ni d'égalité. "
        "Ce qu'il reproche à l'État, c'est d'étouffer les individus d'exception sous le troupeau.",
        "{-nn}{-tab_voy}{tab_tup}{clas}Pour aller plus loin, un détour par l'Amérique du Sud. Dans les années 1960, "
        "l'ethnologue Pierre Clastres vit parmi des Indiens du Paraguay, les Guayaki. En 1974, dans La Société contre l'État, "
        "il défend une thèse renversante. {clas.1}On disait de ces sociétés qu'elles étaient sans État, comme s'il leur manquait "
        "quelque chose, comme si elles étaient en retard. {clas.2}Clastres répond : elles sont contre l'État. "
        "Elles empêchent qu'un pouvoir séparé n'apparaisse.",
        "{-clas}{chef}Le chef en est la preuve. {chef.1}Il doit faire la paix entre les familles. {chef.2}Il doit être généreux, "
        "et donner ce qu'il a. {chef.3}Il doit être bon orateur. Mais sa parole ne commande pas : personne n'est obligé de l'écouter. "
        "Le {#le langage}langage du chef est un honneur, pas un pouvoir. S'il voulait donner des ordres, on l'abandonnerait.",
        ("L'État n'est donc pas une fatalité. C'est une invention… et des sociétés l'ont refusée.", {"rate": "-5%"}),
        "{-chef}{-tab_tup}",
    ], vis={
        "n_nz": dict(type="note", titre="Ainsi parlait Zarathoustra (1883)", cles=["idole"],
                    t="Un chapitre : « De la nouvelle idole ».", x=640, y=150, w=570),
        "nietz": dict(type="portrait", annee=1844, img="nietzsche", nom="Friedrich Nietzsche", dates="1844 – 1900",
                      legende="Ainsi parlait Zarathoustra (1883-1885)", x=110, y=120, w=330, h=420),
        "tab_zar": dict(type="tableau", img="et4-zarathoustra", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .3],
                        legende="Also sprach Zarathustra, édition en trois parties, Leipzig, 1887"),
        "c_nie": dict(type="cit", a="Nietzsche", o="Ainsi parlait Zarathoustra, I, « De la nouvelle idole » (1883), trad. Henri Albert",
                      x=640, y=150, w=570),
        "tab_dor": dict(type="tableau", img="et4-leviathan", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .65],
                        legende="Gustave Doré, La Destruction de Léviathan, 1865 (gravure pour la Bible)"),
        "men": dict(type="liste", titre="Le mensonge de l'État", items=[
            "Les peuples naissent d'une foi, de valeurs créées", "L'État : une machine froide, qui ne voit que des numéros",
            "Il se fait adorer : la nouvelle idole"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_voy": dict(type="tableau", img="et4-voyageur", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, vers 1818 (Kunsthalle, Hambourg)"),
        "c_fin": dict(type="cit", a="Nietzsche", o="Ainsi parlait Zarathoustra, I, « De la nouvelle idole », trad. Henri Albert",
                      x=170, y=200, w=940),
        "nn": dict(type="note", titre="Contresens à éviter", cles=["anarchiste", "exception"],
                   t="Nietzsche n'est pas anarchiste : il ne rêve ni de contrats libres, ni d'égalité.",
                   etape="Il reproche à l'État d'étouffer les individus d'exception sous le troupeau.", x=170, y=190, w=940),
        "tab_tup": dict(type="tableau", img="et4-tupi", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .35],
                        legende="Albert Eckhout, Homme tupi, 1643 (Musée national du Danemark)"),
        "clas": dict(type="cols", g="Sans État ?", gq="comme s'il leur manquait quelque chose", d="Contre l'État",
                     dq="elles empêchent qu'un pouvoir séparé apparaisse", vs="→", plus=True,
                     repere="Pierre Clastres · La Société contre l'État (1974)"),
        "chef": dict(type="liste", titre="Le chef sans pouvoir (Clastres)", items=[
            "Faire la paix entre les familles", "Être généreux : donner ce qu'il a",
            "Bien parler… sans jamais commander"], marques=["1", "2", "3"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ V. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_col2}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : La Boétie. Le tyran n'a que la force qu'on lui donne. "
        "Soyez résolus de ne servir plus, et vous voilà libres.",
        "{rec.2}Deux : Marx et Engels. L'État n'est pas neutre : c'est l'instrument d'une classe. Dans une société sans classes, "
        "il devrait dépérir.",
        "{rec.3}Trois : les anarchistes. Proudhon veut l'ordre sans le commandement ; Bakounine prédit qu'un État ouvrier "
        "fabriquera de nouveaux maîtres.",
        "{rec.4}Quatre : Nietzsche, et le plus froid des monstres froids. Et, avec Clastres, des sociétés qui ont refusé l'État.",
        "{-rec}{-tab_col2}{tab_fin}{q_suite}Toutes ces critiques posent, au fond, la même question : à qui sert l'État ? "
        "Mais alors, un État juste est-il possible ? Et qui devrait gouverner ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : l'État et la justice. Platon, Machiavel, Hegel et Rawls.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_col2": dict(type="tableau", img="et4-colosse", fond=True, sombre=True, de=[1.3, .5, .25], a=[1.0, .5, .4],
                         legende="Maarten van Heemskerck et Philip Galle, Le Colosse de Rhodes, gravure, 1572"),
        "rec": dict(type="carte", centre="CONTRE L'ÉTAT ?", branches=[
            dict(t="La Boétie", items=["la servitude volontaire", "coutume, jeux, complices", "« ne servir plus »"]),
            dict(t="Marx et Engels", items=["l'instrument d'une classe", "libre en droit, pas en fait", "le dépérissement"]),
            dict(t="Les anarchistes", items=["an-arkhè : sans chef", "Proudhon : contrats, fédéralisme", "Bakounine : de nouveaux maîtres"]),
            dict(t="Nietzsche, Clastres", items=["le plus froid des monstres froids", "la nouvelle idole", "des sociétés contre l'État"])]),
        "tab_fin": dict(type="tableau", img="et4-lorenzetti", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Ambrogio Lorenzetti, Allégorie du bon gouvernement, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "q_suite": dict(type="question", t="Un État juste est-il possible ? Et qui devrait gouverner ?"),
        "fin": dict(type="titre", sur="À suivre", t="L'État et la justice", sous="Épisode 5 · Platon, Machiavel, Hegel, Rawls"),
    }),
]

QUIZ = [
    dict(q="Selon La Boétie, d'où le tyran tire-t-il sa force ?",
         r=["De son armée seule", "De ceux qui le servent : la servitude est volontaire", "De Dieu", "De la loi"], ok=1,
         voir="un", ex="Le tyran n'a que deux yeux et deux mains : ce sont les hommes qui se donnent. « Soyez résolus de ne servir plus, et vous voilà libres. »"),
    dict(q="Laquelle n'est PAS une des trois raisons de la servitude selon La Boétie ?",
         r=["La coutume", "Les divertissements", "La chaîne des complices", "La peur de l'enfer"], ok=3,
         voir="cau", ex="On obéit par habitude, parce qu'on est distrait (« les appâts de la servitude ») et parce que chacun est un peu acheté."),
    dict(q="Pour Marx et Engels, l'État moderne est…",
         r=["un arbitre neutre au service de tous", "l'instrument de la classe dominante",
            "l'expression de la volonté générale", "une invention des anarchistes"], ok=1,
         voir="c_man", ex="« Un comité qui gère les affaires communes de la classe bourgeoise » (Manifeste, 1848)."),
    dict(q="Que doit devenir l'État dans une société sans classes, selon Engels ?",
         r=["Il doit être renforcé", "Il doit dépérir, s'éteindre de lui-même", "Il doit devenir une monarchie", "Rien ne change"], ok=1,
         voir="dep", ex="On ne l'abolit pas : il s'éteint, et sa machine va « au musée des antiquités ». L'histoire du XXᵉ siècle a montré l'inverse."),
    dict(q="Que signifie « anarchie » au sens de Proudhon ?",
         r=["Le désordre et la violence", "L'absence de commandement : l'ordre par l'accord", "Le pouvoir du peuple en armes",
            "La dictature du prolétariat"], ok=1,
         voir="an", ex="An-arkhè : sans chef. Proudhon propose des contrats libres, le mutuellisme et le fédéralisme."),
    dict(q="Que reproche Bakounine au projet de Marx ?",
         r=["De vouloir abolir l'État trop vite", "Qu'un État gouverné au nom des ouvriers créera une nouvelle minorité dirigeante",
            "De défendre la propriété", "De refuser la révolution"], ok=1,
         voir="mb", ex="Étatisme et anarchie (1873) : savants et bureaucrates opprimeront au nom du peuple."),
    dict(q="« L'État, c'est le plus froid de tous les monstres froids. » Quel est, selon Nietzsche, son mensonge ?",
         r=["« Moi, l'État, je suis le Peuple »", "« Je protège la propriété »", "« Je suis Dieu »", "« Je suis provisoire »"], ok=0,
         voir="c_nie", ex="Ainsi parlait Zarathoustra, I, « De la nouvelle idole » : l'État se fait passer pour le peuple, et se fait adorer."),
    dict(q="Pourquoi Clastres parle-t-il de sociétés « contre » l'État, et non « sans » État ?",
         r=["Parce qu'elles sont en guerre contre leurs voisins", "Parce qu'elles empêchent activement l'apparition d'un pouvoir séparé",
            "Parce qu'elles n'ont pas encore inventé l'État", "Parce qu'elles obéissent à un roi"], ok=1,
         voir="clas", ex="Le chef y fait la paix, donne et parle, mais ne commande pas : l'État n'est pas une fatalité."),
]

CREDITS = [
    "Portraits : Étienne de La Boétie (statue de Sarlat, photo Tommy-Boy, CC BY-SA 4.0) ; Karl Marx (photographie de John Mayall) ; "
    "Friedrich Engels (photographie, 1891, domaine public) ; Pierre-Joseph Proudhon (Gustave Courbet, 1865, détail) ; "
    "Michel Bakounine (photographie de Nadar, 1862) ; Friedrich Nietzsche (photographie, domaine public)",
    "Tableaux et gravures : Maarten van Heemskerck et Philip Galle, Le Colosse de Rhodes (1572) ; Jean-Léon Gérôme, Pollice verso (1872) ; "
    "Adolph Menzel, Le Laminoir (1872-1875) ; Gustave Courbet, Pierre-Joseph Proudhon et ses enfants (1865) ; "
    "Abraham Bosse, frontispice du Léviathan (1651) ; Gustave Doré, La Destruction de Léviathan (1865) ; "
    "Caspar David Friedrich, Le Voyageur contemplant une mer de nuages (vers 1818) ; Albert Eckhout, Homme tupi (1643) ; "
    "Ambrogio Lorenzetti, Allégorie du bon gouvernement (1338-1339) ; congrès de l'AIT à Bâle (1869) : domaine public",
    "Documents et photographies : Bucarest, décembre 1989 (Musée national d'histoire de la Roumanie, collection « Le communisme en Roumanie », "
    "utilisation libre avec attribution) ; maison de La Boétie à Sarlat (Thesupermat, CC BY-SA 3.0) ; copie manuscrite du Discours "
    "(Bibliothèques virtuelles humanistes, CC BY-SA 4.0) ; Manifeste du parti communiste, édition de 1848 ; Pyramid of Capitalist System (1911) ; "
    "barricade de la Commune, 1871 (Bruno Braquehais, Paris Musées, CC0) ; palais du Parlement, Bucarest (Sludge G, CC BY-SA 2.0) ; "
    "Also sprach Zarathustra (1887) ; foule et téléphones (Rawpixel, CC BY 2.0)",
    "Citations : La Boétie, Discours de la servitude volontaire, orthographe modernisée (Wikisource) ; Marx et Engels, Manifeste du parti "
    "communiste (1848), trad. courante ; Proudhon, Idée générale de la Révolution au XIXᵉ siècle (1851, Wikisource) ; Nietzsche, "
    "Ainsi parlait Zarathoustra, trad. Henri Albert (Wikisource). Engels, Bakounine et Clastres : paraphrases.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
