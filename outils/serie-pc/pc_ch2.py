"""Physique-chimie, chapitre 2 : « Méthodes physiques d'analyse » — le cours en vidéo.

Même chaîne que la vidéo du chapitre 4 (outils/serie-pc/pc_ch4.py) : outils/serie-philo/generer.py, voix clonée,
calage des visuels sur les mots ; moteur pc/serie/moteur.js (types anim, formule, graphe, exo, pause).
Contenu : le cours du site (pc/index.html, chapitre 2 : rappels, fiches 1 à 9, TP 2 et TP 3, fiche mémo), rien au-delà ;
ce qui dépasse le programme est dit « hors programme ». Les trois exercices sont inventés pour la vidéo (signalé à
l'écran) ; leurs valeurs ont été recalculées (voir les commentaires).
Usage : python3 outils/serie-philo/verifier.py pc_ch2 ; puis generer.py pc_ch2 ; chevauchements.py ch2.
"""

SITE = "pc"
CODE = "ch2"
NOTION = "Méthodes physiques d'analyse"
NUM = 2
TITRE = "Méthodes physiques d'analyse"
SUIVANT = "Chapitre 3 · Méthodes chimiques d'analyse"
PRONONCIATION = {"Kohlrausch": "Kolraouche", "Beer-Lambert": "Bère-Lambère", "Alodont": "Alodonte",
                 "Saint-Marc": "Saint-Mar"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]"


# ---------------------------------------------------------------- données des graphiques
import math


def gauss(x, x0, s, a):
    return a * math.exp(-((x - x0) / s) ** 2 / 2)


# spectre du E131 schématisé (maximum vers 630 nm), comme dans le schéma interactif du site ; solution de référence à
# 2,00 mg/L : A = 0,26 au maximum ; solution suspecte du TP 2 : A = 0,025 (même allure) ; sulfate de cuivre : absorbe
# peu vers 630 nm et culmine au-delà de 800 nm (allure schématisée)
LAMS = list(range(400, 901, 10))
E131 = [[l, round(gauss(l, 630, 32, 0.26) + 0.004, 4)] for l in LAMS]
SUSP = [[l, round(gauss(l, 630, 32, 0.025) + 0.001, 4)] for l in LAMS]
CUSO4 = [[l, round(gauss(l, 830, 95, 0.20) + 0.003, 4)] for l in LAMS]
# TP 2 : A = 0,13 × C (C en mg/L, cuve de 1,0 cm) ; suspecte A = 0,025 → C = 0,025 / 0,13 = 0,192 ≈ 0,19 mg/L
TP2 = [[c, round(0.13 * c, 4)] for c in (0.04, 0.10, 0.20, 0.40, 0.50, 1.00, 2.00)]
# TP 3 (mesures d'Orhan) : σ en mS/cm ; k ≈ 82 mS·cm⁻¹ par mol/L ; Saint-Marc /10 : σ = 2,10 → C = 2,10/82 = 0,0256 ≈ 2,6e-2
TP3 = [[0.010, 0.76], [0.020, 1.64], [0.050, 4.14], [0.10, 7.43]]


# spectres infrarouges schématisés (transmittance en %, bandes vers le bas), d'après la table des bandes du cours
def ir(bandes):
    pts = []
    for s in range(4000, 499, -25):
        t = 92 - sum(gauss(s, c, w, p) for c, w, p in bandes)
        pts.append([s, round(max(4, t), 1)])
    return pts


EMPREINTE = [(1450, 25, 25), (1380, 18, 18), (1250, 30, 22), (1100, 25, 30), (1050, 22, 40), (880, 20, 25), (700, 25, 18)]
IR_ETHANOL = ir([(3350, 110, 60), (2970, 25, 40), (2900, 20, 25)] + EMPREINTE)
IR_ACIDE = ir([(2950, 260, 55), (3050, 160, 15), (1715, 22, 78), (1290, 30, 40)] + EMPREINTE[:3])
IR_PROPANONE = ir([(3000, 20, 18), (2930, 18, 12), (1715, 20, 82), (1360, 20, 40), (1220, 25, 45)])

# exercice 3 : étalonnage inventé du colorant bleu à 630 nm (c en µmol/L) ; k (régression par l'origine) = 0,1049 ≈ 0,105
EX3 = [[1.0, 0.104], [2.0, 0.211], [4.0, 0.418], [6.0, 0.632], [8.0, 0.838]]

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_coul}{q1}Un flacon de bain de bouche, bleu. On le soupçonne d'être une contrefaçon. "
        "Le colorant est-il le bon ? Et y en a-t-il la bonne quantité ?",
        "{-q1}{q2}Tu pourrais le faire réagir avec un réactif. Mais il existe plus simple, plus rapide, et sans en détruire une seule goutte : "
        "il suffit de faire passer de la lumière à travers.",
        "{-q2}{q3}Et cette lessive diluée, sur une étiquette effacée : était-elle assez concentrée pour laver un sol ? "
        "Cette fois, c'est un petit courant électrique qui va répondre.",
        ("Comment mesurer une concentration sans toucher à la solution ?", {"rate": "-6%"}),
        "{-q3}{-tab_coul}{plan}Dans cette vidéo, on part de zéro. {plan.1}D'abord la couleur d'une solution, et la lumière qu'elle absorbe : "
        "l'absorbance et la loi de Beer-Lambert. {plan.2}Puis le spectre, pour choisir la bonne longueur d'onde et identifier une espèce. "
        "{plan.3}Ensuite le dosage par étalonnage, le cœur pratique du chapitre. "
        "{plan.4}Puis la conductivité et la loi de Kohlrausch, et les pièges d'unités. "
        "{plan.5}Puis la spectroscopie infrarouge, pour reconnaître des groupes d'atomes. "
        "{plan.6}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_coul": dict(type="tableau", img="c2-etalons", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .6],
                         legende="Gamme de solutions bleues en fioles jaugées, photo Alina Popova, CC BY 4.0"),
        "q1": dict(type="question", t="Ce bain de bouche bleu est-il une contrefaçon ?"),
        "q2": dict(type="question", t="Analyser sans détruire : faire passer de la lumière."),
        "q3": dict(type="question", t="Cette lessive diluée était-elle assez concentrée ?"),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "La couleur, l'absorbance et la loi de Beer-Lambert", "Le spectre UV-visible : choisir λ, identifier",
            "Le dosage par étalonnage", "Conductivité, loi de Kohlrausch et unités",
            "La spectroscopie infrarouge", "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 2", t="Méthodes physiques d'analyse",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. mesurer sans détruire
    dict(id="sansdetruire", chap="Mesurer sans détruire", fond="nuit", humeur="lumiere",
         retenir="Méthode physique : on mesure une grandeur (absorbance, conductivité) sans faire réagir. Identifier = quelle espèce ; doser = combien.",
         beats=[
        "{tab_spec}Tout le chapitre répond à une seule question : comment connaître la composition d'une solution sans la transformer ?",
        "{-tab_spec}{def_phy}{def_phy.1}Une méthode physique mesure une grandeur physique de la solution : sa couleur, sa conductivité, "
        "la façon dont elle absorbe un rayonnement. On ne fait rien réagir : l'échantillon ressort intact. "
        "Une méthode chimique, au contraire, fait réagir l'espèce étudiée avec un réactif. C'est le chapitre trois.",
        "{-def_phy}{atouts}Les méthodes physiques ont deux atouts. {atouts.1}Elles sont non destructives : on peut refaire la mesure, ou récupérer le produit. "
        "{atouts.2}Et elles sont rapides, ce qui compte quand un laboratoire analyse des centaines d'échantillons par jour.",
        "{-atouts}{outils}Voici les outils du chapitre. "
        "{outils.1}Pour doser une espèce colorée : la spectrophotométrie, qui mesure l'absorbance A. "
        "{outils.2}Pour doser une espèce ionique : la conductimétrie, qui mesure la conductivité, notée sigma. "
        "{outils.3}Pour identifier une espèce colorée : son spectre ultraviolet-visible, et la position de son maximum. "
        "{outils.4}Pour identifier un groupe d'atomes dans une molécule : la spectroscopie infrarouge.",
        "{-outils}{id_dos}Et une distinction que l'énoncé attend toujours. {id_dos.g}Identifier, c'est répondre à la question : quelle espèce ? "
        "On compare la forme d'un spectre à une référence. "
        "{id_dos.d}Doser, c'est répondre à la question : combien ? On mesure une intensité, et on la convertit en concentration par un étalonnage.",
        "Les deux travaux pratiques du chapitre font les deux, l'un après l'autre : identifier d'abord, doser ensuite, et discuter enfin la validité du résultat.",
        "{-id_dos}",
    ], vis={
        "tab_spec": dict(type="tableau", img="c2-spectro", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .55],
                         legende="Spectrophotomètre de laboratoire, photo TimVickers (domaine public)"),
        "def_phy": dict(type="def", terme="Méthode physique d'analyse", cles=["grandeur", "intact"],
                        t="On mesure une grandeur physique de la solution sans la faire réagir : l'échantillon ressort intact.",
                        etape="Méthode chimique : on fait réagir l'espèce avec un réactif (chapitre 3).", x=170, y=180, w=940),
        "atouts": dict(type="liste", titre="Deux atouts", items=[
            "Non destructive : on peut refaire la mesure, récupérer le produit", "Rapide : des centaines d'échantillons"],
                       marques=["1", "2"], x=170, y=200, w=940),
        "outils": dict(type="liste", titre="Les outils du chapitre", items=[
            "Doser une espèce colorée : spectrophotométrie → absorbance A",
            "Doser une espèce ionique : conductimétrie → conductivité σ",
            "Identifier une espèce colorée : spectre UV-visible, position de λ_{max}",
            "Identifier un groupe caractéristique : spectroscopie infrarouge"], x=140, y=140, w=1000),
        "id_dos": dict(type="cols", g="Identifier", gq="« quelle espèce ? » · on compare la forme d'un spectre à une référence",
                       d="Doser", dq="« combien ? » · on mesure une intensité, on la convertit par étalonnage", vs="≠",
                       repere="Les TP : identifier, puis doser, puis discuter"),
    }),

    # ================================================================ II. la couleur
    dict(id="couleur", chap="La couleur d'une solution", fond="aube", humeur="calme",
         retenir="La couleur perçue est la complémentaire de la couleur absorbée : une solution bleue absorbe l'orange-rouge, vers 600-630 nm.",
         beats=[
        "{tab_cuv}Commençons par un rappel de Première. Pourquoi une solution est-elle colorée ? "
        "Parce qu'elle absorbe une partie de la lumière blanche, et laisse passer le reste.",
        "{-tab_cuv}{def_coul}{def_coul.1}La couleur que tu vois est celle de la lumière transmise. C'est la couleur complémentaire de celle qui a été absorbée.",
        "{-def_coul}{assoc}Retiens quelques associations, elles tombent souvent. "
        "{assoc.1}Une solution qui absorbe le bleu, vers quatre cent soixante-dix nanomètres, paraît jaune. "
        "{assoc.2}Une solution qui absorbe le bleu-vert, vers cinq cent dix nanomètres, paraît rouge. "
        "{assoc.3}Une solution qui absorbe le vert, vers cinq cent quarante nanomètres, paraît pourpre. "
        "{assoc.4}Et une solution qui absorbe l'orange, vers six cent trente nanomètres, paraît bleue.",
        "{-assoc}{piege_c}C'est le piège classique : on croit spontanément qu'une solution bleue absorbe le bleu. "
        "C'est l'inverse. Elle laisse passer le bleu, et absorbe l'orange. "
        "La couleur qu'on voit n'est jamais celle qu'on mesure.",
        "{-piege_c}{rap_k}Deuxième rappel de Première : pour une espèce colorée en solution diluée, la lumière absorbée augmente avec la concentration. "
        "{rap_k.1}On avait écrit A égale k fois c. {rap_k.2}Ce chapitre va expliquer ce que contient ce coefficient k, "
        "et étendre la méthode à une deuxième grandeur, la conductivité.",
        "{-rap_k}",
    ], vis={
        "tab_cuv": dict(type="tableau", img="c2-cuves", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .5],
                        legende="Cuves de spectrophotomètre, photo Retama, CC BY-SA 4.0"),
        "def_coul": dict(type="def", terme="Couleur perçue", cles=["transmise", "complémentaire"],
                         t="On voit la lumière transmise : la couleur complémentaire de celle qui est absorbée.", x=170, y=200, w=940),
        "assoc": dict(type="liste", titre="Couleur absorbée → couleur perçue", items=[
            "Absorbe le bleu (≈ 470 nm) → paraît jaune", "Absorbe le bleu-vert (≈ 510 nm) → paraît rouge",
            "Absorbe le vert (≈ 540 nm) → paraît pourpre", "Absorbe l'orange (≈ 630 nm) → paraît bleue"], x=170, y=150, w=940),
        "piege_c": dict(type="note", titre="Le sens de lecture", cles=["inverse", "orange"],
                        t="Une solution bleue absorbe l'orange, vers 600-630 nm. C'est l'inverse de ce qu'on croit.", x=170, y=210, w=940),
        "rap_k": dict(type="formule", titre="Rappel de Première", x=150, y=190, w=980, lignes=[
            dict(f="A = k × c", cadre=True, taille=56, n="en solution diluée : l'absorbance est proportionnelle à la concentration"),
            dict(f="Ce chapitre : que contient k ? Et une deuxième grandeur, σ.", txt=True)]),
    }),

    # ================================================================ III. absorbance, Beer-Lambert
    dict(id="beer", chap="L'absorbance et la loi de Beer-Lambert", fond="nuit", humeur="lumiere",
         retenir="A = log(I₀/I), sans unité. A = ε × ℓ × c : ε en L·mol⁻¹·cm⁻¹, ℓ en cm, c en mol·L⁻¹. En dosage, A = k × c. Au-delà de A ≈ 2,5 : diluer.",
         beats=[
        "{an_bl}{bl_pts}{bl_pts.1}{an_bl.1}Voici l'appareil : le spectrophotomètre. Une lampe, un dispositif qui ne garde qu'une seule longueur d'onde, "
        "une cuve qui contient la solution, et un détecteur. On commence toujours par le blanc : la cuve ne contient que le solvant. "
        "Toute la lumière arrive : c'est l'intensité de référence, I zéro.",
        "{bl_pts.2}{an_bl.2}On remplit la cuve d'une solution colorée. Certains photons rencontrent une molécule de colorant, et sont absorbés. "
        "Le détecteur en reçoit moins. Ici, la moitié seulement passe.",
        "{bl_pts.3}{an_bl.3}On allonge la cuve : deux centimètres, puis trois. Chaque centimètre contient autant de molécules, "
        "donc chacun absorbe la même fraction de ce qu'il reçoit. Cent pour cent, puis cinquante, puis vingt-cinq, puis douze et demi.",
        "{bl_pts.4}{an_bl.4}Retour à un centimètre, mais avec deux fois plus de molécules : seul un quart des photons passe. "
        "Ce qui compte, c'est le nombre de molécules sur le trajet de la lumière.",
        "{-an_bl}{-bl_pts}{f_A}{f_A.1}Pour mesurer cet affaiblissement, on définit l'absorbance : A égale le logarithme décimal de I zéro sur I. "
        "{f_A.2}I zéro, c'est l'intensité qui entre ; I, celle qui sort. L'absorbance n'a pas d'unité.",
        "{f_A.3}Comme I est plus petit que I zéro, le rapport dépasse un, et l'absorbance est toujours positive. "
        "Une solution qui n'absorbe rien donne I égale I zéro, donc A égale zéro. "
        "{f_A.4}Et quand la moitié de la lumière passe, A vaut log de deux : zéro virgule trente.",
        "{-f_A}{pourquoi_log}Pourquoi un logarithme, et pas une simple différence ? {pourquoi_log.1}Parce que l'absorption est un phénomène multiplicatif. "
        "Chaque tranche de solution absorbe la même fraction de la lumière qu'elle reçoit, pas la même quantité. "
        "{pourquoi_log.2}L'intensité est donc divisée à chaque tranche : cent, cinquante, vingt-cinq, douze, six. "
        "{pourquoi_log.3}Or le logarithme change les divisions en soustractions régulières. Chaque tranche ajoute la même absorbance, ici zéro virgule trente. "
        "{pourquoi_log.4}L'absorbance devient donc proportionnelle au nombre de tranches traversées.",
        "{-pourquoi_log}{f_BL}Et le nombre de molécules rencontrées dépend de deux choses seulement : la longueur du trajet, et la concentration. "
        "{f_BL.1}D'où, immédiatement : A est proportionnelle à l, et A est proportionnelle à c. "
        "{f_BL.2}C'est la loi de {!Beer-Lambert}Beer-Lambert : A égale epsilon, fois l, fois c.",
        "{f_BL.3}Epsilon, c'est le coefficient d'absorption molaire, en litre par mole par centimètre. "
        "l, c'est la longueur de la cuve, en centimètres. Et c, la concentration, en mole par litre.",
        "{f_BL.4}Epsilon mesure la capacité d'une espèce à absorber la lumière. Il dépend de l'espèce, et de la longueur d'onde : "
        "la même molécule a un epsilon élevé à son maximum d'absorption, et presque nul ailleurs.",
        "{-f_BL}{u_eps}D'où vient cette unité bizarre ? Elle n'est pas choisie, elle est imposée. "
        "{u_eps.1}Isolons epsilon : epsilon égale A divisé par l fois c. "
        "{u_eps.2}A n'a pas d'unité, l est en centimètres, c en mole par litre. "
        "{u_eps.3}L'unité d'epsilon est donc l'inverse du produit : litre par mole par centimètre. Rien à apprendre par cœur : elle se reconstruit.",
        "{u_eps.4}Et c'est aussi le meilleur contrôle : dans epsilon fois l fois c, les litres, les moles et les centimètres se simplifient. "
        "Si ça ne se simplifie pas, une grandeur est dans la mauvaise unité.",
        "{-u_eps}{f_k}{f_k.1}En pratique, pendant un dosage, on ne change ni la cuve, ni la longueur d'onde. Epsilon et l sont constants. "
        "{f_k.2}Leur produit forme un seul coefficient : k égale epsilon fois l. Et on retrouve la relation de Première : A égale k fois c.",
        "{f_k.3}Une conséquence pratique : seul compte le produit l fois c. Une cuve cinq fois plus longue remplace exactement une solution cinq fois plus concentrée.",
        "{-f_k}{limites}Mais cette loi a trois limites, à citer. "
        "{limites.1}Un : l'appareil sature. A égale un, c'est un dixième de la lumière qui passe. A égale deux, un centième. A égale trois, un millième. "
        "Au-delà de deux virgule cinq environ, le détecteur ne reçoit presque plus rien, et la mesure n'a plus de sens. "
        "{limites.2}Deux : la solution doit être diluée. À forte concentration, les molécules interagissent, et la proportionnalité se perd. "
        "{limites.3}Trois : une seule espèce doit absorber à la longueur d'onde choisie. Sinon, les absorbances s'ajoutent, et on ne sait plus ce qu'on mesure.",
        "{-limites}{ex_sat}Un exemple. Une solution de permanganate de potassium, à environ deux millimoles par litre, "
        "avec un epsilon de deux virgule deux fois dix puissance trois litres par mole par centimètre, dans une cuve d'un centimètre. "
        "{ex_sat.1}D'abord, on convertit : deux fois dix puissance moins trois mole par litre. "
        "{ex_sat.2}A égale deux virgule deux fois dix puissance trois, fois un, fois deux fois dix puissance moins trois : quatre virgule quatre. "
        "{ex_sat.3}C'est hors de la gamme : l'appareil sature. La solution est de diluer, par exemple quatre fois, puis de multiplier par quatre la concentration trouvée.",
        "{-ex_sat}",
    ], vis={
        "an_bl": dict(type="anim", nom="beerlambert", x=40, y=72, h=624, seg=[[1.2, 10], [10, 21], [21, 32], [32, 43]]),
        "bl_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Le blanc : solvant seul, I = I_0, A = 0", "Des photons absorbés : la moitié passe, A = 0,30",
            "Chaque centimètre absorbe la même fraction : A ∝ ℓ", "Deux fois plus de molécules : A double, A ∝ c"]),
        "f_A": dict(type="formule", titre="L'absorbance", x=150, y=120, w=980, lignes=[
            dict(f="A = log " + fr("I_0", "I"), cadre=True, taille=56),
            dict(f="I_0 : intensité qui entre · I : intensité qui sort · A sans unité", txt=True),
            dict(f="I < I_0  ⇒  A > 0 ; rien d'absorbé : A = 0", taille=34),
            dict(f="la moitié passe : A = log 2 ≈ 0,30", taille=34)]),
        "pourquoi_log": dict(type="liste", titre="Pourquoi un logarithme ?", items=[
            "Chaque tranche absorbe la même fraction, pas la même quantité",
            "L'intensité est divisée : 100 → 50 → 25 → 12 → 6",
            "Le logarithme change les divisions en additions : + 0,30 par tranche",
            "A est proportionnelle au nombre de tranches traversées"], x=150, y=150, w=980),
        "f_BL": dict(type="formule", titre="La loi de Beer-Lambert", x=150, y=100, w=980, lignes=[
            dict(f="A ∝ ℓ   et   A ∝ c", taille=40),
            dict(f="A = ε × ℓ × c", cadre=True, taille=58),
            dict(f="ε en L·mol^-1·cm^-1 · ℓ en cm · c en mol·L^-1", txt=True),
            dict(f="ε dépend de l'espèce et de la longueur d'onde", txt=True, pt=True)]),
        "u_eps": dict(type="formule", titre="D'où vient l'unité de ε", x=150, y=130, w=980, lignes=[
            dict(f="ε = " + fr("A", "ℓ × c")),
            dict(f="A sans unité · ℓ en cm · c en mol·L^-1", txt=True),
            dict(f="ε en " + fr("1", "cm × mol·L^-1") + " = L·mol^-1·cm^-1", cadre=True),
            dict(f="contrôle : L·mol^-1·cm^-1 × cm × mol·L^-1 → sans unité ✓", txt=True, ok=True)]),
        "f_k": dict(type="formule", titre="En dosage : cuve et λ fixées", x=150, y=150, w=980, lignes=[
            dict(f="ε et ℓ constants", txt=True),
            dict(f="A = k × c   avec   k = ε × ℓ", cadre=True),
            dict(f="seul compte ℓ × c : une cuve 5 fois plus longue = une solution 5 fois plus concentrée", txt=True, pt=True)]),
        "limites": dict(type="liste", titre="Trois limites", items=[
            "L'appareil sature : A = 1 → 1/10 passe, A = 2 → 1/100 ; au-delà de 2,5 : diluer",
            "La solution doit être diluée",
            "Une seule espèce doit absorber à la longueur d'onde choisie"], marques=["1", "2", "3"], x=140, y=160, w=1000),
        "ex_sat": dict(type="formule", titre="Exemple · permanganate à 2 mmol·L^-1, ε = 2,2 × 10^3 L·mol^-1·cm^-1", x=130, y=150, w=1020, lignes=[
            dict(f="c = 2 mmol·L^-1 = 2 × 10^-3 mol·L^-1"),
            dict(f="A = 2,2 × 10^3 × 1 × 2 × 10^-3 = 4,4"),
            dict(f="4,4 > 2,5 : l'appareil sature → diluer (× 4), puis multiplier c par 4", ko=True, taille=32)]),
    }),

    # ================================================================ IV. le spectre UV-visible
    dict(id="spectre", chap="Le spectre UV-visible", fond="nuit", humeur="calme",
         retenir="On mesure à λmax : sensibilité maximale et courbe plate. Même λmax et même allure qu'une référence = même espèce. La hauteur renseigne sur la concentration.",
         beats=[
        "{an_sp}{sp_pts}{sp_pts.1}{an_sp.1}Une question reste : à quelle longueur d'onde mesurer ? On fait varier lambda, et on relève l'absorbance pour chacune. "
        "La courbe A en fonction de lambda, c'est le spectre d'absorption. Ce colorant absorbe surtout l'orange-rouge, avec un maximum vers six cent trente nanomètres. "
        "Il laisse passer le bleu : la solution paraît bleue.",
        "{-an_sp}{-sp_pts}{lmax}On se place au maximum d'absorption, lambda max, pour deux raisons. Et l'énoncé attend les deux. "
        "{lmax.1}Première raison : la sensibilité est maximale. C'est là qu'une petite variation de concentration produit la plus grande variation d'absorbance.",
        "{lmax.2}Deuxième raison : la courbe y est plate. Au sommet, une petite erreur sur le réglage de la longueur d'onde ne change presque rien à l'absorbance. "
        "Sur un flanc raide, la même erreur fausserait tout.",
        "{lmax.3}La raison est mathématique : au sommet d'une courbe, la pente est nulle. Une erreur de deux nanomètres est sans conséquence à lambda max, "
        "et catastrophique trente nanomètres plus loin.",
        "{-lmax}{gr_sp}Le spectre sert aussi à identifier. Regarde les documents du TP deux. Un bain de bouche, coloré par le bleu patenté, le E cent trente et un. "
        "{gr_sp.1}Voici le spectre du E cent trente et un de référence : un maximum vers six cent trente nanomètres. "
        "{gr_sp.2}Voici celui du sulfate de cuivre, l'autre suspect : il n'absorbe presque pas vers six cent trente, et culmine au-delà de huit cents. "
        "{gr_sp.3}Et voici la solution du flacon suspect : même maximum, même allure que le E cent trente et un. Seulement plus bas.",
        "{-gr_sp}{id_h}Conclusion, et retiens bien la distinction. {id_h.g}Ce qui prouve l'identité de l'espèce, c'est la position du maximum et la forme du spectre. "
        "Le flacon contient du E cent trente et un. "
        "{id_h.d}Ce qui renseigne sur la concentration, c'est la hauteur. Plus bas que la référence : moins concentré.",
        "Confondre les deux est l'erreur classique. Et attention à la formulation : l'absorbance est proportionnelle à la concentration, jamais à la longueur d'onde.",
        "{-id_h}{deux_esp}Dernier point. {deux_esp.1}Si deux espèces absorbent toutes les deux à la longueur d'onde choisie, leurs absorbances s'additionnent, "
        "et le dosage est faussé. {deux_esp.2}Ici, c'est réglé : à six cent trente nanomètres, le sulfate de cuivre n'absorbe pratiquement pas. "
        "Même s'il était présent, il ne perturberait pas la mesure. C'est un troisième argument pour le choix de lambda.",
        "{-deux_esp}",
    ], vis={
        "an_sp": dict(type="anim", nom="beerlambert", x=40, y=72, h=624, seg=[[43, 53]]),
        "sp_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=200, w=560, items=[
            "On fait varier λ : le spectre A = f(λ) ; maximum vers 630 nm, la solution paraît bleue"]),
        "lmax": dict(type="liste", titre="Pourquoi mesurer à λ_{max}", items=[
            "La sensibilité est maximale : petite variation de c → grande variation de A",
            "La courbe est plate : une petite erreur sur λ ne change presque rien",
            "Au sommet, la pente est nulle : 2 nm d'écart, sans conséquence"], marques=["1", "2", "∴"], x=150, y=160, w=980),
        "gr_sp": dict(type="graphe", titre="TP 2 · spectres d'absorption", x=300, y=100, w=700, h=540,
                      ax=dict(x=[400, 900], y=[0, 0.3], gx=[500, 600, 700, 800, 900], gy=[0.1, 0.2, 0.3], lx="λ (nm)", ly="A"),
                      el=[dict(type="courbe", pts=E131, c="#5aa9ff", lbl="E131 · 2,00 mg/L", lp=[680, 0.27]),
                          dict(type="courbe", pts=CUSO4, c="#4fd1c5", lbl="sulfate de cuivre", lp=[770, 0.225]),
                          dict(type="courbe", pts=SUSP, c="sa", lbl="flacon suspect", lp=[640, 0.06])]),
        "id_h": dict(type="cols", g="Identifier", gq="position du maximum et allure du spectre : c'est du E131",
                     d="Doser", dq="hauteur du spectre : moins concentré que la référence", vs="≠",
                     repere="A ∝ c, jamais ∝ λ"),
        "deux_esp": dict(type="note", titre="Deux espèces, deux spectres", cles=["additionnent", "pratiquement"],
                         t="Si deux espèces absorbent à λ, les absorbances s'additionnent. À 630 nm, le sulfate de cuivre n'absorbe pratiquement pas.",
                         etape="Troisième argument pour mesurer à 630 nm.", x=170, y=200, w=940),
    }),

    # ================================================================ V. dosage par étalonnage
    dict(id="etalonnage", chap="Le dosage par étalonnage", fond="aube", humeur="calme",
         retenir="Gamme d'étalons qui encadre l'inconnue, blanc, mêmes conditions, droite par l'origine, lecture inverse c = A/k. Jamais d'extrapolation ; remonter la dilution.",
         beats=[
        "{tab_gam}Voici le cœur pratique du chapitre, la méthode commune aux deux TP : le dosage par étalonnage.",
        "{-tab_gam}{an_et}{et_pts}{et_pts.1}{an_et.1}Le principe. On prépare des solutions étalons, de concentrations connues. On mesure sur chacune la même grandeur. "
        "Les points s'alignent sur une droite qui passe par l'origine. Puis on mesure l'échantillon, et on fait la lecture inverse : "
        "on entre par l'axe vertical avec la grandeur mesurée, on ressort par l'axe horizontal avec la concentration.",
        "{et_pts.2}{an_et.2}Et la limite : si la solution est trop concentrée, presque aucun photon ne traverse. L'absorbance mesurée plafonne, les points quittent la droite. "
        "Il faut diluer, pour revenir dans la zone où la droite est valable.",
        "{-an_et}{-et_pts}{proto}Le protocole, en six étapes. "
        "{proto.1}Un : choisir la gamme, de façon que les étalons encadrent la valeur attendue, et pas qu'ils soient tous d'un côté. "
        "{proto.2}Deux : préparer les étalons par dilution d'une solution mère, à la pipette jaugée et à la fiole jaugée. Jamais au bécher gradué. "
        "{proto.3}Trois : faire le blanc avec le solvant seul, pour que l'appareil parte de zéro. "
        "{proto.4}Quatre : mesurer chaque étalon dans les mêmes conditions : même cuve, même longueur d'onde, même température. "
        "{proto.5}Cinq : tracer, et vérifier que les points sont alignés sur une droite qui passe par l'origine. "
        "{proto.6}Six : mesurer l'inconnue, et lire sa concentration sur la droite.",
        "{-proto}{f_dil}{f_dil.1}Pour préparer chaque étalon, on utilise la conservation de la quantité de soluté : "
        "c mère fois V mère égale c fille fois V fille. {f_dil.2}Donc le volume à prélever vaut c fille fois V fille, divisé par c mère. "
        "{f_dil.3}Par exemple, pour obtenir cent millilitres à zéro virgule vingt milligramme par litre, à partir d'une mère à deux milligrammes par litre : "
        "on prélève dix millilitres.",
        "{-f_dil}{regles}Quatre règles, qui font gagner ou perdre des points. "
        "{regles.1}Pas d'extrapolation : le résultat n'est valable que si la mesure tombe entre les étalons. Prolonger la droite, c'est supposer que la proportionnalité continue, "
        "et rien ne le garantit. Si l'inconnue sort du domaine, on la dilue, ou on étend la gamme.",
        "{regles.2}La droite doit passer par l'origine : concentration nulle, signal nul. Sinon, c'est un problème : blanc mal fait, cuve sale, ou autre espèce qui contribue. "
        "{regles.3}Dans la lecture inverse, on divise : c égale A sur k. On ne multiplie jamais. "
        "{regles.4}Et si l'échantillon a été dilué avant la mesure, on n'oublie pas de remonter la dilution à la fin.",
        "{-regles}{gr_tp2}Appliquons tout cela au flacon suspect du TP deux. {gr_tp2.1}Voici les étalons de E cent trente et un, mesurés à six cent trente nanomètres, en cuve d'un centimètre. "
        "{gr_tp2.2}Ils sont alignés sur une droite passant par l'origine : la loi de Beer-Lambert est vérifiée. "
        "Sa pente vaut zéro virgule vingt-six divisé par deux : zéro virgule treize litre par milligramme. "
        "{gr_tp2.3}Le flacon suspect donne une absorbance de zéro virgule zéro vingt-cinq.",
        "{-gr_tp2}{ex_tp2}{ex_tp2.1}On divise : c égale A sur k, {ex_tp2.2}zéro virgule zéro vingt-cinq sur zéro virgule treize : zéro virgule dix-neuf milligramme par litre. "
        "{ex_tp2.3}La valeur tombe bien dans le domaine étalonné.",
        "{ex_tp2.4}La zone d'authenticité va de zéro virgule vingt à zéro virgule trente. On est à cinq pour cent sous la borne basse. "
        "Mais une erreur de lecture de deux millièmes sur une absorbance si faible déplace déjà la concentration de deux centièmes. "
        "On ne peut ni conclure à la contrefaçon, ni certifier l'authenticité. Et n'oublie jamais l'unité : zéro virgule dix-neuf tout court ne veut rien dire.",
        "{-ex_tp2}{amelio}Comment faire mieux ? Le défaut, ce sont des absorbances toutes très basses, tout en bas de la gamme de l'appareil, là où le bruit compte. "
        "{amelio.1}L'amélioration décisive : une cuve de cinq centimètres. L'absorbance étant proportionnelle à l, elle serait multipliée par cinq : "
        "zéro virgule cent vingt-cinq pour le flacon, loin du bruit. {amelio.2}Mais il faudrait refaire toute la gamme avec cette cuve, puisque k dépend de l.",
        "{-amelio}",
    ], vis={
        "tab_gam": dict(type="tableau", img="c2-etalons", fond=True, sombre=True, de=[1.15, .5, .7], a=[1.0, .5, .55],
                        legende="Une gamme d'étalons en fioles jaugées, photo Alina Popova, CC BY 4.0"),
        "an_et": dict(type="anim", nom="beerlambert", x=40, y=72, h=624, seg=[[53, 63], [63, 74]]),
        "et_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Étalons alignés sur une droite ; l'échantillon : lecture inverse", "Trop concentré : A plafonne, il faut diluer"]),
        "proto": dict(type="liste", titre="Le protocole en six étapes", items=[
            "Choisir une gamme qui encadre la valeur attendue", "Préparer les étalons : pipette jaugée, fiole jaugée",
            "Faire le blanc avec le solvant seul", "Mesurer dans les mêmes conditions (cuve, λ, température)",
            "Tracer : points alignés, droite par l'origine", "Mesurer l'inconnue, lire sa concentration"], x=150, y=90, w=980, petit=True),
        "f_dil": dict(type="formule", titre="Préparer un étalon : la dilution", x=150, y=150, w=980, lignes=[
            dict(f="c_{mère} × V_{mère} = c_{fille} × V_{fille}", cadre=True),
            dict(f="V_{mère} = " + fr("c_{fille} × V_{fille}", "c_{mère}")),
            dict(f="V_{mère} = " + fr("0,20 × 100,0", "2,00") + " = 10,0 mL", n="pipette jaugée de 10,0 mL, fiole jaugée de 100,0 mL")]),
        "regles": dict(type="liste", titre="Quatre règles", items=[
            "Aucune extrapolation hors du domaine étalonné", "La droite passe par l'origine",
            "Lecture inverse : c = A / k, on divise", "Remonter la dilution à la fin"], marques=["1", "2", "3", "4"], x=150, y=160, w=980),
        "gr_tp2": dict(type="graphe", titre="TP 2 · droite d'étalonnage du E131 (630 nm, cuve de 1,0 cm)", x=330, y=110, w=640, h=520,
                       ax=dict(x=[0, 2.2], y=[0, 0.3], gx=[0.5, 1.0, 1.5, 2.0], gy=[0.1, 0.2, 0.3], lx="C (mg·L^-1)", ly="A"),
                       el=[dict(type="points", pts=TP2, c="#5aa9ff", pas=.15),
                           dict(type="droite", pts=[[0, 0], [2.2, 0.286]], c="#5aa9ff", lbl="A = 0,13 × C", lp=[1.35, 0.24], ep=2.6),
                           dict(type="point", x=0.19, y=0.025, c="sa", proj=True, lbl="flacon : A = 0,025", lp=[0.62, 0.06])]),
        "ex_tp2": dict(type="formule", titre="TP 2 · la concentration du flacon suspect", x=150, y=110, w=980, lignes=[
            dict(f="C = " + fr("A", "k")),
            dict(f="C = " + fr("0,025", "0,13") + " = 0,19 mg·L^-1", cadre=True),
            dict(f="dans le domaine étalonné (0 à 2,00 mg·L^-1) : pas d'extrapolation", ok=True, taille=32),
            dict(f="zone d'authenticité 0,20 – 0,30 : écart de 5 %, pas significatif", txt=True)]),
        "amelio": dict(type="formule", titre="L'amélioration : une cuve de 5,0 cm", x=150, y=170, w=980, lignes=[
            dict(f="A × 5 : flacon 0,025 → 0,125 · mère 0,26 → 1,3", taille=38),
            dict(f="k = ε × ℓ change : toute la gamme est à refaire", txt=True, pt=True)]),
    }),

    # ================================================================ VI. conductance et conductivité
    dict(id="conductance", chap="Conductance et conductivité", fond="nuit", humeur="lumiere",
         retenir="G = I/U = 1/R en siemens : dépend de la sonde. σ = G × L/S = K × G en S·m⁻¹ : ne dépend que de la solution. Relever l'unité affichée.",
         beats=[
        "{tab_cond}Changeons d'outil. Une solution qui contient des ions conduit le courant électrique. Le conductimètre mesure à quel point.",
        "{-tab_cond}{ohm}Un rappel du collège et de Première d'abord. {ohm.1}La loi d'Ohm : U égale R fois I. "
        "{ohm.2}La conductance, notée G, est l'inverse de la résistance. Elle mesure la facilité avec laquelle le courant passe, là où la résistance mesure la difficulté. "
        "G égale un sur R, égale I sur U. {ohm.3}Elle s'exprime en siemens.",
        "{-ohm}{an_c}{c_pts}{c_pts.1}{an_c.1}Deux plaques métalliques plongent dans l'eau distillée, reliées à un générateur et à un ampèremètre. "
        "Presque aucun ion : presque aucun courant. Dans une solution, ce ne sont pas des électrons qui transportent le courant, ce sont les ions.",
        "{c_pts.2}{an_c.2}On dissout du chlorure de sodium. Les ions sodium, positifs, migrent vers la plaque négative. Les ions chlorure, négatifs, vers la plaque positive. "
        "C'est le courant. Ici, cent vingt-six microampères sous un volt : une conductance de cent vingt-six microsiemens.",
        "{c_pts.3}{an_c.3}On double la concentration : deux fois plus d'ions, deux fois plus de courant.",
        "{c_pts.4}{an_c.4}Même solution, mais plaques deux fois plus proches : le courant double encore ! La solution n'a pas changé. "
        "C'est la sonde qui a changé.",
        "{-an_c}{-c_pts}{dist}Voici donc la distinction centrale du chapitre. {dist.g}La conductance G, c'est ce que l'appareil mesure. "
        "Mais elle dépend de la géométrie de la sonde : la même solution, mesurée avec deux cellules différentes, donne deux conductances différentes. "
        "{dist.d}La conductivité sigma, elle, caractérise la solution seule. Elle ne dépend plus de la sonde : c'est elle qu'on tabule et qu'on compare.",
        "{-dist}{voies}Comment passe-t-on de l'une à l'autre ? Imagine les ions comme des voitures qui vont d'une plaque à l'autre. "
        "{voies.1}La surface S des plaques, c'est le nombre de voies de circulation. Deux fois plus de voies, deux fois plus de débit : G est proportionnelle à S. "
        "{voies.2}La distance L entre les plaques, c'est la longueur du trajet. Deux fois plus long, deux fois moins de courant : G est proportionnelle à un sur L.",
        "{-voies}{f_sig}{f_sig.1}D'où : G égale sigma fois S sur L. {f_sig.2}Et donc sigma égale G fois L sur S. "
        "Multiplier par L sur S, c'est exactement annuler l'effet de la sonde.",
        "{f_sig.3}Le rapport L sur S s'appelle la constante de cellule, notée K. Sigma égale K fois G. "
        "K est propre à la sonde, et se règle une fois pour toutes en étalonnant le conductimètre.",
        "{f_sig.4}Et l'unité de sigma se reconstruit : des siemens, fois des mètres, divisés par des mètres carrés. Des siemens par mètre. "
        "La constante de cellule, elle, est en mètres moins un. C'est pour cela qu'une notice annonce : K égale un centimètre moins un.",
        "{-f_sig}{rho}Tu connais déjà cette formule sous un autre nom. Pour un fil électrique, la résistance vaut rho fois L sur S. "
        "Même géométrie, même raisonnement. La résistivité est à la résistance ce que la conductivité est à la conductance. "
        "La conductimétrie n'invente rien : elle applique à une solution ce qu'on sait d'un fil.",
        "{-rho}{aff}Un dernier piège, pratique. {aff.1}Selon le mode, le conductimètre affiche une conductance, en millisiemens ou microsiemens, "
        "ou une conductivité, en millisiemens par centimètre. Relève l'unité avant de noter la valeur : c'est une consigne explicite du TP trois.",
        "{-aff}",
    ], vis={
        "tab_cond": dict(type="tableau", img="c2-conductimetre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                         legende="Conductimètre et sa sonde, photo Nuno Nogueira, CC BY-SA 2.5"),
        "ohm": dict(type="formule", titre="Rappel · la loi d'Ohm", x=150, y=150, w=980, lignes=[
            dict(f="U = R × I", n="U en volts (V) · I en ampères (A) · R en ohms (Ω)"),
            dict(f="G = " + fr("1", "R") + " = " + fr("I", "U"), cadre=True, taille=52),
            dict(f="G en siemens (S) · « R, c'est 1 sur G »", txt=True)]),
        "an_c": dict(type="anim", nom="conductivite", x=40, y=72, h=624, seg=[[1.2, 9.5], [9.5, 20.5], [20.5, 30.5], [30.5, 40.5]]),
        "c_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=120, w=560, items=[
            "Eau distillée : presque aucun ion, I ≈ 0", "NaCl : cations vers −, anions vers + ; G = I/U = 126 µS",
            "c × 2 : deux fois plus d'ions, I × 2", "Plaques deux fois plus proches : G × 2, la solution n'a pas changé"]),
        "dist": dict(type="cols", g="Conductance G", gq="ce que l'appareil mesure · en siemens (S) · dépend de la sonde",
                     d="Conductivité σ", dq="propre à la solution · en S·m⁻¹ · on la tabule et on la compare", vs="≠",
                     repere="La distinction centrale du chapitre"),
        "voies": dict(type="liste", titre="Pourquoi G dépend de la sonde", items=[
            "Surface S des plaques = nombre de voies : G ∝ S",
            "Distance L entre les plaques = longueur du trajet : G ∝ 1/L"], marques=["S", "L"], x=150, y=200, w=980),
        "f_sig": dict(type="formule", titre="Conductance et conductivité", x=150, y=100, w=980, lignes=[
            dict(f="G = σ × " + fr("S", "L")),
            dict(f="σ = G × " + fr("L", "S") + " = K × G", cadre=True, taille=50),
            dict(f="K = " + fr("L", "S") + " : constante de cellule, propre à la sonde", txt=True),
            dict(f="σ en S × " + fr("m", "m^2") + " = S·m^-1 · K en m^-1 (ou cm^-1)", taille=34)]),
        "rho": dict(type="note", titre="Tu la connais déjà", cles=["résistivité", "conductivité"],
                    t="Pour un fil : R = ρ × L/S. La résistivité ρ est à la résistance ce que la conductivité σ est à la conductance.",
                    x=170, y=200, w=940),
        "aff": dict(type="note", titre="L'unité affichée", cles=["conductance", "conductivité"],
                    t="Selon le mode, l'appareil affiche une conductance (mS, µS) ou une conductivité (mS·cm⁻¹). Relever l'unité avant de noter.",
                    x=170, y=210, w=940),
    }),

    # ================================================================ VII. Kohlrausch
    dict(id="kohlrausch", chap="La loi de Kohlrausch", fond="nuit", humeur="tension",
         retenir="σ = Σ λᵢ × [Xᵢ] : σ en S·m⁻¹, λ en S·m²·mol⁻¹, [X] en mol·m⁻³. Le coefficient stœchiométrique va devant le λ de l'ion. Valable en solution diluée.",
         beats=[
        "{an_k}{k_pts}{k_pts.1}{an_k.1}Tous les ions conduisent-ils aussi bien ? Même concentration, mais de l'acide chlorhydrique à la place du sel. "
        "Les ions oxonium remplacent les ions sodium, et le courant est plus de trois fois plus fort.",
        "{k_pts.2}{an_k.2}C'est la loi de {!Kohlrausch}Kohlrausch : chaque ion apporte sa contribution, et ces contributions s'additionnent.",
        "{k_pts.3}{an_k.3}Elle a une limite : aux fortes concentrations, les points quittent la droite. On y reviendra.",
        "{-an_k}{-k_pts}{f_ko}{f_ko.1}La loi s'écrit : sigma égale la somme, sur tous les ions, de lambda i fois la concentration de l'ion i.",
        "{f_ko.2}Lambda, c'est la conductivité molaire ionique : la capacité d'un ion à conduire le courant. Elle est tabulée, propre à chaque ion, "
        "en siemens mètre carré par mole. {f_ko.3}Et la concentration doit être en mole par mètre cube. Pas en mole par litre.",
        "{f_ko.4}Pourquoi ? L'unité se reconstruit encore : lambda égale sigma sur la concentration, des siemens par mètre divisés par des moles par mètre cube : "
        "des siemens mètre carré par mole. C'est cette unité qui impose les moles par mètre cube.",
        "{-f_ko}{pq_add}Pourquoi les contributions s'additionnent-elles ? {pq_add.1}Parce que chaque ion transporte sa charge indépendamment des autres. "
        "Le courant total est la somme des courants portés par chaque espèce, comme le débit d'une autoroute est la somme des débits de ses voies.",
        "{pq_add.2}Et c'est aussi la limite du modèle : il suppose que les ions s'ignorent. Quand ils se rapprochent, chacun s'entoure d'un nuage d'ions de charge opposée qui le retient. "
        "Sa contribution diminue, et sigma croît moins vite que la concentration. La loi ne tient qu'en solution diluée.",
        "{-pq_add}{relais}Et pourquoi l'ion oxonium conduit-il si bien ? {relais.1}Un ion sodium doit traverser la solution en écartant les molécules d'eau : c'est lent. "
        "{relais.2}L'ion oxonium, lui, passe simplement son proton à la molécule d'eau voisine, qui devient à son tour un ion oxonium, et recommence. "
        "La charge progresse par relais, sans qu'aucun atome ne fasse vraiment le trajet, comme une ola dans un stade. "
        "{relais.3}Même chose pour l'ion hydroxyde. Leurs conductivités molaires sont deux à cinq fois plus grandes que celles des autres ions : "
        "les solutions acides ou basiques conduisent remarquablement bien.",
        "{-relais}{f_nacl}Deux cas à savoir écrire. {f_nacl.1}Le chlorure de sodium, de concentration c : un ion sodium et un ion chlorure, chacun à la concentration c. "
        "{f_nacl.2}Sigma égale c fois, lambda sodium plus lambda chlorure. La conductivité est proportionnelle à la concentration : le dosage par étalonnage est possible.",
        "{f_nacl.3}Le cas piégeux : le chlorure de magnésium, M g C l deux. Sa dissolution libère un ion magnésium, mais deux ions chlorure. "
        "La concentration en chlorure vaut donc deux c. {f_nacl.4}Sigma égale c fois, lambda magnésium plus deux lambda chlorure. "
        "Le deux se place devant le lambda de l'ion concerné, jamais ailleurs.",
        "{-f_nacl}{ex_soude}Un calcul complet. Une solution d'hydroxyde de sodium à zéro virgule deux cents mole par litre. "
        "Lambda sodium vaut cinq virgule zéro un fois dix puissance moins trois, lambda hydroxyde dix-neuf virgule huit fois dix puissance moins trois, en siemens mètre carré par mole. "
        "{ex_soude.1}Premier réflexe : convertir. Zéro virgule deux cents mole par litre, c'est deux cents moles par mètre cube. "
        "{ex_soude.2}Sigma égale deux cents, fois la somme des lambda, vingt-quatre virgule huit fois dix puissance moins trois. "
        "{ex_soude.3}On trouve quatre virgule quatre-vingt-seize siemens par mètre.",
        "{ex_soude.4}Sans la conversion, on trouverait mille fois moins : la valeur d'une eau presque pure. C'est de loin l'erreur la plus fréquente du chapitre.",
        "{-ex_soude}{gr_tp3}Et le dosage, dans le TP trois. Une lessive aux cristaux de soude, de l'hydrogénocarbonate de sodium, diluée dix fois. "
        "La notice demande vingt grammes par litre pour un sol intérieur. {gr_tp3.1}Voici les quatre étalons. "
        "{gr_tp3.2}La droite passe par l'origine, mais le point le plus concentré s'écarte vers le bas : c'est exactement la limite de Kohlrausch. "
        "On retient la pente sur la partie fiable : quatre-vingt-deux millisiemens par centimètre, par mole par litre. "
        "{gr_tp3.3}L'échantillon mesure deux virgule dix millisiemens par centimètre.",
        "{-gr_tp3}{ex_tp3}{ex_tp3.1}On divise : c égale sigma sur k, deux virgule dix sur quatre-vingt-deux : deux virgule six fois dix puissance moins deux mole par litre. "
        "{ex_tp3.2}On remonte la dilution : fois dix, zéro virgule vingt-six mole par litre. "
        "{ex_tp3.3}En masse, avec une masse molaire de quatre-vingt-quatre grammes par mole : environ vingt-deux grammes par litre.",
        "{ex_tp3.4}Très proche des vingt grammes par litre recommandés : la solution convenait au sol de la cantine. "
        "Oublier le facteur dix, c'est répondre deux virgule deux grammes par litre, et se tromper de conclusion.",
        "{-ex_tp3}",
    ], vis={
        "an_k": dict(type="anim", nom="conductivite", x=40, y=72, h=624, seg=[[40.5, 52.4], [52.4, 63], [63, 74]]),
        "k_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "HCl à la même concentration : I plus de 3 fois plus fort", "σ = Σ λ_i [X_i] : les contributions s'additionnent",
            "Fortes concentrations : la droite se courbe"]),
        "f_ko": dict(type="formule", titre="La loi de Kohlrausch", x=150, y=100, w=980, lignes=[
            dict(f="σ = Σ λ_i × [X_i]", cadre=True, taille=58),
            dict(f="λ_i : conductivité molaire ionique, en S·m^2·mol^-1 (tabulée)", txt=True),
            dict(f="[X_i] en mol·m^-3 · σ en S·m^-1", txt=True, pt=True),
            dict(f="λ = " + fr("σ", "[X]") + " → " + fr("S·m^-1", "mol·m^-3") + " = S·m^2·mol^-1", taille=34)]),
        "pq_add": dict(type="liste", titre="Pourquoi on additionne", items=[
            "Chaque ion transporte sa charge indépendamment : les courants s'ajoutent",
            "Limite : en solution concentrée, les ions se gênent, σ croît moins vite que c"], marques=["+", "!"], x=150, y=190, w=980),
        "relais": dict(type="liste", titre="H₃O⁺ et HO⁻ conduisent par relais", items=[
            "Na⁺ traverse la solution en écartant les molécules d'eau : lent",
            "H₃O⁺ passe son proton à la molécule d'eau voisine : la charge avance par relais",
            "λ(H₃O⁺) et λ(HO⁻) : 2 à 5 fois plus grands que les autres"], x=150, y=170, w=980),
        "f_nacl": dict(type="formule", titre="Écrire la loi pour un soluté", x=150, y=100, w=980, lignes=[
            dict(f="NaCl : [Na^+] = [Cl^-] = c", taille=38),
            dict(f="σ = c × (λ_{Na^+} + λ_{Cl^-})", cadre=True, taille=42),
            dict(f="MgCl_2 : [Mg^{2+}] = c  et  [Cl^-] = 2c", taille=38),
            dict(f="σ = c × (λ_{Mg^{2+}} + 2 λ_{Cl^-})", cadre=True, taille=42)]),
        "ex_soude": dict(type="formule", titre="Exemple · soude à 0,200 mol·L^-1", x=150, y=100, w=980, lignes=[
            dict(f="c = 0,200 mol·L^-1 = 0,200 × 10^3 = 2,00 × 10^2 mol·m^-3"),
            dict(f="σ = 2,00 × 10^2 × (5,01 + 19,8) × 10^-3", n="λ(Na⁺) = 5,01 × 10⁻³ · λ(HO⁻) = 19,8 × 10⁻³ S·m²·mol⁻¹"),
            dict(f="σ = 4,96 S·m^-1", cadre=True),
            dict(f="sans conversion : 4,96 × 10^-3 S·m^-1, mille fois trop petit", ko=True, taille=32)]),
        "gr_tp3": dict(type="graphe", titre="TP 3 · étalonnage conductimétrique (NaHCO₃)", x=330, y=110, w=640, h=520,
                       ax=dict(x=[0, 0.11], y=[0, 9], gx=[0.02, 0.04, 0.06, 0.08, 0.10], gy=[2, 4, 6, 8], lx="C (mol·L^-1)", ly="σ (mS·cm^-1)"),
                       el=[dict(type="points", pts=TP3, c="#5aa9ff", pas=.2),
                           dict(type="droite", pts=[[0, 0], [0.11, 9.02]], c="#5aa9ff", tir=True, ep=2.4, lbl="pente k ≈ 82", lp=[0.062, 6.6]),
                           dict(type="point", x=0.0256, y=2.10, c="sa", proj=True, lbl="Saint-Marc /10 : 2,10", lp=[0.036, 2.3])]),
        "ex_tp3": dict(type="formule", titre="TP 3 · la lessive diluée dix fois", x=150, y=110, w=980, lignes=[
            dict(f="C = " + fr("σ", "k") + " = " + fr("2,10", "82") + " = 2,6 × 10^-2 mol·L^-1"),
            dict(f="C_0 = 10 × 2,6 × 10^-2 = 0,26 mol·L^-1", n="on remonte la dilution"),
            dict(f="c_m = C_0 × M = 0,26 × 84,0 ≈ 22 g·L^-1", cadre=True),
            dict(f="≈ 20 g·L^-1 recommandés : adaptée au sol intérieur", ok=True, taille=32)]),
    }),

    # ================================================================ VIII. unités
    dict(id="unites", chap="Les unités sans piège", fond="aube", humeur="calme",
         retenir="1 mol·L⁻¹ = 10³ mol·m⁻³ · 1 mmol·L⁻¹ = 1 mol·m⁻³ · 1 cm² = 10⁻⁴ m² · 1 mS·cm⁻¹ = 0,1 S·m⁻¹. Écrire les unités avant les nombres.",
         beats=[
        "{sys}Le point qui fait perdre le plus de points dans ce chapitre, ce sont les unités. Parce qu'il mélange deux systèmes incompatibles. "
        "{sys.g}Côté Beer-Lambert, les unités de la paillasse : la cuve en centimètres, la concentration en mole par litre. C'est ce qu'impose le tableau des epsilon. "
        "{sys.d}Côté Kohlrausch, le système international : les distances en mètres, la concentration en mole par mètre cube. C'est ce qu'impose le tableau des lambda.",
        "Le réflexe : regarde d'abord l'unité des données tabulées. Elle te dit dans quel système travailler.",
        "{-sys}{conv}Quatre conversions, et pourquoi elles valent ça. "
        "{conv.1}Une mole par litre égale mille moles par mètre cube, parce qu'un mètre cube contient mille litres. "
        "{conv.2}Une millimole par litre égale une mole par mètre cube : les deux facteurs mille se compensent. Une concentration en millimoles par litre est déjà prête pour Kohlrausch. "
        "{conv.3}Un centimètre carré égale dix puissance moins quatre mètre carré : le dix puissance moins deux de la longueur est élevé au carré. "
        "Écrire dix puissance moins deux, c'est se tromper d'un facteur cent. "
        "{conv.4}Et un millisiemens par centimètre égale zéro virgule un siemens par mètre : dix puissance moins trois divisé par dix puissance moins deux. "
        "Les deux préfixes ne se simplifient pas : ils se divisent.",
        "{-conv}{methode}Voici la méthode qui rend toute erreur d'unité impossible. "
        "{methode.1}Un : écris la formule sans aucun nombre. "
        "{methode.2}Deux : sous chaque symbole, écris son unité, telle qu'elle est donnée dans l'énoncé. "
        "{methode.3}Trois : simplifie les unités seules. Si tu n'obtiens pas l'unité attendue, arrête-toi : une conversion manque. "
        "{methode.4}Quatre : seulement ensuite, remplace par les nombres.",
        "{-methode}{ex_u}Sur l'exemple de la soude. {ex_u.1}Concentration en mole par litre, fois lambda en siemens mètre carré par mole : "
        "on obtient des siemens mètre carré par litre. Ce n'est pas des siemens par mètre ! On voit l'erreur avant d'avoir touché à la calculatrice. "
        "{ex_u.2}Avec des moles par mètre cube, on obtient bien des siemens par mètre. On peut calculer.",
        "{-ex_u}{deux_sig}Un dernier piège de notation. {deux_sig.1}Dans ce chapitre, la lettre sigma désigne deux choses sans aucun rapport : "
        "la conductivité, en siemens par mètre, et, en infrarouge, le nombre d'onde, en centimètres moins un. Le contexte tranche : une solution ionique d'un côté, un spectre de l'autre.",
        "{-deux_sig}",
    ], vis={
        "sys": dict(type="cols", g="Beer-Lambert", gq="unités de paillasse · ℓ en cm · c en mol·L⁻¹ · imposées par ε",
                    d="Kohlrausch", dq="unités SI · L en m · [X] en mol·m⁻³ · imposées par λ", vs="≠",
                    repere="Regarde d'abord l'unité des données tabulées"),
        "conv": dict(type="liste", titre="Les quatre conversions", items=[
            "1 mol·L⁻¹ = 10³ mol·m⁻³ : 1 m³ = 1 000 L", "1 mmol·L⁻¹ = 1 mol·m⁻³ : les facteurs mille se compensent",
            "1 cm² = 10⁻⁴ m² : (10⁻²)², pas 10⁻²", "1 mS·cm⁻¹ = 10⁻³ S / 10⁻² m = 0,1 S·m⁻¹"], x=150, y=150, w=980),
        "methode": dict(type="liste", titre="La méthode en quatre temps", items=[
            "Écrire la formule sans nombres", "Écrire sous chaque symbole l'unité de l'énoncé",
            "Simplifier les unités seules : sinon, une conversion manque", "Seulement ensuite, les nombres"],
                        marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "ex_u": dict(type="formule", titre="Contrôle des unités · σ = c × (λ₊ + λ₋)", x=150, y=170, w=980, lignes=[
            dict(f="mol·L^-1 × S·m^2·mol^-1 = S·m^2·L^-1  ✗", ko=True, n="ce n'est pas des S·m⁻¹ : une conversion manque"),
            dict(f="mol·m^-3 × S·m^2·mol^-1 = S·m^-1  ✓", ok=True)]),
        "deux_sig": dict(type="note", titre="Deux σ dans le même chapitre", cles=["conductivité", "nombre"],
                         t="σ conductivité, en S·m⁻¹ · σ nombre d'onde en infrarouge, en cm⁻¹. Aucun rapport : le contexte tranche.",
                         x=170, y=210, w=940),
    }),

    # ================================================================ IX. infrarouge
    dict(id="infrarouge", chap="La spectroscopie infrarouge", fond="nuit", humeur="mystere",
         retenir="σ = 1/λ en cm⁻¹, axe de 4000 à 500. O—H alcool 3200-3600 large ; O—H acide 2500-3200 très large ; N—H 3300-3500 ; C=O 1700-1750 fine et intense. On identifie des groupes, pas des molécules.",
         beats=[
        "{ir_but}Dernière technique du chapitre. L'infrarouge ne sert pas à doser, mais à identifier : il révèle quels groupes caractéristiques une molécule contient.",
        "{-ir_but}{vib}Que fait le rayonnement infrarouge ? {vib.1}Il fait vibrer les liaisons. Une liaison peut s'allonger et se raccourcir : c'est une vibration d'élongation. "
        "{vib.2}Ou changer d'angle avec sa voisine : c'est une déformation. Chaque type de liaison absorbe à des fréquences qui lui sont propres.",
        "{-vib}{ressort}Pourquoi une fréquence précise ? Parce qu'une liaison se comporte comme un ressort qui relie deux masses. "
        "Un ressort a une fréquence propre. Quand l'infrarouge arrive exactement à cette fréquence, il y a résonance : la liaison absorbe, et vibre plus fort. "
        "{ressort.1}Et cette fréquence dépend de deux choses. La raideur : une double liaison C O, plus raide, absorbe vers mille sept cents ; une simple liaison C O, plus souple, bien plus bas. "
        "{ressort.2}La masse : l'hydrogène est l'atome le plus léger. Toutes les liaisons avec un hydrogène, O H, N H, C H, se retrouvent en haut du spectre, au-dessus de deux mille huit cents.",
        "{-ressort}{f_sw}{f_sw.1}En infrarouge, l'axe horizontal ne porte pas la longueur d'onde, mais le nombre d'onde, encore noté sigma : sigma égale un sur lambda, en centimètres moins un. "
        "{f_sw.2}L'axe se lit de droite à gauche, de quatre mille à cinq cents. "
        "{f_sw.3}Pourquoi ce choix ? Parce que le nombre d'onde est proportionnel à l'énergie du rayonnement. À gauche, les liaisons raides et légères ; à droite, les vibrations molles.",
        "{f_sw.4}Et souvent, l'axe vertical est la transmittance : les bandes d'absorption pointent vers le bas. Moins la lumière passe, plus la liaison absorbe. "
        "Regarde toujours l'étiquette de l'axe avant d'interpréter.",
        "{-f_sw}{table}Voici la table des bandes, à savoir exploiter. "
        "{table.1}O H d'un alcool : entre trois mille deux cents et trois mille six cents, forte et large. "
        "{table.2}O H d'un acide carboxylique : entre deux mille cinq cents et trois mille deux cents, très large, étalée. "
        "{table.3}N H, d'une amine ou d'un amide : entre trois mille trois cents et trois mille cinq cents, moyenne. Une bande pour N H, deux pour N H deux. "
        "{table.4}C H : entre deux mille huit cents et trois mille, présente presque partout, donc peu utile. "
        "{table.5}Et C double liaison O : entre mille sept cents et mille sept cent cinquante, forte et fine.",
        "{-table}{gr_ir}Regardons trois spectres schématisés. {gr_ir.1}L'éthanol, un alcool : une bande large et profonde vers trois mille trois cent cinquante. Pas de bande vers mille sept cents.",
        "{gr_ir.2}L'acide éthanoïque : une bande O H énorme, qui s'étale jusqu'à deux mille cinq cents, au point d'avaler les bandes C H. Et une bande fine et intense vers mille sept cent quinze.",
        "{gr_ir.3}La propanone, une cétone : pas de O H du tout. Seulement la bande fine du C double liaison O, vers mille sept cent quinze.",
        "{-gr_ir}{large}Pourquoi la bande O H est-elle large, et celle du C O fine ? {large.1}Les groupes O H forment des liaisons hydrogène entre eux. "
        "Chacun se retrouve dans un environnement un peu différent, plus ou moins assoupli, et vibre à une fréquence un peu différente. Au lieu d'une fréquence unique, une distribution : la bande s'étale. "
        "{large.2}Le C O, lui, ne forme pas de liaison hydrogène par lui-même : tous vibrent à la même fréquence, d'où une bande étroite. "
        "{large.3}Et les acides s'associent deux par deux par une double liaison hydrogène très solide : leur bande O H est encore plus large.",
        "{-large}{lire}La méthode pour lire un spectre, en trois questions. "
        "{lire.1}Un : y a-t-il une bande large entre trois mille et trois mille six cents ? Si oui, il y a un O H. "
        "{lire.2}Deux : y a-t-il une bande fine et intense vers mille sept cents ? Si oui, il y a un C double liaison O. "
        "{lire.3}Trois : croise les deux. O H large et C O : acide carboxylique. C O seul : aldéhyde ou cétone. O H seul : alcool.",
        "{-lire}{groupes}Et une précision qui compte dans la rédaction. {groupes.1}L'infrarouge identifie des groupes, pas des molécules. "
        "Deux molécules de la même famille ont des spectres très semblables ; ce qui les distingue est la zone sous mille cinq cents, l'empreinte digitale, trop complexe à lire à la main. "
        "On conclut donc : ce spectre présente un groupe hydroxyle. Pas : c'est du propan-un-ol. Sauf si l'énoncé donne une liste fermée de candidats.",
        "{-groupes}{entite}Pour finir le cours, une question : pourquoi le visible renseigne-t-il sur les électrons, et l'infrarouge sur les liaisons ? "
        "Parce qu'une onde ne perturbe efficacement qu'une entité de taille comparable à sa longueur d'onde. "
        "Comme la houle : des vaguelettes passent sous un chalutier sans le déranger, une houle immense le soulève en bloc, et ce sont les vagues de sa taille qui le secouent.",
        "{entite.1}Les rayons gamma agissent sur les noyaux. {entite.2}L'ultraviolet et le visible, sur les électrons des molécules : ce sont les transitions électroniques, et la couleur. "
        "{entite.3}L'infrarouge, sur les liaisons, qu'il fait vibrer.",
        "{-entite}",
    ], vis={
        "ir_but": dict(type="mot", t="Identifier", g="l'infrarouge révèle les groupes caractéristiques d'une molécule", y=240),
        "vib": dict(type="liste", titre="L'infrarouge fait vibrer les liaisons", items=[
            "Élongation : la liaison s'allonge et se raccourcit", "Déformation : l'angle entre deux liaisons change"], x=150, y=200, w=980),
        "ressort": dict(type="liste", titre="Une liaison, un ressort entre deux masses", items=[
            "Liaison plus raide → fréquence plus élevée : C=O vers 1 700 cm⁻¹, C—O bien plus bas",
            "Atomes plus légers → vibration plus rapide : O—H, N—H, C—H au-dessus de 2 800 cm⁻¹"], x=150, y=190, w=980),
        "f_sw": dict(type="formule", titre="Le nombre d'onde", x=150, y=110, w=980, lignes=[
            dict(f="σ = " + fr("1", "λ") + "   en cm^-1", cadre=True, taille=52),
            dict(f="axe lu de 4 000 à 500 cm^-1, de gauche à droite", txt=True),
            dict(f="σ proportionnel à l'énergie : à gauche, liaisons raides et légères", txt=True, pt=True),
            dict(f="en transmittance, les bandes pointent vers le bas", txt=True, pt=True)]),
        "table": dict(type="liste", titre="La table des bandes", items=[
            "O—H alcool : 3 200 – 3 600 cm⁻¹, forte et large", "O—H acide carboxylique : 2 500 – 3 200, très large",
            "N—H : 3 300 – 3 500 ; une bande pour N—H, deux pour NH₂", "C—H : 2 800 – 3 000, presque partout",
            "C=O : 1 700 – 1 750, forte et fine"], x=150, y=120, w=980),
        "gr_ir": dict(type="graphe", titre="Spectres IR schématisés (transmittance)", x=250, y=100, w=780, h=540,
                      ax=dict(x=[4000, 500], y=[0, 100], gx=[4000, 3000, 2000, 1500, 1000, 500], gy=[25, 50, 75, 100],
                              lx="σ (cm^-1)", ly="T (%)"),
                      el=[dict(type="courbe", pts=IR_ETHANOL, c="#5aa9ff", lbl="éthanol · O—H large", lp=[3350, 22], fin="2", dur=2.4),
                          dict(type="courbe", pts=IR_ACIDE, c="sa", lbl="acide éthanoïque · O—H très large + C=O", lp=[2600, 26], fin="3", dur=2.4),
                          dict(type="courbe", pts=IR_PROPANONE, c="#7ce08a", lbl="propanone · C=O seul", lp=[1900, 8], dur=2.4)]),
        "large": dict(type="liste", titre="Large ou fine ?", items=[
            "O—H : liaisons hydrogène, environnements variés → bande large",
            "C=O : pas de liaison hydrogène par lui-même → bande fine",
            "Acide : associé deux par deux → O—H encore plus large"], x=150, y=170, w=980),
        "lire": dict(type="liste", titre="Lire un spectre en trois questions", items=[
            "Bande large vers 3 000 – 3 600 ? → un O—H", "Bande fine et intense vers 1 700 ? → un C=O",
            "Croiser : O—H + C=O = acide · C=O seul = aldéhyde ou cétone · O—H seul = alcool"],
                     marques=["1", "2", "3"], x=150, y=170, w=980),
        "groupes": dict(type="note", titre="Des groupes, pas des molécules", cles=["groupes", "hydroxyle"],
                        t="Conclure « ce spectre présente un groupe hydroxyle », pas « c'est du propan-1-ol », sauf liste fermée de candidats.",
                        x=170, y=200, w=940),
        "entite": dict(type="liste", titre="Quelle onde pour quelle entité", items=[
            "Rayons γ : le noyau (≈ 10⁻¹⁵ m)", "UV-visible : les électrons des molécules → la couleur",
            "Infrarouge : les liaisons → élongations, déformations"], x=150, y=180, w=980),
    }),

    # ================================================================ X. exercice 1 (simple)
    # λmax = 540 nm (vert) → pourpre ; ε = 3,0e4 ; A = 0,45 ; ℓ = 1,0 cm : c = 0,45 / 3,0e4 = 1,5e-5 mol/L ;
    # M = 500 g/mol : cm = 7,5e-3 g/L = 7,5 mg/L ; cuve de 2,0 cm : A = 0,90
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. Un colorant alimentaire présente un maximum d'absorption à cinq cent quarante nanomètres. "
        "Son coefficient d'absorption molaire à cette longueur d'onde vaut trois virgule zéro fois dix puissance quatre litres par mole par centimètre, "
        "et sa masse molaire cinq cents grammes par mole. Une boisson diluée donne, en cuve d'un centimètre, une absorbance de zéro virgule quarante-cinq.",
        "Cinq questions : la couleur de la boisson ; pourquoi mesurer à cinq cent quarante nanomètres ; la concentration molaire ; "
        "la concentration en masse, en milligrammes par litre ; et l'absorbance dans une cuve de deux centimètres.",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}C'est parti pour la correction. {s11}{s11.1}Question un : cinq cent quarante nanomètres, c'est du vert. "
        "{s11.2}La solution absorbe le vert, et on voit sa couleur complémentaire : elle paraît pourpre.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux, les deux raisons, toujours. La sensibilité est maximale au maximum d'absorption. "
        "{s12.2}Et la courbe y est plate : une petite erreur de réglage de la longueur d'onde ne change presque rien.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : A égale epsilon l c, donc c égale A sur epsilon fois l. "
        "{s13.2}Zéro virgule quarante-cinq, divisé par trois virgule zéro fois dix puissance quatre, fois un. "
        "{s13.3}Un virgule cinq fois dix puissance moins cinq mole par litre. Vérifie les unités : tout se simplifie, il reste des moles par litre.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre : la concentration en masse vaut c fois M. "
        "{s14.2}Un virgule cinq fois dix puissance moins cinq, fois cinq cents : sept virgule cinq fois dix puissance moins trois gramme par litre. "
        "{s14.3}Soit sept virgule cinq milligrammes par litre.",
        "{-s14}{ex1c.q5}{s15}{s15.1}Question cinq : l'absorbance est proportionnelle à l. La cuve est deux fois plus longue : "
        "{s15.2}l'absorbance double, zéro virgule quatre-vingt-dix. Toujours sous deux virgule cinq : la mesure reste valable.",
        "{-s15}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="Le colorant d'une boisson", src="Exercice inventé pour la vidéo",
                    enonce=["Un colorant alimentaire a son maximum d'absorption à λ_{max} = 540 nm. Une boisson diluée, placée dans une cuve de 1,0 cm, "
                            "a une absorbance A = 0,45 à cette longueur d'onde."],
                    donnees=["ε(540 nm) = 3,0 × 10^4 L·mol^-1·cm^-1", "M = 500 g·mol^-1", "ℓ = 1,0 cm"],
                    questions=["De quelle couleur est la boisson ?", "Pourquoi mesurer à 540 nm ?", "Calculer la concentration molaire c.",
                               "En déduire la concentration en masse, en mg·L⁻¹.", "Quelle absorbance dans une cuve de 2,0 cm ?"]),
        "pa1": dict(type="pause", t="Couleur, choix de λ, concentration molaire et en masse, cuve de 2,0 cm."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="Le colorant d'une boisson",
                     donnees=["λ_{max} = 540 nm", "ε = 3,0 × 10^4", "A = 0,45", "M = 500 g·mol^-1"],
                     questions=["Couleur ?", "Pourquoi 540 nm ?", "c ?", "c_m en mg·L⁻¹ ?", "A en cuve de 2,0 cm ?"]),
        "s11": dict(type="formule", titre="1 · La couleur", x=540, y=180, w=700, lignes=[
            dict(f="540 nm : vert, absorbé", taille=40), dict(f="couleur perçue : pourpre", cadre=True, taille=40)]),
        "s12": dict(type="formule", titre="2 · Pourquoi λ_{max}", x=540, y=170, w=700, lignes=[
            dict(f="sensibilité maximale", taille=40, ok=True), dict(f="courbe plate : erreur sur λ sans effet", taille=34, ok=True)]),
        "s13": dict(type="formule", titre="3 · La concentration molaire", x=540, y=150, w=700, lignes=[
            dict(f="c = " + fr("A", "ε × ℓ"), taille=40), dict(f="c = " + fr("0,45", "3,0 × 10^4 × 1,0"), taille=40),
            dict(f="c = 1,5 × 10^-5 mol·L^-1", cadre=True, taille=40)]),
        "s14": dict(type="formule", titre="4 · La concentration en masse", x=540, y=150, w=700, lignes=[
            dict(f="c_m = c × M", taille=40), dict(f="c_m = 1,5 × 10^-5 × 500 = 7,5 × 10^-3 g·L^-1", taille=32),
            dict(f="c_m = 7,5 mg·L^-1", cadre=True, taille=40)]),
        "s15": dict(type="formule", titre="5 · Une cuve de 2,0 cm", x=540, y=170, w=700, lignes=[
            dict(f="A ∝ ℓ : ℓ × 2  ⇒  A × 2", taille=40), dict(f="A = 0,90 (< 2,5 : valable)", cadre=True, taille=40)]),
    }),

    # ================================================================ XI. exercice 2 (difficile)
    # CaCl2 à 2,0 mmol/L : [Ca2+] = 2,0 mol/m³, [Cl-] = 4,0 mol/m³ ; λ(Ca2+) = 11,9e-3, λ(Cl-) = 7,63e-3 S·m²/mol
    # σ = 11,9e-3 × 2,0 + 7,63e-3 × 4,0 = 0,0238 + 0,0305 = 0,0543 S/m ; K = 1,0e-2 / 1,0e-4 = 100 m-1 ; G = σ/K = 5,4e-4 S
    # affichage : 0,0543 S/m = 0,543 mS/cm ; oubli du 2 : 2,0 × 19,5e-3 = 3,9e-2 S/m ; σ = 0,136 → c = 0,136 / 27,16e-3 = 5,0 mol/m³
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile : il croise conductance, conductivité, Kohlrausch et unités. "
        "On étudie une solution de chlorure de calcium, C a C l deux, à deux virgule zéro millimoles par litre. "
        "La cellule du conductimètre a deux plaques d'un centimètre carré, distantes d'un centimètre.",
        "On demande : les concentrations des ions en moles par mètre cube ; la conductivité de la solution ; la conductance mesurée ; "
        "la valeur affichée en millisiemens par centimètre ; l'erreur commise si l'on oublie un coefficient ; "
        "et enfin, la concentration d'une autre solution de chlorure de calcium, de conductivité zéro virgule cent trente-six siemens par mètre.",
        "{-ex2}{pa2}Celui-là demande du soin, surtout avec les unités. Mets sur pause, et fais-le en entier.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un. La dissolution libère un ion calcium et deux ions chlorure. "
        "{s21.2}Deux virgule zéro millimoles par litre, c'est deux virgule zéro moles par mètre cube : les facteurs mille se compensent. "
        "{s21.3}Donc calcium : deux virgule zéro moles par mètre cube ; chlorure : le double, quatre virgule zéro.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux, Kohlrausch : sigma égale lambda calcium fois sa concentration, plus lambda chlorure fois la sienne. "
        "{s22.2}Onze virgule neuf fois dix puissance moins trois, fois deux, plus sept virgule soixante-trois fois dix puissance moins trois, fois quatre. "
        "{s22.3}Cinq virgule quatre fois dix puissance moins deux siemens par mètre.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois. La constante de cellule vaut L sur S. En mètres : dix puissance moins deux, divisé par dix puissance moins quatre. "
        "{s23.2}K égale cent mètres moins un. {s23.3}Et G égale sigma sur K : cinq virgule quatre fois dix puissance moins quatre siemens, "
        "soit zéro virgule cinquante-quatre millisiemens.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre. Un millisiemens par centimètre vaut zéro virgule un siemens par mètre. "
        "{s24.2}Donc zéro virgule zéro cinq quatre trois siemens par mètre, divisé par zéro virgule un : l'appareil affiche zéro virgule cinquante-quatre millisiemens par centimètre.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq. Si on oublie le deux devant lambda chlorure, on calcule deux fois la somme des lambda : "
        "trois virgule neuf fois dix puissance moins deux siemens par mètre. Près de trente pour cent trop bas. "
        "{s25.2}Et si on garde la concentration en moles par litre ? Mille fois trop petit. Les deux erreurs classiques du chapitre.",
        "{-s25}{ex2c.q6}{s26}{s26.1}Question six. Pour le chlorure de calcium, sigma égale c fois, lambda calcium plus deux lambda chlorure. "
        "{s26.2}Donc c égale sigma divisé par cette somme : zéro virgule cent trente-six, sur vingt-sept virgule deux fois dix puissance moins trois. "
        "{s26.3}Cinq virgule zéro moles par mètre cube, soit cinq virgule zéro millimoles par litre. "
        "La solution reste diluée : la loi de Kohlrausch s'applique.",
        "{-s26}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=60, titre="Le chlorure de calcium", src="Exercice inventé pour la vidéo",
                    enonce=["Une solution de chlorure de calcium CaCl₂ a une concentration c = 2,0 mmol·L⁻¹. La cellule du conductimètre "
                            "comporte deux plaques de surface S = 1,0 cm², distantes de L = 1,0 cm."],
                    donnees=["λ(Ca^{2+}) = 11,9 × 10^-3 S·m^2·mol^-1", "λ(Cl^-) = 7,63 × 10^-3 S·m^2·mol^-1"],
                    questions=["Concentrations des ions, en mol·m⁻³.", "Conductivité σ de la solution.", "Constante de cellule K et conductance G.",
                               "Valeur affichée en mS·cm⁻¹.", "Erreur si l'on oublie le coefficient 2, ou la conversion ?",
                               "Concentration d'une solution de CaCl₂ de conductivité σ' = 0,136 S·m⁻¹."]),
        "pa2": dict(type="pause", t="Concentrations des ions, σ, K et G, affichage, erreurs classiques, concentration inconnue."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Le chlorure de calcium",
                     donnees=["c = 2,0 mmol·L^-1", "S = 1,0 cm²", "L = 1,0 cm", "λ(Ca²⁺) = 11,9 · λ(Cl⁻) = 7,63 (× 10⁻³)"],
                     questions=["[Ca²⁺], [Cl⁻] ?", "σ ?", "K et G ?", "Affichage ?", "Erreurs ?", "c pour σ' = 0,136 ?"]),
        "s21": dict(type="formule", titre="1 · Les concentrations des ions", x=540, y=140, w=700, lignes=[
            dict(f="CaCl_2 → Ca^{2+} + 2 Cl^-", taille=38),
            dict(f="c = 2,0 mmol·L^-1 = 2,0 mol·m^-3", taille=38),
            dict(f="[Ca^{2+}] = 2,0 · [Cl^-] = 4,0 mol·m^-3", cadre=True, taille=34)]),
        "s22": dict(type="formule", titre="2 · La conductivité", x=540, y=140, w=700, lignes=[
            dict(f="σ = λ_{Ca^{2+}}[Ca^{2+}] + λ_{Cl^-}[Cl^-]", taille=34),
            dict(f="σ = 11,9 × 10^-3 × 2,0 + 7,63 × 10^-3 × 4,0", taille=32),
            dict(f="σ = 5,4 × 10^-2 S·m^-1", cadre=True, taille=38)]),
        "s23": dict(type="formule", titre="3 · Constante de cellule et conductance", x=540, y=130, w=700, lignes=[
            dict(f="K = " + fr("L", "S") + " = " + fr("1,0 × 10^-2 m", "1,0 × 10^-4 m^2"), taille=34),
            dict(f="K = 1,0 × 10^2 m^-1", taille=38),
            dict(f="G = " + fr("σ", "K") + " = 5,4 × 10^-4 S = 0,54 mS", cadre=True, taille=34)]),
        "s24": dict(type="formule", titre="4 · L'affichage", x=540, y=170, w=700, lignes=[
            dict(f="1 mS·cm^-1 = 0,1 S·m^-1", taille=38),
            dict(f="σ = " + fr("0,0543", "0,1") + " = 0,54 mS·cm^-1", cadre=True, taille=38)]),
        "s25": dict(type="formule", titre="5 · Les deux erreurs classiques", x=540, y=150, w=700, lignes=[
            dict(f="oubli du 2 : 2,0 × (11,9 + 7,63) × 10^-3 = 3,9 × 10^-2 S·m^-1", ko=True, taille=28, n="près de 30 % trop bas"),
            dict(f="c en mol·L^-1 : résultat 1 000 fois trop petit", ko=True, taille=30)]),
        "s26": dict(type="formule", titre="6 · La concentration inconnue", x=540, y=130, w=700, lignes=[
            dict(f="σ' = c × (λ_{Ca^{2+}} + 2 λ_{Cl^-})", taille=34),
            dict(f="c = " + fr("0,136", "(11,9 + 2 × 7,63) × 10^-3") + " = " + fr("0,136", "27,2 × 10^-3"), taille=30),
            dict(f="c = 5,0 mol·m^-3 = 5,0 mmol·L^-1", cadre=True, taille=36)]),
    }),

    # ================================================================ XII. exercice 3 (type bac)
    # étalonnage à 630 nm (cuve 1,0 cm) : k ≈ 0,105 L·µmol⁻¹ (régression : 0,1049) ; sirop dilué 10 fois : A = 0,47
    # c = 0,47 / 0,105 = 4,48 ≈ 4,5 µmol/L ; sirop : 45 µmol/L = 4,5e-5 mol/L ; cm = 4,5e-5 × 583 = 2,6e-2 g/L = 26 mg/L
    # sirop pur : A ≈ 4,7 > 2,5 ; z = |26 − 25| / 1 = 1 ≤ 2 : compatible ; ε = 0,105 L/µmol/cm = 1,05e5 L/mol/cm
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac. Un sirop de menthe vert. Sa couleur vient de deux colorants : un jaune, qui absorbe vers quatre cent cinquante nanomètres, "
        "et un bleu, qui absorbe vers six cent trente. L'étiquette annonce vingt-cinq milligrammes par litre de colorant bleu. "
        "Un laboratoire veut le vérifier, et contrôler aussi l'arôme, qu'on soupçonne d'être de la menthone au lieu du menthol.",
        "{-ex3}{gr_ex3}{gr_ex3.1}Voici le document : la gamme d'étalons du colorant bleu, mesurée à six cent trente nanomètres, en cuve d'un centimètre. "
        "Le sirop, dilué dix fois, donne une absorbance de zéro virgule quarante-sept.",
        "{-gr_ex3}{ex3b}Sept questions. Un : pourquoi le sirop est-il vert ? Deux : pourquoi mesurer à six cent trente nanomètres ? "
        "Trois : pourquoi a-t-on dilué le sirop ? Quatre : déterminer la concentration en masse du colorant bleu dans le sirop. "
        "Cinq : le résultat est-il compatible avec l'étiquette, sachant que l'incertitude-type vaut un milligramme par litre ? "
        "Six : le spectre infrarouge de l'arôme montre une bande large vers trois mille trois cent cinquante, et aucune bande vers mille sept cents. Menthol ou menthone ? "
        "Sept : un regard critique sur la méthode.",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}{s31.1}Question un. Le colorant jaune absorbe le bleu, le colorant bleu absorbe l'orange-rouge. "
        "{s31.2}Ce qui n'est absorbé par aucun des deux, c'est le vert, au milieu du spectre : c'est lui qu'on voit.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Question deux. Six cent trente nanomètres, c'est le maximum d'absorption du colorant bleu : sensibilité maximale, et courbe plate. "
        "{s32.2}Et surtout ici : le colorant jaune n'absorbe pas à cette longueur d'onde. Sinon les absorbances s'additionneraient, et le dosage serait faussé.",
        "{-s32}{ex3c.q3}{s33}{s33.1}Question trois. Sans dilution, l'absorbance serait dix fois plus grande : environ quatre virgule sept. "
        "{s33.2}Bien au-delà de deux virgule cinq : l'appareil saturerait. Et elle sortirait de la gamme d'étalonnage, qui s'arrête vers zéro virgule quatre-vingt-quatre.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Question quatre. La droite passe par l'origine, de pente environ zéro virgule cent cinq litre par micromole. "
        "{s34.2}On divise : zéro virgule quarante-sept sur zéro virgule cent cinq, quatre virgule cinq micromoles par litre. Bien entre les étalons à quatre et à six. "
        "{s34.3}On remonte la dilution : quarante-cinq micromoles par litre dans le sirop. "
        "{s34.4}En masse : quatre virgule cinq fois dix puissance moins cinq, fois cinq cent quatre-vingt-trois, deux virgule six fois dix puissance moins deux gramme par litre. "
        "Vingt-six milligrammes par litre.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq. On compare l'écart à l'incertitude-type : vingt-six moins vingt-cinq, divisé par un. "
        "{s35.2}Un, c'est moins que deux : la valeur mesurée est compatible avec l'étiquette.",
        "{-s35}{ex3c.q6}{s36}{s36.1}Question six. Une bande large vers trois mille trois cent cinquante : un groupe O H, celui d'un alcool. "
        "{s36.2}Aucune bande fine vers mille sept cents : pas de C double liaison O. Or la menthone est une cétone, elle en aurait une. "
        "{s36.3}L'arôme est donc le menthol, un alcool. On peut conclure sur la molécule, parce que l'énoncé donne une liste fermée de deux candidats.",
        "{-s36}{ex3c.q7}{s37}{s37.1}Question sept, le regard critique, toujours valorisé. Les points sont bien alignés et passent par l'origine : le modèle est pertinent. "
        "{s37.2}La mesure est faite à l'intérieur de la gamme, sans extrapolation. "
        "{s37.3}Les incertitudes viennent de la dilution, des étalons, de la cuve et du blanc. "
        "{s37.4}Et on suppose qu'aucune autre espèce du sirop n'absorbe à six cent trente nanomètres : on pourrait le vérifier en traçant le spectre du sirop.",
        "{-s37}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Le sirop de menthe", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Un sirop de menthe vert contient un colorant jaune (λ_{max} ≈ 450 nm) et un colorant bleu (λ_{max} ≈ 630 nm, "
                            "le jaune n'y absorbe pas). L'étiquette annonce 25 mg·L⁻¹ de colorant bleu.",
                            "On soupçonne aussi que l'arôme est de la menthone (une cétone) au lieu du menthol (un alcool)."],
                    donnees=["M(colorant bleu) = 583 g·mol^-1", "sirop dilué 10 fois : A = 0,47 (630 nm, 1,0 cm)", "u(c_m) = 1 mg·L^-1"]),
        "gr_ex3": dict(type="graphe", titre="Document · étalonnage du colorant bleu à 630 nm", x=330, y=110, w=640, h=520,
                       ax=dict(x=[0, 9], y=[0, 1.0], gx=[2, 4, 6, 8], gy=[0.2, 0.4, 0.6, 0.8, 1.0], lx="c (µmol·L^-1)", ly="A"),
                       el=[dict(type="points", pts=EX3, c="#5aa9ff", pas=.15),
                           dict(type="droite", pts=[[0, 0], [9, 0.944]], c="#5aa9ff", ep=2.4, lbl="A = 0,105 × c", lp=[5.2, 0.75])]),
        "ex3b": dict(type="exo", niveau="bac", titre="Le sirop de menthe · questions",
                     questions=["Pourquoi le sirop est-il vert ?", "Pourquoi mesurer à 630 nm ?", "Pourquoi avoir dilué le sirop ?",
                                "Concentration en masse du colorant bleu dans le sirop.", "Compatible avec l'étiquette ?",
                                "IR : bande large vers 3 350 cm⁻¹, rien vers 1 700. Menthol ou menthone ?", "Regard critique sur la méthode."]),
        "pa3": dict(type="pause", t="Couleur, choix de λ, dilution, concentration, comparaison, infrarouge, regard critique."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Le sirop de menthe",
                     donnees=["A = 0,47 (dilué 10 fois)", "M = 583 g·mol^-1", "étiquette : 25 mg·L^-1", "u = 1 mg·L^-1"],
                     questions=["Vert ?", "630 nm ?", "Dilution ?", "c_m ?", "Compatible ?", "Menthol ?", "Critique ?"]),
        "s31": dict(type="liste", titre="1 · Pourquoi vert", items=[
            "Le jaune absorbe le bleu ; le bleu absorbe l'orange-rouge",
            "Le vert n'est absorbé par aucun des deux : on le voit"], x=540, y=180, w=700),
        "s32": dict(type="liste", titre="2 · Pourquoi 630 nm", items=[
            "λ_{max} du bleu : sensibilité maximale, courbe plate",
            "Le jaune n'y absorbe pas : pas d'absorbances qui s'additionnent"], x=540, y=180, w=700),
        "s33": dict(type="formule", titre="3 · Pourquoi diluer", x=540, y=170, w=700, lignes=[
            dict(f="sirop pur : A ≈ 10 × 0,47 ≈ 4,7", taille=38),
            dict(f="> 2,5 : saturation, et hors de la gamme (≤ 0,84)", ko=True, cadre=True, taille=32)]),
        "s34": dict(type="formule", titre="4 · La concentration en masse", x=540, y=110, w=700, lignes=[
            dict(f="c = " + fr("A", "k") + " = " + fr("0,47", "0,105") + " ≈ 4,5 µmol·L^-1", taille=34),
            dict(f="dans la gamme (entre 4,0 et 6,0) ✓", ok=True, taille=30),
            dict(f="sirop : c_0 = 10 × 4,5 = 45 µmol·L^-1", taille=34),
            dict(f="c_m = 4,5 × 10^-5 × 583 ≈ 26 mg·L^-1", cadre=True, taille=36)]),
        "s35": dict(type="formule", titre="5 · La comparaison", x=540, y=170, w=700, lignes=[
            dict(f=fr("|26 − 25|", "1") + " = 1", taille=42),
            dict(f="1 ≤ 2 : compatible avec l'étiquette", ok=True, cadre=True, taille=36)]),
        "s36": dict(type="liste", titre="6 · Menthol ou menthone", items=[
            "Bande large vers 3 350 cm⁻¹ : un O—H d'alcool", "Rien vers 1 700 : pas de C=O, donc pas la menthone (cétone)",
            "C'est le menthol (liste fermée de deux candidats)"], x=540, y=150, w=700),
        "s37": dict(type="liste", titre="7 · Regard critique", items=[
            "Points alignés, droite par l'origine : modèle pertinent", "Mesure dans la gamme : aucune extrapolation",
            "Incertitudes : dilution, étalons, cuve, blanc", "Autre espèce à 630 nm ? Tracer le spectre du sirop"], x=540, y=120, w=700, petit=True),
    }),

    # ================================================================ XIII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, une idée : mesurer sans détruire, avec une grandeur proportionnelle à la concentration. "
        "{carte.1}L'absorbance : A égale epsilon l c, et la saturation au-delà de deux virgule cinq. "
        "{carte.2}Le spectre : on mesure à lambda max, et la couleur perçue est la complémentaire de la couleur absorbée. "
        "{carte.3}La conductivité : sigma égale K fois G, et la loi de Kohlrausch, en moles par mètre cube. "
        "{carte.4}Et l'infrarouge : le nombre d'onde, et les bandes O H et C double liaison O.",
        "{-carte}{bac}Et voici les savoir-faire du plan de travail, à cocher. "
        "{bac.1}Exploiter la loi de Beer-Lambert pour déterminer une concentration. "
        "{bac.2}Exploiter la loi de Kohlrausch pour déterminer une concentration. "
        "{bac.3}Exploiter un spectre infrarouge pour identifier un groupe caractéristique. "
        "{bac.4}Exploiter un spectre ultraviolet-visible pour identifier une espèce. "
        "{bac.5}Mesurer une conductance et tracer une courbe d'étalonnage. "
        "{bac.6}Et maîtriser les conversions d'unités.",
        "Si tu sais faire ces six choses, tu as tout le bagage du chapitre. Le site t'attend avec les exercices du plan de travail, les deux TP corrigés et la fiche mémo. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="MESURER SANS DÉTRUIRE", branches=[
            dict(t="L'absorbance", items=["A = log(I_0/I)", "A = ε × ℓ × c", "au-delà de 2,5 : diluer"]),
            dict(t="Le spectre UV-visible", items=["mesurer à λ_{max}", "couleur complémentaire", "identifier : λ_{max} + allure"]),
            dict(t="La conductivité", items=["G = I/U · σ = K × G", "σ = Σ λ_i [X_i]", "[X] en mol·m^-3"]),
            dict(t="L'infrarouge", items=["σ = 1/λ en cm^-1", "O—H large · C=O fine", "des groupes, pas des molécules"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "C1 · Beer-Lambert : déterminer une concentration", "C2 · Kohlrausch : déterminer une concentration",
            "C3 · Spectre IR : identifier un groupe caractéristique", "C4 · Spectre UV-visible : identifier une espèce",
            "C5 · Mesurer une conductance, tracer un étalonnage", "Conversions d'unités : mol·m⁻³, cm², mS·cm⁻¹"],
                    marques=["✓"] * 6, x=170, y=100, w=940),
    }),
]

QUIZ = [
    dict(q="Une solution paraît bleue. Elle absorbe surtout…",
         r=["le bleu", "l'orange-rouge, vers 600-630 nm", "toutes les couleurs autant"], ok=1,
         ex="On voit la couleur transmise, complémentaire de la couleur absorbée.", voir="assoc"),
    dict(q="La moitié de la lumière traverse une cuve. L'absorbance vaut…",
         r=["0,50", "0,30", "2,0"], ok=1, ex="A = log(I₀/I) = log 2 ≈ 0,30.", voir="f_A"),
    dict(q="Dans A = ε × ℓ × c, l'unité de ε est…",
         r=["L·mol⁻¹·cm⁻¹", "mol·L⁻¹·cm", "sans unité"], ok=0,
         ex="ε = A/(ℓ × c) : l'inverse de cm × mol·L⁻¹, soit L·mol⁻¹·cm⁻¹.", voir="u_eps"),
    dict(q="Un calcul prédit A = 4,4 pour une solution. Que faire ?",
         r=["Mesurer quand même", "Diluer d'un facteur connu, puis remonter la dilution", "Prolonger la droite d'étalonnage"], ok=1,
         ex="Au-delà de 2,5 environ, le spectrophotomètre sature. On dilue, puis on multiplie la concentration trouvée par le facteur.", voir="ex_sat"),
    dict(q="Pourquoi mesure-t-on à λmax ? (la réponse complète)",
         r=["Parce que la solution y est plus colorée", "Sensibilité maximale et courbe plate", "Parce que ε y est nul"], ok=1,
         ex="Les deux raisons sont attendues : la plus grande variation de A pour une variation de c, et une erreur sur λ sans effet au sommet.", voir="lmax"),
    dict(q="Droite d'étalonnage A = 0,13 × C (C en mg·L⁻¹). L'échantillon donne A = 0,025. Sa concentration vaut…",
         r=["0,0033 mg·L⁻¹", "0,19 mg·L⁻¹", "5,2 mg·L⁻¹"], ok=1, ex="C = A / k = 0,025 / 0,13 ≈ 0,19 mg·L⁻¹ : on divise.", voir="ex_tp2"),
    dict(q="On rapproche les plaques de la cellule de moitié, même solution. Que deviennent G et σ ?",
         r=["G double, σ ne change pas", "G et σ doublent", "G ne change pas, σ double"], ok=0,
         ex="G = σ × S/L dépend de la sonde ; σ ne dépend que de la solution.", voir="an_c"),
    dict(q="Pour MgCl₂ à la concentration c, la loi de Kohlrausch s'écrit…",
         r=["σ = c(λMg²⁺ + λCl⁻)", "σ = c(λMg²⁺ + 2λCl⁻)", "σ = 2c(λMg²⁺ + λCl⁻)"], ok=1,
         ex="[Cl⁻] = 2c : le 2 se place devant le λ de l'ion chlorure.", voir="f_nacl"),
    dict(q="Dans σ = Σ λᵢ[Xᵢ], avec λ en S·m²·mol⁻¹, une concentration de 0,200 mol·L⁻¹ s'écrit…",
         r=["0,200 mol·m⁻³", "2,00 × 10² mol·m⁻³", "2,00 × 10⁻⁴ mol·m⁻³"], ok=1,
         ex="1 mol·L⁻¹ = 10³ mol·m⁻³. Sans conversion, le résultat est mille fois trop petit.", voir="ex_soude"),
    dict(q="Un spectre IR montre une bande fine et intense vers 1 715 cm⁻¹ et aucune bande large vers 3 300. La molécule est…",
         r=["un alcool", "un acide carboxylique", "un aldéhyde ou une cétone"], ok=2,
         ex="C=O sans O—H : aldéhyde ou cétone. O—H + C=O : acide ; O—H seul : alcool.", voir="lire"),
]

CREDITS = [
    "Photos : gamme de solutions en fioles jaugées, Alina Popova, CC BY 4.0 ; cuves de spectrophotomètre, Retama, CC BY-SA 4.0 ; "
    "spectrophotomètre de laboratoire, TimVickers (domaine public) ; conductimètre, Nuno Nogueira, CC BY-SA 2.5.",
    "Images trouvées sur Wikimedia Commons. Animations, schémas et graphiques : faits pour le site ; spectres infrarouges schématisés "
    "d'après la table des bandes du cours. Valeurs des TP 2 et 3 : énoncés et mesures de la classe. Les trois exercices sont inventés pour la vidéo.",
]
