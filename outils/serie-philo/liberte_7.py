"""La liberté, épisode 7 : « Récap »

Texte lu (beats) et visuels de chaque scène ; même format que liberte_1.py (voir son en-tête).
L'essentiel de la série pour la veille de l'épreuve : les trois libertés et les repères, les thèses de chaque épisode,
les citations à savoir par cœur, les exemples qui marchent, une carte mentale et une frise des auteurs.
"""

CODE = "liberte-7"
NOTION = "La liberté"
NUM = 7
TITRE = "Récap"
SUIVANT = ""

PRONONCIATION = {"Nietzsche": "Nitche", "Libet": "Libette", "Sapere": "Sapéré", "aude": "aoudé", "Stockdale": "Stokdèle",
                 "Tocqueville": "Tokvil", "Durkheim": "Durkème",
                 "Isaiah Berlin": "Isaïa Berline"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="calme", carton=False, beats=[
        "{tab_vei}{q_veil}C'est la veille de l'épreuve. Tu n'as plus le temps de tout relire. "
        "Alors, en quelques minutes, reprenons ensemble l'essentiel de la série : les idées, les auteurs, "
        "les citations et les exemples qui font une bonne copie.",
        ("Prêt ? On y va.", {"rate": "-4%", "pitch": "+2Hz"}),
        ("P", 0.3),
        "{-q_veil}{-tab_vei}{titre}",
        ("P", 3.0),
    ], vis={
        "tab_vei": dict(type="tableau", img="t7-veille", fond=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Matthias Stom, Jeune homme lisant à la chandelle, v. 1630-1640"),
        "q_veil": dict(type="question", t="Que faut-il savoir, la veille de l'épreuve ?"),
        "titre": dict(type="titre", sur="La liberté · Épisode 7", t="Récap",
                      sous="L'essentiel de la série, pour la veille de l'épreuve"),
    }),

    # ------------------------------------------------------------------ I. les fondations
    dict(id="bases", chap="Les fondations", fond="aube", humeur="lumiere",
         retenir="Le premier réflexe : de quelle liberté parle le sujet ? D'agir, de vouloir, ou politique ?", beats=[
        "{arist}{tab_ath}D'abord, le sens premier. Pour Aristote, l'homme libre est celui qui est à lui-même sa propre fin : "
        "il n'est l'instrument de personne. Le contraire de l'homme libre, c'est l'esclave.",
        "{-arist}{-tab_ath}{cartes}Ensuite, la clé de toute la notion : il y a trois libertés. "
        "{cartes.1}La liberté d'agir : puis-je faire ce que j'ai décidé ? "
        "{cartes.2}Le libre arbitre : aurais-je pu vouloir autre chose ? "
        "{cartes.3}La liberté politique : que me garantit la société ?",
        "{-cartes}{tab_hie}{epic}Ces trois libertés ne vont pas forcément ensemble. Épictète, esclave, n'avait aucune liberté politique… "
        "et pourtant, il restait maître de lui. À l'inverse, on peut avoir tous les droits et rester esclave de ses habitudes.",
        "{-epic}{-tab_hie}{tab_dan}{fv}Et une distinction qui sauve des copies : {fv.g}faire ce que je veux, {fv.d}ce n'est pas vouloir librement. "
        "Pour Hobbes, être libre, c'est ne rencontrer aucun obstacle, comme l'eau qu'on libère de son vase. Mais Platon répond avec les tonneaux percés : "
        "celui qui suit tous ses désirs en est l'esclave.",
        "{-fv}{-tab_dan}{tab_dor}{rep}Enfin, les repères à placer. {rep.1}Contrainte et obligation : le mur me contraint, "
        "le feu rouge m'oblige ; l'obligation suppose que je sois libre de désobéir. "
        "{rep.2}Nécessaire et contingent : si tout est nécessaire, le libre arbitre semble une illusion. "
        "{rep.3}En droit et en fait : une liberté écrite dans la loi n'est pas toujours une liberté réelle. "
        "Souviens-toi d'Anatole France : la loi interdit au riche comme au pauvre de coucher sous les ponts.",
        ("P", 0.4),
    ], vis={
        "arist": dict(type="portrait", annee=-384, img="aristote", nom="Aristote", dates="384 – 322 av. J.-C.",
                      legende="Métaphysique · Politique", x=110, y=120, w=330, h=420),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.5, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511"),
        "cartes": dict(type="cartes", items=[
            dict(ic="porte", t="Liberté d'agir", q="Puis-je faire ce que j'ai décidé ?"),
            dict(ic="chemins", t="Libre arbitre", q="Aurais-je pu vouloir autre chose ?"),
            dict(ic="colonnes", t="Liberté politique", q="Que me garantit la société ?")]),
        "fv": dict(type="cols", g="Faire ce que je veux", gq="Hobbes : l'absence d'obstacles",
                   d="Vouloir librement", dq="Platon : l'esclave de ses désirs", vs="≠"),
        "tab_hie": dict(type="tableau", img="t-hierapolis", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.0, .7, .5],
                        legende="Hiérapolis, en Phrygie, ville natale d'Épictète (photo Bernard Gagnon, CC BY-SA 3.0)"),
        "epic": dict(type="portrait", annee=50, img="epictete", nom="Épictète", dates="v. 50 – v. 130",
                     legende="esclave, et maître de lui", x=110, y=120, w=330, h=420),
        "tab_dan": dict(type="tableau", img="t-danaides", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.25, .5, .6],
                        legende="John William Waterhouse, Les Danaïdes, 1906"),
        "tab_dor": dict(type="tableau", img="t-dore", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Gustave Doré, Londres vu du chemin de fer, 1872"),
        "rep": dict(type="liste", titre="Les repères", items=[
            "Contrainte / obligation : le mur et le feu rouge", "Nécessaire / contingent",
            "En droit / en fait : libertés formelles et réelles"], marques=["✻", "✻", "✻"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ II. le grand débat
    dict(id="debat", chap="Le grand débat", fond="nuit", humeur="tension",
         retenir="Déterminisme ≠ fatalisme : connaître ce qui nous détermine, c'est le premier pas vers la liberté.", beats=[
        "{tab_chr}{deb}Le cœur du sujet, c'est un débat. {deb.g}D'un côté, ceux qui affirment notre liberté. "
        "Descartes : ma volonté est infinie, et l'indifférence n'est que le plus bas degré de la liberté. "
        "Sartre : l'existence précède l'essence ; je suis ce que je fais.",
        "{-deb}",
        ("C", "L'homme est condamné à être libre.", "c_sar"),
        "{-c_sar}{deb.d}De l'autre, les soupçons. Spinoza : la pierre lancée, si elle pouvait penser, se croirait libre.",
        "{-deb}",
        ("C", "Telle est cette liberté humaine que tous se vantent de posséder et qui consiste en cela seul que les hommes "
              "sont conscients de leurs désirs et ignorants des causes qui les déterminent.", "c_spi"),
        "{-c_spi}{-deb}{freud}Freud ajoute l'inconscient : lapsus, rêves, actes manqués.",
        ("C", "Le moi n'est pas maître dans sa propre maison.", "c_fre"),
        "{-freud}{-c_fre}{soup}{soup.1}Marx, Durkheim, Bourdieu : la société pense en nous, jusque dans nos goûts. "
        "{soup.2}Libet, en neurosciences : le cerveau semble se préparer avant que nous ayons conscience de vouloir… "
        "mais il nous laisse le temps de dire non. "
        "{soup.3}Et Nietzsche soupçonne qu'on a déclaré les hommes libres pour pouvoir les juger et les punir.",
        "{-soup}{-tab_chr}{rep_det}La réponse à retenir : {rep_det.1}déterminisme ne veut pas dire fatalisme. "
        "{rep_det.2}Connaître ce qui nous détermine, ce n'est pas se résigner : c'est le premier pas pour s'en libérer.",
        ("P", 0.4),
    ], vis={
        "tab_chr": dict(type="tableau", img="t-christine", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .55],
                        legende="Nils Forsberg, Descartes à la cour de la reine Christine (d'après P.-L. Dumesnil), XIXᵉ siècle"),
        "deb": dict(type="cols", g="Nous sommes libres", gq="Descartes · Sartre (épisode 2)",
                    d="Une illusion ?", dq="Spinoza · Freud · Marx · Bourdieu · Libet (épisode 3)", vs="VS"),
        "c_sar": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=170, y=230, w=940),
        "c_spi": dict(type="cit", a="Spinoza", o="Lettre 58 à Schuller, octobre 1674 (trad. Appuhn)", x=170, y=170, w=940),
        "freud": dict(type="portrait", annee=1856, img="freud", nom="Sigmund Freud", dates="1856 – 1939",
                      legende="l'inconscient", x=110, y=120, w=330, h=420),
        "c_fre": dict(type="cit", a="Freud", o="Une difficulté de la psychanalyse (1917 ; trad. 1933)", x=640, y=200, w=570),
        "soup": dict(type="liste", titre="D'autres soupçons (épisode 3)", items=[
            "Marx, Durkheim, Bourdieu : la société pense en nous", "Libet : le cerveau prépare le geste… mais on peut dire non",
            "Nietzsche : déclarés libres pour être jugés et punis"], marques=["1", "2", "3"], x=170, y=160, w=940),
        "rep_det": dict(type="def", cles=["fatalisme", "libérer"], terme="Déterminisme ≠ fatalisme",
                        t="Tout a une cause… mais connaître les causes permet d'agir sur elles.",
                        etape="Connaître ses déterminismes : le premier pas vers la libération.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. se libérer
    dict(id="liberer", chap="Se libérer", fond="aube", humeur="calme",
         retenir="On ne naît pas libre, on le devient : par le jugement, la connaissance, la loi qu'on se donne.", beats=[
        "{tab_mar}{lib}Troisième idée : la liberté se conquiert. {lib.1}Les stoïciens : distinguer ce qui dépend de nous "
        "de ce qui n'en dépend pas. Épictète, esclave, reste maître de son jugement. "
        "{lib.2}Spinoza : comprendre la nécessité, c'est se libérer de la servitude des passions ; "
        "une passion cesse d'en être une dès que nous en formons une idée claire. "
        "{lib.3}Rousseau et Kant : être libre, c'est obéir à la loi qu'on se donne. C'est l'autonomie.",
        "{-lib}",
        ("C", "L'impulsion du seul appétit est esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.", "c_rou"),
        "{-c_rou}{-lib}{-tab_mar}{tab_gib}{kant}Et la formule de Kant : tu dois, donc tu peux. L'homme menacé du gibet "
        "découvre, dans le devoir, qu'il pourrait refuser le faux témoignage. Le devoir lui révèle sa liberté.",
        ("C", "Sapere aude ! Aie le courage de te servir de ton propre entendement.", "c_sap"),
        "{-c_sap}{-kant}{-tab_gib}{tab_nuit}{heg}Et pour aller plus loin, Hegel : la liberté ne se gagne pas seulement en soi-même. "
        "Elle se réalise dans l'histoire, d'un seul homme libre, le despote, à tous les hommes.",
        ("P", 0.4),
    ], vis={
        "tab_mar": dict(type="tableau", img="t4-marc-aurele", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .55, .3],
                        legende="Statue équestre de Marc Aurèle, Capitole, Rome (photo Jebulon, CC0)"),
        "lib": dict(type="liste", titre="Se libérer (épisode 4)", items=[
            "Les stoïciens : ce qui dépend de nous", "Spinoza : comprendre la nécessité",
            "Rousseau, Kant : l'autonomie"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "c_rou": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=170, y=390, w=940),
        "tab_gib": dict(type="tableau", img="t4-gibet", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .5],
                        legende="Pieter Bruegel l'Ancien, La Pie sur le gibet, 1568"),
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="« Tu dois, donc tu peux »", x=110, y=120, w=330, h=420),
        "c_sap": dict(type="cit", a="Kant", o="Qu'est-ce que les Lumières ? (1784)", x=640, y=200, w=570),
        "tab_nuit": dict(type="tableau", img="t4-napoleon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                         legende="Charles Meynier, Entrée de Napoléon à Berlin, 27 octobre 1806, 1810"),
        "heg": dict(type="mot", t="Hegel", g="« L'histoire universelle est le progrès dans la conscience de la liberté »",
                    y=240, taille=96),
    }),

    # ------------------------------------------------------------------ IV. libres ensemble
    dict(id="ensemble", chap="Libres ensemble", fond="nuit", humeur="tension",
         retenir="La loi n'est pas l'ennemie de la liberté : elle la protège, à condition d'être juste et limitée.", beats=[
        "{tab_bas}{pol}Quatrième idée : la liberté politique. {pol.1}Hobbes : sans État, c'est la guerre de tous contre tous ; "
        "on cède sa liberté naturelle pour la sécurité. {pol.2}Locke : là où il n'y a pas de loi, il n'y a pas de liberté. "
        "{pol.3}Rousseau : le peuple n'est libre que s'il obéit aux lois qu'il se donne.",
        "{-pol}{-tab_bas}{tab_ddhc}La Déclaration de 1789 l'avait dit à sa manière.",
        ("C", "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui.", "c_ddhc"),
        "{-c_ddhc}{-tab_ddhc}{tab_bas2}{pol2}Et Montesquieu le précise.",
        "{-pol2}",
        ("C", "La liberté est le droit de faire tout ce que les lois permettent.", "c_mon"),
        "{-c_mon}{-pol2}{polb}{polb.1}Mais la loi peut aussi menacer la liberté. Benjamin Constant distingue la liberté des Anciens, "
        "participer au pouvoir, et celle des Modernes, l'indépendance de la vie privée. "
        "{polb.2}John Stuart Mill pose une limite : on ne peut contraindre quelqu'un que pour l'empêcher de nuire aux autres. "
        "{polb.3}Et Tocqueville met en garde contre la tyrannie de la majorité.",
        "{-polb}{-tab_bas2}{ber}Pour aller plus loin, Isaiah Berlin résume tout le débat en deux mots. {ber.g}La liberté négative : "
        "qu'on me laisse faire. {ber.d}La liberté positive : être maître de sa vie, participer aux décisions.",
        ("P", 0.4),
    ], vis={
        "tab_bas": dict(type="tableau", img="t-bastille", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .45],
                        legende="Jean-Pierre Houël, La Prise de la Bastille, 1789"),
        "pol": dict(type="liste", titre="Libres ensemble (épisode 5)", items=[
            "Hobbes : l'État contre la guerre de tous contre tous", "Locke : pas de liberté sans loi",
            "Rousseau : obéir aux lois qu'on se donne"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "polb": dict(type="liste", titre="Quand la loi menace la liberté", items=[
            "Constant : liberté des Anciens / des Modernes", "Mill : ne contraindre que pour empêcher de nuire",
            "Tocqueville : la tyrannie de la majorité"], marques=["4", "5", "6"], x=170, y=150, w=940),
        "ber": dict(type="cols", g="Liberté négative", gq="qu'on me laisse faire : l'absence d'ingérence",
                    d="Liberté positive", dq="être maître de sa vie, participer au pouvoir", vs="≠", plus=True),
        "tab_ddhc": dict(type="tableau", img="t-ddhc", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                         legende="Jean-Jacques-François Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "c_ddhc": dict(type="cit", a="Déclaration des droits de l'homme et du citoyen", o="article 4, 26 août 1789",
                       x=170, y=190, w=940),
        "tab_bas2": dict(type="tableau", img="t-bastille", fond=True, sombre=True, de=[1.3, .4, .45], a=[1.0, .5, .5],
                         legende="Jean-Pierre Houël, La Prise de la Bastille, 1789"),
        "pol2": dict(type="mot", t="Montesquieu", g="De l'esprit des lois (1748)", y=150, taille=72),
        "c_mon": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 3 (1748)", x=170, y=470, w=940),
    }),

    # ------------------------------------------------------------------ V. le jour J
    dict(id="copie", chap="Le jour J", fond="aube", humeur="lumiere",
         retenir="Définir, distinguer, problématiser, illustrer : une idée, un auteur, un exemple précis.", beats=[
        "{tab_exa}{meth}Et le jour de l'épreuve ? Quatre gestes. {meth.1}Définir chaque mot du sujet, et repérer ce qu'il présuppose. "
        "{meth.2}Te demander de quelle liberté il parle. {meth.3}Faire apparaître une tension : deux réponses "
        "qui semblent toutes les deux vraies. {meth.4}Construire : la réponse spontanée, l'objection, "
        "puis une distinction qui dépasse les deux. Et pour une explication de texte : six éléments d'introduction, "
        "puis, pour chaque phrase, quoi ? comment ? pourquoi ?",
        "{-meth}{suj}Les grands sujets reviennent : {suj.1}Être libre, est-ce faire ce que l'on veut ? "
        "{suj.2}La liberté est-elle une illusion ? {suj.3}L'État est-il l'ennemi de la liberté ? "
        "{suj.4}Peut-on être libre sans les autres ? Pour chacun, tu as maintenant deux camps et des auteurs.",
        "{-suj}{ex}Les exemples qui marchent, tu les as : {ex.1}la jambe d'Épictète. {ex.2}Les tonneaux percés de Platon. "
        "{ex.3}Le garçon de café de Sartre. {ex.4}La pierre de Spinoza. {ex.5}Le gibet de Kant. "
        "{ex.6}Robinson sur son île, qui survit grâce aux savoirs des autres. "
        "{ex.7}Et James Stockdale, qui tient sept ans en prison grâce à Épictète. Un exemple travaillé vaut mieux que dix citations.",
        "{-ex}{-tab_exa}{piege}Un dernier piège à éviter : {piege.1}réciter des auteurs sans répondre à la question. "
        "{piege.2}Un auteur n'est pas un argument d'autorité : c'est un outil pour penser le sujet.",
        ("P", 0.4),
    ], vis={
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "meth": dict(type="liste", titre="Le jour de l'épreuve", items=[
            "Définir chaque mot, repérer le présupposé", "De quelle liberté parle-t-on ?", "Faire apparaître une tension",
            "Réponse spontanée → objection → distinction qui dépasse"], marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "suj": dict(type="liste", titre="Des sujets qui reviennent", items=[
            "Être libre, est-ce faire ce que l'on veut ?", "La liberté est-elle une illusion ?",
            "L'État est-il l'ennemi de la liberté ?", "Peut-on être libre sans les autres ?"], marques=["?", "?", "?", "?"],
                    x=170, y=140, w=940),
        "ex": dict(type="nuage", items=["la jambe d'Épictète", "les tonneaux percés", "le garçon de café",
                                        "la pierre de Spinoza", "le gibet de Kant", "Robinson", "Stockdale"], centre="EXEMPLES"),
        "piege": dict(type="note", titre="Le piège", cles=["réciter", "outil"],
                      t="Réciter des auteurs sans répondre à la question.",
                      etape="Un auteur n'est pas un argument d'autorité : c'est un outil pour penser le sujet.",
                      x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VI. la carte et la frise
    dict(id="fin", chap="Toute la notion", fond="nuit", humeur="lumiere", beats=[
        "{rec}Voici toute la notion, sur une seule carte. {rec.1}Le sens premier et les trois libertés. "
        "{rec.2}Le débat : libres, ou déterminés ? {rec.3}La libération : par le jugement, la connaissance, l'autonomie. "
        "{rec.4}Et la liberté politique : l'État, la loi, les autres.",
        "{-rec}{frise}Et voici ceux qui t'ont accompagné, d'Athènes à Paris : vingt-cinq siècles de pensée.",
        "{-frise}{trois}Si tu ne dois garder que trois phrases : {trois.1}Rousseau, l'obéissance à la loi qu'on s'est prescrite est liberté. "
        "{trois.2}Sartre, l'homme est condamné à être libre. {trois.3}Et Kant : aie le courage de te servir de ton propre entendement.",
        ("Un dernier mot. La liberté n'est pas seulement un sujet de dissertation. C'est une question que tu te poses "
         "chaque fois que tu choisis, que tu refuses, que tu penses par toi-même.", {"rate": "-5%"}),
        ("Demain, devant ta copie, ce sera exactement cela. Bonne chance.", {"rate": "-6%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-trois}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LA LIBERTÉ", branches=[
            dict(t="Les fondations", items=["Aristote : s'appartenir", "agir · vouloir · politique", "faire ≠ vouloir"]),
            dict(t="Le débat", items=["Descartes, Sartre : libres", "Spinoza, Freud, Marx : déterminés", "déterminisme ≠ fatalisme"]),
            dict(t="Se libérer", items=["stoïciens : ce qui dépend de nous", "Spinoza : comprendre", "Rousseau, Kant : autonomie"]),
            dict(t="Libres ensemble", items=["Hobbes, Locke, Rousseau", "Montesquieu, Constant, Mill", "Tocqueville : la majorité"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Platon", d=-428, img="platon"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Épictète", d=50, img="epictete"), dict(nom="Descartes", d=1596, img="descartes"),
            dict(nom="Hobbes", d=1588, img="hobbes"), dict(nom="Spinoza", d=1632, img="spinoza"),
            dict(nom="Montesquieu", d=1689, img="montesquieu"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Hegel", d=1770, img="hegel"), dict(nom="Marx", d=1818, img="marx"),
            dict(nom="Mill", d=1806, img="mill"), dict(nom="Nietzsche", d=1844, img="nietzsche"),
            dict(nom="Freud", d=1856, img="freud"),
            dict(nom="Sartre", d=1905, img="sartre")]),
        "trois": dict(type="liste", titre="Trois phrases à garder", items=[
            "« L'obéissance à la loi qu'on s'est prescrite est liberté » · Rousseau",
            "« L'homme est condamné à être libre » · Sartre", "« Sapere aude ! » · Kant"], marques=["1", "2", "3"],
                      x=170, y=170, w=940),
        "tab_fin": dict(type="tableau", img="t-liberte-peuple", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .35],
                        legende="Eugène Delacroix, La Liberté guidant le peuple, 1830"),
        "fin": dict(type="titre", sur="La liberté", t="Fin de la série", sous="Six épisodes et un récap · bonne épreuve !"),
    }),
]

QUIZ = [
    dict(q="« Aurais-je pu vouloir autre chose ? » De quelle liberté parle-t-on ?",
         r=["La liberté d'agir", "Le libre arbitre", "La liberté politique", "La liberté négative"], ok=1, voir="cartes",
         ex="C'est la liberté de la volonté, la question métaphysique des épisodes 2 et 3."),
    dict(q="Qui affirme que « l'homme est condamné à être libre » ?",
         r=["Descartes", "Spinoza", "Sartre", "Kant"], ok=2, voir="c_sar",
         ex="Sartre, L'existentialisme est un humanisme (1946) : l'existence précède l'essence."),
    dict(q="Pour Spinoza, d'où vient l'illusion du libre arbitre ?",
         r=["De la loi morale", "De ce que nous sommes conscients de nos désirs et ignorants de leurs causes",
            "De l'inconscient", "De la société"], ok=1, voir="deb",
         ex="Lettre 58 à Schuller : la pierre lancée qui pourrait penser se croirait libre."),
    dict(q="« Déterminisme » et « fatalisme », c'est…",
         r=["la même chose", "deux idées opposées : le déterminisme permet d'agir sur les causes",
            "deux noms de la liberté", "deux thèses de Sartre"], ok=1, voir="rep_det",
         ex="Le fatalisme dit : quoi que je fasse, ce sera. Le déterminisme dit : tout a une cause, que je peux connaître et utiliser."),
    dict(q="Selon Épictète, qu'est-ce qui dépend de nous ?",
         r=["Notre corps", "Notre réputation", "Nos jugements", "Notre richesse"], ok=2, voir="lib",
         ex="Manuel, I : la liberté du sage est intérieure. Exemple : la jambe brisée."),
    dict(q="Pour Rousseau et Kant, la liberté, c'est…",
         r=["faire ce qui me plaît", "obéir à la loi qu'on se donne", "ne rencontrer aucun obstacle", "suivre ses penchants"],
         ok=1, voir="c_rou",
         ex="Du contrat social, I, 8 ; chez Kant, c'est l'autonomie : se donner à soi-même sa loi."),
    dict(q="« La liberté est le droit de faire tout ce que les lois permettent. » Qui l'écrit ?",
         r=["Hobbes", "Montesquieu", "Mill", "Tocqueville"], ok=1, voir="c_mon",
         ex="De l'esprit des lois, XI, 3 (1748) : la loi n'est pas l'ennemie de la liberté."),
    dict(q="Le piège le plus fréquent dans une copie sur la liberté ?",
         r=["Citer un auteur", "Réciter des auteurs sans répondre à la question", "Donner un exemple",
            "Définir les mots du sujet"], ok=1, voir="piege",
         ex="Un auteur est un outil pour penser le sujet, pas un argument d'autorité."),
]

CREDITS = [
    "Portraits : voir les épisodes 1 à 6",
    "Tableaux et photographies : Matthias Stom, Jeune homme lisant à la chandelle (v. 1630-1640) ; Raphaël, L'École d'Athènes ; "
    "N. Forsberg, Descartes et la reine Christine ; Waterhouse, Les Danaïdes (1906) ; Doré, Londres (1872) ; Meynier, Entrée de Napoléon à Berlin (1810) ; Bruegel l'Ancien, La Pie sur le gibet (1568) ; J.-P. Houël, La Prise de la Bastille (1789) ; Le Barbier, Déclaration des droits de l'homme et du citoyen (1789) ; "
    "Delacroix, La Liberté guidant le peuple (1830) : domaine public ; Marc Aurèle, Capitole (Jebulon, CC0) ; Hiérapolis (B. Gagnon, CC BY-SA 3.0) ; salle d'examen (domaine public)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
