"""Histoire · H3 « La Seconde Guerre mondiale » — édition française (histoire-géographie de Terminale), épisode 5 :
« Vers le génocide » (partie III du chapitre).

Traduction et adaptation de h3_5.py (édition anglaise, laissée intacte) selon outils/serie-dnl/EDITION_FR.md : même
structure, mêmes identifiants de visuels, mêmes repères, mêmes globes (sc = numéros de scènes de la carte animée H3, qui
passe d'elle-même en français). Plus aucune mention de la DNL, de l'anglais d'examen ni du professeur ; vocabulaire de
l'histoire-géographie classique (dossier documentaire, document, analyse de document, bilan critique).
  H3 : 2 population juive vers 1933 · 8 ghettos de Pologne · 22 ghetto de Varsovie · 27 Einsatzgruppen ·
       32 six centres de mise à mort · 37 Treblinka · 41 Nouvel Ordre européen fin 1942 · 43 soulèvement du ghetto ·
       44 révolte de Treblinka · 45 bilan du génocide
Ce qui n'est pas dans le cours est dit « hors du cours ». Les sélections d'Auschwitz : à partir de 1942, sommet en 1944.
Ton : sobre ; aucune image des victimes (les photographies du cours sont décrites, jamais montrées) ; humeurs
« calme » et « mystere » seulement. Citations : rendus français fidèles (Hilberg, Stroop, Lindwasser, Bomba), alignés
sur le texte français du site.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-5"
NOTION = "La Seconde Guerre mondiale"
NUM = 5
TITRE = "Vers le génocide"
SUIVANT = "Épisode 6 · La Seconde Guerre mondiale à l'examen"
PRONONCIATION = {"Einsatzgruppen": "Aïne-zats-groupen", "Sonderkommando": "Zonnder-kommando", "Zyklon": "Zi-klonne",
                 "Treblinka": "Tré-blinn-ka", "Chelmno": "Kèlm-no", "Majdanek": "Maï-da-nèk", "Belzec": "Bèl-jèts",
                 "Czestochowa": "Tchèn-sto-hova", "Kielce": "Kièl-tsé", "Stroop": "Chtrôp", "Jürgen": "Yur-guenne",
                 "Stangl": "Chtan-gueul", "Willenberg": "Vi-lenn-bèrg", "Lindwasser": "Linnd-vassèr",
                 "Liepaja": "Li-é-pa-ïa", "Chłodna": "Ouod-na", "Ivangorod": "I-vann-go-rod", "Siedlce": "Chièd-ltsé",
                 "Wehrmacht": "Vèr-markt", "Heydrich": "Haï-drik", "Eichmann": "Aïch-mann", "Breslau": "Brès-laou"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Six millions. Six millions d'hommes, de femmes et d'enfants juifs, assassinés par l'Allemagne nazie et ses complices. "
        "Les deux tiers des Juifs d'Europe.",
        "{-q1}{q2}Comment un État moderne en est-il venu à organiser le meurtre de tout un peuple ? Pas en un jour, et pas par accident : "
        "étape par étape, des ghettos aux centres de mise à mort.",
        "{-q2}{-g0}{sobre}Des cartes, des chiffres, de courts extraits de témoignages : les photographies du cours sont décrites par des mots, jamais montrées.",
        "{-sobre}{plan}Voici la troisième partie du chapitre : la politique raciale nazie. {plan.1}D'abord, les événements sur la carte. "
        "{plan.2}Puis le cours : les Juifs pris au piège, et les ghettos. {plan.3}Les Einsatzgruppen. "
        "{plan.4}Les centres de mise à mort, et Treblinka. {plan.5}Enfin : comment le sait-on, et comment s'en servir à l'examen.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[45]),
        "q1": dict(type="question", t="Six millions.", bande=True),
        "q2": dict(type="question", t="Comment un État moderne a-t-il organisé le meurtre de tout un peuple ?", bande=True),
        "sobre": dict(type="note", terme="Avant de commencer", cles=["cartes", "chiffres", "témoignages"],
                      t="Des cartes, des chiffres et de courts extraits de témoignages. Aucune image des victimes.",
                      etape="Les photographies du cours sont décrites par des mots, jamais montrées.", x=170, y=200, w=940),
        "plan": dict(type="liste", titre="Épisode 5 · Partie III du cours", items=[
            "Les événements sur la carte, 1933 – 1943", "III.1 · Les Juifs pris au piège et persécutés : les ghettos",
            "III.2 · Les Einsatzgruppen : la « Shoah par balles »", "III.3 · Les centres de mise à mort : étude de cas, Treblinka",
            "Comment le sait-on ? Les sources à l'examen"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 5", t="Vers le génocide",
                      sous="1933 – 1943 · ghettos · balles · gaz · 6 millions de victimes"),
    }),

    # ================================================================ la carte, 1933-1941
    dict(id="carte1", chap="Sur la carte, 1933 – 1941", fond="nuit", humeur="mystere",
         retenir="Vers 1933 : 9,5 millions de Juifs en Europe, surtout à l'Est · 1939 – 1941 : des ghettos en Pologne occupée · Varsovie : 440 000 Juifs sur 4 km² · à partir de juin 1941 : les Einsatzgruppen en URSS.",
         beats=[
        "{g1}Commençons par la carte, dans l'ordre chronologique. {g1.1}Vers 1933, environ neuf millions et demi de Juifs vivent en Europe. "
        "La plupart vivent à l'Est : trois millions en Pologne, deux millions et demi en Union soviétique. "
        "L'Allemagne, où la persécution nazie commence en 1933, n'en compte que cinq cent soixante-cinq mille.",
        "{g1.2}Septembre 1939 : l'Allemagne conquiert l'ouest de la Pologne. De là jusqu'en 1941, les Juifs de Pologne occupée sont enfermés dans des ghettos, "
        "des quartiers fermés des villes : Varsovie, Lodz, Cracovie, Lublin, Kielce, Czestochowa.",
        "{g1.3}Le plus grand est à Varsovie : quatre cent quarante mille Juifs, entassés sur environ quatre kilomètres carrés, derrière un mur.",
        "{g1.4}Puis, le vingt-deux juin 1941, l'Allemagne envahit l'Union soviétique. Derrière l'armée viennent quatre unités mobiles de tuerie, "
        "les Einsatzgruppen. Ville après ville, elles fusillent les Juifs au bord de fosses. Les historiens parlent de Shoah par balles.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[2, 8, 22, 27]),
    }),

    # ================================================================ la carte, 1941-1943
    dict(id="carte2", chap="Sur la carte, 1941 – 1943", fond="nuit", humeur="mystere",
         retenir="Déc. 1941 : le premier centre de mise à mort · juillet 1942 : Treblinka · 19 avril – 16 mai 1943 : le soulèvement du ghetto de Varsovie · 2 août 1943 : la révolte de Treblinka · 6 millions de Juifs assassinés.",
         beats=[
        "{g2}{g2.1}À partir de décembre 1941, une nouvelle méthode : le gaz. Les nazis font fonctionner six centres de mise à mort, tous en Pologne occupée : "
        "Chelmno, Belzec, Sobibor, Treblinka, Majdanek et Auschwitz. Ils sont construits pour tuer les gens dès leur arrivée.",
        "{g2.2}Juillet 1942 : Treblinka est construit, au nord-est de Varsovie. Des trains y amènent les Juifs du ghetto de Varsovie et des autres ghettos. "
        "En quinze mois, huit cent soixante-seize mille personnes y sont assassinées.",
        "{g2.3}Le dix-neuf avril 1943 : les troupes allemandes entrent dans le ghetto de Varsovie pour déporter ses derniers habitants, et les Juifs se soulèvent. "
        "Le soulèvement dure près d'un mois, jusqu'au seize mai, avant d'être écrasé par les SS.",
        "{g2.4}Le deux août 1943 : à Treblinka même, sept cents esclaves juifs se soulèvent et mettent le feu au camp. "
        "Le camp est fermé en octobre.",
        "{g2.5}Le bilan : six millions de Juifs assassinés. Quatre-vingt-dix pour cent des Juifs de Pologne. Quatre-vingt-dix-sept pour cent des Juifs de Lituanie.",
        "{-g2}{fr2}Les dates à retenir : {fr2.1}1933 ; {fr2.2}1939, les ghettos ; {fr2.3}juin 1941, les Einsatzgruppen ; "
        "{fr2.4}décembre 1941, le premier centre de mise à mort ; {fr2.5}juillet 1942, Treblinka ; {fr2.6}avril 1943, le soulèvement de Varsovie ; "
        "{fr2.7}août 1943, la révolte de Treblinka.",
    ], vis={
        "g2": dict(type="globe", code="H3", sc=[32, 37, 43, 44, 45]),
        "fr2": dict(type="frise", items=[
            dict(nom="9,5 millions de Juifs", d=1933, q="surtout à l'Est"), dict(nom="Ghettos", d=1939, q="Pologne, 1939 – 1941"),
            dict(nom="Einsatzgruppen", d=1941, q="à partir de juin"), dict(nom="Centres de mise à mort", d=1941, q="à partir de décembre"),
            dict(nom="Treblinka", d=1942, q="construit en juillet"), dict(nom="Soulèvement de Varsovie", d=1943, q="19 avril – 16 mai"),
            dict(nom="Révolte de Treblinka", d=1943, q="2 août")]),
    }),

    # ================================================================ III.1 pris au piège
    dict(id="piege", chap="III.1 · Pris au piège", fond="nuit", humeur="calme",
         retenir="Vers 1933 : 9,5 millions de Juifs en Europe, plus des deux tiers à l'Est (Pologne 3 millions, URSS 2 525 000, Allemagne 565 000). En 1942, l'Allemagne domine presque tout le continent : les Juifs sont pris au piège.",
         beats=[
        "{q3}Troisième partie, premier temps : les Juifs pris au piège et persécutés. Pourquoi pris au piège ?",
        "{-q3}{pop}La carte du cours sur la population juive vers 1933 compte : {pop.1}en Europe de l'Est, près de six millions huit cent mille ; "
        "{pop.2}en Europe centrale, un million six cent mille ; {pop.3}en Europe du Nord et de l'Ouest, moins de huit cent mille ; "
        "{pop.4}en Europe du Sud, un peu plus de trois cent mille. Plus des deux tiers vivent à l'Est.",
        "{-pop}En conquérant la Pologne en 1939, puis en envahissant l'Union soviétique en 1941, l'Allemagne met la main sur le cœur du judaïsme européen. "
        "{!Pris au piège}Voilà ce que veut dire pris au piège.",
        "{g3}Une deuxième carte du cours, l'administration allemande de l'Europe en 1942, montre le piège : de la France à l'Ukraine, "
        "le Grand Reich et les territoires occupés, entourés d'États alliés ou dépendants : la Hongrie, la Roumanie, la Slovaquie, la Croatie, la France de Vichy.",
        "{out}Qui reste en dehors ? {out.1}Seul le Royaume-Uni, {out.2}et quelques États neutres : l'Espagne, la Suisse et la Suède. "
        "En 1942, les Juifs d'Europe n'ont presque plus nulle part où fuir.",
    ], vis={
        "q3": dict(type="question", t="Pourquoi les Juifs d'Europe étaient-ils « pris au piège » ?"),
        "pop": dict(type="liste", titre="Population juive d'Europe vers 1933 (carte du cours)", items=[
            "Europe de l'Est : 6 760 000", "Europe centrale : 1 644 200", "Europe du Nord et de l'Ouest : 766 600",
            "Europe du Sud : 329 200"], x=170, y=130, w=940),
        "g3": dict(type="globe", code="H3", sc=[41]),
        "out": dict(type="liste", titre="Hors de la domination allemande en 1942", x=700, y=60, w=540, petit=True, bande=True, items=[
            "Le Royaume-Uni", "États neutres : Espagne, Suisse, Suède"]),
    }),

    # ================================================================ III.1 les ghettos
    dict(id="ghettos", chap="III.1 · Enfermés dans les ghettos", fond="nuit", humeur="calme",
         retenir="À partir de 1939, des ghettos en Pologne occupée : isoler, appauvrir, affaiblir, rassembler pour déporter. Varsovie : 440 000 Juifs sur 4 km², un mur de 3 m de haut et 18 km de long, 146 000 habitants au km² en 1941.",
         beats=[
        "{def3}À partir de 1939, en Pologne occupée, les Allemands concentrent les Juifs dans des {!ghettos}ghettos. Un ghetto est un quartier fermé d'une ville, "
        "coupé du reste de la population. Les Juifs sont forcés de s'y installer presque sans rien.",
        "{-def3}{g4}La carte du cours les place surtout dans le Gouvernement général, "
        "la partie de la Pologne dirigée par une administration civile allemande : Varsovie, Lodz, Cracovie, Lublin, Czestochowa. "
        "Après juin 1941, le système s'étend vers l'est, de Riga et Vilna jusqu'à Minsk et Odessa.",
        "{-g4}{lst4}Sois précis dans ta copie. {lst4.1}Le ghetto, ce n'est pas encore l'extermination. {lst4.2}Mais il isole les Juifs, les appauvrit et les affaiblit, "
        "{lst4.3}et il les rassemble dans des lieux d'où l'on pourra ensuite les déporter.",
        "{-lst4}{war}Le plus grand ghetto est à Varsovie : quatre cent quarante mille Juifs, sur environ quatre kilomètres carrés.",
        "{-war}{wl}{wl.1}Ils ne peuvent emporter que le strict minimum : ils sont dépossédés du jour au lendemain. "
        "{wl.2}Le ghetto est entouré d'un mur de trois mètres de haut et de dix-huit kilomètres de long. "
        "{wl.3}Réduit en 1941, il atteint une densité de cent quarante-six mille habitants au kilomètre carré : "
        "environ sept fois la densité de Paris aujourd'hui, une comparaison ajoutée hors du cours. "
        "{wl.4}Et la rue Chłodna reste en dehors du ghetto et le coupe en deux : une passerelle de bois, au-dessus de la rue, "
        "relie le petit ghetto et le grand ghetto.",
    ], vis={
        "def3": dict(type="def", cles=["quartier", "fermé"], terme="Ghetto",
                     t="Un quartier fermé d'une ville où les nazis enferment les Juifs, coupés du reste de la population.",
                     etape="Pologne occupée, à partir de 1939 · Varsovie, Lodz, Cracovie, Lublin, Czestochowa", x=170, y=200, w=940),
        "g4": dict(type="globe", code="H3", sc=[8]),
        "lst4": dict(type="liste", titre="Ce que fait le ghetto", cles=["extermination", "isole", "déporter"], items=[
            "Ce n'est pas encore l'extermination", "Il isole, appauvrit et affaiblit les Juifs",
            "Il les rassemble là d'où l'on pourra les déporter"], x=170, y=150, w=940),
        "war": dict(type="mot", t="440 000 Juifs · 4 km²", g="Le ghetto de Varsovie (cours)", y=250, taille=96),
        "wl": dict(type="liste", titre="Le ghetto de Varsovie", items=[
            "Dépossédés du jour au lendemain : le strict minimum", "Un mur de 3 m de haut et de 18 km de long",
            "146 000 habitants au km² en 1941 (Paris aujourd'hui ≈ 20 000 : hors du cours)",
            "Rue Chłodna : une passerelle relie le petit et le grand ghetto"], x=150, y=120, w=980),
    }),

    # ================================================================ III.1 la mort au ghetto, le soulèvement
    dict(id="varsovie", chap="III.1 · La mort au ghetto, et le soulèvement", fond="guerre", humeur="calme",
         retenir="Au ghetto, la mort fait partie du quotidien : faim, froid, maladies, 1 naissance pour 45 décès en 1942. Soulèvement : 19 avril – 16 mai 1943, écrasé par Stroop : « Il n'y a plus de quartier juif à Varsovie ! »",
         beats=[
        "{mort}Au ghetto, la mort devient quotidienne. {mort.1}La faim, le froid, l'entassement et les maladies tuent en masse. "
        "{mort.2}La nourriture doit entrer en contrebande, souvent grâce à des enfants, au risque d'être arrêtés. {mort.3}Chaque jour, le plus souvent la nuit, "
        "le service funéraire juif ramasse les cadavres dans les rues ; beaucoup finissent dans des fosses communes. "
        "{mort.4}À la fin, la population ne prête même plus attention aux corps étendus dans les rues.",
        "{-mort}{n45}Un chiffre résume tout. En 1942, le ghetto de Varsovie compte une naissance pour quarante-cinq décès.",
        "{-n45}{up}{up.1}En 1942, la plupart des habitants sont déportés à Treblinka. "
        "{up.2}En avril 1943, des troupes et des policiers allemands entrent dans le ghetto pour déporter les survivants. Les Juifs se soulèvent : "
        "le soulèvement du ghetto de Varsovie dure du dix-neuf avril au seize mai 1943. "
        "{up.3}Les Allemands l'écrasent en détruisant le ghetto maison par maison. Le seize mai, le commandant SS Jürgen Stroop "
        "envoie à Himmler un message qui annonce le résultat.{-up}",
        ("C", "Il n'y a plus de quartier juif à Varsovie !", "c_stroop"),
        "{-c_stroop}{nur}La couverture du rapport de Stroop, montrée dans le cours, porte le tampon du Tribunal militaire international : "
        "le propre rapport du bourreau a servi de preuve contre les dirigeants nazis, à Nuremberg.",
    ], vis={
        "mort": dict(type="liste", titre="La mort au ghetto", cles=["Faim", "contrebande", "nuit", "corps"], items=[
            "Faim, froid, entassement, maladies", "Nourriture passée en contrebande, souvent par des enfants, au risque d'être arrêtés",
            "Cadavres ramassés chaque jour, le plus souvent la nuit", "On ne remarquait plus les corps dans les rues"], x=150, y=120, w=980),
        "n45": dict(type="mot", t="1 naissance · 45 décès", g="Le ghetto de Varsovie en 1942 (cours)", y=250, taille=100),
        "up": dict(type="liste", titre="Le soulèvement du ghetto de Varsovie", items=[
            "1942 : la plupart des habitants déportés à Treblinka", "19 avril – 16 mai 1943 : les Juifs se soulèvent",
            "Écrasé maison par maison ; Stroop rend compte à Himmler"], x=150, y=140, w=980),
        "c_stroop": dict(type="cit", a="Jürgen Stroop", o="rapport à Himmler, 16 mai 1943", x=200, y=200, w=880),
        "nur": dict(type="note", terme="Pourquoi ce document compte", cles=["bourreau", "preuve"],
                    t="Le propre rapport du bourreau a servi de preuve à Nuremberg.",
                    etape="Sa couverture porte le tampon du Tribunal militaire international (cours).", x=170, y=200, w=940),
    }),

    # ================================================================ III.1 Hilberg
    dict(id="hilberg", chap="III.1 · Raul Hilberg : trois étapes", fond="nuit", humeur="calme",
         retenir="Hilberg : conversion (« vous n'avez pas le droit de vivre parmi nous en tant que Juifs ») → expulsion (« vous n'avez pas le droit de vivre parmi nous ») → destruction (« vous n'avez pas le droit de vivre »). L'insigne et le ghetto avaient des précédents ; la seule « invention » nazie : la Solution finale.",
         beats=[
        "{hil}D'où vient le génocide ? Le cours répond avec un historien, Raul Hilberg, auteur de La Destruction des Juifs d'Europe, en 1961. "
        "Dans le film Shoah de Claude Lanzmann, il replace la politique nazie dans une longue histoire de persécutions.",
        "{-hil}{st}{st.1}D'abord, la conversion. Les missionnaires chrétiens disaient en substance aux Juifs : vous n'avez pas le droit de vivre parmi nous en tant que Juifs. "
        "{st.2}Puis, l'expulsion. Les dirigeants séculiers qui ont suivi leur disaient : vous n'avez pas le droit de vivre parmi nous. "
        "{st.3}Enfin, la destruction. Les nazis ont décrété : vous n'avez pas le droit de vivre.",
        "{-st}{can}Avant le vingtième siècle, l'Église et les États chrétiens avaient déjà inventé la plupart des mesures reprises par les nazis : "
        "l'insigne distinctif, le ghetto, l'interdiction des mariages mixtes. {can.g}Hilberg met en regard le droit canonique {can.d}et les mesures nazies : "
        "l'insigne imposé par le concile du Latran, en 1215, et l'étoile juive de 1941 ; les ghettos du synode de Breslau, "
        "en 1267, et l'ordre de Heydrich de 1939. Ces dates viennent du livre de Hilberg, hors du cours.",
        "{-can}{inv}Alors, qu'ont inventé les nazis ? Seulement la dernière étape : la décision de tuer tous les Juifs, "
        "et l'organisation de leur meurtre. {!La Solution finale}La Solution finale.",
        "{-inv}{vq1}Les trois questions de la vidéo du cours, avec les réponses proposées par le site : "
        "{vq1.1}trois étapes, conversion, expulsion, destruction ; {vq1.2}avant le vingtième siècle, l'Église et les États chrétiens ; "
        "{vq1.3}et la seule invention nazie, la Solution finale.",
    ], vis={
        "hil": dict(type="mot", t="Raul Hilberg", g="La Destruction des Juifs d'Europe (1961) · interrogé dans Shoah (Lanzmann, 1985)",
                    y=250, taille=96),
        "st": dict(type="liste", titre="Hilberg : trois étapes de la politique antijuive", cles=["Conversion", "Expulsion", "Destruction"], items=[
            "Conversion : « vous n'avez pas le droit de vivre parmi nous en tant que Juifs »",
            "Expulsion : « vous n'avez pas le droit de vivre parmi nous »",
            "Destruction : « vous n'avez pas le droit de vivre »"], x=150, y=150, w=980),
        "can": dict(type="cols", g="Droit canonique", gq="insigne : concile du Latran, 1215 · ghetto : synode de Breslau, 1267 · interdiction des mariages mixtes",
                    d="Mesures nazies", dq="étoile juive : 1er sept. 1941 · ordre sur les ghettos : 21 sept. 1939 (dates hors du cours)", vs="→"),
        "inv": dict(type="def", cles=["tuer", "meurtre"], terme="Notion clé · la Solution finale",
                    t="L'euphémisme nazi pour la décision de tuer tous les Juifs d'Europe et l'organisation de leur meurtre : leur seule « invention », selon Hilberg.",
                    etape="Insigne, ghetto, spoliation avaient des précédents ; le meurtre systématique, non.", x=170, y=200, w=940),
        "vq1": dict(type="liste", titre="Vidéo du cours · Hilberg dans Shoah (réponses proposées)", items=[
            "Trois étapes ? → conversion, expulsion, destruction",
            "Qui persécutait avant ? → l'Église (droit canonique), les États chrétiens",
            "La seule « invention » nazie ? → la Solution finale"], x=150, y=150, w=980),
    }),

    # ================================================================ III.2 les Einsatzgruppen
    dict(id="einsatz", chap="III.2 · Les Einsatzgruppen", fond="guerre", humeur="calme",
         retenir="À partir du 22 juin 1941 : quatre Einsatzgruppen (A, B, C, D) derrière l'armée en URSS. Les Juifs avant tout, mais aussi des responsables communistes et des Roms, fusillés au bord de fosses : la « Shoah par balles », première étape de la Solution finale.",
         beats=[
        "{g7}Deuxième temps : le rôle des Einsatzgruppen. Quand l'Allemagne envahit l'Union soviétique, le vingt-deux juin 1941, "
        "quatre groupes suivent l'armée. {ein}Sur la carte du cours : {ein.1}le groupe A traverse les pays baltes, {ein.2}le B se dirige vers la Biélorussie et Moscou, "
        "{ein.3}le C entre en Ukraine, {ein.4}et le D dans le sud de l'Ukraine et en Crimée.",
        "{-ein}{-g7}{def7}Des unités mobiles de tuerie de la SS et de la police : environ trois mille hommes, un chiffre ajouté hors du cours. "
        "Le cours qualifie leur action de {!première étape}première étape de la Solution finale : dès ses premiers jours, "
        "la guerre d'anéantissement est aussi une guerre contre les Juifs.",
        "{-def7}{tg}Leurs cibles : {tg.1}les Juifs avant tout, {tg.2}mais aussi des responsables communistes et des Roms. "
        "{tg.3}D'abord les hommes ; à partir d'août 1941, des communautés entières, femmes et enfants compris, ce qui est ajouté hors du cours. "
        "{tg.4}La méthode : les victimes sont conduites hors de la ville et fusillées au bord de fosses ou de ravins. "
        "D'où l'expression de la carte du cours : {!la Shoah par balles}la Shoah par balles.",
        "{-tg}{ph}Le cours montre une photographie légendée : Ukraine 1942, action juive, Ivangorod. "
        "Un soldat met en joue une femme qui tient un enfant. Envoyée du front de l'Est vers l'Allemagne, elle a été interceptée à Varsovie par la résistance polonaise. "
        "Hors du cours : à Babi Yar, près de Kiev, plus de trente-trois mille Juifs ont été fusillés en deux jours, en septembre 1941.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[27]),
        "ein": dict(type="liste", titre="Quatre Einsatzgruppen, juin 1941", x=40, y=70, w=340, petit=True, bande=True, items=[
            "A : les pays baltes", "B : la Biélorussie, vers Moscou", "C : l'Ukraine", "D : le sud de l'Ukraine, la Crimée"]),
        "def7": dict(type="def", cles=["mobiles", "SS", "police"], terme="Einsatzgruppen",
                     t="Unités mobiles de tuerie de la SS et de la police, qui suivent l'armée en URSS.",
                     etape="≈ 3 000 hommes (hors du cours) · « la première étape de la Solution finale » (cours)", x=170, y=200, w=940),
        "tg": dict(type="liste", titre="Cibles et méthode", cles=["Juifs", "Roms", "communautés", "fosses"], items=[
            "Les Juifs avant tout", "Aussi des responsables communistes et des Roms",
            "D'abord les hommes ; à partir d'août 1941, des communautés entières (hors du cours)",
            "Fusillades de masse au bord de fosses et de ravins : la « Shoah par balles »"], x=150, y=120, w=980),
        "ph": dict(type="note", terme="Un document du cours (décrit, pas montré)", cles=["Ivangorod", "soldat"],
                   t="« Ukraine 1942, action juive, Ivangorod » : un soldat met en joue une femme qui tient un enfant.",
                   etape="Envoyée du front de l'Est, interceptée à Varsovie par la résistance polonaise.", x=170, y=180, w=940),
    }),

    # ================================================================ III.2 plus d'un million
    dict(id="einsatz2", chap="III.2 · Plus d'un million de victimes", fond="nuit", humeur="calme",
         retenir="Aidés par la police d'ordre, la Wehrmacht et des auxiliaires locaux, les Einsatzgruppen fusillent plus d'un million de Juifs soviétiques jusqu'au printemps 1943. Lituanie : 97 % des Juifs tués ; Lettonie : 75 %.",
         beats=[
        "{aid}Les Einsatzgruppen sont peu nombreux, mais ils n'agissent pas seuls. {aid.1}Des bataillons de la police d'ordre, {aid.2}des unités de la Wehrmacht, "
        "{aid.3}et des auxiliaires locaux recrutés dans les territoires occupés, Lituaniens, Lettons, Ukrainiens, les aident à rafler, garder et fusiller les victimes.",
        "{-aid}{mil}Au printemps 1943, ils ont tué plus d'un million de Juifs soviétiques : ces complices et ce chiffre sont ajoutés hors du cours. "
        "Sur la carte du cours, un million des trois millions de Juifs d'URSS, presque tous fusillés, puisque les centres de mise à mort étaient en Pologne.",
        "{-mil}{bal}Dans les pays baltes, traversés par le groupe A, les communautés sont presque anéanties : "
        "{bal.1}quatre-vingt-dix-sept pour cent des Juifs de Lituanie tués, "
        "{bal.2}soixante-quinze pour cent en Lettonie. "
        "{bal.3}Et un film allemand d'une fusillade à Liepaja, en Lettonie, en 1941, montré dans le cours, prouve que ces tueries ont été vues, et même filmées.",
        "{-bal}{vq2}Les cinq questions de la deuxième vidéo du cours, avec les réponses proposées par le site : "
        "{vq2.1}les membres, la SS et la police ; {vq2.2}les cibles, les Juifs avant tout ; {vq2.3}quatre groupes ; "
        "{vq2.4}des complices, l'armée, la police et des auxiliaires locaux ; {vq2.5}plus d'un million de victimes, fusillées.",
    ], vis={
        "aid": dict(type="liste", titre="Ils n'ont pas agi seuls (hors du cours)", items=[
            "Bataillons de la police d'ordre", "Unités de la Wehrmacht", "Auxiliaires locaux : Lituaniens, Lettons, Ukrainiens"],
            x=150, y=150, w=980),
        "mil": dict(type="mot", t="1 000 000", g="des 3 020 000 Juifs d'URSS tués, presque tous fusillés (carte du cours)", y=240, taille=120),
        "bal": dict(type="liste", titre="Les pays baltes (carte du cours)", items=[
            "Lituanie : 140 000 Juifs tués sur 145 000 (97 %)", "Lettonie : 70 000 sur 95 000 (75 %)",
            "Liepaja, 1941 : une fusillade filmée par des soldats allemands"], x=150, y=150, w=980),
        "vq2": dict(type="liste", titre="Vidéo du cours · la première étape de la Solution finale", petit=True, items=[
            "Membres ? → SS et police, environ 3 000 hommes", "Cibles ? → les Juifs avant tout, des responsables communistes, des Roms",
            "Combien de groupes ? → quatre, de A à D", "Complices ? → Wehrmacht, police d'ordre, auxiliaires locaux",
            "Combien, comment ? → plus d'un million de Juifs soviétiques, fusillés en masse"], x=150, y=120, w=980),
    }),

    # ================================================================ III.3 six centres de mise à mort
    dict(id="centres", chap="III.3 · Six centres de mise à mort", fond="nuit", humeur="calme",
         retenir="À partir de décembre 1941, six centres de mise à mort, tous en Pologne occupée : Chelmno, Treblinka, Sobibor, Belzec, Majdanek, Auschwitz. Gazés dès l'arrivée ; le Sonderkommando ; Treblinka : 3 000 personnes à l'heure à partir d'octobre 1942.",
         beats=[
        "{g9}Troisième temps. À partir de décembre 1941, six centres de mise à mort : selon les mots du cours, des centres sophistiqués de meurtre de masse. "
        "{six}Tous en Pologne occupée : {six.1}Chelmno, dans la partie annexée au Grand Reich ; "
        "{six.2}Treblinka, {six.3}Sobibor, {six.4}Belzec {six.5}et Majdanek, dans le Gouvernement général ; {six.6}et Auschwitz, en bordure du Grand Reich.",
        "{-six}Pourquoi la Pologne ? Au cœur de la plus grande communauté juive d'Europe, près des ghettos, sur le réseau ferré. "
        "Chelmno commence à gazer le huit décembre 1941, une date ajoutée hors du cours.",
        "{-g9}{cmp9}Ne confonds pas deux mots. {cmp9.g}Un camp de concentration enferme et exploite ses détenus. {cmp9.d}Un centre de mise à mort existe pour tuer.",
        "{-cmp9}{gaz}{gaz.1}Dans les centres de mise à mort, les Juifs sont gazés dès leur arrivée : d'abord les hommes, puis les femmes et les enfants. "
        "{gaz.2}Seul un petit groupe d'esclaves est gardé en vie, pour travailler dans le camp et faire disparaître les corps : le {!Sonderkommando}Sonderkommando. "
        "{gaz.3}Les cadavres sont brûlés, en plein air ou, à Auschwitz, dans des fours. "
        "{gaz.4}C'est organisé comme une industrie : à Treblinka, à partir d'octobre 1942, trois mille personnes à l'heure, "
        "et six à sept mille par train.",
        "{-gaz}{bom}Avraham Bomba, un survivant de Treblinka, décrit une chambre à gaz en béton d'environ six mètres sur six, "
        "sans fenêtre, avec des tuyaux qui la faisaient ressembler à une douche. Et il dit :{-bom}",
        ("C", "le tout prenait, je dirais, entre cinq et sept minutes", "c_bomba"),
    ], vis={
        "g9": dict(type="globe", code="H3", sc=[32]),
        "six": dict(type="liste", titre="Six centres de mise à mort, Pologne occupée", x=40, y=60, w=340, petit=True, bande=True, items=[
            "Chelmno", "Treblinka", "Sobibor", "Belzec", "Majdanek", "Auschwitz"]),
        "cmp9": dict(type="cols", g="Camp de concentration", gq="enferme et exploite ses détenus", d="Centre de mise à mort",
                     dq="existe pour tuer, dès l'arrivée", vs="≠"),
        "gaz": dict(type="liste", titre="Un meurtre organisé comme une industrie", cles=["arrivée", "Sonderkommando", "brûlés", "train"], items=[
            "Gazés dès l'arrivée : d'abord les hommes, puis les femmes et les enfants", "Quelques esclaves gardés en vie : le Sonderkommando",
            "Cadavres brûlés : en plein air, ou dans des fours à Auschwitz",
            "Treblinka, oct. 1942 : 3 000 à l'heure ; 6 000 à 7 000 par train"], x=150, y=120, w=980),
        "bom": dict(type="note", terme="Avraham Bomba (1990, dossier sur Treblinka)", cles=["béton", "fenêtre", "tuyaux"],
                    t="Une pièce en béton d'environ 6 m × 6 m, sans fenêtre, avec des tuyaux qui faisaient croire à une douche.",
                    etape="Barbier déporté de Czestochowa en septembre 1942 ; évadé en janvier 1943.", x=170, y=200, w=940),
        "c_bomba": dict(type="cit", a="Avraham Bomba", o="témoignage, 1990 (dossier sur Treblinka)", x=200, y=210, w=880),
    }),

    # ================================================================ III.3 Auschwitz et Majdanek
    dict(id="auschwitz", chap="III.3 · Auschwitz et Majdanek", fond="nuit", humeur="calme",
         retenir="Auschwitz et Majdanek : centre de mise à mort + camp de concentration et de travail ; Zyklon B ; sélections à l'arrivée (environ 80 % envoyés au gaz). Les sélections commencent en 1942 et culminent en 1944 (Hongrie).",
         beats=[
        "{am}Deux des six centres sont différents : Auschwitz et Majdanek. {am.1}Ils associent un centre de mise à mort et un camp de concentration et de travail. "
        "{am.2}On y utilise un nouveau gaz : le {!Zyklon B}Zyklon B. {am.3}Et à l'arrivée, les nazis organisent des sélections : les personnes valides deviennent des esclaves "
        "pour l'effort de guerre allemand ; les autres, environ quatre-vingts pour cent, sont aussitôt conduites aux chambres à gaz. "
        "{am.4}Auschwitz-Birkenau avait d'abord été construit pour les prisonniers de guerre soviétiques, les premiers à y être gazés, comme on l'a vu dans l'épisode précédent.",
        "{-am}{dat}Une correction sur les dates. {dat.1}Le document du cours place les sélections après 1944. "
        "{dat.2}En réalité, elles commencent à Auschwitz dès 1942. {dat.3}Et 1944 en marque le sommet, avec la déportation des Juifs de Hongrie. "
        "C'est un ajout hors du cours. Sur la carte du cours, la Hongrie a perdu soixante-seize pour cent de ses Juifs.",
    ], vis={
        "am": dict(type="liste", titre="Auschwitz et Majdanek : des centres d'un autre type", cles=["travail", "Zyklon", "sélections", "soviétiques"], items=[
            "Centre de mise à mort + camp de concentration et de travail", "Un nouveau gaz : le Zyklon B",
            "Sélections : des esclaves pour l'effort de guerre ; environ 80 % gazés aussitôt",
            "Birkenau d'abord construit pour les prisonniers soviétiques, les premiers gazés"], x=150, y=120, w=980),
        "dat": dict(type="liste", titre="Sélections : les bonnes dates", marques=["✗", "✓", "✓"], items=[
            "Le document : sélections « après 1944 »", "En réalité : dès 1942 à Auschwitz (hors du cours)",
            "Sommet en 1944 : les Juifs de Hongrie (550 000 tués sur 725 000, 76 %)"], x=150, y=150, w=980),
    }),

    # ================================================================ III.3 Treblinka
    dict(id="treblinka", chap="Étude de cas n° 3 : Treblinka", fond="nuit", humeur="calme",
         retenir="Treblinka : construit en juillet 1942 au nord-est de Varsovie ; 876 000 morts (874 000 Juifs, 2 000 Roms) ; victimes trompées jusqu'au bout ; révolte de 700 esclaves le 2 août 1943 (environ 70 survivants connus à la fin de la guerre) ; fermé en octobre 1943.",
         beats=[
        "{g11}L'étude de cas, maintenant : Treblinka, construit en juillet 1942 dans le Gouvernement général, à environ quatre-vingts kilomètres au nord-est de Varsovie, "
        "une distance ajoutée hors du cours. {tb}{tb.1}Jusqu'à sa fermeture, en octobre 1943, "
        "{tb.2}il tue huit cent soixante-seize mille personnes : huit cent soixante-quatorze mille Juifs, venus surtout des ghettos, et deux mille Roms.",
        "{-tb}{-g11}{arr}Les victimes arrivent en train, dans des wagons de marchandises, sous escorte : une photographie du dossier montre des Juifs "
        "qui montent dans des trains à Siedlce, en août 1942. Tout est fait pour les tromper jusqu'au dernier moment. "
        "Un panneau annonce qu'après s'être lavés et changés, les Juifs poursuivront leur voyage vers l'est, pour travailler.",
        "{-arr}Avraham Lindwasser arrive de Varsovie le vingt-huit août 1942 ; il a témoigné au procès Eichmann, en 1961. "
        "Sur la rampe, l'ordre :",
        ("C", "Descendez !", "c_lind"),
        "{-c_lind}{ram}{ram.1}Puis les cris et les coups. {ram.2}L'argent et les bijoux à remettre, les chaussures à enlever. "
        "{ram.3}Les rangs par trois. {ram.4}Et un officier, le capitaine aux lunettes, demande les métiers : quelques hommes sont choisis pour devenir esclaves. "
        "Lindwasser est l'un d'eux. Il est gardé en vie comme esclave pendant un an.",
        "{-ram}{g11b}Le deux août 1943, sept cents esclaves juifs se soulèvent et mettent le feu au camp. Lindwasser s'évade. "
        "{rv}{rv.1}Parmi ceux qui parviennent à s'enfuir, on sait qu'environ soixante-dix ont survécu jusqu'à la fin de la guerre. "
        "{rv.2}En octobre 1943, le camp est fermé.",
    ], vis={
        "g11": dict(type="globe", code="H3", sc=[37]),
        "tb": dict(type="liste", titre="Treblinka (dossier documentaire)", x=700, y=60, w=540, petit=True, bande=True, items=[
            "Juillet 1942 – octobre 1943", "876 000 morts : 874 000 Juifs, 2 000 Roms"]),
        "arr": dict(type="note", terme="Trompés jusqu'au bout", cles=["panneau", "travailler"],
                    t="Un panneau : après le bain, les Juifs poursuivraient leur voyage « vers l'est, pour travailler ».",
                    etape="Document 3 : des Juifs montent dans des trains sous escorte à Siedlce, août 1942 (décrit).", x=170, y=200, w=940),
        "c_lind": dict(type="cit", a="Avraham Lindwasser", o="procès Eichmann, 1961 (dossier sur Treblinka)", x=200, y=230, w=880),
        "ram": dict(type="liste", titre="L'arrivée sur la rampe (Lindwasser)", items=[
            "Cris et coups : pas le temps de comprendre", "Argent, bijoux et chaussures à remettre", "Les rangs par trois",
            "« Le capitaine aux lunettes » choisit quelques esclaves selon leur métier"], x=150, y=130, w=980),
        "g11b": dict(type="globe", code="H3", sc=[44]),
        "rv": dict(type="liste", titre="La révolte, 2 août 1943", x=700, y=60, w=540, petit=True, bande=True, items=[
            "Environ 70 survivants connus à la fin de la guerre", "Octobre 1943 : le camp est fermé"]),
    }),

    # ================================================================ le dossier sur Treblinka
    dict(id="ws4", chap="Le dossier sur Treblinka : l'essentiel des réponses", fond="aube", humeur="calme",
         retenir="Le dossier sur Treblinka : présenter Treblinka (dates, lieu, bilan) · les victimes (ghettos, trains, tromperie) · les tâches des esclaves · le processus de mise à mort, de la rampe à la crémation des corps.",
         beats=[
        "{ws}Les quatre questions du dossier sur Treblinka, avec les réponses proposées par le site, pas un corrigé officiel. "
        "{ws.1}Un : présenter Treblinka, avec ses dates, son lieu et son bilan. "
        "{ws.2}Deux : les victimes : venues des ghettos, Lindwasser de Varsovie, Bomba de Czestochowa ; en train, et trompées. "
        "{ws.3}Trois : les tâches des esclaves juifs. Des barbiers comme Bomba, à l'intérieur même de la chambre à gaz ; le tri des affaires des victimes ; "
        "le camouflage du camp ; et, à Treblinka deux, la zone d'extermination, le transport des cadavres vers les fosses. "
        "{ws.4}Quatre : décrire le processus de mise à mort. Voici l'enchaînement à suivre.",
        "{-ws}{proc}{proc.1}Le train s'arrête sur la rampe : « Descendez ! », les cris et les coups. "
        "{proc.2}L'argent, les bijoux et les chaussures à remettre ; les rangs par trois ; quelques hommes choisis comme esclaves. "
        "{proc.3}Les autres se déshabillent, rassurés par le panneau. "
        "{proc.4}La chambre à gaz : entassés autant que possible ; la mort en cinq à sept minutes. "
        "{proc.5}Les esclaves traînent les cadavres jusqu'aux fosses ; plus tard, les corps sont brûlés en plein air. "
        "Trois mille personnes à l'heure, à partir d'octobre 1942.",
    ], vis={
        "ws": dict(type="liste", titre="Dossier sur Treblinka (réponses proposées)", petit=True, items=[
            "Présenter → centre de mise à mort, juillet 1942 – oct. 1943, au nord-est de Varsovie, 876 000 morts",
            "Les victimes ? → ghettos de Varsovie et d'ailleurs ; en train, sous escorte, trompées",
            "Tâches des esclaves → barbiers, tri des affaires, camouflage, cadavres (« Treblinka 2 »)",
            "Le processus de mise à mort → de la rampe à la crémation des corps"], x=130, y=120, w=1020),
        "proc": dict(type="liste", titre="Question 4 · l'enchaînement à suivre", petit=True, items=[
            "La rampe : « Descendez ! », cris et coups", "Argent, bijoux, chaussures ; rangs par trois ; esclaves choisis",
            "Déshabillage, rassurés par le panneau trompeur", "La chambre à gaz : la mort en 5 à 7 minutes",
            "Cadavres jetés dans les fosses, puis brûlés · 3 000 à l'heure à partir d'oct. 1942"], x=130, y=120, w=1020),
    }),

    # ================================================================ III.3 le bilan, les étapes
    dict(id="bilan", chap="Six millions", fond="guerre", humeur="calme",
         retenir="6 millions de Juifs assassinés, les deux tiers des Juifs d'Europe : Pologne 90 %, Lituanie 97 %, Pays-Bas 71 %, France 28 %, Italie 16 %. Les étapes : ghettos → balles → gaz → révoltes.",
         beats=[
        "{g13}La Shoah a tué six millions de Juifs, les deux tiers des Juifs d'Europe : gazés, fusillés, "
        "ou tués par les conditions de travail et de vie des ghettos et des camps.",
        "{pays}La carte du cours montre d'énormes écarts entre les pays. {pays.1}Pologne : trois millions de morts, quatre-vingt-dix pour cent. "
        "{pays.2}Lituanie : quatre-vingt-dix-sept pour cent. {pays.3}Pays-Bas : soixante et onze pour cent. {pays.4}France : vingt-huit pour cent. "
        "{pays.5}Italie : seize pour cent. Sous occupation allemande directe, en Pologne et dans les pays baltes, les communautés ont été presque anéanties.",
        "{-pays}{-g13}{lien13}Et fais le lien avec l'épisode un. Le génocide a réalisé le premier moteur du Nouvel Ordre européen : "
        "l'Europe comme entité raciale, purifiée par le meurtre.",
        "{-lien13}{eta}Tout le processus, en quatre étapes. {eta.1}À partir de 1939 : les ghettos, pour concentrer, isoler et affamer. "
        "{eta.2}À partir de juin 1941 : les balles, les Einsatzgruppen derrière l'armée. {eta.3}À partir de décembre 1941 : le gaz, six centres de mise à mort en Pologne occupée. "
        "{eta.4}Et en 1943 : les révoltes, quand les victimes se battent, dans le ghetto de Varsovie et à Treblinka.",
        "{-eta}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}On peut le dire ainsi. {rep1.1}À partir de 1939, les Juifs de Pologne sont enfermés dans des ghettos, isolés et affamés. "
        "{rep1.2}À partir de juin 1941, les Einsatzgruppen fusillent plus d'un million de Juifs soviétiques. "
        "{rep1.3}À partir de décembre 1941, six centres de mise à mort les gazent dès leur arrivée : six millions de morts en tout.",
    ], vis={
        "g13": dict(type="globe", code="H3", sc=[45]),
        "pays": dict(type="liste", titre="Part des Juifs tués (carte du cours)", x=880, y=380, w=370, petit=True, bande=True, items=[
            "Pologne : 3 000 000 sur 3 350 000 (90 %)", "Lituanie : 97 %", "Pays-Bas : 100 000 sur 140 000 (71 %)",
            "France : 75 000 sur 270 000 (28 %)", "Italie : 8 000 sur 50 000 (16 %)"]),
        "lien13": dict(type="note", terme="Lien avec l'épisode 1", cles=["raciale", "meurtre"],
                       t="Le génocide a réalisé le premier moteur du Nouvel Ordre européen : l'Europe comme entité raciale, purifiée par le meurtre.",
                       etape="« L'élimination absolue des Juifs » (Hitler, 11 décembre 1941, tel que le cours le cite).", x=170, y=200, w=940),
        "eta": dict(type="liste", titre="De la persécution au génocide : les étapes", items=[
            "1939 – 1941 · Ghettos : concentrer, isoler, affamer", "À partir de juin 1941 · Balles : Einsatzgruppen A à D",
            "À partir de déc. 1941 · Gaz : six centres de mise à mort en Pologne", "1943 · Révoltes : ghetto de Varsovie (avril – mai), Treblinka (2 août)"],
            x=150, y=130, w=980),
        "pa1": dict(type="pause", t="En trois phrases : comment la politique nazie est-elle passée de la persécution au génocide ?",
                    sous="Mets la vidéo en pause, écris ta réponse, puis relance pour comparer."),
        "rep1": dict(type="liste", titre="Un modèle de réponse", items=[
            "À partir de 1939 : les ghettos de Pologne isolent, affament et rassemblent les Juifs.",
            "À partir de juin 1941 : les Einsatzgruppen fusillent plus d'un million de Juifs soviétiques.",
            "À partir de déc. 1941 : six centres de mise à mort gazent dès l'arrivée ; 6 millions de morts."], x=150, y=150, w=980),
    }),

    # ================================================================ comment le sait-on ?
    dict(id="sources", chap="Comment le sait-on ?", fond="nuit", humeur="calme",
         retenir="Comment le sait-on ? Les survivants (Lindwasser 1961 ; Bomba dans Shoah, 1985, et en 1990), les bourreaux (rapport de Stroop ; croquis de Stangl, après son arrestation en 1967), les plans des survivants (Willenberg : à l'échelle, mais il n'a jamais vu la zone d'extermination).",
         beats=[
        "{q14}La dernière question du cours, très importante pour l'examen : comment le sait-on ?",
        "{-q14}{src}Trois sortes de sources, chacune avec son intérêt et ses limites. "
        "{src.1}Les témoignages des survivants : Lindwasser en 1961 ; Bomba dans le film Shoah de Claude Lanzmann, en 1985, et dans un entretien de 1990. "
        "{src.2}Les documents des bourreaux : le rapport de Stroop ; le croquis de Treblinka dessiné par Franz Stangl, son commandant, "
        "après son arrestation en 1967 ; il a été jugé en 1970. {src.3}Et les plans dessinés par des survivants.",
        "{-src}{wil}Le plus célèbre est celui de Samuel Willenberg. Membre du commando de camouflage, il avait accès à la plus grande partie du camp. "
        "Il a dessiné un plan de Treblinka à l'échelle, dans tous ses détails : on le considère comme l'un des plus fiables. "
        "{wil.1}Sauf pour une zone : la zone d'extermination, qu'il n'a jamais vue.",
        "{-wil}{vl}Pour chaque source, deux colonnes : {vl.g}son intérêt, {vl.d}ses limites. Un survivant a vu de ses propres yeux, "
        "mais seulement ce qu'il a vu ; un bourreau connaît le système, mais il peut cacher ou justifier ses crimes.",
    ], vis={
        "q14": dict(type="question", t="Comment le sait-on ?"),
        "src": dict(type="liste", titre="Trois sortes de sources", cles=["survivants", "bourreaux", "plans"], items=[
            "Témoignages des survivants : Lindwasser (1961), Bomba (Shoah, 1985 ; 1990)",
            "Documents des bourreaux : rapport de Stroop ; croquis de Stangl (après son arrestation, 1967)",
            "Plans dessinés par des survivants : Samuel Willenberg"], x=150, y=150, w=980),
        "wil": dict(type="note", terme="Le plan de Samuel Willenberg", cles=["dessiné", "fiables"],
                    t="Dessiné à l'échelle par un survivant du commando de camouflage : l'un des plans de Treblinka les plus fiables.",
                    etape="Limite : la zone d'extermination, qu'il n'a jamais vue.", x=170, y=200, w=940),
        "vl": dict(type="cols", g="Intérêt", gq="un témoin oculaire · un bourreau qui connaît le système · un plan précis",
                   d="Limites", dq="seulement ce que le témoin a vu · un bourreau peut cacher ou justifier ses crimes", vs="↔"),
    }),

    # ================================================================ à l'examen : analyse de document
    dict(id="dbq", chap="À l'examen : une analyse de document", fond="aube", humeur="calme",
         retenir="Analyse de document : présenter le document (nature, auteur, date) · le situer dans son contexte · l'expliquer · bilan critique : intérêt (témoin direct, à l'échelle, recoupé par d'autres sources) et limites (zone d'extermination jamais vue, un seul témoin, des lieux et non des chiffres).",
         beats=[
        "{ex}Un exercice d'examen. {ex.p1}Une analyse de document : le plan de Treblinka dessiné par Samuel Willenberg. "
        "{ex.1}La consigne : montrez en quoi ce document permet de comprendre le fonctionnement du centre de mise à mort de Treblinka, et quelles en sont les limites.",
        "{-ex}{struc}La démarche à suivre : {struc.1}présenter le document, sa nature, son auteur, sa date. "
        "{struc.2}Le situer dans son contexte. {struc.3}L'expliquer : ce qu'il montre, avec tes connaissances. "
        "{struc.4}Et finir par un bilan critique : son intérêt et ses limites.",
        "{-struc}{pa2}",
        ("P", 2.0),
        "{-pa2}{m1}Voici un modèle. D'abord la présentation : ce document est un plan du centre de mise à mort de Treblinka, "
        "dessiné à l'échelle par Samuel Willenberg, un survivant qui travaillait dans le commando de camouflage. "
        "{m1.1}Puis le contexte : Treblinka fonctionne de juillet 1942 à octobre 1943, dans le Gouvernement général ; huit cent soixante-seize mille personnes y sont assassinées.",
        "{-m1}{fort}L'intérêt. {fort.1}C'est l'œuvre d'un témoin direct, qui avait accès à la plus grande partie du camp. "
        "{fort.2}Il est dessiné à l'échelle, dans tous ses détails : la forme extérieure du camp correspond presque au site réel. "
        "{fort.3}Et on peut le recouper avec d'autres sources : Lindwasser, Bomba, et même le croquis du commandant Stangl.",
        "{-fort}{lim}Les limites. {lim.1}Willenberg n'a jamais vu la zone d'extermination. "
        "{lim.2}C'est le regard d'un seul témoin : il faut le confronter à d'autres sources. "
        "{lim.3}Et un plan montre des lieux, pas l'ampleur du meurtre : pour cela, ajoute le bilan, huit cent soixante-seize mille morts, et les témoignages.",
    ], vis={
        "ex": dict(type="exo", niveau="dbq", titre="Le plan de Treblinka de Samuel Willenberg",
                   enonce=["Plan du centre de mise à mort de Treblinka, dessiné à l'échelle par Samuel Willenberg, survivant qui travaillait dans le commando de camouflage."],
                   questions=["Consigne : montrez en quoi ce document permet de comprendre le fonctionnement du centre de mise à mort de Treblinka, et quelles en sont les limites."]),
        "struc": dict(type="liste", titre="Analyse de document · la démarche", items=[
            "Présenter : nature, auteur, date", "Situer dans le contexte",
            "Expliquer : ce que montre le document, avec tes connaissances", "Bilan critique : intérêt et limites"],
            x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Rédige la présentation et le bilan critique : que nous apprend le plan de Willenberg sur Treblinka, et quelles en sont les limites ?",
                    sous="Mets la vidéo en pause, suis la démarche, puis relance pour voir un modèle."),
        "m1": dict(type="note", terme="Un modèle · présentation et contexte", cles=["plan"],
                   t="Ce document est un plan du centre de mise à mort de Treblinka, dessiné à l'échelle par Samuel Willenberg, survivant du commando de camouflage.",
                   etape="Contexte : Treblinka, juillet 1942 – octobre 1943, Gouvernement général ; 876 000 morts.", x=150, y=180, w=980),
        "fort": dict(type="liste", titre="Intérêt", marques=["✓", "✓", "✓"], items=[
            "Un témoin direct, qui avait accès à la plus grande partie du camp", "Dessiné à l'échelle : la forme extérieure correspond au site réel",
            "Recoupé par d'autres sources : Lindwasser, Bomba, le croquis de Stangl"], x=150, y=150, w=980),
        "lim": dict(type="liste", titre="Limites", marques=["✗", "✗", "✗"], items=[
            "Il n'a jamais vu la zone d'extermination", "Un seul témoin : le confronter à d'autres sources",
            "Des lieux, pas des chiffres : ajouter les 876 000 morts et les témoignages"], x=150, y=150, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Les ghettos : à partir de 1939, les Juifs de Pologne, pris au piège, sont enfermés, quatre cent quarante mille à Varsovie ; "
        "pour Hilberg, la seule invention nazie est la Solution finale. "
        "{carte.2}Les balles : à partir de juin 1941, les Einsatzgruppen fusillent plus d'un million de Juifs soviétiques. "
        "{carte.3}Le gaz : à partir de décembre 1941, six centres de mise à mort en Pologne ; à Treblinka, huit cent soixante-seize mille morts ; "
        "en tout, six millions. {carte.4}Et les sources : survivants, bourreaux, plans, chacune avec son intérêt et ses limites.",
        ("P", 4.0),
        "{-carte}{fin}Dans le prochain épisode : la Seconde Guerre mondiale à l'examen, la question problématisée et l'analyse de document, pas à pas.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="VERS LE GÉNOCIDE", branches=[
            dict(t="Ghettos · III.1", items=["9,5 millions de Juifs, surtout à l'Est", "Varsovie : 440 000 sur 4 km²", "Hilberg : la Solution finale"]),
            dict(t="Balles · III.2", items=["Einsatzgruppen A à D, juin 1941", "Juifs, communistes, Roms", "plus d'1 million de Juifs soviétiques"]),
            dict(t="Gaz · III.3", items=["6 centres de mise à mort en Pologne", "Treblinka : 876 000 morts", "6 millions : 2/3 des Juifs d'Europe"]),
            dict(t="Sources", items=["survivants : Lindwasser, Bomba", "bourreaux : Stroop, Stangl", "plans : Willenberg"])]),
        "fin": dict(type="mot", t="Ensuite : la guerre à l'examen", g="Épisode 6 · question problématisée et analyse de document", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Vers 1933, où vivaient la plupart des 9,5 millions de Juifs d'Europe ?",
         r=["En Europe de l'Est (6,76 millions)", "En Allemagne", "En Europe de l'Ouest", "En Europe du Sud"], ok=0, voir="pop",
         ex="La Pologne comptait 3 millions de Juifs, l'URSS 2 525 000, l'Allemagne seulement 565 000 : la conquête de l'Est les a pris au piège."),
    dict(q="Combien de Juifs ont été enfermés dans le ghetto de Varsovie, et sur quelle surface ?",
         r=["440 000 sur environ 4 km²", "44 000 sur 40 km²", "4,4 millions sur 4 km²", "146 000 sur 18 km²"], ok=0, voir="war",
         ex="146 000 habitants au km² en 1941 ; le mur mesurait 3 m de haut et 18 km de long."),
    dict(q="Quelles sont les trois étapes de la politique antijuive selon Raul Hilberg ?",
         r=["Conversion, expulsion, destruction", "Ghettos, balles, gaz", "Insigne, ghetto, étoile", "Persécution, déportation, libération"],
         ok=0, voir="st",
         ex="« Pas le droit de vivre parmi nous en tant que Juifs », « pas le droit de vivre parmi nous », « pas le droit de vivre ». La seule invention nazie : la Solution finale."),
    dict(q="Que faisaient les Einsatzgruppen ?",
         r=["Des unités mobiles de la SS et de la police qui fusillaient les Juifs derrière le front, en URSS", "Ils dirigeaient les centres de mise à mort en Pologne",
            "Ils gardaient le ghetto de Varsovie", "C'étaient des résistants polonais"], ok=0, voir="def7",
         ex="Quatre groupes, de A à D, à partir de juin 1941 : la « Shoah par balles », plus d'un million de Juifs soviétiques tués."),
    dict(q="Où se trouvaient les six centres de mise à mort ?",
         r=["Tous en Pologne occupée", "En Allemagne", "En URSS occupée", "En France et en Belgique"], ok=0, voir="six",
         ex="Chelmno, Treblinka, Sobibor, Belzec, Majdanek, Auschwitz : près des ghettos et sur le réseau ferré."),
    dict(q="Quand les sélections ont-elles commencé à Auschwitz ?",
         r=["En 1942, avec un sommet en 1944", "Seulement après 1944", "En 1939", "En 1945"], ok=0, voir="dat",
         ex="Le document du cours dit « après 1944 » ; en réalité, elles commencent en 1942 et culminent en 1944 avec la déportation des Juifs de Hongrie."),
    dict(q="Combien de personnes ont été tuées à Treblinka ?",
         r=["876 000, dont 874 000 Juifs et 2 000 Roms", "6 millions", "70 000", "3 000"], ok=0, voir="tb",
         ex="De juillet 1942 à octobre 1943 ; 3 000, c'est le nombre de personnes tuées à l'heure dans les chambres à gaz à partir d'octobre 1942."),
    dict(q="Quelle est la principale limite du plan de Treblinka dessiné par Willenberg ?",
         r=["Il n'a jamais vu la zone d'extermination", "Il n'est pas à l'échelle", "Il a été dessiné par le commandant",
            "Il montre le ghetto de Varsovie, pas Treblinka"], ok=0, voir="wil",
         ex="Survivant du commando de camouflage, il a dessiné le camp à l'échelle : un document très utile, mais limité pour cette zone."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 3 « La Seconde Guerre mondiale », partie III : la politique raciale nazie, vers le génocide (dossier documentaire sur Treblinka ; vidéos du cours sur Raul Hilberg et les Einsatzgruppen), tel qu'il est rédigé sur le site, avec des ajouts signalés « hors du cours » (Mémorial de l'Holocauste des États-Unis) ; carte animée du chapitre 3 (site).",
    "Réponses au dossier et aux questions des vidéos : proposées par le site, pas un corrigé officiel.",
    "Aucune photographie des victimes : les documents du cours sont décrits par des mots.",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
