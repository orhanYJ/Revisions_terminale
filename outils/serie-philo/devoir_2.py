"""Le devoir, épisode 2 : « D'où vient le devoir ? »

Texte lu (beats) et visuels de chaque scène ; même format que liberte_1.py (voir son en-tête).
Quatre voix qui disent « tu dois » : la société (Durkheim, Montaigne, Pascal), Dieu (le Décalogue, l'Euthyphron,
Kierkegaard pour aller plus loin), la conscience (Rousseau, Hugo), la raison (annonce de Kant ; Hume pour aller plus loin).
Notions abordées : champ notions des scènes et repères {#…}.
"""

CODE = "devoir-2"
NOTION = "Le devoir"
NUM = 2
TITRE = "D'où vient le devoir ?"
SUIVANT = "Épisode 3 · Le devoir selon Kant"

PRONONCIATION = {"Gygès": "Jijèsse", "Kierkegaard": "Kirkegarde", "Euthyphron": "Eutifron", "Durkheim": "Durkème",
                 "Hume": "Hioume", "Tupinamba": "Toupinamba"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_bou}{q_port}Un soir, dans une rue vide, tu trouves un portefeuille. Trois cents euros, une carte d'identité. "
        "Personne ne t'a vu. Personne ne le saura jamais.",
        "{-q_port}Tu le rapportes quand même. Pourquoi ?",
        "{-tab_bou}{tab_gyg}Platon posait déjà la question, il y a vingt-quatre siècles. Dans la République, il raconte "
        "l'histoire du berger Gygès, qui trouve un anneau magique : en tournant la bague, il devient invisible. "
        "Que ferait un homme qui ne risque plus rien ? Resterait-il juste ?",
        "Dans le récit, Gygès ne résiste pas longtemps. Il se rend au palais, séduit la reine, tue le roi et prend le pouvoir. "
        "Et Glaucon, le frère de Platon, en tire une conclusion brutale : personne n'est juste volontairement. "
        "Donne l'anneau au plus honnête des hommes, il fera comme Gygès. Nous ne respectons nos devoirs, dit-il, "
        "que par peur d'être pris.",
        ("Si personne ne me voit… qu'est-ce qui m'oblige encore ?", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-tab_gyg}{voix}Demande autour de toi, tu entendras quatre réponses. "
        "{voix.1}On m'a appris que ça se fait. {voix.2}Dieu l'ordonne. {voix.3}Ma conscience me le dit. "
        "{voix.4}C'est ce que n'importe qui devrait faire, à ma place.",
        "Quatre voix qui disent : tu dois. La société, Dieu, la conscience, la raison. "
        "Aujourd'hui, nous allons les écouter une par une… et voir laquelle tient debout.",
        ("P", 0.3),
        "{-voix}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_bou": dict(type="tableau", img="dv2-bourse", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .55, .45],
                        legende="Matthias Stom, Vieille femme tenant une bourse à la chandelle, v. 1640"),
        "q_port": dict(type="question", t="Personne ne t'a vu. Tu le rapportes ?"),
        "tab_gyg": dict(type="tableau", img="dv2-gyges", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .6],
                        legende="Anonyme, L'Anneau de Gygès, Ferrare, XVIᵉ siècle"),
        "voix": dict(type="liste", titre="Pourquoi le rapporter ?", items=[
            "« On m'a appris que ça se fait » : la société", "« Dieu l'ordonne » : la religion",
            "« Ma conscience me le dit » : la conscience", "« N'importe qui devrait le faire » : la raison"],
                     marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "titre": dict(type="titre", sur="Le devoir · Épisode 2", t="D'où vient le devoir ?",
                      sous="La société, Dieu, la conscience, la raison"),
    }),

    # ------------------------------------------------------------------ I. la société
    dict(id="societe", chap="La voix de la société", fond="aube", humeur="calme", notions=["la justice", "la nature"],
         retenir="Durkheim : le devoir est d'abord un fait social, appris par l'éducation. Mais si tout vient des mœurs, plus rien n'est juste en soi.",
         beats=[
        "{durk}{tab_eco}Première voix : la société. C'est la réponse du sociologue Émile Durkheim, à la fin du dix-neuvième siècle. "
        "Mes devoirs, dit-il, je ne les ai pas inventés. Ils existaient avant moi, ils existeront après moi.",
        ("C", "Quand je m'acquitte de ma tâche de frère, d'époux ou de citoyen, quand j'exécute les engagements que j'ai "
              "contractés, je remplis des devoirs qui sont définis, en dehors de moi et de mes actes, dans le droit et dans les mœurs.",
         "c_dur"),
        "{-durk}{-c_dur}{fait}Le devoir est un {!fait social}fait social. {fait.1}Il est extérieur à moi : je le trouve tout fait "
        "en naissant. {fait.2}Il s'impose à moi : si je le transgresse, la société réagit, par le blâme, la honte, la sanction. "
        "{fait.3}Et je l'apprends : par l'éducation, à l'école, dans la famille.",
        "Durkheim pense à l'école de la Troisième République, où l'instituteur fait chaque matin la leçon de morale. "
        "Pour lui, la morale commence là où commence l'attachement à un groupe.",
        "{-fait}{berg}Pour aller plus loin, le philosophe Henri Bergson reprendra cette idée en parlant d'une pression sociale. "
        "Comme l'habitude tient le corps, la société tient chacun de nous par un réseau d'obligations. "
        "Nous obéissons presque sans y penser, comme on s'arrête au feu rouge à trois heures du matin, rue déserte.",
        "{-berg}{-tab_eco}{tab_tup}{mont}C'est une idée forte. Elle explique pourquoi les devoirs changent d'un pays à l'autre. "
        "Montaigne l'avait remarqué dès le seizième siècle, en écoutant des récits sur les Indiens du Brésil.",
        ("C", "Chacun appelle barbarie ce qui n'est pas de son usage.", "c_mon"),
        "{-mont}{-c_mon}{-tab_tup}{tab_bid}{pasc}Un siècle plus tard, Pascal enfonce le clou, avec une ironie féroce. "
        "Une rivière sépare la France de l'Espagne. Et la {#la justice}justice change de camp en la traversant.",
        ("C", "Plaisante justice qu'une rivière borne ! Vérité au-deçà des Pyrénées, erreur au-delà.", "c_pas"),
        "{-pasc}{-c_pas}{lim}Mais voilà le problème. {lim.1}Si le devoir n'est que ce que ma société exige, alors il n'y a plus "
        "de devoir juste ou injuste : il y a seulement des coutumes. {lim.2}Dans une société esclavagiste, le devoir serait de "
        "rendre l'esclave en fuite à son maître. {lim.3}Et le réformateur, celui qui dit « notre coutume est injuste », "
        "n'aurait plus aucun sens.",
        ("Or nous jugeons les coutumes. Il faut donc une autre voix… au-dessus de la société.", {"rate": "-4%"}),
        "{-lim}{-tab_bid}",
        ("P", 0.6),
    ], vis={
        "durk": dict(type="portrait", annee=1858, img="durkheim", nom="Émile Durkheim", dates="1858 – 1917",
                     legende="Les Règles de la méthode sociologique (1895)", x=110, y=120, w=330, h=420),
        "tab_eco": dict(type="tableau", img="dv2-ecole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Albert Bettannier, La Tache noire, 1887 (musée d'Orsay)"),
        "c_dur": dict(type="cit", a="Durkheim", o="Les Règles de la méthode sociologique, chap. I (1895)", x=640, y=130, w=570),
        "fait": dict(type="liste", titre="Le devoir, un fait social", items=[
            "Extérieur : je le trouve tout fait en naissant", "Contraignant : la société sanctionne qui le transgresse",
            "Appris : par l'éducation, l'école, la famille"], marques=["1", "2", "3"], cles=["extérieur", "sanctionne", "éducation"],
                     x=170, y=170, w=940),
        "berg": dict(type="note", titre="Pour aller plus loin", cles=["pression sociale", "habitude"],
                     t="Bergson parle d'une « pression sociale » : la société nous tient par un réseau d'obligations, comme l'habitude tient le corps.",
                     etape="Les Deux Sources de la morale et de la religion (1932).", x=170, y=190, w=940),
        "tab_tup": dict(type="tableau", img="dv2-tupinamba", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Theodor de Bry, rituel des Tupinamba du Brésil, gravure coloriée, 1593 (CC0)"),
        "mont": dict(type="portrait", annee=1533, img="montaigne", nom="Michel de Montaigne", dates="1533 – 1592",
                     legende="Essais, I, 31 « Des cannibales » (1580)", x=110, y=120, w=330, h=420),
        "c_mon": dict(type="cit", a="Montaigne", o="Essais, I, 31, « Des cannibales » (1580)", x=640, y=220, w=570),
        "tab_bid": dict(type="tableau", img="dv2-bidassoa", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .4, .5],
                        legende="La Bidassoa, frontière entre la France et l'Espagne (photo Ignacio Gavira, CC BY 2.5)"),
        "pasc": dict(type="portrait", annee=1623, img="pascal", nom="Blaise Pascal", dates="1623 – 1662",
                     legende="Pensées (1670)", x=110, y=120, w=330, h=420),
        "c_pas": dict(type="cit", a="Pascal", o="Pensées, fr. 294 (éd. Brunschvicg ; 1670)", x=640, y=220, w=570),
        "lim": dict(type="liste", titre="La limite", items=[
            "Si le devoir n'est que coutume, plus rien n'est juste en soi",
            "Société esclavagiste : le « devoir » de rendre l'esclave en fuite",
            "Le réformateur qui juge sa coutume injuste n'aurait plus de sens"], marques=["?", "✗", "→"],
                    x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ II. Dieu
    dict(id="dieu", chap="La voix de Dieu", fond="nuit", humeur="mystere", notions=["la religion", "la vérité"],
         retenir="Dilemme de l'Euthyphron : si Dieu commande le bien parce qu'il est bien, le devoir ne dépend pas de Dieu ; sinon, il est arbitraire.",
         beats=[
        "{tab_moi}Deuxième voix : Dieu. Pendant des siècles, c'est la réponse la plus évidente. "
        "Moïse descend du mont Sinaï avec les tables de la Loi. Et la loi ne se discute pas : elle se reçoit.",
        "{-tab_moi}{tab_moi2}{deca}{deca.1}Tu ne tueras point. {deca.2}Tu ne voleras point. "
        "{deca.3}Tu ne porteras point de faux témoignage contre ton prochain.",
        "{-deca}{-tab_moi2}{dost}Dans cette perspective, sans Dieu, plus rien ne tiendrait. On prête souvent à Dostoïevski "
        "une formule qui résume la peur de son personnage Ivan Karamazov : si Dieu n'existe pas, tout est permis.",
        "{-dost}{tab_soc}{euth}Mais un dialogue de Platon pose ici une question redoutable. Socrate attend son procès "
        "et rencontre Euthyphron, un devin très sûr de lui. {euth.1}Le bien est-il bien parce que les dieux le veulent ? "
        "{euth.2}Ou les dieux le veulent-ils parce qu'il est bien ?",
        "{euth.g}Premier cas : si le bien n'est que ce que Dieu veut, alors le devoir est arbitraire. "
        "Si Dieu ordonnait de mentir, mentir deviendrait un devoir.",
        "{euth.d}Second cas : si Dieu veut le bien parce qu'il est bien, alors le bien existe avant l'ordre. "
        "Je peux le connaître moi-même, et le devoir ne dépend plus de la religion.",
        ("Dans les deux cas, la voix de Dieu ne suffit pas à fonder le devoir.", {"rate": "-4%", "pitch": "-1Hz"}),
        "Attention : cela ne veut pas dire que le croyant a tort de suivre les commandements. Cela veut dire que, "
        "s'il les suit, c'est qu'il les juge bons. Et d'ailleurs, ne pas tuer, ne pas voler, ne pas mentir : "
        "presque toutes les sociétés, croyantes ou non, ont fini par l'exiger. Le contenu du devoir semble donc "
        "plus large que la religion qui l'énonce.",
        "{-euth}{-tab_soc}{kier}{tab_abr}Pour aller plus loin, un penseur a pris le problème à bras-le-corps : "
        "le Danois Søren Kierkegaard. Il relit l'histoire d'Abraham, à qui Dieu demande de sacrifier son fils Isaac.",
        "{susp}Au nom de la morale, Abraham est un meurtrier. Au nom de la foi, il est le père des croyants. "
        "Kierkegaard ose parler d'une suspension de l'éthique : la foi passerait au-dessus du devoir.",
        ("Il ajoute aussitôt que c'est terrible… et que nul ne peut s'en réclamer à la légère.", {"rate": "-5%"}),
        "{-kier}{-susp}{-tab_abr}",
        ("P", 0.6),
    ], vis={
        "tab_moi": dict(type="tableau", img="dv2-moise", de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Rembrandt, Moïse brisant les tables de la Loi, 1659 (Gemäldegalerie, Berlin)"),
        "tab_moi2": dict(type="tableau", img="dv2-moise", fond=True, sombre=True, de=[1.3, .5, .25], a=[1.6, .45, .15],
                         legende="Rembrandt, Moïse brisant les tables de la Loi, 1659 (Gemäldegalerie, Berlin)"),
        "deca": dict(type="liste", titre="Le Décalogue · Exode, 20", items=[
            "Tu ne tueras point", "Tu ne voleras point", "Tu ne porteras point de faux témoignage"],
                     marques=["VI", "VIII", "IX"], x=170, y=190, w=940),
        "dost": dict(type="portrait", annee=1821, img="dostoievski", nom="Fiodor Dostoïevski", dates="1821 – 1881",
                     legende="Les Frères Karamazov (1880)", x=110, y=120, w=330, h=420),
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787"),
        "euth": dict(type="cols", g="Bien parce que Dieu le veut ?", gq="alors le devoir est arbitraire",
                     d="Dieu le veut parce qu'il est bien ?", dq="alors le bien existe avant l'ordre", vs="?",
                     repere="Platon, Euthyphron (vers 399 av. J.-C.)"),
        "kier": dict(type="portrait", annee=1813, img="kierkegaard", nom="Søren Kierkegaard", dates="1813 – 1855",
                     legende="Crainte et tremblement (1843)", x=110, y=120, w=330, h=420),
        "tab_abr": dict(type="tableau", img="dv2-abraham", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="Le Caravage, Le Sacrifice d'Isaac, v. 1603 (Offices, Florence)"),
        "susp": dict(type="note", titre="Pour aller plus loin", cles=["morale", "foi", "suspension"],
                     t="Abraham : meurtrier au nom de la morale, père des croyants au nom de la foi. Kierkegaard parle d'une « suspension téléologique de l'éthique ».",
                     etape="La foi au-dessus du devoir : une possibilité terrible, qui ne se revendique pas à la légère.",
                     x=640, y=150, w=570),
    }),

    # ------------------------------------------------------------------ III. la conscience
    dict(id="conscience", chap="La voix de la conscience", fond="aube", humeur="lumiere",
         notions=["la conscience", "la nature"],
         retenir="Rousseau : la conscience morale, « instinct divin », juge du bien et du mal. Mais une conscience peut être faussée.",
         beats=[
        "{rous}{tab_emi}Troisième voix : la conscience. Au dix-huitième siècle, Rousseau la célèbre dans un passage fameux de l'Émile, "
        "la Profession de foi du vicaire savoyard.",
        ("C", "Conscience ! conscience ! instinct divin, immortelle et céleste voix ; guide assuré d'un être ignorant et borné, "
              "mais intelligent et libre ; juge infaillible du bien et du mal, qui rends l'homme semblable à Dieu !", "c_rou"),
        "{-rous}{-c_rou}{-tab_emi}{tab_sam}{pitie}Pour Rousseau, nous n'avons pas besoin d'un livre ni d'un prêtre pour savoir "
        "qu'il faut secourir le blessé au bord de la route. {pitie.1}Avant toute réflexion, nous sentons de la pitié : "
        "une répugnance naturelle à voir souffrir un autre être sensible. {pitie.2}La conscience est cette voix intérieure, "
        "qui juge nos actes avant même que nous les ayons justifiés.",
        "Rousseau en donne un signe simple, dans son Discours sur l'origine de l'inégalité : même les animaux "
        "montrent de la répugnance à passer près d'un des leurs qui agonise. Et l'homme le plus endurci pleure encore "
        "au théâtre, devant des malheurs qui ne le menacent pas. La pitié vient avant la raison, avant les lois, "
        "avant même la parole.",
        "{-pitie}{-tab_sam}{tab_cai}Et cette voix, on ne la fait pas taire. Victor Hugo l'a dit dans un poème célèbre, « La Conscience ». "
        "Caïn, qui a tué son frère, fuit avec sa famille jusqu'au bout du monde. Il fait creuser une tombe, s'y enferme, "
        "fait sceller la pierre au-dessus de lui.",
        ("C", "L'œil était dans la tombe et regardait Caïn.", "c_hug"),
        "{-c_hug}{-tab_cai}{cons}Retiens l'idée. {cons.g}Le devoir, ici, ne vient pas du dehors, comme chez Durkheim. "
        "{cons.d}Il vient du dedans : de ma nature d'homme, qui sent le bien avant de le penser.",
        "{-cons}{lim2}Mais la conscience suffit-elle ? {lim2.1}Le fanatique aussi a la conscience tranquille. "
        "{lim2.2}Une conscience peut être faussée par l'éducation : on peut avoir appris à trouver normal l'insupportable. "
        "{lim2.3}Et Freud, nous le verrons dans l'épisode quatre, soupçonnera dans cette voix l'écho de nos parents : "
        "le surmoi, une part de l'{#l'inconscient}inconscient.",
        ("Pour que le devoir soit sûr, il faudrait une voix que tout le monde puisse vérifier.", {"rate": "-4%"}),
        "{-lim2}",
        ("P", 0.6),
    ], vis={
        "rous": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                     legende="Émile, livre IV (1762)", x=110, y=120, w=330, h=420),
        "tab_emi": dict(type="tableau", img="dv2-emile", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .4],
                        legende="Rousseau, Émile ou De l'éducation, page de titre, 1762"),
        "c_rou": dict(type="cit", a="Rousseau", o="Émile, IV, « Profession de foi du vicaire savoyard » (1762)",
                      x=640, y=120, w=570),
        "tab_sam": dict(type="tableau", img="dv2-samaritain", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .55],
                        legende="Rembrandt, Paysage avec le bon Samaritain, 1638 (musée Czartoryski, Cracovie)"),
        "pitie": dict(type="liste", titre="La voix intérieure", items=[
            "La pitié : répugner à voir souffrir un être sensible", "La conscience : juger nos actes avant de les justifier"],
                      marques=["1", "2"], cles=["pitié", "conscience"], x=170, y=190, w=940),
        "tab_cai": dict(type="tableau", img="dv2-cain", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .5],
                        legende="Fernand Cormon, Caïn, 1880 (musée d'Orsay)"),
        "c_hug": dict(type="cit", a="Victor Hugo", o="« La Conscience », La Légende des siècles (1859)", x=170, y=230, w=940),
        "cons": dict(type="cols", g="Durkheim", gq="le devoir vient du dehors : la société", d="Rousseau",
                     dq="le devoir vient du dedans : la conscience", vs="≠"),
        "lim2": dict(type="liste", titre="Mais…", items=[
            "Le fanatique aussi a la conscience tranquille", "Une conscience peut être faussée par l'éducation",
            "Freud : la voix des parents, le surmoi (épisode 4)"], marques=["✗", "✗", "→"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ IV. la raison
    dict(id="raison", chap="La voix de la raison", fond="nuit", humeur="tension", notions=["la raison", "la liberté"],
         retenir="Kant : le devoir vient de la raison, la même en chacun. Hume : on ne tire pas un « tu dois » d'un simple « c'est ainsi ».",
         beats=[
        "{kant}{tab_nui}Quatrième voix, la plus exigeante : la raison. C'est celle d'Emmanuel Kant, et nous lui consacrerons "
        "tout l'épisode trois. Voici déjà l'idée.",
        "La société varie d'un pays à l'autre. La foi n'est pas partagée par tous. Le sentiment peut se tromper. "
        "Mais la raison, elle, est la même en chacun de nous.",
        "{-kant}{test}Reprends le portefeuille. Ne te demande pas : qu'est-ce qu'on m'a appris ? "
        "Demande-toi : {test.1}et si tout le monde faisait comme moi ? {test.2}Si chacun gardait ce qu'il trouve, "
        "plus personne n'oserait rien perdre, plus personne ne rendrait rien. {test.3}Ma règle se détruit elle-même "
        "dès que je veux qu'elle vaille pour tous.",
        "Voilà le devoir : non pas ce qu'on m'impose, mais ce que je peux vouloir pour tous, sans me contredire.",
        "{-test}{-tab_nui}{auto}Et si c'est ma propre raison qui me donne la loi, alors obéir au devoir n'est plus être esclave. "
        "C'est être autonome. Tu reconnais l'idée de la série sur la {#la liberté}liberté : "
        "« l'obéissance à la loi qu'on s'est prescrite est liberté ».",
        "{-auto}{hume}{tab_hum}Pour aller plus loin, un philosophe écossais, David Hume, a montré pourquoi cette voix est "
        "indispensable. Il remarque un glissement dans tous les livres de morale : on décrit d'abord ce qui est, "
        "puis, sans prévenir, on passe à ce qui doit être.",
        "{loi}{loi.g}Les hommes ont toujours fait ainsi… {loi.d}donc ils doivent faire ainsi. Or, dit Hume, "
        "aucun fait ne contient à lui seul un devoir.",
        "Prends un exemple. Les hommes se sont toujours fait la guerre : c'est un fait, l'histoire le montre. "
        "Faut-il en conclure qu'ils doivent se faire la guerre ? Évidemment pas. Ou encore : la nature élimine les plus faibles. "
        "En conclure qu'il faut abandonner les faibles, c'est commettre exactement le glissement que Hume dénonce.",
        ("Ce qui est ne dit jamais, à lui seul, ce qui doit être.", {"rate": "-5%", "pitch": "-1Hz"}),
        "{-hume}{-loi}{-tab_hum}{bil}C'est pourquoi les coutumes, les faits de {#la nature}nature ou les habitudes ne suffisent pas "
        "à fonder le devoir. Il faut une source qui ne soit pas un simple fait : ce sera, pour Kant, la raison pratique.",
        "{-bil}",
        ("P", 0.6),
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Fondements de la métaphysique des mœurs (1785)", x=110, y=120, w=330, h=420),
        "tab_nui": dict(type="tableau", img="t4-nuit-etoilee", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .6, .3],
                        legende="Vincent van Gogh, La Nuit étoilée, 1889"),
        "test": dict(type="liste", titre="Le test de la raison", items=[
            "Et si tout le monde faisait comme moi ?", "Chacun garde ce qu'il trouve : plus personne ne rend rien",
            "La règle se détruit dès qu'elle vaut pour tous"], marques=["?", "✗", "→"], x=170, y=170, w=940),
        "auto": dict(type="def", cles=["raison", "autonome"], terme="Le devoir selon la raison",
                     t="Non pas ce qu'on m'impose, mais ce que je peux vouloir pour tous sans me contredire : la loi que ma raison se donne.",
                     etape="Obéir au devoir, c'est être autonome (série « La liberté », épisode 4).", x=170, y=190, w=940),
        "hume": dict(type="portrait", annee=1711, img="hume", nom="David Hume", dates="1711 – 1776",
                     legende="Traité de la nature humaine, III (1740)", x=110, y=120, w=330, h=420),
        "tab_hum": dict(type="tableau", img="t2-meditations", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="Descartes, Meditationes de prima philosophia, page de titre, Paris, 1641"),
        "loi": dict(type="cols", g="Ce qui est", gq="« les hommes ont toujours fait ainsi »", d="Ce qui doit être",
                    dq="« donc ils doivent faire ainsi » : passage illégitime", vs="↛",
                    repere="Pour aller plus loin · la « loi de Hume »"),
        "bil": dict(type="mot", t="La raison pratique", g="une source du devoir qui n'est pas un simple fait", y=250, taille=80),
    }),

    # ------------------------------------------------------------------ V. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir. {rec.1}Un : la société. Pour Durkheim, le devoir est un fait social, appris et sanctionné. "
        "Mais alors, plus rien n'est juste en soi.",
        "{rec.2}Deux : Dieu. Le dilemme de l'Euthyphron montre que le commandement seul ne fonde pas le bien.",
        "{rec.3}Trois : la conscience. Rousseau y entend un instinct divin ; mais une conscience peut se tromper.",
        "{rec.4}Quatre : la raison. Seule une loi que chacun peut vouloir pour tous donne au devoir sa force. "
        "Et on ne tire pas un devoir d'un simple fait.",
        "Ces quatre voix ne s'excluent pas toujours. Souvent, elles disent la même chose : rends ce qui n'est pas à toi. "
        "Le problème commence quand elles se contredisent. C'est là qu'il faut savoir laquelle a le dernier mot. "
        "Dans une dissertation, c'est ce classement qui fait ton plan : du devoir reçu au devoir pensé.",
        "{-rec}{tab_bou2}{fin_q}Revenons au portefeuille. Tu le rapportes peut-être parce qu'on te l'a appris, "
        "ou parce que tu aurais honte. Mais si tu le rapportes parce que tu ne pourrais pas vouloir un monde "
        "où chacun garde tout… alors tu agis par devoir.",
        ("La prochaine fois, nous entrons dans la plus célèbre des morales du devoir : celle de Kant.",
         {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-fin_q}{-tab_bou2}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="D'OÙ VIENT LE DEVOIR ?", branches=[
            dict(t="La société", items=["Durkheim : un fait social", "Montaigne, Pascal : les mœurs varient", "limite : plus rien de juste en soi"]),
            dict(t="Dieu", items=["le Décalogue", "le dilemme de l'Euthyphron", "Kierkegaard : la foi au-dessus"]),
            dict(t="La conscience", items=["Rousseau : « instinct divin »", "la pitié", "limite : une conscience faussée"]),
            dict(t="La raison", items=["Kant : vouloir pour tous", "l'autonomie", "Hume : être ≠ devoir être"])]),
        "tab_bou2": dict(type="tableau", img="dv2-bourse", fond=True, sombre=True, de=[1.2, .5, .4], a=[1.0, .5, .5],
                         legende="Matthias Stom, Vieille femme tenant une bourse à la chandelle, v. 1640"),
        "fin_q": dict(type="question", t="Agir par devoir, ou seulement conformément au devoir ?"),
        "tab_fin": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .35],
                        legende="Königsberg, le château, vers 1900 (photochrome, domaine public)"),
        "fin": dict(type="titre", sur="À suivre", t="Le devoir selon Kant", sous="Épisode 3 · La bonne volonté, l'impératif catégorique"),
    }),
]

QUIZ = [
    dict(q="Pour Durkheim, le devoir est d'abord…",
         r=["une révélation divine", "un fait social, extérieur et contraignant, appris par l'éducation",
            "un instinct de la nature", "une invention de chaque individu"], ok=1, voir="fait",
         ex="Les Règles de la méthode sociologique : mes devoirs sont « définis, en dehors de moi […], dans le droit et dans les mœurs »."),
    dict(q="Que veut montrer Pascal avec « Plaisante justice qu'une rivière borne » ?",
         r=["Que la justice est universelle", "Que ce qu'on tient pour juste varie selon les pays",
            "Que les Pyrénées sont une frontière naturelle", "Que la justice vient de Dieu"], ok=1, voir="c_pas",
         ex="Pensées : « Vérité au-deçà des Pyrénées, erreur au-delà. » Si le devoir n'est que coutume, il change avec la frontière."),
    dict(q="Quelle est la limite de la thèse sociologique ?",
         r=["Elle oublie l'école", "Si le devoir n'est que coutume, on ne peut plus juger une coutume injuste",
            "Elle repose sur la religion", "Elle nie l'existence des sociétés"], ok=1, voir="lim",
         ex="Le réformateur qui dit « notre coutume est injuste » n'aurait plus de sens : il faut une voix au-dessus de la société."),
    dict(q="Que montre le dilemme de l'Euthyphron ?",
         r=["Que Dieu n'existe pas", "Que le commandement divin, seul, ne suffit pas à fonder le bien",
            "Que les dieux se trompent toujours", "Que la piété est inutile"], ok=1, voir="euth",
         ex="Si le bien n'est que ce que Dieu veut, il est arbitraire ; si Dieu le veut parce qu'il est bien, le bien existe avant l'ordre."),
    dict(q="Comment Rousseau appelle-t-il la conscience ?",
         r=["« la voix de la société »", "« instinct divin, immortelle et céleste voix »", "« le surmoi »",
            "« la raison pure »"], ok=1, voir="c_rou",
         ex="Émile, IV : « juge infaillible du bien et du mal ». Limite : le fanatique aussi a la conscience tranquille."),
    dict(q="Quel est le test de la raison appliqué au portefeuille ?",
         r=["Me demander ce qu'on m'a appris", "Me demander si quelqu'un m'a vu",
            "Me demander si je peux vouloir que tout le monde fasse comme moi", "Me demander ce que je gagne"], ok=2, voir="test",
         ex="Si chacun gardait ce qu'il trouve, plus personne ne rendrait rien : la règle se détruit dès qu'elle vaut pour tous."),
    dict(q="Que dit la « loi de Hume » ?",
         r=["Qu'il faut obéir aux lois", "Qu'on ne peut pas tirer un devoir d'un simple fait",
            "Que la raison est l'esclave des passions et doit le rester", "Que le devoir vient de Dieu"], ok=1, voir="loi",
         ex="Traité de la nature humaine, III : de « ce qui est », on ne déduit pas, à lui seul, « ce qui doit être »."),
]

CREDITS = [
    "Portraits : Durkheim (photographie anonyme) ; Montaigne (portrait anonyme, musée Condé) ; Pascal (copie d'après François II Quesnel) ; "
    "Dostoïevski (Vassili Perov, 1872) ; Kierkegaard (Bibliothèque royale du Danemark) ; Rousseau (Maurice Quentin de La Tour, 1753) ; "
    "Kant (portrait anonyme, XVIIIᵉ s.) ; Hume (Allan Ramsay, 1766) : domaine public",
    "Tableaux et gravures : Matthias Stom, Vieille femme tenant une bourse (v. 1640) ; L'Anneau de Gygès (Ferrare, XVIᵉ s.) ; "
    "A. Bettannier, La Tache noire (1887) ; Theodor de Bry, rituel tupinamba (1593, CC0) ; Rembrandt, Moïse brisant les tables de la Loi (1659) "
    "et Paysage avec le bon Samaritain (1638) ; J.-L. David, La Mort de Socrate (1787) ; le Caravage, Le Sacrifice d'Isaac (v. 1603) ; "
    "F. Cormon, Caïn (1880) ; V. van Gogh, La Nuit étoilée (1889) ; Émile (1762) et Meditationes (1641), pages de titre ; Königsberg, photochrome (v. 1900) : domaine public",
    "Photographie : la Bidassoa (Ignacio Gavira, CC BY 2.5)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
