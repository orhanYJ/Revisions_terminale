"""Physique-chimie, chapitre 3 : « Méthodes chimiques d'analyse » — le cours en vidéo.

Même chaîne que la vidéo du chapitre 4 (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ;
moteur pc/serie/moteur.js (types anim, formule, graphe, exo, pause).
Contenu : le cours du site (pc/index.html, chapitre 3, rappels, fiches 1 à 9, TP 4), rien au-delà ; ce qui dépasse le
programme est dit « hors programme ». Les trois exercices sont inventés pour la vidéo (signalé à l'écran) ; leurs
valeurs ont été recalculées (voir les commentaires).
Les courbes des graphiques sont calculées, pas dessinées au jugé :
  - pH : bilan des charges exact ([H₃O⁺] + [Na⁺] = [Cl⁻ ou A⁻] + [HO⁻], Ke = 1,0 × 10⁻¹⁴), pKA(acide éthanoïque) = 4,76 ;
  - σ : loi de Kohlrausch, λ en mS·m²·mol⁻¹ (H₃O⁺ 35,0 · HO⁻ 19,8 · Na⁺ 5,01 · Cl⁻ 7,63), dilution prise en compte.
Usage : python3 outils/serie-philo/verifier.py pc_ch3 ; puis generer.py pc_ch3 ; chevauchements.py ch3.
"""

SITE = "pc"
CODE = "ch3"
NOTION = "Méthodes chimiques d'analyse"
NUM = 3
TITRE = "Méthodes chimiques d'analyse"
SUIVANT = "Chapitre 4 · La lumière, un flux de photons"
PRONONCIATION = {"Kohlrausch": "Kolraouch", "Latis": "Latisse", "matplotlib": "mat plot lib",
                 "pH-métrique": "pé hache métrique", "pH-mètre": "pé hache mètre", "pH": "pé hache"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]".replace(" ", " ")


# ---------------------------------------------------------------- données des graphiques (calculées)
# Fiche 3 : 20,0 mL d'acide à 1,00 × 10⁻² mol/L titrés par la soude à 2,00 × 10⁻² mol/L ; VE = 10,0 mL
PH_HCL = [(0, 2.0), (1, 2.07), (2, 2.14), (3, 2.22), (4, 2.3), (5, 2.4), (6, 2.51), (7, 2.65), (8, 2.85), (8.5, 2.98),
          (9, 3.16), (9.3, 3.32), (9.6, 3.57), (9.8, 3.87), (9.9, 4.17), (9.95, 4.48), (10, 7.0), (10.05, 9.52),
          (10.1, 9.82), (10.2, 10.12), (10.4, 10.42), (10.7, 10.66), (11, 10.81), (11.5, 10.98), (12, 11.1), (13, 11.26),
          (14, 11.37), (15, 11.46), (16, 11.52), (17, 11.58), (18, 11.62), (19, 11.66), (20, 11.7)]
# même titrage, acide éthanoïque (pKA = 4,76, hors programme) : pH initial 3,39, pH à l'équivalence 8,29
PH_ACOH = [(0, 3.39), (1, 3.87), (2, 4.18), (3, 4.4), (4, 4.59), (5, 4.76), (6, 4.94), (7, 5.13), (8, 5.36), (8.5, 5.51),
           (9, 5.72), (9.3, 5.88), (9.6, 6.14), (9.8, 6.45), (9.9, 6.76), (9.95, 7.06), (10, 8.29), (10.05, 9.52),
           (10.1, 9.82), (10.2, 10.12), (10.4, 10.42), (10.7, 10.66), (11, 10.81), (11.5, 10.98), (12, 11.1), (13, 11.26),
           (14, 11.37), (15, 11.46), (16, 11.52), (17, 11.58), (18, 11.62), (19, 11.66), (20, 11.7)]
# TP 4 : vinaigre dilué 20 fois (c = 5,95 × 10⁻² mol/L), 20,0 mL, soude à 0,10 mol/L ; VE = 11,9 mL
PH_VIN = [(0, 3.0), (0.5, 3.46), (1, 3.74), (2, 4.07), (3, 4.29), (4, 4.47), (5, 4.62), (6, 4.77), (7, 4.92), (8, 5.07),
          (9, 5.25), (10, 5.48), (10.5, 5.64), (11, 5.85), (11.3, 6.04), (11.5, 6.22), (11.7, 6.53), (11.8, 6.83),
          (11.9, 8.67), (12.0, 10.49), (12.1, 10.79), (12.3, 11.09), (12.5, 11.27), (13, 11.52), (13.5, 11.68), (14, 11.79),
          (15, 11.95), (16, 12.06), (18, 12.21), (20, 12.31), (22, 12.38), (25, 12.46)]
# tangentes parallèles : pente 0,146 /mL, au point (5,95 ; 4,76) et au point (14,6 ; 11,90) ;
# droite médiane y = 6,83 + 0,146 V, qui coupe la courbe en E (11,9 mL ; pH 8,4) — maximum de dpH/dV à 11,90 mL
TG = 0.1458
# Fiche 3 noyée dans 200 mL d'eau : σ en mS/m ; droites ajustées σ = 38,62 − 2,786 V et σ = −8,94 + 2,011 V, VE ≈ 9,9 mL
SIG_HCL = [(0, 38.8), (1, 35.9), (2, 33.0), (3, 30.2), (4, 27.4), (5, 24.6), (6, 21.8), (7, 19.1), (8, 16.3), (9, 13.7),
           (10, 11.0), (11, 13.1), (12, 15.2), (13, 17.2), (14, 19.3), (15, 21.3), (16, 23.3), (17, 25.3), (18, 27.3),
           (19, 29.3), (20, 31.2)]
# Exercice 3 : détartrant dilué 100 fois, 10,0 mL + 200 mL d'eau, soude à 2,00 × 10⁻² mol/L ; vraie c = 2,50 mol/L
# (n = 2,50 × 10⁻⁴ mol, VE vrai 12,5 mL) ; points calculés avec la dilution ; droites des moindres carrés :
# σ = 50,51 − 2,940 V (0 à 11 mL) et σ = −11,09 + 2,046 V (14 à 24 mL) ; intersection V = 12,36 mL ≈ 12,4 mL
SIG_EX3 = [(0, 50.8), (2, 44.6), (4, 38.6), (6, 32.7), (8, 26.9), (10, 21.2), (11, 18.4), (14, 17.4), (16, 21.7),
           (18, 25.8), (20, 29.9), (22, 33.9), (24, 37.9)]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_bur}{q1}Sur l'étiquette d'un vinaigre blanc, on lit : « sept pour cent ». "
        "Sept pour cent de quoi ? Et surtout : comment vérifier que c'est vrai ?",
        "{-q1}{q2}Le problème, c'est que les molécules d'acide sont invisibles, et beaucoup trop nombreuses pour être comptées une à une.",
        "{-q2}{q3}L'idée des chimistes est simple et géniale : on ne compte pas les molécules, on les fait réagir. "
        "On ajoute goutte à goutte une solution qu'on connaît parfaitement, jusqu'à l'instant précis où tout l'acide a été consommé. "
        "Le volume versé à cet instant donne la quantité d'acide.",
        ("Faire réagir pour mesurer : c'est le titrage.", {"rate": "-6%"}),
        "{-q3}{-tab_bur}{plan}Dans cette vidéo, on part de zéro. {plan.1}D'abord les outils de départ, vus en seconde et en première. "
        "{plan.2}Puis le titrage et son instant clé : l'équivalence. {plan.3}Ensuite ce que contient le bécher à chaque goutte, et comment lire une étiquette. "
        "{plan.4}Puis les trois façons de repérer l'équivalence : la couleur, le pH, et la conductivité. "
        "{plan.5}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_bur": dict(type="tableau", img="c3-burette", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .4],
                        legende="Titrage à la burette, gravure d'Alessandri, 1895 (domaine public)"),
        "q1": dict(type="question", t="Vinaigre à 7 % : comment le vérifier ?"),
        "q2": dict(type="question", t="Des molécules invisibles, impossibles à compter."),
        "q3": dict(type="question", t="On ne les compte pas : on les fait réagir."),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les outils de départ : quantité de matière, avancement, pH", "Le titrage et l'équivalence",
            "Le contenu du bécher, et lire une étiquette", "Repérer l'équivalence : couleur, pH, conductivité",
            "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 3", t="Méthodes chimiques d'analyse",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. rappels
    dict(id="rappels", chap="Les outils de départ", fond="nuit", humeur="calme",
         retenir="n = m/M et c = n/V. Une réaction s'arrête au premier réactif épuisé : le réactif limitant. pH = −log[H₃O⁺] ; σ = Σ λᵢ[Xᵢ].",
         beats=[
        "{f_n}Avant de titrer, rassemblons nos outils. {f_n.1}La quantité de matière n, en moles, se calcule à partir d'une masse : n égale m sur M, "
        "la masse divisée par la masse molaire. {f_n.2}Ou à partir d'une solution : n égale c fois V, la concentration fois le volume. "
        "Attention, le volume en litres.",
        "{f_n.3}La concentration en masse, notée c m, c'est la masse de soluté par litre de solution. Elle vaut c fois M. "
        "{f_n.4}Ne la confonds pas avec la masse volumique rhô : la masse de toute la solution, eau comprise, par litre.",
        "{-f_n}{av}Deuxième outil, vu en première : le tableau d'avancement. {av.1}Quand la réaction avance de x, "
        "chaque réactif diminue de son coefficient fois x, et chaque produit augmente de la même façon. "
        "{av.2}La réaction s'arrête au premier réactif épuisé : c'est le {!limitant}réactif limitant.",
        "{av.3}Retiens ce réflexe, il va servir tout le chapitre : avant l'équivalence d'un titrage, c'est le réactif versé qui est limitant. Après, c'est le réactif du bécher.",
        "{-av}{outils}Enfin, quelques outils de terminale. {outils.1}Côté acides et bases : les couples acide-base. Un acide cède un ion H plus, une base le capte. "
        "{outils.2}Et le pH, moins le logarithme de la concentration en ions H trois O plus. Une grandeur logarithmique : gardons ce mot en tête. "
        "{outils.3}Côté conductimétrie : la loi de Kohlrausch. La conductivité sigma est la somme des contributions de chaque ion, lambda fois sa concentration. "
        "{outils.4}Et de seconde : la dilution, c mère fois V mère égale c fille fois V fille.",
        "En première, tu as déjà fait un titrage : on versait une solution violette de permanganate, et l'équivalence se repérait quand la couleur persistait. "
        "Ce chapitre garde exactement ce principe, et ajoute deux façons plus précises de repérer l'équivalence.",
        "{-outils}",
    ], vis={
        "f_n": dict(type="formule", titre="Quantité de matière et concentrations", x=150, y=110, w=980, lignes=[
            dict(f="n = " + fr("m", "M"), cadre=True, n="n en mol · m en g · M en g·mol^-1"),
            dict(f="n = c × V", cadre=True, n="c en mol·L^-1 · V en L"),
            dict(f="c_m = " + fr("m_{soluté}", "V") + " = c × M", n="en g·L^-1"),
            dict(f="ρ = " + fr("m_{solution}", "V") + " : toute la solution, eau comprise", txt=True)]),
        "av": dict(type="liste", titre="Le tableau d'avancement, en trois idées", items=[
            "Quand x augmente : réactifs − coefficient × x, produits + coefficient × x",
            "La réaction s'arrête au premier réactif épuisé : le réactif limitant",
            "Titrage : avant l'équivalence, le réactif versé est limitant ; après, celui du bécher"],
                   marques=["1", "2", "3"], x=150, y=160, w=980),
        "outils": dict(type="liste", titre="Les autres outils de départ", items=[
            "Couples acide-base : acide ⇌ base + H⁺", "pH = −log [H₃O⁺] : une grandeur logarithmique",
            "Kohlrausch : σ = Σ λ_i [X_i]", "Dilution : c_{mère} × V_{mère} = c_{fille} × V_{fille} (2nde)"],
                       marques=["1", "2", "3", "4"], x=150, y=150, w=980),
    }),

    # ================================================================ II. titrer
    dict(id="titrer", chap="Titrer : faire réagir pour mesurer", fond="nuit", humeur="lumiere",
         retenir="Titré dans le bécher (volume connu, pipette jaugée) ; titrant de concentration connue dans la burette. Réaction support totale, rapide, unique.",
         beats=[
        "{montage}Voici le montage d'un titrage. {montage.1}Dans le bécher, l'espèce dont on cherche la quantité : le {!titré}réactif titré. "
        "On en prélève un volume connu, avec une pipette jaugée. "
        "{montage.2}Dans la burette, le réactif titrant : une solution dont on connaît la concentration, et qu'on verse progressivement. "
        "La burette délivre le volume au dixième de millilitre près.",
        "{montage.3}Un agitateur magnétique homogénéise après chaque ajout. {montage.4}Et une sonde suit une grandeur : le pH, ou la conductivité.",
        "{-montage}{exig}La réaction entre le titré et le titrant s'appelle la réaction support. Elle doit remplir trois conditions. "
        "{exig.1}Elle doit être totale : chaque goutte versée doit réagir entièrement, sinon la quantité versée ne dirait plus la quantité consommée. "
        "{exig.2}Rapide : finie le temps d'agiter, sinon on lirait une mesure encore en train d'évoluer. "
        "{exig.3}Et unique : si le titrant réagissait aussi avec autre chose, une partie de ce qu'on verse serait perdue, et le résultat serait faux.",
        "{-exig}{destr}Un titrage est une méthode destructive : l'espèce dosée est consommée, on ne la récupère pas. "
        "C'est le prix à payer pour une méthode très précise, qui ne demande ni droite d'étalonnage, ni appareil coûteux.",
        "{-destr}{dos}Un mot de vocabulaire, souvent demandé. {dos.1}Un dosage, c'est toute méthode qui détermine une quantité. Un dosage par étalonnage en est un. "
        "{dos.2}Un titrage est un dosage particulier, fondé sur une réaction chimique. Tout titrage est un dosage, mais l'inverse est faux.",
        "{-dos}",
    ], vis={
        "montage": dict(type="liste", titre="Le montage d'un titrage", items=[
            "Bécher : le réactif titré, volume V_A prélevé à la pipette jaugée",
            "Burette : le réactif titrant, concentration c_B connue, au 0,1 mL près",
            "Agitateur magnétique : homogénéiser après chaque ajout",
            "Sonde : pH-mètre ou conductimètre"], marques=["A", "B", "↻", "⌁"], x=150, y=150, w=980),
        "exig": dict(type="liste", titre="La réaction support doit être…", items=[
            "Totale : chaque goutte versée réagit entièrement", "Rapide : finie le temps d'agiter",
            "Unique : le titrant ne réagit avec rien d'autre"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "destr": dict(type="note", titre="Une méthode destructive", cles=["destructive", "précise"],
                      t="L'espèce titrée est consommée. En échange : une méthode très précise, sans droite d'étalonnage.", x=170, y=210, w=940),
        "dos": dict(type="cols", g="Dosage", gq="toute méthode qui détermine une quantité · ex. le dosage par étalonnage",
                    d="Titrage", dq="un dosage fondé sur une réaction chimique", vs="⊃",
                    repere="Tout titrage est un dosage ; l'inverse est faux"),
    }),

    # ================================================================ III. l'équivalence
    # fiche 3 : nA = 1,00e-2 × 20,0e-3 = 2,00e-4 mol ; VE = 2,00e-4 / 2,00e-2 = 1,00e-2 L = 10,0 mL
    dict(id="equivalence", chap="L'équivalence et sa relation", fond="aube", humeur="tension",
         retenir="À l'équivalence, les réactifs ont été introduits dans les proportions stœchiométriques : n_A/a = n_B,E/b. Mole à mole : c_A × V_A = c_B × V_E.",
         beats=[
        "{def_eq}Tout le chapitre repose sur un seul instant. {def_eq.1}L'{!équivalence}équivalence, c'est l'état du système pour lequel les réactifs ont été introduits "
        "dans les proportions stœchiométriques de la réaction support. À cet instant, le titré et le titrant sont épuisés en même temps.",
        "{-def_eq}{f_eq}{f_eq.1}Pour une réaction a A plus b B donne des produits, cette définition se traduit en une relation : "
        "n A initiale sur a, égale n B à l'équivalence sur b. "
        "{f_eq.2}Pourquoi ? Parce qu'à l'équivalence, les deux réactifs sont limitants en même temps. "
        "L'avancement maximal annule les deux lignes du tableau : n A moins a x max égale zéro, et n B E moins b x max égale zéro.",
        "{f_eq.3}En éliminant x max, on retrouve exactement la relation. La formule n'est rien d'autre que le tableau d'avancement, lu au bon moment.",
        "{-f_eq}{f_cc}{f_cc.1}Le titrant est connu : la quantité versée à l'équivalence vaut c B fois V E, où V E est le {!volume équivalent}volume équivalent. "
        "{f_cc.2}Pour une réaction mole à mole, a et b valent un, et on obtient la formule qu'on utilise sans cesse : c A fois V A égale c B fois V E. "
        "{f_cc.3}D'où c A égale c B fois V E sur V A.",
        "{-f_cc}{coef}Mais attention aux coefficients. {coef.1}Acide chlorhydrique et soude : un ion H trois O plus pour un ion H O moins. Un pour un, aucun piège. "
        "{coef.2}Acide éthanoïque et soude : un pour un aussi. "
        "{coef.3}Acide sulfurique, un diacide : il faut deux ions H O moins par molécule. La quantité d'acide vaut la moitié de celle de la soude versée. "
        "{coef.4}Et pour un triacide, le tiers.",
        "C'est la source de la plupart des résultats faux d'un facteur deux. D'où le réflexe : écris toujours la réaction support avant la relation à l'équivalence.",
        "{-coef}{piege_v}Autre piège, le plus fréquent du chapitre. V E, c'est le volume de titrant versé à l'équivalence, lu sur la burette ou sur la courbe. "
        "V A, c'est le volume de titré prélevé à la pipette. Ne les confonds jamais, et relis V E sur la courbe au moment de l'écrire dans la formule.",
        "{-piege_v}{ex_eq}{ex_eq.1}Un exemple, qui nous servira tout le chapitre. On titre vingt millilitres d'acide chlorhydrique de concentration un fois dix puissance moins deux mole par litre, "
        "par de la soude à deux fois dix puissance moins deux mole par litre. {ex_eq.2}Il y a au départ c A fois V A, "
        "soit deux fois dix puissance moins quatre mole d'ions H trois O plus. Deux cents micromoles. "
        "{ex_eq.3}Réaction mole à mole : il faut verser autant d'ions H O moins. {ex_eq.4}V E égale deux fois dix puissance moins quatre, sur deux fois dix puissance moins deux : "
        "dix millilitres.",
        "{-ex_eq}",
    ], vis={
        "def_eq": dict(type="def", terme="L'équivalence", cles=["stœchiométriques", "épuisés"],
                       t="État du système pour lequel les réactifs ont été introduits dans les proportions stœchiométriques de la réaction support.",
                       etape="Le titré et le titrant sont épuisés en même temps.", x=170, y=170, w=940),
        "f_eq": dict(type="formule", titre="Relation à l'équivalence", x=150, y=110, w=980, lignes=[
            dict(f=fr("n_{A,initial}", "a") + " = " + fr("n_{B,E}", "b"), cadre=True, taille=54, n="réaction a A + b B → produits · n_{B,E} : titrant versé à l'équivalence"),
            dict(f="n_A − a x_{max} = 0   et   n_{B,E} − b x_{max} = 0", taille=38),
            dict(f="les deux réactifs sont limitants en même temps", txt=True, pt=True)]),
        "f_cc": dict(type="formule", titre="Réaction mole à mole", x=150, y=130, w=980, lignes=[
            dict(f="n_{B,E} = c_B × V_E", n="V_E : volume de titrant versé à l'équivalence"),
            dict(f="c_A × V_A = c_B × V_E", cadre=True, taille=54),
            dict(f="c_A = " + fr("c_B × V_E", "V_A"), cadre=True, n="mêmes unités de volume des deux côtés")]),
        "coef": dict(type="liste", titre="Lire les coefficients", items=[
            "H₃O⁺ + HO⁻ → 2 H₂O : n(H₃O⁺) = n(HO⁻)_E",
            "CH₃COOH + HO⁻ → CH₃COO⁻ + H₂O : un pour un",
            "H₂SO₄ + 2 HO⁻ → SO₄²⁻ + 2 H₂O : n(H₂SO₄) = n(HO⁻)_E / 2",
            "H₃A + 3 HO⁻ → A³⁻ + 3 H₂O : n(H₃A) = n(HO⁻)_E / 3"], marques=["1", "1", "÷2", "÷3"], x=150, y=150, w=980),
        "piege_v": dict(type="note", titre="V_E n'est pas V_A", cles=["burette", "pipette"],
                        t="V_E : titrant versé, lu sur la burette ou la courbe. V_A : titré prélevé à la pipette.", x=170, y=210, w=940),
        "ex_eq": dict(type="formule", titre="Exemple · un acide chlorhydrique titré par la soude", x=150, y=130, w=980, lignes=[
            dict(f="V_A = 20,0 mL · c_A = 1,00 × 10^-2 mol·L^-1 · c_B = 2,00 × 10^-2 mol·L^-1", txt=True, taille=30),
            dict(f="n(H₃O⁺)_i = c_A × V_A = 1,00 × 10^-2 × 20,0 × 10^-3 = 2,00 × 10^-4 mol", taille=34),
            dict(f="mole à mole : n(HO⁻)_E = 2,00 × 10^-4 mol", taille=34),
            dict(f="V_E = " + fr("2,00 × 10^-4", "2,00 × 10^-2") + " = 1,00 × 10^-2 L = 10,0 mL", cadre=True, taille=38)]),
    }),

    # ================================================================ IV. composition du système (animation titrage)
    dict(id="compo", chap="Que contient le bécher ?", fond="cosmos", humeur="calme",
         retenir="Avant l'équivalence : le titrant versé est limitant. Après : le titré est limitant. Les ions spectateurs restent dans le bécher et comptent dans σ.",
         beats=[
        "{an_ti}{ti_pts}{ti_pts.1}{an_ti.1}Regardons ce titrage se faire. Dans le bécher, les ions H trois O plus, en orange, et les ions chlorure, en vert. "
        "Chaque icône vaut dix micromoles. Dans la burette, la soude : des ions sodium et des ions hydroxyde.",
        "{ti_pts.2}{an_ti.2}Chaque goutte apporte des ions H O moins, qui réagissent aussitôt avec les ions H trois O plus. "
        "La soude versée est le réactif limitant. Les ions H trois O plus disparaissent, et des ions sodium, spectateurs, prennent leur place. "
        "Le pH monte lentement. La conductivité baisse.",
        "{ti_pts.3}{an_ti.3}À dix millilitres, l'équivalence : plus d'ions H trois O plus, et pas encore d'ions H O moins en excès. "
        "Le pH fait un saut ; la conductivité passe par son minimum.",
        "{ti_pts.4}{an_ti.4}Après l'équivalence, il n'y a plus rien pour réagir : les ions H O moins versés s'accumulent, avec les ions sodium. "
        "C'est maintenant l'acide du bécher qui est limitant. Le pH se stabilise vers douze, et la conductivité remonte.",
        "{-an_ti}{-ti_pts}{compo_t}Faisons le bilan, en micromoles. {compo_t.1}Au départ : deux cents d'ions H trois O plus, deux cents d'ions chlorure. "
        "{compo_t.2}À cinq millilitres, avant l'équivalence : on a versé cent micromoles de soude. Il reste cent d'ions H trois O plus, et il y a cent d'ions sodium. "
        "{compo_t.3}À dix millilitres, l'équivalence : plus d'acide, plus de base, deux cents d'ions sodium. "
        "{compo_t.4}À quinze millilitres, après : cent d'ions H O moins en excès, trois cents d'ions sodium. Et les chlorures ? Toujours deux cents, du début à la fin.",
        "{-compo_t}{spect}Ce sont les deux ions qu'on oublie : les ions spectateurs. Ils ne réagissent pas, mais ils restent dans le bécher. "
        "Le chlorure ne bouge pas, le sodium augmente à chaque ajout. Ils ne changent rien au pH, mais ils comptent dans la conductivité.",
        "{-spect}{meth3}D'où la méthode en trois questions, pour n'importe quel volume versé. "
        "{meth3.1}Un : quelle quantité de titrant a-t-on versée ? n B égale c B fois V B. "
        "{meth3.2}Deux : qui est limitant ? Avant l'équivalence, le titrant ; après, le titré. "
        "{meth3.3}Trois : que reste-t-il ? Le réactif en excès diminue de la quantité consommée ; les produits et les spectateurs s'ajoutent.",
        "{meth3.4}Et si on te demande une concentration, divise par le volume total du bécher à cet instant, V A plus V B, pas par le volume initial.",
        "{-meth3}{prog}Le programme demande aussi de représenter ces quantités avec un langage de programmation, comme Python. "
        "Le code ne fait que traduire la méthode. {prog.1}On calcule la quantité d'acide initiale, puis V E. "
        "{prog.2}Pour chaque volume versé, on calcule la quantité de soude. {prog.3}Et tout repose sur un test : si V B est inférieur à V E, "
        "la soude est limitante, et il reste n A moins n B d'acide. {prog.4}Sinon, l'acide est épuisé, et il y a n B moins n A d'ions hydroxyde. "
        "{prog.5}Les spectateurs, eux, valent n B pour le sodium et n A pour le chlorure.",
        "Ce test, si V B est inférieur à V E, c'est l'équivalence écrite en langage informatique. Deux lignes de plus avec la bibliothèque matplotlib, et on obtient le graphique.",
        "{-prog}",
    ], vis={
        "an_ti": dict(type="anim", nom="titrage", x=40, y=72, h=624, seg=[[1.2, 9.5], [9.5, 24], [24, 34], [34, 46]]),
        "ti_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Bécher : H₃O⁺ et Cl⁻ · burette : Na⁺ et HO⁻ (1 icône = 10 µmol)",
            "Avant V_E : chaque HO⁻ versé réagit ; H₃O⁺ remplacé par Na⁺",
            "À V_E = 10,0 mL : ni H₃O⁺, ni HO⁻ en excès ; saut de pH",
            "Après V_E : HO⁻ et Na⁺ s'accumulent ; σ remonte"]),
        "compo_t": dict(type="formule", titre="Le bécher, en micromoles (V_E = 10,0 mL)", x=130, y=120, w=1020, lignes=[
            dict(f="V_B = 0 : H₃O⁺ 200 · HO⁻ 0 · Na⁺ 0 · Cl⁻ 200", taille=34),
            dict(f="V_B = 5,0 mL : H₃O⁺ 100 · HO⁻ ≈ 0 · Na⁺ 100 · Cl⁻ 200", taille=34, n="avant : la soude versée est limitante"),
            dict(f="V_B = 10,0 mL : H₃O⁺ ≈ 0 · HO⁻ ≈ 0 · Na⁺ 200 · Cl⁻ 200", taille=34, cadre=True, n="équivalence : les deux à la fois"),
            dict(f="V_B = 15,0 mL : H₃O⁺ ≈ 0 · HO⁻ 100 · Na⁺ 300 · Cl⁻ 200", taille=34, n="après : l'acide du bécher est limitant")]),
        "spect": dict(type="note", titre="Les ions spectateurs", cles=["spectateurs", "conductivité"],
                      t="Na⁺ et Cl⁻ ne réagissent pas mais restent dans le bécher : rien sur le pH, mais ils comptent dans la conductivité.",
                      x=170, y=210, w=940),
        "meth3": dict(type="liste", titre="La méthode en trois questions", items=[
            "Quelle quantité de titrant versée ? n_B = c_B × V_B",
            "Qui est limitant ? Avant V_E le titrant, après le titré",
            "Que reste-t-il ? L'excès diminue ; produits et spectateurs s'ajoutent",
            "Une concentration ? Diviser par le volume total V_A + V_B"], marques=["1", "2", "3", "!"], x=150, y=150, w=980),
        "prog": dict(type="formule", titre="Programmer l'évolution des quantités (Python)", x=150, y=100, w=980, lignes=[
            dict(f="nA0 = cA × VA   ·   VE = nA0 / cB", txt=True, taille=30),
            dict(f="pour chaque VB : nB = cB × VB", txt=True, taille=30),
            dict(f="si VB < VE : n(H₃O⁺) = nA0 − nB ; n(HO⁻) = 0", txt=True, taille=30, n="avant : la soude est limitante"),
            dict(f="sinon : n(H₃O⁺) = 0 ; n(HO⁻) = nB − nA0", txt=True, taille=30, n="après : l'acide est limitant"),
            dict(f="n(Na⁺) = nB   ·   n(Cl⁻) = nA0", txt=True, taille=30, n="les spectateurs")]),
    }),

    # ================================================================ V. titre massique et densité
    # vinaigre TP 4 : cm = 0,07 × 1,01 × 1,00e3 = 70,7 g/L ; c = 70,7 / 60,1 = 1,176 ≈ 1,18 mol/L
    dict(id="etiquette", chap="De l'étiquette à la concentration", fond="nuit", humeur="lumiere",
         retenir="t = m_soluté / m_solution et d = ρ / ρ_eau. c_m = t × d × ρ_eau, c = t × d × ρ_eau / M. Un pourcentage massique se rapporte à une masse, pas à 100 mL.",
         beats=[
        "{q_et}Revenons au vinaigre. Les produits commerciaux n'affichent presque jamais une concentration en moles par litre. "
        "Ils donnent deux nombres : un titre massique et une densité. Savoir les convertir, c'est la première question de presque tous les exercices du chapitre.",
        "{-q_et}{def_t}{def_t.1}Le titre massique t, ou pourcentage massique, c'est la fraction de la masse de solution due au soluté : m soluté sur m solution. "
        "Un vinaigre à sept pour cent contient sept grammes d'acide éthanoïque dans cent grammes de vinaigre. Pas dans cent millilitres !",
        "{-def_t}{def_d}{def_d.1}La densité d d'un liquide compare sa masse volumique à celle de l'eau : d égale rhô sur rhô eau. Elle n'a pas d'unité.",
        "{-def_d}{conv}Pas besoin d'apprendre la conversion par cœur : il suffit de suivre un litre de solution. "
        "{conv.1}Un litre de solution pèse d fois rhô eau fois un litre : c'est la définition de la densité. "
        "{conv.2}La part de soluté dans cette masse vaut t fois d fois rhô eau : c'est la définition du titre massique. "
        "{conv.3}On convertit en quantité de matière en divisant par la masse molaire.",
        "{-conv}{f_t}{f_t.1}D'où les deux formules : c m égale t fois d fois rhô eau, en grammes par litre. "
        "{f_t.2}Et c égale t fois d fois rhô eau, divisé par M, en moles par litre. "
        "{f_t.3}Attention : t s'écrit sans unité, sept pour cent donne zéro virgule zéro sept. Et rhô eau vaut mille grammes par litre.",
        "{-f_t}{ex_vin}Appliquons à notre vinaigre. {ex_vin.1}t vaut zéro virgule zéro sept, d vaut un virgule zéro un, et la masse molaire de l'acide éthanoïque vaut soixante virgule un grammes par mole. "
        "{ex_vin.2}c m égale zéro virgule zéro sept, fois un virgule zéro un, fois mille : soixante-dix virgule sept grammes par litre. "
        "{ex_vin.3}Et c égale soixante-dix virgule sept sur soixante virgule un : un virgule dix-huit mole par litre. "
        "Voilà ce que promet l'étiquette. Reste à le vérifier.",
        "{-ex_vin}{piege_100}Le piège classique : écrire sept grammes dans cent millilitres. Cela revient à supposer que la densité vaut un. "
        "Ici l'écart est petit : soixante-dix au lieu de soixante-dix virgule sept. Mais pour un acide chlorhydrique concentré de densité un virgule dix-huit, l'erreur atteint dix-huit pour cent.",
        "{-piege_100}{dil}Pour préparer une solution plus diluée à partir du produit commercial, c'est une simple dilution. "
        "On calcule le volume à prélever : V mère égale c fille fois V fille sur c mère. On le prélève à la pipette jaugée, et on complète dans une fiole jaugée.",
        "{-dil}",
    ], vis={
        "q_et": dict(type="question", t="Titre massique et densité : de l'étiquette aux moles par litre"),
        "def_t": dict(type="def", terme="Titre massique t", cles=["masse", "grammes"],
                      t="Fraction de la masse de solution due au soluté : t = m_{soluté} / m_{solution}.",
                      etape="7 % : 7 g d'acide dans 100 g de vinaigre, pas dans 100 mL.", x=170, y=180, w=940),
        "def_d": dict(type="def", terme="Densité d", cles=["masse", "unité"],
                      t="Compare la masse volumique d'un liquide à celle de l'eau : d = ρ / ρ_{eau}. Sans unité.", x=170, y=210, w=940),
        "conv": dict(type="liste", titre="Suivre un litre de solution", items=[
            "Il pèse m_{solution} = d × ρ_{eau} × 1 L (définition de d)",
            "Le soluté pèse m_{soluté} = t × d × ρ_{eau} (définition de t)",
            "En moles : diviser par la masse molaire M"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "f_t": dict(type="formule", titre="De l'étiquette à la concentration", x=150, y=130, w=980, lignes=[
            dict(f="c_m = t × d × ρ_{eau}", cadre=True, n="en g·L^-1"),
            dict(f="c = " + fr("t × d × ρ_{eau}", "M"), cadre=True, n="en mol·L^-1 · M en g·mol^-1"),
            dict(f="t sans unité (7 % = 0,07) · ρ_{eau} = 1,00 × 10^3 g·L^-1", txt=True)]),
        "ex_vin": dict(type="formule", titre="Le vinaigre « à 7 % »", x=150, y=140, w=980, lignes=[
            dict(f="t = 0,07 · d = 1,01 · M = 60,1 g·mol^-1", taille=36),
            dict(f="c_m = 0,07 × 1,01 × 1,00 × 10^3 = 70,7 g·L^-1", taille=38),
            dict(f="c = " + fr("70,7", "60,1") + " = 1,18 mol·L^-1", cadre=True, taille=40)]),
        "piege_100": dict(type="note", titre="Le piège des 100 mL", cles=["densité", "dix-huit"],
                          t="« 7 g dans 100 mL » suppose d = 1 : 70 au lieu de 70,7 g/L ici, mais 18 % d'erreur pour un acide de densité 1,18.",
                          x=170, y=210, w=940),
        "dil": dict(type="formule", titre="Préparer la solution à titrer", x=150, y=190, w=980, lignes=[
            dict(f="V_{mère} = " + fr("c_{fille} × V_{fille}", "c_{mère}"), cadre=True, n="pipette jaugée, puis fiole jaugée")]),
    }),

    # ================================================================ VI. suivi pH-métrique
    dict(id="phmetrie", chap="Le suivi pH-métrique", fond="nuit", humeur="tension",
         retenir="pH = f(V_B) : montée lente, saut, palier. V_E au milieu du saut : tangentes parallèles ou maximum de dpH/dV. pH_E = 7 seulement pour fort/fort.",
         beats=[
        "{tab_ph}Première façon de repérer l'équivalence, la plus utilisée : le suivi pH-métrique. "
        "On mesure le pH après chaque ajout, et on trace pH en fonction du volume versé.",
        "{-tab_ph}{gr_ph}{gr_ph.1}Voici la courbe de notre acide chlorhydrique. Elle monte lentement, de deux à moins de quatre, pendant presque dix millilitres. "
        "{gr_ph.2}Puis, autour de dix millilitres, un saut brutal de plusieurs unités. Puis elle se stabilise vers douze. L'équivalence est au milieu du saut.",
        "Pourquoi un saut, et pas une montée régulière ? Parce que le pH est un logarithme. "
        "Avant l'équivalence, il reste beaucoup d'acide : retirer quelques micromoles ne change la concentration que d'un petit facteur. Le pH bouge peu.",
        "Tout près de l'équivalence, il ne reste presque plus rien. Une seule goutte divise la quantité d'acide par dix, puis par cent, puis fait apparaître un excès d'ions H O moins. "
        "La concentration change de plusieurs ordres de grandeur en un dixième de millilitre. Et chaque ordre de grandeur, c'est une unité de pH.",
        "{gr_ph.3}Comparons avec l'acide éthanoïque, à la même concentration. La courbe part plus haut, le saut est plus court, "
        "{gr_ph.4}et le point d'équivalence est plus haut : vers huit, et non sept. Le volume équivalent, lui, est le même : dix millilitres.",
        "{-gr_ph}{phE}Le pH à l'équivalence n'est donc pas toujours sept. {phE.1}Acide fort par base forte : à l'équivalence, le bécher ne contient que de l'eau, "
        "des ions sodium et des ions chlorure. Le pH vaut sept. "
        "{phE.2}Acide éthanoïque par la soude : le bécher contient aussi des ions éthanoate, la base conjuguée formée par la réaction. Ils rendent la solution légèrement basique : pH supérieur à sept. "
        "{phE.3}Et si on titre une base faible, comme l'ammoniaque, par un acide, le pH à l'équivalence est inférieur à sept. Ce sont les couples acide-base qui l'expliquent.",
        "{-phE}{an_tg}{tg_pts}{tg_pts.1}{an_tg.1}Comment lire V E précisément ? Première méthode : les tangentes parallèles. "
        "On trace deux tangentes à la courbe, parallèles entre elles, de part et d'autre du saut. "
        "{tg_pts.2}Puis la droite parallèle et à égale distance des deux. Elle coupe la courbe au point d'équivalence. Son abscisse, c'est V E.",
        "{-an_tg}{-tg_pts}{gr_tg}Faisons-le sur le titrage d'un vinaigre dilué vingt fois. {gr_tg.1}Voici sa courbe. "
        "{gr_tg.2}Une première tangente, avant le saut. {gr_tg.3}Une seconde, parallèle, après le saut. "
        "{gr_tg.4}La droite à égale distance. {gr_tg.5}Elle coupe la courbe en E : V E vaut onze virgule neuf millilitres, et le pH à l'équivalence vaut environ huit virgule quatre.",
        "{-gr_tg}{deriv}{deriv.1}Deuxième méthode : la dérivée. On fait tracer par le logiciel d pH sur d V. Elle présente un pic très net, et V E est l'abscisse de son maximum. "
        "C'est logique : l'équivalence est l'endroit où le pH varie le plus vite. "
        "{deriv.2}Sur ce vinaigre, les deux méthodes ont donné onze virgule quatre-vingt-sept et onze virgule quatre-vingt-dix-huit millilitres : un accord à zéro virgule un millilitre près.",
        "{deriv.3}Quand le logiciel fournit la dérivée, on la privilégie : la courbe du vinaigre n'est pas symétrique autour de l'équivalence, et la méthode des tangentes suppose une certaine symétrie.",
        "{-deriv}{sens}Dernier réflexe : avant de lire V E, regarde le sens du saut. Si on titre une base par un acide, la courbe descend. "
        "Les méthodes restent les mêmes, mais la dérivée présente un creux au lieu d'un pic.",
        "{-sens}",
    ], vis={
        "tab_ph": dict(type="tableau", img="c3-phmetre", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                       legende="pH-mètre de laboratoire, photo OER＿CampLev, CC BY-SA 4.0"),
        "gr_ph": dict(type="graphe", titre="Deux acides à 1,0 × 10^-2 mol/L titrés par la soude", x=330, y=110, w=640, h=520,
                      ax=dict(x=[0, 20], y=[0, 14], gx=[5, 10, 15, 20], gy=[2, 4, 6, 8, 10, 12, 14], lx="V_B (mL)", ly="pH"),
                      el=[dict(type="courbe", pts=[list(p) for p in PH_HCL if p[0] <= 9.9], c="el", dur=2.4, lbl="acide chlorhydrique", lp=[2.5, 1.1]),
                          dict(type="courbe", pts=[list(p) for p in PH_HCL if p[0] >= 9.9], c="el", dur=1.4),
                          dict(type="courbe", pts=[list(p) for p in PH_ACOH], c="vert", dur=2.4, lbl="acide éthanoïque", lp=[1.0, 7.0]),
                          dict(type="point", x=10, y=8.29, c="vert", proj=True, lbl="pH_E ≈ 8,3", lp=[11.0, 8.0])]),
        "phE": dict(type="liste", titre="Le pH à l'équivalence", items=[
            "Acide fort par base forte : eau, Na⁺, Cl⁻ → pH_E = 7",
            "Acide éthanoïque par la soude : CH₃COO⁻, une base → pH_E > 7",
            "Base faible (ammoniaque) par un acide : NH₄⁺, un acide → pH_E < 7"], marques=["=7", ">7", "<7"], x=150, y=170, w=980),
        "an_tg": dict(type="anim", nom="titrage", x=40, y=72, h=624, seg=[[46, 56]]),
        "tg_pts": dict(type="liste", petit=True, titre="La méthode des tangentes", x=680, y=170, w=560, items=[
            "Deux tangentes parallèles, de part et d'autre du saut",
            "La parallèle à égale distance coupe la courbe en E : son abscisse est V_E"]),
        "gr_tg": dict(type="graphe", titre="Vinaigre dilué 20 fois, soude à 0,10 mol/L", x=330, y=110, w=640, h=520,
                      ax=dict(x=[0, 25], y=[0, 14], gx=[5, 10, 15, 20, 25], gy=[2, 4, 6, 8, 10, 12, 14], lx="V_B (mL)", ly="pH"),
                      el=[dict(type="courbe", pts=[list(p) for p in PH_VIN], c="el", dur=2.4),
                          dict(type="droite", pts=[[0.5, 3.893 + TG * 0.5], [13.5, 3.893 + TG * 13.5]], c="iv", ep=2.4),
                          dict(type="droite", pts=[[9.5, 9.764 + TG * 9.5], [23, 9.764 + TG * 23]], c="iv", ep=2.4),
                          dict(type="droite", pts=[[7, 6.829 + TG * 7], [17, 6.829 + TG * 17]], c="vert", tir=True, ep=2.4),
                          dict(type="point", x=11.9, y=8.39, c="vert", proj=True, lbl="E : V_E = 11,9 mL", lp=[13.4, 6.4])]),
        "deriv": dict(type="liste", titre="La méthode de la dérivée", items=[
            "Le logiciel trace dpH/dV : V_E est l'abscisse de son maximum",
            "Vinaigre : tangentes 11,87 mL · dérivée 11,98 mL → V_E ≈ 11,9 mL",
            "Courbe non symétrique : on privilégie la dérivée"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "sens": dict(type="note", titre="Regarder le sens du saut", cles=["descend", "creux"],
                     t="Base titrée par un acide : la courbe descend, la dérivée présente un creux. Les méthodes ne changent pas.", x=170, y=220, w=940),
    }),

    # ================================================================ VII. indicateurs colorés
    dict(id="indicateurs", chap="Repérer l'équivalence par une couleur", fond="aube", humeur="lumiere",
         retenir="Un indicateur est adapté si pH_E appartient à sa zone de virage. Hélianthine 3,1–4,4 · BBT 6,0–7,6 · phénolphtaléine 8,2–10,0. Méthode la moins précise.",
         beats=[
        "{def_ind}{def_ind.1}Deuxième façon, la plus ancienne : un indicateur coloré. C'est un couple acide-base dont l'acide et la base n'ont pas la même couleur. "
        "Sa teinte change sur un petit intervalle de pH : sa {!zone de virage}zone de virage.",
        "{-def_ind}{crit}Le critère de choix est à savoir par cœur : un indicateur est adapté si le pH à l'équivalence appartient à sa zone de virage. "
        "Comme le pH saute de plusieurs unités en une goutte, toute zone comprise dans le saut convient : on a une certaine marge.",
        "{-crit}{ind}Trois indicateurs à connaître. {ind.1}L'hélianthine vire entre trois virgule un et quatre virgule quatre, du rouge au jaune : adaptée si l'équivalence est acide. "
        "{ind.2}Le bleu de bromothymol, entre six et sept virgule six, du jaune au bleu : parfait pour un acide fort titré par une base forte, pH sept. "
        "{ind.3}La phénolphtaléine, entre huit virgule deux et dix, d'incolore à rose : pour un acide faible titré par une base forte, pH supérieur à sept.",
        "{-ind}{gr_ind}Vérifions-le sur nos courbes. {gr_ind.1}La bande bleue, c'est la zone du bleu de bromothymol. {gr_ind.2}La bande rose, celle de la phénolphtaléine. "
        "{gr_ind.3}Pour l'acide chlorhydrique, le saut traverse les deux bandes : les deux conviennent. "
        "{gr_ind.4}Pour l'acide éthanoïque, le pH à l'équivalence, huit virgule trois, est dans la bande rose : c'est la phénolphtaléine qu'il faut. "
        "Le bleu de bromothymol virerait trop tôt, vers neuf virgule cinq millilitres.",
        "{-gr_ind}{tab_chou}Pour le vinaigre, on peut aussi utiliser un indicateur naturel : le jus de chou rouge. Il a plusieurs zones de virage : "
        "rouge, rose, violet, bleu, vert, puis jaune, du plus acide au plus basique. Pendant le titrage du vinaigre, il est passé du violet au bleu, "
        "puis a basculé vers le vert au moment du saut, vers douze millilitres.",
        "{-tab_chou}{lim}La limite de cette méthode : on repère un changement de couleur jugé à l'œil, pas l'équivalence elle-même. "
        "La précision dépend de l'observateur et de la vitesse à laquelle on verse. C'est la méthode la moins précise des trois. "
        "Elle reste très utile pour un premier titrage rapide, qui dit où ralentir.",
        "{-lim}",
    ], vis={
        "def_ind": dict(type="def", terme="Indicateur coloré acido-basique", cles=["couleur", "virage"],
                        t="Couple acide-base dont l'acide et la base n'ont pas la même couleur.",
                        etape="Sa teinte change sur un petit intervalle de pH : sa zone de virage.", x=170, y=190, w=940),
        "crit": dict(type="note", titre="Le critère de choix", cles=["appartient", "saut"],
                     t="Un indicateur est adapté si pH_E appartient à sa zone de virage. Toute zone comprise dans le saut convient.", x=170, y=210, w=940),
        "ind": dict(type="liste", titre="Trois indicateurs", items=[
            "Hélianthine : 3,1 – 4,4 · rouge → jaune · équivalence acide",
            "Bleu de bromothymol : 6,0 – 7,6 · jaune → bleu · fort/fort, pH_E = 7",
            "Phénolphtaléine : 8,2 – 10,0 · incolore → rose · acide faible, pH_E > 7"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "gr_ind": dict(type="graphe", titre="Zones de virage et sauts", x=330, y=110, w=640, h=520,
                       ax=dict(x=[0, 20], y=[0, 14], gx=[5, 10, 15, 20], gy=[2, 4, 6, 8, 10, 12, 14], lx="V_B (mL)", ly="pH"),
                       el=[dict(type="droite", pts=[[0, 6.8], [20, 6.8]], c="rgba(79,140,255,.30)", ep=46, lbl="BBT 6,0 – 7,6", lp=[14.3, 7.5]),
                           dict(type="droite", pts=[[0, 9.1], [20, 9.1]], c="rgba(255,111,177,.30)", ep=52, lbl="phénolphtaléine 8,2 – 10,0", lp=[10.8, 10.5]),
                           dict(type="courbe", pts=[list(p) for p in PH_HCL], c="el", dur=2.0),
                           dict(type="courbe", pts=[list(p) for p in PH_ACOH], c="vert", dur=2.0, lbl="acide éthanoïque", lp=[1.0, 6.2])]),
        "tab_chou": dict(type="tableau", img="c3-chou", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .5],
                         legende="Jus de chou rouge en milieu acide, neutre et basique, photo brittgow, CC BY 2.0"),
        "lim": dict(type="note", titre="La limite du colorimétrique", cles=["œil", "moins"],
                    t="On juge une couleur à l'œil, pas l'équivalence elle-même : la méthode la moins précise. Utile pour un titrage rapide.", x=170, y=220, w=940),
    }),

    # ================================================================ VIII. suivi conductimétrique
    dict(id="conducto", chap="Le suivi conductimétrique", fond="cosmos", humeur="mystere",
         retenir="σ = f(V) : deux segments de droite, V_E à leur intersection. Justifier une pente : quel ion disparaît, quel ion le remplace, comparer les λ. Beaucoup d'eau au départ.",
         beats=[
        "{an_co}{co_pts}{co_pts.1}{an_co.1}Troisième façon : le suivi conductimétrique. On mesure la conductivité sigma après chaque ajout. "
        "La courbe est formée de deux portions de droite. {co_pts.2}On les prolonge : leur intersection a pour abscisse V E. C'est une rupture de pente.",
        "{co_pts.3}Avantage : pas besoin de nombreux points près de l'équivalence. Quelques points de chaque côté suffisent pour tracer les droites.",
        "{-an_co}{-co_pts}{meth_p}Au bac, on te demande souvent de justifier l'allure des pentes. Voici la méthode. "
        "{meth_p.1}Un : écris la réaction support, et repère les ions spectateurs. "
        "{meth_p.2}Deux : avant l'équivalence, quel ion disparaît, et quel ion le remplace ? Compare leurs conductivités molaires ioniques, les lambda. "
        "{meth_p.3}Trois : après l'équivalence, quels ions s'accumulent sans réagir ? Leurs lambda s'ajoutent : la conductivité augmente.",
        "{-meth_p}{gr_co}{gr_co.1}Appliquons-la à notre acide chlorhydrique, noyé dans deux cents millilitres d'eau. "
        "{f_co}{f_co.1}Avant l'équivalence, chaque ion H trois O plus, de lambda trente-cinq, est remplacé par un ion sodium, de lambda cinq. "
        "La perte vaut trente par mole remplacée : sigma chute fortement.",
        "{f_co.2}Après l'équivalence, chaque ajout apporte un ion sodium et un ion H O moins : cinq plus dix-neuf virgule huit, environ vingt-cinq. "
        "Sigma remonte, un peu moins vite qu'elle n'était descendue. {gr_co.2}{gr_co.3}C'est le V dissymétrique de la courbe. "
        "{gr_co.4}Les deux droites se coupent à dix millilitres.",
        "{f_co.3}Pourquoi des lambda si grands pour H trois O plus et H O moins ? Rappel : ils se déplacent par relais de proton entre les molécules d'eau.",
        "{-gr_co}{-f_co}{ag}Un autre exemple classique : des ions argent titrés par des ions chlorure. "
        "{ag.1}La réaction support est une précipitation : Ag plus et Cl moins donnent un solide, le chlorure d'argent. "
        "{ag.2}Avant l'équivalence, chaque ion argent qui précipite est remplacé dans la solution par un ion sodium versé. "
        "Le lambda de l'argent est plus grand que celui du sodium : la solution perd un ion qui conduit bien et gagne un ion qui conduit moins. Sigma diminue. "
        "{ag.3}Après l'équivalence, il n'y a plus d'argent : les ions sodium et chlorure versés s'accumulent. Sigma augmente.",
        "{-ag}{eau}Pourquoi ajouter cent cinquante ou deux cents millilitres d'eau au départ ? Chaque ajout de titrant augmente le volume, donc dilue tous les ions : "
        "les droites se courberaient. En noyant le bécher dans un grand volume d'eau, les quelques millilitres versés deviennent négligeables. "
        "Et ce volume d'eau n'a pas besoin d'être précis : il ne change pas la quantité de titré, seulement sa concentration.",
        "{-eau}{choix}Alors, quelle méthode choisir ? {choix.1}Le colorimétrique demande un indicateur dont la zone contient le pH à l'équivalence, ou une espèce colorée. C'est la moins précise. "
        "{choix.2}Le pH-métrique demande une réaction acide-base. Bonne précision. "
        "{choix.3}Le conductimétrique demande des ions dont les lambda changent pendant le titrage. Bonne précision, même sans saut de pH.",
        "Le raisonnement attendu : le choix dépend de ce que la réaction rend observable. Une précipitation ne fait pas varier le pH : seule la conductimétrie convient. "
        "Un acide très faible donne un saut écrasé, difficile à lire : la conductimétrie peut faire mieux. Et un indicateur suffit pour un repérage rapide.",
        "{-choix}",
    ], vis={
        "an_co": dict(type="anim", nom="titrage", x=40, y=72, h=624, seg=[[56, 65]]),
        "co_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "σ = f(V) : deux portions de droite", "On les prolonge : l'intersection donne V_E = 10,0 mL",
            "Pas besoin de points serrés près de l'équivalence"]),
        "meth_p": dict(type="liste", titre="Justifier une pente : la méthode", items=[
            "Écrire la réaction support, repérer les ions spectateurs",
            "Avant V_E : quel ion disparaît, lequel le remplace ? Comparer les λ",
            "Après V_E : quels ions s'accumulent ? Leurs λ s'ajoutent, σ augmente"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "gr_co": dict(type="graphe", titre="Acide chlorhydrique + 200 mL d'eau", x=40, y=110, w=620, h=520,
                      ax=dict(x=[0, 20], y=[0, 40], gx=[5, 10, 15, 20], gy=[10, 20, 30, 40], lx="V_B (mL)", ly="σ (mS/m)"),
                      el=[dict(type="points", pts=[list(p) for p in SIG_HCL], c="el", pas=.08),
                          dict(type="droite", pts=[[0, 38.62], [12, 38.62 - 2.786 * 12]], c="sa", tir=True, ep=2.4),
                          dict(type="droite", pts=[[8, -8.94 + 2.011 * 8], [20, -8.94 + 2.011 * 20]], c="sa", tir=True, ep=2.4),
                          dict(type="point", x=9.9, y=11.0, c="vert", proj=True, lbl="V_E ≈ 10 mL", lp=[11.0, 9.0])]),
        "f_co": dict(type="formule", titre="Pourquoi ce V dissymétrique", x=690, y=130, w=560, lignes=[
            dict(f="avant : H₃O⁺ (35,0) remplacé par Na⁺ (5,01) : −30", taille=28, n="λ en mS·m²·mol^-1 · σ chute fortement"),
            dict(f="après : Na⁺ + HO⁻ s'ajoutent : 5,01 + 19,8 ≈ +25", taille=28, n="σ remonte, moins vite"),
            dict(f="H₃O⁺ et HO⁻ : relais de proton entre molécules d'eau", txt=True, taille=24)]),
        "ag": dict(type="formule", titre="Une précipitation suivie par conductimétrie", x=150, y=130, w=980, lignes=[
            dict(f="Ag⁺(aq) + Cl⁻(aq) → AgCl(s)", cadre=True, taille=40),
            dict(f="avant : Ag⁺ remplacé par Na⁺ ; λ(Ag⁺) > λ(Na⁺) → σ diminue", taille=32),
            dict(f="après : Na⁺ et Cl⁻ s'accumulent → σ augmente", taille=32)]),
        "eau": dict(type="note", titre="Pourquoi 150 ou 200 mL d'eau ?", cles=["dilue", "droites"],
                    t="Sans eau, chaque ajout dilue les ions et courbe les droites. Le volume d'eau ne change pas la quantité titrée.", x=170, y=210, w=940),
        "choix": dict(type="liste", titre="Choisir la méthode de suivi", items=[
            "Colorimétrique : indicateur adapté ou espèce colorée · la moins précise",
            "pH-métrique : réaction acide-base · saut, tangentes ou dérivée · bonne",
            "Conductimétrique : des λ qui changent · rupture de pente · bonne, même sans saut de pH"],
                      marques=["1", "2", "3"], x=150, y=160, w=980),
    }),

    # ================================================================ IX. retour au vinaigre : TP 4
    # cS1 = 0,10 × 11,9 / 20,0 = 5,95e-2 mol/L ; × 20 = 1,19 mol/L ; écart |1,19 − 1,18| / 1,18 ≈ 0,8 % ≈ 1 %
    # sans dilution : VE = 1,18 × 20,0 / 0,10 = 236 mL ; avec 11,3 mL : 5,65e-2 et 1,13 mol/L (écart 4 %)
    dict(id="tp4", chap="Retour au vinaigre : le titrage au laboratoire", fond="aube", humeur="lumiere",
         retenir="Diluer pour que V_E tombe dans la burette ; titrage rapide puis précis ; c_S1 = c_B V_E / V_A, puis × facteur de dilution ; conclure par un écart relatif.",
         beats=[
        "{tp_dil}Revenons à notre question de départ : le vinaigre est-il vraiment à sept pour cent ? Un titrage au laboratoire y répond. "
        "{tp_dil.1}D'abord, une dilution. À un virgule dix-huit mole par litre, titrer vingt millilitres de vinaigre pur demanderait deux cent trente-six millilitres de soude : dix burettes ! "
        "{tp_dil.2}On dilue donc vingt fois : pipette jaugée de cinq millilitres, fiole jaugée de cent millilitres. Le volume équivalent tombe vers douze millilitres, au milieu de la burette.",
        "{tp_dil.3}On choisit la dilution pour que V E tombe dans la burette, pas au hasard.",
        "{-tp_dil}{tp_et}{tp_et.1}Ensuite, un premier titrage rapide, millilitre par millilitre, avec le jus de chou rouge : le virage annonce l'équivalence entre onze et douze millilitres. "
        "{tp_et.2}Ce titrage grossier ne sert pas à conclure : il dit où ralentir. "
        "{tp_et.3}Puis le titrage précis, au pH-mètre, en resserrant les ajouts à zéro virgule cinq millilitre autour de l'équivalence. "
        "Loin de l'équivalence, le pH varie à peine ; dans le saut, une goutte fait gagner une unité. Sans points rapprochés, on n'aurait qu'un ou deux points dans la zone qui décide de tout.",
        "{-tp_et}{tp_calc}Et enfin, le calcul. {tp_calc.1}Réaction mole à mole : acide éthanoïque plus ion hydroxyde donne ion éthanoate plus eau. "
        "{tp_calc.2}La concentration de la solution diluée vaut c B fois V E sur V A : zéro virgule dix fois onze virgule neuf, sur vingt. "
        "Cinq virgule quatre-vingt-quinze fois dix puissance moins deux mole par litre. "
        "{tp_calc.3}On n'oublie pas la dilution : fois vingt. Un virgule dix-neuf mole par litre.",
        "{tp_calc.4}L'étiquette promettait un virgule dix-huit. L'écart relatif vaut environ un pour cent : l'indication « sept pour cent » est vérifiée.",
        "{-tp_calc}{recop}Une erreur fréquente, à ne pas faire : recopier une mauvaise valeur de V E. Avec onze virgule trois au lieu de onze virgule neuf, "
        "on trouve un virgule treize mole par litre, un écart de quatre pour cent, et on croirait le vinaigre trop faible. "
        "Le réflexe : relire V E sur la courbe au moment de l'écrire dans la formule.",
        "{-recop}{ece}Cette manipulation contient les trois actes de l'épreuve pratique : proposer une dilution adaptée à la burette, titrer en deux temps, rapide puis précis, "
        "et exploiter une courbe par deux méthodes. Puis conclure, en comparant à une valeur de référence. La conclusion rapporte autant que tout le reste.",
        "{-ece}",
    ], vis={
        "tp_dil": dict(type="formule", titre="Pourquoi diluer 20 fois", x=150, y=130, w=980, lignes=[
            dict(f="sans dilution : V_E = " + fr("1,18 × 20,0", "0,10") + " = 236 mL : dix burettes", ko=True, taille=36),
            dict(f="pipette jaugée de 5,0 mL → fiole jaugée de 100,0 mL : facteur 20", taille=34),
            dict(f="V_E vers 12 mL : au milieu d'une burette de 25 mL", ok=True, cadre=True, taille=36)]),
        "tp_et": dict(type="liste", titre="Deux titrages", items=[
            "Rapide, mL par mL, au jus de chou rouge : V_E entre 11 et 12 mL",
            "Il ne sert pas à conclure : il dit où ralentir",
            "Précis, au pH-mètre : ajouts de 0,5 mL autour de l'équivalence"], marques=["1", "→", "2"], x=150, y=170, w=980),
        "tp_calc": dict(type="formule", titre="Le calcul et la conclusion", x=150, y=100, w=980, lignes=[
            dict(f="CH₃COOH + HO⁻ → CH₃COO⁻ + H₂O : mole à mole", taille=32),
            dict(f="c_{S1} = " + fr("c_B × V_E", "V_A") + " = " + fr("0,10 × 11,9", "20,0") + " = 5,95 × 10^-2 mol·L^-1", taille=34),
            dict(f="c_{vinaigre} = 20 × 5,95 × 10^-2 = 1,19 mol·L^-1", cadre=True, taille=36),
            dict(f="écart = " + fr("∣1,19 − 1,18∣", "1,18") + " ≈ 1 % : l'étiquette est vérifiée", ok=True, taille=32)]),
        "recop": dict(type="note", titre="L'erreur de recopie", cles=["relire"],
                      t="11,3 mL au lieu de 11,9 mL : 1,13 mol/L et 4 % d'écart, une conclusion fausse. Relire V_E sur la courbe.", x=170, y=210, w=940),
        "ece": dict(type="liste", titre="Ce que vaut ce titrage pour l'épreuve pratique", items=[
            "Proposer une dilution adaptée au volume de la burette", "Titrer en deux temps : rapide, puis précis",
            "Exploiter la courbe par deux méthodes", "Conclure en comparant à la valeur de référence"],
                    marques=["1", "2", "3", "4"], x=150, y=150, w=980),
    }),

    # ================================================================ X. exercice 1 (simple)
    # aspirine : n = 0,500 / 180,2 = 2,775e-3 mol ; 250,0 mL, prélèvement 20,0 mL : 2,22e-4 mol ; VE attendu 11,1 mL
    # VE mesuré 11,0 mL : n = 2,00e-2 × 11,0e-3 = 2,20e-4 mol ; × 12,5 = 2,75e-3 mol ; m = 2,75e-3 × 180,2 = 0,4956 g ≈ 496 mg
    # écart (500 − 496) / 500 = 0,9 %
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. On veut vérifier qu'un comprimé d'aspirine contient bien cinq cents milligrammes d'acide acétylsalicylique, un monoacide noté A H. "
        "On dissout le comprimé dans une fiole jaugée de deux cent cinquante millilitres. On en prélève vingt millilitres, "
        "qu'on titre par de la soude à deux fois dix puissance moins deux mole par litre. L'équivalence est obtenue pour onze millilitres.",
        "Quatre questions : l'équation de la réaction support ; la quantité d'acide dans les vingt millilitres ; la masse d'acide dans le comprimé, et la conformité ; "
        "et enfin, quel indicateur coloré choisir, sachant que le pH à l'équivalence vaut environ huit ?",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche les quatre questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}C'est parti pour la correction. {s11}{s11.1}Question un : l'acide cède un ion H plus, l'ion hydroxyde le capte. "
        "A H plus H O moins donne A moins plus H deux O. {s11.2}Une réaction mole à mole.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux : à l'équivalence, la quantité d'acide égale la quantité de soude versée. "
        "{s12.2}c B fois V E : deux fois dix puissance moins deux, fois onze fois dix puissance moins trois. "
        "{s12.3}Deux virgule vingt fois dix puissance moins quatre mole. Attention : le volume en litres.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : on n'a titré que vingt millilitres sur deux cent cinquante. Il faut multiplier par deux cent cinquante sur vingt, soit douze virgule cinq. "
        "{s13.2}Deux virgule soixante-quinze fois dix puissance moins trois mole dans le comprimé. "
        "{s13.3}La masse : n fois M, soit deux virgule soixante-quinze fois dix puissance moins trois fois cent quatre-vingts virgule deux : "
        "quatre cent quatre-vingt-seize milligrammes. {s13.4}L'écart avec cinq cents vaut moins de un pour cent : le comprimé est conforme.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre : le pH à l'équivalence vaut environ huit, c'est un acide faible titré par une base forte. "
        "{s14.2}Il faut un indicateur dont la zone de virage contient huit : la phénolphtaléine, de huit virgule deux à dix, qui tient dans le saut. "
        "L'hélianthine, qui vire vers quatre, changerait de couleur bien trop tôt.",
        "{-s14}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", y=60, titre="Le comprimé d'aspirine", src="Exercice inventé pour la vidéo",
                    enonce=["Un comprimé d'aspirine « 500 » est dissous dans une fiole jaugée de 250,0 mL. On titre V_A = 20,0 mL de cette solution "
                            "par la soude (Na⁺ ; HO⁻) à c_B = 2,00 × 10^-2 mol·L^-1. L'équivalence est obtenue pour V_E = 11,0 mL."],
                    donnees=["acide acétylsalicylique : monoacide AH", "M = 180,2 g·mol^-1", "pH_E ≈ 8"],
                    questions=["Écrire l'équation de la réaction support.", "Calculer la quantité d'acide dans les 20,0 mL titrés.",
                               "En déduire la masse d'acide dans le comprimé. Est-il conforme ?",
                               "Choisir un indicateur coloré : hélianthine, BBT ou phénolphtaléine ?"]),
        "pa1": dict(type="pause", t="Équation, quantité titrée, masse dans le comprimé, indicateur."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="Le comprimé d'aspirine",
                     donnees=["fiole 250,0 mL", "V_A = 20,0 mL", "c_B = 2,00 × 10^-2 mol/L", "V_E = 11,0 mL", "M = 180,2 g/mol"],
                     questions=["Équation ?", "n dans 20,0 mL ?", "Masse, conformité ?", "Indicateur ?"]),
        "s11": dict(type="formule", titre="1 · La réaction support", x=540, y=180, w=700, lignes=[
            dict(f="AH + HO⁻ → A⁻ + H₂O", cadre=True, taille=42), dict(f="mole à mole", txt=True, taille=34)]),
        "s12": dict(type="formule", titre="2 · La quantité titrée", x=540, y=150, w=700, lignes=[
            dict(f="n(AH) = n(HO⁻)_E = c_B × V_E", taille=36),
            dict(f="n = 2,00 × 10^-2 × 11,0 × 10^-3", taille=36),
            dict(f="n = 2,20 × 10^-4 mol", cadre=True, taille=38)]),
        "s13": dict(type="formule", titre="3 · La masse dans le comprimé", x=540, y=110, w=700, lignes=[
            dict(f="facteur " + fr("250,0", "20,0") + " = 12,5", taille=34),
            dict(f="n_{comprimé} = 12,5 × 2,20 × 10^-4 = 2,75 × 10^-3 mol", taille=32),
            dict(f="m = n × M = 2,75 × 10^-3 × 180,2 = 0,496 g", cadre=True, taille=29),
            dict(f="496 mg pour 500 mg : écart < 1 %, conforme", ok=True, taille=32)]),
        "s14": dict(type="formule", titre="4 · L'indicateur", x=540, y=170, w=700, lignes=[
            dict(f="acide faible + base forte : pH_E ≈ 8 > 7", taille=34),
            dict(f="phénolphtaléine (8,2 – 10,0)", cadre=True, ok=True, taille=36),
            dict(f="hélianthine (3,1 – 4,4) : virerait bien trop tôt", ko=True, taille=30)]),
    }),

    # ================================================================ XI. exercice 2 (difficile)
    # batterie : c = 0,37 × 1,28 × 1000 / 98,1 = 4,83 mol/L ; dilué 100 fois : 4,83e-2 ; VE attendu = 2 × 4,83e-2 × 10,0 / 0,100 = 9,66 mL
    # sans dilution : 966 mL ; VE mesuré 9,50 mL : c_dil = 0,100 × 9,50 / (2 × 10,0) = 4,75e-2 ; c = 4,75 mol/L ; écart 1,6 %
    # oubli du facteur 2 : 9,50 mol/L (le double)
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile, parce qu'il croise tout le chapitre. L'électrolyte d'une batterie de voiture est une solution d'acide sulfurique, un diacide. "
        "L'étiquette indique trente-sept pour cent en masse, et une densité de un virgule vingt-huit.",
        "On dilue cent fois cette solution, puis on titre dix millilitres de la solution diluée par de la soude à zéro virgule cent mole par litre, avec un suivi pH-métrique. "
        "La méthode des tangentes donne un volume équivalent de neuf virgule cinq millilitres.",
        "Cinq questions. La concentration promise par l'étiquette. Pourquoi diluer. La relation à l'équivalence. "
        "La concentration mesurée, et la conclusion. Et enfin : quel résultat obtiendrait-on en oubliant les coefficients, et quel indicateur coloré conviendrait ?",
        "{-ex2}{pa2}Celui-là demande du temps. Mets sur pause, et fais-le en entier avant de regarder la correction.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un : on suit un litre de solution. c égale t fois d fois rhô eau, divisé par la masse molaire. "
        "{s21.2}Zéro virgule trente-sept, fois un virgule vingt-huit, fois mille, divisé par quatre-vingt-dix-huit virgule un. "
        "{s21.3}Quatre virgule quatre-vingt-trois moles par litre.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux : sans dilution, il faudrait verser deux fois quatre virgule quatre-vingt-trois fois dix, sur zéro virgule cent : "
        "{s22.2}presque mille millilitres de soude ! {s22.3}Diluée cent fois, la solution donne un volume équivalent attendu de neuf virgule sept millilitres, qui tient dans la burette.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois, le cœur de l'exercice. On écrit d'abord la réaction support : H deux S O quatre plus deux H O moins donne S O quatre deux moins plus deux H deux O. "
        "{s23.2}Il faut deux ions hydroxyde par molécule d'acide. La relation est donc : n acide égale n H O moins à l'équivalence, divisé par deux. "
        "{s23.3}Soit c fois V A égale c B fois V E sur deux.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre : la concentration diluée vaut c B fois V E, sur deux fois V A. "
        "{s24.2}Zéro virgule cent fois neuf virgule cinq, sur deux fois dix : quatre virgule soixante-quinze fois dix puissance moins deux mole par litre. "
        "{s24.3}Fois cent pour la dilution : quatre virgule soixante-quinze moles par litre. "
        "{s24.4}L'écart relatif avec quatre virgule quatre-vingt-trois vaut environ un virgule six pour cent : l'étiquette est cohérente avec la mesure.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq : sans le facteur deux, on trouverait neuf virgule cinq moles par litre, exactement le double. "
        "Et on conclurait, à tort, que l'étiquette est fausse. "
        "{s25.2}Pour l'indicateur : un acide fort titré par une base forte, le pH à l'équivalence vaut sept. Le bleu de bromothymol, de six à sept virgule six, convient.",
        "{-s25}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=60, titre="L'acide d'une batterie", src="Exercice inventé pour la vidéo",
                    enonce=["Étiquette de l'électrolyte : acide sulfurique H₂SO₄ à 37 % en masse, densité d = 1,28. On dilue 100 fois, puis on titre "
                            "V_A = 10,0 mL de la solution diluée par la soude à c_B = 0,100 mol·L^-1 (suivi pH-métrique) : V_E = 9,50 mL."],
                    donnees=["M(H₂SO₄) = 98,1 g·mol^-1", "ρ_{eau} = 1,00 × 10^3 g·L^-1", "H₂SO₄ + 2 HO⁻ → SO₄²⁻ + 2 H₂O"],
                    questions=["Calculer la concentration promise par l'étiquette.", "Pourquoi diluer avant de titrer ?",
                               "Écrire la relation à l'équivalence.", "Calculer la concentration mesurée. Conclure.",
                               "Résultat si l'on oublie les coefficients ? Quel indicateur coloré conviendrait ?"]),
        "pa2": dict(type="pause", t="Concentration de l'étiquette, dilution, relation à l'équivalence, concentration mesurée, piège et indicateur."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="L'acide d'une batterie",
                     donnees=["t = 37 %", "d = 1,28", "dilué 100 fois", "V_A = 10,0 mL", "c_B = 0,100 mol/L", "V_E = 9,50 mL"],
                     questions=["c de l'étiquette ?", "Pourquoi diluer ?", "Relation à l'équivalence ?", "c mesurée ? Conclure.", "Piège ? Indicateur ?"]),
        "s21": dict(type="formule", titre="1 · Ce que promet l'étiquette", x=540, y=150, w=700, lignes=[
            dict(f="c = " + fr("t × d × ρ_{eau}", "M"), taille=38),
            dict(f="c = " + fr("0,37 × 1,28 × 1,00 × 10^3", "98,1"), taille=36),
            dict(f="c = 4,83 mol·L^-1", cadre=True, taille=38)]),
        "s22": dict(type="formule", titre="2 · Pourquoi diluer", x=540, y=150, w=700, lignes=[
            dict(f="sans dilution : V_E = " + fr("2 × 4,83 × 10,0", "0,100") + " ≈ 966 mL", ko=True, taille=27),
            dict(f="impossible avec une burette de 25 mL", txt=True, taille=30),
            dict(f="dilué 100 fois : V_E attendu ≈ 9,7 mL", ok=True, cadre=True, taille=34)]),
        "s23": dict(type="formule", titre="3 · La relation à l'équivalence", x=540, y=140, w=700, lignes=[
            dict(f="H₂SO₄ + 2 HO⁻ → SO₄²⁻ + 2 H₂O", taille=34),
            dict(f="n(H₂SO₄) = " + fr("n(HO⁻)_E", "2"), cadre=True, taille=38),
            dict(f="c_{dil} × V_A = " + fr("c_B × V_E", "2"), cadre=True, taille=38)]),
        "s24": dict(type="formule", titre="4 · La concentration mesurée", x=540, y=110, w=700, lignes=[
            dict(f="c_{dil} = " + fr("c_B × V_E", "2 × V_A"), taille=36),
            dict(f="c_{dil} = " + fr("0,100 × 9,50", "2 × 10,0") + " = 4,75 × 10^-2 mol·L^-1", taille=32),
            dict(f="c = 100 × 4,75 × 10^-2 = 4,75 mol·L^-1", cadre=True, taille=34),
            dict(f="écart = " + fr("4,83 − 4,75", "4,83") + " ≈ 1,6 % : cohérent", ok=True, taille=32)]),
        "s25": dict(type="formule", titre="5 · Le piège et l'indicateur", x=540, y=150, w=700, lignes=[
            dict(f="sans le facteur 2 : c = 9,50 mol·L^-1, le double", ko=True, taille=32),
            dict(f="fort/fort : pH_E = 7 → bleu de bromothymol (6,0 – 7,6)", ok=True, cadre=True, taille=30)]),
    }),

    # ================================================================ XII. exercice 3 (type bac)
    # étiquette : t = 9 %, d = 1,04 : c = 0,09 × 1,04 × 1000 / 36,5 = 2,564 mol/L ; dilué 100 fois : 2,56e-2 ; VE attendu 12,8 mL
    # mesure : intersection des droites (moindres carrés) V = 12,36 ≈ 12,4 mL ; c_dil = 2,00e-2 × 12,4 / 10,0 = 2,48e-2 ;
    # c = 2,48 mol/L ; écart (2,56 − 2,48) / 2,56 = 3,3 % ; titre correspondant 2,48 × 36,5 / 1040 = 8,7 %
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac. Un détartrant pour sanitaires contient de l'acide chlorhydrique. "
        "Son étiquette annonce neuf pour cent en masse, avec une densité de un virgule zéro quatre. On veut vérifier cette indication par un titrage conductimétrique.",
        "On dilue le détartrant cent fois. On place dix millilitres de la solution diluée dans un bécher, avec environ deux cents millilitres d'eau distillée, "
        "et on titre par de la soude à deux fois dix puissance moins deux mole par litre.",
        "{-ex3}{gr_ex3}{gr_ex3.1}Voici les mesures : la conductivité baisse régulièrement, puis remonte au-delà de douze millilitres environ.",
        "{-gr_ex3}{ex3b}Cinq questions. Un : justifie l'allure des deux portions de la courbe, à l'aide des conductivités molaires ioniques. "
        "Deux : détermine le volume équivalent. Trois : calcule la concentration du détartrant. "
        "Quatre : compare à l'étiquette. Cinq : pourquoi avoir ajouté deux cents millilitres d'eau, et pourquoi ne pas avoir utilisé un indicateur coloré ?",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}Question un, une justification rédigée : c'est là qu'on perd le plus de points faute de méthode. "
        "{s31.1}La réaction support : H trois O plus plus H O moins donne deux H deux O. Les ions chlorure et sodium sont spectateurs. "
        "{s31.2}Avant l'équivalence, chaque ion H trois O plus, de lambda trente-cinq, est remplacé par un ion sodium, de lambda cinq. La conductivité diminue fortement. "
        "{s31.3}Après l'équivalence, les ions sodium et hydroxyde versés s'accumulent sans réagir : leurs lambda s'ajoutent, la conductivité augmente.",
        "{-s31}{ex3c.q2}{gr_ex3d}{gr_ex3d.1}Question deux. {gr_ex3d.2}On trace la droite qui passe au mieux par les points d'avant l'équivalence. "
        "{gr_ex3d.3}Puis celle d'après. {gr_ex3d.4}Elles se coupent à environ douze virgule quatre millilitres : c'est V E.",
        "{-gr_ex3d}{ex3c.q3}{s33}{s33.1}Question trois : réaction mole à mole, donc c dilué fois V A égale c B fois V E. "
        "{s33.2}c dilué égale deux fois dix puissance moins deux, fois douze virgule quatre, sur dix : deux virgule quarante-huit fois dix puissance moins deux mole par litre. "
        "{s33.3}Fois cent : deux virgule quarante-huit moles par litre.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Question quatre : l'étiquette promet t fois d fois rhô eau sur M : zéro virgule zéro neuf, fois un virgule zéro quatre, fois mille, "
        "sur trente-six virgule cinq. Deux virgule cinquante-six moles par litre. "
        "{s34.2}L'écart relatif vaut environ trois pour cent. {s34.3}La mesure correspond à un titre de huit virgule sept pour cent : "
        "l'indication de neuf pour cent, donnée sans décimale, est cohérente.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq. L'eau ajoutée rend la dilution due aux ajouts de soude négligeable : les portions restent presque droites. "
        "Elle ne change pas la quantité d'acide titrée. "
        "{s35.2}Regard critique : la dilution n'est pas tout à fait négligeable, elle courbe un peu les droites. "
        "Avec ces points, le vrai volume équivalent est légèrement plus grand que celui qu'on lit, d'environ un pour cent. "
        "{s35.3}Et un indicateur coloré était possible, mais la couleur se juge à l'œil : c'est la méthode la moins précise. "
        "La conductimétrie exploite toutes les mesures, de part et d'autre de l'équivalence.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Le détartrant pour sanitaires", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Étiquette : acide chlorhydrique à 9 % en masse, densité d = 1,04. Le détartrant est dilué 100 fois.",
                            "V_A = 10,0 mL de solution diluée + environ 200 mL d'eau sont titrés par la soude à c_B = 2,00 × 10^-2 mol·L^-1, avec un suivi conductimétrique."],
                    donnees=["M(HCl) = 36,5 g·mol^-1", "λ (mS·m²·mol^-1) : H₃O⁺ 35,0 · HO⁻ 19,8 · Cl⁻ 7,63 · Na⁺ 5,01"]),
        "gr_ex3": dict(type="graphe", titre="Document · conductivité mesurée", x=330, y=110, w=640, h=520,
                       ax=dict(x=[0, 25], y=[0, 55], gx=[5, 10, 15, 20, 25], gy=[10, 20, 30, 40, 50], lx="V_B (mL)", ly="σ (mS/m)"),
                       el=[dict(type="points", pts=[list(p) for p in SIG_EX3], c="el", pas=.12)]),
        "ex3b": dict(type="exo", niveau="bac", titre="Le détartrant · questions",
                     questions=["Justifier l'allure des deux portions de la courbe.", "Déterminer le volume équivalent V_E.",
                                "Calculer la concentration c du détartrant.", "Comparer à l'indication de l'étiquette.",
                                "Pourquoi 200 mL d'eau ? Pourquoi pas un indicateur coloré ?"]),
        "pa3": dict(type="pause", t="Pentes, volume équivalent, concentration, comparaison à l'étiquette, regard critique."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Le détartrant",
                     donnees=["t = 9 %", "d = 1,04", "dilué 100 fois", "V_A = 10,0 mL", "c_B = 2,00 × 10^-2 mol/L"],
                     questions=["Les pentes ?", "V_E ?", "c ?", "Étiquette ?", "Eau ? Indicateur ?"]),
        "s31": dict(type="liste", titre="1 · Justifier les pentes", items=[
            "H₃O⁺ + HO⁻ → 2 H₂O ; Cl⁻ et Na⁺ spectateurs",
            "Avant V_E : H₃O⁺ (35,0) remplacé par Na⁺ (5,01) → σ diminue fortement",
            "Après V_E : Na⁺ et HO⁻ s'accumulent → σ augmente"], marques=["1", "2", "3"], x=540, y=140, w=700),
        "gr_ex3d": dict(type="graphe", titre="Les deux droites", x=560, y=110, w=660, h=520,
                        ax=dict(x=[0, 25], y=[0, 55], gx=[5, 10, 15, 20, 25], gy=[10, 20, 30, 40, 50], lx="V_B (mL)", ly="σ (mS/m)"),
                        el=[dict(type="points", pts=[list(p) for p in SIG_EX3], c="el", pas=.05),
                            dict(type="droite", pts=[[0, 50.51], [14.5, 50.51 - 2.940 * 14.5]], c="sa", ep=2.6),
                            dict(type="droite", pts=[[10, -11.09 + 2.046 * 10], [24.5, -11.09 + 2.046 * 24.5]], c="sa", ep=2.6),
                            dict(type="point", x=12.36, y=14.19, c="vert", proj=True, lbl="V_E ≈ 12,4 mL", lp=[15.0, 9.0])]),
        "s33": dict(type="formule", titre="3 · La concentration", x=540, y=150, w=700, lignes=[
            dict(f="c_{dil} × V_A = c_B × V_E", taille=36),
            dict(f="c_{dil} = " + fr("2,00 × 10^-2 × 12,4", "10,0") + " = 2,48 × 10^-2 mol·L^-1", taille=32),
            dict(f="c = 100 × c_{dil} = 2,48 mol·L^-1", cadre=True, taille=36)]),
        "s34": dict(type="formule", titre="4 · Comparer à l'étiquette", x=540, y=140, w=700, lignes=[
            dict(f="c_{étiquette} = " + fr("0,09 × 1,04 × 1,00 × 10^3", "36,5") + " = 2,56 mol·L^-1", taille=30),
            dict(f="écart = " + fr("2,56 − 2,48", "2,56") + " ≈ 3 %", taille=34),
            dict(f="titre mesuré ≈ 8,7 % : cohérent avec 9 %", ok=True, cadre=True, taille=30)]),
        "s35": dict(type="liste", titre="5 · L'eau et le choix de la méthode", items=[
            "L'eau rend la dilution par les ajouts négligeable ; elle ne change pas n(H₃O⁺)",
            "Regard critique : les droites restent un peu courbées ; V_E sous-estimé d'environ 1 %",
            "Indicateur : couleur jugée à l'œil, moins précis ; σ exploite toutes les mesures"], marques=["1", "!", "2"], x=540, y=140, w=700),
    }),

    # ================================================================ XIII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, l'équivalence : les réactifs dans les proportions stœchiométriques. "
        "{carte.1}Côté calcul : n A sur a égale n B E sur b, et c A V A égale c B V E pour une réaction mole à mole. "
        "{carte.2}Côté étiquette : c égale t fois d fois rhô eau sur M. "
        "{carte.3}Côté pH : un saut, les tangentes ou la dérivée, et un indicateur dont la zone contient le pH à l'équivalence. "
        "{carte.4}Côté conductivité : deux droites, et des pentes qu'on justifie par les lambda des ions qui disparaissent et qui s'accumulent.",
        "{-carte}{bac}Et voici ce que le bac peut te demander, à cocher. "
        "{bac.1}Établir la composition du système après un ajout de titrant. "
        "{bac.2}Exploiter un titrage pour déterminer une quantité de matière, une concentration ou une masse. "
        "{bac.3}Justifier qualitativement les pentes d'une courbe conductimétrique. "
        "{bac.4}Calculer une concentration à partir d'un titre massique et d'une densité. "
        "{bac.5}Représenter avec un programme l'évolution des quantités de matière. "
        "{bac.6}Mettre en œuvre un suivi pH-métrique. "
        "{bac.7}Et un suivi conductimétrique.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre. Pour les fixer, entraîne-toi sur d'autres exercices. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="L'ÉQUIVALENCE", branches=[
            dict(t="Le calcul", items=["n_A / a = n_{B,E} / b", "c_A V_A = c_B V_E", "écrire d'abord la réaction"]),
            dict(t="L'étiquette", items=["t = m_{soluté} / m_{solution}", "d = ρ / ρ_{eau}", "c = t d ρ_{eau} / M"]),
            dict(t="Le pH", items=["un saut au milieu", "tangentes ou dérivée", "indicateur : pH_E dans la zone"]),
            dict(t="La conductivité", items=["deux droites, V_E à l'intersection", "pentes : comparer les λ", "beaucoup d'eau au départ"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Établir la composition du système après un ajout", "Exploiter un titrage : n, c ou m",
            "Justifier les pentes d'une courbe conductimétrique", "Concentration à partir de t et d",
            "Programmer l'évolution des quantités de matière", "Mettre en œuvre un suivi pH-métrique",
            "Mettre en œuvre un suivi conductimétrique"], marques=["✓"] * 7, x=170, y=80, w=940, petit=True),
    }),
]

QUIZ = [
    dict(q="À l'équivalence d'un titrage…",
         r=["le pH vaut toujours 7", "les réactifs ont été introduits dans les proportions stœchiométriques", "le réactif titrant est en excès"],
         ok=1, ex="C'est la définition. Le pH ne vaut 7 que pour un acide fort titré par une base forte.", voir="def_eq"),
    dict(q="On titre 20,0 mL d'acide par la soude à 0,10 mol/L, mole à mole ; V_E = 15,0 mL. c_A vaut…",
         r=["7,5 × 10⁻² mol/L", "0,13 mol/L", "3,0 × 10⁻² mol/L"], ok=0,
         ex="c_A = c_B × V_E / V_A = 0,10 × 15,0 / 20,0 = 7,5 × 10⁻² mol/L.", voir="f_cc"),
    dict(q="On titre de l'acide sulfurique H₂SO₄ par la soude. La relation à l'équivalence est…",
         r=["n(H₂SO₄) = n(HO⁻)_E", "n(H₂SO₄) = n(HO⁻)_E / 2", "n(H₂SO₄) = 2 n(HO⁻)_E"], ok=1,
         ex="H₂SO₄ + 2 HO⁻ → SO₄²⁻ + 2 H₂O : il faut deux ions hydroxyde par molécule d'acide.", voir="coef"),
    dict(q="Avant l'équivalence, le réactif limitant est…",
         r=["le réactif titré, dans le bécher", "le réactif titrant versé", "aucun des deux"], ok=1,
         ex="Chaque goutte versée réagit entièrement, car il reste du titré. Après l'équivalence, c'est l'inverse.", voir="an_ti"),
    dict(q="Un vinaigre « à 7 % » (d = 1,01, M = 60,1 g/mol) a une concentration de…",
         r=["1,18 mol/L", "0,12 mol/L", "7,0 mol/L"], ok=0,
         ex="c = t × d × ρ_eau / M = 0,07 × 1,01 × 1 000 / 60,1 = 1,18 mol/L.", voir="ex_vin"),
    dict(q="Pourquoi le pH fait-il un saut près de l'équivalence ?",
         r=["Parce que la réaction s'accélère", "Parce que le pH est un logarithme : une goutte change [H₃O⁺] de plusieurs ordres de grandeur",
            "Parce que la sonde sature"], ok=1,
         ex="Près de l'équivalence, une goutte divise l'acide restant par 10, puis 100… chaque facteur 10 vaut une unité de pH.", voir="gr_ph"),
    dict(q="Pour titrer l'acide éthanoïque par la soude (pH_E ≈ 8,3), quel indicateur choisir ?",
         r=["l'hélianthine (3,1 – 4,4)", "le bleu de bromothymol (6,0 – 7,6)", "la phénolphtaléine (8,2 – 10,0)"], ok=2,
         ex="Le pH à l'équivalence doit appartenir à la zone de virage : seule la phénolphtaléine convient.", voir="gr_ind"),
    dict(q="Titrage conductimétrique de l'acide chlorhydrique par la soude : avant l'équivalence, σ diminue parce que…",
         r=["les ions Cl⁻ disparaissent", "chaque H₃O⁺ (λ = 35,0) est remplacé par un Na⁺ (λ = 5,01)", "le volume augmente"], ok=1,
         ex="La solution perd un ion très conducteur et gagne un ion peu conducteur.", voir="f_co"),
    dict(q="Une précipitation Ag⁺ + Cl⁻ → AgCl ne fait pas varier le pH. Quel suivi choisir ?",
         r=["pH-métrique", "conductimétrique", "aucun suivi n'est possible"], ok=1,
         ex="Les λ des ions changent pendant le titrage : la rupture de pente de σ donne V_E.", voir="choix"),
    dict(q="Pourquoi ajoute-t-on environ 200 mL d'eau avant un titrage conductimétrique ?",
         r=["Pour augmenter la quantité d'acide", "Pour que les ajouts de titrant diluent peu : les portions restent droites", "Pour faire baisser le pH"],
         ok=1, ex="L'eau ne change pas la quantité titrée ; elle rend la dilution par les ajouts négligeable.", voir="eau"),
]

CREDITS = [
    "Images : titrage à la burette, gravure de l'ouvrage d'Alessandri, 1895 (domaine public) ; pH-mètre de laboratoire, OER_CampLev, CC BY-SA 4.0 ; "
    "jus de chou rouge, brittgow, CC BY 2.0. Images trouvées sur Wikimedia Commons.",
    "Animations, schémas et graphiques : faits pour la vidéo ; courbes de pH et de conductivité calculées. Valeurs du titrage du vinaigre : mesures réalisées au laboratoire. "
    "Les trois exercices sont inventés pour la vidéo.",
]
