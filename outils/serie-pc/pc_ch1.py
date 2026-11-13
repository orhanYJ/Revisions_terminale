"""Physique-chimie, chapitre 1 : « Transformations acides-bases » — le cours en vidéo.

Même chaîne que la vidéo du chapitre 4 (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots),
moteur pc/serie/moteur.js (types anim, formule, graphe, exo, pause).
Contenu : le cours du site (pc/index.html, chapitre 1 : rappels, fiches 1 à 12, formules, TP 1), rien au-delà ;
ce qui dépasse le programme est dit « hors programme ». Les trois exercices sont inventés pour la vidéo (signalé à
l'écran) ; leurs valeurs ont été recalculées (voir les commentaires).
Usage : python3 outils/serie-philo/verifier.py pc_ch1 ; puis generer.py pc_ch1 ; chevauchements.py ch1.
"""

SITE = "pc"
VOIX_VIVANTE = True   # voix dite phrase par phrase, prise la plus expressive (generer.py, voix_qwen.py)
RYTHME = "vivant"     # silences variables selon la fin de phrase (generer.py, _ecart_vivant)
CODE = "ch1"
NOTION = "Transformations acides-bases"
NUM = 1
TITRE = "Transformations acides-bases"
SUIVANT = "Chapitre 2 · Méthodes physiques d'analyse"
PRONONCIATION = {"Brønsted": "Brönnstède", "Sørensen": "Seurennsenne", "Jabir": "Djabir", "Hayyan": "Hayane",
                 "oxonium": "oxonium", "amphotère": "amfotère", "amphion": "amfion", "putrescine": "putrécine"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]"


# ---------------------------------------------------------------- données
# TP 1 (mesures d'Orhan, site) : x = −log c, y = pH mesuré ; quotients |écart| / 0,1 = 5,3 · 4,0 · 2,6 · 0,4 · 1,6 · 6,6
TP1 = [(0, 0.53), (1, 1.40), (2, 2.26), (3, 3.04), (4, 4.16), (5, 5.66)]

H3O = "H_3O^{+}"
HO = "HO^{−}"

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_cit}{q1}Un citron. Du vinaigre. Une eau gazeuse. Un détartrant. Tous ont un point commun : ils sont acides. "
        "Ça pique la langue, et ça attaque le calcaire.",
        "{-q1}{q2}Mais au fond, qu'est-ce que ça veut dire ? Qu'est-ce qui rend une solution acide, à l'échelle des molécules ?",
        "{-q2}{q3}Et voici une énigme. Deux flacons d'acide, à la même concentration. Le premier a un pH de deux. "
        "Le second, un pH de deux virgule huit. Même quantité d'acide… et pas la même acidité.",
        ("Pourquoi ?", {"rate": "-8%"}),
        "{-q3}La réponse tient en une idée : un acide est une espèce qui cède un ion hydrogène, une base est une espèce qui le capte. "
        "Tout le chapitre sort de ce simple {!transfert}transfert.",
        "{-tab_cit}{plan}Dans cette vidéo, on part de zéro. {plan.1}D'abord les rappels indispensables, et l'origine de l'acidité : la liaison polarisée. "
        "{plan.2}Puis les définitions de Brønsted, les couples et les réactions acide-base. "
        "{plan.3}Ensuite le pH, le logarithme et la dilution, avec une expérience classique. "
        "{plan.4}Puis la question qui tombe au bac : la réaction avec l'eau est-elle totale, ou limitée ? "
        "{plan.5}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_cit": dict(type="tableau", img="c1-citron", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Citron entier et coupé, photo Ivar Leidus, CC BY-SA 4.0"),
        "q1": dict(type="question", t="Citron, vinaigre, eau gazeuse : tous acides."),
        "q2": dict(type="question", t="Qu'est-ce qui rend une solution acide ?"),
        "q3": dict(type="question", t="Même concentration : pH 2,0 d'un côté, pH 2,8 de l'autre."),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les rappels, et l'origine de l'acidité", "Brønsted : acides, bases, couples, réactions",
            "Le pH, le logarithme, la dilution et une expérience", "Réaction totale ou limitée ?",
            "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 1", t="Transformations acides-bases",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. rappels
    dict(id="rappels", chap="Les rappels indispensables", fond="nuit", humeur="calme",
         retenir="[X] = n/V en mol·L⁻¹ · dilution : C_mère × V_mère = C_fille × V_fille · une solution est toujours électriquement neutre.",
         beats=[
        "{echelle}Commençons par ce que tu sais depuis le collège. Le pH est un nombre, en général compris entre zéro et quatorze, à vingt-cinq degrés. "
        "{echelle.1}En dessous de sept, la solution est acide : le jus de citron, vers deux virgule cinq, le vinaigre, vers trois. "
        "{echelle.2}À sept, elle est neutre : c'est l'eau pure. "
        "{echelle.3}Au-dessus de sept, elle est basique : l'eau savonneuse, vers dix, le déboucheur d'évier, vers quatorze.",
        "Tu sais aussi que diluer une solution acide fait remonter son pH vers sept. Ce chapitre va expliquer pourquoi, et donner au pH une vraie définition.",
        "{-echelle}{ions}Deuxième rappel : les ions. {ions.1}Un ion est un atome, ou un groupe d'atomes, qui a gagné ou perdu des électrons. "
        "Un cation est chargé plus, un anion est chargé moins. "
        "{ions.2}Dans l'eau, un composé ionique se dissocie : le chlorure de sodium donne des ions sodium et des ions chlorure. "
        "L'indice a q signifie : dissous dans l'eau, entouré de molécules d'eau. "
        "{ions.3}Et une règle cruciale pour ce chapitre : une solution est toujours électriquement neutre. "
        "Si des ions positifs apparaissent, des ions négatifs apparaissent en même temps.",
        "{-ions}{f_conc}Troisième rappel : la quantité de matière. {f_conc.1}On passe d'une masse à une quantité de matière en divisant par la masse molaire : n égale m sur M. "
        "{f_conc.2}La concentration d'une espèce dissoute, c'est sa quantité de matière divisée par le volume de solution, en mole par litre. "
        "On la note entre crochets. "
        "{f_conc.3}Ces crochets vont être partout : crochet H trois O plus se lit « concentration en ions oxonium ».",
        "{-f_conc}{f_dil}Quatrième rappel : la dilution. Diluer, c'est ajouter de l'eau sans ajouter de soluté. "
        "{f_dil.1}La quantité de soluté ne change pas, d'où la relation : C mère fois V mère égale C fille fois V fille. "
        "{f_dil.2}Le facteur de dilution F, c'est C mère sur C fille, ou encore V fille sur V mère. "
        "{f_dil.3}Pour diluer dix fois, on prélève par exemple dix millilitres de solution mère à la pipette jaugée, "
        "et on complète à cent millilitres dans une fiole jaugée. C'est le geste de base au laboratoire.",
        "{-f_dil}",
    ], vis={
        "echelle": dict(type="liste", titre="L'échelle de pH à 25 °C", items=[
            "pH < 7 : acide · citron ≈ 2,5 · vinaigre ≈ 3", "pH = 7 : neutre · l'eau pure",
            "pH > 7 : basique · eau savonneuse ≈ 10 · déboucheur ≈ 14"], marques=["<", "=", ">"], x=170, y=170, w=940),
        "ions": dict(type="liste", titre="Ions et solutions aqueuses", items=[
            "Cation : a perdu des électrons (+) · anion : en a gagné (−)",
            "NaCl → Na^{+}(aq) + Cl^{−}(aq) · (aq) : dissous dans l'eau",
            "Une solution est toujours électriquement neutre"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "f_conc": dict(type="formule", titre="Quantité de matière et concentration", x=150, y=140, w=980, lignes=[
            dict(f="n = " + fr("m", "M"), n="n en mol · m en g · M en g·mol^-1"),
            dict(f="[X] = " + fr("n(X)", "V"), cadre=True, n="en mol·L^-1 · V en L"),
            dict(f="[" + H3O + "] : la concentration en ions oxonium", txt=True)]),
        "f_dil": dict(type="formule", titre="La dilution", x=150, y=140, w=980, lignes=[
            dict(f="C_{mère} × V_{mère} = C_{fille} × V_{fille}", cadre=True, n="la quantité de soluté se conserve"),
            dict(f="F = " + fr("C_{mère}", "C_{fille}") + " = " + fr("V_{fille}", "V_{mère}")),
            dict(f="F = 10 : pipette jaugée de 10,0 mL, fiole jaugée de 100,0 mL", txt=True, pt=True)]),
    }),

    # ================================================================ II. Lewis, électronégativité, polarité
    dict(id="polarite", chap="D'où vient l'acidité : la liaison polarisée", fond="cosmos", humeur="mystere",
         retenir="Une liaison entre H et O, N, F ou Cl est polarisée : H porte δ+ et peut partir en H⁺. Une liaison C—H ne l'est presque pas.",
         beats=[
        "{lew}Pour comprendre l'acidité, il faut regarder les électrons. Le schéma de Lewis représente tous les électrons de valence d'une molécule. "
        "{lew.1}Un doublet liant, c'est un trait entre deux atomes : deux électrons partagés, une liaison covalente. "
        "{lew.2}Un doublet non liant, c'est un trait sur un atome : deux électrons qui lui appartiennent, sans être partagés. "
        "{lew.3}Chaque atome cherche à s'entourer de huit électrons : c'est la règle de l'octet. Sauf l'hydrogène, qui en veut deux : la règle du duet.",
        "{-lew}{liais}À connaître par cœur. {liais.1}Le carbone fait quatre liaisons, sans doublet non liant. "
        "{liais.2}L'azote fait trois liaisons, et porte un doublet non liant. "
        "{liais.3}L'oxygène fait deux liaisons, et porte deux doublets non liants. "
        "{liais.4}L'hydrogène fait une liaison. "
        "Quand ce compte change, l'atome porte une charge : un oxygène avec une seule liaison et trois doublets porte une charge moins ; "
        "un azote avec quatre liaisons porte une charge plus.",
        "{-liais}{def_en}Maintenant, l'idée clé : l'{!électronégativité}électronégativité. C'est la capacité d'un atome à attirer vers lui les électrons d'une liaison. "
        "{def_en.1}Retiens l'ordre : le fluor, plus que l'oxygène, plus que l'azote, plus que le chlore. Ce sont les atomes à surveiller.",
        "{-def_en}{an_pol}{pol_pts}{pol_pts.1}{an_pol.1}Regarde la molécule de chlorure d'hydrogène. Le chlore est bien plus électronégatif que l'hydrogène : "
        "il tire vers lui le doublet de la liaison. La liaison est polarisée. Le chlore porte une charge partielle delta moins, l'hydrogène une charge partielle delta plus.",
        "{pol_pts.2}{an_pol.2}Cet hydrogène, appauvri en électrons, est mal retenu. Une molécule d'eau approche : son oxygène, riche en doublets non liants, vient le chercher. "
        "L'hydrogène part sans son électron, sous forme d'ion H plus, et se fixe sur l'eau. "
        "Il se forme un ion oxonium, H trois O plus, et un ion chlorure.",
        "{-an_pol}{-pol_pts}{test}D'où le test à faire sur toute molécule. {test.1}Cherche un hydrogène porté par un oxygène, un azote, un fluor ou un chlore. "
        "{test.2}Une liaison carbone-hydrogène, elle, n'est presque pas polarisée : cet hydrogène ne part jamais. "
        "{test.3}L'acide palmitique, par exemple, compte trente-deux hydrogènes. Un seul est mobile : celui du groupe C O O H.",
        "{-test}{formes}Dernier rappel : une molécule peut avoir des liaisons polarisées sans être polaire. Tout dépend de sa forme. "
        "Les doublets autour d'un atome central se repoussent, et s'écartent le plus possible. "
        "{formes.1}Quatre doublets donnent une forme tétraédrique, comme le méthane. "
        "{formes.2}Avec un doublet non liant, on voit une pyramide : l'ammoniac. "
        "{formes.3}Avec deux doublets non liants, une forme coudée : l'eau. "
        "{formes.4}Deux doublets seulement : une forme linéaire, comme le dioxyde de carbone.",
        "{-formes}{cols_p}{cols_p.g}Dans le dioxyde de carbone, linéaire, les deux liaisons polarisées tirent en sens opposés : elles s'annulent. La molécule est apolaire. "
        "{cols_p.d}Dans l'eau, coudée, les deux polarisations s'ajoutent : la molécule est polaire. "
        "C'est pour cela que l'eau entoure et stabilise les ions, et qu'elle peut arracher un proton à un acide. "
        "La règle pratique : semblable dissout semblable.",
        "{-cols_p}",
    ], vis={
        "lew": dict(type="liste", titre="Le schéma de Lewis", items=[
            "Doublet liant : un trait entre deux atomes, 2 électrons partagés",
            "Doublet non liant : un trait sur un atome, 2 électrons non partagés",
            "Octet : 8 électrons autour de chaque atome · duet : 2 pour H"], marques=["—", "|", "8"], x=150, y=170, w=980),
        "liais": dict(type="liste", titre="Les nombres de liaisons", items=[
            "C : 4 liaisons, 0 doublet non liant", "N : 3 liaisons, 1 doublet non liant",
            "O : 2 liaisons, 2 doublets non liants", "H : 1 liaison"], marques=["C", "N", "O", "H"], x=170, y=150, w=940),
        "def_en": dict(type="def", terme="L'électronégativité", cles=["attirer", "électrons"],
                       t="Capacité d'un atome à attirer vers lui les électrons d'une liaison.",
                       etape="Ordre à retenir : F > O > N > Cl. Une liaison entre l'un d'eux et H est polarisée.", x=170, y=190, w=940),
        "an_pol": dict(type="anim", nom="acidebase", x=40, y=72, h=624, seg=[[1.2, 9.2], [11, 19.5]]),
        "pol_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "H—Cl : le chlore attire le doublet · H^{δ+}, Cl^{δ−}",
            "L'eau capte H^{+} : HCl + H_2O → Cl^{−} + " + H3O]),
        "test": dict(type="liste", titre="Le test à faire sur toute molécule", items=[
            "Un H porté par O, N, F ou Cl ? Un acide potentiel",
            "Une liaison C—H n'est presque pas polarisée : rien ne part",
            "Acide palmitique : 32 H, un seul mobile, celui de —COOH"], marques=["?", "✗", "!"], x=150, y=170, w=980),
        "formes": dict(type="liste", titre="La géométrie, d'après les doublets", items=[
            "4 liaisons : tétraédrique · CH_4", "3 liaisons + 1 doublet : pyramidale · NH_3, " + H3O,
            "2 liaisons + 2 doublets : coudée · H_2O", "2 liaisons doubles : linéaire · CO_2"], marques=["4", "3", "2", "2"], x=150, y=150, w=980),
        "cols_p": dict(type="cols", g="CO_2 : linéaire", gq="les deux polarisations s'annulent · apolaire",
                       d="H_2O : coudée", dq="les polarisations s'ajoutent · polaire · elle dissout les ions", vs="≠",
                       repere="Semblable dissout semblable"),
    }),

    # ================================================================ III. Brønsted
    dict(id="bronsted", chap="Acide et base selon Brønsted", fond="nuit", humeur="lumiere",
         retenir="Acide : espèce capable de céder un ou plusieurs ions H⁺. Base : capable d'en capter. Amphotère : les deux. Redox ou acide-base ? Le critère, c'est l'électron.",
         beats=[
        "{bron}Venons-en aux définitions officielles. Elles portent le nom du chimiste danois Johannes Brønsted, qui les propose en mille neuf cent vingt-trois.",
        "{-bron}{defs}{defs.1}Un acide est une espèce chimique capable de céder un ou plusieurs ions hydrogène, H plus. "
        "{defs.2}Une base est une espèce chimique capable de capter un ou plusieurs ions hydrogène, H plus.",
        "{-defs}{proton}Que représente cet ion H plus ? Un atome d'hydrogène, c'est un proton et un électron. "
        "Retire l'électron : il ne reste que le noyau, un {!proton}proton. "
        "C'est pourquoi on dit indifféremment transfert d'ion hydrogène, ou transfert de proton.",
        "{-proton}{an_br}{br_pts}{br_pts.1}{an_br.1}Exemple de base : l'ammoniac. Son azote porte un doublet non liant. "
        "Ce doublet capte un ion H plus pris à une molécule d'eau. Il se forme l'ion ammonium, N H quatre plus, et l'ion hydroxyde, H O moins. "
        "L'ammoniac est une base.",
        "{br_pts.2}{an_br.2}Et remarque ce qu'a fait l'eau. Face au chlorure d'hydrogène, elle captait un H plus : elle était une base. "
        "Face à l'ammoniac, elle en cède un : elle est un acide. Une espèce qui possède les deux caractères est dite {!amphotère}amphotère.",
        "{-an_br}{-br_pts}{ex_br}Deux exemples classiques. {ex_br.1}Le sulfure d'hydrogène est un acide, car il peut libérer un proton : "
        "H deux S donne H plus et H S moins. "
        "{ex_br.2}L'ammoniac est une base : N H trois, plus H plus, donne N H quatre plus.",
        "{-ex_br}{redox}Attention au piège classique : ne confonds pas acide-base et oxydoréduction. "
        "{redox.1}Une réaction acide-base échange des protons : dans la demi-équation, on voit H plus, et jamais d'électron. "
        "{redox.2}Une oxydoréduction échange des électrons : on voit e moins, et souvent des H plus en plus. "
        "{redox.3}Le critère de tri, c'est donc l'électron, jamais le proton. "
        "Le couple H g O sur H g, par exemple, fait apparaître des H plus dans sa demi-équation, mais aussi deux électrons : c'est de l'oxydoréduction.",
        "{-redox}{amph}{amph.1}Comment prouver qu'une espèce est amphotère ? Il faut écrire deux demi-équations : une où elle cède un H plus, une où elle en capte un. "
        "Une seule ne suffit jamais. "
        "{amph.2}L'eau est l'exemple central : elle appartient à deux couples, H trois O plus sur H deux O, et H deux O sur H O moins. "
        "{amph.3}Autre cas à connaître : l'ion hydrogénocarbonate, H C O trois moins. "
        "{amph.4}Et dans un acide aminé comme l'alanine, sous forme d'amphion, le groupe ammonium peut céder un proton, pendant que le groupe carboxylate peut en capter un.",
        "{-amph}",
    ], vis={
        "bron": dict(type="portrait", annee=1923, img="c1-bronsted", nom="Johannes Brønsted", dates="1879 – 1947",
                     legende="chimiste danois · 1923 : acide et base par le transfert d'un proton"),
        "defs": dict(type="liste", titre="Les deux définitions de Brønsted", items=[
            "Acide : espèce capable de céder un ou plusieurs ions hydrogène H^{+}",
            "Base : espèce capable de capter un ou plusieurs ions hydrogène H^{+}"], marques=["A", "B"], x=150, y=200, w=980),
        "proton": dict(type="note", titre="H⁺, un proton", cles=["noyau", "proton"],
                       t="L'atome H, c'est un proton et un électron. Sans son électron, il ne reste que le noyau : un proton. Transfert d'ion hydrogène = transfert de proton.",
                       x=170, y=200, w=940),
        "an_br": dict(type="anim", nom="acidebase", x=40, y=72, h=624, seg=[[21.6, 29.5], [31.6, 37.5]]),
        "br_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Le doublet de l'azote capte H^{+} : NH_3 + H_2O ⇌ NH_4^{+} + " + HO,
            "L'eau : base face à HCl, acide face à NH_3 · elle est amphotère"]),
        "ex_br": dict(type="formule", titre="Deux exemples classiques", x=150, y=170, w=980, lignes=[
            dict(f="H_2S → H^{+} + HS^{−}", n="le sulfure d'hydrogène cède un proton : un acide"),
            dict(f="NH_3 + H^{+} → NH_4^{+}", n="l'ammoniac capte un proton : une base")]),
        "redox": dict(type="formule", titre="Acide-base ou oxydoréduction ?", x=150, y=130, w=980, lignes=[
            dict(f="acide-base : on échange des H^{+}, jamais d'électron", txt=True, pt=True),
            dict(f="oxydoréduction : on échange des e^{−} (et souvent des H^{+} en plus)", txt=True, pt=True),
            dict(f="HgO + 2 H^{+} + 2 e^{−} ⇌ Hg + H_2O : oxydoréduction", cadre=True, taille=36, n="le critère de tri, c'est l'électron, jamais le proton")]),
        "amph": dict(type="liste", titre="Prouver qu'une espèce est amphotère", items=[
            "Écrire deux demi-équations : elle cède un H^{+}, elle en capte un",
            "L'eau : " + H3O + "/H_2O et H_2O/" + HO,
            "L'ion hydrogénocarbonate HCO_3^{−}",
            "L'alanine (amphion) : —NH_3^{+} cède, —COO^{−} capte"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
    }),

    # ================================================================ IV. le couple
    dict(id="couple", chap="Le couple acide-base", fond="cosmos", humeur="calme",
         retenir="Couple AH/A⁻, l'acide en premier : AH ⇌ A⁻ + H⁺. De l'acide à la base, on retire un H et une charge +. H⁺ seul n'existe pas en solution.",
         beats=[
        "{def_cp}Deux espèces forment un {!couple}couple acide-base si l'on passe de l'une à l'autre par l'échange d'un seul ion hydrogène. "
        "{def_cp.1}On note le couple A H sur A moins : l'acide toujours en premier.",
        "{-def_cp}{f_cp}{f_cp.1}On écrit alors l'équation protonique du couple : A H, double flèche, A moins plus H plus. "
        "{f_cp.2}La double flèche dit que l'équation se lit dans les deux sens : le couple existe indépendamment de la réaction étudiée. "
        "{f_cp.3}Exemple : l'acide éthanoïque, C H trois C O O H, double flèche, l'ion éthanoate, C H trois C O O moins, plus H plus.",
        "{-f_cp}{charges}Une règle mécanique permet de compléter n'importe quel couple. "
        "{charges.1}Pour passer de l'acide à la base, on retire un H, et on retire une charge plus. "
        "{charges.2}Ainsi, la base de H S O trois moins est S O trois deux moins. Pas S O trois moins. "
        "{charges.3}Dans l'autre sens, on ajoute un H et une charge plus. L'erreur classique : ajouter le H sans toucher à la charge. "
        "{charges.4}Et attention, A H sur A moins n'est qu'une forme générique. L'acide peut être un ion positif, et la base une molécule neutre : "
        "N H quatre plus sur N H trois, ou H trois O plus sur H deux O.",
        "{-charges}{h_seul}Dernière remarque, importante : l'ion H plus seul n'existe pas en solution. Un proton nu est aussitôt capté par une molécule d'eau. "
        "L'équation protonique est donc une écriture formelle, utile pour définir le couple. Une vraie réaction met toujours en jeu deux couples.",
        "{-h_seul}",
    ], vis={
        "def_cp": dict(type="def", terme="Couple acide-base", cles=["seul", "ion hydrogène"],
                       t="Deux espèces qui se transforment l'une en l'autre par l'échange d'un seul ion hydrogène H⁺.",
                       etape="Noté AH/A⁻ : l'acide toujours en premier.", x=170, y=190, w=940),
        "f_cp": dict(type="formule", titre="L'équation protonique", x=150, y=140, w=980, lignes=[
            dict(f="AH ⇌ A^{−} + H^{+}", cadre=True, taille=56, n="AH : l'acide · A^{−} : sa base conjuguée"),
            dict(f="⇌ : l'équation se lit dans les deux sens", txt=True),
            dict(f="CH_3COOH ⇌ CH_3COO^{−} + H^{+}", n="couple CH_3COOH/CH_3COO^{−}")]),
        "charges": dict(type="liste", titre="Compléter un couple", items=[
            "Acide → base : on retire un H et une charge +",
            "HSO_3^{−} → SO_3^{2−} (et non SO_3^{−})",
            "Base → acide : on ajoute un H et une charge +",
            "L'acide peut être un ion + : NH_4^{+}/NH_3 · " + H3O + "/H_2O"], marques=["−", "✓", "+", "!"], x=150, y=150, w=980),
        "h_seul": dict(type="note", titre="H⁺ seul n'existe pas", cles=["formelle", "deux couples"],
                       t="Un proton nu est aussitôt capté par l'eau. L'équation protonique est une écriture formelle : une vraie réaction met toujours en jeu deux couples.",
                       x=170, y=200, w=940),
    }),

    # ================================================================ V. la réaction acide-base
    dict(id="reaction", chap="La réaction acide-base", fond="nuit", humeur="lumiere",
         retenir="Acide 1 + base 2 → base 1 + acide 2 : le H⁺ passe de l'acide d'un couple à la base d'un autre. Toujours deux couples, l'eau souvent l'un d'eux.",
         beats=[
        "{an_re}{re_pts}{re_pts.1}{an_re.1}Une réaction acide-base est un transfert d'ion hydrogène de l'acide d'un couple vers la base d'un autre couple. "
        "Ici, l'acide éthanoïque cède l'hydrogène de son groupe carboxyle, et l'ion hydroxyde le capte. "
        "Chaque réactif se transforme en son conjugué : acide un, plus base deux, donne base un, plus acide deux.",
        "{-an_re}{-re_pts}{f_re}Pour écrire l'équation, trois gestes. "
        "{f_re.1}Un : l'équation protonique du couple dont l'acide réagit. C H trois C O O H donne C H trois C O O moins, plus H plus. "
        "{f_re.2}Deux : celle du couple dont la base réagit, écrite dans l'autre sens. H O moins, plus H plus, donne H deux O. "
        "{f_re.3}Trois : on additionne. Les H plus se simplifient, "
        "{f_re.4}et il reste : C H trois C O O H, plus H O moins, donne C H trois C O O moins, plus H deux O.",
        "{-f_re}{reperer}Inversement, pour repérer les couples dans une équation donnée, "
        "{reperer.1}cherche les paires d'espèces qui ne diffèrent que d'un H plus, une de chaque côté de la flèche. Il y en a toujours exactement deux. "
        "{reperer.2}Si tu n'en trouves qu'une, tu as oublié l'eau : elle est presque toujours l'un des deux partenaires. "
        "{reperer.3}Quand on dissout de l'aspirine, par exemple, les couples sont l'aspirine et sa base conjuguée, et H trois O plus sur H deux O : "
        "l'eau joue le rôle de base.",
        "{-reperer}{note_tot}Une précision : savoir si la réaction est totale, avec une flèche simple, ou limitée, avec une double flèche, ne se devine pas. "
        "Cela se décide par une mesure de pH. On le verra à la fin du chapitre.",
        "{-note_tot}",
    ], vis={
        "an_re": dict(type="anim", nom="acidebase", x=40, y=72, h=624, seg=[[39.8, 48.5]]),
        "re_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=170, w=560, items=[
            "CH_3COOH cède H^{+}, " + HO + " le capte : acide 1 + base 2 → base 1 + acide 2"]),
        "f_re": dict(type="formule", titre="Écrire l'équation en trois gestes", x=150, y=110, w=980, lignes=[
            dict(f="CH_3COOH ⇌ CH_3COO^{−} + H^{+}", n="1 · le couple dont l'acide réagit", taille=38),
            dict(f=HO + " + H^{+} ⇌ H_2O", n="2 · le couple dont la base réagit, dans l'autre sens", taille=38),
            dict(f="3 · on additionne : les H^{+} se simplifient", txt=True),
            dict(f="CH_3COOH + " + HO + " → CH_3COO^{−} + H_2O", cadre=True, taille=38)]),
        "reperer": dict(type="liste", titre="Repérer les couples dans une équation", items=[
            "Deux paires d'espèces qui ne diffèrent que d'un H^{+}, une de chaque côté",
            "Une seule paire trouvée ? Tu as oublié l'eau",
            "Aspirine : C_9H_8O_4/C_9H_7O_4^{−} et " + H3O + "/H_2O · l'eau est la base"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "note_tot": dict(type="note", titre="Totale ou limitée ?", cles=["devine", "pH"],
                         t="La flèche simple (totale) ou double (limitée) ne se devine pas : elle se décide par une mesure de pH.",
                         x=170, y=220, w=940),
    }),

    # ================================================================ VI. les couples à connaître, familles
    dict(id="familles", chap="Les couples à connaître", fond="cosmos", humeur="calme",
         retenir="H₃O⁺/H₂O · H₂O/HO⁻ · (CO₂, H₂O)/HCO₃⁻ · HCO₃⁻/CO₃²⁻ · R—COOH/R—COO⁻ · R—NH₃⁺/R—NH₂ : chez les amines, l'acide est l'ion ammonium.",
         beats=[
        "{cpl}Le programme exige quatre familles de couples. Elles reviennent dans presque tous les exercices. "
        "{cpl.1}L'eau : H trois O plus sur H deux O, et H deux O sur H O moins. On la trouve dans toute solution aqueuse. "
        "{cpl.2}L'acide carbonique : C O deux, H deux O, sur H C O trois moins ; puis H C O trois moins sur C O trois deux moins. Eaux gazeuses, pluies, océans, sang. "
        "{cpl.3}Les acides carboxyliques : R C O O H sur R C O O moins. Vinaigre, citron, aspirine. "
        "{cpl.4}Et les amines : R N H trois plus sur R N H deux. L'odeur du poisson, les médicaments.",
        "{-cpl}{piege_am}Attention à l'erreur la plus fréquente du chapitre. Dans le couple des amines, l'acide, c'est l'ion ammonium. La base, c'est l'amine. "
        "Ce qui définit une amine, c'est le doublet non liant de son azote : elle capte un proton.",
        "{-piege_am}{co2}Un mot sur l'écriture C O deux, virgule, H deux O. Le dioxyde de carbone dissous reste associé à une molécule d'eau. "
        "On l'écrit ainsi plutôt que H deux C O trois : c'est la même espèce, mais la notation rappelle l'association. "
        "C'est cet acide qui rend une eau gazeuse acide, et qui acidifie les océans.",
        "{-co2}{fam}Les exercices ne disent jamais « voici un acide » : ils donnent une formule, ou un nom. Il faut reconnaître la famille. "
        "{fam.1}Le groupe carboxyle, C O O H : un acide carboxylique, dont le nom finit en « oïque ». "
        "{fam.2}Sa base, le groupe carboxylate, C O O moins : l'ion « oate ». "
        "{fam.3}Le groupe amino, N H deux : une amine. "
        "{fam.4}Son acide, le groupe N H trois plus : l'ion ammonium. "
        "{fam.5}En revanche, le O H d'un alcool n'a pas de caractère acide en pratique. Et un aldéhyde ou une cétone n'ont aucun hydrogène porté par l'oxygène : rien à céder.",
        "{-fam}{noms}Deux transformations de nom à savoir faire. {noms.1}De l'acide à sa base : la terminaison « oïque » devient « oate », et le mot acide disparaît. "
        "L'acide méthanoïque donne l'ion méthanoate ; l'acide palmitique, l'ion palmitate. "
        "{noms.2}De l'amine à son acide : « amine » devient « ammonium ». L'éthylamine donne l'ion éthylammonium.",
        "{-noms}{ethanal}Et un piège : l'éthanal, C H trois C H O. Il y a un oxygène, et un hydrogène juste à côté… mais cet hydrogène est lié au carbone, pas à l'oxygène. "
        "Aucun caractère acide. L'acide carboxylique, lui, porte deux oxygènes sur le même carbone, dont un avec un hydrogène.",
        "{-ethanal}{lewis_c}Enfin, le programme demande le schéma de Lewis des formes acide et basique. "
        "{lewis_c.1}Dans le carboxylate, l'oxygène qui a perdu son hydrogène porte la charge moins et trois doublets non liants ; l'autre oxygène, doublement lié, en porte deux. "
        "{lewis_c.2}Dans l'amine, l'azote porte trois liaisons et un doublet non liant. "
        "{lewis_c.3}Dans l'ion ammonium, ce doublet a servi à former une quatrième liaison avec un hydrogène : l'azote porte la charge plus, et plus aucun doublet.",
        "{-lewis_c}",
    ], vis={
        "cpl": dict(type="liste", titre="Les couples exigibles", items=[
            "L'eau : " + H3O + "/H_2O et H_2O/" + HO,
            "L'acide carbonique : (CO_2, H_2O)/HCO_3^{−} et HCO_3^{−}/CO_3^{2−}",
            "Les acides carboxyliques : R—COOH/R—COO^{−}",
            "Les amines : R—NH_3^{+}/R—NH_2"], marques=["1", "2", "3", "4"], x=130, y=150, w=1020),
        "piege_am": dict(type="note", titre="Le piège des amines", cles=["ammonium", "amine"],
                         t="Dans R—NH₃⁺/R—NH₂, l'acide est l'ion ammonium, la base est l'amine. Jamais l'inverse.", x=170, y=220, w=940),
        "co2": dict(type="note", titre="L'écriture (CO₂, H₂O)", cles=["associé", "océans"],
                    t="Le dioxyde de carbone dissous reste associé à une molécule d'eau : (CO₂, H₂O) plutôt que H₂CO₃. C'est l'acide des eaux gazeuses et des océans.",
                    x=170, y=200, w=940),
        "fam": dict(type="liste", titre="Reconnaître la famille", items=[
            "—COOH, carboxyle : acide carboxylique, « acide …oïque » · acide",
            "—COO^{−}, carboxylate : « ion …oate » · base",
            "—NH_2, amino : amine · base", "—NH_3^{+} : « ion …ammonium » · acide",
            "—OH d'alcool, —CHO, C=O : pas de caractère acide-base"], marques=["A", "B", "B", "A", "∅"], x=130, y=130, w=1020),
        "noms": dict(type="formule", titre="Changer de nom", x=150, y=170, w=980, lignes=[
            dict(f="acide …oïque → ion …oate", cadre=True, n="acide méthanoïque → ion méthanoate · acide palmitique → ion palmitate"),
            dict(f="…amine → ion …ammonium", cadre=True, n="éthylamine → ion éthylammonium")]),
        "ethanal": dict(type="note", titre="Le piège de l'éthanal", cles=["carbone", "deux oxygènes"],
                        t="Dans CH₃CHO, l'hydrogène du groupe —CHO est lié au carbone : aucun caractère acide. Un acide carboxylique porte deux oxygènes sur le même carbone, dont un avec un H.",
                        x=170, y=200, w=940),
        "lewis_c": dict(type="formule", titre="Lewis : formes acide et basique", x=150, y=150, w=980, lignes=[
            dict(f="R—COO^{−} : l'oxygène chargé porte 3 doublets non liants", txt=True, pt=True),
            dict(f="R—NH_2 : l'azote, 3 liaisons et 1 doublet non liant", txt=True, pt=True),
            dict(f="R—NH_3^{+} : l'azote, 4 liaisons, aucun doublet, charge +", txt=True, pt=True)]),
    }),

    # ================================================================ VII. polyacides
    dict(id="poly", chap="Polyacides et polybases", fond="nuit", humeur="calme",
         retenir="Polyacide à n protons : n couples, n + 1 espèces, n − 1 amphotères. Diacide qui réagit totalement : [H₃O⁺] = 2c (sinon, pH faux de 0,30).",
         beats=[
        "{poly}La définition dit : « un ou plusieurs » ions hydrogène. {poly.1}Un polyacide peut céder plusieurs protons : on dit diacide pour deux, triacide pour trois. "
        "L'acide sulfurique est un diacide. L'acide citrique du citron, avec ses trois groupes carboxyle, est un triacide. "
        "{poly.2}Une polybase peut en capter plusieurs : la putrescine, avec ses deux groupes amino, est une dibase.",
        "{-poly}{f_poly}Trois conséquences. {f_poly.1}Un polyacide capable de céder n protons forme n couples successifs, donc n plus une espèces en tout. "
        "{f_poly.2}Les espèces intermédiaires, il y en a n moins une, sont toutes amphotères. "
        "Pour l'acide phosphorique, H trois P O quatre, un triacide : trois couples, et deux espèces amphotères. "
        "{f_poly.3}Et pour le pH : un diacide qui réagit totalement libère deux ions oxonium par molécule. La concentration en ions oxonium vaut alors deux fois c, et non pas c. "
        "Oublier ce facteur décale le pH de log deux, zéro virgule trente.",
        "{f_poly.4}Enfin, les départs successifs ne sont pas équivalents : le premier proton part le plus facilement. "
        "Arracher un ion positif à une espèce déjà négative coûte plus cher.",
        "{-f_poly}",
    ], vis={
        "poly": dict(type="liste", titre="Polyacides et polybases", items=[
            "Polyacide : cède plusieurs H^{+} · H_2SO_4 diacide · acide citrique triacide",
            "Polybase : en capte plusieurs · la putrescine NH_2(CH_2)_4NH_2, dibase"], marques=["A", "B"], x=150, y=200, w=980),
        "f_poly": dict(type="formule", titre="Trois conséquences", x=150, y=110, w=980, lignes=[
            dict(f="n protons → n couples, n + 1 espèces", taille=40),
            dict(f="n − 1 espèces amphotères", taille=40, n="H_3PO_4 : H_2PO_4^{−} et HPO_4^{2−}"),
            dict(f="diacide, réaction totale : [" + H3O + "] = 2c", cadre=True, taille=40, n="oublier le 2 décale le pH de log 2 = 0,30"),
            dict(f="le premier proton part le plus facilement", txt=True)]),
    }),

    # ================================================================ VIII. le pH
    dict(id="ph", chap="Le pH", fond="aube", humeur="lumiere",
         retenir="pH = −log([H₃O⁺]/c°) et [H₃O⁺] = c° × 10⁻ᵖᴴ, avec c° = 1 mol·L⁻¹. Touches log et 10ˣ, jamais ln ni eˣ. Seules les décimales du pH sont significatives.",
         beats=[
        "{soren}Passons à la mesure. Dans une solution courante, la concentration en ions oxonium va de une mole par litre à dix puissance moins quatorze : "
        "quatorze ordres de grandeur. En mille neuf cent neuf, le chimiste danois Søren Sørensen a l'idée de passer au logarithme. Le pH est né.",
        "{-soren}{f_log}D'abord, l'outil mathématique. {f_log.1}Le logarithme décimal répond à la question : dix puissance combien donne ce nombre ? "
        "Log de dix puissance x égale x. "
        "{f_log.2}Log de un vaut zéro, log de cent vaut deux, log de zéro virgule zéro un vaut moins deux. "
        "{f_log.3}Multiplier un nombre par dix ajoute un à son log ; le diviser par dix retire un. Retiens bien cette propriété : toute la logique du pH est là.",
        "{-f_log}{f_ph}{f_ph.1}Voici la définition : le pH égale moins log de crochet H trois O plus, divisé par c zéro. "
        "{f_ph.2}c zéro, la concentration standard, vaut une mole par litre. Elle sert à rendre l'argument du logarithme sans unité. "
        "Conséquence : la concentration doit être en mole par litre, jamais en millimole par litre. "
        "{f_ph.3}Et la relation réciproque : crochet H trois O plus égale c zéro fois dix puissance moins pH.",
        "{f_ph.4}Plus il y a d'ions oxonium, plus le pH est petit. À vingt-cinq degrés : en dessous de sept, acide ; à sept, neutre ; au-dessus, basique.",
        "{-f_ph}{calc}Sur la calculatrice, deux pièges. {calc.1}Le log du pH est le logarithme décimal : la touche log. Jamais l n, le logarithme népérien des maths. "
        "{calc.2}Pour la réciproque, la touche dix puissance x, souvent en seconde fonction de log. Jamais e puissance x. "
        "Confondre les deux introduit un facteur mille, sans que rien n'ait l'air anormal.",
        "{-calc}{ex_ph}Un exemple. Une eau gazeuse a un pH de cinq virgule cinq. {ex_ph.1}Cinq virgule cinq est inférieur à sept : elle est acide, "
        "à cause du dioxyde de carbone dissous. "
        "{ex_ph.2}Crochet H trois O plus égale dix puissance moins cinq virgule cinq : "
        "{ex_ph.3}trois virgule deux fois dix puissance moins six mole par litre.",
        "{-ex_ph}{cs}Et une règle inhabituelle sur les chiffres significatifs. "
        "{cs.1}Seule la partie décimale du pH est significative : la partie entière ne fait qu'indiquer la puissance de dix. "
        "{cs.2}Une concentration donnée avec deux chiffres significatifs donne donc un pH à deux décimales. "
        "Trois virgule deux fois dix puissance moins six donne un pH de cinq virgule quarante-neuf. Pas cinq virgule cinq, ni cinq virgule quatre cent quatre-vingt-quatorze.",
        "{-cs}",
    ], vis={
        "soren": dict(type="portrait", annee=1909, img="c1-sorensen", nom="Søren Sørensen", dates="1868 – 1939",
                      legende="chimiste danois · 1909 : invente le pH"),
        "f_log": dict(type="formule", titre="Le logarithme décimal", x=150, y=130, w=980, lignes=[
            dict(f="log(10^{x}) = x  ⇔  10^{log x} = x", cadre=True),
            dict(f="log 1 = 0 · log 100 = 2 · log 0,01 = −2"),
            dict(f="× 10 sur le nombre  ⇔  + 1 sur le log", n="÷ 10 sur le nombre ⇔ − 1 sur le log")]),
        "f_ph": dict(type="formule", titre="Le pH", x=150, y=110, w=980, lignes=[
            dict(f="pH = − log ( [" + H3O + "] / c° )", cadre=True, taille=50),
            dict(f="c° = 1 mol·L^-1", n="[" + H3O + "] en mol·L^-1, obligatoirement"),
            dict(f="[" + H3O + "] = c° × 10^{−pH}", cadre=True, taille=46),
            dict(f="plus d'ions oxonium ⇒ pH plus petit · < 7 acide · 7 neutre · > 7 basique", txt=True)]),
        "calc": dict(type="liste", titre="Sur la calculatrice", items=[
            "pH : la touche log (base 10), jamais ln",
            "Réciproque : la touche 10^{x} (2nde + log), jamais e^{x} : sinon, un facteur mille"], marques=["log", "10ˣ"], x=150, y=200, w=980),
        "ex_ph": dict(type="formule", titre="Exemple · une eau gazeuse, pH = 5,5", x=150, y=150, w=980, lignes=[
            dict(f="5,5 < 7 : acide", n="le dioxyde de carbone dissous"),
            dict(f="[" + H3O + "] = 1 × 10^{−5,5}"),
            dict(f="[" + H3O + "] = 3,2 × 10^-6 mol·L^-1", cadre=True)]),
        "cs": dict(type="formule", titre="Les chiffres significatifs du pH", x=150, y=170, w=980, lignes=[
            dict(f="seule la partie décimale du pH est significative", txt=True, pt=True),
            dict(f="3,2 × 10^-6 mol·L^-1  →  pH = 5,49", cadre=True, n="2 chiffres significatifs → 2 décimales (pas 5,5 ni 5,494)")]),
    }),

    # ================================================================ IX. pH et dilution
    dict(id="dilution", chap="pH et dilution", fond="nuit", humeur="calme",
         retenir="Diviser la concentration par F augmente le pH de log F : diluer 10 fois → pH + 1 ; doubler la concentration → pH − 0,30.",
         beats=[
        "{an_dil}{dil_pts}{dil_pts.1}{an_dil.1}Que se passe-t-il quand on dilue un acide fort ? Regarde un même volume prélevé, à l'échelle des ions. "
        "Concentration dix puissance moins deux mole par litre : pH deux. On dilue dix fois : dix fois moins d'ions dans le même volume. "
        "Le pH passe à trois. Encore dix fois : pH quatre.",
        "{-an_dil}{-dil_pts}{f_dil2}{f_dil2.1}C'est la propriété du logarithme : diviser la concentration par un facteur F ne divise pas le pH. Elle l'augmente de log F. "
        "{f_dil2.2}Diluer dix fois fait monter le pH d'exactement une unité. "
        "{f_dil2.3}Doubler la concentration le fait baisser de log deux, soit zéro virgule trente.",
        "{-f_dil2}{ex_no3}Un exemple classique d'exercice. On prépare cinquante millilitres de solution avec un gramme d'acide nitrique, "
        "qui réagit totalement avec l'eau. "
        "{ex_no3.1}Sa masse molaire vaut soixante-trois grammes par mole. n égale m sur M : un virgule six fois dix puissance moins deux mole. "
        "{ex_no3.2}c égale n sur V : zéro virgule trente-deux mole par litre. "
        "{ex_no3.3}Un monoacide, une réaction totale : la concentration en ions oxonium égale c. Le pH vaut moins log de zéro virgule trente-deux : zéro virgule cinquante. "
        "Un pH très bas, mais normal pour un acide fort aussi concentré. "
        "{ex_no3.4}Et si on doublait la quantité d'acide, le pH baisserait de zéro virgule trente : zéro virgule vingt.",
        "{-ex_no3}{poh}Une échelle miroir, utile en exercice : {poh.1}le p O H, moins log de la concentration en ions hydroxyde. "
        "{poh.2}Le produit des concentrations en ions oxonium et hydroxyde vaut dix puissance moins quatorze à vingt-cinq degrés : c'est le produit ionique de l'eau. "
        "{poh.3}Passé au logarithme, il devient : pH plus p O H égale quatorze. C'est commode quand l'espèce apportée est une base.",
        "{-poh}",
    ], vis={
        "an_dil": dict(type="anim", nom="acidebase", x=40, y=72, h=624, seg=[[50.8, 59.5]]),
        "dil_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=170, w=560, items=[
            "[" + H3O + "] ÷ 10 à chaque dilution : pH 2, puis 3, puis 4"]),
        "f_dil2": dict(type="formule", titre="pH et dilution", x=150, y=150, w=980, lignes=[
            dict(f="c → " + fr("c", "F") + "  ⇒  pH → pH + log F", cadre=True, taille=46),
            dict(f="diluer 10 fois : pH + 1"),
            dict(f="doubler la concentration : pH − 0,30", n="log 2 ≈ 0,30")]),
        # n = 1,0 / 63,0 = 1,59e-2 mol ; c = 1,59e-2 / 0,0500 = 0,317 mol/L ; pH = −log(0,317) = 0,498 ≈ 0,50 ; 2c : 0,20
        "ex_no3": dict(type="formule", titre="Exemple · 1,0 g d'acide nitrique dans 50,0 mL", x=150, y=110, w=980, lignes=[
            dict(f="n = " + fr("m", "M") + " = " + fr("1,0", "63,0") + " = 1,6 × 10^-2 mol", taille=38),
            dict(f="c = " + fr("n", "V") + " = " + fr("1,6 × 10^-2", "50,0 × 10^-3") + " = 0,32 mol·L^-1", taille=38),
            dict(f="totale, monoacide : [" + H3O + "] = c ; pH = −log(0,317) = 0,50", cadre=True, taille=36),
            dict(f="quantité doublée : pH = 0,50 − 0,30 = 0,20", taille=36)]),
        "poh": dict(type="formule", titre="Utile en exercice · le pOH", x=150, y=150, w=980, lignes=[
            dict(f="pOH = − log ( [" + HO + "] / c° )"),
            dict(f="[" + H3O + "] × [" + HO + "] / (c°)^{2} = K_e = 10^-14", n="produit ionique de l'eau, à 25 °C"),
            dict(f="pH + pOH = 14", cadre=True)]),
    }),

    # ================================================================ X. TP 1
    dict(id="tp1", chap="Expérience : tester la relation", fond="nuit", humeur="tension",
         retenir="Critère : |pH_mes − pH_théo| / u(pH) ≤ 2, avec u(pH) = 0,1. Seules S₃ et S₄ passent : un modèle a un domaine de validité.",
         beats=[
        "{tab_phm}Au laboratoire, on peut tester cette relation. {tp_prot}{tp_prot.1}Six solutions d'acide chlorhydrique, de une mole par litre à dix puissance moins cinq, "
        "obtenues par dilutions successives d'un facteur dix. "
        "{tp_prot.2}Le matériel : une pipette jaugée de dix millilitres, et une fiole jaugée de cent millilitres. Une pipette jaugée, pas graduée : "
        "sur cinq dilutions enchaînées, les erreurs s'accumulent. "
        "{tp_prot.3}Le pH-mètre est d'abord étalonné, avec un tampon de pH sept, puis de pH quatre. "
        "{tp_prot.4}On rince l'électrode entre chaque solution, et on mesure de la plus diluée à la plus concentrée.",
        "{-tp_prot}{-tab_phm}{gr_tp}Voici une série de mesures réalisées au laboratoire, tracées en fonction de moins log c. "
        "{gr_tp.1}Si la relation était parfaite, les points seraient sur cette droite de pente un. "
        "{gr_tp.2}Les mesures : zéro virgule cinquante-trois, un virgule quarante, deux virgule vingt-six, trois virgule zéro quatre, quatre virgule seize, cinq virgule soixante-six. "
        "L'accord est excellent au milieu, et se dégrade aux deux extrémités.",
        "{-gr_tp}{f_crit}Comment juger objectivement ? {f_crit.1}Avec le critère de compatibilité : l'écart entre la mesure et la valeur théorique, "
        "divisé par l'incertitude-type, doit être inférieur ou égal à deux. "
        "{f_crit.2}On prend une incertitude de zéro virgule un sur le pH. Pas zéro virgule zéro un parce que l'écran affiche deux décimales : "
        "l'étalonnage, la dérive de l'électrode et l'agitation dominent. "
        "{f_crit.3}Les quotients valent cinq virgule trois, quatre, deux virgule six, zéro virgule quatre, un virgule six, et six virgule six. "
        "{f_crit.4}Seules S trois et S quatre passent le test.",
        "{-f_crit}{causes}Ce n'est pas une erreur de manipulation : c'est le point le plus intéressant de l'expérience. "
        "{causes.1}Côté concentré, les ions sont si nombreux qu'ils interagissent : leur concentration efficace est plus faible que prévu, et le pH mesuré est trop élevé. "
        "{causes.2}Côté dilué, l'eau elle-même et surtout le dioxyde de carbone de l'air, dissous dans l'eau distillée, apportent des ions oxonium. "
        "{causes.3}Et cinq dilutions en cascade accumulent les erreurs de pipetage.",
        "{-causes}{concl}La conclusion à savoir rédiger : la relation est validée dans un domaine intermédiaire de concentration, "
        "et cesse de décrire les solutions très concentrées ou très diluées. "
        "Un modèle a toujours un domaine de validité : savoir le délimiter fait partie de la compétence évaluée.",
        "{-concl}",
    ], vis={
        "tab_phm": dict(type="tableau", img="c1-phmetre", fond=True, sombre=True, de=[1.0, .5, .72], a=[1.3, .5, .78],
                        legende="pH-mètre de laboratoire, photo OER CampLev, CC BY-SA 4.0"),
        "tp_prot": dict(type="liste", titre="Expérience · le protocole", items=[
            "Six solutions de HCl, de 1,0 à 10^-5 mol·L^-1, diluées de 10 en 10",
            "Pipette jaugée de 10,0 mL + fiole jaugée de 100,0 mL (jamais graduée)",
            "Étalonnage : tampon pH 7, puis tampon pH 4",
            "Rincer l'électrode · mesurer de la plus diluée à la plus concentrée"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "gr_tp": dict(type="graphe", titre="Expérience · pH mesuré en fonction de −log c", x=330, y=100, w=640, h=540,
                      ax=dict(x=[0, 6], y=[0, 6], gx=[1, 2, 3, 4, 5], gy=[1, 2, 3, 4, 5], lx="−log c", ly="pH"),
                      el=[dict(type="droite", pts=[[0, 0], [5.8, 5.8]], c="el", tir=True, lbl="théorie : pH = −log c", lp=[0.4, 5.4]),
                          dict(type="points", pts=[list(p) for p in TP1], c="sa", pas=.35)]),
        "f_crit": dict(type="formule", titre="Le critère de compatibilité", x=150, y=110, w=980, lignes=[
            dict(f="|pH_{mes} − pH_{théo}| / u(pH) ≤ 2", cadre=True, taille=46),
            dict(f="u(pH) = 0,1", n="pas la résolution de l'écran"),
            dict(f="S_0 à S_5 : 5,3 · 4,0 · 2,6 · 0,4 · 1,6 · 6,6", taille=38),
            dict(f="seules S_3 et S_4 sont compatibles", ok=True, taille=38)]),
        "causes": dict(type="liste", titre="Pourquoi le modèle décroche aux extrémités", items=[
            "Trop concentré : les ions interagissent, pH mesuré trop élevé",
            "Trop dilué : l'eau et le CO_2 de l'air apportent des " + H3O,
            "Cinq dilutions en cascade : les erreurs s'accumulent"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "concl": dict(type="note", titre="La conclusion à rédiger", cles=["domaine", "validité"],
                      t="pH = −log([H₃O⁺]/c°) est validée dans un domaine intermédiaire de concentration. Un modèle a toujours un domaine de validité.",
                      x=170, y=210, w=940),
    }),

    # ================================================================ XI. totale ou limitée
    dict(id="totale", chap="Réaction totale ou limitée ?", fond="aube", humeur="tension",
         retenir="pH mesuré = pH théorique : réaction totale (→). pH mesuré > pH théorique : réaction limitée (⇌). Plus petit : impossible, erreur de calcul.",
         beats=[
        "{q_tot}Dernière notion du chapitre, et la plus fréquente au bac. Le chlorure d'hydrogène réagit totalement avec l'eau : on écrit une flèche simple. "
        "L'acide éthanoïque ne réagit que partiellement : double flèche. Comment le sait-on ?",
        "{-q_tot}{meth}En comparant le pH mesuré au pH qu'on aurait si tout avait réagi. La méthode, en cinq étapes. "
        "{meth.1}Un : écrire l'équation de la réaction de l'acide avec l'eau. "
        "{meth.2}Deux : calculer la quantité d'acide initiale : n égale c fois V, ou m sur M. "
        "{meth.3}Trois : dresser le tableau d'avancement, et trouver l'avancement maximal, celui d'une réaction totale. "
        "{meth.4}Quatre : en déduire la concentration maximale en ions oxonium, puis le pH théorique. "
        "{meth.5}Cinq : comparer au pH mesuré, et conclure.",
        "{-meth}{ex_ac}Exemple traité. Cent millilitres d'acide éthanoïque, à un virgule zéro fois dix puissance moins deux mole par litre. Le pH mesuré vaut deux virgule huit. "
        "{ex_ac.1}L'équation : C H trois C O O H, plus H deux O, double flèche, C H trois C O O moins, plus H trois O plus. "
        "{ex_ac.2}n initial égale c fois V : un virgule zéro fois dix puissance moins trois mole. "
        "{ex_ac.3}L'eau est le solvant, en large excès : l'acide est le réactif limitant, et x max vaut un virgule zéro fois dix puissance moins trois mole. "
        "{ex_ac.4}La concentration maximale en ions oxonium vaut x max sur V : dix puissance moins deux mole par litre. Le pH théorique vaut deux virgule zéro zéro.",
        "{ex_ac.5}Or on mesure deux virgule huit : c'est plus grand. Il s'est formé moins d'ions oxonium que si tout avait réagi. La réaction est limitée. "
        "{ex_ac.6}On peut même chiffrer : dix puissance moins deux virgule huit, c'est un virgule six fois dix puissance moins trois mole par litre. "
        "Environ seize pour cent de l'acide a réagi.",
        "{-ex_ac}{an_tot}{tot_pts}{tot_pts.1}{an_tot.1}Visualise-le. À gauche, l'acide chlorhydrique : toutes les molécules ont réagi, pH deux. "
        "À droite, l'acide éthanoïque, à la même concentration : quatre sur vingt-cinq seulement, pH deux virgule huit. "
        "Et ce n'est pas figé : des molécules se dissocient pendant que d'autres se reforment.",
        "{-an_tot}{-tot_pts}{concl2}La conclusion, dans les deux sens. {concl2.1}Si le pH mesuré égale le pH théorique, tout l'acide a réagi : réaction totale, flèche simple. "
        "{concl2.2}Si le pH mesuré est plus grand, il manque des ions oxonium : réaction limitée, double flèche. "
        "{concl2.3}Un pH mesuré plus petit que le pH théorique est impossible : on ne peut pas produire plus d'ions oxonium que l'acide n'en contient. "
        "Si tu trouves ça, cherche l'erreur de calcul.",
        "{-concl2}{rq_tab}Deux remarques. La valeur de deux virgule huit est celle de cet exemple ; les tables de données donnent plutôt trois virgule quatre "
        "à cette concentration, mais la conclusion est la même. "
        "Et cette distinction sera quantifiée au chapitre suivant, avec le taux d'avancement et la constante d'acidité. "
        "Pour l'instant, il suffit de savoir trancher à partir d'un pH mesuré.",
        "{-rq_tab}",
    ], vis={
        "q_tot": dict(type="question", t="HCl : flèche simple. Acide éthanoïque : double flèche. Comment le sait-on ?"),
        "meth": dict(type="liste", titre="La méthode en cinq étapes", items=[
            "Écrire l'équation de la réaction de l'acide avec l'eau", "n_{acide} = c × V (ou m / M)",
            "Tableau d'avancement : x_{max}, si la réaction était totale", "[" + H3O + "]_{max} = x_{max} / V, puis pH_{théo}",
            "Comparer au pH mesuré, et conclure"], marques=["1", "2", "3", "4", "5"], x=150, y=130, w=980),
        # n = 1,0e-2 × 0,100 = 1,0e-3 mol ; [H3O+]max = 1,0e-2 ; pH théo = 2,00 ; 10^-2,8 = 1,58e-3 → 16 %
        "ex_ac": dict(type="formule", titre="Exemple · acide éthanoïque, 100 mL, pH = 2,8", x=110, y=96, w=1060, lignes=[
            dict(f="CH_3COOH + H_2O ⇌ CH_3COO^{−} + " + H3O, taille=34),
            dict(f="n_i = c × V = 1,0 × 10^-2 × 0,100 = 1,0 × 10^-3 mol", taille=34),
            dict(f="l'eau est en excès : x_{max} = 1,0 × 10^-3 mol", taille=34),
            dict(f="[" + H3O + "]_{max} = " + fr("x_{max}", "V") + " = 1,0 × 10^-2 mol·L^-1 · pH_{théo} = 2,00", taille=34),
            dict(f="2,8 > 2,00 : réaction limitée (⇌)", cadre=True, taille=34),
            dict(f="10^{−2,8} = 1,6 × 10^-3 mol·L^-1 : environ 16 % a réagi", taille=32)]),
        "an_tot": dict(type="anim", nom="acidebase", x=40, y=72, h=624, seg=[[61.8, 74]]),
        "tot_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=170, w=560, items=[
            "Même concentration : HCl, 25 sur 25 ont réagi, pH 2,0 · acide éthanoïque, 4 sur 25, pH 2,8"]),
        "concl2": dict(type="liste", titre="Conclure", items=[
            "pH_{mes} = pH_{théo} : réaction totale, flèche simple →",
            "pH_{mes} > pH_{théo} : réaction limitée, double flèche ⇌",
            "pH_{mes} < pH_{théo} : impossible, cherche l'erreur"], marques=["→", "⇌", "✗"], x=150, y=170, w=980),
        "rq_tab": dict(type="note", titre="Deux remarques", cles=["tables", "chapitre suivant"],
                       t="2,8 est la valeur de cet exemple ; les tables donnent plutôt 3,4 à cette concentration (même conclusion). Taux d'avancement et constante d'acidité : au chapitre suivant.",
                       x=170, y=200, w=940),
    }),

    # ================================================================ XII. exercice 1 (simple)
    # pH 3,20 → [H3O+] = 10^-3,20 = 6,31e-4 mol/L ; c = 3,5e-3 : pH théo = −log(3,5e-3) = 2,46 ; 6,3e-4 / 3,5e-3 = 0,18 → 18 %
    # (cohérent avec les tables : pKa de l'acide lactique 3,86, c ≈ h²/Ka + h = 2,9e-3 + 0,6e-3 = 3,5e-3)
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. L'acide lactique se forme dans le lait qui fermente, et dans les muscles à l'effort. "
        "Sa formule : C H trois, C H O H, C O O H. "
        "Quatre questions : ses groupes caractéristiques et son hydrogène acide ; son couple et le nom de sa base ; la concentration en ions oxonium d'une solution de pH trois virgule vingt ; "
        "et enfin, la réaction avec l'eau est-elle totale ?",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche les quatre questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}C'est parti pour la correction. {s11}{s11.1}Question un : deux groupes caractéristiques. Le groupe hydroxyle, O H, celui d'un alcool, "
        "{s11.2}et le groupe carboxyle, C O O H. C'est donc un acide carboxylique. "
        "{s11.3}L'hydrogène acide est celui du groupe carboxyle, porté par un oxygène. Le O H de l'alcool, lui, n'a pas de caractère acide en pratique.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux : on retire un H et une charge plus au groupe carboxyle. "
        "{s12.2}La base conjuguée est l'ion lactate : acide lactique donne ion lactate, comme acide palmitique donne ion palmitate. "
        "{s12.3}Le couple s'écrit l'acide en premier : acide lactique sur ion lactate. Et l'équation protonique : l'acide, double flèche, l'ion lactate plus H plus.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : la relation réciproque. Crochet H trois O plus égale c zéro fois dix puissance moins pH. "
        "{s13.2}Dix puissance moins trois virgule vingt : {s13.3}six virgule trois fois dix puissance moins quatre mole par litre. "
        "Deux décimales sur le pH, deux chiffres significatifs sur la concentration.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre : la méthode en cinq étapes. Si la réaction était totale, la concentration en ions oxonium serait égale à c, "
        "trois virgule cinq fois dix puissance moins trois mole par litre. "
        "{s14.2}Le pH théorique vaudrait deux virgule quarante-six. "
        "{s14.3}On mesure trois virgule vingt : c'est plus grand. Il manque des ions oxonium : la réaction est limitée, on écrit une double flèche. "
        "{s14.4}Seulement six virgule trois fois dix puissance moins quatre sur trois virgule cinq fois dix puissance moins trois, soit environ dix-huit pour cent de l'acide, a réagi.",
        "{-s14}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="L'acide lactique", src="Exercice inventé pour la vidéo",
                    enonce=["L'acide lactique, formé dans le lait qui fermente et dans les muscles à l'effort, a pour formule CH_3—CH(OH)—COOH. "
                            "Une solution d'acide lactique de concentration apportée c = 3,5 × 10^-3 mol·L^-1 a un pH de 3,20."],
                    donnees=["c° = 1 mol·L^-1"],
                    questions=["Nommer ses groupes caractéristiques ; identifier l'hydrogène responsable du caractère acide.",
                               "Écrire le couple acide-base et nommer la base conjuguée.",
                               "Calculer la concentration en ions oxonium de la solution.",
                               "La réaction de l'acide lactique avec l'eau est-elle totale ? Écrire son équation."]),
        "pa1": dict(type="pause", t="Groupes et hydrogène acide, couple, [H₃O⁺], réaction totale ou limitée."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="L'acide lactique",
                     donnees=["CH_3—CH(OH)—COOH", "c = 3,5 × 10^-3 mol·L^-1", "pH = 3,20"],
                     questions=["Groupes ? H acide ?", "Couple ? Base ?", "[" + H3O + "] ?", "Totale ?"]),
        "s11": dict(type="formule", titre="1 · Groupes caractéristiques", x=540, y=150, w=700, lignes=[
            dict(f="—OH : hydroxyle (alcool)", taille=36), dict(f="—COOH : carboxyle", taille=36),
            dict(f="H acide : celui du —COOH, porté par O", cadre=True, taille=34)]),
        "s12": dict(type="formule", titre="2 · Le couple", x=540, y=130, w=700, lignes=[
            dict(f="on retire H et une charge + à —COOH", txt=True),
            dict(f="base : ion lactate CH_3—CH(OH)—COO^{−}", taille=32),
            dict(f="CH_3CH(OH)COOH ⇌ CH_3CH(OH)COO^{−} + H^{+}", cadre=True, taille=28, n="couple acide lactique / ion lactate")]),
        "s13": dict(type="formule", titre="3 · La concentration en ions oxonium", x=540, y=150, w=700, lignes=[
            dict(f="[" + H3O + "] = c° × 10^{−pH}", taille=38), dict(f="[" + H3O + "] = 10^{−3,20}", taille=38),
            dict(f="[" + H3O + "] = 6,3 × 10^-4 mol·L^-1", cadre=True, taille=38)]),
        "s14": dict(type="formule", titre="4 · Totale ou limitée ?", x=540, y=110, w=700, lignes=[
            dict(f="si totale : [" + H3O + "]_{max} = c = 3,5 × 10^-3 mol·L^-1", taille=30),
            dict(f="pH_{théo} = −log(3,5 × 10^-3) = 2,46", taille=32),
            dict(f="3,20 > 2,46 : réaction limitée (⇌)", cadre=True, taille=32),
            dict(f=fr("6,3 × 10^-4", "3,5 × 10^-3") + " ≈ 0,18 : 18 % a réagi", taille=32)]),
    }),

    # ================================================================ XIII. exercice 2 (difficile)
    # c = 5,0e-3 : pH théo = 2,30 ; B : 10^-3,60 = 2,51e-4 → 5,0 % (pKa réel 4,87 : pH calculé 3,60) ;
    # A dilué : pH 3,60 ⇒ log F = 3,60 − 2,30 = 1,30 ⇒ F = 20 ; 100,0 mL / 20 = 5,00 mL ; B dilué 20 fois : pH ≈ 4,28 (+0,68 < 1,30)
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile, parce qu'il croise tout le chapitre. Deux flacons sans étiquette, A et B, contiennent chacun une solution "
        "à cinq virgule zéro fois dix puissance moins trois mole par litre : l'un d'acide chlorhydrique, l'autre d'acide propanoïque. "
        "On mesure un pH de deux virgule trente pour A, et de trois virgule soixante pour B.",
        "On demande : le pH qu'aurait chaque solution si la réaction avec l'eau était totale ; l'identité de chaque flacon, avec les deux équations ; "
        "la proportion d'acide propanoïque qui a réagi ; comment préparer, en diluant A, cent millilitres d'une solution de même pH que B ; "
        "et enfin : le pH de B, dilué de la même façon, augmenterait-il autant ?",
        "{-ex2}{pa2}Celui-là demande du temps. Mets sur pause, et fais-le en entier avant de regarder la correction.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un : si la réaction était totale, chaque molécule d'acide donnerait un ion oxonium. "
        "La concentration en ions oxonium vaudrait c. "
        "{s21.2}Le pH vaudrait moins log de cinq virgule zéro fois dix puissance moins trois : {s21.3}deux virgule trente, pour les deux flacons.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux : pour A, le pH mesuré égale le pH théorique : réaction totale. C'est l'acide chlorhydrique. "
        "{s22.2}Pour B, trois virgule soixante est plus grand que deux virgule trente : réaction limitée. C'est l'acide propanoïque, un acide carboxylique. "
        "{s22.3}Les équations : H C l plus H deux O donne C l moins plus H trois O plus, avec une flèche simple. "
        "{s22.4}Et C H trois C H deux C O O H, plus H deux O, double flèche, l'ion propanoate, plus H trois O plus.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois : dans B, crochet H trois O plus égale dix puissance moins trois virgule soixante, "
        "{s23.2}soit deux virgule cinq fois dix puissance moins quatre mole par litre. "
        "{s23.3}Divisé par cinq virgule zéro fois dix puissance moins trois : zéro virgule zéro cinq. Seulement cinq pour cent des molécules ont réagi.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre : A est un acide fort. Diluer d'un facteur F augmente son pH de log F. "
        "Il faut passer de deux virgule trente à trois virgule soixante : log F égale un virgule trente. "
        "{s24.2}Donc F égale dix puissance un virgule trente : vingt. "
        "{s24.3}Pour cent millilitres de solution fille, on prélève cent sur vingt, cinq millilitres. "
        "{s24.4}Le matériel : une pipette jaugée de cinq millilitres, une fiole jaugée de cent millilitres, et un bécher pour y verser un peu de A.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq : non. La relation pH plus log F suppose que la concentration en ions oxonium égale c, "
        "c'est-à-dire une réaction totale. "
        "{s25.2}Pour une réaction limitée, diluer favorise la réaction avec l'eau : une plus grande proportion de molécules réagit, ce qui compense en partie la dilution. "
        "{s25.3}Le pH de B augmente donc de moins de un virgule trente. C'est le cas de l'acide éthanoïque : dilué dix fois, son pH ne monte que de zéro virgule six environ.",
        "{-s25}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=50, titre="Deux flacons sans étiquette", src="Exercice inventé pour la vidéo",
                    enonce=["Les flacons A et B contiennent des solutions de même concentration apportée c = 5,0 × 10^-3 mol·L^-1 : "
                            "l'une d'acide chlorhydrique, l'autre d'acide propanoïque CH_3CH_2COOH. On mesure pH_A = 2,30 et pH_B = 3,60."],
                    questions=["pH de chaque solution si la réaction avec l'eau était totale ?",
                               "Identifier chaque flacon ; écrire les deux équations avec la bonne flèche.",
                               "Quelle proportion des molécules d'acide propanoïque a réagi ?",
                               "Préparer, en diluant A, 100,0 mL de même pH que B : facteur, verrerie.",
                               "Diluée de même, B verrait-elle son pH augmenter autant ?"]),
        "pa2": dict(type="pause", t="pH si totale, identité des flacons, proportion, dilution de A, et le cas de B."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Deux flacons",
                     donnees=["c = 5,0 × 10^-3 mol·L^-1", "pH_A = 2,30", "pH_B = 3,60"],
                     questions=["pH si totale ?", "Qui est qui ?", "Proportion ?", "Diluer A ?", "B dilué ?"]),
        "s21": dict(type="formule", titre="1 · Si la réaction était totale", x=540, y=150, w=700, lignes=[
            dict(f="[" + H3O + "]_{max} = c", taille=38), dict(f="pH = −log(5,0 × 10^-3)", taille=38),
            dict(f="pH_{théo} = 2,30", cadre=True, taille=38)]),
        "s22": dict(type="formule", titre="2 · Qui est qui ?", x=540, y=110, w=700, lignes=[
            dict(f="A : 2,30 = 2,30 · totale : acide chlorhydrique", taille=30),
            dict(f="B : 3,60 > 2,30 · limitée : acide propanoïque", taille=30),
            dict(f="HCl + H_2O → Cl^{−} + " + H3O, cadre=True, taille=32),
            dict(f="CH_3CH_2COOH + H_2O ⇌ CH_3CH_2COO^{−} + " + H3O, cadre=True, taille=26)]),
        "s23": dict(type="formule", titre="3 · La proportion qui a réagi", x=540, y=150, w=700, lignes=[
            dict(f="[" + H3O + "] = 10^{−3,60}", taille=38), dict(f="[" + H3O + "] = 2,5 × 10^-4 mol·L^-1", taille=38),
            dict(f=fr("2,5 × 10^-4", "5,0 × 10^-3") + " = 0,050 : 5,0 %", cadre=True, taille=36)]),
        "s24": dict(type="formule", titre="4 · Diluer A", x=540, y=120, w=700, lignes=[
            dict(f="log F = 3,60 − 2,30 = 1,30", taille=36), dict(f="F = 10^{1,30} = 20", cadre=True, taille=36),
            dict(f="V_{mère} = " + fr("100,0 mL", "20") + " = 5,00 mL", taille=34),
            dict(f="pipette jaugée de 5,00 mL · fiole jaugée de 100,0 mL · bécher", txt=True)]),
        "s25": dict(type="formule", titre="5 · Et si on diluait B ?", x=540, y=130, w=700, lignes=[
            dict(f="pH + log F suppose [" + H3O + "] = c : réaction totale", txt=True),
            dict(f="limitée : diluer fait réagir une plus grande proportion", txt=True),
            dict(f="le pH de B monte de moins de 1,30", cadre=True, taille=34, n="exemple : acide éthanoïque dilué 10 fois, + 0,6 seulement")]),
    }),

    # ================================================================ XIV. exercice 3 (type bac)
    # 10^-5,6 = 2,5e-6 ; 10^-4,2 = 6,3e-5 ; rapport 10^1,4 = 25 ; HNO3 : c ≈ 6,3e-5 mol/L, m = 6,3e-5 × 63,0 = 4,0e-3 g = 4,0 mg par litre ;
    # part naturelle négligée : 2,5e-6 / 6,3e-5 = 4 % ; u(pH) = 0,1 : [H3O+] entre 10^-4,3 = 5,0e-5 et 10^-4,1 = 7,9e-5
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac : une analyse de documents, sur les pluies acides. "
        "Document un : une pluie non polluée est naturellement acide, car le dioxyde de carbone de l'air s'y dissout ; son pH est voisin de cinq virgule six. "
        "Document deux : dans une ville industrielle, une pluie a un pH de quatre virgule deux, mesuré avec une incertitude de zéro virgule un. "
        "Son acidité supplémentaire vient surtout de l'acide nitrique, qui réagit totalement avec l'eau.",
        "Document trois : le calcaire des monuments contient des ions carbonate. Les ions oxonium de la pluie les transforment en ions hydrogénocarbonate, et la pierre se dégrade.",
        "{-ex3}{ex3b}Cinq questions. Un : l'équation de la réaction du dioxyde de carbone dissous avec l'eau, et pourquoi la pluie naturelle est acide. "
        "Deux : la concentration en ions oxonium des deux pluies, et combien de fois la pluie polluée est plus acide. "
        "Trois : montrer que l'ion hydrogénocarbonate est amphotère. "
        "Quatre : l'équation de l'attaque du calcaire. "
        "Cinq : estimer la masse d'acide nitrique par litre de pluie polluée, et porter un regard critique sur ce résultat.",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}{s31.1}Question un : le dioxyde de carbone dissous est l'acide du couple C O deux, H deux O, sur H C O trois moins. "
        "L'eau joue le rôle de base. "
        "{s31.2}C O deux, H deux O, plus H deux O, double flèche, H C O trois moins, plus H trois O plus. "
        "{s31.3}Couples : C O deux, H deux O, sur H C O trois moins, et H trois O plus sur H deux O. "
        "{s31.4}La réaction produit des ions oxonium : leur concentration dépasse celle de l'eau pure, et le pH descend sous sept. Voilà pourquoi même une pluie propre est acide.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Question deux : la relation réciproque. Pour la pluie naturelle : dix puissance moins cinq virgule six, deux virgule cinq fois dix puissance moins six mole par litre. "
        "{s32.2}Pour la pluie polluée : dix puissance moins quatre virgule deux, six virgule trois fois dix puissance moins cinq. "
        "{s32.3}Le rapport se lit directement sur l'écart de pH : dix puissance un virgule quatre, environ vingt-cinq. "
        "Pour seulement un virgule quatre unité de pH, vingt-cinq fois plus d'ions oxonium.",
        "{-s32}{ex3c.q3}{s33}{s33.1}Question trois : il faut deux demi-équations. Comme acide, l'ion hydrogénocarbonate cède un proton : "
        "H C O trois moins, double flèche, C O trois deux moins, plus H plus. "
        "{s33.2}Comme base, il en capte un : H C O trois moins, plus H plus, double flèche, C O deux, H deux O. "
        "{s33.3}Il possède les deux caractères : il est amphotère. C'est l'espèce commune aux deux couples de l'acide carbonique.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Question quatre : l'ion carbonate est la base du couple ion hydrogénocarbonate, ion carbonate ; l'ion oxonium est l'acide du couple de l'eau. "
        "{s34.2}L'ion carbonate, plus H trois O plus, donne l'ion hydrogénocarbonate, plus H deux O. "
        "{s34.3}Les ions carbonate, qui constituent la pierre, sont consommés : plus la pluie est acide, plus le calcaire est attaqué.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq, la résolution de problème. On attribue les ions oxonium de la pluie polluée à l'acide nitrique, un monoacide qui réagit totalement : "
        "sa concentration vaut environ six virgule trois fois dix puissance moins cinq mole par litre. "
        "{s35.2}Masse par litre : la concentration fois la masse molaire, soit six virgule trois fois dix puissance moins cinq, fois soixante-trois. Environ quatre milligrammes.",
        "{s35.3}Et le regard critique, toujours valorisé. On a négligé l'acidité naturelle : deux virgule cinq fois dix puissance moins six, "
        "à peine quatre pour cent de la valeur totale. C'est justifié. "
        "{s35.4}Mais avec une incertitude de zéro virgule un sur le pH, la concentration est comprise entre cinq fois dix puissance moins cinq et huit fois dix puissance moins cinq : "
        "environ vingt-cinq pour cent d'incertitude. {s35.5}Le résultat n'est qu'un ordre de grandeur : quelques milligrammes par litre.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Les pluies acides", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Doc 1 · Une pluie non polluée est naturellement acide : le dioxyde de carbone de l'air s'y dissout. Son pH est voisin de 5,6.",
                            "Doc 2 · Dans une ville industrielle, une pluie a un pH de 4,2 (u(pH) = 0,1). Son acidité supplémentaire vient surtout de l'acide nitrique HNO_3, qui réagit totalement avec l'eau.",
                            "Doc 3 · Le calcaire des monuments contient des ions carbonate CO_3^{2−}. Les ions oxonium les transforment en ions hydrogénocarbonate : la pierre se dégrade."],
                    donnees=["M(HNO_3) = 63,0 g·mol^-1", "couples : (CO_2, H_2O)/HCO_3^{−} et HCO_3^{−}/CO_3^{2−}"]),
        "ex3b": dict(type="exo", niveau="bac", titre="Les pluies acides · questions",
                     questions=["Écrire l'équation de la réaction du dioxyde de carbone dissous avec l'eau ; expliquer pourquoi la pluie naturelle est acide.",
                                "Calculer [H_3O^{+}] dans les deux pluies. Combien de fois la pluie polluée est-elle plus acide ?",
                                "Montrer que l'ion hydrogénocarbonate est amphotère.",
                                "Écrire l'équation de la réaction des ions oxonium avec les ions carbonate du calcaire.",
                                "Estimer la masse d'acide nitrique par litre de pluie polluée. Porter un regard critique sur ce résultat."]),
        "pa3": dict(type="pause", t="Équation et couples, deux concentrations, amphotère, attaque du calcaire, masse et regard critique."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Les pluies acides",
                     donnees=["pluie naturelle : pH 5,6", "pluie polluée : pH 4,2", "u(pH) = 0,1", "M(HNO_3) = 63,0 g·mol^-1"],
                     questions=["CO_2 et l'eau ?", "[" + H3O + "] ? Rapport ?", "HCO_3^{−} amphotère ?", "Le calcaire ?", "Masse, regard critique ?"]),
        "s31": dict(type="formule", titre="1 · Le dioxyde de carbone et l'eau", x=540, y=110, w=700, lignes=[
            dict(f="(CO_2, H_2O) : l'acide · l'eau : la base", txt=True),
            dict(f="(CO_2, H_2O) + H_2O ⇌ HCO_3^{−} + " + H3O, cadre=True, taille=30),
            dict(f="couples (CO_2, H_2O)/HCO_3^{−} et " + H3O + "/H_2O", taille=28),
            dict(f="des " + H3O + " sont produits : pH < 7", txt=True)]),
        "s32": dict(type="formule", titre="2 · Deux concentrations, un rapport", x=540, y=140, w=700, lignes=[
            dict(f="naturelle : 10^{−5,6} = 2,5 × 10^-6 mol·L^-1", taille=32),
            dict(f="polluée : 10^{−4,2} = 6,3 × 10^-5 mol·L^-1", taille=32),
            dict(f="rapport : 10^{5,6 − 4,2} = 10^{1,4} ≈ 25", cadre=True, taille=34)]),
        "s33": dict(type="formule", titre="3 · L'ion hydrogénocarbonate", x=540, y=140, w=700, lignes=[
            dict(f="acide : HCO_3^{−} ⇌ CO_3^{2−} + H^{+}", taille=34),
            dict(f="base : HCO_3^{−} + H^{+} ⇌ (CO_2, H_2O)", taille=34),
            dict(f="les deux caractères : amphotère", cadre=True, taille=34)]),
        "s34": dict(type="formule", titre="4 · L'attaque du calcaire", x=540, y=140, w=700, lignes=[
            dict(f="couples HCO_3^{−}/CO_3^{2−} et " + H3O + "/H_2O", taille=30),
            dict(f="CO_3^{2−} + " + H3O + " → HCO_3^{−} + H_2O", cadre=True, taille=34),
            dict(f="les ions carbonate de la pierre sont consommés", txt=True)]),
        "s35": dict(type="formule", titre="5 · Masse et regard critique", x=540, y=100, w=700, lignes=[
            dict(f="totale, monoacide : c ≈ [" + H3O + "] = 6,3 × 10^-5 mol·L^-1", taille=28),
            dict(f="m = c × M × V = 6,3 × 10^-5 × 63,0 ≈ 4,0 × 10^-3 g", cadre=True, taille=28, n="environ 4 mg par litre"),
            dict(f="part naturelle négligée : " + fr("2,5 × 10^-6", "6,3 × 10^-5") + " ≈ 4 %", taille=28),
            dict(f="u(pH) = 0,1 : [" + H3O + "] entre 5,0 × 10^-5 et 7,9 × 10^-5", taille=28),
            dict(f="un ordre de grandeur : quelques mg par litre", txt=True)]),
    }),

    # ================================================================ XV. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, une seule idée : le transfert d'un ion hydrogène. "
        "{carte.1}Côté définitions : l'acide cède un proton, la base le capte, et une espèce amphotère fait les deux. "
        "{carte.2}Côté couples : A H sur A moins, l'acide en premier, et les quatre familles exigibles. "
        "{carte.3}Côté réaction : l'acide d'un couple donne son proton à la base d'un autre, toujours deux couples. "
        "{carte.4}Côté pH : moins log de la concentration en ions oxonium, plus log F à chaque dilution, et la comparaison au pH théorique pour dire si la réaction est totale.",
        "{-carte}{bac}Et voici ce que le bac peut te demander, à cocher. "
        "{bac.1}Identifier un transfert d'ion hydrogène, les couples, et écrire l'équation d'une réaction acide-base. "
        "{bac.2}Connaître les couples de l'eau, de l'acide carbonique, des acides carboxyliques et des amines. "
        "{bac.3}Représenter le schéma de Lewis d'un acide carboxylique, d'un ion carboxylate, d'une amine et d'un ion ammonium. "
        "{bac.4}Identifier une espèce amphotère. "
        "{bac.5}Passer du pH à la concentration en ions oxonium, et inversement. "
        "{bac.6}Mesurer des pH pour tester la relation, au laboratoire. "
        "{bac.7}Et manier le logarithme décimal et sa réciproque.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre. Pour t'en assurer, entraîne-toi sur d'autres exercices corrigés, jusqu'à les réussir sans aide. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="LE TRANSFERT DE H⁺", branches=[
            dict(t="Les définitions", items=["acide : cède H^{+}", "base : capte H^{+}", "amphotère : deux demi-équations"]),
            dict(t="Les couples", items=["AH/A^{−}, l'acide en premier", "eau · acide carbonique", "acides carboxyliques · amines"]),
            dict(t="La réaction", items=["acide 1 + base 2 → base 1 + acide 2", "toujours deux couples", "additionner, H^{+} simplifiés"]),
            dict(t="Le pH", items=["pH = −log([" + H3O + "]/c°)", "÷ F sur c ⇒ pH + log F", "pH_{mes} > pH_{théo} : limitée"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Identifier un transfert de H^{+}, les couples, écrire l'équation", "Connaître les couples exigibles",
            "Lewis : acide carboxylique, carboxylate, amine, ammonium", "Identifier une espèce amphotère",
            "Passer du pH à [" + H3O + "], et inversement", "Mesurer des pH pour tester la relation",
            "Manier log et 10^{x}"], marques=["✓"] * 7, x=170, y=80, w=940, petit=True),
    }),
]

QUIZ = [
    dict(q="Pourquoi l'hydrogène du groupe —COOH peut-il partir sous forme d'ion H⁺, et pas ceux du groupe CH₃ ?",
         r=["Parce qu'il est porté par un oxygène : la liaison O—H est polarisée", "Parce qu'il est en bout de chaîne", "Parce que le carbone est plus électronégatif que l'oxygène"],
         ok=0, ex="Une liaison avec O, N, F ou Cl est polarisée ; une liaison C—H ne l'est presque pas, son hydrogène ne part jamais.", voir="test"),
    dict(q="Le couple HgO/Hg a pour demi-équation HgO + 2 H⁺ + 2 e⁻ ⇌ Hg + H₂O. C'est…",
         r=["un couple acide-base, puisqu'il y a des H⁺", "un couple oxydant/réducteur, puisqu'il y a des électrons", "ni l'un ni l'autre"],
         ok=1, ex="Le critère de tri est l'électron, jamais le proton : dès qu'un e⁻ est nécessaire, c'est de l'oxydoréduction.", voir="redox"),
    dict(q="La base conjuguée de HSO₃⁻ est…", r=["SO₃⁻", "SO₃²⁻", "H₂SO₃"], ok=1,
         ex="De l'acide à la base, on retire un H et une charge + : la charge passe de −1 à −2.", voir="charges"),
    dict(q="Dans le couple des amines, l'acide est…", r=["l'amine R—NH₂", "l'ion ammonium R—NH₃⁺", "l'ion hydroxyde"], ok=1,
         ex="L'amine capte un proton grâce au doublet non liant de son azote : c'est la base. Son acide conjugué est l'ion ammonium.", voir="piege_am"),
    dict(q="Pour prouver qu'une espèce est amphotère, il faut…",
         r=["écrire une demi-équation où elle cède H⁺", "écrire deux demi-équations : une où elle cède H⁺, une où elle en capte un", "mesurer son pH"],
         ok=1, ex="Une seule demi-équation ne suffit jamais. L'eau, HCO₃⁻ et l'amphion d'un acide aminé sont les cas types.", voir="amph"),
    dict(q="[H₃O⁺] = 3,2 × 10⁻⁶ mol·L⁻¹. Le pH s'écrit…", r=["5,5", "5,49", "5,494"], ok=1,
         ex="Seule la partie décimale du pH est significative : deux chiffres significatifs sur la concentration donnent deux décimales.", voir="cs"),
    dict(q="Pour retrouver [H₃O⁺] à partir du pH, la touche de la calculatrice est…", r=["eˣ", "10ˣ", "ln"], ok=1,
         ex="[H₃O⁺] = c° × 10⁻ᵖᴴ : la réciproque du logarithme décimal est la puissance de dix. Avec eˣ, l'erreur atteint un facteur mille.", voir="calc"),
    dict(q="On dilue dix fois une solution d'acide fort de pH 2,3. Le nouveau pH vaut…", r=["0,23", "3,3", "23"], ok=1,
         ex="Diviser la concentration par F augmente le pH de log F : + 1 pour F = 10.", voir="f_dil2"),
    dict(q="Un diacide qui réagit totalement est apporté à la concentration c. La concentration en ions oxonium vaut…",
         r=["c", "2c", "c/2"], ok=1, ex="Chaque molécule cède deux protons. Oublier le facteur 2 décale le pH de log 2 = 0,30.", voir="f_poly"),
    dict(q="Un acide à 1,0 × 10⁻² mol·L⁻¹ a un pH mesuré de 2,8. Sa réaction avec l'eau est…",
         r=["totale", "limitée", "impossible à déterminer"], ok=1,
         ex="Si elle était totale, le pH vaudrait 2,00. Un pH plus grand signifie moins d'ions oxonium : la réaction est limitée (⇌).", voir="ex_ac"),
]

CREDITS = [
    "Portraits : Søren Sørensen dans son laboratoire, photographie anonyme (domaine public) ; Johannes Brønsted, photographie de Peter Elfelt (domaine public).",
    "Photos : citron entier et coupé, Ivar Leidus, CC BY-SA 4.0 ; pH-mètre Mettler Toledo FiveEasy, OER CampLev, CC BY-SA 4.0.",
    "Images trouvées sur Wikimedia Commons. Animation, schémas et graphique : faits pour la vidéo. Mesures : une série réalisée au laboratoire. "
    "Les trois exercices sont inventés pour la vidéo.",
]
