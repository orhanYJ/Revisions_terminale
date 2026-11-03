"""L'État, épisode 2 : « Pourquoi l'État ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la nature} dans le texte lu. Prolonge la série « La liberté », épisode 5 (Hobbes, Locke, Rousseau) sans la refaire.
Citations : Aristote, La Politique, I, 1, § 9, 10 et 12 (trad. J. Barthélemy-Saint-Hilaire, 1874, Wikisource) ;
Locke, Traité du gouvernement civil, § 27, 93, 124 (trad. D. Mazel, 1795) ; Rousseau, Discours sur l'origine de
l'inégalité, seconde partie (1755), et Du contrat social, I, 6 et III, 15 (1762), Wikisource.
Hobbes, Léviathan, XIII (1651) : traduit de l'anglais pour la série, marqué « citation approchée ».
Résumés par le narrateur : Hobbes (XIII et XVII, le dieu mortel, les conventions sans le glaive), Hume (Du contrat
primitif, 1748), Kant (le contrat comme idée de la raison), la grève de la police de Montréal (7 octobre 1969).
"""

CODE = "etat-2"
NOTION = "L'État"
NUM = 2
TITRE = "Pourquoi l'État ?"
SUIVANT = "Épisode 3 · L'État et la liberté : Montesquieu, Spinoza, Arendt, Orwell"
PRONONCIATION = {"Hobbes": "Obbse", "Locke": "Lok", "Hume": "Hioume", "Malmesbury": "Malmzbeuri",
                 "Barthélemy-Saint-Hilaire": "Barthélemy-Saint-Hilaire", "Brixham": "Brixame"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_gor}{an}Montréal, le 7 octobre 1969. Ce matin-là, les policiers de la ville se mettent en grève. "
        "Les pompiers les suivent. D'un coup, une grande ville moderne n'a plus personne pour faire respecter la loi.",
        ("Combien de temps faut-il pour que tout bascule ?", {"rate": "-6%"}),
        "{-an}{mtl}{mtl.1}Quelques heures. Dans la journée, des bandes masquées braquent des banques. "
        "{mtl.2}Le soir, des vitrines volent en éclats ; on pille les magasins du centre-ville. "
        "{mtl.3}Un policier de la police provinciale est tué par balle.",
        "{mtl.4}Le soir même, l'Assemblée du Québec vote une loi d'urgence qui force les policiers à reprendre le travail, "
        "et l'armée entre dans la ville peu après minuit. Seize heures, pas davantage.",
        "{-mtl}{-tab_gor}{tab_dess}{q_sans}Alors, une question. Que serions-nous sans l'État ? "
        "Des loups les uns pour les autres ? Ou bien l'État est-il simplement naturel, comme la famille ?",
        "{-q_sans}{deux}Deux grandes réponses s'affrontent. {deux.g}Pour les uns, l'homme est fait pour vivre dans une cité. "
        "{deux.d}Pour les autres, l'État est une invention : un contrat, passé pour sortir d'un monde sans loi.",
        ("P", 0.3),
        "{-deux}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_gor": dict(type="tableau", img="et2-gordon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .55],
                        legende="John Seymour Lucas, Les Émeutes de Gordon (Londres, 1780), 1879"),
        "an": dict(type="mot", t="7 octobre 1969", g="Montréal : la police se met en grève", y=270, taille=96),
        "mtl": dict(type="liste", titre="Seize heures sans police", items=[
            "Dans la journée : des banques braquées", "Le soir : vitrines brisées, magasins pillés",
            "Un policier tué", "Le soir : une loi d'urgence ; après minuit, l'armée"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "tab_dess": dict(type="tableau", img="et2-leviathan-dessin", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .3],
                         legende="Frontispice du Léviathan, dessin à l'encre sur vélin offert à Charles II, 1651 (British Library)"),
        "q_sans": dict(type="question", t="Que serions-nous sans l'État ?"),
        "deux": dict(type="cols", g="Une cité naturelle", gq="l'homme est fait pour vivre dans la cité", d="Un contrat",
                     dq="une invention, pour sortir d'un monde sans loi", vs="ou"),
        "titre": dict(type="titre", sur="L'État · Épisode 2", t="Pourquoi l'État ?",
                      sous="Aristote, Hobbes, Locke, Rousseau"),
    }),

    # ------------------------------------------------------------------ I. Aristote
    dict(id="aristote", chap="Un animal politique", fond="aube", humeur="lumiere", notions=["la nature", "le langage", "la justice"],
         retenir="Aristote : la cité est naturelle, l'homme est un animal politique. La parole sert à dire le juste et l'injuste. Hors de la cité : une brute ou un dieu.",
         beats=[
        "{tab_ari}{arist}Première réponse, la plus ancienne. Au quatrième siècle avant notre ère, Aristote observe les cités grecques "
        "et se demande d'où elles viennent. Sa réponse tient en une généalogie.",
        "{-arist}{gen}{gen.1}D'abord, la famille : l'homme et la femme, les parents et les enfants, pour vivre au jour le jour. "
        "{gen.2}Puis le village, qui réunit plusieurs familles. {gen.3}Enfin, la cité, qui réunit les villages et se suffit à elle-même. "
        "Née pour assurer la vie, elle existe pour permettre de bien vivre.",
        "{-gen}{-tab_ari}{tab_acr}Pour Aristote, la cité n'est donc pas une invention. Elle est l'achèvement d'un mouvement "
        "qui commence avec la famille. Elle est dans la {#la nature}nature de l'homme.",
        ("C", "De là cette conclusion évidente, que l'État est un fait de nature, que naturellement l'homme est un être sociable…", "c_nat"),
        "{-c_nat}{zoon}{zoon.1}En grec : zôon politikon. L'homme est un animal politique, c'est-à-dire fait pour vivre dans une polis, "
        "une cité. {-tab_acr}{tab_abe}{zoon.2}Plus encore que les abeilles, qui vivent pourtant en essaim. Pourquoi ? Parce que la nature, "
        "dit Aristote, ne fait rien en vain. Et elle n'a donné qu'à l'homme la parole.",
        "{-zoon}La voix des animaux exprime le plaisir et la douleur. La parole, elle, fait autre chose.",
        ("C", "Mais la parole est faite pour exprimer le bien et le mal, et, par suite aussi, le juste et l'injuste…", "c_par"),
        "{-c_par}{-tab_abe}{tab_rem}{tout}Parler, c'est discuter de ce qui est juste : c'est déjà faire de la politique. "
        "{tout.1}D'où une idée choquante pour nous, modernes : la cité passe avant l'individu, comme le tout avant la partie. "
        "{tout.2}Une main séparée du corps n'est plus une main, sauf par le nom, comme une main de pierre.",
        "{-tout}Et celui qui prétendrait vivre seul, sans cité, sans lois ?",
        ("C", "… celui qui ne peut vivre en société, et dont l'indépendance n'a pas de besoins, celui-là ne saurait "
              "jamais être membre de l'État. C'est une brute ou un dieu.", "c_brute"),
        "{-c_brute}{-tab_rem}",
    ], vis={
        "tab_ari": dict(type="tableau", img="et2-aristote-rembrandt", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .45, .35],
                        legende="Rembrandt, Aristote contemplant le buste d'Homère, 1653 (Metropolitan Museum of Art, New York)"),
        "arist": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      legende="La Politique", x=110, y=120, w=330, h=420),
        "gen": dict(type="liste", titre="D'où vient la cité ?", items=[
            "La famille : vivre au jour le jour", "Le village : plusieurs familles",
            "La cité : elle se suffit à elle-même, pour bien vivre"], marques=["1", "2", "3"],
                    cles=["famille", "village", "bien vivre"], x=170, y=150, w=940),
        "tab_acr": dict(type="tableau", img="t-acropole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .42],
                        legende="Leo von Klenze, l'Acropole et l'Aréopage d'Athènes, reconstitution, 1846"),
        "c_nat": dict(type="cit", a="Aristote", o="La Politique, I, 1, § 9, trad. Barthélemy-Saint-Hilaire", x=170, y=210, w=940),
        "zoon": dict(type="def", cles=["politique", "parole"], terme="Zôon politikon",
                     t="L'homme est un animal politique : fait pour vivre dans une cité.",
                     etape="Plus que les abeilles : la nature ne fait rien en vain, et elle ne donne la parole qu'à l'homme.",
                     x=170, y=200, w=940),
        "tab_abe": dict(type="tableau", img="et2-ruche", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Représentation emblématique d'une ruche, gravure, XVIIᵉ siècle (Rijksmuseum, Amsterdam)"),
        "c_par": dict(type="cit", a="Aristote", o="La Politique, I, 1, § 10, trad. Barthélemy-Saint-Hilaire", x=170, y=210, w=940),
        "tab_rem": dict(type="tableau", img="et2-aristote-rembrandt", fond=True, sombre=True, de=[1.35, .6, .55], a=[1.1, .5, .5],
                        legende="Rembrandt, Aristote contemplant le buste d'Homère, 1653 (Metropolitan Museum of Art, New York)"),
        "tout": dict(type="liste", titre="Le tout avant la partie", items=[
            "La cité passe avant l'individu", "Une main séparée du corps n'est plus une main"],
                     marques=["1", "2"], x=170, y=190, w=940),
        "c_brute": dict(type="cit", a="Aristote", o="La Politique, I, 1, § 12, trad. Barthélemy-Saint-Hilaire", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ II. Hobbes
    dict(id="hobbes", chap="Hobbes : la peur et le Léviathan", fond="nuit", humeur="tension", notions=["la nature", "la liberté", "la religion"],
         retenir="Hobbes : égaux par nature, les hommes se craignent. Sans pouvoir commun, la guerre de chacun contre chacun. Le pacte crée le Léviathan, « dieu mortel ».",
         beats=[
        "{tab_arm}{hob}Deux mille ans plus tard, en Angleterre, un philosophe ose dire le contraire. {n_hob}Thomas Hobbes naît en 1588, "
        "l'année où l'Armada espagnole menace son pays. Sa mère, raconte-t-il, accoucha de jumeaux : lui… et la peur.",
        "{-hob}{-n_hob}{-tab_arm}{tab_lev}{rappel}{mot_g}On l'a vu dans la série sur la liberté : pour Hobbes, sans État, c'est la guerre, "
        "et l'on échange sa liberté contre la sécurité. Allons plus loin : pourquoi la guerre ?",
        "{-rappel}{-mot_g}{pq}{pq.1}D'abord, parce que les hommes sont à peu près {!égaux}égaux. Le plus faible peut tuer le plus fort : "
        "par la ruse, ou en s'alliant à d'autres. Personne n'est assez fort pour être tranquille. "
        "{pq.2}Ensuite, trois passions les opposent : la rivalité, pour les biens ; la méfiance, pour sa sécurité ; "
        "{pq.3}et la gloire, pour sa réputation.",
        "{-pq}",
        ("C", "Tant que les hommes vivent sans un pouvoir commun qui les tienne tous en respect, ils sont dans cette condition "
              "qu'on appelle guerre, et cette guerre est celle de chacun contre chacun.", "c_hob"),
        "{-c_hob}{exp}Une guerre qui n'est pas forcément faite de combats : il suffit qu'on soit toujours prêt à se battre. "
        "Pas d'agriculture, pas de commerce, pas de sciences ; une vie, dit Hobbes, solitaire, pauvre, brutale et courte.",
        "{exp.1}Tu trouves cela exagéré ? Hobbes te répond par l'expérience. Quand tu pars en voyage, tu prends tes précautions. "
        "Quand tu vas dormir, tu fermes ta porte à clé. {exp.2}Que penses-tu donc de tes voisins ? "
        "Montréal, en 1969, n'a pas eu besoin de plus de quelques heures.",
        "{-exp}{-tab_lev}{tab_lev2}{pacte}La solution : un pacte. Chacun dit à chacun : je renonce à mon droit de me gouverner moi-même, "
        "et je le donne à cet homme, ou à cette assemblée, à condition que tu en fasses autant. "
        "{pacte.1}La multitude devient alors une seule personne : l'État. Hobbes l'appelle le grand Léviathan, "
        "du nom du monstre marin de la Bible, {-pacte}{dieu}ou plutôt, ajoute-t-il, ce dieu mortel, à qui nous devons la paix.",
        "{-dieu}{fr}Regarde le frontispice du livre. {fr.1}Un géant couronné domine la campagne. {fr.2}Son corps est fait de centaines "
        "de petits hommes, tournés vers sa tête. {fr.3}Dans une main, l'épée : le pouvoir civil. Dans l'autre, la crosse : le pouvoir religieux. "
        "Hobbes ne veut pas qu'ils soient séparés : la {#la religion}religion elle-même doit obéir au souverain.",
        "{fr.4}Et ce souverain doit être absolu. Car les conventions, sans l'épée, ne sont que des mots.",
        "{-fr}{-tab_lev2}",
    ], vis={
        "tab_arm": dict(type="tableau", img="et2-armada", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                        legende="Philippe-Jacques de Loutherbourg, La Défaite de l'Armada espagnole, 8 août 1588, 1796 (National Maritime Museum, Londres)"),
        "n_hob": dict(type="note", titre="Thomas Hobbes (1588-1679)", cles=["Armada", "peur"],
                     t="Né en 1588, l'année où l'Armada espagnole menace l'Angleterre.",
                     etape="« Ma mère accoucha de jumeaux : moi et la peur. »", x=640, y=150, w=570),
        "hob": dict(type="portrait", annee=1588, img="hobbes", nom="Thomas Hobbes", dates="1588 – 1679",
                    legende="Léviathan (1651)", x=110, y=120, w=330, h=420),
        "tab_lev": dict(type="tableau", img="et2-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .5],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, Londres, 1651 (British Library)"),
        "mot_g": dict(type="mot", t="Sans État, la guerre", g="on échange sa liberté contre la sécurité", y=220, taille=80),
        "rappel": dict(type="tag", style="lien", t="Série « La liberté », épisode 5 : la liberté contre la sécurité", x=170, y=560, w=760),
        "pq": dict(type="liste", titre="Pourquoi la guerre ?", items=[
            "Égaux par nature : le plus faible peut tuer le plus fort",
            "La rivalité (les biens), la méfiance (la sécurité)…",
            "… et la gloire (la réputation)"], marques=["1", "2", "3"], cles=["Égaux", "rivalité", "méfiance", "gloire"],
                   x=170, y=160, w=940),
        "c_hob": dict(type="cit", a="Hobbes", o="Léviathan, chap. XIII (1651), traduit de l'anglais", para=True, x=170, y=180, w=940),
        "exp": dict(type="liste", titre="L'état de nature selon Hobbes", items=[
            "Tu voyages : tu prends tes précautions", "Tu dors : tu fermes ta porte à clé"],
                    marques=["1", "2"], x=170, y=200, w=940),
        "tab_lev2": dict(type="tableau", img="et2-leviathan", fond=True, sombre=True, de=[2.2, .5, .17], a=[1.5, .5, .2],
                         legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651, détail"),
        "pacte": dict(type="def", cles=["renonce", "à condition"], terme="Le pacte",
                      t="Chacun renonce à se gouverner lui-même, à condition que tous en fassent autant.",
                      etape="La multitude devient une seule personne : l'État, le Léviathan.", x=170, y=170, w=940),
        "dieu": dict(type="mot", t="Le dieu mortel", g="Hobbes, Léviathan, chap. XVII", y=430, taille=88),
        "fr": dict(type="liste", titre="Le frontispice", items=[
            "Un géant couronné domine la campagne", "Son corps : des centaines de petits hommes",
            "L'épée (le civil) et la crosse (le religieux)", "Un souverain absolu : sans l'épée, les conventions ne sont que des mots"],
                   marques=["1", "2", "3", "4"], x=170, y=240, w=940),
    }),

    # ------------------------------------------------------------------ III. Locke
    dict(id="locke", chap="Locke : un juge impartial", fond="aube", humeur="lumiere", notions=["le travail", "la justice", "la liberté"],
         retenir="Locke : à l'état de nature, il manque des lois établies, un juge impartial, une force pour exécuter. L'État a pour fin de conserver les « propriétés » : la vie, la liberté, les biens.",
         beats=[
        "{tab_lab}{locke}Quarante ans plus tard, John Locke ne voit pas l'état de nature aussi noir. "
        "{n_lk}{n_lk.1}Les hommes y ont déjà une loi : la loi naturelle, que la raison enseigne. {n_lk.2}Ne nuire à personne dans sa vie, sa liberté, ses biens.",
        "Ils ont même déjà une propriété. D'où vient-elle ? Du {#le travail}travail.",
        "{-n_lk}",
        ("C", "Le travail de son corps et l'ouvrage de ses mains, nous le pouvons dire, sont son bien propre.", "c_trav"),
        "{-locke}{-c_trav}{manq}Alors, pourquoi l'État ? Parce que, dans l'état de nature, trois choses manquent. "
        "{manq.1}Des lois établies, connues de tous. {manq.2}Un juge impartial : chacun y est juge dans sa propre cause, "
        "et la colère, la vengeance l'emportent toujours trop loin. {manq.3}Et une force capable de faire exécuter la sentence.",
        "{-manq}{-tab_lab}{tab_wil}{an88}Voilà ce que les hommes viennent chercher dans l'État. Et Locke en dit le but.",
        "{-an88}",
        ("C", "… la plus grande et la principale fin que se proposent les hommes, lorsqu'ils s'unissent en communauté "
              "et se soumettent à un gouvernement, c'est de conserver leurs propriétés…", "c_fin"),
        "{-c_fin}{prop}Attention au mot : par propriétés, Locke entend {prop.1}la vie, {prop.2}la liberté et {prop.3}les biens. "
        "L'État n'est pas le maître de ces droits. Il en est le gardien.",
        "{-prop}{-tab_wil}{tab_dan}{lions}Et le souverain absolu de Hobbes ? Locke répond aux partisans du pouvoir absolu par une image restée célèbre.",
        "{-lions}",
        ("C", "… s'imaginer que les hommes sont assez fous pour prendre grand soin de remédier aux maux que pourraient leur faire "
              "des fouines et des renards, et […] croire même qu'il serait fort doux pour eux d'être dévorés par des lions.", "c_lions"),
        "{-c_lions}{-tab_dan}{tab_dec}{res}Fuir les renards pour se jeter dans la gueule du lion ? Non. "
        "{res.1}Si le gouvernement viole les droits qu'il devait garder, il trahit le contrat, et le peuple peut lui {#la justice}résister. "
        "On l'a vu dans la série sur la liberté. {res.2}En 1776, la Déclaration d'indépendance américaine reprend presque mot pour mot "
        "cette idée : la vie, la liberté, et le droit de renverser un gouvernement tyrannique.",
        "{-res}{-tab_dec}",
    ], vis={
        "tab_lab": dict(type="tableau", img="et2-labourage", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .5],
                        legende="Rosa Bonheur, Labourage nivernais, 1849 (musée d'Orsay, Paris)"),
        "n_lk": dict(type="liste", titre="L'état de nature selon Locke", items=[
            "Une loi naturelle, que la raison enseigne",
            "Ne nuire à personne : vie, liberté, biens"], marques=["1", "2"], x=640, y=150, w=570),
        "locke": dict(type="portrait", annee=1632, img="locke", nom="John Locke", dates="1632 – 1704",
                      legende="Second Traité du gouvernement civil (1690)", x=110, y=120, w=330, h=420),
        "c_trav": dict(type="cit", a="Locke", o="Traité du gouvernement civil, chap. V, § 27 (1690), trad. Mazel", x=640, y=180, w=570),
        "manq": dict(type="liste", titre="Ce qui manque à l'état de nature", items=[
            "Des lois établies, connues de tous", "Un juge impartial", "Une force pour faire exécuter la sentence"],
                     marques=["1", "2", "3"], cles=["lois", "juge", "force"], x=170, y=160, w=940),
        "tab_wil": dict(type="tableau", img="et2-torbay", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Jan Wyck, Guillaume III débarquant à Brixham, 5 novembre 1688 (la « Glorieuse Révolution »)"),
        "an88": dict(type="mot", t="1688", g="la Glorieuse Révolution : le roi chassé, le Parlement souverain", y=270, taille=110),
        "c_fin": dict(type="cit", a="Locke", o="Traité du gouvernement civil, chap. IX, § 124 (1690), trad. Mazel", x=170, y=190, w=940),
        "prop": dict(type="cartes", items=[
            dict(ic="porte", t="La vie", q="nul ne peut me la prendre"),
            dict(ic="chemins", t="La liberté", q="ne dépendre de la volonté arbitraire de personne"),
            dict(ic="colonnes", t="Les biens", q="ce que mon travail a produit")]),
        "tab_dan": dict(type="tableau", img="et2-lions", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Pierre Paul Rubens, Daniel dans la fosse aux lions, vers 1614-1616 (National Gallery of Art, Washington)"),
        "lions": dict(type="mot", t="Des renards… et un lion", g="Locke contre le souverain absolu", y=270, taille=84),
        "c_lions": dict(type="cit", a="Locke", o="Traité du gouvernement civil, chap. VII, § 93 (1690), trad. Mazel", x=170, y=160, w=940),
        "res": dict(type="liste", titre="Le droit de résistance", items=[
            "Le gouvernement qui viole nos droits trahit le contrat",
            "1776 : la Déclaration d'indépendance américaine"], marques=["1", "2"], x=170, y=190, w=940),
        "tab_dec": dict(type="tableau", img="et2-declaration", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="John Trumbull, La Déclaration d'indépendance, 1818 (Capitole des États-Unis, Washington)"),
    }),

    # ------------------------------------------------------------------ IV. Rousseau
    dict(id="rousseau", chap="Rousseau : le faux et le vrai contrat", fond="nuit", humeur="mystere", notions=["la justice", "la liberté"],
         retenir="Rousseau : la propriété fonde la société civile, et le riche invente un faux contrat. Le vrai contrat : chacun se donne à tous, sous la volonté générale. Le peuple seul est souverain.",
         beats=[
        "{tab_van}{rous}Locke fonde la propriété sur le travail. Rousseau, lui, voit les choses tout autrement. "
        "Écoute le début de la seconde partie de son Discours sur l'origine de l'inégalité, en 1755.",
        ("C", "Le premier qui, ayant enclos un terrain, s'avisa de dire : Ceci est à moi, et trouva des gens assez simples "
              "pour le croire, fut le vrai fondateur de la société civile.", "c_encl"),
        "{-rous}{-c_encl}{faux}Avec la propriété viennent les inégalités, les jalousies, la guerre. Alors le riche, qui a le plus à perdre, "
        "a une idée de génie. {faux.1}Il propose aux pauvres de s'unir, pour protéger les faibles et garantir à chacun ce qu'il possède. "
        "{faux.2}Mais qui possède le plus ? Lui. Le contrat protège ses biens, et fige l'inégalité.{-faux}",
        ("C", "Tous coururent au-devant de leurs fers croyant assurer leur liberté…", "c_fers"),
        "{-c_fers}{-tab_van}{tab_jeu}{vrai}{ctr}Faut-il alors renoncer à l'État ? Non. En 1762, dans le Contrat social, Rousseau cherche "
        "le contrat légitime. On l'a vu dans la série sur la liberté : obéir à la loi qu'on s'est donnée, c'est être libre. "
        "Voici la clause qui rend cela possible.",
        "{-vrai}{-ctr}",
        ("C", "Chacun de nous met en commun sa personne et toute sa puissance sous la suprême direction de la volonté générale ; "
              "et nous recevons en corps chaque membre comme partie indivisible du tout.", "c_pacte"),
        "{-c_pacte}{trois_c}Regarde la différence. {trois_c.g}Chez Hobbes, on se donne à un maître. "
        "{trois_c.d}Chez Rousseau, chacun se donne à tous, et donc à personne en particulier. "
        "Le souverain, c'est le {!peuple}peuple lui-même. Et la souveraineté ne se délègue pas.",
        "{-trois_c}{-tab_jeu}{tab_hou}{plus_r}Pour aller plus loin, Rousseau va jusqu'à se moquer du régime anglais, "
        "que Locke admirait tant.{-plus_r}",
        ("C", "Le peuple anglais pense être libre ; il se trompe fort, il ne l'est que durant l'élection des membres du Parlement ; "
              "sitôt qu'ils sont élus, il est esclave, il n'est rien.", "c_angl"),
        "{-c_angl}{q_rep}Voter une fois tous les cinq ans, est-ce gouverner ? La question est toujours posée à nos démocraties. "
        "Elle touche à la {#la justice}justice même de nos lois : sont-elles vraiment la volonté de tous ?",
        "{-q_rep}{-tab_hou}",
    ], vis={
        "tab_van": dict(type="tableau", img="et2-enclos", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .55],
                        legende="Vincent van Gogh, Champ de blé clos au soleil levant, 1889"),
        "rous": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                     legende="Discours sur l'inégalité (1755) · Du contrat social (1762)", x=110, y=120, w=330, h=420),
        "c_encl": dict(type="cit", a="Rousseau", o="Discours sur l'origine de l'inégalité, seconde partie (1755)", x=640, y=150, w=570),
        "faux": dict(type="liste", titre="Le faux contrat du riche", items=[
            "« Unissons-nous » : protéger les faibles, garantir à chacun ce qu'il possède",
            "Mais le contrat protège surtout les biens du riche"], marques=["1", "2"], x=170, y=190, w=940),
        "c_fers": dict(type="cit", a="Rousseau", o="Discours sur l'origine de l'inégalité, seconde partie (1755)", x=170, y=220, w=940),
        "tab_jeu": dict(type="tableau", img="et2-jeudepaume", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Jacques-Louis David, Le Serment du Jeu de paume (20 juin 1789), détail (musée Carnavalet, Paris)"),
        "vrai": dict(type="tag", style="lien", t="Série « La liberté », épisode 5 : la volonté générale, obéir à soi-même",
                     x=170, y=560, w=800),
        "ctr": dict(type="mot", t="Du contrat social", g="1762 : chercher le contrat légitime", y=230, taille=88),
        "c_pacte": dict(type="cit", a="Rousseau", o="Du contrat social, I, 6 (1762)", x=170, y=170, w=940),
        "trois_c": dict(type="cols", g="Hobbes", gq="chacun se donne à un maître", d="Rousseau",
                        dq="chacun se donne à tous : le peuple est souverain", vs="≠"),
        "tab_hou": dict(type="tableau", img="et2-communes", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="George Hayter, La Chambre des communes en 1833, 1833-1843 (National Portrait Gallery, Londres)"),
        "plus_r": dict(type="tag", style="plus", t="Pour aller plus loin", x=170, y=560, w=420),
        "c_angl": dict(type="cit", a="Rousseau", o="Du contrat social, III, 15 (1762)", x=170, y=170, w=940),
        "q_rep": dict(type="question", t="Voter une fois tous les cinq ans, est-ce gouverner ?"),
    }),

    # ------------------------------------------------------------------ V. fiction ou histoire
    dict(id="fiction", chap="Un contrat… qui n'a jamais eu lieu ?", fond="aube", humeur="calme", notions=["la raison", "la nature"],
         retenir="Le contrat n'est pas un fait historique : c'est une hypothèse, une idée de la raison, qui sert à juger la légitimité d'un État.",
         beats=[
        "{tab_bay}{tab3}Faisons le point. Trois penseurs, trois contrats. {tab3.1}Hobbes : on fuit la guerre, on obtient la sécurité, "
        "sous un souverain absolu. {tab3.2}Locke : on veut un juge impartial, on obtient un gouvernement limité, qui garde nos droits. "
        "{tab3.3}Rousseau : on cherche la liberté, on obtient un peuple souverain.",
        "{-tab3}{hume}{n_hume}Mais une objection s'impose, et c'est David Hume qui la formule, en 1748. Ce contrat, qui l'a jamais signé ? "
        "Les États sont nés de la conquête, de l'usurpation, de la violence. Regarde la tapisserie de Bayeux : "
        "en 1066, Guillaume ne demande pas aux Anglais leur avis. Il les conquiert.",
        "{-hume}{-n_hume}{hyp}{hyp.1}La réponse des philosophes du contrat est fine. Rousseau l'avait dit lui-même : "
        "commençons par écarter tous les faits. Le contrat n'est pas un événement du passé. "
        "{hyp.2}C'est une hypothèse, une expérience de pensée.",
        "{-hyp}{-tab_bay}{tab_kant}{crit}Pour aller plus loin, Kant le dira nettement : le contrat originaire est une simple idée "
        "de la {#la raison}raison. {crit.1}Il ne raconte pas comment les États sont nés. {crit.2}Il permet de juger s'ils sont légitimes. "
        "Une loi est juste si tout un peuple pourrait y consentir.",
        "{-crit}{nat}Reste le grand débat de cet épisode. {nat.g}Pour Aristote, la cité est naturelle : l'homme y accomplit sa nature. "
        "{nat.d}Pour Hobbes, Locke et Rousseau, l'État est artificiel : une œuvre humaine, qui doit être justifiée.",
        ("Et ce qui a été fait par les hommes… peut être défait par eux.", {"rate": "-5%", "pitch": "-2Hz"}),
        "{-nat}{-tab_kant}",
    ], vis={
        "tab_bay": dict(type="tableau", img="et2-bayeux", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.0, .7, .5],
                        legende="Tapisserie de Bayeux, la bataille d'Hastings (1066), vers 1070 (musée de la Tapisserie, Bayeux)"),
        "tab3": dict(type="liste", titre="Trois contrats", items=[
            "Hobbes : contre la guerre → la sécurité, un souverain absolu",
            "Locke : un juge impartial → un gouvernement limité",
            "Rousseau : la liberté → le peuple souverain"], marques=["1", "2", "3"],
                     cles=["sécurité", "limité", "souverain"], x=170, y=150, w=940),
        "hume": dict(type="portrait", annee=1711, img="hume", nom="David Hume", dates="1711 – 1776",
                     legende="Du contrat primitif (1748)", x=110, y=120, w=330, h=420),
        "n_hume": dict(type="note", titre="L'objection de Hume", cles=["conquête"],
                       t="Ce contrat, qui l'a jamais signé ?", etape="Les États naissent de la conquête, de l'usurpation, de la violence.",
                       x=640, y=180, w=570),
        "hyp": dict(type="def", cles=["hypothèse", "expérience de pensée"], terme="Le contrat",
                    t="Pas un événement du passé : une hypothèse.",
                    etape="Rousseau : « commençons par écarter tous les faits ».", x=170, y=200, w=940),
        "tab_kant": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                         legende="Königsberg, ville de Kant, photochrome, vers 1900 (domaine public)"),
        "crit": dict(type="liste", titre="Une idée de la raison (Kant)", items=[
            "Il ne raconte pas comment les États sont nés", "Il permet de juger s'ils sont légitimes"],
                     marques=["✗", "✓"], x=170, y=190, w=940, plus=True),
        "nat": dict(type="cols", g="Aristote", gq="la cité est naturelle", d="Hobbes, Locke, Rousseau",
                    dq="l'État est artificiel : il doit être justifié", vs="≠", repere="Repère · nature / artifice"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Aristote. L'homme est un animal politique ; "
        "la cité est naturelle, et la parole sert à dire le juste et l'injuste.",
        "{rec.2}Deux : Hobbes. Sans pouvoir commun, la guerre de chacun contre chacun ; le pacte crée le Léviathan, souverain absolu.",
        "{rec.3}Trois : Locke. L'État est un juge impartial, gardien de la vie, de la liberté et des biens ; s'il trahit, on lui résiste.",
        "{rec.4}Quatre : Rousseau. Le faux contrat du riche, et le vrai : le peuple souverain, sous la volonté générale.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Mais un État assez fort pour nous protéger est aussi assez fort pour nous écraser. "
        "Comment empêcher le protecteur de devenir un tyran ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : l'État et la liberté. Montesquieu, Spinoza, Hannah Arendt, et le 1984 d'Orwell.",
         {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="et2-leviathan", fond=True, sombre=True, de=[1.6, .5, .2], a=[1.0, .5, .4],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651 (British Library)"),
        "rec": dict(type="carte", centre="POURQUOI L'ÉTAT ?", branches=[
            dict(t="Aristote", items=["l'animal politique", "la cité naturelle", "la parole : le juste"]),
            dict(t="Hobbes", items=["la guerre de chacun contre chacun", "le pacte", "le Léviathan"]),
            dict(t="Locke", items=["un juge impartial", "vie, liberté, biens", "le droit de résistance"]),
            dict(t="Rousseau", items=["« Ceci est à moi »", "la volonté générale", "un contrat : une idée"])]),
        "tab_fin": dict(type="tableau", img="et2-panoptique", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Willey Reveley, plan du Panoptique de Jeremy Bentham, 1791"),
        "q_suite": dict(type="question", t="Comment empêcher le protecteur de devenir un tyran ?"),
        "fin": dict(type="titre", sur="À suivre", t="L'État et la liberté", sous="Épisode 3 · Montesquieu, Spinoza, Arendt, Orwell"),
    }),
]

QUIZ = [
    dict(q="Pour Aristote, pourquoi l'homme est-il un animal politique plus que les abeilles ?",
         r=["Parce qu'il est plus fort", "Parce que seul il a la parole, qui exprime le juste et l'injuste",
            "Parce qu'il a signé un contrat", "Parce qu'il craint la mort violente"], ok=1,
         voir="c_par", ex="La nature ne fait rien en vain : elle ne donne la parole qu'à l'homme. Parler du juste, c'est déjà faire de la politique (La Politique, I)."),
    dict(q="Selon Aristote, celui qui peut vivre sans cité est…",
         r=["un sage", "un citoyen modèle", "une brute ou un dieu", "un homme libre"], ok=2,
         voir="c_brute", ex="La cité est naturelle, et passe avant l'individu comme le tout avant la partie."),
    dict(q="Pourquoi, selon Hobbes, l'état de nature est-il une guerre de chacun contre chacun ?",
         r=["Parce que les hommes sont naturellement méchants", "Parce qu'ils sont à peu près égaux, et que rivalité, méfiance et gloire les opposent",
            "Parce que Dieu les a abandonnés", "Parce que les riches oppriment les pauvres"], ok=1,
         voir="pq", ex="Le plus faible peut tuer le plus fort : personne n'est en sécurité. Sans pouvoir commun, la vie est « solitaire, pauvre, brutale et courte »."),
    dict(q="Que tient le géant du frontispice du Léviathan ?",
         r=["Une balance et un livre", "L'épée et la crosse : le pouvoir civil et le pouvoir religieux",
            "Une couronne et un sceptre", "Une charrue et une épée"], ok=1,
         voir="fr", ex="Son corps est fait des sujets eux-mêmes ; le souverain réunit les deux pouvoirs."),
    dict(q="Selon Locke, que manque-t-il à l'état de nature ?",
         r=["Une loi naturelle", "La propriété", "Des lois établies, un juge impartial, une force pour exécuter", "Un roi de droit divin"], ok=2,
         voir="manq", ex="Traité du gouvernement civil, § 124-126. Chacun y est juge dans sa propre cause. La fin de l'État : conserver la vie, la liberté, les biens."),
    dict(q="« Le premier qui, ayant enclos un terrain, s'avisa de dire : Ceci est à moi… » Qui l'écrit, et pour dire quoi ?",
         r=["Locke, pour fonder la propriété sur le travail", "Rousseau, pour montrer que la propriété fonde la société civile et l'inégalité",
            "Hobbes, pour justifier le souverain", "Aristote, pour décrire la famille"], ok=1,
         voir="c_encl", ex="Discours sur l'inégalité (1755) : le riche propose ensuite un faux contrat qui protège ses biens. « Tous coururent au-devant de leurs fers »."),
    dict(q="Le contrat social a-t-il vraiment eu lieu ?",
         r=["Oui, en 1789", "Oui, dans l'Antiquité", "Non : c'est une hypothèse, une idée qui sert à juger la légitimité d'un État",
            "Non : c'est pourquoi l'État est illégitime"], ok=2,
         voir="crit", ex="Hume objecte que les États naissent de la conquête. Rousseau : « écartons tous les faits » ; Kant : une idée de la raison."),
]

CREDITS = [
    "Portraits : Aristote (buste, Palazzo Altemps, photo Jastrow, domaine public) ; Thomas Hobbes (John Michael Wright, vers 1669-1670) ; "
    "John Locke (Godfrey Kneller, 1697) ; Jean-Jacques Rousseau (Maurice Quentin de La Tour, 1753) ; David Hume (Allan Ramsay, 1766) : domaine public",
    "Tableaux : John Seymour Lucas, Les Émeutes de Gordon (1879) ; Rembrandt, Aristote contemplant le buste d'Homère (1653) ; "
    "Leo von Klenze, l'Acropole (1846) ; Philippe-Jacques de Loutherbourg, La Défaite de l'Armada (1796) ; Rosa Bonheur, Labourage nivernais (1849) ; "
    "Jan Wyck, Guillaume III à Brixham (1688) ; Rubens, Daniel dans la fosse aux lions (vers 1614-1616) ; John Trumbull, La Déclaration d'indépendance (1818) ; "
    "Van Gogh, Champ de blé clos au soleil levant (1889) ; Jacques-Louis David, Le Serment du Jeu de paume (musée Carnavalet) ; "
    "George Hayter, La Chambre des communes en 1833 : domaine public",
    "Gravures et documents : Abraham Bosse, frontispice du Léviathan (1651) et dessin sur vélin (British Library) ; ruche emblématique (Rijksmuseum) ; "
    "Tapisserie de Bayeux (vers 1070) ; Königsberg, photochrome (vers 1900) ; Willey Reveley, plan du Panoptique (1791) : domaine public",
    "Citations : Aristote, La Politique, trad. J. Barthélemy-Saint-Hilaire (1874) ; Locke, Traité du gouvernement civil, trad. D. Mazel (1795) ; "
    "Rousseau, Discours sur l'origine de l'inégalité (1755) et Du contrat social (1762) ; Hobbes, Léviathan (1651), traduit de l'anglais pour la série. "
    "Hume, Kant et la grève de la police de Montréal (1969) sont résumés par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
