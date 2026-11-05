"""SVT, chapitre 3 du thème 1.A (Mme Philip) : « L'évolution du génome au sein des populations » — le cours en vidéo.

Même chaîne que les vidéos de physique-chimie (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les
mots) ; moteur svt/serie/moteur.js (type mental = carte mentale du thème 1.A) ; illustrations propres au chapitre dans
svt/serie/illu-svt-ch3.js (melange, population, croisement, barres, derive9, buri, fondateur, beringie, amish, tri,
reseau, denisova, speciation).
Contenu : les pages t3 et t3b du site (svt/index.html), rien au-delà. Ce qui dépasse le programme est dit « hors
programme » ; l'exemple du papillon aurore (dimorphisme sexuel) ne vient pas du cours et la voix le dit. Les résultats
de l'activité 1 (scénarios) et l'histogramme de Buri sont des SIMULATIONS du protocole (graines fixes ci-dessous),
annoncées comme telles : la classe n'a reçu aucune courbe corrigée. L'explication du groupe O est « proposée », comme
sur le site. Les trois exercices sont inventés pour la vidéo (valeurs recalculées en commentaire).
Usage : python3 outils/serie-philo/verifier.py svt_ch3 ; puis generer.py svt_ch3 ; chevauchements.py svt-ch3 ; fermer.py svt_ch3.
"""
import random

SITE = "svt"
CODE = "svt-ch3"
NOTION = "L'évolution du génome au sein des populations"
NUM = 3
TITRE = "L'évolution du génome au sein des populations"
SUIVANT = "Chapitre 4 · La diversité non génétique du vivant"
PRONONCIATION = {"p": "pé", "q": "ku", "m": "ème", "Hardy": "Hardi", "Weinberg": "Vaïnbergue", "Buri": "Bouri",
                 "bw75": "bé double-vé soixante-quinze", "bw": "bé double-vé", "AceR": "assé erre", "AceS": "assé esse", "Culex": "Culèxe",
                 "pipiens": "pipiènce", "Ellis-van": "Élisse-vane", "Creveld": "Crévelde", "HLA": "ache èl a",
                 "Kell": "Kèl", "Doolittle": "Doulitel", "Denisova": "Dénissova", "Mezmaiskaya": "Mezmaïskaïa",
                 "Vindija": "Vindiya", "Han": "Hane", "lugubris": "lugubrisse", "paralugubris": "paralugubrisse",
                 "Mendel": "Mendèle", "Philip": "Philippe", "Huttérites": "Hutérites", "Linné": "Liné"}


def fr(a, b):
    """Fraction affichée (texte enrichi du moteur)."""
    return f"[[{a}|{b}]]"


# ---------------------------------------------------------------- simulations (graines fixes, rendu reproductible)
def _wf(n, p0, gens, graine):
    """Modèle de Wright-Fisher : n individus diploïdes, 2n allèles tirés au hasard à chaque génération."""
    r, p, out = random.Random(graine), p0, [(0, p0)]
    for g in range(1, gens + 1):
        p = sum(r.random() < p for _ in range(2 * n)) / (2 * n)
        out.append((g, round(p, 3)))
    return out


def _selection(p0, gens, n, graine):
    """Valeurs sélectives A//A = 1, A//B = 0,8, B//B = 0,8 (activité 1, scénario 4), population de n individus."""
    r, p, out = random.Random(graine), p0, [(0, p0)]
    for g in range(1, gens + 1):
        q = 1 - p
        pp = (p * p + .8 * p * q) / (p * p + 1.6 * p * q + .8 * q * q)
        p = sum(r.random() < pp for _ in range(2 * n)) / (2 * n)
        out.append((g, round(p, 3)))
    return out


def _buri(graine, npop=107, n=16, gens=19):
    """Histogramme des 107 populations (nombre d'allèles bw75 sur 32) à chaque génération."""
    r, ks, hist = random.Random(graine), [n] * npop, []
    for g in range(gens + 1):
        h = [0] * (2 * n + 1)
        for k in ks:
            h[k] += 1
        hist.append(h)
        ks = [sum(r.random() < k / (2 * n) for _ in range(2 * n)) for k in ks]
    return hist


S1 = _wf(1000, .5, 10, 3)            # témoin : 1 000 individus
S2a, S2b = _wf(9, .5, 11, 1), _wf(9, .5, 11, 23)     # dérive : fixation, puis perte
S3a, S3b = _wf(9, .2, 11, 2), _wf(9, .2, 11, 7)      # effet fondateur (20 %) : perte, puis hausse par hasard
S4a, S4b = _selection(.5, 10, 1000, 5), _selection(.5, 10, 1000, 6)
BURI = _buri(6)                       # génération 19 : 15 populations ont perdu bw75, 18 l'ont fixé
CULEX = [(1968, 0), (1972, .01), (1976, .02), (1980, .04), (1982, .1), (1984, .22), (1986, .35), (1988, .45),
         (1990, .52), (1992, .57), (1994, .6), (1996, .61), (1998, .6), (2000, .6)]   # allure du graphique du manuel


def gr_freq(titre, courbes, y=110, x=300, w=680, h=520, gens=10, note=None):
    """Graphique fréquence = f(génération)."""
    el = [dict(type="courbe", pts=[list(p) for p in c[0]], c=c[1], lbl=c[2], lp=c[3]) for c in courbes]
    if note:
        el.append(dict(type="texte", x=note[0], y=note[1], t=note[2], c="iv2"))
    return dict(type="graphe", titre=titre, x=x, y=y, w=w, h=h,
                ax=dict(x=[0, gens + .5], y=[0, 1.05], gx=list(range(2, gens + 1, 2)), gy=[.25, .5, .75, 1],
                        lx="générations", ly="fréquence de l'allèle"), el=el)


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="foret", humeur="mystere", carton=False, beats=[
        "{ouv_m}Voici la carte mentale du thème un, partie A, telle que Madame Philip l'a dessinée : génétique et évolution. "
        "Quatre chapitres. Le premier expliquait comment chaque individu reçoit un génotype unique. Le deuxième, comment les génomes se complexifient.",
        "{ouv_m.1}Ce chapitre-ci, le troisième, change d'échelle. On ne regarde plus un individu, ni une cellule, "
        "mais une population entière, et ce que deviennent ses allèles au fil des générations.",
        "{ouv_m.2}D'abord, un modèle : l'équilibre de Hardy-Weinberg. Il prédit ce qui se passerait dans une population idéale, sans évolution. "
        "{ouv_m.3}Ensuite, les écarts à cet équilibre : la dérive génétique, l'effet fondateur, la sélection naturelle, "
        "avec les drosophiles de Buri, les Amish, le groupe sanguin O des Amérindiens et les moustiques du Languedoc. "
        "{ouv_m.4}Et pour finir, une question plus délicate qu'elle n'en a l'air : qu'est-ce qu'une espèce ?",
        "{ouv_m.5}Les calculs de Hardy-Weinberg tombent souvent au bac. Tu les feras avec moi, pas à pas, puis seul, sur trois exercices corrigés.",
        "{-ouv_m}{titre}",
        ("P", 3.2),
    ], vis={
        "ouv_m": dict(type="mental", vers=["t1a", "c3", "c3a", "c3b", "c3c", "c3"], pousse=True),
        "titre": dict(type="titre", sur="SVT · Thème 1 · Chapitre 3", t="L'évolution du génome au sein des populations",
                      sous="Le cours complet, de zéro au bac"),
    }),

    # ================================================================ A. Hardy-Weinberg : l'énigme
    dict(id="enigme", chap="L'énigme de la diversité", fond="foret", humeur="mystere",
         retenir="L'hérédité par mélange est fausse : les allèles se transmettent intacts. D'où la persistance des variants.",
         beats=[
        "{m_a}{m_a.1}Première branche de la carte : l'équilibre de Hardy-Weinberg. Et pour comprendre pourquoi on en a eu besoin, il faut remonter vers mille huit cents.",
        "{-m_a}{mel}À cette époque, on ne connaît pas la méiose. Et la théorie admise, c'est l'{!hérédité par mélange} : "
        "le descendant de deux parents aurait un phénotype intermédiaire, un mélange des deux. "
        "{mel.1}L'exemple de la diapositive : une souris noire croisée avec une souris blanche donnerait une souris grise.",
        "{mel.2}Si c'était vrai, chaque variant serait dilué un peu plus à chaque génération. Au bout de quelques générations, tout le monde serait gris : "
        "tous les individus se ressembleraient.",
        "Or on observe l'inverse. Les variants persistent. Regarde une population humaine : une immense diversité de phénotypes, "
        "génération après génération. C'est l'énigme de la persistance des variants génétiques.",
        "{mel.3}La solution, tu la connais depuis le chapitre un. Les allèles se transmettent intacts, par la méiose et la fécondation. "
        "Un hétérozygote peut avoir un phénotype intermédiaire, mais ses deux allèles restent distincts. "
        "{mel.4}Et ils peuvent se retrouver séparés dans ses gamètes. Mendel l'avait montré dès les années mille huit cent soixante.",
        "{-mel}{hw}Reste à comprendre comment les fréquences des allèles se comportent dans une population entière. "
        "En mille neuf cent huit, deux scientifiques répondent, chacun de son côté : le mathématicien britannique Godfrey Harold Hardy, "
        "et le médecin allemand Wilhelm Weinberg.",
        "{-hw}{pb}D'où la question à laquelle tout le chapitre répond : {pb.1}comment les fréquences des allèles évoluent-elles dans une population, "
        "au fil des générations, et pourquoi s'écartent-elles de l'équilibre prévu par le modèle de Hardy-Weinberg ?",
        "{-pb}",
    ], vis={
        "m_a": dict(type="mental", vers=["c3", "c3a"]),
        "mel": dict(type="illu", nom="melange", x=170, y=96, w=940, h=560),
        "hw": dict(type="cols", g="Godfrey Harold Hardy", gq="mathématicien britannique", d="Wilhelm Weinberg", dq="médecin allemand",
                   vs="1908", repere="Deux découvertes indépendantes, la même année"),
        "pb": dict(type="def", terme="La question du chapitre", cles=["fréquences", "équilibre"],
                   t="Comment les fréquences des allèles évoluent-elles dans une population au fil des générations, et pourquoi s'écartent-elles de l'équilibre prévu par le modèle de Hardy-Weinberg ?",
                   x=170, y=190, w=940),
    }),

    # ================================================================ population et fréquences
    dict(id="frequences", chap="Population et fréquences alléliques", fond="foret", humeur="calme",
         retenir="f(A) = (2 × nombre de A//A + nombre de A//m) / 2N. Et f(m) = 1 − f(A).",
         beats=[
        "{defs}Trois définitions, à savoir par cœur. {defs.1}Une population, c'est un groupe d'individus de la même espèce, "
        "vivant dans une même zone, pouvant se reproduire entre eux et engendrer une descendance fertile.",
        "{defs.2}Son patrimoine génétique, c'est l'ensemble des allèles présents dans la population. "
        "{defs.3}Et chaque allèle a une fréquence allélique : sa proportion parmi tous les exemplaires du gène présents dans la population.",
        "{-defs}{pop}Comptons ensemble. Voici une petite population de vingt-cinq individus, pour un gène à deux allèles, A et m. "
        "{pop.1}Chaque individu est diploïde : il porte deux exemplaires du gène, un par moitié de disque.",
        "{pop.2}Les neuf homozygotes A A apportent chacun deux allèles A : dix-huit. "
        "{pop.3}Les douze hétérozygotes A m en apportent un chacun : douze. Les homozygotes m m n'en apportent aucun.",
        "{pop.4}Vingt-cinq individus diploïdes, cela fait cinquante exemplaires du gène. Trente allèles A sur cinquante : "
        "la fréquence de A vaut zéro virgule six. Et celle de m, un moins zéro virgule six : zéro virgule quatre.",
        "{-pop}{f_fa}D'où la formule générale. {f_fa.1}Pour N individus, il y a deux N exemplaires du gène. "
        "{f_fa.2}La fréquence de A égale deux fois le nombre de A A, plus le nombre de A m, le tout divisé par deux N. "
        "{f_fa.3}Et la fréquence de m égale un moins la fréquence de A.",
        "{-f_fa}{pa_f}À toi. Une population de mille individus compte trois cent soixante A A, quatre cent quatre-vingts A m et cent soixante m m. "
        "Calcule la fréquence de A, et les trois fréquences génotypiques.",
        "{pa_f.stop}{-pa_f}{f_ex}Correction. {f_ex.1}Mille individus, donc deux mille exemplaires du gène. "
        "{f_ex.2}Allèles A : deux fois trois cent soixante, plus quatre cent quatre-vingts : mille deux cents. "
        "{f_ex.3}La fréquence de A vaut mille deux cents sur deux mille : zéro virgule six. Celle de m, zéro virgule quatre.",
        "{f_ex.4}Les fréquences génotypiques, elles, sont les proportions de chaque génotype : "
        "zéro virgule trente-six pour A A, zéro virgule quarante-huit pour A m, zéro virgule seize pour m m. "
        "Ne confonds jamais les deux : fréquence d'un allèle, fréquence d'un génotype.",
        "{-f_ex}",
    ], vis={
        "defs": dict(type="liste", titre="Trois définitions", items=[
            "Population : individus de la même espèce, dans une même zone, qui se reproduisent entre eux (descendance fertile)",
            "Patrimoine génétique : l'ensemble des allèles présents dans la population",
            "Fréquence allélique : la proportion d'un allèle parmi tous les exemplaires du gène"], marques=["1", "2", "3"],
            x=130, y=150, w=1020),
        "pop": dict(type="illu", nom="population", x=100, y=110, w=1080, h=500),
        "f_fa": dict(type="formule", titre="Calculer une fréquence allélique (gène à deux allèles A et m)", x=150, y=150, w=980, lignes=[
            dict(f="N individus diploïdes → 2N exemplaires du gène"),
            dict(f="f(A) = " + fr("2 × (A//A) + (A//m)", "2N"), cadre=True, taille=46, n="les homozygotes comptent deux fois, les hétérozygotes une fois"),
            dict(f="f(m) = 1 − f(A)")]),
        "pa_f": dict(type="pause", t="1 000 individus : 360 A//A, 480 A//m, 160 m//m. Calcule f(A), f(m) et les fréquences génotypiques."),
        "f_ex": dict(type="formule", titre="Correction · 360 A//A, 480 A//m, 160 m//m", x=150, y=120, w=980, lignes=[
            dict(f="2N = 2 × 1 000 = 2 000 exemplaires du gène"),
            dict(f="allèles A : 2 × 360 + 480 = 1 200"),
            dict(f="f(A) = " + fr("1 200", "2 000") + " = 0,6  ·  f(m) = 0,4", cadre=True),
            dict(f="génotypes : f(A//A) = 0,36 · f(A//m) = 0,48 · f(m//m) = 0,16", taille=32)]),
    }),

    # ================================================================ la loi de Hardy-Weinberg
    dict(id="loi", chap="La loi de Hardy-Weinberg", fond="foret", humeur="lumiere",
         retenir="p + q = 1. À l'équilibre : f(A//A) = p², f(A//m) = 2pq, f(m//m) = q², et p² + 2pq + q² = 1.",
         beats=[
        "{f_pq}On note p la fréquence de l'allèle A, et q celle de l'allèle m. "
        "{f_pq.1}Comme il n'y a que deux allèles : p plus q égale un.",
        "{-f_pq}{cr}Imaginons maintenant que les gamètes se rencontrent au hasard. {cr.1}Un gamète, mâle ou femelle, porte l'allèle A avec la probabilité p, "
        "et l'allèle m avec la probabilité q. On construit le tableau de croisement, comme un carré de côté un.",
        "{cr.2}Un gamète A rencontre un gamète A : probabilité p fois p, p au carré. C'est la fréquence des homozygotes A A.",
        "{cr.3}A rencontre m : p fois q. Mais il y a deux cases ! A peut venir du père et m de la mère, ou l'inverse. "
        "Les hétérozygotes ont donc la fréquence deux p q.",
        "{cr.4}Et m rencontre m : q au carré, la fréquence des homozygotes m m.",
        "{cr.5}Les quatre cases remplissent tout le carré : p au carré, plus deux p q, plus q au carré, égale un. "
        "C'est simplement p plus q, au carré : un au carré, un.",
        "{-cr}{f_hw}Voilà la loi de Hardy-Weinberg. {f_hw.1}{f_hw.2}{f_hw.3}"
        "Fréquence des A A : p au carré. Fréquence des A m : deux p q. Fréquence des m m : q au carré. "
        "{f_hw.4}Et p au carré plus deux p q plus q au carré égale un.",
        "{-f_hw}{piege_hw}Deux pièges d'écriture. {piege_hw.1}La diapositive écrit « p deux plus deux p q plus q deux », sans le « égale un » : "
        "toi, écris-le toujours. Et l'hétérozygote compte deux fois. Si tu écris p q au lieu de deux p q, ta somme ne fait plus un.",
        "{-piege_hw}",
    ], vis={
        "f_pq": dict(type="formule", titre="Deux allèles, deux fréquences", x=230, y=210, w=820, lignes=[
            dict(f="f(A) = p  ·  f(m) = q", taille=44),
            dict(f="p + q = 1", cadre=True, taille=54)]),
        "cr": dict(type="illu", nom="croisement", x=60, y=100, w=1160, h=560, p=.6),
        "f_hw": dict(type="formule", titre="La loi de Hardy-Weinberg", x=230, y=120, w=820, lignes=[
            dict(f="f(A//A) = p²", taille=40), dict(f="f(A//m) = 2pq", taille=40), dict(f="f(m//m) = q²", taille=40),
            dict(f="p² + 2pq + q² = 1", cadre=True, taille=52, n="c'est (p + q)² = 1")]),
        "piege_hw": dict(type="note", titre="Deux pièges d'écriture", cles=["=", "deux"],
                         t="Écris toujours « p² + 2pq + q² = 1 », avec le = 1. L'hétérozygote compte deux fois : 2pq, pas pq.",
                         etape="A du père et m de la mère, ou m du père et A de la mère : deux façons d'obtenir A//m.",
                         x=170, y=200, w=940),
    }),

    # ================================================================ l'équilibre
    dict(id="equilibre", chap="Un équilibre : pas d'évolution", fond="foret", humeur="calme",
         retenir="Dans le modèle, les fréquences alléliques et génotypiques restent constantes : il n'y a pas d'évolution.",
         beats=[
        "{demo}Que devient la fréquence de A à la génération suivante ? Faisons le calcul. "
        "{demo.1}Les allèles A des descendants viennent de deux sources : tous ceux des homozygotes A A, "
        "et la moitié de ceux des hétérozygotes. {demo.2}Donc la nouvelle fréquence de A vaut p au carré, plus la moitié de deux p q : p au carré plus p q.",
        "{demo.3}On factorise par p : p fois, p plus q. {demo.4}Et p plus q vaut un. Il reste p. Exactement la même fréquence qu'au départ.",
        "{-demo}{gr_eq}{gr_eq.1}Sur un graphique, la fréquence de A reste une droite horizontale, génération après génération. "
        "{gr_eq.2}{gr_eq.3}{gr_eq.4}Et comme les fréquences des génotypes se calculent à partir de p et q, elles restent constantes elles aussi : "
        "trente-six, quarante-huit et seize pour cent, indéfiniment.",
        "{-gr_eq}{mot}La conclusion de la diapositive dix, à retenir mot pour mot : {mot.1}il n'y a donc pas d'évolution dans ce cadre de modélisation théorique.",
        "C'est la solution de l'énigme du début : la reproduction sexuée, à elle seule, ne fait disparaître aucun allèle. "
        "Les variants persistent. La souris grise n'arrive jamais.",
        "{-mot}",
    ], vis={
        "demo": dict(type="formule", titre="Pourquoi la fréquence de A ne change pas", x=150, y=130, w=980, lignes=[
            dict(f="les A des descendants : tous ceux des A//A + la moitié de ceux des A//m", txt=True, taille=30),
            dict(f="p′ = p² + " + fr("1", "2") + " × 2pq = p² + pq", taille=44),
            dict(f="p′ = p (p + q)", taille=44),
            dict(f="p′ = p × 1 = p", cadre=True, taille=50, n="la fréquence n'a pas bougé")]),
        "gr_eq": dict(type="graphe", titre="Une population à l'équilibre (p = 0,6)", x=300, y=110, w=680, h=520,
                      ax=dict(x=[0, 10.5], y=[0, 1.05], gx=[2, 4, 6, 8, 10], gy=[.25, .5, .75, 1], lx="générations", ly="fréquence"),
                      el=[dict(type="courbe", pts=[[0, .6], [10, .6]], c="sa", lbl="f(A) = p = 0,6", lp=[6.2, .69]),
                          dict(type="courbe", pts=[[0, .48], [10, .48]], c="te", lbl="A//m : 2pq = 0,48", lp=[6.2, .42]),
                          dict(type="courbe", pts=[[0, .36], [10, .36]], c="or", lbl="A//A : p² = 0,36", lp=[.3, .31]),
                          dict(type="courbe", pts=[[0, .16], [10, .16]], c="ca", lbl="m//m : q² = 0,16", lp=[6.2, .1])]),
        "mot": dict(type="def", terme="Diapositive 10 · mot pour mot", cles=["pas", "d'évolution"],
                    t="Il n'y a donc pas d'évolution dans ce cadre de modélisation théorique.",
                    etape="La reproduction sexuée, à elle seule, ne fait disparaître aucun allèle : les variants persistent.",
                    x=170, y=210, w=940),
    }),

    # ================================================================ vérifier l'équilibre
    dict(id="verifier", chap="Vérifier qu'une population est à l'équilibre", fond="foret", humeur="lumiere",
         retenir="Méthode : p et q d'après les effectifs observés ; effectifs attendus p²N, 2pqN, q²N ; comparer.",
         beats=[
        "{meth}Voici la méthode qui tombe au bac, en trois étapes. {meth.1}Un : calculer p et q à partir des effectifs observés. "
        "{meth.2}Deux : calculer les effectifs attendus à l'équilibre : p au carré fois N, deux p q fois N, q au carré fois N. "
        "{meth.3}Trois : comparer les effectifs observés et attendus.",
        "{-meth}{b1}Reprenons la population de tout à l'heure : trois cent soixante, quatre cent quatre-vingts, cent soixante. "
        "{b1.1}Voici les effectifs observés. {b1.2}Avec p égal zéro virgule six, on attend zéro virgule trente-six fois mille, trois cent soixante ; "
        "zéro virgule quarante-huit fois mille, quatre cent quatre-vingts ; et cent soixante. "
        "{b1.3}Observé et attendu coïncident : la population est à l'équilibre.",
        "{-b1}{b2}Une deuxième population : cinq cents A A, deux cents A m, trois cents m m. "
        "{b2.1}Calcule p : mille plus deux cents, sur deux mille. Encore zéro virgule six ! Même fréquence allélique.",
        "{b2.2}Donc on attend les mêmes effectifs : trois cent soixante, quatre cent quatre-vingts, cent soixante. "
        "{b2.3}Mais on observe beaucoup trop d'homozygotes, et pas assez d'hétérozygotes. Cette population s'écarte de l'équilibre.",
        "Une des conditions du modèle n'est pas respectée. Par exemple, des accouplements qui ne se font pas au hasard, entre individus apparentés : "
        "ils produisent plus d'homozygotes.",
        "{-b2}{lecon}La leçon : {lecon.1}une fréquence allélique ne suffit pas. Deux populations peuvent avoir le même p. "
        "C'est la comparaison des fréquences génotypiques, observées et attendues, qui révèle l'écart.",
        "{-lecon}",
    ], vis={
        "meth": dict(type="liste", titre="Tester l'équilibre de Hardy-Weinberg", items=[
            "Calculer p et q à partir des effectifs observés", "Calculer les effectifs attendus : p² × N, 2pq × N, q² × N",
            "Comparer observé et attendu, puis conclure"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "b1": dict(type="illu", nom="barres", x=170, y=100, w=940, h=540, obs=[360, 480, 160], att=[360, 480, 160], max=520,
                   titre="Population 1 · N = 1 000 · p = 0,6", verdict="observé = attendu : à l'équilibre", ok=True),
        "b2": dict(type="illu", nom="barres", x=170, y=100, w=940, h=540, obs=[500, 200, 300], att=[360, 480, 160], max=520,
                   titre="Population 2 · N = 1 000 · p = (1 000 + 200) / 2 000 = 0,6",
                   verdict="trop d'homozygotes, pas assez d'hétérozygotes : écart à l'équilibre", ok=False),
        "lecon": dict(type="note", titre="La leçon", cles=["suffit", "comparaison"],
                      t="Une fréquence allélique ne suffit pas : c'est la comparaison des fréquences génotypiques observées et attendues qui révèle l'écart.",
                      x=170, y=220, w=940),
    }),

    # ================================================================ les conditions
    dict(id="conditions", chap="Les conditions du modèle", fond="foret", humeur="calme",
         retenir="Le modèle n'est valable que pour une population très grande, panmictique, isolée, sans sélection ni mutation : c'est une référence.",
         beats=[
        "{cond}Le modèle prévoit la stabilité des fréquences. Mais seulement sous certaines conditions, diapositives onze et douze. "
        "{cond.1}Une population de taille infinie, en pratique très grande. "
        "{cond.2}Une espèce diploïde, à reproduction sexuée. "
        "{cond.3}La panmixie : les croisements se font au hasard. "
        "{cond.4}Une population isolée : aucune migration, donc aucun flux de gènes. "
        "{cond.5}Pas de sélection naturelle. {cond.6}Pas de mutation. "
        "{cond.7}Et pas de croisements entre générations : elles ne se chevauchent pas.",
        "{-cond}{panm}Arrêtons-nous sur un mot savant : {panm.1}la panmixie. Elle recouvre trois idées. "
        "L'équiprobabilité des gamètes, qu'on appelle la pangamie ; des accouplements aléatoires, sans préférence entre partenaires ; "
        "et une ségrégation aléatoire des allèles dans les gamètes, lors de la méiose.",
        "{-panm}{ref}Tu le vois : aucune population réelle ne remplit toutes ces conditions. "
        "{ref.1}Il est pour ainsi dire presque impossible qu'une population réelle soit à l'équilibre.",
        "{ref.2}Alors à quoi sert le modèle ? C'est une {!référence}. Quand une population s'en écarte, c'est qu'une force agit sur elle. "
        "Et l'écart permet de la rechercher. Comme un thermomètre : on ne s'intéresse pas au trente-sept degrés, mais à la fièvre.",
        "{-ref}",
    ], vis={
        "cond": dict(type="liste", titre="Les conditions du modèle (diapositives 11 et 12)", petit=True, items=[
            "Population de taille infinie (en pratique, très grande)", "Espèce diploïde, à reproduction sexuée",
            "Panmixie : croisements au hasard", "Population isolée : pas de migration, pas de flux de gènes",
            "Pas de sélection naturelle", "Pas de mutation", "Pas de croisements entre générations"],
            marques=["1", "2", "3", "4", "5", "6", "7"], x=170, y=96, w=940),
        "panm": dict(type="def", terme="Panmixie", cles=["hasard"],
                     t="Les croisements se font au hasard : gamètes équiprobables (pangamie), accouplements aléatoires, ségrégation aléatoire des allèles à la méiose.",
                     etape="Le contraire : des préférences entre partenaires, ou des accouplements entre apparentés.", x=170, y=190, w=940),
        "ref": dict(type="liste", titre="À retenir", items=[
            "Presque aucune population réelle n'est à l'équilibre",
            "Le modèle sert de référence : un écart révèle une force qui agit"], marques=["!", "→"], x=150, y=210, w=980),
    }),

    # ================================================================ les causes d'écart
    dict(id="ecarts", chap="Pourquoi les populations réelles s'écartent", fond="foret", humeur="tension",
         retenir="Chaque condition non respectée donne une cause d'écart : ce sont les forces évolutives.",
         beats=[
        "{cau}La diapositive treize pose la question : à partir des conditions du modèle, qu'est-ce qui peut expliquer un écart dans la réalité ? "
        "Chaque condition non respectée donne une cause.",
        "{cau.1}Pas de mutation ? Dans la réalité, des mutations apparaissent et créent de nouveaux allèles. Tu l'as vu en Première : "
        "les mutations sont la source de la variabilité.",
        "{cau.2}Population isolée ? Il y a des migrations, des flux de gènes : de nouvelles variations arrivent, ou une partie de la population part et s'isole. "
        "Des barrières naturelles peuvent aussi séparer une partie de la population du reste.",
        "{cau.3}Pas de sélection ? Un changement de climat ou d'environnement modifie les conditions de survie, donc la sélection naturelle. "
        "L'arrivée d'une nouvelle espèce, en compétition pour les mêmes ressources, joue le même rôle.",
        "{cau.4}Accouplements au hasard ? Il existe des préférences sexuelles : la reproduction ne se fait pas au hasard.",
        "{cau.5}Population infinie ? La population peut être toute petite. Et alors, le hasard de la reproduction pèse énormément.",
        "{-cau}{fe}Ces causes d'écart ont un nom : {fe.1}les {!forces évolutives}. Elles sont l'objet de la deuxième branche de la carte. "
        "Mais avant, entraîne-toi : deux exercices sur Hardy-Weinberg.",
        "{-fe}",
    ], vis={
        "cau": dict(type="liste", titre="Condition non respectée → ce qui se passe (diapositive 14)", petit=True, items=[
            "Absence de mutations → des mutations créent de nouveaux allèles",
            "Population isolée → migrations, flux de gènes ; barrières naturelles",
            "Absence de sélection → changement de climat, d'environnement, nouvelle espèce concurrente",
            "Panmixie → préférences sexuelles : reproduction non aléatoire",
            "Taille infinie → petite population : le hasard pèse beaucoup"], marques=["1", "2", "3", "4", "5"], x=130, y=110, w=1020),
        "fe": dict(type="def", terme="Forces évolutives", cles=["écart"],
                   t="Les causes d'écart à l'équilibre de Hardy-Weinberg : mutations, migrations, sélection naturelle, reproduction non aléatoire, dérive dans les petites populations.",
                   x=170, y=210, w=940),
    }),

    # ================================================================ exercice 1 (simple)
    # 250 papillons : 160 A//A, 80 A//m, 10 m//m → 2N = 500 ; A = 320 + 80 = 400 ; p = 0,8 ; q = 0,2
    # attendus : 0,64 × 250 = 160 ; 0,32 × 250 = 80 ; 0,04 × 250 = 10 → à l'équilibre
    dict(id="exo1", chap="Exercice 1 · pour démarrer", fond="foret", humeur="calme", beats=[
        "{ex1}Premier exercice. Une population de deux cent cinquante papillons compte cent soixante individus A A, quatre-vingts A m, et dix m m. "
        "Trois questions : la fréquence des deux allèles ; les effectifs attendus à l'équilibre ; et la conclusion.",
        "{-ex1}{pa1}Prends une feuille. Mets la vidéo sur pause, et applique la méthode en trois étapes.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Correction. {s11}{s11.1}Deux cent cinquante individus : cinq cents exemplaires du gène. "
        "{s11.2}Allèles A : deux fois cent soixante, plus quatre-vingts : quatre cents. "
        "{s11.3}p égale quatre cents sur cinq cents, zéro virgule huit. Et q, zéro virgule deux.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Effectifs attendus. A A : p au carré, zéro virgule soixante-quatre, fois deux cent cinquante : cent soixante. "
        "{s12.2}A m : deux p q, zéro virgule trente-deux, fois deux cent cinquante : quatre-vingts. "
        "{s12.3}m m : q au carré, zéro virgule zéro quatre, fois deux cent cinquante : dix. "
        "{s12.4}Vérification : zéro virgule soixante-quatre, plus zéro virgule trente-deux, plus zéro virgule zéro quatre : un.",
        "{-s12}{ex1c.q3}{s13}{s13.1}Conclusion : les effectifs observés, cent soixante, quatre-vingts et dix, sont égaux aux effectifs attendus. "
        "{s13.2}La population est à l'équilibre de Hardy-Weinberg. Ses fréquences devraient rester constantes, tant que les conditions du modèle sont respectées.",
        "{-s13}{-ex1c}",
    ], vis={
        "ex1": dict(type="exo", niveau="simple", titre="Des papillons à l'équilibre ?", src="Exercice inventé pour la vidéo",
                    enonce=["Une population de 250 papillons compte 160 individus de génotype (A//A), 80 de génotype (A//m) et 10 de génotype (m//m)."],
                    questions=["Calculer les fréquences p et q des allèles A et m.",
                               "Calculer les effectifs attendus si la population est à l'équilibre de Hardy-Weinberg.",
                               "La population est-elle à l'équilibre ? Conclure."]),
        "pa1": dict(type="pause", t="p et q, effectifs attendus, conclusion."),
        "ex1c": dict(type="exo", mode="coin", niveau="simple", titre="Des papillons à l'équilibre ?",
                     donnees=["N = 250", "160 A//A · 80 A//m · 10 m//m"], questions=["p et q ?", "Effectifs attendus ?", "Équilibre ?"]),
        "s11": dict(type="formule", titre="1 · Les fréquences alléliques", x=540, y=150, w=700, lignes=[
            dict(f="2N = 500", taille=36), dict(f="A : 2 × 160 + 80 = 400", taille=36),
            dict(f="p = " + fr("400", "500") + " = 0,8  ·  q = 0,2", cadre=True, taille=38)]),
        "s12": dict(type="formule", titre="2 · Les effectifs attendus", x=540, y=120, w=700, lignes=[
            dict(f="A//A : p² × N = 0,64 × 250 = 160", taille=32), dict(f="A//m : 2pq × N = 0,32 × 250 = 80", taille=32),
            dict(f="m//m : q² × N = 0,04 × 250 = 10", taille=32), dict(f="0,64 + 0,32 + 0,04 = 1", ok=True, taille=30)]),
        "s13": dict(type="formule", titre="3 · Conclusion", x=540, y=170, w=700, lignes=[
            dict(f="observés : 160 · 80 · 10 = attendus", taille=34),
            dict(f="population à l'équilibre de Hardy-Weinberg", cadre=True, ok=True, taille=32)]),
    }),

    # ================================================================ exercice 2 (difficile)
    # 400 escargots : 160 A//A, 80 A//m, 160 m//m → A = 320 + 80 = 400 / 800 → p = q = 0,5
    # attendus : 0,25 × 400 = 100 ; 0,5 × 400 = 200 ; 100 → 240 hétérozygotes attendus en plus de ceux observés : 120 manquent
    dict(id="exo2", chap="Exercice 2 · plus difficile", fond="foret", humeur="tension", beats=[
        "{ex2}Deuxième exercice, plus difficile. Dans une population de quatre cents escargots, on compte cent soixante A A, quatre-vingts A m, et cent soixante m m. "
        "On demande : p et q ; les effectifs attendus à l'équilibre ; si la population est à l'équilibre ; "
        "et enfin, quelle condition du modèle n'est sans doute pas respectée, et pourquoi.",
        "{-ex2}{pa2}La dernière question demande de raisonner, pas seulement de calculer. Mets sur pause.",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Correction. {s21}{s21.1}Huit cents exemplaires du gène. "
        "{s21.2}Allèles A : trois cent vingt plus quatre-vingts, quatre cents. {s21.3}p vaut zéro virgule cinq, et q aussi.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Attendus : p au carré, zéro virgule vingt-cinq, fois quatre cents : cent A A. "
        "{s22.2}Deux p q, zéro virgule cinq, fois quatre cents : deux cents A m. {s22.3}Et cent m m.",
        "{-s22}{ex2c.q3}{b3}{b3.1}{b3.2}{b3.3}On compare : on attendait deux cents hétérozygotes, on n'en observe que quatre-vingts. "
        "Et soixante homozygotes de trop, de chaque côté. La population n'est pas à l'équilibre.",
        "{-b3}{ex2c.q4}{s24}{s24.1}Quelle condition ? Le déficit d'hétérozygotes et l'excès d'homozygotes, c'est la signature d'une reproduction non aléatoire. "
        "{s24.2}Par exemple, des accouplements entre individus semblables, ou entre individus apparentés : la panmixie n'est pas respectée. "
        "{s24.3}Attention à la rédaction : on propose une hypothèse. Le calcul montre un écart ; il ne prouve pas, à lui seul, sa cause.",
        "{-s24}{-ex2c}",
    ], vis={
        "ex2": dict(type="exo", niveau="difficile", titre="Des escargots trop homozygotes", src="Exercice inventé pour la vidéo",
                    enonce=["Une population de 400 escargots compte 160 individus (A//A), 80 individus (A//m) et 160 individus (m//m)."],
                    questions=["Calculer p et q.", "Calculer les effectifs attendus à l'équilibre de Hardy-Weinberg.",
                               "La population est-elle à l'équilibre ?",
                               "Quelle condition du modèle n'est probablement pas respectée ? Justifier."]),
        "pa2": dict(type="pause", t="p et q, attendus, comparaison, puis l'hypothèse sur la condition non respectée."),
        "ex2c": dict(type="exo", mode="coin", niveau="difficile", titre="Des escargots trop homozygotes",
                     donnees=["N = 400", "160 A//A · 80 A//m · 160 m//m"], questions=["p et q ?", "Attendus ?", "Équilibre ?", "Quelle condition ?"]),
        "s21": dict(type="formule", titre="1 · Les fréquences", x=540, y=150, w=700, lignes=[
            dict(f="2N = 800", taille=36), dict(f="A : 2 × 160 + 80 = 400", taille=36),
            dict(f="p = " + fr("400", "800") + " = 0,5  ·  q = 0,5", cadre=True, taille=38)]),
        "s22": dict(type="formule", titre="2 · Les effectifs attendus", x=540, y=150, w=700, lignes=[
            dict(f="A//A : 0,25 × 400 = 100", taille=34), dict(f="A//m : 0,50 × 400 = 200", taille=34), dict(f="m//m : 0,25 × 400 = 100", taille=34)]),
        "b3": dict(type="illu", nom="barres", x=470, y=110, w=780, h=520, obs=[160, 80, 160], att=[100, 200, 100], max=220,
                   titre="3 · Observé et attendu", verdict="80 hétérozygotes au lieu de 200 : pas à l'équilibre", ok=False),
        "s24": dict(type="formule", titre="4 · L'hypothèse", x=540, y=130, w=700, lignes=[
            dict(f="déficit d'hétérozygotes, excès d'homozygotes", taille=30),
            dict(f="reproduction non aléatoire (individus semblables ou apparentés)", cadre=True, taille=28),
            dict(f="Le calcul montre l'écart ; la cause reste une hypothèse.", txt=True, taille=24)]),
    }),

    # ================================================================ B. les forces évolutives : modéliser
    dict(id="forces", chap="Modéliser les forces évolutives", fond="cellule", humeur="mystere",
         retenir="Activité 1 : un logiciel fait se reproduire une population ; on change un paramètre à la fois et on suit les fréquences.",
         beats=[
        "{m_b}{m_b.1}Deuxième branche de la carte : les écarts à l'équilibre. La dérive génétique, l'effet fondateur, la sélection naturelle. "
        "Et n'oublie pas les deux autres forces : les mutations et les migrations.",
        "{-m_b}{q2}La question de la partie deux : {q2.1}comment les forces évolutives sont-elles à l'origine d'un écart des fréquences alléliques, "
        "par rapport à l'équilibre théorique de Hardy-Weinberg ?",
        "{-q2}{act}Pour y répondre, l'activité un utilise un logiciel. {act.1}Il simule une population, et la fait se reproduire génération après génération. "
        "{act.2}On change un seul paramètre à la fois : la taille de la population, des mutations, des accouplements non aléatoires, "
        "ou un caractère plus avantageux. {act.3}Et on suit les fréquences sur une dizaine de générations, parce que les écarts s'observent dans le temps.",
        "{-act}{gr_s1}Les courbes que tu vas voir sont des simulations qui reproduisent les scénarios de l'activité. "
        "La classe n'a pas reçu de courbe corrigée : ce sont des résultats attendus, proposés. "
        "{gr_s1.1}Scénario un, le témoin : mille individus, deux allèles à cinquante pour cent, pas de mutation, rencontres au hasard. "
        "La fréquence reste très proche de zéro virgule cinq, avec de toutes petites fluctuations. Aucun allèle ne disparaît.",
        "Dans une grande population, les conditions du modèle sont presque réunies : les fréquences restent à peu près constantes. Gardons ce témoin en tête.",
        "{-gr_s1}",
    ], vis={
        "m_b": dict(type="mental", vers=["c3", "c3b"]),
        "q2": dict(type="def", terme="La question de la partie II", cles=["écart"],
                   t="Comment les forces évolutives sont-elles à l'origine d'un écart des fréquences alléliques par rapport à l'équilibre théorique de Hardy-Weinberg ?",
                   x=170, y=200, w=940),
        "act": dict(type="liste", titre="Activité 1 · le principe", items=[
            "Un logiciel simule une population qui se reproduit, génération après génération",
            "On change un seul paramètre : taille, mutations, accouplements, avantage d'un caractère",
            "On suit les fréquences sur une dizaine de générations"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "gr_s1": gr_freq("Scénario 1 · le témoin : 1 000 individus (simulation)", [(S1, "sa", "1 000 individus", [5.2, .62])]),
    }),

    # ================================================================ la dérive génétique
    dict(id="derive", chap="La dérive génétique", fond="cellule", humeur="tension",
         retenir="Dérive génétique : évolution aléatoire des fréquences, due au hasard de la reproduction, d'autant plus forte que la population est petite.",
         beats=[
        "{gr_s2}Scénario deux : seulement neuf individus, deux allèles à cinquante pour cent, onze générations. Et on lance le logiciel deux fois. "
        "{gr_s2.1}Premier lancement : la fréquence fait des bonds, et l'allèle finit fixé, à un. L'autre a disparu.",
        "{gr_s2.2}Deuxième lancement, exactement les mêmes conditions : cette fois, l'allèle disparaît. "
        "Deux résultats opposés, avec le même point de départ. Rien n'a favorisé un allèle plutôt que l'autre : c'est le hasard.",
        "{-gr_s2}{d_der}C'est la {!dérive génétique}. {d_der.1}Un phénomène d'évolution aléatoire, dû au hasard de la reproduction et de la descendance. "
        "Et elle est beaucoup plus forte sur une petite population.",
        "{-d_der}{d9}Le schéma de la diapositive vingt le montre. {d9.1}Une population de neuf individus. "
        "{d9.2}À la première génération, seuls cinq individus se reproduisent, et ils n'ont pas le même nombre de descendants : deux, un, un, un et trois. "
        "Quatre individus ne laissent aucun descendant : leurs allèles sont perdus pour la génération suivante.",
        "{d9.3}La deuxième génération ne compte plus que huit individus, et les couleurs ne sont plus dans les mêmes proportions. "
        "{d9.4}La troisième en compte dix. {d9.5}Au bout de dix générations, la composition allélique est impossible à prévoir.",
        "{-d9}{expl}Pourquoi ? Voici l'explication de Madame Philip, diapositive quarante-six. "
        "{expl.1}Dans une petite population, les allèles n'ont pas tous la même probabilité de se transmettre. "
        "{expl.2}Pour qu'un individu transmette à coup sûr tous ses allèles, il faudrait que son nombre de descendants tende vers l'infini. "
        "{expl.3}Il est donc statistiquement inévitable que certains allèles ne soient transmis à aucun enfant. "
        "{expl.4}Le nombre des allèles fluctue énormément : certains se retrouvent sur-représentés, d'autres sous-représentés.",
        "{-expl}{fix}D'où deux idées à retenir. {fix.1}La dérive est d'autant plus forte que la population est petite. "
        "{fix.2}Et elle peut aller jusqu'à la {!fixation} d'un allèle, fréquence un, et la disparition de l'autre. "
        "{fix.3}La fiche de l'activité ajoute : la dérive peut appauvrir la diversité génétique, et même faire disparaître une population. "
        "À l'inverse, elle peut contribuer à l'apparition d'une nouvelle espèce. On y reviendra.",
        "{-fix}",
    ], vis={
        "gr_s2": gr_freq("Scénario 2 · la dérive : 9 individus, deux lancements (simulation)",
                         [(S2a, "sa", "lancement 1 : fixé", [7.2, .93]), (S2b, "or", "lancement 2 : perdu", [7.2, .1])], gens=11),
        "d_der": dict(type="def", terme="Dérive génétique · diapositive 20", cles=["aléatoire", "petite"],
                      t="Un phénomène d'évolution aléatoire, dû au hasard de la reproduction et de la descendance. Elle est beaucoup plus forte sur une petite population.",
                      x=170, y=200, w=940),
        "d9": dict(type="illu", nom="derive9", x=110, y=96, w=1060, h=560),
        "expl": dict(type="liste", titre="L'explication (diapositive 46)", petit=True, items=[
            "Dans une petite population, les allèles n'ont pas tous la même probabilité de se transmettre",
            "Transmettre à coup sûr tous ses allèles : il faudrait une infinité de descendants",
            "Il est statistiquement inévitable que certains allèles ne soient transmis à aucun enfant",
            "Les nombres d'allèles fluctuent : sur-représentés, sous-représentés"], marques=["1", "2", "3", "4"], x=130, y=120, w=1020),
        "fix": dict(type="liste", titre="À retenir", items=[
            "Plus la population est petite, plus la dérive est forte",
            "Elle peut fixer un allèle (fréquence 1) et faire disparaître l'autre",
            "Elle appauvrit la diversité… et peut contribuer à une nouvelle espèce"], marques=["1", "2", "3"], x=150, y=180, w=980),
    }),

    # ================================================================ Buri
    dict(id="buri", chap="Les drosophiles de Buri", fond="cellule", humeur="mystere",
         retenir="Buri, 1956 : 107 populations de 16 drosophiles, toutes à 0,5 au départ ; après 19 générations, bw75 fixé ou perdu dans beaucoup d'entre elles. C'est la dérive.",
         beats=[
        "{tab_dro}Le cas réel du cours : la drosophile, la petite mouche du vinaigre des laboratoires de génétique. "
        "{buri_p}En mille neuf cent cinquante-six, le chercheur Peter Buri met en place cent sept populations, selon le même protocole. "
        "{buri_p.1}Chaque population compte au départ seize mouches, toutes hétérozygotes pour la mutation brown eye : génotype bw75 sur bw. "
        "Huit mâles, huit femelles. {buri_p.2}La fréquence de l'allèle bw75 vaut donc zéro virgule cinq dans toutes les populations.",
        "{buri_p.3}À chaque génération, huit mâles et huit femelles sont pris au hasard parmi les descendants pour former la génération suivante. "
        "{buri_p.4}Et l'expérience dure dix-neuf générations.",
        "{-buri_p}{-tab_dro}{hb}Voici ce que cela donne. L'histogramme compte les populations selon leur fréquence de bw75. "
        "Je l'ai reproduit par simulation, avec le protocole de Buri : ce ne sont pas ses chiffres exacts, mais le phénomène est le même. "
        "{hb.1}Au départ, les cent sept populations sont toutes au même endroit, à zéro virgule cinq.",
        "Génération après génération, les fréquences s'étalent. Certaines populations montent, d'autres descendent. "
        "Et bientôt, des populations atteignent les bords : zéro, ou un. Une fois au bord, elles n'en bougent plus : il n'y a plus qu'un seul allèle.",
        "{hb.2}À la fin de l'expérience, l'histogramme a la forme d'un U. {hb.3}De nombreuses populations ont fixé l'allèle bw75, et de nombreuses autres l'ont perdu, "
        "à peu près autant dans un sens que dans l'autre.",
        "{-hb}{exb}L'explication. {exb.1}Les cent sept populations ont été traitées exactement de la même façon. "
        "{exb.2}Et la couleur des yeux ne change pas la survie des mouches en élevage : il n'y a pas de sélection. "
        "{exb.3}Si les fréquences ont divergé, c'est par le seul hasard du tirage des reproducteurs, dans de très petites populations de seize individus : c'est la dérive génétique. "
        "{exb.4}Son résultat est imprévisible pour une population donnée, mais il conduit souvent à la fixation ou à la perte d'un allèle.",
        "{-exb}",
    ], vis={
        "tab_dro": dict(type="tableau", img="ch3-drosophile", fond=True, sombre=True, de=[1.0, .55, .45], a=[1.25, .5, .45],
                        legende="Drosophila melanogaster, photo André Karwath, CC BY-SA 2.5"),
        "buri_p": dict(type="liste", titre="Le protocole de Buri (1956)", items=[
            "107 populations de 16 drosophiles, toutes hétérozygotes bw75//bw (8 mâles, 8 femelles)",
            "Au départ, f(bw75) = 0,5 dans toutes les populations",
            "À chaque génération : 8 mâles et 8 femelles tirés au hasard parmi les descendants",
            "19 générations"], marques=["1", "2", "3", "4"], x=130, y=150, w=1020),
        "hb": dict(type="illu", nom="buri", x=150, y=86, w=980, h=580, hist=BURI, max=25),
        "exb": dict(type="liste", titre="L'explication", items=[
            "Même protocole pour les 107 populations", "La couleur des yeux ne change pas la survie : pas de sélection",
            "Le seul hasard du tirage, dans des populations de 16 : la dérive génétique",
            "Imprévisible pour une population, mais souvent fixation ou perte"], marques=["1", "2", "3", "4"], x=150, y=150, w=980),
    }),

    # ================================================================ l'effet fondateur
    dict(id="fondateur", chap="L'effet fondateur", fond="cellule", humeur="lumiere",
         retenir="Effet fondateur : une petite population fondatrice n'emporte qu'un échantillon non représentatif des allèles ; la dérive s'y ajoute.",
         beats=[
        "{gr_s3}Retour à l'activité, scénario trois : neuf individus encore, mais des fréquences de départ inégales, vingt pour cent pour le premier allèle. "
        "{gr_s3.1}Le plus souvent, l'allèle rare est perdu en quelques générations. {gr_s3.2}Mais par hasard, il peut aussi augmenter.",
        "{-gr_s3}{d_fond}Ce scénario modélise l'{!effet fondateur}. {d_fond.1}Une petite sous-population se sépare de la population initiale, par exemple lors d'une migration. "
        "Elle n'emporte qu'un échantillon non représentatif, tiré au hasard, des allèles de la population mère. "
        "{d_fond.2}Ses fréquences alléliques peuvent donc être très différentes.",
        "{-d_fond}{ifo}Regarde. {ifo.1}Une grande population, avec trois allèles. "
        "{ifo.2}Huit individus partent coloniser un nouveau milieu. Par hasard, ils ne portent aucun allèle violet.",
        "{ifo.3}Compare les fréquences : la population fondatrice n'a pas du tout la composition de départ. Un allèle a disparu d'un coup, sans aucune sélection. "
        "{ifo.4}Puis la colonie s'accroît. Elle reste petite, et la dérive génétique continue d'agir, d'autant plus fort que la population est petite.",
        "{-ifo}{cause}La cause de l'écart, diapositive quarante-huit : {cause.1}la population fondatrice ne représente qu'un échantillon non représentatif des allèles de départ : "
        "ils n'y sont pas en proportions équiprobables. {cause.2}Et le plus souvent, s'y ajoute une reproduction non aléatoire : "
        "les membres d'une petite communauté isolée se reproduisent entre eux.",
        "{-cause}",
    ], vis={
        "gr_s3": gr_freq("Scénario 3 · effet fondateur : 9 individus, 20 % au départ (simulation)",
                         [(S3a, "or", "lancement 1 : perdu", [5.5, .1]), (S3b, "sa", "lancement 2 : par hasard, il monte", [3.4, .9])], gens=11),
        "d_fond": dict(type="def", terme="Effet fondateur · diapositive 47", cles=["échantillon", "non", "représentatif"],
                       t="Une petite sous-population se sépare de la population initiale. Elle n'emporte qu'un échantillon non représentatif, tiré au hasard, des allèles de la population mère.",
                       etape="Ses fréquences peuvent être fort différentes ; l'écart est d'autant plus grand qu'elle est petite, et la dérive s'y ajoute.",
                       x=170, y=170, w=940),
        "ifo": dict(type="illu", nom="fondateur", x=90, y=96, w=1100, h=560),
        "cause": dict(type="liste", titre="La cause de l'écart (diapositive 48)", items=[
            "Un échantillon non représentatif des allèles de départ",
            "Une reproduction non aléatoire : une petite communauté isolée se reproduit en son sein"], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ Amish et Huttérites
    dict(id="amish", chap="Les Amish et les Huttérites", fond="cellule", humeur="calme",
         retenir="Amish : syndrome d'Ellis-van Creveld, q = 0,07, toutes les familles descendent d'un même couple d'immigrants. C'est l'effet fondateur.",
         beats=[
        "{tab_am}Premier cas humain : les Amish de Pennsylvanie, une communauté d'origine européenne installée en Amérique du Nord, qui vit à l'écart et se marie en son sein. "
        "{evc}Chez eux, un syndrome est relativement fréquent : {evc.1}le syndrome d'Ellis-van Creveld, une forme de nanisme accompagnée de doigts surnuméraires. "
        "Cette précision médicale ne vient pas du diaporama.",
        "{evc.2}La fréquence de l'allèle en cause atteint q égal zéro virgule zéro sept, alors que la maladie est exceptionnelle dans le reste du monde. "
        "{evc.3}Dans toutes les familles amish étudiées, la mutation est la même. Et on a pu démontrer que toutes ces familles descendaient d'un même couple d'immigrants.",
        "{-evc}{-tab_am}{ham}Le tableau de la diapositive vingt-neuf, d'après McLellan et ses collaborateurs, en mille neuf cent quatre-vingt-sept, "
        "compare trois groupes : les Européens et Américains, les Huttérites, autre communauté d'origine européenne, et les Amish. "
        "{ham.1}Groupe sanguin A : vingt-cinq à trente-deux pour cent en Europe ; trente-cinq chez les Huttérites ; soixante-six chez les Amish !",
        "{ham.2}L'allèle H L A A onze, un marqueur des groupes tissulaires : quatre virgule cinq à sept virgule quatre pour cent en Europe ; zéro chez les Huttérites, il a disparu ; "
        "quatorze chez les Amish. {ham.3}Et le groupe Kell : trois à cinq pour cent en Europe ; quatorze chez les Huttérites ; zéro virgule deux chez les Amish.",
        "{-ham}{exa}Ce qu'on observe : {exa.1}les deux communautés s'écartent fortement de la population européenne dont elles sont issues, et elles diffèrent aussi entre elles. "
        "Un allèle peut y être absent, ou bien plus fréquent qu'ailleurs.",
        "{exa.2}L'explication : chaque communauté a été fondée par un petit nombre d'immigrants, qui n'emportaient qu'un échantillon non représentatif des allèles européens. "
        "C'est l'effet fondateur. {exa.3}Ensuite, ces communautés vivent isolées et se marient entre elles : une reproduction non aléatoire. "
        "Et leur petite taille renforce la dérive génétique. Trois mécanismes, qui s'additionnent.",
        "{-exa}",
    ], vis={
        "tab_am": dict(type="tableau", img="ch3-amish", fond=True, sombre=True, de=[1.0, .7, .5], a=[1.2, .68, .5],
                       legende="Buggy amish sur une route de Pennsylvanie, photo Ad Meskens, CC BY-SA 3.0"),
        "evc": dict(type="liste", titre="Les Amish de Pennsylvanie", items=[
            "Syndrome d'Ellis-van Creveld : nanisme, doigts surnuméraires (précision hors diaporama)",
            "Fréquence de l'allèle : q = 0,07 ; maladie exceptionnelle ailleurs",
            "Même mutation dans toutes les familles : un même couple d'immigrants"], marques=["1", "2", "3"], x=130, y=150, w=1020),
        "ham": dict(type="illu", nom="amish", x=150, y=100, w=980, h=540),
        "exa": dict(type="liste", titre="Ce qu'on observe, et pourquoi", petit=True, items=[
            "Les deux communautés s'écartent de l'Europe, et diffèrent entre elles",
            "Effet fondateur : peu d'immigrants, un échantillon non représentatif",
            "Reproduction non aléatoire + petite taille (dérive)"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ le groupe O
    dict(id="groupeo", chap="Le groupe O des Amérindiens", fond="cellule", humeur="mystere",
         retenir="Groupe O : 90 à 100 % chez les Amérindiens. Explication proposée : un effet fondateur à l'échelle d'un continent, puis la dérive.",
         beats=[
        "{obs_o}Deuxième cas, diapositive trente et un : une carte de la proportion de personnes de groupe sanguin O dans les populations autochtones du monde. "
        "{obs_o.1}Elle est élevée presque partout : souvent cinquante à soixante-dix pour cent. "
        "{obs_o.2}Mais chez les populations amérindiennes, elle atteint quatre-vingt-dix à cent pour cent. En Amérique, presque tout le monde est de groupe O.",
        "{-obs_o}{ber}La diapositive laisse la case de l'explication à remplir. Voici une explication possible, proposée sur le site. "
        "{ber.1}En Asie, les trois allèles A, B et O sont présents. "
        "{ber.2}L'Amérique a été peuplée par un petit nombre d'individus venus d'Asie, par la Béringie. "
        "Ce groupe fondateur portait, par hasard, une proportion très élevée de l'allèle O.",
        "{ber.3}Puis la dérive génétique a pu faire disparaître les allèles A et B dans plusieurs populations. "
        "C'est un effet fondateur à l'échelle d'un continent.",
        "{-ber}",
    ], vis={
        "obs_o": dict(type="liste", titre="Groupe sanguin O · diapositive 31", items=[
            "Dans le monde : souvent 50 à 70 % des personnes", "Chez les Amérindiens : 90 à 100 %"],
            marques=["◐", "●"], x=150, y=200, w=980),
        "ber": dict(type="illu", nom="beringie", x=90, y=96, w=1100, h=560),
    }),

    # ================================================================ la sélection naturelle
    dict(id="selection", chap="La sélection naturelle", fond="foret", humeur="lumiere",
         retenir="Sélection naturelle : les génotypes au meilleur succès reproducteur dans un milieu donné voient leurs allèles augmenter. Valeur sélective : 1 au maximum.",
         beats=[
        "{d_sel}Troisième force : la {!sélection naturelle}. {d_sel.1}Elle favorise les individus dont le génotype confère, dans un milieu donné, "
        "un meilleur taux de survie et de reproduction. Ils laissent plus de descendants, et la fréquence de leurs allèles augmente, génération après génération.",
        "{-d_sel}{vs}On la mesure par la valeur sélective. {vs.1}C'est la probabilité qu'un génotype se transmette à la descendance. "
        "{vs.2}Elle vaut un pour le génotype au succès reproducteur maximal. "
        "{vs.3}Et si tous les génotypes ont la même valeur sélective, la population n'est pas soumise à la sélection naturelle.",
        "{-vs}{tab_ph}L'exemple de la fiche d'activité : la phalène du bouleau. Sur des troncs noircis, la forme noire est moins visible. "
        "Elle est moins chassée par ses prédateurs, et elle laisse plus de descendants.",
        "{-tab_ph}{gr_s4}Scénario quatre de l'activité, avec un autre logiciel, celui de l'académie de Nice : "
        "le génotype A A a une valeur sélective de un ; A B et B B, zéro virgule huit. "
        "{gr_s4.1}La fréquence de A augmente régulièrement. Elle tend vers la fixation. "
        "{gr_s4.2}Et quand on relance, on obtient presque la même courbe.",
        "Voilà la grande différence avec la dérive : le résultat se répète d'un lancement à l'autre. "
        "La sélection fait évoluer les fréquences dans une direction donnée : celle de l'allèle favorable dans ce milieu.",
        "{-gr_s4}",
    ], vis={
        "d_sel": dict(type="def", terme="Sélection naturelle", cles=["survie", "reproduction", "augmente"],
                      t="Elle favorise les individus dont le génotype confère, dans un milieu donné, un meilleur taux de survie et de reproduction : la fréquence de leurs allèles augmente.",
                      x=170, y=200, w=940),
        "vs": dict(type="liste", titre="La valeur sélective", items=[
            "Probabilité qu'un génotype se transmette à la descendance", "Elle vaut 1 pour le génotype au succès reproducteur maximal",
            "Même valeur sélective pour tous : pas de sélection naturelle"], marques=["1", "2", "3"], x=150, y=180, w=980),
        "tab_ph": dict(type="tableau", img="ch3-phalenes", de=[1.0, .5, .5], a=[1.12, .5, .5],
                       legende="Phalène du bouleau, forme claire et forme noire (carbonaria), photos Olaf Leillinger, CC BY-SA 2.5"),
        "gr_s4": gr_freq("Scénario 4 · sélection : A//A = 1 ; A//B = B//B = 0,8 (simulation)",
                         [(S4a, "sa", "lancement 1", [6.4, .8]), (S4b, "te", "lancement 2", [1.2, .9])]),
    }),

    # ================================================================ Culex pipiens
    dict(id="culex", chap="Culex pipiens et les insecticides", fond="foret", humeur="tension",
         retenir="Culex pipiens : l'insecticide trie les larves ; AceR augmente tant que le milieu le favorise. L'allèle préexistait : pas de finalisme.",
         beats=[
        "{tab_cu}Le cas réel du cours : les moustiques Culex pipiens du Languedoc-Roussillon. "
        "{ctx}{ctx.1}Depuis mille neuf cent soixante-huit, on les contrôle en épandant des insecticides sur les étendues d'eau où se développent les larves. "
        "Ce sont surtout des organophosphorés, qui tuent les larves en perturbant certaines synapses.",
        "{ctx.2}Le gène Ace existe sous deux allèles. AceR confère une résistance aux organophosphorés, mais il ralentit aussi le développement des moustiques. "
        "AceS ne protège pas. {ctx.3}Dans les années quatre-vingt-dix, les quantités épandues ont été fortement réduites, et un autre insecticide a été employé, le téméphos.",
        "{-ctx}{-tab_cu}{gr_cu}Le graphique du manuel, redessiné ici dans son allure, pour la population un. "
        "{gr_cu.1}La fréquence de AceR reste proche de zéro jusqu'au début des années quatre-vingt. "
        "Puis elle augmente rapidement, jusqu'à environ zéro virgule six au milieu des années quatre-vingt-dix. Ensuite, elle se stabilise.",
        "{-gr_cu}{itr}Le mécanisme. {itr.1}Dans l'eau, les larves porteuses de AceR sont rares. "
        "{itr.2}On épand l'insecticide. {itr.3}Les larves sensibles meurent ; les résistantes survivent. "
        "{itr.4}Elles seules se reproduisent : à la génération suivante, AceR est bien plus fréquent. L'insecticide exerce une {!pression de sélection}.",
        "{-itr}{cout}Mais pourquoi la courbe s'arrête-t-elle vers zéro virgule six ? {cout.1}Parce que l'allèle a un coût : un développement plus lent. "
        "Sans insecticide, il désavantage ses porteurs. {cout.2}Son avantage dépend donc du milieu. Quand l'usage d'insecticide diminue, sa progression s'arrête.",
        "{-cout}{fin_c}Et un piège de rédaction, très important. {fin_c.1}Jamais de finalisme. "
        "Un moustique ne devient pas résistant « pour » survivre. L'allèle AceR existait déjà, apparu par mutation. L'insecticide a trié les porteurs. "
        "{fin_c.2}C'est le même raisonnement que pour les bactéries résistantes aux antibiotiques, vues en Première : l'antibiotique ne crée pas la résistance, il élimine les sensibles.",
        "{-fin_c}",
    ], vis={
        "tab_cu": dict(type="tableau", img="ch3-culex", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.2, .5, .42],
                       legende="Culex pipiens, photo gbohne, CC BY-SA 2.0"),
        "ctx": dict(type="liste", titre="Culex pipiens en Languedoc-Roussillon", petit=True, items=[
            "Depuis 1968 : insecticides organophosphorés sur les eaux où vivent les larves",
            "Gène Ace : AceR résiste mais ralentit le développement ; AceS ne protège pas",
            "Années 1990 : bien moins d'insecticide, et un autre produit, le téméphos"], marques=["1", "2", "3"], x=130, y=150, w=1020),
        "gr_cu": dict(type="graphe", titre="Fréquence de AceR, population 1 (allure du graphique du manuel, redessinée)", x=280, y=110, w=720, h=520,
                      ax=dict(x=[1965, 2002], y=[0, 1], gx=[1970, 1980, 1990, 2000], gy=[.25, .5, .75, 1], lx="années", ly="f(AceR)"),
                      el=[dict(type="courbe", pts=[list(p) for p in CULEX], c="or", lbl="AceR", lp=[1995, .7], dur=3.2)]),
        "itr": dict(type="illu", nom="tri", x=110, y=96, w=1060, h=560),
        "cout": dict(type="liste", titre="Un avantage qui dépend du milieu", items=[
            "AceR a un coût : un développement plus lent", "Moins d'insecticide : sa progression s'arrête"], marques=["−", "→"], x=150, y=200, w=980),
        "fin_c": dict(type="note", titre="Jamais de finalisme", cles=["existait", "trié"],
                      t="Le moustique ne devient pas résistant « pour » survivre : l'allèle AceR existait, apparu par mutation ; l'insecticide a trié les porteurs.",
                      etape="Même raisonnement que les bactéries résistantes aux antibiotiques (Première).", x=170, y=200, w=940),
    }),

    # ================================================================ dérive ou sélection ?
    dict(id="comparer", chap="Dérive ou sélection ?", fond="foret", humeur="calme",
         retenir="Dérive : hasard, imprévisible, petites populations. Sélection : orientée par le milieu, reproductible, quelle que soit la taille.",
         beats=[
        "{dvs}Un tableau à savoir refaire, parce qu'on te demandera souvent de reconnaître la force en jeu. "
        "{dvs.g}À gauche, la dérive génétique, et l'effet fondateur qui lui est lié. Sa cause : le hasard de la reproduction. "
        "Sa direction : aléatoire, imprévisible. Deux populations identiques évoluent différemment. Elle est forte dans les petites populations. "
        "Exemples : les drosophiles de Buri, les Amish, le groupe O des Amérindiens.",
        "{dvs.1}À droite, la sélection naturelle. Sa cause : un avantage de survie ou de reproduction dans un milieu donné. "
        "Sa direction : orientée. L'allèle favorable augmente, et l'expérience est reproductible. Elle agit quelle que soit la taille de la population. "
        "Exemples : Culex pipiens et les insecticides, la phalène du bouleau.",
        "{-dvs}{reflexe}Le réflexe pour un document : {reflexe.1}si des populations identiques divergent dans tous les sens, sans rapport avec le milieu, c'est la dérive. "
        "{reflexe.2}Si un allèle progresse là où il est avantageux, et seulement là, c'est la sélection.",
        "{-reflexe}",
    ], vis={
        "dvs": dict(type="cols", g="Dérive génétique", gq="hasard · imprévisible · forte si petite population · Buri, Amish, groupe O",
                    d="Sélection naturelle", dq="avantage dans un milieu · orientée, reproductible · toute taille · Culex, phalène",
                    vs="≠", repere="Les deux différencient les populations"),
        "reflexe": dict(type="liste", titre="Reconnaître la force sur un document", items=[
            "Populations identiques qui divergent au hasard → dérive",
            "Un allèle qui progresse là où il est avantageux → sélection"], marques=["?", "?"], x=150, y=200, w=980),
    }),

    # ================================================================ C. la notion d'espèce : histoire
    dict(id="espece", chap="Qu'est-ce qu'une espèce ?", fond="aube", humeur="calme",
         retenir="De Linné (espèces fixes) à Darwin (espèces apparentées qui se transforment). Critères phénotypique, biologique, moléculaire : aucun ne suffit seul.",
         beats=[
        "{m_c}{m_c.1}Troisième branche de la carte : la notion d'espèce. C'est le bilan du chapitre : "
        "si les fréquences des allèles changent sans cesse, qu'est-ce qu'une espèce ?",
        "{-m_c}{p_lin}Pour les naturalistes d'avant la théorie de l'évolution, comme Linné au dix-huitième siècle, l'inventeur du nom scientifique en deux mots, genre et espèce, "
        "une espèce est un ensemble d'individus semblables, qui engendrent des individus semblables à eux. Elle est fixe, créée telle quelle.",
        "{-p_lin}{p_dar}Au dix-neuvième siècle, Darwin introduit une relation de parenté entre les espèces. "
        "La variabilité des individus, triée par la sélection naturelle, fait que les espèces se transforment au cours du temps, "
        "et qu'elles dérivent d'ancêtres communs.",
        "Et tout ce chapitre te donne les mécanismes de cette transformation, que Darwin ne connaissait pas : la dérive, l'effet fondateur, la sélection, "
        "qui changent les fréquences des allèles.",
        "{-p_dar}",
        "{crit}Comment décider que deux individus appartiennent à la même espèce ? Trois critères, et chacun a ses limites. "
        "{crit.1}Le critère phénotypique, la ressemblance. C'est le plus simple, mais il trompe. "
        "Deux papillons d'aspect très différent peuvent être le mâle et la femelle d'une même espèce : c'est le dimorphisme sexuel.",
        "Un exemple qui n'est pas dans ton cours : l'aurore, un papillon blanc de nos prairies. Seul le mâle a le bout des ailes orange ; la femelle n'en a pas.",
        "{crit.2}Le critère biologique, l'interfécondité : une espèce est un ensemble de populations dont les individus peuvent se reproduire entre eux, "
        "et engendrer une descendance fertile. C'est la définition de référence. Mais elle ne s'applique ni aux fossiles, "
        "ni aux organismes qui ne se reproduisent pas sexuellement. Et certaines espèces distinctes s'hybrident : l'exemple du manuel, deux espèces de canards fuligules.",
        "{crit.3}Le critère moléculaire : on compare les séquences d'ADN. Exemple du manuel : jusqu'en mille neuf cent quatre-vingt-seize, "
        "deux fourmis des bois, Formica lugubris et Formica paralugubris, étaient considérées comme une seule espèce. "
        "Les études moléculaires ont montré que ce sont deux espèces distinctes.",
        "{-crit}{aucun}Conclusion : {aucun.1}aucun critère ne suffit seul. C'est la première raison pour laquelle la notion d'espèce est délicate.",
        "{-aucun}",
    ], vis={
        "m_c": dict(type="mental", vers=["c3", "c3c"]),
        "p_lin": dict(type="portrait", img="ch3-linne", nom="Carl von Linné", dates="1707-1778", annee=1750,
                      legende="naturaliste suédois · portrait par Alexander Roslin, 1775 (domaine public)"),
        "p_dar": dict(type="portrait", img="ch3-darwin", nom="Charles Darwin", dates="1809-1882", annee=1859,
                      legende="L'Origine des espèces, 1859 · photographie vers 1874 (domaine public)"),
        "crit": dict(type="liste", titre="Trois critères, trois limites", petit=True, items=[
            "Phénotypique (ressemblance) · limite : le dimorphisme sexuel",
            "Biologique (interfécondité, descendance fertile) · limites : fossiles, reproduction asexuée, hybrides (fuligules)",
            "Moléculaire (séquences d'ADN) · Formica lugubris et F. paralugubris, séparées en 1996"],
            marques=["1", "2", "3"], x=130, y=150, w=1020),
        "aucun": dict(type="note", titre="Aucun critère ne suffit seul", cles=["aucun"],
                      t="Aucun des trois critères ne suffit à lui seul pour délimiter une espèce.", x=170, y=230, w=940),
    }),

    # ================================================================ arbres et réseau
    dict(id="reseau", chap="Arbre des espèces, arbre des molécules, réseau du vivant", fond="aube", humeur="mystere",
         retenir="Arbre des espèces ≠ arbre des molécules (duplications, pertes, transferts). Doolittle : un réseau du vivant plutôt qu'un arbre.",
         beats=[
        "{arb}Deux sortes d'arbres. {arb.1}Un arbre des espèces représente l'histoire évolutive d'un groupe d'espèces. "
        "{arb.2}Un arbre des molécules représente l'histoire d'une famille de molécules : des gènes, des protéines.",
        "{arb.3}Les deux ne sont pas toujours identiques. Une famille de molécules peut contenir plusieurs copies d'un même gène dans une espèce : des duplications. "
        "Un gène peut avoir été perdu dans une lignée. Et des molécules peuvent avoir été transférées horizontalement, d'une espèce à une autre. "
        "Tu reconnais le chapitre deux.",
        "{-arb}{ires}Ces transferts compliquent beaucoup la classification. {ires.1}Un arbre suppose que les branches ne se croisent jamais. "
        "{ires.2}Or, dans les années mille neuf cent quatre-vingt-dix, le séquençage des génomes de bactéries a révélé qu'elles avaient échangé un très grand nombre de gènes. "
        "La comparaison de ces gènes n'indique plus alors la parenté entre les espèces, mais la période où chaque gène a été transféré.",
        "{-ires}{cit_d}Le chercheur canadien William Ford Doolittle en tire une conclusion radicale.",
        ("C", "Vouloir construire un arbre du vivant n'a pas de sens.", "cit_d"),
        "{-cit_d}{ires2}{ires2.1}{ires2.2}{ires2.3}Il propose un réseau du vivant, où les espèces sont reliées en plusieurs points, à chaque transfert de gènes.",
        "{-ires2}",
    ], vis={
        "arb": dict(type="liste", titre="Deux arbres", items=[
            "Arbre des espèces : l'histoire évolutive d'un groupe d'espèces",
            "Arbre des molécules : l'histoire d'une famille de gènes ou de protéines",
            "Ils diffèrent : duplications, pertes de gènes, transferts horizontaux"], marques=["1", "2", "≠"], x=150, y=170, w=980),
        "ires": dict(type="illu", nom="reseau", x=170, y=110, w=940, h=540),
        "cit_d": dict(type="cit", t="Vouloir construire un arbre du vivant n'a pas de sens.", a="William Ford Doolittle",
                      o="cité dans le cours", x=170, y=230, w=940),
        "ires2": dict(type="illu", nom="reseau", x=170, y=110, w=940, h=540),
    }),

    # ================================================================ Denisova
    dict(id="denisova", chap="Denisova : une espèce identifiée par son ADN", fond="roche", humeur="mystere",
         retenir="Denisova : une phalange et une molaire ; leur ADN révèle une forme humaine distincte des sapiens et des Néandertaliens.",
         beats=[
        "{meth_d}Aujourd'hui, on peut rattacher un spécimen à une espèce grâce à son ADN. {meth_d.1}On place la séquence d'un gène indicateur dans un arbre phylogénétique, "
        "construit avec les séquences de ce même gène chez les espèces connues, stockées dans des bases de données librement accessibles. "
        "{meth_d.2}On montre ainsi que le spécimen appartient à une espèce connue, ou bien qu'il s'agit d'une espèce nouvelle pour la science.",
        "{-meth_d}{tab_den}Cette technique a précisé l'histoire du genre Homo. On dispose du génome complet de plusieurs Néandertaliens, et d'un très grand nombre de sapiens. "
        "Et de l'ADN extrait d'une phalange et d'une molaire, trouvées dans la grotte de Denisova, en Sibérie.",
        "{-tab_den}{iden}L'arbre de la diapositive quarante-quatre. {iden.1}D'un côté, les sapiens actuels : San, Yoruba, Français, Han, Papous. "
        "{iden.2}De l'autre, les Néandertaliens de Mezmaiskaya et de Vindija. "
        "{iden.3}Et Denisova se place à côté des Néandertaliens, à l'écart des sapiens.",
        "Les données moléculaires confortent l'idée que Néandertaliens et humains modernes forment deux espèces différentes. "
        "Et elles révèlent une autre forme humaine, les Dénisoviens, dont l'ADN est distinct à la fois de celui des sapiens et de celui des Néandertaliens. "
        "Alors qu'on ne connaît presque rien de sa morphologie : une phalange, une molaire.",
        "{-iden}{hp_d}La diapositive conclut que cet ADN n'a pas fini de remettre en question la notion d'espèces distinctes. "
        "{hp_d.1}Voici pourquoi. Ce qui suit est hors programme. Sapiens, Néandertaliens et Dénisoviens se sont reproduits entre eux. "
        "Les humains actuels hors d'Afrique portent un à quatre pour cent d'ADN néandertalien, et certaines populations d'Océanie jusqu'à cinq pour cent d'ADN dénisovien. "
        "Selon le critère d'interfécondité, ce ne seraient donc pas des espèces totalement séparées.",
        "{-hp_d}",
    ], vis={
        "meth_d": dict(type="liste", titre="Identifier un spécimen par son ADN", items=[
            "Placer la séquence d'un gène indicateur dans un arbre construit avec les espèces connues (bases de données)",
            "Conclure : espèce connue, ou espèce nouvelle pour la science"], marques=["1", "2"], x=150, y=190, w=980),
        "tab_den": dict(type="tableau", img="ch3-denisova", de=[1.0, .5, .45], a=[1.25, .55, .4],
                        legende="Panneau vers la grotte de Denisova, Altaï (Sibérie), photo Yuriy59, CC BY-SA 3.0"),
        "iden": dict(type="illu", nom="denisova", x=150, y=100, w=980, h=540),
        "hp_d": dict(type="note", titre="Hors programme · des espèces qui se sont croisées", cles=["reproduits"],
                     t="Sapiens, Néandertaliens et Dénisoviens se sont reproduits entre eux : 1 à 4 % d'ADN néandertalien hors d'Afrique, jusqu'à 5 % d'ADN dénisovien en Océanie.",
                     etape="Selon l'interfécondité, ce ne seraient pas des espèces totalement séparées.", x=170, y=190, w=940, plus=True),
    }),

    # ================================================================ espèce en devenir
    dict(id="devenir", chap="Une espèce en devenir", fond="aube", humeur="lumiere",
         retenir="Une population suffisamment isolée génétiquement est une espèce en devenir. Les espèces sont des ensembles hétérogènes de populations, évoluant distinctement dans le temps.",
         beats=[
        "{isp}Le bilan de la diapositive quarante-cinq relie tout le chapitre. {isp.1}L'environnement est, par définition, instable. "
        "{isp.2}Imagine une population coupée en deux par une barrière.",
        "{isp.3}De chaque côté, la sélection et la dérive agissent, chacune à sa façon. Elles mènent à une différenciation génétique des populations au cours du temps.",
        "{isp.4}Conséquence possible : les populations ne peuvent plus échanger de gènes. Il n'y a plus de reproduction entre elles, "
        "car elles sont devenues trop différentes génétiquement.",
        "{-isp}{d_dev}On assiste alors à une {!espèce en devenir} : {d_dev.1}une population suffisamment isolée génétiquement des autres populations.",
        "{-d_dev}{bil}D'où la conclusion du chapitre. {bil.1}La notion d'espèce est délicate à définir. "
        "{bil.2}Les espèces sont des ensembles hétérogènes de populations, évoluant distinctement dans le temps. "
        "Retiens cette phrase telle quelle : c'est la définition qui clôt le cours.",
        "{-bil}",
    ], vis={
        "isp": dict(type="illu", nom="speciation", x=110, y=96, w=1060, h=560),
        "d_dev": dict(type="def", terme="Espèce en devenir", cles=["isolée"],
                      t="Une population suffisamment isolée génétiquement des autres populations.",
                      x=170, y=220, w=940),
        "bil": dict(type="liste", titre="Bilan (diapositive 45)", items=[
            "La notion d'espèce est délicate à définir",
            "Les espèces sont des ensembles hétérogènes de populations, évoluant distinctement dans le temps"], marques=["1", "2"], x=150, y=200, w=980),
    }),

    # ================================================================ exercice 3 (type bac)
    # 1 naissance sur 2 500 malade (m//m) : q² = 4 × 10^-4 → q = 0,02 ; p = 0,98 ; 2pq = 0,0392 ≈ 1/25,5 (≈ 1 sur 25)
    # communauté isolée : q = 0,07 → q² = 0,0049 ≈ 1 sur 204, 12 fois plus que 4 × 10^-4
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice, au format du bac. Une maladie génétique est due à un allèle récessif m : seuls les homozygotes m m sont malades. "
        "Dans une grande population, on supposera l'équilibre de Hardy-Weinberg. Une naissance sur deux mille cinq cents est atteinte.",
        "{ex3b}Cinq questions. Un : calculer q, puis p. Deux : calculer la proportion de porteurs sains, les hétérozygotes. "
        "Trois : pourquoi a-t-on besoin du modèle pour l'estimer ? "
        "Quatre : dans une petite communauté isolée, fondée par quelques couples, la fréquence de m atteint zéro virgule zéro sept. "
        "Calculer la proportion de malades attendue, et expliquer l'écart avec la grande population. "
        "Cinq : on y observe en réalité encore plus de malades que prévu. Proposer une explication.",
        "{-ex3}{-ex3b}{pa3}Vingt minutes, comme au bac. Mets sur pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Correction. {s31}{s31.1}Les malades sont les m m : leur fréquence est q au carré. "
        "{s31.2}q au carré égale un sur deux mille cinq cents, quatre fois dix puissance moins quatre. "
        "{s31.3}Donc q égale la racine carrée : zéro virgule zéro deux. Et p égale zéro virgule quatre-vingt-dix-huit.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Porteurs sains : deux p q, deux fois zéro virgule quatre-vingt-dix-huit fois zéro virgule zéro deux. "
        "{s32.2}Zéro virgule zéro trente-neuf : environ quatre pour cent, une personne sur vingt-cinq ! "
        "Cent fois plus que les malades : l'allèle se cache surtout chez des porteurs en bonne santé.",
        "{-s32}{ex3c.q3}{s33}{s33.1}Pourquoi le modèle ? Parce que les hétérozygotes ne sont pas malades : on ne peut pas les compter sur leur phénotype. "
        "{s33.2}On ne connaît que les malades, donc q au carré. Seule la loi de Hardy-Weinberg permet d'en déduire q, puis deux p q.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Dans la communauté : q au carré égale zéro virgule zéro sept au carré, zéro virgule zéro zéro quarante-neuf. "
        "{s34.2}Environ un malade sur deux cents : douze fois plus que dans la grande population. "
        "{s34.3}Explication : un effet fondateur. Les quelques couples fondateurs portaient, par hasard, l'allèle m à une fréquence élevée. "
        "Puis la petite taille de la communauté a laissé agir la dérive. C'est exactement le cas des Amish et du syndrome d'Ellis-van Creveld.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Encore plus de malades que q au carré ne le prévoit ? C'est un excès d'homozygotes. "
        "{s35.2}Dans une petite communauté isolée, on se marie entre apparentés : la reproduction n'est pas aléatoire, la panmixie n'est pas respectée. "
        "{s35.3}Les conditions du modèle ne sont pas réunies, donc la loi de Hardy-Weinberg ne s'applique pas exactement. "
        "Regard critique : le calcul de la question quatre n'était qu'une estimation.",
        "{-s35}{-ex3c}",
    ], vis={
        "ex3": dict(type="exo", niveau="bac", titre="Une maladie récessive, deux populations", src="Exercice inventé pour la vidéo, au format du bac",
                    enonce=["Une maladie génétique est due à un allèle récessif m : seuls les individus (m//m) sont malades. "
                            "Dans une grande population, supposée à l'équilibre de Hardy-Weinberg, 1 naissance sur 2 500 est atteinte."],
                    donnees=["1 malade pour 2 500 naissances", "communauté isolée : q = 0,07"]),
        "ex3b": dict(type="exo", niveau="bac", titre="Une maladie récessive · questions", y=70,
                     questions=["Calculer q, puis p.", "Calculer la proportion de porteurs sains (A//m).",
                                "Pourquoi faut-il le modèle de Hardy-Weinberg pour l'estimer ?",
                                "Communauté isolée fondée par quelques couples : q = 0,07. Proportion de malades attendue ? Expliquer l'écart.",
                                "On y observe encore plus de malades que prévu. Proposer une explication."]),
        "pa3": dict(type="pause", t="q et p, porteurs sains, rôle du modèle, la communauté isolée, l'excès de malades."),
        "ex3c": dict(type="exo", mode="coin", niveau="bac", titre="Une maladie récessive",
                     donnees=["1 malade sur 2 500", "communauté : q = 0,07"],
                     questions=["q et p ?", "Porteurs sains ?", "Pourquoi le modèle ?", "La communauté ?", "Encore plus de malades ?"]),
        "s31": dict(type="formule", titre="1 · q, puis p", x=540, y=140, w=700, lignes=[
            dict(f="malades = m//m : fréquence q²", taille=32),
            dict(f="q² = " + fr("1", "2 500") + " = 4 × 10^-4", taille=36),
            dict(f="q = √(4 × 10^-4) = 0,02  ·  p = 0,98", cadre=True, taille=34)]),
        "s32": dict(type="formule", titre="2 · Les porteurs sains", x=540, y=170, w=700, lignes=[
            dict(f="2pq = 2 × 0,98 × 0,02 ≈ 0,039", taille=36),
            dict(f="≈ 4 % : environ 1 personne sur 25", cadre=True, taille=34)]),
        "s33": dict(type="formule", titre="3 · Pourquoi le modèle ?", x=540, y=160, w=700, lignes=[
            dict(f="Les hétérozygotes ne sont pas malades : on ne peut pas les compter.", txt=True, taille=28),
            dict(f="on connaît q² → q → 2pq", cadre=True, taille=36)]),
        "s34": dict(type="formule", titre="4 · La communauté isolée", x=540, y=120, w=700, lignes=[
            dict(f="q² = 0,07² = 0,0049", taille=36),
            dict(f="≈ 1 malade sur 200 : 12 fois plus", taille=34),
            dict(f="effet fondateur, puis dérive (petite population)", cadre=True, taille=30)]),
        "s35": dict(type="formule", titre="5 · Encore plus de malades", x=540, y=120, w=700, lignes=[
            dict(f="excès d'homozygotes m//m", taille=34),
            dict(f="unions entre apparentés : pas de panmixie", cadre=True, taille=32),
            dict(f="Le modèle ne s'applique pas exactement : la question 4 n'était qu'une estimation.", txt=True, taille=24)]),
    }),

    # ================================================================ récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{bac}Voici ce que le bac peut te demander sur ce chapitre, à cocher. "
        "{bac.1}Définir une population, son patrimoine génétique, une fréquence allélique. "
        "{bac.2}Calculer des fréquences alléliques et génotypiques à partir d'effectifs. "
        "{bac.3}Établir et utiliser p au carré plus deux p q plus q au carré égale un, et tester l'équilibre en comparant observé et attendu. "
        "{bac.4}Énoncer les conditions du modèle, et en déduire les causes d'écart : les forces évolutives.",
        "{bac.5}Expliquer la dérive génétique et son lien avec la taille de la population, avec Buri. "
        "{bac.6}Expliquer l'effet fondateur, avec les Amish et le groupe O. "
        "{bac.7}Expliquer la sélection naturelle, avec Culex pipiens, sans finalisme. "
        "{bac.8}Et discuter les critères de l'espèce, jusqu'à l'espèce en devenir.",
        "{-bac}{fin_m}Revenons à la carte. {fin_m.1}Le chapitre trois tient en trois branches : un modèle sans évolution, "
        "{fin_m.2}les forces qui en écartent les populations réelles, {fin_m.3}et des espèces qui ne sont jamais figées. "
        "{fin_m.4}Le chapitre suivant ira plus loin encore : il montrera que le phénotype peut aussi se diversifier sans que le génome change.",
        "Sur le site, tu trouveras le cours écrit, le vocabulaire, les sujets de rédaction corrigés. Et maintenant, les questions du quiz, juste sous la vidéo.",
        "{-fin_m}",
    ], vis={
        "bac": dict(type="liste", titre="Pour le bac · à cocher", petit=True, items=[
            "Définir population, patrimoine génétique, fréquence allélique", "Calculer fréquences alléliques et génotypiques",
            "p² + 2pq + q² = 1 : tester l'équilibre (observé / attendu)", "Conditions du modèle → forces évolutives",
            "Dérive et taille de la population (Buri)", "Effet fondateur (Amish, groupe O)",
            "Sélection naturelle sans finalisme (Culex pipiens)", "Critères de l'espèce, espèce en devenir"],
            marques=["✓"] * 8, x=150, y=76, w=980),
        "fin_m": dict(type="mental", vers=["t1a", "c3", "c3a", "c3b", "c3c", "c4"]),
    }),
]

QUIZ = [
    dict(q="Une population de 100 individus compte 49 A//A, 42 A//m et 9 m//m. La fréquence de l'allèle A vaut…",
         r=["0,49", "0,7", "0,91"], ok=1, ex="f(A) = (2 × 49 + 42) / 200 = 140 / 200 = 0,7.", voir="f_fa"),
    dict(q="À l'équilibre de Hardy-Weinberg, la fréquence des hétérozygotes A//m vaut…", r=["pq", "2pq", "p² + q²"], ok=1,
         ex="Deux cases du tableau de croisement : A du père et m de la mère, ou l'inverse.", voir="cr"),
    dict(q="Que prédit la loi de Hardy-Weinberg ?",
         r=["Une augmentation de l'allèle dominant", "Des fréquences alléliques constantes : pas d'évolution", "La disparition des hétérozygotes"], ok=1,
         ex="p′ = p² + pq = p(p + q) = p : la fréquence ne change pas.", voir="demo"),
    dict(q="Deux populations ont la même fréquence p = 0,6. On peut en conclure qu'…",
         r=["elles sont toutes les deux à l'équilibre", "il faut comparer les effectifs observés et attendus pour conclure", "aucune n'est à l'équilibre"], ok=1,
         ex="Une fréquence allélique ne suffit pas : la population 2 (500, 200, 300) a p = 0,6 et s'écarte de l'équilibre.", voir="lecon"),
    dict(q="Laquelle de ces conditions ne fait PAS partie du modèle ?",
         r=["Une population très grande", "L'absence de mutation", "Une sélection naturelle forte"], ok=2,
         ex="Le modèle suppose l'absence de sélection naturelle.", voir="cond"),
    dict(q="Dans l'expérience de Buri, 107 populations de 16 drosophiles partent toutes à 0,5. Après 19 générations…",
         r=["toutes ont fixé bw75", "beaucoup ont fixé bw75, beaucoup l'ont perdu", "toutes sont restées à 0,5"], ok=1,
         ex="Le hasard du tirage des reproducteurs, sans sélection : c'est la dérive génétique.", voir="hb"),
    dict(q="La dérive génétique est la plus forte dans…", r=["une très grande population", "une petite population", "une population soumise à la sélection"], ok=1,
         ex="Plus la population est petite, plus il est probable que des allèles ne soient transmis à aucun descendant.", voir="fix"),
    dict(q="Pourquoi le syndrome d'Ellis-van Creveld est-il fréquent chez les Amish (q = 0,07) ?",
         r=["Parce que l'allèle est avantageux", "Par effet fondateur : toutes les familles descendent d'un même couple d'immigrants", "Parce que la mutation se produit souvent chez eux"], ok=1,
         ex="Un échantillon non représentatif au départ, puis une reproduction au sein de la communauté et la dérive.", voir="evc"),
    dict(q="Chez Culex pipiens, la fréquence de AceR augmente parce que…",
         r=["l'insecticide provoque la mutation de résistance", "l'insecticide tue les larves sensibles : les porteurs de AceR, déjà présents, laissent plus de descendants", "les moustiques apprennent à résister"], ok=1,
         ex="Pression de sélection, sans finalisme : l'allèle existait, l'insecticide trie les porteurs.", voir="itr"),
    dict(q="Selon le bilan du chapitre, une espèce en devenir est…",
         r=["une population suffisamment isolée génétiquement des autres populations", "une espèce qui vient d'apparaître dans les fossiles", "un hybride entre deux espèces"], ok=0,
         ex="Sélection et dérive différencient les populations ; si elles ne peuvent plus échanger de gènes, on parle d'espèce en devenir.", voir="d_dev"),
]

CREDITS = [
    "Photos : Drosophila melanogaster, André Karwath (CC BY-SA 2.5) ; buggy amish, Ad Meskens (CC BY-SA 3.0) ; Culex pipiens, gbohne "
    "(CC BY-SA 2.0) ; phalènes du bouleau, Olaf Leillinger (CC BY-SA 2.5) ; route de la grotte de Denisova, Yuriy59 (CC BY-SA 3.0) ; "
    "Carl von Linné par Alexander Roslin, 1775, et Charles Darwin (domaine public). Images trouvées sur Wikimedia Commons.",
    "Carte mentale d'après la carte de Mme Philip. Schémas, graphiques et simulations faits pour le site : les courbes de l'activité 1 "
    "et l'histogramme de Buri sont des simulations du protocole, pas les résultats de la classe ni ceux de Buri. Les trois exercices sont inventés pour la vidéo.",
]
