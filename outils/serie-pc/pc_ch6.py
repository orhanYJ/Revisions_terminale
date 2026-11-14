"""Physique-chimie, chapitre 6 : « Interférences et diffraction » — le cours en vidéo.

Même modèle que pc_ch4.py et pc_ch5.py (voir leur en-tête). Contenu : le chapitre 6 du site (pc/index.html : rappels,
fiches 1 à 11, formules), rien au-delà ; l'ouverture circulaire (1,22 λ/d), les hyperboles de la cuve à ondes, l'unité
profonde diffraction / interférences et les interféromètres géants sont dits « hors programme », comme dans pc/index.html.
Animations du site rejouées : pc/anim/diffraction.html (8 étapes, 92 s) et pc/anim/interferences.html (8 étapes, 90 s).
Illustrations du moteur : onde, dualite. Graphiques calculés ci-dessous (profils d'intensité, sommes de sinusoïdes, droites).
Les trois exercices sont inventés pour la vidéo (valeurs recalculées en commentaire de chaque exercice).
Usage : python3 outils/serie-philo/verifier.py pc_ch6 ; SERIE_MOTEUR=muet generer.py pc_ch6 ; chevauchements.py ch6.
"""
import math

SITE = "pc"
VOIX_VIVANTE = True   # voix dite phrase par phrase, prise la plus expressive (generer.py, voix_qwen.py)
RYTHME = "vivant"     # silences variables selon la fin de phrase (generer.py, _ecart_vivant)
CODE = "ch6"
NOTION = "Interférences et diffraction"
NUM = 6
TITRE = "Interférences et diffraction"
SUIVANT = "Les autres chapitres de physique-chimie"
PRONONCIATION = {"Young": "Yongue", "Fresnel": "Frénel", "Huygens": "Huiguens", "tweeter": "touiteur", "woofer": "woufeur",
                 "Blu-ray": "Blou-rè", "§l": "èle"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]".replace(" ", " ")


# ---------------------------------------------------------------- données des graphiques
def _sinc2(u):
    return 1.0 if abs(u) < 1e-9 else (math.sin(u) / u) ** 2


# profil de diffraction d'une fente : λ = 650 nm, a = 100 µm, D = 2,00 m → L = 2λD/a = 26 mm ;
# abscisse = position sur l'écran (mm), centre à 40 mm, premières extinctions à 27 et 53 mm
PROFIL = [[round(x, 2), round(_sinc2(math.pi * (x - 40) / 13), 4)] for x in [i * 0.25 for i in range(321)]]
# fentes d'Young réelles : λ = 650 nm, D = 2,00 m, écart a = 0,50 mm → i = λD/a = 2,6 mm ;
# largeur de chaque fente ℓ = 0,10 mm → tache centrale 2λD/ℓ = 26 mm (centre à 30 mm, extinctions à 17 et 43 mm)
YOUNG = [[round(x, 2), round(math.cos(math.pi * (x - 30) / 2.6) ** 2 * _sinc2(math.pi * (x - 30) / 13), 4)]
         for x in [i * 0.1 for i in range(601)]]
ENVEL = [[round(x, 2), round(_sinc2(math.pi * (x - 30) / 13), 4)] for x in [i * 0.25 for i in range(241)]]
# deux signaux synchrones de même amplitude A (en unités de A), t en périodes
_T = [i / 60 for i in range(121)]
SIN1 = [[round(t, 3), round(math.cos(2 * math.pi * t), 4)] for t in _T]
SIN_OP = [[round(t, 3), round(-math.cos(2 * math.pi * t), 4)] for t in _T]
SOMME_PH = [[round(t, 3), round(2 * math.cos(2 * math.pi * t), 4)] for t in _T]
# série de mesures classique : D = 1,800 m ; a = 30, 40, 60, 80, 100, 150, 200 µm ; L = 77, 59, 40, 30, 24, 16, 12 mm
# θ = L/(2D) ; abscisse 1/a en 10³ m⁻¹, ordonnée θ en 10⁻³ rad ; modélisation affine (numpy.polyfit) :
# pente 6,39 × 10⁻⁷ m (≈ 6,4 × 10⁻⁷ m, λ ≈ 640 nm), ordonnée à l'origine 2,7 × 10⁻⁴ rad (≈ 0)
MES_A = [30, 40, 60, 80, 100, 150, 200]
MES_L = [77, 59, 40, 30, 24, 16, 12]
MESURES = [[round(1000 / a, 2), round(L / 3.6, 2)] for a, L in zip(MES_A, MES_L)]
# exercice 3 : D = 2,00 m ; a = 40, 50, 80, 100, 125 µm ; L = 64, 51, 32, 26, 20 mm ; 1/a = 25 ; 20 ; 12,5 ; 10 ; 8 (10³ m⁻¹)
# droite passant par l'origine (moindres carrés) : pente 2,557 mm par 10³ m⁻¹ = 2,56 × 10⁻⁶ m²
EX3 = [[25, 64], [20, 51], [12.5, 32], [10, 26], [8, 20]]
EX3_K = 2.557

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="cosmos", humeur="mystere", carton=False, beats=[
        "{q1}Quelqu'un parle dans le couloir, derrière une porte ouverte. Tu l'entends parfaitement. Mais tu ne le vois pas.",
        "{-q1}{q2}Le son passe le coin du mur. La lumière, non. Pourquoi une telle différence ?",
        ("Parce que ce sont deux ondes de tailles très différentes.", {"rate": "-6%"}),
        "{-q2}{q3}Deuxième énigme. Une bulle de savon est faite d'eau, sans couleur. "
        "Et pourtant, elle brille de toutes les couleurs. D'où viennent-elles ?",
        "{-q3}{q4}Les deux réponses tiennent dans ce chapitre. Deux comportements que seules les ondes savent avoir : "
        "la {!diffraction}diffraction, et les {!interférences}interférences.",
        "{-q4}{plan}Voici le chemin. {plan.1}D'abord quelques rappels sur les ondes. "
        "{plan.2}Puis la diffraction : le phénomène, ses conditions, l'angle caractéristique, et la mesure sur un écran. "
        "{plan.3}Ensuite les interférences : la superposition, la différence de marche, les fentes d'Young et l'interfrange. "
        "{plan.4}Puis les conséquences concrètes de ces deux phénomènes, tout autour de nous. "
        "{plan.5}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q1": dict(type="question", t="Derrière la porte : on l'entend, on ne le voit pas."),
        "q2": dict(type="question", t="Le son contourne le mur. Pas la lumière. Pourquoi ?"),
        "q3": dict(type="question", t="Une bulle d'eau incolore… et toutes les couleurs."),
        "q4": dict(type="question", t="Diffraction et interférences : deux signatures des ondes."),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les rappels : onde, longueur d'onde, unités",
            "La diffraction : phénomène, conditions, θ = λ/a, mesure sur un écran",
            "Les interférences : superposition, différence de marche, fentes d'Young",
            "Les conséquences concrètes, autour de nous",
            "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 6", t="Interférences et diffraction",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. rappels
    dict(id="rappels", chap="Les rappels : ondes et longueur d'onde", fond="nuit", humeur="calme",
         retenir="λ = v × T = v / f, en mètres. Lumière visible : 400 à 800 nm. Tout convertir en mètres : 1 nm = 10⁻⁹ m, 1 µm = 10⁻⁶ m.",
         beats=[
        "{def_o}Tout ce chapitre parle d'ondes. Une onde progressive, c'est une perturbation qui se propage de proche en proche. "
        "{def_o.1}Elle transporte de l'énergie, mais pas de matière. Le son et les vagues ont besoin d'un milieu. La lumière, elle, traverse aussi le vide.",
        "{-def_o}{onde}Une onde périodique se répète dans le temps, avec une période T, et une fréquence f égale à un sur T. "
        "{onde.1}Et elle se répète dans l'espace : la distance entre deux crêtes successives, c'est la longueur d'onde, lambda.",
        "{onde.c}Pour la lumière, la célérité vaut trois cent mille kilomètres par seconde. "
        "Et pendant une période, toute onde avance d'exactement une longueur d'onde.",
        "{-onde}{f_l}{f_l.1}D'où la relation à connaître : lambda égale v fois T, c'est-à-dire v sur f. "
        "{f_l.2}Lambda en mètres, v en mètres par seconde, T en secondes, f en hertz.",
        "{f_l.3}Par exemple, un son de six cent quatre-vingts hertz, dans l'air, à trois cent quarante mètres par seconde : "
        "lambda vaut zéro virgule cinquante mètre.",
        "{-f_l}{og}Garde en tête trois ordres de grandeur : ils vont tout expliquer. "
        "{og.1}Le son dans l'air : de un virgule sept centimètre à dix-sept mètres. Une voix : environ un mètre. "
        "{og.2}La houle : de dix à cent mètres. "
        "{og.3}Et la lumière visible : de quatre cents à huit cents nanomètres. Environ un demi-micromètre.",
        "{-og}{piege_u}Et voici l'erreur la plus fréquente du chapitre : mélanger les unités. "
        "{piege_u.1}Avant le moindre calcul, on convertit tout en mètres. "
        "Un nanomètre, c'est dix puissance moins neuf mètre. Un micromètre, dix puissance moins six.",
        "{-piege_u}{chg}Dernier rappel. {chg.1}Quand une onde change de milieu, sa fréquence reste celle de la source ; "
        "c'est sa célérité, et donc sa longueur d'onde, qui changent. "
        "{chg.2}Retiens-le, car on va voir un phénomène où rien de tout cela ne change. Seulement la direction.",
        "{-chg}",
    ], vis={
        "def_o": dict(type="def", terme="Onde progressive", cles=["perturbation", "énergie"],
                      t="La propagation d'une perturbation, de proche en proche.",
                      etape="Transport d'énergie, sans transport de matière.", x=170, y=200, w=940),
        "onde": dict(type="illu", nom="onde", x=110, y=150, w=1060, h=420),
        "f_l": dict(type="formule", titre="La double périodicité", x=150, y=140, w=980, lignes=[
            dict(f="λ = v × T = " + fr("v", "f"), cadre=True, taille=54),
            dict(f="λ en m · v en m·s^-1 · T en s · f en Hz", txt=True),
            dict(f="Son à 680 Hz : λ = " + fr("340", "680") + " = 0,50 m", taille=36)]),
        "og": dict(type="liste", titre="Trois ordres de grandeur", items=[
            "Son dans l'air : de 1,7 cm (20 kHz) à 17 m (20 Hz) · une voix ≈ 1 m",
            "Houle : de 10 à 100 m",
            "Lumière visible : de 400 à 800 nm, environ 0,5 µm"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "piege_u": dict(type="note", titre="Tout en mètres", cles=["mètres"],
                        t="λ en nm, a en µm, D en m, L en cm : on convertit tout en mètres avant de calculer.",
                        etape="1 nm = 10^-9 m · 1 µm = 10^-6 m · 1 mm = 10^-3 m · 650 nm = 6,50 × 10^-7 m", x=170, y=190, w=940),
        "chg": dict(type="liste", titre="Ce qui change, ce qui ne change pas", items=[
            "Changement de milieu : f reste celle de la source ; v et λ changent",
            "Bientôt : un phénomène où f, v et λ ne changent pas. Seule la direction."], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ II. le phénomène de diffraction
    dict(id="phenomene", chap="Le phénomène de diffraction", fond="nuit", humeur="mystere",
         retenir="Diffraction : une onde qui rencontre une ouverture ou un obstacle s'étale au-delà. Même f, même v, même λ : seule la direction change. Toutes les ondes.",
         beats=[
        "{an1}{pts1}{pts1.1}{an1.1}Une expérience classique : la cuve à ondes, vue de dessus. "
        "Des ondes planes, aux crêtes espacées de lambda, arrivent sur une paroi percée d'une ouverture de largeur a.",
        "Ici, l'ouverture est large : plus de cinq fois lambda. L'onde passe presque en ligne droite, en gardant la largeur de l'ouverture.",
        "{pts1.2}{an1.2}Maintenant, on rétrécit l'ouverture, jusqu'à l'ordre de lambda. Et là, surprise : "
        "l'onde s'étale derrière la paroi, en ondes presque circulaires. Comme si l'ouverture était devenue une nouvelle source.",
        "{pts1.3}Regarde bien l'écart entre les crêtes, avant et après la paroi. Il n'a pas changé : la longueur d'onde est la même.",
        "{-pts1}{-an1}{def_d}C'est la {!diffraction}diffraction : la modification de la direction de propagation d'une onde "
        "qui rencontre une ouverture ou un obstacle. L'onde s'étale au-delà de la ligne droite.",
        "{def_d.1}Elle garde la même fréquence, la même célérité, donc la même longueur d'onde. Seule sa direction change.",
        "{-def_d}{toutes}Ce phénomène concerne toutes les ondes. {toutes.1}Les ondes mécaniques : le son, les vagues, les ondes sismiques. "
        "{toutes.2}Et les ondes électromagnétiques : la lumière, les ondes radio, les rayons X. "
        "{toutes.3}Observer de la diffraction, c'est donc la signature d'un comportement ondulatoire.",
        "{toutes.4}Et un obstacle diffracte comme une ouverture de même taille : un son contourne un pilier, la lumière s'étale derrière un fil fin.",
        "{-toutes}{porte}{porte.g}Revenons à l'énigme du couloir. Le son de la voix a une longueur d'onde d'environ un mètre. "
        "La porte aussi fait environ un mètre. Le son est donc fortement diffracté : il s'étale dans la pièce, et tu l'entends sans voir la personne.",
        "{porte.d}La lumière, elle, a une longueur d'onde un million de fois plus petite : elle n'est pas visiblement diffractée par la porte.",
        "{-porte}{refr}Attention à ne pas confondre avec la réfraction. La réfraction, c'est un changement de direction au passage d'un milieu à un autre, "
        "de l'air à l'eau par exemple. {refr.1}La diffraction se produit sans changer de milieu, à cause de la taille limitée de l'ouverture ou de l'obstacle.",
        "{-refr}",
    ], vis={
        "an1": dict(type="anim", nom="diffraction", x=40, y=72, h=624, seg=[[0.5, 10.9], [12.2, 22.9]]),
        "pts1": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Ouverture large (a > 5 λ) : l'onde passe presque en ligne droite",
            "Ouverture de l'ordre de λ : l'onde s'étale en ondes presque circulaires",
            "Avant et après la paroi : même écart entre les crêtes, même λ"]),
        "def_d": dict(type="def", terme="La diffraction", cles=["direction", "obstacle"],
                      t="Modification de la direction de propagation d'une onde qui rencontre une ouverture ou un obstacle : l'onde s'étale.",
                      etape="Même fréquence, même célérité, même λ : seule la direction change.", x=170, y=180, w=940),
        "toutes": dict(type="liste", titre="Toutes les ondes", items=[
            "Ondes mécaniques : son, vagues, ondes sismiques",
            "Ondes électromagnétiques : lumière, radio, rayons X",
            "La diffraction est une signature ondulatoire",
            "Un obstacle diffracte comme une ouverture de même taille"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "porte": dict(type="cols", g="Le son de la voix", gq="λ ≈ 1 m ≈ largeur de la porte · forte diffraction : on l'entend",
                      d="La lumière", dq="λ ≈ 0,5 µm ≪ 1 m · pas de diffraction visible : on ne voit pas", vs="≠"),
        "refr": dict(type="note", titre="Diffraction ≠ réfraction", cles=["milieu", "taille"],
                     t="Réfraction : changement de direction au passage d'un milieu à un autre, avec changement de célérité.",
                     etape="Diffraction : sans changement de milieu, à cause de la taille limitée de l'ouverture ou de l'obstacle.",
                     x=170, y=200, w=940),
    }),

    # ================================================================ III. conditions et angle θ
    dict(id="angle", chap="Conditions et angle caractéristique", fond="nuit", humeur="lumiere",
         retenir="Diffraction d'autant plus marquée que a est petite devant λ. θ = λ / a : θ en radians, λ et a dans la même unité. θ est un demi-angle.",
         beats=[
        "{cond}Quand la diffraction est-elle visible ? Ce qui compte, ce n'est pas la taille de l'ouverture seule. "
        "C'est sa taille comparée à la longueur d'onde. {cond.1}La diffraction est d'autant plus marquée que la dimension a de l'ouverture est petite devant lambda.",
        "{cond.2}Si a est de l'ordre de lambda, ou plus petite, la diffraction est importante : l'onde s'étale presque partout. "
        "{cond.3}Si a est très grande devant lambda, l'étalement devient négligeable. On retrouve la propagation en ligne droite : "
        "c'est le domaine de l'optique géométrique, celui des rayons lumineux.",
        "{cond.4}Et pour la lumière, on la voit encore très bien avec une fente de zéro virgule un millimètre : environ cent cinquante fois lambda.",
        "{-cond}{piege_p}Le piège classique : « l'ouverture est petite, donc il y a diffraction ». Non : il faut toujours comparer a à lambda. "
        "{piege_p.1}Une fente d'un millimètre est minuscule pour un son d'un mètre, mais énorme pour des rayons X.",
        "{-piege_p}{an2}{pts2}{pts2.1}{an2.1}Mesurons maintenant cet étalement. Derrière une fente, l'onde diffractée n'est pas répartie uniformément. "
        "L'essentiel de l'énergie part dans un cône autour de la direction incidente. Il est limité par deux directions où l'onde s'annule.",
        "{pts2.2}L'angle caractéristique de diffraction, noté thêta, c'est l'écart angulaire entre la direction de l'onde incidente "
        "et la première direction où l'onde s'annule. {pts2.3}Attention : c'est un demi-angle. Le cône central va de moins thêta à plus thêta.",
        "{-pts2}{f_th}{f_th.1}Pour une fente de largeur a, il vaut : thêta égale lambda sur a. "
        "{f_th.2}Thêta en radians. Lambda et a dans la même unité, en général le mètre.",
        "{f_th.3}Thêta augmente quand lambda augmente : à fente égale, le rouge est plus diffracté que le bleu. "
        "{f_th.4}Et thêta augmente quand a diminue : plus la fente est fine, plus l'onde s'étale.",
        "{-f_th}{-an2}{ex_th}Deux exemples. {ex_th.1}Un laser rouge de six cent cinquante nanomètres, une fente de cent micromètres. "
        "{ex_th.2}Thêta vaut six cent cinquante fois dix puissance moins neuf, divisé par cent fois dix puissance moins six. "
        "Six virgule cinq fois dix puissance moins trois radian. À peine zéro virgule trente-sept degré : la lumière s'étale très peu.",
        "{ex_th.3}Un son de trente centimètres de longueur d'onde, à travers une ouverture de quatre mètres : "
        "{ex_th.4}thêta vaut zéro virgule zéro soixante-quinze radian, environ quatre virgule trois degrés.",
        "{-ex_th}{dir}Dans quelle direction la figure s'étale-t-elle ? Dans la direction où l'ouverture est étroite. "
        "{dir.1}Une fente verticale, fine et haute, donne une figure étalée à l'horizontale.",
        "{-dir}{pieges_th}Trois pièges sur thêta. {pieges_th.1}Un : c'est un demi-angle. "
        "{pieges_th.2}Deux : lambda sur a donne des radians, jamais des degrés. "
        "{pieges_th.3}Trois : a, c'est la largeur de la fente, pas la largeur de la tache sur l'écran.",
        "{-pieges_th}",
    ], vis={
        "cond": dict(type="liste", titre="Les conditions d'observation", items=[
            "Diffraction d'autant plus marquée que a est petite devant λ",
            "a de l'ordre de λ, ou plus petite : diffraction importante",
            "a ≫ λ : étalement négligeable, propagation rectiligne",
            "Lumière : bien visible pour a jusqu'à une centaine de λ environ"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "piege_p": dict(type="note", titre="« Petite » par rapport à quoi ?", cles=["comparer"],
                        t="Il faut toujours comparer a à λ, jamais juger une ouverture « petite » dans l'absolu.",
                        etape="Fente de 1 mm : diffraction totale pour un son de 1 m, aucune pour des rayons X de 0,1 nm.", x=170, y=200, w=940),
        "an2": dict(type="anim", nom="diffraction", x=40, y=72, h=624, seg=[[24.2, 34.9]]),
        "pts2": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "L'énergie part dans un cône, limité par deux directions où l'onde s'annule",
            "θ : de la direction incidente à la première extinction",
            "θ est un demi-angle : le cône central va de −θ à +θ"]),
        "f_th": dict(type="formule", titre="Angle caractéristique de diffraction", x=680, y=110, w=560, lignes=[
            dict(f="θ = " + fr("λ", "a"), cadre=True, taille=58),
            dict(f="θ en rad · λ et a dans la même unité (m)", txt=True, taille=26),
            dict(f="λ ↑ ⇒ θ ↑ : le rouge plus que le bleu", taille=28),
            dict(f="a ↓ ⇒ θ ↑ : fente fine, onde très étalée", taille=28)]),
        "ex_th": dict(type="formule", titre="Deux ordres de grandeur", x=150, y=130, w=980, lignes=[
            dict(f="Laser : λ = 650 nm, a = 100 µm", taille=36),
            dict(f="θ = " + fr("650 × 10^-9", "100 × 10^-6") + " = 6,5 × 10^-3 rad ≈ 0,37°", cadre=True, taille=38),
            dict(f="Son : λ = 0,30 m, a = 4,0 m", taille=36),
            dict(f="θ = " + fr("0,30", "4,0") + " = 0,075 rad ≈ 4,3°", cadre=True, taille=38)]),
        "dir": dict(type="def", terme="La direction de l'étalement", cles=["étroite"],
                    t="L'onde s'étale dans la direction où l'ouverture est étroite.",
                    etape="Fente verticale (fine et haute) → figure étalée à l'horizontale.", x=170, y=200, w=940),
        "pieges_th": dict(type="liste", titre="Trois pièges sur θ", items=[
            "θ est un demi-angle : le cône central vaut 2θ",
            "θ = λ/a donne des radians, jamais des degrés",
            "a : largeur de la fente, pas largeur de la tache"], marques=["✗", "✗", "✗"], x=150, y=180, w=980),
    }),

    # ================================================================ IV. laser, fente, écran
    dict(id="ecran", chap="Laser, fente, écran : L = 2λD/a", fond="nuit", humeur="tension",
         retenir="tan θ = (L/2)/D ≈ θ, donc θ = L/(2D) ; avec θ = λ/a : L = 2λD/a. Tout en mètres, θ en radians. L : largeur de la tache centrale.",
         beats=[
        "{an3}{pts3}{pts3.1}{an3.1}Passons à la lumière, au laboratoire. Un laser éclaire une fente fine, de quelques dizaines de micromètres. "
        "Un écran est placé à une distance D, de l'ordre du mètre ou plus.",
        "{pts3.2}Sur l'écran, on n'observe pas un trait de la largeur de la fente. On voit une tache centrale très lumineuse, de largeur L. "
        "{pts3.3}De part et d'autre, des taches secondaires, moins lumineuses et deux fois moins larges. "
        "Et entre elles, des extinctions : aucune lumière.",
        "{-pts3}{pts4}{pts4.1}{an3.2}Reste à relier thêta à ce qu'on mesure sur l'écran : c'est la démonstration demandée dans presque tous les sujets. "
        "{pts4.2}On regarde le triangle formé par la fente, le milieu de la tache centrale, et sa première extinction.",
        "{-pts4}{-an3}{demo}Voici la démonstration, à savoir refaire. {demo.1}Dans ce triangle, le côté adjacent à thêta vaut D. "
        "Le côté opposé vaut la moitié de la tache : L sur deux. Donc tangente de thêta égale L sur deux D.",
        "{demo.2}Thêta est très petit, et exprimé en radians. Donc tangente de thêta est presque égale à thêta. "
        "D'où : thêta égale L sur deux D.",
        "{demo.3}Et pour une fente, thêta égale lambda sur a. {demo.4}On égale les deux expressions : L sur deux D égale lambda sur a. "
        "{demo.5}Soit L égale deux lambda D sur a.",
        "{-demo}{pa_ang}Pourquoi a-t-on le droit d'écrire tangente de thêta égale thêta ? "
        "Pour quelques milliradians, l'écart est inférieur à un millième. Mais seulement en radians !",
        "{-pa_ang}{ex_L}Un calcul complet, avec six cent cinquante nanomètres, cent micromètres, et deux virgule zéro zéro mètres. "
        "{ex_L.1}{ex_L.2}L égale deux fois six virgule cinquante fois dix puissance moins sept, fois deux virgule zéro zéro, "
        "divisé par un virgule zéro zéro fois dix puissance moins quatre. "
        "{ex_L.3}On trouve deux virgule soixante fois dix puissance moins deux mètre. Deux virgule six centimètres.",
        "{ex_L.4}Avec une fente deux fois plus fine, cinquante micromètres, la tache double : cinq virgule deux centimètres. "
        "{ex_L.5}Avec un laser vert de cinq cent trente-deux nanomètres, et la fente de cent micromètres, elle rétrécit : deux virgule un centimètres.",
        "{-ex_L}{prop}Retiens : {prop.1}L est proportionnelle à lambda, {prop.2}proportionnelle à D, sans que thêta change, "
        "{prop.3}et inversement proportionnelle à a.",
        "{-prop}",
    ], vis={
        "an3": dict(type="anim", nom="diffraction", x=40, y=72, h=624, seg=[[36.2, 46.9], [48.2, 58.9]]),
        "pts3": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Laser → fente fine → écran à la distance D",
            "Une tache centrale très lumineuse, de largeur L",
            "Des taches secondaires deux fois moins larges, séparées par des extinctions"]),
        "pts4": dict(type="liste", petit=True, titre="Relier θ à l'écran", x=680, y=150, w=560, items=[
            "La démonstration demandée dans presque tous les sujets",
            "Le triangle : fente, milieu de la tache, première extinction"]),
        "demo": dict(type="formule", titre="Démontrer L = 2λD/a", x=150, y=96, w=980, lignes=[
            dict(f="tan θ = " + fr("L/2", "D") + " = " + fr("L", "2D"), taille=40),
            dict(f="petit angle, en radians : tan θ ≈ θ  ⇒  θ = " + fr("L", "2D"), taille=36),
            dict(f="fente : θ = " + fr("λ", "a"), taille=38),
            dict(f=fr("L", "2D") + " = " + fr("λ", "a"), taille=40),
            dict(f="L = " + fr("2λD", "a"), cadre=True, taille=50, n="L, λ, D, a en mètres")]),
        "pa_ang": dict(type="note", titre="Pourquoi tan θ ≈ θ ?", cles=["radians", "millième"],
                       t="Pour quelques milliradians, l'écart est inférieur à un millième ; à 0,10 rad, il n'est que de 0,3 %. Seulement en radians !",
                       x=170, y=210, w=940),
        "ex_L": dict(type="formule", titre="Exemple · λ = 650 nm, a = 100 µm, D = 2,00 m", x=150, y=110, w=980, lignes=[
            dict(f="L = " + fr("2λD", "a"), taille=38),
            dict(f="L = " + fr("2 × 6,50 × 10^-7 × 2,00", "1,00 × 10^-4"), taille=36),
            dict(f="L = 2,60 × 10^-2 m = 2,6 cm", cadre=True, taille=40),
            dict(f="a = 50 µm : la tache double, L = 5,2 cm", taille=32),
            dict(f="λ = 532 nm (vert), a = 100 µm : L = 2,1 cm", taille=32)]),
        "prop": dict(type="liste", titre="Ce que dit L = 2λD/a", items=[
            "L proportionnelle à λ",
            "L proportionnelle à D (θ, lui, ne dépend pas de D)",
            "L inversement proportionnelle à a"], marques=["λ", "D", "1/a"], x=150, y=180, w=980),
    }),

    # ================================================================ V. fil, lumière blanche, lire L
    dict(id="fil", chap="Un fil, la lumière blanche, bien lire L", fond="aube", humeur="calme",
         retenir="Un fil de diamètre a diffracte comme une fente de largeur a : a = 2λD/L. Lumière blanche : centre blanc, bords irisés. L se lit d'une extinction à l'autre.",
         beats=[
        "{an4}{pts5}{pts5.1}{an4.1}Vérifions. Fente deux fois plus fine : tache deux fois plus large. Laser vert : elle rétrécit. "
        "{pts5.2}Et L en fonction de un sur a donne une droite qui passe par l'origine. On y reviendra.",
        "{-pts5}{pts6}{pts6.1}{an4.2}Maintenant, remplaçons la fente par un fil fin. Surprise : la figure est la même qu'avec une fente de même largeur. "
        "Un fil de diamètre a diffracte comme une fente de largeur a.",
        "{pts6.2}Conséquence très pratique : on peut mesurer le diamètre d'un cheveu avec un laser et une règle ! "
        "Il suffit de retourner la formule : a égale deux lambda D sur L.",
        "{pts6.3}En lumière blanche, chaque couleur se diffracte avec son propre angle. Le centre reste blanc, "
        "mais la tache du rouge est plus large que celle du bleu : les bords sont irisés.",
        "{-pts6}{-an4}{ex_ch}{ex_ch.1}Mesurons un cheveu. Laser à six cent cinquante nanomètres, écran à deux mètres : "
        "la tache centrale mesure trois virgule trois centimètres. "
        "{ex_ch.2}a égale deux fois six virgule cinquante fois dix puissance moins sept, fois deux virgule zéro zéro, "
        "divisé par trois virgule trois fois dix puissance moins deux. "
        "{ex_ch.3}Environ sept virgule neuf fois dix puissance moins cinq mètre : soixante-dix-neuf micromètres.",
        "{ex_ch.4}Une mesure au millimètre donne un diamètre au micromètre près : la diffraction joue le rôle d'un amplificateur.",
        "{-ex_ch}{lireL}Une question de méthode, qui coûte souvent des points. "
        "{lireL.1}L, c'est la largeur de la tache centrale, d'une extinction à l'autre. Pas celle de toute la figure. "
        "{lireL.2}Sur une photographie, on passe par l'échelle, par proportionnalité. "
        "{lireL.3}Et pour gagner en précision, on place l'écran le plus loin possible, puisque L grandit avec D.",
        "{-lireL}{gr_prof}Avec un logiciel de traitement d'image, on trace le profil d'intensité de la figure. "
        "Le voici, pour notre exemple à six cent cinquante nanomètres. {gr_prof.1}Au centre, le maximum ; sur les côtés, les taches secondaires, bien plus faibles.",
        "{gr_prof.2}Les premières extinctions sont à vingt-sept et à cinquante-trois millimètres. "
        "{gr_prof.3}La tache centrale mesure donc vingt-six millimètres : deux virgule six centimètres, comme le calcul.",
        "{-gr_prof}",
    ], vis={
        "an4": dict(type="anim", nom="diffraction", x=40, y=72, h=624, seg=[[60.2, 68.9], [70.2, 79.9]]),
        "pts5": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "a divisée par deux : L double · laser vert : L diminue",
            "L en fonction de 1/a : une droite passant par l'origine"]),
        "pts6": dict(type="liste", petit=True, titre="Un fil, puis la lumière blanche", x=680, y=120, w=560, items=[
            "Un fil de diamètre a diffracte comme une fente de largeur a",
            "Mesurer un cheveu : a = 2λD / L",
            "Lumière blanche : centre blanc, bords irisés, le rouge s'étale plus"]),
        "ex_ch": dict(type="formule", titre="Mesurer un cheveu · λ = 650 nm, D = 2,00 m, L = 3,3 cm", x=150, y=130, w=980, lignes=[
            dict(f="a = " + fr("2λD", "L"), taille=40),
            dict(f="a = " + fr("2 × 6,50 × 10^-7 × 2,00", "3,3 × 10^-2"), taille=36),
            dict(f="a ≈ 7,9 × 10^-5 m ≈ 79 µm", cadre=True, taille=40),
            dict(f="L au millimètre → a au micromètre : un amplificateur", txt=True, pt=True)]),
        "lireL": dict(type="liste", titre="Bien lire L", items=[
            "D'une extinction à l'autre : la tache centrale seule",
            "Sur une photographie : par l'échelle (proportionnalité)",
            "Écran loin (L grandit avec D), règle graduée en millimètres"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "gr_prof": dict(type="graphe", titre="Profil d'intensité · λ = 650 nm, a = 100 µm, D = 2,00 m", x=250, y=110, w=780, h=520,
                        ax=dict(x=[0, 80], y=[0, 1.1], gx=[10, 20, 30, 40, 50, 60, 70], gy=[0.5, 1], lx="position (mm)", ly="intensité"),
                        el=[dict(type="courbe", pts=PROFIL, c="el", dur=2.4),
                            dict(type="points", pts=[[27, 0], [53, 0]], c="ca", lbl="extinctions : 27 et 53 mm", lp=[66, 0.32]),
                            dict(type="droite", pts=[[27, 0.16], [53, 0.16]], c="ca", ep=3, lbl="L = 26 mm", lp=[40, 0.24])]),
    }),

    # ================================================================ VI. exploiter des mesures
    dict(id="mesures", chap="Exploiter des mesures", fond="aube", humeur="calme",
         retenir="L = f(1/a) : droite par l'origine, pente k = 2λD. θ = f(1/a) : pente λ. Étalonnage : a = k / L. Compatible si z = |a − a_réf| / u(a) ≤ 2.",
         beats=[
        "{why}En pratique, on mesure L pour une série de fentes calibrées, et on trace un graphique. Mais lequel ? "
        "{why.1}La relation L égale deux lambda D sur a s'écrit aussi : "
        "L égale k fois un sur a, avec k égale deux lambda D.",
        "{why.2}Donc si on trace L en fonction de un sur a, et pas en fonction de a, on doit obtenir une droite qui passe par l'origine. "
        "Sa pente vaut deux lambda D. {why.3}En fonction de a, on obtiendrait une courbe décroissante, une hyperbole : inexploitable directement.",
        "{-why}{gr_th}Voici une série de mesures classique. Sept fentes, de trente à deux cents micromètres, un écran à un virgule huit mètre. "
        "On calcule thêta, égal à L sur deux D, et on le trace en fonction de un sur a. {gr_th.1}Les points s'alignent.",
        "{gr_th.2}On les modélise par une droite, qui passe pratiquement par l'origine : la relation est vérifiée. "
        "{gr_th.3}Et puisque thêta égale lambda fois un sur a, la pente vaut directement lambda. "
        "Ici, environ six virgule quatre fois dix puissance moins sept mètre : six cent quarante nanomètres.",
        "{-gr_th}{pente}Attention à la lecture. {pente.1}Avec L en ordonnée, la pente vaut deux lambda D ; avec thêta, elle vaut lambda. "
        "{pente.2}Pour la lire, choisis un point de la droite, pas un point de mesure, loin de l'origine. "
        "{pente.3}Et respecte les unités des axes.",
        "{-pente}{etal}Deuxième usage : l'étalonnage. {etal.1}Quand lambda ou D ne sont pas connus précisément, on ne se sert pas de la formule. "
        "On lit la pente k sur la droite d'étalonnage. {etal.2}Puis, pour un objet inconnu, un fil ou un cheveu, on mesure L, et a égale k sur L.",
        "{-etal}{inc}Troisième étape : l'incertitude. Le sujet donne la formule, par exemple celle-ci. "
        "{inc.1}u de a, sur a, égale la racine de : u de L sur L, au carré, plus u de k sur k, au carré. "
        "{inc.2}On arrondit u de a par excès. "
        "{inc.3}Puis on calcule z : l'écart à la valeur de référence, divisé par u de a. Compatible si z est inférieur ou égal à deux.",
        "{-inc}{ex_inc}Un exemple : un brin de brosse à dents. {ex_inc.1}La droite d'étalonnage donne k égale un virgule quatre-vingt-seize fois dix puissance moins six "
        "mètre carré, à zéro virgule zéro trois près. La tache mesure un virgule quatre-vingt-neuf centimètre, à un millimètre près. "
        "{ex_inc.2}a égale k sur L : un virgule zéro quatre fois dix puissance moins quatre mètre. Cent quatre micromètres.",
        "{ex_inc.3}La formule donne u de a égale environ six micromètres. "
        "{ex_inc.4}Le fabricant annonce cent micromètres. z égale quatre sur six : environ zéro virgule sept. "
        "C'est inférieur à deux : la mesure est compatible.",
        "{-ex_inc}{py}Dans les sujets, ce traitement est souvent fait par un petit programme Python, qui trace les points et les modélise par une droite. "
        "{py.1}Pas besoin de l'écrire de mémoire. Mais sache dire ce que fait chaque ligne.",
        "{-py}",
    ], vis={
        "why": dict(type="formule", titre="Quel graphique tracer ?", x=150, y=120, w=980, lignes=[
            dict(f="L = " + fr("2λD", "a") + " = k × " + fr("1", "a") + "   avec   k = 2λD", cadre=True, taille=44),
            dict(f="L = f(1/a) : droite passant par l'origine, de pente k = 2λD (en m^{2})", taille=32),
            dict(f="L = f(a) : hyperbole décroissante, inexploitable directement", taille=30, ko=True)]),
        "gr_th": dict(type="graphe", titre="Série de mesures · D = 1,80 m, θ = L / (2D)", x=300, y=110, w=680, h=520,
                      ax=dict(x=[0, 36], y=[0, 24], gx=[5, 10, 15, 20, 25, 30, 35], gy=[5, 10, 15, 20],
                              lx="1/a (× 10³ m⁻¹)", ly="θ (× 10⁻³ rad)"),
                      el=[dict(type="points", pts=MESURES, c="sa", pas=.3),
                          dict(type="droite", pts=[[0, 0.27], [35, 22.65]], c="el", ep=3),
                          dict(type="texte", x=22, y=7, t="pente ≈ 6,4 × 10^-7 m = λ", c="el")]),
        "pente": dict(type="liste", titre="Lire une pente", items=[
            "L = f(1/a) : pente 2λD · θ = f(1/a) : pente λ. Regarder l'ordonnée !",
            "Un point de la droite, pas un point de mesure, loin de l'origine",
            "Respecter les unités des axes (« × 10³ », mm…)"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "etal": dict(type="liste", titre="L'étalonnage", items=[
            "λ ou D mal connus : on lit la pente k de la droite d'étalonnage",
            "Objet inconnu (fil, cheveu) : on mesure L, puis a = k / L"], marques=["1", "2"], x=150, y=190, w=980),
        "inc": dict(type="formule", titre="Incertitude et compatibilité (formules données)", x=150, y=120, w=980, lignes=[
            dict(f=fr("u(a)", "a") + " = √[ (" + fr("u(L)", "L") + ")^{2} + (" + fr("u(k)", "k") + ")^{2} ]", taille=40),
            dict(f="u(a) arrondie par excès, 1 ou 2 chiffres significatifs", txt=True, pt=True),
            dict(f="z = " + fr("∣a − a_{réf}∣", "u(a)") + "  ≤ 2  : compatible", cadre=True, taille=40)]),
        "ex_inc": dict(type="formule", titre="Exemple · un brin de brosse à dents", x=150, y=100, w=980, lignes=[
            dict(f="k = 1,96 × 10^-6 m^{2} (u = 0,03 × 10^-6) · L = 1,89 cm (u = 0,10 cm)", taille=30),
            dict(f="a = " + fr("k", "L") + " = " + fr("1,96 × 10^-6", "1,89 × 10^-2") + " = 1,04 × 10^-4 m = 104 µm", taille=32),
            dict(f="u(a) = 104 × √[ (" + fr("0,03", "1,96") + ")^{2} + (" + fr("0,10", "1,89") + ")^{2} ] ≈ 6 µm", taille=32),
            dict(f="z = " + fr("∣104 − 100∣", "6") + " ≈ 0,7 ≤ 2 : compatible", cadre=True, ok=True, taille=34)]),
        "py": dict(type="note", titre="Le traitement en Python", cles=["ligne"],
                   t="Le programme calcule 1/a et θ = L/(2D), trace les points et les modélise par une droite (np.polyfit).",
                   etape="Pas à écrire de mémoire : savoir dire ce que fait chaque ligne.", x=170, y=200, w=940),
    }),

    # ================================================================ VII. conséquences de la diffraction
    dict(id="consequences", chap="La diffraction autour de nous", fond="cosmos", humeur="lumiere",
         retenir="Une phrase pour tout justifier : θ = λ/a, l'onde s'étale d'autant plus que λ est grande devant la taille de l'obstacle. Diffraction ≠ réfraction ≠ interférences ≠ dispersion.",
         beats=[
        "{an5}{pts7}{pts7.1}{an5.1}Le programme demande de citer des conséquences concrètes de la diffraction. "
        "Et elles se justifient toutes par la même phrase : thêta égale lambda sur a. "
        "L'onde s'étale d'autant plus que lambda est grande devant la taille de l'ouverture ou de l'obstacle.",
        "{pts7.2}Le son passe une porte, la houle entre dans un port. "
        "{pts7.3}La lumière, elle, ne se diffracte visiblement que par des ouvertures très fines.",
        "{-pts7}{-an5}{cons}Faisons le tour. {cons.1}Entendre sans voir. Derrière un pilier de soixante-dix centimètres, on entend encore les graves. "
        "À deux cents hertz, lambda vaut un virgule sept mètre : ils sont très diffractés. "
        "À mille hertz, lambda ne vaut que trente-quatre centimètres : les aigus passent moins bien.",
        "{cons.2}Les enceintes. Pour que les aigus, de petite longueur d'onde, s'étalent dans la pièce, il faut une petite membrane : le tweeter. "
        "Les graves s'étalent de toute façon : le woofer peut être grand.",
        "{cons.3}La houle s'étale après l'entrée d'un port, et agite les bassins sur le côté. "
        "{cons.4}Les grandes ondes radio, d'un kilomètre de longueur d'onde, contournent les collines.",
        "{cons.5}Les instruments d'optique. L'image d'un point n'est jamais un point, mais une petite tache de diffraction. "
        "Deux détails trop proches se confondent. Un objectif de grand diamètre réduit cette tache.",
        "{cons.6}Les disques optiques. Du CD, en infrarouge, au Blu-ray, en violet, la longueur d'onde diminue : "
        "le spot du laser est plus petit, et on grave plus de données.",
        "{-cons}{hp_c}Hors programme : pour un trou circulaire de diamètre d, la figure est faite d'anneaux, "
        "et le premier anneau sombre est vu sous l'angle un virgule vingt-deux lambda sur d. Si un sujet en a besoin, il la fournit.",
        "{-hp_c}{tab_pr}{pas_d}Et ce qui n'est pas de la diffraction. {pas_d.1}La réfraction : un changement de milieu. "
        "{pas_d.2}Les couleurs d'une bulle de savon, ou les reflets d'un CD : ce sont des interférences. On y arrive. "
        "{pas_d.3}Et l'arc-en-ciel, ou la lumière décomposée par un prisme, comme ici : c'est la dispersion, liée à la réfraction.",
        "{-pas_d}{-tab_pr}{rep}Et une réponse type, à réutiliser. "
        "Le phénomène est la diffraction. Il est d'autant plus marqué que la dimension a de l'obstacle est petite devant la longueur d'onde. "
        "{rep.1}Ici, lambda et a sont du même ordre de grandeur : la diffraction est importante.",
        "{-rep}",
    ], vis={
        "an5": dict(type="anim", nom="diffraction", x=40, y=72, h=624, seg=[[81.2, 91.5]]),
        "pts7": dict(type="liste", petit=True, titre="La même phrase pour tout", x=680, y=120, w=560, items=[
            "θ = λ/a : l'onde s'étale d'autant plus que λ est grande devant a",
            "Le son passe une porte, la houle entre dans un port",
            "La lumière : seulement par des ouvertures très fines"]),
        "cons": dict(type="liste", titre="Des conséquences concrètes", items=[
            "Derrière un pilier : on entend mieux les graves (λ = 1,7 m) que les aigus (0,34 m)",
            "Enceintes : petit tweeter pour étaler les aigus, gros woofer pour les graves",
            "La houle s'étale dans un port et agite les bassins sur le côté",
            "Grandes ondes radio (λ ≈ 1 km) : elles contournent les collines",
            "Instruments d'optique : la tache de diffraction limite les détails visibles",
            "CD (780 nm) → Blu-ray (405 nm) : spot plus petit, plus de données"],
                     marques=["1", "2", "3", "4", "5", "6"], x=130, y=90, w=1020, petit=True),
        "hp_c": dict(type="note", titre="Hors programme · le trou circulaire", cles=["anneaux"], plus=True,
                     t="Trou de diamètre d : une tache centrale entourée d'anneaux ; premier anneau sombre sous l'angle θ = 1,22 λ/d (formule donnée par le sujet).",
                     x=170, y=200, w=940),
        "tab_pr": dict(type="tableau", img="c4-spectre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                       legende="Spectre de la lumière du Soleil à travers un prisme, photo Pittigrilli, CC BY-SA 4.0"),
        "pas_d": dict(type="liste", titre="Ce qui n'est pas de la diffraction", items=[
            "La réfraction : un changement de milieu",
            "Les couleurs d'une bulle, les reflets d'un CD : des interférences",
            "L'arc-en-ciel, le prisme : la dispersion"], marques=["✗", "✗", "✗"], x=150, y=180, w=980),
        "rep": dict(type="def", terme="Une réponse type", cles=["diffraction", "importante"],
                    t="« Le phénomène est la diffraction. Il est d'autant plus marqué que la dimension a de l'obstacle est petite devant λ (θ = λ/a). »",
                    etape="« Ici λ ≈ … et a ≈ … sont du même ordre de grandeur : la diffraction est importante, donc… »", x=170, y=180, w=940),
    }),

    # ================================================================ VIII. superposition et cohérence
    dict(id="superposition", chap="Superposer deux ondes : la cohérence", fond="cosmos", humeur="mystere",
         retenir="Interférences stables : deux sources cohérentes, même fréquence et déphasage constant. En phase : amplitude A₁ + A₂. En opposition de phase : |A₁ − A₂|.",
         beats=[
        "{an6}{pts8}{pts8.1}{an6.1}Deuxième phénomène du chapitre. Dans la cuve à ondes, deux pointes frappent l'eau ensemble, au même rythme. "
        "Chacune crée des ondes circulaires, de même longueur d'onde.",
        "{pts8.2}Là où elles se rencontrent, chacune continue son chemin. Mais en chaque point, les deux perturbations s'ajoutent : "
        "c'est le principe de superposition.",
        "{-pts8}{-an6}{def_i}On appelle {!interférences}interférences ce qui se produit quand deux ondes de même nature se superposent. "
        "{def_i.1}En certains points, elles se renforcent : interférences constructives. "
        "En d'autres, elles s'affaiblissent, voire s'annulent : interférences destructives.",
        "{-def_i}{gr_ph}Pour comprendre, regardons ce qui se passe en un seul point. Deux signaux sinusoïdaux synchrones, c'est-à-dire de même fréquence, y arrivent. "
        "{gr_ph.1}Le premier, en bleu. {gr_ph.2}Le second, en rose. "
        "{gr_ph.3}S'ils sont en phase, leurs maximums arrivent en même temps. La somme est un signal de même période, d'amplitude maximale : "
        "A un plus A deux. Ici, deux A.",
        "{-gr_ph}{gr_op}{gr_op.1}{gr_op.2}Décalons maintenant le second d'une demi-période. Le maximum de l'un tombe sur le minimum de l'autre : "
        "ils sont en opposition de phase. {gr_op.3}La somme est minimale : la valeur absolue de A un moins A deux. "
        "Et si les amplitudes sont égales, comme ici, elle est nulle à chaque instant. C'est le silence.",
        "{-gr_op}{py2}Cette somme, tu dois savoir la représenter en Python. Quelques lignes suffisent. "
        "{py2.1}Des dates sur trois périodes. {py2.2}y un, égale cosinus de deux pi t sur T. "
        "{py2.3}y deux, le même, décalé d'une phase à l'origine phi. "
        "{py2.4}Et on trace la somme : avec phi égale zéro, l'amplitude double ; avec phi égale pi, elle est nulle.",
        "{-py2}{coh}Mais attention : pour voir des interférences stables, il faut une condition. "
        "Les deux sources doivent être cohérentes. {coh.1}Même fréquence, et un déphasage constant au cours du temps.",
        "{-coh}{an7}{pts9}{pts9.1}{an7.1}Regarde ce qui se passe sinon. Si les deux sources ne sont pas accordées, leur décalage change sans arrêt. "
        "Les zones calmes se déplacent tout le temps, et l'œil ne voit qu'un brouillage.",
        "{pts9.2}Deux pointes sur le même vibreur, deux haut-parleurs sur le même générateur : cohérents. "
        "{pts9.3}Deux lampes, ou deux lasers différents : pas cohérents. Voilà pourquoi deux lampes ne font jamais de franges sur un mur. "
        "En optique, on partage donc la lumière d'une seule source.",
        "{-pts9}{-an7}",
    ], vis={
        "an6": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[0.5, 7.9]]),
        "pts8": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Deux sources synchrones : même fréquence, même phase",
            "Là où elles se croisent, les perturbations s'ajoutent : la superposition"]),
        "def_i": dict(type="def", terme="Les interférences", cles=["renforcent", "annulent"],
                      t="Ce qui se produit quand deux ondes de même nature se superposent.",
                      etape="Elles se renforcent (constructives) ou s'affaiblissent, voire s'annulent (destructives).", x=170, y=200, w=940),
        "gr_ph": dict(type="graphe", titre="En phase · y₁ + y₂", x=300, y=110, w=680, h=500,
                      ax=dict(x=[0, 2.1], y=[-2.4, 2.4], gx=[0.5, 1, 1.5, 2], gy=[-2, -1, 1, 2], lx="t / T", ly="signal (en A)"),
                      el=[dict(type="courbe", pts=SIN1, c="el", dur=1.4, lbl="y₁", lp=[0.08, 1.35]),
                          dict(type="courbe", pts=SIN1, c="ca", tir=True, dur=1.4, lbl="y₂", lp=[0.62, -1.4]),
                          dict(type="courbe", pts=SOMME_PH, c="iv", ep=5, dur=1.8, lbl="y₁ + y₂ : amplitude 2A", lp=[1.5, 2.25])]),
        "gr_op": dict(type="graphe", titre="En opposition de phase · y₁ + y₂", x=300, y=110, w=680, h=500,
                      ax=dict(x=[0, 2.1], y=[-2.4, 2.4], gx=[0.5, 1, 1.5, 2], gy=[-2, -1, 1, 2], lx="t / T", ly="signal (en A)"),
                      el=[dict(type="courbe", pts=SIN1, c="el", dur=1.4, lbl="y₁", lp=[0.08, 1.35]),
                          dict(type="courbe", pts=SIN_OP, c="ca", tir=True, dur=1.4, lbl="y₂", lp=[0.08, -1.35]),
                          dict(type="droite", pts=[[0, 0], [2, 0]], c="iv", ep=6, lbl="y₁ + y₂ = 0 : le silence", lp=[1.25, 0.35])]),
        "py2": dict(type="liste", titre="La somme de deux signaux en Python", items=[
            "t = np.linspace(0, 3*T, 600) : trois périodes",
            "y1 = np.cos(2*np.pi*t/T)",
            "y2 = np.cos(2*np.pi*t/T + phi) : décalé de phi",
            "plt.plot(t, y1 + y2) : phi = 0, amplitude double ; phi = π, somme nulle"], marques=["1", "2", "3", "4"], x=150, y=160, w=980),
        "coh": dict(type="def", terme="Sources cohérentes", cles=["fréquence", "constant"],
                    t="Condition pour observer des interférences stables.",
                    etape="Même fréquence (synchrones) et déphasage constant au cours du temps.", x=170, y=200, w=940),
        "an7": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[34.2, 44.9]]),
        "pts9": dict(type="liste", petit=True, titre="Cohérentes ou non ?", x=680, y=120, w=560, items=[
            "Sans déphasage constant : les zones calmes bougent, on ne voit qu'un brouillage",
            "Même vibreur, même générateur : cohérentes",
            "Deux lampes, deux lasers : non. En optique, on partage une seule source"]),
    }),

    # ================================================================ IX. différence de marche
    dict(id="marche", chap="Constructives ou destructives : δ", fond="nuit", humeur="tension",
         retenir="δ = d₂ − d₁. Sources en phase : δ = kλ, constructives ; δ = (k + ½)λ, destructives (k entier relatif). Médiatrice : δ = 0.",
         beats=[
        "{an8}{pts10}{pts10.1}{an8.1}Revenons à la cuve, avec deux sources cohérentes. La surface se partage de façon stable. "
        "Sur certaines lignes, l'eau reste immobile : les deux ondes s'annulent. Entre elles, l'agitation est maximale : elles se renforcent.",
        "{pts10.2}Ces lignes sont des hyperboles, c'est hors programme. Ce qui compte, c'est de prévoir où elles sont.",
        "{-pts10}{pts11}{pts11.1}{an8.2}Prenons un point M. L'onde de S un a parcouru d un. Celle de S deux a parcouru d deux. "
        "On appelle différence de marche : delta égale d deux moins d un.",
        "{pts11.2}L'une a parcouru delta de plus que l'autre. Or une onde retrouve le même état chaque fois qu'elle avance d'une longueur d'onde.",
        "{-pts11}{-an8}{f_cond}D'où les deux conditions, à connaître par cœur, pour deux sources en phase. "
        "{f_cond.1}Si delta égale k lambda, les ondes arrivent en phase, une crête avec une crête : interférences constructives. "
        "{f_cond.2}Si delta égale k plus un demi, fois lambda, une crête arrive avec un creux : interférences destructives. "
        "{f_cond.3}k est un entier relatif.",
        "{-f_cond}{med}Sur la médiatrice du segment S un S deux, les deux distances sont égales. "
        "{med.1}Delta vaut zéro : l'agitation y est maximale.",
        "{-med}{meth}La méthode pour décider en un point. {meth.1}Calculer d un et d deux, souvent avec le théorème de Pythagore. "
        "{meth.2}Calculer delta, puis le rapport delta sur lambda. "
        "{meth.3}Si c'est un entier : constructives. Un entier plus un demi : destructives. Autre chose : un cas intermédiaire.",
        "{-meth}{ex_seg}Un exemple classique. {ex_seg.1}Deux vibreurs synchrones de deux cents hertz, distants de seize centimètres, "
        "à la surface d'un liquide. {ex_seg.2}Les ondes vont à quatre mètres par seconde : lambda vaut deux centimètres.",
        "{ex_seg.3}Un point P du segment, à la distance b du premier vibreur, est à seize moins b du second. "
        "Donc delta égale b, moins seize moins b : deux b moins seize, en centimètres. "
        "{ex_seg.4}Amplitude maximale si deux b moins seize égale deux k. Soit b égale huit plus k. "
        "Un maximum tous les centimètres, c'est-à-dire tous les lambda sur deux.",
        "{ex_seg.5}Il y en a donc quinze entre les deux vibreurs.",
        "{-ex_seg}{pieges_i}Deux pièges. {pieges_i.1}Une seule onde ne fait pas d'interférences. "
        "{pieges_i.2}Et si les sources sont en opposition de phase, les deux conditions s'échangent.",
        "{-pieges_i}",
    ], vis={
        "an8": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[9.2, 21.9], [23.2, 32.9]]),
        "pts10": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Lignes de calme (les ondes s'annulent) et lignes d'agitation, fixes",
            "Ce sont des hyperboles (hors programme)"]),
        "pts11": dict(type="liste", petit=True, titre="La différence de marche", x=680, y=150, w=560, items=[
            "En M : δ = d_2 − d_1",
            "Une onde retrouve le même état tous les λ"]),
        "f_cond": dict(type="formule", titre="Conditions d'interférences (sources en phase)", x=150, y=120, w=980, lignes=[
            dict(f="δ = k λ  :  constructives", cadre=True, taille=46, n="ondes en phase : une crête avec une crête"),
            dict(f="δ = (k + ½) λ  :  destructives", cadre=True, taille=46, n="opposition de phase : une crête avec un creux"),
            dict(f="k entier relatif · δ et λ dans la même unité", txt=True)]),
        "med": dict(type="def", terme="La médiatrice de [S₁S₂]", cles=["médiatrice", "maximale"],
                    t="Sur la médiatrice, d₁ = d₂.",
                    etape="δ = 0 = 0 × λ : interférences constructives, agitation maximale.", x=170, y=200, w=940),
        "meth": dict(type="liste", titre="Décider en un point", items=[
            "Calculer d_1 et d_2 (souvent avec Pythagore)",
            "Calculer δ = d_2 − d_1, puis le rapport δ / λ",
            "Entier : constructives · entier + ½ : destructives · sinon : intermédiaire"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "ex_seg": dict(type="formule", titre="Deux vibreurs à 200 Hz, v = 4,0 m/s, distants de 16 cm", x=150, y=100, w=980, lignes=[
            dict(f="P à b du premier vibreur, à 16 − b du second", txt=True),
            dict(f="λ = " + fr("v", "f") + " = " + fr("4,0", "200") + " = 2,0 × 10^-2 m = 2,0 cm", taille=34),
            dict(f="δ = b − (16 − b) = 2b − 16  (en cm)", taille=36),
            dict(f="2b − 16 = 2k  ⇒  b = 8 + k : un maximum tous les λ/2 = 1 cm", cadre=True, taille=34),
            dict(f="15 maxima entre les vibreurs (b = 1, 2, …, 15 cm)", taille=32)]),
        "pieges_i": dict(type="liste", titre="Deux pièges", items=[
            "Une seule onde ne fait pas d'interférences : il en faut deux, cohérentes",
            "Sources en opposition de phase : les deux conditions s'échangent"], marques=["✗", "✗"], x=150, y=190, w=980),
    }),

    # ================================================================ X. fentes d'Young
    dict(id="young", chap="Les fentes d'Young et l'interfrange", fond="cosmos", humeur="lumiere",
         retenir="δ = ax/D (donnée). Frange brillante : δ = kλ, donc x_k = kλD/a, et i = λD/a. Ici, a est l'écart entre les deux fentes.",
         beats=[
        "{frise}Et la lumière ? {frise.1}À la fin du dix-septième siècle, Huygens la décrit comme une onde. "
        "{frise.2}En mille sept cent quatre, Newton défend des corpuscules. "
        "{frise.3}En mille huit cent un, Thomas Young fait interférer la lumière issue de deux petits trous, éclairés par la même source. "
        "{frise.4}Et vers mille huit cent dix-huit, Fresnel bâtit la théorie ondulatoire de la diffraction. La lumière est bien une onde.",
        "{-frise}{dua}L'expérience reste spectaculaire : même avec une lumière si faible que ses grains, les photons, arrivent un par un, "
        "les impacts finissent par dessiner des franges.",
        "{-dua}{an9}{pts12}{pts12.1}{an9.1}Le dispositif. Un laser éclaire deux fentes séparées de a, de l'ordre du dixième de millimètre. "
        "Chaque fente diffracte la lumière. Derrière elles, les deux faisceaux diffractés se recouvrent. Issus du même laser, ils sont cohérents.",
        "{pts12.2}Sur un écran, à la distance D, on observe des franges brillantes et sombres, régulièrement espacées. "
        "{pts12.3}Au centre, les deux chemins sont égaux : delta égale zéro, la frange centrale est toujours brillante.",
        "{-pts12}{-an9}{f_dm}Pour un point M de l'écran, à l'abscisse x, la différence de chemin optique vaut : {f_dm.1}delta égale a x sur D. "
        "{f_dm.2}Cette relation est donnée par les sujets.",
        "{-f_dm}{demo_i}En revanche, l'interfrange est à savoir établir. "
        "{demo_i.1}Une frange brillante en M, ce sont des interférences constructives : delta égale k lambda. Donc a x sur D égale k lambda.",
        "{demo_i.2}Les franges brillantes sont donc aux abscisses x k égale k lambda D sur a. Au centre, k égale zéro : x égale zéro, frange brillante. "
        "{demo_i.3}Deux franges brillantes voisines, k et k plus un, sont séparées de x k plus un, moins x k : lambda D sur a. "
        "{demo_i.4}Cette distance, c'est l'interfrange : i égale lambda D sur a.",
        "{-demo_i}{an10}{pts13}{pts13.1}{an10.1}Ce qui la fait varier. Rapproche les fentes : les franges s'écartent. "
        "{pts13.2}Prends un laser bleu : elles se resserrent. "
        "{pts13.3}L'interfrange est proportionnelle à lambda et à D, et inversement proportionnelle à a.",
        "{-pts13}{-an10}{ex_i}Mesurons une longueur d'onde. Fentes à zéro virgule vingt millimètre, écran à deux virgule cinquante mètres : "
        "trois interfranges mesurent vingt virgule zéro millimètres. {ex_i.1}Donc i vaut six virgule soixante-sept millimètres.",
        "{ex_i.2}Et lambda égale i a sur D. {ex_i.3}On trouve cinq virgule trois fois dix puissance moins sept mètre : cinq cent trente nanomètres. Un laser vert.",
        "{-ex_i}{pieges_y}Trois pièges. {pieges_y.1}Un : on mesure plusieurs interfranges, puis on divise, pour être plus précis. "
        "{pieges_y.2}Deux : six franges brillantes consécutives, c'est cinq intervalles, pas six. "
        "{pieges_y.3}Trois : en diffraction, a est la largeur d'une fente ; chez Young, c'est l'écart entre les deux fentes. "
        "Certains sujets écrivent b pour l'une des deux : lis bien l'énoncé.",
        "{-pieges_y}",
    ], vis={
        "frise": dict(type="frise", items=[
            dict(d=1690, nom="Huygens", q="la lumière, une onde"), dict(d=1704, nom="Newton", q="des corpuscules"),
            dict(d=1801, nom="Young", q="interférences de la lumière"), dict(d=1818, nom="Fresnel", q="théorie de la diffraction")]),
        "dua": dict(type="illu", nom="dualite", x=200, y=100, w=880, h=520),
        "an9": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[46.2, 58.9]]),
        "pts12": dict(type="liste", petit=True, titre="Les fentes d'Young", x=680, y=120, w=560, items=[
            "Deux fentes séparées de a, éclairées par le même laser : sources cohérentes",
            "Sur l'écran : franges brillantes et sombres, régulièrement espacées",
            "Au centre : δ = 0, frange toujours brillante"]),
        "f_dm": dict(type="formule", titre="Différence de chemin optique (relation donnée)", x=150, y=170, w=980, lignes=[
            dict(f="δ = " + fr("a × x", "D"), cadre=True, taille=56, n="a : écart entre les fentes · x : abscisse de M · D ≫ a et x"),
            dict(f="donnée par les sujets : pas à retrouver", txt=True)]),
        "demo_i": dict(type="formule", titre="Établir l'interfrange (à connaître)", x=150, y=110, w=980, lignes=[
            dict(f="brillante en M : δ = kλ  ⇒  " + fr("a x", "D") + " = kλ", taille=40),
            dict(f="x_k = " + fr("kλD", "a") + "  (k = 0 : frange centrale brillante)", taille=38),
            dict(f="x_{k+1} − x_k = " + fr("λD", "a"), taille=40),
            dict(f="i = " + fr("λD", "a"), cadre=True, taille=54, n="i, λ, D, a en mètres")]),
        "an10": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[60.2, 69.3]]),
        "pts13": dict(type="liste", petit=True, titre="Ce qui fait varier i", x=680, y=120, w=560, items=[
            "Fentes plus proches (a ↓) : les franges s'écartent",
            "Laser bleu (λ ↓) : les franges se resserrent",
            "i ∝ λ · i ∝ D · i ∝ 1/a"]),
        "ex_i": dict(type="formule", titre="Mesurer λ · a = 0,20 mm, D = 2,50 m, 3 i = 20,0 mm", x=150, y=120, w=980, lignes=[
            dict(f="i = " + fr("20,0", "3") + " = 6,67 mm", taille=38),
            dict(f="λ = " + fr("i × a", "D") + " = " + fr("6,67 × 10^-3 × 0,20 × 10^-3", "2,50"), taille=34),
            dict(f="λ = 5,3 × 10^-7 m = 530 nm : un laser vert", cadre=True, taille=38)]),
        "pieges_y": dict(type="liste", titre="Trois pièges", items=[
            "Mesurer plusieurs interfranges, puis diviser",
            "6 franges brillantes consécutives = 5 intervalles",
            "Diffraction : a = largeur d'une fente · Young : a = écart entre les fentes"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ XI. interférences et diffraction ensemble
    dict(id="ensemble", chap="Interférences et diffraction ensemble", fond="aube", humeur="calme",
         retenir="Vraies fentes d'Young : des franges d'interfrange λD/a dans la tache de diffraction de largeur 2λD/ℓ. Lumière blanche : frange centrale blanche, franges irisées.",
         beats=[
        "{gr_y}Avec de vraies fentes, les deux phénomènes se voient sur la même figure. Chaque fente a une largeur, qu'on note l. "
        "Chaque fente diffracte, et les deux faisceaux diffractés interfèrent. {gr_y.1}Voici le profil d'intensité sur l'écran.",
        "{gr_y.2}Les pics fins, tous de même largeur et régulièrement espacés : ce sont les franges d'interférences. "
        "Leur écart, c'est l'interfrange, lambda D sur a. Ici, deux virgule six millimètres.",
        "{gr_y.3}Et l'enveloppe, plus large : c'est la figure de diffraction d'une seule fente. "
        "{gr_y.4}Sa tache centrale mesure deux lambda D sur l : vingt-six millimètres. Elle contient une dizaine d'interfranges.",
        "{-gr_y}{cmp}{cmp.g}Comment les distinguer ? En diffraction seule, la tache centrale fait le double des autres. "
        "{cmp.d}En interférences, les franges ont toutes la même largeur, régulièrement espacées.",
        "{-cmp}{an11}{pts14}{pts14.1}{an11.1}Et en lumière blanche ? Chaque couleur produit ses franges, avec sa propre interfrange. "
        "Au centre, delta égale zéro pour toutes : elles sont toutes constructives, et la frange centrale est blanche.",
        "{pts14.2}De part et d'autre, les franges des différentes couleurs se décalent. On voit quelques franges irisées, puis un mélange blanchâtre. "
        "{pts14.3}C'est pourquoi on mesure une interfrange avec un laser, pas avec une lampe.",
        "{-pts14}{-an11}{hp_hf}Pour aller plus loin, hors programme : pour Huygens et Fresnel, chaque point d'une ouverture est une petite source. "
        "La diffraction, ce sont alors les interférences d'une infinité de sources : au fond, le même phénomène.",
        "{-hp_hf}",
    ], vis={
        "gr_y": dict(type="graphe", titre="Fentes d'Young · λ = 650 nm, D = 2,00 m, a = 0,50 mm, ℓ = 0,10 mm", x=250, y=110, w=780, h=520,
                     ax=dict(x=[0, 60], y=[0, 1.15], gx=[10, 20, 30, 40, 50], gy=[0.5, 1], lx="position (mm)", ly="intensité"),
                     el=[dict(type="courbe", pts=YOUNG, c="el", ep=2.6, dur=2.8),
                         dict(type="texte", x=46, y=0.82, t="pics fins : i = λD/a = 2,6 mm", c="el"),
                         dict(type="courbe", pts=ENVEL, c="ca", tir=True, ep=3, dur=1.8),
                         dict(type="droite", pts=[[17, 1.08], [43, 1.08]], c="ca", ep=3, lbl="enveloppe : 2λD/ℓ = 26 mm", lp=[30, 0.98])]),
        "cmp": dict(type="cols", g="Diffraction (une fente)", gq="tache centrale double des autres · L = 2λD/ℓ",
                    d="Interférences (deux fentes)", dq="franges de même largeur, régulières · i = λD/a", vs="≠"),
        "an11": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[70.6, 78.9]]),
        "pts14": dict(type="liste", petit=True, titre="En lumière blanche", x=680, y=120, w=560, items=[
            "Au centre, δ = 0 pour toutes les couleurs : frange centrale blanche",
            "Plus loin : quelques franges irisées, puis un mélange blanchâtre",
            "On mesure i avec un laser, pas avec une lampe"]),
        "hp_hf": dict(type="note", titre="Hors programme · le même phénomène ?", cles=["sources", "infinité"], plus=True,
                      t="Pour Huygens et Fresnel, chaque point d'une ouverture est une petite source : la diffraction, ce sont les interférences d'une infinité de sources.",
                      x=170, y=200, w=940),
    }),

    # ================================================================ XII. interférences dans la vie courante
    dict(id="vie", chap="Des interférences dans la vie courante", fond="cosmos", humeur="lumiere",
         retenir="Casque anti-bruit : le même son en opposition de phase. Enceinte près d'un mur : δ = 2D. Irisations : bulles, CD, plumes. Mesure de très petites distances.",
         beats=[
        "{an12}{pts15}{pts15.1}{an12.1}Des interférences, il y en a partout, voulues ou subies. "
        "{pts15.2}Le casque à réduction de bruit. Un micro capte le bruit ambiant. Le casque émet le même son, en opposition de phase. "
        "Dans l'oreille, les deux ondes interfèrent de façon destructive : le bruit s'atténue. Surtout les sons graves et réguliers.",
        "{-pts15}{-an12}{mur}L'enceinte posée près d'un mur. {mur.1}L'onde réfléchie interfère avec l'onde directe. "
        "À la distance D du mur, l'onde réfléchie a fait un aller-retour de plus : delta égale deux D. "
        "{mur.2}Là où deux D égale k plus un demi, fois lambda, le son s'éteint. {mur.3}Un rideau, qui absorbe l'onde réfléchie, règle le problème.",
        "{-mur}{iris}{iris.1}Les irisations. Les couleurs d'une bulle de savon, d'une flaque d'essence, d'un CD, des ailes de certains papillons, "
        "des plumes de certains oiseaux. Elles viennent d'interférences entre ondes lumineuses réfléchies par des structures très fines, de l'ordre de lambda. "
        "Selon l'épaisseur et l'angle de vue, chaque couleur est renforcée ou éteinte. Voilà la réponse à notre énigme de la bulle.",
        "{iris.2}Mesurer des distances minuscules : l'interfrange obtenue en éclairant l'écran d'un téléphone révèle l'écart entre deux pixels. "
        "{iris.3}Et même le wifi : à quelques centimètres près, les ondes réfléchies par les murs rendent le signal bon ou mauvais.",
        "{-iris}{rep_i}Et la réponse type à rédiger. Les deux ondes sont cohérentes : même fréquence, déphasage constant. "
        "{rep_i.1}En ce point, la différence de marche vaut k plus un demi, fois lambda. "
        "Les ondes arrivent en opposition de phase : les interférences sont destructives.",
        "{-rep_i}",
    ], vis={
        "an12": dict(type="anim", nom="interferences", x=40, y=72, h=624, seg=[[80.2, 89.5]]),
        "pts15": dict(type="liste", petit=True, titre="Voulues ou subies", x=680, y=150, w=560, items=[
            "Des interférences partout autour de nous",
            "Casque anti-bruit : le même son en opposition de phase → destructives"]),
        "mur": dict(type="liste", titre="L'enceinte près d'un mur", items=[
            "Onde directe + onde réfléchie : à la distance D du mur, δ = 2D",
            "2D = (k + ½)λ : le son s'éteint ; pour les aigus, des « trous » rapprochés",
            "Un rideau absorbe l'onde réfléchie : plus de problème"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "iris": dict(type="liste", titre="Encore des interférences", items=[
            "Irisations : bulles de savon, essence, CD, ailes de papillons, plumes",
            "Mesurer l'écart entre deux pixels · interféromètres (hors programme)",
            "Wifi : onde directe et ondes réfléchies, bon ou mauvais signal à quelques cm près"],
                     marques=["1", "2", "3"], x=150, y=170, w=980),
        "rep_i": dict(type="def", terme="Une réponse type", cles=["cohérentes", "destructives"],
                      t="« Les deux ondes sont cohérentes (même fréquence, déphasage constant). »",
                      etape="« Ici δ = … = (k + ½)λ : opposition de phase, les interférences sont destructives, donc… »", x=170, y=190, w=940),
    }),

    # ================================================================ XIII. exercice 1 (simple)
    # θ = λ/a = 532e-9 / 70e-6 = 7,6e-3 rad ; × 180/π = 0,435° ≈ 0,44°
    # L = 2θD = 2 × 7,6e-3 × 1,50 = 2,28e-2 m ≈ 2,3 cm
    # cheveu : a = 2λD/L = 2 × 532e-9 × 1,50 / 2,8e-2 = 1,596e-6 / 2,8e-2 = 5,70e-5 m = 57 µm
    # rouge : L ∝ λ, L = 2 × 633e-9 × 1,50 / 70e-6 = 2,71e-2 m ≈ 2,7 cm (= 2,28 × 633/532), plus large
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. Un laser vert, de longueur d'onde cinq cent trente-deux nanomètres, "
        "éclaire une fente de soixante-dix micromètres. L'écran est à un virgule cinquante mètre.",
        "Quatre questions : l'angle caractéristique, en radians puis en degrés ; la largeur de la tache centrale ; "
        "le diamètre d'un cheveu qui donne une tache de deux virgule huit centimètres ; et enfin, ce qui change avec un laser rouge.",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche les quatre questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Question un : thêta égale lambda sur a. "
        "Cinq cent trente-deux fois dix puissance moins neuf, divisé par soixante-dix fois dix puissance moins six. "
        "{s11.2}On trouve sept virgule six fois dix puissance moins trois radian. "
        "{s11.3}En degrés, on multiplie par cent quatre-vingts sur pi : environ zéro virgule quarante-quatre degré.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux : L égale deux lambda D sur a, c'est-à-dire deux thêta D. "
        "{s12.2}Deux fois sept virgule six fois dix puissance moins trois, fois un virgule cinquante. "
        "{s12.3}Deux virgule trois fois dix puissance moins deux mètre : deux virgule trois centimètres.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois. Un cheveu diffracte comme une fente de même largeur. Donc a égale deux lambda D sur L. "
        "{s13.2}Deux fois cinq cent trente-deux fois dix puissance moins neuf, fois un virgule cinquante, divisé par deux virgule huit fois dix puissance moins deux. "
        "{s13.3}Cinq virgule sept fois dix puissance moins cinq mètre : cinquante-sept micromètres. Un cheveu plutôt fin.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre. L est proportionnelle à lambda. "
        "Six cent trente-trois nanomètres, c'est plus que cinq cent trente-deux : la tache s'élargit. "
        "{s14.2}Deux virgule vingt-huit centimètres, fois six cent trente-trois sur cinq cent trente-deux : environ deux virgule sept centimètres. "
        "Le rouge est plus diffracté que le vert.",
        "{-s14}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="Un laser vert et une fente", src="Exercice inventé pour la vidéo",
                    enonce=["Un laser vert de longueur d'onde λ = 532 nm éclaire une fente de largeur a = 70 µm. "
                            "Un écran est placé à D = 1,50 m de la fente."],
                    donnees=["λ = 532 nm", "a = 70 µm", "D = 1,50 m"],
                    questions=["Calculer l'angle caractéristique de diffraction θ, en radians puis en degrés.",
                               "Calculer la largeur L de la tache centrale.",
                               "On remplace la fente par un cheveu : la tache centrale mesure 2,8 cm. Quel est son diamètre ?",
                               "Avec un laser rouge (633 nm) et la même fente, la tache est-elle plus large ou plus étroite ? Combien mesure-t-elle ?"]),
        "pa1": dict(type="pause", t="θ en radians et en degrés, la tache centrale, le cheveu, puis le laser rouge."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="Un laser vert et une fente",
                     donnees=["λ = 532 nm", "a = 70 µm", "D = 1,50 m"],
                     questions=["θ ?", "L ?", "Cheveu : a pour L = 2,8 cm ?", "Laser rouge (633 nm) ?"]),
        "s11": dict(type="formule", titre="1 · L'angle caractéristique", x=540, y=150, w=700, lignes=[
            dict(f="θ = " + fr("λ", "a") + " = " + fr("532 × 10^-9", "70 × 10^-6"), taille=38),
            dict(f="θ = 7,6 × 10^-3 rad", cadre=True, taille=40),
            dict(f="7,6 × 10^-3 × " + fr("180", "π") + " ≈ 0,44°", taille=34)]),
        "s12": dict(type="formule", titre="2 · La tache centrale", x=540, y=150, w=700, lignes=[
            dict(f="L = " + fr("2λD", "a") + " = 2θD", taille=38),
            dict(f="L = 2 × 7,6 × 10^-3 × 1,50", taille=36),
            dict(f="L ≈ 2,3 × 10^-2 m = 2,3 cm", cadre=True, taille=38)]),
        "s13": dict(type="formule", titre="3 · Le cheveu", x=540, y=150, w=700, lignes=[
            dict(f="fil ≡ fente : a = " + fr("2λD", "L"), taille=36),
            dict(f="a = " + fr("2 × 532 × 10^-9 × 1,50", "2,8 × 10^-2"), taille=34),
            dict(f="a ≈ 5,7 × 10^-5 m = 57 µm", cadre=True, taille=38)]),
        "s14": dict(type="formule", titre="4 · Le laser rouge", x=540, y=150, w=700, lignes=[
            dict(f="L ∝ λ : 633 nm > 532 nm, la tache s'élargit", taille=32),
            dict(f="L = 2,28 cm × " + fr("633", "532") + " ≈ 2,7 cm", cadre=True, ok=True, taille=36)]),
    }),

    # ================================================================ XIV. exercice 2 (difficile)
    # λ = v/f = 340/1700 = 0,200 m
    # M à 1,60 m devant S1, S1S2 = 1,20 m (triangle rectangle en S1) : d1 = 1,60 m, d2 = √(1,60² + 1,20²) = 2,00 m
    # δ = d2 − d1 = 0,40 m ; δ/λ = 2,0 → constructives
    # N : d1 = 2,30 m, d2 = 2,60 m : δ = 0,30 m ; δ/λ = 1,5 = 1 + ½ → destructives
    # minimum en M : δ = (k + ½)λ → λ = 0,40/(k + ½) ; λ le plus grand pour k = 0 : λ = 0,80 m → f = 340/0,80 = 425 Hz
    # (k = 1 : λ = 0,267 m, f = 1 275 Hz ; k = 2 : f = 2 125 Hz)
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile : des interférences sonores. Deux haut-parleurs, branchés sur le même générateur, "
        "émettent en phase un son de mille sept cents hertz. Ils sont distants de un virgule vingt mètre.",
        "Un micro est placé en M, à un virgule soixante mètre devant le premier. "
        "On cherche la nature des interférences en M, puis en un point N. "
        "Et enfin, la plus basse fréquence pour laquelle le micro, en M, capte un minimum.",
        "{-ex2}{pa2}La dernière question demande un vrai raisonnement. Mets sur pause, et cherche.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un : même générateur, donc même fréquence et déphasage constant. "
        "Les sources sont cohérentes.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux : lambda égale v sur f, trois cent quarante sur mille sept cents. "
        "{s22.2}Zéro virgule deux cents mètre.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois. d un vaut un virgule soixante mètre. "
        "{s23.2}Le triangle est rectangle en S un. Par Pythagore, d deux égale la racine de un virgule soixante au carré, "
        "plus un virgule vingt au carré. Deux virgule zéro zéro mètres. "
        "{s23.3}Delta vaut donc zéro virgule quarante mètre. Et delta sur lambda égale deux : un entier. "
        "{s23.4}Les interférences sont constructives : le micro capte un son fort.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre. En N, delta égale deux virgule soixante moins deux virgule trente : zéro virgule trente mètre. "
        "{s24.2}Delta sur lambda égale un virgule cinq : un plus un demi. {s24.3}Les interférences sont destructives : en N, le son est très faible.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq, la plus subtile. En M, delta reste zéro virgule quarante mètre : il ne dépend que de la géométrie. "
        "Pour un minimum, il faut delta égale k plus un demi, fois lambda. "
        "{s25.2}Donc lambda égale zéro virgule quarante, divisé par k plus un demi. "
        "{s25.3}La plus basse fréquence, c'est la plus grande longueur d'onde : k égale zéro. Lambda vaut alors deux delta : zéro virgule quatre-vingts mètre.",
        "{s25.4}Et f égale v sur lambda : trois cent quarante sur zéro virgule quatre-vingts. Quatre cent vingt-cinq hertz.",
        "{-s25}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=60, titre="Deux haut-parleurs et un micro", src="Exercice inventé pour la vidéo",
                    enonce=["Deux haut-parleurs S₁ et S₂, branchés sur le même générateur, émettent en phase un son de fréquence f = 1 700 Hz. "
                            "Ils sont distants de S₁S₂ = 1,20 m. Un micro est placé en M, à 1,60 m de S₁, sur la perpendiculaire à (S₁S₂) passant par S₁."],
                    donnees=["v = 340 m·s^-1", "f = 1 700 Hz", "S_1S_2 = 1,20 m", "S_1M = 1,60 m"],
                    questions=["Pourquoi les deux sources sont-elles cohérentes ?", "Calculer la longueur d'onde λ.",
                               "Calculer d₁ = S₁M, d₂ = S₂M et δ = d₂ − d₁. Nature des interférences en M ?",
                               "En N, d₁ = 2,30 m et d₂ = 2,60 m. Nature des interférences en N ?",
                               "Quelle est la plus basse fréquence pour laquelle le micro, en M, capte un minimum ?"]),
        "pa2": dict(type="pause", t="Cohérence, λ, la différence de marche en M puis en N, et la fréquence qui éteint le son en M."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Deux haut-parleurs et un micro",
                     donnees=["f = 1 700 Hz", "v = 340 m/s", "S_1S_2 = 1,20 m", "S_1M = 1,60 m"],
                     questions=["Cohérentes ?", "λ ?", "En M ?", "En N ?", "f la plus basse pour un minimum en M ?"]),
        "s21": dict(type="formule", titre="1 · Des sources cohérentes", x=540, y=170, w=700, lignes=[
            dict(f="même générateur : même fréquence, déphasage constant (nul)", txt=True, cadre=True, taille=32)]),
        "s22": dict(type="formule", titre="2 · La longueur d'onde", x=540, y=170, w=700, lignes=[
            dict(f="λ = " + fr("v", "f") + " = " + fr("340", "1 700"), taille=40),
            dict(f="λ = 0,200 m = 20,0 cm", cadre=True, taille=40)]),
        "s23": dict(type="formule", titre="3 · Au point M", x=540, y=110, w=700, lignes=[
            dict(f="d_1 = S_1M = 1,60 m", taille=34),
            dict(f="d_2 = √(1,60^{2} + 1,20^{2}) = 2,00 m", taille=34),
            dict(f="δ = 0,40 m · " + fr("δ", "λ") + " = " + fr("0,40", "0,200") + " = 2,0", taille=34),
            dict(f="entier : constructives, son fort", cadre=True, ok=True, taille=34)]),
        "s24": dict(type="formule", titre="4 · Au point N", x=540, y=150, w=700, lignes=[
            dict(f="δ = 2,60 − 2,30 = 0,30 m", taille=36),
            dict(f=fr("δ", "λ") + " = " + fr("0,30", "0,200") + " = 1,5 = 1 + ½", taille=36),
            dict(f="destructives : son très faible", cadre=True, ko=True, taille=36)]),
        "s25": dict(type="formule", titre="5 · Éteindre le son en M", x=540, y=110, w=700, lignes=[
            dict(f="minimum : δ = (k + ½)λ, avec δ = 0,40 m fixé", taille=32),
            dict(f="λ = " + fr("0,40", "k + ½"), taille=36),
            dict(f="f la plus basse ⇔ λ la plus grande : k = 0, λ = 2δ = 0,80 m", taille=30),
            dict(f="f = " + fr("340", "0,80") + " = 425 Hz", cadre=True, taille=40)]),
    }),

    # ================================================================ XV. exercice 3 (type bac)
    # Partie A : D = 2,00 m ; L = 2λD × (1/a) = k × (1/a), k = 2λD
    # droite d'étalonnage (moindres carrés par l'origine) : pente 2,557 mm par 10³ m⁻¹ ; point lu sur la droite : 1/a = 20 × 10³ m⁻¹,
    # L ≈ 51 mm → k = 51e-3 / 20e3 = 2,55e-6 m² → λ = k/(2D) = 2,55e-6 / 4,00 = 6,4e-7 m = 640 nm (6,38e-7 ; régression : 6,39e-7)
    # Partie B : 10 i = 25,5 mm → i = 2,55 mm ; a = λD/i = 640e-9 × 2,00 / 2,55e-3 = 5,02e-4 m = 0,502 mm
    # u(i) = 0,5/10 = 0,05 mm ; u(a)/a = √[(10/640)² + (0,01/2,00)² + (0,05/2,55)²] = √(2,44e-4 + 2,5e-5 + 3,84e-4) = 0,0256
    # u(a) = 0,502 × 0,0256 = 0,0128 mm → 0,013 mm (par excès) ; z = |0,502 − 0,500| / 0,013 = 0,15 ≤ 2 : compatible
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac, en deux parties. Partie A : on mesure la tache centrale d'un laser à travers cinq fentes calibrées, "
        "pour trouver sa longueur d'onde. "
        "Partie B : ce même laser éclaire deux fentes d'Young, et dix interfranges mesurent vingt-cinq virgule cinq millimètres.",
        "{-ex3}{ex3b}Cinq questions : le choix du graphique, la longueur d'onde, la démonstration de l'interfrange, "
        "l'écart entre les fentes, et son incertitude, à comparer à la valeur du fabricant.",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}{s31.1}Question un. L égale deux lambda D sur a, c'est-à-dire L égale k fois un sur a, avec k égale deux lambda D. "
        "{s31.2}Lambda et D sont fixes : L est proportionnelle à un sur a. Le graphique L en fonction de un sur a doit être une droite passant par l'origine, "
        "de pente deux lambda D.",
        "{-s31}{gr_ex3}{gr_ex3.1}Voici les cinq points. {gr_ex3.2}Ils s'alignent sur une droite qui passe par l'origine.",
        "{-gr_ex3}{ex3c.q2}{gr_ex3b}{gr_ex3b.1}Question deux. On lit la pente sur la droite, pas sur un point de mesure. "
        "{gr_ex3b.2}Au point d'abscisse vingt fois dix puissance trois mètre puissance moins un, on lit L égale cinquante et un millimètres.",
        "{-gr_ex3b}{s32}{s32.1}La pente k vaut donc cinquante et un fois dix puissance moins trois, divisé par vingt fois dix puissance trois. "
        "Deux virgule cinquante-cinq fois dix puissance moins six mètre carré. "
        "{s32.2}Et lambda égale k sur deux D : deux virgule cinquante-cinq fois dix puissance moins six, divisé par quatre virgule zéro zéro. "
        "{s32.3}Six virgule quatre fois dix puissance moins sept mètre : six cent quarante nanomètres. Un laser rouge.",
        "{-s32}{ex3c.q3}{s33}Question trois : la démonstration de tout à l'heure, à rédiger en entier. "
        "{s33.1}Delta égale a x sur D. {s33.2}Frange brillante : delta égale k lambda, donc x k égale k lambda D sur a. "
        "{s33.3}Deux franges voisines sont séparées de i égale lambda D sur a.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Question quatre. Dix interfranges pour vingt-cinq virgule cinq millimètres : "
        "i égale deux virgule cinquante-cinq millimètres. {s34.2}Donc a égale lambda D sur i. "
        "{s34.3}a vaut cinq virgule zéro deux fois dix puissance moins quatre mètre : zéro virgule cinq cent deux millimètre.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq. Dix interfranges à zéro virgule cinq millimètre près, c'est i à zéro virgule zéro cinq millimètre près. "
        "{s35.2}On applique la formule donnée, avec u de lambda et u de D : u de a sur a vaut environ deux virgule six pour cent.",
        "{s35.3}u de a vaut environ zéro virgule zéro treize millimètre, arrondi par excès. "
        "{s35.4}Enfin, z égale zéro virgule zéro zéro deux, divisé par zéro virgule zéro treize : environ zéro virgule quinze. "
        "C'est bien inférieur à deux : la mesure est compatible avec la valeur du fabricant.",
        "{s35.5}Et le regard critique : l'incertitude vient surtout de la lecture des franges. D'où l'intérêt d'en mesurer dix plutôt qu'une.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Du laser aux fentes d'Young", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Partie A. Un laser éclaire successivement cinq fentes calibrées ; l'écran est à D = 2,00 m. On mesure la tache centrale L.",
                            "Partie B. Le même laser éclaire deux fentes d'Young ; écran à D = 2,00 m. Dix interfranges mesurent 25,5 mm (à 0,5 mm près). "
                            "Le fabricant annonce un écart de 0,500 mm entre les fentes."],
                    donnees=["a (µm) : 40 · 50 · 80 · 100 · 125", "L (mm) : 64 · 51 · 32 · 26 · 20",
                             "u(λ) = 10 nm · u(D) = 1 cm",
                             "u(a)/a = √[(u(λ)/λ)^{2} + (u(D)/D)^{2} + (u(i)/i)^{2}]", "δ = ax/D"]),
        "ex3b": dict(type="exo", niveau="bac", titre="Du laser aux fentes d'Young · questions",
                     questions=["Justifier le tracé de L en fonction de 1/a ; exprimer la pente k.",
                                "Lire la pente de la droite et en déduire λ.",
                                "Établir l'expression de l'interfrange i à partir de δ = ax/D.",
                                "Calculer l'écart a entre les deux fentes.",
                                "Évaluer u(a) et conclure sur la valeur annoncée par le fabricant."]),
        "pa3": dict(type="pause", t="La droite L = f(1/a), λ, l'interfrange, l'écart entre les fentes, son incertitude et z."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Du laser aux fentes d'Young",
                     donnees=["D = 2,00 m", "10 i = 25,5 mm (± 0,5 mm)", "fabricant : 0,500 mm"],
                     questions=["Pourquoi L = f(1/a) ?", "Pente, puis λ ?", "Établir i ?", "a ?", "u(a), z ?"]),
        "s31": dict(type="formule", titre="1 · Pourquoi L en fonction de 1/a", x=540, y=150, w=700, lignes=[
            dict(f="L = " + fr("2λD", "a") + " = k × " + fr("1", "a") + " , k = 2λD", taille=36),
            dict(f="droite passant par l'origine, de pente k = 2λD", cadre=True, taille=32)]),
        "gr_ex3": dict(type="graphe", titre="Partie A · L en fonction de 1/a", x=560, y=110, w=660, h=520,
                       ax=dict(x=[0, 28], y=[0, 75], gx=[5, 10, 15, 20, 25], gy=[10, 20, 30, 40, 50, 60, 70],
                               lx="1/a (× 10³ m⁻¹)", ly="L (mm)"),
                       el=[dict(type="points", pts=EX3, c="sa", pas=.3),
                           dict(type="droite", pts=[[0, 0], [27, round(27 * EX3_K, 1)]], c="el", ep=3)]),
        "gr_ex3b": dict(type="graphe", titre="Lire la pente sur la droite", x=560, y=110, w=660, h=520,
                        ax=dict(x=[0, 28], y=[0, 75], gx=[5, 10, 15, 20, 25], gy=[10, 20, 30, 40, 50, 60, 70],
                                lx="1/a (× 10³ m⁻¹)", ly="L (mm)"),
                        el=[dict(type="droite", pts=[[0, 0], [27, round(27 * EX3_K, 1)]], c="el", ep=3, dur=.8),
                            dict(type="point", x=20, y=51, c="ca", proj=True, lbl="(20 × 10³ m⁻¹ ; 51 mm)", lp=[12, 64])]),
        "s32": dict(type="formule", titre="2 · La pente, puis λ", x=540, y=140, w=700, lignes=[
            dict(f="k = " + fr("51 × 10^-3", "20 × 10^3") + " = 2,55 × 10^-6 m^{2}", taille=34),
            dict(f="λ = " + fr("k", "2D") + " = " + fr("2,55 × 10^-6", "4,00"), taille=34),
            dict(f="λ ≈ 6,4 × 10^-7 m = 640 nm (rouge)", cadre=True, taille=36)]),
        "s33": dict(type="formule", titre="3 · Établir i = λD/a", x=540, y=140, w=700, lignes=[
            dict(f="δ = " + fr("a x", "D") + " (donnée)", taille=36),
            dict(f="brillante : δ = kλ  ⇒  x_k = " + fr("kλD", "a"), taille=34),
            dict(f="i = x_{k+1} − x_k = " + fr("λD", "a"), cadre=True, taille=38)]),
        "s34": dict(type="formule", titre="4 · L'écart entre les fentes", x=540, y=140, w=700, lignes=[
            dict(f="i = " + fr("25,5", "10") + " = 2,55 mm", taille=36),
            dict(f="a = " + fr("λD", "i") + " = " + fr("640 × 10^-9 × 2,00", "2,55 × 10^-3"), taille=34),
            dict(f="a = 5,02 × 10^-4 m = 0,502 mm", cadre=True, taille=36)]),
        "s35": dict(type="formule", titre="5 · Incertitude et compatibilité", x=540, y=100, w=700, lignes=[
            dict(f="u(i) = " + fr("0,5", "10") + " = 0,05 mm", taille=30),
            dict(f=fr("u(a)", "a") + " = √[(" + fr("10", "640") + ")^{2} + (" + fr("0,01", "2,00") + ")^{2} + (" + fr("0,05", "2,55") + ")^{2}] ≈ 2,6 %", taille=28),
            dict(f="u(a) ≈ 0,013 mm (par excès)", taille=32),
            dict(f="z = " + fr("∣0,502 − 0,500∣", "0,013") + " ≈ 0,15 ≤ 2 : compatible", cadre=True, ok=True, taille=32),
            dict(f="Regard critique : la lecture des franges domine ; mesurer 10 i plutôt qu'une.", txt=True)]),
    }),

    # ================================================================ XVI. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, deux comportements qui signent une onde. "
        "{carte.1}La diffraction : elle est marquée quand a n'est pas grande devant lambda, et thêta égale lambda sur a, en radians. "
        "{carte.2}Sur l'écran : tangente de thêta égale L sur deux D, presque égale à thêta, donc L égale deux lambda D sur a. "
        "{carte.3}Les interférences : deux sources cohérentes ; delta égale k lambda, constructives ; k plus un demi, fois lambda, destructives. "
        "{carte.4}Et les fentes d'Young : delta égale a x sur D, donnée, et l'interfrange i égale lambda D sur a.",
        "{-carte}{pieges}Les pièges qui coûtent des points. {pieges.1}Tout en mètres. {pieges.2}Thêta en radians. "
        "{pieges.3}Deux lambda D sur a, la tache ; lambda D sur a, l'interfrange. "
        "{pieges.4}Thêta est un demi-angle. "
        "{pieges.5}a : largeur d'une fente, ou écart entre deux fentes. "
        "{pieges.6}Et n franges brillantes font n moins un interfranges.",
        "{-pieges}{bac}Ce que le bac peut te demander, à cocher. "
        "{bac.1}Caractériser la diffraction. {bac.2}Exploiter thêta égale lambda sur a. "
        "{bac.3}Établir la largeur de la tache. {bac.4}Exploiter une droite, avec une incertitude. "
        "{bac.5}Les conditions d'interférences. {bac.6}Établir l'interfrange. "
        "{bac.7}La somme de deux signaux en Python. {bac.8}Et les conséquences concrètes.",
        "Si tu sais faire ces huit choses, tu as tout le bagage du chapitre. Les questions du quiz t'attendent juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="DEUX SIGNATURES DES ONDES", branches=[
            dict(t="La diffraction", items=["a pas trop grande devant λ", "θ = λ/a (rad)", "même λ, seule la direction change"]),
            dict(t="Sur l'écran", items=["tan θ = L/(2D) ≈ θ", "L = 2λD/a", "L = f(1/a) : pente 2λD"]),
            dict(t="Les interférences", items=["sources cohérentes", "δ = kλ : constructives", "δ = (k + ½)λ : destructives"]),
            dict(t="Fentes d'Young", items=["δ = ax/D (donnée)", "i = λD/a", "a : écart entre les fentes"])]),
        "pieges": dict(type="liste", titre="Les pièges", items=[
            "Tout en mètres : nm × 10^-9, µm × 10^-6, mm × 10^-3",
            "θ = λ/a et θ = L/(2D) en radians",
            "2λD/a : tache de diffraction · λD/a : interfrange",
            "θ est un demi-angle : L = 2 × (L/2)",
            "a : largeur d'une fente (diffraction) ≠ écart entre fentes (Young)",
            "n franges brillantes = n − 1 interfranges"], marques=["✗"] * 6, x=150, y=100, w=980, petit=True),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Caractériser la diffraction, en citer des conséquences", "Exploiter θ = λ/a",
            "Établir L = 2λD/a", "Exploiter L = f(1/a), avec une incertitude",
            "Conditions d'interférences : δ = kλ, δ = (k + ½)λ", "Établir i = λD/a",
            "Somme de deux signaux sinusoïdaux en Python", "Citer des conséquences des interférences"],
                    marques=["✓"] * 8, x=170, y=80, w=940, petit=True),
    }),
]

QUIZ = [
    dict(q="La diffraction d'une onde par une ouverture de largeur a est d'autant plus marquée que…",
         r=["a est grande devant λ", "a est petite devant λ", "l'onde est intense"], ok=1,
         ex="θ = λ/a grandit quand a diminue : il faut toujours comparer a à λ.", voir="cond"),
    dict(q="Après une ouverture, l'onde diffractée a…",
         r=["une longueur d'onde plus petite", "la même longueur d'onde et la même fréquence", "une célérité plus faible"], ok=1,
         ex="Seule la direction de propagation change : f, v et λ restent les mêmes.", voir="def_d"),
    dict(q="λ = 532 nm et a = 0,10 mm. L'angle caractéristique vaut…", r=["5,3 × 10⁻³ rad", "5,3 rad", "0,30 rad"], ok=0,
         ex="θ = λ/a = 532 × 10⁻⁹ / 0,10 × 10⁻³ = 5,3 × 10⁻³ rad (soit 0,30°, mais la formule donne des radians).", voir="f_th"),
    dict(q="Dans la démonstration de L = 2λD/a, tan θ vaut…", r=["L / D", "L / (2D)", "2L / D"], ok=1,
         ex="Le côté opposé à θ est la moitié de la tache centrale : tan θ = (L/2)/D.", voir="demo"),
    dict(q="On recule l'écran de 1,0 m à 2,0 m. La tache centrale…",
         r=["double de largeur, θ ne change pas", "double de largeur, θ double", "ne change pas"], ok=0,
         ex="θ = λ/a ne dépend pas de D ; L = 2θD est proportionnelle à D.", voir="prop"),
    dict(q="On trace θ = f(1/a). La pente de la droite obtenue vaut…", r=["λ", "2λD", "D"], ok=0,
         ex="θ = λ × (1/a) : la pente vaut λ. Avec L en ordonnée, elle vaudrait 2λD.", voir="pente"),
    dict(q="Deux ondes cohérentes ont…", r=["la même amplitude", "la même fréquence et un déphasage constant", "la même fréquence seulement"], ok=1,
         ex="Même fréquence ne suffit pas : le décalage entre les sources doit rester constant.", voir="coh"),
    dict(q="Sources en phase, λ = 2,0 cm ; en M, δ = 5,0 cm. Les interférences y sont…", r=["constructives", "destructives", "intermédiaires"], ok=1,
         ex="δ/λ = 2,5 = 2 + ½ : les ondes arrivent en opposition de phase.", voir="f_cond"),
    dict(q="L'interfrange des fentes d'Young s'écrit…", r=["i = λa/D", "i = λD/a", "i = 2λD/a"], ok=1,
         ex="i = λD/a ; 2λD/a est la largeur de la tache centrale de diffraction d'une fente.", voir="demo_i"),
    dict(q="Sur l'écran, 6 franges brillantes consécutives occupent 15 mm. L'interfrange vaut…", r=["2,5 mm", "3,0 mm", "15 mm"], ok=1,
         ex="6 franges, 5 intervalles : i = 15/5 = 3,0 mm.", voir="pieges_y"),
    dict(q="Un casque à réduction de bruit émet le son ambiant…", r=["en phase", "en opposition de phase", "à une fréquence double"], ok=1,
         ex="Dans l'oreille, les deux ondes interfèrent de façon destructive.", voir="pts15"),
]

CREDITS = [
    "Photo : spectre de la lumière du Soleil à travers un prisme, Pittigrilli, CC BY-SA 4.0 (Wikimedia Commons).",
    "Animations, schémas et graphiques : faits pour la vidéo. Les trois exercices sont inventés pour la vidéo.",
]
