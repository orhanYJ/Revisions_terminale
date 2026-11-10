"""Physique-chimie, chapitre 5 : « La lunette astronomique » — le cours en vidéo.

Même modèle que pc_ch4.py (voir son en-tête). Contenu : le chapitre 5 du site (pc/index.html : rappels de Première sur
les lentilles, l'œil et les petits angles, fiches 1 à 8, TP 7), rien au-delà ; Galilée et Kepler, le diamètre de
l'objectif, le cercle oculaire et le télescope sont dits « hors programme », comme sur le site.
Animation du site rejouée : pc/anim/lunette.html (7 étapes, 84 s). Illustrations du moteur : lentille, angle.
Les trois exercices sont inventés pour la vidéo (valeurs recalculées ci-dessous, en commentaire de chaque exercice).
"""

SITE = "pc"
CODE = "ch5"
NOTION = "La lunette astronomique"
NUM = 5
TITRE = "La lunette astronomique"
SUIVANT = "Les autres chapitres de physique-chimie"
PRONONCIATION = {"Kepler": "Képlère", "Yerkes": "Yerkiz", "Galilée": "Galilée", "Copernic": "Copernic"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]".replace(" ", " ")


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="cosmos", humeur="mystere", carton=False, beats=[
        "{tab_lune}{q1}Regarde la Lune. Elle est à près de quatre cent mille kilomètres. Impossible de s'en approcher. "
        "Et pourtant, avec deux simples lentilles dans un tube, on voit ses cratères, ses montagnes, ses mers.",
        "{-q1}{q2}Alors, une lunette rapproche-t-elle la Lune ?",
        ("Non. Elle ne rapproche rien.", {"rate": "-8%"}),
        "{-q2}{q3}Elle fait quelque chose de plus subtil : elle agrandit l'angle sous lequel on voit l'astre. "
        "Tout le chapitre tient dans cette idée, et dans une formule très simple qu'on va établir ensemble.",
        "{-q3}{-tab_lune}{plan}Voici le chemin. {plan.1}D'abord les rappels indispensables : la lentille convergente, la construction d'une image, "
        "la relation de conjugaison, l'œil et les petits angles. {plan.2}Puis le cœur du chapitre : l'objectif, l'image intermédiaire, l'oculaire, "
        "et le réglage afocal. {plan.3}Ensuite le grossissement, sa démonstration, et les lunettes du commerce. "
        "{plan.4}Puis la lunette montée sur un banc optique, et les limites du modèle. "
        "{plan.5}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_lune": dict(type="tableau", img="c5-lune", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.5, .5, .42],
                         legende="La pleine Lune au-dessus de l'atmosphère, photographiée depuis l'espace, NASA (domaine public)"),
        "q1": dict(type="question", t="La Lune est à 384 400 km… et on voit ses cratères."),
        "q2": dict(type="question", t="Une lunette rapproche-t-elle la Lune ?"),
        "q3": dict(type="question", t="Non : elle agrandit l'angle sous lequel on la voit."),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les rappels : lentille, image, conjugaison, œil, petits angles",
            "L'objectif, l'image intermédiaire, l'oculaire, le réglage afocal",
            "Le grossissement, sa démonstration, les lunettes du commerce",
            "La lunette sur le banc optique, les limites du modèle",
            "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 5", t="La lunette astronomique",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. la lentille convergente
    dict(id="lentille", chap="La lentille convergente", fond="nuit", humeur="lumiere",
         retenir="Rayon parallèle à l'axe → passe par F′. Rayon par O → non dévié. Rayon par F → ressort parallèle. C = 1/f′, f′ en mètres.",
         beats=[
        "{def_l}Une lunette, ce n'est que deux lentilles convergentes l'une derrière l'autre. Alors commençons par une seule. "
        "{def_l.1}Une lentille convergente est plus épaisse au centre que sur les bords. Elle fait converger, par réfraction, les rayons qui la traversent.",
        "{-def_l}{vocab}Quatre mots à connaître. {vocab.1}L'axe optique : la droite perpendiculaire à la lentille qui passe par son centre. "
        "{vocab.2}Le centre optique O : le point de la lentille situé sur l'axe. "
        "{vocab.3}Le foyer image F prime : le point de l'axe où convergent les rayons qui arrivent parallèles à l'axe. "
        "{vocab.4}Et le foyer objet F, symétrique de F prime par rapport à O.",
        "{-vocab}{f_C}{f_C.1}La distance focale f prime, c'est la distance de O à F prime. Et sa vergence C vaut un sur f prime. "
        "{f_C.2}Attention : la vergence s'exprime en dioptries, seulement si f prime est en mètres. "
        "Une focale de cinq centimètres donne une vergence de un sur zéro virgule zéro cinq : vingt dioptries. Pas zéro virgule deux.",
        "{f_C.3}Sur une lunette de banc optique classique, l'objectif a une vergence de deux dioptries, donc une focale de cinquante centimètres. "
        "L'oculaire a vingt dioptries : cinq centimètres. Plus la vergence est grande, plus la focale est courte.",
        "{-f_C}{constr}Pour construire l'image d'un objet, on utilise trois rayons particuliers, issus du point B. "
        "{constr.1}Un rayon qui arrive parallèle à l'axe ressort en passant par le foyer image F prime. "
        "{constr.2}Un rayon qui passe par le centre O n'est pas dévié. "
        "{constr.3}Un rayon qui passe par le foyer objet F ressort parallèle à l'axe.",
        "{constr.4}L'image B prime est à leur intersection. Deux rayons suffisent. Et A prime est sur l'axe, à la verticale de B prime. "
        "Ici, l'objet est au-delà de F : l'image est réelle, renversée, et on pourrait la recueillir sur un écran.",
        "Attention : ces trois rayons ne sont pas les seuls à traverser la lentille. Tous les rayons issus de B passent par B prime. "
        "Ce sont simplement ceux qu'on sait tracer sans calcul.",
        "{-constr}",
    ], vis={
        "def_l": dict(type="def", terme="Lentille mince convergente", cles=["épaisse", "converger"],
                      t="Plus épaisse au centre que sur les bords, elle fait converger les rayons par réfraction.", x=170, y=200, w=940),
        "vocab": dict(type="liste", titre="Quatre mots", items=[
            "L'axe optique : perpendiculaire à la lentille, par son centre", "Le centre optique O",
            "Le foyer image F′ : là où convergent les rayons parallèles à l'axe", "Le foyer objet F : symétrique de F′ par rapport à O"],
                      marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "f_C": dict(type="formule", titre="Distance focale et vergence", x=150, y=130, w=980, lignes=[
            dict(f="f′ = ‾{OF′}   ;   C = " + fr("1", "f′"), cadre=True, n="f′ en mètres · C en dioptries (δ), 1 δ = 1 m^-1"),
            dict(f="f′ = 5,0 cm = 0,050 m  ⇒  C = " + fr("1", "0,050") + " = 20 δ  (et non 0,2 δ)", taille=36),
            dict(f="Banc optique : objectif +2,0 δ → f′_1 = 50 cm · oculaire +20 δ → f′_2 = 5,0 cm", taille=32)]),
        "constr": dict(type="illu", nom="lentille", x=90, y=110, w=1100, h=520, oa=-2.5, f=130),
    }),

    # ================================================================ II. conjugaison
    dict(id="conjugaison", chap="La relation de conjugaison", fond="nuit", humeur="calme",
         retenir="1/‾{OA′} − 1/‾{OA} = 1/f′ ; γ = ‾{OA′}/‾{OA}. Objet à l'infini → image dans le plan focal image. Objet en F → image à l'infini.",
         beats=[
        "{alg}Pour calculer au lieu de dessiner, on oriente l'axe dans le sens de la lumière, de gauche à droite. "
        "{alg.1}Une mesure algébrique, O A barre, est positive si A est à droite de O, négative s'il est à gauche. "
        "Un objet placé avant la lentille a donc toujours O A négatif.",
        "{-alg}{f_conj}{f_conj.1}La relation de conjugaison : un sur O A prime, moins un sur O A, égale un sur f prime. "
        "{f_conj.2}Et le grandissement gamma : A prime B prime sur A B, égal à O A prime sur O A. "
        "S'il est négatif, l'image est renversée. S'il dépasse un en valeur absolue, elle est agrandie.",
        "{-f_conj}{ex_conj}Un exemple. Un objet à trente centimètres avant une lentille de dix centimètres. "
        "{ex_conj.1}O A vaut moins trente. {ex_conj.2}Un sur O A prime égale un sur dix, plus un sur moins trente : deux trentièmes. "
        "{ex_conj.3}Donc O A prime égale plus quinze centimètres. {ex_conj.4}Et gamma vaut quinze sur moins trente : moins zéro virgule cinq. "
        "L'image est réelle, renversée, deux fois plus petite.",
        "{-ex_conj}{piege_signe}Le piège classique : oublier le signe moins. Avec O A égal à plus trente, on trouverait une image plus proche que F prime, "
        "ce qui est impossible pour un objet réel. Si ton résultat te paraît étrange, vérifie d'abord ce signe.",
        "{-piege_signe}{limites}Et voici les deux cas limites, les seuls dont la lunette a besoin. "
        "{limites.1}Objet à l'infini : un sur O A tend vers zéro, donc O A prime égale f prime. L'image est dans le plan focal image. "
        "{limites.2}Objet au foyer objet : un sur O A prime égale un sur f prime moins un sur f prime, c'est-à-dire zéro. "
        "L'image est rejetée à l'infini : les rayons ressortent parallèles.",
        "{-limites}",
    ], vis={
        "alg": dict(type="def", terme="Mesure algébrique", cles=["positive", "négative"],
                    t="Sur l'axe orienté dans le sens de la lumière, ‾{OA} est positive si A est à droite de O, négative s'il est à gauche.",
                    etape="Un objet réel, placé avant la lentille, a toujours ‾{OA} < 0.", x=170, y=180, w=940),
        "f_conj": dict(type="formule", titre="Conjugaison et grandissement", x=150, y=150, w=980, lignes=[
            dict(f=fr("1", "‾{OA′}") + " − " + fr("1", "‾{OA}") + " = " + fr("1", "f′") + " = C", cadre=True, taille=50,
                 n="mesures algébriques, toutes dans la même unité"),
            dict(f="γ = " + fr("‾{A′B′}", "‾{AB}") + " = " + fr("‾{OA′}", "‾{OA}"), cadre=True, taille=46,
                 n="γ < 0 : image renversée · |γ| > 1 : image agrandie")]),
        "ex_conj": dict(type="formule", titre="Exemple · objet à 30 cm d'une lentille de 10 cm", x=150, y=120, w=980, lignes=[
            dict(f="‾{OA} = −30 cm  ·  f′ = 10 cm"),
            dict(f=fr("1", "‾{OA′}") + " = " + fr("1", "10") + " + " + fr("1", "−30") + " = " + fr("2", "30")),
            dict(f="‾{OA′} = +15 cm : image réelle, après la lentille", cadre=True),
            dict(f="γ = " + fr("15", "−30") + " = −0,5 : renversée, deux fois plus petite")]),
        "piege_signe": dict(type="note", titre="Le signe moins qu'on oublie", cles=["signe", "impossible"],
                            t="‾{OA} = +30 cm donnerait ‾{OA′} = +7,5 cm, plus près que F′ : impossible pour un objet réel. Vérifie le signe.",
                            x=170, y=210, w=940),
        "limites": dict(type="liste", titre="Les deux cas limites", items=[
            "Objet à l'infini : ‾{OA′} = f′, image dans le plan focal image",
            "Objet au foyer objet (‾{OA} = −f′) : image à l'infini, rayons parallèles"], marques=["∞", "F"], x=150, y=190, w=980),
    }),

    # ================================================================ III. l'œil et les petits angles
    dict(id="oeil", chap="L'œil et les petits angles", fond="cosmos", humeur="calme",
         retenir="L'œil au repos voit net à l'infini. Un objet de taille h à la distance D est vu sous α ≈ h/D, en radians. Pouvoir séparateur ≈ 3 × 10⁻⁴ rad.",
         beats=[
        "{oeil_m}Deuxième rappel : l'œil. En Seconde, on le modélise par un diaphragme, l'iris, une lentille convergente, le cristallin, "
        "et un écran, la rétine. {oeil_m.1}Pour voir net, l'image doit se former sur la rétine.",
        "{oeil_m.2}Au repos, l'œil normal voit net les objets à l'infini. {oeil_m.3}Pour un objet proche, le cristallin se bombe : c'est l'accommodation. "
        "Elle demande un effort, et elle fatigue.",
        "Retiens la conséquence pour la lunette : on veut que l'image finale soit à l'infini, pour l'observer longtemps sans fatigue. "
        "C'est toute la raison d'être du réglage afocal.",
        "{-oeil_m}{ang}Troisième rappel : comment mesurer la taille apparente d'un objet lointain ? Par l'angle sous lequel on le voit. "
        "Un objet de taille h, à la distance D, est vu sous un angle alpha, dont la tangente vaut h sur D.",
        "{ang.2}Et pour un petit angle, exprimé en radians, la tangente est presque égale à l'angle lui-même : alpha vaut à peu près h sur D.",
        "{-ang}{ex_lune}Un exemple que tu retrouveras partout dans ce chapitre : la Lune. {ex_lune.1}Son diamètre : trois mille quatre cent soixante-quatorze kilomètres. "
        "Sa distance : trois cent quatre-vingt-quatre mille quatre cents kilomètres. "
        "{ex_lune.2}Alpha vaut environ neuf virgule zéro fois dix puissance moins trois radian, soit à peu près un demi-degré. "
        "C'est son diamètre apparent.",
        "{-ex_lune}{pieges_a}Deux réflexes. {pieges_a.1}Un : l'approximation tangente de alpha égale alpha n'est vraie qu'en radians. "
        "Vérifie le mode de ta calculatrice avant tout calcul d'angle. Pour convertir des degrés, on multiplie par pi sur cent quatre-vingts. "
        "{pieges_a.2}Deux : l'œil ne distingue deux points que s'ils sont vus sous plus de trois fois dix puissance moins quatre radian environ. "
        "C'est son pouvoir séparateur. Une lunette sert à porter au-dessus de cette limite des détails qui sont en dessous.",
        "{-pieges_a}",
    ], vis={
        "oeil_m": dict(type="liste", titre="Le modèle de l'œil", items=[
            "Iris (diaphragme) · cristallin (lentille) · rétine (écran)", "Au repos, l'œil normal voit net à l'infini",
            "Objet proche : le cristallin se bombe, c'est l'accommodation, qui fatigue"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "ang": dict(type="illu", nom="angle", x=90, y=120, w=1100, h=480),
        "ex_lune": dict(type="formule", titre="La Lune à l'œil nu", x=150, y=170, w=980, lignes=[
            dict(f="h = 3 474 km  ·  D = 384 400 km"),
            dict(f="α ≈ " + fr("3 474", "384 400") + " ≈ 9,0 × 10^-3 rad ≈ 0,52°", cadre=True, n="le diamètre apparent de la Lune")]),
        "pieges_a": dict(type="liste", titre="Deux réflexes", items=[
            "tan α ≈ α seulement en radians : mode radian, ou × π/180",
            "Pouvoir séparateur de l'œil ≈ 3 × 10^-4 rad"], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ IV. objet à l'infini, objectif
    dict(id="infini", chap="L'objectif et l'image intermédiaire", fond="nuit", humeur="lumiere",
         retenir="Un astre envoie des rayons parallèles : l'objectif en forme une image réelle et renversée dans son plan focal image, de taille f′₁ × α.",
         beats=[
        "{an1}{pts1}{pts1.1}{an1.1}Entrons dans la lunette. Un astre est si loin que les rayons issus d'un même point arrivent parallèles entre eux. "
        "Ceux qui viennent du point A situé sur l'axe arrivent parallèles à l'axe : la lentille les fait converger en F prime. "
        "C'est l'objectif, la première lentille, du côté de l'astre : il a une grande focale.",
        "{pts1.2}{an1.2}Un autre point B de l'astre envoie lui aussi des rayons parallèles, mais inclinés d'un angle alpha. "
        "Ils convergent en un point B un, dans le plan focal image, le plan vertical qui passe par F prime.",
        "Une astuce pour le trouver d'un seul trait : parmi ces rayons parallèles, trace celui qui passe par le centre O. "
        "Il n'est pas dévié. Là où il coupe le plan focal image, c'est B un.",
        "{pts1.3}L'objectif fabrique donc une petite image de l'astre, A un B un : l'image intermédiaire. "
        "Elle est réelle, renversée, et située dans le plan focal image de l'objectif.",
        "{-pts1}{f_taille}{f_taille.1}Quelle est sa taille ? Dans le triangle O F prime B un, rectangle, l'angle en O vaut alpha. "
        "Donc tangente de alpha égale A un B un sur f prime un. {f_taille.2}Pour un petit angle : A un B un vaut à peu près f prime un fois alpha.",
        "{f_taille.3}Pour la Lune et un objectif de sept cents millimètres : sept cents fois neuf fois dix puissance moins trois, environ six virgule trois millimètres. "
        "Avec un objectif de deux mille millimètres, elle mesurerait dix-huit millimètres.",
        "{f_taille.4}D'où la première règle de la lunette : plus la focale de l'objectif est longue, plus l'image intermédiaire est grande. "
        "C'est exactement ce qu'on vérifie sur un banc optique, en changeant d'objectif.",
        "{-f_taille}{-an1}",
    ], vis={
        "an1": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[1.2, 11], [11, 22]]),
        "pts1": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Point sur l'axe : rayons parallèles à l'axe, qui convergent en F′_1",
            "Point B hors de l'axe : rayons inclinés de α, qui convergent en B_1",
            "A_1B_1 : image intermédiaire, réelle et renversée, dans le plan focal image"]),
        "f_taille": dict(type="formule", titre="Taille de l'image intermédiaire", x=680, y=110, w=560, lignes=[
            dict(f="tan α = " + fr("A_1B_1", "f′_1"), taille=38),
            dict(f="A_1B_1 ≈ f′_1 × α", cadre=True, taille=40, n="α en radians"),
            dict(f="Lune, f′_1 = 700 mm : 700 × 9,0 × 10^-3 ≈ 6,3 mm", taille=28),
            dict(f="focale plus longue → image plus grande", txt=True, pt=True)]),
    }),

    # ================================================================ V. la lunette afocale
    dict(id="afocale", chap="La lunette afocale", fond="nuit", humeur="lumiere",
         retenir="Lunette afocale : F′₁ = F₂, donc O₁O₂ = f′₁ + f′₂. D'un objet à l'infini, elle donne une image à l'infini : l'œil voit net sans fatigue.",
         beats=[
        "{an2}{pts2}{pts2.1}{an2.1}Deuxième lentille : l'oculaire, du côté de l'œil, avec une petite focale. "
        "On le place de sorte que son foyer objet, qu'on note F deux, soit confondu avec le foyer image de l'objectif, qu'on note F prime un.",
        "{pts2.2}Pourquoi ? L'image intermédiaire est dans le plan focal image de l'objectif. Si F prime un égale F deux, elle est aussi "
        "dans le plan focal objet de l'oculaire. Et on l'a vu : un objet dans le plan focal objet donne une image à l'infini.",
        "{pts2.3}Les rayons ressortent donc parallèles entre eux : l'œil au repos voit net, sans accommoder, et peut observer longtemps sans fatigue.",
        "{-pts2}{def_af}{def_af.1}On dit que la lunette est afocale : d'un objet à l'infini, elle donne une image à l'infini. "
        "Des rayons parallèles à l'entrée ressortent parallèles.",
        "{-def_af}{f_long}{f_long.1}La condition : F prime un égale F deux. {f_long.2}Et la longueur de la lunette : O un O deux égale f prime un plus f prime deux.",
        "{f_long.3}Sur le banc optique : cinquante plus cinq, l'oculaire se place à cinquante-cinq centimètres de l'objectif.",
        "{-f_long}{piege_f}Attention au piège classique du QCM : ce sont le foyer IMAGE de l'objectif et le foyer OBJET de l'oculaire qui coïncident. "
        "Écrire F un égale F prime deux, ou F prime un égale F prime deux, est faux.",
        "{-piege_f}{-an2}{gal}{tab_ye}Un mot d'histoire, hors programme. Galilée tourne sa lunette vers le ciel en mille six cent neuf. "
        "Il découvre les satellites de Jupiter et les montagnes de la Lune. Mais son oculaire était divergent. "
        "C'est Kepler, en mille six cent onze, qui propose l'oculaire convergent : c'est notre modèle. "
        "Et la plus grande lunette du monde, à Yerkes, aux États-Unis, a un objectif d'un mètre de diamètre.",
        "{-gal}{-tab_ye}",
    ], vis={
        "an2": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[22, 35]]),
        "pts2": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "L'oculaire est placé pour que F′_1 = F_2",
            "B_1 est au foyer objet de l'oculaire : les rayons ressortent parallèles",
            "Image finale à l'infini : l'œil voit net sans effort"]),
        "def_af": dict(type="def", terme="Système afocal", cles=["infini", "parallèles"],
                       t="Il donne d'un objet à l'infini une image à l'infini : des rayons parallèles à l'entrée ressortent parallèles.",
                       x=680, y=170, w=560),
        "f_long": dict(type="formule", titre="Lunette afocale", x=680, y=140, w=560, lignes=[
            dict(f="F′_1 = F_2", cadre=True, taille=46),
            dict(f="O_1O_2 = f′_1 + f′_2", cadre=True, taille=42),
            dict(f="Banc optique : 50 + 5,0 = 55 cm", taille=34)]),
        "piege_f": dict(type="note", titre="Ne pas confondre les foyers", cles=["image", "objet"],
                        t="F′₁ = F₂ : foyer image de l'objectif, foyer objet de l'oculaire. Ni F₁ = F′₂, ni F′₁ = F′₂.", x=680, y=200, w=560),
        "gal": dict(type="portrait", annee=1610, img="galilee", nom="Galilée", dates="1564 – 1642",
                    legende="hors programme · tourne une lunette vers le ciel en 1609-1610"),
        "tab_ye": dict(type="tableau", img="c5-yerkes", fond=True, sombre=True, de=[1.0, .6, .4], a=[1.25, .6, .35],
                       legende="La lunette de 40 pouces (102 cm) de l'observatoire Yerkes, 1897 (domaine public)"),
    }),

    # ================================================================ VI. le faisceau émergent
    dict(id="faisceau", chap="Construire le faisceau émergent", fond="nuit", humeur="tension",
         retenir="Méthode : lentilles et foyers ; B₁ par le rayon passant par O₁ ; direction de sortie (B₁O₂) ; rayons émergents parallèles à (B₁O₂). Image renversée.",
         beats=[
        "{meth}C'est le savoir-faire graphique du chapitre, très souvent demandé : tracer le faisceau qui sort de la lunette. "
        "La méthode tient en quatre étapes, toujours les mêmes.",
        "{meth.1}Un : placer les deux lentilles, à la distance f prime un plus f prime deux. Entre les deux, marquer le foyer image de l'objectif, confondu avec le foyer objet de l'oculaire. Puis marquer les deux autres foyers : le foyer objet de l'objectif, avant lui, et le foyer image de l'oculaire, après lui.",
        "{meth.2}Deux : trouver B un. On trace le rayon incident qui passe par O un : il n'est pas dévié, et il coupe le plan focal en B un. "
        "Les autres rayons incidents, parallèles à lui, passent tous par B un après l'objectif.",
        "{meth.3}Trois : trouver la direction de sortie. On trace, en pointillés, la droite qui va de B un à O deux : ce rayon-là n'est pas dévié par l'oculaire.",
        "{meth.4}Quatre : tracer les rayons émergents. Chacun ressort parallèle à cette droite B un O deux, puisque B un est dans le plan focal objet de l'oculaire.",
        "{-meth}{an3}{pts3}{pts3.1}{an3.1}Regarde maintenant ce que cela implique. Les rayons incidents descendent : ils viennent d'un point situé au-dessus de l'axe. "
        "Les rayons émergents, eux, montent. L'œil les reçoit comme s'ils venaient d'un point situé en dessous.",
        "{pts3.2}L'image est donc renversée. Un cratère au nord de la Lune apparaît en bas. En astronomie, ce n'est pas gênant. "
        "Pour un paysage, les jumelles ajoutent des prismes redresseurs.",
        "{-pts3}{-an3}{err}Les erreurs qui coûtent des points sur ce schéma. {err.1}Faire ressortir les rayons convergents ou divergents : "
        "pour une lunette afocale, ils ressortent parallèles entre eux. {err.2}Les faire ressortir parallèles à l'axe : seul le faisceau venant du point sur l'axe fait cela. "
        "{err.3}Oublier les flèches de sens de propagation. {err.4}Et ne pas faire passer les rayons réfractés par l'objectif par B un.",
        "{-err}",
    ], vis={
        "meth": dict(type="liste", titre="La méthode en quatre étapes", items=[
            "Placer L_1, L_2 à f′_1 + f′_2, et les foyers F′_1 = F_2, F_1, F′_2",
            "Trouver B_1 : le rayon par O_1 n'est pas dévié",
            "Direction de sortie : la droite (B_1O_2), en pointillés",
            "Rayons émergents : tous parallèles à (B_1O_2)"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "an3": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[35, 46]]),
        "pts3": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Le rayon le plus haut à l'entrée ressort le plus bas",
            "L'image est renversée : un cratère du haut est vu en bas"]),
        "err": dict(type="liste", titre="Les erreurs qui coûtent des points", items=[
            "Rayons émergents convergents ou divergents : non, parallèles",
            "Rayons émergents parallèles à l'axe : seulement pour le point sur l'axe",
            "Oublier les flèches de sens de propagation",
            "Rayons réfractés par L_1 qui ne passent pas par B_1"], marques=["✗", "✗", "✗", "✗"], x=150, y=150, w=980),
    }),

    # ================================================================ VII. le grossissement
    dict(id="grossissement", chap="Le grossissement", fond="aube", humeur="lumiere",
         retenir="G = α′/α = f′₁/f′₂ (angles en radians, focales dans la même unité). Pour grossir : objectif long, oculaire court.",
         beats=[
        "{an4}{pts4}{pts4.1}{an4.1}Comment mesurer ce que gagne la lunette ? Pas en mètres : l'astre et son image sont à l'infini. "
        "Ce qui change, c'est l'angle. {pts4.2}Alpha : l'angle sous lequel on voit l'astre à l'œil nu. Alpha prime : l'angle sous lequel on le voit dans la lunette.",
        "{-pts4}{f_G}{f_G.1}Le grossissement G est leur rapport : G égale alpha prime sur alpha. Il n'a pas d'unité.",
        "{-f_G}{demo}Il faut savoir établir son expression. Voici la démonstration rédigée, à connaître. "
        "{demo.1}Dans le triangle O un F prime un B un, rectangle en F prime un, l'angle en O un vaut alpha, car le rayon qui passe par O un n'est pas dévié. "
        "Donc tangente de alpha égale A un B un sur f prime un.",
        "{demo.2}Dans le triangle O deux F deux B un, rectangle en F deux, l'angle en O deux vaut alpha prime, car le rayon B un O deux n'est pas dévié, "
        "et tous les rayons émergents lui sont parallèles. Donc tangente de alpha prime égale A un B un sur f prime deux.",
        "{demo.3}Les angles sont petits et en radians : tangente de alpha vaut à peu près alpha, et de même pour alpha prime.",
        "{demo.4}Donc G égale alpha prime sur alpha : A un B un sur f prime deux, multiplié par f prime un sur A un B un. "
        "La taille de l'image intermédiaire se simplifie.",
        "{-demo}{-an4}{f_G2}{f_G2.1}Le résultat, à encadrer : G égale f prime un sur f prime deux. "
        "{f_G2.2}Pour grossir, il faut que l'objectif ait la plus grande focale. Et pour grossir davantage, on prend un objectif plus long, "
        "ou un oculaire plus court. Le diamètre des lentilles n'intervient pas.",
        "{f_G2.3}La lunette du banc optique : cinquante sur cinq, G vaut dix. La Lune, vue à l'œil nu sous neuf fois dix puissance moins trois radian, "
        "est vue dans la lunette sous neuf fois dix puissance moins deux radian, environ cinq degrés. "
        "C'est l'angle sous lequel on verrait une Lune dix fois plus proche.",
        "{-f_G2}{piege_G}Un dernier piège. Sur les schémas des exercices, les angles sont exagérés, huit ou dix degrés. "
        "Là, l'approximation est moins bonne : on trouve tangente de alpha prime égale G fois tangente de alpha, donc un alpha prime un peu plus petit que G fois alpha. "
        "Ne t'inquiète pas d'un petit écart au rapporteur.",
        "{-piege_G}",
    ], vis={
        "an4": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[46, 58]]),
        "pts4": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=140, w=560, items=[
            "On compare des angles, pas des tailles : l'astre et l'image sont à l'infini",
            "α : à l'œil nu · α′ : dans la lunette"]),
        "f_G": dict(type="formule", titre="Définition du grossissement", x=680, y=170, w=560, lignes=[
            dict(f="G = " + fr("α′", "α"), cadre=True, taille=54, n="sans unité · angles en radians")]),
        "demo": dict(type="formule", titre="Établir l'expression de G", x=680, y=96, w=560, lignes=[
            dict(f="O_1F′_1B_1 : tan α = " + fr("A_1B_1", "f′_1"), taille=32),
            dict(f="O_2F_2B_1 : tan α′ = " + fr("A_1B_1", "f′_2"), taille=32),
            dict(f="petits angles : tan α ≈ α, tan α′ ≈ α′", taille=26, txt=True),
            dict(f="G = " + fr("α′", "α") + " = " + fr("A_1B_1", "f′_2") + " × " + fr("f′_1", "A_1B_1"), taille=32)]),
        "f_G2": dict(type="formule", titre="Grossissement d'une lunette afocale", x=150, y=130, w=980, lignes=[
            dict(f="G = " + fr("α′", "α") + " = " + fr("f′_1", "f′_2"), cadre=True, taille=56, n="les deux focales dans la même unité"),
            dict(f="objectif long, oculaire court → G grand · le diamètre n'intervient pas", txt=True, pt=True),
            dict(f="Banc optique : G = " + fr("50", "5,0") + " = 10 · Lune : α′ = 10 × 9,0 × 10^-3 = 9,0 × 10^-2 rad ≈ 5°", taille=30)]),
        "piege_G": dict(type="note", titre="Angles de dessin", cles=["exagérés", "écart"],
                        t="Pour 8° ou 10°, tan α′ = G × tan α : α′ est un peu plus petit que G × α. Un petit écart au rapporteur est normal.",
                        x=170, y=210, w=940),
    }),

    # ================================================================ VIII. lunettes du commerce
    dict(id="commerce", chap="Les lunettes du commerce", fond="cosmos", humeur="calme",
         retenir="« 70/700 » : diamètre puis focale de l'objectif, en mm. Changer d'oculaire, c'est changer de grossissement : G = f′₁/f′₂.",
         beats=[
        "{inscr}Une lunette du commerce porte une inscription comme soixante-dix sur sept cents. {inscr.1}Le premier nombre est le diamètre de l'objectif, "
        "le second sa focale, en millimètres. {inscr.2}Elle est livrée avec plusieurs oculaires, marqués par leur focale : vingt-cinq millimètres, dix millimètres.",
        "{-inscr}{an5}{pts5}{pts5.1}{an5.1}Changer d'oculaire, c'est changer de grossissement. Avec un oculaire plus court, la lunette grossit davantage. "
        "{pts5.2}Avec un objectif plus long, l'image intermédiaire grandit, et le grossissement aussi.",
        "{-pts5}{-an5}{ex_70}{ex_70.1}Pour la soixante-dix sur sept cents : avec l'oculaire de vingt-cinq millimètres, G vaut sept cents sur vingt-cinq, vingt-huit. "
        "{ex_70.2}Avec celui de dix millimètres : soixante-dix.",
        "{-ex_70}{quest}Dans un exercice sur une lunette commerciale, il y a presque toujours ces quatre questions. "
        "{quest.1}Lire les deux focales, et les mettre dans la même unité. {quest.2}Calculer G. "
        "{quest.3}Calculer l'angle à l'œil nu, taille sur distance, en radians, puis alpha prime égale G fois alpha. "
        "{quest.4}Conclure : le détail est visible si alpha prime dépasse le pouvoir séparateur de l'œil.",
        "{-quest}{tab_sat}{ex_sat}Essayons avec les anneaux de Saturne. {ex_sat.1}Saturne est à environ un virgule trois milliard de kilomètres, "
        "et ses anneaux s'étendent sur deux cent soixante-dix mille kilomètres. {ex_sat.2}À l'œil nu : environ deux fois dix puissance moins quatre radian. "
        "C'est sous le pouvoir séparateur : on ne voit qu'un point. "
        "{ex_sat.3}Avec l'oculaire de dix millimètres, G vaut soixante-dix : alpha prime vaut environ un virgule quatre fois dix puissance moins deux radian. Les anneaux apparaissent nettement.",
        "{-ex_sat}{hp_d}Et le diamètre de l'objectif ? Hors programme : il ne change pas le grossissement, mais il fixe la quantité de lumière collectée, "
        "et la finesse des détails. Au-delà d'environ deux fois le diamètre en millimètres, on grossit une image floue.",
        "{-hp_d}{-tab_sat}",
    ], vis={
        "inscr": dict(type="def", terme="Lire une lunette du commerce", cles=["diamètre", "focale"],
                      t="« 70/700 » : diamètre D de l'objectif, puis sa focale f′₁, en millimètres.",
                      etape="Les oculaires sont marqués par leur focale : 25 mm, 10 mm…", x=170, y=190, w=940),
        "an5": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[58, 70]]),
        "pts5": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Oculaire plus court : G plus grand", "Objectif plus long : A_1B_1 et G grandissent"]),
        "ex_70": dict(type="formule", titre="La lunette 70/700", x=150, y=180, w=980, lignes=[
            dict(f="oculaire 25 mm : G = " + fr("700", "25") + " = 28"),
            dict(f="oculaire 10 mm : G = " + fr("700", "10") + " = 70", cadre=True)]),
        "quest": dict(type="liste", titre="Exercice type · lunette du commerce", items=[
            "Lire f′_1 et f′_2, même unité", "Calculer G = f′_1 / f′_2",
            "α ≈ taille / distance (rad), puis α′ = G × α", "Conclure : visible si α′ > 3 × 10^-4 rad"],
                      marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "tab_sat": dict(type="tableau", img="c5-saturne", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .5],
                        legende="Saturne vue par la sonde Cassini, 2004, NASA/JPL/Space Science Institute (domaine public)"),
        "ex_sat": dict(type="formule", titre="Les anneaux de Saturne avec la 70/700", x=150, y=150, w=980, lignes=[
            dict(f="D ≈ 1,3 × 10^9 km  ·  anneaux ≈ 2,7 × 10^5 km", taille=36),
            dict(f="α ≈ " + fr("2,7 × 10^5", "1,3 × 10^9") + " ≈ 2 × 10^-4 rad < 3 × 10^-4 rad : un point", taille=36, ko=True),
            dict(f="α′ = 70 × 2 × 10^-4 ≈ 1,4 × 10^-2 rad : les anneaux sont visibles", cadre=True, taille=36)]),
        "hp_d": dict(type="note", titre="Hors programme", cles=["lumière", "floue"], plus=True,
                     t="Le diamètre ne change pas G : il fixe la lumière collectée et la finesse des détails (grossissement utile ≈ 2 × D en mm).",
                     x=170, y=210, w=940),
    }),

    # ================================================================ IX. TP, réglage, limites
    dict(id="banc", chap="Sur le banc optique, et les limites", fond="nuit", humeur="calme",
         retenir="Banc optique : objet au foyer de L₀ (à l'infini), image intermédiaire sur un écran à f′₁, oculaire à O₁O₂ = f′₁ + f′₂. Limites : diffraction, aberrations.",
         beats=[
        "{tp}Au laboratoire, on fabrique une lunette sur un banc optique, et c'est au programme. {tp.1}D'abord, simuler un objet à l'infini : "
        "on place une diapositive éclairée au foyer objet d'une lentille L zéro, de trois dioptries, donc à trente-trois virgule trois centimètres avant elle. "
        "Les rayons ressortent parallèles, comme ceux d'un astre.",
        "{tp.2}Ensuite, visualiser l'image intermédiaire : on place l'objectif, puis un écran. L'image nette se forme à f prime un après l'objectif, "
        "quelle que soit la distance entre L zéro et l'objectif. C'est la preuve qu'elle est dans le plan focal image.",
        "{tp.3}Puis régler la lunette : on retire l'écran, et on place l'oculaire à f prime deux après la position de l'image. "
        "{tp.4}Enfin, mesurer le grossissement : on mesure A un B un, on en déduit alpha et alpha prime, et on compare leur rapport à f prime un sur f prime deux.",
        "{-tp}{an6}{pts6}{pts6.1}{an6.1}Et si l'oculaire est mal placé ? S'il est trop loin, l'image intermédiaire est au-delà de son foyer objet : "
        "les rayons ressortent convergents. S'il est trop près, ils ressortent divergents. Dans les deux cas, l'œil au repos voit flou. "
        "{pts6.2}On règle la lunette en déplaçant l'oculaire, jusqu'à ce que les rayons ressortent parallèles.",
        "{-pts6}{-an6}{hp_c}Sur le banc, on rencontre aussi le cercle oculaire, hors programme : c'est l'image du bord de l'objectif par l'oculaire. "
        "Toute la lumière sortie de la lunette passe par ce petit disque, juste après F prime deux. C'est là qu'on place la pupille.",
        "{-hp_c}{lim}Pour finir, le modèle des deux lentilles minces a ses limites, que le programme demande de connaître. "
        "{lim.1}Il n'explique pas pourquoi deux points très proches restent confondus même avec un grand grossissement : c'est la diffraction par l'objectif. "
        "{lim.2}Il ne rend pas compte des déformations de l'image : une vraie lentille n'est parfaite que près de l'axe. Ce sont les aberrations géométriques. "
        "{lim.3}Et il n'explique pas les irisations colorées sur les bords : l'indice du verre dépend de la longueur d'onde. C'est l'aberration chromatique.",
        "Les grands télescopes remplacent d'ailleurs l'objectif par un miroir, qui ne disperse pas les couleurs. Hors programme, là encore.",
        "{-lim}",
    ], vis={
        "tp": dict(type="liste", titre="La lunette sur le banc optique", items=[
            "Objet au foyer de L_0 (+3,00 δ, à 33,3 cm) : un objet « à l'infini »",
            "Écran : l'image intermédiaire nette à f′_1 après l'objectif",
            "Oculaire à f′_2 après l'image : O_1O_2 = f′_1 + f′_2",
            "Mesurer A_1B_1, en déduire α, α′, et comparer à f′_1 / f′_2"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "an6": dict(type="anim", nom="lunette", x=40, y=72, h=624, seg=[[70, 84]]),
        "pts6": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Oculaire trop loin : rayons convergents · trop près : divergents",
            "On règle en déplaçant l'oculaire jusqu'au réglage afocal"]),
        "hp_c": dict(type="note", titre="Hors programme · le cercle oculaire", cles=["pupille"], plus=True,
                     t="Image du bord de l'objectif par l'oculaire, juste après F′₂ : toute la lumière y passe, on y place la pupille.",
                     x=170, y=210, w=940),
        "lim": dict(type="liste", titre="Les limites du modèle", items=[
            "Diffraction : deux points très proches restent confondus",
            "Aberrations géométriques : une vraie lentille n'est parfaite que près de l'axe",
            "Aberration chromatique : l'indice dépend de la longueur d'onde"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ X. exercice 1 (simple)
    # C1 = 1,25 δ → f′1 = 0,800 m ; f′2 = 20 mm ; O1O2 = 820 mm ; G = 800/20 = 40
    # Jupiter : 1,40e5 km / 6,3e8 km = 2,22e-4 rad < 3e-4 ; α′ = 40 × 2,22e-4 = 8,9e-3 rad (comme la Lune à l'œil nu)
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. Un club d'astronomie possède une lunette dont l'objectif a une vergence "
        "de un virgule vingt-cinq dioptrie, et un oculaire de vingt millimètres de focale.",
        "Quatre questions : la focale de l'objectif ; la longueur de la lunette réglée en afocal ; son grossissement ; "
        "et enfin, Jupiter, vue à l'œil nu comme un simple point, apparaît-elle comme un disque dans cette lunette ?",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche les quatre questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Question un : f prime un égale un sur C un, un sur un virgule vingt-cinq. "
        "{s11.2}Zéro virgule huit cents mètre, soit huit cents millimètres.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux : la lunette est afocale si F prime un est confondu avec F deux. "
        "{s12.2}Alors O un O deux égale f prime un plus f prime deux : huit cents plus vingt, huit cent vingt millimètres. Quatre-vingt-deux centimètres.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : G égale f prime un sur f prime deux, huit cents sur vingt. {s13.2}G vaut quarante. "
        "Attention, les deux focales dans la même unité : huit cents millimètres, pas zéro virgule huit.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre. Jupiter mesure environ cent quarante mille kilomètres, "
        "et elle est à environ six cent trente millions de kilomètres de nous à l'opposition. {s14.2}À l'œil nu, alpha vaut environ deux virgule deux fois dix puissance moins quatre radian : "
        "c'est sous le pouvoir séparateur, on voit un point. "
        "{s14.3}Dans la lunette, alpha prime égale quarante fois deux virgule deux fois dix puissance moins quatre : environ huit virgule neuf fois dix puissance moins trois radian. "
        "Jupiter apparaît comme un disque, à peu près aussi grand que la Lune à l'œil nu !",
        "{-s14}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="La lunette du club", src="Exercice inventé pour la vidéo (données sur Jupiter arrondies)",
                    enonce=["Une lunette a un objectif de vergence C₁ = +1,25 δ et un oculaire de focale f′₂ = 20 mm."],
                    donnees=["Jupiter : diamètre ≈ 1,40 × 10^5 km", "distance ≈ 6,3 × 10^8 km", "pouvoir séparateur de l'œil ≈ 3 × 10^-4 rad"],
                    questions=["Calculer la focale f′₁ de l'objectif.", "Quelle est la longueur O₁O₂ de la lunette réglée en afocal ?",
                               "Calculer son grossissement G.", "Jupiter apparaît-elle comme un disque à l'œil nu ? Et dans la lunette ?"]),
        "pa1": dict(type="pause", t="Focale de l'objectif, longueur, grossissement, Jupiter à l'œil nu et dans la lunette."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="La lunette du club",
                     donnees=["C_1 = +1,25 δ", "f′_2 = 20 mm", "Jupiter : 1,40 × 10^5 km à 6,3 × 10^8 km"],
                     questions=["f′_1 ?", "O_1O_2 ?", "G ?", "Jupiter : point ou disque ?"]),
        "s11": dict(type="formule", titre="1 · La focale de l'objectif", x=540, y=170, w=700, lignes=[
            dict(f="f′_1 = " + fr("1", "C_1") + " = " + fr("1", "1,25"), taille=40),
            dict(f="f′_1 = 0,800 m = 800 mm", cadre=True, taille=40)]),
        "s12": dict(type="formule", titre="2 · La longueur de la lunette", x=540, y=170, w=700, lignes=[
            dict(f="afocale : F′_1 = F_2", taille=38),
            dict(f="O_1O_2 = f′_1 + f′_2 = 800 + 20 = 820 mm", cadre=True, taille=36)]),
        "s13": dict(type="formule", titre="3 · Le grossissement", x=540, y=170, w=700, lignes=[
            dict(f="G = " + fr("f′_1", "f′_2") + " = " + fr("800 mm", "20 mm"), taille=40),
            dict(f="G = 40", cadre=True, taille=44)]),
        "s14": dict(type="formule", titre="4 · Jupiter", x=540, y=130, w=700, lignes=[
            dict(f="α ≈ " + fr("1,40 × 10^5", "6,3 × 10^8") + " ≈ 2,2 × 10^-4 rad", taille=34),
            dict(f="2,2 × 10^-4 < 3 × 10^-4 rad : un point à l'œil nu", ko=True, taille=30),
            dict(f="α′ = 40 × 2,2 × 10^-4 ≈ 8,9 × 10^-3 rad : un disque", cadre=True, ok=True, taille=32)]),
    }),

    # ================================================================ XI. exercice 2 (difficile)
    # α = 0,50° = 8,73e-3 rad ; A1B1 = 600 mm × tan α = 5,24 mm ; tan α′ = 5,24/40 = 0,131 → α′ ≈ 0,13 rad ≈ 7,5° ;
    # G = 0,131/8,73e-3 = 15,0 = 60/4,0 ; oculaire de 6,0 cm : O1O2 passe de 64 à 66 cm (+2,0 cm), G = 10
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile : il fait refaire tout le raisonnement du grossissement. "
        "Une lunette afocale a un objectif de soixante centimètres de focale et un oculaire de quatre centimètres. "
        "On vise un astre de diamètre apparent zéro virgule cinquante degré.",
        "On demande : alpha en radians ; la taille de l'image intermédiaire ; l'angle alpha prime en sortie ; "
        "le grossissement, calculé de deux façons. Et enfin : on remplace l'oculaire par un de six centimètres. Que faire pour que la lunette reste afocale, "
        "et que devient le grossissement ?",
        "{-ex2}{pa2}Celui-là demande un vrai raisonnement. Mets sur pause, et fais-le en entier avant de regarder la correction.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un : alpha en radians égale alpha en degrés, fois pi sur cent quatre-vingts. "
        "{s21.2}Zéro virgule cinq fois pi sur cent quatre-vingts : huit virgule sept fois dix puissance moins trois radian.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux : l'image intermédiaire est dans le plan focal image de l'objectif, "
        "et A un B un égale f prime un fois tangente de alpha. {s22.2}Six cents millimètres fois huit virgule sept fois dix puissance moins trois : "
        "environ cinq virgule deux millimètres.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois : dans le triangle O deux F deux B un, tangente de alpha prime égale A un B un sur f prime deux. "
        "{s23.2}Cinq virgule deux sur quarante : zéro virgule treize. {s23.3}Alpha prime vaut environ zéro virgule treize radian, à peu près sept degrés et demi.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre : par la définition, G égale alpha prime sur alpha : zéro virgule treize sur huit virgule sept fois dix puissance moins trois. "
        "On trouve quinze. {s24.2}Et par la formule : soixante sur quatre, quinze aussi. Les deux méthodes concordent.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq. Pour rester afocale, il faut toujours F prime un égal F deux. "
        "La longueur passe de soixante plus quatre, soixante-quatre centimètres, à soixante plus six, soixante-six centimètres. "
        "{s25.2}Il faut donc éloigner l'oculaire de deux centimètres de l'objectif. "
        "{s25.3}Et le grossissement devient soixante sur six : dix. Un oculaire plus long grossit moins.",
        "{-s25}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=60, titre="Refaire le raisonnement du grossissement", src="Exercice inventé pour la vidéo",
                    enonce=["Une lunette afocale a un objectif de focale f′₁ = 60 cm et un oculaire de focale f′₂ = 4,0 cm. "
                            "Elle vise un astre de diamètre apparent α = 0,50°."],
                    donnees=["f′_1 = 60 cm", "f′_2 = 4,0 cm", "α = 0,50°"],
                    questions=["Exprimer α en radians.", "Calculer la taille A₁B₁ de l'image intermédiaire.",
                               "En déduire l'angle α′ sous lequel on voit l'astre dans la lunette.",
                               "Calculer G de deux façons et comparer.",
                               "On prend un oculaire de 6,0 cm : comment garder la lunette afocale ? Nouveau G ?"]),
        "pa2": dict(type="pause", t="α en radians, A₁B₁, α′, G de deux façons, puis le nouvel oculaire."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Le grossissement, pas à pas",
                     donnees=["f′_1 = 60 cm", "f′_2 = 4,0 cm", "α = 0,50°"],
                     questions=["α en rad ?", "A_1B_1 ?", "α′ ?", "G, deux façons ?", "Oculaire de 6,0 cm ?"]),
        "s21": dict(type="formule", titre="1 · α en radians", x=540, y=170, w=700, lignes=[
            dict(f="α = 0,50 × " + fr("π", "180"), taille=40),
            dict(f="α ≈ 8,7 × 10^-3 rad", cadre=True, taille=40)]),
        "s22": dict(type="formule", titre="2 · L'image intermédiaire", x=540, y=170, w=700, lignes=[
            dict(f="A_1B_1 = f′_1 × tan α", taille=38),
            dict(f="A_1B_1 = 600 mm × 8,7 × 10^-3 ≈ 5,2 mm", cadre=True, taille=36)]),
        "s23": dict(type="formule", titre="3 · L'angle en sortie", x=540, y=150, w=700, lignes=[
            dict(f="tan α′ = " + fr("A_1B_1", "f′_2"), taille=38),
            dict(f="tan α′ = " + fr("5,2 mm", "40 mm") + " ≈ 0,13", taille=38),
            dict(f="α′ ≈ 0,13 rad ≈ 7,5°", cadre=True, taille=38)]),
        "s24": dict(type="formule", titre="4 · Le grossissement, deux façons", x=540, y=150, w=700, lignes=[
            dict(f="G = " + fr("α′", "α") + " = " + fr("0,13", "8,7 × 10^-3") + " ≈ 15", taille=36),
            dict(f="G = " + fr("f′_1", "f′_2") + " = " + fr("60", "4,0") + " = 15", taille=36),
            dict(f="les deux méthodes concordent", cadre=True, ok=True, taille=34)]),
        "s25": dict(type="formule", titre="5 · Le nouvel oculaire", x=540, y=140, w=700, lignes=[
            dict(f="avant : O_1O_2 = 60 + 4,0 = 64 cm", taille=34),
            dict(f="après : O_1O_2 = 60 + 6,0 = 66 cm", taille=34),
            dict(f="éloigner l'oculaire de 2,0 cm", cadre=True, taille=36),
            dict(f="G = " + fr("60", "6,0") + " = 10 : un oculaire plus long grossit moins", taille=32)]),
    }),

    # ================================================================ XII. exercice 3 (type bac)
    # 90/900 : f′1 = 900 mm ; oculaires 25 mm → G = 36, O1O2 = 925 mm ; 9 mm → G = 100
    # Copernic : 93 km / 384 400 km = 2,42e-4 rad < 3e-4 ; α′ (25 mm) = 36 × 2,42e-4 = 8,7e-3 rad ≈ 0,50°
    # 1° = 1,75e-2 rad → G ≥ 1,75e-2 / 2,42e-4 = 72 → f′2 ≤ 900/72 = 12,5 mm : l'oculaire de 9 mm convient (G = 100), pas celui de 25 mm
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac. Le club veut observer le cratère Copernic, sur la Lune, avec une lunette quatre-vingt-dix sur neuf cents, "
        "livrée avec deux oculaires : vingt-cinq millimètres et neuf millimètres.",
        "On donne : Copernic mesure quatre-vingt-treize kilomètres de diamètre, la Lune est à trois cent quatre-vingt-quatre mille quatre cents kilomètres, "
        "et le pouvoir séparateur de l'œil vaut environ trois fois dix puissance moins quatre radian.",
        "{-ex3}{ex3b}Cinq questions. Un : identifier l'objectif et l'oculaire, et donner la condition et la longueur de la lunette afocale avec l'oculaire de vingt-cinq millimètres. "
        "Deux : calculer les deux grossissements. Trois : établir l'expression du grossissement. "
        "Quatre : Copernic est-il visible à l'œil nu ? Et avec l'oculaire de vingt-cinq millimètres ? "
        "Cinq : le club veut voir Copernic sous au moins un degré. Quel oculaire choisir ?",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}{s31.1}Question un. L'objectif est la lentille de grande focale, neuf cents millimètres, du côté de l'astre. "
        "L'oculaire est celle de petite focale, du côté de l'œil. {s31.2}La lunette est afocale si le foyer image de l'objectif est confondu avec le foyer objet de l'oculaire. "
        "{s31.3}Alors O un O deux égale neuf cents plus vingt-cinq : neuf cent vingt-cinq millimètres.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Question deux. Avec l'oculaire de vingt-cinq millimètres : neuf cents sur vingt-cinq, G vaut trente-six. "
        "{s32.2}Avec celui de neuf millimètres : cent.",
        "{-s32}{ex3c.q3}{s33}Question trois : c'est la démonstration du grossissement, à rédiger en entier. {s33.1}Dans le triangle O un F prime un B un, tangente de alpha égale A un B un sur f prime un. "
        "{s33.2}Dans le triangle O deux F deux B un, tangente de alpha prime égale A un B un sur f prime deux. "
        "{s33.3}Les angles sont petits et en radians. {s33.4}Donc G égale alpha prime sur alpha, égale f prime un sur f prime deux.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Question quatre. À l'œil nu, alpha vaut quatre-vingt-treize sur trois cent quatre-vingt-quatre mille quatre cents : "
        "environ deux virgule quatre fois dix puissance moins quatre radian. {s34.2}C'est moins que le pouvoir séparateur : Copernic n'est pas visible à l'œil nu. "
        "{s34.3}Avec l'oculaire de vingt-cinq millimètres : trente-six fois cet angle, environ huit virgule sept fois dix puissance moins trois radian. "
        "Bien au-dessus du pouvoir séparateur : le cratère est visible.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq, la résolution de problème. Un degré, c'est un virgule soixante-quinze fois dix puissance moins deux radian. "
        "{s35.2}Le grossissement nécessaire : un virgule soixante-quinze fois dix puissance moins deux, divisé par deux virgule quatre fois dix puissance moins quatre. "
        "Environ soixante-douze. {s35.3}Il faut donc un oculaire de focale inférieure à neuf cents sur soixante-douze, environ douze virgule cinq millimètres. "
        "{s35.4}L'oculaire de neuf millimètres convient, avec un grossissement de cent. Celui de vingt-cinq ne suffit pas.",
        "{s35.5}Et le regard critique, toujours valorisé : le modèle des lentilles minces ne dit rien de la diffraction ni des aberrations. "
        "Grossir plus ne sert à rien si l'image devient floue. Ici, un grossissement de cent reste raisonnable pour un objectif de quatre-vingt-dix millimètres.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Observer le cratère Copernic", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Un club d'astronomie dispose d'une lunette « 90/900 » livrée avec deux oculaires de focales 25 mm et 9 mm.",
                            "Il veut observer le cratère Copernic, sur la Lune."],
                    donnees=["Copernic : diamètre ≈ 93 km", "distance Terre-Lune ≈ 384 400 km", "pouvoir séparateur de l'œil ≈ 3 × 10^-4 rad"]),
        "ex3b": dict(type="exo", niveau="bac", titre="Observer le cratère Copernic · questions",
                     questions=["Identifier objectif et oculaire ; condition et longueur de la lunette afocale (oculaire de 25 mm).",
                                "Calculer le grossissement avec chaque oculaire.",
                                "Établir l'expression du grossissement d'une lunette afocale.",
                                "Copernic est-il visible à l'œil nu ? Avec l'oculaire de 25 mm ?",
                                "Le club veut voir Copernic sous au moins 1°. Quel oculaire choisir ?"]),
        "pa3": dict(type="pause", t="Schéma afocal, grossissements, démonstration, Copernic à l'œil nu et dans la lunette, choix de l'oculaire."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Le cratère Copernic",
                     donnees=["90/900", "oculaires 25 mm et 9 mm", "Copernic 93 km à 384 400 km"],
                     questions=["Objectif, oculaire, O_1O_2 ?", "Les deux G ?", "Établir G ?", "Visible ?", "Quel oculaire pour 1° ?"]),
        "s31": dict(type="formule", titre="1 · Objectif, oculaire, réglage", x=540, y=130, w=700, lignes=[
            dict(f="objectif : f′_1 = 900 mm · oculaire : f′_2 = 25 mm", taille=32),
            dict(f="afocale : F′_1 = F_2", taille=38),
            dict(f="O_1O_2 = 900 + 25 = 925 mm", cadre=True, taille=38)]),
        "s32": dict(type="formule", titre="2 · Les grossissements", x=540, y=170, w=700, lignes=[
            dict(f="25 mm : G = " + fr("900", "25") + " = 36", taille=40),
            dict(f="9 mm : G = " + fr("900", "9") + " = 100", cadre=True, taille=40)]),
        "s33": dict(type="formule", titre="3 · Établir G = f′₁ / f′₂", x=540, y=110, w=700, lignes=[
            dict(f="O_1F′_1B_1 : tan α = " + fr("A_1B_1", "f′_1"), taille=32),
            dict(f="O_2F_2B_1 : tan α′ = " + fr("A_1B_1", "f′_2"), taille=32),
            dict(f="petits angles, en radians : tan α ≈ α", taille=26, txt=True),
            dict(f="G = " + fr("α′", "α") + " = " + fr("f′_1", "f′_2"), cadre=True, taille=36)]),
        "s34": dict(type="formule", titre="4 · Copernic est-il visible ?", x=540, y=120, w=700, lignes=[
            dict(f="α ≈ " + fr("93", "384 400") + " ≈ 2,4 × 10^-4 rad", taille=34),
            dict(f="< 3 × 10^-4 rad : invisible à l'œil nu", ko=True, taille=32),
            dict(f="α′ = 36 × 2,4 × 10^-4 ≈ 8,7 × 10^-3 rad : visible", cadre=True, ok=True, taille=32)]),
        "s35": dict(type="formule", titre="5 · Quel oculaire pour 1° ?", x=540, y=96, w=700, lignes=[
            dict(f="1° = 1,75 × 10^-2 rad", taille=32),
            dict(f="G ≥ " + fr("1,75 × 10^-2", "2,4 × 10^-4") + " ≈ 72", taille=32),
            dict(f="f′_2 ≤ " + fr("900", "72") + " ≈ 12,5 mm", taille=32),
            dict(f="l'oculaire de 9 mm (G = 100)", cadre=True, ok=True, taille=34),
            dict(f="Regard critique : le modèle ignore diffraction et aberrations ; grossir plus ne sert à rien si l'image est floue.", txt=True)]),
    }),

    # ================================================================ XIII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, la lunette afocale : F prime un égale F deux. "
        "{carte.1}D'abord les lentilles : les trois rayons particuliers, la vergence, la relation de conjugaison. "
        "{carte.2}Ensuite l'objectif : d'un astre, il forme une image intermédiaire réelle et renversée dans son plan focal image. "
        "{carte.3}Puis l'oculaire : placé pour que F prime un égale F deux, il renvoie l'image à l'infini, et l'œil voit net sans fatigue. "
        "{carte.4}Et le grossissement : G égale alpha prime sur alpha, égale f prime un sur f prime deux.",
        "{-carte}{bac}Voici ce que le bac peut te demander, à cocher. "
        "{bac.1}Représenter le schéma d'une lunette afocale. {bac.2}Identifier l'objectif et l'oculaire. "
        "{bac.3}Tracer le faisceau émergent issu d'un point à l'infini. {bac.4}Établir l'expression du grossissement. "
        "{bac.5}Exploiter les données d'une lunette commerciale. {bac.6}Déterminer le grossissement d'une maquette ou d'une vraie lunette. "
        "{bac.7}Et vérifier la position de l'image intermédiaire sur un écran.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre. Il ne te reste qu'à t'entraîner sur d'autres exercices. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="LUNETTE AFOCALE · F′₁ = F₂", branches=[
            dict(t="Les lentilles", items=["3 rayons particuliers", "C = 1/f′ (f′ en m)", "1/‾{OA′} − 1/‾{OA} = 1/f′"]),
            dict(t="L'objectif", items=["grande focale", "A₁B₁ dans le plan focal image", "réelle, renversée, ≈ f′₁ × α"]),
            dict(t="L'oculaire", items=["petite focale", "image à l'infini", "œil au repos, sans fatigue"]),
            dict(t="Le grossissement", items=["G = α′/α (rad)", "G = f′₁/f′₂", "« 70/700 » : D puis f′₁"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Représenter le schéma d'une lunette afocale", "Identifier l'objectif et l'oculaire",
            "Tracer le faisceau émergent d'un point à l'infini", "Établir G = f′_1 / f′_2",
            "Exploiter les données d'une lunette commerciale", "Déterminer le grossissement d'une lunette (expérience)",
            "Vérifier la position de l'image intermédiaire sur un écran"], marques=["✓"] * 7, x=170, y=80, w=940, petit=True),
    }),
]

QUIZ = [
    dict(q="Une lentille a une focale de 5,0 cm. Sa vergence vaut…", r=["0,2 δ", "5,0 δ", "20 δ"], ok=2,
         ex="C = 1/f′ avec f′ en mètres : 1/0,050 = 20 δ.", voir="f_C"),
    dict(q="Un objet est placé au foyer objet d'une lentille convergente. Son image est…",
         r=["dans le plan focal image", "à l'infini : les rayons ressortent parallèles", "confondue avec l'objet"], ok=1,
         ex="Avec ‾{OA} = −f′, la relation de conjugaison donne 1/‾{OA′} = 0 : l'image est à l'infini.", voir="limites"),
    dict(q="Où se forme l'image intermédiaire d'un astre donnée par l'objectif ?",
         r=["Dans le plan focal image de l'objectif", "Au foyer objet de l'objectif", "Sur l'oculaire"], ok=0,
         ex="Un objet à l'infini donne une image dans le plan focal image : A₁B₁ est en F′₁.", voir="pts1"),
    dict(q="Une lunette est afocale quand…", r=["F₁ = F′₂", "F′₁ = F₂", "F′₁ = F′₂"], ok=1,
         ex="Le foyer image de l'objectif coïncide avec le foyer objet de l'oculaire : l'image intermédiaire est au foyer objet de l'oculaire.", voir="piege_f"),
    dict(q="Une lunette afocale a f′₁ = 50 cm et f′₂ = 5,0 cm. Sa longueur O₁O₂ vaut…", r=["45 cm", "55 cm", "250 cm"], ok=1,
         ex="O₁O₂ = f′₁ + f′₂ = 55 cm.", voir="f_long"),
    dict(q="Dans une lunette astronomique, l'image d'un astre est…", r=["droite", "renversée", "droite ou renversée selon l'oculaire"], ok=1,
         ex="Le rayon le plus haut à l'entrée ressort le plus bas : l'image est renversée.", voir="pts3"),
    dict(q="Le grossissement d'une lunette afocale vaut…", r=["f′₂ / f′₁", "f′₁ / f′₂", "f′₁ × f′₂"], ok=1,
         ex="G = α′/α = f′₁/f′₂ : l'objectif doit avoir la plus grande focale.", voir="f_G2"),
    dict(q="Une lunette « 70/700 » est utilisée avec un oculaire de 10 mm. Son grossissement vaut…", r=["7", "70", "700"], ok=1,
         ex="700 est la focale de l'objectif en mm : G = 700/10 = 70.", voir="ex_70"),
    dict(q="Pour calculer α ≈ h/D, l'angle doit être exprimé…", r=["en degrés", "en radians", "dans n'importe quelle unité"], ok=1,
         ex="tan α ≈ α n'est vrai qu'en radians : vérifie le mode de la calculatrice.", voir="pieges_a"),
    dict(q="Les irisations colorées sur les bords de l'image s'expliquent par…",
         r=["la diffraction", "l'aberration chromatique : l'indice du verre dépend de la longueur d'onde", "un mauvais réglage afocal"], ok=1,
         ex="C'est une limite du modèle des lentilles minces : les foyers du bleu et du rouge ne coïncident pas.", voir="lim"),
]

CREDITS = [
    "Photos : la pleine Lune vue depuis l'espace, NASA (domaine public) ; Saturne vue par Cassini, 2004, NASA/JPL/Space Science Institute "
    "(domaine public) ; la lunette de 40 pouces de l'observatoire Yerkes, 1897 (domaine public) ; Galilée par Justus Sustermans (Offices, domaine public).",
    "Images trouvées sur Wikimedia Commons. Animations, schémas et graphiques : faits pour la vidéo. Données astronomiques arrondies. "
    "Les trois exercices sont inventés pour la vidéo.",
]
