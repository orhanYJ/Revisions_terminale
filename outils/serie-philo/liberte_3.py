"""La liberté, épisode 3 : « Et si c'était une illusion ? »

Même format que liberte_1.py (voir l'en-tête de ce fichier) : beats lus, repères {id} / {-id} / {id.k} / {!mot},
citations ("C", texte, id), visuels par scène.
"""

CODE = "liberte-3"
NOTION = "La liberté"
NUM = 3
TITRE = "Et si c'était une illusion ?"
SUIVANT = "Épisode 4 · Se libérer : les stoïciens, Spinoza, Kant"

PRONONCIATION = {"Nietzsche": "Nitche", "Holbach": "Olbak", "Libet": "Libette", "Durkheim": "Durkème", "Charcot": "Charko"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_cha}Paris, à la fin du dix-neuvième siècle. Dans les amphithéâtres de la Salpêtrière, puis à Nancy, "
        "des médecins font une expérience troublante : {hyp}la suggestion sous hypnose.",
        "{-hyp}{etapes}Voici, en substance, ce qu'on y observe. {etapes.1}On endort un patient. On lui donne un ordre : "
        "« À ton réveil, quand je frapperai dans mes mains, tu iras ouvrir la fenêtre. » "
        "{etapes.2}Puis on le réveille. Il ne se souvient de rien.",
        "{etapes.3}Le médecin frappe dans ses mains. Le patient se lève… et ouvre la fenêtre.",
        ("P", 0.5),
        "{etapes.4}On lui demande pourquoi. Il répond, très sûr de lui : « Il fait chaud, ici. »",
        ("P", 0.6),
        "{-etapes}{q_pat}Il se sent libre. Il a même une raison. Mais la vraie cause de son geste… "
        "il l'{!ignore}ignore complètement.",
        ("Un jeune médecin viennois assiste à ces séances. Il s'appelle Sigmund Freud. Il ne les oubliera jamais.",
         {"rate": "-4%"}),
        "{-q_pat}{-tab_cha}{q1}Et si nous étions tous ce patient ? Si chacun de nos choix avait des causes que nous ne voyons pas ? "
        "Dans l'épisode deux, Descartes et Sartre nous disaient : tu es libre, absolument. "
        "Aujourd'hui, place à ceux qui en doutent.",
        ("P", 0.3),
        "{-q1}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_cha": dict(type="tableau", img="t3-charcot", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .7, .45],
                        legende="André Brouillet, Une leçon clinique à la Salpêtrière, 1887 · Charcot présente une patiente"),
        "hyp": dict(type="mot", t="L'hypnose", g="la suggestion qui agit… à l'insu du sujet", y=250, taille=100),
        "etapes": dict(type="liste", titre="L'expérience", items=[
            "Sous hypnose : « À mon signal, tu ouvriras la fenêtre. »",
            "Au réveil : aucun souvenir de l'ordre",
            "Le signal : il se lève, il ouvre",
            "« Pourquoi ? » — « Il fait chaud, ici. »"], marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "q_pat": dict(type="question", t="Une raison… mais pas la vraie cause"),
        "q1": dict(type="question", t="Et si nous étions tous ce patient ?"),
        "titre": dict(type="titre", sur="La liberté · Épisode 3", t="Et si c'était une illusion ?",
                      sous="Spinoza, Freud, les sciences humaines"),
    }),

    # ------------------------------------------------------------------ I. Spinoza
    dict(id="spinoza", chap="La pierre de Spinoza", fond="aube", humeur="mystere",
         retenir="Pour Spinoza, se croire libre, c'est être conscient de ses désirs et ignorant de leurs causes.", beats=[
        "{spino}{tab_exc}Commençons par le plus radical. Baruch Spinoza, Amsterdam, dix-septième siècle. "
        "À vingt-trois ans, il est chassé de sa communauté pour ses idées. Il vivra modestement, en polissant des verres de lunettes.",
        "{-tab_exc}{tab_eth}Son grand livre, l'Éthique, part d'une idée simple et vertigineuse : {nat}tout ce qui existe "
        "fait partie d'une seule et même réalité, qu'il appelle Dieu, ou la Nature. Et dans la Nature, {nat.1}rien n'arrive sans cause.",
        "{nat.2}Pas d'exception. Pas même pour l'homme. L'homme n'est pas, dit Spinoza, {!empire}un empire dans un empire.",
        "{-nat}{lance}Tu te souviens de sa pierre ? Lancée en l'air, elle continue son mouvement. {lance.1}Si elle pouvait penser, "
        "{lance.2}elle se croirait libre : elle est consciente de son effort, pas de la main qui l'a lancée. "
        "Spinoza l'écrit dans une lettre de 1674.{-lance}",
        ("C", "Telle est cette liberté humaine que tous se vantent de posséder et qui consiste en cela seul que les hommes "
              "sont conscients de leurs désirs et ignorants des causes qui les déterminent.", "c_spi"),
        "{-c_spi}{-spino}{exs}Et il multiplie les exemples. {exs.1}L'enfant croit désirer librement le lait. "
        "{exs.2}L'enfant en colère croit vouloir librement se venger. {exs.3}L'homme ivre croit parler par une libre décision… "
        "et regrette, une fois dégrisé, ce qu'il aurait voulu taire.",
        "{-exs}{def_ill}Voilà le cœur de l'argument. {def_ill.1}Le sentiment de liberté ne prouve rien : il naît précisément de "
        "notre ignorance. Nous voyons nos désirs ; nous ne voyons pas ce qui les produit.",
        ("Plus nous ignorons les causes… plus nous nous croyons libres.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{rep_cs}Retiens ici un repère : croire et savoir. Se sentir libre, c'est une croyance, vécue de l'intérieur. "
        "Savoir si on l'est vraiment, c'est une autre affaire. Et le sentiment, à lui seul, ne suffit pas à le prouver.",
        "{-def_ill}{-rep_cs}{-tab_eth}{tab_orr}{laplace}Un siècle plus tard, les savants poussent l'idée jusqu'au bout. "
        "Le baron d'Holbach écrit que l'homme n'est libre à aucun instant de sa vie. "
        "Et le mathématicien Laplace imagine une intelligence qui connaîtrait toutes les forces de la nature, "
        "et la position de chaque atome.",
        ("C", "Rien ne serait incertain pour elle, et l'avenir, comme le passé, serait présent à ses yeux.", "c_lap"),
        "{-laplace}{-c_lap}{-tab_orr}{rep_det}C'est ce qu'on appelle le {!déterminisme}déterminisme : "
        "tout ce qui arrive est l'effet nécessaire de ce qui précède. Si c'est vrai… mes choix étaient écrits avant moi.",
        ("P", 0.6),
    ], vis={
        "spino": dict(type="portrait", annee=1632, legende="Éthique (1677)", img="spinoza", nom="Baruch Spinoza",
                      dates="1632 – 1677", x=110, y=120, w=330, h=420),
        "tab_exc": dict(type="tableau", img="t3-spinoza-exc", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .5],
                        legende="Samuel Hirszenberg, Spinoza excommunié, 1907"),
        "tab_eth": dict(type="tableau", img="t-ethica", fond=True, sombre=True, de=[1.0, 0.5, 0.3], a=[1.3, 0.5, 0.45],
                        legende="Spinoza, Ethica, dans les Opera posthuma, 1677"),
        "nat": dict(type="def", cles=["cause", "empire"], terme="Spinoza · Dieu, ou la Nature",
                    t="Une seule réalité, où rien n'arrive sans cause.",
                    etape="L'homme n'est pas « un empire dans un empire » : il suit les lois de la Nature, comme tout le reste.",
                    x=640, y=170, w=570),
        "lance": dict(type="illu", nom="lance", x=600, y=150, w=660, h=434),
        "c_spi": dict(type="cit", a="Spinoza", o="Lettre 58 à Schuller, octobre 1674 (trad. Appuhn)", x=640, y=150, w=570),
        "exs": dict(type="liste", titre="Ils se croient libres…", items=[
            "L'enfant qui désire le lait", "L'enfant en colère qui veut se venger",
            "L'homme ivre qui parle… et le regrette"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "def_ill": dict(type="def", cles=["ignorance", "causes"], terme="L'illusion du libre arbitre",
                        t="Se croire libre = être conscient de ses désirs + ignorer les causes qui les produisent.",
                        etape="Le sentiment de liberté ne prouve rien : il naît de notre ignorance.", x=170, y=190, w=940),
        "rep_cs": dict(type="tag", style="repere", t="Repère · croire / savoir", x=170, y=560, w=420),
        "tab_orr": dict(type="tableau", img="t3-orrery", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Joseph Wright of Derby, Un philosophe expliquant le planétaire, v. 1766"),
        "laplace": dict(type="tag", style="plus", t="Pour aller plus loin · d'Holbach (1770), Laplace (1814)",
                        x=170, y=560, w=640),
        "c_lap": dict(type="cit", a="Laplace", o="Essai philosophique sur les probabilités (1814)", x=170, y=170, w=940),
        "rep_det": dict(type="def", cles=["nécessaire", "précède"], terme="Le déterminisme",
                        t="Tout ce qui arrive est l'effet nécessaire de ce qui précède.",
                        etape="Repère · nécessaire / contingent : s'il n'y a pas de contingent, il n'y a pas de libre arbitre.",
                        x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. Freud
    dict(id="freud", chap="L'inconscient", fond="nuit", humeur="tension",
         retenir="Freud : le moi n'est pas maître dans sa propre maison. Une part de nous agit à notre insu.", beats=[
        "{freud}{tab_goy}Revenons à notre jeune médecin viennois. Sigmund Freud a vu, à la Salpêtrière et à Nancy, "
        "qu'une idée pouvait agir en nous sans que nous le sachions. Il va en tirer une théorie : {!inconscient}l'inconscient.",
        "{-tab_goy}{-freud}{bless}En 1917, Freud raconte l'histoire de l'humanité comme une suite de trois blessures d'amour-propre. "
        "{bless.1}{tab_cop}La première, avec Copernic : la Terre n'est plus le centre de l'univers.",
        "{-tab_cop}{tab_dar}{bless.2}La deuxième, avec Darwin : l'homme n'est plus à part du règne animal ; il descend d'une longue série d'espèces.",
        "{-tab_dar}{bless.3}La troisième… c'est la sienne. La psychanalyse montre à l'homme que, même chez lui, dans son propre esprit, "
        "il ne commande pas.{-bless}",
        ("C", "Le moi n'est pas maître dans sa propre maison.", "c_freud"),
        "{-c_freud}{tab_ice}{ice}On représente souvent l'esprit, selon Freud, comme un iceberg. "
        "{ice.g}La partie visible, c'est la conscience. {ice.d}Sous l'eau, bien plus vaste, il y a l'inconscient : "
        "des désirs refoulés, des souvenirs oubliés, des peurs d'enfance.",
        "{-ice}{refoul}Pourquoi ces désirs restent-ils cachés ? Parce qu'ils sont inacceptables pour la conscience : honteux, interdits, "
        "douloureux. {refoul.1}Alors l'esprit les repousse hors de la conscience. Freud appelle cela {!refoulement}le refoulement. "
        "Mais ce qui est refoulé ne disparaît pas : il cherche à revenir, déguisé.",
        "{-refoul}{-ice}{-tab_ice}{signes}Comment le savoir, si c'est caché ? Par ses traces. {signes.1}Le lapsus, quand un mot en remplace un autre. "
        "{signes.2}L'acte manqué : tu oublies, comme par hasard, le rendez-vous qui t'ennuyait. "
        "{signes.3}{tab_cau}Le rêve, que Freud appelle la voie royale vers l'inconscient. {signes.4}Et les symptômes névrotiques.",
        "{-tab_cau}{-signes}{exl}Prends un exemple. Le président de la Chambre des députés autrichienne ouvre la séance en disant : "
        "{exl.1}« Je déclare la séance close. » Il voulait dire : ouverte. Freud rapporte ce lapsus célèbre.",
        ("Le mot lui a échappé. Mais il disait, peut-être, ce qu'il souhaitait vraiment.", {"rate": "-5%"}),
        "{-exl}{cons}Conséquence pour la liberté : {cons.1}je crois choisir mon métier, mon amour, mes peurs… "
        "{cons.2}mais des forces que j'ignore travaillent dans mon dos. Comme le patient de l'hypnose, "
        "je me donne de bonnes raisons après coup.",
        "{-cons}{sartre_obj}Pour aller plus loin : Sartre, le héros de l'épisode deux, refusera cette idée. "
        "Pour lui, dire « c'est mon inconscient », c'est se trouver une excuse : c'est encore de la mauvaise foi. "
        "Le débat reste ouvert, et il est excellent pour une copie.",
        ("P", 0.6),
    ], vis={
        "sartre_obj": dict(type="cols", g="Freud", gq="l'inconscient agit à mon insu", d="Sartre",
                           dq="invoquer l'inconscient, c'est de la mauvaise foi", vs="↔", plus=True),
        "freud": dict(type="portrait", annee=1856, legende="Introduction à la psychanalyse (1917)", img="freud",
                      nom="Sigmund Freud", dates="1856 – 1939", x=110, y=120, w=330, h=420),
        "tab_goy": dict(type="tableau", img="t3-goya", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .3],
                        legende="Francisco Goya, Le sommeil de la raison engendre des monstres, Caprices, 1799"),
        "bless": dict(type="liste", titre="Les trois blessures de l'amour-propre", items=[
            "Copernic : la Terre n'est pas le centre de l'univers",
            "Darwin : l'homme est issu du règne animal",
            "Freud : le moi ne commande pas chez lui"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_cop": dict(type="tableau", img="t3-copernic", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .35],
                        legende="Jan Matejko, L'Astronome Copernic, ou la conversation avec Dieu, 1873"),
        "tab_dar": dict(type="tableau", img="t3-darwin", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .2],
                        legende="Darwin en singe, caricature de la revue The Hornet, 1871"),
        "c_freud": dict(type="cit", a="Freud", o="Une difficulté de la psychanalyse (1917 ; trad. 1933)",
                        x=170, y=200, w=940),
        "tab_ice": dict(type="tableau", img="t3-iceberg", fond=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Iceberg dans l'océan Austral (photo NOAA, domaine public)"),
        "ice": dict(type="cols", g="La conscience", gq="la partie visible : ce que je sais de moi", d="L'inconscient",
                    dq="sous la surface, bien plus vaste : désirs refoulés, souvenirs, peurs", vs="⇣",
                    repere="Repère · conscience / inconscient"),
        "refoul": dict(type="def", cles=["inacceptables", "refoulement"], terme="Le refoulement",
                       t="Les désirs inacceptables pour la conscience sont repoussés hors d'elle… sans disparaître.",
                       etape="Le refoulé cherche à revenir, déguisé : lapsus, rêves, symptômes.", x=170, y=190, w=940),
        "signes": dict(type="liste", titre="Les traces de l'inconscient", items=[
            "Le lapsus : un mot pour un autre", "L'acte manqué : l'oubli « par hasard »",
            "Le rêve : « la voie royale »", "Le symptôme névrotique"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "tab_cau": dict(type="tableau", img="t3-cauchemar", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .5],
                        legende="Johann Heinrich Füssli, Le Cauchemar, 1781"),
        "exl": dict(type="dialogue", lignes=["« Je déclare la séance close. »"],
                    src="lapsus rapporté par Freud, Psychopathologie de la vie quotidienne (1901)", x=170, y=200, w=940),
        "cons": dict(type="liste", titre="Et la liberté ?", items=[
            "Je crois choisir : métier, amours, peurs…",
            "… mais des forces ignorées agissent, et je me trouve des raisons après coup"],
                     marques=["?", "→"], x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ III. sciences humaines
    dict(id="societe", chap="La société en nous", fond="aube", humeur="tension",
         retenir="Marx, Durkheim, Bourdieu : nos idées et nos goûts portent la marque de notre place dans la société.", beats=[
        "{q_soc}Mais l'inconscient n'est pas la seule force cachée. Il y a aussi… les autres. La société entière.",
        "{-q_soc}{tab_usi}{marx}Au dix-neuvième siècle, Karl Marx observe les ouvriers des usines. Ce qu'ils pensent, "
        "ce qu'ils croient juste, ce qu'ils trouvent naturel… dépend de leur condition matérielle.",
        ("C", "Ce n'est pas la conscience des hommes qui détermine leur être ; c'est inversement leur être social "
              "qui détermine leur conscience.", "c_marx"),
        "{-c_marx}{ideo}C'est ce que Marx appelle l'{!idéologie}idéologie : les idées dominantes d'une époque sont, le plus souvent, "
        "celles de la classe qui domine. {ideo.1}Le travailleur qui trouve normal son sort pense avec des idées "
        "qui ne sont pas vraiment les siennes.",
        "{-ideo}{-marx}{-c_marx}{-tab_usi}{tab_rue}{durk}Quelques décennies plus tard, Émile Durkheim fonde la sociologie avec une règle : "
        "étudier les faits sociaux comme des choses.",
        "{-durk}{def_fs}Un fait social, c'est une façon d'agir, de penser ou de sentir qui existe hors de l'individu "
        "{def_fs.1}et qui s'impose à lui. La langue que tu parles, la mode que tu suis, la politesse : tu ne les as pas inventées.",
        "Durkheim montre même que le suicide, l'acte en apparence le plus personnel qui soit, varie selon les époques, "
        "les pays, les religions, avec une régularité troublante.",
        "{-def_fs}{-tab_rue}{tab_eco}{bour}Plus près de nous, Pierre Bourdieu parle d'{!habitus}habitus : "
        "{bour.1}des manières d'être, des goûts, des façons de parler, acquis dans la famille et à l'école, "
        "{bour.2}qui deviennent une seconde nature.",
        "{bour.3}Ce que tu aimes écouter, les études que tu trouves faites pour toi, ta façon de te tenir… "
        "tout cela te semble venir de toi. Mais statistiquement, on peut souvent le prédire à partir de ton milieu.",
        "Dans Les Héritiers, en 1964, Bourdieu et Passeron montrent que la réussite à l'université dépend fortement du milieu "
        "d'origine. Ce qu'on prend pour un don personnel est souvent un héritage.",
        "{-bour}{-tab_eco}{tab_pin}{mario}D'où la question qui fâche : sommes-nous des {!marionnettes}marionnettes, "
        "tirées par des fils que nous ne voyons pas ?",
        ("P", 0.6),
    ], vis={
        "q_soc": dict(type="question", t="Et si les autres pensaient en nous ?"),
        "tab_usi": dict(type="tableau", img="t3-usine", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .55],
                        legende="Adolph von Menzel, La Forge (Le Laminoir), 1872-1875"),
        "marx": dict(type="portrait", annee=1818, legende="Contribution à la critique de l'économie politique (1859)",
                     img="marx", nom="Karl Marx", dates="1818 – 1883", x=110, y=120, w=330, h=420),
        "c_marx": dict(type="cit", a="Marx", o="Contribution à la critique de l'économie politique, préface (1859)",
                       x=640, y=150, w=570),
        "ideo": dict(type="def", cles=["dominantes", "siennes"], terme="Marx · l'idéologie",
                     t="Les idées dominantes d'une époque sont, le plus souvent, celles de la classe dominante.",
                     etape="On peut penser avec des idées qui ne sont pas vraiment les siennes.", x=640, y=170, w=570),
        "tab_rue": dict(type="tableau", img="t3-rue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Gustave Caillebotte, Rue de Paris, temps de pluie, 1877"),
        "durk": dict(type="portrait", annee=1858, legende="Les Règles de la méthode sociologique (1895)", img="durkheim",
                     nom="Émile Durkheim", dates="1858 – 1917", x=110, y=120, w=330, h=420),
        "def_fs": dict(type="def", cles=["extérieure", "impose"], terme="Durkheim · le fait social",
                       t="Une manière d'agir, de penser ou de sentir, extérieure à l'individu, et qui s'impose à lui.",
                       etape="La langue, la mode, la politesse… et même les taux de suicide (Le Suicide, 1897).",
                       x=170, y=180, w=940),
        "tab_eco": dict(type="tableau", img="t3-ecole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .5],
                        legende="Albert Anker, L'École de village en 1848, 1896"),
        "bour": dict(type="def", cles=["goûts", "nature"], terme="Bourdieu · l'habitus",
                     t="Des goûts, des manières d'être et de parler, acquis dans son milieu, devenus une seconde nature.",
                     etape="Ils semblent venir de moi… mais on peut souvent les prédire à partir de mon milieu.",
                     x=170, y=190, w=940),
        "tab_pin": dict(type="tableau", img="t3-pinocchio", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .25],
                        legende="Enrico Mazzanti, Pinocchio, illustration de l'édition originale, 1883"),
        "mario": dict(type="question", t="Sommes-nous des marionnettes ?"),
    }),

    # ------------------------------------------------------------------ IV. le cerveau (pour aller plus loin)
    dict(id="cerveau", chap="Le cerveau a-t-il décidé avant moi ?", fond="nuit", humeur="mystere",
         retenir="Libet : une activité cérébrale précède la conscience de vouloir. Mais l'expérience prouve moins qu'on ne le dit.", beats=[
        "{tab_ves}{libet}Dernier soupçon, venu des neurosciences. En 1983, le neurologue américain Benjamin Libet "
        "demande à des volontaires de plier le poignet quand ils le veulent, et de noter l'instant exact où ils en ont eu l'intention.",
        "{-libet}{chrono}Pendant ce temps, des électrodes enregistrent leur cerveau. Résultat : {chrono.1}une activité cérébrale "
        "commence environ une demi-seconde avant le geste… {chrono.2}mais les volontaires ne prennent conscience de vouloir "
        "qu'à peine deux dixièmes de seconde avant. {chrono.3}Le cerveau semble avoir commencé… avant moi.",
        ("Alors, c'est réglé ? Le libre arbitre, une simple illusion du cerveau ?", {"pitch": "+2Hz"}),
        "{-chrono}{lim}Pas si vite. {lim.1}Le geste étudié est minuscule et sans enjeu : plier le poignet, ce n'est pas choisir sa vie. "
        "{lim.2}Libet lui-même remarquait qu'on garde le temps de dire non, d'opposer un veto au geste qui se prépare. "
        "{lim.3}Et des chercheurs ont montré depuis que ce signal pourrait n'être qu'un bruit de fond du cerveau, "
        "pas une décision déjà prise.",
        "{rep_sc}Retiens la leçon de méthode : une expérience scientifique décrit des mécanismes. "
        "Elle ne tranche pas, à elle seule, une question philosophique.",
        ("P", 0.5),
    ], vis={
        "tab_ves": dict(type="tableau", img="t3-vesale", fond=True, sombre=True, de=[1.0, .5, .2], a=[1.25, .5, .15],
                        legende="André Vésale, De humani corporis fabrica, 1543 (Wellcome Collection, CC BY 4.0)"),
        "libet": dict(type="mot", t="Libet, 1983", g="« Pliez le poignet quand vous le voulez »", y=230, taille=96),
        "chrono": dict(type="liste", titre="L'expérience de Libet", items=[
            "≈ −0,5 s : une activité cérébrale commence",
            "≈ −0,2 s : « je veux bouger » (conscience)",
            "0 s : le geste"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "lim": dict(type="liste", titre="Ses limites", items=[
            "Un geste minuscule, sans enjeu",
            "Le veto : on peut encore dire non",
            "Le signal n'est peut-être qu'un bruit de fond"], marques=["✗", "✗", "✗"], x=170, y=170, w=940, plus=True),
        "rep_sc": dict(type="tag", style="copie", t="Copie · une expérience décrit des mécanismes, elle ne tranche pas seule",
                       x=170, y=560, w=780),
    }),

    # ------------------------------------------------------------------ V. le soupçon et la réponse
    dict(id="reponse", chap="Alors, tout est joué ?", fond="aube", humeur="calme",
         retenir="Déterminisme ≠ fatalisme : connaître ses déterminismes, c'est le premier pas vers la libération.", beats=[
        "{nietz}{tab_min}Avant de conclure, un dernier soupçon, plus féroce. Pour Friedrich Nietzsche, si l'on tient tant au libre arbitre, "
        "ce n'est pas parce qu'il est vrai. C'est parce qu'il est utile… pour juger.",
        ("C", "Les hommes ont été considérés comme « libres », pour pouvoir être jugés et punis.", "c_nietz"),
        "{-nietz}{-c_nietz}{-tab_min}{q_resp}Alors faut-il tout abandonner ? Plus de responsabilité, plus de mérite, plus de faute ? "
        "Pas si vite. Trois réponses.",
        "{-q_resp}{tab_oed}{fat}Première réponse : {fat.g}le fatalisme dit que tout arrivera, quoi que je fasse. "
        "C'est Œdipe, qui fuit l'oracle… et l'accomplit en le fuyant. {fat.d}Le déterminisme dit autre chose : "
        "tout a une cause, et mes actes en font partie. Ma décision n'est pas inutile : elle est elle-même une cause.",
        "{-fat}{-tab_oed}{conn}Deuxième réponse : {conn.1}Spinoza ne s'arrête pas à l'illusion. Comprendre les causes qui me déterminent, "
        "c'est déjà cesser de les subir aveuglément. {conn.2}Freud non plus : la cure psychanalytique consiste à rendre conscient "
        "ce qui était inconscient, pour que le moi regagne du terrain. {conn.3}Et la sociologie, en me montrant ce qui me façonne, "
        "me donne une prise sur lui.",
        "{-conn}{tab_pen}{subj}Troisième réponse : {subj.1}même celui qui nie la liberté continue de délibérer, de peser, de choisir. "
        "On ne peut pas vivre comme une pierre qui tombe.",
        ("Les déterminismes ne prouvent peut-être pas que nous ne sommes pas libres. Ils prouvent que la liberté "
         "n'est pas donnée d'avance.", {"rate": "-5%"}),
        "{-subj}{-tab_pen}{copie}Et dans ta copie ? Ces auteurs sont parfaits pour la partie qui doute : celle où l'on montre que "
        "le sentiment d'être libre peut tromper. À condition de ne pas s'arrêter là, et de dépasser le soupçon.",
        "{-copie}{tab_cop2}{pivot}Elle n'est pas un point de départ… {pivot.1}mais peut-être un point d'arrivée. "
        "Non pas un fait, mais une {!conquête}conquête. Et c'est exactement le sujet de l'épisode quatre.",
        ("P", 0.8),
    ], vis={
        "nietz": dict(type="portrait", annee=1844, legende="Crépuscule des idoles (1888)", img="nietzsche",
                      nom="Friedrich Nietzsche", dates="1844 – 1900", x=110, y=120, w=330, h=420),
        "tab_min": dict(type="tableau", img="t3-minos", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .65, .4],
                        legende="Gustave Doré, Minos, le juge des Enfers, pour L'Enfer de Dante, 1861"),
        "c_nietz": dict(type="cit", a="Nietzsche", o="Crépuscule des idoles, « Les quatre grandes erreurs », § 7 (1888 ; trad. H. Albert)",
                        x=640, y=170, w=570),
        "q_resp": dict(type="question", t="Plus de liberté… plus de responsabilité ?"),
        "tab_oed": dict(type="tableau", img="t3-oedipe", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .55, .35],
                        legende="Jean-Auguste-Dominique Ingres, Œdipe explique l'énigme du Sphinx, 1808"),
        "fat": dict(type="cols", g="Fatalisme", gq="tout arrivera, quoi que je fasse (Œdipe)", d="Déterminisme",
                    dq="tout a une cause… et mes décisions sont des causes", vs="≠", repere="À ne pas confondre"),
        "conn": dict(type="liste", titre="Connaître pour se libérer", items=[
            "Spinoza : comprendre les causes, c'est cesser de les subir aveuglément",
            "Freud : rendre conscient ce qui était inconscient",
            "La sociologie : voir ce qui me façonne, pour avoir prise sur lui"], marques=["1", "2", "3"],
                     x=170, y=150, w=940),
        "tab_pen": dict(type="tableau", img="t-penseur", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Auguste Rodin, Le Penseur, détail de La Porte de l'Enfer, musée Rodin (photo Jebulon, CC0)"),
        "subj": dict(type="def", cles=["délibérer", "pierre"], terme="L'argument de l'expérience vécue",
                     t="Même celui qui nie la liberté continue de délibérer et de choisir.",
                     etape="On ne peut pas vivre comme une pierre qui tombe.", x=170, y=210, w=940),
        "copie": dict(type="def", cles=["doute", "dépasser"], terme="Réflexe copie",
                      t="Spinoza, Freud, Marx, Durkheim, Bourdieu : la partie qui doute du sentiment d'être libre.",
                      etape="Ne pas s'arrêter au soupçon : le dépasser (épisode 4).", x=170, y=200, w=940),
        "tab_cop2": dict(type="tableau", img="t3-copernic", fond=True, sombre=True, de=[1.15, .45, .3], a=[1.0, .5, .45],
                         legende="Jan Matejko, L'Astronome Copernic, ou la conversation avec Dieu, 1873"),
        "pivot": dict(type="cols", g="Un point de départ ?", gq="la liberté donnée, évidente", d="Un point d'arrivée",
                      dq="la liberté conquise, par la connaissance", vs="→"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : pour Spinoza, se croire libre, c'est être conscient de ses désirs "
        "et ignorant de leurs causes.",
        "{rec.2}Deux : avec Freud, le moi n'est pas maître dans sa propre maison : l'inconscient agit à notre insu.",
        "{rec.3}Trois : Marx, Durkheim et Bourdieu montrent la société à l'œuvre dans nos idées et nos goûts.",
        "{rec.4}Quatre : le déterminisme n'est pas le fatalisme. Et connaître ses déterminismes, c'est commencer à s'en libérer.",
        "{-rec}{frise}À toi maintenant : les questions t'attendent sous la vidéo.",
        ("La prochaine fois… nous chercherons comment devenir libre.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-frise}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="UNE ILLUSION ?", branches=[
            dict(t="Spinoza", items=["conscients de nos désirs", "ignorants des causes", "déterminisme (Laplace)"]),
            dict(t="Freud", items=["l'inconscient", "« le moi n'est pas maître… »", "lapsus, rêves, actes manqués"]),
            dict(t="La société en nous", items=["Marx : l'être social", "Durkheim : le fait social", "Bourdieu : l'habitus"]),
            dict(t="La réponse", items=["déterminisme ≠ fatalisme", "connaître pour se libérer", "Libet, Nietzsche : deux soupçons"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Spinoza", d=1632, img="spinoza"), dict(nom="Laplace", d=1749),
            dict(nom="Marx", d=1818, img="marx"), dict(nom="Nietzsche", d=1844, img="nietzsche"),
            dict(nom="Freud", d=1856, img="freud"), dict(nom="Durkheim", d=1858, img="durkheim"),
            dict(nom="Bourdieu", d=1930), dict(nom="Libet", d=1916)]),
        "tab_fin": dict(type="tableau", img="t3-charcot", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="André Brouillet, Une leçon clinique à la Salpêtrière, 1887"),
        "fin": dict(type="titre", sur="À suivre", t="Se libérer", sous="Épisode 4 · Les stoïciens, Spinoza, Kant"),
    }),
]

QUIZ = [
    dict(q="Pour Spinoza, pourquoi les hommes se croient-ils libres ?",
         r=["Parce qu'ils ont une volonté infinie", "Parce qu'ils sont conscients de leurs désirs et ignorants des causes qui les déterminent",
            "Parce que Dieu leur a donné le libre arbitre", "Parce qu'ils ne rencontrent aucun obstacle"], ok=1,
         voir="c_spi", ex="Lettre 58 (1674) : la pierre lancée qui pourrait penser se croirait libre. Le sentiment de liberté naît de l'ignorance."),
    dict(q="Quelle est la « troisième blessure » infligée à l'amour-propre humain, selon Freud ?",
         r=["La Terre n'est pas le centre de l'univers", "L'homme descend du règne animal",
            "Le moi n'est pas maître dans sa propre maison", "Dieu est mort"], ok=2,
         voir="bless", ex="Après Copernic (cosmologique) et Darwin (biologique), la psychanalyse inflige la blessure psychologique (1917)."),
    dict(q="Lequel de ces phénomènes Freud considère-t-il comme une trace de l'inconscient ?",
         r=["Le raisonnement mathématique", "Le lapsus", "La perception des couleurs", "Le réflexe rotulien"], ok=1,
         voir="signes", ex="Lapsus, actes manqués, rêves (« la voie royale ») et symptômes trahissent des désirs refoulés."),
    dict(q="Pour Durkheim, un fait social est…",
         r=["une décision libre et personnelle", "une manière d'agir, de penser ou de sentir extérieure à l'individu et qui s'impose à lui",
            "un événement historique important", "un désir inconscient"], ok=1,
         voir="def_fs", ex="La langue, la mode, la politesse… et même les taux de suicide varient avec régularité selon les sociétés."),
    dict(q="Quelle est la différence entre fatalisme et déterminisme ?",
         r=["Aucune : ce sont deux mots pour la même idée",
            "Le fatalisme dit que tout arrivera quoi que je fasse ; le déterminisme, que tout a une cause, mes décisions comprises",
            "Le déterminisme croit au destin, le fatalisme à la science", "Le fatalisme est moderne, le déterminisme antique"], ok=1,
         voir="fat", ex="Pour le déterminisme, ma décision n'est pas inutile : elle est elle-même une cause. Œdipe illustre le fatalisme."),
    dict(q="Que montre, au mieux, l'expérience de Libet (1983) ?",
         r=["Que le libre arbitre est définitivement réfuté",
            "Qu'une activité cérébrale précède la conscience de vouloir un geste simple",
            "Que l'inconscient freudien existe", "Que nous n'avons pas de cerveau libre"], ok=1,
         voir="chrono", ex="Geste minuscule, veto possible, signal peut-être simple bruit de fond : l'expérience ne tranche pas seule la question."),
    dict(q="Selon Nietzsche, pourquoi a-t-on inventé l'idée de libre arbitre ?",
         r=["Pour expliquer le mouvement des astres", "Pour pouvoir juger et punir les hommes",
            "Pour fonder la démocratie", "Pour guérir les névroses"], ok=1,
         voir="c_nietz", ex="Crépuscule des idoles : « les hommes ont été considérés comme libres, pour pouvoir être jugés et punis »."),
]

CREDITS = [
    "Spinoza : portrait anonyme, vers 1665 · Marx : photographie de John Mayall",
    "Freud : photographie de Max Halberstadt, vers 1921 · Nietzsche : photographie de Gustav Schultze, 1882 · "
    "Durkheim : photographie anonyme (domaine public)",
    "Tableaux et gravures : A. Brouillet, Une leçon clinique à la Salpêtrière (1887) ; S. Hirszenberg, Spinoza excommunié (1907) ; "
    "J. Wright of Derby, Un philosophe expliquant le planétaire (v. 1766) ; Goya, Le sommeil de la raison engendre des monstres (1799) ; "
    "J. Matejko, Copernic (1873) ; Darwin en singe, The Hornet (1871) ; J. H. Füssli, Le Cauchemar (1781) ; "
    "A. von Menzel, Le Laminoir (1875) ; G. Caillebotte, Rue de Paris, temps de pluie (1877) ; A. Anker, L'École de village (1896) ; "
    "E. Mazzanti, Pinocchio (1883) ; G. Doré, Minos (1861) ; J.-A.-D. Ingres, Œdipe et le Sphinx (1808) ; "
    "Spinoza, Ethica (1677) : domaine public ; Rodin, Le Penseur (photo Jebulon, CC0)",
    "Photographies : iceberg de l'océan Austral (NOAA, domaine public) ; Vésale, De humani corporis fabrica (1543), "
    "Wellcome Collection (CC BY 4.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
