"""Le devoir, épisode 4 : « Contre le devoir »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la conscience} dans le texte lu.
Nietzsche (la dette, la mauvaise conscience, maîtres et esclaves, le lion contre le dragon « Tu dois »),
Freud (le surmoi, Malaise dans la civilisation), l'utilitarisme (Bentham, Mill ; le tramway pour aller plus loin),
les morales du bonheur (Épicure, Aristote).
Citations approchées (traductions variables) : Généalogie de la morale II, 4 et II, 16 ; Malaise dans la civilisation, VII.
"""

CODE = "devoir-4"
NOTION = "Le devoir"
NUM = 4
TITRE = "Contre le devoir"
SUIVANT = "Épisode 5 · Conflits de devoirs"

PRONONCIATION = {"Nietzsche": "Nitche", "Schuld": "Choulde", "Schulden": "Chouldenne", "Bentham": "Bentame",
                 "Shylock": "Chaïlok", "Ménécée": "Ménécé", "Foot": "Foutte", "Thomson": "Tomsonne",
                 "Jarvis": "Djarvis", "Durkheim": "Durkème"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_vei}{q1}Dimanche soir. Tu as passé l'après-midi avec tes amis. Rien de grave. "
        "Et pourtant, une boule au ventre : tu n'as pas révisé. Tu te sens coupable.",
        ("Coupable… mais de quoi, au juste ? Et envers qui ?", {"rate": "-6%"}),
        "{-q1}{rappel}Cette voix qui dit « tu aurais dû », nous l'écoutons depuis trois épisodes. "
        "{rappel.1}Le devoir est une obligation, pas une contrainte. {rappel.2}Il viendrait de la société, de Dieu, ou de la conscience. "
        "{rappel.3}Et pour Kant, il se fonde sur la raison : agir par devoir, sans calcul.",
        "{-rappel}{-tab_vei}{tab_cri}{q2}Aujourd'hui, on change de camp. Et si le devoir n'était pas ce qu'il prétend être ? "
        "Et s'il nous rendait malades… ou s'il nous trompait sur ce qui compte vraiment ?",
        "{-q2}{quatre}Quatre attaques, de plus en plus douces. {quatre.1}Nietzsche. {quatre.2}Freud. "
        "{quatre.3}Les utilitaristes, qui jugent les actes à leurs conséquences. "
        "{quatre.4}Et les sages grecs, pour qui la vraie question n'est pas le devoir, mais le bonheur.",
        "{-quatre}{-tab_cri}Épisode quatre.",
        ("P", 0.3),
        "{titre}",
        ("P", 3.2),
    ], vis={
        "tab_vei": dict(type="tableau", img="t7-veille", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .4],
                        legende="Matthias Stom, Jeune homme lisant à la chandelle, v. 1630-1640"),
        "q1": dict(type="question", t="Coupable… mais de quoi ? Et envers qui ?"),
        "rappel": dict(type="liste", titre="Ce que nous savons déjà", items=[
            "Ép. 1 · Le devoir : une obligation, pas une contrainte",
            "Ép. 2 · Il viendrait de la société, de Dieu, de la conscience",
            "Ép. 3 · Kant : agir par devoir, selon la raison"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_cri": dict(type="tableau", img="t2-cri", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Edvard Munch, Le Cri, 1893 (Galerie nationale d'Oslo)"),
        "q2": dict(type="question", t="Et si le devoir nous rendait malades ?"),
        "quatre": dict(type="liste", titre="Quatre attaques contre le devoir", items=[
            "Nietzsche : la cruauté à l'origine de la morale",
            "Freud : la voix intériorisée des parents",
            "Bentham et Mill : juger par les conséquences",
            "Épicure et Aristote : d'abord le bonheur"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "titre": dict(type="titre", sur="Le devoir · Épisode 4", t="Contre le devoir",
                      sous="Nietzsche, Freud, l'utilitarisme, les morales du bonheur"),
    }),

    # ------------------------------------------------------------------ I. Nietzsche : la dette
    dict(id="dette", chap="Nietzsche : la dette et la faute", fond="aube", humeur="mystere",
         notions=["la conscience", "la justice"],
         retenir="Nietzsche : la faute vient de la dette ; la mauvaise conscience, c'est l'agressivité retournée contre soi.", beats=[
        "{nietz}{tab_sil}Commençons par le plus féroce. Friedrich Nietzsche, philosophe allemand, publie en 1887 "
        "la Généalogie de la morale. Une généalogie, c'est une enquête sur les origines… et les origines ne sont pas toujours belles.",
        "On l'a croisé dans la série sur la liberté. Ici, il pose une question radicale : d'où vient le sentiment même du devoir ?",
        "{-nietz}{-tab_sil}{tab_jus}Souviens-toi de l'épisode un : devoir vient de debere, être en dette. "
        "Nietzsche fait la même remarque sur sa propre langue.",
        ("C", "Le concept moral fondamental de « faute », Schuld, tire son origine du concept très matériel de « dette », Schulden.",
         "c_schuld"),
        "{-c_schuld}{-tab_jus}{tab_shy}{cd}Au commencement, dit Nietzsche, il y a un rapport très simple : "
        "{cd.g}un créancier, {cd.d}un débiteur. Celui qui ne rembourse pas paiera autrement : avec son corps, avec sa souffrance.",
        "Shakespeare en a tiré une pièce. Dans Le Marchand de Venise, l'usurier Shylock exige une livre de chair "
        "de son débiteur, qui ne peut pas rembourser.",
        "{-cd}{-tab_shy}{pun}Pour Nietzsche, le châtiment est né là. {pun.1}Le tort est une dette. {pun.2}La peine est un paiement. "
        "{pun.3}Et voir souffrir le coupable procure au créancier… un plaisir : celui d'exercer sa puissance.",
        ("Au fond de la morale, il y a de la {!cruauté}cruauté.", {"rate": "-6%"}),
        "{-pun}{tab_sil2}{int}Mais comment cette dette est-elle devenue intérieure ? "
        "Quand les hommes ont été enfermés dans la société et dans la paix, leurs instincts sauvages, "
        "l'agressivité, le goût de la chasse et de la destruction, n'ont plus pu sortir. Alors ils se sont retournés.{-int}",
        ("C", "Tous les instincts qui ne se déchargent pas au-dehors se retournent en dedans.", "c_int"),
        "{-c_int}{mc}Voilà ce que Nietzsche appelle la mauvaise {#la conscience}conscience : l'homme devenu son propre bourreau. "
        "{mc.1}Ta boule au ventre du dimanche, ce serait cela : une dette que tu te réclames à toi-même. "
        "Et quand on croit devoir tout à un Dieu infini, la dette devient impayable.",
    ], vis={
        "nietz": dict(type="portrait", annee=1844, legende="Généalogie de la morale (1887)", img="nietzsche",
                      nom="Friedrich Nietzsche", dates="1844 – 1900", x=110, y=120, w=330, h=420),
        "tab_sil": dict(type="tableau", img="dv4-sils", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .45],
                        legende="Sils-Maria, où Nietzsche passait ses étés (photo Hansueli Krapf, CC BY-SA 4.0)"),
        "tab_jus": dict(type="tableau", img="dv4-justitia", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.35, .5, .3],
                        legende="Pieter Bruegel l'Ancien (d'après), La Justice, gravure, 1559 (Rijksmuseum, CC0)"),
        "c_schuld": dict(type="cit", a="Nietzsche", o="Généalogie de la morale, II, 4 (1887)", para=True, x=170, y=170, w=940),
        "tab_shy": dict(type="tableau", img="dv4-shylock", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .55, .3],
                        legende="Gilbert Stuart Newton, Shylock et Jessica, 1830"),
        "cd": dict(type="cols", g="Le créancier", gq="on lui doit : il a le droit de faire souffrir", d="Le débiteur",
                   dq="il ne rembourse pas : il paie de son corps", vs="→"),
        "pun": dict(type="liste", titre="La généalogie du châtiment", items=[
            "Le tort est une dette", "La peine est un paiement",
            "La souffrance du coupable : un plaisir pour le créancier"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_sil2": dict(type="tableau", img="t3-cauchemar", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                         legende="Johann Heinrich Füssli, Le Cauchemar, 1781"),
        "int": dict(type="mot", t="Une dette intériorisée", g="la société enferme les instincts : où vont-ils ?", y=270),
        "c_int": dict(type="cit", a="Nietzsche", o="Généalogie de la morale, II, 16 (1887)", para=True, x=170, y=170, w=940),
        "mc": dict(type="def", terme="La mauvaise conscience", cles=["retourne", "bourreau"],
                   t="L'agressivité qui ne peut plus sortir se retourne contre soi : l'homme devient son propre bourreau.",
                   etape="Le devoir : une dette qu'on se réclame à soi-même.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. Nietzsche : maîtres et esclaves
    dict(id="maitres", chap="Nietzsche : maîtres et esclaves", fond="nuit", humeur="tension",
         notions=["la religion", "la liberté"],
         retenir="Morale des maîtres (« nous sommes bons ») / morale des esclaves (« ils sont méchants ») : le ressentiment. "
                 "Le lion dit « Je veux » au dragon « Tu dois ».", beats=[
        "{tab_leo}{me}Deuxième coup, dans le même livre. Il y a, dit Nietzsche, deux façons d'inventer des valeurs. "
        "{me.g}Les maîtres, les aristocrates guerriers de l'Antiquité, partent d'eux-mêmes : nous sommes forts, fiers, généreux… "
        "donc nous sommes bons. Le mauvais, c'est simplement ce qui est bas, faible, vulgaire.",
        "{me.d}Les esclaves, eux, partent des autres : les forts nous écrasent, ils sont méchants. "
        "Donc nous, qui ne sommes pas comme eux, nous sommes bons.",
        "{-me}{-tab_leo}{tab_mar}{ress}Ce sentiment, Nietzsche lui donne un nom français : le ressentiment. "
        "La rancune de celui qui ne peut pas agir… et qui se venge en jugeant.",
        "{ress.1}C'est la révolte des esclaves dans la morale : l'humilité, l'obéissance, la pitié deviennent des vertus, "
        "et la force devient une faute. Selon Nietzsche, et c'est une thèse très discutée, "
        "la {#la religion}religion chrétienne aurait fait triompher cette morale en Europe.",
        "{-ress}{-tab_mar}{trp}Le devoir universel, « tu dois, comme tout le monde », serait alors une morale de troupeau : "
        "une règle faite par les faibles, pour ramener les forts à leur niveau.",
        "{-trp}{tab_cha}{meta}Contre elle, Nietzsche raconte une fable, dans Ainsi parlait Zarathoustra : les trois métamorphoses de l'esprit. "
        "{meta.1}D'abord, le chameau. Il s'agenouille, et réclame les plus lourds fardeaux. Il porte tous les devoirs, sans broncher.",
        "{meta.2}{-tab_cha}{tab_lio}Puis le chameau, au désert, devient lion. Il affronte un grand dragon, "
        "dont chaque écaille brille de deux mots dorés : « Tu dois ». Et le lion répond : « Je veux ».",
        "{meta.3}{-tab_lio}{tab_tot}Enfin, le lion devient enfant : innocence, oubli, jeu, nouveau commencement. "
        "L'enfant ne se contente pas de refuser les valeurs : il en crée.",
        "{-meta}{-tab_tot}{nk}Tu vois l'opposition avec l'épisode trois. {nk.g}Pour Kant, être libre, c'est obéir à la loi que ma raison se donne. "
        "{nk.d}Pour Nietzsche, c'est créer ses propres valeurs. Son mot d'ordre : deviens ce que tu es.",
        ("Attention : cela ne veut pas dire « tout est permis ».", {"rate": "-5%"}),
        "Le créateur de valeurs est plus exigeant que le chameau : il se donne une forme, un style… mais il ne reçoit sa loi de personne.",
    ], vis={
        "tab_leo": dict(type="tableau", img="dv4-leonidas", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="Jacques-Louis David, Léonidas aux Thermopyles, 1814 (musée du Louvre)"),
        "me": dict(type="cols", g="Morale des maîtres", gq="« nous sommes forts : nous sommes bons »", d="Morale des esclaves",
                   dq="« ils sont forts : ils sont méchants »", vs="≠"),
        "tab_mar": dict(type="tableau", img="dv4-martyrs", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .65, .55],
                        legende="Jean-Léon Gérôme, La Dernière Prière des martyrs chrétiens, 1863-1883 (Walters Art Museum)"),
        "ress": dict(type="def", terme="Le ressentiment", cles=["venge", "jugeant"],
                     t="La rancune de celui qui ne peut pas agir, et qui se venge en jugeant.",
                     etape="La révolte des esclaves dans la morale : la faiblesse devient vertu, la force devient faute.",
                     x=170, y=200, w=940),
        "trp": dict(type="mot", t="Une morale de troupeau ?", g="le devoir universel : ramener les forts au niveau des faibles", y=270),
        "tab_cha": dict(type="tableau", img="dv4-chameau", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.25, .45, .6],
                        legende="Caravane de dromadaires (photo Van Achterberg, ASC Leiden, CC BY-SA 4.0)"),
        "meta": dict(type="liste", titre="Les trois métamorphoses · Ainsi parlait Zarathoustra (1883)", items=[
            "Le chameau : il porte les fardeaux, « tu dois »",
            "Le lion : contre le dragon « Tu dois », il dit « Je veux »",
            "L'enfant : innocence, jeu, création de valeurs"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_lio": dict(type="tableau", img="dv4-lion", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .55],
                        legende="Jean-Léon Gérôme, Lion cherchant à saisir un papillon"),
        "tab_tot": dict(type="tableau", img="dv4-toton", fond=True, sombre=True, de=[1.0, .55, .45], a=[1.3, .6, .4],
                        legende="Jean Siméon Chardin, L'Enfant au toton, 1738 (musée du Louvre)"),
        "nk": dict(type="cols", g="Kant", gq="obéir à la loi que ma raison se donne", d="Nietzsche",
                   dq="créer ses valeurs : « deviens ce que tu es »", vs="≠"),
    }),

    # ------------------------------------------------------------------ III. Freud : le surmoi
    dict(id="freud", chap="Freud : le surmoi", fond="aube", humeur="tension", notions=["l'inconscient", "la conscience"],
         retenir="Freud : le surmoi, voix intériorisée des parents ; la civilisation le paie en culpabilité.", beats=[
        "{freud}{tab_div}Une génération plus tard, à Vienne, Sigmund Freud arrive, par un autre chemin, à une conclusion voisine. "
        "On l'a rencontré dans la série sur la liberté : le moi n'est pas maître dans sa propre maison. Allons plus loin.",
        "{-freud}{-tab_div}{tab_ice}{topi}En 1923, Freud décrit le psychisme comme trois instances. "
        "{topi.1}Le ça : nos pulsions, qui veulent être satisfaites, tout de suite. "
        "{topi.2}Le surmoi : les interdits, les idéaux, le « tu dois ». "
        "{topi.3}Et le moi, pris entre les deux… et la réalité.",
        "{-topi}{-tab_ice}{orig}D'où vient le surmoi ? {orig.1}De nos parents : l'enfant intériorise leurs interdits. "
        "{orig.2}La voix qui grondait est devenue une voix intérieure. "
        "{orig.3}Et elle reste en grande partie {#l'inconscient}inconsciente : elle nous juge, sans que nous sachions pourquoi.",
        "{-orig}{tab_jer}{para}D'où un paradoxe que Freud relève. Plus quelqu'un est vertueux, plus il se sent coupable : "
        "ce sont les saints qui se disent les plus grands pécheurs. Le surmoi est insatiable ; chaque renoncement le rend plus sévère.",
        "{-para}{-tab_jer}{tab_cit}{mal}En 1930, dans Malaise dans la civilisation, Freud élargit l'idée à toute la société. "
        "Pour vivre ensemble, il faut renoncer à une part de nos pulsions, surtout à l'agressivité. Comment la civilisation s'y prend-elle ?{-mal}",
        ("C", "La civilisation domine la dangereuse agressivité de l'individu… en le faisant surveiller par une instance "
              "en lui-même, comme par une garnison placée dans une ville conquise.", "c_gar"),
        "{-c_gar}{-tab_cit}{nf}Rapproche Nietzsche et Freud : la même idée, presque mot pour mot. "
        "{nf.g}La mauvaise conscience, {nf.d}le surmoi : dans les deux cas, une agressivité retournée contre soi.",
        "{-nf}{bilf}Le devoir serait donc le prix de la civilisation. {bilf.1}Il nous protège les uns des autres. "
        "{bilf.2}Mais nous le payons en malaise et en culpabilité. "
        "{bilf.3}Freud ne dit pas qu'il faut tout s'autoriser : il dit qu'un surmoi trop cruel rend malade.",
    ], vis={
        "freud": dict(type="portrait", annee=1856, legende="Malaise dans la civilisation (1930)", img="freud",
                      nom="Sigmund Freud", dates="1856 – 1939", x=110, y=120, w=330, h=420),
        "tab_div": dict(type="tableau", img="dv4-divan", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .6],
                        legende="Le divan de Freud, Freud Museum, Londres (photo Marcelo, domaine public)"),
        "tab_ice": dict(type="tableau", img="t3-iceberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Iceberg dans l'océan Austral (photo NOAA, domaine public)"),
        "topi": dict(type="liste", titre="Le moi et le ça (1923) : trois instances", items=[
            "Le ça : les pulsions, « tout, tout de suite »",
            "Le surmoi : les interdits et les idéaux, « tu dois »",
            "Le moi : pris entre le ça, le surmoi et la réalité"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "orig": dict(type="liste", titre="D'où vient le surmoi ?", items=[
            "Des parents : l'enfant intériorise leurs ordres",
            "La voix qui grondait devient une voix intérieure",
            "Elle reste en grande partie inconsciente"], marques=["→", "→", "→"], x=170, y=170, w=940),
        "tab_jer": dict(type="tableau", img="t6-jerome", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .45],
                        legende="Albrecht Dürer, Saint Jérôme dans son cabinet de travail, 1514 (Met, CC0)"),
        "para": dict(type="def", terme="Le paradoxe du surmoi", cles=["vertueux", "coupable"],
                     t="Plus on est vertueux, plus on se sent coupable : le surmoi est insatiable.",
                     etape="Chaque renoncement le rend plus sévère.", x=170, y=200, w=940),
        "tab_cit": dict(type="tableau", img="dv4-citadelle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="La citadelle de Besançon (photo Groumfy69, CC0)"),
        "mal": dict(type="mot", t="Malaise dans la civilisation", g="Freud, 1930 : le prix de la vie en commun", y=270, taille=64),
        "c_gar": dict(type="cit", a="Freud", o="Malaise dans la civilisation, VII (1930), trad. courante", para=True,
                      x=170, y=150, w=940),
        "nf": dict(type="cols", g="Nietzsche", gq="la mauvaise conscience : les instincts retournés en dedans", d="Freud",
                   dq="le surmoi : une garnison dans la ville conquise", vs="≈"),
        "bilf": dict(type="liste", titre="Le devoir, prix de la civilisation", items=[
            "Il nous protège les uns des autres",
            "Il se paie en malaise, en culpabilité",
            "Un surmoi trop cruel rend malade"], marques=["+", "−", "!"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ IV. l'utilitarisme
    dict(id="utilite", chap="Juger par les conséquences", fond="nuit", humeur="lumiere", notions=["le bonheur", "la justice"],
         retenir="Utilitarisme : une action vaut par ses conséquences, le plus grand bonheur du plus grand nombre. "
                 "Kant : par son intention.", beats=[
        "{bent}{tab_ico}Troisième attaque : elle vient d'Angleterre, et elle est beaucoup plus calme. "
        "À la fin du dix-huitième siècle, le juriste Jeremy Bentham veut une morale simple, presque scientifique. "
        "Elle part d'un constat.",
        ("C", "La nature a placé l'humanité sous l'empire de deux maîtres souverains : la douleur et le plaisir.", "c_ben"),
        "Bentham a même légué son corps à la science : son squelette, habillé, est toujours exposé à Londres.",
        "{-bent}{-c_ben}{-tab_ico}{princ}D'où le principe d'utilité. {princ.1}Une action est bonne si elle augmente le plaisir, "
        "mauvaise si elle augmente la souffrance. {princ.2}Le bonheur de chacun compte, et compte autant que celui des autres. "
        "{princ.3}Le but : le plus grand {#le bonheur}bonheur du plus grand nombre.",
        "{-princ}{opp}Tu vois la différence avec Kant. {opp.g}Pour Kant, une action vaut par son intention : agir par devoir. "
        "{opp.d}Pour l'utilitariste, elle vaut par ses conséquences : le bien qu'elle produit dans le monde.",
        "Mentir est-il mal ? Pour Kant, toujours. Pour Bentham, cela dépend : si un mensonge sauve une vie, il faut mentir.",
        "{-opp}{mill}{tab_soc}John Stuart Mill, qu'on a rencontré dans la série sur la liberté, reprend l'idée en 1861, avec une correction. "
        "Tous les plaisirs ne se valent pas : ceux de l'esprit sont supérieurs à ceux du corps.",
        ("C", "Il vaut mieux être un homme insatisfait qu'un porc satisfait ; il vaut mieux être Socrate insatisfait "
              "qu'un imbécile satisfait.", "c_mill"),
        "{-mill}{-c_mill}{-tab_soc}{tab_aig}{tram}Mais l'utilitarisme a ses vertiges. Pour aller plus loin, voici une expérience de pensée, "
        "proposée par la philosophe Philippa Foot en 1967. {tram.1}Un tramway fou fonce vers cinq ouvriers. "
        "{tram.2}Tu peux actionner un aiguillage : il partira sur une autre voie, où il tuera un seul homme. "
        "{tram.3}La plupart des gens répondent : j'actionne. Cinq vies contre une.",
        "{tram.4}Changeons le décor, comme l'a fait Judith Jarvis Thomson. Tu es sur un pont, à côté d'un homme très corpulent. "
        "Si tu le pousses, son corps arrêtera le tramway. Cinq vies contre une, encore. Et cette fois, presque tout le monde refuse.",
        "{-tram}{-tab_aig}{q_tram}Pourquoi ? Le calcul est le même. Peut-être parce que quelque chose en nous résiste : "
        "on n'a pas le droit de se servir d'un homme comme d'un simple moyen. Tu reconnais Kant.",
        ("La {#la justice}justice ne se réduit peut-être pas à un calcul.", {"rate": "-5%"}),
    ], vis={
        "bent": dict(type="portrait", annee=1748, legende="Introduction aux principes de morale et de législation (1789)",
                     img="bentham", nom="Jeremy Bentham", dates="1748 – 1832", x=110, y=120, w=330, h=420),
        "tab_ico": dict(type="tableau", img="dv4-autoicone", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .5, .3],
                        legende="L'« auto-icône » de Bentham, University College London (photo Karmakolle, CC0)"),
        "c_ben": dict(type="cit", a="Bentham", o="Introduction aux principes de morale et de législation, I, 1 (1789), trad. courante",
                      x=640, y=170, w=570),
        "princ": dict(type="liste", titre="Le principe d'utilité", cles=["utilité"], items=[
            "Bon : ce qui augmente le plaisir ; mauvais : ce qui augmente la souffrance",
            "Le bonheur de chacun compte autant que celui des autres",
            "Le but : le plus grand bonheur du plus grand nombre"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "opp": dict(type="cols", g="Morale du devoir", gq="Kant : l'intention, la règle d'abord", d="Utilitarisme",
                    dq="Bentham, Mill : les conséquences", vs="≠", plus=True),
        "mill": dict(type="portrait", annee=1806, legende="L'Utilitarisme (1861)", img="mill", nom="John Stuart Mill",
                     dates="1806 – 1873", x=110, y=120, w=330, h=420),
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787"),
        "c_mill": dict(type="cit", a="John Stuart Mill", o="L'Utilitarisme, chap. II (1861), trad. courante", x=640, y=170, w=570),
        "tab_aig": dict(type="tableau", img="dv4-aiguillage", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                        legende="Levier d'aiguillage (photo W. Carter, domaine public)"),
        "tram": dict(type="liste", titre="Le dilemme du tramway · pour aller plus loin", items=[
            "Un tramway fou fonce vers cinq ouvriers",
            "Un aiguillage le dévierait vers un seul homme",
            "La plupart actionnent : cinq vies contre une",
            "Pousser un homme du pont ? Presque tous refusent"], marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "q_tram": dict(type="question", t="Cinq vies contre une : pourquoi refusons-nous de pousser l'homme ?"),
    }),

    # ------------------------------------------------------------------ V. les morales du bonheur
    dict(id="bonheur", chap="Les morales du bonheur", fond="aube", humeur="calme",
         notions=["le bonheur", "la nature", "la raison"],
         retenir="Épicure : le plaisir comme absence de trouble, trier ses désirs. Aristote : le bonheur dans la vertu, "
                 "qui s'acquiert par l'habitude.", beats=[
        "{epic}{tab_oli}Dernière attaque, la plus ancienne… et la plus douce. Pour les Grecs, on l'a vu dans l'épisode un, "
        "la grande question n'est pas « que dois-je faire ? », mais « comment vivre heureux ? ». "
        "Vers 306 avant notre ère, Épicure ouvre à Athènes une école dans un jardin.",
        ("C", "C'est pourquoi nous disons que le plaisir est le principe et la fin de la vie bienheureuse.", "c_epi"),
        "{-epic}{-c_epi}{-tab_oli}{tab_rom}{atar}Le plaisir ? Contresens. "
        "Épicure prévient : il ne parle pas des plaisirs des débauchés, mais de l'absence de douleur dans le corps, "
        "et de trouble dans l'âme. Les Grecs appellent cette paix l'ataraxie.",
        "{-atar}{-tab_rom}{tab_cot}{des}Pour y parvenir, il faut trier ses désirs. "
        "{des.1}Les désirs {#la nature}naturels et nécessaires : manger, boire, s'abriter, avoir des amis. "
        "{des.2}Les désirs naturels mais non nécessaires : un repas raffiné. "
        "{des.3}Les désirs vains : la gloire, la richesse sans limite, l'immortalité.",
        "{-des}{tonneaux}Ces derniers sont des tonneaux percés, comme ceux de Calliclès dans la série sur la liberté : "
        "on ne les remplit jamais. Avec du pain et de l'eau, Épicure se disait prêt à rivaliser de bonheur avec Zeus.",
        "{-tonneaux}{-tab_cot}{arist}{tab_hir}Aristote, lui, ne place pas le bonheur dans le plaisir, mais dans l'activité "
        "conforme à la vertu : faire excellemment ce que l'homme fait de propre, vivre selon la raison. "
        "On l'a vu dans l'épisode un : la vertu est un juste milieu, une habitude qui se cultive.",
        "Et cela prend du temps. Comme il le dit, une hirondelle ne fait pas le printemps ; un seul beau jour ne fait pas une vie heureuse.",
        "{-arist}{-tab_hir}{dvb}Voilà la critique la plus profonde. {dvb.g}La morale du devoir demande : qu'est-ce qui est obligatoire ? "
        "{dvb.d}Les morales du bonheur demandent : quelle vie vaut la peine d'être vécue ?",
        "Pour elles, l'homme vertueux fait le bien avec plaisir, comme un musicien joue juste. "
        "Aristote va jusqu'à dire que celui qui n'aime pas agir justement n'est pas vraiment juste.",
        "{-dvb}{kr}Kant répondrait : {kr.1}le bonheur est trop incertain pour fonder une morale : chacun l'imagine à sa façon. "
        "{kr.2}Et un devoir accompli avec joie reste un devoir. Le débat n'est pas clos.",
    ], vis={
        "epic": dict(type="portrait", annee=-341, legende="Lettre à Ménécée (v. 300 av. J.-C.)", img="epicure", nom="Épicure",
                     dates="341 – 270 av. J.-C.", x=110, y=120, w=330, h=420),
        "tab_oli": dict(type="tableau", img="dv4-oliviers", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .55],
                        legende="Oliveraie à Paxos, au lever du soleil (photo Jess Stubenbord, CC0)"),
        "c_epi": dict(type="cit", a="Épicure", o="Lettre à Ménécée, 128-129, trad. courante", x=640, y=170, w=570),
        "tab_rom": dict(type="tableau", img="dv4-romains", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .55],
                        legende="Thomas Couture, Les Romains de la décadence, 1847 (musée d'Orsay)"),
        "atar": dict(type="mot", t="L'ataraxie", g="ni douleur du corps, ni trouble de l'âme", y=270),
        "tab_cot": dict(type="tableau", img="dv4-cotan", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .5],
                        legende="Juan Sánchez Cotán, Coing, chou, melon et concombre, v. 1602 (San Diego Museum of Art)"),
        "des": dict(type="liste", titre="Épicure : trier ses désirs", cles=["naturels", "vains"], items=[
            "Naturels et nécessaires : manger, boire, un abri, des amis",
            "Naturels mais non nécessaires : un repas raffiné",
            "Vains : la gloire, la richesse sans limite"], marques=["✓", "~", "✗"], x=170, y=150, w=940),
        "tonneaux": dict(type="illu", nom="tonneaux", x=140, y=100, w=1000, h=500),
        "arist": dict(type="portrait", annee=-384, legende="Éthique à Nicomaque", img="aristote", nom="Aristote",
                      dates="384 – 322 av. J.-C.", x=110, y=120, w=330, h=420),
        "tab_hir": dict(type="tableau", img="dv4-hirondelle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                        legende="Hirondelle rustique (photo Yerpo, CC BY-SA 4.0)"),
        "dvb": dict(type="cols", g="Morale du devoir", gq="« qu'est-ce qui est obligatoire ? »", d="Morales du bonheur",
                    dq="« quelle vie vaut d'être vécue ? »", vs="≠"),
        "kr": dict(type="liste", titre="La réponse de Kant", items=[
            "Le bonheur est trop incertain pour fonder une morale",
            "Un devoir accompli avec joie reste un devoir"], marques=["→", "→"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Que reste-t-il du devoir après ces quatre attaques ? "
        "{rec.1}Un : pour Nietzsche, la faute vient de la dette ; la mauvaise conscience est une cruauté retournée contre soi.",
        "{rec.2}Deux : pour Freud, le surmoi est la voix intériorisée des parents ; la civilisation se paie en culpabilité.",
        "{rec.3}Trois : pour les utilitaristes, une action se juge à ses conséquences. Le tramway en montre les limites.",
        "{rec.4}Quatre : pour Épicure et Aristote, la vraie question est celle de la vie heureuse.",
        "{-rec}{frise}Le devoir n'est pas mort. Mais il a perdu son innocence : on ne peut plus dire « tu dois » sans se demander qui parle.",
        ("Et quand deux devoirs se contredisent ? Ce sera l'épisode cinq.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-frise}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="CONTRE LE DEVOIR", branches=[
            dict(t="Nietzsche", items=["faute = dette", "mauvaise conscience", "le lion : « Je veux »"]),
            dict(t="Freud", items=["le surmoi", "la garnison intérieure"]),
            dict(t="Utilitarisme", items=["les conséquences", "le tramway"]),
            dict(t="Le bonheur", items=["Épicure : l'ataraxie", "Aristote : la vertu"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Aristote", d=-384, img="aristote"), dict(nom="Épicure", d=-341, img="epicure"),
            dict(nom="Kant", d=1724, img="kant"), dict(nom="Bentham", d=1748, img="bentham"),
            dict(nom="Mill", d=1806, img="mill"), dict(nom="Nietzsche", d=1844, img="nietzsche"),
            dict(nom="Freud", d=1856, img="freud")]),
        "tab_fin": dict(type="tableau", img="dv4-antigone", fond=True, sombre=True, de=[1.0, .4, .45], a=[1.25, .3, .4],
                        legende="Nikiphoros Lytras, Antigone devant Polynice mort, 1865 (photo Francesco Bini, CC BY-SA 4.0)"),
        "fin": dict(type="titre", sur="À suivre", t="Conflits de devoirs", sous="Épisode 5 · Antigone, la désobéissance, Eichmann"),
    }),
]

QUIZ = [
    dict(q="Selon Nietzsche, d'où vient le concept moral de « faute » ?",
         r=["Du commandement divin", "Du concept très matériel de « dette »", "De la raison pratique", "De l'instinct de pitié"], ok=1,
         voir="c_schuld", ex="En allemand, Schuld (la faute) et Schulden (les dettes) : le coupable est d'abord un débiteur qui paie de sa souffrance."),
    dict(q="Qu'est-ce que la « mauvaise conscience » selon Nietzsche ?",
         r=["La voix de Dieu en nous", "Les instincts agressifs retournés contre soi",
            "Le regret d'une erreur de calcul", "La peur du gendarme"], ok=1,
         voir="mc", ex="Enfermés dans la société, les instincts qui ne peuvent plus sortir se retournent en dedans : l'homme devient son propre bourreau."),
    dict(q="Dans la fable de Zarathoustra, que répond le lion au dragon « Tu dois » ?",
         r=["« Je peux »", "« Je veux »", "« Je dois aussi »", "« Je pense »"], ok=1,
         voir="meta", ex="Le chameau porte les devoirs, le lion les refuse (« Je veux »), l'enfant crée de nouvelles valeurs."),
    dict(q="Pour Freud, d'où vient le surmoi ?",
         r=["De l'intériorisation des ordres et des interdits des parents", "De la raison universelle",
            "Des pulsions du ça", "D'un contrat entre citoyens"], ok=0,
         voir="orig", ex="La voix qui grondait devient une voix intérieure, en grande partie inconsciente."),
    dict(q="Quelle image Freud emploie-t-il pour le surmoi dans Malaise dans la civilisation ?",
         r=["Un iceberg", "Une garnison dans une ville conquise", "Un cocher et deux chevaux", "Un tribunal de la raison"], ok=1,
         voir="c_gar", ex="La civilisation fait surveiller l'individu par une instance en lui-même, comme par une garnison placée dans une ville conquise."),
    dict(q="Pour un utilitariste, une action est bonne si…",
         r=["elle est faite par devoir", "elle produit le plus grand bonheur du plus grand nombre",
            "elle respecte les commandements", "elle exprime la volonté du plus fort"], ok=1,
         voir="princ", ex="Le principe d'utilité de Bentham : juger par les conséquences, pas par l'intention (contrairement à Kant)."),
    dict(q="Pourquoi presque tout le monde refuse-t-il de pousser l'homme du pont, dans le dilemme du tramway ?",
         r=["Parce que le calcul donne un autre résultat", "Parce qu'on refuse de se servir d'un homme comme d'un simple moyen",
            "Parce que le tramway ne s'arrêterait pas", "Parce que la loi l'interdit"], ok=1,
         voir="tram", ex="Le calcul est le même (cinq vies contre une) : une intuition kantienne résiste au calcul utilitariste."),
    dict(q="Pour Épicure, le plaisir qui est « le principe et la fin de la vie bienheureuse », c'est…",
         r=["la fête et l'abondance", "l'absence de douleur du corps et de trouble de l'âme",
            "la gloire", "la satisfaction de tous les désirs"], ok=1,
         voir="c_epi", ex="L'ataraxie : on y parvient en triant ses désirs (naturels et nécessaires, naturels non nécessaires, vains)."),
]

CREDITS = [
    "Portraits : Nietzsche (photographie de Gustav Schultze, 1882) ; Freud (photographie de Max Halberstadt, vers 1921) ; "
    "Jeremy Bentham (Henry William Pickersgill, 1829, National Portrait Gallery) ; Épicure (buste, Palazzo Massimo, Rome) ; "
    "John Stuart Mill ; Aristote (buste, Palazzo Altemps, photo Jastrow) ; Kant : domaine public",
    "Tableaux et gravures : Matthias Stom, Jeune homme lisant à la chandelle ; Edvard Munch, Le Cri (1893) ; "
    "Pieter Bruegel l'Ancien (d'après), La Justice (1559, Rijksmuseum, CC0) ; Gilbert Stuart Newton, Shylock et Jessica (1830) ; "
    "Füssli, Le Cauchemar (1781) ; Jacques-Louis David, Léonidas aux Thermopyles (1814) et La Mort de Socrate (1787) ; "
    "Jean-Léon Gérôme, La Dernière Prière des martyrs chrétiens et Lion cherchant à saisir un papillon ; "
    "Chardin, L'Enfant au toton (1738) ; Dürer, Saint Jérôme dans son cabinet (1514, Met, CC0) ; "
    "Thomas Couture, Les Romains de la décadence (1847) ; Juan Sánchez Cotán, Coing, chou, melon et concombre (v. 1602) : domaine public",
    "Photographies : Sils-Maria (Hansueli Krapf, CC BY-SA 4.0) ; caravane (Van Achterberg, ASC Leiden, CC BY-SA 4.0) ; "
    "divan de Freud (Marcelo, domaine public) ; iceberg (NOAA, domaine public) ; citadelle de Besançon (Groumfy69, CC0) ; "
    "auto-icône de Bentham (Karmakolle, CC0) ; levier d'aiguillage (W. Carter, domaine public) ; oliveraie de Paxos (Jess Stubenbord, CC0) ; "
    "hirondelle (Yerpo, CC BY-SA 4.0) ; Lytras, Antigone devant Polynice mort (1865, photo Francesco Bini, CC BY-SA 4.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
