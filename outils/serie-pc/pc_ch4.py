"""Physique-chimie, chapitre 4 : « La lumière, un flux de photons » — le cours en vidéo.

Même chaîne que les séries philo (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ;
moteur pc/serie/moteur.js, qui ajoute les types anim (animations du site pilotées par le temps), formule, graphe,
exo et pause (la vidéo s'arrête d'elle-même avant chaque correction).
Contenu : le cours du site (pc/index.html, chapitre 4, fiches 1 à 8, TP 6), rien au-delà ; ce qui dépasse le
programme est dit « hors programme ». Les trois exercices sont inventés pour la vidéo (signalé à l'écran) ; leurs
valeurs ont été recalculées (voir les commentaires).
Usage : python3 outils/serie-philo/verifier.py pc_ch4 ; puis generer.py pc_ch4 ; chevauchements.py ch4.
"""

SITE = "pc"
CODE = "ch4"
NOTION = "La lumière, un flux de photons"
NUM = 4
TITRE = "La lumière, un flux de photons"
SUIVANT = "Chapitre 5 · La lunette astronomique"
PRONONCIATION = {"Hertz": "Hertz", "Hallwachs": "Hallvaks", "Millikan": "Milikane", "Lenard": "Lénard", "Planck": "Planque",
                 "Maxwell": "Maxouel", "Young": "Yongue", "Fresnel": "Frénel", "Compton": "Comptone"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur PC)."""
    return f"[[{a}|{b}]]".replace(" ", " ")


# ---------------------------------------------------------------- données des graphiques
# TP 6 : cellule 10 cm × 10 cm sous 400 W/m² (tableur du professeur) ; U en V, I en mA
TP6 = [(0, 120), (.5, 119.8), (1, 119.5), (1.5, 119.1), (2, 118.6), (2.5, 117.9), (3, 116.8), (3.5, 115), (4, 111.5),
       (4.3, 107), (4.5, 101.5), (4.7, 92), (4.9, 78), (5.1, 60.5), (5.3, 41), (5.5, 22.5), (5.7, 8), (5.8, 0)]
TP6_P = [(u, round(u * i / 1000, 3)) for u, i in TP6]          # P en W ; maximum 0,460 W à 4,3 V
# exercice 3 : module d'une lampe de jardin, 80 cm², 800 W/m² (valeurs inventées, cohérentes : Pmax 0,95 W à 4,2 V)
JARDIN = [(0, 250), (1, 249), (2, 247), (3, 243), (3.5, 238), (4, 232), (4.2, 226), (4.4, 205), (4.6, 150), (4.8, 80), (5, 0)]
JARDIN_P = [(u, round(u * i / 1000, 3)) for u, i in JARDIN]    # maximum 0,949 W à 4,2 V
H_EV = 0.4136                                                    # h en eV par 10^14 Hz (pente des droites Ec = f(ν))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_cal}{q1}Regarde cette calculatrice. Pas de pile. Une petite bande sombre, en haut : une cellule solaire. "
        "Sous la lumière du jour, elle marche. Dans le noir, elle s'éteint.",
        "{-q1}{q2}Alors une question toute simple : comment la lumière peut-elle fabriquer un courant électrique ?",
        "{-q2}{-tab_cal}{tab_sol}{q3}Et voici l'énigme qui a résisté aux plus grands physiciens à la fin du dix-neuvième siècle. "
        "Une lampe rouge, même énorme, même allumée des heures, ne fait sortir aucun électron d'une plaque de zinc. "
        "Une petite lampe ultraviolette, très faible, y arrive tout de suite.",
        ("Pourquoi ?", {"rate": "-8%"}),
        "{-q3}Pour répondre, il va falloir changer d'idée sur ce qu'est la lumière. "
        "Elle n'est pas seulement une onde : elle est aussi faite de grains d'énergie, les {!photons}photons.",
        "{-tab_sol}{plan}Dans cette vidéo, on part de zéro. {plan.1}D'abord les bases : l'onde lumineuse et le photon. "
        "{plan.2}Puis les atomes qui absorbent et émettent la lumière. {plan.3}Ensuite l'effet photoélectrique, et l'idée géniale d'Einstein. "
        "{plan.4}Enfin les cellules solaires et leur rendement. {plan.5}Et pour finir, trois exercices corrigés : un simple, un plus difficile, et un type bac.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "tab_cal": dict(type="tableau", img="c4-calculatrice", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .2],
                        legende="Calculatrice solaire, photo Evan-Amos (domaine public)"),
        "q1": dict(type="question", t="Pas de pile… et pourtant elle marche."),
        "q2": dict(type="question", t="Comment la lumière fabrique-t-elle un courant ?"),
        "tab_sol": dict(type="tableau", img="c4-soleil", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .5],
                        legende="Le Soleil vu par le Solar Dynamics Observatory, NASA (domaine public)"),
        "q3": dict(type="question", t="Lampe rouge énorme : rien. Petite lampe UV : ça marche."),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Les bases : l'onde lumineuse et le photon", "Absorber et émettre : les niveaux d'énergie",
            "L'effet photoélectrique et l'idée d'Einstein", "Les cellules solaires et leur rendement",
            "Trois exercices corrigés : simple, difficile, type bac"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Physique-chimie · Chapitre 4", t="La lumière, un flux de photons",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ I. l'onde lumineuse
    dict(id="onde", chap="La lumière, une onde", fond="nuit", humeur="lumiere",
         retenir="λ = c / ν : longueur d'onde en mètres, fréquence en hertz, c = 3,00 × 10⁸ m/s. Plus la fréquence est grande, plus λ est courte.",
         beats=[
        "{tab_pri}Commençons par ce que tu sais déjà, ou presque. La lumière est une onde électromagnétique : "
        "une vibration du champ électrique et du champ magnétique, qui se propage, même dans le vide.",
        "{-tab_pri}{onde}Comme toute onde périodique, elle a {onde.1}une longueur d'onde, notée lambda : "
        "la distance entre deux crêtes, ou, plus exactement, la distance parcourue par l'onde pendant une période.",
        "Elle a aussi une fréquence, notée nu, la lettre grecque : le nombre d'oscillations par seconde, en hertz. "
        "{onde.c}Et elle avance à la célérité c : trois cent mille kilomètres par seconde dans le vide. "
        "C'est la même vitesse pour toutes les couleurs.",
        "{-onde}{f_lam}{f_lam.1}Ces trois grandeurs sont liées par une relation à connaître par cœur : lambda égale c sur nu.",
        "{f_lam.2}D'où vient-elle ? Pendant une période, qui vaut un sur nu, l'onde avance de c fois la période. "
        "Et c'est justement la définition de la longueur d'onde. Donc lambda égale c fois T, c'est-à-dire c sur nu.",
        "{f_lam.3}Conséquence : plus la fréquence est grande, plus la longueur d'onde est courte. Les deux varient en sens inverse.",
        "{-f_lam}{spec}Classons maintenant les lumières par longueur d'onde. Entre quatre cents et huit cents nanomètres environ : "
        "le visible, du violet au rouge. En dessous de quatre cents nanomètres : l'ultraviolet, invisible. "
        "Au-dessus de huit cents : l'infrarouge, invisible lui aussi.",
        "{-spec}{piege_nm}Attention au piège d'unité le plus fréquent du chapitre. Les longueurs d'onde sont données en nanomètres, "
        "et un nanomètre, c'est dix puissance moins neuf mètre. Dans la formule, lambda doit être en mètres. "
        "Six cent trente-trois nanomètres s'écrit donc six cent trente-trois fois dix puissance moins neuf mètre.",
        "{-piege_nm}{ex_lam}Faisons un premier calcul. Un laser rouge a une longueur d'onde de six cent trente-trois nanomètres. "
        "{ex_lam.1}Sa fréquence vaut c sur lambda : {ex_lam.2}trois fois dix puissance huit, divisé par six cent trente-trois fois dix puissance moins neuf. "
        "{ex_lam.3}On trouve environ quatre virgule soixante-quatorze fois dix puissance quatorze hertz. "
        "Près de cinq cent mille milliards d'oscillations par seconde !",
        "{-ex_lam}",
    ], vis={
        "tab_pri": dict(type="tableau", img="c4-spectre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Spectre de la lumière du Soleil à travers un prisme, photo Pittigrilli, CC BY-SA 4.0"),
        "onde": dict(type="illu", nom="onde", x=110, y=150, w=1060, h=420),
        "f_lam": dict(type="formule", titre="Longueur d'onde et fréquence", x=150, y=130, w=980, lignes=[
            dict(f="λ = " + fr("c", "ν") + "  ⇔  ν = " + fr("c", "λ"), cadre=True, n="λ en mètres (m) · c = 3,00 × 10^8 m·s^-1 · ν en hertz (Hz)"),
            dict(f="Pendant une période T = " + fr("1", "ν") + ", l'onde avance de c × T : c'est λ.", txt=True),
            dict(f="ν grande  ⇒  λ courte", n="les deux varient en sens inverse")]),
        "spec": dict(type="illu", nom="spectre", x=120, y=170, w=1040, h=380),
        "piege_nm": dict(type="note", titre="Le piège des nanomètres", cles=["mètres", "nanomètre"],
                         t="1 nm = 10^-9 m. Dans λ = c / ν, λ est en mètres : 633 nm = 633 × 10^-9 m.", x=170, y=200, w=940),
        "ex_lam": dict(type="formule", titre="Exemple · un laser rouge, λ = 633 nm", x=150, y=150, w=980, lignes=[
            dict(f="ν = " + fr("c", "λ")),
            dict(f="ν = " + fr("3,00 × 10^8", "633 × 10^-9")),
            dict(f="ν ≈ 4,74 × 10^14 Hz", cadre=True)]),
    }),

    # ================================================================ II. le photon
    dict(id="photon", chap="Le photon, grain de lumière", fond="cosmos", humeur="mystere",
         retenir="E = hν = hc/λ, avec h = 6,63 × 10⁻³⁴ J·s et 1 eV = 1,60 × 10⁻¹⁹ J. Plus intense = plus de photons, pas des photons plus énergétiques.",
         beats=[
        "{dual}Voici maintenant l'idée centrale du chapitre. Selon l'expérience, la lumière se comporte de deux façons. "
        "Elle fait des interférences et de la diffraction : ce sont des comportements d'onde.",
        "Mais regarde cette expérience. On envoie la lumière si faiblement qu'elle arrive grain par grain. "
        "Chaque grain fait un point, un seul, à un endroit précis de l'écran. Et petit à petit, les points dessinent… des franges d'interférence.",
        ("La lumière arrive comme une particule, et se répartit comme une onde.", {"rate": "-5%"}),
        "{-dual}{def_dual}C'est ce qu'on appelle la {!dualité}dualité onde-particule : ni l'image de l'onde, ni celle de la particule, ne suffit seule.",
        "{-def_dual}{def_ph}Ces grains de lumière s'appellent des photons. {def_ph.1}Un photon, c'est une particule associée à une onde électromagnétique de fréquence nu. "
        "Retiens ses trois caractéristiques : il a une énergie, il se déplace à la vitesse c dans le vide, et sa masse est nulle. Sa charge aussi.",
        "{-def_ph}{f_E}{f_E.1}Et son énergie est donnée par la relation la plus importante du chapitre : E égale h nu.",
        "{f_E.2}h, c'est la constante de Planck : six virgule soixante-trois fois dix puissance moins trente-quatre joule seconde. "
        "Un nombre minuscule, parce que l'énergie d'un seul photon est minuscule.",
        "{f_E.3}Et comme nu égale c sur lambda, on peut aussi écrire : E égale h c sur lambda.",
        "{f_E.4}Retiens le sens de variation : l'énergie d'un photon ne dépend que de sa fréquence. "
        "Plus la longueur d'onde est courte, plus le photon est énergétique. Un photon ultraviolet porte bien plus d'énergie qu'un photon infrarouge.",
        "{-f_E}{f_eV}Les énergies en joules sont si petites qu'on utilise une unité adaptée : l'électronvolt. "
        "{f_eV.1}Un électronvolt vaut un virgule soixante fois dix puissance moins dix-neuf joule. "
        "{f_eV.2}Pour passer des joules aux électronvolts, on divise. {f_eV.3}Des électronvolts aux joules, on multiplie.",
        "{-f_eV}{ex_E}Reprenons notre laser rouge à six cent trente-trois nanomètres. "
        "{ex_E.1}E égale h c sur lambda. {ex_E.2}Six virgule soixante-trois fois dix puissance moins trente-quatre, fois trois fois dix puissance huit, "
        "divisé par six cent trente-trois fois dix puissance moins neuf. "
        "{ex_E.3}On obtient trois virgule quatorze fois dix puissance moins dix-neuf joule. "
        "{ex_E.4}On divise par un virgule soixante fois dix puissance moins dix-neuf : un virgule quatre-vingt-seize électronvolt.",
        "{-ex_E}{astuce}Une astuce pour vérifier tes calculs, sans la présenter comme une formule du cours : "
        "l'énergie en électronvolts vaut à peu près mille deux cent quarante divisé par la longueur d'onde en nanomètres. "
        "Mille deux cent quarante sur six cent trente-trois : environ un virgule quatre-vingt-seize. Ça colle.",
        "Et un repère à garder en tête : le visible va d'environ un virgule six électronvolt, pour le rouge, à trois virgule un électronvolt, pour le violet.",
        "{-astuce}{fais}Maintenant, une idée qui va tout débloquer plus tard. Que veut dire une lumière plus intense ? "
        "{fais.1}Une lumière rouge faible envoie peu de photons. {fais.2}Une lumière rouge intense en envoie beaucoup plus… mais chacun a exactement la même énergie. "
        "{fais.3}Pour avoir des photons plus énergétiques, il ne faut pas plus de lumière : il faut une autre couleur, une fréquence plus grande.",
        "{-fais}{f_P}{f_P.1}La puissance d'un faisceau, c'est donc le nombre de photons émis par seconde, multiplié par l'énergie d'un photon. "
        "P égale N fois h nu. {f_P.2}Pour un pointeur laser rouge d'un milliwatt, cela fait environ trois virgule deux fois dix puissance quinze photons par seconde. "
        "Tellement que le faisceau paraît continu.",
        "{-f_P}{frise}Un mot d'histoire, car le programme le demande. {frise.1}En mille sept cent quatre, Newton pense que la lumière est faite de corpuscules. "
        "{frise.2}Au début du dix-neuvième siècle, Young puis Fresnel observent les interférences : la lumière est une onde. "
        "{frise.3}En mille huit cent soixante-cinq, Maxwell montre que c'est une onde électromagnétique. "
        "{frise.4}En mille neuf cent, Planck suppose que l'énergie est échangée par paquets, des quanta. "
        "{frise.5}En mille neuf cent cinq, Einstein va plus loin : la lumière elle-même est faite de quanta. "
        "{frise.6}Et en mille neuf cent seize, Millikan, qui voulait lui donner tort, le confirme par ses mesures.",
        "{-frise}",
    ], vis={
        "dual": dict(type="illu", nom="dualite", x=200, y=100, w=880, h=520),
        "def_dual": dict(type="def", terme="Dualité onde-particule", cles=["onde", "particule"],
                         t="La lumière se comporte comme une onde (interférences, diffraction) et comme une particule (échanges d'énergie par paquets).",
                         x=170, y=190, w=940),
        "def_ph": dict(type="def", terme="Le photon", cles=["énergie", "vitesse", "masse"],
                       t="Particule associée à une onde électromagnétique de fréquence ν.",
                       etape="Une énergie E = hν · une vitesse c dans le vide · une masse nulle (et une charge nulle).", x=170, y=170, w=940),
        "f_E": dict(type="formule", titre="Énergie d'un photon", x=150, y=110, w=980, lignes=[
            dict(f="E = h × ν", cadre=True, taille=56),
            dict(f="h = 6,63 × 10^-34 J·s", n="la constante de Planck · E en joules (J) · ν en hertz (Hz)"),
            dict(f="E = h × ν = " + fr("h × c", "λ"), cadre=True, n="λ en mètres"),
            dict(f="λ courte  ⇒  photon énergétique", txt=True)]),
        "f_eV": dict(type="formule", titre="L'électronvolt", x=150, y=170, w=980, lignes=[
            dict(f="1 eV = 1,60 × 10^-19 J", cadre=True),
            dict(f="J → eV : on divise par 1,60 × 10^-19", txt=True, pt=True),
            dict(f="eV → J : on multiplie par 1,60 × 10^-19", txt=True, pt=True)]),
        "ex_E": dict(type="formule", titre="Exemple · le laser rouge, λ = 633 nm", x=150, y=120, w=980, lignes=[
            dict(f="E = " + fr("h × c", "λ")),
            dict(f="E = " + fr("6,63 × 10^-34 × 3,00 × 10^8", "633 × 10^-9")),
            dict(f="E = 3,14 × 10^-19 J"),
            dict(f="E = " + fr("3,14 × 10^-19", "1,60 × 10^-19") + " = 1,96 eV", cadre=True)]),
        "astuce": dict(type="note", titre="Pour vérifier un calcul", cles=["vérifier", "visible"],
                       t="E (en eV) ≈ 1 240 / λ (en nm). Le visible va de 1,6 eV (rouge, 800 nm) à 3,1 eV (violet, 400 nm).",
                       x=170, y=200, w=940),
        "fais": dict(type="illu", nom="faisceau", x=120, y=110, w=1040, h=500),
        "f_P": dict(type="formule", titre="Puissance d'un faisceau", x=150, y=150, w=980, lignes=[
            dict(f="P = N × h × ν", cadre=True, n="P en watts · N : nombre de photons émis par seconde"),
            dict(f="N = " + fr("P", "h × ν") + " = " + fr("1,0 × 10^-3", "3,14 × 10^-19") + " ≈ 3,2 × 10^15 photons par seconde",
                 n="pointeur laser rouge de 1 mW")]),
        "frise": dict(type="frise", items=[
            dict(d=1704, nom="Newton", q="corpuscules"), dict(d=1801, nom="Young, Fresnel", q="interférences : une onde"),
            dict(d=1865, nom="Maxwell", q="onde électromagnétique", img="maxwell"), dict(d=1900, nom="Planck", q="les quanta", img="planck"),
            dict(d=1905, nom="Einstein", q="la lumière en quanta", img="einstein"), dict(d=1916, nom="Millikan", q="confirmation", img="millikan")]),
    }),

    # ================================================================ III. niveaux d'énergie
    dict(id="niveaux", chap="Absorber et émettre", fond="cosmos", humeur="calme",
         retenir="|ΔE| = |E_final − E_initial| = hν = hc/λ. L'absorption est du tout ou rien : le photon doit apporter exactement un écart entre deux niveaux.",
         beats=[
        "{an_ph}Passons de la lumière à la matière. L'énergie d'un atome ne peut pas prendre n'importe quelle valeur : elle est quantifiée. "
        "{ph_pts}{ph_pts.1}{an_ph.1}Sur le diagramme de droite, chaque trait horizontal est un niveau d'énergie permis. "
        "Le plus bas s'appelle l'état fondamental. Les autres sont des états excités. Entre deux niveaux, rien.",
        "Les énergies sont négatives : zéro, tout en haut, c'est l'électron arraché à l'atome.",
        "{ph_pts.2}{an_ph.2}Envoyons un photon de onze électronvolts sur un atome d'hydrogène dans son état fondamental. "
        "Il faudrait que l'atome monte à moins deux virgule six électronvolts. Or aucun niveau n'existe là. Résultat : rien. Le photon passe.",
        "{ph_pts.3}{an_ph.3}Envoyons maintenant un photon de dix virgule deux électronvolts. Cette fois, c'est exactement l'écart entre le niveau un et le niveau deux. "
        "Le photon est absorbé : il disparaît, et l'atome monte au niveau deux. C'est l'{!absorption}absorption.",
        "{ph_pts.4}{an_ph.4}Un atome excité ne le reste pas. Il redescend, et en redescendant, il émet un photon qui emporte exactement la différence d'énergie. "
        "C'est l'émission.",
        "{ph_pts.5}{an_ph.5}Il peut aussi monter plus haut, puis redescendre par étapes. De trois à deux, il émet un photon de un virgule quatre-vingt-neuf électronvolt : "
        "une raie rouge, visible, à six cent cinquante-six nanomètres.",
        "{-ph_pts}{f_dE}{f_dE.1}Tout cela tient en une relation : la valeur absolue de delta E, l'écart entre les niveaux, égale h nu, égale h c sur lambda. "
        "{f_dE.2}Si l'atome descend, il émet. S'il monte, il absorbe.",
        "{f_dE.3}Et retiens bien ceci : l'absorption est du tout ou rien. Un atome ne prend pas ce qu'il peut. "
        "Le photon doit apporter exactement un écart entre deux niveaux, sinon il n'est pas absorbé du tout.",
        "{-f_dE}{-an_ph}{methode}Voici la méthode, pas à pas, pour passer d'une transition à une longueur d'onde. "
        "{methode.1}Un : lis les deux niveaux et calcule l'écart en électronvolts. "
        "{methode.2}Deux : convertis-le en joules, en multipliant par un virgule soixante fois dix puissance moins dix-neuf. "
        "{methode.3}Trois : calcule lambda égale h c sur delta E, en mètres, puis convertis en nanomètres. "
        "{methode.4}Quatre : situe lambda. Ultraviolet, visible, ou infrarouge ?",
        "{-methode}{ex_ha}Appliquons-la à la raie rouge de l'hydrogène, la transition de trois vers deux. "
        "{ex_ha.1}Delta E égale moins un virgule cinquante et un, moins, moins trois virgule quarante : un virgule quatre-vingt-neuf électronvolt. "
        "{ex_ha.2}En joules : trois virgule zéro deux fois dix puissance moins dix-neuf. "
        "{ex_ha.3}Lambda égale h c sur delta E : on trouve environ six cent cinquante-huit nanomètres. "
        "{ex_ha.4}La raie mesurée est à six cent cinquante-six nanomètres : le petit écart vient des arrondis des niveaux. C'est du rouge, visible.",
        "{-ex_ha}{tab_ori}Cette raie porte un nom : H alpha. C'est elle qui donne leur couleur rouge aux nébuleuses, comme celle d'Orion. "
        "Chaque élément a ses propres niveaux, donc ses propres raies : c'est sa signature.",
        "{an_ph2}{ph2_pts}{ph2_pts.1}{an_ph2.1}Et un même gaz absorbe exactement les longueurs d'onde qu'il sait émettre : "
        "les raies noires du spectre d'absorption sont aux mêmes places que les raies colorées du spectre d'émission.",
        "{ph2_pts.2}{an_ph2.2}Dernier cas : un photon de plus de treize virgule six électronvolts. Il peut toujours être absorbé, quelle que soit son énergie, "
        "car il arrache l'électron, et le surplus devient de l'énergie cinétique. Garde cette image en tête : c'est exactement l'idée de l'effet photoélectrique.",
        "{-an_ph2}{-ph2_pts}{-tab_ori}",
    ], vis={
        "an_ph": dict(type="anim", nom="photon", x=40, y=72, h=624, seg=[[1.2, 9], [9, 18.5], [18.5, 29], [29, 37], [37, 50.5]]),
        "ph_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=110, w=560, items=[
            "Des niveaux permis : le fondamental, puis les états excités", "Photon de 11,0 eV : aucun niveau à −2,6 eV, rien",
            "Photon de 10,2 eV = E_2 − E_1 : absorbé, l'atome monte", "Il redescend : un photon de 10,2 eV est émis",
            "3 → 2 : 1,89 eV, la raie rouge à 656 nm"]),
        "f_dE": dict(type="formule", titre="Transition entre deux niveaux", x=680, y=130, w=560, lignes=[
            dict(f="|ΔE| = h × ν = " + fr("h × c", "λ"), cadre=True, taille=40, n="ΔE = E_{final} − E_{initial}"),
            dict(f="descend : émission · monte : absorption", txt=True),
            dict(f="tout ou rien : exactement un écart", txt=True, pt=True)]),
        "methode": dict(type="liste", titre="Méthode · de la transition à λ", items=[
            "Lire les deux niveaux, calculer |ΔE| en eV", "Convertir en joules : × 1,60 × 10^-19",
            "λ = hc / |ΔE| en mètres, puis en nm", "Situer λ : UV, visible ou IR"], x=170, y=150, w=940),
        "ex_ha": dict(type="formule", titre="La raie rouge de l'hydrogène (3 → 2)", x=150, y=130, w=980, lignes=[
            dict(f="|ΔE| = −1,51 − (−3,40) = 1,89 eV"),
            dict(f="|ΔE| = 1,89 × 1,60 × 10^-19 = 3,02 × 10^-19 J"),
            dict(f="λ = " + fr("6,63 × 10^-34 × 3,00 × 10^8", "3,02 × 10^-19") + " ≈ 6,58 × 10^-7 m"),
            dict(f="≈ 658 nm : rouge, visible (mesuré : 656 nm)", cadre=True)]),
        "tab_ori": dict(type="tableau", img="c4-orion", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .45, .45],
                        legende="La nébuleuse d'Orion, télescope spatial Hubble, NASA, ESA, M. Robberto (domaine public)"),
        "ph2_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=150, w=560, items=[
            "Émission et absorption : les mêmes longueurs d'onde", "Plus de 13,6 eV : l'électron est arraché, le surplus devient E_c"]),
        "an_ph2": dict(type="anim", nom="photon", x=40, y=72, h=624, seg=[[50.5, 60.5], [60.5, 74]]),
    }),

    # ================================================================ IV. l'effet photoélectrique : les faits
    dict(id="faits", chap="L'effet photoélectrique : les faits", fond="nuit", humeur="tension",
         retenir="Seuil de fréquence, émission instantanée, Ec qui dépend de ν et pas de l'intensité, nombre d'électrons proportionnel à l'intensité : l'onde n'explique pas les trois premiers.",
         beats=[
        "{hertz}Nous voici au cœur du chapitre. En mille huit cent quatre-vingt-sept, Heinrich Hertz observe un phénomène étrange : "
        "la lumière ultraviolette favorise les étincelles entre deux électrodes. Hallwachs l'étudie ensuite avec une plaque de zinc.",
        "{-hertz}{def_pe}{def_pe.1}C'est l'effet photoélectrique : l'émission d'électrons par un matériau, le plus souvent un métal, sous l'effet d'une lumière.",
        "{-def_pe}{an_pe}{pe_pts}{pe_pts.1}{an_pe.1}Regarde la plaque de zinc. Ses électrons sont prisonniers du métal : pour en sortir, il leur faut une énergie minimale.",
        "{pe_pts.2}{an_pe.2}On l'éclaire avec une lampe rouge très puissante. Résultat : rien. Aucun électron ne sort. Même après des heures.",
        "{pe_pts.3}{an_pe.3}Or le modèle de l'onde prévoyait l'inverse : une onde intense apporte beaucoup d'énergie, en attendant assez longtemps, "
        "l'électron aurait dû finir par sortir. Ce n'est jamais observé.",
        "{pe_pts.4}{an_pe.4}Maintenant, une lampe ultraviolette, très faible. Et là, des électrons sortent. Tout de suite. Sans attendre.",
        "{pe_pts.5}{an_pe.5}On augmente l'intensité de l'ultraviolet : il sort plus d'électrons… mais ils ne vont pas plus vite.",
        "{pe_pts.6}{an_pe.6}On prend un ultraviolet de fréquence plus grande : cette fois, les électrons sortent plus vite.",
        "{-an_pe}{-pe_pts}{tab_faits}Résumons les quatre faits expérimentaux, à savoir décrire. "
        "{tab_faits.1}Un : il existe une fréquence seuil, propre au métal. En dessous, aucun électron n'est émis, même avec une lumière très intense. "
        "{tab_faits.2}Deux : au-dessus du seuil, l'émission est instantanée, même avec une lumière très faible. "
        "{tab_faits.3}Trois : l'énergie cinétique des électrons augmente avec la fréquence, et ne dépend pas de l'intensité. "
        "{tab_faits.4}Quatre : le nombre d'électrons émis est proportionnel à l'intensité lumineuse.",
        "{-tab_faits}{onde_ko}Le modèle de l'onde, qui triomphait depuis un siècle, n'explique que le quatrième fait. "
        "Les trois autres le contredisent. Il faut une autre idée.",
        "{-onde_ko}",
    ], vis={
        "hertz": dict(type="portrait", annee=1887, img="hertz", nom="Heinrich Hertz", dates="1857 – 1894",
                      legende="observe l'effet photoélectrique en 1887"),
        "def_pe": dict(type="def", terme="L'effet photoélectrique", cles=["émission", "électrons"],
                       t="L'émission d'électrons par un matériau, le plus souvent un métal, sous l'effet d'un rayonnement électromagnétique.",
                       x=170, y=200, w=940),
        "an_pe": dict(type="anim", nom="photoelec", x=40, y=72, h=624, seg=[[1.2, 9], [9, 20], [20, 30], [30, 41], [41, 51], [51, 62.5]]),
        "pe_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=96, w=560, items=[
            "Les électrons sont liés au zinc : il faut 4,3 eV pour sortir", "Rouge très intense : aucun électron",
            "L'onde prévoyait une sortie, à force d'attendre : jamais observé", "UV très faible : un électron sort aussitôt",
            "UV plus intense : plus d'électrons, pas plus rapides", "UV de plus haute fréquence : électrons plus rapides"]),
        "tab_faits": dict(type="liste", titre="Les quatre faits expérimentaux", items=[
            "Une fréquence seuil ν_0 : en dessous, aucun électron, même très intense",
            "Au-dessus du seuil, émission instantanée, même très faible",
            "E_c augmente avec ν, ne dépend pas de l'intensité",
            "Le nombre d'électrons est proportionnel à l'intensité"], marques=["1", "2", "3", "4"], x=150, y=140, w=980),
        "onde_ko": dict(type="note", titre="Ce que l'onde n'explique pas", cles=["quatrième", "contredisent"],
                        t="Le modèle ondulatoire n'explique que le fait 4. Les faits 1, 2 et 3 le contredisent.", x=170, y=220, w=940),
    }),

    # ================================================================ V. l'explication d'Einstein
    dict(id="einstein", chap="L'idée d'Einstein", fond="aube", humeur="lumiere",
         retenir="Un photon, un électron, tout ou rien. Effet si hν ≥ Φ, soit ν ≥ ν₀ = Φ/h, soit λ ≤ λ₀ = hc/Φ.",
         beats=[
        "{ein}En mille neuf cent cinq, un jeune employé de l'office des brevets de Berne propose une explication : Albert Einstein. "
        "Son idée : la lumière est faite de grains d'énergie h nu. Et c'est pour ce travail, pas pour la relativité, qu'il reçoit le prix Nobel en mille neuf cent vingt et un.",
        "{-ein}{regle}Voici la règle, en une phrase. {regle.1}Un photon interagit avec un seul électron. "
        "{regle.2}Il lui cède toute son énergie d'un coup, ou rien. Le photon disparaît. "
        "{regle.3}Et un électron ne peut pas additionner l'énergie de deux photons.",
        "{-regle}{def_phi}Pour sortir du métal, un électron doit recevoir une énergie minimale : {def_phi.1}le travail d'extraction, noté phi. "
        "Il est propre au métal, car les électrons sont plus ou moins liés selon l'élément.",
        "{-def_phi}{f_seuil}{f_seuil.1}Donc il y a effet photoélectrique seulement si un photon apporte au moins phi : h nu supérieur ou égal à phi. "
        "{f_seuil.2}Ce qui donne la fréquence seuil : nu zéro égale phi sur h. "
        "{f_seuil.3}Et la longueur d'onde seuil : lambda zéro égale h c sur phi.",
        "{f_seuil.4}Attention au sens des inégalités : il faut une fréquence supérieure au seuil, donc une longueur d'onde inférieure au seuil. "
        "Assez énergétique, ça veut dire assez bleu.",
        "{-f_seuil}{metaux}Quelques valeurs. {metaux.1}Le césium : phi vaut environ un virgule neuf électronvolt, seuil vers six cent cinquante nanomètres. "
        "{metaux.2}Le potassium : deux virgule trois électronvolts, seuil vers cinq cent quarante nanomètres. "
        "{metaux.3}Le zinc : quatre virgule trois électronvolts, seuil vers deux cent quatre-vingt-dix nanomètres, dans l'ultraviolet. "
        "Voilà pourquoi la lampe rouge ne fait rien au zinc.",
        "{-metaux}{ex_k}Exemple. Le potassium éclairé en rouge, à six cent dix nanomètres : {ex_k.1}mille deux cent quarante sur six cent dix, "
        "environ deux électronvolts. C'est moins que deux virgule trois : aucun électron, quelle que soit la puissance de la lampe. "
        "{ex_k.2}En bleu, à quatre cent vingt nanomètres : environ trois électronvolts, plus que deux virgule trois. Des électrons sortent.",
        "{-ex_k}{quatre}Et maintenant, les quatre faits s'expliquent un par un. "
        "{quatre.1}Le seuil : si h nu est inférieur à phi, aucun photon pris seul ne peut arracher un électron. En envoyer plus n'y change rien. "
        "{quatre.2}L'instantanéité : l'énergie est livrée en bloc par un photon. Dès le premier photon assez énergétique, un électron peut sortir. "
        "{quatre.3}L'énergie cinétique dépend de nu : c'est l'énergie d'un photon qui la fixe. "
        "{quatre.4}Le nombre d'électrons dépend de l'intensité : plus de lumière, c'est plus de photons, donc plus d'électrons arrachés.",
        "{-quatre}{milli}Millikan, convaincu qu'Einstein avait tort, passe dix ans à mesurer l'effet avec une grande précision. "
        "En mille neuf cent seize, ses mesures confirment toutes les prévisions, et lui donnent même une valeur précise de h. "
        "C'est l'un des actes de naissance de la physique quantique.",
        "{-milli}",
    ], vis={
        "ein": dict(type="portrait", annee=1905, img="einstein", nom="Albert Einstein", dates="1879 – 1955",
                    legende="1905 : la lumière est faite de quanta · prix Nobel 1921"),
        "regle": dict(type="liste", titre="L'idée d'Einstein", items=[
            "Un photon agit sur un seul électron", "Il lui cède toute son énergie hν, ou rien",
            "Un électron n'additionne pas l'énergie de deux photons"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "def_phi": dict(type="def", terme="Travail d'extraction Φ (ou W₀)", cles=["minimale", "propre"],
                        t="Énergie minimale à fournir à un électron pour l'arracher à la surface d'un métal.",
                        etape="Elle est propre au métal.", x=170, y=200, w=940),
        "f_seuil": dict(type="formule", titre="Condition d'émission et seuils", x=150, y=120, w=980, lignes=[
            dict(f="h × ν ≥ Φ", cadre=True),
            dict(f="ν ≥ ν_0 = " + fr("Φ", "h"), n="ν_0 : fréquence seuil, en Hz"),
            dict(f="λ ≤ λ_0 = " + fr("h × c", "Φ"), n="λ_0 : longueur d'onde seuil, en m · Φ en joules"),
            dict(f="fréquence au-dessus du seuil = longueur d'onde en dessous : « assez bleu »", txt=True)]),
        "metaux": dict(type="liste", titre="Trois métaux", items=[
            "Césium : Φ ≈ 1,9 eV · λ_0 ≈ 650 nm", "Potassium : Φ = 2,3 eV · λ_0 ≈ 540 nm",
            "Zinc : Φ = 4,3 eV · λ_0 ≈ 290 nm (il faut de l'UV)"], marques=["Cs", "K", "Zn"], x=170, y=180, w=940),
        "ex_k": dict(type="formule", titre="Exemple · le potassium, Φ = 2,3 eV", x=150, y=170, w=980, lignes=[
            dict(f="rouge, 610 nm : E ≈ " + fr("1 240", "610") + " ≈ 2,0 eV < 2,3 eV → aucun électron", ko=True, taille=34),
            dict(f="bleu, 420 nm : E ≈ " + fr("1 240", "420") + " ≈ 3,0 eV > 2,3 eV → des électrons sortent", ok=True, taille=34)]),
        "quatre": dict(type="liste", titre="Les quatre faits, expliqués", items=[
            "Seuil : hν < Φ, aucun photon seul ne suffit",
            "Instantané : l'énergie arrive en bloc",
            "E_c dépend de ν : l'énergie du photon la fixe",
            "Plus intense = plus de photons = plus d'électrons"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "milli": dict(type="portrait", annee=1916, img="millikan", nom="Robert Millikan", dates="1868 – 1953",
                      legende="1916 : ses mesures confirment Einstein · prix Nobel 1923"),
    }),

    # ================================================================ VI. bilan d'énergie
    dict(id="bilan", chap="Le bilan d'énergie", fond="nuit", humeur="calme",
         retenir="hν = Φ + Ec, donc Ec = hν − Φ = h(ν − ν₀) : une droite de pente h. Convertir avant de soustraire ; Ec en joules pour la vitesse.",
         beats=[
        "{an_bil}{an_bil.1}Allons jusqu'au bout. Le photon apporte h nu. Une partie, phi, sert à arracher l'électron. "
        "Le reste devient l'énergie cinétique de l'électron qui sort.",
        "{f_bil}{f_bil.1}D'où la relation d'Einstein : h nu égale phi plus E c. "
        "{f_bil.2}Ou encore : E c égale h nu moins phi, {f_bil.3}c'est-à-dire h fois nu moins nu zéro.",
        "{-an_bil}{-f_bil}{redac}Au bac, on peut te demander d'établir cette relation. Voici la rédaction attendue, en quatre temps. "
        "{redac.1}Le système : un électron du métal, et le photon qu'il absorbe. "
        "{redac.2}L'énergie reçue : le photon, absorbé en entier, apporte h nu. "
        "{redac.3}L'énergie dépensée : au minimum phi, pour quitter le métal. "
        "{redac.4}La conservation de l'énergie : ce qui reste est l'énergie cinétique de l'électron. E c égale h nu moins phi.",
        "{-redac}{gr_ec}Traçons E c en fonction de nu. {gr_ec.1}Pour le potassium, on obtient une droite. "
        "{gr_ec.2}Pour le zinc, une autre droite, parallèle. Même pente, pour tous les métaux : cette pente, c'est h. "
        "{gr_ec.3}Chaque droite coupe l'axe des fréquences en nu zéro, la fréquence seuil du métal. "
        "{gr_ec.4}Et si on la prolonge vers la gauche, elle coupe l'axe vertical en moins phi.",
        "C'est exactement ce qu'a mesuré Millikan : avec la pente, il a trouvé h ; avec l'intersection, le travail d'extraction.",
        "{-gr_ec}{ex_zn}Un exemple complet. Une plaque de zinc est éclairée par un ultraviolet à deux cents nanomètres. "
        "{ex_zn.1}L'énergie d'un photon : mille deux cent quarante sur deux cents, environ six virgule deux électronvolts. "
        "{ex_zn.2}E c égale six virgule deux moins quatre virgule trois : un virgule neuf électronvolt. "
        "{ex_zn.3}En joules, pour la suite : trois virgule zéro fois dix puissance moins dix-neuf. "
        "{ex_zn.4}Et puisque E c égale un demi m v carré, la vitesse vaut la racine de deux E c sur m. "
        "{ex_zn.5}Environ huit virgule deux fois dix puissance cinq mètres par seconde. Plus de huit cents kilomètres par seconde !",
        "{-ex_zn}{pieges}Deux pièges classiques. {pieges.1}Un : ne mélange jamais joules et électronvolts dans h nu moins phi. Convertis avant de soustraire. "
        "Et pour la vitesse, E c doit être en joules. "
        "{pieges.2}Deux : une lumière plus intense ne donne pas des électrons plus rapides. Elle donne plus d'électrons.",
        "{-pieges}{hp}Une précision, hors programme : phi est l'énergie qu'il faut aux électrons les moins liés. "
        "Les autres dépensent davantage et sortent moins vite. La relation donne donc l'énergie cinétique maximale des électrons émis.",
        "{-hp}",
    ], vis={
        "an_bil": dict(type="anim", nom="photoelec", x=40, y=72, h=624, seg=[[62.5, 74]]),
        "f_bil": dict(type="formule", titre="Relation d'Einstein", x=680, y=150, w=560, lignes=[
            dict(f="h × ν = Φ + E_c", cadre=True, taille=42),
            dict(f="E_c = h × ν − Φ", taille=40),
            dict(f="E_c = h × (ν − ν_0)", taille=40, n="E_c = ½ m_e v^2 · m_e = 9,11 × 10^-31 kg · mêmes unités partout")]),
        "redac": dict(type="liste", titre="Établir la relation · la rédaction attendue", items=[
            "Système : un électron du métal et le photon qu'il absorbe",
            "Énergie reçue : le photon apporte E = hν",
            "Énergie dépensée : au minimum Φ pour quitter le métal",
            "Conservation de l'énergie : E_c = hν − Φ"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
        "gr_ec": dict(type="graphe", titre="E_c en fonction de ν", x=330, y=110, w=640, h=520,
                      ax=dict(x=[0, 16], y=[-5, 5], gx=[4, 8, 12, 16], gy=[-4, -2, 2, 4], lx="ν (10^14 Hz)", ly="E_c (eV)"),
                      el=[dict(type="droite", pts=[[2.3 / H_EV, 0], [16, 16 * H_EV - 2.3]], c="vert", lbl="potassium", lp=[12.2, 4.3]),
                          dict(type="droite", pts=[[4.3 / H_EV, 0], [16, 16 * H_EV - 4.3]], c="sa", lbl="zinc · pente h", lp=[14.6, 1.0]),
                          dict(type="point", x=4.3 / H_EV, y=0, c="sa", lbl="ν_0 du zinc", lp=[10.4, -0.6]),
                          dict(type="droite", pts=[[0, -4.3], [4.3 / H_EV, 0]], c="sa", tir=True, ep=2.4)]),
        "ex_zn": dict(type="formule", titre="Exemple · le zinc éclairé à 200 nm", x=150, y=100, w=980, lignes=[
            dict(f="E_{photon} ≈ " + fr("1 240", "200") + " ≈ 6,2 eV"),
            dict(f="E_c = 6,2 − 4,3 = 1,9 eV"),
            dict(f="E_c = 1,9 × 1,60 × 10^-19 = 3,0 × 10^-19 J"),
            dict(f="v = √" + fr("2 E_c", "m_e") + " = √" + fr("2 × 3,0 × 10^-19", "9,11 × 10^-31")),
            dict(f="v ≈ 8,2 × 10^5 m·s^-1", cadre=True)]),
        "pieges": dict(type="liste", titre="Deux pièges", items=[
            "Mélanger J et eV : convertir avant de soustraire ; E_c en joules pour la vitesse",
            "Plus intense ≠ plus rapide : plus d'électrons, pas des électrons plus rapides"], marques=["✗", "✗"], x=150, y=190, w=980),
        "hp": dict(type="note", titre="Hors programme", cles=["maximale"], plus=True,
                   t="E_c = hν − Φ est l'énergie cinétique maximale : les électrons plus liés sortent moins vite.", x=170, y=220, w=940),
    }),

    # ================================================================ VII. cellules et applications
    dict(id="cellules", chap="Des photons au courant : les cellules", fond="aube", humeur="lumiere",
         retenir="Cellule photoélectrique : capteur (cathode, anode, générateur). Cellule photovoltaïque : générateur (silicium n et p, champ interne).",
         beats=[
        "{cpe}Première application directe : la cellule photoélectrique. Dans une ampoule vidée d'air, une cathode métallique fait face à une anode. "
        "Un générateur porte l'anode à un potentiel plus élevé. {cpe.1}Si la lumière est assez énergétique, des électrons sont arrachés à la cathode, "
        "attirés par l'anode, et reviennent par le circuit : l'ampèremètre mesure un courant.",
        "{cpe.2}Avec une lumière rouge, même très intense, au-delà de la longueur d'onde seuil : plus aucun courant. "
        "{cpe.3}Et avec un ultraviolet plus intense, le courant augmente, car il y a plus de photons, donc plus d'électrons.",
        "Le courant mesure donc l'intensité de la lumière : la cellule photoélectrique est un capteur. "
        "Elle a longtemps servi dans les portes automatiques.",
        "{-cpe}{an_pv}Deuxième application, la plus importante : la cellule photovoltaïque, celle des panneaux solaires. "
        "{pv_pts}{pv_pts.1}{an_pv.1}Pas de vide, pas de métal émetteur : une plaquette de silicium, un semi-conducteur, d'environ deux dixièmes de millimètre. "
        "La couche du dessus est dopée au phosphore, qui a un électron de plus que le silicium : des électrons en excès. "
        "La couche du dessous est dopée au bore, qui en a un de moins : des trous.",
        "{pv_pts.2}{an_pv.2}À la jonction, des électrons passent de la couche n vers la couche p et comblent des trous. "
        "La couche n devient positive près de la jonction, la couche p négative. Ces charges créent un champ électrique interne, permanent.",
        "{pv_pts.3}{an_pv.3}Un photon assez énergétique libère un électron d'un atome de silicium. Il ne sort pas du matériau : il est libéré à l'intérieur. "
        "{pv_pts.4}{an_pv.4}Le champ interne pousse cet électron vers la grille, la cathode. Il traverse le circuit, fait briller l'ampoule, "
        "et revient par l'anode, où il comble un trou.",
        "{pv_pts.5}{an_pv.5}Plus il y a de photons absorbés, plus il y a d'électrons libérés, plus le courant est fort.",
        "{-an_pv}{-pv_pts}{cols_c}Compare les deux. {cols_c.g}La cellule photoélectrique : l'électron sort du métal, il faut un générateur. C'est un capteur. "
        "{cols_c.d}La cellule photovoltaïque : l'électron reste dans le silicium, et c'est le champ interne qui le met en mouvement. "
        "Pas besoin de générateur : c'est elle, le générateur.",
        "Ce qui ne change pas : un photon agit sur un électron, il faut un seuil d'énergie, et le courant est proportionnel au nombre de photons absorbés.",
        "{-cols_c}{hp_si}Hors programme : pour le silicium, ce seuil vaut un virgule douze électronvolt. "
        "Les photons de longueur d'onde supérieure à environ mille cent nanomètres traversent la cellule sans effet.",
        "{-hp_si}{tab_ccd}{appli}Le programme demande aussi de citer des applications. Partout, la même règle : un photon est absorbé ou émis "
        "quand un électron change d'état, et son énergie vaut l'écart entre les deux états. "
        "{appli.1}Les capteurs d'appareil photo : chaque pixel compte les électrons libérés par les photons. "
        "{appli.2}Les diodes électroluminescentes font l'inverse : un électron qui retombe dans un trou émet un photon. "
        "{appli.3}La spectroscopie, vue au chapitre deux : les photons ultraviolets et visibles excitent les électrons des molécules, "
        "les photons infrarouges, moins énergétiques, font seulement vibrer les liaisons. "
        "{appli.4}Et le laser : une seule transition, donc des photons tous de même énergie, une couleur pure.",
        "{-appli}{-tab_ccd}",
    ], vis={
        "cpe": dict(type="illu", nom="cellpe", x=180, y=110, w=920, h=480),
        "an_pv": dict(type="anim", nom="cellule", x=40, y=72, h=624, seg=[[1.2, 9], [9, 19], [19, 30], [30, 42], [42, 52]]),
        "pv_pts": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=110, w=560, items=[
            "Couche n (phosphore) : électrons en excès · couche p (bore) : trous", "Jonction : un champ électrique interne",
            "Un photon libère un électron dans le silicium", "Le champ le pousse vers la grille, puis dans le circuit",
            "Plus de photons : plus de courant"]),
        "cols_c": dict(type="cols", g="Cellule photoélectrique", gq="l'électron sort du métal · il faut un générateur · un capteur",
                       d="Cellule photovoltaïque", dq="l'électron reste dans le silicium · champ interne · un générateur", vs="≠",
                       repere="Commun : un photon, un électron, un seuil"),
        "hp_si": dict(type="note", titre="Hors programme", cles=["seuil"], plus=True,
                      t="Le seuil du silicium vaut 1,12 eV : au-delà de 1 100 nm environ, les photons traversent sans effet.", x=170, y=220, w=940),
        "tab_ccd": dict(type="tableau", img="c4-capteur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .5],
                        legende="Capteur CCD d'un appareil photo, photo Aquilaa1, CC BY-SA 4.0"),
        "appli": dict(type="liste", titre="Photons et électrons au quotidien", items=[
            "Capteur d'appareil photo : photon → électron, on compte les électrons",
            "DEL : électron → photon, la couleur dépend de l'écart d'énergie",
            "Spectroscopie : UV-visible excite les électrons, IR fait vibrer les liaisons",
            "Laser : une seule transition, une couleur pure"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
    }),

    # ================================================================ VIII. rendement
    dict(id="rendement", chap="Le rendement d'une cellule", fond="nuit", humeur="calme",
         retenir="η = P_él,max / P_reçue, avec P_reçue = E × S et P_él = U × I. Le maximum de U × I se lit sur la courbe P = f(U).",
         beats=[
        "{tab_pan}Dernière notion du cours, très présente au bac : le rendement d'une cellule photovoltaïque. "
        "{f_eta}{f_eta.1}Le rendement, noté êta, compare ce que la cellule fournit à ce qu'elle reçoit : la puissance électrique maximale, divisée par la puissance lumineuse reçue.",
        "{f_eta.2}La puissance reçue, c'est l'éclairement fois la surface. L'éclairement se mesure au solarimètre, en watts par mètre carré. "
        "{f_eta.3}La puissance électrique, c'est U fois I.",
        "{f_eta.4}Attention : dans ce chapitre, la lettre E désigne deux choses. L'énergie d'un photon, en joules, et l'éclairement, en watts par mètre carré. "
        "C'est l'unité qui dit de quoi on parle.",
        "{-f_eta}{-tab_pan}{gr_iu}Pourquoi la puissance maximale ? Regarde la caractéristique de la cellule du TP six : l'intensité en fonction de la tension. "
        "{gr_iu.1}On l'obtient en branchant une résistance variable, et en mesurant U et I. "
        "Tant que la tension reste faible, le courant est presque constant. Puis il s'effondre.",
        "{gr_iu.2}La puissance, U fois I, c'est l'aire de ce rectangle. En court-circuit, U est nulle : aucune puissance. "
        "À vide, I est nul : aucune puissance non plus. Entre les deux, l'aire passe par un maximum.",
        "{gr_iu.3}Il se trouve au coude de la courbe : vers quatre virgule trois volts et cent sept milliampères.",
        "{-gr_iu}{gr_p}{gr_p.1}Sur la courbe de la puissance, c'est le sommet : {gr_p.2}P max vaut environ zéro virgule quarante-six watt.",
        "{-gr_p}{ex_tp}Calculons le rendement. {ex_tp.1}La cellule mesure dix centimètres sur dix : zéro virgule dix fois zéro virgule dix, "
        "un centième de mètre carré. {ex_tp.2}Sous quatre cents watts par mètre carré, elle reçoit quatre watts. "
        "{ex_tp.3}Êta égale zéro virgule quarante-six sur quatre : environ douze pour cent.",
        "{-ex_tp}{piege_ma}Le piège classique : le tableur donne I en milliampères. Quatre virgule trois fois cent sept, ça fait quatre cent soixante… "
        "milliwatts. Dans le rendement, il faut zéro virgule quarante-six watt.",
        "{-piege_ma}{chaine}{chaine.2}La chaîne énergétique le montre : sur toute l'énergie lumineuse reçue, environ quinze pour cent seulement devient électrique. "
        "{chaine.3}Le reste est perdu, surtout sous forme thermique. {chaine.4}",
        "{-chaine}{pertes}Pourquoi pas cent pour cent ? Le modèle du photon l'explique. "
        "{pertes.1}Une partie de la lumière est réfléchie, ou masquée par la grille. "
        "{pertes.2}Les photons trop peu énergétiques, l'infrarouge lointain, ne libèrent aucun électron. "
        "{pertes.3}Les photons très énergétiques libèrent un électron, mais leur surplus d'énergie part en chaleur : la cellule chauffe. "
        "{pertes.4}Et certains électrons se recombinent avant d'atteindre le circuit.",
        "{-pertes}{enjeux}Un rendement de quinze à vingt-deux pour cent, c'est faible devant un barrage, environ quatre-vingts pour cent, "
        "et du même ordre qu'une centrale ou un moteur thermique, environ trente. Mais l'énergie solaire est gratuite et renouvelable, "
        "sans combustible ni déchet en fonctionnement. Son défaut : elle est intermittente, la nuit, les nuages, ce qui impose un stockage.",
        "{-enjeux}",
    ], vis={
        "tab_pan": dict(type="tableau", img="c4-panneaux", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Centrale photovoltaïque sur un toit, Nüziders (Autriche), photo Asurnipal, CC BY-SA 4.0"),
        "f_eta": dict(type="formule", titre="Rendement d'une cellule photovoltaïque", x=150, y=110, w=980, lignes=[
            dict(f="η = " + fr("P_{él,max}", "P_{reçue}"), cadre=True, taille=52, n="sans unité, souvent en %"),
            dict(f="P_{reçue} = E × S", n="E : éclairement en W·m^-2 · S : surface en m^2"),
            dict(f="P_{él} = U × I", n="U en V · I en A (attention aux mA)"),
            dict(f="E : énergie d'un photon (J) ou éclairement (W·m^-2) : regarde l'unité", txt=True)]),
        "gr_iu": dict(type="graphe", titre="TP 6 · caractéristique I = f(U)", x=330, y=110, w=640, h=520,
                      ax=dict(x=[0, 6], y=[0, 140], gx=[1, 2, 3, 4, 5, 6], gy=[40, 80, 120], lx="U (V)", ly="I (mA)"),
                      el=[dict(type="courbe", pts=[list(p) for p in TP6], c="el", dur=2.2),
                          dict(type="balaye", pts=[list(p) for p in TP6], de=.6, a=5.6, dur=6, c="sa", fmt="P = {p} mW"),
                          dict(type="rect", x=4.3, y=107, c="vert", fmt="P_max ≈ {p} mW", dur=.6)]),
        "gr_p": dict(type="graphe", titre="TP 6 · puissance P = f(U)", x=330, y=110, w=640, h=520,
                     ax=dict(x=[0, 6], y=[0, 0.5], gx=[1, 2, 3, 4, 5, 6], gy=[0.1, 0.2, 0.3, 0.4, 0.5], lx="U (V)", ly="P (W)"),
                     el=[dict(type="courbe", pts=[list(p) for p in TP6_P], c="sa", dur=2.2),
                         dict(type="point", x=4.3, y=0.46, c="vert", proj=True, lbl="P_max ≈ 0,46 W", lp=[4.0, 0.49])]),
        "ex_tp": dict(type="formule", titre="Le rendement de la cellule du TP 6", x=150, y=150, w=980, lignes=[
            dict(f="S = 0,10 × 0,10 = 1,0 × 10^-2 m^2"),
            dict(f="P_{reçue} = E × S = 400 × 1,0 × 10^-2 = 4,0 W"),
            dict(f="η = " + fr("0,46", "4,0") + " ≈ 0,12 = 12 %", cadre=True)]),
        "piege_ma": dict(type="note", titre="Le piège des milliampères", cles=["milliwatts", "watt"],
                         t="4,3 V × 107 mA = 460 mW = 0,46 W. Dans le rendement, P en watts.", x=170, y=220, w=940),
        "chaine": dict(type="illu", nom="chaine", x=110, y=170, w=1060, h=420, eta=.15, boite="cellule photovoltaïque"),
        "pertes": dict(type="liste", titre="Pourquoi η < 100 %", items=[
            "Lumière réfléchie ou masquée par la grille", "Photons trop peu énergétiques : aucun électron",
            "Photons trop énergétiques : le surplus part en chaleur", "Électrons qui se recombinent en route"],
                       marques=["1", "2", "3", "4"], x=150, y=160, w=980),
        "enjeux": dict(type="cols", g="Atouts", gq="ressource gratuite, renouvelable · ni combustible ni déchet en fonctionnement",
                       d="Limites", dq="rendement 15 à 22 % · intermittence : stockage · courant continu : onduleur", vs="⚖",
                       repere="Barrage ≈ 80 % · centrale ou moteur thermique ≈ 30 %"),
    }),

    # ================================================================ IX. exercice 1 (simple)
    # λ = 254 nm : ν = 3,00e8 / 254e-9 = 1,18e15 Hz ; E = 6,63e-34 × 1,181e15 = 7,83e-19 J = 4,89 eV ; zinc : Ec = 0,59 eV
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="nuit", humeur="calme", beats=[
        "{ex1}Place aux exercices. Le premier, pour démarrer. Une lampe germicide, qui stérilise l'eau, émet un ultraviolet de longueur d'onde "
        "deux cent cinquante-quatre nanomètres. Quatre questions : sa fréquence, l'énergie d'un photon en joules puis en électronvolts, "
        "son domaine, et enfin : ces photons peuvent-ils arracher des électrons au zinc ?",
        "{-ex1}{pa1}Prends une feuille et ta calculatrice. Mets la vidéo sur pause, et cherche les quatre questions.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}C'est parti pour la correction. {s11}{s11.1}Question un : nu égale c sur lambda. "
        "{s11.2}Trois fois dix puissance huit, divisé par deux cent cinquante-quatre fois dix puissance moins neuf : "
        "{s11.3}un virgule dix-huit fois dix puissance quinze hertz.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Question deux : E égale h nu. {s12.2}Six virgule soixante-trois fois dix puissance moins trente-quatre, "
        "fois un virgule dix-huit fois dix puissance quinze : {s12.3}sept virgule quatre-vingt-trois fois dix puissance moins dix-neuf joule. "
        "{s12.4}Divisé par un virgule soixante fois dix puissance moins dix-neuf : quatre virgule quatre-vingt-neuf électronvolts. "
        "Vérification : mille deux cent quarante sur deux cent cinquante-quatre, environ quatre virgule quatre-vingt-huit. Parfait.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Question trois : deux cent cinquante-quatre nanomètres, c'est moins de quatre cents. "
        "{s13.2}Ultraviolet. D'ailleurs l'énergie dépasse trois virgule un électronvolt.",
        "{-s13}{ex1c.q4}{s14}{s14.1}Question quatre : il y a effet si l'énergie du photon dépasse le travail d'extraction. "
        "{s14.2}Quatre virgule quatre-vingt-neuf est plus grand que quatre virgule trois : oui, des électrons sont arrachés. "
        "{s14.3}Et leur énergie cinétique maximale vaut quatre virgule quatre-vingt-neuf moins quatre virgule trois : environ zéro virgule six électronvolt.",
        "{-s14}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="La lampe germicide", src="Exercice inventé pour la vidéo",
                    enonce=["Une lampe germicide, utilisée pour stériliser l'eau, émet une radiation de longueur d'onde λ = 254 nm."],
                    donnees=["h = 6,63 × 10^-34 J·s", "c = 3,00 × 10^8 m·s^-1", "1 eV = 1,60 × 10^-19 J", "zinc : Φ = 4,3 eV"],
                    questions=["Calculer la fréquence ν de la radiation.", "Calculer l'énergie d'un photon, en J puis en eV.",
                               "Dans quel domaine se situe cette radiation ?", "Ces photons peuvent-ils arracher des électrons au zinc ? Si oui, avec quelle E_c maximale ?"]),
        "pa1": dict(type="pause", t="Fréquence, énergie en J et en eV, domaine, effet sur le zinc."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="La lampe germicide",
                     donnees=["λ = 254 nm", "Φ_{zinc} = 4,3 eV"],
                     questions=["ν ?", "E en J puis en eV ?", "Domaine ?", "Effet sur le zinc ? E_c ?"]),
        "s11": dict(type="formule", titre="1 · La fréquence", x=540, y=150, w=700, lignes=[
            dict(f="ν = " + fr("c", "λ"), taille=40), dict(f="ν = " + fr("3,00 × 10^8", "254 × 10^-9"), taille=40),
            dict(f="ν = 1,18 × 10^15 Hz", cadre=True, taille=40)]),
        "s12": dict(type="formule", titre="2 · L'énergie d'un photon", x=540, y=120, w=700, lignes=[
            dict(f="E = h × ν", taille=38), dict(f="E = 6,63 × 10^-34 × 1,18 × 10^15", taille=38),
            dict(f="E = 7,83 × 10^-19 J", cadre=True, taille=38),
            dict(f="E = " + fr("7,83 × 10^-19", "1,60 × 10^-19") + " = 4,89 eV", cadre=True, taille=38)]),
        "s13": dict(type="formule", titre="3 · Le domaine", x=540, y=180, w=700, lignes=[
            dict(f="254 nm < 400 nm", taille=40), dict(f="ultraviolet (et E > 3,1 eV)", cadre=True, taille=40)]),
        "s14": dict(type="formule", titre="4 · L'effet sur le zinc", x=540, y=150, w=700, lignes=[
            dict(f="effet si E_{photon} ≥ Φ", taille=38),
            dict(f="4,89 eV > 4,3 eV : des électrons sont arrachés", ok=True, taille=30),
            dict(f="E_c = 4,89 − 4,3 ≈ 0,6 eV", cadre=True, taille=38)]),
    }),

    # ================================================================ X. exercice 2 (difficile)
    # 532 nm : E = 1,989e-25 / 532e-9 = 3,74e-19 J = 2,34 eV ; césium Φ = 1,90 eV : Ec = 0,44 eV = 7,0e-20 J ;
    # v = √(2 × 7,0e-20 / 9,11e-31) = 3,9e5 m/s ; N = 5,0e-3 / 3,74e-19 = 1,3e16 /s ; Ne = 0,21e-3 / 1,60e-19 = 1,3e15 /s ;
    # λ0 = 1,989e-25 / (1,90 × 1,60e-19) = 6,54e-7 m = 654 nm
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="nuit", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile, parce qu'il croise tout le chapitre. Un pointeur laser vert, de longueur d'onde cinq cent trente-deux nanomètres "
        "et de puissance cinq milliwatts, éclaire la cathode en césium d'une cellule photoélectrique. Le travail d'extraction du césium vaut un virgule quatre-vingt-dix électronvolt.",
        "On demande : l'énergie d'un photon ; s'il y a effet, l'énergie cinétique maximale et la vitesse des électrons ; "
        "le nombre de photons par seconde ; puis, sachant que le courant mesuré vaut zéro virgule vingt et un milliampère, "
        "la proportion de photons qui arrachent un électron. Et enfin : que se passe-t-il avec un laser infrarouge à sept cent quatre-vingts nanomètres ?",
        "{-ex2}{pa2}Celui-là demande du temps. Mets sur pause, et fais-le en entier avant de regarder la correction.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Question un : E égale h c sur lambda. "
        "{s21.2}Six virgule soixante-trois fois dix puissance moins trente-quatre, fois trois fois dix puissance huit, sur cinq cent trente-deux fois dix puissance moins neuf. "
        "{s21.3}Trois virgule soixante-quatorze fois dix puissance moins dix-neuf joule, {s21.4}soit deux virgule trente-quatre électronvolts.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Question deux : deux virgule trente-quatre est plus grand que un virgule quatre-vingt-dix. Il y a effet photoélectrique. "
        "{s22.2}E c égale deux virgule trente-quatre moins un virgule quatre-vingt-dix : zéro virgule quarante-quatre électronvolt. "
        "{s22.3}Pour la vitesse, on repasse en joules : sept virgule zéro fois dix puissance moins vingt. "
        "{s22.4}V égale la racine de deux E c sur m : environ trois virgule neuf fois dix puissance cinq mètres par seconde.",
        "{-s22}{ex2c.q3}{s23}{s23.1}Question trois : la puissance, c'est le nombre de photons par seconde fois l'énergie d'un photon. "
        "{s23.2}Donc N égale P sur E : cinq fois dix puissance moins trois, divisé par trois virgule soixante-quatorze fois dix puissance moins dix-neuf. "
        "{s23.3}Environ un virgule trois fois dix puissance seize photons par seconde.",
        "{-s23}{ex2c.q4}{s24}{s24.1}Question quatre : l'intensité, c'est la charge qui passe par seconde. Chaque électron porte la charge e. "
        "Donc le nombre d'électrons par seconde vaut I sur e. "
        "{s24.2}Zéro virgule vingt et un fois dix puissance moins trois, sur un virgule soixante fois dix puissance moins dix-neuf : un virgule trois fois dix puissance quinze. "
        "{s24.3}Dix fois moins que de photons. Environ un photon sur dix arrache un électron qui atteint l'anode.",
        "{-s24}{ex2c.q5}{s25}{s25.1}Question cinq : calculons la longueur d'onde seuil. Lambda zéro égale h c sur phi. "
        "{s25.2}Phi en joules : un virgule quatre-vingt-dix fois un virgule soixante fois dix puissance moins dix-neuf. On trouve environ six cent cinquante-quatre nanomètres. "
        "{s25.3}Sept cent quatre-vingts nanomètres, c'est au-dessus du seuil : chaque photon infrarouge est trop peu énergétique. "
        "Aucun courant. Et ça ne dépend pas de la puissance du laser : même cent fois plus puissant, rien.",
        "{-s25}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", y=60, titre="Un laser vert sur une cellule au césium", src="Exercice inventé pour la vidéo",
                    enonce=["Un pointeur laser vert (λ = 532 nm, P = 5,0 mW) éclaire la cathode en césium d'une cellule photoélectrique. "
                            "Le courant mesuré vaut I = 0,21 mA."],
                    donnees=["Φ_{césium} = 1,90 eV", "h = 6,63 × 10^-34 J·s", "c = 3,00 × 10^8 m·s^-1", "e = 1,60 × 10^-19 C", "m_e = 9,11 × 10^-31 kg"],
                    questions=["Énergie d'un photon, en J et en eV.", "Y a-t-il effet ? E_c maximale et vitesse des électrons.",
                               "Nombre de photons émis par seconde.", "Nombre d'électrons par seconde ; proportion de photons efficaces.",
                               "Que se passe-t-il avec un laser infrarouge à 780 nm ?"]),
        "pa2": dict(type="pause", t="Énergie, E_c et vitesse, photons par seconde, électrons par seconde, laser à 780 nm."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Laser vert et césium",
                     donnees=["λ = 532 nm", "P = 5,0 mW", "Φ = 1,90 eV", "I = 0,21 mA"],
                     questions=["E du photon ?", "Effet ? E_c, v ?", "Photons par seconde ?", "Électrons par seconde ?", "Laser à 780 nm ?"]),
        "s21": dict(type="formule", titre="1 · L'énergie d'un photon", x=540, y=130, w=700, lignes=[
            dict(f="E = " + fr("h × c", "λ"), taille=38), dict(f="E = " + fr("6,63 × 10^-34 × 3,00 × 10^8", "532 × 10^-9"), taille=36),
            dict(f="E = 3,74 × 10^-19 J", cadre=True, taille=38), dict(f="E = 2,34 eV", cadre=True, taille=38)]),
        "s22": dict(type="formule", titre="2 · Effet, énergie cinétique, vitesse", x=540, y=110, w=700, lignes=[
            dict(f="2,34 eV > 1,90 eV : effet photoélectrique", ok=True, taille=32),
            dict(f="E_c = 2,34 − 1,90 = 0,44 eV", taille=36),
            dict(f="E_c = 0,44 × 1,60 × 10^-19 = 7,0 × 10^-20 J", taille=32),
            dict(f="v = √" + fr("2 E_c", "m_e") + " ≈ 3,9 × 10^5 m·s^-1", cadre=True, taille=36)]),
        "s23": dict(type="formule", titre="3 · Photons par seconde", x=540, y=150, w=700, lignes=[
            dict(f="P = N × E", taille=38), dict(f="N = " + fr("P", "E") + " = " + fr("5,0 × 10^-3", "3,74 × 10^-19"), taille=38),
            dict(f="N ≈ 1,3 × 10^16 photons/s", cadre=True, taille=38)]),
        "s24": dict(type="formule", titre="4 · Électrons par seconde", x=540, y=140, w=700, lignes=[
            dict(f="I = N_e × e  ⇒  N_e = " + fr("I", "e"), taille=36),
            dict(f="N_e = " + fr("0,21 × 10^-3", "1,60 × 10^-19") + " ≈ 1,3 × 10^15 /s", taille=36),
            dict(f=fr("N_e", "N") + " ≈ 0,1 : environ 1 photon sur 10", cadre=True, taille=36)]),
        "s25": dict(type="formule", titre="5 · Le laser infrarouge", x=540, y=140, w=700, lignes=[
            dict(f="λ_0 = " + fr("h × c", "Φ"), taille=38),
            dict(f="λ_0 = " + fr("6,63 × 10^-34 × 3,00 × 10^8", "1,90 × 1,60 × 10^-19") + " ≈ 654 nm", taille=32),
            dict(f="780 nm > λ_0 : aucun électron, quelle que soit la puissance", ko=False, cadre=True, taille=30)]),
    }),

    # ================================================================ XI. exercice 3 (type bac)
    # S = 80 cm² = 8,0e-3 m² ; P reçue = 800 × 8,0e-3 = 6,4 W ; Pmax = 4,2 × 0,226 = 0,95 W ; η = 0,949 / 6,4 = 14,8 % ≈ 15 %
    # énergie : 0,95 W × 6 h = 5,7 Wh ; batterie 70 % : 4,0 Wh ; DEL 0,30 W × 8 h = 2,4 Wh
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac. Une lampe de jardin solaire. Pendant la journée, un petit module photovoltaïque de quatre-vingts centimètres carrés "
        "charge une batterie. La nuit, la batterie alimente une diode électroluminescente de zéro virgule trente watt, pendant huit heures.",
        "À midi, l'éclairement vaut huit cents watts par mètre carré. On donne la caractéristique du module, et la batterie ne restitue que soixante-dix pour cent de l'énergie reçue.",
        "{-ex3}{gr_j}{gr_j.1}Voici la caractéristique : le courant reste vers deux cent cinquante milliampères, puis s'effondre au-delà de quatre volts.",
        "{-gr_j}{ex3b}Cinq questions. Un : explique comment le module produit un courant. Deux : calcule la puissance reçue à midi. "
        "Trois : détermine la puissance maximale et le rendement. Quatre : donne deux raisons, liées au modèle du photon, pour lesquelles le rendement est loin de cent pour cent. "
        "Cinq : six heures de plein soleil suffisent-elles pour éclairer toute la nuit ?",
        "{-ex3b}{pa3}C'est un vrai sujet de bac : prends vingt minutes. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}Question un, une question de cours rédigée. "
        "{s31.1}Un photon assez énergétique est absorbé par le silicium et libère un électron. "
        "{s31.2}Le champ électrique interne, créé à la jonction entre la couche n et la couche p, sépare cet électron de son trou et le pousse vers la grille. "
        "{s31.3}L'électron parcourt le circuit extérieur : c'est le courant. Plus il y a de photons absorbés, plus le courant est intense.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Question deux. Attention aux centimètres carrés : quatre-vingts centimètres carrés, c'est huit fois dix puissance moins trois mètre carré. "
        "{s32.2}P reçue égale E fois S : huit cents fois huit fois dix puissance moins trois, six virgule quatre watts.",
        "{-s32}{ex3c.q3}{gr_jp}Question trois. On calcule U fois I pour chaque point, et on trace la puissance. {gr_jp.1}"
        "{gr_jp.2}Le maximum est atteint vers quatre virgule deux volts, avec deux cent vingt-six milliampères : environ zéro virgule quatre-vingt-quinze watt.",
        "{-gr_jp}{s33}{s33.1}Le rendement vaut zéro virgule quatre-vingt-quinze sur six virgule quatre : {s33.2}environ zéro virgule quinze. Quinze pour cent. "
        "C'est cohérent avec les panneaux du commerce.",
        "{-s33}{ex3c.q4}{s34}Question quatre. {s34.1}Les photons trop peu énergétiques, comme l'infrarouge lointain, ne libèrent aucun électron : leur énergie est perdue. "
        "{s34.2}Les photons très énergétiques libèrent un électron, mais le surplus d'énergie au-delà du seuil part en chaleur. "
        "{s34.3}On peut ajouter la lumière réfléchie ou masquée par la grille, et les recombinaisons.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Question cinq, la résolution de problème. Énergie produite en six heures au maximum : zéro virgule quatre-vingt-quinze watt fois six heures, cinq virgule sept wattheures. "
        "{s35.2}La batterie en restitue soixante-dix pour cent : environ quatre wattheures. "
        "{s35.3}La diode consomme zéro virgule trente watt pendant huit heures : deux virgule quatre wattheures. "
        "{s35.4}Quatre est plus grand que deux virgule quatre : oui, ça suffit.",
        "{s35.5}Et n'oublie pas le regard critique, toujours valorisé : l'éclairement n'est pas de huit cents watts toute la journée, le module ne travaille pas toujours "
        "à sa puissance maximale, et il chauffe. La marge est donc utile.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="La lampe de jardin solaire", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Le jour, un module photovoltaïque de surface S = 80 cm² charge une batterie. La nuit, la batterie alimente une DEL de 0,30 W pendant 8 h.",
                            "À midi, l'éclairement vaut E = 800 W·m⁻². La batterie restitue 70 % de l'énergie qu'elle reçoit."],
                    donnees=["S = 80 cm²", "E = 800 W·m^-2", "DEL : 0,30 W pendant 8 h", "batterie : 70 %"]),
        "gr_j": dict(type="graphe", titre="Document · caractéristique I = f(U) du module", x=330, y=110, w=640, h=520,
                     ax=dict(x=[0, 5.5], y=[0, 300], gx=[1, 2, 3, 4, 5], gy=[50, 100, 150, 200, 250, 300], lx="U (V)", ly="I (mA)"),
                     el=[dict(type="points", pts=[list(p) for p in JARDIN], c="el", pas=.12),
                         dict(type="courbe", pts=[list(p) for p in JARDIN], c="el", ep=2.4)]),
        "ex3b": dict(type="exo", niveau="bac", titre="La lampe de jardin solaire · questions",
                     questions=["Expliquer comment le module produit un courant.", "Calculer la puissance lumineuse reçue à midi.",
                                "Déterminer P_max et le rendement du module.", "Donner deux raisons, liées au modèle du photon, pour lesquelles η est loin de 100 %.",
                                "Six heures de plein soleil suffisent-elles pour éclairer toute la nuit ?"]),
        "pa3": dict(type="pause", t="Fonctionnement, puissance reçue, P_max et rendement, pertes, bilan sur une journée."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="La lampe de jardin",
                     donnees=["S = 80 cm²", "E = 800 W·m^-2", "DEL 0,30 W × 8 h", "batterie 70 %"],
                     questions=["Fonctionnement ?", "P_{reçue} ?", "P_max et η ?", "Pourquoi η < 100 % ?", "Assez pour la nuit ?"]),
        "s31": dict(type="liste", titre="1 · Comment le module produit un courant", items=[
            "Un photon assez énergétique libère un électron du silicium",
            "Le champ interne (jonction n-p) le sépare du trou et le pousse vers la grille",
            "Il parcourt le circuit : plus de photons, plus de courant"], marques=["1", "2", "3"], x=540, y=140, w=700),
        "s32": dict(type="formule", titre="2 · La puissance reçue", x=540, y=170, w=700, lignes=[
            dict(f="S = 80 cm² = 80 × 10^-4 = 8,0 × 10^-3 m^2", taille=34),
            dict(f="P_{reçue} = E × S = 800 × 8,0 × 10^-3 = 6,4 W", cadre=True, taille=34)]),
        "gr_jp": dict(type="graphe", titre="P = U × I en fonction de U", x=560, y=120, w=660, h=500,
                      ax=dict(x=[0, 5.5], y=[0, 1.0], gx=[1, 2, 3, 4, 5], gy=[0.2, 0.4, 0.6, 0.8, 1.0], lx="U (V)", ly="P (W)"),
                      el=[dict(type="courbe", pts=[list(p) for p in JARDIN_P], c="sa", dur=2.2),
                          dict(type="point", x=4.2, y=0.949, c="vert", proj=True, lbl="P_max ≈ 0,95 W", lp=[3.3, 0.98])]),
        "s33": dict(type="formule", titre="3 · Le rendement", x=540, y=200, w=700, lignes=[
            dict(f="η = " + fr("P_{max}", "P_{reçue}") + " = " + fr("0,95", "6,4"), taille=40),
            dict(f="η ≈ 0,15 = 15 %", cadre=True, taille=40)]),
        "s34": dict(type="liste", titre="4 · Pourquoi η est loin de 100 %", items=[
            "Photons trop peu énergétiques (IR lointain) : aucun électron",
            "Photons très énergétiques : le surplus part en chaleur",
            "Lumière réfléchie, grille, recombinaisons"], marques=["1", "2", "+"], x=540, y=150, w=700),
        "s35": dict(type="formule", titre="5 · Le bilan d'une journée", x=540, y=100, w=700, lignes=[
            dict(f="produite : 0,95 W × 6 h = 5,7 W·h", taille=32),
            dict(f="restituée : 0,70 × 5,7 ≈ 4,0 W·h", taille=32),
            dict(f="consommée : 0,30 W × 8 h = 2,4 W·h", taille=32),
            dict(f="4,0 > 2,4 : oui, ça suffit", cadre=True, ok=True, taille=34),
            dict(f="Regard critique : éclairement variable, module pas toujours au maximum, échauffement.", txt=True)]),
    }),

    # ================================================================ XII. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{carte}Récapitulons tout le chapitre. Au centre, le photon, grain d'énergie h nu. "
        "{carte.1}Côté onde : lambda égale c sur nu, et le piège des nanomètres. "
        "{carte.2}Côté atome : le photon absorbé ou émis porte exactement l'écart entre deux niveaux. "
        "{carte.3}Côté effet photoélectrique : un photon, un électron, tout ou rien ; h nu égale phi plus E c. "
        "{carte.4}Côté cellules : le courant vient des électrons libérés, et le rendement compare la puissance électrique maximale à la puissance reçue.",
        "{-carte}{bac}Et voici ce que le bac peut te demander, à cocher. "
        "{bac.1}Calculer l'énergie d'un photon, en joules et en électronvolts. "
        "{bac.2}Exploiter un diagramme de niveaux. "
        "{bac.3}Décrire l'effet photoélectrique, ses quatre faits, et son importance historique. "
        "{bac.4}L'interpréter avec le modèle du photon. "
        "{bac.5}Établir le bilan d'énergie d'Einstein. "
        "{bac.6}Citer des applications, expliquer une cellule. "
        "{bac.7}Et déterminer un rendement.",
        "Si tu sais faire ces sept choses, tu as tout le bagage du chapitre. Le site t'attend avec d'autres exercices, le TP six corrigé et la fiche mémo. "
        "Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-bac}",
    ], vis={
        "carte": dict(type="carte", centre="LE PHOTON · E = hν", branches=[
            dict(t="L'onde", items=["λ = c / ν", "λ en mètres (1 nm = 10^-9 m)", "UV · visible · IR"]),
            dict(t="L'atome", items=["|ΔE| = hν = hc / λ", "absorption : tout ou rien", "émission : raies"]),
            dict(t="L'effet photoélectrique", items=["un photon, un électron", "hν ≥ Φ · λ ≤ λ_0", "hν = Φ + E_c"]),
            dict(t="Les cellules", items=["capteur ou générateur", "champ interne n-p", "η = P_max / (E × S)"])]),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Calculer E = hν = hc/λ, en J et en eV", "Exploiter un diagramme de niveaux d'énergie",
            "Décrire l'effet photoélectrique et son histoire", "L'interpréter avec le modèle du photon",
            "Établir hν = Φ + E_c par un bilan d'énergie", "Citer des applications, expliquer une cellule",
            "Déterminer un rendement"], marques=["✓"] * 7, x=170, y=80, w=940, petit=True),
    }),
]

QUIZ = [
    dict(q="On rend un faisceau rouge monochromatique deux fois plus intense. Ses photons…",
         r=["portent deux fois plus d'énergie", "sont deux fois plus nombreux, avec la même énergie", "ont une longueur d'onde deux fois plus courte"],
         ok=1, ex="L'énergie d'un photon ne dépend que de sa fréquence : E = hν. Plus intense, c'est plus de photons par seconde (P = N hν).", voir="fais"),
    dict(q="Dans E = hc/λ, la longueur d'onde d'un laser à 633 nm s'écrit…",
         r=["633 × 10⁻⁶ m", "633 × 10⁻⁹ m", "633 m"], ok=1,
         ex="1 nm = 10⁻⁹ m. C'est le piège d'unité le plus fréquent du chapitre.", voir="piege_nm"),
    dict(q="Un atome d'hydrogène au fondamental (−13,6 eV) reçoit un photon de 11,0 eV ; les niveaux suivants sont −3,40 et −1,51 eV. Que se passe-t-il ?",
         r=["Il l'absorbe et monte à −2,6 eV", "Il prend 10,2 eV et laisse repartir le reste", "Rien : aucun niveau ne vaut −2,6 eV"],
         ok=2, ex="L'absorption est du tout ou rien : le photon doit apporter exactement un écart entre deux niveaux.", voir="an_ph"),
    dict(q="Une lampe rouge très puissante éclaire une plaque de zinc (Φ = 4,3 eV) pendant des heures. On observe…",
         r=["une émission lente d'électrons", "aucune émission d'électrons", "une émission dès que la plaque chauffe"],
         ok=1, ex="Chaque photon rouge apporte moins de 2 eV, moins que Φ, et un électron n'additionne pas l'énergie de deux photons.", voir="tab_faits"),
    dict(q="Le travail d'extraction du potassium vaut 2,3 eV. Sa longueur d'onde seuil λ₀ = hc/Φ vaut environ…",
         r=["290 nm", "540 nm", "1 100 nm"], ok=1,
         ex="λ₀ ≈ 1 240 / 2,3 ≈ 540 nm. Il y a effet pour λ < 540 nm : le bleu et le vert, pas le rouge.", voir="metaux"),
    dict(q="Des photons de 6,2 eV éclairent du zinc (Φ = 4,3 eV). L'énergie cinétique maximale des électrons vaut…",
         r=["10,5 eV", "1,9 eV", "6,2 eV"], ok=1, ex="Ec = hν − Φ = 6,2 − 4,3 = 1,9 eV.", voir="ex_zn"),
    dict(q="Sur le graphique Ec = f(ν), la pente de la droite est…",
         r=["le travail d'extraction Φ", "la constante de Planck h, la même pour tous les métaux", "la fréquence seuil ν₀"],
         ok=1, ex="Ec = hν − Φ : une droite de pente h. Elle coupe l'axe des fréquences en ν₀ et l'axe vertical en −Φ.", voir="gr_ec"),
    dict(q="Dans une cellule photovoltaïque, le rôle du champ électrique interne est…",
         r=["d'arracher les électrons aux atomes de silicium", "de séparer l'électron libéré de son trou et de le pousser vers la grille", "de fournir l'énergie du courant"],
         ok=1, ex="Ce sont les photons qui libèrent les électrons ; le champ de la jonction n-p les met en mouvement dans un sens unique.", voir="an_pv"),
    dict(q="Une cellule de 100 cm² reçoit 400 W/m² et fournit au mieux 0,46 W. Son rendement vaut…",
         r=["0,12 %", "12 %", "46 %"], ok=1, ex="P reçue = 400 × 0,01 = 4,0 W ; η = 0,46 / 4,0 ≈ 12 %.", voir="ex_tp"),
    dict(q="Pourquoi une cellule au silicium ne peut-elle pas convertir toute l'énergie lumineuse ?",
         r=["Parce que les photons trop faibles ne libèrent rien et que le surplus des photons énergétiques part en chaleur",
            "Parce que la lumière solaire est trop intense", "Parce que le silicium conduit mal le courant"],
         ok=0, ex="Ces deux pertes, les plus grosses, découlent directement du modèle du photon.", voir="pertes"),
]

CREDITS = [
    "Portraits : Albert Einstein par Herman Mishkin, 1921 (domaine public) ; Max Planck, Bundesarchiv Bild 183-R0116-504, CC BY-SA 3.0 de ; "
    "Heinrich Hertz par Robert Krewaldt (domaine public) ; Robert Millikan, Fondation Nobel (domaine public) ; James Clerk Maxwell, gravure de G. J. Stodart, 1890 (domaine public).",
    "Photos : calculatrice solaire, Evan-Amos (domaine public) ; le Soleil, NASA/SDO (domaine public) ; nébuleuse d'Orion, NASA, ESA, M. Robberto, Hubble (domaine public) ; "
    "spectre à travers un prisme, Pittigrilli, CC BY-SA 4.0 ; capteur CCD, Aquilaa1, CC BY-SA 4.0 ; centrale photovoltaïque de Nüziders, Asurnipal, CC BY-SA 4.0.",
    "Images trouvées sur Wikimedia Commons. Animations, schémas et graphiques : faits pour le site. Valeurs du TP 6 : tableur du professeur. "
    "Les trois exercices sont inventés pour la vidéo.",
]
