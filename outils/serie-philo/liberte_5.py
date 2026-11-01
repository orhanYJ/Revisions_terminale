"""La liberté, épisode 5 : « Libres ensemble » (l'État, la loi, la société).

Même format que liberte_1.py (voir l'en-tête de ce fichier) : beats lus, repères {id} / {-id} / {id.k} / {!mot},
citations ("C", texte, id), visuels par scène.
Citations : Hobbes, Léviathan, XIII (trad. F. Tricaud) ; Locke, Second Traité, § 57 (formule de la traduction courante) ;
Rousseau, Du contrat social, I, 1, 6 et 7 ; Montesquieu, De l'esprit des lois, XI, 3 et 4 ; Constant, discours de 1819 ;
Mill, De la liberté, chap. I (approchée) ; Tocqueville, De la démocratie en Amérique, I, II, 7.
"""

CODE = "liberte-5"
NOTION = "La liberté"
NUM = 5
TITRE = "Libres ensemble"
SUIVANT = "Épisode 6 · La liberté à l'épreuve du bac"
PRONONCIATION = {"Isaiah Berlin": "Isaïa Berline", "Landsgemeinde": "Lannsguémaïnde"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_rob}Un naufragé échoue sur une île déserte. Il s'appelle Robinson Crusoé, et il va y vivre vingt-huit ans.",
        "{q0}Sur son île, personne ne lui donne d'ordre. Pas de roi, pas de police, pas d'impôts. Aucune loi. "
        "{-q0}{rob}Alors, question : {rob.1}Robinson est-il l'homme le plus libre du monde ?",
        ("Regarde mieux.", {"rate": "-6%", "pitch": "-1Hz"}),
        "{rob.2}Il passe ses journées à survivre : chasser, construire, se protéger. "
        "{rob.3}Il ne peut ni se faire soigner, ni apprendre, ni parler à personne. Libre de tout… et capable de presque rien.",
        "{-rob}{-tab_rob}{tab_hem}{q1}Voilà le paradoxe de cet épisode. Les autres, la loi, l'État semblent limiter ma liberté. "
        "Et si, au contraire, ils en étaient la condition ?",
        "{-q1}Après la liberté de l'esprit, place à la liberté politique : celle que nous vivons ensemble.",
        ("P", 0.3),
        "{-tab_hem}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_rob": dict(type="tableau", img="t5-robinson", fond=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="N. C. Wyeth, Robinson Crusoé, illustration pour le roman de Daniel Defoe, 1920"),
        "q0": dict(type="question", t="Aucune loi, aucun maître…"),
        "rob": dict(type="cols", g="Libre de…", gq="aucun ordre, aucune loi, aucun maître", d="Libre pour… ?",
                    dq="survivre seul : presque rien d'autre", vs="?"),
        "tab_hem": dict(type="tableau", img="t5-hemicycle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .55],
                        legende="L'hémicycle de l'Assemblée nationale, Paris (photo Coucouoeuf, CC BY-SA 3.0)"),
        "q1": dict(type="question", t="Les autres, la loi, l'État : obstacles… ou conditions de ma liberté ?"),
        "titre": dict(type="titre", sur="La liberté · Épisode 5", t="Libres ensemble",
                      sous="L'État, la loi, la société"),
    }),

    # ------------------------------------------------------------------ I. l'état de nature
    dict(id="nature", chap="L'état de nature", fond="aube", humeur="tension", notions=["l'État", "la nature"],
         retenir="Hobbes : sans État, la liberté de tous fait la guerre de chacun contre chacun.", beats=[
        "{tab_sau}{nat}Pour comprendre à quoi sert l'État, les philosophes ont fait une expérience de pensée : "
        "imaginer les hommes avant toute société, sans loi ni gouvernement. C'est ce qu'ils appellent {!état de nature}l'état de nature.",
        "{-nat}{hobbes}{tab_lev}Thomas Hobbes, que tu connais depuis l'épisode un, a vu l'Angleterre se déchirer dans une guerre civile. "
        "Son verdict est sombre. À l'état de nature, chacun a droit à tout, et peut tout faire pour se conserver.",
        "Mais si tous ont droit à tout, chacun est une menace pour chacun. C'est la guerre de chacun contre chacun. "
        "Imagine une ville sans police ni tribunaux : tu fermerais ta porte à double tour, tu dormirais mal, tu te méfierais de tous.",
        "Hobbes reprend d'ailleurs une vieille formule latine, empruntée au poète Plaute : l'homme est un loup pour l'homme.",
        ("C", "La vie de l'homme est alors solitaire, besogneuse, pénible, quasi animale, et brève.", "c_hob"),
        "{-hobbes}{-c_hob}{pacte}Pour en sortir, les hommes passent un pacte. {pacte.1}Chacun renonce à sa liberté naturelle, "
        "{pacte.2}et la remet à un souverain tout-puissant, {pacte.3}en échange de la sécurité. Ce souverain, c'est le Léviathan.",
        "{-pacte}{neg}Où reste alors la liberté des sujets ? {neg.1}Dans ce que la loi ne règle pas. "
        "Là où le souverain se tait, je suis libre. {neg.2}Tu reconnais la liberté négative : l'absence d'obstacles.",
        ("Moins de liberté… mais enfin la paix. C'est le marché de Hobbes.", {"rate": "-5%"}),
        "{-neg}{-tab_lev}{crit}Ce marché pose pourtant une question redoutable : {crit.1}qui me protégera du Léviathan lui-même ? "
        "Un souverain tout-puissant peut garantir la paix… mais aussi m'écraser. Les penseurs suivants vont chercher une autre voie.",
        ("P", 0.6),
    ], vis={
        "tab_sau": dict(type="tableau", img="t5-sauvage", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Thomas Cole, Le Cours de l'empire : l'état sauvage, 1834"),
        "nat": dict(type="def", cles=["avant", "loi"], terme="L'état de nature",
                    t="Une expérience de pensée : les hommes avant toute société, sans loi ni gouvernement.",
                    x=170, y=200, w=940),
        "hobbes": dict(type="portrait", annee=1588, legende="Léviathan (1651)", img="hobbes", nom="Thomas Hobbes",
                       dates="1588 – 1679", x=110, y=120, w=330, h=420),
        "tab_lev": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .3],
                        legende="Abraham Bosse, frontispice du Léviathan, 1651 · le souverain fait de tous ses sujets"),
        "c_hob": dict(type="cit", a="Hobbes", o="Léviathan, chap. XIII (1651 ; trad. F. Tricaud)", x=640, y=170, w=570),
        "pacte": dict(type="liste", titre="Le pacte selon Hobbes", items=[
            "Chacun renonce à sa liberté naturelle", "Il la remet à un souverain tout-puissant",
            "En échange : la sécurité"], marques=["1", "2", "→"], x=170, y=170, w=940),
        "neg": dict(type="liste", titre="La liberté des sujets", items=[
            "Elle réside là où la loi se tait", "C'est la liberté négative : l'absence d'obstacles"],
                    marques=["→", "✻"], x=170, y=190, w=940),
        "crit": dict(type="question", t="Qui me protégera du Léviathan lui-même ?"),
    }),

    # ------------------------------------------------------------------ II. la loi qui libère
    dict(id="loi", chap="La loi qui libère", fond="nuit", humeur="lumiere", notions=["l'État", "la justice"],
         retenir="Locke, Montesquieu : la loi protège la liberté ; et pour la garantir, le pouvoir arrête le pouvoir.", beats=[
        "{locke}{tab_tra}En 1690, un autre Anglais, John Locke, renverse la perspective. Pour lui, la loi n'est pas la cage de la liberté. "
        "Elle en est la protection.",
        ("C", "Là où il n'y a pas de loi, il n'y a pas de liberté.", "c_loc"),
        "{-c_loc}{-locke}{lic}Pourquoi ? Parce que sans loi, je suis à la merci du plus fort, de ses caprices, de sa violence. "
        "{lic.g}La liberté n'est pas la licence, faire n'importe quoi. {lic.d}C'est ne dépendre de la volonté arbitraire de personne.",
        "{-lic}Et le pouvoir n'est {#la justice}légitime que s'il protège les droits naturels de chacun : la vie, la liberté, les biens. "
        "S'il les viole, s'il devient tyrannique, le peuple a le droit de lui résister. C'est la réponse de Locke à Hobbes.",
        "{-locke}{-tab_tra}"
        "{mont}{tab_esp}Un demi-siècle plus tard, en France, Montesquieu donne la définition qu'il te faut connaître par cœur.",
        ("C", "La liberté est le droit de faire tout ce que les lois permettent.", "c_mon"),
        "{-c_mon}{-mont}{pourquoi}Pourquoi pas tout ce que je veux ? {pourquoi.1}Parce que si je pouvais faire ce que les lois défendent, "
        "{pourquoi.2}les autres le pourraient aussi… {pourquoi.3}et il n'y aurait plus de liberté pour personne.",
        "Pense au code de la route. Il t'oblige à t'arrêter au feu rouge. Mais sans lui, personne n'oserait plus prendre la route : "
        "la règle qui me limite est aussi celle qui me permet de circuler.",
        "{-pourquoi}{-tab_esp}{tab_hem2}{abus}Mais Montesquieu sait aussi que tout homme qui a du pouvoir est porté à en abuser. "
        "D'où sa grande idée.",
        "{-abus}",
        ("C", "Pour qu'on ne puisse abuser du pouvoir, il faut que, par la disposition des choses, le pouvoir arrête le pouvoir.",
         "c_pou"),
        "{-c_pou}{-abus}{sep}C'est la séparation des pouvoirs. {sep.1}Ceux qui font les lois, {sep.2}ceux qui les exécutent, "
        "{sep.3}et ceux qui jugent ne doivent jamais être les mêmes.",
        "{-sep}{tab_ddhc}{art}La Déclaration de 1789 en fera un critère. Une société où les droits ne sont pas garantis "
        "et où les pouvoirs ne sont pas séparés, dit son article seize, n'a point de constitution.",
        ("Voilà la réponse à la question de Hobbes : on se protège du Léviathan en le divisant.", {"rate": "-5%"}),
        ("P", 0.6),
    ], vis={
        "locke": dict(type="portrait", annee=1632, legende="Second Traité du gouvernement civil (1690)", img="locke",
                      nom="John Locke", dates="1632 – 1704", x=110, y=120, w=330, h=420),
        "tab_tra": dict(type="tableau", img="t5-traites", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .4],
                        legende="Locke, Two Treatises of Government, page de titre, Londres, 1690 (Library of Congress)"),
        "c_loc": dict(type="cit", a="Locke", o="Second Traité du gouvernement civil, chap. VI, § 57 (1690 ; trad. courante)",
                      x=640, y=190, w=570),
        "lic": dict(type="cols", g="Licence", gq="faire n'importe quoi, à la merci du plus fort", d="Liberté",
                    dq="ne dépendre de la volonté arbitraire de personne", vs="≠"),
        "mont": dict(type="portrait", annee=1689, legende="De l'esprit des lois (1748)", img="montesquieu",
                     nom="Montesquieu", dates="1689 – 1755", x=110, y=120, w=330, h=420),
        "tab_esp": dict(type="tableau", img="t5-esprit", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="Montesquieu, De l'esprit des lois, édition originale, Genève, 1748"),
        "c_mon": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 3 (1748)", x=640, y=190, w=570),
        "pourquoi": dict(type="liste", titre="Pourquoi pas « tout ce que je veux » ?", items=[
            "Si je pouvais faire ce que les lois défendent…", "… les autres le pourraient aussi",
            "… et personne ne serait plus libre"], marques=["1", "2", "→"], x=170, y=170, w=940),
        "tab_hem2": dict(type="tableau", img="t5-hemicycle", fond=True, sombre=True, de=[1.25, .5, .5], a=[1.0, .5, .5],
                        legende="L'hémicycle de l'Assemblée nationale, Paris (photo Coucouoeuf, CC BY-SA 3.0)"),
        "abus": dict(type="mot", t="Tout pouvoir tend à l'abus", g="« c'est une expérience éternelle », dit Montesquieu",
                     y=90, taille=60),
        "c_pou": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 4 (1748)", x=170, y=260, w=940),
        "sep": dict(type="cartes", items=[
            dict(ic="colonnes", t="Législatif", q="fait les lois"),
            dict(ic="porte", t="Exécutif", q="les fait appliquer"),
            dict(ic="chemins", t="Judiciaire", q="juge"),
        ]),
        "tab_ddhc": dict(type="tableau", img="t-ddhc", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                         legende="Jean-Jacques-François Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "art": dict(type="note", cles=["garantie", "séparation", "constitution"], titre="DDHC, article 16",
                    t="Toute société dans laquelle la garantie des droits n'est pas assurée, ni la séparation des pouvoirs déterminée, n'a point de Constitution.",
                    x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ III. Rousseau
    dict(id="rousseau", chap="Rousseau : obéir à soi-même", fond="aube", humeur="lumiere", notions=["l'État", "le devoir"],
         retenir="Rousseau : en obéissant à la loi que je me suis donnée, je n'obéis qu'à moi-même.", beats=[
        "{rousseau}{tab_con}Jean-Jacques Rousseau va plus loin encore. Son Contrat social s'ouvre sur une phrase-choc.",
        ("C", "L'homme est né libre, et partout il est dans les fers.", "c_fer"),
        "{-c_fer}La question n'est donc pas de revenir à l'état de nature. C'est de trouver une société qui ne soit pas une prison. "
        "Rousseau formule le problème avec une précision d'horloger.",
        ("C", "Trouver une forme d'association qui défende et protège de toute la force commune la personne et les biens de chaque "
              "associé, et par laquelle chacun s'unissant à tous n'obéisse pourtant qu'à lui-même et reste aussi libre qu'auparavant.",
         "c_ass"),
        "{-c_ass}{-rousseau}{-tab_con}{tab_gla}{vg}La solution : chacun se donne tout entier à la communauté. {vg.1}Les lois sont votées "
        "par le peuple lui-même, et expriment {!volonté générale}la volonté générale : non la somme des intérêts privés, mais ce qui est bon pour tous.",
        "Attention : la volonté générale n'est pas la volonté de tous. Si chacun vote seulement pour payer moins d'impôts, "
        "on obtient la somme des égoïsmes. La volonté générale, c'est ce que je veux en tant que citoyen, pour le bien commun.",
        "{vg.2}Alors, en obéissant à la loi, je n'obéis qu'à moi-même, puisque j'en suis l'auteur. "
        "Tu reconnais la formule de l'épisode un.",
        "{-vg}",
        ("C", "L'obéissance à la loi qu'on s'est prescrite est liberté.", "c_obe"),
        "{-c_obe}{-vg}{aut}C'est une liberté d'un autre genre : non plus l'absence d'obstacles, mais l'{!autonomie}autonomie. "
        "{aut.1}Du grec autos, soi-même, et nomos, la loi : se donner à soi-même sa propre loi.",
        "{-aut}{-tab_gla}{forc}Mais Rousseau écrit aussi une phrase qui a fait frémir ses lecteurs : celui qui refuse d'obéir "
        "à la volonté générale y sera contraint par tout le corps.",
        "{-forc}",
        ("C", "Ce qui ne signifie autre chose sinon qu'on le forcera d'être libre.", "c_for"),
        "{-c_for}{-forc}{dang}Forcé d'être libre ? Pour Rousseau, c'est logique : la loi exprime ce que je veux vraiment. "
        "{dang.1}Mais qui décide de ce que je veux vraiment ? {dang.2}Tous les régimes autoritaires ont prétendu savoir mieux que leurs sujets ce qui les libère.",
        ("P", 0.6),
    ], vis={
        "rousseau": dict(type="portrait", annee=1712, legende="Du contrat social (1762)", img="rousseau",
                         nom="Jean-Jacques Rousseau", dates="1712 – 1778", x=110, y=120, w=330, h=420),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.2, .5, .5],
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "c_fer": dict(type="cit", a="Rousseau", o="Du contrat social, I, 1 (1762)", x=640, y=190, w=570),
        "c_ass": dict(type="cit", a="Rousseau", o="Du contrat social, I, 6 (1762)", x=640, y=130, w=570),
        "tab_gla": dict(type="tableau", img="t5-glaris", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="La Landsgemeinde de Glaris, assemblée des citoyens à main levée, 2009 (photo Marc Schlumpf, CC BY-SA 3.0)"),
        "vg": dict(type="liste", cles=["peuple", "générale", "auteur"], titre="Le contrat social", items=[
            "Le peuple vote lui-même ses lois : la volonté générale",
            "J'obéis à la loi dont je suis l'auteur : je n'obéis qu'à moi-même"], x=170, y=120, w=940),
        "c_obe": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=170, y=380, w=940),
        "aut": dict(type="def", cles=["autonomie", "loi"], terme="L'autonomie",
                    t="Se donner à soi-même sa propre loi.", etape="Du grec autos, « soi-même », et nomos, « la loi ».",
                    x=170, y=200, w=940),
        "forc": dict(type="mot", t="« Forcé d'être libre »", g="le paradoxe le plus discuté du Contrat social",
                     y=100, taille=72),
        "c_for": dict(type="cit", a="Rousseau", o="Du contrat social, I, 7 (1762)", x=170, y=270, w=940),
        "dang": dict(type="liste", titre="Le danger", items=[
            "Qui décide de ce que je veux « vraiment » ?",
            "Les régimes autoritaires prétendent savoir mieux que leurs sujets ce qui les libère"],
                     marques=["?", "!"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ IV. anciens et modernes
    dict(id="modernes", chap="La liberté des Anciens et des Modernes", fond="nuit", humeur="calme", notions=["l'État"],
         retenir="Constant : liberté des Anciens (participer au pouvoir) ≠ liberté des Modernes (indépendance privée).", beats=[
        "{constant}{tab_per}En 1819, à Paris, Benjamin Constant prononce un discours resté célèbre. "
        "Il y montre que le mot liberté n'a pas le même sens pour les Anciens et pour nous.",
        "{-constant}{am}{am.g}Pour un citoyen d'Athènes, être libre, c'est participer au pouvoir : voter, débattre sur l'agora, juger. "
        "Mais dans sa vie privée, la cité peut tout contrôler, jusqu'à l'exiler par un vote. "
        "Socrate lui-même, citoyen d'Athènes, fut condamné à mort par un tribunal populaire, en 399 avant notre ère, pour ses idées.",
        "{-tab_per}{tab_sta}{am.d}Pour un moderne, être libre, c'est d'abord être tranquille chez soi : penser, travailler, croire, "
        "aller et venir sans rendre de comptes. Nous déléguons le pouvoir à des représentants. "
        "Quand tu choisis {#la religion}ta religion, ton métier, tes amis, sans que l'État s'en mêle, tu vis la liberté des Modernes.",
        "{-am}",
        ("C", "Le but des modernes est la sécurité dans les jouissances privées ; et ils nomment liberté les garanties "
              "accordées par les institutions à ces jouissances.", "c_con"),
        "{-c_con}{-am}{risq}Mais Constant voit le piège. {risq.1}À force de ne s'occuper que de nos affaires privées, "
        "{risq.2}nous risquons de laisser le pouvoir à d'autres… {risq.3}et de perdre jusqu'à notre indépendance.",
        ("Il faut donc combiner les deux libertés, et non choisir l'une contre l'autre.", {"rate": "-4%"}),
        "{-risq}{-tab_sta}",
        ("P", 0.4),
    ], vis={
        "constant": dict(type="portrait", annee=1767, legende="De la liberté des Anciens comparée à celle des Modernes (1819)",
                         img="constant", nom="Benjamin Constant", dates="1767 – 1830", x=110, y=120, w=330, h=420),
        "tab_per": dict(type="tableau", img="t-pericles", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .62, .4],
                        legende="Philipp von Foltz, Périclès parlant aux Athéniens, 1852 (photographie, Rijksmuseum)"),
        "am": dict(type="cols", g="Liberté des Anciens", gq="participer au pouvoir · la vie privée contrôlée",
                   d="Liberté des Modernes", dq="l'indépendance privée · le pouvoir délégué", vs="≠"),
        "tab_sta": dict(type="tableau", img="t5-statue", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .45, .3],
                        legende="Edward Moran, L'Inauguration de la statue de la Liberté, 1886"),
        "c_con": dict(type="cit", a="Benjamin Constant", o="De la liberté des Anciens comparée à celle des Modernes (1819)",
                      x=170, y=170, w=940),
        "risq": dict(type="liste", titre="Le piège des Modernes", items=[
            "Ne s'occuper que de ses affaires privées", "Laisser le pouvoir à d'autres",
            "Perdre jusqu'à son indépendance"], marques=["1", "2", "→"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ V. les limites du pouvoir
    dict(id="limites", chap="Jusqu'où la société peut-elle aller ?", fond="aube", humeur="tension", notions=["l'État", "la justice"],
         retenir="Mill : seul le tort fait à autrui justifie de limiter ma liberté. Tocqueville : gare à la tyrannie de la majorité.", beats=[
        "{mill}Reste une question très concrète : jusqu'où la société peut-elle limiter ma liberté ? "
        "En 1859, le philosophe anglais John Stuart Mill y répond dans un livre intitulé, tout simplement, De la liberté.",
        "{nuis}Sa réponse tient en un principe : {nuis.1}la seule raison légitime d'user de la contrainte contre quelqu'un, "
        "c'est de l'empêcher de nuire aux autres. {nuis.2}Pour son propre bien ? Ce n'est jamais une raison suffisante.",
        "Concrètement : la société peut t'informer des dangers du tabac, te conseiller, te mettre en garde. "
        "Mais tant que tu ne nuis qu'à toi-même, elle n'a pas à décider à ta place. "
        "En revanche, elle peut t'interdire d'enfumer les autres.",
        "{-nuis}",
        ("C", "Sur lui-même, sur son corps et son esprit, l'individu est souverain.", "c_mil"),
        "{-c_mil}{-nuis}{-mill}{tab_ddhc2}Tu reconnais l'esprit de l'article quatre de la Déclaration, vu dans l'épisode un : "
        "pouvoir faire tout ce qui ne nuit pas à autrui. Mill y ajoute une exigence forte : la liberté de penser et de s'exprimer, "
        "même pour les opinions qui nous choquent. Car on ne sait jamais d'avance laquelle est {#la vérité}vraie. "
        "Et même une opinion fausse a son utilité : en la combattant, nous comprenons mieux pourquoi la vérité est vraie.",
        "{-tab_ddhc2}{toc}{tab_sta2}Mais un danger nouveau guette les démocraties. Alexis de Tocqueville l'a vu en voyageant en Amérique. "
        "Quand c'est la majorité qui gouverne, qui protège la minorité ?",
        "Il l'appelle {!tyrannie}la tyrannie de la majorité. Elle ne met personne en prison ; elle exerce une pression sur les esprits, "
        "et chacun finit par penser comme tout le monde.",
        ("C", "Je ne connais pas de pays où il règne, en général, moins d'indépendance d'esprit et de véritable liberté de discussion "
              "qu'en Amérique.", "c_toc"),
        "{-c_toc}{-toc}{-tab_sta2}{tab_tok}Pense aux réseaux sociaux, à la peur d'être différent, aux opinions qu'on n'ose plus dire. "
        "Tocqueville écrivait en 1835… et il parle de nous.",
        "{-tab_tok}{ber}Pour finir, un outil précieux pour tes copies. {ber.g}Au vingtième siècle, Isaiah Berlin distingue deux concepts de liberté. "
        "La liberté négative : qu'on me laisse faire. C'est Hobbes, c'est Mill. "
        "{ber.d}Et la liberté positive : être maître de soi, se gouverner soi-même. C'est Rousseau.",
        ("Les deux sont précieuses. Et chacune, poussée seule, a ses dangers.", {"rate": "-5%"}),
        ("P", 0.6),
    ], vis={
        "mill": dict(type="portrait", annee=1806, legende="De la liberté (1859)", img="mill", nom="John Stuart Mill",
                     dates="1806 – 1873", x=110, y=120, w=330, h=420),
        "nuis": dict(type="liste", cles=["nuire", "propre"], titre="Le principe de non-nuisance", items=[
            "Seule raison légitime de contraindre : empêcher de nuire aux autres",
            "« Pour son propre bien » ne suffit jamais"], marques=["✓", "✗"], x=640, y=130, w=570),
        "c_mil": dict(type="cit", a="John Stuart Mill", o="De la liberté, chap. I (1859)", para=True, x=640, y=360, w=570),
        "tab_ddhc2": dict(type="tableau", img="t-ddhc", fond=True, sombre=True, de=[1.2, .5, .45], a=[1.0, .5, .5],
                          legende="Jean-Jacques-François Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "toc": dict(type="portrait", annee=1805, legende="De la démocratie en Amérique (1835-1840)", img="tocqueville",
                    nom="Alexis de Tocqueville", dates="1805 – 1859", x=110, y=120, w=330, h=420),
        "tab_sta2": dict(type="tableau", img="t5-statue", fond=True, sombre=True, de=[1.3, .45, .3], a=[1.0, .5, .5],
                         legende="Edward Moran, L'Inauguration de la statue de la Liberté, 1886"),
        "c_toc": dict(type="cit", a="Tocqueville", o="De la démocratie en Amérique, I, II, 7 (1835)", x=640, y=150, w=570),
        "tab_tok": dict(type="tableau", img="t-tokyo", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Tokyo, carrefour de Shibuya (photo Benh Lieu Song, CC BY-SA 2.0)"),
        "ber": dict(type="cols", g="Liberté négative", gq="qu'on me laisse faire · Hobbes, Mill", d="Liberté positive",
                    dq="me gouverner moi-même · Rousseau", vs="≠", plus=True,
                    repere="Isaiah Berlin, Deux concepts de liberté (1958)"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Faisons le point. {rec.1}Hobbes : sans État, la liberté de tous mène à la guerre ; on l'échange contre la sécurité.",
        "{rec.2}Locke et Montesquieu : la loi ne détruit pas la liberté, elle la protège. Et le pouvoir doit arrêter le pouvoir.",
        "{rec.3}Rousseau : obéir à la loi qu'on s'est donnée, c'est être autonome. Mais gare au « forcé d'être libre ».",
        "{rec.4}Constant, Mill, Tocqueville : protéger l'individu, y compris contre la majorité.",
        "Et remarque le lien avec les épisodes précédents : la liberté politique ne remplace pas la liberté intérieure. "
        "Des droits garantis ne servent à rien à qui reste esclave de ses désirs ; et la sagesse seule ne protège pas du tyran.",
        "Retiens surtout ceci pour ta copie : la loi peut être une contrainte, ou la condition même de la liberté. "
        "Tout dépend de qui la fait, et de ce qu'elle protège.",
        "{-rec}{quiz}À toi de jouer : les questions t'attendent sous la vidéo.",
        ("Et la prochaine fois… nous passerons à la pratique : la liberté à l'épreuve du bac.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-quiz}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LIBRES ENSEMBLE", branches=[
            dict(t="Hobbes", items=["l'état de nature : la guerre", "le pacte : liberté contre sécurité",
                                    "liberté = silence de la loi"]),
            dict(t="Locke, Montesquieu", items=["pas de loi, pas de liberté", "le droit de faire ce que les lois permettent",
                                                "le pouvoir arrête le pouvoir"]),
            dict(t="Rousseau", items=["la volonté générale", "l'autonomie", "« forcé d'être libre »"]),
            dict(t="Protéger l'individu", items=["Constant : Anciens / Modernes", "Mill : ne pas nuire",
                                                 "Tocqueville : tyrannie de la majorité"])]),
        "quiz": dict(type="mot", t="À toi de jouer", g="les questions t'attendent sous la vidéo", y=260, taille=84),
        "tab_fin": dict(type="tableau", img="t-liberte-peuple", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .35],
                        legende="Eugène Delacroix, La Liberté guidant le peuple, 1830"),
        "fin": dict(type="titre", sur="À suivre", t="La liberté à l'épreuve du bac", sous="Épisode 6 · Sujets, plans, pièges"),
    }),
]

QUIZ = [
    dict(q="Pourquoi, selon Hobbes, les hommes sortent-ils de l'état de nature ?",
         r=["Pour devenir plus libres", "Pour échapper à la guerre de chacun contre chacun, en échange de leur liberté naturelle",
            "Parce que Dieu le leur ordonne", "Pour pouvoir voter les lois"], ok=1,
         voir="pacte", ex="Léviathan : la vie à l'état de nature est « solitaire, besogneuse, pénible, quasi animale, et brève ». Le pacte échange la liberté contre la sécurité."),
    dict(q="« Là où il n'y a pas de loi, il n'y a pas de liberté. » Qui l'écrit ?",
         r=["Hobbes", "Locke", "Rousseau", "Mill"], ok=1,
         voir="c_loc", ex="Locke, Second Traité (1690) : la loi protège de l'arbitraire. La liberté n'est pas la licence."),
    dict(q="Pour Montesquieu, la liberté, c'est…",
         r=["faire tout ce que l'on veut", "le droit de faire tout ce que les lois permettent", "participer au pouvoir",
            "obéir au souverain"], ok=1,
         voir="c_mon", ex="De l'esprit des lois, XI, 3 : si je pouvais faire ce que les lois défendent, les autres le pourraient aussi."),
    dict(q="À quoi sert la séparation des pouvoirs ?",
         r=["À rendre l'État plus rapide", "À empêcher l'abus de pouvoir : le pouvoir arrête le pouvoir",
            "À supprimer les lois", "À donner tout le pouvoir au peuple"], ok=1,
         voir="sep", ex="Législatif, exécutif, judiciaire : jamais les mêmes mains. La DDHC (art. 16) en fait une condition de toute constitution."),
    dict(q="Qu'est-ce que l'autonomie, au sens de Rousseau ?",
         r=["Vivre seul, sans les autres", "Se donner à soi-même sa propre loi", "Faire ce que l'on désire",
            "Ne rencontrer aucun obstacle"], ok=1,
         voir="aut", ex="« L'obéissance à la loi qu'on s'est prescrite est liberté » (Contrat social, I, 8)."),
    dict(q="La « liberté des Modernes », selon Constant, c'est surtout…",
         r=["participer directement au pouvoir", "l'indépendance de la vie privée, garantie par les institutions",
            "l'absence de toute loi", "la liberté intérieure du sage"], ok=1,
         voir="am", ex="Pour les Anciens, être libre, c'est participer au pouvoir ; pour les Modernes, c'est être tranquille dans sa vie privée."),
    dict(q="Le principe de Mill autorise à limiter la liberté de quelqu'un…",
         r=["pour son propre bien", "pour l'empêcher de nuire aux autres", "quand la majorité le veut",
            "quand ses opinions choquent"], ok=1,
         voir="nuis", ex="De la liberté (1859) : sur lui-même, l'individu est souverain. Seul le tort fait à autrui justifie la contrainte."),
    dict(q="Que désigne la « tyrannie de la majorité » chez Tocqueville ?",
         r=["Un coup d'État militaire", "La pression de l'opinion majoritaire sur les esprits et les minorités",
            "Le pouvoir d'un roi absolu", "La séparation des pouvoirs"], ok=1,
         voir="c_toc", ex="La démocratie peut opprimer sans prison : par le conformisme. D'où l'importance de protéger les minorités."),
]

CREDITS = [
    "Hobbes : John Michael Wright, vers 1669-1670 ; Rousseau : Maurice Quentin de La Tour, 1753",
    "Locke : Godfrey Kneller, 1697 (Ermitage) ; Montesquieu : gravure (Rijksmuseum, CC0) ; Benjamin Constant : Lina Vallier ; John Stuart Mill : G. F. Watts, 1873 ; Tocqueville : Théodore Chassériau, 1850",
    "Tableaux et gravures : N. C. Wyeth, Robinson Crusoé (1920) ; Thomas Cole, L'État sauvage (1834) ; Abraham Bosse, frontispice du Léviathan (1651) ; Locke, Two Treatises (1690, Library of Congress) ; Montesquieu, De l'esprit des lois (1748) ; Du contrat social (1762) ; J.-J.-F. Le Barbier, Déclaration des droits de l'homme et du citoyen (1789) ; P. von Foltz, Périclès (1852, Rijksmuseum) ; E. Moran, L'Inauguration de la statue de la Liberté (1886) ; E. Delacroix, La Liberté guidant le peuple (1830) : domaine public",
    "Photographies : hémicycle de l'Assemblée nationale (Coucouoeuf, CC BY-SA 3.0) ; Landsgemeinde de Glaris (Marc Schlumpf, CC BY-SA 3.0) ; Shibuya (Benh Lieu Song, CC BY-SA 2.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
