"""La liberté, épisode 4 : « Se libérer »

Texte lu (beats) et visuels de chaque scène ; même format que liberte_1.py (voir son en-tête).
On ne naît pas libre, on le devient : les stoïciens, Spinoza, Rousseau et Kant, les Lumières ; Hegel pour aller plus loin.
"""

CODE = "liberte-4"
NOTION = "La liberté"
NUM = 4
TITRE = "Se libérer"
SUIVANT = "Épisode 5 · Libres ensemble : l'État, la loi, la société"

PRONONCIATION = {"Stockdale": "Stokdèle", "Königsberg": "Keunigsberg", "Sapere": "Sapéré", "aude": "aoudé",
                 "Hoa Lo": "Hoa Lô", "nomos": "nomosse", "autos": "autosse"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_hoa}{stock}Septembre 1965. Au-dessus du Viêt Nam, un pilote américain, James Stockdale, est abattu. "
        "Pendant qu'il descend en parachute vers le village où on l'attend, il se murmure une phrase étrange : "
        "je quitte le monde de la technique… j'entre dans le monde d'Épictète.",
        "Stockdale avait lu, à l'université, le Manuel d'Épictète : le petit livre d'un ancien esclave. "
        "Il va en avoir besoin.",
        "{-stock}{-tab_hoa}{tab_cel}Sept ans et demi de captivité, dans la prison de Hoa Lo, à Hanoï. "
        "Les fers aux pieds, la torture, quatre années à l'isolement.",
        ("On lui a tout pris. Son corps, son temps, ses camarades.", {"rate": "-6%", "pitch": "-2Hz"}),
        "Et pourtant, une chose, une seule, lui restait : son jugement. Ce qu'il acceptait. Ce qu'il refusait.",
        "{-tab_cel}{q_ouv}Peut-on être libre… en prison ?",
        ("P", 0.6),
        "{-q_ouv}{voie}Dans les épisodes deux et trois, deux camps se sont affrontés. Pour Descartes et Sartre, "
        "nous sommes libres, absolument. Pour Spinoza et Freud, cette liberté est une illusion. "
        "{voie.1}Aujourd'hui, une troisième voie. Et si la liberté n'était ni un don… ni une illusion ? "
        "{voie.2}Et si c'était une {!conquête}conquête ?",
        ("On ne naît pas libre. On le devient.", {"rate": "-6%"}),
        ("P", 0.3),
        "{-voie}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_hoa": dict(type="tableau", img="t4-hoalo", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Hanoï, entrée de la prison de Hoa Lo, la « Maison centrale » (photo David McKelvey, CC BY 2.0)"),
        "stock": dict(type="portrait", annee=1923, img="stockdale", nom="James Stockdale", dates="1923 – 2005",
                      legende="prisonnier à Hoa Lo, 1965 – 1973", x=110, y=120, w=330, h=420),
        "tab_cel": dict(type="tableau", img="t4-hoalo-cellule", de=[1.0, .5, .5], a=[1.25, .4, .55],
                        legende="Hoa Lo, reconstitution d'une salle de détention, musée de la prison (photo Richard Mortel, CC BY 2.0)"),
        "q_ouv": dict(type="question", t="Peut-on être libre en prison ?"),
        "voie": dict(type="liste", titre="Trois réponses", items=[
            "Descartes, Sartre : nous sommes libres (ép. 2)",
            "Spinoza, Freud : c'est une illusion (ép. 3)",
            "Aujourd'hui : la liberté se conquiert"], marques=["2", "3", "4"], x=170, y=170, w=940),
        "titre": dict(type="titre", sur="La liberté · Épisode 4", t="Se libérer",
                      sous="Les stoïciens, Spinoza, Rousseau, Kant"),
    }),

    # ------------------------------------------------------------------ I. les stoïciens
    dict(id="stoiciens", chap="Ce qui dépend de nous", fond="nuit", humeur="calme",
         retenir="Distinguer ce qui dépend de nous (nos jugements) de ce qui n'en dépend pas : la liberté du sage est intérieure.",
         beats=[
        "{epic}{tab_epi}Revenons à l'homme que lisait Stockdale. Épictète, l'esclave boiteux de l'épisode un. "
        "Affranchi, il ouvre une école de philosophie. Et tout son enseignement tient dans la première phrase de son Manuel.",
        ("C", "Il y a ce qui dépend de nous, il y a ce qui ne dépend pas de nous.", "c_epi1"),
        "{-epic}{-c_epi1}{-tab_epi}{dep}Ce qui ne dépend pas de nous : {dep.g}notre corps, la richesse, la réputation, "
        "ce que pensent les autres, la maladie, la mort. {dep.d}Ce qui dépend de nous : nos jugements, nos désirs, nos refus. "
        "Bref, notre manière de prendre les choses.",
        "Toute la sagesse consiste à ne pas confondre les deux colonnes. Celui qui met son bonheur à gauche "
        "sera toujours esclave : de la fortune, des autres, du hasard. Celui qui le met à droite… personne ne peut le lui prendre.",
        "{-dep}{tab_exa}{bac}Prends ton bac. {bac.1}Le sujet, le correcteur, ta forme du jour : cela ne dépend pas entièrement de toi. "
        "{bac.2}Ta préparation, ta manière de lire le sujet, ton calme devant la copie : cela, oui. "
        "Le stoïcien met toute son énergie là, et seulement là.",
        "{-bac}{-tab_exa}{tab_sto}Car, dit encore Épictète, ce n'est pas l'événement qui nous blesse.",
        ("C", "Ce qui trouble les hommes, ce ne sont pas les choses, mais les jugements qu'ils portent sur les choses.",
         "c_epi5"),
        "{-c_epi5}{jambe}Souviens-toi de la jambe brisée. {jambe.1}Le maître pouvait tordre la jambe d'Épictète. "
        "{jambe.2}Il ne pouvait pas l'obliger à juger que c'était un malheur. "
        "La colère, la peur, la plainte : voilà les vraies chaînes. Et celles-là, c'est nous qui les serrons.",
        "{-jambe}{-tab_sto}{marc}{tab_mar}Quelques décennies plus tard, l'homme le plus puissant du monde lit les leçons d'Épictète. "
        "Marc Aurèle, empereur de Rome, écrit le soir, pour lui seul, des pensées en grec. "
        "Esclave ou empereur : la leçon est la même.",
        "{-marc}{citad}Il compare l'esprit libéré des passions à une forteresse, où l'on peut toujours se retirer. "
        "Un grand historien de la philosophie, Pierre Hadot, en a tiré une belle formule : la citadelle intérieure.",
        "{-citad}{-tab_mar}{sen}{tab_sen}Sénèque, conseiller de Néron, le montre jusqu'au bout. Condamné par l'empereur "
        "à se donner la mort, il s'ouvre les veines, calmement, en consolant ses amis.",
        ("Ce qui compte, ce n'est pas ce qu'on endure. C'est la manière de l'endurer.", {"rate": "-5%"}),
        "{-sen}{-tab_sen}{lim}Mais une bonne copie voit aussi la limite. {lim.1}Si je ne change que mon regard, "
        "ne vais-je pas accepter l'inacceptable ? {lim.2}L'esclave stoïcien est libre dans sa tête… mais il reste esclave. "
        "La sagesse peut glisser vers la {!résignation}résignation. "
        "{lim.3}La liberté intérieure ne remplace donc pas la liberté politique : elle l'accompagne.",
        ("P", 0.6),
    ], vis={
        "epic": dict(type="portrait", annee=50, img="epictete", nom="Épictète", dates="v. 50 – v. 130",
                     legende="Manuel · Entretiens", x=110, y=120, w=330, h=420),
        "tab_epi": dict(type="tableau", img="t4-epictete", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .4],
                        legende="Épictète, sa béquille près de lui · frontispice du Manuel, Oxford, 1715 (gravure de M. Burghers)"),
        "c_epi1": dict(type="cit", a="Épictète", o="Manuel, I (IIᵉ siècle)", x=640, y=200, w=570),
        "dep": dict(type="cols", g="Ne dépend pas de nous", gq="le corps, la richesse, la réputation, les autres, la mort",
                    d="Dépend de nous", dq="nos jugements, nos désirs, nos refus", vs="≠"),
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "bac": dict(type="cols", g="Ne dépend pas de moi", gq="le sujet, le correcteur, ma forme du jour",
                    d="Dépend de moi", dq="ma préparation, ma lecture du sujet, mon calme", vs="≠"),
        "tab_sto": dict(type="tableau", img="t-hierapolis", fond=True, sombre=True, de=[1.0, .7, .5], a=[1.15, .3, .5],
                        legende="Hiérapolis, en Phrygie, ville natale d'Épictète (photo Bernard Gagnon, CC BY-SA 3.0)"),
        "c_epi5": dict(type="cit", a="Épictète", o="Manuel, V", x=170, y=190, w=940),
        "jambe": dict(type="liste", titre="La jambe d'Épictète", items=[
            "Le corps : au pouvoir du maître", "Le jugement : à moi seul"], marques=["✗", "✓"],
                      cles=["corps", "jugement"], x=170, y=190, w=940),
        "marc": dict(type="portrait", annee=121, img="marc-aurele", nom="Marc Aurèle", dates="121 – 180",
                     legende="Pensées pour moi-même", x=110, y=120, w=330, h=420),
        "tab_mar": dict(type="tableau", img="t4-marc-aurele", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.35, .55, .3],
                        legende="Statue équestre de Marc Aurèle, Capitole, Rome (photo Jebulon, CC0)"),
        "citad": dict(type="mot", t="La citadelle intérieure", g="Marc Aurèle, Pensées, VIII, 48 · formule de Pierre Hadot",
                      x=640, y=250, w=570, taille=64),
        "sen": dict(type="portrait", annee=-4, img="seneque", nom="Sénèque", dates="v. 4 av. – 65 apr. J.-C.",
                    legende="Lettres à Lucilius", x=110, y=120, w=330, h=420),
        "tab_sen": dict(type="tableau", img="t4-seneque", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Pierre Paul Rubens, La Mort de Sénèque, v. 1615"),
        "lim": dict(type="liste", titre="La limite du stoïcisme", items=[
            "Changer son regard… ou accepter l'inacceptable ?",
            "Libre dans sa tête, l'esclave reste esclave",
            "La liberté intérieure ne remplace pas la liberté politique"], marques=["?", "✗", "→"],
                    x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ II. Spinoza
    dict(id="spinoza", chap="Comprendre, c'est se libérer", fond="aube", humeur="mystere",
         retenir="Spinoza : on est esclave de ses passions tant qu'on ignore leurs causes ; comprendre la nécessité, c'est se libérer.",
         beats=[
        "{spin}Dans l'épisode trois, Spinoza nous a dit : le libre arbitre est une illusion. "
        "Nous sommes comme la pierre qui se croit libre. Alors, tout est perdu ? Non. "
        "Car c'est le même Spinoza qui a écrit l'un des plus grands livres sur la libération : l'Éthique.",
        "{tab_rij}Et il l'a vécue. Exclu de sa communauté à vingt-trois ans, il vit modestement en polissant des verres "
        "d'optique. Quand on lui offre une chaire à l'université de Heidelberg, il refuse : il tient à garder sa liberté de penser.",
        "{-spin}{-tab_rij}{tab_tem}{serv}Il commence par nommer notre mal : la {!servitude}servitude. Être esclave, pour Spinoza, "
        "ce n'est pas avoir un maître. C'est être gouverné par ses passions : la colère, la jalousie, la peur, l'espoir. "
        "{serv.1}Celui qui est mené par elles voit le meilleur… et fait le pire.",
        "{-serv}{-tab_tem}{tab_ast}Le remède ? Pas la volonté : Spinoza n'y croit pas. Le remède, c'est la connaissance.",
        ("C", "Une affection qui est une passion cesse d'être une passion sitôt que nous en formons une idée claire et distincte.",
         "c_v3"),
        "{-c_v3}{ex}Prends un exemple. Tu es furieux contre un ami qui t'a laissé tomber. "
        "Tant que tu ne vois que lui, la colère te possède. {ex.1}Mais si tu comprends ce qui l'a poussé : "
        "sa peur, sa fatigue, son histoire… {ex.2}la colère retombe. Tu n'as pas fait un effort de volonté. Tu as compris.",
        "{-ex}{-tab_ast}{nec}Voilà le renversement. {nec.g}La liberté, ce n'est pas échapper à la nécessité. "
        "{nec.d}C'est la comprendre. Spinoza appelle libre ce qui agit par la seule nécessité de sa nature, "
        "et non poussé du dehors.",
        "{-nec}{spin2}Et l'homme libre, celui que guide la raison, n'est plus hanté par la peur.",
        ("C", "L'homme libre ne pense à rien moins qu'à la mort, et sa sagesse est une méditation, non de la mort, mais de la vie.",
         "c_mort"),
        "{-spin2}{-c_mort}{tab_eth}{beat}Au bout du chemin, Spinoza promet une joie stable, qu'il appelle la béatitude. "
        "Pas une récompense : la liberté elle-même, enfin vécue. Il prévient pourtant, à la dernière ligne de son livre : "
        "ce chemin est aussi difficile que rare.",
        "{-beat}{para}Retiens le paradoxe pour ta copie. {para.g}Spinoza nie le libre arbitre… "
        "{para.d}et pourtant, il est l'un des grands penseurs de la liberté. Ce qu'il refuse, c'est le pouvoir de choisir sans cause. "
        "Ce qu'il défend, c'est la puissance de comprendre.",
        ("P", 0.6),
    ], vis={
        "spin": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                     legende="Éthique (1677)", x=110, y=120, w=330, h=420),
        "tab_tem": dict(type="tableau", img="t4-tempete", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Rembrandt, La Tempête sur la mer de Galilée, 1633"),
        "tab_rij": dict(type="tableau", img="t4-rijnsburg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Rijnsburg, la maison où vécut Spinoza, photographie ancienne (Elias Canneman, RCE, CC BY-SA 4.0)"),
        "serv": dict(type="def", cles=["passions", "maître"], terme="La servitude · Éthique, IV",
                     t="Être gouverné par ses passions : on ne s'appartient plus, on est le jouet de la fortune.",
                     etape="« Je vois le meilleur et je l'approuve… je fais le pire » (Ovide, cité par Spinoza).",
                     x=170, y=190, w=940),
        "tab_ast": dict(type="tableau", img="t4-astronome", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .62, .4],
                        legende="Johannes Vermeer, L'Astronome, 1668"),
        "c_v3": dict(type="cit", a="Spinoza", o="Éthique, V, proposition 3 (1677)", x=170, y=170, w=940),
        "ex": dict(type="liste", titre="Un exemple", items=[
            "Je ne vois que lui : la colère me possède",
            "Je comprends ses causes : peur, fatigue, histoire",
            "La passion retombe : j'ai compris, je suis plus libre"], marques=["1", "2", "→"],
                   x=170, y=170, w=940),
        "nec": dict(type="cols", g="Ce n'est pas…", gq="échapper à la nécessité", d="C'est…", dq="comprendre la nécessité",
                    vs="→", repere="Repère · nécessaire / contingent"),
        "spin2": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      legende="Éthique, IV, proposition 67", x=110, y=120, w=330, h=420),
        "c_mort": dict(type="cit", a="Spinoza", o="Éthique, IV, proposition 67 (1677)", x=640, y=170, w=570),
        "tab_eth": dict(type="tableau", img="t-ethica", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                        legende="Spinoza, Ethica, dans les Opera posthuma, 1677"),
        "beat": dict(type="mot", t="La béatitude", g="non la récompense de la liberté : la liberté elle-même", y=250, taille=96),
        "para": dict(type="cols", g="Spinoza refuse", gq="le libre arbitre : choisir sans cause", d="Spinoza défend",
                     dq="la liberté : la puissance de comprendre", vs="≠"),
    }),

    # ------------------------------------------------------------------ III. Rousseau et Kant
    dict(id="autonomie", chap="Obéir à sa propre loi", fond="nuit", humeur="tension",
         retenir="Autonomie : se donner à soi-même sa loi. « Tu dois, donc tu peux » : le devoir me révèle que je suis libre.",
         beats=[
        "{rous}{tab_con}Au dix-huitième siècle, Rousseau ouvre une autre voie. Tu connais déjà sa phrase de l'épisode un. "
        "Écoute-la en entier, cette fois.",
        ("C", "… la liberté morale, qui seule rend l'homme vraiment maître de lui ; car l'impulsion du seul appétit est "
              "esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.", "c_rous"),
        "{-rous}{-c_rous}{-tab_con}{obeir}Obéir… et être libre ? On croyait les deux contraires. "
        "{obeir.g}Rousseau dit l'inverse : obéir à ses envies, c'est être esclave. "
        "{obeir.d}Obéir à une loi qu'on s'est donnée, c'est être son propre maître.",
        "{-obeir}{kantp}{tab_kon}Celui qui va pousser cette idée jusqu'au bout lisait Rousseau avec passion : "
        "Emmanuel Kant, à Königsberg. On raconte qu'il ne manqua sa promenade quotidienne qu'une seule fois : "
        "le jour où il dévorait l'Émile.",
        "{-kantp}{-tab_kon}{tab_kt}{auto}Kant donne un nom à cette liberté : l'{!autonomie}autonomie. Du grec autos, soi-même, "
        "et nomos, la loi. {auto.g}Être autonome, c'est se donner à soi-même sa loi. "
        "{auto.d}Le contraire, c'est l'hétéronomie : recevoir sa loi d'un autre. D'un maître… ou de ses propres penchants.",
        ("L'esclave de ses désirs n'est donc pas autonome. Il obéit encore à quelqu'un.", {"rate": "-4%"}),
        "{-auto}{-tab_kt}{tab_gib}Mais comment savoir que nous sommes libres ? Kant imagine une expérience de pensée. "
        "{gib}{gib.1}Un homme prétend qu'il ne peut pas résister à son désir. Supposons qu'on dresse un gibet devant la maison "
        "où il va le satisfaire, pour l'y pendre aussitôt après. Résisterait-il ? Évidemment, oui : la peur suffit.",
        "{gib.2}Maintenant, son prince lui ordonne, sous peine de mort, de porter un faux témoignage contre un honnête homme. "
        "Résisterait-il ? Il n'ose peut-être pas le promettre. Mais il doit reconnaître que c'est possible.",
        ("C", "Il juge donc qu'il peut faire quelque chose, parce qu'il a la conscience de le devoir, et il reconnaît ainsi "
              "en lui-même la liberté qui, sans la loi morale, lui serait toujours demeurée inconnue.", "c_kant"),
        "{-gib}{-c_kant}{-tab_gib}{tdtp}On résume souvent cette idée en une formule : {tdtp.1}tu dois, donc tu peux. "
        "Ce n'est pas parce que je suis libre que j'ai des devoirs. C'est parce que j'entends le devoir… "
        "que je découvre que je suis libre. Kant ne dit pas que nous résistons toujours. Il dit que nous le pouvons.",
        ("La peur du gibet fait de nous des animaux prudents. Le devoir fait de nous des hommes libres.", {"rate": "-5%"}),
        "{lien_site}Ce texte de Kant, tu peux l'étudier pas à pas dans le guide de l'explication de texte du site.",
        ("P", 0.6),
    ], vis={
        "rous": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                     legende="Du contrat social (1762)", x=110, y=120, w=330, h=420),
        "tab_con": dict(type="tableau", img="t-contrat", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.2, .5, .5],
                        legende="Du contrat social, édition originale, Amsterdam, 1762"),
        "c_rous": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=640, y=150, w=570),
        "obeir": dict(type="cols", g="Obéir à ses envies", gq="« l'impulsion du seul appétit » : esclavage",
                      d="Obéir à sa propre loi", dq="« la loi qu'on s'est prescrite » : liberté", vs="≠"),
        "kantp": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                      legende="Critique de la raison pratique (1788)", x=110, y=120, w=330, h=420),
        "tab_kt": dict(type="tableau", img="t4-kant-table", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .5],
                       legende="Emil Doerstling, Kant et ses convives, 1892-1893 (reproduction)"),
        "tab_kon": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.2, .5, .3],
                        legende="Königsberg, le château, vers 1900 (photochrome, domaine public)"),
        "auto": dict(type="cols", g="Autonomie", gq="autos + nomos : se donner à soi-même sa loi",
                     d="Hétéronomie", dq="recevoir sa loi d'un autre : d'un maître, de ses penchants", vs="≠"),
        "tab_gib": dict(type="tableau", img="t4-gibet", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.4, .45, .5],
                        legende="Pieter Bruegel l'Ancien, La Pie sur le gibet, 1568"),
        "gib": dict(type="liste", titre="L'expérience du gibet", items=[
            "Le désir, et le gibet derrière la porte : il résiste. La peur suffit.",
            "Le faux témoignage, sous peine de mort : il peut refuser. Le devoir suffit."], marques=["1", "2"],
                    x=170, y=150, w=940),
        "c_kant": dict(type="cit", a="Kant", o="Critique de la raison pratique, I, § 6, remarque (1788)", x=170, y=170, w=940),
        "tdtp": dict(type="def", cles=["devoir", "libre"], terme="« Tu dois, donc tu peux »",
                     t="Ce n'est pas la liberté qui fonde le devoir : c'est le devoir qui me révèle que je suis libre.",
                     etape="La loi morale est la preuve de la liberté.", x=170, y=200, w=940),
        "lien_site": dict(type="tag", style="lien", t="Guide de l'explication de texte · le Kant du gibet, corrigé pas à pas",
                          x=170, y=560, w=760),
    }),

    # ------------------------------------------------------------------ IV. les Lumières
    dict(id="lumieres", chap="Ose penser", fond="aube", humeur="lumiere",
         retenir="Les Lumières : sortir de la minorité, oser se servir de son propre entendement. La liberté se conquiert.",
         beats=[
        "{tab_nuit}{ciel}Kant voulait qu'on retienne de lui deux choses. Il l'écrit à la fin de sa Critique de la raison pratique : "
        "deux choses remplissent son cœur d'admiration. {ciel.g}Le ciel étoilé au-dessus de moi… {ciel.d}et la loi morale en moi.",
        "D'un côté, la nature, où tout est nécessaire. De l'autre, la liberté, qui ne se voit pas, "
        "mais qui se fait entendre dans chaque devoir.",
        "{-ciel}{-tab_nuit}{lum}En 1784, une revue berlinoise pose une question : qu'est-ce que les Lumières ? "
        "Kant répond : c'est la sortie de l'homme hors de l'état de minorité, dont il est lui-même responsable. "
        "{lum.1}Être mineur, c'est se laisser penser par d'autres : un livre qui pense à ma place, "
        "un directeur de conscience qui décide de ma morale, un médecin qui choisit mon régime.",
        "{lum.2}Et si l'on reste mineur, ce n'est pas faute d'intelligence. C'est faute de courage. "
        "Il est si confortable d'être mineur.",
        ("C", "Sapere aude ! Aie le courage de te servir de ton propre entendement.", "c_sap"),
        "Voilà, dit Kant, la devise des Lumières.",
        "{-lum}{-c_sap}{tab_ecr}{mineur}Aujourd'hui, le livre qui pense à ta place porte d'autres noms. "
        "{mineur.1}Le fil qui choisit ce que tu vas voir. {mineur.2}La réponse toute faite, qu'on recopie sans la refaire. "
        "{mineur.3}Penser par soi-même, ce n'est pas penser tout seul : c'est oser juger, au lieu de laisser juger pour soi.",
        "{-mineur}{-tab_ecr}{hegel}{tab_nap}Pour aller plus loin, un dernier penseur : Hegel. Pour lui, la liberté ne se conquiert pas "
        "seulement dans la tête de chacun. Elle se réalise dans l'histoire, dans des lois, des institutions. "
        "En octobre 1806, il voit passer Napoléon à cheval dans Iéna, et il écrit à un ami qu'il a vu l'âme du monde.",
        ("C", "L'histoire universelle est le progrès dans la conscience de la liberté.", "c_heg"),
        "{-hegel}{-c_heg}{hist}Selon lui, {hist.1}dans les anciens empires d'Orient, un seul était libre : le despote. "
        "{hist.2}Chez les Grecs et les Romains, quelques-uns : les citoyens, pas les esclaves. "
        "{hist.3}Avec le monde moderne s'impose l'idée que tous les hommes sont libres. "
        "Tu retrouves le fil de l'épisode un : l'histoire de la liberté est celle de son extension.",
        ("P", 0.6),
    ], vis={
        "tab_nuit": dict(type="tableau", img="t4-nuit-etoilee", fond=True, de=[1.0, .5, .3], a=[1.35, .7, .25],
                         legende="Vincent van Gogh, La Nuit étoilée, 1889"),
        "ciel": dict(type="cols", g="Le ciel étoilé au-dessus de moi", gq="la nature : tout y est nécessaire",
                     d="La loi morale en moi", dq="la liberté : elle se fait entendre dans le devoir", vs="&"),
        "lum": dict(type="def", cles=["minorité", "courage"], terme="Les Lumières · Kant, 1784",
                    t="La sortie de l'homme hors de l'état de minorité, dont il est lui-même responsable.",
                    etape="On reste mineur non par manque d'intelligence, mais par manque de courage.",
                    x=170, y=150, w=940),
        "c_sap": dict(type="cit", a="Kant", o="Réponse à la question : qu'est-ce que les Lumières ? (1784)",
                      x=170, y=390, w=940),
        "tab_ecr": dict(type="tableau", img="t-ecrans", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .4, .45],
                        legende="Photo Rawpixel, CC BY 2.0"),
        "mineur": dict(type="liste", titre="Mineur, aujourd'hui ?", items=[
            "Le fil qui choisit ce que je vais voir", "La réponse toute faite, recopiée sans être refaite",
            "Penser par soi-même : oser juger"], marques=["✗", "✗", "✓"], x=170, y=170, w=940),
        "hegel": dict(type="portrait", annee=1770, img="hegel", nom="G. W. F. Hegel", dates="1770 – 1831",
                      legende="Leçons sur la philosophie de l'histoire", x=110, y=120, w=330, h=420),
        "tab_nap": dict(type="tableau", img="t4-napoleon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Charles Meynier, Entrée de Napoléon à Berlin, 27 octobre 1806, 1810"),
        "c_heg": dict(type="cit", a="Hegel", o="Leçons sur la philosophie de l'histoire, introduction (1822-1830 ; trad. courante)",
                      x=640, y=200, w=570),
        "hist": dict(type="liste", titre="Hegel · la liberté dans l'histoire", items=[
            "L'Orient ancien : un seul est libre, le despote", "Grecs et Romains : quelques-uns, les citoyens",
            "Le monde moderne : tous les hommes sont libres"], marques=["1", "2", "3"], plus=True,
                     x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ V. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : les stoïciens. Distinguer ce qui dépend de nous "
        "de ce qui n'en dépend pas.",
        "{rec.2}Deux : Spinoza. On est esclave de ses passions tant qu'on en ignore les causes ; comprendre, c'est se libérer.",
        "{rec.3}Trois : Rousseau et Kant. Être libre, ce n'est pas faire ce qui me plaît : c'est obéir à la loi que je me donne.",
        "{rec.4}Quatre : la liberté se conquiert. Par le courage de penser… et, dit Hegel, dans l'histoire.",
        "{-rec}{tab_hoa2}{fin_q}Revenons à James Stockdale. Libéré en février 1973, il racontera que le petit livre d'Épictète "
        "l'avait aidé à tenir. Il n'était pas libre d'agir. Mais il était resté maître de lui.",
        "Reste une question. Une liberté seulement intérieure suffit-elle ? Stockdale, lui, voulait aussi sortir de prison.",
        ("La prochaine fois, la liberté descend dans la rue : l'État, la loi… et les autres.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-fin_q}{-tab_hoa2}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="SE LIBÉRER", branches=[
            dict(t="Les stoïciens", items=["ce qui dépend de nous", "la citadelle intérieure", "limite : la résignation"]),
            dict(t="Spinoza", items=["la servitude des passions", "comprendre la nécessité", "la béatitude"]),
            dict(t="Rousseau, Kant", items=["obéir à la loi qu'on se donne", "autonomie / hétéronomie", "tu dois, donc tu peux"]),
            dict(t="Conquérir", items=["Sapere aude ! (Kant)", "la liberté dans l'histoire (Hegel)"])]),
        "tab_hoa2": dict(type="tableau", img="t4-hoalo", fond=True, sombre=True, de=[1.2, .5, .45], a=[1.0, .5, .5],
                         legende="Hanoï, prison de Hoa Lo (photo David McKelvey, CC BY 2.0)"),
        "fin_q": dict(type="question", t="Une liberté seulement intérieure suffit-elle ?"),
        "tab_fin": dict(type="tableau", img="t-ddhc", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .35],
                        legende="Jean-Jacques-François Le Barbier, Déclaration des droits de l'homme et du citoyen, 1789"),
        "fin": dict(type="titre", sur="À suivre", t="Libres ensemble", sous="Épisode 5 · L'État, la loi, la société"),
    }),
]

QUIZ = [
    dict(q="Selon Épictète, qu'est-ce qui dépend de nous ?",
         r=["Notre corps et notre santé", "Notre réputation", "Nos jugements, nos désirs, nos refus", "Ce que les autres pensent de nous"],
         ok=2, voir="dep",
         ex="Manuel, I : le corps, la richesse, la réputation ne dépendent pas de nous ; nos jugements, si. La liberté du sage est intérieure."),
    dict(q="Quelle est la principale limite de la liberté stoïcienne ?",
         r=["Elle exige d'être riche", "Elle peut glisser vers la résignation et ne remplace pas la liberté politique",
            "Elle nie l'existence du devoir", "Elle repose sur le libre arbitre absolu"], ok=1, voir="lim",
         ex="Libre dans sa tête, l'esclave reste esclave : la liberté intérieure accompagne la liberté politique, elle ne la remplace pas."),
    dict(q="Pour Spinoza, qu'est-ce que la servitude ?",
         r=["Avoir un maître", "Être gouverné par ses passions", "Obéir aux lois de l'État", "Ne pas avoir de libre arbitre"],
         ok=1, voir="serv",
         ex="Éthique, IV : soumis à ses affects, l'homme ne s'appartient plus ; il « voit le meilleur et fait le pire »."),
    dict(q="Comment Spinoza peut-il nier le libre arbitre et penser la liberté ?",
         r=["Il se contredit", "La liberté, pour lui, c'est comprendre la nécessité, non choisir sans cause",
            "Il réserve la liberté aux philosophes", "Il pense que Dieu nous rend libres par miracle"], ok=1, voir="para",
         ex="Ce qu'il refuse : le pouvoir de choisir sans cause. Ce qu'il défend : la puissance de comprendre (Éthique, V, 3)."),
    dict(q="Que signifie « autonomie » chez Kant ?",
         r=["Faire ce qui me plaît", "Vivre sans aucune loi", "Se donner à soi-même sa loi", "Obéir à son maître"],
         ok=2, voir="auto",
         ex="Autos, soi-même ; nomos, la loi. Le contraire est l'hétéronomie : recevoir sa loi d'un autre, ou de ses penchants."),
    dict(q="Que montre l'expérience du gibet ?",
         r=["Que la peur de la mort est toujours la plus forte", "Que le devoir me révèle que je suis libre",
            "Que nos désirs sont irrésistibles", "Que le prince a toujours raison"], ok=1, voir="c_kant",
         ex="Critique de la raison pratique : il juge qu'il peut, parce qu'il a conscience de devoir. « Tu dois, donc tu peux »."),
    dict(q="« Sapere aude ! » signifie :",
         r=["Obéis sans discuter", "Aie le courage de te servir de ton propre entendement", "Connais-toi toi-même",
            "Supporte et abstiens-toi"], ok=1, voir="c_sap",
         ex="Qu'est-ce que les Lumières ? (1784) : on reste mineur non par manque d'intelligence, mais par manque de courage."),
]

CREDITS = [
    "James Stockdale : portrait officiel, US Navy (domaine public)",
    "Marc Aurèle : statue équestre, Capitole, Rome (photo Jebulon, CC0)",
    "Hegel : Jakob Schlesinger, 1831",
    "Épictète, Spinoza, Rousseau, Kant : voir l'épisode 1",
    "Photographies : prison de Hoa Lo, Hanoï (David McKelvey, CC BY 2.0 ; Richard Mortel, CC BY 2.0) ; Hiérapolis (B. Gagnon, CC BY-SA 3.0) ; maison de Spinoza à Rijnsburg (E. Canneman, RCE, CC BY-SA 4.0) ; salle d'examen ; "
    "foule et téléphones (Rawpixel, CC BY 2.0) ; Ethica (1677) ; Du contrat social (1762)",
    "Tableaux et gravures : frontispice du Manuel d'Épictète (Oxford, 1715) ; Rubens, La Mort de Sénèque (v. 1615) ; "
    "Rembrandt, La Tempête sur la mer de Galilée (1633) ; Vermeer, L'Astronome (1668) ; Doerstling, Kant et ses convives (1892-1893) ; Königsberg, photochrome (v. 1900) ; "
    "Bruegel l'Ancien, La Pie sur le gibet (1568) ; Van Gogh, La Nuit étoilée (1889) ; Meynier, Entrée de Napoléon à Berlin (1810) ; "
    "Le Barbier, Déclaration des droits de l'homme et du citoyen (1789) : domaine public",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
